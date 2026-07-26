---
id: UXA-024
title: Wireframe de Baixa Fidelidade do Mapa de Oportunidades
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-007
  - UXA-010
  - UXA-012
related:
  - UXA-020
  - UXA-022
  - UXA-025
normative: false
---

# Wireframe de Baixa Fidelidade do Mapa de Oportunidades

## 1. Finalidade

Este documento materializa a referência gráfica móvel do Mapa de Oportunidades como superfície própria da navegação recorrente da Guivos.

A versão 0.2.0 incorpora a reformulação governada pela **UXA-025 — Validação Funcional e Reformulação do Mapa de Oportunidades**.

O wireframe verifica hierarquia, contexto de atuação, pesquisa, alternância entre mapa e lista, filtros, resultados, região, camadas, localização, oportunidade selecionada, privacidade territorial e continuidade para o Detalhe de Oportunidade.

Ele não representa mapa real, design visual, tecnologia cartográfica, dados de produção ou implementação.

## 2. Posição na experiência

O Mapa não entra entre a Página Inicial pública e a Tela Hoje.

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A superfície também poderá ser acessada:

- pela exploração geral da Home, sem personalização;
- por Explorar;
- pelo bloco contextual `Perto de mim` da Tela Hoje;
- pelo Detalhe de Oportunidade;
- por um local salvo, Organização, Coletivo, atividade, evento ou ponto de apoio.

## 3. Artefato visual reformulado

![Wireframe reformulado de baixa fidelidade do Mapa de Oportunidades](../assets/wireframes/uxa-024-opportunity-map-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- estado principal: pessoa autenticada, compreensão inicial revisada, gate de personalização atendido e localização aproximada autorizada.

## 4. Hierarquia validada

A ordem funcional da superfície é:

```text
nome da superfície e contexto de atuação
→ pesquisa
→ Mapa ou Lista
→ filtros ativos e limpeza
→ quantidade de resultados
→ Pesquisar nesta área
→ mapa e controles territoriais
→ legenda
→ localização e privacidade
→ oportunidade selecionada
→ detalhe, salvamento e rota contextual
→ navegação recorrente
```

A área territorial permanece o maior campo visual, mas não oculta busca, filtros, resultados, privacidade ou ações do item selecionado.

## 5. Contexto e pesquisa

O cabeçalho utiliza:

> **Agindo como: Minha jornada**

Quando a pessoa estiver representando uma Organização ou atuando em um Coletivo, participante, papel e escopo deverão permanecer explícitos.

A pesquisa poderá abranger oportunidade, Organização, Coletivo, atividade, evento, categoria, cidade, bairro ou região.

## 6. Mapa e Lista

A superfície permite alternar entre:

```text
Mapa
↔ Lista
```

A alternância não cria dois catálogos independentes.

Busca, filtros, região, quantidade de resultados, item selecionado e explicação de relevância deverão permanecer sincronizados quando aplicável.

## 7. Filtros e resultados

O estado principal apresenta filtros ativos de período, distância e gratuidade.

A marca textual `✓` demonstra atividade sem depender somente de cor.

A superfície também apresenta:

- quantidade total de filtros ativos;
- quantidade de resultados na área visível;
- ação `Limpar filtros`;
- acesso ao conjunto ampliado.

O conjunto ampliado poderá incluir categoria, data, horário, preço, modalidade, disponibilidade, elegibilidade, acessibilidade, idioma, Organização, Coletivo, origem, patrocínio, confiança da fonte e vínculo com objetivo ou Próximo Passo.

A limpeza de filtros não deverá apagar a busca ou alterar a região silenciosamente.

## 8. Atualização da região

Quando a pessoa mover ou ampliar o mapa, a interface deverá oferecer:

> **Pesquisar nesta área**

A movimentação territorial não atualiza resultados silenciosamente. A pessoa reconhece que a área mudou e decide quando deseja consultar a nova região.

## 9. Área territorial e camadas

O mapa esquemático poderá apresentar:

- oportunidades;
- Organizações;
- Coletivos;
- eventos e atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos.

Agrupamentos numéricos poderão representar vários itens em uma área.

A legenda utiliza forma e texto para distinguir tipos. Cor nunca será o único meio de identificação.

A ação `Camadas` permite mostrar ou ocultar tipos sem apagar filtros de negócio ou preferências permanentes silenciosamente.

## 10. Controles territoriais

A superfície oferece controles para:

- visualizar camadas;
- aumentar ou reduzir escala;
- reposicionar a visualização;
- pesquisar nesta área;
- alterar raio;
- usar localização exata temporária, aproximada, cidade informada ou região selecionada;
- desativar localização;
- revisar privacidade.

## 11. Localização e privacidade

O estado principal declara:

> **Localização aproximada · raio 10 km**

> Sua posição exata não está visível.

A pessoa pode abrir `Alterar` e `Privacidade` diretamente no bloco territorial.

Localização exata temporária exige finalidade, duração e ação de encerramento.

O Mapa não deverá:

- mostrar localização de participantes;
- revelar residência ou local sensível;
- expor endereço protegido antes da condição aplicável;
- exigir rastreamento contínuo;
- manter localização exata sem finalidade e prazo;
- utilizar histórico sensível para publicidade;
- presumir interesse apenas por proximidade.

## 12. Oportunidade selecionada

Ao selecionar um ponto, a pessoa recebe um cartão resumido com:

- tipo e modalidade;
- título;
- Organização, Coletivo ou fonte responsável;
- distância ou região;
- data, prazo ou disponibilidade;
- preço, gratuidade ou faixa;
- vagas ou capacidade quando material;
- acessibilidade;
- razão resumida de relevância;
- relação comercial;
- ações para abrir detalhes, salvar ou criar rota quando aplicável.

O cartão não substitui o Detalhe de Oportunidade. Condições completas, elegibilidade, riscos, política de cancelamento, composição de preço e autoridade permanecem na superfície especializada.

## 13. Rota contextual

`Criar rota` somente aparece quando o item possui local físico, o endereço pode ser utilizado naquele estado e a ação não revela residência ou local sensível.

O estado ilustrado declara:

> Endereço disponível · rota permitida neste estado

Quando o endereço estiver protegido, a ação deverá ser substituída por `Ver área aproximada`, `Entender quando o endereço será liberado` ou `Revisar condições de acesso`.

## 14. Relevância e exploração

### 14.1 Antes do gate

A superfície poderá apresentar conteúdo geral, institucional, editorial ou resultante de busca explícita.

Ela não deverá afirmar adequação ao Momento Atual.

### 14.2 Depois do gate

A Guivos poderá explicar relevância com base em objetivo, Próximo Passo, preferência, localização autorizada, disponibilidade e elegibilidade conhecida.

A pessoa poderá abrir `Por que aparece aqui?`, corrigir contexto, ocultar categorias, reduzir o uso de localização ou continuar sem recomendações pessoais.

Proximidade, popularidade, patrocínio ou comissão não constituem relevância suficiente.

## 15. Relação comercial

A relação comercial deverá permanecer identificada, por exemplo:

- `Sem patrocínio`;
- `Patrocinado`;
- `Comissão aplicável`;
- outra formulação materialmente correta.

A relação comercial não altera a prioridade funcional.

## 16. Estados funcionais mínimos

| Estado | Comportamento esperado |
|---|---|
| localização desativada | permite cidade ou região manual e explica limitações |
| localização aproximada | mostra área e raio sem posição exata |
| localização exata temporária | apresenta finalidade, duração e encerramento |
| região sem resultados | não preenche artificialmente; oferece ampliar raio, período ou filtros |
| carregamento | preserva busca, região, filtros e estrutura |
| baixa conectividade | reduz camadas e informa atualização limitada |
| item indisponível | preserva razão e data da mudança quando possível |
| endereço protegido | mostra área aproximada e condição para revelar detalhes |
| permissão revogada | interrompe uso futuro e mantém alternativas manuais |
| erro de fonte | identifica falha sem apresentar dado como confiável |
| contexto sem gate | remove linguagem personalizada e mantém exploração geral |
| mapa indisponível | oferece Lista com busca, filtros e região conhecida |

A criação de wireframes específicos para esses estados permanece ato separado.

## 17. Relação com a Tela Hoje

A Tela Hoje poderá mostrar somente um recorte compacto `Perto de mim` e oferecer `Abrir no mapa`.

Ela não incorpora o mapa completo e não se transforma em catálogo territorial.

## 18. Relação com Explorar

`Explorar` organiza descoberta por busca, lista, categorias e filtros.

`Mapa` organiza a mesma descoberta pela dimensão territorial.

```text
Explorar em lista
↔ visualizar no Mapa
↔ abrir Detalhe de Oportunidade
```

## 19. Continuidade com o Detalhe

O Mapa conduz ao Detalhe de Oportunidade para condições completas e decisão consciente.

Ao retornar, a pessoa deverá recuperar região, filtros e item selecionado quando tecnicamente viável e compatível com privacidade.

## 20. Resultado da validação

A primeira validação funcional está registrada em UXA-025.

O wireframe é considerado funcionalmente válido após reformulação porque:

- utiliza contexto de atuação explícito;
- distingue filtros ativos;
- mostra resultados da região;
- oferece pesquisa consciente nesta área;
- apresenta legenda;
- torna localização e privacidade encontráveis;
- preserva Mapa e Lista como uma descoberta única;
- oferece contexto suficiente antes do Detalhe;
- condiciona rota à disponibilidade segura do endereço;
- separa relevância de proximidade e patrocínio;
- mantém alternativas sem localização e sem personalização.

## 21. Limites

Este incremento não:

- define fornecedor ou tecnologia de mapas;
- cria geocodificação, rotas ou rastreamento;
- define coordenadas, cidades ou oportunidades reais;
- define ícones, cores ou tipografia finais;
- conclui responsividade para computador ou tablet;
- cria textos finais de interface;
- cria protótipo navegável;
- executa teste de usabilidade;
- inicia Engenharia de Produto.

## 22. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados alternativos do Mapa, começando por Lista ou localização desativada;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
