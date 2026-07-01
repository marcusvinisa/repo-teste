# 04 · Memória & Aprendizado no Tempo

> Mecanismo de continuidade com **loop humano mínimo**. Dentro de um Claude Project, o Claude não persiste aprendizado sozinho entre sessões — a persistência vem deste arquivo + do ritual de fechamento + dos recursos nativos (memória e "buscar conversas anteriores"). A partir de jun/2026, o **build** migra para o **Claude Code (spec-driven)**; este projeto (claude.ai) permanece como a **fundação estratégica e de conhecimento**.

---

## 🧭 STATE — snapshot vivo (sempre atualizado no topo)

- **Empreendimento:** **EOS-DENO** — plataforma de energia AI-native/operada por agentes, BR; spinoff da empresa-âncora (Marcus co-fundador/CPTO). Beachhead = **integrador/EPC**.
- **Fase atual:** **transição estratégia → arquitetura/protótipo.** Fundação estratégica concluída (hardware + software + portfólio + economia). Build vai para o **Claude Code (spec-driven)**.
- **Última decisão:** (1) portfólio de **14 produtos** aprovado em 3 tiers de PMF; (2) **R-12/R-13** (hardware-licenciamento) autorizadas; (3) **top-5** por aderência×receita = P2 GD · P1 Integrador · P4 OS-licença · P5 Meter MaaS · P7 Canal; (4) **iniciar o v1 no Claude Code** — fatia mínima do beachhead.
- **Escopo do v1 (decidido):** produto do **integrador/EPC (P1)** rodando sobre o **hardware smart-meter existente** (não o ODM próprio ainda). Fluxo: Smart → ingestão → time-series → modelo de ativo → **portal do integrador** (monitoramento + frota + comissionamento + diagnóstico remoto). **Camada de abstração de device (S2.3) desde a 1ª linha** — trocar p/ medidor ODM depois = configuração, não reescrita. **Fora do v1:** VPP, CCEE, agent-fabric, otimização, mercado livre, os 18 cenários.
- **Achado-âncora:** P5 Meter MaaS **não fecha como SaaS** (LTV:CAC ~1,4x, payback ~69m) — economia de infraestrutura, exige financiamento (modelo Intellihub/green loans).
- **Próxima ação sugerida:** abrir conversa nova (mesmo projeto) → 1º entregável = **brief de escopo do v1** (in/out, critério de "pronto", decisão build/fork por componente) → depois a spec detalhada. Rodar **descoberta com 2–3 integradores em paralelo** ao build (transforma os [H]/[INPUT] em evidência).
- **Decision-gates abertos:** marca/nome (**EOS-DENO sem checagem de colisão**); constituição de entidade; refletir R-12/R-13 no REV-01; pivô de tese/beachhead; contratação.

---

## 🔁 Ritual de fechamento de sessão (a automação)

Ao fim de cada sessão — ou quando o Marcus disser **"fecha a sessão"** — o Claude **gera automaticamente** um bloco pronto-para-colar com: (1) **STATE atualizado** (substitui o de cima); (2) **nova entrada de LOG** (no topo); (3) se algo mudou em decisões/glossário/skills, o trecho exato a atualizar em 01–03. O Marcus só cola. Se ele não pedir, o Claude oferece proativamente quando a sessão produziu decisão ou artefato.

> Reforço: manter ativados, nas configurações, **"gerar memória a partir do histórico"** e **"buscar conversas anteriores"**.

---

## 🟢 Autonomia (proceder SEM perguntar)
Pesquisar e validar fatos · rascunhar · modelar cenários · produzir artefatos · propor próximos passos · atualizar esta memória · cruzar benchmark · sinalizar riscos · **desafiar premissas (sempre)**. Em tarefas de 3+ passos, planejar antes (skill `agent-behavior`).

## 🔴 Decision-gates (PARAR e trazer o Marcus)
Marca/nome · constituição de entidade · gasto/captação · submissão regulatória real · pivô de tese/beachhead · contratação · qualquer coisa irreversível ou que assuma fato não verificado de alto impacto. Fora desses: **proceder e reportar**.

---

## 📓 LOG — append-only (mais recente no topo)

### 2026-06-30 — Portfólio de produtos + unit economics + HTMLs + transição p/ build
- **Decisões:** (1) portfólio de **14 produtos** aprovado em 3 tiers de PMF (deep-dive futuro); (2) **R-12** (Medidor-MaaS) e **R-13** (Energy Hub attach) autorizadas p/ o mapa de receitas; (3) **top-5** por aderência×receita = P2, P1, P4, P5, P7; (4) tema dos HTMLs clareado + contraste de descrições/"como" elevado; spec de hardware reestruturado em O QUE/COMO/nota; (5) **decidido iniciar o v1 no Claude Code (spec-driven)**, escopo = beachhead integrador (P1) sobre o smart-meter existente.
- **Fatos/fontes:** Intellihub financia metering com ~A$3 bi em green loans [F]; nenhum dos 16 players de software tem CCEE/BR nem agent-fabric LLM (scoring) — os 2 tetos vazios.
- **Aprendizados:** (1) **P5 Meter MaaS = infra, não SaaS** — financiar como project finance; (2) aderência da Intellihub é em mercado AU **mandatado**; BR sem mandato de smart meter → timing não transfere (risco banana-com-banana mais agudo); (3) o "como" do spec/matriz **estava presente mas em baixo contraste** — os 2 pedidos de ajuste eram a mesma raiz; (4) P4 OS-licença: LTV:CAC sensível ao tamanho do deal; (5) não specar "a plataforma" — specar a fatia mínima do beachhead.
- **Artefatos:** `eos-deno-docs-2026-06-30.zip` (20 docs: hardware + software + produtos). Inclui personas/cenários, matriz/scoring/spec de SW e HW, matriz de produtos, unit-economics-top5.xlsx. Tema atualizado nos 4 spec/matriz.

### 2026-06 — Arco EOS-DENO (rename + fundação técnica) [consolidado]
- **Decisões:** rename **CORRENTE → EOS-DENO**; recalibração jun/2026 (smart meter próprio + DERMS própria = BUILD/moat; crédito+canal-âncora = moat herdado; empresa-âncora adquire comercializadora; multi-tenant obrigatório).
- **Artefatos:** matriz/scoring(11 players)/spec de **hardware**; personas+18 cenários, matriz(~70 microsserviços)/scoring(16 players, dupla-lente)/spec de **software** com decisão build/fork/buy.
- **Aprendizados:** 2 tetos de mercado vazios = **CCEE/BR** e **agent-fabric AI-native (LLM)** — onde o EOS-DENO nasce à frente; fork OpenEMS (EMS) + build-on ThingsBoard (multi-tenant/IoT) + EMHASS/PyPSA (otimização); Intellihub = paralelo mais próximo (valida fundação, não moat).

### [data] — Backbone do projeto
- **Decisões:** criado o Projeto (então "CORRENTE"); arquivos 00–04 + instruções; protocolo de memória/gates.
- **Aprendizados:** loop mínimo = ritual de fechamento + recursos nativos de memória.

### (sessões anteriores — resumo)
- Entrada bowling-pin + scorecard de beachhead (`playbook-entrada-newbets.html`).
- Arquitetura societária HoldCo híbrida (`arquitetura-societaria-plataforma.html`).
- Operadora descentralizada, duas trilhas + empilhamento (`operadora-descentralizada-blueprint.html`).
- Benchmark 5 arquétipos + modelo composto (`benchmark-energy-tech-overlay-brasil.html`).
