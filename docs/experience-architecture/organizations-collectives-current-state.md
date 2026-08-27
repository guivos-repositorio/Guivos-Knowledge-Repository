---
id: GKR-UX-ORGCOL-STATE-001
title: Organizações e Coletivos — Visão Geral e Estado Atual
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-26
normative: false
related:
  - UXA-014
  - UXA-019
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - RP-002-OCE-001
---

# Organizações e Coletivos — Visão Geral e Estado Atual

## 1. Finalidade

Este documento é a porta de entrada atual para o conhecimento sobre **Organizações e Coletivos** no Guivos Knowledge Repository.

Ele existe para impedir três confusões:

1. tratar Organizações e Coletivos apenas como telas ou contas de produto;
2. confundir conhecimento funcional já estabelecido com hipóteses de Research;
3. apresentar como vigente uma materialização de UX que ainda não foi oficialmente definida.

A regra de leitura é:

> **Organizações e Coletivos são participantes estruturais do ecossistema Guivos. Sua fundação, suas relações, suas jornadas, seu papel no supply e sua experiência de produto possuem níveis de maturidade diferentes e devem permanecer explicitamente separados.**

## 2. Estado executivo

| Dimensão | Estado atual | Autoridade / referência |
|---|---|---|
| definição de Organização | definida funcionalmente | `UXA-014` |
| definição de Coletivo | definida funcionalmente | `UXA-014` |
| distinção Organização × Coletivo | definida funcionalmente | `UXA-014` |
| relações Organização ↔ Coletivo | contrato funcional existente, não normativo | `UXA-019` |
| Jornada da Organização | documento integrado em `draft`; não equivale a UX final | `GKR-JOURNEY-ORGANIZATION-001` |
| Jornada do Coletivo | documento integrado em `draft`; não equivale a UX final | `GKR-JOURNEY-COLLECTIVE-001` |
| papel no supply | pesquisa consolidada pré-campo | `RP-002-OCE-001` |
| proposta de valor econômica e de rede | hipótese de Research, não Canon | `RP-002-OCE-001` |
| Home pública de Organizações e Coletivos | possui Documento Mestre próprio | `public-home-organizations-collectives-master-document.md` |
| wireframe da experiência autenticada da Organização | **não definido** | pendente |
| wireframe da experiência autenticada do Coletivo | **não definido** | pendente |
| validação de wireframe da Organização | **não realizada em objeto vigente** | pendente |
| validação de wireframe do Coletivo | **não realizada em objeto vigente** | pendente |
| UI / protótipo autenticado | não definido | pendente |
| Engenharia da experiência autenticada | não autorizada a partir de wireframe | pendente |

## 3. Organização

Uma **Organização** é uma entidade institucional que possui identidade, autoridade, responsabilidades, recursos, processos, representantes e capacidade de oferecer produtos, serviços, programas, benefícios, suporte, infraestrutura ou oportunidades.

Pode possuir natureza:

- empresarial;
- pública;
- educacional;
- social;
- comunitária;
- religiosa;
- cultural;
- profissional;
- filantrópica;
- híbrida.

Organização não é sinônimo de:

- cliente do Guivos Business;
- anunciante;
- parceiro comercial;
- página institucional;
- fornecedor admitido;
- oportunidade;
- autoridade sobre a Journey de uma Pessoa.

Uma Organização pode exercer um ou vários desses papéis, mas sua natureza institucional permanece distinta deles.

## 4. Coletivo

Um **Coletivo** é uma formação voluntária de pessoas reunidas por propósito, identidade, causa, interesse, território, prática, experiência ou objetivo compartilhado.

Pode existir:

- independentemente;
- apoiado por uma Organização;
- em relação com múltiplas Organizações;
- em colaboração com outros Coletivos.

Coletivo não é sinônimo de:

- grupo de mensagens;
- audiência;
- comunidade de seguidores;
- canal de marketing;
- propriedade de uma Organização;
- força de trabalho gratuita;
- conta comercial.

Sua autonomia, governança, participação voluntária, pausa, saída e contestação devem permanecer protegidas.

## 5. Diferença estrutural

```text
ORGANIZAÇÃO
→ identidade institucional
→ autoridade formal
→ recursos e processos
→ responsabilidades institucionais
→ capacidade de oferta e execução

COLETIVO
→ propósito compartilhado
→ formação voluntária
→ pertencimento
→ governança própria
→ ação e experiência coletiva
```

Uma Organização pode apoiar um Coletivo sem possuí-lo.

Um Coletivo pode colaborar com uma Organização sem representá-la institucionalmente fora do escopo acordado.

## 6. Relações entre Organizações e Coletivos

O contrato funcional atual está em [`UXA-019`](uxa-019-organization-collective-relationship-functional-contract.md).

Ele preserva, entre outros elementos:

- finalidade explícita;
- autoridade bilateral;
- compromissos verificáveis;
- recursos e condições econômicas transparentes;
- dados e privacidade;
- uso de marca;
- autonomia e influência;
- proteção e não retaliação;
- revisão, suspensão e encerramento.

Princípio central:

> **Apoio, financiamento, patrocínio ou infraestrutura não transferem automaticamente propósito, governança, pertencimento ou autoridade.**

## 7. Jornadas atuais

As Jornadas integradas permanecem documentadas em:

- [Jornada Integrada da Organização](../journeys/organization.md);
- [Jornada Integrada do Coletivo](../journeys/collective.md).

Ambos os documentos possuem estado `draft`.

Eles ajudam a mapear continuidade, estados e relações do ecossistema, mas **não devem ser interpretados como prova de que a arquitetura de telas autenticadas, wireframes ou UI já foi definida**.

Qualquer trecho desses documentos que derive maturidade de `UXA-015`, `UXA-016`, `UXA-017` ou `UXA-018` fica subordinado à reconciliação de estado registrada aqui: os wireframes autenticados de Organização e Coletivo ainda não foram oficialmente definidos.

## 8. Organizações e Coletivos no supply

A investigação `RP-002` ampliou a compreensão sobre Organizações e Coletivos como agentes do supply.

O aprofundamento está em [Organizações, Coletivos, Efeito de Rede e Modelo Econômico do Supply](../research/RP-002/organizations-collectives-and-economic-model.md).

### 8.1 Papéis possíveis de Organizações

Research observou papéis como:

- provider;
- enabler;
- employer;
- infrastructure provider;
- funder;
- partner;
- verifier;
- venue / host;
- executor;
- sponsor;
- aggregator;
- source.

Esses papéis pertencem à relação ou à oportunidade concreta; não substituem a identidade institucional da Organização.

### 8.2 Papéis possíveis de Coletivos

Research observou papéis como:

- provider;
- ambiente de experiência;
- enabler;
- source;
- destination;
- rede de reciprocidade;
- detector de necessidades;
- criador de supply;
- coordenador local;
- mobilizador de recursos.

Coletivos podem materializar ou habilitar possibilidades que mercados tradicionais não atendem adequadamente.

## 9. Modelo de valor — estado de Research

A hipótese atual para Organizações é:

> **A Guivos pode ajudar uma Organização a compreender para quais Pessoas, Momentos e Possibilidades aquilo que ela oferece realmente apresenta valor — e aprender com o que acontece depois da experiência.**

A hipótese atual para Coletivos é:

> **A Guivos pode ajudar Coletivos a encontrar Pessoas, capacidades e recursos compatíveis com seu propósito compartilhado, organizar participação e compreender contribuição sem reduzir valor a popularidade.**

Essas formulações são **Research**, não promessa comercial nem contrato canônico de produto.

## 10. Neutralidade econômica

Permanecem preservadas as seguintes separações:

```text
PAGAR ≠ SER RELEVANTE
PARCEIRO ≠ SER MAIS RELEVANTE
PLANO MAIOR ≠ TER MAIS EVIDÊNCIA
PATROCÍNIO ≠ AUTORIDADE SOBRE O COLETIVO
PUBLICAR MAIS ≠ CONTRIBUIR MAIS
```

A Guivos pode monetizar infraestrutura, operação, integração, escala, serviços, transações e Intelligence agregada sem vender relevância funcional, dignidade, autoridade ou força de evidência.

## 11. Presença pública

A Home pública de Organizações e Coletivos possui construção própria em [Documento Mestre da Home Pública de Organizações e Coletivos](public-home-organizations-collectives-master-document.md).

Essa Home pública não deve ser confundida com:

- ambiente autenticado da Organização;
- ambiente autenticado do Coletivo;
- dashboard;
- área administrativa;
- wireframe das jornadas internas.

## 12. Estado de UX

O estado vigente está detalhado em [Organizações e Coletivos — Estado de UX e Wireframes](organizations-collectives-ux-state.md).

Resumo:

> **Ainda não existe wireframe oficialmente definido para a experiência autenticada da Organização nem para a experiência autenticada do Coletivo.**

Materiais anteriores que afirmavam o contrário foram reclassificados como registros históricos superseded.

## 13. Mapa de conhecimento

| Tema | Documento principal |
|---|---|
| definição e fundamento | `UXA-014` |
| estado mestre | este documento |
| relações Organização ↔ Coletivo | `UXA-019` |
| Jornada da Organização | `journeys/organization.md` |
| Jornada do Coletivo | `journeys/collective.md` |
| Home pública | `public-home-organizations-collectives-master-document.md` |
| supply, rede e modelo econômico | `RP-002-OCE-001` |
| estado de UX e wireframes | `GKR-UX-ORGCOL-UX-STATE-001` |

## 14. Próxima sequência legítima para UX autenticada

Quando essa frente for retomada, a sequência correta é:

```text
fundamentos e papéis atuais
→ necessidades e jobs por participante
→ arquitetura da informação
→ mapa de superfícies e estados
→ fluxos prioritários
→ wireframe de baixa fidelidade
→ validação funcional
→ UI
→ protótipo
→ testes
→ handoff técnico
```

Nenhuma etapa posterior deve ser presumida antes da anterior estar materialmente definida.

## 15. Regra de autoridade desta reconciliação

Para o estado atual de Organizações e Coletivos:

> **este documento prevalece sobre afirmações de maturidade de wireframe presentes em registros históricos ou documentos `draft` que dependam de `UXA-015` a `UXA-018`.**

Isso não apaga o histórico; apenas impede que materializações prematuras sejam confundidas com decisão vigente.