---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.44.0
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
  - PAS-001
  - M7.68
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

### 4.1 Cobertura materializada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| descoberta e busca móvel | 5 | 5 | 0 |
| Perfil Público móvel | 4 | 4 | 0 |
| revisão e solicitação móvel | 5 | 5 | 0 |
| Solicitação Pendente móvel | 8 | 0 | 8 |
| demais famílias de Coletivos | 0 | 0 | não materializadas |
| **Total de Coletivos** | **22** | **14** | **8** |

A contagem de Coletivos permanece separada do Opportunity Boost.

### 4.2 Espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | materializada e validada |
| 2 | Resultados de Busca | materializada e validada |
| 3 | Perfil Público do Coletivo | materializada e validada |
| 4 | Revisão e Solicitação de Participação | materializada e validada |
| 5 | Solicitação Pendente | materializada; validação pendente |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Famílias validadas

Autoridades:

- UXA-060 e UXA-061 — descoberta e busca;
- UXA-062 e UXA-063 — Perfil Público;
- UXA-064 e UXA-065 — revisão e solicitação.

Estão validados:

- origens distinguíveis;
- filtros reversíveis;
- acompanhar separado de participar;
- reputação contextual;
- dados e consequências antes da ação;
- confirmações inicialmente vazias;
- cancelamento anterior ao envio;
- solicitação sem criação de vínculo;
- comprovante separado de acompanhamento contínuo;
- convite protegido com exposição proporcional.

## 6. Solicitação Pendente

Autoridade:

- UXA-066 — oito SVGs móveis materializados e ainda não validados funcionalmente.

Estados materializados:

1. aguardando decisão;
2. análise protegida;
3. informação adicional solicitada;
4. revisão da resposta adicional;
5. cancelada pela Pessoa;
6. aprovada;
7. recusada;
8. expirada.

Decisões representadas:

- estado, data, identificador e autoridade visíveis;
- prazo estimado sem promessa;
- dados enviados e protegidos;
- espera distinta de ação necessária;
- pergunta adicional com finalidade declarada;
- resposta revisável antes do envio;
- cancelamento separado de recusa;
- expiração separada de recusa;
- aprovação sem papel automático;
- recusa sem funcionar como reputação da Pessoa;
- processo protegido com exposição mínima;
- ausência de navegação ativa para `Meus Coletivos`.

## 7. Proteções transversais

- contagem não funciona como ranking;
- lista nominal permanece protegida;
- publicidade não compra legitimidade, reputação ou prioridade;
- apoio institucional não concede dados ou autoridade;
- visualização não revela identidade;
- denúncia não é avaliação;
- proteção não é irregularidade;
- convite não cria vínculo;
- decisão sobre vínculo não é reputação da Pessoa;
- estado contratual não gera automaticamente um SVG exclusivo.

## 8. Limites

O programa ainda não inicia:

- validação funcional da UXA-066;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- gestão do responsável;
- contestação completa;
- ambiente de simulação das jornadas;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 9. Próxima transição

**UXA-067 — Validação Funcional e Reformulação da Solicitação Pendente Móvel em Coletivos.**

O pacote deverá validar os oito SVGs antes de iniciar `Meus Coletivos` e dependerá de autorização separada.
