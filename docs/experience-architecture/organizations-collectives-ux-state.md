---
id: GKR-UX-ORGCOL-UX-STATE-001
title: Organizações e Coletivos — Estado Funcional de Experiência e Handoff para Design
status: active
version: 1.12.5
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-24
normative: false
related:
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
  - GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001
  - UXA-014
  - UXA-019
---

# Organizações e Coletivos — Estado Funcional de Experiência e Handoff para Design

## 1. Decisão de estado

O estado vigente é:

> **A primeira entrega low-fidelity de Organização e Coletivo foi executada e validada com `PASS`. A elegibilidade high-fidelity posterior também concluiu `PASS` em `GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001 v1.0.1`; a autorização high-fidelity foi concedida em `GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001 v1.0.2`, e o ato separado `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0` liberou a execução externa; a entrega high-fidelity ainda está `NOT_RECEIVED`.**

A entrega corrente materializa em baixa fidelidade a visão geral/início de Organização e Coletivo, a hierarquia funcional, variantes de atenção, autoridade, proteção, troca de contexto e indisponibilidade. Permanecem deliberadamente não definidos: UI final, componentes finais, visual high-fidelity, protótipo navegável, implementação e testes de usabilidade.

Atores, papéis, autoridades, jobs prioritários, Arquitetura da Informação, mapa lógico de superfícies, mapa funcional de estados, Priority Flows e Navigation Materialization autenticada já foram definidos documentalmente em instrumentos próprios. A Navigation Materialization canônica está em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2`. Posteriormente, os wireframes autenticados low-fidelity foram autorizados, entregues em `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` e validados com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. O release externo posterior não equivale a entrega high-fidelity recebida ou validada. UI final recebida pelo GKR, protótipo e implementação continuam não materializados por esta autoridade.

## 2. O que já existe e governa a continuidade da UX

A existência do pacote low-fidelity validado não equivale a UI final, high-fidelity ou implementação.

Já existem insumos e autoridades documentais relevantes:

- `UXA-014` — fundação funcional de Organizações e Coletivos;
- `UXA-019` — contrato funcional das relações Organização ↔ Coletivo;
- `GKR-UX-ORGCOL-AUTH-JOBS-001` — atores, papéis, autoridades e jobs prioritários da experiência autenticada;
- `GKR-UX-ORGCOL-AUTH-IA-001` — Arquitetura da Informação autenticada;
- `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001` — mapa lógico de superfícies autenticadas definido documentalmente;
- `GKR-UX-ORGCOL-AUTH-STATE-MAP-001` — mapa funcional de estados autenticados definido documentalmente;
- `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001` — fluxos prioritários autenticados definidos documentalmente;
- Jornadas integradas da Organização e do Coletivo em estado `active`;
- contratos de oportunidades, publicação, descoberta e relações;
- Documento Mestre da Home pública de Organizações e Coletivos;
- `RP-002` — Research sobre supply, papéis, rede, valor e modelo econômico.

Esses materiais governam a continuidade da experiência. O pacote low-fidelity corrente é evidência visual funcional explícita; Jobs, IA, Surface Map, State Map, Priority Flows, Navigation Materialization e low-fidelity validado não autorizam inferir UI final executada, linguagem visual final, protótipo ou implementação; o release high-fidelity existente libera execução externa, com `DELIVERY_NOT_RECEIVED` e validação high-fidelity ainda `NOT_STARTED`.

## 3. Correção dos registros anteriores

`UXA-015..018` são produtores históricos absorvidos e removidos do corpus corrente. Sua proveniência permanece no Git, sem autoridade visual ou funcional vigente.

```text
UXA-015..018
→ FUNCTION ABSORBED
→ PHYSICAL PRODUCERS REMOVED
→ GIT PRESERVES PROVENANCE
→ NOT DESIGN INPUT
→ NOT AI INPUT
```

Os SVGs associados também foram removidos fisicamente. Nenhum SVG histórico desses produtores permanece disponível como especificação, referência aprovada, baseline de produto ou autoridade de Design.

## 4. O que não pode ser inferido

Não é permitido concluir, a partir de material histórico, da IA documental, do mapa lógico de superfícies ou do State Map, que já estejam definidos:

- dashboard da Organização;
- Home autenticada da Organização;
- Home autenticada do Coletivo;
- menu interno final;
- cards prioritários;
- ordem final dos blocos;
- ações principais materializadas;
- densidade de informação;
- layout desktop ou mobile;
- estados vazios materializados;
- estados de permissão materializados;
- fluxos de administração materializados;
- modelo visual final de gestão de membros;
- sistema visual final de governança;
- componentes reutilizáveis;
- padrões visuais.

## 5. Separação entre arquitetura funcional, IA, mapa de superfícies, State Map e wireframe

Uma arquitetura funcional, uma Arquitetura da Informação, um mapa lógico de superfícies e um mapa funcional de estados podem afirmar que a experiência precisa preservar:

- autoridade;
- autonomia;
- voluntariedade;
- transparência;
- responsabilidade;
- evidência;
- contestação;
- proteção;
- clareza de papéis;
- agrupamentos lógicos e contexto ativo.

Isso não determina automaticamente:

```text
onde cada elemento aparece
→ em qual tela
→ em qual ordem visual
→ com qual componente
→ com qual densidade
→ com qual interação
→ com qual linguagem visual
```

Essas decisões pertencem às etapas posteriores de Navigation Materialization e wireframing ainda pendentes.

## 6. Sequência obrigatória quando a frente avançar

A construção deverá continuar do estado documental vigente, e não dos SVGs históricos:

1. fundamentos, Research e jornadas vigentes — reconciliados documentalmente;
2. atores, papéis, autoridades e jobs prioritários — definidos em `GKR-UX-ORGCOL-AUTH-JOBS-001`;
3. Arquitetura da Informação — definida em `GKR-UX-ORGCOL-AUTH-IA-001`;
4. mapa lógico de superfícies — definido documentalmente em `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001`;
5. mapa funcional de estados — definido documentalmente em `GKR-UX-ORGCOL-AUTH-STATE-MAP-001`;
6. Priority Flows — definidos documentalmente em `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001`;
7. elegibilidade de Navigation Materialization — `PASS / ACTIVE / CANONICAL` em `GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001`;
8. Navigation Materialization — `DEFINED / CANONICAL DOCUMENTARY` em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2`;
9. wireframes low-fidelity — entregues e validados;
10. elegibilidade high-fidelity — `PASS`;
11. autorização high-fidelity — `GRANTED`;
12. release para execução externa high-fidelity — `ISSUED` em `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001`;
13. receber entrega high-fidelity inspecionável;
14. validar a entrega high-fidelity contra as autoridades funcionais correntes;
15. construir protótipo somente quando autorizado por gate posterior;
16. testar com Pessoas / representantes reais quando houver autorização e objeto adequado;
17. somente depois preparar handoff técnico.

Nenhuma etapa concluída autoriza automaticamente a seguinte.

## 7. Gate para declarar um wireframe definido

Um wireframe só poderá ser considerado definido quando existir, cumulativamente:

- escopo da superfície explicitado;
- participante e papel explicitados;
- pergunta funcional da superfície definida;
- estados principais e alternativos mapeados;
- hierarquia de informação decidida;
- fluxos de entrada e saída identificados;
- materialização gráfica produzida;
- revisão humana explícita;
- versão e estado documental registrados.

Sem esses elementos, existe apenas hipótese ou exploração.

## 8. Gate para declarar validação

Uma validação de wireframe exige um wireframe vigente como objeto.

Portanto:

> **a validação vigente low-fidelity de Organização e Coletivo é `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0 = PASS`; isso não executa high-fidelity e não autoriza protótipo ou implementação.**

A validação corrente foi executada contra a entrega v0.1.0 e as autoridades vigentes; qualquer reformulação futura exigirá validação correspondente.

## 9. Home pública não é wireframe autenticado

A existência do Documento Mestre da Home pública de Organizações e Coletivos não altera este estado.

```text
HOME PÚBLICA
→ aquisição / posicionamento / entrada pública

EXPERIÊNCIA AUTENTICADA DA ORGANIZAÇÃO
→ operação institucional dentro da Guivos

EXPERIÊNCIA AUTENTICADA DO COLETIVO
→ participação, governança e operação coletiva dentro da Guivos
```

São superfícies e problemas distintos.

## 10. Estado de prontidão

| Etapa | Organização | Coletivo |
|---|---|---|
| fundamento funcional | existente | existente |
| relações e limites | existente em conjunto | existente em conjunto |
| Research de supply/valor | existente | existente |
| jornada integrada | **active** | **active** |
| atores, papéis, autoridades e jobs | **definidos documentalmente** | **definidos documentalmente** |
| arquitetura de informação autenticada | **definida** | **definida** |
| mapa lógico de superfícies autenticadas | **definido documentalmente** | **definido documentalmente** |
| mapa funcional de estados autenticados | **definido documentalmente** | **definido documentalmente** |
| Priority Flows | **definidos documentalmente** | **definidos documentalmente** |
| Navigation Materialization Eligibility | **PASS / ACTIVE / CANONICAL** | **PASS / ACTIVE / CANONICAL** |
| Navigation Materialization | **DEFINED / CANONICAL DOCUMENTARY / v1.0.2** | **DEFINED / CANONICAL DOCUMENTARY / v1.0.2** |
| wireframe low-fidelity | **DELIVERY v0.1.0 + VALIDATION v1.0.0** | **DELIVERY v0.1.0 + VALIDATION v1.0.0** |
| validação de wireframe | **PASS** | **PASS** |
| high-fidelity eligibility | **PASS** | **PASS** |
| high-fidelity design authorization | **GRANTED** | **GRANTED** |
| high-fidelity execution release | **ISSUED / DELIVERY NOT_RECEIVED** | **ISSUED / DELIVERY NOT_RECEIVED** |
| UI | pendente | pendente |
| protótipo | pendente | pendente |
| testes de usabilidade | pendente | pendente |
| handoff técnico | pendente | pendente |

## 11. Absorção governada dos estados históricos de UXA-015..018

A auditoria de `F-006` recuperou o conteúdo material anterior à supersessão de `UXA-015..018` e separou **semântica necessária** de **decisão visual histórica**.

A regra de absorção é:

```text
ESTADO FUNCIONAL NECESSÁRIO
→ PRESERVADO COMO REQUISITO DE COBERTURA NO STATE MAP E PARA ETAPAS POSTERIORES

COMPOSIÇÃO / ORDEM VISUAL / COPY / CONTROLE HISTÓRICO
→ NÃO É PROMOVIDO A DECISÃO ATUAL

CONCLUSÃO HISTÓRICA DE "WIREFRAME VALIDADO"
→ NÃO É PROMOVIDA
```

### 11.1 Organização — estados que a futura materialização deverá poder acomodar

Os estados abaixo ficam absorvidos como **cobertura funcional**, sem definir tela, bloco, componente ou fluxo visual:

- operação regular sem atenção ou responsabilidade material urgente;
- Organização ainda não verificada, quando a verificação for aplicável;
- autoridade insuficiente para a ação pretendida;
- unidade ou contexto sem responsável legitimamente atribuído;
- contexto institucional incompleto;
- informações conflitantes ou contestadas;
- ausência de oportunidade ou programa ativo;
- capacidade limitada, atingida ou esgotada;
- compromisso ou obrigação material atrasada;
- risco material ou urgente;
- ausência de evidência suficiente para reconhecer avanço;
- relação institucional pausada, suspensa, contestada ou encerrada com obrigações remanescentes;
- falha de integração ou indisponibilidade de fonte, sem transformar ausência técnica em conclusão funcional;
- baixa conectividade quando relevante;
- operação legítima em múltiplos países, idiomas ou moedas.

Esses estados se conectam às autoridades atuais de contexto/autoridade, atenção derivada, oportunidades, relações, responsabilidades/evidências e estados transversais da IA e do State Map. A enumeração acima fecha lacunas de cobertura sem determinar materialização.

### 11.2 Coletivo — estados que a futura materialização deverá poder acomodar

Os estados abaixo ficam absorvidos como **cobertura funcional**, sem definir tela, bloco, componente ou fluxo visual:

- Coletivo recém-criado ou ainda sem atividade material;
- pessoa observando antes de participar;
- solicitação de entrada ou participação pendente;
- participação pausada;
- ausência de atividade próxima;
- operação regular sem necessidade ou atenção material;
- nenhuma pessoa disponível ou legitimamente responsável por uma função necessária;
- atividade ajustada, adiada, pausada ou cancelada;
- conflito de governança;
- moderação, proteção ou acessibilidade que exija atenção urgente;
- saída de responsável ou necessidade de recompor autoridade/continuidade;
- recurso insuficiente ou capacidade limitada;
- relação com Organização ou outro Coletivo contestada, suspensa ou em revisão;
- informação sensível protegida;
- ausência de evidência suficiente para reconhecer avanço ou aprendizado;
- baixa conectividade quando relevante;
- necessidade ampliada de acessibilidade;
- Coletivo em processo legítimo de encerramento, com responsabilidades remanescentes quando aplicável.

Esses estados se conectam às autoridades atuais de participação, governança/proteção, relações, aprendizados/evidências, atividade e contexto/autoridade. A enumeração acima preserva a cobertura funcional sem reativar o antigo wireframe.

A condição de pessoa observando antes de participar permanece na perspectiva da Pessoa e não é reclassificada como estado operacional interno do Coletivo.

### 11.3 Conteúdo dos históricos que permanece apenas como proveniência

Permanecem **históricos apenas**, sem autoridade atual:

- hierarquia específica e ordem dos blocos de `UXA-015/016`;
- composição desktop/mobile e qualquer associação visual dos SVGs históricos;
- nomes de seções, labels e copy aprovados apenas naquele objeto;
- exemplos de cards, controles e chamadas de ação materializadas na exploração antiga;
- decisão de quais elementos deveriam aparecer no primeiro campo visual;
- navegação proposta na composição antiga;
- cenários e exemplos usados somente para validar aquele wireframe;
- conclusões de `UXA-017/018` de que as superfícies estavam funcionalmente válidas/reformuladas;
- qualquer inferência de readiness para protótipo, UI, Design ou Engenharia.

Esses elementos podem ser consultados no histórico como evidência de exploração, mas qualquer reutilização futura exigirá nova decisão contra as autoridades então vigentes.

### 11.4 Proveniência dos produtores absorvidos

O conteúdo funcional ainda válido de `UXA-015..018` foi absorvido por autoridades posteriores; os produtores físicos e seus SVGs foram removidos.

```text
CURRENT FUNCTIONAL AUTHORITY
→ CURRENT O/C AUTHORITIES

UXA-015..018 + ASSOCIATED SVGs
→ REMOVED / HISTORICAL

PROVENANCE
→ GIT

REINTRODUCTION AS BASELINE OR DESIGN REQUIREMENT
→ PROHIBITED BY CURRENT AUTHORITY
```

Nenhum desses IDs ou antigos ativos pode voltar a operar como baseline visual, requisito de materialização ou evidência de maturidade corrente.

## 12. Regra final

> **O GKR define função, conteúdo, estados, regras, critérios, Priority Flows e Navigation Materialization documentais. O pacote low-fidelity Delivery v0.1.0 + Validation v1.0.0 é a referência visual corrente; a elegibilidade high-fidelity está `PASS`, a autorização está `GRANTED` e o release de execução externa foi `ISSUED`; a entrega high-fidelity ainda não foi recebida ou validada. Protótipo e implementação continuam sujeitos a gates próprios. Artefatos históricos não podem antecipar nem restringir essa autoridade.**