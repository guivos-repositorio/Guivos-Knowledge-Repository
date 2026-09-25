---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: active
version: 0.23.5
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
related:
  - PAS-001-DOMAIN-MODEL-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-UX-PER002-MASTER-001
  - GKR-UX-PER003-MASTER-001
  - GKR-UX-PER004-MASTER-001
  - GKR-UX-PER005-MASTER-001
normative: false
---

# Jornada Integrada da Pessoa

## 1. Entrada e compreensão

```text
HOME PÚBLICA
→ ENTRADA PROTEGIDA
→ EXPRESSÃO GUIADA
→ COMPREENSÃO INICIAL
→ HOJE
```

A entrada não presume avanço, urgência, diagnóstico, prioridade ou objetivo. A experiência deve usar somente contexto confirmado, autorizado e vigente.

## 2. Domínios de Evolução

A Pessoa pode relacionar zero, um ou vários Domínios de Evolução. Domínio é contexto, não score, diagnóstico ou prioridade automática.

`Ainda estou descobrindo` permanece estado legítimo.

## 3. Hoje, Objetivos, Próximos Passos e Evolução

```text
PER-008 — HOJE
├── PER-010 — MEUS OBJETIVOS
├── PER-011 — MEUS PRÓXIMOS PASSOS
└── PER-012 — MINHA EVOLUÇÃO
```

- Objetivos preservam intenção, revisão e prioridade declarada;
- Próximos Passos preservam prontidão, dependência e possibilidade de recusa;
- Evolução preserva incerteza, interpretação revisável e privacidade;
- retorno a Hoje não confirma, conclui ou altera automaticamente nenhum objeto.

## 4. Oportunidades

```text
MAPA ↔ LISTA
→ DETALHE
→ REVISÃO CONSCIENTE
→ FRONTEIRA EXTERNA
```

A saída para terceiro exige informação suficiente, ação afirmativa e minimização de dados. Resultado posterior pertence ao terceiro.

## 5. Planos

Pessoa usa `Free · Plus · Pro`.

Abrir Planos não seleciona tier, não inicia cobrança e não altera contexto da Journey.

## 6. Coletivos

A Pessoa pode descobrir Coletivos, consultar perfil público, solicitar participação, acompanhar solicitação, acessar seus Coletivos e receber atualizações conforme autoridade e vínculo.

Participação não cria exposição ilimitada de contexto pessoal.

## 7. Proteções

- autonomia da Pessoa;
- privacidade por finalidade;
- explicabilidade proporcional;
- correlação distinta de causalidade;
- ausência de score humano;
- nenhum avanço inferido apenas por uso da interface.

## 8. Documentação por superfície para Design e IA

A Jornada da Pessoa possui uma coleção própria de documentação de consumo para Design, construída **uma superfície por vez**.

Entrada:

- `GKR-UX-PERSON-JOURNEY-READ-FIRST-001` — regras de consumo, granularidade e liberdade criativa;
- `GKR-UX-PERSON-JOURNEY-FLOW-001` — mapa completo das 26 superfícies/responsabilidades a documentar após a Home;
- `GKR-UX-PER002-MASTER-001` — Documento Mestre de `PER-002 — Entrada Protegida`;
- `GKR-UX-PER003-MASTER-001` — Documento Mestre de `PER-003 — Escolha de Modalidade`;
- `GKR-UX-PER004-MASTER-001` — Documento Mestre de `PER-004 — Expressão por Texto ou Voz`;
- `GKR-UX-PER005-MASTER-001` — Documento Mestre de `PER-005 — Inventário e Autorização`.

A coleção não cria telas por inferência. Cada Documento Mestre deve corresponder a uma superfície/responsabilidade já reconhecida pelo Registry e preservar estados internos dentro dessa mesma responsabilidade quando não existir novo `PER-ID`.

Para prototipação e Design, continuar usando:

- `GKR-JOURNEY-SCREEN-CATALOG-001`;
- `GKR-JOURNEY-SURFACE-REGISTRY-001`;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
- Documento Mestre da superfície, quando já construído;
- contratos específicos somente quando a superfície exigir.

## 9. Estado

```text
PERSON JOURNEY VIEW
→ CURRENT

VISUAL MATERIALIZATION
→ DESIGN-OWNED

IMPLEMENTATION
→ SEPARATE
```
