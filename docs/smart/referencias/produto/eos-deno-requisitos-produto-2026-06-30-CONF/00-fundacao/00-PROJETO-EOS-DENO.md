# ⚡ Projeto EOS-DENO

> **Codinome do workspace estratégico** (antes "CORRENTE", renomeado jun/2026). EOS-DENO é o nome de trabalho do empreendimento — **sem checagem de colisão de marca** (decision-gate aberto).

---

## O que é este projeto

Workspace de co-fundação da **EOS-DENO** — plataforma de energia **AI-native e operada por agentes**, no Brasil, para toda a cadeia descentralizada (gerador, distribuidor, orquestrador, agregador, integrador/instalador, comercializadora, consumidor) com capacidades de EMS, DER, HEMS, OMS, VPP e energy trading.

**Relação com a empresa-âncora:** EOS-DENO é **spinoff** da empresa-âncora (Marcus é co-fundador da empresa-âncora e CPTO da EOS-DENO). Lança **com** a empresa-âncora como âncora (moat herdado: crédito/banco, sourcing em escala, canal de ~5k integradores, acesso a IoT/smart meter), mas o produto é **deliberadamente independente** — as competências da empresa-âncora são insumos substituíveis acessados via APIs limpas, não o moat nem a posse do produto. A empresa-âncora está adquirindo uma comercializadora (âncora regulada para trading antes do mercado abrir). **A plataforma é multi-tenant** — empresa-âncora é tenant, não dona.

## Tese central (estado atual)

1. **Duas fundações, uma plataforma.** (a) **Hardware** — smart meter software-defined com funções HEMS (ODM próprio, firmware e telemetria proprietários) + Energy Hub; monetiza direto **e** como licenciamento/MaaS a terceiros (modelo Kraken/gridX/Intellihub). (b) **Software** — energy OS em ~70 microsserviços, multi-tenant, montado sobre fundações open-source (fork OpenEMS, build-on ThingsBoard/EMHASS/PyPSA) com os diferenciadores construídos do zero.

2. **O moat são os dois domínios que ninguém ocupa:** **CCEE/BR** (liquidação/billing/rateio nativos — nenhum estrangeiro tem) e **agent-fabric AI-native (LLM)** (operação por agentes — ninguém tem ainda). Existir como medidor+plataforma já existe no mundo (Intellihub); o diferencial está nessas duas camadas.

3. **Beachhead = integrador/EPC.** É a única persona que **fecha unit economics sem gatilho regulatório** e a máquina de **CAC subsidiado** das demais camadas. O LTV do consumidor BT individual não sustenta venda direta paga — vende-se via canal.

4. **Portfólio de 14 produtos em 3 tiers de PMF:** **T1 validado** (âncora BR real, operável hoje), **T2 gatilhado** (Lei 15.269/2025 abre Grupo B em nov/2027–2028), **T3 aposta** (regra inexistente, VP~0 no caso-base — opcionalidade, nunca caso-base). Três modelos econômicos distintos que **não podem ser confundidos**: (A) dono do book; (B) operador AI-native white-label sobre carteiras de terceiros — **a tese durável**; (C) compra de ativos distressed — aposta de preço.

## Fase atual & próximos passos

Fundação estratégica **concluída** (matriz/scoring/spec de hardware e software; portfólio; unit economics do top-5). **O build migra para o Claude Code, com metodologia spec-driven.** Este projeto (claude.ai) permanece como **fundação estratégica e de conhecimento**. Próximo entregável: **brief de escopo do v1** = produto do integrador (P1) sobre o **smart-meter existente**, com camada de abstração de device desde o início.

## Para quem são os outputs

Materiais **nível board/investidor e co-founders**, prontos para o mundo real: teses, arquiteturas, modelos econômicos, decks, memorandos, specs. Padrão: rigor factual + clareza executiva.

## Princípios de operação

- **PT-BR, denso, técnico.** Proposta estruturada antes de tarefa grande. Mobile-friendly quando for mensagem.
- **Taxonomia epistêmica obrigatória:** [F] fato c/ fonte · [E] estimativa · [H] hipótese · [INPUT] placeholder. **Banana-com-banana** (paralelo nomeado + tradução BR). Bear case/pré-mortem em todo doc externo.
- **Fato ancorado, criatividade liberada** (inclusive desenhar legislação/lobby — desde que embasado e rotulado).
- **Red-team é parte do trabalho.** Construir e criticar a própria construção; discordar com franqueza; nunca otimizar para concordância.
- **Loop humano mínimo** (ver `04-MEMORIA-E-APRENDIZADO.md`): proceder autônomo abaixo dos decision-gates.
- **Artefatos:** HTML dark interativo é o formato padrão de entrega estratégica (design system definido em 03).
