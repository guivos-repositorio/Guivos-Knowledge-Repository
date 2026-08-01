---
id: UXA-045
title: Validação Funcional e Reformulação dos Wireframes dos Estados Patrocinados para Lista e Mapa
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
parent: UXA-044
depends_on:
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-024
  - UXA-025
  - UXA-028
  - UXA-029
  - UXA-032
  - UXA-033
  - UXA-038
  - UXA-039
  - UXA-042
  - UXA-043
  - UXA-044
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.47
normative: false
---

# Validação Funcional e Reformulação dos Wireframes dos Estados Patrocinados para Lista e Mapa

## 1. Finalidade

Este documento valida funcionalmente os quatro wireframes criados pela UXA-044 e registra as reformulações necessárias para que Lista e Mapa preservem uma única consulta territorial, distinção orgânica, transparência publicitária, localização opcional e controles reversíveis.

A pergunta de validação é:

> **A pessoa distingue oportunidades orgânicas e patrocinadas nos dois modos, compreende o que pertence à consulta e o que pertence à preferência publicitária, mantém região, busca, filtros, seleção e privacidade ao alternar Lista e Mapa e consegue ocultar ou desativar publicidade sem perder o catálogo orgânico?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova design visual final, tecnologia cartográfica, algoritmo, perfil publicitário, política de categorias, densidade definitiva, cobrança, acessibilidade técnica, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. Lista patrocinada para aplicativo móvel;
2. Lista patrocinada para computador;
3. Mapa patrocinado para aplicativo móvel;
4. Mapa patrocinado para computador;
5. paridade entre Lista e Mapa;
6. região, busca, filtros e atualização;
7. quantidade de oportunidades orgânicas e unidades pagas;
8. preferência publicitária;
9. primeiro resultado orgânico;
10. marcador patrocinado e agrupamentos;
11. seleção entre marcador e cartão;
12. movimentação da área territorial;
13. localização e privacidade;
14. ocultação, desativação, denúncia e contestação;
15. densidade e baixa oferta orgânica;
16. acessibilidade e linguagem clara.

## 4. Lacunas identificadas

### 4.1 Quantidade total ambígua

Os quatro artefatos apresentavam `8 resultados` sem esclarecer se a quantidade incluía unidades patrocinadas.

A ambiguidade poderia:

- misturar catálogo orgânico e inventário pago;
- sugerir que pagamento criou uma oportunidade organicamente elegível;
- dificultar a comparação entre Lista e Mapa;
- impedir a pessoa de compreender o efeito de ocultar publicidade.

### 4.2 Preferência publicitária confundida com filtro de negócio

O controle `Patrocinados: sim` ou `Patrocinados: mostrar` aparecia junto de busca e filtros, sem declarar que se tratava de uma preferência publicitária separada.

A pessoa poderia interpretar que:

- patrocinado era uma categoria de oportunidade;
- alterar a preferência mudaria os filtros de negócio;
- desativar publicidade reduziria o catálogo orgânico;
- o anunciante controlava o estado do filtro.

### 4.3 Limite interno exposto como critério de interface

As referências para computador mostravam `Máximo candidato: 20%` como item do painel de publicidade.

O percentual é uma proteção arquitetural candidata e não uma decisão operacional que a pessoa precise configurar. A apresentação poderia criar falsa precisão, expectativa contratual ou interpretação de que densidade era um filtro pessoal.

### 4.4 Efeito da ocultação entre Lista e Mapa insuficiente

Os cartões ofereciam ocultação da campanha, mas não declaravam claramente que a mesma unidade seria removida nos dois modos sem afetar região, busca, filtros e resultados orgânicos.

### 4.5 Seleção territorial sem vínculo funcional explícito

O Mapa mostrava marcador `P1` e cartão patrocinado, mas não nomeava o marcador como selecionado nem declarava que selecionar no Mapa não altera a ordem da Lista, afinidade ou recomendação.

### 4.6 Movimentação do Mapa sem gate visível

O Mapa não apresentava de forma suficientemente clara que mover ou ampliar a área não altera automaticamente a consulta.

Sem um gate explícito, a pessoa poderia perder o contexto territorial, acionar nova busca involuntariamente ou interpretar a movimentação como autorização de localização.

## 5. Reformulação aprovada

### 5.1 Contagens separadas

Lista e Mapa passam a apresentar, no exemplo:

```text
8 oportunidades orgânicas
1 oportunidade patrocinada exibida
4 filtros de oportunidades
```

A quantidade orgânica permanece estável quando publicidade é ocultada ou desativada.

Unidades pagas não são contabilizadas como resultados orgânicos.

### 5.2 Filtros de oportunidades e preferência publicitária

A interface separa duas áreas:

- `Filtros de oportunidades` — período, preço, modalidade, acessibilidade e demais critérios de negócio;
- `Preferência publicitária` — mostrar, ocultar, reduzir ou desativar oportunidades patrocinadas.

Alterar a preferência publicitária não modifica:

- região;
- busca;
- filtros de oportunidades;
- quantidade de resultados orgânicos;
- ordenação orgânica;
- localização ou privacidade.

O estado exibido representa a preferência atual da pessoa, não uma decisão do anunciante.

### 5.3 Densidade em linguagem funcional

O percentual candidato de 20% deixa de aparecer como controle da pessoa.

A interface utiliza linguagem funcional:

- publicidade limitada;
- unidades pagas nunca consecutivas;
- pouca oferta orgânica reduz publicidade.

A proteção quantitativa permanece na arquitetura e deverá ser calibrada posteriormente.

### 5.4 Ocultação sincronizada

A ação passa a informar:

> **Ocultar esta campanha na Lista e no Mapa.**

A consequência é:

- remover somente a campanha específica nos dois modos;
- preservar oportunidades orgânicas;
- preservar região, busca e filtros;
- preservar localização e privacidade;
- permitir revisão e reversão conforme a política aplicável.

Ocultar, mostrar menos, desativar patrocinados, denunciar conteúdo e contestar dados permanecem ações distintas.

### 5.5 Seleção do marcador patrocinado

O marcador `P1` passa a possuir estado textual `selecionado` e vínculo explícito com o cartão `P1 selecionado`.

A interface declara:

- selecionar no Mapa não muda a ordem da Lista;
- seleção não cria correspondência orgânica;
- proximidade não equivale a afinidade;
- marcador pago não é a posição da pessoa;
- seleção não autoriza personalização.

### 5.6 Gate `Pesquisar nesta área`

Mover, ampliar ou reduzir o Mapa não altera automaticamente a consulta.

A atualização territorial exige ação explícita:

> **Pesquisar nesta área**

Antes da confirmação, permanecem preservados:

- região vigente;
- busca;
- filtros;
- quantidade de resultados;
- seleção;
- preferência publicitária;
- localização e privacidade.

Mover o Mapa não equivale a conceder acesso à localização.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- Lista e Mapa representam a mesma consulta territorial;
- alternar entre os modos não reinicia busca ou filtros;
- resultados orgânicos e unidades pagas possuem contagens separadas;
- primeiro resultado da Lista permanece orgânico;
- inventário pago não participa da ordenação orgânica;
- preferência publicitária está separada dos filtros de oportunidades;
- ocultar ou desativar patrocinados preserva o catálogo orgânico;
- marcadores orgânicos e patrocinados são distinguíveis por forma, texto e rótulo;
- agrupamentos apresentam contagens orgânicas e patrocinadas separadas;
- marcador patrocinado não cobre ou substitui marcador orgânico;
- marcador selecionado e cartão selecionado possuem o mesmo identificador;
- seleção no Mapa não muda a ordem da Lista;
- proximidade, distância e seleção não são afinidade ou recomendação;
- localização permanece opcional;
- posição exata não alimenta a campanha;
- mover o Mapa não executa nova consulta automaticamente;
- `Pesquisar nesta área` é uma decisão explícita;
- baixa oferta orgânica reduz publicidade;
- duas unidades pagas consecutivas permanecem proibidas;
- ocultação, preferência, denúncia e contestação possuem escopos próprios;
- nenhuma campanha, tecnologia cartográfica, cobrança ou perfil publicitário é criado pelos artefatos.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-044-sponsored-list-mobile.svg`;
2. `uxa-044-sponsored-list-desktop.svg`;
3. `uxa-044-sponsored-map-mobile.svg`;
4. `uxa-044-sponsored-map-desktop.svg`.

Os artefatos permanecem em baixa fidelidade, com dimensões de 390 × 844 pixels para móvel e 1.440 × 1.024 pixels para computador.

## 8. Proteções preservadas

- pagamento não compra posição orgânica, relevância, afinidade, confiança, qualidade ou impacto;
- primeiro resultado da Lista permanece orgânico;
- compreensão inicial, Momento Atual e Próximo Passo não alimentam publicidade;
- localização permanece opcional;
- posição exata e histórico territorial não alimentam campanhas;
- marcador patrocinado não encobre oportunidade orgânica;
- agrupamentos não combinam contagens sem distinção;
- baixa oferta orgânica reduz publicidade;
- ocultação não reduz busca, filtros, Lista, Mapa ou catálogo orgânico;
- preferência negativa prevalece sobre entrega contratada;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado;
- movimentação do Mapa não autoriza localização ou nova consulta.

## 9. Limites

Esta validação não cria:

- estados de erro ou ausência de inventário patrocinado;
- gestão de campanha ativa;
- relatório agregado;
- algoritmo de entrega ou leilão;
- perfil publicitário;
- tecnologia cartográfica;
- geocodificação, rota ou rastreamento;
- política final de densidade ou frequência;
- design visual final;
- protótipo navegável;
- teste com usuários;
- checkout, cobrança ou Engenharia de Produto.

## 10. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar os wireframes de gestão da campanha ativa;
2. criar o wireframe do relatório agregado;
3. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
4. criar estados de erro, inventário insuficiente e preferência publicitária;
5. testar posteriormente disclosure, densidade, frequência, marcadores, localização e controles com Pessoas, Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
