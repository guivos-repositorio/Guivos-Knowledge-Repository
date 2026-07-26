---
id: UXA-025
title: Validação Funcional e Reformulação do Mapa de Oportunidades
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-010
  - UXA-012
  - UXA-024
related:
  - UXA-002
  - UXA-006
  - UXA-007
  - UXA-011-A1
  - UXA-020
  - UXA-023
normative: true
---

# Validação Funcional e Reformulação do Mapa de Oportunidades

## 1. Finalidade

Este documento registra a primeira validação funcional do **Mapa de Oportunidades**, governa a reformulação do wireframe móvel UXA-024 e estabelece os critérios mínimos para a continuidade entre Mapa, Lista, Explorar, Tela Hoje e Detalhe de Oportunidade.

A decisão permanece restrita à Arquitetura da Experiência. Ela não aprova tecnologia cartográfica, fornecedor de mapas, geocodificação, rotas, design visual, protótipo navegável, teste de usabilidade ou desenvolvimento.

## 2. Decisão humana registrada

Em 26/07/2026, o Fundador autorizou a validação funcional do wireframe móvel do Mapa de Oportunidades após a integração da UXA-024.

A validação examinou:

- posição do Mapa na experiência recorrente;
- hierarquia da superfície;
- contexto de atuação;
- busca, resultados e filtros;
- alternância entre Mapa e Lista;
- leitura das camadas territoriais;
- localização e privacidade;
- oportunidade selecionada;
- relevância e relação comercial;
- continuidade para o Detalhe de Oportunidade;
- estados alternativos e falhas;
- aderência à Fundação da Guivos.

## 3. Resultado da validação

O Mapa de Oportunidades é considerado **funcionalmente válido após reformulação**.

O wireframe inicial já estabelecia corretamente a superfície própria, a alternância entre Mapa e Lista, os filtros, a localização aproximada, as camadas territoriais, o cartão selecionado e a navegação recorrente.

Entretanto, a validação identificou riscos de compreensão e controle que exigiram correção antes do fechamento funcional:

1. o seletor de contexto não utilizava a expressão consolidada `Agindo como`;
2. filtros visíveis não distinguiam com clareza estado ativo e quantidade aplicada;
3. o total de resultados da região não estava visível;
4. a ação `Pesquisar nesta área` estava descrita no contrato, mas ausente do wireframe;
5. os símbolos territoriais não possuíam legenda encontrável;
6. o controle de localização dependia de uma ação secundária pouco evidente;
7. a continuidade entre Mapa e Lista não demonstrava preservação explícita de busca, filtros, região e seleção;
8. a ação `Criar rota` não declarava a condição de disponibilidade do endereço;
9. a linguagem personalizada precisava estar vinculada de forma inequívoca ao gate de personalização atendido;
10. ausência de resultados, localização desativada e endereço protegido precisavam de comportamento governado, mesmo sem novos wireframes neste incremento.

## 4. Posição funcional preservada

A ordem vigente permanece:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não entra entre a Home e a Tela Hoje.

Ele é uma superfície própria da navegação recorrente e poderá ser acessado:

- pela exploração geral da Home;
- por Explorar;
- pelo bloco `Perto de mim` da Tela Hoje;
- pelo Detalhe de Oportunidade;
- por uma Organização, Coletivo, evento, atividade, ponto de apoio ou local salvo.

## 5. Gate de alinhamento à Fundação

### 5.1 Essência

O Mapa reduz a distância entre a pessoa e possibilidades concretas existentes no território, sem transformar proximidade em obrigação ou relevância automática.

### 5.2 Propósito

A superfície amplia o acesso a oportunidades, Organizações, Coletivos, experiências e pontos de apoio que possam contribuir para evolução humana, institucional ou coletiva.

### 5.3 Missão Operacional

A interface deverá ajudar a pessoa a descobrir possibilidades, compreender condições, avaliar relevância e decidir conscientemente se deseja abrir detalhes, salvar, comparar ou criar uma rota.

### 5.4 Visão de Longo Prazo

O contrato deverá funcionar em diferentes países, culturas, densidades urbanas, contextos rurais, condições de conectividade e modelos de localização, sem depender de uma representação territorial única.

### 5.5 Constituição e Princípios Permanentes

A reformulação preserva:

- evolução como finalidade;
- oportunidade como meio;
- decisão final com a pessoa;
- contexto como base da relevância;
- privacidade e controle territorial;
- simplicidade estrutural;
- validade global;
- transparência comercial;
- acessibilidade;
- ação no mundo real sem coerção.

## 6. Hierarquia reformulada

A hierarquia funcional será:

```text
nome da superfície e contexto de atuação
→ pesquisa
→ alternância Mapa e Lista
→ filtros ativos, quantidade e limpeza
→ quantidade de resultados na região
→ ação Pesquisar nesta área
→ área territorial e controles
→ legenda das camadas
→ localização e privacidade
→ oportunidade selecionada
→ detalhe, salvamento e rota contextual
→ navegação recorrente
```

A área territorial continua sendo o maior campo da superfície, mas não poderá ocultar busca, filtros, resultados, privacidade ou a decisão sobre o item selecionado.

## 7. Contexto de atuação

O seletor deverá utilizar a formulação consolidada:

> **Agindo como: Minha jornada**

Quando a pessoa representar uma Organização ou atuar em um Coletivo, o participante, o papel e o escopo deverão permanecer explícitos.

Mudança de contexto deverá ser consciente, visível e reversível. A interface não poderá executar uma ação institucional como pessoal nem uma ação pessoal como institucional.

## 8. Busca, região e resultados

A pesquisa deverá aceitar oportunidade, Organização, Coletivo, atividade, evento, categoria, cidade, bairro ou região quando aplicável.

O Mapa deverá mostrar a quantidade de resultados correspondente à área visível e aos filtros vigentes, por exemplo:

> 8 resultados nesta área

Quando a pessoa mover ou ampliar o mapa, deverá aparecer a ação:

> **Pesquisar nesta área**

A movimentação territorial não deverá alterar silenciosamente os resultados. A pessoa precisa reconhecer quando a área mudou e decidir se deseja atualizar a busca.

## 9. Filtros

Filtros ativos deverão ser distinguíveis sem depender somente de cor.

Cada filtro ativo deverá possuir pelo menos um dos seguintes sinais:

- marca de seleção;
- preenchimento estrutural;
- texto `ativo`;
- valor aplicado;
- possibilidade individual de remoção.

A superfície deverá indicar a quantidade total de filtros aplicados e oferecer `Limpar filtros` sem apagar a busca ou alterar a região silenciosamente.

O conjunto ampliado poderá incluir:

- categoria;
- período, data e horário;
- distância ou região;
- preço ou gratuidade;
- modalidade;
- disponibilidade;
- elegibilidade;
- acessibilidade;
- idioma;
- Organização ou Coletivo;
- origem;
- patrocínio ou relação comercial;
- confiança da fonte;
- vínculo com objetivo ou Próximo Passo.

Filtros de relevância pessoal somente poderão utilizar contexto autorizado e corrigível depois do gate.

## 10. Mapa e Lista como uma descoberta única

Mapa e Lista não constituem catálogos independentes.

A alternância deverá preservar, quando aplicável:

- pesquisa;
- filtros;
- região;
- quantidade de resultados;
- ordenação compatível;
- item selecionado;
- posição aproximada na lista;
- explicação de relevância.

A pessoa deverá poder compreender por que a ordem territorial difere da ordem da lista, especialmente quando a lista utilizar prazo, relevância, acessibilidade ou disponibilidade além da distância.

## 11. Camadas, símbolos e legenda

A superfície poderá apresentar camadas de:

- oportunidades;
- Organizações;
- Coletivos;
- eventos e atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos.

Os símbolos deverão possuir legenda encontrável. Forma, texto e rótulo deverão complementar a diferenciação; cor nunca será o único meio.

Agrupamentos numéricos deverão indicar quantidade e permitir aproximação, expansão ou abertura em lista.

A ação `Camadas` deverá permitir mostrar ou ocultar tipos sem apagar filtros de negócio ou preferências permanentes silenciosamente.

## 12. Localização e privacidade territorial

O estado principal reformulado utiliza localização aproximada e declara:

> Sua posição exata não está visível.

O controle de localização deverá permanecer encontrável e permitir:

- localização desativada;
- cidade ou região informada manualmente;
- localização aproximada;
- localização exata temporária;
- alteração do raio;
- encerramento do uso exato;
- retirada de permissão.

Localização exata temporária exige finalidade, duração e ação de encerramento.

O Mapa não deverá:

- mostrar localização de participantes;
- revelar residência ou local sensível;
- expor endereço protegido antes da condição aplicável;
- exigir rastreamento contínuo;
- manter localização exata sem finalidade e prazo;
- utilizar histórico sensível para publicidade;
- presumir interesse somente pela proximidade.

## 13. Oportunidade selecionada

O cartão resumido deverá manter:

- tipo e modalidade;
- título;
- responsável ou fonte;
- distância ou região;
- data, prazo ou disponibilidade;
- preço, gratuidade ou faixa;
- vagas quando material;
- acessibilidade;
- razão resumida de relevância;
- relação comercial;
- ações contextuais.

A hierarquia do cartão será:

```text
tipo, modalidade e distância
→ título e preço ou gratuidade
→ responsável, data e disponibilidade
→ acessibilidade e razão de relevância
→ relação comercial
→ Ver detalhes
→ Salvar
→ Criar rota, quando aplicável
```

O cartão não substitui o Detalhe de Oportunidade.

## 14. Rota e endereço protegido

`Criar rota` somente deverá aparecer quando:

- houver local físico aplicável;
- o endereço puder ser utilizado naquele estado;
- a pessoa tiver autorização ou condição necessária;
- a origem da localização estiver disponível;
- a ação não revelar residência ou local sensível.

Quando o endereço estiver protegido, a superfície deverá substituir a ação por uma formulação como:

- `Ver área aproximada`;
- `Entender quando o endereço será liberado`;
- `Revisar condições de acesso`.

O Mapa não deverá utilizar a ação de rota para contornar proteção territorial.

## 15. Relevância e relação comercial

Antes do gate, o Mapa poderá apresentar somente conteúdo geral, institucional, editorial ou resultante de busca explícita.

Depois do gate, poderá explicar relevância com base em objetivo, Próximo Passo, preferência, localização autorizada, disponibilidade e elegibilidade conhecida.

A pessoa deverá poder:

- abrir `Por que aparece aqui?`;
- ver informações utilizadas;
- corrigir contexto;
- ocultar categoria;
- reduzir o uso de localização;
- continuar sem recomendações pessoais.

Proximidade, popularidade, patrocínio ou comissão não constituem relevância suficiente.

Relação comercial deverá ser identificada como `Sem patrocínio`, `Patrocinado`, `Comissão aplicável` ou outra formulação materialmente correta, sem alterar a prioridade funcional.

## 16. Estados funcionais validados

| Estado | Decisão funcional |
|---|---|
| localização desativada | permitir cidade ou região manual, sem bloquear exploração |
| localização aproximada | mostrar área e raio sem posição exata |
| localização exata temporária | explicar finalidade, duração e encerramento |
| região sem resultados | não preencher artificialmente; oferecer ampliar raio, período ou filtros |
| carregamento | preservar estrutura, busca, região e filtros |
| baixa conectividade | reduzir camadas e declarar atualização limitada |
| item indisponível | informar mudança e data quando possível |
| endereço protegido | mostrar área aproximada e condição para revelar detalhes |
| permissão revogada | interromper uso futuro e preservar alternativas manuais |
| erro de fonte | identificar falha e evitar apresentação como dado confiável |
| contexto sem gate | retirar linguagem personalizada e manter exploração geral |
| mapa indisponível | oferecer Lista com a mesma busca, filtros e região conhecida |

Esses estados são funcionalmente governados. A criação de wireframes específicos permanece ato separado.

## 17. Relação com outras superfícies

### 17.1 Tela Hoje

A Tela Hoje poderá mostrar somente um recorte compacto `Perto de mim` e conduzir ao Mapa. Ela não incorporará o mapa completo.

### 17.2 Explorar

Explorar e Mapa compartilham busca, filtros, resultados e contexto de descoberta. Explorar prioriza lista e categorias; Mapa prioriza território.

### 17.3 Detalhe de Oportunidade

O Mapa conduz ao Detalhe para condições completas, elegibilidade, riscos, política de cancelamento, composição de preço, autoridade e decisão consciente.

Ao retornar do Detalhe, a pessoa deverá recuperar região, filtros e item selecionado quando tecnicamente viável e compatível com privacidade.

## 18. Reformulação aplicada ao wireframe

A versão reformulada da UXA-024 deverá demonstrar:

- `Agindo como: Minha jornada`;
- filtros ativos com marca textual;
- quantidade de filtros e ação de limpeza;
- quantidade de resultados na área;
- ação `Pesquisar nesta área`;
- legenda das camadas;
- localização aproximada e privacidade mais encontráveis;
- cartão selecionado com relação comercial;
- rota apresentada como ação contextual;
- Mapa selecionado na navegação recorrente.

## 19. Resultado final

Após a reformulação, o Mapa atende ao contrato funcional porque:

- é reconhecível como superfície recorrente própria;
- mantém Mapa e Lista como uma descoberta única;
- torna busca, filtros, região e resultados compreensíveis;
- preserva controle territorial;
- oferece contexto suficiente antes do Detalhe;
- distingue preço, origem, acessibilidade, relevância e relação comercial;
- não transforma proximidade ou patrocínio em prioridade;
- preserva ausência legítima de resultados;
- mantém alternativas sem localização;
- impede rota quando houver endereço protegido;
- não inicia design ou implementação.

## 20. Limites

Esta validação não:

- aprova textos finais de interface;
- define fornecedor ou tecnologia cartográfica;
- cria coordenadas, geocodificação ou rotas;
- conclui acessibilidade técnica;
- cria versão para computador;
- cria protótipo navegável;
- executa teste de usabilidade;
- inicia Engenharia de Produto.

## 21. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados alternativos do Mapa, começando por Lista ou localização desativada;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido da jornada;
4. criar a referência móvel da Página Inicial pública;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
