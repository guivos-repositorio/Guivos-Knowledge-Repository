---
id: GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
title: Detalhamento Obrigatório das Superfícies da Pessoa
status: active
version: 0.23.2
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-090
  - UXA-097
  - UXA-098
  - GKR-PLANS-PERSON-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C4B-001
normative: false
---

# Detalhamento Obrigatório das Superfícies da Pessoa

> **Regra corrente de materialização.** Produtores low-fidelity removidos por F-016 não são entrada atual de Design/IA. O contrato funcional deve ser lido pelas autoridades e validações vigentes. Referências visuais especializadas ainda citadas em pacotes correntes não constituem UI final nem identidade visual.


## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não é um segundo inventário e não altera contagens por conta própria.

## 2. Campos por identificador

| ID | Autoridade corrente | Estado/versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | GKR-UX-HOME-MASTER-001 + UXA-020 | contrato funcional corrente | acesso público | iniciar ou continuar | entrada protegida | conteúdo institucional público | nenhum para leitura | retorno livre | nenhuma | parcial | integração ponta a ponta | entrada pública |
| GKR-SURF-PER-002 | GKR-UX-PER002-MAT-ELIGIBILITY-001 + protótipo corrente GKR-UX-PER002-PROTOTYPE-DELIVERY-001 | protótipo v1.0.0 / validação v2.0.0 PASS | Home pública | compreender o contexto protegido e decidir se prossegue | TRN-002 → PER-003 | finalidade, controles e contexto mínimo; conteúdo sintético no protótipo | autenticação quando necessária; processamento material exige autoridade própria | voltar/interromper/explorar sem personalização quando aplicável | aparência histórica não governa o estado corrente | protótipo interativo validado; TRN-002 permanece localmente validada | implementação técnica não comprovada | entrada protegida; uma responsabilidade com estados/variantes internos |
| GKR-SURF-PER-003 | UXA-020/023/035 + GKR-JOURNEY-PERSON-001 | contrato funcional corrente | entrada protegida | escolher texto ou voz | expressão guiada | modalidade escolhida | escolha explícita | trocar/voltar/cancelar | nenhuma | parcial | continuidade entre pacotes | escolha de modalidade |
| GKR-SURF-PER-004 | UXA-069 + GKR-JOURNEY-PERSON-001 | contrato funcional corrente | escolha de modalidade | expressar/revisar/concluir | inventário | conteúdo de origem e derivados | solicitação consciente | editar/descartar/pausar | nenhuma | parcial | integração com inventário | expressão guiada |
| GKR-SURF-PER-005 | UXA-023/035 + GKR-JOURNEY-PERSON-001 | contrato funcional corrente | expressão guiada | revisar e autorizar | processamento | conteúdos e finalidade | autorização específica | recusar/retirar/voltar | nenhuma | parcial | transição entre pacotes | inventário |
| GKR-SURF-PER-006 | UXA-023/037 + GKR-JOURNEY-PERSON-001 | contrato funcional corrente | inventário autorizado | acompanhar processamento | compreensão | estado e fontes | autorização registrada | interromper/retornar | nenhuma | local | continuidade ponta a ponta | processamento |
| GKR-SURF-PER-007 | UXA-023/037/097 + GKR-JOURNEY-PERSON-001 | contrato funcional corrente | processamento/compreensão revisada | escolher persistência e personalização independentemente | `TRN-007` para Hoje ou rotas explícitas | síntese revisada, origens, escolhas e finalidades | escolhas compatíveis + confirmação explícita | voltar/revisar/excluir e explorar | decisão refinada UXA-097 | **TRN-007 integralmente validada** | demais handoffs pessoais anteriores | exclusão + exploração fora de TRN-007 |
| GKR-SURF-PER-008 | UXA-097 primeira entrada + GKR-UX-D5-C1-001 / GKR-UX-D5-C4B-001 | estado recorrente governado pelo contrato corrente; primeira variante 0.1.0 | compreensão confirmada via TRN-007 ou acesso recorrente | compreender o que importa e escolher se/quando agir | continuidades recorrentes; `TRN-008/010/012` integrais quando affordance aplicável estiver presente | condição confirmada/autorizada/vigente; sínteses sem exposição sensível indevida; contexto mínimo de navegação | estado canônico; personalização não é gate; revalidação no destino | revisar/ignorar/navegar; retornos `TRN-009/011/013` integrais | primeira variante UXA-097; recorrente reformulada GKR-UX-D5-C1-001 / GKR-UX-D5-C4B-001 | **TRN-007 e TRN-008..013 integralmente validadas** | estados alternativos de Hoje permanecem separados | primeira entrada não presume avanço; Hoje sintetiza e não absorve capacidades especializadas |
| GKR-SURF-PER-009 | GKR-PLANS-PERSON-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | responsabilidade contratada sem materialização própria necessária | acesso autenticado à Conta/Configurações | escolher área administrativa e abrir Planos voluntariamente | `TRN-406` para PER-301 ou outras áreas ainda não governadas | somente contexto administrativo necessário; nenhum conteúdo adicional inferido | autenticação | permanecer/retornar; `TRN-407` | nenhuma | `TRN-406/407` contratadas | materialização própria de Conta | responsabilidade criada somente para origem/retorno de Planos; não define arquitetura total da Conta |
| GKR-SURF-PER-010 | GKR-UX-D5-C1-001 + PAS-001-OBJ-VIEW-001 | contrato funcional corrente | `TRN-008` integral a partir do Hoje recorrente | compreender, organizar e controlar objetivos sem julgamento ou mutação automática | `TRN-009` integral para PER-008; demais handoffs diretos não contratados | objetivos, estados, prioridades declaradas, critérios, marcos, progresso/evidências legítimas, conflitos, histórico, permissões e `0..n domain_link` | autenticação; autoridade da Pessoa; proteção proporcional a conteúdo sensível | retornar por `TRN-009`; revisar/pausar/retomar/retirar conforme contrato funcional | histórico visual preservado no Git | **TRN-008/009 integralmente validadas por GKR-UX-D5-C4B-001** | handoffs diretos com PER-011/012 não definidos | estado, prioridade e progresso permanecem separados; Área da jornada não cria Objetivo nem prioridade |
| GKR-SURF-PER-011 | GKR-UX-D5-C1-001 + PAS-001-PP-VIEW-001 | contrato funcional corrente | `TRN-010` integral a partir do Hoje recorrente | compreender, organizar e controlar movimentos contextuais sem converter sugestão em execução | `TRN-011` integral para PER-008; demais handoffs diretos não contratados | passos, estados, prontidão, prioridade, dependências, bloqueios, responsabilidade, recorrência, resultados, histórico e `0..n domain_link` | autenticação; decisão consciente; minimização de conteúdo sensível | retornar por `TRN-011`; adiar/pausar/cancelar/substituir conforme contrato funcional | histórico visual preservado no Git | **TRN-010/011 integralmente validadas por GKR-UX-D5-C4B-001** | handoffs diretos com PER-010/012 não definidos | proposta ≠ decisão; prontidão ≠ obrigação; Área da jornada não representa urgência ou mérito |
| GKR-SURF-PER-012 | GKR-UX-D5-C1-001 + PAS-001-EC-VIEW-001 | contrato funcional corrente | `TRN-012` integral a partir do Hoje recorrente | compreender e controlar trajetórias, mudanças, continuidades e interpretações sem score humano | `TRN-013` integral para PER-008; demais handoffs diretos não contratados | trajetórias, períodos, baselines, direções, observações, interpretações, evidências, confiança, incerteza, contestações, histórico e `0..n domain_link` | autenticação; privacidade por padrão; distinção entre declarado/observado/inferido/confirmado | retornar por `TRN-013`; contestar/corrigir/pausar/revogar conforme contrato funcional | histórico visual preservado no Git | **TRN-012/013 integralmente validadas por GKR-UX-D5-C4B-001** | estados sensíveis adicionais quando aplicáveis; handoffs diretos com PER-010/011 não definidos | interpretação inferida é explícita; Domínio de Evolução, dimensão do Contexto Vivo e aspecto descritivo permanecem separados |
| GKR-SURF-PER-101 | UXA-056 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | navegação recorrente | explorar/pesquisar | resultados | termos/filtros/origem | nenhum vínculo | limpar/voltar | produtores móveis absorvidos | parcial | famílias | descoberta de Coletivos independente de canal |
| GKR-SURF-PER-102 | UXA-056 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | Explorar | selecionar/refinar | Perfil Público | filtros/resultados/origem | conteúdo público | voltar/refinar | produtores móveis absorvidos | parcial | descoberta → perfil | contexto preservado |
| GKR-SURF-PER-103 | UXA-056 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | busca/origem legítima | avaliar e solicitar | revisão | identidade, propósito, funcionamento, condição de entrada | autenticação ao solicitar | retornar/não prosseguir | produtores móveis absorvidos | parcial | participação | Perfil Público não cria vínculo |
| GKR-SURF-PER-104 | UXA-056 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | Perfil Público | revisar e confirmar | solicitação enviada ou entrada conforme regra | dados necessários, regras e consequências | confirmação explícita | editar/cancelar | produtores móveis absorvidos | parcial | destino do responsável | revisão consciente precede efeito |
| GKR-SURF-PER-105 | UXA-056 + UXA-090/092 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | solicitação/evento | acompanhar/responder/cancelar/compreender | decisão ou PER-106 | estado/prazo/pedidos/decisão | autoridade + ação consciente | cancelar/não prosseguir | produtores móveis absorvidos; UXA-092 refina aprovado | validada no escopo vigente | handoffs 105..109 integrais | consultar não altera fila ou prioridade |
| GKR-SURF-PER-106 | UXA-092/094 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | vínculo confirmado ou acesso recorrente | reconhecer participações e abrir atualizações opcionalmente | PER-107 | Coletivo, estado, papel e mudança de vínculo | autenticação/vínculo | trocar categoria/voltar | refinada UXA-094 | TRN-108/110 integrais | P0B separado | não é feed |
| GKR-SURF-PER-107 | UXA-094/096 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | PER-106 ou atualização legítima | compreender mudança e escolher ação/contexto | PER-105/PER-106/PER-108 | origem, tipo, autoridade, data, ação, prazo e vínculo | vínculo/autorização revalidados | retornar/ajustar preferência | revalidada UXA-096 | TRN-110/111 integrais | P0B separado | triagem, não feed |
| GKR-SURF-PER-108 | UXA-096 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | vínculo atual e contexto selecionado | compreender propósito/vínculo/momento e escolher área | áreas internas próprias; Central | propósito, vínculo, papel, momento e controles | vínculo/permissões revalidados | voltar/pausar/sair/contestar | revalidada UXA-096 | TRN-111 integral | P0B e áreas internas | síntese interna |
| GKR-SURF-PER-201 | UXA-004/025/098 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | oportunidades | explorar/selecionar; alternar Mapa ↔ Lista sem perder a consulta | lista/detalhe | região, consulta, busca, filtros e seleção; localização somente quando autorizada | localização opcional; região manual permitida | voltar/limpar/editar região; desativar localização | estados especializados absorvidos no contrato corrente | TRN-203/204/210 integradas | integração patrocinada | Mapa e Lista preservam a mesma consulta territorial |
| GKR-SURF-PER-202 | UXA-029/098 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | PER-201 / modo Lista | ordenar/filtrar/selecionar mantendo a mesma consulta territorial | detalhe ou retorno ao Mapa | região, busca, filtros, ordenação, cartões e seleção | nenhum vínculo; localização não é requisito | Mapa ↔ Lista preserva contexto; voltar/limpar | wireframe histórico sem baseline visual corrente | TRN-210/211 integradas | integração patrocinada | Lista é modo textual integral da mesma descoberta territorial |
| GKR-SURF-PER-203 | UXA-004/012/098/101 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | contrato funcional corrente | mapa/lista via TRN-204/211 | avaliar/salvar/comparar; ao agir, revisar conscientemente a saída externa | permanecer no Detalhe ou `TRN-205 → BND-001` | condições, responsável, relação comercial, destino externo e disclosure de dados/contexto | ação afirmativa + destino conhecido/autorizado revalidado; nenhuma conclusão externa presumida | voltar ao detalhe; bloquear saída inválida; retorno externo neutro | estado de revisão consolidado e validado pela UXA-101 | **TRN-205 integralmente validada até BND-001** | processo e resultado posteriores pertencem ao terceiro | revisão é estado de PER-203; BND-001 não é tela Guivos |
| GKR-SURF-PER-301 | GKR-PLANS-PERSON-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado de Planos validado | `TRN-406` ou acesso contextual legítimo | compreender plano atual/delta e manter ou escolher mudança | TRN-401/403 ou `TRN-407` | Free/Plus/Pro, preços candidatos e capacidades | autenticação; alternativas gratuitas preservadas | permanecer/retornar | contrato corrente preservado no Surface/Transition Registry | superfície validada; TRN-401..405 locais; TRN-406/407 contratadas | PER-009 sem materialização; gateway/fiscal/proration | comparação no mesmo PER-301 |
| GKR-SURF-PER-302 | GKR-PLANS-PERSON-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-401 | revisar contratação | TRN-402 ou retorno | plano alvo, preço, recorrência, pagador/beneficiário | ação afirmativa | voltar sem contratar | contrato corrente preservado no Registry | validada localmente | gateway/fiscal/proration | não é checkout implementado |
| GKR-SURF-PER-303 | GKR-PLANS-PERSON-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-403 | revisar downgrade/cancelamento | TRN-404 ou retorno | plano atual/futuro, perdas e data efetiva | titular autenticado | manter plano/exportar | contrato corrente preservado no Registry | validada localmente | proration/estorno | consequências explícitas |
| GKR-SURF-PER-304 | GKR-PLANS-PERSON-001 + GEM-004-PLAN-TAXONOMY-AUTHORITY-001 + GKR-JOURNEY-TRANSITION-REGISTRY-001 | fluxo especializado validado localmente | TRN-402/404 | compreender resultado e recuperar | TRN-405 | estado resultante, confirmação/falha | confirmação real para ativação | retornar/tentar novamente | contrato corrente preservado no Registry | validada localmente | processamento/persistência | falha preserva estado anterior |

## 3. Regra de incerteza

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`. Nenhum campo poderá ser completado por inferência.

## 4. Entrada e retorno de Planos — contrato corrente

`PER-009` preserva a identidade documental da origem voluntária de Planos sem criar uma materialização artificial de Conta. `TRN-406/407` permanecem contratadas no `GKR-JOURNEY-TRANSITION-REGISTRY-001` até que haja evidência suficiente para validação ponta a ponta. Navegar para Planos não seleciona plano, não inicia cobrança e não amplia consentimento.

## 5. Direção, Movimento e Evolução

`GKR-UX-D5-C1-001` governa o contrato funcional corrente de `PER-010..012`. `GKR-UX-D5-C4B-001` registra a validação integrada corrente de `TRN-008..013`.

Os antigos degraus de materialização low-fidelity e reformulação visual pertencem à proveniência do Git e não são necessários para consumir a verdade corrente.

## 6. Efeito da UXA-101 preservado

A UXA-101 não cria superfície nova. `PER-203` continua sendo a responsabilidade de compreender a oportunidade e decidir como prosseguir, agora com estado funcional explícito de revisão antes de `BND-001`. O processo externo posterior continua fora da autoridade da Guivos.

## 7. Mapa e Lista — estados operacionais correntes

`PER-201` e `PER-202` compartilham uma única continuidade de descoberta territorial. Mapa e Lista são modos da mesma consulta; alternar entre eles não cria nova jornada, nova oportunidade ou nova autorização.

Regras correntes:

- localização do dispositivo é opcional;
- com localização desativada, a Guivos não presume posição, residência, deslocamento ou marcador pessoal;
- a Pessoa pode informar região manualmente sem transformar essa escolha em residência, posição atual ou histórico territorial;
- rota, quando aplicável, pode solicitar origem manual ou localização temporária autorizada; isso não autoriza retenção ou rastreamento contínuo;
- ausência de resultados é estado válido, recuperável e não equivale a ausência de possibilidades para a Pessoa;
- no estado sem resultados, consulta, região, busca e filtros devem permanecer compreensíveis e revisáveis; cobertura/atualização deve ser explicitada quando houver evidência;
- ações de recuperação podem editar região, busca ou filtros, com revisão antes de aplicar mudanças; desfazer só existe quando houver alteração reversível concreta;
- composição para computador ou móvel pertence ao Design e não cria superfície canônica distinta;
- não existe baseline visual corrente obrigatório para Mapa ou Lista.

Os antigos produtores especializados de localização desativada, estado sem resultados e referência desktop tiveram sua função corrente absorvida por este contrato, pelo Surface Registry e pelas transições vigentes. Sua proveniência permanece no Git e não é entrada padrão de Design ou IA.

## 8. Estado

O detalhamento está `active` como parte integrante do registro granular. A GKR-UX-D5-C4B-001 valida a continuidade especializada com Hoje no limite documental, sem promover a Jornada da Pessoa como completa e sem comprovar implementação técnica.