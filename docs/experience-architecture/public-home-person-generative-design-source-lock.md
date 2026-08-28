---
id: GKR-UX-HOME-PERSON-GENINPUT-001
title: Source Lock de Checkpoint — Home Pública — Pessoa — Primeira Exploração de Design
status: active
version: 1.1.0
owner: Experience Architecture
last_updated: 2026-08-27
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001
normative: false
maturity: checkpoint_evidence_non_authorizing
---

# Source Lock de Checkpoint — Home Pública — Pessoa

## 1. Finalidade atual

Este documento preserva integralmente o **Source Lock utilizado na primeira exploração de Design da Home Pública principal da Guivos, com perspectiva predominante da Pessoa**, no checkpoint registrado em 13/08/2026.

Naquele checkpoint, ele funcionou como instância operacional de `GKR-UX-HOMES-GENINPUT-001`: congelou as fontes então vigentes, explicitou o que precisava ser preservado e forneceu um prompt controlado para Figma Make ou ferramenta generativa equivalente.

Depois da auditoria integral e da reconstrução de `GKR-UX-HOME-MASTER-001 v1.0.0`, sua função corrente mudou.

Hoje este arquivo é **evidência de checkpoint e rastreabilidade de uma rodada anterior**. Ele não autoriza nova execução de Design.

```text
SOURCE LOCK DE 13/08/2026
→ preserva o pacote de entrada daquela rodada
→ preserva prompt, invariantes, liberdades e proibições então usados
→ permite auditar o que a ferramenta recebeu

SOURCE LOCK DE 13/08/2026
≠ autorização atual de Design
≠ autoridade superior ao master reconciliado
≠ autorização para novo wireframe
≠ autorização para UI
≠ UXA-102 / V5
≠ retomada de Product Engineering
```

### 1.1 Estado de autoridade

| Dimensão | Estado atual |
|---|---|
| checkpoint original | `main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db` |
| função original | Source Lock operacional da primeira exploração |
| função atual | evidência de checkpoint / rastreabilidade |
| autoridade normativa atual | **não** |
| reutilização automática do prompt | **não autorizada** |
| master atual da Home | `GKR-UX-HOME-MASTER-001 v1.0.0` |
| nova materialização | exige decisão governada e novo/reconciliado Source Lock |

### 1.2 Por que o conteúdo é preservado

A reclassificação não apaga o pacote anterior porque ele contém conhecimento útil para auditoria:

- quais fontes foram fornecidas;
- quais invariantes foram protegidos;
- quais liberdades de Design existiam;
- quais inferências foram proibidas;
- qual prompt foi efetivamente preparado;
- qual autoauditoria era exigida;
- qual maturidade a saída poderia atingir.

```text
RECLASSIFICAR AUTORIDADE
≠ APAGAR EVIDÊNCIA

CHECKPOINT SUPERADO
≠ CONTEÚDO HISTÓRICO SEM VALOR
```

A partir daqui, as seções seguintes preservam o pacote do checkpoint original, com avisos explícitos onde sua linguagem operacional poderia ser confundida com autorização corrente.

---

## 2. Source Lock original preservado

### Home

`Home Pública — Pessoa`

### Fase autorizada naquela instância

`arquitetura visual + wireframe low-fi responsivo`

Essa autorização valeu exclusivamente para a rodada e o checkpoint registrados abaixo. **Não permanece aberta no estado atual do GKR.**

### Objetivo daquela rodada

Produzir uma primeira materialização estrutural da Home em desktop e mobile, suficiente para validar:

- hierarquia;
- progressão narrativa;
- ritmo;
- agrupamento dos movimentos;
- relação entre texto, imagem, conteúdo e ação;
- comportamento do Header e navegação em nível conceitual;
- preservação da percepção institucional da Guivos.

Não era objetivo daquela execução fechar direção visual, UI final, design system, copy final ou implementação.

### Checkpoint do GKR

`main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db`

Regra original já registrada e ainda válida como princípio de rastreabilidade:

> **Qualquer execução posterior em outro checkpoint deve gerar novo Source Lock ou registrar explicitamente a reconciliação das diferenças.**

O estado atual está em checkpoint posterior e possui master reconstruído; portanto, essa condição está materialmente acionada.

---

## 3. Fontes autorizadas no checkpoint original

### Fonte de processo

- ID: `GKR-UX-HOMES-DESIGN-HANDOFF-001`
- versão: `1.0.0`
- path: `docs/experience-architecture/public-homes-design-handoff.md`

### Fonte arquitetural principal naquele checkpoint

- ID: `GKR-UX-HOME-MASTER-001`
- versão: `0.1.0`
- path: `docs/experience-architecture/public-home-master-document.md`

> O master da Home foi posteriormente reconstruído como `GKR-UX-HOME-MASTER-001 v1.0.0`. A referência `0.1.0` é preservada aqui porque descreve o pacote realmente usado naquela rodada; ela não é a versão corrente.

### Fonte complementar vigente naquele checkpoint

- ID: `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`
- versão: `1.0.0`
- path: `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`

### Regra de entrada daquela execução

Para a primeira execução, **não adicionar automaticamente** documentos históricos, benchmarks, antigos wireframes, prompts, auditorias ou outras Homes.

Se uma dúvida concreta exigisse aprofundamento, a nova fonte deveria ser declarada antes de entrar no contexto da ferramenta.

---

## 4. Invariantes preservados daquela rodada

A ferramenta deveria preservar:

1. a Guivos como ecossistema maior do que a soma dos produtos;
2. percepção de futuro, possibilidade, simplicidade, confiança e escala ampla/global;
3. tecnologia sem frieza e sofisticação sem complexidade;
4. perspectiva predominante da Pessoa;
5. possibilidade antes de produto;
6. autonomia antes de dependência;
7. a pergunta-mãe e a função narrativa registradas no Documento Mestre;
8. os onze movimentos como progressão sem obrigar onze blocos visuais equivalentes;
9. produtos aparecendo como manifestações/capacidades da Guivos, não como catálogo inicial de sete cards equivalentes;
10. evidência real, conteúdo editorial, conteúdo institucional e ação mantendo naturezas distinguíveis;
11. Media podendo abastecer editorialmente a Home sem adquirir autoridade sobre sua narrativa institucional;
12. ausência de promessa causal de transformação garantida;
13. acessibilidade, responsividade e performance como requisitos da solução, não correções posteriores.

Esses invariantes são preservados como evidência da rodada. Sua validade corrente deve ser lida contra `GKR-UX-HOME-MASTER-001 v1.0.0` e autoridades superiores vigentes; o Source Lock não os promove independentemente.

---

## 5. Liberdades de Design daquela rodada

A ferramenta e Design podiam explorar:

- grid;
- composição;
- número de dobras;
- agrupamento visual dos movimentos;
- escala e hierarquia;
- densidade;
- ritmo;
- uso de espaço vazio;
- tipografia provisória;
- direção de imagem e vídeo;
- fundos e atmosfera;
- componentes;
- modo de materializar Header e navegação;
- microinterações conceituais;
- desktop e mobile com soluções próprias;
- assimetria e variação de escala quando fortalecessem significado.

`Mesma família Guivos` não significava reproduzir a composição das Homes Mall, Travel ou Media.

Essas liberdades descrevem a rodada original e **não constituem autorização corrente para materialização**.

---

## 6. Proibições de inferência preservadas

A ferramenta não podia inventar ou assumir como vigente:

- novos produtos ou serviços;
- funcionalidades não governadas;
- números de usuários;
- métricas de impacto;
- parceiros;
- depoimentos;
- cases;
- avaliações;
- campanhas;
- disponibilidade comercial;
- preços;
- rankings;
- promessas de transformação;
- taxonomias novas;
- uma comunidade Guivos como requisito da Home;
- gamificação como protagonista da Home;
- conteúdo fictício apresentado como evidência real.

Não transformar a Home em:

- landing page SaaS;
- catálogo de serviços;
- dashboard;
- portal de produtos;
- feed social;
- manifesto institucional excessivamente textual.

Essas proibições continuam úteis como evidência e guardrail histórico, mas a autoridade corrente para a Home está no master reconciliado e suas dependências vigentes.

---

## 7. Conteúdo e placeholders daquela rodada

Placeholder era permitido somente para testar arquitetura.

Quando um conteúdo real não estivesse disponível, deveriam ser usados rótulos explícitos como:

- `[HISTÓRIA REAL — A DEFINIR]`;
- `[IMAGEM DOCUMENTAL — A DEFINIR]`;
- `[CONTEÚDO EDITORIAL — A DEFINIR]`;
- `[PROVA VERIFICÁVEL — A DEFINIR]`.

Nunca fabricar nome, número, pessoa, parceiro, organização ou resultado para tornar o wireframe mais convincente.

---

## 8. Pacote entregue à ferramenta naquela execução

A execução deveria receber:

1. este Source Lock;
2. `GKR-UX-HOMES-DESIGN-HANDOFF-001`;
3. `GKR-UX-HOME-MASTER-001` na versão então vigente (`0.1.0`);
4. `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`.

`GKR-UX-HOMES-GENINPUT-001` governava a criação da instância e permanecia como referência operacional do GKR; não precisava ser duplicado no contexto da ferramenta se este Source Lock fosse entregue integralmente.

> **Este pacote é preservado para rastreabilidade. Não deve ser reutilizado como pacote atual.**

---

## 9. Prompt controlado preservado — NÃO EXECUTAR COMO AUTORIZAÇÃO ATUAL

O bloco abaixo é preservado integralmente como evidência do prompt preparado para a primeira exploração.

```text
Você está trabalhando na primeira exploração de Design da Home Pública principal da Guivos, com perspectiva predominante da Pessoa.

OBJETIVO
Crie uma proposta de arquitetura visual e wireframe low-fi responsivo para desktop e mobile. A saída deve permitir avaliar hierarquia, progressão narrativa, ritmo, agrupamento dos movimentos e caminhos de ação. Não trate a saída como UI final nem como implementação pronta.

FONTES AUTORIZADAS
Use exclusivamente os documentos anexados e este Source Lock como fonte de decisões sobre a Guivos e esta Home. Se alguma informação necessária não estiver definida, sinalize a lacuna ou use hipótese explicitamente rotulada. Não transforme hipótese em requisito.

INVARIANTES
- a Guivos deve parecer maior do que a soma de seus produtos;
- futuro, possibilidade, simplicidade, confiança e escala ampla/global devem orientar a percepção;
- a Pessoa é a perspectiva predominante;
- possibilidade vem antes de produto;
- preserve a pergunta-mãe e a função dos onze movimentos;
- onze movimentos não significam onze seções visuais equivalentes;
- não abra a experiência com catálogo de produtos ou serviços;
- preserve autonomia e evite promessas de transformação garantida;
- conteúdo do Guivos Media pode fornecer evidência e matéria editorial, mas a Home mantém autoridade institucional;
- mantenha conteúdo institucional, evidência real, editorial e ação semanticamente distinguíveis;
- mobile deve preservar hierarquia, não apenas empilhar o desktop.

LIBERDADE DE DESIGN
Você pode propor grid, composição, dobras, agrupamentos, escala, ritmo, tipografia provisória, direção de imagem, fundos, componentes, Header, navegação, microinterações conceituais e comportamento responsivo.

NÃO INVENTE
Produtos, features, dados, métricas, parceiros, depoimentos, cases, campanhas, preços, avaliações, disponibilidade, provas sociais ou histórias reais. Use placeholders explicitamente rotulados quando necessário.

ANTI-TEMPLATE
Não transforme a Guivos em landing page SaaS, dashboard ou catálogo. Evite hero genérico + três benefícios + grade de cards + CTA final como solução automática. Busque uma experiência própria, narrativa, ampla e contemporânea.

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação breve de como os onze movimentos foram agrupados visualmente;
5. lista de hipóteses introduzidas;
6. lista de lacunas encontradas;
7. autoauditoria dos invariantes acima.

STATUS DA SAÍDA
EXPLORAÇÃO. Nada produzido nesta execução se torna canônico, aprovado ou requisito sem validação humana posterior contra o GKR.
```

---

## 10. Autoauditoria obrigatória daquela rodada

Antes de selecionar a direção como `CANDIDATO`, deveria ser verificado:

- a primeira leitura fala de possibilidade antes de produtos?;
- a Guivos parece ecossistema, não catálogo?;
- os produtos não dominaram a narrativa?;
- os onze movimentos continuam reconhecíveis em função, mesmo agrupados?;
- existe hierarquia real ou apenas blocos equivalentes?;
- conteúdo fictício está marcado?;
- o Media foi usado como fonte editorial, não como dono da Home?;
- mobile possui decisão própria?;
- a solução evita clichê SaaS?;
- acessibilidade e performance continuam plausíveis?;
- hipóteses estão separadas de requisitos?;
- nenhuma decisão nova de produto foi criada pela ferramenta?

---

## 11. Saída esperada naquela rodada

A rodada podia encerrar com:

```text
EXPLORAÇÃO
→ uma ou mais direções geradas

CANDIDATO
→ direção selecionada para revisão humana de UX
```

Ela não podia encerrar diretamente como `VALIDADO EM UI` ou `APROVADO PARA HANDOFF DE ENGENHARIA`.

---

## 12. Sequência prevista no checkpoint original

Depois da seleção de um candidato, a equipe deveria registrar:

- o que foi aceito;
- o que foi rejeitado;
- hipóteses resolvidas;
- decisões novas que exigissem governança;
- se o checkpoint das fontes continuava vigente.

Somente então deveria ser criado o Source Lock da etapa de UX detalhada ou direção visual/UI.

> **Essa sequência descreve a governança prevista para a rodada de 13/08. Ela não é o próximo passo governado atual.**

O próximo movimento atual continua sendo a auditoria integral do GKR. Qualquer retomada de Design deverá partir do estado canônico vigente depois do gate correspondente.

---

## 13. Síntese preservada do checkpoint

A formulação que orientou a rodada foi:

> **Na Home Pública da Pessoa, a ferramenta pode explorar como tornar possibilidade visível; não pode redefinir o que a Guivos significa nem transformar seus produtos no ponto de partida da experiência.**

A leitura atual acrescenta:

> **O Source Lock preserva como aquela exploração foi governada; ele não autoriza repetir a exploração com fontes superadas.**

---

## 14. Gate para qualquer futura retomada de Design

Antes de uma nova rodada de materialização da Home Pessoa, devem ser comprovados, no mínimo:

1. autorização explícita para retomar Design;
2. checkpoint canônico atual identificado;
3. `GKR-UX-HOME-MASTER-001` vigente incluído como fonte;
4. diferenças em relação ao Source Lock anterior reconciliadas;
5. documentos especializados necessários classificados como vigentes/evidência;
6. claims e disponibilidade operacional reconciliados quando materialmente afetados;
7. novo Source Lock ou reconciliação formal equivalente;
8. saída novamente limitada à maturidade autorizada para aquela rodada.

```text
DESIGN ANTERIOR EXISTE
≠ DESIGN ATUAL AUTORIZADO

SOURCE LOCK ANTERIOR EXISTE
≠ SOURCE LOCK AINDA VIGENTE PARA EXECUÇÃO
```
