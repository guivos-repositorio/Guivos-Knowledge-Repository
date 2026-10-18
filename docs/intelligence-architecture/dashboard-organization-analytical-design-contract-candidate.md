---
id: GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-CANDIDATE-001
title: Dashboard Organização — Contrato Candidato de Design Analítico e Rastreabilidade
status: draft
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-10-18
normative: false
maturity: candidate_pre_implementation_design_contract
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-BRAND-TYPOGRAPHY-001
  - GKR-BRAND-COLOR-PALETTE-001
  - UXA-014
  - UXA-019
  - GEM-009-MEASUREMENT-CONTRACT-001
---

# Dashboard Organização — Contrato Candidato de Design Analítico e Rastreabilidade

> **CANDIDATO / NÃO ADJUDICADO.** O ID e o ownership são provisórios, sujeitos ao registry. Este documento não autoriza Design final, protótipo, Replit, backend, dados reais, publicação, produção, RBAC ou exportação.

## 1. Escopo, precedência e invariantes

Este contrato candidato especifica apresentação, navegação analítica interna, rastreabilidade, acessibilidade e tratamento de estados do Dashboard Organização. Prevalecem o master global `GKR-INTELLIGENCE-DASHBOARD-KPI-001`, o Anexo C `GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-001` e, em conflito, a autoridade especializada mais restritiva.

- Organização ≠ Coletivo ≠ Guivos Business; o Dashboard Coletivo será tratado em etapa independente posterior.
- Dashboard Analytics ≠ Home ou Visão Geral autenticada ≠ fonte de verdade operacional.
- Agrupamento de Analytics não cria `GKR-SURF-*` nem `GKR-TRN-*`.
- Relação com Pessoa não autoriza divulgação de Journey individual.
- Atividade ≠ evidência ≠ resultado ≠ impacto; correlação ≠ causalidade.
- Plano pago ≠ legitimidade, relevância ou autoridade.
- Os 39 KPIs permanecem `proposed / NOT_READY`. Design não promove estado nem inventa fonte, fórmula, preço, meta, threshold, entitlement ou permissão.
- `REPLIT BUILD → NOT AUTHORIZED` neste ato.

## 2. Contexto e navegação analítica

Entrada candidata: contexto de Organização autenticada → Analytics → agrupamento visual interno. O owner documental segue o master especializado (`Guivos Intelligence Architecture`); UX/Design permanece autoridade consultada para apresentação, sem transferência automática de ownership ou aprovação de UI. A troca de Organização, unidade ou papel revalida contexto, autoridade e dados, invalida filtros/caches não transportáveis e não exibe dados do contexto anterior.

| Código visual provisório | Agrupamento interno | Família |
|---|---|---|
| ORG-AN-V01 | Visão Executiva | Composição transversal autorizada |
| ORG-AN-V02 | Oportunidades e Programas | OPP |
| ORG-AN-V03 | Participação | PAR |
| ORG-AN-V04 | Relações Institucionais | REL |
| ORG-AN-V05 | Evidências e Resultados | EVD |
| ORG-AN-V06 | Economia | ECO |
| ORG-AN-V07 | Planos e Capacidade | CAP |
| ORG-AN-V08 | Território e Demografia | GEO |
| ORG-AN-V09 | Qualidade dos Dados | DQ |

São agrupamentos de consumo; nove itens não significam obrigatoriamente nove rotas ou novas superfícies canônicas. A Visão Executiva compõe leituras selecionadas, não um score geral.

## 3. Envelope de visualização

Cada visualização deverá identificar: `visual_id`, agrupamento, pergunta, `metric_id` ou contrato de composição, classe autorizada, população, unidade e granularidade, período e fuso, numerador e denominador quando aplicáveis, exclusões, fonte e versão, freshness, natureza e proveniência da evidência, política de acesso/supressão, filtros e drill-down, estados, claims permitidos/proibidos, acessibilidade, responsividade, owner, maturidade e aceite. Campo ainda indefinido deve permanecer pendente.

| Representação | Uso candidato | Condição |
|---|---|---|
| Card | Contagem/taxa válida | Unidade, período e zero legitimamente medido |
| Série temporal | Evolução | Comparabilidade e ruptura de série explícitas |
| Barras | Distribuição por categoria | Denominador e supressão |
| Funil/coortes | Etapas comparáveis | Mesma coorte, eventos e exclusões contratados |
| Tabela | Objetos autorizados | Sem Journey privada individual |
| Mapa | Cobertura/agregado territorial | Geografia legítima e threshold |
| Grafo | Relações institucionais | Bilateralidade, proveniência e ausência de score implícito |

## 4. Rastreabilidade integral dos 39 KPIs do Anexo C

Cada associação abaixo é uma **proposta de visualização**, não aprovação operacional, semântica ou técnica. V01 pode consumir composições desses IDs quando autorizadas.

| KPI | Agrupamento | Nome | Representação candidata | Gate material | Estado |
|---|---|---|---|---|---|
| ORG-KPI-OPP-001 | V02 | Oportunidades válidas | card/série | estado e fonte | proposed / NOT_READY |
| ORG-KPI-OPP-002 | V02 | Oportunidades ativas | card/linha | estado ativo e janela | proposed / NOT_READY |
| ORG-KPI-OPP-003 | V02 | Oportunidades publicadas no período | barra/linha | evento de publicação | proposed / NOT_READY |
| ORG-KPI-OPP-004 | V02 | Oportunidades encerradas | série/tabela | evento de encerramento | proposed / NOT_READY |
| ORG-KPI-OPP-005 | V02 | Programas/iniciativas ativos | card/barras | taxonomia e lifecycle | proposed / NOT_READY |
| ORG-KPI-OPP-006 | V02 | Distribuição por Domínio de Evolução | barras | vínculo JED e denominador | proposed / NOT_READY |
| ORG-KPI-PAR-001 | V03 | Pessoas elegíveis | card/coorte | elegibilidade e disclosure | proposed / NOT_READY |
| ORG-KPI-PAR-002 | V03 | Inscrições/participações válidas | linha/barras | taxonomia de eventos | proposed / NOT_READY |
| ORG-KPI-PAR-003 | V03 | Participantes únicos | card/série | deduplicação e proteção | proposed / NOT_READY |
| ORG-KPI-PAR-004 | V03 | Taxa de participação | taxa/série | numerador e denominador | proposed / NOT_READY |
| ORG-KPI-PAR-005 | V03 | Participação por oportunidade/programa | barras/tabela | escopo e disclosure | proposed / NOT_READY |
| ORG-KPI-PAR-006 | V03 | Cadastros válidos relacionados | card/tabela | semântica de cadastro | proposed / NOT_READY |
| ORG-KPI-REL-001 | V04 | Relações ativas | card/série | UXA-019 e lifecycle | proposed / NOT_READY |
| ORG-KPI-REL-002 | V04 | Relações por contraparte/tipo | barras | taxonomia e disclosure | proposed / NOT_READY |
| ORG-KPI-REL-003 | V04 | Propostas de relação abertas | card/tabela | estado bilateral | proposed / NOT_READY |
| ORG-KPI-REL-004 | V04 | Relações em revisão | card/tabela | estado de revisão | proposed / NOT_READY |
| ORG-KPI-REL-005 | V04 | Relações pausadas/encerradas no período | série | eventos e período | proposed / NOT_READY |
| ORG-KPI-EVD-001 | V05 | Responsabilidades abertas | card/tabela | estado e fonte | proposed / NOT_READY |
| ORG-KPI-EVD-002 | V05 | Responsabilidades vencendo | faixas/tabela | janela de vencimento | proposed / NOT_READY |
| ORG-KPI-EVD-003 | V05 | Compromissos concluídos | card/série | conclusão e evidência | proposed / NOT_READY |
| ORG-KPI-EVD-004 | V05 | Evidências registradas | série/tabela | validade e proveniência | proposed / NOT_READY |
| ORG-KPI-EVD-005 | V05 | Resultados autorizados | série/tabela | claim/evidence | proposed / NOT_READY |
| ORG-KPI-EVD-006 | V05 | Itens sem evidência suficiente | card/barras | suficiência de evidência | proposed / NOT_READY |
| ORG-KPI-ECO-001 | V06 | Transações econômicas autorizadas | card/série | domínio e GEM-009 | proposed / NOT_READY |
| ORG-KPI-ECO-002 | V06 | Valor econômico autorizado | valor/série | reconhecimento GEM-009 | proposed / NOT_READY |
| ORG-KPI-ECO-003 | V06 | Vendas elegíveis | card/barras | semântica de venda | proposed / NOT_READY |
| ORG-KPI-ECO-004 | V06 | Valor de vendas elegíveis | série/barras | ECO-003 e GEM-009 | proposed / NOT_READY |
| ORG-KPI-CAP-001 | V07 | Plano institucional vigente | cartão | fonte e entitlement | proposed / NOT_READY |
| ORG-KPI-CAP-002 | V07 | Uso de capacidade | barra | ciclo e contrato | proposed / NOT_READY |
| ORG-KPI-CAP-003 | V07 | Capacidade disponível | barra/valor | saldo e contrato | proposed / NOT_READY |
| ORG-KPI-CAP-004 | V07 | Eventos de alteração de plano | eventos | lifecycle confirmado | proposed / NOT_READY |
| ORG-KPI-GEO-001 | V08 | Distribuição territorial autorizada | mapa/barras | geografia e supressão | proposed / NOT_READY |
| ORG-KPI-GEO-002 | V08 | Cobertura territorial de oportunidades | mapa/barras | geografia dos objetos | proposed / NOT_READY |
| ORG-KPI-GEO-003 | V08 | Perfil demográfico agregado autorizado | barras | finalidade e thresholds | proposed / NOT_READY |
| ORG-KPI-DQ-001 | V09 | Freshness compliance | percentual | SLA e freshness | proposed / NOT_READY |
| ORG-KPI-DQ-002 | V09 | Indicadores indisponíveis | card/lista | registry de disponibilidade | proposed / NOT_READY |
| ORG-KPI-DQ-003 | V09 | Supressões de disclosure | contagem protegida | política de disclosure | proposed / NOT_READY |
| ORG-KPI-DQ-004 | V09 | Eventos rejeitados | barras/série | validação | proposed / NOT_READY |
| ORG-KPI-DQ-005 | V09 | Completude de proveniência | percentual | proveniência | proposed / NOT_READY |

## 5. Reconciliação das 14 leituras complementares

São marcadores de discussão não canônicos, não novos IDs de produção.

| Referência | Leitura | Destino | Natureza e pendência |
|---|---|---|---|
| ORG-OPP-C01 | Crescimento de oportunidades | V02 | Derivação temporal OPP-001 |
| ORG-OPP-C02 | Continuidade de programas | V02 | Refinamento OPP-005 |
| ORG-PAR-C01 | Manifestação para inscrição | V03 | Composição por coorte; contrato pendente |
| ORG-PAR-C02 | Participação efetiva | V03 | Refinamento PAR-002/004 |
| ORG-PAR-C03 | Conclusão sustentada por evidência | V03/V05 | Composição PAR+EVD |
| ORG-REL-C01 | Relações ativas | V04 | Duplicidade de REL-001: não criar KPI |
| ORG-REL-C02 | Colaboração com entrega | V04/V05 | Composição REL+EVD |
| ORG-EVD-C01 | Cobertura de evidências | V05 | Derivação EVD; denominador pendente |
| ORG-EVD-C02 | Evolução de resultados | V05 | Comparação EVD-005 |
| ORG-CAP-C01 | Utilização de capacidade | V07 | Sobreposição CAP-002: não criar KPI |
| ORG-GEO-C01 | Cobertura territorial | V08 | Refinamento GEO-002 |
| ORG-GEO-C02 | Lacunas de oferta | V02/V08 | Demanda agregada autorizada; risco de inferência |
| ORG-ECO-C01 | Sustentabilidade econômica | V06 | GEM-009 e fontes pendentes |
| ORG-DQ-C01 | Métricas confiáveis | V09 | Composição DQ-001/002/005 |

## 6. Filtros, drill-down e isolamento

Globais candidatos: período, comparação e organização/unidade autorizada. Locais candidatos: objeto, programa, estado, domínio JED aplicável, contraparte, território, plano/ciclo, natureza de evidência e classe de resultado. Todos apenas restringem o access scope.

N0 organização/unidade autorizada → N1 família → N2 objeto/período/segmento autorizado → N3 objeto operacional ou relação autorizada. Pessoa individual não é nível padrão. Composição de filtros e exportação não podem contornar supressão, inclusive reidentificação por diferenças entre recortes. Backend/serving futuro deverá impor a política; esconder informação no cliente não basta.

## 7. Estados obrigatórios

| Estado | Comportamento |
|---|---|
| AVAILABLE | Exibir dado autorizado, unidade, período e proveniência |
| LOADING | Carregamento sem valor fabricado |
| NO_DATA | Sem registros utilizáveis, diferente de zero |
| INSUFFICIENT_DATA | Base insuficiente, sem interpretação indevida |
| SUPPRESSED_BY_POLICY | Valor protegido, sem revelar faixa reidentificável |
| SOURCE_DELAYED | Atraso, com tratamento conforme contrato de freshness |
| NOT_ENTITLED | Entitlement/capacidade contratual indisponível ou insuficiente, quando aplicável; nunca inferir falta de autoridade ou sugerir upgrade para dado protegido |
| ERROR | Mensagem segura e recuperação |

**Negativa de autorização** (papel, finalidade, participante, unidade ou disclosure) é resolvida no serving e/ou na navegação antes da renderização, sem exposição da métrica. Não corresponde a `NOT_ENTITLED` e não cria por inferência um nono estado do catálogo analítico do Anexo C. Exibir mensagem segura de acesso não autorizado somente quando a política permitir revelar a existência da funcionalidade, sem convite comercial, valor, metadado sensível ou detalhes do recorte protegido.

Cada card/série em uma composição preserva estado próprio; a seção não simula completude.

## 8. Identidade visual e acessibilidade

**Obrigatório conforme `GKR-BRAND-COLOR-PALETTE-001 v1.0.0` (active/normative):** canvas/base de **todas** as páginas e viewports em `White #FFFFFF`; cores de UI (texto, ícones, botões, bordas, estados, séries de gráficos, mapas e nós/arestas de grafos) exclusivamente entre os **30 tokens hexadecimais oficiais**. Não gerar tonalidades derivadas, gradientes intermediários fora dos tokens, variantes automáticas de bibliotecas ou `rgba`/`hsla` que criem novas cores. Gray 3 `#E3E3E3`, Gray 2 `#F3F3F3` e Purple 4 `#5D34A9` são aplicações candidatas **dentro** da paleta obrigatória; apenas o mapeamento semântico, a composição e o layout estão sujeitos a Design. Fotografias/vídeos reais mantêm cores naturais segundo a exceção normativa. Todos os contrastes, estados de foco, legendas e visualizações exigem testes de acessibilidade e sinalização que não dependa apenas da cor.

Desktop permite comparações lado a lado; tablet reduz colunas; mobile prioriza leitura vertical e alternativa acessível às tabelas/gráficos. As experiências exigem navegação por teclado, foco visível, contraste, textos e explicações acessíveis sem depender exclusivamente de tooltip. Fixtures devem exibir **DADOS FICTÍCIOS / DEMONSTRAÇÃO**.

## 8.1. Autoridade tipográfica e navegação

A tipografia oficial é **Goldplay**, conforme `GKR-BRAND-TYPOGRAPHY-001 v1.0.2` (normative/current). Aplicar escala e regras da autoridade vigente; este documento não cria tokens tipográficos. As **restrições cromáticas oficiais já são vinculantes** por `GKR-BRAND-COLOR-PALETTE-001 v1.0.0`; somente aplicação semântica de tokens, hierarquia e layout permanecem decisões de Design.

O modelo `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2` governa a navegação autenticada. Analytics é tratado aqui como entrada/capacidade candidata especializada, não como reclassificação automática de L2, GKR-SURF ou GKR-TRN. Qualquer vínculo efetivo ao menu existente depende de adjudicação da autoridade de navegação, preservando recontextualização de Organização/unidade/papel.

## 8.2. Proteção reforçada para análises e interação

- Segmentação agregada não implica divulgação segura; exigir thresholds de proteção e avaliação de inferência por diferença entre filtros, séries e exportações.
- Mapas territoriais e grafos institucionais devem oferecer alternativas textuais/tabelares acessíveis e não expor entidades/arestas sem autoridade aplicável.
- Funis não podem misturar coortes, cadastros, manifestações, inscrições e participações sem definições de eventos e deduplicação.
- O estado `SUPPRESSED_BY_POLICY` não pode revelar magnitude, faixa ou atributo sensível por tooltip ou rótulo.
- Mensagens de `SOURCE_DELAYED`, `NO_DATA` e `INSUFFICIENT_DATA` permanecem distintas de zero real.

## 9. Limites de engenharia

Cadeia conceitual: fonte autorizada → agregação/Graph/Intelligence conforme domínio → contrato KPI → serving com políticas → dashboard → usuário autorizado. Este contrato não define tecnologias físicas, endpoints, schemas, ingestão, API ou RBAC. Adaptadores de mock e real devem permanecer separados se autorizados futuramente. Dados reais, backend, exportações e Replit permanecem não autorizados por este contrato.

## 10. Gates herdados, sem promoção

| Gate | Estado | Evidência pendente |
|---|---|---|
| G-ORG-01 | UNRESOLVED | Consumidor × KPI × finalidade × disclosure |
| G-ORG-02 | UNRESOLVED | Estados/eventos/coortes/janelas/deduplicação/denominadores |
| G-ORG-03 | SOURCE_PENDING | Fonte, proveniência, freshness e qualidade |
| G-ORG-04 | UNRESOLVED | Bilateralidade UXA-019 e exposição de relações |
| G-ORG-05 | BLOCKED | GEM-009, economia, plano e entitlements |
| G-ORG-06 | UNRESOLVED | Reconciliação e contratos dos 39 KPIs |
| G-ORG-07 | NOT_AUTHORIZED | Serving, RBAC, Design final e build |

### Checklist de revisão antes de merge

- [ ] Adjudicar ID provisório e ownership perante registry e autoridade de Intelligence/UX; até lá permanecem candidatos.
- [ ] Validar os nove agrupamentos perante IA/navegação autenticada/Surface Registry.
- [ ] Auditar os 39 vínculos KPI → visualização e os 14 refinamentos.
- [ ] Validar disclosure, filtros, mapas, coortes e grafos.
- [ ] Validar uso exclusivo dos 30 tokens da paleta normativa, fundo-base branco e focus states acessíveis; escala Goldplay conforme GKR-BRAND-TYPOGRAPHY-001.
- [ ] Corrigir separadamente divergência histórica Anexo C: cabeçalho v0.1.2 × seção 24 v0.1.1.
- [ ] Revisar autoridades de UX, inclusive documentos que ainda constam draft.
- [ ] Validar semantic/mechanical gates e revisão humana antes de eventual merge.
- [ ] Não converter merge documental em autorização automática de implementação.

## 11. Estado final

```text
DOCUMENT STATUS → DRAFT / NOT ADJUDICATED
INTERNAL VISUAL GROUPS → 9 (NOT GKR-SURF)
EXISTING KPI IDS → 39 / ALL proposed / NOT_READY
EXTRA ANALYTICAL CANDIDATES → 14 / NON-CANONICAL
DATA STATES → 8 PRESERVED
G-ORG-01..07 → UNCHANGED
REAL DATA / API / RBAC / EXPORT / REPLIT BUILD → NOT AUTHORIZED
ORGANIZATION FIRST → COLLECTIVE DEFERRED
```

Fontes: `docs/intelligence-architecture/dashboards-kpis-analytics-master-specification.md`, `docs/intelligence-architecture/dashboard-organization-master-specification.md`, `docs/experience-architecture/organizations-collectives-authenticated-navigation-materialization.md`, `docs/experience-architecture/organizations-collectives-authenticated-actors-authorities-and-jobs.md`, `docs/experience-architecture/organizations-collectives-journey/ux-ui-orchestration-master.md` (draft consultado) e `docs/economic-model/gem-009-measurement-contract.md` (draft consultado).

---

## 12. Registro candidato de adjudicação documental — 18/10/2026

> **PARECER TÉCNICO PARA DECISÃO HUMANA, NÃO ADJUDICAÇÃO.** Esta seção registra proposta, evidências e consequências sem alterar IDs, owners, maturidades, acesso ou autorização técnica.

| Questão | Proposta para adjudicação | Autoridade a validar | Situação |
|---|---|---|---|
| Identidade documental | Manter `GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-CANDIDATE-001` somente como ID provisório até checagem formal de namespace/registry | Governança documental GKR / Intelligence | PROPOSED |
| Responsabilidade pelo contrato | Herdar `Guivos Intelligence Architecture` do Anexo C como owner documental; UX/Design é autoridade de apresentação a consultar, sem substituir o owner | Anexo C + GKR-UX-ORGCOL-AUTH-NAV-MAT-001 | ALIGNED TO EXISTING MASTER / APPROVAL PENDING |
| Vínculo de Analytics | A autoridade de navegação (§16.2) enquadra Intelligence como apoio contextual, não eixo principal. A entrada visual Analytics observada no protótipo não é promovida por este documento a nó canônico. Nove agrupamentos internos continuam candidatos | `GKR-UX-ORGCOL-AUTH-NAV-MAT-001` §16.2 + Anexo C | BOUNDARY VERIFIED / UI ENTRY PENDING |
| Vinculação do Design System | Consumir `GKR-BRAND-TYPOGRAPHY-001 v1.0.2` (Goldplay) e paleta/tokens oficiais vigentes, sem congelar decisões de layout | Autoridade de marca e Design System | REFERENCED / REVIEW_PENDING |
| Catálogo analítico | Preservar 39 IDs sem mudança de status e 14 refinamentos não canônicos | Master global + Anexo C + owners de domínio | DOCUMENTARILY RECONCILED / NOT APPROVED |
| Privacidade e acesso | Exigir população, finalidade, autoridade, thresholds e serving antes de qualquer dado real | G-ORG-01/03/04/07 | BLOCKED FOR REAL DATA |
| Economia e capacidade | Nenhuma venda, receita ou entitlement presumido | `GEM-009-MEASUREMENT-CONTRACT-001` + contratos especializados | BLOCKED |
| Prontidão para implementação | Nenhum gate liberado por esta PR | G-ORG-01..07 | NOT_AUTHORIZED |

### Evidências e riscos restantes

1. Conferência de completude por ID: os 39 `ORG-KPI-*` do Anexo C estão representados, sem IDs novos nesta matriz. Isso não valida fórmula, rótulo de interface ou permissão de cada métrica.
2. Os nove agrupamentos não são `GKR-SURF-*` e não devem se tornar rotas obrigatórias por inferência.
3. Para navegação, validar o comportamento real do item Analytics no protótipo operacional em ato específico; este documento não afirma que esteja implementado.
4. Validar tokens visuais e critérios de acessibilidade com responsáveis pelo Design System.
5. Preservar `status: draft` e `normative: false` até revisão humana, verificações automatizadas finais e eventual promoção separada.
6. A divergência textual de versão do Anexo C (`v0.1.2` no frontmatter versus `v0.1.1` na seção 24) não é corrigida neste documento nem serve como bloqueio oculto de outras frentes; necessita ato próprio.

### Decisão ainda requerida

```text
CANDIDATE REVIEW → DOCUMENTED
HUMAN ADJUDICATION → PENDING
IDENTITY FINAL → PENDING; OWNER DOCUMENTAL → ALIGNED TO ANNEX C / REVIEW PENDING
ANALYTICS NAVIGATION BOUNDARY → VERIFIED; UI ENTRY / LINK → PENDING
KPI READINESS → 39 proposed / NOT_READY
G-ORG-01..07 → UNCHANGED
PR #704 → DRAFT / NO MERGE AUTHORIZED BY THIS SECTION
REPLIT / REAL DATA / PRODUCT ENGINEERING → NOT AUTHORIZED
```
