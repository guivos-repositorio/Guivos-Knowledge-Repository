---
id: UXA-032
title: Wireframe de Baixa Fidelidade do Mapa de Oportunidades — Referência para Computador
status: active
version: 0.2.0
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
  - UXA-033
normative: false
---

# Wireframe de Baixa Fidelidade do Mapa de Oportunidades — Referência para Computador

## 1. Finalidade

Este documento materializa a referência funcionalmente validada e reformulada do Mapa de Oportunidades para computador.

A superfície utiliza espaço amplo para manter simultaneamente contexto, consulta territorial, pesquisa, filtros, Mapa, Lista da mesma consulta, oportunidade selecionada, explicabilidade, relação comercial, privacidade e continuidade para o Detalhe.

O incremento não cria produto, catálogo ou experiência exclusivos para computador. Mapa e Lista continuam representando a mesma consulta territorial.

O artefato não representa identidade visual final, tecnologia cartográfica, dados de produção, algoritmo, componente técnico, responsividade concluída ou implementação.

A validação funcional está registrada em [UXA-033](uxa-033-opportunity-map-desktop-functional-validation-and-reformulation.md).

## 2. Posição na experiência

O Mapa permanece uma superfície recorrente:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O item `Mapa` permanece selecionado.

A referência para computador não altera a primeira entrada e não transforma o Mapa em etapa obrigatória.

## 3. Artefatos visuais reformulados

### 3.1 Estado com resultados

![Referência reformulada para computador do Mapa com resultados](../assets/wireframes/uxa-032-opportunity-map-desktop.svg)

Arquivo:

`docs/assets/wireframes/uxa-032-opportunity-map-desktop.svg`

### 3.2 Estado sem resultados

![Referência reformulada para computador do Mapa sem resultados](../assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg)

Arquivo:

`docs/assets/wireframes/uxa-032-opportunity-map-no-results-desktop.svg`

Dimensão de referência:

- canal: aplicação web para computador;
- largura: 1.440 pixels;
- altura: 1.024 pixels;
- localização ilustrada: desativada;
- posição: não acessada;
- região: escolhida manualmente;
- disposição padrão: visão dividida;
- estado principal: oito resultados;
- estado alternativo: zero resultados com cobertura verificável.

A dimensão verifica distribuição e densidade. Ela não define pontos de quebra, tablet ou responsividade completa.

## 4. Pergunta validada

> **Em tela ampla, a pessoa consegue compreender e controlar uma única consulta territorial enquanto vê Mapa, Lista, filtros, seleção, privacidade e condições sem contradição ou sobrecarga funcional?**

A UXA-033 concluiu que a resposta é positiva após as reformulações descritas neste documento.

## 5. Paridade entre canais

A referência para computador preserva as regras do canal móvel.

Ela não poderá:

- criar filtros exclusivos sem equivalência funcional;
- alterar silenciosamente região, busca, filtros ou ordenação;
- utilizar fonte de resultados diferente da Lista móvel;
- transformar a Lista em catálogo independente;
- ativar localização por haver mais espaço;
- revelar residência ou local sensível;
- promover publicidade como relevância funcional;
- criar personalização sem gate;
- mudar significado ao alterar disposição.

Diferenças de disposição são permitidas. Diferenças de significado não são.

## 6. Estrutura de tela ampla

A referência utiliza:

```text
cabeçalho e navegação recorrente
→ contexto territorial e privacidade
→ consulta territorial ativa e pesquisa
→ filtros + Mapa + Lista
→ painel contextual recolhível da seleção
```

A área principal é distribuída em três colunas:

1. **consulta e filtros**;
2. **campo territorial do Mapa**;
3. **Lista da mesma consulta**.

As três colunas utilizam a mesma região, busca, filtros, quantidade e atualização.

## 7. Faixa compartilhada da consulta

A reformulação acrescenta uma declaração transversal:

> **Consulta territorial ativa · mesma região, busca, filtros e atualização**

No estado com resultados:

> **8 resultados · atualizada agora**

No estado sem resultados:

> **0 resultados · cobertura verificada · atualizada agora**

A faixa evita a percepção de três buscas independentes.

Nenhum painel poderá manter versão divergente da consulta.

## 8. Cabeçalho, contexto e navegação

O cabeçalho apresenta:

- `Mapa de Oportunidades`;
- `Agindo como: Pessoa`;
- `Exploração geral · sem personalização`;
- `Hoje | Jornada | Explorar | Mapa | Eu`;
- `Mapa` selecionado;
- conta e controles;
- privacidade territorial.

A disposição horizontal não autoriza ocultar o contexto de atuação.

## 9. Localização opcional e região manual

O estado principal demonstra:

> **Localização desativada · posição não acessada**

> **Região manual · não é sua posição**

A pessoa poderá alterar a região, ativar localização aproximada voluntariamente, usar localização exata temporária com finalidade e duração explícitas ou continuar sem compartilhar posição.

O Mapa não apresenta marcador pessoal.

Região manual não equivale a residência, posição atual ou histórico territorial.

## 10. Pesquisa territorial

A pesquisa permanece acima do conjunto principal.

A consulta reconhece oportunidades, Organizações, Coletivos, atividades, eventos, categorias e regiões.

Busca, região e filtros permanecem dimensões distintas.

`Limpar busca` não apaga região ou filtros.

## 11. Consistência dos filtros

Resumo e controles detalhados utilizam os mesmos valores:

- `Hoje e próximos 7 dias`;
- `Gratuitas e preço informado`;
- `Presencial e online`;
- `Acessibilidade confirmada ou informada`.

O painel também poderá abrir categoria, disponibilidade, fonte, Organização, Coletivo e relação comercial.

Vínculo com objetivo ou Próximo Passo somente poderá aparecer quando o gate estiver atendido.

`Limpar filtros` não apaga busca ou região.

Filtros incompatíveis após alteração territorial serão informados antes de qualquer remoção.

## 12. Visão dividida e modos de foco

A disposição padrão declara:

> **Visão dividida ativa**

As ações são:

- `Focar no Mapa`;
- `Focar na Lista`;
- `Voltar à visão dividida` nos estados concentrados.

Foco não cria nova consulta e não modifica região, busca, filtros, quantidade, atualização, ordenação, seleção, localização ou permissões.

Ao retornar, o contexto e a posição de leitura deverão ser preservados quando materialmente possível.

## 13. Movimento do Mapa

Antes de qualquer movimento, o campo declara:

> **Área atual · resultados atualizados**

`Pesquisar nesta área` somente aparece após movimento material do Mapa.

O estado pendente deverá declarar:

> **Área movida · resultados ainda correspondem à consulta anterior**

Mover o campo cartográfico não executa nova consulta silenciosamente.

## 14. Campo territorial

O Mapa permanece o maior elemento visual e poderá apresentar:

- oportunidades;
- Organizações;
- Coletivos;
- eventos;
- atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos;
- agrupamentos;
- camadas e legenda.

Forma e texto acompanham qualquer uso de cor.

A legenda declara que nenhum símbolo representa a posição da pessoa.

## 15. Lista territorial comparável

A Lista declara:

> **Lista territorial · mesma consulta ativa do Mapa**

Cada cartão visível deverá apresentar, de forma compacta:

- tipo;
- título;
- responsável;
- modalidade;
- região ou condição online;
- data ou prazo;
- preço;
- disponibilidade;
- acessibilidade;
- origem funcional;
- relação comercial;
- `Por que aparece aqui?`.

Dados ausentes serão declarados como não informados.

A ordenação informa seu critério e oferece:

> **Entender ordenação**

## 16. Seleção sincronizada

A mesma oportunidade utiliza o vínculo:

> **Marcador 1 · selecionada**

O identificador conecta:

- marcador no Mapa;
- cartão na Lista;
- painel contextual.

A seleção não altera ordenação, relevância ou permissões.

Ela permanece ao focar Mapa, focar Lista, abrir o Detalhe ou retornar.

## 17. Painel contextual recolhível

A oportunidade selecionada abre um:

> **Painel contextual recolhível**

O painel apresenta:

- título e responsável;
- tipo e modalidade;
- região ou distância válida;
- data ou disponibilidade;
- preço;
- vagas;
- acessibilidade;
- condição do endereço;
- razão funcional;
- relação comercial;
- `Ver detalhes`;
- `Salvar`;
- `Definir origem`, quando aplicável;
- ação `Recolher`.

Recolher o painel preserva seleção e devolve espaço para comparação.

O painel não substitui o Detalhe.

## 18. Explicabilidade e relação comercial

A pessoa poderá abrir:

- `Por que aparece aqui?`;
- `Entender ordenação`;
- `Ver cobertura`;
- `Entender disponibilidade dos dados`;
- `Privacidade`;
- explicação da relação comercial.

A relação comercial utiliza rótulo explícito e permanece separada da origem funcional e da posição na Lista.

Patrocínio, comissão, popularidade ou proximidade isolada não constituem recomendação pessoal.

## 19. Continuidade com o Detalhe

Ao abrir e retornar do Detalhe, permanecem quando aplicável:

- `Agindo como`;
- região;
- busca;
- filtros;
- quantidade;
- atualização;
- ordenação;
- posição da Lista;
- seleção;
- modo de foco;
- estado de localização;
- origem da navegação.

Mudança real de disponibilidade será informada.

## 20. Estado sem resultados

O estado alternativo preserva:

- região;
- busca;
- quatro filtros consistentes;
- contexto;
- localização desativada;
- região manual;
- total zero;
- cobertura;
- atualização;
- seleção anterior, quando existir.

A recuperação principal fica concentrada no painel `Consulta e filtros`.

O centro apresenta:

- `0 resultados correspondem a esta consulta`;
- `Sua consulta permanece intacta`;
- cobertura limitada à atualização atual;
- `Revisar consulta preservada`;
- `Explorar sem alterar esta consulta`.

A Lista apresenta o mesmo diagnóstico e orienta o uso do painel de consulta, sem repetir todas as ações.

## 21. Recuperação consciente

As ações independentes permanecem:

- `Ampliar região`;
- `Alterar período`;
- `Revisar filtros`;
- `Editar busca`;
- `Desfazer`, quando houver alteração identificável.

A pessoa revisa valor atual, valor proposto, dimensões preservadas e efeito possível antes de aplicar.

A interface não altera automaticamente região, período, filtros, busca, localização ou personalização.

## 22. Seleção anterior no total zero

Quando houver seleção incompatível com a consulta atual, a Lista declara:

> **Seleção anterior fora da consulta atual**

A oportunidade não integra o total zero.

A pessoa poderá abrir o Detalhe, remover a seleção, desfazer alteração compatível ou manter a consulta.

## 23. Estados sem mapa carregado

Lista, filtros, diagnóstico e ações essenciais continuam operáveis quando:

- localização estiver desativada;
- fornecedor cartográfico estiver indisponível;
- Mapa não carregar;
- houver baixa conectividade;
- houver ampliação ou tecnologia assistiva.

A Lista é alternativa integral, não contingência inferior.

## 24. Privacidade territorial

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

## 25. Acessibilidade funcional

A ordem funcional é:

```text
cabeçalho e contexto
→ consulta territorial ativa
→ pesquisa
→ filtros
→ Mapa
→ Lista
→ painel contextual
```

A superfície deverá permitir acesso direto a consulta, filtros, Mapa, Lista e seleção.

Quantidade, atualização, localização, cobertura, foco e seleção deverão ser anunciáveis textualmente.

Esta referência não conclui conformidade técnica de acessibilidade.

## 26. Resultado da validação

A UXA-033 considera a referência **funcionalmente válida após reformulação**.

Foram corrigidos:

- contradições entre filtros resumidos e detalhados;
- ambiguidade de `Ampliar`;
- atualização territorial sem estado pendente;
- vínculo insuficiente da seleção;
- cartões secundários pouco comparáveis;
- painel selecionado que comprimida a Lista sem condição de recolhimento;
- repetição de recuperação no estado zero.

## 27. Limites

Este incremento não:

- define tecnologia de mapas;
- cria geocodificação, rotas ou rastreamento;
- define algoritmo de busca, recomendação ou ordenação;
- define cobertura real de fontes;
- cria dados reais;
- define identidade visual final;
- conclui pontos de quebra ou responsividade;
- cria referência específica para tablet;
- cria protótipo navegável;
- executa teste de usabilidade;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto.

## 28. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o wireframe gráfico do início protegido;
2. criar a referência móvel da Página Inicial pública;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar outros estados especializados do Mapa;
6. criar referência específica para tablet, caso priorizada;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
