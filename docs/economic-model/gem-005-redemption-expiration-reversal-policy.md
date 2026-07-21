---
id: GEM-005-REDEMPTION-EXPIRATION-REVERSAL-POLICY-001
title: Política de Resgate, Expiração e Reversão
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Política de Resgate, Expiração e Reversão

## 1. Objetivo

Estabelecer limites conceituais para utilização, encerramento e correção de recompensas futuras, preservando transparência, disponibilidade, contestação e histórico.

## 2. Resgate

Todo resgate futuro deverá informar:

- benefício;
- fornecedor;
- condição de elegibilidade;
- quantidade futura necessária;
- disponibilidade;
- prazo;
- território;
- restrições;
- responsabilidade pela entrega;
- dados compartilhados;
- cancelamento;
- substituição;
- confirmação final;
- dependências jurídicas, fiscais ou regulatórias.

## 3. Regras de resgate

O resgate não deverá:

- exigir compra adicional não divulgada;
- utilizar preço de referência artificial;
- ocultar indisponibilidade;
- permitir uso duplicado;
- criar saldo negativo sem consentimento e regra específica;
- expor dados além do necessário;
- alterar reconhecimento ou evidência;
- transformar recompensa em dívida da pessoa;
- impedir contestação;
- utilizar confirmação enganosa.

## 4. Reserva de saldo

Durante o resgate, a reserva deverá:

- indicar quantidade e benefício;
- possuir identificador;
- impedir duplo uso;
- possuir expiração própria;
- ser liberada quando a entrega falhar;
- não constituir entrega final;
- manter rastreabilidade.

## 5. Confirmação de entrega

A entrega poderá exigir, conforme risco:

- confirmação do parceiro;
- confirmação do participante;
- evento de sistema;
- documento;
- evidência múltipla.

A confirmação deverá ser proporcional e não coletar dados excessivos.

## 6. Indisponibilidade

Quando o benefício não estiver disponível:

- não deverá ser reservado como disponível;
- a pessoa deverá ser informada;
- saldo reservado deverá ser liberado;
- substituição equivalente poderá ser proposta futuramente;
- nenhuma substituição será automática sem regra;
- o responsável deverá ser registrado;
- incidentes recorrentes poderão suspender o parceiro ou benefício.

## 7. Expiração

A expiração somente será admissível quando existir fundamento legítimo, como:

- encerramento de campanha;
- validade do benefício do parceiro;
- término de programa vinculado;
- prevenção de responsabilidade indefinida;
- condição operacional ou contratual futura;
- risco devidamente registrado.

## 8. Requisitos de expiração

- regra anterior à emissão;
- data ou condição compreensível;
- visibilidade no saldo;
- aviso proporcional;
- acesso ao histórico;
- tratamento de indisponibilidade;
- contestação de erro;
- preservação de progresso e reconhecimento.

Não será admissível expiração surpresa ou criada retroativamente.

## 9. Reversão

Poderá ocorrer por:

- emissão incorreta;
- duplicidade;
- evento cancelado;
- compra devolvida;
- chargeback;
- fraude comprovada;
- evidência materialmente inválida;
- resgate não concluído;
- violação objetiva de regra anterior.

## 10. Reversões não admissíveis

- mudança retroativa arbitrária;
- crítica ou reclamação legítima;
- término de vínculo sem relação com o evento;
- recusa de publicidade;
- decisão exclusivamente automatizada em caso material sem revisão adequada;
- ausência de atividade posterior;
- expiração do patrocinador sobre benefício já legitimamente constituído e coberto.

## 11. Registro de reversão

```yaml
reversal_id: string
reward_issue_id: string
reason_code: string
reason_description: string
evidence:
  - string
authority: string
occurred_at: datetime
quantity_affected: number | null
monetary_value_defined: false
related_event: string | null
appeal_available: true
status: string
```

## 12. Saldo insuficiente após reversão

Cenário em que a recompensa já foi utilizada deverá ser tratado futuramente sem criar automaticamente dívida financeira.

Opções conceituais para avaliação posterior:

- compensação com emissões futuras;
- saldo administrativo negativo não financeiro;
- absorção pelo responsável;
- disputa;
- reparação contratual entre organizações;
- encerramento do caso.

Nenhuma opção é aprovada nesta versão.

## 13. Cancelamento pelo participante

Quando o resgate permitir cancelamento, deverão ser definidos:

- prazo;
- estado do benefício;
- responsabilidade;
- liberação de reserva;
- retorno de saldo;
- custos não recuperáveis futuros;
- dados já compartilhados;
- confirmação.

## 14. Encerramento do parceiro

Deverá tratar:

- benefícios listados;
- reservas;
- resgates confirmados;
- saldos relacionados;
- substituição;
- comunicação;
- cobertura;
- responsabilidade residual.

## 15. Contestação

A pessoa deverá conseguir:

- compreender a decisão;
- apresentar evidência;
- corrigir dados;
- solicitar revisão;
- receber resultado;
- identificar a autoridade;
- acessar o histórico do caso.

## 16. Fora do escopo

- catálogo de recompensas;
- quantidades;
- valores;
- SLAs;
- contratos;
- processo técnico de reserva;
- integração com parceiros;
- operação.
