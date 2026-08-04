---
id: ROADMAP-12.40.0
title: Roadmap Arquitetural — Revisão e Solicitação Móvel de Participação Materializadas
status: active
version: 12.40.0
owner: Guivos
last_updated: 2026-08-04
supersedes_partial:
  - ROADMAP-12.39.0
related:
  - GKR-STATE-001
  - GPA-007
  - GEM-004-A1
  - GEM-007-A1
  - GEM-010-A2
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.66
---

# Roadmap Arquitetural — Revisão e Solicitação Móvel de Participação Materializadas

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | revisão e solicitação móvel materializadas | M7.66 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Descoberta móvel | 5 SVGs materializados e validados | UXA-060; UXA-061 |
| Perfil Público móvel | 4 SVGs materializados e validados | UXA-062; UXA-063 |
| Revisão e Solicitação | 5 SVGs materializados; validação pendente | UXA-064 |
| Opportunity Boost | 46 materializados; 36 validados; 10 pendentes | UXA-038 a UXA-055 |
| Resultados Empresariais | 18 decisões; zero canônicos | BA-STR-002-CODR-001 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência concluída dos Coletivos

```text
UXA-056 — descoberta, Perfil Público e participação contratados
→ UXA-057 — avaliação e reputação contratadas
→ UXA-058 — interação, recomendação e conexão contratadas
→ UXA-059 — programa de wireframes priorizado
→ UXA-060 — descoberta e busca materializadas
→ UXA-061 — descoberta e busca validadas
→ UXA-062 — Perfil Público materializado
→ UXA-063 — Perfil Público validado
→ UXA-064 — revisão e solicitação materializadas
```

## 4. Estado da espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | validada |
| 2 | Resultados de Busca | validada |
| 3 | Perfil Público do Coletivo | validado |
| 4 | Revisão e Solicitação de Participação | materializada; validação pendente |
| 5 | Solicitação Pendente | não iniciada |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Resultado da UXA-064

A família contém cinco estados:

1. revisão da entrada aberta;
2. entrada aberta confirmada;
3. revisão da solicitação mediante aprovação;
4. comprovante transitório de envio;
5. revisão protegida de convite.

Foram materializados:

- significado do vínculo;
- regras e condições materiais;
- dados enviados e proibidos;
- permissões separadas;
- confirmações inicialmente vazias;
- cancelamento antes do envio;
- autoridade e prazo estimado;
- entrada aberta sem função automática;
- solicitação sem criação de vínculo;
- convite protegido sem participação automática;
- comprovante sem substituir Solicitação Pendente.

## 6. Gate obrigatório

Antes de iniciar Solicitação Pendente, deverá ser concluída:

> **UXA-065 — Validação Funcional e Reformulação da Revisão e Solicitação de Participação Móvel em Coletivos**

O gate deverá examinar os cinco SVGs como percurso único entre Perfil Público, confirmação imediata, envio para análise e continuidade futura.

## 7. Próxima sequência prevista

Após validação e nova autorização, a sequência poderá avançar para:

```text
UXA-065 — validar revisão e solicitação
→ Solicitação Pendente
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

A Solicitação Pendente deverá tratar estado contínuo, prazo, responsável, cancelamento, informação adicional, decisão e próximos eventos sem reutilizar o comprovante como tela de acompanhamento.

## 8. Gates preservados

Antes de avançar além da UXA-064, deverão ser demonstrados:

- confirmações compreensíveis e não coercitivas;
- dados mínimos e proporcionais;
- autoridade de quem recebe a solicitação;
- diferença entre entrada aberta, aprovação e convite;
- cancelamento anterior ao envio;
- ausência de consentimento pré-selecionado;
- resultado e continuidade compreensíveis;
- proteção de grupos sensíveis;
- separação entre comprovante transitório e estado pendente.

## 9. Frentes paralelas preservadas

Não são reabertas automaticamente:

- validação dos 10 estados residuais do Opportunity Boost;
- Resultados Empresariais;
- preços ou baseline comercial;
- política jurídica;
- protótipo;
- testes com pessoas;
- Engenharia de Produto.

## 10. Regra de autorização

Integração da UXA-064 não inicia a UXA-065. Cada pacote continuará exigindo autorização própria para criação e autorização separada para integração.
