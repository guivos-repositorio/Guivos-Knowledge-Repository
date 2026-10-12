---
id: GEM-OPPORTUNITIES-POINTS-REWARDS-CANDIDATE-001
title: Oportunidades — Retorno em Pontos e Premiações de Eventos — Proposta Transversal
status: draft
version: 2.4.0
owner: Guivos
last_updated: 2026-10-12
normative: false
maturity: conceptual_candidate
related:
  - GEM-000
  - GKR-UX-ORG-OPPORTUNITY-REGISTRATION-MASTER-001
  - GKR-UX-PUBLISHER-APPLICATION-CONTRACT-001
  - GPA-002
---

# Oportunidades — Retorno em Pontos e Premiações de Eventos

> **Candidato, não aprovado como contrato normativo ou produto ativo.** Diretrizes conceituais fornecidas pelo fundador; sem autorização de publicação, implementação, emissão real de pontos ou promoção no MENU.

## 1. Princípios estabelecidos para a proposta

1. Oportunidades são geradas/oferecidas por **Organizações e Coletivos** e podem ser **pagas ou gratuitas**.
2. Os incentivos em pontos são **opcionais** para ambos os tipos de ofertante; não são condição de cadastro, descoberta ou participação.
3. **100% do custo dos pontos é financiado pelo participante ofertante** que configurou a oportunidade; não há cofinanciamento presumido da Guivos.
4. Nas oportunidades pagas, o ofertante pode escolher um **percentual entre opções predefinidas** pela Guivos para converter parte do valor elegível em pontos à Pessoa.
5. Organizações e Coletivos também podem estruturar **premiações em pontos por participação, desempenho, classificação ou critérios expressos**, inclusive em eventos gratuitos, segundo um orçamento próprio.
6. O saldo elegível da Pessoa poderá alimentar uma economia transversal e ser utilizado no Mall e Travel **somente conforme regras futuras de paridade, validade, liquidação e resgate**. Nenhuma integração atual é presumida.
7. Os benefícios não representam, por si sós, evolução garantida, resultado de Journey, validação de mérito pessoal ou compra de reconhecimento institucional.

## 2. Dois mecanismos distintos e combináveis

| Mecanismo | Condição de origem | Configuração pelo ofertante | Gatilho de crédito candidato |
|---|---|---|---|
| PCT — Retorno percentual | Oportunidade paga | Percentual de uma tabela governada + base elegível | Pagamento liquidado e transação confirmada, com janela de estorno |
| FIX — Participação elegível | Evento/atividade paga ou gratuita | X pontos por pessoa elegível | Participação validada sob regra divulgada |
| RANK — Classificação | Evento/competição paga ou gratuita | Pontos por posição/faixa de resultado | Resultado validado, prazo de contestação cumprido |
| CUSTOM — Outras premiações | Oportunidade paga ou gratuita | Regras parametrizadas e aprováveis | Evidência válida do critério contratado |

Combinações são possíveis quando explicitamente autorizadas e custeadas. O incentivo é opcional e **a ausência de pontos não desqualifica a oportunidade**.

## 3. Exemplo — corrida de um Coletivo

`Corrida de sábado, dia X`, com regras divulgadas previamente:

- Participação efetiva: 100 pontos por pessoa.
- Primeiro lugar: bônus de 1.000 pontos.
- Segundo lugar: bônus de 600 pontos.
- Terceiro lugar: bônus de 300 pontos.

Para 50 participantes elegíveis, o compromisso bruto é `50 × 100 + 1.000 + 600 + 300 = 6.900 pontos`, assumindo bônus cumulativos e uma premiação por classificação. Quantidades e política de empate são ilustrativas, **não valores oficiais**.

O sistema deverá impedir que a soma efetiva supere o saldo/orçamento reservado sem autorização e aporte adicionais do ofertante. A premiação poderá ser condicionada a confirmação de presença, resultado e análise de eventuais contestações.

## 4. Cadastro de oportunidade: bloco opcional de pontos

**Campos candidatos compartilhados por Organização e Coletivo:**
- Tipo: gratuita / paga; valor e moeda se paga.
- Incentivo em pontos: `DESATIVADO` por padrão; `ATIVADO` mediante escolha expressa.
- Modalidade: `PCT`, `FIX`, `RANK`, modalidades combinadas permitidas.
- `PCT`: percentual em tabela controlada, valor base elegível e prévia do benefício; não habilitar em oportunidade gratuita com base zero.
- `FIX`: pontos por participação; regras de elegibilidade e validação.
- `RANK`: classes/posições, pontos de cada faixa, política de empate, revisão de resultados.
- Período da ação, limite de pessoas, orçamento total, saldo reservado, custo projetado, condições de cancelamento e estorno.
- Evidências mínimas proporcionais, transparência à Pessoa, impedimentos/antifraude, privacidade e canal de contestação.
- Aceite explícito de **custeio integral pelo ofertante** e das regras econômicas aplicáveis.

**Não presumir superfície:** o Master `ORG-002` existe para cadastro de Organização; a documentação corrente declara que o Coletivo não possui superfície equivalente estável automaticamente. A proposta é uma **capacidade de domínio compartilhável**, cuja alocação na jornada de Coletivos exige adjudicação de autoridade e superfície próprias, sem replicar `ORG-002` por simetria.

## 5. Financiamento, reservas e saldo

Proposta de mecanismo pré-financiado:
1. O ofertante seleciona os incentivos e o sistema estima exposição máxima.
2. O ofertante provisiona/deposita recursos equivalentes aos pontos prometidos, segundo paridade e regras contratuais aprovadas.
3. A Guivos mantém **razão contábil de pontos e ledger financeiro separados**, com rastreio de reservas, emissão, bloqueio, reversão, expiração e resgate.
4. Os pontos são creditados após comprovação do gatilho elegível; promessa e reserva não constituem pontos disponíveis.
5. Estornos, ausência, fraude, erro e disputa geram suspensão/correção proporcional, sem ajuste silencioso ou saldo negativo indevido.
6. Mall e Travel consomem a **mesma unidade de valor governada**, mas cada aceitação/liquidação requer acordo econômico explícito.

**Questões ainda em aberto:** lista oficial de percentuais, paridade monetária, modelo de pré-pagamento e garantia, impostos, taxas, exclusões de base, limites de pontos, expiração, transferibilidade, estornos após resgate, responsabilidades dos parceiros de resgate e política de saldos remanescentes. Percentuais e paridades exemplificados não são regras oficiais.

## 6. Estados e controles candidatos

```text
INCENTIVO DESATIVADO
  → CONFIGURADO (RASCUNHO)
  → SUBMETIDO / VALIDADO
  → ORÇAMENTO RESERVADO
  → OFERTA ATIVA
  → GATILHO ELEGÍVEL COMPROVADO
  → CRÉDITO APROVADO
  → PONTOS DISPONÍVEIS
  → RESGATE / LIQUIDAÇÃO

RAMOS CONTROLADOS: SUSPENSÃO, CONTESTAÇÃO, ESTORNO, CANCELAMENTO,
REVISÃO DE RESULTADO, EXPIRAÇÃO E ENCERRAMENTO.
```

Esses estados **não** constituem novos IDs `GKR-TRN`, eventos implementados ou autorização técnica. A publicação da oportunidade e a validade de seu incentivo possuem controles separados.

## 7. Casos e invariantes mínimos

- Oportunidade gratuita sem incentivo deve funcionar normalmente.
- Oportunidade paga com incentivo percentual deve explicar preço, percentual e pontos estimados.
- Oportunidade gratuita pode premiar presença/classificação com saldo previamente reservado.
- Um mesmo participante não recebe duplicação indevida por inscrição múltipla.
- Inscrição, clique ou acesso a vínculo externo **não comprovam** compra, pagamento, presença nem colocação. Em `BND-001`, não presumir sucesso fora da Guivos.
- O ofertante não deve visualizar dados sensíveis da Journey nem dados pessoais desnecessários.
- Premiação baseada em resultado precisa de evidência, contestação e resolução de empates.
- O sistema não deverá prometer pontos sem controle de financiamento e limites.
- Incentivos não podem prejudicar Coletivos informais nem impor exposição pública indevida.
- Créditos e resgates precisam ser auditáveis e reconciliáveis entre domínios.
- Valor pago, confirmação de pagamento e evidência de participação devem ter fontes de autoridade distintas.

## 8. Integração arquitetural a reconciliar

- **Oportunidades/participantes:** contrato de oportunidade e autoridades de publicação por Organizações/Coletivos.
- **Journey:** elegibilidade, descoberta e vínculo pessoal sem coerção ou garantia de evolução.
- **Economia:** custeio pelo ofertante, orçamento, paridade de pontos, responsabilidades contratuais e liquidação.
- **Mall/Travel:** resgates e aceitação condicionados a contratos próprios.
- **Intelligence/Ads:** não transformar pontuação em rankeamento manipulativo ou publicidade não identificada.
- **GKR:** submeter à governança dos Masters, Surface/Transition Registries e políticas econômicas vigentes, sem promoção automática.

## 9. Próximas adjudicações e bloqueios

| Gate candidato | Pergunta | Estado |
|---|---|---|
| ECO-01 | Unidade única, paridade, reservas e responsabilidade financeira? | PENDENTE |
| ECO-02 | Tabela governada de percentuais e base elegível? | PENDENTE |
| ECO-03 | Orçamento, liquidação, estorno, fraude e resgate Mall/Travel? | PENDENTE |
| UX-01 | Como configurar incentivos em oportunidades de Organização e Coletivo sem superfícies presumidas? | PENDENTE |
| UX-02 | Quais gatilhos comprováveis de participação, classificação, empate e recurso? | PENDENTE |
| LEG-01 | Regime jurídico, fiscal, dados, transparência e proteção de Pessoas? | PENDENTE |
| TEC-01 | Contrato técnico, testes E2E e homologação? | PENDENTE |

**Situação:** proposta de produto/economia recebida e documentada; não é regra operacional ou autorização de implementação. Sem alterações de `main`, `mkdocs.yml`, Masters, registries ou PR #654 (Reconhecimento de Coletivos, frente pausada).

## 10. Limites de benefício por ordem de inscrição — proposta complementar v0.2.0

**Diretriz do fundador:** o ofertante pode limitar a quantidade de pessoas contempladas com determinado incentivo **sem limitar o número de inscrições ou participações na oportunidade**.

### Exemplo — corrida com pontos para inscrições iniciais

Um Coletivo divulga uma corrida com **100 pontos para as primeiras 30 inscrições elegíveis**. Após a 30ª inscrição elegível, outras Pessoas continuam podendo se inscrever normalmente, mas **não recebem esse incentivo específico**. A eventual premiação por colocação (1º, 2º, 3º) possui regras e orçamento próprios e poderá continuar acessível aos participantes posteriores se o regulamento assim definir.

```text
OPORTUNIDADE / EVENTO
  → INSCRIÇÕES ABERTAS
  → INCENTIVO DE INSCRIÇÃO: 100 PONTOS × 30 VAGAS DE BENEFÍCIO
  → ORÇAMENTO MÁXIMO DESTE INCENTIVO: 3.000 PONTOS
  → PRIMEIRAS 30 INSCRIÇÕES ELEGÍVEIS: RESERVA CONDICIONAL
  → INSCRIÇÕES 31+ : INSCRIÇÃO PERMITIDA, SEM ESTE INCENTIVO
  → PRESENÇA / PARTICIPAÇÃO COMPROVADA (SE EXIGIDA)
  → CRÉDITO EFETIVO DAS RESERVAS ELEGÍVEIS
```

**Separar semanticamente** `LIMITE_INSCRIÇÕES_EVENTO` de `LIMITE_BENEFICIÁRIOS_INCENTIVO`; o segundo não encerra o primeiro. O compromisso do incentivo de inscrição é limitado a `30 × 100 = 3.000 pontos`, sem incluir premiações de classificação ou outros incentivos contratados, que exigem orçamento adicional.

### Campos candidatos

- Incentivo ativado, quantidade de pontos, **máximo de beneficiários**, período promocional e critério de ordenação.
- Marco de ordenação verificável: inscrição interna **confirmada e elegível**, com timestamp de autoridade e desempate determinístico. Uma inscrição meramente iniciada não garante direito.
- Reserva condicional por beneficiário, orçamento reservado, quantidade remanescente e estados `DISPONÍVEL` / `ESGOTADO` do **benefício**, nunca do evento por inferência.
- Regra divulgada para desistência, cancelamento, duplicidade, não comparecimento e eventual reaproveitamento de cota. **Não presumir** realocação automática aos próximos inscritos sem política previamente informada.
- Separação entre **elegibilidade à reserva** (posição dentro das 30 primeiras inscrições válidas) e **direito a crédito final** (cumprimento de eventual exigência de presença/participação).
- Exibição clara antes da inscrição: “100 pontos para as 30 primeiras inscrições elegíveis”, com indicação de disponibilidade atual sem garantia quando a confirmação depende de processamento.
- Se a inscrição ocorrer por sistema externo/`BND-001`, a Guivos não infere ordem, confirmação ou elegibilidade sem prova de integração autorizada e confiável.

### Invariantes econômicos e técnicos

1. Um mecanismo transacional/atômico impede reservar a mesma última vaga de benefício para duas Pessoas concorrentes.
2. O teto reservado é calculado sobre beneficiários, **não** sobre todas as inscrições; no exemplo, 3.000 pontos mais orçamentos independentes de classificação.
3. A inscrição após o esgotamento do benefício continua disponível quando o evento aceita novas inscrições.
4. Desistência e não comparecimento não geram crédito indevido; reaproveitamento de cotas segue regra expressa.
5. Incentivos distintos podem ter públicos, tetos e gatilhos próprios; bonificações acumuladas exigem regras visíveis.
6. O ofertante financia 100% das reservas e créditos conforme a política econômica aprovada.
7. A experiência da Pessoa distingue `INSCRIÇÃO CONFIRMADA`, `BENEFÍCIO RESERVADO`, `BENEFÍCIO ESGOTADO` e `PONTOS CREDITADOS`; nenhuma dessas expressões é novo ID oficial do GKR.
8. O limite opcional pode igualmente ser configurado por Organizações e Coletivos, respeitando a autoridade de cadastro de cada tipo de participante.

**Pendências de adjudicação:** regra definitiva do instante de prioridade, elegibilidade em modalidades externas, devolução e redistribuição de cotas, tratamento de empates/concurrency, estornos, limite de campanha e provas de participação. Esta proposta não altera Masters, registros GKR-SURF/TRN, MENU, `main` nem autoriza engenharia.

## 11. Orçamento, reserva e distribuição por incentivo — candidato v0.3.0

**Objetivo:** oferecer ao publicador instrumentos opcionais de incentivo com orçamento definido, financiamento integral pelo próprio ofertante e uma separação auditável entre **inscrição**, **elegibilidade**, **reserva**, **validação** e **crédito**. Regras ainda candidatas, não contrato vigente.

### 11.1 Objetos econômicos separados

| Objeto | Responsabilidade | Invariante |
|---|---|---|
| Oportunidade | Cadastro e condições de participação | Permanece válida e inscrevível independentemente de o incentivo esgotar, se houver vagas de participação |
| Campanha de pontos | Vigência, regulamento, modalidades e custeio | Incentivo é opcional, versão de regra fica preservada |
| Faixa de incentivo | Pontos por beneficiário, limite e critérios de elegibilidade | Tetos por faixa e gatilhos não se confundem |
| Orçamento comprometido | Exposição máxima prevista da campanha | Ofertante custeia 100%; não criar obrigação sem lastro |
| Reserva condicional | Alocação a pessoa elegível, ainda não creditada | Uma reserva por direito, com controle de concorrência |
| Crédito confirmado | Pontos efetivamente disponibilizados | Exige prova do gatilho, registro de ledger e ausência de duplicidade |
| Reversão/expiração | Ajuste de direitos conforme política | Rastreável; nunca apagar histórico contábil |

### 11.2 Fórmulas e tetos de exemplo

**Primeiras N inscrições:** `ORÇAMENTO_FAIXA = PONTOS_POR_PESSOA × LIMITE_BENEFICIÁRIOS`. Para 100 pontos × 30 primeiras inscrições elegíveis: **3.000 pontos de limite de compromisso**, sem limitar o número de inscrições do evento.

**Premiação por colocação:** `ORÇAMENTO_RANK = SOMA(PONTOS_DE_CADA_POSIÇÃO × QTDE_DE_BENEFICIÁRIOS_DA_POSIÇÃO)`, com tratamento explícito para empates e eventual prêmio compartilhado.

**Incentivo percentual em oportunidade paga:** `BASE_ELEGÍVEL × TAXA_ESCOLHIDA` produz **valor econômico de benefício**, não quantidade de pontos, até a política oficial definir paridade, arredondamento e custos de liquidação. Para volume incerto, exigir teto de transações/beneficiários ou reserva máxima monetária convertida e coberta financeiramente.

**Exemplo combinado:** 3.000 pontos de primeiras inscrições + (1.000 + 600 + 300) pontos de classificação = **4.900 pontos de exposição nominal**. O prêmio por classificação é independente; a distribuição real depende dos gatilhos comprovados. Empates ou outras bonificações não podem elevar o teto sem regra e financiamento adicionais.

### 11.3 Fluxo candidato de orçamento e emissão

```text
ORGANIZAÇÃO OU COLETIVO
  → CONFIGURA OPORTUNIDADE E INCENTIVOS OPCIONAIS
  → DEFINE TETOS, REGRAS, GATILHOS E JANELA
  → SISTEMA CALCULA EXPOSIÇÃO MÁXIMA
  → OFERTANTE FINANCIA / GARANTE 100% DO COMPROMISSO
  → LASTRO RECONCILIADO E CAMPANHA APTA A ATIVAÇÃO
  → INSCRIÇÃO ELEGÍVEL OCUPA UMA DAS N COTAS (ATOMICAMENTE)
  → RESERVA CONDICIONAL DE PONTOS, NÃO SALDO DISPONÍVEL
  → PRESENÇA / RESULTADO / PAGAMENTO COMPROVADO, CONFORME FAIXA
  → CRÉDITO FINAL EM LEDGER ÚNICO DE PONTOS
  → UTILIZAÇÃO NO MALL / TRAVEL SUJEITA ÀS REGRAS DE RESGATE
```

A Guivos não participa do **custeio econômico** dos pontos prometidos, conforme diretriz estabelecida. Custódia, liquidação e eventuais serviços administrativos ainda exigem modelo contratual e operacional próprios; o termo “100% financiado” não dispensa definir esses papéis.

### 11.4 Esgotamento de benefício ≠ encerramento de inscrição

- A capacidade de inscrição na oportunidade e o limite de beneficiários do incentivo são contadores distintos.
- Para as primeiras 30 inscrições elegíveis, a reserva só nasce após confirmação válida sob ordenação verificável. Para a 31ª em diante, o sistema não reserva esses 100 pontos, mas permite inscrição se o evento estiver aberto.
- A Pessoa deve conhecer antes de confirmar se o benefício é elegível, indisponível ou depende de confirmação.
- Bloquear promessas sem disponibilidade de orçamento e evitar duas reservas para a última cota.
- Cancelamento ou falta de presença pode invalidar o crédito; **redistribuição da cota não é automática** sem regra pública prévia. Se permitida, deverá respeitar uma fila elegível, janela de corte e cronologia auditável.

### 11.5 Ledger mínimo e reconciliação

Registrar por transação `incentive_id`, `opportunity_id`, `issuer_id`, `person_ref` protegido, `rule_version`, `eligible_event_id`, `idempotency_key`, quantidade, estado, timestamps, origem da comprovação, referência de lastro e eventual operação reversa.

Manter sem ambiguidade:
- **Orçamento máximo** da campanha;
- **Orçamento financiado/garantido**, sujeito ao regime econômico futuro;
- **Cotas/reservas condicionais** ainda não creditadas;
- **Créditos efetivos** emitidos em conta de Pessoa;
- **Obrigações de resgate/liquidação**, sem pressupor que reserva represente receita;
- **Saldo não utilizado**, cuja liberação/restituição depende de prazos, conciliações e disputas.

A validade e autorização de uma oportunidade não bastam para autorizar sua campanha de pontos; a campanha requer regras e orçamento próprios.

### 11.6 Cenários obrigatórios de validação futura

| Cenário | Resultado esperado em proposta |
|---|---|
| 30ª e 31ª inscrições simultâneas | Uma única atribuição da última cota; inscrição da outra Pessoa pode continuar |
| Evento com 100 participantes e apenas 30 bonificados | 30 cotas de incentivo no máximo; até 100 inscritos conforme limite da atividade |
| Cancelamento da 5ª inscrição | Não premiar sem gatilho; reabrir cota apenas quando regra expressa permitir |
| Ausência do 1º colocado | Tratar resultado/recurso conforme regulamento, não creditá-lo automaticamente |
| Orçamento insuficiente | Não ativar novo compromisso, ou suspender novas reservas sem afetar indevidamente direitos já adquiridos |
| Pagamento externo em `BND-001` | Não presumir transação liquidada ou elegibilidade sem prova confiável |
| Pontos parcialmente resgatados, depois estornados | Processo governado de dívida/ajuste e contestação; evitar saldo negativo silencioso |
| Incentivo percentual + inscrição + podium | Orçamentos, eventos elegíveis e controles separados; cumulação divulgada |
| Encerramento do evento com orçamento sobrante | Conciliar obrigações, disputas e saldo residual antes de liberação contratual |

### 11.7 Gates de decisão

1. **FIN-01:** modalidade de pré-financiamento/garantia, liquidez, custódia e liquidação; **não decidida**.
2. **FIN-02:** paridade oficial monetária ↔ pontos, percentual e arredondamento; **não decidida**.
3. **FIN-03:** cancelamento, expiração, reabertura de cota e saldo residual; **não decidida**.
4. **FUN-01:** identidade de inscrição elegível e confiabilidade de ordem, inclusive integração externa; **não decidida**.
5. **FUN-02:** regras de combinação, empates, contestação e ratificação de resultado; **não decidida**.
6. **GOV-01:** autorização de orçamento e função legítima de publicador Coletivo sem presumir `ORG-002`; **não decidida**.
7. **TEC-01:** transações atômicas, reconciliação, ledger, privacidade e homologação E2E; **não autorizadas**.

### Checkpoint

```text
CANDIDATE MODEL → BUDGET / RESERVATION / DISTRIBUTION DOCUMENTED
ISSUER FINANCING → 100% OF OFFERED POINTS
BENEFIT QUOTA LIMIT → INDEPENDENT OF OPPORTUNITY ENROLLMENT
PERCENTAGE / PARTICIPATION / PLACEMENT → DISTINCT, COMBINABLE BY EXPLICIT RULES
OFFICIAL POINTS PARITY / PERCENTAGE CATALOG → UNDEFINED
ECONOMIC, UX, LEGAL AND TECHNICAL GATES → PENDING
PR #655 → OPEN / DRAFT
MAIN / MENU / MASTERS / REGISTRIES / PRODUCT → UNCHANGED
```

## 12. Economia dos pontos: paridade, pré-financiamento e liquidação transversal (v0.4.0 candidato)

**Princípio fornecido:** 100% do custo econômico de pontos ofertados decorre da Organização ou Coletivo que os promete; Guivos não é cofinanciadora presumida. A fonte, depósito, titularidade dos recursos, custódia e tratamento contábil exigem decisão posterior.

### Modelo recomendado para avaliação, não regra vigente

1. Definir uma **unidade única de pontos** com fator de emissão e valor econômico de resgate, versionados e passíveis de revisão prospectiva sem retirar direito adquirido indevidamente.
2. Separar claramente três números: **valor pago pela Pessoa**, **valor econômico financiado pelo ofertante** e **quantidade de pontos emitidos**. Para a modalidade percentual, uma escolha de 5% sobre R$ 200 gera base de custeio de R$ 10; a quantidade emitida depende de paridade a definir. Para premiação fixa de 100 pontos, custo de cobertura depende do valor unitário de responsabilidade por ponto.
3. Adotar como **hipótese candidata** pré-financiamento segregado ou garantia economicamente suficiente antes de assumir obrigações de pontos. Não converter a hipótese em regra bancária, de pagamento ou financeira aprovada.
4. Orçamentos de incentivos separados (percentual, primeiras N inscrições, participação validada, classificação), com somatório da exposição e reservas condicionais atômicas.
5. O saldo da Pessoa somente fica disponível após evento elegível verificado e ledger de crédito idempotente; reserva condicional não é crédito.
6. Mall e Travel funcionam como **destinos de resgate condicionados a contratos futuros**, com compensação/liquidação entre participantes e produtos. Pontos não equivalem a dinheiro sacável, transferível ou reembolsável sem norma expressa.
7. Definir quem suporta taxas operacionais, impostos, devoluções, expiração, variações de preço de resgate, fraudes e quebra de lastro, sem transferir o custeio dos pontos à Guivos por omissão.

### Exemplo com duas reservas

- Campanha de uma corrida: 100 pontos × 30 primeiras inscrições elegíveis = teto de 3.000 pontos.
- Premiações adicionais: 1.000 + 600 + 300 = 1.900 pontos, antes da política de empates.
- **Teto nominal combinado: 4.900 pontos**, com controles independentes.
- Se a taxa de garantia futura for R$ `v` por ponto, o valor de lastro seria `4.900 × v`; o documento não define `v` nem paridade de resgate.

### Riscos que exigem adjudicação

| Gate | Ponto decisório | Situação |
|---|---|---|
| ECO-PAR | Emissão percentual, valor econômico, paridade, arredondamento e revisões | PENDENTE |
| ECO-FUND | Pré-financiamento, caução/garantia, custódia e titularidade dos recursos | PENDENTE |
| ECO-LIQ | Contratos de resgate Mall/Travel, liquidação e responsabilidade por diferença de valores | PENDENTE |
| ECO-CAN | Estornos, ausência, cancelamento e créditos já resgatados | PENDENTE |
| ECO-RES | Saldo remanescente, expiração, restituição e eventos de insolvência | PENDENTE |
| ECO-LEG | Avaliação jurídica, fiscal, consumerista, privacidade e eventual regulação de meios de pagamento | PENDENTE |

**Separações obrigatórias:** incentivo não é desconto presumido; pontos não são declaração de impacto; campanha de pontos não é pagamento por relevância no Journey; participação e resultado permanecem condicionados a prova proporcional; oportunidades sem pontos continuam legítimas.

## 13. Auditoria de pertinência editorial — Home de Organizações e Coletivos (v0.4.0 candidato)

**Fonte examinada na main:** `GKR-UX-HOME-OC-MASTER-001`, versão 1.0.7, `active`, `normative: false`, documento vigente de consumo para design; `GKR-UX-HOME-OC-READ-FIRST-001`, v1.0.5. Nenhum arquivo da Home foi alterado.

### Correspondência com os movimentos existentes

| Tema recente | Movimento da Home | Juízo documental | Limite de publicação |
|---|---|---|---|
| Selos `Verificado` e `Contribuição Reconhecida` | M09 — Confiança por autoridade, evidência e proteção | **Aderência semântica forte**; preservar existência/representação ≠ contribuição e impacto | Política em estudo na PR #654; não mostrar badges como concedidos ou disponíveis |
| Oportunidade paga com percentual opcional em pontos | M08 — Circulação de valor; M10 — Produtos | **Aderência econômica forte**; custo integral do ofertante, escolha optativa, conexão potencial Mall/Travel | PR #655 candidata; não anunciar cashbacks ou resgates ativos |
| Incentivos por participação/resultado em eventos (Organizações e Coletivos) | M02 — Capacidades reais; M08 — Circulação de valor | **Aderência funcional**: organizadores podem conceber formatos com limites, regras e prêmios | Não simular evento real, concessão atual ou resultados não comprovados |
| Limite de 100 pontos para primeiras 30 inscrições sem bloquear restantes | M08, como explicação aprofundada futura | **Detalhe de mecanismo**, não assunto de hero ou narrativa principal | Melhor em exemplo editorial secundário e nas superfícies de cadastro após adjudicação |
| Integração de pontos a Mall/Travel | M10 — Papéis de produtos | **Aderência transversal**; conservar especialização e não transformar Journey em loja | Não presumir conversão, resgate ou liquidação operacional |

### Proposta editorial de conteúdo, explicitamente futuro/candidato

**M02 — Capacidades e contribuições:** "Organizações e Coletivos podem criar oportunidades, experiências e eventos. Formatos futuros de incentivo poderão permitir que quem organiza reconheça participação ou desempenho por regras e limites definidos, sem converter participação em obrigação ou medida universal de evolução."

**M08 — Circulação de valor:** "O ecossistema estuda mecanismos pelos quais Organizações e Coletivos poderão, opcionalmente e com custeio próprio, oferecer pontos vinculados a oportunidades pagas ou premiar participações e resultados em atividades e eventos. Os limites, os critérios e o orçamento serão definidos pelo ofertante sob regras comuns da Guivos."

**M09 — Evidência e confiança:** "Também estão em estudo formas diferentes de reconhecer a existência e representação legítima de um Coletivo e de analisar contribuições contextuais apoiadas em evidências. Verificação não significa garantia de segurança ou impacto, e reconhecimento de contribuição não equivale a resultado universal."

**M10 — Ecossistema integrado:** "Pontos gerados por mecanismos elegíveis poderão, conforme regras econômicas futuras, conectar oportunidades, experiências e opções de utilização no Guivos Mall e Guivos Travel, preservando as responsabilidades de cada produto."

**Atenção:** as frases usam futuro e estágio de estudo. Não são recomendação de exibição pública imediata enquanto a governança das capacidades estiver pendente. O conceito pode orientar o design do futuro sem ser representado como funcionalidade corrente.

### Restrições de hierarquia e provas

- **Não incluir seção autônoma ou cards promocionais de três funcionalidades no hero.** Preservar a narrativa de 11 movimentos, possibilidades reais, participantes e evidências.
- **Não misturar selos com pontos.** Os selos dizem respeito a legitimidade e contribuição; os pontos são compromissos econômicos facultativos do ofertante.
- **Não diferenciar indevidamente Organização e Coletivo**: ambos podem oferecer incentivos conforme regras, ainda que a arquitetura corrente do cadastro em `ORG-002` não se aplique por simetria ao Coletivo.
- **Não prometer recursos ativos**: nem badge de verificação, nem crédito de pontos, nem liquidação Mall/Travel, nem cotas de evento implantadas.
- **Não alterar a autoridade editorial da Home por esta PR**; futura proposta de revisão deve reconciliar `GKR-UX-HOME-OC-MASTER-001`, Read First, roteiro de design e provas.
- **Não reabrir G0/B-01 da PR #654** sem evidência institucional material.

### Próxima análise recomendada

Preparar uma matriz de impacto redacional de M02/M08/M09/M10 sobre a Home, com textos alternativas, atributos de prova e propostas de versão, **sem alteração direta do Master vigente** antes de decisão editorial distinta. Em paralelo, amadurecer ECO-PAR/ECO-FUND/ECO-LIQ com propostas comparadas e explícita distinção entre hipótese e ato econômico aprovado.

```text
PR #655 → OPEN / DRAFT
ECONOMIC PARITY / FINANCING / SETTLEMENT → ANALYTIC CANDIDATES, NOT APPROVED
HOME O/C CONTENT AUDIT → DOCUMENTED IN CANDIDATE
HOME O/C MAIN MASTER / READ FIRST → UNCHANGED
SELLOS PR #654 / G0 / 0-36 → UNCHANGED
MENU / GKR REGISTRIES / REPLIT / LIVE POINTS → UNCHANGED
```

## 14. Diretriz de hierarquia narrativa — Home Organizações e Coletivos (v0.5.0 candidato)

**Ressalva expressa do fundador em 12/10/2026:** a Home de Organizações e Coletivos deve expressar **a mesma visão da Home Pessoa sob outro ângulo**, e não girar em torno dos pontos, selos ou de um catálogo de mecanismos. Esta diretriz **corrige a ênfase** da avaliação da seção 13; aderência temática não implica destaque, destaque no hero ou presença obrigatória nos movimentos.

### Princípio editorial central

A Home Pessoa parte de quem vive sua Journey, reconhece necessidades, desejos, possibilidades, oportunidades e próximos passos. A Home de Organizações e Coletivos parte de quem tem propósito, pessoas, recursos, iniciativas, conhecimento, experiências, serviços e oportunidades que podem contribuir com essa mesma realidade. **É o mesmo ecossistema, uma perspectiva complementar**. Não são duas teses, um catálogo B2B ou uma vitrine de recompensas.

**Hierarquia inegociável de comunicação:**
1. Propósito da Guivos, possibilidades, contexto e vida real;
2. Papel e capacidade legítima de Organizações e Coletivos de criar/habilitar oportunidades e relações;
3. Conexão entre participantes, território, experiências e continuidade;
4. Confiança, transparência e contribuição com evidências;
5. Mecanismos instrumentais opcionais (pontos, premiações e selos), apenas se úteis à compreensão — jamais protagonista.

### Critérios de inclusão dos mecanismos

| Tema | Prioridade narrativa | Regra |
|---|---|---|
| Criar e habilitar oportunidades reais | Central como expressão de contribuição | Não reduzir oferta ao aspecto monetário |
| Capacidades, experiências, contextos e relações | Central | Preservar autonomia dos participantes e relevância local/global |
| Pontos percentuais e prêmios em eventos | **Terciária / detalhe funcional** | Não destacar no hero, não criar movimento nem card promocional obrigatório |
| Selos Verificado e Contribuição Reconhecida | **Terciária / detalhe de governança** | Podem compor futuro detalhamento de confiança, mas não substituir confiança por símbolo |
| Mall/Travel como destinos possíveis | Complementar | Não transformar Home em argumento comercial de recompensas |

**Direção textual:** se uma atualização da Home for necessária, preferir uma frase discreta dentro de M08 sobre circulação de valor, sem exemplos de percentuais, quantidade de pontos, rankings ou orçamento; selos, quando cabíveis e aprovados, devem ficar em fontes de profundidade ou menção discreta de confiança em M09. M02 e M10 **não exigem alteração** apenas porque os mecanismos estão em estudo. O contexto existente sobre oportunidades, participação e papéis dos produtos já é suficiente para a narrativa principal.

**Regra de não regressão:** um visitante deve conseguir compreender a visão Guivos e seu papel como Organização ou Coletivo **sem precisar conhecer o sistema de pontos ou os dois selos**. Retirar essas menções não pode enfraquecer a mensagem central da Home.

**Estado:** diretriz editorial candidata registrada, sem mudança no Master da Home, sem autorização de publicação dos pontos ou selos e sem alteração no MENU ou na PR #654.

## 15. Confirmação de direção sobre os dois selos — orientação de Home (v0.6.0)

**Decisão comunicada pelo fundador em 12/10/2026:** a política conceitual dos selos **Verificado** e **Contribuição Reconhecida** é considerada **aprovada na direção de produto**. As pendências de registros e formalização no GKR não impedem que a equipe de design contemple esses elementos na futura Home. Esta decisão atualiza a interpretação editorial anterior de que os selos só poderiam ser considerados no design após conclusão de todos os registros.

**Não confundir estágios:** aprovação declarada de direção de produto ≠ regularização documental já concluída ≠ competência institucional comprovada para todos os atos ≠ implementação, emissão ou concessão real de selos. O histórico de exames e adjudicações na PR #654 deve ser atualizado pelo rito próprio, sem reclassificação automática de 0/36 para 36/36.

**Aplicação à Home O/C:** os selos podem fazer parte do escopo de concepção de design, **discretamente** e em conexão com M09 (confiança, representação, evidências, contribuições), sem entrar no hero, protagonizar a narrativa ou substituir o significado de confiança por ícones. Sua eventual exposição como funcionalidades disponíveis em site público ainda exige implantação e veracidade operacional.

**Invariante:** mesma visão da Home Pessoa sob o ângulo de Organizações/Coletivos; nenhum mecanismo instrumental — selos ou pontos — se torna protagonista.

## 16. Reconciliação conceitual entre as Homes — mesmo ecossistema, duas perspectivas (v0.7.0 candidato)

**Fontes comparadas na `main` em 12/10/2026:** `GKR-UX-HOME-MASTER-001 v1.0.7` (Pessoa) e `GKR-UX-HOME-OC-MASTER-001 v1.0.7` (Organizações e Coletivos). Ambos estão `active`, `normative:false`, como referências correntes de consumo de design; o Master O/C declara o Master Pessoa como `parent`. Esta análise não modifica nenhum Master.

### Regra-mãe de simetria

**Uma Guivos, uma visão, perspectivas complementares.** A Home Pessoa apresenta o ecossistema desde a autonomia de quem vive a própria Journey. A Home O/C expõe possibilidades desde as capacidades, iniciativas, recursos e contribuições dos agentes que podem habilitar experiências reais. A segunda página não é um funil de aquisição B2B, ferramenta de preços ou vitrine de funcionalidades.

### Matriz de equivalência semântica

| Eixo | Perspectiva Pessoa | Perspectiva Organização/Coletivo | Resultado |
|---|---|---|---|
| Fundação | Momento, possibilidade, próximo passo e experiências vividas | Capacidade legítima, contribuição, contexto e acesso | CONVERGENTE, sem promessa de impacto |
| Participantes | Pessoa com decisão sobre sua Journey | Organização/Coletivo preserva identidade e governança | CONVERGENTE, papéis distintos |
| Possibilidade/oportunidade | Descobre, compreende, decide participar | Cria, habilita ou disponibiliza oportunidades reais | CONVERGENTE, complementar |
| Vida real/território | Pessoas, lugares e experiências além da tela | Ações, iniciativas, infraestrutura e vínculos territoriais | CONVERGENTE, não simular escala |
| Autonomia | Sem prescrição e coerção | Sem captura da Journey, compra de relevância ou pressão comercial | CONVERGENTE |
| Confiança e prova | Escolha consciente com evidências | Responsabilidade, representação, proteção e comprovação de alegações | CONVERGENTE |
| Jornada/produtos | Journey central, especializados como capacidades | Mesma Guivos e papéis preservados, sem reduzir organizações a Business | CONVERGENTE |
| Valor/circulação | Viver experiências e conexões | Contribuir e habilitar contexto de valor | CONVERGENTE; pontos instrumentais |

### Impacto dos mecanismos adicionais

- **Selos** `Verificado` e `Contribuição Reconhecida`: há aprovação expressa da **direção de produto** pelo fundador para integrarem o **escopo do design** da Home O/C. Permanecem elementos contextuais possíveis de M09; não substituem confiança, evidência, transparência ou contribuição. Formalização documental específica da PR #654 segue distinta.
- **Pontos** em oportunidades pagas e eventos: apoio econômico facultativo, custeado integralmente pelo ofertante; podem ser compreendidos em aprofundamento sobre M08, **sem obrigação de menção na Home pública**. Percentuais, cotas, paridade, ranking de colocação e orçamentos pertencem às superfícies funcionais e às políticas econômicas, não à tese pública central.
- **Mall e Travel**: possíveis relações futuras de utilização de pontos não alteram o conceito de Journey nem tornam a Home O/C um catálogo de produtos ou programa de fidelidade.

### Diagnóstico de lacunas reais

**Lacuna narrativa estrutural demonstrada:** NENHUMA nas fontes comparadas. A Home O/C já contém movimentos de capacidades, fragmentação, contribuição, complementaridade, circulação de valor, confiança e produtos em papéis próprios.

**Possível aperfeiçoamento condicionado:** quando a equipe materializar o design e houver prova/estado adequado, adicionar menção **curta e contextual** aos selos no M09, sem seção nova e sem alegar selos concedidos. Menção econômica sobre pontos no M08 é **opcional**, não requisito de aceitação. Não se exige ajuste em M02/M10 por existirem propostas de mecanismos.

**Rejeitar:** hero com cashback, cards centrais de premiações, benefícios como eixo de convencimento, selos como substitutos da confiança, exemplares inventados de Coletivos reconhecidos, comparação de planos ou narrativa comercial incompatível com a Home Pessoa.

### Critérios de aceitação futuros

1. Um visitante entende propósito, possibilidades, contribuição e relações mesmo sem conhecer selos/pontos.
2. Os 11 movimentos preservam função, hierarquia e liberdade criativa do designer.
3. Ambas as Homes continuam expressando a mesma fundação sem copiar textualmente conteúdo nem apagar diferenças de perspectiva.
4. Toda alegação pública corresponde à maturidade real de produto; design conceitual não equivale a funcionalidade operacional.
5. Selos, quando representados, são contextuais e não viram credencial fictícia em atores reais.
6. Pontos não controlam percepção de relevância, ordenação de oportunidades nem mérito dos Coletivos.

**Encaminhamento:** manter Masters vigentes intactos neste ciclo; usar esta matriz como insumo candidato de design e auditoria, com eventual PR específica de revisão apenas se surgir mudança textual justificada por lacuna verificável.

```text
HOME PERSON v1.0.7 / HOME O-C v1.0.7 → CONCEPTUALLY RECONCILED
ONE ECOSYSTEM / TWO PERSPECTIVES → PRESERVED
STRUCTURAL HOME NARRATIVE GAP → NONE CONFIRMED
BADGES → PRODUCT DIRECTION APPROVED / DESIGN CONTEXTUAL
POINTS → OPTIONAL SUPPORTING DETAIL, NOT HOME EMPHASIS
HOME MASTERS / MENU / REGISTRIES / MAIN → UNCHANGED
PR #655 → OPEN / DRAFT
```

## 17. Alternativas econômicas para paridade, custeio e liquidação Mall/Travel (v0.8.0 candidato)

**Resultado:** comparação analítica de arquitetura econômica; nenhuma taxa, preço do ponto, entidade custodiante ou meio de pagamento está aprovado. O custeio dos incentivos é **100% do ofertante** (Organização ou Coletivo), independentemente da modalidade.

### 17.1 Definições separadas

- `B`: valor econômico do benefício prometido, em reais, derivado de percentual sobre pagamento efetivamente elegível ou de pontuação fixa com custo unitário.
- `q_emissao`: pontos emitidos por R$ 1 de benefício econômico; variável **pendente de decisão**.
- `q_resgate`: valor de abatimento/resgate correspondente a cada ponto; variável **pendente de decisão**, contratual e distinta da taxa de emissão.
- `P`: pontos prometidos/emitidos; `F`: financiamento efetivo recebido/garantido do ofertante; `L`: obrigação estimada de liquidação/resgate, com reservas e ajustes sujeitos à política.
- Reserva de orçamento, reserva individual, crédito disponível e resgate são eventos contabilmente distintos; obrigação de incentivo **não é receita automática** da Guivos.

### 17.2 Comparação de modelos de paridade

| Alternativa | Forma | Benefício | Limitação / controle necessário |
|---|---|---|---|
| PAR-A — Paridade fixa uniforme | Uma taxa governada e versionada para emissão/resgate | Compreensibilidade e previsibilidade | Exposição a subsídio oculto, inflação e custo dos parceiros |
| PAR-B — Duas taxas governadas | Emissão e resgate definidos separadamente, com transparência e limites | Permite cobrir custos e preservar sustentabilidade | Exige explicação clara, proteção dos direitos já adquiridos e governança contra depreciação |
| PAR-C — Conversão por catálogo de recompensas | Pontos necessários por item/viagem variam segundo resgate | Adapta-se a ofertas heterogêneas | Precificação menos intuitiva e volatilidade; custos precisam estar integralmente cobertos |

**Direção analítica:** comparar **PAR-A** como baseline de simplicidade e **PAR-B** como cenário de flexibilidade; PAR-C pode coexistir no catálogo, mas não deve obscurecer o valor que a Pessoa efetivamente recebe. Nenhum modelo é escolhido normativamente.

### 17.3 Comparação de garantia do custo dos pontos

| Alternativa | Mecanismo | Regra para ofertante | Risco |
|---|---|---|---|
| FUND-A — Pré-financiamento integral por campanha | Recursos proporcionais ao máximo comprometido recebidos antes de ativar | Reserva efetivamente lastreada | Exige custódia, conciliação e tratamento de saldos |
| FUND-B — Saldo pré-pago reutilizável do ofertante | Carteira de orçamento empresarial/coletivo, com blocos reservados por campanha | Compromisso nunca supera saldo livre | Precisa isolar saldos e evitar duplo compromisso |
| FUND-C — Garantia externa/limite contratado | Caução/garantia aprovada equivalente à exposição máxima | Garantia executável suficiente | Crédito, inadimplência, enforcement e maior complexidade jurídica |

**Direção analítica recomendada para MVP futuro:** examinar **FUND-A** ou **FUND-B** porque ambos permitem travas por orçamento e pré-reserva mais simples do que crédito ao ofertante. Trata-se de recomendação para teste de viabilidade, **não escolha normativa ou autorização financeira**. Em todos os casos, o custo econômico do incentivo pertence ao ofertante; a Guivos não é fonte residual de cobertura por padrão.

### 17.4 Liquidação em Mall e Travel

**Modelo de responsabilidade candidato:**
1. Oportunidade gera direito condicional; apenas crédito comprovado aumenta o saldo de pontos da Pessoa.
2. Um serviço de ledger central mantém emissão, bloqueio, resgate, reversão e idempotência, com competência econômica e segurança adjudicadas.
3. No Mall, um pedido elegível pode aceitar pontos até limite definido, registrando cotação, valor coberto, parceiro vendedor, taxas e evidência de entrega/liquidação.
4. No Travel, reserva ou serviço elegível pode aceitar pontos sob disponibilidade e política de cancelamento própria, com liquidação diferenciada por fornecedor e janela de reserva.
5. O custo do resgate é atendido pelo lastro economicamente atribuído às campanhas, com conciliação entre emissor, plataforma e recebedor. Não presumir que Mall ou Travel financiam os pontos.
6. A disponibilidade ou o preço de uma viagem não pode ser inferido do saldo de pontos. A jornada de resgate exige confirmação real do produto/serviço.

### 17.5 Cenários ilustrativos sem paridade oficial

**Oportunidade paga:** R$ 200 pagos × 5% configurados = R$ 10 de benefício financiado pelo ofertante. Os pontos `P = R$ 10 × q_emissao` serão calculáveis apenas após fixação de `q_emissao`.

**Corrida de Coletivo:** 30 inscrições × 100 pontos = 3.000 pontos de teto do incentivo; premiação separada de 1.900 pontos → 4.900 pontos totais de exposição nominal. Custeio em reais dependerá de `q_resgate`, tarifas e demais obrigações.

**Exemplo de teste matemático (não oficial):** se 1 ponto pudesse gerar R$ 0,01 de resgate e não houvesse custo adicional, a exposição nominal de 4.900 pontos equivaleria a R$ 49,00; não se adota essa equivalência.

### 17.6 Invariantes para adjudicação

1. Garantia/recursos suficientes **antes** de prometer pontos; orçamento bloqueado por campanha.
2. Quem criou a campanha paga integralmente sua obrigação, inclusive ajustes previstos contratualmente, sem cofinanciamento implícito.
3. A Pessoa vê regra, quantidade esperada, condições, validade e valor de uso aplicável sem comunicação enganosa.
4. A alocação às primeiras `N` inscrições não restringe outras inscrições da oportunidade.
5. Direitos adquiridos têm tratamento explícito para alteração de paridade, cancelamento ou encerramento de parceiro.
6. Nenhum resgate é liquidado duas vezes; reserva de checkout expira e libera saldo conforme política.
7. Privacidade e reconciliação de ledger, conciliação financeira e razão de auditoria são separados por função e acesso.
8. Os termos "pontos", "saldo" e "resgate" não presumem classificações regulatórias sem exame jurídico adequado.

### 17.7 Gates de decisão e sequência

| Gate | Decisão requerida | Estado |
|---|---|---|
| PAR-01 | Taxa de emissão e unidade única de valor | PENDENTE |
| PAR-02 | Taxa/precificação de resgate e direitos acumulados | PENDENTE |
| FUND-01 | FUND-A/B/C, regras de depósito/garantia, auditoria e saldos | PENDENTE |
| LIQ-01 | Liquidação Mall, elegibilidade de pedidos e parceiros | PENDENTE |
| LIQ-02 | Liquidação Travel, reservas, cancelamentos e fornecedores | PENDENTE |
| RISK-01 | Impostos, consumo, privacidade, meios de pagamento e insolvência | PENDENTE |
| GKR-01 | Conciliação com economia, UX, contratos e IDs oficiais | PENDENTE |

**Próximo trabalho:** matriz de decisão para comparar PAR-A/B e FUND-A/B com casos de estorno, saldos remanescentes e variações de resgate; somente após critérios claros, preparar deliberação institucional e implementação.

```text
GKR PR #655 → OPEN / DRAFT
POINTS PARITY → ALTERNATIVES COMPARED / NOT CHOSEN
ISSUER FINANCING → 100% / PRE-FUNDING OPTIONS COMPARED
MALL / TRAVEL SETTLEMENT → CONCEPTUAL CONDITIONS DOCUMENTED
PERSON / O-C HOME MASTERS → UNCHANGED
GKR MAIN / MENU / REGISTRIES → UNCHANGED
ENGINEERING / LIVE POINTS → NOT AUTHORIZED
```

## 18. Matriz decisória econômica: paridade, custeio e cenários adversos (v0.9.0 candidato)

**Estado:** comparação documental concluída; opções não adjudicadas. O ofertante (Organização ou Coletivo) financia **100% da obrigação econômica** de pontos que oferecer, inclusive em modalidades percentuais, participação ou colocação. A taxa de paridade e o modelo operacional não foram aprovados.

### 18.1 Critérios de comparação

Pontuação qualitativa analítica: `BAIXA / MÉDIA / ALTA` para clareza à Pessoa, previsibilidade de passivo, simplicidade operacional, flexibilidade no Mall/Travel, risco de mudança de valor percebido e carga de reconciliação. **Não constituem ranking normativo**, validação contábil ou autorização jurídica.

| Modelo | Clareza à Pessoa | Previsibilidade econômica | Complexidade | Risco central |
|---|---|---|---|---|
| PAR-A: paridade uniforme de emissão/resgate | ALTA | ALTA quando reserva cobre obrigação | MENOR | Custo de liquidação e manutenção da equivalência |
| PAR-B: emissão/resgate com regras distintas | MÉDIA, depende de transparência | MÉDIA/ALTA sob teto e versão | MAIOR | Confusão sobre valor real dos pontos, mudanças retroativas |
| PAR-C: recompensas precificadas em pontos por catálogo | MÉDIA/BAIXA sem referência financeira clara | DEPENDE DE ESTOQUE/COTAÇÃO | MAIOR | Resgate desigual por produto/fornecedor |

**PAR-A e PAR-B** seguem alternativas principais de comparação, sem escolha. Se PAR-B for adotada, valor de utilização, validade, revisões e comunicação devem ser explícitos e coerentes com direitos já concedidos.

### 18.2 Matriz de financiamento

| Modelo | Reserva | Benefício | Risco e proteção |
|---|---|---|---|
| FUND-A: pré-financiamento por campanha | Orçamento vinculado à campanha antes de compromisso | Simplicidade do teto e encerramento | Saldos dispersos; exigir conciliação por campanha e regras de devolução |
| FUND-B: saldo pré-pago reutilizável | Saldo central do ofertante, segregado em reservas por campanha | Flexibilidade para múltiplas oportunidades | Concorrência entre campanhas; exigir bloqueio atômico do saldo comprometido |
| FUND-C: garantia externa | Capacidade de cobertura por garantia validada | Menor desembolso antecipado | Inadimplemento, execução e risco de liquidez; não preferencial na análise de MVP |

**Hipótese de implementação para testes posteriores:** admitir FUND-A e FUND-B como modelos alternativos de origem dos recursos e exigir, em ambos, a mesma regra de **orçamento disponível ≥ compromissos novos**. Não instituir carteira financeira sem análise regulatória específica.

### 18.3 Cenários de decisão

| Evento | Efeito sobre a oportunidade | Efeito na cota/reserva | Efeito econômico |
|---|---|---|---|
| 31ª inscrição após bônus para 30 | Inscrição permitida se evento aberto | Nenhuma nova reserva do bônus | Não cria obrigação de 100 pontos |
| Cancelamento antes do gatilho | Conforme regulamento de inscrição | Reserva pode ser liberada; redistribuição só se prevista | Saldo retorna à disponibilidade após conciliação |
| Não comparecimento a evento | Inscrição pode ter existido | Não creditar prêmio condicionado à presença | Obrigação condicional extinta ou contestável |
| Resultado esportivo contestado | Participação pode permanecer válida | Prêmio por posição suspenso até adjudicação | Manter lastro do valor em disputa |
| Oportunidade paga estornada | Elegibilidade econômica revogada conforme regras | Suspender/reverter crédito quando permitido | Tratar resgate já ocorrido em procedimento formal, não subtrair em silêncio |
| Duas campanhas competindo pelo último saldo | Publicações condicionadas ao orçamento | Reservar atomicamente sem duplicidade | Não permitir exposição superior ao lastro |
| Resgate Mall confirmado | Oportunidade originária permanece histórica | Debitar saldo uma única vez | Liquidação conforme preço, parceiro e conciliação |
| Reserva Travel cancelada | Aplicam-se regras do fornecedor/Guivos Travel | Reverter bloqueio/crédito conforme estágio | Reconciliação de taxas e estornos dependente de contrato |
| Expiração de pontos | Sem alteração retrospectiva da oportunidade | Respeitar prazo informado e contestação | Destinação de recurso remanescente exige regra contratual |
| Ofertante encerra atividade | Não extinguir direitos adquiridos por padrão | Reservas e obrigações em aberto precisam continuidade | Política de garantia e insolvência a adjudicar |

### 18.4 Exemplos ilustrativos comparados

**Oportunidade paga:** preço elegível R$ 200, taxa escolhida hipotética de 5%, orçamento econômico do benefício R$ 10. Em PAR-A, pontos emitidos dependem da paridade oficial uniforme. Em PAR-B, o valor de emissão e a capacidade de resgate são definidos por fatores diferentes, exigindo garantir ao menos a obrigação prometida segundo termos comunicados. Nenhuma taxa oficial foi definida.

**Corrida:** primeira faixa 30 × 100 = **3.000 pontos**; podium 1.000 + 600 + 300 = **1.900 pontos**; obrigação máxima nominal **4.900 pontos**, sem empates que aumentem a distribuição. Em FUND-A, a campanha deve ter seu lastro reservado; em FUND-B, cada faixa deve bloquear parte do saldo pré-pago do ofertante. Inscrições além da 30ª seguem possíveis sem o bônus de inscrição.

### 18.5 Regras de transparência e direitos

- Antes da adesão, revelar condição elegível, teto de beneficiários, regra de prioridade e se pontos são estimados, reservados, pendentes ou disponíveis.
- Nenhuma mudança unilateral de paridade deve eliminar sem tratamento adequado um benefício já legitimamente adquirido.
- Distinguir financiamento de pontos de tarifa da plataforma: custo do incentivo pertence integralmente ao ofertante; taxas adicionais, se existirem, demandam política própria.
- Não tratar custo do incentivo como desconto obrigatório nem pontos como dinheiro resgatável em espécie sem autorização.
- Manter razão financeira, ledger de pontos e estados de oportunidade como registros reconciliáveis, mas distintos.
- Proibir que pontos comprados pelo ofertante alterem o ranking de relevância, a confiança ou o mérito de reconhecimentos.

### 18.6 Parecer analítico e portas de decisão

**PAR-A + FUND-A**: candidato de referência para simulação simples de uma campanha; simplicidade não é decisão de adoção.

**PAR-A + FUND-B**: candidato para ofertantes recorrentes, com saldo reutilizável e reservas individuais auditáveis.

**PAR-B + FUND-A/FUND-B**: somente se a flexibilidade justificar complexidade e comunicação transparente do valor de resgate.

**Pendências antes de decisão econômica:** paridade de emissão/resgate, lastro unitário, custo de cobertura, retenção, custódia, conciliação, regras de pontos vencidos, reversões após resgate, responsabilidades Mall/Travel, análise jurídica-fiscal-contábil e compatibilidade com a unidade única de valor da Guivos.

**Próxima etapa candidata:** instrumento de adjudicação econômica `PAR-01/PAR-02/FUND-01/LIQ-01/LIQ-02`, com campos para premissas, efeitos, riscos, evidências e aprovação por autoridade legítima. Esta etapa não gera superfície/ID `GKR-SURF`, transição `GKR-TRN` ou autorização de implementação.

```text
VERSION → v0.9.0 CANDIDATE
PARITY MODELS → COMPARATIVE EXAM COMPLETE / NO NORMATIVE CHOICE
FUNDING MODELS → COMPARATIVE EXAM COMPLETE / ISSUER FUNDS 100%
CANCELLATION / REVERSAL / MALL / TRAVEL → SCENARIOS DOCUMENTED
HOME PERSON AND O-C → UNCHANGED
PR #655 → OPEN / DRAFT
GKR MAIN / MENU / MASTERS / REGISTRIES → UNCHANGED
ENGINEERING / POINT ISSUANCE / LIVE REDEMPTION → NOT AUTHORIZED
```

## 19. Instrumento de decisão econômica — PAR-01/PAR-02/FUND-01/LIQ-01/LIQ-02 (v1.0.0 candidato)

**Natureza:** formulário documental de adjudicação futura, sem decisão financeira registrada ou poderes presumidos. O ofertante financia 100% dos pontos propostos, seja Organização ou Coletivo. Pontos são facultativos e secundários à proposta de valor Guivos.

### 19.1 Princípios que toda decisão deve preservar

- Unidade única de pontos do ecossistema, com semântica e regras comunicáveis à Pessoa.
- Valor econômico prometido coberto integralmente pelo ofertante, sem obrigação implícita de subsídio Guivos.
- Inscrições em oportunidades independentes do número de beneficiários de pontos.
- Pontos podem decorrer de percentual sobre oportunidade paga ou regras fixas por participação/classificação em evento gratuito ou pago.
- Reserva de orçamento, elegibilidade, crédito em saldo, resgate e liquidação são eventos distintos.
- Guivos Mall e Guivos Travel só aceitam/resgatam pontos sob contratos e regras operacionais próprios.
- Não impor ranking de relevância ou reconhecimento institucional por capacidade de financiar pontos.

### 19.2 Quadro de adjudicação

| Gate | Pergunta institucional | Opções avaliadas | Evidência mínima | Situação |
|---|---|---|---|---|
| **PAR-01** | Qual fator de emissão e precisão/arredondamento transforma benefício econômico ou prêmio em pontos? | PAR-A fixa; PAR-B com taxas distintas; regras explícitas para pontos fixos | Fórmulas, casos monetários, cenários de arredondamento, transparência | ABERTO |
| **PAR-02** | Qual capacidade de utilização/resgate por ponto e como preservar valor e direitos adquiridos? | Valor uniforme ou regras diferenciadas governadas; PAR-C em catálogo | Teste de custos Mall/Travel, validade, mudança de política e comunicação | ABERTO |
| **FUND-01** | Como assegurar lastro e segregar compromissos de cada ofertante/campanha? | FUND-A campanha; FUND-B saldo pré-pago; FUND-C garantia | Conciliação financeira, ledger, insolvência, limites e saldo residual | ABERTO |
| **LIQ-01** | Como aceitar e liquidar pontos em pedidos elegíveis do Mall? | Abatimento/cobertura conforme contratos dos vendedores | Reserva de checkout, confirmação, taxas, estorno, parceiro recebedor | ABERTO |
| **LIQ-02** | Como aceitar e liquidar pontos em reservas elegíveis do Travel? | Resgate com cotação e confirmação de disponibilidade | Prazo de reserva, cancelamento, fornecedor, diferença tarifária | ABERTO |

### 19.3 Campos obrigatórios em cada decisão

```text
GATE: [PAR-01 / PAR-02 / FUND-01 / LIQ-01 / LIQ-02]
VERSÃO DA POLÍTICA: [NÃO DEFINIDA]
AUTORIDADE COMPETENTE / FUNDAMENTO: [COMPROVAR]
PROPOSTA ESCOLHIDA: [NÃO ESCOLHIDA]
OPÇÕES DESCARTADAS E MOTIVAÇÃO: [PENDENTE]
FÓRMULA / UNIDADE / PRECISÃO: [PENDENTE]
CUSTO E OBRIGAÇÃO PARA OFERTANTE: [PENDENTE]
DIREITO, VALIDADE E COMUNICAÇÃO À PESSOA: [PENDENTE]
LIQUIDAÇÃO E RESPONSABILIDADE DOS PRODUTOS: [PENDENTE]
FRAUDE / ESTORNO / CONTESTAÇÃO / RISCO: [PENDENTE]
EVIDÊNCIAS E TESTES ECONÔMICOS: [PENDENTES]
ANÁLISE JURÍDICA / FISCAL / CONTÁBIL APLICÁVEL: [PENDENTE]
RESULTADO: [APROVAR / APROVAR_COM_AJUSTES / DEVOLVER / REJEITAR]
DATA / SIGNATÁRIO / FUNDAMENTO: [NÃO REGISTRADOS]
```

A concordância para prosseguir a documentação não preenche o resultado nem comprova competências decisórias.

### 19.4 Matriz de dependências

```text
PAR-01 + PAR-02
    → fatores oficiais e direitos dos pontos

FUND-01
    → compromisso econômico coberto e reservas auditáveis

PAR + FUND
    → emissão condicionada a elegibilidade verificável

LIQ-01 / LIQ-02
    → aceitação, cotação, bloqueio, resgate, estornos, repasse

VALIDAÇÃO JURÍDICA / FISCAL / CONTÁBIL + UX + AUDITORIA
    → autorização técnica/homologação posterior
```

PAR-01/PAR-02 e FUND-01 devem convergir antes de liberar compromissos reais; LIQ-01 e LIQ-02 demandam regras específicas de cada produto, sem supor que a aprovação de um libera o outro.

### 19.5 Testes de consistência que devem acompanhar a deliberação

1. R$ 200 de base elegível × 5% hipotéticos = R$ 10 de obrigação econômica; confirmar pontos emitidos, taxa de resgate, cobertura e arredondamento.
2. Corrida com 100 pontos às primeiras 30 inscrições: teto de 3.000 pontos, sem bloquear inscrições subsequentes.
3. Bônus por classificação de 1.000/600/300 pontos separado do teto acima: exposição combinada de 4.900 pontos, sujeita a regras de empate.
4. Duas campanhas tentando comprometer o último saldo de um ofertante: evitar duplo bloqueio.
5. Desistência e ausência: prova de elegibilidade e redistribuição de cota apenas quando prevista.
6. Compra ou reserva cancelada após crédito: tratamento do estorno e eventual resgate já efetuado.
7. Variação de preço de item Mall ou reserva Travel: garantir cotação e confirmação adequadas antes da liquidação.
8. Inadimplência, fechamento do ofertante ou indisponibilidade do parceiro: tratar direitos e obrigações sem transferir automaticamente o custo à Guivos.

### 19.6 Critério de saída e próximo passo

O instrumento estará **pronto para apreciação econômica formal** quando vier acompanhado de tabelas de valores, simulações financeiras, modelo de garantia, responsáveis e pareceres pertinentes. Estar pronto para apreciação não equivale a ratificação.

**Próxima etapa:** simulações comparativas de paridade e capacidade financeira por campanha/ofertante, com cenários explícitos de emissão, resgate, custo, estorno e saldos remanescentes, utilizando números **hipotéticos** até aprovação de taxas oficiais.

```text
DOCUMENT CANDIDATE → v1.0.0
ECONOMIC DECISION INSTRUMENT → DRAFTED
PAR-01/PAR-02/FUND-01/LIQ-01/LIQ-02 → 0/5 NORMATIVE DECISIONS
ISSUER FUNDS → 100%
POINTS → OPTIONAL
HOME PERSON / HOME O-C → UNCHANGED
GKR MAIN / MENU / MASTERS / REGISTRIES → UNCHANGED
PR #655 → OPEN / DRAFT
REAL POINT ISSUANCE / REDEMPTION / REPLIT → NOT AUTHORIZED
```

## 20. Simulações econômicas comparativas — emissão, reservas e resgate (v1.1.0 candidato)

**Natureza:** ensaio matemático hipotético, não precificação oficial, oferta pública ou autorização financeira. O ofertante custeia 100% do compromisso; pontos e taxas abaixo são cenários apenas para comparação.

### 20.1 Premissas transparentes

- **Cenário A:** 100 pontos por R$ 1,00 de benefício financiado, resgate teórico a R$ 0,01 por ponto. Equivalência matemática simétrica; sem tarifas.
- **Cenário B:** 100 pontos por R$ 1,00 de benefício financiado, resgate teórico a R$ 0,008 por ponto. Equivalência assimétrica; diferença **não é automaticamente margem ou receita** da Guivos, pois existem custos, obrigações, direitos e efeitos jurídicos a avaliar.
- **Cenário C:** 50 pontos por R$ 1,00 de benefício financiado, resgate teórico a R$ 0,02 por ponto. Equivalência econômica simétrica com menor quantidade nominal.
- Todos os cenários desconsideram tarifas operacionais, tributos, spread de fornecedor, riscos de cancelamento e precificação específica do Mall/Travel, que deverão compor simulação posterior.

### 20.2 Oportunidade paga: R$ 200, benefício opcional hipotético de 5%

`B = R$ 200 × 5% = R$ 10,00`; obrigação econômica-base do ofertante: **R$ 10,00**, além de encargos que venham a ser contratados.

| Cenário | Pontos emitidos | Valor teórico de resgate | Diferença teórica entre B e resgate |
|---|---:|---:|---:|
| A | 1.000 | R$ 10,00 | R$ 0,00 |
| B | 1.000 | R$ 8,00 | R$ 2,00 |
| C | 500 | R$ 10,00 | R$ 0,00 |

**Atenção:** a diferença do cenário B não constitui receita reconhecida, desconto em benefício contratado ou justificativa para reduzir o que foi anunciado à Pessoa. A política precisará declarar a economia efetiva e seus compromissos.

### 20.3 Corrida: 100 pontos às primeiras 30 inscrições e prêmio de classificação

`P_inscricao = 30 × 100 = 3.000 pontos`; `P_podio = 1.000 + 600 + 300 = 1.900 pontos`; teto de exemplo **4.900 pontos**, sem multiplicador por empates. Inscrições após a 30ª continuam disponíveis segundo regras do evento, **sem esse bônus específico**.

| Cenário | Teto nominal de pontos | Valor teórico de resgate a cobrir |
|---|---:|---:|
| A | 4.900 | R$ 49,00 |
| B | 4.900 | R$ 39,20 |
| C | 4.900 | R$ 98,00 |

Para prêmios fixados diretamente em **pontos**, o custo econômico de cobertura depende da paridade e do custo real de liquidação; portanto não pode ser inferido apenas do valor nominal. Antes de aprovação, verificar valor prometido, custos e se eventual modelo assimétrico atende às condições divulgadas.

### 20.4 Pré-financiamento: comparação FUND-A / FUND-B

**FUND-A — por campanha:** reserva econômica específica antes de lançar obrigação; conciliação individual e saldo remanescente após encerrar inscrições, resultados, recursos e resgates.

**FUND-B — saldo pré-pago do ofertante:** se o saldo disponível for R$ 100 e a primeira campanha reservar R$ 49, restariam **R$ 51 livres** para outras campanhas (cenário A, sem tarifas). Uma segunda reserva de R$ 60 deve ser negada ou condicionada a novo aporte; a reserva de R$ 49 continua protegida.

A simulação de saldo pressupõe que recursos podem ser legalmente recebidos e administrados segundo solução validada; **não constitui autorização para carteira financeira**.

### 20.5 Resgates e estornos exemplificados

**Mall:** compra elegível com abatimento teórico de 600 pontos no cenário A = R$ 6,00; confirmar disponibilidade de pontos, valor aplicável, regras do vendedor e liquidação, com reserva atômica para não debitar duas vezes.

**Travel:** reserva elegível com uso teórico de 2.000 pontos no cenário A = R$ 20,00; não pressupor disponibilidade, taxa de câmbio, cotação de fornecedor nem direito automático a reserva. Cancelamentos seguem contrato Travel/fornecedor; pontos bloqueados podem voltar ao saldo somente conforme estado verificável.

**Estorno de oportunidade paga:** se o valor elegível foi estornado antes de os pontos serem creditados, cancelar reserva correspondente. Se já houve crédito ou resgate, aplicar política de recuperação/compensação e contestação, sem débito silencioso em saldo pessoal.

**Inscrição cancelada:** reserva pode ser liberada, mas não passar automaticamente à pessoa seguinte sem regra de realocação previamente publicada.

### 20.6 Sensibilidade e sustentabilidade

| Parâmetro variável | Consequência a medir |
|---|---|
| Taxa de emissão | Pontos nominais concedidos e entendimento da Pessoa |
| Taxa de resgate | Valor efetivo entregue e exigência de lastro |
| Preço Mall/Travel e taxas de fornecedores | Diferenças reais de liquidação, não capturadas pelos cenários ideais |
| Participações válidas e cancelamentos | Obrigações efetivas versus reservas condicionais |
| Volume de campanhas simultâneas | Necessidade de saldo livre e controle de concorrência |
| Expiração, estorno após resgate e insolvência | Tratamento jurídico/contábil do passivo e direitos |

**Critério recomendado para próxima deliberação:** escolher primeiramente a *semântica de valor compreensível* e testar cobertura integral de obrigações; somente então parametrizar o número nominal de pontos, taxas de utilização, fontes de custeio e contratos de resgate.

### 20.7 Registro de testes analíticos (sem homologação)

```text
SCENARIO A: 200 × 0.05 = R$10; 1000 POINTS × R$0.01 = R$10
SCENARIO B: 200 × 0.05 = R$10; 1000 POINTS × R$0.008 = R$8
SCENARIO C: 200 × 0.05 = R$10; 500 POINTS × R$0.02 = R$10
REGISTRATION INCENTIVE: 30 × 100 = 3000 POINTS
PODIUM INCENTIVE: 1000 + 600 + 300 = 1900 POINTS
COMBINED CAP: 3000 + 1900 = 4900 POINTS
FUND-B TEST: R$100 - R$49 = R$51; R$60 EXTRA RESERVE UNSUPPORTED
```

**Próxima etapa candidata:** definir teste de decisão dos cenários A/B/C com critérios de comunicação de valor, lastro completo, custo de parceiros, tributos, garantia e proteção da Pessoa, preparando recomendação condicional aos gates PAR/FUND/LIQ — sem declarar taxas oficiais.

```text
VERSION → v1.1.0 CANDIDATE
ECONOMIC SIMULATIONS → DOCUMENTED / HYPOTHETICAL
POINT ISSUER FINANCING → 100% BY OFFERING ORGANIZATION OR COLLECTIVE
PAR/FUND/LIQ GATES → 0/5 RATIFIED
MALL / TRAVEL REDEMPTION → CONCEPTUAL EXAMPLES ONLY
GKR MAIN / MENU / MASTERS / REGISTRIES → UNCHANGED
PR #655 → OPEN / DRAFT
IMPLEMENTATION / REAL POINT ISSUANCE → NOT AUTHORIZED
```

## 21. Duas regras de custeio — abatimento no repasse de compra versus saldo pré-pago de premiações (v1.2.0 candidato)

**Decisão explícita do fundador, 12/10/2026:** distinguir obrigatoriamente dois modelos econômicos por origem dos pontos. Esta decisão substitui, nos casos de compra intermediada pela Guivos, a hipótese anterior de exigir pré-financiamento de todas as campanhas. Permanecem 100% custeados pelo ofertante; não há duplicação de cobrança de lastro.

### 21.1 Compra de oportunidade paga — retenção no repasse ao ofertante

**Contrato econômico definido para modelagem:**
1. A Organização ou Coletivo cadastra oportunidade paga com percentual opcional de pontos escolhido de opções predefinidas pela Guivos.
2. A Pessoa paga a oportunidade por fluxo de cobrança/liquidação **intermediado pela Guivos**, para que exista valor a repassar.
3. No acerto, a Guivos **abate do repasse ao ofertante o valor econômico correspondente aos pontos creditados à Pessoa**.
4. **A taxa da plataforma Guivos é cobrada separadamente desse abatimento**, segundo regras comerciais próprias (alíquota, incidência, tributos e taxas de meios de pagamento a definir).
5. O ofertante recebe o valor líquido após o benefício em pontos **e** após a taxa de plataforma aplicável. O benefício não é desconto no preço pago pela Pessoa.

**Exemplo expresso do fundador:** curso de **R$ 200,00**; percentual **1%**; Pessoa recebe **2 pontos**; valor de custeio desses pontos = **R$ 2,00**; repasse-base à Organização = **R$ 198,00**, **antes de descontar a taxa da plataforma Guivos**, se aplicável.

```text
COMPRA DA PESSOA                         R$ 200,00
RETORNO EM PONTOS (1%)                   2 pontos
VALOR ECONÔMICO DO INCENTIVO            R$   2,00
REPASSE-BASE À ORGANIZAÇÃO               R$ 198,00
TAXA DA PLATAFORMA GUIVOS                [DEFINIR] — SEPARADA
REPASSE LÍQUIDO FINAL AO OFERTANTE       R$ 198,00 - TAXA APLICÁVEL
```

**Paridade implícita deste caso aprovado como direção de modelagem:** para esta modalidade, 1% × R$ 200 = R$ 2 de incentivo e **2 pontos**; isto representa **1 ponto por R$ 1 de benefício calculado** na emissão percentual. Não implica por si só que **1 ponto vale R$ 1 no resgate no Mall/Travel**; a taxa de uso, custódia e liquidação deve ser formalizada de modo a honrar obrigações prometidas. A simulação anterior de 100 pontos por R$ 1 era hipótese e **não deve prevalecer sobre este exemplo**.

**Guarda essencial:** retenção só se aplica a transação efetivamente intermediada/liquidada pela Guivos. Para compras fora da plataforma, sem repasse sob controle da Guivos, não presumir abatimento possível nem direito automático a pontos; exigir integração e acordo distintos ou deixar a função desativada.

**Outras condições a especificar:** base de cálculo (valor efetivo pago), cálculo e arredondamento de frações de pontos, prazos de confirmação, chargebacks/estornos, refund parcial, separação contábil entre valores de terceiros e obrigações de pontos, limites de elegibilidade e conciliação com taxa da plataforma.

### 21.2 Eventos e premiações — orçamento em pontos pré-pago

1. Organização ou Coletivo adiciona/contrata **saldo pré-pago em pontos** no módulo de incentivos sob regras econômicas e de pagamento governadas.
2. Após confirmação do pagamento do saldo, configura livre e opcionalmente faixas e critérios: primeiras N inscrições, presença validada, posições/pódio, outras recompensas autorizadas.
3. Cada premiação **reserva pontos do saldo do ofertante**, sem ultrapassá-lo. Inscrições no evento permanecem abertas mesmo quando as cotas de pontos se esgotarem, conforme regras do evento.
4. Após comprovação do gatilho elegível, os pontos reservados são creditados à Pessoa; cancelamentos e saldos não utilizados seguem política contratual.
5. **Não há retenção de repasse de compras como fonte de cobertura para essas premiações.** Trata-se de pré-pagamento explícito do organizador.

**Exemplo:** Coletivo compra/deposita saldo de **4.900 pontos** e cria corrida com 100 pontos para as 30 primeiras inscrições elegíveis (3.000 pontos), primeiro lugar 1.000, segundo 600 e terceiro 300 (1.900 pontos). O sistema reserva o orçamento contratado, permite inscrições adicionais sem bônus de entrada e só distribui créditos com provas válidas. O **preço em reais da aquisição de 4.900 pontos não está definido** nesta etapa.

### 21.3 Matriz de duas origens

| Critério | Compra de oportunidade paga | Evento / premiação |
|---|---|---|
| Origem de financiamento | **Abatimento no valor de repasse ao ofertante** | **Saldo de pontos pré-pago pelo organizador** |
| Gatilho | Transação paga e liquidada elegível | Inscrição, presença, resultado ou critério válido |
| Escolha | Percentual em tabela Guivos | Pontos por critério e limite de beneficiários |
| Crédito | Pontos ao comprador | Pontos aos beneficiários elegíveis |
| Taxa da Guivos | Separada do percentual de pontos | Taxas de aquisição/serviço, se houver, separadas e explícitas |
| Necessidade de financiamento antecipado | **Não**, quando a Guivos controla repasse suficiente | **Sim**, saldo disponível antes das promessas |
| Oportunidade gratuita | Não admite retorno percentual baseado em preço inexistente | Pode distribuir premiações com saldo pré-pago |
| Limite de participantes | Regra da oportunidade independente | Regra do evento independente do limite de beneficiários de pontos |

### 21.4 Reconciliação expressa das análises anteriores

- Onde as seções 5, 11, 12, 17–20 tratam **pré-financiamento universal**, isso passa a ser **substituído para incentivos percentuais de compras intermediadas** pela retenção no repasse definida nesta seção. As alternativas FUND-A/B continuam aplicáveis à compra de saldo e distribuição em eventos.
- As taxas e cenários **A/B/C da seção 20 são experimentos históricos**, não taxas oficiais ou representação fiel da nova regra de 1% = 2 pontos para R$ 200.
- Separar **paridade de emissão em oportunidade paga** (fixada conceitualmente pelo exemplo) de **valor de compra de pontos pré-pagos** e **valor de resgate** (ambos pendentes de regra oficial).
- Evitar creditar pontos antes de pagamento elegível liquidado e conciliação do repasse, para não transformar reversões em subsídio involuntário.
- Não implementar fluxo de compra de pontos de um Coletivo antes de adjudicar autoridade de conta, mecanismo de pagamento, custódia, conciliação e responsabilidades contratuais.
- Repasses, taxas, reservas e valores não são receita reconhecida sem análise contábil; nada nesta seção autoriza operar serviços financeiros sem requisitos legais.

### 21.5 Próxima etapa

Atualizar a matriz PAR/FUND/LIQ, distinguindo formalmente **FIN-COMPRA** (retenção na liquidação) de **FIN-EVENTO** (saldo pré-pago) e definir cálculo, prazos, contabilidade, estorno e pagamento do saldo. Preservar a hierarquia narrativa das Homes: pontos são recurso secundário da experiência.

```text
CANDIDATE VERSION → v1.2.0
USER-DECIDED COMPRA → 1% OF R$200 = 2 POINTS / R$2 COST / R$198 PRE-FEE TRANSFER
USER-DECIDED EVENTO → POINT BALANCE PREPAID BY ORGANIZER
ISSUER COST SHARE → 100%
PLATFORM FEE → ADDITIONAL / SEPARATE / NOT YET PARAMETERIZED
POINT REDEMPTION PARITY → NOT DECIDED
PR #655 → OPEN / DRAFT
MAIN / MASTERS / MENU / PRODUCT / REPLIT → UNCHANGED
```

## 22. Reconciliação dos gates econômicos — duas origens de financiamento (v1.3.0 candidato)

**Resultado:** reconciliação documental das regras decididas pelo fundador com os cinco gates PAR/FUND/LIQ; sem aprovar parâmetros financeiros ou emissão real.

### 22.1 Regras de precedência

**FIN-COMPRA — retorno percentual nas compras intermediadas pela Guivos.** Valor de pontos sai do valor a repassar ao ofertante, sem exigir compra prévia de saldo. A taxa da plataforma é separada. Exemplo vinculante de direção de produto: `R$ 200 × 1% = R$ 2 = 2 pontos`; `repasse-base = R$ 200 - R$ 2 = R$ 198`, antes da taxa Guivos. **A emissão percentual desse exemplo usa 1 ponto por R$ 1 de benefício econômico**; preço/valor de resgate ainda precisam de decisão.

**FIN-EVENTO — premiações por participação, inscrição, desempenho e colocação.** Organização/Coletivo obtém saldo de pontos antecipadamente, após pagamento confirmado; aloca e reserva pontos conforme regras, gatilhos e limites. A oportunidade/inscrição pode continuar mesmo após esgotamento do incentivo. O valor de compra de pontos pré-pagos permanece pendente.

**Precedência sobre comparações anteriores:** FUND-A/B não constituem mais pré-financiamento universal de todas as oportunidades. As simulações da seção 20 são históricas/hipotéticas e não substituem o cálculo de compra 1% → 2 pontos.

### 22.2 Reconciliação gate a gate

| Gate | FIN-COMPRA | FIN-EVENTO | Decisão remanescente |
|---|---|---|---|
| **PAR-01 — emissão** | Percentual × base elegível monetária; equivalência 1 ponto por R$ 1 do benefício no exemplo | Quantidade fixa de pontos do saldo pré-pago conforme campanha | Decimais, arredondamento, limites e mudanças da tabela percentual |
| **PAR-02 — valor de uso** | Pontos creditados à Pessoa após liquidação elegível | Pontos creditados após prova de participação/resultado | Paridade de resgate Mall/Travel, validade, proteção de direitos e comunicação |
| **FUND-01 — cobertura** | Abatimento no repasse ao ofertante, separado da taxa Guivos | Pagamento antecipado de saldo com reserva por incentivo | Custódia, contabilização, preço do saldo, critérios de cobertura e conciliação |
| **LIQ-01 — Mall** | Saldo creditado pode ser utilizado, se elegível e autorizado | Mesmo saldo único, sem distinção discriminatória por origem | Pedido, abatimento, repasse ao vendedor, cancelamento, custo e auditoria |
| **LIQ-02 — Travel** | Saldo creditado pode ser utilizado, se elegível e autorizado | Mesmo saldo único, sem distinção discriminatória por origem | Cotação, reserva, disponibilidade, fornecedor, cancelamento e liquidação |

**Unidade única:** a origem financeira do crédito não cria espécies incompatíveis de pontos para a Pessoa. O ledger poderá preservar origem e obrigações para conciliação, mas a experiência utilizará uma unidade de valor comum, sujeita à política de elegibilidade e resgate.

### 22.3 Campos de cálculo, pagamento e contabilidade

| Campo | Direção candidata |
|---|---|
| `purchase_paid_amount` | Valor efetivamente pago e elegível; imposto/frete/desconto/exclusões a definir |
| `selected_points_percent` | Opção predefinida da Guivos, selecionada expressamente pelo ofertante |
| `points_benefit_amount` | Valor pago elegível × percentual |
| `points_quantity` na compra | Quantidade equivalente ao benefício em R$, conforme exemplo; política de frações pendente |
| `gross_payable_to_issuer` | Montante da transação atribuível ao ofertante antes de retenções |
| `points_cost_withheld` | Custo em R$ dos pontos debitado no repasse |
| `guivos_platform_fee` | Taxa distinta e explícita, com base de incidência a definir |
| `issuer_transfer_net` | Repasse-base menos taxa e outras retenções legítimas expressamente previstas |
| `prepaid_points_balance` | Saldo em pontos adquirido e pago antes da campanha, com preço unitário a definir |
| `reserved_points` | Saldo bloqueado por incentivo/cota, sem creditá-lo ainda à Pessoa |
| `issued_points` | Pontos efetivamente creditados após gatilho validado |
| `redeemed_points` | Pontos consumidos em Mall/Travel sob contrato aplicável |

**Fórmula ilustrativa da compra sem outros ajustes:**
```text
VALOR ELEGÍVEL = 200,00
PERCENTUAL = 1%
CUSTO DE PONTOS = 200,00 × 0,01 = 2,00
PONTOS CREDITÁVEIS = 2 (sujeito à elegibilidade/liquidação)
REPASSE-BASE = 200,00 - 2,00 = 198,00
REPASSE FINAL = 198,00 - TAXA GUIVOS APLICÁVEL
```

A classificação contábil dos valores retidos, taxas, receitas e obrigações necessita validação própria; a retenção dos R$ 2 **não** deve ser equiparada automaticamente a receita.

### 22.4 Estornos e condições de emissão

**Compras:** a confirmação do pagamento e do direito ao repasse deve sustentar o crédito; compra cancelada ou parcialmente estornada requer ajuste proporcional, com regras para pontos já creditados ou usados. Não exigir que o ofertante antecipe recursos para essa modalidade por simples herança do antigo modelo.

**Eventos:** pagamento do saldo precede sua utilização; inscrição elegível pode reservar um benefício, mas presença/posição precisa de prova conforme regulamento. Cancelamentos e redistribuição de cotas seguem regra explícita, sem compromisso acima do saldo não reservado.

**Resgates:** Mall e Travel consultam a mesma unidade de pontos, reservam no checkout elegível e liquidam após confirmação, sem presumir disponibilidade de produtos ou viagens; eventual devolução de pontos acompanha o ciclo do pedido/reserva.

### 22.5 Checklist de validação futura

1. Especificar quais valores compõem a base elegível e como pontos fracionários serão tratados.
2. Definir tabela oficial de percentuais e se há mínimo/máximo por compra.
3. Deliberar incidência, percentual e destinatário da taxa Guivos, junto com custos de pagamento e tributos.
4. Definir **preço de aquisição** dos pontos pré-pagos e cobertura do custo de resgate.
5. Fixar paridade de utilização, condições, validade e destino de recursos não utilizados.
6. Documentar conciliação entre transação paga, repasse ao ofertante, retenção para pontos, ledger e estorno.
7. Proteger independência entre cotas de pontos e número de inscrições/participações.
8. Revisar responsabilidade jurídica, fiscal, contábil e de proteção de dados antes de operar.
9. Definir transições oficiais, testes e homologação próprios para compra e premiações, sem criar IDs por inferência.

### Próxima etapa

**Etapa candidata:** contrato econômico-funcional dos dois fluxos, com casos de borda de frações, refund parcial, indisponibilidade de repasse, recompensas cumulativas e saldo insuficiente. Sem mudanças na Home nem autorização de engenharia.

```text
VERSION → v1.3.0 CANDIDATE
FIN-COMPRA → WITHHOLD POINTS COST FROM PAYOUT
FIN-EVENTO → PREPAID POINT BALANCE REQUIRED
ISSUER FUNDS POINTS → 100%
PAR/FUND/LIQ → RECONCILED DOCUMENTALLY; 0/5 FORMAL GATES RATIFIED
REDEMPTION PARITY / PREPAID PRICE / PLATFORM FEES → OPEN
PR #655 → OPEN / DRAFT
GKR MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 23. Contrato econômico-funcional dos dois fluxos e casos de borda (v1.4.0 candidato)

**Estado:** contrato funcional candidato preparado para exame; não equivale a homologação ou implantação. As decisões expressas permanecem: (a) compras elegíveis geram pontos por percentual com **abatimento no repasse ao ofertante**, taxa Guivos separada; (b) eventos e premiações usam **saldo de pontos pré-pago** pela Organização/Coletivo. Em ambos, o ofertante suporta integralmente o custo dos pontos.

### 23.1 Fluxo FIN-COMPRA — cálculo e repasse

```text
OPORTUNIDADE PAGA + PERCENTUAL OPCIONAL PRÉ-DEFINIDO
→ COMPRA INTERMEDIADA PELA GUIVOS
→ PAGAMENTO CONFIRMADO / CONDIÇÃO DE LIQUIDAÇÃO VERIFICADA
→ BASE ELEGÍVEL × PERCENTUAL = VALOR DO INCENTIVO (R$)
→ CONVERSÃO EM PONTOS (REGRA DE FRAÇÕES PENDENTE)
→ ABATIMENTO DO CUSTO DO INCENTIVO NO REPASSE AO OFERTANTE
→ COBRANÇA SEPARADA DA TAXA GUIVOS
→ REPASSE LÍQUIDO RECONCILIADO
→ CRÉDITO DA PESSOA SEGUNDO REGRA DE CONFIRMAÇÃO/ESTORNO
```

**Fórmula base sem demais retenções:** `R = V - (V × p) - T`, onde `V` é o valor elegível efetivamente atribuído ao ofertante, `p` o percentual optativo e `T` a taxa aplicável da plataforma, definida separadamente. O cálculo oficial precisará esclarecer quando a base é diferente do valor total cobrado (tributos, frete, descontos, cupons, taxas de terceiros e múltiplos ofertantes).

**Caso expresso:** R$ 200 × 1% → custo de R$ 2 → 2 pontos à Pessoa → repasse-base de R$ 198, antes de `T`.

### 23.2 Frações, precisão e arredondamento

Exemplo meramente técnico: compra de R$ 149,90 com 1% produz benefício econômico de **R$ 1,499**. A diretriz 1 ponto para R$ 1 de benefício do exemplo não define se a Pessoa receberá pontos inteiros, frações de pontos ou acumulação residual.

**Alternativas a adjudicar:**
- `ROUND-A`: permitir pontos fracionários com precisão padronizada.
- `ROUND-B`: emitir apenas pontos inteiros, com regra clara sobre valores residuais.
- `ROUND-C`: acumular frações economicamente devidas até atingir unidade creditável.

**Proteção obrigatória:** a retenção econômica no repasse deve reconciliar exatamente a obrigação emitida e os resíduos; não reter silenciosamente valores que não geram direito correspondente. Determinar também a precisão monetária e o instante do arredondamento (item, compra ou liquidação consolidada).

### 23.3 Estorno parcial e total em FIN-COMPRA

- **Antes do crédito:** recalcular a base após estorno e cancelar/reduzir pontos pendentes e abatimento no repasse conforme liquidação.
- **Após crédito, antes de resgate:** executar ajuste rastreável, observando notificação e contestação.
- **Após resgate dos pontos:** registrar obrigação de ajuste/compensação com procedimento e responsáveis previamente definidos; não lançar saldo negativo oculto.
- **Exemplo:** compra de R$ 200 a 1% (2 pontos) com devolução elegível de R$ 50 → base remanescente R$ 150 e benefício remanescente de R$ 1,50; a quantidade de pontos definitiva depende da regra de frações. A retenção inicial de R$ 2 deverá ser recalculada sem exceder o compromisso final.

**Falha ou indisponibilidade de repasse:** se o valor não for recebido ou não estiver sob controle da Guivos, não ativar retenção fictícia nem liberar crédito sem lastro. Transações com intermediário externo exigem contrato explícito, prova de liquidação e estratégia de liquidação aprovada. Conciliar eventuais chargebacks e inadimplência.

### 23.4 Fluxo FIN-EVENTO — aquisição, reserva e premiação

```text
OFERTANTE ADQUIRE SALDO DE PONTOS (PAGAMENTO PRÉVIO CONFIRMADO)
→ SALDO DISPONÍVEL
→ CONFIGURA CAMPANHA, REGRAS, LIMITES E GATILHOS
→ RESERVA ATÔMICA DOS PONTOS NECESSÁRIOS
→ INSCRIÇÕES/RESULTADOS ELEGÍVEIS COMPROVADOS
→ CRÉDITOS EM CONTAS DE PESSOAS
→ CONCILIAÇÃO DE RESERVAS, SALDO LIVRE E CONTROVÉRSIAS
```

Exemplo: 4.900 pontos em saldo pré-pago; 3.000 reservados para as primeiras 30 inscrições elegíveis e 1.900 para pódio. Inscrições subsequentes continuam disponíveis sem bônus das primeiras 30, se o evento permanecer aberto.

**Saldo insuficiente:** impedir nova promessa/reserva que exceda saldo livre, permitir recarga validada antes da ativação e preservar compromissos já assumidos. A falta de pontos não pode cancelar automaticamente uma inscrição válida; eventual suspensão da promoção é distinta da continuidade do evento.

**Premiações acumuladas:** participação e classificação podem acumular se o regulamento permitir; reservar o teto máximo de cada modalidade, evitar crédito em duplicidade e explicitar empates/redistribuição.

### 23.5 Contratos de estado e evidência, sem criação de IDs oficiais

| Evento candidato | Evidência mínima | Efeito econômico |
|---|---|---|
| Compra liquidada | Transação reconciliada e repasse sob controle | Habilita abatimento e geração elegível de pontos |
| Pagamento de saldo de pontos | Pagamento confirmado do ofertante | Aumenta saldo pré-pago disponível |
| Campanha ativada | Regulamento, tetos e saldo reservado | Bloqueia orçamento para obrigações prometidas |
| Inscrição elegível | Confirmação com ordem verificável | Reserva cota, sem necessariamente creditar |
| Participação/resultado confirmado | Prova proporcional e direito de contestação | Autoriza crédito da modalidade correspondente |
| Estorno/cancelamento | Evento financeiro ou funcional verificável | Ajuste/reversão com trilha |
| Resgate Mall/Travel | Cotação elegível, disponibilidade e confirmação | Bloqueia/debita pontos e registra liquidação |

### 23.6 Invariantes de reconciliação

1. **FIN-COMPRA:** `valor pago elegível = repasse ofertante + custo pontos retido + taxa Guivos + demais valores legítimos explicitamente discriminados`, com tratamento contábil conforme contrato.
2. **FIN-EVENTO:** `saldo adquirido = saldo livre + saldo reservado + pontos distribuídos + outros ajustes rastreáveis` considerando recargas e estornos; não inferir que pontos já distribuídos continuam saldo do ofertante.
3. Os dois fluxos geram a **mesma unidade de pontos da Pessoa**, mas possuem lançamentos financeiros de origem diferentes.
4. Idempotência na liquidação, na reserva, no crédito e no resgate; concorrência nunca permite usar uma mesma cota/saldo duas vezes.
5. Oportunidade pode existir sem incentivo; benefício esgotado não implica inscrições encerradas.
6. Nenhuma obrigação econômica é gerada por clique, inscrição externa não confirmada, visualização, conclusão presumida ou resultado não validado.
7. Informações sensíveis da Journey não são condição implícita para verificar direito a pontos.

### 23.7 Casos obrigatórios para testes futuros

| Caso | Comportamento requerido |
|---|---|
| R$ 149,90 × 1% | Não fixar pontos finais até política oficial de frações |
| Estorno parcial de R$ 50 em compra de R$ 200 | Reconciliar R$ 1,50 de benefício residual com pontos e abatimento |
| Plataforma não controla repasse | Não presumir retenção possível |
| 30ª/31ª inscrições simultâneas | Uma única última cota de benefício; inscrições independentes |
| Saldo do ofertante menor que prêmio programado | Bloquear nova promessa, manter inscrições conforme evento |
| Pessoa vence e também recebe bônus de inscrição | Acumular somente conforme regra divulgada, sem crédito duplicado |
| Cancelamento após pontos utilizados | Ajuste rastreável, sem saldo negativo silencioso |
| Compra de saldo do ofertante estornada | Congelar emissão futura e reconciliar reservas/direitos válidos |
| Resgate no Mall ou Travel cancelado | Reconciliar bloqueio, devolução e repasse conforme contrato de produto |

### 23.8 Pendências de formalização

`ROUND-A/B/C`, definição de base elegível, catálogo de percentuais, momento de crédito, taxas, preço do saldo pré-pago, paridade de resgate, cronograma de repasses, contratos de custódia e liquidação, tributação, proteção de consumidores, LGPD, responsabilidade por chargebacks e homologação permanecem pendentes de decisões específicas.

**Próxima etapa candidata:** adjudicação comparada de regras de fração e resíduos em FIN-COMPRA, acompanhada de reconciliação numérica completa de estornos e da cobertura econômica da conta de pontos pré-pagos.

```text
VERSION → v1.4.0 CANDIDATE
FIN-COMPRA → ABATIMENTO NO REPASSE; TAXA GUIVOS SEPARADA
FIN-EVENTO → SALDO DE PONTOS PRÉ-PAGO PELO OFERTANTE
POINT ISSUER FINANCING → 100%
FRACTIONS / FEES / PREPAID UNIT PRICE / REDEMPTION VALUE → NOT ADJUDICATED
PAR/FUND/LIQ → 0/5 FORMAL GATES RATIFIED
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 24. Frações, resíduos e conciliação de estornos — avaliação ROUND-A/B/C (v1.5.0 candidato)

**Estado:** exame técnico comparativo, sem definição normativa da política de arredondamento. Mantêm-se as decisões: FIN-COMPRA financiado por retenção no repasse; FIN-EVENTO financiado por saldo pré-pago.

### 24.1 Precisão econômica e semântica

A compra de R$ 149,90 com retorno de 1% calcula exatamente **R$ 1,499 de benefício bruto** antes da regra monetária de centavos. Não há autorização para reter R$ 1,499 em um meio financeiro que liquida apenas em centavos nem para afirmar que 1,499 ponto foi creditado sem definir granularidade da unidade.

**Separar obrigatoriamente** (1) percentual aplicado à base; (2) valor monetário do incentivo após regra explícita de precisão; (3) pontos devidos/visíveis; (4) resíduos, quando houver; e (5) custo efetivamente retido em centavos. Não arredondar cada item e novamente o carrinho sem regra oficial.

### 24.2 Comparação de políticas

| Modelo | Pontos visíveis no exemplo | Tratamento de R$ 1,499 | Proteção e ônus |
|---|---|---|---|
| ROUND-A — pontos fracionários | 1,499 pontos antes da precisão adotada | Definir precisão do ponto (por exemplo 0,01 ou 0,001) e monetária | Melhor correspondência, mas exige UI, ledger e resgate fracionário |
| ROUND-B — pontos inteiros por compra | 1 ou 2 pontos, conforme arredondamento definido | Diferença residual precisa voltar ao ofertante ou ser lastreada sem ocultação | Simples na interface, risco de ganho/perda arbitrária em compras pequenas |
| ROUND-C — resíduo acumulado | 1 ponto + resíduo rastreável | Fração elegível permanece registrada e poderá converter em ponto futuro; valor retido exige conciliação | Pontos inteiros visíveis; precisa de subconta, expiração, estornos e política de encerramento |

**Recomendação técnica condicionada:** priorizar teste de **ROUND-A com precisão explícita**, por manter a proporcionalidade do retorno sem converter frações em saldo oculto; avaliar **ROUND-C** somente se a experiência de pontos inteiros for requisito de produto. **ROUND-B com truncamento ou arredondamento isolado por compra não é recomendável sem proteção expressa** da parcela não creditada. Isto **não aprova ROUND-A**.

### 24.3 Simulação monetária de uma compra

Para fins de teste, e **não como regra oficial**, suponha arredondamento monetário para centavos uma única vez por compra, `half-up`, com representação decimal exata:

| Compra elegível | Retorno | Incentivo bruto | Incentivo em centavos (hipótese) | Repasse-base antes da taxa |
|---|---:|---:|---:|---:|
| R$ 200,00 | 1% | R$ 2,000 | R$ 2,00 | R$ 198,00 |
| R$ 149,90 | 1% | R$ 1,499 | R$ 1,50 | R$ 148,40 |
| R$ 49,95 | 1% | R$ 0,4995 | R$ 0,50 | R$ 49,45 |
| R$ 0,49 | 1% | R$ 0,0049 | R$ 0,00 | R$ 0,49 |

**Observação crítica:** com ROUND-A, se ponto proporcional ao incentivo em reais, a quantidade creditada nesse ensaio deve reconciliar com **o valor final em centavos retido** (por exemplo **1,50 ponto**, não simultaneamente 1,499 ponto e retenção de R$ 1,50), salvo regra de diferença expressamente financiada. Qualquer arredondamento que produza incentivo nulo para compras pequenas deve ser transparente e validado.

### 24.4 Estorno parcial e recomposição

Compra original `R$ 200 × 1% → R$ 2,00 → 2 pontos`. Após devolução elegível de R$ 50, a base remanescente é R$ 150:

```text
BENEFÍCIO INICIAL            R$ 2,00 / 2,00 PONTOS
BENEFÍCIO RECOMPUTADO        R$ 1,50 / 1,50 PONTOS (ROUND-A HIPOTÉTICO)
AJUSTE DE INCENTIVO          -R$ 0,50 / -0,50 PONTOS
REPASSE-BASE RECOMPUTADO     R$ 150,00 - R$ 1,50 = R$ 148,50
TAXA GUIVOS / PROCESSAMENTO  A RECONCILIAR SEPARADAMENTE
```

**Não confundir** repasse-base final da compra (R$ 148,50) com **transferência adicional ou estorno em caixa** após um repasse original já efetuado; o segundo depende do fluxo financeiro real. Ledger deve registrar lançamentos de ajuste, não apagar o histórico.

### 24.5 Concorrência, compras agrupadas e disputas

- Se várias oportunidades forem adquiridas em um carrinho, calcular elegibilidade e percentual por **oportunidade/ofertante**, depois conciliar os totais; não retirar custo de pontos do repasse do ofertante errado.
- Se o pagamento tiver valor dividido em parcelas, definir se o direito surge pela transação integral liquidada ou por parcela efetivamente confirmada, sem duplicar créditos.
- Se estorno ocorrer após resgate Mall/Travel, registrar passivo e procedimento de regularização auditável sem debitar silenciosamente a Pessoa.
- Reservas de pontos de eventos não compartilham o mesmo algoritmo de arredondamento da compra; eventos prometem **quantidade nominal de pontos adquiridos antecipadamente** e exigem saldo suficiente.
- Idempotência de eventos de pagamento, estorno, crédito e ajuste; uso de decimal exato em vez de ponto flutuante binário para dinheiro.

### 24.6 Critérios para deliberação e aceite

1. Escolher precisão monetária e de pontos, forma de exibição e regra de arredondamento por transação.
2. Fazer coincidir custo retido no repasse, obrigação de pontos concedidos e lastro econômico da carteira, com diferenças expressamente contabilizadas.
3. Estipular como o resgate de frações funciona em Mall/Travel e como a política de expiração se aplica.
4. Validar exemplos de valor pequeno, divisão por ofertante, alteração de percentual, estorno antes/depois do crédito e cancelamento após resgate.
5. Obter aprovação jurídica, contábil, UX e governança econômica antes de tornar parâmetros operacionais.

**Próximo passo candidato:** matriz de adjudicação de ROUND-A/B/C, com especificação de precisão e política de repasse escolhidas pela autoridade competente. O exemplo fundador R$ 200 → 2 pontos → repasse-base R$ 198 fica preservado sem alteração.

```text
CANDIDATE → v1.5.0
ROUND-A/B/C → EXAMINED; ROUND-A CONDITIONALLY RECOMMENDED, NOT APPROVED
PRECISION / ROUNDING / RESIDUALS → NOT ADJUDICATED
FIN-COMPRA → PAYOUT DEDUCTION / PLATFORM FEE SEPARATE
FIN-EVENTO → PREPAID POINT BALANCE
PAR/FUND/LIQ FORMAL GATES → 0/5
PR #655 → OPEN / DRAFT
MAIN / MENU / MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 25. Instrumento de adjudicação ROUND — precisão, arredondamento e evidências (v1.6.0 candidato)

**Status:** pronto para apreciação, não adjudicado. A análise ROUND-A (pontos fracionários) é preferencial tecnicamente, mas não se presume decisão humana de precisão, valor de resgate ou metodologia contábil.

### 25.1 Decisões separadas

| Subgate | Questão | Proposta para testar | Situação |
|---|---|---|---|
| ROUND-01 | Pontos inteiros, fracionários ou resíduos acumulados? | ROUND-A, com frações visíveis | ABERTO |
| ROUND-02 | Quantas casas decimais para pontos? | Avaliar 2 versus 3 casas | ABERTO |
| ROUND-03 | Quando arredondar o benefício em reais? | Uma vez por oportunidade/ofertante e transação liquidada, com decimal exato | ABERTO |
| ROUND-04 | O que fazer com arredondamentos residuais? | Conciliar retenção em centavos e obrigação efetiva de pontos; sem diferença oculta | ABERTO |
| ROUND-05 | Como tratar pontos em estornos, cancelamentos e resgates já realizados? | Ajustes auditáveis, política informada e contestação | ABERTO |
| ROUND-06 | Como expor frações em saldo, checkout Mall e Travel? | Mesmo saldo com precisão uniforme, sem prometer resgate indisponível | ABERTO |

### 25.2 Conjunto de testes para aceitação futura

| Teste | Entrada | Esperado / critério |
|---|---|---|
| T01 — Caso fundador | R$ 200,00; 1% | Exatamente 2 pontos, retenção R$ 2,00, repasse-base R$ 198,00 |
| T02 — Compra com fração | R$ 149,90; 1% | Valor bruto R$ 1,499; demonstrar reconciliação com arredondamento monetário aprovado |
| T03 — Compra pequena | R$ 0,49; 1% | R$ 0,0049 bruto; declarar se benefício é zero ou acumulável, sem retenção indevida |
| T04 — Limiar de centavo | R$ 0,50; 1% | R$ 0,005 bruto; comparar modos half-up/half-even e evidenciar escolha, sem presumir um |
| T05 — Multi-ofertante | Itens R$ 80 e R$ 120, ofertantes distintos, ambos 1% | Reconciliar R$ 0,80 e R$ 1,20 separadamente; não cruzar repasses |
| T06 — Devolução parcial | R$ 200 com estorno R$ 50 | Benefício final R$ 1,50; diferença -R$ 0,50; repasse-base final teórico R$ 148,50, sem confundir com caixa pós-repasse |
| T07 — Estorno total | R$ 200 estornados | Ajuste completo dos 2 pontos, respeitando estado de resgate e política |
| T08 — Retry de pagamento | Mesmo ID transacional reapresentado | Zero duplicidade em retenção, ponto, taxa e repasse |
| T09 — Pagamento em parcelas | Pagamento parcelado com liquidações distintas | Uma só obrigação por base elegível; regra de crédito explicitada |
| T10 — Resgate e estorno posterior | Pontos usados em Mall/Travel antes de refund | Não gerar débito oculto; registrar disputa/compensação |
| T11 — Cashback versus prêmio | Compra com incentivo e participação no evento | Origens financeiras distintas, crédito único por gatilho, combinações só se divulgadas |
| T12 — Saldo evento insuficiente | Reserva excede pontos disponíveis | Falha da promoção sem impedir inscrição válida |
| T13 — Concorrência de cotas | Duas inscrições pela última vaga de bônus | Uma só reserva de pontos, ambas inscrições seguem regras do evento |

**Propriedade numérica obrigatória:** para cada ofertante e transação, `valor elegível = repasse-base + retenção de incentivo`, antes de taxa da plataforma e outros ajustes previstos. Para o saldo de pessoa, emissão, estorno e resgate devem preservar ledger verificável, não apenas um número final.

### 25.3 Registro de escolha — a preencher em deliberação

```text
POLÍTICA ROUND / VERSÃO: A DEFINIR
AUTORIDADE COMPETENTE E EVIDÊNCIA: A IDENTIFICAR
MODALIDADE SELECIONADA: ROUND-A / ROUND-B / ROUND-C / OUTRA
PRECISÃO DOS PONTOS: NÃO APROVADA
PRECISÃO E ARREDONDAMENTO MONETÁRIO: NÃO APROVADOS
NÍVEL DO CÁLCULO: ITEM / OPORTUNIDADE / TRANSAÇÃO — NÃO APROVADO
TRATAMENTO DOS RESÍDUOS: NÃO APROVADO
REGRAS PARA REFUND/CHARGEBACK: NÃO APROVADAS
CONSISTÊNCIA NO MALL E TRAVEL: A VALIDAR
EVIDÊNCIAS DOS TESTES T01..T13: NÃO EXECUTADOS
PARECER ECONÔMICO, CONTÁBIL, JURÍDICO E UX: PENDENTE
RESULTADO DA DELIBERAÇÃO: NÃO REGISTRADO
```

**Porta de saída:** definição formal dos subgates e validação econômica dos T01..T13, acompanhada de compatibilidade com PAR-02/FUND-01/LIQ-01/LIQ-02, precede implementação real. O presente instrumento é apenas uma proposta documental.

### 25.4 Próxima etapa

Montar tabela de decisão com **efeitos sobre saldo da Pessoa e conciliação por ofertante**, sobretudo para compras pequenas e cenários de arredondamento divergente, e estabelecer uma recomendação final condicionada para revisão humana.

```text
VERSION → v1.6.0 CANDIDATE
ROUND SUBGATES → 6 DOCUMENTED / 0 ADJUDICATED
ACCEPTANCE TESTS → 13 DEFINED / 0 EXECUTED
FIN-COMPRA / FIN-EVENTO → PRESERVED
PR #655 → OPEN / DRAFT
MAIN / MENU / MASTERS / REGISTRIES / IMPLEMENTATION → UNCHANGED
```

## 26. Comparação numérica ROUND-A/B/C — créditos, resíduos e repasse (v1.7.0 candidato)

**Status:** exemplos calculados com aritmética decimal exata e conferência matemática, sem teste de software produtivo nem adjudicação. Hipótese exclusivamente comparativa: percentual de 1%, benefício monetário arredondado para centavos com `half-up` uma vez por oportunidade/ofertante/transação. Essa política **não está aprovada**.

### 26.1 Contratos alternativos usados na simulação

- **ROUND-A:** crédito fracionário em pontos igual ao valor do benefício arredondado em reais; retenção igual a esse valor. Exige suportar ao menos duas casas nos pontos.
- **ROUND-B:** crédito apenas dos pontos inteiros por truncamento; **retenção ajustada ao valor realmente creditado**, devolvendo o resíduo ao repasse do ofertante. Não é admissível reter a fração sem a creditar ou contratualmente resolver o resíduo.
- **ROUND-C:** creditar imediatamente a parte inteira, registrar a fração em uma **subconta nominativa de direitos pendentes**, e reter economicamente a quantia correspondente ao benefício total; a fração acumulada deve ser convertível e a obrigação coberta. Para a simulação, o resíduo é demonstrado em equivalência monetária, não um crédito de resgate disponível.

### 26.2 Compras individuais

| Compra | Benefício bruto 1% | Benefício em centavos hipotético | ROUND-A: pontos imediatos / retenção | ROUND-B: pontos / retenção / repasse-base | ROUND-C: pontos + resíduo pendente / retenção |
|---|---:|---:|---|---|---|
| R$ 200,00 | R$ 2,0000 | R$ 2,00 | 2,00 pt / R$ 2,00 | 2 pt / R$ 2,00 / R$ 198,00 | 2 pt + 0,00 / R$ 2,00 |
| R$ 149,90 | R$ 1,4990 | R$ 1,50 | 1,50 pt / R$ 1,50 | 1 pt / R$ 1,00 / R$ 148,90 | 1 pt + 0,50 / R$ 1,50 |
| R$ 49,95 | R$ 0,4995 | R$ 0,50 | 0,50 pt / R$ 0,50 | 0 pt / R$ 0,00 / R$ 49,95 | 0 pt + 0,50 / R$ 0,50 |
| R$ 0,49 | R$ 0,0049 | R$ 0,00 | 0,00 pt / R$ 0,00 | 0 pt / R$ 0,00 / R$ 0,49 | 0 pt + 0,00 / R$ 0,00 |
| R$ 0,50 | R$ 0,0050 | R$ 0,01 | 0,01 pt / R$ 0,01 | 0 pt / R$ 0,00 / R$ 0,50 | 0 pt + 0,01 / R$ 0,01 |
| R$ 0,51 | R$ 0,0051 | R$ 0,01 | 0,01 pt / R$ 0,01 | 0 pt / R$ 0,00 / R$ 0,51 | 0 pt + 0,01 / R$ 0,01 |

**Exemplo de precisão:** R$ 149,90 × 1% = R$ 1,499 antes da política de centavos; sob a hipótese `half-up`, retorna R$ 1,50 e o ROUND-A concede 1,50 ponto. Não misturar valor bruto não liquidável de R$ 1,499 com retenção de R$ 1,50 e pontos 1,499 sem reconciliar a diferença.

### 26.3 Duas compras e efeito de agregação de resíduos

Pessoa compra oportunidades de R$ 149,90 e R$ 49,95, ambas elegíveis a 1%, de **dois ofertantes diferentes**.

- Benefícios arredondados por transação: R$ 1,50 + R$ 0,50 = **R$ 2,00**.
- ROUND-A: **2,00 pontos disponíveis** e R$ 2,00 retidos dos **respectivos ofertantes**.
- ROUND-B truncado com retenção equivalente: **1 ponto disponível**, R$ 1,00 retido do primeiro ofertante; **R$ 1,00** de incentivos calculados deixa de ser entregue, mas também não pode ser cobrado dos ofertantes.
- ROUND-C: **1 ponto disponível** e **1,00 ponto acumulado como resíduo**, que pode converter-se em um ponto adicional; R$ 1,50 e R$ 0,50 retidos **individualmente de cada ofertante**. A subconta exige política de titularidade, reversão e expiração.

**Cuidado:** a Pessoa pode somar benefícios em sua carteira, mas a conciliação financeira não pode misturar obrigações ou alterar repasses por ofertante.

### 26.4 Estorno parcial (caso fundador)

Compra original R$ 200,00 com 1% → 2 pontos / R$ 2 de retenção; estorno elegível de R$ 50,00 → base R$ 150,00 e benefício final R$ 1,50.

| Alternativa | Saldo de direito após estorno | Ajuste do incentivo | Repasse-base final teórico |
|---|---|---:|---:|
| ROUND-A | 1,50 pt | -R$ 0,50 / -0,50 pt | R$ 148,50 |
| ROUND-B truncado | 1 pt | -R$ 1,00 / -1 pt | R$ 149,00 |
| ROUND-C | 1 pt + 0,50 pt pendente | -R$ 0,50 / -0,50 pt de direito total | R$ 148,50 |

Repasse-base final teórico **não equivale** ao dinheiro que precisará ser movimentado após eventuais repasses originais: conciliar pagamentos e estornos já efetivados, taxa Guivos e custos dos meios de pagamento separadamente.

### 26.5 Decisão analítica condicionada

**ROUND-A** mantém a proporcionalidade prometida com menos estados ocultos e é o candidato técnico preferencial. **ROUND-C** preserva equivalência, mas requer subconta e regras adicionais. **ROUND-B** produz perda de incentivos percebidos em compras pequenas, salvo se oferta e percentual forem formulados de maneira compatível e explícita.

**Não decididos:** número máximo de decimais de pontos, arredondamento oficial, aplicação por linha/carrinho, regras de microvalores, preço de saldo pré-pago para eventos, taxa da plataforma e paridade de utilização Mall/Travel.

**Próxima etapa candidata:** submeter a preferência ROUND-A e hipótese de duas casas decimais ao rito de decisão competente, anexando evidências econômicas e teste de política em cenários de estorno, sem confundir acordo para continuidade documental com adjudicação.

```text
VERSION → v1.7.0 CANDIDATE
ROUND COMPARISON → MATHEMATICAL CASES DOCUMENTED (NOT LIVE TESTS)
ROUND-A → CONDITIONALLY PREFERRED / NOT RATIFIED
ROUND-01..06 → 0/6 ADJUDICATED
FIN-COMPRA → DEDUCT POINT COST FROM OFFEROR PAYOUT
FIN-EVENTO → PREPAID ORGANIZER BALANCE
PR #655 → OPEN / DRAFT
GKR MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 27. Parecer técnico ROUND-A: duas casas decimais e resgates Mall/Travel (v1.8.0 candidato)

**Natureza:** recomendação técnica formal para apreciação, sem aprovação de política, publicação, homologação ou implementação. O consentimento de continuidade da documentação não significa adjudicação de ROUND-01..06.

### 27.1 Proposta condicionada

- **ROUND-A como alternativa preferencial:** saldo da Pessoa suporta pontos fracionários, evitando perda de valor por truncamento por compra.
- **Precisão candidata:** **duas casas decimais para quantidade de pontos na unidade exibida**, sujeita a testes e validação de valor econômico.
- **Cálculo candidato:** calcular o percentual em aritmética decimal exata; arredondar o **benefício econômico** uma única vez por oportunidade/ofertante e transação elegível em centavos; então traduzir esse benefício em pontos com a equivalência aprovada no exemplo de FIN-COMPRA (**R$ 1,00 de incentivo = 1 ponto**). O modo `half-up` permanece **hipótese**, não política aprovada.
- **A mesma precisão deve percorrer carteira, reserva, checkout, resgate, reversão e conciliação**; nenhum produto pode arredondar silenciosamente ou ocultar a fração.
- **Separar taxa de emissão de valor de resgate:** duas casas decimais na quantidade não escolhem a paridade de utilização nem o preço de compra de pontos pré-pagos.

### 27.2 Exames de compatibilidade Mall / Travel

| Aspecto | Mall | Travel | Condição |
|---|---|---|---|
| Exposição do saldo | Exibir `1,50 ponto` e custo em pontos da oferta | Exibir `1,50 ponto` e pontos aplicáveis à reserva | Saldo único e legível |
| Cotação | Congelar valor de uso no pedido antes de confirmar | Congelar cotação e validade conforme fornecedor | PAR-02, LIQ-01/02 pendentes |
| Reserva | Bloqueio atômico de frações, com expiração clara | Bloqueio sob disponibilidade e tempo de cotação | Sem overspend |
| Liquidação | Consumo definitivo após condições do pedido | Consumo definitivo conforme reserva/fornecedor | Ledger idempotente |
| Estorno | Devolver frações elegíveis com rastreio | Devolver frações conforme multa/penalidade contratual | Sem devolução presumida |
| Arredondamento monetário | Taxa de conversão e centavos conciliados | Taxas/tarifas e fornecedor conciliados | Sem valor residual oculto |
| Oferta indivisível | Produto/pedido pode exigir quantidade mínima ou múltiplo | Reserva pode exigir mínimo ou cotação integral | Informar requisitos antes de confirmar |

**Princípio:** Guivos Mall e Guivos Travel podem oferecer regras distintas de elegibilidade e disponibilidade, mas não produzir pontos de qualidade desigual pela sua origem (FIN-COMPRA vs FIN-EVENTO) nem aplicar precisões contraditórias ao mesmo saldo da Pessoa.

### 27.3 Casos numéricos e riscos

**Caso P1 — compra do fundador:** R$ 200,00 × 1% = R$ 2,00 de incentivo = **2,00 pontos**; repasse-base ao ofertante **R$ 198,00**, antes da taxa da plataforma. Invariante obrigatória.

**Caso P2 — pequena fração:** R$ 149,90 × 1% = R$ 1,499 bruto; sob arredondamento hipotético de centavos `half-up` = R$ 1,50 → **1,50 ponto** e retenção de R$ 1,50; repasse-base R$ 148,40.

**Caso P3 — microtransação:** R$ 0,49 × 1% = R$ 0,0049, que arredondaria a R$ 0,00 sob o exemplo `half-up`. O resultado de 0,00 ponto não pode esconder uma retenção maior que zero. Produto deve decidir se há valor mínimo, acumulação ou regra de comunicação apropriada.

**Caso P4 — prêmio:** Coletivo configura 100,00 pontos por inscrição elegível, sujeito ao orçamento pré-pago e à cota; não há dedução de repasse por compra. Prêmios inteiros continuam permitidos.

**Caso P5 — resgate parcial hipotético:** se houver saldo de 2,50 pontos e resgate autorizado de 1,25 pontos, saldo restante = 1,25 pontos. O equivalente monetário só é conhecido após PAR-02 e cotação do produto; **não presumir 1 ponto = R$ 1 no resgate**.

**Caso P6 — ajuste após estorno:** 2,00 pontos iniciais, compra R$ 200,00; refund R$ 50,00 → benefício final 1,50 ponto na hipótese de precisão; ajuste de -0,50 ponto, sujeito a procedimento se resgate já ocorreu.

### 27.4 Recomendação para deliberação

**Propor como pacote técnico:** ROUND-A + quantidade de pontos com duas casas decimais + aritmética decimal exata + retenção reconciliada por ofertante + crédito somente após evento financeiro elegível + operações idempotentes em Mall/Travel.

**Não incluir automaticamente no pacote:** modo de arredondamento `half-up`, taxa de resgate, prazo de validade, preço do saldo pré-pago, forma de custódia, regra de microcompras ou autoridade de emissão; exigem deliberações separadas.

**Condições de aprovação futura:**
1. Demonstrar que duas casas decimais cobrem todos os percentuais permitidos com representação justa, inclusive em compras pequenas.
2. Executar testes T01..T13 e casos P1..P6 contra protótipo ou implementação verificável, após autorização técnica.
3. Validar custo máximo e lastro em cenários reais de Mall/Travel e em prêmios pré-pagos.
4. Garantir legibilidade de saldo, resgate e estorno à Pessoa; responsabilidade por tarifas e termos ao ofertante.
5. Obter registro de competência e aprovação formal de ROUND-01..06, PAR-02, FUND-01, LIQ-01 e LIQ-02 antes de ativação operacional.

```text
VERSION → v1.8.0 CANDIDATE
ROUND-A + 2 DECIMAL POINT PRECISION → FORMAL TECHNICAL RECOMMENDATION
HALF-UP → TEST ASSUMPTION ONLY
POINT REDEMPTION RATE → UNDECIDED
MALL/TRAVEL → COMPATIBILITY CONDITIONS DOCUMENTED / NOT IMPLEMENTED
ROUND-01..06 → 0/6 ADJUDICATED
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 28. Paridade transversal: emissão por compra, compra de saldo e utilização (v1.9.0 candidato)

**Escopo:** análise de consistência econômica — não autoriza taxa oficial, preço de pontos, operação financeira ou resgate real. O fundador definiu `R$ 200 × 1% = R$ 2 de custeio = 2 pontos`, com repasse-base de R$ 198 antes da taxa Guivos; e premiações/eventos com saldo de pontos pré-pago.

### 28.1 Três relações distintas

1. **FIN-COMPRA, emissão:** valor do benefício monetário calculado em R$ a partir do percentual e convertido em pontos na proporção do exemplo: **R$ 1 de custo de pontos = 1 ponto creditável** (sujeito à precisão/estorno). O custo é retido do repasse ao ofertante.
2. **FIN-EVENTO, aquisição de saldo:** Organização ou Coletivo **paga antecipadamente** um valor `C` para obter `P` pontos; **preço por ponto `a=C/P` ainda não aprovado**. Saldo disponível só após confirmação da aquisição e conciliação.
3. **MALL/TRAVEL, utilização:** Pessoa aplica `P` pontos sob regra `u` de benefício efetivo por ponto ou cotação de produto, **a definir**. Não inferir `u` a partir da regra de emissão, embora a sustentabilidade exija comparação entre custo, obrigação de resgate e taxas/fornecedor.

**Invariante:** pontos de origens diferentes formam uma mesma unidade de valor para a Pessoa; a conciliação financeira preserva origem, responsável por custeio e obrigação.

### 28.2 Matriz de cenários econômicos hipotéticos

Para tornar diferenças verificáveis, usar `a` = preço em R$ cobrado por ponto pré-pago e `u` = benefício monetário em R$ efetivamente coberto por ponto em resgate elegível, **ambos fictícios nos cenários abaixo**.

| Cenário | Emissão FIN-COMPRA | Aquisição FIN-EVENTO (`a`) | Utilização (`u`) | Exposição principal |
|---|---|---|---|---|
| EQ-1 — simétrico | R$ 1 retido → 1 ponto | R$ 1 por ponto | R$ 1 por ponto | Clareza; custos operacionais/fornecedores não cobertos sem tarifa ou contrato próprio |
| EQ-2 — aquisição diferenciada | R$ 1 retido → 1 ponto | R$ 1,05 por ponto | R$ 1 por ponto | Diferença de R$ 0,05 requer classificação e transparência; pode cobrir serviços, não presumir receita |
| EQ-3 — utilização inferior | R$ 1 retido → 1 ponto | R$ 1 por ponto | R$ 0,80 por ponto | Pessoa recebe benefício inferior ao custo nominal; risco de percepção enganosa se não comunicado previamente |
| EQ-4 — utilização superior | R$ 1 retido → 1 ponto | R$ 1 por ponto | R$ 1,10 por ponto | Obrigação pode superar lastro de origem; exige financiamento contratual extra explícito |

**Diagnóstico:** EQ-1 é **baseline conceitual para testar integridade de valor**, sem ser aprovado. EQ-2 permite separar eventual tarifa de serviço do custo dos pontos e merece simulação específica. EQ-3 e EQ-4 geram riscos que precisam de fundamento econômico, transparência, cobertura financeira e aprovação formal, não podendo ser adotados por inferência.

### 28.3 Exemplos consistentes por modalidade

**Curso de R$ 200 a 1%:** 2 pontos para Pessoa, R$ 2 de custo retidos, repasse-base **R$ 198** antes de taxa Guivos. Na hipótese EQ-1, 2 pontos poderiam cobrir até R$ 2 de uso elegível, desde que Mall/Travel aceitem os pontos sob seus próprios contratos. **Esse resgate não está aprovado.**

**Corrida de 4.900 pontos:** sob EQ-1, o Coletivo necessitaria de **R$ 4.900 de aquisição pré-paga**; sob EQ-2, **R$ 5.145**, dos quais R$ 245 corresponderiam à diferença de preço a classificar e justificar. Os valores são *simulações*, não preço praticado ou oferta comercial. A quantidade total de 4.900 permanece composta de 3.000 pontos para inscrições e 1.900 para classificação.

**Ponto de atenção:** a compra percentual gera poucos pontos quando comparada aos prêmios nominais (por exemplo, 2 versus 1.000). Antes de definir a paridade de resgate, verificar se prêmios como 1.000 pontos representam incentivo econômico intencionalmente alto. O organizador deve conhecer o **custo em reais da premiação antes de confirmá-la**, e a Guivos não deve subsidiar implicitamente a diferença.

### 28.4 Custeio, taxa e liquidação

- O preço de aquisição pré-paga e qualquer **taxa de administração da Guivos** devem ser apresentados em linhas distintas; sugerir `a = custo lastreado por ponto` e `tarifa = item separado` para melhor transparência, mas essa decomposição requer decisão contratual.
- O mesmo vale para compra de oportunidade: `R$ 200 - R$ 2 de pontos - taxa Guivos aplicável = repasse líquido` (outros descontos legalmente previstos devem ser discriminados).
- Em Mall/Travel, o ledger não transforma automaticamente valor de ponto em caixa do fornecedor; deve haver conciliação de crédito de pontos, baixa da obrigação, pedido/reserva e repasse ao parceiro.
- Valores de taxas, tributos, custo de adquirência, câmbio, cancelamentos e spreads de fornecedor afetam a sustentabilidade do cenário EQ-1 e precisam ser cobertos explicitamente por contrato — sem reduzir em segredo o direito prometido à Pessoa.
- Expiração, uso parcial, reembolso e insolvência requerem tratamento jurídico e contábil específico, incluindo destinação de recursos não utilizados.

### 28.5 Gate de decisão transversal

| Gate | Pergunta a adjudicar | Estado |
|---|---|---|
| PAR-01 | Confirmar norma da taxa de emissão do exemplo e tratamento de frações | Direção de produto definida, formalização pendente |
| FUND-01 | Fixar preço de aquisição de saldo pré-pago, confirmação e reserva | Pendente |
| PAR-02 | Fixar valor de uso/benefício por ponto, comunicação e validade | Pendente |
| LIQ-01 | Cobertura da liquidação no Mall e repasse a vendedor | Pendente |
| LIQ-02 | Cobertura da liquidação no Travel e repasse a fornecedor | Pendente |
| ECO-COVER | Demonstrar cobertura integral de pontos e custos, sem subsídio implícito | Pendente |

### 28.6 Parecer técnico para apreciação

**Recomendar como ponto de partida para deliberação** uma paridade econômica compreensível, com hipótese simétrica EQ-1 e **tarifas de serviço separadas**, sujeita a teste de sustentabilidade, legalidade e adequação ao posicionamento Guivos. **Não validar automaticamente EQ-1 como regra de resgate oficial.**

**Próximo exame:** simulação de fluxo de caixa/razão por origens — retenção de compras e aquisição de saldo — contra resgates efetivos, tarifas, estornos e saldos não utilizados; identificar responsabilidade pelo passivo em cada estado.

```text
VERSION → v1.9.0 CANDIDATE
FIN-COMPRA → R$200 AT 1% = 2 POINTS; R$198 BASE PAYOUT
FIN-EVENTO → ORGANIZER PREPAID POINT BALANCE
EQ-1..EQ-4 → HYPOTHETICAL ECONOMIC COMPARISON
ACQUISITION PRICE / REDEMPTION VALUE / FEES → NOT FORMALLY APPROVED
POINTS → SINGLE UNIT, OPTIONAL
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 29. Fluxo financeiro e reconciliação transversal — retenção, saldo pré-pago e resgate (v2.0.0 candidato)

**Natureza:** simulação documental e numérica de fluxos, sem instituição de conta de pagamento, custódia, regra contábil, preço oficial de ponto ou implementação. Cenário-base fictício **EQ-1: um ponto gera R$ 1,00 de abatimento elegível**, sem taxas nem tributos; NÃO é paridade aprovada.

### 29.1 Origens distintas; unidade de pontos única

**FIN-COMPRA:** compra intermediada por Guivos → benefício percentual → valor retido do repasse ao ofertante → obrigação de pontos da Pessoa, após critérios de liquidação. **FIN-EVENTO:** ofertante aporta antecipadamente recursos para adquirir pontos → saldo pré-pago do ofertante → reserva por campanha → distribuição após gatilho → obrigação de pontos da Pessoa. Após o crédito, o saldo da Pessoa mantém unidade comum, embora os lançamentos de origem continuem identificáveis para auditoria.

**Não confundir três responsabilidades:** (i) dinheiro do comprador devido ao ofertante; (ii) recursos retidos ou recebidos para cobertura de incentivos; (iii) obrigação potencial de liquidar uso dos pontos perante fornecedor no Mall/Travel. A cobrança da taxa Guivos ocorre **fora** do valor prometido como pontos.

### 29.2 Mini-razão hipotético, sem tributos nem taxa da plataforma

**Operação A — compra de curso.** Pessoa paga R$ 200,00; retorno opcional 1% = 2,00 pontos; R$ 2,00 retidos para cobertura; repasse-base R$ 198,00 ao ofertante. Identificar receita de taxa e demais repasses separadamente quando aprovados.

**Operação B — Coletivo pré-paga pontos de evento.** Coletivo adquire 4.900 pontos: custo **hipotético EQ-1** R$ 4.900,00; o sistema registra 4.900 pontos livres. Ao ativar corrida, compromete 3.000 para inscrições e 1.900 para pódio, sem novo débito do caixa — apenas transfere saldo livre para reserva. Pontos concedidos à Pessoa saem da reserva, sem nova emissão financeira sem lastro.

**Operação C — resgate.** A Pessoa utiliza hipoteticamente 1,25 ponto num pedido elegível do Mall com valor de cobertura de R$ 1,25; o sistema bloqueia 1,25 ponto e, após confirmação, baixa o saldo e reconhece obrigação de liquidação ao parceiro conforme contrato. A transferência ao parceiro deve conciliar o valor reconhecido e os ajustes cabíveis. No Travel, a lógica de ledger pode ser análoga, mas regras de disponibilidade, cotação, fornecedor, cancelamento e datas são específicas.

### 29.3 Razão ilustrativo por evento

| Evento | Caixa/repasse em R$ | Pontos do ofertante livres | Pontos ofertante reservados | Pontos disponíveis da Pessoa | Obrigação de resgate em R$ |
|---|---|---:|---:|---:|---:|
| A1: curso R$ 200 com 1% | R$ 200 recebidos; R$ 198 repasse-base; R$ 2 de cobertura | — | — | +2,00 | R$ 2,00, sob EQ-1 |
| B1: aquisição do Coletivo | R$ 4.900 aporte hipotético | +4.900 | 0 | 0 | Obrigação de saldo adquirido a classificar |
| B2: reserva da corrida | Sem novo pagamento | 0 | 4.900 | 0 | Reserva financiada, ainda não crédito à Pessoa |
| B3: entrega de 100 pontos | Sem novo pagamento | 0 | 4.800 | +100 | R$ 100,00, sob EQ-1 |
| C1: resgate Mall de 1,25 ponto | Pagamento ao parceiro só conforme liquidação contratual | — | — | -1,25 | -R$ 1,25 de obrigação da Pessoa, transferida/quitada conforme fluxo |
 
**Advertência:** linhas são movimentos independentes e ilustrativos; não se deve somar A1, B3 e C1 para inferir saldo de **uma** carteira pessoal sem declarar titularidade. A coluna de obrigação é uma exposição econômica sob hipótese EQ-1, **não lançamento contábil obrigatório**; natureza da obrigação de saldo do ofertante exige parecer próprio.

### 29.4 Exemplo de saldo de uma Pessoa, explícito

Pessoa X recebeu **2,00 pontos** do curso elegível e **100,00 pontos** da inscrição em corrida. Saldo total após concessões: **102,00 pontos**. Se utilizar **1,25 ponto** em resgate autorizado: saldo disponível **100,75 pontos**. Custo de utilização hipotético EQ-1: **R$ 1,25**; tarifas e obrigações de parceiro não incluídas.

### 29.5 Repasses e taxas sem mascarar custos

Para uma oportunidade simples sem outras retenções: `V=R$200; beneficio=V×1%=R$2; taxa_plataforma=T; repasse_liquido=R$198−T`. O valor de `T` e sua base não estão aprovados. O custo do benefício não pode aparecer também como taxa ou ser cobrado duas vezes do ofertante.

No FIN-EVENTO, o custo dos pontos pré-pagos e eventual tarifa de serviço devem aparecer separadamente: `pagamento_do_ofertante = lastro_dos_pontos + tarifa_explicita + demais_itens_legalmente_previstos`, segundo modelo contratual ainda não definido.

### 29.6 Estornos, reservas remanescentes e fluxo de caixa

| Ocorrência | Tratamento econômico candidato | Risco a resolver |
|---|---|---|
| Estorno integral de compra antes do crédito | Desfazer valor de incentivo pendente e acertar repasse | Chargeback, tarifas não reversíveis |
| Refund parcial após crédito | Recalcular benefício proporcional e ajustar saldo de modo auditável | Pontos já utilizados |
| Inscrição cancelada antes do direito ao bônus | Liberar reserva conforme regulamento publicado | Redistribuição não automática |
| Premiação de pódio pendente | Manter reserva até resultado confirmado ou encerramento contratual | Empates, recursos e fraude |
| Campanha encerrada com saldo não prometido | Liberar reserva para saldo livre do ofertante se regra permitir | Reembolso, expiração, destinação de caixa |
| Saldo pré-pago não utilizado | Conservar obrigação e status conforme prazo contratual | Custódia, insolvência, tributos e rescisão |
| Checkout Mall expirado | Reverter bloqueio de pontos não liquidados | Concorrência e consistência de pedido |
| Cancelamento Travel | Aplicar contrato do fornecedor e regra específica de restituição | Multas, variação tarifária e prazo de liquidação |

**Invariante:** reclassificar reserva em saldo livre não equivale automaticamente a **reembolsar dinheiro** ao ofertante. As devoluções em caixa dependem das condições contratuais e análise jurídica/contábil.

### 29.7 Reconciliações mínimas para operação futura

1. **Por compra e ofertante:** pagamento confirmado = repasse-base + incentivo retido, antes de taxa Guivos e demais ajustes identificados.
2. **Por orçamento de campanha:** pontos pré-pagos adquiridos + ajustes = pontos livres + reservados + distribuídos + outras baixas rastreáveis, sem contabilizar novamente pontos distribuídos como propriedade do ofertante.
3. **Por Pessoa:** saldo inicial + concessões - resgates ± estornos e ajustes = saldo final verificável.
4. **Por parceiro Mall/Travel:** pontos confirmados utilizados × regra de cobertura/cotação = obrigação liquidável ± descontos, taxas e estornos contratuais, com documentação do beneficiário do repasse.
5. **Por fonte de lastro:** origem da cobertura de pontos de compra ou evento identificada sem criar dois saldos incompatíveis para a Pessoa.
6. **Por estado financeiro:** não reconhecer como entrada de caixa a mera reserva nem contabilizar duas vezes a liquidação de um mesmo pagamento.

### 29.8 Riscos e gates ainda sem fechamento

- **PAR-02:** valor efetivo de utilização no Mall/Travel e proteção de direitos.
- **FUND-01:** preço e natureza do saldo de pontos pré-pago, cobertura, custódia e ressarcimento.
- **LIQ-01/LIQ-02:** obrigações e repasses a vendedores/fornecedores, com regras próprias de cancelamento e confirmação.
- **ROUND:** precisão monetária e política oficial de arredondamento.
- **LEGAL/FIN:** natureza jurídica dos pontos e saldos, retenção para terceiros, meios de pagamento, tributação, normas de consumo, tratamento contábil, insolvência e proteção de dados.
- **OPERAÇÃO:** relatórios de reconciliação, tolerância a divergências, idempotência e evidência auditável de pagamentos.

**Próxima etapa candidata:** matriz de reconciliação de passivos e recursos por estado, com testes de insuficiência de cobertura, estorno após resgate e múltiplos ofertantes/fornecedores. Sem promoção de maturidade institucional ou autorização de engenharia.

```text
VERSION → v2.0.0 CANDIDATE
FIN-COMPRA → POINT COST DEDUCTED FROM ISSUER PAYOUT
FIN-EVENTO → ORGANIZER PREPAID POINTS
EQ-1 → HYPOTHETICAL SETTLEMENT ONLY, NOT OFFICIAL
CASH / ISSUER BALANCES / PERSON POINTS / PARTNER SETTLEMENT → SEPARATED
PAR/FUND/LIQ → 0/5 FORMAL RATIFICATIONS
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 30. Matriz de cobertura financeira e conciliação de obrigações (v2.1.0 candidato)

**Natureza:** exame documental de risco financeiro e consistência de ledger, sem homologação, autorização de custódia, operação ou definição da taxa de resgate. Padrões definidos pelo fundador permanecem: FIN-COMPRA = deduzir custo dos pontos do repasse ao ofertante, taxa Guivos separada; FIN-EVENTO = organizador adquire saldo pré-pago de pontos.

### 30.1 Separação das exposições

| Camada | Origem | Obrigação | Controle mínimo |
|---|---|---|---|
| Recebível de compra | Pagamento da Pessoa por oportunidade | Repasse líquido ao ofertante e retenções discriminadas | Confirmação de liquidação, conciliação por transação |
| Cobertura FIN-COMPRA | Montante retido do repasse | Lastro dos pontos creditados | Não creditar sem montante sob controle e condição satisfeita |
| Cobertura FIN-EVENTO | Aquisição pré-paga de pontos pelo organizador | Saldo livre, reservado e transferido à Pessoa | Pagamento confirmado e reservas atômicas |
| Carteira da Pessoa | Créditos de ambas as origens | Disponibilidade para resgate elegível | Razão imutável/idempotente e conciliação de reversões |
| Liquidação Mall/Travel | Resgate aprovado de pontos | Obrigação perante parceiro/fornecedor | Cotação, confirmação, autorização e prova de repasse |

**Regra de solvência econômica a demonstrar:** em qualquer instante, a cobertura financeira efetivamente segregada ou juridicamente exigível deve ser suficiente para as obrigações assumidas, medidas pela política oficial de resgate e pelos custos contratuais. Não contar como disponível duas vezes uma reserva ou retenção.

### 30.2 Matriz de cenários de risco

| Cenário | Falha a impedir | Resposta candidata | Prova de reconciliação |
|---|---|---|---|
| RSK-01 — pagamento confirmado, repasse ainda indisponível | Crédito sem lastro | Crédito pendente até direito financeiro confirmado, ou garantia aprovada | Pagamento, retenção e crédito ligados a um identificador único |
| RSK-02 — chargeback após crédito | Perda de cobertura | Suspender nova exposição onde legítimo e executar política de ajuste/contestação | Reversão financeira e de pontos no ledger |
| RSK-03 — estorno após resgate no Mall | Saldo negativo oculto e perda não alocada | Registrar obrigação em disputa e mecanismo transparente de compensação | Trilha que conecta compra, resgate, vendedor e liquidação |
| RSK-04 — estorno após reserva Travel | Divergência entre pontos e condições da tarifa | Respeitar janela, multa e cancelamento do fornecedor, sem crédito automático | Cotação, contrato de viagem, estado da reserva e restituição |
| RSK-05 — aporte do organizador não liquidado | Reserva de pontos fictícia | Não disponibilizar saldo antes da confirmação de pagamento | Conciliação do pagamento com pontos adquiridos |
| RSK-06 — saldo insuficiente em campanha | Overdraft de pontos | Bloqueio atômico; permitir recarga ou reduzir campanha antes de ativar | Pontos livres nunca negativos |
| RSK-07 — duas campanhas pelo mesmo saldo | Dupla promessa econômica | Reserva serializável/idempotente por ofertante e campanha | Total reservado ≤ saldo comprovado |
| RSK-08 — múltiplos ofertantes no mesmo carrinho | Custos debitados do parceiro errado | Particionar por item, origem e ofertante; repasses independentes | Identificadores e totais conciliáveis por ofertante |
| RSK-09 — múltiplos fornecedores num resgate | Repasses cruzados e dupla baixa | Alocar valor/pontos por linha e fornecedor | Liquidação por item/fornecedor e reconciliação com pedido |
| RSK-10 — parceiro encerra atividades | Pontos não resgatáveis e obrigações sem responsável | Plano de continuidade ou substituição contratual legítima | Inventário de obrigações e lastro reservado |
| RSK-11 — pontos expirados ou não utilizados | Tratamento indevido de saldo e recursos | Aplicar política informada, sem apropriação automática | Classificação jurídico-contábil e histórico |
| RSK-12 — alteração de paridade | Obrigações maiores que lastro ou redução retroativa | Versionamento, simulação de exposição e proteção de direitos | Comparativo de passivo antes/depois e cobertura adicional |

### 30.3 Ensaios numéricos com paridade EQ-1 hipotética

**Caso A — curso, ponto e estorno posterior:** R$ 200 pagos, 1% = 2 pontos, custo R$ 2 retido e repasse-base R$ 198. Se 1 ponto for usado em resgate hipotético EQ-1 de R$ 1, e a compra for posteriormente estornada integralmente, não basta subtrair 2 pontos do saldo restante: existe pelo menos **R$ 1 de obrigação já liquidada ao parceiro**, que exige atribuição de risco, eventual recuperação e tratamento contratual. Sem a política, não se promete recuperação automática.

**Caso B — duas campanhas e saldo único:** ofertante adquiriu hipoteticamente 500 pontos pré-pagos; Campanha 1 reserva 350; Campanha 2 tenta reservar 200: **somente 150 pontos livres**; a segunda reserva não pode exceder o saldo. Se uma terceira tentativa concorrer pelo saldo, idempotência e bloqueio evitam duplicidade.

**Caso C — carrinho multi-ofertante:** Pessoa compra R$ 80 de A e R$ 120 de B, ambos com retorno opcional de 1%. Custo de pontos: **R$ 0,80 para A** e **R$ 1,20 para B**; repasses-base: **R$ 79,20** e **R$ 118,80**, respectivamente, antes das taxas e demais ajustes. Crédito agregado: 2,00 pontos, com lastro de fontes separado.

**Caso D — múltiplos fornecedores:** Pessoa usa hipoteticamente 3 pontos no Mall, sendo 1 para produto do vendedor X e 2 para produto do vendedor Y. Sob EQ-1, obrigação ilustrativa de R$ 1 a X e R$ 2 a Y; cada repasse requer confirmação própria e não se liquidam R$ 3 apenas ao primeiro vendedor.

### 30.4 Identificadores e relatórios necessários, sem instituir registro oficial

**Vínculos mínimos candidatos:** `purchase_id`, `issuer_id`, `purchase_line_id`, `payment_settlement_id`, `campaign_id`, `prepaid_funding_id`, `points_ledger_entry_id`, `person_account_id`, `redemption_id`, `partner_id`, `payout_id`, `reversal_id`, com políticas de proteção de dados e segregação de acessos.

**Relatórios futuros:** compromisso por ofertante, conciliação de retenções versus pontos de compra, posição de pontos pré-pagos por campanha, saldos por Pessoa sem exposição indevida, valores pendentes de parceiros, estornos e disputas, e razão de ajuste de cobertura. Estes são nomes conceituais, não contratos técnicos publicados.

### 30.5 Portas de decisão e impedimentos

- **COVER-01:** aprovar método de mensuração da obrigação e suficiência de lastro em função de PAR-02, custos e direitos.
- **COVER-02:** atribuir responsabilidade financeira por chargeback após resgate e por insolvência de ofertantes/parceiros.
- **COVER-03:** formalizar reconciliação multi-ofertante/multi-fornecedor e identidade de lançamentos.
- **COVER-04:** definir política de saldos não utilizados, reembolsos e expiração.
- **COVER-05:** homologar procedimentos de incidentes, disputa, correção contábil e auditoria.

**Nenhum COVER aprovado.** O exame econômico exige parecer jurídico, fiscal e contábil e testes de engenharia autorizados; o presente documento não pressupõe que Guivos possui permissões operacionais para guardar recursos de terceiros ou operar carteira regulada.

**Próxima etapa candidata:** pacote de decisão de cobertura financeira e risco residual, rastreando cada caso RSK-01..12 até responsável, prova, tratamento contratual e teste, com foco no risco de estornos após resgate.

```text
VERSION → v2.1.0 CANDIDATE
FIN-COMPRA / FIN-EVENTO → DIRECTIONS PRESERVED
RISK CASES → 12 DOCUMENTED; FORMAL HOMOLOGATION NONE
COVER-01..05 → 0/5 ADJUDICATED
EQ-1 → ILLUSTRATIVE ONLY
PAR/FUND/LIQ → FORMAL RATIFICATIONS PENDING
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 31. Pacote decisório de riscos residuais — responsabilidade e evidência (v2.2.0 candidato)

**Natureza:** matriz documental, sem aprovação contratual ou operacional. FIN-COMPRA retém custo dos pontos do repasse ao ofertante; FIN-EVENTO exige saldo pré-pago. O ofertante financia o incentivo, mas chargebacks, fraudes e perdas após resgate requerem **atribuição específica de responsabilidade**, não presumida.

### Matriz de 12 cenários

| Risco | Responsável funcional proposto (não autoridade formal) | Evidência | Tratamento contratual pendente | Teste de aceite futuro |
|---|---|---|---|---|
| RSK-01 repasse indisponível | Financeiro/Payments | Pagamento, liquidação, retenção | Crédito após cobertura real | Impedir crédito sem lastro |
| RSK-02 chargeback após crédito | Risco/Payments + ofertante | Contestação, crédito, saldo | Recuperação e contestação | Reversão rastreável |
| RSK-03 refund após Mall | Risco + Mall + vendedor | Compra origem, emissão, resgate, repasse | Alocação de perda após resgate | Não criar débito negativo oculto |
| RSK-04 refund após Travel | Risco + Travel + fornecedor | Cotação, reserva, multas, liquidação | Multas, cancelamentos e ressarcimentos | Estágios distintos de cancelamento |
| RSK-05 saldo pré-pago pendente | Payments + campanhas | Pagamento e aporte | Ativação só após confirmação | Aporte não confirmado não cria pontos |
| RSK-06 saldo de campanha insuficiente | Ledger + organizador | Disponível, reservas, configuração | Vedação de novas promessas | Reserva superior ao saldo falha |
| RSK-07 campanhas concorrentes | Ledger + organizador | Operações atômicas e idempotência | Prioridade e rollback | Uma reserva pelo último saldo |
| RSK-08 múltiplos ofertantes | Payments + ofertantes | Itens, IDs, splits e refund | Repasses e taxas separados | Refund parcial de um ofertante |
| RSK-09 múltiplos fornecedores | Mall/Travel + ledger | Itens, parceiros e liquidações | Split e reversão por fornecedor | Não cruzar repasses |
| RSK-10 parceiro encerra operação | Jurídico/Risco + parceiro | Contratos e obrigações abertas | Continuidade e garantia | Parceiro indisponível |
| RSK-11 saldo expirado/não usado | Jurídico/Financeiro | Prazo, comunicação e saldo | Direitos, reembolso e destino do lastro | Prazo-limite e contestação |
| RSK-12 alteração de paridade | Governança econômica | Versionamento e exposição | Preservar direitos e cobertura | Comparar obrigações antes/depois |

### Foco RSK-03 — estorno após resgate

Curso de R$ 200, retorno 1% → **2 pontos**, R$ 2 retidos do repasse e repasse-base de R$ 198 (taxa Guivos separada). Pessoa utiliza **1,25 ponto** no Mall. Na hipótese **EQ-1 não aprovada**, o parceiro tem cobertura teórica de R$ 1,25. Depois ocorre estorno integral da compra do curso.

Separar: (a) os **0,75 ponto** ainda não resgatados e potencialmente reversíveis, sujeitos à política; (b) os **1,25 ponto** já consumidos e obrigação com parceiro; (c) a reversão financeira de origem e a necessidade de atribuir a perda **sem presumir automaticamente responsabilidade de Guivos, ofertante ou Pessoa**.

**Procedimento candidato:** detectar incidente; vincular pagamento, crédito, pedido e liquidação; verificar contestação; medir exposição; notificar partes; adjudicar responsável sob contrato e lei; compensar/reverter com lançamentos identificáveis; reconciliar parceria e encerrar auditavelmente. Proibido débito oculto, saldo negativo silencioso ou cancelamento unilateral de repasse devido.

**Alternativas de responsabilidade para decisão:** recuperação proporcional e juridicamente permitida com contestação; garantia contratual de chargeback do ofertante; responsabilidade por fraude/falha comprovada do agente competente; atraso de disponibilidade ou limites para reduzir risco. Nenhuma selecionada.

### Gates de cobertura a ratificar

| Gate | Evidência exigida | Estado |
|---|---|---|
| COVER-01 | Obrigação mensurada sob paridade aprovada e lastro suficiente | ABERTO |
| COVER-02 | Contratos e parecer jurídico de chargeback, insolvência e responsabilização | ABERTO |
| COVER-03 | Split e conciliação por ofertante, parceiro e linha de pedido | ABERTO |
| COVER-04 | Tratamento de expiração, saldos livres, reembolso e destinação de recursos | ABERTO |
| COVER-05 | Trilha de incidentes, controles, testes e auditoria | ABERTO |

**Rito seguinte:** especificação candidata do ledger financeiro e de pontos e matriz de aceite ponta a ponta, sem implantar APIs nem adjudicar competências. Requisitos jurídico, fiscal, contábil, privacidade e meios de pagamento permanecem gates independentes.

```text
VERSION → v2.2.0 CANDIDATE
RSK-01..12 → 12 DOCUMENTED; NO LIVE TESTS
COVER-01..05 → 0/5 ADJUDICATED
PARITY EQ-1 → SIMULATION ONLY
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 32. Contrato mínimo de ledger e matriz de aceite ponta a ponta (v2.3.0 candidato)

**Natureza:** especificação lógica candidata, sem definição de tecnologia de custódia, API operacional, registro oficial de transições, aprovação institucional ou autorização de implementação. FIN-COMPRA e FIN-EVENTO são origens financeiras distintas, mas entregam **uma unidade de pontos** à Pessoa.

### 32.1 Razões e separação de responsabilidades

| Razão lógico | Responsabilidade | Não confundir com |
|---|---|---|
| `purchase_settlement_ledger` | Compra, pagamento elegível, retenção dos pontos, taxa Guivos e repasse por ofertante | Carteira de pontos |
| `prepaid_funding_ledger` | Aquisição antecipada, saldo livre e reservas de campanha por Organização/Coletivo | Receita automática da Guivos |
| `person_points_ledger` | Créditos, reservas, resgates, ajustes e saldo verificável da Pessoa | Dinheiro disponível ou conta bancária |
| `partner_settlement_ledger` | Obrigações de resgates confirmados e repasses a vendedor/fornecedor | Cobrança original da oportunidade |
| `reconciliation_audit_log` | Vínculos, evidências e divergências entre razões | Fonte de autoridade jurídica ou prova artificial de liquidação |

### 32.2 Eventos candidatos e estados

```text
FIN-COMPRA
purchase_created → payment_pending → payment_confirmed
→ settlement_eligible → points_withholding_recorded
→ issuer_payout_reconciled → person_points_credited
↘ refund_requested / refund_confirmed / chargeback_opened
→ adjustment_reviewed → financial_and_points_adjustment_reconciled

FIN-EVENTO
funding_requested → payment_pending → funding_confirmed
→ organizer_points_available → campaign_reserve_confirmed
→ participation_or_ranking_verified → person_points_credited
↘ cancellation_or_dispute → reserve_adjusted_or_released

RESGATE
redemption_quoted → points_reserved → partner_order_confirmed
→ points_redeemed → partner_settlement_pending → partner_settled
↘ quote_expired / cancelled / partially_refunded → points_and_cash_reconciled
```

Esses nomes são **vocabulário de estudo**, não IDs canônicos GKR-TRN nem implementação de máquina de estados. Transições financeiras dependem de eventos verificados; callback externo isolado não comprova liquidação sem reconciliação.

### 32.3 Contrato lógico de lançamento

Campos mínimos candidatos: `entry_id`, `source_type` (compra/evento/resgate/ajuste), `source_id`, `issuer_id`, `person_id` quando aplicável, `partner_id`, `campaign_id`, `asset` (BRL/pontos), `amount` decimal exato, `entry_type`, `event_time`, `effective_time`, `policy_version`, `idempotency_key`, `correlation_id`, `status`, `evidence_ref`, `reversal_of_entry_id`.

- Todo lançamento possui **origem rastreável**; reversão é novo lançamento vinculado, sem apagar histórico.
- Saldos são derivados do ledger e de reservas confirmadas; não confiar em contador mutável isolado.
- Cada chave de idempotência produz no máximo um efeito econômico por operação e escopo.
- Controle de concorrência impede dois créditos/compromissos para a mesma cota ou utilização duplicada de saldo.
- Identificadores de Pessoas e evidências devem respeitar LGPD, minimização e segregação de acesso.

### 32.4 Invariantes econômicas testáveis

1. **Compra:** `valor elegível = repasse-base ao ofertante + retenção para pontos` antes de taxa Guivos e outros ajustes explicitamente discriminados; R$ 200 × 1% → 2 pontos, R$ 2 retidos, repasse-base R$ 198.
2. **Campanha:** `pontos adquiridos + ajustes = livres + reservados + distribuídos + baixas justificadas`; não reaproveitar os pontos distribuídos como saldo do ofertante.
3. **Pessoa:** `saldo inicial + concessões − resgates ± ajustes = saldo final`; pontos reservados para checkout não podem ser gastos simultaneamente.
4. **Parceiro:** cada resgate confirmado vincula a obrigação de liquidação ao parceiro correto e não gera repasse duplicado.
5. **Cobertura:** em paridade e condições **ainda não aprovadas**, qualquer compromisso real deverá ter lastro suficiente, inclusive custos e riscos contratuais.
6. **Cancelamento:** refund da compra pode rever elegibilidade sem apagar pagamento original ou liquidação ocorrida.
7. **Unidade:** pontos de compra e de evento são fungíveis para a Pessoa sob política única; origem financeira continua segregável para auditoria.
8. **Separação funcional:** ausência de saldo pré-pago bloqueia recompensa de evento, não impede automaticamente inscrições legítimas.

### 32.5 Matriz de testes ponta a ponta proposta

| ID | Cenário | Critério de aceite | Situação |
|---|---|---|---|
| E2E-01 | Curso R$ 200, 1% | 2 pontos; custo R$ 2; repasse-base R$ 198; taxa Guivos separada | NÃO EXECUTADO |
| E2E-02 | Compra com pontos fracionários | Precisão e retenção compatíveis com ROUND aprovado | NÃO EXECUTADO |
| E2E-03 | Carrinho com dois ofertantes | Retenção e repasse individual sem cruzamento | NÃO EXECUTADO |
| E2E-04 | Retry/duplicidade de confirmação | Um só crédito, retenção e repasse | NÃO EXECUTADO |
| E2E-05 | Estorno parcial pré-resgate | Ajuste proporcional auditável | NÃO EXECUTADO |
| E2E-06 | Estorno integral pós-resgate | Exposição e responsável identificados; nenhum débito oculto | NÃO EXECUTADO |
| E2E-07 | Compra de saldo para evento | Pontos só disponíveis após pagamento confirmado | NÃO EXECUTADO |
| E2E-08 | Corrida 30 × 100 + pódio 1.000/600/300 | Reservar 4.900 pontos, sem impedir 31ª inscrição | NÃO EXECUTADO |
| E2E-09 | Última cota com duas inscrições simultâneas | Cota atribuída uma vez e ordem verificável | NÃO EXECUTADO |
| E2E-10 | Saldo insuficiente em campanhas paralelas | Nova reserva negada sem prejudicar compromissos anteriores | NÃO EXECUTADO |
| E2E-11 | Vencedor com bônus de inscrição | Acúmulo apenas quando regulamento permite, sem crédito duplicado | NÃO EXECUTADO |
| E2E-12 | Pedido Mall com dois vendedores | Liquidação e estorno alocados por vendedor | NÃO EXECUTADO |
| E2E-13 | Reserva Travel cancelada | Multa, reversão de pontos e parceiro conforme contrato | NÃO EXECUTADO |
| E2E-14 | Checkout expirado | Reserva liberada sem crédito/resgate duplicado | NÃO EXECUTADO |
| E2E-15 | Alteração de paridade/validade | Direitos adquiridos e cobertura preservados por versão | NÃO EXECUTADO |
| E2E-16 | Organizador encerra campanha | Saldos livres/reservados tratados sem reembolso em caixa presumido | NÃO EXECUTADO |

### 32.6 Gates de passagem

O artefato só se torna contrato implementável após ratificação de `PAR-02`, `FUND-01`, `LIQ-01/02`, ROUND, COVER e responsabilidades jurídico-fiscais-contábeis; testes E2E exigem ambiente e implementação autorizados. Nenhum dos 16 testes foi executado nesta etapa. Não há publicação de preço oficial de ponto nem autorização de custódia de recursos.

**Próximo passo candidato:** mapa de dependências entre os 16 E2E, gates e evidências, identificando o conjunto mínimo seguro de validação de FIN-COMPRA e FIN-EVENTO antes de ativar resgates Mall/Travel.

```text
VERSION → v2.3.0 CANDIDATE
LEDGER LOGICAL DOMAINS → 5 DRAFTED
E2E CASES → 16 DEFINED / 0 EXECUTED
FIN-COMPRA → PAYOUT WITHHOLDING
FIN-EVENTO → PREPAID BALANCE
PR #655 → OPEN / DRAFT
MAIN / MENU / HOME MASTERS / REGISTRIES / REPLIT → UNCHANGED
```

## 33. Mapa de dependências E2E e validação incremental por fluxo (v2.4.0 candidato)

**Estado:** análise de dependências e critérios de entrada/saída, sem execução dos 16 testes, sem adjudicação de gates econômicos e sem autorização de engenharia. Esta seção não altera a premissa de FIN-COMPRA (retenção no repasse ao ofertante) nem de FIN-EVENTO (saldo de pontos pré-pago). A unidade de pontos da Pessoa é comum às duas origens.

### 33.1 Sequenciamento por domínio

| Etapa | Escopo | Testes E2E relevantes | Dependências formais | Saída verificável |
|---|---|---|---|---|
| V0 — Definição de política | Base elegível, emissão, precisão, estorno, lastro, identidade e segurança | Precondição de todos | PAR-01, ROUND-01..06, FUND-01, COVER-01..05 e análises legais pertinentes | Regras aprovadas, versionadas e rastreáveis |
| V1 — FIN-COMPRA isolado | Compra, dedução no repasse, crédito, refund, multi-ofertante e idempotência | E2E-01,02,03,04,05,06 | V0; processador de pagamento/repasse integrado e contratualizado | Pagamentos, retenções, pontos e estornos conciliados por ofertante |
| V2 — FIN-EVENTO isolado | Aquisição de saldo, reserva, cotas, premiação e campanha | E2E-07,08,09,10,11,16 | V0; pagamento pré-pago confirmado e atribuição de competência ao organizador | Saldo não negativo, reservas atômicas e créditos com evidência |
| V3 — Resgate Mall isolado | Pedido, múltiplos vendedores, bloqueio e estorno | E2E-12,14,15; cruzamento com E2E-06 | V1 ou V2 validado, PAR-02, LIQ-01, cobertura contratual e testes de segurança | Liquidação por vendedor reconciliada |
| V4 — Resgate Travel isolado | Cotação, reserva, cancelamento e fornecedor | E2E-13,14,15; cruzamento com E2E-06 | V1 ou V2 validado, PAR-02, LIQ-02, contrato do fornecedor | Pontos e valor de liquidação conciliados segundo reserva |
| V5 — Transversal | Duas fontes financiadoras + saldo único da Pessoa + múltiplos produtos | Reexecução encadeada E2E-01..16 com identidades e saldos controlados | V1/V2/V3/V4 validados e políticas compatíveis | Ausência de dupla emissão, repasse cruzado ou resgate além da cobertura |

**Distinção:** validação de FIN-COMPRA ou FIN-EVENTO isolados não autoriza automaticamente aceitar pontos como pagamento no Mall ou Travel. Homologação funcional também não equivale a autorização regulatória, contábil ou institucional.

### 33.2 Conjunto mínimo de aceite para FIN-COMPRA

**Casos de entrada:** E2E-01 (curso de R$ 200 → 2 pontos, R$ 198 de repasse-base), E2E-02 (frações com política efetiva), E2E-03 (dois ofertantes), E2E-04 (retry/idempotência), E2E-05 (refund parcial), E2E-06 (refund após resgate em cenário integrado; como teste de risco, requer ambiente de resgate habilitado).

**Mínimo para validar núcleo sem resgate:** E2E-01..05, mais prova de **não crédito sem liquidação** e tratamento de chargeback pendente; E2E-06 continua **bloqueador para liberar resgate** e não pode ser silenciosamente dispensado. Matriz de autorização precisa distinguir teste do núcleo de liberação de uso comercial.

**Evidência:** transação confirmada, base elegível, percentual escolhido, custo retido, taxa Guivos discriminada, repasse por ofertante, lançamento da Pessoa, reversões e razão de conciliação. Sem contratos e recursos legalmente adequados, a execução não pode ser classificada como homologação.

### 33.3 Conjunto mínimo de aceite para FIN-EVENTO

**Casos centrais:** E2E-07 (aquisição pré-paga confirmada), 08 (4.900 pontos, duas classes de incentivo e 31ª inscrição permitida), 09 (última cota concorrente), 10 (saldo insuficiente), 11 (acúmulo apenas conforme regulamento), 16 (encerramento de campanha sem reembolso automático).

**Condições adicionais:** inscrição não implica presença validada; resultado contestado suspende prêmio segundo política; nenhuma promessa ultrapassa o saldo livre; cancelamento redistribui cota apenas sob regulamento expresso. O núcleo de campanha poderá ser tecnicamente validado antes de integrar resgate em produtos, mas **não** operacionalizado sem gates de financiamento e proteção.

### 33.4 Dependências exclusivas de Mall e Travel

- **Mall:** LIQ-01, política de valor efetivo de pontos PAR-02, custo e preço do item, split de vários vendedores, confirmação de entrega/compra, devolução e baixas.
- **Travel:** LIQ-02, PAR-02, disponibilidade e janela de cotação, penalidades, moeda, fornecedor, cancelamento e reembolso.
- **Compartilhados:** carteira da Pessoa, reservas idempotentes, precisão ROUND aprovada, prova de lastro, conciliação da obrigação financeira e proteção de direitos.
- **Regra de não contágio:** falha em Travel não autoriza debitar resgate Mall ou desconsiderar crédito elegível de origem; cada produto precisa de confirmação e resolução própria.

### 33.5 Critérios de classificação de maturidade

| Classificação | Significado | Neste registro |
|---|---|---|
| DOCUMENTED | Caso e dependência descritos | SIM |
| POLICY_APPROVED | Gate materialmente decidido por autoridade competente | NÃO comprovado para os itens pendentes |
| TEST_READY | Ambiente, oráculos, dados, responsáveis, contratos e política preparados | NÃO |
| EXECUTED | Evidências de execução reproduzíveis | 0/16 |
| VALIDATED | Execução, reconciliação e revisão humana concluídas | 0/16 |
| LIVE_AUTHORIZED | Implantação e operação expressamente autorizadas | NÃO |

### 33.6 Bloqueadores explícitos e próximo passo

**Bloqueadores:** ROUND, paridade de uso PAR-02, preço do saldo pré-pago FUND-01, cobertura COVER, processamento de pagamentos, responsabilidades por fraude/chargeback e contratos LIQ-01/02. Não criar IDs canônicos, compromissos reais, saldos operacionais, páginas públicas nem promessas de pontos antes do rito competente.

**Próxima etapa candidata:** consolidar decisões de produto já expressas em um resumo executivo dos dois modelos e produzir um pacote de perguntas econômicas **somente das pendências reais**, evitando a repetição de alternativas já encerradas pelo fundador.

```text
VERSION → v2.4.0 CANDIDATE
E2E TESTS → 16/16 MAPPED; 0/16 EXECUTED
FIN-COMPRA CORE → E2E-01..05 (E2E-06 INTEGRATED BLOCKER)
FIN-EVENTO CORE → E2E-07..11,16
MALL → E2E-12,14,15 + INTEGRATED RISK
TRAVEL → E2E-13,14,15 + INTEGRATED RISK
LIVE AUTHORIZATION → NONE
PR #655 → OPEN / DRAFT
MAIN / MENU / MASTERS / REGISTRIES / REPLIT → UNCHANGED
```
