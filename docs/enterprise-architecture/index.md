---
id: GEA-000
title: Guivos Enterprise Architecture
status: consolidated
version: 1.10.0
owner: Guivos
last_updated: 2026-07-26
related_adrs:
  - ADR-003
  - ADR-004
  - ADR-005
  - ADR-006
related_validations:
  - AV-001
related:
  - GKR-STATE-001
  - GKR-AUD-002
  - GKR-REMEDIATION-002
  - BA-STR-002
  - BA-STR-002-CODR-001
  - COD-018
  - M7.20
---

# Guivos Enterprise Architecture

## Definição

A Guivos Enterprise Architecture (GEA) é o sistema de arquiteturas que organiza, conecta e governa a evolução da Guivos como ecossistema, empresa e plataforma de produtos.

A GEA não é uma arquitetura isolada. Ela integra todas as arquiteturas oficiais, preservando propriedade única, dependências explícitas e evolução governada.

O Guivos Knowledge Repository é a fonte oficial em que a GEA é documentada, versionada e publicada.

## Estado transversal

O estado global vigente não é mantido de forma independente nesta página. Ele é declarado pelo [GKR-STATE-001 — Registro do Estado Atual](../project/current-state-register.md).

No estado atual:

- Guivos Journey está publicado em `PAS-001 1.0.0`, com nove capacidades funcionalmente concluídas;
- Guivos Economic Model possui arquitetura documental inicial concluída em `GEM-001` a `GEM-010`;
- a remediação e a validação mecânica do repositório estão concluídas;
- `A2-R03 — Revisão da Arquitetura de Negócios` permanece como frente arquitetural ativa;
- a validação externa, a Matriz de Avaliação inicial e as 18 decisões humanas sobre Resultados estão concluídas;
- o registro possui 9 candidatos em validação, 3 fundidos e 6 rejeitados;
- `BUS-CAND-010` foi fundido em `BUS-CAND-005` por `COD-018`;
- nenhum Resultado canônico foi criado;
- a reaplicação dos testes, o AQS-O01 e as Capacidades Empresariais aguardam atos separados;
- Engenharia de Produto permanece pausada antes de `W0-01`.

## Missão

Projetar, preservar e evoluir uma arquitetura empresarial de classe mundial, baseada em fundamentos sólidos, conhecimento consolidado, validação por evidências e decisões estratégicas de longo prazo.

## Arquitetura de maturidade

A GEA representa a Guivos em sua capacidade institucional máxima. Ela não deve ser limitada pelo estágio atual da implementação.

> A Guivos é concebida em sua capacidade máxima. A implementação realiza progressivamente essa visão.

## Dois eixos de organização

A GEA classifica seus ativos por dois eixos complementares:

1. **Domínio arquitetural:** Fundação, Conhecimento, Ecossistema, Produto, Negócio, Dados e Inteligência, Economia, Tecnologia e Governança.
2. **Permanência:** Arquitetura Permanente, Arquitetura de Referência, Programas Empresariais e Entrega Empresarial.

O domínio define responsabilidade conceitual. A camada de permanência define horizonte, velocidade de mudança e rigor de governança.

Consulte o [GEA-PLM-001 — Modelo de Camadas de Permanência](permanence-layer-model.md).

## Modelo de camadas de permanência

```mermaid
graph TD
    PA[Arquitetura Permanente] --> RA[Arquitetura de Referência]
    RA --> EP[Programas Empresariais]
    EP --> ED[Entrega Empresarial]
    ED --> L[Resultados e Aprendizado]
    L --> R[Revisão formal quando necessária]
    R --> RA
```

| Camada | Horizonte | Pergunta principal |
|---|---|---|
| Arquitetura Permanente | décadas | O que continuará verdadeiro na maturidade da Guivos? |
| Arquitetura de Referência | anos | Qual é a melhor forma arquitetural conhecida de realizar a visão? |
| Programas Empresariais | meses e ciclos plurianuais | Quais programas transformarão a arquitetura em realidade? |
| Entrega Empresarial | dias, semanas e versões | O que será entregue agora e como será implementado? |

## Estrutura oficial

```mermaid
graph TD
    GEA[Guivos Enterprise Architecture]
    GEA --> FA[Foundation Architecture]
    GEA --> GKA[Guivos Knowledge Architecture]
    GEA --> EA[Ecosystem Architecture]
    GEA --> PA[Product Architecture]
    GEA --> BA[Business Architecture]
    GEA --> GIA[Guivos Intelligence Architecture]
    GEA --> EM[Guivos Economic Model]
    GEA --> TA[Technology and Engineering Architecture]
    GEA --> GA[Governance Architecture]
    EA --> GEB[Guivos Ecosystem Blueprint]
```

## Arquiteturas integrantes

| Arquitetura | Pergunta principal | Situação vigente |
|---|---|---|
| Foundation Architecture | Quem é a Guivos e por que ela existe? | congelada em `A2-B3` |
| Guivos Knowledge Architecture | Como a Guivos descobre, valida, consolida e evolui conhecimento institucional? | reconhecida por `ADR-006`; documentação interna pendente |
| Ecosystem Architecture | Como ocorre a transformação dos participantes? | em consolidação por meio do GEB |
| Product Architecture | Quais produtos materializam capacidades e propostas de valor? | estrutura superior consolidada; Journey publicado; portfólio especializado pendente de rebaseline |
| Business Architecture | Como a Guivos organiza transformação, Resultados, capacidades e execução do negócio? | `A2-R03` ativa; 18 decisões humanas concluídas; reavaliação e Canon pendentes |
| Guivos Intelligence Architecture | Como conhecimento, dados, contexto e conexões se tornam inteligência aplicada? | conceitos superiores consolidados; produto especializado ainda não rebaselineado |
| Guivos Economic Model | Como a Guivos sustenta economicamente o ecossistema sem contrariar seu propósito? | arquitetura documental inicial concluída; validação empírica e especializada pendente |
| Technology and Engineering Architecture | Como as capacidades são implementadas tecnicamente? | planejada e pausada antes de `W0-01` |
| Governance Architecture | Como decisões, riscos e mudanças são controlados? | ativa por métodos, auditorias, decisões e validação permanente do GKR |

## Relação entre GEA, GKR, GKA e GEB

- **GEA** é o conjunto integrado das arquiteturas da Guivos.
- **GKR** preserva a representação canônica, decisões, evidências e histórico.
- **GKA** governa como o conhecimento é descoberto, validado, promovido e evoluído.
- **GEB** é o blueprint principal da Ecosystem Architecture.
- **GKR-STATE-001** declara o estado transversal vigente sem redefinir as arquiteturas.

## Responsabilidade conceitual

Todo conceito, modelo, capacidade, ativo arquitetural ou decisão canônica deve possuir uma única arquitetura proprietária.

Arquiteturas consumidoras podem utilizar e referenciar esses ativos, mas não redefini-los.

A decisão de propriedade está registrada no [ADR-003 — Architectural Ownership](../adr/ADR-003-architectural-ownership.md).

## Princípios permanentes

### A arquitetura precede a implementação

Decisões estruturais devem ser definidas antes da implementação de software, processos ou produtos.

### O conhecimento precede a arquitetura

Arquiteturas permanentes devem derivar de conhecimento consolidado e rastreável.

### A realidade precede o conhecimento

Quando evidências consistentes demonstrarem inadequação, o conhecimento deverá ser revisado pelos processos formais da GKA.

### Uma decisão, uma fonte da verdade

Cada decisão arquitetural possui registro oficial. Resumos, roadmaps e painéis não criam decisões paralelas.

### Propriedade arquitetural única

Cada ativo canônico possui uma única arquitetura proprietária responsável por sua definição, evolução e governança.

### Separação entre arquiteturas

Negócio, produto, dados, inteligência, economia, tecnologia, governança e conhecimento são domínios relacionados, mas não intercambiáveis.

### Independência tecnológica

Conceitos e capacidades devem permanecer válidos mesmo quando linguagens, fornecedores, frameworks ou infraestrutura forem substituídos.

### Evolução controlada

Alterações estruturais devem ser registradas por governança formal e, quando necessário, por Architecture Decision Records.

### Estabilidade como ativo

A arquitetura deve evoluir por aumento de clareza, consistência e completude, evitando mudanças sem necessidade comprovada.

### Orientação à decisão

Todo ativo arquitetural deve declarar quais decisões orienta e quais não orienta.

### Evidência arquitetural

Nenhuma decisão estrutural deve ser tomada apenas por preferência.

### Realização progressiva

A Guivos é concebida em sua capacidade máxima e realizada progressivamente por programas, entregas e ciclos de implementação.

## Fluxo oficial de fundamentação

```text
realidade e evidências
→ conhecimento validado
→ arquitetura permanente e de referência
→ programas empresariais
→ entrega empresarial
→ resultados observados
→ aprendizado e revisão governada
```

Nenhuma camada posterior redefine silenciosamente a anterior.