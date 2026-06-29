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
- Energia injetada gera **créditos** (kWh) usados para abater o consumo, com **validade de 60 meses** (REN 1.059/2023, Art. 655-L).
- A **Lei 14.300** encerrou a gratuidade integral do uso da rede. Para quem se conectou **a partir de 7/jan/2023 (GD II)**, há **cobrança gradual do TUSD Fio B** sobre a **energia injetada/compensada**, em rampa anual: **15% (2023) · 30% (2024) · 45% (2025) · 60% (2026) · 75% (2027) · 90% (2028)**; a partir de **2029** a ANEEL **revisa a metodologia** (diretrizes do CNPE) — **não** é automaticamente 100%. Quem protocolou acesso **até 6/jan/2023 (GD I)** mantém **direito adquirido** (isenção do Fio B) **até 2045**. O **autoconsumo instantâneo** (gerar e consumir no mesmo instante) **não** é tarifado pelo Fio B — só a energia **injetada**.

**Impacto no produto:** o motor de economia precisa modelar (a) crédito de energia por UC, (b) custo de Fio B incidente, (c) validade/rateio de créditos e (d) o trade-off injetar-agora vs autoconsumir/armazenar. Ver [04 — modelo de tarifa/crédito](04-modelo-de-dominio-e-dados.md) e [10 — modos](10-modos-de-operacao-e-features.md).

---

## 4. Mercado livre (ACL) e abertura da baixa tensão

- O mercado brasileiro divide-se em **ACR** (Ambiente de Contratação Regulada, tarifa da distribuidora) e **ACL** (Ambiente de Contratação Livre).
- Desde **jan/2024**, **todo consumidor do Grupo A** (alta/média tensão) pode migrar ao ACL, podendo ser atendido por **comercializador varejista**.
- **Abertura da baixa tensão — agora com marco legal:** a **Lei nº 15.269/2025 (24/11/2025)** iniciou a abertura do mercado livre para a BT. Cronograma anunciado: até **nov/2027** para consumidores **comerciais e industriais** de BT, e até **nov/2028** para **residenciais**. A lei cria o **Supridor de Última Instância (SUI)** para garantir fornecimento em situações excepcionais. A ANEEL conduz o **aprimoramento regulatório** (medição, contratação) com horizonte **2027**. `[VERIFICAR regulamentação infralegal em construção]`

**Impacto no produto:** o "arranjo C" deve ser desenhado para entrar em produção **quando a BT abrir**, exigindo: medição compatível para liquidação na CCEE, modelagem de **contrato/PLD** em vez de tarifa regulada, e fluxos de **migração**. Tratar como **roadmap Fase 2** ([12](12-roadmap-e-faseamento.md)) e marcar dependência regulatória em [13](13-gaps-riscos-e-decisoes.md).

---

## 5. Estrutura tarifária da baixa tensão (Grupo B)

| Componente | Descrição | Uso no Smart |
|---|---|---|
| **TUSD** | Tarifa de Uso do Sistema de Distribuição (fio) | Compõe custo; base do Fio B na GD |
| **TE** | Tarifa de Energia | Compõe custo da energia consumida |
| **Tarifa convencional** | Monômia, preço único de energia (R$/kWh) | Baseline de economia |
| **Tarifa Branca** | **ToU** opcional do Grupo B, 3 postos: **ponta** (~18–21h, varia por distribuidora), **intermediário** (1h antes e 1h depois da ponta) e **fora-ponta** | Habilita **load shifting** e carga inteligente |
| **Bandeiras tarifárias** | Adicional **verde/amarela/vermelha 1 e 2** conforme custo de geração | Sinal de preço de curto prazo para otimização |

> No mercado cativo, **não há tarifa dinâmica horária de mercado** como na Europa; o sinal de preço disponível é **tarifa branca + bandeiras**. A "tarifa dinâmica" plena só aparece no **mercado livre** (preço de contrato/PLD). O motor de otimização deve suportar **ambos os mundos** — ver [08](08-plataforma-cloud-e-apis.md) e [10](10-modos-de-operacao-e-features.md).

---

## 6. Serviços de rede / *grid services* no Brasil (nível N5)

Diferente da Europa (FCR/aFRR com mercados abertos a agregadores residenciais), no Brasil:

- **Serviços ancilares** são contratados pelo **ONS** (controle de frequência, reserva de potência operativa, suporte de reativos, restabelecimento) — historicamente de **grandes geradores**, não de DERs residenciais.
- **Resposta da demanda / serviços ancilares — avanços recentes (2025–2026):** a ANEEL criou um **sandbox regulatório** para testar **contratação competitiva de serviços ancilares** (primeiros projetos em subestações de MG) e **autorizou o ONS a contratar serviços ancilares de controle de tensão** (out/2025; TSA 2026 ≈ R$ 10,41/Mvar-h). A **agenda regulatória** inclui requisitos de **observabilidade, operabilidade e controlabilidade de RED** (Recursos Energéticos Distribuídos).
- **Medição inteligente em BT:** a **Consulta Pública nº 001/2026** da ANEEL trata da **modernização dos sistemas de medição / medidores inteligentes** em BT — habilitador-chave para grid services e para o mercado livre residencial.
- **Armazenamento + revenue stacking:** a ANEEL reconhece o potencial do **armazenamento distribuído** com *revenue stacking* (arbitragem, resposta da demanda, suporte de tensão). Ainda assim, um **mercado amplo e remunerado para flexibilidade residencial em BT** está **em construção** — o N5 deve nascer como **capacidade técnica pronta**, monetizando conforme a regulação evolui. `[VERIFICAR regras finais]`

**Impacto no produto:** o nível **N5 (grid services)** deve ser construído como **capacidade técnica pronta** (medição, telemetria, despacho, agregação — ver [08](08-plataforma-cloud-e-apis.md)) porém com **monetização condicionada à evolução regulatória**. No curto prazo, o "grid service" viável é mais **local/contratual** (ex.: limitação de injeção/curtailment por ordem da distribuidora, controle de reativo, gestão de demanda contratada) — análogo funcional ao **§14a alemão** citado pelas fontes, mas adaptado ao Brasil. Detalhe em [10](10-modos-de-operacao-e-features.md) e [11](11-matriz-de-cenarios.md).

---

## 7. Normas técnicas e certificação (requisitos do hardware e da conexão)

### Conexão de GD à rede (PRODIST)
- **PRODIST Módulo 3** — procedimentos de **acesso e conexão** de micro/minigeração à distribuição (solicitação de acesso, parecer, requisitos de proteção, medição).
- **REN ANEEL 1.098/2024** — **dispensa a análise de inversão de fluxo** em três casos, incluindo **micro/minigeração que não injeta na rede ("grid zero" / zero-export)** e autoconsumo local até 7,5 kW. **Favorável ao Smart**: a topologia zero-export simplifica a conexão. `[VERIFICAR aplicabilidade por distribuidora]`

### Inversores e sistema FV (ABNT)
| Norma | Escopo |
|---|---|
| **ABNT NBR 16149** | Características da interface de conexão de inversores FV à rede |
| **ABNT NBR 16150** | Procedimentos de ensaio de conformidade da interface |
| **ABNT NBR 16274** | Sistemas FV conectados à rede — documentação, comissionamento e inspeção |
| **ABNT NBR IEC 62116** | Ensaio de **anti-ilhamento** (prevenção de ilhamento) |
| **ABNT NBR 16690** | Instalações elétricas de arranjos FV |

### Certificação compulsória e homologação
- **INMETRO** — certificação compulsória de equipamentos FV (módulos, **inversores**, controladores de carga e baterias) consolidada na **Portaria nº 140/2022**, alterada pela **Portaria nº 515/2023** (inclui **dispositivo de desconexão de emergência**). Escopo cobre inversores até **75 kW**; desde **02/05/2025** só se fabrica/importa inversores **> 10 kW** conforme a 140/2022. *(Aplica-se ao **inversor**, não ao gateway Smart — ver [06](06-especificacao-hardware.md).)*
- **ANATEL** — **homologação obrigatória** de qualquer produto com radiofrequência (Wi-Fi, Bluetooth, celular 4G/LTE) — aplica-se ao **hardware Smart** (ver [06](06-especificacao-hardware.md)).
- **Segurança elétrica** — conformidade com ABNT/NBR aplicáveis ao equipamento eletroeletrônico e instalação (ex.: NBR 5410 para instalações de BT) `[VERIFICAR]`.

### Carregadores de VE e armazenamento
- **ABNT NBR IEC 61851** (sistema de carga condutiva de VE; modos de carga) e **NBR IEC 62196** (conectores/plugues).
- **Armazenamento (baterias/ESS):** regulação específica em **construção** no Brasil; aplicar normas IEC/ABNT de segurança de baterias e seguir consultas/REN da ANEEL `[VERIFICAR]`.

### Medição
- GD exige **medidor bidirecional** que diferencie energia **consumida** e **injetada** (**PRODIST Módulo 5**, REN 956/2021). Medidor de **faturamento** deve ter **modelo aprovado pelo INMETRO** (RTM **Portaria 587/2012** — classes D 0,2% / C 0,5% / B 1,0% / A 2,0%). Para **mercado livre**, medição apta ao **SMF/CCEE** (memória de massa 5–60 min por ≥ 32 dias, relógio sincronizável GMT-3, ABNT/IEC). `[VERIFICAR requisitos por porte]`
- **INMETRO Portaria 657/2025** (vigência **01/01/2026**) — substitui a *verificação inicial* pela **Declaração de Conformidade** do fabricante/importador autorizado para instrumentos de medição (inclui medidores de energia); verificações periódicas/pós-reparo permanecem. **Favorece medidor OEM** já certificado (ver [06](06-especificacao-hardware.md)). `[VERIFICAR autorização para emitir DC]`
- **Troca nacional de medidores de BT até ~2035** (Portaria Normativa 126/2026, meta ~2%/ano por distribuidora) — amplia a base de **medição inteligente**, habilitador de dados para o Smart. `[VERIFICAR]`

---

## 8. Síntese de implicações para o Smart

1. **Dois mundos de preço:** cativo = tarifa regulada (convencional/branca/bandeiras); livre = contrato/PLD. O motor de otimização precisa de **ambos** ([08](08-plataforma-cloud-e-apis.md)).
2. **GD compartilhada = rateio + créditos + Fio B:** requer um subsistema de **billing/conciliação multi-UC** ([08](08-plataforma-cloud-e-apis.md)).
3. **Grid services = capacidade técnica pronta, monetização gradual:** construir N5 sem depender de mercado que ainda não existe em BT ([11](11-matriz-de-cenarios.md)).
4. **Hardware deve nascer certificável no Brasil:** INMETRO + ANATEL + ABNT desde o design ([06](06-especificacao-hardware.md)).
5. **Conexão segue PRODIST/ABNT:** o produto deve **respeitar** (não burlar) as proteções do inversor (anti-ilhamento) e limites de injeção ([07](07-especificacao-firmware-edge.md)).

> Lacunas e dependências regulatórias críticas estão consolidadas em [13 — Gaps, Riscos e Decisões](13-gaps-riscos-e-decisoes.md).
