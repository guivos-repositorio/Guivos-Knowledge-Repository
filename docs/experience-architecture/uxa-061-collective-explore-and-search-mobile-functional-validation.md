---
id: UXA-061
title: Validação Funcional e Reformulação de Explorar Coletivos e Busca Móvel
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-03
parent: UXA-060
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-024
  - UXA-028
  - UXA-030
  - UXA-043
  - UXA-055
related:
  - UXA-062
  - M7.63
normative: false
---

# Validação Funcional e Reformulação de Explorar Coletivos e Busca Móvel

## 1. Finalidade

Este documento valida funcionalmente os cinco wireframes móveis materializados pela UXA-060 e registra as reformulações necessárias antes de qualquer ampliação da experiência de Coletivos.

A validação examina:

- hierarquia;
- continuidade entre estados;
- origem da descoberta;
- separação entre conteúdo orgânico e publicidade;
- preservação de busca, área e filtros;
- tratamento do estado sem resultados;
- privacidade territorial;
- acessibilidade textual;
- continuidade para o futuro Perfil Público do Coletivo.

A validação não representa teste com pessoas, design visual final, conformidade técnica de acessibilidade, algoritmo, protótipo ou implementação.

## 2. Artefatos examinados

1. `uxa-060-collective-explore-mobile.svg`;
2. `uxa-060-collective-search-results-mobile.svg`;
3. `uxa-060-collective-search-filters-mobile.svg`;
4. `uxa-060-collective-search-no-results-mobile.svg`;
5. `uxa-060-collective-discovery-origin-mobile.svg`.

Todos permanecem móveis, com referência de 390 × 844 pixels e baixa fidelidade.

## 3. Método

A análise foi realizada em duas camadas.

### 3.1 Validação especializada

Cada artefato foi examinado quanto a:

- finalidade dominante;
- ordem de leitura;
- ação principal;
- estados e rótulos;
- dados expostos;
- origem;
- privacidade;
- retorno e recuperação.

### 3.2 Validação transversal

A família foi examinada como sequência:

```text
Explorar Coletivos
→ iniciar busca ou selecionar tema
→ comparar resultados
→ abrir filtros sem perder consulta
→ compreender origem ou publicidade
→ retornar ao mesmo resultado
→ abrir futuro Perfil Público
```

O estado sem resultados foi validado como continuidade alternativa da mesma consulta.

## 4. Diagnóstico inicial

| Artefato | Diagnóstico inicial | Ação |
|---|---|---|
| Explorar Coletivos | hierarquia, área manual, categorias, origem e privacidade suficientes | aprovado sem alteração |
| Resultados de busca | publicidade não oferecia continuidade equivalente ao Perfil Público; limpeza possuía escopo ambíguo | reformulado |
| Filtros | seleções dependiam parcialmente de preenchimento visual; limpeza possuía escopo ambíguo | reformulado |
| Busca sem resultados | área e filtros estavam combinados no mesmo resumo; revisão anterior à mudança precisava ser explícita | reformulado |
| Explicação da origem | título genérico e fechamento não declaravam retorno ao resultado com contexto preservado | reformulado |

## 5. Explorar Coletivos

O artefato foi considerado funcionalmente válido sem alteração porque:

- permite busca direta;
- permite exploração por tema;
- mostra a área de exploração antes dos resultados;
- não exige localização precisa;
- funciona sem personalização;
- distingue exploração por tema e exploração on-line;
- identifica origem orgânica;
- conduz ao futuro Perfil Público;
- declara que visualizar não cria vínculo;
- mantém privacidade e navegação recorrente encontráveis.

A área `Com entrada disponível` poderá incluir entrada aberta ou mediante aprovação, desde que a disponibilidade real permaneça declarada.

## 6. Resultados de busca reformulados

A reformulação passou a demonstrar:

- área manual e ausência de localização precisa;
- ação `Limpar só filtros`, preservando busca e área;
- primeiro resultado orgânico;
- publicidade identificada antes do conteúdo;
- anunciante e critérios materiais;
- ordem orgânica preservada;
- continuidade `Ver perfil público` também no item patrocinado;
- explicação patrocinada separada da continuidade institucional;
- resultados orgânicos posteriores sem perda de hierarquia.

A publicidade não recebe uma superfície institucional inferior ou superior ao resultado orgânico. A natureza comercial é separada da possibilidade de compreender o Coletivo no Perfil Público.

## 7. Filtros reformulados

A reformulação passou a distinguir seleções sem depender apenas de cor ou preenchimento.

Os três filtros selecionados exibem marca textual:

- `Ciclismo · selecionado`;
- `Entrada disponível ✓`;
- `Híbrida ✓`.

Também ficaram explícitos:

- busca e área não mudam ao operar o painel;
- `Cancelar` não aplica alterações;
- `Limpar somente filtros` não apaga busca, área ou preferências de publicidade;
- preferências publicitárias permanecem fora dos filtros;
- nenhuma alteração é aplicada antes de `Aplicar 3 filtros`.

## 8. Estado sem resultados reformulado

A região foi separada das demais dimensões:

> **Belo Horizonte · região manual · sem localização precisa**

Os filtros permanecem em chips próprios.

O estado validado declara:

- total zero limitado à consulta;
- consulta concluída;
- cobertura verificada;
- busca, região e filtros preservados;
- publicidade ausente como preenchimento artificial;
- ações independentes para busca, filtros, região e modalidade;
- revisão anterior à aplicação de cada mudança;
- exploração paralela sem apagar a consulta;
- distinção entre zero, erro, cobertura parcial e conexão limitada.

`Cobertura verificada` somente poderá ser utilizada quando existir evidência correspondente em produção.

## 9. Explicação patrocinada reformulada

O título foi especializado:

> **Por que este anúncio?**

O fechamento foi substituído por:

> **Voltar aos resultados**

A explicação também declara que, ao retornar, permanecem:

- busca;
- área;
- filtros;
- posição do resultado.

O estado preserva:

- natureza comercial;
- anunciante;
- posição após o primeiro resultado orgânico;
- critérios objetivos;
- ausência de ampliação silenciosa;
- informações não utilizadas;
- identidade do visualizador não entregue ao anunciante;
- controles separados de ocultar, reduzir, desativar e denunciar.

## 10. Origem da descoberta

A família mantém as origens separadas:

- busca;
- exploração por tema;
- território;
- sugestão da Guivos;
- recomendação pessoal;
- convite;
- link compartilhado;
- publicidade.

A presença do mesmo Coletivo em mais de uma origem não autoriza representar uma origem como outra.

Sugestão, recomendação e convite permanecem contratos futuros de materialização detalhada. Sua nomenclatura nesta família funciona apenas como distinção de origem.

## 11. Ordenação e popularidade

A ordenação orgânica poderá considerar critérios autorizados pela UXA-056.

Permanecem excluídos como fatores dominantes:

- quantidade de participantes;
- volume de mensagens;
- popularidade genérica;
- duração na plataforma;
- plano contratado;
- publicidade;
- avaliação isolada.

A contagem aproximada de participantes funciona como contexto governado. Ela não cria ranking, prova de qualidade ou recomendação.

## 12. Publicidade

A validação confirma que:

- o primeiro resultado é orgânico;
- publicidade é identificada antes do conteúdo;
- anunciante e critérios são visíveis;
- pagamento não altera a ordem orgânica;
- publicidade não é recomendação;
- publicidade não preenche o estado sem resultados;
- filtros orgânicos e preferências publicitárias são controles diferentes;
- a identidade de quem apenas visualizou não é entregue ao anunciante;
- conteúdo protegido e dados sensíveis permanecem excluídos.

A família não aprova operação comercial real nem política publicitária definitiva para Coletivos.

## 13. Localização e território

A família funciona com área manual.

Permanecem distintos:

- cidade ou região informada;
- localização aproximada autorizada;
- localização precisa temporária;
- disponibilidade on-line;
- ausência de território.

A busca e o estado vazio não podem usar ausência de correspondência como justificativa para exigir localização precisa.

## 14. Continuidade para o Perfil Público

Todos os cartões capazes de conduzir ao Coletivo, inclusive conteúdo patrocinado autorizado, utilizam a continuidade:

> **Ver perfil público**

O futuro Perfil Público deverá receber, quando compatível com privacidade:

- origem;
- consulta;
- área;
- filtros;
- posição do resultado;
- relação comercial;
- estado de personalização.

Ao retornar, a pessoa deverá reencontrar o contexto anterior.

A validação não cria o Perfil Público.

## 15. Acessibilidade funcional

A família validada utiliza:

- títulos e descrições nos SVGs;
- rótulos textuais anteriores ao conteúdo;
- marcas textuais para filtros selecionados;
- total zero textual;
- ações nomeadas;
- origem e relação comercial escritas;
- hierarquia linear;
- ausência de dependência exclusiva de cor.

Conformidade técnica com tecnologia assistiva permanece pendente de protótipo e teste próprios.

## 16. Matriz de resultado

| Artefato | Resultado | Estado final |
|---|---|---|
| Explorar Coletivos | aprovado sem alteração | funcionalmente válido |
| Resultados de busca | aprovado após continuidade e escopo de limpeza | funcionalmente válido após reformulação |
| Filtros | aprovado após marcas textuais e escopo de limpeza | funcionalmente válido após reformulação |
| Busca sem resultados | aprovado após separação territorial e revisão explícita | funcionalmente válido após reformulação |
| Explicação patrocinada | aprovado após especialização e retorno contextual | funcionalmente válido após reformulação |

## 17. Critérios de aceite atendidos

1. busca e exploração permanecem úteis sem personalização;
2. área manual não equivale a localização precisa;
3. origens permanecem distinguíveis;
4. primeiro resultado permanece orgânico;
5. publicidade é identificada antes do conteúdo;
6. pagamento não altera ordem orgânica;
7. publicidade possui continuidade ao Perfil Público sem perder sua natureza comercial;
8. contagem de participantes não cria ranking;
9. busca, área e filtros permanecem separados;
10. cancelar filtros não altera a consulta;
11. limpar filtros preserva busca e área;
12. seleção não depende apenas de cor;
13. zero confirmado não é erro;
14. publicidade não preenche zero;
15. recuperação do zero é consciente e por dimensão;
16. explicação retorna ao resultado preservando contexto;
17. visualizar não cria acompanhamento ou participação;
18. nenhum protótipo ou desenvolvimento foi iniciado.

## 18. Cobertura atualizada

### Coletivos

- cinco wireframes de descoberta materializados;
- cinco wireframes funcionalmente validados;
- quatro reformulados;
- um preservado sem alteração;
- demais famílias ainda não materializadas.

### Opportunity Boost

Permanece separado:

- 46 wireframes materializados;
- 36 validados por pacote;
- dez estados residuais pendentes.

## 19. Limites

Esta validação não:

- cria dados reais;
- define algoritmo de busca ou publicidade;
- cria Perfil Público;
- cria fluxo de participação;
- cria protótipo;
- executa teste de usabilidade;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto;
- altera contratos econômicos;
- altera Resultados Empresariais.

## 20. Próximo ato recomendado

Após integração e nova autorização, o próximo pacote recomendado será:

> **UXA-062 — Wireframes Móveis do Perfil Público do Coletivo**

Esse pacote deverá permanecer limitado ao Perfil Público e aos estados de entrada aberta, aprovação, entradas fechadas e reputação com base insuficiente.

Nenhum ato posterior é iniciado automaticamente.
