---
id: GKR-UX-EVALUATION-REPUTATION-HANDOFF-MATRIX-001
title: Avaliação e Reputação — Matriz Candidata de Handoffs e Continuidade
status: superseded
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
related:
  - UXA-057
  - GKR-UX-EVALUATION-REPUTATION-RESPONSIBILITY-ADJUDICATION-001
  - GKR-UX-EVALUATION-REPUTATION-INITIAL-COVERAGE-001
  - GKR-UX-EVALUATION-REPUTATION-PERSON-SURFACE-PARTITION-001
  - GKR-UX-EVALUATION-REPUTATION-CONTEXTUAL-DISPLAY-AUTHORITY-001
  - GKR-UX-EVALUATION-REPUTATION-RESPONSE-GOVERNANCE-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Avaliação e Reputação — Matriz Candidata de Handoffs e Continuidade

> **Estado pós-adjudicação — 03/10/2026**
>
> Este documento foi superado por `GKR-UX-EVALUATION-REPUTATION-AUTHORITY-001 — Avaliação e Reputação — Autoridade Canônica`. Permanece somente como proveniência técnica não normativa das alternativas e hipóteses examinadas. Não deve ser usado como fonte corrente de produto, MENU, superfície, transição, Design ou Engenharia.


## 1. Alcance

Esta proposta desenvolve a quinta dependência documental de UXA-057: identificar **origem, destino candidato, contexto, pré-condições, revalidação, interrupção, retorno e idempotência** de possíveis passagens entre responsabilidades. Não aprova fluxo, rota, tela, superfície, ID, transição ou cobertura inicial. UXA-057 e os Masters/registries vigentes prevalecem. Os destinos especializados descritos abaixo são **responsabilidades candidatas sem superfície adjudicada**; não devem ser tratados como destinos existentes no Transition Registry.

A identidade mínima de uma experiência candidata combina objeto, titularidade, unidade/edição ou relação, etapa, período, versão material, papel da Pessoa e proveniência de evidência. A identidade de uma avaliação submetida exige referência estável própria, distinta da identidade da experiência. Não expor identificadores ou participação protegidos na URL, no retorno ou em notificações não autorizadas.

## 2. Matriz de passagens candidatas

| Passagem | Origem identificada ou candidata | Destino e responsabilidade candidata | Pré-condições e revalidação no destino | Retorno, interrupção e prevenção de duplicidade |
|---|---|---|---|---|
| H1 — descobrir avaliação de experiência vinculada a Coletivo | PER-108, somente se houver extensão explícita do Master | Registro protegido da avaliação, **sem superfície identificada** | Vínculo não comprova experiência; validar edição/etapa vivida, papel, evidência, elegibilidade, proteção e eventual avaliação já existente | Recusa, perda de elegibilidade ou interrupção retornam ao contexto autorizado sem afetar vínculo; mesma experiência não gera nova avaliação |
| H2 — descobrir avaliação de oportunidade | PER-203, após extensão explícita | Registro protegido, sem superfície identificada | Inscrição válida pode demonstrar apenas a experiência da inscrição quando essa for a etapa avaliada; clique, interesse e redirecionamento externo não demonstram participação posterior | Retorno neutro ao detalhe se ainda autorizado; não modificar inscrição, contratação ou resultado por causa da avaliação |
| H3 — descobrir avaliação de atividade, curso ou Organização | Detalhe público **não comprovado nesta frente** | Registro protegido, sem superfície identificada | Exigir inventário do detalhe real, unidade/edição, responsável, fonte e permissão; não criar origem por analogia a COL-006 ou ORG-001 | **Bloqueada até comprovação da origem**; eventual acesso legítimo à própria avaliação não depende da existência futura do detalhe |
| H4 — registro e envio | Responsabilidade especializada de registro, sem superfície adjudicada | Persistência governada e confirmação da avaliação | Revalidar autorização, versão de critérios, visibilidade, unidade, evidência, conflitos e duplicidade no envio; revisão consciente pela autora | Falha não equivale a envio; retry idempotente pela mesma unidade/operação; confirmação inequívoca e retorno contextual sem alteração de jornada |
| H5 — registro para continuidade | Registro protegido, após envio confirmado ou rascunho legítimo | Continuidade da autora, sem superfície adjudicada | Referência estável da avaliação, autoria e escopo de acesso; distinguir rascunho de submissão concluída | Não reenviar nem duplicar; retomada conserva histórico, estado e direitos, inclusive quando objeto deixa de ser público |
| H6 — acesso permanente à própria avaliação | Ponto de acesso a adjudicar; PER-009 apenas hipótese de entrada transversal | Continuidade da autora | Autenticação, titularidade e proteção; não presumir que PER-009 possui painel de avaliações | Acesso legítimo não depende de retorno ao objeto original; indisponibilidade pública não apaga histórico privado autorizado |
| H7 — continuidade para objeto publicado | Continuidade da autora | PER-103 ou PER-203 **somente após extensão**; demais detalhes dependem de comprovação | Objeto, edição/etapa, versão e visibilidade ainda existentes; autorização para consulta pública independente do acesso da autora | Se indisponível, preservar consulta legítima da autora sem inventar rota histórica ou exposição pública |
| H8 — responsável consulta e responde | COL-002 ou ORG-001 como entradas administrativas candidatas, após extensão | Resposta oficial especializada por objeto, sem superfície adjudicada | Mandato vigente, titularidade da edição, conflito de interesse, escopo de dados e proteção da autora; coexecução exige delegação específica | Ausência/perda de mandato impede envio; resposta principal identificada com histórico material, sem DM nem edição da avaliação |
| H9 — responsável contesta avaliação | Entrada administrativa candidata com autoridade comprovada | Contestação especializada, distinta da resposta | Objeto, unidade, representação, fundamento específico e evidências; discordância com crítica não basta | Contestação não suprime automaticamente conteúdo; protocolo idempotente e retorno de estado sem expor identidade protegida |
| H10 — autora denuncia resposta ou contesta moderação | Continuidade da autora | Denúncia ou contestação especializadas, **procedimentos distintos** | Titularidade da avaliação ou legitimidade afetada, referência da resposta/decisão, fundamento e proteção; autoridade competente | Recebimento com referência e consulta de estado; falha não duplica protocolo; nenhum contato privado obrigatório |
| H11 — triagem para decisão material | Procedimento especializado de denúncia/contestação | Governança especializada de moderação, sem superfície identificada | Competência, conflito de interesse, proveniência, proteção, contraditório e política operacional aprovada | Estado proporcional e histórico; medida cautelar somente se política específica autorizar; denúncia não prova infração |
| H12 — decisão para recurso | Decisão material comunicável de moderação | Instância de recurso especializada e separada | Legitimidade da parte afetada, decisão recorrível, prazo e provas segundo política ainda pendente; independência de quem decidiu inicialmente | Decisão e eventual reversão preservam histórico e efeitos permitidos; não reabrir avaliação como experiência nova |
| H13 — relação Organização↔Coletivo | Contexto bilateral sob UXA-019; ORG-005/COL-008 não são origens UXA-057 aprovadas | Eventual registro ou contestação UXA-057 **dependente de contrato específico** | Identificar acordo/execução, competência das partes, Pessoas legitimamente afetadas, confidencialidade e evidência da experiência; não equiparar negociação à avaliação pública | **Bloqueada para transição** até contrato e origem reais; não excluir automaticamente Pessoas afetadas nem expor dados bilaterais |

Estas passagens são **hipóteses de responsabilidade**, não uma sequência obrigatória de telas. Não há autorização para prompts, notificações, convites, mensagens privadas ou novos relacionamentos entre participantes.

## 3. Envelope candidato de contexto e integridade

Um futuro handoff só poderá transmitir o mínimo necessário, com contrato explícito de origem/destino e proteção:

- **Objeto e experiência:** tipo, identificador autorizado, edição/unidade/relação, etapa, período e versão material; não transferir avaliação de uma edição para outra.
- **Ator e competência:** papel atual, escopo da representação ou autoria, delegação e conflito de interesse; revalidar no destino, sem confiar apenas na origem.
- **Evidência:** categoria, proveniência, validade e escopo; confirmação do responsável, declaração e fonte externa não equivalem à verificação Guivos.
- **Operação:** intenção (iniciar, retomar, consultar, responder, contestar, denunciar ou recorrer), referência estável e chave de idempotência adequada à unidade/operação; não incluir conteúdo sensível em parâmetros públicos.
- **Retorno:** contexto seguro e autorizado, resultado confirmado, pendência, recusa, interrupção ou falha; não presumir envio nem alteração de vínculo quando o usuário apenas navegou.

A especificação de identificadores técnicos, formato, retenção, chaves e políticas de segurança pertence à adjudicação especializada e à Engenharia, não a esta matriz.

## 4. Revalidação e exceções transversais

**Na entrada:** conferir que a origem efetivamente existe e possui autoridade para oferecer a ação; o destino candidato não recebe poder por analogia. Conferir a etapa avaliada, titularidade, identidade protegida e consentimento informado aplicável.

**Na retomada:** revalidar mudanças de edição, critério, evidência, mandato, visibilidade, moderação, vínculo ou objeto. Um rascunho não autoriza envio automático após mudança material. A autora pode recusar sem prejuízo de acesso, vínculo ou oportunidade.

**Na persistência:** distinguir clique, tentativa, envio confirmado e publicação. Repetição por falha de rede não deve criar avaliações ou contestações duplicadas. Nova edição ou etapa materialmente distinta exige evidência e unidade próprias.

**Na resposta e contestação:** o responsável não vê identidade protegida além do permitido, não altera a avaliação, não cria DM e não adquire poder de moderação. Contestação e denúncia seguem trilhas distintas.

**Na moderação e recurso:** decisão material depende de autoridade e política específicas; o recurso não deve ser julgado exclusivamente pela mesma parte interessada. Estado público e comunicação privada podem diferir para proteger segurança e dados.

**No encerramento do objeto:** o detalhe público pode deixar de existir; a consulta legítima da autora e a integridade histórica exigem tratamento próprio, sem presumir manutenção de publicação pública.

## 5. Dependências e gates antes de qualquer GKR-TRN

1. Adjudicar a cobertura inicial, unidade/edição e evidência elegível; a presente matriz não escolhe objeto de lançamento.
2. Conferir entradas e Masters vigentes de PER-108, PER-203, PER-009, COL-002, ORG-001 e COL-007, e localizar os detalhes públicos efetivos antes de afirmar origem ou destino.
3. Decidir materialização das responsabilidades especializadas da Pessoa, do responsável e da governança; os 24 estados funcionais não equivalem a 24 telas.
4. Definir titularidade, delegação, coexecução, proteção de Pessoas afetadas por O↔C e competências independentes de resposta, contestação, moderação e recurso.
5. Aprovar política jurídica/operacional de evidência, publicação, retenção, limiares, prazos, conflito de interesse, segurança e recurso.
6. Só então propor transições individualizadas com origem/destino existentes no Registry, pré-condições, retorno, falha, interrupção, revalidação, idempotência e autorização humana para cada alteração normativa.

## 6. Estado

**DRAFT / NON-NORMATIVE / HANDOFF MATRIX CANDIDATE / NO INITIAL COVERAGE SELECTED / NO NEW IDS / NO TRANSITIONS / NO MATURITY PROMOTION / NO DESIGN OR ENGINEERING RELEASE.**

Não modifica UXA-057, Masters, Surface Registry, Transition Registry, gaps, Current State Register nem operação.
