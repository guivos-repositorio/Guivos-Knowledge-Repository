---
id: GEM-008-REINVESTMENT-LIFECYCLE-001
title: Ciclo de Vida do Reinvestimento
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Ciclo de Vida do Reinvestimento

## 1. Objetivo

Definir o percurso conceitual de uma necessidade até sua revisão, sem autorizar alocação financeira ou execução.

## 2. Fluxo

```text
necessidade identificada
→ proposta
→ elegibilidade
→ evidência
→ priorização
→ autorização futura
→ alocação
→ execução
→ resultado observado
→ revisão
→ continuidade, correção ou encerramento
```

## 3. Estados

```yaml
reinvestment_status:
  identified |
  proposed |
  eligible |
  prioritized |
  approved_future |
  allocated |
  in_execution |
  completed |
  under_review |
  adjusted |
  suspended |
  terminated
```

## 4. Requisitos por transição

### `identified → proposed`

- problema ou oportunidade descrita;
- beneficiário;
- escopo;
- relação com propósito.

### `proposed → eligible`

- ausência de obrigação prioritária incompatível;
- fonte candidata legítima;
- riscos e externalidades registrados;
- capacidade mínima considerada.

### `eligible → prioritized`

- evidência proporcional;
- comparação com alternativas;
- impacto sobre gratuito e reservas;
- dependências e reversibilidade.

### `prioritized → approved_future`

Exige ciclo separado com autoridade, orçamento, valores e dependências especializadas.

### `allocated → in_execution`

Exige owner, plano, controles e evidência de disponibilidade.

### `completed → under_review`

Deverá avaliar entrega, resultado, custo, externalidades e aprendizagem.

## 5. Condições de suspensão

- obrigação protegida emergente;
- indisponibilidade de recurso;
- capacidade insuficiente;
- risco material;
- conflito de finalidade;
- externalidade não tratada;
- evidência invalidada;
- mudança de prioridade.

## 6. Regras

- proposta não cria direito a recurso;
- prioridade não equivale a autorização;
- alocação não equivale a resultado;
- resultado observado deverá ser separado de expectativa;
- encerramento deverá preservar registros e obrigações;
- nenhum estado operacional é alcançado neste documento.

## 7. Fora do escopo

- orçamento;
- aprovação real;
- valores;
- execução;
- métricas finais;
- sistema de gestão.