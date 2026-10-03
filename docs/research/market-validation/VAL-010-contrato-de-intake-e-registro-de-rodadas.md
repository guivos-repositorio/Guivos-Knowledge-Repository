---
id: VAL-010
title: Contrato de Intake, Evidência e Registro de Rodadas de Validação
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - VAL-004
  - VAL-005
  - VAL-006
  - VAL-007
  - VAL-009
normative: true
---

# VAL-010 — Contrato de Intake, Evidência e Registro de Rodadas de Validação

## 1. Finalidade

Este documento define o contrato mínimo para receber, tratar, auditar e registrar dados reais de uma rodada de validação da Guivos.

O objetivo é permitir que qualquer resultado publicado no GKR possa ser rastreado até:

```text
instrumento
→ rodada
→ base bruta
→ tratamento
→ denominadores
→ métricas
→ gates
→ decisão
```

O contrato não exige que dados pessoais ou respostas brutas sensíveis sejam armazenados no GKR. O repositório pode registrar referências controladas para evidências mantidas em ambiente apropriado.

## 2. Identificador de rodada

Toda aplicação deve receber um `round_id` estável antes de gerar uma decisão.

Formato recomendado:

```text
VAL-RND-YYYY-NNN
```

Exemplo de schema, não de rodada real:

```yaml
round_id: VAL-RND-YYYY-NNN
instrument_id: VAL-002
instrument_version: x.y.z
audience: B2C
territory_scope: <escopo>
opened_at: YYYY-MM-DD
closed_at: YYYY-MM-DD | null
status: planned | instrument_deployed | data_received | data_cleaned | metrics_calculated | decision_recorded
```

## 3. Registro mestre da rodada

Campos obrigatórios quando aplicáveis:

| Campo | Finalidade |
|---|---|
| `round_id` | impedir mistura de rodadas |
| `objective` | hipótese/pergunta testada |
| `instrument_id` | identificar questionário |
| `instrument_version` | garantir reprodutibilidade |
| `audience` | B2C/B2B/outro recorte autorizado |
| `territory_scope` | delimitar alcance da conclusão |
| `channels` | identificar origem de aquisição da amostra |
| `opened_at` | início real da coleta |
| `closed_at` | fechamento/corte analítico |
| `pretest_status` | planned/completed/evidence_pending/not_applicable |
| `raw_evidence_ref` | referência segura à base original |
| `received_count` | respostas recebidas no corte |
| `valid_count` | respostas após limpeza |
| `treatment_version` | versão das regras/scripts usados |
| `analysis_ref` | referência à análise reproduzível |
| `decision_state` | none/ready/recorded |
| `decision` | Go/Go com ajustes/Pivot parcial/No-Go temporário quando autorizado |
| `owner_role` | função responsável |
| `approved_by` | autoridade da decisão, em sistema apropriado |
| `limitations` | vieses e restrições de interpretação |

## 4. Pacote de entrada da base

O intake deve receber, quando disponível:

1. export bruto imutável ou snapshot identificável;
2. metadata da exportação;
3. dicionário de perguntas/campos;
4. versão exata do instrumento;
5. período da coleta;
6. origem/canal;
7. regras de consentimento aplicadas;
8. lista de mudanças ocorridas durante a coleta;
9. referência separada de contatos voluntários, quando houver;
10. checksum, versionamento ou outro mecanismo proporcional para garantir que a base analisada corresponda à evidência recebida.

## 5. Dados pessoais e minimização

O dataset analítico deve priorizar identificadores anônimos/pseudônimos e conter somente dados necessários à análise autorizada.

Quando contato for coletado para primeira experiência ou follow-up:

- deve permanecer separado da análise quando possível;
- deve possuir finalidade clara;
- não deve ser usado para inferir aceitação adicional;
- não deve ser publicado no GKR;
- deve seguir política de retenção/privacidade aplicável.

O interesse em contato não autoriza uso irrestrito dos demais dados.

## 6. Ledger de limpeza

Toda transformação entre `received_count` e `valid_count` deve gerar um ledger agregável.

Estrutura mínima:

| Regra | Contagem | Justificativa |
|---|---:|---|
| recebidas | N | base de entrada |
| incompletas excluídas | N | regra objetiva |
| duplicadas excluídas | N | critério de deduplicação |
| automatizadas/inválidas excluídas | N | evidência de baixa qualidade |
| versão incompatível segregada | N | ausência de mapeamento seguro |
| fora do escopo segregadas | N | território/público quando aplicável |
| **válidas** | **N** | denominador elegível final |

A tabela acima é modelo e não contém números reais.

Nenhuma resposta negativa deve ser excluída por contrariar a hipótese.

## 7. Versionamento do tratamento

O tratamento deve possuir versão estável quando regras, fórmulas ou classificação qualitativa mudarem.

```text
raw dataset
+ treatment_version
+ codebook_version
= analyzed dataset
```

Se uma regra mudar depois da primeira análise, a rodada deve ser recalculada ou registrar explicitamente que resultados pertencem a versões diferentes.

## 8. Classificação da Q11

Como Q11 exige classificação humana/assistida de compreensão, o pacote deve registrar:

- rubrica usada;
- versão da rubrica;
- categorias possíveis;
- exemplos de borda sanitizados quando necessário;
- responsável/metodologia de codificação;
- mecanismo de revisão de inconsistências;
- quantidade em cada categoria.

Uso de IA para auxiliar classificação não transforma a classificação em fato objetivo. A rubrica e a revisão continuam sendo a autoridade metodológica.

## 9. Denominadores

Todo KPI deve possuir um `metric_record` com:

```yaml
metric_id: <id>
round_id: <round>
numerator: <n>
denominator: <n>
exclusions: <regras>
value: <resultado>
segment: <geral ou segmento>
method_ref: <VAL-004/006>
```

É proibido publicar percentual sem denominador quando o denominador difere do total de respostas válidas.

Isso é especialmente importante para Q8, Q9 e outras perguntas com alternativas excluídas da base elegível.

## 10. Composição da amostra

O pacote analítico deve incluir, no mínimo:

- faixa etária;
- situação principal;
- estado/DF;
- região;
- área escolhida;
- momento atual;
- mudança desejada;
- canal de aquisição quando disponível;
- participantes fora do Brasil segregados.

Também deve registrar:

- maior concentração por estado;
- maior concentração por canal;
- segmentos com N reduzido;
- diferenças relevantes de composição em relação ao recorte pretendido.

## 11. Métricas obrigatórias

Uma rodada candidata a decisão formal deve produzir as métricas definidas por VAL-006/007, incluindo:

- descoberta tardia;
- lacuna de adequação;
- IFO;
- esforço;
- compreensão;
- relevância contextual;
- contribuição percebida;
- intenção positiva;
- interesse confirmado;
- IGV;
- duração/abandono quando disponíveis.

Cada valor deve preservar base e faixa de decisão.

## 12. Gate ledger

O registro de decisão deve materializar os gates de VAL-007:

| Gate | Condição | Resultado | Evidência |
|---|---|---|---|
| G1 Base elegível | >= 200 válidas | pass/fail/not_evaluable | ref |
| G2 Compreensão | >= 80% para Go | pass/fail/not_evaluable | ref |
| G3 Problema | IFO >= 65% para Go | pass/fail/not_evaluable | ref |
| G4 Valor | relevância e contribuição >= 8,0 | pass/fail/not_evaluable | ref |
| G5 Adoção | intenção >= 60% | pass/fail/not_evaluable | ref |
| G6 Qualidade | sem viés crítico não tratado | pass/fail/not_evaluable | ref |
| G7 Cobertura | concentração identificada/considerada | pass/fail/not_evaluable | ref |
| G8 Instrumento | pré-teste sem falha grave | pass/fail/not_evaluable | ref |

`not_evaluable` não pode ser interpretado como `pass`.

## 13. Registro de decisão

Modelo mínimo:

```yaml
round_id: VAL-RND-YYYY-NNN
technical_recommendation: <Go | Go com ajustes | Pivot parcial | No-Go temporário>
igv: <valor>
gates_passed: []
gates_failed: []
gates_not_evaluable: []
key_positive_evidence: []
key_negative_evidence: []
limitations: []
allowed_conclusion_scope: <escopo>
human_decision: <estado>
decision_date: YYYY-MM-DD
next_validation: <ato>
```

Esse schema não registra uma decisão real nesta versão.

## 14. Evidência favorável e contrária

O relatório não pode ser composto apenas por sinais positivos.

Para cada rodada, registrar:

- indicadores abaixo da meta;
- segmentos de baixa aderência;
- objeções;
- falhas de compreensão;
- concentração de canal/território;
- sinais de resposta por cortesia ou seleção;
- carga cognitiva/abandono;
- resultados que contrariem a narrativa esperada.

A evidência contrária não é ruído a ser removido; é parte da validade da decisão.

## 15. Alcance da conclusão

Toda decisão deve informar o que **não** está autorizado a concluir.

Exemplos de limites:

- amostra brasileira não prova aceitação em Portugal;
- alta intenção declarada não prova retenção;
- relevância percebida não prova disposição a pagar;
- interesse em primeira experiência não prova uso recorrente;
- 200 respostas não provam product-market fit;
- resultado B2C não valida Guivos Business B2B;
- aceitação conceitual não valida todos os sete Produtos Especializados.

## 16. Relação com preço e monetização

A pesquisa conceitual vigente mantém preço fora de seu escopo.

Portanto:

```text
VAL-002 positivo
≠ preço validado
≠ willingness-to-pay comprovada
≠ plano comercial aprovado
```

Preço deve ser testado em frente apropriada, com metodologia e amostra compatíveis.

## 17. Relação com comportamento

Após decisão conceitual, o sistema deve buscar evidências comportamentais como:

- clique/inscrição em primeira experiência;
- comparecimento;
- ativação;
- retorno;
- conclusão de ação;
- retenção;
- indicação;
- transação quando autorizada.

Esses eventos devem ser interpretados no contexto de privacidade, denominador e seleção adequada.

## 18. Publicação no GKR

O GKR deve publicar, quando autorizado:

- round_id;
- versão do instrumento;
- período;
- contagens agregadas;
- método de tratamento;
- KPIs;
- gates;
- decisão;
- limitações;
- referências de evidência sanitizadas.

Não deve publicar automaticamente:

- respostas pessoais identificáveis;
- contatos;
- IPs/device identifiers;
- dados brutos sensíveis;
- segredos de plataforma;
- qualquer informação que viole consentimento ou política de privacidade.

## 19. Estado desta versão

O contrato está ativo como **regra para futuras evidências de execução**.

Ele não afirma que uma rodada real tenha sido processada, que 200/500 respostas tenham sido alcançadas ou que uma decisão de mercado exista.
