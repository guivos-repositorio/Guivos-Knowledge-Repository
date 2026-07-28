# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado atual

A autoridade única para o estado transversal vigente é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.34 — Referência do Mapa para Computador Funcionalmente Validada e Reformulada |
| Remediação | concluída; validação mecânica permanente ativa |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas |
| Guivos Journey | PAS-001 1.0.0; nove capacidades concluídas |
| Modelo Econômico | GEM-001 a GEM-010 documentariamente concluídos |
| Resultados Empresariais | 9 em validação, 3 fundidos e 6 rejeitados |
| Resultados canônicos | nenhum criado |
| Home pública | validada e materializada para computador |
| Início protegido | funcionalmente validado; wireframe pendente |
| Referência móvel da Home | não iniciada |
| Tela Hoje | entrada recorrente após compreensão confirmada |
| Mapa de Oportunidades | funcionalmente validado e reformulado |
| Estado sem localização | funcionalmente validado e reformulado |
| Lista do Mapa | funcionalmente validada e reformulada |
| Estado sem resultados | funcionalmente validado e reformulado |
| Referência do Mapa para computador | funcionalmente validada e reformulada |
| Referência para tablet | não iniciada |
| Demais estados do Mapa | governados; wireframes não iniciados |
| Protótipo, design e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |
| Validação de Mercado | trilha paralela preservada |

## Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não entra entre a Home e a Tela Hoje.

## Página Inicial e início protegido

A Home explica concretamente o que é a Guivos, permite iniciar uma jornada ou explorar sem personalização e não coleta relato pessoal.

O ambiente protegido explica o processo antes da autenticação e da coleta, separa criação de conta de autorização, exige revisão e bloqueia personalização antes do gate.

## Mapa de Oportunidades

O Mapa é uma superfície da navegação recorrente e foi considerado funcionalmente válido após reformulação.

A UXA-024 e a UXA-025 estabelecem contexto `Agindo como`, pesquisa, filtros, resultados, legenda, privacidade, seleção, relação comercial e rota contextual.

## Estados móveis validados

A UXA-026 a UXA-031 estabelecem:

- uso sem localização;
- região manual distinta da posição pessoal;
- Lista como representação textual da mesma consulta;
- filtros e quantidade preservados;
- cartões comparáveis;
- cobertura verificável;
- estado zero limitado à consulta atual;
- recuperação consciente;
- seleção anterior explicável;
- operação sem mapa carregado.

Arquivos móveis:

- `docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`;
- `docs/assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg`;
- `docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`;
- `docs/assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg`.

## Referência do Mapa para computador validada

A UXA-032 e a UXA-033 estabelecem dois wireframes de 1.440 por 1.024 pixels, funcionalmente válidos após reformulação:

- Mapa com resultados;
- Mapa sem resultados.

A referência apresenta:

- `Consulta territorial ativa` compartilhada;
- filtros com valores consistentes;
- `Visão dividida ativa`;
- foco no Mapa ou na Lista sem perda de contexto;
- retorno à visão dividida;
- movimento do Mapa sem atualização silenciosa;
- `Pesquisar nesta área` somente após movimento pendente;
- seleção `Marcador 1` sincronizada;
- cartões comparáveis com origem e explicação;
- `Entender ordenação`;
- relação comercial rotulada;
- painel contextual recolhível;
- recuperação do estado zero concentrada em `Consulta e filtros`;
- seleção anterior explicável;
- localização opcional;
- Lista integral sem mapa carregado.

Arquivos:

- `docs/assets/wireframes/uxa-032-opportunity-map-desktop.svg`;
- `docs/assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg`.

A validação não conclui responsividade, pontos de quebra, tablet, design, protótipo, teste com usuários, acessibilidade técnica ou implementação.

## Estado dos Resultados Empresariais

```text
Validação externa concluída
→ Matriz de Avaliação inicial concluída
→ 18 decisões humanas concluídas
→ 9 candidatos em validação, 3 fundidos e 6 rejeitados
→ reaplicação dos quatro testes após nova autorização
→ ajuste do AQS-O01
→ catálogos canônicos
→ Capacidades Empresariais
```

A fusão de BUS-CAND-010 em BUS-CAND-005 não aprova o candidato-alvo, não torna reinvestimento obrigatório e não cria Resultado canônico.

## Próximos atos possíveis

Nenhum movimento é automático. Após integração e nova autorização, poderão ocorrer separadamente:

- wireframe gráfico do início protegido;
- referência móvel da Home;
- validação da revisão da compreensão inicial;
- validação da primeira Tela Hoje após a transição;
- demais estados alternativos do Mapa;
- referência específica para tablet, caso priorizada;
- reaplicação dos quatro testes dos Resultados Empresariais.

## Backlog estratégico preservado

Após Resultados e Capacidades Empresariais, o portfólio será reavaliado a partir da ordem histórica:

1. Guivos Mall;
2. Guivos Business;
3. Guivos Intelligence;
4. Guivos Ads;
5. Guivos Media;
6. Guivos Travel;
7. Modelo Comercial;
8. Entrada no Mercado.

## Acesso principal

- [Estado atual oficial](docs/project/current-state-register.md)
- [Roadmap arquitetural](docs/roadmap.md)
- [Painel de Conhecimento](docs/project/knowledge-board.md)
- [Marcos Arquiteturais](docs/project/architectural-milestones.md)
- [Matriz de Consolidação Canônica](docs/project/canonical-consolidation-matrix.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Página Inicial e Início](docs/experience-architecture/uxa-020-home-and-journey-entry.md)
- [Wireframe da Home](docs/experience-architecture/uxa-022-public-home-low-fidelity-wireframe.md)
- [Validação do Início Protegido](docs/experience-architecture/uxa-023-protected-journey-entry-functional-validation-and-reformulation.md)
- [Wireframe do Mapa](docs/experience-architecture/uxa-024-opportunity-map-low-fidelity-wireframe.md)
- [Validação do Mapa](docs/experience-architecture/uxa-025-opportunity-map-functional-validation-and-reformulation.md)
- [Mapa sem Localização](docs/experience-architecture/uxa-026-opportunity-map-location-disabled-state.md)
- [Validação sem Localização](docs/experience-architecture/uxa-027-opportunity-map-location-disabled-functional-validation-and-reformulation.md)
- [Lista do Mapa](docs/experience-architecture/uxa-028-opportunity-map-list-state.md)
- [Validação da Lista](docs/experience-architecture/uxa-029-opportunity-map-list-functional-validation-and-reformulation.md)
- [Mapa sem Resultados](docs/experience-architecture/uxa-030-opportunity-map-no-results-state.md)
- [Validação sem Resultados](docs/experience-architecture/uxa-031-opportunity-map-no-results-functional-validation-and-reformulation.md)
- [Mapa para Computador](docs/experience-architecture/uxa-032-opportunity-map-desktop-reference.md)
- [Validação Desktop](docs/experience-architecture/uxa-033-opportunity-map-desktop-functional-validation-and-reformulation.md)
- [Adendo Canônico UXA-033](docs/project/canonical-consolidation-matrix-uxa-033-addendum.md)
- [Histórico 1.56.0](docs/project/changelog-1.56.0-uxa-033.md)
- [Guivos Enterprise Architecture](docs/enterprise-architecture/index.md)
- [Guivos Journey — PAS-001](docs/product-architecture/pas-001-guivos-journey.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Guivos Business Architecture](docs/business-architecture/index.md)
- [Business Outcomes](docs/business-architecture/strategy/business-outcomes.md)
- [Documentação completa](docs/index.md)

## Regra de leitura

Documentos normativos de domínio definem a arquitetura. O Registro do Estado Atual define o estado global vigente. Roadmaps, painéis, páginas iniciais e registros históricos não criam autorizações independentes.
