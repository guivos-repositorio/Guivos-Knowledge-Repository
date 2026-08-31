---
id: GKR-UX-ORGCOL-UX-STATE-001
title: Organizações e Coletivos — Estado de UX e Wireframes
status: active
version: 1.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-30
normative: false
related:
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - UXA-014
  - UXA-019
---

# Organizações e Coletivos — Estado de UX e Wireframes

## 1. Decisão de estado

O estado vigente é:

> **Os wireframes da experiência autenticada de Organizações e Coletivos ainda não foram definidos.**

Isso vale para, no mínimo:

- visão geral / início da Organização autenticada;
- visão geral / início do Coletivo autenticado;
- arquitetura final de navegação interna;
- hierarquia visual das superfícies;
- composição de componentes;
- estados responsivos;
- protótipo navegável;
- UI final;
- testes de usabilidade dessas superfícies.

Atores, papéis, autoridades, jobs prioritários e a Arquitetura da Informação autenticada já foram definidos documentalmente em instrumentos posteriores. Esse avanço **não equivale** a mapa final de superfícies, wireframe, UI, protótipo ou implementação.

## 2. O que já existe e pode alimentar a futura UX

A ausência de wireframe não significa ausência de fundamento.

Já existem insumos e autoridades documentais relevantes:

- `UXA-014` — fundação funcional de Organizações e Coletivos;
- `UXA-019` — contrato funcional das relações Organização ↔ Coletivo;
- `GKR-UX-ORGCOL-AUTH-JOBS-001` — atores, papéis, autoridades e jobs prioritários da experiência autenticada;
- `GKR-UX-ORGCOL-AUTH-IA-001` — Arquitetura da Informação autenticada definida em estado pré-mapa de superfícies;
- Jornadas integradas da Organização e do Coletivo em estado `draft`;
- contratos de oportunidades, publicação, descoberta e relações;
- Documento Mestre da Home pública de Organizações e Coletivos;
- `RP-002` — Research sobre supply, papéis, rede, valor e modelo econômico.

Esses materiais são **inputs para a construção futura da UX**, não wireframes implícitos. A definição documental de Jobs e IA não autoriza inferir mapa final de superfícies ou decisões visuais.

## 3. Correção dos registros anteriores

Foram encontrados quatro documentos históricos que davam a entender que os wireframes já existiam e estavam validados:

- `UXA-015` — Visão Geral da Organização;
- `UXA-016` — Início do Coletivo;
- `UXA-017` — validação da Visão Geral da Organização;
- `UXA-018` — validação do Início do Coletivo.

Esses registros foram produzidos prematuramente e **não representam mais o estado vigente**.

A reconciliação atual estabelece:

```text
UXA-015 → registro histórico superseded
UXA-016 → registro histórico superseded
UXA-017 → registro histórico superseded
UXA-018 → registro histórico superseded
```

Os SVGs associados permanecem apenas como histórico técnico no repositório e não devem ser utilizados como especificação, referência aprovada, baseline de produto ou autoridade de design.

## 4. O que não pode ser inferido

Não é permitido concluir, a partir de material histórico ou da IA documental já definida, que já estejam definidos:

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

## 5. Separação entre arquitetura funcional, IA e wireframe

Uma arquitetura funcional e uma Arquitetura da Informação podem afirmar que a experiência precisa preservar:

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

Essas decisões pertencem às etapas posteriores de mapa de superfícies, arquitetura de experiência e wireframing ainda pendentes.

## 6. Sequência obrigatória quando a frente avançar

A construção deverá continuar do estado documental vigente, e não dos SVGs históricos:

1. fundamentos, Research e jornadas vigentes — reconciliados documentalmente;
2. atores, papéis, autoridades e jobs prioritários — definidos em `GKR-UX-ORGCOL-AUTH-JOBS-001`;
3. Arquitetura da Informação — definida em `GKR-UX-ORGCOL-AUTH-IA-001`, em estado pré-mapa de superfícies;
4. definir e validar documentalmente o mapa de superfícies;
5. definir fluxos prioritários e estados críticos;
6. construir wireframes de baixa fidelidade **somente quando essa materialização estiver autorizada**;
7. validar funcionalmente os wireframes reais;
8. reformular quando necessário;
9. avançar para UI somente quando autorizado;
10. construir protótipo somente quando autorizado;
11. testar com Pessoas / representantes reais;
12. somente depois preparar handoff técnico.

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

> **não existe validação vigente de wireframe da Organização ou do Coletivo enquanto os respectivos wireframes oficiais não forem construídos.**

A futura validação deverá ocorrer contra o objeto então vigente e contra os fundamentos e contratos atualizados naquele momento.

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
| jornada integrada | draft | draft |
| atores, papéis, autoridades e jobs | **definidos documentalmente** | **definidos documentalmente** |
| arquitetura de informação autenticada | **definida — pré-mapa de superfícies** | **definida — pré-mapa de superfícies** |
| mapa final de superfícies | pendente | pendente |
| wireframe | **pendente** | **pendente** |
| validação de wireframe | **pendente** | **pendente** |
| UI | pendente | pendente |
| protótipo | pendente | pendente |
| testes de usabilidade | pendente | pendente |
| handoff técnico | pendente | pendente |

## 11. Absorção governada dos estados históricos de UXA-015..018

A auditoria de `F-006` recuperou o conteúdo material anterior à supersessão de `UXA-015..018` e separou **semântica necessária** de **decisão visual histórica**.

A regra de absorção é:

```text
ESTADO FUNCIONAL NECESSÁRIO
→ PODE SER PRESERVADO COMO REQUISITO PRÉ-SURFACE-MAP

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

Esses estados se conectam às autoridades atuais de contexto/autoridade, atenção derivada, oportunidades, relações, responsabilidades/evidências e estados transversais da IA. A enumeração acima fecha lacunas de cobertura sem determinar materialização.

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

### 11.4 Efeito sobre F-006

Com esta absorção, `UXA-015..018` deixam de ser necessários como fonte vigente para os **estados funcionais** recuperados pela auditoria. A auditoria posterior também concluiu a reconciliação das dependências funcionais ativas encontradas e comprovou a elegibilidade documental de cleanup. Isso **não autoriza sua remoção física automaticamente**.

Estado vigente:

```text
F-006
→ OPEN
→ ABSORPTION_APPLIED
→ ACTIVE_FUNCTION_DEPENDENCIES_RECONCILED
→ CLEANUP_ELIGIBILITY_PROVEN
→ PHYSICAL_REMOVAL_NOT_AUTHORIZED
```

Os gates documentais de absorção material e reconciliação das dependências funcionais já estão concluídos. Antes de qualquer cleanup físico ainda é obrigatório:

1. obter autorização humana separada e explícita para a remoção física;
2. se autorizada a remoção, reconciliar na mesma transação links, catálogo, gallery, registry e traceability afetados;
3. recomputar as contagens físicas e associações após a eventual remoção dos dois SVGs;
4. validar semanticamente e mecanicamente o corpus no novo head exato;
5. executar nova revisão repo-wide no novo head;
6. preservar a proveniência histórica no Git;
7. somente então decidir o fechamento de `F-006` e o fechamento formal de H/I.

Até a conclusão desses passos, os quatro documentos `UXA-015..018` e os SVGs associados permanecem fisicamente preservados e não devem ser tratados como autoridade funcional vigente.

## 12. Regra final

> **Nenhum artefato histórico deve antecipar o estado de maturidade da experiência. Primeiro definimos; depois materializamos; depois validamos.**
