---
id: GKR-UX-COL-REQUEST-MANAGEMENT-MASTER-001
title: Jornada de Organizações e Coletivos — Coletivo — Gestão de Solicitações — Documento Mestre de Superfície
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
  - GKR-SURF-COL-002
  - GKR-SURF-COL-003
  - GKR-SURF-COL-004
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-108
  - GKR-TRN-109
  - GKR-TRN-112
  - GKR-JOURNEY-COLLECTIVE-001
---

# Coletivo — Gestão de Solicitações — Documento Mestre de Superfície

## 1. Responsabilidade

Este Documento Mestre governa a responsabilidade funcional de `GKR-SURF-COL-003` — Gestão de Solicitações.

A superfície permite que uma Pessoa legitimamente autorizada, atuando no contexto de um Coletivo, compreenda e trate solicitações de participação sem confundir análise da solicitação com vínculo, representação, administração ou autoridade posterior.

```text
SOLICITAÇÃO
→ ANÁLISE SOB AUTORIDADE
→ DECISÃO OU PEDIDO LEGÍTIMO DE INFORMAÇÃO
→ CONTINUIDADE REGISTRADA QUANDO EXISTENTE

SOLICITAÇÃO
≠ PARTICIPAÇÃO ATIVA

APROVAÇÃO
≠ REPRESENTAÇÃO
≠ ADMINISTRAÇÃO
≠ AUTORIDADE IRRESTRITA
```

## 2. Por que esta responsabilidade é específica do Coletivo

`COL-003` pertence ao domínio **Participação** e atende a continuidade de `COL-J04`.

A Organização não possui superfície semanticamente equivalente para gerir entrada de participantes em um Coletivo. A família `ORG-004..006 / COL-008` governa relações bilaterais Organização–Coletivo e não deve ser usada como equivalente.

Consequentemente:

- este Master não é compartilhado por inferência;
- nenhuma superfície da Organização é criada para produzir simetria;
- relação bilateral não substitui participação;
- eventual equivalência futura exige autoridade própria.

## 3. Participante, contexto e autoridade

O agente humano é uma **Pessoa autenticada** atuando no contexto do Coletivo.

Antes de ação material, a experiência deve preservar:

- Coletivo ativo correto;
- papel e autoridade da Pessoa;
- escopo da solicitação;
- estado corrente da solicitação;
- informação e proteção aplicáveis;
- aprovação adicional quando legitimamente exigida.

```text
ACESSAR SOLICITAÇÕES
≠ DECIDIR

ANALISAR
≠ APROVAR

APROVAR
≠ ATRIBUIR PAPEL

PERTENCER
≠ REPRESENTAR
≠ ADMINISTRAR
```

Mudança de contexto, sessão expirada ou alteração de autoridade exige revalidação antes de efeito material.

## 4. Origens e continuidades legítimas

O Transition Registry permanece autoridade para as transições identificadas. Este Master consome, sem promover, a família especializada `GKR-TRN-105..109` e a entrada contextual `GKR-TRN-112`.

```text
CONTEXTO DO COLETIVO
→ GKR-TRN-112, QUANDO APLICÁVEL
→ GKR-SURF-COL-003

PERSPECTIVA DA PESSOA
→ GKR-SURF-PER-105 / AUTORIDADES RELACIONADAS
→ GKR-TRN-105..109, CONFORME O CONTRATO EXISTENTE
→ GKR-SURF-COL-003
```

A continuidade operacional após aprovação deve preservar uma lacuna conhecida:

```text
COL-003
→ COL-004

TRANSIÇÃO ESTÁVEL DEDICADA
→ NÃO REGISTRADA

TRATAMENTO
→ PRESERVAR A LACUNA
→ NÃO INVENTAR GKR-TRN
```

Aprovação em `COL-003` não autoriza declarar automaticamente que `COL-004` foi materializado, persistido ou atualizado.

## 5. Job principal

A Pessoa autorizada deve conseguir:

1. identificar o Coletivo e a solicitação sob análise;
2. compreender o estado corrente e a proveniência das informações disponíveis;
3. distinguir informação declarada, verificada, ausente, protegida, desatualizada ou contestada;
4. reconhecer sua autoridade e eventual necessidade de aprovação adicional;
5. analisar a solicitação sem acessar dados pessoais além do necessário;
6. aguardar legitimamente quando não houver base suficiente para decidir;
7. solicitar informação adicional quando sustentado pela autoridade;
8. aprovar ou recusar somente quando houver autoridade e base aplicáveis;
9. compreender o resultado confirmado, falha recuperável ou estado indeterminado;
10. retornar ao contexto do Coletivo sem duplicar decisão ou perder a referência canônica.

## 6. Informação e minimização

Quando sustentados pelas autoridades de origem, a responsabilidade pode apresentar:

- identidade suficiente da solicitação;
- Coletivo relacionado;
- estado e momento da solicitação;
- informação fornecida legitimamente para a finalidade;
- respostas ou evidências necessárias à decisão;
- proveniência e atualidade material;
- condições de participação aplicáveis;
- proteção ou restrição de acesso;
- histórico material necessário à compreensão e auditoria legítima;
- decisão e fundamento no limite permitido;
- informação adicional solicitada e seu estado.

A superfície não deve inventar nem exigir por convenção:

- score de candidato;
- ranking de solicitantes;
- recomendação automática de aprovação;
- probabilidade de sucesso;
- perfil psicológico;
- inferência sensível;
- dados não necessários à finalidade;
- comparação competitiva entre pessoas;
- autoridade decorrente de popularidade, plano ou atividade.

## 7. Proveniência e verdade operacional

```text
DECLARADO
≠ VERIFICADO

INFERIDO
≠ FATO

AUSÊNCIA DE DADO
≠ RESPOSTA NEGATIVA

INFORMAÇÃO ADICIONAL SOLICITADA
≠ OBRIGAÇÃO UNIVERSAL

CONTESTADO
≠ INVÁLIDO POR DEFINIÇÃO

DECISÃO REGISTRADA
≠ VÍNCULO TÉCNICO CONFIRMADO
```

A experiência não deve preencher lacunas com inferências silenciosas.

## 8. Estados mínimos

Quando aplicáveis, a materialização deve comportar:

- solicitação pendente;
- em análise;
- informação adicional necessária;
- aguardando resposta;
- autoridade insuficiente;
- aprovação adicional necessária;
- informação material incompleta;
- informação protegida;
- informação contestada;
- aprovada;
- recusada;
- retirada ou cancelada pela origem quando autoridade própria permitir;
- expirada quando houver condição de expiração legitimamente definida;
- bloqueada por proteção, privacidade ou governança;
- processamento em curso;
- falha recuperável;
- resultado indeterminado;
- atualização concorrente;
- contexto ou sessão expirados;
- dependência externa indisponível;
- operação degradada ou baixa conectividade.

```text
PENDENTE
≠ APROVADA

AGUARDANDO
≠ RECUSADA

BLOQUEADA
≠ RECUSADA

APROVADA
≠ VÍNCULO ATIVO CONFIRMADO

RECUSADA
≠ PUNIÇÃO
```

## 9. Ações e controles

Somente quando estado e autoridade permitirem, a responsabilidade pode oferecer:

- abrir e revisar solicitação;
- consultar informação material autorizada;
- solicitar informação adicional;
- registrar continuidade de análise;
- aprovar;
- recusar;
- retornar sem decidir;
- revalidar contexto e autoridade;
- reconsultar estado canônico;
- repetir processamento recuperável sem duplicar efeito.

Nenhum controle visual concede autoridade.

Ações materiais devem exigir confirmação proporcional e feedback explícito do resultado.

## 10. Solicitação de informação adicional

Solicitar informação adicional deve ser uma ação finalística, proporcional e necessária à decisão.

A experiência deve:

- tornar claro o que está sendo solicitado;
- preservar finalidade;
- não converter ausência em inferência negativa;
- não exigir dado sensível por convenção;
- permitir que a solicitação permaneça em estado compatível enquanto aguarda;
- distinguir resposta recebida de resposta validada;
- preservar proteção e minimização.

Este Master não inventa perguntas, campos ou documentos obrigatórios.

## 11. Aprovação e recusa

Aprovação e recusa são decisões materiais distintas.

### Aprovação

Aprovação significa que a solicitação recebeu decisão favorável no limite da autoridade aplicável. Ela não significa automaticamente:

- criação técnica de vínculo;
- atribuição de papel;
- representação;
- administração;
- acesso ampliado;
- consentimento para outras finalidades;
- comunicação pública.

### Recusa

Recusa deve:

- ser registrada como decisão no limite autorizado;
- preservar fundamento quando exigido e permitido;
- não produzir exposição indevida;
- não ser tratada como punição;
- preservar contestação ou revisão quando autoridade própria as prever.

Este Master não inventa política universal de recurso ou obrigação de justificativa onde ela não estiver governada.

## 12. Relação com a perspectiva da Pessoa

As superfícies `PER-103..108` permanecem responsabilidades da perspectiva da Pessoa.

`COL-003` administra a responsabilidade operacional do Coletivo; não absorve a experiência pessoal.

```text
PESSOA SOLICITANTE
→ CONTROLA SUA EXPERIÊNCIA SOB AUTORIDADES DA PESSOA

COLETIVO
→ CONTROLA A ANÁLISE SOB SUA AUTORIDADE LEGÍTIMA

COL-003
→ NÃO AUTORIZA ACESSO AO CONTEXTO PESSOAL AMPLO
→ NÃO AUTORIZA INFERÊNCIAS NÃO NECESSÁRIAS
```

## 13. Relação com COL-004 — Participantes e Vínculos

`COL-004` é responsabilidade distinta.

```text
COL-003
→ DECIDE A SOLICITAÇÃO

COL-004
→ GOVERNA PARTICIPANTES E VÍNCULOS NO LIMITE DE SUA AUTORIDADE

COL-003 → COL-004
→ GKR-TRN-114
→ CONTINUIDADE OPERACIONAL DO MESMO VÍNCULO JÁ FORMADO
→ CONTRATADA
```

`GKR-TRN-114` fecha a lacuna de identidade da continuidade, mas não trata aprovação como persistência técnica confirmada do vínculo e não duplica o efeito de `GKR-TRN-108`.

## 14. Processamento e confirmação

```text
INTENÇÃO
→ CONFIRMAÇÃO CONSCIENTE, QUANDO APLICÁVEL
→ PROCESSAMENTO
→ SUCESSO CONFIRMADO
  OU FALHA RECUPERÁVEL
  OU RESULTADO INDETERMINADO
```

Regras:

- interface otimista não substitui confirmação;
- retry não pode duplicar decisão;
- resultado indeterminado exige reconsulta antes de repetir ação;
- mudança de contexto exige revalidação;
- sucesso técnico não deve ser confundido com vínculo posterior quando forem estados distintos.

## 15. Vazio, erro, indisponibilidade e recuperação

A experiência deve tratar explicitamente:

- nenhuma solicitação pendente;
- solicitação não localizada;
- informação necessária ausente;
- informação protegida;
- dado desatualizado ou contestado;
- autoridade insuficiente;
- aprovação adicional pendente;
- dependência indisponível;
- processamento interrompido;
- resultado desconhecido;
- atualização concorrente;
- contexto expirado;
- baixa conectividade.

Estado vazio não deve ser apresentado como falha do Coletivo.

Erro técnico não deve ser apresentado como falha moral, administrativa ou da Pessoa solicitante.

## 16. Reversibilidade, interrupção e idempotência

```text
VOLTAR
≠ RECUSAR

FECHAR
≠ DECIDIR

CANCELAR UMA INTENÇÃO
≠ CANCELAR A SOLICITAÇÃO

RETRY
≠ REPETIR DECISÃO

MUDAR DE CONTEXTO
→ REVALIDAR AUTORIDADE
```

Decisões materiais não podem ser disparadas por navegação, fechamento de janela ou simples mudança de contexto.

## 17. Proteção, privacidade e não retaliação

A experiência deve aplicar minimização e acesso proporcional.

Solicitação, contestação, pedido de informação, recusa ou revisão não podem ser usados para:

- expor dados além da finalidade;
- retaliar automaticamente a Pessoa;
- inferir características sensíveis;
- produzir ranking oculto;
- ampliar autoridade do Coletivo sobre outros contextos da Pessoa.

Informação protegida deve permanecer protegida mesmo quando a solicitação exigir análise.

## 18. Planos e capacidade comercial

Planos do Coletivo permanecem capacidade especializada/contextual.

Este Master não autoriza:

- prioridade de solicitação por plano;
- maior chance de aprovação por plano;
- ranking por capacidade comercial;
- bloqueio de direito material para induzir upgrade;
- alteração de autoridade por contratação;
- inventar quota ou entitlement de solicitações;
- transformar gestão de participação em funil de upsell.

Se uma capacidade comercial real e documentada afetar uma função, sua explicação deve preservar alternativas e direitos já autorizados.

## 19. Acessibilidade

Estado, autoridade, proteção, informação pendente, decisão, processamento, erro e confirmação não podem depender exclusivamente de:

- cor;
- ícone;
- posição;
- animação;
- hover;
- blur;
- densidade;
- contraste implícito.

A operação deve ser compreensível por meios acessíveis e não depender de padrões visuais como única fonte de significado.

## 20. Liberdade de Design

Design mantém liberdade sobre:

- composição;
- grid;
- navegação local;
- componentes;
- hierarquia visual;
- número de frames;
- tipografia dentro da autoridade oficial;
- imagens e ícones;
- densidade;
- motion;
- solução responsiva.

Design não pode:

- fundir `COL-003` e `COL-004` por conveniência;
- tratar `GKR-TRN-114` como nova aprovação, novo vínculo ou confirmação de persistência técnica;
- transformar pessoas em ranking;
- criar score de aprovação;
- ocultar autoridade, proteção ou estado material;
- representar processamento como decisão confirmada;
- usar low-fidelity como baseline visual canônica.

## 21. IA e prototipação — source lock

IA pode explorar forma de materialização, mas não pode inventar:

- campos;
- perguntas obrigatórias;
- critérios de aprovação;
- ações;
- estados;
- transições;
- automações;
- rankings;
- scores;
- recomendações;
- notificações;
- integrações;
- permissões;
- entitlement;
- persistência;
- criação automática de vínculo.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 22. Critérios de aceite

Este Master é funcionalmente suficiente quando a materialização:

1. preserva `COL-003` como responsabilidade distinta de `COL-004`;
2. identifica claramente Coletivo, solicitação, estado e autoridade;
3. consome `TRN-105..109` e `TRN-112` sem promoção;
4. preserva `GKR-TRN-114` como continuidade operacional do vínculo já formado, sem duplicar `GKR-TRN-108`;
5. não confunde aprovação com vínculo, papel, representação ou administração;
6. suporta informação adicional sem inventar formulário universal;
7. preserva estados de proteção, contestação, indisponibilidade e resultado indeterminado;
8. não transforma ausência de dado em conclusão;
9. não cria ranking, score ou recomendação automática de aprovação;
10. preserva minimização e separação da perspectiva da Pessoa;
11. mantém Planos como capacidade especializada/contextual;
12. preserva reversibilidade e idempotência;
13. mantém low-fidelity como evidência funcional, não baseline visual;
14. mantém IA em source lock;
15. não cria IDs, não promove maturidade e não libera Product Engineering.

## 23. Lacunas preservadas

Permanecem fora deste Master até autoridade específica:

- critérios materiais universais de aprovação, se vierem a existir;
- política universal de revisão/recurso, se vier a existir;
- RBAC técnico;
- persistência;
- integrações externas;
- notificações finais;
- analytics e KPIs;
- entitlement técnico;
- regras técnicas de criação/atualização de vínculo;
- high-fidelity final;
- protótipo;
- implementação;
- Product Engineering.

## 24. Estado documental

```text
MASTER
→ DRAFT / FUNCTIONAL CONTRACT CANDIDATE

SURFACE GOVERNED
→ GKR-SURF-COL-003

CONTEXTUAL ENTRY
→ GKR-SURF-COL-002 / GKR-TRN-112, WHEN APPLICABLE

SPECIALIZED TRANSITIONS
→ GKR-TRN-105..109
→ MATURITY PRESERVED

POST-APPROVAL CONTINUITY
→ GKR-SURF-COL-004
→ DEDICATED STABLE TRANSITION GAP PRESERVED

ORGANIZATION EQUIVALENT
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
