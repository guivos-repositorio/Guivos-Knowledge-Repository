---
id: GKR-UX-PER106-MASTER-001
title: Jornada da Pessoa — PER-106 — Meus Coletivos — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - UXA-056
  - UXA-092
  - UXA-094
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-SURF-PER-107
  - GKR-TRN-108
  - GKR-TRN-110
---

# Jornada da Pessoa — PER-106 — Meus Coletivos — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-106 — Meus Coletivos` para designer humana, IA opcional, Produto, UX, Research, Privacidade e Engenharia.

A superfície permite à Pessoa **reconhecer seus vínculos com Coletivos, compreender o estado e o papel atual de cada vínculo, perceber mudanças relevantes e escolher conscientemente qual contexto deseja abrir**.

`PER-106` é uma superfície central de vínculos. Não é feed, ranking, placar de engajamento, comparação entre participantes nem fila de solicitações.

## 2. Papel na Journey

```text
APROVAÇÃO AUTORIZADA
→ VÍNCULO FORMADO
→ TRN-108 / INTEGRALLY VALIDATED
→ PER-106 DISPONÍVEL COMO CONTINUIDADE

PER-106
→ AÇÃO EXPLÍCITA
→ TRN-110 / INTEGRALLY VALIDATED
→ PER-107 — CENTRAL DE ATUALIZAÇÕES
```

A aprovação forma o vínculo antes da navegação para `PER-106`. Abrir `Meus Coletivos` é continuidade opcional e não constitui participação.

## 3. Job da Pessoa

A superfície deve permitir que a Pessoa:

1. reconheça os Coletivos com os quais possui vínculo legitimamente reconhecido;
2. diferencie estados de vínculo sem convertê-los em mérito;
3. compreenda seu papel atual quando houver papel aplicável;
4. reconheça mudança relevante de estado;
5. compreenda última atualização relevante quando legitimamente disponível;
6. reconheça itens não lidos por categoria sem pressão artificial;
7. troque categoria ou contexto sem alterar o vínculo;
8. escolha conscientemente abrir a Central de Atualizações;
9. retorne sem produzir efeito substantivo;
10. preserve privacidade entre vínculos distintos.

## 4. Regra constitutiva do vínculo

```text
DECISÃO AUTORIZADA DE APROVAÇÃO
→ CRIA O VÍNCULO LÓGICO

ABRIR PER-106
≠ CRIAR VÍNCULO

NÃO ABRIR PER-106
≠ DESFAZER APROVAÇÃO

REPETIR EVENTO DE APROVAÇÃO
≠ DUPLICAR VÍNCULO
```

A interface deve representar o vínculo já existente, não fabricar um segundo ato de adesão.

## 5. Categorias e estados

As autoridades correntes reconhecem categorias distintas de vínculo, incluindo, quando aplicáveis:

- participação confirmada;
- participação com função aceita;
- participação pausada;
- vínculo encerrado;
- outros estados legitimamente registrados pela autoridade corrente.

Essas categorias servem para compreensão e organização. Não formam ranking de dedicação, qualidade, valor, mérito ou prioridade.

```text
ESTADO DE PARTICIPAÇÃO
≠ PAPEL

PAPEL
≠ AUTORIDADE

DISPONIBILIDADE
≠ PARTICIPAÇÃO

PRESENÇA EM ATIVIDADE
≠ ESTADO DO VÍNCULO
```

A designer não deve fundir esses conceitos em um único indicador.

## 6. Informações que podem ser exibidas

Quando legitimamente disponíveis e necessárias, `PER-106` pode exibir:

- identidade necessária do Coletivo;
- estado corrente do vínculo;
- papel atual da Pessoa;
- mudança relevante de estado;
- última atualização relevante;
- itens não lidos por categoria;
- ação legítima para abrir contexto relacionado;
- acesso explícito à Central de Atualizações.

A superfície não deve expor, por conveniência:

- conteúdo protegido da Journey;
- outros vínculos pessoais sem relação com o contexto;
- dados sensíveis sem finalidade;
- inferências pessoais não autorizadas;
- informação operacional reservada do responsável;
- comparação de comportamento entre participantes.

## 7. Organização sem ranking

A organização dos vínculos pode apoiar compreensão por categoria ou estado, mas não pode sugerir:

- ranking de dedicação;
- sequência obrigatória;
- pontuação de engajamento;
- comparação entre participantes;
- obrigação de frequência;
- prioridade moral entre Coletivos;
- pressão para abrir atualizações.

Ordenação ou agrupamento visual não deve ser apresentado como avaliação da Pessoa.

## 8. Atualizações sem absorver PER-107

`PER-106` pode apresentar sinais resumidos necessários para orientar a Pessoa, como última atualização relevante ou quantidade/categoria de itens não lidos quando houver autoridade e dado real.

Isso não transforma a superfície em Central de Atualizações.

```text
PER-106
→ RECONHECER VÍNCULOS
→ COMPREENDER ESTADO
→ ESCOLHER CONTEXTO

PER-107
→ TRIAR E COMPREENDER ATUALIZAÇÕES
→ RESPONSABILIDADE SEPARADA
```

A lista detalhada, triagem e compreensão das atualizações pertencem a `PER-107`.

## 9. TRN-108 — continuidade pós-aprovação

`COL-003 → PER-106`.

A decisão autorizada de aprovação forma o vínculo e torna `PER-106` disponível como continuidade opcional.

Estado: **integralmente validada**.

A transição não depende de clique posterior para constituir o vínculo e repetição do evento não deve duplicá-lo.

## 10. TRN-110 — Central de Atualizações

`PER-106 → PER-107`.

A transição ocorre por ação explícita da Pessoa.

Estado: **integralmente validada**.

Abrir a Central:

- não altera vínculo;
- não cria participação;
- não registra presença;
- não confirma leitura de conteúdo que ainda não foi efetivamente compreendido;
- não produz efeito substantivo da atualização;
- não transfere autoridade.

## 11. Ações e controles

Conforme vínculo e autoridade, a Pessoa pode:

- consultar seus Coletivos;
- alternar categoria ou agrupamento;
- abrir contexto legítimo de um Coletivo quando houver continuidade contratada;
- abrir a Central de Atualizações por ação explícita;
- retornar;
- compreender mudança relevante sem ser obrigada a agir.

Este Master não inventa handoff direto para superfície que não esteja contratada no Transition Registry.

## 12. Estados internos de experiência

A designer pode representar dentro de `PER-106`:

- carregamento/revalidação;
- conjunto de vínculos disponíveis;
- categoria selecionada;
- ausência legítima de vínculos em determinada categoria;
- mudança relevante de vínculo;
- indicador resumido de atualização;
- vínculo pausado;
- vínculo encerrado;
- erro recuperável;
- estado incerto exigindo revalidação;
- indisponibilidade temporária.

Esses estados não criam novos `PER-ID`s.

## 13. Vazio e ausência

Ausência de Coletivos ou ausência em determinada categoria é estado legítimo.

A experiência não deve interpretar vazio como:

- falha pessoal;
- isolamento;
- falta de engajamento;
- recomendação obrigatória para aderir a um Coletivo;
- permissão para inventar vínculos ou sugestões como fatos.

Qualquer continuidade de descoberta deve existir somente quando houver handoff e autoridade correspondentes.

## 14. Pausa e encerramento

Participação pausada e vínculo encerrado devem ser reconhecíveis sem serem tratados como punição ou demérito.

A superfície não pode inferir:

- motivo da pausa;
- culpa;
- abandono;
- avaliação negativa;
- possibilidade de reativação quando não contratada;
- efeito sobre outros vínculos.

## 15. Privacidade e separação entre vínculos

A superfície deve preservar minimização e separação contextual.

Um Coletivo não recebe automaticamente:

- lista dos demais Coletivos da Pessoa;
- contexto privado da Journey;
- atividades em outros vínculos;
- preferências de outros contextos;
- informação sensível sem finalidade e autoridade.

A visão agregada pertence à Pessoa e não transfere visibilidade entre Coletivos.

## 16. Processamento e recuperação

Quando o estado precisar ser revalidado:

- não fabricar vínculo;
- não duplicar vínculo após repetição de evento;
- não transformar demora em encerramento;
- não alterar estado por simples abertura;
- preservar contexto em erro recuperável;
- reconsultar fonte canônica quando o estado estiver incerto;
- não apresentar atualização obsoleta como estado vigente.

## 17. Linguagem e claims

Evitar linguagem que:

- transforme participação em mérito;
- pressione por frequência;
- trate papel como autoridade automática;
- apresente não lidos como dívida moral;
- confunda atualização com obrigação;
- confunda vínculo pausado com encerrado;
- trate vínculo encerrado como avaliação negativa;
- sugira que abrir `PER-106` cria participação.

Preferir linguagem factual, contextual e orientada ao estado real.

## 18. Acessibilidade

Estado do vínculo, papel, mudanças, categorias, indicadores e ações devem ser compreensíveis sem depender exclusivamente de:

- cor;
- posição;
- ícone;
- animação;
- som.

Agrupamentos, contagens e mudanças de estado devem possuir rótulos compreensíveis por tecnologias assistivas e ordem de foco coerente.

## 19. Dados reais e conteúdo sintético

Nenhum Coletivo, vínculo, papel, estado, atualização, contagem ou relação pode ser inventado e apresentado como real.

Conteúdo sintético para prototipação é permitido quando:

- claramente fictício;
- não atribuído a entidade ou pessoa real;
- não usado para criar regra de produto;
- não cria ranking ou score;
- não sugere vínculo inexistente;
- respeita os estados e limites canônicos.

## 20. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer possui liberdade sobre composição, agrupamento, densidade, componentes, ritmo, imagens, iconografia, motion, microinterações e responsividade, preservando:

- distinção entre vínculo, papel, autoridade e atividade;
- ausência de ranking e pressão;
- privacidade;
- acessibilidade;
- handoffs governados;
- autoridades atuais de marca, incluindo a tipografia oficial quando aplicável.

## 21. Limites para IA

IA não pode:

- inventar Coletivo, vínculo, papel, estado ou atualização;
- criar ranking, score ou comparação entre participantes;
- transformar itens não lidos em obrigação;
- inferir autoridade a partir de papel sem contrato;
- criar ou encerrar vínculo;
- expor outros vínculos a um Coletivo;
- absorver `PER-107` em `PER-106`;
- tratar abertura de `PER-106` como ato constitutivo do vínculo;
- promover ou rebaixar `TRN-108` ou `TRN-110`;
- criar novo `PER-ID`;
- impor baseline visual;
- iniciar Product Engineering.

## 22. Critérios de aceite funcional

O consumo de `PER-106` é aceitável quando:

1. vínculos reais da Pessoa são reconhecíveis;
2. estado do vínculo é distinguível de papel;
3. papel é distinguível de autoridade;
4. disponibilidade e presença não são confundidas com participação;
5. categorias não formam ranking;
6. não existe score de engajamento;
7. não existe comparação entre participantes;
8. aprovação é reconhecida como ato que forma o vínculo;
9. abrir `PER-106` não é apresentado como criação do vínculo;
10. não abrir `PER-106` não desfaz aprovação;
11. repetição do evento não duplica vínculo;
12. última atualização relevante só aparece quando houver dado legítimo;
13. não lidos não criam pressão artificial;
14. `PER-106` não se transforma em feed;
15. `PER-107` permanece responsabilidade separada;
16. `TRN-108` permanece integralmente validada;
17. `TRN-110` permanece integralmente validada;
18. abrir a Central exige ação explícita;
19. abrir a Central não altera vínculo ou presença;
20. estados vazios não geram julgamento;
21. pausa e encerramento permanecem distintos;
22. privacidade entre vínculos é preservada;
23. estados internos não criam novos `PER-ID`s;
24. erros não fabricam estado ou vínculo;
25. conteúdo sintético não se apresenta como real;
26. acessibilidade não depende apenas de cor ou posição;
27. Design preserva liberdade criativa dentro das autoridades;
28. Product Engineering permanece não liberado.

## 23. Lacunas que não podem ser preenchidas por inferência

Este Master não autoriza inventar:

- ranking ou fórmula de engajamento;
- ordem obrigatória entre Coletivos;
- regra de prioridade;
- handoff direto não registrado;
- reativação automática de vínculo pausado ou encerrado;
- política de recomendação a partir de estado vazio;
- arquitetura detalhada da Central de Atualizações;
- arquitetura técnica de notificações;
- novos estados canônicos;
- novas transições;
- novos `PER-ID`s;
- implementação de Product Engineering.

## 24. Estado

```text
PER-106
→ DOCUMENTED

MASTER
→ GKR-UX-PER106-MASTER-001 v0.1.0
→ CURRENT

TRN-108
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-110
→ INTEGRALLY VALIDATED / UNCHANGED

PER-107
→ SEPARATE RESPONSIBILITY

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-107 — Central de Atualizações`.
