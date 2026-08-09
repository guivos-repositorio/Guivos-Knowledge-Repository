---
id: GKR-UX-D5-B-001
title: Materialização Controlada dos Domínios de Evolução na Camada de Oportunidades
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: UXA-000
normative: false
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-UX-D5-A-001
  - UXA-004
  - UXA-007
  - UXA-008
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
---

# GKR-UX-D5-B-001 — Materialização Controlada dos Domínios de Evolução na Camada de Oportunidades

## 1. Finalidade

A D5-B materializa o eixo canônico de **Domínios de Evolução** na camada de Oportunidades sem converter domínio em recomendação, classificação da Pessoa, elegibilidade, publicidade ou prova de evolução.

O recorte cobre exclusivamente:

1. `ORG-002 — Cadastro da oportunidade`;
2. `PER-201 — Mapa`;
3. `PER-202 — Lista`;
4. `PER-203 — Detalhe`.

A frente não cria nova superfície, estado granular, fronteira, transição ou família visual.

## 2. Invariante semântico

A D5-B preserva a seguinte separação:

```text
domínio da oportunidade
≠ domínio confirmado da Pessoa
≠ relevância contextual
≠ recomendação
```

Da mesma forma:

```text
mesmo domínio
≠ match automático
≠ recomendação automática
≠ compartilhamento automático
≠ autorização automática
```

O domínio informa **sobre o que a oportunidade trata**. Ele é apenas um dos possíveis sinais de organização e explicação do inventário.

## 3. ORG-002 — Cadastro da oportunidade

### 3.1 Áreas relacionadas

A etapa já existente **Jornada e contribuição** passa a admitir `0..n` **Áreas relacionadas** à oportunidade.

Exemplo público:

```text
Áreas relacionadas
Trabalho, carreira e estudos
Empreendedorismo e projetos
```

Essa declaração pertence à oportunidade/programa e não ao participante que poderá encontrá-la.

### 3.2 Autoridade da Organização

A Organização pode declarar:

- quais áreas descrevem a oportunidade;
- a contribuição pretendida;
- o contexto geral apoiado;
- o Próximo Passo que pode apoiar;
- limites e não garantias.

A Organização não pode, por esse cadastro:

- afirmar que uma Pessoa pertence a determinado domínio;
- acessar domínio confirmado ou inferido da Pessoa;
- determinar prioridade da jornada pessoal;
- garantir relevância ou distribuição;
- transformar área em critério de mérito ou evolução.

### 3.3 Sem nova etapa

A D5-B não cria uma 12ª etapa. `Áreas relacionadas` integra **Jornada e contribuição** e deve aparecer também nos resumos dessa etapa quando o cadastro estiver em passos posteriores.

## 4. PER-201 — Mapa

### 4.1 Área como filtro explícito

O painel de filtros do Mapa passa a admitir **Área da jornada**.

Exemplo:

```text
Área da jornada
Trabalho, carreira e estudos
```

O filtro é uma escolha explícita da Pessoa naquele contexto de exploração.

### 4.2 Proibição de ativação silenciosa

O filtro não pode ser ativado automaticamente porque:

- a Pessoa confirmou um domínio em outro momento;
- a Guivos inferiu uma área;
- a oportunidade compartilha domínio com um item da jornada;
- um anunciante ou Organização deseja segmentar audiência.

Especialmente em contextos de saúde, espiritualidade/religião e finanças, a navegação não pode revelar ou reconstruir silenciosamente contexto sensível da Pessoa.

### 4.3 Metadado da oportunidade

Um cartão selecionado pode apresentar o domínio declarado da própria oportunidade, com origem compreensível quando necessário.

Exemplo:

```text
Área da oportunidade: Trabalho, carreira e estudos
Declarada pelo Instituto Horizonte
```

Isso não significa que a Pessoa foi classificada nessa área.

## 5. PER-202 — Lista

Mapa e Lista continuam sendo duas visualizações da mesma consulta.

Portanto, os filtros de área seguem a mesma semântica, mesma origem e mesmo estado entre as duas visualizações.

A Lista pode exibir a área de cada item para comparação, inclusive quando a consulta contém oportunidades de domínios diferentes.

Exemplo:

```text
Mentoria de carreira
Área: Trabalho, carreira e estudos

Ação comunitária
Área: Causas, voluntariado e contribuição
```

A presença de itens de múltiplos domínios é válida e não força a Pessoa a escolher um único domínio.

## 6. PER-203 — Detalhe

### 6.1 Área da oportunidade

O Detalhe deve separar explicitamente o metadado da oportunidade da explicação de relevância contextual.

Exemplo:

```text
Área desta oportunidade
Trabalho, carreira e estudos
Declarada pelo Instituto Horizonte
```

### 6.2 Por que pode fazer sentido

Em bloco separado, a Guivos pode explicar sinais contextuais legitimamente utilizados, como:

- busca ou filtro escolhido pela Pessoa;
- Objetivo ou Próximo Passo confirmado;
- localização e temporalidade compatíveis;
- preferências ou restrições autorizadas;
- elegibilidade conhecida e aplicável.

O domínio, quando usado, deve aparecer apenas como **um sinal contextual**, nunca como justificativa suficiente.

### 6.3 Regra de explicabilidade

```text
área da oportunidade
+ contexto compatível
→ pode contribuir para explicar presença/relevância

área da oportunidade isoladamente
→ não autoriza recomendação
```

A Pessoa deve continuar podendo revisar ou corrigir o contexto utilizado sem alterar os metadados institucionais da oportunidade.

## 7. Proveniência

A D5-B diferencia duas proveniências:

1. **proveniência da área da oportunidade** — normalmente declaração da Organização/Coletivo responsável ou classificação editorial governada;
2. **proveniência do contexto pessoal** — declaração, confirmação ou uso autorizado pela Pessoa.

Essas proveniências não devem ser fundidas.

## 8. Sensibilidade e privacidade

A D5-B não autoriza:

- inferência de saúde, crença, condição financeira ou outro contexto sensível a partir de cliques;
- criação de segmento publicitário por domínio pessoal;
- exposição pública do domínio confirmado da Pessoa;
- compartilhamento de domínio pessoal com Organização ou Coletivo;
- preenchimento automático de filtros sensíveis;
- uso de `JED-*` como rótulo público.

Ads permanece separado da relevância orgânica.

## 9. Materialização visual

A D5-B utiliza os ativos já existentes e não cria nova família visual.

| Superfície | Ativo vigente | Materialização D5-B |
|---|---|---|
| `ORG-002` | cadastro institucional existente | `Áreas relacionadas` governadas dentro de `Jornada e contribuição`; sem nova etapa |
| `PER-201` | Mapa de Oportunidades existente | filtro explícito de área + metadado da oportunidade selecionada |
| `PER-202` | Lista territorial existente | mesma semântica de filtro + área por item quando útil à comparação |
| `PER-203` | Detalhe existente | área da oportunidade/proveniência separadas da justificativa contextual |

O SVG de `ORG-002` atualmente apresenta um passo posterior do wizard e reutiliza `Jornada e contribuição` como resumo. A D5-B governa que a área relacionada integra esse resumo quando declarada, sem alterar a etapa ativa ou criar nova etapa.

## 10. Contagens preservadas

A D5-B preserva:

- **118 SVGs canônicos**;
- **118 associações individuais**;
- **31 perfis de rastreabilidade**;
- **54 superfícies/estados/fronteiras**;
- **60 transições documentais**;
- **42 de 54 IDs com referência visual**;
- **10 responsabilidades sem SVG dedicado**;
- **2 fronteiras sem tela**.

Não há novo `PER-*`, `COL-*`, `ORG-*`, `BND-*` ou `TRN-*`.

## 11. Critérios de aceitação

| Critério | Resultado esperado |
|---|---|
| oportunidade pode ter `0..n` áreas | atendido |
| área pertence semanticamente à oportunidade | atendido |
| Organização não classifica a Pessoa | atendido |
| Área da jornada é filtro explícito | atendido |
| filtro não é ativado silenciosamente | atendido |
| Mapa e Lista preservam a mesma consulta | atendido |
| área pode aparecer como metadado por item | atendido |
| Detalhe separa área e relevância contextual | atendido |
| mesmo domínio não cria recomendação | atendido |
| domínio sensível não vira segmentação de Ads | atendido |
| nenhuma nova superfície/transição | atendido |
| contagens de UX preservadas | atendido |

## 12. Fora do escopo

A D5-B não autoriza:

- D5-C — `Meus Objetivos`, `Meus Próximos Passos`, `Minha Evolução` ou novas superfícies correlatas;
- D6 — grafo, Neo4j, ontologia física ou `domain_link` implementado;
- D7 — Public Canon;
- UXA-102/V5;
- Engenharia de Produto;
- alteração física de banco, API, payload ou eventos;
- ranking ou recomendação baseados exclusivamente em domínio;
- publicidade comportamental por domínio;
- nova taxonomia ou décimo domínio;
- alteração de Planos, cobrança ou `BND-002`.

## 13. Estado resultante

```text
Organização descreve a oportunidade
→ declara 0..n áreas relacionadas
→ oportunidade entra no inventário com proveniência própria
→ Pessoa pode pesquisar ou filtrar explicitamente por área
→ Mapa e Lista preservam a mesma consulta
→ Detalhe mostra área da oportunidade separada do contexto pessoal
→ Guivos explica relevância usando apenas sinais legítimos
```

A D5-B materializa os Domínios de Evolução na camada de Oportunidades sem converter taxonomia em perfil compulsório, recomendação automática ou mecanismo publicitário.