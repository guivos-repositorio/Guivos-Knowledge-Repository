---
id: GKR-PENDING-WORK-20261017-001
title: Pendências Consolidadas — Retomada Pós-17-10-2026
status: informational
version: 1.0.0
owner: Guivos
last_updated: 2026-10-17
normative: false
---

# Pendências Consolidadas — Retomada Pós-17/10/2026

> **Registro de continuidade, não autoridade normativa nem autorização de execução.** Este inventário preserva a situação identificada na auditoria de 17/10/2026, antes do início de uma frente separada de prototipação no Replit. A situação real deverá ser atualizada por nova auditoria ao retomar. Prevalecem os documentos mestres, registries, decisões específicas e [GKR-STATE-001](current-state-register.md).

## 1. Frentes documentais a retomar

| Frente | Fontes atuais | Pendências e condição de avanço |
|---|---|---|
| Pontos e incentivos em oportunidades | [Guia de Pontos](../economic-model/pontos-guia-consulta.md), [Autoridade Econômica](../economic-model/points-economic-authority.md), [PR #655](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/655), [Issue #661](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/issues/661) | Reconciliar PR candidata; paridade, cobertura, funding, percentuais, validade, resgates Mall/Travel, contratos econômicos/legais e testes. Política de ROUND_HALF_EVEN aprovada em princípio não é implementação. Não selecionar fornecedores ou infraestrutura por inferência. |
| Selos de Coletivos | [Guia de Selos](../economic-model/selos-guia-consulta.md), [PR #654](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/654), [Issue #660](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/issues/660) | Comprovação G0/B-01, competência e rito de concessão, metodologia/limiares/validade, 36 objetos DEC/RSP sem ratificação individual comprovada, proteção, recurso e eventual liberação de implementação separada. |
| Rodapé institucional e componente global | [Referência aprovada](../experience-architecture/global-institutional-footer.md), [Quadro FTR](../experience-architecture/global-footer-ftr-control-board.md), [Arquitetura Candidata](../experience-architecture/global-footer-surface-candidate.md) | Conciliar visual posterior do botão Obter o app/QR com a referência oficial; FTR-01 parcial. FTR-02..08 pendentes de destino, evidência 8/8, jurídico/privacidade, acessibilidade, implementação, teste e release. D1..D6 são decisões delimitadas, não gate integralmente fechado. Domínios guivos.com e guivos.us já registrados segundo confirmação do fundador; não repetir essa pergunta. |
| Marca, logo e ativos | [Marca e Ativos](../governance-framework/brand-and-digital-assets-index.md), [PR #653](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/653) | Reconciliar a PR e a origem do ativo de logo com a autoridade vigente; verificar presença de ativo vetorial/binário e publicação no MENU sem redesenhar a marca. |
| Journey / superfícies O-C / UXA | [Jornada O/C — Leia Primeiro](../experience-architecture/organizations-collectives-journey/read-first.md), [PR #599](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/599), [PR #590](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/590), [PR #548](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/548) | Reconciliar PRs antigas com Masters, Surface/Transition Registries e autoridade normativa mais recente, sem promover TRN ou liberar Engineering por inferência. Validação e prototipação externas são frentes separadas. |
| Intelligence / KPIs / evidência | [PR #571](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/571), [PR #648](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/648), [Intelligence](../intelligence-architecture/index.md) | Sanear CI semântico antigo, compatibilidade da autorização operacional, proveniência G-XD e evidência de KPI; não presumir operações, modelos ou dados reais. |
| MENU e sincronização global | [Início do GKR](../index.md), [Roadmap](../roadmap.md), [Estado Atual](current-state-register.md), [Auditoria Integral](gkr-full-corpus-audit.md) | Revisar duplicações, navegação, hubs, precedência entre documento ativo/candidato e entradas de Pontos, Selos, Rodapé e Marca; atualizar Roadmap, registro global e auditoria apenas quando mudanças justificarem promoção própria. |

## 2. PRs preexistentes a classificar ao retomar

| PR | Situação encontrada em 17/10/2026 | Próxima disposição necessária |
|---|---|---|
| [#653](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/653) | Aberta, draft, CI semântico/mecânico SUCCESS | Reconciliar logo e MENU |
| [#654](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/654) | Aberta, draft, CI SUCCESS | Preservar proposta, verificar G0/B-01 e autoridade |
| [#655](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/655) | Aberta, draft, CI SUCCESS | Preservar cenários, separar parâmetros e decisões |
| [#648](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/648) | Aberta, draft, CI SUCCESS | Verificar estado de KPIs/G-XD |
| [#599](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/599) | Aberta, não draft, CI SUCCESS | Revalidar maturidade e contexto G4 |
| [#590](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/590) | Aberta, draft, CI SUCCESS, mergeabilidade pendente | Reconciliar UXA-106 e conflito |
| [#571](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/571) | Aberta, não draft, falha semântica e mecânica SUCCESS | Corrigir/avaliar obsolescência da frente Intelligence |
| [#548](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/548) | Aberta, draft, CI SUCCESS | Reconciliação UXA-057 |

**Nenhuma dessas oito PRs é aprovada para merge em lote por este inventário.** Revisar base atual, diferenças, precedência e decisão válida antes de integrar, corrigir, substituir ou encerrar.

## 3. Fronteira com a nova frente de Replit

Em 17/10/2026 o fundador autorizou **iniciar um novo projeto de desenvolvimento/prototipação da Jornada de Organizações e Coletivos no Replit**. Isso substitui, para essa frente, a pausa anterior sobre edição no Replit, mas **não encerra automaticamente gates documentais antigos nem libera produção/impactos externos**.

- A nova implementação deverá consultar as autoridades vigentes de Organization/Collective, os onze Masters por Superfície, os Maps de IA/Estados/Fluxos e os contratos transversais.
- Os Masters da coleção O/C estão em estado documental draft, e sua existência não concede autorização para criar políticas econômicas, pagamentos, autoridade legal, acesso a dados pessoais reais, notificações externas ou integrações de produção não adjudicadas.
- Para protótipo, usar dados de demonstração rotulados, interfaces e transições coerentes com o GKR. Só usar ações reais com fundamento e autorização próprios.
- Logo oficial, Goldplay e paleta de 30 tokens/ fundo branco exigem respeito às fontes e licença; arquivos de fonte não podem ser expostos publicamente por conveniência.
- Avanço da implementação no Replit não significa `GKR-STATE` promovido, release homologado nem produção autorizada.

## 4. Ordem sugerida para retomada documental

1. Conferir mudanças desde 17/10/2026 e classificar as oito PRs.
2. Resolver gates institucionais de Selos e econômicos de Pontos sem inventar regras/valores.
3. Reconciliar Marca, Rodapé FTR-01..08, Masters e evidências visuais.
4. Reconciliar estados Journey/UXA e Intelligence/KPIs.
5. Auditar MENU/hubs, vínculos, precedência e cobertura; atualizar Roadmap e GKR-STATE somente se necessário.

**Estado deste registro:** `BACKLOG_DOCUMENTED / NOT_ADJUDICATED / RESUME_ON_REQUEST`.
