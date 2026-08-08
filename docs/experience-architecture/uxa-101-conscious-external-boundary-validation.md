---
id: UXA-101
title: Validação da Saída Consciente para Fronteira Externa de Oportunidades
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
depends_on:
  - UXA-004
  - UXA-007
  - UXA-012
  - UXA-059
  - UXA-098
related:
  - GKR-SURF-PER-203
  - GKR-SURF-BND-001
  - GKR-TRN-205
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.88
normative: false
---

# UXA-101 — Validação da Saída Consciente para Fronteira Externa de Oportunidades

## 1. Objetivo

Encerrar V4 no lado controlado pela Guivos, validando a continuidade documental `PER-203 → TRN-205 → BND-001` sem transformar o destino externo em superfície da Guivos e sem afirmar resultado que dependa de terceiro.

## 2. Escopo

A UXA-101 examina:

- o gatilho a partir do Detalhe da Oportunidade (`PER-203`);
- a revisão consciente imediatamente anterior à saída;
- a identificação explícita do responsável e do destino externo;
- a informação sobre dados/contexto que acompanham ou não a transição;
- cancelamento e retorno ao Detalhe;
- revalidação do destino antes da saída;
- comportamento quando o destino está ausente, inválido ou deixou de ser autorizado;
- idempotência do acionamento;
- o limite de autoridade ao alcançar `BND-001`.

Ficam fora do escopo:

- comportamento interno do site/app de terceiro;
- inscrição, reserva, compra ou contratação externa;
- disponibilidade, pagamento, autenticação ou suporte do terceiro após a fronteira;
- confirmação de resultado externo pela Guivos sem evidência reconciliada;
- criação de nova superfície canônica para a revisão intermediária;
- Engenharia de Produto.

## 3. Decisão de fragmentação

A revisão pré-saída **permanece como estado de `PER-203`**.

Não é criada nova superfície porque o estado preserva:

- a mesma responsabilidade primária: compreender a oportunidade e decidir conscientemente como prosseguir;
- a mesma autoridade Guivos até o momento do handoff;
- o mesmo objeto lógico de oportunidade;
- retorno direto ao Detalhe sem criar novo contexto persistente.

`BND-001` continua sendo uma fronteira, não uma tela Guivos.

## 4. Contrato validado de `TRN-205`

```text
PER-203 — Detalhe da oportunidade
→ Pessoa seleciona “Ver como participar”
→ PER-203 entra em estado de revisão de saída
→ destino externo e responsável são identificados
→ é informado o que acompanha ou não acompanha a transição
→ Pessoa pode cancelar e permanecer na Guivos
→ Pessoa confirma conscientemente “Continuar no site oficial”
→ Guivos revalida o destino conhecido/autorizado
→ TRN-205
→ BND-001 — autoridade externa
```

### 4.1 Antes da confirmação

A interface deve tornar explícitos, em linguagem proporcional:

1. que a próxima etapa ocorrerá fora da Guivos;
2. qual organização ou responsável controla o destino;
3. o domínio, aplicação ou referência de destino quando disponível;
4. quais dados serão enviados pela Guivos, se houver;
5. quais dados **não** são enviados automaticamente;
6. que condições, preço, disponibilidade e elegibilidade podem ser revalidados pelo responsável externo;
7. que continuar não equivale a inscrição, reserva, compra ou contratação concluída.

### 4.2 Confirmação

A saída exige ato afirmativo. A opção de permanecer no Detalhe deve continuar disponível e não pode ser tratada como erro, abandono ou perda de oportunidade.

### 4.3 Revalidação do destino

No momento imediatamente anterior ao handoff, o estado conhecido do destino deve ser revalidado no limite documental aplicável.

Se o destino estiver ausente, inválido, incompatível ou materialmente alterado, a Guivos não deve realizar redirecionamento silencioso. A Pessoa permanece em `PER-203` e recebe explicação e alternativa segura, como retornar, consultar responsável/origem ou atualizar o Detalhe.

### 4.4 Idempotência

Repetir a confirmação não cria duas inscrições, duas reservas ou dois efeitos externos presumidos. A Guivos registra apenas o evento de handoff conforme política aplicável; qualquer efeito posterior pertence à autoridade externa até existir reconciliação autorizada.

## 5. Privacidade e transferência de contexto

A regra padrão é minimização.

- nenhum contexto pessoal sensível ou inferido acompanha a saída por conveniência;
- parâmetros de rastreamento ou atribuição não ampliam consentimento;
- se algum dado identificável precisar ser transferido, finalidade, destinatário e base/autorização aplicável devem estar explicitados antes da confirmação;
- ausência de autorização suficiente impede a transferência, não o acesso a uma alternativa pública quando existir;
- abrir destino externo não autoriza o terceiro a acessar a jornada completa da Pessoa na Guivos.

## 6. Retorno e reconciliação

Retornar posteriormente à Guivos:

- reabre o estado canônico vigente de `PER-203` ou a origem preservada quando aplicável;
- não presume conclusão externa;
- não marca evolução, presença, compra, inscrição ou sucesso automaticamente;
- pode mostrar que a Pessoa saiu para um destino externo apenas quando esse histórico for permitido e útil;
- exige evidência própria para qualquer reconciliação futura de resultado externo.

## 7. Materialização visual reformulada

O ativo `docs/assets/wireframes/uxa-007-opportunity-detail-mobile.svg` é reformulado nesta frente para incluir, no mesmo artefato e sob a mesma responsabilidade `PER-203`, o estado acionado por **“Ver como participar”**.

A reformulação explicita:

- aviso de saída da Guivos;
- responsável/destino;
- tratamento mínimo de dados/contexto;
- ausência de garantia de conclusão externa;
- ações `Continuar no site oficial` e `Voltar ao detalhe`;
- recuperação local quando o destino não puder ser confirmado.

Nenhum SVG de `BND-001` é criado.

## 8. Veredito funcional

### `PER-203`

**Revalidada no recorte de saída externa.** O Detalhe passa a materializar explicitamente o estado de revisão previsto desde UXA-007.

### `GKR-TRN-205`

**Integralmente validada até a fronteira de autoridade da Guivos.** Origem, decisão, dados/contexto, revalidação, retorno, interrupção e idempotência são examinados no lado Guivos.

A expressão acima não significa validação do processo externo. Depois de `BND-001`, a autoridade é do terceiro.

### `GKR-SURF-BND-001`

**Fronteira examinada e confirmada como não pertencente à Guivos.** Não possui tela Guivos por definição.

## 9. Efeito sobre V4

V4 — efeito externo de oportunidades — fica **encerrada no limite documental controlável pela Guivos**.

O que se encerra é o handoff consciente até `BND-001`. Resultados e operações posteriores do terceiro não são absorvidos pela Guivos nem convertidos em validação ponta a ponta de uma experiência externa.

## 10. Preservações

A UXA-101:

- não cria nova responsabilidade canônica;
- não aumenta a contagem de SVGs;
- não altera as 53 superfícies/estados/fronteiras nem as 54 transições existentes;
- não valida `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` ou `TRN-426`;
- não inicia V5;
- não implementa redirect, analytics, consentimento técnico ou integração de terceiros;
- não inicia Engenharia de Produto.
