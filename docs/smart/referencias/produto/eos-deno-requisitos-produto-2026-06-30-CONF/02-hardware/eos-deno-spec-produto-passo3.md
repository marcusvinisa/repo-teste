# EOS-DENO · Especificação do Produto Ideal — Passo 3

> **Herdar a fundação. Alcançar o software. Ocupar o Brasil.**
> O scoring dos 11 players deu um mapa cirúrgico: o smart-meter **já lidera 3 camadas** (medição, hardware, BR) e **zera 2** (inteligência, VPP). A spec não é "ter tudo" — são três movimentos em ordem crescente de esforço e risco. Cada capacidade traz **número**, **salto de nível** (atual→alvo, do scoring), **referência** (quem detém o teto) e **o que é / como se faz**.

**A tese em uma linha:** o EOS-DENO é o **sistema operacional de energia AI-native enraizado no medidor** — agnóstico, BR-nativo — construído sobre a fundação que já é a melhor do grupo, alcançando a camada de software que o mercado já provou, e ocupando o espaço brasileiro que hoje está vazio.

---

## 01 · Por que três movimentos, e não um roadmap único

Misturar "o que já temos", "o que o mercado já provou" e "o que ninguém tem" num só plano esconde o que mais importa: **cada um tem risco e horizonte radicalmente diferentes.** Não se financia a aposta com a lógica do que é grátis — e não se trata o conhecido como se fosse fronteira.

| Movimento | Risco | O que é |
|---|---|---|
| **Herdar** | ~0 | A fundação que já lidera o mercado. Custo zero — manter e não estragar. |
| **Alcançar** | execução | A camada de software que 4 líderes já provaram. Caminho conhecido, replicável — mas exige times. |
| **Ocupar** | tese | O espaço BR vazio + a fronteira AI-native. Ninguém tem. Maior prêmio, maior incerteza. |

---

## 02 · Herdar — a fundação que já é a melhor do grupo

Estas capacidades o smart-meter **já tem no topo do mercado**. O trabalho é preservar e não diluir — e usar como o moat que os controladores puros (EzManager, Air 2, gridX) **não têm: o sensor próprio.** Todo controlador HEMS depende de um medidor externo; o EOS-DENO **é** o medidor.

| # | Capacidade | Nível | Referência | O que é / como se faz |
|---|---|---|---|---|
| 02.1 | Medição nativa Classe 1/2 | teto 3 · manter | smart-meter detém | Mede V/I no ponto de conexão com exatidão Classe 1 — é a fonte de verdade. Metering IC calibrado + TCs. Nenhum controlador puro tem isso; todos dependem de medidor externo |
| 02.2 | Hardware IP65 · <5W · TFT+RGB | teto 4 · manter | smart-meter detém | Gabinete vedado outdoor abrigado, consumo mínimo sem ventilação, display local com QR. Componentes grau industrial — melhor que o IP20/LED do EzManager |
| 02.3 | Agnosticismo de fabricante | 3 → 4 | EzManager = 0 | Lê/comanda inversores de várias marcas por uma camada de driver que traduz cada mapa Modbus proprietário p/ um modelo canônico. Ampliar = mais perfis testados. É onde o EzManager (murado) é zero |
| 02.4 | Comando inversor + bateria + cargas | 2–3 → 3 | já existe | Escreve setpoints (% potência, SOC, carga/descarga) via Modbus e comanda cargas por relé/plug. A base de atuação já existe; consolidar e ampliar cobertura |
| 02.5 | Celular 4G/NB-IoT + I/O físico + OTA | teto 3 · manter | já existe | Modem celular dá autonomia sem Wi-Fi do cliente; I/O permite comando local; atualização via flash dual-bank com rollback |
| 02.6 | BR-nativo | único · manter | nenhum dos 10 | Tensões/topologia da rede BR, conformidade de descarte (PNRS), canal de ~5k integradores. Única fundação brasileira entre os 11 — vantagem que estrangeiro não replica rápido |

---

## 03 · Alcançar — a camada que o mercado já provou

Aqui o smart-meter está no **chão (0)** ou abaixo do teto. A boa notícia: **4 líderes (gridX, Kiwigrid, Eniris, Fenecon) já provaram que dá.** Não é pesquisa de fronteira — é execução conhecida. Copiar o melhor de cada, tropicalizando. Risco de **execução**, não de tese.

| # | Capacidade | Nível | Referência | O que é / como se faz |
|---|---|---|---|---|
| 03.1 | Inteligência cloud-edge (previsão + scheduling) | 0 → 4 | gridX, Kiwigrid | Previsão de geração/carga (ML + meteorologia) alimenta um otimizador (MILP/MPC) que decide carga/descarga e cargas; parte roda no edge p/ latência e resiliência. Degrau central |
| 03.2 | Compute no edge (resiliência) | 1 → 4 | 5 já fazem | Device guarda plano e regras e opera offline; runtime leve (contêiner/WASM) executa a lógica localmente. Os que não fazem (EzManager/Zerofy) são os mais frágeis |
| 03.3 | VPP / agregação | 0 → 4 | Eniris, Kiwigrid, Lifepowr | Plataforma coordena a frota como recurso único e oferta a flexibilidade em mercado/serviço de rede. No BR, tropicalizar p/ CCEE/ONS — todo VPP pesquisado é §14a/Elia/AEMO |
| 03.4 | API aberta / white-label / multi-tenant | 1 → 4 | gridX, Kiwigrid | API documentada (OpenAPI) + tematização por tenant p/ parceiros entregarem como produto próprio, com isolamento multi-tenant. Exigido pela tese (comercializadora = tenant) |
| 03.5 | Otimização por tarifa (ToU / dinâmica / BR) | 0 → 3 | Eniris, Fenecon | Otimizador ingere a curva de preço (tarifa branca, bandeiras, dinâmica) e desloca consumo/armazenamento p/ janelas baratas. Modelar a estrutura tarifária BR é o ajuste local |
| 03.6 | Comando de VE + bomba de calor | 0 → 3 | todos | OCPP ajusta a corrente do carregador; SG-Ready/Modbus/EEBUS desloca a bomba p/ excedente solar (power-to-heat). Lacuna pontual do smart-meter — todos os outros já fazem |
| 03.7 | UX autopilot + onboarding sem fricção | 2 → 4 | Zerofy | Modo padrão aplica a melhor estratégia sem o usuário configurar nada; dashboard traduz kWh em R$ e CO₂. Lição do Zerofy: UX é capacidade de produto |
| 03.8 | Protocolos (Modbus-TCP, EEBUS, OCPP) | 2 → 4 | gridX, Kiwigrid | Adicionar Modbus-TCP (LAN), EEBUS (bomba/VE) e OCPP (VE) ao stack p/ cobrir mais ativos e integrar mais fácil |

---

## 04 · Ocupar — o espaço brasileiro vazio

O achado mais forte do scoring: **o teto brasileiro está vazio onde mora a receita.** Todo o VPP do mundo pesquisado está plugado em §14a/Elia/AEMO — **zero em CCEE.** Conformidade ANEEL/PRODIST/INMETRO: nenhum dos 10. Aqui o EOS-DENO não copia ninguém — ocupa um vazio e antecipa a fronteira AI-native.

| # | Capacidade | Nível | Referência | O que é / como se faz |
|---|---|---|---|---|
| 04.1 | Conformidade ANEEL/PRODIST/INMETRO nativa | 2 → 4 | ninguém | Homologação INMETRO da medição + aderência ao PRODIST + homologação na distribuidora. Fosso que estrangeiro não tem pronto — e armadilha de prazo (custo/tempo) |
| 04.2 | Integração CCEE / mercado livre (ACL) | 0 → 4 | vazio no BR | Integração com a medição/contabilização/liquidação da CCEE e gestão de contratos do mercado livre. O VPP brasileiro não existe ainda — espaço a ocupar, não a copiar |
| 04.3 | Agent-fabric AI-native (por persona) | 0 → 4 | fronteira 2030 | Agentes LLM por persona, cada um com ferramentas que leem/escrevem ativos e mercados sob políticas, + copilot operacional. Fronteira onde a tese nasce à frente |
| 04.4 | Liquidação automática no ACL | 0 → 4 | fronteira BR | Settlement direto no mercado livre, sem intermediário manual conciliando medição e contratos. Depende de integração profunda com a CCEE |

---

## 05 · Arquitetura — três decisões travadas

| Decisão | O quê | Por quê |
|---|---|---|
| **1 · Topologia desacoplada** | Medidor universal barato (smart-meter evoluído) em toda a base + Energy Hub premium só onde há geração | O medidor é o sensor universal; o controle ativa por assinatura onde paga. Break-even vs. SKU integrado ~35% de adoção |
| **2 · Cloud-edge, não nuvem pura** | Controle crítico no edge (sobrevive à queda da nuvem); otimização pesada e agregação na nuvem | Evidência do scoring: 5 dos 11 líderes já fazem; os que não (EzManager, Zerofy) são os mais frágeis |
| **3 · Multi-tenant + agent-fabric** | Plataforma multi-tenant desde a fundação; camada de agentes por persona | A comercializadora-âncora é um tenant, não a dona. A operação AI-native nasce na arquitetura |

---

## 06 · Roadmap em ondas

A ordem é a dos três movimentos: o grátis primeiro, a execução conhecida em seguida, a aposta por último. Cada onda destrava a próxima.

| Onda | Foco | O quê | Destrava |
|---|---|---|---|
| **M0** | fundação | Medidor agnóstico Classe 1/2 + nuvem + assinatura + comando de inversor/bateria/cargas. **Nada a construir** | Ponto de partida com a melhor fundação do grupo |
| **M1** | alcançar EMS+IA | Escrita de controle ampliada (VE/bomba), EMS completo (demanda/peak/tarifa), inteligência cloud-edge (previsão+scheduling), API aberta, UX autopilot | Fecha unit economics do integrador/EPC (beachhead) |
| **M2** | VPP + ocupar BR | Agregação/VPP tropicalizada (CCEE), conformidade ANEEL/PRODIST/INMETRO, white-label multi-tenant | Destrava receita de flexibilidade no espaço BR vazio |
| **M3** | fronteira | Agent-fabric AI-native, CCEE-nativo + liquidação automática, copilot operacional por persona | A aposta que nasce à frente do mercado |

---

## Σ · Pré-mortem — onde isto quebra

Não-negociável: a spec só vale com o bear case na mesa. Cinco formas de esta tese falhar — e o que a protege.

**01 · O relógio competitivo fecha a janela.** Octopus/Kraken e gridX/Kiwigrid (white-label) podem tropicalizar antes. A janela é a abertura do Grupo B (2027–2028). Se chegarem com capital e playbook pronto, o espaço BR vazio fecha.
→ *mitigação:* velocidade no M1+M2; o medidor-sensor como moat de dado que controlador puro não tem.

**02 · "Execução conhecida" ≠ execução barata.** Inteligência cloud-edge + VPP exigem times de ML, energia e regulatório. O caminho está provado, mas replicá-lo custa. É risco de execução, não de tese — e risco de execução mata startups.
→ *mitigação:* herdar a fundação libera capital/foco para o M1; o beachhead do integrador financia a onda.

**03 · Conformidade BR é fosso e armadilha.** ANEEL/PRODIST/INMETRO protege contra estrangeiros — mas o custo/tempo de homologação pode atrasar o M2 e queimar caixa antes da receita.
→ *mitigação:* começar a homologação cedo, em paralelo ao M1; usar a comercializadora-âncora como âncora regulada.

**04 · O VPP brasileiro pode estar vazio porque não existe.** O "espaço vazio" pode ser vazio porque o mercado ainda não se formou. Receita de flexibilidade no BR é **hipótese, não fato** — depende de regulação em construção.
→ *mitigação:* não modelar M2 como receita certa; tratar VPP como opção regulatória, não premissa de sobrevivência.

**05 · Agnosticismo é passivo de engenharia perpétuo.** Suportar N fabricantes é custo contínuo — cada firmware de inversor que muda quebra a integração. O EzManager escolheu o jardim murado por isso. O moat tem manutenção.
→ *mitigação:* driver layer disciplinada + certificação de device + priorizar as marcas que cobrem 80% da base BR.

---

*Sequência: herdar (grátis) → alcançar (execução) → ocupar (aposta). Não financiar a aposta com a lógica do que é grátis. Notas-alvo derivadas do scoring dos 11 players; referências = quem detém o teto de cada capacidade. Premissas de mercado e regulatórias a validar com assessoria. Projeto EOS-DENO · passo 3. Espelha `eos-deno-spec-produto-passo3.html`.*
