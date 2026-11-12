# Decisão — Tipografia exclusiva Goldplay na Home Principal / Pessoa

**Data:** 2026-11-11
**Autoridade:** instrução expressa da direção Guivos nesta conversa.
**Aplicação:** implementação web independente da Home Principal / Pessoa derivada do Figma `guivos.com 2.0` / frame `16152:941`.

## Decisão vinculante
- **Não utilizar Outfit** em nenhum elemento da implementação da Home Principal / Pessoa.
- Substituir todas as ocorrências de Outfit por **Goldplay**, usando peso correspondente quando disponível: Regular 400, Medium 500 e Semibold 600.
- Toda tipografia, inclusive header, footer, chips, cards, gráficos, formulários, botões e navegação, deve usar Goldplay.
- Preservar conteúdo, hierarquia, tamanho, cores, espaçamento, alinhamentos e comportamento do design do Figma; eventuais ajustes estritamente tipográficos necessários para conservar a geometria visual devem ser verificados e documentados.
- Essa substituição é **exceção explicitamente autorizada** à regra anterior de copiar as propriedades de fontes renderizadas no Figma. A exigência de fidelidade integral permanece para todos os outros atributos.
- Não alterar o arquivo Figma sem instrução específica. Não publicar, não fazer merge e não alterar outras aplicações.

## Precedência
Esta decisão substitui, apenas no ponto da família tipográfica Outfit, as referências anteriores em `FIGMA_BASELINE.md` e `EXTRACAO_TECNICA_V3.md` desta branch. Goldplay passa a ser a fonte obrigatória para toda a implementação.

## Validação
Auditar fontes computadas em todos os elementos e assegurar ausência de Outfit no código, nas dependências tipográficas utilizadas e na renderização final. A conformidade integral ainda depende de auditoria de screenshots e comportamentos.
