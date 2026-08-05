---
id: GKR-JOURNEY-SURFACE-REGISTRY-001
title: Registro Granular de Superfícies e Estados
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Superfícies e Estados

## 1. Finalidade

Este registro atribui identificadores estáveis às superfícies, estados e responsabilidades conhecidas nas Jornadas Integradas.

Uma entrada pode representar:

- tela ou estado materializado;
- responsabilidade contratada ou programada ainda sem superfície específica;
- ausência conhecida necessária para continuidade.

A inclusão não altera maturidade, não cria interface e não fecha lacuna.

## 2. Convenções

| Valor | Uso |
|---|---|
| `—` | nenhuma referência específica disponível |
| `ausente` | responsabilidade conhecida sem materialização necessária |
| `não examinado` | integração não avaliada como conjunto |
| `parcial` | parte da continuidade possui evidência e parte permanece sem cobertura |
| `local` | validação limitada ao pacote de origem |

## 3. Pessoa — início, compreensão e recorrência

| ID | Perspectiva | Família | Superfície ou estado | Canal | Maturidade | Autoridade | Materialização | Validação | Entrada conhecida | Saída conhecida | Continuidade | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | visitante público | início protegido | Home pública | público | validado | UXA-020 | UXA-022 | UXA-021 | acesso público | entrada protegida | parcial | integração ponta a ponta |
| GKR-SURF-PER-002 | Pessoa | início protegido | entrada protegida | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | Home pública | escolha de modalidade | parcial | continuidade entre pacotes |
| GKR-SURF-PER-003 | Pessoa | início protegido | escolha de modalidade | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | entrada protegida | expressão guiada | parcial | ligação explícita com UXA-068 |
| GKR-SURF-PER-004 | Pessoa | expressão guiada | expressão por texto ou voz | protegido | validado | UXA-068 | UXA-068 | UXA-069 | escolha de modalidade | inventário e autorização | parcial | integração com inventário |
| GKR-SURF-PER-005 | Pessoa | início protegido | inventário dos conteúdos e autorização | protegido | validado | UXA-023 | UXA-034 | UXA-035 | expressão guiada | processamento | parcial | transição integrada entre pacotes |
| GKR-SURF-PER-006 | Pessoa | compreensão inicial | processamento visível | protegido | validado | UXA-023 | UXA-036 | UXA-037 | inventário autorizado | compreensão inicial | local | continuidade ponta a ponta |
| GKR-SURF-PER-007 | Pessoa | compreensão inicial | compreensão inicial revisável | protegido | validado | UXA-023 | UXA-036 | UXA-037 | processamento | decisão sobre persistência | parcial | ligação com experiência recorrente |
| GKR-SURF-PER-008 | Pessoa autenticada | experiência recorrente | Tela Hoje | protegido | validado | UXA-002 | UXA-006 | UXA-010 | compreensão e gates próprios | continuidades recorrentes | não examinado | reconciliação com compreensão inicial |

## 4. Pessoa em Coletivos

| ID | Perspectiva | Família | Superfície ou estado | Canal | Maturidade | Autoridade | Materialização | Validação | Entrada conhecida | Saída conhecida | Continuidade | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-101 | visitante | descoberta | Explorar Coletivos | móvel | validado | UXA-056 | UXA-060 | UXA-061 | navegação recorrente | Resultados de Busca | parcial | continuidade entre famílias |
| GKR-SURF-PER-102 | visitante | descoberta | Resultados de Busca | móvel | validado | UXA-056 | UXA-060 | UXA-061 | Explorar Coletivos | Perfil Público | parcial | caminhos alternativos consolidados |
| GKR-SURF-PER-103 | visitante | presença pública | Perfil Público do Coletivo | móvel | validado | UXA-056 | UXA-062 | UXA-063 | busca ou acesso direto | revisão e solicitação | parcial | handoff para participação |
| GKR-SURF-PER-104 | solicitante | participação | revisão e solicitação | móvel | validado | UXA-056 | UXA-064 | UXA-065 | Perfil Público | envio da solicitação | parcial | destino operacional do Coletivo |
| GKR-SURF-PER-105 | solicitante | participação | Solicitação Pendente | móvel | validado | UXA-056 | UXA-066 | UXA-067 | solicitação enviada | retorno, cancelamento ou decisão | parcial e assimétrica | visão do responsável ausente |
| GKR-SURF-PER-106 | participante | continuidade | Meus Coletivos | não definido | não iniciado | UXA-059 | — | — | vínculo formado | Central de Atualizações | ausente | superfície e transições |
| GKR-SURF-PER-107 | participante | continuidade | Central de Atualizações | não definido | não iniciado | UXA-059 | — | — | Meus Coletivos | Início do Participante | ausente | superfície e transições |
| GKR-SURF-PER-108 | participante | operação interna | Início do Participante | não definido | reformulação pendente | UXA-059 | referência anterior não promovida | — | vínculo e atualizações | experiência interna | ausente | reformulação e continuidade |

## 5. Coletivo

| ID | Perspectiva | Família | Superfície ou responsabilidade | Canal | Maturidade | Autoridade | Materialização | Validação | Entrada conhecida | Saída conhecida | Continuidade | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COL-001 | visitante e responsável | presença pública | Visão Geral ou presença pública existente | público/protegido | materializado | UXA-014; UXA-056 | UXA-016 e referências relacionadas | UXA-018; UXA-063 no escopo aplicável | criação ou acesso público | descoberta e participação | parcial | separação entre vista pública e operação |
| GKR-SURF-COL-002 | responsável | operação | Visão Geral do Responsável | protegido | não iniciado | UXA-059 | — | — | autoridade de representação | solicitações, vínculos e operação | ausente | superfície do responsável |
| GKR-SURF-COL-003 | responsável | participação | gestão de solicitações | protegido | programado | UXA-056; UXA-059 | apenas retornos na visão da Pessoa | UXA-067 na perspectiva da Pessoa | solicitação recebida | pedir informação, aprovar, recusar ou expirar | ausente na origem | operação bilateral |
| GKR-SURF-COL-004 | responsável | vínculos | participantes e vínculos | protegido | programado | UXA-059 | — | — | vínculo formado | gestão, saída ou contestação | ausente | continuidade interna |
| GKR-SURF-COL-005 | responsável | comunicação | comunicação oficial | protegido | programado | UXA-058; UXA-059 | — | — | vínculo e autoridade | atualizações aos participantes | ausente | superfície e regras operacionais |
| GKR-SURF-COL-006 | responsável | operação | atividades, consultas e decisões | protegido | programado | UXA-059 | parcial ou dispersa | — | governança interna | resultados e próximas decisões | não examinado | matriz operacional integrada |
| GKR-SURF-COL-007 | responsável | proteção | proteção e moderação | protegido | contratado | UXA-058 | cobertura parcial | — | evento protegido | decisão ou encaminhamento | não examinado | fluxo protegido completo |
| GKR-SURF-COL-008 | responsável | relações | relações institucionais | protegido | contratado | UXA-019 | — | — | proposta institucional | negociação e decisão bilateral | ausente | relação Organização–Coletivo |

## 6. Organização

| ID | Perspectiva | Família | Superfície ou responsabilidade | Canal | Maturidade | Autoridade | Materialização | Validação | Entrada conhecida | Saída conhecida | Continuidade | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-ORG-001 | representante institucional | visão geral | Visão Geral da Organização | protegido | validado | UXA-014 | UXA-015 | UXA-017 | identidade e autoridade | oportunidades, relações e resultados | parcial | matriz institucional completa |
| GKR-SURF-ORG-002 | representante institucional | oportunidades | cadastro de oportunidade | protegido | validado | UXA-004 | UXA-008 | UXA-013 | autoridade institucional | publicação | parcial | integração com descoberta |
| GKR-SURF-ORG-003 | representante institucional | oportunidades | oportunidade publicada | público | materializado | UXA-004 | UXA-007 e superfícies de descoberta | UXA-012 no detalhe | cadastro concluído | consulta pela Pessoa | parcial | ciclo completo de publicação |
| GKR-SURF-ORG-004 | representante institucional | relações | proposta de relação com Coletivo | protegido | contratado | UXA-019 | — | — | decisão institucional | avaliação pelo Coletivo | ausente | superfície bilateral |
| GKR-SURF-ORG-005 | representante e responsável | relações | avaliação e negociação bilateral | protegido | contratado | UXA-019 | — | — | proposta | aprovação, recusa ou ajuste | ausente | materialização bilateral |
| GKR-SURF-ORG-006 | representante e responsável | relações | relação ativa e revisão | protegido | contratado | UXA-019 | — | — | aprovação bilateral | renovação, ajuste, pausa ou encerramento | ausente | operação bilateral |
| GKR-SURF-ORG-007 | representante institucional | evidências | resultados e evidências institucionais | protegido | indeterminado | referências dispersas | — | — | atividades e compromissos | revisão institucional | não examinado | matriz visual institucional |

## 7. Camada comercial identificada

| ID | Perspectiva | Família | Superfície ou estado | Canal | Maturidade | Autoridade | Materialização | Validação | Entrada conhecida | Saída conhecida | Continuidade | Lacuna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COM-001 | anunciante | Opportunity Boost | configuração do fluxo do anunciante | protegido | materializado | UXA-038 | UXA-040 | UXA-041 | intenção de promover | campanha configurada | parcial | integração econômica completa |
| GKR-SURF-COM-002 | Pessoa exposta | Opportunity Boost | cartão patrocinado e explicação | público/protegido | validado | UXA-038 | UXA-042 | UXA-043 | entrega identificada | detalhe, explicação ou retorno orgânico | parcial | integração com superfícies orgânicas |
| GKR-SURF-COM-003 | Pessoa exposta | Opportunity Boost | estados patrocinados de lista e mapa | público/protegido | validado | UXA-038 | UXA-044 | UXA-045 | descoberta em lista ou mapa | detalhe ou explicação | parcial | continuidade transversal |
| GKR-SURF-COM-004 | anunciante | Opportunity Boost | gestão da campanha ativa | protegido | materializado | UXA-038 | UXA-046 | validação correspondente não consolidada nesta seção | campanha ativa | ajuste, pausa ou encerramento | parcial | validação residual |
| GKR-SURF-COM-005 | anunciante e Pessoa exposta | Opportunity Boost | 10 estados residuais | diversos | materializado | UXA-038 | UXA-047 a UXA-054 conforme pacote | — | estados anteriores | continuidades específicas | não examinado | validação dos estados residuais |

## 8. Regras de uso

- o registro aponta para fontes; não copia artefatos canônicos;
- maturidade pertence à referência registrada, não à jornada inteira;
- validação local não comprova entrada ou saída integrada;
- responsabilidades sem interface permanecem registradas como ausência;
- nenhuma contagem deve ser usada para declarar completude ponta a ponta;
- o registro permanece `draft` até validação funcional específica.
