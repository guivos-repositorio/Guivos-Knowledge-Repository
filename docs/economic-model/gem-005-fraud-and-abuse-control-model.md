---
id: GEM-005-FRAUD-ABUSE-CONTROL-MODEL-001
title: Modelo de Controle de Fraude e Abuso
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Modelo de Controle de Fraude e Abuso

## 1. Objetivo

Classificar riscos e controles conceituais para proteger eventos, evidências, emissões, saldos, resgates, parceiros e participantes.

## 2. Princípios

- controle proporcional ao risco;
- presunção não substitui evidência;
- suspensão deve ser limitada ao necessário;
- revisão humana será usada em casos materiais;
- dados serão minimizados;
- decisões serão rastreáveis;
- contestação estará disponível;
- parceiro e operador também poderão ser investigados;
- fraude confirmada não autoriza punição coletiva;
- nenhum controle técnico é implementado nesta versão.

## 3. Riscos de identidade e conta

- contas duplicadas;
- identidade falsa;
- conta compartilhada;
- venda de conta;
- acesso não autorizado;
- tomada de conta;
- criação automatizada de perfis;
- uso indevido de conta de terceiro.

## 4. Riscos de evento e evidência

- evento fictício;
- documento alterado;
- autoconfirmação indevida;
- conluio;
- confirmação por parte relacionada;
- localização falsa;
- horas sobrepostas;
- repetição do mesmo evento;
- evidência reutilizada;
- cancelamento posterior do evento;
- atividade não realizada.

## 5. Riscos de emissão e saldo

- dupla emissão;
- emissão acima da cobertura;
- regra aplicada incorretamente;
- saldo criado sem evento;
- alteração indevida de saldo;
- reversão sem autoridade;
- expiração incorreta;
- inconsistência entre estados;
- uso simultâneo de saldo reservado.

## 6. Riscos de resgate

- duplo resgate;
- benefício inexistente;
- confirmação falsa;
- parceiro não entrega;
- uso de identificador de terceiro;
- cancelamento após utilização;
- estorno ou chargeback;
- substituição inferior não informada;
- dados desviados da finalidade.

## 7. Riscos de indicação e campanha

- autorreferência;
- múltiplos canais reivindicando o mesmo evento;
- lead sem consentimento;
- compra de tráfego inválido;
- incentivos para cadastro artificial;
- combinação entre participantes;
- campanha acima do limite;
- parceiro manipulando atribuição.

## 8. Riscos de voluntariado e impacto

- organização inexistente;
- atividade não realizada;
- horas infladas;
- beneficiário usado como evidência sem consentimento;
- evento inseguro;
- sobreposição de participantes;
- patrocinador alterando registros;
- recompensa tratada como prova de impacto.

## 9. Controles conceituais

- limites por evento e período;
- chaves de duplicidade;
- confirmação progressiva;
- estados pendentes;
- espera antes da disponibilidade;
- validação por múltiplas fontes;
- segregação de funções;
- trilha de auditoria;
- revisão humana;
- suspensão proporcional;
- controle de cobertura;
- reconciliação futura;
- interrupção de parceiro;
- contestação e correção;
- reversão rastreável.

## 10. Matriz de risco

```yaml
fraud_risk_id: string
program_id: string
category: string
scenario: string
assets_affected:
  - string
likelihood: string
impact: string
detection_signals:
  - string
preventive_controls:
  - string
detective_controls:
  - string
response:
  - string
appeal_available: true
owner: string
status: open
```

## 11. Sinais candidatos

- volume incompatível com capacidade humana ou operacional;
- repetição de evidência;
- eventos simultâneos incompatíveis;
- concentração incomum em dispositivo, parceiro ou local;
- taxa elevada de cancelamento;
- emissão seguida de devolução;
- resgates em sequência anormal;
- divergência entre parceiro e participante;
- alteração manual recorrente;
- cobertura sendo excedida;
- múltiplas contas relacionadas.

Sinal não equivale a fraude comprovada.

## 12. Resposta

A resposta poderá incluir:

- solicitação de evidência;
- bloqueio do evento;
- suspensão do saldo relacionado;
- limitação temporária;
- revisão humana;
- cancelamento da emissão;
- reversão;
- suspensão do programa;
- suspensão do parceiro;
- encaminhamento especializado futuro;
- restauração quando a suspeita não for confirmada.

## 13. Contestação

A pessoa ou organização afetada deverá poder:

- conhecer a razão em nível compatível com segurança;
- corrigir dados;
- apresentar evidência;
- solicitar revisão;
- receber decisão;
- identificar a autoridade;
- obter restauração quando aplicável.

## 14. Privacidade

Controles antifraude não autorizam coleta irrestrita. Cada dado deverá possuir finalidade, necessidade, acesso limitado e retenção proporcional.

## 15. Parceiros e operadores

O modelo deverá controlar também:

- emissão manual;
- alteração de catálogo;
- confirmação de entrega;
- criação de campanhas;
- acesso a dados;
- encerramento de benefícios;
- conflitos de interesse;
- ações administrativas.

## 16. Condições de parada

- cobertura excedida;
- duplicidade sistêmica;
- parceiro não entrega;
- taxa de reversão material;
- controle incapaz de distinguir eventos;
- acesso indevido a dados;
- decisões sem contestação;
- fraude organizada;
- saldo inconsistente;
- incidente de segurança.

## 17. Fora do escopo

- regras quantitativas;
- modelos preditivos;
- fornecedor antifraude;
- identidade digital implementada;
- monitoramento técnico;
- investigação criminal;
- operação.
