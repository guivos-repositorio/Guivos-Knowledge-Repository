---
id: GKR-UX-PER107-MASTER-001
title: Jornada da Pessoa — PER-107 — Central de Atualizações — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - UXA-056
  - UXA-092
  - UXA-094
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-106
  - GKR-SURF-PER-107
  - GKR-SURF-PER-108
  - GKR-TRN-110
  - GKR-TRN-111
---

# Jornada da Pessoa — PER-107 — Central de Atualizações — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-107 — Central de Atualizações` para designer humana, IA opcional, Produto, UX, Research, Privacidade e Engenharia.

A superfície permite à Pessoa **triar e compreender atualizações relacionadas a vínculos legítimos, reconhecer origem, tipo, autoridade, contexto temporal e ação possível e decidir conscientemente se deseja seguir para uma continuidade válida**.

`PER-107` não é feed de engajamento, ranking, score, mecanismo de pressão por leitura nem executor automático da ação comunicada.

## 2. Papel na Journey

```text
PER-106 — MEUS COLETIVOS
→ AÇÃO EXPLÍCITA
→ TRN-110 / INTEGRALLY VALIDATED
→ PER-107 — CENTRAL DE ATUALIZAÇÕES

PER-107
→ CONTINUIDADE LEGÍTIMA
→ TRN-111 / INTEGRALLY VALIDATED
→ PER-108 — INÍCIO DO PARTICIPANTE
```

Abrir a Central não altera vínculo, não cria presença, não constitui participação e não confirma efeito substantivo.

## 3. Job da Pessoa

A superfície deve permitir que a Pessoa:

1. reconheça atualizações legitimamente relacionadas aos seus vínculos;
2. compreenda de onde cada atualização veio;
3. diferencie tipo de atualização;
4. reconheça a autoridade associada quando aplicável;
5. compreenda data e contexto temporal;
6. identifique ação possível e prazo legítimo quando existirem;
7. reconheça qual vínculo está relacionado;
8. diferencie atenção comum de risco ou segurança material;
9. perceba quando uma atualização se tornou obsoleta;
10. escolha conscientemente uma continuidade;
11. ajuste preferências de atualização dentro da autoridade existente;
12. retorne sem produzir efeito substantivo.

## 4. Estrutura mínima de compreensão

Cada atualização deve tornar compreensíveis, quando aplicável:

- origem;
- tipo;
- autoridade;
- data;
- ação possível;
- prazo legítimo;
- vínculo relacionado.

A ausência legítima de um desses elementos não autoriza sua invenção.

## 5. Triagem, não feed

A Central existe para triagem e compreensão.

```text
CENTRAL
→ COMPREENDER
→ PRIORIZAR ATENÇÃO LEGÍTIMA
→ ESCOLHER

CENTRAL
≠ FEED DE ENGAJAMENTO
≠ COMPETIÇÃO POR ATENÇÃO
≠ POPULARIDADE
≠ SCORE
≠ PRESSÃO POR FREQUÊNCIA
```

A designer pode organizar e agrupar conteúdo, mas a composição não deve converter volume, frequência ou leitura em mérito.

## 6. Ordenação funcional

Quando risco ou segurança material competir com atenção comum, risco ou segurança material pode preceder atenção comum.

Essa precedência:

- protege compreensão e ação legítima;
- não cria score da Pessoa;
- não cria score do Coletivo;
- não mede importância pessoal;
- não cria ranking de participantes;
- não transforma volume de atualização em prioridade.

Qualquer ordenação adicional deve permanecer dentro das autoridades correntes e não pode ser inventada como regra canônica.

## 7. Leitura versus efeito

```text
VISUALIZAR
≠ EXECUTAR

ABRIR
≠ ACEITAR

LER
≠ PRODUZIR EFEITO SUBSTANTIVO

AÇÃO SUBSTANTIVA
→ REVALIDAR ESTADO CORRENTE NO DESTINO
→ PRODUZIR EFEITO SOMENTE SE AINDA VÁLIDO
```

A interface não pode representar simples visualização como consentimento, presença, participação, aceite ou conclusão de obrigação.

## 8. Atualização obsoleta

Quando uma atualização estiver obsoleta, a experiência deve:

- deixar de apresentá-la como estado corrente;
- tornar a obsolescência compreensível quando relevante;
- impedir ação baseada em estado inválido;
- preservar contexto necessário para compreensão;
- revalidar o destino antes de ação substantiva.

Obsolescência não autoriza apagar silenciosamente contexto material que a Pessoa precise compreender.

## 9. Preferências

Preferências de atualização permanecem separadas de vínculo e autoridade.

```text
SILENCIAR / REDUZIR ATUALIZAÇÕES
≠ ENCERRAR PARTICIPAÇÃO
≠ REVOGAR AUTORIDADE
≠ REVOGAR OBRIGAÇÃO MATERIAL
```

A experiência deve evitar linguagem que faça a Pessoa acreditar que controlar notificações equivale a sair do Coletivo ou alterar seu papel.

## 10. Idempotência de consumo

Repetir abertura, retorno ou leitura:

- não duplica evento substantivo;
- não muda vínculo;
- não cria presença;
- não cria participação;
- não produz aceite;
- não altera autoridade por si só.

## 11. TRN-110 — entrada na Central

`PER-106 → PER-107`.

A transição parte de `Meus Coletivos` por ação explícita da Pessoa.

Estado: **integralmente validada**.

A transição:

- não altera vínculo;
- não confirma leitura substantiva;
- não produz efeito da atualização;
- não cria presença ou participação.

## 12. TRN-111 — continuidade para Início do Participante

`PER-107 → PER-108`.

Estado: **integralmente validada**.

A continuidade deve preservar vínculo e contexto legítimo. A Central não absorve a responsabilidade de `PER-108 — Início do Participante`.

Qualquer ação substantiva disparada a partir de uma atualização deve revalidar o estado corrente no destino antes de produzir efeito.

## 13. Ações e controles

Conforme autoridade e atualização, a Pessoa pode:

- abrir uma atualização para compreender contexto;
- filtrar ou agrupar atualizações quando houver suporte legítimo;
- seguir uma ação válida;
- abrir continuidade do vínculo quando contratada;
- ajustar preferências permitidas;
- retornar a `PER-106`;
- ignorar ou adiar atenção quando não houver obrigação material;
- reconhecer atualização obsoleta sem executar ação inválida.

Este Master não inventa ação, destino ou obrigação ausente das autoridades.

## 14. Estados internos de experiência

A designer pode representar dentro de `PER-107`:

- carregamento e revalidação;
- conjunto de atualizações;
- agrupamento ou filtro legítimo;
- ausência de atualizações;
- atualização não lida;
- atualização compreendida;
- atualização com ação disponível;
- atualização com prazo legítimo;
- atualização material de risco ou segurança;
- atualização obsoleta;
- vínculo ou autorização alterados;
- erro recuperável;
- indisponibilidade temporária.

Esses estados não criam novos `PER-ID`s.

## 15. Vazio

Ausência de atualizações é estado legítimo.

A experiência não deve transformar vazio em:

- falha de engajamento;
- recomendação obrigatória;
- incentivo artificial à atividade;
- pressão para participar mais;
- permissão para inventar conteúdo.

## 16. Prazo e obrigação

Prazo legítimo deve ser apresentado somente quando existir autoridade e dado correspondente.

A existência de prazo:

- não significa prioridade moral;
- não significa culpa;
- não autoriza contagem regressiva manipulativa;
- não autoriza inventar consequência;
- não substitui explicação sobre a ação correspondente.

Obrigações materiais não desaparecem apenas porque a Pessoa silenciou uma categoria de atualização.

## 17. Privacidade e minimização

A Central deve apresentar somente o contexto necessário para a finalidade da atualização.

Não deve expor automaticamente:

- contexto privado da Journey;
- vínculos não relacionados;
- dados de outros participantes;
- informação operacional reservada;
- inferências pessoais;
- dados sensíveis sem finalidade e autoridade.

## 18. Processamento e recuperação

Antes de efeito substantivo:

1. revalidar estado corrente;
2. revalidar vínculo quando necessário;
3. revalidar autorização quando necessário;
4. confirmar que ação continua disponível;
5. impedir ação quando o estado de origem estiver obsoleto;
6. preservar contexto suficiente para recuperação.

A Central não deve executar silenciosamente ação que exige confirmação ou autoridade no destino.

## 19. Linguagem e claims

Evitar linguagem que:

- trate não lidos como dívida moral;
- transforme frequência em mérito;
- use urgência sem fundamento;
- confunda leitura com aceite;
- confunda abertura com presença;
- apresente prazo inexistente;
- apresente autoridade não comprovada;
- transforme atualização em obrigação universal;
- trate preferência como alteração do vínculo.

Preferir linguagem factual, contextual e proporcional ao efeito real.

## 20. Acessibilidade

Origem, tipo, autoridade, data, prazo, estado, obsolescência e ação devem ser compreensíveis sem depender exclusivamente de:

- cor;
- posição;
- ícone;
- animação;
- som.

Prioridade material e estado obsoleto devem possuir rótulos compreensíveis por tecnologias assistivas.

## 21. Dados reais e conteúdo sintético

Nenhuma atualização, origem, autoridade, prazo, vínculo, ação, contagem ou estado pode ser inventado e apresentado como real.

Conteúdo sintético para prototipação é permitido quando:

- claramente fictício;
- não atribuído a entidade ou pessoa real;
- não cria regra de produto;
- não cria urgência falsa;
- não inventa obrigação;
- não sugere vínculo inexistente;
- respeita limites e estados canônicos.

## 22. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer possui liberdade sobre composição, agrupamento, densidade, componentes, ritmo, imagens, iconografia, motion, microinterações e responsividade, preservando:

- triagem e compreensão;
- distinção entre leitura e efeito;
- clareza de origem e autoridade;
- tratamento proporcional de risco e segurança;
- privacidade;
- acessibilidade;
- handoffs governados;
- autoridades atuais de marca, incluindo tipografia oficial quando aplicável.

## 23. Limites para IA

IA não pode:

- inventar atualização, origem, autoridade, prazo, vínculo ou ação;
- criar ranking ou score;
- usar não lidos para pressionar a Pessoa;
- inferir urgência sem fundamento;
- marcar efeito substantivo por simples leitura;
- transformar preferência em alteração de vínculo;
- executar ação sem revalidar destino;
- manter ação obsoleta como válida;
- absorver `PER-108` em `PER-107`;
- promover ou rebaixar `TRN-110` ou `TRN-111`;
- criar novo `PER-ID`;
- impor baseline visual;
- iniciar Product Engineering.

## 24. Critérios de aceite funcional

O consumo de `PER-107` é aceitável quando:

1. a Central permanece superfície de triagem e compreensão;
2. não se torna feed de engajamento;
3. origem é compreensível quando aplicável;
4. tipo é compreensível quando aplicável;
5. autoridade é compreensível quando aplicável;
6. data é compreensível;
7. ação possível é clara quando existente;
8. prazo só aparece quando legítimo;
9. vínculo relacionado é compreensível;
10. risco ou segurança material pode preceder atenção comum sem criar score;
11. leitura não é apresentada como execução;
12. abertura não é apresentada como aceite;
13. ação substantiva revalida estado no destino;
14. atualização obsoleta não mantém ação inválida;
15. preferências permanecem separadas do vínculo;
16. silenciar não encerra participação;
17. repetição de abertura/leitura não duplica evento;
18. `TRN-110` permanece integralmente validada;
19. entrada pela `TRN-110` exige ação explícita;
20. `TRN-111` permanece integralmente validada;
21. `PER-108` permanece responsabilidade separada;
22. vazio não gera pressão por engajamento;
23. prazo não cria consequência inventada;
24. privacidade e minimização são preservadas;
25. estados internos não criam novos `PER-ID`s;
26. erros não fabricam atualização ou estado;
27. conteúdo sintético não se apresenta como real;
28. acessibilidade não depende apenas de cor ou posição;
29. Design preserva liberdade criativa dentro das autoridades;
30. Product Engineering permanece não liberado.

## 25. Lacunas que não podem ser preenchidas por inferência

Este Master não autoriza inventar:

- algoritmo geral de ordenação;
- score de relevância;
- política universal de urgência;
- arquitetura técnica de notificações;
- canal de entrega;
- política jurídica universal de obrigação;
- novos tipos canônicos de atualização;
- novas ações substantivas;
- novos destinos;
- novas transições;
- novos `PER-ID`s;
- implementação de Product Engineering.

## 26. Estado

```text
PER-107
→ DOCUMENTED

MASTER
→ GKR-UX-PER107-MASTER-001 v0.1.0
→ CURRENT

TRN-110
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-111
→ INTEGRALLY VALIDATED / UNCHANGED

PER-108
→ SEPARATE RESPONSIBILITY

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-108 — Início do Participante`.
