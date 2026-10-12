---
id: GEM-OPPORTUNITIES-POINTS-REWARDS-CANDIDATE-001
title: Oportunidades — Retorno em Pontos e Premiações de Eventos — Proposta Transversal
status: draft
version: 0.4.0
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
