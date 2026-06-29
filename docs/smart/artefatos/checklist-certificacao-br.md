# Artefato — Checklist de Certificação e Conformidade (Brasil)

> Lista de verificação para colocar o **hardware Smart** (Gateway + Smart Meter) e o **sistema** em conformidade no Brasil. Baseado em [02](../02-contexto-regulatorio-mercado-br.md) e [06](../06-especificacao-hardware.md). Itens `[VERIFICAR]` dependem de portaria/ensaio vigente.

---

## 1. Radiofrequência — ANATEL
- [ ] Homologação ANATEL de **todo** rádio embarcado (Wi-Fi, Bluetooth, 4G/LTE). `[VERIFICAR]`
- [ ] Preferir **módulos pré-certificados** (reduz custo/tempo).
- [ ] Etiqueta/selo ANATEL no produto e na documentação.

## 2. Segurança elétrica e EMC
- [ ] Conformidade do equipamento eletroeletrônico (ABNT/NBR aplicável). `[VERIFICAR]`
- [ ] Ensaios de **compatibilidade eletromagnética (EMC)**. `[VERIFICAR]`
- [ ] Instalação conforme **NBR 5410** (instalações elétricas de BT). `[VERIFICAR]`
- [ ] Proteção contra surtos/transientes nas interfaces.

## 3. Metrologia — Smart Meter
- [ ] Exatidão **< 1% de desvio** comprovada em ensaio.
- [ ] Avaliação metrológica (INMETRO/portaria de medidores) **se** uso faturável. `[VERIFICAR classe/uso]`
- [ ] Medição **bidirecional** quando houver GD.

## 4. Inversor (não é o Gateway, mas o sistema depende)
- [ ] Inversor com certificação **INMETRO Portaria 140/2022 + 515/2023** (inclui dispositivo de desconexão de emergência).
- [ ] Inversor conforme **ABNT NBR 16149 / 16150** (interface de conexão) e **IEC 62116** (anti-ilhamento).
- [ ] O Smart **não desabilita** proteções do inversor (anti-ilhamento, limites).

## 5. Conexão da GD — PRODIST / distribuidora
- [ ] Solicitação de acesso e **parecer** conforme **PRODIST Módulo 3**.
- [ ] Respeito a **limite de injeção** / zero-export quando exigido no parecer.
- [ ] Documentação e comissionamento conforme **NBR 16274**.
- [ ] Requisitos específicos da **distribuidora** local. `[VERIFICAR por concessionária]`

## 6. EV charger (quando aplicável)
- [ ] **ABNT NBR IEC 61851** (sistema de carga condutiva) e **NBR IEC 62196** (conectores). `[VERIFICAR]`

## 7. Armazenamento (ESS)
- [ ] Normas IEC/ABNT de **segurança de baterias**; acompanhar REN/consultas ANEEL de ESS. `[VERIFICAR]`

## 8. Dados e privacidade — LGPD
- [ ] Base legal/consentimento para dados pessoais e de consumo.
- [ ] Políticas de **retenção** e titularidade dos dados.
- [ ] Segurança da informação (mTLS, criptografia, secure boot — ver [03](../03-arquitetura-de-sistema.md)/[07](../07-especificacao-firmware-edge.md)).

## 9. Mercado / comercialização (arranjos B e C)
- [ ] **GD compartilhada:** conformidade com **Lei 14.300** / **REN 1.000** (modalidade, rateio, SCEE, Fio B).
- [ ] **Mercado livre BT:** medição apta à **CCEE**; acompanhar regulamentação da **Lei 15.269/2025** (2027/2028) e do **SUI**. `[VERIFICAR]`

---

> Este checklist é um **guia**; a engenharia de certificação deve confirmar portarias e normas **vigentes na data** do projeto e por modelo de hardware.
