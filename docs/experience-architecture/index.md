---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.70.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - UXA-038
  - UXA-050
  - UXA-055
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
  - UXA-069
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.72
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório em experiências compreensíveis para Pessoas, Coletivos e Organizações.

Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design visual ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização visual ou documental
→ validação funcional
→ reformulação, quando exigida
→ nova validação
→ promoção controlada, quando aplicável
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Jornada pessoal — início protegido

| Responsabilidade | Autoridade |
|---|---|
| contrato do início protegido | UXA-020; UXA-023 |
| escolha, rascunho, revisão e autorização | UXA-034; UXA-035 |
| processamento e compreensão inicial | UXA-036; UXA-037 |
| expressão guiada por texto e voz | UXA-068 |
| validação da expressão guiada | UXA-069 |

### 3.1 Cobertura relacionada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Início protegido geral | 4 | 4 | 0 |
| Compreensão inicial | 5 | 5 | 0 |
| Expressão Guiada do Momento Atual | 8 | 8 | 0 |
| **Subtotal relacionado** | **17** | **17** | **0** |

A contagem permanece separada das famílias de Coletivos e Opportunity Boost e não comprova validação ponta a ponta da jornada integrada.

## 4. Decisões da expressão guiada preservadas

- conteúdo de origem separado da ajuda temporária;
- ajuda somente após solicitação consciente;
- texto e voz equivalentes;
- rascunho sem análise ou salvamento implícitos;
- gravação e transcrição com finalidade limitada;
- interrupção, descarte e retorno com efeitos conhecidos;
- síntese identificada como derivada;
- inventário e autorização antes do processamento material.

## 5. Autoridades dos Coletivos

| Responsabilidade | Autoridade |
|---|---|
| descoberta, Perfil Público e participação | UXA-056 |
| avaliação e reputação contextual | UXA-057 |
| interação, recomendação, contato e proteção | UXA-058 |
| programa e priorização de wireframes | UXA-059 |
| descoberta e busca móvel | UXA-060; UXA-061 |
| Perfil Público móvel | UXA-062; UXA-063 |
| revisão e solicitação móvel | UXA-064; UXA-065 |
| Solicitação Pendente móvel | UXA-066; UXA-067 |

## 6. Estado visual dos Coletivos

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| descoberta e busca | 5 | 5 | 0 |
| Perfil Público | 4 | 4 | 0 |
| revisão e solicitação | 5 | 5 | 0 |
| Solicitação Pendente | 8 | 8 | 0 |
| **Total de Coletivos** | **22** | **22** | **0** |

As 22 referências cobrem principalmente a perspectiva da Pessoa. `Meus Coletivos`, Central de Atualizações, Início do Participante reformulado, Visão Geral do Responsável e a operação bilateral permanecem ausentes.

## 7. Programa e evolução das Jornadas Integradas

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — validação funcional não aprovada até reformulação
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — revalidação aprovada com ressalvas no escopo documental
→ UXA-075 — promoção seletiva e sincronização pós-validação executadas
→ UXA-076 — registros granulares materializados em draft
→ UXA-077 — validação granular não aprovada até correção obrigatória
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante institucional, especialista, anunciante e patrocinador são perspectivas, papéis ou operadores contextuais, não novos participantes estruturais.

## 8. Modelo de evidência vigente

Cada nó, superfície ou família deve separar:

| Campo | Função |
|---|---|
| maturidade primária | um único estado controlado da UXA-070 |
| autoridade contratual | contrato ou programa que governa a responsabilidade |
| referência materializada | documento, wireframe ou SVG existente |
| evidência de validação | pacote que validou a referência materializada |
| continuidade integrada | validada, parcial, ausente ou não examinada |

```text
cobertura das superfícies
≠ cobertura das transições
≠ validação da jornada integrada
```

## 9. Registros granulares

A UXA-076 materializou:

- `GKR-JOURNEY-SURFACE-REGISTRY-001` — 36 superfícies, estados, responsabilidades ou ausências conhecidas;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001` — 34 transições documentais.

Os IDs seguem:

```text
GKR-SURF-<PARTICIPANTE>-NNN
GKR-TRN-NNN
```

A atribuição de ID não equivale a implementação, validação ou completude.

## 10. Resultado da UXA-077

[UXA-077 — Validação Funcional do Registro Granular](uxa-077-granular-registry-functional-validation.md) emitiu o parecer:

> **não aprovado até correção obrigatória**

### 10.1 Aspectos confirmados

- 36 entradas de superfície ou responsabilidade;
- 34 transições;
- IDs sem duplicidade dentro dos registros;
- maturidade aderente ao vocabulário da UXA-070;
- incertezas e lacunas preservadas;
- nenhum avanço técnico ou promocional implícito.

### 10.2 Achados obrigatórios

1. endpoints sem ID estável em `GKR-TRN-205` e `GKR-TRN-304`;
2. mistura entre busca de Coletivos e descoberta de oportunidades;
3. mistura entre estado institucional de publicação e Detalhe de Oportunidade;
4. referência incorreta dos dez estados residuais, cuja fonte é UXA-055;
5. campos obrigatórios ausentes no registro de superfícies.

Os registros permanecem `draft` até reformulação e nova validação.

## 11. Reutilização canônica

- artefatos são referenciados por ID, caminho e versão;
- arquivos canônicos permanecem em modo somente leitura;
- uma mesma referência pode aparecer em várias perspectivas sem cópia;
- nenhuma ligação é criada por proximidade visual ou numeração;
- inclusão no ambiente não altera maturidade, prioridade ou canonicidade;
- Opportunity Boost permanece camada comercial identificada, não participante ou autoridade.

## 12. Continuidade governada

### 12.1 Jornada pessoal

A ligação entre compreensão inicial e Tela Hoje permanece não examinada como conjunto e registrada como `GKR-TRN-007`.

### 12.2 Coletivos P0A

As cinco primeiras referências possuem materialização e validação na perspectiva coberta. As seguintes permanecem lacunas. `GKR-SURF-PER-102` representa busca de Coletivos e não poderá ser usada como busca de oportunidades.

### 12.3 Organização e Coletivo

A relação está contratada pela UXA-019 e registrada granularmente, mas não possui materialização bilateral específica validada.

### 12.4 Oportunidades

A reformulação futura deverá separar:

- estado institucional de publicação;
- mapa, lista ou cartão de oportunidade;
- Detalhe de Oportunidade percebido pela Pessoa;
- fronteira externa identificada.

## 13. Estado da seção documental

| Artefato | Estado |
|---|---|
| navegação de primeiro nível | active |
| visão geral | active |
| Pessoa, Coletivo e Organização | draft por incompletude explícita |
| handoffs | active como matriz resumida governada |
| cenários | active como hipóteses documentais governadas |
| catálogo | active como inventário agregado |
| lacunas | active, observacional e não promocional |
| registro granular de superfícies | draft; validação não aprovada |
| registro granular de transições | draft; validação não aprovada |
| reformulação granular | não iniciada |
| protótipo ou aplicação | não iniciados |

## 14. Decisões estruturais preservadas

- compartilhar pouco não é falha;
- digitar não solicita análise automática;
- gravar autoriza somente a operação apresentada;
- transcrição automática não é declaração confirmada;
- ajuda temporária não cria compreensão;
- síntese não substitui fonte;
- desconhecido não é fato;
- personalização depende de gates próprios;
- solicitação não é aprovação;
- convite não cria vínculo;
- publicidade não compra relevância, reputação ou autoridade;
- superfície validada não equivale a jornada integrada validada;
- atribuição de ID não equivale a implementação;
- status `active` não equivale a completude.

## 15. Próxima evolução documental possível

**UXA-078 — Reformulação Controlada dos Registros Granulares de Transições e Superfícies**, mediante autorização separada.

A UXA-078, a nova validação posterior, protótipo, testes e Engenharia de Produto não estão iniciados.
