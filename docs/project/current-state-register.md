---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 1.39.0
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
  - UXA-010
  - GEM-CLOSURE-REVIEW-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - ROADMAP-11.86.0
  - M7.19.4
normative: true
---

# Registro do Estado Atual (identificador GKR-STATE-001)

## 1. Autoridade

Este registro é a superfície oficial do estado global vigente do **Repositório de Conhecimento da Guivos (Guivos Knowledge Repository — GKR)** quando o incremento correspondente estiver integrado à branch principal.

## 2. Estado global proposto

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era de conhecimento | fase de estruturação do conhecimento da Guivos | GE-2 — Knowledge |
| Marco atual | primeira validação funcional da Tela Hoje registrada e aplicada | M7.19.4 |
| Remediação do repositório | concluída; validação mecânica aprovada | R1–R6 |
| Achados críticos, maiores ou menores conhecidos | nenhum aberto | 0 |
| Revisão da Arquitetura de Negócios | ativa, mas pausada antes da decisão sobre capacidade de reinvestimento responsável | A2-R03; BUS-CAND-010 |
| Resultados Empresariais (Business Outcomes) | 17 de 18 decisões humanas; nenhuma submissão aberta | BA-STR-002 |
| Capacidade de reinvestimento responsável | em validação; decisão e incorporação não antecipadas | BUS-CAND-010; `Under Validation` |
| Registro de Candidatos a Resultados | 10 em validação, 2 incorporados e 6 rejeitados | Candidate Outcome Register — COR 0.29.0 |
| Registro de Decisões sobre Candidatos a Resultados | 17 de 18 decisões humanas registradas | Candidate Outcome Decision Register — CODR 0.33.0 |
| Frente ativa | reformulação funcional da Tela Hoje | UXA-010 |
| Arquitetura da Experiência da Guivos | fundação integrada; Tela Hoje reformulada; dois wireframes aguardam validação | UXA-000 a UXA-010 |
| Tela Hoje | primeira validação funcional concluída e wireframe reformulado | UXA-006 0.3.0; UXA-010 |
| Detalhe de oportunidade | wireframe inicial aguardando validação funcional | UXA-007 |
| Cadastro pela Organização | wireframe inicial aguardando validação funcional | UXA-008 |
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

As autoridades ativas são:

1. **Arquitetura da Experiência da Guivos** (identificador UXA-000);
2. **Fundação da Arquitetura da Experiência** (identificador UXA-001);
3. **Experiência Diária e Tela Hoje** (identificador UXA-002);
4. **Mapa Inicial de Jornadas e Telas** (identificador UXA-003);
5. **Oportunidades, Organizações, Coletivos e Mapa** (identificador UXA-004);
6. **Programa Inicial de Wireframes de Baixa Fidelidade** (identificador UXA-005);
7. **Wireframe de Baixa Fidelidade da Tela Hoje** (identificador UXA-006);
8. **Wireframe de Baixa Fidelidade do Detalhe de Oportunidade** (identificador UXA-007);
9. **Wireframe de Baixa Fidelidade do Cadastro pela Organização** (identificador UXA-008);
10. **Padrão de Linguagem Clara e Identificadores Técnicos** (identificador UXA-009);
11. **Validação Funcional e Reformulação da Tela Hoje** (identificador UXA-010).

## 5. Resultado da primeira validação funcional

A Tela Hoje foi reformulada para aplicar:

- contexto de atuação explícito por meio de `Agindo como`;
- síntese do momento condicional;
- um único item principal de atenção;
- múltiplos itens críticos reunidos na Central de Intervenções;
- movimento atual antes das oportunidades;
- até dois cartões de oportunidade empilhados e em largura integral;
- Coletivos e atividades somente quando houver utilidade temporal;
- navegação Hoje, Jornada, Explorar, Mapa e Eu preservada.

A reformulação não transforma o wireframe em design final nem valida a experiência com participantes.

## 6. Wireframes em revisão

### 6.1 Tela Hoje

Wireframe móvel reformulado após decisão humana funcional. Os estados vazio, múltiplos itens críticos, modo discreto, baixa conectividade e contextos institucionais permanecem pendentes.

### 6.2 Detalhe de oportunidade

Wireframe móvel com identidade, preço, custo total, validade do preço, relevância, disponibilidade, elegibilidade, Organização responsável, transparência comercial e ações. A validação funcional ainda não foi realizada.

### 6.3 Cadastro pela Organização

Wireframe para web em computador com onze etapas, preço e condições, consistência, salvamento, pré-visualização e separação entre envio, avaliação, ativação e apresentação. A validação funcional ainda não foi realizada.

## 7. Padrão de linguagem clara

O nome completo deverá aparecer antes do identificador. Códigos permanecem para rastreabilidade, não como forma principal de comunicação.

Estados técnicos serão apresentados em português, com o termo canônico entre parênteses quando necessário.

## 8. Sequência oficial vigente

```text
Guivos Journey — concluído funcionalmente e publicado
→ Modelo Econômico da Guivos — arquitetura documental inicial concluída
→ remediação do repositório — concluída
→ decisões humanas sobre Resultados Empresariais — 17 de 18
→ pausa antes da capacidade de reinvestimento responsável
→ Arquitetura da Experiência — integrada
→ três wireframes iniciais — criados
→ padrão de linguagem clara — estabelecido
→ primeira validação funcional da Tela Hoje — concluída
→ Tela Hoje — reformulada em baixa fidelidade
→ validação do Detalhe de Oportunidade, do Cadastro pela Organização ou de estado alternativo
→ retorno aos Resultados Empresariais quando autorizado
```

## 9. Próximo ato autorizado

Decidir separadamente entre:

1. validar funcionalmente o Detalhe de Oportunidade;
2. validar funcionalmente o Cadastro de Oportunidade pela Organização;
3. selecionar um estado alternativo da Tela Hoje para novo wireframe.

Nenhum protótipo, teste ou desenvolvimento será iniciado automaticamente.

## 10. Limites

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