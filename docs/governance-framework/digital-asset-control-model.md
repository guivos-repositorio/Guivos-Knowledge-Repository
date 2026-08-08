---
id: GKR-DIGITAL-ASSET-CONTROL-001
title: Modelo Governado de Registro e Controle de Ativos Digitais
status: proposed
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
normative: true
---

# Modelo Governado de Registro e Controle de Ativos Digitais

## 1. Finalidade

Este documento define o **schema e o processo de controle** de ativos digitais vinculados à Guivos sem publicar o inventário operacional sensível.

Ele permite responder, de forma auditável:

- que objeto está sendo protegido ou operado;
- qual nome canônico ele suporta;
- qual é seu estado factual;
- qual é sua criticidade;
- que evidência sustenta a afirmação;
- quem responde pelo ativo em termos funcionais;
- quando a evidência precisa ser revista;
- quais informações não podem aparecer no GKR público.

O documento não lista a carteira completa de domínios, registradores, contas, perfis, chaves ou configurações.

## 2. Unidade de registro

Cada ativo recebe um registro lógico independente.

Schema mínimo:

| Campo | Obrigatório | Regra |
|---|---|---|
| `asset_id` | sim | identificador interno estável, sem credencial |
| `asset_type` | sim | tipo governado do ativo |
| `canonical_object` | sim | marca, produto, programa ou serviço que o ativo suporta |
| `public_label` | quando público | rótulo publicável; não precisa revelar locator sensível |
| `locator_class` | sim | `public`, `masked`, `restricted` ou `secret` |
| `state` | sim | estado factual governado |
| `criticality` | sim | critical / high / medium / low |
| `evidence_ref` | para estados comprovados | referência à evidência; nunca segredo bruto |
| `evidence_date` | para estados comprovados | data da verificação |
| `owner_role` | sim | função accountable |
| `custodian_role` | quando aplicável | função operacional responsável |
| `territory_scope` | quando relevante | jurisdição/território, sem inferência global |
| `renewal_or_review_due` | quando aplicável | data de revisão/renovação |
| `dependencies` | quando relevante | serviços dependentes sem expor credenciais |
| `supersedes` | quando aplicável | ativo ou nome substituído |
| `notes_classification` | sim | classificação das notas associadas |

## 3. Tipos de ativo

Tipos iniciais suportados:

- `domain`;
- `subdomain`;
- `trademark_record`;
- `social_handle`;
- `app_store_identity`;
- `package_or_namespace`;
- `email_domain`;
- `certificate_identity`;
- `public_profile`;
- `brand_property`;
- `redirect_or_alias`;
- `other_governed_identity`.

A inclusão de um tipo não significa que a Guivos já possua ativos desse tipo.

## 4. Estados factuais

| Estado | Pode ser afirmado sem evidência? | Interpretação |
|---|---|---|
| `candidate` | sim, como intenção | ativo desejado ou em análise |
| `evidence_pending` | sim, explicitando incerteza | alegação existente sem prova suficiente |
| `confirmed_control` | não | controle administrativo/técnico verificado |
| `registered` | não | registro/titularidade comprovado para objeto e escopo indicado |
| `delegated` | não | operação atribuída a terceiro com responsabilidade comprovada |
| `active_service` | não | utilizado por serviço real comprovado |
| `suspended` | não | ativo preservado, uso suspenso de forma verificada |
| `superseded` | não | substituído formalmente |
| `retired` | não | encerrado conforme decisão/evidência |
| `unknown` | sim | não há base para afirmar outro estado |

É proibido converter `candidate` em `registered`, `confirmed_control` ou `active_service` a partir de conversa, planejamento ou pesquisa de disponibilidade.

## 5. Criticidade

### Critical

Ativo cuja perda, alteração ou indisponibilidade pode comprometer identidade institucional, autenticação, e-mail, pagamentos, tráfego principal, cadeia de confiança ou recuperação administrativa.

### High

Ativo capaz de afetar produto relevante, aquisição, reputação, distribuição, canal oficial ou operação comercial significativa.

### Medium

Ativo com impacto limitado e recuperável sem comprometer a identidade central.

### Low

Ativo experimental, temporário ou de baixo impacto, desde que não carregue segredo, confiança ou dependência crítica ocultos.

A criticidade deve considerar impacto e dependência real, não apenas valor de compra do ativo.

## 6. Evidência

O registro não armazena segredo bruto. Ele armazena referência para evidência em local apropriado.

Exemplo conceitual:

```text
asset_id: DA-0001
asset_type: domain
canonical_object: <objeto canônico>
locator_class: restricted
state: confirmed_control
evidence_ref: <referência segura para comprovação>
evidence_date: YYYY-MM-DD
criticality: critical
owner_role: <função>
custodian_role: <função>
```

Esse exemplo é schema e **não representa um ativo real da Guivos**.

## 7. Separação entre catálogo público e registro restrito

O modelo prevê duas visões:

### 7.1 Visão pública/documental

Pode conter:

- nome canônico;
- finalidade;
- política aplicável;
- estado de naming;
- informação operacional já deliberadamente pública e não sensível;
- referência sanitizada de governança.

### 7.2 Registro restrito de controle

Pode conter, em sistema apropriado:

- hostname/username completo quando não publicável;
- registrador/plataforma;
- account identifier;
- datas de renovação detalhadas;
- responsáveis nominativos;
- histórico de transferências;
- configurações administrativas;
- incidentes e recuperação;
- evidências privadas.

### 7.3 Cofre de segredos

Credenciais, recovery codes, private keys, seeds, tokens e segredos equivalentes pertencem a cofre apropriado e **nunca** ao GKR.

## 8. Regras de domínio

Para cada domínio ou subdomínio governado, o registro deve diferenciar:

```text
nome desejado
controle registral
controle DNS
uso por serviço
uso de e-mail
certificado
renovação
```

Nenhum desses estados deve ser inferido dos demais.

Exemplo:

- domínio registrado não prova que DNS esteja sob controle atual;
- DNS respondendo não prova titularidade registral;
- site acessível não prova que o domínio pertença à Guivos;
- e-mail funcionando não comprova política de segurança adequada;
- certificado válido não comprova domínio registrado em nome da entidade pretendida.

## 9. Regras de propriedade intelectual

Um registro de marca deve separar:

- sinal/nome;
- titular indicado;
- país/região;
- órgão/rota registral;
- classe(s), quando aplicável;
- estado do processo;
- número de protocolo/registro em sistema restrito ou publicável conforme decisão;
- data;
- vigência/renovação;
- oposição, exigência ou limitação relevante.

Estados sugeridos para `trademark_record` podem ser refinados em sistema jurídico, mas o GKR nunca deve resumir `filed/pending` como `registered` ou `globally protected`.

## 10. Processo de intake

Quando surgir nova alegação de ativo:

```text
alegação
→ classificar objeto
→ localizar evidência
→ validar autoridade
→ classificar sensibilidade
→ atribuir estado
→ registrar responsável funcional
→ definir revisão
→ publicar somente visão permitida
```

Se a evidência não puder ser obtida, usar `evidence_pending` ou `unknown`.

## 11. Mudança de naming e migração de ativos

Renomear produto ou propriedade pode exigir migração de domínios, handles, URLs, certificados, campanhas, documentação e referências externas.

A migração deve preservar:

- nome anterior como `superseded` quando necessário;
- redirecionamento quando adequado e comprovado;
- continuidade de identidade;
- ausência de duas autoridades correntes concorrentes;
- plano de retirada do alias;
- atualização de consumidores.

No caso já governado de `Guivos Marketplace → Guivos Mall`, o modelo deve tratar Marketplace como alias de migração, não como segundo produto corrente.

## 12. Renovação e continuidade

Para ativos renováveis, o registro restrito deve possuir:

- próxima data relevante;
- mecanismo de renovação;
- owner e backup de responsabilidade;
- forma de pagamento/contrato em sistema apropriado, sem dados sensíveis no GKR;
- alerta antecipado proporcional à criticidade;
- procedimento de falha de cobrança ou perda de acesso;
- procedimento de transferência quando houver mudança de custodiante.

## 13. Revisões periódicas

Frequência mínima recomendada por criticidade:

| Criticidade | Revisão de controle |
|---|---|
| critical | trimestral e após mudança material |
| high | semestral e após mudança material |
| medium | anual |
| low | anual ou antes de reutilização |

A frequência é política de governança; implementação de ferramenta ou calendário depende de operação própria.

## 14. Eventos que exigem revisão imediata

- mudança de nome canônico;
- mudança de titular/custodiante;
- desligamento de pessoa com acesso privilegiado;
- mudança de registrador/provedor;
- incidente de segurança;
- falha de renovação;
- alteração de DNS crítica;
- lançamento em novo território;
- novo produto/serviço dependente;
- mudança de entidade jurídica aplicável;
- aquisição, fusão ou encerramento de propriedade digital.

## 15. Indicadores de governança

Quando houver inventário operacional suficiente, podem ser medidos:

- % de ativos críticos com evidência vigente;
- % com owner/custodian definidos;
- % de ativos renováveis com revisão futura registrada;
- ativos `evidence_pending` por idade;
- aliases `superseded` ainda encontrados em superfícies correntes;
- ativos críticos dependentes de conta pessoal;
- ativos sem caminho de recuperação comprovado;
- divergências entre nome canônico e propriedade pública.

Nenhum valor de KPI é afirmado nesta versão.

## 16. Relação com o GKR

O GKR é autoridade para:

- política;
- naming canônico;
- modelo de controle;
- estado sanitizado quando comprovado;
- decisões arquiteturais decorrentes.

O GKR não deve ser usado como:

- password manager;
- cofre;
- inventário completo de superfície de ataque;
- substituto de registrador;
- ferramenta de DNS;
- sistema jurídico oficial;
- prova automática de titularidade.

## 17. Critério de adoção

O modelo está pronto para uso quando cada novo ativo puder ser classificado sem inventar fatos e quando informações críticas puderem permanecer referenciadas sem serem expostas.

A população do inventário real depende de intake de evidências e deve ocorrer em ambiente/classificação apropriados.
