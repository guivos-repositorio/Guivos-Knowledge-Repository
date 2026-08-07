---
id: GKR-CHANGELOG-UXA-087-001
title: Changelog — UXA-087 — Validação Funcional da Visão Geral do Responsável
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-087
  - GKR-STATE-001
related:
  - UXA-086
  - GKR-SURF-COL-002
  - GKR-SURF-COL-003
  - GKR-TRN-112
  - M7.74
normative: false
---

# Changelog — UXA-087 — Validação Funcional da Visão Geral do Responsável

## 1. Baseline

- base: integração da UXA-086;
- `GKR-STATE-001`: 2.12.0;
- marco: M7.73;
- SVGs: 98;
- validações funcionais registradas: 87;
- pendentes: 11;
- `GKR-SURF-COL-002`: materializado; validação pendente.

## 2. Mudança principal

A UXA-087 valida funcionalmente `GKR-SURF-COL-002 — Visão Geral do Responsável do Coletivo` após reformular o mesmo SVG desktop criado pela UXA-086.

## 3. Achados corrigidos

Foram corrigidos quatro pontos funcionais:

1. estado e escopo de autoridade antes implícitos;
2. prazo da atenção principal antes não verificável;
3. alternativa de adiamento antes insuficiente;
4. retorno ao contexto anterior antes não visível.

## 4. Veredito

**Aprovada após reformulação controlada no escopo da superfície.**

O veredito promove somente `GKR-SURF-COL-002` para `validado`.

## 5. Cobertura após o pacote

| Indicador | Antes | Depois |
|---|---:|---:|
| SVGs | 98 | 98 |
| associações individuais | 98 | 98 |
| perfis documentais | 24 | 24 |
| validações funcionais | 87 | 88 |
| pendentes | 11 | 10 |
| IDs com referência visual | 26 de 40 | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 | 13 |
| superfícies registradas | 40 | 40 |
| transições registradas | 37 | 37 |

Os dez pendentes remanescentes pertencem exclusivamente à UXA-055.

## 6. Continuidade preservada

`GKR-TRN-112` permanece `parcial`:

- origem `GKR-SURF-COL-002`: materializada e validada;
- destino `GKR-SURF-COL-003`: ainda sem superfície operacional própria.

A validação da origem não comprova o handoff ponta a ponta.

## 7. Estado proposto após integração

- `GKR-STATE-001`: 2.13.0;
- marco: M7.74;
- ROADMAP: 12.60.0;
- UXA-000: 0.80.0;
- Jornadas Integradas: 0.15.0;
- Galeria: 0.7.0;
- página de Coletivos: 0.5.0;
- Matriz por SVG: 0.5.0;
- Catálogo: 0.12.0;
- Lacunas: 0.12.0;
- Registro de Superfícies: 0.5.0;
- detalhamento do Coletivo: 0.4.0;
- Registro de Transições: permanece 0.4.0 porque a transição não muda de estado.

## 8. Limites

A UXA-087 não:

- cria novo SVG;
- materializa `GKR-SURF-COL-003`;
- valida `GKR-TRN-112` ponta a ponta;
- materializa Meus Coletivos, Central de Atualizações ou Início do Participante;
- promove a jornada do Coletivo;
- altera Resultados Empresariais;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-088.

## 9. Próxima frente possível

**UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo (`GKR-SURF-COL-003`)**, mediante autorização separada.
