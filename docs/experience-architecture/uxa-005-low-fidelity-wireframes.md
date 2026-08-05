---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.45.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-000
related:
  - UXA-001
  - UXA-003
  - UXA-009
  - UXA-020
  - UXA-024
  - UXA-038
  - UXA-050
  - UXA-055
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - UXA-065
  - UXA-066
  - UXA-067
  - UXA-068
  - PAS-001
  - M7.69
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de experiência antes de identidade visual, protótipo, teste ou implementação.

```text
contrato funcional
→ programa e priorização
→ wireframe de baixa fidelidade
→ validação funcional
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Materialização não equivale a validação. Validação funcional não autoriza automaticamente protótipo ou Engenharia.

## 2. Convenções

| Elemento | Significado |
|---|---|
| borda contínua | área funcional |
| preenchimento escuro | ação principal consciente |
| preenchimento cinza | limite, resumo ou indisponibilidade |
| borda tracejada | proteção, exceção ou relação comercial |
| texto sublinhado | ação secundária ou explicação |
| rótulo anterior ao conteúdo | origem, autoridade ou natureza comercial |
| estado textual | condição que não depende apenas de cor |
| confirmação vazia | confirmação ainda não registrada |

Cor, tipografia e iconografia não possuem significado definitivo.

## 3. Opportunity Boost

| Família | Materializados | Validados por pacote | Pendentes |
|---|---:|---:|---:|
| configuração para computador | 5 | 5 | 0 |
| configuração móvel | 5 | 5 | 0 |
| cartão e explicação | 6 | 6 | 0 |
| Lista e Mapa patrocinados | 4 | 4 | 0 |
| gestão para computador | 6 | 6 | 0 |
| gestão móvel | 6 | 6 | 0 |
| relatório agregado | 4 | 4 | 0 |
| estados residuais | 10 | 0 | 10 |
| **Total** | **46** | **36** | **10** |

## 4. Programa de Coletivos

A UXA-059 organiza 88 estados contratuais em P0A, P0B, P1 e P2.

### 4.1 Cobertura materializada e validada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| descoberta e busca móvel | 5 | 5 | 0 |
| Perfil Público móvel | 4 | 4 | 0 |
| revisão e solicitação móvel | 5 | 5 | 0 |
| Solicitação Pendente móvel | 8 | 8 | 0 |
| demais famílias de Coletivos | 0 | 0 | não materializadas |
| **Total de Coletivos** | **22** | **22** | **0** |

A contagem de Coletivos permanece separada do Opportunity Boost.

### 4.2 Espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | materializada e validada |
| 2 | Resultados de Busca | materializada e validada |
| 3 | Perfil Público do Coletivo | materializada e validada |
| 4 | Revisão e Solicitação de Participação | materializada e validada |
| 5 | Solicitação Pendente | materializada e validada |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Autoridades das famílias validadas

- UXA-060 e UXA-061 — descoberta e busca;
- UXA-062 e UXA-063 — Perfil Público;
- UXA-064 e UXA-065 — revisão e solicitação;
- UXA-066 e UXA-067 — Solicitação Pendente.

## 6. Resultado da Solicitação Pendente

Estados validados:

1. aguardando decisão;
2. análise protegida;
3. informação adicional solicitada;
4. revisão da resposta adicional;
5. cancelada pela Pessoa;
6. aprovada;
7. recusada;
8. expirada.

Regras validadas:

- consulta não altera fila ou prioridade;
- estimativa não é promessa;
- dado material não é editado silenciosamente durante análise;
- autoridade protegida é limitada ao processo;
- pedido adicional não é obrigação de revelar;
- resposta, preferência, contestação e cancelamento são distintos;
- descartar resposta não cancela solicitação;
- envio adicional poderá retomar análise sem criar vínculo;
- tratamento posterior não é garantia técnica ou jurídica absoluta;
- aprovação não cria função, autoridade, presença ou notificação automática;
- recusa não é sanção, reputação ou denúncia;
- expiração não é recusa ou consentimento;
- revisão formal não é simulada sem contrato próprio;
- `Meus Coletivos` não é apresentado como disponível.

## 7. Proteções transversais

- contagem não funciona como ranking;
- lista nominal permanece protegida;
- publicidade não compra legitimidade, reputação ou prioridade;
- apoio institucional não concede dados ou autoridade;
- visualização não revela identidade;
- denúncia não é avaliação nem revisão formal;
- proteção não é irregularidade;
- convite não cria vínculo;
- decisão sobre vínculo não é reputação da Pessoa;
- estado contratual não gera automaticamente um SVG exclusivo.

## 8. Lacuna prioritária fora de Coletivos

A tela de escolha multimodal do início protegido permite texto, voz, arquivo e perguntas opcionais, mas ainda não orienta suficientemente a Pessoa a expressar o Momento Atual.

A UXA-068 deverá materializar orientação para situação, impacto, prioridade, direção e contexto, com relato livre, perguntas adaptativas, síntese e revisão.

## 9. Limites

O programa ainda não inicia:

- UXA-068;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- gestão do responsável;
- revisão formal completa da recusa;
- ambiente de simulação das jornadas;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 10. Próxima transição

**UXA-068 — Expressão Guiada do Momento Atual por Texto e Voz.**

O pacote dependerá de autorização separada.
