---
id: GKR-UX-GLOBAL-FOOTER-FTR06-001
title: Rodapé Global — Contrato de Implementação e Integridade do Componente FTR-06
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-implementation-integrity-evidence
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
  - GKR-UX-GLOBAL-FOOTER-FTR02-001
  - GKR-UX-GLOBAL-FOOTER-FTR04-001
  - GKR-UX-GLOBAL-FOOTER-FTR05-001
---

# Rodapé Global — Contrato FTR-06 de Implementação e Integridade

## 1. Escopo e precedência

**Contrato documental de evidências de implementação, não autorização para alterar código.** Define o que uma futura entrega de componente deve demonstrar para ser examinada em FTR-06. O [Rodapé Institucional Oficial](global-institutional-footer.md) v1.0.0 continua autoridade da cópia, marca e referência visual; a [Arquitetura Candidata](global-footer-surface-candidate.md) v0.2.8 registra a arquitetura transversal e as decisões FTR-01/D1/D2. O [Quadro de Controle](global-footer-ftr-control-board.md) concentra estados, o [Inventário FTR-02](global-footer-ftr02-destination-inventory.md) trata destinos, a [Matriz FTR-04](global-footer-ftr04-legal-privacy-review.md) trata dados e legal, e a [Matriz FTR-05](global-footer-ftr05-responsive-accessibility-matrix.md) especifica provas de responsividade/acessibilidade.

**Estado inicial:** `FTR-06 = IMPLEMENTATION_CONTRACT_DOCUMENTED / IMPLEMENTATION_NOT_EVIDENCED / GATE_OPEN`. Nenhuma integração, alteração em Replit, componente React, implantação ou ensaio decorre deste texto.

## 2. Componentização e integridade de fonte

| ID | Exigência candidata de implementação | Evidência necessária | Estado |
|---|---|---|---|
| FTR06-C01 | Componente institucional com fonte editorial compartilhada para as oito Homes elegíveis | Identificação de artefato/caminho, versão, contratos de props, referência de conteúdos e dependências, sem inventar nome de componente | NOT_EVIDENCED |
| FTR06-C02 | Conformidade com a referência institucional: marca, `Possibility, lived.`, `Conectamos pessoas a possibilidades que podem transformar suas vidas.`, grupos, `Receba novidades`, faixa inferior, `Descubra. Viva. Evolua.` | Comparativo de cópia, ordem e layout perante referência aprovada; diferenças registradas | NOT_EVIDENCED |
| FTR06-C03 | Aplicação explícita de `full` nas oito Homes públicas | Inventário de rotas elegíveis, versão da aplicação e prova de renderização por rota; não contar fallback ou páginas de plano como Home | NOT_EVIDENCED |
| FTR06-C04 | `compact` ou `minimal` somente por exceção formal de contexto, preservando acesso a direitos e ajuda | Registro por rota, justificativa e decisão competente com data, diferenças autorizadas e comportamento | NOT_EVIDENCED |
| FTR06-C05 | Ausência de rodapés institucionais locais duplicados ou variações editoriais acidentais | Auditoria de composição e evidência de que cada rota elegível rende exatamente a configuração autorizada | NOT_EVIDENCED |
| FTR06-C06 | Rótulos de navegação ligados apenas a destinos oficiais verificados | Vínculos item a item ao inventário FTR-02, destinos e comportamento com estado de indisponibilidade honesto | BLOCKED_BY_FTR02 |
| FTR06-C07 | `Mapa do Ecossistema` localizado após os oito destinos de `Explore o ecossistema`; link somente após destino definido e verificado | Ordem e existência editorial, URL oficial/decisão de arquitetura e teste de abertura antes de torná-lo clicável | POSITION_ACCEPTED / DESTINATION_BLOCKED |
| FTR06-C08 | Formulário `Receba novidades` sem envio simulado, finalidade e fluxo próprios aprovados antes de ativação | Código/integração, validação, estados e revisão FTR-04, evidência de persistência e descadastramento quando aplicáveis | BLOCKED_BY_FTR04 |
| FTR06-C09 | Canais sociais, legais, eventual app e QR sem links inventados | Catálogo de URLs/titularidade; destinação exata do QR e disponibilidade real se adotado; rastreabilidade FTR-02/04 | BLOCKED_BY_FTR02_FTR04 |
| FTR06-C10 | Semântica, foco, labels, contraste, comportamento e reflow implementados e passíveis de testes | Árvores acessíveis, capturas por variante e execução da matriz FTR-05/FTR-07; código sozinho não equivale a aprovação | TESTS_NOT_EXECUTED |
| FTR06-C11 | Responsabilidade clara por alterações de conteúdo, visual, URLs e código | Registro de owners por função, decisões, origem dos tokens e relação com referências oficiais | NOT_EVIDENCED |
| FTR06-C12 | Mudanças auditáveis e possibilidade de reversão | PR de código, hash/artefato, escopo, testes automatizados e plano de rollback quando houver deploy | NOT_EVIDENCED |

A composição visual branca (`#FFFFFF`), os tokens, a tipografia e a ordem dos ícones obedecem à referência aprovada. Não impor framework, arquitetura de pastas, CMS, tecnologia, nomes de props ou breakpoints por inferência: os critérios são **independentes da implementação técnica**.

## 3. Estado relatado do protótipo e lacunas

A seção FTR-03 da [arquitetura candidata](global-footer-surface-candidate.md), incluída pela PR #674, registra **relato secundário de inspeção do aplicativo Replit**, não homologação:

- foram identificadas no aplicativo inspecionado rotas `/pessoa` e `/organizacoes-coletivos`; as seis Homes restantes não tinham rotas de Home próprias naquele aplicativo;
- o rodapé `FlowFooter` relatado continha marcação exploratória e textos distintos da referência de 14/10, sem os quatro grupos e os elementos aprovados;
- a área de Organizações/Coletivos também apresentava outro rodapé local, indicando risco de duplicidade;
- um acesso `Mapa` no cabeçalho não é prova de `Mapa do Ecossistema` no rodapé;
- capturas do agente em preview, sem anexos primários versionados no GKR, **não encerram FTR-03/FTR-05**; relato de falha pública também não estabelece por si só diagnóstico causal.

**Não alterar o Replit nesta fase.** Os itens acima são pontos de atenção e hipóteses de correção futura, não instruções de intervenção, escopo de produto aprovado ou diagnóstico independente de todo o ecossistema.

## 4. Critérios de aceite e evidência por superfície

Para cada futura aplicação do rodapé, registrar: (i) Home/página e rota **reais**; (ii) variante `full/compact/minimal` e decisão de elegibilidade; (iii) commit/versão/ambiente; (iv) referência editorial e de tokens; (v) elemento compartilhado, configurações e exceções; (vi) capturas primárias desktop/tablet/mobile identificadas; (vii) lista de destinos reais e comportamento quando indisponíveis; (viii) tratamento de formulário/dados; (ix) teste de duplicidade; (x) revisão de Design, Brand, Engenharia, Acessibilidade e Legal conforme competência; (xi) divergências, correções e decisão.

**Cobertura necessária:** as oito Homes públicas, sem substituir falta de Home por rota fallback, mockup isolado ou página funcional de outro produto. Caso a aplicação examinada não contenha todas as Homes, registrar honestamente o subconjunto observado e a dependência externa, sem afirmar 8/8.

### Critério de bloqueio

Não promover FTR-06 a `IMPLEMENTED` pela simples existência de `FlowFooter`, por merge do GKR, por captura exploratória ou por implementação parcial. Exigir evidência de componente conforme referência, composição de superfícies, ausência de duplicidade, tratamento de URLs e decisões contextuais.

## 5. Interdependência com outros gates

- **FTR-01**: aprovação das regras de variantes não autoriza cada exceção de rota.
- **FTR-02**: nenhum destino se torna operacional antes de verificação.
- **FTR-03**: revisão visual comparativa por Home permanece independente do aceite técnico.
- **FTR-04**: matéria legal e fluxo de dados exigem revisão competente.
- **FTR-05**: acessibilidade/responsividade dependem de provas reais por ambiente.
- **FTR-07**: execução de testes e resultados comprováveis é etapa própria.
- **FTR-08**: deploy, URL pública, release e monitoramento requerem prova separada.

## 6. Registro de atualização futura

Cada avanço deverá informar `exigência C01..C12`, objeto, versão de código, URL/ambiente, evidência primária, responsável funcional, resultado, pendência e ato autorizativo. Falta de evidência mantém `NOT_EVIDENCED` ou `BLOCKED`.

**Status deste documento:** candidato não normativo. **FTR-06 permanece aberto**, sem implementação autorizada ou comprovada por esta atualização do GKR.
