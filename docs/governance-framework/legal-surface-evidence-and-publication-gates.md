---
id: GKR-LEGAL-SURFACE-GATES-001
title: Gates de Evidência e Publicação de Superfícies Legais
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GKR-DATA-PRIVACY-CONSENT-001
  - GKR-OPERATIONAL-LEGAL-TRUTH-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
  - GKR-STATE-001
normative: true
---

# Gates de Evidência e Publicação de Superfícies Legais

## 1. Finalidade

Este documento governa o ciclo de vida de Termos, avisos, políticas, contratos-padrão, consentimentos, preferências e demais superfícies legais ou regulatórias que possam ser exibidas ou aceitas por usuários, clientes, parceiros ou outros titulares.

Seu objetivo é impedir que rascunho, link, layout, texto aprovado, deployment ou clique sejam tratados como fatos equivalentes.

## 2. Regra central

```text
necessidade identificada
≠ texto redigido
≠ revisão jurídica
≠ aprovação interna
≠ implementação técnica
≠ publicação
≠ aceite/consentimento registrado
≠ operação comprovada
```

Cada superfície deverá possuir objeto, owner, versão, estado, evidência e escopo de aplicação próprios.

## 3. Tipos de superfície candidatos

A necessidade concreta poderá exigir, entre outras:

- Termos de Uso gerais;
- Aviso ou Política de Privacidade;
- aviso de cookies e/ou centro de preferências;
- termos de produto ou programa;
- termos de Guivos Business;
- condições comerciais;
- regras de comunidade;
- autorização ou consentimento específico quando aplicável;
- preferência de comunicação/marketing;
- aviso de integração com terceiro;
- Data Processing Agreement ou instrumento equivalente;
- cláusulas de proteção de dados em contratos;
- canal/instruções para direitos de titulares;
- avisos para públicos ou tratamentos específicos.

A lista não declara que esses documentos já sejam necessários, existentes ou publicados em todos os produtos.

## 4. Estados LS0–LS8

### LS0 — obrigação ou necessidade identificada

Existe uma razão jurídica, contratual, regulatória ou de transparência para avaliar uma superfície.

Não comprova texto, aprovação ou publicação.

### LS1 — escopo e owner definidos

Estão identificados:

- entidade responsável candidata;
- público;
- produto/jornada/canal;
- finalidade;
- dependências;
- owner de negócio;
- owner jurídico/compliance quando aplicável.

### LS2 — conteúdo em draft

Existe uma versão redigida e identificável.

`draft` não deve ser apresentado como política vigente.

### LS3 — revisão especializada concluída

O conteúdo foi revisado por competência adequada ao contexto, incluindo revisão jurídica quando necessária.

A evidência deve registrar versão, data, escopo e responsável.

### LS4 — aprovação interna

A versão está formalmente aprovada para implementação/publicação pela autoridade competente.

A aprovação não comprova publicação.

### LS5 — implementação técnica validada

A superfície foi implementada no canal alvo e testada quanto a:

- versão correta;
- disponibilidade;
- navegação;
- acessibilidade proporcional;
- comportamento de aceite/preferência quando houver;
- armazenamento de evidência quando necessário;
- rollback/versionamento.

### LS6 — publicação evidenciada

A versão aprovada está efetivamente disponível no canal definido e há evidência datada de sua publicação.

Uma URL sem conteúdo verificado não satisfaz LS6.

### LS7 — aceite, consentimento ou preferência operacionalmente evidenciado

Aplicável somente quando a superfície depende de manifestação ou registro do titular/usuário.

A evidência deverá distinguir o tipo de ato:

```text
aceite contratual
≠ consentimento de proteção de dados
≠ preferência voluntária
≠ mera ciência
```

Nem toda superfície precisa de LS7.

### LS8 — assurance operacional

Há evidência de operação contínua compatível com o desenho, incluindo quando aplicável:

- versionamento;
- logs/registros;
- revogação ou alteração de preferência;
- tratamento de versões anteriores;
- auditoria/amostragem;
- tratamento de incidentes;
- revisão periódica;
- despublicação/substituição controlada.

## 5. Registro mínimo de superfície

Cada superfície relevante deverá possuir, quando aplicável:

| Campo | Descrição |
|---|---|
| `surface_id` | identificador estável |
| nome | nome funcional |
| tipo | termos, aviso, política, consentimento, preferência, contrato etc. |
| entidade responsável | quando evidenciada |
| público | usuários/titulares/cliente/contraparte |
| produto/canal | onde se aplica |
| jurisdição/idioma | escopo aplicável |
| versão | versão do conteúdo |
| estado LS | LS0–LS8 |
| data de vigência | somente quando aprovada/publicada |
| owner | responsável |
| revisão jurídica | estado/evidência |
| URL/local | somente quando existente |
| manifestação exigida | nenhuma, aceite, consentimento, preferência etc. |
| mecanismo de prova | quando necessário |
| supersede | versão anterior |
| evidências | links/artefatos |

## 6. Termos de Uso

Termos de Uso são instrumento contratual ou regulatório conforme seu desenho e contexto.

O P6 exige separar:

- existência do texto;
- aprovação;
- publicação;
- mecanismo de aceite;
- prova do aceite;
- versão aceita;
- efeito de atualização dos Termos.

A Guivos não deve afirmar “o usuário aceitou os Termos” apenas porque visitou uma página, salvo se o modelo jurídico aplicável e a evidência efetivamente sustentarem essa conclusão.

## 7. Aviso/Política de Privacidade

Um aviso de privacidade deverá descrever os tratamentos reais ou aprovados para o escopo publicado, e não uma lista genérica de possibilidades sem correspondência operacional.

A publicação de um aviso:

```text
não cria base jurídica inexistente
não substitui minimização
não substitui contrato com operador
não substitui segurança
não substitui atendimento de direitos
não transforma consentimento inválido em válido
```

Mudanças materiais de finalidade, agentes, compartilhamentos ou direitos podem exigir revisão e atualização da superfície aplicável.

## 8. Cookies e preferências

Banner de cookies não deverá ser criado por mera convenção visual.

Primeiro deve existir inventário das tecnologias realmente utilizadas e sua classificação por finalidade e base jurídica. Depois, são definidos os controles necessários.

Quando consentimento ou escolha do titular for utilizada, o mecanismo deve permitir manifestação coerente com o contexto e revogação/alteração quando aplicável.

O P6 não declara que cookies não necessários estejam atualmente em uso na Guivos.

## 9. Marketing e comunicações

Preferência de receber comunicação e tratamento de dados para determinada finalidade são objetos governados.

O mecanismo futuro deverá separar, quando necessário:

- comunicação transacional necessária ao serviço;
- comunicação operacional;
- conteúdo solicitado;
- marketing/promocional;
- comunicações de parceiros;
- pesquisas;
- notificações de produto.

Não se deve presumir que contratar, criar conta ou participar do ecossistema autoriza toda forma de comunicação promocional.

## 10. Produtos e jurisdições

Uma superfície geral não deve ser automaticamente aplicada a todos os Produtos Especializados, segmentos B2B, países ou relações jurídicas.

Journey, Mall, Travel, Business, Media, Intelligence e Ads poderão exigir regras complementares conforme atividade real.

Expansão para nova jurisdição exige avaliação das superfícies aplicáveis; tradução de um documento brasileiro não comprova adequação jurídica local.

## 11. Dados sensíveis, menores e contextos vulneráveis

Tratamentos que envolvam dados pessoais sensíveis, crianças/adolescentes ou outras condições de vulnerabilidade poderão exigir desenhos e superfícies adicionais.

Nenhuma dessas condições é declarada operacionalmente ativa por este documento.

O gate correspondente deverá ser definido antes do tratamento real.

## 12. Contratos B2B e DPA

Guivos Business ou outras relações B2B poderão exigir instrumentos próprios de proteção de dados, inclusive definição dos papéis de agentes de tratamento, instruções, suboperadores, segurança, incidentes, transferências, retenção e término.

`contrato comercial assinado` não significa que todas as responsabilidades de proteção de dados estejam corretamente modeladas.

## 13. Estados atuais das superfícies

No momento de criação do P6 não há, no GKR auditado, evidência suficiente para promover as seguintes superfícies a `LS6 published` ou superior:

| Superfície | Estado governado no P6 |
|---|---|
| Termos de Uso gerais | `not_evidenced` |
| Aviso/Política de Privacidade pública | `not_evidenced` |
| aviso/centro de preferências de cookies | `not_evidenced` |
| registro de aceite de Termos | `not_evidenced` |
| consentimento LGPD em produção | `not_evidenced` |
| preferências de marketing em produção | `not_evidenced` |
| canal formal de direitos LGPD da Guivos | `not_evidenced` |
| DPA padrão Guivos | `not_evidenced` |
| termos específicos de Guivos Business | `not_evidenced` |

`not_evidenced` descreve o estado do conhecimento governado no GKR, não uma negação absoluta sobre artefatos externos ainda não auditados.

## 14. Versionamento e substituição

Toda superfície publicada relevante deverá poder responder:

- qual versão estava vigente em uma data;
- quem aprovou;
- onde foi publicada;
- o que mudou;
- quem precisava ser notificado;
- se novo aceite/consentimento era necessário;
- como versões anteriores são preservadas para prova;
- quando a versão foi substituída.

O texto atual não deve apagar a evidência da versão histórica aplicável a um evento passado.

## 15. Gate para afirmação pública

Somente LS6 autoriza afirmar que uma superfície está publicada.

Somente LS7, quando pertinente, autoriza afirmar que o mecanismo correspondente de manifestação está operacionalmente evidenciado.

Somente LS8 autoriza descrever a superfície como processo continuamente governado com assurance operacional.

Nenhuma passagem de tempo promove um estado automaticamente.

## 16. Limites

Este documento não escreve o conteúdo final de Termos, Política de Privacidade, DPA, banner ou consentimento; não publica superfícies; não aprova jurisdição; e não constitui aconselhamento jurídico específico.
