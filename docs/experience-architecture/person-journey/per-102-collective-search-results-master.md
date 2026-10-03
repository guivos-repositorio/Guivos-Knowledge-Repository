---
id: GKR-UX-PER102-MASTER-001
title: Jornada da Pessoa — PER-102 — Resultados de Busca de Coletivos — Documento Mestre de Superfície
status: active
version: 0.1.1
maturity: current_surface_design_definition
depends_on:
  - UXA-056
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
tags:
  - person-journey
  - per-102
  - collectives
  - discovery
  - search-results
  - surface-master
---

# Jornada da Pessoa — PER-102 — Resultados de Busca de Coletivos — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-102 — Resultados de Busca de Coletivos` para designer humana, IA opcional, Produto, UX, Research, Privacidade e Engenharia.

A superfície existe para permitir que a Pessoa **compreenda o conjunto produzido pela descoberta, reconheça os critérios e a origem que o sustentam, refine a consulta e escolha conscientemente um Coletivo para compreender melhor**.

Ela não é Perfil Público do Coletivo, participação, acompanhamento, solicitação de entrada, ranking de popularidade nem autorização implícita para personalização sensível.

## 2. Papel na Jornada

```text
PER-101 — EXPLORAR COLETIVOS
→ TRN-101 / LOCALMENTE VALIDADA
→ PER-102 — RESULTADOS DE BUSCA DE COLETIVOS
→ SELECIONAR UM RESULTADO
→ TRN-102 / PARTIAL
→ PER-103 — PERFIL PÚBLICO DO COLETIVO
```

`PER-102` governa resultados, seus estados e refinamento. `PER-103` governa a compreensão pública do Coletivo selecionado.

## 3. Trabalho da Pessoa

A Pessoa precisa conseguir, conforme aplicável:

1. reconhecer o que foi pesquisado ou explorado;
2. compreender filtros, território, modalidade e origem aplicáveis;
3. distinguir resultados orgânicos, sugestões, recomendações e publicidade quando coexistirem;
4. compreender por que um resultado pode aparecer quando explicabilidade for material;
5. revisar, remover ou alterar critérios;
6. reconhecer carregamento, erro e ausência de resultados;
7. recuperar a consulta sem ampliação silenciosa;
8. reconhecer disponibilidade e visibilidade declaradas sem interpretá-las como garantia;
9. selecionar um Coletivo para abrir seu Perfil Público;
10. voltar à exploração preservando contexto legítimo;
11. permanecer sem criar vínculo apenas por visualizar ou selecionar um resultado.

## 4. Contexto recebido de PER-101

`TRN-101` pode preservar, quando aplicável:

- consulta;
- filtros;
- origem;
- território;
- modalidade;
- contexto autorizado necessário à continuidade.

A superfície deve tornar critérios materialmente ativos compreensíveis e revisáveis.

Contexto recebido não pode ser ampliado silenciosamente nem transformado em preferência permanente por padrão.

## 5. Conjunto de resultados

Cada resultado pode apresentar somente informação suficiente e legitimamente pública para apoiar identificação e escolha, conforme disponibilidade real e proteção aplicável.

Podem ser pertinentes:

- nome ou identificação pública permitida;
- propósito ou descrição curta;
- categoria;
- território em granularidade autorizada;
- modalidade;
- estado de funcionamento;
- disponibilidade declarada de novas entradas;
- acessibilidade declarada;
- relação institucional material quando pública;
- origem ou natureza da apresentação quando necessária à compreensão.

A lista não obriga Design a exibir todos os campos simultaneamente.

Informação reservada ao Perfil Público, gestão ou participação não deve ser antecipada apenas para enriquecer o resultado.

## 6. Origem e natureza da descoberta

A superfície deve preservar distinção entre:

- resultado de busca;
- exploração por categoria;
- resultado territorial;
- sugestão da Guivos;
- recomendação de uma pessoa;
- convite;
- link compartilhado;
- conteúdo patrocinado.

Uma origem não pode se apresentar como outra.

Quando a origem influenciar materialmente o conjunto ou a ordem, a Pessoa deve conseguir compreendê-la de forma proporcional.

## 7. Ordenação orgânica

A ordenação orgânica pode considerar, conforme autoridade:

- correspondência com consulta;
- filtros escolhidos;
- território e modalidade;
- disponibilidade de entrada;
- atualidade das informações;
- acessibilidade declarada;
- coerência entre descrição e funcionamento confirmado;
- segurança e confiabilidade;
- preferências explicitamente autorizadas.

Não podem dominar a ordenação:

- quantidade de participantes;
- volume de publicações ou mensagens;
- duração na plataforma;
- compra de plano;
- publicidade;
- popularidade sem contexto.

Este Master não define algoritmo, pesos, score ou ranking universal.

## 8. Conteúdo patrocinado

Conteúdo patrocinado deve permanecer inequivocamente identificado como publicidade.

Publicidade:

- não altera silenciosamente a ordenação orgânica;
- não recebe aparência de relevância neutra;
- não implica confiança, legitimidade ou adequação;
- não substitui ausência de resultado orgânico;
- não substitui nem ocupa o lugar do primeiro resultado orgânico quando resultados orgânicos existirem;
- não utiliza contexto sensível sem autoridade própria.

A compra de plano ou relação comercial não pode elevar silenciosamente um Coletivo no conjunto orgânico.

## 9. Visibilidade, encontrabilidade e proteção

Resultados respeitam a autoridade vigente do Coletivo.

Podem existir estados como público, público com aprovação, não listado, privado, protegido e temporariamente fechado.

Coletivos não listados, privados ou protegidos não podem ser tornados encontráveis contra sua configuração.

Coletivos sensíveis podem exigir nome reduzido, descrição limitada, contagem oculta, não encontrabilidade, convite ou outras proteções. Completude visual não justifica exposição adicional.

## 10. Localização e território

Localização precisa não é requisito para resultados.

Território pode decorrer, conforme autoridade, de cidade, região, território informado ou proximidade aproximada legitimamente autorizada.

```text
RESULTADO TERRITORIAL
≠ RESIDÊNCIA DA PESSOA
≠ POSIÇÃO ATUAL
≠ HISTÓRICO DE LOCALIZAÇÃO
```

A superfície não pode inferir ou expor relações além da base autorizada.

## 11. Refinamento

A Pessoa deve poder compreender e revisar critérios materialmente ativos.

Refinar pode incluir, quando aplicável:

- alterar consulta;
- adicionar ou remover filtros;
- alterar território;
- alterar modalidade;
- limpar critérios;
- retornar à exploração.

Refinamento não cria preferência permanente por padrão.

A superfície não pode ampliar silenciosamente consulta, território ou filtros para aumentar a quantidade de resultados.

## 12. Carregamento

Durante carregamento, a experiência deve comunicar que o conjunto ainda não está concluído sem fabricar resultados, quantidade ou certeza.

Resultados anteriores não devem parecer atuais se estiverem sendo substituídos por nova consulta sem indicação adequada.

Falha parcial ou atraso não autoriza apresentação de dado sintético como real.

## 13. Erro e recuperação

Quando resultados não puderem ser obtidos, a superfície deve:

- preservar critérios necessários à recuperação;
- distinguir erro de ausência legítima de resultados;
- permitir nova tentativa ou revisão de critérios quando aplicável;
- não atribuir culpa à Pessoa;
- não ampliar critérios silenciosamente;
- não preencher a falha com publicidade ou resultados fabricados.

Erro técnico não equivale a inexistência de Coletivos.

## 14. Ausência de resultados

Zero resultados é um estado legítimo de `PER-102`.

A superfície deve manter compreensível o que foi pesquisado e permitir revisão consciente.

Pode oferecer caminhos para alterar critérios, desde que a alteração seja explícita.

Não pode:

- ampliar automaticamente território;
- remover filtros sem informar;
- trocar a intenção pesquisada;
- apresentar publicidade como resposta orgânica;
- inventar Coletivos;
- afirmar inexistência universal quando apenas o conjunto consultado não retornou resultado.

## 15. Seleção de resultado e PER-103

Selecionar um resultado inicia a continuidade para `PER-103 — Perfil Público do Coletivo` por `TRN-102`.

`TRN-102` permanece `partial` e este Master não promove sua maturidade.

A continuidade pode preservar o contexto necessário para retorno e explicação da origem, sem transferir contexto pessoal desnecessário ao Coletivo.

```text
SELECIONAR RESULTADO
≠ ACOMPANHAR
≠ PARTICIPAR
≠ SOLICITAR ENTRADA
≠ CRIAR VÍNCULO
```

## 16. Retorno

Ao retornar de uma continuidade legitimamente suportada, a Pessoa deve poder recuperar contexto pertinente da descoberta quando isso estiver contratado.

Retorno não autoriza:

- reconstrução de filtros por inferência sensível;
- criação de preferência permanente;
- marcação do Coletivo como acompanhado;
- compartilhamento de identidade com o Coletivo.

Este Master não cria transições ausentes do Registry.

## 17. Privacidade

A superfície segue minimização por finalidade.

Não pode ocorrer silenciosamente:

- uso de conteúdo protegido da Journey;
- uso de relatos sensíveis;
- inferência de localização precisa;
- perfilamento sensível a partir de consultas;
- compartilhamento da identidade da Pessoa com Coletivos apenas por exposição ou seleção;
- expansão de consentimento;
- transformação de consulta em vínculo.

Explicabilidade deve ser proporcional quando contexto autorizado influenciar materialmente apresentação ou ordenação.

## 18. Acessibilidade

Consulta, filtros, origem, publicidade, estados, resultados e ações essenciais devem ser compreensíveis sem depender exclusivamente de cor, posição, ícone, motion ou outra pista isolada.

Informações declaradas de acessibilidade podem apoiar escolha sem inferir necessidades pessoais não autorizadas.

## 19. Estados funcionais

Estados pertencentes a `PER-102` podem incluir:

- carregamento inicial;
- conjunto de resultados;
- critérios refinados;
- atualização do conjunto;
- conteúdo patrocinado identificado;
- ausência de resultados;
- erro recuperável;
- retorno com contexto preservado.

```text
ESTADO INTERNO
≠ NOVA SUPERFÍCIE
≠ NOVO PER-ID
```

## 20. Linguagem

Evitar:

- “melhor” ou “mais adequado” sem autoridade específica;
- “mais relevante” sem critério legítimo;
- “mais popular” como proxy de qualidade;
- “perto de você” sem base territorial autorizada;
- “recomendado para você” quando a origem não sustentar recomendação;
- publicidade apresentada como resultado orgânico;
- “nenhum Coletivo existe” quando somente a consulta atual não retornou resultados;
- pressão para participar.

## 21. Conteúdo sintético para exploração

Design e prototipação podem usar conteúdo claramente fictício para explorar:

- conjuntos com diferentes quantidades;
- filtros e refinamento;
- carregamento;
- erro;
- zero resultados;
- resultados territoriais;
- conteúdo patrocinado;
- Coletivo temporariamente fechado;
- proteções de visibilidade.

Conteúdo sintético nunca pode ser apresentado como Coletivo, quantidade, disponibilidade, território, patrocínio ou condição real.

## 22. Liberdade criativa de Design

Este Master governa significado, responsabilidade, limites e critérios funcionais — não composição estética.

Designer humana pode definir tipografia, cores, imagens, ícones, grid, densidade, hierarquia, motion, microinterações, responsividade e linguagem gráfica, preservando o contrato funcional.

Não existe baseline visual obrigatório para `PER-102`.

## 23. Uso de IA

IA pode apoiar exploração e produção sob direção humana.

IA não pode:

- inventar Coletivos ou resultados reais;
- fabricar disponibilidade, condição de entrada ou localização;
- preencher zero-results ou erro com dados fictícios apresentados como reais;
- ampliar critérios silenciosamente;
- presumir localização precisa;
- usar contexto sensível sem autoridade;
- confundir orgânico, sugestão, recomendação e publicidade;
- transformar popularidade em qualidade;
- criar vínculo por exposição ou seleção;
- criar novos `PER-IDs`;
- promover `TRN-102`;
- definir algoritmo de ranking como autoridade;
- iniciar Product Engineering.

## 24. Critérios funcionais de aceitação

Uma futura solução visual é funcionalmente aceitável quando:

1. preserva consulta, filtros e origem pertinentes;
2. torna critérios materialmente ativos compreensíveis e revisáveis;
3. respeita visibilidade e encontrabilidade;
4. protege Coletivos sensíveis;
5. não exige localização precisa;
6. distingue publicidade de resultado orgânico e preserva o primeiro resultado orgânico contra substituição patrocinada;
7. não permite que compra de plano, publicidade ou popularidade dominem ordenação orgânica;
8. não define ranking universal como autoridade;
9. governa carregamento sem fabricar resultados;
10. distingue erro de ausência legítima de resultados;
11. permite recuperação sem ampliação silenciosa;
12. trata zero-results como estado legítimo;
13. não preenche zero-results com publicidade disfarçada;
14. não fabrica Coletivos, disponibilidade ou quantidade;
15. preserva `TRN-102` em maturidade `partial`;
16. seleção não cria vínculo;
17. protege contexto sensível e identidade da Pessoa;
18. não cria novos `PER-IDs`;
19. não impõe baseline visual;
20. IA permanece subordinada às autoridades;
21. Product Engineering permanece não liberado.

## 25. Limites e lacunas

Este Master não define:

- layout ou wireframe;
- sistema visual;
- tecnologia de busca;
- algoritmo ou pesos de ranking;
- Perfil Público do Coletivo;
- participação ou acompanhamento;
- solicitação de entrada;
- gestão do Coletivo;
- comunicação ou chat;
- moderação operacional completa;
- implementação técnica.

Lacunas permanecem explícitas e não podem ser completadas por inferência.

## 26. Estado governado

```text
PER-102 MASTER
→ GKR-UX-PER102-MASTER-001 v0.1.1
→ CURRENT SURFACE DESIGN DEFINITION

TRN-101
→ LOCALLY VALIDATED / UNCHANGED

TRN-102
→ PARTIAL / UNCHANGED

NEW PER-IDS
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED

NEXT DOCUMENTATION TARGET
→ PER-103 — PERFIL PÚBLICO DO COLETIVO
```
