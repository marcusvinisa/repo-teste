# EOS-DENO · Mapa de Especificações & Funcionalidades

> **O que é:** a árvore completa de capacidades de um EMS/HEMS/VPP/DER de classe mundial — montada como **mapa de engenharia**, não checklist. Cada item traz três coisas: um **número** hierárquico (camada · capacidade · sub-feature), **o que é / faz** (o destino), e **como é feito ou pode ser feito** (o mecanismo). Esta é a rubrica contra a qual os 11 players são pontuados (ver `eos-deno-scoring-11-players`).

**Escopo:** núcleo residencial/GD (00–09) · C&I em camada separada · horizonte 2030 à parte.
**★** = capacidade de alto valor estratégico para a tese EOS-DENO.
Tudo no nível 4 (ideal) por definição — a coluna **Como** descreve o mecanismo de classe mundial.

---

## 00 · Medição & Sensoriamento
*A fundação — o sensor sobre o qual todo o resto se empilha.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 00.1.1 | Medição elétrica | Grandezas medidas | V (L-N/L-L), I, P/Q/S, FP, freq, energia import/export, THD, desequilíbrio | Amostragem simultânea de tensão (divisor resistivo) e corrente (TC/Rogowski) a kHz; um metering IC/DSP (ADE/STPM) calcula RMS, potências e harmônicos por FFT |
| 00.1.2 | Medição elétrica | Topologia de rede | Mono/bi/trifásico, 3 e 4 fios, detecção automática | Múltiplos canais de V e I no front-end; o firmware detecta presença e defasagem das fases e auto-seleciona a topologia |
| 00.1.3 | Medição elétrica | Método de aquisição | TC split/solid-core, Rogowski, shunt — ou medidor externo | TC split-core clipa no cabo sem cortar a fiação (retrofit); ou lê o medidor da concessionária via óptica/P1/Modbus |
| 00.1.4 | Medição elétrica | Classe metrológica | Classe 0.5S/1 (IEC 62053), bidirecional, billing-grade | Metering IC calibrado em laboratório contra padrão rastreável; aprovação INMETRO via ensaio de exatidão sob carga e temperatura |
| 00.1.5 | Medição elétrica | Resolução temporal | Sub-segundo (transitórios), 1s (controle), 1–15min (telemetria) | Buffer de alta taxa captura eventos (sag/swell) + agregação configurável para telemetria e faturamento |
| 00.1.6 | Medição elétrica | Submedição | Por circuito, por carga, por fase — múltiplos pontos | Um TC por derivação do quadro (circuito) ou por carga; ou rede de submedidores em barramento Modbus/RS485 — cada ponto é um canal independente |
| 00.2.1 | Sensoriamento ambiental | Irradiância solar | Piranômetro / sensor de referência | Sensor de irradiância na entrada analógica; correlaciona com a geração para calibrar previsão e detectar sujeira/sombra |
| 00.2.2 | Sensoriamento ambiental | Temperatura | De painel, bateria, ambiente | Termistores/RTD (PT100) ou 1-Wire nos pontos críticos; usado para derating de potência e proteção térmica da bateria |
| 00.2.3 | Sensoriamento ambiental | Qualidade de energia | Sags/swells, flicker, detecção de ilhamento | Janela RMS rápida + monitoramento de freq/fase; algoritmo anti-ilhamento (salto de freq) desconecta na perda de rede |
| 00.3.1 | Estado de ativos | Bateria | SOC, SOH, temperatura, ciclos, potência | Leitura do BMS via CAN/Modbus do inversor híbrido; SOC do balanço de carga, SOH da degradação de capacidade ao longo dos ciclos |
| 00.3.2 | Estado de ativos | Inversor / geração | Status, potência, alarmes, curva de geração | Polling Modbus/SunSpec dos registradores (potência, falha, energia acumulada) a cada poucos segundos |
| 00.3.3 | Estado de ativos | Cargas | Consumo por dispositivo, on/off, NILM | Smart plug por carga (medição direta) ou NILM — ML desagrega o consumo agregado por assinatura, sem sensor em cada aparelho |

## 01 · Conectividade & Protocolos
*O sistema nervoso — como o produto fala com tudo.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 01.1.1 | Comunicação física | Sem fio curto | Wi-Fi (2.4/5GHz), BLE, Zigbee, Z-Wave, Thread/Matter | SoC de rádio (ESP32/Nordic): Wi-Fi p/ nuvem, BLE p/ comissionamento, Zigbee/Thread/Matter p/ malha de dispositivos |
| 01.1.2 | Comunicação física | Celular | 4G/LTE, NB-IoT/Cat-M, 5G | Modem celular embarcado + SIM/eSIM M2M; NB-IoT/Cat-M p/ baixo consumo onde não há Wi-Fi, autonomia total do roteador do cliente |
| 01.1.3 | Comunicação física | Serial / barramento | RS485, RS232, CAN | Transceiver RS485 p/ barramento Modbus multidrop (~500m/32 nós); CAN p/ o BMS da bateria |
| 01.1.4 | Comunicação física | Cabeada | Ethernet / LAN (gigabit) | PHY Ethernet p/ conexão estável; preferida em C&I e onde o Wi-Fi é instável |
| 01.2.1 | Protocolos de energia | Medição/inversor | Modbus-RTU/TCP, SunSpec, DLMS/COSEM | Stack Modbus mestre lê/escreve holding registers; o mapa SunSpec padroniza registradores entre fabricantes; DLMS p/ medidores de concessionária |
| 01.2.2 | Protocolos de energia | Grid / utility | IEC 61850, IEC 60870-5-104, DNP3 | Protocolos de subestação/telecontrole p/ interface com o SCADA da distribuidora — usados em despacho e serviços de rede |
| 01.2.3 | Protocolos de energia | Cargas / IoT | MQTT, REST/JSON, EEBUS, KNX | MQTT (pub/sub leve) p/ telemetria; REST/JSON p/ integração; EEBUS p/ bomba/VE (padrão europeu); KNX p/ automação predial |
| 01.2.4 | Protocolos de energia | Ativos específicos | OCPP (VE), SG-Ready (bomba de calor) | OCPP sobre WebSocket comanda a corrente de carga; SG-Ready aciona modos da bomba por contato seco (DO) |
| 01.3.1 | I/O físico | Entradas | DI (contatos, RCR/ripple), AI (0-10V/4-20mA) | Optoacopladores isolam as DI (sinal de ripple/RCR); ADC lê as AI de sensores |
| 01.3.2 | I/O físico | Saídas | DO/relé, analógicas | Relés ou saídas a transistor comandam contatores/cargas diretamente — atuação local sem depender da nuvem |
| 01.4.1 | Ciclo de vida de firmware | Atualização | OTA remoto + USB local, rollback | Flash dual-bank (A/B): baixa em background, valida checksum, troca o boot e reverte se falhar |
| 01.4.2 | Ciclo de vida de firmware | Segurança de firmware | Assinatura, versionamento, anti-tamper | Imagem assinada com chave privada do fabricante e verificada no boot; secure boot rejeita firmware não-assinado |
| 01.5.1 | Gateway de borda | Resiliência offline | Store-and-forward, broker local, opera sem nuvem | Buffer em flash/RAM guarda telemetria na queda do link e reenvia ao reconectar; broker MQTT local mantém os dispositivos coordenados |
| 01.5.2 | Gateway de borda | Runtime de borda | Executa lógica/modelos localmente (edge compute) | Runtime leve no SoC (contêiner/WASM) roda regras e modelos de otimização localmente, sem ida-e-volta à nuvem |

## 02 · Integração & Comando de Ativos
*As mãos — ler é monitorar; comandar é controlar.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 02.1.1 | Inversor FV | Leitura | Geração, status, alarmes | Polling dos registradores de leitura via Modbus/SunSpec |
| 02.1.2 | Inversor FV | Comando | Curtailment / limite de potência ativa, reativo | Escrita nos registradores de setpoint (% de potência ativa, cosφ/Q) — limita injeção e ajusta reativo em malha fechada |
| 02.2.1 | Bateria / BESS | Leitura | SOC, SOH, potência | Leitura via inversor híbrido/BMS por CAN/Modbus |
| 02.2.2 | Bateria / BESS | Comando | Setpoint carga/descarga, limites SOC, modo | Escreve setpoint de potência (kW) e limites de SOC no inversor híbrido; seleciona o modo (autoconsumo/backup/arbitragem) |
| 02.3.1 | Carregador de VE | Leitura | Estado de sessão, potência, conector | OCPP/Modbus reporta o estado da sessão e a energia transferida |
| 02.3.2 | Carregador de VE | Comando | Corrente de carga, smart charging (OCPP), V2G/V2H | OCPP ajusta a corrente (6–32A) conforme excedente/tarifa; V2G/V2H exige carregador bidirecional p/ devolver energia |
| 02.4.1 | Bomba de calor | Comando | SG-Ready, Modbus/EEBUS, power-to-heat | Contato seco SG-Ready (4 estados) ou Modbus/EEBUS desloca o aquecimento p/ janelas de excedente solar/tarifa baixa |
| 02.4.2 | Bomba de calor | Cargas térmicas | Boiler/água quente, AC, piscina | Relé/contator no circuito da resistência/bomba; usa a inércia térmica do reservatório como armazenamento |
| 02.5.1 | Cargas & eletrodomésticos | Comando | Smart plugs, relés, liga/desliga, dimming, agendamento | Smart plug (Wi-Fi/Zigbee) ou relé liga/desliga a carga; agenda por excedente de geração ou por tarifa |
| 02.5.2 | Cargas & eletrodomésticos | Eletrodomésticos | Linha branca, gestão de partida | Integração via API do fabricante (Home Connect) ou Matter; difere a partida de máquinas p/ as janelas mais baratas |
| 02.6.1 | Geração de backup | Genset | Partida/parada, sincronismo, transferência | DO de partida + leitura de status; controle de transferência (ATS) e sincronismo em sistemas híbridos |
| 02.7.1 | ★ Agnosticismo de fabricante | Camada de driver/abstração | Abstrai N fabricantes atrás de API única | Um driver por fabricante traduz o mapa Modbus/API proprietário p/ um modelo de dados canônico — o resto do sistema fala uma só língua |
| 02.7.2 | ★ Agnosticismo de fabricante | Cobertura multimarca | Dezenas a centenas de marcas | Biblioteca de perfis de equipamento, versionada; cada perfil é um arquivo de mapeamento testado em laboratório |
| 02.7.3 | ★ Agnosticismo de fabricante | Onboarding de equipamento | Auto-detecção, lista pública, certificação | Varredura do barramento + identificação pelo registrador de modelo; fallback manual ("Outros") e processo de certificação de novo device |

## 03 · Controle & EMS
*As regras — proteção, qualidade e despacho determinístico.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 03.1.1 | Proteção & qualidade | Autoconsumo | Maximiza o uso local da geração | Loop de controle: quando geração > consumo, direciona o excedente p/ bateria/cargas antes de exportar |
| 03.1.2 | Proteção & qualidade | Anti-backfeed / zero feed-in | Limita ou zera a exportação | Medição no ponto de conexão + curtailment do inversor em malha fechada p/ manter injeção ≤ limite |
| 03.1.3 | Proteção & qualidade | Limite de demanda / peak shaving | Corta picos (demand charge) | Monitora a demanda em janela móvel (15min) e descarrega bateria/desliga cargas ao se aproximar do teto contratado |
| 03.1.4 | Proteção & qualidade | Controle de potência | Ativa (curtailment) e reativa (FP, tensão) | Setpoint de P e Q escrito no inversor conforme a regra ou a ordem da rede |
| 03.1.5 | Proteção & qualidade | Proteção de fusível/disjuntor | Anti-trip no ponto de conexão | Soma das correntes por fase em tempo real; reduz a carga de VE/bomba antes que o disjuntor atue (load balancing dinâmico) |
| 03.1.6 | Proteção & qualidade | Balanço de fase | Compensação entre fases | Redistribui cargas controláveis e potência do inversor entre as fases p/ equalizar corrente |
| 03.1.7 | Proteção & qualidade | Backup / ilhamento | Transição on→off-grid, ilha, religamento | Detecção de queda + chave de transferência; inversor forma a rede (grid-forming) na ilha e ressincroniza no retorno |
| 03.1.8 | Proteção & qualidade | Priorização de cargas | Load shedding hierárquico | Tabela de prioridade; em déficit, desliga as cargas da menor prioridade p/ a maior |
| 03.2.1 | Otimização econômica | Time-of-Use (ToU) | Arbitragem em tarifa horária | Carrega em fora-ponta (barato) e descarrega na ponta (caro) por agenda fixa de tarifa |
| 03.2.2 | Otimização econômica | Tarifa dinâmica | Day-ahead / spot / 15-min | Ingere a curva de preço futura (API) e otimiza carga/descarga contra ela |
| 03.2.3 | Otimização econômica | Tarifa BR | Tarifa branca, bandeiras, ponta/fora-ponta | Modela a estrutura tarifária brasileira dentro do otimizador |
| 03.2.4 | Otimização econômica | Multi-objetivo | Custo × autoconsumo × vida de bateria × CO₂ | Função-objetivo ponderada que penaliza custo, ciclos de bateria e emissões simultaneamente |

## 04 · Inteligência / AI
*O cérebro — prever, otimizar, aprender.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 04.1.1 | Previsão | Geração solar | Curva de geração intraday → multi-dia | Modelo físico (clear-sky + geometria) ajustado por ML sobre histórico do site + previsão meteorológica (nuvem/irradiância de API ou satélite) |
| 04.1.2 | Previsão | Carga / consumo | Perfil de demanda futura | ML (gradient boosting/LSTM) sobre histórico + calendário/clima; opcionalmente desagregado por dispositivo via NILM |
| 04.1.3 | Previsão | Preço | Day-ahead / spot | Série temporal sobre preços históricos + sinais de mercado; ou ingestão direta da curva day-ahead publicada |
| 04.2.1 | Otimização / scheduling | Motor de decisão | Rule-based → LP/MILP → MPC → RL | Formula o despacho como problema de otimização (MILP) com horizonte; MPC re-resolve a cada passo; RL p/ políticas adaptativas |
| 04.2.2 | Otimização / scheduling | Horizonte & cadência | Planeja 24–48h, re-otimiza a cada 15min | Janela rolante (receding horizon): plano de 24–48h recomputado a cada 15min com dados frescos |
| 04.3.1 | Aprendizado & adaptação | Adaptação ao usuário | Aprende padrões sem update manual | Modelo online re-treina com os dados do próprio site e ajusta padrões (rotina de banho/VE) sem firmware novo |
| 04.3.2 | Aprendizado & adaptação | Detecção de anomalia | Falha, degradação, desvio de geração | Compara baseline esperado vs. medido; o desvio dispara alerta |
| 04.3.3 | Aprendizado & adaptação | NILM | Desagregação não-intrusiva | ML sobre a curva agregada identifica a assinatura de cada aparelho sem medidor por carga |
| 04.4.1 | ★ Locus de compute | Arquitetura | Nuvem pura · edge puro · híbrido cloud-edge | Controle crítico no edge (device); otimização pesada e treino na nuvem; os dois sincronizam o plano |
| 04.4.2 | ★ Locus de compute | Resiliência | Controle ótimo sobrevive à queda da nuvem | Device guarda o último plano/política e regras de fallback; opera horas/dias offline e ressincroniza ao reconectar |

## 05 · Despacho Externo & Flexibilidade / VPP
*A interface com a rede e o mercado — onde DER vira receita.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 05.1.1 | Sinais de rede / DSO | Despacho da distribuidora | RCR/ripple, §14a, telecontrole/RTU, control box | Recebe o sinal de controle (ripple via DI, ou control box digital/§14a) e aplica o curtailment/limite ordenado |
| 05.1.2 | Sinais de rede / DSO | BR-equivalente | Comandos da distribuidora, corte/religamento | Interface com o comando da distribuidora (futuro padrão BR) p/ corte/religamento e limite de injeção remotos |
| 05.2.1 | ★ Agregação / VPP | Agregação de DER | Coordena frota como usina virtual | Plataforma na nuvem coordena milhares de baterias/inversores como um recurso único, despachando setpoints em massa |
| 05.2.2 | ★ Agregação / VPP | Papel de mercado | BSP / BRP | Qualificação junto ao operador (ONS/distribuidora no BR) p/ ofertar a capacidade agregada como recurso de balanceamento |
| 05.2.3 | ★ Agregação / VPP | Serviços ancilares | FCR, aFRR, mFRR, reserva, tensão | Resposta automática a desvio de frequência (droop) ou a sinal do operador (AGC), com tempo de resposta certificado |
| 05.2.4 | ★ Agregação / VPP | Demand response | Resposta da demanda, capacity market | Em um evento, a plataforma desliga/desloca as cargas agregadas mediante incentivo ou contrato de capacidade |
| 05.3.1 | Trading / mercado | Mercados | Day-ahead, intraday, imbalance/balancing | Algoritmo de bidding posiciona a flexibilidade agregada nos mercados; arbitra entre autoconsumo e venda |
| 05.3.2 | Trading / mercado | Interface comercial | Comercializadoras/tradings, direct marketing | API p/ a comercializadora/trading que liquida a energia; direct marketing da geração |
| 05.3.3 | Trading / mercado | BR | CCEE, mercado livre (ACL), curto prazo | Integração com a CCEE (medição, contabilização, liquidação) e gestão de contratos no mercado livre |
| 05.4.1 | Desligamento remoto | Curtailment remoto | Corte sob comando do operador/agregador | O comando escreve o limite/zero no inversor; cada intervenção fica em trilha de auditoria |

## 06 · Plataforma, Nuvem & Dados
*A plataforma — onde o produto vira negócio escalável.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 06.1.1 | App & portal | Aplicações | App usuário, portal instalador, dashboard operador | Front-end web/mobile sobre a API; visões distintas por papel (consumo, diagnóstico, frota) |
| 06.1.2 | App & portal | Papéis & permissões | RBAC, multi-tenant, multi-site | Tenants isolados + RBAC; cada organização vê só seus ativos, com hierarquia de permissão |
| 06.2.1 | ★ API & integração | API aberta | REST/GraphQL, webhooks, SDK | API documentada (OpenAPI) + webhooks de eventos + SDK p/ terceiros construírem integrações |
| 06.2.2 | ★ API & integração | White-label | Marca do parceiro, multi-tenant, marketplace | Tematização (logo/cores/domínio) por tenant + marketplace de módulos; o parceiro entrega como produto próprio |
| 06.2.3 | ★ API & integração | Cloud-to-cloud | Home Assistant, Google Home, Alexa | Conectores OAuth p/ os ecossistemas — integra sem hardware adicional |
| 06.3.1 | Dados & analytics | Telemetria | Tempo real + histórico (granularidade configurável) | Time-series DB (Influx/Timescale) com retenção configurável; streaming em tempo real via WebSocket |
| 06.3.2 | Dados & analytics | Export & relatórios | CSV/API alta resolução, relatórios automáticos | Exportação de séries via API/CSV; relatórios (economia, geração) agendados |
| 06.3.3 | Dados & analytics | Pipeline de ML | Data lake, treino de modelos, feature store | Data lake + pipeline de features/treino que alimenta os modelos e melhora com o agregado da frota |
| 06.4.1 | Comissionamento & O&M | Setup | Web/app/QR, auto-config, sem-app opcional | QR no device abre o fluxo web; a auto-detecção de ativos reduz a configuração manual |
| 06.4.2 | Comissionamento & O&M | Diagnóstico remoto | Troubleshooting remoto, alarmes, RMA | Logs/telemetria remotos + acesso remoto ao device p/ diagnóstico sem ir a campo; fluxo de RMA |
| 06.4.3 | Comissionamento & O&M | Fleet management | Frota em escala, atualização em massa | Console que aplica config/firmware em lote a milhares de devices, com rollout em ondas e monitoramento de saúde |
| 06.5.1 | Monetização | Modelos de receita | Assinatura, licença, white-label, revenue-share, freemium | Cobrança recorrente por device/seat, licença de plataforma, ou revenue-share da flexibilidade despachada |

## 07 · Conformidade, Segurança & Mercado
*A confiança — sem isto, não conecta na rede nem fatura.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 07.1.1 | ★ Conformidade grid-code | Internacional | CE, EN 18031, IEC 62368, grid codes locais | Ensaios de EMC e segurança em laboratório acreditado; conformidade com o grid code do mercado-alvo |
| 07.1.2 | ★ Conformidade grid-code | Brasil | ANEEL/PRODIST, INMETRO, homologação de distribuidora, NBR | Homologação INMETRO da medição + aderência ao PRODIST + homologação junto à distribuidora |
| 07.2.1 | Certificação metrológica | Faturamento | Selo metrológico p/ medição faturável | Aprovação de modelo INMETRO + verificação inicial/periódica p/ valor fiscal |
| 07.3.1 | Segurança / cyber | Proteção de dados | TLS, encriptação em repouso, LGPD/GDPR | TLS em trânsito + encriptação em repouso; tratamento de dados pessoais conforme a LGPD |
| 07.3.2 | Segurança / cyber | Hardening | Assinatura de firmware, pen-testing, NIS2, BSI TR-03109 | Secure boot + firmware assinado + pen-testing periódico + gestão de vulnerabilidades |
| 07.4.1 | Mercados homologados | Geografias | Onde é certificado e opera de fato | Matriz de certificações por país/distribuidora define onde o produto pode ser conectado legalmente |

## 08 · Hardware & Forma
*O corpo — onde há hardware (vs. software/nuvem puro).*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 08.1.1 | Forma & instalação | Formato | Gateway DIN-rail, medidor, módulo, plug | SKU por papel: gateway em trilho DIN (quadro), medidor com TCs (retrofit), módulo ou plug (carga única) |
| 08.1.2 | Forma & instalação | Montagem | Trilho DIN, parede, mesa | Trilho DIN 35mm no quadro ou fixação em parede; dimensões compactas p/ caber no QDC |
| 08.2.1 | Robustez ambiental | Proteção | IP20 (indoor) → IP65 (outdoor abrigado) | Gabinete vedado (IP65) p/ áreas externas abrigadas; IP20 onde fica em quadro interno |
| 08.2.2 | Robustez ambiental | Faixa térmica & consumo | -30~+70°C, <5–7W | Componentes grau industrial + projeto de baixo consumo (sem ventilação ativa) |
| 08.3.1 | Interface local | Display & indicadores | TFT / LED bar / e-paper, botões | Display TFT/e-paper mostra estado e QR de comissionamento; LED/RGB p/ status rápido; botões p/ ações locais |

## 09 · UX & Conveniência
*A experiência — simplicidade é capacidade de produto (a lição do Zerofy).*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 09.1.1 | ★ Onboarding sem fricção | Instalação | Sem app (web/QR), auto-detecção, plug-and-play | Comissionamento pelo navegador (sem baixar app) + auto-detecção de ativos; o instalador conclui em minutos |
| 09.2.1 | Operação autônoma | Autopilot | Otimiza sozinho, sem intervenção | Modo padrão que aplica a melhor estratégia automaticamente; o usuário não precisa configurar regras |
| 09.3.1 | Engajamento | Visualização de valor | Economia em R$, CO₂ evitado, gamificação | O dashboard traduz kWh em R$ economizados e CO₂ evitado; metas/streaks aumentam a retenção |
| 09.3.2 | Engajamento | Copilot / linguagem natural | Pergunta e comanda em linguagem natural | Interface conversacional (LLM) sobre os dados e controles — "quanto economizei?" ou "carregue o carro até as 7h" |
| 09.4.1 | Multi-residência | Multi-site | Vários imóveis/clientes em uma conta | Uma conta agrega múltiplos sites com visão consolidada — p/ prosumidores e gestores |

---

## C&I · Comercial & Industrial *(módulo acoplável)*
*Separada do núcleo residencial/GD.*

| # | Capacidade | Sub-feature | O que é (destino) | Como é feito / pode ser feito |
|---|---|---|---|---|
| C&I.1.1 | Medição & submedição em escala | Multi-ponto | Dezenas de pontos/circuitos, hierarquia, rateio por centro de custo | Rede de submedidores em Modbus/RS485 (ou TCs por circuito) mapeados a centros de custo; o gateway concentra dezenas de pontos |
| C&I.1.2 | Medição & submedição em escala | Qualidade de energia C&I | Harmônicos, FP por ponto, registro de eventos | Analisador de qualidade por ponto registra harmônicos/FP/eventos p/ conformidade e diagnóstico |
| C&I.2.1 | Gestão de demanda contratada | Demanda BR | Demanda contratada, ultrapassagem, otimização de contrato | Monitora a demanda vs. a contratada; atua p/ evitar ultrapassagem (multa) e sugere ajuste do contrato |
| C&I.2.2 | Gestão de demanda contratada | Correção de FP em escala | Banco de capacitores, reativo industrial | Controlador de banco de capacitores chaveia estágios p/ manter o FP ≥ 0,92 e evitar multa por reativo |
| C&I.3.1 | Portfólio & multi-site | Energy management de portfólio | Múltiplas plantas, benchmarking, metas | Consolida múltiplas plantas numa só visão; benchmarking entre sites e metas de redução |
| C&I.3.2 | Portfólio & multi-site | Integração SCADA/BMS | Building Management System, automação | Protocolos industriais (Modbus/BACnet/IEC) conectam ao BMS/SCADA predial-industrial já existente |
| C&I.4.1 | Mercado livre (ACL) | Gestão de portfólio de energia | Contratos ACL, sazonalização, flexibilidade, CCEE | Modela contratos ACL, sazonalização e flexibilidade; integra à contabilização da CCEE |
| C&I.4.2 | Mercado livre (ACL) | Geração distribuída C&I | Autoprodução, consórcio, geração compartilhada | Gestão de autoprodução/consórcio/geração compartilhada com rateio de créditos entre unidades |

---

## 2030 · Horizonte — a fronteira
*Capacidades que quase nenhum dos 11 players tem hoje, mas que a régua AI-native + a abertura regulatória BR vão exigir.*

| # | Capacidade | Sub-feature | O que é (fronteira) | Como é feito / pode ser feito |
|---|---|---|---|---|
| 2030.1.1 | Operação AI-native | Agent-fabric | Agentes autônomos por persona operando o sistema | Agentes LLM por persona (gerador, agregador, consumidor), cada um com ferramentas que leem/escrevem nos ativos e mercados sob políticas |
| 2030.1.2 | Operação AI-native | Linguagem natural end-to-end | Configurar, diagnosticar e despachar por conversa | Copilot operacional traduz a intenção ("priorize o carro amanhã") em ações concretas nos sistemas |
| 2030.2.1 | Mercados emergentes | P2P energy trading | Negociação peer-to-peer (quando houver base legal BR) | Plataforma casa ofertas entre prosumidores; liquidação por contrato/registro quando a regulação BR permitir |
| 2030.2.2 | Mercados emergentes | Transactive energy | Liquidação automática, settlement programável/blockchain | Settlement automático entre agentes (possivelmente sobre ledger) conforme as regras do mercado, sem conciliação manual |
| 2030.2.3 | Mercados emergentes | CCEE-nativo + liquidação automática | Integração e liquidação no mercado livre sem intermediário | Integração direta com a medição/contabilização/liquidação da CCEE — o ciclo de mercado fecha sem intermediário manual |
| 2030.3.1 | Controle de rede avançado | Dynamic Operating Envelopes (DOE) | Envelopes operacionais dinâmicos por nó | Recebe da distribuidora um envelope (limite de import/export variável por nó/hora) e o respeita em tempo real no inversor |
| 2030.3.2 | Controle de rede avançado | Grid-forming orchestration | Coordenação de inversores formadores de rede | Coordena inversores grid-forming p/ manter estabilidade de tensão/frequência em alta penetração de FV |
| 2030.4.1 | Frota & ativos inteligentes | V2G em escala | Frota de VEs como armazenamento despachável | Agrega VEs bidirecionais como armazenamento despachável, respeitando rotina e SOC mínimo do dono |
| 2030.4.2 | Frota & ativos inteligentes | Digital twin em tempo real | Gêmeo digital p/ simulação e controle | Réplica em tempo real do sistema simula cenários ("e se?") e otimiza antes de atuar no físico |
| 2030.4.3 | Frota & ativos inteligentes | Manutenção preditiva em frota | ML prevê falha antes de ocorrer | ML sobre a telemetria da frota detecta a assinatura de falha iminente (inversor/bateria) e agenda a manutenção antes da parada |

---

*Mapa de especificações montado com engenharia de energia (EMS/HEMS/VPP/DER) + os 11 players pesquisados. A coluna **Como** é nível-arquitetural (o mecanismo correto), não datasheet de componente. Projeto EOS-DENO · v2. Espelha `eos-deno-matriz-produto-ideal-v2.html`.*
