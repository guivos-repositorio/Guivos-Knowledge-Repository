---
id: GEM-008-CAPACITY-AND-SATURATION-MODEL-001
title: Modelo de Capacidade e Saturação
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Modelo de Capacidade e Saturação

## 1. Objetivo

Definir como capacidade, comprometimento, saturação e degradação deverão ser reconhecidos antes de crescimento, expansão ou aumento de obrigações.

## 2. Domínios de capacidade

- pessoas;
- tecnologia;
- infraestrutura;
- atendimento;
- parceiros;
- qualidade;
- segurança;
- privacidade;
- dados;
- governança;
- conhecimento;
- distribuição;
- operação econômica futura;
- suporte jurídico e regulatório futuro.

## 3. Estados

```yaml
capacity_status:
  not_assessed |
  available |
  partially_committed |
  committed |
  constrained |
  saturated |
  degraded |
  unavailable
```

## 4. Separações

- capacidade contratada não é capacidade disponível;
- capacidade instalada não é capacidade utilizável;
- capacidade utilizável não é qualidade garantida;
- demanda não é capacidade de atendimento;
- utilização máxima não é operação sustentável;
- crescimento não é prontidão;
- redundância declarada não é continuidade comprovada.

## 5. Sinais de saturação

- aumento recorrente de filas ou atrasos;
- suporte insuficiente;
- incidentes e retrabalho;
- degradação de qualidade;
- indisponibilidade de parceiros;
- concentração em pessoa-chave;
- falha de moderação ou contestação;
- sobrecarga de segurança;
- redução do baseline gratuito;
- obrigações acumuladas;
- ausência de capacidade de recuperação.

## 6. Tratamentos candidatos

- limitar escopo;
- reduzir volume;
- suspender expansão;
- priorizar obrigações essenciais;
- adicionar capacidade;
- substituir dependência;
- criar redundância;
- encerrar oferta;
- comunicar restrições;
- revisar promessa e entitlement.

## 7. Registro conceitual

```yaml
capacity_scope_id: string
domain: string
status: not_assessed
committed_to:
  - string
critical_dependencies:
  - string
quality_risks:
  - string
saturation_threshold_defined: false
continuity_defined: false
owner: null
```

## 8. Fora do escopo

- limites quantitativos;
- headcount;
- infraestrutura contratada;
- SLAs;
- arquitetura técnica;
- operação.