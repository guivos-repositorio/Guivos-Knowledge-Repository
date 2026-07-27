# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado atual

A autoridade única para o estado transversal vigente é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.31 — Estado do Mapa sem Resultados Criado |
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
| Estado sem resultados | wireframe móvel criado; validação funcional pendente |
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

A Home explica concretamente o que é a Guivos, permite iniciar uma jornada ou explorar sem personalização, distingue caminhos pessoais, gerais e institucionais e não coleta relato pessoal.

O ambiente protegido explica o processo antes da autenticação e da coleta, separa criação de conta de autorização, preserva compartilhamento mínimo, exige revisão e bloqueia personalização antes do gate.

## Mapa de Oportunidades

O Mapa é uma superfície própria da navegação recorrente e foi considerado funcionalmente válido após reformulação.

A UXA-024 e a UXA-025 estabelecem contexto `Agindo como`, pesquisa, Mapa e Lista sincronizados, filtros, resultados da área, camadas, legenda, privacidade, cartão selecionado, relação comercial e rota contextual.

Arquivo principal:

`docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`

## Estado sem localização

A UXA-026 e a UXA-027 estabelecem que a pessoa pode utilizar o Mapa sem conceder localização do dispositivo.

O estado apresenta posição não acessada, região manual distinta da posição pessoal, busca, filtros, ausência de marcador, salvamento, origem específica e continuidade para o Detalhe.

Arquivo:

`docs/assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg`

## Visualização em Lista validada

A UXA-028 e a UXA-029 estabelecem a Lista como representação textual integral da mesma consulta territorial do Mapa.

A reformulação apresenta:

- `LISTA TERRITORIAL DO MAPA · MESMA CONSULTA`;
- contexto `Agindo como: Pessoa`;
- região, busca e filtros preservados;
- total consolidado de filtros;
- quantidade e atualização dos resultados;
- ordenação explícita e explicável;
- cartões comparáveis com dados ausentes declarados;
- item selecionado preservado;
- explicação funcional e relação comercial separadas;
- salvamento, origem e Detalhe sem localização;
- retorno ao Mapa sem perda de contexto;
- funcionamento sem mapa carregado.

Arquivo:

`docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`

A referência possui 390 por 844 pixels. A validação é arquitetural e não representa teste com usuários, design ou implementação.

## Estado sem resultados

A UXA-030 cria a referência móvel para uma consulta territorial concluída sem correspondências.

O estado apresenta:

- região, busca e filtros preservados;
- total zero limitado à consulta atual;
- consulta concluída sem falha conhecida;
- ações separadas para ampliar região, alterar período, revisar filtros e editar busca;
- reversão da última alteração quando aplicável;
- distinção entre ausência legítima, falha de fonte e indisponibilidade;
- continuidade entre Mapa e Lista;
- localização opcional;
- ausência de preenchimento patrocinado ou personalizado artificial;
- funcionamento textual sem mapa carregado.

Arquivo:

`docs/assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg`

O estado ainda não foi funcionalmente validado.

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

- validação funcional do estado sem resultados;
- referência do Mapa para computador;
- wireframe gráfico do início protegido;
- referência móvel da Home;
- validação da revisão da compreensão inicial;
- validação da primeira Tela Hoje após a transição;
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
- [Adendo Canônico UXA-030](docs/project/canonical-consolidation-matrix-uxa-030-addendum.md)
- [Histórico 1.53.0](docs/project/changelog-1.53.0-uxa-030.md)
- [Guivos Enterprise Architecture](docs/enterprise-architecture/index.md)
- [Guivos Journey — PAS-001](docs/product-architecture/pas-001-guivos-journey.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Guivos Business Architecture](docs/business-architecture/index.md)
- [Business Outcomes](docs/business-architecture/strategy/business-outcomes.md)
- [Documentação completa](docs/index.md)

## Regra de leitura

Documentos normativos de domínio definem a arquitetura. O Registro do Estado Atual define o estado global vigente. Roadmaps, painéis, páginas iniciais e registros históricos não criam autorizações independentes.
