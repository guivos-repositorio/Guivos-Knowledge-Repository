---
id: GKR-UX-OPPORTUNITIES-LIVE-001
title: Oportunidades em Movimento — Gráfico Vivo e Aplicação nas Homes
status: active
version: 1.0.0
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

# Oportunidades em Movimento — Gráfico Vivo e Aplicação nas Homes

## 1. Finalidade e limite de autoridade

Este documento é uma **referência de concepção narrativa, UX e dados**, acessível pelo MENU do GKR, sobre um único gráfico de linha vivo que expresse a variação de oportunidades efetivamente disponíveis no ecossistema Guivos. Não altera os Documentos Mestres das Homes nem autoriza implementação, produção de dados fictícios, lançamento ou publicação de números como reais.

O gráfico é **instrumento narrativo secundário**, não KPI que substitui a Pessoa, catálogo de funcionalidades, mecanismo comercial ou argumento de urgência.

**Tese:** muitas possibilidades existem além do campo de percepção de uma Pessoa. Cursos, encontros, caminhadas, pedaladas, projetos e experiências surgem, ficam disponíveis e se encerram em seus próprios tempos. A Guivos pode aproximar Pessoas de possibilidades reais e contextualizadas, sem garantir que toda oportunidade seja relevante ou acessível para qualquer Pessoa.

## 2. Direção editorial

**Título candidato:** O mundo de possibilidades não para.

**Texto de apoio candidato:** Oportunidades surgem, se transformam e se encerram todos os dias. Muitas podem fazer sentido para diferentes momentos da vida, mas nem sempre chegam ao nosso campo de percepção. A Guivos ajuda a aproximar pessoas dessas possibilidades, conectando contextos e tornando caminhos mais visíveis.

**Complemento:** Ver uma oportunidade não é obrigação de participar. O papel da Guivos é ampliar percepção, ajudar a reconhecer contexto e preservar a decisão da Pessoa.

Evitar: «você perdeu X oportunidades», contagens de oportunidades supostamente personalizadas, pressão para cadastro, sensação fabricada de escassez, aumento contínuo fictício, promessas de match e causalidade de evolução não demonstrada.

## 3. Matriz de aplicação nas Homes

| Home | Decisão editorial | Local/contexto | Justificativa e limite |
|---|---|---|---|
| **Pessoa — pública principal** | **Prioritária, condicionada à viabilidade e ao design** | **Movimento 02 — Possibilidades Reais**; pode estabelecer continuidade para Movimento 06 | Torna observável a existência dinâmica de oportunidades reais, sem capturar a Hero nem confundir presença com relevância |
| **Organizações e Coletivos — pública** | **Opcional e secundária** | **Movimento 08 — Circulação de valor, supply e escala responsável**; pode dialogar com a ideia de capacidades do Movimento 02 | Mostra que o supply é gerado por Organizações/Coletivos, mas não duplica automaticamente o impacto principal nem vira ranking comercial |
| Guivos Intelligence | **Opcional como visão analítica específica**, não cópia do apelo público | Superfície de dados sob contrato próprio | Permite estudar a evolução da oferta com métricas verificáveis, sujeito a escopo e acesso |
| Mall | **Não recomendado como gráfico global da Home** | Somente se houver caso próprio validado | Mall não deve se confundir com total de oportunidades do ecossistema |
| Travel | **Não recomendado como gráfico global da Home** | Somente se houver caso próprio validado | Experiências e reservas requerem disponibilidade e regras particulares |
| Business | **Não recomendado como gráfico global da Home** | Dados de programas/organizações apenas em contexto próprio | Evitar tratar métrica global como indicador comercial de cliente |
| Media | **Não recomendado como gráfico global da Home** | Eventual matéria explicativa/editorial | Não presumir que mídia equivale a oferta ativa |
| Ads | **Não recomendado como gráfico global da Home** | Sem função publicitária direta | Relevância e oportunidade não são compradas com mídia |

O **mesmo componente de dados** pode alimentar mais de uma superfície; a inclusão visual em uma Home não exige sua reprodução em outra. As duas Homes expressam a mesma Guivos sob perspectivas complementares, conforme seus Masters vigentes.

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
| OPM-06 O/C | Há benefício narrativo comprovado na segunda Home ou a repetição seria redundante? | Aberto |
| OPM-07 Prova pública | Números, alcance geográfico e disponibilidade são reais e auditáveis? | Aberto |
| OPM-08 Publicação | Aprovações, compatibilidade com Masters e qualidade do design estão concluídas? | Aberto |

A recomendação de **Home Pessoa / Movimento 02** é de pertinência semântica, não um novo movimento obrigatório ou ordem de implementação. O gráfico pode ser rejeitado no design final se prejudicar clareza, confiança ou ritmo.

## 8. Encaminhamento

Este documento específico deve ficar no MENU, sob **Experiência e Journey → Visualizações e Narrativa → Oportunidades em Movimento**, como referência de design e dados, mantendo Masters como autoridade corrente de cada Home. Após avaliação de OPM-01..08, propor ajuste editorial pontual aos Masters **somente se necessário**. Não iniciar integração real, eventos produtivos ou publicação sem validação.

```text
DOCUMENT → GKR-UX-OPPORTUNITIES-LIVE-001 v1.0.0
HOME PESSOA → PRIMARY CANDIDATE (MOVIMENTO 02)
HOME O/C → OPTIONAL CONTEXTUAL CANDIDATE (MOVIMENTO 08)
OTHER HOMES → NO DEFAULT REPLICATION
DATA → REAL VERIFIED EVENTS ONLY
DESIGN → NOT REQUIRED TO USE GRAPH IF UNSUITABLE
HOME MASTERS → NOT MODIFIED
IMPLEMENTATION → NOT AUTHORIZED
```
