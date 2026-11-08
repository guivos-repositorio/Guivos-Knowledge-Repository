---
title: Grafo Vivo — Decisão da Direção CT-01 e CT-02 — Reconhecimento e Contratos Formais
status: direction_approved_scoped_conceptual_decision
version: 0.1.0
owner: Direção da Guivos
last_updated: 2026-11-08
normative: false
maturity: conceptual_registry_reconciliation_approved_pending_formalization
---

# Grafo Vivo — Decisão da Direção CT-01 e CT-02

> **Aprovação expressa da Direção nesta conversa: “de acordo, segue”**, em resposta à solicitação de **aprovação conceitual de CT-01 e CT-02** nos termos recomendados: reconhecer a responsabilidade distinta no **planejamento de reconciliação do Surface Registry** e reconhecer a **necessidade de contratos formais de entrada e retorno no Transition Registry**, **sem atribuir novos IDs nem modificar automaticamente os registros normativos**.

## 1. Decisões com alcance aprovado

### CT-01 — Responsabilidade distinta e Surface Registry

**Aprovado conceitualmente:** planejar o reconhecimento formal e rastreável da responsabilidade funcional distinta **Grafo Vivo expandido** na arquitetura de superfícies da Jornada da Pessoa, sem absorção por PER-008 e sem apropriação de PER-010/011/012.

**Não aprovado por este ato:** atribuir identificador de superfície, criar entrada oficial no Surface Registry, definir maturidade formal do destino sem análise, alterar PER-008 ou publicar.

A análise preliminar do Surface Registry `GKR-JOURNEY-SURFACE-REGISTRY-001` v0.36.22 registra **GKR-SURF-PER-008 — Tela Hoje**, como superfície validada, enquanto `GKR-SURF-PER-010/011/012` dispõem de contratos especializados. Não existe no trecho de Jornada da Pessoa examinado um registro dedicado do Grafo Vivo; **a aprovação de CT-01 não equivale à criação dele**.

### CT-02 — Contratos formais de entrada e retorno

**Aprovado conceitualmente:** reconhecer a necessidade de **contratos formais próprios** para os dois sentidos da passagem funcional entre PER-008/Hoje e o destino Grafo Vivo, com precondições, origem/destino, contexto mínimo, versão, escolha voluntária, saída neutra, recuperação e idempotência.

**Não aprovado por este ato:** criação/numeração de TRNs, lançamento no Transition Registry, validação contratual ou implantação.

O Transition Registry `GKR-JOURNEY-TRANSITION-REGISTRY-001` v0.29.26 preserva `TRN-007` (PER-007 → PER-008) e `TRN-008..013` (Hoje ↔ PER-010/011/012). **Nenhum desses contratos existentes passa a apontar para o Grafo Vivo.**

## 2. Matriz focal de reconciliação — sem alterações em fontes vigentes

| Fonte/tema | Situação reconhecida | Reconciliação a instruir | Ato não autorizado |
| --- | --- | --- | --- |
| PER-008 — Hoje Master v0.1.0 | Síntese, primeira entrada e retorno, sem novo domínio absorvido | Verificar o menor ponto de acesso contextual, opcional, também no primeiro Hoje quando elegível | Alterar conteúdo/competência do Master |
| Surface Registry v0.36.22 | PER-008 validada; PER-010/011/012 especializadas; destino Grafo Vivo não formalizado | Preparar proposta de representação de responsabilidade distinta, com escopo, estado e autoridade competente | Criar GKR-SURF/PER-ID ou linha oficial |
| Transition Registry v0.29.26 | TRN-007 e TRN-008..013 regem outros pares | Preparar **duas minutas próprias de contrato**, entrada e retorno, com origem/destino ainda sem ID próprio | Criar TRN, redirecionar TRN existente, declarar validação |
| Orquestração da Jornada v0.4.0 | Coordena continuidade sem substituir Masters/Registries | Examinar compatibilidade de handoff e recuperação com mesma responsabilidade expandida | Instituir novo fluxo operativo tacitamente |
| PER-007 / Privacidade | Revisão e persistência/personalização independentes | Discriminar uso de sessão, memória, versão, revogação e finalidade | Presumir consentimento, reter/transmitir dados |
| GIA / PAS-001 | Intelligence compreende; domínios mantêm fonte de verdade | Delimitar grafo como projeção/contexto, sem efeitos materiais em objetivos/passos/evolução | Autorizar automação de objetos ou persistência |
| Modos Explorar/Escutar/Conversar | São modos internos da responsabilidade Grafo Vivo | Definir estados locais e passagem de foco/versão | Criar TRNs por alternância de modo |

## 3. Proposta de instrução dos contratos — campos mínimos

| Campo candidato | Entrada: Hoje → Grafo Vivo | Retorno: Grafo Vivo → Hoje |
| --- | --- | --- |
| Origem funcional | PER-008 — Hoje | Destino expandido do Grafo Vivo (a formalizar) |
| Destino funcional | Grafo Vivo — responsabilidade distinta (a formalizar) | PER-008 — Hoje |
| Gatilho | Ação consciente da Pessoa | Ação explícita de retorno ou recuperação segura |
| Elegibilidade | Contexto legítimo suficiente, inclusive no primeiro Hoje; sem histórico obrigatório | Sessão e autorização verificáveis; saída não condicionada a concluir atividade |
| Contexto mínimo | Referências permitidas, finalidade, versão, proveniência e escolhas pertinentes | Reconsulta do estado canônico de Hoje; referência mínima de navegação quando permitida |
| Efeitos materiais | Nenhum por simples entrada | Nenhum por simples retorno |
| Interrupção | Cancelamento seguro; não persistir nem narrar por padrão | Parar operação não autorizada; não guardar edição efêmera automaticamente |
| Concorrência | Verificação de versão antes de renderizar informação | Não exibir estado antigo como atualizado |
| Falha e idempotência | Retries não duplicam autorizações ou eventos materiais | Falha honesta e retorno recuperável sem efeito duplicado |
| Autoridade | A deliberar na formalização do Registry | A deliberar na formalização do Registry |

Esta tabela é **minuta de instrução** e não torna nenhum campo contrato normativo ou API implementável. A aceitação de CT-01/CT-02 não resolve a atribuição do ID do destino; não há como formalizar par identificado sem decisão posterior sobre sua representação.

## 4. Gates e próximas decisões

1. **Representação do destino**: confrontar alternativas de representação no Surface Registry, demonstrando competência, sem escolher identificador prematuramente.
2. **Duas minutas de passagem e retorno**: revisar pré-condições/efeitos e compatibilidade com os estados da Jornada e com o Registry vigente.
3. **Dados e consentimento**: verificar finalidades, escolha de sessão, retenção, revogação, proveniência e acessibilidade com autoridades aplicáveis.
4. **Ato normativo específico**, se e quando aprovado: somente então alterar Master/Orquestração/Registries e considerar novos IDs.
5. **Ato operacional específico**, posterior: auditoria de leitura do Replit, desenvolvimento, testes e publicação, separadamente autorizados.

A Direção é decisora final deste estudo; a aprovação é emitida nesta conversa e refletida no GKR/GitHub para rastreabilidade. A ausência de revisor GitHub nomeado não bloqueia deliberações da Direção; não simular parecer externo.

## 5. Estado

- **CT-01 — planejamento do reconhecimento em Surface Registry:** aprovado conceitualmente; nenhuma entrada criada.
- **CT-02 — necessidade de contratos formais próprios de entrada e retorno:** aprovada conceitualmente; nenhuma TRN criada.
- **Alternativa B, competência distinta, entrada voluntária, retorno neutro, três modos internos, acesso no primeiro Hoje:** preservados.
- **Surface Registry, Transition Registry, Master PER-008, Orquestração:** inalterados.
- **PR #730:** rascunho, sem merge ou publicação.
- **Jornada da Pessoa — Replit:** não inspecionada ou modificada por esta aprovação.

**Próximo exame recomendado:** comparar opções de representação da responsabilidade distinta no Surface Registry e estabelecer critérios de suficiência para que as duas minutas de handoff possam ser submetidas à Direção, sem alteração normativa imediata.
