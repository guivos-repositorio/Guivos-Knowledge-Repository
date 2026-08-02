# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository é a fonte oficial, versionada e governada do conhecimento da Guivos. Ele reúne fundamentos, arquiteturas, modelos, decisões, especificações e o histórico de evolução do ecossistema.

## Estado atual

A autoridade única para o estado transversal vigente é o [Registro do Estado Atual](docs/project/current-state-register.md).

| Elemento | Estado resumido |
|---|---|
| Era | GE-2 — Knowledge |
| Marco | M7.48 — Gestão da Campanha Ativa do Opportunity Boost Materializada |
| Remediação | concluída; validação mecânica permanente ativa |
| Arquitetura de Negócios | 18 decisões humanas; zero Resultados canônicos |
| Modelo Econômico | planos e Opportunity Boost candidatos definidos |
| Planos para Pessoas | Free, Plus e Pro |
| Planos para Coletivos | Livre, Gestão, Impacto e Enterprise |
| Planos para Organizações | Business Start, Growth e Scale |
| Opportunity Boost | add-on publicitário separado dos planos |
| Experiência do Boost | validada e reformulada |
| Fluxo do anunciante | cinco wireframes validados e reformulados |
| Cartão e explicação | seis wireframes validados e reformulados |
| Lista e Mapa patrocinados | quatro wireframes validados e reformulados |
| Gestão da campanha ativa | seis wireframes para computador criados; validação pendente |
| Guivos Ads | operador econômico do Boost |
| Preços | candidatos; cobrança não autorizada |
| Home, início e compreensão | funcionalmente validados |
| Mapa | estados orgânicos e patrocinados funcionalmente validados |
| Protótipo, design e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## Baseline comercial de planos

### Pessoas

| Plano | Mensal | Anual |
|---|---:|---:|
| Guivos Free | R$ 0,00 | R$ 0,00 |
| Guivos Plus | R$ 24,90 | R$ 249,00 |
| Guivos Pro | R$ 49,90 | R$ 499,00 |

### Coletivos

| Plano | Mensal | Anual |
|---|---:|---:|
| Coletivo Livre | R$ 0,00 | R$ 0,00 |
| Coletivo Gestão | R$ 89,90 | R$ 899,00 |
| Coletivo Impacto | R$ 249,90 | R$ 2.499,00 |
| Coletivo Enterprise | sob consulta | contrato anual |

### Organizações

| Plano | Mensal | Anual |
|---|---:|---:|
| Business Start | R$ 299,00 | R$ 2.990,00 |
| Business Growth | R$ 799,00 | R$ 7.990,00 |
| Business Scale | a partir de R$ 1.990,00 | contrato anual |

Todos os valores permanecem candidatos para validação.

## Opportunity Boost

O Opportunity Boost permite ampliar a distribuição publicitária identificada de uma oportunidade aprovada e ativa.

### Elegibilidade

- Coletivo Gestão, Impacto e Enterprise;
- Business Start, Growth e Scale;
- Coletivo Livre somente por Boost Social Financiado;
- oportunidade ativa, atualizada e com capacidade de atendimento.

### Orçamento candidato

| Modalidade | Orçamento mínimo |
|---|---:|
| Boost Local | R$ 30,00 |
| Boost Regional | R$ 100,00 |
| Boost Ampliado | R$ 300,00 |
| Boost Gerenciado | a partir de R$ 1.000,00 |

- CPM candidato: R$ 12,00 a R$ 25,00;
- CPC candidato: R$ 0,80 a R$ 2,50;
- uma campanha não será cobrada simultaneamente por CPM e CPC;
- orçamento limitado e sem renovação automática por padrão.

### Experiência validada

A validação funcional estabeleceu bloqueios explicáveis, objetivo único, critérios utilizados e proibidos visíveis, prévia separada do ranking orgânico, pausa por alteração material, estados completos, identificação do Boost Social Financiado, controles reversíveis, proteção da densidade e relatório futuro em quatro camadas.

### Fluxo do anunciante validado

A UXA-040 reformulada e a UXA-041 validam cinco wireframes para computador: elegibilidade, objetivo e critérios, orçamento e duração, prévia e confirmação e envio para avaliação.

### Cartão patrocinado e explicação validados

A UXA-042 reformulada e a UXA-043 validam seis wireframes móveis e para computador, incluindo Boost Social Financiado, com natureza comercial anterior ao conteúdo, critérios protegidos excluídos e controles reversíveis.

### Lista e Mapa patrocinados validados

A UXA-044 reformulada e a UXA-045 validam quatro wireframes com uma única consulta territorial, contagens orgânicas e pagas separadas, filtros distintos da preferência publicitária, marcadores próprios, seleção sem alteração da ordem da Lista, localização opcional, gate `Pesquisar nesta área` e ocultação sincronizada sem perda do catálogo orgânico.

### Gestão da campanha ativa materializada

A UXA-046 cria seis wireframes para computador:

1. campanha programada;
2. campanha ativa;
3. campanha limitada;
4. campanha pausada;
5. alteração material;
6. encerramento e cancelamento.

O conjunto apresenta programação sem entrega, orçamento reservado, utilizado e saldo separados, indicadores operacionais distintos de relatório agregado, limitação sem aceleração de orçamento, pausas com causas próprias, alteração material com nova avaliação, eventos e histórico preservados e cancelamento com confirmação proporcional.

Os seis artefatos ainda exigem validação funcional. Nenhuma campanha, cobrança ou entrega real foi iniciada.

### Regras centrais

- ranking orgânico permanece independente de pagamento;
- anúncio é identificado como `Patrocinado` ou `Impulsionado`;
- densidade candidata máxima de 20%;
- duas unidades patrocinadas consecutivas são proibidas;
- marcador patrocinado não encobre oportunidade orgânica;
- localização permanece opcional e posição exata não alimenta publicidade;
- movimentação do Mapa não autoriza localização ou nova consulta;
- limitação não acelera orçamento;
- pausa interrompe entrega futura;
- alteração material impede entrega desatualizada;
- cancelamento preserva eventos válidos e histórico;
- saldo não é devolução confirmada;
- compreensão inicial, Momento Atual e Próximo Passo não alimentam segmentação;
- Tela Hoje e Jornada pessoal não recebem Boost nesta baseline;
- anunciante não recebe lista de visualizadores;
- alcance pago não equivale a recomendação, conversão ou impacto.

## Regras comerciais preservadas

- catálogo público permanece acessível no Guivos Free;
- Coletivo Livre publica somente ofertas gratuitas;
- publicação paga exige Coletivo Gestão ou superior;
- pessoa gratuita pode adquirir atividade paga;
- plano, transação, comissão, Boost, taxa de pagamento e tributo permanecem separados;
- pagamento não aumenta relevância, confiança, impacto ou evidência;
- oferta e publicidade não entram no fluxo protegido de compreensão e autorização.

## Sequência pessoal vigente

```text
Página Inicial pública
→ explicação do ambiente protegido
→ acesso quando necessário
→ relato mínimo revisado e autorizado
→ compreensão inicial como hipótese
→ decisões independentes sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## Resultados Empresariais

```text
18 decisões humanas concluídas
→ 9 candidatos em validação
→ 3 fundidos
→ 6 rejeitados
→ 0 Resultados canônicos
```

## Próximos atos possíveis

Nenhum movimento é automático. Após integração e nova autorização, poderão ocorrer separadamente:

- validação funcional e reformulação dos wireframes da UXA-046;
- wireframe do relatório agregado;
- validação funcional do conjunto completo;
- estados móveis de gestão, se priorizados;
- estados de erro, inventário insuficiente e preferência publicitária;
- pesquisa de disposição a pagar;
- calibração de orçamento, CPM ou CPC;
- política especializada de publicidade;
- custos, antifraude e unit economics;
- revisões especializadas;
- página de Planos e Preços;
- política transacional;
- transição para a primeira Tela Hoje;
- retomada dos testes dos Resultados Empresariais.

## Acesso principal

- [Estado atual oficial](docs/project/current-state-register.md)
- [Roadmap arquitetural](docs/roadmap.md)
- [Painel de Conhecimento](docs/project/knowledge-board.md)
- [Marcos Arquiteturais](docs/project/architectural-milestones.md)
- [Guivos Economic Model](docs/economic-model/index.md)
- [Catálogo de Planos e Preços](docs/economic-model/gem-004-a1-commercial-plans-pricing-catalog.md)
- [Contrato Econômico do Opportunity Boost](docs/economic-model/gem-007-a1-opportunity-boost-economic-and-product-contract.md)
- [Preços e Mensuração do Opportunity Boost](docs/economic-model/gem-010-a2-opportunity-boost-pricing-budget-and-measurement.md)
- [Contrato Funcional Reformulado do Boost](docs/experience-architecture/uxa-038-opportunity-boost-functional-experience-contract.md)
- [Validação Funcional do Boost](docs/experience-architecture/uxa-039-opportunity-boost-functional-validation-and-reformulation.md)
- [Wireframes do Fluxo do Anunciante](docs/experience-architecture/uxa-040-opportunity-boost-advertiser-flow-low-fidelity-wireframes.md)
- [Validação dos Wireframes do Anunciante](docs/experience-architecture/uxa-041-opportunity-boost-advertiser-wireframe-functional-validation-and-reformulation.md)
- [Cartão Patrocinado e Explicação](docs/experience-architecture/uxa-042-opportunity-boost-sponsored-card-and-explanation-low-fidelity-wireframes.md)
- [Validação do Cartão e Explicação](docs/experience-architecture/uxa-043-opportunity-boost-sponsored-card-functional-validation-and-reformulation.md)
- [Estados Patrocinados de Lista e Mapa](docs/experience-architecture/uxa-044-opportunity-boost-sponsored-list-and-map-low-fidelity-wireframes.md)
- [Validação dos Estados Patrocinados de Lista e Mapa](docs/experience-architecture/uxa-045-opportunity-boost-sponsored-list-map-functional-validation-and-reformulation.md)
- [Gestão da Campanha Ativa](docs/experience-architecture/uxa-046-opportunity-boost-active-campaign-management-low-fidelity-wireframes.md)
- [Adendo Canônico da UXA-046](docs/project/canonical-consolidation-matrix-uxa-046-addendum.md)
- [Histórico 1.70.0](docs/project/changelog-1.70.0-uxa-046.md)
- [Arquitetura da Experiência](docs/experience-architecture/index.md)
- [Guivos Business Architecture](docs/business-architecture/index.md)
- [Documentação completa](docs/index.md)

## Regra de leitura

Documentos normativos de domínio definem a arquitetura. O Registro do Estado Atual define o estado global vigente. Roadmaps, painéis, páginas iniciais e registros históricos não criam autorizações independentes.
