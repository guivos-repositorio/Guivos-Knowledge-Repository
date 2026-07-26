---
id: UXA-007
title: Wireframe de Baixa Fidelidade do Detalhe de Oportunidade
status: draft
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-005
related:
  - UXA-002
  - UXA-004
  - UXA-006
  - UXA-009
  - UXA-011
  - UXA-012
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
normative: false
---

# Wireframe de Baixa Fidelidade do Detalhe de Oportunidade (identificador UXA-007)

O identificador técnico `UXA-007` serve somente para rastreabilidade. O nome de leitura desta superfície é **Detalhe de Oportunidade**.

Esta versão incorpora a **Presença Companheira e Coerência de Posicionamento da Guivos** e a **Validação Funcional e Reformulação do Detalhe de Oportunidade**.

## 1. Pergunta da superfície

> **Como a Guivos compreende meu momento, qual avanço já reconhece, por que esta oportunidade pode fazer sentido agora e o que preciso saber antes de decidir?**

A superfície deverá apresentar a oportunidade como meio para um possível Próximo Passo. Ela não deverá parecer página genérica de venda, recomendação definitiva ou etapa obrigatória de evolução.

## 2. Wireframe reformulado

![Wireframe móvel reformulado do Detalhe de Oportunidade](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg)

[Visualizar o arquivo gráfico vetorial escalável](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg)

O wireframe permanece monocromático e estrutural. Ele não define identidade visual, componentes técnicos ou comportamento implementado.

## 3. Hierarquia aprovada

| Ordem | Bloco | Responsabilidade |
|---:|---|---|
| 1 | identidade e origem | identificar a possibilidade, seu tipo, estado e responsável |
| 2 | como a Guivos compreende seu momento | mostrar informações confirmadas, observadas, externas, inferidas e ainda desconhecidas |
| 3 | avanço reconhecido | demonstrar mudanças já percebidas sem inventar progresso |
| 4 | por que este Próximo Passo faz sentido | explicar a cadeia entre momento, objetivo, lacuna, possibilidade e contribuição esperada |
| 5 | investimento e condições | mostrar preço, custo total, validade, prazo e cancelamento |
| 6 | antes de decidir | reunir disponibilidade, modalidade, horário, acessibilidade e compromissos |
| 7 | condições para participar | explicar elegibilidade, autoridade decisória e verificações |
| 8 | quem oferece | permitir avaliar a Organização ou o Coletivo responsável |
| 9 | relação comercial com a Guivos | revelar comissão, patrocínio ou outra relação material |
| 10 | ações contextuais | permitir agir, salvar ou comparar sem ocultar alternativas |

## 4. Gate de alinhamento à Fundação da Guivos

A superfície somente poderá avançar quando demonstrar:

- **Essência:** reduz a distância entre Momento Atual e Próximo Passo;
- **Propósito:** amplia possibilidades concretas de evolução;
- **Missão Operacional:** ajuda a compreender ou realizar um próximo movimento relevante;
- **Visão de Longo Prazo:** funciona como parte de um ecossistema global, não como produto isolado;
- **Constituição:** preserva evolução como finalidade, oportunidade como meio, autonomia e relevância contextual;
- **Princípios Permanentes:** prioriza Próximo Passo, contexto, experiência vivida, simplicidade e ação real.

Preço, conversão ou relação comercial não poderão ocupar uma posição que descaracterize esses fundamentos.

## 5. Identidade e origem

O topo deverá apresentar:

- indicação `Possibilidade para sua jornada`;
- tipo da oportunidade;
- modalidade;
- estado de disponibilidade;
- título;
- Organização ou Coletivo responsável;
- origem funcional;
- ações de ocultar, contestar ou denunciar.

A palavra `possibilidade` orienta a leitura, mas não substitui a entidade canônica Oportunidade.

## 6. Como a Guivos compreende seu momento

O bloco deverá apresentar uma leitura verificável e corrigível do momento atual.

Deverá distinguir:

- objetivo confirmado pelo participante;
- Próximo Passo atual;
- experiência ou etapa já registrada;
- preferência declarada;
- limitação ou dúvida ainda existente;
- informação proveniente de fonte autorizada;
- inferência da Guivos;
- informação que ainda não está disponível.

Exemplo:

> A Guivos compreende que você deseja desenvolver comunicação profissional em inglês, já concluiu o nível básico e prefere atividades online à noite. Ainda não sabemos se você possui disponibilidade para aulas ao vivo duas vezes por semana.

Controles mínimos:

- `Ver informações utilizadas`;
- `Corrigir meu momento`;
- `Meu momento mudou`;
- `Não usar esta informação`.

Quando a base for insuficiente, a tela deverá declarar que não possui informação suficiente, em vez de simular compreensão.

## 7. Avanço reconhecido

O avanço deverá ser percebido por mudança relevante na jornada, e não por percentual genérico, pontos, sequência de dias ou volume de tarefas.

Evidências possíveis:

- passo concreto concluído;
- capacidade desenvolvida;
- barreira removida;
- experiência vivida;
- decisão consciente registrada;
- mudança de contexto;
- confirmação do próprio participante.

Exemplo:

> Avanço reconhecido: você concluiu o nível básico e registrou que já consegue compreender textos simples. O desafio atual informado é utilizar o idioma em situações profissionais.

A evidência deverá informar origem, data e possibilidade de correção. Quando não houver base suficiente, a interface deverá dizer que ainda não há evidência para afirmar avanço.

## 8. Por que este Próximo Passo faz sentido

A justificativa deverá conectar:

```text
momento atual confirmado
→ avanço reconhecido
→ objetivo autorizado
→ lacuna ou possibilidade atual
→ Próximo Passo
→ contribuição possível da oportunidade
```

Exemplo:

> Este Próximo Passo faz sentido porque você já concluiu o nível básico, deseja utilizar o inglês no trabalho e informou que a prática profissional ainda é uma dificuldade. O curso pode oferecer situações de comunicação aplicada, mas não é o único caminho possível.

A tela deverá apresentar:

- informações utilizadas;
- distinção entre fato e inferência;
- razão temporal;
- contribuição possível;
- incertezas;
- alternativas disponíveis;
- controles para corrigir ou rejeitar a relação.

Respostas possíveis:

- `Faz sentido para mim`;
- `Faz sentido parcialmente`;
- `Não faz sentido para mim`;
- `Quero outro caminho`.

A concordância não cria obrigação de agir.

## 9. Investimento e condições

O bloco deverá apresentar:

- preço principal;
- custo total conhecido ou estimado;
- parcelas ou recorrência;
- custos obrigatórios adicionais;
- validade do preço;
- prazo de inscrição;
- cancelamento;
- reembolso, quando aplicável;
- última confirmação da fonte.

Exemplo:

> R$ 79,90 por mês, em seis parcelas. Custo total estimado: R$ 479,40. Valor válido para novas inscrições até 31/07/2026.

### 9.1 Validade do preço

Validade do preço é a data ou período até o qual a Organização declara que o valor permanece vigente para nova inscrição, contratação ou compra.

Ela não representa:

- duração do serviço;
- vencimento da parcela;
- prazo de inscrição;
- período do contrato;
- prazo de cancelamento;
- prazo de reembolso.

Após a validade, o preço deverá ser confirmado novamente. Mudança durante processo iniciado exigirá confirmação consciente.

Regras:

- `grátis` não poderá ocultar custos obrigatórios;
- `a partir de` deverá indicar variáveis de preço;
- preço sob consulta limitará comparação e apresentação;
- destaque promocional não poderá superar custo total e condições.

## 10. O que precisa saber antes de decidir

O primeiro nível deverá mostrar:

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

Políticas extensas permanecerão em detalhamento progressivo.

## 11. Condições para participar

O título de leitura será **Condições para participar**. O estado técnico de elegibilidade permanecerá explícito.

Estados possíveis:

- não avaliada;
- possivelmente elegível;
- elegível;
- elegível com condição;
- exige verificação;
- possivelmente não elegível;
- não elegível;
- contestada.

A tela deverá explicar:

- requisito considerado;
- informação ainda não verificada;
- autoridade responsável pela decisão;
- passo de verificação;
- correção ou contestação disponível.

A Guivos não poderá apresentar probabilidade como aprovação.

## 12. Quem oferece

O bloco deverá permitir verificar:

- nome e identidade;
- estado de verificação;
- unidade responsável;
- propósito ou atuação relevante;
- canal de suporte;
- atualização e histórico materiais;
- perfil institucional;
- outras oportunidades;
- contestação ou denúncia.

Verificação institucional não representa garantia de resultado ou adequação individual.

## 13. Relação comercial com a Guivos

A tela deverá declarar, quando aplicável:

- comissão;
- afiliação;
- patrocínio;
- exclusividade;
- promoção paga;
- participação da Guivos na receita;
- financiamento;
- relação indireta relevante.

Formulação de referência:

> A Guivos poderá receber comissão se a contratação for concluída. Essa relação não aumentou a relevância funcional desta oportunidade.

A presença companheira não poderá ser utilizada para disfarçar publicidade.

## 14. Ações contextuais

Não haverá uma ação principal universal.

A ação poderá ser:

- `Ver como participar`;
- `Iniciar inscrição`;
- `Solicitar contato`;
- `Reservar`;
- `Entrar na lista de espera`;
- `Acompanhar abertura`;
- `Abrir no mapa`, quando localização for material;
- `Conhecer a Organização`.

No wireframe de referência, a ação principal será:

> Ver como participar

Essa ação abrirá uma etapa intermediária com executor, dados compartilhados, destinatário, custos, compromissos e reversibilidade.

Ações secundárias persistentes:

- salvar para considerar;
- comparar.

`Mapa` não permanecerá na barra quando a oportunidade não depender de localização.

## 15. Estados alternativos ainda pendentes

- informação insuficiente sobre o momento;
- sinais de contexto conflitantes;
- avanço ainda não confirmado;
- inferência contestada;
- momento alterado recentemente;
- múltiplos Próximos Passos igualmente válidos;
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
- acessibilidade com texto ampliado e leitor de tela.

## 16. Decisões humanas aplicadas

1. A leitura do momento antecede a justificativa do Próximo Passo.
2. O avanço é demonstrado por evidências de mudança relevantes para a jornada.
3. A Guivos explica por que o Próximo Passo faz sentido por meio de uma cadeia compreensível e contestável.
4. A relação com a jornada antecede preço e conversão.
5. O preço permanece visível como investimento e condição, não argumento promocional.
6. A oportunidade é declarada como possibilidade, não recomendação definitiva.
7. A temporalidade passa a utilizar `Por que apareceu agora?`.
8. Elegibilidade passa a ser lida em `Condições para participar`.
9. `Organização responsável` passa a ser `Quem oferece`.
10. `Transparência comercial` passa a ser `Relação comercial com a Guivos`.
11. A ação principal passa a depender do tipo e estado real.
12. `Mapa` deixa de ser ação persistente quando não for material.
13. Salvar e comparar permanecem alternativas legítimas.
14. O gate da Fundação integra os critérios de aceite.

## 17. Critérios de aceite

O wireframe poderá avançar quando:

- aderência à Fundação da Guivos estiver demonstrada;
- a leitura do momento apresentar informações e fontes utilizadas;
- fato, evidência, informação externa e inferência estiverem distinguidos;
- o avanço reconhecido for demonstrado sem inventar progresso;
- o Próximo Passo for explicado por uma cadeia lógica e corrigível;
- alternativas e incertezas permanecerem visíveis;
- a relação com a jornada for compreendida antes da conversão;
- possibilidade e recomendação definitiva forem distinguidas;
- preço, custo total, validade e condições forem compreendidos;
- prazo de inscrição, validade do preço e duração não forem confundidos;
- relevância e temporalidade forem explicáveis e ajustáveis;
- elegibilidade não for interpretada como aprovação;
- fonte, responsável e relação comercial forem identificáveis;
- ação principal refletir o estado real;
- o participante puder corrigir, recusar, salvar ou comparar sem pressão;
- publicidade permanecer subordinada à relevância funcional;
- a tela não parecer página genérica de venda;
- a interação favorecer compreensão e ação no mundo real;
- a leitura não depender do identificador técnico.

## 18. Limites

Esta versão não autoriza protótipo navegável, design visual, testes de usabilidade, componentes técnicos, preços reais, validação de Organizações ou desenvolvimento.