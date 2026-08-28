---
id: RP-002-PILOT-SEARCH-WEB-DEC-001
title: Piloto — Decisão de Implementação do A9 Search e Web
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: implementation_target_approved_pre_configuration
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-RESEARCH-BASE-DEC-001
  - RP-002-PILOT-OPENAI-API-DEC-001
  - RP-002-PILOT-OPS-REG-001
---

# Piloto — Decisão de Implementação do A9 Search e Web

## 1. Finalidade

Este documento define o target documental de `A9 — Search / Web` para localizar, verificar e atualizar supply público no `RP-002` sem expor identidade direta da Pessoa.

```text
A9 DOCUMENTATION TARGET
→ DECIDED

A9 OPERATIONAL CONFIGURATION
→ HOLD
```

## 2. Finalidades permitidas

Search/Web poderá ser utilizado para:

- localizar oportunidades públicas;
- verificar existência e disponibilidade;
- checar critérios públicos de elegibilidade;
- confirmar datas, localização, preço e condições;
- verificar freshness;
- comparar fontes;
- identificar sinais de desatualização ou incompatibilidade.

Não deve ser usado para investigar a identidade da Pessoa nem enriquecer perfil pessoal por conveniência.

## 3. Princípio de minimização

A query deve conter o mínimo contexto necessário para encontrar supply.

```text
DIRECT NAME
→ NO

EMAIL / PHONE
→ NO

CPF / ID DOCUMENT
→ NO

LINKAGE KEY
→ NEVER

PARTICIPANT_ID
→ NORMALLY NO NEED TO SEND

CONTEXT
→ only non-identifying attributes necessary for supply search
```

Exemplo de intenção adequada:

```text
curso presencial de gestão operacional em Belo Horizonte setembro 2026
```

Evitar consultas que combinem detalhes únicos capazes de reidentificar a Pessoa sem necessidade.

## 4. Método-alvo

O target primário é consolidar pesquisa assistida no mesmo projeto dedicado da OpenAI API definido em A8, usando capacidade de Web Search quando apropriada.

```text
PRIMARY SEARCH TARGET
→ OpenAI API Web Search
→ dedicated RP-002 project
→ minimized query/context

SOURCE VERIFICATION
→ open original public source
→ verify material facts
→ record source reference in Research Base
```

A documentação atual da OpenAI informa que Web Search é elegível aos controles ZDR, sujeito às condições gerais de elegibilidade/configuração da organização. O piloto não presume que ZDR esteja ativado.

Fonte oficial verificada em 2026-08-27:

<https://platform.openai.com/docs/models/default-usage-policies-by-endpoint>

## 5. Verificação humana de fonte

Resultado de mecanismo de busca não é evidência suficiente quando um fato for material.

Fluxo:

```text
SEARCH RESULT
→ OPEN ORIGINAL SOURCE WHEN AVAILABLE
→ CHECK DATE / CONDITIONS / LOCATION / ELIGIBILITY
→ RECORD MATERIAL FACTS
→ RECORD FRESHNESS
→ APPLY GATES
```

Para afirmações críticas, preferir fonte primária/oficial.

## 6. Contexto que pode ser usado

Quando material ao supply, pode-se usar de forma minimizada:

- cidade/região;
- idioma;
- faixa de preço/orçamento sem dado financeiro pessoal detalhado;
- janela de datas;
- modalidade presencial/remota;
- tema de aprendizagem ou carreira;
- requisitos objetivos da oportunidade;
- restrições logísticas não identificáveis;
- preferências diretamente relevantes à busca.

## 7. Contexto proibido por padrão

Não enviar ao Search/Web:

- nome real;
- e-mail;
- telefone;
- endereço residencial completo;
- documentos;
- dados bancários;
- credenciais;
- histórico pessoal amplo;
- transcrição integral;
- informação sensível desnecessária;
- Linkage Key;
- conteúdo do Identity Vault.

## 8. Pesquisa de pessoas

O piloto não deve pesquisar terceiros privados como forma de validar ou vigiar a Pessoa participante.

Pesquisa de pessoas somente poderá ocorrer quando a própria oportunidade pública exigir verificação legítima de um agente público/profissional e a informação utilizada for pública e material ao supply.

## 9. Resultado e armazenamento

Na Research Base, registrar somente o que for útil ao episódio:

- URL/referência da fonte;
- título/organização quando relevante;
- data de verificação;
- fatos materiais;
- freshness;
- critérios de elegibilidade;
- limitações/incertezas;
- resultado dos gates.

Não copiar páginas inteiras ou datasets por conveniência.

## 10. Browser / acesso direto a URLs

Abertura direta de uma fonte pública para verificação deve evitar transmitir contexto da Pessoa no próprio URL, query string, formulários ou campos de busca do site.

Se o site exigir login, envio de dados pessoais ou candidatura, isso deixa de ser simples verificação pública e exige decisão separada antes de qualquer ação em nome da Pessoa.

## 11. Ação em nome da Pessoa

```text
SEARCH
→ MAY LOCATE / VERIFY

APPLY / REGISTER / BUY / SEND FORM
→ NO BY DEFAULT
```

O Dry Run não autoriza executar transação, inscrição, candidatura ou contato externo em nome da Pessoa sem autorização específica e fluxo aprovado.

## 12. Publicidade e resultados patrocinados

Resultado patrocinado não deve receber tratamento privilegiado.

Regras:

- distinguir anúncio de evidência orgânica quando possível;
- aplicar os mesmos gates;
- não considerar pagamento como sinal de relevância;
- registrar conflito material quando aplicável.

## 13. Freshness

Para supply temporal, registrar a data da verificação.

Se uma oportunidade tiver prazo, disponibilidade ou condição volátil, a evidência deve ser revalidada próximo do momento de apresentação quando necessário.

A política de freshness definida no RP-002 continua prevalecendo.

## 14. Transferência / operador

Como o target primário usa OpenAI API Web Search, o processamento externo fica vinculado às condições documentadas em A8.

```text
PRIMARY EXTERNAL OPERATOR
→ OpenAI API / Web Search target

DIRECT IDENTIFIERS
→ PROHIBITED BY DEFAULT

INTERNATIONAL PROCESSING
→ MATERIAL / review with A8
```

A navegação em fontes públicas originais pode envolver operadores dos respectivos sites. Por isso, não submeter dados da Pessoa a esses sites durante simples verificação.

## 15. Teste futuro

```text
T-SEARCH-WEB-001
1. USE SYNTHETIC NON-IDENTIFYING MOMENTO CONTEXT
2. CREATE MINIMIZED SEARCH QUERY
3. EXECUTE SEARCH IN APPROVED PROJECT
4. OPEN PRIMARY SOURCE
5. VERIFY MATERIAL FACTS / FRESHNESS
6. STORE ONLY SOURCE + MATERIAL FACTS
7. CONFIRM NO DIRECT IDENTIFIER WAS SENT
8. CONFIRM NO FORM / TRANSACTION WAS EXECUTED
```

O teste permanece adiado.

## 16. Subgates de A9

```text
A9-1 PURPOSE / MINIMIZATION
→ DOCUMENTED

A9-2 PRIMARY METHOD TARGET
→ DOCUMENTED

A9-3 SOURCE VERIFICATION METHOD
→ DOCUMENTED

A9-4 REAL PROJECT / TOOL CONFIGURATION
→ HOLD

A9-5 OPERATOR / CONTRACT STATE VERIFIED
→ DEPENDS ON A8 / HOLD

A9-6 SYNTHETIC TEST
→ HOLD

A9 OVERALL
→ OPERATIONAL HOLD
```

## 17. Estado final

```text
A9 DOCUMENTATION
→ TARGET CLOSED

A9 IMPLEMENTATION
→ DEFERRED

A9 OPERATIONAL STATUS
→ HOLD

NEXT DOCUMENTAL BLOCK
→ A10 RETENTION

P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD
```
