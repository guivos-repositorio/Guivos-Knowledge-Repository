---
id: GKR-BRAND-COLOR-PALETTE-001
title: Guivos — Paleta Oficial de Cores e Fundo Branco
status: active
version: 1.3.3
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
| Completa, sucesso, confirmação e disponibilidade | **Green** | `Green 4 #18A15D` para marca visual/indicador ou texto grande, não para texto pequeno sobre branco; `Green 2 #D7FFEB` para superfície interna leve; demais verdes apenas conforme contraste |
| Pendências, erro de preenchimento, alerta e urgência | **Orange** | `Orange 4 #E04D02` para marca visual/indicador ou texto grande, não para texto pequeno sobre branco; `Orange 2 #FFEBE1` para superfície interna leve; **vermelho não é cor da paleta** |
| Orientação e informação não urgente | **Blue** | Azul oficial, com texto legível e contexto explícito |
| Aba ativa, ação primária, seleção, navegação ativa | **Purple** | Roxo oficial como seleção independente de estado completa/pendente |
| Superfícies, texto e bordas comuns | **Gray / Black** | Cores neutras oficiais, base de página sempre `#FFFFFF` |
| Atenção leve e destaque editorial/promocional | **Yellow / Pink** | Não substituir laranja nos alertas funcionais nem verde nas confirmações |

### Aplicação obrigatória — abas de formulários

> **Atualização específica aprovada pelo fundador em 18/10/2026 — prevalece sobre a preferência anterior de colorir somente o rótulo:** cada **aba/cartão de etapa inteiro** deverá indicar o estado com preenchimento semântico claro. **COMPLETA/PRONTA** → fundo **Green 2 `#D7FFEB`**; **PENDÊNCIAS** → fundo **Orange 2 `#FFEBE1`**. Não usar preenchimento rosa ou roxo para indicar conclusão. Títulos e status ficam em **Black 2 `#232323`**, acompanhados de sinal gráfico Green 4 `#18A15D` ou Orange 4 `#E04D02`, respectivamente. A seleção/aba ativa permanece identificável por **contorno/indicador contextual discreto** (Organização Purple 4 `#5D34A9`; Coletivo Pink 4 `#E84CAB`) e **não substitui o fundo semântico da etapa**. Etapas ainda não iniciadas podem permanecer em White/Gray. Essa regra de sinalização aplicada ao cartão inteiro vale para cadastros de perfis e oportunidades, em todos os participantes, desktop e mobile; cor não é o único meio de indicar estado. Validação de campos e navegação livre/résumé de rascunhos permanecem inalteradas. A superfície da página continua White `#FFFFFF`.



- **Aba ativa**: destaque roxo da Guivos, independentemente de estar concluída ou pendente.
- **Aba completa**: palavra `COMPLETA` legível em `#232323` associada a pequeno indicador `#18A15D`, ou texto verde somente quando o contraste real atender ao requisito; preenchimento interno verde claro `#D7FFEB` pode existir quando necessário, sem cobrir a seleção roxa.
- **Aba com pendências**: palavra `PENDÊNCIAS` legível em `#232323` associada a pequeno indicador `#E04D02`, ou texto laranja somente quando o contraste real atender ao requisito; `#FFEBE1` pode ser usado como apoio interno discreto.
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

## Auditoria completa por família — cores neutras, acentos e feedback (18/10/2026)

**Base documental:** *Paleta de Cores.pdf*, *Foundations / Colors / Cores*, página 1, coleção `guivos.com.br`, 30 variáveis primitivas. Reafirmação do fundador: a UX deve aproveitar **todas as famílias de modo contextual**, sobretudo os neutros `Gray/Black` indispensáveis à estrutura; não basta enfatizar roxo/rosa nem apenas os status. A tabela estabelece orientações de aplicação, **não** cria token fora do PDF.

| Família | Tokens oficiais | Semântica da fonte | Aplicação em componentes |
|---|---|---|---|
| **Gray** | `Gray 1 #F9F9F9`; `Gray 2 #F3F3F3`; `Gray 3 #E3E3E3`; `Gray 4 #A1A1A1`; `White #FFFFFF` | Base neutra, superfícies, bordas e texto secundário | Canvas **White**; Gray 1 para cards/superfícies internas leves, Gray 2 para agrupamentos internos, Gray 3 para divisórias e bordas, Gray 4 para elementos secundários/desabilitados **sem depender dele para textos pequenos importantes** |
| **Black** | `Black 1 #292929`; `Black 2 #232323` | Texto principal e alto contraste | Títulos, textos corridos, rótulos, dados e estados de alto valor informativo; Black 2 como fallback seguro para textos pequenos sobre branco e sobre fundos claros da paleta |
| **Purple** | `#7D55C6`; `#EDE9FE`; `#B1A1E4`; `#5D34A9` | Marca, seleção e ação primária | Identidade Pessoa (Purple 1–4), identidade Organização (Purple 4), ações/seleção da hierarquia aplicável, foco consistente |
| **Yellow** | `#FDDC00`; `#FFFCDD`; `#FFF089` | Destaque, atenção leve, energia visual | Acentos, destaque editorial e superfície interna leve; não substitui alerta laranja; textos escuros quando sobre amarelo claro |
| **Pink** | `#F177C5`; `#FBE8F5`; `#F7AADD`; `#E84CAB` | Acentos promocionais e editoriais; **Pink 4 também identifica Coletivo por decisão específica** | Coletivo reconhecível sem transformar toda a página em rosa; Pink 2 para superfície interna quando apropriado; evitar texto pequeno branco sobre Pink 4 |
| **Orange** | `#FF5600`; `#FFEBE1`; `#FFB996`; `#E04D02` | Alerta, urgência e comunicação quente | Erro/pendência com marca visual Orange 4 e texto legível; Orange 2 em apoio sutil; nenhuma cor vermelha externa |
| **Green** | `#26CF7C`; `#D7FFEB`; `#BCF6D8`; `#18A15D` | Sucesso, confirmação, disponibilidade | Completa/sucesso com indicador Green 4 e texto contrastante; Green 2/3 em apoio sutil; não usar como confirmação onde ainda houver pendência |
| **Blue** | `#21D9EF`; `#DEFDFF`; `#66EDFA`; `#0EB2C6` | Informação, apoio e orientação | Dicas de ajuda, informação contextual e orientação não urgente; Blue 2 em fundo interno e texto contrastante |

### Composição por camadas (não criar uma nova paleta)

1. **Estrutura:** `White #FFFFFF` para página, `Black 1/2` para títulos e corpo, `Gray 1/2` para superfícies internas e `Gray 3` para bordas e separadores. Gray 4 pode indicar detalhes secundários ou indisponibilidade, com leitura acessível; não substituir automaticamente todos os textos auxiliares por Gray 4.
2. **Participante ativo:** Purple 4 para Organização; Pink 4 para Coletivo; conjunto Purple 1–4 para Pessoa, sempre com identificação escrita do contexto. A cor predominante é **um acento contextual**, não uma autorização para pintar os fundos completos ou substituir texto negro estrutural.
3. **Semântica funcional:** Green para concluído, Orange para erro/pendências, Blue para informação, Yellow para atenção leve, Pink/Yellow para acento editorial conforme uso; não inverter nem trocar papel funcional apenas para variar visualmente.
4. **Estados:** ativa/selecionada com cor do contexto e foco; completa/pendência com indicador funcional discreto e texto contrastante; neutra/desabilitada com Gray/Black e explicação quando necessária. Hover/focus/disabled devem usar somente valores oficiais.
5. **Imagens:** fotografias e vídeos reais mantêm suas cores naturais; as cores desenhadas pela interface ao redor continuam limitadas aos 30 tokens.

### Critério obrigatório de contraste — evitar erro ao usar HEX semanticamente corretos

O documento original exige contraste suficiente. A família semântica **não torna automaticamente qualquer combinação acessível**. Razões de contraste aproximadas calculadas para texto sobre `White #FFFFFF`:

| Token no texto / branco | Contraste | Aplicação |
|---|---:|---|
| `Black 2 #232323` | **15,72:1** | Texto normal/pequeno seguro |
| `Black 1 #292929` | **14,55:1** | Texto normal/pequeno seguro |
| `Purple 4 #5D34A9` | **8,30:1** | Texto normal acessível |
| `Purple 1 #7D55C6` | **5,27:1** | Texto normal acessível |
| `Orange 4 #E04D02` | **4,01:1** | **Insuficiente para texto normal WCAG AA 4,5:1** sobre branco; adequado somente em usos que não dependam desse contraste para texto pequeno |
| `Green 4 #18A15D` | **3,34:1** | **Insuficiente para texto normal WCAG AA** sobre branco |
| `Pink 4 #E84CAB` | **3,47:1** | **Insuficiente para texto normal WCAG AA** sobre branco |
| `Gray 4 #A1A1A1` | **2,58:1** | **Insuficiente para texto normal e como único indicador informacional essencial** sobre branco |

**Padrão de remediação:** rótulos pequenos `COMPLETA` e `PENDÊNCIAS` devem priorizar texto `#232323` sobre fundo muito claro autorizado (`Green 2 #D7FFEB` ou `Orange 2 #FFEBE1`), acrescido de elemento funcional verde/laranja; não exigir texto verde/laranja em branco quando falha o contraste. Para navegação Coletivo em `Pink 4`, evitar texto branco pequeno, usar `Black 2` quando contraste suficiente, ou superfícies claras autorizadas. Manter o roxo da aba ativa sem sacrificar foco, teclado ou a indicação funcional.

**Proibição expressa:** não solucionar contraste inventando um novo verde/laranja/rosa/cinza escuro; selecionar **outra combinação entre os mesmos 30 tokens** ou um recurso redundante de texto/forma. Conferir texto normal, texto grande, ícones informativos, bordas de componentes, hover, foco, erros, modal e gráfico individualmente; razões acima não substituem testes da combinação real de primeiro plano/fundo.

### Critérios de aceite transversal

- Inventário visual/CSS de cada tela e estado contendo **somente os 30 tokens**; zero vermelhos externos, cinzas padrão herdados, preto `#000000`, branco derivado ou tons interpolados não autorizados.
- Fundo-base `#FFFFFF` em todas as jornadas; `Gray/Black` fazem a maior parte da estrutura da experiência.
- Todos os **oito grupos cromáticos** usados segundo função (não é obrigatório forçar a presença das oito famílias em cada tela).
- Organização/Coletivo/Pessoa distinguíveis pelo padrão contextual, **não apenas pela cor**.
- Textos e controles atendem contraste para seu tamanho/função, sem criar novos HEX para corrigir problemas.
- Abas e ações mantêm semântica, legibilidade e acessibilidade, sem afetar rascunho, navegação livre ou autorização de produção.
- Auditar telas, componentes, CSS servido, ícones, estados, temas importados, gráficos e PDF/SVG desenhados para UI, quando aplicáveis.

### Padrão estrutural de bordas claras — decisão do fundador (18/10/2026)

**Direção expressa, motivada pela inspeção do modal “Registrar evidência”:** contornos externos de **modais, diálogos, formulários, cartões e contêineres estruturais** devem utilizar **neutros claros oficiais**, preferencialmente **Gray 3 `#E3E3E3`**, alternativamente **Gray 2 `#F3F3F3`** quando uma separação ainda mais leve for adequada. A base interna do modal/card é preferencialmente `White #FFFFFF`; a base da página permanece obrigatoriamente `#FFFFFF`.

- **Não usar Black 1 `#292929` ou Black 2 `#232323` como contorno estrutural padrão**, mesmo sendo cores da paleta. Sua função principal continua sendo texto e contraste alto.
- O padrão deve ser aplicado de modo consistente a bordas de modais, cards, painéis de revisão, formulários e áreas de evidência, sem apagar limites de controle, separadores funcionais, hierarquia, agrupamentos ou acessibilidade.
- Estados com significado próprio podem usar indicadores ou cores semânticas apropriadas da paleta, **sem converter todas as bordas em alertas ou destaques**. Estado de foco perceptível e indicação de seleção ativa são exceções funcionais justificadas, com tokens oficiais.
- Evitar contornos pretos, sombras pesadas e novas tonalidades criadas por opacidade ou misturas. Se houver elevação visual, resolver prioritariamente por contraste entre `#FFFFFF`, `#F9F9F9`, `#F3F3F3`, borda `#E3E3E3` e espaçamento; não introduzir preto translúcido.
- **Verificação obrigatória:** modal “Registrar evidência” sem contorno escuro; diálogos e cards da jornada revisados em Organização e Coletivo, desktop e mobile; legibilidade, foco, teclado e distinção dos limites mantidos.

**Estado:** `FOUNDER_BORDER_STYLE_ACCEPTED / LIGHT_NEUTRAL_DEFAULT / PALETTE_30_ONLY`.

### Padrão transversal de botões e ações comuns — decisão do fundador (18/10/2026)

**Correção explícita de identidade × funcionalidade:** as cores predominantes de participantes identificam **o contexto** e **não devem determinar automaticamente a cor de botões ou funcionalidades padrão**. Todos os participantes compartilham o mesmo padrão visual de botões do sistema, evitando excesso de cor ou mudanças arbitrárias ao alternar Organização e Coletivo.

- **Botão primário padrão** (incluindo `Continuar`, `Criar oportunidade` e ações gerais equivalentes): fundo **Black 2 `#232323`** e texto **White `#FFFFFF`**, sem cor rosa/roxa por contexto. A aplicação deve verificar contraste e dimensionamento. Black 1 `#292929` pode compor estados dentro do padrão oficial, quando legitimamente especificado.
- **Botões secundários e terciários:** fundo `#FFFFFF`, texto `#232323`, contorno leve `Gray 3 #E3E3E3` ou `Gray 2 #F3F3F3` quando aplicável, conservando diferenciação hierárquica, foco visível e acessibilidade.
- **Desabilitado:** neutros oficiais (`Gray`/`Black`) com indicação textual e funcional; não depender apenas de cor.
- **Identidade contextual:** Purple 4 `#5D34A9` continua identificando Organização, Pink 4 `#E84CAB` continua identificando Coletivo; família Purple identifica Pessoa. Usar nos acentos, ilustrações, marcação do contexto e elementos de seleção. **Botão primário não muda de cor quando outro participante é selecionado.**
- **Exceções semânticas legítimas:** controles cujo papel seja inequivocamente funcional (estado de alerta, sucesso, informação) podem ter sinalização Orange/Green/Blue **sem converter o padrão geral de botões** ou gerar nova regra de cor por participante. Não pintar botões comuns de rosa ou roxo por serem da jornada Coletivo/Organização.
- **Alcance:** tela inicial de escolha de participante, criação/edição de perfis, oportunidades, operações de Coletivo/Organização, modais, ações de formulário e componentes reutilizáveis; aplicar em todos os projetos de forma progressiva e governada, sem modificar produto, autorização, dados ou produção.
- **Verificação:** alternar a seleção Organização ↔ Coletivo: ilustração e cartões indicam participante, mas `Continuar` permanece Black 2; botões `Criar oportunidade` em ambos os ambientes usam o mesmo Black 2; status e bordas continuam semânticos e neutros conforme a paleta.

Esta regra **prevalece** sobre orientações anteriores de colorir todos os botões e ações conforme o participante. Não elimina o papel Purple da paleta na marca e nos estados selecionados; apenas estabelece a **uniformidade dos botões funcionais padrão**.

**Estado:** `FOUNDER_COMMON_BUTTON_STANDARD_ACCEPTED / BLACK_2_PRIMARY / PARTICIPANT_ACCENT_SEPARATE`.

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
