---
id: GKR-UX-ORGCOL-UX-STATE-001
title: Organizações e Coletivos — Estado de UX e Wireframes
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-26
normative: false
related:
  - GKR-UX-ORGCOL-STATE-001
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

## 2. O que já existe e pode alimentar a futura UX

A ausência de wireframe não significa ausência de fundamento.

Já existem insumos relevantes:

- `UXA-014` — fundação funcional de Organizações e Coletivos;
- `UXA-019` — contrato funcional das relações Organização ↔ Coletivo;
- Jornadas integradas da Organização e do Coletivo em estado `draft`;
- contratos de oportunidades, publicação, descoberta e relações;
- Documento Mestre da Home pública de Organizações e Coletivos;
- `RP-002` — Research sobre supply, papéis, rede, valor e modelo econômico.

Esses materiais são **inputs para a construção futura da UX**, não wireframes implícitos.

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

Não é permitido concluir, a partir de material histórico, que já estejam definidos:

- dashboard da Organização;
- Home autenticada da Organização;
- Home autenticada do Coletivo;
- menu interno;
- cards prioritários;
- ordem final dos blocos;
- ações principais;
- densidade de informação;
- layout desktop ou mobile;
- estados vazios;
- estados de permissão;
- fluxos de administração;
- modelo final de gestão de membros;
- sistema final de governança;
- componentes reutilizáveis;
- padrões visuais.

## 5. Separação entre arquitetura funcional e wireframe

Uma arquitetura funcional pode afirmar que a experiência precisa preservar:

- autoridade;
- autonomia;
- voluntariedade;
- transparência;
- responsabilidade;
- evidência;
- contestação;
- proteção;
- clareza de papéis.

Isso não determina automaticamente:

```text
onde cada elemento aparece
→ em qual tela
→ em qual ordem
→ com qual componente
→ com qual densidade
→ com qual interação
→ com qual linguagem visual
```

Essas decisões pertencem à etapa de arquitetura de experiência e wireframing ainda pendente.

## 6. Sequência obrigatória quando a frente for retomada

A construção deverá recomeçar do estado atual, e não dos SVGs históricos:

1. reconciliar fundamentos, Research e jornadas vigentes;
2. definir atores, papéis, autoridades e jobs prioritários;
3. definir arquitetura da informação;
4. definir mapa de superfícies;
5. definir fluxos prioritários e estados críticos;
6. construir wireframes de baixa fidelidade;
7. validar funcionalmente os wireframes reais;
8. reformular quando necessário;
9. avançar para UI;
10. construir protótipo;
11. testar com Pessoas / representantes reais;
12. somente depois preparar handoff técnico.

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
| arquitetura de informação autenticada | pendente | pendente |
| mapa final de superfícies | pendente | pendente |
| wireframe | **pendente** | **pendente** |
| validação de wireframe | **pendente** | **pendente** |
| UI | pendente | pendente |
| protótipo | pendente | pendente |
| testes de usabilidade | pendente | pendente |
| handoff técnico | pendente | pendente |

## 11. Regra final

> **Nenhum artefato histórico deve antecipar o estado de maturidade da experiência. Primeiro definimos; depois materializamos; depois validamos.**