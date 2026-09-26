---
id: GKR-UX-PER006-MASTER-001
title: Jornada da Pessoa — PER-006 — Processamento Visível — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-023
  - UXA-037
related:
  - GKR-UX-PER005-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - PER-005
  - PER-006
  - PER-007
  - TRN-005
  - TRN-006
---

# Jornada da Pessoa — PER-006 — Processamento Visível — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-006 — Processamento Visível` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

A superfície existe para tornar o processamento material **visível, temporário, interrompível e compreensível**, sem simular compreensão instantânea, sem expor raciocínio interno detalhado e sem transformar processamento em persistência ou personalização.

Este documento não cria tela, layout, wireframe, UI, protótipo, sistema visual ou implementação.

```text
PER-005 — INVENTÁRIO E AUTORIZAÇÃO
→ TRN-005 / PARCIAL
→ PER-006 — PROCESSAMENTO VISÍVEL
→ TRN-006 / LOCALMENTE VALIDADA
→ PER-007 — COMPREENSÃO INICIAL REVISÁVEL
```

## 2. Papel na Jornada

`PER-006` governa o período entre a autorização específica de processamento e a disponibilidade da compreensão inicial revisável.

Ela governa:

- indicação explícita de que existe processamento temporário em andamento;
- uso somente dos conteúdos revisados e autorizados;
- estado textual compreensível do processamento;
- indicação das fontes consideradas em nível compatível com a autonomia da Pessoa;
- interrupção com efeito conhecido;
- descarte do resultado parcial quando interrompido;
- retorno para revisar conteúdos quando aplicável;
- saída para exploração sem personalização;
- falha e recuperação sem continuidade oculta;
- handoff governado para `PER-007`.

Ela não governa:

- revisão das afirmações da compreensão;
- confirmação de fatos ou inferências;
- persistência da compreensão;
- personalização;
- modelo ou fornecedor de IA;
- exposição de chain-of-thought ou raciocínio interno detalhado;
- armazenamento, retenção ou política jurídica final.

## 3. Entrada legítima

A entrada corrente ocorre por `TRN-005 — PER-005 → PER-006`, que permanece parcial.

A entrada exige, no limite funcional corrente:

- inventário revisado;
- itens elegíveis conscientemente selecionados;
- autorização específica registrada;
- finalidade conhecida;
- exclusão do processamento de itens não autorizados.

```text
DISPONÍVEL TECNICAMENTE
≠ AUTORIZADO

AUTORIZADO
→ SOMENTE PARA A FINALIDADE DECLARADA
```

Este Master não promove `TRN-005`.

## 4. Job da Pessoa

Durante o processamento, a Pessoa precisa conseguir compreender:

1. que o processamento começou;
2. que ele é temporário;
3. quais conteúdos autorizados estão sendo considerados em nível apropriado;
4. qual é a finalidade;
5. qual é o estado real;
6. que processamento não significa conclusão;
7. como interromper;
8. o que acontece ao interromper;
9. como voltar para revisar conteúdos;
10. como sair para explorar sem personalização;
11. quando existe falha ou ação necessária;
12. quando a compreensão inicial está pronta para revisão.

## 5. Estado explícito

A experiência deve declarar de forma inequívoca:

> **Processamento temporário em andamento.**

O Design pode reformular a redação desde que preserve o significado.

Não deve haver estado visual que sugira:

- que a Guivos já “entendeu” a Pessoa;
- que a compreensão está confirmada;
- que existe diagnóstico;
- que houve persistência;
- que personalização foi ativada;
- que uma tarefa continuará silenciosamente após interrupção.

## 6. Etapas por estado, não por evolução humana

Quando etapas forem mostradas, elas devem representar **estado do processamento**, não percentual de evolução da Pessoa.

São incompatíveis com o contrato:

- “você está 80% compreendido”;
- score de completude humana;
- progresso que represente maturidade, mérito ou evolução pessoal;
- percentual inventado de certeza.

O Design pode mostrar estados operacionais legítimos, desde que não invente mecanismo técnico ou precisão inexistente.

## 7. Conteúdo considerado

Somente conteúdos revisados e autorizados podem entrar no processamento.

A superfície deve conseguir comunicar, em granularidade adequada:

- que fontes autorizadas estão sendo consideradas;
- que itens excluídos permanecem fora;
- que a finalidade permanece limitada;
- que a autorização não se expande durante o processamento.

A disponibilidade de uma fonte adicional não autoriza seu uso automático.

## 8. Fontes e proveniência

A Pessoa deve conseguir reconhecer quais categorias de fonte autorizada participam do processamento quando isso for material para sua compreensão e controle.

A experiência não precisa expor:

- prompts internos;
- tokens;
- chain-of-thought;
- raciocínio interno detalhado;
- arquitetura técnica;
- logs internos;
- parâmetros do modelo.

```text
EXPLICABILIDADE
→ FONTES + NATUREZA + FINALIDADE + ESTADO + CONTROLES

EXPLICABILIDADE
≠ EXPOSIÇÃO DE RACIOCÍNIO INTERNO
```

## 9. Interrupção

A interrupção deve possuir efeito explícito.

A autoridade corrente valida o significado:

> **Interromper e descartar resultado parcial.**

Ao interromper:

- o processamento em curso é encerrado;
- o resultado parcial não é promovido a compreensão;
- não existe continuidade silenciosa em segundo plano;
- os conteúdos de origem permanecem somente conforme os controles anteriores;
- nenhuma persistência ou personalização é criada por consequência.

A ação pode exigir confirmação proporcional ao efeito, sem coerção.

## 10. Revisar conteúdos durante o processamento

Quando a Pessoa escolher revisar os conteúdos usados:

```text
REVISAR CONTEÚDOS
→ INTERROMPE PROCESSAMENTO ATUAL
→ DESCARTA RESULTADO PARCIAL
→ RETORNA AO CONTEXTO DE REVISÃO APLICÁVEL
```

Uma alteração material exige novo estado compatível de revisão/autorização antes de novo processamento.

Este Master não transforma essa volta em nova transição integralmente validada.

## 11. Explorar sem personalização

A experiência deve preservar uma saída legítima equivalente a:

> **Interromper e explorar sem personalização.**

Essa escolha:

- encerra o processamento;
- descarta o resultado parcial;
- não ativa personalização;
- não deve ser apresentada como fracasso;
- não deve pressionar a Pessoa a concluir a compreensão inicial.

O destino exato deve respeitar a autoridade de navegação vigente; este Master não inventa uma rota nova.

## 12. Pausa e saída

Não se deve usar um rótulo genérico como `Sair` quando seu efeito for ambíguo.

Se a solução oferecer pausa ou saída, deve ficar claro:

- se o processamento para;
- se o resultado parcial é descartado;
- se algum conteúdo permanece segundo controles anteriores;
- qual é o destino;
- se existe ou não possibilidade legitimamente contratada de retomada.

Nenhuma continuidade em background pode ser presumida.

## 13. Falha

A experiência deve acomodar falha real sem simular sucesso.

Quando houver falha:

- o estado deve ser declarado;
- nenhuma compreensão deve ser apresentada como concluída;
- o resultado parcial não deve ser promovido silenciosamente;
- a Pessoa deve receber ações compatíveis com a autoridade corrente;
- repetir processamento não pode expandir autorização;
- conteúdo não autorizado continua fora.

## 14. Base insuficiente

Se o processamento não puder formar base suficiente para uma compreensão inicial útil, a experiência não deve pressionar a Pessoa a compartilhar mais.

A continuidade pode oferecer, quando legitimamente aplicável:

- revisar o que foi compartilhado;
- compartilhar algo adicional voluntariamente;
- continuar sem personalização;
- encerrar ou voltar à exploração.

```text
BASE INSUFICIENTE
≠ INSUFICIÊNCIA DA PESSOA
≠ OBRIGAÇÃO DE EXPOSIÇÃO ADICIONAL
```

## 15. Proteções durante o processamento

Devem permanecer verdadeiras:

- autenticação não autoriza processamento;
- autorização vale somente para a finalidade declarada;
- conteúdo não autorizado fica fora;
- inferências sensíveis automáticas não são autorizadas por este Master;
- engajamento não equivale a evolução;
- processamento não equivale a persistência;
- processamento não equivale a personalização;
- publicidade não recebe autorização por consequência;
- retirada ou revisão aplicável deve produzir efeito conhecido.

## 16. Estados funcionais

O Design deve conseguir acomodar, quando aplicável:

1. processamento iniciado;
2. processamento temporário em andamento;
3. estado operacional intermediário legítimo;
4. ação de interrupção disponível;
5. confirmação de interrupção quando necessária;
6. processamento interrompido;
7. retorno para revisão de conteúdos;
8. exploração sem personalização;
9. falha;
10. ação necessária;
11. base insuficiente;
12. compreensão inicial disponível;
13. estado pronto para `TRN-006`.

```text
ESTADOS FUNCIONAIS
≠ TELAS CANÔNICAS
≠ NOVOS PER-IDs
```

## 17. Handoff para PER-007

`TRN-006 — PER-006 → PER-007` é **localmente validada** por `UXA-037`.

O handoff ocorre quando existe uma compreensão inicial disponível para revisão.

```text
PROCESSAMENTO CONCLUÍDO
→ COMPREENSÃO INICIAL DISPONÍVEL
→ TRN-006 / LOCALMENTE VALIDADA
→ PER-007 — COMPREENSÃO INICIAL REVISÁVEL
```

A passagem não significa:

- que a compreensão é fato;
- que a Pessoa a confirmou;
- que inferências foram aceitas;
- que persistência foi autorizada;
- que personalização foi autorizada.

Este Master preserva a maturidade corrente de `TRN-006`; não a promove para integralmente validada.

## 18. Relação com a compreensão inicial

`PER-006` prepara o resultado temporário; `PER-007` governa sua apresentação/revisão e as decisões posteriores.

A compreensão inicial deve chegar à superfície seguinte como material revisável, não como diagnóstico ou verdade consolidada.

As regras detalhadas de:

- identidade das afirmações;
- natureza;
- origem;
- confiança;
- confirmação;
- rejeição;
- correção;
- manutenção em aberto;
- persistência;
- personalização;

pertencem à responsabilidade de `PER-007` e não devem ser antecipadas como decisão em `PER-006`.

## 19. Linguagem

A linguagem deve:

- usar estado real;
- evitar “já entendemos você” durante processamento;
- evitar diagnóstico;
- evitar promessa de precisão;
- evitar percentual de compreensão humana;
- evitar urgência ou culpa;
- explicar o efeito da interrupção;
- distinguir processamento de persistência e personalização;
- tratar base insuficiente de forma neutra.

## 20. Acessibilidade

A futura solução deve considerar:

- operação por teclado;
- foco visível;
- estados não dependentes apenas de cor;
- atualizações de estado anunciáveis por tecnologia assistiva;
- ação de interrupção identificável;
- mensagens de falha compreensíveis;
- ausência de animação obrigatória para compreender o estado;
- preferência por movimento reduzido;
- zoom e responsividade.

## 21. Conteúdo sintético para Design

Design pode simular:

- fontes fictícias autorizadas;
- estados intermediários;
- processamento em andamento;
- interrupção;
- falha;
- base insuficiente;
- conclusão do processamento;
- handoff simulado para `PER-007`.

Não pode apresentar como real:

- processamento real;
- modelo de IA real;
- percentual real de progresso sem autoridade técnica;
- persistência;
- personalização;
- dado pessoal real;
- inferência sensível real;
- autorização adicional.

## 22. Liberdade de Design

A designer pode decidir:

- quantidade de frames;
- composição;
- componentes;
- hierarquia;
- tipografia;
- paleta;
- iconografia;
- densidade;
- motion;
- microinterações;
- representação visual dos estados;
- responsividade;
- forma visual dos controles de interrupção e recuperação.

O GKR não define baseline visual obrigatório para `PER-006`.

Referências visuais anteriores não são autoridade estética corrente.

## 23. Uso por IA

Quando IA for usada para explorar `PER-006`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. Surface Registry e detalhamento da Pessoa;
5. Transition Registry;
6. `UXA-023`;
7. `UXA-037`;
8. `GKR-UX-PER005-MASTER-001` para a fronteira de entrada.

A IA não pode:

- usar item não autorizado;
- inventar autorização;
- inventar percentual de compreensão;
- simular chain-of-thought;
- prometer processamento em background;
- antecipar confirmação da compreensão;
- liberar persistência;
- liberar personalização;
- promover `TRN-005`;
- promover `TRN-006`;
- criar novo `PER-ID`;
- iniciar Product Engineering.

## 24. Critérios de Aceite Funcional

Uma futura solução visual de `PER-006` é aceitável quando:

1. declara processamento temporário em andamento;
2. somente conteúdos revisados e autorizados participam;
3. o estado real é compreensível;
4. etapas não representam evolução humana;
5. não existe percentual inventado de compreensão;
6. fontes consideradas são compreensíveis em nível apropriado;
7. raciocínio interno detalhado não é exposto;
8. interrupção possui efeito explícito;
9. interrupção descarta resultado parcial;
10. não existe processamento silencioso após interrupção;
11. revisar conteúdos interrompe e descarta o resultado parcial;
12. explorar sem personalização permanece legítimo;
13. falha não é apresentada como sucesso;
14. base insuficiente não pressiona exposição adicional;
15. processamento não equivale a persistência;
16. processamento não equivale a personalização;
17. `TRN-005` permanece parcial;
18. `TRN-006` permanece localmente validada;
19. nenhuma nova superfície é criada;
20. Product Engineering permanece não liberado.

## 25. Limites

Este Documento Mestre não:

- cria tela final;
- cria Figma;
- cria protótipo;
- define modelo ou fornecedor de IA;
- define política jurídica final;
- define armazenamento ou retenção;
- implementa processamento;
- implementa segurança;
- implementa persistência;
- implementa personalização;
- autoriza inferências sensíveis;
- expõe raciocínio interno;
- cria diagnóstico;
- conclui textos finais;
- executa testes com usuários;
- altera `TRN-005`;
- promove `TRN-006`;
- cria `PER-007`;
- inicia Product Engineering.

## 26. Estado Corrente

```text
PER-006 MASTER
→ CURRENT DESIGN DEFINITION

ENTRY
→ TRN-005 / PARTIAL

JOB
→ VISIBLE + TEMPORARY + INTERRUPTIBLE PROCESSING

INPUT
→ REVIEWED + AUTHORIZED CONTENT ONLY

INTERRUPTION
→ EXPLICIT EFFECT
→ DISCARD PARTIAL RESULT
→ NO SILENT BACKGROUND CONTINUITY

INSUFFICIENT BASIS
→ NEUTRAL
→ NO PRESSURE TO SHARE MORE

PERSISTENCE
→ BLOCKED

PERSONALIZATION
→ BLOCKED

TRN-006
→ LOCALLY VALIDATED / UNCHANGED

NEXT DOCUMENTATION TARGET
→ PER-007 — COMPREENSÃO INICIAL REVISÁVEL

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
