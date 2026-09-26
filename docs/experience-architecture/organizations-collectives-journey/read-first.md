---
id: GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
title: Jornada de Organizações e Coletivos — Leia Primeiro
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: true
maturity: journey_consumption_authority
depends_on:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Jornada de Organizações e Coletivos — Leia Primeiro

## 1. Função

Este documento é a porta de entrada para a construção e o consumo da **Jornada de Organizações e Coletivos — Superfícies e Fluxos**.

A coleção reúne Organização e Coletivo na mesma arquitetura documental sempre que compartilham responsabilidade funcional, preservando diferenças reais de contexto, autoridade, governança, plano, interesse, estado e capacidade.

```text
ARQUITETURA COMPARTILHADA
≠ EXPERIÊNCIA IDÊNTICA

VARIAÇÃO CONTEXTUAL
≠ NOVA TELA POR PADRÃO

DIFERENÇA DE PARTICIPANTE
≠ DUPLICAÇÃO AUTOMÁTICA DE SUPERFÍCIE
```

## 2. Princípio de composição conjunta

Organização e Coletivo podem compartilhar uma mesma superfície ou Documento Mestre quando o job, a responsabilidade e a continuidade funcional forem equivalentes.

A experiência deve adaptar o que for legítimo ao participante ativo, incluindo quando aplicável:

- linguagem e contexto;
- autoridade e papel de quem atua;
- interesses e objetivos institucionais ou coletivos;
- estados e ações disponíveis;
- relações e vínculos;
- dados e evidências pertinentes;
- plano vigente e capacidades autorizadas;
- governança, proteção e prestação de contas.

Uma diferença visual, de conteúdo ou de nomenclatura não justifica por si só uma nova superfície.

Uma separação somente deve ser proposta quando existir responsabilidade funcional própria que não possa ser governada com clareza pela responsabilidade compartilhada.

## 3. Fonte de verdade

A construção deve consumir, em conjunto:

1. Jornada Integrada da Organização;
2. Jornada Integrada do Coletivo;
3. Atores, Autoridades e Jobs Prioritários;
4. Arquitetura da Informação autenticada;
5. Mapa de Superfícies autenticadas;
6. Mapa de Estados;
7. Fluxos Prioritários;
8. Surface Registry;
9. Transition Registry;
10. planos e demais autoridades específicas aplicáveis.

Nenhum documento isolado autoriza extrapolar os demais.

## 4. Ordem de consumo

```text
LEIA PRIMEIRO
→ JORNADAS INTEGRADAS
→ ATORES / AUTORIDADES / JOBS
→ ARQUITETURA DA INFORMAÇÃO
→ MAPA DE SUPERFÍCIES
→ MAPA DE ESTADOS
→ FLUXOS PRIORITÁRIOS
→ DOCUMENTO MESTRE DA SUPERFÍCIE, QUANDO EXISTENTE
→ PROTOTIPAÇÃO
```

A ordem organiza consumo. Ela não impõe sequência visual fixa à experiência.

## 5. Regra para futuras superfícies

A evolução desta coleção deve seguir a ordem:

```text
RESPONSABILIDADE EXISTENTE
→ ESTADO / CONTROLE CONTEXTUAL, SE SUFICIENTE
→ EXPANSÃO DA RESPONSABILIDADE, SE NECESSÁRIA
→ TRANSIÇÃO, SOMENTE QUANDO HOUVER MUDANÇA REAL DE RESPONSABILIDADE
→ NOVA SUPERFÍCIE, SOMENTE QUANDO HOUVER JOB + ESTADO + CONTINUIDADE PRÓPRIOS
```

Não criar nova superfície apenas porque Organização e Coletivo exibem conteúdo diferente, usam planos diferentes ou possuem nomenclatura distinta.

## 6. O que cada futuro Documento Mestre deve governar

Quando aplicável, cada Documento Mestre deve tornar explícitos:

- propósito e responsabilidade;
- participante e contexto aplicáveis;
- origens e destinos legítimos;
- job atendido;
- informações exibidas e capturadas;
- autoridade necessária;
- estados;
- ações e controles;
- diferenças adaptáveis entre Organização e Coletivo;
- processamento e feedback;
- vazio, indisponibilidade, erro e recuperação;
- retorno, pausa, recusa e interrupção;
- privacidade, proteção e minimização;
- handoffs e efeitos;
- acessibilidade;
- limites de IA;
- liberdade de Design;
- critérios de aceite;
- lacunas ainda não autorizadas.

## 7. Liberdade de Design

O GKR governa significado, responsabilidade, estados, autoridade, limites e continuidade. Não congela automaticamente composição visual, grid, hierarquia gráfica, componentes, imagens, motion ou solução responsiva.

A adaptação visual entre Organização e Coletivo é permitida quando preserva a mesma verdade funcional e torna o contexto mais compreensível.

## 8. IA e prototipação — source lock

IA utilizada para design ou prototipação opera em **source lock com o GKR**.

Se uma funcionalidade, ação, estado, transição, dado, permissão, plano, entitlement, automação, notificação, integração, persistência ou comportamento não possuir fundamento documental identificável:

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

Convenção de mercado, facilidade técnica, componente disponível ou sugestão do modelo não constituem autoridade de produto.

A IA pode explorar **como materializar** uma responsabilidade governada. Não pode decidir autonomamente **o que passa a existir**.

## 9. Limites desta coleção

Esta coleção não deve:

- transformar Organização em Pessoa;
- antropomorfizar Coletivo;
- confundir Organização com Guivos Business;
- conceder acesso automático a contexto pessoal individual;
- transportar autoridade entre Organização e Coletivo por semelhança;
- converter plano comercial em entitlement implementado por inferência;
- inventar métricas, scores, rankings ou recomendações universais;
- promover maturidade documental sem gate próprio;
- liberar Product Engineering por consequência da documentação.

## 10. Estado

```text
JORNADA DE ORGANIZAÇÕES E COLETIVOS — SUPERFÍCIES E FLUXOS
→ FUNDAÇÃO DOCUMENTAL CONJUNTA

ORGANIZAÇÃO / COLETIVO
→ ARQUITETURA COMPARTILHÁVEL
→ DIFERENÇAS ADAPTÁVEIS PRESERVADAS

DOCUMENTOS MESTRES DE SUPERFÍCIE
→ A EVOLUIR DE FORMA GOVERNADA

NOVOS IDs DE SUPERFÍCIE / TRANSIÇÃO
→ NONE BY THIS DOCUMENT

VISUAL BASELINE
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```
