---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-005
  - UXA-070
  - UXA-075
  - UXA-080
  - UXA-081
  - UXA-082
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os 97 SVGs existentes em `docs/assets/wireframes/` para inspeção humana de assertividade, coerência e cobertura.

Os arquivos permanecem em seus caminhos canônicos e são incorporados por referência. A galeria não modifica SVGs, valida transições, fecha lacunas, promove jornadas ou autoriza implementação.

## 2. Abrir as galerias

| Grupo | SVGs | Estado |
|---|---:|---|
| [Pessoa — Fundação, Entrada e Compreensão](screen-gallery-person.md) | 19 | validados nos pacotes de origem; ordem integrada pendente de correção |
| [Oportunidades e Organização](screen-gallery-opportunities-organization.md) | 9 | validados nos pacotes de origem; continuidade integrada pendente |
| [Coletivos](screen-gallery-collectives.md) | 23 | validados nas perspectivas cobertas; operação do responsável ausente |
| [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | validados nos pacotes de origem |
| [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | 16 validados e 10 pendentes |
| **Total** | **97** | **87 validados e 10 pendentes** |

A divisão em páginas evita sobrecarga de renderização e mantém um único ponto de entrada para a inspeção.

## 3. Auditoria

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual direta ou agrupada | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |

A quantidade de SVGs não equivale à quantidade de superfícies: estados alternativos e dispositivos podem compartilhar a mesma responsabilidade granular.

## 4. Responsabilidades sem SVG dedicado

- `GKR-SURF-PER-106` — Meus Coletivos;
- `GKR-SURF-PER-107` — Central de Atualizações;
- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-002` — Visão Geral do Responsável;
- `GKR-SURF-COL-003` — gestão de solicitações na origem operacional;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008` — operação interna e institucional do Coletivo;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007` — relação com Coletivos e resultados institucionais.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 5. Resultado da UXA-082

**Veredito: não aprovada para promoção até reformulação controlada.**

A galeria permanece válida como inventário visual e ponto central de acesso. A validação identificou cinco achados:

1. a página da Pessoa não segue a ordem funcional registrada;
2. Home pública e Tela Hoje estão agrupadas apesar de ocuparem momentos distintos;
3. não existe rota integrada de inspeção entre as cinco páginas;
4. a associação agrupada não informa o papel de cada SVG na entrada, decisão, saída, retorno ou interrupção;
5. resumos documentais ainda registravam a versão anterior da galeria.

A ordem funcional esperada para a jornada pessoal é:

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

A estrutura atual não deve ser interpretada como essa sequência.

## 6. Prioridade governada de continuidade

A primeira frente futura de novas telas será a continuidade operacional de Coletivos, respeitando dependências:

| Ordem | Superfície | ID |
|---:|---|---|
| 1 | Visão Geral do Responsável | GKR-SURF-COL-002 |
| 2 | gestão completa de solicitações | GKR-SURF-COL-003 |
| 3 | Meus Coletivos | GKR-SURF-PER-106 |
| 4 | Central de Atualizações | GKR-SURF-PER-107 |
| 5 | Início do Participante | GKR-SURF-PER-108 |

Essa decisão não inicia materialização. Antes dela, a própria galeria deverá ser reformulada e revalidada.

## 7. Dívidas de validação separadas

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- erros, retornos e interrupções integrados.

Esses itens não devem ser confundidos com ausência de novas telas.

## 8. Estado

A galeria e suas páginas permanecem `draft`. Sua presença na navegação não aprova assertividade visual, continuidade integrada ou prontidão de produto.

## 9. Próxima transição possível

**UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção.**

A UXA-083 exige autorização separada.
