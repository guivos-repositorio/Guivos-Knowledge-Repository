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
| GKR-SURF-COM-005 | UXA-055; validação UXA-099 | 0.1.0 + validação 0.1.0 | erro, inventário, baixa oferta, falha de atualização ou controle da Pessoa | continuar, revisar, tentar novamente, ocultar, reduzir, desativar, desfazer, denunciar ou contestar conforme estado | continuidade específica sem efeito implícito | erro técnico, inventário, densidade, versão confirmada/candidata, preferências, denúncia e contestação | gates validados pela UXA-099 | retorno/reversão conforme escopo; repetição idempotente | materialização UXA-055 refinada pela UXA-099 | **superfície validada; TRN-305 parcial** | integração ponta a ponta | dez referências funcionalmente validadas |
| GKR-SURF-BND-001 | UXA-004/007; validação UXA-101 | validação 0.1.0 | estado de revisão em PER-203 | confirmar conscientemente saída externa ou permanecer no Detalhe | autoridade transferida ao destino externo após confirmação/revalidação | destino, finalidade, responsável e contexto mínimo | ação afirmativa, destino válido/autorizado e disclosure proporcional | cancelar antes da saída; retorno não presume conclusão externa | endpoint anterior consolidado pela UXA-101 | **fronteira examinada; TRN-205 validada até o limite Guivos** | comportamento posterior pertence ao terceiro | não é tela Guivos nem implementação externa |
| GKR-SURF-BND-002 | UXA-100/A3 — handoff de contratação/dimensionamento assistido | 0.2.0 | COL-301 via TRN-416 ou ORG-301 via TRN-426 quando a intenção não for autonomamente configurável | solicitar início de processo assistido de proposta, dimensionamento, configuração, análise ou contrato | processo comercial/contratual assistido fora do autoatendimento | participante institucional, necessidade/escopo, contexto de capacidade e dados mínimos necessários, conforme autorização futura | ação afirmativa e autoridade institucional; nenhum checkout, plano específico ou capacidade presumidos | voltar a Planos antes de compromisso; recusar proposta futura conforme processo | mesma fronteira BND-002 com semântica corrigida | **parcial** | processo posterior, proposta, contrato e handoffs operacionais não materializados | fronteira documental genérica; não significa Enterprise, Scale, Rede ou Transforma e não é tela de checkout |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo pode ser completado por inferência.

## 4. BND-002 — contrato semântico

`BND-002` existe para separar autoatendimento de contratação que exige assistência. A decisão de usá-lo depende da complexidade concreta da intenção, não do nome do plano.

Pode ser necessário, por exemplo, quando houver:

- dimensionamento de capacidade;
- proposta comercial;
- configuração específica;
- análise operacional/jurídica adicional;
- contrato;
- combinação de requisitos que não possa ser confirmada autonomamente.

A fronteira não atribui automaticamente preço, SLA, capacidade, entitlement ou plano.

## 5. Preservações

- `COM-005` permanece validado pela UXA-099 sem promover `TRN-305`;
- `BND-001` continua fronteira externa, não tela Guivos;
- `BND-002` mantém ID e maturidade `parcial`;
- `TRN-416` e `TRN-426` permanecem parciais;
- nenhum `SURF`, `TRN`, `BND` ou SVG é criado;
- nenhuma transição de Guivos Business é inferida;
- pagamento de plano e Opportunity Boost permanecem objetos separados.

## 6. Estado

O detalhamento permanece `active` como parte integrante do registro. O status aprova o instrumento documental e não altera automaticamente maturidade de jornadas, processo comercial ou implementação.
