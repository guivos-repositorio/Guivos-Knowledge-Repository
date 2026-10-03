---
id: GKR-P0-REBASELINE-001
title: Rebaseline da Recuperação P0 após a UXA-084
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-06
depends_on:
  - GKR-STATE-001
  - GKR-AUD-ACCUMULATED-003
  - GKR-P0-CLOSURE-001
related:
  - GKR-SOURCE-INTAKE-001
  - GKR-CLAIMS-TRACE-001
  - GKR-EXT-SOURCE-PRESERVATION-001
  - GKR-INFO-CLASS-001
normative: false
---

# Rebaseline da Recuperação P0 após a UXA-084

## 1. Finalidade

Este documento governa a recuperação dos onze artefatos produzidos no P0 pelo PR nº 164 e impede que fotografias de estado registradas em 5 de agosto de 2026 sejam interpretadas como o estado corrente do Guivos Knowledge Repository.

A recuperação preserva o conteúdo auditável do P0 sem promover fontes externas, hipóteses, resultados, produtos, operações ou decisões não comprovadas.

## 2. Motivo da recuperação

O PR nº 164 produziu trabalho material de intake, rastreabilidade, linhagem, disposição de autoridade, sensibilidade, preservação de fontes e operação do repositório. Entretanto, ele não foi integrado antes do avanço posterior da Arquitetura da Experiência.

A integração direta do PR original deixou de ser segura porque seus documentos registram como contemporâneos:

- `GKR-STATE-001` 1.99.0;
- marco M7.72;
- UXA-070 como última frente integrada;
- UXA-071 como não iniciada;
- PR nº 164 ainda em rascunho.

Essas afirmações descrevem corretamente o corte histórico auditado em 5 de agosto de 2026, mas não substituem a autoridade atual.

## 3. Autoridade temporal

Os onze artefatos recuperados permanecem snapshots documentais do P0 no head original `144926ec5042572dc3dd9228ce9bd89f53eab81a`.

Regras obrigatórias de leitura:

1. afirmações sobre baseline, marco, última UXA integrada e estado de PR possuem validade no corte original;
2. o Registro do Estado Atual integrado à `main` prevalece para o estado corrente;
3. fatos históricos comprovados, decisões de não promoção, classificações de sensibilidade e disposições de autoridade permanecem válidos até revisão explícita;
4. números de fontes, claims e desvios representam o inventário daquele corte e não garantem exaustividade futura;
5. nenhuma frase dos snapshots pode reverter ou apagar integrações posteriores;
6. divergências futuras devem ser resolvidas por evidência Git e autoridade integrada.

## 4. Estado corrente preservado

A recuperação parte da `main` no merge da UXA-084:

```text
main: 9c6a7b45eacb954e45a10d5923697f71fb88494a
UXA-084: integrada pelo PR nº 180
Galeria Visual Integrada: draft 0.4.0
Cinco páginas visuais: draft 0.2.0
Matriz de Rastreabilidade por SVG: draft 0.2.0
Catálogo Integrado: active 0.9.0
Lacunas: active 0.9.0
Jornadas Integradas: 0.12.0
Arquitetura da Experiência: 0.77.0
Registro do Estado Atual: 2.10.0
Roadmap: ROADMAP-12.57.0
UXA-085: não iniciada
Engenharia de Produto: pausada
```

A aprovação documental da UXA-084 preserva as ressalvas registradas no PR nº 180. Ela não promove automaticamente a galeria ou a matriz, não valida jornadas ponta a ponta e não inicia a UXA-085.

## 5. Conteúdo recuperado

Os seguintes arquivos são reaplicados com os blobs exatos do head original do PR nº 164:

1. `accumulated-claims-git-traceability-2026-08-05.md`;
2. `accumulated-conversations-and-sources-audit-2026-08-05.md`;
3. `contexto-vivo-external-draft-reconciliation-2026-08-05.md`;
4. `external-governance-and-knowledge-architecture-disposition-2026-08-05.md`;
5. `external-source-preservation-decision-2026-08-05.md`;
6. `gc-con-001-lineage-resolution-2026-08-05.md`;
7. `github-codex-operational-runbook-2026-08-05.md`;
8. `information-sensitivity-and-publication-control-2026-08-05.md`;
9. `p0-residual-controls-closure-2026-08-05.md`;
10. `source-intake-register-2026-08-05.md`;
11. `val-operational-evidence-audit-2026-08-05.md`.

A preservação literal evita reescrever retrospectivamente a evidência de auditoria. Este rebaseline fornece a camada de interpretação temporal necessária.

## 6. Disposições preservadas

Permanecem preservadas, nos limites de evidência registrados pelo P0:

- Git, commits, branches, PRs e autoridades integradas prevalecem sobre resumos conversacionais;
- autodeclaração externa de status não cria autoridade no GKR;
- a família externa `GC-CON-001` possui linhagem conflitante e não pode ser importada diretamente;
- fontes externas seguem abordagem `reference_first` no repositório público;
- conteúdo deve ser classificado como `public`, `internal`, `confidential` ou `restricted` antes de publicação;
- recomendações Neo4j não comprovam implantação;
- desenho VAL não comprova pré-teste, coleta, base válida, KPI, decisão ou Outcome;
- planos de marca, domínio, Fundação e internacionalização não comprovam execução;
- Guivos Mall permanece o nome arquitetural vigente e Marketplace permanece nome histórico;
- nenhum Outcome empresarial canônico é criado por esta recuperação.

## 7. Exclusões e bloqueios

Esta recuperação não inclui:

- arquivos ou validadores do P1;
- alterações em README, Home, MkDocs, changelog ou navegação global;
- reuso do gate semântico antigo que exigia UXA-071 não iniciada;
- atualização do Registro do Estado Atual;
- início da UXA-085;
- início ou retomada da Engenharia de Produto;
- execução dos pacotes P2–P9;
- publicação de fontes externas integrais;
- merge automático.

O P1 deverá ser reconstruído separadamente sobre a baseline corrente, com regras semânticas compatíveis com a UXA-084 integrada.

## 8. Gates antes de integração

O PR de recuperação deverá permanecer em rascunho até verificar:

1. correspondência dos onze blobs com o head original do PR nº 164;
2. front matter e identificadores;
3. links internos e navegação aplicável;
4. ausência de informação sensível indevida;
5. whitespace;
6. construção MkDocs em modo estrito;
7. árvore rastreada limpa;
8. ausência de alteração semântica do estado corrente;
9. ausência de promoção automática de fontes, hipóteses ou resultados;
10. separação integral entre P0 recuperado e P1 a reconstruir.

## 9. Próximo ato governado

Após validação do PR de recuperação, as opções serão:

1. solicitar correções;
2. marcar o PR como pronto para revisão;
3. autorizar sua integração;
4. manter o PR em rascunho.

Somente após a decisão sobre a recuperação do P0 deverá ser executada a reconstrução do P1. A UXA-085 permanece bloqueada durante esse saneamento de continuidade.

## 10. Resultado

```text
P0 source PR: 164
Recovered artifacts: 11
Recovery base: UXA-084 merge
Historical snapshots modified: no
Temporal qualification added: yes
P1 included: no
UXA-085 initiated: no
Automatic merge: prohibited
```
