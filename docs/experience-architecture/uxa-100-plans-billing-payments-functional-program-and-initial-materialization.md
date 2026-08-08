---
id: UXA-100
title: Programa Funcional, Materialização, Validação e Promoção de Planos, Cobrança e Pagamentos
status: draft
version: 0.5.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-UPGRADE-DOWNGRADE-CANCELLATION-POLICY-001
  - GEM-COMMERCIAL-BASELINE-001
  - GEM-003-PAYER-BENEFICIARY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - UXA-011-A1
  - UXA-070
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GKR-STATE-001
normative: false
---

# Programa Funcional, Materialização, Validação e Promoção de Planos, Cobrança e Pagamentos

## 1. Finalidade

A UXA-100 estrutura, materializa, valida e registra canonicamente a experiência documental de **planos, comparação de benefícios, cobrança, pagamento e ciclo de vida comercial** para:

- Pessoa;
- Coletivo;
- Organização.

A frente deriva da baseline comercial candidata do GEM-004. Ela **não autoriza oferta pública, cobrança real, gateway, implantação, desenvolvimento, política fiscal final ou publicação de preços como oferta vigente**.

A versão 0.5.0 consolida:

- `UXA-100-A1` — telas dedicadas de Planos e integração às três jornadas;
- `UXA-100-A2` — auditoria funcional dos nove SVGs, com 9/9 aprovados após reforma controlada de seis;
- `UXA-100-A3` — fragmentação mínima e promoção canônica de superfícies, transições, galeria e rastreabilidade.

## 2. Pergunta funcional

A experiência deve responder, sem coerção:

> **Qual plano está ativo, o que ele inclui, qual limite foi alcançado, quais alternativas gratuitas permanecem válidas, o que muda ao escolher outro plano, quem paga e quem recebe o benefício, qual é a recorrência e o que acontece em sucesso, falha, downgrade ou cancelamento?**

Para a Pessoa existe uma obrigação adicional:

> **Como limitar correspondências personalizadas do Guivos Free sem esconder oportunidades públicas nem transformar pagamento em condição para descobrir oportunidades?**

## 3. Autoridades e limites preservados

### 3.1 Baseline comercial candidata

A UXA-100 usa somente referências já documentadas em GEM-004-A1 e GEM-004-A2. Valores exibidos permanecem **preços candidatos para simulação documental**.

### 3.2 Oportunidade pública não é ofuscada

O limite do Guivos Free recai sobre uma **correspondência personalizada adicional após a cota semanal**, não sobre a existência da oportunidade pública.

Permanecem disponíveis, conforme regras públicas aplicáveis:

- Explorar;
- Mapa;
- catálogo público;
- informações públicas essenciais;
- segurança, preço, prazo e responsabilidade da oferta quando publicamente acessíveis.

É proibido ocultar ou desfocar oportunidade pública para pressionar upgrade.

### 3.3 Pagamento não altera relevância

Plano pago não eleva posição orgânica, relevância funcional, veracidade, confiança, legitimidade, impacto ou evolução humana.

### 3.4 Assinatura é distinta de transação

```text
assinatura da plataforma
≠ preço de atividade ou oportunidade
≠ comissão
≠ taxa do meio de pagamento
≠ tributo
```

### 3.5 Parâmetros não definidos

A UXA-100 não inventa:

- gateway ou adquirente;
- bandeira, PIX, boleto ou carteira oficial;
- tokenização;
- prazo de tolerância após falha;
- pró-rata ou crédito entre ciclos;
- política fiscal/tributária definitiva;
- trial com conversão automática.

Nos wireframes, pagamento aparece apenas como **método autorizado em simulação**.

## 4. Decisão estrutural e fragmentação

Planos e cobrança não usam `COM-*`, pois `COM-*` permanece reservado ao Opportunity Boost/publicidade.

A UXA-100-A3 aplica os critérios de fragmentação da UXA-059: estado somente recebe identidade própria quando muda materialmente hierarquia, decisão, autoridade, público, dados, consequência, risco, continuidade, canal ou recuperação.

Por participante existem quatro famílias canônicas:

1. **`*-301 — Planos e comparação`**;
2. **`*-302 — Revisão de contratação`**;
3. **`*-303 — Gestão de downgrade e cancelamento`**;
4. **`*-304 — Resultado e recuperação`**.

Não recebem superfície própria:

- comparação incremental isolada — permanece em `*-301`;
- processamento de pagamento — permanece transitório entre revisão e resultado;
- mensagens simples de confirmação;
- periodicidade mensal/anual como tela separada;
- preview contextual de limite;
- Enterprise/Scale como checkout.

A fronteira compartilhada `BND-002` representa somente a saída para processo comercial Enterprise/Scale.

## 5. Espinha dorsal transversal canônica

```text
*-301 Planos e comparação
├── upgrade
│   → *-302 revisão de contratação
│   → *-304 resultado/recuperação
│   → *-301 estado reconciliado
├── downgrade/cancelamento
│   → *-303 revisão do ciclo e consequências
│   → *-304 resultado/recuperação
│   → *-301 estado reconciliado
└── Enterprise/Scale
    → BND-002 processo comercial governado
```

As transições internas da frente são localmente validadas. `TRN-416` e `TRN-426` permanecem parciais porque o processo posterior a `BND-002` não foi materializado.

## 6. Comparação entre planos

A experiência possui duas leituras complementares:

- **matriz geral**, com todos os planos e capacidades;
- **delta incremental**, mostrando somente o que o plano superior acrescenta ao imediatamente inferior.

```text
plano superior
= tudo o que permanece do plano anterior
+ benefícios/capacidades adicionais deste degrau
```

Benefícios herdados não são reapresentados como novidades.

Quando plano atual e alvo são conhecidos, a interface também apresenta o **delta direto atual → escolhido**. Exemplo: `Free → Pro` consolida Plus + Pro sem exigir soma mental das colunas.

No downgrade, a regra se inverte: a revisão destaca exatamente o que deixa de existir ou terá limite reduzido.

## 7. Entradas nas jornadas

Existem dois pontos legítimos de entrada:

```text
entrada voluntária
Conta / Administração / Configurações
→ Planos
```

```text
entrada contextual
limite legítimo atingido
→ alternativas gratuitas/operacionais aplicáveis
→ comparar planos
→ Planos
```

O participante **não precisa atingir limite** para consultar ou administrar seu plano.

A UXA-100-A3 não inventa transições de origem quando `Conta/Configurações`, publicação ou correspondência personalizada ainda não possuem identidade canônica suficiente para esse handoff.

## 8. Pessoa

### 8.1 Planos candidatos

| Plano | Mensal | Anual | Correspondências personalizadas completas |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | 2 por semana |
| Guivos Plus | R$ 24,90 | R$ 249,00 | sem cota semanal fixa, sujeito a uso justo |
| Guivos Pro | R$ 49,90 | R$ 499,00 | sem cota semanal fixa, com análise ampliada |

### 8.2 Free com cota esgotada

Após duas correspondências completas abertas na semana, uma correspondência adicional pode preservar categoria, modalidade, localidade, prazo, natureza gratuita/paga, indicação de relação autorizada e período de renovação, enquanto limita a camada personalizada adicional.

Devem permanecer acessíveis: `Explorar oportunidades públicas`, `Ver no Mapa` e `Conhecer o Guivos Plus`.

### 8.3 Superfícies e transições

- `PER-301` — Planos e comparação;
- `PER-302` — revisão de contratação;
- `PER-303` — downgrade/cancelamento;
- `PER-304` — resultado/recuperação;
- `TRN-401` a `TRN-405` — localmente validadas.

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

## 9. Coletivo

### 9.1 Planos candidatos

| Plano | Mensal | Anual | Atividades/mês | Oportunidades/mês | Ativas | Publicação paga |
|---|---:|---:|---:|---:|---:|---|
| Livre | R$ 0,00 | R$ 0,00 | 1 gratuita | 1 gratuita | 2 | não |
| Gestão | R$ 89,90 | R$ 899,00 | 4 | 4 | 6 | sim |
| Impacto | R$ 249,90 | R$ 2.499,00 | 15 | 15 | 20 | sim |
| Enterprise | sob consulta | contrato anual | capacidade contratada | capacidade contratada | capacidade contratada | sim |

Ao atingir cota ou tentar publicação paga, permanecem publicações existentes, rascunho, opção de aguardar ciclo, encerramento/agendamento quando aplicável e alternativa gratuita funcionalmente possível.

Antes do downgrade, o Coletivo trata publicações pagas/gratuitas, administradores, núcleos/unidades, compromissos e exportação. Não existe exclusão silenciosa.

### 9.2 Superfícies e transições

- `COL-301` — Planos e comparação;
- `COL-302` — revisão de contratação;
- `COL-303` — downgrade/cancelamento;
- `COL-304` — resultado/recuperação;
- `TRN-411` a `TRN-415` — localmente validadas;
- `TRN-416` — parcial até processo Enterprise posterior a `BND-002`.

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

## 10. Organização

### 10.1 Planos candidatos

| Plano | Mensal | Anual | Novas oportunidades/programas | Ativas | Administradores | Unidades |
|---|---:|---:|---:|---:|---:|---:|
| Business Start | R$ 299,00 | R$ 2.990,00 | 10/mês | 15 | 3 | 1 |
| Business Growth | R$ 799,00 | R$ 7.990,00 | 50/mês | 75 | 10 | até 5 |
| Business Scale | a partir de R$ 1.990,00/mês | contrato anual | capacidade contratada | capacidade contratada | conforme contrato | múltiplas |

Quando a Organização atinge capacidade, devem permanecer visíveis limite, consumo, período de renovação, efeito exato do upgrade e alternativas de arquivar/agendar/manter rascunho quando aplicáveis.

Antes do downgrade, seleciona unidades, administradores, publicações e Coletivos relacionados mantidos, integrações a encerrar e dados a exportar. Históricos/agregados não são apagados para forçar retenção.

### 10.2 Superfícies e transições

- `ORG-301` — Planos e comparação;
- `ORG-302` — revisão de contratação;
- `ORG-303` — downgrade/cancelamento;
- `ORG-304` — resultado/recuperação;
- `TRN-421` a `TRN-425` — localmente validadas;
- `TRN-426` — parcial até processo Scale posterior a `BND-002`.

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

## 11. Pagador e beneficiário

Toda revisão de contratação distingue explicitamente pagador, beneficiário, autoridade de cancelamento e escopo de dados necessário à cobrança.

Pagamento por terceiro não transfere automaticamente autoridade, acesso à jornada pessoal, dados sensíveis ou poder de alterar relevância/recomendação.

## 12. Resultado, falha e recuperação

`*-304` agrupa sucesso e falha porque ambos pertencem à responsabilidade de resultado/recuperação, mas as consequências permanecem distintas.

Falha informa:

- pagamento não confirmado;
- ativação não presumida;
- plano/estado anterior identificável;
- direitos essenciais preservados;
- caminho para tentar novamente/revisar método;
- ausência de duplicação por simples repetição da intenção.

A UXA-100 não define `grace_period`.

## 13. Downgrade e cancelamento

`*-303` mostra estado atual/futuro, capacidades perdidas/reduzidas, excedentes a tratar, data efetiva e alternativas de retorno. Cancelamento interrompe renovação futura, confirma plano posterior e não reativa sem autorização.

A UXA-100 não presume pró-rata, estorno ou crédito entre ciclos.

## 14. Materialização visual canônica

### 14.1 Telas dedicadas

- `uxa-100-person-plans-screen-mobile.svg`;
- `uxa-100-collective-plans-screen-desktop.svg`;
- `uxa-100-organization-plans-screen-desktop.svg`.

### 14.2 Boards de fluxo

- `uxa-100-person-plans-payments-flow-board.svg`;
- `uxa-100-collective-plans-payments-flow-board.svg`;
- `uxa-100-organization-plans-payments-flow-board.svg`.

### 14.3 Comparações incrementais

- `uxa-100-person-plan-incremental-benefits-comparison.svg`;
- `uxa-100-collective-plan-incremental-benefits-comparison.svg`;
- `uxa-100-organization-plan-incremental-benefits-comparison.svg`.

Inspeção: [Planos, Comparação e Cobrança — Galeria Canônica](../journeys/screen-gallery-plans-billing.md).

Os nove SVGs pertencem aos perfis `R29`, `R30` e `R31` e elevam o conjunto canônico para **118 SVGs / 118 associações / 31 perfis**.

## 15. Resultado da validação e promoção

A UXA-100-A2 confirmou:

- 9/9 SVGs funcionalmente aprovados;
- 6 reformulados controladamente;
- 3 comparações incrementais preservadas sem reforma;
- 0 pendências específicas após a auditoria.

A UXA-100-A3 promove:

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **118** |
| associações | **118** |
| perfis | **31** |
| validações funcionais vigentes | **118** |
| pendências específicas | **0** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| IDs com referência visual | **42** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela | **2** |

## 16. Fora do escopo

A UXA-100 não:

- altera a baseline econômica do GEM-004;
- valida preços no mercado;
- cria checkout real, gateway, nota fiscal, pró-rata, crédito ou grace period;
- implementa entitlement;
- publica oferta comercial;
- materializa o processo posterior a `BND-002`;
- promove Pessoa, Coletivo ou Organização para `active`;
- inicia protótipo ou Engenharia de Produto.

## 17. Estado da frente

A UXA-100 permanece `draft` como programa documental, mas suas materializações e identidades foram promovidas canonicamente pela UXA-100-A3 dentro dos registros governados.

A distinção é obrigatória:

```text
programa UXA-100 em draft
≠ ativos sem autoridade
```

Os 9 SVGs, 12 superfícies e 17 transições possuem agora identidade canônica no branch da PR #200, com maturidade explícita.

A existência documental não constitui integração à `main`, lançamento, cobrança, implementação ou operação. Nenhuma próxima UXA é iniciada automaticamente.