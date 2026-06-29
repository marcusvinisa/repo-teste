# Bootstrap Prompt — energy-connectors (cole numa nova sessão do Claude Code)

> Copie o bloco abaixo num repositório **vazio** (com `canonical/` e `SPEC.md` copiados deste seed) e rode numa sessão dedicada do Claude Code. Ele dirige o build pelo fluxo **spec-driven** (specify→plan→tasks→implement), contrato-primeiro e fatias verticais.

---

```
Você vai construir o serviço "energy-connectors": um conector vendor-agnóstico
que integra nuvens de fabricantes de energia (GoodWe, Deye/Solarman, Sungrow,
Growatt, Huawei, Solis) e expõe UMA API REST normalizada mapeada a um modelo
canônico. Reutilizável fora de qualquer plataforma específica.

ENTRADAS NESTE REPO:
- canonical/modelo-canonico.schema.json  → contrato de dados (telemetria/dispositivos/comandos). Fonte de verdade.
- canonical/mapa-canonico-capacidades.md → catálogo humano de capacidades (ids canônicos).
- SPEC.md                                 → especificação completa (objetivo, API, estrutura, testes, boundaries).

ATIVE as skills: spec-driven-development, api-and-interface-design,
planning-and-task-breakdown, test-driven-development, incremental-implementation.

FLUXO OBRIGATÓRIO (gated — não avance sem validar):
1. SPECIFY: leia SPEC.md e canonical/. Liste premissas e confirme a tech stack
   (recomendado TypeScript+Node+Fastify+Zod; alternativa Python/FastAPI). Pare e confirme comigo.
2. PLAN: gere o grafo de dependências e a ordem (core → 1º conector → API → demais conectores).
3. TASKS: quebre em fatias verticais (uma marca de ponta a ponta por vez), cada tarefa com
   critério de aceite + verificação + arquivos (máx ~5 arquivos/tarefa). Pare e confirme.
4. IMPLEMENT: uma tarefa por vez, TDD (teste falha → implementa → passa → commit).

CONTRATO-PRIMEIRO (api-and-interface-design):
- Defina os tipos do modelo canônico a partir do JSON Schema ANTES de qualquer conector.
- Interface única VendorConnector (authenticate/listDevices/readTelemetry/writeCommand/capabilities);
  TODOS os conectores passam o MESMO conjunto de testes de contrato.
- Erros consistentes { error:{code,message,details?} }; listas paginadas; nomes REST plural/camelCase.
- VALIDE toda resposta de fabricante com Zod (dados externos = não confiáveis).
- "Ler" NÃO implica "controlar": declare capacidades por conector; 409 onde controle não é suportado.
- Aditivo > modificação; one-version rule.

PLANO DE TAREFAS (fatias verticais — ajuste no passo TASKS):
Fase 1 — Fundação
  T1. core/: tipos canônicos (do schema) + interface VendorConnector + tipos de erro. Aceite: compila, tipos cobrem telemetria/comando. Verify: pnpm build + testes de tipos.
  T2. api/: esqueleto Fastify + erro padrão + /v1/vendors (estático) + OpenAPI gen. Aceite: GET /v1/vendors responde; openapi.yaml gerado. Verify: pnpm test (rota), pnpm openapi:gen.
  T3. testes de contrato reutilizáveis (suite que qualquer conector deve passar). Aceite: suite roda contra um conector fake. 
  CHECKPOINT: build limpo, contrato definido, OpenAPI válido.
Fase 2 — Primeiro conector vertical (GoodWe)
  T4. connectors/goodwe: authenticate + listDevices (canônico). Aceite: lista devices de fixture. Verify: unit + contrato.
  T5. goodwe readTelemetry + map.ts (pv.power, bat.soc, meter.*). Aceite: fixtures → canônico corretos. Verify: unit.
  T6. goodwe writeCommand onde permitido + capabilities(model). Aceite: comando suportado→202; não suportado→Unsupported. 
  T7. fiar GoodWe na API (/v1/devices, /telemetry, /commands) + rate-limit. Aceite: e2e mockado verde.
  CHECKPOINT: uma marca funciona ponta-a-ponta pela API pública.
Fase 3 — Demais conectores (repetir a fatia por marca)
  T8..T12. Deye/Solarman, Sungrow, Growatt, Huawei, Solis — cada um: auth+list+telemetry+map (+command se houver). Aceite: passam o MESMO contrato + matriz de capacidades publicada.
Fase 4 — Acabamento
  T13. webhooks/eventos; T14. docs/ por fabricante (espelhar template-fabricante-api.md); T15. CI (lint+test+openapi).
  CHECKPOINT FINAL: success criteria da SPEC.md atendidos.

BOUNDARIES:
- Always: validar dados externos; segredos fora do repo; testar antes de commit.
- Ask first: novo fabricante no core; mudança no contrato público; dependência pesada.
- Never: comitar credenciais; assumir controle a partir de leitura; quebrar campo existente.

ENTREGUE: serviço rodando local (pnpm dev), OpenAPI versionado, 6 conectores de leitura,
matriz de capacidades, testes verdes, e docs/ por fabricante. Mantenha canonical/ imutável
(sincroniza da plataforma; proponha novos ids em docs/sugestoes-ao-canonico.md).
```

---

> **Reuso em outros projetos:** este prompt + `canonical/` + `SPEC.md` bastam. Para outro domínio canônico, troque a pasta `canonical/` e ajuste a lista de fabricantes na SPEC.
