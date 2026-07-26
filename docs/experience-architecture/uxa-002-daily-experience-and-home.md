---
id: UXA-002
title: Experiência Diária e Tela Hoje
status: active
version: 0.2.0
owner: Guivos Experience Architecture
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-001
  - PAS-001
  - PAS-001-CV-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
related:
  - UXA-020
normative: false
---

# UXA-002 — Experiência Diária e Tela Hoje

## 1. Pergunta central

> **O que justificará o retorno de um participante à Guivos hoje, sem transformar recorrência em dependência ou cobrança?**

A resposta proposta é uma superfície denominada **Hoje**, orientada por mudanças materiais, decisões reais e oportunidades temporalmente relevantes.

## 2. Decisão de experiência

`Hoje` será a porta de entrada recorrente da experiência pessoal **depois que a pessoa tiver iniciado sua jornada e confirmado uma compreensão inicial suficiente do Momento Atual**.

A primeira entrada pertence à **Página Inicial da Guivos e Início da Jornada (identificador UXA-020)**.

A Tela Hoje não será:

- a página institucional de apresentação da Guivos;
- a primeira coleta de contexto de uma pessoa sem jornada iniciada;
- feed social;
- catálogo infinito;
- painel de produtividade;
- mural publicitário;
- sequência obrigatória;
- resumo de tudo que existe na Guivos;
- mecanismo de culpa por ausência;
- substituto das telas especializadas.

Ela deverá responder:

> **O que mudou, o que merece minha atenção e quais possibilidades podem apoiar meu momento agora?**

### 2.1 Relação com a HOME da Guivos

A sequência funcional é:

```text
HOME da Guivos
→ relato voluntário do Momento Atual
→ compreensão inicial revisada e confirmada
→ Tela Hoje
```

Antes da confirmação suficiente, a pessoa poderá conhecer e explorar o ecossistema, mas a Guivos não deverá afirmar que uma oportunidade, solução ou Próximo Passo é relevante para seu momento.

Depois do início da jornada, a Tela Hoje poderá ser a entrada padrão após autenticação. A HOME continuará acessível como superfície institucional e de acesso às soluções do ecossistema.

## 3. Razões legítimas para entrar hoje

A tela poderá apresentar um item somente quando houver fundamento material, como:

1. decisão ou confirmação pendente;
2. Próximo Passo pronto, agendado ou bloqueado;
3. oportunidade relevante com janela temporal real;
4. alteração de preço, prazo, disponibilidade ou elegibilidade;
5. atividade de Coletivo próxima ou solicitada;
6. convite, inscrição, reserva ou processo em andamento;
7. mudança de contexto que afete a jornada;
8. experiência recente aguardando reconhecimento;
9. resultado ou evidência que mereça revisão;
10. alerta de privacidade, segurança ou conflito;
11. solicitação direta do participante;
12. resumo voluntariamente configurado.

Popularidade, patrocínio, comissão, meta comercial, tempo de tela ou ausência de acesso recente não constituem razões suficientes.

## 4. Estrutura inicial da tela Hoje

### 4.1 Cabeçalho contextual

Deverá apresentar:

- saudação neutra;
- contexto de atuação atual: Pessoa, Organização ou Coletivo;
- localização, somente quando autorizada e relevante;
- acesso à Central de Intervenções;
- seletor de contexto e papel;
- estado de privacidade ou modo discreto, quando aplicável.

### 4.2 Síntese do momento

Resumo curto e revisável, por exemplo:

> Hoje há um passo pronto para começar, uma oportunidade com inscrições até sexta-feira e uma atividade do seu coletivo amanhã.

Quando não houver itens materiais:

> Nada precisa da sua atenção agora. Sua jornada permanece disponível quando você quiser revisar ou explorar algo.

### 4.3 Bloco principal de atenção

Deverá mostrar no máximo um item principal por vez, escolhido por:

- prazo real;
- risco;
- confirmação necessária;
- dependência material;
- prioridade declarada;
- solicitação do participante;
- reversibilidade e impacto.

O item poderá ser:

- confirmar contexto;
- decidir sobre Próximo Passo;
- revisar alteração de oportunidade;
- responder convite;
- concluir processo;
- registrar resultado;
- revisar permissão.

### 4.4 Meu movimento atual

Resumo do Próximo Passo mais relevante, quando existir:

- formulação;
- objetivo relacionado;
- estado;
- janela temporal;
- bloqueio ou dependência;
- ação principal;
- alternativas.

A ausência de Próximo Passo não deverá gerar pressão para criar um.

### 4.5 Oportunidades para considerar

Recorte pequeno de oportunidades, limitado por utilidade e diversidade.

Cada cartão deverá apresentar:

- título;
- tipo;
- Organização, Coletivo ou fonte responsável;
- motivo resumido de relevância;
- preço ou gratuidade;
- custo total conhecido e condições;
- data, prazo ou disponibilidade;
- localização ou modalidade;
- elegibilidade resumida;
- relação comercial ou patrocínio;
- ação principal;
- acesso a `Por que estou vendo isto?`.

A tela não deverá exibir dezenas de oportunidades. O acesso ao catálogo completo pertence a `Explorar` e `Minhas Oportunidades`.

### 4.6 Coletivos e atividades

Poderá mostrar:

- próxima atividade de um Coletivo do qual participa;
- solicitação de entrada ou convite;
- mudança relevante em regras ou agenda;
- oportunidade criada pelo Coletivo;
- ação ou causa próxima;
- item que requer decisão de moderador ou líder.

Atualizações sociais sem finalidade não deverão ocupar a tela principal.

### 4.7 Perto de mim

Quando localização estiver autorizada, poderá apresentar:

- oportunidades próximas;
- eventos nas próximas horas ou dias;
- Organizações e Coletivos relacionados ao contexto;
- serviços ou experiências relevantes;
- alterações de local ou disponibilidade.

O bloco deverá permitir:

- abrir o mapa;
- ajustar raio;
- desativar localização;
- ocultar categorias;
- distinguir localização exata, aproximada e informada manualmente.

### 4.8 Registro do vivido

Após uma experiência ou ação, a tela poderá perguntar de forma não invasiva:

- você participou?;
- o que aconteceu?;
- deseja registrar um resultado?;
- algo mudou em seu contexto?;
- deseja manter isso privado?;
- este Próximo Passo continua fazendo sentido?

Ausência de resposta não equivale a ausência de experiência ou evolução.

## 5. Ordem de prioridade

A ordem funcional inicial será:

```text
segurança e direitos
→ prazo ou risco material
→ decisão solicitada pelo participante
→ compromisso ou processo em andamento
→ Próximo Passo ativo
→ oportunidade com janela real
→ atividade de Coletivo
→ revisão de contexto
→ exploração opcional
```

A ordem deverá ser explicável e ajustável. Um item patrocinado nunca poderá superar um item funcionalmente mais relevante.

## 6. Frequência e cadência

### Diário

Somente quando houver valor material ou configuração voluntária:

- resumo do dia;
- atividade próxima;
- janela de oportunidade;
- passo agendado;
- mudança relevante.

### Semanal

Poderá reunir:

- revisão de objetivos e passos;
- oportunidades salvas;
- atividades futuras;
- experiências recentes;
- alterações no contexto;
- recomendações de exploração.

### Eventual

Intervenções poderão ocorrer quando houver:

- evento de vida;
- mudança de preço ou disponibilidade;
- aprovação ou rejeição externa;
- convite;
- alerta de risco;
- solicitação do participante.

A Guivos não deverá enviar contato apenas para recuperar usuários inativos.

## 7. Controles de frequência

O participante deverá poder definir:

- resumo diário ligado ou desligado;
- dias e horários;
- categorias autorizadas;
- canais;
- prioridade de alertas;
- modo silencioso;
- períodos de pausa;
- notificações por Coletivo;
- notificações por oportunidade;
- uso de localização;
- agrupamento de mensagens;
- limites de frequência.

## 8. Controle de relevância

Em cada item, o participante poderá acessar ações como:

- `É relevante para mim`;
- `Não é relevante agora`;
- `Mostrar menos como isto`;
- `Ocultar esta categoria`;
- `Não usar esta informação`;
- `Corrigir meu contexto`;
- `Salvar para depois`;
- `Por que estou vendo isto?`;
- `Por que agora?`;
- `Contestação ou denúncia`.

A Guivos deverá distinguir preferência declarada, comportamento observado e inferência técnica.

## 9. Estados vazios

Estados vazios deverão oferecer calma e orientação, não preenchimento artificial.

Exemplos:

- `Nada precisa da sua atenção agora.`
- `Nenhuma oportunidade compatível foi identificada neste momento.`
- `Você não possui atividades de coletivos próximas.`
- `Nenhum passo está ativo. Você pode revisar sua jornada quando quiser.`

Ações opcionais poderão incluir:

- revisar contexto;
- explorar oportunidades;
- consultar o mapa;
- visitar um Coletivo;
- registrar uma mudança;
- permanecer sem ação.

## 10. Hipótese de retorno diário

A hipótese inicial é:

> Participantes retornarão com frequência quando a Guivos reduzir esforço real de decisão e coordenação, mostrando de forma confiável o que mudou, o que precisa de atenção e quais oportunidades possuem utilidade temporal — não porque a plataforma cria estímulos artificiais.

Essa hipótese deverá ser validada posteriormente por protótipos e pesquisa comportamental.

## 11. Métricas futuras permitidas

Poderão ser estudadas:

- itens materiais compreendidos;
- decisões concluídas com clareza;
- oportunidades consideradas e justificadas;
- processos iniciados e concluídos;
- controles de relevância utilizados;
- notificações silenciadas;
- tempo até uma ação no mundo real;
- correções de contexto;
- retornos voluntários após mudança material.

Não deverão ser metas isoladas:

- tempo de tela;
- número de sessões;
- sequência de dias;
- quantidade de cliques;
- rolagem;
- notificações abertas;
- volume de oportunidades exibidas.