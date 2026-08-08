---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.29.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - GPA-007
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
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

Este registro declara o estado global vigente do Guivos Knowledge Repository após a consolidação documental P1–P9 de 2026-08-08.

A consolidação documental **não cria novo marco funcional, não inicia implementação e não converte arquitetura, plano ou método em operação comprovada**. Em caso de divergência, prevalece esta autoridade transversal e, dentro de cada domínio, a autoridade temática específica mais recente.

## 2. Estado global

| Elemento | Estado vigente |
|---|---|
| Era | GE-2 — Knowledge |
| Marco funcional | **M7.88 — saída consciente para fronteira externa validada** |
| Última frente funcional | **UXA-101** |
| Próxima UXA | **UXA-102/V5 não iniciada** |
| Engenharia de Produto | pausada antes de W0-01 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** |
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

## 3. Cobertura funcional preservada

A consolidação P1–P9 não altera as contagens funcionais:

- 118 SVGs existentes e referenciados;
- 118 associações individuais;
- 31 perfis de rastreabilidade;
- 118 validações funcionais vigentes de SVG;
- 0 pendentes de validação específica de SVG;
- 42 de 53 IDs granulares com referência visual;
- 9 responsabilidades sem SVG dedicado;
- 2 fronteiras sem tela por definição;
- 53 superfícies/estados/fronteiras;
- 54 transições documentais.

A UXA-101 continua encerrando V4 em `BND-001`. Resultado executado por terceiro após essa fronteira não é presumido pela Guivos.

## 4. Participantes, planos e produtos

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

Separações canônicas:

```text
Organização ≠ Guivos Business
participante ≠ produto
plano ≠ mérito ou nível de evolução
Parceria Estratégica ≠ Organização
Guivos Mall = nome canônico
Guivos Marketplace = alias histórico/migração
```

`BND-002` permanece fronteira genérica de contratação/dimensionamento assistido e não pertence semanticamente a um plano específico.

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

## 6. Grafo e Intelligence

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

## 12. Public Canon

`GOG-001 — Guia Oficial da Guivos` é a única superfície institucional classificada como `public-canon` neste domínio documental.

O Public Canon traduz autoridades do GKR para linguagem pública e deve distinguir claramente:

- visão e disponibilidade real;
- arquitetura e implementação;
- preço/plano candidato e oferta vigente;
- expansão planejada e mercado ativo;
- conceito institucional e entidade constituída;
- privacidade por design e controles efetivamente publicados/operacionais.

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
| V4 — efeito externo de oportunidades | encerrada pela UXA-101 até BND-001 |
| V5 — erros, retornos e interrupções | **pendente; não iniciada** |

## 15. Preservações finais

- M7.88 permanece o marco funcional;
- UXA-101 permanece a última frente funcional;
- UXA-102/V5 não foi iniciada;
- Engenharia de Produto permanece pausada antes de W0-01;
- Pessoa, Coletivo e Organização permanecem jornadas `draft`;
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

Após a consolidação P9, novas frentes devem partir de necessidade, evidência ou autorização própria. O P9 não inicia UXA-102, Product Engineering, operação internacional, implantação tecnológica, programa social, pesquisa real, cobrança ou qualquer outro ato operacional.
