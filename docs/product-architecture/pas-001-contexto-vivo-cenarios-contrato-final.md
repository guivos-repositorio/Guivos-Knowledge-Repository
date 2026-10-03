---
id: PAS-001-CV-CONTRACT-001
title: Cenários e Contrato Final do Contexto Vivo
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
supersedes_status:
  - PAS-001 sections 44-45
related:
  - PAS-001
  - PAS-001-CV-STATE-001
  - PAS-001-CV-UPDATE-001
  - PAS-001-CV-CONFLICT-001
  - PAS-001-CV-VIEW-001
  - PAS-001-CV-EVENT-001
  - PAS-001-CV-INTEGRATION-001
  - PAS-001-CV-KPI-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-CONTRACT-001 — Cenários e Contrato Final do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é a **oitava extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`, das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0`, das seções 60 a 83 do `PAS-001-CV-UPDATE-001 1.0.0`, das seções 84 a 113 do `PAS-001-CV-CONFLICT-001 1.0.0`, das seções 114 a 148 do `PAS-001-CV-VIEW-001 1.0.0`, das seções 149 a 208 do `PAS-001-CV-EVENT-001 1.0.0`, das seções 209 a 262 do `PAS-001-CV-INTEGRATION-001 1.0.0` e das seções 263 a 310 do `PAS-001-CV-KPI-001 1.0.0`.

Para fins de estado da capacidade e continuidade do Product Engineering, este documento **substitui normativamente as seções 44 e 45 do `PAS-001 0.5.0`**, que permanecem apenas como registro da baseline anterior.

A permanência do arquivo-base do `PAS-001` na versão `0.5.0` até futura edição consolidada não reduz a autoridade desta extensão.

# 311. Cenários funcionais do Contexto Vivo

Os cenários funcionais demonstram como a Capacidade 02 deverá se comportar em diferentes condições de informação, autorização, confiança, integração e risco.

Eles não representam apenas fluxos de interface.

Cada cenário deverá verificar:

- qualidade do contexto disponível;
- finalidade pretendida;
- atualidade;
- confiança;
- conflitos;
- permissões;
- sensibilidade;
- disponibilidade das integrações;
- impacto da decisão;
- possibilidade de atuação segura.

Os cenários serão organizados em três condições principais:

1. **ideal**;
2. **alternativa**;
3. **limite**.

> O Contexto Vivo deverá continuar útil quando as condições não forem ideais, sem preencher lacunas com suposições indevidas.

# 312. Premissas comuns aos cenários

Em qualquer condição:

1. o participante deverá permanecer no controle;
2. ausência de informação não deverá ser interpretada como ausência de condição;
3. comportamento observado não deverá substituir intenção declarada;
4. informação sensível não deverá ser inferida ou ativada sem base adequada;
5. permissões deverão limitar os usos;
6. conflitos relevantes deverão permanecer visíveis;
7. informações envelhecidas deverão ser tratadas conforme impacto;
8. integrações indisponíveis deverão reduzir automação, não aumentar suposições;
9. capacidades consumidoras deverão receber apenas o recorte necessário;
10. decisões críticas deverão exigir contexto proporcionalmente confiável.

# 313. Cenário funcionalmente ideal

O cenário ideal ocorre quando o Contexto Vivo possui informação suficiente, atual, autorizada e explicável para determinada finalidade.

Não exige que todas as oito dimensões estejam integralmente preenchidas.

## Condições esperadas

- participante corretamente identificado;
- finalidade claramente definida;
- contexto suficiente para a ação;
- elementos relevantes atuais;
- proveniência preservada;
- confiança adequada;
- permissões vigentes;
- ausência de conflito crítico;
- integrações necessárias disponíveis;
- capacidades consumidoras sincronizadas;
- participante capaz de visualizar e corrigir a compreensão.

# 314. Fluxo do cenário ideal

```text
Necessidade funcional identificada
→ finalidade validada
→ recorte contextual mínimo construído
→ atualidade e confiança verificadas
→ permissões verificadas
→ capacidade consumidora acionada
→ decisão ou recomendação produzida
→ explicação disponibilizada
→ resultado ou interação devolvida
→ Contexto Vivo atualizado somente quando houver base suficiente
```

Exemplo:

```text
Objetivo ativo:
melhorar a saúde

Disponibilidade confirmada:
sábado pela manhã

Preferência confirmada:
atividade coletiva

Restrição vigente:
evitar atividade de alto impacto

→ Oportunidades Ativas recebe somente o recorte necessário
→ apresenta caminhada em grupo compatível
→ participante compreende por que recebeu a recomendação
```

# 315. Resultado esperado do cenário ideal

No cenário ideal:

- a ação deverá ser relevante;
- o recorte deverá ser mínimo;
- a explicação deverá estar disponível;
- nenhuma informação não autorizada deverá ser utilizada;
- a capacidade consumidora deverá compreender incertezas residuais;
- o participante deverá poder corrigir ou limitar o contexto;
- o resultado deverá retornar como evidência, não como conclusão automática.

# 316. Critérios de aceite do cenário ideal

O cenário será considerado adequado quando:

1. a finalidade estiver identificada;
2. somente elementos necessários forem utilizados;
3. atualidade e confiança forem proporcionais ao impacto;
4. nenhuma hipótese for tratada como fato;
5. permissões forem respeitadas;
6. a decisão puder ser explicada;
7. o participante puder exercer controle;
8. o retorno da experiência não alterar automaticamente dimensões não comprovadas;
9. os eventos funcionais forem registrados;
10. os KPIs relevantes puderem ser medidos.

# 317. Cenário funcionalmente alternativo

O cenário alternativo ocorre quando a finalidade ainda poderá ser atendida, mas alguma condição ideal não está presente.

Exemplos:

- informação parcialmente incompleta;
- integração temporariamente indisponível;
- preferência não confirmada;
- conflito de baixo ou médio impacto;
- elemento próximo de revisão;
- participante optou por não utilizar determinada dimensão;
- contexto suficiente apenas para ação manual;
- capacidade consumidora precisa trabalhar com incerteza explícita.

O cenário alternativo não representa necessariamente erro.

Ele representa operação adaptada e segura.

# 318. Classes de cenário alternativo

## 318.1 Alternativa por informação incompleta

Existe contexto suficiente para oferecer opções, mas não para ordenar ou selecionar automaticamente.

Exemplo:

> A Guivos conhece o objetivo e a localização, mas não conhece a disponibilidade.

Comportamento:

- apresentar opções;
- evitar confirmação de agenda;
- permitir filtro manual;
- solicitar disponibilidade apenas quando necessária.

## 318.2 Alternativa por informação envelhecida

A informação poderá ser utilizada em atividade de baixo impacto, com indicação de incerteza.

Comportamento:

- reduzir confiança;
- solicitar confirmação no momento adequado;
- não utilizar em decisão crítica;
- preservar acesso manual a alternativas.

## 318.3 Alternativa por integração indisponível

A fonte externa não está disponível, mas existe alternativa legítima.

Comportamento:

- utilizar último contexto ainda válido;
- solicitar confirmação direta;
- permitir entrada manual;
- não excluir oportunidade apenas pela indisponibilidade.

## 318.4 Alternativa por conflito não crítico

Informações diferentes existem, mas não impedem completamente a finalidade.

Comportamento:

- expor a incerteza à capacidade consumidora;
- evitar automatização irreversível;
- permitir escolha do participante;
- manter conflito aberto.

## 318.5 Alternativa por permissão limitada

A informação existe, mas não poderá ser usada para a finalidade solicitada.

Comportamento:

- recompor o recorte sem o elemento;
- buscar alternativa;
- solicitar autorização somente quando houver benefício claro;
- respeitar a recusa.

## 318.6 Alternativa por baixa confiança

A compreensão existe apenas como hipótese.

Comportamento:

- utilizar para exploração;
- não utilizar para bloqueio;
- apresentar opções amplas;
- diferenciar hipótese de preferência confirmada.

# 319. Fluxo do cenário alternativo

```text
Finalidade identificada
→ limitação detectada
→ impacto da limitação avaliado
→ alternativa segura localizada
→ automação reduzida
→ incerteza explicitada
→ participante recebe opções ou confirmação contextual
→ ação proporcional executada
→ limitação permanece registrada
```

# 320. Regras do cenário alternativo

1. A experiência deverá continuar quando houver forma segura.
2. A ausência de integração não deverá gerar bloqueio automático.
3. A incerteza deverá ser propagada.
4. A pessoa não deverá ser obrigada a fornecer informação desnecessária.
5. A alternativa manual deverá permanecer disponível quando viável.
6. Recomendações poderão ser ampliadas em vez de excessivamente filtradas.
7. Nenhuma limitação deverá ser ocultada.
8. A capacidade consumidora deverá saber que recebeu contexto parcial.
9. O sistema deverá evitar confirmação repetitiva.
10. O cenário poderá retornar ao ideal após nova informação ou confirmação.

# 321. Critérios de aceite do cenário alternativo

O cenário alternativo será considerado adequado quando:

- a limitação estiver identificada;
- nenhum dado ausente for presumido;
- a alternativa não ampliar permissões;
- o impacto estiver controlado;
- ações críticas permanecerem suspensas quando necessário;
- opções manuais forem oferecidas;
- o participante compreender a limitação relevante;
- o contexto puder evoluir posteriormente;
- eventos e métricas forem produzidos;
- a operação não criar conclusão indevida.

# 322. Cenário funcionalmente limite

O cenário limite ocorre quando não existe base suficiente para atuar com segurança, ou quando qualquer ação poderá violar permissão, confiança, sensibilidade ou controle do participante.

Exemplos:

- identidade do participante incerta;
- informação crítica contraditória;
- revogação ainda não propagada;
- hipótese sensível não confirmada;
- conflito de alto impacto;
- informação expirada indispensável;
- integração associou dados à pessoa incorreta;
- finalidade não autorizada;
- decisão crítica depende de contexto insuficiente;
- risco de exposição de informação de terceiro.

> No cenário limite, não agir poderá ser a decisão funcional correta.

# 323. Tipos de cenário limite

## 323.1 Limite por identificação incerta

Não existe segurança de que a informação pertence ao participante correto.

Resultado:

- não incorporar;
- não compartilhar;
- não utilizar em decisão;
- solicitar verificação adequada.

## 323.2 Limite por permissão

O uso pretendido não está autorizado.

Resultado:

- interromper o processamento;
- recompor o recorte;
- não presumir consentimento;
- explicar a limitação.

## 323.3 Limite por sensibilidade

A informação poderá produzir dano ou exposição indevida.

Resultado:

- exigir finalidade específica;
- limitar acesso;
- solicitar confirmação proporcional;
- impedir inferência crítica.

## 323.4 Limite por conflito crítico

As informações disponíveis sustentam decisões incompatíveis.

Resultado:

- suspender decisão dependente;
- preservar as versões;
- solicitar esclarecimento;
- evitar prevalência silenciosa.

## 323.5 Limite por atualidade

A única informação disponível está expirada ou envelhecida para a finalidade crítica.

Resultado:

- não utilizar;
- solicitar confirmação;
- apresentar alternativa sem dependência daquele elemento.

## 323.6 Limite por revogação

A autorização foi retirada e a propagação ainda não foi concluída.

Resultado:

- suspender preventivamente todos os novos usos relacionados;
- notificar consumidores;
- registrar processamento pendente;
- não informar conclusão antes da efetivação.

## 323.7 Limite por falha grave de integração

A fonte produz dados inválidos, duplicados ou associados incorretamente.

Resultado:

- isolar a fonte;
- suspender efeitos;
- preservar último contexto válido;
- iniciar investigação;
- informar o participante quando houver impacto.

# 324. Fluxo do cenário limite

```text
Finalidade solicitada
→ condição crítica detectada
→ uso ou decisão suspensa
→ dados e efeitos isolados
→ capacidade consumidora informada
→ participante recebe explicação proporcional
→ confirmação, correção, autorização ou investigação solicitada
→ retomada somente após condição segura
```

# 325. Comportamentos obrigatórios no cenário limite

O Contexto Vivo deverá:

- abster-se de conclusão indevida;
- não ocultar a limitação;
- preservar histórico;
- impedir novos usos não autorizados;
- evitar propagação de informação incerta;
- oferecer alternativa segura quando existir;
- não pressionar o participante;
- registrar o motivo da suspensão;
- permitir retomada posterior;
- tratar violações como incidentes quando aplicável.

# 326. Comportamentos proibidos no cenário limite

Não deverá:

- preencher lacunas com inferência;
- apresentar hipótese como fato;
- continuar uso após revogação;
- escolher silenciosamente uma informação conflitante;
- excluir oportunidade relevante por ausência de dado;
- revelar informação sensível para explicar uma falha;
- criar autorização implícita;
- atribuir erro ao participante;
- informar sucesso antes da propagação;
- degradar controle em nome de conveniência.

# 327. Transições entre cenários

Os cenários não são permanentes.

## Ideal → Alternativo

Poderá ocorrer quando:

- informação se aproximar de revisão;
- integração ficar indisponível;
- surgir incerteza;
- permissão for limitada;
- conflito não crítico aparecer.

## Alternativo → Ideal

Poderá ocorrer após:

- confirmação;
- integração restabelecida;
- conflito contextualizado;
- atualização aplicada;
- autorização adequada.

## Ideal ou Alternativo → Limite

Poderá ocorrer após:

- revogação;
- contestação crítica;
- associação incorreta;
- conflito de alto impacto;
- expiração de informação essencial;
- incidente de segurança.

## Limite → Alternativo

Poderá ocorrer quando a condição crítica for reduzida, mas ainda existir incerteza.

## Limite → Ideal

Somente quando:

- a causa crítica estiver resolvida;
- os recortes forem recompostos;
- consumidores estiverem atualizados;
- permissões estiverem válidas;
- confiança e atualidade forem suficientes.

# 328. Cenário de primeiro uso

## Condição

O participante possui pouco ou nenhum contexto registrado.

## Comportamento esperado

- solicitar somente informações necessárias para a primeira finalidade;
- permitir deixar dimensões para depois;
- explicar por que cada informação é solicitada;
- não exigir preenchimento integral;
- registrar declarações sem extrapolação;
- mostrar síntese inicial humilde;
- disponibilizar correção imediata.

## Resultado

O Contexto Vivo inicia em condição parcial, mas funcionalmente suficiente para determinada ação.

# 329. Cenário de atualização declarada

## Condição

O participante informa que algo mudou.

## Comportamento esperado

- diferenciar correção de mudança real;
- identificar data efetiva;
- atualizar somente elementos sustentados;
- preservar estado anterior;
- avaliar dimensões relacionadas;
- recompor recortes;
- notificar capacidades afetadas;
- explicar impactos.

# 330. Cenário de Evento de Vida

## Condição

O participante registra mudança relevante, como:

- mudança de cidade;
- início ou fim de trabalho;
- nascimento de filho;
- problema de saúde;
- conclusão de formação;
- mudança familiar.

## Comportamento esperado

- registrar o evento;
- avaliar dimensões separadamente;
- não presumir todos os impactos;
- solicitar confirmação apenas para efeitos relevantes;
- preservar temporalidade;
- reavaliar decisões dependentes;
- proteger informações sensíveis.

# 331. Cenário de conflito

## Condição

Duas informações incompatíveis afetam a mesma finalidade.

## Comportamento esperado

- abrir conflito;
- preservar proveniência;
- comparar tempo, contexto e natureza;
- verificar coexistência;
- suspender decisão crítica quando necessário;
- envolver o participante proporcionalmente;
- registrar resolução ou manutenção do conflito.

# 332. Cenário de contestação de inferência

## Condição

O participante informa que uma interpretação da Guivos não está correta.

## Comportamento esperado

- suspender o uso da inferência;
- registrar contestação;
- impedir decisões críticas dependentes;
- permitir correção, remoção ou limitação;
- reavaliar inferências derivadas;
- não exigir comprovação;
- explicar quais efeitos foram interrompidos.

# 333. Cenário de revogação

## Condição

O participante revoga finalidade, compartilhamento ou integração.

## Comportamento esperado

- interromper novos usos;
- recompor recortes;
- notificar consumidores;
- reavaliar inferências;
- aplicar retenção adequada;
- confirmar conclusão somente após efetivação;
- informar o que poderá permanecer legitimamente no histórico.

# 334. Cenário de integração indisponível

## Condição

Uma fonte necessária não responde.

## Comportamento esperado

- verificar último contexto válido;
- reduzir confiança;
- impedir ação crítica baseada em suposição;
- oferecer confirmação manual;
- registrar falha;
- evitar exclusão automática;
- retomar sincronização posteriormente.

# 335. Cenário de informação sensível

## Condição

A finalidade depende de informação relacionada a:

- saúde;
- religião;
- renda;
- vulnerabilidade;
- política;
- condição familiar;
- acessibilidade;
- segurança.

## Comportamento esperado

- justificar necessidade;
- solicitar autorização específica;
- minimizar conteúdo;
- limitar consumidores;
- impedir uso publicitário não autorizado;
- fornecer controle reforçado;
- permitir revogação clara;
- ocultar detalhes em visualizações gerais.

# 336. Cenário de informação insuficiente

## Condição

Não existe contexto suficiente para recomendar, filtrar ou decidir.

## Comportamento esperado

A Guivos poderá:

- apresentar opções amplas;
- solicitar uma pergunta objetiva;
- permitir busca manual;
- utilizar informação temporária de sessão;
- explicar que ainda não possui base suficiente;
- adiar a decisão.

Ela não deverá:

- inventar preferência;
- concluir objetivo;
- atribuir identidade;
- bloquear integralmente a jornada sem necessidade.

# 337. Cenário de atualização retroativa

## Condição

O participante informa hoje uma mudança ocorrida no passado.

## Comportamento esperado

- registrar data do fato;
- registrar data de conhecimento;
- preservar decisões tomadas anteriormente;
- corrigir o contexto a partir da data aplicável;
- reavaliar somente consequências ainda relevantes;
- não reescrever a história como se a Guivos já soubesse.

# 338. Cenário entre canais

## Condição

Uma alteração é feita por conversa, aplicativo, web ou canal organizacional autorizado.

## Comportamento esperado

- utilizar o mesmo contrato funcional;
- registrar origem;
- refletir a alteração em `Meu Contexto Hoje`;
- evitar contextos paralelos;
- aplicar permissões comuns;
- preservar histórico entre canais.

# 339. Cenário de relacionamento entre participantes

## Condição

Uma experiência envolve duas ou mais pessoas, organizações ou coletivos.

## Comportamento esperado

- preservar contexto individual;
- limitar informações compartilhadas;
- não permitir alteração unilateral do contexto de outro participante;
- proteger terceiros;
- permitir saída;
- registrar somente o vínculo necessário.

# 340. Cenário de decisão apoiada pelo contexto

## Condição

Uma capacidade solicita contexto para produzir recomendação ou ação.

## Comportamento esperado

- verificar finalidade;
- construir recorte mínimo;
- indicar atualidade e confiança;
- incluir conflitos relevantes;
- impedir uso de elemento não autorizado;
- registrar consumidor;
- disponibilizar explicação;
- receber retorno sem presumir evolução.

# 341. Matriz resumida dos cenários

| Condição | Automação | Uso de contexto | Participação da pessoa | Resultado esperado |
|---|---|---|---|---|
| Ideal | Ampla, mas controlada | Contexto suficiente e autorizado | Controle e correção disponíveis | Decisão contextual adequada |
| Alternativa | Reduzida | Contexto parcial ou incerto | Confirmação ou escolha quando necessária | Continuidade segura |
| Limite | Suspensa ou mínima | Elementos críticos bloqueados | Confirmação, correção ou autorização necessária | Abstenção ou alternativa segura |

# 342. Critérios gerais de aceite dos cenários

Os cenários serão considerados adequadamente definidos quando permitirem:

1. operação segura fora da condição ideal;
2. redução proporcional de automação;
3. propagação explícita de incerteza;
4. suspensão de decisões críticas;
5. alternativas manuais;
6. ausência de inferência para preencher lacunas;
7. transição controlada entre condições;
8. explicação ao participante;
9. eventos e métricas correspondentes;
10. proteção contra exclusão excessiva de oportunidades;
11. respeito às permissões;
12. recuperação após falhas;
13. consistência entre canais;
14. preservação do histórico;
15. retorno ao cenário ideal somente após condição suficiente.

# 343. Contrato final da Capacidade 02 — Contexto Vivo

## Identificação

| Campo | Definição |
|---|---|
| Capacidade | 02 — Contexto Vivo |
| Camada principal | Guivos Journey — Experience Layer |
| Natureza | Capacidade funcional permanente |
| Estado após consolidação | Funcionalmente especificada |
| Especificação principal | PAS-001 |
| Extensões normativas | STATE, UPDATE, CONFLICT, VIEW, EVENT, INTEGRATION, KPI e CONTRACT |
| Participante central | Pessoa, Organização ou Coletivo |
| Capacidades consumidoras | Objetivos, Próximos Passos, Oportunidades, Intervenções, Experiências e Evolução |
| Camadas de apoio | Guivos Intelligence e Platform Layer |

# 344. Propósito da capacidade

O Contexto Vivo existe para manter uma representação multidimensional, temporal, governada e explicável do contexto relevante de um participante.

Seu propósito é permitir que a Guivos:

- compreenda o momento atual;
- preserve continuidade;
- evite repetição desnecessária;
- adapte decisões e experiências;
- reconheça mudanças;
- controle incertezas;
- respeite permissões;
- mantenha o participante no controle.

# 345. Responsabilidade principal

A responsabilidade principal do Contexto Vivo é:

> Manter e disponibilizar uma representação contextual seletiva, atualizável, explicável e autorizada, suficiente para apoiar as demais capacidades da jornada sem definir permanentemente a identidade do participante.

# 346. Responsabilidades funcionais

A capacidade deverá:

1. organizar informações nas oito dimensões;
2. preservar elementos contextuais individualmente;
3. distinguir declaração, observação, evidência e inferência;
4. controlar origem, temporalidade, confiança e finalidade;
5. atualizar elementos seletivamente;
6. envelhecer informações sem tratá-las automaticamente como falsas;
7. registrar e resolver conflitos;
8. preservar histórico;
9. fornecer `Meu Contexto Hoje`;
10. aplicar permissões por finalidade;
11. produzir eventos funcionais;
12. integrar capacidades e fontes;
13. fornecer recortes mínimos;
14. notificar consumidores após mudanças relevantes;
15. medir qualidade e desempenho;
16. operar em condições ideal, alternativa e limite.

# 347. Não responsabilidades

O Contexto Vivo não deverá:

- definir objetivos em nome do participante;
- selecionar sozinho Próximos Passos;
- escolher oportunidades;
- executar intervenções;
- declarar evolução sem base;
- substituir Guivos Intelligence;
- substituir autenticação e infraestrutura;
- criar perfis comerciais irrestritos;
- diagnosticar a pessoa;
- classificar valor ou potencial humano;
- armazenar todo dado disponível;
- ampliar autorização;
- transformar comportamento em intenção;
- tratar integração como verdade absoluta.

# 348. Entradas oficiais

A capacidade poderá receber:

- declarações;
- confirmações;
- correções;
- contestações;
- Eventos de Vida;
- resultados de experiências;
- evidências;
- sinais de interação;
- hipóteses da Intelligence Layer;
- dados de integrações;
- alterações de permissão;
- informações temporárias de sessão;
- eventos de capacidades consumidoras.

Toda entrada deverá ser avaliada antes de alterar o contexto vigente.

# 349. Requisitos de admissão

Uma entrada somente poderá produzir efeito quando houver, conforme sua natureza:

- participante identificado;
- origem conhecida;
- finalidade legítima;
- autorização válida;
- referência temporal;
- natureza da informação;
- elemento afetado;
- sensibilidade;
- confiança;
- evidência suficiente;
- confirmação proporcional;
- ausência de bloqueio crítico.

Entradas que não atendam aos requisitos poderão ser:

- rejeitadas;
- mantidas como hipótese;
- registradas como observação;
- encaminhadas para confirmação;
- transformadas em conflito;
- utilizadas somente em sessão.

# 350. Representação interna funcional

O Contexto Vivo deverá organizar elementos nas dimensões:

1. Identidade;
2. Momento;
3. Direção;
4. Capacidades;
5. Restrições;
6. Preferências;
7. Relacionamentos;
8. Evolução.

Cada elemento deverá possuir:

- conteúdo;
- origem;
- natureza;
- temporalidade;
- confiança;
- sensibilidade;
- finalidade;
- permissões;
- estado funcional;
- histórico;
- evidências;
- conflitos;
- revisão prevista.

# 351. Saídas oficiais

A capacidade poderá produzir:

- síntese do momento atual;
- estado de cada dimensão;
- elementos contextuais autorizados;
- recortes por finalidade;
- informações de atualidade e confiança;
- indicação de conflito;
- necessidade de confirmação;
- histórico contextual;
- explicação de origem e uso;
- eventos funcionais;
- notificações a consumidores;
- sinalização de cenário ideal, alternativo ou limite;
- indicadores de qualidade.

# 352. Contrato dos recortes contextuais

Todo recorte deverá informar:

- finalidade;
- capacidade consumidora;
- elementos necessários;
- origem;
- atualidade;
- confiança;
- conflitos;
- sensibilidade;
- permissões;
- validade;
- limitações.

Um recorte não deverá representar acesso irrestrito ao Contexto Vivo.

# 353. Ciclo de vida funcional

```text
Entrada recebida
→ admissibilidade avaliada
→ elemento criado, atualizado, proposto ou rejeitado
→ dimensão recomposta
→ contexto sintetizado
→ recortes afetados recalculados
→ consumidores notificados
→ decisões reavaliadas
→ histórico e eventos preservados
→ revisão futura programada quando necessária
```

# 354. Regras de atualização

As atualizações deverão ser:

- seletivas;
- proporcionais;
- rastreáveis;
- explicáveis;
- historicamente preservadas;
- reversíveis quando aplicável;
- limitadas à finalidade;
- propagadas de forma controlada.

Nenhuma atualização crítica deverá ocorrer silenciosamente.

# 355. Regras de conflito

Conflitos deverão:

- possuir registro próprio;
- preservar informações envolvidas;
- diferenciar tempo e contexto;
- impedir prevalência automática indevida;
- envolver o participante quando necessário;
- afetar consumidores de forma explícita;
- permanecer reabríveis;
- sustentar explicação.

# 356. Regras de permissão

Permissões deverão:

- ser específicas por finalidade;
- limitar consumidores;
- possuir duração quando aplicável;
- permitir pausa e revogação;
- produzir efeito prioritário;
- recompor recortes;
- impedir novos usos após revogação;
- não ser ampliadas por inferência ou integração.

# 357. Regras de transparência

O participante deverá conseguir:

- visualizar síntese e dimensões;
- identificar origem;
- diferenciar fato e inferência;
- compreender atualidade;
- visualizar conflitos;
- confirmar;
- corrigir;
- contestar;
- limitar;
- ocultar;
- remover;
- revogar;
- consultar histórico;
- solicitar explicação;
- desfazer alterações quando aplicável.

# 358. Eventos oficiais da capacidade

A capacidade deverá produzir eventos específicos para:

- propostas;
- atualizações;
- confirmações;
- correções;
- contestações;
- envelhecimento;
- conflitos;
- permissões;
- integrações;
- propagação;
- reavaliação;
- interação;
- falhas.

Eventos deverão representar fatos reconhecidos, ser versionados e evitar efeitos duplicados.

# 359. Integrações oficiais

O Contexto Vivo deverá integrar-se com:

- Captura de Contexto;
- Objetivos;
- Eventos de Vida;
- Próximos Passos;
- Oportunidades Ativas;
- Intervenções Contextuais;
- Experiências;
- Evolução Contínua;
- Guivos Intelligence;
- Platform Layer;
- Business;
- Mall;
- Travel;
- Media;
- Ads;
- fontes externas autorizadas.

Cada integração deverá possuir contrato funcional próprio.

# 360. Regras de falha

Diante de falha, a capacidade deverá:

- preservar último contexto válido quando adequado;
- reduzir automação;
- explicitar incerteza;
- suspender decisões críticas;
- impedir propagação indevida;
- oferecer alternativa manual;
- registrar processamento pendente;
- informar impacto real;
- retomar somente após condição segura.

# 361. Guardrails obrigatórios

A capacidade não poderá aceitar:

- uso sem autorização;
- finalidade ampliada silenciosamente;
- hipótese sensível tratada como fato;
- revogação ignorada;
- conflito crítico ocultado;
- evento crítico duplicado;
- associação confirmada à pessoa errada;
- exposição indevida de terceiro;
- decisão crítica baseada em informação expirada;
- perfil comercial criado a partir de contexto não autorizado.

Esses casos possuem tolerância funcional zero.

# 362. Indicadores obrigatórios

A capacidade deverá medir, no mínimo:

- cobertura funcional;
- atualidade;
- proveniência;
- confiança;
- correções;
- contestações;
- conflitos;
- permissões;
- revogações;
- explicabilidade;
- esforço;
- fadiga;
- integrações;
- propagação;
- falha segura;
- utilidade dos recortes;
- adequação das decisões;
- exclusões indevidas;
- violações de guardrail.

# 363. Condições de conclusão funcional

A Capacidade 02 será considerada funcionalmente especificada quando:

1. responsabilidades e limites estiverem definidos;
2. entradas e saídas estiverem contratadas;
3. dimensões e estados estiverem definidos;
4. atualização e envelhecimento estiverem especificados;
5. conflitos possuírem tratamento completo;
6. `Meu Contexto Hoje` estiver funcionalmente definido;
7. eventos possuírem contratos;
8. integrações estiverem delimitadas;
9. KPIs e guardrails estiverem estabelecidos;
10. cenários ideal, alternativo e limite estiverem definidos;
11. critérios de aceite estiverem consolidados;
12. não existirem lacunas funcionais críticas conhecidas.

Todos esses critérios estão atendidos pela baseline normativa vigente.

# 364. Critérios finais de aceite da capacidade

O Contexto Vivo deverá permitir que a Guivos:

- compreenda sem rotular;
- atualize sem apagar história;
- personalize sem invadir;
- integre sem perder significado;
- inferir sem transformar hipótese em fato;
- explicar sem sobrecarregar;
- proteger sem bloquear excessivamente;
- agir quando houver base;
- perguntar quando necessário;
- esperar quando apropriado;
- silenciar quando agir puder causar dano;
- manter a pessoa no controle.

# 365. Regras fundamentais finais

1. O Contexto Vivo representa contexto, não identidade definitiva.
2. As oito dimensões evoluem de forma independente.
3. Elementos contextuais são a unidade mínima de atualização.
4. Tempo reduz confiança de atualidade, não prova falsidade.
5. Proveniência deverá acompanhar toda compreensão relevante.
6. Declaração atual prevalece funcionalmente sobre inferência incompatível.
7. Comportamento não define intenção.
8. Conflitos não deverão ser ocultados.
9. Permissões limitam finalidade e consumidores.
10. Revogações interrompem novos usos.
11. Informações sensíveis exigem proteção reforçada.
12. Integrações possuem autoridade limitada.
13. Eventos preservam o que aconteceu.
14. Métricas avaliam o sistema, não a pessoa.
15. Operação alternativa deverá permanecer segura.
16. No cenário limite, abstenção poderá ser a decisão correta.
17. O participante deverá compreender e controlar seu contexto.
18. A implementação técnica não poderá alterar o significado funcional.
19. Nenhuma média positiva poderá compensar violação de guardrail.
20. O valor da capacidade depende de produzir utilidade sob controle do participante.

Com isso, ficam definidos os **cenários funcionalmente ideal, alternativo e limite** e consolidado o **contrato final da Capacidade 02 — Contexto Vivo**.

A Capacidade 02 está **funcionalmente concluída**.

O próximo ponto oficial do Product Engineering é:

> **Capacidade 03 — Objetivos.**
