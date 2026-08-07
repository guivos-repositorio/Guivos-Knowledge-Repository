---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.10.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.10.0 preserva as 37 transições e as seis validações integrais já vigentes no fluxo de solicitação. A UXA-093 materializa o destino de `GKR-TRN-110`, mas a ligação permanece `parcial` porque ainda não foi validada ponta a ponta. `GKR-TRN-111` permanece `ausente` porque `PER-108` continua sem materialização vigente.

Permanecem vigentes as correções estruturais anteriores:

- todos os endpoints resolvem para IDs registrados;
- oportunidades utilizam superfícies próprias de mapa, lista e detalhe;
- o estado institucional de publicação permanece separado da experiência da Pessoa;
- a fronteira externa recebe endpoint documental controlado;
- o retorno do Opportunity Boost é dividido entre mapa e lista orgânicos;
- os dez estados residuais apontam para UXA-055.

O status `active` aprova o registro como instrumento documental. Nenhuma linha executa lógica de negócio ou cria ligação implementada.

## 2. Convenções de estado

| Estado | Significado |
|---|---|
| integralmente validada | origem, destino, autoridade, dados, efeito, retorno, interrupção e concorrência foram examinados como uma única ligação ponta a ponta no escopo documental |
| localmente validada | examinada dentro do pacote indicado, sem comprovação ponta a ponta |
| parcial | origem, destino ou efeito possuem cobertura incompleta ou a ligação ainda não foi validada como conjunto |
| contratada | autoridade define a ligação, mas não há materialização suficiente |
| ausente | ligação necessária conhecida sem materialização suficiente |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

Endpoints materializados ou mesmo validados como superfícies não tornam automaticamente a transição validada. A classificação `integralmente validada` também não comprova implementação técnica.

## 3. Contagem

| Família | Quantidade |
|---|---:|
| jornada pessoal | 7 |
| Pessoa em Coletivos e operação do responsável | 13 |
| Organização, oportunidades e relações bilaterais | 11 |
| Opportunity Boost | 6 |
| **Total** | **37** |

A UXA-093 não cria transições novas.

## 4. Jornada pessoal

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-001 | GKR-SURF-PER-001 | GKR-SURF-PER-002 | visitante → Pessoa | direta; protegida | escolher iniciar jornada | UXA-020 | muda de conteúdo público para entrada protegida; nenhum dado sensível presumido | entrada consciente | retorno à Home; imediata | UXA-021; UXA-035 | parcial | continuidade entre pacotes |
| GKR-TRN-002 | GKR-SURF-PER-002 | GKR-SURF-PER-003 | Pessoa | direta; protegida | concluir orientação e escolher modalidade | UXA-020; UXA-023 | registra somente a escolha apresentada | autenticação quando necessária | retorno permitido; imediata | UXA-034; UXA-035 | localmente validada | integração com expressão guiada |
| GKR-TRN-003 | GKR-SURF-PER-003 | GKR-SURF-PER-004 | Pessoa | condicional; reversível | escolher texto ou voz | UXA-068 | abre modalidade escolhida; conteúdo ainda é rascunho | escolha explícita | troca ou cancelamento; imediata | UXA-069 | parcial | ligação UXA-034 → UXA-068 |
| GKR-TRN-004 | GKR-SURF-PER-004 | GKR-SURF-PER-005 | Pessoa | protegida; reversível | concluir expressão e avançar para inventário | UXA-023; UXA-068 | conteúdo de origem e derivados identificados seguem para revisão | revisão consciente; sem análise implícita | editar, descartar ou voltar; imediata | UXA-035; UXA-069 | parcial | integração expressão–inventário |
| GKR-TRN-005 | GKR-SURF-PER-005 | GKR-SURF-PER-006 | Pessoa | protegida; condicional | autorizar finalidade específica | UXA-023 | somente conteúdos autorizados entram em processamento | autorização específica | recusar ou retirar antes do processamento; imediata | UXA-035; UXA-037 | parcial | continuidade entre materializações |
| GKR-TRN-006 | GKR-SURF-PER-006 | GKR-SURF-PER-007 | Pessoa | direta; protegida | processamento concluído | UXA-023 | apresenta compreensão inicial revisável, mantendo fontes separadas | processamento previamente autorizado | interrupção e retorno conforme pacote; assíncrona ou imediata conforme estado | UXA-037 | localmente validada | continuidade ponta a ponta |
| GKR-TRN-007 | GKR-SURF-PER-007 | GKR-SURF-PER-008 | Pessoa autenticada | condicional; protegida | revisar compreensão e decidir persistência ou personalização | UXA-002; UXA-023 | somente conteúdos e permissões aceitos podem sustentar continuidade | revisão e gates próprios | recusar persistência; tempo não consolidado | UXA-010; UXA-037 | não examinada | reconciliação com Tela Hoje |

## 5. Pessoa em Coletivos e operação do responsável

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-101 | GKR-SURF-PER-101 | GKR-SURF-PER-102 | visitante | direta; condicional | pesquisar ou aplicar filtro | UXA-056 | critérios produzem resultados de Coletivos; consulta não cria vínculo | nenhum vínculo | limpar filtros ou voltar; imediata | UXA-061 | localmente validada | continuidade entre famílias |
| GKR-TRN-102 | GKR-SURF-PER-102 | GKR-SURF-PER-103 | visitante | direta | selecionar Coletivo | UXA-056 | abre informações públicas do Coletivo | conteúdo público | retorno aos resultados; imediata | UXA-061; UXA-063 | parcial | ligação entre pacotes |
| GKR-TRN-103 | GKR-SURF-PER-103 | GKR-SURF-PER-104 | solicitante potencial | protegida; condicional | escolher solicitar participação | UXA-056 | inicia revisão consciente; nenhuma aprovação presumida | autenticação e elegibilidade quando aplicáveis | cancelar e retornar; imediata | UXA-063; UXA-065 | parcial | handoff para solicitação |
| GKR-TRN-104 | GKR-SURF-PER-104 | GKR-SURF-PER-105 | solicitante | protegida; assíncrona; handoff de autoridade | confirmar envio | UXA-056 | dados autorizados da solicitação seguem ao Coletivo; estado torna-se pendente | confirmação explícita | cancelar conforme estado; aguarda decisão | UXA-065; UXA-067 | parcial | continuidade posterior possui endpoints materializados, mas não validação integrada |
| GKR-TRN-105 | GKR-SURF-PER-105 | GKR-SURF-COL-003 | solicitante → responsável | entre participantes; handoff de autoridade; assíncrona | solicitação disponível para análise | UXA-056; UXA-059 | transfere próxima decisão ao responsável; preserva identificador lógico; dados limitados à finalidade | autoridade vigente do responsável; estado revalidado antes de efeito | solicitante pode cancelar; cancelamento ou expiração superveniente torna análise obsoleta; repetição não duplica efeito | UXA-067; UXA-089; UXA-090 | integralmente validada | — |
| GKR-TRN-106 | GKR-SURF-COL-003 | GKR-SURF-PER-105 | responsável → solicitante | entre participantes; assíncrona; reversível | pedir informação adicional | UXA-056; UXA-066; UXA-067; UXA-088; UXA-089 | pergunta, finalidade, autoridade e referência temporal chegam à mesma solicitação; aprovação não ocorre; acessibilidade não é critério oculto | autoridade vigente e finalidade limitada; solicitação ainda aberta | Pessoa responde, prefere não informar, contesta ou cancela; pedido sobre estado encerrado não prevalece; repetição não cria novo pedido lógico | UXA-067; UXA-089; UXA-090 | integralmente validada | — |
| GKR-TRN-107 | GKR-SURF-PER-105 | GKR-SURF-COL-003 | solicitante → responsável | entre participantes; assíncrona | enviar resposta adicional | UXA-056; UXA-067; UXA-088; UXA-089 | somente conteúdo conscientemente enviado retorna à mesma pergunta e finalidade; não cria vínculo | resposta consciente; estado ainda elegível para recebimento | editar antes do envio, descartar rascunho ou desistir; processo encerrado não reabre silenciosamente; repetição não duplica conteúdo lógico | UXA-067; UXA-089; UXA-090 | integralmente validada | — |
| GKR-TRN-108 | GKR-SURF-COL-003 | GKR-SURF-PER-106 | responsável → participante | handoff de autoridade; entre participantes; continuidade mediada por resultado | aprovar solicitação, formar vínculo, apresentar resultado em PER-105 e permitir continuidade opcional para Meus Coletivos | UXA-014; UXA-056; UXA-088; UXA-089; UXA-091; UXA-092 | cria um único vínculo conforme papel aceito; o resultado aprovado em PER-105 declara o vínculo já formado; `Ver em Meus Coletivos` apenas navega; PER-106 exibe o mesmo vínculo sem função, moderação, reputação ou notificação automática | decisão autorizada, estado vigente e resultado revalidado; o clique posterior não é gate do vínculo | abandonar decisão antes da confirmação; após o resultado, escolher `Agora não` interrompe apenas navegação; repetição não duplica vínculo | UXA-089 na origem; UXA-092 no resultado, destino e continuidade; contrato transversal UXA-090 | integralmente validada | — |
| GKR-TRN-109 | GKR-SURF-COL-003 | GKR-SURF-PER-105 | responsável → solicitante | entre participantes; assíncrona | recusar solicitação; expiração permanece evento temporal distinto | UXA-056; UXA-067; UXA-088; UXA-089 | apresenta recusa proporcional baseada em condição previamente apresentada na mesma solicitação, distinta de cancelamento, sanção, reputação ou expiração | autoridade vigente, fundamento proporcional e confirmação consciente; estado revalidado | voltar sem decidir antes da confirmação; cancelamento/expiração já vigentes não são sobrescritos; repetição não cria segunda recusa lógica | UXA-067; UXA-089; UXA-090 | integralmente validada | — |
| GKR-TRN-110 | GKR-SURF-PER-106 | GKR-SURF-PER-107 | participante | direta; controle de atenção | acessar atualizações relacionadas aos vínculos | UXA-056; UXA-058; UXA-059 | origem validada organiza vínculos; destino materializado por UXA-093 apresenta origem, natureza, autoridade, leitura, ação e prazo sem transformar a experiência em feed | vínculo ou autorização pertinente ao objeto; ambos os endpoints existem, mas o handoff ainda não foi validado como conjunto | permanecer/retornar a Meus Coletivos; leitura não conclui ação substantiva; concorrência e idempotência ainda exigem validação | UXA-092 na origem; UXA-093 no destino | parcial | validar gatilho, contexto, retorno, concorrência, leitura versus ação e efeito ponta a ponta |
| GKR-TRN-111 | GKR-SURF-PER-107 | GKR-SURF-PER-108 | participante | direta; condicional | selecionar Coletivo ou atualização que exija contexto interno | UXA-058; UXA-059 | origem materializada não cria por si só o Início do Participante | vínculo e papel; PER-108 ainda não vigente | retorno às atualizações; nenhum destino é afirmado como disponível | UXA-093 apenas na origem | ausente | Início do Participante em reformulação e sem materialização vigente |
| GKR-TRN-112 | GKR-SURF-COL-002 | GKR-SURF-COL-003 | responsável | direta; protegida | acessar solicitações a partir da visão geral | UXA-059; UXA-086; UXA-087; UXA-088; UXA-089 | abre a fila especializada preservando Coletivo representado e escopo concedido; nenhuma decisão é implícita | representação válida e escopo vigente | permanecer ou retornar à visão geral; falta de autoridade bloqueia operação; navegação não altera fila ou estado | UXA-087; UXA-089; UXA-090 | integralmente validada | — |
| GKR-TRN-113 | GKR-SURF-COL-004 | GKR-SURF-COL-005 | responsável | condicional; protegida | comunicar a participantes autorizados | UXA-058; UXA-059 | distribui comunicação oficial com finalidade identificada | papel e escopo de audiência | corrigir ou encerrar conforme regras futuras | — | contratada | operação interna não materializada |

## 6. Organização, oportunidades e relações bilaterais

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-201 | GKR-SURF-ORG-001 | GKR-SURF-ORG-002 | representante institucional | protegida; direta | escolher cadastrar oportunidade | UXA-004; UXA-014 | inicia cadastro dentro da unidade e papel apresentados | autoridade institucional | cancelar e retornar | UXA-013 | parcial | ligação com visão institucional |
| GKR-TRN-202 | GKR-SURF-ORG-002 | GKR-SURF-ORG-003 | representante institucional | protegida; condicional | revisar, enviar e obter aprovação para ativação | UXA-004 | move o cadastro ao estado institucional elegível ou ativo sem representar a tela da Pessoa | confirmação, autoridade e avaliação aplicável | editar, retirar, pausar ou encerrar conforme estado | UXA-013 | localmente validada | distribuição entre superfícies |
| GKR-TRN-203 | GKR-SURF-ORG-003 | GKR-SURF-PER-201 | Organização → Pessoa ou visitante | entre participantes; assíncrona; condicional | oportunidade ativa torna-se elegível para descoberta no mapa | UXA-004 | metadados públicos e condições vigentes podem ser apresentados no Mapa de Oportunidades | publicação válida; visibilidade e elegibilidade aplicáveis | Organização pode pausar, corrigir ou retirar; tempo não consolidado | UXA-013; UXA-025 em pacotes distintos | não examinada | integração publicação–descoberta |
| GKR-TRN-204 | GKR-SURF-PER-201 | GKR-SURF-PER-203 | Pessoa ou visitante | direta; reversível | selecionar oportunidade no mapa | UXA-004; UXA-007 | abre Detalhe de Oportunidade identificado; não cria vínculo ou transação | conteúdo público; gates posteriores conforme ação | retorno ao mapa; imediata | UXA-025; UXA-012 em pacotes distintos | parcial | efeito externo posterior |
| GKR-TRN-205 | GKR-SURF-PER-203 | GKR-SURF-BND-001 | Pessoa | externa; reversível | escolher ação externa conscientemente apresentada | UXA-004; UXA-007 | conduz à fronteira identificada sem atribuir efeito interno ou externo não comprovado | ação consciente; requisitos do destino permanecem externos | retorno ao GKR quando possível; efeito e tempo externos não examinados | UXA-012 no escopo da superfície | parcial | efeito externo não validado |
| GKR-TRN-206 | GKR-SURF-ORG-004 | GKR-SURF-COL-008 | Organização → Coletivo | entre participantes; handoff de autoridade; assíncrona | enviar proposta de relação | UXA-019 | finalidade, compromissos e recursos seguem para avaliação | autoridade institucional | retirar ou ajustar antes de aceite conforme contrato | UXA-019 | contratada | superfícies bilaterais ausentes |
| GKR-TRN-207 | GKR-SURF-COL-008 | GKR-SURF-ORG-005 | Coletivo → Organização | entre participantes; assíncrona | aceitar para avaliação, negociar ou recusar | UXA-019 | devolve decisão bilateral sem transferir propriedade | autoridade do responsável | recusa ou ajuste preservados | UXA-019 | contratada | interface bilateral ausente |
| GKR-TRN-208 | GKR-SURF-ORG-005 | GKR-SURF-ORG-006 | representantes autorizados | entre participantes; protegida | ambas as autoridades aprovam | UXA-019 | cria relação ativa com finalidade e limites definidos | aprovação bilateral | pausa, revisão e encerramento previstos | UXA-019 | contratada | operação bilateral não materializada |
| GKR-TRN-209 | GKR-SURF-ORG-006 | GKR-SURF-ORG-006 | representantes autorizados | condicional; reversível ou destrutiva | revisar e decidir renovar, ajustar, pausar ou encerrar | UXA-019 | altera estado da relação preservando histórico e autonomia | autoridade bilateral conforme efeito | contestação e saída previstas | UXA-019 | contratada | estados operacionais ausentes |
| GKR-TRN-210 | GKR-SURF-PER-201 | GKR-SURF-PER-202 | Pessoa ou visitante | direta; reversível | alternar do mapa para a lista sincronizada | UXA-004 | preserva consulta e filtros compatíveis sem criar nova busca de Coletivos | nenhum vínculo; localização conforme escolha | retorno ao mapa; imediata | UXA-025; UXA-029 em pacotes distintos | parcial | sincronização integrada entre mapa e lista |
| GKR-TRN-211 | GKR-SURF-PER-202 | GKR-SURF-PER-203 | Pessoa ou visitante | direta; reversível | selecionar oportunidade na lista | UXA-004; UXA-007 | abre Detalhe de Oportunidade identificado; não cria vínculo ou transação | conteúdo público; gates posteriores conforme ação | retorno à lista; imediata | UXA-029; UXA-012 em pacotes distintos | parcial | efeito externo posterior |

## 7. Opportunity Boost como camada comercial

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-301 | GKR-SURF-COM-001 | GKR-SURF-COM-004 | anunciante | protegida; condicional | concluir configuração e ativar campanha | UXA-038 | campanha passa ao estado ativo com parâmetros identificados | autoridade econômica e confirmação | pausar ou encerrar conforme contrato | UXA-041; UXA-046 | parcial | estados residuais e regras econômicas |
| GKR-TRN-302 | GKR-SURF-COM-004 | GKR-SURF-COM-002 | anunciante → Pessoa exposta | entre participantes; assíncrona | entrega comercial elegível | UXA-038 | conteúdo patrocinado identificado é apresentado sem comprar autoridade | critérios comerciais e proteção | Pessoa pode ignorar ou seguir organicamente | UXA-043 | parcial | integração completa com superfícies orgânicas |
| GKR-TRN-303 | GKR-SURF-COM-003 | GKR-SURF-COM-002 | Pessoa exposta | direta; reversível | selecionar item patrocinado ou explicação | UXA-038 | abre detalhe ou explicação mantendo identificação comercial | nenhuma legitimidade implícita | retorno à lista ou mapa | UXA-043; UXA-045 | localmente validada | continuidade transversal |
| GKR-TRN-304 | GKR-SURF-COM-002 | GKR-SURF-PER-201 | Pessoa exposta | reversível | voltar ao contexto orgânico de mapa | UXA-038 | restaura o Mapa de Oportunidades sem alterar reputação, relevância ou estado comercial | nenhum | retorno imediato | UXA-043; UXA-025 em pacotes distintos | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | GKR-SURF-COM-004 | GKR-SURF-COM-005 | anunciante | condicional | campanha ou entrega alcança estado residual específico | UXA-038 | efeito depende do estado materializado pela UXA-055 | autoridade e controle aplicáveis ao estado | retorno, desfazer, contestar ou continuar dependem do estado ainda não validado | UXA-055 | não examinada | dez estados residuais sem validação |
| GKR-TRN-306 | GKR-SURF-COM-002 | GKR-SURF-PER-202 | Pessoa exposta | reversível | voltar ao contexto orgânico de lista | UXA-038 | restaura a Lista de Oportunidades sem alterar reputação, relevância ou estado comercial | nenhum | retorno imediato | UXA-043; UXA-029 em pacotes distintos | parcial | integração orgânico–patrocinado |

## 8. Efeito da UXA-093

A UXA-093 não cria transições novas e preserva as seis ligações integralmente validadas no fluxo de solicitação: `105`, `106`, `107`, `108`, `109` e `112`.

Ela altera somente a evidência material de continuidade seguinte:

- `GKR-TRN-110` permanece `parcial`, agora com `PER-106` validada na origem e `PER-107` materializada no destino; gatilho, contexto, retorno, concorrência, idempotência e leitura versus ação ainda não foram validados como uma ligação única;
- `GKR-TRN-111` permanece `ausente`, agora com origem materializada, porque `PER-108` continua sem materialização vigente.

## 9. Regras de uso

- origem e destino materializados ou validados não presumem transição validada;
- materialização parcial não equivale a validação de transição;
- contrato bilateral não equivale a transição operacional validada;
- validação local não equivale a continuidade integrada;
- validação integral documental não equivale a implementação técnica;
- um handoff exige autoridade, identidade, dados, efeito, retorno, interrupção e tratamento de concorrência explícitos;
- estado obsoleto não pode produzir efeito sobre estado canônico mais recente;
- repetição de interação ou entrega não pode duplicar o efeito lógico;
- estado `lido` não pode ser confundido com estado substantivo, consentimento ou ação concluída;
- uma versão visual reformulada exige revalidação antes de ser tratada como versão funcionalmente validada;
- navegação posterior a uma decisão não deve ser confundida com gate para o efeito já confirmado;
- transições ausentes permanecem registradas sem seta afirmativa de implementação;
- fronteira externa identificada não presume execução ou resultado externo;
- a cobertura permanece seletiva e não exaustiva;
- o status `active` aprova o instrumento de registro, não a implementação ponta a ponta.