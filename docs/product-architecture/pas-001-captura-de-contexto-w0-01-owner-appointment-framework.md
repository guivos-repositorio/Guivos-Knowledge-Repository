---
id: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
title: Framework de Nomeação dos Owners Técnicos do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNERS-001
related:
  - PAS-001-CC-W0-01-CHARTER-001
  - PAS-001-CC-W0-01-READINESS-001
  - PAS-001-CC-W0-RISK-001
---

# PAS-001-CC-W0-01-OWNER-APPOINTMENT-001 — Framework de Nomeação dos Owners Técnicos

> **Estado:** `Appointment framework defined — nominal assignments pending`.
>
> Este documento define como selecionar, qualificar, nomear, revisar, suspender e substituir owners técnicos. Não nomeia pessoas, não cria vínculo e não autoriza execução do W0-01.

## 1. Objetivo

Estabelecer um processo verificável para preencher os papéis:

- Architecture Owner;
- Engineering Owner / Tech Lead;
- Security & Privacy Owner;
- Quality & Evidence Owner;
- Platform/DevOps Owner;
- Data Owner antes do W0-03.

## 2. Princípios

1. owner lógico não equivale a owner nominal;
2. competência precede autoridade;
3. equity, contrato ou senioridade declarada não substituem evidência de capacidade;
4. aceitação do papel deve ser explícita;
5. autoridade possui escopo, limite e validade;
6. conflito de interesse deve ser tratado;
7. nomeação não autoriza automaticamente execução;
8. patrocinador não substitui revisão técnica especializada;
9. fornecedor não recebe governança por padrão;
10. alteração crítica exige segregação mínima.

## 3. Processo de nomeação

### Etapa 1 — Perfil oficial

Cada papel deverá possuir missão, responsabilidades, autoridade, limites, competências, disponibilidade, modelo de vínculo, conflitos incompatíveis e critérios de substituição.

### Etapa 2 — Identificação

Candidatos poderão vir de processo seletivo, rede profissional, consultoria, parceria, contratação, cofundação ou advisory operacional. Identificação não cria autoridade.

### Etapa 3 — Evidências do candidato

Registrar, conforme aplicável:

- nome completo;
- conta GitHub;
- currículo ou perfil profissional;
- portfólio e projetos relevantes;
- referências;
- disponibilidade;
- modelo de vínculo pretendido;
- declaração de conflitos;
- concordância com confidencialidade e propriedade intelectual.

### Etapa 4 — Avaliação

A avaliação deverá incluir:

- análise documental;
- entrevista estruturada;
- exercício técnico controlado;
- avaliação de autoridade, segurança e documentação;
- matriz de pontuação;
- registro de riscos e limitações.

O exercício não deverá exigir solução completa gratuita nem uso de dados reais.

### Etapa 5 — Decisão

A decisão deverá registrar:

- candidato avaliado;
- papel;
- evidências;
- pontuação;
- limitações;
- conflitos;
- recomendação;
- aprovadores;
- validade da decisão.

### Etapa 6 — Aceite

A pessoa deverá aceitar explicitamente:

- responsabilidades;
- autoridade de interrupção;
- limites;
- política de acesso;
- segregações;
- confidencialidade;
- propriedade intelectual;
- revisão periódica;
- condições de suspensão e destituição.

### Etapa 7 — Ativação

O status somente muda para `active` quando:

- aceite estiver registrado;
- conta GitHub estiver vinculada;
- acesso for compatível;
- CODEOWNERS estiver planejado ou configurado;
- conflitos estiverem tratados;
- validade estiver definida;
- EV-017 for atualizada.

## 4. Estados

- `identified`: pessoa conhecida, sem avaliação concluída;
- `screening`: documentação em análise;
- `assessment`: avaliação em andamento;
- `proposed`: recomendação pronta;
- `accepted`: pessoa aceitou formalmente;
- `active`: acesso e autoridade ativados;
- `suspended`: autoridade temporariamente bloqueada;
- `revoked`: nomeação encerrada;
- `expired`: validade encerrada;
- `rejected`: candidatura não aprovada.

Somente `active` satisfaz owner nominal para autorização técnica. `accepted` sem acesso e controles não é suficiente.

## 5. Autoridade de aprovação

| Nomeação | Aprovação mínima |
|---|---|
| Architecture Owner | Guilherme Oliveira + parecer técnico independente quando disponível |
| Engineering Owner | Guilherme Oliveira + Architecture Owner, se já ativo |
| Security & Privacy Owner | Guilherme Oliveira + parecer especializado independente |
| Quality & Evidence Owner | Guilherme Oliveira + Architecture ou Security conforme escopo |
| Platform/DevOps Owner | Engineering + Security/Privacy, com ciência de Guilherme |
| Data Owner | Architecture + Security/Privacy, com ciência de Guilherme |

Na ausência de autoridade técnica ativa, a nomeação deverá registrar revisão externa ou limitação provisória, sem dispensar a avaliação.

## 6. Validade e revisão

Toda nomeação deverá possuir:

- data de início;
- data de revisão;
- validade ou condição de permanência;
- substituto ou regra de delegação;
- gatilhos de suspensão;
- gatilhos de destituição.

Revisar após incidente, mudança material de escopo, conflito, indisponibilidade prolongada, falha grave de gate ou alteração de vínculo.

## 7. Suspensão imediata

Suspender autoridade quando houver:

- exposição indevida de dados ou segredo;
- ampliação de autoridade humana pelo sistema;
- aprovação de evidência sabidamente inválida;
- conflito de interesse não declarado;
- acesso incompatível com o papel;
- descumprimento material de confidencialidade;
- tentativa de promover POC a produção sem autorização;
- ausência prolongada sem delegação válida.

## 8. Evidência

A nomeação deverá produzir parte de EV-017 com:

- registro de avaliação;
- registro de decisão;
- aceite;
- conta GitHub;
- autoridade e limites;
- conflitos e mitigação;
- validade;
- aprovadores;
- hash dos artefatos;
- status atual.

## 9. Condição de autorização

O W0-01 continuará bloqueado até que os cinco papéis obrigatórios estejam `active`, ou que Platform/DevOps possua acumulação provisória expressamente aprovada, com revisão independente e validade limitada.

## 10. Limites

Este framework não:

- nomeia candidatos;
- cria vínculo trabalhista ou societário;
- concede equity;
- concede acesso ao GitHub;
- cria repositório;
- aceita ADR;
- autoriza código, POC, ambiente, W0-01, W0-02 ou produção.