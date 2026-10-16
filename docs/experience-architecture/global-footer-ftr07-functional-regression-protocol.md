---
id: GKR-UX-GLOBAL-FOOTER-FTR07-001
title: Rodapé Global — Protocolo de Testes Funcionais e Regressão FTR-07
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-functional-test-evidence
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
  - GKR-UX-GLOBAL-FOOTER-FTR02-001
  - GKR-UX-GLOBAL-FOOTER-FTR04-001
  - GKR-UX-GLOBAL-FOOTER-FTR05-001
  - GKR-UX-GLOBAL-FOOTER-FTR06-001
---

# Rodapé Global — Protocolo FTR-07 de Testes Funcionais e Regressão

## 1. Finalidade, fontes e limite

Este protocolo **documenta os ensaios que deverão ser executados quando existir uma implementação autorizada e identificável**. Não certifica comportamento já entregue nem substitui aceite visual, jurídico, de acessibilidade ou de release.

A autoridade de conteúdo e aparência é o [Rodapé Institucional Oficial](global-institutional-footer.md) v1.0.0. As decisões sobre variante e posição do Mapa constam da [Arquitetura Candidata](global-footer-surface-candidate.md) v0.2.8. Ver o [Quadro de Controle](global-footer-ftr-control-board.md), o [Inventário de Destinos FTR-02](global-footer-ftr02-destination-inventory.md), a [Matriz Legal e Privacidade FTR-04](global-footer-ftr04-legal-privacy-review.md), a [Matriz Responsiva e Acessibilidade FTR-05](global-footer-ftr05-responsive-accessibility-matrix.md) e o [Contrato de Integridade FTR-06](global-footer-ftr06-implementation-integrity.md).

**Estado:** `FTR-07 = TEST_PROTOCOL_DOCUMENTED / TESTS_NOT_EXECUTED / GATE_OPEN`. Todo resultado abaixo é `NOT_RUN` ou bloqueado por dependência; não há aqui registros de execução real.

## 2. Condições prévias à execução

Antes de marcar um cenário como `PASS` ou `FAIL`, obter: ambiente reproduzível, URL/rota legítima, identificador de build/commit, artefato de componente, versão da referência editorial, variante aplicada e suas exceções autorizadas, status de links FTR-02, decisão aplicável FTR-04 e responsável por teste.

Não substituir as oito Homes por fallback, páginas internas de planos ou mockups. O relato exploratório de Replit incorporado à arquitetura candidata na PR #674 não equivale a testes FTR-07 executados.

## 3. Casos funcionais e de regressão

| Caso | Objetivo verificável | Evidência exigida | Resultado inicial |
|---|---|---|---|
| FTR07-01 | Renderizar exatamente o rodapé institucional esperado em cada Home pública elegível, com referência textual e visual correta | Rota real + versão + captura por Home + confronto com referência | NOT_RUN |
| FTR07-02 | Detectar ausência de duplicação de rodapés e de variantes locais não autorizadas | Árvore/render por Home e lista de componentes/instâncias | NOT_RUN |
| FTR07-03 | Conferir ordem dos oito destinos e presença editorial de `Mapa do Ecossistema` na posição FTR-01/D1 | Inspeção da ordem e da estrutura por rota | NOT_RUN |
| FTR07-04 | Cada link ativo abre exatamente o destino verificado em FTR-02; itens indisponíveis não fazem navegação enganosa | Matriz item → URL oficial → clique → resultado e data | BLOCKED_BY_FTR02 |
| FTR07-05 | Links de Ajuda e jurídicos correspondem a destinos aprovados, inclusive as ocorrências duplicadas de Privacidade/Termos | Revisão FTR-02/FTR-04 e teste real de abertura | BLOCKED_BY_FTR02_FTR04 |
| FTR07-06 | Ícones sociais conduzem somente a contas oficiais confirmadas, com rótulo acessível | URL, prova de titularidade e navegação | BLOCKED_BY_FTR02 |
| FTR07-07 | Bloco `Receba novidades` apresenta instruções, rótulos, validação e estados coerentes; sem simulação de envio | Registro do fluxo real ou indisponibilidade honesta | BLOCKED_BY_FTR04_FTR06 |
| FTR07-08 | Quando houver inscrição efetiva, validar consentimento/base legal, submissão, erro, duplicidade, feedback, tratamento de dados e cancelamento conforme o serviço real | Cenários e resultados do backend e da UI, sem exposição de dados pessoais | BLOCKED_BY_FTR04_FTR06 |
| FTR07-09 | Fluxos não disparam ações ou inscrições quando recurso está apenas representado visualmente | Teste negativo por estado de indisponibilidade | NOT_RUN |
| FTR07-10 | Foco, teclado, leitores de tela e estados expandidos (quando houver) operam corretamente | Evidências FTR-05 e execução com tecnologia assistiva | BLOCKED_BY_FTR05_IMPLEMENTATION |
| FTR07-11 | `full` desktop/tablet/mobile preserva todos os módulos, navegação, direitos e legibilidade com reflow | Matriz de viewports, fotos, zoom, orientação e falhas | BLOCKED_BY_FTR05_IMPLEMENTATION |
| FTR07-12 | `compact` ou `minimal` só é exibido na rota com exceção contextual previamente aprovada | Registro da decisão e testes da instância real | BLOCKED_BY_CONTEXT_APPROVAL |
| FTR07-13 | Links e ações não dependem de `#`, destinos fictícios, QR ilustrativo apresentado como oficial ou link público quebrado | Inventário de href, QR decodificado quando aplicável e testes negativos | BLOCKED_BY_FTR02 |
| FTR07-14 | Regressão entre versões preserva cópias aprovadas, grupos, ordem e contratos sem alterar outras Homes | Comparativo de builds/capturas e diferenças resolvidas | NOT_RUN |
| FTR07-15 | Mudança de idioma/mercado, quando realmente suportada, mantém destinos e informações legais coerentes | Cenários por locale/mercado oficialmente existente | CONDITIONAL_NOT_RUN |
| FTR07-16 | Se houver botões de lojas/QR, destinos oficiais e apresentação de disponibilidade são verdadeiros em cada estado | Links oficiais, titularidade, QR decodificado e teste de loja | CONDITIONAL_BLOCKED_BY_FTR02 |
| FTR07-17 | Erros de rede/serviço e links indisponíveis produzem feedback real e recuperável sem prometer sucesso | Simulação controlada e captura da mensagem real | BLOCKED_BY_IMPLEMENTATION |
| FTR07-18 | Módulo compartilhado preserva integridade visual e funcional após integração em todas as rotas elegíveis | Evidência de build, execução automatizada quando aplicável e revisão humana | BLOCKED_BY_FTR06 |

Os casos são **candidatos a teste**. O método de execução e os limiares técnicos devem ser aprovados por QA/Produto/Design/Legal/Acessibilidade conforme o risco. Não fixar nomes de bibliotecas, seletores, breakpoints ou endpoints antes do desenho de implementação.

## 4. Cobertura mínima e tipificação de resultado

Registrar as **oito Homes individuais**, a variante `full` em desktop, tablet e mobile, estados de links/formulário disponíveis, casos negativos e rotas excepcionais `compact` ou `minimal` **somente se aprovadas**. Não presumir que isso já representa 24 capturas executadas.

Para cada caso preencher:

| Campo | Regra de registro |
|---|---|
| Caso e gate relacionado | ID `FTR07-xx` e FTR-02/03/04/05/06 pertinente |
| Objeto | Home, rota, ação ou conteúdo exato, sem inventar |
| Versão e ambiente | SHA/build, URL, data, navegador, dispositivo e viewport |
| Pré-condições | Disponibilidade de destino, decisão legal/contextual e dependências |
| Passos e resultado esperado | Reproduzíveis, com rótulo do requisito original |
| Resultado observado | `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN` ou `N/A` com justificativa |
| Evidência primária | Artefato, screenshot, vídeo, log não sensível ou relatório versionado |
| Responsáveis funcionais | Executor, revisor e decisão de aceitação |
| Divergência e correção | Issue e link do reteste, se existir |

**`BLOCKED` não é `PASS`**. `N/A` exige justificativa vinculada à indisponibilidade legítima de uma variante/recurso.

## 5. Critério de saída do FTR-07

O gate só poderá ser adjudicado após: (a) matriz preenchida por cenário executável; (b) casos críticos executados e aprovados; (c) falhas tratadas e retestadas ou exceções explicitamente aprovadas; (d) avaliação de regressão nas oito Homes realmente disponibilizadas; (e) concordância funcional de QA/Produto com revisões de Legal/Acessibilidade onde pertinentes; (f) referência exata a código, build e evidências primárias.

Não concluir FTR-07 com base em CI do próprio GKR: Semantic/Mechanical validam **documentação**, não os recursos de rodapé do produto.

## 6. Limites com publicação

Mesmo FTR-07 aprovado **não** comprova FTR-08: release, domínios públicos, implantação e verificação pós-publicação permanecem independentes. As rotas públicas relatadas como indisponíveis em auditoria exploratória não devem ser apresentadas como publicadas.

**Fronteira desta fase:** somente GKR; sem testes automatizados acionados contra Replit, sem edição de aplicativo, criação de QR ou ativação de serviços.
