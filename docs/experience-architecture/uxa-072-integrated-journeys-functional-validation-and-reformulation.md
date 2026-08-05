---
id: UXA-072
title: Validação Funcional e Reformulação das Jornadas Integradas
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-071
  - GKR-JOURNEYS-001
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-SCENARIOS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.46.0
  - M7.72
normative: false
---

# Validação Funcional e Reformulação das Jornadas Integradas

## 1. Finalidade

Este pacote valida a materialização documental criada pela UXA-071 para determinar se a seção **Jornadas Integradas** já funciona como uma área própria, rastreável, compreensível e governada dentro do Guivos Knowledge Repository.

A validação examina:

- presença e acessibilidade da seção no GKR publicado;
- coerência entre Pessoa, Coletivo e Organização;
- rastreabilidade até contratos, programas, wireframes e validações canônicas;
- separação entre maturidade, materialização e evidência de validação;
- legitimidade das transições e handoffs apresentados;
- consistência dos cenários documentais;
- fidelidade do catálogo de telas;
- exposição de lacunas e continuidades ausentes;
- sincronização com o Registro do Estado Atual, roadmap e índice da Arquitetura da Experiência;
- preservação dos limites entre documentação, protótipo e implementação.

A UXA-072 não valida usabilidade com pessoas, não testa software e não autoriza protótipo, aplicação, motor de simulação ou Engenharia de Produto.

## 2. Escopo examinado

Foram examinados os seguintes artefatos integrados pela UXA-071:

1. `docs/journeys/index.md`;
2. `docs/journeys/person.md`;
3. `docs/journeys/collective.md`;
4. `docs/journeys/organization.md`;
5. `docs/journeys/handoffs.md`;
6. `docs/journeys/scenarios.md`;
7. `docs/journeys/screen-catalog.md`;
8. `docs/journeys/gaps.md`;
9. `docs/experience-architecture/uxa-071-integrated-journeys-map-materialization.md`.

Também foram confrontados:

- `mkdocs.yml`;
- `docs/project/current-state-register.md`;
- `docs/roadmap.md`;
- `docs/experience-architecture/index.md`;
- UXA-070 e autoridades citadas pelos mapas.

Base auditada: `main` em `3ee23476af22d15598b8390c3be017f2cd01d570`.

## 3. Método

Cada requisito recebeu uma das classificações:

| Resultado | Significado |
|---|---|
| aprovado | requisito demonstrado sem correção obrigatória |
| aprovado com ressalva | requisito presente, mas requer precisão ou reforço não bloqueador |
| parcial | parte demonstrada e parte ainda sem evidência suficiente |
| reprovado | requisito não atendido ou contradito pelo estado do Repositório |
| não aplicável | requisito fora do escopo documental |

A validação não promove uma tela, transição ou jornada apenas porque ela aparece em um diagrama ou sequência textual.

## 4. Parecer executivo

> **Resultado: não aprovado até reformulação obrigatória.**

A UXA-071 criou os arquivos necessários e estabeleceu uma boa estrutura inicial de leitura. Entretanto, a seção ainda não pode ser declarada funcionalmente validada porque existem quatro bloqueios:

1. **a seção não está presente na navegação principal do MkDocs**, portanto não funciona como seção própria acessível no GKR publicado;
2. **os registros centrais continuam declarando a UXA-071 e o mapa integrado como não iniciados**, produzindo divergência com a `main`;
3. **maturidade, materialização e validação são combinadas em várias células**, contrariando a taxonomia controlada da UXA-070;
4. **telas individualmente validadas são apresentadas em sequências que podem ser interpretadas como jornada integrada validada**, embora transições e handoffs ainda não tenham evidência equivalente.

Os artefatos permanecem válidos como **primeira materialização documental em rascunho**. Eles não estão rejeitados, mas necessitam de reformulação e nova validação antes de serem promovidos como seção funcionalmente validada.

## 5. Resultado por critério

| Critério | Resultado | Síntese |
|---|---|---|
| seção interna criada no Repositório | aprovado | oito arquivos de domínio e uma autoridade UXA foram criados |
| seção própria acessível no GKR publicado | reprovado | `mkdocs.yml` não contém `Jornadas Integradas` na navegação |
| separação de Pessoa, Coletivo e Organização | aprovado | participantes estruturais permanecem distintos |
| separação entre participante, papel e autoridade | aprovado com ressalva | modelo está correto, mas alguns handoffs não explicitam maturidade dos dois lados |
| reutilização canônica por referência | aprovado | nenhum SVG ou contrato foi duplicado como nova fonte de verdade |
| exposição de lacunas | aprovado | lacunas materiais estão visíveis e priorizadas |
| taxonomia de maturidade | reprovado | estados compostos misturam contrato, materialização e validação |
| legitimidade de nós | aprovado com ressalva | nós possuem referências, mas nem sempre distinguem tipo de evidência |
| legitimidade de transições | parcial | sequências são úteis, porém parte das ligações não possui evidência de integração validada |
| handoffs entre autoridades | parcial | responsabilidades estão descritas, mas várias superfícies de destino não foram materializadas |
| cenários documentais | parcial | cenários são compreensíveis, mas cobertura de telas não equivale a validação ponta a ponta |
| catálogo de telas | aprovado com ressalva | inventário inicial é útil, porém deve separar tela validada de continuidade validada |
| equivalência textual | aprovado | todos os mapas possuem leitura textual |
| acessibilidade de navegação | reprovado | ausência na navegação impede acesso como seção de primeiro nível |
| sincronização do estado global | reprovado | GKR-STATE-001 permanece em 1.99.0 e declara o mapa não iniciado |
| sincronização do roadmap | reprovado | ROADMAP-12.46.0 ainda recomenda iniciar a UXA-071 |
| sincronização da Arquitetura da Experiência | reprovado | UXA-000 ainda lista UXA-071 e materialização como não iniciadas |
| limites de produto e engenharia | aprovado | nenhum protótipo, aplicação, motor ou Engenharia de Produto foi iniciado |

## 6. Achados controlados

### UXA-072-F01 — Seção ausente da navegação principal

**Severidade:** bloqueadora.

Os arquivos em `docs/journeys/` são construídos pelo MkDocs por causa da configuração de conteúdo, mas não aparecem como uma área própria na navegação principal.

Isso viola a decisão registrada de que `Jornadas Integradas` deve ser uma seção de primeiro nível do GKR.

**Correção obrigatória:** adicionar ao `mkdocs.yml` uma seção equivalente a:

```yaml
- Jornadas Integradas:
    - Visão Geral: journeys/index.md
    - Pessoa: journeys/person.md
    - Coletivo: journeys/collective.md
    - Organização: journeys/organization.md
    - Handoffs: journeys/handoffs.md
    - Cenários: journeys/scenarios.md
    - Catálogo de Telas: journeys/screen-catalog.md
    - Lacunas: journeys/gaps.md
```

A posição final deverá preservar a leitura arquitetural do Repositório e não ocultar a relação com a Arquitetura da Experiência.

### UXA-072-F02 — Registro do Estado Atual contraditório

**Severidade:** bloqueadora.

O GKR-STATE-001 ainda declara:

- marco centrado apenas no programa funcional da UXA-070;
- ambiente sem materialização;
- mapa integrado documental não iniciado;
- UXA-071 como próxima transição autorizável;
- UXA-071 não iniciada.

Essas declarações foram superadas pela integração do PR nº 167.

**Correção obrigatória:** publicar nova versão do GKR-STATE-001 que reconheça:

- UXA-071 materializada em rascunho;
- seção `Jornadas Integradas` existente;
- validação UXA-072 concluída com resultado não aprovado até reformulação;
- navegação e sincronização como bloqueios vigentes;
- protótipo, teste com pessoas, aplicação, motor e Engenharia de Produto ainda não iniciados.

### UXA-072-F03 — Roadmap desatualizado

**Severidade:** bloqueadora.

O ROADMAP-12.46.0 ainda apresenta a UXA-071 como iniciativa futura e declara o mapa integrado como não iniciado.

**Correção obrigatória:** publicar versão sucessora do roadmap com a sequência real:

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — validação funcional reprovada até reformulação
→ pacote de remediação e sincronização
→ nova validação funcional
→ protótipo somente mediante autorização posterior
→ Engenharia de Produto somente após gates próprios
```

### UXA-072-F04 — Índice da Arquitetura da Experiência desatualizado

**Severidade:** bloqueadora.

A UXA-000 ainda declara como não iniciados:

- UXA-071;
- materialização do mapa integrado.

Também recomenda UXA-071 como próxima transição.

**Correção obrigatória:** atualizar o índice para reconhecer UXA-071, UXA-072 e o estado de reformulação obrigatória.

### UXA-072-F05 — Estados de maturidade compostos

**Severidade:** alta.

A UXA-070 definiu estados controlados individuais, como `contratado`, `materializado`, `validado` e `não iniciado`.

Nos mapas, expressões como as seguintes combinam dimensões diferentes:

- `contratada e validada`;
- `materializada e validada`;
- `materializada, reformulada e validada`;
- `contratado; materialização parcial`.

Essas expressões dificultam responder qual é o estado primário do nó e qual evidência sustenta esse estado.

**Correção obrigatória:** separar, no mínimo, as colunas:

| Campo | Função |
|---|---|
| maturidade primária | um único estado controlado da UXA-070 |
| autoridade contratual | contrato ou programa que governa a responsabilidade |
| referência materializada | documento, wireframe ou SVG existente |
| evidência de validação | pacote que validou a referência materializada |
| continuidade integrada | validada, parcial, ausente ou não examinada |

### UXA-072-F06 — Validação de tela confundida com validação de jornada

**Severidade:** alta.

As contagens `17/17` e `22/22` demonstram que referências visuais específicas foram materializadas e validadas em seus respectivos pacotes.

Elas não demonstram automaticamente que:

- todas as transições entre as telas foram validadas como sequência integrada;
- todos os handoffs entre participantes foram materializados dos dois lados;
- a jornada está completa;
- entradas, retornos, interrupções e saídas possuem cobertura equivalente.

**Correção obrigatória:** toda tabela ou cenário deverá distinguir:

```text
cobertura das superfícies
≠ cobertura das transições
≠ validação da jornada integrada
```

### UXA-072-F07 — Handoffs com cobertura assimétrica

**Severidade:** alta.

A matriz de handoffs descreve corretamente as autoridades conceituais, mas vários destinos ainda não possuem superfície materializada, incluindo:

- operação da solicitação pelo responsável do Coletivo;
- Visão Geral do Responsável;
- gestão bilateral da relação Organização–Coletivo;
- aplicação institucional completa;
- continuidade depois de `Solicitação Pendente`.

**Correção obrigatória:** cada handoff deverá registrar separadamente:

- maturidade da origem;
- maturidade do destino;
- autoridade da decisão;
- evidência da transição;
- condição de retorno ou contestação;
- lacuna aplicável.

Nenhuma linha poderá sugerir simetria quando apenas a perspectiva da Pessoa estiver materializada.

### UXA-072-F08 — Cenários excedem a evidência integrada disponível

**Severidade:** média-alta.

Os seis cenários são adequados como hipóteses documentais governadas. Entretanto, alguns textos podem ser lidos como demonstração de fluxo completo.

**Correção obrigatória:** cada cenário deverá possuir cabeçalho de evidência com:

- finalidade;
- participantes e perspectivas;
- nós materializados;
- nós apenas contratados;
- transições validadas;
- transições documentais não validadas;
- ponto exato de interrupção por lacuna;
- conclusão permitida e conclusão proibida.

### UXA-072-F09 — Catálogo sem coluna de continuidade integrada

**Severidade:** média.

O catálogo registra quantidades de telas e validações, mas não demonstra se as ligações entre elas foram examinadas como jornada.

**Correção obrigatória:** adicionar coluna ou matriz complementar para:

- superfície materializada;
- superfície validada;
- transição de entrada validada;
- transição de saída validada;
- perspectiva coberta;
- lacuna associada.

### UXA-072-F10 — Status documental inconsistente

**Severidade:** média.

Os principais arquivos permanecem `draft`, enquanto o registro de lacunas está `active`. Essa diferença não é necessariamente incorreta, mas não existe explicação explícita sobre o que pode ser tratado como vigente.

**Correção obrigatória:** após a remediação:

- manter como `draft` qualquer mapa ainda não revalidado;
- manter o registro de lacunas como `active` somente se ele for declarado observacional e não promocional;
- promover documentos para `active` apenas depois de nova validação aprovada;
- registrar a versão validada de cada artefato.

## 7. Validação por arquivo

### 7.1 `docs/journeys/index.md`

**Resultado:** parcial.

Pontos aprovados:

- finalidade compreensível;
- separação entre ambiente documental e produto;
- acesso às oito vistas internas;
- primeiro diagrama integrado;
- limites explícitos.

Correções necessárias:

- inserir estado de validação visível;
- explicar que a sequência integrada ainda não foi validada ponta a ponta;
- separar cobertura de telas e cobertura de transições;
- tornar a seção acessível na navegação principal.

### 7.2 `docs/journeys/person.md`

**Resultado:** parcial.

Pontos aprovados:

- início protegido corretamente ordenado;
- autorização separada de processamento e personalização;
- participação em Coletivos não confundida com aprovação;
- lacuna antes de `Meus Coletivos` identificada.

Correções necessárias:

- separar maturidade primária das evidências;
- não declarar a sequência completa validada apenas por causa dos 17 estados;
- identificar transições que ainda não possuem pacote de validação integrada;
- registrar entradas, saídas e interrupções por nó.

### 7.3 `docs/journeys/collective.md`

**Resultado:** parcial.

Pontos aprovados:

- perspectivas de participante e responsável separadas;
- lacunas do responsável expostas;
- autonomia do Coletivo preservada;
- patrocínio sem autoridade sobre pertencimento.

Correções necessárias:

- marcar explicitamente que a operação pelo responsável é majoritariamente contratada ou não iniciada;
- separar a jornada percebida pela Pessoa da capacidade operacional do Coletivo;
- não representar handoff concluído quando a superfície receptora não existe;
- associar cada lacuna à transição interrompida.

### 7.4 `docs/journeys/organization.md`

**Resultado:** parcial.

Pontos aprovados:

- Visão Geral da Organização referenciada corretamente;
- relação bilateral não transfere propriedade ou autoridade;
- dados pessoais e conhecimento institucional permanecem separados;
- matriz institucional incompleta é reconhecida.

Correções necessárias:

- diferenciar contrato bilateral de materialização bilateral;
- identificar quais fases possuem apenas autoridade documental;
- registrar cobertura por unidade, representante e decisão;
- não tratar a relação como fluxo operacional existente.

### 7.5 `docs/journeys/handoffs.md`

**Resultado:** parcial.

Pontos aprovados:

- handoff não é tratado como transferência automática de autoridade;
- condições e limites estão presentes;
- casos relevantes foram inventariados.

Correções necessárias:

- adicionar maturidade de origem e destino;
- registrar evidência específica da transição;
- mostrar assimetria quando apenas um lado possui wireframe;
- distinguir handoff contratado, materializado e validado.

### 7.6 `docs/journeys/scenarios.md`

**Resultado:** parcial.

Pontos aprovados:

- seis cenários previstos pela UXA-070 foram representados;
- cenários comerciais permanecem subordinados à experiência;
- lacunas são mencionadas.

Correções necessárias:

- criar cabeçalho de evidência por cenário;
- interromper visualmente o fluxo no primeiro nó ou handoff não materializado;
- não usar uma sequência contínua para transições ainda não validadas;
- declarar explicitamente o limite da conclusão permitida.

### 7.7 `docs/journeys/screen-catalog.md`

**Resultado:** aprovado com ressalva.

Pontos aprovados:

- referências canônicas preservadas;
- contagens por família mantidas separadas;
- estados não iniciados não recebem arquivos fictícios;
- Opportunity Boost não é somado às jornadas humanas.

Correções necessárias:

- adicionar cobertura de entrada, saída e continuidade;
- distinguir validação da tela de validação da jornada;
- registrar a versão exata das referências quando o catálogo for promovido.

### 7.8 `docs/journeys/gaps.md`

**Resultado:** aprovado com ressalva.

Pontos aprovados:

- lacunas relevantes e materiais foram registradas;
- prioridades iniciais são coerentes;
- nenhuma ausência foi preenchida por suposição.

Correções necessárias:

- incluir a ausência da seção no `mkdocs.yml`;
- incluir dessincronização de GKR-STATE-001, roadmap e UXA-000;
- associar cada lacuna a nós e transições afetados;
- separar lacuna de experiência, lacuna documental e lacuna de governança.

### 7.9 UXA-071

**Resultado:** materialização confirmada; validação funcional não aprovada.

A UXA-071 cumpriu sua finalidade de criar uma primeira referência estática e inspecionável. Ela não deve ser revertida nem tratada como inexistente.

Seu estado correto até a remediação é:

```text
materialização criada
→ validação examinada
→ reformulação obrigatória
→ nova validação pendente
```

## 8. Contrato de reformulação obrigatória

A remediação deverá executar, em um único pacote governado ou em pacotes explicitamente encadeados:

1. adicionar `Jornadas Integradas` ao `mkdocs.yml` como seção própria;
2. atualizar GKR-STATE-001 para refletir UXA-071 e UXA-072;
3. publicar sucessor do ROADMAP-12.46.0;
4. atualizar UXA-000 e incluir UXA-072;
5. atualizar UXA-071 com o resultado desta validação;
6. revisar os oito arquivos em `docs/journeys/`;
7. separar maturidade, autoridade, materialização, validação e continuidade;
8. marcar transições integradas como validadas, parciais, ausentes ou não examinadas;
9. explicitar cobertura assimétrica nos handoffs;
10. adicionar estado de validação no índice da seção;
11. atualizar a fila de lacunas com problemas de navegação e governança;
12. executar validação mecânica do Repositório;
13. submeter a seção reformulada a nova validação funcional.

## 9. Critérios para aprovação futura

A seção poderá ser aprovada quando:

- estiver visível como seção própria na navegação do GKR;
- GKR-STATE-001, roadmap e UXA-000 estiverem sincronizados;
- cada nó possuir um único estado de maturidade primário;
- autoridade, materialização e validação estiverem em campos separados;
- nenhuma contagem de telas for apresentada como validação automática da jornada;
- cada handoff mostrar maturidade dos dois lados;
- cenários interromperem a continuidade onde houver lacuna;
- catálogo distinguir superfície e transição;
- links, IDs, front matter e navegação passarem pela validação mecânica;
- uma nova validação funcional não encontrar bloqueios.

## 10. Preservações

Este parecer não:

- remove os arquivos da UXA-071;
- invalida wireframes ou validações canônicas anteriores;
- altera contratos funcionais;
- cria telas ausentes;
- materializa `Meus Coletivos`;
- materializa Central de Atualizações;
- cria Visão Geral do Responsável;
- cria operação bilateral de Organização e Coletivo;
- conclui os dez estados residuais do Opportunity Boost;
- cria protótipo navegável;
- implementa aplicação ou motor de simulação;
- inicia teste com pessoas;
- inicia Engenharia de Produto;
- autoriza integração automática de qualquer pacote posterior.

## 11. Próxima transição recomendada

**UXA-073 — Reformulação, Navegação e Sincronização das Jornadas Integradas.**

O pacote futuro deverá corrigir os bloqueios UXA-072-F01 a UXA-072-F10 e preparar a seção para uma nova validação funcional.

A UXA-073 depende de autorização separada para criação e de nova autorização para integração. Ela não corresponderá a protótipo ou implementação técnica.