---
id: GEM-OPPORTUNITIES-POINTS-REWARDS-CANDIDATE-001
title: Oportunidades — Retorno em Pontos e Premiações de Eventos — Proposta Transversal
status: draft
version: 0.1.0
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
