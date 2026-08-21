---
id: GKR-INTERNAL-AUTHORITY-BOUNDARY-001
title: Fronteira entre Classificação, Publicação e Finalidade de Uso
status: proposed
version: 1.2.0
owner: Guivos
last_updated: 2026-08-21
related:
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-CHRISTIAN-FOUNDATION-001
normative: true
---

# Fronteira entre Classificação, Publicação e Finalidade de Uso

## 1. Finalidade

Este documento estabelece a separação entre três dimensões que não devem ser confundidas no Guivos Knowledge Repository:

1. **classificação de sensibilidade da informação**;
2. **perfil de autoridade/publicação**;
3. **finalidade de uso do documento**.

A regra central é:

```text
CLASSIFICAÇÃO DE SENSIBILIDADE
≠ PERFIL DE AUTORIDADE
≠ FINALIDADE DE USO
```

Um documento pode, portanto, ser classificado como `public`, possuir perfil `public_foundational` e ainda ter `primary_use: internal_governance`.

## 2. Taxonomia de sensibilidade preservada

Este documento **não substitui nem cria uma nova taxonomia de confidencialidade**.

Permanece vigente a classificação já estabelecida no GKR:

| Classe | Definição | Tratamento no GKR público |
|---|---|---|
| `public` | conteúdo aprovado para divulgação externa | pode residir/publicar no GKR conforme governança aplicável |
| `internal` | conteúdo de trabalho não destinado à divulgação irrestrita | somente síntese sanitizada quando houver valor arquitetural |
| `confidential` | estratégia, ativos, contratos, dados comerciais, jurídicos ou operacionais protegidos | não publicar integralmente; somente metadados/síntese permitidos |
| `restricted` | credenciais, chaves, tokens, dados pessoais brutos, acessos, segredos técnicos ou evidência de alto impacto | publicação integral proibida |

Esta taxonomia mantém precedência para **sensibilidade e publicação**.

Referências preservadas:

- `docs/project/information-sensitivity-and-publication-control-2026-08-05.md`;
- `docs/project/p0-post-uxa084-rebaseline-2026-08-06.md`.

```text
public / internal / confidential / restricted
= TAXONOMIA DE SENSIBILIDADE VIGENTE
```

## 3. Perfil de autoridade

`public_foundational` não é uma quinta classe de confidencialidade.

É um **perfil de autoridade** aplicável a documentos que:

1. são classificados como `public` quanto à sensibilidade;
2. definem fundamentos permanentes ou de alta estabilidade;
3. integram canonicamente o GKR;
4. podem ter finalidade predominantemente ou exclusivamente interna;
5. não devem ser reutilizados automaticamente como copy comercial ou comunicação externa.

Uso recomendado de metadados:

```yaml
classification: public
authority_profile: public_foundational
primary_use: internal_governance
```

## 4. Uso interno ≠ classificação internal

```text
USO INTERNO ≠ CLASSIFICAÇÃO internal
FINALIDADE DE USO ≠ NÍVEL DE SIGILO
ARMAZENAMENTO PÚBLICO ≠ DESTINAÇÃO PÚBLICA
```

Um fundamento, princípio cultural, doutrina de propósito ou autoridade ética pode estar classificado como `public` e armazenado no GKR, mas existir **para orientar internamente a organização**.

Nesse caso, a acessibilidade pública decorre da classificação de sensibilidade e da decisão de manter o GKR como fonte oficial; ela não altera a finalidade do documento.

## 5. Conteúdo internal, confidential e restricted

Conteúdo classificado como `internal`, `confidential` ou `restricted` não pode ser colocado integralmente no GKR público apenas porque:

- não aparece no menu do MkDocs;
- está em pasta chamada `internal`;
- está em branch não mesclada;
- está em PR draft;
- está em Issue;
- está em comentário de review;
- está em artifact de workflow;
- está em arquivo com nome obscuro;
- está em commit supostamente temporário.

Em repositório público, essas superfícies devem ser tratadas como potencialmente públicas e historicamente recuperáveis.

## 6. Fundamento Cristão da Guivos

Por decisão explícita da liderança, o **Fundamento Cristão e Doutrina de Propósito da Guivos** usa a seguinte combinação de atributos:

```text
CLASSIFICAÇÃO DE SENSIBILIDADE   public
PERFIL DE AUTORIDADE             public_foundational
USO                              interno
FINALIDADE                       governança / cultura / estratégia / propósito
ARMAZENAMENTO                    Guivos Knowledge Repository
ACESSIBILIDADE                   pública por natureza do repositório
USO EXTERNO                      não automático; exige decisão contextual própria
USO COMERCIAL                    não automático
AUTORIDADE                       GKR-CHRISTIAN-FOUNDATION-001
```

Isso significa que o conteúdo pode permanecer no GKR sem ser tratado como confidencial, mas **o documento continua sendo de uso interno**.

Não significa que:

- todo produto deve expor conteúdo religioso;
- toda Home deve citar versículos;
- toda campanha deve utilizar linguagem cristã;
- fé deve ser usada como argumento de venda;
- o documento seja uma peça de comunicação destinada ao público;
- o documento deixe de ser uma autoridade interna de governança.

## 7. Relação com MkDocs e GitHub Pages

O GKR usa MkDocs e GitHub Pages como superfície documental pública.

A ausência de um arquivo no `nav` não garante confidencialidade.

Portanto:

```text
NOT_IN_NAV ≠ PRIVATE
UNLISTED ≠ internal
```

Conteúdo `public` pode estar tecnicamente acessível no corpus quando essa exposição é deliberadamente aceita.

## 8. Preservação histórica e não retroatividade

Esta autoridade não reclassifica automaticamente documentos anteriores.

Classificações existentes como `public`, `internal`, `confidential` e `restricted` permanecem válidas até que uma autoridade específica determine o contrário.

`public_foundational` deve ser aplicado apenas como **perfil complementar**, nunca como substituto da classificação de sensibilidade.

```text
PUBLIC_FOUNDATIONAL PROFILE
≠ NOVA CLASSE DE CONFIDENCIALIDADE
```

## 9. Invariantes

```text
public / internal / confidential / restricted = TAXONOMIA PRESERVADA
public_foundational = PERFIL DE AUTORIDADE
USO INTERNO ≠ CLASSIFICAÇÃO internal
FINALIDADE DE USO ≠ NÍVEL DE SIGILO
ARMAZENAMENTO PÚBLICO ≠ DESTINAÇÃO PÚBLICA
PUBLIC_FOUNDATIONAL ≠ COPY COMERCIAL
NOT_IN_NAV ≠ PRIVATE
DRAFT PR ≠ PRIVATE
DELETE ≠ UNPUBLISH
```

## 10. Critério de adoção

Esta fronteira pode ser considerada adotada quando:

- a taxonomia de sensibilidade de quatro classes permanecer preservada;
- perfis de autoridade forem tratados como dimensão separada;
- a finalidade de uso estiver explicitada separadamente da sensibilidade;
- conteúdo `internal`, `confidential` e `restricted` não for publicado integralmente contra sua classificação;
- o fundamento cristão estiver claramente identificado como **documento de uso interno mantido no GKR**, sem criar uma nova classe de confidencialidade;
- validações mecânicas e semânticas permanecerem verdes.
