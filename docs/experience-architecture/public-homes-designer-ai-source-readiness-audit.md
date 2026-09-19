---
id: GKR-UX-HOMES-DESIGN-SOURCE-READINESS-AUDIT-001
title: Homes Públicas — Auditoria Final de Prontidão das Fontes para Designer e Sistemas de AI
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-09-19
normative: false
maturity: designer_ai_source_readiness_audit_in_progress
depends_on:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-HOME-MASTERS-REMEDIATION-001
related:
  - GKR-STATE-001
  - ROADMAP-13.46.0
---

# Homes Públicas — Auditoria Final de Prontidão das Fontes para Designer e Sistemas de AI

## 1. Finalidade

Esta frente reabre deliberadamente a camada **documental** das oito Homes públicas antes do início do serviço externo de Design.

O objetivo não é desenhar, prototipar ou produzir Figma dentro do GKR. O objetivo é deixar as fontes suficientemente completas, coerentes, rastreáveis e autocontidas para que:

- a designer consiga criar manualmente sem reconstruir decisões dispersas;
- sistemas de AI possam consumir o mesmo material como apoio de criação sem preencher lacunas por inferência;
- a liberdade criativa permaneça ampla;
- significado, fronteiras, fatos, claims, evidências e proibições permaneçam inequívocos;
- a Guivos não descubra lacunas materiais somente depois da conclusão e pagamento do serviço de Design.

## 2. Decisão humana que governa esta frente

```text
GKR / CHATGPT
→ NÃO CRIA ARQUIVOS FIGMA
→ NÃO PRODUZ DIREÇÃO VISUAL
→ NÃO PROTOTIPA PÁGINAS
→ NÃO DEFINE IDENTIDADE VISUAL

DESIGNER
→ CRIA MANUALMENTE
→ TOTAL LIBERDADE VISUAL DENTRO DAS FRONTEIRAS SEMÂNTICAS
→ USA GKR + DOCUMENTOS MESTRES + FONTES RELACIONADAS

SISTEMAS DE AI
→ PODEM CONSUMIR AS FONTES COMO APOIO À CRIAÇÃO
→ NÃO RECEBEM AUTORIDADE ARQUITETURAL
→ NÃO SÃO GATE OBRIGATÓRIO
→ NÃO SUBSTITUEM A DESIGNER

GUIVOS.COM 2.0 / FIGMA HISTÓRICO
→ CONSULTA / REFERÊNCIA
→ NÃO AUTORIDADE SEMÂNTICA
→ NÃO BASELINE OBRIGATÓRIA
```

## 3. Relação com o Design Production Release

O Design Production Release anteriormente concedido não é revogado. Contudo, a decisão humana atual **adianta a prioridade documental** e posterga o início operacional da designer até o fechamento desta auditoria.

```text
DESIGN PRODUCTION RELEASE
→ GRANTED

EXTERNAL DESIGNER START
→ DEFERRED BY HUMAN DECISION
→ UNTIL FINAL SOURCE READINESS PASS

GKR FIGMA EXECUTION
→ OUT OF SCOPE / NOT TO BE PERFORMED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 4. Tratamento do snapshot v5

O snapshot v5 permanece congelado e reproduzível como evidência histórica do estado anterior.

```text
delivery/design-handoff-v5
→ FROZEN
→ DO NOT MUTATE
→ HISTORICAL DELIVERY SNAPSHOT AFTER THIS FRONT OPENS

NEW DESIGN START
→ MUST NOT RELY ON V5 AS FINAL CURRENT PACKAGE

NEXT PACKAGE
→ V6 CANDIDATE
→ ONLY AFTER THIS AUDIT PASSES
```

Nenhum arquivo do v5 deve ser reescrito retroativamente para representar decisões posteriores.

## 5. Escopo da auditoria

A auditoria cobre quatro camadas.

### A. Autoridades comuns

Verificar e reconciliar:

- Handoff comum;
- contrato de prontidão;
- template de Source Lock / prompt para AI;
- fluxo operacional de entrega;
- Manifesto do pacote;
- autoridade de release;
- entrypoints e estado corrente.

### B. Oito Homes

Auditar individualmente:

1. Pessoa;
2. Organizações e Coletivos;
3. Mall;
4. Travel;
5. Media;
6. Ads;
7. Business;
8. Intelligence.

### C. Fontes específicas e contratos relacionados

Para cada Home, provar:

- fonte mestre vigente;
- fontes complementares realmente necessárias;
- contratos de produto aplicáveis;
- nomenclaturas oficiais;
- estados e boundaries relevantes;
- conteúdo que exige dado real;
- perguntas ainda abertas;
- proibições de inferência;
- ausência de dependência em documento histórico superado.

### D. Consumibilidade por humano e AI

Cada pacote deve responder sem reconstrução externa:

- o que esta Home é;
- para quem existe;
- qual percepção deve produzir;
- qual pergunta-mãe ou tese a governa;
- quais movimentos/funções narrativas precisam sobreviver;
- o que pode ser criado livremente;
- o que não pode ser inferido;
- quais dados precisam de fonte real;
- quais conteúdos podem ser placeholder;
- quais copies estão congeladas, candidatas ou abertas;
- quais relações com outras Homes/produtos precisam ser preservadas;
- quais referências históricas são somente inspiração;
- quais questões permanecem abertas e quem deve resolvê-las.

## 6. Princípio de completude

```text
100% READY
≠ IDENTIDADE VISUAL PRÉ-DEFINIDA
≠ COPY TODA CONGELADA
≠ LAYOUT PRÉ-DESENHADO

100% READY
→ ZERO LACUNA MATERIAL DE SIGNIFICADO
→ ZERO CONFLITO DE AUTORIDADE
→ ZERO DADO FACTUAL OBRIGATÓRIO SEM CLASSIFICAÇÃO
→ ZERO INFERÊNCIA NECESSÁRIA PARA ENTENDER A HOME
→ LIBERDADE CRIATIVA EXPLÍCITA
→ QUESTÕES ABERTAS EXPLÍCITAS E NÃO-BLOQUEADORAS OU COM DESTINO
```

A ausência deliberada de tipografia, paleta, fotografia, iconografia, composição, grid, motion, linguagem gráfica ou atmosfera **não é finding**.

## 7. Teste por Home

Uma Home somente pode receber `PASS` quando:

1. existe uma autoridade mestre vigente e identificável;
2. a fonte mestre contém a verdade de consumo corrente;
3. dependências materiais estão listadas e atuais;
4. não exige leitura de histórico para compreender estado atual;
5. narrativa e percepção estão explícitas;
6. participantes, produtos e responsabilidades não se confundem;
7. conteúdo factual real está separado de hipótese/placeholder;
8. claims e evidências possuem regras claras;
9. liberdade de Design está explícita;
10. proibições de inferência estão explícitas;
11. estados/condições comerciais ou operacionais relevantes estão classificados;
12. mobile/responsividade possuem princípios suficientes sem prescrever layout;
13. acessibilidade/performance possuem limites suficientes quando aplicáveis;
14. integração com outras Homes/produtos não depende de suposição;
15. a Home pode ser explicada a uma designer nova sem conversa adicional obrigatória;
16. o mesmo contexto pode ser fornecido a uma AI sem induzir invenção arquitetural.

## 8. Testes transversais 8/8

Após os testes individuais:

- mesma taxonomia operacional nas oito Homes;
- mesma distinção `CANONICAL / DESIGN_CREATIVE / CONTENT_CANDIDATE / DESIGN_HYPOTHESIS / PROTOTYPE_PLACEHOLDER / REAL_DATA_REQUIRED / OPEN_QUESTION / PROHIBITED_INFERENCE`;
- nenhuma contradição entre Masters;
- nomes oficiais e papéis de produtos consistentes;
- assinatura de marca consistente;
- autonomia, privacidade, causalidade e prova consistentes;
- diferenças reais entre Homes preservadas;
- nenhuma Home convertida em cópia estrutural de outra;
- nenhum requisito estético global inferido;
- pacote inicial de cada Home com contexto suficiente e sem excesso de documentos irrelevantes.

## 9. Classificação de findings

```text
P0
→ impede compreensão correta da Home

P1
→ lacuna material que pode induzir erro de Design/AI

P2
→ ambiguidade relevante, inconsistência ou falta de rastreabilidade

P3
→ melhoria editorial/documental não bloqueadora
```

Nenhum `P0/P1` pode permanecer aberto no fechamento.

## 10. Registro inicial de findings

A primeira passada de consumibilidade sobre as oito Homes e suas fontes diretamente relacionadas identificou os seguintes findings. A classificação abaixo representa o estado **antes da remediação**.

| ID | Severidade | Escopo | Finding | Risco para Design/AI | Estado |
|---|---|---|---|---|---|
| SR-001 | P1 | Business Master + Business Source Lock × Intelligence | Intelligence é prescrito visualmente como dashboard/KPIs/gráficos, enquanto a autoridade própria do Intelligence estabelece `INTELLIGENCE ≠ DASHBOARD` e trata essas formas apenas como recursos admissíveis. | engessa a designer e pode fazer AI interpretar dashboard como requisito canônico | REMEDIATED_IN_BRANCH / FINAL_VALIDATION_PENDING |
| SR-002 | P1 | Business Master + Source Lock + Authority | cadeia procedimental superada: Source Lock tratado como próximo estágio; Handoff descrito como cobrindo seis Homes; Master/Source Lock declarados inexistentes em autoridade anterior; Home Intelligence tratada como documento futuro | faz designer/AI reconstruir estado corrente a partir de instruções incompatíveis | REMEDIATED_IN_BRANCH / FINAL_VALIDATION_PENDING |
| SR-003 | P2 | Mall Master | o Movimento 10 é definido como `PROVA E CONFIANÇA`, mas o corpo usa dois títulos independentes `Movimento 10 — Prova` e `Movimento 10 — Confiança` | pode induzir contagem de 12 movimentos ou materialização de funções como movimentos distintos | REMEDIATED_IN_BRANCH / FINAL_VALIDATION_PENDING |
| SR-004 | P2 | O/C Master | front matter e fechamento ainda registram auditoria integral em curso e materialização sob gate histórico, embora a auditoria esteja concluída e o release posterior exista | estado temporal incorreto para consumo atual | REMEDIATED_IN_BRANCH / FINAL_VALIDATION_PENDING |
| SR-005 | P1 | Intelligence Master + Source Lock + Handoff | documentos tratam Source Lock/GENINPUT/Handoff como próximos estágios embora Source Lock e Handoff já existam; Handoff ainda nomeia execução em Figma Make | ordem de consumo e próximo gate ficam materialmente incorretos para humano/AI | REMEDIATED_IN_BRANCH / FINAL_VALIDATION_PENDING |
| SR-006 | P1 | Mall / Travel / Media / Ads / Intelligence Masters | metadados `status: draft` coexistem com documentos declarados convergidos e utilizados como fontes vigentes no pacote de Design | AI ou designer pode interpretar fontes-mestre correntes como rascunhos sem autoridade de consumo | REMEDIATED_IN_BRANCH / FINAL_VALIDATION_PENDING |
| SR-007 | P2 | Camada comum | fluxo anterior tratava Figma Make como etapa obrigatória e confundia release com execução visual pelo GKR/ChatGPT | contraria a decisão humana designer-first e reduz liberdade criativa | REMEDIATED_IN_BRANCH |

### 10.1 Critério de remediação

Uma correção é aceita somente quando:

- elimina o drift sem reabrir decisões semânticas válidas;
- não converte liberdade visual em regra;
- mantém história preservada no Git;
- atualiza a autoridade corrente em vez de reescrever snapshots históricos;
- não promove Design, implementação ou produto além do necessário para corrigir a fonte.

### 10.2 Estado por Home — primeira passada

```text
PESSOA
→ REVIEWED / NO MATERIAL HOME-SPECIFIC FINDING IDENTIFIED IN FIRST PASS

ORGANIZAÇÕES E COLETIVOS
→ REVIEWED / SR-004 REMEDIATED / FINAL VALIDATION PENDING

MALL
→ REVIEWED / SR-003 + SR-006 REMEDIATED / FINAL VALIDATION PENDING

TRAVEL
→ REVIEWED / SR-006 REMEDIATED / FINAL VALIDATION PENDING

MEDIA
→ REVIEWED / SR-006 REMEDIATED / FINAL VALIDATION PENDING

ADS
→ REVIEWED / SR-006 REMEDIATED / FINAL VALIDATION PENDING

BUSINESS
→ REVIEWED / SR-001 + SR-002 REMEDIATED / FINAL VALIDATION PENDING

INTELLIGENCE
→ REVIEWED / SR-005 + SR-006 REMEDIATED / FINAL VALIDATION PENDING

TRANSVERSE COMMON LAYER
→ SR-007 REMEDIATED IN BRANCH
```

## 11. Saída esperada

Ao final desta frente:

```text
8 / 8 HOMES
→ AUDITED

COMMON AUTHORITIES
→ RECONCILED

P0
→ 0 OPEN

P1
→ 0 OPEN

AI CONSUMABILITY
→ PASS

DESIGNER CONSUMABILITY
→ PASS

V6 SOURCE PACKAGE ELIGIBILITY
→ PASS OR FAIL

FIGMA ARTIFACTS PRODUCED BY GKR
→ 0
```

Se o resultado for `PASS`, a etapa posterior será a emissão/materialização de um **snapshot v6 somente documental**, seguido de validação de integridade e entrega à designer.

## 12. Estado atual

```text
AUDIT
→ IN_PROGRESS

COMMON-LAYER RECONCILIATION
→ MATERIAL REMEDIATION APPLIED IN BRANCH / VALIDATION PENDING

HOME-BY-HOME REVIEW
→ FIRST PASS COMPLETED / FINDINGS UNDER REMEDIATION

V6
→ NOT_EMITTED

EXTERNAL DESIGNER START
→ DEFERRED UNTIL PASS

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```
