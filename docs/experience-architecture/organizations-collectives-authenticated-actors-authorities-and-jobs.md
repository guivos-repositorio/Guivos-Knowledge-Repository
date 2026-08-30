---
id: GKR-UX-ORGCOL-AUTH-JOBS-001
title: Organizações e Coletivos — Atores, Autoridades e Jobs Prioritários da Experiência Autenticada
status: active
version: 1.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-30
normative: false
maturity: authenticated_information_architecture_defined_pre_surface_map
depends_on:
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - UXA-014
  - UXA-019
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-UX-ORGCOL-SUPPLY-VALUE-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - RP-002
  - RP-002-OCE-001
  - RP-002-PMF-001
---

# Organizações e Coletivos — Atores, Autoridades e Jobs Prioritários da Experiência Autenticada

## 1. Finalidade

Este documento fechou a etapa imediatamente anterior à **Arquitetura da Informação** da experiência autenticada de Organizações e Coletivos.

Após a validação deste incremento, `GKR-UX-ORGCOL-AUTH-IA-001` definiu a Arquitetura da Informação autenticada no estágio **pre-surface-map**. Este documento permanece `active` como autoridade dos atores, limites e jobs que alimentam essa IA; não volta a classificar a IA como pendente.

Ele reconcilia os fundamentos e contratos vigentes para responder quatro perguntas:

1. quem atua na experiência autenticada;
2. em nome de qual participante e contexto essa atuação ocorre;
3. que tipo de autoridade precisa estar explícita;
4. quais jobs precisam ser suportados antes de decidir navegação, superfícies ou wireframes.

Este documento não define menu, dashboard, tela inicial, componentes, permissões técnicas, RBAC, wireframe, UI ou implementação. A definição posterior da IA permanece governada por `GKR-UX-ORGCOL-AUTH-IA-001`.

```text
ATOR FUNCIONAL
≠ CONTA TÉCNICA
≠ ROLE DE RBAC
≠ PERMISSÃO IMPLEMENTADA

JOB PRIORITÁRIO
≠ ITEM DE MENU
≠ TELA
≠ COMPONENTE

AUTORIDADE DECLARADA
≠ AUTORIDADE VERIFICADA TECNICAMENTE
```

## 2. Baseline reconciliada

A frente parte das seguintes autoridades e estados:

- `UXA-014` define Organização, Coletivo e suas responsabilidades funcionais;
- `UXA-019` define autoridade bilateral, limites, compromissos, recursos, dados, contestação e ciclo de vida das relações Organização ↔ Coletivo;
- `GKR-JOURNEY-ORGANIZATION-001` preserva a Jornada da Organização em `draft` e maturidades independentes de fluxos especializados;
- `GKR-JOURNEY-COLLECTIVE-001` preserva a Jornada do Coletivo em `draft` e maturidades independentes de fluxos especializados;
- `GKR-UX-ORGCOL-UX-STATE-001` preserva o baseline histórico no qual a arquitetura da informação e os wireframes principais autenticados ainda não estavam definidos;
- `GKR-UX-ORGCOL-AUTH-IA-001` define a Arquitetura da Informação autenticada de Organização e Coletivo em estado **defined pre-surface-map**, sem materializar wireframes, UI ou implementação;
- `GKR-UX-ORGCOL-SUPPLY-VALUE-001` fornece Research sobre supply, relevância e papéis sem transformar Research em Canon ou PMF.

A sequência governada permanece:

```text
fundamentos e papéis
→ atores, autoridades e jobs prioritários
→ arquitetura da informação
→ mapa de superfícies e estados
→ fluxos prioritários
→ wireframes de baixa fidelidade
→ validação funcional
→ UI
→ protótipo
→ testes
→ handoff técnico
```

No estado corrente, atores/autoridades/jobs e Arquitetura da Informação já estão definidos documentalmente; o próximo gap começa no mapa final de superfícies e estados. Nenhuma etapa seguinte é iniciada automaticamente.

## 3. Unidade de atuação autenticada

A experiência não deve partir da ideia genérica de “usuário da Organização” ou “usuário do Coletivo”.

A unidade funcional mínima é:

```text
PESSOA AUTENTICADA
+
PARTICIPANTE REPRESENTADO
+
CONTEXTO / UNIDADE APLICÁVEL
+
PAPEL DECLARADO
+
AUTORIDADE E LIMITES
+
JOB ATUAL
```

A mesma Pessoa poderá atuar em contextos diferentes, mas a experiência não deve fundir silenciosamente autoridades.

Exemplos conceituais:

```text
Pessoa A
→ representa Organização X / Unidade Y
→ possui determinado escopo institucional

Pessoa A
→ também participa de Coletivo Z
→ possui outro papel e outra autoridade
```

```text
MESMA PESSOA
≠ MESMA AUTORIDADE

PERTENCIMENTO
≠ REPRESENTAÇÃO

REPRESENTAÇÃO
≠ APROVAÇÃO IRRESTRITA
```

## 4. Classes funcionais de atores — Organização

As classes abaixo são lógicas. Uma mesma Pessoa poderá acumular mais de uma classe quando isso for legítimo, e uma implementação futura poderá decompor ou combinar papéis de outra forma.

### 4.1 Representante institucional autenticado

Pessoa que atua em nome de uma Organização ou unidade institucional dentro do escopo que lhe foi concedido.

Precisa compreender:

- qual Organização/unidade está representando;
- qual papel está ativo;
- até onde pode agir;
- quais decisões exigem outra autoridade;
- quais responsabilidades assumiu;
- como trocar de contexto sem transportar autoridade indevida.

Não recebe autoridade geral sobre toda a Organização por estar autenticado.

### 4.2 Autoridade institucional de aprovação

Pessoa ou instância legitimamente capaz de aprovar atos materiais conforme o contexto, por exemplo:

- relações com Coletivos;
- compromissos institucionais;
- recursos e condições econômicas;
- alterações materiais de escopo;
- usos de dados ou marca quando exigirem aprovação;
- decisões que ultrapassem o limite do representante operacional.

Essa classe funcional não presume que toda aprovação pertença à mesma pessoa ou instância.

### 4.3 Responsável operacional / de prestação de contas

Pessoa ou papel responsável por acompanhar execução, compromissos, riscos, prazos, evidências e correções dentro do escopo atribuído.

Responsabilidade operacional não equivale automaticamente a poder de aprovação material.

### 4.4 Contraparte autorizada

Quando a Organização atua em relação com um Coletivo ou outra Organização, a contraparte é um participante distinto com autoridade própria.

A experiência deve preservar bilateralidade e não transformar a contraparte em recurso interno da Organização.

## 5. Classes funcionais de atores — Coletivo

### 5.1 Responsável / representante autorizado do Coletivo

Pessoa que atua em nome do Coletivo dentro das regras de governança aplicáveis.

Precisa compreender:

- qual Coletivo está representando;
- qual papel possui;
- que decisões pode tomar;
- que decisões exigem consulta ou aprovação adicional;
- quais limites de representação existem;
- como contestação e revisão podem ocorrer.

### 5.2 Instância de governança / decisão coletiva

Pessoa, conjunto de pessoas ou mecanismo legitimamente definido pelo Coletivo para decisões que não pertencem a um representante isolado.

A experiência deve permitir que decisões materiais continuem vinculadas à regra de governança aplicável, e não à simples posse de acesso técnico.

### 5.3 Responsável por operação, moderação ou proteção

Papel legitimamente atribuído para tarefas como:

- organização de atividades;
- gestão de solicitações;
- moderação;
- proteção;
- acessibilidade;
- comunicação oficial;
- acompanhamento de compromissos.

Receber uma função não concede autoridade fora dela.

### 5.4 Participante do Coletivo

Pessoa que pertence ou participa legitimamente do Coletivo.

Participação não significa automaticamente:

- administração;
- moderação;
- representação;
- consentimento para toda decisão;
- autorização para dados de outros membros;
- obrigação de atividade permanente.

Os fluxos da Pessoa participante já possuem maturidades próprias e não devem ser confundidos com a futura experiência principal do responsável pelo Coletivo.

### 5.5 Contraparte autorizada

Organizações ou outros Coletivos relacionados permanecem participantes externos ao governo interno do Coletivo, salvo delegação explícita e limitada.

Apoio, financiamento, infraestrutura ou patrocínio não transferem automaticamente governança.

## 6. Papel funcional da Guivos

Na experiência autenticada, a Guivos poderá organizar contexto, informação, evidências, estados, riscos e Próximos Passos dentro das autoridades vigentes.

A Guivos poderá apoiar funções como:

- identificação do contexto ativo;
- explicação de atenção material;
- organização de informações confirmadas, externas, inferidas, desconhecidas ou contestadas;
- verificação quando houver autoridade própria;
- suporte a moderação, proteção e processos de contestação quando aplicável;
- explicação de alternativas e Próximos Passos;
- preservação de rastreabilidade.

A Guivos não assume automaticamente:

- direção da Organização;
- governo do Coletivo;
- autoridade jurídica dos participantes;
- poder de aprovar compromissos em nome deles;
- poder de consentir em nome de Pessoas;
- decisão final sobre objetivos pessoais;
- prova de impacto sem evidência suficiente.

```text
GUIVOS ORGANIZA A EXPERIÊNCIA
≠ GUIVOS SUBSTITUI A AUTORIDADE DO PARTICIPANTE
```

## 7. Matriz de autoridade — princípios mínimos

| Ato funcional | Organização | Coletivo | Regra preservada |
|---|---|---|---|
| visualizar contexto próprio autorizado | representante dentro do escopo | responsável/participante dentro do escopo | acesso depende de contexto e finalidade |
| corrigir informação própria | papel autorizado | papel autorizado | correção deve preservar rastreabilidade quando necessária |
| publicar/operar oportunidade ou atividade | papel legitimamente autorizado | papel legitimamente autorizado | publicação não compra relevância |
| aprovar relação bilateral | autoridade institucional aplicável | autoridade coletiva aplicável | mesmo escopo deve ser aprovado pelas duas partes |
| assumir compromisso | autoridade compatível com obrigação | autoridade compatível com governança | presença ou silêncio não equivalem a aceite |
| ampliar dados/recursos/escopo | nova aprovação quando material | nova aprovação quando material | alteração material exige reavaliação |
| contestar / solicitar revisão | participante autorizado afetado | participante autorizado afetado | contestação não pode gerar retaliação |
| pausar / encerrar relação | conforme autoridade e contrato | conforme autoridade e governança | saída deve tratar obrigações remanescentes |
| acessar contexto pessoal protegido | não por padrão | não por padrão | relação institucional/coletiva não amplia finalidade automaticamente |

Essa matriz é funcional e não substitui futura matriz técnica de permissões.

## 8. Jobs prioritários — Organização

Os jobs abaixo expressam o que a experiência precisa permitir realizar. A ordem não define navegação nem posição visual.

### ORG-J01 — Compreender em qual contexto institucional estou atuando

A pessoa autenticada precisa saber:

- Organização e unidade;
- papel atual;
- autoridade e limites;
- responsabilidades relevantes;
- quando uma ação exige outra aprovação.

**Criticidade:** estrutural.

### ORG-J02 — Entender o Momento institucional e a atenção material atual

A pessoa precisa compreender:

- o que está acontecendo agora;
- qual ponto exige responsabilidade;
- por que exige atenção;
- que informação sustenta a leitura;
- o que permanece desconhecido, inferido ou contestado.

**Criticidade:** estrutural.

### ORG-J03 — Manter identidade, capacidade, condições e responsabilidades materialmente corretas

Inclui corrigir ou atualizar informações autorizadas sobre:

- identidade/unidade;
- capacidade e disponibilidade;
- obrigações e prazos;
- riscos;
- limitações;
- informações necessárias para oportunidades e programas.

**Criticidade:** núcleo operacional.

### ORG-J04 — Criar e acompanhar oportunidades e programas legítimos

A experiência deve permitir operar o ciclo aplicável sem confundir publicação com distribuição, relevância ou impacto.

Fluxos especializados já validados preservam sua autoridade própria e devem ser reutilizados pela futura arquitetura quando aplicável, não reconstruídos por inferência.

**Criticidade:** núcleo operacional.

### ORG-J05 — Gerir relações com Coletivos e Organizações sem perder bilateralidade

Inclui compreender e atuar sobre:

- finalidade;
- autoridades;
- compromissos;
- recursos;
- dados;
- marca e condições econômicas;
- riscos e conflitos;
- revisão, ajuste, pausa ou encerramento.

**Criticidade:** núcleo operacional.

### ORG-J06 — Acompanhar compromissos, evidências e resultados sem fabricar impacto

A pessoa precisa distinguir:

- execução;
- evidência;
- contribuição provável;
- limitações;
- fatores externos;
- resultado autorizado;
- ausência de evidência suficiente.

**Criticidade:** continuidade e prestação de contas.

### ORG-J07 — Compreender capacidade comercial e Planos quando o contexto exigir

O fluxo especializado de Planos já possui maturidade própria.

A futura experiência principal deve conseguir chegar a esse fluxo e retornar dele sem tratar plano maior como maior relevância, autoridade, legitimidade ou acesso a dados pessoais.

**Criticidade:** especializada / contextual.

### ORG-J08 — Corrigir, contestar, revisar, pausar ou encerrar quando necessário

A experiência deve preservar ação legítima diante de:

- informação incorreta;
- autoridade insuficiente;
- risco;
- conflito;
- compromisso inviável;
- relação contestada;
- mudança material;
- necessidade de saída.

**Criticidade:** proteção e governança.

### ORG-J09 — Entender o Próximo Passo e quem possui autoridade para realizá-lo

Todo Próximo Passo material precisa explicar:

- contexto;
- motivo;
- evidência/incerteza;
- contribuição esperada;
- alternativas;
- autoridade exigida;
- responsável apenas quando houver atribuição legítima.

**Criticidade:** estrutural.

## 9. Jobs prioritários — Coletivo

### COL-J01 — Compreender em qual contexto coletivo estou atuando

A pessoa autenticada precisa saber:

- Coletivo;
- propósito;
- papel atual;
- autoridade e limites;
- regra de governança aplicável quando material.

**Criticidade:** estrutural.

### COL-J02 — Entender o Momento coletivo e a atenção material atual

A experiência precisa tornar compreensíveis:

- situação atual;
- necessidade ou decisão aberta;
- atenção principal e motivo;
- próxima atividade ou ação relevante;
- informação desconhecida, contestada ou ainda não decidida.

**Criticidade:** estrutural.

### COL-J03 — Coordenar atividades, ações, recursos e necessidades do propósito compartilhado

Inclui organizar o que está em movimento sem reduzir o Coletivo a agenda ou feed.

A experiência deve preservar voluntariedade e distinguir necessidade coletiva de obrigação individual.

**Criticidade:** núcleo operacional.

### COL-J04 — Gerir participação, solicitações, papéis e vínculos legitimamente

Fluxos especializados existentes de solicitação e gestão preservam suas maturidades próprias.

A futura arquitetura principal deve integrá-los sem presumir que pertencimento conceda função, moderação ou autoridade.

**Criticidade:** núcleo operacional.

### COL-J05 — Governar decisões, comunicação, moderação e proteção

A experiência precisa suportar os mecanismos legítimos do Coletivo para:

- decisões;
- comunicação oficial;
- consulta quando aplicável;
- moderação;
- proteção;
- acessibilidade;
- contestação;
- não retaliação.

**Criticidade:** proteção e governança.

### COL-J06 — Criar e acompanhar oportunidades ou atividades legítimas

Quando o Coletivo atua como provider, enabler ou criador de supply, a experiência deve permitir operação responsável sem confundir popularidade, volume ou plano pago com relevância ou impacto.

**Criticidade:** núcleo operacional.

### COL-J07 — Gerir relações com Organizações e outros Coletivos preservando autonomia

Inclui finalidade, autoridade, compromissos, recursos, dados, influência, patrocínio, riscos, revisão e saída.

Apoio externo não transforma o Coletivo em propriedade ou canal institucional da contraparte.

**Criticidade:** núcleo operacional.

### COL-J08 — Acompanhar avanço, aprendizado e evidências coletivas sem transformar atividade em impacto

A experiência deve ajudar a distinguir:

- atividade realizada;
- participação legítima;
- aprendizado;
- contribuição;
- evidência;
- limitação;
- resultado ainda não confirmado.

**Criticidade:** continuidade e prestação de contas.

### COL-J09 — Compreender capacidade e Planos quando o contexto exigir

O fluxo especializado de Planos preserva maturidade própria.

A arquitetura futura deve permitir entrada e retorno sem fazer do plano pago um atalho de legitimidade, relevância ou autoridade.

**Criticidade:** especializada / contextual.

### COL-J10 — Corrigir, contestar, revisar, pausar ou encerrar quando necessário

Inclui proteger:

- revisão de informação;
- contestação de decisão ou evidência;
- revisão de relação;
- suspensão proporcional;
- saída legítima;
- encerramento responsável;
- obrigações remanescentes.

**Criticidade:** proteção e governança.

### COL-J11 — Entender o Próximo Passo e qual decisão coletiva ou autoridade ele exige

O Próximo Passo deve ser justificável, corrigível e compatível com a regra de governança do Coletivo.

**Criticidade:** estrutural.

## 10. Jobs bilaterais Organização ↔ Coletivo

Alguns jobs não pertencem exclusivamente a uma das experiências e precisam permanecer sincronizados entre os dois participantes.

### BIL-J01 — Propor uma relação com finalidade e escopo claros

Nenhum compromisso nasce apenas da intenção unilateral.

### BIL-J02 — Avaliar autoridade, capacidade, riscos e condições

Cada participante deve poder avaliar a proposta a partir de sua própria autoridade.

### BIL-J03 — Negociar alterações materiais com rastreabilidade

Mudança material não pode ser absorvida silenciosamente.

### BIL-J04 — Aprovar o mesmo escopo pelas duas autoridades legítimas

Silêncio, reunião, repasse de recurso ou uso informal de marca não equivalem a consentimento.

### BIL-J05 — Acompanhar compromissos e evidências

A leitura de execução precisa preservar contribuição, limitações e fatores externos.

### BIL-J06 — Revisar, contestar, pausar ou encerrar

Cada lado precisa compreender direitos, consequências e obrigações remanescentes.

## 11. Jobs que não devem dominar a experiência principal

A experiência autenticada não deve ser organizada prioritariamente em torno de:

### Organização

- vendas;
- receita isolada;
- número de anúncios;
- visualizações;
- seguidores;
- quantidade de oportunidades publicadas;
- compra de mídia.

### Coletivo

- feed;
- curtidas;
- ranking de membros;
- streaks;
- volume de publicações;
- quantidade bruta de membros;
- notificações como finalidade;
- permanência compulsória.

Esses sinais podem existir quando legitimamente úteis, mas não substituem propósito, responsabilidade, contexto, evidência ou Próximo Passo.

## 12. Restrições preservadas pela Arquitetura da Informação

A Arquitetura da Informação autenticada vigente, definida por `GKR-UX-ORGCOL-AUTH-IA-001`, preserva no mínimo estas restrições derivadas dos Jobs:

1. contexto ativo e autoridade precisam permanecer reconhecíveis;
2. Organização e Coletivo não podem compartilhar automaticamente a mesma estrutura apenas por possuírem funções semelhantes;
3. fluxos especializados já validados devem preservar autoridade e maturidade próprias;
4. relações bilaterais precisam aparecer coerentemente para os dois lados sem criar propriedade ou subordinação;
5. informação pessoal protegida não pode surgir por inferência de vínculo institucional, coletivo, comercial ou patrocinado;
6. atenção material precisa ser explicável e contestável;
7. Próximos Passos devem identificar autoridade necessária;
8. estados de risco, bloqueio, divergência, ausência de autoridade, pausa e encerramento precisam ser suportáveis;
9. Planos devem permanecer capacidade comercial especializada, não eixo de relevância ou identidade;
10. a experiência principal não pode ser um dashboard comercial genérico da Organização nem um feed social genérico do Coletivo.

Essas restrições não materializam categorias de menu, surface map final, wireframes ou superfícies.

## 13. Decisões explicitamente adiadas

Este documento não decide:

- arquitetura final de navegação;
- agrupamento de conteúdo;
- menu global ou local;
- quantidade de superfícies;
- nome final das superfícies;
- dashboard;
- Home autenticada;
- ordem visual;
- widgets/cards;
- modelo final de permissões;
- convite/gestão técnica de usuários;
- componentes;
- desktop/mobile;
- wireframe;
- UI;
- protótipo;
- implementação.

Também não reativa `UXA-015..018` e não inicia `UXA-102/V5`.

## 14. Gate histórico de IA e estado corrente

O gate originalmente registrado para iniciar a Arquitetura da Informação exigia que:

- atores funcionais estivessem distinguíveis;
- contexto representado estivesse distinguível;
- autoridade e limites estivessem explícitos conceitualmente;
- jobs estruturais, operacionais, de proteção e bilaterais estivessem registrados;
- fluxos especializados existentes estivessem identificados como inputs, não como UX principal pronta;
- decisões de tela e navegação continuassem não antecipadas.

Esse gate foi consumido pela definição posterior de `GKR-UX-ORGCOL-AUTH-IA-001`. O estado corrente é:

```text
FOUNDATIONS / ROLES
→ RECONCILED

FUNCTIONAL ACTORS
→ DEFINED FOR IA INPUT

AUTHORITY BOUNDARIES
→ DEFINED FOR IA INPUT

PRIORITY JOBS
→ DEFINED FOR IA INPUT

AUTHENTICATED INFORMATION ARCHITECTURE
→ DEFINED PRE-SURFACE-MAP

FINAL SURFACE MAP
→ NOT YET DEFINED

MAIN AUTHENTICATED WIREFRAMES
→ NOT YET DEFINED

UXA-102 / V5
→ NOT STARTED

PRODUCT ENGINEERING
→ PAUSED
```

## 15. Próximo ato documental permitido

Após a definição da Arquitetura da Informação autenticada, o próximo ato documental possível nesta frente, somente quando houver autorização específica, é:

> **definir o mapa final de superfícies e estados autenticados de Organização e Coletivo a partir da IA, destes atores, autoridades, jobs e contratos existentes.**

Esse próximo ato não está sendo iniciado por esta reconciliação e não deve produzir wireframe, UI, protótipo ou implementação.