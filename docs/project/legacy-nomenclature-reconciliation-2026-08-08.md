---
id: GKR-LEGACY-NOMENCLATURE-RECONCILIATION-001
title: Reconciliação transversal de nomenclaturas legadas — 2026-08-08
status: in-review
version: 0.2.0
owner: Guivos
last_updated: 2026-08-08
---

# Reconciliação transversal de nomenclaturas legadas — 2026-08-08

## 1. Objetivo

Este registro governa a etapa `P1.1 — Reconciliação de Nomenclaturas Legadas` da ressincronização ampla do Guivos Knowledge Repository.

O objetivo é impedir que nomenclaturas substituídas continuem sendo apresentadas como autoridade vigente em documentos, tabelas, jornadas, superfícies, wireframes, exemplos, matrizes, arquitetura de produto ou materiais públicos do GKR.

A limpeza não destrói evidência histórica. Termos antigos permanecem quando o documento é inequivocamente histórico, superseded, arquivado ou quando a própria autoridade canônica precisa registrar a substituição.

## 2. Baseline auditada

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- branch-base: `main`;
- SHA-base: `9a0de25e664aab65b83c76ca5414c444dad893ae`;
- data da baseline: `2026-08-08`;
- autoridade principal de planos: `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`;
- integração que consolidou a autoridade corrente: PR `#207`;
- arquitetura oficial de produtos consultada: `GPA-000`.

## 3. Taxonomia vigente de planos

| Papel / produto | Taxonomia vigente |
|---|---|
| Pessoa | Free · Plus · Pro |
| Coletivo | Livre · Mobiliza · Impacta · Rede |
| Organização | Conecta · Eleva · Transforma |
| Guivos Business | Start · Growth · Scale · Enterprise |

Regras estruturais obrigatórias:

- `Pessoa`, `Coletivo` e `Organização` são papéis estruturais de participante;
- `Guivos Business` é Produto Especializado/contrato e não um quarto tipo de participante;
- `Organização ≠ Guivos Business`;
- `Organização Transforma ≠ Guivos Business Enterprise`;
- não existe correspondência automática 1:1 entre `Conecta / Eleva / Transforma` e `Start / Growth / Scale / Enterprise`;
- escolha de plano representa profundidade, capacidade, escopo e complexidade de serviço, nunca valor humano, mérito ou status da pessoa.

## 4. Substituições comprovadas

As seguintes nomenclaturas são legadas quando usadas para afirmar a taxonomia ou o naming atual:

| Nomenclatura legada | Autoridade vigente |
|---|---|
| Coletivo Gestão | Coletivo Mobiliza |
| Coletivo Impacto | Coletivo Impacta |
| Coletivo Enterprise | Coletivo Rede |
| Organização Start | Organização Conecta |
| Organização Growth | Organização Eleva |
| Organização Scale | Organização Transforma |
| Guivos Marketplace | Guivos Mall |

`Start`, `Growth`, `Scale` e `Enterprise` não são termos globalmente obsoletos. Permanecem vigentes como tiers do Produto Especializado `Guivos Business`. `Enterprise` também aparece legitimamente em `Guivos Enterprise Architecture` e em terminologia externa. Por isso, os tokens exigem classificação por contexto antes de alteração.

`Guivos Marketplace` pode permanecer em autoridade de migração ou histórico somente para registrar que o nome oficial vigente é `Guivos Mall`.

## 5. Regra de correção

A reconciliação segue quatro classes:

1. **autoridade corrente incorreta** — corrigir para a nomenclatura vigente;
2. **derivado corrente incorreto** — corrigir e alinhar ao documento de autoridade;
3. **evidência histórica ou de migração legítima** — preservar, mantendo a condição histórica explícita;
4. **ocorrência ambígua** — não substituir automaticamente; abrir revisão semântica.

É proibida substituição textual cega de palavras genéricas como `gestão`, `impacto`, `rede`, `marketplace`, `Start`, `Growth`, `Scale` ou `Enterprise` fora de contexto governado.

## 6. Resultado do primeiro inventário mecânico

O primeiro ciclo do gate encontrou:

| Classe | Quantidade inicial | Interpretação |
|---|---:|---|
| violações vivas exatas | **40** | nomenclaturas comprovadamente legadas em superfícies correntes |
| ocorrências históricas/referenciais | **24** | evidência preservável, não bloqueante |
| candidatos Business-tier para revisão semântica | **179** | tokens ambíguos que não permitem mass-replace |

As 40 violações vivas iniciais foram corrigidas no escopo conhecido. O gate intermediário chegou a `0` violações exatas antes da inclusão do alias `Guivos Marketplace`.

A ampliação do controle para `Guivos Marketplace → Guivos Mall` revelou quatro ocorrências correntes. A revisão individual demonstrou que todas as quatro eram **autoridades explícitas de migração**, não uso corrente incorreto:

- glossário;
- índice da Product Architecture;
- front matter de `Guivos Mall` com `former_name`;
- declaração do próprio documento do Mall de que o novo nome substitui o anterior.

Esses arquivos foram classificados como referências de migração permitidas. O uso de `Guivos Marketplace` fora dessas autoridades e do histórico permanece bloqueável.

## 7. Desvios materiais corrigidos

### 7.1 Coletivo

A jornada, registros e autoridades econômicas ainda continham a escada antiga `Livre → Gestão → Impacto → Enterprise`.

Leitura corrente reconciliada:

```text
Livre → Mobiliza → Impacta → Rede
```

Os valores econômicos candidatos foram preservados no degrau correspondente quando já havia autoridade econômica; a mudança de nome não cria nova capacidade, preço ou entitlement.

### 7.2 Organização e Guivos Business

Foram encontradas autoridades derivadas ainda usando `Business Start / Growth / Scale` como se fossem planos da Organização.

Leitura corrente reconciliada:

```text
Organização: Conecta → Eleva → Transforma
Guivos Business: Start → Growth → Scale → Enterprise
```

Os preços candidatos historicamente governados para a jornada institucional foram preservados sob `Organização Conecta / Eleva / Transforma`. Eles **não** foram migrados para Guivos Business.

Guivos Business continua sem tabela própria de preço/entitlement nesta frente.

### 7.3 BND-002

Diversos derivados ainda descreviam `BND-002` como processo ou fronteira `Enterprise/Scale`.

Leitura vigente:

> `BND-002` é uma fronteira genérica de contratação/dimensionamento assistido quando o autoatendimento não é suficiente.

Ela não pertence semanticamente a Enterprise, Scale, Rede, Transforma, Coletivo, Organização ou produto específico.

### 7.4 UXA-100-A2

A auditoria funcional original ainda narrava a nomenclatura antiga, embora os SVGs canônicos já estivessem atualizados.

A reconciliação preserva o fato histórico da auditoria e sua conclusão funcional, mas faz a leitura corrente utilizar:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business separado: `Start · Growth · Scale · Enterprise`.

### 7.5 Opportunity Boost

O uso de Start/Growth/Scale como proxy de elegibilidade da Organização para Boost foi removido.

Isso revelou uma pendência real, antes mascarada pela nomenclatura antiga:

> **o entitlement de Opportunity Boost para Organização precisa ser reconciliado especificamente com Conecta/Eleva/Transforma ou com outra autoridade econômica válida.**

A P1.1 não inventa essa elegibilidade.

## 8. Áreas tocadas

A correção alcançou, entre outras:

- modelo gratuito/pago;
- catálogo de arquétipos;
- catálogo comercial de planos e preços;
- política de oferta/upgrade/downgrade/cancelamento;
- premissas de precificação;
- baseline comercial;
- contrato econômico e baseline do Opportunity Boost;
- jornada do Coletivo;
- jornada da Organização;
- catálogo e registros granulares de jornadas;
- matriz de rastreabilidade dos SVGs;
- UXA-100-A2;
- índice da Arquitetura da Experiência;
- roadmap arquitetural;
- wireframe de elegibilidade do Boost;
- README;
- controle mecânico permanente de nomenclatura.

As contagens canônicas de UXA foram preservadas onde a mudança foi exclusivamente semântica.

## 9. Classificação dos candidatos ambíguos

O relatório de `Start/Growth/Scale/Enterprise` é deliberadamente não bloqueante porque mistura usos semanticamente distintos.

Famílias já reconhecidas como legítimas incluem:

- `Guivos Enterprise Architecture` e termos de Enterprise Architecture;
- `Enterprise Programs` e `Enterprise Delivery`;
- tiers correntes de Guivos Business;
- declarações negativas/corretivas como `BND-002 ≠ Enterprise/Scale`;
- referências científicas ou externas que usam `growth` ou `enterprise` em sentido próprio;
- nomes de domínio GTM, como `Go-to-Market, Growth & Capital`.

O relatório permanece útil como detector humano de deriva, mas não autoriza troca automática.

## 10. Estado e dívidas não absorvidas pela P1.1

A P1.1 não deve ser confundida com o rebaseline completo do GKR.

Foram observadas dívidas que pertencem às etapas seguintes:

- `GKR-STATE-001` ainda referencia versões anteriores de alguns derivados de jornada;
- o Public Canon permanece anterior aos avanços recentes e deve ser reconciliado em P9;
- P2 ainda precisa integrar a arquitetura tecnológica/grafo de referência;
- P8 ainda precisa reconstruir a visão dos sete Produtos Especializados contra a autoridade corrente;
- o entitlement de Opportunity Boost para Organização permanece pendente de autoridade específica;
- outras nomenclaturas somente serão bloqueadas quando houver evidência inequívoca de supersessão.

## 11. Controle mecânico permanente

Foi introduzido `scripts/validate_legacy_nomenclature.py` e integrado ao workflow `GKR Mechanical Validation`.

O gate:

- bloqueia nomenclatura comprovadamente legada quando afirmada em superfície corrente;
- informa ocorrências históricas/referenciais sem falhá-las;
- permite autoridades explícitas de migração;
- sinaliza `Start/Growth/Scale/Enterprise` fora de contextos explicitamente Business/econômicos/GTM para revisão humana;
- evita mass-replace semântico.

O conjunto de regras poderá ser ampliado somente quando nova substituição possuir autoridade comprovada.

## 12. Critério de conclusão da P1.1

A etapa somente pode ser considerada concluída quando:

1. todas as violações vivas conhecidas estiverem corrigidas ou legitimamente classificadas;
2. ocorrências ambíguas materiais tiverem sido revisadas;
3. referências históricas/de migração legítimas estiverem preservadas de forma inequívoca;
4. nenhum documento corrente reatribuir `Start/Growth/Scale` a Organização;
5. nenhum documento corrente usar os nomes antigos de Coletivo como taxonomia vigente;
6. `Organização ≠ Guivos Business` permanecer preservado em todos os derivados tocados;
7. `BND-002` permanecer semanticamente genérico;
8. `Guivos Mall` permanecer nome oficial do produto, com Marketplace somente como referência histórica/de migração;
9. o gate mecânico passar;
10. o gate semântico do GKR permanecer verde.

## 13. Relação com a ressincronização ampla

A P1.1 antecede a consolidação dos demais pacotes para evitar propagação de taxonomia obsoleta.

Depois de concluída, a sequência recomendada permanece:

`P2 → P8 → P3 → P4 → P5 → P6 → reconciliação P7 → P9`.

Nenhuma implantação técnica, contratação, campanha, alteração societária, investimento ou merge é autorizado por este registro.
