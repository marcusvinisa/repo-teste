# 01 — Visão de Produto e PRD

> Documento de requisitos e visão do **Smart**, um produto único de gestão de energia residencial e de pequeno porte (EMS/HEMS) que unifica nuvem, aplicativos e hardware proprietário sob uma marca, de forma **agnóstica de fabricante**, para unidades consumidoras de baixa tensão no Brasil.

---

## 1. Contexto e problema

Hoje o mercado oferece duas categorias de ferramenta que **não conversam bem** e deixam lacunas:

1. **Portais/apps de nuvem do fabricante** (ex.: SEMS+ Web da GoodWe). Excelentes para **monitorar** e **configurar remotamente** ativos **daquele fabricante**, mas:
   - Presos a uma marca (silos por inversor/bateria);
   - Dependentes de nuvem (sem nuvem, sem controle);
   - Sem **controle determinístico** local de baixa latência;
   - Sem orquestração de **cargas de terceiros** (EV, bomba de calor, tomadas) de forma profunda.

2. **Gateways de hardware** (ex.: EzManager3000 da GoodWe). Trazem controle local e integração de cargas (via Shelly, SG-Ready, Modbus), mas:
   - Limites rígidos de quantos ativos gerenciam;
   - Forte amarração ao ecossistema do próprio fabricante;
   - Inteligência de mercado/otimização ainda centrada em tarifa dinâmica europeia, não no contexto brasileiro.

**Nenhum dos dois, isolado, entrega** um produto que: (a) seja **multimarca de verdade**, (b) combine **borda determinística + nuvem inteligente**, (c) cubra os **arranjos comerciais brasileiros** (cativo, GD compartilhada, mercado livre) e (d) escale de uma casa simples até **serviços de rede/VPP**.

### O que o Smart faz que os dois isolados não fazem

| Lacuna nos produtos isolados | Resposta do Smart |
|---|---|
| Silo por marca | **Camada de abstração de dispositivos (DAL)** com drivers locais + conectores de nuvem multimarca → ver [05](05-integracao-e-conectividade.md) |
| "Ou app, ou hardware" | **Topologia mista**: cada função roda na camada certa (`[SW]`/`[SW+HW]`/`[HW]`/`[AMBOS]`) |
| Sem controle offline | **Edge-first** com fail-safe local → ver [07](07-especificacao-firmware-edge.md) |
| Contexto europeu | **Modelagem dos 15 cenários brasileiros** (cativo/GD compartilhada/mercado livre) → ver [11](11-matriz-de-cenarios.md) |
| Casa → rede | Mesmo produto escala até **VPP/grid services e GD compartilhada** → ver [08](08-plataforma-cloud-e-apis.md) |

---

## 2. Proposta de valor

> **"Um só produto para enxergar, controlar e rentabilizar toda a energia da unidade consumidora — qualquer marca, com ou sem nuvem."**

Três promessas centrais:

1. **Economia e autonomia** — maximiza autoconsumo, desloca cargas para horários baratos, reduz conta (tarifa branca/ToU/dinâmica/bandeiras) e dá backup confiável.
2. **Agnóstico e à prova de futuro** — funciona com inversores, baterias, carregadores de VE, bombas e cargas de diferentes marcas, hoje e amanhã.
3. **Pronto para o mercado** — habilita GD compartilhada (rateio), migração ao mercado livre e participação futura em serviços de rede/VPP, sem trocar de plataforma.

---

## 3. Personas e *jobs-to-be-done*

| Persona | Quem é | Principais *jobs* | Superfície primária |
|---|---|---|---|
| **Morador / proprietário** (primária) | Dono da UC residencial/pequeno comércio | "Quero pagar menos, ter backup e controlar minha casa sem complexidade" | App mobile |
| **Instalador / integrador** (primária) | EPCista, integrador solar, O&M | "Quero comissionar rápido, monitorar uma frota e configurar/atualizar remoto" | Web Pro |
| **Comercializadora / agregador (VPP)** (avançada) | Varejista, agregador de flexibilidade | "Quero agregar e despachar flexibilidade e faturar serviços" | Web Pro + API |
| **Gestor de GD compartilhada** (avançada) | Administrador de geração compartilhada/cooperativa/consórcio | "Quero ratear créditos entre UCs e conciliar geração x consumo" | Portal GD |

Detalhamento de fluxos por persona em [09 — Apps e UX](09-apps-web-mobile-e-ux.md).

---

## 4. Princípios de produto

1. **Agnóstico por design** — toda integração passa pela DAL; nenhuma feature depende de uma marca específica.
2. **Camada certa para cada função** — controle crítico/offline no edge; inteligência pesada e agregação na nuvem; experiência no app.
3. **Híbrido, não "ou/ou"** — local **e** cloud-to-cloud coexistem; o Smart escolhe o melhor caminho por ativo (ver [05](05-integracao-e-conectividade.md)).
4. **Seguro e determinístico** — `[HW]` garante comportamento mesmo sem internet; comandos idempotentes.
5. **Escala progressiva** — o mesmo produto cobre do N0 (só consumo) ao N5 (grid services) sem re-arquitetura (ver [11](11-matriz-de-cenarios.md)).
6. **Conformidade brasileira primeiro** — PRODIST, ANEEL, INMETRO, ANATEL e arranjos comerciais locais são requisitos, não extras (ver [02](02-contexto-regulatorio-mercado-br.md)).

---

## 5. Empacotamento e *tiers*

O empacotamento acompanha **nível de ativos** (N0–N5) e **persona**. Hardware é opcional nos níveis baixos (modo só-nuvem) e recomendado/obrigatório nos níveis que exigem controle determinístico.

| Tier | Público | Hardware | Funções centrais |
|---|---|---|---|
| **Smart Lite** `[SW]` | Cativo/GD só consumo ou só PV | Nenhum (via API/nuvem do fabricante) | Monitoramento, contas, relatórios, alarmes |
| **Smart Home** `[SW+HW]` | +Bateria, +EV, +cargas | **Smart Gateway** | Autoconsumo, backup, EV smart charging, automações, tarifa branca/ToU |
| **Smart Home+** `[SW+HW]` | +Load shifting + tarifa dinâmica | **Gateway + Smart Meter** | Otimização por preço + forecast, medição própria, peak shaving |
| **Smart Grid** `[SW+HW]` | +Grid services / VPP / mercado livre | **Gateway + Smart Meter** | Despacho de flexibilidade, agregação, controle de reativo, billing |
| **Smart Pro / Fleet** `[SW]` | Instalador/agregador | — | Comissionamento, frota, OTA, O&M, API, white-label |
| **Smart GD** `[SW]` | Gestor de GD compartilhada | — | Rateio, conciliação, multi-UC, faturamento de créditos |

Famílias de hardware em [06](06-especificacao-hardware.md); preço e *make-vs-buy* em [12](12-roadmap-e-faseamento.md). Modelo de receita (assinatura por UC + venda/locação de hardware + *fee* de serviços de mercado) é **[PREMISSA]** a validar — ver [13](13-gaps-riscos-e-decisoes.md).

---

## 6. Diferenciais competitivos

Benchmark detalhado em [02](02-contexto-regulatorio-mercado-br.md) e na base de conhecimento; resumo do posicionamento:

- **vs gridX / Kiwigrid (DE):** plataformas maduras e agnósticas, mas centradas em regulação europeia (§14a, tarifas dinâmicas EU). O Smart leva esse nível de sofisticação para **GD compartilhada, mercado livre e tarifa branca/bandeiras brasileiras**.
- **vs SmartFox (AT):** forte em controle de excedente PV e cargas, porém hardware-cêntrico e foco DACH. O Smart adiciona **nuvem multimarca + VPP + apps por persona**.
- **vs Lifepowr (BE):** forte em agregação/V2X; o Smart entrega o **mesmo continuum casa→rede** com hardware proprietário e conformidade BR.
- **vs SEMS+/EzManager (GoodWe, as fontes):** o Smart **descola da marca**, mantém o que eles fazem bem (monitoramento, config remota, OTA, diagnóstico IV/AI Health, gateway de cargas) e adiciona multimarca, edge-first e contexto regulatório brasileiro.

---

## 7. Métricas de sucesso (KPIs) `[PREMISSA]`

- **Economia média na conta** por tier (% e R$/mês).
- **Taxa de autoconsumo** (self-consumption ratio) e **autossuficiência**.
- **Cobertura multimarca** (nº de modelos de inversor/bateria/EV/bomba suportados).
- **Tempo de comissionamento** por UC (instalador).
- **Disponibilidade do controle offline** (% de modos que seguem operando sem nuvem).
- **Receita de flexibilidade** por UC agregada (VPP/serviços).
- **UCs por gestor de GD** e precisão do rateio.
- **NPS** morador e instalador.

---

## 8. Escopo MVP vs futuro (resumo)

- **MVP (Fase 0):** monitoramento multimarca, autoconsumo, comissionamento/config remota, app mobile + web, suporte a cativo/GD nos níveis N0–N2.
- **Fase 1:** tarifa branca/ToU/dinâmica + load shifting + EV smart charging + bateria.
- **Fase 2:** grid services, VPP, mercado livre, billing/rateio de GD compartilhada.

Detalhe e critérios de entrada/saída em [12 — Roadmap](12-roadmap-e-faseamento.md).
