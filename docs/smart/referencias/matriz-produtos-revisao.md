# Revisão — Matriz de Produtos Ideais (EOS-DENO) × Suite Smart

> **Verificação de lógica** da [matriz de produtos](fontes/matriz-produtos.md) fornecida pelo usuário, contra a documentação Smart (18 cenários, 7 personas, decisões de hardware D2, fontes de receita do [15](../15-modelo-de-negocio-e-precificacao.md)). Objetivo: validar coerência interna, mapear os produtos EOS-* para os tiers/SKUs Smart, reconciliar a numeração de receitas e listar correções. Liga-se a [00 — Absorção](00-absorcao-e-ajustes.md).

---

## 1. Veredito

A lógica da matriz é **sólida e consistente** com a suite Smart. A taxonomia de 3 tiers, o mapa por persona e a divisão SW/HW são internamente coerentes e batem com o que já documentamos. **Nada contradiz** as decisões fechadas (7 personas, hardware sinal-only, 18 cenários, Lei 14.300/15.269). Há **7 ajustes** a fazer — todos de *clareza/reconciliação*, nenhum de mérito. Detalhe abaixo.

---

## 2. Crosswalk: produto EOS-* → SKU/tier Smart

A matriz usa nomes "EOS-*" (projeto EOS-DENO); nosso produto é **Smart**. Os 14 produtos mapeiam limpo nos tiers do [01 §5](../01-visao-e-prd.md) e nas capacidades do [08](../08-plataforma-cloud-e-apis.md):

| Matriz | Equivalente Smart | Camada/onde |
|---|---|---|
| **P1** EOS Integrador | **Smart Pro / Fleet** `[SW]` | [01 §5](../01-visao-e-prd.md) · comissionamento/frota/OTA |
| **P2** EOS GD | **Smart DG** `[SW]` | [01 §5](../01-visao-e-prd.md) · billing/rateio [08 §4](../08-plataforma-cloud-e-apis.md) |
| **P3** EOS Consumo | **Smart Lite / Smart Home** `[SW]`/`[SW+HW]` | app do morador [09](../09-apps-web-mobile-e-ux.md) |
| **P4** EOS OS (licença) | **White-label / API** (multi-tenant) | [08 §5–6](../08-plataforma-cloud-e-apis.md) · GTM canal [15 §5](../15-modelo-de-negocio-e-precificacao.md) |
| **P5** EOS Meter MaaS | **Smart Meter** (modo serviço/locação) | [06](../06-especificacao-hardware.md) HW |
| **P6** EOS Hub | **Smart Gateway** (controlador HEMS por **sinal**) | [06](../06-especificacao-hardware.md) HW · decisão **D2** [13](../13-gaps-riscos-e-decisoes.md) |
| **P7** EOS Canal | **GTM canal/white-label** | [15 §5](../15-modelo-de-negocio-e-precificacao.md) |
| **P8** EOS ACL | **Migração mercado livre** (serviço) | capacidade Smart Grid · [02](../02-contexto-regulatorio-mercado-br.md) |
| **P9** EOS Comercializadora | **fora do escopo de produto** — negócio regulado | ver §4 ajuste #1 |
| **P10** EOS Grid | **Grid services p/ DSO** | Smart Grid · [08 §3](../08-plataforma-cloud-e-apis.md) |
| **P11** EOS Flex/VPP | **VPP/agregação** | módulo VPP [08 §3](../08-plataforma-cloud-e-apis.md) |
| **P12** EOS Dados | **API pública / dados** | [08 §6](../08-plataforma-cloud-e-apis.md) |
| **P13** EOS Agentes | **Agent-fabric AI-native** | moat [00 §5.3](00-absorcao-e-ajustes.md) · roadmap Fase 3 [12](../12-roadmap-e-faseamento.md) |
| **P14** EOS P2P | **P2P** (feature futura) | horizonte |

> **Conclusão do crosswalk:** os 14 produtos da matriz e o packaging Smart (6 tiers) **são o mesmo desenho** visto por lentes diferentes — a matriz é *go-to-market por persona/maturidade*; nossos tiers são *empacotamento por ativo*. Complementares, não conflitantes.

---

## 3. Reconciliação de receitas (doc 15 R1–R6 ↔ matriz R-01…R-13)

São **duas numerações diferentes**. Nosso [15](../15-modelo-de-negocio-e-precificacao.md) tem 6 fontes (simplificadas); a matriz cita o mapa EOS-DENO de 11 (+2 propostas), **cuja legenda R-01…R-11 não está neste repo**. Mapeamento inferido pelo uso:

| Smart (doc 15) | Matriz EOS-DENO | Nota |
|---|---|---|
| **R1** Hardware | **R-13** (atacado Energy Hub) + **R-12** (Meter MaaS, modo locação) | matriz **separa** device-margem vs MaaS-recorrente |
| **R2** SaaS | **R-01** (SaaS integrador) | — |
| **R3** Fee mercado/VPP | **R-08** (rev-share flexibilidade) | T3 nos dois |
| **R4** Fee GD | **R-06** (GD compartilhada) | — |
| **R5** White-label/API | **R-02** (licença OS) + **R-07** (canal) + **R-09** (dados) | nosso R5 agrega 3 da matriz |
| **R6** Serviços profissionais | **R-03** (success fee ACL) | — |
| *(ausente no doc 15)* | **R-04** (take-rate BT), **R-05** (spread comercialização), **R-10** (marketplace), **R-11** (P2P) | avançado/gatilhado |

> **Ação proposta (carece de OK):** no [15](../15-modelo-de-negocio-e-precificacao.md), **dividir R1 em R1a (venda/margem de device) e R1b (Smart Meter MaaS — recorrente, OpEx)**, para capturar o modelo Intellihub que o usuário pediu explicitamente. R-04/R-05/R-10/R-11 entram como linhas "gatilhadas/futuras" se desejado.

---

## 4. Ajustes a fazer (todos de clareza, nenhum de mérito)

1. **P9 (Comercializadora) não é um SKU de produto** — é uma **entidade regulada** (capital alto, garantias, balanço; a própria matriz marca "gate D2"). Tratar como **opção de negócio**, não como produto da suite. *Sem isso, parece um tier de software que não é.*
2. **⚠️ Contradição de tier do P13 (Agentes) — o achado mais agudo.** Está como **T3** ("aposta, VP~0"), mas o texto diz que ele **habilita o P8-BT a fechar** (custo de servir ~zero). Se o caso-base do P8 (T2) **depende** do P13, então o P8 herda o risco de execução do P13 → P8 deixa de ser um T2 "de-riscado". **Correção:** o caso-base do P8-BT tem de fechar **sem** assumir agentes (agentes = *upside*, não premissa); ou declarar a dependência explicitamente e rebaixar o P8 para T2/T3. Isto preserva a regra de ouro "a narrativa não pode depender de T3".
3. **"T1.5" é meio-tier ad-hoc.** P4/P5 são "modelo validado globalmente, **adoção BR** em aberto". Mais limpo: manter **3 tiers** e adicionar uma flag ortogonal de *risco-de-adoção* (P4/P5 = "T1-modelo / T2-adoção"). Evita inflar a taxonomia.
4. **Tensão CON × "MVP primário".** A matriz diz que a venda **direta paga** ao CON é fraca (vender via canal INT/COM); nosso [01](../01-visao-e-prd.md) diz "MVP primário: CON+INT". **Não é contradição** se lido como "**CON = superfície de uso primária; INT = cliente pagante/beachhead**". Recomendo afinar a redação do [01](../01-visao-e-prd.md) para não sugerir que o CON é fonte de receita **direta**.
5. **Autossuficiência:** a matriz referencia R-01…R-11 sem a legenda (mapa EOS-DENO externo). Resolvido pela tabela do §3 acima; idealmente trazer a legenda das 11 receitas para o repo (ou linkar a fonte).
6. **Marca:** nomes EOS-* convivendo com "Smart" — resolvido pelo crosswalk do §2. Ao operacionalizar, usar os nomes Smart.
7. **Menores (sem ação obrigatória):** P3 poderia incluir **A0** (consumo puro cativo, monitoramento); N5 (grid services) é uniformemente T2/T3 em A/B/C — **consistente** com nossa ressalva de que flexibilidade BT é prospectiva.

---

## 5. O que **confirma** (alinhamento forte)

- **Divisão de hardware** (P5 Meter / P6 Hub) bate exatamente com a **decisão D2**: o "Hub" = **Smart Gateway** (controla por **sinal**, aciona chave externa, nunca chaveia potência); o "Meter" = **Smart Meter** commodity. ✅
- **INT como beachhead** (única persona com receita primária operável hoje; máquina de CAC) bate com [01](../01-visao-e-prd.md) ("INT primário/beachhead") e [15 §5](../15-modelo-de-negocio-e-precificacao.md) (canal via integradores). ✅
- **AGG = 100% aposta** e **N5 prospectivo** batem com nossa ressalva regulatória ([02](../02-contexto-regulatorio-mercado-br.md): figura do agregador de RED inexistente). ✅
- **Tiers de maturidade** batem com a régua regulatória: Lei 14.300 = T1; **Lei 15.269 BT nov/2027–2028** = gatilho T2; agregador ausente = T3. ✅
- **Moats** (CCEE/BR + agent-fabric) idênticos aos registrados em [00 §5](00-absorcao-e-ajustes.md). ✅

---

## 6. Respostas aos 3 pedidos da matriz

1. **"Validar o fatiamento em 14 produtos."** ✅ **Sólido para o escopo Smart.** Nenhum produto falta. Única correção de fundo: **P9 não é produto** (é negócio regulado — §4 #1), e **P13 precisa sair do caso-base** como dependência (§4 #2). Demais tiers OK.
2. **"Autorizar R-12 e R-13."** Isso altera o **documento-fonte EOS-DENO** (`receitas-energia-br.md`) — **decisão sua**, fora deste repo. No lado Smart, recomendo refletir como **split do R1 (R1a device / R1b MaaS)** no [15](../15-modelo-de-negocio-e-precificacao.md) — aplico se você aprovar (§3).
3. **"Profundidade do próximo passo (a/b/c)."** Recomendo **adiar HTML e xlsx** (são entregáveis EOS-DENO, não da suite). Para o repo Smart, o passo de maior valor já foi feito (crosswalk + reconciliação). O **unit economics de P1+P5** vale quando você quiser fechar pricing — mas depende de inputs de **disposição a pagar** (decisões em aberto do [15 §6](../15-modelo-de-negocio-e-precificacao.md)).

---

## 7. Pendências para você decidir

| # | Decisão | Default se você não responder |
|---|---|---|
| M1 | Aplicar split **R1 → R1a/R1b** no doc 15? | Não aplico (deixo como proposta) |
| M2 | Afinar redação do [01](../01-visao-e-prd.md) (CON = uso / INT = receita)? | Aplico (é só clareza, baixo risco) |
| M3 | Reclassificar P13 fora do caso-base do P8 — refletir no [13](../13-gaps-riscos-e-decisoes.md)/[12](../12-roadmap-e-faseamento.md)? | Registro como nota de risco |
| M4 | Marcar P9 como "negócio regulado, não-produto" onde for citado? | Aplico na próxima edição relevante |
