---
id: GKR-RESYNCHRONIZATION-BASELINE-2026-08-08-001
title: Baseline Governada de Ressincronização do Repositório — 2026-08-08
status: in-progress
version: 0.2.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GKR-UPDATE-PROGRAM-001
  - GKR-STATE-001
  - GKR-VALIDATED-UPDATES-SYNC-2026-08-08-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GTM-000
  - GKR-LEGACY-NOMENCLATURE-RECONCILIATION-001
  - ADR-007
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - VAL-009
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
normative: false
---

# Baseline Governada de Ressincronização do Repositório — 2026-08-08

## 1. Finalidade

Este checkpoint reconcilia o programa P0–P9 com as autoridades efetivamente integradas após o inventário acumulado iniciado em agosto de 2026.

A versão 0.2.0 substitui a leitura intermediária da 0.1.0: os pacotes P1.1, P2, P3, P4 e P8 que antes apareciam como pendentes foram validados e integrados. Os pacotes sem evidência suficiente continuam explicitamente abertos.

A baseline preserva quatro estados que não podem ser confundidos:

1. **integrado na `main`** — autoridade corrente;
2. **validado/referência** — decisão arquitetural ou metodológica sem prova de operação;
3. **dependente de evidência** — não promovível a fato;
4. **pendente de consolidação** — ainda necessita pacote próprio.

## 2. Baseline técnica

- checkpoint anterior de GTM: merge da PR #209 em `9a0de25e664aab65b83c76ca5414c444dad893ae`;
- pacote cumulativo integrado até PR #215: `669cf8eb9ce236003974acf8e6ccd285662dc1da`;
- data: 2026-08-08;
- registro auditável das integrações: `GKR-VALIDATED-UPDATES-SYNC-2026-08-08-001`;
- estado transversal atualizado: `GKR-STATE-001` 2.28.0.

Nenhum SHA acima autoriza, por si só, implementação, operação, contratação, cobrança, investimento, internacionalização ou tratamento jurídico.

## 3. Avanços integrados antes deste ciclo

O repositório já havia incorporado:

- UXA-097 a UXA-101, encerrando V4 até `BND-001`;
- UXA-100 com Planos, comparação, estados de contratação/pagamento e fronteira assistida;
- PR #207 com a autoridade atual de planos e a separação Organização ≠ Guivos Business;
- PR #208 com o domínio GTM, lançamento, expansão, captação, metas, receita, valuation e Parcerias Estratégicas;
- PR #209 com horizontes curto M0–M12, médio M13–M36 e longo M37–M60.

O marco funcional permanece M7.88; V5/UXA-102 não foi iniciada.

## 4. Estado reconciliado do programa P0–P9

| Pacote | Estado após a sincronização | Leitura governada | Próximo ato |
|---|---|---|---|
| P0 — intake/evidência | **reconstruído e preservado** | fontes e inventário de atualização foram organizados | reutilizar quando houver nova evidência |
| P1 — ressincronização semântica | **integrado** | autoridades estruturais e derivados principais foram reconciliados | não reabrir genericamente |
| P1.1 — nomenclaturas legadas | **integrado** | PR #210 corrigiu resíduos e adicionou gate permanente | monitorar regressões pelo CI |
| P2 — tecnologia e grafo | **arquitetura de referência integrada** | Neo4j é referência primária; implantação não comprovada | POC/infra somente por ato futuro |
| P3 — marca, naming, domínios e ativos | **governança integrada** | naming e modelo de evidência existem; registro/titularidade/controle específicos não são presumidos | incorporar fatos apenas com evidência |
| P4 — validação de mercado | **método e gates de evidência integrados** | VAL-001–010 governam a rodada; resultado real continua pendente | intake de uma rodada real quando disponível |
| P5 — institucional/Fundação/jurídico | **não consolidado** | hipóteses não equivalem a estrutura jurídica constituída | inventário e evidência antes de autoridade |
| P6 — verdade operacional/privacidade/legal | **dependente de evidência** | não declarar políticas, consentimentos ou conformidade operacionais sem prova | intake jurídico/operacional específico |
| P7 — internacionalização | **parcialmente governado pelo GTM** | Brasil→Portugal e gates territoriais existem; operação internacional não está autorizada | consolidar somente fatos/decisões adicionais |
| P8 — Produtos Especializados | **rebaseline integrado** | sete produtos e handoffs foram reconciliados contra a autoridade atual | preservar gaps reais sem inventar IDs |
| P9 — consolidação global/Public Canon | **ainda pendente** | deve refletir as autoridades temáticas após fechamento dos pacotes aplicáveis | executar após P5/P6/P7 ou classificação explícita |

## 5. P1.1 — nomenclaturas

A autoridade corrente é:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business: `Start · Growth · Scale · Enterprise`.

Regras:

- Organização ≠ Guivos Business;
- `BND-002` é fronteira genérica de contratação/dimensionamento assistido;
- aliases antigos podem permanecer apenas como histórico/migração claramente identificada;
- o CI possui validação específica para regressões conhecidas.

## 6. P2 — tecnologia e grafo

`ADR-007` e `GEA-GRAPH-REFERENCE-001` posicionam Neo4j como tecnologia primária de referência.

```text
referência escolhida
≠ POC
≠ provisionado
≠ integrado
≠ produção
```

GDS, GraphRAG e Power BI permanecem capacidades/padrões de referência quando aplicáveis, sem afirmação de implementação.

## 7. P8 — Produtos Especializados

Os sete Produtos Especializados são:

1. Journey;
2. Mall;
3. Travel;
4. Business;
5. Media;
6. Intelligence;
7. Ads.

A política de representação e handoffs preserva produto ≠ participante, Organização ≠ Business, proveniência de Intelligence, distinção patrocinado/orgânico de Ads e gaps Journey → Mall / Journey → Travel sem criar `SURF` ou `TRN` inexistentes.

A PR #203 permanece histórica/intermediária e não deve ser integrada como autoridade atual.

## 8. P3 — marca e ativos digitais

A governança integrada separa:

```text
nome canônico
≠ marca registrada
≠ domínio controlado
≠ DNS operacional
≠ serviço em produção
```

`Guivos Mall` é canônico; `Guivos Marketplace` é alias histórico/de migração.

O GKR não publica credenciais, recovery codes, chaves, tokens, account IDs, carteira defensiva completa, detalhes operacionais sensíveis de DNS ou outros segredos.

Nenhuma proteção registral ou titularidade específica é declarada sem evidência.

## 9. P4 — validação de mercado

A metodologia B2C vigente possui VAL-001–010.

Parâmetros já governados incluem:

- VAL-002 2.1.0;
- 19 perguntas;
- pré-teste previsto de 10 a 15 participantes;
- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500;
- IFO, compreensão, relevância, contribuição, intenção, interesse e IGV;
- Go, Go com ajustes, Pivot parcial e No-Go temporário.

A regra central é:

```text
método definido
≠ instrumento aplicado
≠ base válida
≠ métrica calculada
≠ decisão
```

Nenhum resultado real foi promovido sem pacote de evidência E0–E7.

## 10. Guardrail posterior de incentivos

A sincronização também incorpora `GEM-005-A1 — Propósito Antes do Incentivo`.

A decisão impede que pontos, créditos, ranking, streak ou saldo se tornem o objetivo da experiência ou proxy de evolução.

O guardrail não cria programa de recompensas; ele restringe qualquer programa futuro a finalidade legítima, redução de barreira, proporcionalidade, alternativa saudável e segurança comportamental.

## 11. Dívidas transversais preservadas

Ainda dependem de trabalho próprio ou evidência:

- P5 institucional/Fundação/jurídico;
- P6 operação pública, privacidade e superfícies legais;
- P7 fatos de internacionalização além do GTM;
- P9 Public Canon e consolidação global;
- resultado empírico da pesquisa;
- implementação de grafo;
- proteção marcária/digital específica;
- cobrança e infraestrutura real;
- qualquer operação pós-`BND-001` ou pós-`BND-002` não controlada pela autoridade atual.

## 12. Critério de encerramento do programa amplo

A ressincronização ampla somente pode ser declarada totalmente encerrada quando:

- P5/P6/P7 forem consolidados ou formalmente classificados como não aplicáveis/dependentes de evidência;
- P9 reconstruir estado derivado e Public Canon a partir das autoridades finais;
- navegação e índices refletirem as autoridades vigentes;
- gates mecânicos e semânticos passarem sobre o head cumulativo;
- nenhuma lacuna empírica, jurídica, operacional ou tecnológica for promovida silenciosamente a fato.

Portanto, **as validações identificadas neste ciclo estão sincronizadas, mas o programa P0–P9 como um todo permanece em andamento**.
