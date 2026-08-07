---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.10.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-005
  - UXA-070
  - UXA-075
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **106 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-091 acrescenta a referência móvel de `GKR-SURF-PER-106 — Meus Coletivos` e reformula o estado aprovado da família `PER-105` para tornar a continuidade pós-aprovação explícita.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que suas transições ou jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 106 SVGs compartilham 26 perfis de rastreabilidade;
- 11 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- 12 SVGs aguardam validação específica;
- dez desses 12 são estados residuais da UXA-055;
- o estado aprovado corrente de `PER-105` foi reformulado e aguarda revalidação;
- o novo `PER-106` está materializado e aguarda validação;
- `GKR-TRN-108` permanece parcial;
- `GKR-TRN-110` permanece parcial por ausência de `PER-107`;
- as cinco transições validadas pela UXA-090 permanecem integralmente validadas.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md) — uma associação para cada um dos 106 arquivos;
- [Catálogo Integrado de Telas](screen-catalog.md) — visão agregada por família;
- [Registro Granular de Superfícies e Estados](surface-registry.md);
- [Registro Granular de Transições](transition-registry.md);
- [Lacunas e Continuidades Ausentes](gaps.md).

## 4. Rota canônica de inspeção

A rota abaixo organiza a leitura documental. Ela não representa uma única jornada de produto.

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | 19 | Home → início protegido → expressão → compreensão → Tela Hoje |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação institucional → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 32 | descoberta → perfil → solicitação → pendência → gestão responsável → resultado aprovado → Meus Coletivos |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → ativação → exposição identificada → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **106** | **94 validados funcionalmente; 12 pendentes** |

As páginas são instrumentos documentais ativos. A presença ou a validação de um SVG não valida automaticamente a continuidade que ele representa.

## 5. Sequências funcionais destacadas

### Pessoa

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada
→ inventário e autorização
→ processamento
→ compreensão inicial revisável
→ Tela Hoje
```

A passagem final continua `não examinada` como conjunto.

### Organização e oportunidades

```text
Visão Geral da Organização
→ cadastro e ativação
→ mapa
→ lista sincronizada
→ detalhe
→ fronteira externa
```

A publicação e a descoberta permanecem em pacotes distintos.

### Coletivos

```text
explorar e buscar
→ Perfil Público
→ revisão e solicitação
→ Solicitação Pendente
→ Visão Geral do Responsável
→ gestão de solicitações
→ resultado aprovado em PER-105
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

`PER-106` agora possui referência própria. O estado aprovado de `PER-105` e `PER-106` aguardam validação na versão corrente. `PER-107` permanece ausente e `PER-108` continua com reformulação pendente.

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 106 |
| associações individuais | 106 |
| perfis de rastreabilidade | 26 |
| com validação funcional vigente | 94 |
| pendentes de validação específica | 12 |
| IDs com referência visual direta ou agrupada | 28 de 40 |
| responsabilidades sem SVG dedicado | 11 |
| fronteira documental sem tela por definição | 1 |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-PER-107` — Central de Atualizações;
- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-091

A UXA-091:

- adiciona `uxa-091-my-collectives-mobile.svg`;
- mantém o inventário granular em 40 superfícies e 37 transições;
- aumenta cobertura visual de 105 para 106 SVGs;
- aumenta perfis de 25 para 26;
- aumenta IDs com referência visual de 27 para 28;
- reduz responsabilidades sem SVG de 12 para 11;
- reduz validações vigentes de 95 para 94 porque uma versão previamente validada de `PER-105` foi reformulada e precisa ser reexaminada;
- eleva pendências de 10 para 12 ao somar a versão aprovada reformulada e o novo `PER-106`;
- preserva `TRN-108` e `TRN-110` como parciais.

## 9. Estado

A galeria está `active` 0.10.0. A página de Coletivos está `active` 0.8.0 e a matriz por SVG está `active` 0.8.0 no pacote proposto pela UXA-091.

O status `active` aprova somente os instrumentos documentais de inspeção. Não valida jornadas ponta a ponta, não inicia protótipo ou Engenharia de Produto e não autoriza UXA-092 automaticamente.

## 10. Próxima transição possível

**UXA-092 — Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação**, mediante autorização separada.

A UXA-092 não é iniciada por esta atualização da galeria.
