---
id: GEM-007-CROSS-PRODUCT-VALUE-ATTRIBUTION-001
title: Atribuição de Valor entre Produtos
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-007
---

# Atribuição de Valor entre Produtos

## 1. Objetivo

Definir princípios para reconhecer contribuições de vários produtos sem dupla contagem, causalidade presumida ou apropriação indevida de receita, impacto ou resultado.

## 2. Tipos de atribuição

### Origem

Produto que inicia descoberta, contexto ou demanda.

### Assistência

Produto que contribui para compreensão, confiança ou avanço do fluxo.

### Influência

Produto associado a uma mudança observada, sem causalidade comprovada.

### Conversão

Produto responsável pelo evento comercial principal.

### Entrega

Produto ou parceiro responsável pelo valor efetivamente disponibilizado.

### Retenção

Produto que contribui para continuidade, renovação ou relacionamento.

### Financiamento

Produto que organiza a fonte econômica ou patrocínio.

### Evidência

Produto que produz registros sobre entrega, utilização ou resultado.

### Suporte

Produto que trata dúvidas, falhas, cancelamento ou disputa.

## 3. Estados

- `direct`;
- `assisted`;
- `shared`;
- `unresolved`;
- `not_attributable`.

## 4. Regras

- o mesmo valor não poderá ser registrado integralmente em vários produtos;
- influência não será causalidade automática;
- visualização não será conversão automática;
- clique não será valor realizado automático;
- origem não substitui entrega;
- produto que financia não recebe autoridade sobre evidência;
- receita consolidada deverá eliminar duplicidades futuras;
- repasse não será receita atribuível;
- recursos vinculados deverão manter sua finalidade;
- custos compartilhados não poderão desaparecer da análise;
- atribuição local não poderá prejudicar o resultado do ecossistema.

## 5. Janela e modelo de atribuição

O GEM-007 não define:

- janela temporal;
- first-touch;
- last-touch;
- modelo multi-touch;
- pesos;
- percentual;
- algoritmo;
- regra contábil.

Essas decisões exigirão evidência, objetivo de medição e validação separada.

## 6. Exemplos

### Journey → Mall

Journey poderá receber atribuição de origem ou assistência. Mall poderá receber atribuição de conversão e coordenação transacional. Fornecedor permanece relacionado à entrega.

### Media → Business

Media poderá receber atribuição de influência ou assistência; Business permanece responsável pela relação institucional e pela contratação futura.

### Ads → Travel

Ads poderá receber atribuição direta da campanha identificada; Travel permanece responsável pela reserva e experiência turística.

### Intelligence transversal

Intelligence poderá receber atribuição por capacidade ou assistência, sem absorver a receita integral do produto consumidor.

## 7. Evidência mínima futura

- identificação do evento;
- produto originador;
- produto responsável;
- relação temporal;
- consentimento aplicável;
- dado minimizado;
- resultado observado;
- limitações;
- duplicidades removidas.

## 8. Guardrails

- atribuição não poderá manipular ranking;
- métrica não poderá justificar vigilância;
- pagamento não poderá comprar crédito causal;
- patrocinador não poderá definir impacto;
- pessoas não serão reduzidas a conversões;
- ausência de evidência deverá resultar em `unresolved` ou `not_attributable`.

## 9. Estado

`conceptually_defined — attribution models and evidence not validated`.
