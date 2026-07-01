# Passo 2 · Pontuação dos 11 Players contra a Matriz Ideal

> Cada player pontuado **nível de capacidade**, escala **0–4** de maturidade, contra a rubrica (`matriz-funcionalidades-ideal.md`). `–` = fonte não confirma (sem chute). As 3 camadas que de fato diferenciam (**02 Integração, 04 Inteligência, 05 VPP**) vêm detalhadas por capacidade; as demais, no resumo por camada.

**Escala:** 0 ausente · 1 observa · 2 controla por regra · 3 otimiza · 4 autônomo/transaciona.

**Fidelidade dos dados (honesto):** smart-meter = granular (validado clique a clique com você). EzManager3000 / Air 2 = datasheet/página de produto. Os 8 demais = pesquisa web (fontes oficiais). Onde a granularidade da fonte não sustenta a nota, usei `–`.

---

## 1 · Matriz-resumo por camada (0–4 holístico)

Nota por camada = leitura consolidada das capacidades daquela camada. **Total e média medem *completude* (largura), não *qualidade* — um app cloud-only é penalizado em camadas de hardware que ele deliberadamente não faz.** Leia junto com a seção 2.

| Player | 00 Med | 01 Con | 02 Int | 03 EMS | 04 IA | 05 VPP | 06 Plat | 07 Conf | 08 HW | 09 UX | **Méd** | Rank |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Ideal** | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **4.0** | — |
| Kiwigrid | 2 | 4 | 3 | 4 | 4 | 4 | 3 | 3 | 2 | 4 | **3.3** | 1 |
| gridX | 2 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 2 | 3 | **3.2** | 2 |
| Eniris | 2 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | **3.0** | 3 |
| Fenecon | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | **2.9** | 4 |
| enjoyelec Air 2 | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | – | 3 | **2.7** | 5 |
| Lifepowr | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 2 | 2 | 3 | **2.6** | 6 |
| Bliq | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 2 | 2 | **2.5** | 7 |
| GoodWe EzManager | 1 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | **2.4** | 8 |
| Evergen | 1 | 1 | 1 | 4 | 3 | 3 | 3 | 1 | 0 | 3 | **2.0** | 9 |
| **smart-meter** | **2** | **2** | **2** | **1** | **0** | **0** | **2** | **2** | **4** | **2** | **1.7** | 10 |
| Zerofy | 1 | 0 | 3 | 3 | 2 | 0 | 3 | 1 | 0 | 4 | **1.7** | 10 |

**Leitura imediata:** os líderes de *completude* são as plataformas europeias agnósticas de hardware+nuvem (Kiwigrid, gridX, Eniris, Fenecon). O smart-meter e o Zerofy empatam no fim **desta** lista — mas por motivos **espelhados e opostos**: o smart-meter é forte em hardware/medição e zero em inteligência/VPP; o Zerofy é forte em UX/inteligência e zero em hardware/medição/VPP. *Nenhum dos dois é "pior" — cada um tem metade do produto. O ideal CORRENTE quer as duas metades.*

---

## 2 · Teto de mercado por camada — e a distância do smart-meter

A leitura que importa para construir produto: em cada camada, **qual a maior nota atingida**, **quem a detém**, e **onde o smart-meter está**. Isto é o gabarito real (não o ideal teórico, mas o teto que alguém já provou ser possível).

| Camada | Teto real | Quem detém | smart-meter | Gap |
|---|:--:|---|:--:|---|
| **00 Medição** | **3** | **smart-meter** (medição nativa Classe 1/2) + Fenecon | **3** ⭐ | **Lidera.** Falta só sensoriamento ambiental |
| 01 Conectividade | 4 | gridX, Kiwigrid, Eniris | 2 | Sem Modbus-TCP/EEBUS/OCPP; sem gateway de borda |
| 02 Integração | 4 | Eniris, gridX, Kiwigrid, Fenecon (agnosticismo) | 2 (agnost.=3) | Falta comando de VE e bomba; ampliar cobertura |
| 03 Controle & EMS | 4 | Eniris, gridX, Kiwigrid, Fenecon, Lifepowr | 1 | Falta limite de demanda e otimização por tarifa |
| **04 Inteligência** | **4** | **gridX, Kiwigrid** | **0** | **Bloco inteiro ausente** — previsão, scheduling, edge |
| **05 VPP/Flex** | **4** | **Eniris, Kiwigrid, Lifepowr** | **0** | **Bloco inteiro ausente** — DSO, VPP, trading |
| 06 Plataforma | 4 | gridX, Kiwigrid, Eniris, Fenecon | 2 | Falta API aberta / white-label / multi-tenant |
| **07 Conformidade BR** | **2** | **smart-meter** (único BR-nativo) | **2** ⭐ | **Lidera por ausência** — ninguém mais é BR. Falta INMETRO formal |
| **08 Hardware** | **4** | **smart-meter** (IP65, <5W, TFT+RGB) | **4** ⭐ | **Lidera.** Sem gap |
| 09 UX | 4 | Zerofy | 2 | Falta autopilot, copilot, onboarding sem fricção |

**O resultado é cirúrgico:** o smart-meter **já detém o teto** em **medição (00)** e **hardware (08)**, e é o **líder de fato em conformidade BR (07)** — porque nenhum dos 10 estrangeiros tem presença brasileira. E está no **chão absoluto (0)** exatamente em **inteligência (04)** e **VPP (05)**. O gap não é difuso: são **dois blocos limpos** sobre uma fundação que já é a melhor do grupo em metrologia, hardware e BR.

---

## 3 · Detalhe das camadas diferenciadoras

### 3.1 · Camada 02 — Integração & Comando de Ativos

| Player | Inversor FV | Bateria | Carreg. VE | Bomba calor | Cargas | ★ Agnosticismo |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Ideal | 4 | 4 | 4 | 4 | 4 | 4 |
| smart-meter | 3 | 2 | **0** | **0** | 2 | 3 |
| EzManager | 3 | 3 | 3 | 2 | 2 | **0** |
| Air 2 | 3 | 3 | 3 | 3 | – | **4** |
| Eniris | 3 | 3 | 3 | 3 | 3 | **4** |
| Lifepowr | 2 | 3 | 3 | 1 | 2 | 3 |
| Bliq | 2 | 3 | – | – | – | 3 |
| gridX | 3 | 3 | 3 | 3 | 2 | **4** |
| Kiwigrid | 3 | 3 | 3 | 3 | 3 | **4** |
| Fenecon | 3 | **4** | 3 | 3 | 3 | **4** |
| Evergen | 2 | 3 | 0 | 0 | 0 | 3 |
| Zerofy | 1 | 1 | 3 | 3 | 3 | **4** |

*Insight:* o smart-meter já **comanda inversor e bateria** (≥ a maioria) e é **agnóstico (3)** — mas o **EzManager é 0 em agnosticismo** (jardim murado). O agnosticismo é o eixo onde o smart-meter já bate o líder de mercado de inversores. As lacunas reais do smart-meter aqui são pontuais: **VE e bomba de calor (0)**.

### 3.2 · Camada 04 — Inteligência / AI

| Player | Previsão | Scheduling | Aprendizado | ★ Locus de compute |
|---|:--:|:--:|:--:|:--:|
| Ideal | 4 | 4 | 4 | 4 |
| **smart-meter** | **0** | **0** | **0** | **1** |
| EzManager | 3 | 3 | 2 | 2 (IA na nuvem) |
| Air 2 | 3 | 3 | 3 | **4** (cloud-edge) |
| Eniris | 3 | 3 | 2 | **4** (fallback edge) |
| Lifepowr | 3 | 3 | 2 | 2 |
| Bliq | 3 | 3 | 3 | 2 |
| gridX | **4** | **4** | 2 | **4** (híbrido) |
| Kiwigrid | 3 | **4** | 3 | **4** (RailX+ offline) |
| Fenecon | 3 | **4** | 2 | **4** (opera sem internet) |
| Evergen | **4** | **4** | 3 | 1 (nuvem) |
| Zerofy | 3 | 3 | 2 | **0** (só nuvem) |

*Insight:* aqui o smart-meter é **0/0/0**. O teto é **gridX e Kiwigrid (4)**. Decisivo: **5 players já fazem compute no edge resiliente (locus 4)** — gridX, Kiwigrid, Fenecon, Eniris, Air 2 — enquanto EzManager (nuvem) e Zerofy (nuvem) **não**. A lição arquitetural para o smart-meter evoluir é **cloud-edge, não nuvem pura.**

### 3.3 · Camada 05 — Despacho & Flexibilidade / VPP

| Player | Sinais DSO | ★ Agregação/VPP | Trading | Deslig. remoto |
|---|:--:|:--:|:--:|:--:|
| Ideal | 4 | 4 | 4 | 4 |
| **smart-meter** | **0** | **0** | **0** | **0** |
| EzManager | **4** (§14a) | 1 | 3 | 3 |
| Air 2 | – | 3 | 2 | – |
| Eniris | 3 | **4** | **4** | 3 |
| Lifepowr | 2 | **4** (BSP Elia) | 3 | 2 |
| Bliq | – | 2 | 3 | – |
| gridX | **4** | 3 | 3 | 3 |
| Kiwigrid | **4** | **4** (Energy Hub Alliance) | 3 | 3 |
| Fenecon | **4** | 2 | 3 | 3 |
| Evergen | 2 | **4** (DERMS p/ utilities) | 3 | 3 |
| Zerofy | **0** | **0** | **0** | **0** |

*Insight:* smart-meter e Zerofy são os únicos **0/0/0/0** — nenhuma camada de mercado. O teto de **VPP é Eniris, Kiwigrid, Lifepowr, Evergen (4)**. Mas nota crítica: **todo esse VPP é estrangeiro e plugado em mercados europeus/australianos (§14a, Elia, AEMO)** — **nenhum** está plugado em **CCEE / mercado livre brasileiro**. O teto de "VPP no Brasil" hoje é **vazio**.

---

## 4 · Perfil de cada player (uma linha)

- **Kiwigrid** [DE] — plataforma IoT white-label agnóstica; gateway RailX+ offline + IA Matua + VPP via Energy Hub Alliance. O mais completo. Zero BR.
- **gridX** [DE, E.ON] — HEMS white-label agnóstico; gridBox+XENON híbrido edge, +50 marcas, forte em plataforma/API. Zero BR.
- **Eniris** [BE] — EMS agnóstico (+60 marcas) hardware+nuvem; VPP SmartgridX + mercados de balanceamento; fallback no edge. Zero BR.
- **Fenecon** [DE] — fabricante de BESS + FEMS **open-source** (OpenEMS); agnóstico, edge, API aberta. Interface a trading (VPP via 3º). Zero BR.
- **enjoyelec Air 2** [CN/EU] — controlador HEMS agnóstico **cloud-edge** (controle local sobrevive à nuvem); linha VPP própria. Conformidade UE. Zero BR.
- **Lifepowr** [BE] — plataforma de flexibilidade + FlexiObox; **VPP com BSP licenciado pela Elia**; otimização por custo real. Zero BR.
- **Bliq** [NL/BE] — EMS focado em **bateria** residencial; Modbus, trading dinâmico; cobertura de ativos estreita. Só NL/BE.
- **GoodWe EzManager3000** [CN] — controlador EMS rico mas **murado** (só GoodWe); IA na nuvem, §14a, sem medição nativa. UE/AU.
- **Evergen** [AU] — **software puro** de otimização de bateria + **DERMS/VPP** (tecnologia CSIRO); opera VPPs para utilities. Sem hardware/medição.
- **smart-meter** [BR] — **medidor agnóstico + EMS por regra**; metrologia Classe 1/2, IP65, comanda inversor/bateria/cargas. **Único BR-nativo.** Zero inteligência/VPP.
- **Zerofy** [EE/CH] — **app puro** agnóstico (800+ devices); scheduling por preço+previsão, **UX líder**. Sem hardware/medição/VPP.

---

## 5 · Findings & mapa de gap do smart-meter

1. **O smart-meter não está "atrás" — está incompleto numa direção específica.** Ele lidera 3 camadas (medição, hardware, BR) e zera 2 (inteligência, VPP). Não é um produto pior; é **meio produto, com a metade certa de fundação.**

2. **A metade que falta é exatamente a metade "software/mercado"** — e é a metade que **todos os líderes (Kiwigrid, gridX, Eniris, Fenecon) já têm.** Ou seja: o caminho é conhecido, está provado, e é replicável. Não é pesquisa de fronteira; é execução.

3. **O agnosticismo já é um trunfo do smart-meter (3)** — e é onde o concorrente mais óbvio (EzManager, 0) é estruturalmente fraco. Preservar e ampliar isso é mais barato que construir do zero.

4. **Compute no edge é a aposta arquitetural certa:** 5 dos 11 já fazem (locus 4); os que não fazem (EzManager, Zerofy) são notoriamente os mais frágeis. O smart-meter está em 1 — subir para edge-resiliente é o degrau técnico central.

5. **O teto brasileiro está vazio nas camadas que valem receita.** VPP, trading, conformidade ANEEL/PRODIST/INMETRO, CCEE: **nenhum dos 10 estrangeiros ocupa isso no Brasil.** O smart-meter, sendo o único BR-nativo, parte desse espaço com vantagem — se construir a camada de mercado **antes** que Kiwigrid/gridX/Octopus a tropicalizem.

6. **Zerofy é a prova viva do seu ponto:** um "app" pontua **4 em UX e 3 em scheduling/inteligência de cargas** — capacidades de produto reais que o smart-meter (2 e 0) ainda não tem. Excluí-lo teria escondido um teto legítimo. A camada 09 (UX) e o scheduling de cargas entram no roadmap por causa dele.

---

## 6 · Ponte para o passo 3 — a especificação do produto ideal CORRENTE

Com o teto de cada capacidade mapeado e quem o detém, o passo 3 monta a **spec do produto ideal CORRENTE** sobre três decisões:

- **Herdar** (já temos a fundação, é o melhor do grupo): medição nativa Classe 1/2, hardware IP65/<5W/TFT, agnosticismo, BR-nativo, comando de inversor/bateria/cargas.
- **Alcançar** (o mercado já provou, é execução conhecida — copiar o melhor de cada): inteligência cloud-edge (gridX/Kiwigrid), VPP/agregação (Eniris/Kiwigrid/Lifepowr), API aberta/white-label (gridX/Kiwigrid), UX autopilot (Zerofy), comando de VE/bomba (todos).
- **Superar / criar (ninguém tem no BR):** conformidade ANEEL/PRODIST/INMETRO nativa, integração CCEE/mercado livre, e a camada AI-native (agent-fabric) do horizonte 2030 — onde a tese nasce à frente, não atrás.

> A spec do passo 3 não é "ter tudo": é **herdar a fundação que já lidera, alcançar a camada de software que o mercado já provou, e ocupar o espaço BR que está vazio** — nessa ordem de esforço/risco.

---

*Documento de arquitetura de produto · Projeto CORRENTE · passo 2 (scoring). Notas 0–4 no nível de capacidade; `–` = não documentado pela fonte. Fidelidade de dados desigual (ver topo). Rubrica completa em `matriz-funcionalidades-ideal.md`.*
