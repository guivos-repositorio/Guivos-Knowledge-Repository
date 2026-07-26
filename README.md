# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado atual

A autoridade única para o estado transversal vigente é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.25 — Wireframe Móvel do Mapa de Oportunidades Criado |
| Remediação | concluída; validação mecânica permanente ativa |
| Revisão da Arquitetura de Negócios | ativa; 18 decisões humanas concluídas |
| Guivos Journey | PAS-001 1.0.0; nove capacidades concluídas |
| Modelo Econômico | GEM-001 a GEM-010 documentariamente concluídos |
| Resultados Empresariais | 9 em validação, 3 fundidos e 6 rejeitados |
| Resultados canônicos | nenhum criado |
| Página Inicial pública | validada e materializada para computador |
| Início protegido da jornada | funcionalmente validado e reformulado |
| Wireframe do início protegido | não iniciado |
| Referência móvel da Home | não iniciada |
| Tela Hoje | entrada recorrente após compreensão confirmada |
| Mapa de Oportunidades | contrato e wireframe móvel de baixa fidelidade criados |
| Validação funcional do Mapa | não iniciada |
| Protótipo, design e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |
| Validação de Mercado | trilha operacional paralela preservada |

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

## Página Inicial pública

A Home explica concretamente o que é a Guivos, permite iniciar uma jornada ou explorar sem personalização, distingue caminhos pessoais, gerais e institucionais e não coleta texto pessoal, voz, arquivos ou fontes externas.

O wireframe vetorial para computador permanece uma hipótese monocromática de baixa fidelidade. Ele não representa a versão móvel, identidade visual ou implementação.

## Início protegido da jornada

O ambiente protegido deverá explicar o processo antes da autenticação e da coleta, separar criação de conta de autorização, preservar compartilhamento mínimo e progressivo, tratar texto, voz, arquivos e perguntas como alternativas, exigir revisão antes do processamento material, mostrar estados e falhas, permitir pausa, retirada, correção e exclusão e bloquear personalização antes do gate.

## Mapa de Oportunidades

O Mapa é uma superfície própria da navegação recorrente.

O wireframe móvel UXA-024 representa:

- pesquisa por oportunidade, Organização ou região;
- alternância entre mapa e lista;
- filtros compactos;
- camadas de oportunidades, Organizações, Coletivos e eventos;
- localização aproximada declarada;
- cartão selecionado com preço, distância, data, vagas e acessibilidade;
- explicação de relevância e relação comercial;
- ações para detalhe, salvamento e rota;
- controles de privacidade territorial.

Arquivo vetorial:

`docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`

A referência possui 390 por 844 pixels e não representa geografia real, tecnologia cartográfica, design ou implementação.

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

- validação funcional do wireframe do Mapa;
- estados alternativos do Mapa;
- referência do Mapa para computador;
- wireframe gráfico do início protegido;
- referência móvel da Home;
- validação da revisão da compreensão inicial;
- reaplicação dos quatro testes dos Resultados Empresariais;
- ajuste do AQS-O01 e consolidação canônica em fases posteriores.

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
- [Página Inicial e Início da Jornada](docs/experience-architecture/uxa-020-home-and-journey-entry.md)
- [Wireframe da Página Inicial Pública](docs/experience-architecture/uxa-022-public-home-low-fidelity-wireframe.md)
- [Validação do Início Protegido](docs/experience-architecture/uxa-023-protected-journey-entry-functional-validation-and-reformulation.md)
- [Wireframe do Mapa de Oportunidades](docs/experience-architecture/uxa-024-opportunity-map-low-fidelity-wireframe.md)
- [Guivos Enterprise Architecture](docs/enterprise-architecture/index.md)
- [Guivos Journey — PAS-001](docs/product-architecture/pas-001-guivos-journey.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Guivos Business Architecture](docs/business-architecture/index.md)
- [Business Outcomes](docs/business-architecture/strategy/business-outcomes.md)
- [Documentação completa](docs/index.md)

## Regra de leitura

Documentos normativos de domínio definem a arquitetura. O Registro do Estado Atual define o estado global vigente. Roadmaps, painéis, páginas iniciais e registros históricos não criam autorizações independentes.
