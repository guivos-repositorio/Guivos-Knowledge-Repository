---
id: GKR-OPERATIONAL-PRIVACY-LEGAL-INDEX-001
title: Verdade Operacional, Privacidade, Consentimentos e Superfícies Legais — Índice P6
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-LEGAL-SURFACE-GATES-001
  - GKR-OPERATIONAL-LEGAL-TRUTH-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
  - GKR-STATE-001
normative: false
---

# Verdade Operacional, Privacidade, Consentimentos e Superfícies Legais — P6

## 1. Propósito

O P6 governa a transição entre princípios/arquitetura e fatos operacionais verificáveis nos domínios de dados pessoais, privacidade, consentimentos, Termos, avisos, direitos dos titulares, segurança relacionada a dados e demais superfícies legais.

A regra transversal é:

```text
desenho
≠ implementação
≠ publicação
≠ manifestação registrada
≠ uso real
≠ controle contínuo
```

## 2. Documentos

### Governança de Dados Pessoais, Privacidade e Consentimentos

[Governança de Dados Pessoais, Privacidade e Consentimentos](data-privacy-and-consent-governance.md)

Define:

- atividade de tratamento como unidade de governança;
- titular como pessoa natural, sem confusão com papéis de participante;
- controlador/operador por realidade da atividade;
- base jurídica separada de consentimento;
- aceite contratual separado de consentimento LGPD;
- governança de dados sensíveis, inferências, perfis e derivados;
- compartilhamento, terceiros, cookies/SDKs, direitos, Encarregado, incidentes e retenção;
- estado atual explicitamente não operacional quando não evidenciado.

### Gates de Evidência e Publicação de Superfícies Legais

[Gates de Evidência e Publicação de Superfícies Legais](legal-surface-evidence-and-publication-gates.md)

Define LS0–LS8, de necessidade identificada até assurance operacional, para:

- Termos;
- avisos/políticas;
- consentimentos;
- preferências;
- cookies;
- contratos e superfícies B2B;
- documentos específicos de produto ou jurisdição.

### Registro de Verdade Operacional e Legal

[Registro de Verdade Operacional e Legal](operational-and-legal-truth-registry.md)

Define OT0–OT8 e a regra de evidência para separar:

- desenho;
- aprovação;
- implementação não produtiva;
- deployment;
- operação evidenciada;
- controle;
- assurance;
- sustentabilidade operacional.

Também registra o estado máximo atualmente suportado pelo GKR para os principais objetos P6.

## 3. Estado corrente

No checkpoint de criação do P6, a autoridade documental sustenta arquitetura e guardrails, mas não comprova operação de privacidade em produção.

| Objeto | Estado no conhecimento governado |
|---|---|
| arquitetura de privacidade | proposta/referência |
| inventário de tratamentos | `not_evidenced` |
| bases jurídicas revisadas por atividade | `not_evidenced` |
| consentimentos em produção | `not_evidenced` |
| aceite de Termos em produção | `not_evidenced` |
| Termos públicos versionados | `not_evidenced` |
| Aviso/Política de Privacidade pública versionada | `not_evidenced` |
| inventário de cookies/SDKs | `not_evidenced` |
| canal operacional de direitos | `not_evidenced` |
| Encarregado formalmente indicado | `not_evidenced` |
| processo operacional de incidentes com dados pessoais | `not_evidenced` |
| política operacional de retenção por atividade | `not_evidenced` |
| mapa completo de operadores/suboperadores | `not_evidenced` |
| transferências internacionais de dados | `not_evidenced` |
| dados pessoais em Neo4j/produção | `not_evidenced` |

`not_evidenced` significa que o GKR não possui evidência governada suficiente para promover o fato; não é afirmação absoluta sobre artefatos externos não auditados.

## 4. Distinções obrigatórias

### Participação × proteção de dados

```text
Pessoa / Coletivo / Organização
≠ titular / controlador / operador
```

Titular é pessoa natural. Uma relação B2B ou comunitária não elimina direitos das pessoas naturais envolvidas.

### Contrato × consentimento

```text
aceitar Termos
≠ consentir com todos os tratamentos de dados
```

Consentimento é uma hipótese jurídica específica e não deve ser usado como solução universal.

### Política × conformidade

```text
Política de Privacidade publicada
≠ conformidade operacional comprovada
```

O conteúdo público precisa corresponder aos tratamentos e controles reais.

### Entidade relacionada × compartilhamento

```text
vínculo societário/institucional
≠ base jurídica
≠ permissão automática de dados
```

A separação P5 permanece integralmente aplicável.

### Arquitetura de grafo × produção

```text
Neo4j reference_selected
≠ dado pessoal carregado
≠ produção autorizada
```

`GEA-GRAPH-REFERENCE-001` exige segurança/privacidade para produção e continua sem evidenciar dados reais no grafo.

## 5. Baseline regulatório brasileiro

O P6 foi estruturado considerando a LGPD e atos vigentes da ANPD consultados no momento da elaboração, incluindo regulamentação sobre Encarregado e comunicação de incidentes.

Esse referencial deve ser verificado novamente antes de implementação, publicação ou operação, especialmente quando houver mudança de jurisdição, atividade, categoria de dados, público ou tecnologia.

## 6. Próxima maturidade legítima

Após integração do P6, o próximo avanço operacional de privacidade não é escrever uma política genérica.

A sequência recomendada é:

1. inventariar tratamentos reais/candidatos por produto e operação;
2. identificar entidades e agentes por atividade;
3. classificar dados, finalidades, fontes, compartilhamentos e derivados;
4. revisar bases jurídicas e riscos;
5. definir retenção, direitos, segurança e terceiros;
6. derivar as superfícies legais realmente necessárias;
7. obter revisão jurídica aplicável;
8. implementar e testar controles;
9. publicar somente versões correspondentes à realidade;
10. capturar evidência operacional e assurance.

## 7. O que o P6 não autoriza

- coleta de dados pessoais;
- dados sensíveis;
- tracking/cookies opcionais;
- consentimento em produção;
- Política de Privacidade pública;
- Termos públicos;
- DPA;
- nomeação de Encarregado;
- contratação de operador;
- transferência internacional;
- processamento em Neo4j;
- campanha de marketing;
- uso de dado para Ads;
- decisão automatizada;
- produção de Guivos Intelligence com dados pessoais;
- declaração pública de conformidade LGPD.

## 8. Relação com P5 e próximas frentes

P5 responde **quem poderá existir juridicamente e como entidades devem permanecer separadas**.

P6 responde **como atividades, dados, superfícies e fatos operacionais devem ser evidenciados**.

P7 continuará tratando internacionalização e deverá consumir estes gates antes de converter expansão territorial em operação de dados em nova jurisdição.

P9 somente poderá produzir Canon/páginas públicas finais depois que os estados factuais das frentes anteriores estiverem reconciliados.
