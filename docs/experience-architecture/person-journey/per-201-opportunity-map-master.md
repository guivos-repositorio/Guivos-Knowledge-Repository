---
id: GKR-UX-PER201-MASTER-001
title: Jornada da Pessoa — PER-201 — Mapa de Oportunidades — Documento Mestre de Superfície
status: active
version: 0.1.0
maturity: current_surface_design_definition
depends_on:
  - GKR-UXA-004
  - GKR-UXA-025
  - GKR-UXA-098
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-VIEW-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
tags:
  - person-journey
  - per-201
  - opportunities
  - map
  - territorial-discovery
  - surface-master
---

# Jornada da Pessoa — PER-201 — Mapa de Oportunidades — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-201 — Mapa de Oportunidades` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

`Mapa de Oportunidades` existe para permitir que a Pessoa **explore e selecione oportunidades dentro de uma consulta territorial compreensível**, preservando controle sobre região, busca, filtros, localização e mudança de modo.

A superfície não é mecanismo de pressão comercial, ranking humano, prova de relevância pessoal, rastreador de participantes nem autorização implícita para uso contínuo de localização.

## 2. Papel na Jornada

As continuidades correntes relevantes são:

```text
PER-201 — MAPA
↔ TRN-210 / INTEGRALMENTE VALIDADA
↔ PER-202 — LISTA

PER-201 — MAPA
→ TRN-204 / INTEGRALMENTE VALIDADA
→ PER-203 — DETALHE
```

Uma oportunidade institucional elegível pode alcançar a descoberta por `TRN-203`, integralmente validada, sem garantia de distribuição.

Mapa e Lista representam a mesma consulta territorial. Alternar entre eles não cria nova consulta, oportunidade, interesse ou autorização.

## 3. Trabalho da Pessoa

A Pessoa precisa conseguir, conforme contexto:

1. compreender qual região ou área está sendo consultada;
2. compreender a origem da região utilizada;
3. pesquisar oportunidades;
4. aplicar, revisar e remover filtros;
5. alterar conscientemente a região;
6. decidir quando atualizar resultados após mudança territorial;
7. explorar oportunidades territorialmente;
8. compreender quando localização do dispositivo está ou não autorizada;
9. usar região manual sem declarar residência ou posição atual;
10. alternar entre Mapa e Lista preservando a consulta;
11. compreender estado sem resultados;
12. selecionar uma oportunidade e decidir se deseja abrir seu Detalhe;
13. distinguir conteúdo orgânico de conteúdo patrocinado;
14. reconhecer condições comerciais relevantes;
15. desativar localização e continuar por alternativas compatíveis;
16. recuperar-se de indisponibilidade cartográfica sem perder acesso ao catálogo quando possível.

## 4. Unidade funcional da consulta

A descoberta territorial deve preservar, conforme aplicável:

```text
CONSULTA TERRITORIAL
→ região / área
→ origem da região
→ estado de localização
→ busca
→ filtros
→ resultados
→ seleção
```

Esses elementos formam uma consulta compreensível.

Alterar um elemento não autoriza a Guivos a alterar silenciosamente os demais.

## 5. Mapa e Lista

`PER-201 — Mapa` e `PER-202 — Lista` são modos da mesma descoberta territorial.

`TRN-210` deve preservar, quando aplicável:

- região;
- busca;
- filtros;
- identidade das oportunidades;
- contexto necessário à continuidade.

```text
MAPA ↔ LISTA
→ SAME TERRITORIAL QUERY
→ ≠ NOVA JORNADA
→ ≠ NOVA AUTORIZAÇÃO
```

A Lista não é fallback inferior. Ela é modo textual integral da mesma descoberta.

## 6. Região e contexto territorial

A região consultada deve ser compreensível e revisável.

Uma região manual:

```text
REGIÃO MANUAL
≠ RESIDÊNCIA
≠ POSIÇÃO ATUAL
≠ HISTÓRICO TERRITORIAL
```

Nenhuma posição pessoal deve ser presumida quando localização estiver desativada.

Mover ou alterar a área de interesse não deve recalcular silenciosamente a consulta sem sinal claro. A Pessoa deve manter controle sobre quando atualizar os resultados territoriais.

## 7. Localização e privacidade

Localização do dispositivo é opcional.

Pode estar:

- não autorizada;
- temporariamente autorizada;
- indisponível;
- substituída por região manual.

Autorizar localização para uma finalidade não autoriza:

- histórico territorial;
- rastreamento contínuo;
- publicidade baseada em trajetória;
- inferência de residência;
- exposição da localização de participantes;
- retenção além da finalidade legítima.

Somente a precisão necessária deve ser utilizada.

## 8. Busca

Busca direta deve operar dentro do contexto compreensível da consulta.

Consultas sensíveis exigem proteção proporcional. Busca relacionada a saúde, finanças, religião, violência, situação jurídica, emprego, moradia, assistência social ou vulnerabilidade não pode ser reutilizada para publicidade sem autorização específica.

Sugestões de busca não podem transformar inferência sensível em fato.

## 9. Filtros

Filtros podem refinar a consulta conforme autoridade vigente.

A Pessoa deve compreender quais filtros estão ativos e poder revisá-los ou removê-los.

Filtros comerciais podem permitir mostrar ou ocultar oportunidades patrocinadas, mas relação comercial não pode ser ocultada nem operar como relevância humana automática.

## 10. Atualização territorial

A ação equivalente a “pesquisar nesta área” deve preservar autonomia sobre quando recalcular resultados.

Atualização não pode:

- ampliar raio silenciosamente;
- remover filtros sem indicação;
- ativar localização;
- substituir região manual;
- inferir residência;
- criar histórico territorial indevido.

Quando houver alteração concreta e reversível, recuperação e desfazer podem ser oferecidos de forma coerente.

## 11. Estado sem resultados

Zero resultados é estado legítimo da consulta atual.

```text
ZERO RESULTS
→ ≠ AUSÊNCIA DE POSSIBILIDADES PARA A PESSOA
→ ≠ FALHA HUMANA
→ ≠ AUTORIZAÇÃO PARA AMPLIAR CRITÉRIOS
```

Nesse estado, região, busca e filtros devem permanecer compreensíveis e revisáveis.

Cobertura ou atualização devem ser explicitadas somente quando houver evidência.

A recuperação pode envolver editar região, busca ou filtros conscientemente. Nenhum critério deve ser ampliado automaticamente.

## 12. Oportunidade selecionada

Uma seleção no Mapa pode apresentar contexto suficiente para a Pessoa decidir se deseja abrir o Detalhe.

Selecionar ou abrir oportunidade não significa:

```text
INTERESSE CONFIRMADO
INSCRIÇÃO
COMPRA
CONTRATAÇÃO
ACEITAÇÃO
RESULTADO
EVOLUÇÃO
```

`TRN-204` preserva a identidade da oportunidade e retorno coerente ao contexto de descoberta.

## 13. Oportunidade Ativa

Oportunidade Ativa é meio potencialmente disponível e legitimamente admissível ao contexto; não é recomendação definitiva nem garantia de resultado.

Disponibilidade isolada, patrocínio, estoque ou presença territorial não bastam para estabelecer relevância humana.

Pode legitimamente não existir nenhuma oportunidade adequada à consulta ou contexto atual.

## 14. Orgânico, patrocinado e relação comercial

Inventário patrocinado deve permanecer identificado.

```text
PATROCÍNIO
≠ RELEVÂNCIA HUMANA
≠ PRIORIDADE PESSOAL
≠ GARANTIA DE RESULTADO
```

Relação comercial não pode:

- substituir silenciosamente resultado orgânico;
- eliminar alternativas não patrocinadas;
- fabricar urgência pessoal;
- converter escassez comercial em prioridade;
- ocultar comissão ou relação relevante;
- explorar mudança sensível da Pessoa.

Ordenação comercial só pode existir em área explicitamente publicitária conforme autoridade própria.

## 15. Relevância e elegibilidade

Compatibilidade deve utilizar somente contexto autorizado e finalidade legítima.

Elegibilidade sensível não deve ser inferida sem autoridade e finalidade adequadas.

A interface não deve expor inferências sensíveis desnecessariamente.

Quando houver explicação de relevância, deve ser proporcional e não revelar dados ou inferências que não precisam ser expostos.

## 16. Condição e disponibilidade

A oportunidade pode possuir condições como disponibilidade imediata, futura, limitada, lista de espera, sob consulta ou indisponibilidade.

Essas condições pertencem à oportunidade e não representam urgência pessoal.

Alterações, pausa, encerramento ou inelegibilidade durante a navegação exigem revalidação do estado corrente antes de ação material.

## 17. Privacidade territorial

O Mapa não deve:

- mostrar localização de participantes;
- expor endereço exato de atividade protegida antes da autorização apropriada;
- registrar localização contínua sem finalidade;
- inferir deslocamento;
- converter região escolhida em dado residencial;
- reutilizar consulta sensível comercialmente sem autoridade.

Localização da oportunidade e localização estimada/autorizada da Pessoa devem permanecer distinguíveis.

## 18. Estados funcionais

Estados pertencentes à responsabilidade de `PER-201` permanecem na mesma superfície quando não existir novo `PER-ID`.

Podem incluir, conforme aplicável:

- consulta disponível;
- localização não autorizada;
- localização temporariamente autorizada;
- região manual;
- atualização territorial pendente;
- carregamento;
- resultados disponíveis;
- zero resultados;
- oportunidade selecionada;
- mapa indisponível;
- baixa conectividade;
- erro recuperável.

```text
ESTADO INTERNO
≠ NOVA SUPERFÍCIE
≠ NOVO PER-ID
```

## 19. Indisponibilidade do Mapa e baixa conectividade

Indisponibilidade cartográfica não deve eliminar acesso à descoberta quando os dados necessários estiverem disponíveis por outro modo governado.

A continuidade com Lista deve preservar a consulta.

Falha de mapa não autoriza alteração silenciosa de região, filtros, localização ou critérios.

## 20. Retorno e continuidade

Ao retornar de `PER-203`, o contexto territorial deve permanecer coerente quando ainda válido.

Se a oportunidade ou consulta tiver mudado materialmente, a interface deve refletir o estado corrente em vez de fabricar continuidade antiga.

Retorno não confirma interesse nem produz resultado.

## 21. Explicabilidade

A Pessoa deve conseguir compreender, quando material:

- qual região está sendo consultada;
- se localização está sendo usada;
- origem da região;
- busca e filtros ativos;
- por que resultados mudaram;
- se existe patrocínio ou relação comercial;
- condição relevante da oportunidade;
- por que não há resultados quando a causa for conhecida;
- quando o estado precisa ser atualizado.

Explicabilidade não autoriza exposição de inferências sensíveis.

## 22. Linguagem

A linguagem deve ser neutra e informativa.

Evitar pressão como:

- “você está perdendo oportunidades”;
- “não perca esta oportunidade única”;
- “a oportunidade que mudará sua vida”;
- formulações que transformem proximidade, escassez ou patrocínio em urgência pessoal.

Ausência de resultados deve ser comunicada sem julgamento.

## 23. Acessibilidade

A descoberta não deve depender exclusivamente de mapa visual.

Informações e ações essenciais devem possuir alternativa compreensível quando aplicável, inclusive por meio da Lista.

Cor, posição, marcador, tamanho ou animação não podem ser os únicos meios de comunicar condição, patrocínio, seleção ou estado.

## 24. Conteúdo sintético para exploração

Design e prototipação podem usar conteúdo claramente fictício para explorar:

- diferentes regiões;
- localização desativada;
- região manual;
- busca e filtros;
- resultados orgânicos;
- oportunidade patrocinada identificada;
- zero resultados;
- oportunidade selecionada;
- mapa indisponível;
- baixa conectividade.

Conteúdo sintético não pode ser apresentado como oferta real, disponibilidade real, preço real, localização real ou comportamento implementado.

## 25. Liberdade criativa de Design

Este Master governa significado, responsabilidade, limites e critérios funcionais — não estética nem tecnologia cartográfica.

Designer humana pode definir tipografia, cores, ilustrações, imagens, ícones, grid, composição, componentes, densidade, hierarquia, motion, microinterações, responsividade e linguagem gráfica, preservando o contrato funcional.

Não existe baseline visual obrigatório para `PER-201`.

## 26. Uso de IA

IA pode apoiar exploração e produção sob direção humana.

IA não pode:

- inventar oportunidades reais;
- inventar disponibilidade, preço, localização ou condição;
- presumir localização da Pessoa;
- inferir residência;
- ampliar consulta silenciosamente;
- transformar patrocínio em relevância;
- ocultar relação comercial;
- inferir elegibilidade sensível sem autoridade;
- criar interesse, inscrição, compra ou evolução por navegação;
- criar novo `PER-ID` para estado interno;
- alterar `TRN-203/204/210`;
- iniciar Product Engineering.

## 27. Critérios funcionais de aceitação

Uma futura solução visual é funcionalmente aceitável quando:

1. preserva a consulta territorial;
2. mantém Mapa e Lista como modos da mesma descoberta;
3. preserva `TRN-204/210` e o contrato aplicável de `TRN-203`;
4. localização permanece opcional;
5. região manual não é tratada como residência ou posição atual;
6. a Pessoa controla atualização territorial;
7. busca e filtros permanecem compreensíveis;
8. zero resultados é estado legítimo;
9. recuperação não amplia critérios automaticamente;
10. selecionar oportunidade não confirma interesse ou ação;
11. patrocínio e relação comercial permanecem identificados;
12. alternativas orgânicas não são silenciosamente substituídas;
13. privacidade territorial é preservada;
14. consultas sensíveis recebem proteção proporcional;
15. indisponibilidade do mapa não destrói a continuidade possível;
16. estados internos não criam novos `PER-IDs`;
17. não existe baseline visual imposta;
18. IA permanece subordinada às autoridades;
19. Product Engineering permanece não liberado.

## 28. Limites e lacunas

Este Master não define:

- tecnologia ou fornecedor cartográfico;
- layout, wireframe ou sistema visual;
- algoritmo de relevância;
- ranking comercial;
- geofencing contínuo;
- rastreamento territorial;
- arquitetura técnica;
- detalhe integral de `PER-202` ou `PER-203`;
- comportamento posterior a fronteiras externas;
- novas superfícies;
- implementação.

Lacunas permanecem explícitas e não podem ser completadas por inferência.

## 29. Estado governado

```text
PER-201 MASTER
→ GKR-UX-PER201-MASTER-001 v0.1.0
→ CURRENT SURFACE DESIGN DEFINITION

TRN-203
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-204
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-210
→ INTEGRALLY VALIDATED / UNCHANGED

PRODUCT ENGINEERING
→ NOT RELEASED

NEXT DOCUMENTATION TARGET
→ PER-202 — LISTA DE OPORTUNIDADES
```
