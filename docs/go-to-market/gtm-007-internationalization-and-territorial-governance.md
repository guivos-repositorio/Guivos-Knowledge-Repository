---
id: GTM-007
title: Governança de Internacionalização e Programa Territorial
status: proposed
version: 0.1.0
owner: Guivos Strategy & Growth
last_updated: 2026-08-08
depends_on:
  - GTM-001
  - GTM-005
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-DIGITAL-ASSET-CONTROL-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
  - GKR-DATA-PRIVACY-CONSENT-001
related:
  - GTM-008
  - GKR-INTERNATIONAL-OPERATIONS-READINESS-001
normative: true
---

# Governança de Internacionalização e Programa Territorial

## 1. Finalidade

Este documento governa como a Guivos transforma intenção geográfica em programa territorial verificável, sem confundir presença digital, usuários incidentais, proteção de marca, pesquisa de mercado, prospecção, piloto, contratação, estabelecimento jurídico e operação real.

A internacionalização permanece subordinada ao propósito, densidade do ecossistema, capacidade operacional, conformidade e sustentabilidade econômica.

## 2. Sequência territorial vigente

```text
Belo Horizonte
→ São Paulo
→ amplificação nacional seletiva
→ Portugal / Lisboa
→ Portugal / Porto
→ novo país europeu somente mediante novo gate
```

Portugal continua sendo o primeiro mercado internacional de referência. Lisboa é a base inicial candidata. Porto é expansão posterior condicionada ao resultado do piloto em Lisboa.

Este documento não declara Portugal, Lisboa ou Porto como mercados operacionais.

## 3. Separações obrigatórias

```text
usuário acessando de um país ≠ mercado ativo nesse país
site acessível globalmente ≠ oferta comercial direcionada globalmente
domínio territorial ≠ operação territorial
marca protegida ≠ estabelecimento jurídico
pesquisa de mercado ≠ prospecção comercial
prospecção comercial ≠ contrato local
aceitação de pagamento ≠ conformidade fiscal completa
parceiro local ≠ entidade Guivos local
piloto autorizado ≠ piloto executado
piloto executado ≠ escala aprovada
presença digital ≠ presença física
```

## 4. Registro territorial mínimo

Cada território candidato deverá diferenciar:

- território e papel estratégico;
- estado territorial;
- hipótese de entrada;
- segmentos e oferta local necessária;
- owner, orçamento e limites de perda;
- aquisição, vendas e parcerias;
- suporte e operação;
- pagamentos, faturação e fiscalidade;
- contratos e superfícies legais;
- proteção de dados e transferências;
- consumidor/e-commerce quando aplicável;
- obrigações de plataforma/marketplace quando aplicáveis;
- propriedade intelectual e ativos digitais;
- necessidade de entidade, filial, representação ou equipe local;
- terceiros críticos;
- métricas de piloto, kill criteria e gate de escala;
- evidência que sustenta cada estado.

## 5. Estados territoriais

| Estado | Significado |
|---|---|
| `T0_observed_inbound` | acesso ou interesse incidental; nenhum programa territorial |
| `T1_candidate` | território candidato estratégico |
| `T2_researched` | pesquisa inicial documentada |
| `T3_readiness_assessment` | avaliação comercial, operacional, jurídica, fiscal, privacidade e pagamentos |
| `T4_design_approved` | desenho territorial aprovado, ainda sem piloto operacional |
| `T5_pilot_authorized` | piloto explicitamente autorizado com owner, escopo, orçamento e gates |
| `T6_pilot_evidenced` | piloto realmente executado e evidenciado |
| `T7_scale_gate_passed` | critérios de escala aprovados a partir da evidência |
| `T8_active_market` | operação territorial recorrente comprovada |
| `T9_replication_ready` | playbook territorial estável e replicável mediante novo gate |
| `paused` | avanço suspenso deliberadamente |
| `retired` | programa encerrado |

Nenhum estado é inferido automaticamente do anterior.

## 6. Estado de Portugal em 2026-08-08

Portugal permanece em `T1_candidate`, com planejamento documentado em `GTM-001`.

- Portugal: primeiro país internacional de referência;
- Lisboa: primeira base candidata;
- Porto: expansão posterior condicionada;
- segundo país europeu: não autorizado;
- operação comercial local: `not_evidenced`;
- entidade/filial local: `not_evidenced`;
- equipe local: `not_evidenced`;
- contratos locais: `not_evidenced`;
- pagamentos europeus em produção: `not_evidenced`;
- faturação/IVA em operação: `not_evidenced`;
- suporte internacional em produção: `not_evidenced`;
- campanha local executada: `not_evidenced`.

Conversas anteriores sobre telefone, domínios, polos ou presença internacional não promovem esses objetos a operação real.

## 7. Gate de entrada internacional

A passagem de `T3_readiness_assessment` para `T4_design_approved` exige, no mínimo:

1. product-market fit operacional mínimo no Brasil;
2. retenção e qualidade de receita compatíveis com expansão;
3. oferta local suficiente;
4. capacidade de suporte internacional;
5. modelo de aquisição e vendas;
6. estrutura contratual revisada;
7. análise fiscal e de faturação;
8. análise de pagamentos/chargebacks;
9. avaliação de proteção de dados e transferências;
10. avaliação de consumidor/e-commerce, quando aplicável;
11. avaliação de obrigações específicas de plataforma/marketplace, quando aplicável;
12. posição de marca e ativos digitais adequada ao risco;
13. terceiros críticos identificados;
14. owner executivo;
15. orçamento e limites de perda;
16. métricas e critérios de encerramento do piloto.

## 8. Proteção de dados Brasil–União Europeia

O RGPD pode alcançar controlador ou operador estabelecido fora da União Europeia quando oferece bens/serviços a pessoas na União ou monitora o seu comportamento dentro da União. A ausência de entidade europeia não elimina automaticamente a incidência regulatória.

Em 2026, Brasil e União Europeia adotaram decisões mútuas de adequação para transferências internacionais de dados pessoais. Isso reduz fricção no fluxo coberto pelas decisões, mas não elimina deveres de finalidade, transparência, segurança, direitos, minimização, retenção, contratos ou incidentes.

Referências oficiais para revalidação antes do piloto:

- RGPD: `https://eur-lex.europa.eu/eli/reg/2016/679/oj`
- Comissão Europeia — aplicação do RGPD: `https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en`
- Comissão Europeia — adequação: `https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en`
- ANPD — transferências internacionais: `https://www.gov.br/anpd/pt-br/assuntos/assuntos-internacionais/transferencia-internacional-de-dados`
- ANPD — Resolução CD/ANPD nº 32/2026.

Adequação Brasil–UE ≠ permissão irrestrita de compartilhamento.

## 9. Fiscalidade, IVA e faturação

A expansão europeia exige avaliação por modelo de receita, contraparte, natureza da oferta, localização do fornecedor, localização do cliente e papel efetivo da Guivos.

O VAT/IVA europeu possui regras distintas para B2B, B2C, bens, serviços, conteúdo digital e operações facilitadas por plataformas. O OSS pode ser relevante em determinados fluxos, inclusive para empresas não estabelecidas na UE, mas sua aplicabilidade deve ser validada contra o modelo real.

Referências oficiais:

- `https://europa.eu/youreurope/business/taxation/vat/cross-border-vat/index_en.htm`
- `https://europa.eu/youreurope/business/taxation/vat/one-stop-shop/index_en.htm`

O GKR não declara regime fiscal, número de IVA, registro OSS ou obrigação concreta antes da análise aplicável.

## 10. Consumidor, e-commerce e plataformas

Quando houver oferta direcionada a consumidores na UE, deverão ser avaliadas regras de informação pré-contratual, contratação à distância, cancelamento, garantias, preço, pagamentos, entrega e serviços/conteúdo digital.

Quando um Produto Especializado atuar como marketplace, plataforma intermediária, serviço de viagem, mídia social ou outro serviço regulado, deverão ser avaliadas obrigações específicas do papel real — inclusive, quando aplicável, o Digital Services Act e regras de segurança/proveniência de produtos.

Referências oficiais:

- `https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_en.htm`
- `https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-services-act_en`

A existência de Mall, Travel, Media, Ads ou Journey não prova isoladamente a aplicabilidade de uma obrigação específica.

## 11. Entidade local e presença física

A decisão de criar entidade, filial, estabelecimento, escritório, representação ou equipe local é separada da decisão de realizar piloto.

A análise deverá considerar, conforme o desenho real:

- contratação e representação;
- risco tributário/estabelecimento permanente;
- faturação;
- emprego e prestação de serviços;
- licenças e atividades reguladas;
- propriedade intelectual;
- contas e pagamentos;
- governança;
- proteção de dados;
- responsabilidade por consumidor e parceiros.

## 12. Ativos digitais e marca

Por `GKR-DIGITAL-ASSET-CONTROL-001`:

```text
domínio desejado
≠ domínio controlado
≠ DNS controlado
≠ serviço ativo
≠ operação territorial
```

Estratégia defensiva em `.pt`, `.eu` ou outros territórios pode existir antes da entrada operacional e deve permanecer classificada como proteção de ativo.

## 13. Métricas por praça

- densidade de oferta útil;
- Pessoas cadastradas, ativadas, MAU e retenção;
- Coletivos/Organizações qualificados e ativos;
- Business e Parcerias Estratégicas por objeto da relação;
- CAC e conversão;
- receita/margem;
- custo de suporte;
- incidentes e reclamações;
- chargebacks/falhas de pagamento;
- direitos de titulares;
- desempenho de terceiros críticos;
- concentração de oferta/receita;
- NPS/CSAT quando aprovado.

Crescimento não substitui qualidade, conformidade ou propósito.

## 14. Kill criteria

O piloto pode ser pausado ou encerrado quando houver, entre outros:

- densidade insuficiente;
- retenção incompatível;
- economics inadequados;
- suporte incapaz de manter qualidade;
- risco jurídico/operacional não mitigado;
- pagamentos/faturação inviáveis;
- dependência crítica de parceiro;
- custo de adaptação superior à hipótese de valor;
- expansão sem aprendizado replicável.

## 15. Segundo país europeu

Nenhum segundo país europeu é autorizado por calendário ou volume de cadastros.

```text
piloto português evidenciado
+ retenção
+ economics
+ operação estável
+ compliance operacional
+ suporte
+ playbook replicável
+ razão estratégica
+ autorização executiva
```

## 16. Limites

Este documento não inicia operação em Portugal; não cria empresa, filial, conta bancária, número fiscal/IVA, PSP, equipe, domínio, marca, Termos, Política de Privacidade, representante europeu ou obrigação concreta de DSA/OSS/IVA. Também não inicia UXA-102/V5 nem retoma Product Engineering.
