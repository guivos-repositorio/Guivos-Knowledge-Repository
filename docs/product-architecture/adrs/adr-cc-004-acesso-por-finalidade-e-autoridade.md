---
id: ADR-CC-004
title: Modelo de Acesso por Finalidade e Autoridade
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001-CC-UIC-GUARDRAILS-ACCESS-001
  - PAS-001-CC-UIC-CONTRACTS-001
---

# ADR-CC-004 — Modelo de Acesso por Finalidade e Autoridade

## Status

`Proposed 0.1.0`.

## Contexto

Papéis isolados são insuficientes para a Captura de Contexto. O mesmo ator pode ter permissões distintas conforme participante, representação, finalidade, sensibilidade, estado, canal e operação. Conceder acesso por papel amplo permitiria que acesso técnico fosse confundido com autoridade funcional.

## Decisão

Adotar decisão de acesso composta por:

- identidade e nível de garantia;
- papel;
- autoridade funcional;
- finalidade;
- operação;
- participante e representação;
- natureza e sensibilidade;
- estado do ciclo de vida;
- canal e contexto de apresentação;
- restrições de retenção e revogação;
- decisão própria do consumidor.

A decisão padrão é negar. Proibições prevalecem sobre permissões.

## Regras

1. papel não concede autoridade automaticamente;
2. acesso técnico não permite confirmar ou autorizar;
3. finalidade genérica não autoriza propagação material;
4. representação possui escopo e prazo;
5. menor, terceiro e dispositivo compartilhado exigem proteção reforçada;
6. revogação bloqueia novos usos;
7. suporte e administração recebem visão minimizada;
8. consumidor realiza decisão própria;
9. busca aplica o escopo antes da recuperação;
10. toda decisão material é observável sem expor conteúdo bruto.

## Consequências positivas

- menor privilégio real;
- decisões contextualizadas;
- separação entre plataforma, Intelligence e autoridade humana;
- revogação e representação controláveis;
- auditoria de decisões materiais.

## Consequências negativas

- maior número de atributos e políticas;
- necessidade de sincronização entre identidade, domínio e consumidores;
- risco de negações indevidas se o contexto estiver incompleto;
- necessidade de testes combinatórios.

## Alternativas rejeitadas

### RBAC puro

Rejeitado por não representar finalidade, participante, estado, sensibilidade e representação.

### ACL por objeto

Rejeitada como modelo único por não expressar autoridade funcional e contexto temporal.

### Decisão delegada somente ao consumidor

Rejeitada porque a exposição já pode ocorrer antes da decisão do consumidor.

## Falha segura

Contexto ausente, expirado, incompatível ou não verificável resulta em negação material. Operações de proteção C0 permanecem disponíveis por caminho autorizado específico.

## Evidências requeridas

- matriz de atores e autoridades;
- testes de finalidade incompatível;
- testes de representação;
- testes de menor e terceiro;
- teste de revogação;
- teste de acesso administrativo;
- relatório de decisões permitidas e negadas.

## Decisões posteriores

Provedor de identidade, motor de autorização, formato de token, sessão e mecanismo físico de auditoria serão definidos em ADRs tecnológicos.