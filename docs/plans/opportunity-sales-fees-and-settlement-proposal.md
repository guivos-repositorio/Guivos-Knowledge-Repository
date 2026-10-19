---
title: Taxas Guivos por venda de oportunidades — proposta de política comercial e simulação
version: 1.1.0
status: approved_for_design_and_simulation
decision_date: 2026-10-19
scope: Organizações e Coletivos; oportunidades pagas
---

# Taxas Guivos por venda de oportunidades

## Estado de governança

**DECISÃO DE PRODUTO APROVADA EM 2026-10-19 PARA DOCUMENTAÇÃO E SIMULAÇÃO NO CADASTRO DE OPORTUNIDADES.** O responsável confirmou a adoção da regra proposta de 8,9% e R$ 1,00 acima de R$ 20,00 como **referência de simulação**, e autorizou seu registro no GKR e aplicação na estação Replit. Esta aprovação **não ativa a cobrança efetiva**, a dedução em pagamentos reais, contratos ou checkout: esses passos permanecem condicionados à validação de Financeiro/Jurídico, viabilidade de adquirência, tributos, chargebacks, custo de pontos e publicação financeira específica. Deve ser conciliada com `Planos — Business` e políticas de pontos anteriormente validadas; as regras existentes não foram presumidas substituídas.

## 1. Benchmark consultado

Hotmart, política oficial https://hotmart.com/pt-br/legal/politicas-de-pagamento, consultada em 2026-10-19: transações BRL até R$10,00, serviço 20%, sem tarifa fixa; a partir de R$10,01, serviço 9,9% e tarifa fixa BRL R$2,49 por transação. Condições comerciais especiais/por volume podem divergir, conforme https://hotmart.com/pt-br/taxa-hotmart. **Esses números não são tarifas Guivos nem necessariamente representam custos da Guivos.**

## 2. Regra aprovada para simulação — tarifa Guivos (BRL)

Incidência: **cada venda de oportunidade paga aprovada/capturada pela Guivos**, independentemente do tipo do publicador (Organização/Coletivo), com regras de plano/contratação para elegibilidade à publicação determinadas por instrumentos próprios.

- Para valor bruto positivo **até R$20,00**: **8,9% do preço efetivamente cobrado**, sem componente fixo.
- Para valor bruto **superior a R$20,00**: **8,9% do preço efetivamente cobrado + R$1,00** por venda aprovada.
- Não há taxa transacional sobre oportunidade **gratuita sem cobrança**; outras taxas de planos/serviços, se existirem, são contratos separados.
- Não presumir descontos progressivos por volume ou taxas por país/moeda sem proposta adicional versionada.
- A taxa é suportada pelo publicador no repasse e **não somada silenciosamente ao preço apresentado à Pessoa**.
- Nunca descontar taxa no evento de cadastro, criação, edição ou salvamento de rascunho; somente por transação financeira elegível. Regras finais de reconhecimento financeiro, reserva, retenção, liquidação e notas fiscais ficam para a integração de pagamentos.

## 3. Quatro valores separados na UI

1. **Preço da oportunidade / preço de venda**: valor cobrado da Pessoa, antes de incentivos custeados pelo publicador; se houver desconto REAL à Pessoa, a base passa a ser o total efetivamente pago após desconto, conforme regras de cupom/checkout.
2. **Incentivo em Pontos Guivos**: custo monetário de pontos financiados integralmente por Organização/Coletivo, limitado pelas regras específicas; não é desconto automático do preço ao consumidor.
3. **Valor após incentivo** = preço da venda − custo monetário dos pontos concedidos por essa venda.
4. **Repasse líquido estimado** = valor após incentivo − taxa Guivos − outras deduções explicitamente contratadas e discriminadas; jamais rotular o valor após incentivo como 'repasse líquido'.

**Taxa Guivos percentual incide sobre preço efetivamente cobrado da Pessoa**, independentemente de incentivo em pontos; componente fixo é por transação e não por item, se a venda for de um único item. Compras agrupadas, parcelas, cupons, créditos em pontos usados como pagamento e tarifas de terceiros permanecem **fora de escopo** até contrato financeiro completo.

## 4. Cálculo de incentivo e limites

- Incentivo percentual: `custo_pontos = arredondar_para_centavos(valor_cobrado × percentual / 100)`, conforme versão das regras de pontos aplicável à oportunidade.
- Incentivo fixo em pontos: **política específica de custo unitário de concessão aprovada em 2026-10-19**, com custo de R$ 1,00 para o publicador por ponto concedido, conforme `opportunity-points-issuer-unit-cost-policy.md`. Não é paridade monetária universal, resgate, saque ou obrigação de pagar esse valor à Pessoa. Custo = quantidade inteira de pontos × R$1,00; percentual equivalente = 100 × custo / preço cobrado; mostrar esse percentual sem alterar a quantidade fixa originária.
- Validar `0 ≤ custo_pontos ≤ valor_cobrado`; percentuais, limites de saldo, condições e quantidade de pontos respeitam política de oportunidades.
- No incentivo fixo, a quantidade de pontos é aquela escolhida e seu custo monetário decorre da nova política específica. No incentivo percentual, calcular custo em BRL; **não prometer quantidade inteira de pontos derivada do custo decimal** até aprovar regra institucional de arredondamento/inteiros.

## 5. Fórmulas da simulação financeira BRL

`T = valor_venda_efetivamente_cobrado` (em centavos, T > 0).

`taxa_percentual = arredondar_para_centavos(T × 0,089)`.

`taxa_fixa = 0` se `T ≤ R$20,00`; senão `R$1,00`.

`taxa_guivos = taxa_percentual + taxa_fixa`.

`apos_pontos = T - custo_pontos`.

`repasse_estimado = apos_pontos - taxa_guivos - outras_deducoes_expressas`.

**Arredondamento:** valores monetários em centavos inteiros, arredondamento decimal HALF_UP nos cálculos monetários individualizados, política de arredondamento versionada. A taxa pode exceder o saldo líquido de transações de valores baixos com incentivos altos: **não realizar liquidação negativa silenciosa**; bloquear condições inviáveis para publicação e informar o motivo, ou tratar conforme política específica de pré-pagamento de incentivo e saldo, ainda pendente.

**Exemplo aprovado como ilustração, não tarifa definitiva:** T=R$200,00, percentual pontos=1% (custo R$2,00), após pontos R$198,00; taxa 8,9% × R$200,00 = R$17,80 + R$1,00 = R$18,80; repasse líquido estimado R$179,20, antes de outras deduções eventualmente aplicáveis.

**Exemplo microtransação:** T=R$10,00; sem pontos, taxa R$0,89; repasse R$9,11.

**Exemplo gratuita:** T=R$0,00; nenhuma venda paga sujeita à taxa. Regras de premiação em pontos com saldo pré-pago do Coletivo são independentes e preservadas.

## 6. Cadastro de oportunidade (versão de simulação)

Ao selecionar **Paga**, mostrar, junto da régua/campo de incentivo, um painel de cálculo reativo, legível e sem ambiguidade, com:
- `Preço de venda (Pessoa paga)`
- `Incentivo em pontos (custo do publicador)`
- `Valor após incentivo`
- `Taxa Guivos estimada: 8,9% + componente fixo quando aplicável`
- `Outras deduções`: se não houver contrato definido, declarar 'não incluídas nesta simulação', sem mostrar taxa fictícia
- `Repasse líquido estimado à Organização/Coletivo`

Campos dependentes do preço e percentual se atualizam ao alterar valor, opção 'Sem incentivo', 'Percentual do valor cobrado' ou 'Quantidade fixa de pontos', com cálculo automático dos pontos fixos pela regra específica de custo R$1,00 por ponto concedido, sem declarar esse valor como resgate do ponto; no modo percentual, manter a transparência sobre arredondamento/quantidade de pontos ainda não definida. No cadastro da oportunidade **gratuita**, evitar apresentar taxa de venda e preços como se houvesse cobrança. Salvar rascunhos mesmo sem plano se a pessoa responsável tiver autorização; requisitos de contratação continuam aplicados ao publicar oportunidades pagas.

Texto de transparência: `Simulação sujeita às regras comerciais aprovadas; taxas e valores definitivos serão informados antes da publicação e confirmação da venda.`

A interface de simulação **NÃO habilita cobrança**, repasse, criação de crédito monetário, emissão de documentos fiscais ou vínculo de contratos.

## 7. Regras pendentes da operação real

- Diferenciar venda capturada/aprovada, liquidada, reembolsada, cancelada, contestada e chargeback; reversões idempotentes de taxas/pontos; proibir dupla retenção e pontos indevidos.
- Versionar política comercial por transação, com congelamento do contrato da venda e trilha auditável.
- Definir se custos de gateway/adquirência, antifraude, impostos, saques, parcelamento, chargeback, reembolso e antecipação são absorvidos pela Guivos ou cobrados separadamente; **jamais inventar esses valores**.
- Distinguir custo da plataforma e custo de aquisição/geração de pontos, incluindo pré-pagamento e conferência de saldos.
- Validar documentação fiscal, Código de Defesa do Consumidor, transparência contratual, restrições de plano, preço mínimo e efeitos contábeis.
- Integração com checkout e backoffice somente após aprovação expressa do modelo e testes financeiros.

## 8. Gates

| Gate | Critério | Estado |
|---|---|---|
| GTAX-01 | Aprovação percentual e componente fixo, inclusão/isenções e política de microvendas | Aberto |
| GTAX-02 | Custos de processamento, tributos, margens e limites de negócio | Aberto |
| GTAX-03 | Contratos de planos e harmonização com política de pontos | Aberto |
| GTAX-04 | Reembolso, cancelamento, chargeback e reversão de pontos | Aberto |
| GTAX-05 | Precificação no cadastro/checkout, transparência, arredondamento e repasse | Aberto |
| GTAX-06 | Testes de cálculo, integração e auditoria | Aberto |
| GTAX-07 | Aprovação institucional e ativação de cobrança real | Aberto |

## 9. Governança

Proposta para seção de Monetização, Planos e Pagamentos do GKR, com entrada no MENU após revisão e merge. Prevalecem políticas de pontos e planos vigentes até decisão expressa que as modifique. Qualquer implementação imediata no Replit será **somente simulador não operacional**; não alterar taxas reais em checkout, lançamentos, contratos, relatórios produtivos ou pagamentos existentes.
