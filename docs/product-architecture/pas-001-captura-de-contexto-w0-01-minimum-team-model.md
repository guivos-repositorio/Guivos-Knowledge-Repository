---
id: PAS-001-CC-W0-01-MINIMUM-TEAM-001
title: Modelo Mínimo de Equipe Técnica do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
related:
  - PAS-001-CC-W0-01-ROLE-PROFILES-001
  - PAS-001-CC-W0-01-CONFLICT-SEGREGATION-001
---

# PAS-001-CC-W0-01-MINIMUM-TEAM-001 — Modelo Mínimo de Equipe Técnica

## 1. Objetivo

Permitir uma estrutura inicial enxuta sem eliminar competências, independência crítica ou autoridade de interrupção.

## 2. Modelo mínimo recomendado

### Pessoa A — Technical Lead da Captura de Contexto

Pode acumular provisoriamente:

- Architecture Owner;
- Engineering Owner / Tech Lead;
- Platform/DevOps Owner.

Condições:

- demonstrar competência nos três escopos;
- Platform/DevOps possuir validade limitada ao W0-01;
- mudanças de segurança exigirem coaprovação de Security & Privacy;
- evidências exigirem revisão de Quality & Evidence;
- decisão arquitetural de alto custo possuir revisão independente quando disponível;
- a própria pessoa não ser única autora e aprovadora de mudança crítica.

### Pessoa B — Security & Privacy Owner

Deve permanecer independente de Engineering durante o W0-01.

Pode acumular consultoria jurídica ou privacidade operacional somente quando possuir competência e não houver conflito de autoridade.

### Pessoa C — Quality & Evidence Owner

Deve permanecer independente de Engineering para aprovação de EV-017, EV-018 e controles críticos.

Pode colaborar com testes, mas não ser único produtor e aprovador da mesma evidência.

## 3. Data Owner

O Data Owner deverá estar ativo antes do W0-03. Durante o W0-01 pode ser:

- papel futuro identificado;
- acumulado pelo Architecture Owner com competência comprovada;
- especialista dedicado;
- consultor com escopo delimitado.

Persistência, retenção, exclusão, restore e integridade exigirão revisão de Security & Privacy.

## 4. Modelo ideal posterior

A evolução esperada separa:

1. Architecture Owner;
2. Engineering Owner;
3. Security & Privacy Owner;
4. Quality & Evidence Owner;
5. Platform/DevOps Owner;
6. Data Owner quando a complexidade justificar.

A separação deverá ocorrer quando:

- carga operacional exceder capacidade;
- acúmulo comprometer revisão;
- ambientes integrados aumentarem risco;
- Internal Trial for proposto;
- incidentes demonstrarem conflito;
- especialização se tornar necessária.

## 5. Papéis de Guilherme Oliveira

Guilherme permanece:

- patrocinador executivo;
- autoridade de produto e propósito;
- aprovador de governança;
- administrador inicial provisório do GitHub.

Não acumula automaticamente owner técnico. Pode participar como `A`, `C` ou `I` conforme a matriz, mas aprovação técnica requer pessoa competente.

## 6. Capacidade mínima

Cada pessoa deverá declarar:

- disponibilidade semanal;
- janela de revisão;
- tempo de resposta para bloqueios;
- cobertura em ausência;
- duração do compromisso;
- limites de simultaneidade;
- outros projetos que gerem conflito.

## 7. Quórum mínimo por decisão

| Decisão | Quórum mínimo |
|---|---|
| ADR-TCC-001 | Technical Lead + Security/Privacy consultado + Quality consultado + governança |
| ADR-TCC-006 | Technical Lead + Security/Privacy + governança |
| branch protection | Technical Lead/Platform + Security/Privacy |
| pipeline mínimo | Engineering/Platform + Quality + Security consultado |
| dados sintéticos | Engineering + Security/Privacy + Quality |
| EV-017/EV-018 | Quality aprovador + owners produtores + governança |
| risco critical | Security ou owner competente + Architecture + Guilherme |
| encerramento W0-01 | todos os owners ativos + Guilherme |

## 8. Acúmulos proibidos

Durante o W0-01 são proibidos:

- uma única pessoa acumular todos os cinco papéis;
- Engineering e Quality como única dupla autora/aprovadora da mesma evidência;
- Engineering e Security na mesma pessoa sem revisão externa aprovada;
- administrador GitHub ser único aprovador de sua própria alteração de acesso;
- fornecedor controlar governança, execução e evidência sem segregação.

## 9. Delegação

Delegação temporária deverá possuir:

- pessoa de origem e destino;
- competência compatível;
- escopo;
- início e expiração;
- motivo;
- acessos;
- aprovador;
- condição de encerramento.

Delegação não pode superar a autoridade do papel original nem contornar segregação.

## 10. Critérios de suficiência

O modelo mínimo é suficiente somente quando:

- três pessoas distintas estiverem ativas;
- competências dos cinco papéis estiverem cobertas;
- Security e Quality forem independentes de Engineering;
- Platform acumulado possuir validade;
- quóruns estiverem definidos;
- conflitos estiverem tratados;
- EV-017 refletir a estrutura real.

## 11. Limites

O modelo mínimo não:

- recomenda contratação específica;
- define remuneração ou equity;
- substitui avaliação individual;
- autoriza acesso;
- autoriza W0-01;
- permanece válido automaticamente para Internal Trial ou produção.