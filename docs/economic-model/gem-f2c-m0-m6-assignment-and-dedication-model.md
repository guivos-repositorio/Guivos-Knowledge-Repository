---
id: GEM-F2C-M0-M6-ASSIGNMENT-DEDICATION-001
title: Matriz de Assignment e Dedicação M0–M6 — F2-C
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-010
depends_on:
  - GEM-F2-M0-M6-CAPACITY-HEADCOUNT-BASELINE-001
  - GEM-F2B-M0-M6-PEOPLE-DELIVERY-COST-001
  - GEM-F1-M0-M6-COST-BASELINE-001
  - GEM-008-CAPACITY-AND-SATURATION-MODEL-001
  - GEM-008-GROWTH-AND-CAPACITY-GATES-001
  - GEM-009-CAPACITY-AND-QUALITY-METRICS-001
  - GEM-010-OPERATING-DRIVER-MODEL-001
  - GTM-001
  - GTM-002
related:
  - GEM-010-COST-AND-CAPACITY-MODEL-001
  - GEM-F1B-M0-M6-COST-CALIBRATION-001
normative: true
---

# Matriz de Assignment e Dedicação M0–M6 — F2-C

## 1. Finalidade

Converter as capacidades e modos de entrega já governados por F2 e F2-B em uma **arquitetura de assignment e dedicação para M0–M6**, suficiente para identificar concentração, dupla contagem e sobrecarga antes de qualquer contratação ou cálculo de custo mensal.

F2-C responde a cinco perguntas:

1. qual escopo funcional é owner primário de cada capacidade;
2. quais capacidades podem ser compartilhadas com um RE dedicado;
3. quanto de capacidade pode ser comprometido sem apagar o mandato principal;
4. quando uma sobreposição deixa de ser aceitável e exige capacidade adicional;
5. quais assignments permanecem condicionais, externos ou bloqueados.

F2-C **não nomeia pessoas, não cria vagas, não escolhe CLT/PJ, não aprova remuneração, não define organograma definitivo, não ativa Product Engineering e não calcula burn, runway ou necessidade de capital**.

## 2. Regra central: assignment não é pessoa

O modelo separa:

```text
capacidade funcional
→ owner_scope
→ resource_scope candidato
→ allocation_fraction / planning band
→ capacity conflict check
→ delivery mode
→ valor econômico somente em camada posterior
```

Consequências:

- `owner_scope` é responsabilidade funcional, não nome de empregado;
- um RE dedicado não equivale automaticamente a uma pessoa física;
- uma mesma pessoa física somente poderá cobrir múltiplos scopes se a soma de suas alocações permanecer sustentável;
- dois RE dedicados não podem ser considerados integralmente cobertos pela mesma pessoa ao mesmo tempo sem divisão explícita de capacidade;
- cobertura compartilhada não elimina necessidade de owner;
- founder coverage não autoriza custo zero;
- allocation não autoriza contratação ou remuneração.

## 3. Estados de assignment

| Estado | Significado |
|---|---|
| `assigned_to_dedicated_role_scope` | owner primário é um dos RE dedicados já governados |
| `shared_assignment` | capacidade deve ser coberta por scope compartilhado e pode consumir fração de RE existente |
| `fractional_specialist_assignment` | owner operacional depende de especialista fracionário/externo |
| `conditional_assignment` | assignment nasce somente quando contrato, lançamento, evento ou volume aciona a capacidade |
| `partner_enabled_assignment` | capacidade pode ser habilitada por relação de parceria, sem transferir governança |
| `blocked_by_product_engineering` | assignment de implementação continua bloqueado |
| `assignment_TBD` | owner/cobertura ainda não pode ser fechado |

## 4. Estados de dedicação

| Estado | Significado |
|---|---|
| `candidate_planning_band` | faixa de planejamento usada como guardrail; não é medição real |
| `allocation_required` | owner definido, fração ainda precisa ser definida por recurso/período |
| `observed_allocation` | fração observada em operação real |
| `contracted_allocation` | dedicação sustentada por contrato/escopo |
| `actual_allocation` | dedicação reconciliada com execução real |
| `not_applicable` | não aplicável ao período com evidência |
| `TBD` | insuficiência de evidência |

As faixas deste F2-C são **parâmetros candidatos de planejamento**, não thresholds operacionais comprovados.

## 5. Contrato mínimo de assignment

```yaml
capacity_id: F2-Rxx
period: M0..M6
owner_scope: string
resource_scope: string_or_TBD
assignment_state: string
delivery_mode_candidate: string_or_TBD
core_or_secondary: core | secondary | shared | specialist | conditional | blocked
allocation_fraction: number_or_TBD
allocation_band: string_or_TBD
planning_load_state: reserve_preserved | reserve_consumed | overallocated | not_assessed
capacity_conflict_check: pass | conditional | fail | TBD
source: authority_or_evidence
notes: string
```

Nenhum registro de assignment produz custo monetário sem cumprir os requisitos de F2-B.

## 6. Guardrails candidatos de utilização

Para os três RE dedicados `F2-R01`, `F2-R02` e `F2-R03`, F2-C institui os seguintes guardrails de planejamento:

```yaml
core_allocation_floor: 0.65
planned_assigned_load_ceiling: 0.85
minimum_uncommitted_slack: 0.15
single_secondary_capacity_soft_ceiling: 0.20
```

Interpretação:

1. ao menos **65%** da capacidade planejada de um RE dedicado deve permanecer no mandato central;
2. a soma de alocações planejadas de um recurso não deve exceder **85%** sem revisão explícita, preservando 15% de folga para pico, recuperação, retrabalho e variabilidade;
3. uma única capacidade secundária acima de **20%** exige revisão de concentração e desenho funcional;
4. soma acima de `1.00` para o mesmo recurso é `overallocated` e invalida o plano;
5. faixa entre `0.85` e `1.00` consome a folga e exige `capacity_review_required` antes de expansão;
6. os percentuais são guardrails candidatos de planejamento e deverão ser recalibrados com dados observados.

Esses guardrails não alteram os estados operacionais do GEM-008. Servem apenas como **sinal preventivo**.

## 7. Consequência matemática para sobreposição entre RE dedicados

Se dois RE dedicados exigem, cada um, piso de 65% no mandato principal:

```text
0.65 + 0.65 = 1.30
```

Logo, **uma única pessoa física não pode ser tratada como cobertura integral simultânea de dois RE dedicados** sob esta baseline.

Se uma pessoa vier a cobrir partes de dois RE:

- as frações deverão ser explicitadas;
- pelo menos um dos RE ficará abaixo da cobertura dedicada plena;
- a lacuna deverá ser coberta por outro recurso, contractor, parceiro habilitador ou redução de escopo;
- o plano não poderá contar `2 RE` quando existe menos de `2 RE` de capacidade real.

## 8. Assignment primário dos três RE dedicados

| RE | Owner scope primário | Estado | Mandato principal | Faixa central candidata |
|---|---|---|---|---|
| F2-R01 | `growth_gtm_scope` | assigned_to_dedicated_role_scope | liderança Growth/GTM, aquisição, posicionamento, coordenação de crescimento | 0.65–0.85 |
| F2-R02 | `institutional_commercial_business_scope` | assigned_to_dedicated_role_scope | comercial institucional, Organizações e Guivos Business | 0.65–0.85 |
| F2-R03 | `ecosystem_partnerships_scope` | assigned_to_dedicated_role_scope | Coletivos, ecossistema e Parcerias Estratégicas | 0.65–0.85 |

A faixa não significa que cada RE deva consumir 85% em todos os meses. O valor mensal será definido somente no registro de capacidade do período.

## 9. Matriz de assignment das 18 capacidades

| ID | Capacidade | Owner scope primário | Cobertura secundária admissível | Estado F2-C |
|---|---|---|---|---|
| F2-R01 | liderança Growth/GTM | growth_gtm_scope | governança executiva quando compatível | assigned_to_dedicated_role_scope |
| F2-R02 | comercial institucional + Guivos Business | institutional_commercial_business_scope | CS/implantação institucional | assigned_to_dedicated_role_scope |
| F2-R03 | ecossistema + Parcerias Estratégicas | ecosystem_partnerships_scope | operação/onboarding e campo | assigned_to_dedicated_role_scope |
| F2-R04 | conteúdo e marketing | growth_gtm_scope | contractor/shared execution | shared_assignment |
| F2-R05 | operação local, onboarding e ativação BH | ecosystem_partnerships_scope | institutional_commercial_business_scope para contas institucionais | shared_assignment |
| F2-R06 | suporte e atendimento | shared_operations_support_scope | R02/R03 somente como cobertura transitória e mensurada | shared_assignment |
| F2-R07 | Customer Success / implantação institucional | institutional_commercial_business_scope | ecosystem_partnerships_scope para onboarding de ecossistema | conditional_assignment |
| F2-R08 | moderação, curadoria, trust & safety e fraude | shared_trust_safety_scope | external specialist quando risco exigir | shared_assignment |
| F2-R09 | finanças, administração e controles | founder_or_shared_admin_scope | external specialist | shared_assignment |
| F2-R10 | contabilidade e fiscal | accounting_tax_specialist_scope | none | fractional_specialist_assignment |
| F2-R11 | jurídico, privacidade e compliance | legal_privacy_compliance_scope | none | fractional_specialist_assignment |
| F2-R12 | segurança e risco especializado | security_risk_specialist_scope | shared internal coordination | fractional_specialist_assignment |
| F2-R13 | governança executiva e decisões de escopo | founder_executive_governance_scope | R01 somente se o mesmo recurso estiver formalmente alocado | shared_assignment |
| F2-R14 | produto/design/UX — coordenação documental | product_ux_governance_scope | founder/shared/contractor | shared_assignment |
| F2-R15 | engenharia/plataforma — implementação | none | none | blocked_by_product_engineering |
| F2-R16 | dados/IA/analytics — implementação | none | none | blocked_by_product_engineering |
| F2-R17 | eventos/presença de campo BH | ecosystem_partnerships_scope | shared operations / partner enabled | conditional_assignment |
| F2-R18 | compras/vendors/integrações operacionais | shared_operations_vendor_scope | ecosystem_partnerships_scope / external specialist | conditional_assignment |

## 10. Bandas candidatas para capacidades secundárias

As bandas abaixo servem para testar absorção por RE dedicado **sem afirmar que a carga real já foi medida**.

### M0–M3 — preparação

| Capacidade secundária | Owner primário | Banda candidata quando absorvida pelo mesmo recurso |
|---|---|---:|
| conteúdo/marketing — coordenação | R01 | 0.10–0.20 |
| operação/onboarding BH | R03 | 0.10–0.20 |
| CS/implantação institucional | R02 | 0.00–0.15, condicional a contrato/piloto |
| governança executiva | founder scope / R01 se coincidente | 0.10–0.20 |
| produto/UX documental | product governance scope | 0.10–0.20 |
| eventos/campo | R03 | 0.00–0.10, condicional |
| vendors/integrações operacionais | shared/R03 | 0.00–0.10, condicional |

### M4–M6 — lançamento BH

| Capacidade secundária | Owner primário | Banda candidata quando absorvida pelo mesmo recurso |
|---|---|---:|
| conteúdo/marketing — coordenação | R01 | 0.15–0.20 |
| operação/onboarding BH | R03 | 0.15–0.20 |
| CS/implantação institucional | R02 | 0.10–0.20 |
| governança executiva | founder scope / R01 se coincidente | 0.10–0.20 |
| produto/UX documental | product governance scope | 0.05–0.15 |
| eventos/campo | R03 | 0.05–0.15, quando ativado |
| vendors/integrações operacionais | shared/R03 | 0.05–0.10, quando ativado |

### Regra de combinação

Bandas não são somadas automaticamente. Se o mesmo recurso for proposto para duas ou mais linhas, deverá existir uma instância mensal que demonstre:

```text
core allocation
+ secondary allocations
+ shared allocations aplicáveis
<= 0.85 planejado
```

Se isso não for possível, o desenho exige capacidade adicional, redução de escopo ou reatribuição.

## 11. Coberturas compartilhadas não presumidas dentro dos 3 RE

F2-C **não presume** que as seguintes capacidades caibam dentro dos três RE dedicados:

- suporte/atendimento;
- moderação/trust & safety/fraude;
- finanças/admin quando material;
- contabilidade/fiscal;
- jurídico/privacidade/compliance;
- segurança/risco especializado;
- execução de conteúdo/marketing;
- execução de eventos/campo;
- trabalho especializado de vendors/integrações.

Essas capacidades possuem owner scope, mas sua quantidade de recurso continua `allocation_required`, `quote_required` ou condicional conforme F2-B/F1.

## 12. Pool de capacidade adjacente dos três RE

Com os guardrails deste F2-C:

```text
por RE dedicado:
0.65 core mínimo
+ até 0.20 de carga secundária planejada
+ 0.15 de folga mínima
= 1.00 de capacidade
```

Portanto, a absorção planejada máxima de capacidades secundárias **dentro dos três RE**, preservando o piso central e a folga, é de até:

```text
3 × 0.20 = 0.60 RE-equivalent de carga secundária agregada
```

Esse `0.60` é **envelope máximo de absorção planejada**, não headcount disponível, não prova de capacidade real e não autorização para distribuir 0.60 automaticamente.

Qualquer demanda compartilhada que não caiba nesse envelope deverá aparecer como capacidade adicional, externa, fracionária, condicional ou não coberta.

## 13. Concentração e single-point-of-failure

Um recurso deverá receber `capacity_conflict_check: conditional` ou `fail` quando ocorrer qualquer uma das condições abaixo:

- dois mandatos dedicados sendo contabilizados como integrais sobre a mesma capacidade física;
- soma planejada acima de 0.85 sem plano de contingência;
- soma acima de 1.00;
- função protetiva sem backup ou especialista acessível;
- founder scope concentrando Growth/GTM, governança, produto e operação acima do limite planejado;
- comercial acumulando venda, implantação e suporte de forma que degrade pipeline ou atendimento;
- ecossistema acumulando parcerias, onboarding, campo e vendors acima da capacidade;
- ausência de owner alternativo para atividade crítica em M4–M6.

Concentração não gera contratação automática; gera **gate de revisão**.

## 14. Gate mensal de assignment

Antes de cada mês M0–M6, o registro deverá responder:

1. quais capacidades estão ativas no mês;
2. qual owner scope responde por cada uma;
3. qual recurso/scope executará a cobertura;
4. qual dedicação é planejada ou contratada;
5. a soma por recurso preserva folga;
6. existe dupla contagem entre RE, shared coverage e especialista externo;
7. existe cobertura para ausência, pico ou incidente material;
8. o capacity status é compatível com crescimento pretendido.

Resultado mensal:

- `assignment_ready`;
- `assignment_conditioned`;
- `assignment_constrained`;
- `assignment_blocked`.

## 15. Gate específico antes de M4

O lançamento BH não deve avançar somente porque o calendário chegou a M4.

Antes de M4, deve existir instância documentada para:

- R01, R02 e R03 com owner scope e recurso identificável;
- conteúdo/marketing com execução definida;
- operação/onboarding com capacidade demonstrável;
- suporte/atendimento com owner e capacidade;
- moderação/trust & safety com owner;
- finanças/admin com cobertura;
- jurídico/privacidade/compliance aplicável;
- segurança/risco aplicável;
- governança executiva;
- contingência para concentração crítica.

Se a única forma de fechar a matriz for alocar um mesmo recurso acima de 0.85 ou contar duas vezes a mesma capacidade, o gate será `assignment_constrained` ou `assignment_blocked`.

## 16. Relação com F2-B e F1-C05

Após F2-C, `F1-C05` pode ser descrito como:

> `partially_parameterized_by_F2B_F2C — delivery modes and market benchmarks exist; owner scopes, overlap guardrails and dedication planning bands are defined; named resources, exact monthly allocations, regime, compensation, benefits and quotes remain pending`.

Isso reduz a incerteza de dimensionamento, porém **não fecha o custo mensal de pessoas**.

Para um valor mensal de F1-C05 ainda são necessários:

1. resource assignment real/candidato por mês;
2. delivery mode escolhido por assignment;
3. fração mensal exata dentro das bandas ou justificativa de exceção;
4. remuneração/fee/cotação sustentada;
5. componentes acessórios aplicáveis;
6. reconciliação de dupla contagem com outros pools.

## 17. O que F2-C não autoriza

F2-C não autoriza:

- contratar três pessoas;
- contratar qualquer pessoa;
- afirmar que uma pessoa específica já ocupa R01, R02 ou R03;
- publicar organograma;
- fixar jornada de trabalho individual;
- definir salário, pró-labore, fee, comissão ou benefício;
- escolher regime jurídico de contratação;
- transformar 0.60 RE em headcount;
- tratar 0.85 como produtividade comprovada;
- iniciar Product Engineering/W0-01;
- calcular custo completo, burn, runway ou capital necessário.

## 18. Resultado F2-C

| Gate | Resultado |
|---|---|
| owner scopes das 18 capacidades | PASS |
| owner primário dos três RE | PASS |
| regra de dupla contagem de RE | PASS |
| bandas de dedicação secundária | PASS — candidate planning bands |
| folga operacional planejada | PASS — guardrail candidato de 15% |
| envelope adjacente dos três RE | PASS — até 0.60 RE de carga, não HC |
| shared/specialist assignments | PARTIAL — owner definido; quantidade/quote pendente |
| resource assignment nominal | PENDING |
| fração mensal exata por recurso | PENDING |
| delivery mode efetivamente escolhido | PENDING |
| remuneração/fee real | PENDING |
| custo mensal completo F1-C05 | NOT CALCULABLE |
| burn/runway/capital | NOT CALCULABLE |

**Parecer:** `PARTIAL PASS — F2-C defines role-scope assignment, overlap constraints and candidate dedication guardrails for M0–M6 without converting role-equivalents into people or planning fractions into headcount; named resources, exact monthly allocations and monetary decisions remain pending.`

## 19. Próximo incremento permitido

Após integração de F2-C, o próximo incremento econômico recomendado é:

**F1-C — evidências e cotações materiais ainda faltantes**, incluindo os pools sem valor suficiente e as cotações necessárias para transformar assignments admissíveis em linhas econômicas sustentadas.

F3 — caixa, capital de giro e necessidade de capital permanece bloqueado até cobertura monetária material suficiente de F1/F2.
