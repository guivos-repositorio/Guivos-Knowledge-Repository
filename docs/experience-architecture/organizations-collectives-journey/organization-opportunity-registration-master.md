---
id: GKR-UX-ORG-OPPORTUNITY-REGISTRATION-MASTER-001
title: Jornada de Organizações e Coletivos — Organização — Cadastro de Oportunidade / Programa — Documento Mestre de Superfície
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-ORG-001
  - GKR-SURF-ORG-002
  - GKR-SURF-ORG-003
  - GKR-TRN-201
  - GKR-TRN-202
  - GKR-JOURNEY-ORGANIZATION-001
---

# Organização — Cadastro de Oportunidade / Programa — Documento Mestre de Superfície

## 1. Responsabilidade

Este Documento Mestre governa a responsabilidade funcional de `GKR-SURF-ORG-002` — **cadastro de oportunidade / programa pela Organização**.

Sua função é permitir que uma Pessoa com autoridade institucional legítima **crie, revise, preserve como rascunho, envie ou cancele um cadastro**, compreendendo as condições materiais que serão submetidas antes de qualquer ativação.

```text
ORG-001 — VISÃO GERAL
↓
TRN-201
↓
ORG-002 — CADASTRO / REVISÃO / ENVIO
↓
TRN-202
↓
ORG-003 — APROVADA / ATIVA
```

Este Master não absorve `ORG-003`. Cadastro e publicação ativa possuem responsabilidades e estados distintos.

```text
CADASTRAR
≠ APROVAR
≠ ATIVAR
≠ DISTRIBUIR
≠ GERAR RELEVÂNCIA
≠ GERAR IMPACTO
```

## 2. Por que esta responsabilidade é específica de Organização

A arquitetura conjunta permite Masters compartilhados somente quando job, responsabilidade e continuidade forem equivalentes.

Neste caso, `ORG-J04` e `ORG-002` sustentam uma responsabilidade institucional própria. O Coletivo possui atividades, oportunidades e governança em autoridades diferentes, sem uma superfície estável equivalente a `ORG-002`.

Portanto:

```text
RESPONSABILIDADE PRÓPRIA DA ORGANIZAÇÃO
→ MASTER ESPECÍFICO

AUSÊNCIA DE EQUIVALENTE NO COLETIVO
→ NÃO DUPLICAR
→ NÃO INVENTAR
→ NÃO FORÇAR PARIDADE
```

## 3. Participante, contexto e autoridade

O agente humano é uma Pessoa autenticada atuando em contexto de Organização.

A entrada exige:

- Organização ativa e identificável;
- unidade/contexto institucional quando aplicável;
- representação institucional válida;
- autoridade compatível com a ação pretendida;
- aprovação adicional quando a autoridade corrente assim exigir.

A superfície deve distinguir acesso, edição, envio e aprovação.

```text
ACESSAR
≠ EDITAR

EDITAR
≠ ENVIAR

ENVIAR
≠ APROVAR

REPRESENTAR
≠ AUTORIDADE IRRESTRITA
```

Quando a autoridade for insuficiente, a experiência deve preservar o trabalho permitido sem simular capacidade inexistente.

## 4. Origens e destinos legítimos

### Origem principal

A continuidade registrada é:

- `GKR-TRN-201` — `ORG-001 → ORG-002`, com maturidade própria preservada.

O cadastro também pode ser retomado a partir de rascunho ou continuidade institucional já autorizada quando a fonte de verdade sustentar esse estado.

### Destino principal

- `GKR-TRN-202` — `ORG-002 → ORG-003`, preservando sua maturidade corrente.

A navegação para `ORG-003` não pode ocorrer como se a ativação estivesse confirmada antes do resultado real do processo aplicável.

Este Master não cria transições adicionais.

## 5. Job principal

A Pessoa autorizada deve conseguir:

1. compreender o que está cadastrando e em nome de qual Organização;
2. informar ou revisar os dados materiais necessários;
3. identificar campos ausentes, inválidos, contestados ou dependentes de confirmação;
4. compreender condições, riscos e responsabilidades antes do envio;
5. salvar rascunho quando permitido;
6. revisar antes de submeter;
7. enviar somente com autoridade suficiente;
8. cancelar ou retirar a intenção antes de efeito material, quando o estado permitir;
9. compreender o resultado sem confundir envio com aprovação ou ativação.

## 6. Informação e dados

O contrato corrente admite, quando aplicável e sustentado pela autoridade de origem:

- identidade da Organização responsável;
- responsável institucional;
- identificação e descrição da oportunidade ou programa;
- disponibilidade e vigência;
- preço ou condição econômica, quando houver;
- elegibilidade;
- condições materiais;
- riscos;
- relação comercial aplicável;
- evidências ou referências necessárias;
- estado do cadastro;
- informação sobre aprovação aplicável.

Somente dados necessários ao cadastro e à decisão legítima devem ser capturados.

Nenhum campo pode ser inventado por convenção de mercado ou conveniência do protótipo.

## 7. Proveniência e qualidade da informação

Informação deve permanecer distinguível quando for:

- declarada pela Organização;
- proveniente de fonte externa autorizada;
- inferida;
- desconhecida;
- desatualizada;
- contestada;
- ainda não confirmada.

```text
INFORMAÇÃO DECLARADA
≠ INFORMAÇÃO VERIFICADA

INFERÊNCIA
≠ FATO

AUSÊNCIA DE DADO
≠ ZERO
≠ NÃO APLICÁVEL
```

## 8. Estados mínimos

A responsabilidade deve suportar, quando aplicável:

- novo cadastro;
- rascunho;
- rascunho incompleto;
- dados válidos para revisão;
- informação material ausente;
- informação inválida;
- informação contestada;
- autoridade insuficiente;
- aprovação adicional necessária;
- pronto para envio;
- envio em processamento;
- envio confirmado;
- envio com falha recuperável;
- resultado indeterminado;
- cancelado antes do envio;
- retirado quando o ciclo vigente permitir;
- dependência indisponível;
- contexto ou sessão expirados;
- atualização concorrente.

O Design pode materializar esses estados de formas diferentes, desde que preserve seu significado.

## 9. Ações e controles

A superfície pode oferecer, conforme estado e autoridade:

- iniciar cadastro;
- editar;
- revisar;
- salvar rascunho;
- retomar rascunho;
- corrigir informação;
- remover informação ainda não submetida quando permitido;
- cancelar;
- enviar para o próximo estágio;
- retornar sem enviar;
- revalidar contexto/autoridade;
- tentar novamente após falha recuperável.

Ações destrutivas ou materiais exigem clareza proporcional ao efeito.

Não deve existir pré-seleção silenciosa que converta preenchimento em publicação.

## 10. Revisão antes do envio

Antes de um envio material, a Pessoa deve conseguir compreender:

- o que será submetido;
- em nome de qual Organização;
- quais condições materiais estão vigentes;
- quais informações ainda possuem incerteza relevante;
- qual autoridade está sendo exercida;
- qual é o próximo estágio conhecido;
- o que o envio **não** garante.

```text
REVISÃO
→ COMPREENSÃO ANTES DO EFEITO

ENVIO
≠ APROVAÇÃO
≠ PUBLICAÇÃO ATIVA
≠ DESCOBERTA GARANTIDA
```

## 11. Processamento e feedback

O envio deve preservar:

```text
INTENÇÃO
→ CONFIRMAÇÃO CONSCIENTE
→ PROCESSAMENTO
→ SUCESSO CONFIRMADO
OU
→ FALHA RECUPERÁVEL
OU
→ ESTADO INDETERMINADO
```

`INTENÇÃO ≠ PROCESSAMENTO ≠ SUCESSO`.

Retry não pode duplicar cadastro ou efeito material.

Quando o resultado estiver indeterminado, a experiência deve reconsultar a fonte de verdade antes de convidar a repetir a ação.

## 12. Vazio, erro, indisponibilidade e recuperação

A experiência deve tratar explicitamente:

- ausência de rascunhos;
- informação obrigatória ausente;
- dado inválido;
- dependência externa indisponível;
- perda ou expiração de autoridade;
- sessão expirada;
- conflito de atualização;
- falha de processamento;
- estado de resultado ainda desconhecido.

Nenhum erro técnico deve ser apresentado como falha institucional da Organização.

Quando seguro, conteúdo já informado deve ser preservado para recuperação.

## 13. Reversibilidade, interrupção e retorno

Antes de envio confirmado, deve ser possível retornar ou interromper sem mutação silenciosa, respeitando o estado real.

Quando o contrato permitir:

- rascunho pode ser salvo;
- rascunho pode ser descartado conscientemente;
- cadastro pode ser cancelado antes do envio;
- cadastro submetido pode seguir regras próprias de retirada/correção conforme seu estado.

```text
VOLTAR
≠ ENVIAR

FECHAR
≠ DESCARTAR AUTOMATICAMENTE

CANCELAR INTENÇÃO
≠ APAGAR HISTÓRICO LEGÍTIMO
```

## 14. Continuidade com ORG-003 e descoberta

`ORG-003` governa a oportunidade aprovada/ativa e permanece fora desta responsabilidade.

Somente quando o estado real e a autoridade aplicável sustentarem a continuidade, `TRN-202` pode levar ao estágio correspondente.

A descoberta pela Pessoa permanece separada e usa autoridades próprias, inclusive `TRN-203` no recorte já validado.

```text
ORG-002
→ CADASTRO

ORG-003
→ ESTADO INSTITUCIONAL APROVADO / ATIVO

PER-201...
→ DESCOBERTA PELA PESSOA

PERSPECTIVAS
→ NÃO SE FUNDem
```

## 15. Relação com Planos e capacidade

Plano comercial pode afetar capacidade somente quando uma autoridade específica sustentar o limite.

Este Master não pode:

- inventar quota;
- inventar entitlement;
- bloquear cadastro por limite não documentado;
- alterar relevância orgânica;
- converter cadastro em upsell;
- inferir que pagamento garante distribuição, relevância ou resultado.

Se uma limitação legítima de capacidade for encontrada, a continuidade para Planos deve seguir a autoridade própria, preservando alternativas existentes.

## 16. Privacidade, proteção e minimização

O cadastro deve capturar e exibir somente informação necessária à finalidade legítima.

Dados pessoais ou sensíveis não se tornam institucionais apenas por estarem associados a uma oportunidade.

A Organização não recebe, por publicar uma oportunidade, acesso adicional ao contexto individual de Pessoas.

## 17. Acessibilidade

Estado, obrigatoriedade, erro, autoridade, risco, processamento e confirmação não podem depender exclusivamente de:

- cor;
- ícone;
- posição;
- animação;
- hover;
- blur;
- densidade visual.

Revisão e confirmação devem ser compreensíveis por tecnologia assistiva e navegação sem apontador.

## 18. Liberdade de Design

Design mantém liberdade sobre:

- composição;
- grid;
- navegação local;
- componentes;
- progressão visual;
- quantidade de frames;
- tipografia dentro da autoridade oficial de marca;
- imagens e ícones;
- densidade;
- motion;
- solução responsiva.

Essa liberdade não autoriza:

- transformar o fluxo em wizard obrigatório sem fundamento;
- inventar etapas;
- inventar campos;
- inventar aprovação;
- esconder condição material;
- declarar sucesso antes de confirmação;
- fundir `ORG-002` e `ORG-003`;
- usar publicação como promessa de relevância ou impacto.

O low-fidelity existente pode ser consumido como evidência funcional, não como baseline visual obrigatório.

## 19. IA e prototipação — source lock

IA pode explorar forma para materializar este contrato, mas não pode inventar:

- campos;
- estados;
- ações;
- transições;
- automações;
- validações materiais;
- critérios de elegibilidade;
- integrações;
- notificações;
- métricas;
- recomendações;
- permissões;
- entitlements;
- regras de plano;
- persistência.

```text
GKR
→ FONTE DE VERDADE

IA
→ CONSUMIDORA

LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 20. Critérios de aceite

O contrato é preservado quando a materialização futura:

1. identifica claramente a Organização e o contexto ativo;
2. verifica autoridade antes de ação material;
3. mantém `ORG-002` separado de `ORG-003`;
4. permite compreender, preencher e revisar os dados materiais sustentados pelas autoridades;
5. preserva rascunho/cancelamento/retorno conforme estado;
6. não confunde envio com aprovação ou ativação;
7. distingue informação declarada, inferida, desconhecida e contestada quando aplicável;
8. trata falha e resultado indeterminado sem duplicar efeito;
9. não inventa quota, entitlement ou regra de plano;
10. não promete distribuição, relevância ou impacto;
11. preserva privacidade e minimização;
12. não transforma low-fidelity em baseline visual obrigatório;
13. não amplia escopo por IA;
14. não promove maturidade de `ORG-002`, `TRN-201` ou `TRN-202`.

## 21. Lacunas preservadas

Este Master não resolve por inferência:

- integração técnica final com descoberta;
- materialização high-fidelity final;
- regras técnicas de RBAC;
- persistência;
- integrações externas;
- notificações;
- critérios adicionais não documentados;
- entitlement técnico;
- implementação;
- Product Engineering.

Lacunas devem permanecer explícitas até autoridade própria.

## 22. Estado documental

```text
MASTER
→ DRAFT / FUNCTIONAL CONTRACT CANDIDATE

SURFACE GOVERNED
→ GKR-SURF-ORG-002

ORIGIN
→ GKR-SURF-ORG-001 / GKR-TRN-201

NEXT RESPONSIBILITY
→ GKR-SURF-ORG-003 / GKR-TRN-202

COLLECTIVE EQUIVALENT
→ NONE BY INFERENCE

NEW SURFACE ID
→ NONE

NEW TRANSITION ID
→ NONE

MATURITY PROMOTION
→ NONE

LOW-FIDELITY
→ FUNCTIONAL EVIDENCE / NOT VISUAL BASELINE

PROTOTYPE
→ NOT AUTHORIZED BY THIS MASTER

PRODUCT ENGINEERING
→ NOT RELEASED
```
