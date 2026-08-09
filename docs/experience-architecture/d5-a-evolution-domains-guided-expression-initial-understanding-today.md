---
id: GKR-UX-D5-A-001
title: Materialização Controlada dos Domínios de Evolução na Jornada Inicial
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-000
normative: false
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001
  - UXA-006
  - UXA-010
  - UXA-011-A1
  - UXA-036
  - UXA-037
  - UXA-068
  - UXA-069
  - UXA-097
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
---

# GKR-UX-D5-A-001 — Materialização Controlada dos Domínios de Evolução na Jornada Inicial

## 1. Finalidade

Esta frente materializa, na Arquitetura da Experiência, o eixo canônico de **Domínios de Evolução** definido por `PAS-001-DOMAIN-MODEL-001`, exclusivamente nos pontos da jornada inicial em que a área pode apoiar compreensão sem criar classificação obrigatória, score, diagnóstico ou identidade permanente.

O recorte D5-A cobre somente:

1. `PER-004 — Expressão Guiada do Momento Atual`;
2. `PER-007 — Compreensão Inicial`;
3. `PER-008 — Hoje`.

A materialização é feita **in-place** em SVGs já existentes. Não cria nova superfície, estado granular, fronteira ou transição.

## 2. Autoridade e precedência

A autoridade semântica permanece em `PAS-001-DOMAIN-MODEL-001`.

Esta frente não redefine os nove domínios, não cria décimo domínio e não altera o contrato semântico `domain_link`.

Para fins de experiência:

```text
Domínio de Evolução
= contexto semântico sobre o que a jornada está tratando
≠ diagnóstico
≠ identidade
≠ objetivo
≠ Próximo Passo
≠ evidência
≠ evolução
≠ score
```

A formulação pública deverá usar o nome do domínio, e não o identificador interno `JED-*`.

## 3. Decisão estrutural

A D5-A adota três níveis de materialização:

```text
Expressão Guiada
→ sugestão opcional e revisável

Compreensão Inicial
→ apresentação explícita como candidata + gate de confirmação

Hoje
→ contexto discreto somente quando já confirmado/autorizado
```

A área não se torna obrigatória em nenhum desses níveis.

A ausência de domínio confirmado permanece estado legítimo e não impede continuidade da jornada.

## 4. PER-004 — Expressão Guiada

### 4.1 Papel da área

A Expressão Guiada continua priorizando o relato livre da Pessoa. O sistema não exige que a Pessoa escolha uma área antes de explicar seu momento.

Depois da organização do relato, a síntese pode apresentar uma **Área da jornada possivelmente relacionada**.

A área apresentada pela Guivos deve estar marcada como:

- sugestão;
- candidata;
- baseada no relato;
- não confirmada.

### 4.2 Controles mínimos

A Pessoa deve poder:

- confirmar;
- adicionar outra área;
- indicar que a área não representa seu relato;
- manter a classificação em aberto.

Os caminhos **Ainda estou descobrindo** e **Outra área** permanecem legítimos.

### 4.3 Não propagação automática

Confirmar ou revisar a síntese não autoriza, por si só, a promoção automática da área para todos os usos do Journey.

A área candidata e a síntese derivada continuam separadas dos conteúdos de origem e das finalidades autorizadas.

## 5. Reconciliação terminológica da UXA-068

A expressão histórica **Dimensões de referência** utilizada na UXA-068 para `situação`, `impacto`, `prioridade`, `direção` e `contexto` deve ser interpretada, a partir desta frente, como **eixos de organização do relato**.

Ela não representa:

- os oito elementos estruturais do Contexto Vivo;
- os nove Domínios de Evolução `JED-001..JED-009`;
- categorias de identidade da Pessoa.

Portanto:

```text
situação / impacto / prioridade / direção / contexto
= eixos de organização do relato

JED-001..JED-009
= Domínios de Evolução
```

Essa separação evita colisão semântica entre arquitetura funcional e experiência.

## 6. PER-007 — Compreensão Inicial

### 6.1 Papel da área

A Compreensão Inicial é o principal gate de confirmação da D5-A porque já diferencia fatos declarados, inferências, desconhecidos e itens em aberto.

Uma área sugerida pela Guivos deverá aparecer como unidade separada das afirmações A1/A2 e com estado próprio.

Exemplo visual governado:

```text
Área possivelmente relacionada
Trabalho, carreira e estudos
Natureza: candidata da Guivos
Base: A1/A2
Estado: não confirmada
```

### 6.2 Independência de confirmação

A confirmação de uma afirmação não confirma automaticamente um domínio.

Da mesma forma:

```text
A1 confirmado
≠ área confirmada

A2 confirmado
≠ área confirmada

A1 + A2 confirmados
≠ área confirmada
```

A decisão sobre o domínio possui controle próprio.

### 6.3 Controles mínimos

Para uma área candidata, a revisão deve permitir:

- confirmar esta área;
- adicionar outra área;
- indicar que não representa a jornada;
- manter em aberto.

Nenhuma opção deve estar pré-selecionada.

### 6.4 Multidomínio

Adicionar outra área não substitui necessariamente a primeira. O modelo permite `0..n` domínios quando a experiência concreta atravessa mais de uma área.

### 6.5 Limites

Uma área confirmada:

- pode organizar contexto;
- não comprova evolução;
- não cria prioridade automática;
- não garante recomendação;
- não define identidade;
- não autoriza inferência sensível adicional.

## 7. PER-008 — Hoje

### 7.1 Papel da área

A Tela Hoje não ganha painel de domínios.

Quando houver domínio legitimamente confirmado e seu uso for adequado à finalidade, ele pode aparecer de forma discreta para explicar o contexto de um movimento já existente.

Exemplo:

```text
ÁREA CONFIRMADA POR VOCÊ · TRABALHO, CARREIRA E ESTUDOS
Preparar transição de carreira
Próximo passo: revisar competências
```

### 7.2 Condicionalidade

Sem domínio confirmado, a Tela Hoje continua funcionando normalmente.

A área não deve ocupar a hierarquia principal acima de Momento, atenção real ou Próximo Passo.

### 7.3 Revisabilidade

Quando a área aparecer em Hoje, deve existir caminho de revisão compatível com a autoridade da Pessoa.

### 7.4 Proteção contra falsa recomendação

A presença de um domínio confirmado não torna uma oportunidade automaticamente relevante.

Permanece válida a relação:

```text
domínio compatível ≠ oportunidade relevante
```

A D5-A não altera contratos de ranking, recomendação, oportunidade ou publicidade.

## 8. Sensibilidade

Os domínios podem conter subáreas sensíveis ou contextualmente sensíveis.

A D5-A não autoriza exposição destacada em Hoje, nem inferência automática, para conteúdos de saúde, religião/espiritualidade, finanças ou outros conteúdos sensíveis apenas porque a taxonomia possui um domínio correspondente.

Devem continuar prevalecendo:

- finalidade;
- minimização;
- autoridade;
- confirmação;
- privacidade por padrão;
- contestação e retirada.

## 9. Materialização visual

A frente reforma quatro SVGs existentes:

| Superfície | SVG | Mudança |
|---|---|---|
| `PER-004` | `uxa-068-guided-current-moment-structured-summary-mobile.svg` | área candidata após organização do relato + controles de revisão |
| `PER-007` | `uxa-036-initial-understanding-presentation-mobile.svg` | área candidata separada das afirmações e explicitamente não confirmada |
| `PER-007` | `uxa-036-initial-understanding-review-mobile.svg` | gate próprio de confirmação/rejeição/abertura da área |
| `PER-008` | `uxa-006-hoje-mobile.svg` | domínio confirmado como contexto discreto da continuidade |

Nenhum novo SVG é criado.

## 10. Contagens preservadas

A D5-A preserva:

- **118 SVGs canônicos**;
- **118 associações individuais**;
- **31 perfis de rastreabilidade**;
- **54 superfícies/estados/fronteiras**;
- **60 transições documentais**;
- `PER-004`, `PER-007` e `PER-008` como IDs vigentes.

Não há novo `PER-*`, `COL-*`, `ORG-*`, `BND-*` ou `TRN-*`.

## 11. Critérios de aceitação da D5-A

| Critério | Resultado esperado |
|---|---|
| área não antecede obrigatoriamente o relato | atendido |
| candidato é visualmente distinto de confirmado | atendido |
| confirmação de afirmação não confirma área | atendido |
| ausência de área continua legítima | atendido |
| multidomínio permanece possível | atendido |
| “Ainda estou descobrindo” não vira domínio | atendido |
| “Outra área” permanece mecanismo de extensibilidade | atendido |
| Hoje não ganha painel de nove áreas | atendido |
| Hoje usa apenas exemplo de área confirmada | atendido |
| JED interno não aparece como rótulo público | atendido |
| domínio não vira score/diagnóstico/identidade | atendido |
| nenhuma superfície ou transição nova | atendido |
| 118 SVGs preservados | atendido |

## 12. Fora do escopo

A D5-A não autoriza:

- D5-B — cadastro de oportunidade, Mapa, Lista ou Detalhe;
- D5-C — materialização de `Meus Objetivos`, `Meus Próximos Passos` ou `Minha Evolução`;
- novo painel ou “roda da vida”;
- décimo domínio;
- UXA-102/V5;
- implementação de `domain_link` em banco, API ou grafo;
- Engenharia de Produto;
- recomendação baseada exclusivamente em domínio;
- publicidade comportamental por domínio;
- alteração de cobrança, Planos ou `BND-002`.

## 13. Estado resultante

Com a D5-A, a experiência inicial passa a possuir uma continuidade semântica explícita:

```text
Pessoa relata seu momento
→ Guivos pode organizar o relato
→ área pode surgir como candidata e revisável
→ Compreensão Inicial apresenta a candidatura separadamente
→ Pessoa confirma, rejeita, adiciona outra área ou mantém em aberto
→ Hoje pode reutilizar somente domínio confirmado/autorizado como contexto discreto
```

Isso materializa o eixo **sobre o que a jornada trata** sem deslocar a arquitetura já vigente de **como a jornada opera**.

A conclusão documental da D5-A não inicia D5-B, D5-C, UXA-102/V5 ou Engenharia de Produto.