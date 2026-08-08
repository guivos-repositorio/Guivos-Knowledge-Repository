---
id: GKR-JOURNEY-SURFACE-DETAIL-COMMERCIAL-001
title: Detalhamento Obrigatório da Camada Comercial e da Fronteira
status: active
version: 0.6.0
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
  - UXA-099
  - UXA-100
  - UXA-100-A3
  - UXA-101
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
normative: false
---

# Detalhamento Obrigatório da Camada Comercial e da Fronteira

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens por si só.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COM-001 | UXA-040 — `docs/experience-architecture/uxa-040-opportunity-boost-advertiser-flow-low-fidelity-wireframes.md` | indeterminado | intenção de promover | configurar, revisar, confirmar ou cancelar campanha | campanha configurada | objetivo, orçamento, público permitido, inventário e parâmetros comerciais | autoridade econômica e confirmação | editar, cancelar ou salvar antes da ativação | nenhuma identificada | parcial | integração econômica completa | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-002 | UXA-042 — `docs/experience-architecture/uxa-042-opportunity-boost-sponsored-card-and-explanation-low-fidelity-wireframes.md` | indeterminado | entrega identificada | abrir detalhe, pedir explicação, ocultar ou retornar | detalhe, explicação ou retorno orgânico | conteúdo patrocinado identificado, origem, relação comercial e controles | nenhuma legitimidade ou autoridade implícita | ignorar, ocultar, denunciar ou retornar ao contexto orgânico | nenhuma identificada | parcial | integração com superfícies orgânicas | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-003 | UXA-044 — `docs/experience-architecture/uxa-044-opportunity-boost-sponsored-list-and-map-low-fidelity-wireframes.md` | indeterminado | descoberta em lista ou mapa | selecionar unidade identificada ou continuar organicamente | cartão, detalhe ou explicação | unidades patrocinadas identificadas e conteúdo orgânico preservado | critérios comerciais e proteção; nenhuma compra de relevância | ignorar, voltar, ocultar ou seguir resultados orgânicos | nenhuma identificada | parcial | continuidade transversal | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-004 | UXA-046/053 — gestão ativa desktop/móvel | indeterminado | campanha ativa | ajustar, pausar, retomar ou encerrar campanha | ajuste, pausa ou encerramento | estado, orçamento, entrega agregada e parâmetros autorizados | autoridade econômica e confirmação conforme efeito | revisar, desfazer quando permitido, pausar ou encerrar | nenhuma identificada | parcial | integração com estados residuais | validações locais UXA-047/054; transições permanecem separadas |
| GKR-SURF-COM-005 | UXA-055 — `docs/experience-architecture/uxa-055-opportunity-boost-residual-states-low-fidelity-wireframes.md`; validação UXA-099 | 0.1.0 + validação 0.1.0 | erro, zero inventário, baixa oferta, falha de atualização ou controle da pessoa | continuar, revisar, tentar novamente, ocultar, reduzir, desativar, desfazer, denunciar ou contestar conforme o estado | continuidade específica sem efeito implícito | erro técnico, inventário, densidade, versão confirmada/candidata, preferências, denúncia e contestação | gates específicos validados pela UXA-099; mudança material não confirmada bloqueia entrega futura | retorno e reversão conforme escopo; escolhas independentes; repetição idempotente | materialização UXA-055 refinada pela validação UXA-099 | **superfície validada; TRN-305 permanece parcial** | integração ponta a ponta das transições | dez referências móveis funcionalmente validadas; oito sem alteração e duas reformuladas |
| GKR-SURF-BND-001 | UXA-004/007; validação UXA-101 — `docs/experience-architecture/uxa-101-conscious-external-boundary-validation.md` | validação 0.1.0 | estado de revisão em PER-203 | confirmar conscientemente saída para destino externo identificado ou permanecer no Detalhe | autoridade transferida ao destino externo após confirmação e revalidação | identificador do destino, finalidade, responsável e contexto mínimo; dados pessoais não acompanham por conveniência | ação afirmativa, destino ainda válido/autorizado e disclosure proporcional de dados/contexto | cancelar antes da saída; retornar à Guivos não presume conclusão externa | endpoint textual anterior consolidado pela UXA-101 | **fronteira examinada; TRN-205 integralmente validada até o limite de autoridade Guivos** | comportamento e resultado posteriores pertencem ao terceiro | endpoint documental; não é participante estrutural, tela Guivos nem implementação externa |
| GKR-SURF-BND-002 | UXA-100/A3 — handoff de contratação/dimensionamento assistido | 0.2.0 | COL-301 via TRN-416 ou ORG-301 via TRN-426 quando a contratação deixar de ser autonomamente configurável | solicitar análise, proposta, dimensionamento, configuração assistida ou contrato conforme necessidade | processo governado fora do autoatendimento | participante institucional, contexto de capacidade e dados mínimos necessários ao processo, conforme finalidade e autorização | ação afirmativa e autoridade institucional; nenhum checkout, plano específico ou capacidade infinita presumidos | voltar a Planos antes de compromisso; recusar proposta futura conforme processo | semântica Enterprise/Scale anterior substituída por autoridade genérica | **parcial** | processo posterior, proposta, contrato e handoffs operacionais não materializados | fronteira documental compartilhada e genérica; não é plano, produto, checkout ou tela autônoma; não pertence semanticamente a Enterprise/Scale |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Efeito da UXA-101

A UXA-101 examina `BND-001` e valida `TRN-205` **até a fronteira de autoridade da Guivos**. O estado de revisão permanece em `PER-203`; nenhum SVG é criado para a fronteira e nenhum resultado externo é presumido.

A Guivos deve interromper a saída quando o destino conhecido não puder ser revalidado e deve preservar retorno seguro ao Detalhe. Dados pessoais, inferências ou histórico de jornada não acompanham a transição sem finalidade e autorização adequadas.

## 5. Regra corrigida de BND-002

`BND-002` é a **fronteira de contratação/dimensionamento assistido**.

Pode ser utilizada quando um contexto exigir proposta, capacidade dimensionada, configuração assistida, análise específica ou contrato. O gatilho funcional é a necessidade de assistência, não o nome de um plano.

Consequentemente:

- `BND-002` não equivale a Enterprise;
- `BND-002` não equivale a Scale;
- `BND-002` não pertence exclusivamente a Coletivo ou Organização;
- `BND-002` não cria qualquer superfície de Guivos Business;
- `TRN-416` e `TRN-426` permanecem parciais e com os mesmos IDs.

## 6. Preservações

- `COM-005` permanece validado pela UXA-099 sem promover `TRN-305`;
- `BND-001` continua sendo fronteira externa, não tela Guivos;
- `BND-002` não define proposta, preço final, contrato, SLA ou capacidade real;
- `TRN-416` e `TRN-426` permanecem parciais;
- pagamento de plano e Opportunity Boost permanecem objetos econômicos separados;
- Organização e Guivos Business permanecem estruturas distintas.

## 7. Estado

O detalhamento está `active` como parte integrante do registro. O status aprova o instrumento documental e não altera automaticamente maturidade de jornadas, processo comercial ou implementação.