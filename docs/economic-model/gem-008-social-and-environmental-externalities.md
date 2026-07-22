---
id: GEM-008-SOCIAL-AND-ENVIRONMENTAL-EXTERNALITIES-001
title: Externalidades Sociais e Ambientais
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Externalidades Sociais e Ambientais

## 1. Objetivo

Incorporar impactos sobre participantes, terceiros, comunidades e ambiente à análise de sustentabilidade, mesmo quando não apareçam como custo financeiro direto.

## 2. Categorias

### Pessoas e autonomia

- pressão comportamental;
- dependência induzida;
- perda de autonomia;
- exploração de vulnerabilidade;
- desigualdade de acesso;
- sobrecarga emocional ou operacional.

### Dados e confiança

- coleta excessiva;
- reutilização incompatível;
- exposição;
- perda de confiança;
- assimetria informacional;
- publicidade ou influência oculta.

### Parceiros e trabalho

- transferência silenciosa de risco;
- sobrecarga de fornecedores;
- relações de trabalho inadequadamente disfarçadas;
- concentração de poder;
- condições inseguras.

### Comunidades e impacto social

- exposição de beneficiários;
- competição sobre sofrimento;
- deslocamento de prioridades locais;
- uso promocional de causas;
- atividade apresentada como impacto comprovado.

### Ambiente

- consumo de recursos;
- logística e deslocamento;
- descarte;
- emissões;
- incentivos a consumo irresponsável;
- efeitos indiretos de escala.

## 3. Estados

```yaml
externality_status:
  not_assessed |
  identified |
  evidence_required |
  mitigation_required |
  material |
  unacceptable |
  blocked
```

## 4. Regras

- resultado financeiro positivo não compensa externalidade material incompatível;
- ausência de preço não significa ausência de custo social;
- impacto alegado deverá ser separado de evidência;
- beneficiários não serão tratados como ativos promocionais;
- custos não poderão ser transferidos silenciosamente a voluntários, comunidades ou parceiros;
- mitigação deverá possuir owner, evidência e revisão;
- externalidade incerta deverá permanecer visível;
- `unacceptable` ou `blocked` impedirá expansão conceitual do mecanismo.

## 5. Tratamentos candidatos

- prevenção;
- redução;
- transparência;
- consentimento;
- acessibilidade;
- limite de exposição;
- compensação apropriada;
- substituição;
- suspensão;
- encerramento;
- reparação futura.

## 6. Registro conceitual

```yaml
externality_id: string
scope: string
category: string
affected_parties:
  - string
status: identified
severity_defined: false
evidence:
  - string
mitigation:
  - string
owner: null
interruption_condition: string
```

## 7. Fora do escopo

- mensuração de carbono;
- avaliação de impacto real;
- compensação financeira;
- auditoria;
- operação.