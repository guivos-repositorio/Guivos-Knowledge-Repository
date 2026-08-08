---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.28.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - GPA-007
  - UXA-000
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-101
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GTM-000
  - GTM-006
  - ADR-007
  - GEA-GRAPH-REFERENCE-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
  - GKR-DIGITAL-ASSET-CONTROL-001
  - VAL-009
  - VAL-010
  - GEM-005-A1
  - GKR-VALIDATED-UPDATES-SYNC-2026-08-08-001
  - ROADMAP-12.75.0
  - M7.88
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente da `main` após a sincronização governada das validações recentes de 2026-08-08.

Em caso de divergência entre este registro e resumos não normativos, prevalece `GKR-STATE-001` e, para cada domínio, a autoridade temática mais específica e mais recente.

A sincronização temática **não cria novo marco funcional UXA**. O marco funcional permanece `M7.88`, encerrado pela UXA-101 no limite controlável pela Guivos.

## 2. Estado global vigente

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco funcional | **M7.88 — saída consciente para fronteira externa validada** | UXA-101 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** | UXA-101 |
| Galeria visual | `active` 0.21.0; **118 SVGs** | UXA-101 |
| Matriz por SVG | `active` 0.17.0; **118 arquivos / 31 perfis** | UXA-101 |
| Jornadas Integradas | `active` 0.31.0; Pessoa, Coletivo e Organização permanecem `draft` | UXA-101 |
| Taxonomia de planos | autoridade consolidada | GEM-004-PLAN-TAXONOMY-AUTHORITY-001 |
| Go-to-Market | domínio integrado; metas continuam candidatas/cenários onde indicado | GTM-000 a GTM-006 |
| Grafo | Neo4j selecionado como tecnologia primária de referência | ADR-007 |
| Produtos Especializados | sete produtos rebaselineados contra jornadas e handoffs | GPA-SPECIALIZED-EXPERIENCE-POLICY-001 |
| Marca/naming/ativos | governança documental integrada; fatos registrários dependem de evidência | GKR-BRAND-ASSET-GOVERNANCE-001 |
| Validação de mercado | método e gates de evidência integrados; resultado real não estabelecido | VAL-009; VAL-010 |
| Incentivos | guardrail ativo de propósito antes da recompensa | GEM-005-A1 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura funcional e visual preservada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica de SVG | **0** |
| IDs granulares com referência visual | **42 de 53** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela por definição | **2** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |

A sincronização P1.1/P2/P3/P4/P8 e o guardrail GEM-005-A1 não criam SVG, `SURF`, `TRN`, `BND` ou nova UXA.

## 4. Estado da Arquitetura da Experiência

A sequência funcional recente permanece:

```text
UXA-097 — compreensão inicial → primeira Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos, comparação, contratação e estados de pagamento
→ UXA-101 — revisão consciente → TRN-205 → BND-001
```

A UXA-101 encerra V4 no limite documental controlável pela Guivos:

```text
PER-203 — Detalhe
→ revisão consciente de saída
→ TRN-205
→ BND-001 — autoridade externa
```

Nenhuma inscrição, reserva, compra, contratação, presença ou outro resultado posterior a `BND-001` é presumido pela Guivos.

Continuidades preservadas:

- `TRN-007` integralmente validada pela UXA-097;
- `TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` integralmente validadas pela UXA-098;
- `COM-005` funcionalmente validado pela UXA-099;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`;
- 15 transições internas de Planos permanecem localmente validadas;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais.

## 5. Taxonomia vigente de participantes e planos

A autoridade consolidada é:

- **Pessoa:** Free · Plus · Pro;
- **Coletivo:** Livre · Mobiliza · Impacta · Rede;
- **Organização:** Conecta · Eleva · Transforma;
- **Guivos Business:** Start · Growth · Scale · Enterprise.

Regras estruturais:

- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- não existe correspondência automática 1:1 entre planos de Organização e tiers de Business;
- plano representa profundidade de serviço, capacidade, escopo ou complexidade atendida — nunca valor humano, mérito, prestígio ou nível de evolução;
- `BND-002` é fronteira genérica de contratação/dimensionamento assistido e não pertence semanticamente a um plano específico.

A auditoria P1.1 integrou também um gate permanente para impedir regressão de nomenclaturas legadas conhecidas.

## 6. Go-to-Market, crescimento e capital

O domínio GTM integrado governa, como baseline candidata onde indicado:

- lançamento e densidade inicial em Belo Horizonte;
- São Paulo como principal frente comercial de escala nacional;
- Portugal como primeiro mercado internacional condicionado a gates;
- Lisboa como base inicial candidata e Porto como expansão posterior;
- metas de Pessoas, Coletivos, Organizações, Business e Parcerias Estratégicas por horizonte;
- receita e run-rate de planejamento separados de realizado, contrato, faturamento e caixa;
- valuation histórico candidato de R$ 10 milhões a R$ 15 milhões, com âncora interna de R$ 12 milhões pre-money;
- horizontes curto M0–M12, médio M13–M36 e longo M37–M60.

Separação canônica:

```text
Organização
≠ oportunidade
≠ Guivos Business
≠ Parceria Estratégica
```

Parceria Estratégica é relação corporativa da Guivos enquanto empresa com contraparte externa. Relação cujo objeto seja entregar valor diretamente a Pessoas ou Coletivos pertence ao papel de Organização quando aplicável.

Parceria Estratégica não exige receita direta; pode gerar alcance, escala, infraestrutura, tecnologia, integração, apoio, divulgação, acesso territorial, eficiência ou outra capacidade corporativa material.

Metas permanecem `candidate_target` ou `scenario` quando assim classificadas e não são convertidas em compromisso ou realizado pela publicação.

## 7. Arquitetura de grafo e Guivos Intelligence

`ADR-007` estabelece **Neo4j como tecnologia primária de referência para a camada de grafo**.

A leitura obrigatória é:

```text
reference_selected
≠ POC
≠ provisioned
≠ integrated
≠ production
```

Estado factual:

- referência Neo4j: selecionada;
- POC: não comprovada;
- Aura/Server/cluster: não declarado como provisionado;
- dados reais no grafo: não comprovados;
- Graph Data Science: não implementado por esta decisão;
- GraphRAG: não implementado por esta decisão;
- Power BI: não declarado conectado ao grafo;
- produção: não autorizada.

`Grafo Global ≠ Guivos Intelligence ≠ Neo4j`. O produto/camada de inteligência não é substituído pela tecnologia de persistência/consulta de grafo.

## 8. Produtos Especializados e handoffs

A arquitetura vigente reconhece sete Produtos Especializados:

1. Guivos Journey;
2. Guivos Mall;
3. Guivos Travel;
4. Guivos Business;
5. Guivos Media;
6. Guivos Intelligence;
7. Guivos Ads.

Participante não é produto e produto não é participante.

A política vigente preserva:

- Journey como host principal da experiência;
- Intelligence como apoio transversal com proveniência e explicabilidade;
- Business como produto B2B separado de Organização;
- Mall como responsabilidade comercial/transacional própria quando materializada;
- Travel como responsabilidade especializada de viagem quando materializada;
- Media como responsabilidade editorial quando materialmente distinta;
- Ads como responsabilidade publicitária com natureza patrocinada identificável.

`TRN-203` representa publicação por Organização → descoberta Journey, e não Business → Journey.

Journey → Mall e Journey → Travel continuam gaps reais de handoff; nenhum `SURF` ou `TRN` foi inventado para fechá-los.

A PR #203 permanece fonte histórica/intermediária e não autoridade candidata de merge.

## 9. Marca, naming, domínios e ativos digitais

A governança integrada estabelece:

```text
nome canônico
≠ marca registrada
≠ domínio controlado
≠ DNS operacional
≠ serviço em produção
```

Também:

- `Guivos Mall` é o nome canônico do produto;
- `Guivos Marketplace` permanece somente como alias histórico/de migração;
- protocolo ou pedido não equivale a concessão;
- proteção nacional não equivale a proteção global;
- plano de proteção não equivale a execução;
- inventário defensivo, registradores, account IDs, DNS detalhado, contatos de recuperação, credenciais, tokens, chaves e recovery codes não pertencem ao corpus público.

A existência da governança não comprova registro, titularidade, domínio adquirido ou controle técnico específico. Esses estados dependem de evidência própria.

## 10. Validação de mercado

O sistema VAL-001–010 está documentado para a validação B2C inicial.

Autoridades metodológicas incluem:

- VAL-002 2.1.0 com 19 perguntas;
- pré-teste previsto de 10 a 15 participantes;
- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas;
- IFO, compreensão, relevância, contribuição, intenção, interesse e IGV;
- decisões possíveis Go, Go com ajustes, Pivot parcial ou No-Go temporário.

A leitura obrigatória é:

```text
método definido
≠ instrumento pronto
≠ aplicação executada
≠ base válida
≠ métricas calculadas
≠ decisão de mercado
```

`VAL-009` e `VAL-010` exigem evidência E0–E7 antes de promover resultados. Neste estado global, não existe autoridade suficiente para declarar PMF, disposição a pagar, retenção, recorrência, resultado real da pesquisa ou alcance de 200/500 respostas.

## 11. Incentivos, pontos e créditos

`GEM-005-A1` estabelece o guardrail **Propósito Antes do Incentivo**.

A Guivos não deverá construir uma experiência em que a pessoa persiga saldo, pontos, créditos, sequência ou ranking em substituição à própria evolução.

```text
evolução e valor legítimo
> acumulação e engajamento artificial
```

Pontos, créditos ou benefícios futuros somente podem ser considerados quando apoiam finalidade legítima, reduzem barreiras ou reforçam uma ação que continuaria valiosa mesmo sem recompensa.

Nenhum programa real de pontos, conversão, carteira, token, transferência, cashback, saldo ou implementação é autorizado por este guardrail.

## 12. Dívidas e pacotes ainda não promovidos

Permanecem fora de autoridade operacional ou ainda dependentes de consolidação/evidência:

- P5 — arquitetura institucional, jurídica e eventual Fundação Guivos;
- P6 — verdade operacional pública, privacidade, consentimentos e superfícies legais;
- P7 — internacionalização operacional além da estratégia/gates já governados em GTM;
- P9 — consolidação global e nova edição do Public Canon;
- dados reais da validação de mercado;
- proteção registral e controle de ativos específicos sem evidência;
- implementação de grafo;
- cobrança real, gateway, proration, grace period e política fiscal final;
- processos posteriores a `BND-001` ou `BND-002` sob autoridade externa/assistida apropriada.

Não preencher essas lacunas por inferência é parte da governança do GKR.

## 13. Estado documental funcional preservado

| Camada | Estado |
|---|---|
| Arquitetura da Experiência | `active` 0.94.0 |
| Jornadas Integradas | `active` 0.31.0 |
| Jornada da Pessoa | `draft` 0.15.0 |
| Jornada do Coletivo | `draft` 0.15.0 |
| Jornada da Organização | `draft` 0.8.0 |
| catálogo integrado | `active` 0.26.0 |
| galeria visual | `active` 0.21.0 |
| galeria de Planos | `active` 0.3.0 |
| matriz por SVG | `active` 0.17.0 |
| lacunas | `active` 0.26.0 |
| registro de superfícies | `active` 0.17.0 |
| registro de transições | `active` 0.18.0 |
| detalhamento comercial/fronteira | `active` 0.5.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 14. Fila funcional preservada

| Ordem | Continuidade ou família | Estado |
|---:|---|---|
| V1 | compreensão inicial → Tela Hoje | encerrada por UXA-097 |
| V2 | publicação → descoberta/mapa/lista/detalhe | encerrada por UXA-098 |
| V3 | dez estados residuais UXA-055 | encerrada por UXA-099 |
| Planos | identidade e promoção canônica | encerrada por UXA-100-A3 |
| V4 | efeito externo de oportunidades | encerrada por UXA-101 até BND-001 |
| V5 | erros, retornos e interrupções | **pendente; não iniciada** |

## 15. Preservações

- materialização, validação, promoção, contratação e implementação são estados distintos;
- arquitetura de referência não é implantação;
- preço candidato não é disposição a pagar;
- projeção não é realizado;
- valuation interno não é laudo, oferta ou promessa;
- validação até uma fronteira não valida sistema de terceiro;
- relação comercial não compra relevância funcional;
- recompensa não compra evolução, mérito ou autoridade;
- Pessoa, Coletivo e Organização permanecem `draft`;
- UXA-102/V5 não foi iniciada;
- Engenharia de Produto permanece pausada antes de W0-01;
- nenhuma etapa autoriza automaticamente a seguinte.

## 16. Próximo ato governado

O repositório está sincronizado com as validações temáticas identificadas até este checkpoint.

O próximo avanço global deve tratar somente pacotes ainda pendentes com evidência suficiente — especialmente P5, P6, P7 e, após suas decisões aplicáveis, P9/Public Canon — sem reabrir as autoridades recém-integradas salvo nova evidência ou decisão explícita.
