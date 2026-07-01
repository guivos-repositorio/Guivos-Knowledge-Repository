---
id: GCCM-001
title: Guivos Core Capability Model
status: discovery
version: 0.3.0
owner: Guivos Enterprise Architecture
last_updated: 2026-07-01
layer: Reference Architecture
milestone: A2 — Functional Architecture Discovery
---

# GCCM-001 — Guivos Core Capability Model

## Estado

`Discovery`.

Este documento conduz a descoberta do conjunto mínimo e suficiente de Core Capabilities da Guivos. Nenhuma Core Capability está canônica nesta versão.

A Evidence Extraction foi concluída para cinco das seis unidades da Foundation:

- `GEB-P01-F01 — Essência da Guivos`;
- `GEB-P01-F02 — Propósito`;
- `GEB-P01-F03 — Missão Operacional`;
- `GEB-P01-F04 — Visão de Longo Prazo`;
- `GEB-P01-F05 — Constituição da Guivos`.

`GEB-P01-F06 — Princípios Permanentes` permanece pendente antes da revisão consolidada da Foundation.

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

### Evidence recurrence

Nenhuma Core Capability pode ser promovida a partir de uma única unidade documental. Repetição, centralidade e consistência entre fontes devem preceder a formulação de candidatas.

### Hypothesis separation

Hipóteses podem orientar observação, mas não entram na Canon nem no catálogo de capacidades sem validação suficiente.

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

## Método de descoberta estabilizado

O método permanece congelado durante a execução da Foundation. Alterações metodológicas somente devem ocorrer diante de limitação concreta, inconsistência comprovada ou melhoria demonstrada pela aplicação.

### Etapa 1 — Evidence Extraction

Extrair, sem consolidar prematuramente:

- afirmações institucionais atômicas;
- significados institucionais;
- invariantes;
- responsabilidades;
- objetivos e estados desejados;
- decisões e relações;
- capacidades explícitas ou implícitas.

A decomposição em afirmações atômicas é técnica operacional de análise, não uma nova camada canônica.

### Etapa 2 — Evidence Convergence

Comparar evidências entre fontes segundo:

- frequência;
- centralidade;
- consistência;
- confirmação, ampliação, ausência ou contradição;
- natureza funcional, constitucional, estrutural ou informacional.

Agrupamentos de evidência são instrumentos analíticos. Não constituem Core Capabilities.

### Etapa 3 — Confidence Assessment

Ao concluir cada fonte, avaliar:

- consistência;
- originalidade;
- relevância arquitetural;
- impacto na convergência.

A avaliação controla a qualidade da descoberta e não integra a Canon da Foundation.

### Etapa 4 — Semantic Clustering

Agrupar evidências equivalentes ou fortemente relacionadas, mantendo referências às fontes originais.

### Etapa 5 — Candidate Formulation

Converter apenas agrupamentos suficientemente distintos e recorrentes em candidatas provisórias.

### Etapa 6 — Admission Tests

Submeter cada candidata aos testes de permanência, propósito, fronteira, composição, independência, reutilização e autonomia evolutiva.

### Etapa 7 — Destruction and Irreducibility Tests

Tentar eliminar, fundir, reduzir ou reclassificar cada candidata.

### Etapa 8 — Mission Coverage

Avaliar se o conjunto remanescente cobre integralmente a Guivos sem redundâncias relevantes.

### Etapa 9 — Architectural Validation

Registrar divergências, lacunas, sobreposições e justificativas antes de qualquer promoção.

### Etapa 10 — Canonical Catalog

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

## Foundation Evidence Progress — 5/6

| Fonte | Assertions | Meanings | Invariants | Responsibilities | Estado |
|---|---:|---:|---:|---:|---|
| F01 — Essência | 29 | 5 | 6 | 9 | Concluída |
| F02 — Propósito | 25 | 5 | 7 | 7 | Concluída |
| F03 — Missão Operacional | 19 | 5 | 5 | 6 | Concluída |
| F04 — Visão de Longo Prazo | 31 | 6 | 8 | 8 | Concluída |
| F05 — Constituição | 30 | 8 | 10 | 10 | Concluída |
| F06 — Princípios Permanentes | — | — | — | — | Pendente |

Totais provisórios antes da deduplicação e da revisão da Foundation:

- 134 afirmações institucionais atômicas;
- 29 grupos de significado;
- 36 invariantes provisórios;
- 40 responsabilidades institucionais.

## Convergência provisória da Foundation

### Agrupamentos recorrentes

1. Compreensão de contexto.
2. Identificação de possibilidades relevantes.
3. Conexão e fortalecimento do ecossistema.
4. Apoio à progressão da jornada.
5. Preservação da autonomia.
6. Governança de aderência à jornada.
7. Universalidade e inclusão contextual.
8. Tecnologia subordinada ao propósito.
9. Ecossistema irredutível a produtos.
10. Coerência arquitetural sob variação.

### Agrupamentos adicionais observados

- espiritualidade não coercitiva;
- tradução do propósito em execução diária;
- orientação de IA e experiência pela missão;
- escalabilidade e internacionalização;
- extensibilidade para oportunidades futuras;
- conhecimento como patrimônio permanente;
- IA como intérprete, não substituta do conhecimento;
- simplicidade e suficiência arquitetural;
- oportunidade como meio subordinado à evolução.

Esses agrupamentos ainda poderão ser fundidos, reclassificados, enfraquecidos ou rejeitados na revisão consolidada.

## Descobertas institucionais consolidadas até F05

As fontes analisadas sustentam as seguintes relações:

- evolução é finalidade;
- oportunidade é meio;
- tecnologia, IA, dados e automações são instrumentos;
- o participante mantém a decisão;
- conhecimento é patrimônio permanente;
- a Guivos é ecossistema, não produto isolado;
- a arquitetura central deve permanecer coerente enquanto implementações variam.

Essas relações orientam a descoberta, mas não são automaticamente Core Capabilities.

## Hipóteses preservadas fora da Canon

Permanecem abertas e não promovidas:

- Permanent Responsibilities como camada formal;
- ontologia institucional;
- transições positivas de estado como objeto institucional;
- Architectural Evidence Registry específico da A2;
- ADM-001;
- Architecture Reviews como padrão definitivo de toda a GEA.

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

Essa hierarquia não autoriza antecipar decisões de implementação durante a descoberta.

## Governança

- o owner do GCCM é a Guivos Enterprise Architecture;
- cada candidata deve manter rastreabilidade até suas evidências;
- fusões, rejeições e promoções devem registrar justificativa;
- novas Core Capabilities não podem ser criadas diretamente por arquiteturas de domínio;
- arquiteturas de domínio reutilizam ou especializam o catálogo validado;
- mudanças estruturais no modelo exigem análise de impacto e governança correspondente;
- a Foundation produz evidências, não promoção automática de capacidades;
- execução e evolução do método permanecem separadas.

## Critério de conclusão da versão de descoberta

A fase de descoberta estará concluída quando:

1. o inventário mínimo de fontes prioritárias tiver sido analisado;
2. as evidências estiverem registradas e agrupadas;
3. todas as candidatas tiverem sido submetidas aos testes;
4. o conjunto remanescente demonstrar cobertura da missão;
5. sobreposições e lacunas estiverem explicitadas;
6. houver base suficiente para uma validação arquitetural formal.

## Próximos passos

1. analisar `GEB-P01-F06 — Princípios Permanentes`;
2. concluir a `Foundation Evidence Matrix`;
3. executar `A2-R01 — Foundation Architecture Review`;
4. avançar para o Modelo Fundamental do GEB;
5. manter o registro de candidatas vazio até convergência suficiente.