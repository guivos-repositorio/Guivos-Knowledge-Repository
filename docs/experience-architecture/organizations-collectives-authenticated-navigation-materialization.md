---
id: GKR-UX-ORGCOL-AUTH-NAV-MAT-001
title: Organizações e Coletivos — Materialização da Navegação Autenticada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-18
normative: false
maturity: authenticated_navigation_materialization_canonical_pre_wireframes
depends_on:
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - UXA-014
  - UXA-019
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
---

# Organizações e Coletivos — Materialização da Navegação Autenticada

## 1. Finalidade

Este documento materializa documentalmente a **topologia, hierarquia e semântica de entrada, continuidade, retorno e troca de contexto** da navegação autenticada de Organizações e Coletivos.

A frente foi aberta após:

```text
GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
→ v1.0.0
→ ACTIVE
→ PASS / CANONICAL ELIGIBILITY ADJUDICATION
→ INTEGRATED INTO MAIN

HUMAN AUTHORIZATION
→ NAVIGATION MATERIALIZATION
→ GRANTED AFTER ELIGIBILITY INTEGRATION

MAIN BASELINE
→ 9aad3c60d6ddcc83037f82e0353996b7b3fed696
```

A materialização responde:

> **Como a pessoa autenticada encontra e percorre o trabalho legítimo de uma Organização ou de um Coletivo, preservando contexto, autoridade, objeto, estado, retorno e lacunas reais, sem transformar navegação em permissão, tela ou implementação?**

A candidata documental concluiu `DRAFT SUFFICIENCY = PASS`, Semantic #1130 `SUCCESS`, Mechanical #1367 `SUCCESS`, revisão read-only sem finding material e foi então promovida canonicamente por autorização humana explícita. A promoção torna esta topologia a autoridade corrente de Navigation Materialization; ela não libera wireframes.

Este documento **não é wireframe** e não define aparência final.

```text
NAVIGATION MATERIALIZATION
→ TOPOLOGY
→ HIERARCHY
→ REACHABILITY
→ ENTRY / RETURN SEMANTICS
→ CONTEXT REBINDING
→ DOCUMENTARY / FUNCTIONAL

NAVIGATION MATERIALIZATION
≠ FINAL MENU VISUAL
≠ LAYOUT
≠ FRAME
≠ COMPONENT
≠ URL / ROUTE
≠ RBAC TÉCNICO
≠ UI
≠ PROTOTYPE
≠ IMPLEMENTATION
```

## 2. Regra de autoridade e identidade

Esta materialização reutiliza exclusivamente as identidades já governadas.

Regras:

1. `GKR-JOURNEY-SURFACE-REGISTRY-001` continua autoridade de superfícies;
2. `GKR-JOURNEY-TRANSITION-REGISTRY-001` continua autoridade de transições e maturidades;
3. este documento **não cria `GKR-SURF-*`**;
4. este documento **não cria `GKR-TRN-*`**;
5. este documento **não promove maturidade de transição**;
6. caminho de navegação documental não equivale a transição de lifecycle;
7. agrupamento navegacional não cria nova superfície;
8. ausência de superfície dedicada continua ausência explícita;
9. `UXA-019` continua restrito a Organização ↔ Coletivo;
10. relações Organização ↔ Organização e Coletivo ↔ Coletivo não são inventadas.

```text
NAVIGATION PATH
≠ GKR-TRN

NAVIGATION NODE
≠ NEW GKR-SURF

DISCOVERABLE
≠ AUTHORIZED

AUTHORIZED
≠ EFFECT EXECUTED
```

## 3. Modelo topológico comum

A experiência autenticada O/C possui cinco camadas funcionais de navegação.

```text
L0 — CONTEXTO ATIVO E AUTORIDADE
↓
L1 — ENTRADA / SÍNTESE DO MOMENTO
↓
L2 — DOMÍNIOS PRINCIPAIS DE TRABALHO
↓
L3 — CAPACIDADES ESPECIALIZADAS / CONTEXTUAIS
↓
L4 — HANDOFFS, RETORNOS E FRONTEIRAS
```

### 3.1 L0 — Contexto ativo e autoridade

Antes de resolver qualquer destino, a navegação precisa saber:

- qual Pessoa está autenticada;
- em nome de qual participante ela atua;
- qual Organização ou Coletivo está ativo;
- qual unidade/contexto se aplica;
- qual papel está ativo;
- quais limites de autoridade existem.

L0 é uma **camada transversal**, não uma nova superfície.

Quando o participante possui mais de um contexto elegível, a experiência deve permitir recontextualização explícita. A forma visual dessa escolha fica para wireframing.

### 3.2 L1 — Entrada e síntese

Cada contexto possui um anchor principal conhecido:

```text
ORGANIZAÇÃO
→ GKR-SURF-ORG-001 — Visão Geral da Organização

COLETIVO
→ GKR-SURF-COL-002 — Visão Geral do Responsável / Início autenticado
```

Esses anchors sintetizam Momento, atenção material e Próximos Passos sem absorver as fontes de verdade dos demais domínios.

### 3.3 L2 — Domínios principais

L2 organiza o trabalho nuclear do contexto.

Um domínio pode ser:

- **destination-backed** — possui uma superfície principal conhecida;
- **state-resolved** — resolve para superfícies diferentes conforme objeto/estado;
- **contextual-only** — deve permanecer acessível como contexto, mas não possui superfície dedicada;
- **shared-surface** — reutiliza a mesma superfície em mais de uma responsabilidade sem duplicá-la.

### 3.4 L3 — Capacidades especializadas

Capacidades comerciais ou especializadas não estruturam o núcleo da navegação.

Incluem, conforme autoridade própria:

- Planos e Capacidade;
- Intelligence;
- Ads;
- Business;
- Journey;
- Mall;
- Travel;
- Media.

A existência de produto não cria item principal automático.

### 3.5 L4 — Handoffs, retornos e fronteiras

L4 trata:

- retorno ao contexto de origem;
- continuidade para outro objeto;
- interrupção;
- revalidação após mudança de contexto;
- fronteiras com outra perspectiva ou participante;
- fronteiras externas já registradas.

## 4. Regra canônica de recontextualização

Trocar Organização, Coletivo ou unidade aplicável é uma **mudança de contexto**, não uma autorização nova.

```text
CURRENT CONTEXT
↓
EXPLICIT CONTEXT CHANGE
↓
REVALIDATE:
- PARTICIPANT
- UNIT / SCOPE
- ROLE
- AUTHORITY
- PROTECTED DATA ACCESS
↓
CLEAR NON-PORTABLE TRANSIENT STATE
↓
LAND ON TARGET CONTEXT ANCHOR
```

Destino após recontextualização válida:

```text
TARGET = ORGANIZAÇÃO
→ GKR-SURF-ORG-001

TARGET = COLETIVO
→ GKR-SURF-COL-002
```

Essa regra não cria `GKR-TRN-*` porque representa rebinding do contexto de atuação, não lifecycle de objeto.

Não podem ser transportados silenciosamente entre contextos:

- filtros não universais;
- decisões pendentes;
- formulários incompletos;
- contraparte;
- dados protegidos;
- ação iniciada;
- autoridade;
- consentimento;
- seleção comercial;
- pressuposto de continuidade.

Se a autoridade do novo contexto não puder ser confirmada, a experiência não deve executar ação material nesse contexto.

## 5. Organização — topologia principal

A topologia documental da Organização é:

```text
CONTEXTO ORGANIZAÇÃO
│
├── VISÃO GERAL
│   └── GKR-SURF-ORG-001
│
├── OPORTUNIDADES E PROGRAMAS
│   ├── GKR-SURF-ORG-002 — cadastro / preparação
│   └── GKR-SURF-ORG-003 — aprovada / ativa
│
├── RELAÇÕES
│   ├── GKR-SURF-ORG-004 — proposta O↔C
│   ├── GKR-SURF-ORG-005 — avaliação / negociação O↔C
│   └── GKR-SURF-ORG-006 — ativa / revisão O↔C
│
├── RESPONSABILIDADES E EVIDÊNCIAS
│   └── GKR-SURF-ORG-007
│
├── ORGANIZAÇÃO E AUTORIDADE
│   └── CONTEXTUAL-ONLY / SEM SUPERFÍCIE EXCLUSIVA
│
└── PLANOS E CAPACIDADE
    └── ESPECIALIZADO / CONTEXTUAL
        └── GKR-SURF-ORG-301..304
```

A estrutura acima é hierarquia funcional, não composição visual de sidebar/header.

## 6. Organização — regras de entrada por domínio

### 6.1 Visão Geral

**Tipo:** destination-backed.

Entrada:

```text
ORGANIZAÇÃO ATIVA
→ GKR-SURF-ORG-001
```

Funções navegacionais:

- anchor do contexto;
- síntese de Momento;
- descoberta de atenção material;
- origem legítima de acessos contextuais;
- retorno neutro quando nenhuma continuidade mais específica prevalecer.

Não pode se transformar em dashboard total.

### 6.2 Oportunidades e Programas

**Tipo:** state-resolved.

Não existe superfície genérica dedicada de “hub de oportunidades” adicional às identidades existentes.

Resolução:

```text
INTENÇÃO = CRIAR / PREPARAR
→ GKR-SURF-ORG-002

OBJETO = APROVADO / ATIVO
→ GKR-SURF-ORG-003

OBJETO EM OUTRO ESTADO
→ RESOLVER PELA AUTORIDADE ESPECIALIZADA
→ NÃO INVENTAR NOVA SUPERFÍCIE
```

Transições existentes preservadas:

- `GKR-TRN-201` — `ORG-001 → ORG-002` — parcial;
- `GKR-TRN-202` — `ORG-002 → ORG-003` — localmente validada;
- `GKR-TRN-203` — `ORG-003 → PER-201` — integralmente validada no recorte próprio.

A navegação não promove nenhuma delas.

`TRN-203` representa continuidade de distribuição/descoberta, não item de navegação operacional da Organização.

### 6.3 Relações

**Tipo:** state-resolved.

Escopo desta materialização:

```text
ORGANIZAÇÃO ↔ COLETIVO
→ SUPORTADO POR UXA-019

ORGANIZAÇÃO ↔ ORGANIZAÇÃO
→ GAP EXPLÍCITO
→ NÃO MATERIALIZADO POR ANALOGIA
```

Resolução do mesmo objeto bilateral:

```text
PROPOSTA
→ GKR-SURF-ORG-004

AVALIAÇÃO / NEGOCIAÇÃO
→ GKR-SURF-ORG-005

ATIVA / REVISÃO
→ GKR-SURF-ORG-006
```

A mudança de estado do objeto não implica criar um novo item principal de navegação.

### 6.4 Responsabilidades e Evidências

**Tipo:** destination-backed.

Destino conhecido:

```text
GKR-SURF-ORG-007
→ resultados e evidências institucionais
```

A maturidade própria de `ORG-007` permanece inalterada. A inclusão topológica não certifica wireframe, implementação ou qualidade visual.

### 6.5 Organização e Autoridade

**Tipo:** contextual-only.

O Surface Map não possui `GKR-SURF-ORG-*` exclusivo para esse domínio.

Portanto:

- não é criado um “Perfil da Organização” novo;
- não é criado um hub administrativo;
- contexto, unidade, papel e autoridade permanecem expostos pela camada L0 e pela síntese de `ORG-001`;
- ações específicas de correção/autoridade só podem apontar para superfícies existentes quando houver autoridade própria;
- eventual superfície futura exige governança própria do Surface Registry.

### 6.6 Planos e Capacidade

**Tipo:** especializado/contextual.

Superfícies:

- `GKR-SURF-ORG-301`;
- `GKR-SURF-ORG-302`;
- `GKR-SURF-ORG-303`;
- `GKR-SURF-ORG-304`.

Entrada/retorno documentalmente estabilizados:

```text
GKR-SURF-ORG-001
↓ GKR-TRN-427
GKR-SURF-ORG-301
↓
FLUXO ESPECIALIZADO
↓ GKR-TRN-428
GKR-SURF-ORG-001
```

Regras:

- Planos não é eixo principal;
- abrir Planos não seleciona plano;
- retornar não cancela nem altera capacidade;
- acesso comercial não altera relevância;
- nenhum acesso direto adicional a `ORG-301` é tratado como transição estável sem autoridade própria.

## 7. Coletivo — topologia principal

A topologia documental do Coletivo é:

```text
CONTEXTO COLETIVO
│
├── INÍCIO
│   └── GKR-SURF-COL-002
│
├── ATIVIDADES E OPORTUNIDADES
│   └── GKR-SURF-COL-006
│
├── PARTICIPAÇÃO
│   ├── GKR-SURF-COL-003 — solicitações
│   ├── GKR-SURF-COL-004 — participantes e vínculos
│   └── GKR-SURF-COL-005 — comunicação oficial quando aplicável
│
├── GOVERNANÇA E PROTEÇÃO
│   ├── GKR-SURF-COL-005 — comunicação oficial
│   ├── GKR-SURF-COL-006 — decisões no recorte aplicável
│   └── GKR-SURF-COL-007 — proteção e moderação
│
├── RELAÇÕES
│   └── GKR-SURF-COL-008 — Organização↔Coletivo
│
├── APRENDIZADOS E EVIDÊNCIAS
│   └── CONTEXTUAL-ONLY / SEM SUPERFÍCIE EXCLUSIVA
│
├── COLETIVO E AUTORIDADE
│   └── CONTEXTUAL-ONLY / GKR-SURF-COL-002 PARCIALMENTE
│
└── PLANOS E CAPACIDADE
    └── ESPECIALIZADO / CONTEXTUAL
        └── GKR-SURF-COL-301..304
```

A reutilização de `COL-005` e `COL-006` em mais de um domínio não duplica superfícies.

## 8. Coletivo — regras de entrada por domínio

### 8.1 Início

**Tipo:** destination-backed.

```text
COLETIVO ATIVO
→ GKR-SURF-COL-002
```

Funções:

- anchor do contexto;
- propósito e governança resumidos;
- Momento coletivo;
- atenção material;
- Próximos Passos compatíveis com autoridade.

`COL-001` continua presença/entrada pública separada e não é absorvido pela navegação autenticada principal.

### 8.2 Atividades e Oportunidades

**Tipo:** destination-backed / shared-surface.

Destino:

```text
GKR-SURF-COL-006
→ atividades, consultas e decisões
```

A mesma superfície também participa do domínio de governança quando o objeto é uma decisão. Isso não cria duplicata.

### 8.3 Participação

**Tipo:** state-resolved.

Resolução:

```text
SOLICITAÇÕES
→ GKR-SURF-COL-003

PARTICIPANTES / VÍNCULOS
→ GKR-SURF-COL-004

COMUNICAÇÃO OFICIAL RELACIONADA À PARTICIPAÇÃO
→ GKR-SURF-COL-005
```

Transições preservadas:

- `GKR-TRN-105..109`;
- `GKR-TRN-112`;
- `COL-003 → COL-004` continua continuidade lógica sem ID estável;
- `GKR-TRN-113` continua contratada no recorte `COL-004 → COL-005`.

A navegação não transforma a continuidade lógica `COL-003 → COL-004` em `GKR-TRN-*`.

### 8.4 Governança e Proteção

**Tipo:** state-resolved / shared-surface.

```text
COMUNICAÇÃO OFICIAL
→ GKR-SURF-COL-005

DECISÃO / CONSULTA NO RECORTE APLICÁVEL
→ GKR-SURF-COL-006

PROTEÇÃO / MODERAÇÃO
→ GKR-SURF-COL-007
```

A posse de acesso técnico não substitui regra de governança.

### 8.5 Relações

**Tipo:** destination-backed no escopo conhecido.

```text
COLETIVO ↔ ORGANIZAÇÃO
→ GKR-SURF-COL-008
→ UXA-019

COLETIVO ↔ COLETIVO
→ GAP EXPLÍCITO
→ NÃO MATERIALIZADO POR ANALOGIA
```

`COL-008` não é expandido semanticamente para Coletivo↔Coletivo.

### 8.6 Aprendizados e Evidências

**Tipo:** contextual-only.

Não existe `GKR-SURF-COL-*` exclusivo.

Logo:

- não é criado hub de Aprendizados;
- evidência permanece associada ao objeto de origem;
- Início pode sintetizar atenção sem duplicar fonte de verdade;
- navegação pode retornar ao objeto que sustenta o aprendizado/evidência;
- eventual superfície futura exige governança própria.

### 8.7 Coletivo e Autoridade

**Tipo:** contextual-only / partially anchored.

`GKR-SURF-COL-002` contém parte do contexto necessário, mas não é reclassificado como superfície exclusiva de autoridade.

Portanto:

- contexto, papel e regra de governança pertencem a L0 + Início;
- nenhuma nova superfície administrativa é criada;
- mudança de papel/autoridade não é inferida de navegação.

### 8.8 Planos e Capacidade

**Tipo:** especializado/contextual.

Superfícies:

- `GKR-SURF-COL-301`;
- `GKR-SURF-COL-302`;
- `GKR-SURF-COL-303`;
- `GKR-SURF-COL-304`.

Entrada/retorno estabilizados:

```text
GKR-SURF-COL-002
↓ GKR-TRN-417
GKR-SURF-COL-301
↓
FLUXO ESPECIALIZADO
↓ GKR-TRN-418
GKR-SURF-COL-002
```

Planos continua fora do eixo principal de relevância, propósito e governança.

## 9. Navegação derivada de Momento, Atenção e Próximo Passo

A Visão Geral/Início pode apresentar acessos contextuais derivados do Momento.

Esses acessos obedecem:

```text
ATTENTION / NEXT STEP
→ IDENTIFY SOURCE OBJECT
→ PRESERVE ACTIVE CONTEXT
→ REVALIDATE AUTHORITY
→ OPEN EXISTING RESPONSIBLE SURFACE
```

Não obedecem:

```text
ATTENTION
→ INVENT NEW DESTINATION

NEXT STEP
→ CREATE AUTHORITY

CLICK
→ CONFIRM DECISION
```

Um acesso contextual pode apontar para uma superfície existente mesmo sem `GKR-TRN-*` dedicado, desde que seja somente **navegação para compreensão/trabalho** e não seja tratado como evidência de transição de lifecycle.

Se a continuidade material exige transição estável, a ausência no Transition Registry permanece lacuna explícita.

## 10. Navegação por objeto e estado

Quando um domínio possui múltiplas superfícies, a navegação deve resolver o destino pelo objeto e pelo estado, não pela vontade de preencher um menu.

Regra:

```text
DOMAIN INTENT
+
CANONICAL OBJECT
+
CURRENT STATE
+
ACTOR / AUTHORITY
→ RESOLVED EXISTING SURFACE
```

Exemplos:

```text
ORGANIZAÇÃO / RELAÇÃO O↔C / PROPOSTA
→ ORG-004

ORGANIZAÇÃO / RELAÇÃO O↔C / NEGOCIAÇÃO
→ ORG-005

ORGANIZAÇÃO / RELAÇÃO O↔C / ATIVA
→ ORG-006

COLETIVO / PARTICIPAÇÃO / SOLICITAÇÃO
→ COL-003

COLETIVO / PARTICIPAÇÃO / VÍNCULO
→ COL-004

COLETIVO / PROTEÇÃO
→ COL-007
```

## 11. Bilateralidade Organização ↔ Coletivo

A relação bilateral possui duas perspectivas legítimas sobre um mesmo escopo governado.

```text
ORGANIZAÇÃO
→ ORG-004 / ORG-005 / ORG-006

COLETIVO
→ COL-008
```

Transições existentes:

- `GKR-TRN-206`;
- `GKR-TRN-207`;
- `GKR-TRN-208`;
- `GKR-TRN-209`.

Maturidade: contratadas.

A navegação:

- não promove essas transições;
- não permite “atuar como contraparte”;
- não troca contexto automaticamente;
- não torna o Coletivo recurso interno da Organização;
- não torna a Organização autoridade sobre o governo do Coletivo;
- preserva o mesmo escopo bilateral aprovado.

## 12. Discoverability, visibility e autoridade

A navegação distingue quatro perguntas:

1. o domínio existe para este contexto?
2. o ator pode compreender que ele existe?
3. o ator pode acessar o objeto?
4. o ator pode executar a ação?

Essas respostas podem ser diferentes.

```text
DOMAIN EXISTS
≠ OBJECT ACCESS

OBJECT ACCESS
≠ ACTION AUTHORITY

ACTION AUTHORITY
≠ APPROVAL COMPLETE
```

A forma visual de mostrar indisponibilidade, bloqueio ou ausência de autoridade é decisão posterior de wireframe/UI.

## 13. Estados alternativos da navegação

A topologia deve suportar, sem inventar destinos:

### 13.1 Autoridade insuficiente

A pessoa pode compreender o contexto permitido, mas a ação material fica bloqueada.

### 13.2 Aprovação adicional necessária

O objeto permanece no domínio responsável e indica dependência de outra autoridade.

### 13.3 Responsável ausente

A navegação não elege automaticamente novo responsável.

### 13.4 Informação incompleta

A pessoa permanece no objeto/fonte de verdade aplicável; ausência não é preenchida por inferência.

### 13.5 Proteção requerida

Conteúdo protegido não é exposto por estar em um domínio navegável.

### 13.6 Contestação

O objeto permanece acessível conforme autoridade, preservando a existência da contestação.

### 13.7 Indisponibilidade

Falha ou indisponibilidade não é convertida em estado de negócio.

### 13.8 Contexto expirado

O contexto deve ser revalidado antes de ação; navegação anterior não perpetua autoridade.

## 14. Regra de retorno

Retorno é semântica de continuidade, não comando de mutação.

```text
RETURN
→ PRESERVE CANONICAL OBJECT STATE
→ RECONSULT WHEN NECESSARY
→ RESTORE LEGITIMATE CONTEXT
→ NO SILENT COMMIT
```

Regras:

- voltar não confirma;
- voltar não cancela;
- voltar não desfaz automaticamente;
- retornar ao anchor não resolve pendência por inferência;
- retorno após mudança de contexto exige revalidação;
- retorno de capacidade especializada segue sua autoridade própria;
- retry não duplica efeito.

## 15. Busca, filtros e notificações

Busca, filtro, notificação e atenção são **mecanismos de acesso**, não domínios autônomos.

Devem sempre preservar:

- contexto ativo;
- escopo de autoridade;
- objeto canônico;
- fonte de verdade;
- proteção;
- retorno.

```text
SEARCH RESULT
→ EXISTING OBJECT / SURFACE

NOTIFICATION
→ EXISTING OBJECT / SURFACE

FILTER
→ VIEW STATE

NONE OF THE ABOVE
→ NEW DOMAIN
```

## 16. Produtos especializados e capacidades transversais

Produtos especializados podem receber handoff somente quando houver justificativa contextual e autoridade própria.

### 16.1 Planos

Materializado documentalmente pelos fluxos especializados já governados.

### 16.2 Intelligence

Pode apoiar compreensão dentro do contexto autorizado, mas não vira autoridade decisória nem eixo principal da navegação O/C.

### 16.3 Ads

Não recebe posição principal por capacidade comercial. Patrocínio não altera relevância orgânica.

### 16.4 Business

Permanece produto especializado; não substitui a experiência institucional da Organização.

### 16.5 Journey

Não permite a Organização ou o Coletivo acessar automaticamente contexto pessoal protegido.

### 16.6 Mall, Travel e Media

Podem existir como handoffs contextuais quando houver contrato funcional próprio; não são promovidos por esta materialização.

## 17. Matriz consolidada — Organização

| Domínio | Classe navegacional | Destino(s) existente(s) | Regra |
|---|---|---|---|
| Visão Geral | destination-backed / anchor | `ORG-001` | entrada e síntese |
| Oportunidades e Programas | state-resolved | `ORG-002`, `ORG-003` | resolver por intenção/estado |
| Relações | state-resolved | `ORG-004..006` | somente O↔C em `UXA-019` |
| Responsabilidades e Evidências | destination-backed | `ORG-007` | maturidade própria preservada |
| Organização e Autoridade | contextual-only | sem ID exclusivo | L0 + síntese; sem superfície inventada |
| Planos e Capacidade | specialized/contextual | `ORG-301..304` | não é eixo principal |

## 18. Matriz consolidada — Coletivo

| Domínio | Classe navegacional | Destino(s) existente(s) | Regra |
|---|---|---|---|
| Início | destination-backed / anchor | `COL-002` | entrada e síntese |
| Atividades e Oportunidades | destination-backed/shared | `COL-006` | objeto/decisão preservados |
| Participação | state-resolved | `COL-003..005` | solicitação, vínculo e comunicação |
| Governança e Proteção | state-resolved/shared | `COL-005..007` | governança ≠ acesso técnico |
| Relações | destination-backed | `COL-008` | somente O↔C em `UXA-019` |
| Aprendizados e Evidências | contextual-only | sem ID exclusivo | evidência permanece no objeto |
| Coletivo e Autoridade | contextual-only/partial anchor | `COL-002` parcialmente | sem superfície exclusiva |
| Planos e Capacidade | specialized/contextual | `COL-301..304` | não é eixo principal |

## 19. Matriz de transitions preservadas

| Continuidade | Transições existentes | Tratamento nesta autoridade |
|---|---|---|
| oportunidade Organização | `TRN-201..203` | reutilizar; sem promoção |
| participação Coletivo | `TRN-105..109`, `TRN-112`, `TRN-113` | reutilizar; preservar gap `COL-003 → COL-004` |
| relação O↔C | `TRN-206..209` | reutilizar; permanecem contratadas |
| Planos Coletivo | `TRN-417/418` | preservar validada |
| Planos Organização | `TRN-427/428` | preservar validada |
| demais caminhos de navegação | sem ID automático | não criar `GKR-TRN-*` por inferência |

## 20. Lacunas preservadas

Permanecem fora da materialização canônica candidata:

```text
ORGANIZAÇÃO ↔ ORGANIZAÇÃO
→ SEM AUTORIDADE/SUPERFÍCIE DEDICADA SUFICIENTE

COLETIVO ↔ COLETIVO
→ SEM AUTORIDADE/SUPERFÍCIE DEDICADA SUFICIENTE

ORGANIZAÇÃO E AUTORIDADE
→ SEM GKR-SURF-ORG-* EXCLUSIVO

COLETIVO — APRENDIZADOS E EVIDÊNCIAS
→ SEM GKR-SURF-COL-* EXCLUSIVO

COLETIVO E AUTORIDADE
→ SEM SUPERFÍCIE EXCLUSIVA

CONTINUIDADES SEM GKR-TRN-*
→ CONTINUAM SEM ID
```

A navegação trata essas lacunas como boundary, não como convite para inventar estrutura.

## 21. O que esta materialização não decide

Permanecem explicitamente adiados:

- posição esquerda/topo/rodapé;
- sidebar;
- tabs;
- drawer;
- quantidade visual de itens simultâneos;
- nomenclatura final de interface;
- ícones;
- cores;
- densidade;
- largura;
- breakpoint;
- comportamento responsivo;
- breadcrumbs visuais;
- cards;
- CTA final;
- ordem visual fina;
- componentes;
- estados visuais;
- URL;
- slug;
- rota técnica;
- RBAC;
- cache;
- persistência;
- implementação.

Essas decisões pertencem a wireframes, Design/UI e Product Engineering nos respectivos gates.

## 22. Critérios de suficiência desta materialização

A candidata somente poderá ser promovida se, cumulativamente:

1. L0–L4 preservarem contexto e autoridade;
2. Organização e Coletivo mantiverem topologias próprias;
3. nenhum domínio lógico exigir superfície inventada;
4. os anchors permanecerem `ORG-001` e `COL-002`;
5. domínios multi-superfície forem resolvidos por objeto/estado;
6. `ORG-004..006` e `COL-008` permanecerem somente O↔C;
7. O↔O e C↔C permanecerem gaps;
8. `COL-005` e `COL-006` puderem ser reutilizadas sem duplicação;
9. Aprendizados/Evidências do Coletivo permanecer contextual-only enquanto não houver ID;
10. Organização/Coletivo e Autoridade permanecerem contextuais onde não há superfície exclusiva;
11. Planos permaneça especializado/contextual;
12. produtos especializados não se tornem eixo principal;
13. navegação derivada de atenção aponte para objeto/superfície existente;
14. nenhum caminho de navegação seja usado para promover `GKR-TRN-*`;
15. retorno não produza mutação silenciosa;
16. recontextualização revalide autoridade;
17. estados alternativos permaneçam suportáveis;
18. wireframes continuem não iniciados;
19. Design/UI/protótipo continuem não autorizados;
20. Product Engineering permaneça pausado;
21. Semantic State Validation conclua com sucesso;
22. Mechanical Validation conclua com sucesso;
23. revisão independente não identifique finding material;
24. promoção canônica permaneça ato governado separado.

## 23. Resultado canônico

A materialização candidata define:

```text
O/C AUTHENTICATED NAVIGATION MATERIALIZATION
→ ACTIVE v1.0.0
→ DEFINED / CANONICAL DOCUMENTARY
→ TOPOLOGY DEFINED
→ HIERARCHY DEFINED
→ ENTRY / RETURN SEMANTICS DEFINED
→ CONTEXT REBINDING DEFINED
→ DOMAIN RESOLUTION DEFINED

NEW GKR-SURF-*
→ NONE

NEW GKR-TRN-*
→ NONE

TRANSITION MATURITY CHANGES
→ NONE

PRODUCT MENU VISUAL
→ NOT DEFINED

WIREFRAMES
→ NOT STARTED

DESIGN / UI / PROTOTYPE
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED
```

## 24. Estado governado desta frente

```text
GKR-UX-ORGCOL-AUTH-NAV-MAT-001
→ ACTIVE v1.0.0
→ DEFINED / CANONICAL DOCUMENTARY
→ NORMATIVE = FALSE

NAVIGATION MATERIALIZATION EXECUTION
→ AUTHORIZED BY HUMAN
→ DOCUMENTARY CANDIDATE EXECUTED
→ VALIDATED

CANONICAL PROMOTION
→ AUTHORIZED BY HUMAN
→ EXECUTED
→ VALIDATED

AUTHENTICATED WIREFRAMES
→ SUBSEQUENTLY AUTHORIZED
→ DELIVERY v0.1.0 EXECUTED
→ VALIDATION v1.0.0 PASS
→ CURRENT LOW-FIDELITY REFERENCE

DESIGN / UI / PROTOTYPE
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED

NEXT AUTOMATIC EXECUTION
→ NONE
```
