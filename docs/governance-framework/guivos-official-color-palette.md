---
id: GKR-BRAND-COLOR-PALETTE-001
title: Guivos — Paleta Oficial de Cores e Fundo Branco
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-10-11
normative: true
---

# Guivos — Paleta Oficial de Cores e Fundo Branco

## Origem

Fonte primária: **Paleta de Cores.pdf**, enviada pelo fundador em 11/10/2026, página 1, *Foundations / Colors / Cores*. O documento apresenta 30 tokens da coleção `guivos.com.br`. A regra adicional de canvas branco e exclusividade cromática foi determinada expressamente pelo fundador em 11/10/2026. A origem visual não deve ser confundida com uma autorização de produto/implementação.

## Regras obrigatórias para telas e protótipos

1. **Exclusividade:** toda cor criada para a interface (texto, fundo de componente, borda, ícone, botão, estado, legenda, série de gráfico, nó/aresta de grafo e ilustração de UI) deve pertencer exatamente aos 30 hexadecimais abaixo. Nenhuma outra tonalidade, cor derivada ou variação não listada é permitida.
2. **Fundo branco em todas as páginas:** o canvas/base de **toda tela, página ou viewport** é obrigatoriamente `White #FFFFFF`. Componentes internos podem usar outros tokens oficiais, preservando o fundo-base branco. Não adotar modo escuro ou página com fundo cinza/púrpura.
3. **Sem tonalidades inventadas:** proibir cores arbitrárias, variantes automáticas de bibliotecas, `color-mix`, `rgba`/`hsla` usados para criar novos tons, algoritmos de cor por categoria e gradientes intermediários fora da paleta; preferir bordas oficiais a sombras tingidas.
4. **Acessibilidade:** selecionar combinações com contraste adequado, foco perceptível e codificação redundante por texto/forma/padrão. Se uma combinação não for legível, substituir por outra **da própria paleta**.
5. **Gráficos e Graph Analytics:** componentes analíticos, grafos, matrizes e mapas de calor usam apenas tokens oficiais. Nunca distinguir entidades ou relações exclusivamente pela cor; aplicar legenda, texto, padrões ou formatos.
6. **Universalidade:** cumprir em protótipos atuais e futuros, incluindo Guivos Descoberta de Oportunidades e Guivos Business Dashboard no Replit. A regra cromática não altera definição, autorização, dados, contratos KPI ou liberação produtiva.
7. **Escopo de imagens:** fotografias e vídeos do mundo real preservam cores naturais; não são variantes inventadas da UI. Ícones, diagramas e ilustrações produzidos como elementos cromáticos da interface devem utilizar os tokens oficiais.

## Paleta primitiva oficial — 30 tokens

| Família | Token | Hex |
|---|---|---|
| Gray | Gray 1 | `#F9F9F9` |
| Gray | Gray 2 | `#F3F3F3` |
| Gray | Gray 3 | `#E3E3E3` |
| Gray | Gray 4 | `#A1A1A1` |
| Gray | White | `#FFFFFF` |
| Black | Black 1 | `#292929` |
| Black | Black 2 | `#232323` |
| Purple | Purple 1 | `#7D55C6` |
| Purple | Purple 2 | `#EDE9FE` |
| Purple | Purple 3 | `#B1A1E4` |
| Purple | Purple 4 | `#5D34A9` |
| Yellow | Yellow 1 | `#FDDC00` |
| Yellow | Yellow 2 | `#FFFCDD` |
| Yellow | Yellow 3 | `#FFF089` |
| Pink | Pink 1 | `#F177C5` |
| Pink | Pink 2 | `#FBE8F5` |
| Pink | Pink 3 | `#F7AADD` |
| Pink | Pink 4 | `#E84CAB` |
| Orange | Orange 1 | `#FF5600` |
| Orange | Orange 2 | `#FFEBE1` |
| Orange | Orange 3 | `#FFB996` |
| Orange | Orange 4 | `#E04D02` |
| Green | Green 1 | `#26CF7C` |
| Green | Green 2 | `#D7FFEB` |
| Green | Green 3 | `#BCF6D8` |
| Green | Green 4 | `#18A15D` |
| Blue | Blue 1 | `#21D9EF` |
| Blue | Blue 2 | `#DEFDFF` |
| Blue | Blue 3 | `#66EDFA` |
| Blue | Blue 4 | `#0EB2C6` |

## Mapeamento semântico do anexo

| Papel | Família | Aplicação |
|---|---|---|
| Brand | Purple | Ações primárias, seleção, navegação ativa e assinatura visual |
| Neutral | Gray / Black | Texto, superfície, borda, separadores e estados desabilitados |
| Feedback | Green / Orange / Blue | Sucesso, alerta e informação contextual |
| Accent | Yellow / Pink | Campanhas, badges e momentos de destaque controlado |

Gray 1/2 podem compor superfícies **internas**, nunca o canvas base de página. `White #FFFFFF` continua obrigatório em todas as telas.

## Variáveis primitivas de implementação

```css
:root {
  --guivos-gray-1: #F9F9F9;
  --guivos-gray-2: #F3F3F3;
  --guivos-gray-3: #E3E3E3;
  --guivos-gray-4: #A1A1A1;
  --guivos-white: #FFFFFF;
  --guivos-black-1: #292929;
  --guivos-black-2: #232323;
  --guivos-purple-1: #7D55C6;
  --guivos-purple-2: #EDE9FE;
  --guivos-purple-3: #B1A1E4;
  --guivos-purple-4: #5D34A9;
  --guivos-yellow-1: #FDDC00;
  --guivos-yellow-2: #FFFCDD;
  --guivos-yellow-3: #FFF089;
  --guivos-pink-1: #F177C5;
  --guivos-pink-2: #FBE8F5;
  --guivos-pink-3: #F7AADD;
  --guivos-pink-4: #E84CAB;
  --guivos-orange-1: #FF5600;
  --guivos-orange-2: #FFEBE1;
  --guivos-orange-3: #FFB996;
  --guivos-orange-4: #E04D02;
  --guivos-green-1: #26CF7C;
  --guivos-green-2: #D7FFEB;
  --guivos-green-3: #BCF6D8;
  --guivos-green-4: #18A15D;
  --guivos-blue-1: #21D9EF;
  --guivos-blue-2: #DEFDFF;
  --guivos-blue-3: #66EDFA;
  --guivos-blue-4: #0EB2C6;
}
```

## Verificação e aceite

- Verificar `#FFFFFF` como fundo-base em todas as rotas, modos e resoluções.
- Auditar cores efetivamente usadas em CSS, SVG/canvas, gráficos, grafos, elementos interativos, estados de foco e bibliotecas.
- Bloquear cores explícitas não pertencentes à tabela; converter bibliotecas gráficas para tokens da Guivos sem alterar os dados.
- Preservar contraste, legibilidade, interpretação não dependente de cor e acessibilidade.
- Imagens fotográficas não requerem recoloração; a restrição cromática incide sobre as cores geradas para a interface.

## Checkpoint

```text
OFFICIAL PRIMITIVE COLOR TOKENS → 30
OUT-OF-PALETTE UI COLORS → PROHIBITED
ALL PAGE BASE BACKGROUNDS → #FFFFFF / REQUIRED
DASHBOARD KPI MATURITY → UNCHANGED
PRODUCT IMPLEMENTATION AUTHORITY → UNCHANGED
```
