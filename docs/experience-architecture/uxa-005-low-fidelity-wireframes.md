---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.40.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-000
related:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-020
  - UXA-024
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
  - PAS-001
  - M7.64
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência para validar organização, hierarquia, conteúdo, decisão e continuidade antes de identidade visual, protótipo, teste ou implementação.

```text
contrato funcional
→ programa e priorização
→ wireframe de baixa fidelidade
→ validação funcional
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Wireframe materializado não equivale a wireframe validado.

## 2. Convenções

| Elemento | Significado |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal consciente |
| preenchimento cinza | resumo, limite ou ação indisponível |
| borda tracejada | exceção, proteção, limitação ou relação comercial |
| texto sublinhado | ação secundária ou explicação |
| rótulo anterior | origem, autoridade ou natureza comercial antes do conteúdo |
| estado textual | condição que não depende apenas de cor |
| confirmação vazia | autorização ainda não concedida |
| origem preservada | busca, categoria, recomendação, convite ou publicidade identificados |

Cor, iconografia e tipografia não possuem significado definitivo.

## 3. Cobertura do Opportunity Boost

| Família | Materializados | Validados por pacote | Pendentes |
|---|---:|---:|---:|
| configuração para computador | 5 | 5 | 0 |
| configuração móvel | 5 | 5 | 0 |
| cartão e explicação | 6 | 6 | 0 |
| Lista e Mapa patrocinados | 4 | 4 | 0 |
| gestão para computador | 6 | 6 | 0 |
| gestão móvel | 6 | 6 | 0 |
| relatório agregado | 4 | 4 | 0 |
| estados residuais | 10 | 0 | 10 |
| **Total** | **46** | **36** | **10** |

A UXA-050 preserva sua autoridade transversal histórica sobre 25 artefatos examinados naquele incremento. Ela não valida retrospectivamente artefatos posteriores.

## 4. Programa de Coletivos

A UXA-059 organiza 88 estados contratuais das UXA-056 a UXA-058 em quatro níveis:

```text
P0A — espinha dorsal
→ P0B — estados críticos
→ P1 — participação interna e operação
→ P2 — confiança, contato e proteção avançada
```

Estado contratual não equivale automaticamente a SVG.

## 5. Espinha dorsal P0A

| Ordem | Superfície | Canal inicial | Estado atual |
|---:|---|---|---|
| 1 | Explorar Coletivos | móvel | materializado e validado |
| 2 | Resultados de Busca | móvel | materializado e validado |
| 3 | Perfil Público do Coletivo | móvel | quatro SVGs materializados; validação pendente |
| 4 | Solicitação de Participação | móvel | não iniciada |
| 5 | Solicitação Pendente | móvel | não iniciada |
| 6 | Meus Coletivos | móvel | não iniciado |
| 7 | Central de Atualizações | móvel | não iniciada |
| 8 | Início do Participante | móvel | reformulação não iniciada |
| 9 | Visão Geral do Responsável | computador | não iniciada |

## 6. Descoberta e busca de Coletivos

As UXA-060 e UXA-061 governam cinco SVGs móveis:

- Explorar Coletivos;
- resultados de busca;
- filtros;
- busca sem resultados;
- explicação de origem e publicidade.

Cobertura: **5 materializados, 5 validados e 0 pendente**.

## 7. Perfil Público do Coletivo

A UXA-062 materializa quatro estados:

1. entrada aberta;
2. entrada mediante aprovação;
3. entradas temporariamente indisponíveis;
4. apresentação protegida.

Cobertura: **4 materializados, 0 validados e 4 pendentes**.

A família demonstra:

- origem orgânica, publicidade ou convite;
- propósito e funcionamento;
- território, modalidade e acessibilidade;
- acompanhar separado de participar;
- regras e condições anteriores ao vínculo;
- contagens governadas e lista protegida;
- responsáveis e relações institucionais limitadas;
- reputação suficiente, insuficiente ou suprimida;
- denúncia, proteção e compartilhamento permitido.

## 8. Cobertura consolidada de Coletivos

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| descoberta e busca | 5 | 5 | 0 |
| Perfil Público | 4 | 0 | 4 |
| demais famílias | 0 | 0 | não materializadas |
| **Total visual atual** | **9** | **5** | **4** |

As contagens de Coletivos permanecem separadas das contagens do Opportunity Boost.

## 9. Limite recomendado por incremento

Por padrão, cada pacote deverá possuir:

- até três superfícies principais;
- até seis SVGs, incluindo estados alternativos;
- uma responsabilidade dominante;
- um canal principal;
- matriz explícita de cobertura;
- estados incluídos e excluídos;
- validação funcional antes de ampliar a família seguinte.

## 10. Regra para novo SVG

Um novo SVG somente será criado quando houver mudança material de:

- hierarquia;
- decisão principal;
- autoridade;
- público ou visibilidade;
- dados expostos;
- consequência;
- proteção;
- continuidade;
- canal;
- recuperação após falha.

## 11. Próxima transição

A próxima transição especializada é:

> **UXA-063 — Validação Funcional e Reformulação do Perfil Público Móvel do Coletivo**

Ela deverá validar os quatro SVGs antes de qualquer início da Solicitação de Participação.

## 12. Fronteiras preservadas

Não estão iniciados por este programa:

- protótipo navegável;
- teste com pessoas;
- identidade visual;
- componentes técnicos;
- algoritmo de busca ou reputação;
- política jurídica;
- Engenharia de Produto.
