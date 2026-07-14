---
id: PAS-001-EV-INTEGRATION-001
title: Integrações Funcionais da Capacidade de Eventos de Vida
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-EV-FOUNDATION-001
  - PAS-001-EV-LIFECYCLE-001
  - PAS-001-EV-VIEW-001
  - PAS-001-EV-EVENT-001
  - PAS-001-CV-INTEGRATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-INTEGRATION-001
  - PAS-001-OBJ-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-EV-INTEGRATION-001 — Integrações Funcionais da Capacidade de Eventos de Vida

## 1. Autoridade e vínculo

Este documento é a **quinta extensão normativa da Capacidade 04 — Eventos de Vida** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 885 a 956 de `PAS-001-EV-FOUNDATION-001 1.0.0`, das seções 957 a 1061 de `PAS-001-EV-LIFECYCLE-001 1.0.0`, das seções 1062 a 1144 de `PAS-001-EV-VIEW-001 1.0.0`, das seções 1145 a 1254 de `PAS-001-EV-EVENT-001 1.0.0` e da especificação-base `PAS-001 0.5.0`.

Esta extensão consolida as integrações funcionais da Capacidade de Eventos de Vida com as demais capacidades do Journey, Guivos Intelligence, Platform Layer, produtos e serviços especializados, organizações e fontes externas.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade normativa das extensões anteriores.

# 1255. Integrações funcionais da Capacidade de Eventos de Vida

As integrações deverão permitir que mudanças relevantes da realidade sejam reconhecidas, contextualizadas e utilizadas pelas capacidades autorizadas da Guivos sem transferir titularidade, ampliar indevidamente a autoridade das fontes ou expor vulnerabilidades.

A integração deverá preservar o fluxo:

```text
fonte ou capacidade
→ entrada minimizada
→ validação de identidade, autoridade e finalidade
→ sinal, proposta ou fato reconhecido
→ Evento de Vida
→ impactos avaliados
→ recortes autorizados
→ capacidades responsáveis reavaliam suas unidades
```

> Integrar um Evento de Vida não significa entregar sua narrativa completa a todo o ecossistema. Significa fornecer a cada consumidor somente o recorte necessário para uma finalidade legítima.

# 1256. Objetivos das integrações

As integrações deverão:

1. receber mudanças relevantes de fontes autorizadas;
2. identificar corretamente o participante;
3. preservar origem e temporalidade;
4. limitar a autoridade de cada fonte;
5. distinguir fato, sinal, hipótese e proposta;
6. evitar duplicidades;
7. identificar impactos possíveis;
8. solicitar reavaliações às capacidades responsáveis;
9. propagar somente recortes necessários;
10. proteger eventos sensíveis;
11. controlar compartilhamentos e revogações;
12. preservar histórico e explicabilidade;
13. tratar divergências;
14. operar com degradação controlada;
15. impedir exploração comercial de vulnerabilidades;
16. manter o participante no controle.

# 1257. Princípios das integrações

## 1257.1 Finalidade explícita

Toda integração deverá possuir finalidade definida antes do acesso ou da propagação.

## 1257.2 Minimização

A integração deverá utilizar somente as informações necessárias.

## 1257.3 Autoridade limitada

Nenhuma fonte poderá afirmar além do seu escopo legítimo.

## 1257.4 Titularidade preservada

O Evento de Vida pertence ao participante titular, não à integração ou ao consumidor.

## 1257.5 Independência funcional

Cada capacidade deverá governar suas próprias unidades e decisões.

## 1257.6 Confirmação proporcional

Entradas de maior impacto ou sensibilidade deverão exigir confirmação ou autoridade equivalente.

## 1257.7 Revogabilidade

Compartilhamentos e usos revogáveis deverão poder ser interrompidos.

## 1257.8 Explicabilidade

O participante deverá compreender origem, finalidade, uso e efeitos.

## 1257.9 Neutralidade comercial

Receita, patrocínio, comissão ou estoque não deverão influenciar o reconhecimento ou o tratamento do evento.

## 1257.10 Falha segura

Falhas deverão reduzir automação e preservar o último estado válido.

# 1258. Tipos de integração

As integrações poderão ser:

- internas entre capacidades;
- internas entre produtos;
- externas institucionais;
- externas pessoais;
- autorizadas pelo participante;
- organizacionais;
- coletivas;
- temporárias;
- contínuas;
- síncronas;
- assíncronas;
- orientadas a eventos;
- orientadas a consulta;
- manuais;
- assistidas;
- automatizadas dentro de limites definidos.

# 1259. Modos de integração

## Recebimento

A Capacidade 04 recebe informação que poderá representar Evento de Vida.

## Consulta

A capacidade consulta fonte autorizada para complementar ou validar informação.

## Propagação

A capacidade envia recorte para outro consumidor.

## Solicitação de revisão

A capacidade informa que determinada unidade funcional poderá precisar de reavaliação.

## Confirmação de processamento

O consumidor informa que recebeu e processou o recorte.

## Sincronização

Estados relacionados são mantidos consistentes entre sistemas.

## Reconciliação

Divergências são identificadas e tratadas.

# 1260. Contrato funcional comum

Toda integração deverá definir:

| Elemento | Definição necessária |
|---|---|
| Produtor | Quem fornece a informação |
| Consumidor | Quem recebe |
| Titular | Participante a quem o evento pertence |
| Finalidade | Por que a integração existe |
| Autoridade | O que a fonte pode afirmar |
| Entrada | Informação recebida |
| Saída | Recorte produzido |
| Temporalidade | Frequência, latência e período |
| Confiança | Qualidade e certeza |
| Sensibilidade | Proteções aplicáveis |
| Permissões | Usos autorizados |
| Transformações | Alterações realizadas |
| Eventos | Fatos funcionais produzidos |
| Falhas | Tratamento de erros |
| Revogação | Interrupção de novos usos |
| Retenção | Tempo e finalidade de conservação |
| Explicação | Informação oferecida ao participante |

# 1261. Requisitos de admissão

Uma integração somente deverá produzir efeitos quando houver:

- participante identificado;
- fonte identificada;
- contrato vigente;
- finalidade válida;
- autoridade compatível;
- temporalidade representável;
- qualidade mínima;
- sensibilidade classificada;
- permissões aplicáveis;
- possibilidade de contestação;
- tratamento de revogação;
- consumidor responsável.

Entradas inadequadas deverão permanecer como sinal, hipótese, proposta ou rejeição.

# 1262. Identidade e associação

Antes de associar informação a um Evento de Vida, deverão ser validados:

- identidade do titular;
- categoria do participante;
- organização ou coletivo relacionado;
- identificadores externos;
- representação autorizada;
- possibilidade de homônimos;
- associação a evento existente;
- risco de exposição cruzada.

Associação incerta deverá bloquear efeitos materiais.

# 1263. Titular, ator, fonte e participante afetado

A integração deverá distinguir:

- titular do evento;
- ator envolvido na mudança;
- fonte da informação;
- representante autorizado;
- organização relacionada;
- participante afetado;
- consumidor do recorte.

Esses papéis não deverão ser tratados como equivalentes.

# 1264. Autoridade da fonte

A integração deverá registrar:

- fatos que a fonte pode confirmar;
- interpretações que poderá sugerir;
- informações que não poderá afirmar;
- período de validade;
- escopo organizacional;
- limites territoriais ou contratuais;
- nível de confiança.

A autoridade técnica de acesso não deverá representar autoridade funcional.

# 1265. Proveniência

Cada entrada deverá preservar:

- sistema de origem;
- organização responsável;
- identificador externo;
- data do fato;
- data da publicação;
- data de recebimento;
- transformação aplicada;
- versão do contrato;
- autoridade;
- confiança;
- finalidade;
- permissões.

# 1266. Qualidade da informação

A qualidade deverá considerar:

- completude;
- consistência;
- atualidade;
- precisão conhecida;
- estabilidade;
- autenticidade;
- associação correta;
- disponibilidade;
- possibilidade de contestação.

Baixa qualidade deverá reduzir os efeitos permitidos.

# 1267. Transformações

Transformações poderão incluir:

- normalização;
- tradução;
- classificação;
- extração de datas;
- associação de participantes;
- deduplicação;
- minimização;
- pseudonimização;
- agregação;
- conversão de unidade;
- geração de resumo.

Toda transformação material deverá ser rastreável.

# 1268. Transformações proibidas

A integração não deverá:

- converter sinal em fato confirmado;
- ampliar autoridade;
- fabricar data exata;
- atribuir significado emocional;
- criar diagnóstico;
- inferir causalidade sem base;
- transformar atividade em Evento de Vida;
- ocultar divergência;
- remover sensibilidade;
- criar perfil de terceiro;
- converter vulnerabilidade em segmentação comercial.

# 1269. Temporalidade da integração

A integração deverá distinguir:

- data do fato;
- data informada pela fonte;
- data de recebimento;
- data de processamento;
- data de reconhecimento;
- data de aplicação;
- frequência de sincronização;
- última atualização;
- atraso conhecido.

# 1270. Atualização em tempo real

Integração em tempo real somente deverá ser utilizada quando:

- houver necessidade funcional;
- a frequência for proporcional;
- o participante compreender o uso;
- o risco de exposição estiver controlado;
- a fonte possuir autoridade;
- o benefício superar o custo de vigilância.

Eventos de Vida não deverão ser inferidos continuamente apenas porque existe acesso técnico a dados em tempo real.

# 1271. Dados históricos

Fontes poderão fornecer dados anteriores à conexão.

A incorporação deverá considerar:

- finalidade;
- intervalo autorizado;
- sensibilidade;
- volume;
- capacidade de contestação;
- relevância atual;
- retenção;
- risco de reconstrução excessiva da vida.

O histórico não deverá ser importado integralmente por padrão.

# 1272. Sincronização

A sincronização deverá preservar:

- versão vigente;
- estado do evento;
- estado da informação;
- temporalidade;
- permissões;
- contestações;
- correções;
- revogações;
- impactos;
- recortes.

# 1273. Prevenção de ciclos

A integração deverá evitar ciclos como:

```text
fonte externa gera sinal
→ Evento de Vida atualiza Contexto Vivo
→ Contexto Vivo retorna a mesma atualização
→ novo Evento de Vida duplicado
```

Deverão ser utilizados:

- correlação;
- causalidade;
- identificador externo;
- versão;
- origem;
- idempotência;
- transformação registrada.

# 1274. Divergência entre fontes

Quando duas fontes apresentarem informações incompatíveis, a capacidade deverá:

- preservar ambas;
- identificar autoridade;
- comparar temporalidade;
- limitar efeitos;
- reduzir confiança;
- solicitar confirmação quando necessário;
- impedir sobrescrita silenciosa;
- registrar a divergência.

# 1275. Hierarquia não absoluta das fontes

Não deverá existir uma hierarquia universal em que uma fonte sempre prevaleça.

A consideração deverá depender de:

- fato afirmado;
- autoridade;
- titularidade;
- temporalidade;
- evidência;
- finalidade;
- sensibilidade;
- contestação.

# 1276. Integração com Captura de Contexto

A Captura de Contexto poderá fornecer:

- declaração livre;
- mudança recente;
- evento planejado;
- evento em andamento;
- impacto percebido;
- correção;
- contestação;
- informação sensível;
- narrativa contextual.

# 1277. Responsabilidades da Captura de Contexto

A Captura deverá:

- preservar expressão original;
- identificar participante e canal;
- registrar temporalidade declarada;
- evitar classificação definitiva;
- indicar sensibilidade aparente;
- informar incerteza;
- encaminhar a informação para avaliação.

# 1278. Limites da Captura de Contexto

A Captura não deverá:

- confirmar unilateralmente evento;
- impor categoria;
- declarar relevância definitiva;
- aplicar impactos;
- atualizar objetivos;
- criar causalidade;
- propagar conteúdo sensível diretamente.

# 1279. Retorno para Captura de Contexto

A Capacidade 04 poderá solicitar:

- esclarecimento;
- confirmação;
- data aproximada;
- titularidade;
- impacto percebido;
- participantes envolvidos;
- permissão;
- correção.

As perguntas deverão ser proporcionais e evitar repetição.

# 1280. Integração com Contexto Vivo

A Capacidade de Eventos de Vida deverá informar ao Contexto Vivo:

- evento reconhecido;
- mudança representada;
- dimensão possivelmente afetada;
- estado anterior conhecido;
- estado resultante proposto;
- temporalidade;
- origem;
- autoridade;
- confiança;
- sensibilidade;
- permissões.

# 1281. Responsabilidade do Contexto Vivo

O Contexto Vivo deverá decidir, por seus contratos:

- admitir atualização;
- solicitar confirmação;
- aplicar alteração;
- manter como proposta;
- registrar conflito;
- limitar uso;
- rejeitar;
- envelhecer informação;
- recompor recortes.

# 1282. Separação funcional com o Contexto Vivo

```text
Evento de Vida:
governa a mudança

Contexto Vivo:
governa o estado resultante
```

A Capacidade 04 não deverá manter uma versão paralela do estado contextual.

# 1283. Atualização contextual automática

Atualização automática poderá ocorrer somente quando:

- o fato for objetivo;
- a fonte tiver autoridade;
- o impacto for de baixo risco;
- a alteração for reversível;
- a finalidade estiver autorizada;
- não houver conflito;
- não envolver interpretação pessoal sensível;
- o contrato do Contexto Vivo permitir.

# 1284. Atualizações contextuais proibidas

Não deverão ser aplicadas automaticamente:

- identidade subjetiva;
- significado emocional;
- direção pessoal;
- preferência sensível;
- relacionamento íntimo;
- diagnóstico;
- avaliação de valor;
- mudança espiritual;
- conclusão sobre evolução humana.

# 1285. Integração com Objetivos

A Capacidade 04 poderá informar à Capacidade de Objetivos:

- objetivo potencialmente afetado;
- possível alteração de prioridade;
- bloqueio;
- desbloqueio;
- mudança de horizonte;
- conflito;
- critério possivelmente inadequado;
- evidência relacionada;
- conclusão potencial;
- necessidade de revisão.

# 1286. Responsabilidade da Capacidade de Objetivos

Objetivos deverá governar:

- confirmação de impacto;
- alteração de prioridade;
- pausa;
- bloqueio;
- reformulação;
- mudança de critério;
- conclusão;
- retirada;
- criação de novo objetivo;
- reativação.

# 1287. Limites da integração com Objetivos

Eventos de Vida não deverão:

- criar objetivo pessoal ativo;
- confirmar objetivo;
- impor prioridade;
- retirar objetivo;
- concluir objetivo qualitativo;
- alterar critério pessoal definitivamente;
- interpretar inatividade como abandono.

# 1288. Revisão agrupada de objetivos

Quando um evento afetar diversos objetivos, a capacidade poderá propor revisão agrupada.

A revisão deverá:

- identificar objetivos;
- explicar impactos;
- permitir avaliação individual;
- evitar decisões em massa;
- preservar objetivos não afetados;
- reduzir fadiga.

# 1289. Integração com Próximos Passos

A Capacidade 04 poderá solicitar que Próximos Passos sejam:

- criados;
- reavaliados;
- suspensos;
- cancelados;
- reordenados;
- adiados;
- substituídos;
- mantidos.

# 1290. Responsabilidade de Próximos Passos

A Capacidade 05 deverá decidir:

- qual ação é necessária;
- prioridade operacional;
- momento adequado;
- dependências;
- responsável;
- conclusão;
- cancelamento;
- substituição.

O Evento de Vida não deverá conter o ciclo completo da ação.

# 1291. Eventos críticos e Próximos Passos

Eventos críticos poderão justificar tratamento prioritário, mas não deverão gerar automaticamente:

- excesso de tarefas;
- plano completo;
- múltiplas notificações;
- ações não autorizadas;
- recomendações fora da competência da Guivos.

# 1292. Integração com Oportunidades Ativas

Eventos de Vida poderão alterar:

- elegibilidade;
- localização;
- disponibilidade;
- prazo;
- restrições;
- segurança;
- necessidade;
- relevância;
- acionabilidade;
- janela temporal.

# 1293. Responsabilidade de Oportunidades Ativas

A Capacidade 06 deverá:

- recalcular relevância;
- validar elegibilidade;
- respeitar prioridade;
- considerar restrições;
- identificar oportunidade patrocinada;
- preservar neutralidade;
- explicar compatibilidade.

# 1294. Limites comerciais

Um Evento de Vida não deverá ser utilizado para:

- explorar vulnerabilidade;
- aumentar preço;
- induzir compra urgente;
- segmentar publicidade sensível;
- priorizar patrocinador;
- inferir fragilidade financeira;
- vender solução como inevitável;
- ocultar alternativas não comerciais.

# 1295. Integração com Intervenções Contextuais

A Capacidade 04 poderá informar:

- necessidade de ação;
- necessidade de pergunta;
- necessidade de alerta;
- necessidade de acompanhamento;
- necessidade de silêncio;
- risco de fadiga;
- sensibilidade;
- urgência funcional;
- confiança.

# 1296. Responsabilidade de Intervenções Contextuais

A Capacidade 07 deverá decidir:

- agir;
- perguntar;
- orientar;
- lembrar;
- observar;
- esperar;
- silenciar;
- escolher canal;
- escolher momento;
- limitar conteúdo.

# 1297. Intervenções em eventos sensíveis

Eventos sensíveis deverão favorecer:

- discrição;
- linguagem neutra;
- confirmação antes de detalhes;
- canais privados;
- baixa frequência;
- controle do participante;
- possibilidade de silêncio.

Gravidade percebida não autoriza comunicação invasiva.

# 1298. Integração com Experiências

Uma experiência poderá:

- produzir sinal de Evento de Vida;
- produzir evidência;
- iniciar transição;
- encerrar transição;
- alterar impacto;
- ser interrompida pelo evento;
- mudar de significado.

# 1299. Separação entre Experiência e Evento de Vida

```text
Experiência:
vivência realizada

Evento de Vida:
mudança relevante da realidade
```

A participação em uma experiência não deverá ser registrada automaticamente como mudança relevante.

# 1300. Resultados de experiências

Resultados poderão gerar:

- evidência;
- impacto proposto;
- Evento de Vida proposto;
- atualização contextual;
- revisão de objetivo.

A capacidade responsável deverá confirmar cada efeito por seu próprio contrato.

# 1301. Integração com Evolução Contínua

Eventos de Vida poderão servir como:

- marcos temporais;
- transições;
- delimitadores de ciclos;
- explicações contextuais;
- pontos de comparação;
- causas possíveis de mudança;
- origem de novas capacidades ou restrições.

# 1302. Limites com Evolução Contínua

A ocorrência de Evento de Vida não deverá representar automaticamente:

- progresso;
- regressão;
- sucesso;
- fracasso;
- maturidade;
- transformação;
- valor humano.

Evolução Contínua deverá produzir suas próprias avaliações.

# 1303. Integração com Guivos Intelligence

Guivos Intelligence poderá:

- identificar sinais;
- sugerir classificação;
- propor evento;
- relacionar eventos;
- sugerir relevância;
- propor impactos;
- identificar objetivos possivelmente afetados;
- detectar inconsistências;
- resumir mudanças;
- sugerir perguntas;
- produzir explicações;
- apoiar deduplicação;
- identificar padrões operacionais.

# 1304. Saídas permitidas da Guivos Intelligence

As saídas deverão permanecer como:

- hipótese;
- proposta;
- recomendação;
- classificação sugerida;
- possível impacto;
- alerta;
- resumo;
- explicação.

O grau de confiança e as limitações deverão permanecer visíveis.

# 1305. Ações proibidas da Guivos Intelligence

Guivos Intelligence não deverá:

- confirmar unilateralmente evento pessoal sensível;
- definir significado emocional;
- diagnosticar;
- criar objetivo pessoal ativo;
- impor prioridade;
- concluir objetivo;
- compartilhar evento;
- ampliar autoridade de fonte;
- afirmar causalidade sem base;
- explorar vulnerabilidade;
- ocultar incerteza.

# 1306. Dados para inteligência

O uso de Eventos de Vida pela Guivos Intelligence deverá respeitar:

- finalidade;
- minimização;
- sensibilidade;
- isolamento;
- autorização;
- retenção;
- auditabilidade;
- exclusão de usos incompatíveis;
- proteção contra reidentificação.

# 1307. Aprendizado e melhoria

Aprendizados agregados poderão aperfeiçoar:

- classificação;
- identificação de duplicidades;
- explicações;
- prevenção de falhas;
- estimativas de impacto;
- experiência de confirmação.

Eles não deverão gerar perfil oculto de vulnerabilidade individual.

# 1308. Integração com a Platform Layer

A Platform Layer deverá fornecer suporte técnico para:

- identidade;
- autenticação;
- autorização;
- consentimentos;
- persistência;
- versionamento;
- eventos;
- filas;
- APIs;
- grafo;
- busca;
- notificações;
- armazenamento;
- auditoria;
- observabilidade;
- retenção;
- exclusão.

# 1309. Identidade e autenticação

A Platform Layer deverá:

- validar participante;
- validar representante;
- separar Pessoa, Organização e Coletivo;
- proteger troca de contexto;
- impedir associação cruzada;
- registrar nível de autenticação;
- exigir autenticação reforçada quando necessário.

# 1310. Autorização

A autorização deverá avaliar:

- ator;
- ação;
- evento;
- finalidade;
- sensibilidade;
- consumidor;
- período;
- contexto;
- representação;
- revogação.

# 1311. Grafo

O grafo poderá representar relações entre:

- participantes;
- Eventos de Vida;
- impactos;
- dimensões contextuais;
- objetivos;
- experiências;
- organizações;
- fontes;
- permissões;
- capacidades consumidoras.

A existência de relação técnica não deverá autorizar acesso ao conteúdo.

# 1312. APIs

APIs deverão:

- utilizar contratos versionados;
- exigir autenticação;
- validar finalidade;
- limitar campos;
- aplicar autorização;
- registrar correlação;
- suportar idempotência;
- distinguir comando e evento;
- evitar exposição excessiva;
- retornar estados reais de processamento.

# 1313. Busca

A busca deverá respeitar:

- titularidade;
- sensibilidade;
- finalidade;
- escopo;
- minimização;
- ocultação;
- revogação;
- retenção;
- informação de terceiros.

Eventos sensíveis não deverão ser indexados integralmente por padrão.

# 1314. Notificações

Notificações deverão:

- minimizar conteúdo;
- utilizar título neutro;
- respeitar canal;
- respeitar silêncio;
- evitar exposição;
- indicar quando existe ação pendente;
- não afirmar processamento concluído prematuramente;
- permitir controle do participante.

# 1315. Armazenamento

O armazenamento deverá separar, quando necessário:

- dados estruturados;
- expressão original;
- documentos;
- evidências;
- informações sensíveis;
- logs;
- recortes;
- permissões;
- histórico.

# 1316. Observabilidade

A observabilidade deverá permitir acompanhar:

- entradas;
- rejeições;
- eventos produzidos;
- duplicidades;
- latência;
- divergências;
- falhas;
- reprocessamentos;
- propagação;
- revogações;
- exposições indevidas;
- estado dos consumidores.

Logs não deverão conter narrativas sensíveis quando metadados mínimos forem suficientes.

# 1317. Integração com Guivos Business

Guivos Business poderá fornecer ou consumir Eventos de Vida organizacionais, como:

- contratação;
- desligamento;
- promoção;
- mudança de função;
- afastamento;
- conclusão de treinamento;
- reestruturação;
- mudança de unidade.

# 1318. Limites da Guivos Business

A organização poderá confirmar fatos institucionais sob sua autoridade.

Ela não deverá:

- definir impacto pessoal integral;
- acessar objetivos pessoais não compartilhados;
- inferir estado emocional;
- receber conteúdo familiar, espiritual ou clínico;
- utilizar evento para avaliação discriminatória;
- impor objetivo pessoal;
- acompanhar toda a jornada do colaborador.

# 1319. Separação entre evento institucional e pessoal

Um mesmo fato poderá gerar:

```text
Evento institucional:
desligamento registrado pela organização

Evento pessoal:
transição profissional vivenciada pelo participante
```

Os registros deverão possuir titularidade, autoridade, finalidade e permissões distintas.

# 1320. Integração com Guivos Mall

Guivos Mall poderá receber recortes somente quando necessários para:

- adequar disponibilidade;
- impedir oferta incompatível;
- ajustar localização;
- respeitar restrição;
- cumprir pedido explicitamente solicitado;
- apoiar solução escolhida pelo participante.

# 1321. Limites da Guivos Mall

Guivos Mall não deverá:

- receber narrativa completa;
- utilizar vulnerabilidade para venda;
- concluir impacto;
- criar Evento de Vida a partir de compra;
- tratar compra como progresso;
- aumentar urgência comercial;
- priorizar produto patrocinado por causa do evento.

# 1322. Integração com Guivos Travel

Guivos Travel poderá relacionar-se a eventos como:

- mudança de cidade;
- viagem de longa duração;
- imigração;
- retorno;
- alteração de residência;
- deslocamento relevante;
- início de jornada internacional.

# 1323. Limites da Guivos Travel

Reserva ou compra não deverá confirmar:

- mudança permanente;
- imigração concluída;
- alteração de residência;
- impacto emocional;
- novo objetivo;
- progresso pessoal.

Dados de localização deverão possuir finalidade e retenção restritas.

# 1324. Integração com Guivos Media

Guivos Media poderá utilizar eventos somente para:

- oferecer conteúdo contextual autorizado;
- explicar transições;
- apresentar histórias ou orientações gerais;
- apoiar compreensão.

# 1325. Limites da Guivos Media

Guivos Media não deverá:

- expor Evento de Vida;
- transformar história pessoal em conteúdo sem autorização específica;
- criar perfil editorial sensível;
- tratar consumo de conteúdo como confirmação de mudança;
- utilizar vulnerabilidade para aumentar engajamento.

# 1326. Integração com Guivos Ads

Guivos Ads deverá permanecer funcionalmente separada da Capacidade de Eventos de Vida.

Eventos sensíveis não deverão ser utilizados para segmentação publicitária.

# 1327. Usos publicitários proibidos

Não deverão ser utilizados para publicidade:

- diagnóstico;
- separação;
- falecimento;
- desemprego;
- dívida;
- violência;
- vulnerabilidade;
- religião;
- sexualidade;
- migração sensível;
- deficiência;
- condição familiar;
- crise pessoal.

Mesmo eventos não sensíveis exigirão finalidade distinta e autorização quando aplicável.

# 1328. Serviços profissionais e empregadores

Fontes profissionais poderão confirmar:

- vínculo;
- função;
- início;
- término;
- promoção;
- afastamento;
- certificação;
- fato contratual.

Não poderão confirmar automaticamente:

- satisfação;
- vocação;
- impacto familiar;
- identidade profissional subjetiva;
- transformação pessoal.

# 1329. Instituições educacionais

Instituições poderão fornecer:

- matrícula;
- início;
- conclusão;
- aprovação;
- reprovação;
- interrupção;
- certificação.

Esses fatos não deverão confirmar:

- aprendizado integral;
- mudança de identidade;
- evolução humana;
- conquista de objetivo pessoal não compartilhado.

# 1330. Serviços de saúde

Integrações de saúde somente deverão existir com:

- base legítima;
- autorização adequada;
- escopo mínimo;
- proteção reforçada;
- finalidade explícita;
- controles de acesso;
- retenção limitada;
- explicabilidade.

A Guivos não deverá realizar diagnóstico ou substituir profissional de saúde.

# 1331. Serviços financeiros

Fontes financeiras poderão fornecer fatos autorizados como:

- mudança de renda declarada;
- recebimento;
- encerramento de benefício;
- quitação;
- obrigação financeira;
- alteração contratual.

Não deverão ser utilizados para:

- inferir valor pessoal;
- expor renda;
- segmentar publicidade vulnerável;
- impor prioridade;
- definir impacto emocional;
- compartilhar com organizações sem base legítima.

# 1332. Calendários

Calendários poderão indicar:

- evento planejado;
- compromisso;
- previsão;
- período;
- alteração;
- cancelamento.

Um compromisso no calendário não deverá confirmar que o Evento de Vida ocorreu.

# 1333. Localização e mobilidade

Sinais de localização poderão sugerir:

- viagem;
- mudança de rotina;
- possível mudança residencial;
- alteração de deslocamento.

Eles não deverão confirmar mudança permanente sem base adicional.

A localização precisa deverá possuir tratamento de alta sensibilidade.

# 1334. Aplicativos esportivos e de atividade

Aplicativos poderão informar:

- atividade;
- interrupção;
- retomada;
- mudança de rotina;
- evento esportivo registrado.

Atividade física não deverá ser convertida automaticamente em Evento de Vida, recuperação ou transformação pessoal.

# 1335. Organizações sociais e voluntariado

Organizações poderão confirmar:

- adesão;
- participação;
- conclusão de ação;
- mudança de papel;
- liderança;
- saída.

Participação isolada não deverá ser tratada como mudança permanente de identidade social.

# 1336. Comunidades religiosas e espirituais

Integrações deverão ser excepcionalmente restritas.

Uma organização poderá confirmar somente fatos institucionais autorizados.

Não deverá:

- inferir crença;
- registrar conversão sem declaração;
- compartilhar prática;
- expor participação;
- utilizar informação comercialmente;
- criar classificação espiritual.

# 1337. Serviços jurídicos e governamentais

Fontes poderão confirmar fatos oficiais sob seu escopo, como:

- registro;
- mudança documental;
- decisão;
- vínculo;
- benefício;
- autorização.

A existência do dado público não representa autorização para incorporação irrestrita à Guivos.

# 1338. Fontes públicas

Informações públicas somente deverão ser utilizadas quando:

- houver finalidade legítima;
- forem necessárias;
- possuírem associação segura;
- não produzirem vigilância excessiva;
- puderem ser contestadas;
- respeitarem sensibilidade e contexto.

# 1339. Integrações pessoais

O participante poderá conectar:

- calendário;
- arquivos;
- aplicativos;
- dispositivos;
- contas profissionais;
- serviços educacionais;
- serviços esportivos;
- fontes financeiras;
- serviços de viagem.

A conexão deverá explicar quais informações poderão ser utilizadas.

# 1340. Integrações temporárias

Uma integração poderá ser autorizada apenas para:

- confirmar evento específico;
- importar documento;
- verificar fato;
- acompanhar transição;
- concluir processamento;
- produzir determinado recorte.

Após a finalidade, o acesso deverá ser encerrado ou reduzido.

# 1341. Pausa da integração

O participante deverá poder pausar integração quando aplicável.

A pausa deverá:

- interromper novas coletas;
- preservar histórico necessário;
- indicar impactos sobre atualidade;
- suspender automações dependentes;
- permitir retomada;
- não apagar fatos já reconhecidos automaticamente.

# 1342. Revogação

A revogação deverá:

- interromper novos acessos;
- interromper novos usos;
- recompor recortes;
- notificar consumidores;
- acompanhar propagação;
- preservar obrigações legítimas;
- informar pendências.

# 1343. Revogação e fato histórico

Revogar uma integração não significa que um fato legitimamente reconhecido deixou de ocorrer.

A capacidade deverá distinguir:

- fonte desconectada;
- uso futuro revogado;
- evento histórico;
- evidência indisponível;
- retenção legítima;
- conteúdo passível de exclusão.

# 1344. Falha de integração

Uma falha poderá envolver:

- indisponibilidade;
- autenticação;
- autorização;
- associação;
- versão;
- transformação;
- duplicidade;
- atraso;
- divergência;
- propagação;
- revogação;
- retenção.

# 1345. Degradação controlada

Quando uma integração falhar, a capacidade deverá:

- preservar o último estado válido;
- reduzir confiança;
- indicar desatualização;
- suspender efeitos críticos;
- evitar falsa confirmação;
- limitar automação;
- oferecer alternativa manual;
- informar o participante quando relevante.

# 1346. Fonte indisponível

A indisponibilidade deverá resultar em:

- estado desconhecido;
- informação possivelmente desatualizada;
- revisão pendente;
- uso limitado;
- tentativa de recuperação.

Ausência de dado não deverá ser tratada como ausência de evento.

# 1347. Informação incompleta

Entradas incompletas poderão permanecer como:

- sinal;
- proposta;
- confirmação parcial;
- impacto proposto;
- divergência;
- pendência.

A capacidade não deverá completar lacunas por suposição silenciosa.

# 1348. Informação retroativa

Quando a fonte fornecer evento passado, deverão ser preservados:

- data do fato;
- data de conhecimento;
- data de integração;
- decisões anteriores;
- possíveis impactos históricos;
- limites da reconstrução;
- necessidade de revisão atual.

# 1349. Correção de fonte externa

Quando uma fonte corrigir informação, a capacidade deverá:

- preservar valor anterior;
- registrar correção;
- validar autoridade;
- recompor impactos;
- notificar consumidores;
- reavaliar decisões;
- evitar duplicidade.

# 1350. Eventos relacionados a mais de um participante

Uma integração deverá separar:

- evento compartilhado;
- impacto individual;
- conteúdo privado;
- autoridade de cada parte;
- permissões;
- contestações;
- perspectivas divergentes.

# 1351. Pessoa, Organização e Coletivo

Cada categoria deverá possuir contratos de:

- identidade;
- titularidade;
- representação;
- autoridade;
- consentimento;
- decisão;
- compartilhamento;
- saída;
- contestação.

# 1352. Objetivos e eventos compartilhados

Um evento compartilhado não deverá alterar automaticamente objetivos de todos os participantes.

Cada participante deverá poder:

- confirmar seu impacto;
- limitar compartilhamento;
- contestar;
- manter objetivo próprio;
- sair da relação compartilhada;
- preservar conteúdo privado.

# 1353. Informações de terceiros

A integração deverá:

- minimizar identidade;
- evitar criação de perfil;
- não inferir estado interno;
- limitar acesso;
- utilizar descrição genérica;
- impedir propagação desnecessária;
- preservar somente o necessário para o evento do titular.

# 1354. Explicabilidade das integrações

O participante deverá conseguir compreender:

- qual fonte está conectada;
- qual informação foi recebida;
- por qual finalidade;
- com qual autoridade;
- quais transformações ocorreram;
- qual evento foi reconhecido;
- quais impactos foram propostos;
- quais capacidades receberam recortes;
- como pausar ou revogar;
- quais efeitos permanecem pendentes.

# 1355. Auditoria

A auditoria deverá permitir reconstruir:

```text
fonte
→ autenticação
→ entrada
→ transformação
→ validação
→ proposta ou evento
→ impactos
→ recortes
→ consumidores
→ processamento
→ correções, falhas ou revogações
```

# 1356. Retenção

A retenção deverá considerar:

- finalidade;
- sensibilidade;
- autoridade;
- estado do evento;
- dependências;
- obrigação legítima;
- contestação;
- explicabilidade;
- revogação;
- controle do participante.

Sinais rejeitados deverão possuir retenção reduzida.

# 1357. Eventos funcionais das integrações

A capacidade poderá produzir:

- `IntegracaoDeEventoDeVidaAutorizada`;
- `IntegracaoDeEventoDeVidaAtivada`;
- `EntradaIntegradaDeEventoDeVidaRecebida`;
- `EntradaIntegradaDeEventoDeVidaRejeitada`;
- `IdentidadeDeEntradaIntegradaConfirmada`;
- `AssociacaoDeEntradaIntegradaContestado`;
- `AutoridadeDeFonteDeEventoValidada`;
- `QualidadeDeEntradaIntegradaAvaliada`;
- `TransformacaoDeEntradaIntegradaAplicada`;
- `PossivelEventoDeVidaIdentificadoPorIntegracao`;
- `EventoDeVidaConfirmadoPorFonteAutorizada`;
- `ImpactoDeEntradaIntegradaProposto`;
- `RecorteDeEventoDeVidaProduzido`;
- `RecorteDeEventoDeVidaEntregue`;
- `ProcessamentoDeRecorteDeEventoConfirmado`;
- `DivergenciaEntreFontesDeEventoIdentificada`;
- `SincronizacaoDeEventoDeVidaPendente`;
- `SincronizacaoDeEventoDeVidaConcluida`;
- `IntegracaoDeEventoDeVidaPausada`;
- `IntegracaoDeEventoDeVidaRetomada`;
- `IntegracaoDeEventoDeVidaRevogada`;
- `PropagacaoDeRevogacaoDeIntegracaoIniciada`;
- `PropagacaoDeRevogacaoDeIntegracaoConcluida`;
- `IntegracaoDeEventoDeVidaFalhou`;
- `IntegracaoDeEventoDeVidaDegradada`;
- `IntegracaoDeEventoDeVidaRecuperada`.

# 1358. Métricas funcionais das integrações

As integrações poderão ser avaliadas por:

- entradas recebidas;
- entradas rejeitadas;
- associações incorretas;
- duplicidades;
- autoridade insuficiente;
- eventos confirmados por fonte;
- eventos posteriormente contestados;
- divergências;
- recortes excessivos;
- tempo de propagação;
- falhas;
- recuperação;
- revogações pendentes;
- usos após revogação;
- exposição sensível;
- automações suspensas;
- explicações disponíveis.

As métricas deverão avaliar o sistema, não o participante.

# 1359. Integrações funcionalmente proibidas

Não deverão existir integrações que:

- confirmem evento pessoal por comportamento isolado;
- convertam compra em Evento de Vida;
- utilizem evento sensível para publicidade;
- compartilhem narrativa integral sem necessidade;
- criem objetivo pessoal ativo;
- imponham prioridade;
- tratem calendário como prova de ocorrência;
- transformem localização em mudança permanente;
- ampliem autoridade institucional;
- criem perfil de terceiros;
- ocultem divergências;
- mantenham uso após revogação;
- afirmem propagação concluída sem confirmação;
- transformem indisponibilidade em ausência de evento;
- utilizem vulnerabilidade para vantagem comercial.

# 1360. Critérios funcionais de aceite

As integrações serão consideradas adequadamente definidas quando:

1. possuírem finalidade explícita;
2. utilizarem dados minimizados;
3. preservarem titularidade;
4. diferenciarem titular, ator, fonte e afetado;
5. validarem identidade antes de efeitos materiais;
6. limitarem autoridade da fonte;
7. preservarem proveniência;
8. representarem qualidade e confiança;
9. rastrearem transformações;
10. separarem fato, sinal, hipótese e proposta;
11. preservarem temporalidades;
12. evitarem ciclos e duplicidades;
13. tratarem divergências sem sobrescrita;
14. integrarem Captura de Contexto sem ampliar sua autoridade;
15. preservarem a responsabilidade do Contexto Vivo;
16. preservarem a responsabilidade de Objetivos;
17. enviarem solicitações, não decisões, às capacidades consumidoras;
18. protegerem eventos sensíveis;
19. impedirem exploração comercial;
20. limitarem Guivos Intelligence a hipóteses e propostas;
21. preservarem a semântica funcional na Platform Layer;
22. controlarem serviços especializados;
23. restringirem fontes externas;
24. suportarem integrações temporárias;
25. permitirem pausa e revogação;
26. tratarem falhas com degradação controlada;
27. preservarem fatos retroativos;
28. protegerem informações de terceiros;
29. oferecerem explicabilidade e auditoria;
30. manterem o participante no controle.

# 1361. Regras fundamentais das integrações

1. Integração não transfere titularidade.
2. Acesso técnico não representa autoridade funcional.
3. Fonte somente afirma fatos sob seu escopo.
4. Sinal integrado não equivale a Evento de Vida confirmado.
5. Disponibilidade de dado não autoriza seu uso.
6. Finalidade deverá anteceder a coleta.
7. Recortes deverão ser mínimos.
8. Temporalidade da fonte e do fato deverão permanecer separadas.
9. Transformações deverão ser rastreáveis.
10. Integração não deverá fabricar precisão.
11. Divergências não deverão ser ocultadas.
12. Contexto Vivo governa o estado contextual.
13. Objetivos governa alterações na direção.
14. Próximos Passos governa ações.
15. Oportunidades Ativas governa relevância de oportunidades.
16. Intervenções Contextuais governa comunicações e ações.
17. Experiências permanece unidade distinta.
18. Evolução Contínua não deverá classificar o evento automaticamente.
19. Guivos Intelligence produz hipóteses e propostas.
20. Platform Layer não redefine semântica.
21. Organização não recebe jornada pessoal integral.
22. Compra não equivale a mudança humana.
23. Reserva não confirma mudança residencial.
24. Calendário não confirma ocorrência.
25. Localização não confirma permanência.
26. Atividade não confirma transformação.
27. Evento sensível não deverá alimentar publicidade.
28. Vulnerabilidade não deverá gerar vantagem comercial.
29. Pausa interrompe nova coleta.
30. Revogação interrompe novos usos.
31. Revogação não apaga automaticamente fatos históricos legítimos.
32. Falha deverá reduzir automação.
33. Ausência de dado não equivale a ausência de evento.
34. Informações de terceiros deverão ser minimizadas.
35. Métricas deverão avaliar a integração.
36. O participante deverá permanecer no controle.

# 1362. Continuidade normativa

`PAS-001-EV-INTEGRATION-001 1.0.0` deverá ser registrado como a **quinta extensão normativa da Capacidade 04 — Eventos de Vida**.

Ele deverá:

- consolidar as integrações funcionais da capacidade;
- preservar a autoridade das quatro extensões anteriores;
- manter a capacidade no estado `In progress`;
- elevar o progresso editorial de referência para `90%`;
- manter o `PAS-001 0.5.0` como especificação-base.

Com isso, ficam definidas as **integrações funcionais da Capacidade de Eventos de Vida** com as demais capacidades do Journey, Guivos Intelligence, Platform Layer, produtos e serviços especializados, organizações e fontes externas.

O próximo bloco deverá consolidar:

> **os KPIs, guardrails, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão e contrato final da Capacidade 04 — Eventos de Vida.**
