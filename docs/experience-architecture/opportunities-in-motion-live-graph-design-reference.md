---
id: GKR-UX-OPPORTUNITIES-LIVE-001
title: Oportunidades em Movimento — Gráfico Vivo no Movimento 11 da Home Pessoa
status: active
version: 1.1.1
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-12
normative: false
maturity: design_reference_non_operational
related:
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NARR-003
---

# Oportunidades em Movimento — Gráfico Vivo no Movimento 11 da Home Pessoa

## 1. Finalidade e limite de autoridade

Este documento é uma **referência de concepção narrativa, UX e dados**, acessível pelo MENU do GKR, sobre um único gráfico de linha vivo que expresse a variação de oportunidades efetivamente disponíveis no ecossistema Guivos. A aplicação editorial aprovada é exclusiva da Home Pessoa / Movimento 11 — Descoberta; o Documento Mestre recebe referência pontual nesta mesma PR. Não autoriza implementação, produção de dados fictícios, lançamento ou publicação de números como reais.

O gráfico é **instrumento narrativo secundário**, não KPI que substitui a Pessoa, catálogo de funcionalidades, mecanismo comercial ou argumento de urgência.

**Tese:** muitas possibilidades existem além do campo de percepção de uma Pessoa. Cursos, encontros, caminhadas, pedaladas, projetos e experiências surgem, ficam disponíveis e se encerram em seus próprios tempos. A Guivos pode aproximar Pessoas de possibilidades reais e contextualizadas, sem garantir que toda oportunidade seja relevante ou acessível para qualquer Pessoa.

## 2. Movimento 11 — Descoberta: texto validado

**Aplicação aprovada:** exclusivamente na **Home Pública Pessoa, Movimento 11 — Descoberta**. Não utilizar o gráfico na Home Organizações e Coletivos. A posição no Movimento 02 foi superada pela decisão expressa do fundador.

**Rótulo:** Oportunidades em movimento

**Título:** O mundo de possibilidades não para.

**Texto de apoio:** Oportunidades surgem, se transformam e se encerram todos os dias.

**Elemento visual:** Gráfico vivo de linha com contagem real das oportunidades disponíveis, atualizado conforme eventos efetivos de ativação e saída do estado disponível.

**Texto de fechamento:** Explore o ecossistema, conheça o que existe e descubra qual pode ser o próximo passo.

**CTA:** Descubra a Guivos

**Composição:** rótulo → título → texto de apoio → gráfico → texto de fechamento → CTA.

Não acrescentar texto explicativo **abaixo do gráfico** que replique os Movimentos 04 (desconexão) e 05 (conexão), já responsáveis por explicar as possibilidades invisíveis e o papel da Guivos em aproximá-las. O gráfico **mostra o fenômeno**; não precisa reexplicar o problema.

**Referência visual:** amostra de gráfico com fundo branco validada para orientar a designer, sem constituir layout obrigatório, fonte de números reais ou autorização de publicação. Os valores exemplificativos da imagem são simulados e não devem ser reaproveitados como números reais.

## 3. Aplicação exclusiva e fronteiras

| Home | Decisão |
|---|---|
| **Home Pessoa — Movimento 11** | **APLICAR NA CONCEPÇÃO DO DESIGN**, subordinado à verdade dos dados e aos gates de publicação |
| **Home Organizações e Coletivos** | **NÃO APLICAR** — decisão expressa |
| **Demais Homes** | **NÃO APLICAR** como componente global; não criar replicações por padrão |

O Documento Mestre da Home Pessoa continua sendo a autoridade de narrativa da Home; este documento aprofunda dados, métrica e comportamento do gráfico. Aplicação narrativa aprovada **não implica sistema já disponível**.

## 4. Definição da métrica

**Indicador principal:** contagem de oportunidades **efetivamente disponíveis** e publicamente elegíveis no momento `t` — definição final de `disponível` a adjudicar com Produto/UX e contratos de cadastro.

```text
A(t) = A(t-1) + NOVAS ATIVAÇÕES ELEGÍVEIS - SAÍDAS DO ESTADO DISPONÍVEL
```

| Transição observada | Variação | Nota |
|---|---:|---|
| Cadastro em rascunho | 0 | Não há oportunidade disponível |
| Publicação/ativação elegível | +1 | Apenas primeira entrada no estado disponível |
| Alteração de descrição, imagem ou preço | 0 | Não muda elegibilidade de disponibilidade |
| Encerramento de inscrições ou esgotamento, se indisponível à Pessoa | -1 | A regra exata depende do tipo de oportunidade |
| Inativação, cancelamento ou encerramento definitivo | -1 | Contar apenas se estava disponível |
| Reativação elegível | +1 | Nova transição verificável, não novo cadastro duplicado |
| Evento ocorrido sem inscrições abertas | Depende da definição validada | Não confundir atividade acontecendo com oferta disponível |

Distinguir em todo o contrato: **cadastrada**, **publicada**, **disponível à descoberta**, **inscrições abertas**, **em andamento**, **encerrada**, **cancelada**. Um curso pode ser publicado antes de abrir inscrições; uma caminhada pode terminar sem nunca ter aberto inscrições pela Guivos. É necessário resolver o estado específico antes de contar.

**Uma linha, uma unidade:** total de oportunidades disponíveis por instante. Entradas e saídas podem aparecer como microeventos na mesma visualização, mas não como curvas extras obrigatórias. O crescimento líquido não deve ser confundido com o número bruto de ativações.

## 5. Fonte de verdade e tempo real

Arquitetura candidata:

1. Registro do cadastro e das transições **verificadas** pelo backend responsável por oportunidades.
2. Publicação de eventos idempotentes de ativação/saída da disponibilidade, com `opportunity_id`, `event_id`, `effective_at`, `state_before`, `state_after`, `source` e versão de regra.
3. Projeção de contagem por tempo, com snapshot inicial e histórico suficiente para desenhar a linha; evitar depender apenas do stream, que perde eventos para visitantes que entram depois.
4. Distribuição por **SSE** para recepção unidirecional no navegador, ou WebSocket se a infraestrutura o justificar.
5. **Apache ECharts** como primeira opção de renderização; Lightweight Charts como alternativa. Avaliação técnica e de licenças deve ser conferida antes do desenvolvimento.
6. Recuperação de desconexão por snapshot, reprocessamento idempotente e reconciliação periódica com base de oportunidades.

**Instantâneo** significa atualização automática após a confirmação da transição e propagação técnica mensurável, **não garantia de latência zero**. Definir orçamento de latência, carimbo de atualização e estado «dados temporariamente indisponíveis».

## 6. Contrato visual e acessibilidade

- Um gráfico de linha, sem animações que inventem eventos, números ou escala.
- Se não houver alterações, manter a linha estável.
- Mostrar total atual com clareza, janela temporal identificada e última atualização verificada.
- Ativações e encerramentos podem ser indicados discretamente, com linguagem factual.
- Respeitar `prefers-reduced-motion`, acessibilidade por teclado e alternativa textual de estado e tendência.
- Em ausência de dados reais, usar **demonstração rotulada como simulada** apenas em protótipo; nunca expor «milhares agora» sem contagem comprovada.
- Nenhuma personalização ou inferência sobre Journey, saúde, finanças ou interesses privados a partir da curva global.
- Priorizar estabilidade do layout, desempenho mobile e preservação da liberdade criativa do designer.
- Contexto territorial/local/global somente com filtros, cobertura e proveniência realmente sustentados.

## 7. Critérios de avaliação e evidências necessárias

| Gate | Pergunta / evidência | Estado |
|---|---|---|
| OPM-01 Semântica | O que exatamente torna uma oportunidade disponível e quando ela sai? | Aberto |
| OPM-02 Fonte | Estados do cadastro e eventos têm fonte e identidade verificáveis? | Aberto |
| OPM-03 Integridade | Deduplicação, reativação, correção retroativa e múltiplas edições são reconciliáveis? | Aberto |
| OPM-04 Desempenho | Histórico, SSE, latência, reconexão e custo suportam crescimento? | Aberto |
| OPM-05 UX | O gráfico melhora compreensão da Pessoa sem competir com Hero ou provocar FOMO? | Aberto |
| OPM-06 Exclusividade | A composição respeita a decisão de uso exclusivo na Home Pessoa / Movimento 11, sem replicação na Home O/C? | Direção editorial definida; validar no design |
| OPM-07 Prova pública | Números, alcance geográfico e disponibilidade são reais e auditáveis? | Aberto |
| OPM-08 Publicação | Aprovações, compatibilidade com Masters e qualidade do design estão concluídas? | Aberto |

A recomendação de **Home Pessoa / Movimento 11** é de pertinência semântica, não um novo movimento obrigatório ou ordem de implementação. A designer mantém liberdade de execução visual; eventual ausência do componente ou mudança de posição exige reconciliar a decisão editorial do Movimento 11, sem reivindicar funcionamento real.

## 8. Encaminhamento

Este documento específico deve ficar no MENU, sob **Experiência e Journey → Visualizações e Narrativa → Oportunidades em Movimento**, como referência de design e dados, mantendo Masters como autoridade corrente de cada Home. O ajuste editorial pontual ao Master da Home Pessoa foi incluído nesta PR; a Home O/C permanece inalterada. Os gates OPM-01..08 continuam pertinentes à especificação funcional, às evidências dos dados e à publicação da experiência. Não iniciar integração real, eventos produtivos ou publicação sem validação.

```text
DOCUMENT → GKR-UX-OPPORTUNITIES-LIVE-001 v1.1.1
HOME PESSOA → APPROVED DESIGN PLACEMENT (MOVIMENTO 11)
HOME O/C → DO NOT APPLY
OTHER HOMES → NO DEFAULT REPLICATION
DATA → REAL VERIFIED EVENTS ONLY
DESIGN → NOT REQUIRED TO USE GRAPH IF UNSUITABLE
HOME PERSON MASTER → UPDATED IN PR #656 / HOME O-C MASTER → UNCHANGED
IMPLEMENTATION → NOT AUTHORIZED
```
