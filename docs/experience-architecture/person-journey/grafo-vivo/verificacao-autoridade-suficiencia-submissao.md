---
title: Grafo Vivo — Verificação de Autoridade e Suficiência Documental para Submissão
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: governance_pre_submission_diagnostic
---

# Grafo Vivo — Verificação de Autoridade e Suficiência Documental para Submissão

> **Verificação documental condicionada, sem submissão, parecer de autoridade nem adjudicação.** Não aprova alternativa A/B/C, alteração normativa, Design, integração, Replit, teste, merge ou publicação.

## 1. Objeto e futuro local de materialização

Verificar a competência e suficiência das fontes para submeter a **Consulta Focal UX/Journey (AF-01/02/03/10)**. Registrar o alinhamento à intenção da direção de **avaliar a implantação posterior na dashboard da Jornada da Pessoa no workspace Replit `@guivos/Jornada-da-Pessoa` apenas quando houver material e autorizações suficientes**. O apontamento do destino é referência de planejamento, **não autorização para acessar/modificar o workspace**.

A imagem da interface disponibilizada pela direção nesta conversa (08/11/2026) mostra como baseline visual informativa a tela **“Composição da Pessoa”** com:
- área **Meu Contexto** com **Chat/Histórico** e composição textual ou por áudio/anexos;
- área **Compreensão contextual**, com indicador segmentado de clareza/avaliação e distinção entre registros enviados e compreensão validada;
- abas **Visão geral** e **Compreensão**;
- estado inicial sem compreensão por IA e contagens factuais zeradas;
- organização de dois painéis, com contexto à esquerda e inteligência à direita.

**Limites da evidência visual:** a imagem não comprova código, comportamento operacional, conectividade com provedores, responsividade mobile, permissões, memória implementada ou capacidade de receber o Grafo Vivo. O baseline visual não deve ser confundido com aprovação para reconstrução da tela.

## 2. Fontes normativas verificadas nesta etapa

| Fonte | Documento/versão observada | Regra relevante | Efeito para a consulta |
| --- | --- | --- | --- |
| Conhecimento oficial | `ADR-001` — GKR como fonte única da verdade (aprovada) | Conteúdo aprovado versionado no GKR; alterações relevantes rastreáveis | A consulta deve preservar proveniência e não assumir que o PR é Canon |
| Arquitetura do Conhecimento | `ADR-006` — Guivos Knowledge Architecture (aprovada) | GKA governa conhecimento e sua maturação, **não cria produtos, não substitui arquitetura ou implementação técnica** | Não delegar a GKA decisão funcional de UX nem implantação |
| Pipeline de consolidação | `A2-METHOD-001` v2.0.0, `normative: true` | Evidência → hipótese → consolidação → readiness → validação → auditoria → Canon; hipóteses fora da Canon; documentação ≠ implementação | Estudos do Grafo Vivo continuam hipóteses/diagnósticos até validação aplicável |
| Auditoria Arquitetural | `GEA-AUDIT-001` v2.0.0, `normative: true` | Auditoria verifica integridade, **não cria verdade por inferência**; baseline requer validação e ausência de achados graves | Parecer de auditoria não substitui ato de domínio |
| Superfícies | `GKR-JOURNEY-SURFACE-REGISTRY-001` v0.36.22 | PER-008 tem responsabilidade de Hoje; PER-010/011/012 têm responsabilidades especializadas | Não criar nova competência do Grafo Vivo por rótulo de interface |
| Transições | `GKR-JOURNEY-TRANSITION-REGISTRY-001` v0.29.26 | TRN-007 e TRN-008..013 têm origem/destino específicos; sem links diretos entre PER-010/011/012 | Entrada/retorno expandido carece de decisão de Registry quando aplicável |
| Orquestração | `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001` v0.4.0, `normative: true` | Governança da continuidade e do comportamento ponta a ponta, sem substituir Masters/Registries/Planos | Consulta deve confrontar a responsabilidade transversal |
| PER-007 e PER-008 | Documentos Mestres vigentes | Compreensão inicial revisável, persistência e personalização independentes; Hoje como síntese | Entrada no Grafo não concede novas autorizações |

### Nota sobre atribuição institucional

As fontes consultadas **identificam a área/arquitetura responsável**, mas não demonstram de forma suficiente **qual pessoa, órgão ou instância nomeada possui poderes conclusivos** para adjudicar alteração de Surface Registry, Transition Registry e escopo de PER-008 em conjunto. O ponto AF-10 permanece **aberto**. Não atribuir competência automática à autoria de um documento, ao GKR, à GKA nem ao agente que elaborou esta minuta.

## 3. Resultado focal para AF-01/AF-02/AF-03/AF-10

| Quesito | Evidência suficiente para formular pergunta? | Evidência suficiente para decidir? | Pendência |
| --- | --- | --- | --- |
| **AF-01 — Escopo de Hoje** | **Sim**, Master PER-008 e Orquestração são fontes identificáveis | **Não** | Delimitação competente entre explicação leve, narração e exploração expandida |
| **AF-02 — Superfícies** | **Sim**, Surface Registry e Mestres especializados | **Não** | Reconhecer se há estado interno cabível ou responsabilidade adicional |
| **AF-03 — Transições** | **Sim**, TRN-007..013 e limites expressos | **Não** | Determinar se qualquer opção implica novo handoff/retorno e seu instrumento |
| **AF-10 — Autoridade do ato** | **Parcial**, framework e donos documentais identificados | **Não** | Confirmar instância que pode emitir parecer, decidir e alterar as fontes |

**Parecer diagnóstico:** há material para **revisão da minuta e identificação do destinatário**, mas **não há evidência suficiente para afirmar submissão institucional válida ou competência adjudicatória individualizada**.

## 4. Instrumentos diferenciados

| Instrumento possível | Pode servir a | Não equivale a |
| --- | --- | --- |
| Minuta/consulta focal (presente) | Organizar perguntas, alternativas, fontes e limites | Manifestação oficial |
| Parecer de compatibilidade por autoridade competente | Interpretar o que as fontes vigentes permitem, se houver competência | Mudança automática de Registry |
| Decisão expressa de domínio/arquitetura | Definir objeto, alcance, autoridade e condições sob instrumento válido | Autorização automática de tecnologia ou desenvolvimento |
| Reconciliação de Masters/Registries | Atualizar corpus somente mediante ato e validação específicos | Liberação operacional tácita |
| Readiness/validação/auditoria | Verificar suficiência, coerência, rastreabilidade e estado documental | Evidência de funcionalidade testada |
| Autorização operacional separada | Liberar escopo específico de Design, Replit, testes ou implementação, se emitida | Seleção implícita por estudo conceitual |

Os nomes dos instrumentos são **descrições analíticas**, sujeitos ao regime concreto de governança.

## 5. Critério de suficiência para futura implantação na dashboard

A intenção da direção é **começar a implantação quando o material for suficiente**; traduz-se aqui em **gates a verificar**, não em autorização antecipada ou agendamento.

| Gate local | Evidência mínima antes de solicitar implantação | Status |
| --- | --- | --- |
| I-01 — Enquadramento funcional | Ato competente sobre localização A/B/C, sem conflito com PER-008 | Aberto |
| I-02 — Surface/Transition | Competências e handoffs admitidos e conciliados, se exigidos | Aberto |
| I-03 — Intelligence/semântica | Papel de explicação e limites de domínio preservados | Aberto |
| I-04 — Dados/memória | Finalidades, sessão, persistência, personalização, correção e retenção adjudicadas | Aberto |
| I-05 — Voz/fornecedores | Fluxos mínimos, risco, contratos/retenção e segurança de Grok/STT examinados | Aberto |
| I-06 — Acessibilidade | Conteúdo equivalente por texto, voz e visualização, incluindo falhas | Aberto |
| I-07 — Contrato de integração | Responsabilidades, versão, falhas e dados necessários no app publicado especificados | Aberto |
| I-08 — Auditoria do Replit | Inspeção do código/telas/serviços, fluxo atual, mobile e regressões sem alterar produto | **Não executada** |
| I-09 — Autorização operacional | Aprovação expressa e limitada de Design/testes/implementação | **Não emitida** |

I-xx são códigos internos desta tabela, **não novos IDs oficiais**. Se uma etapa futura autorizar auditoria de leitura do Replit, ela deve registrar código efetivo, superfícies, APIs existentes e compatibilidade com o app **antes** de sugerir mudanças.

## 6. Achado adicional: tratamento do menu do GKR

O comentário de governança existente em `mkdocs.yml` declara que documentos `draft/proposed` **somente devem aparecer no MENU quando autoridade superior corrente os declarar expressamente fonte operacional**. A branch em estudo atualmente possui entradas de navegação para os estudos `conceptual_study` do Grafo Vivo.

**Achado de reconciliação:** tal escolha de menu precisa ser revisada **antes de qualquer merge ou publicação**, pois o PR é rascunho e os documentos não são operacionais. Esta verificação **não declara que exista autorização superior** nem modifica o menu nesta etapa. O presente estudo é ligado apenas pelo índice `read-first.md` para não acrescentar nova entrada preliminar ao menu.

## 7. Encaminhamento sugerido, sem envio da consulta

1. Submeter **a verificação de competência AF-10** à governança competente para identificar a instância/ato formal aplicável.
2. Após identificação, encaminhar a **Consulta Focal AF-01/02/03/10** por canal autorizado, registrando autoria, escopo e resposta verificáveis.
3. Em caso de decisão expressa, confrontar efeitos com Masters/Registries, GPA-006/GIA-COG-001, PAS-001 e autoridades de dados, antes de qualquer reconciliação.
4. Validar o tratamento de documentação candidata no menu e os controles de baseline do GKR.
5. Só então, mediante autorização específica, realizar **auditoria técnica de leitura** do workspace Replit e planejar a incorporação por incrementos e dados sintéticos.
6. Solicitar autorização própria de implantação; não confundir a intenção condicional da direção com liberação atual.

## 8. Estado e parecer

- Consulta AF-01/02/03/10: **minuta, sem submissão formal ou parecer recebido**.
- Identificação da instância apta a adjudicar: **não resolvida**.
- Alternativas de localização A/B/C: **nenhuma selecionada**; B segue prioritária para exame.
- Baseline visual informado pela direção: **registrado como referência descritiva, não auditoria de código**.
- Replit Jornada da Pessoa: **nenhum acesso, alteração, teste ou publicação executados nesta etapa**.
- Menu do GKR: **achado de governança aberto para reconciliação antes de merge**.
- PR #730: **ramo documental em rascunho, sem merge ou publicação**.

**Conclusão:** material suficiente para continuar preparando a deliberação; insuficiente para declarar adjudicação funcional, prontidão operacional ou autorização de implantação.
