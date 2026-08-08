---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 3.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-STATE-001
related:
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - GOG-001
  - UXA-101
  - ADR-007
  - GTM-007
  - GTM-008
  - GEM-005-A1
  - GKR-FUNDACAO-GUIVOS-CONCEPT-001
  - GKR-DATA-PRIVACY-CONSENT-001
  - M7.88
normative: false
---

# Matriz de Consolidação Canônica

## 1. Finalidade

Esta matriz oferece uma leitura transversal compacta das autoridades correntes. Ela não substitui `GKR-STATE-001` nem a autoridade temática específica.

A edição 3.0.0 substitui a leitura agregada anterior, que refletia o estado funcional de julho. Addenda e changelogs anteriores permanecem evidência histórica.

## 2. Regras de decisão

| Estado | Significado |
|---|---|
| consolidado | autoridade integrada e vigente |
| referência | arquitetura/tecnologia escolhida sem prova de implantação |
| candidato | direção ou meta ainda dependente de gate/evidência |
| dependente de evidência | não pode ser promovido a fato |
| histórico | preservado para rastreabilidade, não autoridade corrente |
| pausado | válido, mas sem execução autorizada |

## 3. Fundação, propósito e participantes

| Elemento | Estado | Autoridade/limite |
|---|---|---|
| Essência, propósito, missão e princípios | consolidado | GEA/GEB Foundation |
| Participantes | consolidado | Pessoa · Coletivo · Organização |
| Organização ≠ Guivos Business | consolidado | taxonomia/GPA |
| Jornada como evolução contextual | consolidado | GEF/PAS/UXA |
| autonomia do participante | consolidado | arquitetura da experiência |
| evolução ≠ engajamento ≠ pontos | consolidado | GEM-005-A1 |

## 4. Produtos e planos

| Elemento | Estado | Leitura corrente |
|---|---|---|
| Guivos Journey | consolidado | host principal da experiência |
| Guivos Mall | consolidado | nome canônico; Marketplace é alias histórico |
| Guivos Travel | consolidado | Produto Especializado |
| Guivos Business | consolidado | Produto B2B separado de Organização |
| Guivos Media | consolidado | responsabilidade editorial especializada |
| Guivos Intelligence | consolidado | inteligência transversal; não é Neo4j |
| Guivos Ads | consolidado | publicidade/patrocínio identificável |
| Pessoa | consolidado | Free · Plus · Pro |
| Coletivo | consolidado | Livre · Mobiliza · Impacta · Rede |
| Organização | consolidado | Conecta · Eleva · Transforma |
| Business | consolidado | Start · Growth · Scale · Enterprise |
| preços e entitlements | parcialmente candidatos | autoridade econômica específica; preço ≠ WTP |

## 5. Experiência e materialização

| Elemento | Estado |
|---|---|
| marco funcional | **M7.88** |
| última UXA | **UXA-101** |
| UXA-102/V5 | não iniciada |
| SVGs | 118 |
| associações | 118 |
| perfis | 31 |
| superfícies/estados/fronteiras | 53 |
| transições | 54 |
| Pessoa/Coletivo/Organização | jornadas `draft` |
| Engenharia de Produto | pausada antes de W0-01 |

V1–V4 estão encerradas nos limites documentais definidos. `BND-001` continua fronteira de autoridade externa; `BND-002` continua fronteira genérica de contratação/dimensionamento assistido.

## 6. Handoffs e gaps preservados

- `TRN-203` = Organização publica → descoberta Journey; não prova Business;
- Journey → Mall: handoff dedicado ainda é gap;
- Journey → Travel: handoff dedicado ainda é gap;
- Media: contexto editorial próprio ainda requer maturação quando materializado;
- Intelligence: proveniência/explicabilidade devem acompanhar derivados;
- Ads/Opportunity Boost: transições patrocinadas parciais permanecem parciais;
- processo posterior a `BND-001` não pertence à autoridade da Guivos;
- processo posterior a `BND-002` depende da autoridade contratual/assistida aplicável.

## 7. Tecnologia e dados

| Elemento | Estado |
|---|---|
| Neo4j | `reference_selected` |
| POC Neo4j | não comprovado |
| infraestrutura Neo4j | não comprovada |
| GraphRAG | referência, não implementação |
| GDS | referência, não produção |
| Power BI conectado ao grafo | não comprovado |
| dados pessoais no grafo | não comprovados |

`Grafo Global ≠ Guivos Intelligence ≠ Neo4j`.

## 8. Marca e ativos digitais

```text
nome canônico
≠ registro de marca
≠ domínio controlado
≠ DNS operacional
≠ serviço ativo
```

Governança e modelo de evidência estão consolidados. Titularidade, registro, proteção territorial e controle técnico específico dependem de evidência própria.

## 9. Mercado e GTM

| Elemento | Estado |
|---|---|
| metodologia B2C VAL-001–010 | consolidada |
| aplicação/resultados reais | dependentes de evidência |
| PMF | não estabelecido |
| disposição a pagar real | não estabelecida |
| BH → SP → Portugal | baseline territorial candidata integrada |
| Portugal | `T1_candidate` |
| Lisboa | base inicial candidata |
| Porto | posterior, condicionado |
| segundo país europeu | não autorizado |
| metas M6–M60 | `candidate_target`/scenario conforme autoridade |
| valuation R$10–15 mi / âncora R$12 mi | referência de planejamento, não fato transacional |

## 10. Institucional e jurídico

`Fundação Guivos` é conceito institucional social validado e nome de trabalho. Forma jurídica, entidade constituída, CNPJ, governança formal e operação própria não estão comprovados.

F0–F9 governam eventual formação. Produto, participante, empresa e veículo social permanecem objetos distintos.

## 11. Privacidade e verdade operacional

```text
aceite contratual ≠ consentimento LGPD ≠ preferência
arquitetura ≠ implementação ≠ operação evidenciada
```

P6 governa atividades de tratamento, bases jurídicas, consentimentos, superfícies legais LS0–LS8 e verdade operacional OT0–OT8. Não presume Termos, Política/Aviso de Privacidade, cookies/SDKs, Encarregado, fluxo de direitos ou incident response em produção.

## 12. Internacionalização

P7 governa T0–T9 e PT0–PT9.

Acesso de usuário, domínio territorial, marca protegida, pesquisa ou prospecção não tornam um território mercado ativo. Piloto autorizado não equivale a piloto executado; piloto executado não equivale a escala aprovada.

## 13. Public Canon

`GOG-001 — Guia Oficial da Guivos` é a tradução pública das autoridades atuais.

O Public Canon não pode afirmar como disponível, registrado, implementado ou operacional aquilo que o GKR classifica como candidato, referência ou dependente de evidência.

## 14. Programa de ressincronização P0–P9

O programa documental está consolidado após P9. Isso significa que as frentes temáticas previstas foram reconciliadas com a autoridade atual; **não significa que os objetos de negócio, tecnologia, mercado, jurídico ou operação estejam executados**.

Novas evidências deverão atualizar o domínio correspondente por novo ato governado.
