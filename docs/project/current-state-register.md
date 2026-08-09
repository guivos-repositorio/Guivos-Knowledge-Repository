---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.31.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - PAS-001-DOMAIN-MODEL-001
  - GPA-007
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A4
  - UXA-101
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GTM-000
  - GTM-007
  - GTM-008
  - ADR-007
  - GEA-GRAPH-REFERENCE-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-FUNDACAO-GUIVOS-CONCEPT-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
  - GKR-INSTITUTIONAL-LEGAL-EVIDENCE-001
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-LEGAL-SURFACE-GATES-001
  - GKR-OPERATIONAL-LEGAL-TRUTH-001
  - GKR-INTERNATIONAL-OPERATIONS-READINESS-001
  - VAL-009
  - VAL-010
  - GEM-005-A1
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - ROADMAP-12.76.0
  - M7.88
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente do Guivos Knowledge Repository após a consolidação documental P1–P9 de 2026-08-08, a reconciliação controlada da origem voluntária de Planos pela UXA-100-A4 e a formalização do modelo canônico de Domínios de Evolução do Guivos Journey.

A formalização de Domínios de Evolução **não cria novo marco funcional, não inicia UXA-102, não retoma Engenharia de Produto e não converte taxonomia, arquitetura ou exemplos em operação comprovada**. Em caso de divergência, prevalece esta autoridade transversal e, dentro de cada domínio, a autoridade temática específica mais recente.

## 2. Estado global

| Elemento | Estado vigente |
|---|---|
| Era | GE-2 — Knowledge |
| Marco funcional | **M7.88 — saída consciente para fronteira externa validada** |
| Última frente funcional | **UXA-101** |
| Subfrente de reconciliação | **UXA-100-A4 — origem voluntária de Planos** |
| Próxima UXA | **UXA-102/V5 não iniciada** |
| Engenharia de Produto | pausada antes de W0-01 |
| Domínios de Evolução do Journey | **9 domínios canônicos + estado transversal “Ainda estou descobrindo”** |
| Registros granulares | **54 superfícies/estados/fronteiras e 60 transições** |
| Galeria visual | **118 SVGs** |
| Matriz por SVG | **118 associações / 31 perfis** |
| Jornadas principais | Pessoa, Coletivo e Organização permanecem `draft` |
| P1/P1.1 | integrado — semântica e nomenclaturas reconciliadas |
| P2 | integrado como arquitetura de referência — Neo4j `reference_selected` |
| P3 | governança integrada — fatos registrários/digitais dependem de evidência |
| P4 | método/gates integrados — resultado real de mercado não estabelecido |
| P5 | arquitetura institucional integrada — Fundação Guivos continua conceito, não entidade comprovada |
| P6 | arquitetura de privacidade/verdade operacional integrada — controles reais dependem de evidência |
| P7 | governança territorial integrada — Portugal permanece `T1_candidate` |
| P8 | sete Produtos Especializados rebaselineados |
| P9 | consolidação global e Public Canon em edição corrente |

## 3. Cobertura funcional preservada e reconciliada

A formalização dos Domínios de Evolução não altera a baseline visual ou de transições da Arquitetura da Experiência:

- 118 SVGs existentes e referenciados;
- 118 associações individuais;
- 31 perfis de rastreabilidade;
- 118 validações funcionais vigentes de SVG;
- 0 pendentes de validação específica de SVG;
- 42 de 54 IDs granulares com referência visual;
- 10 responsabilidades sem SVG dedicado;
- 2 fronteiras sem tela por definição;
- 54 superfícies/estados/fronteiras;
- 60 transições documentais.

`PER-009 — Conta e configurações da Pessoa` permanece sem SVG. `TRN-406/407` ficam contratadas; `TRN-417/418` e `TRN-427/428` são integralmente validadas no limite documental de navegação administrativa. As transições comerciais internas de Planos preservam suas maturidades anteriores.

A UXA-101 continua encerrando V4 em `BND-001`. Resultado executado por terceiro após essa fronteira não é presumido pela Guivos.

## 4. Participantes, planos, produtos e Domínios de Evolução

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Taxonomia de planos:

- Pessoa: Free · Plus · Pro;
- Coletivo: Livre · Mobiliza · Impacta · Rede;
- Organização: Conecta · Eleva · Transforma;
- Guivos Business: Start · Growth · Scale · Enterprise.

Sete Produtos Especializados:

1. Guivos Journey;
2. Guivos Mall;
3. Guivos Travel;
4. Guivos Business;
5. Guivos Media;
6. Guivos Intelligence;
7. Guivos Ads.

### 4.1 Domínios de Evolução do Guivos Journey

`PAS-001-DOMAIN-MODEL-001` governa o baseline inicial de nove Domínios de Evolução:

1. Saúde e Bem-estar;
2. Trabalho, Carreira e Estudos;
3. Vida Financeira;
4. Empreendedorismo e Projetos;
5. Relacionamentos e Vida Social;
6. Espiritualidade, Propósito e Valores;
7. Viagens, Lazer, Cultura e Novas Experiências;
8. Causas, Voluntariado e Contribuição;
9. Organização e Equilíbrio da Vida.

`Ainda estou descobrindo` é estado transversal legítimo de exploração e **não** constitui décimo domínio. `Outra área` é mecanismo de extensibilidade e preservação da expressão original do participante.

Os domínios possuem interpretação específica para Pessoa, Coletivo e Organização. Uma trajetória pode envolver vários domínios simultaneamente.

Separações canônicas:

```text
Organização ≠ Guivos Business
participante ≠ produto
plano ≠ mérito ou nível de evolução
Parceria Estratégica ≠ Organização
Guivos Mall = nome canônico
Guivos Marketplace = alias histórico/migração
Domínio de Evolução ≠ identidade
Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo
Domínio de Evolução ≠ Objetivo
Domínio de Evolução ≠ score
Domínio de Evolução ≠ diagnóstico
Domínio de Evolução ≠ prova de evolução
```

A UXA-100-A4 corrige no SVG de `ORG-001` o rótulo visual obsoleto `Guivos Business`, sem criar novo ativo. `BND-002` permanece fronteira genérica de contratação/dimensionamento assistido e não pertence semanticamente a um plano específico.

## 5. Go-to-Market e internacionalização

O GTM governa como baseline candidata:

```text
Belo Horizonte
→ São Paulo
→ amplificação nacional seletiva
→ Portugal / Lisboa
→ Portugal / Porto somente após gate
→ novo país europeu somente mediante novo gate
```

Portugal permanece `T1_candidate`.

Não estão comprovados por esta documentação:

- entidade/filial portuguesa;
- equipe local;
- contratos locais;
- IVA/OSS em operação;
- PSP europeu em produção;
- suporte internacional em produção;
- piloto Lisboa executado;
- Porto autorizado;
- segundo país europeu autorizado.

A governança territorial exige distinguir acesso internacional, pesquisa, readiness, piloto autorizado, piloto executado e mercado ativo.

## 6. Grafo, Journey e Intelligence

Neo4j é a tecnologia primária de referência para a camada de grafo.

```text
reference_selected
≠ POC
≠ provisioned
≠ integrated
≠ production
```

Não há autoridade suficiente para afirmar POC, cluster/Aura provisionado, dados pessoais reais no grafo, GDS em produção, GraphRAG implementado ou Power BI conectado.

`Grafo Global ≠ Guivos Intelligence ≠ Neo4j`.

Os Domínios de Evolução agora constituem vocabulário semântico canônico do Journey e podem orientar futura ontologia, classificação explicável e relações no Grafo Global. Isso **não** declara ontologia física, nós, relações, embeddings, pipelines ou dados implementados.

Guivos Intelligence pode produzir candidatos de domínio e relações multidomínio, mas não pode transformar inferência em domínio confirmado sem autoridade suficiente, criar score humano ou utilizar domínio sensível como autorização de publicidade comportamental.

## 7. Marca, naming e ativos digitais

```text
nome canônico
≠ marca registrada
≠ domínio controlado
≠ DNS operacional
≠ serviço em produção
```

O GKR governa naming e estados de evidência, mas não presume titularidade, proteção territorial, domínio adquirido ou controle técnico específico sem prova própria. Segredos, credenciais, recovery codes, chaves, tokens e inventário operacional sensível permanecem fora do corpus público.

## 8. Validação de mercado

VAL-001–010 constituem o sistema metodológico B2C inicial.

Parâmetros governados incluem questionário VAL-002 2.1.0 com 19 perguntas, pré-teste previsto de 10–15 participantes, mínimo de 200 respostas válidas para decisão inicial e meta preferencial de 500.

As áreas utilizadas no instrumento de pesquisa contribuíram para o baseline semântico dos Domínios de Evolução. Essa promoção arquitetural **não transforma a existência da pergunta ou das opções em resultado de pesquisa, preferência de mercado ou evidência de eficácia**.

```text
método definido
≠ instrumento aplicado
≠ base válida
≠ KPI calculado
≠ decisão de mercado
≠ product-market fit
```

Neste checkpoint não existe evidência integrada suficiente para declarar PMF, disposição a pagar, retenção, recorrência ou resultado real da pesquisa.

## 9. Incentivos

`GEM-005-A1` estabelece **Propósito Antes do Incentivo**.

Pontos, créditos, saldo, streak ou ranking não podem substituir evolução, autonomia ou valor legítimo como objetivo da experiência. Nenhum programa operacional de pontos/créditos, carteira, token, cashback ou conversão está autorizado.

O modelo de Domínios de Evolução reforça que contribuição, espiritualidade, saúde, finanças, relacionamentos ou organização não podem ser convertidos em ranking moral, score humano ou competição por “nível de evolução”.

## 10. Arquitetura institucional e Fundação Guivos

`Fundação Guivos` permanece:

```text
conceito institucional social validado
+ nome de trabalho
≠ forma jurídica escolhida
≠ entidade constituída
≠ CNPJ/registro comprovado
≠ operação social própria comprovada
```

F0–F9 governam a eventual progressão do conceito até uma operação institucional evidenciada. A forma jurídica permanece `unresolved`.

## 11. Privacidade, consentimentos e verdade operacional

P6 estabelece:

```text
aceite contratual ≠ consentimento LGPD ≠ preferência voluntária
arquitetura de privacidade ≠ conformidade operacional comprovada
política em draft ≠ política publicada
controle projetado ≠ controle implementado ≠ controle evidenciado
```

Não são presumidos como operacionais: Termos publicados, Aviso/Política de Privacidade vigente, consentimentos, centro de preferências, inventário de cookies/SDKs, Encarregado formalmente indicado, fluxo de direitos, incident response LGPD ou dados pessoais em produção no grafo.

Domínios que envolvam saúde, condição emocional, espiritualidade/religião, finanças, emprego, família, sexualidade, vulnerabilidade ou outras informações sensíveis exigem finalidade, minimização, autoridade e proteção reforçada.

## 12. Public Canon

`GOG-001 — Guia Oficial da Guivos` é a única superfície institucional classificada como `public-canon` neste domínio documental.

O Public Canon traduz autoridades do GKR para linguagem pública e deve distinguir claramente:

- visão e disponibilidade real;
- arquitetura e implementação;
- preço/plano candidato e oferta vigente;
- expansão planejada e mercado ativo;
- conceito institucional e entidade constituída;
- privacidade por design e controles efetivamente publicados/operacionais.

A página pública de Arquitetura do Guivos Journey passa a explicitar os nove Domínios de Evolução e exemplos de como a Guivos pode apoiar jornadas nesses domínios, preservando os guardrails do `PAS-001-DOMAIN-MODEL-001`.

Nenhum texto público pode promover estado superior ao evidenciado nas autoridades internas.

## 13. Programa P0–P9

O programa amplo de ressincronização documental está **consolidado** quanto aos pacotes temáticos previstos:

- P0 — intake/evidência: preservado;
- P1/P1.1 — semântica/nomenclatura: integrado;
- P2 — tecnologia/grafo: integrado como referência;
- P3 — marca/naming/ativos: integrado;
- P4 — validação de mercado: integrado como método/gates;
- P5 — institucional/jurídico: integrado como arquitetura/gates;
- P6 — operação/privacidade/legal: integrado como arquitetura/gates;
- P7 — internacionalização: integrado como programa territorial/gates;
- P8 — Produtos Especializados: integrado;
- P9 — estado global/Public Canon: consolidado por `GKR-P9-GLOBAL-CONSOLIDATION-001`.

**Encerramento documental não significa encerramento das lacunas operacionais.** Itens dependentes de evidência permanecem abertos em seus domínios próprios.

## 14. Fila funcional

| Família | Estado |
|---|---|
| V1 — compreensão inicial → Tela Hoje | encerrada pela UXA-097 |
| V2 — publicação → descoberta/mapa/lista/detalhe | encerrada pela UXA-098 |
| V3 — estados residuais Opportunity Boost | encerrada pela UXA-099 |
| Planos — identidade/promoção canônica | encerrada pela UXA-100-A3 |
| Planos — origem voluntária e retorno | identidade encerrada pela UXA-100-A4; PER-009 ainda sem materialização |
| Journey — Domínios de Evolução | **baseline canônico documentado; sem implementação técnica ou nova UX presumida** |
| V4 — efeito externo de oportunidades | encerrada pela UXA-101 até BND-001 |
| V5 — erros, retornos e interrupções | **pendente; não iniciada** |

## 15. Preservações finais

- M7.88 permanece o marco funcional;
- UXA-101 permanece a última frente funcional numerada;
- UXA-100-A4 é subfrente de reconciliação e não inicia UXA-102;
- UXA-102/V5 não foi iniciada;
- Engenharia de Produto permanece pausada antes de W0-01;
- Pessoa, Coletivo e Organização permanecem jornadas `draft`;
- nove Domínios de Evolução estão governados como vocabulário do Journey;
- “Ainda estou descobrindo” não é décimo domínio;
- classificação de domínio por IA não está declarada como operacional;
- ontologia de grafo física não está declarada como implementada;
- materialização, validação, promoção, contratação, implementação e operação são estados distintos;
- projeção não é realizado;
- preço não é disposição a pagar;
- capital não é receita;
- valuation interno não é laudo/oferta/promessa;
- relação comercial não compra relevância;
- recompensa não compra evolução;
- internacionalização planejada não é mercado ativo;
- nenhuma etapa autoriza automaticamente a seguinte.

## 16. Próximo ato governado

A formalização dos Domínios de Evolução não autoriza automaticamente nova UX, esquema de banco, ontologia física, classificação algorítmica, coleta de dado sensível ou implementação.

Materialização de `PER-009`, maturidade das transições internas de Planos, cobrança real, processo posterior a `BND-002`, UXA-102/V5 e Product Engineering permanecem frentes separadas e exigem autorização própria.
