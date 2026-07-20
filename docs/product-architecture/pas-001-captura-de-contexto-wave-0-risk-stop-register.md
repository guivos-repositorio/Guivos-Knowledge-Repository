---
id: PAS-001-CC-W0-RISK-001
title: Registro de Riscos, Exceções e Interrupção da Onda 0
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-UIC-NFR-SECURITY-001
  - PAS-001-CC-UIC-READINESS-001
  - PAS-001-CC-W0-EVIDENCE-001
---

# PAS-001-CC-W0-RISK-001 — Registro de Riscos, Exceções e Interrupção

## 1. Objetivo

Definir riscos iniciais, critérios de interrupção, tratamento de exceções e condições formais de retomada da Onda 0.

## 2. Escalas

### Probabilidade

- `P1`: rara;
- `P2`: improvável;
- `P3`: possível;
- `P4`: provável;
- `P5`: quase certa.

### Impacto

- `I1`: baixo e localizado;
- `I2`: moderado;
- `I3`: material;
- `I4`: alto;
- `I5`: crítico para pessoas, autoridade, segurança ou integridade.

### Severidade

- `low`: até 4;
- `medium`: 5 a 9;
- `high`: 10 a 15;
- `critical`: 16 a 25 ou qualquer risco que viole autoridade humana, isolamento ou revogação.

## 3. Registro inicial

| ID | Risco | P | I | Severidade | Tratamento inicial | Owner lógico | Gatilho de interrupção |
|---|---|---:|---:|---|---|---|---|
| W0-R-001 | domínio reinterpretado pela tecnologia | 3 | 5 | high | revisão de autoridade em cada ADR e história | arquitetura | requisito normativo alterado sem decisão formal |
| W0-R-002 | vazamento entre participantes | 2 | 5 | critical | escopo obrigatório e testes adversariais | segurança | qualquer acesso cruzado |
| W0-R-003 | conteúdo sensível em logs | 3 | 5 | high | redaction, scanning e campos proibidos | segurança/SRE | ocorrência de conteúdo bruto |
| W0-R-004 | revogação não bloquear novos usos | 3 | 5 | high | bloqueio central e tracking distribuído | domínio/segurança | novo recorte após efetividade |
| W0-R-005 | correção entregue mas não aplicada | 3 | 4 | high | ack funcional e consumidor registrado | plataforma | estado incorreto tratado como atual |
| W0-R-006 | restore reativar conteúdo revogado | 2 | 5 | critical | tombstones, replay e testes de desastre | dados | conteúdo volta a uso permitido |
| W0-R-007 | mídia maliciosa escapar da quarentena | 3 | 5 | high | sandbox e isolamento | segurança/dados | processamento fora da zona segura |
| W0-R-008 | prompt injection alterar comportamento | 4 | 5 | critical | conteúdo como dado, isolamento e testes | Intelligence/segurança | ação material ou autoridade ampliada |
| W0-R-009 | dependência provisória virar permanente | 4 | 3 | high | expiração e plano de substituição | arquitetura | fallback sem data ou owner |
| W0-R-010 | POC ser tratada como produção | 3 | 5 | high | ambientes e limites explícitos | governança | uso público ou real não autorizado |
| W0-R-011 | custo de mídia inviável | 3 | 3 | medium | quotas, retenção e medição | produto/finanças | custo excede limite aprovado |
| W0-R-012 | SLO candidato inadequado | 4 | 3 | high | carga e revisão por classe | engenharia | meta incentiva insegurança ou custo desproporcional |
| W0-R-013 | consumidor comprometido continuar ativo | 2 | 5 | critical | kill switch e detecção | segurança/plataforma | compromisso de segurança material |
| W0-R-014 | segredo exposto | 2 | 5 | critical | vault/KMS futuro, scanning e rotação | segurança | segredo em código, log ou artefato |
| W0-R-015 | evento incompatível alterar estado | 2 | 5 | critical | schema, quarentena e compatibilidade | engenharia | mensagem inválida produz efeito |
| W0-R-016 | idempotência mascarar payload divergente | 3 | 4 | high | hash material e conflito estável | engenharia | mesma chave produz efeitos diferentes |
| W0-R-017 | owner ausente para risco crítico | 3 | 4 | high | matriz de responsabilidade | governança | risco crítico sem responsável |
| W0-R-018 | expansão silenciosa do escopo | 4 | 3 | high | backlog e deferred explícitos | produto/arquitetura | nova capacidade sem alteração aprovada |
| W0-R-019 | evidência não reproduzível | 3 | 4 | high | template, configuração e hash | qualidade | gate baseado em prova informal |
| W0-R-020 | dados reais usados sem autorização | 2 | 5 | critical | dados sintéticos por padrão | privacidade | dado pessoal real não aprovado |

## 4. Critérios globais de interrupção

Interromper imediatamente o fluxo afetado quando houver:

1. vazamento entre participantes;
2. ampliação de autoridade humana por sistema, Intelligence ou administrador;
3. novo uso após revogação efetiva;
4. conteúdo sensível bruto em log;
5. segredo exposto;
6. restore reativando conteúdo proibido;
7. mídia maliciosa fora da quarentena;
8. prompt injection produzindo ação material;
9. mensagem incompatível alterando estado;
10. perda de rastreabilidade de correção ou revogação;
11. uso de dado real não autorizado;
12. tentativa de exposição pública;
13. ausência de owner para risco crítico;
14. tecnologia exigindo relaxamento de requisito obrigatório;
15. método de evidência não reproduzível.

## 5. Níveis de interrupção

### Stop-L1 — História

Aplicável quando o problema é local e não afeta autoridade ou integridade global.

### Stop-L2 — Incremento

Aplicável quando dependência, contrato ou risco impede conjunto de histórias.

### Stop-L3 — Onda 0

Aplicável quando há risco crítico, conflito normativo, exposição de dados ou incapacidade estrutural.

### Stop-L4 — Governança

Aplicável quando a decisão ultrapassa autoridade da equipe de engenharia ou exige reabrir arquitetura funcional.

## 6. Registro de interrupção

```yaml
stop_id: string
level: L1 | L2 | L3 | L4
detected_at: datetime
detected_by: string
fact: string
impact: string
requirement_ids: string[]
evidence_references: string[]
affected_scope: string[]
immediate_containment: string
owner: string
decision_authority: string
alternatives: object[]
resume_conditions: string[]
status: open | contained | decision_required | resolved | accepted_exception
resolved_at: datetime | null
```

## 7. Condições de retomada

Retomada exige:

- contenção comprovada;
- causa compreendida em nível suficiente;
- requisito e escopo afetados identificados;
- owner definido;
- correção ou mitigação implementável;
- evidência de revalidação planejada;
- riscos atualizados;
- aprovador competente;
- nenhuma pressão de cronograma como justificativa isolada.

## 8. Exceções

Toda exceção deverá conter:

```yaml
exception_id: string
requirement_id: string
justification: string
risk_id: string
scope: string[]
mitigation: string
owner: string
approver: string
created_at: datetime
expires_at: datetime
closure_criteria: string[]
compensating_evidence: string[]
status: proposed | accepted | rejected | expired | closed
```

Regras:

- exceção permanente exige ADR;
- exceção sem expiração é inválida;
- risco crítico não pode ser aceito apenas pela equipe executora;
- exceção expirada bloqueia gate;
- exceção não pode autorizar produção;
- exceção não pode permitir vazamento cruzado ou autoridade indevida.

## 9. Revisão de riscos

Revisar:

- no início de cada incremento;
- após cada POC;
- após mudança tecnológica;
- após incidente ou near miss;
- antes de cada gate;
- antes do Internal Trial;
- antes da decisão de conclusão.

## 10. Risco residual

Risco residual deverá registrar:

- risco original;
- controles aplicados;
- evidências;
- probabilidade e impacto restantes;
- limitações;
- owner;
- autoridade de aceite;
- validade;
- gatilho de reabertura.

## 11. Critérios de gate

- risco crítico aberto bloqueia todos os gates aplicáveis;
- risco high sem owner bloqueia governança;
- exceção inválida equivale a falha;
- risco não medido não é risco baixo;
- ausência de incidente não é evidência;
- gate aprovado não elimina revalidação quando contexto muda.

## 12. Autoridades de aceite

| Tipo | Autoridade mínima |
|---|---|
| risco técnico medium | owner técnico e arquitetura |
| risco high | arquitetura + segurança/produto conforme tema |
| risco critical | governança Guivos e autoridade competente |
| privacidade e dados pessoais | privacidade/jurídico + governança |
| produção ou go-live | processo futuro independente |

## 13. Estado inicial

Todos os riscos deste documento iniciam como `open_for_planning`. A implementação deverá atualizar probabilidade, impacto, owner nominal, tratamento, evidência e status antes de W0-08.