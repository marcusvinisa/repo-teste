> Extração fiel (subagente) do bloco. Fonte: docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/. Preserva taxonomia [F]/[E]/[H]/[INPUT].

I now have all three documents. I have the source dossier (01-mercado), the reconciliation target (02-contexto-regulatorio-mercado-br.md), and the epistemic convention. The v1 scope is clear: the integrator/EPC portal on existing smart-meter hardware, with VPP/CCEE/mercado livre explicitly out of v1. I have everything needed to produce the faithful extraction.

---

# Bloco 01-mercado — Extração de Fatos (EOS-DENO)

**Fonte extraída:** `docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/01-mercado/mercado-energia-br-gd-acl-jun2026.md`
**Reconciliação com:** `docs/smart/02-contexto-regulatorio-mercado-br.md`

> Nota epistêmica: o dossiê-fonte usa marcação própria (Fonte / data por número + caveats). A taxonomia [F]/[E]/[H]/[INPUT] foi aplicada com fidelidade — `[F]` só onde o dossiê cita fonte; projeções auto-reportadas e metas de players ficam `[E]/[H]` conforme os próprios caveats do documento. Nenhuma fonte foi inventada.

---

## 1. Resumo do bloco

O mercado BR de energia em baixa tensão está em ponto de inflexão estrutural. A **GD compartilhada** (energia solar por assinatura, base regulatória REN 482→687→Lei 14.300→REN 1.000/1.059) acumula **~1,55 milhão de UCs** e **~2,74 GW**, operada por "dezenas de gestoras" lideradas por Órigo e Cemig SIM. O **ACL** reúne **~85,4 mil UCs** (**42% do consumo nacional**), hoje restrito ao Grupo A. A **Lei 15.269/2025 (24/11/2025)** destrava a baixa tensão (Grupo B) com cronograma legal: comercial/industrial BT em **nov/2027**, residencial em **nov/2028**, criando o **SUI** e um TAM de **~89–92 milhões de UCs / ~R$ 35,8 bi/ano**. A mesma lei reconhece o **armazenamento (BESS)** como atividade autônoma (regulamentação ANEEL em **02/jun/2026**). O sinal de preço no cativo é **tarifa branca + bandeiras**; a tarifação horária plena só existe no livre. **Para o v1 do integrador/EPC, quase todo esse conteúdo é contexto de fases futuras** — o dossiê é dimensionamento de TAM/SAM (ACL, VPP, agregador), não requisito do portal de monitoramento/frota que se constrói agora.

---

## 2. Fatos [F] com fonte

Marcados [F] = dossiê cita fonte explícita. Onde a fonte é player auto-reportado/projeção, movo para [E]/[H] na seção 3 (conforme caveats do próprio dossiê, linhas 243–249).

| ID | Afirmação | Fonte citada (no dossiê) | Data ref. |
|---|---|---|---|
| **FATO-MKT-01** | Potência MMGD total instalada: **43,5–45 GW** | ANEEL/ABGD · EPE 2025 | dez/2025 |
| **FATO-MKT-02** | GD compartilhada: **~2,74 GW** e **~1,55 milhão de UCs** beneficiadas | Canal Solar c/ EPE/ANEEL | 2025 |
| **FATO-MKT-03** | **~2.224 sistemas** de GD compartilhada em operação; **+296 MW** adicionados jan–set/2025 (vs +545 MW no ano 2024); **~116 mil UCs novas** no período (≈52 UCs/sistema) | pv magazine c/ ANEEL | jan–set/2025 |
| **FATO-MKT-04** | **99,3%** da capacidade MMGD total é solar fotovoltaica | ANEEL | jun/2025 |
| **FATO-MKT-05** | Em abr/2024 a modalidade compartilhada tinha 9.294 sistemas, 875 MW, 330 mil UCs (<1% dos sistemas, 8% das UCs) — biênio 24–25 triplicou potência e quadruplicou UCs | ANEEL (resposta ao TCU) | abr/2024 |
| **FATO-MKT-06** | Modalidades SCEE: autoconsumo remoto ~2,76 mi UCs / ~11,37 GW; junto à carga ~4,8 GW adicionados em 2025 | ANEEL / Canal Solar | 2025 |
| **FATO-MKT-07** | Distribuição regional MMGD (≈41,5 GW recorte): Sudeste 13,5 · Nordeste 8,9 (ultrapassou o Sul) · Sul 8,7 · Centro-Oeste 7,0 · Norte 3,1 GW | Electra Energy c/ ANEEL | jun/2025 |
| **FATO-MKT-08** | **ACL: ~85,4 mil UCs**; **42% do consumo nacional (≈30,2 GW médios)** | CCEE (dez/2025) · EstudoCCEE (mar/2026) | dez/2025–mar/2026 |
| **FATO-MKT-09** | **~506 comercializadoras** na CCEE; **503 comercializadores atacadistas** (+1,4% em 12m) | CCEE 2024 · ePowerBay c/ CCEE mar/2026 | 2024 / mar/2026 |
| **FATO-MKT-10** | **129 varejistas habilitadas** (+23 em processo); **11 varejistas com >1.000 UCs**; 38.635 UCs com perfil varejista (+7.630 em 12m) | CCEE · ePowerBay · Thunders c/ CCEE | mar/2026 |
| **FATO-MKT-11** | ~16 mil agentes totais na CCEE (dos quais ~13,1 mil consumidores); base cresceu de ~10,9 mil (2021) → ~16 mil | CCEE | out/2024 |
| **FATO-MKT-12** | Cargas <500 kW só migram sob representação varejista | Portaria MME 50/2022 | — |
| **FATO-MKT-13** | Figura formal do **agregador de RED ainda NÃO criada** (jun/2026); prevista para o 3º/último ciclo da CP 39/2023 | ANEEL/gov.br (CP 39/2023) | jun/2026 |
| **FATO-MKT-14** | Programa estrutural de **Resposta da Demanda** operado por ONS+CCEE desde set/2022; **Sandbox RD Produto Disponibilidade** (lotes mín. 5 MW) | REN ANEEL 1.040/2022 · REN Autorizativa 12.600/2022 | set/2022 |
| **FATO-MKT-15** | **21.707 novas migrações ACL em 2025** (vs 26.834 em 2024); **13.519 agentes consumidores**; universo Grupo A ~202 mil UCs (headroom ~117 mil) | EstudoCCEE · Thunders c/ CCEE | 2025 / fev/2025 |
| **FATO-MKT-16** | Migrações ACL 2025 por ramo: Serviços 6.648 · Comércio 4.098 · Manufaturados 1.940 · Saneamento 904 · Alimentícios 665 · CPF 370 | EstudoCCEE / Agência iNFRA | 2025 |
| **FATO-MKT-17** | **Lei nº 15.269/2025 publicada em 24/11/2025** (conversão da MP 1.304/2025 que absorveu a MP 1.300/2025, 20 vetos) — maior reforma do setor desde 2004; cria cronograma legal de abertura do ACL ao Grupo B | Lei 15.269/2025 | 24/11/2025 |
| **FATO-MKT-18** | Cronograma: Grupo A completo jan/2024; **indústria/comércio BT em nov/2027 (24 meses, varejista obrigatório)**; **residencial/abertura total nov/2028 (36 meses)** com criação do **SUI**; fim do critério de tensão no rateio da CDE em 2038 | Lei 15.269/2025 | 24/11/2025 |
| **FATO-MKT-19** | Universo Grupo B (TAM): Residencial B1 **82,9 mi** · Comercial B3 **6,0–6,1 mi** · Rural B2 **3,9–4,5 mi** · Industrial BT **410,7 mil** → **total ~89–92 mi UCs** | EPE Anuário 2025 (UCs dez/2024) | dez/2024 |
| **FATO-MKT-20** | Economia potencial abertura BT: **R$ 35,8 bi/ano**, economia média ~19% (preços 2022); estudo anterior estimava até R$ 25 bi/ano e R$ 210 bi acum. até 2035 | ABRACEEL, estudo "Portabilidade da Conta de Luz…" | — |
| **FATO-MKT-21** | Consumo Brasil 2024: **532 TWh** (+4,4%); residencial ~184 TWh (+8%); comercial ~112 TWh (+7,4%); >10 GW médios de contratos ACR vencendo até 2028 | EPE BEN 2025 / Anuário 2025 · ABRACEEL | 2024 |
| **FATO-MKT-22** | Perfil GD compartilhada por classe: Residencial B1 **73,6%** · Comércio B3 16,6% · Rural B2 7,0% · Indústria 2,4% | ABSOLAR | — |
| **FATO-MKT-23** | **BESS — marco legal:** Lei 15.269/2025 reconhece armazenamento como **atividade autônoma**; REIDI ampliado; **Imposto de Importação zerado até 2030** | Lei 15.269/2025 | nov/2025 |
| **FATO-MKT-24** | **BESS — regulamentação ANEEL aprovada em 02/jun/2026** (encerra 2ª fase da CP 39/2023, 652 sugestões/70 participantes); SAE autônomo despachado pelo ONS, MUSTc de consumo = zero; ONS publicará mapas anuais de pontos de conexão; **LRCAP 2026** incluirá baterias pela 1ª vez | ANEEL (CP 39/2023) | 02/jun/2026 |
| **FATO-MKT-25** | Mobilidade elétrica: **21.061 pontos públicos/semipúblicos** (+42% a/a; era 14.827); recarga rápida DC +167% (2.430→6.479, 31% do total); 411.869 VE plug-in; 19,6 VE/eletroposto; 1.649 municípios | ABVE + Tupi Mobilidade | fev/2026 |
| **FATO-MKT-26** | Recarga regulada no Cap. V da REN 1.000/2021 (preços livres); **CP 42/2025** (contribuições 11/dez/2025–10/mar/2026) aprimora conexão de carregadores | ANEEL (REN 1.000/2021 · CP 42/2025) | 2025–2026 |
| **FATO-MKT-27** | ~7 milhões de UCs beneficiadas pela MMGD total; 21 milhões de pessoas beneficiadas por MMGD | ANEEL/ABGD | — |
| **FATO-MKT-28** | Desde jul/2025, migração via API faz parte das UCs varejistas não aparecer nas bases públicas da CCEE — números reais maiores que os divulgados | CCEE (nota de dados) | jul/2025 |

> **Nota sobre Fio B e tarifa branca/bandeiras:** o dossiê-fonte (01-mercado) **cita** REN 1.000/1.059 e a rampa do Fio B apenas no encadeamento regulatório (linha 31), **sem detalhar** os percentuais anuais nem os postos da tarifa branca. Esse detalhamento (rampa Fio B 15%→90%, GD I/GD II, validade 60 meses Art. 655-L, tarifa branca 3 postos, bandeiras verde/amarela/vermelha) está no doc de reconciliação `02-contexto-regulatorio-mercado-br.md`, **não** no dossiê deste bloco. Preservo a distinção para não atribuir fonte errada. Ver seção 5.

---

## 3. Estimativas [E] / Hipóteses [H]

Reclassificadas a partir dos caveats explícitos do dossiê (linhas 243–247: "players auto-reportados… não auditados"; "projeções vs. realizado"; "dimensionamento do agregador é prospectivo").

- **[E] Gestoras de GD compartilhada (auto-reportado, não auditado):**
  - Órigo Energia (líder): **580 MWp / 91 mil UCs**, nacional (13 estados+DF), captação R$ 500 mi (Santander), receita R$ 416,5 mi.
  - Cemig SIM: **330 MWp / ~40.000 UCs** (MG, +60 municípios).
  - Lemon Energia: >10.000 clientes (gere usinas de terceiros; foco PMEs); Sun Mobi 22,5 MW; Bulbe >50 mil famílias; Nex >5.000 clientes; Matrix 16,28 MWp / ~2.900 (estimativa).
  - Telecoms (Claro pioneira jul/2022, Vivo/SouVagalume, Oi, TIM) usam assinatura solar como cross-sell.
- **[H] Metas/projeções de players (não realizadas):** Órigo meta 2 GWp até 2027; Cemig SIM meta 1 GWp até 2029.
- **[E] Mercado "pulverizado" de "dezenas de empresas"** de gestoras de GD compartilhada — faixa qualitativa, sem número oficial (fontes InfoMoney/Reuters, O Tempo, Greener).
- **[E] Ticket/economia GD compartilhada:** Órigo exige consumo >R$ 300/mês; economia típica **10%–25%** (Lemon/Órigo/Sun Mobi).
- **[E] SAM/TAM consolidado (dimensionamento do dossiê):** ACL Grupo B comercial/industrial ≈ **6,5 mi UCs / R$ 7,9 bi/ano** (SAM prioritário, abre nov/2027); Grupo B residencial/rural ≈ **87 mi UCs / R$ 25,5 bi/ano** (TAM máximo).
- **[H] Camada agregador/VPP inteira é prospectiva** — figura não existe até jun/2026; todo dimensionamento é hipótese dependente de regulação (3º ciclo CP 39/2023).
- **[E] "Ago/2026" para antecipação BT comercial** consta do texto original da MP, **não vinculante**; o prazo legal vinculante é **nov/2027**.

---

## 4. Implicações para o v1 do integrador/EPC

**Regra de corte (README-CLAUDE-CODE, escopo v1):** o v1 constrói o **portal do integrador/EPC** sobre smart-meter existente (ingestão → time-series → modelo de ativo → monitoramento + frota + comissionamento + diagnóstico remoto). **VPP, CCEE, mercado livre, otimização e os 18 cenários são explicitamente fora do v1.** Portanto, **quase todo o dossiê 01-mercado é contexto de mercado/fases futuras, não requisito de produto do v1.**

**O que do bloco importa para o v1 (contexto que molda o produto do integrador):**
- **GD compartilhada é o mercado mais maduro hoje** (~1,55 mi UCs, ~2.224 sistemas, ~52 UCs/sistema) e 99,3% solar FV — é a realidade operacional dos clientes do integrador/EPC. O portal precisa lidar com **frota de sistemas FV multi-UC** e **comissionamento** de usinas de assinatura solar. Isso é aterrado no v1 (frota + comissionamento), independente de CCEE/VPP.
- **Concentração e escala das gestoras** (Órigo, Cemig SIM, dezenas de players pulverizados) definem o **perfil de cliente-alvo do integrador**: quem instala/opera essas fazendas solares é o comprador do portal. Contexto de go-to-market, não requisito técnico.
- **Perfil B1 residencial (73,6%) + B3 comercial** indica volume de pequenas UCs pulverizadas — reforça a necessidade da **camada de abstração de device (S2.3)** e ingestão escalável desde a 1ª linha.

**O que é contexto de fases futuras (NÃO v1):**
- Toda a análise ACL / Lei 15.269 / abertura BT nov/2027–2028 / SUI / varejista obrigatório → **Fase 2 (mercado livre)**, explicitamente fora do v1.
- BESS revenue-stacking, agregador de RED, VPP, RD, LRCAP 2026, recarga VE → **fases posteriores** (agent-fabric/otimização/VPP fora do v1).
- Dimensionamento TAM/SAM (R$ 35,8 bi/ano etc.) → material de investidor/estratégia, não requisito de build.

**Leitura líquida:** este bloco é **dossiê de tese de mercado** que justifica o roadmap além do beachhead. Para o v1 ele contribui **contexto** (maturidade da GD compartilhada, perfil de cliente, gatilhos regulatórios futuros) mas **nenhum requisito funcional novo** além do que já está no escopo integrador (frota + comissionamento de FV/GD).

---

## 5. Reconciliação com `docs/smart/02-contexto-regulatorio-mercado-br.md`

Os dois docs são **complementares, não redundantes**: o `02-contexto` é o mapa **regulatório-técnico** (tarifas, Fio B, normas, medição — o que define requisitos do produto); o dossiê 01-mercado é o **dimensionamento quantitativo** (números de mercado, players, TAM). Onde se sobrepõem, são majoritariamente **consistentes**.

### ✅ Confirma
- **Lei 15.269/2025 (24/11/2025)** e cronograma de abertura BT: `02-contexto` §4 diz "até nov/2027 comercial/industrial, até nov/2028 residencial, cria o SUI" — **idêntico** ao FATO-MKT-18. Confirmado.
- **Três arranjos comerciais** (cativo / GD compartilhada Lei 14.300 / ACL): a estrutura de `02-contexto` §2 casa com a cadeia de valor do dossiê (seção "Cadeias de valor").
- **Encadeamento regulatório GD** (REN 482→687→Lei 14.300→REN 1.000/1.059) aparece nos dois (FATO-MKT §1 vs `02-contexto` §3).
- **Modalidades SCEE** (autoconsumo local/remoto, geração compartilhada, EMUC): consistentes entre `02-contexto` §3 e FATO-MKT-06.
- **Sinal de preço no cativo = tarifa branca + bandeiras**; tarifação horária plena só no livre — coerente com a menção do dossiê a "precificação horária para a BT" (linha 210) e detalhado em `02-contexto` §5.
- **Agregador de RED ainda não regulado / 3º ciclo CP 39/2023** e **RD via ONS+CCEE (REN 1.040/2022)**: `02-contexto` §6 fala em "agenda regulatória de observabilidade/RED"; o dossiê é mais específico (FATO-MKT-13, 14). Confirma e detalha.

### 🔼 Atualiza / supera (dossiê traz dado que `02-contexto` não tem ou tem menos preciso)
- **BESS — regulamentação ANEEL:** `02-contexto` §7 diz apenas "regulação específica em construção… `[VERIFICAR]`". O dossiê **supera**: FATO-MKT-24 fixa **aprovação em 02/jun/2026** (encerramento da 2ª fase da CP 39/2023, SAE autônomo, MUSTc=0, LRCAP 2026). → `02-contexto` deveria remover o `[VERIFICAR]` de BESS e datar 02/jun/2026.
- **BESS — marco legal:** FATO-MKT-23 (atividade autônoma, II zerado até 2030, REIDI) não consta de `02-contexto`. Atualização a incorporar.
- **Números de mercado** (~85,4 mil UCs ACL, ~1,55 mi GD compartilhada, 42% do consumo, 506 comercializadoras, TAM ~89–92 mi UCs / R$ 35,8 bi): `02-contexto` é qualitativo e **não traz nenhum desses números** — o dossiê **preenche** a camada quantitativa que falta no `02-contexto`.
- **Serviços ancilares / controle de tensão** (out/2025, TSA 2026 ≈ R$ 10,41/Mvar-h) e **CP 001/2026 medição inteligente** aparecem em `02-contexto` §6 mas **não** no dossiê — aqui `02-contexto` é que supera o dossiê. (Complementaridade, não conflito.)

### ⚠️ Conflitos / divergências numéricas
- **Rampa do Fio B e validade de créditos:** `02-contexto` §3 detalha a rampa (15%/2023 → 90%/2028, com **revisão** — não 100% automático — em 2029), GD I/GD II, isenção adquirida até 2045, e **validade de créditos 60 meses (REN 1.059/2023, Art. 655-L)**. O **dossiê 01-mercado NÃO cita** esses percentuais nem o Art. 655-L — apenas nomeia a rampa como contexto. **Não é conflito**, é ausência: o número autoritativo de Fio B/60 meses **vem do `02-contexto`, não deste bloco**. (Alerta para não citar o dossiê como fonte da rampa do Fio B.)
- **Divergência de datas — sanção da Lei 15.269:** o próprio dossiê registra caveat de "24 vs 25/nov/2025" (publicação oficial 24/11/2025). `02-contexto` usa **24/11/2025** — **alinhado**. Sem conflito material.
- **Comercializadoras 506 vs 503:** divergência **interna ao dossiê** (506 = CCEE 2024; 503 atacadistas = mar/2026, bases metodológicas distintas), não com `02-contexto`. Registrada no próprio caveat (linha 248).
- **Antecipação BT "ago/2026":** o dossiê marca como texto original da MP, **não vinculante**; `02-contexto` corretamente usa nov/2027 como marco. Sem conflito — ambos convergem para nov/2027 vinculante.

**Conclusão da reconciliação:** nenhum **conflito material** de fato/número entre os dois docs. O dossiê 01-mercado **complementa** o `02-contexto` adicionando (a) a **camada quantitativa de mercado** (UCs, GW, TAM, players) e (b) a **atualização do status do BESS** (regulamentação ANEEL 02/jun/2026 — supera o `[VERIFICAR]` do `02-contexto`). Em sentido inverso, o `02-contexto` mantém o **detalhe regulatório-técnico** (Fio B, tarifa branca, normas INMETRO/ANATEL/PRODIST, medição) que o dossiê não cobre e que é o que **de fato aterra requisitos do produto**.
