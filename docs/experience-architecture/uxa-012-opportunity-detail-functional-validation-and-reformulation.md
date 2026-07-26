---
id: UXA-012
title: Validação Funcional e Reformulação do Detalhe de Oportunidade
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-004
  - UXA-005
  - UXA-007
  - UXA-009
  - UXA-011
  - GEB-P01-F01
  - GEB-P01-F02
  - GEB-P01-F03
  - GEB-P01-F04
  - GEB-P01-F05
  - GEB-P01-F06
related:
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
normative: false
---

# Validação Funcional e Reformulação do Detalhe de Oportunidade (identificador UXA-012)

## 1. Finalidade

Este documento registra a primeira validação funcional do **Detalhe de Oportunidade** e as decisões aplicadas ao seu wireframe de baixa fidelidade.

A validação responde:

> Como apresentar uma oportunidade como possibilidade de evolução, e não como produto isolado ou página genérica de conversão, preservando clareza comercial, autonomia e capacidade de ação?

## 2. Diagnóstico do wireframe anterior

O wireframe anterior já apresentava preço, custo total, validade, relevância, elegibilidade, Organização responsável e transparência comercial.

Entretanto, sua hierarquia iniciava por identidade e preço e terminava com uma ação universal de inscrição. Essa estrutura poderia ser interpretada como página comercial convencional, mesmo contendo informações corretas.

Os principais riscos identificados foram:

1. preço visualmente anterior ao significado da oportunidade na jornada;
2. linguagem de relevância correta, mas ainda separada da identidade institucional da Guivos;
3. ação `Iniciar inscrição` tratada como padrão para tipos diferentes de oportunidade;
4. `Mapa` apresentado como ação persistente mesmo quando a oportunidade era online;
5. ausência de mensagem explícita de que a oportunidade é uma possibilidade, não uma recomendação definitiva;
6. pouca conexão entre objetivo, Próximo Passo, experiência esperada e decisão;
7. risco de a tela parecer pertencente a qualquer marketplace, plataforma educacional ou comparador.

## 3. Decisão estrutural

A hierarquia reformulada será:

```text
identidade e origem
→ como pode apoiar sua jornada
→ investimento e condições
→ o que precisa saber antes de decidir
→ condições para participar
→ quem oferece
→ relação comercial com a Guivos
→ ações contextuais
```

A oportunidade permanece identificada imediatamente. O preço continua visível no primeiro percurso de leitura, mas deixa de definir o significado inicial da superfície.

## 4. Aplicação do gate de alinhamento à Fundação

### 4.1 Essência da Guivos

A superfície deverá reduzir a distância entre o Momento Atual e um Próximo Passo possível. A oportunidade será apresentada como meio para apoiar a jornada, não como finalidade própria.

### 4.2 Propósito

A tela deverá demonstrar como a oportunidade pode ampliar possibilidades concretas de evolução para o momento atual, sem coercão ou promessa de transformação.

### 4.3 Missão Operacional

A interface deverá ajudar o participante a compreender se essa possibilidade contribui para um Próximo Passo relevante e o que seria necessário para agir.

### 4.4 Visão de Longo Prazo

A superfície deverá funcionar para diferentes tipos de oportunidade, países, culturas, modelos comerciais e participantes. Ela não poderá reduzir a Guivos a marketplace, curso, vaga, viagem ou produto isolado.

### 4.5 Constituição da Guivos

A reformulação preserva:

- evolução como finalidade;
- oportunidade como meio;
- decisão final com o participante;
- tecnologia e inteligência como instrumentos;
- natureza ecossistêmica;
- contexto como base da relevância;
- conhecimento como patrimônio;
- simplicidade estrutural.

### 4.6 Princípios Permanentes

A tela priorizará Próximo Passo, relevância contextual, autonomia, experiência vivida, simplicidade, transparência, validade global e ação no mundo real.

## 5. Identidade e origem

O topo deverá apresentar:

- tipo e modalidade;
- disponibilidade;
- título;
- Organização ou Coletivo responsável;
- origem funcional da oportunidade;
- acesso a ações de ocultar, contestar ou denunciar.

O título contextual preferencial será:

> Possibilidade para sua jornada

Esse título não substitui a classificação técnica de Oportunidade. Ele orienta a leitura sem transformar a oportunidade em recomendação definitiva.

## 6. Como pode apoiar sua jornada

Este bloco passará a anteceder o preço.

Deverá explicar, com base autorizada:

- objetivo relacionado;
- Próximo Passo relacionado;
- contexto ou preferência declarada;
- razão temporal para aparecer agora;
- experiência ou resultado esperado, sem garantia;
- fonte da relação identificada.

Exemplo:

> Esta oportunidade pode apoiar seu próximo passo de desenvolver comunicação profissional em inglês. Ela apareceu agora porque as inscrições encerram em 31/07 e você informou preferência por atividades online à noite.

A tela deverá declarar:

> Esta é uma possibilidade para você considerar. A decisão continua sendo sua.

Controles:

- `Por que apareceu agora?`;
- `Corrigir esta relação`;
- `Não faz sentido para mim`;
- `Não usar esta informação`;
- `Mostrar menos oportunidades como esta`.

## 7. Investimento e condições

O bloco deverá apresentar:

- preço principal;
- custo total conhecido ou estimado;
- parcelas ou recorrência;
- custos obrigatórios adicionais;
- validade do preço;
- prazo de inscrição;
- política de cancelamento;
- reembolso, quando aplicável;
- última confirmação da fonte.

Formulação de referência:

> R$ 79,90 por mês, em seis parcelas. Custo total estimado: R$ 479,40. Valor válido para novas inscrições até 31/07/2026.

O preço não poderá utilizar destaque promocional maior do que a clareza sobre custo total e condições.

## 8. O que precisa saber antes de decidir

Este bloco reunirá:

- disponibilidade;
- modalidade;
- data e horário;
- local ou abrangência;
- duração;
- acessibilidade;
- compromissos exigidos;
- requisitos principais;
- cancelamento;
- riscos ou limitações materiais;
- última atualização.

O conteúdo deverá permitir uma decisão inicial sem exigir leitura integral de políticas extensas.

## 9. Condições para participar

O título de leitura será **Condições para participar**. O estado técnico de elegibilidade permanecerá visível e explicável.

Exemplo:

> Sua situação: possivelmente elegível.

A tela deverá explicar:

- requisito utilizado na avaliação;
- informação ainda não verificada;
- quem possui autoridade para decidir;
- próximos passos de verificação;
- possibilidade de corrigir ou contestar dados.

A Guivos não poderá apresentar probabilidade como aprovação ou utilizar elegibilidade estimada para pressionar conversão.

## 10. Quem oferece

O bloco deverá apresentar:

- nome e identidade da Organização ou Coletivo;
- estado de verificação;
- unidade responsável;
- propósito ou atuação relevante;
- canal de suporte;
- histórico ou atualização material;
- perfil institucional;
- outras oportunidades;
- contestação ou denúncia.

Verificação institucional não equivale a garantia de resultado, qualidade ou adequação individual.

## 11. Relação comercial com a Guivos

O título será explícito: **Relação comercial com a Guivos**.

A tela deverá informar, quando aplicável:

- comissão;
- afiliação;
- patrocínio;
- exclusividade;
- promoção paga;
- participação na receita;
- financiamento;
- outra relação material.

Formulação de referência:

> A Guivos poderá receber comissão se a contratação for concluída. Essa relação não aumentou a relevância funcional desta oportunidade.

Publicidade e patrocínio não poderão utilizar a presença companheira para disfarçar intenção comercial.

## 12. Ações contextuais

Não haverá uma ação principal universal para todas as oportunidades.

A ação dependerá do tipo e do estado real:

- `Ver como participar`;
- `Iniciar inscrição`;
- `Solicitar contato`;
- `Reservar`;
- `Entrar na lista de espera`;
- `Acompanhar abertura`;
- `Abrir no mapa`, quando localização for material;
- `Conhecer a Organização`;
- `Salvar para considerar`;
- `Comparar`.

Para o wireframe de referência, a ação principal passa a ser:

> Ver como participar

Essa ação deverá abrir uma etapa intermediária com executor, dados compartilhados, destinatário, custos, compromissos e reversibilidade antes do início do processo.

Ações secundárias persistentes:

- salvar para considerar;
- comparar.

`Mapa` deixará de ser persistente quando a localização não for material.

## 13. Decisões aplicadas

1. A relação com a jornada passa a anteceder preço e conversão.
2. O preço permanece visível, mas é apresentado como investimento e condição, não como argumento promocional.
3. A oportunidade é declarada como possibilidade, não recomendação definitiva.
4. O motivo temporal passa a utilizar `Por que apareceu agora?`.
5. A elegibilidade passa a ser lida como `Condições para participar`, mantendo o estado técnico explicável.
6. `Organização responsável` passa a ser `Quem oferece` na leitura principal.
7. `Transparência comercial` passa a ser `Relação comercial com a Guivos`.
8. A ação principal deixa de ser universal e passa a depender do estado da oportunidade.
9. `Mapa` deixa de ser ação persistente em oportunidades sem localização material.
10. Salvar e comparar permanecem alternativas legítimas sem pressão.
11. O gate de alinhamento à Fundação passa a integrar os critérios de aceite.

## 14. Critérios de aceite

A superfície poderá avançar quando:

- demonstrar aderência à Essência, Propósito, Missão, Visão, Constituição e Princípios Permanentes;
- explicar a relação da oportunidade com a jornada antes de enfatizar conversão;
- diferenciar possibilidade de recomendação definitiva;
- preservar preço, custo total, validade e condições de forma clara;
- distinguir prazo de inscrição, validade do preço e duração;
- explicar por que a oportunidade apareceu agora;
- permitir correção, contestação, recusa, salvamento e comparação;
- não apresentar elegibilidade estimada como aprovação;
- mostrar fonte, Organização responsável e relação comercial;
- adaptar a ação principal ao tipo e ao estado real;
- manter publicidade subordinada à relevância funcional;
- não parecer uma página genérica de venda;
- favorecer compreensão e ação no mundo real sem pressão.

## 15. Estados ainda pendentes

- oportunidade gratuita com custos externos;
- preço variável ou sob consulta;
- lista de espera;
- abertura futura;
- elegibilidade insuficiente;
- risco elevado;
- oportunidade patrocinada;
- oportunidade criada por Coletivo;
- oportunidade presencial com localização protegida;
- oportunidade expirada;
- informação contestada;
- falha de sincronização com fonte externa;
- baixa conectividade;
- texto ampliado e leitor de tela.

## 16. Limites

Esta validação:

- não cria design visual definitivo;
- não define componentes técnicos;
- não cria protótipo navegável;
- não executa teste de usabilidade;
- não valida preços ou Organizações reais;
- não autoriza desenvolvimento;
- não altera a pausa dos Resultados Empresariais;
- não antecipa a decisão sobre Capacidade de Reinvestimento Responsável.