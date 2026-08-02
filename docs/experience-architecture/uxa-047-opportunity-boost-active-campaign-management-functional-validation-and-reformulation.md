---
id: UXA-047
title: Validação Funcional e Reformulação dos Wireframes de Gestão da Campanha Ativa do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
parent: UXA-046
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
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.49
normative: false
---

# Validação Funcional e Reformulação dos Wireframes de Gestão da Campanha Ativa do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente os seis wireframes criados pela UXA-046 e registra as reformulações necessárias para que o anunciante compreenda programação, entrega, limitação, pausa, alteração material, cancelamento e encerramento sem interpretar estado operacional como garantia, cobrança definitiva, relatório agregado ou política final de saldo.

A pergunta de validação é:

> **O anunciante identifica o estado atual da campanha, compreende o motivo de cada restrição, distingue eventos válidos de entrega futura, entende o efeito sobre orçamento e período e executa somente ações compatíveis com as condições de retomada ou encerramento?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova design visual final, acessibilidade técnica, algoritmo de entrega, cobrança, política jurídica, fiscal ou contábil, tratamento definitivo do saldo, relatório agregado, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. campanha programada;
2. campanha ativa;
3. campanha limitada;
4. campanha pausada;
5. alteração material;
6. cancelamento e estados finais;
7. distinção entre orçamento total, reservado, utilizado e saldo;
8. distinção entre indicador operacional e relatório agregado;
9. período de referência e validade das informações;
10. frequência, capacidade e baixa oferta orgânica;
11. pausa voluntária, pausa automática e suspensão por política;
12. condição para retomada;
13. comparação entre versão aprovada e versão alterada;
14. confirmação proporcional do cancelamento;
15. preservação de eventos válidos e histórico;
16. tratamento candidato do saldo e reconciliação;
17. acessibilidade, linguagem clara e ações indisponíveis.

## 4. Lacunas identificadas

### 4.1 Programação e início condicionados pouco explícitos

O estado programado informava que nenhuma entrega havia começado, mas não demonstrava suficientemente que o início dependia da permanência das condições aprovadas até a data programada.

Também não distinguia com clareza alterar a programação, cancelar a campanha antes do início e revisar informação material.

### 4.2 Indicadores operacionais sem período de referência suficiente

O estado ativo apresentava impressões e cliques válidos, porém o período de apuração e o horário de atualização não estavam associados diretamente ao bloco.

A ausência poderia fazer um resumo parcial parecer relatório final, conversão, impacto ou resultado consolidado.

### 4.3 Limitação ainda próxima de pausa

Embora o texto declarasse que a campanha não estava pausada, o estado precisava demonstrar de modo mais direto:

- que a entrega continuava reduzida;
- qual proteção produziu a limitação;
- que o limite diário não seria aumentado;
- que o período não seria prorrogado automaticamente;
- que atualizar capacidade não normalizaria a entrega imediatamente.

### 4.4 Pausa confundida com interrupção definitiva de cobrança

O wireframe utilizava `cobrança futura: interrompida`.

Essa formulação poderia antecipar regra financeira ainda não definida. A consequência funcional correta é interromper novos eventos de entrega, mantendo eventos válidos anteriores sujeitos à apuração e reconciliação posteriores.

### 4.5 Retomada indisponível sem controle visível

A condição de retomada era descrita, mas a interface não apresentava o controle indisponível de forma explícita nem associava o bloqueio à causa pendente.

### 4.6 Cancelamento da alteração material ambíguo

A ação `Cancelar alteração` poderia ser interpretada como retomada imediata da campanha, cancelamento da campanha inteira ou restauração automática da versão aprovada.

### 4.7 Confirmação de cancelamento parecia executável antes dos requisitos

O botão de confirmação aparecia como ação principal mesmo com motivo não selecionado e confirmações vazias.

Isso contrariava a exigência de confirmação inicialmente não concedida e poderia sugerir cancelamento acidental.

### 4.8 Estados finais incompletos e misturados ao fluxo de cancelamento

A referência não incluía de forma equivalente a suspensão por política e misturava estados automáticos, conclusão natural, cancelamento voluntário e reconciliação em uma única lista sem declarar que possuem causas e consequências próprias.

Também afirmava acesso posterior ao relatório de forma que poderia parecer que o relatório agregado já existia.

## 5. Reformulação aprovada

### 5.1 Campanha programada com gates de início

A referência passa a demonstrar:

- estado aprovado e programado;
- nenhuma entrega ou evento operacional iniciado;
- orçamento total reservado e utilizado igual a zero;
- início condicionado à oportunidade ativa, capacidade suficiente, informação material atual e ausência de bloqueio;
- verificação novamente realizada antes do início;
- alteração de programação separada de cancelamento da campanha;
- revisão de informação material sem aprovação automática.

Programação não garante início, entrega integral ou consumo do orçamento.

### 5.2 Resumo operacional com recorte temporal

Impressões, cliques e tráfego inválido passam a mostrar:

- período de referência;
- horário da última atualização;
- natureza operacional e provisória;
- ausência de equivalência a conversão, atribuição, impacto ou relatório final.

### 5.3 Estado limitado como ativo com entrega reduzida

O selo passa a declarar `ATIVA COM ENTREGA REDUZIDA`.

A referência explicita:

- motivo atual;
- consequência sobre a entrega;
- limite diário preservado;
- orçamento não acelerado;
- período não prorrogado automaticamente;
- saldo não consumido por compensação;
- atualização de capacidade seguida de nova verificação;
- ausência de normalização imediata garantida.

### 5.4 Pausa sem antecipação financeira

A pausa passa a informar:

- novos eventos de entrega interrompidos;
- eventos válidos anteriores preservados para apuração;
- orçamento utilizado preservado;
- saldo remanescente separado;
- período continuando até regra futura em contrário;
- possibilidade de expiração durante a pausa;
- ausência de retomada automática;
- ausência de promessa sobre cobrança, devolução ou reconciliação.

### 5.5 Retomada bloqueada e explicável

O controle `Retomar campanha` permanece visível como indisponível enquanto a causa não for resolvida.

A interface nomeia a condição pendente e orienta a ação disponível antes de qualquer retomada.

Suspensão por política continua separada da pausa voluntária e poderá impedir retomada.

### 5.6 Decisão sobre alteração material sem retomada implícita

As ações passam a ser:

- `Enviar para nova avaliação`;
- `Descartar alteração e revisar versão aprovada`.

Nenhuma ação inicia entrega imediatamente.

Descartar a alteração não elimina histórico e não presume que a versão aprovada ainda seja válida para retomada.

### 5.7 Cancelamento com gate completo

A confirmação permanece indisponível até:

1. seleção de motivo;
2. confirmação de encerramento da entrega futura;
3. confirmação de preservação dos eventos válidos;
4. confirmação de ausência de retomada da mesma campanha.

O estado inicial do botão é textual e visualmente indisponível.

A alternativa de pausa aparece somente quando a causa permitir retomada.

### 5.8 Estados finais separados

A referência distingue:

- orçamento esgotado;
- capacidade esgotada;
- oportunidade expirada;
- suspensa por política;
- concluída;
- cancelada;
- reconciliada.

Cada estado possui motivo e consequência próprios.

O registro operacional e o histórico permanecem acessíveis. O relatório agregado continua inexistente neste pacote e deverá ser criado separadamente.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- campanha programada não equivale a campanha ativa;
- início depende da permanência das condições aprovadas;
- nenhuma entrega ocorre antes do início válido;
- orçamento total, reservado, utilizado e saldo possuem significados distintos;
- indicadores operacionais possuem período e atualização explícitos;
- impressão e clique não representam conversão, atribuição ou impacto;
- campanha limitada permanece ativa com entrega reduzida;
- limitação não acelera orçamento nem amplia limite diário;
- limitação não prorroga período automaticamente;
- atualizar capacidade não garante normalização imediata;
- pausa voluntária, automática e suspensão por política são distintas;
- pausa interrompe novos eventos de entrega, não apaga eventos válidos anteriores;
- pausa não antecipa política de cobrança ou devolução;
- período poderá continuar e a campanha poderá expirar durante a pausa;
- retomada automática não é presumida;
- ação indisponível explica a condição necessária;
- alteração material compara versão aprovada e alterada;
- descartar alteração não retoma a campanha automaticamente;
- nova avaliação não equivale a nova aprovação;
- cancelamento exige motivo e confirmações inicialmente vazias;
- botão de cancelamento permanece indisponível antes do gate completo;
- cancelamento encerra entrega futura e impede retomada da mesma campanha;
- orçamento utilizado, eventos válidos e histórico são preservados;
- saldo permanece candidato, não devolução confirmada;
- estados finais automáticos e voluntários são distinguíveis;
- suspensão por política está representada;
- reconciliação permanece posterior;
- relatório agregado não é apresentado como existente;
- nenhum algoritmo, cobrança real, campanha real ou implementação é criado.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-046-campaign-scheduled-desktop.svg`;
2. `uxa-046-campaign-active-desktop.svg`;
3. `uxa-046-campaign-limited-desktop.svg`;
4. `uxa-046-campaign-paused-desktop.svg`;
5. `uxa-046-campaign-material-change-desktop.svg`;
6. `uxa-046-campaign-closure-desktop.svg`.

Os artefatos permanecem em baixa fidelidade, com 1.440 × 1.024 pixels para computador.

## 8. Proteções preservadas

- pagamento não compra posição orgânica, relevância, confiança, qualidade ou impacto;
- nenhum resultado é garantido;
- nenhuma entrega ocorre com informação material desatualizada;
- limite diário não é ampliado para compensar restrição;
- pausa não apaga eventos válidos;
- saldo não é apresentado como crédito, estorno ou devolução confirmados;
- cancelamento não apaga histórico;
- anunciante não recebe lista de visualizadores;
- nenhum perfil publicitário é criado;
- relatório operacional não é relatório agregado;
- Engenharia de Produto permanece pausada.

## 9. Limites

Esta validação não cria:

- wireframe do relatório agregado;
- estados móveis de gestão;
- estados de erro ou ausência de inventário;
- algoritmo de entrega ou leilão;
- política final de densidade ou frequência;
- política final de cancelamento, devolução, crédito ou disputa;
- perfil publicitário;
- design visual final;
- protótipo navegável;
- teste com usuários;
- checkout, faturamento, cobrança ou Engenharia de Produto.

## 10. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar o wireframe do relatório agregado;
2. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
3. criar estados móveis de gestão, se priorizados;
4. criar estados de erro, inventário insuficiente e preferência publicitária;
5. testar posteriormente estados, pausa, cancelamento, orçamento e controles com Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
