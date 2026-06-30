# Spec: energy-connectors

> Especificação spec-driven do serviço de **conectores cloud-to-cloud** multimarca. Contrato-primeiro. O contrato canônico (`canonical/`) é a fonte de verdade do vocabulário.

## Objetivo

Construir um serviço/biblioteca que:
1. Conecta-se às **nuvens de fabricantes** de energia via suas APIs oficiais.
2. **Normaliza** leitura (telemetria) e escrita (comandos) para o **modelo canônico** (`canonical/modelo-canonico.schema.json`).
3. Expõe **uma API REST única** independente de marca, com matriz de capacidades por fabricante/modelo.
4. É **reutilizável** fora da plataforma Smart (pacote/serviço standalone).

**Usuário:** a plataforma Smart cloud e quaisquer integradores/terceiros que precisem ler/controlar ativos de múltiplas marcas sem implementar cada API.

**Sucesso:** dado um ativo de marca suportada, um cliente lê `pv.power`/`bat.soc` e (onde permitido) envia `bat.power.setpoint`/`inv.limit.export` **sem saber** qual fabricante está por trás.

## Fabricantes-alvo (ordem de prioridade)
GoodWe (SEMS Open-API) · Deye/Solarman · Sungrow (iSolarCloud) · Growatt · Huawei (FusionSolar) · Solis (SolisCloud). Demais (SolarEdge, Fronius, Enphase, Tesla) em fase posterior. Capacidade real de **controle** varia — declarar por conector (muitos só leem).

> **Primeiro conector = GoodWe.** Referência oficial: **https://openapi.goodwe.com/#/api/doc-10a71afe72c271** (GoodWe Developer Platform). Cobrir os **3 tipos**: **OpenAPI** (dados de negócio, HTTPS, ~3600 req/h), **Real-time Data** (raw/Kafka, sem controle) e **Batch Remote Control** (Kafka, controle → VPP/microgrid). A doc é uma SPA — extrair endpoints/campos na sessão de build a partir da página oficial.

## Tech Stack `[a confirmar na sessão de build]`
- **TypeScript + Node 20 + Fastify** (API + tipagem forte + OpenAPI nativo). Alternativa: Python/FastAPI.
- **Zod** para validação de entrada/saída (inclusive **respostas de fabricantes = dados não confiáveis**).
- **OpenAPI 3.1** gerado a partir dos schemas.
- Fila/retry: BullMQ/Redis (rate-limit por fabricante).
- Testes: Vitest + nock (mock de APIs externas).

## Comandos `[após bootstrap]`
```
Instalar:  pnpm install
Dev:       pnpm dev
Build:     pnpm build
Testes:    pnpm test
Lint:      pnpm lint --fix
OpenAPI:   pnpm openapi:gen   # gera openapi.yaml a partir dos schemas
```

## Estrutura de projeto
```
energy-connectors/
├── canonical/                 # contrato canônico vendado (NÃO editar aqui; sincroniza da plataforma)
├── src/
│   ├── core/                  # modelo canônico (tipos), interface de conector, normalizador
│   │   ├── canonical.ts       # tipos gerados do JSON Schema
│   │   ├── connector.ts       # interface VendorConnector (contrato)
│   │   └── capabilities.ts    # matriz de capability por conector
│   ├── connectors/            # um diretório por fabricante
│   │   ├── goodwe/            (auth, listDevices, readTelemetry, writeCommand, map)
│   │   ├── deye-solarman/
│   │   ├── sungrow/
│   │   ├── growatt/
│   │   ├── huawei/
│   │   └── solis/
│   ├── api/                    # camada HTTP (rotas, validação, erros)
│   └── lib/                    # rate-limit, retry, auth/credential store
├── docs/                       # ficha por fabricante (espelha integracao/template-fabricante-api.md)
├── tests/
└── openapi.yaml                # contrato público (gerado)
```

## Contrato da API (contrato-primeiro)

Erros consistentes em **todos** os endpoints: `{ error: { code, message, details? } }`. Status: 400/401/403/404/409/422/500. Listas **paginadas**. Nomes: REST plural, camelCase, enums UPPER_SNAKE.

```
POST /v1/connections                # registra credencial de uma conta de fabricante -> connectionId
GET  /v1/vendors                     # fabricantes suportados + capacidades (ler/controlar)
GET  /v1/devices?connectionId=&page= # lista dispositivos normalizados (paginado)
GET  /v1/devices/:id                 # device + capabilities canônicas
GET  /v1/devices/:id/telemetry?points=pv.power,bat.soc&from=&to=&resolution=
POST /v1/devices/:id/commands        # { point, value, ttlS?, idempotencyKey } -> 202 | 409 (não suportado)
POST /v1/webhooks                    # assina eventos (telemetria/erro/comando concluído)
```

Interface interna de cada conector (todos implementam o mesmo contrato):
```ts
interface VendorConnector {
  vendor: string;
  authenticate(creds: VendorCreds): Promise<Session>;
  listDevices(s: Session): Promise<Device[]>;            // -> modelo canônico
  readTelemetry(s: Session, deviceId: string, points: PointId[], range: TimeRange): Promise<TelemetrySample[]>;
  writeCommand(s: Session, deviceId: string, cmd: Command): Promise<CommandAck>; // throws Unsupported
  capabilities(model: string): Capability[];             // o que este modelo expõe e por onde
}
```
Regras: **validar toda resposta de fabricante** antes de usar (Zod). Conector declara o que **não** suporta (controle frequentemente indisponível). Aditivo > modificação (campos novos opcionais). One-version rule.

## Code Style
TypeScript estrito; sem `any`; erros tipados; um conector = um módulo isolado que só conhece o contrato `VendorConnector` e o canônico. Exemplo de mapeamento:
```ts
// goodwe/map.ts — traduz resposta nativa -> ponto canônico
export const toCanonical = (r: GoodweReadout): TelemetrySample[] => ([
  { point: 'pv.power', ts: r.time, value: r.pac, unit: 'W', quality: 'good', source: 'cloud-connector' },
  { point: 'bat.soc',  ts: r.time, value: r.soc, unit: '%', quality: 'good', source: 'cloud-connector' },
]);
```

## Testing Strategy
- **Unit:** cada `map.ts` (resposta fixture → canônico) e validação Zod.
- **Contrato:** cada conector contra a interface `VendorConnector` (mesmos testes para todos).
- **Integração:** API com APIs externas mockadas (nock); golden files de OpenAPI.
- Cobertura mínima 80% no `core/` e nos `connectors/*/map.ts`.

## Boundaries
- **Always:** validar respostas externas; nunca expor segredos/credenciais; testes antes de commit; controle crítico **não** é responsabilidade deste serviço (é do edge/`energy-device-maps`).
- **Ask first:** adicionar novo fabricante ao núcleo; mudar o contrato público; adicionar dependência pesada.
- **Never:** comitar credenciais de fabricante; assumir que "ler" implica "controlar"; quebrar campo existente da API.

## Success Criteria
- [ ] 6 conectores prioritários com **leitura** normalizada + matriz de capacidades publicada.
- [ ] Escrita (comando) implementada onde o fabricante permite; `409` claro onde não.
- [ ] OpenAPI 3.1 versionado e validado em CI.
- [ ] Cada conector passa o **mesmo** conjunto de testes de contrato.
- [ ] Pacote utilizável standalone (sem dependência da plataforma Smart além do `canonical/`).

## Open Questions
- Linguagem final (TS/Node vs Python/FastAPI)?
- Armazenamento de credenciais (Vault/KMS) — provido pelo host ou interno?
- Streaming (Kafka/MQTT) além de REST/webhooks na v1?
- Política de rate-limit por fabricante (ex.: GoodWe ~3600 req/h) — configurável por conector.
