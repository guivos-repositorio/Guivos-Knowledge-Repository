# Guivos Knowledge Repository

O GKR é a fonte oficial, versionada e governada do conhecimento da Guivos.

## Estado vigente

Consulte o [Registro do Estado Atual](project/current-state-register.md) para a declaração oficial de era, marco, frentes, pausas e próximos atos governados.

| Dimensão | Situação |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.32 — Estado do Mapa sem Resultados Validado e Reformulado |
| Remediação | concluída; validação mecânica permanente ativa |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas |
| Resultados Empresariais | 9 em validação, 3 fundidos, 6 rejeitados e zero canônicos |
| Home pública | validada e materializada para computador |
| Início protegido | funcionalmente validado; wireframe pendente |
| Tela Hoje | entrada recorrente após compreensão confirmada |
| Mapa de Oportunidades | funcionalmente validado e reformulado |
| Estado sem localização | funcionalmente validado e reformulado |
| Lista do Mapa | funcionalmente validada e reformulada |
| Estado sem resultados | funcionalmente validado e reformulado |
| Demais estados do Mapa | governados; wireframes não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## Experiência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não entra entre a Home e a Tela Hoje.

## Estado sem resultados validado

A UXA-030 e a UXA-031 estabelecem o estado para uma consulta territorial concluída sem correspondências.

O estado reformulado apresenta:

- `0 resultados correspondem a esta consulta`;
- `Consulta concluída · cobertura verificada · atualizada agora`;
- ação `Ver cobertura`;
- região, busca e filtros preservados;
- total consolidado de filtros;
- ações explícitas para ampliar região, alterar período, revisar filtros ou editar busca;
- revisão antes de aplicar qualquer alteração;
- última alteração identificada e `Desfazer` condicional;
- seleção anterior fora da consulta atual;
- distinção entre ausência legítima, falha de fonte, indisponibilidade e cobertura parcial;
- continuidade entre Mapa e Lista;
- localização opcional;
- exploração geral sem alterar a consulta;
- tratamento textual sem mapa carregado;
- ausência de preenchimento patrocinado ou personalizado artificial.

Arquivo:

`assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg`

A validação é arquitetural e não equivale a teste com usuários, design, algoritmo ou conformidade técnica de acessibilidade.

## Acesso rápido

### Estado e governança

- [Registro do Estado Atual](project/current-state-register.md)
- [Roadmap](roadmap.md)
- [Painel de Conhecimento](project/knowledge-board.md)
- [Marcos Arquiteturais](project/architectural-milestones.md)
- [Matriz de Consolidação Canônica](project/canonical-consolidation-matrix.md)
- [Adendo Canônico do Estado sem Resultados](project/canonical-consolidation-matrix-uxa-030-addendum.md)
- [Adendo Canônico da Validação sem Resultados](project/canonical-consolidation-matrix-uxa-031-addendum.md)
- [Histórico 1.54.0](project/changelog-1.54.0-uxa-031.md)

### Arquiteturas e modelos

- [Guivos Enterprise Architecture](enterprise-architecture/index.md)
- [Guivos Journey — PAS-001](product-architecture/pas-001-guivos-journey.md)
- [Guivos Economic Model](economic-model/index.md)
- [Guivos Business Architecture](business-architecture/index.md)
- [Arquitetura da Experiência](experience-architecture/index.md)
- [Página Inicial e Início](experience-architecture/uxa-020-home-and-journey-entry.md)
- [Wireframe da Home](experience-architecture/uxa-022-public-home-low-fidelity-wireframe.md)
- [Validação do Início Protegido](experience-architecture/uxa-023-protected-journey-entry-functional-validation-and-reformulation.md)
- [Wireframe do Mapa](experience-architecture/uxa-024-opportunity-map-low-fidelity-wireframe.md)
- [Validação do Mapa](experience-architecture/uxa-025-opportunity-map-functional-validation-and-reformulation.md)
- [Mapa sem Localização](experience-architecture/uxa-026-opportunity-map-location-disabled-state.md)
- [Validação sem Localização](experience-architecture/uxa-027-opportunity-map-location-disabled-functional-validation-and-reformulation.md)
- [Lista do Mapa](experience-architecture/uxa-028-opportunity-map-list-state.md)
- [Validação da Lista](experience-architecture/uxa-029-opportunity-map-list-functional-validation-and-reformulation.md)
- [Mapa sem Resultados](experience-architecture/uxa-030-opportunity-map-no-results-state.md)
- [Validação sem Resultados](experience-architecture/uxa-031-opportunity-map-no-results-functional-validation-and-reformulation.md)

### Resultados Empresariais

- [Business Outcomes](business-architecture/strategy/business-outcomes.md)
- [Candidate Outcome Register](business-architecture/strategy/candidate-outcome-register.md)
- [Candidate Outcome Evaluation Matrix](business-architecture/strategy/candidate-outcome-evaluation-matrix.md)
- [Candidate Outcome Decision Register](business-architecture/strategy/candidate-outcome-decision-register.md)

## Próximos atos

Após nova autorização, poderão ocorrer separadamente: referência do Mapa para computador, wireframe do início protegido, referência móvel da Home, validação da compreensão inicial, demais estados do Mapa ou retomada dos testes dos Resultados Empresariais.

## Regra de precedência

As autoridades normativas de cada domínio definem o conteúdo arquitetural. O Registro do Estado Atual define o estado transversal vigente. Esta página não cria decisões ou autorizações próprias.
