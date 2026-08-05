---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A transição pode estar:

- validada apenas dentro de um pacote de origem;
- parcial entre pacotes;
- contratada sem materialização;
- ausente;
- não examinada como continuidade integrada.

Nenhuma linha executa lógica de negócio ou cria ligação inexistente.

## 2. Convenções de estado

| Estado | Significado |
|---|---|
| localmente validada | examinada dentro do pacote indicado, sem comprovação ponta a ponta |
| parcial | origem, destino ou efeito possuem cobertura incompleta |
| contratada | autoridade define a ligação, mas não há materialização suficiente |
| ausente | ligação necessária conhecida sem materialização |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

## 3. Jornada pessoal

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-001 | GKR-SURF-PER-001 | GKR-SURF-PER-002 | visitante → Pessoa | direta; protegida | escolher iniciar jornada | UXA-020 | muda de conteúdo público para entrada protegida; nenhum dado sensível presumido | entrada consciente | retorno à Home; imediata | UXA-021; UXA-035 | parcial | continuidade entre pacotes |
| GKR-TRN-002 | GKR-SURF-PER-002 | GKR-SURF-PER-003 | Pessoa | direta; protegida | concluir orientação e escolher modalidade | UXA-020; UXA-023 | registra somente a escolha apresentada | autenticação quando necessária | retorno permitido; imediata | UXA-034; UXA-035 | localmente validada | integração com expressão guiada |
| GKR-TRN-003 | GKR-SURF-PER-003 | GKR-SURF-PER-004 | Pessoa | condicional; reversível | escolher texto ou voz | UXA-068 | abre modalidade escolhida; conteúdo ainda é rascunho | escolha explícita | troca ou cancelamento; imediata | UXA-069 | parcial | ligação UXA-034 → UXA-068 |
| GKR-TRN-004 | GKR-SURF-PER-004 | GKR-SURF-PER-005 | Pessoa | protegida; reversível | concluir expressão e avançar para inventário | UXA-023; UXA-068 | conteúdo de origem e derivados identificados seguem para revisão | revisão consciente; sem análise implícita | editar, descartar ou voltar; imediata | UXA-035; UXA-069 | parcial | integração expressão–inventário |
| GKR-TRN-005 | GKR-SURF-PER-005 | GKR-SURF-PER-006 | Pessoa | protegida; condicional | autorizar finalidade específica | UXA-023 | somente conteúdos autorizados entram em processamento | autorização específica | recusar ou retirar antes do processamento; imediata | UXA-035; UXA-037 | parcial | continuidade entre materializações |
| GKR-TRN-006 | GKR-SURF-PER-006 | GKR-SURF-PER-007 | Pessoa | direta; protegida | processamento concluído | UXA-023 | apresenta compreensão inicial revisável, mantendo fontes separadas | processamento previamente autorizado | interrupção e retorno conforme pacote; assíncrona ou imediata conforme estado | UXA-037 | localmente validada | continuidade ponta a ponta |
| GKR-TRN-007 | GKR-SURF-PER-007 | GKR-SURF-PER-008 | Pessoa autenticada | condicional; protegida | revisar compreensão e decidir persistência/personalização | UXA-002; UXA-023 | somente conteúdos e permissões aceitos podem sustentar continuidade | revisão e gates próprios | recusar persistência; tempo não consolidado | UXA-010; UXA-037 | não examinada | reconciliação com Tela Hoje |

## 4. Pessoa em Coletivos e operação do responsável

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-101 | GKR-SURF-PER-101 | GKR-SURF-PER-102 | visitante | direta; condicional | pesquisar ou aplicar filtro | UXA-056 | critérios produzem resultados; consulta não cria vínculo | nenhum vínculo | limpar filtros ou voltar; imediata | UXA-061 | localmente validada | continuidade entre famílias |
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

## 5. Organização, oportunidades e relações bilaterais

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-201 | GKR-SURF-ORG-001 | GKR-SURF-ORG-002 | representante institucional | protegida; direta | escolher cadastrar oportunidade | UXA-004; UXA-014 | inicia cadastro dentro da unidade e papel apresentados | autoridade institucional | cancelar e retornar | UXA-013 | parcial | ligação com visão institucional |
| GKR-TRN-202 | GKR-SURF-ORG-002 | GKR-SURF-ORG-003 | representante institucional | protegida; condicional | revisar e publicar | UXA-004 | torna oportunidade consultável segundo regras de visibilidade | confirmação e autoridade | editar ou retirar posteriormente | UXA-013 | localmente validada | distribuição entre superfícies |
| GKR-TRN-203 | GKR-SURF-ORG-003 | GKR-SURF-PER-102 | Organização → visitante | entre participantes; direta | oportunidade aparece em descoberta | UXA-004 | metadados públicos tornam-se encontráveis | publicação válida | Organização pode editar ou retirar | pacotes distintos de cadastro e descoberta | não examinada | integração publicação–consumo |
| GKR-TRN-204 | GKR-SURF-PER-102 | GKR-SURF-ORG-003 | visitante | direta | selecionar oportunidade | UXA-004; UXA-007 | abre detalhe identificado | conteúdo público | retorno à lista ou mapa | UXA-012 | parcial | efeito externo posterior |
| GKR-TRN-205 | GKR-SURF-ORG-003 | destino externo identificado | Pessoa | externa; reversível | escolher ação externa apresentada | UXA-004; UXA-007 | conduz ao destino sem atribuir efeito interno não comprovado | ação consciente | retorno ao GKR quando possível | UXA-012 no escopo da superfície | parcial | efeito externo não validado |
| GKR-TRN-206 | GKR-SURF-ORG-004 | GKR-SURF-COL-008 | Organização → Coletivo | entre participantes; handoff de autoridade; assíncrona | enviar proposta de relação | UXA-019 | finalidade, compromissos e recursos seguem para avaliação | autoridade institucional | retirar ou ajustar antes de aceite conforme contrato | UXA-019 | contratada | superfícies bilaterais ausentes |
| GKR-TRN-207 | GKR-SURF-COL-008 | GKR-SURF-ORG-005 | Coletivo → Organização | entre participantes; assíncrona | aceitar para avaliação, negociar ou recusar | UXA-019 | devolve decisão bilateral sem transferir propriedade | autoridade do responsável | recusa ou ajuste preservados | UXA-019 | contratada | interface bilateral ausente |
| GKR-TRN-208 | GKR-SURF-ORG-005 | GKR-SURF-ORG-006 | representantes autorizados | entre participantes; protegida | ambas as autoridades aprovam | UXA-019 | cria relação ativa com finalidade e limites definidos | aprovação bilateral | pausa, revisão e encerramento previstos | UXA-019 | contratada | operação bilateral não materializada |
| GKR-TRN-209 | GKR-SURF-ORG-006 | GKR-SURF-ORG-006 | representantes autorizados | condicional; reversível ou destrutiva | revisar e decidir renovar, ajustar, pausar ou encerrar | UXA-019 | altera estado da relação preservando histórico e autonomia | autoridade bilateral conforme efeito | contestação e saída previstas | UXA-019 | contratada | estados operacionais ausentes |

## 6. Opportunity Boost como camada comercial

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-301 | GKR-SURF-COM-001 | GKR-SURF-COM-004 | anunciante | protegida; condicional | concluir configuração e ativar campanha | UXA-038 | campanha passa ao estado ativo com parâmetros identificados | autoridade econômica e confirmação | pausar ou encerrar conforme contrato | UXA-041; UXA-046 | parcial | estados residuais e regras econômicas |
| GKR-TRN-302 | GKR-SURF-COM-004 | GKR-SURF-COM-002 | anunciante → Pessoa exposta | entre participantes; assíncrona | entrega comercial elegível | UXA-038 | conteúdo patrocinado identificado é apresentado sem comprar autoridade | critérios comerciais e proteção | Pessoa pode ignorar ou seguir organicamente | UXA-043 | parcial | integração completa com superfícies orgânicas |
| GKR-TRN-303 | GKR-SURF-COM-003 | GKR-SURF-COM-002 | Pessoa exposta | direta; reversível | selecionar item patrocinado ou explicação | UXA-038 | abre detalhe ou explicação mantendo identificação comercial | nenhuma legitimidade implícita | retorno à lista ou mapa | UXA-043; UXA-045 | localmente validada | continuidade transversal |
| GKR-TRN-304 | GKR-SURF-COM-002 | superfície orgânica de origem | Pessoa exposta | reversível | voltar ou continuar sem ação comercial | UXA-038 | restaura contexto orgânico sem alteração de reputação | nenhum | retorno imediato | UXA-043 | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | GKR-SURF-COM-004 | GKR-SURF-COM-005 | anunciante | condicional | campanha alcança estado residual específico | UXA-038 | efeito depende do estado materializado | autoridade econômica aplicável | conforme estado ainda não validado | UXA-047 a UXA-054 conforme pacote | não examinada | 10 estados residuais sem validação |

## 7. Regras de uso

- origem materializada não presume destino materializado;
- contrato bilateral não equivale a transição operacional;
- validação local não equivale a continuidade integrada;
- um handoff exige autoridade, dados, efeito, retorno e interrupção explícitos;
- transições ausentes permanecem registradas sem seta afirmativa de implementação;
- o registro permanece `draft` até validação funcional específica.
