# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado atual

A autoridade única para o estado transversal vigente é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.36 — Wireframe Móvel do Início Protegido Funcionalmente Validado e Reformulado |
| Remediação | concluída; validação mecânica permanente ativa |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas |
| Guivos Journey | PAS-001 1.0.0; nove capacidades concluídas |
| Modelo Econômico | GEM-001 a GEM-010 documentariamente concluídos |
| Resultados Empresariais | 9 em validação, 3 fundidos e 6 rejeitados |
| Resultados canônicos | nenhum criado |
| Home pública | validada e materializada para computador |
| Início protegido móvel | funcionalmente validado e reformulado |
| Referência móvel da Home | não iniciada |
| Compreensão inicial | contrato estabelecido; materialização pendente |
| Tela Hoje | entrada recorrente após compreensão confirmada |
| Mapa e estados | funcionalmente validados e reformulados |
| Referência para tablet | não iniciada |
| Protótipo, design e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |
| Validação de Mercado | trilha paralela preservada |

## Sequência pessoal vigente

```text
Página Inicial pública
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## Página Inicial e início protegido

A Home explica concretamente o que é a Guivos, permite iniciar uma jornada ou explorar sem personalização e não coleta relato pessoal.

A UXA-023 governa o início protegido. A UXA-034 reformulada e a UXA-035 validam quatro estados móveis de 390 por 844 pixels:

1. explicação anterior ao relato;
2. acesso somente quando necessário;
3. escolha de modalidade e rascunho mínimo;
4. revisão anterior ao processamento específico.

O conjunto demonstra:

- relato pessoal separado de dados técnicos e de acesso;
- estados nomeados, pausáveis e retomáveis;
- ausência de formulário linear obrigatório;
- sessão válida sem repetição da etapa de acesso;
- texto, voz, arquivo e perguntas opcionais sem seleção automática;
- compartilhamento mínimo;
- explicação anterior para voz e arquivo;
- pausa, salvamento, saída e exclusão com efeitos distintos;
- inventário antes do processamento;
- autorização específica e inicialmente desmarcada;
- preparação apenas de compreensão inicial temporária e revisável;
- recusa sem processamento;
- persistência e personalização bloqueadas até a revisão da compreensão.

Arquivos:

- `docs/assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-access-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-review-mobile.svg`.

A validação não conclui autenticação, segurança técnica, armazenamento, gravação, upload, IA, protótipo, teste ou desenvolvimento.

## Mapa de Oportunidades

A UXA-024 a UXA-033 estabelecem o Mapa principal, uso sem localização, Lista territorial, estado sem resultados e referência para computador, com consulta compartilhada, explicabilidade, privacidade, seleção e resiliência.

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

- referência móvel da Home;
- materialização da revisão da compreensão inicial;
- validação da primeira Tela Hoje após a transição;
- estados especializados de texto, voz e arquivos;
- referência do início protegido para computador;
- estados de processamento, pausa, falha e retomada;
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
- [Contrato do Início Protegido](docs/experience-architecture/uxa-023-protected-journey-entry-functional-validation-and-reformulation.md)
- [Wireframe do Início Protegido](docs/experience-architecture/uxa-034-protected-journey-entry-low-fidelity-wireframe.md)
- [Validação do Wireframe Protegido](docs/experience-architecture/uxa-035-protected-journey-entry-wireframe-functional-validation-and-reformulation.md)
- [Wireframe do Mapa](docs/experience-architecture/uxa-024-opportunity-map-low-fidelity-wireframe.md)
- [Validação Desktop do Mapa](docs/experience-architecture/uxa-033-opportunity-map-desktop-functional-validation-and-reformulation.md)
- [Adendo Canônico UXA-035](docs/project/canonical-consolidation-matrix-uxa-035-addendum.md)
- [Histórico 1.58.0](docs/project/changelog-1.58.0-uxa-035.md)
- [Guivos Enterprise Architecture](docs/enterprise-architecture/index.md)
- [Guivos Journey — PAS-001](docs/product-architecture/pas-001-guivos-journey.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Guivos Business Architecture](docs/business-architecture/index.md)
- [Business Outcomes](docs/business-architecture/strategy/business-outcomes.md)
- [Documentação completa](docs/index.md)

## Regra de leitura

Documentos normativos de domínio definem a arquitetura. O Registro do Estado Atual define o estado global vigente. Roadmaps, painéis, páginas iniciais e registros históricos não criam autorizações independentes.
