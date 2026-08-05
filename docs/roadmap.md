---
id: ROADMAP-12.43.0
title: Roadmap Arquitetural — Solicitação Pendente Móvel Validada
status: active
version: 12.43.0
owner: Guivos
last_updated: 2026-08-04
supersedes_partial:
  - ROADMAP-12.42.0
related:
  - GKR-STATE-001
  - GPA-007
  - GEM-004-A1
  - GEM-007-A1
  - GEM-010-A2
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - UXA-065
  - UXA-066
  - UXA-067
  - UXA-068
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.69
---

# Roadmap Arquitetural — Solicitação Pendente Móvel Validada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Solicitação Pendente móvel validada | M7.69 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Descoberta móvel | 5 SVGs materializados e validados | UXA-060; UXA-061 |
| Perfil Público móvel | 4 SVGs materializados e validados | UXA-062; UXA-063 |
| Revisão e Solicitação | 5 SVGs materializados e validados | UXA-064; UXA-065 |
| Solicitação Pendente | 8 SVGs materializados e validados | UXA-066; UXA-067 |
| Opportunity Boost | 46 materializados; 36 validados; 10 pendentes | UXA-038 a UXA-055 |
| Resultados Empresariais | 18 decisões; zero canônicos | BA-STR-002-CODR-001 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência concluída dos Coletivos

```text
UXA-056 — descoberta, Perfil Público e participação contratados
→ UXA-057 — avaliação e reputação contratadas
→ UXA-058 — interação, recomendação e conexão contratadas
→ UXA-059 — programa de wireframes priorizado
→ UXA-060 — descoberta e busca materializadas
→ UXA-061 — descoberta e busca validadas
→ UXA-062 — Perfil Público materializado
→ UXA-063 — Perfil Público validado
→ UXA-064 — revisão e solicitação materializadas
→ UXA-065 — revisão e solicitação validadas
→ UXA-066 — Solicitação Pendente materializada
→ UXA-067 — Solicitação Pendente validada
```

## 4. Estado da espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | validada |
| 2 | Resultados de Busca | validada |
| 3 | Perfil Público do Coletivo | validado |
| 4 | Revisão e Solicitação de Participação | validada |
| 5 | Solicitação Pendente | validada |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Resultado da UXA-067

A validação consolidou:

- consulta sem alteração de fila;
- estimativa sem promessa;
- dado material sem edição silenciosa;
- autoridade protegida limitada ao processo;
- pedido adicional sem obrigação de revelar;
- resposta, preferência, contestação e cancelamento separados;
- descarte do rascunho sem cancelamento da solicitação;
- envio adicional com efeito compreensível;
- tratamento posterior sem garantia técnica ou jurídica absoluta;
- aprovação sem função, autoridade ou notificação automática;
- recusa sem sanção ou reputação;
- expiração sem recusa ou consentimento;
- denúncia separada de revisão formal;
- recomeço condicionado à disponibilidade vigente.

## 6. Gate concluído

O gate funcional da quinta referência P0A foi concluído.

Isso não inicia automaticamente `Meus Coletivos`, outra família de Coletivos ou implementação.

## 7. Lacuna transversal priorizada

A jornada pessoal possui escolha genérica entre texto, voz, arquivo e perguntas opcionais, mas ainda não possui uma superfície dedicada a orientar a expressão do Momento Atual.

A próxima iniciativa recomendada é:

> **UXA-068 — Expressão Guiada do Momento Atual por Texto e Voz**

O pacote deverá materializar:

- explicação do que a Guivos precisa compreender;
- situação, impacto, prioridade, direção e contexto;
- relato livre com orientação;
- voz com guia anterior à gravação;
- perguntas adaptativas para lacunas;
- síntese estruturada;
- correção e revisão antes da compreensão inicial.

## 8. Sequência prevista

```text
UXA-068 — materializar Expressão Guiada do Momento Atual
→ validação funcional da expressão guiada
→ pacote transversal do ambiente de simulação das jornadas
```

A ordem das famílias restantes de Coletivos deverá ser reavaliada após o tratamento dessa lacuna transversal, sem considerar `Meus Coletivos` automaticamente iniciado.

## 9. Ambiente de simulação das jornadas

A necessidade de visualizar as telas em sequência para Pessoa, Coletivo e Organização permanece registrada.

O ambiente deverá:

- reutilizar artefatos canônicos;
- ordenar jornadas por participante;
- mostrar estados materializados, validados, pendentes e não iniciados;
- revelar transições ausentes;
- alternar perspectivas relacionadas.

Essa iniciativa não está autorizada para implementação.

## 10. Frentes preservadas

Não são reabertas automaticamente:

- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante;
- gestão do responsável;
- validação dos 10 estados residuais do Opportunity Boost;
- Resultados Empresariais;
- preços ou baseline comercial;
- ambiente de simulação das jornadas;
- política jurídica;
- protótipo;
- testes com pessoas;
- Engenharia de Produto.

## 11. Regra de autorização

Integração da UXA-067 não inicia a UXA-068, `Meus Coletivos` ou o ambiente de simulação. Cada pacote exige autorização própria para criação e autorização separada para integração.
