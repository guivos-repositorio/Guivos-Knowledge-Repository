---
id: GKR-UX-GLOBAL-FOOTER-FTR05-001
title: Rodapé Global — Matriz de Verificação Responsiva e Acessibilidade FTR-05
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-responsive-accessibility-verification
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
  - GKR-UX-GLOBAL-FOOTER-FTR02-001
  - GKR-UX-GLOBAL-FOOTER-FTR04-001
---

# Rodapé Global — Matriz FTR-05 de Responsividade e Acessibilidade

## 1. Finalidade e limites de autoridade

**Checklist documental e protocolo de coleta de evidências, não relatório de ensaio concluído.** Esta matriz transforma em critérios verificáveis a decisão arquitetural `FTR-01/D2 = ARCHITECTURE_VARIANTS_ACCEPTED_SCOPED`, registrada na [arquitetura candidata](global-footer-surface-candidate.md) v0.2.8. Não introduz outra variante, não escolhe breakpoints sem teste, não altera o conteúdo e **não aprova exceções de superfície**.

Autoridade de conteúdo, marca e layout desktop: [Rodapé Institucional Oficial](global-institutional-footer.md) v1.0.0. Estado dos gates: [Quadro de Controle FTR](global-footer-ftr-control-board.md). Destinos reais: [Inventário FTR-02](global-footer-ftr02-destination-inventory.md). Tratamento jurídico e do campo de novidades: [Matriz FTR-04](global-footer-ftr04-legal-privacy-review.md).

**Estado inicial:** `FTR-05 = MATRIX_DOCUMENTED / RESPONSIVE_AND_ACCESSIBILITY_TESTS_NOT_EXECUTED / GATE_OPEN`. Um merge de documentação comprova apenas a existência do checklist.

## 2. Variantes e admissibilidade

| Variante e cenário | Regra já aceita | Critério verificável no futuro | Exclusões não autorizadas |
|---|---|---|---|
| `full` — desktop, oito Homes públicas | Hierarquia visual oficial, área de marca, navegação, novidades e faixa inferior | Confrontar imagem/captura real com cópia, ordem, contraste, leitura e interação | Não omitir grupos, assinatura, ajuda ou área de novidades |
| `full` refluído — tablet ou espaço intermediário | Mesmos conteúdos, reorganizados sem comprimir colunas | Conferir orientação, mudanças de janela, quebra de texto, largura de campos e ausência de sobreposição | Não criar versão “mobile reduzida” com conteúdo suprimido |
| `full` empilhado — viewport estreita/mobile | Todos os módulos permanecem alcançáveis em leitura linear | Verificar ordem visual/DOM, scroll, zoom, toque, legibilidade, estado expandido (se existir) | Não ocultar informações legais ou transformar ícones em controles sem rótulo |
| `compact` — página interna pública elegível | Somente quando houver justificativa e decisão por contexto; conteúdo essencial preservado | Identificar rota e decisão, diferenças aprovadas, foco, navegação e recuperação de ajuda | Não assumir omissão de `Receba novidades` sem decisão explícita |
| `minimal` — fluxo sensível/autenticado ou de indisponibilidade | Exceção condicionada a contrato específico por superfície | Provar contexto autorizado, identidade, informação jurídica/ajuda, privacidade e ausência de dados privados | Não aplicar automaticamente às oito Homes; não eliminar vias essenciais |

A variante corresponde ao **contexto e ao conteúdo**, não a um nome arbitrário de breakpoint. Os valores concretos de largura e pontos de quebra serão definidos e justificados somente com medições e evidência visual reproduzível.

## 3. Matriz de verificações transversais

| ID de ensaio proposto | Área | Procedimento/requisito verificável | Prova mínima | Estado |
|---|---|---|---|---|
| FTR05-T01 | Hierarquia e conteúdo | Conferir textos aprovados, ordem de 3 colunas editoriais, bloco `Receba novidades`, faixa inferior, assinaturas, fundo branco, cores e tipografia da referência | Captura identificada + checklist de divergências por variante | NOT_TESTED |
| FTR05-T02 | Reflow e zoom | Redimensionar tela e ampliar conteúdo; verificar legibilidade, ordem, conteúdo alcançável e inexistência de recortes/scroll horizontal indevido | Viewport, escala, dispositivo/navegador, captura antes/depois | NOT_TESTED |
| FTR05-T03 | Navegação por teclado | Percorrer a partir do conteúdo anterior, todos os controles reais do rodapé e o conteúdo seguinte; usar Tab/Shift+Tab/Enter/Espaço conforme controle | Sequência de foco documentada + gravação ou registro reproduzível | NOT_TESTED |
| FTR05-T04 | Foco e estados | Verificar indicador de foco perceptível, não encoberto por elementos fixos, distinção de hover/foco/desabilitado, ordem sem armadilhas | Capturas dos estados e lista de controles | NOT_TESTED |
| FTR05-T05 | Estrutura semântica | Rodapé como região/landmark apropriado, agrupamento e títulos compreensíveis, texto de links discernível sem depender da posição | Inspeção da árvore de acessibilidade e leitura com tecnologia assistiva | NOT_TESTED |
| FTR05-T06 | Leitor de tela | Navegar os grupos, links jurídicos, ícones sociais e formulário, incluindo erros e feedback, sem anúncio enganoso de destinos não disponíveis | Ambiente/testador, sequência narrada e resultado por controle | NOT_TESTED |
| FTR05-T07 | Contraste e legibilidade | Avaliar combinações reais de tokens de texto, ícones, bordas, estados e fundo `#FFFFFF`; usar critério de contraste aplicável à natureza do elemento | Pares de cores observados e cálculo/documento de análise | NOT_TESTED |
| FTR05-T08 | Alvos e gestos | Verificar tamanho e espaçamento dos alvos tocáveis, alcance no mobile e alternativas a gestos complexos, se houver | Medições e capturas de estados tocáveis | NOT_TESTED |
| FTR05-T09 | Idioma e rótulos | Verificar idioma de página, pronúncia e rótulos acessíveis para `Possibility, lived.`, redes, botões e eventual QR | Captura da árvore acessível/registro de teste | NOT_TESTED |
| FTR05-T10 | Expansores opcionais | Se grupos colapsáveis existirem, testar nome, estado expandido/recolhido, controle por teclado e conteúdo recuperável | Registro do componente, estados e tecnologia assistiva | NOT_APPLICABLE_UNTIL_DESIGNED |
| FTR05-T11 | Formulário de novidades | Se funcional, verificar label, finalidade, instruções, validação, erros, sucesso real, feedback e gestão de dados; conferir FTR-04 | Evidência de interface integrada + testes FTR-07 + decisão FTR-04 | BLOCKED_BY_IMPLEMENTATION_AND_PRIVACY |
| FTR05-T12 | Links e destinos | Destino anunciado corresponde ao link validado; sem `#`, ação falsa ou navegação para página genérica de erro | ID do item FTR-02 + teste de abertura | BLOCKED_BY_FTR02 |
| FTR05-T13 | Movimento e interrupções | Testar redução de movimento para efeitos existentes, animações e controles; se não houver movimento, registrar N/A justificado | Configuração de preferência e gravação do comportamento | NOT_TESTED |
| FTR05-T14 | Orientação e dispositivos | Repetir cenários em mobile/tablet/desktop, retrato/paisagem, tamanhos de fonte e navegadores amostrados; registrar limites | Matriz de ambientes e capturas por contexto | NOT_TESTED |
| FTR05-T15 | Privacidade em variantes restritas | Se `minimal` for proposta, inspecionar risco de exposição de estado privado, conteúdo e links de saída, com decisão contextual | Rota específica, justificativa aprovada e captura anonimizada | BLOCKED_BY_CONTEXT_APPROVAL |
| FTR05-T16 | Regressão entre Homes | Nas oito Homes reais, verificar componente compartilhado, conteúdo consistente e ausência de rodapés locais duplicados | Conjunto 8/8 de capturas por viewport + vínculo FTR-03/FTR-06 | BLOCKED_BY_FTR03_AND_IMPLEMENTATION |

**As verificações são critérios operacionais candidatos.** Qualquer declaração de conformidade técnica deverá identificar referencial/acordo de acessibilidade aplicável, versão, método, evidência primária e avaliador competente. Este documento não certifica WCAG, não define conformidade legal e não afirma testes já realizados.

## 4. Protocolo de evidências e amostragem

Para **cada execução** registrar: `ID`, variante, Home/rota exata, ambiente (SO, navegador, versão, dispositivo), largura/altura da viewport, escala de zoom e/ou tamanho do texto, estado de autenticação quando pertinente, técnica assistiva, objeto testado, resultado (`PASS`, `FAIL`, `BLOCKED` ou `N/A` justificado), evidência primária versionada, defeito e responsável funcional pela revisão.

**Mínimo de cobertura antes do aceite:**
1. Todas as oito Homes públicas com `full`; desktop, tablet e mobile evidenciados individualmente, com rastreio do mesmo conteúdo.
2. Testes de teclado e leitura assistiva sobre componentes realmente implementados; prova de foco/contraste/zoom e tratamento de erros.
3. Qualquer aplicação de `compact` ou `minimal` catalogada por rota e acompanhada de aprovação contextual e ensaios próprios.
4. Divergências resolvidas ou explicitamente adjudicadas, sem converter `BLOCKED` em `PASS`.
5. Evidências e resultados de interações amarrados a FTR-02, FTR-04, FTR-06 e FTR-07, e prova de produção separada em FTR-08.

**Importante:** exigência de evidência 8/8 não equivale a 24 testes já executados. Capturas do agente Replit reportadas em FTR-03 sem anexo primário versionado no GKR não satisfazem este protocolo.

## 5. Registro de exceção de superfície

Modelo para qualquer caso `compact` ou `minimal`:

| Campo obrigatório | Preenchimento exigido |
|---|---|
| Rota e superfície | Endereço/identificador exato; não inventar |
| Variante proposta | `compact` ou `minimal` e motivo contextual |
| Diferença versus referência | Lista de blocos e ações alterados, sem elipse |
| Elementos preservados | Marca, suporte e informação jurídica pertinente; tratamento explícito de `Receba novidades` |
| Responsáveis pela decisão | Funções de Produto/Design/Brand/Legal/Acessibilidade relevantes, decisão datada |
| Evidência visual e testes | Capturas reais, a11y, foco, links e comportamento |
| Estado | `PROPOSED`, `APPROVED_SCOPED`, `REJECTED` ou `BLOCKED`, com fonte |

**Não existe exceção de rota aprovada por esta matriz.** A aprovação genérica de D2 não é uma aprovação de instância.

## 6. Encerramento e relações com outros gates

`FTR-05` só pode migrar de `MATRIX_DOCUMENTED / TESTS_NOT_EXECUTED` quando houver prova real por variante e contexto, avaliação humana competente, falhas resolvidas e decisões registradas. Aceite documental deste checklist **não é aceite técnico**.

- FTR-01: governa elegibilidade e arquitetura de variantes.
- FTR-02: comprova existência e natureza dos destinos clicáveis.
- FTR-03: prova aderência contextual às oito Homes e à referência visual.
- FTR-04: governa dados, consentimento e matéria legal.
- FTR-06: comprova componente implementado.
- FTR-07: valida funcionalidade e regressão.
- FTR-08: comprova implantação e aceite pós-publicação.

**Fronteira desta PR:** somente GKR. Nenhuma atualização de aplicativo, screenshots de produção, breakpoint implementado ou teste executado.
