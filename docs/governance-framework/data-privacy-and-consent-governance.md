---
id: GKR-DATA-PRIVACY-CONSENT-001
title: Governança de Dados Pessoais, Privacidade e Consentimentos
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
  - GKR-OPERATIONAL-LEGAL-TRUTH-001
  - GKR-LEGAL-SURFACE-GATES-001
  - GEA-GRAPH-REFERENCE-001
  - GKR-STATE-001
normative: true
---

# Governança de Dados Pessoais, Privacidade e Consentimentos

## 1. Finalidade

Este documento estabelece a arquitetura de referência para tratamento de dados pessoais no ecossistema Guivos e define como finalidade, papéis, bases jurídicas, consentimentos, direitos, retenção, compartilhamento e evidência devem ser separados.

Ele **não declara que controles de privacidade já estejam implementados em produção** e não substitui análise jurídica aplicada aos tratamentos concretos.

A leitura obrigatória é:

```text
princípio de privacidade
≠ inventário de dados
≠ atividade de tratamento mapeada
≠ base jurídica analisada
≠ controle projetado
≠ controle implementado
≠ superfície publicada
≠ registro operacional comprovado
```

## 2. Referencial normativo brasileiro

Quando a LGPD for aplicável, o desenho deverá observar a Lei nº 13.709/2018 e regulamentação vigente da Autoridade Nacional de Proteção de Dados.

O P6 usa como baseline jurídico, sujeito a revisão antes de operação:

- LGPD — Lei nº 13.709/2018;
- regulamentações vigentes da ANPD;
- Resolução CD/ANPD nº 18/2024 sobre atuação do Encarregado;
- Resolução CD/ANPD nº 15/2024 sobre comunicação de incidentes de segurança;
- guias e orientações oficiais aplicáveis aos temas concretos, incluindo cookies quando houver tratamento correspondente.

Fontes oficiais de consulta:

- `https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm`
- `https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd`

A existência dessas normas não prova que a Guivos já tenha completado sua implementação de conformidade.

## 3. Princípios estruturais

O tratamento deverá ser concebido segundo, no mínimo:

1. finalidade identificável;
2. adequação entre dado e finalidade;
3. necessidade/minimização;
4. transparência proporcional ao contexto;
5. qualidade e possibilidade de correção;
6. segurança e prevenção;
7. não discriminação;
8. responsabilização e prestação de contas;
9. separação entre evidência, inferência e recomendação;
10. controle de acesso proporcional;
11. ciclo de vida e retenção definidos;
12. direitos do titular operacionalizáveis quando aplicáveis.

A coleta de um dado porque ele “pode ser útil no futuro” não é finalidade suficiente.

## 4. Unidade mínima: atividade de tratamento

A governança não deve partir apenas de telas, bancos de dados ou nomes de sistemas. A unidade mínima deverá ser uma **atividade de tratamento com finalidade definida**.

Cada atividade futura deverá registrar, quando aplicável:

| Campo | Conteúdo esperado |
|---|---|
| `processing_id` | identificador estável |
| objeto/finalidade | por que o tratamento existe |
| titular | Pessoa ou pessoa natural relacionada a Coletivo/Organização/contraparte |
| contexto | jornada, produto, operação ou obrigação |
| categorias de dados | tipos efetivamente necessários |
| dados sensíveis | presença, necessidade e proteção adicional |
| origem | declarado, observado, terceiro, derivado ou inferido |
| controlador | entidade que decide finalidade/elementos essenciais, quando aplicável |
| operador | entidade que trata em nome do controlador, quando aplicável |
| base jurídica | hipótese aplicável, com estado de revisão |
| destinatários | compartilhamentos necessários |
| transferência | internacional ou entre entidades, quando houver |
| retenção | critério/prazo e descarte |
| segurança | controles requeridos |
| direitos | canal e tratamento das solicitações |
| derivados | perfis, scores, embeddings, grafos, modelos ou agregações geradas |
| estado operacional | referência, projetado, implementado ou evidenciado |
| evidência | artefato que sustenta o estado declarado |

Nenhum campo deve ser preenchido por suposição apenas para “completar” o registro.

## 5. Titular e participante não são conceitos equivalentes

No modelo Guivos, Pessoa, Coletivo e Organização são papéis de participação do ecossistema.

Na proteção de dados pessoais, **titular é pessoa natural**.

Assim:

- uma Pessoa participante poderá ser titular;
- representantes, colaboradores ou contatos de um Coletivo ou Organização também poderão ser titulares;
- Coletivo ou Organização, enquanto estrutura, não substitui os direitos das pessoas naturais cujos dados sejam tratados;
- uma relação B2B não remove obrigações relativas a dados de representantes, colaboradores ou usuários individuais.

## 6. Controlador, operador e relações entre entidades

A qualificação dos agentes deve ser feita por atividade de tratamento e realidade decisória, não por nome contratual ou proximidade societária.

```text
empresa relacionada
≠ controlador conjunto automático
≠ operador automático
≠ autorização automática de compartilhamento
```

Conforme `GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001`, entidades Guivos relacionadas, um futuro veículo social, fornecedores ou parceiros não compartilham dados automaticamente.

A futura arquitetura deverá identificar quem determina finalidade e elementos essenciais e quem atua em nome de outro agente, conforme a situação concreta.

## 7. Base jurídica não é sinônimo de consentimento

O P6 proíbe o uso de `consentimento` como rótulo universal de privacidade.

A LGPD prevê diferentes hipóteses para tratamento de dados pessoais e regras próprias para dados pessoais sensíveis. A base aplicável deve ser analisada em função da finalidade e do tratamento concreto.

Portanto:

```text
aceite de Termos de Uso
≠ consentimento LGPD para todos os tratamentos

consentimento para uma finalidade
≠ autorização genérica para outras finalidades

ausência de consentimento
≠ ausência automática de base jurídica
```

Quando consentimento for a base adequada, deverá ser livre, informado, inequívoco e relacionado a finalidade determinada, além de possuir mecanismo de prova e revogação compatível com a legislação aplicável.

## 8. Estados governados de base jurídica

| Estado | Significado |
|---|---|
| `unassessed` | atividade ainda sem análise jurídica |
| `candidate` | hipótese candidata identificada, sem revisão suficiente |
| `review_pending` | análise em andamento |
| `reviewed` | hipótese revisada para o desenho documentado |
| `approved_for_implementation` | desenho jurídico e controle aprovados para implementação |
| `operational_evidenced` | tratamento e controles correspondentes possuem evidência operacional |
| `reassessment_required` | mudança de finalidade, contexto, dado, tecnologia ou norma exige revisão |
| `retired` | atividade encerrada conforme governança de retenção |

Uma atividade não deve entrar em produção baseada apenas em `candidate`.

## 9. Consentimentos e preferências

Quando houver consentimento juridicamente pertinente ou preferência voluntária do usuário, os objetos devem permanecer separados.

Possíveis objetos:

- consentimento para tratamento específico;
- preferência de comunicação;
- inscrição em conteúdo/newsletter;
- escolha de cookies não necessários;
- autorização opcional de integração com terceiro;
- autorização específica relacionada a dado, recurso ou finalidade.

Não se deve agrupar finalidades materialmente diferentes em um único “aceito tudo”.

### Registro mínimo candidato de consentimento

Quando aplicável:

- titular/identificador apropriado;
- finalidade;
- texto/versão exibidos;
- data/hora;
- meio;
- contexto;
- ação positiva registrada;
- estado;
- origem da prova;
- revogação e data, quando houver;
- efeito da revogação;
- relação com derivados e retenção.

A existência dessa especificação não prova que tal registro já esteja implementado.

## 10. Termos, contratos e aceite

Aceite contratual deverá ser governado como objeto distinto de consentimento de privacidade.

Um registro de aceite poderá ser necessário para demonstrar adesão a Termos de Uso, condições de programa ou contrato eletrônico. Esse registro poderá coexistir com tratamentos baseados em diferentes hipóteses jurídicas.

A UI não deve induzir o usuário a acreditar que aceitar um contrato significa renunciar genericamente a direitos de proteção de dados.

## 11. Dados pessoais sensíveis e contexto de evolução humana

A Guivos poderá lidar, em sua visão de maturidade, com contextos de evolução que tangenciem saúde, crenças, relações, finanças ou outros aspectos íntimos.

Isso exige proteção reforçada.

O fato de uma dimensão existir na arquitetura de evolução **não autoriza coletar dados sensíveis sobre ela**.

```text
dimensão conceitual
≠ atributo obrigatório
≠ dado pessoal necessário
≠ dado sensível autorizado
```

Antes de qualquer tratamento dessa natureza devem ser definidos finalidade, necessidade, hipótese jurídica aplicável, acesso, retenção, segurança, compartilhamentos e impactos aos titulares.

Dados sensíveis não podem ser usados para construir ranking de valor humano, coerção, exclusão indevida ou exploração comercial incompatível com o propósito.

## 12. Inferências, perfil e inteligência

Guivos Intelligence e o grafo devem preservar:

```text
dado declarado
≠ evento observado
≠ dado derivado
≠ inferência
≠ hipótese
≠ recomendação
```

Uma inferência não deve ser apresentada como fato informado pelo titular.

Quando uma atividade produzir perfis, scores, embeddings, clusters, recomendações ou outros derivados vinculáveis a pessoa natural, deverão ser governados também:

- finalidade;
- proveniência;
- explicabilidade proporcional;
- acesso;
- contestação/correção quando pertinente;
- retenção;
- efeitos da correção ou exclusão da fonte;
- risco de discriminação;
- revisão de decisões automatizadas quando aplicável.

`GEA-GRAPH-REFERENCE-001` permanece autoridade técnica complementar e não prova tratamento real de dados no grafo.

## 13. Compartilhamento e terceiros

Compartilhamento deverá possuir finalidade e relação formal identificáveis.

Antes de compartilhar dados com fornecedor, parceiro, anunciante, Organização, produto terceiro ou entidade relacionada, deverão ser avaliados, conforme o caso:

- necessidade;
- papel do destinatário;
- base jurídica;
- instruções e limites;
- segurança;
- retenção;
- subcontratação;
- direitos do titular;
- transferência internacional;
- encerramento/devolução/exclusão;
- evidência contratual.

`Parceiro estratégico` não é uma permissão de dados.

## 14. Cookies, SDKs e tecnologias de rastreamento

A existência de site, aplicativo ou analytics não autoriza inferir uma solução de cookies ou rastreamento específica.

Quando essas tecnologias forem usadas, deverá existir inventário técnico e jurídico que identifique finalidade, necessidade, fornecedor, duração, categorias de dados, hipótese jurídica e controle do titular quando aplicável.

Banners e centros de preferências são **controles derivados do tratamento real**, não elementos decorativos obrigatórios por template.

Cookies ou tecnologias estritamente necessárias e tecnologias opcionais não devem ser tratadas como se possuíssem finalidade e base idênticas.

## 15. Direitos dos titulares

A arquitetura futura deverá permitir o exercício dos direitos aplicáveis, conforme contexto e legislação vigente.

O fluxo deve possuir pelo menos:

1. canal identificável;
2. autenticação proporcional ao risco;
3. classificação da solicitação;
4. identificação dos tratamentos afetados;
5. análise jurídica/operacional quando necessária;
6. execução nos sistemas e derivados pertinentes;
7. resposta ao titular;
8. registro auditável;
9. tratamento de exceções e retenções legalmente necessárias.

Uma página “fale conosco” não comprova, sozinha, um processo operacional de direitos.

## 16. Encarregado

A arquitetura deve prever o papel de Encarregado quando juridicamente aplicável, conforme LGPD e regulamentação vigente.

Este documento não nomeia pessoa natural ou jurídica, não cria vínculo funcional e não afirma que a indicação formal já tenha ocorrido.

Qualquer estado futuro deverá distinguir:

- papel previsto;
- candidato;
- ato formal de indicação;
- contato público;
- capacidade operacional;
- evidência de atuação.

## 17. Segurança e incidentes

Privacidade e segurança são complementares, mas não equivalentes.

Atividades com dados pessoais deverão possuir controles proporcionais de prevenção, detecção, resposta e recuperação.

A arquitetura operacional futura deverá incluir processo de incidentes capaz de:

- identificar se há dados pessoais envolvidos;
- registrar e preservar evidências;
- avaliar risco ou dano aos titulares;
- mitigar impactos;
- decidir e executar comunicações obrigatórias quando aplicáveis;
- manter registros pelo período exigido;
- corrigir causas e derivados afetados.

A Resolução CD/ANPD nº 15/2024 integra o baseline regulatório brasileiro para comunicação de incidentes, mas este P6 não afirma que o processo Guivos já esteja implementado.

## 18. Retenção e eliminação

`guardar para sempre` não é política de retenção.

Cada atividade deverá estabelecer critério compatível com finalidade, obrigação aplicável, exercício de direitos, segurança e necessidade real.

A arquitetura deverá considerar também cópias, backups, caches, logs, índices, embeddings, datasets derivados, grafo e sistemas de terceiros.

Exclusão da fonte não deve ser descrita como “eliminação completa” quando derivados ou backups ainda permanecerem legitimamente retidos.

## 19. Estado corrente do P6

No checkpoint de criação deste documento:

| Objeto | Estado |
|---|---|
| princípios/arquitetura de privacidade | `reference_proposed` |
| inventário completo de tratamentos | `not_evidenced` |
| RoPA/registro equivalente de atividades | `not_evidenced` |
| bases jurídicas revisadas por atividade | `not_evidenced` |
| consentimentos em produção | `not_evidenced` |
| centro de preferências | `not_evidenced` |
| política/aviso de privacidade publicado e versionado | `not_evidenced` |
| Termos de Uso publicados e versionados | `not_evidenced` |
| fluxo operacional de direitos | `not_evidenced` |
| Encarregado formalmente indicado | `not_evidenced` |
| inventário de cookies/SDKs | `not_evidenced` |
| processo operacional de incidentes LGPD | `not_evidenced` |
| mapa completo de operadores/suboperadores | `not_evidenced` |
| produção com dados pessoais em Neo4j | `not_evidenced` |

O estado `not_evidenced` significa ausência de evidência integrada e governada no GKR; não deve ser convertido em afirmação categórica sobre sistemas externos não auditados.

## 20. Limites

Este documento não:

- aprova coleta específica;
- escolhe base jurídica para tratamento ainda não mapeado;
- autoriza dado sensível;
- publica política;
- publica Termos;
- nomeia Encarregado;
- implementa consentimento;
- instala cookie banner;
- autoriza rastreamento;
- aprova fornecedor;
- cria transferência internacional;
- substitui RIPD/DPIA ou avaliação equivalente quando necessária;
- comprova conformidade operacional.
