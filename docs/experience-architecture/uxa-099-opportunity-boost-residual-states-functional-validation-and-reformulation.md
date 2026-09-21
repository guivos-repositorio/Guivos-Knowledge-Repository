---
id: UXA-099
title: Contrato Funcional Corrente dos Estados Residuais do Opportunity Boost
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-055
depends_on:
  - UXA-038
  - UXA-039
  - UXA-043
  - UXA-045
  - UXA-047
  - UXA-049
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - GKR-JOURNEY-SURFACE-DETAIL-ADS-BOUNDARIES-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Contrato Funcional Corrente dos Estados Residuais do Opportunity Boost

> **Proveniência F-016.** Este contrato foi originalmente validado a partir de materializações low-fidelity hoje removidas. O vínculo `parent: UXA-055` preserva somente proveniência histórica. Nenhum SVG, composição móvel ou baseline visual histórico é entrada corrente de Design ou IA.

## 1. Finalidade

Consolidar os estados residuais correntes do Opportunity Boost de forma **independente de canal**, preservando distinções entre erro, inventário, baixa oferta, alteração material, preferência, denúncia e contestação.

A regra superior permanece:

> distribuição paga amplia exposição identificada; não compra relevância orgânica, recomendação pessoal, prioridade de jornada ou resultado.

## 2. Estados correntes

| Estado | Regra funcional corrente |
|---|---|
| erro técnico patrocinado | preservar catálogo orgânico e permitir nova tentativa sem representar erro como zero inventário |
| falha de atualização do anunciante | versão candidata não substitui a confirmada; mudança material não confirmada bloqueia nova entrega até revisão |
| inventário patrocinado indisponível | zero apurado não amplia critérios automaticamente e não altera resultados orgânicos |
| baixa oferta orgânica | reduzir ou eliminar publicidade; inventário pago não pode compensar artificialmente baixa oferta |
| mostrar menos deste tipo | preferência publicitária revisável, separada de filtros orgânicos |
| desativar oportunidades patrocinadas | preservar catálogo orgânico e permitir reversão consciente |
| ocultar campanha específica | afetar somente a campanha identificada, sem revelar identidade ou motivo da Pessoa ao anunciante |
| revisar e desfazer preferências | mostrar tipo, objeto, data, escopo e estado atual; reversões são independentes |
| denunciar conteúdo ou informação | fluxo de integridade separado de preferência publicitária |
| contestar uso indevido de dados | fluxo de privacidade/governança separado de denúncia e preferência |

Esses estados são responsabilidades funcionais. Não determinam número final de telas, componentes, breakpoints ou composição visual.

## 3. Alteração material não confirmada

Quando uma alteração candidata material não puder ser confirmada:

1. a última versão confirmada permanece a autoridade de configuração;
2. a versão candidata não é aplicada silenciosamente;
3. nova entrega entra em pausa protetiva;
4. eventos válidos anteriores permanecem preservados;
5. nenhuma nova entrega ou gasto futuro é presumido durante a incerteza;
6. o anunciante pode revisar, descartar ou reenviar conscientemente;
7. retomada exige confirmação válida e nova verificação dos gates aplicáveis.

A pausa protetiva não transforma o valor candidato em verdade canônica. Ela apenas impede continuidade baseada em informação possivelmente desatualizada.

## 4. Preferências e reversibilidade

Controles da Pessoa devem preservar escopos distintos:

```text
MOSTRAR MENOS DESTE TIPO
≠ OCULTAR CAMPANHA
≠ DESATIVAR PATROCINADOS
≠ DENUNCIAR CONTEÚDO
≠ CONTESTAR USO DE DADOS
```

Cada preferência revisável deve apresentar contexto suficiente para compreensão de:

- tipo de controle;
- objeto afetado;
- data de aplicação;
- superfície ou conjunto de superfícies aplicáveis;
- estado atual;
- possibilidade de reversão.

Reativar publicidade não restaura campanha expirada, encerrada ou inelegível e não cria personalização retroativa.

## 5. Idempotência funcional

A repetição da mesma intenção não deve duplicar efeito lógico:

```text
RECARREGAR CONTEÚDO PATROCINADO
→ não duplica impressão, evento, gasto ou preferência

REENVIAR A MESMA ALTERAÇÃO AINDA NÃO CONFIRMADA
→ não cria duas versões canônicas nem duas transições equivalentes

REPETIR CONFIRMAÇÃO JÁ APLICADA
→ preserva o mesmo efeito lógico
```

Este contrato não define chave técnica, armazenamento, protocolo, deduplicação ou algoritmo de mensuração.

## 6. Proteções correntes

- primeiro resultado orgânico permanece orgânico;
- pagamento não altera relevância funcional;
- localização contínua e histórico territorial sensível não alimentam campanhas;
- preferência negativa prevalece sobre entrega contratada no escopo aplicável;
- controles publicitários não reduzem o catálogo orgânico;
- anunciante ou financiador não recebem identidade, motivo, preferência, denúncia ou contestação da Pessoa por conveniência;
- relato protegido, compreensão inicial, Momento Atual, Próximo Passo, mensagens e inferências sensíveis permanecem fora do uso publicitário sem autoridade específica;
- erro técnico, zero inventário e baixa oferta permanecem estados distintos.

## 7. Relação com as superfícies correntes

```text
COM-001
→ configuração / revisão / confirmação do anunciante

COM-002
→ unidade patrocinada + explicação + controles da Pessoa

COM-003
→ presença patrocinada em Lista / Mapa

COM-004
→ campanha ativa / relatório / alterações / encerramento

COM-005
→ estados residuais deste contrato
```

`COM-005` permanece funcionalmente validada por este contrato. Isso **não promove** `TRN-305`, cuja ligação ponta a ponta continua parcial no Transition Registry.

## 8. Limites

Este contrato não cria ou aprova:

- política jurídica final de publicidade, denúncia, contestação ou retenção;
- limiar definitivo de agregação e privacidade;
- algoritmo de entrega, leilão, densidade ou frequência;
- antifraude técnico;
- mecanismo técnico de idempotência;
- cobrança, checkout ou faturamento;
- design visual final;
- protótipo navegável;
- teste com pessoas;
- implementação de `TRN-304`, `TRN-305` ou `TRN-306`;
- Engenharia de Produto.

## 9. Estado

```text
COM-005
→ FUNCTIONALLY VALIDATED

CHANNEL-SPECIFIC HISTORICAL WIREFRAMES
→ ABSORBED / GIT PROVENANCE

TRN-305
→ PARTIAL

PRODUCT ENGINEERING
→ NOT RELEASED
```
