---
title: Incentivos em Pontos Guivos — Custo Unitário ao Publicador
version: 1.0.0
status: approved_for_design_and_simulation
decision_date: 2026-10-19
scope: Organizações e Coletivos; cadastro de oportunidades pagas
---

# Custo de concessão de Pontos Guivos em oportunidades

## Decisão de produto — 2026-10-19

Fica aprovada, **para cálculo de incentivo e simulação de repasse no cadastro de oportunidades**, a equivalência de **1 ponto concedido = R$ 1,00 de custo para a Organização ou Coletivo que financia a concessão**. Isto permite converter tanto incentivos em quantidade fixa quanto incentivos em percentual do preço em uma única unidade econômica de custo suportado pelo publicador.

**Atenção, escopo semântico:** o R$ 1,00 constitui o **custo unitário de concessão de ponto ao publicador**, NÃO valor monetário de resgate, cotação, crédito sacável, meio de pagamento, paridade universal POINTS ↔ BRL, ativo ou promessa à Pessoa. A Guivos não passa a dever R$ 1,00 à Pessoa por ponto. A autoridade econômica canônica de pontos, que não define taxa de conversão monetária universal, permanece íntegra fora desta precificação operacional específica. Mudanças na autoridade canônica, custeio real, tesouraria, custódia ou resgates exigem decisões institucionais adicionais.

Aprovação cobre **documentação e simulador de cadastro do Replit**. Não ativa venda de pontos, transferência financeira, distribuição efetiva, saldo pré-pago, passivo, checkout ou pagamento real. Reconciliar com a política conceitual de pontos e créditos, pontos em premiações de Coletivos e com planos antes de qualquer ativação produtiva.

## Fórmulas dos incentivos em oportunidade paga

Definições: `P` = preço cobrado da Pessoa em BRL, `Q` = quantidade inteira de pontos, `r` = incentivo percentual expresso em %, `C` = custo de concessão do incentivo em BRL.

- **Quantidade fixa:** `C = Q × R$ 1,00` e `r_equivalente = 100 × C / P`, quando `P > 0`. A régua e o campo percentual equivalente refletem este valor, mas não substituem a origem escolhida (continua `Quantidade fixa`).
- **Percentual do valor cobrado:** `C = arredondar_centavos(P × r / 100)`, e `Q` deve ser calculado somente após definição institucional da política de inteiros/fracionários e arredondamento de pontos. **Não prometer Q pontos a partir de C decimal se essa regra não existir.** Até lá, o simulador pode mostrar custo em BRL e informar que a quantidade de pontos aguarda arredondamento formal.
- **Sem incentivo:** `C = 0`, `Q = 0`, `r_equivalente = 0`.
- **Valor após incentivo:** `A = P − C`.
- **Taxa Guivos para simulação (PR #712):** para `0 < P ≤ R$20`, `T = arredondar_centavos(0,089 × P)`; para `P > R$20`, `T = arredondar_centavos(0,089 × P) + R$1,00`. Para oportunidade gratuita, sem venda, `T = 0`.
- **Repasse líquido estimado:** `L = A − T − outras_deduções_contratadas_discriminadas`. Jamais confundir `A` com `L`.
- **Limite de incentivo:** bloquear finalização/publicação se `C > P`; não permitir simular repasse negativo como repasse pagável, exibir aviso de inviabilidade e preservar rascunho.
- **Precisão:** armazenar/cacular monetários em centavos com arredondamento decimal explícito; exibir taxa e componentes separadamente, formato pt-BR.

O percentual equivalente pode possuir precisão maior que o passo de 0,1% da régua, portanto mostrar precisão suficiente para não induzir erro e não arredondar o percentual armazenado de forma que altere o **custo determinado pela quantidade fixa**. No modo fixo, a quantidade Q permanece a fonte de verdade, e a régua é indicação equivalente, não pode alterar Q sem mudança explícita de modalidade ou interação definida para isso.

## Exemplo validado de cálculo — Coletivo ou Organização

Preço `P = R$1.000,00`, incentivo fixo `Q = 10 pontos`:
- Custo dos pontos: **R$10,00**.
- Percentual equivalente: **1%**.
- Valor após incentivo: **R$990,00**.
- Taxa percentual Guivos simulada 8,9%: **R$89,00**; tarifa fixa **R$1,00**, total **R$90,00**.
- Repasse líquido estimado: **R$900,00**.

Exemplo `P = R$200,00`, `Q = 2 pontos`: C = R$2,00; r = 1%; taxa = R$18,80; repasse estimado = **R$179,20**.

## UX e consistência de dados

Na seção `Incentivo em Pontos Guivos`, ao escolher `Quantidade fixa de pontos`, o campo Q inteiro é editável e todo o resumo financeiro recalcula imediatamente: `Percentual equivalente da oportunidade`, `Quantidade de pontos`, `Custo dos pontos (R$)`, `Valor após incentivo`, `Taxa Guivos percentual`, `Tarifa fixa`, `Taxa Guivos total` e `Repasse líquido estimado à Organização/ao Coletivo`. Remover mensagens desatualizadas sobre ausência de paridade de **custo de concessão**. Manter aviso claro: `1 ponto concedido tem custo de R$ 1,00 para quem publica; não representa valor de resgate do ponto.`

Preservar seleção e recálculo ao alternar modos, editar preço, salvar e reabrir rascunho; mesma regra para Organização e Coletivo. Exibir limitações honestas para quantidade de pontos decorrente de percentual quando política de arredondamento não estiver definida. A opção `Gratuita` não deve gerar taxa de venda, sem prejudicar regras distintas de eventos com premiação e orçamento pré-pago.

## Controles e dependências

1. **Produto:** autorizar eventual ativação do custeio unitário em cobranças reais somente após testes econômicos, limites e política de saldo, incluindo elegibilidade do plano.
2. **Financeiro/Jurídico:** confirmar natureza contratual de custo de concessão, encargos, estornos, chargeback e tributos.
3. **Governança de pontos:** resolver quantidade inteira/fracionária no modo percentual, arredondamento e comunicação ao usuário; compatibilizar com premiação em pontos.
4. **Engenharia:** versionamento de regra, cálculo determinístico, persistência, reconciliação e auditoria, não liberar emissão real de pontos via simulador.
5. **GKR:** referenciar a política em Planos/Pontos/Oportunidades e MENU após incorporação, sem alterar a autoridade geral de resgate.

**Estado:** aprovada para especificação e simulação; operação financeira real não habilitada.
