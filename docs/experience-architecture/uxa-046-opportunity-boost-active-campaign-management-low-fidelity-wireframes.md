---
id: UXA-046
title: Wireframes de Baixa Fidelidade da Gestão da Campanha Ativa do Opportunity Boost
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
parent: UXA-045
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
  - GEM-007-A1
  - GEM-010-A2
related:
  - UXA-047
  - GPA-007
  - M7.49
normative: false
---

# Wireframes de Baixa Fidelidade da Gestão da Campanha Ativa do Opportunity Boost

## 1. Finalidade

Este documento materializa a gestão posterior à aprovação de uma campanha do Opportunity Boost.

O pacote demonstra como o anunciante poderá compreender e controlar programação, entrega, limitação, pausa, alteração material e encerramento sem:

- confundir estado operacional com resultado humano;
- acelerar orçamento para compensar restrições;
- continuar entrega com informação desatualizada;
- esconder orçamento utilizado ou saldo não utilizado;
- apresentar pausa como cancelamento;
- antecipar cobrança, devolução, crédito, reconciliação ou retomada ainda não definidos;
- apagar eventos válidos ou histórico;
- iniciar relatório agregado, algoritmo, cobrança real ou Engenharia de Produto.

## 2. Estado de validação

A UXA-047 examinou os seis artefatos e os considerou:

> **Funcionalmente válidos após reformulação.**

As principais reformulações foram:

- explicitar que programação não garante ativação;
- associar indicadores operacionais a período e atualização;
- nomear limitação como campanha ativa com entrega reduzida;
- preservar limite diário e período durante a limitação;
- substituir antecipação de cobrança por interrupção de novos eventos de entrega;
- mostrar retomada bloqueada e sua causa;
- esclarecer o efeito de descartar alteração material;
- bloquear cancelamento até motivo e confirmações completas;
- separar suspensão por política, cancelamento e demais estados finais;
- declarar que o relatório agregado ainda não existe.

Validação funcional não equivale a acessibilidade técnica, teste com usuários, design, protótipo ou implementação.

## 3. Pergunta funcional do conjunto

> **O anunciante identifica o estado atual da campanha, compreende o motivo de cada restrição, distingue eventos válidos de entrega futura, entende o efeito sobre orçamento e período e executa somente ações compatíveis com as condições de retomada ou encerramento?**

A UXA-047 responde positivamente após as reformulações registradas.

## 4. Artefatos

| Estado | Canal | Dimensão |
|---|---|---:|
| campanha programada | web para computador | 1.440 × 1.024 |
| campanha ativa | web para computador | 1.440 × 1.024 |
| campanha limitada | web para computador | 1.440 × 1.024 |
| campanha pausada | web para computador | 1.440 × 1.024 |
| alteração material | web para computador | 1.440 × 1.024 |
| encerramento e cancelamento | web para computador | 1.440 × 1.024 |

Todos os artefatos utilizam baixa fidelidade, dados ilustrativos e rótulos textuais independentes de cor.

## 5. Artefatos visuais reformulados

### 5.1 Campanha programada

![Campanha programada](../assets/wireframes/uxa-046-campaign-scheduled-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-scheduled-desktop.svg`

Demonstra:

- campanha aprovada e programada;
- data e horário futuros;
- ausência de entrega e eventos operacionais;
- orçamento total, reservado, utilizado e saldo não utilizado;
- gates novamente verificados antes do início;
- ausência de ativação automática quando um gate falhar;
- alteração de programação separada de cancelamento;
- revisão de informação material sem aprovação automática.

Programação não equivale a garantia de início, entrega integral ou uso do orçamento.

### 5.2 Campanha ativa

![Campanha ativa](../assets/wireframes/uxa-046-campaign-active-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-active-desktop.svg`

Demonstra:

- entrega em andamento dentro das condições vigentes;
- orçamento total, utilizado e saldo não utilizado;
- período e tempo restante;
- resumo operacional com período de referência e atualização;
- frequência, capacidade, informação material e política;
- linha do tempo de decisões;
- pausa, atualização de capacidade e solicitação de alteração material;
- consequência das ações antes de sua execução.

Impressões, cliques e tráfego inválido são indicadores parciais e operacionais. Não constituem conversão, atribuição, impacto ou relatório agregado.

### 5.3 Campanha limitada

![Campanha limitada](../assets/wireframes/uxa-046-campaign-limited-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-limited-desktop.svg`

Demonstra:

- campanha ativa com entrega reduzida;
- limitação por capacidade no exemplo;
- novos eventos ainda permitidos em ritmo protegido;
- limite diário preservado;
- orçamento não acelerado;
- período não ampliado automaticamente;
- saldo não consumido para compensação;
- condição para nova verificação;
- ausência de normalização imediata garantida;
- distinção entre capacidade, frequência, pouca oferta orgânica e outra restrição operacional.

### 5.4 Campanha pausada

![Campanha pausada](../assets/wireframes/uxa-046-campaign-paused-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-paused-desktop.svg`

Demonstra:

- pausa automática por informação material alterada;
- interrupção de novos eventos de entrega;
- preservação de eventos válidos anteriores para apuração posterior;
- orçamento utilizado e saldo não utilizado separados;
- período vigente e possibilidade de expiração durante a pausa;
- condição explícita para solicitar retomada;
- controle de retomada indisponível enquanto a causa persistir;
- distinção entre pausa voluntária, pausa automática e suspensão por política;
- ausência de decisão final sobre cobrança, devolução ou reconciliação.

### 5.5 Alteração material

![Alteração material](../assets/wireframes/uxa-046-campaign-material-change-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-material-change-desktop.svg`

Demonstra:

- comparação entre versão aprovada e versão alterada;
- campos alterados identificados por texto;
- impacto sobre decisão, elegibilidade e capacidade;
- pausa anterior à nova entrega;
- eventos válidos anteriores vinculados à versão aprovada;
- envio para nova avaliação;
- descarte da alteração com revisão da versão aprovada;
- nenhuma aprovação ou retomada automática.

### 5.6 Encerramento e cancelamento

![Encerramento e cancelamento](../assets/wireframes/uxa-046-campaign-closure-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-closure-desktop.svg`

Demonstra:

- campanha ainda ativa antes da confirmação completa;
- consequência irreversível para a mesma campanha;
- novos eventos encerrados e eventos válidos anteriores preservados;
- orçamento utilizado e saldo não utilizado separados;
- motivo obrigatório;
- três confirmações inicialmente vazias;
- botão de cancelamento indisponível antes do gate completo;
- estados orçamento esgotado, capacidade esgotada, oportunidade expirada, suspensão por política, conclusão, cancelamento e reconciliação;
- registro operacional preservado;
- relatório agregado explicitamente ainda não criado.

## 6. Modelo de estados preservado

```text
programada
→ ativa
→ ativa com entrega reduzida por frequência | capacidade | pouca oferta orgânica
→ pausada pelo anunciante | pausada automaticamente
→ orçamento esgotado | capacidade esgotada | oportunidade expirada
→ suspensa por política
→ concluída | cancelada
→ reconciliada
```

A interface não apresenta os estados como sequência obrigatoriamente linear.

Cada estado explica:

1. motivo;
2. consequência sobre novos eventos de entrega;
3. efeito sobre orçamento, saldo e período;
4. ação disponível ou indisponível;
5. condição para verificação, retomada ou encerramento.

## 7. Programação

Uma campanha programada:

- foi aprovada;
- possui data futura de início;
- ainda não iniciou entrega;
- possui orçamento reservado e utilizado igual a zero;
- não gera impressão, clique ou evento operacional;
- depende da permanência dos gates até o início;
- poderá ter data ou horário alterados;
- poderá ser cancelada antes do início mediante confirmação;
- poderá exigir nova avaliação se informação material mudar.

Programação não equivale a garantia de ativação ou entrega integral.

## 8. Estado ativo

O estado ativo demonstra que a campanha poderá gerar novos eventos dentro de:

- período aprovado;
- orçamento e limite diário;
- critérios aprovados;
- frequência permitida;
- capacidade declarada;
- informação material atual;
- política vigente.

Indicadores operacionais deverão informar período e atualização. Eles não representam conversão, atribuição, impacto, relatório final ou garantia.

## 9. Limitação

A campanha poderá permanecer ativa com entrega reduzida quando houver:

- proteção de frequência;
- capacidade insuficiente para entrega normal;
- pouca oferta orgânica, que reduz inventário pago;
- outra limitação operacional explicável.

A limitação:

- mantém novos eventos em ritmo protegido;
- não acelera orçamento;
- não amplia limite diário;
- não amplia duração automaticamente;
- não remove saldo;
- exige nova verificação após atualização;
- não promete normalização imediata.

## 10. Pausa

### 10.1 Pausa voluntária

Poderá ser iniciada pelo anunciante quando não houver bloqueio superior.

Deverá mostrar:

- novos eventos interrompidos;
- eventos válidos anteriores preservados;
- orçamento utilizado;
- saldo não utilizado;
- período restante;
- possibilidade e condição de retomada.

### 10.2 Pausa automática

Poderá ocorrer por:

- alteração material;
- informação desatualizada;
- capacidade insuficiente;
- orçamento ou limite;
- expiração;
- segurança, moderação ou política.

Retomada automática não será presumida.

A pausa não define cobrança futura, devolução ou crédito. Eventos válidos anteriores permanecem sujeitos à apuração e reconciliação posteriores.

### 10.3 Suspensão por política

Suspensão por política não é pausa voluntária. Poderá impedir retomada e exigir revisão especializada.

## 11. Alteração material

Mudança em preço, gratuidade, data, local, modalidade, responsável, elegibilidade, risco, capacidade ou condição comercial deverá:

1. interromper novos eventos quando puder alterar a decisão da pessoa;
2. comparar versão aprovada e versão alterada;
3. preservar eventos válidos anteriores;
4. preservar orçamento utilizado;
5. manter saldo separado;
6. recalcular somente estimativas futuras;
7. exigir nova avaliação quando necessário;
8. impedir entrega com informação desatualizada;
9. impedir retomada automática ao descartar a alteração.

Correção editorial sem mudança material poderá seguir fluxo distinto e deverá manter histórico.

## 12. Orçamento, saldo e período

A gestão apresenta separadamente:

- orçamento total aprovado;
- orçamento reservado, quando ainda não iniciado;
- orçamento utilizado validado;
- saldo não utilizado;
- limite diário;
- período vigente;
- tratamento candidato do saldo após encerramento.

A interface não poderá:

- prometer uso integral do orçamento;
- acelerar gasto após limitação;
- ampliar limite diário ou período automaticamente;
- apresentar saldo como crédito, estorno ou devolução confirmados;
- apagar eventos inválidos ou válidos;
- cobrar simultaneamente CPM e CPC na mesma campanha.

## 13. Encerramento

Estados finais informam motivo e consequência próprios:

- orçamento esgotado;
- capacidade esgotada;
- oportunidade expirada;
- suspensa por política;
- concluída;
- cancelada;
- reconciliada.

Cancelamento:

- exige motivo;
- exige confirmações inicialmente vazias;
- mantém o botão indisponível antes do gate completo;
- encerra novos eventos;
- não apaga eventos válidos;
- não apaga histórico;
- não permite retomada da mesma campanha;
- mostra orçamento utilizado e saldo candidato;
- mantém o registro operacional acessível.

Reconciliação será posterior ao tratamento dos eventos e do saldo. Este pacote não cria o relatório agregado nem a política final de reconciliação.

## 14. Linha do tempo e histórico

A gestão registra, quando aplicável:

- aprovação;
- programação;
- início;
- limitação;
- pausa;
- alteração material;
- nova avaliação;
- retomada;
- esgotamento;
- suspensão;
- conclusão;
- cancelamento;
- reconciliação.

Histórico não será apagado por pausa, cancelamento, edição ou descarte de alteração.

## 15. Acessibilidade e linguagem

- estado é textual e não depende de cor;
- motivo, consequência e ação são anunciáveis;
- valores possuem rótulo e unidade;
- período de indicadores é explícito;
- mudanças materiais são identificadas por texto;
- ações indisponíveis explicam a condição necessária;
- pausa e cancelamento possuem consequências distintas;
- confirmações não começam selecionadas;
- botão bloqueado é textual e visualmente reconhecível;
- urgência, culpa e escassez artificial são proibidas;
- indicadores operacionais são distinguidos de relatório e impacto.

Esta referência não conclui acessibilidade técnica.

## 16. Proteções preservadas

- nenhuma entrega antes da programação válida;
- nenhuma entrega com informação material desatualizada;
- limitação não acelera orçamento ou amplia limite diário;
- pausa interrompe novos eventos de entrega;
- eventos válidos anteriores permanecem;
- saldo não é tratado como devolução confirmada;
- cancelamento exige gate completo e encerra retomada;
- pagamento não compra relevância, qualidade, confiança ou impacto;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado;
- indicadores operacionais não constituem relatório agregado;
- Engenharia de Produto permanece pausada.

## 17. Limites

Este incremento não cria:

- wireframe do relatório agregado;
- estados móveis de gestão;
- algoritmo de entrega ou leilão;
- política final de densidade ou frequência;
- política final de cancelamento, devolução, crédito e disputa;
- perfil publicitário;
- design visual final;
- protótipo navegável;
- teste com usuários;
- checkout, faturamento, cobrança ou Engenharia de Produto.

## 18. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o wireframe do relatório agregado;
2. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
3. criar estados móveis de gestão, se priorizados;
4. criar estados de erro, inventário insuficiente e preferência publicitária;
5. testar posteriormente estados, pausa, cancelamento, orçamento e controles com Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
