---
title: Cards de Oportunidades de Coletivos — Padrão Neutro Institucional
version: 0.3.0
status: proposed
decision_date: 2026-10-19
area: Experiência, Design System e Oportunidades
scope: Coletivos
---

# Cards de Oportunidades de Coletivos — Padrão Neutro Institucional

## 1. Decisão aprovada em conceito

O padrão visual dos **cards de oportunidades publicadas por Coletivos** da Guivos é **neutro**, sem personalização cromática por marca do Coletivo e sem codificação de cores por área de atuação. Esta diretriz se aplica a listagens, resultados de descoberta, vitrines, cards resumidos e demais reutilizações do mesmo componente nas superfícies do ecossistema.

A opção foi escolhida expressamente em 2026-10-19 entre: (a) card neutro, (b) contorno na cor particular da marca do Coletivo e (c) contorno na cor da área de atuação. A alternativa adotada é **(a)**. Não implementar as alternativas (b) e (c) por padrão.

A decisão sobre cards **não altera** o reconhecimento visual institucional de Coletivos pela cor **Gray 4 #A1A1A1**, que substitui o antigo rosa nas superfícies dos Coletivos. Cores antigas Pink 1–4 deixam de ter função como acento de Coletivo nos componentes abrangidos por esta decisão. A aplicação global dessa mudança de identidade em todo o GKR deve ser conciliada por revisão própria de tokens existentes.

## 2. Tokens e regras visuais

| Propriedade | Valor / regra | Nota |
|---|---|---|
| Fundo do card | White `#FFFFFF` | Sem preenchimento da cor do Coletivo, da marca ou da categoria |
| Borda estrutural | Gray 3 `#E3E3E3` | Fina, discreta, uniforme; alinhar a PR #702 |
| Alternativa para divisórias/fundos auxiliares | Gray 2 `#F3F3F3`, Gray 1 `#F9F9F9` | Somente onde necessário |
| Identidade do tipo de participante | Gray 4 `#A1A1A1` | Em elementos acessórios não essenciais; não colorir todo o card |
| Texto principal e informação essencial | Black 1 `#292929` ou Black 2 `#232323` | Contraste e hierarquia; evitar Gray 4 em texto pequeno essencial |
| Tipografia | Goldplay 400 / 500 / 600 | Conforme padrões institucionais e disponibilidade/licenciamento |
| Botão principal | Preto, conforme padrão Guivos | Não variar por Coletivo ou categoria |
| Feedback de interação | Foco perceptível e acessível conforme sistema | Não depender apenas de cor ou borda cinza clara |
| Imagens | Imagem própria da oportunidade, conforme autorização e política de mídia | Imagem não determina cor da moldura |
| Etiquetas | Descritivas, em linguagem clara | Não atribuir cores por área de atuação |

**Regra absoluta:** os cards de oportunidades de Coletivos não recebem borda colorida na cor particular da marca e não recebem contorno colorido específico de Saúde, Esporte, Finanças, Educação ou qualquer outra área.

Usar componentes e tokens semânticos (ex.: `opportunityCard.surface`, `opportunityCard.border`, `participant.collective.accent`) em vez de estilos isolados por cada tela.

## 3. Identificação da origem e da área

A identidade do Coletivo será transmitida por **nome do Coletivo**, referência textual a **Coletivo** e, quando pertinente, logotipo ou imagem autorizada, sem alterar a borda/estrutura por cor de marca.

A área de atuação deve ser distinguida por **rótulo textual**, ícone semanticamente adequado e, quando útil, classificação/filtro. Exemplos: `Esporte`, `Saúde`, `Bem-estar`, `Educação`, `Finanças`. Não impor uma relação de uma cor para cada área.

Uma oportunidade pode ter múltiplas áreas compatíveis: uma pedalada pode aparecer em **Esporte** e **Bem-estar** sem obrigação de escolher uma cor predominante. A taxonomia de áreas e suas regras de classificação pertencem ao contrato funcional de oportunidades, não à decoração cromática do card.

## 4. Informações e composição do card

Card deve priorizar, quando disponíveis e aplicáveis, imagem; título objetivo da oportunidade; identificação do Coletivo responsável; localidade ou formato; data ou período; gratuidade ou valor; disponibilidade/inscrições; e ação principal contextual. Não inventar pontos, valores, classificações, avaliações, disponibilidade ou selos que não existam no modelo funcional.

Manter informações secundárias hierarquizadas e evitar excesso de etiquetas ou ícones. Selos institucionais **Verificado** e **Contribuição Reconhecida**, quando legitimamente concedidos, são independentes da cor da categoria e devem aparecer de modo contextual, sem se transformarem em decoração obrigatória de todo card.

Card deve ter versão responsiva para desktop/tablet/mobile, com leitura acessível por teclado, leitor de tela e dispositivos de toque.

## 4A. Referências normativas de layout — anexos originais do usuário

**Referências exclusivamente dos anexos enviados em 2026-10-19:** `Card Vertical.pdf` (página 1) e `Card horizontal.pdf` (página 1). **Não substituir esses desenhos por fotografias, imagens de busca, exemplificações genéricas de e-commerce nem outro template.** Uma descrição genérica anterior foi considerada incorreta e fica substituída por esta leitura fiel.

### Card Vertical.pdf — página 1 (três cards verticais lado a lado)

O PDF mostra uma **fileira de três cards** com a mesma estrutura em orientação vertical. Em cada card:

1. **Grande área de imagem na parte superior**, de cantos arredondados, com placeholder quadriculado no arquivo. Não consta imagem fotográfica nesse PDF.
2. **Linha de indicadores e ações imediatamente abaixo da imagem:** selo contornado `15% off` verde, selo contornado `Recomendado` violeta; à direita, ícones de coração rosa, cesta cinza e compartilhamento ciano.
3. **Aviso pequeno `Últimas unidades`**, em verde e sublinhado, na linha seguinte, alinhado à esquerda.
4. **Título `Descrição do Produto`** à esquerda; no mesmo alinhamento, pequena estrela amarela e avaliação `4,8` à direita.
5. **`Subdescrição`** cinza abaixo do título.
6. **Linha de três atributos**: `Item 01`, `Item 02`, `Item 03`, cada um com pequeno ícone circular claro.
7. **Separador horizontal claro** antes do rodapé.
8. **Rodapé de valores:** texto `a partir de` acima; indicação do preço anterior `0.000 pts` riscada, preço principal `00.000 pts` e unidade `p/pessoa`.
9. **Ação circular com seta diagonal no canto inferior direito**, em cinza muito claro em dois exemplos e em roxo no terceiro; o terceiro também tem destaque/sombra visual.

Preservar a sequência, os alinhamentos, a hierarquia e a posição dos elementos na tradução para cards de oportunidade. Os três exemplares são exemplos visuais do mesmo componente, **não três tipos de cadastro ou entidades**.

### Card horizontal.pdf — página 1 (dois cards horizontais empilhados)

O PDF mostra **dois cards largos, um embaixo do outro**, cada um com:

1. **Grande imagem/placeholder quadriculado à esquerda**, ocupando aproximadamente um terço da largura; conteúdo ocupando os dois terços restantes à direita.
2. Na primeira linha do conteúdo à direita, **etiquetas `15% off` e `Recomendado` à esquerda** e **ícones coração rosa, cesta cinza e compartilhar ciano no canto superior direito**.
3. **Título `Descrição do Produto`**, com estrela amarela e nota `4,8` à direita.
4. **`Subdescrição`** e depois uma **linha com `Item 01`, `Item 02`, `Item 03`**.
5. **`Últimas unidades`** aparece **depois** da linha dos atributos (diferentemente do card vertical, onde está antes do título).
6. **Divisória longa** separando o conteúdo principal do rodapé.
7. Rodapé com **`a partir de`**, antigo `0.000 pts` riscado, `00.000 pts` e `p/pessoa`; **seta circular no extremo inferior direito**.
8. Na variação inferior o **botão circular é roxo**, enquanto na superior ele é cinza-claro; os dois exemplos representam tratamentos/estados visuais do mesmo card.

**Diferença de orientação é estrutural e inclui mudança de posição de `Últimas unidades`**. Não padronizar arbitrariamente a sequência ignorando os anexos. As proporções exatas devem ser aferidas no original antes de implementação, e não inferidas de imagens externas.

### Transferência para oportunidades de Coletivos — limites explícitos

Aprova-se a **mesma composição de Travel/Mall**, com versão vertical e horizontal, mantendo cards neutros: White `#FFFFFF`, estrutura/borda sutil Gray 3 `#E3E3E3`, sem contorno por marca ou categoria e sem fundo rosa/Gray4 obrigatório. **Neutralidade do card não exige tornar monocromáticos os elementos funcionais ilustrados nos arquivos**; a eventual adoção de selos, estados ou ícones coloridos deve seguir regra e tokens institucionais aplicáveis, após validação, e não representar cores de Coletivos.

| Elemento no arquivo | Interpretação funcional na Guivos |
|---|---|
| `Descrição do Produto` / `Subdescrição` | Título e descrição curta da oportunidade |
| Placeholder quadriculado | Área de imagem da oportunidade, sem pressupor imagem real no PDF |
| `15% off` | Desconto **somente se aplicável e comprovado**; não atribuir desconto inexistente |
| `Recomendado` | Recomendação **somente se existir lógica válida e auditável** |
| Coração, cesta e compartilhamento | Manter posição de referência; implementar só ações pertinentes e existentes, especialmente evitar cesta/carrinho sem fluxo de compra |
| `Últimas unidades` | Eventual disponibilidade de vagas, apenas com capacidade verificável; adaptar nomenclatura para oportunidade |
| Estrela e nota `4,8` | Exibir avaliação somente se a Guivos possuir sistema válido de avaliações para essa oportunidade |
| `Item 01 / 02 / 03` | Atributos verificáveis da oportunidade, conforme modelo funcional |
| `0.000 pts`, `00.000 pts`, `p/pessoa` | Placeholder do PDF; preço, gratuidade e pontos obedecem a regras próprias, sem obrigatoriedade de operação integral em pontos |
| Setas circulares cinza-claro/roxo | Tratamentos visuais do PDF, **não estados funcionais definidos**; adaptar funcionalidade/contraste após validação de UX |

**Critério de aceitação:** qualquer especificação, protótipo ou implementação desses cards deve ser comparada diretamente com ambas as páginas dos anexos originais, incluindo imagem, posição dos ícones, posição distinta de disponibilidade no vertical versus horizontal, título/nota, separadores e área inferior de valores/CTA. Não aceitar imagens genéricas como representação desses modelos.

## 5. Hierarquia cromática do ecossistema

- **Pessoas:** preservam identidade roxa da Guivos.
- **Organizações:** preservam sua identidade Purple 4 `#5D34A9`.
- **Coletivos:** identidade institucional Gray 4 `#A1A1A1` nas superfícies próprias, observadas as regras de contraste.
- **Cards de oportunidades de Coletivos:** mantêm-se **neutros e brancos**, com borda Gray 3; não herdam borda Gray 4 obrigatória, nem qualquer rosa anterior.
- A neutralidade dos cards não significa remover imagens, conteúdo visual ou indicadores de status legítimos; significa **não vincular a identidade do card à cor particular da marca ou à área**.

## 6. Interações, acessibilidade e exceções

Estados `hover`, `selected`, `focus-visible`, `disabled` e `loading` seguem tokens globais de interface; não devem introduzir coloração por marca do Coletivo ou por categoria. O foco precisa ser claramente perceptível. Gray 4 sobre branco não deve sustentar sozinho significado crítico; usar textos Black 1/Black 2 e outros sinais acessíveis quando necessário.

Cores funcionais (por exemplo, sucesso, alerta, erro) só podem aparecer quando exigidas por uma regra de estado da interface, usando a paleta institucional e não como identidade permanente da oportunidade. Promoções, descontos, níveis de plano e pontos obedecem às respectivas especificações de produto e não autorizam colorir a borda por marca/categoria.

Uma eventual exceção cromática deverá ser **proposta formalmente, justificada e versionada no GKR**, após análise de acessibilidade, consistência e escalabilidade. Não há exceção de cor da marca aprovada neste documento.

## 7. Governança e validação

1. Registrar este documento em **Experiência / Design System / Cards de Oportunidades de Coletivos**, com entrada no MENU do GKR após a incorporação.
2. Harmonizar a regra com a especificação dos **componentes de oportunidades**, a política de paleta e o novo token institucional de Coletivos Gray 4; não redefinir a identidade de Organizações e Pessoas.
3. Auditar componentes compartilhados nas vitrines e demais superfícies para impedir que estilos de Coletivo afetem oportunidades publicadas por Organizações.
4. Validar telas de card em repouso, hover, foco, ação, mobile e acessibilidade; verificar exemplos multitemáticos, com imagem e sem imagem.
5. Implementação em Replit e publicação só após decisão de escopo e autorização específica; **esta especificação não executa alterações nos aplicativos**.

## 8. Registro de alternativas rejeitadas

- **Contorno na cor escolhida pelo Coletivo:** rejeitado como padrão atual porque introduz ampla variabilidade cromática, conflito com a paleta oficial e risco de ruído visual no catálogo.
- **Contorno por área:** rejeitado porque transfere taxonomia funcional para um código de cores difícil de manter, inclusive em oportunidades com múltiplas áreas.
- **Neutro:** adotado porque preserva consistência, legibilidade, comparabilidade e escalabilidade entre participantes.

### Estado da decisão

**Decisão de produto:** aprovada no diálogo em 2026-10-19.

**Estado documental:** proposta em PR, aguardando revisão/merge e inclusão no MENU para integrar o GKR publicado.

**Estado técnico:** nenhum app alterado por este registro.
