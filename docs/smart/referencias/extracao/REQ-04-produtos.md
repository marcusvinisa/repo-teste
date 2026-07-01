> Extração fiel (subagente) do bloco. Fonte: docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/. Preserva taxonomia [F]/[E]/[H]/[INPUT].

I now have everything needed. I have the full target file (14 products, tiers, personas, econ models, bear case, R-12/R-13 proposal), the persona legend, the STATE/LOG with the v1 scope and top-5, the README framing, and the `docs/smart/15` doc with R1-R6 for reconciliation. The xlsx is confirmed binary (Excel 2007+, 15KB). The `receitas-energia-br.md` (REV-01, source of R-01…R-13) is referenced but absent from the repo — I'll flag that.

Let me produce the deliverable.

---

# EOS-DENO · Extração de Requisitos — Bloco 04-produtos

Fonte primária: `docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/04-produtos/eos-deno-matriz-produtos-ideais.md`
Binário a converter: `.../04-produtos/eos-deno-unit-economics-top5.xlsx` (Excel 2007+, ~15 KB) — **unit economics do top-5** (P2, P1, P4, P5, P7) com aba de premissas; NÃO lido (binário). Item a converter para markdown depois.

## 1 · Resumo do bloco

O bloco fatia a oportunidade em **14 produtos ideais** (P1–P14) organizados por **dois eixos**: (a) **fundação de onde a receita nasce** — SW software / HW hardware / ⊕ ambas — tratando o hardware não como insumo, mas como **produto de licenciamento a terceiros** (modelo Kraken/gridX/Intellihub); (b) **maturidade de PMF em 3 tiers** — T1 validado (âncora BR real, operável com Lei 14.300), T2 gatilhado (espera Lei 15.269, BT nov/2027), T3 aposta/opcionalidade (regra inexistente, VP~0 no caso-base). Princípio econômico central: o **integrador/EPC (INT) é a única persona que fecha unit economics hoje sem gatilho regulatório** e serve de **máquina de CAC subsidiado** para as demais camadas — o LTV do consumidor BT (R$165–790 [E]) não sustenta venda direta paga [F]. Daí o beachhead ser P1, não o maior TAM. Achado-âncora: **P5 Meter MaaS não fecha como SaaS** (LTV:CAC ~1,4x, payback ~69m [E/INPUT]) — é infraestrutura/project-finance, não SaaS. O bloco também **propõe duas novas formas de receita** (R-12 MaaS e R-13 attach de Energy Hub) para estender o mapa TechCo-cêntrico R-01…R-11, e inclui bear case com 8 kill signals. Grande parte do unit economics é **[E]/[H]/[INPUT]** — a validar com descoberta de 2–3 integradores antes de tratar como fato.

## 2 · Portfólio — 14 produtos

Legenda persona: **INT** Integrador/EPC (beachhead) · **CON** Consumidor/Prosumidor · **COM** Comercializadora/Varejista · **GER** Gerador (GD) · **AGG** Agregador/VPP · **DSO** Distribuidor · **ORQ** Orquestrador (opera a plataforma). Fundação: SW=software · HW=hardware · ⊕=ambas. Modelo econômico (contexto STATE): **A** = dono do book · **B** = operador AI-native white-label (tese durável) · **C** = compra de distressed. *Nota: o `.md` de 04-produtos NÃO rotula A/B/C por produto — o mapeamento abaixo é inferência do enquadramento (STATE) + modelo de negócio de cada linha; marcado como [E/inferência], a confirmar.*

| id | Produto | Fund. | Tier PMF | Persona-alvo | Modelo econ. A/B/C [E/inf.] | Modelo de negócio (fonte) | Receita | Tag/destaque |
|---|---|:--:|:--:|---|:--:|---|:--:|---|
| **P1** ★ | **EOS Integrador** — suíte de operação do EPC (monitoramento, O&M, frota, comissionamento, diagnóstico remoto) | SW | **T1** | INT | **B** | SaaS por usina/mês + por integrador/suíte | R-01 (+R-07, R-10) | **BEACHHEAD · V1** |
| **P2** ★ | **EOS GD** — orquestração de GD compartilhada (rateio créditos Lei 14.300, billing, fidelização) | SW | **T1** | GER, COM, CON | B | SaaS por UC/mês + take | R-06 | **TOP-5 (nº1 aderência×receita)** |
| **P3** | **EOS Consumo** — app do dono + autoconsumo + otimização (HEMS na nuvem) | ⊕ | **T1\*** | CON | B | assinatura embutida (vendida via INT/COM) | attach R-01/R-06/R-02 | \*T1 na categoria, ressalva de canal (venda direta paga fraca) |
| **P4** ★ | **EOS OS (licença)** — licenciamento do energy OS por UC (back-office varejo: CRM, billing, dados) | SW | **T1.5** | COM | B | licença por conta/ano (white-label) | R-02 | **TOP-5** · modelo Kraken; adoção BR = aposta |
| **P5** ★ | **EOS Meter MaaS** — medidor-como-serviço a varejistas/DSOs (HW + dados + comunicação geridos) | HW | **T1.5** | COM, DSO | **C** (infra/project-fin.) | fee por medidor/mês (OpEx, não CapEx) | **R-12 (propor)** | **TOP-5** · **NÃO fecha como SaaS** (ver REQ-PROD-09) |
| **P6** | **EOS Hub** — Energy Hub/controlador HEMS (atacado a integradores, onde há geração) | HW | **T1** | INT, CON | A/C | margem de hardware + attach de software | **R-13 (propor)** | break-even vs SKU integrado ~35% adoção [E] |
| **P7** ★ | **EOS Canal** — white-label + rev-share (originação de crédito, distribuição, marketplace) | ⊕ | **T1** | INT, COM | B | rev-share / take de originação 1–4% | R-07, R-10 | **TOP-5** · alavanca ativo-âncora |
| **P8** | **EOS ACL** — migração ao mercado livre (success fee) + gestão BT contínua (take-rate) | SW | **T2** | COM, CON | B | success fee one-off → take-rate recorrente | R-03 → R-04 | gatilho Lei 15.269, BT nov/2027; BT só fecha R$3–15/UC/mês [H] |
| **P9** | **EOS Comercializadora** — spread de comercialização de energia (entidade regulada) | SW→Reg | **T2** | COM, GER | **A** (dono do book) | spread R$/MWh | R-05 | **capital ALTO** (garantias+balanço) — gate D2 |
| **P10** | **EOS Grid** — sinais de rede p/ DSO (RCR/§14a/DOE, curtailment, hosting capacity) | ⊕ | **T2/T3** | DSO | B | fee de serviço / contrato distribuidora | deriva R-12 + serviço | depende de programas do DSO existirem no BR [H] |
| **P11** | **EOS Flex / VPP** — agregação + bidding + serviços ancilares | SW | **T3** | AGG, GER, DSO | B | rev-share de flexibilidade | R-08 | figura do agregador de RED inexistente [F]; merchant não fecha (~R$4.500 vs ~R$600/MW) [F] — VP~0 |
| **P12** | **EOS Dados** — inteligência/API sobre dado proprietário | SW | **T3** | todas, Fintech | B | API / assinatura de dados | R-09 | tardio por desenho (consequência do moat) |
| **P13** | **EOS Agentes** — operação AI-native por agentes (camada transversal, não produto isolado) | SW | **T3** | ORQ, todas | B (habilitador) | embutido (reduz custo de servir → habilita P8 BT) | (habilitador) | **ninguém tem em LLM** — moat de fronteira; NÃO é receita |
| **P14** | **EOS P2P** — energy trading peer-to-peer | SW | **T3** | CON | B | take transacional | R-11 | sandbox, WTP fraca — feature de marca; Powerledger/LO3 pivotaram [E] |

★ = **top-5** (P2 · P1 · P4 · P5 · P7). **P1 = beachhead, escopo do V1.** (Fora do V1, deliberado: VPP, CCEE, agent-fabric, otimização, mercado livre, os 18 cenários.)

**Nota epistêmica sobre A/B/C:** a coluna de modelo econômico é **inferência [E]** — o documento 04-produtos não atribui A/B/C. Pela tese durável do STATE (B = operador AI-native white-label), a maioria dos produtos de plataforma cai em **B**; **P9 Comercializadora** é o único claramente **A** (dono do book, entidade regulada, capital alto); **P5 Meter MaaS** aproxima-se de **C/infra** (project-finance, distressed/economia de infraestrutura). **Item a validar com o Marcus.**

## 3 · Requisitos de produto/negócio (`REQ-PROD-NN`)

Relevância: **[V1]** entra na fatia mínima do beachhead · **[FASE-2+]** onda 2/gatilhos · **[CONTEXTO]** decisão/princípio de portfólio.

| ID | Enunciado | Tag(s) | Relevância | Fonte |
|---|---|---|---|---|
| **REQ-PROD-01** | Fatiar a oportunidade em **14 produtos** distintos (P1–P14) por persona × caso de uso × modelo × receita, cada linha um "produto ideal". | [F] portfólio aprovado | CONTEXTO | 04-produtos §1; STATE (14 produtos aprovados) |
| **REQ-PROD-02** | Classificar cada produto em **3 tiers de PMF** (T1 validado / T2 gatilhado por Lei 15.269 BT nov/2027 / T3 aposta VP~0) e tratar cada tier por sua regra (construir / pré-construir / opcionalidade). | [F] tiers; [F] Lei 15.269 | CONTEXTO | 04-produtos §0 tabela de tiers |
| **REQ-PROD-03** | **Beachhead = P1 EOS Integrador (INT)** — única persona com receita primária operável hoje; funciona como **máquina de CAC subsidiado** das demais camadas. Sequência decide por "quem fecha unit economics sem gatilho", não por maior TAM. | [F] LTV BT não sustenta CAC; [E] pricing | **V1** | 04-produtos §0 princípio; STATE escopo v1 |
| **REQ-PROD-04** | **P1** monetiza como **SaaS por usina/mês + por integrador/suíte** (R-01, +R-07/R-10); faixa R$1–5/usina/mês a R$200–1.500/mês/integrador. Concorrentes reais: SolarZ, Sunne, GDASH, SolarMaker, Solar Next. | [F] concorrentes; **[E][INPUT]** preços | **V1** | 04-produtos §1 P1 |
| **REQ-PROD-05** | **P2 EOS GD** — rateio de créditos Lei 14.300, billing e **fidelização (dor nº1 [F])**; SaaS por UC/mês + take (R-06); R$2–6/UC/mês [H]. Âncora Órigo (R$416,5M / 91k UCs [E]; desconto 14–15% [F]). | [F] fidelização/desconto; [E] Órigo; [H] preço | FASE-2+ (top-5, onda 1) | 04-produtos §1 P2 |
| **REQ-PROD-06** | **P3 EOS Consumo** é **T1 com ressalva de canal**: tem PMF, mas o modelo de venda validado é **via integrador/comercializadora**, NÃO venda direta paga ao consumidor BT (LTV R$165–790 [E] não sustenta CAC direto [F]). Assinatura geralmente **embutida**. | [F] venda direta fraca; [E] LTV | CONTEXTO (design de canal) | 04-produtos §1 P3 + nota\* |
| **REQ-PROD-07** | **P4 EOS OS** — licenciamento white-label do energy OS por conta/ano (R-02); modelo Kraken (US$500M ARR / 70M contas ≈ US$7,1/conta/ano [F]); tradução BR R$8–35/UC/ano com **deflator 50–70% [E]**. **Modelo validado, adoção BR = aposta**; LTV:CAC sensível ao tamanho do deal. | [F] Kraken; **[E]** deflator/preço BR | FASE-2+ (onda 2, "abre com logos") | 04-produtos §1 P4; LOG aprend. #4 |
| **REQ-PROD-08** | **R-12 (Medidor-MaaS + dados a terceiros)** e **R-13 (attach de Energy Hub ao canal)** **autorizadas** para o mapa de receitas — hardware entra como **linha de receita/canal de aquisição**, não como custo/insumo. Requer refletir no REV-01. | [F] decisão autorizada (STATE) | CONTEXTO → FASE-2+ | STATE última decisão (2); 04-produtos §4; LOG 2026-06-30 |
| **REQ-PROD-09** | **ACHADO-ÂNCORA: P5 Meter MaaS NÃO fecha como SaaS** — **LTV:CAC ~1,4x, payback ~69m [E/INPUT]**. É **economia de infraestrutura → financiar como project finance / green loans** (modelo Intellihub, ~A$3 bi em green loans [F]). Âncora AU é **mercado mandatado**; BR sem mandato de smart meter → **timing não transfere** (risco banana-com-banana mais agudo). | **[E/INPUT]** ratio/payback; [F] Intellihub green loans; [H] timing BR | CONTEXTO (kill-check) | Achado-âncora README/STATE; 04-produtos §1 P5 + §4 R-12 + bear case #7 |
| **REQ-PROD-10** | **R-12 (P5)**: fee por medidor/mês (**OpEx, não CapEx**); Intellihub 2,5M+ medidores, MaaS a 20+ varejistas [F]; fornecedores Landis+Gyr/EDMI [F]; adoção BR **voluntária** (sem mandato) = aposta [H]. | [F] Intellihub/fornecedores; [H] adoção BR | FASE-2+ (top-5) | 04-produtos §4 tabela R-12 |
| **REQ-PROD-11** | **R-13 (P6 EOS Hub)**: margem de device (FOB ~US$34 [E]) + attach de software; **break-even vs SKU integrado ~35% adoção [E]**; Air2/GoodWe provam o device [F]; **internalizar só pós-volume [E]** (NRE excede economia por unidade em M1). | [F] device; **[E]** FOB/break-even/timing | FASE-2+ (onda 1 como porta de entrada) | 04-produtos §1 P6 + §4 R-13 + bear #8 |
| **REQ-PROD-12** | **P13 EOS Agentes** é **exceção de papel**: NÃO é linha de receita — é o **habilitador** que leva custo de servir a ~zero, o que faz o **R-04 BT (P8) fechar** a R$3–15/UC/mês e constitui o moat de fronteira. **Ninguém tem em LLM [scoring].** (Deliberadamente FORA do V1 como agent-fabric.) | [scoring] teto vazio; [H] custo~zero | CONTEXTO (atravessa ondas) | 04-produtos §1 P13, §3 T3 |
| **REQ-PROD-13** | **Sequência recomendada por real investido:** Onda 1 (→12m) P1+P7+P2+P5/P6; Onda 2 (12–24m) P4+P8 (origina); Onda 3 (gatilhos) P8/P9 BT nov/2027, P11/P12/P14 opcionalidade, P13 atravessa tudo. **Software multi-tenant e tenant-aware desde o dia 1.** | [E] sequência; [F] gatilho | CONTEXTO (roadmap) | 04-produtos §Recomendação (ondas) |
| **REQ-PROD-14** | **Disciplina de escopo V1 (STATE):** construir **apenas P1** sobre o **smart-meter existente** (não o ODM); fluxo Smart→ingestão→time-series→modelo de ativo→**portal do integrador**. **Camada de abstração de device (S2.3) desde a 1ª linha** — troca p/ ODM = configuração, não reescrita. | [F] decisão de escopo | **V1** | STATE; README §Escopo |
| **REQ-PROD-15** | **Bear case — 8 kill signals** a monitorar: (1) BT não fecha (custo>R$5/UC/mês); (2) deflator Kraken pior (<R$8/UC/ano em 3 conversas) mata P4; (3) **incumbentes no beachhead (Thunders/Clarke/Way2), win-rate <20% em bake-off de P1 = maior lacuna de inteligência atual**; (4) success fee mascara PMF (conversão fee→recorrente <60%); (5) flex atrasa 3+ anos; (6) churn >3%/mês corta LTV P2/P3; (7) MaaS BR não destrava; (8) attach de Hub não materializa. | [H]/[E] kill signals | CONTEXTO (gates) | 04-produtos §Σ bear case |

## 4 · Modelo de receita — como os produtos monetizam

**Mapa R-01…R-13** (fonte declarada: `receitas-energia-br.md` / REV-01 — **arquivo referenciado mas AUSENTE do repo**; ver §5). R-01…R-11 é o mapa TechCo-cêntrico existente; **R-12 e R-13 são as duas formas novas propostas e já autorizadas** (REQ-PROD-08) para tratar hardware como licenciamento.

| Receita | Como monetiza | Produto(s) | Fund. |
|---|---|---|---|
| R-01 | SaaS por usina/mês + por integrador (suíte O&M/frota) | **P1** (+P3 attach) | SW |
| R-02 | Licença white-label do energy OS por conta/ano | **P4** (+P3) | SW |
| R-03 | Success fee one-off de migração ACL | **P8** | SW |
| R-04 | Take-rate recorrente de gestão BT (fecha só com custo~zero de P13) | **P8** | SW |
| R-05 | Spread de comercialização R$/MWh (entidade regulada) | **P9** | Reg |
| R-06 | SaaS por UC/mês + take de GD compartilhada | **P2** (+P3) | SW |
| R-07 | Rev-share / take de originação de crédito (1–4%) | **P7** | ⊕ |
| R-08 | Rev-share de flexibilidade (ancilares/VPP) | **P11** | SW |
| R-09 | API / assinatura de dados | **P12** | SW |
| R-10 | Distribuição / marketplace (originação) | **P1, P7** | ⊕ |
| R-11 | Take transacional P2P | **P14** | SW |
| **R-12** (novo) | Fee por medidor/mês — **OpEx MaaS + dados a terceiros** | **P5** (deriva P10) | HW |
| **R-13** (novo) | Margem de device (Energy Hub) + attach de software | **P6** | HW |

**Reconciliação com `docs/smart/15-modelo-de-negocio-e-precificacao.md` (R1–R6, `[PROPOSTA]`):** o doc-15 é a proposta anterior/Smart, mais grosseira (6 fontes); o mapa R-01…R-13 do EOS-DENO é o refinamento. Correspondência:

| doc-15 (R1–R6) | EOS-DENO (R-01…R-13) | Observação |
|---|---|---|
| **R1** Hardware (venda/locação Gateway/Meter) | **R-13** (attach Hub) + **R-12** (MaaS, mas como OpEx/serviço, não venda) | doc-15 trata HW como venda/locação de CapEx; EOS-DENO **substitui por MaaS OpEx (R-12) + attach (R-13)** — mudança de tese (hardware = licenciamento, não insumo). |
| **R2** Assinatura SaaS por UC | **R-01** (P1) + **R-06** (P2, por UC) + **R-02** (P4, licença) | doc-15 colapsa em uma linha; EOS-DENO separa por produto/persona. |
| **R3** Fee de VPP/grid services | **R-08** (P11 flex) + parte de P10 grid | Ambos marcam como **opcional/gradual, não base do plano** (doc-15 §4; EOS-DENO T3 VP~0). |
| **R4** Fee de GD compartilhada | **R-06** (P2) | Mesma dor; EOS-DENO adiciona take + fidelização. |
| **R5** Licença white-label / API | **R-02** (P4 OS) + **R-07/R-10** (P7 canal) + **R-09** (P12 dados/API) | doc-15 junta white-label e API; EOS-DENO separa OS-licença, canal e dados. |
| **R6** Serviços profissionais (comissionamento/suporte) | *sem linha 1:1* — embutido em **P1** (comissionamento é caso de uso de INT), não é linha de receita própria | EOS-DENO trata comissionamento como **funcionalidade do produto P1**, não como fonte de receita separada. |

Modelo/opção do doc-15: recomenda **A (HW+SaaS)** base + **C (canal/B2B2C)** escala. Isso é **consistente** com a tese EOS-DENO, porém o STATE redefine os rótulos econômicos (A dono do book / B operador AI-native white-label / C compra de distressed) — **os "A/B/C" do doc-15 e os "A/B/C" do STATE NÃO são o mesmo esquema** (colisão de nomenclatura a resolver; ver §5).

## 5 · Itens [INPUT]/[H] a validar com descoberta de integradores

**Metas de descoberta (STATE/README): rodar com 2–3 integradores em paralelo ao build; transformar [H]/[INPUT] em evidência antes de tratar como fato.**

1. **[INPUT] Preços de P1** (R-01): R$1–5/usina/mês e R$200–1.500/mês/integrador — validar disposição a pagar e faixa real. *(REQ-PROD-04)*
2. **[H] Preço de P2** (R-06): R$2–6/UC/mês — confirmar com gestores de GD. *(REQ-PROD-05)*
3. **[E/INPUT] Unit economics de P5 Meter MaaS**: LTV:CAC ~1,4x e payback ~69m — **validar contra o xlsx `eos-deno-unit-economics-top5.xlsx` (a converter)** e testar se project-finance/green-loan fecha no BR. *(REQ-PROD-09)*
4. **[H] Timing/adoção MaaS BR** (R-12): BR sem mandato de smart meter → adoção voluntária acima do CAC de instalação? Risco banana-com-banana AU→BR mais agudo. *(REQ-PROD-09/10, bear #7)*
5. **[E] Deflator Kraken p/ P4** (R-02): R$8–35/UC/ano com deflator 50–70% — 3 conversas de pricing com varejistas; abaixo de R$8 mata P4. *(REQ-PROD-07, bear #2)*
6. **[E] Attach e FOB de P6/Energy Hub** (R-13): FOB ~US$34, break-even vs SKU integrado ~35% adoção; integrador vende o Hub junto? *(REQ-PROD-11, bear #8)*
7. **[H] Win-rate no beachhead vs incumbentes** (Thunders, Clarke, Way2): **maior lacuna de inteligência atual** — bake-off de P1; win-rate <20% invalida. *(bear #3)*
8. **[INPUT] Alavanca do ativo-âncora em P7** (canal/rev-share 1–4%): originação de crédito/distribuição via empresa-âncora. *(REQ-PROD; P7)*
9. **[H] Custo de servir ~zero (P13)**: a tese AI-native realmente entrega custo→zero que faz o R-04 BT (P8) fechar a R$3–15/UC/mês? *(REQ-PROD-12, bear #1)*
10. **[H] Churn de consumidor** (>3%/mês corta LTV P2/P3 pela metade). *(bear #6)*

**Pendências de reconciliação / gaps de documento (para o Marcus):**
- **`receitas-energia-br.md` (REV-01) não existe no repo** — é a fonte declarada de R-01…R-13. Sem ele, R-01…R-11 foram reconstruídos a partir das colunas "Receita" da matriz de produtos; **R-12/R-13 autorizadas mas ainda a refletir no REV-01** (decision-gate aberto no STATE).
- **Colisão de nomenclatura A/B/C:** o esquema do STATE (A dono do book / B operador white-label / C distressed) difere do esquema do doc-15 (A HW+SaaS / B HaaS / C canal / D share-de-economia). O `.md` de 04-produtos **não rotula produtos com A/B/C** — a coluna de modelo econômico na §2 é **inferência [E]**, a confirmar.
- **`eos-deno-unit-economics-top5.xlsx`** (binário, ~15KB, Excel 2007+): contém o unit economics do **top-5 (P2,P1,P4,P5,P7)** com aba de premissas; **converter para markdown** para expor os números que hoje aparecem só como [E]/[INPUT] no texto (LTV:CAC de P5, deflator de P4, break-even de P6 etc.).
