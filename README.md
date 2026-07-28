# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado atual

A autoridade única para o estado transversal vigente é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.39 — Baseline Comercial de Planos, Benefícios e Preços Definida |
| Remediação | concluída; validação mecânica permanente ativa |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas |
| Guivos Journey | PAS-001 1.0.0; nove capacidades concluídas |
| Modelo Econômico | arquitetura inicial concluída; baseline comercial candidata definida |
| Planos para Pessoas | Free, Plus e Pro definidos |
| Planos para Coletivos | Livre, Gestão, Impacto e Enterprise definidos |
| Planos para Organizações | Business Start, Growth e Scale definidos |
| Preços | candidatos para validação; cobrança não autorizada |
| Resultados Empresariais | 9 em validação, 3 fundidos e 6 rejeitados |
| Resultados canônicos | nenhum criado |
| Home pública | validada e materializada para computador |
| Início protegido móvel | funcionalmente validado e reformulado |
| Compreensão inicial móvel | funcionalmente validada e reformulada em cinco estados |
| Referência móvel da Home | não iniciada |
| Tela Hoje | entrada recorrente após condição explicitamente escolhida |
| Mapa e estados | funcionalmente validados e reformulados |
| Protótipo, design e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |
| Validação de Mercado | planos, limites e preços ainda não testados |

## Baseline comercial candidata

### Pessoas

| Plano | Preço mensal | Preço anual | Ampliação principal |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | catálogo público completo e 2 correspondências personalizadas por semana |
| Guivos Plus | R$ 24,90 | R$ 249,00 | correspondências, filtros, alertas e histórico ampliados |
| Guivos Pro | R$ 49,90 | R$ 499,00 | análises, integrações, relatórios e suporte avançados |

### Coletivos

| Plano | Preço mensal | Preço anual | Limite principal |
|---|---:|---:|---|
| Coletivo Livre | R$ 0,00 | R$ 0,00 | 1 atividade e 1 oportunidade gratuitas/mês; 2 ativas |
| Coletivo Gestão | R$ 89,90 | R$ 899,00 | 4 atividades, 4 oportunidades e 6 ativas; monetização permitida |
| Coletivo Impacto | R$ 249,90 | R$ 2.499,00 | 15 atividades, 15 oportunidades e 20 ativas |
| Coletivo Enterprise | sob consulta | contrato anual | capacidade contratada, categorias personalizáveis, API, SSO e SLA |

### Organizações

| Plano | Preço mensal | Preço anual | Limite principal |
|---|---:|---:|---|
| Business Start | R$ 299,00 | R$ 2.990,00 | 10 novos programas ou oportunidades/mês; 15 ativos |
| Business Growth | R$ 799,00 | R$ 7.990,00 | 50 novos/mês; 75 ativos; até 5 unidades |
| Business Scale | a partir de R$ 1.990,00 | contrato anual | capacidade contratada, API, SSO, Power BI e SLA |

Os valores não constituem oferta pública, autorização de cobrança, orçamento ou viabilidade comprovada.

## Regras comerciais centrais

- o catálogo público permanece acessível no Guivos Free;
- a cota individual limita correspondências personalizadas, não oportunidades públicas;
- Coletivo Livre publica somente atividades e oportunidades gratuitas;
- publicação paga exige Coletivo Gestão ou superior;
- pessoa gratuita pode adquirir atividade paga sem assinar Plus ou Pro;
- assinatura, transação, comissão, taxa do meio de pagamento e tributo permanecem separados;
- cota atingida não reduz a visibilidade de publicação existente;
- Enterprise e Scale operam por capacidade contratada e uso justo;
- plano pago não aumenta ranking, relevância, impacto ou evidência;
- oferta não poderá interromper consentimento, compreensão, revisão ou controle de dados.

## Sequência pessoal vigente

```text
Página Inicial pública
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ processamento temporário visível e interrompível
→ compreensão inicial apresentada como hipótese
→ revisão por afirmação
→ decisões independentes sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

Oferta de plano não entra nessa sequência protegida antes da Tela Hoje.

## Compreensão inicial móvel validada

A UXA-036 reformulada e a UXA-037 estabelecem cinco estados:

1. processamento temporário visível e interrompível;
2. compreensão apresentada como hipótese;
3. revisão por afirmação, correção e limitação;
4. decisões independentes sobre persistência e personalização;
5. base autorizada insuficiente.

O conjunto preserva interrupção sem tarefa oculta, afirmações individualizadas, revisão sem resposta padrão, relato original separado, decisões independentes e continuidade sem personalização.

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

- validação de planos, limites e disposição a pagar;
- modelagem de custos, margem e unit economics;
- definição de comissão e política transacional;
- arquitetura da página de Planos e Preços;
- referência móvel da Home;
- validação da transição para a primeira Tela Hoje;
- reaplicação dos quatro testes dos Resultados Empresariais.

## Acesso principal

- [Estado atual oficial](docs/project/current-state-register.md)
- [Roadmap arquitetural](docs/roadmap.md)
- [Painel de Conhecimento](docs/project/knowledge-board.md)
- [Marcos Arquiteturais](docs/project/architectural-milestones.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Catálogo de Planos e Preços](docs/economic-model/gem-004-a1-commercial-plans-pricing-catalog.md)
- [Política Comercial de Planos](docs/economic-model/gem-004-a2-commercial-offer-upgrade-and-lifecycle-policy.md)
- [Premissas de Precificação](docs/economic-model/gem-010-a1-pricing-assumptions-and-validation.md)
- [Revisão da Baseline Comercial](docs/economic-model/gem-commercial-plans-baseline-review.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Wireframe da Compreensão Inicial](docs/experience-architecture/uxa-036-initial-understanding-low-fidelity-wireframe.md)
- [Validação da Compreensão Inicial](docs/experience-architecture/uxa-037-initial-understanding-wireframe-functional-validation-and-reformulation.md)
- [Adendo Canônico dos Planos](docs/project/canonical-consolidation-matrix-gem-commercial-plans-addendum.md)
- [Histórico 1.61.0](docs/project/changelog-1.61.0-gem-commercial-plans.md)
- [Guivos Business Architecture](docs/business-architecture/index.md)
- [Documentação completa](docs/index.md)

## Regra de leitura

Documentos normativos de domínio definem a arquitetura. O Registro do Estado Atual define o estado global vigente. Roadmaps, painéis, páginas iniciais e registros históricos não criam autorizações independentes.
