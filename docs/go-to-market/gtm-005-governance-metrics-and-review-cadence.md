---
id: GTM-005
title: Governança, Métricas e Cadência do Go-to-Market
status: draft
version: 0.2.0
owner: Guivos Strategy & Growth
last_updated: 2026-08-08
parent: GTM-000
related:
  - GTM-001
  - GTM-002
  - GTM-003
  - GTM-004
  - GEM-006
  - GEM-009
  - GEM-010
normative: false
---

# Governança, Métricas e Cadência do Go-to-Market

## 1. Finalidade

Definir como as metas do domínio GTM serão operadas, comparadas com resultados reais, recalibradas e apresentadas internamente ou a investidores.

## 2. Quatro classes obrigatórias de número

Todo número deve carregar uma destas leituras:

| Classe | Significado |
|---|---|
| `realized` | realizado e suportado por dado verificável |
| `approved_target` | meta formalmente aprovada para gestão |
| `candidate_target` | meta candidata usada para planejamento e teste |
| `scenario` | hipótese/sensibilidade sem compromisso operacional |

É proibido apresentar `candidate_target` ou `scenario` como `realized`.

## 3. Estado inicial dos documentos GTM

Na criação desta baseline:

- geografia BH/SP/Portugal: direção estratégica histórica, com execução ainda pendente;
- 1 milhão de usuários em M60: `candidate_target` derivado de direção histórica;
- metas de pagantes, vendas, captação e Parcerias Estratégicas: `candidate_target`;
- faturamento anual: `scenario/base planning target`;
- valuation R$ 10–15 milhões: `candidate negotiation anchor` derivado de faixa histórica;
- R$ 12 milhões pre-money: `scenario/base anchor`;
- aporte de R$ 2 milhões: `scenario`;
- valuation futuro e MOIC: `scenario`, nunca guidance ou retorno prometido.

## 4. Separação obrigatória de métricas

Os seguintes objetos devem possuir KPIs independentes:

```text
Organização ativa
≠ oportunidade ativa
≠ contrato Guivos Business
≠ Parceiro Estratégico ativo
```

- `Organização ativa` mede participante institucional ativo no ecossistema;
- `oportunidade ativa` mede oferta disponível às Pessoas/Coletivos sob autoridade aplicável;
- `contrato Guivos Business` mede contratação do produto especializado;
- `Parceiro Estratégico ativo` mede contraparte única com relação estratégica qualificada conforme `GTM-002`.

Se a mesma pessoa jurídica exercer mais de um papel, cada métrica registra somente o objeto que lhe corresponde. Nenhuma oportunidade deve ser duplicada em métricas de parceria.

## 5. Scorecard executivo

### Crescimento e produto

- Pessoas cadastradas;
- ativação;
- MAU/WAU conforme produto;
- retenção por coorte;
- conversão Free → Plus/Pro;
- churn e reativação.

### Ecossistema e oferta

- Coletivos ativos e pagantes;
- Organizações ativas e pagantes;
- oportunidades/ofertas úteis ativas;
- oportunidades por Organização/Coletivo conforme autoridade aplicável;
- densidade de oferta por praça;
- utilização e qualidade da oferta;
- concentração de oferta por Organização ou Coletivo quando relevante.

### Parcerias Estratégicas

- contrapartes estratégicas em prospecção;
- teses bilaterais qualificadas;
- Parceiros Estratégicos ativos;
- parceiros ativos por categoria e território;
- contribuição para distribuição/aquisição;
- contribuição para tecnologia/integração;
- contribuição para acesso institucional/territorial;
- entregáveis e resultados por aliança;
- dependência e concentração por parceiro estratégico;
- alianças suspensas, encerradas ou em revisão.

A quantidade de Parceiros Estratégicos nunca deve ser usada como proxy de quantidade de oportunidades disponíveis na Journey.

### Comercial

- pipeline por estágio;
- valor ponderado e não ponderado;
- ciclo médio de venda;
- propostas;
- win rate;
- contratos Business;
- expansão, downgrade, cancelamento e renovação.

### Econômico-financeiro

- MRR/ARR elegível;
- faturamento;
- receita reconhecida quando contabilmente disponível;
- caixa recebido;
- margem de contribuição;
- CAC;
- payback;
- LTV somente quando metodologicamente defensável;
- burn e runway;
- concentração de receita;
- inadimplência, estornos e perdas.

### Experiência e propósito

- satisfação/qualidade;
- incidentes e suporte;
- evidência de valor entregue;
- acesso gratuito preservado;
- denúncias ou sinais de incentivo adverso;
- risco de monetização desalinhada ao propósito.

## 6. Cadência

### Semanal — operação

Responsáveis de Growth, Comercial, Ecossistema, Parcerias Estratégicas e Operações revisam:

- pipeline comercial;
- aquisição;
- oferta disponível;
- pipeline de alianças estratégicas;
- bloqueios;
- capacidade;
- ações dos próximos sete dias.

### Mensal — performance

Revisão executiva de:

- meta × realizado;
- variações versus baseline;
- receita e caixa;
- conversões;
- churn;
- qualidade das coortes;
- densidade e qualidade da oferta;
- resultados das Parcerias Estratégicas;
- produtividade de canais e equipe;
- necessidade de correção.

### Trimestral — estratégia

- manter, acelerar ou reduzir investimento por canal;
- revisar metas anuais;
- reavaliar praça e expansão;
- recalibrar ICP e oferta;
- revisar carteira e concentração de Parcerias Estratégicas;
- revisar valuation apenas se houver evidência material;
- revisar necessidade de capital e runway.

### Anual — baseline

GTM-001 a GTM-005 deverão receber uma versão anual reconciliada entre:

```text
planejado
→ realizado
→ desvio
→ causa
→ aprendizado
→ nova premissa
→ nova meta aprovada
```

## 7. Gates executivos

### Gate A — lançamento BH

Exige oferta mínima, responsáveis, instrumentação, suporte, segurança operacional e primeiras capacidades estratégicas necessárias ao lançamento.

### Gate B — aceleração SP

Exige aprendizado demonstrável de BH e capacidade para operar duas praças sem degradação.

### Gate C — escala nacional

Exige retenção, economics, oferta e modelo comercial replicável, além de canais ou alianças suficientes para expansão eficiente.

### Gate D — Portugal

Exige PMF operacional mínimo, capacidade internacional, jurídico/fiscal/privacidade/pagamentos avaliados, rede de oferta local, alianças de entrada territorial quando necessárias e budget aprovado.

### Gate E — rodada institucional

Exige data room, cap table, tese de uso de recursos, métricas verificáveis e distinção clara entre realizado e projetado.

## 8. Regras para apresentações a investidores

Todo pitch ou data room que utilizar números deste domínio deve indicar:

- data-base;
- moeda;
- se é realizado, meta ou cenário;
- fonte do preço/driver;
- exclusões relevantes;
- definição operacional de Organização, oportunidade, Business e Parceiro Estratégico;
- premissas de diluição quando mostrar participação;
- que retornos são sensibilidades, não promessas.

É proibido:

- apresentar ARR projetado como contratado;
- apresentar pipeline como receita;
- apresentar cadastro como usuário ativo;
- somar Organizações e Parceiros Estratégicos como se fossem a mesma base de oferta;
- apresentar número de parceiros estratégicos como número de oportunidades;
- apresentar valuation interno como oferta recebida;
- apresentar MOIC matemático como rentabilidade esperada;
- omitir diluição quando ela for material ao exemplo.

## 9. Ownership proposto

| Dimensão | Owner funcional |
|---|---|
| lançamento e território | Strategy/GTM |
| aquisição de Pessoas | Growth |
| Coletivos e oferta comunitária | Ecosystem |
| Organizações e oferta institucional | Sales/Ecosystem |
| Guivos Business | Sales/Business |
| Parcerias Estratégicas | Strategy/Partnerships |
| receita e caixa | Finance/Economic Model |
| valuation e fundraising | Founder/Strategy/Finance |
| dados e scorecards | Intelligence/Data |
| capacidade e qualidade | Operations/Product |

Owners são responsabilidades funcionais, não cargos ou contratações automaticamente aprovadas.

## 10. Relação com GEM-006 e GEM-010

`GEM-006` permanece autoridade para papéis, relacionamento, elegibilidade, valor bilateral, riscos e lifecycle de parceiros.

O GTM apenas define quando uma relação é contabilizada na meta comercial/estratégica de Parceiros Estratégicos e como ela entra no scorecard.

O GTM fornece metas e hipóteses aprováveis; o GEM-010 permanece responsável por transformar parâmetros em cenários financeiros coerentes e separar receita, margem, caixa, capital e funding.

O GTM não substitui demonstrações financeiras, contabilidade, planejamento orçamentário ou modelagem financeira detalhada.

## 11. Estado

`draft — governance framework ready for executive calibration; no candidate target is automatically approved by publication`.