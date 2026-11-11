# Extração técnica — Home Pessoa / Figma v3

**Fonte**: Figma `guivos.com 2.0`; frame desktop `16152:941`; 1440 × 10129 px.

## Mapeamento exato dos frames
- `16152:942`: Header; 1440 × 97.
- `16152:943`: M01 Hero; y97, 1440 × 816.
- `16152:964`: M02/M03 Possibilidades Reais + Amplitude; y913, 1440 × 1501.
- `16152:1020`: M04/M05 Desconexão → Conexão; y2414, 1440 × 884.
- `16152:1051`: M06/M07 Possibilidade → Experiência + Pertencimento; y3298, 1440 × 1766.
- `16152:1095`: M08 Ecossistema; y5064, 1440 × 1090.
- `16152:1136`: M09/M10 Depoimentos + Autonomia; y6154, 1440 × 1755.
- `16152:1195`: Assinatura global; y7909, 1440 × 252.
- `16152:1197`: M11 Oportunidades em Movimento; y8161, 1440 × 1137.
- `16152:1202`: Pré-rodapé; y9298, 1440 × 74.
- `16152:1205`: Rodapé; y9372, 1440 × 757.

## Conteúdo/interações de alta fidelidade, derivados dos nós
- M01: três imagens de mídia `16152:951`–`953` com chips sobrepostos; título **O que se torna possível quando você entra aqui?** e CTA **Explore possibilidades**. Preservar imagens provisórias.
- M02/M03: cinco cartões de histórias em vídeo vertical (aprendizagem, saúde/bem-estar, contribuição, empreendedorismo, pertencimento), slider e carrossel de fotos. Placeholders autorizados presentes no Figma devem permanecer literalmente.
- M04/M05: dois campos visuais lado a lado, dispersão e conexão com seis oportunidades e hub “Você”; preservar posições e linhas/vetores originais.
- M06/M07: timeline de cinco etapas (Contexto, Possibilidade, Escolha, Experiência, E depois?); anotação Figma sugere mostrar acontecimentos correspondentes ao hover e informa que a história real ainda será definida. Há vídeo/arte central e cards de participantes.
- M08: painel Journey + entradas Mall, Travel, Business, Media, Ads e faixa Intelligence. Anotação autoral: no hover das entradas, trocar imagem no painel da esquerda para o tema do produto.
- M09/M10: quatro cartões de depoimentos e slider; bloco de autonomia com quatro itens e mosaico de sete imagens.
- Assinatura: texto **Possibility, lived.**
- M11: gráfico de área, marcador agora, tooltip e contadores **3.482**, **+ 412**, **− 287**. Anotação afirma que são valores **ilustrativos** e somente dados reais, com origem/definição/período, podem ir para produção.
- Rodapé: logo, colunas de navegação, newsletter, redes sociais e outros ativos Figma. Preservar a composição e o conteúdo exatos.

## Restrições obrigatórias
1. O Figma é a verdade visual para cada propriedade renderizada. Nomes das camadas não se sobrepõem às propriedades CSS: há Goldplay e Outfit misturados no design.
2. Não substituir imagens por similares nem converter vídeo em peça genérica; arquivos originais SVG/PNG devem ser baixados e armazenados localmente antes do deploy.
3. Não usar URL temporária de asset Figma em execução.
4. Não acrescentar textos, chamadas, ícones ou navegação e não remover placeholders presentes no frame.
5. Responsividade deve ser derivada da variante Figma específica, não inventada.
6. Em largura 1440, conferir *pixel a pixel* via capturas de referência e screenshot da implementação; registrar diferenças e corrigi-las.
7. Não publicar, alterar o Figma, mesclar em main ou afirmar 100% sem auditoria visual e funcional comprovada.

## Situação
Extração de estrutura e componentes de todos os movimentos executada. Código da Home ainda não validado nem publicado. A implementação fica restrita à branch `implementation/home-pessoa-figma-v3`.
