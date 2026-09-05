---
id: GKR-JOURNEY-SURFACE-DETAIL-ORGANIZATION-001
title: Detalhamento Obrigatório das Superfícies da Organização
status: active
version: 0.7.0
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

# Detalhamento Obrigatório das Superfícies da Organização

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens, maturidade ou status das entradas por conta própria.

A reconciliação pós-PR #313/#314 estabelece que o antigo SVG associado a `ORG-001`, produzido no ciclo `UXA-015/017`, é **histórico e superseded**. O ativo físico foi removido por F-006; sua proveniência permanece no histórico Git e não constitui baseline de produto ou autoridade de Design da experiência autenticada da Organização.

A UXA-100-A4 preserva contratos e decisões de navegação do fluxo de Planos no limite documental em que tenham autoridade própria, mas não transforma o SVG histórico de `ORG-001` em wireframe vigente.

A arquitetura da informação autenticada da Organização está definida por `GKR-UX-ORGCOL-AUTH-IA-001` no estágio **pre-surface-map**. Isso não define mapa final de superfícies, wireframe principal, UI, protótipo ou implementação.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-ORG-001 | contrato funcional de superfície ainda sujeito à consolidação; materialização visual = Design-only; `UXA-015/017` e `antigo ativo visual F-006 de ORG-001` permanecem somente como histórico superseded | estado visual vigente: não definido; IA autenticada definida pre-surface-map | identidade e autoridade | responsabilidade institucional deve respeitar a IA autenticada vigente; composição visual principal ainda não definida | contratos especializados podem partir/retornar ao contexto institucional quando sua própria autoridade os sustentar | identidade, unidade, autoridade, compromissos e evidências no limite dos fundamentos e da IA vigentes | representação institucional válida | retorno e revisão permanecem requisitos funcionais; materialização final pendente | `UXA-015`, `UXA-017` e SVG associado superseded | `TRN-427/428` preservam seu estado documental próprio, sem provar materialização vigente de ORG-001; TRN-201 preserva maturidade própria | **mapa funcional de superfícies/estados ainda sujeito à consolidação; materialização visual e matriz visual pertencem a Design** | Organização permanece participante; não é Guivos Business; IA definida ≠ wireframe vigente; contrato de navegação ≠ wireframe vigente |
| GKR-SURF-ORG-002 | UXA-008 — `docs/experience-architecture/UXA-008 [historical producer removed_after_absorption in F-016]` | indeterminado | autoridade institucional | criar, revisar, enviar ou cancelar cadastro | estado institucional de publicação | dados da oportunidade, responsável, disponibilidade, preço, elegibilidade, riscos e relação comercial | autoridade institucional; confirmação antes do envio | editar, salvar rascunho, cancelar ou retirar conforme estado | nenhuma identificada | parcial | integração com descoberta | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-003 | UXA-008 — `docs/experience-architecture/UXA-008 [historical producer removed_after_absorption in F-016]` | indeterminado | cadastro revisado e aprovado | ativar, pausar, corrigir ou encerrar dentro do ciclo institucional | distribuição elegível em superfícies de oportunidades | estado institucional, disponibilidade, versão publicada e condições vigentes | autoridade institucional e aprovação aplicável | pausar, corrigir, retirar ou encerrar conforme ciclo | significado anterior dividido pela UXA-078; Detalhe de Oportunidade migra para GKR-SURF-PER-203 | parcial | integração publicação–descoberta | estado institucional protegido; não representa o detalhe percebido pela Pessoa |
| GKR-SURF-ORG-004 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | decisão institucional | formular, revisar, enviar ou retirar proposta | avaliação pelo Coletivo | finalidade, compromissos, recursos, dados, autonomia e saída | autoridade institucional | retirar, ajustar ou cancelar antes de aceite conforme contrato | nenhuma identificada | ausente | superfície bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-005 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | proposta | negociar, aprovar, recusar ou solicitar ajuste | aprovação, recusa ou ajuste | proposta, contraproposta, compromissos, recursos e limites | autoridades bilateralmente legítimas | recusar, ajustar, pausar negociação ou sair | nenhuma identificada | ausente | materialização bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-006 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | aprovação bilateral | revisar e decidir continuidade da relação | renovação, ajuste, pausa ou encerramento | estado, compromissos, recursos, evidências e histórico | autoridade bilateral conforme efeito | renovar, ajustar, pausar, contestar ou encerrar | nenhuma identificada | ausente | operação bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-007 | UXA-014 — `docs/experience-architecture/uxa-014-organizations-and-collectives-functional-foundation.md` | indeterminado | atividades e compromissos | indeterminado | revisão institucional | evidências e resultados dispersos; inventário ausente | indeterminado | indeterminado | nenhuma identificada | não examinado | matriz visual institucional | responsabilidade conhecida com evidência insuficiente para classificar |
| GKR-SURF-ORG-301 | UXA-100/A1/A2/A3/A4 — `uxa-100-organization-plans-screen-desktop.svg`; comparação; board | 0.1.0 canônico no fluxo especializado de Planos | capacidade legítima alcançada ou origem institucional contratada | compreender Conecta/Eleva/Transforma, uso e delta; manter, mudar ou solicitar dimensionamento assistido | TRN-421, TRN-423, TRN-426 ou retorno ao contexto institucional | plano atual, ciclo, oportunidades/programas, publicações ativas, admins, unidades, Coletivos relacionados, preços e benefícios incrementais | autoridade institucional válida; alternativas de arquivar/agendar/rascunho preservadas; ranking orgânico não muda | permanecer, arquivar, agendar, manter rascunho ou retornar | nenhuma supersessão do fluxo especializado; a origem visual antiga de ORG-001 não é baseline vigente | `TRN-427/428` preservam seu estado documental próprio; transições internas locais | contratação/dimensionamento após BND-002 e cobrança real; materialização vigente da origem institucional | comparação incremental e estado de capacidade pertencem à mesma família |
| GKR-SURF-ORG-302 | UXA-100/A2/A3 — board `uxa-100-organization-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-421 | revisar contratação de plano de Organização e confirmar ou voltar quando autonomamente configurável | TRN-422 ou retorno a ORG-301 | plano alvo, preço, periodicidade, recorrência, pagador/autoridade financeira, beneficiário institucional, início e método em simulação | autoridade financeira identificada; nenhuma pré-seleção; pagamento não amplia acesso à jornada pessoal de Pessoas | voltar/revisar sem contratar | estado do board promovido por UXA-100-A3 | validada localmente no pacote | gateway, tributação e proration fora do escopo | revisão pré-contratual, não checkout implementado |
| GKR-SURF-ORG-303 | UXA-100/A2/A3 — board `uxa-100-organization-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-423 | revisar downgrade/cancelamento e selecionar explicitamente capacidades mantidas/encerradas | TRN-424 ou retorno a ORG-301 | unidades, administradores, publicações, Coletivos relacionados, integrações, dados a exportar, plano futuro e data efetiva | representante autorizado; nenhum dado/histórico é apagado para forçar retenção | manter plano; ajustar seleção; exportar; voltar | estado do board promovido por UXA-100-A3 | validada localmente no pacote | efeitos financeiros entre ciclos e execução institucional não implementados | excedentes são tratados explicitamente antes da efetivação |
| GKR-SURF-ORG-304 | UXA-100/A2/A3 — board `uxa-100-organization-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-422 ou TRN-424 | compreender resultado, recuperar falha ou retornar | TRN-425; tentar novamente quando aplicável | plano resultante/anterior, capacidade, confirmação/recibo, direitos/dados preservados e estado de falha | confirmação real para ativar; falha preserva plano anterior identificável | nova tentativa consciente; retorno a Planos | estados de resultado promovidos por UXA-100-A3 | validada localmente no pacote | processamento financeiro e entitlement técnico não implementados | sucesso e falha compartilham família sem compartilhar consequência |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

A existência física de um SVG histórico não autoriza classificá-lo como wireframe vigente nem como evidência de validação atual.

## 4. Regras de Planos preservadas

- capacidade contratada não altera relevância, confiança ou evidência de impacto;
- Organização usa `Conecta · Eleva · Transforma`;
- Guivos Business usa `Start · Growth · Scale · Enterprise` em produto separado;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- abrir Planos não inicia contratação nem cobrança;
- retornar de Planos não altera plano ou capacidade;
- quando o autoatendimento não for suficiente, `BND-002` representa contratação/dimensionamento assistido e não plano específico;
- pagamento por Organização não concede acesso ao contexto individual de Pessoas;
- downgrade exige seleção explícita das capacidades institucionais que permanecerão;
- dados agregados e históricos não são apagados automaticamente para forçar retenção.

## 5. Efeito da UXA-100-A4 após a reconciliação

A UXA-100-A4 permanece evidência do pacote especializado de Planos, incluindo decisões documentais de origem/retorno e correção histórica de nomenclatura. Após a reconciliação pós-PR #313/#314:

```text
contrato de navegação de Planos
≠ wireframe principal autenticado vigente

SVG histórico de ORG-001
≠ baseline de produto
≠ UI definida
≠ validação vigente do wireframe principal
```

Qualquer futura materialização da Visão Geral da Organização deverá ser construída a partir dos fundamentos, Jobs/autoridades e da arquitetura da informação autenticada vigente, e não pela promoção automática do SVG histórico.

## 6. Estado

O detalhamento está `active` 0.7.0 como parte integrante do registro. A Jornada da Organização permanece incompleta e `draft`. A arquitetura da informação autenticada está **definida pre-surface-map**; o mapa final de superfícies e o wireframe principal autenticado da Organização permanecem **pendentes**, enquanto fluxos especializados preservam apenas a maturidade que possuam por autoridade própria.