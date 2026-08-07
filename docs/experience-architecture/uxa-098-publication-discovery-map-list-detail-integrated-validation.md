---
id: UXA-098
title: Validação Integrada da Continuidade Publicação → Descoberta, Mapa, Lista e Detalhe
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-004
  - UXA-007
  - UXA-008
  - UXA-012
  - UXA-013
  - UXA-024
  - UXA-025
  - UXA-028
  - UXA-029
  - UXA-038
related:
  - UXA-045
  - UXA-050
  - UXA-097
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - M7.85
normative: false
---

# Validação Integrada da Continuidade Publicação → Descoberta, Mapa, Lista e Detalhe

## 1. Finalidade

A UXA-098 executa a prioridade `V2 — publicação → descoberta/mapa/lista/detalhe` e valida como conjunto a continuidade entre:

```text
ORG-003 — Cadastro de Oportunidade pela Organização
→ TRN-203 — oportunidade ativa torna-se elegível à descoberta
→ PER-201 — Mapa de Oportunidades
↔ TRN-210 — mesma consulta em Lista
→ PER-202 — Lista territorial do Mapa

PER-201 → TRN-204 → PER-203 — Detalhe de Oportunidade
PER-202 → TRN-211 → PER-203 — Detalhe de Oportunidade
```

A validação é documental e funcional. Ela não cria algoritmo, distribuição real, implementação, tecnologia cartográfica ou campanha comercial.

## 2. Baseline governado

A frente foi iniciada a partir de `main` exatamente em:

`0de00298093b6f4fa7c54a26cb970812679b2f4b`

A auditoria confirmou que `ORG-003`, `PER-201`, `PER-202` e `PER-203` já possuem materialização e validação funcional local. Nenhum novo ID de superfície ou transição é necessário.

## 3. Diagnóstico integrado

Os contratos existentes já resolvem localmente:

- o ciclo `Rascunho → Enviada → Em avaliação → Ajustes solicitados → Aprovada para ativação → Ativa`;
- a regra de que ativação não garante apresentação;
- Mapa e Lista como duas representações da mesma consulta;
- preservação de busca, filtros, região e seleção;
- abertura do Detalhe com origem e contexto preservados;
- separação entre relevância funcional e relação comercial;
- identificação explícita de inventário patrocinado.

A lacuna remanescente era integrada: os registros não comprovavam, como um único contrato ponta a ponta, identidade lógica, estado canônico, elegibilidade à descoberta, mudança de modo, abertura do detalhe, retorno, atualização concorrente e fronteira entre distribuição orgânica e patrocinada.

## 4. Veredito

> **Aprovada sem reformulação visual, com formalização contratual integrada da publicação, descoberta e continuidade Mapa/Lista/Detalhe.**

Nenhum SVG foi criado ou alterado. As validações locais das quatro superfícies permanecem vigentes.

## 5. Contrato canônico da oportunidade

A mesma oportunidade lógica deverá preservar um identificador canônico através de cadastro, ativação, descoberta, Mapa, Lista e Detalhe.

Regras:

1. a Organização declara e mantém informações dentro de autoridade institucional vigente;
2. envio não equivale a aprovação;
3. aprovação não equivale a ativação automática;
4. somente estado ativo, vigente e materialmente consistente pode ser candidato à descoberta orgânica;
5. tornar-se candidato à descoberta não garante impressão, posição, recomendação, alcance ou exposição a qualquer pessoa;
6. o estado canônico mais recente prevalece sobre cópias, cartões ou telas abertas anteriormente;
7. pausa, expiração, encerramento, indisponibilidade ou correção material devem repercutir nas superfícies de descoberta sem fabricar histórico alternativo;
8. abrir, retornar, recarregar ou alternar Mapa/Lista não cria outra oportunidade lógica.

## 6. `GKR-TRN-203` — publicação → descoberta

`TRN-203` ocorre somente quando a oportunidade alcança condição canônica elegível para descoberta.

```text
ORG-003
→ oportunidade aprovada e ativa
→ autoridade, disponibilidade e informações materiais vigentes
→ TRN-203
→ entrada como candidata ao inventário descobrível de PER-201
```

### 6.1 Efeito válido

O efeito é **elegibilidade à descoberta**, não distribuição garantida.

A Organização não adquire autoridade para definir:

- posição orgânica;
- relevância individual;
- recomendação pessoal;
- prioridade de Próximo Passo;
- exposição mínima;
- conversão ou resultado.

### 6.2 Atualização e interrupção

Se preço, data, local, modalidade, capacidade, elegibilidade, risco, responsável ou outra condição material mudar, as superfícies consumidoras devem consultar ou receber o estado canônico atualizado antes de uma ação substantiva.

Oportunidade pausada, expirada, encerrada ou materialmente inválida deixa de ser acionável. Uma tela antiga não restaura elegibilidade.

### 6.3 Idempotência

Reprocessar a mesma ativação ou sincronização não cria oportunidade duplicada, nova prioridade ou impressão artificial.

## 7. `GKR-TRN-210` — Mapa ↔ Lista

Mapa e Lista representam a mesma consulta territorial, não dois catálogos independentes.

A alternância preserva, quando aplicável:

- contexto `Agindo como`;
- origem da consulta;
- região;
- busca;
- filtros;
- versão conhecida dos resultados;
- quantidade compatível;
- critérios de ordenação explicáveis;
- item selecionado;
- permissões e precisão territorial já autorizadas.

A troca de modo não:

- cria nova autorização de localização;
- ativa personalização;
- altera vínculo ou autoridade;
- transforma seleção em relevância;
- compra prioridade;
- reinicia silenciosamente a consulta.

Diferenças temporárias de quantidade ou ordem devem ser explicadas por atualização, fonte, prazo, disponibilidade ou critério declarado.

## 8. `GKR-TRN-204` e `GKR-TRN-211` — Mapa/Lista → Detalhe

As duas rotas conduzem ao mesmo `PER-203` canônico.

Ao abrir o Detalhe:

- o identificador lógico da oportunidade é preservado;
- origem Mapa ou Lista permanece reconhecível para retorno;
- região, busca, filtros, ordenação e seleção são preservados quando aplicáveis;
- o Detalhe consulta o estado material mais recente antes de permitir ação substantiva;
- indisponibilidade, expiração, mudança de preço ou alteração material prevalecem sobre o cartão de origem;
- abrir o Detalhe não significa interesse, inscrição, aceitação, recomendação ou evolução;
- retornar não altera posição orgânica, consentimento, localização ou personalização.

`TRN-204` e `TRN-211` terminam no Detalhe. Qualquer processo externo posterior pertence a `GKR-TRN-205` e permanece fora da UXA-098.

## 9. Relação orgânica e patrocinada

A publicação orgânica e o Opportunity Boost permanecem contratos distintos.

- pagamento amplia distribuição publicitária identificada; não altera avaliação funcional;
- inventário patrocinado e orgânico permanecem distinguíveis;
- oportunidade patrocinada continua sujeita a estado ativo, informações materiais vigentes, capacidade, moderação e controles da pessoa;
- posição patrocinada não é apresentada como posição orgânica;
- pagamento não altera relevância pessoal, confiança, qualidade ou Próximo Passo;
- ocultar publicidade não reduz acesso ao catálogo orgânico equivalente.

A UXA-098 não valida `TRN-304` ou `TRN-306`; apenas preserva sua fronteira com V2.

## 10. Concorrência e estado obsoleto

Casos integrados examinados:

| Situação | Regra |
|---|---|
| oportunidade pausada enquanto a pessoa vê Mapa/Lista | estado canônico prevalece; ação substantiva é bloqueada ou atualizada |
| oportunidade expira com Detalhe aberto | Detalhe informa indisponibilidade; tela aberta não restaura validade |
| preço ou condição muda entre cartão e Detalhe | condição atual é apresentada antes da decisão |
| resultado muda após movimento do mapa | nova área exige ação explícita `Pesquisar nesta área` |
| pessoa alterna Mapa/Lista repetidamente | mesma consulta e mesma identidade lógica; nenhum efeito duplicado |
| item patrocinado também possui correspondência orgânica | razões e inventários permanecem explicados separadamente |
| Organização reenvia sincronização do mesmo estado | atualização idempotente; sem duplicação de oportunidade |

## 11. Resultado nas transições

| Transição | Antes | Depois da UXA-098 |
|---|---|---|
| `GKR-TRN-203` | não examinada | **integralmente validada** |
| `GKR-TRN-204` | parcial | **integralmente validada** |
| `GKR-TRN-210` | parcial | **integralmente validada** |
| `GKR-TRN-211` | parcial | **integralmente validada** |

A validação integral cobre origem, destino, autoridade, estado, dados, efeito, retorno, interrupção, concorrência e idempotência no escopo documental.

## 12. Cobertura visual preservada

Como nenhum SVG foi criado ou alterado:

- SVGs: **109**;
- associações individuais: **109**;
- perfis de rastreabilidade: **28**;
- validações funcionais vigentes: **99**;
- pendentes: **10, exclusivamente UXA-055**;
- IDs com referência visual: **30 de 40**;
- responsabilidades sem SVG dedicado: **9**;
- superfícies: **40**;
- transições: **37**.

## 13. Jornadas

A UXA-098 melhora a continuidade entre Organização e Pessoa, mas não promove uma jornada inteira.

A Jornada da Organização permanece `draft` porque relação Organização–Coletivo, matriz institucional completa, estados residuais do Opportunity Boost e evidências/resultados institucionais seguem incompletos.

A Jornada da Pessoa permanece `draft` porque outras transições pessoais, incluindo `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005`, continuam parciais.

## 14. Limites

A UXA-098 não:

- altera SVGs;
- cria superfícies ou transições;
- define algoritmo de ranking, busca ou recomendação;
- garante distribuição, alcance ou visibilidade;
- valida os dez estados residuais UXA-055;
- valida `TRN-205`, `TRN-304` ou `TRN-306`;
- inicia efeito externo, transação, protótipo, teste com pessoas, W0-01 ou Engenharia de Produto;
- promove Jornada da Pessoa, do Coletivo ou da Organização.

## 15. Próximo ato governado

Após eventual integração da UXA-098 e nova autorização separada, a fila registrada poderá avançar para `V3 — dez estados residuais UXA-055`, por uma eventual UXA-099.

A UXA-099 não é iniciada por este documento.