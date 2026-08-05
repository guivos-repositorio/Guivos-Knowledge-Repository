---
id: GKR-VAL-OPS-AUD-001
title: Auditoria de Evidência Operacional do Programa VAL
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-STATE-001
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
  - GKR-CLAIMS-TRACE-001
  - VAL-002
  - VAL-006
  - VAL-007
related:
  - VAL-001
  - VAL-003
  - VAL-004
  - VAL-005
  - VAL-008
normative: false
---

# Auditoria de Evidência Operacional do Programa VAL

## 1. Finalidade

Este documento verifica se o programa de validação B2C possui evidência suficiente de execução operacional, além dos instrumentos e critérios documentais já integrados.

A auditoria distingue:

- desenho do instrumento;
- readiness para pré-teste;
- pré-teste executado;
- formulário publicado;
- coleta iniciada;
- base recebida;
- respostas válidas;
- análise concluída;
- decisão formal;
- Outcome empresarial.

Nenhuma dessas etapas é inferida a partir da etapa anterior.

## 2. Autoridades documentais confirmadas

A baseline da `main` contém:

| Artefato | Versão | Papel |
|---|---:|---|
| VAL-002 | 2.1.0 | Pesquisa Oficial B2C |
| VAL-006 | 1.3.1 | Dashboard e dicionário de indicadores |
| VAL-007 | 1.3.1 | Critérios de decisão |

A pesquisa vigente possui:

- título público `Construindo a Guivos`;
- duração estimada de 3 a 5 minutos;
- 19 perguntas;
- linguagem direta ao participante;
- versionamento obrigatório da resposta;
- preço e comportamento real fora da validação conceitual inicial.

O programa integrado também determina:

- pré-teste com 10 a 15 participantes;
- mínimo de 200 respostas válidas para decisão formal;
- meta preferencial de 500 respostas válidas;
- diversidade e qualidade mínimas da amostra;
- cálculo integral dos KPIs;
- critérios de `Go`, `Go com ajustes`, `Pivot parcial` e `No-Go temporário`.

Esses elementos comprovam desenho e readiness documental. Não comprovam execução.

## 3. Evidências pesquisadas

A auditoria procurou no Git e no acervo disponível:

- commit de formulário operacional;
- identificador de versão do formulário publicado;
- relatório de pré-teste;
- lista de ajustes decorrentes do pré-teste;
- data de abertura da coleta;
- data de encerramento ou corte;
- exportação de respostas;
- registro de versão por resposta;
- log de respostas excluídas;
- contagem de respostas recebidas e válidas;
- perfil da amostra;
- cálculo de indicadores;
- dashboard preenchido;
- decisão formal;
- dataset ou evidência equivalente;
- registro de consentimento e privacidade aplicáveis.

## 4. Resultado da busca

### 4.1 Evidência localizada

Foram localizados:

- instrumentos VAL integrados;
- regras de validade da resposta;
- níveis de maturidade da base;
- fórmulas e denominadores;
- gates de decisão;
- conversas históricas indicando que o formulário definitivo e a planilha automática seriam entregáveis posteriores;
- conversa indicando que os KPIs seriam analisados quando existisse base significativa;
- menção conversacional a um endereço público de pesquisa e mensagens de convite.

### 4.2 Evidência não localizada

Não foram localizados na baseline auditada:

- relatório de pré-teste concluído;
- dez a quinze registros de pré-teste identificáveis;
- versão imutável do formulário operacional;
- comprovação da equivalência entre o formulário publicado e VAL-002 2.1.0;
- changelog operacional do formulário;
- exportação de respostas;
- número de respostas recebidas;
- número de respostas válidas;
- taxa de conclusão;
- taxa de abandono;
- tempos médio e mediano;
- motivos de exclusão;
- perfil e concentração da amostra;
- classificação da pergunta aberta;
- cálculo do IFO, esforço, compreensão, relevância, contribuição, intenção ou interesse;
- dashboard preenchido;
- decisão formal;
- Outcome empresarial.

A ausência de evidência localizada não prova que nenhuma atividade externa ocorreu. Ela prova que essa atividade não está suficientemente registrada para alterar o estado do GKR.

## 5. Matriz de maturidade operacional

| Etapa | Estado auditado | Evidência mínima exigida |
|---|---|---|
| Desenho do instrumento | `verified` | VAL-002 2.1.0 |
| Modelo de análise | `verified` | VAL-006 1.3.1 |
| Critérios de decisão | `verified` | VAL-007 1.3.1 |
| Readiness para pré-teste | `verified_documentally` | instrumento e protocolo definidos |
| Pré-teste | `not_verified` | relatório, amostra, duração, dúvidas e abandono |
| Ajuste pós-pré-teste | `not_verified` | changelog e justificativa |
| Formulário definitivo | `not_verified` | URL, provedor, ID e versão imutável |
| Consentimento e privacidade | `not_verified` | texto aplicado e base legal adequada |
| Coleta iniciada | `not_verified` | data, canal, versão e registro de abertura |
| Respostas recebidas | `not_verified` | exportação ou painel do provedor |
| Base válida | `not_verified` | exclusões e critérios aplicados |
| Análise | `not_verified` | cálculos reproduzíveis e denominadores |
| Decisão VAL | `not_verified` | registro formal e limitações |
| Outcome empresarial | `not_authorized` | processo posterior aplicável |

## 6. Risco de versão

O acervo histórico contém referências a VAL-002, VAL-006 e VAL-007 em versões 1.1.0, com:

- 23 perguntas;
- duração de 5 a 7 minutos;
- indicadores e pesos diferentes;
- numeração de perguntas diferente;
- formulações de decisão diferentes.

A `main` possui versões posteriores.

Qualquer formulário construído a partir da versão 1.1.0 não poderá ser tratado como aplicação de VAL-002 2.1.0.

Antes da análise, será obrigatório comprovar:

```text
form_version
survey_version
question_code_map
launch_date
response_version
```

Resultados de versões materialmente diferentes não poderão ser combinados sem mapeamento explícito.

## 7. Risco de link sem trilha de evidência

Um domínio ou link divulgado pode comprovar intenção de distribuição, mas não comprova isoladamente:

- conteúdo efetivamente exibido;
- versão do instrumento;
- funcionamento durante o período;
- consentimento;
- quantidade de respostas;
- integridade da base;
- ausência de duplicidade;
- cálculo dos KPIs;
- elegibilidade para decisão.

O endereço público deverá ser associado a um registro de publicação e a uma versão imutável do instrumento.

## 8. Pacote mínimo de evidência operacional

Para reconhecer uma rodada, deverão existir:

### 8.1 Registro da publicação

- identificador da rodada;
- URL e provedor;
- versão de VAL-002;
- data e hora de abertura;
- canais de divulgação;
- público pretendido;
- texto de apresentação;
- termos, consentimento e privacidade aplicados;
- responsável pela rodada.

### 8.2 Registro do pré-teste

- 10 a 15 participantes;
- critérios de seleção;
- tempo médio e mediano;
- abandono;
- perguntas relidas;
- dúvidas e ambiguidades;
- percepção de excesso de opções;
- interpretação da proposta;
- problemas encontrados;
- ajustes aceitos e rejeitados.

### 8.3 Registro da base

- exportação bruta preservada;
- hash ou localização restrita;
- versão do instrumento em cada resposta;
- respostas recebidas, concluídas, válidas e excluídas;
- razões de exclusão;
- duplicidades;
- tempos plausíveis;
- distribuição da amostra;
- concentração por canal e geografia.

### 8.4 Registro da análise

- fórmulas aplicadas;
- denominadores;
- classificação da pergunta aberta;
- KPIs calculados;
- segmentos;
- limitações;
- evidências favoráveis e contrárias;
- dashboard reproduzível.

### 8.5 Registro da decisão

- estado `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário`;
- gates atendidos e não atendidos;
- autoridade decisória;
- data;
- limitações;
- próxima hipótese;
- ações autorizadas e não autorizadas.

## 9. Sensibilidade e privacidade

Respostas de pesquisa podem conter:

- estado ou localização;
- faixa etária;
- situação pessoal;
- objetivos;
- dificuldades;
- comentários abertos;
- contato opcional.

A base bruta não deverá ser publicada no repositório público. O GKR deverá armazenar somente:

- metadados da rodada;
- metodologia;
- resultados agregados adequadamente anonimizados;
- hashes ou referências controladas;
- decisões e limitações.

Contato opcional deverá permanecer separado dos KPIs e da análise principal.

## 10. Decisão da auditoria

```text
VAL documentation readiness: verified
Pre-test execution: not verified
Published-form equivalence: not verified
Collection status: not verified
Valid response base: not verified
KPI results: not verified
Formal decision: not verified
Canonical Outcome: none
```

### Estado permitido

```text
operational_evidence_pending
```

Não é permitido declarar:

- pesquisa concluída;
- aceitação forte, média ou baixa;
- base significativa;
- validação de mercado;
- decisão Go;
- interesse comprovado;
- intenção representativa;
- Outcome empresarial.

## 11. Encaminhamento

A execução e reconciliação operacional pertencem ao P4.

O P0 registra:

- versões corretas;
- ausência de evidência suficiente;
- pacote mínimo exigido;
- proteção contra combinação de versões;
- necessidade de preservar privacidade.

## 12. Resultado

```text
Audit target: VAL operational evidence
Documentary design: PASS
Operational evidence: NOT VERIFIED
Decision eligibility: NO
Current-state change: NO
Route: P4
```
