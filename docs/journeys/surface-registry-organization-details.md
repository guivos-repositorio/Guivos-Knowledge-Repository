---
id: GKR-JOURNEY-SURFACE-DETAIL-ORGANIZATION-001
title: Detalhamento Obrigatório das Superfícies da Organização
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-076
  - UXA-077
  - UXA-078
normative: false
---

# Detalhamento Obrigatório das Superfícies da Organização

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens, maturidade ou status.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-ORG-001 | UXA-015 — `docs/experience-architecture/uxa-015-organization-overview-low-fidelity-wireframe.md` | indeterminado | identidade e autoridade | consultar momento e escolher responsabilidade institucional | oportunidades, relações e resultados | identidade, unidade, autoridade, compromissos e evidências | representação institucional válida | retornar, revisar contexto ou escolher outra responsabilidade | nenhuma identificada | parcial | matriz institucional completa | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-002 | UXA-008 — `docs/experience-architecture/uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md` | indeterminado | autoridade institucional | criar, revisar, enviar ou cancelar cadastro | estado institucional de publicação | dados da oportunidade, responsável, disponibilidade, preço, elegibilidade, riscos e relação comercial | autoridade institucional; confirmação antes do envio | editar, salvar rascunho, cancelar ou retirar conforme estado | nenhuma identificada | parcial | integração com descoberta | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-003 | UXA-008 — `docs/experience-architecture/uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md` | indeterminado | cadastro revisado e aprovado | ativar, pausar, corrigir ou encerrar dentro do ciclo institucional | distribuição elegível em superfícies de oportunidades | estado institucional, disponibilidade, versão publicada e condições vigentes | autoridade institucional e aprovação aplicável | pausar, corrigir, retirar ou encerrar conforme ciclo | significado anterior dividido pela UXA-078; Detalhe de Oportunidade migra para GKR-SURF-PER-203 | parcial | integração publicação–descoberta | estado institucional protegido; não representa o detalhe percebido pela Pessoa |
| GKR-SURF-ORG-004 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | decisão institucional | formular, revisar, enviar ou retirar proposta | avaliação pelo Coletivo | finalidade, compromissos, recursos, dados, autonomia e saída | autoridade institucional | retirar, ajustar ou cancelar antes de aceite conforme contrato | nenhuma identificada | ausente | superfície bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-005 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | proposta | negociar, aprovar, recusar ou solicitar ajuste | aprovação, recusa ou ajuste | proposta, contraproposta, compromissos, recursos e limites | autoridades bilateralmente legítimas | recusar, ajustar, pausar negociação ou sair | nenhuma identificada | ausente | materialização bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-006 | ausente; autoridade: UXA-019 — `docs/experience-architecture/uxa-019-organization-collective-relationship-functional-contract.md` | indeterminado | aprovação bilateral | revisar e decidir continuidade da relação | renovação, ajuste, pausa ou encerramento | estado, compromissos, recursos, evidências e histórico | autoridade bilateral conforme efeito | renovar, ajustar, pausar, contestar ou encerrar | nenhuma identificada | ausente | operação bilateral | entrada documental seletiva; não declara jornada completa |
| GKR-SURF-ORG-007 | UXA-014 — `docs/experience-architecture/uxa-014-organizations-and-collectives-functional-foundation.md` | indeterminado | atividades e compromissos | indeterminado | revisão institucional | evidências e resultados dispersos; inventário ausente | indeterminado | indeterminado | nenhuma identificada | não examinado | matriz visual institucional | responsabilidade conhecida com evidência insuficiente para classificar |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Estado

O detalhamento permanece `draft` junto com o registro principal e aguarda revalidação funcional específica.
