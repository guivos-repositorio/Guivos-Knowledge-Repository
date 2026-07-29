---
id: UXA-040
title: Wireframes de Baixa Fidelidade do Fluxo do Anunciante do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
parent: UXA-039
depends_on:
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-038
  - UXA-039
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.42
normative: false
---

# Wireframes de Baixa Fidelidade do Fluxo do Anunciante do Opportunity Boost

## 1. Finalidade

Este documento materializa a primeira referência gráfica do fluxo pelo qual uma Organização ou um Coletivo elegível configura e envia uma campanha de Opportunity Boost para avaliação.

O conjunto preserva a distinção entre:

- plano elegível;
- oportunidade elegível;
- objetivo publicitário;
- critérios permitidos;
- critérios proibidos;
- orçamento e duração;
- alcance estimado;
- prévia patrocinada;
- confirmação afirmativa;
- envio para avaliação.

O conjunto não representa design final, campanha real, checkout, cobrança, algoritmo, política publicitária final, protótipo navegável ou Engenharia de Produto.

## 2. Posição na experiência

```text
Gestão da oportunidade
→ verificar disponibilidade para impulsionamento
→ escolher objetivo único
→ definir critérios permitidos
→ revisar critérios excluídos
→ definir orçamento, duração e limite diário
→ visualizar alcance estimado sem garantia
→ revisar prévia patrocinada
→ confirmar responsabilidades
→ enviar para avaliação
```

O fluxo não altera a posição orgânica da oportunidade e não utiliza compreensão inicial, Momento Atual, Próximo Passo ou inferências sensíveis.

## 3. Canal e dimensão

- canal: web para computador;
- largura: 1.440 pixels;
- altura: 1.024 pixels;
- orientação: paisagem;
- fidelidade: baixa;
- contexto: painel de Organização ou Coletivo.

## 4. Artefatos visuais

### 4.1 Elegibilidade e gate de entrada

![Elegibilidade para impulsionamento](../assets/wireframes/uxa-040-opportunity-boost-eligibility-desktop.svg)

`docs/assets/wireframes/uxa-040-opportunity-boost-eligibility-desktop.svg`

Demonstra:

- oportunidade selecionada;
- plano atual;
- estado de aprovação e atividade;
- atualização das informações materiais;
- capacidade disponível;
- responsável institucional;
- pendências de segurança ou moderação;
- ação principal disponível somente quando todos os gates forem atendidos;
- ações de correção específicas para cada bloqueio.

### 4.2 Objetivo e critérios de distribuição

![Objetivo e critérios permitidos](../assets/wireframes/uxa-040-opportunity-boost-objective-audience-desktop.svg)

`docs/assets/wireframes/uxa-040-opportunity-boost-objective-audience-desktop.svg`

Demonstra:

- objetivo único sem seleção automática;
- métrica principal associada;
- critérios gerais permitidos;
- critérios expressamente excluídos;
- ausência de público suficiente como bloqueio ou limitação;
- ação para revisar as escolhas antes de avançar.

### 4.3 Orçamento, duração e alcance estimado

![Orçamento, duração e estimativa](../assets/wireframes/uxa-040-opportunity-boost-budget-schedule-desktop.svg)

`docs/assets/wireframes/uxa-040-opportunity-boost-budget-schedule-desktop.svg`

Demonstra:

- orçamento total;
- limite diário;
- início e término;
- base candidata de cobrança;
- ausência de renovação automática;
- alcance estimado agregado;
- aviso de que estimativa não representa garantia;
- tratamento de orçamento abaixo do mínimo candidato.

### 4.4 Prévia e confirmação

![Prévia patrocinada e revisão final](../assets/wireframes/uxa-040-opportunity-boost-preview-confirmation-desktop.svg)

`docs/assets/wireframes/uxa-040-opportunity-boost-preview-confirmation-desktop.svg`

Demonstra:

- cartão patrocinado identificado;
- primeiro resultado orgânico preservado;
- superfícies selecionadas;
- ação `Por que estou vendo isto?`;
- resumo de objetivo, critérios, orçamento, duração e capacidade;
- critérios não utilizados;
- consequências de alteração material, pausa e cancelamento;
- confirmação afirmativa inicialmente desmarcada.

### 4.5 Envio para avaliação

![Envio para avaliação](../assets/wireframes/uxa-040-opportunity-boost-submission-desktop.svg)

`docs/assets/wireframes/uxa-040-opportunity-boost-submission-desktop.svg`

Demonstra:

- campanha recebida para avaliação;
- estado `Em avaliação`;
- itens que serão verificados;
- ausência de entrega antes da aprovação;
- possibilidade de cancelar o envio;
- acesso ao histórico e ao resumo enviado;
- próximos estados possíveis sem promessa de aprovação.

## 5. Pergunta funcional do conjunto

> **O anunciante compreende por que pode ou não impulsionar, escolhe conscientemente objetivo, critérios, orçamento e duração, distingue estimativa de garantia, revisa a apresentação patrocinada e envia a campanha sem acreditar que comprou relevância orgânica, recomendação ou resultado?**

Esta pergunta ainda deverá ser respondida por validação funcional especializada dos wireframes.

## 6. Gate de elegibilidade

A ação `Configurar impulsionamento` permanece indisponível enquanto existir qualquer condição crítica:

- plano não elegível;
- oportunidade não aprovada;
- oportunidade inativa ou expirada;
- informações materiais desatualizadas;
- capacidade insuficiente;
- pendência de segurança ou moderação;
- responsável institucional ausente.

Cada bloqueio apresenta motivo, consequência e ação de correção. A contratação de plano não elimina exigências de aprovação, capacidade ou segurança.

## 7. Objetivo e público

O anunciante deverá escolher uma única finalidade de distribuição. Nenhuma opção começa selecionada.

A interface apresenta separadamente:

```text
Critérios utilizados
→ região, idioma, categoria, modalidade, data, preço ou preferência geral permitida

Critérios excluídos
→ relato protegido, compreensão inicial, Momento Atual, Próximo Passo e inferências sensíveis

Alcance estimado
→ cálculo agregado e revisável, sem garantia de entrega ou conversão
```

O sistema não ampliará silenciosamente os critérios quando o público estimado for pequeno.

## 8. Orçamento e duração

A superfície deverá evidenciar:

- orçamento total limitado;
- limite diário opcional ou obrigatório conforme política futura;
- período explícito;
- ausência de renovação automática por padrão;
- base candidata de cobrança utilizada na campanha;
- orçamento mínimo candidato aplicável;
- saldo e consumo como objetos futuros, não implementados neste artefato.

Valores exibidos são ilustrativos e não constituem cobrança autorizada.

## 9. Prévia e confirmação

A prévia deverá separar visualmente:

- espaço patrocinado;
- resultado orgânico;
- marcador ou cartão identificado;
- filtros objetivos;
- explicação da distribuição;
- controles da pessoa.

A confirmação final permanece indisponível até que o anunciante:

1. revise o resumo;
2. reconheça que orçamento não garante resultado;
3. reconheça que pagamento não altera ranking orgânico;
4. aceite as responsabilidades aplicáveis por ação afirmativa.

## 10. Estado de envio

Depois do envio:

- a campanha entra em `Em avaliação`;
- nenhuma entrega publicitária começa;
- o anunciante pode abrir o resumo enviado;
- o anunciante pode cancelar o envio antes da decisão, quando permitido;
- ajustes solicitados, rejeição e aprovação permanecem estados distintos;
- nenhum prazo ou aprovação é prometido pelo wireframe.

## 11. Acessibilidade e linguagem

- o estado patrocinado não depende apenas de cor;
- controles possuem rótulos textuais;
- campos obrigatórios são identificados em linguagem clara;
- bloqueios informam ação de correção;
- valores utilizam formato monetário pt-BR;
- nenhuma urgência, culpa ou escassez artificial é utilizada;
- termos técnicos aparecem somente como referência secundária.

## 12. Limites

Este incremento não cria:

- wireframe do cartão patrocinado para a pessoa como artefato independente;
- explicação completa `Por que estou vendo isto?`;
- estados patrocinados para Lista ou Mapa;
- relatório agregado do anunciante;
- validação funcional dos wireframes;
- design visual;
- protótipo;
- teste com usuários;
- campanha, algoritmo, checkout, cobrança ou Engenharia de Produto.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente e reformular os wireframes do fluxo do anunciante;
2. criar wireframes do cartão patrocinado e da explicação de distribuição;
3. criar estados patrocinados para Lista e Mapa;
4. criar wireframe do relatório agregado;
5. validar o conjunto completo de wireframes do Opportunity Boost.

Nenhum ato é iniciado automaticamente.
