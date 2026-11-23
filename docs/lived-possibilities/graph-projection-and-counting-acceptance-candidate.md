---
id: GKR-LIVED-POSSIBILITIES-GRAPH-CONTRACT-CANDIDATE-001
title: Possibilidades Vividas — G04 Contrato Candidato de Grafo e Contabilização
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-22
normative: false
---

# G04 — Grafo público de impacto: projeção e contabilização

Contrato documental candidato para validação anterior ao futuro protótipo isolado; não é autorização para engenharia, publicação pública, dados reais ou mudança de autoridade. Baseado no [Documento Mestre](index.md), [Grafo Público](public-graph-belonging-and-continuity.md), [G02](authority-and-flow-contract-candidate.md) e [G03](evaluation-instrument-acceptance-candidate.md).

## 1. Escopo e invariantes

A projeção representa **exclusivamente o impacto percebido de uma oportunidade nas pessoas que a viveram**. Não incorporar avaliação de pontualidade, atendimento, organização, segurança operacional, satisfação do ofertador, reputação, objetivos privados, direcionamentos da Jornada nem analytics administrativo como nós, ligações ou indicadores. Não atribuir causalidade às coocorrências.

A fonte da projeção é a contribuição elegível e autorizada derivada de R1/P1 segundo UXA-057; o grafo não é autoridade nova, nem seu estado visual prova a existência jurídica de P1. Dados de teste podem simular autoridade e autorização, sempre rotulados como sintéticos na documentação de teste. Uma manifestação da Pessoa pode integrar vários agrupamentos, mas a Pessoa não é multiplicada no total único.

O escopo de cada cálculo contém, quando pertinentes: oportunidade e edição/unidade, etapa efetivamente vivida, período, população elegível, versão semântica, versão da avaliação vigente e finalidade/autorização da projeção. Não combinar edições, objetos, etapas ou categorias de evidência sem contrato explícito e informação visível. A ausência de representação pode decorrer de privacidade, não resposta, insuficiência de evidência ou supressão, não necessariamente ausência de impacto.

## 2. Anatomia do grafo

| Tipo de nó | Conteúdo e função | Escala |
|---|---|---|
| Oportunidade | CAPA oficial do cadastro, nome e síntese autorizada; central | Proeminência identitária, **não** tamanho proporcional a contagem |
| Família semântica | Conjunto de manifestações relacionadas, com possibilidade de várias dimensões | União de Pessoas distintas que sustentam expressões autorizadas |
| Expressão | Manifestação específica universal ou emergente legitimamente agrupada | Quantidade de Pessoas únicas na expressão |
| Aprofundamento | Conteúdo autorizado que detalha manifestação | Não atribuir tamanho quantitativo sem métrica aplicável |
| Participante | Pessoa vinculada a manifestação autorizada, conforme identificação, foto e perfil permitidos | Não codificar mérito, reputação, intensidade ou relevância pessoal |

Quatro relações: (1) família ↔ expressão, de agrupamento semântico; (2) expressão ↔ expressão, de coocorrência realmente declarada por mesmas Pessoas no mesmo escopo; (3) expressão ↔ aprofundamento, de detalhamento; (4) Pessoa ↔ manifestação, de participação pública individual autorizada. Uma relação de agrupamento pode ter contagem de suporte, mas não declarar coocorrência causal. Um aprofundamento pode existir sem identificação da Pessoa; sua exposição requer autorização de conteúdo específica. Continuidade temporal é proveniência e versão, não quinta aresta pública automática. Não criar arestas meramente decorativas.

## 3. Contagens e denominadores

Considere, em cada escopo contextual s, o conjunto A(s) de pessoas únicas com contribuição pública elegível, vigente e legitimamente autorizada para agregação. O total representado é |A(s)|, **não** a soma das expressões, o total de compradores, o total de registros ou o total de visitantes.

Para uma expressão e, E(e,s) é o conjunto de pessoas de A(s) que sustentam e na versão vigente autorizada; sua contagem é |E(e,s)|. Para uma família f, F(f,s) é a união dos E(e,s) de expressões pertencentes a f; sua contagem é |F(f,s)|, sem somar os totais das expressões. Expressões associadas a várias famílias podem sustentar cada família legitimamente, sem multiplicar a Pessoa em uma família.

Para coocorrência real entre expressões e1 e e2, C(e1,e2,s) = E(e1,s) ∩ E(e2,s). Arestas com outra semântica não herdam esse cálculo automaticamente. Quantificar espessura apenas quando métrica comparável e evidência suficiente existirem. Não atribuir número fictício a conexão conceitual.

Percentual de expressão, quando exibido e permitido, é |E(e,s)| / D(e,s), com o denominador D explicitamente identificado e comparável. Como escolha de referência para ensaios sintéticos, D pode ser A(s) quando todas as expressões do cenário tiverem a mesma base elegível e autorizada; **não fixar denominador universal de produção**. Os percentuais das expressões podem somar mais de 100%, pois a seleção é múltipla. A distribuição de relevância usa apenas respostas válidas à pergunta de relevância no escopo; a distribuição de natureza usa sua própria base. Não misturar incerteza, sem resposta, ausência de impacto percebido, não aplicável e conteúdo suprimido. A base de fotos identificadas é subconjunto diferente da base agregada.

Exemplo sintético de teste: A={P1,P2,P3,P4}; expressão “Me motivou”={P1,P2,P3}, expressão “Aprendi algo novo”={P2,P3}; família contendo ambas={P1,P2,P3}, **3**, não 5; coocorrência={P2,P3}, **2**; percentuais de expressões nessa base comum são 75% e 50%, cuja soma é 125%. P4 pode compor A mesmo sem declarar essas expressões, desde que sua contribuição pública esteja legitimamente representada em outro conteúdo do grafo. O caso não estabelece amostra mínima, algoritmo ou estatística real.

## 4. Atualizações, seleção e privacidade

Nova manifestação autorizada atualiza conjuntos e relações afetados; atualização da mesma avaliação substitui projeção vigente, sem segundo participante. Revogação, mudança de visibilidade, restrição de evidência e moderação competente recalculam ou restringem projeções derivadas; não ressuscitar por cache, replay, restauração ou visita posterior. Histórico privado não é publicação histórica permanente.

Na abertura, a CAPA oficial é o nó central. Algumas fotos **reais e autorizadas** de participantes elegíveis podem integrar a visão inicial, sem revelar automaticamente identidade de quem contribuiu anonimamente. A quantidade visual não representa amostra estatística; distribuir possibilidades de percepção, sem escolher apenas manifestações positivas, influenciadores ou participantes mais populares. A seleção deve permanecer estável durante a sessão e variar somente entre visitas conforme contrato posterior. Ausência de foto não exclui contribuição agregada. Acesso ao perfil e exposição de relato, foto, identidade, vínculo, eixos individuais e quantidade agregada têm escopos diferentes, conforme G05/G06.

A janela contextual apresenta conteúdo adequado a nó e aresta, com navegação bidirecional, sem deduzir autorização a partir da existência do nó. Seleção pode realçar relações sem apagar demais nós. O tamanho de família/expressão indica quantidade, não intensidade, valor ou favorabilidade; cor é família semântica, não nota ou sentimento obrigatório. Distância é layout, não correlação. Parâmetros visuais, motor e animação seguem G07.

Grupos pequenos, contexto sensível, cruzamentos, combinações de filtros, relato identificável e consultas repetidas podem exigir supressão/agrupamento ou não exposição. Nenhum limiar numérico é aprovado aqui; G06 definirá critérios de proteção apropriados. Não apresentar total zero quando a base foi suprimida; distinguir “sem dados elegíveis”, “nenhuma manifestação nessa categoria” e “informação não exibida por proteção”, quando a própria distinção não induzir vazamento.

## 5. Critérios de aceite documental e futuro teste sintético

| ID local | Cenário | Resultado esperado |
|---|---|---|
| G04-T01 | Uma pessoa registra três expressões | Contar a pessoa uma vez no total, uma vez em cada expressão |
| G04-T02 | Duas expressões compartilham pessoas na mesma família | Família usa união; não soma simples |
| G04-T03 | Duas expressões sustentadas por mesmas pessoas | Aresta de coocorrência usa interseção real, sem atribuir causa |
| G04-T04 | Relação família–expressão ou expressão–aprofundamento | Não declarar automaticamente que espessura representa coocorrência |
| G04-T05 | Base comum com respostas múltiplas | Percentuais podem somar acima de 100%; informar denominador |
| G04-T06 | Uma pergunta tem menos respostas que outra | Relevância e natureza mostram bases próprias |
| G04-T07 | Incerteza, sem resposta, ausência de impacto, não aplicável | Estados semanticamente separados, sem inferir zero |
| G04-T08 | Participante atualiza a mesma avaliação | Projeção vigente e contagens atualizadas sem duplicidade |
| G04-T09 | Participação em outra edição | Não combinar bases por padrão |
| G04-T10 | Pessoa retira autorização de agregação | Recalcular/remover contribuições derivadas, sem ressurreição |
| G04-T11 | Pessoa retira apenas autorização de foto | Foto deixa a projeção; agregação ainda permitida permanece |
| G04-T12 | Pessoa autorizou agregação, não identificação | Contribuir em nós agregados sem nó público pessoal identificável |
| G04-T13 | Falta evidência suficiente para projeção pública | Não incorporar sem validação competente |
| G04-T14 | Grupo pequeno ou sensível | Proteger/suprimir conforme política, sem vazar pelo detalhe |
| G04-T15 | Dados protegidos foram suprimidos | Não apresentar falsa contagem zero |
| G04-T16 | Repetição de consulta ou cruzamento de escopos | Não permitir inferir identidade protegida |
| G04-T17 | Foto inicial de participantes | Somente elegíveis e autorizados; conjunto não é amostra estatística |
| G04-T18 | Foto da CAPA muda | Nó central atualiza; avaliações e histórico preservados |
| G04-T19 | Seleção de expressão ou relação | Destaque sem apagar outros nós; painel contextual correto |
| G04-T20 | Oferta com feedback operacional negativo | Grafo representa somente impacto pessoal, não qualidade operacional |
| G04-T21 | Manifestação emergente | Preservar relato e proveniência; não canonizar família automaticamente |
| G04-T22 | Tentativa de exibir dados do Grafo Vivo privado | Não integrar objetivo, condição ou direcionamento pessoal à projeção |
| G04-T23 | Atualização e remoção simultâneas | Revalidar versão/autorização; não mostrar projeção obsoleta |
| G04-T24 | Participante com múltiplas expressões e múltiplos relatos | Preservar uma pessoa lógica no escopo; conteúdo exibido apenas se autorizado |

Todos os 24 cenários estão **especificados, não executados**. O aceite documental não é validação empírica ou implementação. G05 definirá fonte de identidade, CAPA e perfil; G06, limites efetivos de exposição; G07, acessibilidade e interações. Para futuro Replit, só após autorização expressa, dados sintéticos e aplicação independente.

## 6. Limites do G04

Ainda não são definitivos: mínimo seguro de agregação, período de apresentação, denominadores operacionais, método de supressão contra reidentificação, pesos visuais/escala, desenho de coocorrência, performance, definição de identidades deduplicadas em diferentes modalidades, mecanismo de sincronização, direitos de mídia, teste em dispositivos, tecnologia de grafo e contrato público da API. Esses itens deverão ser tratados em gates próprios e adjudicações competentes, nunca presumidos aprovados porque o protótipo exibe uma amostra sintética.

**Estado G04:** contrato candidato e 24 cenários disponíveis para aceite documental humano, sem adjudicação normativa, liberação de interface, testes executados ou autorização de Replit.
