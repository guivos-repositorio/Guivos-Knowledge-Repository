---
id: GKR-UX-ORG-ACTIVE-OPPORTUNITY-MASTER-001
title: Jornada de Organizações e Coletivos — Organização — Oportunidade Aprovada / Ativa — Documento Mestre de Superfície
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-ORG-002
  - GKR-SURF-ORG-003
  - GKR-SURF-PER-201
  - GKR-TRN-202
  - GKR-TRN-203
  - GKR-JOURNEY-ORGANIZATION-001
---

# Organização — Oportunidade Aprovada / Ativa — Documento Mestre de Superfície

## 1. Responsabilidade

Este Documento Mestre governa a responsabilidade funcional de `GKR-SURF-ORG-003` — oportunidade institucional aprovada/ativa.

A superfície permite que uma Pessoa legitimamente autorizada, atuando no contexto de uma Organização, compreenda e administre o estado institucional de uma oportunidade ou programa depois do ciclo de cadastro e revisão governado por `GKR-SURF-ORG-002`.

```text
ORG-002
→ GKR-TRN-202
→ ORG-003
→ GKR-TRN-203
→ ELEGIBILIDADE PARA DESCOBERTA PELA PESSOA
```

A responsabilidade de `ORG-003` começa quando existe estado institucional suficiente para a continuidade aprovada/ativa. Ela não absorve cadastro, não decide relevância individual e não controla a jornada da Pessoa.

```text
CADASTRO
≠ APROVAÇÃO

APROVAÇÃO
≠ ATIVAÇÃO

ATIVAÇÃO
≠ DISTRIBUIÇÃO GARANTIDA

PUBLICAÇÃO
≠ RELEVÂNCIA

DESCOBERTA ELEGÍVEL
≠ MATCH GARANTIDO
≠ RESULTADO
≠ IMPACTO
```

## 2. Por que esta responsabilidade é específica da Organização

`GKR-SURF-ORG-003` materializa uma responsabilidade institucional própria do domínio **Oportunidades e Programas** e atende a continuidade de `ORG-J04`.

O Coletivo possui atividades, oportunidades e decisões sob outras responsabilidades e autoridades. O GKR não registra uma superfície do Coletivo semanticamente equivalente a `ORG-003`.

Consequentemente:

- este Master não é compartilhado por inferência;
- nenhuma superfície do Coletivo é criada para produzir simetria;
- diferenças entre Organização e Coletivo permanecem explícitas;
- eventual equivalência futura depende de autoridade documental própria.

## 3. Participante, contexto e autoridade

O agente humano continua sendo uma **Pessoa autenticada** atuando no contexto de uma Organização.

Antes de qualquer ação material, a experiência deve preservar:

- Organização ativa correta;
- unidade ou contexto institucional aplicável, quando existente;
- papel da Pessoa;
- representação válida;
- autoridade compatível com a ação;
- aprovação adicional quando exigida pela autoridade de origem;
- estado corrente do objeto.

```text
ACESSAR
≠ EDITAR

EDITAR
≠ ATIVAR

ATIVAR
≠ PAUSAR

PAUSAR
≠ ENCERRAR

REPRESENTAR
≠ AUTORIDADE IRRESTRITA
```

Mudança de contexto, expiração de sessão ou alteração material de autoridade exige revalidação antes de efeito institucional.

## 4. Origens e destinos legítimos

### 4.1 Origem principal

A origem registrada é:

```text
GKR-SURF-ORG-002
→ GKR-TRN-202
→ GKR-SURF-ORG-003
```

A maturidade de `GKR-TRN-202` permanece a definida pelo Transition Registry. Este Master não a promove.

Retornos legítimos ao objeto já ativo também podem ocorrer a partir do contexto autenticado da Organização quando a autoridade vigente permitir localizar o objeto canônico. Isso não cria nova transição.

### 4.2 Continuidade para descoberta

A continuidade registrada é:

```text
GKR-SURF-ORG-003
→ GKR-TRN-203
→ GKR-SURF-PER-201
```

`GKR-TRN-203` expressa a continuidade de elegibilidade para descoberta. Ela não transfere à Organização autoridade sobre a experiência, o contexto pessoal ou a relevância individual da Pessoa.

### 4.3 Outras continuidades

Pausa, correção, encerramento, responsabilidades e evidências permanecem limitados às autoridades existentes. Este Master não cria transições para preencher lacunas do Registry.

## 5. Job principal

A Pessoa autorizada deve conseguir:

1. identificar qual oportunidade/programa está administrando e em nome de qual Organização;
2. compreender o estado institucional corrente;
3. revisar informações materiais vigentes e sua proveniência;
4. identificar condições, riscos, vigência, disponibilidade e responsabilidades relevantes;
5. reconhecer o que exige atenção ou correção;
6. executar somente ações permitidas pelo estado e pela autoridade;
7. distinguir edição, ativação, pausa, correção, retirada e encerramento;
8. compreender quando a oportunidade está elegível para descoberta sem interpretar isso como garantia de distribuição;
9. reconhecer resultado confirmado, falha recuperável ou estado indeterminado;
10. retornar ao contexto institucional sem perder a referência ao objeto canônico.

## 6. Informação e dados

Quando sustentados pelas autoridades de origem, a responsabilidade pode apresentar ou operar:

- identidade da oportunidade ou programa;
- Organização responsável;
- unidade/contexto institucional aplicável;
- responsável institucional autorizado;
- descrição e finalidade;
- disponibilidade e vigência;
- condição econômica ou preço, quando houver;
- elegibilidade e condições materiais;
- riscos e responsabilidades;
- relação comercial aplicável;
- evidências e referências autorizadas;
- estado de aprovação/ativação;
- estado de disponibilidade;
- alterações materiais;
- situação de pausa, retirada, expiração ou encerramento;
- informação necessária à continuidade de descoberta elegível.

A superfície não deve inventar por convenção:

- alcance;
- impressões;
- conversões;
- ranking;
- score;
- demanda prevista;
- taxa de sucesso;
- impacto;
- recomendação universal;
- performance;
- audiência estimada;
- prioridade algorítmica.

## 7. Proveniência e verdade operacional

Informações materiais devem preservar, quando aplicável, sua condição:

```text
DECLARADO
≠ VERIFICADO

APROVADO
≠ ATIVO

ATIVO
≠ DISPONÍVEL EM TODO CONTEXTO

INFERIDO
≠ FATO

AUSÊNCIA DE DADO
≠ ZERO

DESATUALIZADO
≠ ATUAL

CONTESTADO
≠ INVÁLIDO POR DEFINIÇÃO
```

A experiência não deve transformar síntese, inferência ou cache em nova fonte institucional de verdade.

## 8. Estados mínimos

A materialização futura deve comportar, quando aplicáveis:

- aprovado e aguardando ativação;
- ativo;
- ativo com informação material incompleta;
- ativo com atenção material;
- alteração pendente de revisão ou aprovação;
- autoridade insuficiente;
- aprovação adicional necessária;
- pausado;
- correção em processamento;
- retirada solicitada;
- encerramento solicitado;
- encerrado;
- expirado;
- indisponível por condição real;
- contestado;
- bloqueado por proteção, privacidade ou governança;
- dependência externa indisponível;
- processamento em curso;
- falha recuperável;
- resultado indeterminado;
- atualização concorrente;
- contexto ou sessão expirados;
- operação degradada ou baixa conectividade.

```text
PAUSADO
≠ ENCERRADO

EXPIRADO
≠ EXCLUÍDO

BLOQUEADO
≠ RECUSADO

AGUARDANDO
≠ APROVADO

INDISPONIBILIDADE TÉCNICA
≠ FALHA DA ORGANIZAÇÃO
```

## 9. Ações e controles

Somente quando estado e autoridade permitirem, a responsabilidade pode oferecer:

- revisar informações vigentes;
- corrigir informação;
- concluir ação pendente legitimamente autorizada;
- ativar;
- pausar;
- retomar após pausa, quando permitido;
- solicitar ou executar retirada;
- solicitar ou executar encerramento;
- revisar condição contestada;
- retornar ao contexto institucional;
- revalidar contexto e autoridade;
- repetir processamento recuperável sem duplicar efeito material.

A existência de um controle visual não concede autoridade.

Ações materiais exigem feedback proporcional e confirmação antes de serem apresentadas como concluídas.

## 10. Alterações materiais

Alterações capazes de mudar condição, elegibilidade, risco, responsabilidade, disponibilidade ou relação econômica devem respeitar a autoridade aplicável.

Quando uma alteração exigir nova revisão ou aprovação:

```text
ESTADO VIGENTE
→ ALTERAÇÃO PROPOSTA
→ REVISÃO / APROVAÇÃO LEGÍTIMA
→ NOVO ESTADO EFETIVO

ATÉ CONFIRMAÇÃO
→ NÃO DECLARAR A ALTERAÇÃO COMO EFETIVA
```

Este Master não inventa quais campos exigem reaprovação quando essa regra não estiver definida pela autoridade de origem.

## 11. Ativação, pausa, retirada e encerramento

Esses estados não são equivalentes.

- **ativação** torna efetivo o estado autorizado aplicável;
- **pausa** interrompe temporariamente a continuidade permitida sem declarar encerramento;
- **retirada** remove a oportunidade da continuidade aplicável quando a autoridade e o estado permitirem;
- **encerramento** finaliza a continuidade institucional segundo as responsabilidades remanescentes;
- **expiração** decorre de condição temporal ou material definida, não de decisão implícita da interface.

Nenhuma dessas ações autoriza apagar trilha legítima, evidência necessária, obrigação remanescente ou direito de contestação.

## 12. Descoberta e relação com a Jornada da Pessoa

A Organização administra a verdade institucional da oportunidade dentro de sua autoridade.

A Jornada da Pessoa administra descoberta e compreensão pessoal sob autoridades próprias.

```text
ORG-003
→ PODE TORNAR A OPORTUNIDADE ELEGÍVEL À CONTINUIDADE REGISTRADA

ORG-003
→ NÃO ESCOLHE QUEM DEVE RECEBER A OPORTUNIDADE
→ NÃO DEFINE RELEVÂNCIA INDIVIDUAL
→ NÃO ACESSA CONTEXTO PESSOAL POR CONSEQUÊNCIA
→ NÃO GARANTE MATCH
→ NÃO GARANTE CONVERSÃO
```

Ads, patrocínio ou relação comercial não podem ser confundidos com relevância orgânica.

## 13. Processamento e confirmação

Ações materiais seguem a distinção:

```text
INTENÇÃO
→ CONFIRMAÇÃO CONSCIENTE, QUANDO APLICÁVEL
→ PROCESSAMENTO
→ SUCESSO CONFIRMADO
  OU FALHA RECUPERÁVEL
  OU RESULTADO INDETERMINADO
```

Regras:

- interface otimista não substitui confirmação da fonte responsável;
- retry não pode duplicar efeito material;
- resultado indeterminado exige reconsulta antes de repetir ação;
- mudança de contexto exige revalidação;
- sucesso técnico não deve ser confundido com resultado institucional quando forem estados distintos.

## 14. Vazio, erro, indisponibilidade e recuperação

A experiência deve tratar explicitamente:

- oportunidade não localizada;
- estado ainda não disponível;
- informação material ausente;
- dado inválido ou desatualizado;
- contestação;
- autoridade insuficiente;
- aprovação adicional pendente;
- dependência externa indisponível;
- processamento interrompido;
- resultado desconhecido;
- atualização concorrente;
- contexto expirado;
- baixa conectividade.

Recuperação deve preservar conteúdo e estado legítimos quando seguro, permitir retorno e orientar somente ações sustentadas pela autoridade vigente.

Nenhum erro técnico deve ser apresentado como falha moral, operacional ou institucional da Organização.

## 15. Reversibilidade e continuidade

A experiência deve distinguir:

```text
VOLTAR
≠ DESFAZER

PAUSAR
≠ ENCERRAR

CANCELAR UMA INTENÇÃO
≠ APAGAR HISTÓRICO LEGÍTIMO

RETRY
≠ REPETIR EFEITO MATERIAL

RETORNAR AO OBJETO
→ RECONSULTAR ESTADO CANÔNICO QUANDO NECESSÁRIO
```

Ações irreversíveis ou materialmente relevantes exigem tratamento proporcional e não podem ocorrer por navegação, fechamento de janela ou simples mudança de contexto.

## 16. Planos e capacidade comercial

Planos permanecem capacidade especializada/contextual da Organização.

Este Master não autoriza:

- inventar quota;
- inventar entitlement;
- limitar publicação sem autoridade comercial correspondente;
- alterar relevância orgânica por plano;
- converter atenção operacional em upsell;
- ocultar condição material para induzir contratação;
- prometer alcance, distribuição, resultado ou impacto por plano.

Quando um limite comercial real e documentado afetar uma capacidade, a experiência pode explicar o limite e oferecer continuidade legítima para Planos sem bloquear alternativas já autorizadas.

## 17. Privacidade, proteção e minimização

A superfície deve utilizar somente dados necessários à responsabilidade institucional.

A relação entre oportunidade e Pessoa não concede automaticamente à Organização acesso a:

- contexto pessoal;
- objetivos privados;
- inferências individuais;
- dados sensíveis;
- histórico pessoal;
- razões internas de relevância;
- outras relações da Pessoa.

Informações sensíveis, protegidas ou contestadas seguem sua autoridade de origem.

## 18. Acessibilidade

Estado, autoridade, risco, alteração material, pausa, bloqueio, processamento, erro e confirmação não podem depender exclusivamente de:

- cor;
- ícone;
- posição;
- animação;
- hover;
- blur;
- densidade;
- contraste implícito.

A experiência deve permitir compreensão equivalente e operação por meios acessíveis.

## 19. Liberdade de Design

Design mantém liberdade sobre:

- composição;
- grid;
- navegação local;
- componentes;
- hierarquia visual;
- número de frames;
- tipografia dentro da autoridade oficial de marca;
- imagens e ícones;
- densidade;
- motion;
- solução responsiva.

Design não pode:

- fundir `ORG-002` e `ORG-003` em uma única responsabilidade funcional por conveniência;
- inventar estados ou ações;
- transformar oportunidade ativa em dashboard obrigatório;
- criar métricas sem autoridade;
- prometer alcance, relevância, conversão ou impacto;
- ocultar risco ou condição material;
- representar processamento como sucesso;
- usar low-fidelity como baseline visual canônica.

## 20. IA e prototipação — source lock

IA pode explorar forma de materializar esta responsabilidade, mas não pode inventar:

- ações;
- campos;
- estados;
- transições;
- automações;
- validações materiais;
- critérios de elegibilidade;
- métricas;
- rankings;
- recomendações;
- notificações;
- integrações;
- permissões;
- entitlement;
- regra de plano;
- persistência;
- comportamento de descoberta.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 21. Critérios de aceite

Este Master é funcionalmente suficiente quando a materialização:

1. preserva `ORG-003` como responsabilidade distinta de `ORG-002`;
2. identifica claramente Organização, objeto, estado e autoridade;
3. preserva `TRN-202` e `TRN-203` sem promoção;
4. não confunde aprovação, ativação, publicação, descoberta, relevância, resultado e impacto;
5. suporta estados de pausa, expiração, contestação, bloqueio, indisponibilidade e resultado indeterminado quando aplicáveis;
6. exige autoridade compatível antes de efeito material;
7. preserva revisão proporcional de alterações materiais;
8. não concede à Organização autoridade sobre contexto pessoal ou relevância individual;
9. não inventa métricas, alcance, score ou performance;
10. mantém Planos como capacidade especializada/contextual;
11. preserva reversibilidade e recuperação sem duplicar efeito;
12. mantém low-fidelity como evidência funcional, não baseline visual;
13. mantém IA em source lock;
14. não cria IDs nem promove maturidade;
15. não libera Product Engineering.

## 22. Lacunas preservadas

Permanecem fora deste Master até autoridade específica:

- regras técnicas finais de publicação e descoberta;
- mecanismo técnico de elegibilidade/distribuição;
- critérios adicionais não documentados de aprovação;
- regras técnicas finais de alteração material;
- RBAC técnico;
- persistência;
- integrações externas;
- notificações finais;
- analytics e KPIs;
- entitlement técnico;
- high-fidelity final;
- protótipo;
- implementação;
- Product Engineering.

`GKR-SURF-ORG-007` permanece responsabilidade distinta para resultados/evidências institucionais e não é completada por inferência neste documento.

## 23. Estado documental

```text
MASTER
→ DRAFT / FUNCTIONAL CONTRACT CANDIDATE

SURFACE GOVERNED
→ GKR-SURF-ORG-003

ORIGIN
→ GKR-SURF-ORG-002 / GKR-TRN-202

DISCOVERY CONTINUITY
→ GKR-SURF-PER-201 / GKR-TRN-203

COLLECTIVE EQUIVALENT
→ NONE BY INFERENCE

NEW SURFACE ID
→ NONE

NEW TRANSITION ID
→ NONE

MATURITY PROMOTION
→ NONE

LOW-FIDELITY
→ FUNCTIONAL EVIDENCE / NOT VISUAL BASELINE

PROTOTYPE
→ NOT AUTHORIZED BY THIS MASTER

PRODUCT ENGINEERING
→ NOT RELEASED
```
