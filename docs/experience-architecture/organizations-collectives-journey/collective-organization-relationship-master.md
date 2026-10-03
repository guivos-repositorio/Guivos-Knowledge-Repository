---
id: GKR-UX-COL-ORG-RELATIONSHIP-MASTER-001
title: Jornada de Organizações e Coletivos — Coletivo — Relação Organização–Coletivo — Documento Mestre de Superfície
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: false
maturity: functional_contract_candidate
depends_on:
  - UXA-019
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-COL-008
  - GKR-SURF-ORG-004
  - GKR-SURF-ORG-005
  - GKR-SURF-ORG-006
  - GKR-TRN-206
  - GKR-TRN-207
  - GKR-TRN-208
  - GKR-TRN-209
---

# Coletivo — Relação Organização–Coletivo — Documento Mestre de Superfície

## 1. Responsabilidade

Este Master governa `GKR-SURF-COL-008` como a perspectiva do Coletivo sobre o mesmo objeto bilateral Organização–Coletivo contratado por `UXA-019`.

```text
PERSPECTIVA DO COLETIVO
≠ SEGUNDO OBJETO

RELAÇÃO
≠ TRANSFERÊNCIA DE AUTORIDADE

APROVAÇÃO DE UMA PARTE
≠ APROVAÇÃO BILATERAL

RELAÇÃO ATIVA
≠ IMPACTO COMPROVADO
```

O escopo é exclusivamente Organização ↔ Coletivo. Relações Coletivo ↔ Coletivo permanecem lacuna explícita e não usam `COL-008` por analogia.

## 2. Objeto bilateral único

Organização e Coletivo devem operar sobre a mesma identidade lógica da relação, preservando:

- finalidade;
- escopo;
- versão materialmente relevante;
- autoridades;
- compromissos;
- recursos;
- dados;
- limites;
- consentimentos/aprovações;
- condições de proteção;
- histórico material.

Mudança de perspectiva não duplica o objeto nem cria consentimento.

## 3. Handoffs estáveis existentes

O fluxo estável já registrado é:

```text
GKR-SURF-ORG-004
↓ GKR-TRN-206
GKR-SURF-COL-008
↓ GKR-TRN-207
GKR-SURF-ORG-005
↓ GKR-TRN-208
GKR-SURF-ORG-006
↓ GKR-TRN-209
GKR-SURF-ORG-006
```

`GKR-TRN-206..209` permanecem `contratadas`.

Este Master não promove maturidade e não cria transições adicionais.

## 4. TRN-206 — proposta Organização → perspectiva do Coletivo

`TRN-206` disponibiliza ao Coletivo autorizado o mesmo objeto de proposta originado em `ORG-004`.

O handoff deve preservar:

- identidade da proposta;
- Organização proponente;
- finalidade e escopo;
- versão material;
- compromissos e recursos;
- dados e limites relevantes;
- autoridade conhecida;
- condições pendentes;
- proveniência.

Receber/visualizar a proposta não equivale a aprovar, negociar, assumir compromisso ou ativar a relação.

## 5. Job do COL-008

A perspectiva do Coletivo deve permitir, dentro da autoridade aplicável:

1. compreender quem propõe e com qual finalidade;
2. compreender escopo, compromissos, recursos, dados e limites;
3. verificar autoridade própria e da contraparte no limite visível;
4. identificar informação ausente, risco, conflito ou proteção;
5. recusar, solicitar ajuste/informação ou prosseguir legitimamente;
6. compreender alterações materiais e versão vigente;
7. confirmar conscientemente quando a ação produzir efeito material;
8. compreender continuidade, revisão, pausa, contestação e encerramento;
9. preservar autonomia do Coletivo.

## 6. TRN-207 — Coletivo → avaliação/negociação da Organização

`TRN-207` representa o handoff do mesmo objeto bilateral de `COL-008` para `ORG-005`, quando existe continuidade legítima para avaliação/negociação.

Não implica:

- aprovação final;
- ativação;
- aceite silencioso;
- transferência de autoridade;
- concordância com versão futura ainda não aprovada.

Informação/condição material apresentada pelo Coletivo deve manter proveniência e versão.

## 7. TRN-208 — negociação → relação ativa

`TRN-208` permanece `ORG-005 → ORG-006` e só pode representar continuidade para relação ativa no limite já contratado quando as autoridades legítimas aprovaram o mesmo escopo.

```text
NEGOCIAÇÃO
≠ RELAÇÃO ATIVA

APROVAÇÕES DIVERGENTES
≠ APROVAÇÃO BILATERAL

MESMA VERSÃO MATERIAL APROVADA
→ PRÉ-CONDIÇÃO PARA O EFEITO CONTRATADO
```

Este Master não declara efeito técnico além do contrato documental existente.

## 8. TRN-209 — revisão e continuidade do mesmo objeto

`TRN-209` permanece `ORG-006 → ORG-006` para revisão, alteração e continuidade do mesmo objeto bilateral.

Alteração material proposta exige nova avaliação e aprovação bilateral antes de substituir o escopo efetivo.

Até isso ocorrer, o escopo anteriormente aprovado permanece o único escopo efetivo, salvo condição legítima de pausa, bloqueio, proteção ou encerramento já aplicável.

## 9. Lifecycle preservado

Estados funcionais contratados incluem:

- rascunho;
- proposta;
- avaliação bilateral;
- negociação;
- aguardando informação;
- aguardando consentimento/aprovação;
- aprovada pelas autoridades;
- ativa;
- em revisão;
- alteração material pendente;
- renovada ou ajustada;
- pausada;
- bloqueada por proteção ou privacidade;
- contestada;
- suspensa preventivamente;
- expirada;
- encerrada;
- encerrada com responsabilidades remanescentes.

Estados não devem ser colapsados quando mudam autoridade, reversibilidade, obrigação ou proteção.

## 10. Condições alternativas

A perspectiva do Coletivo deve distinguir quando materialmente aplicável:

- proposta recusada;
- autoridade insuficiente;
- aprovação divergente entre as partes;
- relação ativa sem atenção material;
- compromisso atrasado;
- recurso indisponível;
- dado ou consentimento ausente;
- conflito de interesse;
- denúncia em análise;
- suspensão urgente;
- renovação pendente;
- encerramento solicitado por uma das partes;
- risco ou condição de proteção;
- informação sensível protegida;
- evidência insuficiente;
- falha recuperável;
- estado indeterminado.

Ausência ou bloqueio não devem ser apresentados como recusa quando a evidência não sustenta essa conclusão.

## 11. Alterações materiais

Conforme `UXA-019`, mudanças materiais exigem nova avaliação e aprovação bilateral, incluindo quando aplicável mudança de:

- finalidade;
- público;
- tratamento de dados;
- recurso ou obrigação relevante;
- exclusividade;
- autoridade;
- uso de marca;
- operação;
- outra condição material do escopo.

A interface deve tornar a alteração compreensível sem substituir a versão vigente silenciosamente.

## 12. Autoridade bilateral

Cada lado preserva autoridade própria.

O Coletivo não recebe autoridade da Organização por participar da relação; a Organização não recebe autoridade interna do Coletivo.

Planos, investimento, patrocínio, recurso financeiro, volume ou relevância percebida não substituem consentimento e governança.

## 13. Dados, minimização e proteção

Somente dados necessários à finalidade e ao estado podem atravessar perspectivas.

Mudança de perspectiva não autoriza acesso irrestrito a dados internos, perfis pessoais, Journey da Pessoa, mensagens privadas ou governança protegida.

Condições de privacidade/proteção podem limitar continuidade sem fabricar conclusão sobre mérito da relação.

## 14. Confirmação e reversibilidade

Ações materiais devem exigir confirmação proporcional quando aplicável.

Navegar, abrir, ler, alternar contexto, fechar janela ou retornar não pode:

- aprovar proposta;
- aceitar alteração;
- ativar relação;
- renovar;
- pausar;
- encerrar;
- transferir recurso/dado;
- criar compromisso.

## 15. Concorrência, versão e idempotência

Antes de ação material, a versão corrente deve ser revalidada.

Se a contraparte alterar materialmente o objeto, confirmação baseada em versão anterior não vale como aprovação da nova versão.

Repetição após falha/indeterminação deve reconsultar estado canônico para evitar duplicidade de efeito.

## 16. Contestação, proteção e revisão

Contestação não produz retaliação automática nem encerra silenciosamente a relação.

Condição de proteção pode limitar continuidade de forma proporcional e revisável.

Quando a responsabilidade material for de `COL-007`, proteção/moderação permanece sob sua autoridade; o objeto bilateral apenas referencia o estado necessário.

## 17. Encerramento e responsabilidades remanescentes

Encerramento deve tratar, quando aplicável:

- dados;
- recursos;
- comunicações;
- compromissos;
- proteção;
- auditoria/proveniência;
- responsabilidades remanescentes.

`ENCERRADA` e `ENCERRADA COM RESPONSABILIDADES REMANESCENTES` permanecem estados distintos.

Encerrar não apaga histórico material necessário nem fabrica quitação universal.

## 18. Comunicação

Comunicação oficial material relacionada à relação mantém autoridade própria de `COL-005` quando aplicável.

A relação pode exigir comunicação; isso não transforma `COL-008` em superfície genérica de comunicação.

## 19. Resultados e impacto

Relação ativa, recurso aplicado, atividade executada ou compromisso cumprido não equivalem automaticamente a resultado ou impacto.

```text
RELAÇÃO
≠ RESULTADO

RESULTADO
≠ IMPACTO

CORRELAÇÃO
≠ CAUSALIDADE
```

## 20. Planos e capacidade comercial

Planos não alteram:

- autoridade bilateral;
- autonomia;
- peso de aprovação;
- legitimidade de recusa;
- proteção;
- força de evidência.

Nenhum plano pode criar aprovação preferencial ou influência decisória neste Master.

## 21. Acessibilidade

Finalidade, versão, autoridade, compromisso, alteração material, proteção, estado e efeito não podem depender apenas de cor, ícone, posição ou motion.

## 22. Design — liberdade e limites

Design mantém liberdade criativa.

Não pode:

- criar dois objetos independentes para as duas perspectivas;
- esconder versão material;
- transformar visualização em aceite;
- tratar negociação como ativação;
- substituir escopo vigente por alteração não aprovada;
- ampliar `COL-008` para Coletivo↔Coletivo;
- inventar transições;
- usar low-fidelity como baseline visual canônica;
- representar relação ativa como impacto comprovado.

## 23. IA e prototipação — source lock

IA não pode inventar:

- novos critérios de aprovação;
- autoridade;
- pesos de decisão;
- campos obrigatórios além do que os contratos governantes já exigem ou autorizam;
- lifecycle paralelo;
- transições;
- automações;
- métricas;
- efeitos financeiros/técnicos.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 24. Critérios de aceite

A materialização é funcionalmente suficiente quando:

1. `COL-008` representa a perspectiva coletiva do mesmo objeto bilateral;
2. `TRN-206..209` preservam origem, destino e maturidade;
3. proposta recebida não vira aprovação;
4. aprovação exige mesma versão material legitimamente aprovada pelas autoridades aplicáveis;
5. alteração material pendente não substitui o escopo vigente;
6. autonomia e autoridade das partes permanecem separadas;
7. dados são minimizados;
8. contestação/proteção não produzem retaliação automática;
9. encerramento preserva responsabilidades remanescentes quando existentes;
10. relação não é tratada como impacto;
11. Coletivo↔Coletivo permanece fora do escopo;
12. nenhuma nova transição é criada por conveniência.

## 25. Lacunas preservadas

Permanecem abertas:

- validação dedicada ponta a ponta de `TRN-206..209`;
- implementação técnica;
- infraestrutura de assinatura/consentimento quando aplicável;
- execução financeira;
- integrações;
- notificações técnicas;
- analytics/KPIs;
- relações Coletivo↔Coletivo.

## 26. Estado de fechamento documental

```text
SURFACE GOVERNED
→ GKR-SURF-COL-008

OBJECT
→ ONE BILATERAL ORGANIZATION–COLLECTIVE RELATIONSHIP

STABLE TRANSITIONS
→ GKR-TRN-206..209
→ CONTRACTED / MATURITY PRESERVED

COLLECTIVE↔COLLECTIVE
→ OUT OF SCOPE / EXPLICIT GAP

NEW TRANSITION ID
→ NONE

NEW SURFACE ID
→ NONE

TECHNICAL IMPLEMENTATION
→ NOT CLAIMED

END-TO-END VALIDATION
→ NOT CLAIMED
```
