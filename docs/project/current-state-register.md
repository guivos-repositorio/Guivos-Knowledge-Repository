---
id: GKR-STATE-001
title: Current State Register
status: active
version: 1.37.0
owner: Guivos Knowledge Repository
last_updated: 2026-07-26
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - UXA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - GEM-CLOSURE-REVIEW-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - ROADMAP-11.84.0
  - M7.19.2
normative: true
---

# GKR-STATE-001 — Current State Register

## 1. Autoridade

Este registro é a superfície oficial para o estado global vigente do Guivos Knowledge Repository quando o incremento correspondente estiver integrado à branch principal.

## 2. Estado global proposto por este incremento

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.19.2 — Initial Low-Fidelity Wireframes Drafted` |
| Remediação do GKR | concluída; R5 `PASS` e R6 concluído |
| Achados Critical, Major ou Minor conhecidos abertos | 0 |
| A2-R03 — Business Architecture Review | ativa, operacionalmente pausada antes de `BUS-CAND-010` |
| Business Outcomes | 17 de 18 decisões; nenhuma submissão aberta |
| `BUS-CAND-010` | `Under Validation`; decisão e fusão não antecipadas |
| COR | `0.29.0`; 10 `Under Validation`, 2 `Merged` e 6 `Rejected` |
| CODR | `0.33.0`; 17 de 18 decisões humanas |
| Frente ativa | `UXA-005 — Programa Inicial de Wireframes de Baixa Fidelidade` |
| Experience Architecture | fundação e arquitetura inicial integradas; wireframes em revisão |
| Wireframes de baixa fidelidade | 3 superfícies iniciais criadas |
| Protótipo navegável | não iniciado |
| Design visual | não iniciado |
| Testes de usabilidade | não iniciados |
| Outcomes canônicos | `0` |
| Business Capabilities | não iniciadas |
| Guivos Journey | `PAS-001 1.0.0 active`; nove capacidades concluídas |
| Guivos Economic Model | arquitetura documental inicial concluída; validações reais pendentes |
| Product Engineering | pausado antes do `W0-01`; execução em `0%` |
| Market Validation | trilha paralela preservada; formulário e planilha pendentes |

## 3. Pausa governada de Business Outcomes

A pausa determinada antes da décima oitava decisão permanece vigente.

Consequências preservadas:

- `BUS-CAND-010 — Capacidade de reinvestimento responsável` permanece `Under Validation`;
- `BA-STR-002-COD-SUB-018` não existe;
- `COD-018` não existe;
- a recomendação `Merge into BUS-CAND-005` não foi executada;
- a frente de Business Outcomes não foi concluída;
- nenhum Outcome foi promovido ou canonicalizado;
- a retomada dependerá de autorização explícita posterior.

## 4. Experience Architecture integrada

As autoridades iniciais permanecem:

- `UXA-000 — Arquitetura da Experiência da Guivos`;
- `UXA-001 — Fundação da Arquitetura da Experiência`;
- `UXA-002 — Experiência Diária e Tela Hoje`;
- `UXA-003 — Mapa Inicial de Jornadas e Telas`;
- `UXA-004 — Oportunidades, Organizações, Coletivos e Mapa`.

O incremento atual adiciona:

- `UXA-005 — Programa Inicial de Wireframes de Baixa Fidelidade`;
- `UXA-006 — Wireframe da Tela Hoje`;
- `UXA-007 — Wireframe do Detalhe de Oportunidade`;
- `UXA-008 — Wireframe do Cadastro de Oportunidade pela Organização`.

## 5. Wireframes iniciais

### 5.1 Tela Hoje

Wireframe móvel com:

- cabeçalho contextual;
- síntese do momento;
- atenção principal;
- movimento atual;
- oportunidades para considerar;
- Coletivos e atividades;
- navegação `Hoje, Jornada, Explorar, Mapa e Eu`.

### 5.2 Detalhe de oportunidade

Wireframe móvel com:

- identidade, preço e custo total;
- explicação de relevância;
- disponibilidade e condições;
- elegibilidade;
- Organização responsável;
- transparência comercial;
- ações de inscrição, salvamento e mapa.

### 5.3 Cadastro pela Organização

Wireframe desktop com:

- onze etapas de cadastro;
- etapa detalhada de preço e condições;
- painel de consistência e transparência;
- salvamento de rascunho;
- pré-visualização;
- separação entre envio, avaliação, ativação e apresentação.

## 6. Sequência oficial vigente

```text
Guivos Journey — concluído funcionalmente e publicado
→ Guivos Economic Model — arquitetura documental inicial concluída
→ remediação R1–R5 — PASS
→ R6 — retomada governada concluída
→ decisões humanas do BA-STR-002 — 17 de 18
→ pausa governada antes de BUS-CAND-010
→ Experience Architecture Discovery — integrada
→ três wireframes iniciais de baixa fidelidade — em revisão
→ decisão sobre reformulação ou protótipo navegável
→ retorno a BUS-CAND-010 quando autorizado
→ conclusão de Business Outcomes
→ Business Capabilities e fases posteriores
```

## 7. Próximo ato autorizado

Revisar e decidir sobre:

1. hierarquia e conteúdo da tela `Hoje`;
2. estrutura do detalhe de oportunidade;
3. sequência e densidade do cadastro organizacional;
4. estados alternativos prioritários;
5. reformulação dos wireframes ou autorização posterior de protótipo navegável de baixa fidelidade.

Nenhum protótipo, teste ou desenvolvimento será iniciado automaticamente.

## 8. Limites

O estado proposto não autoriza:

- criar `BA-STR-002-COD-SUB-018` ou `COD-018`;
- fundir `BUS-CAND-010` em `BUS-CAND-005`;
- concluir Business Outcomes;
- promover candidatos a `Approved`;
- criar códigos canônicos `EO-###` ou `BO-###`;
- iniciar AQS-O01 ou Business Capabilities;
- tratar os wireframes como design visual definitivo;
- criar protótipo navegável sem nova autorização;
- executar testes de usabilidade;
- definir preços e planos finais;
- iniciar Product Engineering, W0-01, POCs, ambientes ou produção;
- tratar Market Validation como já executada.
