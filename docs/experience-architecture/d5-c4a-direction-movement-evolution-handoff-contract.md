---
id: GKR-UX-D5-C4A-001
title: Materialização e Contrato Integrado dos Handoffs de Direção, Movimento e Evolução — D5-C4A
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: UXA-000
depends_on:
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
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

# GKR-UX-D5-C4A-001 — Materialização e Contrato Integrado dos Handoffs de Direção, Movimento e Evolução

## 1. Finalidade

A D5-C4A fecha o contrato semântico e a materialização mínima necessários para que os handoffs entre `PER-008 — Hoje` e `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` e `PER-012 — Minha Evolução` possam ser validados posteriormente como ligações ponta a ponta.

A frente:

1. reformula **in-place** o estado recorrente de `PER-008 — Hoje` para tornar inequívocos os acessos conscientes às três responsabilidades especializadas;
2. define o contexto semântico mínimo permitido em `TRN-008..013`;
3. define retorno neutro, interrupção, concorrência, idempotência e revalidação de autoridade;
4. reforça a proteção adicional de `TRN-012/013` por envolver trajetórias potencialmente sensíveis;
5. revalida localmente o SVG recorrente de Hoje no limite dessa reformulação.

A D5-C4A **não promove `TRN-008..013`**. As seis transições continuam `contratadas` até validação integrada posterior.

## 2. Escopo físico e granular

A frente não cria:

- novo SVG;
- nova superfície;
- novo perfil de rastreabilidade;
- nova transição;
- nova UXA numerada;
- implementação técnica.

A baseline permanece:

- 121 SVGs canônicos;
- 121 associações;
- 34 perfis;
- 57 superfícies/estados/fronteiras;
- 66 transições;
- 45 de 57 IDs com referência visual;
- 10 responsabilidades sem SVG dedicado;
- 2 fronteiras sem tela.

O SVG recorrente `uxa-006-hoje-mobile.svg` é reformulado e revalidado localmente. A primeira variante de Hoje (`uxa-097-first-today-after-initial-understanding-mobile.svg`) permanece inalterada porque sua responsabilidade é orientar a primeira entrada sem sobrecarga. Os handoffs especializados são disponibilidade do estado recorrente quando aplicáveis, não obrigação da primeira entrada.

## 3. Papel de Hoje após D5-C4A

`PER-008` continua síntese recorrente, não dashboard completo das três capacidades.

A reformulação usa um único bloco existente de continuidade e acrescenta três affordances compactas, sem criar três cards permanentes:

```text
Meus Objetivos
Abrir este passo
Minha Evolução
```

Regras:

- `Meus Objetivos` é acesso genérico e não confirma que exista um objetivo prioritário;
- `Abrir este passo` pode transportar somente a referência lógica mínima do passo explicitamente mostrado em Hoje;
- `Minha Evolução` é acesso genérico e neutro; sua presença não afirma que houve mudança ou evolução;
- nenhuma dessas ações cria, confirma, inicia, conclui, reconhece ou compartilha algo por efeito da navegação;
- conteúdo sensível não é exposto no rótulo de acesso.

## 4. Contrato transversal dos seis handoffs

### 4.1 Identidade

Quando houver objeto lógico explicitamente selecionado em Hoje, o destino deve tentar preservar essa identidade sem duplicá-la.

Se o objeto não estiver mais vigente, autorizado ou disponível, a navegação deverá cair para um estado neutro da superfície de destino, sem recriar, inferir ou substituir silenciosamente o objeto.

### 4.2 Contexto mínimo

A navegação pode transportar somente contexto suficiente para orientar a apresentação.

O contexto semântico permitido inclui, quando aplicável:

- origem `Hoje`;
- referência lógica do objeto explicitamente acionado;
- âncora de retorno;
- indicação de que o acesso foi iniciado conscientemente pela Pessoa.

A navegação não transporta automaticamente:

- inferências novas;
- domínio sensível;
- conteúdo clínico, financeiro, religioso ou de terceiros;
- prioridade implícita;
- decisão;
- progresso;
- consentimento ampliado;
- autorização de compartilhamento.

### 4.3 Revalidação

O destino revalida estado, autoridade, visibilidade e atualidade antes de apresentar conteúdo protegido ou permitir ação substantiva.

Uma referência de origem pode estar desatualizada, retirada, contestada, concluída, pausada ou indisponível. Nesses casos, o destino deve apresentar o estado vigente ou uma alternativa neutra, sem tratar o snapshot de Hoje como fonte soberana.

### 4.4 Retorno

Retornar a Hoje é navegação, não mutação.

Se a Pessoa realizou uma ação substantiva dentro da superfície especializada, qualquer mudança legítima pertence à ação governada nessa superfície. Ao voltar, Hoje pode refletir o estado canônico atualizado somente após revalidação.

Sem ação substantiva:

```text
abrir
→ consultar
→ voltar
≠ criar
≠ iniciar
≠ aceitar
≠ concluir
≠ reconhecer evolução
```

### 4.5 Interrupção

Fechar, abandonar, perder conectividade ou interromper a navegação não produz mutação automática.

Reentrada posterior usa o estado canônico vigente. Retomada específica somente poderá ocorrer quando houver estado legitimamente persistido por uma ação própria da superfície, não pela transição em si.

### 4.6 Concorrência

Se o objeto ou permissão mudar entre origem e destino, prevalece o estado vigente no momento da revalidação.

A transição não pode forçar conteúdo obsoleto, restaurar autorização retirada ou sobrescrever mudança concorrente legítima.

### 4.7 Idempotência

Abrir e voltar repetidamente não pode:

- duplicar Objetivo;
- duplicar Próximo Passo;
- criar evidência;
- marcar item como visto, iniciado ou concluído;
- confirmar interpretação;
- reconhecer evolução;
- gerar nova autorização.

## 5. TRN-008 — Hoje → Meus Objetivos

Entrada materializada no estado recorrente de Hoje por `Meus Objetivos`.

O acesso é genérico por padrão.

Quando Hoje estiver mostrando uma direção claramente vinculada a um Objetivo vigente, uma referência lógica poderá ser preservada para destaque no destino, mas isso não é requisito para abrir `PER-010`.

```text
abrir Meus Objetivos
≠ criar Objetivo
≠ priorizar Objetivo
≠ confirmar sugestão
≠ registrar progresso
```

`TRN-008` permanece `contratada` após D5-C4A.

## 6. TRN-009 — Meus Objetivos → Hoje

O retorno `‹ Hoje` permanece affordance local do `PER-010`.

Retornar:

- não salva edição incompleta silenciosamente;
- não altera prioridade;
- não registra progresso;
- não encerra revisão em aberto;
- não converte visita em evidência.

Se houve ação explícita e concluída em `PER-010`, Hoje pode refletir o novo estado canônico após revalidação.

`TRN-009` permanece `contratada` após D5-C4A.

## 7. TRN-010 — Hoje → Meus Próximos Passos

O rótulo anterior `Abrir passo` é refinado para **`Abrir este passo`**, tornando explícito que a navegação parte do Próximo Passo mostrado em Hoje.

O contexto mínimo pode preservar a referência lógica desse passo para que `PER-011` o destaque, desde que o item continue vigente e autorizado.

Se o passo não estiver mais disponível, `PER-011` abre em estado neutro ou atualizado e informa a mudança sem criar substituição automática.

```text
Abrir este passo
≠ iniciar
≠ aceitar
≠ concluir
≠ transformar proposta em decisão
```

`TRN-010` permanece `contratada` após D5-C4A.

## 8. TRN-011 — Meus Próximos Passos → Hoje

O retorno `‹ Hoje` não marca passo como visto, aceito, iniciado, executado ou concluído.

Se a Pessoa realizou `Iniciar`, `Adiar`, `Revisar`, `Não seguir` ou outra ação explícita dentro de `PER-011`, o efeito pertence à ação governada da superfície. Hoje apenas reconsulta o estado vigente.

`TRN-011` permanece `contratada` após D5-C4A.

## 9. TRN-012 — Hoje → Minha Evolução

A entrada em `PER-012` é deliberadamente **genérica e neutra**.

Hoje apresenta `Minha Evolução` como acesso à capacidade, sem afirmar que:

- houve mudança;
- existe evolução reconhecida;
- há trajetória ativa;
- determinada área sensível está sendo acompanhada.

Por padrão, `TRN-012` não transporta referência de trajetória, área, domínio, interpretação ou evidência a partir de Hoje.

O destino revalida autenticação, privacidade, visibilidade e sensibilidade antes de apresentar qualquer trajetória.

```text
abrir Minha Evolução
≠ reconhecer mudança
≠ confirmar inferência
≠ expor domínio sensível
```

`TRN-012` permanece `contratada` após D5-C4A.

## 10. TRN-013 — Minha Evolução → Hoje

O retorno `‹ Hoje` não confirma:

- interpretação;
- baseline;
- direção;
- mudança;
- evolução;
- compartilhamento.

Hoje não pode transformar uma interpretação `PRELIMINAR — INFERIDA` em afirmação factual após o retorno.

Qualquer síntese futura em Hoje deve preservar a natureza epistemológica do conteúdo e as permissões vigentes. Conteúdo sensível permanece minimizado por padrão.

`TRN-013` permanece `contratada` após D5-C4A.

## 11. Revalidação local de PER-008

O estado recorrente de Hoje é revalidado localmente porque a reformulação:

- torna explícito o acesso consciente às três capacidades especializadas;
- não cria três cards permanentes;
- não cria urgência ou obrigação;
- não afirma evolução;
- não expõe conteúdo sensível nos rótulos;
- clarifica que o passo aberto é o item atualmente mostrado;
- preserva Hoje como síntese recorrente.

Essa revalidação mantém o inventário em **121 SVGs funcionalmente validados / 0 pendentes**.

Ela não constitui validação ponta a ponta das seis transições.

## 12. Maturidade resultante

Após D5-C4A:

```text
PER-008 recorrente — reformulado e revalidado localmente
PER-010 — validado localmente
PER-011 — validado localmente
PER-012 — validado localmente

TRN-008 — contratada
TRN-009 — contratada
TRN-010 — contratada
TRN-011 — contratada
TRN-012 — contratada
TRN-013 — contratada
```

## 13. Gate posterior

A próxima frente lógica, se autorizada separadamente, é **D5-C4B — validação integrada dos seis handoffs**.

A D5-C4B deverá decidir individualmente se cada `TRN-008..013` possui evidência suficiente para promoção, sem assumir que as seis devem receber a mesma maturidade.

D5-C4A não inicia D5-C4B, UXA-102/V5, D6, D7 ou Engenharia de Produto.