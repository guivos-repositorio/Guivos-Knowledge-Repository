---
id: UXA-083
title: Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-082
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.56.0
normative: false
---

# Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção

## 1. Finalidade

A UXA-083 corrige os cinco bloqueios registrados pela UXA-082 sem modificar os 97 SVGs canônicos e sem iniciar a materialização de qualquer lacuna.

## 2. Base

```text
main
a8bdfc9da19410133222af332f4769c986cad5d4
```

## 3. Escopo executado

1. reordenação da página da Pessoa;
2. separação entre Home pública e Tela Hoje;
3. criação de uma rota canônica entre as cinco páginas;
4. criação de matriz individual para os 97 SVGs;
5. sincronização das versões e dos resumos documentais.

## 4. Ordem funcional da Pessoa

Antes:

```text
Home pública + Tela Hoje
→ início protegido
→ compreensão inicial
→ expressão guiada
```

Depois:

```text
Home pública
→ início protegido
→ expressão guiada
→ compreensão inicial
→ Tela Hoje
```

A reformulação corrige a leitura, mas não altera o estado `não examinada` de `GKR-TRN-007`.

## 5. Rota integrada de inspeção

A galeria passa a oferecer navegação anterior, índice, matriz e próxima página:

```text
Pessoa
→ Organização e Oportunidades
→ Coletivos
→ Opportunity Boost — Configuração e Exposição
→ Opportunity Boost — Operação, Relatórios e Resíduos
```

Essa rota organiza a auditoria documental. Ela não declara uma única jornada de produto.

## 6. Matriz por SVG

Foi criado `GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001`, contendo:

- 23 perfis documentais de rastreabilidade;
- associação individual dos 97 arquivos;
- superfície ou responsabilidade;
- entrada;
- saída;
- retorno ou interrupção;
- lacuna;
- validação de origem.

O uso de perfis evita repetir descrições e, ao mesmo tempo, impede que um arquivo permaneça sem associação explícita.

## 7. Resolução dos achados da UXA-082

| Achado | Estado após UXA-083 |
|---|---|
| F01 — ordem incorreta da Pessoa | resolvido documentalmente |
| F02 — Home e Tela Hoje agrupadas | resolvido documentalmente |
| F03 — ausência de rota integrada | resolvido documentalmente |
| F04 — rastreabilidade apenas agrupada | resolvido por associação individual a perfis |
| F05 — versões divergentes | resolvido nos instrumentos sincronizados |

## 8. Estado dos objetos

| Objeto | Estado |
|---|---|
| Galeria Visual Integrada | `draft` 0.3.0; reformulada |
| cinco páginas visuais | `draft` 0.2.0 |
| matriz por SVG | `draft` 0.1.0 |
| Catálogo Integrado | `active` 0.8.0 |
| registro de lacunas | `active` 0.8.0 |
| 97 SVGs | inalterados |
| 87 validações locais | preservadas |
| 10 estados da UXA-055 | pendentes |
| jornadas principais | `draft` |
| protótipo e Engenharia de Produto | não iniciados |

## 9. Lacunas não iniciadas

A prioridade futura de Coletivos permanece:

```text
GKR-SURF-COL-002 — Visão Geral do Responsável
→ GKR-SURF-COL-003 — gestão completa de solicitações
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

Nenhuma dessas superfícies é criada, desenhada ou promovida por este pacote.

## 10. Veredito do incremento

**Reformulação executada. Revalidação ainda necessária.**

A galeria não é promovida por este pacote. A assertividade da nova ordem, da rota e da matriz deverá ser examinada por ato separado.

## 11. Limites

A UXA-083 não:

- altera SVGs;
- cria telas;
- fecha lacunas;
- valida jornadas ponta a ponta;
- promove a galeria;
- inicia protótipo;
- inicia teste com pessoas;
- inicia aplicação, motor ou Engenharia de Produto.

## 12. Próxima transição possível

**UXA-084 — Revalidação Funcional e Visual da Galeria Integrada Reformulada**, mediante autorização separada.
