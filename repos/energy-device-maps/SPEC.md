# Spec: energy-device-maps

> Especificação spec-driven do **registro de perfis Modbus/SunSpec** + biblioteca + CLI de ingestão. Contrato-primeiro: o **schema de perfil** e o **modelo canônico** (`canonical/`) são os contratos.

## Objetivo

1. Definir um **formato único de perfil de dispositivo** (YAML) que mapeia registradores Modbus/SunSpec → **capacidades canônicas** (`canonical/`).
2. Manter um **registro versionado** de perfis por fabricante/modelo/firmware (começando por GoodWe, Deye, Sungrow, Growatt, Huawei, Solis).
3. Fornecer uma **biblioteca** que carrega um perfil e **decodifica** leituras de registradores → telemetria canônica, e **codifica** comandos canônicos → escritas de registrador.
4. Fornecer uma **CLI** que: (a) ingere o PDF oficial "Modbus protocol" via **markitdown** e gera um **perfil-rascunho**; (b) **valida** perfis contra o schema; (c) gera a **matriz de compatibilidade**.
5. Ser **reutilizável** por qualquer gateway/edge/EMS (pacote standalone).

**Usuário:** o firmware/edge da plataforma Smart e qualquer integrador que precise falar Modbus com inversores/baterias/medidores de várias marcas sem reimplementar cada mapa.

**Sucesso:** dado um perfil `goodwe/et-series.yaml`, a lib lê os registradores de um inversor real e devolve `pv.power`, `bat.soc`, etc. no canônico; e escreve `inv.limit.export` no registrador certo.

## Tech Stack `[a confirmar na sessão de build]`
- **Python 3.11** (markitdown é Python; ecossistema pymodbus; pydantic). Alternativa: Rust/Go p/ edge embarcado.
- **pydantic v2** + **jsonschema** (validação de perfil); **pymodbus** (transporte); **typer** (CLI); **pytest**.
- Perfis em **YAML** (legível, diff-friendly); schema em JSON Schema.

## Comandos `[após bootstrap]`
```
Instalar:   uv pip install -e .   (ou poetry install)
Validar:    edmaps validate profiles/**/*.yaml
Ingerir:    edmaps ingest <protocolo.pdf> --vendor goodwe --model et-series   # markitdown -> rascunho
Decode:     edmaps decode profiles/goodwe/et-series.yaml --registers dump.json
Matriz:     edmaps matrix > MATRIX.md
Testes:     pytest
```

## Estrutura de projeto
```
energy-device-maps/
├── canonical/                  # contrato canônico vendado (sincroniza da plataforma; não editar)
├── schema/
│   └── profile.schema.json     # JSON Schema do formato de perfil (CONTRATO)
├── profiles/                   # o registro, por fabricante/modelo
│   ├── goodwe/et-series.yaml
│   ├── deye/sun-sg-series.yaml
│   ├── sungrow/sh-rt-series.yaml
│   ├── growatt/min-sph-series.yaml
│   ├── huawei/sun2000.yaml
│   └── solis/s6-series.yaml
├── src/edmaps/
│   ├── model.py                # tipos do perfil (pydantic) + canônico
│   ├── loader.py               # load + valida perfil
│   ├── codec.py                # decode(registers)->canônico ; encode(comando)->registers
│   ├── ingest.py               # markitdown -> perfil-rascunho (heurística + revisão humana)
│   ├── matrix.py               # gera matriz de compatibilidade
│   └── cli.py                  # typer
├── docs/                       # ficha por fabricante (espelha integracao/template-fabricante-modbus.md)
├── tests/
└── MATRIX.md                   # gerado
```

## Contrato do perfil (formato único)
Cada perfil declara identidade, convenções e o mapeamento registrador↔capacidade canônica:
```yaml
vendor: goodwe
series: ET
models: [ET-6.0kW, ET-10kW]            # [VERIFICAR cobertura]
firmware_min: "<a confirmar>"
protocol: modbus-rtu                    # modbus-rtu | modbus-tcp | sunspec
unit_id: 247
serial: { baud: 9600, format: "8N1" }
conventions: { endianness: big, word_swap: false }
sunspec: { supported: partial, models: [1, 103, 124] }   # se aplicável
source: { file: "fontes/goodwe-modbus-v1.x.md", version: "1.x", date: "YYYY-MM-DD" }
registers:
  - canonical: inv.ac.power      # id do mapa canônico
    address: 0x0##               # [VERIFICAR no doc oficial]
    type: s32
    scale: 1
    unit: W
    access: R
    fn: 3
  - canonical: bat.power.setpoint
    address: 0x0##
    type: s16
    scale: 1
    unit: W
    access: W
    fn: 16
    notes: "sinal +carrega/-descarrega"
enums:
  inv.workmode: { 0: self-use, 1: feed-in-priority }
gaps: ["registrador X não documentado [VERIFICAR]"]
```
Regras: ids **somente** do `canonical/`; capacidade sem registrador = não suportada por aquele modelo; nunca inventar endereço (faltou → `gaps`/`[VERIFICAR]`); proteções regulatórias do inversor (anti-ilhamento) são **read-only** — a lib não as desabilita.

## API da biblioteca (contrato-primeiro)
```python
load_profile(vendor, model) -> Profile           # valida contra schema
decode(profile, registers: dict) -> list[TelemetrySample]   # canônico
encode(profile, command: Command) -> list[RegisterWrite]    # raises Unsupported
capabilities(profile) -> list[Capability]
```

## Testing Strategy
- **Unit:** `codec.decode/encode` com fixtures de registradores → canônico (golden) por perfil.
- **Schema:** todo perfil em `profiles/**` valida contra `schema/profile.schema.json` (CI).
- **Ingest:** `ingest` sobre um markdown de exemplo gera rascunho com campos esperados marcados `[VERIFICAR]`.
- **Round-trip:** encode→decode de um setpoint preserva semântica.
- Cobertura mínima 85% em `codec.py` e `loader.py`.

## Boundaries
- **Always:** validar perfil contra schema; marcar lacunas `[VERIFICAR]`; manter `source`/`date` por perfil; respeitar proteções do inversor (read-only).
- **Ask first:** mudar o schema de perfil (contrato); adicionar capacidade nova ao canônico.
- **Never:** inventar endereços de registrador; comitar PDFs proprietários sem licença; quebrar perfis existentes ao mudar o schema (versionar).

## Success Criteria
- [ ] `schema/profile.schema.json` estável e validando em CI.
- [ ] 6 perfis prioritários (mesmo que parciais, com `[VERIFICAR]`) válidos.
- [ ] `decode`/`encode` testados por golden files.
- [ ] CLI `ingest/validate/decode/matrix` funcionando; `MATRIX.md` gerado.
- [ ] Pacote utilizável standalone por um gateway (sem a plataforma Smart).

## Open Questions
- Linguagem (Python p/ tooling vs Rust/Go p/ rodar no edge embarcado) — talvez **lib de perfis em dados (YAML) + dois leitores** (Python p/ tooling, leitor leve no firmware).
- Distribuir perfis como pacote, submódulo git, ou feed versionado?
- Cobertura SunSpec automática (quando o device é SunSpec-compliant, dispensar mapa proprietário).
