---
id: GKR-UX-COL-PROTECTION-MODERATION-MASTER-001
title: Jornada de Organizações e Coletivos — Coletivo — Proteção e Moderação — Documento Mestre de Superfície
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-058
related:
  - GKR-SURF-COL-005
  - GKR-SURF-COL-006
  - GKR-SURF-COL-007
  - GKR-SURF-COL-008
---

# Coletivo — Proteção e Moderação — Documento Mestre de Superfície

## 1. Responsabilidade

Este Documento Mestre governa `GKR-SURF-COL-007` — Proteção e Moderação.

A superfície existe para permitir que condições legítimas de proteção, privacidade, segurança, integridade e moderação sejam compreendidas, avaliadas e tratadas por autoridade proporcional, com possibilidade de contestação, revisão ou encaminhamento quando aplicável.

```text
PROTEÇÃO
≠ PUNIÇÃO AUTOMÁTICA

MODERAÇÃO
≠ AUTORIDADE IRRESTRITA

DENÚNCIA
≠ VIOLAÇÃO CONFIRMADA

CONTESTAÇÃO
≠ RETALIAÇÃO
```

## 2. Fronteiras

- `COL-005` governa comunicação oficial material.
- `COL-006` governa atividade, consulta e decisão.
- `COL-007` governa proteção e moderação.
- `COL-008` governa relação Organização–Coletivo no escopo próprio.

Uma decisão de governança não se torna medida de moderação por conveniência. Comunicação sobre moderação não transfere a responsabilidade material de proteção para `COL-005`.

## 3. Autoridade e proporcionalidade

Ação material de proteção/moderação exige:

- contexto correto;
- finalidade limitada;
- autoridade específica;
- evidência suficiente para a ação permitida;
- proporcionalidade;
- minimização;
- proteção contra exposição indevida;
- revisão/recurso quando aplicável.

Acesso administrativo, vínculo, plano ou apoio financeiro não ampliam autoridade de proteção automaticamente.

## 4. Entrada funcional

`COL-007` pode tornar-se aplicável quando existir condição material de:

- segurança;
- privacidade;
- acessibilidade;
- integridade;
- moderação;
- denúncia;
- conteúdo/informação protegida;
- conflito ou contestação que exija tratamento especializado.

A relação entre outra superfície e `COL-007` não equivale a transição registrada. Este Master não cria nova `GKR-TRN-*`.

## 5. Informação mínima e proveniência

O tratamento deve preservar, no limite autorizado:

- natureza da condição;
- relato ou origem;
- contexto;
- evidências mínimas disponíveis;
- estado;
- autoridade responsável;
- medida ou encaminhamento;
- motivo;
- efeito;
- possibilidade de revisão/recurso quando aplicável;
- proveniência e histórico material necessários.

Informação protegida não deve ser exposta integralmente apenas para explicar uma medida.

## 6. Estados funcionais

Estados canônicos incluem, conforme aplicáveis:

- proteção regular;
- proteção requerida;
- conteúdo/informação protegida;
- denúncia/relato recebido sem conclusão automática;
- em avaliação;
- evidência insuficiente;
- evidência conflitante;
- evidência contestada;
- fonte indisponível;
- medida proporcional pendente;
- medida material aplicada;
- decisão contestada;
- conflito de governança;
- revisão necessária;
- recurso apresentado;
- decisão revisada;
- conteúdo restaurado quando legitimamente aplicável;
- nenhuma violação confirmada;
- encerrada;
- falha recuperável;
- estado indeterminado.

Nenhum estado de acusação ou denúncia deve ser apresentado como violação confirmada antes de autoridade/evidência suficientes.

## 7. Medidas materiais

Medidas materiais devem informar motivo, efeito, autoridade e recurso, salvo quando a exposição dessas informações aumentar risco real.

Uma medida pode ser limitada, temporária, revisável ou encerrada conforme autoridade aplicável.

Este Master não inventa catálogo universal de sanções, duração, strikes, pontuação, reputação ou escalonamento automático.

## 8. Não retaliação

Perguntar, discordar, recusar convite, silenciar, bloquear, denunciar, contestar ou sair não produz automaticamente:

- perda de reputação;
- exposição pública;
- restrição de direitos;
- exclusão de oportunidade;
- pressão por contato externo;
- marcação negativa oculta.

Medida legítima depende de fato, autoridade, proporcionalidade e possibilidade de revisão quando aplicável.

## 9. Contestação, revisão e recurso

Contestação não apaga o estado anterior nem produz reversão automática.

Quando aplicável, a experiência deve permitir compreender:

- o que está sendo contestado;
- fundamento conhecido;
- autoridade responsável;
- efeito corrente;
- informação protegida que não pode ser exibida;
- possibilidade de revisão/recurso;
- resultado da revisão quando confirmado.

```text
CONTESTAR
≠ REVERTER AUTOMATICAMENTE

REVISAR
≠ APAGAR HISTÓRICO

RECURSO
≠ GARANTIA DE RESULTADO
```

## 10. Relação com COL-006

Atividade, consulta ou decisão pode originar condição de proteção, mas `COL-006` não absorve a avaliação especializada de moderação.

Da mesma forma, `COL-007` não substitui a autoridade de governança de `COL-006` para registrar decisões coletivas.

Nenhum handoff `COL-006 ↔ COL-007` recebe novo ID sem evidência no Transition Registry.

## 11. Relação com COL-005

Quando uma medida ou condição exigir comunicação oficial legítima, `COL-005` mantém sua responsabilidade própria.

Comunicar uma medida não equivale a decidir a medida.

Nenhum handoff `COL-007 ↔ COL-005` recebe novo ID por inferência.

## 12. Pessoas, vínculos e privacidade

Proteção/moderação não concede acesso irrestrito a:

- perfil pessoal;
- Journey da Pessoa;
- relações externas;
- dados não necessários;
- mensagens privadas fora da autoridade aplicável.

Pertencimento ao mesmo Coletivo não elimina minimização, consentimento ou proteção.

## 13. Confirmação e processamento

Ações materiais difíceis de reverter exigem confirmação proporcional quando aplicável.

```text
PROCESSANDO
≠ APLICADO

RELATO RECEBIDO
≠ VIOLAÇÃO CONFIRMADA

MEDIDA APLICADA
≠ CASO IRREVERSIVELMENTE ENCERRADO
```

Falha ou indeterminação exige reconsulta ao estado canônico antes de repetir ação que possa duplicar efeito.

## 14. Concorrência e histórico

Mudança concorrente de evidência, autoridade, medida ou estado exige revalidação.

Histórico material necessário à integridade, accountability e revisão não deve ser reescrito silenciosamente.

Correção legítima deve preservar relação com a informação anterior quando necessário.

## 15. Erro e recuperação

Devem ser distinguíveis:

- autoridade insuficiente;
- evidência insuficiente;
- informação protegida;
- dependência indisponível;
- conflito de governança;
- ação interrompida;
- falha recuperável;
- estado indeterminado;
- revisão pendente.

Ausência de evidência suficiente não deve ser convertida em culpa ou inocência universal; sustenta apenas a afirmação permitida pela evidência disponível.

## 16. Planos e capacidade comercial

Planos não alteram:

- direito a proteção;
- proporcionalidade;
- legitimidade de denúncia;
- autoridade de moderação;
- peso de recurso;
- privacidade;
- força da evidência.

Não existe moderação prioritária, punição ampliada ou proteção reduzida por plano neste Master.

## 17. Acessibilidade

Estado, risco, autoridade, efeito, proteção, revisão e resultado não podem depender exclusivamente de cor, ícone, posição ou motion.

Informação necessária para compreender uma medida deve ser acessível no limite permitido pela proteção.

## 18. Design — liberdade e limites

Design mantém liberdade criativa de composição e componentes.

Não pode:

- transformar denúncia em culpa visual;
- transformar moderação em ranking;
- expor informação protegida para justificar estado;
- esconder contestação/revisão material;
- confundir proteção com decisão coletiva;
- confundir comunicação com medida;
- inventar transição;
- inventar score de risco/reputação;
- usar low-fidelity como baseline visual canônica.

## 19. IA e prototipação — source lock

IA não pode inventar:

- sanções;
- critérios de violação;
- duração de medidas;
- níveis de severidade;
- score;
- automação decisória;
- autoridade;
- acesso a dados;
- regras de recurso;
- transições.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 20. Critérios de aceite

A materialização é funcionalmente suficiente quando:

1. preserva `COL-007` como responsabilidade própria de proteção/moderação;
2. distingue denúncia de violação confirmada;
3. exige autoridade, finalidade e proporcionalidade;
4. preserva minimização e informação protegida;
5. apresenta motivo, efeito, autoridade e recurso para medidas materiais quando aplicável;
6. preserva não retaliação;
7. permite compreender contestação/revisão sem reversão automática;
8. não absorve `COL-005` ou `COL-006`;
9. trata concorrência, falha e indeterminação;
10. não cria sanções, scores ou automações sem autoridade;
11. não cria transições por simetria.

## 21. Lacunas preservadas

Permanecem abertas:

- handoffs específicos de entrada/saída de `COL-007`;
- cadeia estável de transições;
- catálogo técnico de medidas;
- infraestrutura de moderação;
- regras específicas por contexto protegido;
- automações;
- SLAs;
- analytics/KPIs;
- validação dedicada ponta a ponta;
- implementação.

## 22. Estado de fechamento documental

```text
SURFACE GOVERNED
→ GKR-SURF-COL-007

PRIMARY RESPONSIBILITY
→ PROTECTION / MODERATION

REPORT
→ NOT AUTOMATICALLY CONFIRMED VIOLATION

MATERIAL MEASURE
→ AUTHORITY + PURPOSE + PROPORTIONALITY

CONTESTATION / REVIEW
→ PRESERVED

NEW TRANSITION ID
→ NONE

NEW SURFACE ID
→ NONE

TECHNICAL IMPLEMENTATION
→ NOT CLAIMED

END-TO-END VALIDATION
→ NOT CLAIMED
```
