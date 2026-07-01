# EOS-DENO · Matriz de Produtos Ideais

> **Como fatiar a oportunidade em produtos** — por persona × caso de uso × produto × modelo de negócio × receita, separando o que já tem **PMF validado** do que é **aposta** (com gatilho conhecido) ou **opcionalidade** (regra inexistente). Cobre as **duas fundações**: software (plataforma) **e** hardware (medidor/Energy Hub como produto de licenciamento a terceiros, modelo Kraken/gridX/Intellihub).
>
> Rótulos obrigatórios: **[F]** fato com fonte · **[E]** estimativa fundamentada · **[H]** hipótese a validar · **[INPUT]** placeholder. Âncoras nomeadas (banana-com-banana) com tradução BR. Base: mapa das 11 receitas (`receitas-energia-br.md`, REV-01) + personas/cenários + scoring de software/hardware.

---

## 0 · A lógica do fatiamento (antes da matriz)

**Dois eixos organizam tudo.**

**Eixo 1 — Fundação (de onde a receita nasce).** Você apontou certo: o hardware não é só device de consumidor; é **produto de licenciamento/atacado a terceiros** — o que a Intellihub faz com medidor+plataforma (MaaS a 20+ varejistas [F]), o que o Kraken faz com software (US$ ~7,1/conta/ano × 70M contas [F]), o que a gridX faz white-label. Então o portfólio tem **duas fundações**, cada uma monetizável **diretamente** (vender ao usuário final) **e como licenciamento** (vender a quem serve o usuário final).

**Eixo 2 — Maturidade de PMF.** Não é binário (validado/aposta) — são **três tiers**, que é como o próprio mapa de receitas já se estrutura:

| Tier | Definição | Regra de tratamento |
|---|---|---|
| **T1 · PMF validado** | Categoria com PMF real **no BR hoje** (âncora BR nomeada) ou análogo forte + receita recorrente + operável já | **Construir o negócio aqui.** É o caso-base. |
| **T2 · PMF gatilhado** | Modelo validado em análogo, mas **espera uma regra com data**: Lei 15.269/2025 abre Grupo B em 2027–2028 [F] | **Pré-construir, monetizar no gatilho.** Projeção com catalisador conhecido. |
| **T3 · Aposta / opcionalidade** | Depende de **regra que não existe** (figura do agregador de RED, P2P) — VP ~0 no caso-base [F] | **Opcionalidade.** Presença regulatória ativa, mas a narrativa **não** depende disso. |

**A lição da Intellihub (sua observação de aderência), em uma frase:** a Intellihub **prova que o modelo combinado medidor+plataforma+MaaS monetiza** [F] — mas ela **não tem** a camada AI-native (agentes) nem a camada CCEE-nativa. Ou seja: a **fundação** (T1/T2) é validada por ela; as **apostas** do EOS-DENO são exatamente os dois domínios que ela (e o Kraken) deixam vazios — **CCEE/BR** e **agent-fabric**. O moat não está em existir como medidor+plataforma (isso já existe no mundo); está nas duas camadas que ninguém ocupa.

**Princípio de qualidade herdado da skill** (preserva a coerência econômica): o **integrador/EPC é a única persona com formas de receita primárias operáveis hoje** e funciona como **máquina de CAC subsidiado** das demais camadas — o LTV do consumidor BT individual (R$ 165–790 [E]) não sustenta venda direta paga [F]. Isso decide a sequência: o beachhead não é "o maior mercado", é "o único que fecha unit economics sem gatilho regulatório".

---

## 1 · Matriz-mestre de produtos (as duas fundações)

Cada linha é um **produto ideal** distinto. `F`=fundação (SW software / HW hardware / ⊕ ambas).

| # | Produto | F | Persona(s) | Caso de uso / cenário | Modelo de negócio | Receita | Tier | Âncora / evidência [tag] |
|---|---|:--:|---|---|---|---|:--:|---|
| **P1** | **EOS Integrador** — suíte de operação do EPC (monitoramento, O&M, frota, comissionamento, diagnóstico remoto) | SW | INT | transversal (todo ativo instalado) | SaaS por usina/mês + por integrador/suíte | R-01 (+R-07, R-10) | **T1** | SolarZ, Sunne, GDASH, SolarMaker, Solar Next existem [F]; R$1–5/usina/mês a R$200–1.500/mês/integrador [E][INPUT] |
| **P2** | **EOS GD** — orquestração de GD compartilhada (rateio de créditos Lei 14.300, billing, fidelização) | SW | GER, COM, CON | B0–B4 | SaaS por UC/mês + take | R-06 | **T1** | Órigo R$416,5M/91k UCs [E]; desconto 14–15% [F]; fidelização = dor nº1 [F]; R$2–6/UC/mês [H] |
| **P3** | **EOS Consumo** — app do dono + autoconsumo + otimização (HEMS na nuvem) | ⊕ | CON | A1–A4 | assinatura (geralmente **embutida**, vendida via INT/COM) | attach a R-01/R-06/R-02 | **T1\*** | Zerofy/Tibber provam app HEMS [F]; **venda direta paga é fraca** — LTV BT R$165–790 [E] não sustenta CAC direto [F] |
| **P4** | **EOS OS (licença)** — licenciamento do energy OS por UC (back-office de varejo: CRM, billing, dados) | SW | COM | carteira de varejo | licença por conta/ano (white-label) | R-02 | **T1.5** | Kraken US$500M ARR/70M contas ≈ US$7,1/conta/ano [F]; **modelo validado, adoção BR é aposta** — R$8–35/UC/ano c/ deflator 50–70% [E] |
| **P5** | **EOS Meter MaaS** — medidor-como-serviço a varejistas/DSOs (hardware + dados + comunicação geridos) | HW | COM, DSO | transversal (N0 base) | fee por medidor/mês (OpEx, não CapEx) | **R-12 (propor)** | **T1.5** | **Intellihub: 2,5M+ medidores, 20+ varejistas, MaaS [F]**; modelo validado, **timing BR é aposta** (sem mandato de smart meter ainda [F]) |
| **P6** | **EOS Hub** — Energy Hub/controlador HEMS (atacado a integradores, onde há geração) | HW | INT, CON | A1–A5, B/C com ativo | margem de hardware + attach de software | **R-13 (propor)** | **T1** | Air2/GoodWe provam o device [F]; FOB ~US$34 [E]; break-even vs SKU integrado ~35% adoção [E] |
| **P7** | **EOS Canal** — white-label + rev-share (originação de crédito, distribuição, marketplace) | ⊕ | INT, COM | transversal | rev-share / take de originação 1–4% | R-07, R-10 | **T1** | 1KOMMA5° €520M lucrativa, install-led [F]; alavanca ativo-âncora [INPUT] |
| **P8** | **EOS ACL** — migração ao mercado livre (success fee) + gestão BT contínua (take-rate) | SW | COM, CON | C0–C4 | success fee one-off → take-rate recorrente | R-03 → R-04 | **T2** | Gatilho Lei 15.269, BT nov/2027 [F]; economia BT ~19% [F]; gestão Grupo A R$500–2.500/UC/mês [E], **BT só fecha a R$3–15/UC/mês [H]** |
| **P9** | **EOS Comercializadora** — spread de comercialização de energia (entidade regulada) | SW→Reg | COM, GER | carteira ACL | spread R$/MWh | R-05 | **T2** | Gerador líquido GD R$80–140/MWh [F]; **capital ALTO (garantias+balanço) — gate D2** |
| **P10** | **EOS Grid** — sinais de rede para o DSO (RCR/§14a/DOE, curtailment, hosting capacity) | ⊕ | DSO | A5, B5 | fee de serviço / contrato com distribuidora | (deriva R-12 + serviço) | **T2/T3** | AutoGrid/Intellihub fazem p/ DSO [F]; **depende de programas do DSO existirem no BR [H]** |
| **P11** | **EOS Flex / VPP** — agregação + bidding + serviços ancilares | SW | AGG, GER, DSO | N5, arranjo C | rev-share de flexibilidade | R-08 | **T3** | Next Kraftwerke >10 GW Europa [F]; **figura do agregador de RED inexistente BR [F]; merchant não fecha (~R$4.500 vs ~R$600/MW) [F] — VP ~0 caso-base** |
| **P12** | **EOS Dados** — inteligência/API sobre o dado proprietário | SW | todas, Fintech | transversal | API / assinatura de dados | R-09 | **T3** | comparáveis BR fracos [H]; 1º cliente plausível Fintech-âncora (score de ativo) [INPUT]; **tardio por desenho — consequência do moat, não motor** |
| **P13** | **EOS Agentes** — operação AI-native por agentes (camada transversal, não produto isolado) | SW | ORQ, todas | transversal | embutido (reduz custo de servir → habilita P8 BT) | (habilitador) | **T3** | **ninguém tem em LLM [scoring]**; é o moat de fronteira + o que faz o R-04 BT fechar (custo de servir ~zero) |
| **P14** | **EOS P2P** — energy trading peer-to-peer | SW | CON | transversal | take transacional | R-11 | **T3** | SCEE compensa créditos, não vende energia (REN 1.000) [F]; Powerledger/LO3 pivotaram de P2P p/ flexibilidade [E]; **sandbox, WTP fraca — feature de marca** |

\* **P3 é T1 na categoria mas com ressalva de canal:** o produto tem PMF, mas o *modelo de venda* validado é via integrador/comercializadora, não venda direta paga ao consumidor BT.

---

## 2 · Matriz por persona (validado vs. aposta, lado a lado)

O recorte que você pediu — para cada persona, **o que fecha PMF hoje** vs. **a aposta**.

| Persona | T1 · Validado (operável hoje) | T2 · Gatilhado (Lei 15.269 / DSO) | T3 · Aposta (VP~0 caso-base) |
|---|---|---|---|
| **INT** Integrador/EPC | **P1 EOS Integrador** + **P6 EOS Hub** + **P7 Canal** — *o beachhead, máquina de CAC* | — | — |
| **CON** Consumidor | **P3 EOS Consumo** (via canal) + autoconsumo | **P8 EOS ACL** (migração+gestão BT) | **P14 P2P** |
| **GER** Gerador (GD) | **P2 EOS GD** (rateio+billing) + **P7** | **P9 Comercializadora** (spread) | **P11 Flex/VPP** |
| **COM** Comercializadora | **P4 EOS OS** (licença) + **P5 Meter MaaS** + **P2** | **P8 ACL** + **P9** | — |
| **AGG** Agregador/VPP | — | — | **P11 Flex/VPP** (o produto inteiro é aposta) |
| **DSO** Distribuidor | **P5 Meter MaaS** (parcial) | **P10 EOS Grid** | **P11** (ancilares) |
| **ORQ** Orquestrador | **P13 Agentes** (operação) + plataforma multi-tenant | — | — |

**Leitura:** as personas com **negócio fechável hoje** são **INT, GER, COM** (e CON via canal). **AGG é 100% aposta** — o produto de agregação/VPP só existe se a regulação criar a figura do agregador. **DSO é misto** (MaaS hoje, grid services depende de programa). Isso confirma o beachhead: comece por quem paga hoje (INT → GER/COM), não por quem só paga no futuro (AGG).

---

## 3 · Os três blocos, destilados

**T1 — Construa o negócio aqui (PMF validado, âncora BR real, recorrente):**
P1 Integrador · P2 GD · P3 Consumo (via canal) · P6 Hub · P7 Canal — e, com ressalva de adoção/timing, **P4 OS-licença (modelo Kraken)** e **P5 Meter MaaS (modelo Intellihub)**.
→ *Todos operáveis com a regulação que já existe (Lei 14.300). Capital baixo-médio. Receita recorrente.*

**T2 — Pré-construa, monetize no gatilho (Lei 15.269, BT nov/2027):**
P8 ACL · P9 Comercializadora · P10 Grid.
→ *Modelo validado em Grupo A; a aposta é (a) a data do gatilho e (b) o BT fechar a R$3–15/UC/mês — o que exige custo de servir ~zero, que é a tese AI-native (P13).*

**T3 — Opcionalidade, nunca caso-base (regra inexistente, VP~0):**
P11 Flex/VPP · P12 Dados · P13 Agentes (como receita) · P14 P2P.
→ *Presença regulatória ativa (Trilha 2), mas a sobrevivência do negócio não pode depender de nenhum deles. P13 é exceção de papel: não é receita, é o **habilitador** que faz o T2 BT fechar e o moat de fronteira.*

---

## 4 · A extensão que falta no mapa de receitas (hardware como licenciamento)

Você pediu explicitamente que o hardware entre como produto de licenciamento (Kraken/gridX/EON). O mapa de receitas atual (R-01…R-11) é **TechCo-cêntrico** — trata hardware como insumo substituível, não como linha de receita. Na disciplina da skill ("se não estiver no mapa, propor adicionar"), **proponho duas formas novas** — sinalizado como item para você autorizar atualizar o `receitas-energia-br.md` / REV-01:

| Nova forma | Camada | Âncora nomeada | Tradução BR | Status |
|---|---|---|---|---|
| **R-12 · Medidor-como-serviço (MaaS) + dados a terceiros** | Hardware/TechCo | **Intellihub: 2,5M+ medidores, MaaS a 20+ varejistas [F]**; Landis+Gyr/EDMI como fornecedores [F] | fee por medidor/mês (OpEx); a aposta é o BR não ter mandato de smart meter ainda [F] → adoção voluntária | Operável (análogo) · **timing BR = aposta [H]** |
| **R-13 · Atacado/attach de Energy Hub (HEMS) ao canal** | Hardware | Air2/GoodWe (device) [F]; modelo de attach de controlador HEMS | margem de device (FOB ~US$34 [E]) + attach de software por cima | Operável hoje · capital de estoque · **internalizar só pós-volume [E]** |

**Por que isso importa estrategicamente:** com R-12 + R-13, a **fundação de hardware vira canal de aquisição e receita**, não custo. O medidor entra na casa/UC (R-12, modelo Intellihub) → a plataforma (P4/P2) é vendida por cima → o Energy Hub (R-13) é attach onde há geração → o software de flexibilidade (P11) fica pré-instalado para quando a regra abrir. É a mesma lógica do Kraken (software como OS licenciado) **somada** à da Intellihub (medidor como porta de entrada) — as duas fundações se reforçando.

---

## Σ · Bear case — o que invalidaria os "validados"

Os kill signals do mapa de receitas, **mais** os específicos das fundações:

1. **Limiar BT não fecha** → custo de servir > R$5/UC/mês no piloto → mata metade do TAM de P8 (e a tese de P13 não entrega o custo ~zero prometido).
2. **Deflator Kraken pior** → 3 conversas de pricing com varejistas abaixo de R$8/UC/ano → P4 (licença OS) não fecha.
3. **Incumbentes no beachhead** (Thunders, Clarke, Way2) → win-rate <20% em bake-off de P1 → *maior lacuna de inteligência atual.*
4. **Success fee mascara PMF** → conversão fee→recorrente <60% em P8 → vira consultoria, não plataforma.
5. **Flexibilidade atrasa 3+ anos** → nenhuma AIR do agregador até dez/2027 → P11 morre (já tratado como T3, então não fere o caso-base — *desde que a narrativa não dependa dele*).
6. **Churn estrutural** → churn de consumidor >3%/mês → corta LTVs de P2/P3 pela metade.
7. **[Hardware] MaaS BR não destrava** → o BR não mandar smart meter e a adoção voluntária ficar abaixo do CAC de instalação → **P5 (R-12) não escala**; a aderência da Intellihub (mercado AU com rollout mandatado) **não transfere direto** — é o risco banana-com-banana mais agudo aqui [H].
8. **[Hardware] Attach não materializa** → integrador não vender o Energy Hub junto → P6/R-13 vira estoque parado (NRE de internalizar excede economia por unidade em M1 [E]).

---

## ⇒ Recomendação e pedido específico

**Recomendação (sequência por real investido, herda a R1 do mapa):**
- **Onda 1 (agora→12m):** P1 (Integrador, beachhead) + P7 (Canal) + P2 (GD) + **P5/P6 (hardware como porta de entrada)**. Software multi-tenant e tenant-aware desde o dia 1.
- **Onda 2 (12–24m):** P4 (licença OS, abre quando há logos) + P8 origina (success fee → take-rate), tudo construído antes do gatilho.
- **Onda 3 (gatilhos):** P8/P9 BT em nov/2027; P11/P12/P14 como opcionalidade ativa na Trilha 2; **P13 (agentes) atravessa todas as ondas** como habilitador de custo, não como receita.

**Pedido específico (o que preciso de você):**
1. **Validar o fatiamento em 14 produtos** — algum produto sobra, falta, ou está no tier errado?
2. **Autorizar a adição de R-12 e R-13** ao mapa de receitas / REV-01 (hardware-licenciamento) — é mudança no documento-fonte, requer seu de-acordo.
3. **Decidir a profundidade do próximo passo:** (a) HTML interativo desta matriz (filtro por persona/tier/fundação); (b) descer ao unit economics de 1–2 produtos T1 (provável P1 Integrador + P5 Meter MaaS) em xlsx com aba de premissas; ou (c) ambos.

*Premissas com rótulo [F]/[E]/[H]/[INPUT] ao longo do texto. Âncoras nomeadas (banana-com-banana) com tradução BR. Bear case incluído. Base: mapa das 11 receitas (REV-01) + personas/cenários + scoring HW/SW. Projeto EOS-DENO · matriz de produtos ideais · cobre fundações software + hardware.*
