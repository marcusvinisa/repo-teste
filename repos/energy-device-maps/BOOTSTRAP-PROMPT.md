# Bootstrap Prompt — energy-device-maps (cole numa nova sessão do Claude Code)

> Copie o bloco abaixo num repositório **vazio** (com `canonical/` e `SPEC.md` deste seed) e rode numa sessão dedicada. Dirige o build pelo fluxo **spec-driven**, contrato-primeiro (schema de perfil) e fatias verticais (uma marca de ponta a ponta).

---

```
Você vai construir "energy-device-maps": um registro versionado de perfis
Modbus/SunSpec (registrador -> capacidade canônica) + biblioteca de decode/encode
+ CLI que ingere PDFs oficiais de protocolo via markitdown. Reutilizável por
qualquer gateway/edge/EMS.

ENTRADAS NESTE REPO:
- canonical/modelo-canonico.schema.json  → vocabulário de capacidades (fonte de verdade).
- canonical/mapa-canonico-capacidades.md → catálogo humano dos ids canônicos.
- SPEC.md                                 → especificação completa (formato de perfil, lib, CLI, testes).

ATIVE as skills: spec-driven-development, api-and-interface-design,
planning-and-task-breakdown, test-driven-development, incremental-implementation.

FLUXO OBRIGATÓRIO (gated):
1. SPECIFY: leia SPEC.md + canonical/. Liste premissas e confirme stack
   (recomendado Python 3.11 + pydantic + pymodbus + typer + markitdown). Pare e confirme.
2. PLAN: dependências (schema de perfil → loader/validator → codec → 1º perfil → CLI → demais perfis).
3. TASKS: fatias verticais (uma marca por vez), cada uma com aceite+verify+arquivos (máx ~5). Pare e confirme.
4. IMPLEMENT: uma tarefa por vez, TDD.

CONTRATO-PRIMEIRO:
- Defina schema/profile.schema.json (o CONTRATO do formato de perfil) ANTES de qualquer perfil.
- ids de capacidade SOMENTE do canonical/. Capacidade sem registrador = não suportada.
- NUNCA inventar endereço de registrador: faltou no doc oficial -> registrar em `gaps` com [VERIFICAR].
- Proteções regulatórias do inversor (anti-ilhamento) = read-only; a lib não as desabilita.
- Versionar o schema; não quebrar perfis existentes.

PLANO DE TAREFAS (ajuste no passo TASKS):
Fase 1 — Contrato e núcleo
  T1. schema/profile.schema.json + model.py (pydantic). Aceite: schema valida um perfil de exemplo. Verify: pytest schema.
  T2. loader.py (load+valida) + erros. Aceite: perfil inválido falha com mensagem clara.
  T3. codec.py decode(registers)->canônico. Aceite: golden fixture -> telemetria canônica correta. Verify: pytest unit.
  T4. codec.py encode(comando)->registers (+ Unsupported). Aceite: round-trip de setpoint preserva semântica.
  CHECKPOINT: contrato de perfil estável; decode/encode testados.
Fase 2 — Primeira marca vertical (GoodWe)
  T5. profiles/goodwe/et-series.yaml (telemetria essencial: pv.power, bat.soc, meter.*, inv.limit.export). Campos sem fonte = [VERIFICAR].
  T6. testes golden do perfil GoodWe (decode/encode). Aceite: passa; gaps documentados.
  CHECKPOINT: uma marca decodifica/codifica ponta-a-ponta.
Fase 3 — CLI e ingestão
  T7. cli.py validate + decode. T8. ingest.py (markitdown PDF -> rascunho com [VERIFICAR]). T9. matrix.py -> MATRIX.md.
  CHECKPOINT: CLI completa; matriz gerada.
Fase 4 — Demais marcas (repetir a fatia)
  T10..T14. Deye, Sungrow, Growatt, Huawei, Solis — perfil + golden (parciais com [VERIFICAR] onde faltar doc oficial).
  CHECKPOINT FINAL: success criteria da SPEC.md.

INGESTÃO (markitdown):
- `edmaps ingest <pdf> --vendor X --model Y` converte o doc oficial e PROPÕE um perfil-rascunho
  (heurística para tabelas de registradores), marcando tudo que não for inequívoco como [VERIFICAR].
- O rascunho SEMPRE passa por revisão humana antes de virar perfil válido. Não comitar PDFs proprietários sem licença.

BOUNDARIES:
- Always: validar contra schema; marcar [VERIFICAR]; manter source/date; respeitar proteções do inversor.
- Ask first: mudar o schema de perfil; adicionar id ao canônico.
- Never: inventar registradores; comitar PDFs proprietários; quebrar perfis existentes.

ENTREGUE: schema estável, lib decode/encode testada, CLI (validate/ingest/decode/matrix),
6 perfis prioritários (parciais ok, com gaps marcados), MATRIX.md e docs/ por fabricante.
Mantenha canonical/ imutável; novos ids propostos em docs/sugestoes-ao-canonico.md.
```

---

> **Reuso:** o formato de perfil + a lib são genéricos. Para incluir **EV chargers** (OCPP) ou **bombas** (SG-Ready/EEBus) depois, estenda o `protocol` do schema e adicione capacidades ao canônico — a estrutura não muda.
