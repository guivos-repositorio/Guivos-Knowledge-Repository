---
id: PAS-001-IC-LIFECYCLE-001
title: Regras do Ciclo de Vida das Intervenções Contextuais
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-15
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-IC-FOUNDATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-IC-LIFECYCLE-001 — Regras do Ciclo de Vida das Intervenções Contextuais

## 1. Autoridade e vínculo

Este documento é a **segunda extensão normativa da Capacidade 07 — Intervenções Contextuais** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser interpretado como continuidade do `PAS-001-IC-FOUNDATION-001 1.0.0`, do `PAS-001 0.5.0`, das seções 1 a 2837, dos contratos finais das Capacidades 02 a 06, da `GLPA-001` e da `GIA-000`.

Esta extensão mantém a Capacidade 07 como `In progress` e eleva o progresso editorial de referência de `20%` para `40%`.

As Capacidades 02, 03, 04, 05 e 06 permanecem `Functionally complete`. A Capacidade 08 — Experiências permanece `Planned`.

# 2838. Finalidade do ciclo de vida

O ciclo de vida deverá governar como uma possível manifestação da Guivos é:

- identificada;
- avaliada;
- admitida;
- programada;
- apresentada;
- respondida;
- adiada;
- silenciada;
- cancelada;
- contestada;
- corrigida;
- encerrada.

O ciclo deverá impedir que um sinal, gatilho técnico ou interesse comercial produza manifestação automática sem avaliação contextual.

# 2839. Fluxo funcional geral

```text
sinal, fato, mudança ou solicitação
→ identificação
→ candidatura
→ avaliação
→ admissão ou rejeição
→ seleção do comportamento
→ programação, espera ou silêncio
→ verificação de prontidão
→ entrega ou execução autorizada
→ resposta, adiamento, recusa ou ausência de resposta
→ reavaliação
→ encerramento, expiração, cancelamento ou nova manifestação
```

# 2840. Dimensões independentes

O ciclo deverá manter separadas:

1. estado funcional da intervenção;
2. estado da informação;
3. estado de autorização;
4. estado temporal;
5. estado de entrega;
6. estado da relação do participante;
7. estado de atenção;
8. estado de fadiga;
9. estado de sensibilidade;
10. situação da operação externa.

Nenhuma dimensão deverá substituir automaticamente outra.

# 2841. Estado funcional principal

Estados possíveis:

| Estado | Significado |
|---|---|
| Identificada | Existe uma possível razão para manifestação |
| Candidata | A possibilidade possui elementos mínimos para avaliação |
| Em avaliação | Relevância, momento, atenção, risco e finalidade estão sendo avaliados |
| Admitida | A manifestação atingiu o limiar funcional |
| Programada | Existe uma janela futura definida |
| Aguardando | Depende de condição, momento ou informação |
| Pronta | Pode seguir para entrega |
| Em entrega | Está sendo transmitida ou executada |
| Entregue | A entrega técnica foi confirmada |
| Respondida | Houve resposta funcional do participante |
| Adiada | O participante ou o sistema definiu retomada posterior |
| Silenciada | A decisão atual é não se manifestar |
| Cancelada | A manifestação foi interrompida explicitamente |
| Expirada | A janela ou validade terminou |
| Contestada | O fundamento ou efeito foi questionado |
| Corrigida | Uma correção funcional foi reconhecida |
| Falha | O processamento ou a entrega não foi concluído adequadamente |
| Encerrada | O ciclo atual terminou |

# 2842. Estado da informação

A informação poderá estar:

- completa;
- parcialmente completa;
- insuficiente;
- estimada;
- divergente;
- desatualizada;
- contestada;
- corrigida;
- indisponível.

Informação incompleta não deverá ser apresentada como certeza.

# 2843. Estado de entrega

A entrega poderá estar:

- não iniciada;
- preparada;
- enviada;
- parcialmente entregue;
- entregue;
- confirmada;
- falha;
- pendente;
- bloqueada;
- cancelada.

Entrega técnica não representa compreensão, interesse ou concordância.

# 2844. Relação do participante

A relação individual poderá estar:

- não apresentada;
- apresentada;
- visualizada;
- respondida;
- aceita;
- recusada;
- adiada;
- ignorada;
- ocultada;
- bloqueada;
- contestada;
- encerrada.

Visualização não representa aceitação.

Ausência de resposta não representa recusa.

# 2845. Estado temporal

A intervenção poderá estar:

- imediata;
- aplicável agora;
- programável;
- futura;
- dependente de condição;
- atrasada;
- próxima do prazo;
- expirada;
- sem prazo;
- com temporalidade incerta.

# 2846. Estado de fadiga

A fadiga poderá ser:

- desconhecida;
- baixa;
- moderada;
- elevada;
- crítica;
- protegida por silêncio.

Fadiga elevada deverá reduzir manifestação, não aumentar pressão.

# 2847. Estado de sensibilidade

A sensibilidade poderá ser:

- comum;
- pessoal;
- confidencial;
- sensível;
- altamente sensível;
- protegida.

A classificação deverá governar conteúdo, canal, título, prévia, autenticação, retenção e compartilhamento.

# 2848. Estado de autorização

A autorização poderá ser:

- não aplicável;
- não avaliada;
- existente;
- condicionada;
- limitada;
- pendente;
- revogada;
- expirada;
- rejeitada.

Disponibilidade técnica não substitui autorização.

# 2849. Transições fundamentais

Transições válidas deverão incluir:

```text
Identificada → Candidata
Candidata → Em avaliação
Em avaliação → Admitida
Em avaliação → Rejeitada
Em avaliação → Aguardando
Admitida → Programada
Admitida → Pronta
Admitida → Silenciada
Programada → Pronta
Programada → Aguardando
Pronta → Em entrega
Em entrega → Entregue
Entregue → Respondida
Entregue → Adiada
Entregue → Encerrada
Qualquer estado material → Contestada
Contestada → Corrigida
Corrigida → Em avaliação
```

# 2850. Transições proibidas

Não deverão ocorrer:

- sinal diretamente para entrega;
- candidatura diretamente para ação material;
- intervenção rejeitada diretamente para pronta;
- intervenção silenciada diretamente para entrega sem nova avaliação;
- intervenção expirada diretamente para apresentação;
- intervenção cancelada diretamente para entrega;
- entrega falha apresentada como entregue;
- visualização convertida em resposta positiva;
- ausência de resposta convertida em recusa;
- adiamento convertido em cancelamento;
- atenção convertida em consentimento;
- urgência comercial convertida em urgência funcional.

# 2851. Identificação

A identificação deverá registrar:

- origem;
- finalidade preliminar;
- participante ou público;
- fato, sinal ou solicitação;
- temporalidade;
- possível comportamento;
- sensibilidade preliminar;
- autoridade conhecida;
- relação comercial conhecida.

Identificação não representa admissão.

# 2852. Identificação por solicitação

Uma solicitação direta do participante poderá originar intervenção candidata.

A solicitação deverá ser interpretada conforme:

- conteúdo;
- finalidade;
- escopo;
- canal;
- temporalidade;
- autorização;
- ambiguidades.

Solicitação não deverá ser ampliada além do necessário.

# 2853. Identificação por sinal

Um sinal poderá iniciar avaliação quando possuir relação plausível com:

- contexto;
- objetivo;
- Evento de Vida;
- Próximo Passo;
- Oportunidade Ativa;
- risco;
- prazo;
- falha;
- processo externo.

Sinal não representa confirmação.

# 2854. Identificação por mudança contextual

Uma mudança no Contexto Vivo poderá originar candidatura quando alterar materialmente:

- relevância;
- momento;
- capacidade;
- restrição;
- disponibilidade;
- risco;
- necessidade de confirmação.

# 2855. Identificação por prazo

Prazos somente poderão originar intervenção quando forem:

- reais;
- verificáveis;
- relevantes;
- atuais;
- vinculados a finalidade legítima.

Prazo promocional não deverá produzir urgência funcional automaticamente.

# 2856. Identificação por risco

Riscos poderão originar intervenção quando houver:

- evidência suficiente;
- autoridade da fonte;
- impacto material;
- temporalidade aplicável;
- comportamento proporcional possível.

# 2857. Identificação por sistema externo

Sistemas externos poderão originar sinais ou fatos sobre:

- disponibilidade;
- inscrição;
- pagamento;
- reserva;
- entrega;
- atendimento;
- falha;
- alteração material.

O sistema externo não deverá decidir sozinho pela manifestação.

# 2858. Deduplicação inicial

Antes da criação de nova candidatura, deverão ser avaliados:

- finalidade;
- participante;
- assunto;
- origem;
- janela;
- comportamento;
- conteúdo;
- processo relacionado.

Intervenções equivalentes deverão ser unificadas ou agrupadas.

# 2859. Candidatura

A candidatura deverá possuir elementos suficientes para avaliação:

- identidade;
- finalidade;
- origem;
- autoridade preliminar;
- contexto mínimo;
- temporalidade;
- sensibilidade;
- comportamento possível;
- benefício esperado;
- custo provável de interrupção.

# 2860. Rejeição preliminar

A candidatura poderá ser rejeitada antes da avaliação completa quando houver:

- finalidade ilegítima;
- fonte sem autoridade;
- publicidade disfarçada;
- ausência de vínculo contextual;
- repetição abusiva;
- autorização revogada;
- exploração de vulnerabilidade;
- conteúdo proibido;
- janela expirada.

# 2861. Início da avaliação

A avaliação deverá registrar:

- critérios utilizados;
- informações consideradas;
- informações excluídas;
- limitações;
- autoridade;
- finalidade;
- validade;
- responsáveis pela decisão.

# 2862. Avaliação de finalidade

A finalidade deverá ser:

- específica;
- legítima;
- compreensível;
- proporcional;
- compatível com a autorização;
- distinta de maximização de engajamento ou conversão.

# 2863. Avaliação de autoridade

Deverá ser validado:

- quem originou a solicitação;
- quem pode confirmar o fato;
- quem pode decidir pela manifestação;
- quem pode executar uma ação;
- quem pode receber a resposta.

# 2864. Avaliação de relevância

A relevância deverá considerar:

- relação com o contexto;
- utilidade;
- impacto;
- necessidade de decisão;
- alternativas;
- custo de interrupção;
- possibilidade de silêncio.

Receita, comissão e patrocínio não deverão elevar relevância.

# 2865. Avaliação temporal

Deverão ser considerados:

- momento do fato;
- momento do conhecimento;
- validade;
- janela de decisão;
- prazo real;
- possibilidade de espera;
- horário local;
- recorrência.

# 2866. Avaliação de atenção

A atenção deverá ser tratada como estimativa limitada.

A capacidade deverá evitar conclusões sobre atenção baseadas apenas em:

- aplicativo aberto;
- tela ativa;
- clique;
- localização;
- dispositivo conectado;
- tempo de uso.

# 2867. Avaliação de interruptibilidade

A interruptibilidade deverá considerar:

- atividade atual;
- horário;
- ambiente;
- canal;
- urgência;
- sensibilidade;
- preferência;
- necessidade de resposta;
- possibilidade de adiamento.

# 2868. Avaliação de urgência

A urgência deverá decorrer de:

- risco material;
- prazo real;
- perda objetiva de opção;
- obrigação externa;
- necessidade declarada;
- condição irreversível.

# 2869. Avaliação de importância

A importância deverá considerar magnitude e relação com a jornada.

Importância elevada não deverá exigir interrupção imediata quando o momento for inadequado.

# 2870. Avaliação de sensibilidade

A avaliação deverá classificar:

- conteúdo;
- origem;
- contexto utilizado;
- impacto da exposição;
- terceiros relacionados;
- necessidade de título neutro;
- canal seguro;
- retenção.

# 2871. Avaliação de fadiga

A fadiga deverá considerar:

- intervenções recentes;
- repetições;
- respostas;
- adiamentos;
- recusas;
- canais;
- intensidade;
- temas;
- sensibilidade.

# 2872. Avaliação de frequência

A frequência deverá ser avaliada:

- globalmente;
- por categoria;
- por finalidade;
- por canal;
- por fonte;
- por organização;
- por produto;
- por período.

# 2873. Avaliação de canal

O canal deverá ser selecionado conforme:

- urgência;
- sensibilidade;
- extensão;
- necessidade de resposta;
- acessibilidade;
- preferência;
- disponibilidade técnica;
- segurança.

# 2874. Avaliação de reversibilidade

A reversibilidade deverá considerar:

- possibilidade de desfazer;
- custo de correção;
- impacto externo;
- exposição de dados;
- efeitos financeiros;
- efeitos institucionais;
- consequências para terceiros.

# 2875. Avaliação de risco

Riscos possíveis incluem:

- físico;
- financeiro;
- jurídico;
- emocional;
- reputacional;
- de privacidade;
- discriminação;
- fraude;
- manipulação;
- exposição de terceiro.

# 2876. Avaliação de alternativas

Antes de uma intervenção material, deverão ser consideradas alternativas como:

- silêncio;
- espera;
- pergunta;
- mensagem passiva;
- agrupamento;
- canal menos intrusivo;
- encaminhamento humano;
- confirmação adicional.

# 2877. Custo de interrupção

O custo de interrupção deverá considerar:

- quebra de foco;
- carga cognitiva;
- ansiedade;
- exposição;
- tempo necessário;
- necessidade de decisão;
- possibilidade de reagendamento.

# 2878. Informação insuficiente

Quando a informação for insuficiente, a capacidade poderá:

- aguardar;
- solicitar confirmação;
- buscar fonte autorizada;
- limitar a manifestação;
- silenciar;
- rejeitar a candidatura.

Não deverá fabricar precisão.

# 2879. Solicitação de informação

A solicitação deverá:

- explicar a finalidade;
- pedir somente o necessário;
- permitir recusa;
- permitir resposta posterior;
- indicar efeitos da ausência;
- evitar pressão.

# 2880. Conclusão da avaliação

A avaliação deverá resultar em:

- admitida;
- admitida com condição;
- aguardando;
- silenciada;
- rejeitada;
- cancelada;
- exige avaliação humana.

# 2881. Admissão

A admissão deverá exigir:

- finalidade legítima;
- autoridade suficiente;
- relevância proporcional;
- temporalidade aplicável;
- risco compatível;
- sensibilidade protegida;
- frequência aceitável;
- canal possível;
- benefício superior ao custo provável da interrupção.

# 2882. Admissão condicionada

A admissão poderá depender de:

- nova confirmação;
- horário;
- redução de fadiga;
- informação externa;
- disponibilidade do canal;
- resolução de conflito;
- autorização adicional.

# 2883. Rejeição após avaliação

A rejeição deverá registrar:

- fundamento;
- critérios;
- autoridade;
- efeitos;
- possibilidade de revisão;
- prazo de retenção;
- relação comercial relevante.

# 2884. Seleção de comportamento

Após admissão, deverá ser selecionado exatamente um comportamento principal:

- agir;
- perguntar;
- informar;
- sugerir;
- lembrar;
- alertar;
- confirmar;
- aguardar;
- observar;
- silenciar.

Comportamentos auxiliares poderão ser associados sem ocultar a decisão principal.

# 2885. Agir

`Agir` deverá exigir:

- autorização vigente;
- escopo delimitado;
- executor responsável;
- impacto conhecido;
- reversibilidade suficiente;
- ausência de necessidade de nova confirmação.

# 2886. Perguntar

`Perguntar` deverá ser utilizado quando o participante precisar completar informação ou decidir.

A pergunta não deverá ser formulada como obrigação.

# 2887. Informar

`Informar` deverá apresentar:

- fato;
- fonte;
- validade;
- limitações;
- impacto;
- ações possíveis.

# 2888. Sugerir

`Sugerir` deverá apresentar possibilidade e alternativas.

A sugestão não deverá criar prioridade ou compromisso.

# 2889. Lembrar

`Lembrar` deverá recuperar algo previamente reconhecido.

Não deverá criar um novo compromisso.

# 2890. Alertar

`Alertar` deverá possuir fundamento material e proporcionalidade.

Alertas não deverão ser utilizados para promoção.

# 2891. Confirmar

`Confirmar` deverá anteceder efeitos materiais, sensíveis, financeiros, externos ou difíceis de reverter.

# 2892. Aguardar

`Aguardar` deverá possuir:

- motivo;
- condição;
- horizonte;
- gatilho de revisão;
- validade;
- limite de espera.

# 2893. Observar

`Observar` deverá possuir finalidade e prazo.

Não deverá constituir vigilância contínua.

# 2894. Silenciar

`Silenciar` deverá registrar:

- motivo;
- escopo;
- duração;
- condições de reavaliação;
- efeitos sobre repetições.

# 2895. Programação

Uma intervenção programada deverá possuir:

- data, período ou condição;
- fuso horário;
- validade;
- canal;
- comportamento;
- prioridade funcional;
- condição de cancelamento;
- regra de reavaliação.

# 2896. Reprogramação

A reprogramação deverá ocorrer quando houver:

- solicitação do participante;
- mudança de contexto;
- fadiga;
- conflito de agenda;
- alteração de prazo;
- indisponibilidade de canal;
- nova informação.

# 2897. Janela de entrega

A janela deverá considerar:

- início;
- término;
- flexibilidade;
- horário protegido;
- urgência;
- expiração;
- possibilidade de agrupamento.

# 2898. Prontidão

Uma intervenção estará pronta quando:

- condições de admissão permanecerem válidas;
- canal estiver disponível;
- autorização estiver vigente;
- conteúdo estiver preparado;
- horário for adequado;
- não houver bloqueio;
- fadiga estiver aceitável.

# 2899. Bloqueio antes da entrega

A entrega deverá ser bloqueada diante de:

- revogação;
- expiração;
- mudança material não avaliada;
- conflito;
- fadiga crítica;
- canal inseguro;
- informação desatualizada;
- ausência de autorização;
- horário protegido.

# 2900. Espera

A espera deverá preservar a candidatura sem apresentá-la como intervenção ativa ao participante.

# 2901. Condição de retomada

A retomada poderá depender de:

- horário;
- data;
- resposta;
- mudança de estado;
- proximidade de prazo;
- resolução de conflito;
- nova autorização;
- atualização de fonte.

# 2902. Entrega

A entrega deverá registrar:

- conteúdo;
- canal;
- momento;
- versão;
- finalidade;
- sensibilidade;
- justificativa;
- relação comercial;
- controles disponíveis.

# 2903. Entrega parcial

Entrega parcial deverá identificar:

- partes transmitidas;
- partes pendentes;
- impacto;
- possibilidade de repetição;
- risco de duplicidade;
- necessidade de correção.

# 2904. Confirmação de entrega

Confirmação técnica não deverá representar:

- leitura;
- compreensão;
- concordância;
- interesse;
- consentimento;
- execução.

# 2905. Falha de entrega

A falha deverá registrar:

- canal;
- etapa;
- causa;
- efeitos aplicados;
- efeitos não aplicados;
- possibilidade de repetição;
- alternativa segura.

# 2906. Apresentação

Apresentação representa disponibilização funcional ao participante.

Não representa visualização ou resposta.

# 2907. Relação com execução externa

Quando a intervenção solicitar ação em outro produto ou sistema:

- o executor deverá permanecer identificado;
- a ação deverá possuir contrato próprio;
- os efeitos externos deverão retornar como fatos;
- a intervenção não deverá presumir conclusão.

# 2908. Resposta

A resposta deverá ser reconhecida somente quando houver manifestação ou fato suficiente.

# 2909. Tipos de resposta

Respostas poderão representar:

- aceitação;
- recusa;
- adiamento;
- solicitação de detalhes;
- contestação;
- ocultação;
- bloqueio;
- ação externa;
- ausência de compreensão;
- confirmação parcial.

# 2910. Ausência de resposta

Ausência de resposta poderá resultar em:

- encerramento;
- espera;
- repetição limitada;
- agrupamento;
- canal alternativo;
- silêncio.

Não deverá produzir julgamento pessoal.

# 2911. Adiamento

O adiamento deverá registrar:

- origem;
- motivo opcional;
- momento de retomada;
- canal;
- escopo;
- limite de repetições.

# 2912. Recusa

A recusa deverá interromper o fluxo atual e limitar futuras reapresentações equivalentes.

Não deverá gerar penalidade.

# 2913. Ocultação

A ocultação poderá abranger:

- ocorrência;
- tema;
- categoria;
- fonte;
- organização;
- produto;
- campanha;
- tipo de intervenção.

# 2914. Bloqueio

O bloqueio deverá impedir novas intervenções dentro do escopo definido até revisão explícita.

# 2915. Silêncio pós-avaliação

A capacidade poderá concluir que a manifestação não produziria utilidade suficiente.

Esse silêncio deverá permanecer auditável sem produzir exposição ao participante.

# 2916. Silêncio solicitado

O silêncio solicitado deverá prevalecer, salvo obrigação legítima ou risco crítico claramente definido.

# 2917. Silêncio por fadiga

Fadiga elevada deverá permitir:

- supressão;
- adiamento;
- agrupamento;
- redução de intensidade;
- canal passivo.

# 2918. Silêncio por sensibilidade

O silêncio poderá ser preferível quando não existir canal suficientemente protegido.

# 2919. Cancelamento

O cancelamento deverá ocorrer quando a manifestação deixar de ser necessária ou legítima antes da conclusão do ciclo.

# 2920. Expiração

A intervenção deverá expirar quando:

- prazo terminar;
- informação perder validade;
- contexto mudar;
- oportunidade desaparecer;
- autorização expirar;
- objetivo da manifestação deixar de existir.

# 2921. Encerramento

O encerramento deverá representar término regular do ciclo atual.

Ele não deverá impedir nova candidatura diante de mudança material.

# 2922. Contestação

O participante ou agente autorizado poderá contestar:

- fundamento;
- relevância;
- temporalidade;
- urgência;
- fonte;
- conteúdo;
- relação comercial;
- frequência;
- uso de contexto;
- efeito produzido.

# 2923. Efeitos da contestação

A contestação material poderá:

- suspender repetições;
- limitar automações;
- bloquear execução;
- reduzir confiança;
- exigir avaliação humana;
- notificar consumidores;
- preservar evidências.

# 2924. Correção

A correção deverá:

- preservar o estado anterior;
- identificar o erro;
- registrar fonte e autoridade;
- aplicar evento compensatório;
- recompor efeitos;
- informar consumidores;
- permitir nova avaliação.

# 2925. Reabertura

Uma intervenção encerrada poderá ser reaberta quando:

- a finalidade permanecer a mesma;
- houver informação nova;
- o contexto mudar;
- a janela retornar;
- a contestação for resolvida.

# 2926. Nova intervenção ou reabertura

Mudança material de finalidade, conteúdo, comportamento, destinatário ou impacto deverá criar nova intervenção, não reutilizar silenciosamente o ciclo anterior.

# 2927. Escalonamento

O escalonamento poderá alterar:

- intensidade;
- canal;
- frequência;
- necessidade de confirmação;
- encaminhamento humano;
- autoridade necessária.

# 2928. Desescalonamento

Deverá ocorrer quando:

- risco diminuir;
- participante responder;
- condição for resolvida;
- prazo se afastar;
- fadiga aumentar;
- informação perder confiança;
- participante solicitar.

# 2929. Encaminhamento humano

O encaminhamento deverá ser considerado quando houver:

- risco elevado;
- ambiguidade material;
- sensibilidade crítica;
- conflito persistente;
- impacto irreversível;
- exigência profissional;
- contestação complexa.

# 2930. Repetição

A repetição somente deverá ocorrer diante de:

- mudança material;
- aproximação legítima de prazo;
- solicitação;
- regra previamente autorizada;
- falha confirmada de entrega;
- condição recorrente.

# 2931. Recorrência

Intervenções recorrentes deverão possuir:

- finalidade;
- frequência;
- limite;
- janela;
- expiração;
- revisão;
- controle do participante.

Recorrência não representa hábito ou necessidade permanente.

# 2932. Agrupamento

Intervenções relacionadas poderão ser agrupadas para reduzir fadiga.

O agrupamento não deverá ocultar urgências, sensibilidades ou relações comerciais distintas.

# 2933. Supressão de duplicidade

Intervenções semanticamente equivalentes deverão ser suprimidas mesmo quando originadas por fontes ou identificadores diferentes.

# 2934. Controle de frequência global

A capacidade deverá limitar o conjunto total de manifestações em determinado período.

# 2935. Controle por categoria

Categorias sensíveis ou repetitivas poderão possuir limites específicos.

# 2936. Controle por canal

Cada canal deverá possuir regras próprias de:

- frequência;
- horário;
- extensão;
- intensidade;
- sensibilidade;
- repetição.

# 2937. Horários protegidos

Horários protegidos deverão bloquear manifestações não críticas.

Exceções deverão ser explícitas e justificáveis.

# 2938. Mudança material

Mudanças em risco, prazo, custo, disponibilidade, autorização, sensibilidade ou contexto deverão causar reavaliação antes da entrega.

# 2939. Intervenções sensíveis

Intervenções sensíveis deverão utilizar:

- minimização;
- título neutro;
- prévia protegida;
- canal seguro;
- autenticação proporcional;
- retenção limitada;
- ausência de publicidade derivada.

# 2940. Saúde

Intervenções de saúde deverão evitar diagnóstico, prescrição automática e promessa de resultado.

# 2941. Finanças

Intervenções financeiras deverão tornar visíveis custos, riscos, autoridade e ausência de garantia.

# 2942. Jurídico

Intervenções jurídicas deverão distinguir informação geral de orientação profissional.

# 2943. Religião e espiritualidade

Intervenções religiosas deverão preservar liberdade, privacidade, pluralidade e ausência de julgamento.

# 2944. Social e voluntariado

Intervenções sociais não deverão utilizar culpa, ranking moral ou pressão baseada em recompensa.

# 2945. Institucional

Comunicações institucionais deverão distinguir obrigação, informação, benefício, convite e oportunidade.

# 2946. Comercial

Intervenções comerciais deverão permanecer identificadas e separadas das funcionais.

# 2947. Coletiva

Intervenções coletivas deverão preservar relações e decisões individuais.

# 2948. Terceiros

Informações sobre terceiros deverão ser minimizadas e não poderão formar perfis independentes.

# 2949. Compartilhamento

O compartilhamento deverá exigir:

- finalidade;
- destinatário;
- campos;
- validade;
- autoridade;
- sensibilidade;
- possibilidade de revogação.

# 2950. Revogação

A revogação deverá interromper:

- novas avaliações;
- novas entregas;
- novas repetições;
- novos compartilhamentos;
- novas execuções dependentes.

# 2951. Propagação

A revogação somente deverá ser concluída após confirmação suficiente dos consumidores e canais afetados.

# 2952. Reprocessamento

O reprocessamento não deverá duplicar:

- candidatura;
- admissão;
- programação;
- entrega;
- alerta;
- lembrete;
- execução;
- resposta;
- contestação;
- revogação.

# 2953. Retroatividade

Eventos retroativos deverão distinguir:

- momento do fato;
- momento do conhecimento;
- momento da avaliação;
- momento da aplicação;
- efeitos reversíveis;
- efeitos já produzidos.

# 2954. Idempotência

Toda operação material deverá possuir chave de idempotência.

# 2955. Ordenação

A ordenação deverá considerar:

- versão;
- causalidade;
- temporalidade;
- dependências;
- estado atual;
- revogações;
- correções.

# 2956. Concorrência

Alterações concorrentes deverão exigir versão esperada e reconciliação sem sobrescrita silenciosa.

# 2957. Estados impossíveis

Não poderão ocorrer:

- entrega após revogação efetiva;
- apresentação após expiração;
- repetição após bloqueio;
- alerta crítico após desescalonamento sem nova avaliação;
- ação material antes de autorização;
- correção antes do fato corrigido;
- resposta anterior à apresentação;
- confirmação de entrega após falha não recuperada.

# 2958. Falha segura

Em falha, a capacidade deverá:

- preservar o último estado válido;
- impedir falsa entrega;
- bloquear efeitos críticos;
- evitar duplicidade;
- reduzir automação;
- permitir recuperação;
- registrar impacto.

# 2959. Falha parcial

Falha parcial deverá permanecer explícita.

Nenhum fluxo parcialmente concluído deverá ser apresentado como sucesso integral.

# 2960. Reconstrução

O estado deverá ser reconstruível por:

- eventos válidos;
- versões;
- decisões;
- correções;
- contestações;
- permissões;
- revogações;
- confirmações de entrega;
- respostas;
- falhas.

# 2961. Eventos funcionais do ciclo

Deverão ser previstos, entre outros:

- `OportunidadeDeIntervencaoIdentificada`;
- `CandidaturaDeIntervencaoCriada`;
- `CandidaturaDeIntervencaoRejeitada`;
- `AvaliacaoDeIntervencaoIniciada`;
- `FinalidadeDeIntervencaoValidada`;
- `AutoridadeDeIntervencaoValidada`;
- `RelevanciaDeIntervencaoAvaliada`;
- `TemporalidadeDeIntervencaoAvaliada`;
- `AtencaoDoParticipanteAvaliada`;
- `InterruptibilidadeAvaliada`;
- `UrgenciaDeIntervencaoAvaliada`;
- `SensibilidadeDeIntervencaoClassificada`;
- `FadigaDeIntervencaoAvaliada`;
- `IntervencaoAdmitida`;
- `IntervencaoAdmitidaComCondicao`;
- `IntervencaoRejeitada`;
- `ComportamentoDeIntervencaoSelecionado`;
- `IntervencaoProgramada`;
- `IntervencaoReprogramada`;
- `IntervencaoAguardando`;
- `IntervencaoPronta`;
- `IntervencaoApresentada`;
- `IntervencaoEntregue`;
- `EntregaDeIntervencaoFalhou`;
- `IntervencaoRespondida`;
- `IntervencaoAdiada`;
- `IntervencaoRecusada`;
- `IntervencaoSilenciada`;
- `IntervencaoCancelada`;
- `IntervencaoExpirada`;
- `IntervencaoContestada`;
- `IntervencaoCorrigida`;
- `IntervencaoEscalonada`;
- `IntervencaoDesescalonada`;
- `RevogacaoDeIntervencaoEmPropagacao`;
- `RevogacaoDeIntervencaoPropagada`;
- `EstadoDeIntervencaoReconstruido`.

# 2962. Responsabilidades do ciclo

O ciclo será responsável por:

1. identificar candidaturas;
2. validar finalidade;
3. validar autoridade;
4. controlar deduplicação;
5. avaliar relevância;
6. avaliar temporalidade;
7. avaliar atenção;
8. avaliar interruptibilidade;
9. separar importância e urgência;
10. classificar sensibilidade;
11. avaliar fadiga;
12. controlar frequência;
13. avaliar canal;
14. avaliar reversibilidade;
15. avaliar risco;
16. considerar alternativas;
17. admitir ou rejeitar;
18. selecionar comportamento;
19. programar;
20. aguardar;
21. silenciar;
22. preparar entrega;
23. registrar entrega;
24. tratar resposta;
25. tratar adiamento;
26. tratar recusa;
27. tratar contestação;
28. aplicar correção;
29. propagar revogações;
30. operar com falha segura.

# 2963. Limites do ciclo

O ciclo não será responsável por:

1. definir Objetivos;
2. confirmar Próximos Passos;
3. ativar Oportunidades;
4. governar transações;
5. executar serviços especializados;
6. diagnosticar;
7. prescrever;
8. decidir juridicamente;
9. impor orientação espiritual;
10. confirmar experiência;
11. medir evolução;
12. fabricar atenção;
13. presumir consentimento;
14. presumir intenção;
15. criar urgência comercial;
16. atribuir prioridade pessoal;
17. acessar a jornada integral;
18. vigiar continuamente;
19. utilizar vulnerabilidade comercialmente;
20. reescrever histórico;
21. ignorar recusa;
22. transformar silêncio em falha;
23. transformar adiamento em rejeição;
24. transformar visualização em interesse;
25. transformar entrega em compreensão;
26. transformar resposta em progresso;
27. substituir decisão do participante;
28. substituir autoridade profissional;
29. ocultar relações comerciais;
30. maximizar tempo de tela ou volume de notificações.

# 2964. Critérios de aceite

A extensão será considerada consolidada quando:

1. definir dimensões independentes;
2. definir estados funcionais;
3. definir transições válidas;
4. proibir transições impossíveis;
5. governar identificação;
6. governar candidatura;
7. governar rejeição preliminar;
8. governar avaliação;
9. governar finalidade;
10. governar autoridade;
11. governar relevância;
12. governar temporalidade;
13. governar atenção;
14. governar interruptibilidade;
15. governar urgência e importância;
16. governar sensibilidade;
17. governar fadiga;
18. governar frequência;
19. governar canal;
20. governar risco;
21. governar admissão;
22. governar comportamentos;
23. governar programação;
24. governar entrega;
25. governar resposta;
26. governar adiamento e silêncio;
27. governar cancelamento e expiração;
28. governar contestação e correção;
29. governar revogação, idempotência e ordenação;
30. preservar falha segura e controle do participante.

# 2965. Regras fundamentais

1. Sinal não representa necessidade confirmada.
2. Identificação não representa candidatura.
3. Candidatura não representa admissão.
4. Admissão não representa apresentação.
5. Programação não representa entrega.
6. Entrega não representa visualização.
7. Visualização não representa compreensão.
8. Compreensão não representa concordância.
9. Resposta não representa progresso.
10. Atenção não representa consentimento.
11. Disponibilidade técnica não representa interruptibilidade.
12. Importância não representa urgência.
13. Urgência comercial não representa urgência funcional.
14. Silêncio é decisão legítima.
15. Espera é decisão legítima.
16. Adiamento não representa recusa.
17. Recusa não representa fracasso.
18. Ausência de resposta não representa desinteresse definitivo.
19. Repetição exige fundamento novo ou regra autorizada.
20. Fadiga reduz frequência e intensidade.
21. Fadiga não autoriza aumento de pressão.
22. Horários protegidos prevalecem sobre manifestações não críticas.
23. Conteúdo sensível exige minimização e canal protegido.
24. Publicidade permanece separada de intervenção funcional.
25. Comissão não altera relevância.
26. Patrocínio não aumenta prioridade.
27. Escassez comercial não fabrica urgência.
28. Produtos especializados executam suas próprias operações.
29. Intervenções decide o momento da manifestação, não o objetivo do participante.
30. Guivos Intelligence pode sugerir e explicar, mas não impor manifestação.
31. Platform Layer entrega mensagens, mas não define relevância humana.
32. Ação material exige autoridade e autorização.
33. Correção não reescreve histórico.
34. Contestação limita efeitos materiais.
35. Revogação interrompe novos usos.
36. Revogação somente termina após propagação suficiente.
37. Reprocessamento não duplica efeitos.
38. Eventos fora de ordem não criam estados impossíveis.
39. Conflitos não são sobrescritos silenciosamente.
40. Falha preserva o último estado válido.
41. Falha parcial não representa sucesso integral.
42. Terceiros não formam perfis paralelos.
43. Métricas futuras deverão avaliar o sistema.
44. O ciclo deverá apoiar decisões reais, não maximizar notificações.
45. O participante permanece no controle.

# 2966. Continuidade normativa

`PAS-001-IC-LIFECYCLE-001 1.0.0` é registrado como a **segunda extensão normativa da Capacidade 07 — Intervenções Contextuais**.

A extensão:

- preserva `PAS-001-IC-FOUNDATION-001 1.0.0`;
- preserva o `PAS-001 0.5.0`;
- mantém as Capacidades 02 a 06 como `Functionally complete`;
- mantém a Capacidade 07 como `In progress`;
- eleva o progresso editorial de `20%` para `40%`;
- preserva a Capacidade 08 como `Planned`;
- consolida estados, dimensões, transições e decisões do ciclo;
- governa frequência, fadiga, sensibilidade e silêncio;
- consolida contestação, correção, revogação, idempotência, ordenação e falha segura;
- estabelece a visualização e o controle como próxima etapa normativa.

O próximo bloco será:

> **Comportamentos funcionais da visualização e do controle das Intervenções Contextuais, incluindo central de intervenções, fila de atenção, mensagens, perguntas, lembretes, alertas, justificativas, histórico, adiamento, silêncio, frequência, horários protegidos, canais, preferências, acessibilidade, privacidade, intervenções sensíveis, relações comerciais e consistência entre superfícies.**
