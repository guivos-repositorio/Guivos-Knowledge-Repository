---
id: GKR-CHANGELOG-UXA-099-001
title: Changelog — UXA-099 — Dez Estados Residuais do Opportunity Boost
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-099
related:
  - GKR-STATE-001
  - ROADMAP-12.72.0
  - M7.86
normative: false
---

# Changelog — UXA-099

## Estado proposto

- GKR-STATE: **2.25.0**;
- marco: **M7.86**;
- ROADMAP: **12.72.0**;
- UXA-000: **0.92.0**;
- Jornadas Integradas: **0.27.0**;
- catálogo integrado: **0.22.0**;
- galeria visual: **0.17.0**;
- matriz por SVG: **0.15.0**;
- registro de superfícies: **0.15.0**;
- registro de transições: **0.16.0**;
- lacunas: **0.24.0**.

## Mudança principal

A UXA-099 executa `V3 — dez estados residuais UXA-055` e valida funcionalmente os dez SVGs móveis residuais do Opportunity Boost.

Resultado:

- **8 SVGs aprovados sem alteração visual**;
- **2 SVGs reformulados e validados**;
- **0 SVGs novos**;
- **0 novos IDs de superfície ou transição**.

## Reformulações controladas

### Falha de atualização material do anunciante

A tentativa de reduzir capacidade de uma campanha ativa é informação material. Se a confirmação falhar:

- a versão confirmada permanece autoridade histórica e de configuração;
- a candidata não é aplicada;
- a entrega futura entra em pausa automática de proteção;
- eventos válidos anteriores permanecem preservados;
- retomada depende de confirmação válida e nova verificação dos gates;
- reenvio da mesma intenção não duplica versão, evento ou gasto.

### Revisão e reversão de preferências

Cada escolha exibida passa a registrar:

- tipo e objeto afetado;
- data de aplicação;
- superfície ou superfícies suportadas;
- escopo;
- estado atual;
- possibilidade de revisão e reversão.

## Contratos consolidados

- erro técnico patrocinado não é zero inventário;
- zero inventário elegível não amplia critérios automaticamente;
- baixa oferta orgânica reduz publicidade;
- catálogo, busca, região, filtros e ordenação orgânicos permanecem preservados;
- ocultar campanha, mostrar menos e desativar patrocinados possuem escopos distintos;
- denúncia de conteúdo e contestação de uso de dados permanecem fluxos distintos;
- identidade, motivo, preferência e contestação da pessoa não são revelados ao anunciante;
- repetição da mesma intenção é funcionalmente idempotente;
- validar `COM-005` não promove automaticamente `TRN-305`.

## Cobertura resultante

- 109 SVGs;
- 109 associações;
- 28 perfis;
- **109 validações funcionais vigentes**;
- **0 pendências de validação específica**;
- 30/40 IDs com referência visual;
- 9 responsabilidades sem SVG dedicado;
- 40 superfícies;
- 37 transições.

## Limites

A UXA-099 não valida `TRN-305` ponta a ponta, não executa `TRN-205`, `TRN-304` ou `TRN-306`, não define algoritmo, política jurídica final, cobrança, antifraude ou perfil publicitário, não promove jornadas e não inicia protótipo, teste, W0-01 ou Engenharia de Produto.

A próxima prioridade registrada após eventual integração é `V4 — efeito externo de oportunidades`. A UXA-100 não foi iniciada.
