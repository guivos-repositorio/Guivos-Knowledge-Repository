---
id: GKR-JOURNEY-SURFACE-DETAIL-COMMERCIAL-001
title: Detalhamento Obrigatório da Camada Comercial e da Fronteira
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
normative: false
---

# Detalhamento Obrigatório da Camada Comercial e da Fronteira

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens, maturidade ou status das entradas.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COM-001 | UXA-040 — `docs/experience-architecture/uxa-040-opportunity-boost-advertiser-flow-low-fidelity-wireframes.md` | indeterminado | intenção de promover | configurar, revisar, confirmar ou cancelar campanha | campanha configurada | objetivo, orçamento, público permitido, inventário e parâmetros comerciais | autoridade econômica e confirmação | editar, cancelar ou salvar antes da ativação | nenhuma identificada | parcial | integração econômica completa | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-002 | UXA-042 — `docs/experience-architecture/uxa-042-opportunity-boost-sponsored-card-and-explanation-low-fidelity-wireframes.md` | indeterminado | entrega identificada | abrir detalhe, pedir explicação, ocultar ou retornar | detalhe, explicação ou retorno orgânico | conteúdo patrocinado identificado, origem, relação comercial e controles | nenhuma legitimidade ou autoridade implícita | ignorar, ocultar, denunciar ou retornar ao contexto orgânico | nenhuma identificada | parcial | integração com superfícies orgânicas | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-003 | UXA-044 — `docs/experience-architecture/uxa-044-opportunity-boost-sponsored-list-and-map-low-fidelity-wireframes.md` | indeterminado | descoberta em lista ou mapa | selecionar unidade identificada ou continuar organicamente | cartão, detalhe ou explicação | unidades patrocinadas identificadas e conteúdo orgânico preservado | critérios comerciais e proteção; nenhuma compra de relevância | ignorar, voltar, ocultar ou seguir resultados orgânicos | nenhuma identificada | parcial | continuidade transversal | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-004 | UXA-046 — `docs/experience-architecture/uxa-046-opportunity-boost-active-campaign-management-low-fidelity-wireframes.md` | indeterminado | campanha ativa | ajustar, pausar, retomar ou encerrar campanha | ajuste, pausa ou encerramento | estado, orçamento, entrega agregada e parâmetros autorizados | autoridade econômica e confirmação conforme efeito | revisar, desfazer quando permitido, pausar ou encerrar | nenhuma identificada | parcial | validação residual | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-COM-005 | UXA-055 — `docs/experience-architecture/uxa-055-opportunity-boost-residual-states-low-fidelity-wireframes.md` | 0.1.0 | estados anteriores | decisão varia por estado residual e permanece não validada como conjunto | continuidades específicas | erro técnico, inventário, densidade, preferências, ocultação, denúncia e contestação | gates específicos ainda aguardam validação funcional | retorno, desfazer ou continuidade dependem do estado; não examinados | referência incorreta UXA-047 a UXA-054 corrigida pela UXA-078 | não examinado | validação dos estados residuais | dez referências móveis materializadas pela UXA-055; validação funcional permanece ausente |
| GKR-SURF-BND-001 | fronteira documental governada por UXA-004 — `docs/experience-architecture/uxa-004-opportunities-organizations-collectives-map.md`; UXA-007 — `docs/experience-architecture/uxa-007-opportunity-detail-low-fidelity-wireframe.md` | indeterminado | Detalhe de Oportunidade | prosseguir para destino externo conscientemente identificado | destino externo apresentado | identificador do destino, finalidade, responsável e contexto mínimo quando disponível | ação consciente; requisitos externos permanecem fora do GKR | retorno quando tecnicamente possível; efeito externo não presumido | substitui o endpoint em texto livre de GKR-TRN-205 | não examinado | efeito externo não validado | endpoint documental; não é participante estrutural, tela Guivos ou implementação externa |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Estado

O detalhamento está `active` como parte integrante do registro promovido pela UXA-080. O status aprova o instrumento documental e não altera maturidade, continuidade ou lacuna de qualquer entrada.
