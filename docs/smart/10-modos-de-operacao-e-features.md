# 10 — Catálogo de Modos de Operação e Features

> Catálogo completo do que o Smart faz, com a **classificação obrigatória por camada** (`[SW]` só software · `[SW+HW]` software+hardware · `[HW]` só hardware/edge · `[AMBOS]` app ou hardware) e **qual camada executa e por quê**. Cada modo aponta os ativos exigidos, dependências regulatórias ([02](02-contexto-regulatorio-mercado-br.md)) e os cenários onde se aplica ([11](11-matriz-de-cenarios.md)).

---

## Tabela-resumo

| # | Modo / Feature | Camada | Executa em | Ativos mínimos |
|---|---|---|---|---|
| 1 | Monitoramento / telemetria | `[SW]` / `[AMBOS]` | nuvem (edge opcional) | qualquer |
| 2 | Autoconsumo (self-consumption) | `[HW]` | edge | PV + (bateria) |
| 3 | Backup / UPS / ilhamento intencional | `[HW]` | edge + inversor híbrido | bateria + híbrido |
| 4 | Peak shaving / limite de demanda | `[HW]` | edge (CT) | medição + carga/bateria |
| 5 | Zero-export / limite de injeção | `[HW]` | edge | PV + medição |
| 6 | Load shifting (branca/ToU/dinâmica) | `[AMBOS]` | plano nuvem, executa edge | carga controlável / bateria |
| 7 | Otimização por preço + forecast | `[SW+HW]` | nuvem planeja, edge executa | bateria/cargas |
| 8 | EV smart charging (V1G) | `[SW+HW]` | edge modula | EV charger |
| 9 | V2H / V2G | `[SW+HW]` | edge + inversor bidirecional | EV bidirecional `[VERIFICAR]` |
| 10 | Bomba de calor (SG-Ready) | `[SW+HW]` | edge | bomba SG-Ready |
| 11 | Gestão de cargas (plug/relé) | `[AMBOS]` | edge/app | smart plug/relé |
| 12 | Scheduling / cenas / automações | `[AMBOS]` | edge executa | qualquer controlável |
| 13 | Grid services / VPP | `[SW+HW]` | nuvem agrega, edge despacha | flexibilidade + medição |
| 14 | Controle de reativo / fator de potência | `[HW]` | edge + inversor | inversor |
| 15 | Curtailment por ordem (estilo §14a) | `[SW+HW]` | nuvem sinaliza, edge limita | inversor/cargas |
| 16 | Rateio / gestão de GD compartilhada | `[SW]` | nuvem | medição por UC |
| 17 | Comissionamento / config remota | `[SW]` + `[HW]` | app/nuvem → edge | qualquer |
| 18 | OTA (dispositivo e frota) | `[SW+HW]` | nuvem → edge | hardware/ativo |
| 19 | Diagnóstico IV / AI Health / consistência bateria | `[SW]` | nuvem | inversor/bateria |

---

## Fichas detalhadas

### 1. Monitoramento / telemetria `[SW]`/`[AMBOS]`
- **Descrição:** coleta e visualização de geração, consumo, fluxo, SoC, alarmes.
- **Camada/por quê:** funciona só pela nuvem (conector cloud) **ou** com edge (telemetria local mais rica/rápida).
- **Cenários:** todos (inclusive N0). **Regulatório:** nenhum específico.

### 2. Autoconsumo `[HW]`
- **Descrição:** prioriza usar a geração PV na própria casa, carregando bateria com excedente.
- **Por quê edge:** malha rápida PV↔carga↔bateria que **não pode depender de nuvem**.
- **Ativos:** PV (+bateria para armazenar excedente). **Cenários:** N1+.

### 3. Backup / UPS / ilhamento intencional `[HW]`
- **Descrição:** na falta de rede, alimenta cargas essenciais a partir de bateria/PV (ilhamento **intencional**).
- **Por quê edge:** transição imediata, local; coordena **transferência** ([06](06-especificacao-hardware.md) Controller) respeitando **anti-ilhamento** do inversor ([02](02-contexto-regulatorio-mercado-br.md)).
- **Ativos:** bateria + inversor híbrido. **Cenários:** N2+.

### 4. Peak shaving / limite de demanda `[HW]`
- **Descrição:** evita ultrapassar um limite de potência/demanda, descarregando bateria ou cortando carga.
- **Por quê edge:** exige **medir e atuar em segundos** (CT no Controller).
- **Regulatório:** relevante onde há **demanda contratada**/custo de ponta. **Cenários:** N2+/N4+.

### 5. Zero-export / limite de injeção `[HW]`
- **Descrição:** limita ou zera a injeção na rede conforme regra/parecer de acesso.
- **Por quê edge:** resposta rápida para **não violar** limite (PRODIST/parecer). **Ativos:** PV + medição. **Cenários:** N1+.

### 6. Load shifting (tarifa branca/ToU/dinâmica) `[AMBOS]`
- **Descrição:** desloca consumo/carga de bateria para horários baratos (fora-ponta/preço baixo) e evita ponta/preço alto.
- **Por quê:** o **plano** vem da nuvem (tarifa/forecast), a **execução** é local (agenda no edge).
- **Regulatório:** depende de **tarifa branca/bandeiras** (cativo) ou **preço de mercado** (livre) — ver [02](02-contexto-regulatorio-mercado-br.md). **Cenários:** N4+.

### 7. Otimização por preço + forecast `[SW+HW]`
- **Descrição:** otimização multivariável (PV, carga, preço, SoC, conforto) minimizando custo/maximizando receita.
- **Por quê:** cálculo pesado na nuvem ([08](08-plataforma-cloud-e-apis.md)); execução e fallback no edge. **Cenários:** N4+, ambos os mundos de preço.

### 8. EV smart charging (V1G) `[SW+HW]`
- **Descrição:** modula a corrente de carga do VE conforme excedente PV, preço e limite da casa.
- **Por quê:** modulação em tempo real no edge (OCPP), planejada na nuvem. **Ativos:** EV charger (OCPP). **Cenários:** N3+.

### 9. V2H / V2G `[SW+HW]`
- **Descrição:** usa a bateria do VE para alimentar a casa (V2H) ou a rede (V2G).
- **Por quê/limites:** exige **hardware bidirecional** e **regulação** que ainda evolui no Brasil — `[VERIFICAR viabilidade regulatória/comercial BR]`. **Cenários:** N3+/N5 (futuro).

### 10. Bomba de calor (SG-Ready) `[SW+HW]`
- **Descrição:** modula aquecimento/água conforme excedente PV e preço (4 estados SG-Ready).
- **Por quê:** sinal SG-Ready/EEBus aplicado no edge. **Cenários:** N4+ (onde houver bomba).

### 11. Gestão de cargas (smart plug/relé) `[AMBOS]`
- **Descrição:** mede e chaveia cargas comuns (boiler, piscina, ar-condicionado) por prioridade.
- **Por quê:** automações executadas no edge; comando manual pelo app. **Cenários:** N4+.

### 12. Scheduling / cenas / automações `[AMBOS]`
- **Descrição:** regras gatilho→ação (horário, preço, SoC, excedente, presença, VE conectado).
- **Por quê:** definidas no app/nuvem, **executadas no edge** (seguem offline). **Cenários:** N3+.

### 13. Grid services / VPP `[SW+HW]`
- **Descrição:** agrega flexibilidade de muitas UCs e despacha para serviços de rede/mercado.
- **Por quê:** nuvem agrega/otimiza ([08](08-plataforma-cloud-e-apis.md)); edge executa com garantias locais.
- **Regulatório:** monetização **gradual** no Brasil — capacidade pronta, receita conforme regulação ([02](02-contexto-regulatorio-mercado-br.md)). **Cenários:** N5.

### 14. Controle de reativo / fator de potência `[HW]`
- **Descrição:** ajusta reativo/FP via inversor conforme requisito da distribuidora.
- **Por quê:** malha rápida local junto ao inversor. **Cenários:** N1+/N5.

### 15. Curtailment por ordem (estilo §14a) `[SW+HW]`
- **Descrição:** limita potência de geração/carga ao receber ordem da distribuidora (análogo BR ao §14a alemão citado nas fontes).
- **Por quê:** sinal pela nuvem, **limitação garantida no edge**. **Cenários:** N5 (e N1+ para limite de injeção).

### 16. Rateio / gestão de GD compartilhada `[SW]`
- **Descrição:** conciliação geração×consumo e **rateio de créditos** entre UCs (Lei 14.300).
- **Por quê:** puramente de dados/billing na nuvem ([08](08-plataforma-cloud-e-apis.md)). **Cenários:** arranjo **B** (todos os níveis).

### 17. Comissionamento / config remota `[SW]`+`[HW]`
- **Descrição:** descoberta de ativos (one-click scan), configuração de parâmetros (modo, conexão à rede, segurança, bateria), em lote.
- **Por quê:** orquestrado pela nuvem/app, aplicado no edge/conector. **Cenários:** todos com hardware/ativo.

### 18. OTA (dispositivo e frota) `[SW+HW]`
- **Descrição:** atualização de firmware do hardware Smart e dos ativos, individual e em lote, com retomada automática.
- **Por quê:** orquestração na nuvem, aplicação A/B no edge ([07](07-especificacao-firmware-edge.md)). **Cenários:** todos.

### 19. Diagnóstico IV / AI Health / consistência de bateria `[SW]`
- **Descrição:** diagnóstico por curva I-V, saúde multidimensional e consistência de baterias (herdados do SEMS, agora multimarca).
- **Por quê:** análise de dados/IA na nuvem. **Cenários:** N1+ (PV) / N2+ (bateria).

---

> A combinação destes modos por cenário (quais ligam em cada célula da grade) está em [11 — Matriz de Cenários](11-matriz-de-cenarios.md).
