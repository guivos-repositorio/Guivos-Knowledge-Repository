---
id: UXA-031
title: Validação Funcional Especializada e Reformulação do Estado do Mapa sem Resultados
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-011-A1
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
related:
  - UXA-002
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-020
  - UXA-023
normative: true
---

# Validação Funcional Especializada e Reformulação do Estado do Mapa sem Resultados

## 1. Finalidade

Este documento registra a validação funcional especializada do estado sem resultados do Mapa de Oportunidades e governa a reformulação da UXA-030.

A decisão permanece restrita à Arquitetura da Experiência. Ela não aprova algoritmo de busca, cobertura de fontes de produção, tecnologia cartográfica, geocodificação, rotas, design visual, protótipo navegável, conformidade técnica de acessibilidade, teste de usabilidade ou desenvolvimento.

## 2. Decisão humana registrada

Em 27/07/2026, o Fundador autorizou a validação funcional especializada da UXA-030 após a integração do marco M7.31.

A validação examinou:

- compreensão de que o total zero se refere somente à consulta atual;
- distinção entre ausência legítima, falha de fonte e indisponibilidade temporária;
- preservação de região, busca, filtros e contexto `Agindo como`;
- clareza e independência das ações de recuperação;
- ausência de alterações silenciosas na consulta;
- equivalência do estado entre Mapa e Lista;
- tratamento de uma oportunidade anteriormente selecionada;
- manutenção da localização como opcional;
- funcionamento textual sem o mapa carregado;
- ausência de personalização ou preenchimento comercial artificial;
- aderência à Fundação da Guivos.

## 3. Resultado da validação

O estado sem resultados do Mapa é considerado **funcionalmente válido após reformulação**.

O wireframe inicial já estabelecia corretamente:

- estado interno da superfície recorrente `Mapa`;
- alternância `Mapa ↔ Lista`;
- localização desativada e posição não acessada;
- região manual distinta da posição pessoal;
- busca e filtros preservados;
- total zero limitado à consulta atual;
- ações separadas para ajustar região, período, filtros e busca;
- distinção conceitual entre ausência, falha e indisponibilidade;
- exploração geral como saída separada;
- tratamento textual sem depender somente do campo cartográfico.

Entretanto, seis riscos exigiram correção antes do fechamento funcional:

1. a cobertura consultada não aparecia de forma verificável no wireframe;
2. `nenhuma falha conhecida` constituía afirmação forte sem evidência acessível na superfície;
3. as ações de recuperação não demonstravam revisão antes da aplicação;
4. `Desfazer alteração` aparecia sem indicar a existência e a natureza da alteração anterior;
5. o tratamento da oportunidade anteriormente selecionada existia no contrato, mas não era materializado no artefato;
6. `Ver estados` utilizava linguagem técnica e `Explorar opções gerais` não declarava a preservação da consulta atual.

## 4. Posição funcional preservada

A ordem vigente permanece:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O estado sem resultados não constitui uma nova tela obrigatória da jornada. Ele é uma condição transitória e recuperável da superfície recorrente do Mapa.

O item `Mapa` permanece selecionado na navegação principal.

## 5. Gate de alinhamento à Fundação

### 5.1 Essência

A reformulação preserva a possibilidade de reconhecer limites reais sem transformar ausência momentânea de correspondências em ausência de possibilidades para a pessoa.

### 5.2 Propósito

O estado ajuda a pessoa a compreender o que foi consultado, o que não foi encontrado e quais mudanças conscientes podem ampliar a descoberta.

### 5.3 Missão Operacional

Região, busca, filtros, cobertura, atualização, limitações e ações de recuperação permanecem verificáveis e controláveis.

### 5.4 Visão de Longo Prazo

O contrato permite operar em diferentes territórios, densidades, fontes de dados, condições de conectividade e canais sem produzir falsas conclusões globais.

### 5.5 Constituição e Princípios Permanentes

São preservados:

- autonomia;
- dignidade;
- transparência;
- explicabilidade;
- privacidade;
- não manipulação;
- acessibilidade;
- reversibilidade;
- separação entre ausência funcional e interesse comercial.

Nenhuma falha material à Fundação foi identificada após a reformulação.

## 6. Natureza do zero validado

O zero validado significa exclusivamente:

> **Nenhuma correspondência foi encontrada para esta consulta, nesta região, com estes filtros, neste momento e dentro da cobertura declarada.**

Ele não significa:

- inexistência de oportunidades no território;
- inexistência de possibilidades futuras;
- inadequação da pessoa;
- falta de capacidade, mérito ou elegibilidade;
- ausência em fontes não consultadas;
- impossibilidade de encontrar alternativas por outros caminhos.

A interface não poderá converter uma observação limitada em uma conclusão absoluta.

## 7. Cobertura verificável

A versão inicial declarava:

> **Consulta concluída · nenhuma falha conhecida**

A formulação era insuficiente porque a pessoa não conseguia verificar quais fontes, categorias ou limites sustentavam a conclusão.

A reformulação passa a declarar:

> **Consulta concluída · cobertura verificada · atualizada agora**

E oferece:

> **Ver cobertura**

A explicação de cobertura deverá informar, quando material:

- fontes previstas para a consulta;
- fontes que responderam;
- fontes não aplicáveis;
- fontes indisponíveis;
- categorias ou tipos consultados;
- período considerado;
- região consultada;
- horário da atualização;
- limitações conhecidas.

`Cobertura verificada` somente poderá ser utilizada quando a condição puder ser sustentada. Caso contrário, a interface deverá utilizar estado de cobertura parcial, falha de fonte, carregamento ou indisponibilidade.

## 8. Mensagem principal

A mensagem validada permanece:

> **Nenhum resultado corresponde à busca, região e filtros atuais.**

Ela deverá ser acompanhada por:

> **Sua consulta permanece intacta.**

A interface não deverá afirmar:

- `Não existem oportunidades`;
- `Não há nada nesta cidade`;
- `Você não tem opções`;
- `Nada é adequado para você`;
- `Não encontramos o que você precisa`.

## 9. Contexto preservado

O estado deverá manter visíveis:

- contexto `Agindo como`;
- presença ou ausência de personalização;
- região ativa;
- origem manual ou autorizada da região;
- busca executada;
- filtros ativos;
- total consolidado de filtros;
- modo Mapa ou Lista;
- total zero;
- momento da atualização;
- cobertura declarada.

O total zero não autoriza apagar, reescrever ou substituir nenhuma dessas dimensões.

## 10. Recuperação com revisão prévia

As ações continuam independentes:

- `Ampliar região`;
- `Alterar período`;
- `Revisar filtros`;
- `Editar busca`;
- `Explorar sem alterar esta consulta`.

A reformulação acrescenta a declaração:

> **Você revisará cada mudança antes de aplicar.**

Cada ação deverá abrir uma etapa de revisão que informe:

- dimensão que será alterada;
- valor atual;
- valor proposto;
- dimensões preservadas;
- possível efeito esperado;
- ação `Aplicar`;
- ação `Cancelar`.

A interface não poderá aplicar automaticamente uma ampliação territorial, remoção de filtro, alteração de período, substituição de busca ou troca de modalidade.

## 11. Desfazer somente quando aplicável

`Desfazer` não constitui ação permanente do estado zero.

Ela somente deverá aparecer quando existir uma alteração anterior identificável e reversível.

A reformulação demonstra:

> **Última alteração: filtro “Hoje” aplicado**

> **Desfazer**

O aviso deverá informar o que será restaurado antes da reversão.

Quando não houver alteração anterior compatível, a ação não deverá aparecer como disponível.

## 12. Oportunidade anteriormente selecionada

Se uma mudança na consulta produzir total zero enquanto existir uma oportunidade anteriormente selecionada, a interface deverá declarar:

> **Seleção anterior fora da consulta atual**

A pessoa poderá:

- abrir o Detalhe, se a oportunidade ainda estiver disponível;
- remover conscientemente a seleção;
- desfazer a mudança que produziu a incompatibilidade;
- manter a nova consulta sem resultados.

A seleção anterior não deverá:

- ser apagada silenciosamente;
- ser reinserida como correspondência atual;
- alterar o total zero;
- receber prioridade artificial;
- contornar indisponibilidade ou condição de acesso.

## 13. Mapa e Lista como o mesmo estado

Mapa e Lista continuam representando a mesma consulta e a mesma atualização.

Ao alternar os modos, deverão permanecer:

- contexto `Agindo como`;
- região;
- busca;
- filtros;
- total zero;
- cobertura;
- horário de atualização;
- diagnóstico;
- ações de recuperação;
- última alteração reversível, quando existente;
- seleção anterior, quando existente;
- estado de localização.

A Lista deverá funcionar integralmente sem renderização cartográfica.

O Mapa deverá anunciar o estado de forma textual e não depender do campo vazio ou da ausência de marcadores.

## 14. Localização e privacidade

O exemplo continua declarando:

> **Localização desativada · posição não acessada**

> **Região manual · não é sua posição**

O estado zero não poderá ser utilizado para pressionar a ativação de localização.

A pessoa poderá revisar ou ampliar a região manual sem:

- conceder acesso à posição;
- autorizar rastreamento;
- criar histórico territorial;
- inferir residência;
- transformar região em posição pessoal.

## 15. Personalização e preenchimento comercial

Sem gate de personalização, a explicação utilizará somente:

- região escolhida;
- busca explícita;
- filtros aplicados;
- período;
- cobertura declarada.

Mesmo após o gate, a ausência deverá ser explicada pela consulta e não pela suposta adequação da pessoa.

O estado não poderá ser preenchido artificialmente por:

- publicidade;
- conteúdo patrocinado;
- comissão;
- popularidade;
- sugestões sem correspondência;
- inferência pessoal não autorizada.

`Explorar sem alterar esta consulta` poderá abrir descoberta geral em uma superfície separada, preservando a consulta territorial para retorno.

## 16. Distinção validada entre condições

| Condição | Mensagem funcional | Regra |
|---|---|---|
| zero legítimo | `0 resultados correspondem a esta consulta` | cobertura verificada e contexto preservado |
| cobertura parcial | `Resultados limitados às fontes disponíveis` | declarar limites e não concluir ausência total |
| falha de fonte | `Não foi possível verificar todas as fontes` | não apresentar zero como conclusão |
| indisponibilidade temporária | `Resultados temporariamente indisponíveis` | preservar consulta e permitir nova tentativa |
| carregamento | `Atualizando resultados` | manter estrutura e não concluir zero |
| baixa conectividade | `Atualização limitada pela conexão` | declarar possível desatualização |

A ação anterior `Ver estados` é substituída por:

> **Entender disponibilidade dos dados**

A linguagem deverá explicar a condição atual sem exigir conhecimento técnico sobre estados internos do sistema.

## 17. Acessibilidade e resiliência

O estado deverá:

- anunciar textualmente o total zero;
- anunciar a cobertura e a atualização;
- não depender de cor, mapa vazio ou ausência de marcadores;
- possuir títulos e ações compreensíveis isoladamente;
- oferecer ordem de foco coerente;
- preservar contexto durante falha cartográfica;
- funcionar integralmente em Lista;
- não criar ciclos automáticos de nova tentativa;
- manter ações essenciais em baixa conectividade quando possível.

Esta validação arquitetural não conclui conformidade técnica de acessibilidade.

## 18. Reformulação aplicada ao wireframe

A versão reformulada da UXA-030 demonstra:

- `Agindo como: Pessoa`;
- exploração geral sem personalização;
- localização desativada e posição não acessada;
- região manual distinta da posição pessoal;
- busca e quatro filtros preservados;
- alternância `Mapa ↔ Lista`;
- `0 resultados correspondem a esta consulta`;
- `Consulta concluída · cobertura verificada · atualizada agora`;
- ação `Ver cobertura`;
- mensagem limitada à consulta atual;
- declaração `Sua consulta permanece intacta`;
- ajustes independentes de região, período, filtros e busca;
- aviso de revisão antes de aplicar;
- última alteração identificada e `Desfazer` condicional;
- seleção anterior fora da consulta atual;
- acesso ao Detalhe e remoção consciente da seleção;
- `Explorar sem alterar esta consulta`;
- `Entender disponibilidade dos dados`;
- equivalência entre Mapa e Lista.

## 19. Resultado final

Após a reformulação, o estado atende ao contrato funcional porque:

- limita o zero à consulta executada;
- demonstra cobertura verificável;
- não confunde ausência com falha;
- preserva região, busca, filtros e contexto;
- exige revisão antes de alterar a consulta;
- torna reversão condicional e explicável;
- preserva seleção anterior sem falsear correspondência;
- mantém Mapa e Lista equivalentes;
- preserva localização opcional;
- evita personalização e preenchimento comercial artificial;
- funciona textualmente sem mapa carregado;
- não inicia design ou implementação.

## 20. Limites

Esta validação não:

- aprova textos finais de interface;
- valida o estado com usuários reais;
- define algoritmo de busca;
- define cobertura de fontes de produção;
- cria dados reais;
- conclui acessibilidade técnica;
- define tecnologia cartográfica;
- cria geocodificação ou rotas;
- cria referência para computador;
- cria protótipo navegável;
- inicia design visual;
- inicia Engenharia de Produto.

## 21. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar referência do Mapa para computador;
2. criar o wireframe gráfico do início protegido;
3. criar a referência móvel da Home;
4. validar a revisão da compreensão inicial;
5. validar a transição para a primeira Tela Hoje;
6. criar outros estados alternativos do Mapa;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
