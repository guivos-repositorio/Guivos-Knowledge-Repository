---
id: UXA-100
title: Programa Funcional, Materialização, Validação e Promoção de Planos, Cobrança e Pagamentos
status: draft
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
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
  - GPA-004
  - GEM-007-BUSINESS-ECONOMIC-ROLE-001
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

A UXA-100 estrutura e materializa a experiência documental de **planos, comparação, cobrança, pagamento e ciclo de vida comercial** para os três tipos de participante já cobertos pela frente:

- Pessoa;
- Coletivo;
- Organização.

A taxonomia vigente é:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`.

**Guivos Business não é quarto tipo de participante da UXA-100.** É produto especializado com taxonomia conceitual `Start · Growth · Scale · Enterprise`, governada por `GPA-004`, `GEM-007-BUSINESS-ECONOMIC-ROLE-001` e `GEM-004-A1`. Esta atualização não cria superfícies, transições, SVGs ou checkout para Business.

A frente não autoriza oferta pública, cobrança real, gateway, implantação, desenvolvimento, política fiscal final ou publicação de preços como oferta vigente.

## 2. Regra conceitual dos planos

Plano representa profundidade de serviço, capacidade operacional ou complexidade atendida. Não representa valor, mérito, prestígio, maturidade ou nível de evolução do participante.

A progressão entre planos não é obrigatória. Permanecer, reduzir, cancelar ou utilizar um plano de menor capacidade não reduz legitimidade, reputação ou evolução.

## 3. Migração taxonômica preservando comportamento

A atualização aplica somente a seguinte equivalência de nomenclatura às materializações UXA-100:

| Anterior | Vigente |
|---|---|
| Coletivo Gestão | Coletivo Mobiliza |
| Coletivo Impacto | Coletivo Impacta |
| Coletivo Enterprise | Coletivo Rede |
| Business Start na jornada da Organização | Organização Conecta |
| Business Growth na jornada da Organização | Organização Eleva |
| Business Scale na jornada da Organização | Organização Transforma |

Preços, capacidades, estados, decisões, IDs e maturidades já governados são preservados onde aplicáveis. A alteração não transforma a Organização em Guivos Business.

## 4. Pergunta funcional

A experiência deve responder, sem coerção:

> **Qual plano está ativo, o que ele inclui, qual limite foi alcançado, quais alternativas permanecem válidas, o que muda ao escolher outro plano, quem paga e quem recebe o benefício, qual é a recorrência e o que acontece em sucesso, falha, downgrade ou cancelamento?**

Para Pessoa há obrigação adicional de limitar a camada personalizada do Free sem esconder oportunidades públicas.

## 5. Autoridades e limites preservados

### 5.1 Baseline comercial

A UXA-100 usa somente referências governadas em GEM-004-A1/A2. Valores exibidos são preços candidatos de participantes para simulação documental.

### 5.2 Oportunidade pública

Limite do Free não reduz Explorar, Mapa, catálogo público nem informações públicas essenciais. É proibido ocultar oportunidade pública para pressionar upgrade.

### 5.3 Pagamento não altera relevância

Plano pago não eleva posição orgânica, relevância funcional, veracidade, confiança, legitimidade, impacto ou evolução humana.

### 5.4 Assinatura é distinta de transação

```text
assinatura da plataforma
≠ preço de atividade/oportunidade
≠ comissão
≠ taxa do meio de pagamento
≠ tributo
```

### 5.5 Parâmetros não definidos

A UXA-100 não inventa gateway, adquirente, método oficial, tokenização, período de graça, pró-rata, crédito entre ciclos, política fiscal/tributária final ou trial com conversão automática.

## 6. Fragmentação canônica preservada

A UXA-100 continua usando quatro famílias por participante:

1. `*-301 — Planos e comparação`;
2. `*-302 — Revisão de contratação`;
3. `*-303 — Gestão de downgrade e cancelamento`;
4. `*-304 — Resultado e recuperação`.

Não recebem superfície própria comparação incremental, processamento transitório de pagamento, mensagens simples de confirmação, periodicidade mensal/anual, preview de limite ou contratação assistida.

## 7. BND-002 — fronteira genérica de contratação assistida

`GKR-SURF-BND-002` passa a ser lido exclusivamente como **fronteira de contratação/dimensionamento assistido**.

Ela é acionável quando uma intenção deixa de ser autonomamente configurável e passa a exigir proposta, dimensionamento, contrato, configuração ou análise específica.

`BND-002`:

- não significa Enterprise, Scale, Rede ou Transforma;
- não pertence a um único participante;
- não é checkout;
- não define preço, SLA ou capacidade;
- não promove `TRN-416` ou `TRN-426`, que permanecem parciais.

## 8. Espinha dorsal transversal

```text
*-301 Planos e comparação
├── upgrade/mudança autônoma
│   → *-302 revisão
│   → *-304 resultado/recuperação
│   → *-301 reconciliado
├── downgrade/cancelamento
│   → *-303 revisão de ciclo/consequências
│   → *-304 resultado/recuperação
│   → *-301 reconciliado
└── contratação não autonomamente configurável
    → BND-002 contratação/dimensionamento assistido
```

## 9. Comparação entre planos

A experiência preserva matriz geral, delta incremental e delta direto atual→alvo. Benefícios herdados não são reapresentados como novidades. No downgrade, o delta explicita exatamente capacidades removidas/reduzidas.

## 10. Entradas nas jornadas

Existem entrada voluntária por Conta/Administração/Configurações e entrada contextual quando limite legítimo é alcançado. O participante não precisa atingir limite para consultar ou administrar seu plano.

A UXA-100 não inventa origem canônica quando a superfície anterior ainda não possui identidade suficiente no registro.

# 11. Pessoa

## 11.1 Planos

| Plano | Mensal | Anual | Correspondências personalizadas completas |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | 2 por semana |
| Guivos Plus | R$ 24,90 | R$ 249,00 | sem cota semanal fixa, sujeito a uso justo |
| Guivos Pro | R$ 49,90 | R$ 499,00 | sem cota semanal fixa, com análise ampliada |

Leitura: Free = começar sem barreira econômica; Plus = aprofundar personalização/continuidade; Pro = aprofundar análise/integração. Nenhum nome representa nível de evolução da Pessoa.

Após cota Free, permanecem `Explorar oportunidades públicas`, `Ver no Mapa` e consulta voluntária de planos.

Superfícies: `PER-301` a `PER-304`. Transições: `TRN-401` a `TRN-405`, localmente validadas.

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

# 12. Coletivo

## 12.1 Planos

| Plano | Mensal | Anual | Atividades/mês | Oportunidades/mês | Ativas | Publicação paga |
|---|---:|---:|---:|---:|---:|---|
| Livre | R$ 0,00 | R$ 0,00 | 1 gratuita | 1 gratuita | 2 | não |
| Mobiliza | R$ 89,90 | R$ 899,00 | 4 | 4 | 6 | sim |
| Impacta | R$ 249,90 | R$ 2.499,00 | 15 | 15 | 20 | sim |
| Rede | sob consulta | contrato anual | capacidade contratada | capacidade contratada | capacidade contratada | sim |

Leitura: Livre = operar/mobilizar sem barreira; Mobiliza = transformar intenção em mobilização coordenada; Impacta = transformar mobilização em impacto sustentado/evidenciado; Rede = coordenar complexidade de rede.

Ao atingir cota/capacidade, publicações existentes, rascunho, espera de ciclo e alternativas operacionais válidas permanecem disponíveis. Downgrade trata compromissos/excedentes sem exclusão silenciosa.

Superfícies: `COL-301` a `COL-304`. `TRN-411` a `TRN-415` permanecem localmente validadas; `TRN-416` permanece parcial até o processo posterior a `BND-002`.

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

# 13. Organização

## 13.1 Planos

| Plano | Mensal | Anual | Novas oportunidades/programas | Ativas | Administradores | Unidades |
|---|---:|---:|---:|---:|---:|---:|
| Conecta | R$ 299,00 | R$ 2.990,00 | 10/mês | 15 | 3 | 1 |
| Eleva | R$ 799,00 | R$ 7.990,00 | 50/mês | 75 | 10 | até 5 |
| Transforma | a partir de R$ 1.990,00/mês | contrato anual | capacidade contratada | capacidade contratada | conforme contrato | múltiplas |

Leitura: Conecta = conectar capacidade institucional a pessoas/Coletivos/oportunidades; Eleva = ampliar coordenação e profundidade institucional; Transforma = transformar capacidade institucional em impacto sistêmico sustentado quando houver evidência e governança.

`Transforma` não garante impacto nem corresponde a Guivos Business Enterprise.

Antes de downgrade, a Organização seleciona unidades, administradores, publicações, Coletivos relacionados, integrações e dados conforme política vigente. Históricos/agregados não são apagados para forçar retenção.

Superfícies: `ORG-301` a `ORG-304`. `TRN-421` a `TRN-425` permanecem localmente validadas; `TRN-426` permanece parcial até o processo posterior a `BND-002`.

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

# 14. Guivos Business fora da materialização UXA-100

Guivos Business possui planos conceituais `Start · Growth · Scale · Enterprise`, mas esta UXA:

- não cria tela de Planos Business;
- não cria `BUS-*`, `SURF`, `TRN` ou SVG adicional;
- não reutiliza `ORG-301..304` como telas Business;
- não copia preço/entitlement de Organização;
- não cria correspondência Conecta↔Start, Eleva↔Growth ou Transforma↔Scale/Enterprise.

`Organização Transforma ≠ Guivos Business Enterprise` é fronteira estrutural obrigatória.

# 15. Pagador e beneficiário

Toda revisão distingue pagador, beneficiário, autoridade de cancelamento e escopo de dados necessário. Pagamento por terceiro não transfere autoridade, acesso à jornada pessoal ou poder de alterar relevância/recomendação.

# 16. Resultado, falha e recuperação

`*-304` agrupa sucesso e falha na mesma responsabilidade, mantendo consequências distintas. Falha informa não confirmação, não presume ativação, preserva estado anterior/direitos, oferece recuperação e impede duplicação por repetição da mesma intenção.

# 17. Downgrade e cancelamento

`*-303` mostra estado atual/futuro, capacidades afetadas, excedentes, data efetiva e alternativas. Cancelamento interrompe renovação futura, confirma o estado posterior e não reativa sem autorização.

# 18. Materialização visual canônica

Os **mesmos nove SVGs** permanecem, sem novos IDs:

### Telas dedicadas

- `uxa-100-person-plans-screen-mobile.svg`;
- `uxa-100-collective-plans-screen-desktop.svg`;
- `uxa-100-organization-plans-screen-desktop.svg`.

### Boards de fluxo

- `uxa-100-person-plans-payments-flow-board.svg`;
- `uxa-100-collective-plans-payments-flow-board.svg`;
- `uxa-100-organization-plans-payments-flow-board.svg`.

### Comparações incrementais

- `uxa-100-person-plan-incremental-benefits-comparison.svg`;
- `uxa-100-collective-plan-incremental-benefits-comparison.svg`;
- `uxa-100-organization-plan-incremental-benefits-comparison.svg`.

A sincronização taxonômica altera apenas nomenclatura/cópia necessária nos ativos de Coletivo e Organização; não cria novo estado funcional.

Os ativos continuam nos perfis `R29`, `R30` e `R31`. O conjunto permanece **118 SVGs / 118 associações / 31 perfis**.

# 19. Estado canônico preservado

A atualização não altera as contagens promovidas pela UXA-100-A3:

- 118 SVGs canônicos;
- 118 associações;
- 31 perfis;
- 53 superfícies/estados/fronteiras;
- 54 transições documentais;
- 12 superfícies de planos para os três participantes;
- 17 transições da família de Planos;
- `TRN-416` e `TRN-426` parciais;
- nenhuma jornada promovida.

# 20. Limites

Esta atualização não cria oferta pública, cobrança real, gateway, entitlement técnico, política fiscal, pró-rata, período de graça, processo posterior a `BND-002`, nova jornada Business, novos IDs, UXA-102/V5, protótipo ou Engenharia de Produto.
