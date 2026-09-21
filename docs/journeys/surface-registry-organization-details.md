---
id: GKR-JOURNEY-SURFACE-DETAIL-ORGANIZATION-001
title: Detalhamento Obrigatório das Superfícies da Organização
status: active
version: 0.13.1
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - GKR-PLANS-ORGANIZATION-001
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

# Detalhamento Obrigatório das Superfícies da Organização

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens, maturidade ou status das entradas por conta própria.

A arquitetura da informação autenticada da Organização permanece definida por `GKR-UX-ORGCOL-AUTH-IA-001` em sua maturidade própria **authenticated_information_architecture_defined**. `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.0` define o mapa lógico-documental canônico de superfícies autenticadas e `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.0` define o mapa funcional de estados autenticados e `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0` define os Priority Flows como autoridades `ACTIVE / DEFINED / CANONICAL DOCUMENTARY`; a Navigation Materialization está definida canonicamente em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`; o wireframe principal autenticado low-fidelity da Organização foi entregue em `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` e validado com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`; high-fidelity Design está autorizado e não iniciado; protótipo e implementação permanecem não autorizados.

## 2. Campos por identificador

| ID | Autoridade corrente | Estado/versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-ORG-001 | GKR-UX-ORGCOL-AUTH-IA-001 + Surface Map + State Map + Priority Flows + Navigation Materialization + Low-Fidelity Delivery/Validation | low-fidelity vigente: DELIVERY v0.1.0 + VALIDATION v1.0.0 / PASS; IA autenticada definida em sua maturidade própria; Surface Map v1.1.0 e State Map v1.1.0 canônicos | identidade e autoridade | responsabilidade institucional deve respeitar a IA, o Surface Map e o State Map vigentes; composição high-fidelity final ainda não definida | contratos especializados podem partir/retornar ao contexto institucional quando sua própria autoridade os sustentar | identidade, unidade, autoridade, compromissos e evidências no limite dos fundamentos, da IA e dos mapas autenticados vigentes | representação institucional válida | retorno e revisão permanecem requisitos funcionais; materialização final pendente | produtores visuais históricos permanecem somente no Git e não são entrada atual | `TRN-427/428` preservam seu estado documental próprio, sem provar materialização vigente de ORG-001; TRN-201 preserva maturidade própria | **Priority Flows e Navigation Materialization definidos; low-fidelity entregue e validado; high-fidelity final e matriz visual permanecem sob Design** | Organização permanece participante; não é Guivos Business; Surface Map/State Map definidos ≠ wireframe vigente; contrato de navegação ≠ wireframe vigente |
| GKR-SURF-ORG-002 | UXA-004 + UXA-013 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | autoridade institucional | criar, revisar, enviar ou cancelar cadastro | estado institucional de publicação | dados da oportunidade, responsável, disponibilidade, preço, elegibilidade, riscos e relação comercial | autoridade institucional; confirmação antes do envio | editar, salvar rascunho, cancelar ou retirar conforme estado | nenhuma identificada | parcial | integração com descoberta | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-003 | UXA-004 + UXA-013 + UXA-098 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | cadastro revisado e aprovado | ativar, pausar, corrigir ou encerrar dentro do ciclo institucional | distribuição elegível em superfícies de oportunidades | estado institucional, disponibilidade, versão publicada e condições vigentes | autoridade institucional e aprovação aplicável | pausar, corrigir, retirar ou encerrar conforme ciclo | Detalhe de Oportunidade pertence a GKR-SURF-PER-203; histórico de decomposição permanece no Git | parcial | integração publicação–descoberta | estado institucional protegido; não representa o detalhe percebido pela Pessoa |
| GKR-SURF-ORG-004 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | decisão institucional | formular, revisar, enviar ou retirar proposta | avaliação pelo Coletivo | finalidade, compromissos, recursos, dados, autonomia e saída | autoridade institucional | retirar, ajustar ou cancelar antes de aceite conforme contrato | nenhuma identificada | ausente | superfície bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-005 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | proposta | negociar, aprovar, recusar ou solicitar ajuste | aprovação, recusa ou ajuste | proposta, contraproposta, compromissos, recursos e limites | autoridades bilateralmente legítimas | recusar, ajustar, pausar negociação ou sair | nenhuma identificada | ausente | materialização bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-006 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | aprovação bilateral | revisar e decidir continuidade da relação | renovação, ajuste, pausa ou encerramento | estado, compromissos, recursos, evidências e histórico | autoridade bilateral conforme efeito | renovar, ajustar, pausar, contestar ou encerrar | nenhuma identificada | ausente | operação bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-007 | UXA-014 — `docs/experience-architecture/uxa-014-organizations-and-collectives-functional-foundation.md` | indeterminado | atividades e compromissos | indeterminado | revisão institucional | evidências e resultados dispersos; inventário ausente | indeterminado | indeterminado | nenhuma identificada | não examinado | matriz visual institucional | responsabilidade conhecida com evidência insuficiente para classificar |
| GKR-SURF-ORG-301 | GKR-PLANS-ORGANIZATION-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado de Planos validado | capacidade legítima alcançada ou origem institucional contratada | compreender Conecta/Eleva/Transforma, uso e delta; manter, mudar ou solicitar dimensionamento assistido | TRN-421, TRN-423, TRN-426 ou retorno ao contexto institucional | plano atual, ciclo, oportunidades/programas, publicações ativas, admins, unidades, Coletivos relacionados, preços e benefícios incrementais | autoridade institucional válida; alternativas de arquivar/agendar/rascunho preservadas; ranking orgânico não muda | permanecer, arquivar, agendar, manter rascunho ou retornar | nenhuma supersessão do fluxo especializado; a origem histórica de ORG-001 não é baseline vigente | `TRN-427/428` preservam seu estado documental próprio; transições internas locais | contratação/dimensionamento após BND-002 e cobrança real; materialização vigente da origem institucional | comparação incremental e estado de capacidade pertencem à mesma família |
| GKR-SURF-ORG-302 | GKR-PLANS-ORGANIZATION-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-421 | revisar contratação de plano de Organização e confirmar ou voltar quando autonomamente configurável | TRN-422 ou retorno a ORG-301 | plano alvo, preço, periodicidade, recorrência, pagador/autoridade financeira, beneficiário institucional, início e método em simulação | autoridade financeira identificada; nenhuma pré-seleção; pagamento não amplia acesso à jornada pessoal de Pessoas | voltar/revisar sem contratar | estado funcional preservado no Registry | validada localmente no pacote | gateway, tributação e proration fora do escopo | revisão pré-contratual, não checkout implementado |
| GKR-SURF-ORG-303 | GKR-PLANS-ORGANIZATION-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-423 | revisar downgrade/cancelamento e selecionar explicitamente capacidades mantidas/encerradas | TRN-424 ou retorno a ORG-301 | unidades, administradores, publicações, Coletivos relacionados, integrações, dados a exportar, plano futuro e data efetiva | representante autorizado; nenhum dado/histórico é apagado para forçar retenção | manter plano; ajustar seleção; exportar; voltar | estado funcional preservado no Registry | validada localmente no pacote | efeitos financeiros entre ciclos e execução institucional não implementados | excedentes são tratados explicitamente antes da efetivação |
| GKR-SURF-ORG-304 | GKR-PLANS-ORGANIZATION-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-422 ou TRN-424 | compreender resultado, recuperar falha ou retornar | TRN-425; tentar novamente quando aplicável | plano resultante/anterior, capacidade, confirmação/recibo, direitos/dados preservados e estado de falha | confirmação real para ativar; falha preserva plano anterior identificável | nova tentativa consciente; retorno a Planos | estados de resultado preservados no Registry | validada localmente no pacote | processamento financeiro e entitlement técnico não implementados | sucesso e falha compartilham família sem compartilhar consequência |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

Materialização histórica preservada no Git não autoriza classificá-la como wireframe vigente nem como evidência de validação atual.

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

## 5. Entrada e retorno de Planos — contrato corrente

O contrato corrente de Planos, incluindo origem/retorno e separação entre Organização e Business, está preservado em `GKR-PLANS-ORGANIZATION-001`, no Surface Registry e no Transition Registry. Na leitura corrente:

```text
contrato de navegação de Planos
≠ wireframe principal autenticado vigente

PROVENIÊNCIA VISUAL HISTÓRICA
≠ baseline de produto
≠ UI definida
≠ validação vigente do wireframe principal
```

Qualquer continuidade visual high-fidelity da Visão Geral da Organização deverá partir dos fundamentos, Jobs/autoridades, da arquitetura da informação autenticada vigente, dos Surface Map e State Map canônicos, da Navigation Materialization e do pacote low-fidelity validado, e não da promoção automática de proveniência visual histórica.

## 6. Estado

O detalhamento está `active` 0.13.1 como parte integrante do registro. A Jornada da Organização está `active`. A arquitetura da informação autenticada preserva sua maturidade documental própria; `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.0`, `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.0` e `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0` permanecem autoridades canônicas. A Navigation Materialization está definida em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`; o wireframe autenticado low-fidelity da Organização foi entregue em `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` e validado com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. High-fidelity está **autorizado e ainda não iniciado**; protótipo interativo e implementação permanecem gates separados e não autorizados por essa decisão. Fluxos especializados preservam a maturidade sustentada por suas próprias autoridades.