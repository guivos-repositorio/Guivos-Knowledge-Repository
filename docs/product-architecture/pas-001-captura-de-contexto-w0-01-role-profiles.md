---
id: PAS-001-CC-W0-01-ROLE-PROFILES-001
title: Perfis dos Papéis Técnicos do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
related:
  - PAS-001-CC-W0-01-OWNERS-001
  - PAS-001-CC-W0-01-DECISIONS-001
---

# PAS-001-CC-W0-01-ROLE-PROFILES-001 — Perfis dos Papéis Técnicos

## 1. Regras gerais

Cada owner deverá demonstrar competência prática, capacidade de documentar decisões, disponibilidade compatível e compreensão dos limites de autoridade da Guivos.

Não são suficientes isoladamente:

- título de cargo;
- certificação sem experiência;
- indicação pessoal;
- participação societária;
- familiaridade genérica com tecnologia;
- declaração sem evidência.

## 2. Architecture Owner

### Missão

Preservar coerência entre domínio, contratos, decisões tecnológicas, segurança, dados e evolução arquitetural.

### Responsabilidades

- revisar limites de domínio;
- conduzir ADRs;
- impedir que tecnologia redefina autoridade funcional;
- revisar dependências e integração;
- aprovar mudanças em contratos funcionais;
- avaliar custo de reversão;
- manter rastreabilidade normativa.

### Competências obrigatórias

- arquitetura de software;
- modelagem de domínio ou DDD;
- APIs e contratos versionados;
- sistemas distribuídos;
- persistência, eventos e consistência;
- segurança por design;
- ADRs e documentação técnica;
- análise de trade-offs.

### Autoridade

Pode bloquear decisão incompatível com autoridade, integridade, segurança, revogação ou rastreabilidade. Não pode alterar propósito ou regra humana sem governança competente.

## 3. Engineering Owner / Tech Lead

### Missão

Transformar o contrato técnico em implementação controlada, testável e revisável.

### Responsabilidades

- organizar execução;
- definir padrões de código;
- revisar PRs;
- manter qualidade técnica;
- garantir testes e integração;
- gerir dívida técnica da Onda 0;
- responder por incidentes técnicos durante a execução.

### Competências obrigatórias

- backend e arquitetura de aplicação;
- tipagem e design de APIs;
- concorrência e idempotência;
- bancos e mensageria;
- testes automatizados;
- CI;
- revisão de código;
- observabilidade e segurança básica.

### Autoridade

Pode bloquear merge por falha técnica, contrato, teste ou risco. Não pode aprovar sozinho segurança, privacidade ou evidência que produziu.

## 4. Security & Privacy Owner

### Missão

Proteger pessoas, dados, autoridade, segredos e superfícies de ataque durante a Onda 0.

### Responsabilidades

- threat modeling;
- identidade, autorização e menor privilégio;
- privacidade e LGPD;
- gestão de segredos;
- criptografia aplicada;
- revisão de logs;
- segurança de pipeline e cloud;
- tratamento de riscos high e critical;
- resposta a incidentes.

### Competências obrigatórias

- application security;
- IAM;
- OWASP;
- cloud security;
- KMS ou mecanismos equivalentes;
- incident response;
- privacy by design;
- segurança de dados e modelos;
- auditoria técnica.

### Autoridade

Pode interromper fluxo por vazamento, segredo exposto, ampliação indevida de autoridade, uso de dados reais não autorizado, prompt injection material ou controle de acesso incompatível.

## 5. Quality & Evidence Owner

### Missão

Assegurar que critérios de aceite, testes, evidências e gates sejam reproduzíveis, íntegros e independentes.

### Responsabilidades

- estratégia de testes;
- critérios de aceite;
- validação de schemas de evidência;
- EV-017 e EV-018;
- preservação de falhas;
- rastreabilidade;
- revisão de cobertura;
- relatórios de gate;
- validade e expiração de evidências.

### Competências obrigatórias

- automação de testes;
- contract testing;
- testes de integração;
- qualidade de software;
- CI;
- análise de falhas;
- evidência reproduzível;
- controle de versão e integridade de artefatos.

### Autoridade

Pode rejeitar evidência insuficiente, não reproduzível, expirada ou produzida em ambiente inadequado. Não deve ser o único produtor e aprovador da mesma prova.

## 6. Platform/DevOps Owner

### Missão

Estabelecer repositório, pipeline, ambientes e credenciais com isolamento e reversibilidade.

### Responsabilidades

- criação e proteção do repositório;
- branch protection;
- GitHub Actions ou mecanismo aprovado;
- segredos e acessos;
- ambientes Local e Test;
- logs de automação;
- rollback;
- disponibilidade dos checks;
- inventário de credenciais.

### Competências obrigatórias

- GitHub e CI/CD;
- infraestrutura como código ou automação equivalente;
- gestão de segredos;
- cloud e redes básicas;
- observabilidade;
- permissões e menor privilégio;
- resposta a falhas de pipeline.

### Autoridade

Pode bloquear merge ou execução por configuração insegura, segredo exposto, ausência de proteção ou ambiente incompatível. Não autoriza produção.

## 7. Data Owner

### Missão

Preservar integridade, retenção, exclusão, restore e reconstrução dos dados funcionais e protegidos.

### Responsabilidades

- sistema de registro;
- modelos de persistência;
- retenção;
- backup e restore;
- integridade;
- classificação;
- reconstrução;
- exclusão e derivados.

É exigido antes do W0-03, não para a nomeação inicial do W0-01.

## 8. Disponibilidade mínima

Cada nomeação deverá declarar:

- horas ou capacidade semanal;
- janela de revisão;
- tempo de resposta para bloqueios;
- disponibilidade em incidentes;
- substituição em ausência;
- duração do compromisso.

## 9. Incompatibilidades

São incompatíveis com o papel:

- recusa em documentar decisões;
- ausência de revisão independente em controle crítico;
- tentativa de usar dados reais sem autorização;
- relativização de revogação, isolamento ou autoridade humana;
- conflito não declarado;
- indisponibilidade incompatível;
- acesso compartilhado ou não rastreável;
- promoção de POC a produção sem decisão.

## 10. Evidência de qualificação

A avaliação deverá citar projetos, decisões, artefatos, referências ou exercício controlado que sustentem cada competência obrigatória. A falta de evidência deverá aparecer como limitação, não ser presumida como atendida.