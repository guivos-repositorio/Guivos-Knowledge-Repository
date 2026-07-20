---
id: PAS-001-CC-W0-ENV-001
title: Ambientes e Estratégia de Integração da Onda 0
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-W0-DEPENDENCY-001
  - PAS-001-CC-UIC-NFR-SECURITY-001
---

# PAS-001-CC-W0-ENV-001 — Ambientes e Estratégia de Integração

## 1. Princípios

- nenhum ambiente da Onda 0 é produção;
- dados pessoais reais são proibidos por padrão;
- dados sintéticos devem ser versionados e reproduzíveis;
- segredos não entram em código, payload ou log;
- acesso é por menor privilégio e tempo limitado;
- cada ambiente possui finalidade e saída permitida;
- evidência registra ambiente, versão e configuração relevante;
- promoção entre ambientes não amplia autoridade.

## 2. Ambientes

### 2.1 Local

**Finalidade:** desenvolvimento individual e testes rápidos.

**Permitido:**

- dados sintéticos;
- dependências substituíveis;
- execução em memória;
- mocks que preservem contratos;
- testes unitários, transição e schema.

**Proibido:**

- dados pessoais reais;
- credenciais compartilhadas;
- acesso a consumidores externos;
- afirmação de SLO real;
- evidência de gate baseada apenas em mock.

### 2.2 Test

**Finalidade:** pipeline automatizado e validação contínua.

**Capacidades mínimas:**

- testes de domínio;
- transições;
- schemas e contratos;
- análise estática;
- varredura de segredos;
- varredura de logs de teste;
- fixtures válidas e inválidas;
- relatórios versionados.

### 2.3 Integration

**Finalidade:** validar fluxos entre persistência, eventos, conteúdo protegido e consumidores mínimos.

**Capacidades mínimas:**

- persistência transacional representativa;
- mecanismo confiável de publicação;
- storage protegido;
- registro de consumidores;
- correção e revogação ponta a ponta;
- busca protegida mínima;
- reconstrução e replay;
- observabilidade segura.

### 2.4 Security Lab

**Finalidade:** exercícios adversariais e validação do threat model.

**Cenários mínimos:**

- enumeração de IDs;
- escalada de privilégio;
- vazamento cruzado;
- abuso de representação;
- mídia maliciosa;
- prompt injection textual e multimodal;
- exfiltração por modelo;
- consumidor comprometido;
- abuso administrativo;
- downgrade de contrato;
- segredo em payload;
- conteúdo sensível em logs.

### 2.5 Performance Lab

**Finalidade:** medir SLIs e validar SLOs candidatos.

**Medições mínimas:**

- p50, p95 e p99;
- throughput;
- backlog por idade;
- disponibilidade por classe;
- propagação de correção;
- propagação de revogação;
- reconstrução;
- RPO e RTO;
- degradação sob pico;
- comportamento de retries.

### 2.6 Internal Trial

**Finalidade:** ensaio restrito, acompanhado e reversível.

**Condições:**

- acesso somente a pessoas autorizadas;
- dados sintéticos ou consentimento específico aprovado;
- nenhuma exposição pública;
- rollout limitado;
- kill switch funcional;
- monitoramento contínuo;
- plano de rollback testado;
- aprovação dos cinco gates aplicáveis ao ensaio.

## 3. Fluxo de promoção

```text
Local
  ↓
Test
  ↓
Integration
  ├──→ Security Lab
  └──→ Performance Lab
            ↓
       Internal Trial
```

Regras:

- falha de contrato impede promoção a Integration;
- falha de isolamento impede qualquer ensaio;
- ausência de redaction impede Security Lab e Internal Trial;
- SLO não medido impede fechamento do gate de qualidade;
- Internal Trial não promove automaticamente a produção.

## 4. Estratégia de integração

### 4.1 Integração por contrato

- produtor e consumidor validam schemas independentemente;
- versão maior incompatível é rejeitada ou isolada;
- consumidor não recebe campo fora do escopo autorizado;
- eventos técnicos não são consumidos como fatos funcionais;
- cada consumidor declara correção, revogação e retenção.

### 4.2 Integração por fluxo

Fluxos mínimos:

1. criar sessão e registrar entrada;
2. transcrever ou classificar sem confirmar;
3. apresentar síntese e receber decisão humana;
4. autorizar finalidade e persistência;
5. emitir recorte mínimo a consumidor;
6. corrigir e acompanhar aplicação;
7. revogar e bloquear novos usos;
8. reconstruir estado e projeções;
9. indexar e remover resultado protegido;
10. restaurar sem reativar conteúdo revogado.

### 4.3 Integração de consumidores

Consumidor mínimo deverá declarar:

- `consumer_id`;
- finalidade;
- versão contratual;
- dados necessários;
- retenção;
- canal de correção;
- canal de revogação;
- tempo de resposta;
- kill switch;
- owner operacional.

## 5. Dados de teste

O catálogo de dados sintéticos deverá cobrir:

- participante individual;
- representação válida e expirada;
- menor e terceiro;
- dispositivo compartilhado;
- conteúdo textual, documento e uma mídia mínima;
- hipótese, interpretação e fato confirmado;
- autorização válida, expirada e revogada;
- correção simples e em cadeia;
- consumidor online, atrasado e comprometido;
- retenção residual legítima;
- mensagem incompatível;
- replay duplicado e fora de ordem.

## 6. Segredos e credenciais

- credenciais são específicas por ambiente;
- privilégios são mínimos;
- rotação é documentada;
- acesso administrativo é JIT quando disponível;
- uso é auditado sem expor segredo;
- credencial local nunca acessa ambiente superior;
- incidente de segredo exige revogação e registro.

## 7. Observabilidade por ambiente

| Ambiente | Logs | Métricas | Tracing | Retenção |
|---|---|---|---|---|
| Local | mínimo e sintético | opcional | opcional | efêmera |
| Test | redigido | pipeline | correlação sintética | curta |
| Integration | redigido | obrigatório | obrigatório nos fluxos críticos | controlada |
| Security Lab | segregado | obrigatório | obrigatório | limitada ao exercício |
| Performance Lab | sem conteúdo | obrigatório | amostrado e seguro | limitada ao relatório |
| Internal Trial | redigido e auditado | obrigatório | obrigatório C0/C1 | conforme finalidade |

## 8. Critérios de rollback

Rollback deverá existir quando:

- versão de contrato falhar;
- consumidor aplicar efeito incompatível;
- índice expor resultado indevido;
- revogação não bloquear novos usos;
- log contiver conteúdo proibido;
- integridade de conteúdo falhar;
- comportamento de carga exceder limite seguro;
- risco crítico surgir sem mitigação.

Rollback não poderá apagar trilha mínima necessária à investigação.

## 9. Gate de ambiente

Antes do Internal Trial, demonstrar:

- isolamento;
- dados permitidos;
- segredos protegidos;
- kill switch;
- rollback;
- correção e revogação;
- observabilidade;
- runbooks;
- owner de plantão;
- aprovação formal do ensaio.

## 10. Produção

Produção permanece fora desta arquitetura de ambientes. Sua criação exigirá:

- decisão posterior;
- arquitetura operacional;
- capacidade de suporte;
- requisitos regulatórios;
- segurança validada;
- plano de continuidade;
- aprovação explícita de go-live.