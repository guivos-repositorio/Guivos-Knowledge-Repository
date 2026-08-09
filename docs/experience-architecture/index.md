---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.99.0
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
| SVGs canônicos | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica de SVG existente | **0** |
| superfícies/estados/fronteiras | **57** |
| transições documentais | **66** |
| IDs com referência visual | **42 de 57** |
| responsabilidades sem SVG dedicado | **13** |
| fronteiras sem tela | **2** |

A UXA-100-A4 adiciona `PER-009` como responsabilidade sem SVG e seis handoffs de navegação de Planos, mantendo os 118 ativos visuais.

A D5-A reforma quatro SVGs já associados a `PER-004`, `PER-007` e `PER-008` para materializar Domínios de Evolução sem criar novo ativo visual, superfície ou transição.

A D5-B materializa o mesmo eixo em `ORG-002`, `PER-201`, `PER-202` e `PER-203`, reutilizando o cadastro institucional e reformulando Mapa, Lista e Detalhe in-place, também sem criar nova superfície ou transição.

A D5-C1 possui natureza diferente: adiciona **três responsabilidades sem SVG** (`PER-010..012`) e **seis handoffs contratados** (`TRN-008..013`). Por isso, as contagens granulares passam a 57/66, mas a baseline visual permanece 118 SVGs, 118 associações e 31 perfis.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional por padrão;
- responsabilidade contratada sem SVG não equivale a superfície materializada;
- transição contratada sem materialização suficiente não equivale a continuidade validada;
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
- `BND-002` representa contratação/dimensionamento assistido quando o autoatendimento não for suficiente e não pertence semanticamente a plano específico;
- estado intermediário não cria superfície própria quando preserva responsabilidade, autoridade e decisão principal;
- fronteira externa não é tela da Guivos;
- validação até uma fronteira não valida comportamento de terceiro;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- validação documental não equivale a implementação técnica;
- Domínio de Evolução organiza sobre o que a jornada trata e não representa diagnóstico, identidade, score, objetivo, Próximo Passo ou prova de evolução;
- domínio candidato deve permanecer visualmente distinto de domínio confirmado;
- ausência de domínio confirmado é estado legítimo e não bloqueia a jornada;
- um participante ou item pode se relacionar a mais de um domínio quando houver autoridade e finalidade adequadas;
- domínio da oportunidade ≠ domínio confirmado da Pessoa ≠ relevância contextual ≠ recomendação;
- Área da jornada, quando usada como filtro de Oportunidades, depende de ação explícita da Pessoa e não pode ser ativada silenciosamente por inferência;
- uma Organização pode declarar a área da oportunidade, mas não classificar a Pessoa nessa área;
- mesmo domínio entre oportunidade e jornada não cria match, recomendação, compartilhamento ou autorização automáticos;
- `PER-008 — Hoje` sintetiza e encaminha, mas não substitui Objetivos, Próximos Passos ou Evolução Contínua;
- Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança.

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
```

D4 e D5 são frentes não numeradas e não alteram a última frente funcional numerada: UXA-101 continua vigente e UXA-102/V5 permanece não iniciada.

### 5.1 Resultado da D5-A

[GKR-UX-D5-A-001 — Materialização Controlada dos Domínios de Evolução na Jornada Inicial](d5-a-evolution-domains-guided-expression-initial-understanding-today.md) consolida:

1. área da jornada candidata e revisável na síntese estruturada de `PER-004`;
2. reconciliação de `situação · impacto · prioridade · direção · contexto` como eixos de organização do relato, distintos dos Domínios de Evolução e das dimensões estruturais do Contexto Vivo;
3. apresentação separada da área candidata em `PER-007`;
4. gate próprio, sem pré-seleção, para confirmar, adicionar outra área, rejeitar ou manter em aberto;
5. preservação de `Ainda estou descobrindo` como estado e `Outra área` como mecanismo de extensibilidade;
6. domínio confirmado exibido somente como contexto discreto da continuidade em `PER-008`;
7. ausência de domínio confirmada como estado legítimo da experiência;
8. nenhuma nova superfície, transição ou família visual;
9. baseline visual de 118 SVGs preservada;
10. D5-B, D5-C, UXA-102/V5 e Engenharia de Produto mantidos fora do escopo daquela frente.

### 5.2 Resultado da D5-B

[GKR-UX-D5-B-001 — Materialização Controlada dos Domínios de Evolução na Camada de Oportunidades](d5-b-evolution-domains-opportunities-layer.md) consolida:

1. `0..n` Áreas relacionadas dentro da etapa existente `Jornada e contribuição` de `ORG-002`, sem criar 12ª etapa;
2. área declarada como metadado da oportunidade, nunca como classificação da Pessoa;
3. Área da jornada disponível como filtro explícito em `PER-201` e `PER-202`;
4. proibição de ativação silenciosa do filtro a partir de inferência ou perfil pessoal;
5. Mapa e Lista preservando a mesma consulta e a mesma semântica de área;
6. `PER-203` separando área/proveniência da oportunidade da explicação de relevância contextual;
7. domínio isolado declarado insuficiente para produzir recomendação;
8. proteção reforçada contra reconstrução de saúde, espiritualidade/religião, finanças ou outros contextos sensíveis por navegação;
9. nenhuma nova superfície, transição ou família visual;
10. D5-C, D6, D7, UXA-102/V5 e Engenharia de Produto mantidos fora do escopo daquela frente.

### 5.3 Resultado da D5-C1

[GKR-UX-D5-C1-001 — Contrato de Materialização das Superfícies de Direção, Movimento e Evolução](d5-c1-direction-movement-evolution-surface-contract.md) consolida:

1. reconciliação de `área ou dimensão contextual` em Objetivos, separando Área da jornada de dimensão estrutural do Contexto Vivo;
2. reconciliação de `área da vida` em Próximos Passos como expressão pública/legada compatível com Área da jornada/domain_link;
3. reconciliação de `dimensão` em Evolução Contínua em três conceitos distintos: Domínio de Evolução, dimensão estrutural do Contexto Vivo e aspecto descritivo da mudança;
4. `PER-010 — Meus Objetivos`;
5. `PER-011 — Meus Próximos Passos`;
6. `PER-012 — Minha Evolução`;
7. `TRN-008..013` como seis handoffs bidirecionais mínimos com `PER-008 — Hoje`;
8. todas as novas responsabilidades e transições no estado `contratado`;
9. nenhum handoff direto entre `PER-010`, `PER-011` e `PER-012` inventado nesta etapa;
10. nenhuma criação de SVG, perfil visual, implementação ou validação ponta a ponta;
11. baseline visual preservada em 118 SVGs / 118 associações / 31 perfis;
12. inventário granular atualizado para 57 superfícies/estados/fronteiras e 66 transições.

## 6. Resultado da UXA-100-A4

[UXA-100-A4 — Origens Administrativas e Handoffs de Entrada em Planos](uxa-100-a4-plans-entry-origin-and-navigation-handoffs.md) continua governando:

1. `PER-009 — Conta e configurações da Pessoa`, sem SVG dedicado;
2. `TRN-406/407` contratadas entre `PER-009` e `PER-301`;
3. `TRN-417/418` integralmente validadas entre `COL-002` e `COL-301`;
4. `TRN-427/428` integralmente validadas entre `ORG-001` e `ORG-301`;
5. navegação de `COL-002` reformulada in-place para explicitar Planos;
6. `ORG-001` reformulada in-place, removendo o rótulo obsoleto `Guivos Business` e explicitando Planos;
7. retorno explícito às origens em `COL-301` e `ORG-301`;
8. nenhuma alteração de maturidade em `TRN-401..405`, `TRN-411..416` ou `TRN-421..426`;
9. nenhuma implementação de cobrança, entitlement, `BND-002`, V5 ou Engenharia de Produto.

## 7. Resultado da UXA-101 preservado

[UXA-101 — Validação da Saída Consciente para Fronteira Externa](uxa-101-conscious-external-boundary-validation.md) continua encerrando V4 no limite controlável pela Guivos.

A frente consolida revisão pré-saída em `PER-203`, identificação do destino externo, minimização de dados/contexto, confirmação afirmativa, revalidação, bloqueio de redirecionamento inválido, retorno seguro e `TRN-205` validada até `BND-001`.

## 8. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.35.0 |
| Jornada da Pessoa | `draft` 0.18.0 |
| Jornada do Coletivo | `draft` 0.18.0 |
| Jornada da Organização | `draft` 0.11.0 |
| catálogo integrado | `active` 0.29.0 |
| galeria visual | `active`; 118 SVGs |
| galeria de Planos | `active` 0.5.0 |
| matriz por SVG | `active` 0.20.0; 118 associações / 31 perfis |
| lacunas | `active` 0.29.0 |
| registro de superfícies | `active` 0.20.0; 57 IDs |
| registro de transições | `active` 0.21.0; 66 transições |
| detalhamento da Pessoa | `active` 0.13.0 |
| detalhamento comercial/fronteira | `active` |
| D5-A — Domínios na jornada inicial | `active` 1.0.0 |
| D5-B — Domínios na camada de Oportunidades | `active` 1.0.0 |
| D5-C1 — contrato direção/movimento/evolução | `active` 1.0.0 |

## 9. Ressalvas vigentes

- 13 responsabilidades permanecem sem SVG dedicado, incluindo `PER-009..012`;
- `TRN-008..013` permanecem contratadas até materialização suficiente de `PER-010..012`;
- `TRN-406/407` permanecem contratadas até materialização suficiente de Conta;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais na integração patrocinada;
- `TRN-416/426` permanecem parciais;
- gateway, cobrança real, proration e processo de contratação/dimensionamento assistido após `BND-002` permanecem fora do escopo;
- processo externo após `BND-001` permanece sob autoridade de terceiro;
- Jornadas da Pessoa, Coletivo e Organização continuam `draft`;
- materializações visuais de `PER-010`, `PER-011` e `PER-012` permanecem não iniciadas e exigem autorização separada;
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
→ D5-C1 — responsabilidades e handoffs mínimos contratados sem SVG
→ V5 — pendente e não iniciada
```

D5-A, D5-B e D5-C1 não consomem nem antecipam V5.

## 11. Próxima evolução possível

A materialização visual de `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` ou `PER-012 — Minha Evolução` exige autorização separada por responsabilidade. D6, D7, materialização de `PER-009`, V5/UXA-102, cobrança real, contratação/dimensionamento assistido após `BND-002` e demais validações também permanecem separadas. Nenhuma delas é iniciada automaticamente por D5-C1.