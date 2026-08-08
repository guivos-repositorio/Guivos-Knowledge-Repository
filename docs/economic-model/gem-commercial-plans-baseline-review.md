---
id: GEM-COMMERCIAL-BASELINE-001
title: Revisão da Baseline Comercial de Planos e Preços
status: active
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-08-08
depends_on:
  - GEM-CLOSURE-REVIEW-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GEM-004-A1
  - GEM-004-A2
  - GEM-010-A1
related:
  - GEM-004
  - GEM-010
  - GKR-STATE-001
  - ROADMAP-12.13.0
  - M7.39
normative: true
---

# Revisão da Baseline Comercial de Planos e Preços

## 1. Finalidade

Esta revisão registra a reabertura localizada do Guivos Economic Model para transformar arquétipos conceituais em uma baseline comercial candidata de planos, benefícios, limites e preços.

A reabertura atende aos critérios da Revisão de Fechamento do Modelo Econômico porque planos e preços passaram a exigir contratos específicos, parâmetros rastreáveis e validação separada.

A versão 0.2.0 reconcilia a revisão com a taxonomia vigente e remove a antiga fusão entre Organização e Guivos Business.

## 2. Escopo reaberto

Foram reabertos somente:

- GEM-004 — Modelo Gratuito e Pago;
- parâmetros de preço, custo e validação relacionados do GEM-010.

Os demais módulos GEM-001 a GEM-003 e GEM-005 a GEM-009 permanecem preservados, salvo referências e rastreabilidade necessárias.

## 3. Resultado

> **PASS — commercial plan baseline documentarily defined; market, operational, financial and specialist validation pending.**

O incremento define:

- planos para Pessoas;
- planos para Coletivos;
- Coletivo Rede e sua fronteira de dimensionamento quando aplicável;
- planos para Organizações;
- separação explícita de Guivos Business como Produto Especializado;
- acesso financiado e patrocinado;
- benefícios e limites candidatos;
- preços mensais e anuais candidatos onde existe autoridade econômica aplicável;
- regras de cotas;
- separação entre assinatura e transação;
- pontos legítimos de oferta;
- proteção contra dark patterns;
- upgrade, downgrade e cancelamento;
- premissas de preço e unit economics;
- gates de validação.

## 4. Planos consolidados

### Pessoas

- Guivos Free;
- Guivos Plus;
- Guivos Pro.

### Coletivos

- Coletivo Livre;
- Coletivo Mobiliza;
- Coletivo Impacta;
- Coletivo Rede.

### Organizações

- Organização Conecta;
- Organização Eleva;
- Organização Transforma.

### Guivos Business

Guivos Business é Produto Especializado com taxonomia própria:

- Start;
- Growth;
- Scale;
- Enterprise.

Esta revisão não atribui aos tiers de Business os preços ou entitlements históricos da jornada de Organização.

### Acesso transversal

- Guivos Patrocinado ou financiado, vinculado a prazo, finalidade e capacidade declarados.

## 5. Decisões materiais

1. Guivos Free mantém catálogo público completo e limita somente correspondências personalizadas completas;
2. a cota individual candidata é de duas correspondências personalizadas por semana;
3. oportunidades públicas permanecem acessíveis pelo Explorar e Mapa;
4. Coletivo Livre permite uma atividade gratuita e uma oportunidade gratuita por mês;
5. Coletivo Livre possui até duas publicações simultaneamente ativas;
6. publicação paga exige Coletivo Mobiliza ou superior;
7. Coletivo Mobiliza possui quatro atividades, quatro oportunidades e seis publicações ativas na baseline candidata;
8. Coletivo Impacta possui quinze atividades, quinze oportunidades e vinte publicações ativas na baseline candidata;
9. Coletivo Rede não possui limite padrão fixo, mas capacidade contratada e uso justo;
10. compra de atividade paga independe da assinatura individual;
11. assinatura, transação, comissão, taxa de pagamento e tributo permanecem objetos distintos;
12. plano pago não aumenta ranking, impacto, evidência ou relevância orgânica;
13. Organização ≠ Guivos Business;
14. Organização Transforma ≠ Guivos Business Enterprise.

## 6. Preços candidatos

| Público | Plano | Mensal | Anual |
|---|---|---:|---:|
| Pessoa | Guivos Free | R$ 0,00 | R$ 0,00 |
| Pessoa | Guivos Plus | R$ 24,90 | R$ 249,00 |
| Pessoa | Guivos Pro | R$ 49,90 | R$ 499,00 |
| Coletivo | Coletivo Livre | R$ 0,00 | R$ 0,00 |
| Coletivo | Coletivo Mobiliza | R$ 89,90 | R$ 899,00 |
| Coletivo | Coletivo Impacta | R$ 249,90 | R$ 2.499,00 |
| Coletivo | Coletivo Rede | sob consulta | contrato anual |
| Organização | Organização Conecta | R$ 299,00 | R$ 2.990,00 |
| Organização | Organização Eleva | R$ 799,00 | R$ 7.990,00 |
| Organização | Organização Transforma | a partir de R$ 1.990,00 | contrato anual |

Os valores são parâmetros candidatos para validação e não autorização de cobrança. Eles não constituem preços de Start/Growth/Scale/Enterprise do Guivos Business.

## 7. Proteções confirmadas

- gratuito real;
- catálogo público preservado;
- segurança, dados e direitos fora de paywall;
- limites transparentes e não acumulativos;
- alternativa gratuita visível;
- nenhuma oferta em momento sensível;
- nenhuma conversão por inferência de vulnerabilidade;
- cancelamento proporcional à contratação;
- retorno ao gratuito;
- acesso financiado sem autoridade indevida do financiador;
- publicações existentes sem redução artificial de visibilidade;
- compromissos pagos preservados no downgrade ou cancelamento.

## 8. Pendências materiais

Continuam pendentes:

- pesquisa de disposição a pagar;
- utilidade e comportamento observados;
- custos de infraestrutura e inteligência;
- custos de suporte;
- tributos;
- taxas de pagamento;
- comissão transacional;
- margens;
- CAC, LTV, retenção e churn;
- política de reembolso;
- contratos;
- revisão jurídica, fiscal, contábil, regulatória, de privacidade e segurança;
- implementação de entitlement;
- oferta pública;
- operação;
- autoridade comercial própria de preços e entitlements do Guivos Business.

## 9. Efeito sobre o fechamento anterior

A Revisão de Fechamento GEM-CLOSURE-REVIEW-001 permanece válida como registro da primeira arquitetura documental.

Este overlay:

- não apaga o fechamento histórico;
- não reabre silenciosamente todo o domínio;
- substitui a ausência deliberada de preços e planos comerciais apenas no escopo definido;
- preserva os demais limites e separações;
- torna GEM-004-A1, GEM-004-A2 e GEM-010-A1 autoridades vigentes da baseline comercial candidata, subordinadas à autoridade conceitual de taxonomia quando houver conflito de nomenclatura.

## 10. Parecer de continuidade

A baseline poderá avançar para validação de mercado e modelagem financeira somente por autorização independente.

A integração deste incremento não autoriza:

- pesquisa com participantes;
- teste de preço;
- checkout;
- cobrança;
- desenvolvimento;
- publicação de página de preços;
- oferta comercial.
