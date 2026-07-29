---
id: UXA-042
title: Wireframes de Baixa Fidelidade do Cartão Patrocinado e da Explicação do Opportunity Boost
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-29
parent: UXA-041
depends_on:
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - GEM-007-A1
  - GEM-010-A2
related:
  - UXA-043
  - GPA-007
  - M7.45
normative: false
---

# Wireframes de Baixa Fidelidade do Cartão Patrocinado e da Explicação do Opportunity Boost

## 1. Finalidade

Este documento materializa as referências de baixa fidelidade do cartão patrocinado e da explicação `Por que estou vendo isto?` para o Opportunity Boost.

O conjunto representa a experiência da pessoa diante de uma oportunidade distribuída em inventário patrocinado identificado, preservando:

- primeiro resultado orgânico;
- separação entre posição paga e ordenação orgânica;
- natureza comercial anterior ao conteúdo;
- anunciante ou financiador identificado;
- preço ou gratuidade;
- critérios gerais utilizados;
- critérios protegidos não utilizados;
- controles de ocultação, redução, desativação, preferência, denúncia e contestação;
- reversibilidade das preferências;
- variação própria para Boost Social Financiado.

O conjunto não representa design final, algoritmo, perfil publicitário, campanha real, política jurídica final, protótipo, teste com usuários ou Engenharia de Produto.

## 2. Resultado funcional

A pergunta funcional do conjunto é:

> **A pessoa reconhece antes da interação que o conteúdo é patrocinado, compreende por que foi distribuído, distingue publicidade de recomendação e correspondência orgânica, conhece os critérios utilizados e não utilizados e consegue controlar ou contestar a experiência sem perder o catálogo orgânico?**

A UXA-043 respondeu afirmativamente após reformulação dos seis artefatos.

O conjunto é considerado **funcionalmente válido após reformulação**, sem equivaler a teste de usabilidade, design ou implementação.

## 3. Canal e dimensões

| Artefato | Canal | Dimensão |
|---|---|---:|
| cartão patrocinado padrão | aplicativo móvel | 390 × 844 |
| explicação patrocinada padrão | aplicativo móvel | 390 × 844 |
| cartão patrocinado padrão | web para computador | 1.440 × 1.024 |
| explicação patrocinada padrão | web para computador | 1.440 × 1.024 |
| cartão de Boost Social Financiado | aplicativo móvel | 390 × 844 |
| explicação do Boost Social Financiado | aplicativo móvel | 390 × 844 |

Todos os artefatos utilizam baixa fidelidade e conteúdo ilustrativo.

## 4. Artefatos visuais reformulados

### 4.1 Cartão patrocinado móvel

![Cartão patrocinado móvel](../assets/wireframes/uxa-042-sponsored-card-mobile.svg)

`docs/assets/wireframes/uxa-042-sponsored-card-mobile.svg`

Demonstra:

- primeiro resultado orgânico anterior ao espaço patrocinado;
- selo `Impulsionado · Conteúdo pago` antes do título;
- anunciante identificado;
- gratuidade, modalidade, capacidade e data;
- declaração de que posição paga não é recomendação;
- ação `Por que estou vendo isto?`;
- ocultação limitada à campanha;
- acesso nomeado aos controles do anúncio;
- preferências revisáveis e reversíveis.

### 4.2 Explicação patrocinada móvel

![Explicação patrocinada móvel](../assets/wireframes/uxa-042-sponsored-explanation-mobile.svg)

`docs/assets/wireframes/uxa-042-sponsored-explanation-mobile.svg`

Demonstra:

- campanha paga identificada;
- oportunidade e anunciante;
- critérios gerais utilizados;
- critérios expressamente não utilizados;
- ausência de lista de visualizadores;
- ausência de influência sobre correspondência orgânica;
- ocultação da campanha;
- redução de conteúdos semelhantes;
- desativação de oportunidades patrocinadas;
- revisão e reversão de preferências;
- denúncia e contestação como fluxos separados.

### 4.3 Cartão patrocinado para computador

![Cartão patrocinado para computador](../assets/wireframes/uxa-042-sponsored-card-desktop.svg)

`docs/assets/wireframes/uxa-042-sponsored-card-desktop.svg`

Demonstra:

- consulta e filtros objetivos preservados;
- primeiro resultado orgânico;
- espaço patrocinado posterior e delimitado;
- identificação comercial anterior ao conteúdo;
- densidade, frequência e baixa oferta orgânica como regras separadas;
- ocultação limitada à campanha;
- destino compreensível dos controles gerais;
- ausência de alteração da ordenação orgânica.

### 4.4 Explicação patrocinada para computador

![Explicação patrocinada para computador](../assets/wireframes/uxa-042-sponsored-explanation-desktop.svg)

`docs/assets/wireframes/uxa-042-sponsored-explanation-desktop.svg`

Demonstra:

- relação paga;
- inventário orgânico separado;
- critérios gerais utilizados;
- dados protegidos e contextos pessoais não utilizados;
- ausência de lista de pessoas expostas;
- correspondência orgânica tratada separadamente quando existir;
- controles com escopos distintos;
- preferência reversível;
- denúncia e contestação separadas.

### 4.5 Cartão móvel do Boost Social Financiado

![Cartão móvel do Boost Social Financiado](../assets/wireframes/uxa-042-social-financed-card-mobile.svg)

`docs/assets/wireframes/uxa-042-social-financed-card-mobile.svg`

Demonstra:

- primeiro resultado orgânico materializado;
- rótulo `Impulsionamento social financiado` posterior ao orgânico;
- oportunidade gratuita;
- Coletivo beneficiário;
- Organização ou parceiro financiador;
- finalidade declarada do financiamento;
- ausência de autoridade do financiador;
- ausência de transferência de plano pago;
- controles equivalentes aos demais conteúdos patrocinados.

### 4.6 Explicação móvel do Boost Social Financiado

![Explicação móvel do Boost Social Financiado](../assets/wireframes/uxa-042-social-financed-explanation-mobile.svg)

`docs/assets/wireframes/uxa-042-social-financed-explanation-mobile.svg`

Demonstra:

- financiador e beneficiário identificados;
- finalidade e gratuidade;
- declaração de que financiamento não é recomendação;
- critérios gerais utilizados;
- ausência de ampliação silenciosa;
- dados e poderes não concedidos ao financiador;
- métricas futuras somente agregadas;
- ocultação, redução, desativação, reversão, denúncia e contestação separadas.

## 5. Ordem orgânica e inventário patrocinado

As referências demonstram a seguinte ordem:

```text
consulta e filtros objetivos
→ primeiro resultado orgânico
→ espaço patrocinado identificado
→ próximos resultados orgânicos
```

O cartão patrocinado:

- não substitui o primeiro resultado orgânico;
- não participa silenciosamente do ranking;
- não recebe selo de recomendação;
- não apresenta aderência pessoal comprada;
- não transforma pagamento em qualidade, confiança ou impacto;
- não aumenta quando houver pouca oferta orgânica.

A mesma ordem é materializada na variação de Boost Social Financiado.

A densidade candidata máxima permanece em 20%, sem duas unidades patrocinadas consecutivas e com redução da publicidade quando faltar inventário orgânico.

## 6. Identificação anterior ao conteúdo

A natureza comercial deverá ser reconhecível antes do título da oportunidade por:

- rótulo textual;
- posição própria;
- anunciante ou financiador;
- informação de gratuidade ou preço;
- linguagem sem ambiguidade entre anúncio e recomendação.

Cor, ícone ou borda não poderão ser o único meio de identificação.

## 7. Explicação de distribuição

A explicação separa:

```text
Motivo
→ campanha paga identificada

Critérios utilizados
→ região, idioma, categoria, modalidade, data, preço ou preferência geral permitida

Critérios não utilizados
→ relato protegido, compreensão inicial, Momento Atual, Próximo Passo, mensagens e inferências sensíveis

Controles
→ ocultar, mostrar menos, desativar patrocinados, revisar preferências, denunciar ou contestar
```

Quando existir correspondência orgânica legítima para a mesma oportunidade, a interface deverá explicar separadamente:

- razão orgânica;
- condição patrocinada;
- critérios de cada uma;
- ausência de influência do pagamento sobre a correspondência.

Quando não existir correspondência orgânica naquele caso, a explicação poderá declarar essa condição sem criar aderência artificial.

## 8. Controles e escopos

- `Ocultar esta campanha` remove somente a campanha específica nas superfícies aplicáveis;
- `Mostrar menos deste tipo` altera preferência geral identificada;
- `Não mostrar oportunidades patrocinadas` desativa inventário patrocinado nas superfícies suportadas;
- `Revisar e desfazer preferências` permite compreender e reverter escolhas anteriores;
- `Denunciar conteúdo ou informação` abre fluxo de integridade e não equivale a preferência;
- `Contestar uso indevido de dados` abre fluxo separado de privacidade e governança.

Nenhuma opção começa selecionada.

Ocultar publicidade não poderá:

- reduzir acesso ao catálogo orgânico;
- ocultar oportunidades orgânicas da mesma categoria;
- ser interpretado como desinteresse orgânico;
- impedir busca, filtros, Lista ou Mapa;
- ser contornado por outra campanha equivalente.

## 9. Boost Social Financiado

A variação social apresenta:

- Coletivo beneficiário;
- financiador;
- finalidade do financiamento;
- oportunidade gratuita;
- ausência de seleção individual pelo financiador;
- ausência de autoridade sobre relevância, ordem ou resultado;
- ausência de acesso a relato, compreensão, jornada ou lista de pessoas;
- ausência de concessão automática de plano pago ao Coletivo Livre.

A experiência declara que financiamento amplia distribuição e não constitui recomendação institucional da Guivos.

## 10. Acessibilidade e linguagem

- leitores de tela deverão anunciar a natureza comercial antes do conteúdo;
- identificação patrocinada não dependerá somente de cor;
- anunciante, financiador e beneficiário terão rótulos textuais;
- preço e gratuidade permanecerão compreensíveis;
- ações terão nome, escopo e consequência;
- preferência, denúncia e contestação serão distinguíveis;
- o retorno ao catálogo orgânico permanecerá evidente;
- não serão usados padrões de urgência, culpa ou escassez artificial.

## 11. Limites

Este incremento não cria:

- estados patrocinados para Lista ou Mapa;
- wireframes de gestão da campanha ativa;
- relatório agregado do anunciante;
- design visual;
- protótipo navegável;
- teste com usuários;
- algoritmo, perfil publicitário ou motor de entrega;
- checkout, cobrança ou Engenharia de Produto.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados patrocinados para Lista e Mapa;
2. validar funcionalmente e reformular esses estados;
3. criar wireframes de gestão da campanha ativa;
4. criar wireframe do relatório agregado;
5. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost.

Nenhum ato é iniciado automaticamente.
