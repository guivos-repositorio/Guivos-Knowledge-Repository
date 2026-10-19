---
title: Cards de Oportunidades de Coletivos — Padrão Neutro Institucional
version: 0.2.0
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

## 4A. Referências visuais formais: Travel e Mall (arquivos fornecidos)

Em 2026-10-19, foram fornecidos os arquivos de referência **Card Vertical.pdf** e **Card horizontal.pdf** (uma página cada). Ambos passam a definir a **estrutura de composição e a família visual** dos cards de oportunidades de Coletivos. Os arquivos são **referências visuais**, não contratos de negócios; seus textos e valores são placeholders e não podem ser copiados como dados de oportunidades reais.

### Versão vertical — Card Vertical.pdf, página 1

- Cartão com imagem ampla na parte superior e corpo de informações imediatamente abaixo, contorno leve e cantos arredondados.
- A área de imagem ocupa uma proporção relevante do conjunto; quando houver múltiplas imagens, usar o padrão de navegação visual existente, sem recriar um novo carrossel.
- Faixa de ações/indicadores abaixo da imagem com espaço para etiquetas (no exemplo: `15% off`, `Recomendado`) e ícones de interação (favoritar, compartilhar e outras ações ilustrativas).
- Em seguida: aviso contextual breve (`Últimas unidades` no exemplo), título, avaliação quando houver avaliação **real e autorizada**, descrição/subdescrição e atributos curtos.
- Separador sutil entre informações e rodapé; bloco inferior com condição comercial/participação e CTA, cujo estado visual pode variar por disponibilidade, sempre respeitando a regra de botões e acessibilidade da superfície.
- Os três cartões justapostos na referência representam variantes do mesmo componente, não três modelos distintos de entidade.

### Versão horizontal — Card horizontal.pdf, página 1

- Cartão retangular alongado com **imagem à esquerda** e **conteúdo à direita**; contorno e raio coerentes com o vertical.
- No topo do conteúdo: etiquetas de contexto e ações secundárias à direita.
- Título, avaliação condicional, descrição curta, atributos e aviso contextual dispostos em hierarquia vertical.
- Rodapé separado por linha leve, contendo eventual valor/condição de participação e CTA alinhado ao extremo direito.
- As duas exemplificações horizontais representam estados do mesmo card; não impõem a cor do CTA demonstrado.
- Em telas estreitas, permitir migração da versão horizontal para a composição vertical, preservando conteúdo, sem corte ou scroll horizontal desnecessário.

### O que é preservado e o que é adaptado

| Elemento dos PDFs | Aplicação nas oportunidades de Coletivos |
|---|---|
| Estrutura de imagem, título, informações, divisória e rodapé | **Preservar** como referência de composição |
| Família visual de borda, cantos e espaçamentos | **Preservar** e adequar aos tokens oficiais Guivos |
| Etiquetas e ações de favoritar/compartilhar | **Condicionais** à funcionalidade efetivamente existente |
| `15% off`, `Recomendado`, `Últimas unidades` | **Não exibir automaticamente**; usar apenas com regras verificáveis de desconto, recomendação e disponibilidade/capacidade |
| `Descrição do Produto` e `Subdescrição` | Substituir por título e descrição objetiva da **oportunidade** |
| `Item 01 / Item 02 / Item 03` | Substituir por informações reais, como modalidade, região/local, data, duração ou público elegível, conforme contrato da oportunidade |
| Estrelas e nota `4,8` | Exibir somente se a Guivos dispuser de sistema de avaliações legitimamente estabelecido para o objeto avaliado |
| `0.000 pts`, `00.000 pts p/pessoa`, preço riscado | Adaptar ao preço em R$ quando pago, gratuidade quando gratuito e **pontos apenas segundo as regras específicas de oportunidades**; não converter automaticamente preço em pontos sem base |
| Ícone de lixeira/cesta e outros ícones do exemplo | **Não transportar literalmente** sem semântica funcional válida para a oportunidade |
| CTA circular com seta | Pode ser aproveitado como affordance visual se houver ação real, rótulo acessível e contraste validado; não presumir roxo como cor obrigatória para Coletivos |
| Imagens quadriculadas de placeholder | Substituir por imagem autorizada da oportunidade ou placeholder neutro institucional quando necessário |

### Regra de unidade entre orientações

Vertical e horizontal representam **o mesmo componente semântico** de oportunidade, com os mesmos dados, regras de preço, pontos, inscrições e disponibilidade. Variam apenas layout e disposição responsiva. Não duplicar modelo de negócio, permissões nem indicadores por orientação.

Não reinterpretar os arquivos como aprovação de novos descontos, pontuações, ratings, destaques, rótulos ou carrinhos: os modelos anexos ilustram visual e hierarquia; a funcionalidade continua subordinada ao GKR.

### Critérios adicionais de aceitação

- Comparar uma amostra de **card vertical** e uma de **card horizontal** lado a lado com os PDFs fornecidos, verificando hierarquia, imagem, proporções, bordas, hierarquia tipográfica, ícones, divisória e CTA.
- Conferir que nenhuma borda use cor da marca do Coletivo ou cor por área de atuação; White/Gray3 seguem como padrão.
- Verificar cards de oportunidade gratuita, paga, com/sem pontos, com/sem fotos, com/sem vagas remanescentes, além de estado sem avaliação.
- Não tratar o estilo rosa/verde/roxo/ciano dos **indicadores ilustrativos nos PDFs** como mudança de paleta institucional ou identidade de Coletivos. Status funcionais legítimos podem ter regras próprias, a validar separadamente.
- Exigir que botões e ícones interativos tenham estados funcionais, acessibilidade por teclado e toque e não sejam elementos decorativos inertes.

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
