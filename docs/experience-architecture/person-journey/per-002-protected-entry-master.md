---
id: GKR-UX-PER002-MASTER-001
title: Jornada da Pessoa — PER-002 — Entrada Protegida — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-HOME-MASTER-001
  - UXA-020
  - UXA-023
  - UXA-035
  - GKR-UX-PER002-PROTOTYPE-DELIVERY-001
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - PER-001
  - PER-002
  - PER-003
  - TRN-001
  - TRN-002
---

# Jornada da Pessoa — PER-002 — Entrada Protegida — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a **definição corrente de consumo de `PER-002 — Entrada Protegida`** para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

Ele detalha o que a superfície precisa **explicar, exibir, solicitar, capturar, bloquear, permitir, entregar e preservar**, sem definir tela, layout, wireframe, UI, direção visual, protótipo novo ou implementação.

```text
PER-001 — HOME PÚBLICA
→ decisão consciente de iniciar
→ PER-002 — ENTRADA PROTEGIDA
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE
```

`PER-002` é uma única responsabilidade funcional. Estados internos, autenticação, recuperação e variantes de sessão **não criam novas superfícies**.

## 2. Papel na Jornada

`PER-002` é a primeira responsabilidade protegida da Jornada da Pessoa após a Home pública.

Seu papel não é capturar o Momento Atual. Seu papel é **preparar a Pessoa para entrar conscientemente em um contexto protegido**, preservando autonomia, finalidade, controle e clareza sobre o que poderá acontecer depois.

```text
PER-002
→ ORIENTA
→ PROTEGE
→ AUTENTICA QUANDO NECESSÁRIO
→ EXPLICA CONTROLES
→ PRESERVA ALTERNATIVAS
→ PREPARA HANDOFF

PER-002
≠ RELATO DO MOMENTO ATUAL
≠ PROCESSAMENTO MATERIAL DO RELATO
≠ COMPREENSÃO INICIAL
≠ TELA HOJE
```

## 3. Job principal da Pessoa

A Pessoa precisa conseguir responder, antes de prosseguir:

- onde estou entrando;
- por que este ambiente é protegido;
- o que será possível fazer depois;
- se preciso me autenticar agora;
- o que autenticação autoriza e o que não autoriza;
- quais controles eu mantenho;
- como voltar, interromper ou não prosseguir;
- qual é o próximo passo legítimo se eu decidir continuar.

## 4. Origem e destino

### Origem

`PER-002` pode ser alcançada a partir da Home pública por `TRN-001`, cuja continuidade permanece parcial.

A entrada deve preservar que:

- iniciar a Journey é decisão voluntária;
- a Home não diagnostica nem presume necessidade;
- nenhum relato pessoal deve ser tratado como já fornecido;
- entrar não equivale a autorizar processamento material.

### Destino

O destino funcional próprio de `PER-002` é `PER-003 — Escolha de Modalidade`, via `TRN-002`, localmente validada.

```text
PER-002 CONCLUÍDA
→ HANDOFF READY
→ TRN-002
→ PER-003

AUTHENTICATION COMPLETED
≠ PER-002 CONCLUÍDA
```

## 5. Estados internos obrigatoriamente compreendidos

O Documento de Design deve conseguir acomodar, quando aplicável, os seguintes estados funcionais dentro da mesma superfície:

1. orientação protegida / pré-autenticação;
2. autenticação necessária;
3. sessão já autenticada;
4. continuação autenticada com controles;
5. recuperação de acesso;
6. restrição ou indisponibilidade;
7. falha recuperável;
8. alternativa de interrupção / saída;
9. estado pronto para handoff a `PER-003`.

```text
9 ESTADOS / RESPONSABILIDADES INTERNAS
≠ 9 TELAS CANÔNICAS
≠ 9 PER-IDs
```

Design pode resolver esses estados por páginas, painéis, modais, variações, navegação progressiva ou outra composição coerente, desde que a semântica funcional seja preservada.

## 6. O que deve ser exibido

Antes de qualquer processamento material da Journey, a experiência deve tornar compreensível, em nível proporcional:

- que a Pessoa saiu do ambiente público;
- que entrou em contexto protegido;
- finalidade geral do fluxo protegido;
- diferença entre dados de acesso e conteúdo da Journey;
- quando autenticação é necessária;
- quais tipos de controle estarão disponíveis;
- que avançar é opcional;
- que é possível voltar ou interromper;
- que autenticação não equivale a consentimento amplo;
- que finalidades materiais futuras exigem autoridade compatível.

Não é necessário expor toda a política jurídica ou técnica nesta superfície. A informação deve ser suficiente para uma decisão consciente sobre continuar.

## 7. O que pode ser solicitado ou capturado

`PER-002` não deve capturar relato substantivo do Momento Atual como sua responsabilidade principal.

Podem existir apenas dados estritamente necessários ao acesso protegido, quando a autenticação for exigida, sujeitos à autoridade técnica/jurídica aplicável.

```text
DADOS DE ACESSO
→ CATEGORIA SEPARADA

CONTEÚDO DA JOURNEY
→ NÃO É AUTORIZADO POR LOGIN

ACCOUNT CREATION
≠ JOURNEY CONTENT CONSENT
```

Este documento não escolhe método de autenticação e não define:

- e-mail;
- telefone;
- username;
- senha;
- passkey;
- biometria;
- provedor de identidade;
- MFA;
- sessão técnica;
- storage;
- API.

Essas decisões dependem de autoridade técnica e jurídica específica.

## 8. Autenticação

Autenticação é um **gate interno de `PER-002`**, não uma superfície independente por inferência.

A experiência deve suportar dois cenários principais:

### 8.1 Pessoa que precisa autenticar

- compreender o contexto antes de autenticar;
- acessar mecanismo legítimo de entrada/criação/recuperação quando aplicável;
- receber feedback de sucesso, restrição ou falha;
- poder interromper sem ser penalizada;
- continuar somente quando o estado de acesso permitir.

### 8.2 Pessoa com sessão já autenticada

- não deve ser forçada a repetir criação ou autenticação sem necessidade;
- ainda deve encontrar finalidade, contexto e controles necessários;
- deve prosseguir para `PER-003` somente quando `PER-002` estiver funcionalmente pronta.

## 9. Ações e controles

A superfície deve preservar, conforme o estado:

- continuar conscientemente;
- voltar;
- sair por agora;
- interromper;
- recuperar acesso;
- trocar/corrigir caminho de acesso quando aplicável;
- explorar sem personalização quando essa alternativa for compatível;
- retomar estado legítimo quando houver relação existente.

Nenhuma ação de saída pode ser escondida por dark pattern ou hierarquia coercitiva.

## 10. Primeira entrada e relação existente

A Journey não deve obrigar uma Pessoa com relação existente a repetir onboarding de primeira entrada.

```text
NOVA ENTRADA
HOME
→ PER-002
→ PER-003
→ continuidade da Journey

RELAÇÃO EXISTENTE
HOME / ACESSO LEGÍTIMO
→ AUTENTICAÇÃO
→ REVALIDAÇÃO
→ RETOMADA DO ESTADO LEGÍTIMO
```

A retomada deve respeitar o estado canônico vigente e não inferir que tarefas anteriores foram concluídas somente porque a Pessoa já possui conta.

## 11. Falha, restrição e recuperação

Quando a entrada protegida não puder prosseguir, a experiência deve distinguir, quando aplicável:

- credencial inválida;
- sessão expirada;
- acesso indisponível;
- recuperação necessária;
- restrição legítima;
- erro técnico temporário;
- estado não autorizado;
- retomada indisponível.

A mensagem deve explicar o que a Pessoa pode fazer em seguida sem expor informação sensível, existência indevida de conta ou detalhes de segurança.

```text
FALHA
≠ CULPA DA PESSOA
≠ PERDA AUTOMÁTICA DE AUTONOMIA
≠ AUTORIZAÇÃO PARA COLETA ADICIONAL
```

## 12. Privacidade e finalidade

A superfície deve preservar:

- finalidade compreensível;
- minimização;
- separação entre acesso e conteúdo da Journey;
- ausência de consentimento genérico;
- possibilidade de não prosseguir;
- disclosure proporcional;
- proteção de terceiros;
- compatibilidade entre finalidade e dado.

Uma confirmação genérica em `PER-002` não pode autorizar gravação, transcrição, leitura de arquivos, inferência, persistência da compreensão ou personalização futura.

## 13. Processamento

`PER-002` pode preparar a Pessoa para processamento futuro, mas não deve tratar autenticação como autorização de processamento material.

```text
DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

AUTHENTICATED
≠ UNDERSTOOD

GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION
```

O processamento material do conteúdo da Journey pertence às responsabilidades posteriores e às autorizações específicas aplicáveis.

## 14. Conteúdo e linguagem

A linguagem deve:

- ser clara e não alarmista;
- explicar proteção sem prometer segurança absoluta;
- não usar urgência artificial;
- não culpabilizar a Pessoa por sair;
- não sugerir que compartilhar mais é moralmente superior;
- não prometer transformação ou resultado;
- não apresentar autenticação como consentimento amplo;
- deixar claro o próximo passo quando houver ação principal.

Copy final não congelada permanece responsabilidade de Design/Content Design, subordinada a essas invariantes.

## 15. Acessibilidade e inclusão

A solução de Design deve permitir, no mínimo:

- ordem semântica compreensível;
- navegação por teclado quando aplicável;
- foco perceptível;
- labels claros;
- feedback de erro não dependente apenas de cor;
- alternativa a interações dependentes de hover;
- linguagem legível;
- suporte a zoom e responsividade;
- não depender de motion para comunicar estado;
- recuperação de erro sem perda desnecessária de contexto.

## 16. Dados reais e conteúdo sintético

Para prototipação, conteúdo sintético pode demonstrar:

- estado pré-auth;
- sessão simulada;
- recuperação simulada;
- erro simulado;
- controles de saída;
- handoff simulado para `PER-003`.

Não podem ser apresentados como reais:

- conta existente;
- sessão real;
- autenticação real;
- consentimento real;
- dados pessoais reais;
- processamento real;
- persistência real;
- telemetria real.

## 17. Referência visual existente

`GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v1.0.0` é referência interativa local corrente, validada por `GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v2.0.0 = PASS`.

Seu uso é subordinado:

```text
PER-002 INTERACTIVE PROTOTYPE
→ LOCAL DESIGN REFERENCE

LOCAL DESIGN REFERENCE
≠ GLOBAL DESIGN SYSTEM
≠ PUBLIC HOME BASELINE
≠ REQUIRED VISUAL DIRECTION
≠ IMPLEMENTED PRODUCT
```

A designer pode propor solução diferente desde que preserve as autoridades funcionais correntes.

## 18. Liberdade de Design

A designer tem liberdade para decidir:

- quantos frames visuais são necessários;
- composição;
- hierarquia;
- componentes;
- progressão visual;
- uso de modal, página, sheet ou outra solução;
- tipografia;
- paleta;
- iconografia;
- ilustração;
- motion;
- microinterações;
- tratamento responsivo;
- tom visual.

O GKR não exige reprodução do protótipo existente.

## 19. Uso por IA

Se IA for usada para explorar `PER-002`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. `GKR-UX-PER002-MAT-ELIGIBILITY-001`;
5. Registry de superfície e transição;
6. protótipo local somente se a designer desejar consultá-lo como referência subordinada.

A IA não deve receber liberdade para:

- inventar mecanismo de autenticação;
- inventar dados obrigatórios;
- criar consentimento genérico;
- antecipar `PER-003`, `PER-007` ou `PER-008` como se fossem parte de `PER-002`;
- criar novo `PER-ID`;
- converter protótipo local em identidade visual canônica.

## 20. Critérios de aceite funcional

Uma futura solução visual de `PER-002` é funcionalmente aceitável quando:

1. a Pessoa entende que saiu da Home pública;
2. o ambiente protegido é compreensível antes de qualquer captura material da Journey;
3. autenticação aparece somente quando necessária;
4. sessão já autenticada é tratada corretamente;
5. autenticação não é apresentada como autorização de processamento;
6. dados de acesso e conteúdo da Journey permanecem separados;
7. voltar, interromper e não prosseguir permanecem possíveis;
8. recuperação e falha têm caminhos legítimos;
9. não há dark pattern material;
10. a superfície não captura indevidamente o papel de `PER-003..008`;
11. `TRN-002` é o handoff downstream preservado;
12. nenhum dado, conta, sessão ou consentimento fictício é apresentado como real;
13. acessibilidade estrutural foi considerada;
14. a solução pode divergir visualmente da referência local sem romper o contrato funcional.

## 21. Limites

Este Documento Mestre não:

- cria tela final;
- define quantidade canônica de frames;
- define sistema visual;
- cria Figma;
- cria protótipo novo;
- autoriza implementação;
- escolhe provedor de identidade;
- escolhe stack;
- define política jurídica final;
- define analytics;
- define persistência;
- inicia Product Engineering;
- altera `TRN-001` ou `TRN-002`;
- cria `PER-003`.

## 22. Estado corrente

```text
PER-002 MASTER
→ CURRENT DESIGN DEFINITION

FUNCTIONAL BOUNDARY
→ GKR-UX-PER002-MAT-ELIGIBILITY-001 v2.0.0
→ CURRENT / FROZEN

LOCAL INTERACTIVE DESIGN REFERENCE
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v1.0.0

LOCAL PROTOTYPE VALIDATION
→ GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v2.0.0
→ PASS

TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

NEXT DOCUMENT IN CONSTRUCTION SEQUENCE
→ PER-003 — ESCOLHA DE MODALIDADE

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
