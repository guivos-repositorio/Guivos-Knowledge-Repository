---
id: GKR-UX-PER011-MASTER-001
title: Jornada da Pessoa — PER-011 — Meus Próximos Passos — Documento Mestre de Superfície
status: active
version: 0.1.0
maturity: current_surface_design_definition
depends_on:
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C4B-001
  - PAS-001-PP-FOUNDATION-001
  - PAS-001-PP-LIFECYCLE-001
  - PAS-001-PP-VIEW-001
  - PAS-001-PP-EVENT-001
  - PAS-001-PP-INTEGRATION-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-PER008-MASTER-001
tags:
  - person-journey
  - per-011
  - next-steps
  - surface-master
---

# Jornada da Pessoa — PER-011 — Meus Próximos Passos — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-011 — Meus Próximos Passos` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

`Meus Próximos Passos` existe para permitir que a Pessoa **compreenda, organize, avalie e controle movimentos contextuais possíveis da própria jornada**, preservando autonomia sobre ritmo, prioridade e execução.

A superfície não é lista compulsória de tarefas, agenda de produtividade, mecanismo de cobrança, ranking de desempenho nem motor de urgência artificial.

## 2. Papel na Jornada

A continuidade governada é:

```text
PER-008 — HOJE
→ TRN-010 / INTEGRALMENTE VALIDADA
→ PER-011 — MEUS PRÓXIMOS PASSOS
→ TRN-011 / INTEGRALMENTE VALIDADA
→ PER-008 — HOJE
```

Abrir `PER-011` não aceita, inicia, executa, conclui ou prioriza um passo.

Retornar a `Hoje` não marca o passo como visto, aceito, iniciado, executado ou concluído. O retorno reconsulta o estado canônico vigente.

O modelo corrente não registra handoffs diretos:

```text
PER-011 ↔ PER-010
PER-011 ↔ PER-012
```

Relação semântica entre Próximos Passos, Objetivos e Evolução não cria navegação direta.

## 3. Trabalho da Pessoa

Conforme estado e autorização, a Pessoa precisa conseguir:

1. compreender quais movimentos existem e por que aparecem;
2. distinguir proposta, decisão confirmada, ação e resultado;
3. compreender estado, prontidão, prioridade, prazo, esforço e confiança sem confundi-los;
4. reconhecer dependências, bloqueios, condições e responsabilidades;
5. avaliar alternativas e passos condicionais;
6. confirmar conscientemente um passo pessoal quando fizer sentido;
7. rejeitar, adiar, pausar, reformular, substituir ou cancelar;
8. compreender recorrência, espera e temporalidade quando aplicáveis;
9. registrar ou revisar execução e resultado sem automatismos indevidos;
10. compreender evidências e origem das informações relevantes;
11. revisar histórico e mudanças sem score de produtividade;
12. controlar exposição de conteúdo sensível;
13. permanecer legitimamente sem Próximo Passo ativo.

## 4. Definição funcional

Próximo Passo é uma **decisão ou hipótese de movimento delimitada e contextual** capaz de aproximar a Pessoa de um objetivo, resultado, responsabilidade ou transição relevante.

```text
PRÓXIMO PASSO
≠ TAREFA
≠ AÇÃO EXECUTADA
≠ PLANO
≠ OPORTUNIDADE
≠ RECOMENDAÇÃO ACEITA
≠ OBRIGAÇÃO AUTOMÁTICA
```

Um passo pode representar ação, preparação, escolha, condição ou espera legítima.

“Próximo” não significa necessariamente o evento cronologicamente mais próximo. A Pessoa pode ter passos distintos para objetivos diferentes, alternativas, passos condicionais ou preparatórios — ou nenhum passo ativo.

## 5. Proposta, decisão e compromisso

Uma recomendação ou possibilidade permanece sugestão até avaliação.

```text
POSSIBILIDADE
→ PROPOSTA
→ DECISÃO CONSCIENTE
→ PASSO CONFIRMADO
```

A exibição, repetição, clique, navegação, comportamento anterior, oportunidade disponível ou inferência não confirmam um passo.

Um passo somente pode ser apresentado como compromisso quando existir aceitação suficiente da Pessoa ou autoridade legítima no respectivo contexto.

Passo institucional e passo pessoal devem preservar suas autoridades próprias. Autoridade institucional não define prioridade pessoal automaticamente.

## 6. Estados funcionais

A superfície pode representar, conforme o contrato funcional, estados como possibilidade/proposta, confirmado, ativo, pronto, agendado, em andamento, bloqueado, pausado, concluído, cancelado, substituído, expirado, contestado e arquivado.

Esses estados são estados funcionais dentro de `PER-011`.

```text
ESTADO INTERNO
≠ NOVA SUPERFÍCIE
≠ NOVO PER-ID
```

Estado funcional e estado da informação permanecem distinguíveis. Falta de atualização recente não significa automaticamente interrupção ou conclusão.

## 7. Prontidão, prioridade e urgência

Estado, prioridade, prontidão, urgência, prazo, esforço e confiança são dimensões distintas.

```text
PRONTO ≠ OBRIGATÓRIO
PRONTO ≠ PRIORIDADE MÁXIMA
PRIORIDADE ≠ URGÊNCIA
PRAZO ≠ PRESSÃO ARTIFICIAL
SUGESTÃO ≠ PRIORIDADE APLICADA
```

Receita, comissão, patrocínio, estoque ou interesse comercial não podem determinar ativação, prioridade ou conclusão.

A Pessoa preserva controle sobre prioridade pessoal.

## 8. Dependências, bloqueios e condições

Quando existirem, a superfície deve tornar compreensíveis:

- dependências relevantes;
- bloqueios reais;
- condições futuras;
- preparações necessárias;
- responsabilidade envolvida;
- impacto de mudanças no passo.

Bloqueio não é falha moral nem inatividade indevida.

Esperar pode ser um Próximo Passo legítimo quando a continuidade depende de condição externa, prazo, resposta, disponibilidade ou outro evento real.

## 9. Temporalidade e recorrência

Datas e janelas devem refletir evidência real e distinguir precisão de aproximação quando necessário.

Recorrência não pode ser criada apenas porque uma atividade se repetiu.

A superfície pode permitir adiar, reagendar, pausar ou retomar quando o contrato do passo permitir, sem transformar mudança de ritmo em julgamento sobre a Pessoa.

## 10. Evidência, execução e resultado

A atividade realizada não confirma automaticamente que o passo era adequado, foi concluído ou gerou progresso.

Evidências devem manter origem e natureza compreensíveis. Conflitos ou insuficiência de evidência não podem ser resolvidos por fabricação de certeza.

A conclusão de um Próximo Passo não conclui automaticamente um Objetivo.

Quantidade de passos concluídos, frequência de uso ou velocidade de execução não medem evolução humana.

## 11. Relação com oportunidades e outras capacidades

Uma oportunidade pode apoiar um Próximo Passo, mas sua disponibilidade não cria compromisso, prioridade ou passo confirmado.

Um Próximo Passo pode se relacionar semanticamente a Objetivos, Contexto Vivo, Eventos de Vida, oportunidades, experiências ou outras capacidades autorizadas.

Essas relações não permitem que `PER-011` absorva as responsabilidades das superfícies especializadas nem criam handoffs não registrados.

## 12. Ações conscientes

Conforme autoridade e estado, a Pessoa pode:

- avaliar uma proposta;
- confirmar ou rejeitar;
- adiar;
- ativar;
- alterar prioridade pessoal;
- indicar bloqueio;
- pausar ou retomar;
- reformular;
- substituir;
- cancelar;
- registrar execução;
- revisar resultado;
- contestar;
- concluir quando houver base legítima;
- revisar histórico.

Nenhuma ação destrutiva ou materialmente consequente deve ser inferida pela ausência de interação.

## 13. Ausência e estados vazios

É legítimo não existir Próximo Passo ativo.

A superfície não deve preencher vazio com tarefas artificiais, recomendações irrelevantes, oportunidades comerciais ou urgência fabricada.

Quando não houver movimento legítimo, a experiência pode explicar o estado e preservar continuidade neutra.

## 14. Falhas e recuperação

Falhas devem preservar o último estado válido e reduzir automação quando necessário.

A recuperação não pode:

- confirmar passo;
- alterar prioridade;
- marcar execução;
- concluir;
- cancelar;
- substituir;
- expandir autorização

sem evidência e ação legítimas.

Repetições técnicas devem ser idempotentes quando aplicável.

## 15. Privacidade, permissões e conteúdo sensível

A superfície deve usar apenas informação necessária, autorizada, proporcional e vigente.

Passos sensíveis exigem proteção compatível com seu conteúdo. A existência de um passo não autoriza compartilhamento com terceiros.

Permissões devem ser revalidadas quando a ação, destino ou contexto exigir.

## 16. Explicabilidade

Quando materialmente relevante, a Pessoa deve conseguir compreender:

- por que o passo aparece;
- origem da proposta;
- relação com objetivo, contexto ou responsabilidade;
- motivo de prontidão ou bloqueio;
- origem de prioridade sugerida;
- dependências;
- evidências usadas;
- consequências de confirmar, adiar, pausar, substituir, cancelar ou concluir.

Explicação não deve transformar inferência em certeza.

## 17. Linguagem

A linguagem deve preservar possibilidade, escolha e contexto.

Evitar formulações que impliquem:

- obrigação inexistente;
- culpa por atraso;
- mérito por produtividade;
- certeza sem evidência;
- urgência fabricada;
- recomendação como decisão tomada;
- conclusão automática.

## 18. Acessibilidade

A solução visual deve permitir compreensão dos estados e ações sem depender exclusivamente de cor, posição, animação ou ícone.

Controles materialmente diferentes precisam ser distinguíveis por significado. Mudanças de estado, erros, bloqueios e consequências devem ser perceptíveis por tecnologias assistivas quando aplicável.

## 19. Conteúdo sintético para exploração

Prototipação pode usar conteúdo sintético claramente fictício para testar:

- diferentes estados;
- ausência de passos;
- dependências e bloqueios;
- propostas e passos confirmados;
- passos condicionais ou em espera;
- recorrência;
- conflitos de evidência;
- recuperação de falhas.

Conteúdo sintético não pode ser apresentado como dado real, métrica validada ou comportamento já implementado.

## 20. Liberdade criativa de Design

Este Master governa significado, responsabilidade, limites e critérios funcionais — não estética.

Designer humana pode definir tipografia, cores, imagens, ilustrações, ícones, grid, composição, componentes, densidade, ritmo, motion, microinterações, hierarquia visual, responsividade e linguagem gráfica, desde que preserve o contrato funcional.

Não existe baseline visual obrigatório para `PER-011`.

## 21. Uso de IA

IA pode apoiar exploração e produção sob direção humana.

IA não pode:

- escolher o Próximo Passo pela Pessoa;
- converter proposta ou inferência em decisão confirmada;
- inventar urgência, prioridade, prazo, dependência, bloqueio, evidência ou resultado;
- marcar execução ou conclusão sem base;
- criar score humano de produtividade;
- expor passo sensível indevidamente;
- criar novo `PER-ID` para estado interno;
- criar handoff direto para `PER-010` ou `PER-012`;
- alterar `TRN-010/011`;
- iniciar Product Engineering.

## 22. Critérios funcionais de aceitação

Uma futura solução visual é funcionalmente aceitável quando:

1. preserva `TRN-010/011`;
2. não cria handoffs diretos para `PER-010/012`;
3. distingue proposta de decisão;
4. distingue passo de tarefa, oportunidade e obrigação;
5. distingue estado, prontidão, prioridade, urgência e prazo;
6. permite compreender dependências e bloqueios;
7. preserva rejeição, adiamento, pausa, reformulação, substituição e cancelamento quando aplicáveis;
8. aceita ausência legítima de passo ativo;
9. não converte atividade em conclusão automática;
10. não converte conclusão do passo em conclusão de objetivo;
11. não mede evolução humana por produtividade;
12. preserva privacidade e autoridade;
13. explica recomendações e estados quando materialmente relevante;
14. não inventa dados ou efeitos;
15. mantém estados internos dentro de `PER-011`;
16. preserva liberdade criativa de Design;
17. mantém IA subordinada às autoridades;
18. não libera implementação.

## 23. Limites e lacunas

Este Master não define:

- layout, wireframe, UI ou sistema visual;
- arquitetura técnica;
- mecanismo de recomendação;
- política jurídica final de retenção;
- integração técnica com terceiros;
- handoffs diretos com `PER-010/012`;
- novas superfícies;
- implementação.

Lacunas futuras devem permanecer explícitas e não podem ser completadas por inferência.

## 24. Estado governado

```text
PER-011 MASTER
→ GKR-UX-PER011-MASTER-001 v0.1.0
→ CURRENT SURFACE DESIGN DEFINITION

TRN-010
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-011
→ INTEGRALLY VALIDATED / UNCHANGED

DIRECT HANDOFFS TO PER-010 / PER-012
→ NOT CONTRACTED

PRODUCT ENGINEERING
→ NOT RELEASED

NEXT DOCUMENTATION TARGET
→ PER-012 — MINHA EVOLUÇÃO
```
