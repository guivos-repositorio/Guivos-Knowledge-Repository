---
id: GKR-UX-PER014-MASTER-001
title: Jornada da Pessoa — PER-014 — Perguntas Opcionais Guiadas — Documento Mestre de Superfície
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-JOURNEY-PERSON-FUNCTIONAL-COMPLETENESS-001
  - GKR-SURF-PER-003
  - GKR-SURF-PER-005
  - GKR-DATA-PRIVACY-CONSENT-001
related:
  - GKR-TRN-016
  - GKR-TRN-017
  - GKR-SURF-PER-004
  - GKR-SURF-PER-006
---

# Jornada da Pessoa — PER-014 — Perguntas Opcionais Guiadas — Documento Mestre de Superfície

## 1. Finalidade

Este documento governa a responsabilidade funcional corrente de Perguntas Opcionais escolhida conscientemente em `PER-003`.

`PER-014` permite à Pessoa responder, pular, manter em aberto, revisar, corrigir ou remover respostas de um fluxo guiado opcional antes de entregar o conjunto revisado a `PER-005 — Inventário e Autorização`.

```text
PER-003 / PERGUNTAS OPCIONAIS
→ TRN-016
→ PER-014 — PERGUNTAS OPCIONAIS GUIADAS
→ TRN-017
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
```

A responsabilidade funcional não determina uma nova tela visual. Superfície funcional, estado e composição visual permanecem conceitos distintos.

## 2. Fronteiras semânticas

```text
ESCOLHER PERGUNTAS OPCIONAIS ≠ RESPONDER
RESPONDER ≠ AUTORIZAR PROCESSAMENTO
PULAR ≠ RECUSAR A JORNADA
NÃO SEI ≠ INSUFICIÊNCIA
PREFIRO NÃO INFORMAR ≠ ERRO
AUSÊNCIA DE RESPOSTA ≠ DADO A SER INFERIDO
CONCLUIR REVISÃO ≠ AUTORIZAR COMPREENSÃO
```

`PER-014` não é a pergunta adaptativa de apoio de `PER-004`. A pergunta adaptativa pertence a um fluxo já iniciado por Texto ou Voz e depende de solicitação consciente de ajuda.

## 3. Job funcional

A Pessoa deve conseguir:

1. compreender que o fluxo é opcional;
2. compreender a finalidade da pergunta antes de decidir responder;
3. responder livremente quando aplicável;
4. pular sem penalidade;
5. declarar `não sei`, `prefiro não informar` ou equivalente quando materialmente necessário;
6. revisar e corrigir respostas;
7. remover respostas;
8. voltar a perguntas anteriores quando aplicável;
9. interromper o fluxo;
10. retomar somente quando houver suporte legítimo e estado preservado;
11. concluir conscientemente o conjunto;
12. entregar respostas revisadas ao inventário sem autorização material implícita.

## 4. Origem e entrada

A origem corrente é `TRN-016 — PER-003 → PER-014`, após escolha explícita de Perguntas Opcionais.

A transição não pode:

- responder automaticamente;
- iniciar questionário compulsório;
- presumir consentimento;
- converter preferência de modalidade em autorização material;
- pré-selecionar respostas;
- ocultar Texto, Voz ou Arquivo como alternativas legítimas.

## 5. Estados funcionais

A experiência deve comportar, quando aplicável:

- orientação inicial;
- pergunta disponível;
- pergunta respondida;
- resposta livre em edição;
- pergunta pulada;
- `não sei`;
- `prefiro não informar`;
- pergunta mantida em aberto;
- resposta corrigida;
- resposta removida;
- revisão do conjunto;
- fluxo interrompido;
- retomada legítima;
- falha recuperável;
- estado indisponível quando tecnicamente comprovado;
- conjunto revisado e pronto para `TRN-017`.

Nenhum estado de ausência deve ser convertido em avaliação negativa da Pessoa.

## 6. Perguntas e finalidade

Cada pergunta deve possuir finalidade compreensível e proporcional ao momento da jornada.

A experiência não deve:

- usar profundidade como objetivo em si;
- criar cadastro obrigatório disfarçado;
- solicitar dado sem necessidade funcional;
- transformar curiosidade analítica em necessidade;
- exigir dado sensível apenas porque ele poderia melhorar personalização;
- apresentar inferência como resposta fornecida.

Quando uma pergunta envolver dado sensível ou finalidade adicional, aplicam-se as autoridades específicas de privacidade, minimização e autorização.

## 7. Resposta e liberdade

Quando aplicável, a Pessoa pode:

- responder em formato permitido;
- usar resposta livre;
- pular;
- manter em aberto;
- indicar que não sabe;
- indicar que prefere não informar;
- corrigir;
- remover.

Não responder não deve reduzir artificialmente acesso, gerar pressão, culpa, score, ranking ou afirmação de baixa qualidade da jornada.

Se determinada informação for realmente necessária para uma operação específica, essa necessidade deve ser explicada no contexto correto e não retroativamente convertida em obrigatoriedade desta modalidade opcional.

## 8. Sequência e profundidade

A sequência pode ser adaptada somente dentro da finalidade autorizada e sem transformar adaptação em inferência material não revisável.

A quantidade de perguntas deve ser proporcional. O GKR não define número fixo, duração ou árvore universal nesta autoridade.

A experiência deve permitir conclusão consciente sem exigir exaustão de todas as perguntas possíveis.

## 9. Revisão

Antes do handoff, a Pessoa deve conseguir reconhecer o conjunto produzido.

A revisão deve distinguir:

- resposta fornecida;
- pergunta pulada;
- dimensão mantida em aberto;
- resposta removida;
- conteúdo eventualmente derivado, se legitimamente existente e governado separadamente.

Alteração material exige revisão aplicável antes da continuidade.

## 10. Interrupção, retorno e retomada

A Pessoa pode interromper sem que isso seja apresentado como falha pessoal.

O retorno pode preservar respostas já produzidas somente quando houver autoridade e suporte técnico legítimos.

Retomada não pode:

- inventar resposta;
- restaurar silenciosamente conteúdo removido;
- alterar `não sei` ou `prefiro não informar`;
- presumir autorização de processamento.

## 11. Falha e recuperação

Falhas possíveis incluem, quando reais:

- indisponibilidade ao carregar pergunta;
- falha ao registrar resposta;
- perda de conexão;
- estado indeterminado após tentativa de salvar;
- falha ao corrigir ou remover;
- conflito de estado em retomada.

A recuperação deve evitar duplicação silenciosa e preservar a última condição comprovável. Quando o estado for indeterminado, a interface deve tratá-lo como indeterminado.

## 12. Handoff para PER-005

`TRN-017 — PER-014 → PER-005` entrega apenas o conjunto revisado aplicável.

O handoff deve preservar:

- proveniência das respostas;
- perguntas puladas ou dimensões abertas quando isso for necessário para não inventar completude;
- remoções;
- distinção entre conteúdo fornecido e derivado;
- ausência de autorização material.

```text
RESPOSTAS REVISADAS
→ INVENTÁRIO
≠
AUTORIZAÇÃO PARA PREPARAR COMPREENSÃO
```

A autorização específica permanece em `PER-005`.

## 13. Relação com PER-004, PER-005 e PER-006

`PER-004` permanece exclusivo para expressão por Texto/Voz e suas ajudas temporárias.

`PER-005` permanece o gate de inventário e autorização.

`PER-006` permanece responsável pelo processamento visível posterior a conteúdo autorizado.

`PER-014` não absorve nenhuma dessas responsabilidades.

## 14. Privacidade e minimização

A modalidade deve aplicar minimização desde a formulação da pergunta.

Devem permanecer distinguíveis:

- dado declarado pela Pessoa;
- ausência de dado;
- inferência;
- derivação;
- autorização de uso.

Consentimento, preferência de comunicação, aceite contratual e autorização de processamento não são equivalentes.

## 15. Acessibilidade

A futura experiência deve permitir:

- navegação por teclado quando aplicável;
- identificação compreensível da pergunta e finalidade;
- alternativas não dependentes apenas de cor;
- leitura clara de estado respondido/pulado/em aberto;
- correção e remoção acessíveis;
- tempo suficiente para responder ou interromper;
- recuperação compreensível de falhas.

## 16. Liberdade de Design

Este Master não define grid, tipografia de composição, cor, ilustração, motion, quantidade de telas ou disposição visual.

A autoridade governa significado, estados, controles, limites e continuidade.

## 17. Limites para IA

IA não pode:

- responder pela Pessoa;
- inferir resposta a partir de silêncio;
- transformar pergunta opcional em obrigatória;
- ocultar `pular`, `não sei` ou `prefiro não informar` quando materialmente necessários;
- inventar finalidade;
- ampliar uso da resposta;
- apresentar inferência como fato declarado;
- promover maturidade de transição;
- decidir autorização material.

## 18. Critérios de aceitação funcional

Uma exploração futura é coerente quando:

1. Perguntas Opcionais continua opcional;
2. a finalidade é compreensível;
3. pular é legítimo;
4. não saber é legítimo;
5. preferir não informar é legítimo;
6. resposta livre existe quando aplicável;
7. respostas são revisáveis;
8. interrupção é possível;
9. falhas possuem recuperação proporcional;
10. ausência não vira inferência;
11. `TRN-017` entrega inventário sem autorização implícita;
12. `PER-004`, `PER-005` e `PER-006` permanecem preservados.

## 19. Gaps explícitos

Permanecem fora deste contrato:

- catálogo real de perguntas;
- regras concretas de adaptação;
- persistência técnica;
- retenção;
- sincronização;
- implementação;
- evidência de produção;
- baseline visual;
- promoção de maturidade além do estado candidato.

## 20. Estado

```text
PER-014
→ RESPONSABILIDADE FUNCIONAL ADJUDICADA / CURRENT

TRN-016 / TRN-017
→ CONTRACTED / UNCHANGED

PER-004
→ PRESERVADO

PER-005
→ GATE DE AUTORIZAÇÃO PRESERVADO

PER-006
→ PRESERVADO

VISUAL BASELINE
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```
