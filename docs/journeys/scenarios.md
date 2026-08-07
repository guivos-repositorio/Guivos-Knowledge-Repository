---
id: GKR-JOURNEY-SCENARIOS-001
title: Cenários Integrados de Jornada
status: active
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
normative: false
---

# Cenários Integrados de Jornada

## 1. Regra de evidência

Cada cenário deve distinguir nós materializados, nós apenas contratados, transições examinadas e ponto de interrupção por lacuna.

Uma narrativa compreensível não equivale a um fluxo funcionalmente validado ou implementado.

## 2. Cenários reformulados

### 2.1 Pessoa inicia sua jornada protegida

| Campo | Registro |
|---|---|
| finalidade | permitir expressão protegida e compreensão inicial revisável |
| participantes e perspectivas | Pessoa |
| nós materializados | Home, entrada protegida, expressão guiada, inventário, processamento e compreensão inicial |
| nós apenas contratados | persistência e personalização posteriores conforme gates próprios |
| transições validadas | transições examinadas dentro dos pacotes UXA-021, UXA-035, UXA-037 e UXA-069 |
| transições não validadas como conjunto | continuidade ponta a ponta entre todos os pacotes e entrada na Tela Hoje |
| interrupção por lacuna | reconciliação integral com a experiência recorrente |
| conclusão permitida | superfícies e decisões locais possuem evidência nos pacotes de origem |
| conclusão proibida | declarar toda a jornada pessoal validada ponta a ponta |

### 2.2 Pessoa encontra, solicita e recebe resultado de participação

| Campo | Registro |
|---|---|
| finalidade | descobrir um Coletivo, solicitar participação e compreender o resultado |
| participantes e perspectivas | Pessoa solicitante e responsável do Coletivo |
| nós materializados | explorar, busca, Perfil Público, revisão, PER-105 e COL-003 |
| nós validados | superfícies até PER-105 na versão aplicável; COL-003; handoffs 105/106/107/109 por UXA-090 |
| transições integralmente validadas | TRN-105, TRN-106, TRN-107 e TRN-109 |
| continuidade parcial | aprovação via TRN-108 após reformulação UXA-091 |
| interrupção por lacuna | validação do estado aprovado corrente e de PER-106 |
| conclusão permitida | solicitação, pedido adicional, resposta e recusa possuem continuidade bilateral validada |
| conclusão proibida | declarar a aprovação pós-UXA-091 validada antes da UXA-092 |

### 2.3 Pessoa recebe aprovação e encontra o vínculo em Meus Coletivos

| Campo | Registro |
|---|---|
| finalidade | tornar a formação do vínculo compreensível sem criar função, pressão ou promessa de superfícies ausentes |
| participantes e perspectivas | responsável do Coletivo e Pessoa participante |
| nós materializados | COL-003; resultado aprovado corrente em PER-105; PER-106 |
| passagem materializada | aprovação → resultado em PER-105 → `Ver em Meus Coletivos` → PER-106 |
| transição | TRN-108 parcial |
| validação | COL-003 validada; estado aprovado corrente e PER-106 pendentes |
| interrupção por lacuna | revalidação integrada em UXA-092 |
| conclusão permitida | existe materialização suficiente para inspecionar a continuidade |
| conclusão proibida | afirmar TRN-108 integralmente validada ou implementada |

### 2.4 Coletivo solicita informação adicional

| Campo | Registro |
|---|---|
| finalidade | complementar solicitação sem criar aprovação implícita |
| participantes e perspectivas | responsável do Coletivo e Pessoa solicitante |
| nós materializados | COL-003 e PER-105 |
| transições integralmente validadas | TRN-106 e TRN-107 por UXA-090 |
| retorno | Pessoa pode responder, não informar, contestar ou cancelar |
| conclusão permitida | o ciclo bilateral de pedido adicional e resposta possui validação documental integrada |
| conclusão proibida | confundir validação documental com implementação técnica |

### 2.5 Organização e Coletivo estabelecem relação

| Campo | Registro |
|---|---|
| finalidade | formar relação bilateral com autonomia e saída preservadas |
| participantes e perspectivas | Organização e Coletivo |
| nós materializados | nenhum fluxo bilateral específico |
| nós apenas contratados | proposta, avaliação, negociação, aprovação, relação ativa, revisão e saída |
| transições validadas | nenhuma como jornada bilateral integrada |
| interrupção por lacuna | início do fluxo bilateral |
| conclusão permitida | UXA-019 define responsabilidades e limites |
| conclusão proibida | afirmar existência de interface ou fluxo operacional bilateral |

### 2.6 Organização publica oportunidade e Pessoa acessa

| Campo | Registro |
|---|---|
| finalidade | publicar oportunidade e permitir consulta pela Pessoa |
| participantes e perspectivas | Organização publicadora e Pessoa visitante |
| nós materializados | cadastro, superfícies de descoberta e detalhe |
| nós apenas contratados | efeitos externos após o destino identificado |
| transições validadas | cadastro e detalhe nos respectivos pacotes |
| transições não validadas como conjunto | publicação até consumo em todas as superfícies e efeitos externos |
| interrupção por lacuna | após o destino ou ação externa |
| conclusão permitida | superfícies existentes possuem validação local |
| conclusão proibida | declarar o ciclo completo da oportunidade validado |

### 2.7 Sobreposição comercial identificada

| Campo | Registro |
|---|---|
| finalidade | permitir promoção identificada sem comprar autoridade, legitimidade ou reputação |
| participantes e perspectivas | Organização anunciante e Pessoa exposta; Opportunity Boost como camada comercial |
| nós materializados | 46 referências |
| transições validadas | 36 referências conforme pacotes |
| transições não validadas como conjunto | 10 estados residuais e integração completa com superfícies orgânicas |
| interrupção por lacuna | estados residuais sem validação |
| conclusão permitida | camada comercial identificada e separada da autoridade orgânica |
| conclusão proibida | tratar publicidade como participante, reputação ou recomendação |

## 3. Critério de completude

Um cenário só poderá ser marcado como completo quando todos os seus nós, transições, autoridades, dados, retornos, estados de exceção e pontos de saída estiverem documentados e funcionalmente validados como conjunto.

## 4. Estado vigente

O documento permanece `active` como síntese de cenários governados e limitados pela evidência. A UXA-091 acrescenta a inspeção do cenário de aprovação até `Meus Coletivos`, ainda parcial.

O status `active` não transforma qualquer cenário em jornada implementada. A UXA-092 não é iniciada por esta sincronização.
