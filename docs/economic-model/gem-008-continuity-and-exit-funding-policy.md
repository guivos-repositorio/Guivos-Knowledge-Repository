---
id: GEM-008-CONTINUITY-AND-EXIT-FUNDING-POLICY-001
title: Política de Financiamento da Continuidade e Saída
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Política de Financiamento da Continuidade e Saída

## 1. Objetivo

Definir o que deverá ser considerado para financiar continuidade, recuperação, transição ou encerramento ordenado de produtos, programas, parceiros e capacidades críticas.

## 2. Eventos candidatos

- perda de cliente relevante;
- encerramento de patrocinador;
- falha ou saída de parceiro;
- indisponibilidade tecnológica;
- fraude;
- incidente de segurança ou privacidade;
- ruptura regulatória;
- queda de receita;
- crescimento excessivo;
- indisponibilidade de pessoa-chave;
- falha de benefício ou recompensa;
- encerramento de produto;
- interrupção regional.

## 3. Elementos mínimos

- escopo afetado;
- participantes e terceiros afetados;
- obrigações protegidas;
- dados e registros;
- parceiros;
- fontes econômicas;
- reservas candidatas;
- alternativa ou substituição;
- comunicação;
- retorno ao estado estável;
- encerramento e preservação histórica.

## 4. Estados

```yaml
continuity_status:
  not_assessed |
  planning_required |
  conceptually_planned |
  dependency_exposed |
  transition_required |
  exit_required |
  blocked
```

## 5. Prioridades

1. segurança de pessoas e dados;
2. direitos e obrigações existentes;
3. continuidade do valor essencial;
4. reembolso, repasse e recompensa coberta;
5. migração e portabilidade;
6. comunicação;
7. substituição;
8. encerramento de capacidades não essenciais;
9. reconstrução futura.

## 6. Regras

- saída não encerra obrigações anteriores;
- suspensão não autoriza perda de dados ou direitos;
- financiador que encerra participação não poderá revogar arbitrariamente benefício coberto;
- capacidade crítica deverá possuir alternativa ou tratamento explícito;
- continuidade não será declarada comprovada sem teste futuro;
- reserva candidata não é cobertura confirmada;
- produto poderá ser encerrado quando manutenção ampliar dano ou inviabilidade;
- encerramento deverá evitar pressão para contratação ou migração indevida.

## 7. Registro conceitual

```yaml
continuity_scope_id: string
trigger: string
critical_capabilities:
  - string
protected_obligations:
  - string
candidate_funding_sources:
  - string
reserve_classes:
  - string
substitution_defined: false
transition_defined: false
communication_defined: false
amount_defined: false
owner: null
```

## 8. Fora do escopo

- plano operacional real;
- RTO ou RPO;
- valores;
- reservas constituídas;
- fornecedores alternativos;
- contratos;
- execução.