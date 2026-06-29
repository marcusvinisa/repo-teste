# EOS-DENO · Mapa de Especificações & Funcionalidades

> **Estudo de referência curado pelo usuário.** Reproduzido em `referencias/`. Ver [00-absorcao-e-ajustes.md](00-absorcao-e-ajustes.md).

> **O que é:** a árvore completa de capacidades de um EMS/HEMS/VPP/DER de classe mundial — **mapa de engenharia**, não checklist. Cada item: **número** hierárquico, **o que é/faz** (destino), e **como é feito ou pode ser feito** (mecanismo). Rubrica contra a qual os 11 players são pontuados.

**Escopo:** núcleo residencial/GD (00–09) · C&I em camada separada · horizonte 2030 à parte. **★** = alto valor estratégico. Tudo no nível 4 (ideal) — a coluna **Como** descreve o mecanismo de classe mundial.

---

## 00 · Medição & Sensoriamento
*A fundação — o sensor sobre o qual todo o resto se empilha.*

| # | Capacidade | Sub-feature | O que é | Como é feito / pode ser feito |
|---|---|---|---|---|
| 00.1.1 | Medição elétrica | Grandezas | V (L-N/L-L), I, P/Q/S, FP, freq, energia import/export, THD, desequilíbrio | Amostragem simultânea de V (divisor resistivo) e I (TC/Rogowski) a kHz; metering IC/DSP (ADE/STPM) calcula RMS, potências e harmônicos |
| 00.1.2 | Medição elétrica | Topologia de rede | Mono/bi/trifásico, 3 e 4 fios, detecção automática | Múltiplos canais V e I; firmware detecta fases e auto-seleciona topologia |
| 00.1.3 | Medição elétrica | Método de aquisição | TC split/solid-core, Rogowski, shunt — ou medidor externo | TC split-core clipa no cabo (retrofit); ou lê medidor da concessionária via óptica/P1/Modbus |
| 00.1.4 | Medição elétrica | Classe metrológica | Classe 0.5S/1 (IEC 62053), bidirecional, billing-grade | Metering IC calibrado contra padrão rastreável; aprovação INMETRO via ensaio sob carga/temperatura |
| 00.1.5 | Medição elétrica | Resolução temporal | Sub-segundo (transitórios), 1s (controle), 1–15min (telemetria) | Buffer de alta taxa (sag/swell) + agregação configurável |
| 00.1.6 | Medição elétrica | Submedição | Por circuito, carga, fase — múltiplos pontos | Um TC por derivação ou rede de submedidores em barramento Modbus/RS485 |
| 00.2.1 | Sensoriamento ambiental | Irradiância | Piranômetro / sensor de referência | Sensor na entrada analógica; correlaciona com geração p/ calibrar previsão e detectar sujeira/sombra |
| 00.2.2 | Sensoriamento ambiental | Temperatura | Painel, bateria, ambiente | Termistores/RTD (PT100) ou 1-Wire; usado p/ derating e proteção térmica |
| 00.2.3 | Sensoriamento ambiental | Qualidade de energia | Sags/swells, flicker, detecção de ilhamento | Janela RMS rápida + monitoramento freq/fase; algoritmo anti-ilhamento |
| 00.3.1 | Estado de ativos | Bateria | SOC, SOH, temperatura, ciclos, potência | Leitura do BMS via CAN/Modbus do híbrido |
| 00.3.2 | Estado de ativos | Inversor/geração | Status, potência, alarmes, curva | Polling Modbus/SunSpec a cada poucos segundos |
| 00.3.3 | Estado de ativos | Cargas | Consumo por dispositivo, on/off, NILM | Smart plug por carga ou NILM (ML desagrega consumo agregado) |

## 01 · Conectividade & Protocolos
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 01.1.1 | Comunicação física | Sem fio curto | Wi-Fi, BLE, Zigbee, Z-Wave, Thread/Matter | SoC de rádio (ESP32/Nordic) |
| 01.1.2 | Comunicação física | Celular | 4G/LTE, NB-IoT/Cat-M, 5G | Modem celular + SIM/eSIM M2M |
| 01.1.3 | Comunicação física | Serial/barramento | RS485, RS232, CAN | Transceiver RS485 (Modbus multidrop); CAN p/ BMS |
| 01.1.4 | Comunicação física | Cabeada | Ethernet/LAN | PHY Ethernet; preferida em C&I |
| 01.2.1 | Protocolos de energia | Medição/inversor | Modbus-RTU/TCP, SunSpec, DLMS/COSEM | Stack Modbus mestre; SunSpec padroniza registradores; DLMS p/ medidores |
| 01.2.2 | Protocolos de energia | Grid/utility | IEC 61850, IEC 60870-5-104, DNP3 | Protocolos de subestação/telecontrole p/ SCADA da distribuidora |
| 01.2.3 | Protocolos de energia | Cargas/IoT | MQTT, REST/JSON, EEBUS, KNX | MQTT (telemetria); EEBUS (bomba/VE); KNX (automação predial) |
| 01.2.4 | Protocolos de energia | Ativos específicos | OCPP (VE), SG-Ready (bomba) | OCPP sobre WebSocket; SG-Ready por contato seco |
| 01.3.1 | I/O físico | Entradas | DI (RCR/ripple), AI (0-10V/4-20mA) | Optoacopladores isolam DI; ADC lê AI |
| 01.3.2 | I/O físico | Saídas | DO/relé, analógicas | Relés/saídas a transistor comandam contatores — atuação local sem nuvem |
| 01.4.1 | Firmware | Atualização | OTA remoto + USB local, rollback | Flash dual-bank (A/B) |
| 01.4.2 | Firmware | Segurança | Assinatura, versionamento, anti-tamper | Imagem assinada; secure boot rejeita firmware não-assinado |
| 01.5.1 | Gateway de borda | Resiliência offline | Store-and-forward, broker local | Buffer em flash/RAM; broker MQTT local |
| 01.5.2 | Gateway de borda | Runtime de borda | Edge compute | Runtime leve (contêiner/WASM) roda regras/modelos localmente |

## 02 · Integração & Comando de Ativos
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 02.1.1/2 | Inversor FV | Leitura/Comando | Geração, status; curtailment/limite de P, reativo | Polling + escrita de setpoint (% P ativa, cosφ/Q) em malha fechada |
| 02.2.1/2 | Bateria/BESS | Leitura/Comando | SOC/SOH/P; setpoint carga/descarga, limites SOC, modo | Via híbrido/BMS (CAN/Modbus); modo autoconsumo/backup/arbitragem |
| 02.3.1/2 | Carregador VE | Leitura/Comando | Estado de sessão; corrente, smart charging (OCPP), V2G/V2H | OCPP ajusta corrente (6–32A); V2G/V2H exige carregador bidirecional |
| 02.4.1/2 | Bomba de calor | Comando/cargas térmicas | SG-Ready, Modbus/EEBUS, power-to-heat; boiler/AC/piscina | Contato seco SG-Ready (4 estados); inércia térmica como armazenamento |
| 02.5.1/2 | Cargas & eletrodomésticos | Comando | Smart plugs, relés, dimming, agendamento; linha branca | Smart plug/relé; API fabricante (Home Connect) ou Matter |
| 02.6.1 | Geração de backup | Genset | Partida/parada, sincronismo, transferência | DO de partida + status; ATS e sincronismo em híbridos |
| ★02.7.1 | Agnosticismo | Camada de driver | Abstrai N fabricantes atrás de API única | Driver por fabricante traduz mapa Modbus/API → canônico |
| ★02.7.2 | Agnosticismo | Cobertura multimarca | Dezenas a centenas de marcas | Biblioteca de perfis versionada; cada perfil = arquivo testado |
| ★02.7.3 | Agnosticismo | Onboarding | Auto-detecção, lista pública, certificação | Varredura do barramento + ID pelo registrador de modelo; fallback "Outros" + certificação |

## 03 · Controle & EMS
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 03.1.1 | Proteção & qualidade | Autoconsumo | Maximiza uso local da geração | Loop: excedente → bateria/cargas antes de exportar |
| 03.1.2 | Proteção & qualidade | Anti-backfeed / zero feed-in | Limita/zera exportação | Medição no ponto + curtailment em malha fechada |
| 03.1.3 | Proteção & qualidade | Peak shaving | Corta picos (demand charge) | Janela móvel 15min; descarrega bateria/desliga cargas |
| 03.1.4 | Proteção & qualidade | Controle de potência | Ativa (curtailment) e reativa (FP, tensão) | Setpoint P e Q no inversor |
| 03.1.5 | Proteção & qualidade | Anti-trip | Proteção de fusível/disjuntor | Soma de correntes em tempo real; reduz VE/bomba antes do disjuntor atuar |
| 03.1.6 | Proteção & qualidade | Balanço de fase | Compensação entre fases | Redistribui cargas e potência do inversor entre fases |
| 03.1.7 | Proteção & qualidade | Backup/ilhamento | Transição on→off-grid, ilha, religamento | Detecção de queda + chave de transferência; inversor grid-forming na ilha |
| 03.1.8 | Proteção & qualidade | Priorização de cargas | Load shedding hierárquico | Tabela de prioridade; desliga menor→maior em déficit |
| 03.2.1 | Otimização econômica | ToU | Arbitragem em tarifa horária | Carrega fora-ponta, descarrega na ponta |
| 03.2.2 | Otimização econômica | Tarifa dinâmica | Day-ahead/spot/15min | Ingere curva de preço futura e otimiza |
| 03.2.3 | Otimização econômica | Tarifa BR | Branca, bandeiras, ponta/fora-ponta | Modela estrutura tarifária BR no otimizador |
| 03.2.4 | Otimização econômica | Multi-objetivo | Custo × autoconsumo × vida de bateria × CO₂ | Função-objetivo ponderada |

## 04 · Inteligência / AI
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 04.1.1 | Previsão | Geração solar | Intraday → multi-dia | Físico (clear-sky) + ML + meteorologia (API/satélite) |
| 04.1.2 | Previsão | Carga/consumo | Demanda futura | ML (gradient boosting/LSTM) + calendário/clima; opcional NILM |
| 04.1.3 | Previsão | Preço | Day-ahead/spot | Série temporal + sinais de mercado, ou ingestão da curva |
| 04.2.1 | Otimização/scheduling | Motor de decisão | Rule-based → LP/MILP → MPC → RL | MILP com horizonte; MPC re-resolve; RL p/ adaptativo |
| 04.2.2 | Otimização/scheduling | Horizonte & cadência | Planeja 24–48h, re-otimiza 15min | Janela rolante (receding horizon) |
| 04.3.1 | Aprendizado | Adaptação ao usuário | Aprende padrões sem update manual | Modelo online re-treina com dados do site |
| 04.3.2 | Aprendizado | Detecção de anomalia | Falha, degradação, desvio | Baseline esperado vs. medido dispara alerta |
| 04.3.3 | Aprendizado | NILM | Desagregação não-intrusiva | ML sobre curva agregada identifica assinatura de aparelho |
| ★04.4.1 | Locus de compute | Arquitetura | Nuvem pura · edge puro · híbrido | Controle crítico no edge; otimização/treino na nuvem; sincronizam o plano |
| ★04.4.2 | Locus de compute | Resiliência | Controle ótimo sobrevive à queda da nuvem | Device guarda plano/política + fallback; opera offline e ressincroniza |

## 05 · Despacho Externo & Flexibilidade / VPP
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 05.1.1 | Sinais de rede / DSO | Despacho da distribuidora | RCR/ripple, §14a, telecontrole/RTU, control box | Recebe sinal (ripple via DI ou control box/§14a) e aplica curtailment/limite |
| 05.1.2 | Sinais de rede / DSO | BR-equivalente | Comandos da distribuidora, corte/religamento | Interface com comando da distribuidora (futuro padrão BR) |
| ★05.2.1 | Agregação/VPP | Agregação de DER | Coordena frota como usina virtual | Plataforma despacha setpoints em massa |
| ★05.2.2 | Agregação/VPP | Papel de mercado | BSP / BRP | Qualificação junto ao operador (ONS/distribuidora no BR) |
| ★05.2.3 | Agregação/VPP | Serviços ancilares | FCR, aFRR, mFRR, reserva, tensão | Resposta a desvio de frequência (droop) ou sinal (AGC), tempo certificado |
| ★05.2.4 | Agregação/VPP | Demand response | Resposta da demanda, capacity market | Desliga/desloca cargas agregadas mediante incentivo/contrato |
| 05.3.1 | Trading/mercado | Mercados | Day-ahead, intraday, imbalance | Algoritmo de bidding posiciona flexibilidade |
| 05.3.2 | Trading/mercado | Interface comercial | Comercializadoras/tradings, direct marketing | API p/ a comercializadora que liquida |
| 05.3.3 | Trading/mercado | BR | CCEE, mercado livre (ACL), curto prazo | Integração CCEE (medição/contabilização/liquidação) + contratos ACL |
| 05.4.1 | Desligamento remoto | Curtailment remoto | Corte sob comando do operador/agregador | Escreve limite/zero no inversor; trilha de auditoria |

## 06 · Plataforma, Nuvem & Dados
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 06.1.1 | App & portal | Aplicações | App usuário, portal instalador, dashboard operador | Front-end web/mobile sobre API; visões por papel |
| 06.1.2 | App & portal | Papéis & permissões | RBAC, multi-tenant, multi-site | Tenants isolados + RBAC |
| ★06.2.1 | API & integração | API aberta | REST/GraphQL, webhooks, SDK | OpenAPI + webhooks + SDK |
| ★06.2.2 | API & integração | White-label | Marca do parceiro, multi-tenant, marketplace | Tematização por tenant + marketplace |
| ★06.2.3 | API & integração | Cloud-to-cloud | Home Assistant, Google Home, Alexa | Conectores OAuth p/ ecossistemas |
| 06.3.1 | Dados & analytics | Telemetria | Tempo real + histórico | Time-series DB (Influx/Timescale) + streaming WebSocket |
| 06.3.2 | Dados & analytics | Export & relatórios | CSV/API, relatórios automáticos | Exportação via API/CSV; relatórios agendados |
| 06.3.3 | Dados & analytics | Pipeline de ML | Data lake, treino, feature store | Data lake + pipeline que melhora com agregado da frota |
| 06.4.1 | Comissionamento & O&M | Setup | Web/app/QR, auto-config | QR abre fluxo web; auto-detecção reduz config manual |
| 06.4.2 | Comissionamento & O&M | Diagnóstico remoto | Troubleshooting, alarmes, RMA | Logs/telemetria remotos + acesso remoto; fluxo de RMA |
| 06.4.3 | Comissionamento & O&M | Fleet management | Frota em escala, atualização em massa | Console aplica config/firmware em lote, rollout em ondas |
| 06.5.1 | Monetização | Modelos de receita | Assinatura, licença, white-label, revenue-share, freemium | Cobrança por device/seat, licença, ou revenue-share da flexibilidade |

## 07 · Conformidade, Segurança & Mercado
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| ★07.1.1 | Conformidade grid-code | Internacional | CE, EN 18031, IEC 62368, grid codes | Ensaios EMC/segurança em lab acreditado |
| ★07.1.2 | Conformidade grid-code | Brasil | ANEEL/PRODIST, INMETRO, homologação de distribuidora, NBR | Homologação INMETRO da medição + PRODIST + distribuidora |
| 07.2.1 | Certificação metrológica | Faturamento | Selo metrológico p/ medição faturável | Aprovação de modelo INMETRO + verificação inicial/periódica |
| 07.3.1 | Segurança/cyber | Proteção de dados | TLS, encriptação em repouso, LGPD/GDPR | TLS + encriptação; LGPD |
| 07.3.2 | Segurança/cyber | Hardening | Assinatura de firmware, pen-test, NIS2, BSI TR-03109 | Secure boot + firmware assinado + pen-testing + gestão de vulnerabilidades |
| 07.4.1 | Mercados homologados | Geografias | Onde é certificado e opera | Matriz de certificações por país/distribuidora |

## 08 · Hardware & Forma
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 08.1.1 | Forma & instalação | Formato | Gateway DIN-rail, medidor, módulo, plug | SKU por papel |
| 08.1.2 | Forma & instalação | Montagem | Trilho DIN, parede, mesa | DIN 35mm ou parede; compacto p/ QDC |
| 08.2.1 | Robustez ambiental | Proteção | IP20 (indoor) → IP65 (outdoor abrigado) | Gabinete vedado IP65 p/ externo |
| 08.2.2 | Robustez ambiental | Faixa térmica & consumo | -30~+70°C, <5–7W | Componentes grau industrial, baixo consumo (sem ventilação ativa) |
| 08.3.1 | Interface local | Display & indicadores | TFT / LED bar / e-paper, botões | Display mostra estado e QR; LED/RGB status; botões |

## 09 · UX & Conveniência
| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| ★09.1.1 | Onboarding sem fricção | Instalação | Sem app (web/QR), auto-detecção, plug-and-play | Comissionamento pelo navegador + auto-detecção; minutos |
| 09.2.1 | Operação autônoma | Autopilot | Otimiza sozinho | Modo padrão aplica a melhor estratégia |
| 09.3.1 | Engajamento | Visualização de valor | Economia em R$, CO₂, gamificação | Dashboard traduz kWh em R$/CO₂; metas/streaks |
| 09.3.2 | Engajamento | Copilot / linguagem natural | Pergunta e comanda em NL | LLM sobre dados e controles |
| 09.4.1 | Multi-residência | Multi-site | Vários imóveis/clientes em uma conta | Visão consolidada |

---

## C&I · Comercial & Industrial *(módulo acoplável)*

| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| C&I.1.1 | Medição & submedição em escala | Multi-ponto | Dezenas de pontos/circuitos, rateio por centro de custo | Rede de submedidores Modbus/RS485 mapeados a centros de custo |
| C&I.1.2 | Medição & submedição | Qualidade de energia C&I | Harmônicos, FP por ponto, registro de eventos | Analisador de qualidade por ponto |
| C&I.2.1 | Gestão de demanda contratada | Demanda BR | Demanda contratada, ultrapassagem, otimização | Monitora demanda vs. contratada; evita ultrapassagem (multa) |
| C&I.2.2 | Gestão de demanda | Correção de FP em escala | Banco de capacitores, reativo industrial | Controlador chaveia estágios p/ FP ≥ 0,92 |
| C&I.3.1 | Portfólio & multi-site | Energy management de portfólio | Múltiplas plantas, benchmarking, metas | Consolida plantas; benchmarking entre sites |
| C&I.3.2 | Portfólio & multi-site | Integração SCADA/BMS | Building Management System | Modbus/BACnet/IEC conectam ao BMS/SCADA |
| C&I.4.1 | Mercado livre (ACL) | Gestão de portfólio de energia | Contratos ACL, sazonalização, flexibilidade, CCEE | Modela contratos ACL + contabilização CCEE |
| C&I.4.2 | Mercado livre (ACL) | Geração distribuída C&I | Autoprodução, consórcio, geração compartilhada | Rateio de créditos entre unidades |

---

## 2030 · Horizonte — a fronteira

| # | Capacidade | Sub-feature | O que é | Como é feito |
|---|---|---|---|---|
| 2030.1.1 | Operação AI-native | Agent-fabric | Agentes autônomos por persona operando o sistema | Agentes LLM por persona, com ferramentas que leem/escrevem ativos/mercados sob políticas |
| 2030.1.2 | Operação AI-native | Linguagem natural end-to-end | Configurar, diagnosticar, despachar por conversa | Copilot traduz intenção em ações |
| 2030.2.1 | Mercados emergentes | P2P energy trading | Negociação peer-to-peer | Plataforma casa ofertas entre prosumidores (quando houver base legal BR) |
| 2030.2.2 | Mercados emergentes | Transactive energy | Liquidação automática, settlement programável/blockchain | Settlement automático entre agentes |
| 2030.2.3 | Mercados emergentes | CCEE-nativo + liquidação automática | Integração e liquidação no mercado livre sem intermediário | Integração direta com medição/contabilização/liquidação CCEE |
| 2030.3.1 | Controle de rede avançado | Dynamic Operating Envelopes (DOE) | Envelopes operacionais dinâmicos por nó | Recebe da distribuidora envelope de import/export variável e respeita em tempo real |
| 2030.3.2 | Controle de rede avançado | Grid-forming orchestration | Coordenação de inversores formadores de rede | Mantém estabilidade de tensão/frequência em alta penetração FV |
| 2030.4.1 | Frota & ativos inteligentes | V2G em escala | Frota de VEs como armazenamento despachável | Agrega VEs bidirecionais respeitando rotina e SOC mínimo |
| 2030.4.2 | Frota & ativos inteligentes | Digital twin em tempo real | Gêmeo digital p/ simulação e controle | Réplica simula "e se?" e otimiza antes de atuar |
| 2030.4.3 | Frota & ativos inteligentes | Manutenção preditiva em frota | ML prevê falha antes de ocorrer | ML sobre telemetria detecta assinatura de falha iminente |

---

*Mapa de especificações montado com engenharia de energia (EMS/HEMS/VPP/DER) + os 11 players pesquisados. A coluna **Como** é nível-arquitetural, não datasheet. Projeto EOS-DENO · v2.*
