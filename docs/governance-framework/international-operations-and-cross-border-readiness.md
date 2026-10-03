---
id: GKR-INTERNATIONAL-OPERATIONS-READINESS-001
title: Prontidão Operacional Internacional e Cross-Border
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-OPERATIONAL-LEGAL-TRUTH-001
  - GKR-LEGAL-SURFACE-GATES-001
  - GKR-DIGITAL-ASSET-CONTROL-001
  - GTM-007
related:
  - GTM-008
normative: true
---

# Prontidão Operacional Internacional e Cross-Border

## 1. Finalidade

Esta autoridade conecta P5, P6 e P7 para impedir que uma decisão de expansão territorial seja confundida com prontidão jurídica, fiscal, tecnológica, contratual ou operacional.

A unidade de análise é a **operação concreta em um território**, e não a intenção de internacionalização.

## 2. Regra central

```text
estratégia internacional
≠ autorização territorial
≠ desenho operacional
≠ conformidade revisada
≠ implementação
≠ operação evidenciada
```

Uma frente somente poderá ser descrita como `active_market` quando os objetos materiais correspondentes possuírem evidência de operação.

## 3. Camadas de prontidão

### R1 — Estratégia

Define por que o território importa, sequência, hipótese de valor e relacionamento com o GTM.

### R2 — Mercado e oferta

Valida demanda, densidade de Coletivos/Organizações, Business, parceiros, canais e proposta de valor localizada.

### R3 — Institucional e jurídico

Define entidade contratante, representação, responsabilidades, estrutura jurídica necessária e relações entre entidades.

### R4 — Privacidade e dados

Mapeia tratamentos, bases, transparência, direitos, transferências, terceiros, incidentes e controles locais.

### R5 — Fiscal, financeiro e pagamentos

Define tributação, faturação, moeda, PSP/adquirência, reconciliação, reembolsos e chargebacks.

### R6 — Consumidor e produto

Avalia contratos, informação pré-contratual, cancelamento, garantias, moderação/intermediação, marketplace, viagens, publicidade e outras obrigações derivadas do papel real dos Produtos Especializados.

### R7 — Tecnologia, segurança e operação

Define disponibilidade, observabilidade, segurança, suporte, incidentes, continuidade, terceiros críticos, SLAs e capacidade de atendimento.

### R8 — Execução e evidência

Comprova que o desenho foi implementado e operado de forma verificável.

Nenhuma camada sozinha autoriza operação.

## 4. Matriz mínima de readiness

| Domínio | Pergunta de gate | Evidência esperada antes de operação |
|---|---|---|
| estratégia | por que este território agora? | decisão, hipótese e critérios de sucesso |
| mercado | existe densidade e demanda suficiente? | discovery, pipeline qualificado e oferta |
| entidade | quem contrata e responde? | desenho jurídico e representação |
| contratos | quais termos governam cada relação? | documentos revisados e versões |
| privacidade | que dados são tratados e por quê? | mapa de tratamento, bases e controles |
| transferência | há fluxo internacional de dados? | mecanismo/decisão aplicável e registro |
| consumidor | que direitos e deveres se aplicam? | matriz de aplicabilidade e controles |
| fiscal | onde e como tributar/faturar? | parecer/validação fiscal e configuração |
| pagamentos | como cobrar, liquidar e reembolsar? | PSP/processos aprovados e testados |
| produto | quais Produtos Especializados entram? | escopo funcional e responsabilidades |
| segurança | como prevenir e responder? | controles, runbooks e testes |
| suporte | quem atende e em qual SLA? | owner, canais, idioma e capacidade |
| terceiros | quem é crítico? | contratos, due diligence e contingência |
| marca/ativos | que identidades são usadas? | estado factual e evidência de controle |
| contabilidade | como reconciliar receita/caixa/impostos? | desenho contábil e owners |
| continuidade | como pausar/encerrar? | kill criteria, rollback e retenção |

## 5. Estados de readiness por domínio

Cada linha material deverá possuir um estado independente:

- `not_assessed`;
- `assessment_in_progress`;
- `design_defined`;
- `specialist_reviewed`;
- `approved_for_implementation`;
- `implemented_nonproduction`;
- `operational_evidenced`;
- `reassessment_required`;
- `retired`.

`specialist_reviewed` não significa que o controle esteja implementado. `implemented_nonproduction` não significa operação real.

## 6. Brasil–União Europeia: dados pessoais

A baseline P7 registra duas realidades simultâneas:

1. o RGPD pode alcançar organizações não estabelecidas na UE quando há oferta de bens/serviços a pessoas na União ou monitoramento de comportamento no território europeu;
2. em 2026, Brasil e União Europeia passaram a reconhecer mutuamente adequação para transferências de dados pessoais nos termos das decisões vigentes.

A consequência arquitetural é reduzir uma classe de fricção de transferência, **não remover a governança de tratamento**.

```text
adequação de transferência
≠ base jurídica para qualquer finalidade
≠ transparência cumprida
≠ contrato com terceiro aprovado
≠ segurança comprovada
≠ retenção definida
≠ direito do titular operacionalizado
```

Referências oficiais devem ser revalidadas antes de cada promoção operacional.

## 7. Dados, produtos e territorialidade

Um mesmo Produto Especializado pode possuir diferentes papéis jurídicos e operacionais conforme o território e o fluxo.

Exemplos de perguntas, sem pressupor resposta:

- Journey hospeda conteúdo próprio, de Organizações ou ambos?
- Mall vende, intermedeia ou apenas encaminha para terceiro?
- Travel contrata, intermedeia, agrega ou redireciona?
- Ads vende mídia própria, campanha patrocinada ou inventário de terceiro?
- Business é contratado pela entidade brasileira ou futura entidade local?
- Intelligence trata dados pessoais, agregados ou anonimizados no caso concreto?
- Media hospeda conteúdo editorial, de usuário ou patrocinado?

A resposta muda a matriz de consumidor, DSA, fiscalidade, pagamentos, responsabilidade e contratos. O nome do produto não decide a obrigação.

## 8. Cross-border não é apenas dado

A arquitetura deve considerar fluxos transfronteiriços de:

- dados pessoais;
- dinheiro;
- contratos;
- propriedade intelectual;
- serviços;
- suporte;
- conteúdo;
- bens físicos quando aplicável;
- responsabilidade e reclamações;
- relatórios contábeis/fiscais;
- evidências operacionais.

Cada fluxo pode possuir autoridade e requisitos próprios.

## 9. Terceiros internacionais

Antes de tornar um terceiro crítico para um mercado ativo, registrar:

- função;
- território;
- papel contratual;
- dados acessados;
- subprocessadores quando aplicável;
- dependência técnica;
- SLA;
- segurança;
- incidentes;
- continuidade;
- saída/migração;
- propriedade dos dados e ativos;
- evidência de due diligence.

Parceiro Estratégico, PSP, cloud, CRM, analytics, fornecedor de IA ou prestador local não recebe confiança irrestrita pelo rótulo da relação.

## 10. Superfícies legais localizadas

Uma versão portuguesa/europeia de Termos, Política/Aviso de Privacidade, política de cookies, condições comerciais ou outro documento somente pode ser declarada publicada/operacional conforme os gates de `GKR-LEGAL-SURFACE-GATES-001`.

Tradução linguística ≠ localização jurídica.

```text
texto traduzido
≠ texto juridicamente revisado
≠ versão aprovada
≠ versão publicada
≠ aceite operacional registrado
```

## 11. Incidentes e continuidade

O desenho internacional deverá prever:

- classificação de incidente;
- jurisdições e titulares afetados;
- owners;
- preservação de evidência;
- comunicações regulatórias/contratuais aplicáveis;
- suporte ao usuário;
- rollback;
- continuidade de pagamentos e serviços;
- dependências de terceiros;
- encerramento de território quando necessário.

Não se deve depender de improvisação pós-incidente para descobrir quem responde em cada país.

## 12. Reporting executivo

O reporting de internacionalização deverá separar:

- `candidate territory`;
- `readiness`;
- `pilot authorized`;
- `pilot active`;
- `market active`;
- `revenue realized`;
- `entity established`;
- `asset protected`;
- `compliance control evidenced`.

Nenhum deles deve ser representado por um único selo “internacional”.

## 13. Limites

Esta arquitetura não constitui parecer jurídico, fiscal ou regulatório; não cria obrigação ou isenção concreta; não prova operação em Portugal; não cria entidade, DPO/representante, número fiscal, IVA, OSS, PSP, contrato, tratamento de dados ou ativo digital; não inicia UXA-102/V5 nem Product Engineering.
