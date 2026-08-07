---
id: UXA-089
title: Validação Funcional e Reformulação da Gestão de Solicitações do Responsável do Coletivo
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-056
  - UXA-059
  - UXA-066
  - UXA-067
  - UXA-086
  - UXA-087
  - UXA-088
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-COL-003
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-108
  - GKR-TRN-109
  - GKR-TRN-112
  - GKR-JOURNEY-GAPS-001
  - M7.76
normative: false
---

# Validação Funcional e Reformulação da Gestão de Solicitações do Responsável do Coletivo

## 1. Finalidade

A UXA-089 valida funcionalmente os sete estados desktop materializados pela UXA-088 para `GKR-SURF-COL-003 — gestão de solicitações` e aplica, no mesmo pacote, somente as reformulações necessárias para que a operação preserve autoridade legítima, minimização de dados, voluntariedade e consequência compreensível.

A família foi examinada como uma operação única:

```text
COL-002 — Visão Geral do Responsável
→ fila de solicitações
→ detalhe comum ou protegido
→ aguardar, pedir informação, aprovar ou recusar
→ resultado correspondente para a Pessoa
```

A UXA-089 valida a superfície e seus sete estados. Ela **não valida os handoffs bilaterais ponta a ponta**, não materializa `PER-106` e não promove a Jornada do Coletivo.

## 2. Autoridades utilizadas

O gate foi realizado contra:

- UXA-014 — fundação funcional de Organizações e Coletivos;
- UXA-056 — descoberta, perfil público, participação e gestão do Coletivo;
- UXA-059 — programa e priorização dos wireframes de Coletivos;
- UXA-066/067 — estados e efeitos já materializados e validados na perspectiva da Pessoa;
- UXA-086/087 — Visão Geral do Responsável materializada e validada;
- UXA-088 — materialização da gestão de solicitações.

Também foram considerados o Registro de Superfícies, o Registro de Transições, a Jornada do Coletivo e o Registro de Lacunas.

## 3. Critérios do gate

A família foi examinada nas seguintes dimensões:

1. entrada protegida e contexto de representação;
2. distinção entre estimativa, prazo e evento temporal;
3. ordenação sem prioridade substantiva automática;
4. dados mínimos e finalidade declarada;
5. critérios previamente apresentados à Pessoa;
6. pedido adicional sem coerção ou inferência sensível;
7. acessibilidade separada de elegibilidade e usada para acomodação;
8. autoridade verificada por escopo, não por autodeclaração;
9. confirmação consciente antes de aprovação ou recusa;
10. recusa proporcional e separada de sanção, reputação e denúncia;
11. estado de autoridade insuficiente sem escalada de permissão;
12. retorno sem decisão e preservação do estado da solicitação;
13. efeito compreensível para a Pessoa;
14. ausência de promessa sobre `PER-106` ou implementação futura.

Falha material em autoridade, dados, coerção ou consequência impede aprovação funcional.

## 4. Diagnóstico da UXA-088

A materialização inicial acertou a estrutura principal:

- fila especializada separada da Visão Geral;
- estados comuns e protegidos distintos;
- consulta sem alteração automática de prioridade;
- dados pessoais limitados à finalidade;
- pedido adicional com pergunta, finalidade, autoridade e prazo;
- aprovação e recusa com confirmação própria;
- recusa separada de reputação e sanção;
- autoridade insuficiente como bloqueio explícito;
- cancelamento pela Pessoa e expiração tratados como eventos, não decisões do responsável;
- inexistência de novos IDs granulares ou transições artificiais.

Entretanto, seis ajustes eram necessários antes da aprovação funcional da família.

## 5. Achados e reformulações

### F01 — “prazo” e “estimativa” estavam misturados na fila

A fila utilizava uma única coluna `Prazo informado` para estados que representam conceitos temporais diferentes: estimativa de decisão, prazo para resposta e outras referências operacionais.

Isso poderia transformar uma estimativa em obrigação ou urgência artificial.

**Correção:** a coluna passa a se chamar `Referência temporal` e cada linha identifica explicitamente `estimativa` ou `resposta até`. A ordenação também declara sua base e informa que não cria prioridade substantiva automática.

### F02 — critérios de decisão não explicitavam que já haviam sido apresentados à Pessoa

O detalhe e a aprovação mencionavam critérios aplicáveis ou públicos, mas não vinculavam claramente a decisão às condições que a Pessoa conheceu antes de solicitar participação.

**Correção:** detalhe, aprovação e recusa passam a referenciar condições previamente apresentadas à Pessoa e ainda vigentes. Critérios ocultos e inferências sensíveis permanecem proibidos.

### F03 — o exemplo de pedido adicional usava acessibilidade dentro da decisão de entrada

A versão inicial perguntava sobre necessidade de recurso de acessibilidade e, ao mesmo tempo, pausava a decisão de participação.

Mesmo com finalidade declarada, essa combinação poderia transformar uma necessidade de acomodação em obstáculo de elegibilidade ou pressionar a Pessoa a revelar informação potencialmente sensível.

**Correção:** o cenário passa a perguntar somente sobre um critério objetivo de participação previamente apresentado. Saúde, diagnóstico e necessidade de acessibilidade ficam explicitamente fora dos dados solicitados para a decisão. A superfície declara que acessibilidade deve ser tratada separadamente para acomodação e nunca como critério oculto de entrada.

### F04 — a confirmação de aprovação podia ser lida como autodeclaração de autoridade

O checkbox original pedia que a pessoa responsável confirmasse que possuía autoridade.

Autoridade não pode surgir de uma confirmação de interface.

**Correção:** a autoridade passa a ser declarada como verificada pelo escopo concedido. O checkbox confirma somente fundamento e consequência; a superfície afirma que marcar a confirmação não cria nem amplia permissão.

### F05 — a confirmação de recusa apresentava o mesmo risco de autodeclaração

A recusa também combinava confirmação do fundamento com declaração de autoridade e utilizava uma referência ambígua a `perfil público`.

**Correção:** a autoridade é tratada como gate previamente verificado; a confirmação começa vazia e cobre somente proporcionalidade, conhecimento prévio da regra e aplicabilidade. A regra é identificada como condição apresentada no Perfil Público do Coletivo.

### F06 — o estado de autoridade insuficiente poderia sugerir gestão da própria permissão

A expressão `revisar suas permissões` poderia ser interpretada como possibilidade de alterar o próprio escopo a partir da experiência operacional.

**Correção:** a superfície passa a oferecer somente consulta do escopo concedido. Encaminhamento continua possível apenas quando existir destinatário legítimo configurado e nunca transfere autoridade ao remetente.

## 6. Artefatos avaliados

| Estado | Resultado |
|---|---|
| fila operacional | reformulada e validada |
| detalhe comum | reformulado e validado |
| análise protegida | validada sem alteração |
| pedido adicional | reformulado e validado |
| confirmação de aprovação | reformulada e validada |
| confirmação de recusa | reformulada e validada |
| autoridade insuficiente | reformulada e validada |

Resultado da família:

- sete SVGs existentes;
- seis SVGs reformulados;
- sete SVGs funcionalmente validados;
- zero novo SVG;
- zero pendência funcional dentro da UXA-088.

## 7. Validação por dimensão

| Dimensão | Resultado | Evidência |
|---|---|---|
| entrada protegida | aprovado | representação e escopo aparecem antes da operação |
| fila e ordenação | aprovado após reformulação | referência temporal tipada e ausência de prioridade automática |
| detalhe comum | aprovado após reformulação | dados autorizados, critérios apresentados e gate de autoridade |
| análise protegida | aprovado | exposição mínima, papel especializado e dados ocultos explícitos |
| pedido adicional | aprovado após reformulação | critério objetivo, voluntariedade e separação de acessibilidade |
| aprovação | aprovado após reformulação | autoridade verificada externamente à confirmação; consequência delimitada |
| recusa | aprovado após reformulação | fundamento proporcional, conhecido e separado de sanção/reputação |
| autoridade insuficiente | aprovado após reformulação | nenhum dado adicional, nenhuma escalada de permissão e encaminhamento legítimo |
| retorno sem decisão | aprovado | fila, detalhe e estados de decisão permitem retorno sem consequência |
| dados e finalidade | aprovado | Jornada, outros Coletivos, contatos e dados sensíveis desnecessários permanecem fora |
| efeito para a Pessoa | aprovado no escopo da superfície | os resultados correspondem aos estados já representados em UXA-066/067 |
| continuidade bilateral | não validada por desenho | requer pacote integrado específico |
| continuidade para PER-106 | ausente | `GKR-SURF-PER-106` ainda não materializada |

## 8. Pedido adicional e voluntariedade

O pedido adicional é aprovado porque:

- pergunta e finalidade são verificáveis;
- somente critério previamente apresentado pode sustentar decisão;
- `prefiro não responder` não é recusa voluntária;
- a análise posterior utiliza somente a base legitimamente disponível;
- saúde, diagnóstico e acessibilidade não são pedidos como condição oculta;
- acessibilidade permanece uma responsabilidade de acomodação, não um mecanismo de exclusão;
- envio do pedido não cria vínculo nem garante resultado.

## 9. Aprovação e recusa

### 9.1 Aprovação

A aprovação é válida porque:

- autoridade é verificada antes da confirmação;
- fundamento usa critérios previamente apresentados;
- o checkbox não cria permissão;
- o vínculo não cria função, moderação, reputação, presença obrigatória ou notificação automática;
- o resultado é compreensível na perspectiva da Pessoa;
- `PER-106` continua explicitamente futuro.

### 9.2 Recusa

A recusa é válida porque:

- fundamento é proporcional e pertinente;
- condição utilizada foi apresentada antes da solicitação;
- nenhuma inferência sensível ou dado externo é autorizado;
- recusa não é sanção, reputação, denúncia ou bloqueio universal;
- revisão formal não é prometida sem regra, prazo e autoridade próprios;
- a confirmação não autoatribui autoridade.

## 10. Autoridade insuficiente

O estado é validado porque:

- identifica a ação indisponível;
- explica o escopo necessário e o escopo atual;
- não libera dados adicionais;
- não oferece autoelevação de permissão;
- permite retorno seguro;
- permite somente consultar o escopo concedido;
- encaminhamento depende de destinatário legítimo configurado;
- a solicitação permanece inalterada.

## 11. Handoffs bilaterais

A UXA-089 **não promove** `GKR-TRN-105` a `GKR-TRN-109` nem `GKR-TRN-112` para validadas ponta a ponta.

Após esta frente:

```text
PER-105 — validada em UXA-067
↔ TRN-105/106/107/109 — continuam parciais
↔ COL-003 — validada em UXA-089

COL-002 — validada em UXA-087
→ TRN-112 — continua parcial
→ COL-003 — validada em UXA-089

COL-003 — validada
→ TRN-108 — continua parcial
→ PER-106 — ausente
```

A existência de endpoints validados não substitui a inspeção da ligação como conjunto.

## 12. Veredito

**Aprovada após reformulação controlada no escopo da superfície.**

`GKR-SURF-COL-003 — gestão de solicitações` pode passar de `materializado; validação pendente` para **validado** como família funcional desktop de baixa fidelidade.

O veredito não aprova:

- `GKR-TRN-105` a `GKR-TRN-109` ponta a ponta;
- `GKR-TRN-112` ponta a ponta;
- `GKR-SURF-PER-106`;
- gestão de participantes (`COL-004`);
- comunicação especializada (`COL-005`);
- moderação completa;
- responsividade móvel;
- jornada integrada do Coletivo como completa.

## 13. Efeito quantitativo

Após eventual integração da UXA-089:

| Indicador | Antes | Depois |
|---|---:|---:|
| SVGs existentes | 105 | 105 |
| associações individuais | 105 | 105 |
| perfis de rastreabilidade | 25 | 25 |
| validações funcionais registradas | 88 | 95 |
| pendentes de validação específica | 17 | 10 |
| IDs com referência visual | 27 de 40 | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 | 12 |
| superfícies registradas | 40 | 40 |
| transições registradas | 37 | 37 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

## 14. Limites

A UXA-089 não:

- cria novo SVG;
- cria novo ID de superfície ou transição;
- valida handoff bilateral como conjunto;
- materializa `PER-106`, `PER-107` ou `PER-108`;
- materializa `COL-004` a `COL-008`;
- promove a Jornada do Coletivo;
- cria protótipo navegável;
- executa teste com pessoas;
- define política jurídica, API ou esquema de dados;
- altera Resultados Empresariais;
- inicia Engenharia de Produto.

## 15. Próxima transição possível

Após integração e autorização separada, a próxima frente recomendada é:

> **UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos.**

A UXA-090 deverá examinar `GKR-TRN-105`, `106`, `107`, `109` e `112` como ligações entre superfícies já validadas, preservando `GKR-TRN-108` como parcial enquanto `GKR-SURF-PER-106` permanecer ausente.

A UXA-090 não é iniciada por esta validação.
