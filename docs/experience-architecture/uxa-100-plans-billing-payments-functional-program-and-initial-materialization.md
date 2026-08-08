---
id: UXA-100
title: Programa Funcional e Materialização Inicial de Planos, Cobrança e Pagamentos
status: draft
version: 0.4.0
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
  - GKR-STATE-001
normative: false
---

# Programa Funcional e Materialização Inicial de Planos, Cobrança e Pagamentos

## 1. Finalidade

A UXA-100 abre uma frente transversal para tornar compreensíveis, em baixa fidelidade, os fluxos de **plano, comparação de benefícios, cobrança, pagamento e efeito de limites comerciais** para os três participantes estruturais da Guivos:

- Pessoa;
- Coletivo;
- Organização.

A frente deriva da baseline comercial candidata do GEM-004. Ela **não autoriza oferta pública, checkout real, cobrança, gateway, implantação, desenvolvimento ou publicação de preços como proposta comercial vigente**.

A versão 0.4.0 incorpora:

- `UXA-100-A1` — telas dedicadas de Planos e integração da etapa às três jornadas;
- `UXA-100-A2` — auditoria funcional dos nove SVGs candidatos, com aprovação após reformulação controlada de seis ativos.

## 2. Pergunta funcional

A experiência deverá responder, sem coerção:

> **Qual plano está ativo, o que ele inclui, qual limite foi alcançado, quais alternativas gratuitas permanecem válidas, o que muda ao escolher outro plano, quem paga e quem recebe o benefício, qual é a recorrência e o que acontece em sucesso, falha, downgrade ou cancelamento?**

Para a Pessoa existe uma pergunta adicional obrigatória:

> **Como limitar correspondências personalizadas do Guivos Free sem esconder oportunidades públicas nem transformar pagamento em condição para descobrir oportunidades?**

## 3. Autoridades e limites preservados

### 3.1 Baseline comercial candidata

A UXA-100 materializa somente referências já documentadas em GEM-004-A1 e GEM-004-A2. Os valores exibidos nos wireframes são **preços candidatos para simulação documental**.

### 3.2 Oportunidade pública não é ofuscada

O estado visual limitado do Guivos Free recai sobre uma **correspondência personalizada adicional após a cota semanal**, não sobre a existência da oportunidade pública.

A experiência preserva catálogo público no Explorar, Mapa, informações públicas essenciais, segurança, preço da oportunidade, prazo e responsabilidade quando a oferta já estiver acessível publicamente.

É proibido desfocar uma oportunidade pública apenas para ocultar sua existência e pressionar upgrade.

### 3.3 Pagamento não altera relevância

Plano pago não poderá elevar posição orgânica, alterar relevância funcional, aumentar veracidade ou confiança institucional, representar evolução humana superior ou ocultar alternativa gratuita legítima.

### 3.4 Assinatura é distinta de transação

```text
assinatura da plataforma
≠ preço de atividade ou oportunidade
≠ comissão
≠ taxa do meio de pagamento
≠ tributo
```

### 3.5 Parâmetros não definidos

A UXA-100 não inventa gateway ou adquirente, bandeira, PIX, boleto ou carteira oficial, tokenização, prazo de tolerância após falha, pró-rata, crédito entre ciclos, data fiscal definitiva, política tributária ou trial com conversão automática.

Nos wireframes, pagamento aparece apenas como **método autorizado em simulação**.

## 4. Decisão estrutural

Planos e cobrança não serão inseridos em `COM-*`, pois a família `COM-*` vigente representa Opportunity Boost/publicidade.

A UXA-100 também não cria ainda IDs canônicos de superfície ou transição.

O conjunto candidato é formado por **nove SVGs**:

1. três telas dedicadas de Planos;
2. três placas de fluxo de planos/pagamentos;
3. três comparações incrementais.

A UXA-100-A2 confirmou a coerência funcional dos nove ativos como candidatos. Uma etapa posterior ainda deverá decidir quantas superfícies canônicas devem existir, quais estados merecem SVG separado, quais IDs serão registrados e quais transições serão integradas ao registro global.

## 5. Espinha dorsal transversal

```text
área da conta/administração
→ Planos
→ plano atual + uso/capacidade
→ comparação voluntária
→ matriz geral + delta incremental
→ seleção afirmativa, sem pré-seleção
→ revisão da contratação
→ pagador + beneficiário
→ preço + periodicidade + recorrência + data de início
→ método autorizado em simulação
→ confirmar
→ processamento
├── sucesso → ativação rastreável + confirmação
└── falha → nenhuma ativação presumida + recuperação

plano ativo
→ downgrade ou cancelamento
→ revisar consequência, capacidades excedentes e data aplicável
→ confirmar
→ registrar estado futuro
```

Quando houver alternativa Enterprise/Scale:

```text
comparar plano
→ necessidade contratual
→ solicitar proposta comercial
→ processo comercial governado
```

Não haverá checkout autônomo fictício para Enterprise/Scale.

## 6. Regra de comparação entre planos

A experiência possui duas leituras complementares:

- **matriz geral**, com todos os planos e capacidades;
- **delta incremental**, mostrando o que cada plano superior acrescenta ao imediatamente inferior.

```text
plano superior
= tudo o que permanece do plano anterior
+ benefícios/capacidades adicionais deste degrau
```

Benefícios herdados não são repetidos como se fossem novos.

Quando o plano atual for conhecido, a interface deverá também mostrar o **delta direto plano atual → plano escolhido**. Exemplo: `Free → Pro` consolida os incrementos de Plus e Pro sem obrigar a Pessoa a reconstruir a diferença entre colunas.

No downgrade, a regra é invertida: a revisão destaca exatamente quais capacidades deixarão de existir ou terão limite reduzido antes da confirmação.

## 7. Planos como etapa das jornadas

A UXA-100-A1 inclui Planos como etapa transversal candidata das três jornadas.

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

A existência desta etapa na jornada não equivale a promoção da jornada nem criação de superfície/transição canônica.

## 8. Pessoa

### 8.1 Planos candidatos

| Plano | Mensal | Anual | Correspondências personalizadas completas |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | 2 por semana |
| Guivos Plus | R$ 24,90 | R$ 249,00 | sem cota semanal fixa, sujeito a uso justo |
| Guivos Pro | R$ 49,90 | R$ 499,00 | sem cota semanal fixa, com análise ampliada |

### 8.2 Estado Free com cota esgotada

Após duas correspondências completas abertas na semana, uma correspondência adicional poderá manter visíveis categoria, modalidade, localidade, prazo, natureza gratuita ou paga, indicação de relação com contexto autorizado e período de renovação da cota.

Poderão permanecer limitados na correspondência personalizada: identidade completa da correspondência personalizada, justificativa detalhada, análise de aderência, relação ampliada com Momento Atual e Próximo Passo e comparação personalizada.

Devem permanecer acessíveis no mesmo estado: `Explorar oportunidades públicas`, `Ver no Mapa` e `Conhecer o Guivos Plus`.

### 8.3 Tela dedicada de Planos

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

### 8.4 Compra e mudança

A Pessoa revisa plano escolhido, preço candidato, mensal/anual, recorrência, pagador, beneficiário, data de início, método autorizado em simulação, downgrade/cancelamento e ausência de promessa de resultado.

## 9. Coletivo

### 9.1 Planos candidatos

| Plano | Mensal | Anual | Atividades/mês | Oportunidades/mês | Ativas | Publicação paga |
|---|---:|---:|---:|---:|---:|---|
| Livre | R$ 0,00 | R$ 0,00 | 1 gratuita | 1 gratuita | 2 | não |
| Gestão | R$ 89,90 | R$ 899,00 | 4 | 4 | 6 | sim |
| Impacto | R$ 249,90 | R$ 2.499,00 | 15 | 15 | 20 | sim |
| Enterprise | sob consulta | contrato anual | capacidade contratada | capacidade contratada | capacidade contratada | sim |

### 9.2 Limite no Coletivo Livre

Ao atingir cota ou tentar publicação paga, a superfície preserva publicações existentes, rascunho, opção de aguardar próximo ciclo, encerramento/agendamento quando aplicável, alternativa gratuita quando funcionalmente possível e comparação voluntária com Gestão/Impacto.

### 9.3 Tela dedicada de Planos

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

### 9.4 Enterprise

Enterprise utiliza solicitação de proposta comercial e dimensionamento; não recebe checkout autônomo fictício.

### 9.5 Downgrade

Antes da efetivação, o Coletivo escolhe publicações gratuitas que permanecerão, encerra/converte publicações pagas excedentes, reduz administradores/núcleos conforme limite e preserva compromissos, exportação e registros aplicáveis. Não há exclusão silenciosa.

## 10. Organização

### 10.1 Planos candidatos

| Plano | Mensal | Anual | Novas oportunidades/programas | Ativas | Administradores | Unidades |
|---|---:|---:|---:|---:|---:|---:|
| Business Start | R$ 299,00 | R$ 2.990,00 | 10/mês | 15 | 3 | 1 |
| Business Growth | R$ 799,00 | R$ 7.990,00 | 50/mês | 75 | 10 | até 5 |
| Business Scale | a partir de R$ 1.990,00/mês | contrato anual | capacidade contratada | capacidade contratada | conforme contrato | múltiplas |

### 10.2 Limite e alternativas

Quando a Organização atingir capacidade, deverão estar visíveis limite e consumo atual, período de renovação, efeito exato do upgrade, arquivar/agendar/manter rascunho quando aplicável e separação entre capacidade comercial e relevância das oportunidades.

### 10.3 Tela dedicada de Planos

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

### 10.4 Business Scale

Scale utiliza processo comercial solicitado pela Organização, com proposta e capacidade contratada. Não há checkout autônomo simulado como se preço e escopo fossem autoatendimento definitivo.

### 10.5 Downgrade

Antes da efetivação, a Organização seleciona unidades, administradores, publicações e Coletivos relacionados mantidos, identifica integrações a encerrar e dados a exportar e recebe a data efetiva/plano posterior. Históricos e agregados não são apagados para forçar retenção.

## 11. Pagador e beneficiário

Toda revisão de contratação distingue explicitamente quem paga, quem recebe o benefício do plano, quem poderá cancelar e qual escopo de dados é necessário à cobrança.

Pagamento por terceiro não transfere automaticamente autoridade, acesso à jornada pessoal, acesso a dados sensíveis ou poder de alterar relevância, recomendação ou resultado.

## 12. Falha de pagamento

A simulação de falha informa pagamento não confirmado, ativação não presumida, plano/estado anterior identificável, acesso gratuito e direitos essenciais preservados, caminho para tentar novamente/revisar método e ausência de duplicação de cobrança por simples reenvio da mesma intenção.

A UXA-100 não define duração de `grace_period`.

## 13. Downgrade e cancelamento

A experiência fica na mesma área de Plano e cobrança, mostra estado atual e futuro, explica capacidades que deixarão de estar disponíveis, trata explicitamente capacidades excedentes, preserva dados/direitos/acesso gratuito aplicável, exige confirmação afirmativa e emite evidência da solicitação.

Cancelamento mostra data efetiva, interrompe renovação futura, confirma plano posterior e não reativa sem autorização.

A UXA-100 não presume pró-rata, estorno ou crédito entre ciclos.

## 14. Materialização candidata

### 14.1 Telas dedicadas de Planos

- `uxa-100-person-plans-screen-mobile.svg`;
- `uxa-100-collective-plans-screen-desktop.svg`;
- `uxa-100-organization-plans-screen-desktop.svg`.

### 14.2 Placas de fluxo

- `uxa-100-person-plans-payments-flow-board.svg`;
- `uxa-100-collective-plans-payments-flow-board.svg`;
- `uxa-100-organization-plans-payments-flow-board.svg`.

### 14.3 Comparações incrementais

- `uxa-100-person-plan-incremental-benefits-comparison.svg`;
- `uxa-100-collective-plan-incremental-benefits-comparison.svg`;
- `uxa-100-organization-plan-incremental-benefits-comparison.svg`.

Inspeção integrada: [Planos, Comparação e Cobrança — Galeria Candidata](../journeys/screen-gallery-plans-billing.md).

Os **9 SVGs são candidatos e não elevam os 109 SVGs canônicos** até promoção governada posterior.

## 15. Resultado da validação funcional candidata

A UXA-100-A2 confirmou os critérios funcionais previstos para os nove SVGs:

1. alternativa gratuita permanece visível e funcional;
2. nenhuma oportunidade pública é ocultada para vender plano;
3. preview limitado do Free não se confunde com catálogo público;
4. plano atual, limite e consumo são compreensíveis;
5. tela de Planos é acessível voluntariamente em cada jornada;
6. entrada contextual não elimina alternativas legítimas;
7. comparação geral e incremental são coerentes;
8. delta direto plano atual → alvo é previsto;
9. nenhuma opção paga vem pré-selecionada;
10. preço, periodicidade, recorrência e data de início aparecem antes da confirmação;
11. pagador e beneficiário são distinguíveis;
12. sucesso não é presumido antes de confirmação;
13. falha não remove direitos essenciais;
14. cancelamento/downgrade são acessíveis e tratam perdas/reduções/excedentes;
15. Enterprise/Scale não fingem checkout autônomo;
16. assinatura não se confunde com taxa transacional;
17. pagamento não promete melhor relevância, confiança ou evolução;
18. parâmetros financeiros ainda indefinidos permanecem indefinidos.

Veredito: **9/9 SVGs funcionalmente aprovados como candidatos; 6 após reforma controlada e 3 sem alteração visual**.

## 16. Fora do escopo

A UXA-100 não altera GEM-004, valida preços no mercado, registra superfícies/transições canônicas, cria checkout real, integra gateway, cria cobrança, nota fiscal, pró-rata, crédito ou grace period, implementa entitlement, publica oferta comercial, promove jornadas ou inicia Engenharia de Produto.

## 17. Estado da frente

A UXA-100 permanece **programa candidato em draft**. A UXA-100-A1 integra a etapa Planos às três jornadas e adiciona as telas dedicadas. A UXA-100-A2 valida funcionalmente os nove ativos no escopo candidato.

Estado atual da frente:

- 9 SVGs candidatos;
- 9/9 funcionalmente aprovados como candidatos;
- 6 reformulados pela UXA-100-A2;
- 3 preservados sem reforma;
- 109 SVGs canônicos permanecem inalterados;
- 0 novas superfícies canônicas;
- 0 novas transições canônicas;
- jornadas permanecem `draft`;
- Engenharia de Produto permanece pausada antes de W0-01.

A existência e validação documental desses ativos não constituem integração à `main`, lançamento, implementação ou operação. A eventual promoção/fragmentação canônica exige decisão governada separada.
