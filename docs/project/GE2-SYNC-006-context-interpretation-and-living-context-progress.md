---
id: GE2-SYNC-006
title: Context Interpretation and Living Context Progress Sync
status: completed
version: 1.0.0
owner: Guivos
last_updated: 2026-07-04
scope: PAS-001 capabilities, context interpretation, living context and public guide alignment
supersedes_partial:
  - GE2-SYNC-005
---

# GE2-SYNC-006 — Context Interpretation and Living Context Progress Sync

## 1. Finalidade

Este documento registra as decisões tomadas após o `GE2-SYNC-005`, consolida o avanço do `PAS-001 — Guivos Journey` e sincroniza a narrativa pública da Guivos com a evolução funcional do produto.

## 2. Decisões de direção

| ID | Decisão | Estado |
|---|---|---|
| D-054 | Manter Product Engineering como frente operacional vigente | Aprovada |
| D-055 | Especificar o Journey por capacidades funcionais completas | Aprovada |
| D-056 | Parar de evoluir o método enquanto não surgir problema real de execução | Aprovada |
| D-057 | Tratar Captura de Contexto como Capacidade 01 | Aprovada |
| D-058 | Tratar Contexto Vivo como Capacidade 02 | Aprovada |
| D-059 | Separar Captura, Interpretação e Construção do Contexto Vivo | Aprovada |
| D-060 | Adotar o Ciclo Cognitivo do Domínio como padrão funcional | Aprovada |
| D-061 | Exigir uma pergunta central e um contrato de aceite para cada capacidade | Aprovada |

## 3. Padrão de capacidade funcional

Cada capacidade do PAS deverá responder uma pergunta central e conter, quando aplicável:

1. objetivo;
2. valor entregue;
3. responsabilidades e limites;
4. entradas;
5. ciclo cognitivo;
6. fluxo do participante;
7. fluxo do sistema;
8. estados;
9. regras de negócio;
10. exceções;
11. privacidade e consentimento;
12. integrações;
13. eventos produzidos;
14. KPIs;
15. cenários completos;
16. contrato da capacidade.

## 4. Capacidade 01 — Captura de Contexto

Pergunta central:

> Como a Guivos começa a compreender um participante?

A Capacidade 01 foi detalhada com:

- voz como canal prioritário, mas não exclusivo;
- texto e fluxo guiado como alternativas equivalentes;
- escuta livre, sem formulário extenso obrigatório;
- reflexão da compreensão antes da recomendação;
- confirmação, correção, complementação, ocultação e limitação;
- perguntas complementares apenas quando necessárias;
- níveis progressivos de profundidade;
- tratamento superior para temas sensíveis;
- resposta inicial de valor após confirmação;
- exceções e critérios de sucesso.

Decisão de aceite:

> A primeira conversa termina quando o participante confirma que foi compreendido e recebe um primeiro caminho útil, não quando completa um cadastro.

## 5. Interpretação do Contexto

A Interpretação do Contexto transforma entradas autorizadas em compreensão coerente, explicável e utilizável.

Ela deve distinguir:

- fatos;
- intenções;
- objetivos;
- limitações;
- preferências;
- emoções percebidas sem diagnóstico;
- incertezas;
- hipóteses e inferências.

Toda interpretação relevante deve preservar proveniência, temporalidade, confiança, possibilidade de revisão e explicação ao participante.

## 6. Ciclo cognitivo

O padrão funcional consolidado é:

```text
Informação
  -> Interpretação
  -> Compreensão
  -> Contexto
  -> Decisão
  -> Ação
  -> Resultado
  -> Aprendizado
  -> Nova informação
```

Este padrão nasce no Journey e poderá ser promovido futuramente para arquitetura transversal somente após validação prática suficiente.

## 7. Capacidade 02 — Contexto Vivo

Pergunta central:

> Como a Guivos mantém uma representação viva, confiável, explicável e continuamente evolutiva do participante?

### Definição funcional

O Contexto Vivo não representa a realidade absoluta do participante. Ele representa a melhor compreensão que a Guivos possui sobre essa realidade em determinado momento, construída a partir de informações, evidências, interpretações e confirmações autorizadas.

### Atributos obrigatórios da representação

- contextual;
- temporal;
- explicável;
- revisável;
- controlável pelo participante.

### Princípio da Representação Humilde

> A Guivos nunca presume conhecer completamente o participante. Ela mantém continuamente a melhor representação possível de sua realidade, sempre aberta à revisão, ao aprendizado e à confirmação.

## 8. Dimensões de compreensão

O Contexto Vivo será tratado como modelo multidimensional de compreensão, não como supercadastro.

Dimensões iniciais:

1. Identidade;
2. Momento;
3. Direção;
4. Capacidades;
5. Restrições;
6. Preferências;
7. Relacionamentos;
8. Evolução.

Uma mesma mudança pode afetar múltiplas dimensões, sem exigir reconstrução integral nem presumir alterações sem evidência.

### Princípio da Evolução Independente das Dimensões

> Cada dimensão do Contexto Vivo evolui de forma independente. Uma alteração poderá impactar outras dimensões, mas não deverá presumir mudanças onde não existam evidências suficientes.

## 9. Ciclo de vida da informação

Estados funcionais iniciais:

```text
Observada
  -> Interpretada
  -> Confirmada
  -> Ativa
  -> Envelhecida
  -> Substituída
  -> Arquivada
```

A Guivos deverá preservar histórico, origem, validade temporal e justificativa das mudanças relevantes.

## 10. Interface conceitual

O participante deverá poder acessar uma visão pública e simples semelhante a `Meu Contexto Hoje`, contendo:

- foco principal;
- mudanças recentes;
- objetivos ativos;
- próximos passos;
- temas acompanhados;
- informações que podem precisar de atualização;
- última revisão.

Também deverá conseguir responder:

- o que a Guivos entende sobre mim;
- por que ela entende isso;
- quando essa compreensão foi atualizada;
- como corrigir, ocultar, limitar ou remover informações.

## 11. Sequência de capacidades do Journey

| Capacidade | Estado |
|---|---|
| 01 — Captura de Contexto | Functional specification substantially complete |
| 02 — Contexto Vivo | In progress |
| 03 — Objetivos | Planned |
| 04 — Eventos de Vida | Planned / concept consolidated |
| 05 — Próximos Passos | Planned |
| 06 — Oportunidades Ativas | Planned / concept consolidated |
| 07 — Intervenções Contextuais | Planned / concept consolidated |
| 08 — Experiências | Planned |
| 09 — Evolução Contínua | Planned |

## 12. Atualização pública

O `GOG-001 — Guia Oficial da Guivos` deverá explicar publicamente que:

- a Guivos constrói compreensão progressiva, e não apenas cadastro inicial;
- essa compreensão acompanha mudanças de vida, objetivos e prioridades;
- a plataforma apresenta sua leitura para revisão e correção;
- recomendações mudam conforme o contexto evolui;
- o participante permanece no controle.

Termos internos como LPM, CIE, modelo multidimensional, Distância para Evolução e Intelligence Engines permanecem fora da narrativa pública como arquiteturas concluídas.

## 13. Ponto exato de retomada

Retomar no `PAS-001 — Guivos Journey`, Capacidade 02 — Contexto Vivo, detalhando:

1. responsabilidades e limites;
2. entradas e saídas;
3. estados de cada dimensão;
4. regras de envelhecimento e atualização;
5. resolução de conflitos;
6. interface `Meu Contexto Hoje`;
7. eventos produzidos;
8. critérios de sucesso;
9. cenários ideal, alternativo e limite;
10. contrato da capacidade.