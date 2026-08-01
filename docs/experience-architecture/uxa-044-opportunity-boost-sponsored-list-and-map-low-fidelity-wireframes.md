---
id: UXA-044
title: Wireframes de Baixa Fidelidade dos Estados Patrocinados para Lista e Mapa
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
parent: UXA-043
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
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.46
normative: false
---

# Wireframes de Baixa Fidelidade dos Estados Patrocinados para Lista e Mapa

## 1. Finalidade

Este documento materializa os estados patrocinados do Opportunity Boost nas superfícies territoriais de Lista e Mapa.

O pacote demonstra como a publicidade identificada poderá coexistir com uma única consulta territorial sem:

- substituir o primeiro resultado orgânico;
- alterar silenciosamente busca, filtros ou ordenação;
- transformar proximidade em afinidade;
- utilizar posição exata ou histórico territorial para publicidade;
- sobrepor marcador patrocinado a oportunidade orgânica;
- ampliar densidade quando houver pouca oferta orgânica;
- reduzir o catálogo orgânico quando a publicidade for ocultada.

O conjunto não representa design final, tecnologia cartográfica, algoritmo, campanha real, perfil publicitário, cobrança, protótipo, teste com usuários ou Engenharia de Produto.

## 2. Pergunta funcional do conjunto

> **A pessoa reconhece imediatamente quais unidades e marcadores são patrocinados, preserva a mesma consulta entre Lista e Mapa, compreende por que o conteúdo pago aparece e consegue ocultar ou desativar publicidade sem perder oportunidades orgânicas ou compartilhar localização?**

A pergunta ainda deverá ser respondida por validação funcional especializada dos wireframes.

## 3. Artefatos e dimensões

| Artefato | Canal | Dimensão |
|---|---|---:|
| Lista patrocinada territorial | aplicativo móvel | 390 × 844 |
| Lista patrocinada territorial | web para computador | 1.440 × 1.024 |
| Mapa patrocinado | aplicativo móvel | 390 × 844 |
| Mapa patrocinado | web para computador | 1.440 × 1.024 |

Todos os artefatos utilizam baixa fidelidade, dados ilustrativos e rótulos textuais independentes de cor.

## 4. Artefatos visuais

### 4.1 Lista patrocinada móvel

![Lista patrocinada móvel](../assets/wireframes/uxa-044-sponsored-list-mobile.svg)

`docs/assets/wireframes/uxa-044-sponsored-list-mobile.svg`

Demonstra:

- Lista territorial pertencente à superfície Mapa;
- região manual e posição não acessada;
- filtro patrocinado reversível;
- primeiro resultado orgânico;
- inventário pago posterior e delimitado;
- anunciante, gratuidade e natureza comercial;
- explicação e controles;
- próximo resultado orgânico;
- retorno ao Mapa sem perda de contexto.

### 4.2 Lista patrocinada para computador

![Lista patrocinada para computador](../assets/wireframes/uxa-044-sponsored-list-desktop.svg)

`docs/assets/wireframes/uxa-044-sponsored-list-desktop.svg`

Demonstra:

- consulta e privacidade em painel próprio;
- filtros territoriais preservados;
- primeiro resultado orgânico anterior ao anúncio;
- unidade patrocinada separada da ordenação;
- densidade e frequência declaradas;
- controles de publicidade independentes dos filtros de negócio;
- continuidade para o Mapa.

### 4.3 Mapa patrocinado móvel

![Mapa patrocinado móvel](../assets/wireframes/uxa-044-sponsored-map-mobile.svg)

`docs/assets/wireframes/uxa-044-sponsored-map-mobile.svg`

Demonstra:

- mapa sem marcador da posição da pessoa;
- região manual e localização desativada;
- marcadores orgânicos circulares;
- marcador patrocinado quadrado e textual;
- agrupamento com contagens orgânicas e patrocinadas separadas;
- ausência de sobreposição do marcador patrocinado;
- cartão pago selecionado com explicação e controles;
- filtro patrocinado reversível.

### 4.4 Mapa patrocinado para computador

![Mapa patrocinado para computador](../assets/wireframes/uxa-044-sponsored-map-desktop.svg)

`docs/assets/wireframes/uxa-044-sponsored-map-desktop.svg`

Demonstra:

- visão dividida com consulta, Mapa e Lista sincronizados;
- localização opcional e região manual;
- marcadores orgânicos e patrocinados distintos;
- agrupamentos com contagens separadas;
- primeiro resultado orgânico preservado na Lista;
- marcador e cartão patrocinados vinculados por identificador;
- controles reversíveis e catálogo orgânico preservado.

## 5. Uma única consulta territorial

Lista e Mapa permanecem representações da mesma consulta.

Devem permanecer sincronizados:

- contexto `Agindo como`;
- região ou área territorial;
- busca;
- filtros;
- quantidade de resultados orgânicos;
- estado do filtro patrocinado;
- atualização;
- seleção;
- explicação da origem;
- localização e privacidade.

Alternar entre Lista, Mapa, visão dividida ou foco não poderá iniciar uma nova campanha, alterar personalização, ativar localização ou reiniciar a consulta.

## 6. Ordem e densidade na Lista

A ordem demonstrada é:

```text
primeiro resultado orgânico
→ inventário patrocinado identificado
→ próximos resultados orgânicos
```

A unidade patrocinada:

- não ocupa posição orgânica;
- não altera ordenação por busca e filtros;
- não recebe selo de recomendação;
- não substitui oportunidade organicamente selecionada;
- não é contabilizada como resultado orgânico;
- não pode aparecer consecutivamente com outra unidade paga.

A densidade candidata máxima permanece em 20%.

Quando houver menos de quatro oportunidades orgânicas elegíveis, a quantidade de publicidade deverá ser reduzida. Ausência de inventário orgânico nunca aumenta a densidade paga.

## 7. Marcadores e agrupamentos no Mapa

Os artefatos utilizam a convenção de baixa fidelidade:

- `O` em forma circular — oportunidade orgânica;
- `P` em forma quadrada — oportunidade patrocinada;
- agrupamento textual — contagens orgânicas e patrocinadas separadas.

Cor não poderá ser o único meio de diferenciação.

Um marcador patrocinado:

- não poderá cobrir marcador orgânico;
- não poderá substituir marcador orgânico em agrupamento;
- não poderá receber área visual desproporcional;
- deverá preservar identificador textual no cartão selecionado;
- deverá abrir explicação e controles equivalentes aos cartões patrocinados;
- não poderá ser interpretado como posição da pessoa.

Agrupamentos deverão informar, por exemplo:

```text
4 orgânicos
1 patrocinado
```

A contagem combinada sem separação é proibida.

## 8. Localização e publicidade

O estado principal demonstra:

> **Região manual · localização desativada · posição não acessada**

A publicidade poderá utilizar somente critérios territoriais gerais permitidos e visíveis.

Não poderá utilizar:

- posição exata para segmentação contínua;
- histórico territorial sensível;
- residência inferida;
- deslocamento ou rota pessoal;
- localização de participantes;
- endereço protegido;
- proximidade isolada como afinidade ou recomendação.

Quando localização aproximada for voluntariamente autorizada para a consulta, a explicação deverá distinguir uso territorial da consulta e critérios da campanha.

Mais espaço de tela não autoriza mais coleta.

## 9. Filtro de conteúdo patrocinado

Lista e Mapa apresentam controle reversível para mostrar ou não oportunidades patrocinadas.

O controle:

- não começa oculto por decisão do anunciante;
- deverá refletir a preferência atual da pessoa;
- não apaga busca, região ou filtros de negócio;
- não reduz resultados orgânicos;
- não impede acesso ao Detalhe de oportunidades orgânicas;
- deverá permanecer sincronizado entre Lista e Mapa;
- poderá ser revisado e desfeito.

A preferência negativa prevalece sobre entrega contratada.

## 10. Explicação e controles

A unidade ou marcador patrocinado oferece:

- `Por que estou vendo isto?`;
- `Ocultar só esta campanha`;
- `Controles do anúncio`;
- `Abrir oportunidade`.

A explicação deverá separar:

- condição paga;
- anunciante ou financiador;
- critérios gerais utilizados;
- critérios protegidos não utilizados;
- eventual correspondência orgânica legítima;
- ausência de influência do pagamento sobre a correspondência;
- localização utilizada pela consulta, quando aplicável;
- controles disponíveis.

Ocultação, redução, desativação total, denúncia de conteúdo e contestação de dados permanecem ações distintas.

## 11. Continuidade e seleção

Ao alternar entre Lista e Mapa, abrir o Detalhe ou retornar, deverão ser preservados quando aplicável:

- região;
- busca;
- filtros;
- ordenação orgânica;
- posição da Lista;
- área do Mapa;
- seleção;
- estado do filtro patrocinado;
- localização e privacidade;
- origem da navegação.

Selecionar uma unidade paga não altera sua prioridade, não gera correspondência orgânica e não autoriza personalização.

## 12. Acessibilidade e linguagem

- natureza patrocinada deverá ser anunciada antes do título;
- forma, texto e rótulo acompanharão qualquer uso de cor;
- contagens de agrupamentos serão textuais;
- Mapa terá alternativa integral em Lista;
- localização, filtro patrocinado, seleção e relação comercial serão anunciáveis;
- controles terão nome, escopo e consequência;
- a interface não utilizará urgência, culpa ou escassez artificial;
- foco e leitura deverão preservar a ordem orgânico, patrocinado e orgânico.

Esta referência não conclui acessibilidade técnica.

## 13. Proteções preservadas

- primeiro resultado orgânico permanece orgânico;
- pagamento não compra relevância, afinidade, confiança, qualidade ou impacto;
- compreensão inicial, Momento Atual e Próximo Passo não alimentam publicidade;
- localização permanece opcional;
- posição exata e histórico territorial não alimentam campanhas;
- marcador patrocinado não encobre oportunidade orgânica;
- agrupamento separa contagens;
- baixa oferta orgânica reduz publicidade;
- nenhuma unidade paga aparece consecutivamente;
- ocultação não reduz o catálogo orgânico;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado pelo wireframe.

## 14. Limites

Este incremento não cria:

- validação funcional dos quatro wireframes;
- estados de erro ou ausência de inventário patrocinado;
- gestão de campanha ativa;
- relatório agregado;
- algoritmo de entrega ou leilão;
- perfil publicitário;
- tecnologia cartográfica;
- geocodificação, rota ou rastreamento;
- design final;
- protótipo navegável;
- teste com usuários;
- checkout, cobrança ou Engenharia de Produto.

## 15. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente e reformular os quatro wireframes da UXA-044;
2. criar wireframes de gestão da campanha ativa;
3. criar wireframe do relatório agregado;
4. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
5. testar posteriormente disclosure, densidade, frequência, marcadores e controles com Pessoas, Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
