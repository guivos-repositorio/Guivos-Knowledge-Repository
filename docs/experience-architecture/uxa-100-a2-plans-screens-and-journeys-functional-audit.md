---
id: UXA-100-A2
title: Auditoria Funcional das Telas, Fluxos e Jornadas de Planos
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
depends_on:
  - UXA-100-A1
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GEM-004-A1
  - GEM-004-A2
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-UPGRADE-DOWNGRADE-CANCELLATION-POLICY-001
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
normative: false
---

# Auditoria Funcional das Telas, Fluxos e Jornadas de Planos

## 1. Finalidade

A UXA-100-A2 registra a auditoria funcional dos **nove SVGs candidatos** da frente de Planos, Comparação, Cobrança e Pagamentos e verifica a integração da etapa Planos às jornadas de Pessoa, Coletivo e Organização.

A versão 0.2.0 reconcilia este registro de auditoria com a autoridade conceitual vigente de planos. A auditoria original ocorreu antes da substituição final de nomenclaturas; os achados funcionais são preservados, mas a leitura corrente dos ativos e jornadas passa a utilizar exclusivamente a taxonomia canônica atual.

A auditoria não cria oferta pública, checkout, gateway, entitlement operacional, cobrança, IDs canônicos de superfície/transição ou promoção de jornada.

## 2. Autoridades examinadas e precedência atual

A auditoria confrontou os ativos com:

- `GEM-004-A1` — catálogo comercial candidato de planos, benefícios e preços;
- `GEM-004-A2` — política de oferta, upgrade, downgrade e cancelamento;
- política de paywall do GEM-004;
- política de ciclo de vida do plano;
- matriz pagador–beneficiário do GEM-003;
- UXA-100 e UXA-100-A1;
- jornadas de Pessoa, Coletivo e Organização.

Para nomenclatura, fronteiras entre participante e produto e interpretação de `BND-002`, prevalece `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`.

## 3. Veredito preservado

> **Aprovados funcionalmente como materializações candidatas após reformulação controlada de seis SVGs; nomenclatura posteriormente reconciliada sem alterar a conclusão funcional.**

Resultado histórico preservado:

- 9 SVGs auditados;
- 3 aprovados sem reformulação funcional naquele ciclo;
- 6 aprovados após reformulação controlada;
- 0 SVGs removidos;
- 0 novos IDs canônicos;
- 0 novas transições canônicas;
- 0 jornadas promovidas;
- contagem canônica permaneceu em 109 SVGs até a promoção governada posterior.

A aprovação funcional significa coerência como **referência de experiência** no escopo auditado. Não significa implementação, operação, oferta comercial vigente ou autorização econômica.

## 4. Matriz de auditoria dos nove SVGs

| Participante | Ativo | Resultado funcional histórico | Estado de nomenclatura atual |
|---|---|---|---|
| Pessoa | tela dedicada de Planos | aprovada após reforma | Free · Plus · Pro |
| Pessoa | fluxo de plano/cobrança/pagamento | aprovado após reforma | Free · Plus · Pro |
| Pessoa | comparação incremental | aprovada | Free · Plus · Pro |
| Coletivo | tela dedicada de Planos | aprovada após reforma | Livre · Mobiliza · Impacta · Rede |
| Coletivo | fluxo de plano/cobrança/pagamento | aprovado após reforma | Livre · Mobiliza · Impacta · Rede |
| Coletivo | comparação incremental | aprovada | Livre · Mobiliza · Impacta · Rede |
| Organização | tela dedicada de Planos | aprovada após reforma | Conecta · Eleva · Transforma |
| Organização | fluxo de plano/cobrança/pagamento | aprovado após reforma | Conecta · Eleva · Transforma |
| Organização | comparação incremental | aprovada | Conecta · Eleva · Transforma |

Guivos Business permanece Produto Especializado separado, com tiers `Start · Growth · Scale · Enterprise`. Nenhum dos três SVGs da Organização é um SVG de Guivos Business.

## 5. Reformulações controladas

### 5.1 Pessoa — tela dedicada de Planos

Problemas encontrados:

- a capacidade de Plus aparecia como “ampliada”, enquanto a autoridade comercial define **sem cota semanal fixa, sujeita a uso justo**;
- preços anuais e forma de cobrança não estavam suficientemente explícitos na comparação;
- faltavam lembretes funcionais sobre recorrência/renovação, data de início, dados/consentimento e separação entre assinatura e preço/taxa de oportunidade.

Reforma:

- linguagem de Plus alinhada ao GEM-004-A1;
- preços anuais candidatos explicitados;
- anual caracterizado como pagamento antecipado;
- revisão deve apresentar recorrência, renovação e data de início;
- assinatura não amplia consentimento automaticamente;
- assinatura, transação e acesso financiado permanecem objetos separados.

### 5.2 Pessoa — fluxo de plano/cobrança/pagamento

Problemas encontrados:

- revisão da contratação não tornava a data de início suficientemente explícita;
- confirmação não registrava claramente a data de início;
- cancelamento não explicitava plano posterior e interrupção da renovação;
- downgrade precisava nomear histórico/relatórios, integrações e exportação como efeitos a revisar.

Reforma:

- inclusão de data de início na revisão e no estado confirmado;
- cancelamento passa a apresentar data efetiva, plano posterior, interrupção da renovação e comprovante;
- downgrade passa a explicitar capacidades, histórico/relatórios, integrações, exportação e baseline gratuito.

### 5.3 Coletivo — tela dedicada de Planos

Problemas encontrados no ciclo original:

- comparação não mostrava os preços anuais candidatos;
- a leitura de núcleo/unidade não estava uniforme;
- condições comerciais mínimas exigidas pelo GEM-004-A2 estavam dispersas.

Reforma funcional preservada e nomenclatura atual:

- preços anual/mensal alinhados ao catálogo;
- núcleo/unidade explicitado onde aplicável;
- condições de recorrência/renovação, data de início, separação de taxa/comissão/tributo e acesso financiado adicionadas ao mesmo contexto de comparação;
- a escada corrente é `Livre → Mobiliza → Impacta → Rede`.

### 5.4 Coletivo — fluxo de plano/cobrança/pagamento

Problemas encontrados no ciclo original:

- a capacidade intermediária de maior profundidade aparecia de forma compacta como “até 5 unidades”, enquanto a autoridade usa `núcleos ou unidades/programas` conforme contexto;
- downgrade/cancelamento não detalhava o tratamento obrigatório das capacidades excedentes;
- data de início não estava explícita na revisão.

Reforma:

- nomenclatura de núcleo/unidade alinhada;
- antes de downgrade para Livre, o Coletivo deve escolher publicações gratuitas mantidas, encerrar/converter publicações pagas excedentes e reduzir administradores/núcleos conforme limite;
- compromissos, exportação e registros permanecem tratados;
- exclusão silenciosa permanece proibida;
- data de início passa a integrar a revisão/confirmação.

### 5.5 Organização — tela dedicada de Planos

Problemas funcionais encontrados no ciclo original:

- exemplos de consumo divergiam do fluxo principal sem indicar que eram cenários distintos;
- preços anuais dos dois primeiros degraus não estavam na tela;
- o valor mínimo do degrau de maior complexidade não explicitava `/mês`;
- condições comerciais mínimas estavam incompletas no contexto de comparação.

Reforma funcional preservada e taxonomia reconciliada:

- consumo da tela alinhado ao cenário de fluxo (`8/10` novas e `12/15` ativas);
- Conecta exibe `R$ 299/mês` e `R$ 2.990/ano` como referências candidatas;
- Eleva exibe `R$ 799/mês` e `R$ 7.990/ano` como referências candidatas;
- Transforma exibe `a partir de R$ 1.990/mês · contrato anual`;
- recorrência/renovação, data de início, separação transacional, acesso financiado e proteção de dados/consentimento ficam explícitos;
- a superfície declara `Organização ≠ Guivos Business`.

Os preços e capacidades acima pertencem à baseline candidata de Organização e não são preços de Guivos Business.

### 5.6 Organização — fluxo de plano/cobrança/pagamento

Problemas encontrados:

- downgrade/cancelamento tratava excedentes de forma genérica;
- a política exige escolha explícita do que permanecerá dentro do plano futuro;
- data de início não estava explícita na revisão/confirmação.

Reforma:

- Organização deve selecionar unidades, administradores, publicações e Coletivos relacionados mantidos;
- integrações a encerrar e dados a exportar devem ser identificados;
- histórico/agregados não podem ser apagados para forçar retenção;
- data efetiva e plano posterior devem aparecer antes da conclusão;
- data de início passa a constar da revisão/confirmação.

## 6. Comparações incrementais — leitura atual

As três placas incrementais preservam o princípio de mostrar apenas o que cada degrau acrescenta.

### Pessoa

```text
Free
→ Plus = tudo do Free + personalização/conveniência ampliadas
→ Pro = tudo do Plus + profundidade analítica, relatórios e integrações ampliadas
```

A placa preserva o catálogo público do Free e usa a formulação correta de Plus sem cota semanal fixa, sujeita a uso justo.

### Coletivo

```text
Livre
→ Mobiliza
→ Impacta
→ Rede
```

Cada degrau mostra apenas capacidades adicionais. Rede permanece sujeito a dimensionamento/contrato quando aplicável e sem promessa de volume infinito. A antiga leitura `Gestão / Impacto / Enterprise` é apenas evidência histórica superseded e não taxonomia corrente.

### Organização

```text
Conecta
→ Eleva
→ Transforma
```

Transforma pode exigir contratação/dimensionamento assistido conforme a autoridade econômica aplicável. Isso não transforma a Organização em Guivos Business.

Separação obrigatória:

```text
Organização Conecta ≠ Guivos Business Start
Organização Eleva ≠ Guivos Business Growth
Organização Transforma ≠ Guivos Business Scale ou Enterprise
```

## 7. Auditoria das jornadas

### 7.1 Pessoa

Planos pode ser acessado voluntariamente por Conta/Configurações e contextualmente após limite legítimo do Free.

A entrada contextual preserva:

- Explorar oportunidades públicas;
- Mapa;
- catálogo público;
- informações públicas essenciais;
- ausência de urgência artificial.

A jornada não transforma assinatura em condição para descobrir oportunidades.

### 7.2 Coletivo

Planos pode ser acessado pela administração ou após limite de cota/capacidade.

Antes de upgrade permanecem alternativas válidas, quando aplicáveis:

- manter publicação gratuita;
- salvar rascunho;
- aguardar próximo ciclo;
- encerrar/agendar publicação.

Downgrade exige tratamento explícito das capacidades excedentes e compromissos existentes.

Quando a contratação não puder ser concluída em autoatendimento, `BND-002` representa apenas a fronteira de contratação/dimensionamento assistido; não representa plano Rede, Enterprise ou qualquer tier de Business.

### 7.3 Organização

Planos pode ser acessado voluntariamente ou após capacidade atingida.

A jornada preserva alternativas de arquivar, agendar, manter rascunho ou aguardar quando aplicáveis. A escada institucional é `Conecta → Eleva → Transforma`.

Downgrade exige escolha explícita dos objetos e capacidades que permanecerão no plano futuro.

Quando for necessário processo assistido, `BND-002` representa a transferência para contratação/dimensionamento assistido e não “ir para Business Scale/Enterprise”.

## 8. Critérios validados e reconciliados

A auditoria confirma, no escopo dos nove SVGs, que:

1. alternativa gratuita permanece visível e funcional;
2. oportunidade pública não é ocultada para vender plano;
3. preview limitado do Free é distinto do catálogo público;
4. plano atual, limite e consumo são compreensíveis;
5. Planos possui entrada voluntária nas três jornadas;
6. entrada contextual preserva alternativas legítimas;
7. matriz geral e comparação incremental são coerentes;
8. delta direto plano atual → alvo está previsto;
9. nenhuma opção paga é pré-selecionada;
10. preço, periodicidade, recorrência e data de início são exigidos antes da confirmação quando aplicáveis;
11. pagador e beneficiário são distintos;
12. sucesso não é presumido antes de confirmação;
13. falha preserva estado anterior, dados e direitos;
14. downgrade/cancelamento mostram consequências e tratamento de excedentes;
15. contratação que exigir assistência segue `BND-002` sem simular checkout autônomo;
16. assinatura não se confunde com taxa transacional;
17. pagamento não promete relevância, confiança, impacto ou evolução;
18. parâmetros financeiros ainda indefinidos permanecem indefinidos;
19. repetição da mesma intenção não deve duplicar cobrança ou ativação;
20. jornada documentada não equivale a implementação;
21. Organização ≠ Guivos Business;
22. tiers Business não recebem automaticamente preços, limites ou entitlements da Organização.

## 9. Estado após reconciliação

A frente preserva o resultado histórico da auditoria e adota a leitura semântica corrente:

- 9 SVGs da frente de Planos funcionalmente aprovados no escopo UXA-100-A2;
- nomenclatura atual sincronizada com a autoridade de planos;
- 0 IDs canônicos novos nesta reconciliação;
- 0 transições canônicas novas nesta reconciliação;
- Pessoa, Coletivo e Organização continuam `draft`;
- Guivos Business permanece Produto Especializado separado;
- `BND-002` permanece fronteira sem tela e com processo posterior ainda parcial;
- Engenharia de Produto continua pausada antes de W0-01.

As contagens canônicas posteriores à promoção UXA-100-A3 são governadas pelos registros vigentes de jornada; a referência histórica a 109 SVGs acima descreve apenas o momento original da auditoria A2.

## 10. Próximo gate possível

Cobrança real, gateway, entitlements técnicos, processo posterior a `BND-002` e demais evoluções exigem autorização separada.

Esta reconciliação não autoriza implementação, nova UXA, oferta comercial, cobrança nem Engenharia de Produto.