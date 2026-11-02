---
id: GKR-UX-HOME-BUSINESS-M07-B2-DIFF-001
title: Home Business M07 — comparação textual candidata B2
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Business — comparação textual candidata da decisão B2

## Escopo e autoridade
Documento de comparação para análise da direção. Nenhuma substituição normativa foi aplicada. A aprovação de B2 autoriza **elaboração**, não aprovação do conteúdo, merge ou execução. Preservar `GPA-006 v2.0.2` como referência normativa da Home Intelligence, sem alegar que a Guivos AI opera as três perspectivas hoje.

## 1. Documento Mestre — M07 (seções 14–16)

**Texto vigente da direção principal:**
> Entenda como as pessoas participam, utilizam e se movimentam entre as possibilidades que escolhem dentro do ecossistema Guivos.

**Texto vigente do apoio:**
> Visualize participação, recorrência, utilização, interesses agregados e movimentos ao longo do tempo para compreender cada vez melhor suas iniciativas dentro da Guivos.

**Proposta candidata de preservação e acréscimo, em vez de substituição dos dois textos anteriores:**
> A compreensão pode distinguir movimentos efetivamente registrados, interpretações do contexto e possibilidades futuras ainda condicionais. Essa distinção não transforma hipóteses em previsões, nem resultados esperados em resultados comprovados.

**Justificativa:** preservar a promessa e a evidência do M07, explicitando três classes de interpretação temporal como modelo conceitual. A palavra “pode” descreve uma leitura conceitual, **não** capacidade tecnológica implementada. O CTA vigente **“Conheça o Guivos Intelligence”** permanece intacto.

**Diff lógico candidato:**
```diff
  M07: direção principal vigente — preservar sem alteração
  M07: supporting copy vigente — preservar sem alteração
+ M07: nota editorial de distinção temporal (somente após aprovação)
+ M07: proibição explícita de prometer cenário/predição funcional não demonstrado
  M07: CTA vigente — preservar sem alteração
```

## 2. Business Source Lock — seções 14, 15 e 30

**Vigente:** seção 14 congela a direção, o apoio, a expressão analítica livre e o CTA. Seção 15 mantém proteção de Journey, limites de causalidade e escopo da análise. Seção 30 exige **nova decisão explícita** para mudar o papel de Intelligence.

**Adendo candidato para análise normativa futura (seção 15):**
> A distinção entre o que foi observado, o que é interpretado no contexto e o que permanece como cenário possível é um princípio de comunicação responsável. Não constitui declaração de função prospectiva disponível, nem altera o objeto analítico autorizado da Home Business.

**Adendo candidato para a regra de mudança (seção 30):**
> A aprovação B2 de 01/11/2026 autoriza exclusivamente a preparação de propostas. A incorporação deste adendo, a alteração de copy congelada ou o anúncio de capacidade prospectiva dependem de decisão documental específica posterior.

**Diff lógico candidato:**
```diff
  §14: textos e CTA congelados — preservar
+ §15: limite editorial sobre observação, inferência e cenário (candidato)
  §30: regra de mudança vigente — preservar
+ §30: rastreabilidade da autorização B2, sem execução por implicação
```

## 3. Authority Contracts — Contrato 7 (seção 8)

**Vigente:** Guivos Intelligence analisa eventos e dados legitimamente conhecidos pela Guivos: participação, utilização, recorrência, interesses agregados e movimentos ao longo do tempo. Não mede automaticamente impactos empresariais dependentes dos dados internos da empresa; não expõe Journey individual.

**Adendo candidato:**
> Leituras retrospectivas são limitadas à proveniência e integridade dos eventos conhecidos; interpretações contextuais devem declarar lacunas e incertezas; cenários prospectivos, quando discutidos, são hipóteses condicionais e não prova de impacto, promessa de predição ou novo acesso a dados internos da empresa.

**Diff lógico candidato:**
```diff
  Contrato 7: autoridade de dados Guivos e regras vigentes — preservar
+ Contrato 7: três classes de evidência e incerteza, sem extensão de permissão
  Contrato 7: COMPREENDER ≠ VIGIAR; CORRELAÇÃO ≠ CAUSA — preservar
```

## 4. Matriz de não regressão

| Área | Critério para aceitação futura |
| --- | --- |
| Narrativa | 10 movimentos existentes; M07 continua Guivos Intelligence, sem novo produto |
| Copy | Hero, headline, supporting copy e CTA vigentes só mudam mediante decisão específica |
| Evidência | Fato registrado ≠ inferência ≠ cenário prospectivo |
| Produto | Nenhum anúncio de função futura como disponível |
| Privacidade | Sem Journey individual, score humano ou inferência sobre vulnerabilidade |
| Business | Sem causalidade empresarial inventada ou acesso implícito a KPI interno |
| Governança | Atualizar Master, Source Lock, Contrato 7, Handoff, Leia Primeiro e Manifesto **somente após** deliberação de texto final |
| Integração | PR e CI próprios, autorização expressa de merge, verificação separada de publicação |

## 5. Deliberação que falta
A direção ainda precisa deliberar sobre **o texto e a incorporação normativa da proposta**, não apenas sobre sua preparação. Até essa deliberação, o presente diff é um instrumento de comparação sem efeito de alteração canônica.

**Estado:** `candidate_diff_prepared / normative_content_not_approved / no_master_edited / merge_not_authorized`.
