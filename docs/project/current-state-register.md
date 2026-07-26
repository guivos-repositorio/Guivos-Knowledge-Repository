---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 1.38.0
owner: Repositório de Conhecimento da Guivos
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
  - UXA-009
  - GEM-CLOSURE-REVIEW-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - ROADMAP-11.85.0
  - M7.19.3
normative: true
---

# Registro do Estado Atual (identificador GKR-STATE-001)

## 1. Autoridade

Este registro é a superfície oficial do estado global vigente do **Repositório de Conhecimento da Guivos (Guivos Knowledge Repository — GKR)** quando o incremento correspondente estiver integrado à branch principal.

## 2. Estado global proposto

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era de conhecimento | fase de estruturação do conhecimento da Guivos | GE-2 — Knowledge |
| Marco atual | padrão de linguagem clara e identificadores técnicos estabelecido | M7.19.3 |
| Remediação do repositório | concluída; validação mecânica aprovada | R1–R6 |
| Achados críticos, maiores ou menores conhecidos | nenhum aberto | 0 |
| Revisão da Arquitetura de Negócios | ativa, mas pausada antes da decisão sobre capacidade de reinvestimento responsável | A2-R03; BUS-CAND-010 |
| Resultados Empresariais (Business Outcomes) | 17 de 18 decisões humanas; nenhuma submissão aberta | BA-STR-002 |
| Capacidade de reinvestimento responsável | em validação; decisão e incorporação não antecipadas | BUS-CAND-010; `Under Validation` |
| Registro de Candidatos a Resultados | 10 em validação, 2 incorporados e 6 rejeitados | Candidate Outcome Register — COR 0.29.0 |
| Registro de Decisões sobre Candidatos a Resultados | 17 de 18 decisões humanas registradas | Candidate Outcome Decision Register — CODR 0.33.0 |
| Frente ativa | linguagem clara aplicada à Arquitetura da Experiência e aos wireframes | UXA-009 |
| Arquitetura da Experiência da Guivos | fundação integrada; três wireframes iniciais em revisão | UXA-000 a UXA-009 |
| Protótipo navegável | não iniciado | — |
| Design visual | não iniciado | — |
| Testes de usabilidade | não iniciados | — |
| Resultados canônicos | nenhum criado | 0 códigos EO/BO |
| Capacidades Empresariais (Business Capabilities) | não iniciadas | — |
| Guivos Journey | especificação arquitetural ativa; nove capacidades concluídas | PAS-001 1.0.0 |
| Modelo Econômico da Guivos | arquitetura documental inicial concluída; validações reais pendentes | GEM-001 a GEM-010 |
| Engenharia de Produto (Product Engineering) | pausada antes da primeira unidade de trabalho; execução em 0% | W0-01 |
| Validação de Mercado | trilha paralela preservada; execução pendente | — |

## 3. Pausa governada dos Resultados Empresariais

A pausa antes da décima oitava decisão permanece vigente.

- **Capacidade de reinvestimento responsável** permanece em validação (candidato empresarial BUS-CAND-010);
- a décima oitava submissão de decisão não existe (identificador previsto BA-STR-002-COD-SUB-018);
- a décima oitava decisão não existe (identificador previsto COD-018);
- a recomendação de incorporação ao resultado de continuidade econômica não foi executada;
- a frente de Resultados Empresariais não foi concluída;
- nenhum Resultado foi promovido ou canonicalizado;
- a retomada dependerá de autorização explícita posterior.

## 4. Arquitetura da Experiência integrada

As autoridades iniciais são:

1. **Arquitetura da Experiência da Guivos** (identificador UXA-000);
2. **Fundação da Arquitetura da Experiência** (identificador UXA-001);
3. **Experiência Diária e Tela Hoje** (identificador UXA-002);
4. **Mapa Inicial de Jornadas e Telas** (identificador UXA-003);
5. **Oportunidades, Organizações, Coletivos e Mapa** (identificador UXA-004);
6. **Programa Inicial de Wireframes de Baixa Fidelidade** (identificador UXA-005);
7. **Wireframe de Baixa Fidelidade da Tela Hoje** (identificador UXA-006);
8. **Wireframe de Baixa Fidelidade do Detalhe de Oportunidade** (identificador UXA-007);
9. **Wireframe de Baixa Fidelidade do Cadastro pela Organização** (identificador UXA-008);
10. **Padrão de Linguagem Clara e Identificadores Técnicos** (identificador UXA-009).

## 5. Wireframes em revisão

### 5.1 Tela Hoje

Wireframe para aplicativo móvel com cabeçalho contextual, síntese do momento, atenção principal, Próximo Passo, oportunidades, Coletivos e navegação global.

### 5.2 Detalhe de oportunidade

Wireframe para aplicativo móvel com identidade, preço, custo total, validade do preço, relevância, disponibilidade, elegibilidade, Organização responsável, transparência comercial e ações.

### 5.3 Cadastro pela Organização

Wireframe para web em computador com onze etapas, preço e condições, consistência, salvamento, pré-visualização e separação entre envio, avaliação, ativação e apresentação.

## 6. Padrão de linguagem clara

O nome completo deverá aparecer antes do identificador. Códigos permanecem para rastreabilidade, não como forma principal de comunicação.

Estados técnicos serão apresentados em português, com o termo canônico entre parênteses quando necessário:

- Em validação (`Under Validation`);
- Incorporado (`Merged`);
- Rejeitado (`Rejected`).

A regra vale imediatamente para novos documentos, respostas, títulos, tabelas e apresentações da Arquitetura da Experiência. Snapshots históricos não serão reescritos apenas por motivo editorial.

## 7. Sequência oficial vigente

```text
Guivos Journey — concluído funcionalmente e publicado
→ Modelo Econômico da Guivos — arquitetura documental inicial concluída
→ remediação do repositório — concluída
→ decisões humanas sobre Resultados Empresariais — 17 de 18
→ pausa antes da capacidade de reinvestimento responsável
→ Arquitetura da Experiência — integrada
→ três wireframes iniciais — em revisão
→ linguagem clara e identificadores técnicos — estabelecidos
→ decisão futura sobre reformulação ou protótipo navegável
→ retorno aos Resultados Empresariais quando autorizado
```

## 8. Próximo ato autorizado

Revisar e decidir sobre:

1. hierarquia e conteúdo da Tela Hoje;
2. estrutura do Detalhe de Oportunidade;
3. sequência e densidade do Cadastro pela Organização;
4. clareza da validade do preço;
5. estados alternativos prioritários;
6. reformulação dos wireframes ou autorização posterior de protótipo navegável de baixa fidelidade.

Nenhum protótipo, teste ou desenvolvimento será iniciado automaticamente.

## 9. Limites

Este estado não autoriza:

- criar a décima oitava submissão ou decisão sobre Resultados Empresariais;
- incorporar a capacidade de reinvestimento responsável a outro resultado;
- concluir Resultados Empresariais;
- criar Resultados canônicos;
- iniciar Capacidades Empresariais;
- tratar os wireframes como design visual definitivo;
- criar protótipo navegável sem nova autorização;
- executar testes de usabilidade;
- definir preços e planos finais;
- iniciar Engenharia de Produto, ambientes, provas de conceito ou produção;
- tratar Validação de Mercado como já executada.
