---
id: UXA-100-A2
title: Auditoria Funcional das Telas, Fluxos e Jornadas de Planos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-100
depends_on:
  - UXA-100-A1
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

A UXA-100-A2 executa a auditoria funcional dos **nove SVGs candidatos** da frente de Planos, Comparação, Cobrança e Pagamentos e verifica a integração da etapa Planos às jornadas de Pessoa, Coletivo e Organização.

A auditoria não cria oferta pública, checkout, gateway, entitlement operacional, cobrança, IDs canônicos de superfície/transição ou promoção de jornada.

## 2. Autoridades examinadas

A auditoria confrontou os ativos com:

- `GEM-004-A1` — catálogo comercial candidato de planos, benefícios e preços;
- `GEM-004-A2` — política de oferta, upgrade, downgrade e cancelamento;
- política de paywall do GEM-004;
- política de ciclo de vida do plano;
- matriz pagador–beneficiário do GEM-003;
- UXA-100 e UXA-100-A1;
- jornadas atuais de Pessoa, Coletivo e Organização.

## 3. Veredito

> **Aprovados funcionalmente como materializações candidatas após reformulação controlada de seis SVGs.**

Resultado:

- 9 SVGs auditados;
- 3 aprovados sem reformulação;
- 6 aprovados após reformulação controlada;
- 0 SVGs removidos;
- 0 novos IDs canônicos;
- 0 novas transições canônicas;
- 0 jornadas promovidas;
- contagem canônica permanece em 109 SVGs até promoção governada posterior.

A aprovação funcional desta frente significa que os ativos estão coerentes como **referências candidatas de experiência**. Não significa implementação, operação, oferta comercial vigente ou integração à `main`.

## 4. Matriz de auditoria dos nove SVGs

| Participante | Ativo | Resultado | Reforma |
|---|---|---|---|
| Pessoa | tela dedicada de Planos | aprovada após reforma | sim |
| Pessoa | fluxo de plano/cobrança/pagamento | aprovado após reforma | sim |
| Pessoa | comparação incremental | aprovada | não |
| Coletivo | tela dedicada de Planos | aprovada após reforma | sim |
| Coletivo | fluxo de plano/cobrança/pagamento | aprovado após reforma | sim |
| Coletivo | comparação incremental | aprovada | não |
| Organização | tela dedicada de Planos | aprovada após reforma | sim |
| Organização | fluxo de plano/cobrança/pagamento | aprovado após reforma | sim |
| Organização | comparação incremental | aprovada | não |

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

Problemas encontrados:

- comparação não mostrava os preços anuais candidatos;
- a leitura de núcleo/unidade não estava uniforme;
- condições comerciais mínimas exigidas pelo GEM-004-A2 estavam dispersas.

Reforma:

- preços anual/mensal alinhados ao catálogo;
- núcleo/unidade explicitado onde aplicável;
- condições de recorrência/renovação, data de início, separação de taxa/comissão/tributo e acesso financiado adicionadas ao mesmo contexto de comparação.

### 5.4 Coletivo — fluxo de plano/cobrança/pagamento

Problemas encontrados:

- `Impacto` aparecia de forma compacta como “até 5 unidades”, enquanto a autoridade usa `núcleos ou unidades/programas` conforme contexto;
- downgrade/cancelamento não detalhava o tratamento obrigatório das capacidades excedentes;
- data de início não estava explícita na revisão.

Reforma:

- nomenclatura de núcleo/unidade alinhada;
- antes de downgrade para Livre, o Coletivo deve escolher publicações gratuitas mantidas, encerrar/converter publicações pagas excedentes e reduzir administradores/núcleos conforme limite;
- compromissos, exportação e registros permanecem tratados;
- exclusão silenciosa permanece proibida;
- data de início passa a integrar a revisão/confirmação.

### 5.5 Organização — tela dedicada de Planos

Problemas encontrados:

- exemplos de consumo divergiam do fluxo principal sem indicar que eram cenários distintos;
- preços anuais de Start/Growth não estavam na tela;
- o valor mínimo de Scale não explicitava `/mês`;
- condições comerciais mínimas estavam incompletas no contexto de comparação.

Reforma:

- consumo da tela alinhado ao cenário de fluxo (`8/10` novas e `12/15` ativas);
- preços anuais de Start/Growth adicionados;
- Scale passa a exibir `a partir de R$ 1.990/mês · contrato anual`;
- recorrência/renovação, data de início, separação transacional, acesso financiado e proteção de dados/consentimento ficam explícitos.

### 5.6 Organização — fluxo de plano/cobrança/pagamento

Problemas encontrados:

- downgrade/cancelamento tratava excedentes de forma genérica;
- a política exige escolha explícita do que permanecerá dentro do plano futuro;
- data de início não estava explícita na revisão/confirmação.

Reforma:

- Organização deve selecionar unidades, administradores, publicações e Coletivos relacionados mantidos;
- integrações a encerrar e dados a exportar devem ser identificados;
- histórico/agregados não podem ser apagados para forçar retenção;
- data efetiva e plano posterior devem aparecer antes da conclusão;
- data de início passa a constar da revisão/confirmação.

## 6. Comparações incrementais aprovadas sem reforma

As três placas incrementais já estavam alinhadas ao catálogo comercial candidato:

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
→ Gestão
→ Impacto
→ Enterprise
```

Cada degrau mostra apenas capacidades adicionais. Enterprise permanece dimensionado por contrato e sem promessa de volume infinito.

### Organização

```text
Business Start
→ Business Growth
→ Business Scale
```

Scale permanece proposta comercial e capacidade contratada, não checkout de escopo fixo.

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

### 7.3 Organização

Planos pode ser acessado voluntariamente ou após capacidade atingida.

A jornada preserva alternativas de arquivar, agendar, manter rascunho ou aguardar quando aplicáveis. Business Scale segue processo comercial governado.

Downgrade exige escolha explícita dos objetos e capacidades que permanecerão no plano futuro.

## 8. Critérios validados

A auditoria confirma, no escopo dos nove SVGs candidatos, que:

1. alternativa gratuita permanece visível e funcional;
2. oportunidade pública não é ocultada para vender plano;
3. preview limitado do Free é distinto do catálogo público;
4. plano atual, limite e consumo são compreensíveis;
5. Planos possui entrada voluntária nas três jornadas;
6. entrada contextual preserva alternativas legítimas;
7. matriz geral e comparação incremental são coerentes;
8. delta direto plano atual → alvo está previsto;
9. nenhuma opção paga é pré-selecionada;
10. preço, periodicidade, recorrência e data de início são exigidos antes da confirmação;
11. pagador e beneficiário são distintos;
12. sucesso não é presumido antes de confirmação;
13. falha preserva estado anterior, dados e direitos;
14. downgrade/cancelamento mostram consequências e tratamento de excedentes;
15. Enterprise/Scale não simulam checkout autônomo;
16. assinatura não se confunde com taxa transacional;
17. pagamento não promete relevância, confiança, impacto ou evolução;
18. parâmetros financeiros ainda indefinidos permanecem indefinidos;
19. repetição da mesma intenção não deve duplicar cobrança ou ativação;
20. jornada documentada não equivale a implementação.

## 9. Estado após auditoria

A frente fica assim:

- 9 SVGs candidatos materializados;
- 9 SVGs funcionalmente aprovados no escopo da UXA-100-A2;
- 6 reformulados nesta auditoria;
- 3 preservados sem alteração;
- 109 SVGs canônicos permanecem como baseline vigente até promoção posterior;
- 0 IDs canônicos novos;
- 0 transições canônicas novas;
- Pessoa, Coletivo e Organização continuam `draft`;
- Engenharia de Produto continua pausada antes de W0-01.

## 10. Próximo gate possível

Uma etapa posterior poderá decidir se os nove ativos devem ser:

- fracionados em superfícies/estados menores;
- registrados com novos IDs canônicos;
- conectados por novas transições;
- incorporados ao catálogo e à galeria canônica.

Essa decisão **não é automática** e não é autorizada por esta auditoria.
