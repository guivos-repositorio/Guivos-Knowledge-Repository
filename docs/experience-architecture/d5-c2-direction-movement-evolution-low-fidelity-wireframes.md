---
id: GKR-UX-D5-C2-001
title: Materialização Low-Fidelity das Superfícies de Direção, Movimento e Evolução
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: UXA-000
related:
  - GKR-UX-D5-C1-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-EC-VIEW-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
normative: false
---

# GKR-UX-D5-C2-001 — Materialização Low-Fidelity das Superfícies de Direção, Movimento e Evolução

## 1. Finalidade

A D5-C2 materializa visualmente, em baixa fidelidade, as três responsabilidades pessoais contratadas pela D5-C1:

- `GKR-SURF-PER-010 — Meus Objetivos`;
- `GKR-SURF-PER-011 — Meus Próximos Passos`;
- `GKR-SURF-PER-012 — Minha Evolução`.

Esta frente cria somente um estado-base móvel por responsabilidade, suficiente para tornar a responsabilidade visualmente inspecionável sem antecipar validação funcional, estados residuais, protótipo ou implementação.

```text
contrato D5-C1
→ materialização low-fidelity D5-C2
≠ validação funcional
≠ validação de transição
≠ protótipo
≠ implementação
```

## 2. Escopo visual

Os três ativos adotam o mesmo envelope móvel low-fidelity da jornada pessoal existente:

- viewport de referência `390 × 844`;
- hierarquia textual simples;
- escala de cinza;
- componentes esquemáticos;
- sem identidade visual final;
- sem microinterações implementadas;
- sem comportamento técnico presumido.

Ativos criados:

| Responsabilidade | SVG | Papel |
|---|---|---|
| `PER-010` | `d5-c2-person-objectives-mobile.svg` | direção e controle de Objetivos |
| `PER-011` | `d5-c2-person-next-steps-mobile.svg` | movimento contextual e controle de Próximos Passos |
| `PER-012` | `d5-c2-person-evolution-mobile.svg` | compreensão, evidência e revisão de trajetórias |

A presença visual de `‹ Hoje` em cada SVG expressa a origem/retorno contratados pela D5-C1, mas **não valida** `TRN-008..013`.

## 3. PER-010 — Meus Objetivos

### 3.1 Decisão principal

A Pessoa deve poder compreender as direções que escolheu acompanhar e decidir como revisá-las, sem converter a experiência em controle de produtividade.

O estado-base materializa:

- título e orientação de finalidade;
- estados de portfólio como `Ativos`, `Pausados` e `Concluídos`;
- filtro opcional `Área da jornada` sob controle da Pessoa;
- Objetivos com estado, área relacionada e próxima revisão;
- multidomínio quando legítimo;
- ausência deliberada de percentual automático de progresso;
- ação explícita para registrar Objetivo;
- mensagem de que objetivo, prioridade e critérios são revisáveis.

### 3.2 Guardrails

```text
Objetivo
≠ produtividade
≠ mérito
≠ obrigação permanente
≠ score de evolução
```

`domain_link` pode organizar ou filtrar, mas não cria Objetivo, não define prioridade e não comprova progresso.

## 4. PER-011 — Meus Próximos Passos

### 4.1 Decisão principal

A Pessoa deve compreender movimentos contextuais disponíveis e poder aceitá-los, revisá-los, adiá-los, concluí-los ou recusá-los sem pressão artificial.

O estado-base materializa:

- `Agora · Propostos · Bloqueados` como leituras possíveis do portfólio;
- filtro opcional por Área da jornada;
- movimento atual relacionado a Objetivo;
- janela contextual sem transformar data em urgência moral;
- proposta explicitamente apresentada como escolha;
- ações de revisar, adiar, concluir, aceitar, manter em aberto ou não seguir;
- mensagem explícita de que conclusão não prova evolução.

### 4.2 Guardrails

```text
Próximo Passo
≠ tarefa de produtividade
≠ obrigação
≠ urgência automática
≠ prova de progresso humano
≠ prova de evolução
```

A futura validação deverá examinar títulos neutros, exposição sensível e estados de bloqueio antes de qualquer promoção funcional.

## 5. PER-012 — Minha Evolução

### 5.1 Decisão principal

A Pessoa deve compreender e revisar trajetórias, mudanças, continuidades, evidências e interpretações sem receber uma nota humana ou conclusão automática.

O estado-base materializa explicitamente:

- Área da jornada;
- Trajetória;
- Direção reconhecida;
- Aspectos observados;
- Contexto relacionado;
- leitura atual com incerteza;
- acesso a evidências e revisão da interpretação;
- controle para revisar trajetória, pausar acompanhamento ou ajustar privacidade.

Também torna visível a reconciliação D5-C1:

```text
Domínio de Evolução
≠ dimensão estrutural do Contexto Vivo
≠ aspecto descritivo da mudança
```

### 5.2 Proibições visuais

Não são utilizados:

- percentual de evolução;
- score humano;
- ranking;
- radar obrigatório;
- roda da vida;
- streak;
- diagnóstico médico ou psicológico;
- avaliação espiritual;
- índice de produtividade pessoal.

## 6. Domínios de Evolução na interface

A D5-C2 preserva `PAS-001-DOMAIN-MODEL-001` e D5-C1:

- nomes públicos podem aparecer na interface;
- `JED-*` permanece rastreabilidade interna, não rótulo obrigatório;
- um objeto pode se relacionar a `0..n` domínios;
- multidomínio é legítimo;
- ausência de domínio não bloqueia a superfície;
- domínio não define identidade permanente;
- domínio sensível não amplia finalidade, acesso ou compartilhamento;
- filtro por Área da jornada depende de ação consciente da Pessoa;
- nenhum domínio compra relevância ou prioridade.

## 7. Privacidade e sensibilidade

A materialização não autoriza coleta adicional.

A futura validação deverá examinar, entre outros casos:

- Objetivo sensível com título minimizado;
- Próximo Passo sensível com notificação neutra;
- trajetória envolvendo Saúde, Espiritualidade/Religião, Finanças ou vulnerabilidade;
- dispositivo compartilhado;
- ocultação ou minimização de Área da jornada quando necessário;
- revisão, retirada e histórico de associações de domínio.

```text
mostrar uma possibilidade visual
≠ autorizar novo tratamento de dados
```

## 8. Handoffs preservados sem promoção

Continuam contratadas:

```text
PER-008 → TRN-008 → PER-010
PER-010 → TRN-009 → PER-008

PER-008 → TRN-010 → PER-011
PER-011 → TRN-011 → PER-008

PER-008 → TRN-012 → PER-012
PER-012 → TRN-013 → PER-008
```

A D5-C2 remove somente a lacuna de **ausência visual das três superfícies**.

Ela não examina ainda ponta a ponta:

- identidade preservada entre origem e destino;
- payload/contexto transferido;
- concorrência;
- idempotência;
- retorno de estado;
- interrupção;
- revalidação de autorização;
- comportamento em erro.

Portanto, `TRN-008..013` permanecem `contratada`.

## 9. Efeito no inventário

Após a D5-C2, o inventário proposto da branch passa a:

| Indicador | Antes | D5-C2 |
|---|---:|---:|
| SVGs canônicos | 118 | **121** |
| associações por SVG | 118 | **121** |
| perfis de rastreabilidade | 31 | **34** |
| SVGs com validação funcional vigente | 118 | **118** |
| SVGs pendentes de validação específica | 0 | **3** |
| superfícies/estados/fronteiras | 57 | **57** |
| transições | 66 | **66** |
| IDs com referência visual | 42/57 | **45/57** |
| responsabilidades sem SVG dedicado | 13 | **10** |
| fronteiras sem tela | 2 | **2** |

A adição visual não cria novos IDs de superfície porque `PER-010..012` já foram contratados pela D5-C1.

## 10. Perfis de rastreabilidade candidatos da frente

A matriz passa a utilizar três perfis próprios:

- `R32 — PER-010`;
- `R33 — PER-011`;
- `R34 — PER-012`.

Os três perfis permanecem com validação pendente até frente específica posterior.

## 11. Limites da D5-C2

A frente não:

- promove `PER-010..012` a `validado`;
- promove `TRN-008..013` além de `contratada`;
- cria estados residuais adicionais;
- cria materialização para Coletivo ou Organização a partir dessas três responsabilidades pessoais;
- cria API, banco, evento, grafo ou `domain_link` físico;
- inicia D6 ou D7;
- inicia UXA-102/V5;
- retoma Product Engineering/W0-01;
- declara os wireframes como produto implementado.

## 12. Próximo gate possível

Após integração governada da D5-C2, uma frente posterior e separada poderá realizar a validação funcional/reformulação das três superfícies e examinar `TRN-008..013`.

Nenhuma validação posterior é autorizada automaticamente por este documento.
