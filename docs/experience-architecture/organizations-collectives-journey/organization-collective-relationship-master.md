---
id: GKR-UX-ORG-COL-RELATIONSHIP-MASTER-001
title: Jornada de Organizações e Coletivos — Organização — Relação Organização–Coletivo — Documento Mestre
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: false
maturity: functional_contract_candidate
depends_on:
  - UXA-019
  - GKR-UX-COL-ORG-RELATIONSHIP-MASTER-001
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-ORG-004
  - GKR-SURF-ORG-005
  - GKR-SURF-ORG-006
  - GKR-SURF-COL-008
  - GKR-TRN-206
  - GKR-TRN-207
  - GKR-TRN-208
  - GKR-TRN-209
---

# Organização — Relação Organização–Coletivo — Documento Mestre

## 1. Responsabilidade

Este Master governa a perspectiva da Organização sobre o mesmo objeto bilateral Organização–Coletivo contratado por `UXA-019`, distribuído em três responsabilidades estáveis:

- `GKR-SURF-ORG-004` — proposta;
- `GKR-SURF-ORG-005` — avaliação e negociação;
- `GKR-SURF-ORG-006` — relação ativa e revisão.

`GKR-SURF-COL-008` permanece a perspectiva do Coletivo sobre esse mesmo objeto.

```text
ORG-004
≠ ORG-005
≠ ORG-006

MAS

ORG-004 + ORG-005 + ORG-006 + COL-008
→ PERSPECTIVAS / RESPONSABILIDADES DO MESMO OBJETO BILATERAL
```

Este Master não governa Organização↔Organização.

## 2. Objeto único e continuidade

A relação preserva uma única identidade lógica, finalidade, escopo, versão material, autoridades, compromissos, recursos, dados, limites, aprovações, proteção e histórico material.

Trocar de superfície não cria novo contrato, novo consentimento ou nova relação.

## 3. Cadeia estável

```text
GKR-SURF-ORG-004
↓ GKR-TRN-206
GKR-SURF-COL-008
↓ GKR-TRN-207
GKR-SURF-ORG-005
↓ GKR-TRN-208
GKR-SURF-ORG-006
↓ GKR-TRN-209
GKR-SURF-ORG-006
```

`GKR-TRN-206..209` permanecem `contratadas`. Nenhuma maturidade é promovida.

## 4. ORG-004 — Proposta

### 4.1 Job

Permitir que autoridade institucional legítima formule, revise, confirme e encaminhe uma proposta O↔C materialmente compreensível, ou a retire/cancele antes do efeito permitido pelo contrato.

### 4.2 Informação material

Conforme `UXA-019`, a proposta deve preservar os campos materiais exigidos pelos contratos governantes, incluindo quando aplicável:

- participantes e natureza da relação;
- finalidade e escopo;
- responsáveis e contatos operacionais;
- autoridades;
- compromissos e responsabilidades;
- recursos e condições comerciais;
- dados, consentimentos e limites;
- condições de marca/comunicação;
- critérios de evidência/acompanhamento;
- revisão e prazos;
- saída e disposição pós-encerramento;
- versão e proveniência.

Este Master não cria novos campos além das autoridades.

### 4.3 Confirmação

Criar, editar, visualizar ou salvar rascunho não envia proposta.

Envio material exige ação consciente e autoridade suficiente.

### 4.4 TRN-206

`TRN-206 ORG-004 → COL-008` disponibiliza ao Coletivo autorizado o mesmo objeto bilateral e a mesma versão material.

```text
ENVIAR PROPOSTA
≠ APROVAR PELO COLETIVO
≠ ATIVAR RELAÇÃO
```

## 5. ORG-005 — Avaliação e Negociação

### 5.1 Job

Permitir que a Organização compreenda a resposta/condições do Coletivo, avalie autoridade, capacidade, risco e coerência, negocie alterações e aprove ou recuse dentro de sua própria autoridade.

### 5.2 Entrada por TRN-207

`TRN-207 COL-008 → ORG-005` mantém o mesmo objeto bilateral.

A entrada deve preservar versão, proveniência e autoria material da contraparte. Não pode transformar resposta, pedido de informação ou contraproposta em aprovação.

### 5.3 Negociação

Alterações materiais devem ser explícitas, comparáveis à versão vigente quando necessário e submetidas a nova avaliação pelas partes afetadas.

Uma parte não pode editar silenciosamente a manifestação da outra.

### 5.4 Aprovação bilateral

Aprovação final exige autoridades legítimas aprovando a mesma versão material.

```text
APROVAÇÃO DA ORGANIZAÇÃO
≠ APROVAÇÃO BILATERAL

APROVAÇÃO DO COLETIVO
≠ APROVAÇÃO BILATERAL

VERSÕES DIFERENTES APROVADAS
≠ APROVAÇÃO BILATERAL
```

### 5.5 TRN-208

`TRN-208 ORG-005 → ORG-006` representa continuidade para relação ativa somente no limite já contratado e quando as precondições bilaterais aplicáveis estão satisfeitas.

Não declara implementação técnica de assinatura, pagamento, provisionamento ou integração.

## 6. ORG-006 — Relação Ativa e Revisão

### 6.1 Job

Permitir compreender e governar, dentro da autoridade bilateral, o estado da relação, compromissos, recursos, evidências, alterações, revisão, pausa, contestação, renovação e encerramento.

### 6.2 Escopo efetivo

Somente o escopo legitimamente aprovado é efetivo.

Alteração material pendente não substitui silenciosamente o escopo vigente.

### 6.3 TRN-209

`TRN-209 ORG-006 → ORG-006` preserva o mesmo objeto durante revisão, alteração e continuidade.

Nova versão material exige nova avaliação/aprovação bilateral antes de substituir a versão efetiva, salvo condição legítima de pausa, proteção ou encerramento aplicável.

### 6.4 Compromissos e recursos

Estado de compromisso ou recurso deve distinguir quando conhecido:

- previsto;
- pendente;
- cumprido/disponibilizado;
- atrasado;
- indisponível;
- contestado;
- indeterminado.

A superfície não fabrica execução financeira, entrega ou quitação.

### 6.5 Evidências, resultados e impacto

Evidência deve preservar fonte, escopo e força da afirmação.

```text
ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO

RELAÇÃO ATIVA
≠ IMPACTO COMPROVADO
```

## 7. Lifecycle bilateral preservado

O lifecycle corrente inclui:

- rascunho;
- proposta;
- avaliação bilateral;
- negociação;
- aguardando informação;
- aguardando consentimento/aprovação;
- aprovada pelas autoridades;
- ativa;
- em revisão;
- alteração material pendente;
- renovada ou ajustada;
- pausada;
- bloqueada por proteção ou privacidade;
- contestada;
- suspensa preventivamente;
- expirada;
- encerrada;
- encerrada com responsabilidades remanescentes.

## 8. Condições alternativas obrigatórias

Quando materialmente aplicáveis, devem permanecer distinguíveis:

- proposta recusada;
- autoridade insuficiente;
- aprovação divergente entre as partes;
- relação ativa sem atenção material;
- compromisso atrasado;
- recurso indisponível;
- dado ou consentimento ausente;
- conflito de interesse;
- denúncia em análise;
- suspensão urgente;
- renovação pendente;
- encerramento solicitado por uma das partes;
- risco ou condição de proteção;
- informação sensível protegida;
- evidência insuficiente;
- falha recuperável;
- estado indeterminado.

Ausência, falha ou proteção não deve ser convertida em recusa ou encerramento sem evidência.

## 9. Autoridade e autonomia

A Organização preserva sua autoridade; o Coletivo preserva a dele.

Relação, financiamento, patrocínio, plano, volume ou relevância percebida não transferem governança da contraparte.

A Organização não recebe acesso geral à governança interna, participantes ou dados do Coletivo por existir uma relação.

## 10. Alteração material

Mudanças materiais definidas por `UXA-019` exigem reavaliação e aprovação bilateral quando aplicável, incluindo mudanças de finalidade, público, dados, recursos/obrigações, exclusividade, autoridade, marca ou operação.

A versão anterior aprovada permanece a referência efetiva até substituição legítima.

## 11. Dados, consentimento e proteção

Somente o recorte necessário pode atravessar perspectivas.

Informação protegida pode limitar explicação ou continuidade sem autorizar fabricação de conclusão.

Condição especializada de proteção/moderação do Coletivo permanece sob `COL-007` quando aplicável.

## 12. Contestação e revisão

Contestar não produz retaliação automática, encerramento automático nem reversão automática.

Revisão preserva histórico material necessário, autoridade e versão.

## 13. Encerramento

Encerramento deve tratar no limite aplicável:

- dados;
- recursos;
- comunicação;
- compromissos;
- proteção;
- auditoria/proveniência;
- responsabilidades remanescentes.

`ENCERRADA` e `ENCERRADA COM RESPONSABILIDADES REMANESCENTES` não são equivalentes.

Solicitar encerramento não equivale a encerramento concluído.

## 14. Concorrência, versão e idempotência

Antes de ação material, a versão corrente deve ser revalidada.

Se a contraparte alterou materialmente o objeto, confirmação sobre versão anterior não aprova a nova.

Após falha ou resultado indeterminado, reconsultar estado canônico antes de repetir efeito potencialmente duplicável.

## 15. Retorno e navegação

Navegar, voltar, alternar contexto, abrir ou fechar uma superfície não:

- envia proposta;
- aprova;
- ativa;
- renova;
- pausa;
- encerra;
- transfere recurso;
- altera dados materialmente.

Retornos contextuais não exigem novo `GKR-TRN-*` sem evidência do Registry.

## 16. Planos

Planos não alteram autoridade bilateral, autonomia, peso de aprovação, proteção, evidência ou legitimidade de recusa.

## 17. Organização↔Organização

Relações Organização↔Organização permanecem sem ID estável dedicado.

Este Master não aplica `ORG-004..006`, `COL-008` ou `UXA-019` por analogia a esse domínio.

## 18. Design

Design possui liberdade criativa, mas não pode:

- fundir ORG-004/005/006 em responsabilidade indistinta;
- criar objetos bilaterais duplicados;
- ocultar versão material;
- converter visualização em aceite;
- converter negociação em ativação;
- representar alteração não aprovada como vigente;
- representar relação como impacto;
- ampliar o escopo para Organização↔Organização;
- inventar transições, scores ou autoridade;
- usar low-fidelity como baseline visual canônica.

## 19. IA — source lock

IA não pode inventar:

- campos obrigatórios além do que os contratos governantes exigem ou autorizam;
- critérios de aprovação;
- autoridade;
- pesos de decisão;
- lifecycle paralelo;
- transições;
- automações;
- métricas;
- efeitos técnicos/financeiros.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 20. Critérios de aceite

1. ORG-004, ORG-005 e ORG-006 mantêm responsabilidades distintas;
2. todas operam o mesmo objeto bilateral compartilhado com COL-008;
3. TRN-206..209 preservam origem, destino e maturidade;
4. envio não vira aprovação;
5. negociação não vira ativação;
6. aprovação bilateral exige mesma versão material;
7. alteração pendente não substitui escopo vigente;
8. autonomia e autoridade permanecem separadas;
9. contestação/proteção não geram retaliação automática;
10. encerramento solicitado não vira encerramento concluído;
11. relação não vira impacto;
12. Organização↔Organização permanece lacuna explícita.

## 21. Lacunas preservadas

Permanecem abertas:

- validação dedicada ponta a ponta de `TRN-206..209`;
- implementação técnica;
- assinatura/consentimento técnico;
- execução financeira;
- integrações;
- notificações técnicas;
- analytics/KPIs;
- Organização↔Organização.

## 22. Fechamento documental

```text
SURFACES GOVERNED
→ GKR-SURF-ORG-004
→ GKR-SURF-ORG-005
→ GKR-SURF-ORG-006

SHARED BILATERAL OBJECT
→ GKR-SURF-COL-008

STABLE TRANSITIONS
→ GKR-TRN-206..209
→ CONTRACTED / MATURITY PRESERVED

ORGANIZATION↔ORGANIZATION
→ EXPLICIT GAP / OUT OF SCOPE

NEW TRANSITION ID
→ NONE

NEW SURFACE ID
→ NONE

TECHNICAL IMPLEMENTATION
→ NOT CLAIMED

END-TO-END VALIDATION
→ NOT CLAIMED
```
