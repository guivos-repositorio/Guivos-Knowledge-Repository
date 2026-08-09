---
id: GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
title: Detalhamento Obrigatório das Superfícies da Pessoa
status: active
version: 0.14.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-090
  - UXA-097
  - UXA-098
  - UXA-100
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
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
| GKR-SURF-PER-008 | UXA-006 recorrente + UXA-097 primeira entrada | primeira variante 0.1.0 | compreensão confirmada via TRN-007 ou acesso recorrente | compreender o que importa e escolher se/quando agir | continuidades recorrentes + `TRN-008/010/012` contratadas | condição confirmada/autorizada/vigente; sínteses sem exposição sensível indevida | estado canônico; personalização não é gate | revisar/ignorar/navegar; retornos `TRN-009/011/013` | primeira variante adicionada UXA-097 | **TRN-007 integralmente validada; TRN-008..013 contratadas** | estados alternativos de Hoje e validação dos handoffs especializados | primeira entrada não presume avanço; Hoje sintetiza e não absorve capacidades especializadas |
| GKR-SURF-PER-009 | sem SVG dedicado; autoridade UXA-100/A1/A4 | indeterminado | acesso autenticado à Conta/Configurações | escolher área administrativa e abrir Planos voluntariamente | `TRN-406` para PER-301 ou outras áreas ainda não governadas | somente contexto administrativo necessário; nenhum conteúdo adicional inferido | autenticação | permanecer/retornar; `TRN-407` | nenhuma | `TRN-406/407` contratadas | materialização própria de Conta | responsabilidade criada somente para origem/retorno de Planos; não define arquitetura total da Conta |
| GKR-SURF-PER-010 | GKR-UX-D5-C2-001 — `d5-c2-person-objectives-mobile.svg`; autoridade funcional PAS-001-OBJ-VIEW-001 | 0.1.0 materializado | `TRN-008` a partir de PER-008 | compreender, organizar e controlar objetivos sem julgamento ou mutação automática | `TRN-009` para PER-008; demais handoffs diretos não contratados | objetivos, estados, prioridades, critérios, marcos, progresso/evidências legítimas, conflitos, histórico, permissões e `0..n domain_link` | autenticação; autoridade da Pessoa; proteção proporcional a conteúdo sensível | retornar por `TRN-009`; revisar/pausar/retomar/retirar conforme contrato funcional | nenhuma | `TRN-008/009` contratadas | validação funcional pendente; handoffs diretos com PER-011/012 não definidos | Área da jornada ≠ dimensão estrutural do Contexto Vivo; domínio não cria Objetivo nem prioridade |
| GKR-SURF-PER-011 | GKR-UX-D5-C2-001 — `d5-c2-person-next-steps-mobile.svg`; autoridade funcional PAS-001-PP-VIEW-001 | 0.1.0 materializado | `TRN-010` a partir de PER-008 | compreender, organizar e controlar movimentos contextuais sem converter sugestão em execução | `TRN-011` para PER-008; demais handoffs diretos não contratados | passos, estados, prontidão, prioridade, dependências, bloqueios, responsabilidade, recorrência, resultados, histórico e `0..n domain_link` | autenticação; decisão consciente; minimização de conteúdo sensível | retornar por `TRN-011`; adiar/pausar/cancelar/substituir conforme contrato funcional | nenhuma | `TRN-010/011` contratadas | validação funcional pendente; handoffs diretos com PER-010/012 não definidos | Área da jornada é contexto semântico; não representa obrigação, urgência ou mérito |
| GKR-SURF-PER-012 | GKR-UX-D5-C2-001 — `d5-c2-person-evolution-mobile.svg`; autoridade funcional PAS-001-EC-VIEW-001 | 0.1.0 materializado | `TRN-012` a partir de PER-008 | compreender e controlar trajetórias, mudanças, continuidades e interpretações sem score humano | `TRN-013` para PER-008; demais handoffs diretos não contratados | trajetórias, períodos, baselines, direções, mudanças/estabilidade, observações, evidências, confiança, incerteza, contestações, histórico e `0..n domain_link` | autenticação; privacidade por padrão; distinção entre declarado/observado/inferido/confirmado | retornar por `TRN-013`; contestar/corrigir/pausar/revogar conforme contrato funcional | nenhuma | `TRN-012/013` contratadas | validação funcional e sensibilidade pendentes; sem roda da vida/score | Domínio de Evolução, dimensão do Contexto Vivo e aspecto descritivo da mudança permanecem separados |
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
| GKR-SURF-PER-301 | UXA-100/A1/A2/A3/A4 — `uxa-100-person-plans-screen-mobile.svg`; comparação; board | 0.1.0 canônico | `TRN-406` ou acesso contextual legítimo | compreender plano atual/delta e manter ou escolher mudança | TRN-401/403 ou `TRN-407` | Free/Plus/Pro, preços candidatos e capacidades | autenticação; alternativas gratuitas preservadas | permanecer/retornar | UXA-100-A3; origem formalizada UXA-100-A4 | superfície validada; TRN-401..405 locais; TRN-406/407 contratadas | PER-009 sem materialização; gateway/fiscal/proration | comparação no mesmo PER-301 |
| GKR-SURF-PER-302 | UXA-100/A2/A3 — board | 0.1.0 canônico | TRN-401 | revisar contratação | TRN-402 ou retorno | plano alvo, preço, recorrência, pagador/beneficiário | ação afirmativa | voltar sem contratar | UXA-100-A3 | validada localmente | gateway/fiscal/proration | não é checkout implementado |
| GKR-SURF-PER-303 | UXA-100/A2/A3 — board | 0.1.0 canônico | TRN-403 | revisar downgrade/cancelamento | TRN-404 ou retorno | plano atual/futuro, perdas e data efetiva | titular autenticado | manter plano/exportar | UXA-100-A3 | validada localmente | proration/estorno | consequências explícitas |
| GKR-SURF-PER-304 | UXA-100/A2/A3 — board | 0.1.0 canônico | TRN-402/404 | compreender resultado e recuperar | TRN-405 | estado resultante, confirmação/falha | confirmação real para ativação | retornar/tentar novamente | UXA-100-A3 | validada localmente | processamento/persistência | falha preserva estado anterior |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Efeito da UXA-100-A4

`PER-009` fecha a identidade documental da origem voluntária de Planos sem criar um SVG artificial de Conta. `TRN-406/407` permanecem contratadas até que haja materialização suficiente para validação ponta a ponta. Navegar para Planos não seleciona plano, não inicia cobrança e não amplia consentimento.

## 5. Efeito da D5-C1 e D5-C2

A D5-C1 contratou `PER-010`, `PER-011` e `PER-012` e seus seis handoffs mínimos com Hoje. A D5-C2 materializa um estado-base low-fidelity para cada responsabilidade sem promover qualquer uma para `validado`.

A presença dos três SVGs remove a lacuna de ausência visual, mas `TRN-008..013` continuam contratadas porque entrada, saída, payload, retorno, interrupção, concorrência, autorização e idempotência ainda não foram examinados ponta a ponta.

A separação entre Domínio de Evolução, dimensão estrutural do Contexto Vivo e aspecto descritivo da mudança permanece obrigatória na futura validação.

## 6. Efeito da UXA-101 preservado

A UXA-101 não cria superfície nova. `PER-203` continua sendo a responsabilidade de compreender a oportunidade e decidir como prosseguir, agora com estado visual explícito de revisão antes de `BND-001`. O processo externo posterior continua fora da autoridade da Guivos.

## 7. Estado

O detalhamento está `active` como parte integrante do registro granular. Materialização low-fidelity não promove a Jornada da Pessoa como completa nem comprova implementação.
