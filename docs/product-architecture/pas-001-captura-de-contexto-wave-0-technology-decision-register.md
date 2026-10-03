---
id: PAS-001-CC-W0-TECH-DECISIONS-001
title: Registro de Decisões Tecnológicas da Onda 0
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-W0-POC-001
  - PAS-001-CC-W0-DEPENDENCY-001
  - ADR-CC-001
  - ADR-CC-002
  - ADR-CC-003
  - ADR-CC-004
  - ADR-CC-005
---

# PAS-001-CC-W0-TECH-DECISIONS-001 — Registro de Decisões Tecnológicas

> Este registro organiza dossiers de decisão. Nenhuma opção é aceita neste ciclo apenas por preferência, popularidade ou conveniência. Decisão permanente exige ADR próprio após evidência suficiente.

## 1. Estados

- `identified`: questão registrada;
- `researching`: critérios e opções em análise;
- `poc_required`: decisão depende de prova;
- `proposed`: recomendação pronta para revisão;
- `accepted`: decisão formalizada em ADR;
- `deferred`: não bloqueia o incremento atual;
- `rejected`: opção descartada com justificativa;
- `superseded`: substituída por decisão posterior.

## 2. Matriz executiva

| ID | Tema | Estado inicial | Bloqueia | POC principal | Saída esperada |
|---|---|---|---|---|---|
| ADR-TCC-001 | linguagem e framework | researching | W0-02 | benchmark de domínio/testes | ADR antes do build |
| ADR-TCC-002 | persistência funcional | poc_required | W0-03 | POC-01 | ADR antes da integração |
| ADR-TCC-003 | conteúdo e object storage | poc_required | W0-04 | POC-02 | ADR antes de mídia representativa |
| ADR-TCC-004 | eventos e mensageria | poc_required | W0-03/W0-05 | POC-01/03 | ADR antes de integração distribuída |
| ADR-TCC-005 | busca e vetores | poc_required | W0-06 | POC-04 | ADR da busca mínima; vetores podem ser deferred |
| ADR-TCC-006 | identidade, autorização e políticas | researching | W0-02/W0-05 | testes de política | ADR antes de acesso integrado |
| ADR-TCC-007 | chaves, segredos e criptografia | researching | W0-04/Security Gate | POC-02 | ADR antes de conteúdo protegido |
| ADR-TCC-008 | observabilidade | researching | W0-07 | POC-05 | ADR antes de gate de qualidade |
| ADR-TCC-009 | modelos e Intelligence | deferred/poc_required | POC-06 | POC-06 | ADR somente se modelo entrar na Onda 0 |
| ADR-TCC-010 | infraestrutura e implantação | researching | ambientes integrados | POC-01/05 | ADR antes de Internal Trial |

## 3. ADR-TCC-001 — Linguagem e framework

### Questão

Qual combinação permite implementar domínio rico, contratos versionados e testes reproduzíveis com baixo risco operacional?

### Critérios

- tipagem e modelagem de domínio;
- imutabilidade e invariantes;
- maturidade de bibliotecas;
- serialização e schemas;
- concorrência e idempotência;
- observabilidade;
- segurança;
- testes;
- produtividade;
- disponibilidade de profissionais;
- portabilidade;
- custo de manutenção.

### Opções a avaliar

- ecossistema TypeScript/Node;
- ecossistema JVM;
- ecossistema .NET;
- ecossistema Go;
- outra opção apenas com justificativa comparável.

### Decisão mínima

Definir linguagem, runtime, framework de aplicação e estratégia de testes sem impor topologia de microsserviços.

## 4. ADR-TCC-002 — Persistência funcional

### Questão

Qual mecanismo preserva transação, versão do agregado, auditabilidade e reconstrução?

### Critérios

- atomicidade;
- concorrência otimista;
- idempotência;
- integridade;
- consultas operacionais;
- snapshots;
- backup e restore;
- RPO/RTO;
- migração;
- custo e operação;
- portabilidade.

### Opções a avaliar

- banco relacional com eventos/outbox;
- event store especializado;
- combinação relacional e log de eventos;
- alternativa documental apenas se comprovar invariantes e transação.

### Decisão mínima

Definir sistema de registro, estratégia de eventos, versionamento e reconstrução.

## 5. ADR-TCC-003 — Conteúdo e object storage

### Questão

Como armazenar mídia e documentos separados do registro funcional com integridade, retenção e exclusão?

### Critérios

- criptografia;
- referência opaca;
- acesso temporário;
- integridade;
- versionamento;
- quarentena;
- retenção;
- exclusão física e criptográfica;
- restore;
- custo;
- portabilidade.

### Decisão mínima

Definir mecanismo de objetos, metadados, chaves, acesso e ciclo de vida.

## 6. ADR-TCC-004 — Eventos e mensageria

### Questão

Como publicar e consumir eventos com recuperação, duplicidade controlada e compatibilidade?

### Critérios

- entrega;
- ordenação;
- retries;
- dead letter ou quarentena;
- replay;
- observabilidade;
- contratos;
- throughput;
- isolamento;
- operação;
- custo.

### Decisão mínima

Definir outbox ou equivalente, transporte, política de retry, compatibilidade e consumidor mínimo.

## 7. ADR-TCC-005 — Busca e vetores

### Questão

Qual mecanismo suporta busca mínima protegida e, opcionalmente, vetores revogáveis?

### Critérios

- filtro anterior à recuperação;
- isolamento por participante;
- finalidade;
- remoção após revogação;
- atualização após correção;
- reconstrução;
- snippets;
- vetores;
- custo;
- operação;
- portabilidade.

### Decisão mínima

Definir busca `metadata_only` e privada. Vetores podem permanecer `deferred` se a prova não for necessária ao núcleo.

## 8. ADR-TCC-006 — Identidade, autorização e políticas

### Questão

Como representar ator, participante, representação, finalidade, escopo e validade sem misturar autenticação com autoridade funcional?

### Critérios

- identidade opaca;
- representação;
- menor privilégio;
- finalidade;
- escopo;
- validade;
- explicabilidade;
- auditoria;
- revogação;
- integração;
- fallback local.

### Decisão mínima

Definir contratos de identidade e mecanismo de decisão de política. Autenticação não poderá confirmar fatos humanos.

## 9. ADR-TCC-007 — Chaves, segredos e criptografia

### Questão

Como proteger conteúdo e credenciais, permitir rotação e sustentar exclusão criptográfica?

### Critérios

- KMS/HSM ou equivalente;
- envelope encryption;
- segregação por ambiente;
- rotação;
- auditoria;
- recuperação;
- disponibilidade;
- revogação;
- acesso JIT;
- custo.

### Decisão mínima

Definir gestão de chaves, segredos, rotação e uso por classe de sensibilidade.

## 10. ADR-TCC-008 — Observabilidade

### Questão

Como medir fluxos e diagnosticar falhas sem expor conteúdo sensível?

### Critérios

- logs estruturados e redigidos;
- métricas;
- tracing;
- correlação opaca;
- retenção;
- alertas;
- acesso;
- custo;
- exportação de evidências;
- segregação por ambiente.

### Decisão mínima

Definir stack, convenções, campos proibidos, SLIs e estratégia de evidência.

## 11. ADR-TCC-009 — Modelos e Intelligence

### Questão

É necessário incluir modelo na Onda 0 e, se necessário, como preservar minimização, proveniência e ausência de autoridade?

### Critérios

- necessidade real para o núcleo;
- isolamento;
- versionamento;
- prompt injection;
- rastreabilidade;
- classificação de saída;
- revogação de derivados;
- privacidade;
- custo;
- portabilidade;
- avaliação.

### Decisão mínima

Primeiro decidir `include` ou `defer`. Se incluído, definir provedor ou runtime, versão, controles e limites. Modelo nunca confirma nem autoriza.

## 12. ADR-TCC-010 — Infraestrutura e implantação

### Questão

Como executar ambientes da Onda 0 com isolamento, recuperação, custo controlado e rollback?

### Critérios

- ambientes;
- isolamento;
- rede;
- segredos;
- implantação;
- rollback;
- observabilidade;
- recuperação;
- escalabilidade inicial;
- custo;
- portabilidade;
- operação regional futura.

### Decisão mínima

Definir infraestrutura da Onda 0 e Internal Trial sem declarar topologia definitiva de produção.

## 13. Método de avaliação

Cada dossier deverá usar matriz ponderada com:

- critério;
- peso;
- evidência;
- pontuação;
- risco;
- limitação;
- custo de mudança;
- recomendação.

Pesos não poderão ocultar requisito obrigatório. Opção que viola autoridade, isolamento, revogação ou auditabilidade é eliminada independentemente da pontuação total.

## 14. Saída de decisão

Uma decisão proposta deverá registrar:

- contexto;
- requisitos;
- opções;
- evidências e POCs;
- decisão;
- consequências positivas;
- consequências negativas;
- riscos;
- condições de revisão;
- plano de migração ou reversão;
- autoridade aprovadora.

## 15. Critérios de ADR obrigatório

Criar ADR próprio quando:

- a escolha for permanente ou de alto custo de reversão;
- afetar autoridade, dados, segurança ou contrato;
- bloquear incremento;
- criar dependência externa;
- definir sistema de registro;
- alterar capacidade operacional;
- aceitar exceção de longa duração.

## 16. Limites

Este registro não:

- escolhe fornecedor;
- aprova contratação;
- transforma POC em produção;
- autoriza dados reais;
- cria microsserviços obrigatórios;
- autoriza Intelligence a decidir por pessoas;
- substitui ADR formal.