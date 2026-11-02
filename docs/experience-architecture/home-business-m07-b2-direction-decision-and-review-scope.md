---
id: GKR-UX-HOME-BUSINESS-M07-B2-DECISION-001
title: Decisão da Direção B2 — preparação da revisão governada do Movimento 07 Business
status: approved_documentary_preparation
version: 1.0.0
owner: Direção da Guivos
last_updated: 2026-11-01
normative: false
---

# Home Business — decisão B2 e escopo de revisão governada

## 1. Decisão expressa

> A direção da Guivos aprova a alternativa B2 para Business, exclusivamente para preparar proposta de revisão governada do Movimento 07 e contratos dependentes, sem publicar capacidades não comprovadas, sem merge ou execução operacional.

O alcance é **preparação documental candidata** e não aprovação antecipada de nova copy pública, novo papel de produto, funcionalidades, integrações, testes ou lançamento.

## 2. Autoridades a confrontar na proposta

- `docs/experience-architecture/public-home-business-master-document.md`, especialmente Movimento 07 e seções 14–16: versão consultada 1.1.10, documento com `normative: true`.
- `docs/experience-architecture/public-home-business-source-lock.md`, especialmente seções 14, 15 e 30: texto e CTA congelados; mudança do papel de Intelligence exige nova decisão expressa e atualização governada.
- `docs/experience-architecture/public-home-business-authority-contracts.md`, Contrato 7: limites de análise, proteção da Journey individual, dados legitimamente conhecidos e vedação de causalidade empresarial sem evidência.
- `docs/product-architecture/business.md` (GPA-004) e `docs/product-architecture/intelligence.md` (GPA-006): nenhuma alteração ou promoção de autoridade de produto autorizada.
- `docs/experience-architecture/public-home-intelligence-master-document.md`: integração de três lentes temporais é proposta separada na PR #720; não declarar como produção vigente.

## 3. Proposta de revisão — estrutura candidata

1. **Retrospectiva — o que aconteceu:** indicadores e eventos efetivamente observados na Guivos, com origem, período, granularidade, autorização e limitações.
2. **Contextual — o que acontece:** leitura de condições, participação e tendências dentro da Guivos, distinguindo medições de interpretações ou inferências.
3. **Prospectiva — o que pode acontecer:** cenários hipotéticos e alternativas para planejamento, nunca previsão certa ou capacidade operacional anunciada sem comprovação.

As lentes podem coexistir. Não criar nova seção obrigatória, produto, três motores de IA, KPI inventado, decisão automatizada ou acesso a dados de pessoas.

## 4. Texto para revisão interna — não é copy aprovada

**Proposta de direção para M07:** “Compreenda o que já aconteceu, reconheça os movimentos do presente e explore possibilidades para novas iniciativas — distinguindo dados observados, interpretações e cenários que ainda dependem de condições reais.”

**Complemento de limites:** “As leituras se restringem aos dados legitimamente conhecidos pela Guivos. Hipóteses sobre o futuro não comprovam resultados empresariais, nem dão acesso à Jornada individual de qualquer Pessoa.”

Esses textos **não substituem** o headline, supporting copy ou CTA congelados. Só podem avançar como revisão normativa depois de análise de impactos e aprovação específica do conteúdo final.

## 5. Matriz de impacto e não regressão

| Fonte | Impacto candidato | Gate |
| --- | --- | --- |
| Home Business Documento Mestre M07 | Explicação temporal acessória ou revisão da narrativa | Avaliação de significado e aprovação posterior |
| Business Source Lock M07 + regra de mudança | Se houver mudança de copy/autoridade, versão candidata e rastreio | Decisão de congelamento separada |
| Authority Contracts, Contrato 7 | Classes de evidência, cenário e limites | Preservar fronteiras de dados e causalidade |
| Design Handoff / Manifesto / Read First | Sincronização de referências após eventual revisão | Não alterar antes de aprovar versões candidatas |
| GPA-004 e GPA-006 | Verificação de compatibilidade, sem edição | Não promover autoridade de produto |
| Superfícies publicadas | Nenhuma nesta fase | Liberação distinta de implantação/publicação |

## 6. Critérios impeditivos

Não afirmar previsão determinística, eficácia da iniciativa, causalidade empresarial, integração aos KPIs internos, análise de Journey individual, scoring humano ou disponibilidade de recursos ainda não implementados. **COMPREENDER ≠ DECIDIR; CENÁRIO ≠ PREVISÃO; INTERPRETAÇÃO ≠ FATO; RESULTADO ESPERADO ≠ COMPROVADO.**

## 7. Próximo produto documental

Preparar diff textual candidato sobre o M07, o Contrato 7 e os itens correlatos do Source Lock, com comparação seção a seção, controle de versões e submissão à revisão da direção. Não alterar as autoridades vigentes nesta etapa.

**Estado:** B2 aprovada para elaboração; conteúdo e integração não aprovados.
