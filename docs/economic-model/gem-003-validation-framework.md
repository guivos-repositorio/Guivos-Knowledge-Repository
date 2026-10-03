---
id: GEM-003-VALIDATION-FRAMEWORK-001
title: Framework de Validação de Famílias de Receita
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-003
---

# Framework de Validação de Famílias de Receita

## 1. Objetivo

Definir hipóteses, evidências e critérios necessários antes que uma família ou mecanismo de receita possa avançar para teste controlado.

## 2. Princípio

A intenção declarada de pagar não comprova comportamento, operação, confiança ou sustentabilidade.

Validação deverá combinar, conforme o risco:

- compreensão da oferta;
- uso real ou comportamento observável;
- evidência de valor;
- disposição real a pagar;
- capacidade operacional;
- custos e riscos;
- proteção de dados;
- confiança;
- reversibilidade;
- análise especializada.

## 3. Dimensões de validação

### V-01 — Valor

O pagador compreende a contraprestação e reconhece benefício identificável?

### V-02 — Comportamento

Existem sinais de aquisição, utilização, continuidade, renovação ou recomendação legítima?

### V-03 — Pagamento

Existe disposição real a pagar em condição compreensível, e não apenas resposta hipotética?

### V-04 — Operação

A Guivos e os atores envolvidos conseguem entregar, suportar, corrigir e encerrar o mecanismo?

### V-05 — Qualidade

A monetização preserva o resultado esperado e os critérios mínimos de qualidade?

### V-06 — Confiança

A relação comercial é entendida como legítima, transparente e compatível com a proposta Guivos?

### V-07 — Economia

Custos, repasses, perdas, suporte, risco e obrigações podem ser medidos?

### V-08 — Gratuito

O mecanismo fortalece ou reduz artificialmente o valor universal?

### V-09 — Conflito

A receita altera recomendação, ordenação, evidência, acesso ou autoridade?

### V-10 — Reversibilidade

Cancelamento, disputa, restituição, correção e suspensão são viáveis?

### V-11 — Dados

A finalidade, minimização, acesso, retenção e proteção são adequados?

### V-12 — Dependências especializadas

Questões jurídicas, fiscais, contábeis, regulatórias e contratuais foram identificadas?

## 4. Estados

- `not_started`;
- `hypothesis_defined`;
- `research_planned`;
- `evidence_insufficient`;
- `passed_conceptually`;
- `passed_for_controlled_test`;
- `passed_with_conditions`;
- `blocked`;
- `rejected`;
- `suspended`.

Somente aprovação separada poderá atribuir `passed_for_controlled_test`.

## 5. Registro mínimo de hipótese

```yaml
hypothesis_id: string
revenue_family_id: string
segment: string
payer: string
beneficiary: string
value_proposition: string
candidate_charge_basis: string
price_defined: false
expected_behavior: string
risk_level: low | moderate | high | critical
evidence_required:
  - string
success_criteria:
  - string
failure_criteria:
  - string
stop_conditions:
  - string
owner: unassigned
status: hypothesis_defined
```

## 6. Métodos futuros admissíveis

- entrevista contextual;
- teste de compreensão;
- análise de comportamento;
- landing page sem cobrança, quando transparente;
- oferta controlada;
- protótipo;
- teste de interesse com compromisso verificável;
- piloto contratual posterior;
- análise de custos;
- análise de suporte;
- avaliação de parceiros;
- parecer especializado.

Nenhum método é automaticamente autorizado por este documento.

## 7. Evidências insuficientes isoladamente

- opinião genérica;
- curtida;
- audiência;
- clique sem contexto;
- cadastro sem uso;
- intenção declarada sem compromisso;
- benchmark não comparável;
- projeção sem premissa observável;
- receita de terceiro sem equivalência;
- crescimento de tráfego sem valor realizado.

## 8. Critérios de bloqueio

- contraprestação incompreensível;
- benefício não identificável;
- conflito material sem tratamento;
- uso incompatível de dados;
- ausência de cancelamento ou contestação;
- dependência de influência oculta;
- dano relevante ao gratuito;
- custo ou risco não observável;
- fragilidade operacional crítica;
- necessidade de decisão especializada não atendida;
- evidência insuficiente para o risco.

## 9. Regra de evidência

Quanto maior o impacto potencial sobre pessoas, dados, autonomia, recursos ou confiança, maior deverá ser a qualidade e independência da evidência.

## 10. Relação com o programa VAL

O programa VAL poderá fornecer evidências de necessidade, percepção, interesse e comportamento, mas não terá seu conteúdo alterado por este ciclo. Testes econômicos materiais deverão possuir protocolo próprio e aprovação futura.

## 11. Fora do escopo

- executar pesquisa;
- definir amostra;
- criar oferta pública;
- cobrar participantes;
- contratar parceiros;
- calcular preço;
- aprovar experimento;
- declarar validação comercial.
