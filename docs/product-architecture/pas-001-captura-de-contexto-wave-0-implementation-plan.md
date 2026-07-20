---
id: PAS-001-CC-W0-PLAN-001
title: Plano Executável da Onda 0 da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-UIC-001
related:
  - PAS-001-CC-UIC-READINESS-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-STORAGE-INDEX-001
  - PAS-001-CC-UIC-GUARDRAILS-ACCESS-001
  - PAS-001-CC-UIC-NFR-SECURITY-001
---

# PAS-001-CC-W0-PLAN-001 — Plano Executável da Onda 0

> **Estado:** `Draft 0.1.0 — Wave 0 implementation planned`.
>
> Este documento transforma o readiness técnico da UIC-01 em sequência executável. Não autoriza produção, lançamento, contratação automática de tecnologia ou flexibilização de guardrails.

## 1. Objetivo

Planejar uma implementação controlada e mínima da Captura de Contexto capaz de:

- comprovar o núcleo do domínio;
- executar contratos e schemas versionados;
- demonstrar persistência, idempotência e publicação confiável;
- separar registro funcional de conteúdo protegido;
- comprovar correção, revogação e reconstrução;
- aplicar finalidade, autoridade e minimização;
- produzir evidências dos cinco gates;
- permitir decisão separada sobre a próxima onda.

## 2. Estado de entrada

| Elemento | Estado de entrada |
|---|---|
| UIC-01 | Draft 0.5.0 |
| Maturidade | Technically ready for implementation |
| Readiness arquitetural | 100% |
| Implementação | não iniciada |
| Gaps arquiteturais | 0 abertos |
| Marco | M5.16 |

## 3. Estado de saída planejado

| Elemento | Estado de saída |
|---|---|
| UIC-01 | Draft 0.6.0 |
| Maturidade | Wave 0 implementation planned |
| Readiness arquitetural | 100% preservado |
| Implementação | 0% executada |
| Marco | M5.17 — Capture Context Wave 0 Implementation Planned |
| Próxima decisão | autorizar ADRs tecnológicos e execução controlada |

## 4. Princípios de execução

1. backlog não reinterpreta autoridade normativa;
2. tecnologia não define o domínio;
3. dependência não implica microsserviço;
4. conteúdo capturado é dado, não instrução de sistema;
5. Intelligence não confirma nem autoriza;
6. Platform Layer não cria autoridade funcional;
7. consumidor decide apenas em seu próprio domínio;
8. registro funcional prevalece sobre projeções, índices e caches;
9. evidência é produzida por execução reproduzível;
10. produção exige decisão posterior e independente.

## 5. Escopo da Onda 0

### 5.1 Incluído

- `CaptureRecord` e `CaptureSession`;
- identidade, autoria e representação;
- natureza da informação;
- confirmação, rejeição e contestação;
- autorização por finalidade, escopo e validade;
- persistência temporária e expiração;
- correção compensatória;
- revogação coordenada;
- comandos, respostas, eventos e schemas versionados;
- catálogo estável de erros;
- idempotência e concorrência;
- publicação confiável de eventos;
- consumidor mínimo controlado;
- reconstrução e replay;
- conteúdo protegido e referência multimodal mínima;
- indexação protegida mínima;
- observabilidade segura;
- auditoria minimizada;
- produção das evidências `EV-001` a `EV-018`.

### 5.2 Fora do escopo

- produto público completo;
- produção pública;
- todos os canais multimodais;
- busca semântica ampla;
- grafo global completo;
- automação integral pela Intelligence;
- todos os consumidores do ecossistema;
- operação internacional;
- arquitetura física definitiva de longo prazo;
- certificação regulatória;
- rollout comercial.

## 6. Incrementos

### W0-01 — Fundação do projeto

**Objetivo:** estabelecer estrutura, convenções, ambientes, pipeline, owners e forma de evidência.

**Entregáveis:**

- estrutura de implementação;
- convenções de branches e versionamento;
- pipeline mínimo;
- inventário de segredos;
- matriz de owners;
- template de evidência;
- registro inicial de riscos e exceções.

**Evidências prioritárias:** `EV-017`, `EV-018`.

### W0-02 — Núcleo de domínio

**Objetivo:** implementar agregado, invariantes, estados e decisões puras.

**Entregáveis:**

- `CaptureRecord`;
- `CaptureSession`;
- entidades e value objects;
- transições válidas e inválidas;
- erros de domínio;
- correção, revogação e replay em memória;
- testes determinísticos.

**Evidências prioritárias:** `EV-001`, `EV-002`.

### W0-03 — Contratos e persistência

**Objetivo:** executar contratos, persistir estado e publicar fatos com segurança contratual.

**Entregáveis:**

- comandos, respostas e eventos executáveis;
- validação de schemas;
- persistência transacional;
- controle otimista de concorrência;
- idempotência;
- publicação pós-persistência;
- matriz de compatibilidade.

**Evidências prioritárias:** `EV-003`, `EV-007`, `EV-015`.

### W0-04 — Dados protegidos e multimodalidade mínima

**Objetivo:** separar conteúdo do registro e comprovar retenção, integridade e descarte.

**Entregáveis:**

- referência protegida;
- hash e proveniência;
- retenção por classe;
- expiração;
- exclusão lógica, física ou criptográfica conforme camada;
- quarentena de mídia;
- backup e restore controlados.

**Evidências prioritárias:** `EV-008`, `EV-009`, `EV-016`.

### W0-05 — Acesso, correção e revogação

**Objetivo:** aplicar finalidade, autoridade e propagação verificável.

**Entregáveis:**

- decisão contextual de acesso;
- matriz de finalidade e autoridade;
- coordenação de correção;
- coordenação de revogação;
- tracking de consumidores;
- kill switch;
- auditoria administrativa minimizada.

**Evidências prioritárias:** `EV-004`, `EV-006`, `EV-012`, `EV-014`.

### W0-06 — Busca protegida mínima

**Objetivo:** localizar conteúdo autorizado sem ampliar escopo ou autoridade.

**Entregáveis:**

- política `prohibited`;
- indexação `metadata_only`;
- índice privado do participante;
- filtro de finalidade antes da recuperação;
- remoção após revogação;
- atualização após correção;
- snippet redigido;
- reconstrução de índice.

**Evidência prioritária:** `EV-010`.

### W0-07 — Segurança, observabilidade e resiliência

**Objetivo:** instrumentar SLIs, testar ameaças e comprovar recuperação.

**Entregáveis:**

- métricas, tracing e alertas;
- redaction de logs;
- testes adversariais;
- testes de prompt injection;
- teste de consumidor comprometido;
- carga inicial;
- restore e replay;
- runbooks C0/C1.

**Evidências prioritárias:** `EV-005`, `EV-011`, `EV-013`.

### W0-08 — Fechamento dos gates

**Objetivo:** consolidar evidências e decidir formalmente a conclusão da Onda 0.

**Entregáveis:**

- pacote versionado de evidências;
- relatório dos cinco gates;
- exceções aprovadas ou rejeitadas;
- riscos residuais atualizados;
- decisão de conclusão;
- proposta da próxima onda.

**Evidências:** consolidação de `EV-001` a `EV-018`.

## 7. Sequência e dependências

```text
W0-01
  ↓
W0-02
  ↓
W0-03
  ├──→ W0-04
  ├──→ W0-05
  └──→ W0-06
          ↓
        W0-07
          ↓
        W0-08
```

Regras:

- W0-04, W0-05 e W0-06 podem evoluir em paralelo após contratos estáveis;
- W0-07 começa parcialmente desde W0-01, mas fecha após integrações;
- W0-08 exige todos os incrementos anteriores;
- falha de gate bloqueia conclusão, não necessariamente aprendizado técnico;
- exceção não transforma item falho em item aprovado sem autoridade competente.

## 8. Critérios de entrada por incremento

| Incremento | Critério mínimo de entrada |
|---|---|
| W0-01 | plano aprovado |
| W0-02 | convenções, owners e ADR-TCC-001 em estado decidível |
| W0-03 | domínio estável e ADR-TCC-002/004 definidos |
| W0-04 | classificação de sensibilidade e ADR-TCC-003/007 definidos |
| W0-05 | identidade, autoridade e consumidores mínimos disponíveis |
| W0-06 | registro funcional estável e ADR-TCC-005 definido |
| W0-07 | fluxos integrados e SLIs instrumentáveis |
| W0-08 | evidências produzidas e riscos atualizados |

## 9. Critérios de saída por incremento

Cada incremento somente poderá ser encerrado quando:

- comportamento planejado existir;
- critérios de aceite estiverem executados;
- testes obrigatórios passarem;
- evidências forem armazenadas e versionadas;
- riscos novos forem registrados;
- exceções tiverem owner e expiração;
- documentação e contratos permanecerem coerentes;
- nenhuma autoridade tiver sido ampliada.

## 10. Gates

| Gate | Responsabilidade primária | Bloqueadores exemplares |
|---|---|---|
| Domínio | arquitetura de software e engenharia | transição sem cobertura, replay criando fato, autoridade ampliada |
| Dados | arquitetura de dados e segurança | conteúdo misturado ao registro, exclusão não comprovada, índice sem finalidade |
| Segurança | segurança e privacidade | vazamento cruzado, log proibido, abuso administrativo, prompt injection material |
| Qualidade | engenharia e qualidade | SLI ausente, recuperação não testada, defeito crítico sem aceite |
| Governança | arquitetura e governança Guivos | ADR ausente, risco sem owner, produção implícita |

## 11. Critérios de interrupção

Interromper o fluxo afetado quando houver:

- conflito com autoridade normativa;
- necessidade de reabrir decisão funcional;
- vazamento entre participantes;
- perda de rastreabilidade;
- impossibilidade de revogação;
- mistura entre conteúdo e registro funcional;
- segredo ou conteúdo sensível em log;
- tecnologia incapaz de cumprir requisito obrigatório;
- custo incompatível com a Onda 0;
- dependência crítica indisponível;
- risco crítico sem owner;
- expansão silenciosa de escopo;
- tentativa de uso como produção.

## 12. Registro obrigatório de interrupção

Toda interrupção deverá produzir:

1. identificador;
2. fato observado;
3. impacto;
4. requisito afetado;
5. decisão necessária;
6. alternativas;
7. owner;
8. evidência;
9. condição de retomada;
10. autoridade aprovadora.

## 13. Definition of Ready da execução

A execução da Onda 0 poderá começar somente quando:

- backlog estiver priorizado;
- dependências `required_before_build` estiverem disponíveis ou com fallback aprovado;
- ambientes mínimos estiverem definidos;
- ADRs tecnológicos bloqueantes estiverem decididos;
- owners dos cinco gates estiverem atribuídos;
- POCs tiverem hipóteses e critérios de sucesso;
- plano de evidências estiver aprovado;
- riscos críticos tiverem tratamento;
- produção estiver explicitamente fora do escopo.

## 14. Definition of Done da Onda 0

A Onda 0 somente estará concluída quando:

- implementação mínima existir;
- cinco gates forem executados;
- `EV-001` a `EV-018` forem produzidas ou formalmente excepcionadas;
- SLOs candidatos forem medidos;
- riscos residuais forem aceitos;
- nenhum bloqueio crítico permanecer;
- conclusão for aprovada por decisão separada;
- próxima onda não for iniciada automaticamente.

## 15. Limites

Este plano não autoriza:

- commit de código sem branch e revisão;
- uso de dados pessoais reais sem base específica;
- produção pública;
- lançamento;
- contratação automática de fornecedor;
- relaxamento de segurança, privacidade ou autoridade;
- promoção da Intelligence a decisor humano;
- declaração de conformidade operacional.