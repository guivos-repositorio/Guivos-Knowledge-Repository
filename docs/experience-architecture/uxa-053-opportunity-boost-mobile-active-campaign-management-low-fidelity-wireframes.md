---
id: UXA-053
title: Wireframes de Baixa Fidelidade da Gestão Móvel da Campanha Ativa do Opportunity Boost
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
parent: UXA-052
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
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.55
normative: false
---

# Wireframes de Baixa Fidelidade da Gestão Móvel da Campanha Ativa do Opportunity Boost

## 1. Finalidade

Este documento materializa em aplicativo móvel as seis responsabilidades de gestão posterior à aprovação do Opportunity Boost já validadas para computador pela UXA-046 reformulada e pela UXA-047.

O conjunto representa:

1. campanha programada;
2. campanha ativa;
3. campanha ativa com entrega reduzida;
4. campanha pausada;
5. alteração material;
6. encerramento e cancelamento.

A materialização não presume responsividade automática, equivalência visual ou implementação compartilhada com a referência para computador.

## 2. Posição no percurso governado

```text
campanha aprovada
→ programação futura
→ nova verificação dos gates
→ ativação válida
→ entrega operacional
→ entrega reduzida | pausa | alteração material
→ conclusão | cancelamento | suspensão
→ reconciliação
→ relatório agregado
```

Programação não garante ativação. Ativação não garante entrega integral. Pausa não equivale a cancelamento. Cancelamento não equivale a reconciliação ou devolução.

## 3. Canal e dimensão

- canal: aplicativo móvel;
- largura de referência: 390 pixels;
- altura de referência: 844 pixels;
- orientação: retrato;
- fidelidade: baixa;
- contexto: painel móvel de Organização ou Coletivo;
- estado: materialização ainda não validada funcionalmente.

## 4. Princípios estruturais móveis

A gestão móvel utiliza:

- estado textual anterior ao conteúdo principal;
- identidade persistente da campanha e da versão aprovada;
- uma responsabilidade operacional principal por tela;
- orçamento, saldo e período próximos ao estado;
- motivo, consequência e condição de ação apresentados no mesmo contexto;
- ações destrutivas ou de retomada condicionadas;
- histórico acessível em todos os estados relevantes;
- rótulos independentes de cor;
- nenhuma promessa de resultado, consumo integral, normalização, crédito ou devolução.

A redução de espaço não autoriza ocultar causa, consequência, versão, saldo, período ou condição de retomada.

## 5. Artefatos visuais

### 5.1 Campanha programada

![Campanha programada móvel](../assets/wireframes/uxa-053-campaign-scheduled-mobile.svg)

`docs/assets/wireframes/uxa-053-campaign-scheduled-mobile.svg`

Demonstra:

- campanha aprovada e programada para data futura;
- versão aprovada identificada;
- ausência de entrega e eventos operacionais;
- orçamento total, reservado e utilizado;
- gates atendido e atendido com limite;
- nova verificação antes do início;
- ativação impedida quando um gate falhar;
- alteração de programação separada de revisão material e cancelamento.

Programação não representa garantia de início, entrega integral ou uso do orçamento.

### 5.2 Campanha ativa

![Campanha ativa móvel](../assets/wireframes/uxa-053-campaign-active-mobile.svg)

`docs/assets/wireframes/uxa-053-campaign-active-mobile.svg`

Demonstra:

- entrega em andamento dentro das condições vigentes;
- campanha e versão aprovada persistentes;
- orçamento total, utilizado e saldo;
- período e tempo restante;
- indicadores operacionais com recorte e atualização;
- impressão, clique e evento inválido separados;
- frequência, capacidade, informação material e política;
- pausa, atualização de capacidade e alteração material como ações distintas;
- histórico e relatório agregado acessíveis separadamente.

Indicador operacional não equivale a conversão, atribuição, impacto ou relatório final.

### 5.3 Campanha ativa com entrega reduzida

![Campanha limitada móvel](../assets/wireframes/uxa-053-campaign-limited-mobile.svg)

`docs/assets/wireframes/uxa-053-campaign-limited-mobile.svg`

Demonstra:

- campanha ainda ativa;
- entrega reduzida por capacidade no exemplo;
- novos eventos ainda permitidos em ritmo protegido;
- distinção de pausa, suspensão e encerramento;
- orçamento utilizado, saldo e limite diário;
- ausência de aceleração do orçamento;
- ausência de ampliação automática do limite ou período;
- condição para nova verificação;
- ausência de normalização imediata garantida;
- outras causas possíveis de limitação.

### 5.4 Campanha pausada

![Campanha pausada móvel](../assets/wireframes/uxa-053-campaign-paused-mobile.svg)

`docs/assets/wireframes/uxa-053-campaign-paused-mobile.svg`

Demonstra:

- pausa automática por alteração material;
- novos eventos de entrega interrompidos;
- eventos válidos anteriores preservados;
- orçamento utilizado e saldo separados;
- período continuando e podendo expirar;
- condição explícita para solicitar retomada;
- controle de retomada visível e indisponível;
- histórico e encerramento acessíveis;
- pausa voluntária, automática e suspensão por política como estados distintos.

A pausa não promete crédito, devolução, reconciliação ou retomada automática.

### 5.5 Alteração material

![Alteração material móvel](../assets/wireframes/uxa-053-campaign-material-change-mobile.svg)

`docs/assets/wireframes/uxa-053-campaign-material-change-mobile.svg`

Demonstra:

- versão aprovada e versão candidata identificadas;
- campos alterados apresentados lado a lado;
- entrega pausada antes de nova decisão;
- eventos anteriores vinculados à versão aprovada;
- orçamento utilizado preservado;
- estimativas futuras sujeitas a recálculo;
- envio para nova avaliação;
- descarte da alteração com revisão da versão aprovada;
- nova verificação dos gates antes de eventual retomada;
- histórico de versões acessível.

Nenhuma ação retoma a entrega automaticamente.

### 5.6 Encerramento e cancelamento

![Encerramento móvel da campanha](../assets/wireframes/uxa-053-campaign-closure-mobile.svg)

`docs/assets/wireframes/uxa-053-campaign-closure-mobile.svg`

Demonstra:

- campanha ainda ativa antes da confirmação completa;
- cancelamento irreversível para a mesma campanha;
- orçamento utilizado e saldo não utilizado separados;
- motivo obrigatório ainda não selecionado;
- três confirmações inicialmente vazias;
- botão de cancelamento indisponível;
- pausa como alternativa quando houver possibilidade de retomada;
- eventos válidos e histórico preservados;
- estados finais com causas próprias;
- relatório agregado acessível quando aplicável;
- reconciliação e tratamento financeiro permanecendo separados.

## 6. Continuidade da campanha

Os seis estados preservam:

- identificador `BST-2026-081`;
- oportunidade vinculada;
- anunciante responsável;
- versão aprovada `v1`;
- orçamento total e limite diário;
- período aprovado;
- histórico das decisões;
- relação entre eventos válidos e versão correspondente.

Alteração material cria versão candidata e não reescreve eventos anteriores.

## 7. Autoridade dos estados

```text
PROGRAMADA
→ aprovada, futura e ainda sem entrega

ATIVA
→ novos eventos permitidos dentro das condições vigentes

ATIVA COM LIMITE
→ novos eventos permitidos em ritmo protegido

PAUSADA
→ novos eventos interrompidos; eventos anteriores preservados

ALTERAÇÃO MATERIAL
→ versão candidata em decisão; entrega futura bloqueada

CANCELAMENTO PENDENTE
→ campanha ainda ativa até motivo e confirmações completas
```

Suspensão por política, orçamento esgotado, capacidade esgotada, oportunidade expirada, conclusão, cancelamento e reconciliação possuem motivos e consequências próprios.

## 8. Orçamento, saldo e período

A gestão móvel apresenta separadamente:

- orçamento total aprovado;
- orçamento reservado, antes do início;
- orçamento utilizado validado;
- saldo não utilizado;
- limite diário;
- período aprovado;
- tempo restante ou término;
- tratamento candidato do saldo após encerramento.

A interface não poderá:

- prometer uso integral do orçamento;
- acelerar gasto após limitação;
- ampliar limite diário ou período automaticamente;
- transformar saldo em devolução confirmada;
- cobrar simultaneamente CPM e CPC;
- apagar eventos válidos, inválidos ou histórico.

## 9. Indicadores e relatório

A tela ativa apresenta indicadores operacionais provisórios com:

- período de referência;
- horário de atualização;
- unidade de cada evento;
- aviso de que não constituem conversão, atribuição, impacto ou relatório final.

O relatório agregado permanece superfície separada, governada pela UXA-048 reformulada e pela UXA-049.

## 10. Pausa e retomada

A pausa:

- interrompe novos eventos;
- preserva eventos válidos anteriores;
- preserva orçamento utilizado;
- mantém saldo separado;
- poderá permitir que o período continue;
- poderá terminar por expiração;
- não presume retomada automática;
- não define tratamento financeiro final.

A retomada somente poderá ser solicitada quando:

1. a causa estiver resolvida;
2. a informação material estiver válida;
3. os gates forem verificados novamente;
4. não houver suspensão superior.

## 11. Alteração material

Mudança em preço, gratuidade, data, local, modalidade, responsável, elegibilidade, risco, capacidade ou condição comercial deverá:

- interromper entrega futura quando relevante;
- comparar versões;
- preservar eventos anteriores;
- preservar orçamento utilizado;
- recalcular apenas estimativas futuras;
- exigir nova avaliação quando aplicável;
- impedir retomada automática após envio ou descarte.

## 12. Cancelamento e estados finais

Cancelamento exige:

1. motivo obrigatório;
2. confirmação de encerramento dos novos eventos;
3. confirmação de preservação dos eventos válidos e histórico;
4. confirmação de impossibilidade de retomada da mesma campanha.

Antes do gate completo, a campanha permanece no estado operacional anterior.

Estados finais preservados:

- orçamento esgotado;
- capacidade esgotada;
- oportunidade expirada;
- suspensa por política;
- concluída;
- cancelada;
- reconciliada.

## 13. Acessibilidade e linguagem

- estados são nomeados por texto;
- motivo, consequência e condição de ação aparecem juntos;
- valores possuem rótulo e unidade;
- indicadores possuem período e atualização;
- ação indisponível apresenta a causa;
- mudanças são identificadas por texto;
- confirmações começam vazias;
- ação destrutiva permanece bloqueada;
- nenhuma urgência, culpa ou escassez artificial é utilizada.

Esta materialização não conclui acessibilidade técnica.

## 14. Perguntas para validação funcional posterior

A validação especializada deverá verificar:

- o estado atual é reconhecido antes dos indicadores?
- campanha e versão permanecem identificáveis nas seis telas?
- programação é distinguível de atividade?
- orçamento reservado, utilizado e saldo são compreensíveis?
- indicadores operacionais parecem provisórios e datados?
- entrega reduzida é distinguível de pausa?
- limite diário e período permanecem protegidos durante a limitação?
- pausa interrompe novos eventos sem sugerir cancelamento?
- evento anterior permanece associado à versão aprovada?
- retomada indisponível explica a causa?
- comparação de versões permanece legível em tela pequena?
- envio e descarte de alteração evitam retomada implícita?
- cancelamento exige motivo e confirmações independentes?
- pausa aparece como alternativa somente quando compatível?
- estados finais e reconciliação permanecem separados?
- histórico e relatório agregado são superfícies distintas?

## 15. Estado funcional

`materialized_not_functionally_validated — six low-fidelity mobile active-campaign management wireframes created; state hierarchy, budget comprehension, pause/resume conditions, version comparison and cancellation gates require specialized functional validation`.

## 16. Proteções preservadas

- pagamento não compra relevância, confiança, qualidade ou impacto;
- nenhuma entrega antes de programação válida;
- nenhuma entrega com informação material desatualizada;
- limitação não acelera orçamento;
- pausa não apaga eventos válidos;
- alteração material não reescreve o passado;
- cancelamento não apaga histórico;
- saldo não é devolução confirmada;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado;
- gestão móvel não autoriza campanha real, cobrança ou implementação.

## 17. Limites

Este incremento não cria:

- validação funcional dos seis artefatos móveis;
- estados completos de erro técnico;
- experiência operacional de inventário insuficiente;
- experiência detalhada de preferência publicitária;
- nova validação transversal dos 36 wireframes;
- design visual final;
- responsividade implementada;
- acessibilidade técnica;
- protótipo navegável;
- teste com Organizações ou Coletivos;
- política final de frequência, cancelamento, devolução, crédito ou disputa;
- algoritmo, antifraude, checkout, cobrança, campanha real ou Engenharia de Produto.

## 18. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente e reformular os seis wireframes móveis da UXA-053;
2. criar estados de erro, inventário insuficiente e preferência publicitária;
3. validar transversalmente os 36 wireframes, se priorizado;
4. definir protocolo de protótipo de baixa ou média fidelidade;
5. preparar plano de teste com Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
