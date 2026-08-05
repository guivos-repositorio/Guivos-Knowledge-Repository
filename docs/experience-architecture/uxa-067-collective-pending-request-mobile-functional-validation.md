---
id: UXA-067
title: Validação Funcional e Reformulação da Solicitação Pendente Móvel em Coletivos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-064
  - UXA-065
  - UXA-066
related:
  - UXA-068
  - M7.69
normative: false
---

# Validação Funcional e Reformulação da Solicitação Pendente Móvel em Coletivos

## 1. Finalidade

Este documento valida funcionalmente os oito wireframes móveis materializados pela UXA-066 e registra as reformulações necessárias antes de qualquer avanço para `Meus Coletivos` ou para outra família P0A.

A família foi examinada como continuidade única:

```text
comprovante transitório
→ solicitação aguardando decisão
→ análise comum ou protegida
→ pedido de informação adicional
→ revisão da resposta ou preferência
→ cancelamento, aprovação, recusa ou expiração
→ retorno seguro ou acesso ao Coletivo
```

A UXA-067 não cria novos SVGs, protótipo, teste com pessoas, política jurídica, automação de decisão, `Meus Coletivos` ou implementação.

## 2. Artefatos avaliados

| Artefato | Estado anterior | Resultado |
|---|---|---|
| aguardando decisão | materializado; pendente | reformulado e validado |
| análise protegida | materializado; pendente | reformulado e validado |
| informação adicional solicitada | materializado; pendente | reformulado e validado |
| revisão da resposta adicional | materializado; pendente | reformulado e validado |
| cancelamento pela Pessoa | materializado; pendente | reformulado e validado |
| aprovação | materializado; pendente | reformulado e validado |
| recusa | materializado; pendente | reformulado e validado |
| expiração | materializado; pendente | reformulado e validado |

Resultado da família:

- oito SVGs materializados;
- oito SVGs reformulados;
- oito SVGs funcionalmente validados;
- zero novo SVG;
- zero pendência funcional dentro desta família.

## 3. Critérios aplicados

A revisão verificou:

1. continuidade entre comprovante e acompanhamento;
2. diferença entre espera, ação necessária e resultado;
3. estado, data, identificador e autoridade;
4. estimativa sem promessa de decisão;
5. atualização sem prioridade ou mudança fictícia de fila;
6. voluntariedade da informação adicional;
7. separação entre resposta, preferência, contestação e cancelamento;
8. confirmação anterior ao envio adicional;
9. cancelamento da resposta separado do cancelamento da solicitação;
10. limites de uso posterior sem garantia jurídica ou técnica absoluta;
11. aprovação sem papel ou preferência automática;
12. recusa separada de sanção, reputação e denúncia;
13. expiração separada de recusa e consentimento;
14. análise protegida com autoridade limitada e exposição mínima;
15. ausência de navegação para superfícies ainda não materializadas.

## 4. Achados e reformulações

### 4.1 Atualização apresentada como possível mudança de estado

Os estados de espera utilizavam ações como `Atualizar estado` e `Atualizar estado protegido`, que poderiam sugerir que a Pessoa alteraria a posição, prioridade ou decisão do processo.

Reformulação:

- ações alteradas para `Verificar se há atualização` e `Verificar atualização protegida`;
- a interface declara que verificar não altera fila, prioridade ou decisão;
- atraso continua distinto de recusa;
- silêncio continua distinto de aprovação.

Decisão validada:

> consultar o estado não poderá parecer uma ação operacional sobre a fila.

### 4.2 Correção de dado durante análise sem edição silenciosa

O estado principal declarava bloqueio de edição, mas não orientava como tratar informação materialmente incorreta.

Reformulação:

- a Pessoa poderá ver exatamente o que foi enviado;
- correção material exige cancelamento e nova revisão;
- nenhum dado é alterado silenciosamente durante a análise;
- nova solicitação não reutiliza confirmações anteriores.

### 4.3 Autoridade protegida insuficientemente delimitada

A análise protegida mencionava equipe especializada sem explicitar seu limite funcional.

Reformulação:

- equipe especializada da Guivos identificada como autoridade limitada ao processo;
- remetente separado de quem analisa e decide;
- remetente não recebe acesso adicional nem decide sozinho;
- identidade operacional completa permanece no registro protegido;
- exposição mínima continua preservada.

### 4.4 Cancelar análise não era cancelar solicitação

A ação `Cancelar análise` poderia sugerir controle da Pessoa sobre uma atividade interna, em vez do encerramento de seu próprio pedido.

Reformulação:

- ação alterada para `Cancelar solicitação`;
- denúncia permanece ação independente;
- verificar, cancelar e denunciar possuem efeitos próprios;
- nenhuma ação cria exposição pública automática.

### 4.5 Informação adicional apresentada como necessária

O título `Informação adicional necessária` podia transformar um pedido do Coletivo em obrigação da Pessoa.

Reformulação:

- título alterado para `Informação adicional solicitada`;
- estado passa a exigir decisão, não necessariamente fornecimento;
- responder, preferir não informar, contestar e cancelar aparecem como alternativas legítimas;
- ausência de resposta não é recusa voluntária;
- eventual expiração deve seguir regra previamente apresentada.

Decisão validada:

> uma pergunta adicional poderá exigir escolha, mas não poderá presumir dever de revelar informação.

### 4.6 Contradição entre análise pausada e dados em análise

O pedido adicional declarava que a análise estava pausada e, simultaneamente, que os dados permaneciam em análise.

Reformulação:

- a decisão fica pausada até a escolha, resposta, cancelamento ou expiração;
- dados já enviados permanecem vinculados ao processo pausado;
- nenhum novo processamento é inferido pelo texto;
- finalidade e tratamento permanecem consultáveis.

### 4.7 Cancelar resposta confundido com cancelar solicitação

A revisão adicional utilizava `Cancelar` e `Cancelar sem enviar resposta`, sem distinguir descarte do rascunho e encerramento do pedido principal.

Reformulação:

- `Descartar rascunho` remove somente a resposta em preparação;
- `Voltar sem enviar esta resposta` mantém a solicitação no estado anterior;
- cancelamento da solicitação permanece na superfície de pedido adicional;
- resposta e opção `prefiro não informar` compartilham revisão consciente;
- confirmação continua inicialmente vazia.

### 4.8 Efeito do envio adicional incompleto

A revisão não informava claramente o que ocorreria após o envio.

Reformulação:

- o envio poderá retomar a análise;
- enviar não cria vínculo nem garante aprovação;
- conteúdo, finalidade e destinatário são revisados antes da ação;
- Organização apoiadora continua sem acesso automático.

### 4.9 Tratamento de dados apresentado como garantia absoluta

Cancelamento e expiração declaravam que novos usos ficariam tecnicamente bloqueados, antecipando política jurídica e implementação.

Reformulação:

- nenhum novo uso incompatível deverá ocorrer;
- retenção, exclusão ou preservação seguem regra apresentada;
- registro mínimo poderá existir quando houver finalidade legítima;
- a UXA-067 não define base jurídica, prazo técnico ou mecanismo de exclusão.

Decisão validada:

> o wireframe governa o comportamento esperado sem alegar garantia técnica ou jurídica ainda não contratada.

### 4.10 Continuidade após aprovação como promessa de implementação

A aprovação afirmava que o ambiente interno abriria preservando escolhas e poderia parecer declarar superfícies futuras como concluídas.

Reformulação:

- ao acessar o ambiente interno, as escolhas deverão ser preservadas;
- a tela não declara pausa, saída ou gestão do vínculo como reformuladas;
- `Abrir Coletivo` continua como continuidade legítima já existente;
- função, autoridade, presença e notificações permanecem separadas.

### 4.11 Revisão da recusa simulada sem contrato próprio

A recusa informava revisão aplicável, mas o processo completo ainda não foi materializado.

Reformulação:

- a regra deverá declarar se existe revisão, prazo e autoridade;
- nenhum caminho de revisão é apresentado como disponível sem contrato próprio;
- denúncia de conduta ou processo permanece separada da revisão;
- denúncia não pressupõe abuso comprovado nem substitui recurso formal.

### 4.12 Recomeço após expiração como possibilidade condicionada

A expiração afirmava que seria possível recomeçar, o que poderia funcionar como promessa independente da disponibilidade futura.

Reformulação:

- nova solicitação poderá ser iniciada somente se entradas estiverem disponíveis;
- nova tentativa exige nova revisão;
- dados anteriores não são preenchidos silenciosamente;
- expiração não é recusa, consentimento, punição ou reputação.

## 5. Resultado por estado

### 5.1 Aguardando decisão

Validado porque:

- estado, autoridade, data e identificador são verificáveis;
- estimativa não é promessa;
- verificação não altera fila;
- correção material não edita silenciosamente o pedido;
- cancelamento continua disponível com confirmação própria.

### 5.2 Análise protegida

Validada porque:

- remetente, equipe e limites de autoridade estão separados;
- alegação não verificada permanece identificada;
- dados mínimos e dados ocultos são distinguíveis;
- cancelamento da solicitação não é cancelamento da atividade interna;
- denúncia não cria exposição pública automática.

### 5.3 Informação adicional solicitada

Validada porque:

- o pedido não é apresentado como obrigação de revelar;
- pergunta, finalidade, autoridade e prazo são visíveis;
- resposta, preferência, contestação e cancelamento permanecem possíveis;
- a decisão pausada não é confundida com processamento ativo;
- silêncio não é recusa voluntária.

### 5.4 Revisão da resposta adicional

Validada porque:

- resposta ou preferência é revisável;
- confirmação começa vazia;
- destinatário, finalidade e dados excluídos estão visíveis;
- descartar rascunho não cancela a solicitação;
- envio poderá retomar análise sem criar vínculo.

### 5.5 Cancelamento

Validado porque:

- decisão é atribuída à própria Pessoa;
- ausência de vínculo e de recusa do Coletivo está clara;
- tratamento posterior não é prometido de forma absoluta;
- nova solicitação exige nova revisão;
- histórico não funciona como confirmação reutilizável.

### 5.6 Aprovação

Validada porque:

- autoridade e fundamento estão identificados;
- vínculo confirmado não cria função ou obrigação;
- preferência de lista e notificações permanecem preservadas;
- continuidade não declara superfícies futuras como reformuladas;
- registro permanece separado de reputação e presença.

### 5.7 Recusa

Validada porque:

- fundamento e consequência estão visíveis;
- recusa não é sanção, reputação ou contato privado;
- revisão não é simulada sem contrato;
- denúncia permanece separada e não presume abuso;
- nova solicitação exige novas condições e revisão.

### 5.8 Expiração

Validada porque:

- regra temporal e ausência de decisão estão explícitas;
- expiração não é recusa ou consentimento;
- tratamento posterior é governado sem garantia absoluta;
- recomeço depende da disponibilidade vigente;
- nenhum dado é reutilizado silenciosamente.

## 6. Continuidade validada

### 6.1 Espera comum

```text
comprovante transitório
→ Solicitação Pendente
→ verificar atualização sem alterar fila
→ aguardar, cancelar ou receber novo evento
```

### 6.2 Pedido adicional

```text
Solicitação Pendente
→ informação adicional solicitada
→ responder, preferir não informar, contestar ou cancelar
→ revisar resposta ou preferência
→ enviar e possivelmente retomar análise
```

### 6.3 Resultado

```text
análise
→ aprovação, recusa, cancelamento ou expiração
→ compreender autoridade, fundamento e consequência
→ retornar ao Perfil Público ou abrir o Coletivo quando aprovado
```

## 7. Cobertura após validação

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Coletivos — revisão e solicitação | 5 | 5 | 0 |
| Coletivos — Solicitação Pendente | 8 | 8 | 0 |
| **Total de Coletivos** | **22** | **22** | **0** |
| Opportunity Boost | 46 | 36 | 10 |

## 8. Decisões preservadas

Continuam vigentes:

- solicitação não é participação;
- consultar estado não altera fila;
- estimativa não é promessa;
- pedido adicional não é obrigação de revelar;
- preferir não informar não é recusa voluntária;
- resposta adicional não garante aprovação;
- descartar resposta não cancela solicitação;
- cancelamento da Pessoa não é recusa do Coletivo;
- recusa não é reputação ou sanção;
- expiração não é recusa ou consentimento;
- denúncia não é revisão formal;
- proteção não é irregularidade;
- apoio institucional não concede dados ou autoridade;
- evento futuro não é garantia de implementação.

## 9. Limites

Não são iniciados:

- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- gestão do responsável;
- revisão formal completa de recusa;
- política jurídica;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto;
- Expressão Guiada do Momento Atual;
- ambiente de simulação das jornadas.

## 10. Critérios de saída

A família está funcionalmente validada porque:

- os oito estados possuem hierarquia e decisão coerentes;
- espera, ação e resultado são distinguíveis;
- autoridade, estimativa, dados e consequência são verificáveis;
- nenhuma consulta simula alteração operacional;
- informação adicional preserva voluntariedade;
- cancelamento, recusa e expiração permanecem distintos;
- tratamento de dados não antecipa garantia jurídica ou técnica;
- nenhuma superfície inexistente é apresentada como disponível.

## 11. Próxima transição recomendada

**UXA-068 — Expressão Guiada do Momento Atual por Texto e Voz.**

O pacote deverá materializar como a Pessoa é orientada a comunicar situação, impacto, prioridade, direção e contexto antes da compreensão inicial, preservando relato livre, perguntas adaptativas, revisão e voluntariedade.

A UXA-068 não é iniciada por esta validação e depende de autorização separada.
