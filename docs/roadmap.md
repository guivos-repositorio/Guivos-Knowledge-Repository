---
id: ROADMAP-12.66.0
title: Roadmap Arquitetural — Central de Atualizações Materializada
status: active
version: 12.66.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.65.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.80
---

# Roadmap Arquitetural — Central de Atualizações Materializada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Central de Atualizações materializada; validação funcional e TRN-110 ainda abertas | UXA-093; M7.80 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-093 |
| Galeria visual | `active` 0.12.0; 107 SVGs | UXA-093 |
| página de Coletivos | `active` 0.10.0 | UXA-093 |
| matriz por SVG | 107 arquivos / 27 perfis; `active` 0.10.0 | UXA-093 |
| validações funcionais vigentes de SVG | 96 | UXA-092 e pacotes anteriores |
| pendentes de validação específica | 11: 10 UXA-055 + PER-107 | UXA-055; UXA-093 |
| handoffs integralmente validados no fluxo de solicitação | 6 | UXA-090; UXA-092 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 a UXA-075 — estruturação e promoção seletiva das Jornadas Integradas
→ UXA-076 a UXA-080 — registros granulares
→ UXA-081 a UXA-085 — galeria e matriz governadas
→ UXA-086 — COL-002 materializada
→ UXA-087 — COL-002 reformulada e validada
→ UXA-088 — COL-003 materializada
→ UXA-089 — COL-003 reformulada e validada
→ UXA-090 — cinco handoffs elegíveis validados ponta a ponta
→ UXA-091 — PER-106 materializada e continuidade pós-aprovação refinada
→ UXA-092 — PER-106 e resultado aprovado reformulados e validados; TRN-108 validada integralmente
→ UXA-093 — PER-107 materializada como Central de Atualizações P0A móvel
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-093

| Dimensão | Resultado |
|---|---|
| GKR-SURF-PER-107 | materializado; validação funcional pendente |
| SVG de PER-107 | 1 novo SVG móvel; nenhum ativo anterior alterado |
| GKR-TRN-110 | parcial; ambos os endpoints materializados, ligação ainda não validada |
| GKR-TRN-111 | ausente; PER-108 não vigente |
| GKR-SURF-PER-108 | reformulação pendente |
| SVGs totais | 107 |
| perfis totais | 27 |
| validações vigentes | 96 |
| pendentes | 11: 10 UXA-055 + PER-107 |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato materializado da Central de Atualizações

`PER-107` é uma superfície pessoal de triagem. Cada atualização preserva, quando aplicável:

- origem;
- natureza;
- contexto;
- autoridade ou autor;
- data ou alteração;
- estado de leitura;
- necessidade de ação;
- prazo legítimo.

A Central não reduz comunicados, alertas, solicitações, perguntas, discussões, decisões, convites ou recomendações a um feed social único.

## 6. Controle de atenção

A ordenação pode considerar segurança, ação vinculada a compromisso aceito, alteração de atividade futura, resposta direta, prazo, preferência e recência.

Não podem dominar a ordem:

- potencial de engajamento;
- reações;
- popularidade;
- quantidade de mensagens;
- compra de plano;
- publicidade;
- interesse comercial não declarado.

Estado `lido` não significa concordância, presença, consentimento ou ação concluída.

## 7. Trilha governada

```text
COL-002 validada
→ TRN-112 integralmente validada
→ COL-003 validada
↔ TRN-105/106/107/109 integralmente validadas com PER-105
→ TRN-108 integralmente validada com PER-105 e PER-106
→ PER-106 validada
→ TRN-110 parcial
→ PER-107 materializada
→ somente depois validar PER-107 e TRN-110 como conjunto
```

## 8. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — validada
→ TRN-105/106/107/108/109/112 — integralmente validadas
→ PER-105 aprovado — validado
→ PER-106 — validada
→ TRN-110 — parcial
→ PER-107 — materializada; validação pendente
→ TRN-111 — ausente
→ PER-108 — reformulação pendente
```

## 9. Dívidas preservadas

- validação funcional de `PER-107` e revalidação integrada de `TRN-110`;
- estados P0B da Central: vazio, excesso de volume e baixa conectividade;
- estados P0B adicionais de `Meus Coletivos`;
- `PER-108` ainda não materializada na forma vigente;
- áreas P1 de comunicação especializada;
- dez estados da UXA-055 sem validação;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 10. Limites

A UXA-093 não valida `PER-107` ou `TRN-110`, não materializa `PER-108`, estados P0B ou áreas P1, não cria novo ID ou transição, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 11. Próxima iniciativa possível

> **UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**

A UXA-094 depende de autorização separada e não é iniciada por este pacote.