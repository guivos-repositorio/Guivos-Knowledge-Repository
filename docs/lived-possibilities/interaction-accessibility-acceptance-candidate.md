---
id: GKR-LIVED-POSSIBILITIES-G07-INTERACTION-ACCESSIBILITY-CANDIDATE-001
title: Possibilidades Vividas — G07 Interações, Responsividade e Acessibilidade
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-23
normative: false
---

# G07 — Contrato candidato de interação e acessibilidade

Especificação documental para a futura aplicação independente Possibilidades Vividas. Preserva as decisões de [Grafo Público](public-graph-belonging-and-continuity.md), [G04](graph-projection-and-counting-acceptance-candidate.md), [G05](identity-media-and-cover-acceptance-candidate.md) e [G06](privacy-sharing-and-authorization-acceptance-candidate.md). Não é protótipo executado, design final, autorização de Replit, validação empírica ou novo contrato normativo.

## 1. Finalidade e anatomia visual

O grafo público da oportunidade deve ser compreensível para a pessoa, orgânico, humano e explorável, não painel administrativo. O centro é a CAPA e o nome oficiais da oportunidade; famílias, expressões, aprofundamentos e participantes constituem os demais tipos de nós. Quatro famílias de relações já aprovadas permanecem. Cor identifica família semântica, não favorabilidade, mérito ou intensidade; tamanho dos nós semânticos representa pessoas únicas conforme G04. A ligação pode conter conteúdo ou quantidade somente quando legitimamente fundamentada.

Premissas visuais aprovadas: fundo com **grid pontilhado**, nós circulares, cores vivas e distintas por família, distribuição orgânica, enquadramento inicial completo, expansão progressiva, destaque de relações sem apagar os demais elementos, atualização visual estável e janela única de contexto. A experiência não deve criar automaticamente novas dimensões, áreas, pontuações ou rankings. Motor gráfico, paleta precisa, geometria, número inicial de nós e animação final não estão adjudicados.

## 2. Estados de navegação e comportamento

| Situação | Comportamento esperado |
|---|---|
| Primeiro acesso | Fit-to-view com conjunto inicial inteligível e CAPA central, sem cortes de rótulos essenciais; opção de reenquadrar |
| Clique/toque em nó | Seleção evidente, destaque de seus vínculos autorizados, demais nós permanecem visíveis |
| Troca de seleção | Detalhes atualizam sem recriar a visualização nem perder arbitrariamente zoom ou posição |
| Clique/toque em aresta | Detalhar natureza e, se aplicável, suporte da relação sem inferir causalidade |
| Clique na CAPA | Retornar à síntese coletiva da oportunidade sem apagar escolhas legítimas de visualização |
| Expansão | Revelar nós/arestas relacionados sem explosão visual, duplicação de pessoa ou deslocamento injustificado |
| Zoom/pan | Controles explícitos e gestos compatíveis; reenquadramento e recuperação seguros |
| Atualização de dados | Preservar foco, seleção e memória espacial sempre que possível; revalidar permissões |
| Elemento retirado ou suprimido | Ocultar projeção desautorizada, tratar foco e explicar indisponibilidade sem vazamento |
| Erro/vazio/carregamento | Estados diferenciados, recuperação segura, sem inventar estatísticas ou exigir reload completo |

A distribuição não é significado quantitativo por distância. A exploração não deve alterar indicadores pelo simples efeito da simulação de movimento.

## 3. Janela contextual única

A janela de contexto será fixa **no canto superior direito da área do grafo** quando houver espaço e com **ponto indicador do elemento selecionado**, segundo direção visual aprovada. A implementação responsiva deve preservar conteúdo e interação sem obstruir a tela; em telas estreitas pode usar uma apresentação equivalente acessível, mantendo uma única instância de detalhe. Não presumir que “fixa” signifique deslocamento da página inteira ou posição absoluta fora do viewport.

Requisitos:
- seleção de oportunidade, família, expressão, aprofundamento, participante ou aresta atualiza a mesma janela;
- abrir/fechar não provoca rolagem inesperada, recentralização automática, zoom arbitrário nem saltos de layout;
- clique fora fecha quando não houver interação modal impedida; oferecer botão de fechar explícito e acessível;
- troca direta entre nós mantém a posição e substitui detalhes imediatamente, evitando painel duplicado;
- ação selecionada na janela pode selecionar/destacar o nó correspondente (navegação bidirecional);
- detalhes exibem somente conteúdo e identidade autorizados, com base/edição/período quando o dado exigir;
- não apresentar participação verificada, foto, perfil, relatos ou eixos individuais sem autoridade específica.

**Acessibilidade:** foco não deve desaparecer ao abrir/fechar; quando necessário, mover foco para título/painel no momento correto e devolvê-lo ao elemento invocador se ainda existir; assegurar Escape e navegação por teclado. “Clicar fora” não é o único mecanismo.

## 4. Acessibilidade e responsividade

- **Teclado:** navegação para nós e arestas relevantes, estado selecionado e foco visível, entrada/saída segura do painel, acionamentos equivalentes a mouse/toque e controles de zoom/recentrar sem depender de arrastar.
- **Leitores de tela:** alternativa textual estruturada e navegável com oportunidade, famílias, expressões, quantidades/base publicáveis, relações relevantes, estado de seleção e acesso aos detalhes. Não exigir interpretação visual espacial para conhecer o conteúdo.
- **Cores e contrastes:** rótulos e formas distinguíveis sem depender exclusivamente de cor; verificar contrastes conforme critérios de acessibilidade aplicáveis. Estados desfavorável/misto/neutro/incerto não devem ser codificados exclusivamente por cor.
- **Movimento:** respeitar preferência por movimento reduzido, permitir pausar ou eliminar movimento não essencial; não mover o grafo enquanto a pessoa estiver analisando uma seleção. Evitar flashes, efeitos vestibulares e animação obrigatória.
- **Touch e mobile:** alvos adequados, zoom/pan sem aprisionamento de gesto, leitura de rótulos, sobreposições que não escondam comandos; janela equivalente acessível em telas menores.
- **Ampliadores e zoom do navegador:** preservar leitura, controles e conteúdo com ampliações pertinentes; layout adaptável, sem depender de largura fixa.
- **Idioma:** rótulos e interface traduzíveis; conteúdo livre da Pessoa preservado e não retraduzido como se fosse declaração original; textos longos e nomes precisam de tratamento responsivo.
- **Desempenho:** carregamento progressivo e representação parcial com indicação clara, preservando contagens corretas no escopo autorizado; não assumir milhões de nós renderizados simultaneamente. Virtualização, técnicas de renderização e SLAs dependem de validação técnica.

Conformidade formal de acessibilidade e testes com tecnologias assistivas exigem avaliação posterior; esta especificação é um conjunto de critérios candidatos.

## 5. Critérios de aceite documental e futuros testes sintéticos

| ID local | Cenário | Resultado esperado |
|---|---|---|
| G07-T01 | Grafo aberto pela primeira vez | Fit-to-view, CAPA central e elementos iniciais enquadrados |
| G07-T02 | Fundo visual | Grid pontilhado preservado sem prejudicar legibilidade |
| G07-T03 | Selecionar um nó | Destacar nó/arestas relevantes sem ocultar demais |
| G07-T04 | Trocar rapidamente de nó | Uma janela atualiza, sem salto de scroll/zoom |
| G07-T05 | Selecionar aresta | Relação identificável e explicada sem causalidade inventada |
| G07-T06 | Selecionar CAPA | Voltar à síntese contextual da oportunidade |
| G07-T07 | Abrir janela contextual | Canto superior direito quando cabível e indicador do nó |
| G07-T08 | Fechar clicando fora ou por botão | Fechamento sem rolagem ou reenquadramento |
| G07-T09 | Teclar Escape | Fechar detalhe quando apropriado e restaurar foco |
| G07-T10 | Selecionar elemento pelo painel | Destacar o correspondente no grafo sem duplicidade |
| G07-T11 | Expandir família | Exibir expressões progressivamente sem perder referência |
| G07-T12 | Aumentar/diminuir zoom e reenquadrar | Preservar controle e oferecer recuperação |
| G07-T13 | Atualização de dados durante seleção | Preservar seleção quando válida; reagir a retirada de acesso |
| G07-T14 | Nó/identidade perde autorização | Remover detalhe sensível e tratar foco sem vazamento |
| G07-T15 | Grafo vazio ou base suprimida | Estado correto, sem apresentar zero falso |
| G07-T16 | Uso somente por teclado | Explorar nós, arestas, painel e controles sem mouse |
| G07-T17 | Uso com leitor de tela | Alternativa textual equivalente às relações autorizadas |
| G07-T18 | Usuário não distingue cores | Rótulos, foco, seleção e estados permanecem compreensíveis |
| G07-T19 | Preferência por movimento reduzido | Sem animações não essenciais ou deslocamentos involuntários |
| G07-T20 | Dispositivo móvel e toque | Janela acessível, alvos utilizáveis e navegação sem colisões |
| G07-T21 | Ampliação de fonte/zoom de navegador | Sem perda de conteúdo e comandos essenciais |
| G07-T22 | Texto longo ou outro idioma | Layout adaptável e rótulos íntegros |
| G07-T23 | Muitos nós e carregamento progressivo | Sem falsa contagem, perda permanente de foco ou travamento assumido |
| G07-T24 | Rede lenta/erro de carregamento | Estado comunicativo, tentativa de recuperação sem exposição indevida |
| G07-T25 | Nó de participante com relato privado | Nenhuma prévia, foco ou tooltip revela conteúdo restrito |
| G07-T26 | Pessoa seleciona conteúdo negativo/misto/incerto | Não usar símbolos, cor ou organização que impliquem mérito/inferioridade |

Todos os 26 cenários estão **definidos documentalmente e não executados**.

## 6. Limites e próximo gate

Permanecem abertos: testes de usabilidade, critérios quantitativos de contraste/tamanho de alvo/zoom, experiência em leitores de tela e equipamentos reais, validação de i18n, densidade, motores de renderização, requisitos de performance e tecnologia de integração. Não aprovar layout definitivo sem materialização visual; ajustes posteriores deverão respeitar arquitetura e autoridades.

A aplicação deve permanecer **independente**, e sua integração futura deve ser **compartilhada e governada**, nunca por cópias isoladas. G08 definirá o escopo documental, isolamento, critérios de autorização e bloqueio explícito de Replit. G06 recebeu aceite documental condicionado e não libera publicação nem tratamento de dados reais.

**Estado G07:** contrato candidato e 26 cenários apresentados para aceite humano; sem execução, design aprovado, publicação ou Replit.
