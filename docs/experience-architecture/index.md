---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 1.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
related:
  - PAS-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GLPA-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - UXA-001
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-069
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-A-001
  - GKR-UX-D5-B-001
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.88
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos em experiências compreensíveis para Pessoas, Coletivos e Organizações. Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design final ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização
→ validação funcional
→ reformulação quando exigida
→ revalidação
→ promoção controlada quando aplicável
→ inspeção integrada
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura visual e granular

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **121** |
| associações individuais | **121** |
| perfis de rastreabilidade | **34** |
| com validação funcional vigente | **121** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **57** |
| transições documentais | **66** |
| IDs com referência visual | **45 de 57** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras sem tela | **2** |

A UXA-100-A4 adiciona `PER-009` como responsabilidade sem SVG e seis handoffs de navegação de Planos.

A D5-A reforma quatro SVGs de `PER-004`, `PER-007` e `PER-008` para materializar Domínios de Evolução sem criar novo ID.

A D5-B materializa o mesmo eixo em `ORG-002`, `PER-201`, `PER-202` e `PER-203`, também in-place.

A D5-C1 adiciona três responsabilidades (`PER-010..012`) e seis handoffs (`TRN-008..013`) no estado contratado. A D5-C2 adiciona três SVGs low-fidelity e três perfis. A D5-C3 reforma in-place e valida funcionalmente os três SVGs, elevando a cobertura visual de **118 para 121 validações vigentes** sem criar novo ativo, ID ou transição.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional;
- validação local de superfície não equivale a continuidade integrada;
- perfil de rastreabilidade não equivale por si só a aprovação da superfície;
- transição contratada não equivale a continuidade validada;
- uma versão visual reformulada exige validação correspondente;
- publicação ou ativação não equivale a distribuição garantida;
- plano pago não altera relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é ocultada para vender plano;
- navegar para Planos não equivale a escolher plano ou iniciar cobrança;
- Pessoa utiliza `Free · Plus · Pro`;
- Coletivo utiliza `Livre · Mobiliza · Impacta · Rede`;
- Organização utiliza `Conecta · Eleva · Transforma`;
- Guivos Business utiliza `Start · Growth · Scale · Enterprise` como Produto Especializado separado;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` representa contratação/dimensionamento assistido e não plano específico;
- fronteira externa não é tela da Guivos;
- validação até uma fronteira não valida comportamento de terceiro;
- Domínio de Evolução organiza sobre o que a jornada trata e não representa diagnóstico, identidade, score, Objetivo, Próximo Passo ou prova de evolução;
- domínio candidato permanece distinto de domínio confirmado;
- ausência de domínio confirmado é estado legítimo;
- multidomínio é legítimo quando houver autoridade e finalidade adequadas;
- domínio da oportunidade ≠ domínio confirmado da Pessoa ≠ relevância contextual ≠ recomendação;
- `PER-008 — Hoje` sintetiza e encaminha, mas não substitui Objetivos, Próximos Passos ou Evolução Contínua;
- Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança;
- `Minha Evolução` ≠ roda da vida obrigatória ≠ ranking ≠ diagnóstico ≠ percentual global da Pessoa.

## 5. Evolução recente

```text
UXA-097 — primeira Hoje e TRN-007
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos nas três jornadas e promoção canônica
→ UXA-101 — revisão consciente de saída e TRN-205 até BND-001
→ UXA-100-A4 — reconciliação das origens administrativas de Planos
→ D4 — propagação documental dos Domínios nas três jornadas
→ D5-A — Domínios em Expressão Guiada, Compreensão Inicial e Hoje
→ D5-B — Domínios na camada de Oportunidades
→ D5-C1 — contrato das superfícies de direção, movimento e evolução
→ D5-C2 — low-fidelity de Meus Objetivos, Meus Próximos Passos e Minha Evolução
→ D5-C3 — validação funcional e reformulação dos três SVGs
```

D4 e D5 são frentes não numeradas. UXA-101 continua a última frente funcional numerada e UXA-102/V5 permanece não iniciada.

### 5.1 D5-A

[GKR-UX-D5-A-001](d5-a-evolution-domains-guided-expression-initial-understanding-today.md) consolida Área da jornada candidata/revisável em Expressão Guiada e Compreensão Inicial e contexto discreto em Hoje, sem nova superfície ou transição.

### 5.2 D5-B

[GKR-UX-D5-B-001](d5-b-evolution-domains-opportunities-layer.md) consolida `0..n` Áreas relacionadas no cadastro institucional, filtro explícito em Mapa/Lista e separação entre área da oportunidade e relevância pessoal no Detalhe.

### 5.3 D5-C1

[GKR-UX-D5-C1-001](d5-c1-direction-movement-evolution-surface-contract.md) consolida:

1. reconciliação terminológica de Objetivos, Próximos Passos e Evolução;
2. `PER-010 — Meus Objetivos`;
3. `PER-011 — Meus Próximos Passos`;
4. `PER-012 — Minha Evolução`;
5. `TRN-008..013` como handoffs mínimos com Hoje;
6. nenhuma navegação direta inventada entre as três superfícies;
7. responsabilidades e transições inicialmente contratadas.

### 5.4 D5-C2

[GKR-UX-D5-C2-001](d5-c2-direction-movement-evolution-low-fidelity-wireframes.md) materializa um estado-base móvel para cada responsabilidade e cria três perfis de rastreabilidade (`R32..R34`). A frente eleva o inventário para 121 SVGs / 121 associações / 34 perfis, mantendo as três novas superfícies pendentes até validação posterior.

### 5.5 D5-C3

[GKR-UX-D5-C3-001](d5-c3-direction-movement-evolution-functional-validation.md) confronta os três SVGs com `PAS-001-OBJ-VIEW-001`, `PAS-001-PP-VIEW-001` e `PAS-001-EC-VIEW-001` e reforma somente insuficiências materiais:

- `PER-010`: estados funcionais claros, prioridade declarada separada de valor pessoal, progresso qualitativo e controles de privacidade;
- `PER-011`: estado `PRONTO`, prontidão/dependência explícitas, proposta distinta de decisão e ação coerente com o estado;
- `PER-012`: período, baseline, direção, interpretação explicitamente inferida, confiança, incerteza, contestação e revisão;
- os três SVGs passam a possuir validação funcional local vigente;
- `TRN-008..013` permanecem contratadas e fora da promoção desta frente.

## 6. Resultado da UXA-100-A4 preservado

[UXA-100-A4](uxa-100-a4-plans-entry-origin-and-navigation-handoffs.md) continua governando `PER-009`, `TRN-406/407`, `TRN-417/418` e `TRN-427/428`. `PER-009` permanece sem SVG; cobrança real, entitlement e processo posterior a `BND-002` continuam fora do escopo.

## 7. Resultado da UXA-101 preservado

[UXA-101](uxa-101-conscious-external-boundary-validation.md) continua encerrando V4 no limite controlável pela Guivos: revisão pré-saída em `PER-203`, destino externo, minimização de dados/contexto, confirmação afirmativa, revalidação, retorno seguro e `TRN-205` validada até `BND-001`.

## 8. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active`; D5-C3 sincronizada |
| Jornada da Pessoa | `draft`; PER-010..012 validados localmente |
| Jornada do Coletivo | `draft` |
| Jornada da Organização | `draft` |
| catálogo integrado | `active`; 121 SVGs / 121 validados |
| galeria visual | `active`; 121 SVGs / 0 pendentes |
| galeria da Pessoa | `active`; 23 SVGs |
| galeria de Planos | `active` 0.5.0 |
| matriz por SVG | `active`; 121 associações / 34 perfis |
| lacunas | `active`; handoffs D5-C permanecem separados |
| registro de superfícies | `active`; 57 IDs |
| registro de transições | `active`; 66 transições |
| detalhamento da Pessoa | `active`; PER-010..012 validados localmente |
| D5-A | `active` 1.0.0 |
| D5-B | `active` 1.0.0 |
| D5-C1 | `active` 1.0.0 |
| D5-C2 | `active` 1.0.0 |
| D5-C3 | `active` 1.0.0 |

## 9. Ressalvas vigentes

- 10 responsabilidades permanecem sem SVG dedicado, incluindo `PER-009`;
- `TRN-008..013` permanecem contratadas até validação ponta a ponta;
- `TRN-406/407` permanecem contratadas;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais na integração patrocinada;
- `TRN-416/426` permanecem parciais;
- gateway, cobrança real, proration e processo após `BND-002` permanecem fora do escopo;
- processo externo após `BND-001` permanece sob autoridade de terceiro;
- Jornadas da Pessoa, Coletivo e Organização continuam `draft`;
- D6 e D7 permanecem não iniciadas;
- V5/UXA-102 permanece não iniciada.

## 10. Fila global preservada

```text
V1 — encerrada pela UXA-097
→ V2 — encerrada pela UXA-098
→ V3 — encerrada pela UXA-099
→ Planos — identidade canônica encerrada pela UXA-100-A3
→ V4 — encerrada pela UXA-101 até BND-001
→ Planos — origem voluntária reconciliada pela UXA-100-A4
→ D5-A — Domínios na jornada inicial materializados in-place
→ D5-B — Domínios na camada de Oportunidades materializados sem nova superfície
→ D5-C1 — responsabilidades e handoffs mínimos contratados
→ D5-C2 — três superfícies materializadas em low-fidelity
→ D5-C3 — três superfícies reformuladas e validadas localmente
→ V5 — pendente e não iniciada
```

D5-A/B/C1/C2/C3 não consomem nem antecipam V5.

## 11. Próxima evolução possível

Após integração governada da D5-C3, uma frente posterior poderá examinar exclusivamente `TRN-008..013` e a continuidade `Hoje ↔ Objetivos/Próximos Passos/Evolução`. D6, D7, materialização de `PER-009`, V5/UXA-102, cobrança real e demais validações permanecem independentes. Nenhuma é iniciada automaticamente.