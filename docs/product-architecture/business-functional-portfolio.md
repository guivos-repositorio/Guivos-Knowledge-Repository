---
id: GPA-004-FUNCTIONAL-PORTFOLIO-001
title: Guivos Business — Portfólio Funcional v1
status: consolidated
version: 1.0.0
owner: Guivos
last_updated: 2026-08-15
depends_on:
  - GPA-004
related:
  - PAS-001
  - GPA-006
  - GPA-007
normative: true
---

# Guivos Business — Portfólio Funcional v1

## 1. Autoridade

Este documento complementa `GPA-004 — Guivos Business` e consolida o **portfólio funcional v1** validado para o produto.

Ele não cria a Home Pública do Business, não define preços finais, não cria entitlements contratuais e não transforma capacidades transversais do ecossistema em módulos pertencentes ao Business.

As separações obrigatórias permanecem:

```text
Organização ≠ Guivos Business
Guivos Business ≠ Guivos Ads
Guivos Intelligence ≠ módulo do Guivos Business
Guivos Journey ≠ propriedade da empresa
Pontos Guivos ≠ medida de evolução
```

## 2. Tese funcional

Guivos Business permite que uma **EMPRESA** utilize capacidades do ecossistema Guivos para:

- incentivar participação e comportamentos empresariais legítimos;
- oferecer benefícios e recompensas com utilidade real no ecossistema;
- custear acesso ao Guivos Journey sem controlar a Journey da pessoa;
- compreender, por meio do Guivos Intelligence, dados e movimentos gerados dentro da Guivos;
- ampliar possibilidades para pessoas sem transformar evolução em controle corporativo.

A pergunta de direção permanece:

> **Como podemos ajudar os seres humanos a terem uma vida melhor?**

## 3. Portfólio principal

O portfólio funcional v1 possui **duas ofertas principais**.

```text
GUIVOS BUSINESS
├── 1. PROGRAMAS DE INCENTIVO
└── 2. GUIVOS JOURNEY CUSTEADO PELA EMPRESA

CAPACIDADES TRANSVERSAIS RELACIONADAS
├── Pontos Guivos
├── Guivos Intelligence
├── integrações/eventos
├── transações e liquidação
└── governança/gestão empresarial
```

As capacidades transversais não constituem automaticamente novas ofertas comerciais independentes.

## 4. Oferta 1 — Programas de Incentivo

### 4.1 Finalidade

A empresa pode estruturar programas destinados a públicos elegíveis, definindo objetivos, eventos verificáveis, regras e benefícios.

Dois recortes comerciais principais utilizam o mesmo núcleo:

```text
FUNCIONÁRIOS
→ engajamento
→ reconhecimento
→ assiduidade
→ comprometimento traduzido em critério observável
→ desempenho/metas legítimas
→ treinamento/certificação
→ segurança
→ inovação
→ sustentabilidade
→ impacto

CLIENTES
→ fidelização
→ recorrência
→ aquisição
→ indicação
→ ativação
→ campanhas
→ relacionamento
```

A existência desses recortes não exige dois motores separados.

### 4.2 Objetos funcionais

O núcleo do Programa de Incentivo é composto por:

```text
Programa
→ Campanha
→ Participante
→ Evento
→ Regra
→ Resultado
→ Orçamento/financiamento
→ Intelligence
```

A lógica básica é:

```text
EVENTO
+
CONDIÇÕES
→ RESULTADO
```

A empresa define o critério empresarial legítimo. A Guivos executa a regra configurada/contratada.

### 4.3 Resultados possíveis

Uma regra pode resultar em:

- Pontos Guivos;
- benefício direto elegível;
- `VALOR DE IMPACTO LIBERADO` quando houver finalidade social legítima.

`VALOR DE IMPACTO LIBERADO` não entra no saldo pessoal de Pontos Guivos e não constitui prova de impacto realizado.

## 5. Oferta 2 — Guivos Journey custeado pela EMPRESA

### 5.1 O produto não muda de identidade

A empresa pode custear acessos ao **Guivos Journey existente**.

Não deve ser criado novo produto ou nome como:

- Journey para Empresas;
- Journey Business;
- Journey Corporativo;
- Journey Patrocinado.

A regra é:

> **Continua sendo Guivos Journey. O que muda é quem paga o acesso.**

### 5.2 Autoridade da pessoa

O Journey custeado pela empresa preserva:

- voluntariedade;
- planos e regras normais do Journey;
- escolha livre das jornadas pela pessoa;
- autoridade da pessoa sobre seu contexto;
- privacidade;
- pertinência e recomendação governadas pelo Journey.

A empresa não pode restringir os temas de evolução disponíveis para tentar direcionar o que as pessoas devem escolher.

### 5.3 Caminho rejeitado

A empresa **não cria jornadas corporativas próprias** dentro do Journey para transformar o produto em LMS, LXP, curso obrigatório, trilha interna ou sequência de tarefas bonificadas.

```text
EMPRESA CUSTEIA O JOURNEY
≠
EMPRESA CRIA/CONTROLA A JOURNEY
```

## 6. Pontos Guivos no Business

### 6.1 Papel

Pontos Guivos são benefício transacional do ecossistema e podem ser concedidos por Programas de Incentivo autorizados.

A equivalência econômica `X pontos = Y reais` já validada permanece vigente e **não é reaberta por este documento**.

### 6.2 Saldo da pessoa

A direção funcional é de um saldo unificado para a pessoa, com origens/lotes preservados internamente para rastreabilidade.

```text
Empresa X → +500
Empresa Y → +300

Pessoa → saldo 800 Pontos Guivos
```

A origem não cria carteiras corporativas separadas visíveis como experiência padrão.

### 6.3 Orçamento da empresa

A empresa carrega previamente orçamento para o programa.

A leitura administrativa validada é:

```text
CARREGADO
CONCEDIDO
DISPONÍVEL
```

`Concedido` representa valor já alocado/consumido do orçamento empresarial no momento em que os pontos são entregues à pessoa.

O uso posterior dos pontos pela pessoa não reabre o saldo da empresa.

### 6.4 Utilização agregada

A empresa não precisa acompanhar pontos ainda guardados pela pessoa ou pontos expirados como decomposição principal de uso.

A métrica validada é a distribuição de **pontos efetivamente utilizados**:

```text
Mall ...... X%
Travel .... Y%
Journey ... Z%
           ----
           100%
```

A distribuição:

- considera somente usos efetivos;
- exclui pontos não utilizados;
- exclui pontos expirados;
- não expõe consumo individual.

### 6.5 Onde podem ser utilizados

Pontos podem ser utilizados em possibilidades pagas elegíveis do:

- Guivos Mall;
- Guivos Travel;
- Guivos Journey, desde que a possibilidade tenha sido apresentada normalmente pelo Journey.

Pontos não alteram descoberta, pertinência, recomendação, prioridade ou `Next Step`.

### 6.6 Plano Journey não é pago com pontos

```text
PLANO JOURNEY
→ segue a regra normal do plano

POSSIBILIDADE PAGA ELEGÍVEL NO JOURNEY
→ pode admitir Pontos Guivos como forma de pagamento
```

### 6.7 Organizações, Coletivos e fornecedores

Uma Organização, Coletivo ou outro fornecedor de possibilidade paga elegível **não precisa operar carteira de Pontos Guivos nem decidir manualmente “aceitar pontos”**.

A Guivos governa a forma de pagamento disponível e processa a transação:

```text
PESSOA
→ paga na plataforma
→ dinheiro / pontos / forma mista elegível
→ GUIVOS processa
→ GUIVOS realiza repasse financeiro
→ FORNECEDOR / ORGANIZAÇÃO / COLETIVO
```

O fornecedor recebe valor financeiro conforme sua relação comercial; não precisa receber Pontos Guivos nem conhecer sua origem.

### 6.8 Pagamento misto

`Pontos + dinheiro` é uma direção funcional validada para possibilidades elegíveis.

A mecânica operacional detalhada depende de regra própria de checkout, estorno e liquidação.

## 7. Expiração e orçamento não concedido

A arquitetura suporta validade de pontos para a pessoa. O exemplo discutido foi 24 meses, mas o prazo exato ainda não é autoridade congelada.

A direção de produto é:

```text
PONTOS JÁ CONCEDIDOS
→ pertencem ao saldo da pessoa durante sua validade
→ não retornam automaticamente à empresa de origem

ORÇAMENTO EMPRESARIAL NÃO CONCEDIDO
→ permanece saldo empresarial
→ pode admitir transferência/estorno conforme contrato
```

A destinação econômica de pontos expirados, prazo final e taxas administrativas exigem regra específica antes de implementação.

## 8. Guivos Intelligence no Business

### 8.1 Fonte de dados

No contexto Business, o Intelligence trabalha com **dados, interações e eventos gerados ou legitimamente conhecidos dentro da Guivos**.

A arquitetura padrão não depende de importar bases completas de:

- RH;
- folha;
- absenteísmo;
- produtividade;
- vendas;
- CRM;
- ERP.

Integrações podem transmitir o **evento mínimo necessário** para acionar uma regra.

Exemplo:

```text
sistema empresarial
→ “evento elegível confirmado”
→ Guivos Business
→ regra
→ benefício
```

### 8.2 Resultado Guivos versus resultado empresarial

```text
RESULTADO OBSERVADO NA GUIVOS
≠
RESULTADO OPERACIONAL INTERNO DA EMPRESA
```

Guivos pode informar participação, concessões, recorrência, orçamento, utilização e movimentos produzidos em seu ecossistema.

A empresa combina esses indicadores com seus KPIs internos em seu próprio ambiente quando desejar analisar relações mais amplas.

### 8.3 Comparações mensais

Comparações mês atual versus mês anterior, tendências e sínteses interpretativas do Guivos Intelligence são direção validada para **diferenciação de planos superiores**.

O entitlement exato ainda precisa ser formalizado.

### 8.4 Exportação e API

Exportação estruturada/API para que a empresa leve indicadores Guivos ao Power BI, Tableau, Looker, Data Lake ou ambiente equivalente também é direção validada para níveis mais avançados do Business.

A Guivos fornece dados/inteligência do próprio ecossistema; o cruzamento com dados corporativos ocorre no ambiente da empresa.

## 9. Intelligence do Journey custeado pela empresa

Quando a empresa custeia acessos Journey, o Intelligence pode produzir leitura agregada e protegida de sinais como:

- interesses de evolução;
- tendências;
- temas emergentes;
- movimentos temporais;
- aderência com benefícios/iniciativas empresariais cadastrados;
- lacunas;
- subutilização quando conhecida pela Guivos.

Regras semânticas:

```text
interesse ≠ condição
intenção ≠ diagnóstico
tema ≠ problema
escolha ≠ causa
```

A empresa não recebe score individual de evolução, Journey individual ou explicação individual de pertinência.

## 10. Planos Business

A taxonomia permanece:

```text
Start
Growth
Scale
Enterprise
```

O plano não determina qual oferta pode ser contratada.

A empresa pode contratar:

- Programas de Incentivo;
- acessos Guivos Journey;
- ambas as ofertas.

O plano governa profundidade de capacidade, Intelligence, integração, governança, escala e serviço.

Direção de referência:

```text
START → operar
GROWTH → acompanhar e compreender
SCALE → interpretar e integrar
ENTERPRISE → governar em alta complexidade/escala
```

Preços e entitlements finais ainda não estão definidos.

## 11. Estrutura econômica do contrato Business

A arquitetura comercial separa:

```text
PLANO BUSINESS
+
ESCALA / PARTICIPANTES / ACESSOS
+
OFERTAS CONTRATADAS
+
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
+
SERVIÇOS ADICIONAIS, QUANDO APLICÁVEIS
```

O orçamento pré-pago não é a assinatura do plano Business.

Acesso Journey custeado pela empresa possui relação econômica própria e não deve ser considerado automaticamente incluído em qualquer plano Business.

## 12. Serviço

A separação conceitual aceita é:

```text
PLANO
= capacidade tecnológica/comercial

SERVIÇO
= nível de participação da Guivos na implantação/operação
```

Foram trabalhados como direção:

- Self-service;
- Assisted;
- Managed.

Os nomes e escopos finais ainda não são entitlements contratuais congelados.

## 13. Relação econômica com outros produtos

Business pode aumentar circulação em Mall, Travel e possibilidades econômicas apresentadas no Journey, mas cada produto preserva sua autoridade e sua receita própria.

Uma empresa cliente Business também pode contratar Guivos Ads em relação independente.

### 13.1 Ads não pertence ao Business

```text
Guivos Business
≠
Guivos Ads
```

Ads não é módulo, upsell interno, benefício de plano, inventário do Business ou extensão de Programa de Incentivo.

O cross-sell comercial pode existir entre produtos, mas a receita de Ads pertence ao domínio econômico de Ads.

## 14. Itens não definidos por este portfólio

Este documento não congela:

- preços;
- limites quantitativos;
- SLAs;
- regra final de expiração de pontos;
- percentuais/destino econômico de pontos expirados;
- política completa de reversão/fraude;
- regra de múltiplos lotes de pontos;
- outras origens autorizadas de pontos;
- multi-moeda;
- comissão/margem transacional específica;
- detalhes fiscais, contábeis ou jurídicos;
- arquitetura técnica de API;
- thresholds de privacidade/coorte;
- Home Pública do Guivos Business.

## 15. Preservação final

O portfólio funcional v1 deve ser retomado pela seguinte leitura:

```text
EMPRESA
├── pode criar PROGRAMAS DE INCENTIVO
│   └── benefícios / Pontos / Valor de Impacto Liberado
│
└── pode CUSTEAR GUIVOS JOURNEY
    └── Journey continua pertencendo à experiência da pessoa

GUIVOS INTELLIGENCE
→ apoia as duas relações com dados/eventos Guivos
→ não se torna módulo Business

GUIVOS ADS
→ permanece produto totalmente distinto
```

A futura Home Pública do Guivos Business deve explicar esse valor sem transformar a página em catálogo técnico, sem confundir Business com Organização e sem apresentar Ads como parte da oferta Business.