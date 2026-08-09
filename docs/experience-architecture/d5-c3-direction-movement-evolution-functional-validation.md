---
id: GKR-UX-D5-C3-001
title: Validação Funcional e Reformulação Controlada de Direção, Movimento e Evolução — D5-C3
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: UXA-000
depends_on:
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
related:
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-EC-VIEW-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-SURF-PER-010
  - GKR-SURF-PER-011
  - GKR-SURF-PER-012
  - GKR-TRN-008
  - GKR-TRN-009
  - GKR-TRN-010
  - GKR-TRN-011
  - GKR-TRN-012
  - GKR-TRN-013
normative: false
---

# GKR-UX-D5-C3-001 — Validação Funcional e Reformulação Controlada de Direção, Movimento e Evolução

## 1. Finalidade

A D5-C3 valida funcionalmente os três estados-base low-fidelity materializados pela D5-C2 e reforma in-place somente os pontos incompatíveis ou insuficientemente explícitos diante dos contratos vigentes.

Escopo:

- `PER-010 — Meus Objetivos`;
- `PER-011 — Meus Próximos Passos`;
- `PER-012 — Minha Evolução`.

A frente não cria nova superfície, novo SVG, novo perfil, nova transição ou novo marco funcional.

## 2. Autoridades confrontadas

A validação usa como autoridade funcional:

- `PAS-001-OBJ-VIEW-001` para `PER-010`;
- `PAS-001-PP-VIEW-001` para `PER-011`;
- `PAS-001-EC-VIEW-001` para `PER-012`.

A desambiguação semântica permanece governada por `GKR-UX-D5-C1-001`, `PAS-001-DOMAIN-MODEL-001` e `PAS-001-DOMAIN-RECON-001`.

A D5-C3 não reescreve esses contratos. Ela verifica se o estado-base visual respeita suas decisões mínimas de compreensão, autonomia, privacidade, explicabilidade e não coerção.

## 3. Método de validação

Cada SVG foi confrontado com seis dimensões:

1. identidade e responsabilidade da superfície;
2. semântica de estados e ações;
3. explicabilidade mínima no estado-base;
4. autonomia e reversibilidade;
5. proteção contra score, julgamento, coerção ou falsa precisão;
6. privacidade, sensibilidade e separações canônicas.

A validação é documental/visual. Ela não representa teste de usabilidade com participantes, implementação técnica, analytics real ou validação ponta a ponta dos handoffs.

## 4. Resultado de PER-010 — Meus Objetivos

### 4.1 Achados pré-reformulação

O SVG D5-C2 já preservava:

- responsabilidade própria de Objetivos;
- filtro opcional por Área da jornada;
- ausência de percentual automático;
- revisão de objetivo;
- retorno para Hoje;
- ausência de ranking ou comparação social.

Entretanto, a validação encontrou três insuficiências:

1. `EM ANDAMENTO` não correspondia com precisão à linguagem de estado funcional governada para Objetivos;
2. `EM DEFINIÇÃO` misturava exploração/formulação sem declarar qual estado funcional estava sendo apresentado;
3. a prioridade — elemento estrutural de `Meus Objetivos` — não aparecia no estado-base, impedindo demonstrar a separação entre prioridade declarada e valor pessoal.

### 4.2 Reformulação

O SVG passa a usar:

- `ATIVO` para o primeiro objetivo;
- `EM EXPLORAÇÃO` para o segundo;
- `Prioridade declarada · principal neste período`;
- progresso qualitativo baseado em marco, sem percentual automático;
- próxima revisão explícita;
- acesso a critérios, evidências e histórico;
- ausência de critério formal apresentada como condição legítima;
- controle de pausa, ocultação de conteúdo sensível e limitação de compartilhamento.

### 4.3 Validação

O estado-base passa a demonstrar que:

```text
estado ≠ prioridade
prioridade ≠ urgência
prioridade ≠ valor humano
Domínio de Evolução ≠ Objetivo
Domínio de Evolução ≠ progresso
```

`PER-010` é validado localmente no limite desse SVG reformulado.

## 5. Resultado de PER-011 — Meus Próximos Passos

### 5.1 Achados pré-reformulação

O SVG D5-C2 já preservava:

- autonomia para revisar, adiar ou não seguir;
- separação de proposta;
- Área da jornada opcional;
- relação com Objetivo;
- ausência de streak e pressão explícita;
- conclusão sem equivalência automática a evolução.

A validação encontrou três insuficiências:

1. `MOVIMENTO ATUAL` descrevia posição na interface, mas não um estado funcional;
2. prontidão e dependência — centrais para decisão — permaneciam implícitas;
3. a ação `Concluir` aparecia diretamente em um item cujo estado não justificava conclusão, reduzindo a coerência entre estado e ação principal.

### 5.2 Reformulação

O primeiro item passa a apresentar:

- estado `PRONTO`;
- prontidão explícita;
- ausência de dependência pendente conhecida;
- janela possível sem urgência artificial;
- ações `Iniciar · Adiar · Revisar`.

O item ainda não decidido passa a apresentar:

- `PROPOSTO — AGUARDA SUA DECISÃO`;
- origem `sugestão da Guivos`;
- declaração explícita de que a sugestão ainda não constitui decisão;
- ações `Avaliar · Manter em aberto · Não seguir`.

A superfície também declara que períodos sem passos ativos são legítimos.

### 5.3 Validação

O estado-base passa a demonstrar:

```text
proposta ≠ decisão
prontidão ≠ obrigação
janela possível ≠ urgência
iniciar ≠ concluir
concluir ≠ provar evolução
```

`PER-011` é validado localmente no limite desse SVG reformulado.

## 6. Resultado de PER-012 — Minha Evolução

### 6.1 Achados pré-reformulação

O SVG D5-C2 já preservava:

- Trajetória separada de Área da jornada;
- Direção reconhecida;
- aspectos descritivos da mudança;
- dimensão estrutural do Contexto Vivo separada;
- linguagem inconclusiva;
- acesso a evidências e revisão;
- ausência de score, ranking, roda da vida e diagnóstico.

A validação encontrou uma insuficiência material: a frase `Há sinais de fortalecimento, ainda inconclusivos` aparecia como leitura atual sem explicitar visualmente:

- natureza da interpretação;
- período;
- baseline;
- confiança;
- incerteza.

Isso poderia aproximar inferência de fato reconhecido, contrariando a separação exigida por `PAS-001-EC-VIEW-001`.

### 6.2 Reformulação

O SVG passa a apresentar:

- período acompanhado;
- baseline explícita;
- direção reconhecida;
- aspectos observados;
- contexto relacionado;
- bloco `INTERPRETAÇÃO PRELIMINAR — INFERIDA`;
- confiança `moderada`;
- limitação `baseline parcial`;
- incerteza explícita;
- acesso a evidências, contestação e revisão;
- controles de correção, pausa e limitação de compartilhamento.

### 6.3 Validação

O estado-base passa a tornar visível:

```text
observação ≠ interpretação
inferência ≠ fato confirmado
trajetória ≠ Domínio de Evolução
Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo
Domínio de Evolução ≠ aspecto descritivo da mudança
mudança local ≠ evolução integral da Pessoa
```

`PER-012` é validado localmente no limite desse SVG reformulado.

## 7. Sensibilidade e privacidade

A validação preserva os seguintes requisitos:

- objetivos sensíveis podem ter conteúdo minimizado ou ocultado;
- passos sensíveis podem utilizar títulos neutros e não devem expor dados clínicos, financeiros ou de terceiros por padrão;
- trajetórias sensíveis podem exigir modo discreto, ocultação de área e aprofundamento consciente;
- `domain_link` sensível não constitui nova autorização de tratamento;
- nenhum dos três estados-base pode produzir publicidade contextual a partir de vulnerabilidade;
- abrir a superfície não amplia consentimento nem compartilhamento.

A materialização exemplifica conteúdo não sensível. Ela não invalida os modos protegidos exigidos pelos contratos.

## 8. Domínios de Evolução

A D5-C3 preserva `0..n` relações com Domínios de Evolução quando pertinentes.

Na interface pública:

- usa-se `Área da jornada` ou o nome compreensível do domínio;
- IDs `JED-*` permanecem identificadores internos;
- multidomínio é legítimo;
- ausência de domínio é legítima;
- domínio não define prioridade, prontidão, progresso, resultado ou evolução.

## 9. Handoffs preservados sem promoção

A D5-C3 não valida integração entre Hoje e as três superfícies.

Permanecem `contratadas`:

```text
TRN-008 — PER-008 → PER-010
TRN-009 — PER-010 → PER-008
TRN-010 — PER-008 → PER-011
TRN-011 — PER-011 → PER-008
TRN-012 — PER-008 → PER-012
TRN-013 — PER-012 → PER-008
```

O rótulo visual `‹ Hoje` demonstra somente affordance local de retorno. Ele não comprova payload, preservação de contexto, concorrência, interrupção, idempotência, autorização ou revalidação ponta a ponta.

Nenhum handoff direto entre `PER-010`, `PER-011` e `PER-012` é criado.

## 10. Maturidade resultante

Após D5-C3:

- `PER-010`: SVG materializado e funcionalmente validado localmente;
- `PER-011`: SVG materializado e funcionalmente validado localmente;
- `PER-012`: SVG materializado e funcionalmente validado localmente;
- `TRN-008..013`: continuam contratadas;
- Jornada da Pessoa: continua `draft`.

Validação local de superfície não equivale a continuidade integrada.

## 11. Efeito no inventário

A D5-C3 não altera inventário físico ou granular:

- 121 SVGs canônicos;
- 121 associações;
- 34 perfis de rastreabilidade;
- 57 superfícies/estados/fronteiras;
- 66 transições;
- 45 de 57 IDs com referência visual;
- 10 responsabilidades sem SVG dedicado;
- 2 fronteiras sem tela.

Ela altera somente a maturidade de validação visual:

```text
SVGs funcionalmente validados: 118 → 121
SVGs pendentes de validação específica: 3 → 0
```

## 12. O que a D5-C3 não autoriza

A frente não autoriza:

- promoção de `TRN-008..013`;
- teste de usabilidade ou pesquisa com participantes;
- protótipo high-fidelity;
- implementação frontend/backend;
- rota, API, evento, banco ou analytics operacional;
- nova superfície ou estado;
- D6;
- D7;
- UXA-102/V5;
- Engenharia de Produto/W0-01;
- classificação operacional por IA dos Domínios de Evolução.

## 13. Gate posterior

A próxima necessidade lógica, caso autorizada separadamente, é auditar e validar a continuidade integrada:

```text
Hoje ↔ Meus Objetivos
Hoje ↔ Meus Próximos Passos
Hoje ↔ Minha Evolução
```

Essa eventual frente deverá tratar `TRN-008..013` como objeto próprio de validação e não pode ser presumida pela aprovação local dos três SVGs.
