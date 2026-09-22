---
id: GKR-JOURNEY-SURFACE-DETAIL-COLLECTIVE-001
title: Detalhamento Obrigatório das Superfícies do Coletivo
status: active
version: 0.17.5
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-22
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-089
  - GKR-PLANS-COLLECTIVE-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
normative: false
---

# Detalhamento Obrigatório das Superfícies do Coletivo

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não altera a contagem de entradas.

A cadeia autenticada corrente de Coletivo está definida por Jobs/autoridade, Arquitetura da Informação, Surface Map, State Map, Priority Flows, Navigation Materialization e pelo pacote low-fidelity entregue e validado. `GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001 v1.0.0` autoriza o Design high-fidelity, cuja execução permanece `NOT_STARTED`; protótipo interativo e Product Engineering permanecem não liberados.

## 2. Campos por identificador

| ID | Autoridade corrente | Estado/versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COL-001 | GKR-UX-HOME-OC-MASTER-001 + UXA-056 + GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 + GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | presença pública governada pelo Master/UXA-056; continuidade autenticada governada pela arquitetura O/C corrente | descoberta/acesso público; entrada protegida depende de arquitetura vigente | consultar presença pública; continuidade autenticada depende do estado atual | descoberta e participação nos fluxos que tenham autoridade própria | identidade, propósito e informações públicas autorizadas | público para consulta; autoridade específica para áreas protegidas | retornar ou encerrar consulta | `UXA-016` e `UXA-018` somente como proveniência histórica superseded | continuidade pública preservada por GKR-UX-HOME-OC-MASTER-001 + UXA-056; travessia autenticada usa Surface/State Map e o pacote low-fidelity corrente | **separação final entre presença pública, entrada autenticada e operação interna ainda pendente** | presença pública válida ≠ wireframe principal autenticado do Coletivo |
| GKR-SURF-COL-002 | GKR-UX-ORGCOL-AUTH-IA-001 + Surface Map + State Map + Navigation Materialization + Low-Fidelity Delivery/Validation | low-fidelity principal vigente: DELIVERY v0.1.0 + VALIDATION v1.0.0 / PASS; IA autenticada definida em sua maturidade própria; Surface Map v1.1.0 e State Map v1.1.0 canônicos | acesso protegido com representação válida | compreender contexto operacional no escopo do pacote e acessar capacidades autorizadas | GKR-TRN-112 para solicitações; continuidade de Planos no contrato próprio | identidade, propósito, representação e escopo no limite necessário | representação válida e escopo concedido | permanecer, retornar ou abrir capacidade autorizada | produtores visuais históricos permanecem somente no Git; nenhuma referência local substitui a arquitetura autenticada corrente | TRN-112 e contratos de Planos preservam maturidade própria, sem provar arquitetura principal vigente | **Priority Flows e Navigation Materialization definidos; low-fidelity principal entregue e validado; high-fidelity autorizado, com execução ainda não iniciada** | referência administrativa local ≠ wireframe principal final do Coletivo; Surface Map/State Map definidos ≠ wireframe vigente |
| GKR-SURF-COL-003 | UXA-056 + UXA-089/090/092 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado corrente validado | GKR-TRN-105 ou GKR-TRN-112; resposta adicional via GKR-TRN-107 | analisar solicitação e escolher aguardar, pedir informação, aprovar ou recusar dentro da autoridade | GKR-TRN-106, GKR-TRN-108 ou GKR-TRN-109; permanência na fila quando não houver decisão | dados autorizados da solicitação; estado; referência temporal; critérios previamente apresentados; fundamento; resposta adicional; dados protegidos mínimos quando aplicável | representação válida; finalidade limitada; autoridade específica verificada; confirmação antes de aprovação ou recusa | voltar sem decidir; aguardar; pedir informação; descartar rascunho; interromper por autoridade insuficiente | referências na perspectiva da Pessoa não são supersedidas | superfície validada; handoffs bilaterais governados | demais áreas internas | fluxo especializado validado; produtores visuais removidos não são entrada atual e isso não define a UX principal completa |
| GKR-SURF-COL-004 | GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 + GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | contratada / não materializada | vínculo formado | compreender/gerir vínculo dentro da autoridade | gestão, saída ou contestação | estado do vínculo e dados mínimos aplicáveis | representação e autoridade | retorno/saída conforme regra | programa histórico de wireframes absorvido | não examinada ponta a ponta | continuidade interna | contrato corrente existe; materialização específica não foi inferida |
| GKR-SURF-COL-005 | UXA-058 + GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 + GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | contratada / não materializada | vínculo e autoridade | comunicar dentro da finalidade legítima | atualização aos participantes autorizados | audiência, finalidade e conteúdo permitido | papel, audiência e finalidade | retorno/revisão conforme contrato | programa histórico de wireframes absorvido | não examinada ponta a ponta | superfície e regras operacionais | comunicação oficial não implica mensagem privada irrestrita |
| GKR-SURF-COL-006 | GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 + GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | contratada / não materializada | governança interna | operar atividade/consulta/decisão dentro de autoridade | resultados e próximas decisões | estado, atividade, decisão e contexto permitido | autoridade contextual | interromper/retornar conforme regra | programa histórico de wireframes absorvido | não examinada ponta a ponta | matriz operacional integrada | atividade não equivale automaticamente a resultado ou impacto |
| GKR-SURF-COL-007 | UXA-058 + GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 + GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | contratada; cobertura low-fidelity parcial em C-A/X2; validação dedicada ponta a ponta não comprovada | condição de proteção/moderação aplicável | avaliar e atuar em proteção/moderação dentro da autoridade proporcional | proteção, moderação ou encaminhamento compatível com o estado | evidências mínimas, relato, estado e encaminhamento no limite autorizado | autoridade de proteção/moderação; finalidade limitada; proporcionalidade | contestar, corrigir, revisar ou encaminhar conforme contrato | programa histórico de wireframes absorvido | Governança e Proteção = PASS no pacote low-fidelity; continuidade dedicada não examinada ponta a ponta | materialização dedicada e handoffs específicos permanecem abertos | proteção/moderação não equivale a punição automática nem amplia autoridade sobre participantes |
| GKR-SURF-COL-008 | UXA-019 + GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 + GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | contratada; lifecycle O↔C definido; cobertura low-fidelity parcial; validação dedicada ponta a ponta não comprovada | proposta ou relação O↔C vigente conforme estado | avaliar, negociar, aceitar, revisar, pausar ou encerrar dentro da autoridade bilateral | continuidade bilateral conforme lifecycle corrente | finalidade, compromissos, recursos, limites, dados e versão materialmente relevante | autoridade do responsável e aprovação bilateral quando aplicável | recusar, ajustar, pausar, contestar ou encerrar conforme contrato | programa histórico de wireframes absorvido | Relações O↔C = PASS no pacote low-fidelity; TRN-206..209 preservam maturidade contratada | materialização dedicada e continuidade ponta a ponta permanecem abertas | escopo exclusivo Organização–Coletivo; não abrange Coletivo–Coletivo por analogia |
| GKR-SURF-COL-301 | GKR-PLANS-COLLECTIVE-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado de Planos validado | limite legítimo ou origem administrativa contratada | compreender Livre/Mobiliza/Impacta/Rede, uso e delta; manter ou escolher mudança | TRN-411, TRN-413, TRN-416 ou retorno ao contexto administrativo | plano atual, ciclo, atividades/oportunidades, publicações ativas, admins, unidades, preços e benefícios incrementais | representação válida; alternativas gratuitas/operacionais preservadas; nenhuma publicação existente perde visibilidade | permanecer, aguardar ciclo, manter rascunho, encerrar/agendar ou retornar | nenhuma supersessão do fluxo especializado; a origem principal final permanece pendente | contratos de origem/retorno e transições internas preservam maturidade própria | contratação/dimensionamento após BND-002 e cobrança real; materialização principal vigente | comparação incremental e estado de limite pertencem à mesma família |
| GKR-SURF-COL-302 | GKR-PLANS-COLLECTIVE-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-411 | revisar contratação Mobiliza/Impacta ou outra mudança autonomamente configurável e confirmar ou voltar | TRN-412 ou retorno a COL-301 | plano alvo, preço, periodicidade, recorrência, pagador autorizado, beneficiário, início e método em simulação | autoridade financeira/representação válidas; nenhuma pré-seleção | voltar/revisar sem contratar | estado funcional preservado no Registry | validada localmente no pacote | gateway, tributação, comissão e proration fora do escopo | assinatura permanece separada de transação/publicação paga |
| GKR-SURF-COL-303 | GKR-PLANS-COLLECTIVE-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-413 | revisar downgrade/cancelamento, tratar excedentes e confirmar | TRN-414 ou retorno a COL-301 | publicações gratuitas/pagas, admins, núcleos/unidades, compromissos, exportação, plano futuro e data efetiva | responsável autorizado; compromissos assumidos não desaparecem; dados não são apagados silenciosamente | manter plano; ajustar escolhas; exportar; voltar | estado funcional preservado no Registry | validada localmente no pacote | política transacional futura e efeitos financeiros entre ciclos | downgrade só efetiva após tratamento das capacidades excedentes aplicáveis |
| GKR-SURF-COL-304 | GKR-PLANS-COLLECTIVE-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-412 ou TRN-414 | compreender resultado, recuperar falha ou retornar | TRN-415; tentar novamente quando aplicável | plano resultante/anterior, capacidade, confirmação/recibo, publicações preservadas e estado de falha | confirmação real para ativar; falha preserva estado anterior e dados | nova tentativa consciente; retorno a Planos | estados de resultado preservados no Registry | validada localmente no pacote | execução financeira e entitlement não implementados | sucesso e falha compartilham família sem compartilhar consequência |

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

## 4. Entrada e retorno de Planos — contrato corrente

O contrato corrente de Planos e sua navegação administrativa está preservado nos registries e em `GKR-PLANS-COLLECTIVE-001`. Ele não define a arquitetura principal autenticada do Coletivo.

```text
contrato de origem/retorno de Planos
≠ wireframe principal autenticado vigente

materialização administrativa local
≠ baseline final da experiência do Coletivo
```

A continuidade visual high-fidelity deverá partir dos fundamentos, papéis, jobs, arquitetura da informação autenticada, Surface Map, State Map, Navigation Materialization e do pacote low-fidelity corrente já validado.

## 5. Estado

O detalhamento está `active` 0.17.5. As superfícies especializadas de solicitações e Planos preservam sua maturidade documental própria. A Jornada do Coletivo está `active`; a arquitetura da informação autenticada preserva sua maturidade documental própria; `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.0`, `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.0` e `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0` permanecem autoridades canônicas. A Navigation Materialization está definida em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`; o wireframe autenticado low-fidelity do Coletivo foi entregue em `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` e validado com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. High-fidelity está autorizado e ainda não iniciado; protótipo interativo e implementação permanecem gates separados.