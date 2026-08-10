---
id: GKR-UX-HOME-GTM-BOUNDARY-001
title: Fronteira entre Arquitetura da Home e Estratégia de Marketing, Lançamento e GTM
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-HANDOFF-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-002
  - GKR-UX-HOME-SYS-001
  - GKR-UX-HOME-AUDIT-001
normative: false
---

# Fronteira entre Arquitetura da Home e Estratégia de Marketing, Lançamento e GTM

## 1. Finalidade

Este documento corrige uma sobreposição de escopo identificada durante a construção da Home pública de `guivos.com`.

A frente atual está construindo **o ecossistema e a arquitetura institucional da Home**. Ela não deve antecipar a futura estratégia de Marketing, lançamento ou Go-to-Market (`GTM`).

A decisão central é:

> **Arquitetura da Home define o que a Guivos é, como o ecossistema deve ser percebido e quais caminhos conceitualmente pertencem à experiência pública. Marketing/GTM define quando, como, em quais mercados e com qual intensidade cada parte do ecossistema será apresentada, ativada ou lançada ao mercado.**

---

## 2. O que pertence à arquitetura da Home

Esta frente pode definir:

- posicionamento e percepção institucional;
- Hero e mensagem central;
- arquitetura narrativa;
- onze movimentos narrativos;
- papel de Pessoas, Organizações e Coletivos;
- papel institucional de Journey, Travel, Mall, Media, Business, Intelligence e Ads;
- hierarquia de navegação;
- Header Persistente;
- launcher do ecossistema;
- presença conceitual de `Sobre`, `Login`, `Iniciar Jornada`, idioma/região e compartilhar;
- link `Mapa do Ecossistema` no rodapé;
- sistema de conteúdo e prova;
- princípios de interação, movimento, ritmo, acessibilidade e percepção visual;
- critérios para futuro wireframe, UX/UI e Figma.

Essas decisões podem ser tomadas enquanto os produtos e o ecossistema ainda estão em construção.

---

## 3. O que NÃO pertence à arquitetura da Home nesta frente

Ficam fora do escopo atual:

- qual produto será lançado primeiro;
- quais produtos estarão operacionais no lançamento inicial;
- quais produtos serão teaser, preview, beta, waitlist ou `em breve`;
- calendário de lançamento;
- rollout progressivo;
- priorização comercial;
- estratégia de pré-lançamento;
- campanhas de lançamento;
- estratégia de aquisição;
- canais de mídia;
- países ou regiões de entrada comercial;
- ordem de internacionalização;
- disponibilidade comercial por mercado;
- exposição maior ou menor de cada produto por fase;
- estratégia de lançamento das páginas institucionais;
- estratégia de lançamento da página `Mapa do Ecossistema`;
- decisão de GTM sobre quando tornar cada destino efetivamente clicável em produção.

Essas decisões deverão ser tratadas futuramente pela autoridade de Marketing/GTM apropriada, reconciliada com Produto, Operação, Legal, Tecnologia e demais autoridades quando necessário.

---

## 4. Presença conceitual não equivale a disponibilidade operacional

A arquitetura pode estabelecer, por exemplo, que o launcher do Header contém conceitualmente:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Isso não declara que todos esses produtos estarão simultaneamente disponíveis em produção em determinada data.

Da mesma forma:

> **`Iniciar Jornada` como porta conceitual da Journey ≠ declaração de que um fluxo específico de Journey está operacional hoje ou estará disponível em uma data de lançamento ainda não definida.**

Separação obrigatória:

```text
presença na arquitetura
≠ disponibilidade operacional
≠ decisão de lançamento
≠ prioridade de Marketing
```

---

## 5. Wireframe conceitual não exige estratégia de lançamento fechada

A futura materialização conceitual da Home poderá representar:

- destinos definidos pela arquitetura;
- slots de histórias e evidências;
- áreas de mídia;
- CTAs por função narrativa;
- launcher;
- Header;
- Movimento 08 — Ecossistema / Produtos;
- estados de conteúdo e fallback.

Ela não precisa conhecer previamente a estratégia de lançamento de cada produto.

Quando um destino ainda não possuir decisão de GTM, o wireframe deve tratá-lo como **destino conceitual governado**, e não inventar um estado comercial ou operacional.

---

## 6. Evidência no wireframe

O wireframe pode reservar e especificar tipos de evidência sem fabricar fatos.

Exemplos válidos de especificação:

- `slot de história real documentada`;
- `slot de fotografia com autorização`;
- `slot de evidência institucional`;
- `slot de métrica com fonte/período`;
- `slot editorial Guivos Media`;
- `fallback quando prova não estiver disponível`.

Exemplos inválidos:

- inventar nome de participante real;
- inventar Organização parceira;
- inventar número de usuários;
- inventar país de operação;
- inventar depoimento;
- inventar resultado de transformação.

Portanto:

> **inventário final de provas não é pré-condição para desenhar a arquitetura; prova fictícia continua proibida.**

---

## 7. Verdade operacional continua obrigatória antes de publicação

Esta separação de escopo não autoriza a Home publicada a declarar capacidades inexistentes.

Antes de uma versão pública entrar em produção, deverão ser reconciliados, pela autoridade apropriada:

- disponibilidade operacional real;
- destinos realmente ativos;
- claims publicáveis;
- evidências e direitos de uso;
- páginas efetivamente publicadas;
- idiomas/regiões efetivamente suportados;
- requisitos legais e regulatórios;
- estratégia de Marketing/GTM aplicável àquela versão.

Esses itens são **gates de publicação/lançamento**, não gates da arquitetura conceitual da Home.

---

## 8. Correção dos gates anteriores

Onde documentos anteriores desta mesma frente apresentarem como pré-condição para iniciar wireframe ou Figma itens como:

- disponibilidade real dos produtos no lançamento;
- estado operacional que será comunicado;
- produtos que poderão ser mostrados publicamente em determinada fase;
- páginas que existirão no primeiro lançamento;
- idiomas/regiões do lançamento;
- inventário definitivo de destinos clicáveis;
- estratégia de exposição comercial por produto;

essas exigências ficam **superadas como gate pré-wireframe** por este refinamento.

Elas poderão retornar futuramente como inputs de:

- conteúdo final;
- implementação;
- QA de publicação;
- release;
- Marketing;
- GTM;
- operação.

---

## 9. O que continua sendo gate da arquitetura

Antes de materialização governada, continuam relevantes:

- escopo restrito à Home pública;
- autoridades e documentos da frente reconciliados;
- arquitetura narrativa aceita;
- Header e navegação conceitualmente definidos;
- limites da Hero preservados;
- produtos subordinados à ideia maior;
- Journey separada do launcher conforme decisão vigente;
- link `Mapa do Ecossistema` limitado ao rodapé, sem antecipar sua página;
- regras de prova e não simulação preservadas;
- autonomia e privacidade preservadas;
- autorização explícita para iniciar a etapa de materialização.

---

## 10. Efeito sobre a auditoria pré-wireframe

`GKR-UX-HOME-AUDIT-001` deve considerar como **fora do gate pré-wireframe**:

- inventário de produtos operacionais no lançamento;
- inventário de páginas do lançamento;
- disponibilidade de idiomas/regiões no lançamento;
- estado comercial de cada produto;
- decisão de teaser/beta/waitlist/em breve;
- destinos finais de produção ainda dependentes de GTM.

A auditoria deve avaliar se a estratégia da Home está suficientemente definida para ser materializada conceitualmente, e não se o plano de lançamento já está definido.

---

## 11. Regra para Marketing futuro

A futura estratégia de Marketing/GTM poderá decidir alterar a exposição de determinadas partes do ecossistema em uma versão específica da Home.

Essa adaptação deverá preservar as autoridades da marca e da experiência.

Marketing poderá decidir **quando e quanto expor**.

Não deverá redefinir, sem governança adequada:

- o que a Guivos é;
- a relação entre Pessoa, Organização e Coletivo;
- o papel estrutural de Journey;
- a responsabilidade dos produtos;
- a autonomia do participante;
- a verdade operacional;
- a arquitetura canônica do ecossistema.

---

## 12. Síntese de controle

```text
ARQUITETURA DA HOME
→ significado
→ narrativa
→ percepção
→ hierarquia
→ caminhos conceituais
→ experiência

MARKETING / GTM
→ timing
→ lançamento
→ exposição por fase
→ canais
→ mercados
→ campanhas
→ ativação

OPERAÇÃO / PRODUTO / TECNOLOGIA / LEGAL
→ o que de fato pode funcionar e ser declarado em produção
```

Regra final:

> **Construir a Home não exige antecipar a estratégia de lançamento do ecossistema. A arquitetura deve ser suficientemente completa para representar a Guivos; Marketing/GTM decidirá futuramente como essa arquitetura será ativada no mercado em cada fase.**
