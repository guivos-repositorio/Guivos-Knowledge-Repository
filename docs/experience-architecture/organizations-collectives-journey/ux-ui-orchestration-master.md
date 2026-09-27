---
id: GKR-UX-ORGCOL-JOURNEY-ORCHESTRATION-001
title: Jornada de Organizações e Coletivos — Documento Mestre de Orquestração UX/UI
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: true
maturity: ux_orchestration_authority_candidate
depends_on:
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-PARTICIPANT-RELATIONSHIPS-INTERACTIONS-001
  - GKR-UX-COMMUNICATIONS-NOTIFICATIONS-001
  - GKR-UX-ORGCOL-DOCUMENTARY-COMPLETENESS-001
---

# Jornada de Organizações e Coletivos — Documento Mestre de Orquestração UX/UI

## 1. Finalidade

Este documento governa a **orquestração ponta a ponta da Jornada de Organizações e Coletivos** para orientar Design, IA de apoio, Produto, UX, prototipação e futura implementação.

Os Documentos Mestres por superfície governam responsabilidades locais. Esta autoridade candidata governa **como essas responsabilidades funcionam em conjunto**, preservando participante ativo, contexto, representação, autoridade, estados, transições, bilateralidade, proteção, evidências, planos e continuidade.

Ela não cria nova superfície ou transição e não substitui Surface Registry, Transition Registry, State Map, Priority Flows, Masters ou autoridades comerciais específicas.

```text
MASTER DE SUPERFÍCIE
→ RESPONSABILIDADE LOCAL

ORQUESTRAÇÃO
→ CONTEXTO + AUTORIDADE + ESTADO + CONTINUIDADE
→ HANDOFFS + RETORNOS + BILATERALIDADE
→ COMPORTAMENTO TRANSVERSAL

PROTÓTIPO UX/UI
→ MATERIALIZA AS REGRAS
→ NÃO CRIA VERDADE DE PRODUTO
```

## 2. Princípio de experiência

Organização e Coletivo devem ser percebidos como experiências coerentes e contínuas, não como coleções de telas independentes.

Em qualquer momento material, a experiência deve tornar compreensível:

1. quem está atuando;
2. em nome de qual participante;
3. qual contexto ou unidade está ativo;
4. qual papel e autoridade se aplicam;
5. qual objeto ou responsabilidade está em foco;
6. qual estado é real;
7. o que pode ser feito agora;
8. o que depende de outra pessoa, contraparte ou aprovação;
9. o que mudou após uma ação;
10. como retornar, interromper, revisar, contestar ou continuar.

```text
VISÍVEL
≠ AUTORIZADO

PERTENCER
≠ REPRESENTAR
≠ APROVAR
≠ ADMINISTRAR

NAVEGAR
≠ CONFIRMAR

CONTEXTO SEMELHANTE
≠ AUTORIDADE TRANSPORTÁVEL
```

## 3. Modelo de orquestração

A espinha transversal é:

```text
PESSOA AUTENTICADA
→ PARTICIPANTE REPRESENTADO
→ CONTEXTO / UNIDADE
→ PAPEL
→ AUTORIDADE
→ MOMENTO
→ OBJETO / RESPONSABILIDADE
→ PRÓXIMO PASSO LEGÍTIMO
→ AÇÃO OU DECISÃO
→ PROCESSAMENTO / HANDOFF QUANDO NECESSÁRIO
→ ESTADO CONFIRMADO
→ CONTINUIDADE COERENTE
```

A Pessoa permanece agente humano. Organização e Coletivo permanecem contextos de atuação com governança própria.

## 4. Contexto ativo e troca de contexto

Toda ação material deve ocorrer em contexto identificável.

A troca entre Organização, Coletivo, unidade ou papel deve revalidar autoridade e dados aplicáveis. Não transportar silenciosamente:

- permissões;
- seleção pendente;
- informação protegida;
- decisão em processamento;
- objeto pertencente a outro contexto;
- representação;
- aprovação;
- filtros que alterem significado material.

A troca de contexto não precisa impor uma solução visual específica. Design pode escolher seletor, navegação, menu ou outro padrão compatível.

## 5. Organização — continuidade principal

A experiência da Organização deve preservar a continuidade entre:

```text
ORG-001 — VISÃO GERAL
→ OPORTUNIDADES / PROGRAMAS
→ MANIFESTAÇÕES E INSCRIÇÕES
→ RELAÇÕES ORGANIZAÇÃO–COLETIVO
→ RESPONSABILIDADES E EVIDÊNCIAS
→ PLANOS / CAPACIDADES CONTEXTUAIS QUANDO APLICÁVEL
```

A Visão Geral sintetiza Momento, atenção e Próximos Passos. Ela não absorve as fontes de verdade dos demais objetos.

A Organização não deve ser confundida com Guivos Business. Seus planos `Conecta · Eleva · Transforma` permanecem distintos de `Start · Growth · Scale · Enterprise`.

## 6. Coletivo — continuidade principal

A experiência do Coletivo deve preservar a continuidade entre:

```text
COL-002 — VISÃO GERAL / INÍCIO
→ SOLICITAÇÕES
→ PARTICIPANTES E VÍNCULOS
→ COMUNICAÇÃO OFICIAL
→ ATIVIDADES / CONSULTAS / DECISÕES
→ PROTEÇÃO / MODERAÇÃO
→ RELAÇÃO ORGANIZAÇÃO–COLETIVO
→ PLANOS / CAPACIDADES CONTEXTUAIS QUANDO APLICÁVEL
```

O Coletivo não deve ser antropomorfizado. Ações pertencem a pessoas com papel e autoridade adequados.

Planos `Livre · Mobiliza · Impacta · Rede` governam capacidades comerciais aplicáveis; não redefinem legitimidade, governança ou autoridade humana.

## 7. Bilateralidade Organização ↔ Coletivo

A relação O↔C deve ser orquestrada como **um mesmo objeto bilateral com perspectivas distintas**.

```text
ORGANIZAÇÃO
→ ORG-004 / ORG-005 / ORG-006

COLETIVO
→ COL-008

OBJETO RELACIONAL
→ MESMO ESCOPO GOVERNADO
→ PERSPECTIVAS E AUTORIDADES DISTINTAS
```

A experiência deve preservar:

- quem propôs;
- quem precisa responder;
- estado corrente;
- escopo;
- compromissos;
- consentimentos;
- uso de marca quando aplicável;
- contestação;
- encerramento;
- responsabilidades remanescentes.

Uma contraparte não se torna recurso interno da outra.

## 8. Oportunidades e manifestações

Na continuidade de oportunidades, distinguir publicação, descoberta, manifestação/inscrição e gestão institucional.

```text
ORG-002
→ CADASTRO

ORG-003
→ OPORTUNIDADE APROVADA / ATIVA

PESSOA
→ DESCOBERTA / DETALHE / DECISÃO

PER-204
↔ ORG-008
→ CONTINUIDADE BILATERAL INTERNA CONTRATADA
```

`TRN-213..216` preservam a continuidade contratada aplicável. Retornos contextuais não recebem novos IDs por simetria.

Publicação não garante distribuição, candidatura, relevância ou resultado.

## 9. Solicitações, participantes e vínculos do Coletivo

A orquestração deve distinguir:

```text
SOLICITAÇÃO
≠ APROVAÇÃO
≠ VÍNCULO FORMADO
≠ PARTICIPAÇÃO ATIVA
≠ AUTORIDADE DE GOVERNANÇA
```

A aprovação legítima pode formar vínculo conforme autoridade vigente; a continuidade operacional posterior não deve repetir aprovação nem inferir persistência técnica.

Participantes pertinentes podem ser exibidos nas superfícies adequadas, respeitando finalidade, minimização, autoridade e proteção.

## 10. Comunicação, atividades e decisões

Comunicação oficial, atividade, consulta e decisão são responsabilidades relacionadas, mas não equivalentes.

```text
COMUNICAR
≠ DECIDIR

PARTICIPAR
≠ APROVAR

ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO
```

A UI deve tornar compreensível quando uma manifestação é informativa, participativa, consultiva ou decisória e qual autoridade produz efeito.

## 11. Responsabilidades, evidências e prestação de contas

`ORG-007` apoia localização e compreensão de responsabilidades, compromissos, resultados autorizados e evidências sem se tornar fonte de verdade de todos os objetos referenciados.

Preservar:

```text
CORRELAÇÃO
≠ CAUSALIDADE

CONFIRMADO
≠ IMPACTO PROVADO

SEM EVIDÊNCIA
≠ SEM RESULTADO

DESCONHECIDO
≠ ZERO
```

Proveniência, escopo, suficiência, contestação e limites de conclusão devem permanecer acessíveis quando materiais.

## 12. Autoridade como responsabilidade transversal

Organização & Autoridade e Coletivo & Autoridade não constituem superfícies exclusivas.

A autoridade deve atravessar a experiência de modo proporcional à ação.

A UI pode tornar papel e capacidade de atuação compreensíveis, mas não deve converter visibilidade em permissão nem substituir governança por RBAC presumido.

## 13. Estados transversais

A orquestração deve acomodar, quando aplicáveis:

- autoridade válida;
- autoridade insuficiente;
- aprovação adicional necessária;
- responsável ausente;
- informação incompleta;
- proteção;
- contestação;
- indisponibilidade;
- pausa;
- expiração;
- encerramento;
- responsabilidades remanescentes;
- contexto alterado;
- dado desatualizado.

Estado alternativo não é erro de Design e não deve ser ocultado para preservar happy path.

## 14. Ação, processamento e feedback

Toda ação material deve distinguir, quando aplicável:

```text
AÇÃO DISPONÍVEL
→ AÇÃO CONSCIENTE
→ PROCESSANDO
→ SUCESSO CONFIRMADO
   ou
→ FALHA RECUPERÁVEL
   ou
→ ESTADO INDETERMINADO
```

A interface não deve antecipar sucesso. Repetição após incerteza deve evitar efeito duplicado quando houver risco material.

## 15. Retorno, interrupção e retomada

```text
VOLTAR
≠ DESFAZER

SAIR DA SUPERFÍCIE
≠ CANCELAR PROCESSO

REENTRAR
≠ REEXECUTAR AÇÃO

RETRY
≠ DUPLICAR EFEITO
```

Retornos devem reconsultar estado corrente quando a informação puder ter sido alterada por outra pessoa ou contraparte.

## 16. Planos e capacidades

Planos devem aparecer de forma contextual, sem dominar responsabilidades operacionais.

```text
PLANO
→ CAPACIDADE COMERCIAL APLICÁVEL

PLANO
≠ AUTORIDADE HUMANA
≠ LEGITIMIDADE
≠ RELEVÂNCIA
≠ IMPACTO
≠ EVIDÊNCIA
```

A experiência pode explicar capacidade indisponível ou alternativa de plano quando existir autoridade comercial correspondente. Não inventar entitlement técnico, limite, métrica ou benefício.

## 17. Proteção, privacidade e minimização

A orquestração deve preservar:

- necessidade e finalidade;
- minimização;
- separação entre contexto pessoal e institucional;
- proteção de participantes;
- contestação e correção quando aplicáveis;
- revalidação de autoridade;
- não exposição de informação protegida por mera encontrabilidade.

```text
ENCONTRÁVEL
≠ REVELÁVEL

AGREGADO
≠ LIVRE DE GOVERNANÇA

HISTÓRICO
≠ RETENÇÃO ILIMITADA
```

## 18. Organização↔Organização e Coletivo↔Coletivo

As duas necessidades conceituais são reconhecidas, mas a evidência corrente não justifica superfície, lifecycle ou transições próprias.

A orquestração não pode preencher essas lacunas por analogia.

```text
O↔O
→ NECESSIDADE CONCEITUAL RECONHECIDA
→ SEM ID DEDICADO JUSTIFICADO

C↔C
→ NECESSIDADE CONCEITUAL RECONHECIDA
→ SEM ID DEDICADO JUSTIFICADO
```

## 19. Aprendizados e evidências do Coletivo

Aprendizados e evidências permanecem responsabilidade transversal.

A experiência pode apoiar compreensão de resultados autorizados e evidências pertinentes sem criar `COL-*` exclusivo ou inferir aprendizado apenas pela ocorrência de atividade.

## 20. Prioridade de atenção

Quando múltiplos elementos disputarem atenção, priorizar:

1. segurança, proteção, direito ou obrigação material;
2. processo iniciado que exija ação;
3. prazo real;
4. contestação ou autoridade insuficiente;
5. continuidade da tarefa atual;
6. responsabilidade pendente;
7. contexto informativo;
8. capacidade comercial contextual.

Plano ou promoção não ultrapassa responsabilidade material apenas por valor comercial.


## 21. Matriz de comportamento por superfície e plano

A orquestração deve traduzir a baseline comercial em comportamento compreensível sem confundir **benefício comercial declarado** com **entitlement tecnicamente implementado**.

### 21.1 Organização

| Contexto / superfície | Conecta | Eleva | Transforma | Comportamento de orquestração |
|---|---|---|---|---|
| ORG-001 — Visão Geral | dashboard básico e indicadores essenciais | analytics avançados e agregados | dashboards personalizados conforme contrato | mostrar apenas profundidade sustentada pelo plano; capacidade superior pode ser explicada sem fabricar dado |
| ORG-002/003 — Oportunidades | até 10 novas/mês; 15 ativas | até 50 novas/mês; 75 ativas | capacidade contratada | antes de ação que consome cota, tornar limite vigente compreensível; correção legítima não deve ser confundida com nova publicação |
| administração | até 3 admins; 1 unidade | até 10 admins; até 5 unidades | conforme contrato / múltiplas unidades | ação de adicionar/expandir deve refletir capacidade vigente e autoridade humana |
| relação com Coletivos | até 2 administráveis | até 10 administráveis | conforme contrato | não ocultar relação já existente por mudança de plano; diferenciar criar/administrar nova capacidade de consultar histórico legítimo |
| exportação | básica | completa | automatizável | opção pode estar ausente, limitada ou explicada conforme capacidade governada |
| integrações | não incluídas | limitadas | API/SSO/dedicadas | não mostrar integração como funcional se implementação não estiver contratada |
| suporte | padrão | prioritário | dedicado/SLA | diferença comercial pode ser explicada em Planos/ajuda contextual sem alterar prioridade funcional da Journey |

### 21.2 Coletivo

| Contexto / superfície | Livre | Mobiliza | Impacta | Rede | Comportamento de orquestração |
|---|---|---|---|---|---|
| atividades | 1 gratuita/mês | 4/mês | 15/mês | contratada | ação de nova atividade deve refletir cota real; edição legítima não deve consumir unidade por inferência |
| oportunidades | 1 gratuita/mês | 4/mês | 15/mês | contratada | explicar limite antes de nova criação quando material |
| publicações ativas | 2 | 6 | 20 | contratada | atingir capacidade não apaga nem deslegitima publicações vigentes |
| cobrança/publicação paga | não | sim | sim | sim | Livre não deve exibir cobrança como capacidade operacional disponível; pode explicar upgrade quando a pessoa responsável tenta publicar com cobrança |
| administração | até 2 admins | até 5 | até 15 | contrato | autoridade humana continua separada de capacidade quantitativa |
| núcleos/unidades | 1 | 1 | até 5 | múltiplos | criação/gestão adicional deve respeitar capacidade vigente |
| participantes | gestão essencial | gestão ampliada | capacidades ampliadas conforme autoridades | conforme contrato | dados exibidos continuam sujeitos a finalidade, papel, minimização e proteção |
| indicadores | básicos / 30 dias | ampliados | históricos e de impacto | personalizados | plano não autoriza inferir impacto; evidência continua necessária |
| exportação | não declarada como capacidade própria | básica | completa | massa/personalizada conforme contrato | somente materializar opção executável quando houver autoridade técnica suficiente |
| integrações | não | limitadas | avançadas | dedicadas/API/SSO | não inventar integração, fornecedor ou comportamento técnico |
| suporte | padrão | prioritário | especializado | dedicado/SLA | não interfere na legitimidade de ações de governança |

## 22. Ação visível, contextual, indisponível e não materializável

Cada ação governada deve poder ser classificada, no contexto corrente, como:

```text
VISÍVEL E DISPONÍVEL
→ plano + autoridade + estado permitem ação

VISÍVEL E CONDICIONAL
→ ação existe, mas depende de condição explicável

VISÍVEL E INDISPONÍVEL
→ capacidade conhecida, porém não disponível no plano/estado atual
→ motivo + alternativa legítima + upgrade opcional quando aplicável

OCULTA POR IRRELEVÂNCIA
→ ação não pertence ao contexto atual
→ ocultação não pode esconder direito, obrigação ou estado material

NÃO MATERIALIZÁVEL
→ benefício/capacidade comercial existe, mas comportamento técnico ainda não está contratado
→ não simular como implementado
```

A decisão de ocultar não pode ser usada para esconder informação necessária à compreensão de estado, consequência, segurança, cobrança, direito ou responsabilidade.

## 23. Upgrade contextual e avanço por necessidade

Upgrade deve surgir de **necessidade observável**, nunca de pressão genérica.

Exemplos legítimos:

- Organização tenta criar nova oportunidade após atingir cota;
- Organização precisa ampliar administradores, unidades ou Coletivos relacionados;
- Organização solicita analytics/exportação/integração pertencente a plano superior;
- Coletivo tenta publicar oferta paga estando no Livre;
- Coletivo atinge cota de atividade, oportunidade ou publicação ativa;
- Coletivo precisa de mais administradores, núcleos, analytics, exportação ou integração;
- necessidade real exige dimensionamento assistido.

A orientação deve explicar:

```text
CONTEXTO ATUAL
→ plano vigente

AÇÃO PRETENDIDA
→ o que a pessoa responsável tentou fazer

LIMITAÇÃO REAL
→ capacidade/cota aplicável

ALTERNATIVA NO PLANO ATUAL
→ quando existir

PLANO / CAMINHO QUE AMPLIA
→ diferença comercial objetiva

DECISÃO
→ permanece com a pessoa autorizada
```

Não usar urgência artificial, perda fabricada, bloqueio surpresa, upgrade automático, plano pré-selecionado como decisão ou linguagem que confunda maior plano com maior legitimidade.

`ORG-301` e `COL-301` permanecem superfícies especializadas de compreensão/comparação. Mudança consciente segue seus fluxos `301→302/303→304`; dimensionamento assistido usa `BND-002` somente quando a necessidade concreta o justificar.

## 24. Mudança de tela e continuidades disponíveis

Toda superfície deve oferecer somente continuidades justificadas por Registry, Priority Flows, Master ou navegação contextual neutra.

A UI deve diferenciar:

- **ação funcional** — produz ou solicita mudança de estado;
- **handoff** — muda responsabilidade/perspectiva;
- **navegação contextual** — muda tela sem produzir efeito material;
- **retorno** — volta ao contexto anterior sem desfazer ação;
- **atalho administrativo** — abre responsabilidade especializada sem mutação;
- **saída para Planos** — consulta capacidade comercial sem selecionar plano.

Exemplos já governados:

```text
ORG-001 ↔ ORG-301
→ TRN-427 / TRN-428
→ NAVEGAÇÃO INSTITUCIONAL SEM MUTAÇÃO COMERCIAL

COL-002 ↔ COL-301
→ TRN-417 / TRN-418
→ NAVEGAÇÃO ADMINISTRATIVA SEM MUTAÇÃO COMERCIAL

ORG-003 → ORG-008
→ TRN-214
→ ACESSO CONTEXTUAL À GESTÃO DE MANIFESTAÇÕES

COL-003 → COL-004
→ TRN-114
→ CONTINUIDADE OPERACIONAL DO VÍNCULO JÁ FORMADO
```

Relação semântica entre superfícies não autoriza criar link direto por conveniência.

## 25. Informações pertinentes sobre participantes envolvidos

Quando uma responsabilidade envolver pessoas, membros, responsáveis, administradores, solicitantes ou contraparte, a superfície deve apresentar **somente o recorte necessário para a tarefa e autorizado pelo contexto**.

Pode ser pertinente, conforme autoridade específica:

- identidade ou referência necessária;
- papel no contexto;
- vínculo;
- estado da solicitação/participação;
- responsabilidade pela próxima ação;
- proveniência da manifestação;
- dados conscientemente enviados para a finalidade;
- histórico material necessário à decisão;
- contraparte institucional/coletiva aplicável.

Nunca inferir que “membro” significa administrador, representante, aprovador ou responsável.

```text
PARTICIPANTE VISÍVEL
≠ TODOS OS DADOS VISÍVEIS

MEMBRO
≠ ADMINISTRADOR

ADMINISTRADOR
≠ AUTORIDADE UNIVERSAL

DADO EXISTENTE
≠ DADO NECESSÁRIO NESTA SUPERFÍCIE
```

## 26. Eventos, atualizações e notificações

A orquestração deve identificar **eventos materiais que exigem consciência ou continuidade**, mas não inventar canal, frequência ou automação sem autoridade específica.

Eventos potencialmente notificáveis incluem, quando governados pelo objeto:

- nova solicitação recebida;
- pedido de informação adicional;
- resposta à solicitação;
- aprovação ou recusa;
- mudança material de estado;
- ação requerida pela contraparte;
- proposta O↔C recebida ou alterada;
- aprovação, recusa, contestação, pausa ou encerramento bilateral;
- manifestação/inscrição interna recebida;
- comunicação/atualização material em `ORG-008 ↔ PER-204`;
- prazo real;
- falha ou indeterminação que exija retomada;
- capacidade/cota atingida quando isso afetar uma ação pretendida;
- resultado confirmado de mudança de plano/cobrança.

Para cada evento, a materialização deve responder, quando aplicável:

```text
O QUE ACONTECEU?
→ estado factual

QUEM / QUAL CONTEXTO?
→ recorte autorizado

EXIGE AÇÃO?
→ sim / não / indeterminado

QUAL AÇÃO?
→ somente se governada

PARA ONDE CONTINUAR?
→ superfície/handoff legítimo

O QUE NÃO DEVE SER EXPOSTO?
→ dados internos/protegidos fora da finalidade
```

Sem contrato específico, não inventar:

- e-mail obrigatório;
- push;
- SMS;
- WhatsApp;
- frequência;
- digest;
- lembrete automático;
- escalonamento;
- preferência padrão;
- marcação de leitura;
- SLA de notificação.

```text
EVENTO MATERIAL
→ PODE EXIGIR ATUALIZAÇÃO VISÍVEL

EVENTO MATERIAL
≠ CANAL AUTOMATICAMENTE AUTORIZADO
≠ AUTOMAÇÃO AUTOMATICAMENTE AUTORIZADA
```

## 27. Matriz mínima de tradução por superfície

Todo Master de superfície consumido pela orquestração deve ser traduzível para a seguinte matriz, sem exigir que todos os campos gerem UI própria:

| Dimensão | Pergunta de orquestração |
|---|---|
| contexto | quem atua e em nome de quem? |
| estado | qual é o estado real agora? |
| informação | o que precisa ser mostrado para compreender/agir? |
| participantes | quem é pertinente e qual recorte pode ser exibido? |
| ações | o que pode ser feito agora? |
| plano | o plano altera capacidade, cota ou profundidade? |
| autoridade | quem pode executar/confirmar? |
| transição | qual mudança material pode ocorrer? |
| navegação | quais continuidades neutras são legítimas? |
| feedback | como processamento, sucesso, falha ou indeterminação aparecem? |
| evento | quem precisa tomar conhecimento após mudança material? |
| proteção | o que não deve ser exposto? |
| upgrade | existe ampliação objetiva aplicável e opcional? |
| retorno | como voltar/retomar sem fabricar efeito? |



## 28. Navegação orientada por perfil, plano e descoberta de capacidades

A Orquestração deve governar **como a pessoa autorizada navega em nome da Organização ou do Coletivo**, considerando simultaneamente perfil/papel, autoridade, participante ativo, plano, estado e objeto corrente.

```text
PESSOA AUTENTICADA
+
PARTICIPANTE ATIVO
+
PAPEL / AUTORIDADE
+
PLANO VIGENTE
+
ESTADO REAL
→ AÇÕES EXECUTÁVEIS
→ AÇÕES CONDICIONAIS
→ CAPACIDADES SUPERIORES DESCOBRÍVEIS
→ CONTINUIDADES DE NAVEGAÇÃO
→ HANDOFFS
→ FEEDBACK
```

Capacidades de planos superiores **não devem desaparecer por padrão** quando sua descoberta for útil para explicar como a Organização ou o Coletivo pode ampliar sua operação.

Elas podem permanecer visíveis como capacidades superiores quando:

- pertencem comprovadamente a plano superior;
- estão claramente diferenciadas das ações executáveis;
- o motivo da indisponibilidade é explicável;
- o plano que amplia a capacidade pode ser identificado objetivamente;
- existe caminho opcional para `ORG-301` ou `COL-301`, conforme o participante;
- a ação atual continua possível quando houver alternativa no plano vigente;
- nenhuma informação protegida é revelada apenas para promover upgrade.

Exemplos:

```text
COLETIVO LIVRE
→ PUBLICAÇÃO PAGA PODE SER DESCOBRÍVEL
→ NÃO EXECUTÁVEL
→ EXPLICAR MOBILIZA/IMPACTA/REDE CONFORME AUTORIDADE COMERCIAL

ORGANIZAÇÃO CONECTA
→ ANALYTICS AVANÇADOS PODEM SER DESCOBRÍVEIS
→ NÃO SIMULAR DADOS AVANÇADOS
→ EXPLICAR ELEVA

CAPACIDADE DIMENSIONADA
→ PODE INDICAR CAMINHO ASSISTIDO
→ BND-002 SOMENTE QUANDO A NECESSIDADE CONCRETA JUSTIFICAR
```

A UI pode usar lock, badge, preview, comparação, tooltip ou outra solução definida por Design. A Orquestração governa o significado: **descoberta não equivale a entitlement**.

## 29. Contrato comportamental das superfícies

Cada superfície O/C deve funcionar como uma responsabilidade executável do sistema, não apenas como um documento de conteúdo.

Para prototipação e futura implementação, cada superfície deve permitir determinar:

| Dimensão | Comportamento governado |
|---|---|
| entrada | origem e condições legítimas de acesso |
| participante ativo | Organização ou Coletivo em cujo contexto se atua |
| perfil/papel | capacidade humana aplicável |
| autoridade | ações que a pessoa pode efetivamente realizar |
| plano | capacidade/cota/profundidade aplicável |
| estado | situação real do objeto/responsabilidade |
| conteúdo | informação necessária e autorizada |
| participantes envolvidos | recorte pertinente, papel e vínculo |
| ações executáveis | controles que podem produzir efeito agora |
| ações condicionais | controles dependentes de estado/autoridade |
| capacidades superiores | opções descobríveis de plano superior sem falsa executabilidade |
| processamento | comportamento após ação material |
| feedback | sucesso, falha, indeterminação, bloqueio ou espera |
| transição | mudança material de responsabilidade/estado |
| navegação | mudança de superfície sem efeito material |
| handoff | mudança de perspectiva/responsabilidade |
| evento | quem precisa tomar conhecimento de mudança material |
| persistência | contexto que pode permanecer legitimamente |
| retorno | retomada sem duplicação ou efeito silencioso |
| upgrade | explicação objetiva da ampliação disponível |
| proteção | informação que não pode atravessar contexto/autoridade |

A prototipação deve conseguir demonstrar esses comportamentos. A futura implementação deve poder derivar estados e regras funcionais dessas autoridades sem depender de inferência visual.


## 30. Prototipação UX/UI — cobertura mínima

Uma prototipação integrada deve conseguir demonstrar, sem afirmar implementação:

- entrada autenticada com contexto compreensível;
- Visão Geral de Organização;
- Visão Geral/Início de Coletivo;
- troca de contexto com revalidação;
- oportunidade: cadastro → ativa → manifestações;
- continuidade bilateral PER-204 ↔ ORG-008 quando aplicável;
- solicitações de Coletivo;
- participantes e vínculos;
- comunicação oficial;
- atividades, consultas e decisões;
- proteção e moderação;
- relação O↔C nas duas perspectivas;
- responsabilidades e evidências;
- autoridade insuficiente;
- contestação;
- indisponibilidade;
- retorno e retomada;
- plano/capacidade contextual quando legítimo;
- estado vazio;
- falha recuperável.

Isso não exige um frame por item.

## 31. Liberdade de Design

Este documento governa significado, continuidade e comportamento transversal, não estética.

Design pode decidir composição, grid, componentes, navegação visual, tipografia conforme autoridade de marca, cores, imagens, iconografia, densidade, motion, microinterações, responsividade e quantidade de frames.

A liberdade visual não pode alterar participante, autoridade, responsabilidade, estado, transição, evidência, plano ou significado governado.

## 32. IA — source lock

IA utilizada para Design ou prototipação deve operar em source lock com o GKR e consumir esta autoridade junto dos Masters necessários.

```text
NÃO ESTÁ GOVERNADO NO GKR
→ NÃO INVENTAR
→ SINALIZAR LACUNA
→ NÃO CRIAR SUPERFÍCIE
→ NÃO CRIAR TRANSIÇÃO
→ NÃO CRIAR PERMISSÃO
→ NÃO CRIAR ENTITLEMENT
→ NÃO CRIAR MÉTRICA
```

IA é consumidora da verdade de produto, não sua autora.

## 33. Critérios executivos de aceite

Uma materialização orientada por esta autoridade é semanticamente aceitável quando:

1. Organização e Coletivo parecem experiências contínuas;
2. participante, contexto, papel e autoridade permanecem compreensíveis;
3. troca de contexto revalida autoridade;
4. Organização e Coletivo não são artificialmente simétricos;
5. bilateralidade O↔C preserva duas perspectivas;
6. ações materiais distinguem processamento e resultado;
7. estados alternativos são representáveis;
8. retornos não produzem mutação silenciosa;
9. plano não substitui autoridade;
10. evidência não vira causalidade ou impacto por inferência;
11. proteção e minimização permanecem preservadas;
12. O↔O e C↔C não são inventados;
13. IA não cria verdade de produto;
14. Design mantém liberdade criativa;
15. protótipo não é confundido com implementação;
16. Product Engineering não é liberado por esta autoridade.

## 34. Ordem recomendada de consumo

```text
LEIA PRIMEIRO
→ ESTE DOCUMENTO DE ORQUESTRAÇÃO
→ JORNADAS INTEGRADAS O/C
→ JOBS / AUTORIDADE
→ ARQUITETURA DA INFORMAÇÃO
→ MAPA DE SUPERFÍCIES
→ MAPA DE ESTADOS
→ FLUXOS PRIORITÁRIOS
→ MASTER DA SUPERFÍCIE EM CONSTRUÇÃO
→ REGISTRIES / AUTORIDADE ESPECÍFICA QUANDO NECESSÁRIO
```

## 35. Boundary de maturidade

Esta autoridade candidata organiza o consumo da verdade documental já existente. Ela não reabre o checkpoint de completude estrutural e não promove maturidade de superfície ou transição.

```text
DOCUMENTARY COMPLETENESS
→ PASS / PRESERVED

NEW GKR-SURF-*
→ NONE

NEW GKR-TRN-*
→ NONE

HIGH-FIDELITY DELIVERY
→ NOT_RECEIVED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED BY THIS DOCUMENT

PRODUCT ENGINEERING
→ NOT_RELEASED
```

## Integrações transversais entre participantes

Esta Orquestração deve consumir conjuntamente:

- `GKR-UX-PARTICIPANT-RELATIONSHIPS-INTERACTIONS-001` para relações, interação, conexão, visibilidade bilateral e recorte de dados entre Pessoa, Coletivo e Organização;
- `GKR-UX-COMMUNICATIONS-NOTIFICATIONS-001` para eventos, atualizações, comunicações e notificações decorrentes dessas relações.

```text
RELAÇÃO / VISIBILIDADE
→ CONTRATO DE PARTICIPANTES

EVENTO / COMUNICAÇÃO / ALERTA
→ CONTRATO DE COMUNICAÇÕES E NOTIFICAÇÕES

ORQUESTRAÇÃO LOCAL
→ NÃO INVENTA NENHUM DOS DOIS
```


## 36. Estado

```text
O/C JOURNEY UX/UI ORCHESTRATION
→ CANDIDATE

ROLE
→ MASTER / END-TO-END ORCHESTRATION
→ DESIGN + AI + PROTOTYPING CONSUMPTION

DOCUMENTARY COMPLETENESS
→ PRESERVED / PASS

NEW SURFACE / TRANSITION IDS
→ NONE

VISUAL BASELINE
→ NONE CREATED BY THIS DOCUMENT

AI
→ SOURCE-LOCKED TO GKR

PRODUCT ENGINEERING
→ NOT RELEASED
```
