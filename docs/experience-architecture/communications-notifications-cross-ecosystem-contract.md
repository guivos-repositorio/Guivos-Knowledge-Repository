---
id: GKR-UX-COMMUNICATIONS-NOTIFICATIONS-001
title: Comunicações e Notificações — Contrato Transversal do Ecossistema
status: draft
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: true
maturity: communications_notifications_contract_candidate
depends_on:
  - GKR-UX-PARTICIPANT-RELATIONSHIPS-INTERACTIONS-001
  - GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001
  - GKR-UX-ORGCOL-JOURNEY-ORCHESTRATION-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-PLANS-PERSON-001
---

# Comunicações e Notificações — Contrato Transversal do Ecossistema

## 1. Finalidade

Este documento governa quando eventos do ecossistema devem produzir consciência, atualização ou ação para participantes autorizados.

Ele separa evento, atualização dentro do produto, comunicação oficial, alerta e canal externo.

## 2. Modelo

```text
EVENTO REAL
→ OBJETO / CONTEXTO
→ DESTINATÁRIO AUTORIZADO
→ RECORTE DE DADOS
→ MATERIALIDADE
→ EXIGE AÇÃO?
→ CONTINUIDADE LEGÍTIMA
→ APRESENTAÇÃO NO PRODUTO
→ ALERTA QUANDO CONTRATADO
→ CANAL EXTERNO SOMENTE QUANDO AUTORIZADO
```

## 3. Distinções

```text
EVENTO
≠ NOTIFICAÇÃO

ATUALIZAÇÃO
≠ ALERTA

COMUNICAÇÃO OFICIAL
≠ MARKETING

ALERTA PERSONALIZADO
≠ CORRESPONDÊNCIA PERSONALIZADA

PRIORIDADE
≠ URGÊNCIA ARTIFICIAL

CANAL EXTERNO
≠ CONSENTIMENTO AUTOMÁTICO
```

## 4. Eventos materiais correntes

Podem exigir atualização/consciência, conforme objeto e autoridade:

- solicitação de participação recebida;
- pedido de informação adicional;
- resposta do solicitante;
- aprovação ou recusa;
- mudança material de vínculo;
- papel/responsabilidade que dependa de ação legítima;
- comunicação oficial do Coletivo;
- atividade/consulta/decisão que exija consciência do participante;
- proposta O↔C recebida/alterada;
- resposta, contestação, pausa, revisão ou encerramento O↔C;
- manifestação/inscrição interna em oportunidade;
- atualização material ORG-008↔PER-204;
- prazo real;
- falha ou estado indeterminado que exija retomada;
- confirmação material de plano/cobrança;
- capacidade/cota atingida quando afeta ação pretendida;
- oportunidade legitimamente relacionada à Pessoa quando houver contrato de alerta aplicável.

## 5. Destinatário

Um evento somente pode alcançar quem possua relação, finalidade e autoridade suficientes.

```text
EXISTIR NO MESMO COLETIVO
≠ RECEBER TODO EVENTO

SER ADMINISTRADOR
≠ RECEBER TODO DADO

PUBLICAR OPORTUNIDADE
≠ CONHECER TODA PESSOA RELACIONADA

SER CORRESPONDÊNCIA
≠ AUTORIZAR EXPOSIÇÃO DA RAZÃO PRIVADA
```

## 6. Central de Atualizações e superfícies contextuais

Quando existir superfície canônica adequada, a atualização deve continuar para ela ou para o objeto que originou o evento.

PER-107 permanece Central de Atualizações da Pessoa no contexto governado da participação em Coletivos; este documento não transforma PER-107 automaticamente em caixa universal de todas as notificações do ecossistema.

Uma futura unificação exige adjudicação própria.

## 7. Oportunidades e alertas da Pessoa

Planos correntes declaram:

- Free: alertas gerais;
- Plus: alertas personalizados;
- Pro: alertas personalizados e prioritários.

A execução deve preservar:

```text
OPORTUNIDADE PÚBLICA
→ PODE SER DESCOBERTA SEM ALERTA

CORRESPONDÊNCIA PERSONALIZADA
→ RELAÇÃO EXPLICÁVEL COM CONTEXTO AUTORIZADO

ALERTA PERSONALIZADO
→ EVENTO/ATUALIZAÇÃO BASEADO EM CRITÉRIO AUTORIZADO
→ NÃO REVELA CONTEXTO PRIVADO A PUBLICADOR

ALERTA PRIORITÁRIO
→ NÃO AUTORIZA RANKING HUMANO
→ NÃO AUTORIZA FALSA URGÊNCIA
→ REGRA DE PRIORIZAÇÃO AINDA EXIGE CONTRATO EXECUTÁVEL
```

Até existir regra executável de disparo, frequência, deduplicação e preferência, Design/IA não deve inventar comportamento automático.

### 7.1 Adjudicação dos níveis Free, Plus e Pro

A baseline comercial prova a existência das categorias **geral**, **personalizado** e **prioritário**, mas não prova seus algoritmos, cadência ou canais.

```text
FREE — ALERTA GERAL
→ CATEGORIA COMERCIAL EXISTENTE
→ REGRA EXECUTÁVEL DE DISPARO NÃO ADJUDICADA

PLUS — ALERTA PERSONALIZADO
→ CATEGORIA COMERCIAL EXISTENTE
→ DEPENDE DE CONTEXTO AUTORIZADO E EXPLICABILIDADE
→ REGRA EXECUTÁVEL DE DISPARO NÃO ADJUDICADA

PRO — ALERTA PERSONALIZADO E PRIORITÁRIO
→ CATEGORIA COMERCIAL EXISTENTE
→ PRIORIDADE NÃO SIGNIFICA URGÊNCIA ARTIFICIAL
→ REGRA EXECUTÁVEL DE PRIORIZAÇÃO NÃO ADJUDICADA
```

Nenhum plano autoriza inferir maior exposição de dados da Pessoa, acesso adicional de publicadores, frequência mais agressiva ou interrupção artificial.

### 7.2 Limite de prototipação

Enquanto as regras executáveis permanecerem abertas, protótipos podem representar **estados conceituais** necessários para explicar a diferenciação comercial, mas não devem simular como canônico:

- momento exato de disparo;
- quantidade/frequência;
- algoritmo de correspondência;
- score ou ranking;
- ordem de prioridade;
- canal externo;
- preferência padrão;
- escalonamento ou insistência.

Uma representação conceitual não promove o contrato a implementação.

## 8. Planos e upgrade

Quando um alerta personalizado ou prioritário for capacidade de plano superior, ele pode ser descobrível segundo a Orquestração.

O upgrade pode aparecer quando a Pessoa demonstra necessidade real da capacidade ou consulta Planos. Não deve interromper informação material já devida no plano atual.

## 9. Comunicação Coletivo → Pessoa

COL-005 governa comunicação oficial. Este contrato não substitui essa superfície.

Comunicação destinada a participantes deve respeitar audiência, vínculo, finalidade, proteção e estado corrente. Pertencimento não equivale a consentimento universal para marketing ou canais externos.

## 10. Comunicação Pessoa → Coletivo

Solicitações, respostas e ações da Pessoa seguem os objetos e transições existentes. Não presumir mensagem livre ao Coletivo fora das responsabilidades governadas.

### Iniciativa Coletivo → Pessoa

O estado corrente não contrata convite genérico de adesão iniciado pelo Coletivo. Consequentemente, este contrato também não cria notificação de convite, lembrete de convite, expiração de convite ou campanha de recrutamento.

Se essa capacidade for futuramente adjudicada, comunicação e notificação somente poderão ser definidas depois que o objeto relacional, o aceite da Pessoa e os dados autorizados estiverem contratados.

## 11. Organização ↔ Pessoa

No processo interno de oportunidade, atualizações materiais seguem PER-204↔ORG-008. A Organização não recebe razões privadas de correspondência/relevância; a Pessoa não recebe estados internos institucionais protegidos.

## 12. Organização ↔ Coletivo

Eventos bilaterais devem preservar o mesmo objeto O↔C, destinatário responsável, escopo e estado. Não duplicar relação para criar uma notificação.

## 13. Pessoa ↔ Pessoa

A relação social bilateral autônoma Pessoa↔Pessoa não está adjudicada. Co-presença em objeto compartilhado não cria canal P↔P.

Eventos de um objeto compartilhado podem gerar atualizações para cada Pessoa quando o contrato daquele objeto justificar, mas a entrega continua sendo **objeto→Pessoa**, não uma mensagem privada Pessoa→Pessoa por inferência.

```text
PESSOA A AGE EM OBJETO COMPARTILHADO
→ OBJETO MUDA
→ PESSOA B PODE RECEBER ATUALIZAÇÃO SE FOR DESTINATÁRIA LEGÍTIMA

ISSO
≠ DM PESSOA A → PESSOA B
```

## 14. Canais

### 14.1 Adjudicação corrente

Nenhum canal externo é definido por inferência.

A auditoria documental corrente não encontrou autoridade suficiente para tornar **push, e-mail, SMS, WhatsApp ou mensagem direta** canais canônicos de entrega de alertas. A existência técnica futura de um canal também não estabelece consentimento, preferência ou finalidade.

```text
ALERTA CONTRATADO
≠ CANAL EXTERNO CONTRATADO

CANAL TECNICAMENTE DISPONÍVEL
≠ CANAL AUTORIZADO PARA A PESSOA

DADO DE CONTATO EXISTENTE
≠ CONSENTIMENTO DE ENTREGA
```

Até autoridade específica, não presumir:

- push;
- e-mail;
- SMS;
- WhatsApp;
- mensagem direta;
- frequência;
- digest;
- lembrete automático;
- escalonamento;
- horário silencioso;
- preferência padrão;
- SLA;
- confirmação de leitura.

O contrato pode evoluir para governar canais sem exigir nova superfície quando a evidência justificar.

## 15. Deduplicação, leitura e validade

A futura execução deve distinguir evento de entrega. Um mesmo evento não deve produzir múltiplos efeitos materiais por retry.

Estado lido/não lido, expiração, agrupamento, digest e retenção permanecem não adjudicados até regra própria.

### 15.1 Garantias mínimas sem inventar mecanismo

Mesmo sem mecanismo executável adjudicado, uma futura implementação deverá preservar:

- idempotência material: retry não pode multiplicar consequência;
- rastreabilidade do evento de origem;
- destinatário autorizado no momento relevante;
- minimização do conteúdo entregue;
- continuidade para objeto/superfície legítimos;
- ausência de falsa urgência;
- ausência de inferência de leitura, ciência ou aceite.

Estas garantias não definem UI, armazenamento, retenção, badge, contador ou fila.

## 16. Privacidade

A notificação deve conter somente o mínimo necessário. Conteúdo sensível ou protegido pode exigir mensagem neutra que leve à superfície autenticada em vez de expor detalhes no canal.

## 17. Critérios de aceite

Uma futura materialização deve permitir responder:

1. qual evento ocorreu;
2. quem pode receber;
3. por que recebe;
4. qual dado pode aparecer;
5. se exige ação;
6. qual continuidade legítima;
7. se o plano altera alerta;
8. se há preferência/consentimento aplicável;
9. como evitar duplicação;
10. o que permanece protegido.

## 18. Estado

```text
COMMUNICATIONS / NOTIFICATIONS CONTRACT
→ CANDIDATE

EVENT TAXONOMY
→ BASELINE DE MATERIALIDADE DEFINIDA

EXTERNAL CHANNELS
→ AUDITED / NO CANONICAL CHANNEL ADJUDICATED

DELIVERY FREQUENCY / DEDUP UI / PREFERENCES / READ STATE / DIGEST / RETENTION
→ NOT ADJUDICATED

PERSON FREE/PLUS/PRO ALERT CATEGORIES
→ COMMERCIALLY DECLARED

PERSON FREE/PLUS/PRO ALERT EXECUTION
→ NOT ADJUDICATED

NEW SURFACE IDS
→ NONE

NEW TRANSITION IDS
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```
