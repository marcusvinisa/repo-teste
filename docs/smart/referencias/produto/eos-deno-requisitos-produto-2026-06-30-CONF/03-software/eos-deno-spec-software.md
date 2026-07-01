# EOS-DENO · Especificação de Software — Passo 3 (camada software)

> **Herdar a base. Alcançar a plataforma. Ocupar o BR e o AI-native.**
> Complementa a spec de hardware. O scoring de 16 players de software deu o mesmo padrão, deslocado: dois tetos de mercado **vazios** — **CCEE/BR (ninguém)** e **agent-fabric AI-native LLM (ninguém)** — e um **ativo já herdado** que o hardware não tinha: o **protótipo de DERMS**. A decisão que organiza tudo é **build vs. fork vs. buy por domínio**.

**A tese em uma linha:** o software do EOS-DENO é a **plataforma de energia AI-native, operada por agentes e CCEE-nativa** — montada sobre o protótipo de DERMS e fundações open-source maduras, alcançando a camada de plataforma que o mercado já provou, e ocupando os dois espaços brasileiros e de fronteira que ninguém ocupa.

**Como ler cada item:** `#` · salto de nível (hoje→alvo, do scoring) · **referência** (quem detém o teto / fundação OSS) · **build / fork / buy** · o que é / como se faz.

---

## 01 · Por que build vs. fork vs. buy é a decisão central

No hardware, "herdar" era o que o medidor já fazia. No software, o "herdar" tem três fontes: o **medidor/ingestão**, o **protótipo de DERMS**, e o **open-source maduro**. A pergunta não é "o que construir" — é **o que NÃO construir**. Open-source é fundação real em ~metade dos domínios (D1/D3/D4/D8/D11), mas **não no moat** (D7 CCEE, D9 agent-fabric). A regra: **forkar as commodities, construir os diferenciadores.**

| Veredito | Domínios | Lógica |
|---|---|---|
| **Fork / build-on OSS** | D1 Ingestão, D4 EMS, D8 Multi-tenant/API, D11 Infra | OpenEMS, ThingsBoard, stack cloud-native dão base madura. Reescrever = desperdício |
| **Build-on a matemática OSS** | D3 Inteligência | EMHASS/PyPSA/OR-Tools dão LP/MPC/forecast; produtizar p/ frota = nosso |
| **Build (com referência)** | D6 VPP/Mercado, D10 UX | Referência de incumbente; mas a implementação é própria (+ tropicalizar) |
| **Build puro — moat** | **D7 CCEE/BR, D9 Agent-fabric** | Sem fundação OSS, sem incumbente no BR. É onde o time deve estar |

---

## 02 · Herdar — a base já existente (medidor + DERMS + OSS)

| # | Capacidade | Nível | Referência | Build/Fork/Buy | O que é / como se faz |
|---|---|---|---|---|---|
| 02.1 | Ingestão & medidor (D1) | 3–4 · manter | medidor próprio + OpenEMS/ThingsBoard | herdar + fork | Ingestão de telemetria via **medidor próprio + edge** (do mapa de hardware); drivers agnósticos. Build-on connectors do OpenEMS/ThingsBoard |
| 02.2 | **Protótipo de DERMS (D5)** | 2 · consolidar | **ativo próprio** | herdar | **Já existe** — o ponto de partida mais forte do software. Orquestração de frota; consolidar para escala e tropicalizar |
| 02.3 | Fundações OSS | — · adotar | OpenEMS, ThingsBoard, EMHASS, k8s | fork | Adotar o que o open-source já resolveu: EMS (OpenEMS), IoT/multi-tenant (ThingsBoard), otimização (EMHASS/PyPSA), infra (stack cloud-native). Corta meses de trabalho não-diferenciado |

---

## 03 · Alcançar — a plataforma que o mercado já provou

| # | Capacidade | Nível | Referência | Build/Fork/Buy | O que é / como se faz |
|---|---|---|---|---|---|
| 03.1 | Inteligência: forecast + otimização (D3) | 0 → 4 | Kraken/AutoGrid/gridX · EMHASS/PyPSA | build-on math | Forecast (físico+ML) alimenta otimizador **MILP/MPC**. Build-on a matemática OSS (EMHASS/HiGHS/PyPSA); o trabalho próprio é **produtizar e escalar para frota** |
| 03.2 | EMS completo (D4) | 1 → 4 | **OpenEMS** · Eniris | **fork forte** | Forkar **OpenEMS** (EMS edge+backend, Apache 2.0, agnóstico) e estender com nossas estratégias/guardrails. A base de EMS mais madura do OSS |
| 03.3 | VPP / Mercado (D6) | 0 → 4 | Kraken/AutoGrid/Next Kraftwerke · OpenADR | build | Agregação + **bidding** em mercados; sinalização DR via OpenADR/OpenLEADR. Implementação própria, tropicalizada |
| 03.4 | Multi-tenant / API / ecossistema (D8) | 1 → 4 | gridX/Kiwigrid/ThingsBoard | build-on infra | **Multi-tenancy + API gateway + white-label**; build-on ThingsBoard (multi-tenant) + Keycloak (identidade) + Kong (API) |
| 03.5 | Apps / UX (D10) | 1 → 4 | **Zerofy/Tibber**/HA | build (ref) | App por persona + **API aberta** (padrão Tibber). UX autopilot (lição do Zerofy). Implementação própria |
| 03.6 | Infra / Sec / MLOps (D11) | 1 → 4 | stack cloud-native OSS | build-on | k8s + observability (Prometheus/Grafana) + MLOps (MLflow) + segurança (Vault, LGPD/SOC2). Padrão cloud-native |

---

## 04 · Ocupar — os dois espaços vazios (BR + AI-native)

| # | Capacidade | Nível | Referência | Build/Fork/Buy | O que é / como se faz |
|---|---|---|---|---|---|
| 04.1 | **CCEE / Liquidação / Billing BR (D7)** | 2 → 4 | **ninguém** | **build puro** | Integração com **medição/contabilização/liquidação da CCEE**, **rateio de créditos de GD compartilhada** (Lei 14.300), settlement no ACL, billing de energia. Sem fundação OSS, sem incumbente — **o fosso** |
| 04.2 | **Agent-fabric AI-native (D9)** | 0 → 4 | Volttron (paradigma) · frameworks LLM | **build (inspirado)** | **Runtime de agentes LLM por persona** + tool registry + copilot operacional + guardrails. Volttron dá o paradigma de agentes (clássicos); o runtime LLM moderno é build. Ninguém tem ainda |

---

## 05 · Arquitetura de software — três decisões

| Decisão | O quê | Por quê |
|---|---|---|
| **1 · Microsserviços modulares → bundles por persona** | Cada domínio é serviço(s) micro; persona/cenário ativa um subconjunto | Personaliza o produto **sem reescrevê-lo** (CON@A0 = bundle mínimo; CON@C5 = bundle completo). É o que você pediu |
| **2 · Fork OSS nas commodities, build nos diferenciadores** | Fork OpenEMS/ThingsBoard/stack cloud-native (D1/D4/D8/D11); build D7/D9 | Investir o time onde está o moat, não em trabalho não-diferenciado |
| **3 · Multi-tenant + cloud-edge + agent-fabric desde a fundação** | Tenant-aware desde o dia 1; controle no edge; agentes por persona | Comercializadora/integrador/agregador são tenants; resiliência no edge; operação AI-native nasce na arquitetura |

---

## 06 · Roadmap de software (ligado aos 18 cenários)

| Onda | Foco | O quê | Cenários que destrava |
|---|---|---|---|
| **M0** | herdar | Ingestão (medidor) + **protótipo DERMS** + fundações OSS escolhidas | A0/B0/C0 (monitoramento, billing, medição CCEE) |
| **M1** | alcançar núcleo | Inteligência (D3) + EMS fork-OpenEMS (D4) + multi-tenant/API (D8) + UX (D10) | A1–A4, B1–B4 (autoconsumo→load shifting, créditos) |
| **M2** | VPP + ocupar BR | VPP/mercado (D6) + **CCEE/BR (D7)** | N5 + arranjos B/C (agregação, ACL, arbitragem) — *monetização gradual conforme regulação* |
| **M3** | ocupar fronteira | **Agent-fabric AI-native (D9)** | Operação por agentes + copilot, cross-cenário |

---

## Σ · Pré-mortem — onde o software quebra

**01 · O fork de OSS vira fardo de manutenção.** Manter um fork de OpenEMS/ThingsBoard sincronizado com o upstream é custo contínuo; divergir demais perde o benefício.
→ *mitigação:* contribuir upstream, fork disciplinado, isolar customizações em camadas próprias.

**02 · "Build os diferenciadores" subestima o agent-fabric (D9).** Agent-fabric LLM é fronteira — caro, incerto, e tentador de superdimensionar. Apostar a operação nele é risco.
→ *mitigação:* agent-fabric como **camada incremental sobre serviços determinísticos**, nunca dependência crítica. Os bundles funcionam sem ele.

**03 · CCEE/BR (D7) é build puro sobre alvo móvel.** A regulação da CCEE/ACL muda; construir cedo demais pode virar retrabalho, tarde demais perde a janela.
→ *mitigação:* abstrair a camada de mercado; começar pela medição/contabilização (estável) antes do settlement (volátil).

**04 · Multi-tenant desde a fundação atrasa o MVP.** Multi-tenancy + white-label completo adiciona complexidade que pode emperrar o primeiro produto.
→ *mitigação:* **modelo de dados tenant-aware** desde o dia 1, mas adiar o ferramental completo de white-label até haver o segundo tenant.

**05 · Kraken/AutoGrid tropicalizam o BR antes (mesmo relógio do hardware).** Eles têm a plataforma completa; falta só CCEE + AI-native — que podem comprar/construir.
→ *mitigação:* velocidade no M1+M2; e o **moat duplo (CCEE + agent-fabric)** que não vem de prateleira.

---

*Sequência: herdar (medidor + DERMS + OSS) → alcançar (plataforma, com fork) → ocupar (CCEE/BR + agent-fabric). A decisão build/fork/buy por domínio é o que evita reconstruir o que o open-source já resolveu. Notas-alvo do scoring de software; referências = teto de mercado + fundação OSS. Premissas regulatórias (CCEE/ACL/VPP BT) a validar. Projeto EOS-DENO · spec de software · passo 3.*
