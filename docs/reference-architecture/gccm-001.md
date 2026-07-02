---
id: GCCM-001
title: Guivos Core Capability Model
status: discovery
version: 0.4.0
owner: Guivos Enterprise Architecture
last_updated: 2026-07-02
layer: Reference Architecture
milestone: A2 — Functional Architecture Discovery
---

# GCCM-001 — Guivos Core Capability Model

## Estado

`Discovery`.

A Evidence Extraction foi concluída para as seis unidades da Foundation. Nenhuma Core Capability está candidata ou canônica nesta versão.

## Propósito

Definir, a partir de evidências existentes no GKR, as capacidades institucionais permanentes que explicam aquilo que a Guivos deve ser capaz de realizar em sua maturidade, independentemente de produtos, tecnologias, estruturas organizacionais ou implementações específicas.

## Pergunta arquitetural

> Quais capacidades institucionais permanentes são necessárias e suficientes para que a Guivos cumpra seu propósito em sua capacidade máxima?

## Definição de Core Capability

Uma Core Capability é uma capacidade institucional permanente, com propósito, responsabilidade e fronteiras próprias, indispensável à missão da Guivos e reutilizável por múltiplos produtos, serviços, experiências e arquiteturas de domínio.

Ela não é produto, funcionalidade, serviço isolado, tecnologia, componente de software, área organizacional, processo temporário ou nome comercial.

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

O conjunto final deve cobrir integralmente propósito, missão, modelo fundamental, geração de valor e operação madura da Guivos.

### Evidence recurrence

Nenhuma Core Capability pode ser promovida a partir de uma única unidade documental. Repetição, centralidade e consistência entre fontes devem preceder a formulação de candidatas.

### Hypothesis separation

Hipóteses podem orientar observação, mas não entram na Canon nem no catálogo de capacidades sem validação suficiente.

## Fontes prioritárias

1. Foundation Architecture;
2. Modelo Fundamental do GEB;
3. Product Architecture;
4. Business Architecture;
5. Research Domain e suas sínteses;
6. ADRs e validações arquiteturais;
7. princípios e modelos consolidados da GEA;
8. demais ativos relevantes, com status e limites explicitados.

## Método de descoberta estabilizado

O método permanece congelado durante a execução. Alterações metodológicas somente devem ocorrer diante de limitação concreta, inconsistência comprovada ou melhoria demonstrada pela aplicação.

```text
Documento
  -> Evidence Extraction
  -> Evidence Convergence
  -> Confidence Assessment
  -> Evidence Matrix
  -> Semantic Clustering
  -> Candidate Formulation
  -> Admission Tests
  -> Destruction and Irreducibility Tests
  -> Mission Coverage
  -> Architectural Validation
  -> Canonical Catalog
```

### Evidence Extraction

Extrair afirmações institucionais atômicas, significados, invariantes, responsabilidades, objetivos, estados desejados, decisões, relações e capacidades explícitas ou implícitas.

A decomposição em afirmações atômicas é técnica operacional, não camada canônica.

### Evidence Convergence

Comparar evidências entre fontes segundo frequência, centralidade, consistência, confirmação, ampliação, ausência, contradição e natureza funcional, constitucional, estrutural ou informacional.

Agrupamentos de evidência são instrumentos analíticos. Não constituem Core Capabilities.

### Confidence Assessment

Avaliar consistência, originalidade, relevância arquitetural e impacto na convergência.

### Evidence Matrix

Consolidar a presença, força, centralidade e consistência dos agrupamentos entre múltiplas fontes antes de formular candidatas.

### Semantic Clustering

Agrupar evidências equivalentes ou fortemente relacionadas, mantendo rastreabilidade até as fontes.

### Candidate Formulation

Converter apenas agrupamentos suficientemente distintos e recorrentes em candidatas provisórias.

### Admission Tests

Submeter cada candidata aos testes de permanência, essencialidade, propósito, fronteira, composição, independência, reutilização, irredutibilidade e rastreabilidade.

### Destruction and Irreducibility Tests

Tentar eliminar, fundir, reduzir ou reclassificar cada candidata.

### Mission Coverage

Avaliar se o conjunto remanescente cobre integralmente a Guivos sem redundâncias relevantes.

### Architectural Validation

Registrar divergências, lacunas, sobreposições e justificativas antes de qualquer promoção.

### Canonical Catalog

Promover somente capacidades suficientemente demonstradas, mediante governança arquitetural aplicável.

## Core Capability Admission Rule

Uma candidata somente poderá avançar quando atender simultaneamente:

1. permanência;
2. essencialidade;
3. propósito próprio;
4. fronteiras explícitas;
5. composição;
6. independência de produto;
7. independência tecnológica;
8. reutilização;
9. irredutibilidade;
10. rastreabilidade.

## Testes de destruição

Para cada candidata, responder:

1. a Guivos ainda cumpre sua missão sem esta capacidade?
2. outra candidata consegue absorvê-la integralmente?
3. trata-se apenas de produto, canal, serviço, feature ou tecnologia?
4. ela permanece válida em diferentes países, culturas e gerações tecnológicas?
5. possui decisões e responsabilidades próprias?
6. sua existência reduz ou aumenta desnecessariamente a complexidade do modelo?

## Foundation Evidence Progress — 6/6

| Fonte | Assertions | Meanings | Invariants | Responsibilities | Estado |
|---|---:|---:|---:|---:|---|
| F01 — Essência | 29 | 5 | 6 | 9 | Concluída |
| F02 — Propósito | 25 | 5 | 7 | 7 | Concluída |
| F03 — Missão Operacional | 19 | 5 | 5 | 6 | Concluída |
| F04 — Visão de Longo Prazo | 31 | 6 | 8 | 8 | Concluída |
| F05 — Constituição | 30 | 8 | 10 | 10 | Concluída |
| F06 — Princípios Permanentes | 39 | 14 | 14 | 14 | Concluída |

Totais brutos antes da deduplicação da `A2-R01`:

- 173 afirmações institucionais atômicas;
- 43 grupos de significado;
- 50 invariantes provisórios;
- 54 responsabilidades institucionais.

## Convergência provisória da Foundation

### Agrupamentos recorrentes

1. compreensão de contexto;
2. identificação de possibilidades relevantes;
3. conexão e fortalecimento do ecossistema;
4. apoio à progressão da jornada;
5. preservação da autonomia;
6. governança de aderência à jornada;
7. universalidade e inclusão contextual;
8. tecnologia subordinada ao propósito;
9. ecossistema irredutível a produtos;
10. coerência arquitetural sob variação;
11. conhecimento como patrimônio permanente;
12. simplicidade e suficiência arquitetural;
13. oportunidade subordinada à evolução.

### Agrupamentos adicionais observados

- espiritualidade não coercitiva;
- propósito traduzido em execução diária;
- IA e experiência orientadas pela missão;
- escalabilidade e internacionalização;
- extensibilidade para oportunidades futuras;
- IA como intérprete, não substituta do conhecimento;
- experiência vivida como realização de valor;
- relacionamentos como patrimônio do ecossistema;
- distinção entre dados e conhecimento;
- Canon orientada à maturidade institucional;
- visão superior às restrições temporárias;
- realização progressiva da arquitetura;
- governança proporcional à permanência.

Esses agrupamentos poderão ser fundidos, reclassificados, enfraquecidos ou rejeitados na `A2-R01`.

## Descobertas institucionais consolidadas

As seis fontes sustentam as seguintes relações:

```text
Evolução = finalidade
Oportunidade = meio
Experiência = realização de valor
Relacionamentos = patrimônio do ecossistema
Conhecimento = compreensão e patrimônio
IA = mecanismo de interpretação
Participante = titular da decisão
Arquitetura = estrutura permanente
Implementação = realização progressiva
```

Essas relações orientam a descoberta, mas não são automaticamente Core Capabilities.

## Hipóteses preservadas fora da Canon

- Permanent Responsibilities como camada formal;
- ontologia institucional;
- transições positivas de estado como objeto institucional;
- Architectural Evidence Registry específico da A2;
- ADM-001;
- Architecture Reviews como padrão definitivo de toda a GEA;
- Foundation como sequência formal de restrições permanentes;
- nova definição canônica de arquitetura.

## Registro de candidatas

| ID | Candidata | Evidências associadas | Estado | Resultado dos testes |
|---|---|---|---|---|
| — | — | — | — | Nenhuma candidata registrada |

## Catálogo canônico

Nenhuma Core Capability canônica nesta versão.

## Hierarquia posterior

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
- mudanças estruturais exigem análise de impacto;
- a Foundation produz evidências, não promoção automática de capacidades;
- execução e evolução do método permanecem separadas.

## Critério de conclusão da versão de descoberta

A descoberta estará concluída quando:

1. o inventário mínimo de fontes prioritárias tiver sido analisado;
2. as evidências estiverem registradas e agrupadas;
3. todas as candidatas tiverem sido submetidas aos testes;
4. o conjunto remanescente demonstrar cobertura da missão;
5. sobreposições e lacunas estiverem explicitadas;
6. houver base suficiente para validação arquitetural formal.

## Próximo passo

Executar `A2-R01 — Foundation Architecture Review`, concluir a Foundation Evidence Matrix, deduplicar invariantes e responsabilidades e decidir o readiness da Foundation antes de avançar para o Modelo Fundamental.