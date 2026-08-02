---
id: UXA-046
title: Wireframes de Baixa Fidelidade da Gestão da Campanha Ativa do Opportunity Boost
status: active
version: 0.1.0
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
  - GPA-007
  - M7.48
normative: false
---

# Wireframes de Baixa Fidelidade da Gestão da Campanha Ativa do Opportunity Boost

## 1. Finalidade

Este documento materializa a gestão posterior à aprovação de uma campanha do Opportunity Boost.

O pacote demonstra como o anunciante poderá compreender e controlar programação, entrega, limitação, pausa, alteração material e encerramento sem:

- confundir estado operacional com resultado humano;
- acelerar orçamento para compensar restrições;
- continuar entrega com informação desatualizada;
- esconder orçamento utilizado ou saldo remanescente;
- apresentar pausa como cancelamento;
- prometer devolução, reconciliação ou retomada ainda não definidas;
- apagar eventos válidos ou histórico;
- iniciar relatório agregado, algoritmo, cobrança real ou Engenharia de Produto.

## 2. Pergunta funcional do conjunto

> **O anunciante compreende o estado atual da campanha, o motivo de qualquer restrição, a consequência sobre entrega e orçamento, a ação disponível e a condição necessária para retomar ou encerrar sem interpretar indicadores operacionais como garantia de resultado?**

A pergunta ainda deverá ser respondida por validação funcional especializada dos wireframes.

## 3. Artefatos

| Estado | Canal | Dimensão |
|---|---|---:|
| campanha programada | web para computador | 1.440 × 1.024 |
| campanha ativa | web para computador | 1.440 × 1.024 |
| campanha limitada | web para computador | 1.440 × 1.024 |
| campanha pausada | web para computador | 1.440 × 1.024 |
| alteração material | web para computador | 1.440 × 1.024 |
| encerramento e cancelamento | web para computador | 1.440 × 1.024 |

Todos os artefatos utilizam baixa fidelidade, dados ilustrativos e rótulos textuais independentes de cor.

## 4. Artefatos visuais

### 4.1 Campanha programada

![Campanha programada](../assets/wireframes/uxa-046-campaign-scheduled-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-scheduled-desktop.svg`

Demonstra:

- aprovação concluída;
- data e horário futuros;
- ausência de entrega;
- orçamento reservado e ainda não utilizado;
- condições verificadas;
- ações anteriores ao início;
- alerta de que alteração material poderá exigir nova avaliação.

### 4.2 Campanha ativa

![Campanha ativa](../assets/wireframes/uxa-046-campaign-active-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-active-desktop.svg`

Demonstra:

- entrega em andamento;
- orçamento total, utilizado e saldo;
- período e tempo restante;
- indicadores operacionais de entrega;
- frequência, capacidade, informação material e política;
- linha do tempo;
- pausa, atualização de capacidade e solicitação de alteração material.

Os indicadores são operacionais e não constituem relatório agregado ou impacto comprovado.

### 4.3 Campanha limitada

![Campanha limitada](../assets/wireframes/uxa-046-campaign-limited-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-limited-desktop.svg`

Demonstra:

- limitação por capacidade no exemplo;
- entrega reduzida sem pausa completa;
- orçamento não acelerado;
- período não ampliado automaticamente;
- condições para normalização;
- distinção entre limitação por capacidade, frequência e baixa oferta orgânica.

### 4.4 Campanha pausada

![Campanha pausada](../assets/wireframes/uxa-046-campaign-paused-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-paused-desktop.svg`

Demonstra:

- pausa automática por informação material alterada;
- interrupção de entrega e cobrança futura;
- preservação de eventos válidos;
- orçamento utilizado e saldo separado;
- condição explícita para retomada;
- distinção entre pausa voluntária, pausa automática e suspensão por política.

### 4.5 Alteração material

![Alteração material](../assets/wireframes/uxa-046-campaign-material-change-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-material-change-desktop.svg`

Demonstra:

- comparação entre informação aprovada e alterada;
- mudanças identificadas por texto;
- pausa anterior à nova entrega;
- efeitos sobre orçamento e estimativas futuras;
- envio para nova avaliação;
- cancelamento da alteração sem início imediato da entrega.

### 4.6 Encerramento e cancelamento

![Encerramento e cancelamento](../assets/wireframes/uxa-046-campaign-closure-desktop.svg)

`docs/assets/wireframes/uxa-046-campaign-closure-desktop.svg`

Demonstra:

- entrega futura encerrada;
- eventos válidos e histórico preservados;
- orçamento utilizado e saldo remanescente;
- tratamento do saldo ainda candidato;
- estados orçamento esgotado, capacidade esgotada, expirada, concluída e cancelada;
- reconciliação posterior;
- confirmação proporcional à ativação.

## 5. Modelo de estados preservado

```text
programada
→ ativa
→ limitada por frequência | limitada por capacidade
→ pausada pelo anunciante | pausada automaticamente
→ orçamento esgotado | capacidade esgotada | oportunidade expirada
→ suspensa por política
→ concluída | cancelada
→ reconciliada
```

A interface não apresenta os estados como uma sequência obrigatoriamente linear.

Cada estado deverá explicar:

1. motivo;
2. consequência sobre entrega;
3. efeito sobre orçamento e saldo;
4. ação possível;
5. condição para retomada ou encerramento.

## 6. Programação

Uma campanha programada:

- foi aprovada;
- possui data futura de início;
- ainda não iniciou entrega;
- possui orçamento reservado, não utilizado;
- não gera impressão, clique ou evento operacional;
- poderá ter programação cancelada;
- poderá exigir nova avaliação se informação material mudar.

Programação não equivale a garantia de entrega integral.

## 7. Estado ativo

O estado ativo demonstra que a campanha poderá entregar dentro de:

- período aprovado;
- orçamento e limite diário;
- critérios aprovados;
- frequência permitida;
- capacidade declarada;
- informação material atual;
- política vigente.

Indicadores operacionais poderão informar impressões válidas, cliques válidos e tráfego inválido removido, mas não deverão ser apresentados como relatório final, conversão ou impacto.

## 8. Limitação

A campanha poderá permanecer ativa com entrega reduzida quando houver:

- proteção de frequência;
- capacidade insuficiente para entrega normal;
- pouca oferta orgânica, que reduz inventário pago;
- outra limitação operacional explicável.

A limitação:

- não acelera orçamento;
- não amplia duração automaticamente;
- não remove saldo;
- não promete normalização após atualização;
- deverá informar condição para retorno à entrega normal.

## 9. Pausa

### 9.1 Pausa voluntária

Poderá ser iniciada pelo anunciante quando não houver bloqueio superior.

Deverá mostrar:

- entrega futura interrompida;
- orçamento utilizado;
- saldo remanescente;
- período restante;
- possibilidade e condição de retomada.

### 9.2 Pausa automática

Poderá ocorrer por:

- alteração material;
- informação desatualizada;
- capacidade insuficiente;
- orçamento ou limite;
- expiração;
- segurança, moderação ou política.

Retomada automática não será presumida.

### 9.3 Suspensão por política

Suspensão por política não é pausa voluntária. Poderá impedir retomada e exigir revisão especializada.

## 10. Alteração material

Mudança em preço, gratuidade, data, local, modalidade, responsável, elegibilidade, risco, capacidade ou condição comercial deverá:

1. interromper entrega quando puder alterar a decisão da pessoa;
2. comparar versão aprovada e versão alterada;
3. preservar eventos válidos anteriores;
4. preservar orçamento utilizado;
5. manter saldo separado;
6. recalcular somente estimativas futuras;
7. exigir nova avaliação quando necessário;
8. impedir entrega com informação desatualizada.

Correção editorial sem mudança material poderá seguir fluxo distinto e deverá manter histórico.

## 11. Orçamento e saldo

A gestão deverá apresentar separadamente:

- orçamento total;
- orçamento utilizado;
- saldo remanescente;
- limite diário;
- período vigente;
- tratamento candidato do saldo após encerramento.

A interface não poderá:

- prometer uso integral do orçamento;
- acelerar gasto após limitação;
- ampliar período automaticamente;
- apresentar saldo como devolução confirmada;
- ocultar eventos invalidados;
- cobrar simultaneamente CPM e CPC na mesma campanha.

## 12. Encerramento

Estados finais deverão informar motivo e consequência próprios:

- orçamento esgotado;
- capacidade esgotada;
- oportunidade expirada;
- suspensa por política;
- concluída;
- cancelada;
- reconciliada.

Cancelamento:

- encerra entrega futura;
- não apaga eventos válidos;
- não apaga histórico;
- não permite retomada da mesma campanha;
- exige confirmação proporcional à ativação;
- mostra orçamento utilizado e saldo candidato;
- mantém acesso posterior ao relatório quando ele existir.

Reconciliação será posterior ao tratamento dos eventos e do saldo. Este pacote não cria o relatório agregado nem a política final de reconciliação.

## 13. Linha do tempo e histórico

A gestão deverá registrar, quando aplicável:

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

Histórico não será apagado por pausa, cancelamento ou edição.

## 14. Acessibilidade e linguagem

- estado será textual e não dependerá de cor;
- motivo, consequência e ação serão anunciáveis;
- valores terão rótulo e unidade;
- mudanças materiais serão identificadas por texto;
- ações indisponíveis explicarão a condição necessária;
- pausa e cancelamento terão consequências explícitas;
- confirmação não começará selecionada;
- urgência, culpa e escassez artificial serão proibidas;
- indicadores operacionais serão distinguidos de relatório e impacto.

Esta referência não conclui acessibilidade técnica.

## 15. Proteções preservadas

- nenhuma entrega antes da programação;
- nenhuma entrega com informação material desatualizada;
- limitação não acelera orçamento;
- pausa interrompe entrega futura;
- eventos válidos anteriores permanecem;
- saldo não é tratado como devolução confirmada;
- cancelamento exige confirmação e encerra retomada;
- pagamento não compra relevância, qualidade, confiança ou impacto;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado;
- indicadores operacionais não constituem relatório agregado;
- Engenharia de Produto permanece pausada.

## 16. Limites

Este incremento não cria:

- validação funcional dos seis wireframes;
- wireframe do relatório agregado;
- estados móveis de gestão;
- algoritmo de entrega ou leilão;
- política final de densidade ou frequência;
- política final de cancelamento, devolução e disputa;
- perfil publicitário;
- tecnologia cartográfica;
- design visual final;
- protótipo navegável;
- teste com usuários;
- checkout, faturamento, cobrança ou Engenharia de Produto.

## 17. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente e reformular os seis wireframes da UXA-046;
2. criar o wireframe do relatório agregado;
3. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
4. criar estados móveis de gestão, se priorizados;
5. criar estados de erro, inventário insuficiente e preferência publicitária;
6. testar posteriormente estados, pausa, cancelamento, orçamento e controles com Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
