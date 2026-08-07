---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.5.0
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
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.5.0 preserva as 37 transições e registra a nova evidência observacional de `GKR-SURF-COL-003` após UXA-088. Nenhuma transição nova é criada e nenhuma é declarada validada ponta a ponta por materialização.

## 2. Convenções de estado

| Estado | Significado |
|---|---|
| localmente validada | examinada dentro do pacote indicado, sem comprovação ponta a ponta |
| parcial | origem, destino, efeito ou validação possuem cobertura incompleta |
| contratada | autoridade define a ligação, mas não há materialização suficiente |
| ausente | ligação necessária conhecida sem materialização |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

## 3. Contagem

| Família | Quantidade |
|---|---:|
| jornada pessoal | 7 |
| Pessoa em Coletivos e operação do responsável | 13 |
| Organização, oportunidades e relações bilaterais | 11 |
| Opportunity Boost | 6 |
| **Total** | **37** |

## 4. Jornada pessoal

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-001 | GKR-SURF-PER-001 | GKR-SURF-PER-002 | visitante → Pessoa | direta; protegida | escolher iniciar jornada | UXA-020 | muda de conteúdo público para entrada protegida | entrada consciente | retorno à Home | UXA-021; UXA-035 | parcial | continuidade entre pacotes |
| GKR-TRN-002 | GKR-SURF-PER-002 | GKR-SURF-PER-003 | Pessoa | direta; protegida | concluir orientação e escolher modalidade | UXA-020; UXA-023 | registra escolha apresentada | autenticação quando necessária | retorno permitido | UXA-034; UXA-035 | localmente validada | integração com expressão guiada |
| GKR-TRN-003 | GKR-SURF-PER-003 | GKR-SURF-PER-004 | Pessoa | condicional; reversível | escolher texto ou voz | UXA-068 | abre modalidade escolhida | escolha explícita | troca ou cancelamento | UXA-069 | parcial | ligação UXA-034 → UXA-068 |
| GKR-TRN-004 | GKR-SURF-PER-004 | GKR-SURF-PER-005 | Pessoa | protegida; reversível | concluir expressão e avançar | UXA-023; UXA-068 | conteúdo e derivados seguem para revisão | revisão consciente | editar, descartar ou voltar | UXA-035; UXA-069 | parcial | integração expressão–inventário |
| GKR-TRN-005 | GKR-SURF-PER-005 | GKR-SURF-PER-006 | Pessoa | protegida; condicional | autorizar finalidade | UXA-023 | somente conteúdo autorizado é processado | autorização específica | recusar ou retirar antes do processamento | UXA-035; UXA-037 | parcial | continuidade entre materializações |
| GKR-TRN-006 | GKR-SURF-PER-006 | GKR-SURF-PER-007 | Pessoa | direta; protegida | processamento concluído | UXA-023 | apresenta compreensão revisável | processamento autorizado | retorno conforme pacote | UXA-037 | localmente validada | continuidade ponta a ponta |
| GKR-TRN-007 | GKR-SURF-PER-007 | GKR-SURF-PER-008 | Pessoa autenticada | condicional; protegida | revisar compreensão e decidir continuidade | UXA-002; UXA-023 | apenas conteúdos e permissões aceitos sustentam continuidade | revisão e gates próprios | recusar persistência | UXA-010; UXA-037 | não examinada | reconciliação com Tela Hoje |

## 5. Pessoa em Coletivos e operação do responsável

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-101 | GKR-SURF-PER-101 | GKR-SURF-PER-102 | visitante | direta; condicional | pesquisar ou aplicar filtro | UXA-056 | consulta produz resultados sem vínculo | nenhum vínculo | limpar filtros ou voltar | UXA-061 | localmente validada | continuidade entre famílias |
| GKR-TRN-102 | GKR-SURF-PER-102 | GKR-SURF-PER-103 | visitante | direta | selecionar Coletivo | UXA-056 | abre informações públicas | conteúdo público | retornar aos resultados | UXA-061; UXA-063 | parcial | ligação entre pacotes |
| GKR-TRN-103 | GKR-SURF-PER-103 | GKR-SURF-PER-104 | solicitante potencial | protegida; condicional | solicitar participação | UXA-056 | inicia revisão consciente | autenticação e elegibilidade | cancelar e retornar | UXA-063; UXA-065 | parcial | handoff para solicitação |
| GKR-TRN-104 | GKR-SURF-PER-104 | GKR-SURF-PER-105 | solicitante | protegida; assíncrona | confirmar envio | UXA-056 | dados autorizados seguem ao processo e estado torna-se pendente | confirmação explícita | cancelar conforme estado | UXA-065; UXA-067 | parcial | handoff posterior agora materializado, integração não validada |
| GKR-TRN-105 | GKR-SURF-PER-105 | GKR-SURF-COL-003 | solicitante → responsável | entre participantes; handoff de autoridade; assíncrona | solicitação disponível para análise | UXA-056; UXA-059 | transfere próxima decisão; dados limitados à finalidade | autoridade do responsável | solicitante pode cancelar | UXA-067 na Pessoa; UXA-088 no responsável | parcial | endpoints materializados; validação integrada pendente |
| GKR-TRN-106 | GKR-SURF-COL-003 | GKR-SURF-PER-105 | responsável → solicitante | entre participantes; assíncrona; reversível | pedir informação adicional | UXA-056; UXA-066; UXA-067 | pedido aparece para a Pessoa sem aprovação | autoridade e finalidade limitada | Pessoa responde, prefere não informar, contesta ou cancela | UXA-088 na origem; UXA-067 no destino | parcial | validação bilateral pendente |
| GKR-TRN-107 | GKR-SURF-PER-105 | GKR-SURF-COL-003 | solicitante → responsável | entre participantes; assíncrona | enviar resposta adicional | UXA-056; UXA-067 | conteúdo autorizado retorna à análise | resposta consciente | editar antes do envio ou desistir | UXA-067 na origem; UXA-088 no destino | parcial | validação bilateral pendente |
| GKR-TRN-108 | GKR-SURF-COL-003 | GKR-SURF-PER-106 | responsável → participante | handoff de autoridade; entre participantes | aprovar e formar vínculo | UXA-014; UXA-056 | cria vínculo de participante sem função automática | autoridade e confirmação | decisão pode ser abandonada antes da confirmação; controles do vínculo futuros | UXA-088 na origem; resultado em UXA-067 | parcial | PER-106 continua ausente; validação integrada pendente |
| GKR-TRN-109 | GKR-SURF-COL-003 | GKR-SURF-PER-105 | responsável → solicitante | entre participantes; assíncrona | recusar; expiração permanece evento temporal distinto | UXA-056; UXA-067 | apresenta recusa proporcional ou estado temporal distinto | autoridade, fundamento e prazo | voltar sem decidir antes da confirmação; nova exploração posterior | UXA-088 na origem; UXA-067 no destino | parcial | validação bilateral pendente |
| GKR-TRN-110 | GKR-SURF-PER-106 | GKR-SURF-PER-107 | participante | direta | acessar atualizações do vínculo | UXA-059 | apresenta comunicações autorizadas | vínculo ativo | retorno a Meus Coletivos | — | ausente | ambas superfícies não materializadas |
| GKR-TRN-111 | GKR-SURF-PER-107 | GKR-SURF-PER-108 | participante | direta; condicional | selecionar Coletivo ou atualização | UXA-059 | abre início operacional | vínculo e papel | retorno às atualizações | — | ausente | Início do Participante em reformulação |
| GKR-TRN-112 | GKR-SURF-COL-002 | GKR-SURF-COL-003 | responsável | direta; protegida | acessar solicitações a partir da visão geral | UXA-059; UXA-086; UXA-088 | abre a fila especializada sem ampliar autoridade | representação válida e escopo concedido | retornar à Visão Geral; nenhuma decisão implícita | UXA-087 na origem; UXA-088 no destino | parcial | ambos endpoints materializados; validação funcional do conjunto pendente |
| GKR-TRN-113 | GKR-SURF-COL-004 | GKR-SURF-COL-005 | responsável | condicional; protegida | comunicar a participantes autorizados | UXA-058; UXA-059 | distribui comunicação oficial | papel e audiência | corrigir ou encerrar conforme regras futuras | — | contratada | operação interna não materializada |

## 6. Organização, oportunidades e relações bilaterais

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-201 | GKR-SURF-ORG-001 | GKR-SURF-ORG-002 | representante institucional | protegida; direta | cadastrar oportunidade | UXA-004; UXA-014 | inicia cadastro | autoridade institucional | cancelar e retornar | UXA-013 | parcial | ligação com visão institucional |
| GKR-TRN-202 | GKR-SURF-ORG-002 | GKR-SURF-ORG-003 | representante institucional | protegida; condicional | revisar e ativar | UXA-004 | move cadastro ao estado elegível/ativo | confirmação e autoridade | editar, retirar, pausar ou encerrar | UXA-013 | localmente validada | distribuição entre superfícies |
| GKR-TRN-203 | GKR-SURF-ORG-003 | GKR-SURF-PER-201 | Organização → Pessoa | entre participantes; assíncrona | oportunidade ativa torna-se elegível | UXA-004 | metadados públicos podem ser descobertos | publicação válida | pausar, corrigir ou retirar | UXA-013; UXA-025 | não examinada | integração publicação–descoberta |
| GKR-TRN-204 | GKR-SURF-PER-201 | GKR-SURF-PER-203 | Pessoa | direta; reversível | selecionar oportunidade no mapa | UXA-004; UXA-007 | abre detalhe | conteúdo público | retorno ao mapa | UXA-025; UXA-012 | parcial | efeito externo posterior |
| GKR-TRN-205 | GKR-SURF-PER-203 | GKR-SURF-BND-001 | Pessoa | externa; reversível | escolher ação externa | UXA-004; UXA-007 | conduz à fronteira identificada | ação consciente | retorno quando possível | UXA-012 | parcial | efeito externo não validado |
| GKR-TRN-206 | GKR-SURF-ORG-004 | GKR-SURF-COL-008 | Organização → Coletivo | entre participantes; assíncrona | enviar proposta | UXA-019 | finalidade e recursos seguem para avaliação | autoridade institucional | retirar ou ajustar | UXA-019 | contratada | superfícies bilaterais ausentes |
| GKR-TRN-207 | GKR-SURF-COL-008 | GKR-SURF-ORG-005 | Coletivo → Organização | entre participantes; assíncrona | avaliar, negociar ou recusar | UXA-019 | devolve decisão sem transferir propriedade | autoridade do responsável | recusa ou ajuste | UXA-019 | contratada | interface bilateral ausente |
| GKR-TRN-208 | GKR-SURF-ORG-005 | GKR-SURF-ORG-006 | representantes autorizados | protegida | ambas autoridades aprovam | UXA-019 | cria relação ativa com limites | aprovação bilateral | pausa, revisão e encerramento | UXA-019 | contratada | operação bilateral não materializada |
| GKR-TRN-209 | GKR-SURF-ORG-006 | GKR-SURF-ORG-006 | representantes autorizados | condicional | revisar relação | UXA-019 | altera estado preservando autonomia | autoridade bilateral | contestação e saída | UXA-019 | contratada | estados operacionais ausentes |
| GKR-TRN-210 | GKR-SURF-PER-201 | GKR-SURF-PER-202 | Pessoa | direta; reversível | mapa → lista | UXA-004 | preserva consulta e filtros | nenhum vínculo | retorno ao mapa | UXA-025; UXA-029 | parcial | sincronização integrada |
| GKR-TRN-211 | GKR-SURF-PER-202 | GKR-SURF-PER-203 | Pessoa | direta; reversível | selecionar oportunidade na lista | UXA-004; UXA-007 | abre detalhe | conteúdo público | retorno à lista | UXA-029; UXA-012 | parcial | efeito externo posterior |

## 7. Opportunity Boost como camada comercial

| ID | Origem | Destino | Perspectiva | Tipo | Condição e ação | Autoridade | Efeito e dados | Gate | Reversibilidade, interrupção e tempo | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-TRN-301 | GKR-SURF-COM-001 | GKR-SURF-COM-004 | anunciante | protegida; condicional | ativar campanha | UXA-038 | campanha torna-se ativa | autoridade econômica e confirmação | pausar ou encerrar | UXA-041; UXA-046 | parcial | estados residuais e regras econômicas |
| GKR-TRN-302 | GKR-SURF-COM-004 | GKR-SURF-COM-002 | anunciante → Pessoa | assíncrona | entrega elegível | UXA-038 | conteúdo patrocinado identificado | critérios comerciais e proteção | ignorar ou seguir organicamente | UXA-043 | parcial | integração com superfícies orgânicas |
| GKR-TRN-303 | GKR-SURF-COM-003 | GKR-SURF-COM-002 | Pessoa | direta; reversível | selecionar item patrocinado | UXA-038 | abre detalhe/explicação comercial | identificação comercial | retorno à lista/mapa | UXA-043; UXA-045 | localmente validada | continuidade transversal |
| GKR-TRN-304 | GKR-SURF-COM-002 | GKR-SURF-PER-201 | Pessoa | reversível | voltar ao mapa orgânico | UXA-038 | restaura mapa sem alterar reputação | nenhum | retorno imediato | UXA-043; UXA-025 | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | GKR-SURF-COM-004 | GKR-SURF-COM-005 | anunciante | condicional | alcançar estado residual | UXA-038 | efeito depende de UXA-055 | autoridade aplicável | depende do estado | UXA-055 | não examinada | dez estados residuais sem validação |
| GKR-TRN-306 | GKR-SURF-COM-002 | GKR-SURF-PER-202 | Pessoa | reversível | voltar à lista orgânica | UXA-038 | restaura lista sem alterar reputação | nenhum | retorno imediato | UXA-043; UXA-029 | parcial | integração orgânico–patrocinado |

## 8. Efeito da UXA-088

A UXA-088 não cria transições. Ela altera a evidência observacional de seis ligações:

- `TRN-105`, `106`, `107`, `108` e `109` passam a possuir materialização do lado responsável;
- `TRN-112` passa a possuir origem e destino materializados;
- todos continuam `parcial` porque a validação funcional bilateral/integrada ainda não foi executada;
- `TRN-108` mantém lacuna adicional porque `PER-106` continua ausente.

## 9. Regras de uso

- endpoints materializados não equivalem a transição validada;
- contrato bilateral não equivale a operação validada;
- validação local não equivale a continuidade integrada;
- um handoff exige autoridade, dados, efeito, retorno e interrupção explícitos;
- fronteira externa identificada não presume execução ou resultado externo;
- o status `active` aprova o instrumento, não a continuidade ponta a ponta.
