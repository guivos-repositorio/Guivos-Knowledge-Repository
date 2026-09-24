---
id: GKR-UX-ORGCOL-AUTH-STATE-MAP-001
title: Organizações e Coletivos — Mapa de Estados da Experiência Autenticada
status: active
version: 1.1.4
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-24
normative: false
maturity: authenticated_state_map_defined
depends_on:
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-014
  - UXA-019
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001
---

# Organizações e Coletivos — Mapa de Estados da Experiência Autenticada

## 1. Finalidade

Este documento define o **mapa funcional de estados** da experiência autenticada de Organização e Coletivo a partir do Surface Map canônico, dos contratos de autoridade, das Jornadas e dos registries já vigentes.

Ele responde à pergunta:

> **Quais condições funcionais relevantes a experiência autenticada precisa conseguir representar e preservar antes que sejam definidos fluxos prioritários, wireframes ou qualquer materialização visual?**

O mapa de estados não determina tela, componente, layout, navegação, rota, copy ou implementação.

```text
MAPA DE SUPERFÍCIES
→ onde uma responsabilidade pertence

MAPA DE ESTADOS
→ em quais condições funcionais essa responsabilidade pode existir

FLUXO
→ como uma mudança entre condições é governada

WIREFRAME / UI
→ como responsabilidades, estados e ações são materializados visualmente
```

Portanto:

```text
ESTADO FUNCIONAL
≠ TELA
≠ COMPONENTE
≠ STATUS VISUAL
≠ TRANSIÇÃO
≠ EVENTO TÉCNICO
≠ REGRA DE RBAC
≠ IMPLEMENTAÇÃO
```

## 2. Autoridade e limite desta frente

Este mapa deriva principalmente de:

1. `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.0.0` — domínios lógicos e crosswalk para superfícies estáveis;
2. `GKR-UX-ORGCOL-AUTH-IA-001` — contexto, síntese, domínios de trabalho, governança/evidência e capacidades especializadas;
3. `GKR-UX-ORGCOL-AUTH-JOBS-001` — atores, autoridade, limites e jobs autenticados;
4. `GKR-UX-ORGCOL-UX-STATE-001` — cobertura funcional de estados absorvida após a supersessão de `UXA-015..018`;
5. `GKR-JOURNEY-SURFACE-REGISTRY-001` — identidade e maturidade individual das superfícies;
6. `GKR-JOURNEY-TRANSITION-REGISTRY-001` — transições já registradas e sua maturidade própria;
7. `UXA-014` e `UXA-019` — fundamento estrutural e contrato bilateral Organização–Coletivo.

Regra central:

> **Este documento organiza estados funcionais; ele não cria um registry paralelo de estados, não cria novos `GKR-TRN-*`, não altera a maturidade das transições existentes e não converte estados em fluxo.**

Os rótulos de estado abaixo são vocabulário funcional desta autoridade, não identificadores estáveis globais.

## 3. Modelo de estado

Um estado funcional descreve uma condição relevante de um contexto, objeto, responsabilidade, informação ou relação que muda o que pode ser compreendido, decidido ou realizado legitimamente.

Os estados são **componíveis**. Uma mesma superfície pode, por exemplo, estar simultaneamente:

- com autoridade válida;
- com capacidade limitada;
- com uma obrigação atrasada;
- com evidência insuficiente;
- e com uma integração indisponível.

Logo, este mapa não impõe uma máquina de estados única e linear.

```text
ESTADO A
+
ESTADO B
+
ESTADO C
→ PODEM COEXISTIR

COEXISTÊNCIA DE ESTADOS
≠ TRANSIÇÃO AUTOMÁTICA
```

Estados de um objeto especializado não são automaticamente estados do domínio inteiro. Uma superfície de síntese pode referenciar um estado pertencente a outro objeto sem se tornar sua nova fonte de verdade.

## 4. Famílias transversais de estado

### 4.1 Contexto e autoridade

Toda ação autenticada depende de contexto e autoridade aplicáveis.

Estados funcionais mínimos:

- **contexto válido** — participante, unidade e escopo identificados suficientemente;
- **contexto incompleto** — faltam dados materiais para interpretar ou agir com segurança;
- **autoridade válida** — papel e autoridade sustentam a ação pretendida;
- **autoridade insuficiente** — a pessoa pode compreender o contexto, mas não executar a ação pretendida;
- **aprovação adicional necessária** — a ação exige outra autoridade legítima antes de produzir efeito;
- **responsável ausente ou não atribuído** — nenhuma pessoa legitimamente responsável está disponível para a responsabilidade necessária;
- **autoridade contestada** — existe disputa material sobre representação, aprovação ou responsabilidade;
- **autoridade encerrada ou expirada** — a relação que sustentava a atuação não está mais vigente.

Mudança de contexto deve reavaliar participante, unidade, papel, autoridade e objeto aplicável; não transporta silenciosamente permissão, dado, decisão pendente ou contexto protegido.

```text
ACESSO AO CONTEXTO
≠ AUTORIDADE

AUTORIDADE PARA UMA AÇÃO
≠ AUTORIDADE IRRESTRITA
```

### 4.2 Operação e atenção material

Estados funcionais mínimos:

- **operação regular** — nenhuma atenção material urgente é conhecida;
- **atenção necessária** — existe responsabilidade, prazo, decisão ou condição que exige ação legítima;
- **atenção urgente** — existe risco, proteção, obrigação ou continuidade com criticidade material;
- **bloqueado** — a responsabilidade não pode avançar sem condição, autoridade, dado ou ação externa necessária;
- **pausado** — continuidade temporariamente interrompida sem equivaler a encerramento;
- **encerrado com responsabilidades remanescentes** — o ciclo principal terminou, mas obrigações, evidências, dados ou deveres ainda precisam ser preservados.

### 4.3 Proveniência, evidência e compreensão

A experiência deve distinguir a natureza epistemológica da informação e a suficiência da evidência. São dimensões relacionadas, mas não idênticas.

Estados de proveniência/compreensão mínimos:

- **confirmada no limite da autoridade aplicável** — informação sustentada pela fonte ou participante legitimamente competente para confirmá-la;
- **externa** — informação proveniente de fonte externa identificável, sem ser convertida automaticamente em verdade própria da Guivos;
- **inferida** — interpretação ou inferência identificada como tal, com limites proporcionais;
- **desconhecida** — informação material ainda não conhecida ou não disponível;
- **contestada** — informação ou interpretação material possui divergência legítima registrada;
- **desatualizada ou materialmente incerta** — existe informação, mas sua atualidade ou confiabilidade não sustenta uso silencioso como estado corrente.

Estados de evidência mínimos:

- **evidência suficiente para a afirmação permitida**;
- **evidência ausente**;
- **evidência insuficiente**;
- **evidência conflitante**;
- **evidência contestada**;
- **fonte indisponível**.

Uma informação confirmada pode ainda não possuir evidência suficiente para uma afirmação de resultado ou impacto. Uma inferência pode ser útil sem ser tratada como fato confirmado.

```text
CONFIRMADO
≠ IMPACTO COMPROVADO

INFERIDO
≠ FATO

DESCONHECIDO
≠ ZERO

SEM EVIDÊNCIA
≠ SEM RESULTADO

DADO AUSENTE
≠ ZERO

CORRELAÇÃO
≠ CAUSALIDADE
```

### 4.4 Proteção, governança e contestação

Estados mínimos:

- **proteção regular** — nenhuma condição material de proteção conhecida exige intervenção;
- **proteção requerida** — moderação, privacidade, acessibilidade, segurança ou integridade exigem atuação proporcional;
- **conteúdo/informação protegida** — informação existe, mas não pode ser exposta integralmente ao ator atual;
- **decisão contestada** — decisão ou fundamento está sob contestação legítima;
- **conflito de governança** — não existe consenso/autoridade suficiente para tratar a decisão como pacificada;
- **revisão necessária** — decisão, relação ou condição precisa ser reavaliada antes da continuidade.

Contestação, denúncia ou pedido de revisão não podem produzir retaliação automática nem desaparecer por simples alteração visual de estado.

### 4.5 Capacidade e disponibilidade

Estados mínimos:

- **capacidade disponível**;
- **capacidade limitada**;
- **capacidade atingida ou esgotada**;
- **recurso necessário indisponível**;
- **dependência externa indisponível**;
- **operação degradada** — parte da capacidade permanece utilizável sem permitir conclusões indevidas;
- **baixa conectividade** — continuidade deve preservar segurança, reversibilidade e não duplicação quando aplicável.

Planos pagos podem alterar capacidade contratada, mas não autoridade, relevância, legitimidade ou força de evidência.

## 5. Organização — estados por domínio

### 5.1 Visão Geral — `GKR-SURF-ORG-001`

A Visão Geral deve conseguir sintetizar, sem se transformar em dashboard total, pelo menos as seguintes condições:

- operação regular sem atenção material urgente;
- contexto institucional incompleto;
- Organização ainda não verificada, quando verificação for aplicável;
- autoridade insuficiente para a ação pretendida;
- unidade/contexto sem responsável legitimamente atribuído;
- compromisso ou obrigação material atrasada;
- risco material ou urgente;
- capacidade limitada, atingida ou esgotada;
- informação material desconhecida, inferida ou contestada;
- evidência insuficiente para reconhecer avanço, resultado ou conclusão;
- fonte ou integração indisponível;
- baixa conectividade;
- operação legítima em múltiplos países, idiomas ou moedas.

Este domínio sintetiza estados pertencentes a outras responsabilidades sem absorver seus objetos nem duplicar suas fontes de verdade.

### 5.2 Oportunidades e Programas — `GKR-SURF-ORG-002..003`

Estados funcionais mínimos:

- nenhuma oportunidade ou programa ativo;
- objeto em preparação dentro do contrato de cadastro aplicável;
- objeto aguardando condição/autoridade necessária para continuidade;
- oportunidade/programa ativo quando sua autoridade especializada assim definir;
- objeto pausado;
- objeto expirado ou encerrado;
- capacidade de publicação limitada ou atingida;
- informação material incompleta, conflitante, contestada ou desatualizada;
- distribuição/descoberta indisponível sem transformar indisponibilidade em conclusão sobre relevância.

O lifecycle detalhado permanece subordinado às autoridades especializadas e às transições já registradas, incluindo `GKR-TRN-201..203` quando aplicáveis.

```text
ATIVO
≠ DISTRIBUÍDO
≠ RELEVANTE
≠ IMPACTANTE
```

### 5.3 Relações — Organização–Coletivo sob `UXA-019`

O escopo estável coberto por `GKR-SURF-ORG-004..006` é exclusivamente Organização–Coletivo. O State Map preserva o lifecycle contratual de `UXA-019` sem transformá-lo em fluxo materializado.

Lifecycle principal:

- **rascunho** — ainda não cria compromisso, divulgação ou acesso a dados;
- **proposta** — finalidade, escopo, recursos, dados, responsabilidades e condições estão apresentados para análise;
- **avaliação bilateral** — cada participante verifica autoridade, capacidade, riscos e coerência;
- **negociação** — alterações materiais permanecem visíveis e dependem de nova confirmação quando aplicável;
- **aguardando informação** — falta informação material necessária à avaliação ou continuidade;
- **aguardando consentimento/aprovação** — falta manifestação legítima de autoridade aplicável;
- **aprovada pelas autoridades** — as duas autoridades legítimas aprovaram o mesmo escopo, sem equivaler ainda a qualquer efeito técnico não governado;
- **ativa** — somente o escopo aprovado pode ser executado;
- **em revisão** — compromissos, evidências, riscos, contexto e vontade de continuidade estão sendo reavaliados;
- **alteração material pendente** — existe proposta de mudança material ainda não reavaliada e aprovada bilateralmente; o escopo já aprovado permanece o único efetivo até nova confirmação legítima;
- **renovada ou ajustada** — continuidade/alteração foi legitimamente aprovada segundo o contrato aplicável;
- **pausada** — atividades definidas estão temporariamente interrompidas sem apagar histórico ou proteção;
- **bloqueada por proteção ou privacidade** — condição material impede ativação ou continuidade no limite afetado;
- **contestada** — divergência legítima exige análise, fundamento e possibilidade de revisão;
- **suspensa preventivamente** — interrupção proporcional e revisável diante de risco material;
- **expirada** — prazo/condição de vigência terminou sem autorizar renovação automática;
- **encerrada** — a relação foi finalizada e o plano de transição aplicável foi executado, sem pressupor responsabilidades remanescentes;
- **encerrada com responsabilidades remanescentes** — a relação terminou, mas permanecem obrigações legítimas de dados, recursos, comunicação, proteção ou auditoria.

Além do lifecycle principal, `UXA-019 §23` exige preservar condições alternativas materiais. Elas são ortogonais ao lifecycle e podem coexistir com ele sem significar transição automática:

- **proposta recusada**;
- **autoridade insuficiente**;
- **aprovação divergente entre as partes**;
- **relação ativa sem atenção material**;
- **compromisso atrasado**;
- **recurso indisponível**;
- **dado ou consentimento ausente**;
- **conflito de interesse**;
- **uso de marca contestado**;
- **relação comercial não declarada**;
- **risco de perda de autonomia**;
- **denúncia em análise**;
- **suspensão urgente**;
- **renovação pendente**;
- **encerramento solicitado por uma das partes**;
- **baixa conectividade**;
- **operação internacional**;
- **informação sensível protegida**.

Essas condições preservam diferenças de autoridade, consentimento, proteção, influência, reversibilidade e responsabilidade que não podem ser colapsadas em rótulos genéricos como “contestado”, “em revisão” ou “suspenso”.

`GKR-SURF-ORG-004..006` permanecem estritamente no escopo Organização–Coletivo. Relações Organização–Organização continuam como lacuna sem ID estável dedicado; esta frente reconhece a existência do domínio prevista pela IA, mas **não aplica `UXA-019` nem inventa um lifecycle específico para Organização–Organização**.

Este mapa não altera `GKR-TRN-206..209`, que preservam maturidade própria no Transition Registry.

### 5.4 Responsabilidades e Evidências — `GKR-SURF-ORG-007`

Estados funcionais mínimos:

- nenhuma responsabilidade material ativa conhecida;
- responsabilidade ativa e dentro do prazo;
- responsabilidade próxima do prazo quando material;
- responsabilidade atrasada;
- responsabilidade bloqueada;
- responsabilidade contestada;
- evidência presente e suficiente apenas para a afirmação permitida;
- evidência ausente;
- evidência insuficiente;
- evidência conflitante;
- evidência contestada;
- resultado registrado sem evidência suficiente para inferir impacto;
- fonte indisponível ou degradada.

### 5.5 Organização e Autoridade — sem ID dedicado

Estados mínimos:

- identidade/contexto institucional suficientemente estabelecidos;
- contexto institucional incompleto;
- verificação aplicável pendente, quando houver autoridade própria para essa condição;
- representação válida;
- representação insuficiente para a ação;
- aprovação adicional necessária;
- responsável ausente;
- autoridade contestada;
- autoridade encerrada ou expirada.

A ausência de ID dedicado não autoriza fundir este domínio com configuração técnica ou RBAC.

## 6. Organização — capacidade comercial especializada

`GKR-SURF-ORG-301..304` e `GKR-SURF-BND-002` preservam suas semânticas especializadas sob `GKR-PLANS-ORGANIZATION-001`, `GEM-004-PLAN-TAXONOMY-AUTHORITY-001` e `GKR-JOURNEY-TRANSITION-REGISTRY-001`. O antigo pacote `UXA-100 + A1..A4` permanece somente como proveniência no Git e não é autoridade corrente.

Esta frente apenas preserva que:

- consultar Planos não inicia contratação;
- revisar contratação não confirma pagamento;
- falha não altera silenciosamente o plano anterior;
- downgrade/cancelamento exige tratamento explícito das capacidades afetadas;
- `BND-002` é fronteira assistida, não um plano específico;
- capacidade comercial não altera relevância, evidência ou autoridade.

Nenhuma maturidade de `GKR-TRN-421..428` é promovida por este mapa.

## 7. Coletivo — estados por domínio

### 7.1 Início — `GKR-SURF-COL-002`

Estados funcionais mínimos:

- Coletivo recém-criado ou ainda sem atividade material;
- operação regular sem atenção material;
- atenção material necessária;
- nenhuma pessoa disponível ou legitimamente responsável por função necessária;
- capacidade/recurso insuficiente;
- conflito de governança que afeta continuidade;
- proteção/moderação/acessibilidade exigindo atenção;
- relação externa contestada ou suspensa;
- informação material desconhecida, inferida ou contestada;
- evidência insuficiente para reconhecer avanço/aprendizado;
- baixa conectividade ou dependência indisponível.

### 7.2 Atividades e Oportunidades — `GKR-SURF-COL-006`

Estados funcionais mínimos:

- nenhuma atividade próxima;
- atividade prevista/ativa quando sustentada por autoridade própria;
- atividade ajustada;
- atividade adiada;
- atividade pausada;
- atividade cancelada;
- responsabilidade operacional sem pessoa legitimamente disponível;
- capacidade/recurso insuficiente;
- condição de proteção que exige reavaliação antes da continuidade.

Este mapa não inventa lifecycle detalhado nem transição para oportunidade do Coletivo onde o registry não possua autoridade dedicada.

### 7.3 Participação — `GKR-SURF-COL-003..005`

Estados mínimos no contexto operacional do Coletivo:

- solicitação de entrada/participação pendente;
- informação adicional necessária;
- vínculo de participação ativo;
- participação pausada;
- participação em processo de saída;
- participação encerrada;
- comunicação oficial disponível ao público autorizado;
- comunicação/informação protegida por autoridade, privacidade ou finalidade.

A condição **pessoa observando antes de participar** permanece cobertura funcional válida absorvida de `GKR-UX-ORGCOL-UX-STATE-001`, mas pertence à perspectiva da Pessoa e às superfícies `GKR-SURF-PER-103..108`; ela não é reclassificada como estado interno de `COL-003..005`.

As superfícies da Pessoa `GKR-SURF-PER-103..108` permanecem separadas e não são absorvidas pelo contexto operacional do Coletivo.

As transições `GKR-TRN-101..113` mantêm maturidade própria e não são promovidas por este documento.

### 7.4 Governança e Proteção — `GKR-SURF-COL-005..007`

Estados funcionais mínimos:

- governança regular;
- decisão legítima pendente;
- aprovação/autoridade adicional necessária;
- decisão contestada;
- conflito de governança;
- moderação necessária;
- proteção urgente;
- necessidade ampliada de acessibilidade;
- informação sensível protegida;
- responsável por proteção/moderação ausente;
- revisão necessária antes da continuidade;
- condição resolvida sem apagar histórico material necessário.

### 7.5 Relações — Organização–Coletivo sob `UXA-019`

Para `GKR-SURF-COL-008`, exclusivamente no escopo Organização–Coletivo, aplica-se o mesmo objeto bilateral e o mesmo lifecycle contratual descrito em `UXA-019` e na seção 5.3 desta autoridade.

Lifecycle principal:

- rascunho;
- proposta;
- avaliação bilateral;
- negociação;
- aguardando informação;
- aguardando consentimento/aprovação;
- aprovada pelas autoridades;
- ativa;
- em revisão;
- alteração material pendente;
- renovada ou ajustada;
- pausada;
- bloqueada por proteção ou privacidade;
- contestada;
- suspensa preventivamente;
- expirada;
- encerrada;
- encerrada com responsabilidades remanescentes.

Na perspectiva do Coletivo, **alteração material pendente** mantém o escopo vigente anterior como único escopo efetivo até reavaliação e nova aprovação bilateral; a edição proposta não produz efeito unilateral.

Condições alternativas obrigatórias do mesmo objeto bilateral, visíveis na perspectiva do Coletivo quando autorizadas e materialmente relevantes:

- proposta recusada;
- autoridade insuficiente;
- aprovação divergente entre as partes;
- relação ativa sem atenção material;
- compromisso atrasado;
- recurso indisponível;
- dado ou consentimento ausente;
- conflito de interesse;
- uso de marca contestado;
- relação comercial não declarada;
- risco de perda de autonomia;
- denúncia em análise;
- suspensão urgente;
- renovação pendente;
- encerramento solicitado por uma das partes;
- baixa conectividade;
- operação internacional;
- informação sensível protegida.

A perspectiva do Coletivo não pode apagar a autoridade, os limites ou a versão materialmente relevante da Organização, e a perspectiva da Organização não pode apagar a autonomia e a governança do Coletivo.

Relações Coletivo–Coletivo permanecem sem ID estável dedicado nesta frente. A IA reconhece o domínio, mas esta autoridade **não amplia `GKR-SURF-COL-008`, não aplica `UXA-019` por analogia e não inventa lifecycle específico para Coletivo–Coletivo**.

### 7.6 Aprendizados e Evidências — sem ID dedicado

Estados mínimos:

- informação confirmada no limite permitido;
- informação externa identificada;
- informação inferida;
- informação desconhecida;
- informação contestada;
- evidência suficiente para a afirmação permitida;
- evidência ausente;
- evidência insuficiente;
- evidência conflitante;
- evidência contestada;
- aprendizado ainda não sustentado;
- resultado observado sem base para inferir impacto;
- fonte indisponível ou desatualizada.

Nenhum score, ranking ou declaração de impacto é criado por inferência.

### 7.7 Coletivo e Autoridade — `GKR-SURF-COL-002` parcialmente; sem ID exclusivo

Estados mínimos:

- propósito/contexto suficientemente estabelecidos;
- contexto incompleto;
- representação válida;
- representação insuficiente;
- instância de governança aplicável disponível;
- responsável necessário ausente;
- autoridade contestada;
- recomposição de autoridade/continuidade necessária;
- encerramento legítimo em curso com responsabilidades remanescentes.

## 8. Coletivo — capacidade comercial especializada

`GKR-SURF-COL-301..304` e `GKR-SURF-BND-002` preservam suas semânticas especializadas e transições próprias.

Esta frente não promove `GKR-TRN-411..418` e não redefine a taxonomia `Livre · Mobiliza · Impacta · Rede`.

Planos podem alterar capacidade contratada, mas não pertencimento, legitimidade, governança, relevância ou impacto.

## 9. Estados de ausência, bloqueio, visibilidade e indisponibilidade

Toda futura materialização deverá distinguir semanticamente pelo menos:

```text
NÃO EXISTE
≠ EXISTE, MAS ESTÁ VAZIO
≠ EXISTE, MAS É DESCONHECIDO
≠ EXISTE, MAS É INFERIDO
≠ EXISTE, MAS É CONTESTADO
≠ EXISTE, MAS NÃO É VISÍVEL AO ATOR ATUAL
≠ EXISTE, MAS ESTÁ BLOQUEADO
≠ EXISTE, MAS A FONTE ESTÁ INDISPONÍVEL
≠ EXISTE, MAS A INFORMAÇÃO É INCERTA/DESATUALIZADA
```

Este documento não define skeleton, spinner, toast, banner, modal, card ou qualquer padrão visual para esses estados.

## 10. Reversibilidade e não inferência

Estados reversíveis não devem produzir efeitos irreversíveis por simples visualização, navegação ou retorno.

Preservações:

- abrir um contexto não concede autoridade;
- trocar de contexto não transporta silenciosamente autoridade ou dado protegido;
- abrir uma relação não a aceita;
- visualizar uma solicitação não a aprova;
- revisar uma oportunidade não a publica;
- visualizar evidência não confirma impacto;
- abrir Planos não inicia contratação;
- retornar de Planos não altera capacidade;
- ausência de dado não confirma inexistência funcional;
- indisponibilidade técnica não equivale a falha do participante;
- contestação não pode ser apagada por mudança visual de estado;
- encerramento não apaga evidências ou responsabilidades cuja retenção seja legitimamente necessária.

## 11. Relação com o Transition Registry

O `GKR-JOURNEY-TRANSITION-REGISTRY-001` continua sendo a autoridade para transições identificadas.

Este mapa:

- **não cria** `GKR-TRN-*`;
- **não altera** origem/destino de transição existente;
- **não promove** estado de validação de transição;
- pode apontar uma condição como necessária sem declarar o caminho para alcançá-la;
- preserva contratos especializados já existentes;
- no ato original deixou novos fluxos para ato governado posterior; essa etapa foi posteriormente definida por `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0`.

```text
ESTADO CONHECIDO
≠ TRANSIÇÃO DEFINIDA

TRANSIÇÃO EXISTENTE
≠ FLUXO PRIORITÁRIO COMPLETO
```

A sequência textual de lifecycle registrada em `UXA-019` e os estados alternativos obrigatórios de sua seção 23 são contratos funcionais do objeto bilateral; sua reprodução como cobertura de estados nesta autoridade **não promove `GKR-TRN-206..209`, não declara cada mudança de condição como transição materializada e não amplia `UXA-019` para relações que ele não governa**.

## 12. Relação com Intelligence, Dashboards, KPIs e Analytics

`GKR-INTELLIGENCE-DASHBOARD-KPI-001` permanece autoridade separada.

O State Map não define:

- KPI;
- fórmula;
- threshold;
- score;
- badge;
- gráfico;
- dashboard;
- recomendação;
- causalidade;
- nível de confiança materializado;
- comportamento analítico de implementação.

Um estado funcional pode exigir compreensão ou evidência sem se converter em métrica visual.

## 13. Critérios de suficiência consumidos na promoção documental

A promoção documental desta autoridade foi adjudicada após o cumprimento cumulativo dos seguintes critérios:

1. cobrir as famílias transversais necessárias de contexto/autoridade, operação, proveniência/evidência, proteção/governança e capacidade/disponibilidade;
2. mapear as condições materiais de todos os domínios autenticados definidos no Surface Map sem inventar IDs;
3. preservar a perspectiva da Pessoa separada das superfícies operacionais de Organização/Coletivo;
4. preservar os lifecycles e estados alternativos especializados já governados sem substituir suas autoridades;
5. manter explícitas as lacunas Organização–Organização e Coletivo–Coletivo sem transportar `UXA-019` por analogia;
6. preservar estados de ausência, bloqueio, contestação, proteção, influência e indisponibilidade;
7. não criar nem promover transições;
8. manter Priority Flows, wireframes, Design/UI e Engenharia fechados;
9. passar validação semântica, mecânica e revisão independente no HEAD de promoção exato.

O atendimento desses critérios promove este documento somente ao estado **DEFINED / CANONICAL DOCUMENTARY**; não promove fluxos, superfícies individuais, transições ou materialização visual.

## 14. Estado documental desta autoridade

Após revisão independente, validações semântica e mecânica e autorização humana específica, a sequência governada é:

```text
FUNDAMENTOS E PAPÉIS
→ DEFINED

ATORES / AUTORIDADE / JOBS
→ DEFINED

ARQUITETURA DA INFORMAÇÃO
→ DEFINED

MAPA LÓGICO DE SUPERFÍCIES
→ DEFINED / CANONICAL DOCUMENTARY

MAPA DE ESTADOS
→ DEFINED / CANONICAL DOCUMENTARY

FLUXOS PRIORITÁRIOS
→ GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.2
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

NAVIGATION MATERIALIZATION
→ ACTIVE / CANONICAL

AUTHENTICATED WIREFRAMES
→ DELIVERY v0.1.0 / VALIDATION v1.0.0 PASS

HIGH-FIDELITY DESIGN
→ AUTHORIZATION GRANTED
→ EXECUTION RELEASE ISSUED
→ EXTERNAL DELIVERY NOT_RECEIVED

PROTOTYPE
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ NOT_RELEASED
```

A promoção desta autoridade não altera por inferência a maturidade individual dos `GKR-SURF-*` nem dos `GKR-TRN-*`.

## 15. Próximo gate após promoção

A promoção deste State Map **não autorizou automaticamente fluxos prioritários**. Eles foram definidos somente depois, por ato governado separado em `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0`.

O ato governado posterior de Priority Flows reconciliou:

- estados definidos;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
- reversibilidade;
- autoridade bilateral;
- ausência/bloqueio/contestação/indisponibilidade;
- fluxos especializados já existentes;
- fronteiras `BND-*`;
- proteção e não retaliação;
- retorno e interrupção.

No momento dessa definição, o próximo gate era **Navigation Materialization**, ainda não autorizado. Esse estado é preservado como proveniência do ato original. Posteriormente, Navigation Materialization foi promovida, o low-fidelity foi autorizado/entregue/validado com `PASS`, high-fidelity recebeu autorização humana e o ato separado `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0` liberou a execução externa.

Estado downstream corrente:

```text
NAVIGATION MATERIALIZATION
→ ACTIVE / CANONICAL

AUTHENTICATED WIREFRAMES
→ DELIVERY v0.1.0 / VALIDATION v1.0.0 PASS

HIGH-FIDELITY DESIGN
→ AUTHORIZATION GRANTED
→ EXECUTION RELEASE ISSUED
→ EXTERNAL DELIVERY NOT_RECEIVED

PROTOTYPE
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ NOT_RELEASED
```

Estado preservado no ato de promoção original:

```text
PRIORITY FLOWS
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

NAVIGATION MATERIALIZATION
→ NOT MATERIALIZED

WIREFRAMES
→ NOT STARTED

DESIGN / UI
→ NOT AUTHORIZED

IMPLEMENTATION
→ NOT AUTHORIZED
```
