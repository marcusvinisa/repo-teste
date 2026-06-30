# EOS-DENO · Matriz de Produtos Ideais (fonte)

> **Documento-fonte fornecido pelo usuário** (estudo curado EOS-DENO), reproduzido aqui com codificação normalizada (UTF-8). É a base da revisão em [`../matriz-produtos-revisao.md`](../matriz-produtos-revisao.md). Conteúdo = curado e revisado pelo usuário; tratado como fonte de alta confiança.
>
> Rótulos: **[F]** fato com fonte · **[E]** estimativa fundamentada · **[H]** hipótese a validar · **[INPUT]** placeholder. Base citada pela fonte: mapa das 11 receitas (`receitas-energia-br.md`, REV-01) + personas/cenários + scoring de software/hardware. *(Esse mapa de 11 receitas é externo a este repo — ver reconciliação na revisão.)*

---

## 0 · A lógica do fatiamento (antes da matriz)

**Dois eixos organizam tudo.**

**Eixo 1 — Fundação (de onde a receita nasce).** O hardware não é só device de consumidor; é **produto de licenciamento/atacado a terceiros** — o que a Intellihub faz com medidor+plataforma (MaaS a 20+ varejistas [F]), o que o Kraken faz com software (US$ ~7,1/conta/ano × 70M contas [F]), o que a gridX faz white-label. O portfólio tem **duas fundações**, cada uma monetizável **diretamente** (vender ao usuário final) **e como licenciamento** (vender a quem serve o usuário final).

**Eixo 2 — Maturidade de PMF.** Três tiers:

| Tier | Definição | Regra de tratamento |
|---|---|---|
| **T1 · PMF validado** | Categoria com PMF real **no BR hoje** (âncora BR nomeada) ou análogo forte + receita recorrente + operável já | **Construir o negócio aqui.** É o caso-base. |
| **T2 · PMF gatilhado** | Modelo validado em análogo, mas **espera uma regra com data**: Lei 15.269/2025 abre Grupo B em 2027–2028 [F] | **Pré-construir, monetizar no gatilho.** |
| **T3 · Aposta / opcionalidade** | Depende de **regra que não existe** (figura do agregador de RED, P2P) — VP ~0 no caso-base [F] | **Opcionalidade.** Presença regulatória ativa, mas a narrativa **não** depende disso. |

**Lição da Intellihub:** prova que o modelo combinado medidor+plataforma+MaaS monetiza [F] — mas **não tem** a camada AI-native (agentes) nem a CCEE-nativa. A fundação (T1/T2) é validada por ela; as apostas do EOS-DENO são exatamente os dois domínios que ela e o Kraken deixam vazios — **CCEE/BR** e **agent-fabric**. O moat não está em existir como medidor+plataforma; está nas duas camadas que ninguém ocupa.

**Princípio de qualidade:** o **integrador/EPC é a única persona com receita primária operável hoje** e funciona como **máquina de CAC subsidiado** das demais camadas — o LTV do consumidor BT individual (R$ 165–790 [E]) não sustenta venda direta paga [F]. O beachhead não é "o maior mercado", é "o único que fecha unit economics sem gatilho regulatório".

---

## 1 · Matriz-mestre de produtos (as duas fundações)

`F` = fundação (SW software / HW hardware / ⬚ ambas).

| # | Produto | F | Persona(s) | Caso de uso / cenário | Modelo de negócio | Receita | Tier | Âncora / evidência [tag] |
|---|---|:--:|---|---|---|---|:--:|---|
| **P1** | **EOS Integrador** — suíte de operação do EPC (monitoramento, O&M, frota, comissionamento, diagnóstico remoto) | SW | INT | transversal (todo ativo instalado) | SaaS por usina/mês + por integrador/suíte | R-01 (+R-07, R-10) | **T1** | SolarZ, Sunne, GDASH, SolarMaker, Solar Next existem [F]; R$1–5/usina/mês a R$200–1.500/mês/integrador [E][INPUT] |
| **P2** | **EOS GD** — orquestração de GD compartilhada (rateio de créditos Lei 14.300, billing, fidelização) | SW | GER, COM, CON | B0–B4 | SaaS por UC/mês + take | R-06 | **T1** | Órigo R$416,5M/91k UCs [E]; desconto 14–15% [F]; fidelização = dor nº1 [F]; R$2–6/UC/mês [H] |
| **P3** | **EOS Consumo** — app do dono + autoconsumo + otimização (HEMS na nuvem) | ⬚ | CON | A1–A4 | assinatura (geralmente **embutida**, vendida via INT/COM) | attach a R-01/R-06/R-02 | **T1\*** | Zerofy/Tibber provam app HEMS [F]; **venda direta paga é fraca** — LTV BT R$165–790 [E] não sustenta CAC direto [F] |
| **P4** | **EOS OS (licença)** — licenciamento do energy OS por UC (back-office de varejo: CRM, billing, dados) | SW | COM | carteira de varejo | licença por conta/ano (white-label) | R-02 | **T1.5** | Kraken US$500M ARR/70M contas → US$7,1/conta/ano [F]; **modelo validado, adoção BR é aposta** — R$8–35/UC/ano c/ deflator 50–70% [E] |
| **P5** | **EOS Meter MaaS** — medidor-como-serviço a varejistas/DSOs (hardware + dados + comunicação geridos) | HW | COM, DSO | transversal (N0 base) | fee por medidor/mês (OpEx, não CapEx) | **R-12 (propor)** | **T1.5** | **Intellihub: 2,5M+ medidores, 20+ varejistas, MaaS [F]**; modelo validado, **timing BR é aposta** (sem mandato de smart meter ainda [F]) |
| **P6** | **EOS Hub** — Energy Hub/controlador HEMS (atacado a integradores, onde há geração) | HW | INT, CON | A1–A5, B/C com ativo | margem de hardware + attach de software | **R-13 (propor)** | **T1** | Air2/GoodWe provam o device [F]; FOB ~US$34 [E]; break-even vs SKU integrado ~35% adoção [E] |
| **P7** | **EOS Canal** — white-label + rev-share (originação de crédito, distribuição, marketplace) | ⬚ | INT, COM | transversal | rev-share / take de originação 1–4% | R-07, R-10 | **T1** | 1KOMMA5° €520M lucrativa, install-led [F]; alavanca ativo Solfácil [INPUT] |
| **P8** | **EOS ACL** — migração ao mercado livre (success fee) + gestão BT contínua (take-rate) | SW | COM, CON | C0–C4 | success fee one-off → take-rate recorrente | R-03 → R-04 | **T2** | Gatilho Lei 15.269, BT nov/2027 [F]; economia BT ~19% [F]; gestão Grupo A R$500–2.500/UC/mês [E], **BT só fecha a R$3–15/UC/mês [H]** |
| **P9** | **EOS Comercializadora** — spread de comercialização de energia (entidade regulada) | SW+Reg | COM, GER | carteira ACL | spread R$/MWh | R-05 | **T2** | Gerador líquido GD R$80–140/MWh [F]; **capital ALTO (garantias+balanço) — gate D2** |
| **P10** | **EOS Grid** — sinais de rede para o DSO (RCR/§14a/DOE, curtailment, hosting capacity) | ⬚ | DSO | A5, B5 | fee de serviço / contrato com distribuidora | (deriva R-12 + serviço) | **T2/T3** | AutoGrid/Intellihub fazem p/ DSO [F]; **depende de programas do DSO existirem no BR [H]** |
| **P11** | **EOS Flex / VPP** — agregação + bidding + serviços ancilares | SW | AGG, GER, DSO | N5, arranjo C | rev-share de flexibilidade | R-08 | **T3** | Next Kraftwerke >10 GW Europa [F]; **figura do agregador de RED inexistente BR [F]; merchant não fecha (~R$4.500 vs ~R$600/MW) [F] → VP ~0 caso-base** |
| **P12** | **EOS Dados** — inteligência/API sobre o dado proprietário | SW | todas, Fintech | transversal | API / assinatura de dados | R-09 | **T3** | comparáveis BR fracos [H]; 1º cliente plausível Fintech Solfácil (score de ativo) [INPUT]; **tardio por desenho** |
| **P13** | **EOS Agentes** — operação AI-native por agentes (camada transversal, não produto isolado) | SW | ORQ, todas | transversal | embutido (reduz custo de servir → habilita P8 BT) | (habilitador) | **T3** | **ninguém tem em LLM [scoring]**; é o moat de fronteira + o que faz o R-04 BT fechar (custo de servir ~zero) |
| **P14** | **EOS P2P** — energy trading peer-to-peer | SW | CON | transversal | take transacional | R-11 | **T3** | SCEE compensa créditos, não vende energia (REN 1.000) [F]; Powerledger/LO3 pivotaram p/ flexibilidade [E]; **sandbox, WTP fraca → feature de marca** |

\* **P3 é T1 na categoria mas com ressalva de canal:** o produto tem PMF, mas o *modelo de venda* validado é via integrador/comercializadora, não venda direta paga ao consumidor BT.

---

## 2 · Matriz por persona (validado vs. aposta)

| Persona | T1 · Validado (operável hoje) | T2 · Gatilhado (Lei 15.269 / DSO) | T3 · Aposta (VP~0 caso-base) |
|---|---|---|---|
| **INT** Integrador/EPC | **P1 EOS Integrador** + **P6 EOS Hub** + **P7 Canal** — *o beachhead, máquina de CAC* | — | — |
| **CON** Consumidor | **P3 EOS Consumo** (via canal) + autoconsumo | **P8 EOS ACL** (migração+gestão BT) | **P14 P2P** |
| **GER** Gerador (GD) | **P2 EOS GD** (rateio+billing) + **P7** | **P9 Comercializadora** (spread) | **P11 Flex/VPP** |
| **COM** Comercializadora | **P4 EOS OS** (licença) + **P5 Meter MaaS** + **P2** | **P8 ACL** + **P9** | — |
| **AGG** Agregador/VPP | — | — | **P11 Flex/VPP** (o produto inteiro é aposta) |
| **DSO** Distribuidor | **P5 Meter MaaS** (parcial) | **P10 EOS Grid** | **P11** (ancilares) |
| **ORQ** Orquestrador | **P13 Agentes** (operação) + plataforma multi-tenant | — | — |

**Leitura:** personas com negócio fechável hoje = **INT, GER, COM** (e CON via canal). **AGG é 100% aposta**. **DSO é misto** (MaaS hoje, grid services depende de programa). Confirma o beachhead: começar por quem paga hoje (INT → GER/COM), não por quem só paga no futuro (AGG).

---

## 3 · Os três blocos, destilados

- **T1 — Construa aqui (PMF validado, Lei 14.300, recorrente):** P1 · P2 · P3 (via canal) · P6 · P7 — e, com ressalva de adoção/timing, **P4 (modelo Kraken)** e **P5 (modelo Intellihub)**. Capital baixo-médio.
- **T2 — Pré-construa, monetize no gatilho (Lei 15.269, BT nov/2027):** P8 · P9 · P10. A aposta é (a) a data do gatilho e (b) o BT fechar a R$3–15/UC/mês — o que exige custo de servir ~zero (tese AI-native, P13).
- **T3 — Opcionalidade, nunca caso-base (regra inexistente, VP~0):** P11 · P12 · P13 (como receita) · P14. P13 é exceção de papel: não é receita, é o **habilitador**.

---

## 4 · Extensão proposta ao mapa de receitas (hardware como licenciamento)

O mapa de receitas EOS-DENO (R-01…R-11) é TechCo-cêntrico — trata hardware como insumo. **Proposta de duas formas novas** (requer autorização do usuário para alterar o documento-fonte `receitas-energia-br.md` / REV-01):

| Nova forma | Camada | Âncora nomeada | Tradução BR | Status |
|---|---|---|---|---|
| **R-12 · Medidor-como-serviço (MaaS) + dados a terceiros** | Hardware/TechCo | **Intellihub: 2,5M+ medidores, MaaS a 20+ varejistas [F]**; Landis+Gyr/EDMI fornecedores [F] | fee por medidor/mês (OpEx); aposta = BR sem mandato de smart meter [F] → adoção voluntária | Operável (análogo) · **timing BR = aposta [H]** |
| **R-13 · Atacado/attach de Energy Hub (HEMS) ao canal** | Hardware | Air2/GoodWe (device) [F]; attach de controlador HEMS | margem de device (FOB ~US$34 [E]) + attach de software | Operável hoje · capital de estoque · **internalizar só pós-volume [E]** |

---

## Σ · Bear case (o que invalidaria os "validados")

1. **Limiar BT não fecha** — custo de servir > R$5/UC/mês no piloto → mata metade do TAM de P8 (e P13 não entrega o custo ~zero prometido).
2. **Deflator Kraken pior** — 3 conversas de pricing com varejistas abaixo de R$8/UC/ano → P4 não fecha.
3. **Incumbentes no beachhead** (Thunders, Clarke, Way2) — win-rate <20% em bake-off de P1 → *maior lacuna de inteligência atual*.
4. **Success fee mascara PMF** — conversão fee→recorrente <60% em P8 → vira consultoria.
5. **Flexibilidade atrasa 3+ anos** — nenhuma AIR do agregador até dez/2027 → P11 morre (já é T3).
6. **Churn estrutural** — churn de consumidor >3%/mês → corta LTVs de P2/P3.
7. **[Hardware] MaaS BR não destrava** — adoção voluntária abaixo do CAC → P5 (R-12) não escala; aderência da Intellihub (AU, rollout mandatado) **não transfere direto** [H].
8. **[Hardware] Attach não materializa** — integrador não vender o Hub junto → P6/R-13 vira estoque parado [E].

---

## ✓ Pedidos da fonte (a serem respondidos pelo usuário/revisão)

1. **Validar o fatiamento em 14 produtos** — algum produto sobra, falta, ou está no tier errado?
2. **Autorizar a adição de R-12 e R-13** ao mapa de receitas / REV-01 (hardware-licenciamento).
3. **Decidir a profundidade do próximo passo:** (a) HTML interativo da matriz; (b) unit economics de 1–2 produtos T1 (P1 + P5) em xlsx; ou (c) ambos.

> Recomendação da fonte — **Onda 1 (agora–12m):** P1 + P7 + P2 + P5/P6 (hardware como porta de entrada). **Onda 2 (12–24m):** P4 + P8 (success fee → take-rate). **Onda 3 (gatilhos):** P8/P9 BT nov/2027; P11/P12/P14 como opcionalidade; **P13 atravessa todas as ondas** como habilitador de custo.
