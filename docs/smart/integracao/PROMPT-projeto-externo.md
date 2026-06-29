# Prompt — Projeto Externo de Ingestão de Mapas (Modbus + APIs)

> Cole o conteúdo abaixo como **prompt inicial** numa sessão dedicada (outro repositório/sessão), com os documentos oficiais dos fabricantes disponíveis. O objetivo é **popular** os [templates por fabricante](00-modelo-de-abstracao.md) e a [matriz de compatibilidade](matriz-compatibilidade.md) a partir dos mapas oficiais, e depois **mesclar** o resultado de volta em `docs/smart/integracao/`.

---

## Contexto (resumo para a sessão externa)

> Estamos construindo o **Smart**, um EMS/HEMS agnóstico de marca (BT, Brasil). Precisamos de uma base de integração que ligue **registradores Modbus/SunSpec** e **campos de APIs cloud** de fabricantes às **capacidades canônicas** do produto. O vocabulário canônico (ids estáveis) está em `mapa-canonico-capacidades.md`. Os formatos de saída estão em `template-fabricante-modbus.md`, `template-fabricante-api.md` e `matriz-compatibilidade.md`.

## Entradas

- **Documentos oficiais** por fabricante: "Modbus protocol" (PDF) e/ou documentação de API. Fabricantes prioritários: **GoodWe, Deye, Sungrow, Growatt, Huawei, Solis** (depois: EV chargers, bombas, medidores).
- Ferramenta de conversão: **[markitdown](https://github.com/microsoft/markitdown)** (PDF/Office → Markdown).
- Os três arquivos de referência citados acima (canônico + templates + matriz).

## Tarefas

1. **Converter** cada documento para Markdown com `markitdown` e salvar em `fontes/`.
2. Para cada **modelo/série**, criar um arquivo a partir do template adequado:
   - Modbus/SunSpec → `fabricantes/modbus/<marca>-<serie>.md`
   - API → `fabricantes/api/<marca>.md`
3. **Mapear** cada registrador/campo nativo → **capacidade canônica** (`id`), preenchendo tipo de dado, escala, unidade, acesso (R/W) e enums.
4. Marcar **lacunas** com `[VERIFICAR]` (registrador ausente, firmware divergente, controle não permitido).
5. Atualizar a **matriz de compatibilidade** (capacidades por caminho `L`/`C`, status, fonte, data).
6. **Curar por tipo de ativo** (inversor, bateria, medidor, EV, bomba, carga), mantendo cabeçalhos consistentes.
7. Produzir um **relatório de cobertura**: o que foi mapeado, o que falta, divergências entre fabricantes.

## Regras

- **Não inventar** registradores/campos: só o que está na fonte oficial. Faltou? → `[VERIFICAR]`.
- Preservar **unidades e sinais** conforme as convenções do mapa canônico (+importa/−exporta).
- Um `id` canônico inexistente para uma função nova → **propor** novo id e listar em "sugestões ao canônico" (não alterar o canônico sozinho).
- Saída **somente em Markdown**, pronta para merge em `docs/smart/integracao/`.

## Saídas esperadas

- `fontes/*.md` (conversões)
- `fabricantes/modbus/*.md` e `fabricantes/api/*.md` preenchidos
- `matriz-compatibilidade.md` atualizada
- `relatorio-cobertura.md`
- `sugestoes-ao-canonico.md` (novos ids propostos)

## Merge de volta

1. Revisar `sugestoes-ao-canonico.md` e, se aprovado, adicionar ids ao `mapa-canonico-capacidades.md` (mantendo estabilidade).
2. Copiar `fabricantes/**` e a matriz atualizada para `docs/smart/integracao/`.
3. Commit na branch de trabalho com resumo da cobertura.

> Mesma estrutura serve para **APIs**: o conector cloud-to-cloud consome os mapas de `fabricantes/api/` exatamente como os drivers locais consomem os de `fabricantes/modbus/`.
