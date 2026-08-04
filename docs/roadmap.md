---
id: ROADMAP-12.39.0
title: Roadmap Arquitetural — Perfil Público Móvel de Coletivos Validado
status: active
version: 12.39.0
owner: Guivos
last_updated: 2026-08-04
supersedes_partial:
  - ROADMAP-12.38.0
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
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.65
---

# Roadmap Arquitetural — Perfil Público Móvel de Coletivos Validado

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Perfil Público móvel validado | M7.65 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Descoberta móvel | 5 SVGs materializados e validados | UXA-060; UXA-061 |
| Perfil Público móvel | 4 SVGs materializados e validados | UXA-062; UXA-063 |
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
```

## 4. Estado da espinha dorsal P0A

| Ordem | Superfície | Estado |
|---:|---|---|
| 1 | Explorar Coletivos | validada |
| 2 | Resultados de Busca | validada |
| 3 | Perfil Público do Coletivo | validado |
| 4 | Revisão e Solicitação de Participação | não iniciada |
| 5 | Solicitação Pendente | não iniciada |
| 6 | Meus Coletivos | não iniciado |
| 7 | Central de Atualizações | não iniciada |
| 8 | Início do Participante | reformulação não iniciada |
| 9 | Visão Geral do Responsável | não iniciada |

## 5. Resultado da UXA-063

A validação aprovou os quatro estados após reformulação:

- entrada aberta;
- entrada mediante aprovação;
- entradas temporariamente indisponíveis;
- apresentação protegida por convite.

Foram consolidados:

- denominadores por dimensão na reputação;
- compartilhamento de perfil sem endosso;
- canais públicos sem contato privado automático;
- dados submetidos somente após revisão;
- separação entre anunciante e responsável operacional;
- explicação da publicidade;
- proveniência do convite protegido;
- navegação protegida fora de Explorar.

## 6. Próximo pacote permitido

Após integração da UXA-063 e nova autorização, o programa poderá avançar para:

> **UXA-064 — Wireframes Móveis da Revisão e Solicitação de Participação em Coletivos**

Escopo máximo recomendado:

1. revisão da entrada aberta;
2. revisão da solicitação mediante aprovação;
3. revisão especializada do convite protegido;
4. regras, dados, permissões e significado do vínculo;
5. confirmações inicialmente vazias;
6. cancelamento antes do envio;
7. resultado imediato ou envio para análise.

A UXA-064 não deverá incluir Solicitação Pendente, `Meus Coletivos`, comunicação interna ou gestão.

## 7. Gates preservados

Antes de avançar além da UXA-064, deverão ser demonstrados:

- confirmação consciente;
- dados mínimos e proporcionais;
- autoridade de quem recebe a solicitação;
- diferença entre entrada aberta, aprovação e convite;
- cancelamento anterior ao envio;
- ausência de consentimento pré-selecionado;
- resultado e continuidade compreensíveis;
- proteção de grupos sensíveis.

## 8. Frentes paralelas preservadas

Não são reabertas automaticamente:

- validação dos 10 estados residuais do Opportunity Boost;
- Resultados Empresariais;
- preços ou baseline comercial;
- política jurídica;
- protótipo;
- testes com pessoas;
- Engenharia de Produto.

## 9. Regra de autorização

Integração da UXA-063 não inicia a UXA-064. Cada pacote continuará exigindo autorização própria para criação e autorização separada para integração.
