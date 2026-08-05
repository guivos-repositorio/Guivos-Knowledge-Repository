---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.3.0 incorpora a promoção controlada da UXA-080 após a revalidação aprovada com ressalvas pela UXA-079. Permanecem vigentes as correções da UXA-078:

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
| localmente validada | examinada dentro do pacote indicado, sem comprovação ponta a ponta |
| parcial | origem, destino ou efeito possuem cobertura incompleta |
| contratada | autoridade define a ligação, mas não há materialização suficiente |
| ausente | ligação necessária conhecida sem materialização |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

## 3. Contagem reformulada

| Família | Quantidade |
|---|---:|
| jornada pessoal | 7 |
| Pessoa em Coletivos e operação do responsável | 13 |
| Organização, oportunidades e relações bilaterais | 11 |
| Opportunity Boost | 6 |
| **Total** | **37** |

O aumento de 34 para 37 transições decorre da divisão controlada de mapa, lista e retornos orgânicos. Não representa comportamento implementado.

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
| GKR-TRN-104 | GKR-SURF-PER-104 | GKR-SURF-PER-105 | solicitante | protegida; assíncrona; handoff de autoridade | confirmar envio | UXA-056 | dados autorizados da solicitação seguem ao Coletivo; estado torna-se pendente | confirmação explícita | cancelar conforme estado; aguarda decisão | UXA-065; UXA-067 | parcial | destino operacional do responsável ausente |
| GKR-TRN-105 | GKR-SURF-PER-105 | GKR-SURF-COL-003 | solicitante → responsável | entre participantes; handoff de autoridade; assíncrona | solicitação disponível para análise | UXA-056; UXA-059 | transfere próxima decisão ao responsável; dados limitados à finalidade | autoridade do responsável | solicitante pode cancelar; tempo protegido | envio e estado pendente na visão da Pessoa | parcial | superfície de gestão ausente |
| GKR-TRN-106 | GKR-SURF-COL-003 | GKR-SURF-PER-105 | responsável → solicitante | entre participantes; assíncrona; reversível | pedir informação adicional | UXA-056; UXA-066; UXA-067 | pedido aparece para a Pessoa; aprovação não ocorre | autoridade do responsável | Pessoa responde, revisa ou não prossegue | UXA-067 na visão da Pessoa | parcial | origem operacional não materializada |
| GKR-TRN-107 | GKR-SURF-PER-105 | GKR-SURF-COL-003 | solicitante → responsável | entre participantes; assíncrona | enviar resposta adicional | UXA-056; UXA-067 | conteúdo adicional autorizado retorna à análise | resposta consciente | editar antes do envio ou desistir | UXA-067 na visão da Pessoa | parcial | fila operacional não materializada |
| GKR-TRN-108 | GKR-SURF-COL-003 | GKR-SURF-PER-106 | responsável → participante | handoff de autoridade; entre participantes | aprovar solicitação e formar vínculo | UXA-014; UXA-056 | cria vínculo conforme papel aceito | decisão autorizada e aceite aplicável | saída e contestação conforme vínculo; assíncrona | resultado representado na visão da Pessoa | parcial | decisão do responsável e Meus Coletivos ausentes |
| GKR-TRN-109 | GKR-SURF-COL-003 | GKR-SURF-PER-105 | responsável → solicitante | entre participantes; assíncrona | recusar ou deixar expirar | UXA-056; UXA-067 | apresenta resultado distinto de cancelamento | autoridade e prazo | nova exploração possível; assíncrona | UXA-067 na visão da Pessoa | parcial | origem operacional não materializada |
| GKR-TRN-110 | GKR-SURF-PER-106 | GKR-SURF-PER-107 | participante | direta | acessar atualizações do vínculo | UXA-059 | apresenta comunicações e mudanças autorizadas | vínculo ativo | retorno a Meus Coletivos | — | ausente | ambas as superfícies não materializadas |
| GKR-TRN-111 | GKR-SURF-PER-107 | GKR-SURF-PER-108 | participante | direta; condicional | selecionar Coletivo ou atualização | UXA-059 | abre início operacional do participante | vínculo e papel | retorno às atualizações | — | ausente | Início do Participante em reformulação |
| GKR-TRN-112 | GKR-SURF-COL-002 | GKR-SURF-COL-003 | responsável | direta; protegida | acessar solicitações | UXA-059 | abre fila operacional dentro da autoridade concedida | representação válida | retorno à visão geral | — | ausente | duas superfícies não materializadas |
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

## 8. Resolução dos achados da UXA-077

### F01 — endpoints

- `GKR-TRN-205` termina em `GKR-SURF-BND-001`;
- `GKR-TRN-304` termina em `GKR-SURF-PER-201`;
- o retorno alternativo à lista é registrado por `GKR-TRN-306` em `GKR-SURF-PER-202`;
- nenhuma origem ou destino permanece em texto livre.

### F02 — descoberta de oportunidades

- `GKR-SURF-PER-102` permanece exclusivo da busca de Coletivos;
- `GKR-TRN-203` conduz ao Mapa de Oportunidades;
- `GKR-TRN-204` conduz do mapa ao Detalhe de Oportunidade;
- `GKR-TRN-210` conecta mapa e lista;
- `GKR-TRN-211` conecta lista e detalhe.

### F03 — publicação e detalhe

- `GKR-SURF-ORG-003` é o estado institucional de oportunidade aprovada ou ativa;
- `GKR-SURF-PER-203` é o Detalhe de Oportunidade percebido pela Pessoa;
- a passagem entre publicação e descoberta permanece `não examinada`.

### F04 — estados residuais

`GKR-TRN-305` aponta para UXA-055 como evidência de materialização. A transição permanece `não examinada` porque os dez estados residuais ainda não possuem validação funcional específica.

## 9. Regras de uso

- origem materializada não presume destino materializado;
- contrato bilateral não equivale a transição operacional;
- validação local não equivale a continuidade integrada;
- um handoff exige autoridade, dados, efeito, retorno e interrupção explícitos;
- transições ausentes permanecem registradas sem seta afirmativa de implementação;
- fronteira externa identificada não presume execução ou resultado externo;
- a cobertura permanece seletiva e não exaustiva;
- o status `active` aprova o instrumento de registro, não a continuidade ponta a ponta;
- a UXA-080 não altera os estados, evidências ou lacunas das 37 transições.
