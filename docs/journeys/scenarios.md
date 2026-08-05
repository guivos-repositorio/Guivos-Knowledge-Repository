---
id: GKR-JOURNEY-SCENARIOS-001
title: Cenários Integrados de Jornada
status: active
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
normative: false
---

# Cenários Integrados de Jornada

## 1. Regra de evidência

Cada cenário deve distinguir nós materializados, nós apenas contratados, transições examinadas e ponto de interrupção por lacuna.

Uma narrativa compreensível não equivale a um fluxo funcionalmente validado.

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

### 2.2 Pessoa encontra e solicita participação em um Coletivo

| Campo | Registro |
|---|---|
| finalidade | descobrir um Coletivo e enviar solicitação consciente |
| participantes e perspectivas | Pessoa visitante e solicitante; Coletivo como destino institucional |
| nós materializados | explorar, buscar, Perfil Público, revisão, solicitação e estados pendentes na visão da Pessoa |
| nós apenas contratados | análise e decisão pelo responsável |
| transições validadas | navegação e estados examinados nas UXA-061, UXA-063, UXA-065 e UXA-067 |
| transições não validadas como conjunto | handoff para o responsável e formação do vínculo |
| interrupção por lacuna | após `Solicitação Pendente`; `Meus Coletivos` ausente |
| conclusão permitida | a perspectiva da Pessoa possui cobertura até o acompanhamento pendente |
| conclusão proibida | afirmar que a operação bilateral está materializada |

### 2.3 Coletivo solicita informação adicional

| Campo | Registro |
|---|---|
| finalidade | complementar uma solicitação sem criar aprovação implícita |
| participantes e perspectivas | responsável do Coletivo e Pessoa solicitante |
| nós materializados | pedido e resposta na perspectiva da Pessoa |
| nós apenas contratados | operação do responsável e retomada de análise |
| transições validadas | estados apresentados à Pessoa pela UXA-067 |
| transições não validadas como conjunto | origem da decisão e retorno à fila operacional |
| interrupção por lacuna | Visão Geral do Responsável e gestão de solicitações ausentes |
| conclusão permitida | o retorno para a Pessoa está representado |
| conclusão proibida | declarar validada a operação do responsável |

### 2.4 Organização e Coletivo estabelecem relação

| Campo | Registro |
|---|---|
| finalidade | formar relação bilateral com autonomia e saída preservadas |
| participantes e perspectivas | Organização e Coletivo |
| nós materializados | nenhum fluxo bilateral específico |
| nós apenas contratados | proposta, avaliação, negociação, aprovação, relação ativa, revisão e saída |
| transições validadas | nenhuma como jornada bilateral integrada |
| transições não validadas como conjunto | todas as etapas da relação |
| interrupção por lacuna | início do fluxo bilateral |
| conclusão permitida | o contrato UXA-019 define responsabilidades e limites |
| conclusão proibida | afirmar existência de interface ou fluxo operacional bilateral |

### 2.5 Organização publica oportunidade e Pessoa acessa

| Campo | Registro |
|---|---|
| finalidade | publicar oportunidade e permitir consulta pela Pessoa |
| participantes e perspectivas | Organização publicadora e Pessoa visitante |
| nós materializados | cadastro, superfícies de descoberta e detalhe |
| nós apenas contratados | efeitos externos após o destino identificado |
| transições validadas | cadastro e detalhe nos respectivos pacotes |
| transições não validadas como conjunto | publicação até consumo em todas as superfícies e efeitos externos |
| interrupção por lacuna | após o destino ou ação externa |
| conclusão permitida | as superfícies existentes possuem validação local |
| conclusão proibida | declarar o ciclo completo da oportunidade validado |

### 2.6 Sobreposição comercial identificada

| Campo | Registro |
|---|---|
| finalidade | permitir promoção identificada sem comprar autoridade, legitimidade ou reputação |
| participantes e perspectivas | Organização anunciante e Pessoa exposta; Opportunity Boost como camada comercial |
| nós materializados | 46 referências |
| nós apenas contratados | regras econômicas e de governança dos pacotes de origem |
| transições validadas | 36 referências validadas conforme pacotes |
| transições não validadas como conjunto | 10 estados residuais e integração completa com superfícies orgânicas |
| interrupção por lacuna | estados residuais sem validação |
| conclusão permitida | a camada comercial é identificada e separada da autoridade orgânica |
| conclusão proibida | tratar publicidade como participante, reputação ou recomendação |

## 3. Critério de completude

Um cenário só poderá ser marcado como completo quando todos os seus nós, transições, autoridades, dados, retornos, estados de exceção e pontos de saída estiverem documentados e funcionalmente validados como conjunto.

## 4. Estado vigente

A UXA-074 aprovou os seis cenários como hipóteses documentais governadas e limitadas pela evidência. A UXA-075 promove este documento para `active` nesse escopo.

O status `active` não transforma qualquer cenário em jornada completa nem executável.
