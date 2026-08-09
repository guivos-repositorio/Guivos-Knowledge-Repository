---
id: GKR-UX-D5-C4B-001
title: Validação Integrada dos Handoffs de Direção, Movimento e Evolução — D5-C4B
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: UXA-000
depends_on:
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-UX-D5-C4A-001
related:
  - GKR-SURF-PER-008
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

# GKR-UX-D5-C4B-001 — Validação Integrada dos Handoffs de Direção, Movimento e Evolução

## 1. Finalidade

A D5-C4B executa a validação integrada individual de `TRN-008..013` após a D5-C4A ter materializado as origens recorrentes em `PER-008 — Hoje` e fechado os contratos de identidade, contexto mínimo, revalidação, retorno, interrupção, concorrência, idempotência, autoridade e sensibilidade.

A frente decide a maturidade de cada transição separadamente. A promoção não é presumida por pertencerem ao mesmo conjunto.

A validação é documental e de Experience Architecture. Ela não declara rotas, APIs, banco, cache, fila, persistência, sincronização técnica ou produto implementado.

## 2. Critério de validação integral

O `GKR-JOURNEY-TRANSITION-REGISTRY-001` considera uma transição `integralmente validada` quando, dentro do limite de autoridade declarado, foram examinados:

1. origem;
2. destino;
3. autoridade;
4. dados/contexto;
5. efeito permitido e proibido;
6. retorno;
7. interrupção;
8. concorrência/estado obsoleto;
9. idempotência quando material ao fluxo.

A D5-C4B aplica o mesmo padrão utilizado em validações integradas anteriores, como `TRN-007`, sem exigir implementação técnica.

## 3. Limite de aplicação em PER-008

`PER-008` possui mais de uma materialização visual.

Os handoffs de entrada `TRN-008`, `TRN-010` e `TRN-012` são validados para o **estado recorrente de Hoje quando o affordance correspondente estiver materializado e aplicável**.

A primeira variante de Hoje, governada pela UXA-097, permanece orientada à primeira entrada e não é obrigada a expor os três aprofundamentos especializados.

Portanto:

```text
transição integralmente validada
≠ affordance obrigatório em toda variante de PER-008
```

Quando o affordance não estiver presente, a transição simplesmente não é instanciada naquele estado visual.

## 4. Matriz de evidência

| TRN | Origem | Destino | Contexto permitido | Revalidação | Retorno/interrupção | Concorrência/idempotência | Veredito |
|---|---|---|---|---|---|---|---|
| `TRN-008` | Hoje recorrente — `Meus Objetivos` | PER-010 validado | origem, âncora e referência lógica opcional de Objetivo vigente | estado, autoridade, visibilidade e atualidade | voltar não cria/salva/prioriza/progride | referência obsoleta cai para estado neutro; repetir não duplica | **integralmente validada** |
| `TRN-009` | PER-010 — `‹ Hoje` | PER-008 recorrente | âncora de retorno; nenhum efeito implícito | Hoje reconsulta estado canônico | edição incompleta não é salva pela navegação; interrupção não muta | mudanças concorrentes prevalecem; voltar repetidamente é neutro | **integralmente validada** |
| `TRN-010` | Hoje recorrente — `Abrir este passo` | PER-011 validado | referência lógica mínima do passo explicitamente mostrado | passo, autoridade, vigência e visibilidade | abrir não inicia/aceita/conclui | item obsoleto cai para estado atualizado/neutro; repetir não duplica | **integralmente validada** |
| `TRN-011` | PER-011 — `‹ Hoje` | PER-008 recorrente | âncora de retorno; ação substantiva pertence ao PER-011 | Hoje reconsulta estado vigente | retorno não marca visto/aceito/iniciado/executado/concluído | alterações concorrentes prevalecem; retorno repetido é neutro | **integralmente validada** |
| `TRN-012` | Hoje recorrente — `Minha Evolução` | PER-012 validado | acesso genérico; sem trajetória/domínio/interpretação/evidência por padrão | autenticação, privacidade, visibilidade e sensibilidade | abrir não reconhece mudança/evolução; interrupção não confirma nada | estado vigente prevalece; repetir não confirma interpretação | **integralmente validada** |
| `TRN-013` | PER-012 — `‹ Hoje` | PER-008 recorrente | âncora de retorno; natureza epistemológica preservada | Hoje reconsulta permissões e estado canônico | retorno não confirma baseline/direção/mudança/evolução/compartilhamento | inferência não vira fato; repetir não cria evidência | **integralmente validada** |

## 5. TRN-008 — Hoje → Meus Objetivos

### 5.1 Origem e destino

Origem materializada no Hoje recorrente por `Meus Objetivos`.

Destino `PER-010` possui estado-base funcionalmente validado pela D5-C3.

### 5.2 Efeito

```text
abrir Meus Objetivos
≠ criar Objetivo
≠ confirmar Objetivo
≠ priorizar Objetivo
≠ registrar progresso
```

O acesso pode ser genérico. Referência lógica de Objetivo é opcional e somente pode ser usada quando o vínculo estiver explícito e vigente.

### 5.3 Estado obsoleto

Se a referência não estiver mais vigente, autorizada ou disponível, `PER-010` abre em estado neutro/atualizado. A transição não recria nem substitui Objetivo.

### 5.4 Veredito

`GKR-TRN-008` é promovida de `contratada` para **integralmente validada** no limite documental do Hoje recorrente.

## 6. TRN-009 — Meus Objetivos → Hoje

### 6.1 Origem e destino

`PER-010` materializa `‹ Hoje` como retorno consciente. `PER-008` recorrente está revalidado pela D5-C4A.

### 6.2 Neutralidade do retorno

Retornar não:

- salva edição incompleta pela navegação;
- muda prioridade;
- registra progresso;
- encerra revisão;
- cria evidência.

Se uma ação substantiva foi concluída em `PER-010`, seu efeito pertence ao contrato do Objetivo. Hoje apenas reconsulta o estado canônico vigente.

### 6.3 Veredito

`GKR-TRN-009` é promovida para **integralmente validada**.

## 7. TRN-010 — Hoje → Meus Próximos Passos

### 7.1 Origem inequívoca

D5-C4A refinou o affordance para `Abrir este passo`, eliminando a ambiguidade entre abrir a capacidade genericamente e abrir o item explicitamente mostrado.

### 7.2 Contexto mínimo

A única identidade funcional específica permitida por padrão é a referência lógica mínima do passo mostrado.

```text
Abrir este passo
≠ iniciar
≠ aceitar
≠ concluir
≠ transformar proposta em decisão
```

Se a referência estiver obsoleta, `PER-011` deve mostrar o estado vigente ou uma entrada neutra; substituição automática é proibida.

### 7.3 Veredito

`GKR-TRN-010` é promovida para **integralmente validada**.

## 8. TRN-011 — Meus Próximos Passos → Hoje

`PER-011` materializa retorno `‹ Hoje`.

A navegação não marca o passo como visto, aceito, iniciado, executado ou concluído.

Ações como `Iniciar`, `Adiar`, `Revisar` ou `Não seguir` são ações próprias de `PER-011`; somente seus efeitos legitimamente concluídos podem aparecer em Hoje após nova consulta ao estado vigente.

Interrupção ou retorno repetido não duplicam qualquer efeito.

### 8.1 Veredito

`GKR-TRN-011` é promovida para **integralmente validada**.

## 9. TRN-012 — Hoje → Minha Evolução

### 9.1 Proteção adicional

O acesso materializado `Minha Evolução` é genérico e neutro.

Por padrão, a transição não transporta:

- trajetória;
- Área da jornada;
- domínio sensível;
- interpretação;
- evidência;
- inferência;
- consentimento adicional.

O destino revalida autenticação, privacidade, visibilidade e sensibilidade antes de apresentar conteúdo.

### 9.2 Efeito

```text
abrir Minha Evolução
≠ reconhecer mudança
≠ confirmar evolução
≠ confirmar inferência
≠ expor contexto sensível
```

### 9.3 Veredito

`GKR-TRN-012` é promovida para **integralmente validada** no limite documental e de privacidade declarado.

## 10. TRN-013 — Minha Evolução → Hoje

O retorno `‹ Hoje` é navegação neutra.

Ele não confirma interpretação, baseline, direção, mudança, evolução ou compartilhamento.

Uma interpretação `PRELIMINAR — INFERIDA` permanece inferida depois do retorno. Hoje não pode reescrevê-la como fato. Qualquer síntese posterior deve preservar natureza epistemológica, minimização e permissões vigentes.

Interrupção, recarga ou retorno repetido não criam evidência nem reconhecimento de evolução.

### 10.1 Veredito

`GKR-TRN-013` é promovida para **integralmente validada**.

## 11. Resultado consolidado

Após D5-C4B:

```text
TRN-008 — integralmente validada
TRN-009 — integralmente validada
TRN-010 — integralmente validada
TRN-011 — integralmente validada
TRN-012 — integralmente validada
TRN-013 — integralmente validada
```

A promoção é individual, embora o resultado final seja uniforme.

O conjunto validado pode ser lido como:

```text
PER-008 recorrente
├── TRN-008 → PER-010 → TRN-009 → PER-008
├── TRN-010 → PER-011 → TRN-011 → PER-008
└── TRN-012 → PER-012 → TRN-013 → PER-008
```

## 12. O que a promoção não significa

A D5-C4B não comprova:

- implementação frontend;
- roteamento real;
- persistência;
- lock, fila, cache ou sincronização;
- telemetria;
- produto em produção;
- consentimentos operacionais;
- proteção técnica de dispositivo compartilhado;
- classificação operacional de Domínios de Evolução;
- grafo/Neo4j implementado.

Validação integrada documental ≠ implementação técnica.

## 13. Inventário

Nenhuma contagem física ou granular muda:

- 121 SVGs;
- 121 associações;
- 34 perfis;
- 121 validações funcionais vigentes de SVG;
- 0 pendências específicas de SVG;
- 57 superfícies/estados/fronteiras;
- 66 transições;
- 45 de 57 IDs com referência visual;
- 10 responsabilidades sem SVG dedicado;
- 2 fronteiras sem tela.

A mudança é exclusivamente de maturidade de `TRN-008..013`.

## 14. Limites de escopo

A D5-C4B não:

- cria ou reforma SVG;
- cria nova superfície, perfil ou transição;
- cria handoffs diretos entre `PER-010`, `PER-011` e `PER-012`;
- inicia UXA-102/V5;
- inicia D6 ou D7;
- materializa `PER-009`;
- altera maturidade de `TRN-406/407`;
- retoma Engenharia de Produto.

## 15. Estado posterior

Com os seis handoffs validados integralmente, a lacuna específica D5-C de continuidade `Hoje ↔ Objetivos/Próximos Passos/Evolução` fica encerrada no limite documental.

Isso não promove a Jornada da Pessoa como um todo, que continua `draft` por outras lacunas anteriores e posteriores.

Nenhuma etapa seguinte é autorizada automaticamente.
