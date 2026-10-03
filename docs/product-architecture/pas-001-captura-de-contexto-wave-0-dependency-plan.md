---
id: PAS-001-CC-W0-DEPENDENCY-001
title: Plano de Dependências da Onda 0 da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-W0-BACKLOG-001
---

# PAS-001-CC-W0-DEPENDENCY-001 — Plano de Dependências da Onda 0

> Dependência significa capacidade mínima necessária. Não implica produto, fornecedor, equipe, microsserviço ou contratação específica.

## 1. Classes temporais

- `required_before_build`: necessária antes do início do núcleo;
- `required_before_integration`: necessária antes dos fluxos integrados;
- `required_before_security_gate`: necessária antes do gate de segurança;
- `required_before_operational_trial`: necessária antes de ensaio interno;
- `required_before_production`: necessária apenas em decisão futura;
- `optional_for_wave_0`: não bloqueia a Onda 0.

## 2. Matriz consolidada

| ID | Capacidade | Classe | Incremento | Owner lógico | Fallback permitido | Evidência |
|---|---|---|---|---|---|---|
| CC-W0-001 | identidade e representação | required_before_build | W0-02 | Identity/Platform | stub contratual com dados sintéticos | autenticação e representação testadas |
| CC-W0-002 | autoridade contextual | required_before_build | W0-02/W0-05 | Security/Domain | policy adapter local com mesmas regras | decisões permitidas e negadas |
| CC-W0-003 | registro transacional do agregado | required_before_build | W0-03 | Data/Engineering | implementação local transacional | atomicidade e versão comprovadas |
| CC-W0-004 | publicação confiável de eventos | required_before_integration | W0-03 | Platform/Engineering | outbox local ou mecanismo equivalente | persistência e publicação reconciliadas |
| CC-W0-005 | registro de idempotência | required_before_build | W0-03 | Engineering | armazenamento transacional mínimo | replay retorna resultado anterior |
| CC-W0-006 | registro de schemas | required_before_build | W0-03 | Architecture/Engineering | catálogo versionado no repositório | versão e compatibilidade resolvidas |
| CC-W0-007 | registro de consumidores | required_before_integration | W0-05 | Architecture/Platform | catálogo local assinado/versionado | finalidade e compromissos explícitos |
| CC-W0-008 | persistência temporária e expiração | required_before_integration | W0-04 | Data/Platform | scheduler controlado no ambiente | expiração e descarte comprovados |
| CC-W0-009 | auditoria minimizada | required_before_security_gate | W0-05/W0-07 | Security/Governance | trilha append-only controlada | decisão e autoridade rastreáveis |
| CC-W0-010 | observabilidade segura | required_before_security_gate | W0-07 | SRE/Security | stack mínima com redaction | zero conteúdo proibido |
| CC-W0-011 | coordenação de correção | required_before_integration | W0-05 | Domain/Platform | consumidor mínimo controlado | aplicação confirmada por consumidor |
| CC-W0-012 | coordenação de revogação | required_before_integration | W0-05 | Domain/Security | bloqueio central + consumidor mínimo | latência e confirmações medidas |
| CC-W0-013 | reconstrução e replay | required_before_integration | W0-03/W0-07 | Engineering/Data | replay do agregado e projeções mínimas | integridade e não reemissão de fatos |
| CC-W0-014 | proteção de referências de mídia | required_before_security_gate quando multimodal | W0-04 | Security/Data | POC restrita a um tipo de mídia | acesso, integridade e expiração |
| CC-W0-015 | classificação de sensibilidade | required_before_build | W0-02/W0-04 | Privacy/Security | tabela normativa versionada | canal, log, retenção e índice governados |
| CC-W0-016 | catálogo de erros | required_before_build | W0-02/W0-03 | Domain/Engineering | catálogo estável no código e schemas | código, significado e retry consistentes |

## 3. Dependências por incremento

### W0-01

- nenhuma dependência técnica externa obrigatória;
- exige owners provisórios e acesso ao repositório;
- deve criar mecanismo de registrar indisponibilidades.

### W0-02

- CC-W0-001;
- CC-W0-002;
- CC-W0-015;
- CC-W0-016.

### W0-03

- CC-W0-003;
- CC-W0-004;
- CC-W0-005;
- CC-W0-006;
- CC-W0-013.

### W0-04

- CC-W0-008;
- CC-W0-014;
- CC-W0-015.

### W0-05

- CC-W0-001;
- CC-W0-002;
- CC-W0-007;
- CC-W0-009;
- CC-W0-011;
- CC-W0-012.

### W0-06

- CC-W0-003;
- CC-W0-007;
- CC-W0-012;
- CC-W0-015.

### W0-07

- CC-W0-009;
- CC-W0-010;
- CC-W0-013;
- CC-W0-014 quando aplicável.

### W0-08

- todas as dependências obrigatórias com evidência válida;
- dependência ausente exige exceção formal ou bloqueia o gate afetado.

## 4. Requisitos de cada dependência

Cada capacidade deverá possuir:

- interface lógica;
- contrato e versão;
- owner;
- ambiente disponível;
- prazo de necessidade;
- risco de ausência;
- fallback explícito;
- limite do fallback;
- evidência de disponibilidade;
- plano de substituição quando provisória.

## 5. Política de fallback

Fallback é permitido apenas quando:

- preserva semântica e autoridade;
- não enfraquece segurança ou privacidade;
- não cria dependência irreversível;
- é limitado a ambiente e período;
- possui owner e data de expiração;
- produz evidência comparável;
- pode ser removido sem migrar significado do domínio.

## 6. Dependências não exigidas

Não bloqueiam o início da Onda 0:

- grafo global completo;
- busca semântica ampla;
- todos os canais de captura;
- todos os produtos Guivos;
- operação multi-país;
- automação integral pela Intelligence;
- topologia física definitiva;
- alta disponibilidade de produção;
- contrato comercial com fornecedores.

## 7. Critérios de bloqueio

Uma dependência bloqueia quando:

- capacidade obrigatória não existe;
- fallback amplia autoridade;
- contrato não está versionado;
- owner não está definido;
- risco crítico não possui mitigação;
- evidência está ausente ou expirada;
- comportamento diverge da autoridade normativa;
- dependência provisória é tratada como decisão permanente.

## 8. Revalidação

A matriz deverá ser revalidada:

- antes de cada incremento;
- após mudança de ADR tecnológico;
- após falha material;
- antes dos gates de dados e segurança;
- antes de qualquer ensaio interno;
- antes de propor a próxima onda.