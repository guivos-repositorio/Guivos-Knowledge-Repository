---
id: UXA-030
title: Wireframe Alternativo do Mapa de Oportunidades — Estado sem Resultados
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-024
depends_on:
  - UXA-004
  - UXA-005
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
related:
  - UXA-002
  - UXA-007
  - UXA-010
  - UXA-011-A1
  - UXA-012
  - UXA-020
  - UXA-023
  - UXA-031
normative: false
---

# Wireframe Alternativo do Mapa de Oportunidades — Estado sem Resultados

## 1. Finalidade

Este documento materializa o estado em que uma consulta territorial válida é concluída sem encontrar oportunidades correspondentes à região, busca e filtros vigentes.

A versão 0.2.0 incorpora a reformulação governada pela **UXA-031 — Validação Funcional Especializada e Reformulação do Estado do Mapa sem Resultados**.

O estado não deverá ser utilizado como mensagem genérica para falha de fonte, indisponibilidade temporária, carregamento incompleto ou baixa conectividade. Ausência legítima de correspondências e incapacidade de consultar dados são condições diferentes.

O artefato preserva a consulta da pessoa, explica o que ocorreu e oferece caminhos explícitos de recuperação sem preencher artificialmente o Mapa, apagar filtros ou ativar personalização.

Este documento não representa design visual, tecnologia cartográfica, dados reais, implementação ou teste com usuários.

## 2. Posição na experiência

O estado permanece dentro da superfície recorrente do Mapa:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

O item `Mapa` continua selecionado. A alternância interna permanece disponível:

```text
Mapa ↔ Lista
```

Mapa e Lista deverão apresentar o mesmo estado sem resultados para a mesma consulta e atualização.

## 3. Condição de entrada no estado

A mensagem de ausência legítima somente poderá aparecer quando:

- a consulta tiver sido executada;
- a região estiver definida;
- busca e filtros vigentes forem conhecidos;
- as fontes previstas tiverem respondido ou sua cobertura aplicável estiver declarada;
- não houver falha ativa capaz de explicar o resultado vazio;
- não houver carregamento pendente material;
- o total correspondente for realmente zero naquele momento de atualização.

A interface reformulada deverá indicar:

> **0 resultados correspondem a esta consulta**

> **Consulta concluída · cobertura verificada · atualizada agora**

E oferecer:

> **Ver cobertura**

A declaração não significa que não existam oportunidades em toda a cidade, no futuro, em outras categorias ou fora das fontes consultadas.

## 4. Artefato visual

![Wireframe alternativo do Mapa de Oportunidades sem resultados](../assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg)

Arquivo vetorial:

`docs/assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg`

Dimensão de referência:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- modo: Mapa selecionado;
- condição ilustrada: localização desativada, posição não acessada, região manual e consulta concluída com zero correspondências.

## 5. Hierarquia funcional

```text
nome da superfície e contexto de atuação
→ estado territorial e privacidade
→ região ativa e editável
→ pesquisa preservada
→ alternância Mapa ou Lista
→ filtros ativos e total consolidado
→ quantidade zero, cobertura e atualização
→ explicação da ausência de correspondências
→ ações explícitas de recuperação
→ revisão antes de aplicar mudanças
→ última alteração reversível, quando existente
→ seleção anterior, quando existente
→ disponibilidade dos dados
→ navegação recorrente
```

A ausência de marcadores no campo territorial não poderá ser o único sinal do estado.

## 6. Contexto preservado

O estado deverá manter visíveis:

- `Agindo como`;
- modalidade geral ou personalizada aplicável;
- região ou área territorial ativa;
- origem da região, como manual ou localização autorizada;
- texto pesquisado;
- filtros ativos;
- total consolidado de filtros;
- modo `Mapa` ou `Lista`;
- momento da última atualização;
- cobertura ou limitação conhecida da consulta.

Nenhum desses elementos poderá ser apagado somente porque o total chegou a zero.

## 7. Mensagem principal

A mensagem deverá informar de forma direta:

> **Nenhum resultado corresponde à busca, região e filtros atuais.**

> **Sua consulta permanece intacta.**

Ela deverá evitar formulações absolutas como:

- `Não existem oportunidades`;
- `Não há nada nesta cidade`;
- `Você não tem opções`;
- `Nada é adequado para você`;
- `Não encontramos o que você precisa`.

O sistema conhece apenas o resultado da consulta executada, não a totalidade de possibilidades existentes nem as necessidades da pessoa.

## 8. Cobertura e atualização

A pessoa deverá poder abrir `Ver cobertura` para verificar, quando material:

- fontes previstas;
- fontes que responderam;
- fontes não aplicáveis;
- fontes indisponíveis;
- categorias consultadas;
- região e período;
- horário da atualização;
- limitações conhecidas.

`Cobertura verificada` somente poderá aparecer quando houver evidência correspondente. Cobertura parcial, falha de fonte, carregamento e indisponibilidade deverão utilizar mensagens próprias.

## 9. Ações de recuperação

A interface deverá oferecer ações conscientes e independentes:

- `Ampliar região`;
- `Alterar período`;
- `Revisar filtros`;
- `Editar busca`;
- `Explorar sem alterar esta consulta`.

A superfície reformulada declara:

> **Você revisará cada mudança antes de aplicar.**

Cada ação deverá apresentar antes da confirmação:

- dimensão alterada;
- valor atual;
- valor proposto;
- dimensões preservadas;
- ação `Aplicar`;
- ação `Cancelar`.

A superfície não poderá:

- remover filtros automaticamente;
- ampliar a região sem confirmação;
- substituir a busca por termos semelhantes sem aviso;
- mudar período, modalidade ou preço silenciosamente;
- ativar localização;
- inserir resultados patrocinados para evitar a tela vazia;
- iniciar personalização para preencher o estado.

## 10. Preservação e reversibilidade

Quando uma ação de recuperação alterar a consulta, a pessoa deverá poder reconhecer:

- qual dimensão mudou;
- quais dimensões permaneceram;
- o novo total de resultados;
- se a atualização foi concluída;
- como desfazer a última mudança quando tecnicamente possível.

`Desfazer` somente deverá aparecer quando existir alteração anterior identificável e reversível.

O wireframe reformulado demonstra:

> **Última alteração: filtro “Hoje” aplicado**

> **Desfazer**

`Limpar filtros` deverá ser uma decisão explícita e não deverá apagar região ou busca.

`Ampliar região` não deverá transformar região manual em posição pessoal nem autorizar rastreamento.

## 11. Mapa e Lista

O estado deverá ser equivalente nos dois modos.

Ao alternar entre Mapa e Lista, deverão permanecer:

- região;
- busca;
- filtros;
- total zero;
- cobertura;
- momento da atualização;
- diagnóstico da consulta;
- ações de recuperação;
- contexto `Agindo como`;
- estado de localização;
- última alteração reversível, quando existente;
- seleção anterior, quando existente.

A Lista deverá funcionar integralmente sem mapa carregado.

O Mapa deverá apresentar informação textual suficiente para leitores de tela e pessoas que não interpretem o campo cartográfico.

## 12. Estado territorial

Quando a localização estiver desativada, deverão permanecer as declarações:

> **Localização desativada · posição não acessada**

> **Região informada manualmente · não é sua posição**

A ausência de resultados não constitui justificativa para solicitar localização de forma bloqueante, insistente ou coerciva.

A pessoa poderá ampliar ou trocar a região manualmente sem compartilhar a posição do dispositivo.

## 13. Personalização e linguagem

Sem o gate de personalização atendido, o estado deverá utilizar linguagem geral baseada somente em:

- região escolhida;
- busca explícita;
- filtros aplicados;
- período;
- fontes e cobertura declaradas.

Não deverá afirmar que uma oportunidade seria melhor, ideal ou adequada ao Momento Atual da pessoa.

Mesmo após o gate, a ausência de resultados deverá ser explicada pela consulta, sem transformar inferências pessoais em certeza.

`Explorar sem alterar esta consulta` poderá abrir descoberta geral separada, preservando a consulta territorial para retorno.

## 14. Distinção entre estados

| Condição | Mensagem funcional | Comportamento |
|---|---|---|
| consulta concluída com zero correspondências | `0 resultados correspondem a esta consulta` | preservar contexto, declarar cobertura e oferecer ajustes explícitos |
| falha de uma ou mais fontes materiais | `Não foi possível verificar todas as fontes` | não apresentar zero como conclusão; identificar limitação e permitir nova tentativa |
| indisponibilidade temporária | `Resultados temporariamente indisponíveis` | preservar consulta e permitir tentar novamente ou usar Lista quando aplicável |
| carregamento em andamento | `Atualizando resultados` | manter estrutura, região, busca e filtros |
| baixa conectividade | `Atualização limitada pela conexão` | declarar possível desatualização e evitar conclusão absoluta |
| cobertura parcial conhecida | `Resultados limitados às fontes disponíveis` | informar escopo e não representar cobertura total |

Falha de fonte não é ausência de oportunidades.

A ação orientada à pessoa será:

> **Entender disponibilidade dos dados**

## 15. Item anteriormente selecionado

Se a consulta anterior possuía uma oportunidade selecionada e uma alteração produzir zero resultados, a interface não deverá apagar a seleção silenciosamente.

O wireframe reformulado demonstra:

> **Seleção anterior fora da consulta atual**

A pessoa poderá:

- abrir o Detalhe se o item continuar disponível;
- remover conscientemente a seleção;
- desfazer a alteração;
- manter a nova consulta sem resultados.

Seleção anterior não deverá ser reinserida artificialmente no conjunto atual nem alterar o total zero.

## 16. Explicabilidade e cobertura

A pessoa deverá poder abrir `Entender este resultado` para verificar:

- região consultada;
- busca executada;
- filtros aplicados;
- período;
- horário da atualização;
- fontes ou categorias consultadas quando material;
- limitações conhecidas;
- distinção entre zero legítimo e erro.

A explicação não deverá expor lógica proprietária desnecessária nem ocultar limitações materiais.

## 17. Acessibilidade e resiliência

O estado deverá:

- anunciar textualmente o total zero;
- anunciar cobertura e atualização;
- não depender de cor, marcadores ou mapa vazio;
- possuir ordem de foco coerente;
- manter títulos e ações compreensíveis fora do contexto visual;
- permitir operação pela Lista;
- preservar conteúdo durante falhas cartográficas;
- evitar ciclos de tentativa automática;
- manter ações essenciais disponíveis em baixa conectividade quando possível.

A validação funcional não conclui conformidade técnica de acessibilidade.

## 18. Privacidade e autonomia

O estado preserva:

- localização opcional;
- posição não acessada quando verdadeiro;
- região manual distinta da posição pessoal;
- consulta sem personalização;
- ausência legítima sem preenchimento comercial artificial;
- ações de recuperação voluntárias;
- revisão antes de aplicar mudanças;
- alteração explícita e reversível;
- separação entre falha técnica e ausência de dados;
- proteção de endereços sensíveis;
- continuidade sem rastreamento.

## 19. Resultado da validação especializada

A UXA-031 considera o estado **funcionalmente válido após reformulação** porque:

- o zero permanece limitado à consulta atual;
- a cobertura passa a ser verificável;
- ausência, falha e indisponibilidade são distintas;
- região, busca, filtros e contexto permanecem visíveis;
- nenhuma recuperação altera a consulta sem revisão;
- `Desfazer` é condicional e identifica a alteração;
- seleção anterior é tratada sem falsear correspondência;
- Mapa e Lista preservam o mesmo estado;
- localização continua opcional;
- não há preenchimento comercial ou personalização artificial;
- o estado funciona sem mapa carregado.

## 20. Limites

Este incremento não:

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
