---
id: GKR-PROFESSIONAL-GEB-OA-RECON-20261113
title: Profissional — Exame focal GEB e Oportunidades Ativas
status: proposed_non_normative
version: 0.1.0
owner: Guivos
last_updated: 2026-11-13
normative: false
---

# Profissional — Exame focal GEB e Oportunidades Ativas

## Finalidade

Examinar, sem alteração automática de documentos superiores, os efeitos da diretriz de incluir **Profissional** como participante ofertador de oportunidades no ecossistema Guivos.

A formulação para enumeração geral permanece **Pessoas, Profissionais, Organizações e Coletivos**. Isso não significa que os quatro possuam as mesmas permissões ou fluxos.

## Evidências confrontadas

| Documento | Constatação | Impacto |
| --- | --- | --- |
| [Modelo Fundamental da Jornada — KU-FM-002](../geb/part-02-fundamental-model/fundamental-journey.md) | A definição do participante exemplifica Pessoa, Organização e Coletivo | Examinar se o Profissional é modalidade de representação/atuação da Pessoa ou participante estrutural distinto, sem criar contradição ontológica |
| [Oportunidades Ativas — fundamentos](../product-architecture/pas-001-oportunidades-ativas-fundamentos-iniciais.md) | Profissional aparece como ator de orientação e entre entidades de oferta, mas a enumeração inicial de participantes destaca apenas Pessoa, Organização e Coletivo | Reconciliar taxonomia de ofertadores e responsabilidades, sem presumir publicação já autorizada |
| [Cadastro de Oportunidades — Organização](../experience-architecture/organizations-collectives-journey/organization-opportunity-registration-master.md) | Declara responsabilidade específica de Organização para cadastro e submissão | Não copiar ORG-002 nem permissões institucionais para Profissional |
| [Participante Profissional — novo registro](../participants/professional.md) | Registra direção conceitual de Profissional ofertador | Exige validação contra autoridades superiores antes de ampliar poderes |
| [Guia Oficial GOG-001](guia-oficial-da-guivos.md) | A redação da nova versão encontra-se proposta nesta PR; a versão atual da main permanece distinta | A publicação de texto institucional deve acompanhar a adjudicação de GEB e oportunidades |

## Questões que exigem decisão

**PRO-REC-01 — Identidade:** esclarecer se Profissional constitui papel próprio assumido por uma Pessoa com representação específica ou uma quarta natureza estrutural de participante no domínio. Preservar a identidade da Pessoa e a segregação entre contextos.

**PRO-REC-02 — Direito de ofertar:** explicitar quais modalidades de oportunidades podem ser cadastradas e publicadas por Profissionais, em quais condições e com quais validações ou credenciais.

**PRO-REC-03 — Autoridade e responsabilidade:** especificar quem é o titular da oferta, quem assume termos e responsabilidades e quais controles são diferentes dos aplicáveis a Organização e Coletivo.

**PRO-REC-04 — Experiência e dados:** definir jornada, perfil, campos de cadastro, estados, notificações, revisões, dados de contato e fronteiras de privacidade.

**PRO-REC-05 — Integração:** delimitar relações com Journey, Intelligence, Guivos AI, oportunidades convencionais/ao vivo e eventual patrocínio, sem presumir ativação.

**PRO-REC-06 — Governança econômica:** examinar taxas, planos, comissões, direitos e obrigações sem herdar automaticamente condições de O/C.

## Recomendação de encaminhamento

1. Registrar a inclusão em textos gerais, com remissão ao [Profissional](../participants/professional.md).
2. Preservar documentos de escopo específico (ex.: ORG-002) e histórico, evitando substituição em massa.
3. Decidir **PRO-REC-01** antes de modificar contratos fundamentais do GEB.
4. Decidir **PRO-REC-02 e PRO-REC-03** antes de habilitar publicação de oportunidades.
5. Atualizar o Guia Oficial somente após reconciliação normativa necessária.

## Estado

Exame focal realizado; **nenhuma das seis questões foi adjudicada por este documento**. Nenhuma nova permissão de acesso, cadastro, publicação, monetização, teste ou implementação foi autorizada.

Este documento é candidato nesta PR e não altera as autoridades mencionadas.


## Exame aprofundado — PRO-REC-01 (13/11/2026)

**Alcance do acordo:** a manifestação “de acordo” autorizou prosseguir na formalização e no exame da identidade, sem indicar expressamente qual alternativa de natureza ontológica deve prevalecer. A opção abaixo é **recomendação candidata, não adjudicação**.

### Alternativas examinadas

| Alternativa | Descrição | Vantagens e tensões |
| --- | --- | --- |
| **A — identidade de atuação vinculada à Pessoa** | Uma Pessoa humana pode atuar no contexto **Profissional**, com perfil, responsabilidades e oferta separados de sua Jornada pessoal | Preserva a natureza humana definida para Pessoa, evita duplicar identidade pessoal e permite contratos específicos; exige controles de contexto, representação e autorização |
| **B — quarto participante estrutural independente** | Profissional como nova categoria ontológica paralela e independente de Pessoa, Organização e Coletivo | Facilita enumerações simples, mas traz tensão com a base atual do GEB e a natureza humana da atuação profissional; exigiria revisão explícita do modelo superior |
| **C — subcategoria de Organização** | Profissional tratado como derivação institucional de Organização | Não se sustenta como regra geral; atuação profissional individual não equivale à identidade institucional |

### Orientação recomendada

**Alternativa A** como melhor hipótese de reconciliação do corpus:

> **Profissional é a identidade funcional de atuação e oferta assumida por uma Pessoa no ecossistema, distinta de sua Jornada pessoal, com contexto, perfil, competências, responsabilidades, oportunidades, permissões e experiências próprias.**

As enumerações públicas podem apresentar **Pessoas, Profissionais, Organizações e Coletivos** porque identificam **contextos de participação e atuação**. Isso não exige concluir, sem decisão, que existem quatro naturezas ontológicas básicas independentes.

### Contratos e limites a preservar

1. A **Pessoa** mantém a identidade humana, autonomia e proteção do contexto pessoal.
2. O **Profissional** recebe contexto de atuação próprio, cuja autoridade para ofertar depende de contratos específicos.
3. Mesmo havendo vínculo de identidade, dados íntimos da Jornada da Pessoa não se tornam automaticamente dados acessíveis na Jornada do Profissional.
4. **Organização** conserva responsabilidade institucional; **Coletivo**, governança coletiva; **Profissional**, atuação individual profissional — sem transferência automática de privilégios.
5. O GEB (`KU-FM-002`) deverá ser reconciliado mediante decisão específica de terminologia e escopo, preservando seus invariantes.
6. A definição não ativa automaticamente cadastro, publicação, relações, analytics, pagamentos ou disponibilização de oportunidades.
7. A implantação poderá adotar identidades, contextos e permissões tecnicamente separados, mas isso exige autorização técnica posterior.

### Estado de PRO-REC-01

**EXAMINADO / ALTERNATIVA A RECOMENDADA / DECISÃO NORMATIVA PENDENTE.**

**Próximo gate:** aprovar ou rejeitar expressamente a alternativa A e a definição candidata antes de editar o Modelo Fundamental da Jornada ou promover a proposta para o Guia Oficial.


## Decisão da Direção — PRO-REC-01 (13/11/2026)

**Manifestação:** a Direção respondeu “de acordo” à recomendação expressa de aprovar a **alternativa A — identidade de atuação vinculada à Pessoa**.

**Decisão conceitual aprovada:** Profissional é a identidade funcional de atuação e oferta assumida por uma Pessoa no ecossistema Guivos, distinta de sua Jornada pessoal, com contexto, perfil, competências, responsabilidades, oportunidades e permissões próprias.

A enumeração **Pessoas, Profissionais, Organizações e Coletivos** designa contextos relevantes de participação, não estabelece por si quatro naturezas humanas ou ontológicas independentes.

Esta decisão encerra **PRO-REC-01 quanto ao enquadramento conceitual**. As questões **PRO-REC-02 a PRO-REC-06 permanecem pendentes**. Não há autorização de implementação, publicação funcional, acesso irrestrito a dados ou promoção automática de contratos de oportunidades.

**Handoff documental:** proposta focal de reconciliação do `KU-FM-002` e da redação institucional `GOG-001` preparada nesta mesma branch. A PR continua em rascunho, e sua integração depende de revisão e autorização próprias.


## Exame focal — PRO-REC-02: ofertar, cadastrar e publicar oportunidades (13/11/2026)

**Escopo:** análise documental para fundamentar a futura decisão sobre o direito de oferta do Profissional. Não cria permissão operacional.

### 1. Distinções indispensáveis

- **Ser Profissional**: assumir uma identidade funcional de atuação vinculada à Pessoa (PRO-REC-01).
- **Poder ofertar conceitualmente**: categoria de participante contemplada como potencial origem de oportunidades.
- **Poder cadastrar**: possuir autorização para criar e manter rascunhos em superfície governada.
- **Poder submeter**: possuir autorização para encaminhar proposta de oferta à verificação ou aprovação correspondente.
- **Poder publicar/ativar**: possuir autorização específica, após regras aplicáveis, para tornar a oportunidade disponível.
- **Poder realizar a atividade**: cumprir qualificações, legislação, condições materiais, consentimento e responsabilidades próprias.

Uma etapa não autoriza automaticamente a seguinte.

### 2. Compatibilidade com os documentos existentes

| Fonte | O que sustenta | O que não transfere |
| --- | --- | --- |
| [Participante Profissional](../participants/professional.md) | Participante potencialmente ofertador, com identidade de atuação própria | Publicação, monetização e escopo regulado automáticos |
| [PAS-001 — Oportunidades Ativas](../product-architecture/pas-001-oportunidades-ativas-fundamentos-iniciais.md) | O Profissional já consta em atores e exemplos de oportunidade e orientação | Contrato completo de publicação do Profissional |
| [Master ORG-002](../experience-architecture/organizations-collectives-journey/organization-opportunity-registration-master.md) | Fluxo institucional da Organização, com distinção cadastro/publicação | Direitos, autorizações ou titularidade para Profissional |
| [PRO-REC-01](#decisão-da-direção--pro-rec-01-13112026) | Identidade funcional profissional vinculada à Pessoa | Habilitação e elegibilidade para tipos específicos de oferta |

### 3. Categorias de oportunidades — hipótese de elegibilidade

| Categoria ilustrativa | Exemplos | Verificação necessária |
| --- | --- | --- |
| Educação e conhecimento | Aulas, mentorias, oficinas, capacitações | Competência, conteúdo, autoria, condições e transparência |
| Atividades e experiências | Workshops, encontros e atividades conduzidas | Escopo, local/formato, segurança, elegibilidade |
| Projetos e trabalho especializado | Colaborações, projetos e prestação de serviços | Responsabilidade, requisitos e regras comerciais |
| Esportes e bem-estar | Aulas e atividades, quando permitidas | Habilitação, segurança e limites de profissão regulamentada |
| Orientações especializadas | Consultorias e atendimentos | Licenças, deveres legais, privacidade e fronteiras profissionais |
| Oportunidades ao vivo | Aulas ou workshops com transmissão/interação síncrona | Contrato próprio de Oportunidades ao Vivo, modalidade, transmissão, agenda e responsabilidade |

A enumeração **não aprova** a publicação dessas categorias nem substitui exame de elegibilidade setorial. Atuação médica, psicológica, jurídica, financeira, educacional regulamentada ou outras profissões sujeitas a licença exigem limites e validação próprios.

### 4. Modelo de estados candidato (não implantado)

```text
Identidade Profissional habilitada para o contexto
  → Rascunho
  → Cadastro completo para submissão
  → Submetida à verificação aplicável
  → Aprovada / Correção solicitada / Rejeitada
  → Publicada / Ativa
  → Pausada / Encerrada / Cancelada
```

Esse mapa serve exclusivamente para estudo. Estados, gatilhos, responsáveis, reversões, automações e notificações **ainda precisam de reconciliação com o ciclo canônico de Oportunidades Ativas**, sem introduzir fluxo paralelo de autoridade.

### 5. Informações mínimas candidatas para estudo

Identidade de oferta do Profissional; especialidade e capacidade declaradas; título e descrição da oportunidade; público e condições de participação; local/online, data e duração; número de participantes ou disponibilidade quando aplicável; valores, pontos ou condições financeiras se autorizados; requisitos de habilitação; política de cancelamento; evidências de segurança/regras; estado de revisão; titularidade; auditabilidade.

**Não exigir ou coletar dados de forma irrestrita**. Os campos reais e suas obrigatoriedades dependem de finalidade, tipo e permissões, e não são instituídos aqui.

### 6. Decisões pendentes para PRO-REC-02

1. **PRO-02A — Direito-base:** Profissional habilitado poderá criar rascunhos de oportunidade por regra geral ou somente após autorização individual/categorial?
2. **PRO-02B — Publicação:** quem aprova e sob quais gates uma oferta se torna ativa?
3. **PRO-02C — Catálogo:** quais classes são permitidas, condicionadas ou vedadas para esse ator?
4. **PRO-02D — Credenciais:** quais especialidades exigem comprovação e revisão periódica?
5. **PRO-02E — Fluxo:** reutilizar infraestrutura comum sem copiar a autoridade institucional ORG-002; quais eventos e estados governam?
6. **PRO-02F — Econômico e interação:** que ofertas admitem pontos, preço, pagamentos, inscrições, publicidade ou relações, sob contratos futuros?

### 7. Recomendação para apreciação

**Recomenda-se reconhecer conceitualmente o Profissional como ofertador elegível em princípio, mas condicionar o direito de cadastrar, submeter e publicar oportunidades a um contrato próprio por categorias, habilitações e responsabilidades.** A existência de uma identidade Profissional não concede licença universal de atuação nem publicação automática.

**Estado do gate:** `PRO-REC-02 EXAMINADO / PROPOSTA NÃO NORMATIVA / DECISÕES PRO-02A…F PENDENTES`. A PR permanece rascunho; sem merge, implementação, habilitação operacional ou alteração em `PAS-001`.


## Deliberação da Direção — PRO-REC-02 (13/11/2026)

A Direção manifestou **“de acordo, segue”** à recomendação expressa de reconhecer o Profissional **como ofertador elegível em princípio**, condicionando cadastro, submissão e publicação de oportunidades a contratos próprios por categoria, habilitação e responsabilidade.

**Diretriz conceitual aprovada:** o Profissional integra as categorias capazes de oferecer oportunidades. A identidade profissional, por si, **não confere direito universal de publicação**, validação automática de credenciais, autorização para exercer atividades regulamentadas ou licença para utilizar dados privados de participantes.

**Limite da aprovação:** as decisões operacionais **PRO-02A a PRO-02F continuam abertas**, inclusive os gatilhos exatos de cadastro, aprovação, categorias admitidas, habilitações, estados e condições econômicas. Esta deliberação não altera o `PAS-001`, não aprova os estados candidatos da seção anterior e não autoriza implantação, testes ou publicação de oportunidades.

## Exame focal — PRO-REC-03: autoridade e responsabilidade da oferta

**Natureza:** proposta analítica subsequente à aprovação conceitual de PRO-REC-01 e PRO-REC-02, sem nova autorização operacional.

### 1. Pergunta central

Quem responde pela oportunidade disponibilizada sob a identidade Profissional, como sua autoridade é demonstrada e quais responsabilidades permanecem com o ofertador, a plataforma e os demais participantes?

### 2. Matriz de fronteiras para apreciação

| Tema | Responsabilidade candidata do Profissional | Limite para a Guivos e terceiros |
| --- | --- | --- |
| Identidade e autoria | Ser identificável como ofertador e declarar a própria atuação, sem representar indevidamente outra entidade | A plataforma deve distinguir identidade pessoal, perfil profissional e representação institucional |
| Escopo profissional | Descrever competências, condições da atividade, limites de formação e eventual habilitação exigida | A presença de perfil não comprova credencial nem habilitação legal |
| Conteúdo da oferta | Garantir clareza, precisão e atualização das condições materiais informadas | A plataforma pode exigir validações e permitir correções, sem assumir automaticamente a execução |
| Elegibilidade | Apresentar requisitos legítimos, sem discriminação indevida | Autoridades de política, moderação e segurança podem impor condições setoriais |
| Disponibilidade e execução | Responder pela capacidade de cumprir a oportunidade que oferecer | Cadastro ou aprovação não equivale a comprovação de resultado |
| Valores e condições | Informar condições de participação e contrapartidas, quando permitidas | Planos, taxas, pontos, pagamentos e reembolsos dependem de contratos econômicos |
| Comunicação | Responder por informações dadas aos participantes por canais governados | Contato e dados pessoais não são liberados indiscriminadamente |
| Segurança e incidentes | Atender deveres próprios da atividade e reportar incidentes relevantes | A plataforma conserva os controles e deveres que sejam seus, não transferíveis por contrato |
| Alteração, retirada e cancelamento | Corrigir ou encerrar uma oportunidade conforme regras aplicáveis | Alterações materiais devem preservar rastreabilidade, participantes afetados e estados governados |
| Evidências e avaliação | Permitir contestação, revisão e tratamento adequado de avaliações | Avaliações, reputação e indicadores exigem contratos próprios e não são presumidos como existentes |

### 3. Titularidade e representação

**Recomendação candidata:** a titularidade de uma oferta individual deve apontar para a **identidade Profissional responsável**, vinculada à Pessoa autenticada e autorizada. Se o mesmo indivíduo agir em nome de uma Organização ou de um Coletivo, a titularidade institucional ou coletiva deverá seguir o contexto de representação correspondente, com autoridade e responsabilidade próprias.

Assim, **a mesma Pessoa humana não torna intercambiáveis** os contratos de publicação em nome próprio, de uma Organização ou de um Coletivo.

O vínculo entre identidade pessoal e profissional deve ser suficiente para autorizar e auditar a operação, sem misturar automaticamente perfil, intenções, histórico privado, mensagens ou dados sensíveis.

### 4. Cenários de responsabilidade

1. **Aula oferecida em nome próprio:** o Profissional é o ofertador declarado; comprovação de especialidade e condições depende da categoria, não do simples cadastro.
2. **Curso oferecido por escola com professor responsável:** a Organização pode ser a titular da oferta, enquanto o Profissional atua como executor, representante ou responsável técnico conforme contrato; não há mudança automática de titularidade.
3. **Atividade organizada por um Coletivo com instrutor convidado:** a responsabilidade pela oportunidade e a participação técnica do Profissional precisam ser explicitamente diferenciadas.
4. **Atividade regulamentada:** oferecer e executar exigem validações apropriadas. Uma oportunidade não se torna lícita apenas por ter sido publicada.
5. **Evento ao Vivo:** titularidade, transmissão, interação síncrona, calendário e condições de acesso devem ser reconciliados com o contrato específico, sem inventar novo fluxo.

### 5. Decisões pendentes — PRO-REC-03

- **PRO-03A:** sujeito titular da oportunidade quando há atuação individual versus representação de Organização/Coletivo.
- **PRO-03B:** evidências e verificações proporcionais de identidade, credenciais e habilitação.
- **PRO-03C:** deveres de informação, atualização, entrega, segurança e condições de cancelamento.
- **PRO-03D:** alçadas de moderação, suspensão, auditoria, contestação e recurso.
- **PRO-03E:** efeitos de múltiplos contextos de atuação sobre identidade, permissões, dados e reputação.
- **PRO-03F:** tratamento de responsabilidade por resultados, avaliações, disputas e incidentes sem presumir isenção total da plataforma.

### 6. Recomendação para próxima deliberação

**Recomenda-se que toda oportunidade tenha um titular de oferta inequívoco e um contexto de atuação autorizado.** Quando o titular for Profissional, a responsabilidade declarada deverá corresponder à identidade funcional profissional vinculada à Pessoa; quando o ofertador for Organização ou Coletivo, deverá prevalecer sua autoridade própria, ainda que a execução envolva um Profissional.

Essa recomendação **não adjudica automaticamente** as questões PRO-03A a PRO-03F, não cria dever legal novo por inferência nem determina modelo técnico de identidade.

**Estado:** `PRO-REC-03 EXAMINADO / RECOMENDAÇÃO CANDIDATA / DECISÃO PENDENTE`. Nenhum merge, publicação operacional ou implementação autorizado por este exame.
