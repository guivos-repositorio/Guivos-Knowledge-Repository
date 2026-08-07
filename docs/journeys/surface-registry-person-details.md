---
id: GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
title: Detalhamento Obrigatório das Superfícies da Pessoa
status: active
version: 0.7.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
normative: false
---

# Detalhamento Obrigatório das Superfícies da Pessoa

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens por conta própria.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | UXA-022 | indeterminado | acesso público | iniciar ou continuar | entrada protegida | conteúdo institucional público | nenhum para leitura | retorno livre | nenhuma | parcial | integração ponta a ponta | entrada pública |
| GKR-SURF-PER-002 | UXA-034 | indeterminado | Home pública | prosseguir após orientação | escolha de modalidade | contexto mínimo | autenticação quando necessária | voltar/interromper | nenhuma | parcial | continuidade entre pacotes | entrada protegida |
| GKR-SURF-PER-003 | UXA-034 | indeterminado | entrada protegida | escolher texto ou voz | expressão guiada | modalidade escolhida | escolha explícita | trocar/voltar/cancelar | nenhuma | parcial | UXA-068 | escolha de modalidade |
| GKR-SURF-PER-004 | UXA-068 | indeterminado | escolha de modalidade | expressar/revisar/concluir | inventário | conteúdo de origem e derivados | solicitação consciente | editar/descartar/pausar | nenhuma | parcial | integração com inventário | expressão guiada |
| GKR-SURF-PER-005 | UXA-034 | indeterminado | expressão guiada | revisar e autorizar | processamento | conteúdos e finalidade | autorização específica | recusar/retirar/voltar | nenhuma | parcial | transição entre pacotes | inventário |
| GKR-SURF-PER-006 | UXA-036 | indeterminado | inventário autorizado | acompanhar processamento | compreensão | estado e fontes | autorização registrada | interromper/retornar | nenhuma | local | continuidade ponta a ponta | processamento |
| GKR-SURF-PER-007 | UXA-036 | indeterminado | processamento | revisar/corrigir/aceitar/rejeitar | persistência | síntese e fontes | revisão consciente | corrigir/rejeitar | nenhuma | parcial | ligação recorrente | compreensão inicial |
| GKR-SURF-PER-008 | UXA-006 | indeterminado | compreensão | escolher próximo passo | continuidades recorrentes | momento atual e oportunidades | permissões contextuais | revisar/ignorar | nenhuma | não examinado | reconciliação | Tela Hoje |
| GKR-SURF-PER-101 | UXA-060 | indeterminado | navegação recorrente | explorar/pesquisar | resultados | termos/filtros | nenhum vínculo | limpar/voltar | nenhuma | parcial | famílias | Coletivos |
| GKR-SURF-PER-102 | UXA-060 | indeterminado | Explorar | selecionar/refinar | Perfil Público | filtros/resultados | conteúdo público | voltar/refinar | nenhuma | parcial | descoberta → perfil | Coletivos |
| GKR-SURF-PER-103 | UXA-062 | indeterminado | busca | avaliar e solicitar | revisão | conteúdo público | autenticação ao solicitar | retornar/não prosseguir | nenhuma | parcial | participação | Perfil Público |
| GKR-SURF-PER-104 | UXA-064 | indeterminado | Perfil Público | revisar e confirmar | solicitação enviada | dados necessários | confirmação explícita | editar/cancelar | nenhuma | parcial | destino do responsável | solicitação |
| GKR-SURF-PER-105 | UXA-066; estado aprovado revalidado UXA-092 | indeterminado | solicitação/evento | acompanhar/responder/cancelar/compreender | decisão ou PER-106 | estado/prazo/pedidos/decisão | autoridade + ação consciente | cancelar/não prosseguir | UXA-091 substituída no aprovado por UXA-092 | validada no escopo vigente | outras continuidades separadas | Solicitação Pendente |
| GKR-SURF-PER-106 | UXA-091/092/094 — `uxa-091-my-collectives-mobile.svg` | 0.2.0 | vínculo confirmado ou acesso recorrente | reconhecer participações e, opcionalmente, abrir atualizações | `Ver atualizações` → PER-107; retornos existentes | Coletivo, estado, papel, mudança de vínculo, informação pública mínima e estados relacionados | autenticação/vínculo; abrir Central não altera vínculo nem leitura | trocar categoria, voltar ou não prosseguir | referência UXA-092 reformulada no gatilho por UXA-094 | validada; TRN-108 e TRN-110 integralmente validadas | P0B adicional separado | não é feed ou Central |
| GKR-SURF-PER-107 | UXA-093/094/095 — `uxa-093-collective-updates-center-mobile.svg` | 0.3.0 | PER-106 ou atualização legitimamente recebida | compreender mudança e escolher ação ou contexto interno | PER-105/PER-106 quando aplicável; `Abrir início do Coletivo` → PER-108 | origem, tipo, contexto, autoridade, fonte, data, leitura, ação, prazo, preferência e vínculo | vínculo/autorização pertinente; abrir PER-108 não altera leitura/vínculo/papel | retornar; ajustar preferência; não prosseguir | SVG UXA-094 reformulado por UXA-095 | **contrato previamente validado; SVG corrente pendente; TRN-111 parcial** | revalidação do SVG + handoff | triagem, não feed; nova entrada interna é neutra |
| GKR-SURF-PER-108 | UXA-095 — `uxa-095-collective-participant-home-mobile.svg` | 0.1.0 | vínculo existente e contexto selecionado em PER-107 | compreender propósito, vínculo, momento, atividade, consulta e escolhas internas | áreas próprias do Coletivo; retorno para Central | propósito, estado de participação, papel, momento, fonte, atividade, consulta, atalhos e controles de autonomia | vínculo válido e permissões contextuais; função/autoridade/presença nunca inferidas | voltar, não participar, pausar, sair, contestar ou ajustar notificações | referência histórica UXA-016 não promovida; nova referência UXA-095 | **materializada; TRN-111 parcial** | validação funcional e integrada | síntese interna, não feed nem réplica dos canais |
| GKR-SURF-PER-201 | UXA-024 | indeterminado | oportunidades | explorar/selecionar | lista/detalhe | consulta/localização/filtros | localização conforme escolha | voltar/limpar | nenhuma | parcial | publicação–descoberta | oportunidades |
| GKR-SURF-PER-202 | UXA-028 | indeterminado | mapa/lista | ordenar/filtrar/selecionar | detalhe | consulta/filtros/cartões | nenhum vínculo | voltar/limpar | nenhuma | parcial | mapa ↔ lista | oportunidades |
| GKR-SURF-PER-203 | UXA-007 | 0.4.0 | mapa/lista | avaliar/salvar/comparar/agir | ação/retorno/fronteira | condições/riscos/relação comercial | ação consciente | retornar/ocultar/contestar | nenhuma | parcial | efeito externo | oportunidades |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Efeito da UXA-095

A UXA-095 materializa `PER-108` e reforma minimamente o SVG corrente de `PER-107` para tornar `TRN-111` observável. A validação anterior de `PER-107` não é aplicada automaticamente à nova versão visual; `PER-108` também aguarda validação. `TRN-111` permanece parcial até exame integrado posterior.

## 5. Estado

O detalhamento está `active` como parte integrante do registro granular. O status não promove a Jornada da Pessoa como completa nem comprova implementação.
