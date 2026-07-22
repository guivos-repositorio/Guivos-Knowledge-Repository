---
id: GEM-006-CONCENTRATION-RESILIENCE-001
title: Concentração e Resiliência na Economia de Parceiros
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-006
---

# Concentração e Resiliência na Economia de Parceiros

## 1. Objetivo

Definir categorias de dependência e respostas conceituais para evitar concentração econômica, operacional, tecnológica, informacional ou de governança.

## 2. Dimensões de concentração

- receita;
- transações;
- recompensas;
- patrocínio;
- categoria de oferta;
- geografia;
- tecnologia;
- dados;
- distribuição;
- conhecimento;
- capacidade de suporte;
- poder de negociação;
- reputação associada.

## 3. Parceiro crítico

Um parceiro poderá ser considerado crítico quando sua interrupção comprometer:

- acesso;
- segurança;
- entrega;
- benefícios;
- recompensas;
- dados;
- confiança;
- continuidade econômica;
- operação de produto;
- obrigações existentes.

## 4. Registro de dependência

```yaml
partner_dependency_id: string
relationship_id: string
dependency_type: string
affected_products:
  - string
affected_actors:
  - string
criticality: not_assessed
substitution_options:
  - string
exit_constraints:
  - string
continuity_controls:
  - string
owner: string
status: open
```

## 5. Controles candidatos

- múltiplas alternativas;
- limites de escopo;
- ativação progressiva;
- interoperabilidade futura;
- portabilidade de dados;
- documentação;
- backup operacional;
- segregação de funções;
- renovação não automática de exclusividade;
- testes de saída;
- inventário de obrigações;
- reserva ou cobertura quando aplicável.

## 6. Riscos de concentração de poder

Um parceiro poderá influenciar indevidamente quando acumula:

- financiamento;
- validação;
- oferta;
- distribuição;
- dados;
- ranking;
- tecnologia;
- suporte;
- auditoria.

Esses papéis deverão ser segregados ou submetidos a controles adicionais.

## 7. Resiliência

Relacionamentos críticos deverão prever futuramente:

- substituição;
- redução de dependência;
- transição;
- preservação de dados;
- continuidade de suporte;
- tratamento de saldos e recompensas;
- comunicação;
- owner de contingência.

## 8. Sem limites numéricos

O GEM-006 não fixa percentuais máximos ou thresholds. A definição quantitativa dependerá de dados, modelo financeiro e governança posterior.

## 9. Fora do escopo

- cálculo de concentração;
- fornecedores alternativos;
- orçamento de contingência;
- arquitetura técnica;
- contratação.
