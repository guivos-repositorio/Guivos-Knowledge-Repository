---
id: GEM-OPPORTUNITIES-POINTS-REWARDS-CANDIDATE-001
title: Oportunidades — Retorno em Pontos e Premiações de Eventos — Proposta Transversal
status: draft
version: 1.2.0
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
