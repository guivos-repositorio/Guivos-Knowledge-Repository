---
id: RP-002-PILOT-OPENAI-API-DEC-001
title: Piloto — Decisão de Implementação do A8 OpenAI API
status: active
version: 1.0.1
owner: Guivos Research
last_updated: 2026-09-04
normative: false
parent: RP-002
maturity: implementation_target_approved_pre_configuration
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-RESEARCH-BASE-DEC-001
  - RP-002-PILOT-OPS-REG-002
  - RP-002-PILOT-DATA-LAW-001
---

# Piloto — Decisão de Implementação do A8 OpenAI API

## 1. Finalidade

Este documento define o target documental para eventual uso da OpenAI API no primeiro Dry Run Real `N=1` do `RP-002`.

A decisão não configura conta, projeto, credencial ou endpoint e não autoriza envio de dados reais nesta fase.

```text
A8 DOCUMENTATION TARGET
→ DECIDED

A8 OPERATIONAL CONFIGURATION
→ HOLD

OPENAI API WITH REAL PARTICIPANT DATA
→ NOT AUTHORIZED
```

## 2. Produto-alvo

O componente de IA aprovado como target documental é:

```text
SERVICE
→ OpenAI API

ACCOUNT CONTEXT
→ Guivos organizational/business use

PROJECT
→ dedicated RP-002 project

CONSUMER CHATGPT ACCOUNT
→ NOT THE PILOT PROCESSING TARGET
```

A finalidade é apoiar tarefas delimitadas de Research sem transformar a Journey completa em contexto automático de terceiros.

## 3. Finalidades permitidas

A OpenAI API poderá ser usada futuramente apenas para tarefas aprovadas, como:

- estruturar contexto pseudonimizado mínimo;
- apoiar geração/comparação de hipóteses de Possibilidades;
- apoiar síntese metodológica de material já minimizado;
- apoiar classificação não sensível de evidências;
- apoiar redação de alternativas para revisão humana;
- apoiar Search/Web quando A9 autorizar o fluxo correspondente.

Não é uma autoridade decisória sobre a Pessoa.

## 4. Dados permitidos

Target:

```text
DIRECT IDENTIFIERS
→ NO BY DEFAULT

LINKAGE KEY
→ NEVER

CONTEXT
→ minimum necessary
→ pseudonymized
→ sanitized before submission

SENSITIVE DATA
→ NO BY DEFAULT
```

Campos como nome, e-mail, telefone, CPF, RG, endereço, credenciais e a chave de ligação não devem ser enviados à API no fluxo normal.

## 5. Fluxo-alvo

```text
RESEARCH BASE
→ select minimum necessary context
→ human sanitization / direct-identifier check
→ OpenAI API request
→ response
→ human review
→ store only material result when needed
```

Não conectar a Research Base inteira automaticamente à API.

## 6. Endpoint e persistência

Para o primeiro `N=1`, o target deve privilegiar chamadas stateless ou de baixa persistência.

Preferência documental:

```text
RESPONSES / CHAT COMPLETIONS STYLE REQUEST
→ store disabled where applicable

CONVERSATIONS / THREAD-LIKE PERSISTENT STATE
→ NO BY DEFAULT

FILES / VECTOR STORES
→ NO BY DEFAULT

BACKGROUND MODE
→ NO BY DEFAULT

FINE-TUNING / EVAL DATA SHARING
→ NO
```

Qualquer recurso que persista application state além da requisição precisa de revisão específica antes de uso.

## 7. Treinamento e compartilhamento de dados

A documentação oficial da OpenAI informa que dados enviados à API não são usados para treinar ou melhorar os modelos por padrão, salvo opt-in explícito do cliente.

A documentação também informa que compartilhamentos voluntários de feedback, inputs/outputs, evals e fine-tuning são controles separados.

Target do piloto:

```text
VOLUNTARY DATA SHARING
→ DISABLED

OPT-IN TO SHARE INPUTS / OUTPUTS
→ NO

OPT-IN TO SHARE EVAL / FINE-TUNING DATA
→ NO
```

Essas configurações deverão ser verificadas operacionalmente antes de qualquer liberação.

Fontes oficiais verificadas em 2026-08-27:

- <https://platform.openai.com/docs/models/default-usage-policies-by-endpoint>
- <https://help.openai.com/en/articles/10306912-sharing-feedback-evals-and-api-data-with-openai>

## 8. Retenção da OpenAI API

A documentação atual informa que, por padrão, abuse monitoring logs podem conter conteúdo do cliente e são mantidos por até 30 dias, salvo obrigação legal de retenção por prazo maior.

Alguns endpoints também podem manter application state por períodos próprios.

Consequência documental:

```text
DEFAULT API USE
→ DO NOT ASSUME ZERO RETENTION

ABUSE MONITORING
→ UP TO 30 DAYS BY DEFAULT

APPLICATION STATE
→ ENDPOINT-DEPENDENT
```

A política interna A10 deve considerar essa realidade quando congelar retenção e Notice.

Fonte oficial:

<https://platform.openai.com/docs/models/default-usage-policies-by-endpoint>

## 9. Zero Data Retention / Modified Abuse Monitoring

A OpenAI documenta controles de `Zero Data Retention (ZDR)` e `Modified Abuse Monitoring (MAM)` para clientes elegíveis e aprovados.

Este documento não presume elegibilidade nem contratação.

```text
ZDR
→ NOT ASSUMED

MAM
→ NOT ASSUMED

ELIGIBILITY / APPROVAL
→ MUST BE VERIFIED IF PURSUED
```

O stack do piloto deve ser seguro mesmo sob o regime padrão aprovado para a conta, ou então permanecer em `HOLD` até que controle adicional necessário esteja efetivamente disponível.

## 10. DPA e papel da OpenAI

O DPA vigente verificado em 2026-08-27 estava atualizado em 2025-12-01 e efetivo desde 2026-01-01.

O DPA estabelece, no escopo coberto, processamento de Customer Data pela OpenAI em nome do cliente e descreve a OpenAI como Data Processor.

Fonte oficial:

<https://openai.com/policies/data-processing-addendum/>

A existência pública do DPA não substitui a verificação de que a conta/projeto da Guivos está sob os termos empresariais/desenvolvedor aplicáveis e que a relação contratual foi aceita de forma válida.

## 11. Transferência internacional e residência

A OpenAI documenta controles de data residency para clientes/projetos elegíveis, com requisitos que variam por região e recurso.

O piloto não deve presumir residência brasileira nem localização exclusiva em uma jurisdição.

```text
INTERNATIONAL PROCESSING / TRANSFER
→ MATERIAL / MUST BE DISCLOSED AND REVIEWED

DATA RESIDENCY
→ OPTIONAL / ELIGIBILITY-DEPENDENT
→ NOT ASSUMED
```

A11 deverá refletir a configuração efetivamente aprovada antes de Pessoa real.

## 12. Chaves e credenciais

```text
API KEY
→ SECRET
→ NOT IN GKR
→ NOT IN RESEARCH BASE
→ NOT IN IDENTITY VAULT AS PARTICIPANT DATA
→ NOT SENT IN CHAT
```

Credenciais devem ser tratadas como segredo operacional da infraestrutura, com mínimo privilégio e revogação possível.

## 13. Projeto dedicado

O target exige projeto separado para `RP-002` porque isso facilita:

- escopo;
- observabilidade;
- limites;
- revogação;
- configuração de data controls;
- separação de outros produtos Guivos;
- encerramento do experimento.

A existência de uma conta OpenAI da Guivos não fecha A8 sem o projeto e os controles reais.

## 14. Modelos e versões

Não congelar um modelo específico no documento de privacidade salvo necessidade metodológica.

Regra:

- usar modelo compatível com a tarefa aprovada;
- manter a finalidade estável;
- registrar mudança material quando afetar dados, retenção ou comportamento metodológico;
- não interpretar troca de versão de modelo como autorização automática para ampliar dados enviados.

## 15. Human-in-the-loop

Toda saída relevante deve passar por revisão humana antes de:

- ser apresentada como Possibilidade;
- ser usada para excluir alternativa;
- sustentar conclusão sobre a Pessoa;
- virar evidência do episódio.

```text
AI OUTPUT
→ ASSISTIVE
→ NOT FINAL AUTHORITY
```

## 16. Safety e conteúdo de alto risco

O piloto não deve usar a API para substituir profissional em domínios de alto risco nem para decidir autonomamente questões médicas, psicológicas, jurídicas, financeiras ou equivalentes.

Se o Momento exigir tratamento fora do escopo, o Safety Gate continua prevalecendo.

## 17. Logging interno

Registrar apenas o necessário para governança, por exemplo:

- tarefa executada;
- endpoint/capability quando material;
- versão do prompt/template interno quando relevante;
- data;
- resultado metodológico agregado;
- falha material.

Não registrar API key, prompt identificável desnecessário ou resposta com identidade direta no GKR.

## 18. Teste futuro

Teste sintético futuro:

```text
T-OPENAI-API-001
1. USE DEDICATED RP-002 PROJECT
2. VERIFY DATA-SHARING SETTINGS
3. VERIFY RETENTION / DATA CONTROL STATE
4. SEND SYNTHETIC PSEUDONYMIZED INPUT ONLY
5. CONFIRM NO DIRECT IDENTIFIER
6. CONFIRM store / persistence behavior selected
7. RECEIVE OUTPUT
8. VERIFY HUMAN REVIEW FLOW
9. DELETE ANY APPLICATION STATE CREATED BY TEST WHEN APPLICABLE
10. RECORD ONLY NON-SECRET EVIDENCE
```

Não executar durante a fase documental atual.

## 19. Subgates de A8

```text
A8-1 PURPOSE / DATA BOUNDARY
→ DOCUMENTED

A8-2 PRODUCT TARGET
→ DOCUMENTED

A8-3 RETENTION / DPA CURRENT-STATE RESEARCH
→ DOCUMENTED

A8-4 DEDICATED PROJECT
→ HOLD

A8-5 DATA CONTROL SETTINGS VERIFIED
→ HOLD

A8-6 CONTRACT / DPA ACCOUNT RELATIONSHIP VERIFIED
→ HOLD

A8-7 SYNTHETIC TEST
→ HOLD

A8 OVERALL
→ OPERATIONAL HOLD
```

## 20. Estado final

```text
A8 DOCUMENTATION
→ TARGET CLOSED

A8 IMPLEMENTATION
→ DEFERRED

A8 OPERATIONAL STATUS
→ HOLD

A9 — SEARCH / WEB DOCUMENTATION
→ NEXT

P3-C
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
