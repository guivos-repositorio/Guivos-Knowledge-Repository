---
id: GKR-PLANS-BUSINESS-001
title: Planos — Guivos Business
status: active
version: 1.3.0
owner: Guivos
last_updated: 2026-09-21
normative: false
depends_on:
  - GPA-004
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GEM-004-A1
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
---

# Planos — Guivos Business

Guivos Business é um **produto especializado B2B**. Seus planos são independentes dos planos do participante Organização.

## Resumo

| Plano | Mensal | Anual | Direção funcional |
|---|---:|---:|---|
| **Start** | R$ 299,00 | R$ 2.990,00 | operar |
| **Growth** | R$ 799,00 | R$ 7.990,00 | acompanhar e compreender |
| **Scale** | a partir de R$ 1.990,00 | contrato anual | interpretar e integrar |
| **Enterprise** | sob consulta | contrato anual | governar em alta complexidade e escala |

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

## Como funciona a contratação Self-service

Self-service é o **modelo digital de composição e contratação** da configuração Business. Não é um quinto plano, não é uma oferta separada e não significa que tudo esteja incluído na assinatura-base.

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

Para contratação Self-service, a leitura correta não é um catálogo solto de serviços, mas uma composição em camadas:

| Camada | Conteúdo |
|---|---|
| **Plano-base** | Start · Growth · Scale · Enterprise |
| **Ofertas Business** | Programas de Incentivo · Journey custeado · ambas |
| **Capacidades da configuração** | escala · Intelligence · integrações · governança · nível de serviço |
| **Volumes contratados** | participantes · acessos · demais volumes formalizados |
| **Serviços de implantação/operação** | Self-service · suporte adicional · gerenciado |
| **Recursos operacionais** | orçamento pré-pago de incentivo |
| **Condições comerciais** | periodicidade, mercado, moeda, tributação e demais condições aplicáveis |

Self-service significa que a empresa consegue **montar, compreender, comparar e contratar essa composição digitalmente** sempre que a configuração for elegível para isso.

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

**Preço:** a partir de R$ 1.990,00/mês · contrato anual
**Função:** atender operações amplas, multiunidade e integradas.

### Leitura

- interpretar e integrar em maior escala;
- suportar maior volume, integração e complexidade;
- exigir dimensionamento de capacidade antes da contratação final.

O valor mensal é referência mínima e não substitui o dimensionamento comercial.

## Enterprise

**Preço:** sob consulta · contrato anual
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

Os **entitlements quantitativos finais** de cada capacidade permanecem sujeitos à formalização comercial própria. O pricing de referência não autoriza inferir limites que ainda não tenham sido governados.

## O que a empresa pode contratar

O plano não determina sozinho qual oferta será utilizada. A empresa pode contratar:

- Programas de Incentivo;
- acessos Guivos Journey custeados;
- ambas as ofertas.

A arquitetura econômica separa:

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
