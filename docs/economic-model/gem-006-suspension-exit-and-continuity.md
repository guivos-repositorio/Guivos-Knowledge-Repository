---
id: GEM-006-SUSPENSION-EXIT-CONTINUITY-001
title: Suspensão, Saída e Continuidade de Parceiros
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-006
---

# Suspensão, Saída e Continuidade de Parceiros

## 1. Objetivo

Definir como relações poderão ser interrompidas ou encerradas sem apagar obrigações, prejudicar participantes ou criar retenção indevida.

## 2. Motivos candidatos de suspensão

- fraude;
- risco à segurança;
- qualidade inadequada;
- oferta indisponível;
- violação de dados;
- publicidade enganosa;
- não cumprimento de obrigação;
- conflito não tratado;
- uso indevido de marca;
- manipulação de evidência;
- perda de habilitação;
- concentração intolerável;
- dependência especializada não atendida.

## 3. Tipos de suspensão

- oferta específica;
- papel específico;
- produto;
- território;
- acesso a dados;
- integração;
- recebimento de novos pedidos;
- relacionamento integral.

A suspensão deverá ser proporcional, exceto quando proteção de participantes exigir interrupção imediata.

## 4. Saída controlada

A saída deverá tratar:

- pedidos ativos;
- reservas;
- serviços em andamento;
- repasses;
- reembolsos;
- chargebacks;
- recompensas emitidas;
- benefícios válidos;
- reclamações;
- disputas;
- dados;
- conteúdo;
- marca;
- integrações;
- comunicação;
- registros históricos.

## 5. Continuidade de obrigações

O encerramento não elimina automaticamente:

- garantia;
- reembolso;
- suporte de entrega já contratada;
- obrigação de dados;
- confidencialidade;
- auditoria;
- investigação;
- resolução de disputa;
- responsabilidade por dano;
- recursos vinculados.

## 6. Saída de parceiro crítico

Deverá existir futuramente:

- inventário de dependências;
- plano de substituição;
- migração de dados;
- transição de participantes;
- tratamento de acesso;
- cobertura de obrigações;
- comunicação;
- owner;
- condição de encerramento completo.

## 7. Registro de saída

```yaml
partner_exit_id: string
relationship_id: string
reason: string
scope: string
started_at: datetime
active_obligations:
  - string
affected_actors:
  - string
continuity_actions:
  - string
data_actions:
  - string
communication:
  - string
completion_criteria:
  - string
owner: string
status: exiting
```

## 8. Proteções

Não serão admissíveis:

- apagar histórico para encerrar conflito;
- abandonar pedidos ou recompensas;
- reter dados como pressão;
- impedir portabilidade legítima;
- comunicar falsamente continuidade;
- transferir responsabilidade sem consentimento ou base apropriada.

## 9. Fora do escopo

- cláusula contratual;
- prazo;
- indenização;
- fornecedor substituto;
- operação real.
