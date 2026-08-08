---
id: GKR-JOURNEY-SURFACE-DETAIL-ORGANIZATION-001
title: Detalhamento Obrigatório das Superfícies da Organização
status: active
version: 0.5.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
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
normative: false
---

# Detalhamento Obrigatório das Superfícies da Organização

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens, maturidade ou status das entradas por conta própria.

A UXA-100-A4 reutiliza `ORG-001` como origem institucional de Planos, corrige o rótulo visual obsoleto `Guivos Business` e explicita o retorno de `ORG-301` à Visão Geral sem criar nova superfície ou SVG.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-ORG-001 | UXA-015/017; navegação reformulada UXA-100-A4 — `uxa-015-organization-overview-desktop.svg` | materialização vigente; navegação A4 | identidade e autoridade | consultar momento e escolher responsabilidade institucional | TRN-201 para oportunidades; `TRN-427` para Planos; demais áreas conforme maturidade própria | identidade, unidade, autoridade, compromissos e evidências | representação institucional válida | retornar, revisar contexto ou escolher outra responsabilidade; `TRN-428` retorna de Planos | rótulo `Guivos Business` corrigido pela UXA-100-A4 | **TRN-427/428 integralmente validadas**; TRN-201 preserva maturidade própria | matriz institucional completa | Organização permanece participante; não é Guivos Business |
| GKR-SURF-ORG-002 | UXA-008 — `docs/experience-architecture/uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md` | indeterminado | autoridade institucional | criar, revisar, enviar ou cancelar cadastro | estado institucional de publicação | dados da oportunidade, responsável, disponibilidade, preço, elegibilidade, riscos e relação comercial | autoridade institucional; confirmação antes do envio | editar, salvar rascunho, cancelar ou retirar conforme estado | nenhuma identificada | parcial | integração com descoberta | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-003 | UXA-008 — `docs/experience-architecture/uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md` | indeterminado | cadastro revisado e aprovado | ativar, pausar, corrigir ou encerrar dentro do ciclo institucional | distribuição elegível em superfícies de oportunidades | estado institucional, disponibilidade, versão publicada e condições vigentes | autoridade institucional e aprovação aplicável | pausar, corrigir, retirar ou encerrar conforme ciclo | significado anterior dividido pela UXA-078; Detalhe de Oportunidade migra para GKR-SURF-PER-203 | parcial | integração publicação–descoberta | estado institucional protegido; não representa o detalhe percebido pela Pessoa |
| GKR-SURF-ORG-004 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | decisão institucional | formular, revisar, enviar ou retirar proposta | avaliação pelo Coletivo | finalidade, compromissos, recursos, dados, autonomia e saída | autoridade institucional | retirar, ajustar ou cancelar antes de aceite conforme contrato | nenhuma identificada | ausente | superfície bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-005 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | proposta | negociar, aprovar, recusar ou solicitar ajuste | aprovação, recusa ou ajuste | proposta, contraproposta, compromissos, recursos e limites | autoridades bilateralmente legítimas | recusar, ajustar, pausar negociação ou sair | nenhuma identificada | ausente | materialização bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-006 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | aprovação bilateral | revisar e decidir continuidade da relação | renovação, ajuste, pausa ou encerramento | estado, compromissos, recursos, evidências e histórico | autoridade bilateral conforme efeito | renovar, ajustar, pausar, contestar ou encerrar | nenhuma identificada | ausente | operação bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-007 | UXA-014 — `docs/experience-architecture/uxa-014-organizations-and-collectives-functional-foundation.md` | indeterminado | atividades e compromissos | indeterminado | revisão institucional | evidências e resultados dispersos; inventário ausente | indeterminado | indeterminado | nenhuma identificada | não examinado | matriz visual institucional | responsabilidade conhecida com evidência insuficiente para classificar |
| GKR-SURF-ORG-301 | UXA-100/A1/A2/A3/A4 — `uxa-100-organization-plans-screen-desktop.svg`; comparação; board | 0.1.0 canônico; retorno A4 | `TRN-427` ou capacidade legítima alcançada | compreender Conecta/Eleva/Transforma, uso e delta; manter, mudar ou solicitar dimensionamento assistido | TRN-421, TRN-423, TRN-426 ou `TRN-428` | plano atual, ciclo, oportunidades/programas, publicações ativas, admins, unidades, Coletivos relacionados, preços e benefícios incrementais | autoridade institucional válida; alternativas de arquivar/agendar/rascunho preservadas; ranking orgânico não muda | permanecer, arquivar, agendar, manter rascunho ou retornar à Visão Geral | origem e retorno formalizados UXA-100-A4 | **TRN-427/428 integrais; transições internas locais** | contratação/dimensionamento após BND-002 e cobrança real | comparação incremental e estado de capacidade pertencem à mesma família |
| GKR-SURF-ORG-302 | UXA-100/A2/A3 — board `uxa-100-organization-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-421 | revisar contratação de plano de Organização e confirmar ou voltar quando autonomamente configurável | TRN-422 ou retorno a ORG-301 | plano alvo, preço, periodicidade, recorrência, pagador/autoridade financeira, beneficiário institucional, início e método em simulação | autoridade financeira identificada; nenhuma pré-seleção; pagamento não amplia acesso à jornada pessoal de Pessoas | voltar/revisar sem contratar | estado do board promovido por UXA-100-A3 | validada localmente no pacote | gateway, tributação e proration fora do escopo | revisão pré-contratual, não checkout implementado |
| GKR-SURF-ORG-303 | UXA-100/A2/A3 — board `uxa-100-organization-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-423 | revisar downgrade/cancelamento e selecionar explicitamente capacidades mantidas/encerradas | TRN-424 ou retorno a ORG-301 | unidades, administradores, publicações, Coletivos relacionados, integrações, dados a exportar, plano futuro e data efetiva | representante autorizado; nenhum dado/histórico é apagado para forçar retenção | manter plano; ajustar seleção; exportar; voltar | estado do board promovido por UXA-100-A3 | validada localmente no pacote | efeitos financeiros entre ciclos e execução institucional não implementados | excedentes são tratados explicitamente antes da efetivação |
| GKR-SURF-ORG-304 | UXA-100/A2/A3 — board `uxa-100-organization-plans-payments-flow-board.svg` | 0.1.0 canônico | TRN-422 ou TRN-424 | compreender resultado, recuperar falha ou retornar | TRN-425; tentar novamente quando aplicável | plano resultante/anterior, capacidade, confirmação/recibo, direitos/dados preservados e estado de falha | confirmação real para ativar; falha preserva plano anterior identificável | nova tentativa consciente; retorno a Planos | estados de resultado promovidos por UXA-100-A3 | validada localmente no pacote | processamento financeiro e entitlement técnico não implementados | sucesso e falha compartilham família sem compartilhar consequência |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

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

## 5. Efeito da UXA-100-A4

A UXA-100-A4 reformula in-place `uxa-015-organization-overview-desktop.svg` e `uxa-100-organization-plans-screen-desktop.svg`, corrige o rótulo obsoleto `Guivos Business`, adiciona `TRN-427/428` e fecha a origem administrativa voluntária de Planos da Organização sem novo SVG ou superfície.

## 6. Estado

O detalhamento está `active` 0.5.0 como parte integrante do registro. A Jornada da Organização permanece incompleta e `draft`; validação documental não comprova implementação.