---
id: GKR-JOURNEY-SURFACE-DETAIL-COLLECTIVE-001
title: Detalhamento Obrigatório das Superfícies do Coletivo
status: active
version: 0.11.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-30
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-100
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Detalhamento Obrigatório das Superfícies do Coletivo

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não altera a contagem de entradas.

A reconciliação pós-PR #313/#314 estabelece que `UXA-016/018` e o SVG associado ao antigo início do Coletivo são históricos `superseded`. Materiais posteriores de operação do responsável, solicitações e Planos preservam apenas a maturidade que possuam por autoridade própria e não podem ser promovidos, por inferência, ao status de wireframe principal autenticado final do Coletivo.

A arquitetura da informação autenticada do Coletivo está definida por `GKR-UX-ORGCOL-AUTH-IA-001` no estágio **pre-surface-map**. O mapa final de superfícies, a navegação materializada e o wireframe principal autenticado do Coletivo permanecem **pendentes**.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COL-001 | presença pública sustentada por UXA-056/062/063; `UXA-016/018` permanecem somente como histórico superseded | estado público preservado no recorte próprio; início autenticado final não definido | descoberta/acesso público; entrada protegida depende de arquitetura vigente | consultar presença pública; continuidade autenticada depende do estado atual | descoberta e participação nos fluxos que tenham autoridade própria | identidade, propósito e informações públicas autorizadas | público para consulta; autoridade específica para áreas protegidas | retornar ou encerrar consulta | `UXA-016` e `UXA-018` superseded | continuidade pública preservada por UXA-056/062/063 | **separação final entre presença pública, entrada autenticada e operação interna ainda pendente** | presença pública válida ≠ wireframe principal autenticado do Coletivo |
| GKR-SURF-COL-002 | UXA-086/087 e navegação UXA-100-A4 permanecem evidência histórica/local de uma superfície administrativa; não são baseline final da experiência principal autenticada | materialização local existente; status de wireframe principal vigente: pendente; IA autenticada definida pre-surface-map | acesso protegido com representação válida | compreender contexto operacional no escopo do pacote e acessar capacidades autorizadas | GKR-TRN-112 para solicitações; continuidade de Planos no contrato próprio | identidade, propósito, representação e escopo no limite necessário | representação válida e escopo concedido | permanecer, retornar ou abrir capacidade autorizada | nenhuma supersessão automática de UXA-086/087; **supersedida apenas a inferência de que definem a experiência principal final** | TRN-112 e contratos de Planos preservam maturidade própria, sem provar arquitetura principal vigente | **mapa final de superfícies, navegação principal materializada e wireframe autenticado final pendentes** | referência administrativa local ≠ wireframe principal final do Coletivo; IA definida ≠ wireframe vigente |
| GKR-SURF-COL-003 | UXA-088 — `docs/experience-architecture/uxa-088-collective-request-management-low-fidelity-wireframes.md`; validação UXA-089; efeitos na Pessoa em UXA-066/067 | materialização 0.2.0; validação 0.1.0 | GKR-TRN-105 ou GKR-TRN-112; resposta adicional via GKR-TRN-107 | analisar solicitação e escolher aguardar, pedir informação, aprovar ou recusar dentro da autoridade | GKR-TRN-106, GKR-TRN-108 ou GKR-TRN-109; permanência na fila quando não houver decisão | dados autorizados da solicitação; estado; referência temporal; critérios previamente apresentados; fundamento; resposta adicional; dados protegidos mínimos quando aplicável | representação válida; finalidade limitada; autoridade específica verificada; confirmação antes de aprovação ou recusa | voltar sem decidir; aguardar; pedir informação; descartar rascunho; interromper por autoridade insuficiente | referências na perspectiva da Pessoa não são supersedidas | superfície validada; handoffs bilaterais governados | demais áreas internas | sete SVGs desktop validados no fluxo especializado; isso não define a UX principal completa |
| GKR-SURF-COL-004 | ausente; autoridade UXA-059 | indeterminado | vínculo formado | indeterminado | gestão, saída ou contestação | indeterminado | papel e autoridade esperados; não materializados | indeterminado | nenhuma identificada | ausente | continuidade interna | não iniciado pela UXA-100-A4 |
| GKR-SURF-COL-005 | ausente; autoridade UXA-058/059 | indeterminado | vínculo e autoridade | indeterminado | atualizações aos participantes | indeterminado | papel, audiência e finalidade esperados | indeterminado | nenhuma identificada | ausente | superfície e regras operacionais | não iniciado pela UXA-100-A4 |
| GKR-SURF-COL-006 | UXA-059 | indeterminado | governança interna | indeterminado por atividade | resultados e próximas decisões | conteúdos dispersos | autoridade contextual esperada | indeterminado | nenhuma identificada | não examinado | matriz operacional integrada | não iniciado pela UXA-100-A4 |
| GKR-SURF-COL-007 | UXA-058 | indeterminado | evento protegido | avaliar evento dentro de competência limitada | decisão ou encaminhamento | evidências mínimas, relato, estado e encaminhamento | autoridade protegida; finalidade limitada | contestar, corrigir ou encaminhar conforme contrato | nenhuma identificada | não examinado | fluxo protegido completo | não iniciado pela UXA-100-A4 |
| GKR-SURF-COL-008 | ausente; autoridade UXA-019 | indeterminado | proposta institucional | avaliar, negociar, aceitar ou recusar proposta | negociação e decisão bilateral | finalidade, compromissos, recursos, limites e dados previstos | autoridade do responsável e aprovação bilateral | recusar, ajustar, pausar ou encerrar conforme contrato | nenhuma identificada | ausente | relação Organização–Coletivo | não iniciado pela UXA-100-A4 |
| GKR-SURF-COL-301 | UXA-100/A1/A2/A3/A4 — `uxa-100-collective-plans-screen-desktop.svg`; comparação; board | 0.1.0 canônico no fluxo especializado de Planos | limite legítimo ou origem administrativa contratada | compreender Livre/Mobiliza/Impacta/Rede, uso e delta; manter ou escolher mudança | TRN-411, TRN-413, TRN-416 ou retorno ao contexto administrativo | plano atual, ciclo, atividades/oportunidades, publicações ativas, admins, unidades, preços e benefícios incrementais | representação válida; alternativas gratuitas/operacionais preservadas; nenhuma publicação existente perde visibilidade | permanecer, aguardar ciclo, manter rascunho, encerrar/agendar ou retornar | nenhuma supersessão do fluxo especializado; a origem principal final permanece pendente | contratos de origem/retorno e transições internas preservam maturidade própria | contratação/dimensionamento após BND-002 e cobrança real; materialização principal vigente | comparação incremental e estado de limite pertencem à mesma família |
| GKR-SURF-COL-302 | UXA-100/A2/A3 — board `uxa-100-collective-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-411 | revisar contratação Mobiliza/Impacta ou outra mudança autonomamente configurável e confirmar ou voltar | TRN-412 ou retorno a COL-301 | plano alvo, preço, periodicidade, recorrência, pagador autorizado, beneficiário, início e método em simulação | autoridade financeira/representação válidas; nenhuma pré-seleção | voltar/revisar sem contratar | estado do board promovido por UXA-100-A3 | validada localmente no pacote | gateway, tributação, comissão e proration fora do escopo | assinatura permanece separada de transação/publicação paga |
| GKR-SURF-COL-303 | UXA-100/A2/A3 — board `uxa-100-collective-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-413 | revisar downgrade/cancelamento, tratar excedentes e confirmar | TRN-414 ou retorno a COL-301 | publicações gratuitas/pagas, admins, núcleos/unidades, compromissos, exportação, plano futuro e data efetiva | responsável autorizado; compromissos assumidos não desaparecem; dados não são apagados silenciosamente | manter plano; ajustar escolhas; exportar; voltar | estado do board promovido por UXA-100-A3 | validada localmente no pacote | política transacional futura e efeitos financeiros entre ciclos | downgrade só efetiva após tratamento das capacidades excedentes aplicáveis |
| GKR-SURF-COL-304 | UXA-100/A2/A3 — board `uxa-100-collective-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-412 ou TRN-414 | compreender resultado, recuperar falha ou retornar | TRN-415; tentar novamente quando aplicável | plano resultante/anterior, capacidade, confirmação/recibo, publicações preservadas e estado de falha | confirmação real para ativar; falha preserva estado anterior e dados | nova tentativa consciente; retorno a Planos | estados de resultado promovidos por UXA-100-A3 | validada localmente no pacote | execução financeira e entitlement não implementados | sucesso e falha compartilham família sem compartilhar consequência |

## 3. Regras preservadas

- valores sem evidência permanecem `indeterminado`, `ausente` ou `não examinado`;
- validação local de `COL-002` não autoriza tratá-la como arquitetura principal final nem completar `COL-004` a `COL-008` por analogia;
- validação do fluxo especializado `COL-003` permanece independente da definição do wireframe principal;
- autoridade é verificada por escopo concedido e não por autodeclaração;
- abrir Planos não inicia contratação nem cobrança;
- retornar de Planos não cancela assinatura nem altera capacidade;
- atingir limite do plano não reduz visibilidade de publicação existente;
- quando a contratação não puder ser concluída autonomamente, a continuidade pode seguir para `BND-002`;
- `BND-002` não pertence semanticamente ao plano Rede nem a qualquer outro plano específico.

## 4. Efeito da UXA-100-A4 após a reconciliação

A UXA-100-A4 preserva o contrato especializado de Planos e sua navegação documental. Ela não define a futura arquitetura principal autenticada do Coletivo.

```text
contrato de origem/retorno de Planos
≠ wireframe principal autenticado vigente

materialização administrativa local
≠ baseline final da experiência do Coletivo
```

A futura UX principal deverá ser construída a partir dos fundamentos, papéis, jobs, arquitetura da informação autenticada e estado vigente.

## 5. Estado

O detalhamento está `active` 0.11.0. As superfícies especializadas de solicitações e Planos preservam sua maturidade documental própria. A Jornada do Coletivo continua incompleta e `draft`; a arquitetura da informação autenticada está **definida pre-surface-map**; o mapa final de superfícies, a navegação principal materializada e o wireframe principal autenticado do Coletivo permanecem **pendentes**.