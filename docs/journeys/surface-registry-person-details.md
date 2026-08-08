---
id: GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
title: Detalhamento Obrigatório das Superfícies da Pessoa
status: active
version: 0.11.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-090
  - UXA-097
  - UXA-098
  - UXA-100
  - UXA-100-A3
  - UXA-101
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
| GKR-SURF-PER-003 | UXA-034 | indeterminado | entrada protegida | escolher texto ou voz | expressão guiada | modalidade escolhida | escolha explícita | trocar/voltar/cancelar | nenhuma | parcial | continuidade entre pacotes | escolha de modalidade |
| GKR-SURF-PER-004 | UXA-068 | indeterminado | escolha de modalidade | expressar/revisar/concluir | inventário | conteúdo de origem e derivados | solicitação consciente | editar/descartar/pausar | nenhuma | parcial | integração com inventário | expressão guiada |
| GKR-SURF-PER-005 | UXA-034 | indeterminado | expressão guiada | revisar e autorizar | processamento | conteúdos e finalidade | autorização específica | recusar/retirar/voltar | nenhuma | parcial | transição entre pacotes | inventário |
| GKR-SURF-PER-006 | UXA-036 | indeterminado | inventário autorizado | acompanhar processamento | compreensão | estado e fontes | autorização registrada | interromper/retornar | nenhuma | local | continuidade ponta a ponta | processamento |
| GKR-SURF-PER-007 | UXA-036; variante revalidada UXA-097 | 0.3.0 | processamento/compreensão revisada | escolher persistência e personalização independentemente | `TRN-007` para Hoje ou rotas explícitas | síntese revisada, origens, escolhas e finalidades | escolhas compatíveis + confirmação explícita | voltar/revisar/excluir e explorar | decisão refinada UXA-097 | **TRN-007 integralmente validada** | demais handoffs pessoais anteriores | exclusão + exploração fora de TRN-007 |
| GKR-SURF-PER-008 | UXA-006 recorrente + UXA-097 primeira entrada | primeira variante 0.1.0 | compreensão confirmada via TRN-007 ou acesso recorrente | compreender o que importa e escolher se/quando agir | continuidades recorrentes | condição confirmada/autorizada/vigente | estado canônico; personalização não é gate | revisar/ignorar/navegar | primeira variante adicionada UXA-097 | **TRN-007 integralmente validada** | estados alternativos de Hoje | primeira entrada não presume avanço |
| GKR-SURF-PER-101 | UXA-060 | indeterminado | navegação recorrente | explorar/pesquisar | resultados | termos/filtros | nenhum vínculo | limpar/voltar | nenhuma | parcial | famílias | Coletivos |
| GKR-SURF-PER-102 | UXA-060 | indeterminado | Explorar | selecionar/refinar | Perfil Público | filtros/resultados | conteúdo público | voltar/refinar | nenhuma | parcial | descoberta → perfil | Coletivos |
| GKR-SURF-PER-103 | UXA-062 | indeterminado | busca | avaliar e solicitar | revisão | conteúdo público | autenticação ao solicitar | retornar/não prosseguir | nenhuma | parcial | participação | Perfil Público |
| GKR-SURF-PER-104 | UXA-064 | indeterminado | Perfil Público | revisar e confirmar | solicitação enviada | dados necessários | confirmação explícita | editar/cancelar | nenhuma | parcial | destino do responsável | solicitação |
| GKR-SURF-PER-105 | UXA-066; aprovado revalidado UXA-092 | indeterminado | solicitação/evento | acompanhar/responder/cancelar/compreender | decisão ou PER-106 | estado/prazo/pedidos/decisão | autoridade + ação consciente | cancelar/não prosseguir | UXA-092 no aprovado | validada no escopo vigente | outras continuidades | Solicitação Pendente |
| GKR-SURF-PER-106 | UXA-091/092/094 — `uxa-091-my-collectives-mobile.svg` | 0.2.0 | vínculo confirmado ou acesso recorrente | reconhecer participações e abrir atualizações opcionalmente | PER-107 | Coletivo, estado, papel e mudança de vínculo | autenticação/vínculo | trocar categoria/voltar | refinada UXA-094 | TRN-108/110 integrais | P0B separado | não é feed |
| GKR-SURF-PER-107 | UXA-093/094/095/096 — `uxa-093-collective-updates-center-mobile.svg` | 0.4.0 | PER-106 ou atualização legítima | compreender mudança e escolher ação/contexto | PER-105/PER-106/PER-108 | origem, tipo, autoridade, data, ação, prazo e vínculo | vínculo/autorização revalidados | retornar/ajustar preferência | revalidada UXA-096 | TRN-110/111 integrais | P0B separado | triagem, não feed |
| GKR-SURF-PER-108 | UXA-095/096 — `uxa-095-collective-participant-home-mobile.svg` | 0.2.0 | vínculo atual e contexto selecionado | compreender propósito/vínculo/momento e escolher área | áreas internas próprias; Central | propósito, vínculo, papel, momento e controles | vínculo/permissões revalidados | voltar/pausar/sair/contestar | revalidada UXA-096 | TRN-111 integral | P0B e áreas internas | síntese interna |
| GKR-SURF-PER-201 | UXA-024 | indeterminado | oportunidades | explorar/selecionar | lista/detalhe | consulta/localização/filtros | localização conforme escolha | voltar/limpar | nenhuma | TRN-203/204/210 integradas | integração patrocinada | oportunidades |
| GKR-SURF-PER-202 | UXA-028 | indeterminado | mapa/lista | ordenar/filtrar/selecionar | detalhe | consulta/filtros/cartões | nenhum vínculo | voltar/limpar | nenhuma | TRN-210/211 integradas | integração patrocinada | oportunidades |
| GKR-SURF-PER-203 | UXA-007/012/098/101 — `uxa-007-opportunity-detail-mobile.svg` | **0.5.0 no recorte UXA-101** | mapa/lista via TRN-204/211 | avaliar/salvar/comparar; ao agir, revisar conscientemente a saída externa | permanecer no Detalhe ou `TRN-205 → BND-001` | condições, responsável, relação comercial, destino externo e disclosure de dados/contexto | ação afirmativa + destino conhecido/autorizado revalidado; nenhuma conclusão externa presumida | voltar ao detalhe; bloquear saída inválida; retorno externo neutro | estado de revisão previsto pela UXA-007 materializado/revalidado pela UXA-101 | **TRN-205 integralmente validada até BND-001** | processo e resultado posteriores pertencem ao terceiro | revisão é estado de PER-203; BND-001 não é tela Guivos |
| GKR-SURF-PER-301 | UXA-100/A1/A2/A3 — `uxa-100-person-plans-screen-mobile.svg`; comparação; board | 0.1.0 canônico | acesso voluntário ou contextual legítimo | compreender plano atual/delta e manter ou escolher mudança | TRN-401/403 | Free/Plus/Pro, preços candidatos e capacidades | autenticação; alternativas gratuitas preservadas | permanecer/retornar | UXA-100-A3 | superfície validada; transições locais | origens genéricas sem IDs | comparação no mesmo PER-301 |
| GKR-SURF-PER-302 | UXA-100/A2/A3 — board | 0.1.0 canônico | TRN-401 | revisar contratação | TRN-402 ou retorno | plano alvo, preço, recorrência, pagador/beneficiário | ação afirmativa | voltar sem contratar | UXA-100-A3 | validada localmente | gateway/fiscal/proration | não é checkout implementado |
| GKR-SURF-PER-303 | UXA-100/A2/A3 — board | 0.1.0 canônico | TRN-403 | revisar downgrade/cancelamento | TRN-404 ou retorno | plano atual/futuro, perdas e data efetiva | titular autenticado | manter plano/exportar | UXA-100-A3 | validada localmente | proration/estorno | consequências explícitas |
| GKR-SURF-PER-304 | UXA-100/A2/A3 — board | 0.1.0 canônico | TRN-402/404 | compreender resultado e recuperar | TRN-405 | estado resultante, confirmação/falha | confirmação real para ativação | retornar/tentar novamente | UXA-100-A3 | validada localmente | processamento/persistência | falha preserva estado anterior |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Efeito da UXA-101

A UXA-101 não cria superfície nova. `PER-203` continua sendo a responsabilidade de compreender a oportunidade e decidir como prosseguir, agora com estado visual explícito de revisão antes de `BND-001`. O processo externo posterior continua fora da autoridade da Guivos.

## 5. Estado

O detalhamento está `active` como parte integrante do registro granular. O status não promove a Jornada da Pessoa como completa nem comprova implementação.