---
id: GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
title: Organizações e Coletivos — Fluxos Prioritários da Experiência Autenticada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-18
normative: false
maturity: authenticated_priority_flows_defined_pre_navigation_wireframes
depends_on:
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - UXA-014
  - UXA-019
related:
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
---

# Organizações e Coletivos — Fluxos Prioritários da Experiência Autenticada

## 1. Finalidade

Este documento é a **autoridade canônica documental dos fluxos prioritários** da experiência autenticada de Organização e Coletivo.

Ele parte das autoridades já definidas de atores, autoridade, jobs, Arquitetura da Informação, Surface Map e State Map para responder:

> **Quais continuidades funcionais ponta a ponta precisam ser compreensíveis e governadas antes de qualquer materialização de navegação, wireframe, UI ou implementação?**

Um Priority Flow organiza uma continuidade funcional legítima entre contexto, objeto, estado, autoridade, ação e retorno. Ele não é sequência visual de telas.

```text
ATORES / AUTORIDADE / JOBS
+
ARQUITETURA DA INFORMAÇÃO
+
SURFACE MAP
+
STATE MAP
+
TRANSIÇÕES JÁ REGISTRADAS
↓
PRIORITY FLOWS

PRIORITY FLOW
≠ MENU
≠ SITEMAP
≠ ROTA / URL
≠ SEQUÊNCIA FIXA DE TELAS
≠ WIREFRAME
≠ UI
≠ RBAC TÉCNICO
≠ IMPLEMENTAÇÃO
```

Esta autoridade foi promovida em ato governado separado após `DRAFT SUFFICIENCY = PASS / 13 OF 13`. A promoção é exclusivamente documental e não materializa navegação, wireframes, UI ou implementação.

## 2. Regra de autoridade e identidade

Os fluxos desta autoridade devem reutilizar as identidades já existentes.

Regras obrigatórias:

1. `GKR-JOURNEY-SURFACE-REGISTRY-001` permanece autoridade dos IDs estáveis de superfícies;
2. `GKR-JOURNEY-TRANSITION-REGISTRY-001` permanece autoridade dos IDs e maturidades de transições;
3. este documento **não cria novos `GKR-TRN-*`**;
4. este documento **não promove** a maturidade de transições existentes;
5. relação conceitual entre domínios não é convertida silenciosamente em transição;
6. lacuna de identidade permanece lacuna explícita;
7. `UXA-019` continua restrito a relações Organização ↔ Coletivo;
8. nenhuma sequência aqui transporta `ORG-004..006` para Organização–Organização;
9. nenhuma sequência aqui transporta `COL-008` para Coletivo–Coletivo.

Rótulos de seções deste documento são nomes funcionais de fluxos, não IDs estáveis de registry.

## 3. O que torna um fluxo prioritário

Um fluxo é prioritário quando cumpre cumulativamente os seguintes critérios:

- sustenta um job estrutural, de núcleo operacional, governança/proteção ou prestação de contas;
- cruza estados materiais que alteram o que pode ser legitimamente compreendido ou realizado;
- exige preservação explícita de contexto e autoridade;
- possui impacto direto sobre continuidade, responsabilidade, proteção ou autonomia;
- precisa acomodar ausência, bloqueio, contestação, indisponibilidade ou interrupção;
- não pode ser substituído por uma capacidade comercial especializada;
- é necessário para que a futura navegação principal seja definida sem inventar tela primeiro.

Fluxos especializados já existentes podem ser conectados aos Priority Flows, mas não são reclassificados como núcleo principal apenas porque possuem materialização ou maturidade maior.

## 4. Contrato mínimo de qualquer Priority Flow

Todo fluxo prioritário precisa declarar ou preservar:

1. **contexto ativo** — Organização ou Coletivo, unidade quando aplicável e escopo;
2. **ator e autoridade** — quem pode compreender, propor, aprovar, executar, contestar ou encerrar;
3. **objeto canônico** — qual objeto possui o estado e a fonte de verdade;
4. **estado de entrada** — condição material que justifica a continuidade;
5. **ação legítima** — ação permitida no limite da autoridade;
6. **condições alternativas** — ausência, bloqueio, contestação, risco, indisponibilidade e proteção;
7. **efeitos proibidos** — o que navegar ou agir não pode inferir;
8. **retorno/interrupção** — como sair, cancelar ou retomar sem mutação silenciosa;
9. **reversibilidade proporcional** — quando a ação deve poder ser revista, pausada ou contestada;
10. **proveniência e evidência** — o que sustenta afirmações e decisões;
11. **relação com o Transition Registry** — transições existentes, lacunas ou ausência deliberada de ID;
12. **fronteira de autoridade** — quando a Guivos ou o participante deixa de controlar o próximo estágio.

## 5. Espinha dorsal transversal — contexto → Momento → objeto → Próximo Passo

Organização e Coletivo compartilham uma continuidade estrutural, sem exigir paridade artificial de navegação:

```text
PESSOA AUTENTICADA
↓
CONTEXTO ATIVO
↓
AUTORIDADE REVALIDADA
↓
MOMENTO / ATENÇÃO MATERIAL
↓
OBJETO CANÔNICO QUE ORIGINA A ATENÇÃO
↓
COMPREENSÃO DO ESTADO
↓
PRÓXIMO PASSO POSSÍVEL
↓
AUTORIDADE NECESSÁRIA
↓
AÇÃO OU DECISÃO LEGÍTIMA
↓
OBJETO CANÔNICO ATUALIZADO
↓
SÍNTESE RECONSULTADA
```

Essa espinha dorsal **não declara transições de navegação** entre Visão Geral/Início e todos os demais domínios.

```text
ATENÇÃO
→ VISTA DERIVADA

PRÓXIMO PASSO
→ ORIENTAÇÃO CONTEXTUAL

ATENÇÃO
≠ NOVO OBJETO

PRÓXIMO PASSO
≠ AUTORIDADE
≠ OBRIGAÇÃO AUTOMÁTICA
```

Mudança de contexto exige revalidação de autoridade e não transporta silenciosamente:

- permissões;
- decisão pendente;
- informação protegida;
- filtros;
- contraparte;
- dados pessoais;
- ação iniciada em outro contexto.

## 6. Organização — Contexto, Momento e responsabilidade atual

### Finalidade

Suportar principalmente `ORG-J01`, `ORG-J02`, `ORG-J03` e `ORG-J09`.

A continuidade funcional esperada é:

```text
ORGANIZAÇÃO / UNIDADE ATIVA
↓
PAPEL E AUTORIDADE
↓
VISÃO GERAL / GKR-SURF-ORG-001
↓
MOMENTO INSTITUCIONAL
↓
ATENÇÃO MATERIAL IDENTIFICADA
↓
OBJETO DE ORIGEM
↓
ESTADO + EVIDÊNCIA / INCERTEZA
↓
AÇÃO POSSÍVEL OU NECESSIDADE DE OUTRA AUTORIDADE
```

Estados mínimos que precisam ser suportados:

- contexto válido;
- contexto incompleto;
- autoridade válida;
- autoridade insuficiente;
- aprovação adicional necessária;
- responsável ausente;
- operação regular;
- atenção necessária;
- atenção urgente;
- bloqueado;
- informação desconhecida, inferida, contestada ou desatualizada;
- capacidade limitada ou atingida;
- proteção requerida.

Nenhum novo `GKR-TRN-*` é declarado para esta espinha principal nesta autoridade.

## 7. Organização — Oportunidade ou programa legítimo

### Finalidade

Suportar `ORG-J04` sem reconstruir o fluxo especializado já existente.

Continuidade principal:

```text
CONTEXTO INSTITUCIONAL VÁLIDO
↓
NECESSIDADE / OBJETIVO / PROGRAMA
↓
DADOS E CONDIÇÕES MATERIAIS
↓
GKR-SURF-ORG-002 — CADASTRO
↓
REVISÃO / CORREÇÃO / AUTORIDADE APLICÁVEL
↓
GKR-SURF-ORG-003 — APROVADA / ATIVA
↓
ELEGÍVEL À DESCOBERTA
↓
ACOMPANHAMENTO DE RESPONSABILIDADES / EVIDÊNCIAS
↓
REVISÃO, PAUSA, EXPIRAÇÃO OU ENCERRAMENTO
```

Transições existentes preservadas:

- `GKR-TRN-201` — `ORG-001 → ORG-002` — parcial;
- `GKR-TRN-202` — `ORG-002 → ORG-003` — localmente validada;
- `GKR-TRN-203` — `ORG-003 → PER-201` — integralmente validada no recorte de ativação → descoberta.

A maturidade acima **não é alterada** por este documento.

Preservações:

- publicação ≠ distribuição;
- distribuição ≠ relevância;
- relevância ≠ impacto;
- patrocínio ≠ prioridade orgânica;
- ausência de evidência ≠ ausência de resultado;
- pausa/expiração/encerramento prevalecem sobre representações anteriores.

## 8. Organização — Responsabilidades, evidências e prestação de contas

### Finalidade

Suportar `ORG-J06` e a parte correspondente de `ORG-J08`.

Superfície principal conhecida:

- `GKR-SURF-ORG-007` — resultados e evidências institucionais — maturidade indeterminada.

Continuidade funcional:

```text
RESPONSABILIDADE / COMPROMISSO
↓
ESTADO DE EXECUÇÃO
↓
EVIDÊNCIA DISPONÍVEL / AUSENTE / INSUFICIENTE / CONFLITANTE
↓
INTERPRETAÇÃO PROPORCIONAL
↓
RESULTADO QUE PODE SER AFIRMADO
↓
LIMITAÇÕES / FATORES EXTERNOS
↓
REVISÃO / CORREÇÃO / CONTESTAÇÃO
```

Invariantes:

```text
ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO COMPROVADO

CONFIRMED
≠ IMPACT PROVEN

INFERRED
≠ FACT

UNKNOWN
≠ ZERO

NO EVIDENCE
≠ NO RESULT

CORRELATION
≠ CAUSATION
```

Nenhuma transição nova é inferida para `ORG-007`.

## 9. Coletivo — Contexto, Início e Momento coletivo

### Finalidade

Suportar `COL-J01`, `COL-J02` e `COL-J11`.

Continuidade:

```text
COLETIVO ATIVO
↓
PROPÓSITO + PAPEL + REGRA DE GOVERNANÇA
↓
GKR-SURF-COL-002 — INÍCIO / CONTEXTO DO RESPONSÁVEL
↓
MOMENTO COLETIVO
↓
ATENÇÃO MATERIAL
↓
OBJETO DE ORIGEM
↓
ESTADO + AUTORIDADE / DECISÃO COLETIVA NECESSÁRIA
↓
PRÓXIMO PASSO JUSTIFICÁVEL
```

A existência de `COL-002` e dos contratos especializados associados não promove o antigo material administrativo a wireframe principal autenticado final.

Estados mínimos:

- contexto válido/incompleto;
- autoridade válida/insuficiente;
- decisão coletiva necessária;
- atenção necessária/urgente;
- bloqueio;
- proteção requerida;
- contestação;
- capacidade limitada;
- informação material desconhecida.

Nenhuma nova transição principal é declarada.

## 10. Coletivo — Participação, solicitação, vínculo e papel

### Finalidade

Suportar `COL-J04` integrando o fluxo especializado existente sem transformar a perspectiva da Pessoa em estado operacional do Coletivo.

Continuidade bilateral já conhecida:

```text
SOLICITAÇÃO DA PESSOA
↓
MESMO OBJETO LÓGICO DISPONIBILIZADO AO RESPONSÁVEL
↓
GKR-SURF-COL-003 — GESTÃO DE SOLICITAÇÕES
├── PEDIR INFORMAÇÃO ADICIONAL
├── APROVAR
└── RECUSAR
↓
VÍNCULO DA PESSOA QUANDO APROVADO
↓
GKR-SURF-COL-004 — PARTICIPANTES E VÍNCULOS
[COL-003 → COL-004 = CONTINUIDADE LÓGICA; TRANSIÇÃO ESTÁVEL NÃO DECLARADA]
↓ GKR-TRN-113 QUANDO HOUVER COMUNICAÇÃO OFICIAL A PARTICIPANTES AUTORIZADOS
GKR-SURF-COL-005 — COMUNICAÇÃO OFICIAL QUANDO APLICÁVEL À CONTINUIDADE DA PARTICIPAÇÃO
```

Transições preservadas:

- `GKR-TRN-105` — `PER-105 → COL-003`;
- `GKR-TRN-106` — `COL-003 → PER-105`;
- `GKR-TRN-107` — `PER-105 → COL-003`;
- `GKR-TRN-108` — `COL-003 → PER-106`;
- `GKR-TRN-109` — `COL-003 → PER-105`;
- `GKR-TRN-112` — `COL-002 → COL-003`.

Essas transições mantêm sua maturidade própria. A continuidade pós-aprovação `COL-003 → COL-004` é reconhecida pelo Surface Map, mas **não possui transição estável declarada**. Quando a continuidade exige comunicação oficial a participantes autorizados, `GKR-TRN-113 — COL-004 → COL-005` já existe como transição **contratada** e mantém essa maturidade sem promoção nesta autoridade.

Preservações:

```text
PERTENCER
≠ REPRESENTAR
≠ MODERAR
≠ APROVAR
≠ ADMINISTRAR

APROVAR VÍNCULO
≠ CONCEDER AUTORIDADE OPERACIONAL IRRESTRITA
```

A perspectiva da Pessoa continua governada pelas superfícies `PER-*` correspondentes.

## 11. Coletivo — Atividade, oportunidade e coordenação

### Finalidade

Suportar `COL-J03` e `COL-J06`.

Superfície principal conhecida:

- `GKR-SURF-COL-006` — atividades e oportunidades.

Continuidade funcional:

```text
PROPÓSITO / NECESSIDADE COLETIVA
↓
ATIVIDADE / OPORTUNIDADE
↓
AUTORIDADE OU DECISÃO APLICÁVEL
↓
RECURSOS / CAPACIDADE / RESPONSÁVEL QUANDO LEGÍTIMO
↓
EXECUÇÃO
↓
ESTADO / BLOQUEIO / PAUSA
↓
APRENDIZADO / EVIDÊNCIA
↓
REVISÃO OU ENCERRAMENTO
```

Esta autoridade não cria transições estáveis para preencher lacunas entre essas condições.

Preservações:

- necessidade coletiva ≠ obrigação individual;
- participação ≠ impacto;
- popularidade ≠ relevância;
- volume ≠ valor;
- plano pago ≠ prioridade;
- baixa participação ≠ fracasso sem contexto/evidência.

## 12. Coletivo — Governança, comunicação e proteção

### Finalidade

Suportar `COL-J05` e `COL-J10`.

Superfícies relacionadas:

- `GKR-SURF-COL-005`;
- `GKR-SURF-COL-006`;
- `GKR-SURF-COL-007`.

Continuidade funcional:

```text
OBJETO / DECISÃO / CONDIÇÃO MATERIAL
↓
REGRA DE GOVERNANÇA APLICÁVEL
↓
AUTORIDADE / INSTÂNCIA LEGÍTIMA
↓
CONSULTA OU DECISÃO QUANDO APLICÁVEL
↓
COMUNICAÇÃO OFICIAL PROPORCIONAL
↓
EXECUÇÃO / PROTEÇÃO / MODERAÇÃO
↓
REVISÃO / CONTESTAÇÃO / NÃO RETALIAÇÃO
```

Transição existente relevante:

- `GKR-TRN-113` — `COL-004 → COL-005` — contratada.

Este documento não promove `TRN-113` e não declara transições adicionais.

Estados alternativos obrigatórios incluem:

- decisão contestada;
- conflito de governança;
- proteção requerida;
- conteúdo/informação protegida;
- revisão necessária;
- suspensão proporcional;
- responsável ausente;
- autoridade insuficiente.

## 13. Coletivo — Aprendizados, evidências e prestação de contas

### Finalidade

Suportar `COL-J08`.

O Surface Map reconhece o domínio lógico **Aprendizados e Evidências**, mas não existe ID exclusivo dedicado no registro corrente.

Essa ausência permanece explícita.

Continuidade funcional:

```text
ATIVIDADE / AÇÃO / EXPERIÊNCIA COLETIVA
↓
REGISTRO LEGÍTIMO
↓
EVIDÊNCIA / LIMITAÇÃO
↓
APRENDIZADO
↓
CONTRIBUIÇÃO QUE PODE SER SUSTENTADA
↓
RESULTADO AINDA NÃO CONFIRMADO QUANDO APLICÁVEL
↓
REVISÃO / CONTESTAÇÃO / ATUALIZAÇÃO
```

Esta autoridade não cria superfície ou transição para eliminar essa lacuna.

## 14. Fluxo bilateral prioritário — Organização ↔ Coletivo

### Finalidade

Este é o fluxo compartilhado governado por `UXA-019` e pelos jobs `BIL-J01..06`.

Ele se aplica **somente a Organização ↔ Coletivo**.

Superfícies e transições estáveis existentes:

```text
GKR-SURF-ORG-004
↓ GKR-TRN-206
GKR-SURF-COL-008
↓ GKR-TRN-207
GKR-SURF-ORG-005
↓ GKR-TRN-208
GKR-SURF-ORG-006
↓ GKR-TRN-209
GKR-SURF-ORG-006
```

Maturidade corrente:

- `GKR-TRN-206..209` = contratadas;
- esta autoridade não promove nenhuma delas.

### Lifecycle funcional

```text
RASCUNHO
↓
PROPOSTA
↓
AVALIAÇÃO BILATERAL
↓
NEGOCIAÇÃO
↓
AGUARDANDO INFORMAÇÃO QUANDO APLICÁVEL
↓
AGUARDANDO CONSENTIMENTO/APROVAÇÃO QUANDO APLICÁVEL
↓
APROVADA PELAS AUTORIDADES
↓
[ATIVA SOMENTE QUANDO AS CONDIÇÕES GOVERNADAS DE ATIVAÇÃO ESTIVEREM SATISFEITAS]
↓
ATIVA
↓
EM REVISÃO
├── RENOVADA OU AJUSTADA
├── ALTERAÇÃO MATERIAL PENDENTE
├── PAUSADA
├── BLOQUEADA POR PROTEÇÃO OU PRIVACIDADE
├── CONTESTADA
├── SUSPENSA PREVENTIVAMENTE
├── EXPIRADA
├── ENCERRADA
└── ENCERRADA COM RESPONSABILIDADES REMANESCENTES
```

A sequência acima organiza condições funcionais. Ela não declara uma transição estável para cada mudança de estado.

```text
APROVADA PELAS AUTORIDADES
≠ EFEITO TÉCNICO AUTOMÁTICO
≠ ATIVAÇÃO AUTOMÁTICA

ATIVA
→ SOMENTE O ESCOPO LEGITIMAMENTE APROVADO PODE SER EXECUTADO
```

### Alteração material

```text
ALTERAÇÃO MATERIAL PROPOSTA
↓
NOVA AVALIAÇÃO BILATERAL
↓
NOVA APROVAÇÃO LEGÍTIMA
↓
NOVO ESCOPO EFETIVO

ATÉ A NOVA APROVAÇÃO:
ESCOPO ANTERIOR APROVADO
→ CONTINUA SENDO O ÚNICO ESCOPO EFETIVO
```

### Estados alternativos obrigatórios

O fluxo precisa preservar:

- proposta recusada;
- autoridade insuficiente;
- aprovação divergente entre as partes;
- relação ativa sem atenção material;
- compromisso atrasado;
- recurso indisponível;
- dado ou consentimento ausente;
- conflito de interesse;
- uso de marca contestado;
- relação comercial não declarada;
- risco de perda de autonomia;
- denúncia em análise;
- suspensão urgente;
- renovação pendente;
- encerramento solicitado por uma das partes;
- baixa conectividade;
- operação internacional;
- informação sensível protegida.

## 15. Fluxo transversal de correção, contestação, pausa e saída

Correção e saída não são telas isoladas nem exceções tardias.

Esse fluxo transversal suporta `ORG-J08`, `COL-J10` e `BIL-J06`.

```text
INFORMAÇÃO / DECISÃO / RELAÇÃO / EVIDÊNCIA
↓
PROBLEMA, MUDANÇA OU CONTESTAÇÃO IDENTIFICADA
↓
AUTORIDADE E FONTE REAVALIADAS
↓
CORREÇÃO / REVISÃO / CONTESTAÇÃO
├── CONTINUIDADE AJUSTADA
├── PAUSA
├── PROTEÇÃO / SUSPENSÃO
└── ENCERRAMENTO
↓
RESPONSABILIDADES REMANESCENTES PRESERVADAS
```

Invariantes:

- contestação não pode ser apagada por mudança de interface;
- pausa ≠ encerramento;
- encerramento ≠ apagamento automático;
- proteção ≠ punição;
- denúncia ≠ culpa comprovada;
- revisão ≠ aprovação automática;
- reversão não pode apagar trilha legítima de decisão;
- não retaliação deve ser preservada quando aplicável.

## 16. Conexões com fluxos especializados

### 16.1 Planos

Planos permanecem capacidade especializada/contextual.

Transições existentes:

- Coletivo: `GKR-TRN-417/418` entre `COL-002` e `COL-301`;
- Organização: `GKR-TRN-427/428` entre `ORG-001` e `ORG-301`.

Regras:

```text
ABRIR PLANOS
≠ SELECIONAR PLANO
≠ CONTRATAR
≠ COBRAR
≠ ALTERAR ENTITLEMENT

RETORNAR DE PLANOS
≠ CANCELAR
≠ ALTERAR CAPACIDADE
```

As famílias `TRN-411..416` e `TRN-421..426` preservam maturidades próprias e não são promovidas por esta frente.

### 16.2 Descoberta pública de oportunidades

`GKR-TRN-203` conecta oportunidade institucional ativa à elegibilidade de descoberta pela Pessoa.

As transições `TRN-204`, `TRN-210`, `TRN-211` e `TRN-205` pertencem à continuidade da Pessoa até `BND-001`.

A experiência autenticada da Organização pode acompanhar o estado autorizado da oportunidade, mas não absorve a jornada pessoal nem recebe autoridade sobre relevância individual.

### 16.3 Intelligence, Ads, Business, Journey, Mall, Travel e Media

Produtos Especializados podem apoiar ou receber handoffs quando existir autoridade própria, mas não se tornam o eixo dos Priority Flows.

```text
ORGANIZAÇÃO
≠ GUIVOS BUSINESS

COLETIVO
≠ PRODUTO ESPECIALIZADO

INTELLIGENCE
→ PODE APOIAR COMPREENSÃO

INTELLIGENCE
≠ AUTORIDADE DE DECISÃO

ADS / PATROCÍNIO
≠ RELEVÂNCIA ORGÂNICA
```

## 17. Ausência, bloqueio e indisponibilidade

Nenhum Priority Flow pode ser definido apenas pelo happy path.

Cobertura mínima:

- informação material incompleta;
- fonte indisponível;
- autoridade insuficiente;
- aprovação adicional necessária;
- responsável ausente;
- contraparte aguardada;
- recurso indisponível;
- capacidade atingida;
- dependência externa indisponível;
- operação degradada;
- baixa conectividade;
- proteção/privacidade bloqueando ação;
- decisão ou evidência contestada;
- conflito de governança;
- alteração material pendente;
- risco urgente;
- expiração;
- encerramento com responsabilidades remanescentes.

```text
AUSÊNCIA DE DADO
≠ ZERO

INDISPONIBILIDADE TÉCNICA
≠ FALHA DO PARTICIPANTE

BLOQUEIO
≠ RECUSA

AGUARDANDO
≠ APROVADO

CONTESTADO
≠ INVÁLIDO POR DEFINIÇÃO
```

## 18. Retorno, interrupção, concorrência e idempotência

Materialização futura dos fluxos deverá preservar:

- retorno ao contexto de origem quando legítimo;
- cancelamento sem mutação silenciosa;
- reconsulta do objeto canônico após retorno;
- proteção contra duplicação por retry;
- revalidação de autoridade após intervalo ou mudança de contexto;
- tratamento explícito de atualização concorrente;
- não transporte de formulário/decisão incompleta entre contextos;
- fallback proporcional quando destino ou dependência estiver indisponível.

```text
NAVEGAR
≠ CONFIRMAR

VOLTAR
≠ DESFAZER AUTOMATICAMENTE

RECARREGAR / RETRY
≠ DUPLICAR EFEITO

MUDANÇA DE CONTEXTO
→ REVALIDA AUTORIDADE
```

## 19. Matriz de cobertura dos Jobs prioritários

Esta matriz demonstra cobertura funcional sem transformar ausência de autoridade em falsa completude.

### Organização

| Job | Cobertura nesta autoridade | Estado |
|---|---|---|
| `ORG-J01` — contexto institucional | §6 | coberto no limite documental |
| `ORG-J02` — Momento e atenção material | §6 | coberto no limite documental |
| `ORG-J03` — identidade, capacidade, condições e responsabilidades | §6 + §15 | coberto funcionalmente; sem nova transição |
| `ORG-J04` — oportunidades e programas | §7 | coberto com reutilização de `TRN-201..203` |
| `ORG-J05` — relações com Coletivos e Organizações | §14 | **parcial**: Organização↔Coletivo coberto por `UXA-019`; Organização↔Organização permanece lacuna explícita |
| `ORG-J06` — compromissos, evidências e resultados | §8 + §14 | coberto no limite documental; sem fabricar impacto |
| `ORG-J07` — capacidade comercial e Planos | §16.1 | conexão especializada preservada; não é eixo principal |
| `ORG-J08` — corrigir, contestar, revisar, pausar ou encerrar | §14 + §15 | coberto transversalmente |
| `ORG-J09` — Próximo Passo e autoridade | §5 + §6 | coberto como orientação contextual, não obrigação |

### Coletivo

| Job | Cobertura nesta autoridade | Estado |
|---|---|---|
| `COL-J01` — contexto coletivo | §9 | coberto no limite documental |
| `COL-J02` — Momento e atenção material | §9 | coberto no limite documental |
| `COL-J03` — atividades, ações, recursos e necessidades | §11 | coberto funcionalmente; lacunas de transição preservadas |
| `COL-J04` — participação, solicitações, papéis e vínculos | §10 | coberto com fluxos existentes e lacuna pós-aprovação explícita |
| `COL-J05` — decisões, comunicação, moderação e proteção | §12 | coberto no limite documental |
| `COL-J06` — oportunidades ou atividades legítimas | §11 | coberto funcionalmente |
| `COL-J07` — relações com Organizações e outros Coletivos | §14 | **parcial**: Organização↔Coletivo coberto por `UXA-019`; Coletivo↔Coletivo permanece lacuna explícita |
| `COL-J08` — avanço, aprendizado e evidências | §13 | coberto no limite documental; domínio sem ID exclusivo preservado |
| `COL-J09` — capacidade e Planos | §16.1 | conexão especializada preservada; não é eixo principal |
| `COL-J10` — corrigir, contestar, revisar, pausar ou encerrar | §14 + §15 | coberto transversalmente |
| `COL-J11` — Próximo Passo e decisão/autoridade | §5 + §9 | coberto como orientação justificável |

### Jobs bilaterais Organização ↔ Coletivo

| Job | Cobertura nesta autoridade | Estado |
|---|---|---|
| `BIL-J01` — propor relação com finalidade/escopo | §14 | coberto |
| `BIL-J02` — avaliar autoridade, capacidade, riscos e condições | §14 | coberto |
| `BIL-J03` — negociar alterações materiais | §14 | coberto com reavaliação e nova aprovação |
| `BIL-J04` — aprovar o mesmo escopo pelas duas autoridades | §14 | coberto; aprovação ≠ ativação automática |
| `BIL-J05` — acompanhar compromissos e evidências | §14 + §8/§13 conforme a perspectiva | coberto no limite de evidência permitida |
| `BIL-J06` — revisar, contestar, pausar ou encerrar | §14 + §15 | coberto |

Consequentemente:

```text
COBERTURA DE JOB
≠ COMPLETUDE DE REGISTRY

ORG-J05
→ ORGANIZAÇÃO↔COLETIVO COBERTO
→ ORGANIZAÇÃO↔ORGANIZAÇÃO = GAP EXPLÍCITO

COL-J07
→ COLETIVO↔ORGANIZAÇÃO COBERTO
→ COLETIVO↔COLETIVO = GAP EXPLÍCITO
```

## 20. Matriz inicial de reconciliação com o Transition Registry

| Fluxo funcional | Superfícies / objetos principais | Transições conhecidas | Tratamento nesta autoridade |
|---|---|---|---|
| Organização — contexto e Momento | `ORG-001` + objetos referenciados | nenhuma espinha principal estável declarada | lacuna preservada; não criar ID |
| Organização — oportunidade/programa | `ORG-002..003` | `TRN-201..203` | reutilizar; sem promoção |
| Organização — evidência/prestação de contas | `ORG-007` | sem transição dedicada conhecida | lacuna preservada |
| Coletivo — contexto e Momento | `COL-002` + objetos referenciados | nenhuma espinha principal estável declarada | lacuna preservada |
| Coletivo — participação | `COL-003..005` + `PER-105/106` | `TRN-105..109`, `TRN-112`; `COL-003 → COL-004` sem ID; `TRN-113` para `COL-004 → COL-005` no recorte de comunicação | reutilizar o existente; preservar somente a lacuna real |
| Coletivo — atividade/oportunidade | `COL-006` | sem cadeia estável completa conhecida | lacuna preservada |
| Coletivo — governança/comunicação/proteção | `COL-005..007` | `TRN-113` no recorte conhecido | reutilizar; sem promoção |
| Coletivo — aprendizados/evidências | domínio lógico sem ID exclusivo | sem transição dedicada conhecida | lacuna preservada |
| Relação Organização ↔ Coletivo | `ORG-004..006`, `COL-008` | `TRN-206..209` | reutilizar como contratadas; sem promoção |
| Planos do Coletivo | `COL-002 ↔ COL-301` | `TRN-417/418` | conexão especializada já validada |
| Planos da Organização | `ORG-001 ↔ ORG-301` | `TRN-427/428` | conexão especializada já validada |

A matriz não certifica completude do Transition Registry e não cria maturidade nova.

## 21. Decisões explicitamente adiadas

Esta autoridade não define:

- sitemap final;
- menu;
- ordem visual de navegação;
- quantidade de telas;
- URLs ou rotas;
- novo `GKR-SURF-*`;
- novo `GKR-TRN-*`;
- wireframe;
- layout;
- componente;
- copy final;
- desktop/mobile;
- responsive behavior;
- notificação final;
- busca/filtro final;
- RBAC técnico;
- Design System;
- UI;
- protótipo;
- implementação;
- integração técnica;
- produção;
- testes com participantes reais.

Também não inicia `UXA-102/V5` nem Product Engineering.

## 22. Critérios de suficiência consumidos na promoção documental

A promoção documental desta autoridade consumiu cumulativamente os seguintes critérios:

1. os fluxos selecionados cobrirem os jobs estruturais e de núcleo sem transformar capacidades especializadas em eixo principal;
2. cada fluxo explicitar contexto, autoridade, objeto, estados relevantes, alternativas, retorno e fronteira;
3. o fluxo bilateral cobrir lifecycle, alteração material, contestação, proteção e encerramento com responsabilidades remanescentes;
4. as perspectivas de Pessoa, Organização e Coletivo permanecerem separadas;
5. todas as referências a `GKR-TRN-*` preservarem origem, destino e maturidade vigentes;
6. nenhuma lacuna seja preenchida por ID inventado;
7. Organização–Organização e Coletivo–Coletivo permaneçam lacunas explícitas onde não houver autoridade própria;
8. Planos e Produtos Especializados permaneçam especializados/contextuais;
9. ausência, bloqueio, contestação e indisponibilidade tenham tratamento explícito;
10. reversibilidade, interrupção, concorrência e idempotência sejam preservadas;
11. evidência e impacto permaneçam semanticamente separados;
12. navegação materializada, wireframes, Design/UI e Product Engineering continuem fechados;
13. validação semântica, mecânica e revisão independente concluam sem finding material no HEAD candidato.

## 23. Estado desta autoridade

```text
GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
→ ACTIVE v1.0.0
→ DEFINED / CANONICAL DOCUMENTARY

SURFACE MAP
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

STATE MAP
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

PRIORITY FLOWS
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

NAVIGATION MATERIALIZATION
→ NOT MATERIALIZED / NOT RELEASED

AUTHENTICATED WIREFRAMES
→ NOT STARTED / NOT RELEASED

DESIGN / UI / PROTOTYPE
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED
```

## 24. Próximo gate após promoção

O próximo gate governado elegível é **Navigation Materialization**, ainda não autorizado.

A promoção documental desta autoridade não autoriza automaticamente:

- navegação materializada;
- wireframes;
- Design/UI;
- protótipo;
- implementação;
- Product Engineering.

Qualquer materialização de navegação deverá ocorrer por ato governado separado, preservando os IDs/maturidades dos registries, as lacunas explícitas, autoridade, reversibilidade, proteção e os limites desta autoridade.
