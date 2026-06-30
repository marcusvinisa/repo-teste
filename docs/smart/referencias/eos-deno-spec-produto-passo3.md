# EOS-DENO · Especificação do Produto Ideal — Passo 3 (hardware)

> **Estudo de referência curado pelo usuário.** Reproduzido em `referencias/`. Ver [00-absorcao-e-ajustes.md](00-absorcao-e-ajustes.md).

> **Herdar a fundação. Alcançar o software. Ocupar o Brasil.**
> O scoring dos 11 players deu um mapa cirúrgico: o Smart Pro **já lidera 3 camadas** (medição, hardware, BR) e **zera 2** (inteligência, VPP). Três movimentos em ordem crescente de esforço e risco.

**A tese em uma linha:** o EOS-DENO é o **sistema operacional de energia AI-native enraizado no medidor** — agnóstico, BR-nativo — construído sobre a fundação que já é a melhor do grupo.

---

## 01 · Por que três movimentos

| Movimento | Risco | O que é |
|---|---|---|
| **Herdar** | ~0 | A fundação que já lidera o mercado. Custo zero — manter e não estragar. |
| **Alcançar** | execução | A camada de software que 4 líderes já provaram. Caminho conhecido — mas exige times. |
| **Ocupar** | tese | O espaço BR vazio + a fronteira AI-native. Ninguém tem. Maior prêmio, maior incerteza. |

---

## 02 · Herdar — a fundação que já é a melhor do grupo

Moat que os controladores puros (EzManager, Air 2, gridX) **não têm: o sensor próprio.** Todo controlador HEMS depende de medidor externo; o EOS-DENO **é** o medidor.

| # | Capacidade | Nível | Referência | O que é / como se faz |
|---|---|---|---|---|
| 02.1 | Medição nativa Classe 1/2 | teto 3 · manter | Smart Pro detém | Mede V/I no ponto de conexão com exatidão Classe 1 — fonte de verdade. Metering IC calibrado + TCs. Nenhum controlador puro tem isso |
| 02.2 | Hardware IP65 · <5W · TFT+RGB | teto 4 · manter | Smart Pro detém | Gabinete vedado outdoor abrigado, consumo mínimo sem ventilação, display local com QR. Melhor que o IP20/LED do EzManager |
| 02.3 | Agnosticismo de fabricante | 3 → 4 | EzManager = 0 | Lê/comanda inversores de várias marcas por camada de driver que traduz cada mapa Modbus proprietário p/ canônico |
| 02.4 | Comando inversor + bateria + cargas | 2–3 → 3 | já existe | Escreve setpoints (% potência, SOC, carga/descarga) via Modbus e comanda cargas por relé/plug |
| 02.5 | Celular 4G/NB-IoT + I/O físico + OTA | teto 3 · manter | já existe | Modem celular dá autonomia sem Wi-Fi do cliente; I/O p/ comando local; flash dual-bank com rollback |
| 02.6 | BR-nativo | único · manter | nenhum dos 10 | Tensões/topologia BR, conformidade de descarte (PNRS), canal de ~5k integradores. Única fundação brasileira |

---

## 03 · Alcançar — a camada que o mercado já provou

4 líderes (gridX, Kiwigrid, Eniris, Fenecon) já provaram. Risco de **execução**, não de tese.

| # | Capacidade | Nível | Referência | O que é / como se faz |
|---|---|---|---|---|
| 03.1 | Inteligência cloud-edge (previsão + scheduling) | 0 → 4 | gridX, Kiwigrid | Previsão (ML + meteorologia) alimenta otimizador (MILP/MPC); parte roda no edge. Degrau central |
| 03.2 | Compute no edge (resiliência) | 1 → 4 | 5 já fazem | Device guarda plano e regras e opera offline; runtime leve (contêiner/WASM) |
| 03.3 | VPP / agregação | 0 → 4 | Eniris, Kiwigrid, Lifepowr | Coordena frota como recurso único; tropicalizar p/ CCEE/ONS |
| 03.4 | API aberta / white-label / multi-tenant | 1 → 4 | gridX, Kiwigrid | API (OpenAPI) + tematização por tenant + isolamento multi-tenant |
| 03.5 | Otimização por tarifa (ToU / dinâmica / BR) | 0 → 3 | Eniris, Fenecon | Otimizador ingere curva de preço (branca, bandeiras, dinâmica); modelar tarifa BR |
| 03.6 | Comando de VE + bomba de calor | 0 → 3 | todos | OCPP ajusta corrente do carregador; SG-Ready/Modbus/EEBUS desloca a bomba p/ excedente |
| 03.7 | UX autopilot + onboarding sem fricção | 2 → 4 | Zerofy | Modo padrão aplica a melhor estratégia sem configuração; dashboard em R$/CO₂ |
| 03.8 | Protocolos (Modbus-TCP, EEBUS, OCPP) | 2 → 4 | gridX, Kiwigrid | Adicionar Modbus-TCP (LAN), EEBUS (bomba/VE) e OCPP (VE) |

---

## 04 · Ocupar — o espaço brasileiro vazio

Todo VPP do mundo pesquisado está plugado em §14a/Elia/AEMO — **zero em CCEE.** Conformidade ANEEL/PRODIST/INMETRO: nenhum dos 10.

| # | Capacidade | Nível | Referência | O que é / como se faz |
|---|---|---|---|---|
| 04.1 | Conformidade ANEEL/PRODIST/INMETRO nativa | 2 → 4 | ninguém | Homologação INMETRO da medição + PRODIST + homologação na distribuidora. Fosso + armadilha de prazo |
| 04.2 | Integração CCEE / mercado livre (ACL) | 0 → 4 | vazio no BR | Medição/contabilização/liquidação CCEE + contratos do mercado livre |
| 04.3 | Agent-fabric AI-native (por persona) | 0 → 4 | fronteira 2030 | Agentes LLM por persona + copilot operacional |
| 04.4 | Liquidação automática no ACL | 0 → 4 | fronteira BR | Settlement direto no mercado livre, sem intermediário manual |

---

## 05 · Arquitetura — três decisões travadas

| Decisão | O quê | Por quê |
|---|---|---|
| **1 · Topologia desacoplada** | Medidor universal barato em toda a base + Energy Hub premium só onde há geração | O medidor é o sensor universal; o controle ativa por assinatura. Break-even vs. SKU integrado ~35% de adoção |
| **2 · Cloud-edge, não nuvem pura** | Controle crítico no edge; otimização pesada e agregação na nuvem | 5 dos 11 líderes já fazem; os que não (EzManager, Zerofy) são os mais frágeis |
| **3 · Multi-tenant + agent-fabric** | Plataforma multi-tenant desde a fundação; agentes por persona | A comercializadora é um tenant, não a dona. Operação AI-native nasce na arquitetura |

---

## 06 · Roadmap em ondas

| Onda | Foco | O quê | Destrava |
|---|---|---|---|
| **M0** | fundação | Medidor agnóstico Classe 1/2 + nuvem + assinatura + comando de inversor/bateria/cargas. **Nada a construir** | Ponto de partida com a melhor fundação |
| **M1** | alcançar EMS+IA | Escrita ampliada (VE/bomba), EMS completo (demanda/peak/tarifa), inteligência cloud-edge, API aberta, UX autopilot | Fecha unit economics do integrador/EPC |
| **M2** | VPP + ocupar BR | Agregação/VPP tropicalizada (CCEE), conformidade ANEEL/PRODIST/INMETRO, white-label multi-tenant | Destrava receita de flexibilidade no espaço BR vazio |
| **M3** | fronteira | Agent-fabric AI-native, CCEE-nativo + liquidação automática, copilot por persona | A aposta que nasce à frente do mercado |

---

## Σ · Pré-mortem — onde isto quebra

**01 · O relógio competitivo fecha a janela.** Octopus/Kraken e gridX/Kiwigrid (white-label) podem tropicalizar antes. Janela = abertura do Grupo B (2027–2028).
→ velocidade no M1+M2; o medidor-sensor como moat de dado.

**02 · "Execução conhecida" ≠ execução barata.** Inteligência cloud-edge + VPP exigem times de ML, energia e regulatório.
→ herdar a fundação libera capital/foco; o beachhead do integrador financia a onda.

**03 · Conformidade BR é fosso e armadilha.** O custo/tempo de homologação pode atrasar o M2.
→ começar a homologação cedo, em paralelo ao M1; usar a comercializadora como âncora regulada.

**04 · O VPP brasileiro pode estar vazio porque não existe.** Receita de flexibilidade no BR é **hipótese, não fato**.
→ não modelar M2 como receita certa; tratar VPP como opção regulatória.

**05 · Agnosticismo é passivo de engenharia perpétuo.** Cada firmware de inversor que muda quebra a integração.
→ driver layer disciplinada + certificação de device + priorizar marcas que cobrem 80% da base BR.

---

*Sequência: herdar (grátis) → alcançar (execução) → ocupar (aposta). Notas-alvo derivadas do scoring dos 11 players. Premissas de mercado e regulatórias a validar. Projeto EOS-DENO · passo 3.*
