---
id: GKR-PONTOS-NAV-001
title: Pontos — Incentivos em Oportunidades
status: informational
version: 1.1.0
owner: Guivos
last_updated: 2026-10-15
normative: false
---

# Pontos — Incentivos em Oportunidades

> **Guia completo de consulta.** A autoridade econômica canônica de Pontos é [GKR-POINTS-ECONOMIC-AUTHORITY-001](points-economic-authority.md) (ativa e normativa). As configurações detalhadas de oportunidades e eventos são **propostas da PR #655 (DRAFT)**. Emissão, utilização no Mall/Travel, paridade e parâmetros comerciais **não estão autorizados** por este guia.

## 1. O que são Pontos Guivos?

Pontos Guivos são uma **unidade interna de benefício transacional**. O programa proposto permite que a Pessoa receba pontos em oportunidades elegíveis — principalmente quando **compra uma oportunidade paga de um ofertante que optou por participar do programa** — e futuramente os utilize em possibilidades pagas elegíveis, como **Guivos Mall e Guivos Travel**, após a aprovação dos contratos pertinentes.

**Pontos não são dinheiro**, saldo bancário, investimento, reputação, avaliação, mérito ou prova de evolução. Não podem, como regra atual, ser comprados pela Pessoa, transferidos ou convertidos em dinheiro. Não existe taxa oficial Pontos↔BRL.

## 2. Quem participa?

| Ator | Papel |
| --- | --- |
| **Pessoa** | Descobre/contrata oportunidades e pode se tornar elegível a pontos; futuro uso depende de contratos de resgate |
| **Organização ofertante** | Oferece oportunidade paga/gratuita e pode optar por financiar incentivos aos participantes |
| **Coletivo ofertante** | Também pode oferecer oportunidades e campanhas de incentivo, com autoridade de configuração ainda a reconciliar |
| **Guivos** | Governa elegibilidade, regras, rastreabilidade e contratos do programa; não presume cofinanciar os pontos oferecidos |
| **Mall / Travel** | Destinos futuros de utilização elegível, sujeitos a aceite, paridade, cobertura e liquidação próprios |

A **adesão do ofertante ao incentivo é opcional**; ausência de pontos não torna uma oportunidade inválida ou menos legítima.

## 3. Como funciona uma compra que gera pontos? (FIN-COMPRA)

**Fluxo funcional candidato — não implementado:**

1. O ofertante publica uma oportunidade **paga** e escolhe participar do programa de pontos.
2. Seleciona um **percentual em tabela de opções predefinidas pela Guivos** — catálogo e valores oficiais ainda não aprovados — e informa regras e limites.
3. A Pessoa vê preço, condições de participação e **prévia de pontos quando essa informação puder ser calculada legitimamente**.
4. A compra precisa ser confirmada mediante evidência confiável do fato gerador; clique, intenção, inscrição isolada ou link externo não comprovam pagamento.
5. A base elegível considera preço e descontos segundo contrato; percentual, custo econômico dos pontos, arredondamento e estornos exigem reconciliação.
6. **O ofertante financia 100% do custo dos pontos que oferece**. Em FIN-COMPRA, a direção estrutural é deduzir esse custo, contratualmente, do repasse devido ao ofertante; remuneração da Guivos é rubrica separada.
7. Cobertura, elegibilidade, validação, ledger e autorização de crédito precisariam ser confirmados **antes** de tornar pontos disponíveis à Pessoa.

**Exemplo conceitual, sem números oficiais:** uma Pessoa compra uma experiência de um ofertante aderente; a oportunidade traz um retorno percentual escolhido entre opções aprovadas. Após compra elegível, confirmação, apuração, financiamento e aprovação dos controles, a Pessoa poderia receber pontos. Não há taxa definida neste documento nem crédito real automático.

Uma compra paga **sem incentivo ativado** não gera pontos por essa modalidade.

## 4. Como funcionam premiações por eventos? (FIN-EVENTO)

Além de compras, o dossiê admite **modalidades candidatas adicionais** custeadas pelo ofertante, inclusive em eventos gratuitos:

| Modalidade | O que gera elegibilidade | Exemplo de regra possível |
| --- | --- | --- |
| **PCT — retorno percentual** | Compra elegível de oportunidade paga | Parcela da compra gera pontos conforme tabela governada |
| **FIX — participação** | Inscrição/participação conforme critério expressamente divulgado e comprovado | Quantidade fixa para cada Pessoa elegível |
| **RANK — classificação** | Resultado validado e regras de desempate/contestação | Quantidade por posição ou faixa |
| **CUSTOM — outra premiação** | Cumprimento de objetivo/condição autorizada e verificável | Regra específica e orçamento próprio |

Em FIN-EVENTO, a direção estrutural aceita prevê **orçamento pré-financiado por campanha**, separado da assinatura Business e de outras campanhas. A efetiva suficiência de lastro, valores, devoluções e direitos ainda precisa de ratificação.

### Limite de incentivo não é limite de inscrições

Um evento pode oferecer um incentivo às **primeiras N inscrições elegíveis**, enquanto mantém inscrições abertas para outras Pessoas. A última cota de benefício não pode ser reservada em duplicidade, e desistência não reabre automaticamente uma cota: isso exige regra divulgada.

**Exemplo estritamente ilustrativo:** 100 pontos para até 30 inscrições elegíveis representa teto nominal de 3.000 pontos **naquela modalidade**, independentemente do total de participantes. Não é oferta oficial, valor monetário nem prova de cobertura. Premiações por colocação teriam orçamento separado.

## 5. O que a Pessoa encontra no saldo de pontos?

A direção funcional aprovada prevê **um saldo unificado de Pontos Guivos por Pessoa**, com rastreabilidade interna por origem/lote, finalidade, evento gerador, financiador, validade, elegibilidade e regras de reversão.

Quando existir interface autorizada, devem ser distinguíveis:

| Estado | Significado |
| --- | --- |
| **Disponível** | Crédito validamente disponível para uso elegível, sujeito às regras pertinentes |
| **Reservado** | Comprometido em operação ou uso pendente; **não** aparece como disponível |
| **Utilizado** | Benefício já aplicado conforme regra e contrato |
| **Suspenso / em disputa** | Necessita decisão sobre elegibilidade ou integridade |
| **Revertido** | Crédito ajustado/estornado com causa e histórico |
| **Expirado** | Benefício vencido de acordo com regra previamente comunicada |

Ter um saldo unificado **não elimina a identificação de lotes** e tampouco cria um direito universal de gastar qualquer ponto em qualquer produto.

## 6. Como a Pessoa poderá usar pontos no Mall e no Travel?

A proposta prevê o uso de pontos **para adquirir ou acessar oportunidades pagas elegíveis**, inclusive:

- **Guivos Mall:** compras elegíveis poderão admitir pontos, isolados ou combinados com dinheiro, quando preço, estoque/oferta, cotação, regras de aceitação, cobertura, vendedor e liquidação forem aprovados.
- **Guivos Travel:** viagens e serviços turísticos elegíveis poderão admitir pontos, observadas cotação, disponibilidade, moeda, regras do fornecedor, reserva, cancelamento e reembolso.

**Pagamento misto (Pontos + dinheiro)** é direção funcional validada para possibilidades elegíveis, mas **não existe checkout ou resgate aprovado**. A existência de pontos no saldo não autoriza saque, transferência, pagamento de plano Journey ou aceitação irrestrita por parceiros.

A **paridade de utilização** (quantos pontos são necessários para um benefício) e o custo de financiamento são decisões **diferentes** e ambas carecem de parâmetros econômicos ratificados. Não presumir que determinado número de pontos equivale a R$ 1 ou outra quantia.

## 7. Quem paga pelos pontos e como a Guivos ganha dinheiro?

O incentivo proposto é **custeado integralmente pelo ofertante que o configurou**, sem subsídio implícito da Guivos.

| Rubrica | FIN-COMPRA | FIN-EVENTO |
| --- | --- | --- |
| Origem | Oportunidade paga elegível | Campanha/premiação de evento, gratuita ou paga |
| Financiador | Ofertante da compra | Organizador/ofertante da campanha |
| Financiamento | Dedução contratual do custo de pontos no repasse | Orçamento pré-financiado e segregado por campanha |
| Remuneração Guivos | Eventual taxa contratada, **separada** do custo dos pontos | Serviços/assinatura ou tarifa **separados**, quando aprovados |
| Status econômico | Preços, percentuais e cobertura pendentes | Parâmetros de garantia, devolução e encerramento pendentes |

Os [Planos Business](../plans/business.md) têm assinatura recorrente e capacidades incluídas conforme tier; **orçamento pré-pago de incentivo ≠ assinatura**. Não cobrar de novo capacidade já incluída nem classificar o recurso de incentivo automaticamente como receita da Guivos.

## 8. Cancelamento, estorno, validade e contestação

As regras canônicas exigem **motivo, autoridade, registro e possibilidade de contestação** em reversões. Situações candidatas incluem devolução de compra, erro, duplicidade, cancelamento de evento, evidência inválida, fraude comprovada e chargeback.

A direção de arredondamento **ROUND/P1** foi aprovada em 13/10/2026: HALF_EVEN, precisão de **0,01 ponto**, por fato gerador/ofertante, com aritmética decimal exata e reversão parcial cumulativa. Essa decisão **não libera a implementação**.

Proteções propostas:

- promessa/reserva de campanha **não é ponto disponível**;
- o valor já utilizado legitimamente não gera dívida automática da Pessoa em razão de um chargeback posterior;
- estorno parcial deve preservar histórico e evitar duplicidade;
- prazo numérico de validade **ainda não foi ratificado** e, quando aplicável, precisa ser informado antes da emissão;
- expiração de pontos não apaga histórico, progresso ou registros legítimos de participação.

## 9. O que os pontos não fazem?

- Não compram **selos**, reputação, relevância, posição orgânica, reconhecimento ou recomendação personalizada.
- Não são uma prova de que a Pessoa evoluiu nem um requisito para participar de oportunidades.
- Não são compráveis pela Pessoa na política atual.
- Não podem ser sacados, negociados ou transferidos por regra padrão.
- Não pagam **planos Journey** por inferência.
- Não são aceitos automaticamente em Mall/Travel antes de contratos próprios.

Veja [Selos — Reconhecimento e Reputação](selos-guia-consulta.md).

## 10. Situações práticas

**Compra elegível:** oferta aderente ao incentivo, compra comprovada, regra de percentuais aplicável e financiamento demonstrado → **candidato a crédito** após os gates econômicos; não emissão presente.

**Compra com devolução parcial:** recalcular direito sobre a base remanescente pela versão original da regra e conciliar reversão; não apagar o histórico.

**Evento gratuito com premiação por participação:** pode ser candidato a FIN-EVENTO, sem compra da Pessoa; requer orçamento, confirmação de participação e regras de elegibilidade.

**Corrida com classificação contestada:** premiação RANK controvertida não deve tornar-se disponível antes do resultado validado.

**Viagem no Travel:** visualizar saldo não basta para converter pontos em passagem; oferta, cotação, contratos, cobertura e cancelamento precisam ser autorizados.

Esses exemplos são explicações de produto proposto, **não funcionalidades lançadas ou promessas de resgate**.

## 11. Decisões aprovadas, abertas e bloqueios

| Objeto | Estado |
| --- | --- |
| Unidade única de pontos, saldo unificado e lotes rastreáveis | Direção funcional/canônica vigente |
| Natureza não monetária, não transferência e não conversibilidade | Defaults econômicos ativos |
| Opcionalidade dos incentivos e custeio integral pelo ofertante | Direção de produto preservada no dossiê |
| FIN-COMPRA (dedução do repasse) / FIN-EVENTO (pré-financiamento) | Direção estrutural aceita; parâmetros abertos |
| ROUND/P1: HALF_EVEN, 0,01 ponto | Direção de política aprovada; sem implementação |
| Percentuais PCT e base elegível definitiva (P4) | Sem ratificação integral |
| Taxas, remuneração e repasses (P5) | Sem parâmetros comerciais finais |
| Valor de utilização PAR-02/P2 | **Sem taxa oficial** |
| Cobertura/obrigações e responsabilidade econômica (COVER/P6/P9) | Evidência material insuficiente para ratificação |
| Aceitação no Mall/Travel (LIQ-01/P7, LIQ-02/P8) | Contratos próprios pendentes |
| 16 cenários E2E | Especificados; **0 executados** conforme dossiê |
| Emissão, carteira operacional, resgate e implementação | **Não autorizados** |

## 12. Perguntas frequentes

**Toda oportunidade paga gera pontos?** Não. O ofertante deve optar pelo incentivo e cumprir as condições elegíveis; além disso, o programa operacional ainda depende de autorização.

**Quem escolhe a quantidade de pontos?** Para retorno percentual, a proposta é selecionar percentual de uma tabela governada pela Guivos; para eventos, definir premiações e limites conforme regulamento e orçamento. Os valores não são oficiais.

**Pontos servem para comprar no Mall e viajar?** É o destino funcional pretendido, **não uma aceitação já habilitada**. Cada produto exige contratos próprios.

**Os pontos representam reais?** Não existe relação monetária canônica aprovada, nem saque ou conversibilidade em espécie.

**Posso ganhar um selo por gastar mais?** Não. São conceitos e autoridades distintos.

**Uma empresa precisa contratar Business para oferecer pontos?** A elegibilidade dos ofertantes por contexto deve obedecer ao contrato aplicável; não presumir que a contratação Business seja condição universal das oportunidades, nem que os planos de participantes se confundam com os tiers Business.

## 13. Fontes e aprofundamento

1. **Autoridade vigente:** [Pontos Guivos — Autoridade Econômica Canônica](points-economic-authority.md).
2. **Modelo econômico:** [Índice GEM e políticas relacionadas](index.md).
3. **Proposta completa de oportunidades, incentivos e premiações:** [PR #655 (DRAFT)](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/655).
4. **Decisões, pendências e evidências econômicas:** [Issue #661](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/issues/661).
5. **Produtos de utilização pretendida:** [Guivos Mall](../product-architecture/mall.md) e [Guivos Travel](../product-architecture/travel.md).
6. **Contratação e separação do orçamento de incentivo:** [Planos Business](../plans/business.md).
7. **Registro de maturidade:** [Estado Atual do GKR](../project/current-state-register.md).

> **Regra editorial:** este guia é explicativo e não cria taxas, carteira, política de resgate ou autorização de operação. No conflito entre uma proposta e a autoridade econômica vigente, prevalece a autoridade canônica ativa.