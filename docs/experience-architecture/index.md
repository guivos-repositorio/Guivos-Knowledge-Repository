---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.71.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
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
  - UXA-069
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.72
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório em experiências compreensíveis para Pessoas, Coletivos e Organizações.

Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design visual ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização visual ou documental
→ validação funcional
→ reformulação, quando exigida
→ nova validação
→ promoção controlada, quando aplicável
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura relacionada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Início protegido geral | 4 | 4 | 0 |
| Compreensão inicial | 5 | 5 | 0 |
| Expressão Guiada do Momento Atual | 8 | 8 | 0 |
| Coletivos | 22 | 22 | demais famílias não materializadas |
| Opportunity Boost | 46 | 36 | 10 estados da UXA-055 |

As contagens não comprovam validação ponta a ponta.

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- rascunho não solicita análise ou salvamento implícitos;
- gravação e transcrição possuem finalidade limitada;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- convite não cria vínculo;
- publicidade não compra relevância, reputação ou autoridade;
- correção documental não equivale a aprovação funcional.

## 5. Autoridades dos Coletivos

| Responsabilidade | Autoridade |
|---|---|
| descoberta, Perfil Público e participação | UXA-056 |
| avaliação e reputação contextual | UXA-057 |
| interação, recomendação, contato e proteção | UXA-058 |
| programa e priorização de wireframes | UXA-059 |
| descoberta e busca móvel | UXA-060; UXA-061 |
| Perfil Público móvel | UXA-062; UXA-063 |
| revisão e solicitação móvel | UXA-064; UXA-065 |
| Solicitação Pendente móvel | UXA-066; UXA-067 |

A busca de Coletivos é representada por `GKR-SURF-PER-101` e `GKR-SURF-PER-102`. Esses IDs não representam oportunidades.

## 6. Evolução das Jornadas Integradas

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — validação funcional não aprovada até reformulação
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — revalidação aprovada com ressalvas no escopo documental
→ UXA-075 — promoção seletiva e sincronização pós-validação executadas
→ UXA-076 — registros granulares materializados em draft
→ UXA-077 — validação granular não aprovada até correção obrigatória
→ UXA-078 — reformulação controlada executada
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante institucional, especialista, anunciante e patrocinador são perspectivas, papéis ou operadores contextuais, não novos participantes estruturais.

## 7. Resultado da UXA-078

[UXA-078 — Reformulação Controlada dos Registros Granulares](uxa-078-controlled-granular-registry-reformulation.md) corrige documentalmente os cinco achados obrigatórios da UXA-077.

### 7.1 Estado quantitativo

| Registro | Quantidade | Estado |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `draft` 0.2.0 |
| transições | 37 | `draft` 0.2.0 |
| endpoints em texto livre | 0 | corrigidos documentalmente |

### 7.2 Separações vigentes

```text
Coletivos:
GKR-SURF-PER-101 → GKR-SURF-PER-102 → GKR-SURF-PER-103

Oportunidades:
GKR-SURF-ORG-003
→ GKR-SURF-PER-201
↔ GKR-SURF-PER-202
→ GKR-SURF-PER-203
→ GKR-SURF-BND-001
```

- `GKR-SURF-ORG-003` representa estado institucional;
- `GKR-SURF-PER-203` representa o Detalhe de Oportunidade;
- `GKR-SURF-BND-001` é fronteira documental, não participante ou tela;
- `GKR-SURF-COM-005` aponta para UXA-055.

### 7.3 Campos obrigatórios

Cada entrada do registro de superfícies passa a explicitar:

- artefato canônico e caminho;
- versão;
- decisão;
- dados;
- gate;
- reversibilidade;
- supersessão;
- observação de escopo.

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 8. Reutilização canônica

- artefatos são referenciados por ID, caminho e versão;
- arquivos canônicos permanecem em modo somente leitura;
- uma referência pode aparecer em várias perspectivas sem cópia;
- nenhuma ligação é criada por proximidade visual;
- inclusão no ambiente não altera maturidade, prioridade ou canonicidade;
- Opportunity Boost permanece camada comercial identificada;
- fronteira documental não equivale a integração técnica.

## 9. Estado da seção documental

| Artefato | Estado |
|---|---|
| navegação de primeiro nível | `active` |
| visão geral | `active` |
| Pessoa, Coletivo e Organização | `draft` por incompletude explícita |
| handoffs | `active` como matriz resumida governada |
| cenários | `active` como hipóteses documentais governadas |
| catálogo | `active` como inventário agregado |
| lacunas | `active`, observacional e não promocional |
| registro granular de superfícies | `draft` 0.2.0; reformulado |
| registro granular de transições | `draft` 0.2.0; reformulado |
| revalidação granular | não iniciada |
| protótipo ou aplicação | não iniciados |

## 10. Limites

Não foram iniciados:

- UXA-079;
- promoção funcional dos registros granulares;
- protótipo navegável;
- aplicação ou motor de simulação;
- modelo de IA ou algoritmo adaptativo;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- relação bilateral Organização–Coletivo materializada;
- validação dos estados residuais da UXA-055;
- teste com pessoas;
- Engenharia de Produto.

## 11. Próxima evolução documental possível

**UXA-079 — Revalidação Funcional dos Registros Granulares Reformulados**, mediante autorização separada.
