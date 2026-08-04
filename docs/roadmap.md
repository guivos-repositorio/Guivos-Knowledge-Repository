---
id: ROADMAP-12.42.0
title: Roadmap Arquitetural — Solicitação Pendente Móvel Materializada
status: active
version: 12.42.0
owner: Guivos
last_updated: 2026-08-04
supersedes_partial:
  - ROADMAP-12.41.0
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
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.68
---

# Roadmap Arquitetural — Solicitação Pendente Móvel Materializada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Solicitação Pendente móvel materializada | M7.68 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Descoberta móvel | 5 SVGs materializados e validados | UXA-060; UXA-061 |
| Perfil Público móvel | 4 SVGs materializados e validados | UXA-062; UXA-063 |
| Revisão e Solicitação | 5 SVGs materializados e validados | UXA-064; UXA-065 |
| Solicitação Pendente | 8 SVGs materializados; validação pendente | UXA-066 |
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
```

## 4. Estado da espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | validada |
| 2 | Resultados de Busca | validada |
| 3 | Perfil Público do Coletivo | validado |
| 4 | Revisão e Solicitação de Participação | validada |
| 5 | Solicitação Pendente | materializada; validação pendente |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Resultado da UXA-066

A família contém oito estados:

1. aguardando decisão;
2. análise protegida;
3. informação adicional solicitada;
4. revisão da resposta adicional;
5. cancelamento pela Pessoa;
6. aprovação;
7. recusa;
8. expiração.

Foram materializados:

- acompanhamento contínuo separado do comprovante;
- estado, data, identificador e autoridade;
- prazo estimado sem garantia;
- dados enviados, protegidos e finalidade;
- espera distinta de ação necessária;
- pedido adicional com pergunta e autoridade;
- resposta revisável antes do envio;
- cancelamento separado de recusa;
- expiração separada de recusa;
- aprovação sem papel automático;
- recusa sem funcionar como reputação;
- análise protegida com exposição mínima.

## 6. Gate obrigatório

Antes de iniciar `Meus Coletivos`, deverá ser concluída:

> **UXA-067 — Validação Funcional e Reformulação da Solicitação Pendente Móvel em Coletivos**

O gate deverá examinar os oito SVGs como continuidade única entre envio, espera, ação necessária, decisão e encerramento.

## 7. Próxima sequência prevista

Após validação e nova autorização, a sequência poderá avançar para:

```text
UXA-067 — validar Solicitação Pendente
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
→ Visão Geral do Responsável
```

`Meus Coletivos` deverá organizar participações, acompanhamentos, solicitações, convites e pausas sem duplicar o conteúdo detalhado da Solicitação Pendente.

## 8. Gates preservados

Antes de avançar além da UXA-066, deverão ser demonstrados:

- estado e autoridade compreensíveis;
- prazo sem garantia indevida;
- dados adicionais proporcionais;
- cancelamento com consequência conhecida;
- recusa e expiração distinguíveis;
- informação adicional não coercitiva;
- proteção de grupos sensíveis;
- histórico sem exposição indevida;
- continuidade para `Meus Coletivos` sem vínculo implícito.

## 9. Ambiente de simulação das jornadas

A necessidade de visualizar as telas em sequência para Pessoa, Coletivo e Organização foi identificada como iniciativa transversal relevante.

Ela deverá ser tratada em pacote próprio para:

- reutilizar os artefatos canônicos existentes;
- ordenar jornadas por participante;
- mostrar estados materializados, validados, pendentes e não iniciados;
- revelar transições ausentes e dependências;
- permitir alternância entre perspectivas relacionadas.

Essa iniciativa não faz parte da UXA-066 e não está autorizada para implementação.

## 10. Frentes paralelas preservadas

Não são reabertas automaticamente:

- validação dos 10 estados residuais do Opportunity Boost;
- Resultados Empresariais;
- preços ou baseline comercial;
- ambiente de simulação das jornadas;
- política jurídica;
- protótipo;
- testes com pessoas;
- Engenharia de Produto.

## 11. Regra de autorização

Integração da UXA-066 não inicia a UXA-067, `Meus Coletivos` ou o ambiente de simulação. Cada pacote continuará exigindo autorização própria para criação e autorização separada para integração.
