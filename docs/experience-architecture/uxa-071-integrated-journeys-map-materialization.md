---
id: UXA-071
title: Materialização Documental do Mapa Integrado de Jornadas e Transições
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
related:
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-SCENARIOS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Materialização Documental do Mapa Integrado de Jornadas e Transições

## 1. Objetivo

A UXA-071 materializa a primeira seção documental integrada das jornadas da Guivos dentro do próprio Guivos Knowledge Repository.

A seção organiza referências existentes para permitir:

- percorrer jornadas por participante;
- comparar perspectivas;
- localizar handoffs de autoridade;
- consultar cenários completos ou interrompidos;
- visualizar maturidade;
- identificar telas, transições e estados ausentes;
- rastrear cada item até seu artefato de origem.

## 2. Seção materializada

```text
docs/journeys/
├── index.md
├── person.md
├── collective.md
├── organization.md
├── handoffs.md
├── scenarios.md
├── screen-catalog.md
└── gaps.md
```

O termo anteriormente tratado como `domínio` corresponde exclusivamente a esta seção interna do GKR.

## 3. Participantes estruturais

- Pessoa;
- Coletivo;
- Organização.

Papéis como visitante, solicitante, participante, responsável, representante institucional, especialista e patrocinador permanecem perspectivas contextuais.

## 4. Resultado da materialização

Foram criados:

1. ponto de entrada da seção Jornadas Integradas;
2. mapa textual inicial da jornada da Pessoa;
3. mapa textual inicial da jornada do Coletivo;
4. mapa textual inicial da jornada da Organização;
5. matriz de handoffs entre participantes;
6. cenários documentais mínimos;
7. catálogo integrado inicial de telas;
8. fila priorizada de lacunas e continuidades ausentes.

## 5. Fonte única

A seção trabalha por referência. Ela não duplica SVGs, contratos, programas ou validações.

Em caso de divergência, prevalece o artefato canônico de origem. A presença de uma referência no mapa não altera status, prioridade, versão ou canonicidade.

## 6. Maturidade

| Camada | Estado proposto |
|---|---|
| programa funcional | concluído |
| seção Jornadas Integradas | materializada |
| mapas textuais iniciais | materializados |
| catálogo inicial | materializado |
| handoffs e cenários iniciais | materializados |
| validação funcional da seção | não iniciada |
| protótipo navegável | não iniciado |
| implementação técnica | não iniciada |

## 7. Lacunas evidenciadas

A materialização confirma, entre outras:

- ausência de Meus Coletivos;
- ausência da Central de Atualizações;
- reformulação não iniciada do Início do Participante;
- ausência da Visão Geral do Responsável;
- ausência da visão operacional completa das solicitações pelo Coletivo;
- materialização específica pendente da relação Organização–Coletivo;
- matriz visual institucional ainda incompleta;
- estados residuais do Opportunity Boost;
- necessidade de reconciliação integrada da Tela Hoje e continuidades.

## 8. Limites

A UXA-071 não:

- cria novo produto ou aplicação;
- cria domínio de internet;
- implementa motor de simulação;
- cria protótipo clicável;
- executa teste com pessoas;
- altera telas canônicas;
- preenche lacunas por inferência;
- inicia Engenharia de Produto;
- inicia automaticamente a validação funcional do mapa.

## 9. Critérios de saída

O pacote estará materializado quando:

- todos os arquivos previstos existirem;
- a navegação interna entre as vistas funcionar;
- participantes, cenários, handoffs, catálogo e lacunas estiverem representados;
- referências canônicas forem preservadas;
- nenhuma experiência ausente for apresentada como existente;
- a validação mecânica do repositório for aprovada.

## 10. Próxima transição recomendada

Pacote separado de **validação funcional da seção Jornadas Integradas**, com revisão de completude, autoridade, visibilidade, transições, retornos, exceções e consistência entre participantes.

Essa validação não iniciará protótipo ou Engenharia de Produto.
