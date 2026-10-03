---
id: GKR-OPERATIONAL-LEGAL-TRUTH-001
title: Registro de Verdade Operacional e Legal
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-LEGAL-SURFACE-GATES-001
  - GKR-INSTITUTIONAL-LEGAL-EVIDENCE-001
  - GEA-GRAPH-REFERENCE-001
  - GKR-STATE-001
normative: true
---

# Registro de Verdade Operacional e Legal

## 1. Finalidade

Este registro estabelece como o GKR deve distinguir arquitetura, intenção, evidência técnica, existência jurídica e operação real em assuntos legais, de privacidade, segurança, dados e compliance.

O objetivo não é centralizar segredos operacionais no GKR. É impedir afirmações institucionais ou públicas superiores à evidência disponível.

## 2. Regra de evidência

```text
planejado
≠ configurado
≠ implementado
≠ publicado
≠ usado
≠ auditado
≠ continuamente controlado
```

Toda afirmação operacional material deverá apontar para evidência verificável, datada e adequada ao fato declarado.

## 3. Estados OT0–OT8

| Estado | Significado |
|---|---|
| `OT0 identified` | obrigação, risco, capacidade ou objeto identificado |
| `OT1 designed` | arquitetura, política ou controle desenhado |
| `OT2 approved` | desenho aprovado pela autoridade aplicável |
| `OT3 implemented_nonproduction` | implementação existe fora de produção ou sem prova de uso real |
| `OT4 deployed` | componente/superfície foi disponibilizado no ambiente alvo |
| `OT5 operational_evidenced` | há evidência de uso/execução real no escopo declarado |
| `OT6 controlled` | controle operacional, ownership e tratamento de exceções estão evidenciados |
| `OT7 assured` | teste, auditoria, amostragem ou revisão independente/interna apropriada sustenta o controle |
| `OT8 sustained` | histórico demonstra operação contínua e revisão periódica |

Uma capacidade pode permanecer legitimamente em OT1 por longo período. Tempo não equivale a maturidade operacional.

## 4. Qualidade da evidência

A evidência deve ser compatível com o fato.

### Exemplos de evidência de desenho

- documento de arquitetura;
- política aprovada;
- ADR;
- modelo de dados;
- matriz de tratamento;
- parecer/revisão.

### Exemplos de evidência de implementação

- configuração versionada;
- release identificável;
- teste automatizado ou manual registrado;
- screenshot técnico governado quando apropriado;
- endpoint/fluxo de homologação comprovado;
- artefato de deployment.

### Exemplos de evidência de operação

- evento/log com contexto e retenção adequados;
- registro de atendimento;
- versão publicada confirmada;
- aceite/consentimento válido registrado;
- incidente processado;
- solicitação de titular atendida;
- relatório operacional verificável.

### Exemplos de assurance

- auditoria;
- teste periódico;
- revisão de acesso;
- exercício de recuperação;
- amostragem de registros;
- revisão de fornecedor;
- teste de processo de incidente;
- reconciliação de versões.

A presença de uma evidência não autoriza extrapolar seu escopo.

## 5. Evidence ledger mínimo

O GKR poderá referenciar, sem armazenar dados sensíveis ou segredos, um ledger com:

| Campo | Uso |
|---|---|
| `evidence_id` | identificador |
| objeto | controle, superfície, sistema ou processo |
| claim | fato que a evidência sustenta |
| estado OT | maturidade autorizada |
| escopo | produto, entidade, ambiente, jurisdição |
| período/data | validade temporal |
| owner | responsável |
| source_type | contrato, sistema, teste, registro, certidão etc. |
| source_location | referência segura, quando apropriado |
| reviewer | quem validou |
| sensitivity | público, interno, restrito ou secreto |
| expires/review_due | quando exige revisão |

Segredos, credenciais, tokens, documentos pessoais e bases com dados pessoais não devem ser copiados para o GKR apenas para provar existência.

## 6. Registro corrente de verdade — P6

A tabela abaixo representa somente o conhecimento integrado/auditado no GKR no checkpoint P6.

| Objeto | Estado máximo sustentado | Observação |
|---|---|---|
| arquitetura de privacidade e consentimentos | `OT1 designed` | autoridade P6 proposta |
| separação de dados entre entidades relacionadas | `OT1 designed` | já suportada pelo P5 |
| guardrails de privacidade para grafo | `OT1 designed` | `GEA-GRAPH-REFERENCE-001` |
| Neo4j em produção com dados pessoais | abaixo de OT5 / `not_evidenced` | arquitetura de referência não prova deployment |
| inventário de atividades de tratamento | `not_evidenced` | não há baseline operacional integrado |
| mapa controlador/operador por atividade | `not_evidenced` | deve ser derivado de atividades reais |
| bases jurídicas revisadas por atividade | `not_evidenced` | consentimento não pode ser presumido |
| Termos de Uso públicos | `not_evidenced` | nenhuma versão pública foi promovida no GKR |
| Aviso/Política de Privacidade pública | `not_evidenced` | idem |
| inventário de cookies/SDKs | `not_evidenced` | requer auditoria técnica real |
| registro operacional de consentimentos | `not_evidenced` | especificação não é implementação |
| registro operacional de aceite de Termos | `not_evidenced` | idem |
| canal formal de direitos LGPD | `not_evidenced` | contato genérico não será presumido |
| Encarregado formalmente indicado | `not_evidenced` | nenhuma pessoa/empresa é nomeada pelo P6 |
| processo de incidente LGPD | `not_evidenced` | baseline regulatório existe; operação não comprovada |
| registro de incidentes com dados pessoais | `not_evidenced` | não inferir existência ou inexistência de incidentes |
| política operacional de retenção | `not_evidenced` | regras por atividade ainda precisam ser mapeadas |
| operadores/suboperadores vigentes | `not_evidenced` | fornecedores técnicos não devem ser inventados |
| transferências internacionais de dados | `not_evidenced` | expansão geográfica não prova transferência |
| RIPD/DPIA ou avaliação equivalente | `not_evidenced` | necessidade deve ser avaliada por tratamento |
| programa contínuo de privacy assurance | `not_evidenced` | futura maturidade OT7/OT8 |

## 7. Regras para fatos negativos

Ausência de evidência no GKR não equivale necessariamente à inexistência de um fato no mundo externo.

Usar:

- `not_evidenced`: não há evidência governada suficiente;
- `not_started`: há evidência de que a atividade formalmente ainda não iniciou;
- `not_implemented`: há autoridade/evidência explícita de não implementação;
- `not_applicable`: somente após análise justificar inaplicabilidade;
- `unknown`: o estado não pôde ser determinado.

Não converter `not_evidenced` em “não existe” sem fonte apropriada.

## 8. Ambiente e escopo

Um estado deve indicar ambiente quando pertinente.

```text
mockup
≠ protótipo
≠ desenvolvimento
≠ homologação
≠ produção
```

Um controle validado em homologação não pode ser descrito como produção.

Da mesma forma:

```text
Brasil
≠ Portugal
≠ União Europeia
≠ operação global
```

Conformidade ou publicação em uma jurisdição não deve ser propagada automaticamente para outra.

## 9. Terceiros e fornecedores

A existência de conta, contrato, SDK ou integração com terceiro deve ser evidenciada separadamente.

Para fornecedores que tratem dados pessoais, o estado operacional futuro poderá exigir:

- contrato vigente;
- função controlador/operador ou outra relação aplicável;
- finalidade;
- dados acessados;
- subcontratação;
- região/transferência;
- controles de segurança;
- retenção/encerramento;
- revisão periódica.

Nomear um fornecedor numa arquitetura candidata não prova contratação.

## 10. Controles de acesso e segurança

Afirmações como “criptografado”, “seguro”, “zero trust”, “backups ativos”, “MFA obrigatório” ou “auditado” precisam de escopo e evidência.

O GKR não deve usar adjetivos absolutos de segurança sem definição verificável.

Exemplo correto:

```text
controle: MFA para função X
ambiente: produção
estado: OT5
fonte: política + configuração + amostra de auditoria
```

Exemplo inválido:

```text
a Guivos é totalmente segura
```

## 11. Incidentes

Ausência de registro de incidente no GKR não autoriza afirmar “zero incidentes”.

Quando um processo de incidentes existir, devem ser separados:

- evento técnico;
- incidente de segurança;
- incidente envolvendo dados pessoais;
- incidente sujeito a avaliação de risco/dano;
- incidente comunicável;
- comunicação executada.

Cada classificação exige evidência própria.

## 12. Direitos dos titulares

Um futuro dashboard, formulário ou e-mail é somente uma superfície de entrada.

Operação de direitos exige cadeia ponta a ponta:

```text
recebimento
→ autenticação proporcional
→ triagem
→ localização de tratamentos
→ decisão
→ execução
→ propagação a derivados/terceiros quando aplicável
→ resposta
→ evidência
```

Somente a operação comprovada dessa cadeia sustenta OT5 ou superior.

## 13. Métricas futuras de assurance

Quando o P6 avançar para operação, métricas poderão incluir:

- cobertura do inventário de atividades;
- percentual de atividades com base jurídica revisada;
- cobertura de contratos com operadores;
- solicitações de titulares por tipo e prazo;
- cobertura de revisão de acessos;
- incidentes por classificação e tratamento;
- superfícies legais por estado LS;
- consentimentos/preferências com versão íntegra;
- tratamentos com retenção definida;
- fornecedores revisados;
- controles testados no período.

Meta futura não é resultado atual.

## 14. Regra de promoção do estado transversal

`GKR-STATE-001`, páginas públicas, pitches e documentos executivos somente poderão afirmar uma capacidade operacional quando o evidence ledger sustentar o estado correspondente.

Uma mudança de arquitetura pode ser integrada sem atualizar métricas operacionais.

Uma mudança de operação deve atualizar o registro de evidência e, quando material, o estado transversal.

## 15. Limites

Este registro:

- não armazena evidência sensível por padrão;
- não certifica conformidade;
- não substitui auditoria;
- não substitui documentação operacional detalhada;
- não declara fornecedores ou sistemas não evidenciados;
- não autoriza produção;
- não reduz obrigações legais a um checklist documental.
