---
id: GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-HANDOFF-CANDIDATE-001
title: Dashboard Organização — Handoff de Design Candidato
status: draft
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-10-18
normative: false
maturity: design_handoff_pre_implementation_candidate
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-CANDIDATE-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-BRAND-COLOR-PALETTE-001
  - GKR-BRAND-TYPOGRAPHY-001
---

# Guivos — Dashboard Organização: Handoff de Design Candidato v0.1.0

> Documento de trabalho para revisão no GKR. **Não constitui liberação de Design final, Replit, implementação, dados reais, API, RBAC, exportação ou produção.** Todos os 39 `ORG-KPI-*` permanecem `proposed / NOT_READY`, os 14 refinamentos são não canônicos e `G-ORG-01..07` permanecem inalterados.

## 1. Objetivo e fronteira

Definir uma representação demonstrativa coerente, legível e responsiva das leituras analíticas institucionais, sem criar `GKR-SURF-*`, `GKR-TRN-*`, novas fontes de verdade ou um dashboard de controle de Pessoas.

A **Visão Geral autenticada** sintetiza o momento e os próximos passos da Organização. **Analytics** é uma capacidade especializada e contextual para consulta analítica, sem posição principal automática na navegação. Dashboard Coletivo e Guivos Business Dashboard estão fora deste escopo.

## 2. Experiência global — anatomia candidata

### Estrutura desktop

1. Cabeçalho de contexto: Organização, unidade e papel ativos. A recontextualização exige revalidação de autoridade e invalidação de valores e filtros não portáveis.
2. Navegação operacional autenticada: preservada conforme sua própria autoridade. A entrada Analytics exige validação especializada, sem ser inferida do handoff.
3. Cabeçalho de Analytics: título, propósito e metadados de atualização/proveniência apenas quando contratados.
4. Navegação analítica interna: nove agrupamentos candidatos, podendo usar abas ou navegação contextual. Não implica nove rotas ou nove novas superfícies.
5. Filtros globais: período, comparação e escopo aplicável somente quando autorizados; filtros por família restringem o recorte.
6. Conteúdo: cartões, séries, tabelas e continuidade contextual legítima, sem absorver a fonte operacional de verdade.
7. Notas interpretativas: natureza da leitura, limitações, supressão, atraso ou ausência de informação.

### Hierarquia editorial

- **O que existe:** contexto, título, período e população.
- **O que mudou:** comparação somente com bases equivalentes.
- **O que requer atenção:** limitações, atrasos ou dados insuficientes, sem decisões automatizadas.
- **Como investigar:** detalhamento apenas até objeto e escopo autorizados.

Não criar escore universal de eficiência, reputação, impacto, valor social ou qualidade de Pessoas. A anatomia é orientação, não wireframe fixo.

## 3. Nove agrupamentos internos candidatos

| Código | Seção | Objetivo | Elementos candidatos | Dependência e limitação |
|---|---|---|---|---|
| V01 | Visão Executiva | Síntese da própria Organização | cards autorizados, tendências comparáveis e disponibilidade | Composição de métricas existentes; sem escore institucional agregado |
| V02 | Oportunidades e Programas | Volume, estados e distribuição | cards, séries, barras e tabela de oportunidades | `ORG-KPI-OPP-001..006`; eventos e lifecycle pendentes |
| V03 | Participação | Inscrições e participação agregada | séries, barras, funil condicionado a coorte aprovada | `ORG-KPI-PAR-001..006`; proteção da Journey individual |
| V04 | Relações Institucionais | Relações legítimas no próprio escopo | cards por estado, distribuição e grafo condicionado | `ORG-KPI-REL-001..005`; autoridade bilateral UXA-019 |
| V05 | Evidências e Resultados | Responsabilidades e evidências | cronologia, faixas, cards, tabela | `ORG-KPI-EVD-001..006`; atividade ≠ resultado ≠ impacto |
| V06 | Economia | Contratos econômicos eventualmente autorizados | estados seguros; reserva de espaço sem valor econômico inventado | `ORG-KPI-ECO-001..004`; GEM-009 / G-ORG-05 bloqueados |
| V07 | Planos e Capacidade | Plano e consumo da capacidade própria | cards, barras e histórico condicionado | `ORG-KPI-CAP-001..004`; Conecta/Eleva/Transforma; plano não concede autoridade |
| V08 | Território e Demografia | Cobertura territorial agregada permitida | barras, mapas e tabela acessível | `ORG-KPI-GEO-001..003`; supressão e inferência diferencial |
| V09 | Qualidade dos Dados | Clareza de disponibilidade, proveniência e freshness | cartões, matriz e mensagens de qualidade | `ORG-KPI-DQ-001..005`; sem exposição de metadados protegidos |

As 14 leituras complementares permanecem candidatas, não canônicas, conforme o contrato integrado pela PR #704. Duplicidades `ORG-REL-C01` versus `REL-001` e `ORG-CAP-C01` versus `CAP-002` não geram KPIs novos.

## 4. Componentes e interações

| Componente | Regras mínimas | Alternativa acessível | Condição |
|---|---|---|---|
| Card KPI | título, unidade, população, período, estado e proveniência quando permitida | texto integral e rótulos | somente dado autorizado; demo marcada |
| Série temporal | temporalidade comparável e interrupções explícitas | tabela e descrição | contrato de evento e freshness |
| Barras | categorias e unidades homogêneas; ordenação interpretável | lista/tabela de valores | dimensão e disclosure autorizados |
| Funil/coorte | mesma coorte, estados, eventos e denominadores | tabela de etapas | G-ORG-02 pendente |
| Mapa | escala, legenda, supressão e geografia legítima | tabela territorial | não inferir localização ou desejo individual |
| Grafo | nó e aresta definidos, bilateralidade e fonte | tabela de vínculos | exposição autorizada |
| Tabela | cabeçalhos semânticos, ordenação, contexto | teclado e leitor de tela | sem drill-down pessoal implícito |
| Filtro | rótulo, escopo e estado explícito | foco/teclado | nunca expandir acesso |
| Estado vazio | distinguir zero, ausência, insuficiência, supressão e atraso | mensagem textual | sem número fabricado |

Não prometer exportação, compartilhamento externo, ação institucional automatizada, API ou monitoramento em tempo real.

## 5. Oito estados obrigatórios e acesso

| Estado | Comportamento | Proibição |
|---|---|---|
| `AVAILABLE` | apresentar dado válido, escopo, período e natureza | valor sem contrato |
| `LOADING` | placeholder neutro sem valor anterior de outro contexto | vazamento de cache |
| `NO_DATA` | informar inexistência de observações utilizáveis | converter automaticamente em zero |
| `INSUFFICIENT_DATA` | informar falta de suficiência | estimar sem autoridade |
| `SUPPRESSED_BY_POLICY` | mensagem segura sem magnitude ou faixa inferível | tooltip/exportação indireta |
| `SOURCE_DELAYED` | indicar atraso de fonte conforme freshness | apresentar como atual |
| `NOT_ENTITLED` | indisponibilidade de entitlement/capacidade contratual, se visibilidade legítima | confundir falta de autorização com plano ou sugerir upgrade para dado protegido |
| `ERROR` | mensagem segura de falha | expor informação interna |

**Negativa de autorização** por papel, finalidade, participante, unidade ou sensibilidade ocorre no serving e/ou na navegação **antes** da renderização. Não equivale a `NOT_ENTITLED` e não cria automaticamente um nono estado canônico. Mensagens não devem revelar a existência de objetos protegidos.

## 6. Identidade visual vinculante

Segundo `GKR-BRAND-COLOR-PALETTE-001 v1.0.0` (**normative**):

- Fundo-base de **toda página e viewport** obrigatório `White #FFFFFF`.
- Qualquer cor de UI, texto, ícone, borda, foco, série, mapa ou grafo deve ser **exclusivamente um dos 30 tokens oficiais**. Proibidas cores derivadas, gradientes intermediários e cores automáticas fora da paleta.
- Tokens úteis: Purple 4 `#5D34A9`, Purple 2 `#EDE9FE`, Gray 3 `#E3E3E3`, Gray 2 `#F3F3F3`, Black 1 `#292929`, White `#FFFFFF`. Escolhas devem preservar contraste, foco e leitura.
- Fotografias e vídeos reais mantêm cores naturais segundo exceção própria; ilustrações de UI obedecem à paleta.
- Não distinguir séries ou estados apenas por cor; usar forma, padrão, texto e legenda.

**Tipografia:** Goldplay conforme `GKR-BRAND-TYPOGRAPHY-001 v1.0.2`: Display 60/60 SemiBold; H1 48/60 SemiBold; H2 40/44 SemiBold; H3 32/40 SemiBold; H4 24/30 Medium; Body 20/30 Regular; Body Small 16/25 Regular; Caption 12/18 Regular; Micro 10/15 Medium. Design escolhe hierarquia; não inventar token `Body Medium`. Não distribuir fontes neste handoff.

## 7. Responsividade

- **Desktop:** grade editorial com comparações lado a lado quando significativas, até quatro colunas de cards conforme largura útil; filtros visíveis ou acessíveis.
- **Tablet:** reduzir colunas, preservar legendas, manter filtro expansível e estado explícito.
- **Mobile:** sequência vertical, sem overflow global, acesso a alternativas tabulares, controles utilizáveis e retenção apenas do contexto permitido.
- **Redução de movimento:** transições opcionais devem respeitar preferência de acessibilidade; não simular real-time.

Breakpoints, dimensões, copy final e geometria não são adjudicados neste handoff.

## 8. Fixtures e cenários demonstrativos

Exclusivamente dados artificiais com aviso **DADOS FICTÍCIOS — NÃO REPRESENTAM OPERAÇÃO REAL**. Não usar nomes de Pessoas, parceiros reais, Journey pessoal ou histórico privado. Exemplos não são baseline, meta, evidência institucional nem autorização de fonte.

Cenários mínimos de futura validação:
1. Organização fictícia com algumas leituras `AVAILABLE`.
2. Contexto `NO_DATA` ou `INSUFFICIENT_DATA`.
3. Contexto com `SUPPRESSED_BY_POLICY`, `SOURCE_DELAYED` ou `NOT_ENTITLED`.
4. Troca de Organização/unidade/papel sem transporte indevido de permissões, filtros ou valores.

## 9. Casos de revisão UX

1. Entrar em Analytics sem substituir `ORG-001`.
2. Alternar agrupamentos sem criar novas superfícies canônicas.
3. Revalidar acesso após troca de Organização/unidade/papel, sem reutilizar dados.
4. Comparar somente períodos e populações equivalentes.
5. Exibir lado a lado métricas disponíveis e indisponíveis sem falsa completude.
6. Separar `NOT_ENTITLED` comercial de acesso negado.
7. Suprimir filtro territorial que permitiria reidentificação.
8. Indicar atraso de fonte sem confundi-lo com zero ou loading.
9. Usar apenas teclado e leitor de tela, com foco/contraste e descrição de gráficos.
10. Preservar interpretação e escopo em desktop, tablet e mobile.

## 10. Critérios de aceite documental

- [ ] Precedência dos masters e contrato da PR #704 verificada.
- [ ] Nove agrupamentos sem novos `GKR-SURF-*` ou `GKR-TRN-*`.
- [ ] 39 KPIs `proposed / NOT_READY` e 14 refinamentos não canônicos.
- [ ] Demonstração não apresenta dados fictícios como evidência real.
- [ ] Oito estados e tratamento de negativa de autorização distinta de `NOT_ENTITLED`.
- [ ] `#FFFFFF` no canvas e somente 30 tokens cromáticos oficiais na UI.
- [ ] Goldplay e escala tipográfica oficial, sem novos tokens.
- [ ] Disclosure, geografia, coortes, relações e grafos sujeitos aos contratos.
- [ ] Responsividade e acessibilidade verificáveis.
- [ ] Responsáveis de Intelligence e UX/Design revisam o candidato.
- [ ] Prototipação/Replit depende de autorização separada.

## 11. Gates preservados e pendências

| Gate | Estado |
|---|---|
| G-ORG-01 | UNRESOLVED |
| G-ORG-02 | UNRESOLVED |
| G-ORG-03 | SOURCE_PENDING |
| G-ORG-04 | UNRESOLVED |
| G-ORG-05 | BLOCKED |
| G-ORG-06 | UNRESOLVED |
| G-ORG-07 | NOT_AUTHORIZED |

O identificador documental, o índice/menu do GKR e a aprovação final exigem governança específica. Divergência histórica de versão interna do Anexo C será tratada independentemente.

**Estado de saída:** `DRAFT / NON-NORMATIVE / DOCUMENT-ONLY / NOT READY FOR PRODUCT ENGINEERING`.
