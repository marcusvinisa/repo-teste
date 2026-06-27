# 02 — Contexto Regulatório e de Mercado (Brasil)

> Mapa do ambiente regulatório e comercial de energia elétrica em **baixa tensão (BT, Grupo B)** no Brasil, que define os requisitos e os limites do Smart. Aterra a [matriz de cenários](11-matriz-de-cenarios.md) (cativo, GD compartilhada, mercado livre) e o catálogo de [modos de operação](10-modos-de-operacao-e-features.md). Itens sensíveis ao tempo estão marcados `[VERIFICAR]` (regulação em evolução).

---

## 1. Atores institucionais

| Sigla | Papel |
|---|---|
| **ANEEL** | Agência reguladora — define regras de GD, tarifas, qualidade, PRODIST |
| **ONS** | Operador Nacional do Sistema — opera a rede e contrata **serviços ancilares** |
| **CCEE** | Câmara de Comercialização — contabiliza e liquida o mercado (ACR e ACL) |
| **MME / CNPE** | Política energética (abertura de mercado, diretrizes) |
| **Distribuidora (DisCo)** | Conexão da UC, medição, faturamento no mercado cativo |
| **Comercializador (varejista/atacadista)** | Vende energia no mercado livre, inclusive a pequenos consumidores |

---

## 2. Os três arranjos comerciais (eixo das colunas da matriz de cenários)

| Arranjo | O que é | Quem fatura a energia | Implicação para o Smart |
|---|---|---|---|
| **A — Cativo** | Mercado regulado: a UC compra da distribuidora local pela tarifa regulada | Distribuidora | Otimização contra **tarifa regulada** (convencional/branca/bandeiras); foco em autoconsumo e load shifting |
| **B — GD compartilhada** | Geração distribuída cujos créditos são repartidos entre várias UCs (Lei 14.300) | Distribuidora (com **SCEE** aplicando créditos) | Gestão de **rateio**, conciliação geração×consumo das UCs, otimização de uso de créditos → ver [Smart GD](08-plataforma-cloud-e-apis.md) |
| **C — Mercado livre (ACL)** | A UC contrata energia de um comercializador, fora da tarifa regulada | Comercializador + DisCo (uso do fio) | Otimização contra **preço de contrato/PLD**, medição para liquidação, migração |

> A combinação **arranjo × nível de ativos** gera a grade de cenários — ver [11](11-matriz-de-cenarios.md).

---

## 3. Geração Distribuída (GD) — Lei 14.300/2022 e REN ANEEL 1.000/2021

A **Lei 14.300/2022** instituiu o *Marco Legal da Microgeração e Minigeração Distribuída*; a regulação operacional está consolidada na **REN ANEEL nº 1.000/2021** (que substituiu as REN 482/2012 e 414/2010) e atualizações como a **REN 1.059/2023** `[VERIFICAR versão vigente]`.

### Portes
- **Microgeração:** potência instalada **≤ 75 kW**.
- **Minigeração:** **> 75 kW** até **3 MW** (fontes despacháveis/limites específicos podem variar) `[VERIFICAR]`.

### Modalidades de compensação (SCEE — Sistema de Compensação de Energia Elétrica)
| Modalidade | Descrição | Relevância p/ Smart |
|---|---|---|
| **Autoconsumo local** | Geração na própria UC | Cenários N1+ "atrás do medidor" |
| **Autoconsumo remoto** | Geração em UC distinta, mesma titularidade, mesma área de concessão | Multi-site do mesmo dono |
| **Geração compartilhada** | Consórcio/cooperativa de consumidores rateia créditos | **Núcleo do "arranjo B"** — rateio entre UCs |
| **EMUC** | Empreendimento com múltiplas UCs (ex.: condomínios) | Gestão coletiva por condomínio |

### SCEE, créditos e "Fio B"
- Energia injetada gera **créditos** (kWh) usados para abater o consumo, com validade (tipicamente 60 meses).
- A **Lei 14.300** encerrou a gratuidade integral do uso da rede: passou a haver **cobrança gradual do TUSD Fio B** sobre a energia compensada para novos conectados, em rampa anual crescente até **100% (≈2029)** `[VERIFICAR percentuais e datas]`. Sistemas com solicitação de acesso protocolada antes do corte (≈ jan/2023) têm **direito adquirido** (regra antiga) até **2045** `[VERIFICAR]`.

**Impacto no produto:** o motor de economia precisa modelar (a) crédito de energia por UC, (b) custo de Fio B incidente, (c) validade/rateio de créditos e (d) o trade-off injetar-agora vs autoconsumir/armazenar. Ver [04 — modelo de tarifa/crédito](04-modelo-de-dominio-e-dados.md) e [10 — modos](10-modos-de-operacao-e-features.md).

---

## 4. Mercado livre (ACL) e abertura da baixa tensão

- O mercado brasileiro divide-se em **ACR** (Ambiente de Contratação Regulada, tarifa da distribuidora) e **ACL** (Ambiente de Contratação Livre).
- Desde **jan/2024**, **todo consumidor do Grupo A** (alta/média tensão) pode migrar ao ACL, podendo ser atendido por **comercializador varejista**.
- A **abertura para o Grupo B (baixa tensão / residencial)** está em discussão regulatória (MME/CCEE), com cronograma ainda **não consolidado** — estimativas apontam janelas a partir de **2026–2028** `[VERIFICAR cronograma oficial]`.

**Impacto no produto:** o "arranjo C" deve ser desenhado para entrar em produção **quando a BT abrir**, exigindo: medição compatível para liquidação na CCEE, modelagem de **contrato/PLD** em vez de tarifa regulada, e fluxos de **migração**. Tratar como **roadmap Fase 2** ([12](12-roadmap-e-faseamento.md)) e marcar dependência regulatória em [13](13-gaps-riscos-e-decisoes.md).

---

## 5. Estrutura tarifária da baixa tensão (Grupo B)

| Componente | Descrição | Uso no Smart |
|---|---|---|
| **TUSD** | Tarifa de Uso do Sistema de Distribuição (fio) | Compõe custo; base do Fio B na GD |
| **TE** | Tarifa de Energia | Compõe custo da energia consumida |
| **Tarifa convencional** | Monômia, preço único de energia (R$/kWh) | Baseline de economia |
| **Tarifa Branca** | **ToU** opcional do Grupo B com 3 postos: **ponta**, **intermediário**, **fora-ponta** | Habilita **load shifting** e carga inteligente |
| **Bandeiras tarifárias** | Adicional **verde/amarela/vermelha 1 e 2** conforme custo de geração | Sinal de preço de curto prazo para otimização |

> No mercado cativo, **não há tarifa dinâmica horária de mercado** como na Europa; o sinal de preço disponível é **tarifa branca + bandeiras**. A "tarifa dinâmica" plena só aparece no **mercado livre** (preço de contrato/PLD). O motor de otimização deve suportar **ambos os mundos** — ver [08](08-plataforma-cloud-e-apis.md) e [10](10-modos-de-operacao-e-features.md).

---

## 6. Serviços de rede / *grid services* no Brasil (nível N5)

Diferente da Europa (FCR/aFRR com mercados abertos a agregadores residenciais), no Brasil:

- **Serviços ancilares** são contratados pelo **ONS** (controle de frequência, reserva de potência operativa, suporte de reativos, restabelecimento) — historicamente de **grandes geradores**, não de DERs residenciais.
- **Resposta da demanda (demand response):** houve **projetos-piloto e chamadas** ANEEL/ONS, mas **ainda não há um mercado consolidado e remunerado para flexibilidade residencial em BT** `[VERIFICAR status atual]`.
- **Agregação / VPP de DERs em BT:** **incipiente**; remuneração de flexibilidade do consumidor de baixa tensão é majoritariamente **futuro/regulatório**.

**Impacto no produto:** o nível **N5 (grid services)** deve ser construído como **capacidade técnica pronta** (medição, telemetria, despacho, agregação — ver [08](08-plataforma-cloud-e-apis.md)) porém com **monetização condicionada à evolução regulatória**. No curto prazo, o "grid service" viável é mais **local/contratual** (ex.: limitação de injeção/curtailment por ordem da distribuidora, controle de reativo, gestão de demanda contratada) — análogo funcional ao **§14a alemão** citado pelas fontes, mas adaptado ao Brasil. Detalhe em [10](10-modos-de-operacao-e-features.md) e [11](11-matriz-de-cenarios.md).

---

## 7. Normas técnicas e certificação (requisitos do hardware e da conexão)

### Conexão de GD à rede (PRODIST)
- **PRODIST Módulo 3** — procedimentos de **acesso e conexão** de micro/minigeração à distribuição (solicitação de acesso, parecer, requisitos de proteção, medição).

### Inversores e sistema FV (ABNT)
| Norma | Escopo |
|---|---|
| **ABNT NBR 16149** | Características da interface de conexão de inversores FV à rede |
| **ABNT NBR 16150** | Procedimentos de ensaio de conformidade da interface |
| **ABNT NBR 16274** | Sistemas FV conectados à rede — documentação, comissionamento e inspeção |
| **ABNT NBR IEC 62116** | Ensaio de **anti-ilhamento** (prevenção de ilhamento) |
| **ABNT NBR 16690** | Instalações elétricas de arranjos FV |

### Certificação compulsória e homologação
- **INMETRO** — etiquetagem/certificação compulsória de **inversores e módulos** (Programa Brasileiro de Etiquetagem) `[VERIFICAR portaria vigente]`.
- **ANATEL** — **homologação obrigatória** de qualquer produto com radiofrequência (Wi-Fi, Bluetooth, celular 4G/LTE) — aplica-se ao **hardware Smart** (ver [06](06-especificacao-hardware.md)).
- **Segurança elétrica** — conformidade com ABNT/NBR aplicáveis ao equipamento eletroeletrônico e instalação (ex.: NBR 5410 para instalações de BT) `[VERIFICAR]`.

### Carregadores de VE e armazenamento
- **ABNT NBR IEC 61851** (sistema de carga condutiva de VE; modos de carga) e **NBR IEC 62196** (conectores/plugues).
- **Armazenamento (baterias/ESS):** regulação específica em **construção** no Brasil; aplicar normas IEC/ABNT de segurança de baterias e seguir consultas/REN da ANEEL `[VERIFICAR]`.

### Medição
- GD exige **medidor bidirecional** (registra energia consumida e injetada). Para mercado livre, medição apta à **liquidação na CCEE** (SMF) `[VERIFICAR requisitos por porte]`.

---

## 8. Síntese de implicações para o Smart

1. **Dois mundos de preço:** cativo = tarifa regulada (convencional/branca/bandeiras); livre = contrato/PLD. O motor de otimização precisa de **ambos** ([08](08-plataforma-cloud-e-apis.md)).
2. **GD compartilhada = rateio + créditos + Fio B:** requer um subsistema de **billing/conciliação multi-UC** ([08](08-plataforma-cloud-e-apis.md)).
3. **Grid services = capacidade técnica pronta, monetização gradual:** construir N5 sem depender de mercado que ainda não existe em BT ([11](11-matriz-de-cenarios.md)).
4. **Hardware deve nascer certificável no Brasil:** INMETRO + ANATEL + ABNT desde o design ([06](06-especificacao-hardware.md)).
5. **Conexão segue PRODIST/ABNT:** o produto deve **respeitar** (não burlar) as proteções do inversor (anti-ilhamento) e limites de injeção ([07](07-especificacao-firmware-edge.md)).

> Lacunas e dependências regulatórias críticas estão consolidadas em [13 — Gaps, Riscos e Decisões](13-gaps-riscos-e-decisoes.md).
