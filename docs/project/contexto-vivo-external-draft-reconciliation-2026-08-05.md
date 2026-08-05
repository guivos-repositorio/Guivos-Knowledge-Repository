---
id: GKR-EXT-CV-RECON-001
title: Reconciliação do Rascunho Externo do Contexto Vivo
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-STATE-001
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
  - GKR-CLAIMS-TRACE-001
  - PAS-001-CV-CONTRACT-001
related:
  - PAS-001-CV-STATE-001
  - PAS-001-CV-UPDATE-001
  - PAS-001-CV-CONFLICT-001
  - PAS-001-CV-VIEW-001
  - PAS-001-CV-EVENT-001
  - PAS-001-CV-INTEGRATION-001
  - PAS-001-CV-KPI-001
normative: false
---

# Reconciliação do Rascunho Externo do Contexto Vivo

## 1. Finalidade

Este documento compara o rascunho conversacional externo que originou parte do desenho do Contexto Vivo com a autoridade integrada `PAS-001-CV-CONTRACT-001 1.0.0`.

A finalidade é determinar:

- quais ideias foram absorvidas;
- quais foram refinadas;
- quais permaneceram apenas como exemplos;
- quais não possuem autoridade;
- se existe conflito capaz de reabrir a Capacidade 02.

A reconciliação não altera o PAS-001, seus contratos ou suas extensões.

## 2. Natureza da fonte externa

O arquivo externo chamado `rascunho.pdf` é uma compilação de conversa e trabalho intermediário. Ele mistura:

- descoberta conceitual do Contexto Vivo;
- exemplos explicativos;
- sugestões de interface;
- avaliações pessoais;
- mensagens sobre erros e continuidade;
- instruções de atualização do GKR;
- versões antigas dos instrumentos VAL;
- alegações operacionais sobre GitHub.

Portanto, ele não é um artefato arquitetural estável e não deve ser importado integralmente.

**Classificação:** `historical_conversational_source`.

## 3. Propostas centrais do rascunho

O rascunho propôs:

1. Contexto Vivo não como supercadastro ou perfil;
2. contexto como conjunto de dimensões de compreensão;
3. oito dimensões:
   - Identidade;
   - Momento;
   - Direção;
   - Capacidades;
   - Restrições;
   - Preferências;
   - Relacionamentos;
   - Evolução;
4. ritmos diferentes de envelhecimento e revisão;
5. um evento capaz de afetar várias dimensões;
6. evolução independente das dimensões;
7. ausência de reconstrução total do contexto quando apenas parte muda;
8. impossibilidade de presumir mudança sem evidência;
9. apresentação ao participante como `Meu Contexto Hoje`, em vez de perfil estático;
10. afirmação de que a arquitetura modela como a Guivos compreende a pessoa ao longo do tempo.

## 4. Autoridade integrada comparada

`PAS-001-CV-CONTRACT-001 1.0.0` é a oitava extensão normativa da Capacidade 02 e substitui o estado anterior aplicável do PAS-001.

O contrato final declara explicitamente:

- organização nas oito dimensões;
- preservação individual de elementos contextuais;
- distinção entre declaração, observação, evidência e inferência;
- controle de origem, temporalidade, confiança e finalidade;
- atualização seletiva;
- envelhecimento sem falsidade automática;
- controle do participante;
- evolução independente das oito dimensões;
- elemento contextual como unidade mínima de atualização;
- contexto como representação revisável, não identidade definitiva.

## 5. Matriz de reconciliação

| Proposta externa | Tratamento no contrato integrado | Resultado |
|---|---|---|
| Contexto Vivo não é cadastro ou perfil | representa contexto, não identidade definitiva | absorvida e normatizada |
| Dimensões de compreensão | representação funcional por dimensões | absorvida |
| Oito dimensões nominais | mesmas oito dimensões no contrato | absorvida integralmente |
| Evolução independente | regra fundamental final | absorvida integralmente |
| Atualização parcial | elementos preservados e atualizados seletivamente | absorvida e refinada |
| Não presumir mudança | hipótese não pode virar fato; base suficiente exigida | absorvida e ampliada |
| Ritmos diferentes de envelhecimento | temporalidade, revisão, expiração e confiança por elemento | absorvida sem frequências fixas |
| Evento afeta múltiplas dimensões | eventos produzem candidaturas e efeitos avaliados individualmente | absorvida com fronteiras de decisão |
| Participante controla a compreensão | visualização, correção, contestação, limitação e revogação | absorvida e ampliada |
| `Meu Contexto Hoje` | não constitui regra normativa do contrato | candidata de linguagem de experiência |
| Frequências “pouco frequente”, “moderado”, “contínuo” | contrato evita calendário universal e avalia por elemento e finalidade | exemplo externo, não regra |
| “estrutura definitiva” | substituída por conclusão governada do contrato e auditoria | afirmação conversacional superada |
| “maior diferencial competitivo” | não pertence ao contrato funcional | claim promocional não absorvido |

## 6. Refinamentos produzidos pela arquitetura integrada

O contrato final amplia substancialmente o rascunho ao introduzir:

- finalidade explícita;
- proveniência;
- confiança;
- permissões;
- sensibilidade;
- conflitos e divergências;
- contestação;
- revogação;
- atualização compensatória;
- integração com capacidades consumidoras;
- cenários ideal, alternativo e limite;
- comportamento seguro diante de informação incompleta;
- explicabilidade;
- eventos funcionais;
- KPIs;
- critérios de conclusão;
- comportamentos proibidos;
- gatilhos formais de reabertura.

O rascunho foi uma fonte de descoberta. O contrato é a autoridade normativa resultante.

## 7. Elementos não absorvidos como autoridade

### 7.1 Nome de tela

`Meu Contexto Hoje` pode ser uma formulação útil para experiência, mas não é nome oficial de tela por força deste rascunho.

Qualquer adoção pertence à Arquitetura da Experiência e exige avaliação no incremento correspondente. Esta reconciliação não inicia UXA-071.

### 7.2 Frequências universais

As classificações de frequência apresentadas no rascunho são exemplos intuitivos. O contrato governa envelhecimento por elemento, finalidade, impacto, confiança e evidência.

Não serão criados prazos universais por dimensão a partir do rascunho.

### 7.3 Claims competitivos

Afirmações como “maior diferencial competitivo” não são evidências de mercado e não devem aparecer como conclusão institucional sem validação.

### 7.4 Exemplos pessoais

Promoção profissional, nascimento de filho e início de MBA são exemplos de raciocínio. Não constituem regras universais de atualização.

## 8. Análise de conflito

Não foi encontrado conflito material entre o núcleo conceitual do rascunho e o contrato final.

A autoridade integrada:

- confirma as oito dimensões;
- confirma evolução independente;
- confirma atualização seletiva;
- impede inferência sem base;
- adiciona governança e proteção superiores às do rascunho.

Os itens não absorvidos são de interface, exemplo ou comunicação, não contradições funcionais.

## 9. Decisão

```text
External source: rascunho.pdf
Source type: historical conversational source
Core concepts absorbed: yes
Normative authority: no
Direct import: no
Contract conflict: no
Capability reopening required: no
UXA reopening required: no
```

### Tratamento

- preservar o rascunho como antecedente histórico, quando necessário;
- não copiar o arquivo integralmente para a área normativa;
- usar `PAS-001-CV-CONTRACT-001` e suas sete extensões anteriores como autoridades;
- tratar propostas de linguagem e interface como candidatas separadas;
- rejeitar claims promocionais sem evidência;
- não reabrir a Capacidade 02.

## 10. Efeitos autorizados

- marcar SRC-011 como reconciliada;
- registrar que o princípio de evolução independente foi absorvido;
- registrar que as oito dimensões foram absorvidas;
- remover a pendência de comparação conceitual do P0;
- preservar o rascunho como fonte histórica não normativa.

## 11. Efeitos não autorizados

- alterar o contrato final;
- renomear telas;
- criar frequências automáticas de revisão;
- iniciar UXA-071;
- iniciar Product Engineering;
- promover claims de mercado;
- declarar o PDF como documento oficial.

## 12. Resultado

```text
Draft-to-contract reconciliation: complete
Core conceptual absorption: confirmed
Residual functional conflict: none
Historical source retention: optional
Current-state change: no
```
