---
id: GKR-PLANS-BUSINESS-001
title: Planos — Guivos Business
status: active
version: 1.6.0
owner: Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GPA-004
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GEM-004-A1
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
---

# Planos — Guivos Business

Guivos Business é um **produto especializado B2B**. Seus planos são independentes dos planos do participante Organização.

## Resumo

| Plano | Mensal | Anual | Direção funcional |
|---|---:|---:|---|
| **Start** | R$ 299,00 | R$ 2.990,00 | operar |
| **Growth** | R$ 799,00 | R$ 7.990,00 | acompanhar e compreender |
| **Scale** | a partir de R$ 1.990,00 | dimensionado | interpretar e integrar |
| **Enterprise** | sob consulta | sob consulta | governar em alta complexidade e escala |

## Periodicidade

Start, Growth, Scale e Enterprise admitem escolha entre **contratação Mensal** e **contratação Anual**.

- Start e Growth possuem valores mensais e anuais numericamente definidos na baseline vigente.
- Scale preserva referência mensal mínima e exige dimensionamento para o valor anual final.
- Enterprise exige dimensionamento em ambas as periodicidades.

Disponibilidade mensal/anual não autoriza derivar valores ainda não formalizados.

## Contratação e modelo de implementação/operação

A contratação do Guivos Business é **online**.

A implementação/operação pode seguir três modelos correntes:

### Self-service

A empresa contrata online, acessa a plataforma, configura e opera com autonomia.

É o caminho de referência quando a configuração é suficientemente simples, padronizada e apta à contratação digital.

### Com apoio do suporte

A empresa contrata e paga online normalmente. Depois da contratação, o suporte Guivos acompanha a continuidade da implementação quando necessário.

### Gerenciado

A empresa contrata online e, depois, a implementação/operação recebe participação mais profunda da Guivos conforme a complexidade e o contrato.

A síntese vigente é:

> **Self-service quando possível. Suporte quando necessário. Operação gerenciada quando a complexidade exigir.**

### Relação entre plano e modelo de operação

```text
PLANO
→ capacidade contratada

CONTRATAÇÃO
→ online

MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
→ definido pela complexidade da configuração
```

Não congelar equivalências como:

```text
Start = Self-service obrigatório
Enterprise = atendimento humano obrigatório
```

Uma configuração Scale pode ser suficientemente padronizada para operar em Self-service. Uma configuração Growth pode exigir apoio por integração, governança ou outra complexidade específica.

## Como funciona o Self-service dentro da contratação online

Self-service é um **modelo de implementação/operação dentro da contratação online do Guivos Business**. A composição e a contratação permanecem digitais também quando a implementação posterior exigir suporte ou operação gerenciada. Self-service não é um quinto plano, não é uma oferta separada e não significa que tudo esteja incluído na assinatura-base.

A lógica de referência é:

```text
NECESSIDADE DA EMPRESA
↓
OFERTA(S) A UTILIZAR
↓
ESCALA / PARTICIPANTES / ACESSOS
↓
CAPACIDADES NECESSÁRIAS
↓
PLANO COMPATÍVEL
↓
COMPOSIÇÃO DO VALOR
↓
CONTRATAÇÃO ONLINE
↓
CONFIGURAÇÃO E OPERAÇÃO
```

### Quadro de composição Self-service

| Etapa | O que a empresa define ou seleciona | O que isso representa | Pode alterar o plano? | Pode alterar o valor? |
|---|---|---|---|---|
| **1. Oferta** | Programas de Incentivo, Guivos Journey custeado ou ambas as ofertas | o que a empresa pretende utilizar | não determina sozinho o plano | sim, conforme a composição econômica aplicável |
| **2. Escala** | participantes, acessos e demais volumes comercialmente formalizados | quanto da capacidade será utilizada | sim, quando a escala ultrapassar a capacidade do plano | sim |
| **3. Intelligence** | profundidade analítica e capacidades aplicáveis | quanto de compreensão/analytics a configuração exige | sim, conforme os entitlements vigentes | sim, quando houver capacidade comercializada separadamente |
| **4. Integrações e eventos** | integrações necessárias para receber/enviar eventos ou dados autorizados | complexidade de conexão com outros sistemas | sim | sim, quando aplicável |
| **5. Governança** | requisitos de gestão, controle e governança compatíveis com a operação | complexidade administrativa e de controle | sim | pode alterar, conforme a configuração |
| **6. Nível de serviço contratual** | capacidades de serviço previstas no plano/contrato | nível de atendimento e compromisso contratual | pode exigir plano superior | pode alterar |
| **7. Implementação/operação** | Self-service, apoio do suporte ou gerenciado | quanto a Guivos participa da implantação/operação | **não define o plano por si só** | sim, se houver serviço adicional contratado |
| **8. Orçamento de incentivo** | valor que a empresa decide disponibilizar para concessões | recurso operacional pré-pago do programa | **não** | sim, mas fica separado da assinatura |
| **9. Acessos Journey custeados** | quantidade e condição dos acessos elegíveis contratados | custeio empresarial do Journey existente | pode afetar escala/capacidade | sim; possui relação econômica própria |

Os limites quantitativos e thresholds exatos que fazem uma dimensão migrar de Start para Growth, Scale ou Enterprise continuam dependentes dos entitlements comerciais formalmente aprovados. O quadro define a **lógica de composição**, não inventa esses limites.

### O que determina o plano contratado

O plano deve refletir a **maior capacidade necessária para suportar integralmente a configuração escolhida**.

```text
CAPACIDADE OPERACIONAL REQUERIDA
+
ESCALA REQUERIDA
+
INTELLIGENCE REQUERIDO
+
INTEGRAÇÃO REQUERIDA
+
GOVERNANÇA REQUERIDA
+
NÍVEL DE SERVIÇO CONTRATUAL REQUERIDO
↓
PLANO COMPATÍVEL
```

Na contratação digital, cada requisito deve ser comparado aos entitlements vigentes. Se uma única dimensão exigir capacidade superior, a configuração precisa ser enquadrada em um plano que suporte essa dimensão.

Isso evita duas interpretações incorretas:

```text
PLANO
≠ pacote escolhido apenas pelo preço

PLANO
≠ soma arbitrária de módulos
```

O plano é a camada de capacidade que sustenta a configuração contratada.

### O que determina o valor total

O valor total não é necessariamente igual apenas ao preço-base do plano.

A composição econômica deve ser apresentada separadamente:

| Componente | Função econômica | Integra a assinatura-base? |
|---|---|---|
| **Plano Business** | capacidade-base contratada | sim |
| **Escala / participantes / acessos** | volume da operação, quando precificado separadamente | conforme regra comercial |
| **Ofertas contratadas** | Programas de Incentivo e/ou Journey custeado | conforme regra comercial |
| **Acessos Journey custeados** | acesso ao Journey pago pela empresa | relação econômica própria |
| **Intelligence avançado / exportações / API / integrações** | capacidades adicionais, quando comercializadas separadamente | somente quando o entitlement do plano não as incluir |
| **Serviços adicionais** | suporte adicional ou operação gerenciada contratada | não necessariamente |
| **Orçamento pré-pago de incentivo** | recursos destinados às concessões do programa | **não**; fica separado da assinatura |

Leitura de referência:

```text
VALOR RECORRENTE / CONTRATUAL
=
PLANO BUSINESS
+ COMPONENTES VARIÁVEIS APLICÁVEIS
+ SERVIÇOS ADICIONAIS, QUANDO CONTRATADOS

RECURSO OPERACIONAL SEPARADO
=
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
```

O configurador deve mostrar essas parcelas separadamente para que a empresa compreenda **o que está pagando pela capacidade da plataforma, o que varia com sua configuração e o que constitui orçamento operacional do programa**.

### Como os “serviços” ficam distribuídos

No caminho Self-service, a leitura correta não é um catálogo solto de serviços, mas uma composição em camadas:

| Camada | Conteúdo |
|---|---|
| **Plano-base** | Start · Growth · Scale · Enterprise |
| **Ofertas Business** | Programas de Incentivo · Journey custeado · ambas |
| **Capacidades da configuração** | escala · Intelligence · integrações · governança · nível de serviço |
| **Volumes contratados** | participantes · acessos · demais volumes formalizados |
| **Serviços de implantação/operação** | Self-service · suporte adicional · gerenciado |
| **Recursos operacionais** | orçamento pré-pago de incentivo |
| **Condições comerciais** | periodicidade, mercado, moeda, tributação e demais condições aplicáveis |

Self-service significa que, além de **montar, compreender, comparar e contratar a composição digitalmente**, a empresa consegue seguir para a implementação/operação com autonomia quando a configuração for elegível. Configurações com suporte ou operação gerenciada continuam sendo contratadas online; o que muda é a participação da Guivos depois da contratação.

## Calculadora e pricing variável

A contratação Self-service deve suportar uma calculadora baseada em composição versionada:

```text
PLANO-BASE
+ POPULAÇÃO / ESCALA
+ OFERTA(S)
+ ACESSOS JOURNEY CUSTEADOS
+ CAPACIDADES ADICIONAIS
+ SERVIÇOS ADICIONAIS
= VALOR RECORRENTE CONTRATUAL, QUANDO PRECIFICÁVEL

ORÇAMENTO PRÉ-PAGO DE INCENTIVO
= RECURSO OPERACIONAL SEPARADO
```

A calculadora deve receber, no mínimo, periodicidade, população/escala, oferta(s) e volumes aplicáveis.

**Estado econômico atual:** a tabela variável foi adjudicada em `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001`. O configurador possui autoridade numérica para população/escala, ofertas, acessos Journey, capacidades adicionais e serviços adicionais, respeitando os entitlements por tier e mantendo Scale/Enterprise dimensionados quando aplicável.

O contrato de experiência detalhado está em `GKR-UX-PLANS-BUSINESS-CONFIGURATOR-001`.


## Tabela de composição econômica vigente

A contratação Business usa a seguinte composição:

```text
ASSINATURA RECORRENTE / CONTRATUAL
=
PLANO-BASE
+ COMPONENTE DE POPULAÇÃO / ESCALA
+ COMPONENTE DE OFERTA
+ ACESSOS JOURNEY CUSTEADOS
+ CAPACIDADES ADICIONAIS
+ SERVIÇOS ADICIONAIS

RECURSO OPERACIONAL SEPARADO
=
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
```

### População / escala

A base precificável é a **população elegível para a configuração contratada**. A cobrança é progressiva por faixa.

| População elegível | Mensal por pessoa na faixa | Anual por pessoa na faixa |
|---|---:|---:|
| 1–50 | incluído | incluído |
| 51–250 | R$ 1,49 | R$ 14,90 |
| 251–1.000 | R$ 0,99 | R$ 9,90 |
| 1.001–5.000 | R$ 0,69 | R$ 6,90 |
| 5.001–20.000 | R$ 0,49 | R$ 4,90 |
| acima de 20.000 | dimensionado | dimensionado |

```text
POPULATION_COMPONENT
=
SOMA DAS PESSOAS EM CADA FAIXA × TARIFA DA FAIXA
```

A cobrança progressiva evita salto integral de preço quando a população cruza uma faixa.

### Oferta Business

| Oferta | Mensal | Anual |
|---|---:|---:|
| **Programas de Incentivo** | R$ 199,00 | R$ 1.990,00 |
| **Journey custeado** | R$ 99,00 | R$ 990,00 |
| **Incentivos + Journey** | R$ 249,00 | R$ 2.490,00 |

A taxa de Programas de Incentivo habilita a operação do programa. O orçamento destinado às recompensas permanece separado.

A taxa de Journey custeado habilita a gestão empresarial dos acessos; os acessos financiados são cobrados separadamente.

### Acessos Journey Plus custeados

| Quantidade | Mensal por acesso | Anual por acesso |
|---|---:|---:|
| 1–99 | R$ 19,90 | R$ 199,00 |
| 100–499 | R$ 17,90 | R$ 179,00 |
| 500–1.999 | R$ 15,90 | R$ 159,00 |
| 2.000+ | R$ 13,90 | R$ 139,00 |

### Acessos Journey Pro custeados

| Quantidade | Mensal por acesso | Anual por acesso |
|---|---:|---:|
| 1–99 | R$ 39,90 | R$ 399,00 |
| 100–499 | R$ 35,90 | R$ 359,00 |
| 500–1.999 | R$ 31,90 | R$ 319,00 |
| 2.000+ | R$ 27,90 | R$ 279,00 |

A faixa de Journey é determinada pela quantidade total de acessos custeados daquela modalidade no contrato.

### Capacidades adicionais

Uma capacidade só gera add-on quando **não estiver incluída no tier contratado**.

| Capacidade | Mensal | Anual |
|---|---:|---:|
| **Intelligence avançado** | R$ 299,00 | R$ 2.990,00 |
| **Exportações automatizadas / Power BI** | R$ 249,00 | R$ 2.490,00 |
| **API Business** | R$ 399,00 | R$ 3.990,00 |
| **SSO / SAML** | R$ 299,00 | R$ 2.990,00 |
| **Governança e trilha de auditoria avançadas** | R$ 249,00 | R$ 2.490,00 |
| **Integração dedicada adicional** | R$ 490,00 | R$ 4.900,00 |

### Inclusões mínimas por tier

| Capacidade | Start | Growth | Scale | Enterprise |
|---|---|---|---|---|
| Intelligence avançado | adicional | incluído | incluído | incluído |
| Exportações automatizadas / Power BI | adicional | adicional | incluído | incluído |
| API Business | adicional | adicional | incluído | incluído |
| SSO / SAML | adicional | adicional | incluído | incluído |
| Governança / auditoria avançadas | adicional | incluído | incluído | incluído |
| 1 integração dedicada | adicional | adicional | incluída | incluída conforme contrato |
| Integrações dedicadas adicionais | adicional | adicional | R$ 490/mês por integração | dimensionado |

```text
CAPACIDADE INCLUÍDA NO TIER
→ ADD-ON = R$ 0,00
```

### Serviços adicionais

| Serviço | Mensal | Anual |
|---|---:|---:|
| **Self-service** | R$ 0,00 | R$ 0,00 |
| **Suporte ampliado** | R$ 299,00 | R$ 2.990,00 |
| **Operação gerenciada** | R$ 990,00 | R$ 9.900,00 |
| **Gestão dedicada / SLA ampliado** | R$ 1.990,00 | R$ 19.900,00 |
| **Projeto de implantação customizada** | sob consulta | sob consulta |

Serviço adicional não define automaticamente o plano-base e não deve ser cobrado separadamente quando estiver expressamente incorporado ao contrato.

### Orçamento pré-pago de incentivo

| Item | Regra |
|---|---|
| Valor | definido pela empresa |
| Integra a assinatura recorrente | não |
| Impacto na assinatura | R$ 0,00 |
| Natureza | recurso operacional pré-pago |
| Uso | conforme regras do programa e saldo disponível |

```text
INCENTIVE PROGRAM FEE
≠ INCENTIVE BUDGET
```

Nenhum markup, spread, taxa de resgate ou expiração econômica é criado por esta tabela.

## Start

**Preço:** R$ 299,00/mês · R$ 2.990,00/ano
**Função:** estabelecer a operação empresarial inicial do produto.

### Leitura

- começar uma operação Business estruturada;
- operar com escopo controlado e capacidades essenciais;
- acessar o núcleo do produto sem transformar o plano em medida de mérito ou impacto.

## Growth

**Preço:** R$ 799,00/mês · R$ 7.990,00/ano
**Função:** ampliar recorrência, públicos, unidades e capacidade analítica.

### Leitura

- acompanhar e compreender a operação com maior continuidade;
- ampliar coordenação e capacidade analítica;
- aprofundar o uso de Intelligence e governança conforme os entitlements aplicáveis.

## Scale

**Preço:** a partir de R$ 1.990,00/mês · anual dimensionado
**Função:** atender operações amplas, multiunidade e integradas.

### Leitura

- interpretar e integrar em maior escala;
- suportar maior volume, integração e complexidade;
- exigir dimensionamento de capacidade antes da contratação final.

O valor mensal é referência mínima e não substitui o dimensionamento comercial.

## Enterprise

**Preço:** sob consulta na contratação mensal · sob consulta na contratação anual
**Função:** adaptar o produto a contextos empresariais de alta complexidade.

### Leitura

- governar operações de alta complexidade e escala;
- dimensionar capacidade, integração, segurança, governança e suporte;
- tratar configurações e condições contratuais específicas.

Enterprise não possui valor fixo único. O preço resulta do dimensionamento da operação.

## O que o plano governa

O plano Business governa a profundidade contratada de:

- capacidade operacional;
- escala;
- Guivos Intelligence;
- integrações;
- governança;
- nível de serviço.

O nível de serviço não substitui o plano e não constitui uma segunda taxonomia de planos.

Os **entitlements quantitativos que não estejam definidos** permanecem sujeitos à formalização comercial própria. As inclusões mínimas das capacidades adicionais por tier são governadas por `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001` e não podem ser cobradas novamente como add-on quando já incluídas.

## O que a empresa pode contratar

O plano não determina sozinho qual oferta será utilizada. A empresa pode contratar:

- Programas de Incentivo;
- acessos Guivos Journey custeados;
- ambas as ofertas.

A arquitetura econômica separa:

```text
PLANO-BASE
+
POPULAÇÃO / ESCALA
+
OFERTA(S)
+
ACESSOS JOURNEY CUSTEADOS
+
CAPACIDADES ADICIONAIS NÃO INCLUÍDAS NO TIER
+
SERVIÇOS ADICIONAIS
=
ASSINATURA RECORRENTE / CONTRATUAL

ORÇAMENTO PRÉ-PAGO DE INCENTIVO
=
RECURSO OPERACIONAL SEPARADO
```

O orçamento pré-pago não é a assinatura do plano Business. O acesso Journey custeado pela empresa possui relação econômica própria.

## Separação obrigatória

```text
ORGANIZAÇÃO
≠ GUIVOS BUSINESS

Organização Transforma
≠ Business Enterprise
```

Valores iguais entre determinados degraus não criam equivalência funcional entre as duas estruturas.

## Estado comercial

Os preços de Start, Growth, Scale e a condição comercial de Enterprise integram a baseline de referência vigente. Limites quantitativos, SLAs e entitlements contratuais que não estejam expressamente formalizados continuam não inferíveis.

A presença desses valores no GKR não constitui, sozinha, autorização automática de cobrança ou oferta pública.
