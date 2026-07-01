# 04 · Engenharia de SOFTWARE (App + Web) — HEMS CORRENTE

> **Status:** Draft v0.1 · **2026-06-26** · Camada: Software cliente · Obedece aos contratos de `00-ARQUITETURA`.
> **Objeto:** reimplementar o equivalente ao **SEMS+ App** — monitoramento, controle, comissionamento local — + console web para operador/instalador/agregador.

## 1 · Objetivo e escopo

**Dentro:** app mobile (monitoramento, controle, comissionamento BLE local, criação de planta), web console (frota/operador/instalador/VPP), camada de protocolo cliente.
**Fora:** lógica de otimização (nuvem `03`); firmware (`02`).

## 2 · Requisitos

### Funcionais (paridade SEMS+ App — [F], fonte manual GoodWe §7)
- **Monitoramento** em tempo real do sistema (geração, consumo, bateria/SOC, rede, autoconsumo).
- **Controle/agendamento** remoto de cargas (EV, bomba SG-Ready, plugs); seleção de modo (autoconsumo / AI).
- **Comissionamento local**: descobrir e conectar ao gateway via **BLE** (+ WiFi-AP fallback), criar planta, setar parâmetros de device. *(manual: comissionamento local por Bluetooth/WiFi)*
- **Gestão de planta**: adicionar inversor/medidor/charger/plug; configurar zero-export, SG-Ready, one-touch shutdown.
- **Web console**: visão de **frota** multi-planta, saúde, e visão **agregador/VPP** (flexibilidade).

### Não-funcionais
| Parâmetro | Alvo | Origem |
|---|---|---|
| Plataformas mobile | **Android 7.0+ / iOS 15.1+** (paridade) | [F] manual GoodWe |
| Atualização tempo real | WebSocket; UI reflete em ≤ 2 s | [H] |
| Comissionamento offline | funciona **sem internet** (BLE local) | [F-decisão] paridade |
| i18n | **pt-BR** primeiro; en/es depois | [E] mercado-alvo |
| Acessibilidade | contraste/estados de erro/loading mínimos | [F] DoD `engineering-process` |

## 3 · Especificação técnica

### 3.1 Arquitetura cliente (thin-client, transport-agnostic)
Reaproveita o padrão **FieldOps** (cliente fino, envelope de mensagem transport-agnostic, descoberta de capacidade). Mesma camada de protocolo serve **nuvem (REST/WS)** e **borda (BLE GATT)**:
```
┌──────────────────────────────────────────────┐
│  App (mobile)        │  Web console (operador) │
│  ├─ Telas: dashboard, planta, cargas, config  │
│  ├─ Camada de protocolo (envelope agnóstico)  │
│  │     ├─ adapter REST/WS  → nuvem (03)        │
│  │     └─ adapter BLE GATT → borda (02) local  │
│  ├─ Provisioning seguro (PoP, sem 1234)        │
│  └─ Estado offline (cache local)               │
└──────────────────────────────────────────────┘
```
**Stacks [H]:** mobile em **React Native** ou **Flutter** (1 base p/ iOS+Android); web em **React + Tailwind**; design system v2 que você já usa. Validar RN vs Flutter por maturidade de **BLE** (comissionamento é o caminho crítico).

### 3.2 Fluxos-chave
1. **Comissionamento (instalador, offline):** app acha gateway por BLE → autentica com **PoP** (sem senha global) → seta rede WiFi/credencial → cria planta → descobre inversores/medidor por Modbus → confirma zero-export/SG-Ready.
2. **Operação (consumidor):** dashboard tempo real via WS; agenda cargas; alterna autoconsumo/AI.
3. **Frota (operador/agregador):** web console com múltiplas plantas, saúde, e seleção de ativos para flexibilidade (VPP).

### 3.3 Delta Brasil (software)
- Telas e métricas em **pt-BR** e na lógica de **compensação SCEE** (não "spot residencial"); rótulos de tarifa adequados ao BR.
- Configuração de **zero-export ANEEL** explícita no fluxo de comissionamento (não RCR).

## 4 · Interfaces
- **↔ Nuvem (`03`):** **REST** (auth, planta, device, config) + **WebSocket** (telemetria/estado). RBAC multi-tenant.
- **↔ Borda (`02`) local:** **BLE GATT** (status, set credencial/rede/planta) — mesmo envelope canônico (`00` §3).
- **Autorização:** papéis herdados de `03` §3.5 (Distribuidor → Revendedor → Instalador + operador/consumidor).

## 5 · Decisões e trade-offs
| Decisão | Opções | Veredicto |
|---|---|---|
| Framework mobile | **React Native** vs **Flutter** | decidir por **suporte BLE** (path crítico) → spike de comissionamento [H] |
| App único vs apps por papel | um app c/ modos vs apps separados (instalador × consumidor) | **um app com modos por RBAC** no v1 (menos manutenção) |
| Web console | dentro do app vs SPA separada | **SPA separada** (operador/agregador têm jornadas distintas) |
| Comissionamento | nuvem-dependente vs **BLE local** | **BLE local** — instalador em telhado sem 4G é realidade BR |

## 6 · Riscos técnicos
- **BLE entre iOS/Android**: comportamento de pareamento/permissão diverge; é o maior risco de cronograma → spike cedo.
- **Comissionamento sem internet**: garantir descoberta + criação de planta 100 % offline (paridade EzManager) antes do 1º piloto.
- **Paridade de monitoramento**: gráficos de PV/carga/bateria/rede como o SEMS+ — escopo de UI grande; faseado.
- **Segurança no cliente**: nunca embutir credencial global; PoP + rotação; não logar segredo.

## 7 · Definition of Done (Software — `engineering-process`, Frontend/Mobile)
```
[ ] Revisão de código por par
[ ] Testado em ≥2 dispositivos/navegadores target (iOS + Android reais)
[ ] Comissionamento BLE completo testado OFFLINE (sem internet)
[ ] Provisioning SEM senha default (1234 proibido) verificado
[ ] Estados de erro/loading + acessibilidade básica implementados
[ ] Tempo real (WS) refletindo telemetria da nuvem; RBAC aplicado
[ ] i18n pt-BR completo · design revisado pelo responsável de produto
[ ] Testado em staging com dados reais/equivalentes
```
