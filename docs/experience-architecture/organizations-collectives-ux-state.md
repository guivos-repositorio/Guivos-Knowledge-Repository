---
id: GKR-UX-ORGCOL-UX-STATE-001
title: Organizações e Coletivos — Estado de UX e Wireframes
status: active
version: 1.1.0
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

## 11. Regra final

> **Nenhum artefato histórico deve antecipar o estado de maturidade da experiência. Primeiro definimos; depois materializamos; depois validamos.**
