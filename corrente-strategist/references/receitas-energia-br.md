# Taxonomia de Receitas — Setor Elétrico BR (CORRENTE)

> Arquivo de referência da skill `corrente-strategist`. **Sincronizado com** `arquitetura-receitas-corrente.html` (CORRENTE-REV-01, r0, jun/2026). Quando o artefato for revisado, atualizar este arquivo junto — divergência aqui produz erro silencioso na análise.
>
> Regra de uso: antes de modelar pricing, unit economics ou P&L, ler este mapa. Nunca inventar forma de receita sem checar se já está aqui. Toda âncora carrega rótulo [F]/[E]/[H]/[INPUT].

## Legenda de camada
- **TechCo** — software, atividade não regulada; serve os 6 personas; é o ativo venture-fundable.
- **Regulada** — transaciona energia; exige entidade própria, garantias CCEE, risco de balanço (gate D2).
- **Futura** — depende de regra que não existe até jun/2026; tratar como opcionalidade com valor presente ~zero no caso-base.

## As 11 formas

| # | Forma | Camada | Âncora real (nomeada) | Tradução BR | Status / capital p/ ligar |
|---|---|---|---|---|---|
| R-01 | SaaS de operação do integrador/EPC | TechCo | SolarZ, Sunne, GDASH, SolarMaker, Solar Next existem [F]; nenhum publica preço | R$ 1–5/usina/mês (monitoramento) a R$ 200–1.500/mês por integrador (suíte) [E] [INPUT] | Operável hoje · capital BAIXO · **cunha do beachhead D1** |
| R-02 | Licenciamento do OS por UC (modelo Kraken) | TechCo | Kraken: US$ 500M ARR / 70M contas ≈ **US$ 7,1/conta/ano** [F]; licença-base £2–4/conta/ano [E, fonte secundária] | R$ 8–35/UC/ano com deflator de disposição a pagar 50–70% [E] | Operável · capital MÉDIO · ciclo 9–18m · poucos logos (129 varejistas, ~48 ativas [F]) |
| R-03 | Success fee de migração ACL | TechCo | Economia média BT ~19% da fatura, ABRACEEL preços 2022 [F]; prática Grupo A 20–50% da economia ano 1 [E] | Conta B3 R$ 2.000/mês → fee R$ 900–2.300 one-off [E] | Gatilho nov/2027 (BT) · capital BAIXO · **one-off: financia CAC, não é PMF** |
| R-04 | Take-rate de gestão contínua BT | TechCo→Comerc. | Gestão Grupo A R$ 500–2.500/UC/mês [E] | BT viável só a R$ 3–15/UC/mês [H] — exige custo de servir ~zero (tese AI-native) | Gatilho nov/2027 · capital MÉDIO · recorrente que o R-03 origina |
| R-05 | Spread de comercialização de energia | Regulada | Gerador líquido GD R$ 80–140/MWh já desc. gestão/inadimplência/churn [F]; 503 atacadistas competindo [F] | margem comprimida; múltiplo baixo | Operável mas capital ALTO (garantias + balanço) · **gate D2** |
| R-06 | Software de orquestração de GD compartilhada | TechCo | Desconto real médio 14–15% (faixa 7–30%) [F]; Órigo R$ 416,5M / 91k UCs [E] | pricing do software R$ 2–6/UC/mês [H] | Operável hoje · capital BAIXO · ataca a dor nº1 do segmento (fidelização [F]) |
| R-07 | Rev-share de canal / white-label | TechCo | 1KOMMA5° €520M, lucrativa, install-led [F]; Fintech Solfácil (originação crédito solar) não-exclusiva [INPUT] | take de originação 1–4% do financiado [E] | Operável hoje · capital BAIXO–MÉDIO · alavanca ativo proprietário |
| R-08 | Flexibilidade / VPP empilhada | Futura | Next Kraftwerke >10 GW na Europa [F]; figura do agregador de RED inexistente BR até jun/2026 (3º ciclo CP 39/2023) [F]; merchant não fecha (~R$4.500/MWh vs ~R$600/MW) [F] | empilhamento arbitragem+capacidade+ancilares é a única via [F] | **BLOQUEADA por regulação** · opcionalidade, VP ~0 no caso-base |
| R-09 | Dados / API / inteligência | TechCo | comparáveis fracos no BR [H]; 1º cliente plausível Fintech Solfácil (score de ativo solar) [INPUT] | pricing especulativo [H] | Tardia por desenho · consequência do moat de dado (D2), não motor inicial |
| R-10 | Marketplace transacional | TechCo | 1KOMMA5° [F]; Distribuidora Solfácil não-exclusiva [INPUT] | take B2B 1–4% do GMV [E] | Operável · capital MÉDIO · margem fina, exige volume |
| R-11 | P2P energy trading | Futura/Sandbox | SCEE **compensa** créditos, não vende energia (REN 482/1.000) [F]; Powerledger/LO3/Piclo pivotaram de P2P-consumidor p/ flexibilidade [E] | sem base legal fora de sandbox; WTP por P2P puro fraca [E] | **Sandbox / Trilha 2** · papel: feature de marca sobre VPP + opcionalidade regulatória · LTV especulativo [H] |

## Hipótese R1 (stack proposto — refutável pelo unit economics)
- **Onda 1 (agora→12m):** R-01 SaaS integrador (cunha) + R-03 success fee (caixa) + R-07 rev-share Solfácil.
- **Onda 2 (12–24m):** R-06 software de gestora + abertura de R-02 (licença OS), software multi-tenant desde o início.
- **Onda 3 (gatilhos):** R-04 take-rate BT em nov/2027; R-05 Comercializadora só pós-G2/G3 (gate).
- **Opcionalidade permanente:** R-08, R-09, R-11 — valor zero no caso-base, presença ativa na Trilha 2 regulatória.
- Racional: maximiza receita recorrente por real investido; cada onda financia e gera o dado da seguinte; usa ativos proprietários declarados. Caso-base é bootstrap; capital externo é acelerador, não premissa de sobrevivência.

## Bear case — kill signals (o que monitorar)
1. **Limiar BT não fecha** → custo de servir > R$ 5/UC/mês no piloto G2 (mata metade do TAM).
2. **Deflator Kraken pior** → 3 conversas de pricing com varejistas abaixo de R$ 8/UC/ano.
3. **Incumbentes no mesmo beachhead** (Thunders, Clarke, Way2) → win-rate < 20% em bake-off. *Maior lacuna de inteligência atual.*
4. **Success fee mascara PMF** → conversão fee→recorrente < 60% após 6 meses (vira consultoria, não plataforma).
5. **Flexibilidade atrasa 3+ anos** → nenhuma AIR do agregador até dez/2027 (não deixar a narrativa depender de VPP).
6. **Churn estrutural** → churn de consumidor > 3%/mês sustentado (corta os LTVs pela metade).

## Insight estrutural a preservar
O **integrador/EPC** é a única persona com 3 formas primárias operáveis hoje (R-01, R-07, R-10) e funciona como **máquina de CAC subsidiado** das camadas seguintes — o LTV do consumidor BT individual (R$ 165–790 [E]) não suporta venda direta paga. Essa é a coerência econômica do bowling-pin (D1).
