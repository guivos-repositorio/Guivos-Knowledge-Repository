---
id: GKR-JOURNEY-PERSON-FUNCTIONAL-COMPLETENESS-001
title: Jornada da Pessoa — Autoridade de Completude Funcional
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: true
maturity: functional_completeness_authority
depends_on:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-PLANS-PERSON-001
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-UX-COMMUNICATIONS-NOTIFICATIONS-001
related:
  - GKR-SURF-PER-003
  - GKR-SURF-PER-009
  - GKR-SURF-PER-108
  - GKR-SURF-PER-203
---

# Jornada da Pessoa — Autoridade de Completude Funcional

> **Reconciliação de autoridade — 2026-09-27**
>
> Para notificações, alertas e mecanismos de entrega prevalece `GKR-UX-COMMUNICATIONS-NOTIFICATIONS-001`. Menções anteriores a preferências de atualização/comunicação não constituem entitlement implementado nem controle executável enquanto não houver adjudicação específica.

## 1. Finalidade

Esta autoridade governa como a Guivos avalia a **completude funcional da Jornada da Pessoa**.

Ela não cria tela, superfície, transição, implementação ou identidade visual. Seu papel é impedir que a conclusão documental da coleção de Surface Masters seja confundida com prova de que toda capacidade legítima da Pessoa já possui ciclo funcional completo.

## 2. Regra fundamental

```text
26 / 26 SURFACE MASTERS BUILT
→ coleção documental prevista concluída

26 / 26
≠ todas as capacidades possíveis da Pessoa
≠ toda opção funcional já governada
≠ topologia definitivamente fechada
≠ implementação comprovada
```

A completude de inventário e a completude funcional são dimensões diferentes.

## 3. Capacidade não é tela

```text
CAPACIDADE
≠ TELA

AÇÃO
≠ NOVO PER-ID

ESTADO
≠ NOVA SUPERFÍCIE

CONTROLE
≠ NOVA TRANSIÇÃO
```

A menor unidade estrutural suficiente deve prevalecer.

Ordem de adjudicação:

1. estado ou controle interno de responsabilidade existente;
2. expansão legítima de responsabilidade existente;
3. transição, quando houver mudança real de responsabilidade;
4. nova superfície somente quando existir job próprio, estado próprio e continuidade que não caibam legitimamente nas responsabilidades atuais.

Nenhum novo `PER-ID` ou `TRN-ID` pode nascer apenas para completar layout, menu ou contagem.

## 4. Critério de completude por capacidade

Uma capacidade pode ser considerada funcionalmente completa quando, conforme aplicável, estiverem governados:

- origem e condição de disponibilidade;
- compreensão da ação;
- dados e autoridade necessários;
- escolha consciente;
- processamento ou mudança de estado;
- resultado;
- reversibilidade ou consequência;
- falha e recuperação;
- retorno/continuidade;
- privacidade e minimização;
- acessibilidade;
- limite de autoridade.

A ausência legítima de algum elemento deve ser explícita, não inventada.

## 5. Classificação

| Classe | Significado |
| --- | --- |
| A — completa | ciclo funcional suficientemente governado no escopo corrente |
| B — parcial | capacidade reconhecida, mas parte material do ciclo permanece aberta |
| C — lacuna funcional | capacidade legítima reconhecida sem continuidade/responsabilidade suficiente |
| D — limite de autoridade | responsabilidade posterior pertence legitimamente a terceiro ou outra autoridade |

## 6. Findings confirmados

### 6.1 Arquivo

`PER-003` reconhece Arquivo como modalidade em paridade, mas a continuidade downstream específica permanece não contratada.

```text
PER-003 / ARQUIVO
→ C — LACUNA FUNCIONAL
```

`PER-004` não absorve Arquivo por inferência.

A adjudicação posterior desta frente concluiu que a lacuna possui job, estados, captura material, falhas/recuperação, reversibilidade e handoff próprios. O contrato candidato `PER-013 — Captura e Revisão de Arquivo` governa `PER-003 / Arquivo → TRN-014 → PER-013 → TRN-015 → PER-005`, preservando `PER-005` como gate de autorização e `PER-006` como processamento posterior.

A remediação deve governar seleção, finalidade, revisão, remoção/substituição, falha, processamento autorizado e continuidade antes de qualquer implementação.

### 6.2 Perguntas Opcionais

`PER-003` reconhece Perguntas Opcionais como modalidade própria. Ela não é equivalente às perguntas adaptativas de apoio de `PER-004`.

```text
PER-003 / PERGUNTAS OPCIONAIS
→ C — LACUNA FUNCIONAL
```

A remediação deve preservar opcionalidade, possibilidade de pular/não saber/não informar, revisão, interrupção e continuidade consciente.

A adjudicação posterior desta frente concluiu que a lacuna possui job, estados, captura voluntária de respostas, revisão, falhas/recuperação, reversibilidade e handoff próprios. O contrato candidato `PER-014 — Perguntas Opcionais Guiadas` governa `PER-003 / Perguntas Opcionais → TRN-016 → PER-014 → TRN-017 → PER-005`, preservando `PER-004` para Texto/Voz, `PER-005` como gate de autorização e `PER-006` como processamento posterior.

### 6.3 Salvar oportunidade

`PER-203` reconhece Salvar para considerar como alternativa legítima quando autorizada e seu contrato corrente passa a governar preservação, confirmação, consulta posterior, remoção e tratamento de mudança, expiração ou indisponibilidade, sem criar novo handoff.

```text
SALVAR
→ B — PARCIAL
→ NÃO EXIGE NOVA SUPERFÍCIE POR PADRÃO
```

Salvar não significa inscrição, reserva, compra, prioridade, resultado ou aceite de publicidade.

A adjudicação concluiu que Salvar permanece controle/estado de `PER-203`. Uma futura responsabilidade para organizar múltiplos itens salvos só poderá ser criada se um job próprio for comprovado; não é inferida deste contrato.

### 6.4 Comparar oportunidades

`PER-203` reconhece Comparar e seu contrato corrente passa a governar seleção contextual, dimensões comparáveis, dados ausentes, remoção e retorno, sem criar superfície ou transição.

```text
COMPARAR
→ B — PARCIAL
→ NOVA SUPERFÍCIE NÃO ADJUDICADA
```

A adjudicação concluiu que Comparar permanece capacidade/estado contextual de `PER-203`. Persistência entre sessões, coleção comparativa permanente, histórico e sincronização não são presumidos; somente evidência futura de job próprio poderá justificar nova responsabilidade.

Comparação não produz vencedor universal.

### 6.5 Controles do vínculo com Coletivos

`PER-108` reconhece, conforme autoridade corrente:

- preferências de atualização — somente como necessidade conceitual/comercial ainda não adjudicada para execução;
- pausa;
- saída;
- proteção;
- denúncia ou contestação;
- consulta ao estado do vínculo.

Esses controles não justificam superfícies separadas por padrão.

```text
CONTROLES DE VÍNCULO
→ B — PARCIAIS
→ CONTRATOS FUNCIONAIS A FECHAR
```

Cada controle material deve governar consequência, confirmação proporcional ao risco, processamento, resultado, recuperação e estado atualizado do vínculo.

A adjudicação desta frente concluiu que consulta do vínculo, pausa/retomada, saída e contestação podem permanecer controles/estados de `PER-108`, sem novo `PER-ID` ou `TRN-ID`. Preferências de atualização não são controle executável corrente e permanecem sujeitas à autoridade transversal de comunicações/notificações. Proteção/denúncia pode ter acesso contextual a partir de `PER-108`, mas triagem, evidências, investigação, acompanhamento, resolução ou recurso pertencem a processo especializado ainda não adjudicado e não podem ser absorvidos por inferência.

### 6.6 Conta / controles da Pessoa

`PER-009` permanece deliberadamente estreita e não define arquitetura total de Conta.

A autoridade de Planos da Pessoa, porém, já registra capacidades como controles de dados, permissões, correção, exportação, exclusão e saída, além de níveis de histórico, alertas e exportação.

```text
PER-009
→ ESCOPO CORRENTE VÁLIDO
→ ARQUITETURA TOTAL DE CONTA NÃO DEFINIDA

PLANOS → CAPACIDADES PROMETIDAS
JOURNEY → LOCALIZAÇÃO/CICLO DE PARTE DESSAS CAPACIDADES AINDA NÃO CONSOLIDADOS
```

A remediação deve primeiro distinguir capacidades e autoridades; não transformar a lista de lacunas de `PER-009` em menu por inferência.

A adjudicação desta frente mantém autenticação, recuperação e variantes de sessão em `PER-002`; mantém correção contextual junto ao objeto quando houver autoridade própria; e localiza em `PER-009` os ciclos administrativos transversais de dados/permissões, exportação, exclusão e saída da Guivos. Isso não cria menu universal, Central de Privacidade, novo `PER-ID` ou novo `TRN-ID`. Notificações/alertas, níveis de histórico, integrações e demais diferenciações comerciais permanecem para a reconciliação Planos × Journey.

## 7. Capacidades que não justificam nova superfície por si

### 7.1 Autenticação e recuperação

`PER-002` já admite como estados internos autenticação necessária, sessão autenticada, recuperação de acesso, sessão expirada e falha recuperável.

Método técnico, provedor de identidade, MFA e sessão técnica permanecem decisões de implementação/segurança, não novas superfícies por inferência.

### 7.2 Histórico

Histórico pode permanecer distribuído pelas responsabilidades que o produzem, como Hoje, Objetivos, Próximos Passos e Evolução.

A existência de níveis comerciais de histórico não cria automaticamente uma Central de Histórico.

### 7.3 Compartilhamento

Compartilhamento deve permanecer contextual quando a autoridade do objeto permitir. A Pessoa deve compreender destinatário, finalidade e escopo quando houver compartilhamento autorizado.

### 7.4 Privacidade e direitos

Consentimento, preferência, aceite contratual e direitos do titular são objetos distintos.

Centros de preferências e superfícies de direitos devem derivar de tratamentos e autoridades reais. Não devem ser criados como elementos decorativos ou por template.

### 7.5 Busca e descoberta

Busca, região, filtros, revisão, remoção de filtros, mapa/lista, zero results e recuperação já pertencem às responsabilidades de descoberta de oportunidades. Salvar e Comparar permanecem findings separados.

## 8. Distinções obrigatórias

```text
EXCLUSÃO DE COMPREENSÃO
≠ EXCLUSÃO DE DADO
≠ EXCLUSÃO DE CONTA

SAÍDA DE COLETIVO
≠ SAÍDA DA GUIVOS
≠ CANCELAMENTO DE PLANO

PREFERÊNCIA DE COMUNICAÇÃO
≠ CONSENTIMENTO
≠ VÍNCULO
≠ OBRIGAÇÃO MATERIAL

AUTENTICAÇÃO
≠ CONSENTIMENTO
≠ AUTORIZAÇÃO DE PROCESSAMENTO
≠ AUTORIDADE FINANCEIRA
```

## 9. Limites externos e técnico-operacionais

Não constituem automaticamente novas superfícies da Pessoa:

- processos posteriores a `BND-001`;
- gateway;
- fiscal;
- proration/estorno;
- processamento financeiro real;
- entitlement;
- persistência técnica;
- provedor de identidade;
- infraestrutura de sessão e segurança.

Esses itens exigem autoridades próprias quando materialmente necessários.

## 10. Regra para Planos × Journey

Toda capacidade comercial prometida em `GKR-PLANS-PERSON-001` deve possuir rastreabilidade funcional suficiente para uma responsabilidade, estado ou controle da Journey antes de ser tratada como experiência pronta para execução.

```text
CAPACIDADE NO PLANO
≠ EXPERIÊNCIA IMPLEMENTADA

CAPACIDADE NO PLANO
→ DEVE TER RESPONSABILIDADE FUNCIONAL LOCALIZÁVEL
```

Divergências devem ser resolvidas sem inventar capacidade, preço, entitlement ou superfície.

A reconciliação da sexta frente localiza responsabilidades para entrada/compreensão, jornada essencial, descoberta, filtros, histórico distribuído, controles administrativos e Salvar. Diferenciações de cotas/uso justo/profundidade de correspondências, níveis de exportação, alertas/lembretes/acompanhamento ampliado, níveis de Intelligence/processamento, integrações, relatórios pessoais, suporte e acesso antecipado permanecem benefícios comerciais cuja execução depende das autoridades específicas de entitlement/capacidade quando necessárias. A ausência dessas autoridades não autoriza inventar comportamento, limite, menu, superfície ou disponibilidade.

```text
PLANOS × JOURNEY
→ RASTREABILIDADE FUNCIONAL RECONCILIADA
→ DIFERENCIAÇÕES NÃO CONTRATADAS EXPLICITAMENTE LIMITADAS
→ NOVO PER-ID = NONE
→ NOVO TRN-ID = NONE
→ PRODUCT ENGINEERING = NOT RELEASED
```

## 11. Sequência de remediação

A existência desta autoridade não autoriza automaticamente mutações subsequentes.

Frentes confirmadas para adjudicação/remediação própria:

1. Arquivo;
2. Perguntas Opcionais;
3. Salvar / Comparar oportunidades;
4. controles do vínculo com Coletivos;
5. Conta / controles da Pessoa;
6. coerência Planos × Journey.

Cada frente deve preservar os Masters existentes sempre que a responsabilidade atual for suficiente.

## 12. Estado governado

```text
ORIGINAL SURFACE MASTER COLLECTION
→ 26 / 26 BUILT

FUNCTIONAL COMPLETENESS AUDIT
→ MATERIAL FINDINGS ADJUDICATED

REMEDIATION FRONTS
→ 6 / 6 TREATED

CURRENT PERSON RESPONSIBILITIES IN REGISTRY
→ 29
→ PER-001 + ORIGINAL 26 + PER-013 / PER-014 POST-AUDIT EXTENSIONS

REMAINING MATERIAL C-GAP FROM THE SIX FRONTS
→ NONE

EXPLICIT BOUNDARIES / OPEN IMPLEMENTATION GAPS
→ PRESERVED WHERE DOCUMENTED

NEW PER-IDS
→ NONE BY THIS AUTHORITY

NEW TRN-IDS
→ NONE BY THIS AUTHORITY

NEW VISUAL SURFACES
→ NONE BY THIS AUTHORITY

PRODUCT ENGINEERING
→ NOT RELEASED
```
