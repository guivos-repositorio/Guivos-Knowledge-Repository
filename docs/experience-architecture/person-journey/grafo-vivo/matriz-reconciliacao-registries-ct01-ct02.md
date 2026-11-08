---
title: Grafo Vivo — Matriz Focal de Reconciliação dos Registries para CT-01 e CT-02
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: documentary_reconciliation_candidate_pending_direction_adjudication
---

# Grafo Vivo — Matriz Focal de Reconciliação dos Registries para CT-01 e CT-02

> **Diagnóstico documental, sem efeito normativo.** A Direção aprovou CT-01 (planejar reconhecimento da responsabilidade distinta no Surface Registry) e CT-02 (necessidade de contratos formais próprios de entrada e retorno). **Não autorizou** a alteração dos Registries, criação de PER/TRN-IDs, validação de transições, implementação ou publicação. Este exame delimita as opções de representação e os requisitos mínimos para decisão posterior.

## 1. Baseline examinado

| Documento | Versão vigente examinada | Evidência relevante |
| --- | --- | --- |
| Surface Registry — `GKR-JOURNEY-SURFACE-REGISTRY-001` | **v0.36.22** | `GKR-SURF-PER-008` é Tela Hoje validada; `GKR-SURF-PER-010/011/012` são especializadas, com seus contratos |
| Transition Registry — `GKR-JOURNEY-TRANSITION-REGISTRY-001` | **v0.29.26** | `TRN-007` PER-007 → PER-008 e `TRN-008..013` para PER-008 ↔ PER-010/011/012, validadas documentalmente em seus limites |
| Master PER-008 — `GKR-UX-PER008-MASTER-001` | **v0.1.0** | Hoje é síntese, com variantes de primeira entrada e retorno; não presume histórico nem absorve Objetivos, Próximos Passos e Evolução |
| Orquestração — `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001` | **v0.4.0** | Coordena a continuidade da Jornada sem substituir os Masters ou os Registries |
| [Decisão CT-01/CT-02](decisao-direcao-ct01-ct02.md) | **08/11/2026** | Autoriza planejamento da representação da responsabilidade distinta e exige dois contratos formais próprios, sem aprovação de alterações normativas |
| [Contrato funcional candidato](contrato-funcional-candidato-passagem-retorno.md) | **v0.1.0** | Delimita elegibilidade, contexto mínimo, versão, retorno, falha, revogação e idempotência para exame |

**Constatação:** as fontes vigentes não contêm destino formal identificado como Grafo Vivo, nem contratos oficiais para o par Hoje ↔ Grafo Vivo. É incorreto declarar esses contratos integralmente validados porque outras transições de Hoje receberam validação.

## 2. CT-01 — três formas de representação documental

| Opção para exame | Descrição | Vantagem | Limite ou incompatibilidade |
| --- | --- | --- | --- |
| **R1 — Estado interno de PER-008** | Grafo expandido como estado ou aba de Hoje | Reutilizaria competência existente | **Incompatível com a decisão vigente** de responsabilidade funcional distinta, salvo nova adjudicação expressa |
| **R2 — Responsabilidade distinta reconhecida no Registry** | Destino com contrato, autoridade, maturidade e fronteiras próprios, sem impor layout visual separado | **Compatível** com Alternativa B, CT-01 e preservação do Master de Hoje | Depende de decisão posterior sobre modo de registro, identificação oficial, owner e maturidade; não pode ser incluído tacitamente |
| **R3 — Responsabilidade distribuída nas superfícies especializadas** | Explorar/Escutar/Conversar espalhados entre PER-010/011/012 | Aproveitaria superfícies de domínio | Contraria o destino expandido integrado com responsabilidade distinta e fragmenta a compreensão governada; exigiria reabrir decisão anterior |

**Parecer técnico candidato:** **R2** é a representação mais coerente com as decisões já tomadas pela Direção. **Não é aprovação para criar linha, ID ou superfície registrada agora.** Uma responsabilidade distinta pode ser apresentada em uma composição visual integrada; identidade funcional e layout visual não são a mesma coisa.

### 2.1 Elementos necessários a uma futura proposta de entrada no Surface Registry

1. **Definição inequívoca da responsabilidade:** exploração multimodal contextual, sem poder criar ou confirmar Objetivos, Próximos Passos, Evolução ou consentimento.
2. **Autoridade e owner:** responsáveis por contrato de experiência, cognição, segurança, privacidade e fonte de verdade; a Direção decide os limites de competência.
3. **Participante e proteção:** Pessoa autenticada, com conteúdo restrito à finalidade e às escolhas legítimas.
4. **Entrada e retorno:** Hoje como origem e destino do retorno, sem utilizar TRN pré-existente para finalidade distinta.
5. **Maturidade honesta:** proposta não validada/documento candidato; não usar “validado” enquanto não houver ato e evidências apropriados.
6. **Referências normativas:** Master PER-008, Orquestração, PER-007, PER-010/011/012, PAS-001, GIA-COG-001, GPA-006 e Registries.
7. **Identificação:** avaliar necessidade e regra de alocação somente em momento de formalização autorizado; **nenhum identificador é proposto neste dossiê**.

## 3. CT-02 — suficiência de dois contratos formais próprios

A exigência aprovada é de **dois sentidos de passagem**, não de duas novas telas nem de transição entre todas as modalidades.

| Cláusula mínima | Entrada Hoje → Grafo Vivo | Retorno Grafo Vivo → Hoje | Estado atual |
| --- | --- | --- | --- |
| Origem/destino | PER-008 → responsabilidade distinta a formalizar | Responsabilidade distinta → PER-008 | **Conceito aprovado; destino sem identificação formal** |
| Gatilho | Escolha afirmativa da Pessoa | Saída explícita ou recuperação segura | **Diretriz aprovada** |
| Elegibilidade | Contexto legítimo suficiente; pode ocorrer no primeiro Hoje | Saída não depende de conclusão da análise ou conversa | **Diretriz aprovada; critérios técnicos pendentes** |
| Contexto mínimo | Escopo/finalidade/referência de versão e proveniência elegível | Reconsulta do estado canônico e referência mínima permitida | **Envelope candidato; sem esquema de dados** |
| Consentimento/dados | Abertura não habilita retenção, personalização nem gravação | Retorno não salva conteúdo efêmero por padrão | **Fronteira aprovada; política detalhada pendente** |
| Efeito de domínio | Nenhuma criação/aceitação/conclusão por entrar | Nenhuma confirmação de progresso ou alteração por retornar | **Neutralidade aprovada** |
| Revogação/versão | Não reutilizar dado ou projeção desautorizada; detectar divergências | Refletir estado vigente, sem representar versão antiga como atual | **Comportamento candidato; contrato de dados pendente** |
| Falha e idempotência | Repetição não concede permissões nem duplica efeito material | Saída recuperável; não declarar retorno concluído antes de confirmação | **Critérios a especificar e posteriormente validar** |
| Maturidade | Não validado | Não validado | **Sem TRN oficial** |

**Suficiência documental atual:** satisfaz a **diretriz conceitual** de dois sentidos separados e identifica cláusulas essenciais; **não satisfaz ainda os requisitos para declarar contratos operacionais ou Registries formalmente atualizados**.

### 3.1 Lacunas que impedem formalização imediata

- Destino ainda não representado oficialmente no Surface Registry, nem escolhido seu regime de identificação.
- Não há versão autorizada de contrato de dados e permissão de cada modalidade.
- Não foram adjudicados critérios mensuráveis/avaliáveis de elegibilidade por contexto e por finalidade.
- As regras operacionais de interrupção, expiração de sessão, concorrência, duplicidade e acessibilidade carecem de validação própria.
- Não foram aprovados contratos de voz, fornecedores externos, gravação ou persistência.
- Não há evidência de auditoria/compatibilidade do workspace Replit.

## 4. Impacto mínimo nas autoridades, caso haja aprovação futura

| Fonte | Exame/alteração potencial | Condição para alteração |
| --- | --- | --- |
| **Surface Registry** | Entrada para a responsabilidade distinta, com owner, maturidade e limites | Deliberação expressa sobre representação, identificação e competência |
| **Transition Registry** | Dois contratos distintos de entrada e retorno | Identificação formal do destino; aprovação específica dos handoffs e dos efeitos |
| **Master PER-008** | Eventual descrição do acesso opcional e do retorno neutro | Comprovar compatibilidade e autorizar alteração do Master, sem absorver Grafo Vivo |
| **Orquestração UX/UI** | Continuidade de contexto, falhas, interrupção, estado de retorno | Revisão autorizada que preserve hierarquia de autoridade |
| **PER-007 / PAS-001 / GIA / privacidade** | Não alterar por conveniência; confrontar dados, cognição e permissões | Decisões por autoridade pertinente, sem presumir novas permissões |
| **Replit — Jornada da Pessoa** | Nenhum efeito desta matriz | Auditoria e implementação dependerão de atos próprios e posteriores |

A matriz é **impact analysis**, não plano de edição automática nem minuta de commit em arquivos normativos.

## 5. Critérios para futura aceitação das minutas de handoff

Uma futura proposta poderá ser considerada pronta para **submissão à decisão normativa** quando apresentar conjuntamente:

1. Um destino funcional inequivocamente reconhecido, com fronteiras documentadas e maturidade correta.
2. Dois contratos distintos com origem, destino, pré-condição, gatilho, dados mínimos, efeito neutro e saída/retorno.
3. Confronto linha a linha com `TRN-007` e `TRN-008..013`, garantindo ausência de mudança silenciosa nos pares existentes.
4. Matriz de estados: primeiro Hoje, Hoje recorrente, contexto insuficiente, permissão revogada, erro de áudio, erro de grafo, contexto desatualizado e retorno sob falha.
5. Versão/proveniência e referência canônica demonstráveis, sem novo esquema de dados presumido.
6. Acessibilidade e fallback textual; sem obrigar a Pessoa a usar modalidade particular.
7. Separação comprovável entre informação temporária, fato confirmado, hipótese, persistência e personalização.
8. Autoridade pertinente e decisão expressa da Direção antes de qualquer atualização oficial.

Mesmo com esses critérios cumpridos, **prontidão documental não equivale a aprovação de implementação**.

## 6. Encaminhamento focal à Direção — sem adjudicação automática

**Recomendação R2 para aprovação em ato posterior:** reconhecer o Grafo Vivo como **responsabilidade distinta representável no Surface Registry**, sem impor nova tela visual, com maturidade inicialmente candidata e identificação oficial a tratar na etapa autorizada.

**Para CT-02:** manter os dois contratos formais próprios como exigência já aprovada, mas condicioná-los à identidade formal do destino, à reconciliação da autoridade de dados e à validação das regras de entrada/retorno. **Não reutilizar TRN-007..013.**

**Pedido de decisão sugerido à Direção:** aprovar **R2 como diretriz de representação documental**, sem criar entradas/IDs e sem alterar os Registries; na sequência, detalhar os itens de suficiência de CT-02 em dois contratos candidatos.

## 7. Limites

- Alternativa B, competência distinta, entrada/retorno, modalidades internas, acesso elegível no primeiro Hoje e CT-01/02: **já aprovados conceitualmente**.
- **R2 permanece recomendação**, não nova decisão da Direção.
- Sem criação de IDs, alteração de Masters, Orquestração ou Registries, Design operacional, testes, APIs, integração de fornecedores, inspeção/alteração do Replit, merge ou publicação.
- PR #730 continua rascunho; o índice único da seção preserva a proveniência de cada estudo.


## Atualização posterior — Diretriz R2 aprovada pela Direção (08/11/2026)

A Direção aprovou expressamente a **R2 como diretriz de representação da responsabilidade funcional distinta**, sem criar superfície ou ID no Registry. Ver [Decisão R2](decisao-direcao-r2.md). A expressão anterior “R2 permanece recomendação” e a solicitação de sua aprovação registram o **estado histórico anterior** a esta decisão. Foram também preparadas [duas minutas separadas de entrada e retorno](minutas-contratos-transicao-entrada-retorno.md), ainda candidatas, sem validação ou alteração normativa.
