---
id: GKR-UX-COL-PARTICIPANTS-LINKS-MASTER-001
title: Jornada de Organizações e Coletivos — Coletivo — Participantes e Vínculos — Documento Mestre de Superfície
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
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
related:
  - GKR-SURF-COL-003
  - GKR-SURF-COL-004
  - GKR-SURF-COL-005
  - GKR-SURF-PER-106
  - GKR-SURF-PER-108
  - GKR-TRN-113
  - GKR-JOURNEY-COLLECTIVE-001
---

# Coletivo — Participantes e Vínculos — Documento Mestre de Superfície

## 1. Responsabilidade

Este Documento Mestre governa a responsabilidade funcional de `GKR-SURF-COL-004` — Participantes e Vínculos.

A superfície permite que uma Pessoa legitimamente autorizada, atuando no contexto de um Coletivo, compreenda e administre a continuidade de participações e vínculos existentes no limite da autoridade aplicável.

```text
SOLICITAÇÃO APROVADA
≠ VÍNCULO TÉCNICO CONFIRMADO

VÍNCULO CONFIRMADO
≠ PAPEL ACEITO

PAPEL ACEITO
≠ REPRESENTAÇÃO

REPRESENTAÇÃO
≠ ADMINISTRAÇÃO
≠ AUTORIDADE IRRESTRITA
```

`COL-004` não absorve a decisão da solicitação governada por `COL-003` e não transforma pessoas em recurso do Coletivo.

## 2. Por que esta responsabilidade é específica do Coletivo

`COL-004` pertence ao domínio **Participação** e atende a continuidade de `COL-J04`, com partes de `COL-J05` e `COL-J10` quando aplicáveis.

A Organização não possui superfície semanticamente equivalente. Relações Organização–Coletivo são governadas por `ORG-004..006 / COL-008` e não substituem pertencimento ou vínculo de uma Pessoa com um Coletivo.

Consequentemente:

- este Master não é compartilhado por inferência;
- vínculo Pessoa–Coletivo não é relação Organização–Coletivo;
- nenhuma superfície da Organização é criada por simetria;
- diferenças de autoridade permanecem explícitas.

## 3. Participante, contexto e autoridade

O agente humano é uma **Pessoa autenticada** atuando no contexto do Coletivo.

Antes de qualquer ação material, a experiência deve preservar:

- Coletivo ativo correto;
- identidade suficiente do vínculo;
- papel e autoridade de quem atua;
- estado corrente da participação;
- papel aceito, quando existente;
- responsabilidade atribuída, quando legitimamente existente;
- restrição ou condição legítima de participação;
- proteção e finalidade aplicáveis.

```text
PERTENCER
≠ REPRESENTAR
≠ MODERAR
≠ APROVAR
≠ ADMINISTRAR

VER UM VÍNCULO
≠ PODER ALTERÁ-LO

ALTERAR VÍNCULO
≠ ALTERAR AUTORIDADE INSTITUCIONAL
```

Mudança de contexto, sessão expirada ou alteração material de autoridade exige revalidação antes de efeito.

## 4. Origem pós-aprovação e lacuna preservada

A continuidade funcional reconhecida é:

```text
GKR-SURF-COL-003
→ SOLICITAÇÃO APROVADA
→ GKR-SURF-COL-004
```

O Transition Registry registra `GKR-TRN-114 — COL-003 → COL-004` como continuidade operacional do mesmo vínculo já formado pela aprovação. A transição permanece contratada e não constitui prova de persistência técnica.

Portanto:

```text
CONTINUIDADE FUNCIONAL
→ GKR-TRN-114
→ CONTRATADA
→ MESMO VÍNCULO / NOVA RESPONSABILIDADE OPERACIONAL

TRATAMENTO
→ NÃO INVENTAR GKR-TRN
→ NÃO DECLARAR PERSISTÊNCIA AUTOMÁTICA
```

Este Master não transforma a aprovação em prova de criação técnica do vínculo.

## 5. Continuidade para comunicação oficial

Quando houver comunicação oficial aplicável a participantes autorizados, existe continuidade registrada:

```text
GKR-SURF-COL-004
→ GKR-TRN-113
→ GKR-SURF-COL-005
```

`GKR-TRN-113` permanece **contratada**. Este Master não promove sua maturidade.

A existência dessa transição não significa que toda alteração de vínculo exija comunicação oficial nem que `COL-005` seja extensão visual obrigatória de `COL-004`.

## 6. Job principal

A Pessoa autorizada deve conseguir:

1. identificar o Coletivo e o vínculo relevante;
2. compreender quem participa e em qual condição legitimamente registrada;
3. distinguir pertencimento, papel, responsabilidade, representação e administração;
4. compreender o estado corrente da participação;
5. reconhecer restrições, condições ou proteções aplicáveis;
6. identificar ações permitidas pelo próprio papel e autoridade;
7. tratar pausa, continuidade ou saída somente quando sustentadas pela autoridade;
8. reconhecer quando uma comunicação oficial relacionada deve seguir para `COL-005`;
9. compreender resultado confirmado, falha recuperável ou estado indeterminado;
10. retornar ao contexto do Coletivo sem perder a referência canônica.

## 7. Informação e objetos

A Arquitetura da Informação autoriza, quando aplicáveis e necessários:

- pertencimento;
- papel aceito;
- responsabilidade atribuída;
- participação atual quando legitimamente necessária;
- pausa;
- saída;
- vínculo;
- restrição ou condição legítima de participação;
- estado do vínculo;
- informação de autoridade necessária à operação;
- proteção aplicável;
- proveniência e atualidade material.

A superfície não deve inventar por convenção:

- score de participante;
- ranking de participação;
- nível de lealdade;
- valor da Pessoa para o Coletivo;
- produtividade pessoal;
- reputação algorítmica;
- perfil psicológico;
- inferência sensível;
- autoridade baseada em popularidade;
- obrigação de atividade contínua;
- presença mínima universal;
- gamificação coerciva.

## 8. Proveniência e verdade operacional

```text
PERTENCIMENTO REGISTRADO
≠ REPRESENTAÇÃO

PAPEL DECLARADO
≠ PAPEL ACEITO

PAPEL ACEITO
≠ AUTORIDADE IRRESTRITA

RESPONSABILIDADE ATRIBUÍDA
≠ RESPONSABILIDADE ACEITA, QUANDO ACEITE FOR NECESSÁRIO

PAUSA
≠ SAÍDA

SAÍDA SOLICITADA
≠ SAÍDA EFETIVA

AUSÊNCIA DE ATIVIDADE
≠ INATIVIDADE FORMAL
≠ DESINTERESSE
```

Inferência, cache ou ausência de dado não podem substituir o estado canônico.

## 9. Estados mínimos

O State Map reconhece no contexto operacional do Coletivo:

- vínculo de participação ativo;
- participação pausada;
- participação em processo de saída;
- participação encerrada.

A materialização também deve tratar, quando aplicáveis à responsabilidade:

- vínculo aguardando confirmação técnica;
- papel ou responsabilidade pendente de aceite legítimo;
- autoridade insuficiente;
- aprovação adicional necessária;
- condição ou restrição material;
- informação protegida;
- estado contestado;
- bloqueio por proteção, privacidade ou governança;
- processamento em curso;
- falha recuperável;
- resultado indeterminado;
- atualização concorrente;
- contexto ou sessão expirados;
- dependência externa indisponível;
- operação degradada ou baixa conectividade.

```text
ATIVO
≠ AUTORIZADO PARA QUALQUER AÇÃO

PAUSADO
≠ ENCERRADO

EM SAÍDA
≠ ENCERRADO

ENCERRADO
≠ APAGADO

BLOQUEADO
≠ ENCERRADO
```

## 10. Ações e controles

Somente quando estado e autoridade permitirem, a responsabilidade pode oferecer:

- consultar participantes e vínculos;
- abrir um vínculo;
- revisar condição e estado;
- reconhecer aceite já registrado de papel/responsabilidade quando houver autoridade e regra aplicáveis;
- aceitar papel/responsabilidade somente quando a própria Pessoa atuante for a titular da atribuição e a autoridade correspondente permitir; quando o aceite pertencer a outro participante, encaminhar ou preservar a continuidade na perspectiva autorizada dessa Pessoa, sem aceitar em seu nome;
- atualizar informação legitimamente editável;
- pausar participação quando permitido;
- retomar participação quando permitido;
- iniciar saída quando permitido;
- concluir ação pendente legitimamente autorizada;
- retornar sem alterar estado;
- revalidar contexto e autoridade;
- reconsultar estado canônico;
- repetir processamento recuperável sem duplicar efeito;
- seguir para comunicação oficial via `TRN-113` quando aplicável.

A presença de controle visual não concede autoridade.

Este Master não inventa quem pode alterar papel, responsabilidade, vínculo ou autoridade quando essa regra não estiver definida.

## 11. Papel, responsabilidade e aceite

Papel e responsabilidade devem permanecer distinguíveis.

Quando a autoridade aplicável exigir aceite da Pessoa:

```text
RESPONSABILIDADE PROPOSTA
→ ACEITE LEGÍTIMO
→ RESPONSABILIDADE VIGENTE

PROPOSTA
≠ ACEITE

SILÊNCIO
≠ ACEITE
```

O responsável do Coletivo pode reconhecer um aceite legitimamente registrado, mas não pode fornecer o aceite pessoal de outro participante. Quando o aceite depender da Pessoa afetada, a decisão deve ocorrer na perspectiva ou no fluxo autorizado dessa própria Pessoa.

Este Master não cria um mecanismo universal de atribuição de papel nem presume que toda responsabilidade exige o mesmo tipo de aceite.

## 12. Pausa, retomada e saída

Pausa, retomada e saída são operações distintas.

- **pausa** preserva o vínculo no estado permitido sem declarar encerramento;
- **retomada** restabelece continuidade quando autoridade e condições permitirem;
- **saída** inicia ou conclui encerramento da participação conforme autoridade aplicável;
- **encerramento** não implica apagar trilha legítima, obrigação remanescente ou evidência necessária.

```text
PAUSAR
≠ SAIR

SAIR DO COLETIVO
≠ SAIR DA GUIVOS

SAIR DO COLETIVO
≠ CANCELAR PLANO

ENCERRAR VÍNCULO
≠ APAGAR DADOS POR INFERÊNCIA
```

A experiência não deve criar fricção coerciva para impedir uma saída legitimamente permitida.

## 13. Relação com a perspectiva da Pessoa

As superfícies `PER-103..108` permanecem separadas e governam a perspectiva da Pessoa.

`COL-004` não autoriza o Coletivo a acessar por consequência:

- contexto pessoal amplo;
- objetivos privados;
- inferências individuais;
- dados sensíveis não necessários;
- outras relações da Pessoa;
- razões internas de relevância;
- histórico pessoal além da finalidade legítima.

A visão operacional do Coletivo e a experiência pessoal podem refletir o mesmo vínculo sem compartilhar toda a informação.

## 14. Comunicação oficial e TRN-113

Quando a continuidade exigir comunicação oficial a participantes autorizados, `TRN-113` conecta `COL-004` a `COL-005`.

A comunicação deve preservar:

- público autorizado;
- finalidade;
- proteção;
- estado do vínculo;
- necessidade real de comunicação;
- limites de autoridade.

```text
VÍNCULO
≠ CONSENTIMENTO PARA TODA COMUNICAÇÃO

COMUNICAÇÃO OFICIAL
≠ MARKETING

COMUNICAÇÃO OFICIAL
≠ EXPOSIÇÃO PÚBLICA
```

Preferência de comunicação, consentimento, pertencimento e obrigação material não devem ser confundidos.

## 15. Processamento e confirmação

Ações materiais seguem:

```text
INTENÇÃO
→ CONFIRMAÇÃO CONSCIENTE, QUANDO APLICÁVEL
→ PROCESSAMENTO
→ SUCESSO CONFIRMADO
  OU FALHA RECUPERÁVEL
  OU RESULTADO INDETERMINADO
```

Regras:

- interface otimista não substitui confirmação;
- retry não pode duplicar efeito material;
- resultado indeterminado exige reconsulta antes de repetir;
- mudança de contexto exige revalidação;
- sucesso técnico não deve ser confundido com mudança de autoridade quando forem estados distintos.

## 16. Vazio, erro, indisponibilidade e recuperação

A experiência deve tratar explicitamente:

- nenhum participante ou vínculo aplicável;
- vínculo não localizado;
- estado ainda não confirmado;
- informação material ausente;
- informação protegida;
- dado desatualizado ou contestado;
- autoridade insuficiente;
- aprovação adicional pendente;
- dependência indisponível;
- processamento interrompido;
- resultado desconhecido;
- atualização concorrente;
- contexto expirado;
- baixa conectividade.

Estado vazio não é falha do Coletivo.

Erro técnico não deve ser apresentado como falha moral, administrativa ou da Pessoa participante.

## 17. Reversibilidade, interrupção e idempotência

```text
VOLTAR
≠ PAUSAR

FECHAR
≠ SAIR

CANCELAR UMA INTENÇÃO
≠ ENCERRAR VÍNCULO

RETRY
≠ REPETIR EFEITO MATERIAL

MUDAR DE CONTEXTO
→ REVALIDAR AUTORIDADE
```

Ações irreversíveis ou materialmente relevantes não podem ocorrer por navegação, fechamento de janela ou simples troca de contexto.

## 18. Proteção, privacidade e não retaliação

Participação não autoriza vigilância ampla.

Pausa, saída, contestação, baixa atividade ou recusa de responsabilidade não podem ser usadas automaticamente para:

- retaliar;
- reduzir direitos sem base legítima;
- produzir ranking oculto;
- inferir desinteresse;
- expor dados;
- ampliar autoridade do Coletivo sobre outros contextos.

Proteção e moderação especializadas permanecem responsabilidade própria de `COL-007` quando aplicáveis.

## 19. Planos e capacidade comercial

Planos do Coletivo permanecem capacidade especializada/contextual.

Este Master não autoriza:

- vínculo privilegiado por plano;
- autoridade maior por contratação;
- ranking de participantes por capacidade comercial;
- bloquear saída para induzir upgrade;
- inventar limite de participantes;
- inventar entitlement de papéis;
- converter pertencimento em funil de upsell.

Se um limite comercial real e documentado afetar capacidade operacional, ele deve ser explicado sem alterar pertencimento, legitimidade ou autoridade por inferência.

## 20. Acessibilidade

Estado do vínculo, papel, autoridade, proteção, pausa, saída, processamento, erro e confirmação não podem depender exclusivamente de:

- cor;
- ícone;
- posição;
- animação;
- hover;
- blur;
- densidade;
- contraste implícito.

A operação deve permanecer compreensível e acionável por meios acessíveis.

## 21. Liberdade de Design

Design mantém liberdade sobre:

- composição;
- grid;
- navegação local;
- componentes;
- hierarquia visual;
- número de frames;
- tipografia dentro da autoridade oficial;
- imagens e ícones;
- densidade;
- motion;
- solução responsiva.

Design não pode:

- fundir `COL-003`, `COL-004` e `COL-005` por conveniência;
- tratar `GKR-TRN-114` como nova aprovação, novo vínculo ou confirmação técnica automática;
- promover `TRN-113`;
- transformar participantes em ranking ou dashboard obrigatório;
- criar métricas sem autoridade;
- ocultar estado, proteção ou autoridade;
- representar processamento como sucesso;
- usar low-fidelity como baseline visual canônica.

## 22. IA e prototipação — source lock

IA pode explorar forma de materialização, mas não pode inventar:

- campos;
- papéis;
- responsabilidades;
- critérios de pertencimento;
- autoridade;
- ações;
- estados;
- transições;
- automações;
- rankings;
- scores;
- notificações;
- integrações;
- permissões;
- entitlement;
- persistência;
- regra de saída.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 23. Critérios de aceite

Este Master é funcionalmente suficiente quando a materialização:

1. preserva `COL-004` como responsabilidade distinta de `COL-003` e `COL-005`;
2. identifica claramente Coletivo, vínculo, estado, papel e autoridade aplicáveis;
3. preserva `GKR-TRN-114` como handoff estável entre decisão da solicitação e gestão do vínculo, sem duplicar `GKR-TRN-108`;
4. consome `TRN-113` como contratado, sem promoção;
5. não confunde pertencimento, papel, representação, administração e autoridade;
6. suporta ativo, pausa, saída e encerramento sem tratá-los como equivalentes;
7. não transforma ausência de atividade em conclusão sobre a Pessoa;
8. preserva minimização e separação da perspectiva da Pessoa;
9. não cria ranking, score ou vigilância de participantes;
10. preserva saída legítima sem coerção;
11. mantém proteção/moderação especializada em `COL-007`;
12. mantém Planos como capacidade especializada/contextual;
13. preserva reversibilidade e idempotência;
14. mantém IA em source lock;
15. não cria IDs, não promove maturidade e não libera Product Engineering.

## 24. Lacunas preservadas

Permanecem fora deste Master até autoridade específica:

- regras técnicas finais de criação e persistência de vínculo;
- modelo técnico de papéis e responsabilidades;
- RBAC técnico;
- regras não documentadas de aceite;
- integrações externas;
- notificações finais;
- analytics e KPIs;
- entitlement técnico;
- high-fidelity final;
- protótipo;
- implementação;
- Product Engineering.

## 25. Estado documental

```text
MASTER
→ DRAFT / FUNCTIONAL CONTRACT CANDIDATE

SURFACE GOVERNED
→ GKR-SURF-COL-004

POST-APPROVAL ORIGIN
→ GKR-SURF-COL-003
→ GKR-TRN-114 / CONTRACTED / SAME LINK CONTINUITY

OFFICIAL COMMUNICATION CONTINUITY
→ GKR-TRN-113
→ GKR-SURF-COL-005
→ CONTRACTED / MATURITY PRESERVED

ORGANIZATION EQUIVALENT
→ NONE BY INFERENCE

NEW SURFACE ID
→ NONE

NEW TRANSITION ID
→ NONE

MATURITY PROMOTION
→ NONE

LOW-FIDELITY
→ FUNCTIONAL EVIDENCE / NOT VISUAL BASELINE

PROTOTYPE
→ NOT AUTHORIZED BY THIS MASTER

PRODUCT ENGINEERING
→ NOT RELEASED
```
