---
id: GEM-010-SCENARIOS-AND-GATES-001
title: Cenários e Gates do GEM-010
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-010
---

# Cenários e Gates do GEM-010

## Cenários de validação

1. ausência de parâmetro material;
2. premissa expirada;
3. crescimento acima da capacidade;
4. receita reconhecida antes do caixa;
5. atraso de recebimento;
6. churn e CAC simultaneamente adversos;
7. margem positiva com caixa negativo;
8. break-even sem cobertura de capital de giro;
9. concentração de receita ou parceiro;
10. subsídio sem fonte suficiente;
11. reserva protegida tratada como caixa livre;
12. dupla contagem entre produtos;
13. expansão cambial ou inflacionária;
14. choque de custo e capacidade;
15. cenário expansivo sem funding.

## Gates

- G1: perímetro, data-base, horizonte e moeda explícitos;
- G2: premissas registradas e classificadas;
- G3: nenhum `TBD` alimenta resultado apresentado como válido;
- G4: drivers reconciliam com outputs;
- G5: receitas reconciliam com recebimentos;
- G6: custos reconciliam com capacidade;
- G7: resultado reconcilia com caixa e capital de giro;
- G8: transferências internas eliminadas;
- G9: reservas e recursos vinculados protegidos;
- G10: unit economics segmentado e limitado;
- G11: sensibilidade e estresse executados;
- G12: riscos e incertezas declarados;
- G13: revisão independente registrada;
- G14: validações financeira e contábil pendentes ou concluídas explicitamente;
- G15: uso decisório formalmente autorizado.

Falha em gate material impede o estado `approved_for_planning`.

