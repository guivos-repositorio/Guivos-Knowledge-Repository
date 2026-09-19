---
id: GKR-UX-HOMES-DESIGN-SOURCE-READINESS-REMEDIATION-001
title: Homes Públicas — Remediação de Prontidão Documental para Designer e IA
status: draft
version: 0.5.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: false
maturity: source_readiness_remediation_in_progress_person_oc_mall_travel_pass
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-HOME-MASTERS-REMEDIATION-001
---

# Homes Públicas — Remediação de Prontidão Documental para Designer e IA

## 1. Finalidade

Esta frente corrige o modelo operacional de entrega das oito Homes públicas antes do trabalho externo de Design.

O objetivo não é criar telas, protótipos, arquivos Figma, identidade visual ou direção artística dentro do GKR.

O objetivo é garantir que a designer — e, opcionalmente, sistemas de IA usados por ela — recebam documentação suficientemente completa, coerente, autocontida e governada para criar as Homes sem depender de reconstrução informal de contexto, conversa histórica ou decisões implícitas.

## 2. Decisão humana superior

```text
DESIGNER HUMANA
→ EXECUTORA CRIATIVA PRINCIPAL
→ CRIAÇÃO MANUAL LIVRE

GKR
→ FONTE DE SIGNIFICADO
→ FUNÇÃO
→ LIMITES
→ FATOS
→ ARQUITETURA
→ CONTEXTO
→ EVIDÊNCIA
→ DECISÕES GOVERNADAS

SISTEMAS DE IA
→ APOIO OPCIONAL
→ PODEM CONSUMIR O MESMO PACOTE GOVERNADO
→ NÃO SÃO PRÉ-REQUISITO
→ NÃO DEFINEM DIREÇÃO CRIATIVA

FIGMA MAKE
→ NÃO É ETAPA OBRIGATÓRIA
→ NÃO É PRÉ-CONDIÇÃO
→ NÃO É FLUXO CANÔNICO DO GKR

GKR / CHATGPT
→ NÃO PRODUZ ARQUIVOS DE DESIGN COMO ETAPA DE PRONTIDÃO
```

## 3. Liberdade criativa preservada

Não serão canonicamente definidos antes do trabalho da designer:

- tipografia;
- paleta;
- fotografia;
- vídeo;
- ilustração;
- iconografia;
- composição;
- grid;
- ritmo;
- respiro;
- motion;
- microinterações;
- aparência de componentes;
- linguagem gráfica;
- atmosfera;
- direção de arte;
- sistema visual;
- copy não congelada;
- forma física de agrupar movimentos narrativos.

A ausência dessas definições não é gap documental.

```text
GKR
→ SIGNIFICADO / FUNÇÃO / LIMITES / VERDADE

DESIGN
→ EXPRESSÃO VISUAL / CRIATIVA

LIBERDADE CRIATIVA
≠ REDEFINIÇÃO DE PRODUTO
≠ INVENÇÃO FACTUAL
```

## 4. Dois modos legítimos de consumo

### 4.1 Consumo humano — designer

A designer deve conseguir:

1. abrir o pacote da Home;
2. compreender rapidamente o propósito e papel da Home;
3. ler o Master como autoridade principal de significado;
4. distinguir decisões obrigatórias de campos criativos;
5. saber quais fatos podem ou não ser apresentados;
6. reconhecer perguntas abertas sem precisar inventar respostas;
7. criar manualmente sua própria direção visual;
8. consultar documentos complementares somente quando necessários;
9. submeter sua direção à revisão humana da Guivos.

### 4.2 Consumo por IA — opcional

Quando a designer decidir usar um sistema de IA, o mesmo pacote deve permitir:

1. Source Lock do contexto;
2. definição explícita da Home;
3. ordem de autoridade;
4. matriz de classes operacionais;
5. prompt tool-agnostic;
6. proibições de inferência;
7. autoauditoria do output;
8. identificação clara de hipótese, placeholder e conteúdo candidato.

Nenhuma IA recebe autoridade para preencher lacunas semânticas.

## 5. Taxonomia operacional preservada

As oito classes permanecem válidas:

1. `CANONICAL`;
2. `DESIGN_CREATIVE`;
3. `CONTENT_CANDIDATE`;
4. `DESIGN_HYPOTHESIS`;
5. `PROTOTYPE_PLACEHOLDER`;
6. `REAL_DATA_REQUIRED`;
7. `OPEN_QUESTION`;
8. `PROHIBITED_INFERENCE`.

A taxonomia serve tanto à designer humana quanto à IA opcional.

## 6. Findings materiais desta remediação

### DR-01 — Figma Make tratado como etapa obrigatória

Documentos comuns e os oito `LEIA-PRIMEIRO` do snapshot v5 descrevem Figma Make/prototipação como etapa operacional anterior à criação definitiva.

Classificação: `MATERIAL`.

Decisão: remover a obrigatoriedade tool-specific das autoridades correntes. IA passa a ser caminho opcional de apoio.

### DR-02 — contrato denominado como Figma/IA

A prontidão deve ser de **Design e consumo por IA**, não de uma ferramenta específica.

Classificação: `MATERIAL`.

Decisão: tornar o contrato tool-agnostic sem perder requisitos de qualidade, governança, acessibilidade, responsividade, assets e aceite.

### DR-03 — fluxo externo excessivamente prescritivo

O fluxo corrente estabelece:

```text
FIGMA MAKE
→ HUMAN REVIEW
→ FINAL FIGMA
```

Isso restringe indevidamente a forma de trabalho da designer.

Decisão:

```text
PACOTE GOVERNADO
→ COMPREENSÃO HUMANA
→ CRIAÇÃO LIVRE DA DESIGNER
→ IA OPCIONAL QUANDO E COMO A DESIGNER DECIDIR
→ REVISÃO HUMANA
→ ENTREGA FINAL
```

### DR-04 — snapshot v5 não deve ser reescrito

O snapshot v5 é evidência histórica congelada e reproduzível.

Decisão: não alterar v5. Mudanças materiais desta frente exigirão nova emissão depois de integração e validação das autoridades corrigidas.

### DR-05 — execução experimental de Figma não integra a baseline

A execução `GKR-UX-HOME-PERSON-DESIGN-EXEC-001` foi encerrada como `SUPERSEDED / NOT PLANNED`.

Qualquer arquivo experimental criado fora do GKR:

- não é autoridade;
- não é baseline visual;
- não é referência obrigatória;
- não limita a designer;
- não entra no novo pacote documental.

### DR-06 — prontidão deve ser demonstrada Home por Home

A afirmação de prontidão não pode depender apenas da existência de um Master.

Cada Home deve passar por auditoria explícita de suficiência para consumo externo.

## 7. Critério de prontidão documental — por Home

Cada Home somente poderá ser classificada como `SOURCE_READY` quando seu pacote permitir responder, sem inferência externa, pelo menos:

### A. Identidade e papel
- o que é esta Home;
- para quem ela existe;
- qual papel exerce no ecossistema;
- o que ela não é.

### B. Tese e percepção
- pergunta-mãe;
- tese narrativa;
- percepção desejada;
- primeiro comportamento desejado.

### C. Arquitetura
- movimentos narrativos vigentes;
- macroagrupamentos quando existirem;
- Header/navegação;
- Hero;
- CTAs;
- entradas/saídas;
- relação com outras Homes/produtos/participantes.

### D. Conteúdo
- classes de conteúdo;
- prova/evidência;
- conteúdo editorial;
- conteúdo comercial quando aplicável;
- placeholders;
- dados reais necessários;
- claims proibidos.

### E. Estados e condições
- estados públicos relevantes;
- disponibilidade;
- ausência/erro;
- campanha/patrocínio quando aplicável;
- personalização quando aplicável;
- autenticação/transição quando aplicável.

### F. Proteções
- autonomia;
- privacidade;
- causalidade;
- relevância;
- autoridade;
- transparência;
- distinção orgânico/pago/recomendado.

### G. Design freedom
- o que é livre;
- o que é hipótese;
- o que exige aprovação;
- o que não pode ser inferido.

### H. Responsividade, acessibilidade e robustez
- desktop/mobile;
- progressive disclosure quando aplicável;
- reduced motion;
- significado sem mídia rica;
- acessibilidade;
- performance;
- fallback.

### I. Dados e conteúdo ainda ausentes
- o que pode ser criado como placeholder;
- o que exige fonte real;
- o que deve permanecer ausente até decisão futura.

### J. Consumo por IA
- Source Lock;
- fontes exatas;
- precedência;
- prompt tool-agnostic;
- autoauditoria;
- output não canônico até aprovação humana.

## 8. Critério de fechamento global

A frente somente poderá declarar `100% SOURCE READY` quando:

```text
8 / 8 HOMES
→ SOURCE_READY

COMMON AUTHORITIES
→ TOOL-AGNOSTIC

MANUAL DESIGNER PATH
→ COMPLETE

OPTIONAL AI PATH
→ COMPLETE

MATERIAL DOCUMENT GAPS
→ 0

UNRESOLVED SEMANTIC CONFLICTS
→ 0

VISUAL IDENTITY PRE-IMPOSED
→ 0

UNSUPPORTED FACTS REQUIRED FOR DESIGN
→ 0

SOURCE PACKAGE
→ REPRODUCIBLE

NEW EXTERNAL SNAPSHOT
→ EMITTED ONLY AFTER REVIEW + HUMAN AUTHORIZATION
```

## 9. Ordem da remediação

1. corrigir autoridades comuns;
2. auditar Master + complementares da Home Pessoa;
3. auditar Organizações e Coletivos;
4. auditar Mall;
5. auditar Travel;
6. auditar Media;
7. auditar Ads;
8. auditar Business;
9. auditar Intelligence;
10. reconciliar findings cruzados;
11. validar navegação, IDs, versões e fontes;
12. emitir novo pacote somente após gate humano separado.

## 10. Progresso por Home

| Home | Estado | Finding material aberto |
|---|---|---:|
| Pessoa | **SOURCE_READY / PASS** | 0 |
| Organizações e Coletivos | **SOURCE_READY / PASS** | 0 |
| Mall | **SOURCE_READY / PASS** | 0 |
| Travel | **SOURCE_READY / PASS** | 0 |
| Media | UNDER_AUDIT | — |
| Ads | NOT_YET_AUDITED | — |
| Business | NOT_YET_AUDITED | — |
| Intelligence | NOT_YET_AUDITED | — |

Home Pessoa foi fechada após:
- reconciliação do Movimento 06 no contrato pós-Media;
- explicitação de condições/fallbacks;
- matriz operacional específica;
- brief mínimo para designer;
- contrato de uso opcional de IA;
- confirmação de zero gap semântico material.

Home Organizações e Coletivos foi fechada após:
- alinhamento dos rótulos pós-Media aos 11 movimentos canônicos;
- reconciliação dos limites procedimentais antigos;
- explicitação da bifurcação Organização/Coletivo e seus fallbacks;
- matriz operacional específica;
- brief mínimo para designer;
- contrato de uso opcional de IA;
- confirmação de zero gap semântico material.

Home Mall foi fechada após:
- confirmação contra GPA-002 v1.2.0;
- explicitação de Movimento 10 = Prova e Confiança com duas facetas;
- contratos de preço/pontos, disponibilidade, personalização, campanha e patrocínio;
- acessibilidade/mobile/fallback;
- matriz operacional e brief para designer/IA;
- confirmação de zero gap semântico material.

Home Travel foi fechada após:
- confirmação das nove frentes operacionais contra GPA-003 v1.3.0;
- separação entre serviço real e inventário/tarifa/disponibilidade específicos;
- contratos de destino, experiência, recomendação, patrocínio e pontos;
- acessibilidade/mobile/fallback;
- matriz operacional e brief para designer/IA;
- confirmação de zero gap semântico material.

## 11. Estado

```text
SOURCE READINESS REMEDIATION
→ IN_PROGRESS

V5 SNAPSHOT
→ FROZEN / HISTORICAL

FIGMA EXECUTION BY GKR
→ STOPPED

DESIGNER MANUAL CREATION
→ TARGET OPERATING MODEL

AI SUPPORT
→ OPTIONAL / TOOL-AGNOSTIC

NEW SNAPSHOT
→ NOT_STARTED
```
