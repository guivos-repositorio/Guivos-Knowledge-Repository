---
id: PAS-001-CC-W0-01-CANDIDATE-ASSESSMENT-001
title: Matriz de Avaliação de Candidatos a Owner Técnico
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
related:
  - PAS-001-CC-W0-01-ROLE-PROFILES-001
  - PAS-001-CC-W0-RISK-001
---

# PAS-001-CC-W0-01-CANDIDATE-ASSESSMENT-001 — Matriz de Avaliação de Candidatos

## 1. Objetivo

Avaliar candidatos com critérios comparáveis, evidências verificáveis e eliminadores explícitos, evitando seleção por afinidade, título, popularidade ou custo isolado.

## 2. Fases

1. elegibilidade;
2. avaliação documental;
3. entrevista estruturada;
4. exercício técnico controlado;
5. referências e conflitos;
6. pontuação;
7. recomendação;
8. decisão e validade.

## 3. Eliminadores

O candidato será reprovado independentemente da pontuação quando:

- defender uso de dados reais sem autorização;
- tratar autenticação como autoridade humana;
- aceitar vazamento entre participantes como risco tolerável;
- negar necessidade de revogação, rastreabilidade ou revisão;
- recusar documentação de decisões;
- ocultar conflito material;
- propor segredo em código ou credencial compartilhada;
- considerar POC equivalente a produção;
- não aceitar autoridade de interrupção aplicável ao papel;
- não possuir disponibilidade mínima declarada.

## 4. Matriz ponderada

| Critério | Peso | Evidência mínima |
|---|---:|---|
| competência específica do papel | 25% | projetos, decisões ou exercício relacionado |
| experiência prática comprovada | 20% | histórico verificável e responsabilidade real |
| segurança, privacidade e autoridade | 15% | análise correta de cenários críticos |
| qualidade de decisão e documentação | 15% | ADR, parecer, desenho ou registro comparável |
| colaboração e revisão | 10% | exemplos de feedback, conflitos e alinhamento |
| disponibilidade e continuidade | 10% | compromisso, resposta e delegação |
| custo e sustentabilidade | 5% | modelo compatível com a Onda 0 |

## 5. Escala

- `0`: sem evidência ou incompatível;
- `1`: conhecimento superficial;
- `2`: experiência limitada com supervisão necessária;
- `3`: capacidade adequada ao escopo;
- `4`: experiência forte e autônoma;
- `5`: domínio comprovado, capacidade de orientar e revisar terceiros.

A pontuação ponderada não substitui requisito obrigatório. Competência classificada como obrigatória com nota inferior a 3 impede nomeação ativa, salvo limitação provisória formal que não afete o escopo delegado.

## 6. Exercícios por papel

### Architecture Owner

- revisar uma invariante do `CaptureRecord`;
- identificar fronteiras entre domínio e infraestrutura;
- analisar trade-offs do ADR-TCC-001;
- explicar como preservar revogação e reconstrução;
- produzir registro curto de decisão.

### Engineering Owner

- decompor uma história P0;
- propor teste de idempotência e concorrência;
- revisar um contrato versionado;
- identificar risco de integração;
- demonstrar abordagem de revisão de PR.

### Security & Privacy Owner

- revisar cenário de representação e menor;
- identificar vazamento em logs;
- tratar segredo exposto;
- avaliar ameaça de prompt injection;
- definir condição de interrupção e retomada.

### Quality & Evidence Owner

- revisar manifesto EV-017;
- distinguir documento de evidência;
- definir teste reproduzível de branch protection;
- identificar evidência expirada ou insuficiente;
- propor critérios de gate.

### Platform/DevOps Owner

- desenhar proteção da `main`;
- propor pipeline mínimo sem produção;
- explicar segregação de segredos;
- definir rollback de automação;
- demonstrar menor privilégio e auditoria.

## 7. Entrevista estruturada

Perguntas mínimas:

1. qual decisão técnica mais difícil você documentou e por quê;
2. como você reage quando requisito obrigatório conflita com prazo;
3. como evita ser único autor e aprovador de controle crítico;
4. qual condição faria você interromper uma entrega;
5. como trata erro próprio descoberto após aprovação;
6. como mantém rastreabilidade entre requisito, código, teste e evidência;
7. como limita uma solução provisória para não se tornar permanente.

## 8. Referências

Quando aplicável, validar:

- papel exercido;
- nível real de responsabilidade;
- capacidade de colaboração;
- qualidade de decisão;
- tratamento de incidentes;
- confiabilidade e documentação;
- motivos de saída ou encerramento do projeto.

## 9. Registro de avaliação

```yaml
assessment_id: string
candidate_name: string
role: string
assessors: string[]
started_at: datetime
completed_at: datetime | null
eligibility: passed | failed
eliminators: string[]
criteria:
  - id: string
    weight: number
    score: number
    evidence: string[]
    limitations: string[]
weighted_score: number
conflicts: string[]
availability: object
recommendation: approve | approve_with_limits | hold | reject
valid_until: date
approvers: string[]
```

## 10. Faixas de recomendação

- `85–100`: recomendação forte, desde que sem eliminador;
- `70–84`: recomendação possível com limites explícitos;
- `55–69`: manter em avaliação ou papel assistido não bloqueante;
- `<55`: não nomear para owner;
- qualquer eliminador: rejeitar ou suspender avaliação.

## 11. Limites

A matriz não:

- garante contratação;
- concede acesso;
- substitui referências;
- autoriza acúmulo de papéis;
- converte candidato em owner;
- permite compensar falha crítica com nota alta em outro critério;
- autoriza execução do W0-01.
