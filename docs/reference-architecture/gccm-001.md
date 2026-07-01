---
id: GCCM-001
title: Guivos Core Capability Model
status: discovery
version: 0.2.0
owner: Guivos Enterprise Architecture
last_updated: 2026-07-01
layer: Reference Architecture
milestone: A2 — Functional Architecture Discovery
---

# GCCM-001 — Guivos Core Capability Model

## Estado

`Discovery`.

Este documento conduz a descoberta do conjunto mínimo e suficiente de Core Capabilities da Guivos. Nenhuma Core Capability está canônica nesta versão.

A primeira extração de evidências foi concluída sobre `GEB-P01-F01 — Essência da Guivos`, versão `0.2.0`, estado `consolidated`.

## Propósito

Definir, a partir de evidências existentes no GKR, as capacidades institucionais permanentes que explicam aquilo que a Guivos deve ser capaz de realizar em sua maturidade, independentemente de produtos, tecnologias, estruturas organizacionais ou implementações específicas.

## Pergunta arquitetural

> Quais capacidades institucionais permanentes são necessárias e suficientes para que a Guivos cumpra seu propósito em sua capacidade máxima?

## Definição de Core Capability

Uma Core Capability é uma capacidade institucional permanente, com propósito, responsabilidade e fronteiras próprias, indispensável à missão da Guivos e reutilizável por múltiplos produtos, serviços, experiências e arquiteturas de domínio.

Ela não é:

- produto;
- funcionalidade;
- serviço isolado;
- tecnologia;
- componente de software;
- área organizacional;
- processo temporário;
- nome comercial.

## Princípios de descoberta

### Evidence before naming

Nenhuma candidata será nomeada ou consolidada sem evidências rastreáveis no GKR.

### Minimum sufficient set

O objetivo não é maximizar a quantidade de capacidades, mas encontrar o menor conjunto capaz de explicar integralmente a Guivos.

### Technology independence

Core Capabilities permanecem válidas quando tecnologias, fornecedores, interfaces e implementações são substituídos.

### Product independence

Produtos combinam e disponibilizam capacidades. Produtos não definem, por si só, a existência de uma Core Capability.

### Irreducibility

Uma Core Capability não pode ser completamente explicada ou absorvida por outra sem perda relevante de responsabilidade arquitetural.

### Mission coverage

O conjunto final deve cobrir integralmente o propósito, a missão operacional, o modelo fundamental, a geração de valor e a operação madura da Guivos.

## Fontes de evidência

A descoberta deverá utilizar, prioritariamente:

1. Foundation Architecture;
2. modelos fundamentais do GEB;
3. Product Architecture;
4. Business Architecture;
5. Research Domain e suas sínteses;
6. ADRs e validações arquiteturais;
7. princípios e modelos consolidados da GEA;
8. demais ativos relevantes, com status e limites explicitados.

Hipóteses, drafts e ativos experimentais podem gerar candidatas, mas não constituem evidência suficiente para promoção isolada.

## Método de descoberta

### Etapa 1 — Evidence Extraction

Extrair, sem consolidar prematuramente:

- afirmações institucionais;
- verbos institucionais;
- significados institucionais;
- invariantes;
- responsabilidades;
- objetivos;
- estados desejados;
- decisões;
- relações;
- capacidades explícitas ou implícitas.

A decomposição em afirmações atômicas é uma técnica operacional de análise, não uma nova camada canônica da arquitetura.

### Etapa 2 — Semantic Clustering

Agrupar evidências equivalentes ou fortemente relacionadas, mantendo referências às fontes originais.

### Etapa 3 — Candidate Formulation

Converter agrupamentos suficientemente distintos em candidatas provisórias.

### Etapa 4 — Admission Tests

Submeter cada candidata aos testes de permanência, propósito, fronteira, composição, independência e autonomia evolutiva.

### Etapa 5 — Destruction and Irreducibility Tests

Tentar eliminar, fundir, reduzir ou reclassificar cada candidata.

### Etapa 6 — Mission Coverage

Avaliar se o conjunto remanescente cobre integralmente a Guivos sem redundâncias relevantes.

### Etapa 7 — Architectural Validation

Registrar divergências, lacunas, sobreposições e justificativas antes de qualquer promoção.

### Etapa 8 — Canonical Catalog

Promover somente capacidades suficientemente demonstradas, mediante a governança arquitetural aplicável.

## Core Capability Admission Rule

Uma candidata somente poderá avançar quando atender simultaneamente aos seguintes critérios:

1. **Permanência:** continuará relevante na maturidade da Guivos.
2. **Essencialidade:** sua ausência compromete materialmente a missão ou o modelo operacional.
3. **Propósito próprio:** possui razão de existir distinta.
4. **Fronteiras explícitas:** responsabilidades e exclusões podem ser descritas sem ambiguidade material.
5. **Composição:** agrega múltiplas capacidades derivadas ou responsabilidades relacionadas.
6. **Independência de produto:** não existe apenas por causa de um produto atual.
7. **Independência tecnológica:** não depende de tecnologia ou fornecedor específico.
8. **Reutilização:** pode servir a múltiplos produtos, experiências, participantes ou contextos.
9. **Irredutibilidade:** não pode ser absorvida integralmente por outra candidata.
10. **Rastreabilidade:** possui evidências identificáveis no GKR.

## Testes de destruição

Para cada candidata, responder:

1. a Guivos ainda cumpre sua missão sem esta capacidade?
2. outra candidata consegue absorvê-la integralmente?
3. trata-se apenas de produto, canal, serviço, feature ou tecnologia?
4. ela permanece válida em diferentes países, culturas e gerações tecnológicas?
5. possui decisões e responsabilidades próprias?
6. sua existência reduz ou aumenta desnecessariamente a complexidade do modelo?

## Evidence Extraction — Foundation / Essência

### Fonte analisada

| Campo | Valor |
|---|---|
| Fonte | `GEB-P01-F01 — Essência da Guivos` |
| Versão | `0.2.0` |
| Estado da fonte | `consolidated` |
| Data da análise | 01/07/2026 |
| Resultado | Primeira passagem concluída |

### Resultado quantitativo

| Artefato analítico | Quantidade |
|---|---:|
| Afirmações institucionais atômicas | 29 |
| Grupos de significado institucional | 5 |
| Invariantes provisórios | 6 |
| Responsabilidades institucionais | 9 |
| Agrupamentos de evidência observados | 6 |

### Invariantes provisórios extraídos

| ID | Invariante provisório | Base principal |
|---|---|---|
| INV-F01-01 | A Guivos existe para potencializar processos de evolução, não para ser um fim em si mesma. | Finalidade, evolução e redução da distância até o Próximo Passo |
| INV-F01-02 | A autonomia do participante deve ser preservada. | Não impor caminhos, não definir sucesso e não decidir pelo participante |
| INV-F01-03 | A Guivos amplia condições para transformação sem impô-la. | Oportunidades, experiências e preservação da decisão do participante |
| INV-F01-04 | A atuação da Guivos deve considerar o contexto e o momento de vida do participante. | Momento Atual, Próximo Passo e relevância contextual |
| INV-F01-05 | A Guivos fortalece o ecossistema sem substituir seus participantes. | Pessoas, Organizações, Coletivos e instituições |
| INV-F01-06 | Decisões futuras devem demonstrar contribuição para a jornada de evolução. | Critério de aderência para funcionalidades, produtos, parcerias e tecnologias |

Os invariantes permanecem provisórios até confirmação por outras fontes canônicas.

### Responsabilidades institucionais extraídas

| ID | Responsabilidade institucional | Origem principal |
|---|---|---|
| RESP-F01-01 | Manter a evolução da Guivos orientada à jornada de evolução dos participantes. | INV-F01-01 |
| RESP-F01-02 | Preservar a autonomia do participante em recomendações, decisões, experiências e interações. | INV-F01-02 |
| RESP-F01-03 | Ampliar condições para transformação sem impor caminhos, metas ou resultados. | INV-F01-03 |
| RESP-F01-04 | Compreender o contexto atual do participante antes de apoiar próximos passos. | INV-F01-04 |
| RESP-F01-05 | Identificar possibilidades relevantes para o momento de vida do participante. | INV-F01-04 |
| RESP-F01-06 | Fortalecer conexões entre participantes sem substituí-los. | INV-F01-05 |
| RESP-F01-07 | Preservar o papel ativo dos participantes no ecossistema. | INV-F01-05 |
| RESP-F01-08 | Avaliar funcionalidades, produtos, parcerias e tecnologias pela contribuição à jornada. | INV-F01-06 |
| RESP-F01-09 | Reavaliar a aderência de elementos que não contribuam para a jornada do participante. | INV-F01-06 |

### Agrupamentos de evidência observados

| ID | Agrupamento provisório | Natureza | Estado |
|---|---|---|---|
| EV-F01-01 | Compreensão de contexto | Funcional | Observed |
| EV-F01-02 | Identificação de possibilidades relevantes | Funcional | Observed |
| EV-F01-03 | Conexão e fortalecimento do ecossistema | Funcional | Observed |
| EV-F01-04 | Apoio à progressão da jornada | Funcional | Observed |
| EV-F01-05 | Preservação da autonomia | Constitucional | Observed |
| EV-F01-06 | Governança de aderência à jornada | Constitucional | Observed |

Esses agrupamentos não são Core Capabilities. Eles poderão ser fortalecidos, fundidos, reclassificados ou rejeitados após análise de outras fontes.

### Revisão crítica da primeira extração

A análise demonstrou que:

- a Foundation fornece identidade, limites, obrigações e critérios de decisão;
- nem toda evidência arquitetural deve originar uma Core Capability;
- evidências funcionais e restrições constitucionais devem permanecer distinguíveis;
- agrupamentos analíticos não constituem, por si só, novas camadas arquiteturais;
- a hipótese de `Institutional Functions` foi rejeitada como camada permanente por apenas reorganizar responsabilidades existentes;
- nenhuma candidata pode ser promovida com base exclusiva nesta fonte.

## Estrutura de registro de evidências

| ID | Fonte | Evidência extraída | Tipo | Agrupamento provisório | Observações |
|---|---|---|---|---|---|
| EV-F01-01 | GEB-P01-F01 | Compreender o Momento Atual e o contexto do participante | Funcional | Compreensão de contexto | Requer confirmação cruzada |
| EV-F01-02 | GEB-P01-F01 | Identificar possibilidades relevantes ao momento de vida | Funcional | Identificação de possibilidades | Requer confirmação cruzada |
| EV-F01-03 | GEB-P01-F01 | Fortalecer conexões entre participantes sem substituí-los | Funcional | Conexão do ecossistema | Requer confirmação cruzada |
| EV-F01-04 | GEB-P01-F01 | Apoiar a redução da distância até o Próximo Passo | Funcional | Progressão da jornada | Requer confirmação cruzada |
| EV-F01-05 | GEB-P01-F01 | Preservar autonomia, definição de sucesso e decisão do participante | Constitucional | Autonomia | Restrição arquitetural; não implica Capability isolada |
| EV-F01-06 | GEB-P01-F01 | Avaliar aderência pela contribuição à jornada de evolução | Constitucional | Governança de aderência | Pode orientar todas as futuras capacidades |

## Registro de candidatas

| ID | Candidata | Evidências associadas | Estado | Resultado dos testes |
|---|---|---|---|---|
| — | — | — | — | Nenhuma candidata registrada |

Estados previstos:

- Observed;
- Clustered;
- Candidate;
- Under Test;
- Retained;
- Merged;
- Rejected;
- Validated;
- Canonical.

## Catálogo canônico

Nenhuma Core Capability canônica nesta versão.

## Hierarquia posterior

Após a validação do catálogo, cada Core Capability poderá ser decomposta, quando necessário, em:

```text
Core Capability
  -> Capability
    -> Business Service
      -> Application Service
        -> Component
          -> Implementation
```

Essa hierarquia não autoriza a antecipação de decisões de implementação durante a descoberta das Core Capabilities.

## Governança

- o owner do GCCM é a Guivos Enterprise Architecture;
- cada candidata deve manter rastreabilidade até suas evidências;
- fusões, rejeições e promoções devem registrar justificativa;
- novas Core Capabilities não podem ser criadas diretamente por arquiteturas de domínio;
- arquiteturas de domínio reutilizam ou especializam o catálogo validado;
- mudanças estruturais no modelo exigem análise de impacto e governança correspondente.

## Critério de conclusão da versão de descoberta

A fase de descoberta estará concluída quando:

1. o inventário mínimo de fontes prioritárias tiver sido analisado;
2. as evidências estiverem registradas e agrupadas;
3. todas as candidatas tiverem sido submetidas aos testes;
4. o conjunto remanescente demonstrar cobertura da missão;
5. sobreposições e lacunas estiverem explicitadas;
6. houver base suficiente para uma validação arquitetural formal.

## Próximo passo

Analisar a próxima unidade da Foundation Architecture e verificar se ela confirma, enfraquece, amplia ou contradiz os seis agrupamentos observados em `GEB-P01-F01`, sem formular Core Capabilities antes da convergência entre múltiplas fontes.
