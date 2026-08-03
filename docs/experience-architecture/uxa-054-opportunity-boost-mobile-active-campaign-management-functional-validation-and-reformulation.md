---
id: UXA-054
title: Validação Funcional e Reformulação da Gestão Móvel da Campanha Ativa do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
parent: UXA-053
depends_on:
  - UXA-005
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - UXA-042
  - UXA-043
  - UXA-044
  - UXA-045
  - UXA-046
  - UXA-047
  - UXA-048
  - UXA-049
  - UXA-050
  - UXA-051
  - UXA-052
  - UXA-053
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.56
normative: false
---

# Validação Funcional e Reformulação da Gestão Móvel da Campanha Ativa do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente os seis wireframes móveis criados pela UXA-053 e registra as reformulações necessárias para que o anunciante compreenda programação, atividade, entrega reduzida, pausa, alteração material, cancelamento e estados finais sem interpretar ausência de medição como zero, limitação como atividade normal ou revisão como execução imediata.

A pergunta de validação é:

> **Em tela móvel, o anunciante reconhece o estado atual antes de agir, distingue entrega normal, limitada e interrompida, compreende orçamento e período, preserva versões e eventos anteriores e executa somente ações compatíveis com retomada ou encerramento?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova design visual final, acessibilidade técnica, responsividade implementada, algoritmo, cobrança, política final de frequência ou saldo, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. campanha programada;
2. campanha ativa;
3. campanha ativa com entrega reduzida;
4. campanha pausada;
5. alteração material;
6. cancelamento e estados finais;
7. continuidade da campanha, oportunidade, anunciante e versão;
8. orçamento total, reservado, utilizado e saldo;
9. limite diário, período e tempo restante;
10. ausência de medição e indicadores provisórios;
11. condição limitada e sua consequência;
12. pausa, horário de aplicação e registros tardios;
13. comparação de versões em tela estreita;
14. revisão de pausa e cancelamento proporcional;
15. preservação de eventos válidos, histórico e reconciliação;
16. linguagem clara e ações indisponíveis.

## 4. Lacunas identificadas

### 4.1 Zero antes do início parecia dado medido

A campanha programada apresentava `0 impressões`, `0 cliques` e `0 eventos operacionais` antes da abertura da janela de entrega.

Esse padrão poderia confundir ausência de medição com medição concluída sem eventos, contrariando a distinção já estabelecida entre zero, não disponível e não aplicável.

### 4.2 Gate limitado sem consequência de início

A campanha programada mostrava capacidade `ATENDIDA COM LIMITE`, mas não declarava se a campanha iniciaria normalmente, com entrega reduzida ou se ficaria bloqueada.

### 4.3 Estado ativo normal continha capacidade limitada

A tela ativa apresentava `capacidade: atendida com limite`, embora exista um estado específico para entrega reduzida.

A sobreposição enfraquecia a hierarquia entre atividade normal e atividade limitada.

### 4.4 Entrega reduzida sem contexto temporal completo

O estado limitado mostrava orçamento utilizado, saldo e limite diário, mas não apresentava:

- orçamento total;
- período completo;
- momento da verificação da causa;
- regra clara de atualização seguida de nova checagem.

### 4.5 Pausa sem horário e afirmação absoluta sobre registros

A tela pausada não informava quando a pausa havia sido aplicada e declarava ausência de qualquer novo registro posterior.

A formulação deveria distinguir novos eventos válidos de entrega de eventuais registros técnicos tardios sujeitos a tratamento separado.

### 4.6 Comparação lateral pouco legível

A versão aprovada e a versão candidata eram apresentadas lado a lado em duas colunas estreitas de 168 pixels.

Em dispositivo móvel, a estrutura reduzia legibilidade, dificultava leitura sequencial e enfraquecia a autoridade distinta das versões.

### 4.7 Ações pareciam execução imediata

Rótulos como `PAUSAR CAMPANHA`, `ALTERAR PROGRAMAÇÃO` e `PAUSAR EM VEZ DISSO` poderiam sugerir execução imediata, apesar de pausa, alteração e cancelamento exigirem revisão e confirmação próprias.

### 4.8 Identidade incompleta entre estados

Nem todas as telas apresentavam de forma equivalente a oportunidade e o anunciante junto do identificador e da versão.

## 5. Reformulação aprovada

### 5.1 Medição ainda não iniciada

A campanha programada passa a apresentar:

- `Medição ainda não iniciada`;
- impressões, cliques e eventos como não aplicáveis antes do início;
- explicação de que zero não representa ausência de janela de medição.

### 5.2 Consequência do gate limitado

A tela programada passa a declarar que, se o limite persistir na nova verificação, a campanha iniciará no estado de entrega reduzida.

Falha bloqueante continua impedindo ativação automática.

### 5.3 Estado ativo sem limitação corrente

A capacidade no estado ativo passa a ser apresentada como dentro da condição aprovada.

Se surgir restrição que reduza entrega, a interface deverá alterar explicitamente o estado para `ATIVA COM LIMITE`.

### 5.4 Limitação datada e completa

A tela de entrega reduzida passa a apresentar:

- oportunidade e versão;
- causa atual;
- horário da última verificação;
- orçamento total, utilizado e saldo;
- limite diário;
- período completo;
- condição de revisão da capacidade seguida de nova checagem;
- ausência de normalização automática.

### 5.5 Pausa com marco temporal e validade de eventos

A pausa passa a apresentar:

- causa;
- horário de aplicação;
- interrupção de novos eventos válidos de entrega;
- preservação de eventos válidos anteriores;
- tratamento separado para eventual registro técnico tardio;
- retomada bloqueada até resolução e nova verificação.

### 5.6 Comparação vertical de versões

A versão aprovada e a candidata passam a ser apresentadas em blocos verticais:

- versão aprovada em somente leitura;
- versão candidata explicitamente ainda não aprovada;
- campos alterados identificados por texto;
- orçamento utilizado e saldo próximos da decisão;
- histórico e eventos anteriores vinculados à aprovada;
- nenhuma retomada automática após envio ou descarte.

### 5.7 Revisão antes da execução

As ações passam a utilizar rótulos de revisão quando existe etapa posterior:

- `REVISAR PROGRAMAÇÃO`;
- `REVISAR PAUSA`;
- `REVISAR CAPACIDADE`;
- `REVISAR ENVIO PARA NOVA AVALIAÇÃO`;
- `REVISAR CANCELAMENTO`.

O botão destrutivo permanece indisponível até motivo e confirmações completas.

### 5.8 Identidade persistente

Os seis estados preservam:

- campanha `BST-2026-081`;
- oportunidade `Formação de jovens em tecnologia`;
- anunciante `Instituto Horizonte` quando necessário ao contexto;
- versão aprovada `v1`;
- versão candidata `v2` somente no fluxo de alteração material.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- campanha programada não equivale a campanha ativa;
- ausência de janela de medição não é exibida como zero;
- gate atendido com limite possui consequência explícita;
- falha bloqueante impede ativação automática;
- atividade normal não contém limitação corrente;
- entrega reduzida permanece ativa e possui causa datada;
- orçamento total, utilizado, saldo, limite e período são distinguíveis;
- limitação não acelera orçamento nem amplia período;
- pausa possui causa e horário;
- novos eventos válidos são interrompidos sem apagar eventos anteriores;
- registros técnicos tardios não são tratados como entrega válida;
- retomada permanece bloqueada até resolução e nova verificação;
- comparação de versões permanece legível em tela estreita;
- versão aprovada e candidata possuem autoridades distintas;
- envio para nova avaliação não equivale a aprovação;
- descarte da candidata não retoma automaticamente a aprovada;
- revisão de pausa não executa a pausa imediatamente;
- cancelamento exige motivo e confirmações inicialmente vazias;
- campanha permanece no estado anterior antes do gate completo;
- cancelamento preserva eventos válidos e histórico;
- saldo permanece candidato, não devolução confirmada;
- histórico, relatório agregado e reconciliação são superfícies distintas;
- nenhuma campanha, cobrança ou implementação real é criada.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-053-campaign-scheduled-mobile.svg`;
2. `uxa-053-campaign-active-mobile.svg`;
3. `uxa-053-campaign-limited-mobile.svg`;
4. `uxa-053-campaign-paused-mobile.svg`;
5. `uxa-053-campaign-material-change-mobile.svg`;
6. `uxa-053-campaign-closure-mobile.svg`.

Os artefatos permanecem em baixa fidelidade, com 390 × 844 pixels para aplicativo móvel.

## 8. Cobertura resultante

| Área | Computador | Aplicativo móvel |
|---|---|---|
| Configuração do anunciante | validada e reformulada | validada e reformulada |
| Cartão e explicação | validada e reformulada | validada e reformulada |
| Lista e Mapa | validada e reformulada | validada e reformulada |
| Gestão da campanha | validada e reformulada | validada e reformulada |
| Relatório agregado | validado e reformulado | validado e reformulado |

O Opportunity Boost passa a possuir 36 wireframes materializados e funcionalmente validados por seus respectivos pacotes.

A UXA-050 permanece como autoridade da validação transversal dos 25 artefatos examinados naquele incremento. Esta validação não amplia retroativamente seu escopo.

## 9. Proteções preservadas

- pagamento não compra posição orgânica, relevância, confiança, qualidade ou impacto;
- nenhum resultado é garantido;
- nenhuma entrega ocorre antes da programação válida;
- nenhuma entrega ocorre com informação material desatualizada;
- limite diário e período não são ampliados para compensar restrição;
- pausa não apaga eventos válidos;
- saldo não é apresentado como crédito, estorno ou devolução confirmados;
- cancelamento não apaga histórico;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado;
- relatório operacional não é relatório agregado;
- Engenharia de Produto permanece pausada.

## 10. Limites

Esta validação não cria:

- estados completos de erro técnico;
- experiência operacional de inventário insuficiente;
- experiência detalhada de preferência publicitária;
- nova validação transversal dos 36 wireframes;
- algoritmo de entrega ou leilão;
- política final de densidade ou frequência;
- política final de cancelamento, devolução, crédito ou disputa;
- design visual final;
- acessibilidade técnica;
- protótipo navegável;
- teste com usuários;
- checkout, faturamento, cobrança ou Engenharia de Produto.

## 11. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar estados de erro, inventário insuficiente e preferência publicitária;
2. validar transversalmente os 36 wireframes, se priorizado;
3. definir protocolo de protótipo de baixa ou média fidelidade;
4. preparar plano de teste com Organizações e Coletivos;
5. validar posteriormente estados, pausa, cancelamento, orçamento e controles com usuários reais.

Nenhum ato é iniciado automaticamente.
