---
id: UXA-032
title: Wireframe de Baixa Fidelidade do Mapa de Oportunidades — Referência para Computador
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-024
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
related:
  - UXA-002
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-020
  - UXA-022
  - UXA-023
normative: false
---

# Wireframe de Baixa Fidelidade do Mapa de Oportunidades — Referência para Computador

## 1. Finalidade

Este documento materializa a primeira referência do Mapa de Oportunidades para computador, preservando os contratos funcionais já validados no canal móvel.

A referência verifica como a superfície pode utilizar espaço amplo para manter simultaneamente contexto, pesquisa, filtros, área territorial, Lista da mesma consulta, oportunidade selecionada, explicabilidade, relação comercial, privacidade e continuidade para o Detalhe.

O incremento não cria um produto diferente, um novo catálogo ou uma experiência exclusiva para computador. Mapa e Lista continuam representando a mesma consulta territorial.

O artefato não representa design visual, identidade final, tecnologia cartográfica, dados de produção, algoritmo, componente técnico, responsividade concluída ou implementação.

## 2. Posição na experiência

O Mapa permanece uma superfície recorrente:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O item `Mapa` permanece selecionado na navegação principal.

A referência para computador não altera a ordem da primeira entrada e não transforma o Mapa em etapa obrigatória da jornada.

## 3. Artefatos visuais

### 3.1 Estado com resultados

![Referência para computador do Mapa de Oportunidades com resultados](../assets/wireframes/uxa-032-opportunity-map-desktop.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-032-opportunity-map-desktop.svg`

### 3.2 Estado sem resultados

![Referência para computador do Mapa de Oportunidades sem resultados](../assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg`

Dimensão de referência dos dois arquivos:

- canal: aplicação web para computador;
- largura: 1.440 pixels;
- altura: 1.024 pixels;
- condição territorial ilustrada: localização desativada, posição não acessada e região escolhida manualmente;
- condição funcional principal: Mapa e Lista da mesma consulta apresentados lado a lado;
- condição alternativa: consulta concluída com zero correspondências e cobertura verificável.

A dimensão verifica distribuição horizontal e densidade. Ela não define largura máxima, grade final, pontos de quebra, comportamento de tablet ou responsividade completa.

## 4. Pergunta da referência

> **Em uma tela ampla, a pessoa consegue compreender e controlar uma única consulta territorial enquanto vê, sem contradição, o Mapa, a Lista, os filtros, a privacidade, a seleção e as condições da oportunidade?**

## 5. Princípio de paridade entre canais

A referência para computador deverá preservar as mesmas regras funcionais do canal móvel.

Ela não poderá:

- criar filtros exclusivos sem equivalência funcional;
- alterar silenciosamente região, busca, filtros ou ordenação;
- utilizar uma fonte de resultados diferente da Lista móvel;
- transformar o painel lateral em catálogo independente;
- ativar localização por haver mais espaço disponível;
- revelar endereço, residência ou local sensível;
- promover publicidade como relevância funcional;
- criar personalização sem o gate aplicável.

Diferenças de disposição são permitidas. Diferenças de significado não são.

## 6. Estrutura de tela ampla

A referência utiliza quatro faixas funcionais:

```text
cabeçalho e navegação recorrente
→ contexto, estado territorial e pesquisa
→ filtros laterais + campo territorial + Lista da mesma consulta
→ oportunidade selecionada, explicações e ações
```

A área principal é distribuída em três colunas:

1. **painel de consulta e filtros**;
2. **campo territorial do Mapa**;
3. **Lista e oportunidade selecionada**.

As colunas pertencem à mesma consulta e deverão utilizar a mesma versão de dados.

## 7. Cabeçalho e navegação

O cabeçalho apresenta:

- identificação `Mapa de Oportunidades`;
- contexto `Agindo como`;
- navegação `Hoje | Jornada | Explorar | Mapa | Eu`;
- item `Mapa` selecionado;
- acesso a privacidade e controles de conta;
- indicação de exploração geral ou personalização aplicável.

O contexto ilustrado utiliza:

> **Agindo como: Pessoa**

> **Exploração geral · sem personalização**

A disposição horizontal não autoriza ocultar o contexto de atuação.

## 8. Localização opcional e região manual

O estado principal demonstra:

> **Localização desativada · posição não acessada**

> **Região manual · não é sua posição**

A pessoa poderá:

- alterar a região manual;
- ativar localização aproximada de forma voluntária;
- usar localização exata temporária com finalidade e duração explícitas;
- continuar sem compartilhar posição;
- abrir a explicação de privacidade.

O mapa não apresenta marcador da pessoa no estado ilustrado.

A região manual não poderá ser tratada como residência, posição atual ou histórico territorial.

## 9. Pesquisa e atualização territorial

A pesquisa permanece visível acima do conjunto principal e poderá abranger oportunidades, Organizações, Coletivos, atividades, eventos, categorias e regiões.

Quando a área cartográfica for movida, a superfície deverá oferecer:

> **Pesquisar nesta área**

A movimentação não atualiza resultados silenciosamente.

A região ativa, o texto pesquisado e o horário da atualização deverão permanecer reconhecíveis nos três painéis.

## 10. Painel de filtros

O painel esquerdo demonstra:

- filtros ativos;
- total consolidado;
- revisão individual;
- ação explícita para limpar filtros;
- período;
- preço;
- modalidade;
- acessibilidade;
- disponibilidade;
- categoria;
- Organização ou Coletivo;
- origem e confiança da fonte;
- relação comercial;
- vínculo com objetivo ou Próximo Passo somente quando o gate estiver atendido.

`Limpar filtros` não apaga busca ou região.

Filtros incompatíveis após alteração territorial deverão ser informados antes de remoção.

## 11. Mapa e Lista integrados

Em tela ampla, Mapa e Lista poderão ser apresentados simultaneamente.

A Lista lateral deverá declarar:

> **Lista territorial · mesma consulta do Mapa**

A apresentação simultânea não cria dois modos independentes. Deverão permanecer sincronizados:

- região;
- busca;
- filtros;
- quantidade;
- atualização;
- ordenação;
- oportunidade selecionada;
- explicação da origem;
- relação comercial;
- estado territorial.

A pessoa poderá ampliar o Mapa ou a Lista para leitura concentrada, sem redefinir a consulta.

## 12. Campo territorial

O campo central permanece o maior elemento visual e poderá mostrar:

- oportunidades;
- Organizações;
- Coletivos;
- eventos e atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos;
- agrupamentos numéricos;
- camadas e legenda.

Forma e texto deverão acompanhar qualquer uso de cor.

A ausência de marcador pessoal deverá ser coerente com o estado de localização.

## 13. Lista e comparação

A Lista lateral deverá permitir comparação rápida por:

- tipo;
- modalidade;
- região ou disponibilidade online;
- título;
- responsável;
- data ou prazo;
- preço;
- disponibilidade;
- acessibilidade;
- origem funcional;
- relação comercial.

Dados ausentes serão apresentados como não informados, não como inexistentes.

A ordenação deverá permanecer explícita e explicável.

## 14. Oportunidade selecionada

A seleção deverá ser reconhecível simultaneamente no Mapa e na Lista.

O painel da oportunidade selecionada apresenta:

- título e responsável;
- tipo e modalidade;
- região ou distância quando válida;
- data ou disponibilidade;
- preço e condições resumidas;
- acessibilidade;
- razão de presença na consulta;
- relação comercial;
- condição do endereço;
- ações `Ver detalhes`, `Salvar` e `Definir origem` ou rota quando aplicável.

A seleção não altera ordenação nem relevância.

O painel não substitui o Detalhe de Oportunidade.

## 15. Explicabilidade e relação comercial

A pessoa deverá poder abrir:

- `Por que aparece aqui?`;
- `Entender ordenação`;
- `Ver cobertura`;
- `Entender disponibilidade dos dados`;
- `Privacidade`;
- explicação da relação comercial.

A relação comercial permanece separada da razão funcional da presença e da posição na Lista.

Patrocínio, comissão, popularidade ou proximidade isolada não constituem recomendação pessoal.

## 16. Continuidade com o Detalhe

Ao abrir o Detalhe, deverão ser preservados quando aplicável:

- contexto `Agindo como`;
- região;
- busca;
- filtros;
- ordenação;
- quantidade;
- posição da Lista;
- oportunidade selecionada;
- estado de localização;
- origem da navegação.

Ao retornar, a pessoa deverá recuperar o mesmo contexto, salvo alteração de disponibilidade claramente informada.

## 17. Estado sem resultados para computador

O segundo artefato utiliza a mesma estrutura, com:

- região, busca e filtros preservados;
- `0 resultados correspondem a esta consulta`;
- `Consulta concluída · cobertura verificada`;
- ação `Ver cobertura`;
- mensagem limitada à consulta atual;
- revisão antes de aplicar qualquer ajuste;
- ações independentes para região, período, filtros e busca;
- `Desfazer` somente quando houver alteração identificada;
- exploração geral sem alterar a consulta territorial;
- tratamento de seleção anterior sem reinserir o item no total zero;
- equivalência entre o campo territorial e a Lista.

A área vazia do Mapa não é o único sinal. O diagnóstico e as ações são textuais.

## 18. Estados sem localização e sem mapa carregado

A Lista, os filtros, o diagnóstico e as ações essenciais deverão continuar operáveis quando:

- a localização estiver desativada;
- o fornecedor cartográfico estiver indisponível;
- o mapa não carregar;
- houver baixa conectividade;
- o dispositivo utilizar ampliação ou tecnologia assistiva.

A Lista constitui alternativa integral, não contingência inferior.

## 19. Privacidade e proteção territorial

A referência preserva:

- localização opcional;
- posição não acessada quando verdadeiro;
- região manual distinta da posição pessoal;
- ausência de localização de participantes;
- endereço protegido;
- origem específica sem rastreamento contínuo;
- ausência de histórico territorial para publicidade;
- ausência de inferência de residência;
- controles de finalidade, precisão e duração.

Mais espaço visual não autoriza mais coleta.

## 20. Acessibilidade e resiliência

A referência deverá:

- manter ordem de leitura coerente entre cabeçalho, filtros, Mapa, Lista e seleção;
- permitir salto direto para Mapa, Lista, filtros e oportunidade selecionada;
- anunciar quantidade, atualização, localização e estado da consulta;
- não depender somente de cor, posição ou cartografia;
- oferecer controles operáveis por teclado;
- manter textos compreensíveis isoladamente;
- preservar conteúdo durante falha cartográfica;
- permitir ampliação da Lista para leitura concentrada.

Este incremento não conclui conformidade técnica de acessibilidade.

## 21. Critérios de validação posterior

A validação funcional especializada deverá verificar:

- se a pessoa entende que Mapa e Lista representam a mesma consulta;
- se o painel de filtros não parece uma busca independente;
- se o contexto `Agindo como` permanece visível;
- se localização desativada e região manual são compreendidas;
- se a seleção é reconhecida no Mapa e na Lista;
- se quantidade, ordenação e atualização são consistentes;
- se explicação funcional e relação comercial permanecem separadas;
- se abrir e retornar do Detalhe preserva contexto;
- se o estado zero mantém diagnóstico e recuperação claros;
- se a Lista continua integral sem mapa carregado;
- se a distribuição horizontal não cria sobrecarga ou perda de prioridade.

## 22. Limites

Este incremento não:

- define fornecedor ou tecnologia de mapas;
- cria geocodificação, rotas ou rastreamento;
- define algoritmo de busca, recomendação ou ordenação;
- define cobertura de fontes de produção;
- cria dados, cidades ou oportunidades reais;
- define identidade visual, ícones, cores ou tipografia finais;
- conclui pontos de quebra ou responsividade;
- cria referência específica para tablet;
- cria protótipo navegável;
- executa teste de usabilidade;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto.

## 23. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente a referência do Mapa para computador;
2. criar o wireframe gráfico do início protegido;
3. criar a referência móvel da Página Inicial pública;
4. validar a revisão da compreensão inicial;
5. validar a transição para a primeira Tela Hoje;
6. criar outros estados especializados do Mapa;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
