---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.43.0
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
  - PAS-001
  - M7.67
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
| demais famílias de Coletivos | 0 | 0 | não materializadas |
| **Total de Coletivos** | **14** | **14** | **0** |

A contagem de Coletivos permanece separada do Opportunity Boost.

### 4.2 Espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | materializada e validada |
| 2 | Resultados de Busca | materializada e validada |
| 3 | Perfil Público do Coletivo | materializada e validada |
| 4 | Revisão e Solicitação de Participação | materializada e validada |
| 5 | Solicitação Pendente | não iniciada |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Descoberta e Perfil Público

Autoridades:

- UXA-060 e UXA-061 — descoberta e busca;
- UXA-062 e UXA-063 — Perfil Público.

Decisões preservadas:

- origens distinguíveis;
- primeiro resultado orgânico;
- filtros reversíveis;
- localização precisa opcional;
- acompanhar separado de participar;
- reputação contextual;
- Perfil Público protegido fora da descoberta pública.

## 6. Revisão e solicitação

Autoridades:

- UXA-064 — cinco SVGs móveis;
- UXA-065 — validação funcional e reformulação.

Estados validados:

1. revisão para entrada aberta;
2. confirmação da entrada aberta;
3. revisão de solicitação mediante aprovação;
4. comprovante transitório do envio;
5. revisão protegida de convite.

Regras validadas:

- nenhuma confirmação começa selecionada;
- visibilidade inicial não é apresentada como escolha inexistente;
- dados permitidos e protegidos aparecem antes da ação;
- papel, autoridade, notificações, marketing e contato privado permanecem separados;
- cancelamento anterior ao envio não compartilha dados;
- acessibilidade permanece recurso próprio;
- envio para aprovação não cria vínculo;
- comprovante não substitui Solicitação Pendente;
- alegação do convite é identificada como não verificada;
- confidencialidade não é garantia absoluta.

## 7. Proteções transversais

- contagem não funciona como ranking;
- lista nominal permanece protegida;
- publicidade não compra legitimidade, reputação ou prioridade;
- apoio institucional não concede dados ou autoridade;
- visualização não revela identidade;
- denúncia não é avaliação;
- proteção não é irregularidade;
- convite não cria vínculo;
- estado contratual não gera automaticamente um SVG exclusivo.

## 8. Limites

O programa ainda não inicia:

- Solicitação Pendente;
- informação adicional, recusa, expiração ou contestação;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- gestão do responsável;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 9. Próxima transição

**UXA-066 — Wireframes Móveis da Solicitação Pendente em Coletivos.**

O pacote dependerá de autorização separada.
