---
id: GEM-F1C-M0-M6-EVIDENCE-QUOTE-PACK-001
title: Evidências e Pacotes de Cotação M0–M6 — F1-C
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-F1-M0-M6-COST-BASELINE-001
depends_on:
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
  - GEM-010-COST-AND-CAPACITY-MODEL-001
related:
  - GEM-008-COST-ARCHITECTURE-001
  - GEM-009-COST-AND-UNIT-ECONOMICS-001
  - GTM-001
  - GTM-002
  - GTM-003
normative: true
---

# Evidências e Pacotes de Cotação M0–M6 — F1-C

## 1. Finalidade

Aprofundar a baseline F1 com **evidência pública adicional e especificações de cotação** para os custos materiais ainda abertos em `M0–M6`, sem transformar preço público em fornecedor escolhido, oferta comercial em orçamento, cotação futura em obrigação, ou benchmark em burn.

F1-C responde a quatro perguntas:

1. quais pools adicionais possuem preço público rastreável suficiente para uma referência unitária;
2. quais componentes continuam dependentes de cotação real porque o escopo é específico da Guivos;
3. quais linhas não devem ser cotadas ainda porque falta decisão de escopo, volume ou tecnologia;
4. quanto a cobertura de evidência evolui sem produzir falsa completude financeira.

F1-C **não aprova fornecedor, compra, contratação, orçamento, Product Engineering, mídia paga, evento, presença física, stack, burn, runway ou necessidade de capital**.

## 2. Regra central

```text
preço público
≠ cotação Guivos
≠ fornecedor escolhido
≠ custo contratado
≠ custo realizado
≠ orçamento
```

Uma evidência pública só pode promover uma linha para `unit_benchmark_available`, `formula_benchmark_available` ou `official_fee_available` quando a unidade e o uso forem identificáveis.

Quando o serviço depende de desenho específico, a saída correta é `quote_required` com um pacote mínimo de cotação. Quando falta escopo anterior à própria cotação, a saída correta é `scope_definition_required`.

## 3. Estados F1-C

| Estado | Significado |
|---|---|
| `unit_benchmark_available` | preço público unitário rastreável; quantidade e adoção permanecem pendentes |
| `formula_benchmark_available` | fórmula/tarifa variável pública; volume e incidência permanecem pendentes |
| `official_fee_available` | tarifa oficial pública por unidade/evento |
| `public_offer_benchmark` | preço público existente, mas com condição promocional ou restritiva; não usar como preço permanente |
| `quote_required` | serviço material com escopo suficiente para pedir proposta |
| `scope_definition_required` | não é economicamente responsável pedir cotação antes de definir escopo/driver |
| `budget_decision_and_experiment_required` | custo discricionário depende de decisão de orçamento e desenho de experimento antes de amount |
| `blocked_by_engineering` | depende de reativação e decisão formal de Product Engineering |
| `amount_TBD` | existe referência, mas falta quantidade/aplicabilidade para amount mensal |

## 4. Fontes públicas recuperadas em 2026-08-08

| Fonte primária | Evidência observada | Pool permitido | Limite |
|---|---|---|---|
| Microsoft Defender para Empresas | R$ 13,70 por usuário/mês, pago anualmente; até 300 usuários e até 5 dispositivos por usuário; impostos não incluídos | F1-C04 | benchmark de proteção de endpoint; não cobre toda segurança/privacidade |
| Adobe Express Teams | preço regular de referência R$ 37/mês por licença; oferta inicial observada de R$ 23/mês no primeiro ano; mínimo de 2 licenças | F1-C07 | usar R$ 37 como referência não promocional; não cobre produção terceirizada |
| Prefeitura de Belo Horizonte / SUMOB | tarifa unitária de referência de ônibus/MOVE de R$ 6,25 em 2026, com linhas e integrações específicas em R$ 6,00 e outros complementos | F1-C09 | benchmark de transporte coletivo local; não cobre táxi/app/km/reembolso |
| Sympla | 10% de taxa de serviço + 2% a 2,5% por venda para eventos pagos; transferência de R$ 7,50 por evento em bancos fora do grupo indicado pela plataforma | F1-C12 | somente se evento pago usar a plataforma; evitar dupla contagem com F1-C13 |
| Zendesk Support Team | R$ 135 por agente/mês, pago anualmente | F1-C15 | benchmark de ferramenta de help desk; não equivale a mão de obra de suporte/moderação |
| Registro.br | manutenção normal de domínio .br: R$ 40 por 1 ano e R$ 76 por 2 anos | F1-C16 | tarifa pública de manutenção .br; disponibilidade/número de domínios continuam pendentes |

### URLs

- Microsoft Defender para Empresas: `https://www.microsoft.com/pt-br/security/business/endpoint-security/microsoft-defender-business`
- Adobe Express: `https://www.adobe.com/br/express/pricing`
- PBH/SUMOB — tarifas e integrações: `https://prefeitura.pbh.gov.br/sumob/onibus/tarifas-e-integracoes`
- Sympla — recebimento e taxas: `https://ajuda.sympla.com.br/hc/pt-br/articles/204767395-Como-Receber-Suas-Vendas-na-Conta-Banc%C3%A1ria`
- Zendesk — pricing: `https://www.zendesk.com.br/pricing/`
- Registro.br — processo de liberação/manutenção: `https://registro.br/dominio/processo-de-liberacao/`

## 5. Novas calibrações públicas

### 5.1 F1-C04 — segurança, privacidade e controles técnicos

```yaml
pool: F1-C04
subcost: endpoint_security_reference
unit_rate_brl: 13.70
unit: usuario_mes
billing: annual_commitment
value_state: benchmark
calibration_state: unit_benchmark_available
source: Microsoft Defender para Empresas
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

Uso permitido:

- referência de ordem de grandeza para proteção de endpoint de pequena empresa;
- quantidade de usuários/dispositivos permanece `TBD`;
- impostos permanecem fora do valor público informado.

Não cobre:

- pentest;
- gestão de vulnerabilidades externa;
- SOC/MDR;
- DLP/identidade avançada além do produto de referência;
- privacidade/LGPD;
- resposta a incidentes;
- arquitetura de segurança da plataforma.

Portanto, F1-C04 passa a **parcialmente calibrado**, mas continua `quote_required` para controles especializados quando aplicáveis.

### 5.2 F1-C07 — marca, conteúdo e produção criativa

```yaml
pool: F1-C07
subcost: creative_collaboration_tool_reference
regular_unit_rate_brl: 37.00
observed_first_year_offer_brl: 23.00
unit: licenca_mes
minimum_licenses: 2
value_state: benchmark
calibration_state: unit_benchmark_available
source: Adobe Express Teams
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

Regras:

- a referência econômica deve usar **R$ 37/licença/mês**, não a oferta temporária de R$ 23;
- quantidade de licenças e decisão de ferramenta permanecem `TBD`;
- produção de vídeo, fotografia, motion, identidade, peças especiais, impressão e agência/freelancer continuam `quote_required` quando ativados.

### 5.3 F1-C09 — prospecção, reuniões e deslocamentos BH

```yaml
pool: F1-C09
subcost: public_transport_bh_reference
unit_rate_brl: 6.25
unit: embarque_referencia
value_state: benchmark
calibration_state: unit_benchmark_available
source: PBH/SUMOB
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

A tarifa é referência de transporte coletivo local para 2026. Existem linhas de R$ 6,00, integrações e complementos específicos; por isso F1-C não cria custo médio por reunião.

Continuam `TBD`:

- número de deslocamentos;
- política de reembolso;
- uso de táxi/aplicativo;
- estacionamento;
- alimentação/hospedagem;
- quilometragem e veículo próprio.

### 5.4 F1-C12 — lançamento, eventos e presença de campo BH

Para **evento pago e somente se a Sympla for adotada**, existe fórmula pública:

```yaml
pool: F1-C12
subcost: paid_event_ticketing_reference
benchmark_formula:
  service_fee: "10% * vendas_evento"
  processing_fee: "2.0%..2.5% * vendas_evento"
  bank_transfer_if_applicable: "R$7.50 * evento"
value_state: benchmark
calibration_state: formula_benchmark_available
source: Sympla
amount_brl: TBD
confidence_source: high
confidence_applicability: low
activation_gate: paid_event_and_platform_adopted
```

Regras de reconciliação:

- evento gratuito não recebe automaticamente essas taxas;
- se a Sympla processar pagamentos do evento, não aplicar Stripe/F1-C13 ao mesmo volume;
- venue, audiovisual, alimentação, equipe, mobiliário, sinalização, fotografia, segurança e produção continuam `quote_required`;
- F1-C não autoriza evento pago nem escolha da Sympla.

### 5.5 F1-C15 — suporte, moderação, curadoria e prevenção de fraude

```yaml
pool: F1-C15
subcost: helpdesk_tool_reference
unit_rate_brl: 135.00
unit: agente_mes
billing: annual_commitment
value_state: benchmark
calibration_state: unit_benchmark_available
source: Zendesk Support Team
amount_brl: TBD
confidence_source: high
confidence_applicability: medium
```

Esse benchmark é **software de suporte**, não salário, contractor ou capacidade humana.

Continuam pendentes:

- quantidade de agentes/usuários de ferramenta;
- canal e SLA;
- carga de tickets;
- moderação de conteúdo;
- trust & safety;
- antifraude;
- escalação humana/especialista.

### 5.6 F1-C16 — domínios, marca, PI e ativos institucionais

F1-B já governa tarifas do INPI. F1-C adiciona domínio `.br`:

```yaml
pool: F1-C16
subcost: dominio_br_maintenance
unit_rate_brl:
  one_year: 40.00
  two_years: 76.00
unit: dominio_periodo
value_state: benchmark
calibration_state: official_fee_available
source: Registro.br
amount_brl: TBD
confidence_source: high
confidence_applicability: high
```

A quantidade de domínios, disponibilidade, categorias e período de manutenção permanecem `TBD`.

Processos competitivos de liberação possuem dinâmica própria e **não** devem ser modelados como custo normal de domínio.

## 6. Pacotes mínimos de cotação

F1-C não inventa preço onde o serviço é customizado. Define apenas o conteúdo mínimo que uma futura cotação deverá possuir.

### Q04 — segurança/privacidade especializada

Aplicável quando o gate exigir cobertura além do benchmark de endpoint.

Solicitar, no mínimo:

- escopo e ativos cobertos;
- avaliação inicial/risk assessment;
- pentest/vulnerability assessment quando aplicável;
- monitoramento/MDR/SOC quando aplicável;
- resposta a incidentes;
- horas/franquia e excedentes;
- periodicidade;
- prazo de implantação;
- SLA;
- impostos;
- vigência e renovação;
- exclusões.

Estado: `quote_required — scope must be mapped before vendor comparison`.

### Q06 — jurídico, privacidade e compliance

Solicitar separadamente para evitar pacote opaco:

1. jurídico societário/contratual;
2. LGPD/privacy advisory;
3. Encarregado/DPO-as-a-service, se aplicável;
4. revisão de Termos/Políticas;
5. contratos/parcerias e demandas extraordinárias.

Campos mínimos:

- fee mensal ou por entrega;
- horas incluídas/excedentes;
- escopo documental;
- SLA;
- canal de atendimento;
- representação/contencioso incluído ou não;
- impostos;
- vigência.

Estado: `quote_required`.

### Q07 — produção criativa

Cotação somente após existir calendário/brief mínimo.

Separar:

- identidade/brand assets;
- social/content design;
- vídeo/motion;
- fotografia;
- copy/roteiro;
- impressão/material físico;
- agência versus freelancer versus produção pontual.

Campos mínimos:

- unidade de entrega;
- quantidade;
- revisões;
- direitos/licenciamento;
- prazo;
- arquivos-fonte;
- impostos;
- recorrência.

Estado: `quote_required after content scope`.

### Q12 — lançamento/eventos/campo

Antes de pedir preço, registrar:

- objetivo do evento;
- público/capacidade;
- duração;
- região de BH;
- gratuito ou pago;
- formato presencial/híbrido;
- necessidade de venue, AV, catering, mobiliário, recepção, segurança, fotografia e sinalização.

A proposta deve separar cada componente e impostos.

Estado: `quote_required after event format`.

### Q15 — suporte/moderação/trust & safety/fraude

Cotação especializada somente quando houver driver observável ou requisito definido.

Solicitar:

- canal;
- janela de cobertura;
- volume incluído;
- SLA;
- idiomas;
- moderação humana/automática;
- tratamento de incidentes e escalonamento;
- fraude/contestação incluída ou não;
- ferramenta incluída ou separada;
- preço fixo, variável e excedentes;
- impostos.

Estado: `quote_required after service model`.

### Q18 — integrações/coordenação/reconciliação

Não pedir cotação genérica de “integração”. Primeiro identificar integração efetivamente autorizada.

Para cada integração futura, registrar:

- sistemas A/B;
- objeto e dados trocados;
- frequência;
- autenticação;
- reconciliação;
- monitoramento;
- suporte;
- volume;
- responsabilidade de cada parte;
- implementação versus operação recorrente.

Estado: `scope_definition_required`; somente depois `quote_required`.

## 7. Pools em que cotar agora seria prematuro

### F1-C01 / C02 / C03

Continuam `blocked_by_engineering`.

Não pesquisar vendor/tier como se fosse custo Guivos enquanto Product Engineering estiver pausado antes de W0-01.

### F1-C10 — onboarding/ecossistema

O custo depende de:

- fluxo real de onboarding;
- tempo por entidade;
- automação versus atendimento;
- documentos/treinamento;
- capacidade compartilhada F2-C.

Estado: `scope_definition_required`.

### F1-C11 — mídia paga/performance

Não existe “preço de mercado” que substitua uma decisão de orçamento e experimento de aquisição.

Estado: `budget_decision_and_experiment_required`, não `quote_required`.

### F1-C18 — integrações

Escopo técnico/operacional ainda não está autorizado em nível suficiente para comparação econômica.

Estado: `scope_definition_required`.

## 8. Matriz consolidada dos 18 pools após F1-C

| Pool | Estado após F1-C | Evidência numérica? | Próximo bloqueio material |
|---|---|:---:|---|
| F1-C01 produto/desenvolvimento/QA | blocked_by_engineering | não | Product Engineering |
| F1-C02 infraestrutura/hospedagem | blocked_by_engineering | não | Product Engineering |
| F1-C03 IA/processamento/dados | blocked_by_engineering | não | Product Engineering |
| F1-C04 segurança/privacidade | partially_calibrated + quote_required | sim | escopo/quantidade + controles especializados |
| F1-C05 equipe/serviços profissionais | partially_parameterized_by_F2B_F2C | sim | resource assignment, regime, remuneração/fee |
| F1-C06 jurídico/contábil/fiscal/admin | partially_calibrated + quote_required | sim | jurídico/privacy/compliance |
| F1-C07 marca/conteúdo/criativo | partially_calibrated + quote_required | sim | calendário/produção |
| F1-C08 CRM/vendas/CS | partially_calibrated | sim | usuários/tier/ativação |
| F1-C09 prospecção/deslocamentos BH | partially_calibrated | sim | política e quantidade de deslocamentos |
| F1-C10 onboarding/ecossistema | scope_definition_required | não | fluxo/esforço/driver |
| F1-C11 mídia paga/performance | budget_decision_and_experiment_required | não | decisão de experimento/orçamento |
| F1-C12 eventos/campo BH | partially_calibrated + quote_required | sim | formato/venue/produção |
| F1-C13 pagamentos/cobrança | formula_benchmark_available | sim | volume/mix/arquitetura |
| F1-C14 reembolsos/disputas/perdas | formula_benchmark_available parcial | sim | incidência/perdas |
| F1-C15 suporte/moderação/fraude | partially_calibrated + quote_required | sim | agentes/carga/modelo + moderação/fraude |
| F1-C16 domínios/marca/IP | official/public fees available parcial | sim | quantidade/ações/honorários |
| F1-C17 espaço/equipamentos | unit_benchmark_available | sim | necessidade/configuração |
| F1-C18 integrações/reconciliação | scope_definition_required | não | integração autorizada |

## 9. Cobertura de evidência

Após F1-C:

- **12/18 pools** possuem ao menos uma taxa, fórmula ou benchmark numérico rastreável;
- **6/18 pools** continuam sem calibração numérica útil (`C01`, `C02`, `C03`, `C10`, `C11`, `C18`);
- **0/18 pools** estão completamente fechados para todos os meses `M0–M6`;
- a melhoria de cobertura **não autoriza somar um “custo mínimo da Guivos”**.

Os 12 pools com alguma evidência numérica são:

`C04`, `C05`, `C06`, `C07`, `C08`, `C09`, `C12`, `C13`, `C14`, `C15`, `C16`, `C17`.

## 10. Regras de prevenção de dupla contagem

1. taxa de processamento Sympla em evento não pode coexistir com Stripe sobre o mesmo volume;
2. software de suporte em C15 não pode ser duplicado em C08 se a mesma licença cumprir a mesma finalidade;
3. especialista de segurança em C04 não deve ser duplicado em C05;
4. jurídico/privacy contratado em C06 não deve ser duplicado em C05;
5. ferramenta criativa em C07 não equivale à mão de obra de criação;
6. transporte em C09 não deve ser duplicado em evento C12 quando já estiver incluído no pacote contratado;
7. domínio `.br` em C16 não inclui hospedagem de C02.

## 11. Gate de promoção para `quoted`

Uma linha somente pode mudar de `benchmark`/`quote_required` para `quoted` quando existir:

```yaml
vendor: identified
proposal_date: YYYY-MM-DD
valid_until: YYYY-MM-DD_or_defined
scope: defined
unit_or_deliverable: defined
quantity_or_band: defined
price: defined
currency: defined
taxes: included | excluded | defined
recurrence: defined
activation_period: M0..M6_or_conditional
source_document: identifiable
```

Sem esses campos, “valor informado em conversa” continua sendo evidência insuficiente.

## 12. O que F1-C ainda não calcula

Continuam `NOT CALCULABLE`:

- custo completo de qualquer mês M0–M6;
- burn mensal;
- burn acumulado;
- margem;
- capital de giro;
- runway;
- necessidade de capital;
- rodada necessária;
- break-even;
- valuation derivado de execução.

## 13. Resultado F1-C

| Gate | Resultado |
|---|---|
| novas fontes primárias rastreáveis | PASS |
| novos benchmarks C04/C07/C09/C12/C15 | PASS |
| domínio .br em C16 | PASS |
| pacotes de cotação material | PASS |
| separação benchmark × quote × contract × actual | PASS |
| prevenção de dupla contagem | PASS |
| 12/18 pools com alguma evidência numérica | PASS |
| 18/18 pools numericamente fechados | FAIL — material evidence/decisions missing |
| custo mensal completo | NOT CALCULABLE |
| burn/runway/capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — F1-C expands traceable numeric evidence from 7/18 to 12/18 pools and defines quote-ready scopes for material external costs, while preserving engineering, scope, volume and contracting gates; no complete M0–M6 cost, burn, runway or capital need is yet supportable.`

## 14. Próximo incremento econômico permitido

Após eventual integração de F1-C, o próximo ato recomendado é uma **reconciliação F1/F2 de prontidão para F3**, verificando se as lacunas remanescentes são suficientemente materiais para bloquear caixa/capital de giro ou se F3 deve começar apenas como estrutura sem amount completo.

Essa reconciliação não autoriza F3 automaticamente.