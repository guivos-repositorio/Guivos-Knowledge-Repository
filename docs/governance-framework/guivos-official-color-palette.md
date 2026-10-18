---
id: GKR-BRAND-COLOR-PALETTE-001
title: Guivos — Paleta Oficial de Cores e Fundo Branco
status: active
version: 1.2.1
owner: Guivos
last_updated: 2026-10-18
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

## Reafirmação institucional — exclusividade e semântica (17–18/10/2026)

**Direção expressa do fundador, ratificando e esclarecendo a regra já ativa nesta autoridade:** em **todo o ecossistema Guivos** (Homes, jornadas, produtos, Replit, documentação, dashboards e componentes), **não pode ser introduzida nenhuma cor de interface fora dos 30 tokens oficiais** desta página. A origem é a paleta oficial *Foundations / Colors / Cores* (30 variáveis da coleção `guivos.com.br`), reapresentada pelo fundador em 17/10/2026. É proibido introduzir vermelho `#FF0000`, variantes de vermelho, cores padronizadas de frameworks, misturas derivadas, opacidades cromáticas ou tonalidades não previstas na paleta.

**A exclusividade dos valores não basta:** cada família deve ser empregada **segundo o contexto semântico previsto na fonte**. Não utilizar uma cor pertencente à paleta com sentido contrário à sua finalidade apenas porque o HEX está permitido.

| Situação | Família oficial | Tokens indicados / limite |
|---|---|---|
| Completa, sucesso, confirmação e disponibilidade | **Green** | `Green 4 #18A15D` para indicação textual quando contraste adequado; `Green 2 #D7FFEB` para superfície interna leve; demais verdes apenas conforme contraste |
| Pendências, erro de preenchimento, alerta e urgência | **Orange** | `Orange 4 #E04D02` para sinalização textual quando contraste adequado; `Orange 2 #FFEBE1` para superfície interna leve; **vermelho não é cor da paleta** |
| Orientação e informação não urgente | **Blue** | Azul oficial, com texto legível e contexto explícito |
| Aba ativa, ação primária, seleção, navegação ativa | **Purple** | Roxo oficial como seleção independente de estado completa/pendente |
| Superfícies, texto e bordas comuns | **Gray / Black** | Cores neutras oficiais, base de página sempre `#FFFFFF` |
| Atenção leve e destaque editorial/promocional | **Yellow / Pink** | Não substituir laranja nos alertas funcionais nem verde nas confirmações |

### Aplicação obrigatória — abas de formulários

- **Aba ativa**: destaque roxo da Guivos, independentemente de estar concluída ou pendente.
- **Aba completa**: palavra `COMPLETA` e/ou pequeno indicador em verde oficial (recomendado `#18A15D` com contraste validado); preenchimento interno verde claro `#D7FFEB` pode existir quando necessário, sem cobrir a seleção roxa.
- **Aba com pendências**: palavra `PENDÊNCIAS` e/ou pequeno indicador em laranja oficial (recomendado `#E04D02` com contraste validado); `#FFEBE1` pode ser usado como apoio interno discreto.
- **Não iniciada**: neutros oficiais, com rótulo próprio; não presumir erro em aba ainda não preenchida quando o fluxo aceita rascunho.
- **Bloqueada/indisponível**: neutros e explicação textual contextual; não atribuir automaticamente semântica de alerta.
- **Critério de equilíbrio**: preferir colorir **somente o rótulo de status** (eventualmente pequeno indicador), sem transformar todas as abas em grandes cartões coloridos. Status legível sem depender exclusivamente da cor; foco e acesso por teclado preservados.
- **Regras funcionais inalteradas**: livre navegação entre abas, salvamento de rascunho incompleto e validação de campos obrigatórios somente no envio definitivo. Cor não pode bloquear uma ação por si só.

**Auditoria de implementação:** impedir vermelho inclusive em bibliotecas, CSS compilado, ícones, mensagens de validação, gráficos e efeitos; impedir cores interpoladas ou derivadas não pertencentes aos 30 valores; verificar estados default/hover/focus/disabled, mobile/desktop e contraste em uso. Fotografias reais podem manter suas cores naturais, como já dispõe a seção de regras obrigatórias. **Esta reafirmação não concede autorização financeira, de produção ou de novas funcionalidades.**

## Identidade cromática por tipo de participante — decisão do fundador (17–18/10/2026)

**Regra institucional aprovada de diferenciação visual dentro do ecossistema Guivos:** os participantes **Organização**, **Coletivo** e **Pessoa** têm identidades contextuais reconhecíveis pelos tokens já existentes na paleta, sem criar nova cor ou subidentidade gráfica independente.

| Participante ativo | Cor(es) predominante(s) | Contrato de aplicação |
|---|---|---|
| **Organização** | **Purple 4 — `#5D34A9`** | Cor contextual predominante para navegação própria, identidade do ambiente, indicador de contexto e ações institucionais quando coerentes com a hierarquia |
| **Coletivo** | **Pink 4 — `#E84CAB`** | Cor contextual predominante para navegação própria, identidade do ambiente, indicador de contexto e ações do Coletivo quando coerentes com a hierarquia |
| **Pessoa** | Família Purple: **Purple 1 `#7D55C6`**, **Purple 2 `#EDE9FE`**, **Purple 3 `#B1A1E4`**, **Purple 4 `#5D34A9`** | Identidade da experiência da Pessoa orientada pelas cores principais da marca; a hierarquia de uso (primária, selecionada, apoio, superfície) deve preservar legibilidade |

### Regras de precedência e consistência

1. **Identidade do participante ≠ estado funcional.** A predominância roxa ou rosa identifica o **contexto de atuação**; não substitui **Green** para conclusão/sucesso, **Orange** para alerta/pendência, **Blue** para informação e neutros para leitura. Nenhuma dessas cores semânticas será recolorida para a cor do participante apenas por personalização.
2. **Coletivo — exceção contextual explícita ao uso geral de Pink.** Embora a família Pink seja descrita na paleta primitiva como acento promocional/editorial, a decisão do fundador atribui especificamente **Pink 4 `#E84CAB`** também à identidade de contexto do Coletivo e à sua navegação. Isso **não** permite usar os outros tons rosa indiscriminadamente em alertas, sucessos ou informações, nem criar novas tonalidades.
3. **Organização — Purple 4.** O uso de Purple 4 no contexto institucional não autoriza inferir que toda superfície, texto ou ícone deva ser roxo, nem afastar o fundo-base branco.
4. **Pessoa — paleta Purple da marca.** Evitar distinguir a Pessoa somente por Purple 4, pois esta é também a cor predominante da Organização; combinar a hierarquia da família Purple, rótulos e elementos de contexto, preservando identidade visual da Pessoa.
5. **Acesso com múltiplos participantes:** na troca efetiva de contexto, sinalizar de forma visível e acessível qual participante está ativo; não alterar permissões, vínculo ou identidade por mudança de cor. Exibir nome/tipo do participante e indicadores textuais, nunca depender **somente da cor** para distinguir Organização, Coletivo e Pessoa.
6. **Base visual única:** canvas `#FFFFFF` em todas as páginas; componentes podem usar somente as outras cores primitivas oficiais conforme propósito. Áreas internas de fundo e bordas permanecem neutras onde a cor contextual prejudicaria legibilidade, acessibilidade ou clareza de hierarquia.
7. **Design system transversal:** aplicar à navegação, cabeçalhos, seleção, botões contextuais, elementos de orientação e padrões reutilizáveis em Home, cadastro, jornadas autenticadas, mobile, web, Replit, produtos e superfícies futuras; preservar liberdade de composição do Design dentro destas regras, sem engessar layout.
8. **Não criar cores por variação:** hover, foco, gradientes, overlays, transparência e estados devem reutilizar tokens existentes, sem produzir tons derivados. Fotografias/vídeos reais conservam suas cores naturais, conforme regra da paleta.

### Amarelo oficial — destaque, atenção leve e energia visual (confirmação do fundador, 18/10/2026)

O **amarelo não deve ser omitido do sistema de identidade visual**. Os três tokens oficiais já constam da paleta primitiva e têm função própria:

| Token | HEX | Aplicação contextual |
|---|---|---|
| **Yellow 1** | **`#FDDC00`** | Destaque de maior intensidade, ponto de energia visual e ênfase controlada |
| **Yellow 2** | **`#FFFCDD`** | Fundo interno sutil de destaque e atenção leve |
| **Yellow 3** | **`#FFF089`** | Destaque intermediário e apoio visual, com contraste validado |

**Precedência:** amarelo sinaliza destaque ou atenção **leve**, não deve substituir `Orange` nos **alertas, erros e pendências**, `Green` nos **sucessos e confirmações**, `Blue` nas **informações de orientação**, nem as identidades predominantes `Purple 4` da Organização, `Pink 4` do Coletivo e família `Purple 1–4` da Pessoa. Pode ser usado em componentes de qualquer participante quando sua finalidade semântica justificar, sem criar nova identidade cromática por participante. Manter canvas de página `#FFFFFF`, valores exclusivamente da paleta, leitura acessível e uso moderado para preservar hierarquia.

### Testes mínimos por contexto

- Entrar em **Organização**: identidade visual institucional distinguível usando `#5D34A9`, com sucesso em verde, alerta em laranja, informação em azul e canvas branco.
- Entrar em **Coletivo**: identidade contextual distinguível usando `#E84CAB`, com as mesmas cores semânticas preservadas e contraste suficiente.
- Entrar em **Pessoa**: identidade da marca com família Purple 1–4, sem copiar indiscriminadamente o estilo de Organização.
- Navegar/trocar contexto: mesma semântica, identificação textual acessível, menu e permissões coerentes com o participante real.
- Auditoria de toda UI: **0 cores de interface fora dos 30 tokens primitivos oficiais**; nenhuma cor fora de contexto, nenhuma dependência exclusiva de cor.

**Estado:** `FOUNDER_PARTICIPANT_COLOR_DIRECTION_ACCEPTED / DESIGN_CONTEXT_AUTHORITY / PALETTE_30_ONLY / NO_PRODUCT_PERMISSION_CHANGE`.

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
