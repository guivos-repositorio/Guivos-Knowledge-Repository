---
id: UXA-027
title: Validação Funcional Especializada e Reformulação do Estado do Mapa sem Localização
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

# Validação Funcional Especializada e Reformulação do Estado do Mapa sem Localização

## 1. Finalidade

Este documento registra a validação funcional especializada do estado do Mapa de Oportunidades com a localização do dispositivo desativada e governa a reformulação da UXA-026.

A decisão permanece restrita à Arquitetura da Experiência. Ela não aprova fornecedor de mapas, localização técnica, geocodificação, rotas, design visual, protótipo navegável, teste de usabilidade ou desenvolvimento.

## 2. Decisão humana registrada

Em 27/07/2026, o Fundador autorizou a validação funcional especializada da UXA-026 após a integração do marco M7.27.

A validação examinou:

- compreensão de que o Mapa funciona sem localização;
- clareza da escolha manual de cidade ou região;
- distinção entre região manual e posição pessoal;
- confirmação de que a posição não foi acessada;
- preservação de busca, filtros e alternância Mapa ou Lista;
- ausência de marcador e distância pessoal presumida;
- linguagem geral sem personalização indevida;
- ativação opcional de localização aproximada;
- salvamento sem localização;
- definição manual de origem para rota;
- continuidade para Detalhe de Oportunidade;
- aderência à Fundação da Guivos.

## 3. Resultado da validação

O estado do Mapa com localização desativada é considerado **funcionalmente válido após reformulação**.

O wireframe inicial já estabelecia corretamente:

- exploração geral sem personalização;
- aviso de localização desativada;
- região escolhida manualmente;
- pesquisa e filtros preservados;
- Mapa e Lista sincronizados;
- área territorial sem marcador pessoal;
- resultados explicados por região e busca explícita;
- ativação opcional de localização aproximada.

Entretanto, quatro riscos exigiram correção antes do fechamento funcional:

1. a ausência de marcador não confirmava de forma inequívoca que a posição não havia sido acessada;
2. a região manual poderia ser interpretada como posição atual da pessoa;
3. o salvamento estava previsto no contrato, mas não demonstrado no artefato;
4. a origem manual para rota estava prevista, mas não aparecia no cartão selecionado.

## 4. Posição funcional preservada

A ordem vigente permanece:

```text
Página Inicial pública
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O estado sem localização não constitui uma nova etapa da jornada. Ele é uma condição operacional da superfície recorrente do Mapa.

## 5. Gate de alinhamento à Fundação

### 5.1 Essência

A superfície reduz barreiras de acesso sem transformar compartilhamento territorial em requisito de participação.

### 5.2 Propósito

A pessoa continua descobrindo possibilidades concretas no território por decisão própria, mesmo quando não deseja ou não consegue compartilhar localização.

### 5.3 Missão Operacional

A interface deverá permitir escolher região, compreender resultados, salvar itens, abrir detalhes e definir origem para rota sem coleta territorial invisível.

### 5.4 Visão de Longo Prazo

O contrato deverá funcionar em países, regiões e dispositivos com diferentes níveis de disponibilidade, precisão, conectividade e confiança em serviços de localização.

### 5.5 Constituição e Princípios Permanentes

A reformulação preserva:

- decisão final com a pessoa;
- localização como dado opcional e controlável;
- exploração sem personalização;
- transparência sobre o que foi e não foi acessado;
- alternativas manuais reais;
- proteção de residências e locais sensíveis;
- simplicidade estrutural;
- validade global;
- publicidade separada de relevância.

## 6. Hierarquia reformulada

A hierarquia funcional será:

```text
Mapa e contexto de exploração
→ localização desativada
→ confirmação de posição não acessada
→ região manual distinta da posição pessoal
→ pesquisa
→ Mapa ou Lista
→ filtros e resultados
→ área territorial sem marcador pessoal
→ oportunidade selecionada
→ explicação, salvar, definir origem e ver detalhes
→ navegação recorrente
```

O aviso de privacidade deverá anteceder resultados e ações territoriais.

## 7. Confirmação de posição não acessada

O estado deverá declarar:

> **Posição não acessada**

A declaração significa que, naquele estado:

- não foi obtida coordenada do dispositivo;
- não foi exibida posição aproximada;
- não foi inferida residência;
- não foi criado marcador pessoal;
- a região visível decorre de escolha manual.

A interface não deverá utilizar a declaração quando houver coleta territorial material ainda ativa.

## 8. Região manual

A região escolhida deverá ser acompanhada de formulação equivalente a:

> **Região informada manualmente · não é sua posição**

A pessoa deverá poder alterar a região sem perder silenciosamente busca, filtros compatíveis, modo Mapa ou Lista, item salvo ou preferências não territoriais.

Filtros dependentes de distância pessoal não poderão permanecer ativos como se houvesse origem válida.

## 9. Busca, filtros, Mapa e Lista

A localização desativada não altera o contrato de descoberta única.

Mapa e Lista deverão preservar, quando aplicável:

- região manual;
- busca;
- filtros;
- quantidade de resultados;
- item selecionado;
- explicação da origem dos resultados.

A movimentação do mapa deverá exigir ação consciente para consultar a nova área. Ela não deverá redefinir silenciosamente a região manual permanente.

## 10. Linguagem geral e gate de personalização

Sem gate de personalização atendido, a superfície deverá utilizar:

> **Exploração geral · sem personalização**

Resultados poderão ser explicados por:

- região manual;
- busca explícita;
- filtros;
- categoria;
- período;
- fonte editorial ou institucional;
- relação comercial identificada.

A superfície não poderá afirmar adequação ao Momento Atual, proximidade pessoal ou recomendação individual.

## 11. Área territorial sem marcador pessoal

O mapa não deverá mostrar:

- ponto de localização da pessoa;
- círculo de precisão;
- posição aproximada presumida;
- residência inferida;
- histórico de deslocamento;
- indicação de presença atual na região selecionada.

A representação territorial poderá mostrar apenas itens e áreas autorizados.

## 12. Oportunidade selecionada

O cartão deverá oferecer contexto suficiente antes do detalhe e demonstrar:

- tipo e modalidade;
- título;
- responsável ou fonte;
- cidade, bairro ou região;
- data ou prazo;
- preço ou gratuidade;
- disponibilidade;
- acessibilidade;
- explicação da origem;
- relação comercial;
- salvamento;
- definição de origem;
- acesso ao detalhe.

A distância pessoal deverá ser omitida sem origem válida.

## 13. Salvamento sem localização

Salvar um item deverá continuar disponível sem localização.

O salvamento não autoriza:

- ativação de localização;
- inferência de residência;
- criação de histórico territorial;
- personalização não autorizada;
- rastreamento futuro.

A origem, região e condições conhecidas do item deverão permanecer rastreáveis.

## 14. Origem manual e rota

Sem origem válida, a rota não poderá iniciar automaticamente.

A ação reformulada será:

> **Definir origem**

A pessoa poderá informar endereço, selecionar ponto conhecido, utilizar endereço salvo com autorização compatível ou ativar localização aproximada conscientemente.

A escolha de origem deverá ser separada da autorização para retenção, histórico ou rastreamento contínuo.

Endereço protegido continuará oferecendo somente área aproximada ou condição de liberação aplicável.

## 15. Ativação opcional de localização

A ação deverá indicar explicitamente sua natureza opcional.

A ativação não poderá ser apresentada como necessária para:

- pesquisar;
- utilizar Mapa ou Lista;
- abrir detalhes;
- salvar oportunidades;
- escolher região;
- compreender resultados.

Antes da ativação, a pessoa deverá poder revisar finalidade, precisão, duração, encerramento e retirada da permissão.

## 16. Estados e transições validados

| Estado ou transição | Decisão funcional |
|---|---|
| nunca concedeu localização | manter exploração manual integral |
| permissão recusada | não bloquear funções essenciais |
| permissão retirada | interromper uso futuro e manter região manual |
| dispositivo sem localização | oferecer região manual e Lista |
| alteração de região | preservar busca e filtros compatíveis |
| alternância Mapa ou Lista | preservar região e item selecionado |
| salvar item | não ativar localização nem personalização |
| definir origem | solicitar origem específica sem rastreamento contínuo |
| ativar localização aproximada | explicar finalidade e manter ação opcional |
| endereço protegido | impedir rota e mostrar somente área permitida |
| mapa indisponível | oferecer Lista com o mesmo contexto |

## 17. Reformulação aplicada ao wireframe

A UXA-026 reformulada demonstra:

- `Exploração geral · sem personalização`;
- `Localização desativada`;
- `Posição não acessada`;
- região informada manualmente e distinta da posição pessoal;
- pesquisa e filtros preservados;
- Mapa e Lista sincronizados;
- mapa sem posição ou marcador pessoal;
- resultado explicado pela região;
- relação comercial;
- `Salvar`;
- `Definir origem`;
- `Ver detalhes`;
- ativação opcional de localização aproximada.

## 18. Resultado final

Após a reformulação, o estado atende ao contrato funcional porque:

- permanece utilizável sem localização;
- torna explícito o que não foi acessado;
- evita confundir região manual com posição pessoal;
- mantém descoberta e continuidade;
- não utiliza linguagem personalizada sem gate;
- oferece salvamento independente de localização;
- trata rota como ação dependente de origem específica;
- mantém ativação territorial opcional;
- protege endereços sensíveis;
- não inicia design ou implementação.

## 19. Limites

Esta validação não:

- aprova textos finais de interface;
- define tecnologia ou fornecedor de mapas;
- cria coordenadas, geocodificação ou rotas;
- conclui acessibilidade técnica;
- cria versão para computador;
- cria protótipo navegável;
- executa teste de usabilidade;
- inicia Engenharia de Produto.

## 20. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o estado alternativo em Lista;
2. criar o estado sem resultados;
3. criar referência do Mapa para computador;
4. criar o wireframe gráfico do início protegido da jornada;
5. criar a referência móvel da Página Inicial pública;
6. validar a revisão da compreensão inicial;
7. validar a transição para a primeira Tela Hoje;
8. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
