#!/usr/bin/env python3
"""edmaps ingest — docling JSON (mapa Modbus oficial) -> perfil-rascunho YAML.

Princípios (ver SPEC.md):
- NUNCA inventa endereço. Extrai verbatim; o que não der pra mapear vira flag [VERIFICAR].
- Mapeamento SEMÂNTICO por linha (acha address/type/scale/unit/access por regex),
  robusto a desalinhamento de coluna entre páginas/continuações.
- Saída é RASCUNHO: canonical=null (o mapeamento p/ canonical/ é passo revisado à parte).
- Cada registrador carrega source {page, table} e anomalias em `verify`.

Uso:
  python ingest.py <docling.json> --vendor goodwe --source-file fontes/x.pdf \
      --out profiles/goodwe/g1.yaml --report docs/g1.anomalies.md \
      --tool "docling 2.107.0 (--no-ocr)" [--series ET] [--protocol modbus-rtu]
"""
import sys, os, re, json, argparse
import yaml

# ---- regex de campos ----
HEX4      = re.compile(r'^[`\s]*([0-9A-Fa-f]{4})\b')
HEX4_DASH = re.compile(r'^[`\s]*([0-9A-Fa-f]{4})\s*-\s*$')          # "0210 -"
HEX4_RANGE= re.compile(r'^[`\s]*([0-9A-Fa-f]{4})\s*-\s*([0-9A-Fa-f]{4})\s*$')
HEX4_ANY  = re.compile(r'\b([0-9A-Fa-f]{4})\b')
FMT       = re.compile(r'\b(INT8U|INT16U|INT16S|INT32U|INT32S|UINT16|UINT32|ASCII|Integer|BCD|FLOAT|REAL)\b', re.I)
ACCESS    = re.compile(r'^\s*(R\s*/\s*W|RW|R|W)\s*$', re.I)
UNIT      = re.compile(r'^\s*(\d*\.?\d+)?\s*(V|A|Hz|kWh|KW\.?Hr|kW|KW|Wh|W|H|s|%|Var|VA|°C|NA)\s*$', re.I)

FMT_MAP = {
    "INT8U": "u8", "INT16U": "u16", "INT16S": "s16", "INT32U": "u32", "INT32S": "s32",
    "UINT16": "u16", "UINT32": "u32", "ASCII": "string", "INTEGER": "s16",
    "BCD": "bcd", "FLOAT": "f32", "REAL": "f32",
}

FULLWIDTH = str.maketrans({"，": ",", "；": ";", "：": ":", "～": "~", "（": "(", "）": ")", "　": " "})


def norm(s):
    if s is None:
        return ""
    s = str(s).translate(FULLWIDTH)
    s = s.strip().strip("`").strip()
    s = re.sub(r"\s+", " ", s)
    return s


def cell_text(c):
    if c is None:
        return ""
    if isinstance(c, dict):
        return norm((c.get("text") or "").replace("\n", " "))
    return norm(c)


def rows_of(table):
    data = table.get("data", {})
    grid = data.get("grid")
    if grid:
        return [[cell_text(c) for c in row] for row in grid]
    nr, nc = data.get("num_rows", 0), data.get("num_cols", 0)
    g = [[""] * nc for _ in range(nr)]
    for c in data.get("table_cells", []):
        r0 = c.get("start_row_offset_idx", 0)
        c0 = c.get("start_col_offset_idx", 0)
        if r0 < nr and c0 < nc:
            g[r0][c0] = cell_text(c)
    return g


def page_of(table):
    prov = table.get("prov") or [{}]
    return prov[0].get("page_no")


def parse_unit(cell):
    m = UNIT.match(cell)
    if not m:
        return None, None
    num, unit = m.group(1), m.group(2)
    if unit.upper() == "NA":
        return None, None
    scale = float(num) if num else 1.0
    if scale == int(scale):
        scale = int(scale)
    return scale, unit


def parse_register_row(cells, page, tidx):
    """Retorna dict de registrador ou None se a linha não for um registrador."""
    cells = [c for c in cells]  # cópia
    nonempty = [c for c in cells if c]
    if not nonempty:
        return None
    c0 = cells[0] if cells else ""

    verify = []
    # --- address (+ range) ---
    addr = addr_end = words = None
    m_range = HEX4_RANGE.match(c0)
    m_dash = HEX4_DASH.match(c0)
    m_hex = HEX4.match(c0)
    if m_range:
        addr, addr_end = m_range.group(1), m_range.group(2)
    elif m_dash:
        addr = m_dash.group(1)
        # docling quebra "0210-0214": o fim aparece solto em outra célula
        for c in cells[1:]:
            mm = re.match(r'^\s*([0-9A-Fa-f]{4})\s*$', c)
            if mm and mm.group(1).upper() != addr.upper():
                addr_end = mm.group(1)
                break
        verify.append("range de endereço reconstruído (NNNN-NNNN quebrado pela extração) — conferir")
    elif m_hex:
        addr = m_hex.group(1)
    else:
        return None  # sem endereço hex no início → não é registrador

    # --- formato/tipo ---
    rtype = None
    fmt_hits = [FMT.search(c).group(1) for c in cells if FMT.search(c)]
    if fmt_hits:
        rtype = FMT_MAP.get(fmt_hits[0].upper(), None)
        if rtype is None:
            verify.append(f"Data Format desconhecido: {fmt_hits[0]}")
        if len(fmt_hits) > 1:
            verify.append(f"múltiplos tokens de formato {fmt_hits} — conferir alinhamento")
    # ASCII/string: precisa de words a partir do range
    if addr_end:
        try:
            words = int(addr_end, 16) - int(addr, 16) + 1
        except ValueError:
            pass

    # --- acesso ---
    access = None
    for c in cells:
        if ACCESS.match(c):
            a = re.sub(r"\s+", "", c).upper().replace("R/W", "RW")
            access = "RW" if a in ("RW",) else a
            break
    if access is None:
        access = "R"
        verify.append("acesso (R/W) não encontrado — assumido R, conferir")

    # --- unidade/escala ---
    scale = unit = None
    for c in cells:
        s, u = parse_unit(c)
        if u:
            scale, unit = s, u
            break

    # --- nome (1ª célula descritiva após o endereço) ---
    used = {c0}
    name = ""
    for c in cells[1:]:
        if c and not FMT.search(c) and not ACCESS.match(c) and not UNIT.match(c) and not re.match(r'^[0-9A-Fa-f]{4}$', c):
            name = c
            used.add(c)
            break

    # --- remarks: última célula descritiva não usada ---
    notes = ""
    for c in reversed(cells):
        if c and c not in used and not FMT.search(c) and not ACCESS.match(c) and not UNIT.match(c) and not re.match(r'^[0-9A-Fa-f]{4}\s*-?\s*$', c):
            notes = c
            break

    # --- range of data: célula com cara de faixa (dígitos + - ou ~) não usada ---
    rng = None
    for c in cells:
        if c in (name, notes) or c == c0:
            continue
        if re.search(r'\d', c) and re.search(r'[-~]', c) and not UNIT.match(c) and not re.match(r'^[0-9A-Fa-f]{4}', c):
            rng = c
            break

    # --- heurística de typo numérico (ex.: 0-66535 vs 65535) ---
    blob = " ".join(cells)
    if re.search(r'\b66535\b', blob):
        verify.append("valor '66535' — provável typo do PDF para 65535")

    # --- nome possivelmente quebrado por wrap (fragmentos de 1 letra) ---
    if name and re.search(r'\b[a-z]\b', name) and len(name.split()) > 2:
        verify.append("nome possivelmente com quebra de linha — conferir verbatim")

    reg = {
        "canonical": None,
        "name": name or None,
        "address": "0x" + addr.upper(),
        "type": rtype,
        "scale": scale,
        "unit": unit,
        "access": access,
        "fn": None,
        "range": rng,
        "notes": notes or None,
        "source": {"page": page, "table": tidx},
        "verify": verify,
    }
    if addr_end:
        reg["address_end"] = "0x" + addr_end.upper()
    if words:
        reg["words"] = words
    return reg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--vendor", required=True)
    ap.add_argument("--series", default="[VERIFICAR]")
    ap.add_argument("--protocol", default="modbus-rtu")
    ap.add_argument("--source-file", required=True)
    ap.add_argument("--tool", default="docling")
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    doc = json.load(open(args.json))
    tables = doc.get("tables", [])
    title = (doc.get("name") or "").strip()

    registers, seen = [], {}
    dup = []
    for tidx, t in enumerate(tables):
        pg = page_of(t)
        for row in rows_of(t):
            reg = parse_register_row(row, pg, tidx)
            if not reg:
                continue
            key = reg["address"]
            if key in seen:
                dup.append((key, seen[key], f"p{pg}/t{tidx}"))
                continue
            seen[key] = f"p{pg}/t{tidx}"
            registers.append(reg)

    # ordena por endereço
    registers.sort(key=lambda r: int(r["address"], 16))

    profile = {
        "vendor": args.vendor,
        "series": args.series,
        "protocol": args.protocol,
        "conventions": {"endianness": "big", "word_swap": False, "address_base": "hex"},
        "source": {
            "file": args.source_file,
            "title": title or None,
            "tool": args.tool,
        },
        "registers": registers,
        "gaps": [],
    }
    # remove chaves None do source
    profile["source"] = {k: v for k, v in profile["source"].items() if v is not None}

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        yaml.safe_dump(profile, f, allow_unicode=True, sort_keys=False, width=100)

    # ---- relatório de anomalias ----
    flagged = [r for r in registers if r["verify"]]
    no_type = [r for r in registers if r["type"] is None]
    no_unit = [r for r in registers if r["unit"] is None]
    os.makedirs(os.path.dirname(args.report), exist_ok=True)
    with open(args.report, "w") as f:
        f.write(f"# Relatório de ingestão — {args.vendor} / {args.source_file}\n\n")
        f.write(f"Extrator: **{args.tool}** · tabelas no doc: **{len(tables)}** · "
                f"registradores extraídos: **{len(registers)}**\n\n")
        f.write(f"- ⚠️ com flag `verify`: **{len(flagged)}**\n")
        f.write(f"- sem `type` (Data Format): **{len(no_type)}**\n")
        f.write(f"- sem `unit`: **{len(no_unit)}**\n")
        f.write(f"- endereços duplicados ignorados: **{len(dup)}**\n\n")
        if dup:
            f.write("## Endereços duplicados (ignorados — conferir)\n\n")
            for k, first, second in dup:
                f.write(f"- `{k}` visto em {first} e de novo em {second}\n")
            f.write("\n")
        f.write("## Registradores com anomalia (gate de verificação)\n\n")
        f.write("| Address | Name | type | unit | access | Flags |\n|---|---|---|---|---|---|\n")
        for r in flagged:
            flags = "; ".join(r["verify"])
            f.write(f"| `{r['address']}` | {r['name'] or ''} | {r['type'] or '—'} | "
                    f"{r['unit'] or '—'} | {r['access']} | {flags} |\n")
        f.write("\n> Revisar cada linha acima contra a imagem da página antes de mapear `canonical`.\n")

    print(f"OK: {len(registers)} registradores -> {args.out}")
    print(f"    {len(flagged)} com flag, {len(no_type)} sem type, {len(dup)} dup -> {args.report}")


if __name__ == "__main__":
    main()
