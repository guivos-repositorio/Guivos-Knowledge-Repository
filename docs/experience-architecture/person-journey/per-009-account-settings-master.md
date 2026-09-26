---
id: GKR-UX-PER009-MASTER-001
title: Jornada da Pessoa — PER-009 — Conta / Configurações — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-PLANS-PERSON-001
related:
  - GKR-SURF-PER-009
  - GKR-SURF-PER-301
  - GKR-TRN-406
  - GKR-TRN-407
---

# Jornada da Pessoa — PER-009 — Conta / Configurações — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida o **recorte governado corrente** de `PER-009 — Conta / Configurações` para Design, IA opcional, Produto, UX, Privacidade e Engenharia.

`PER-009` representa a responsabilidade administrativa autenticada da Pessoa. O recorte originalmente comprovado para origem/retorno de Planos permanece válido e, pela Autoridade de Completude Funcional, a responsabilidade também passa a localizar os **ciclos administrativos transversais de dados e permissões, exportação, exclusão e saída da Guivos** quando materialmente aplicáveis.

Este Master **não define uma arquitetura total de Conta e Configurações**, não cria um menu universal e não transforma cada controle em nova superfície.

## 2. Escopo comprovado

```text
PESSOA AUTENTICADA
→ PER-009 — CONTA / CONFIGURAÇÕES
→ ESCOLHA ADMINISTRATIVA CONSCIENTE
→ TRN-406
→ PER-301 — PLANOS E COMPARAÇÃO

PER-301
→ TRN-407
→ PER-009
```

No estado corrente:

- `TRN-406` está **contratada**;
- `TRN-407` está **contratada**;
- nenhuma das duas é promovida por este Master;
- a materialização de `PER-009` não comprova implementação técnica nem validação ponta a ponta.

## 3. Job da Pessoa no recorte corrente

A superfície deve permitir que a Pessoa:

1. reconheça que está em contexto administrativo próprio;
2. compreenda que Planos é uma área opcional;
3. escolha abrir Planos de forma consciente;
4. permaneça na Conta sem iniciar efeito comercial;
5. retorne de Planos para a Conta sem alteração automática;
6. compreenda que navegação e contratação são atos distintos.

## 4. Limite estrutural

`PER-009` existe no Registry como responsabilidade necessária à origem e ao retorno voluntários de Planos.

Portanto:

```text
PER-009
= ORIGEM / RETORNO ADMINISTRATIVO GOVERNADO

PER-009
≠ ARQUITETURA COMPLETA DE CONTA
≠ CATÁLOGO INVENTADO DE CONFIGURAÇÕES
≠ CENTRAL DE PRIVACIDADE POR INFERÊNCIA
≠ CENTRAL DE SEGURANÇA POR INFERÊNCIA
≠ PERFIL POR INFERÊNCIA
≠ NOTIFICAÇÕES POR INFERÊNCIA
```

A designer pode compor a superfície, mas não preencher áreas não governadas como se fossem capacidades confirmadas.

## 5. Autenticação

O acesso ao recorte corrente de `PER-009` exige contexto autenticado.

Autenticação:

- permite reconhecer a Pessoa e seu contexto administrativo aplicável;
- não amplia consentimento;
- não seleciona plano;
- não autoriza cobrança;
- não transforma navegação em contratação.

Este Master não define mecanismos técnicos de login, sessão, recuperação de conta, MFA ou segurança de credenciais.

## 6. Entrada

A autoridade corrente não contrata uma única origem universal para `PER-009`.

A experiência pode chegar à Conta por navegação autenticada legitimamente disponível, sem que este Master invente uma nova `TRN`.

Quando a entrada decorrer de retorno de Planos, aplica-se `TRN-407`.

## 7. Planos como continuidade opcional

Planos deve ser compreensível como uma escolha administrativa voluntária.

Abrir Planos:

- não seleciona Free, Plus ou Pro;
- não inicia checkout;
- não cria assinatura;
- não altera entitlement;
- não autoriza pagamento;
- não inicia cobrança;
- não amplia consentimento;
- não registra intenção comercial além da navegação necessária.

## 8. TRN-406 — Conta → Planos

`GKR-TRN-406: PER-009 → PER-301`.

Estado: **contratada**.

A transição representa exclusivamente a navegação voluntária da Conta para Planos.

```text
ABRIR PLANOS
→ NAVEGAÇÃO

ABRIR PLANOS
≠ SELECIONAR PLANO
≠ CONTRATAR
≠ PAGAR
≠ ALTERAR PLANO
```

Este Master fornece materialização documental suficiente para Design de `PER-009`, mas **não promove automaticamente a maturidade de TRN-406**. Validação ponta a ponta exige ato governado próprio.

## 9. TRN-407 — Planos → Conta

`GKR-TRN-407: PER-301 → PER-009`.

Estado: **contratada**.

Retornar à Conta:

- não cancela assinatura;
- não desfaz contratação já concluída;
- não confirma alteração;
- não abandona silenciosamente efeito financeiro já confirmado;
- não cria novo efeito;
- não duplica evento.

O estado comercial vigente deve permanecer governado pelas autoridades de Planos.

## 10. Idempotência e repetição

Repetir navegação entre Conta e Planos não deve, por si só:

- criar cobrança;
- duplicar contratação;
- alterar plano;
- confirmar downgrade;
- cancelar assinatura;
- modificar entitlement;
- ampliar consentimento.

Navegação deve permanecer separada de ação comercial substantiva.

## 11. Conteúdo administrativo mínimo

Dentro do recorte comprovado, a superfície pode apresentar:

- identificação suficiente do contexto administrativo da Pessoa;
- acesso compreensível a Planos;
- estado mínimo necessário para orientar a continuidade quando legitimamente disponível;
- retorno e navegação compatíveis com o contexto.

Nenhum outro grupo de configurações é obrigatório por este Master.

## 12. Controles administrativos transversais da Pessoa

A existência de capacidades comerciais de dados, permissões, correção, exportação, exclusão e saída exige responsabilidade funcional localizável. Elas permanecem em `PER-009` quando forem **administrativas e transversais**, sem substituir controles contextuais pertencentes ao objeto de origem.

### 12.1 Dados e permissões

A Pessoa deve poder compreender e controlar, quando houver autoridade aplicável, dados e permissões administrativas sob sua esfera.

O ciclo deve preservar:

- finalidade e escopo compreensíveis;
- distinção entre dado declarado, observado, inferido e confirmado quando aplicável;
- autoridade da Pessoa e eventuais limites legítimos;
- ação consciente para alteração material;
- processamento, resultado confirmado, falha ou estado indeterminado;
- reversibilidade quando juridicamente e tecnicamente aplicável.

```text
PERMISSÃO
≠ PREFERÊNCIA
≠ CONSENTIMENTO AMPLO
≠ AUTENTICAÇÃO
≠ VÍNCULO
```

Correção permanece contextual quando o objeto possui autoridade própria. `PER-009` não deve copiar ou sobrescrever silenciosamente a fonte oficial.

### 12.2 Exportação

Quando exportação estiver legitimamente disponível, a experiência deve tornar compreensíveis:

- escopo exportado;
- finalidade da ação;
- formato ou abrangência quando material;
- processamento;
- resultado disponível, falha ou indisponibilidade;
- limites conhecidos.

```text
EXPORTAR DADOS
≠ COMPARTILHAR DADOS
≠ AUTORIZAR NOVO TRATAMENTO
```

A existência de níveis comerciais de exportação não autoriza inventar formato, prazo, volume, canal ou conteúdo ainda não governado.

### 12.3 Exclusão

A experiência deve distinguir explicitamente:

```text
EXCLUIR COMPREENSÃO
≠ EXCLUIR DADO
≠ EXCLUIR CONTA
```

Antes de uma exclusão material, a Pessoa deve compreender objeto e consequência aplicáveis. O ciclo mínimo é:

```text
SOLICITAR
→ COMPREENDER ESCOPO E CONSEQUÊNCIA
→ CONFIRMAÇÃO PROPORCIONAL
→ PROCESSAMENTO
→ RESULTADO CONFIRMADO OU FALHA/ESTADO INDETERMINADO
```

Restrições legítimas de retenção, obrigação ou autoridade devem ser explicadas quando aplicáveis; não podem ser inventadas por este Master.

### 12.4 Saída da Guivos

Quando a Pessoa puder encerrar sua relação com a Guivos, o controle deve permanecer semanticamente separado de outros encerramentos:

```text
SAÍDA DA GUIVOS
≠ SAÍDA DE COLETIVO
≠ CANCELAMENTO DE PLANO
≠ EXCLUSÃO AUTOMÁTICA DE TODO DADO
```

A saída exige consequência compreensível, confirmação proporcional, processamento e resultado verificável. Nenhum efeito financeiro, contratual, coletivo ou de retenção pode ser presumido sem autoridade própria.

### 12.5 Processamento, idempotência e recuperação

Para controles materiais:

- intenção não equivale a processamento;
- processamento não equivale a sucesso;
- sucesso exige confirmação;
- estado indeterminado permanece indeterminado;
- retry não duplica efeito;
- falha recuperável oferece continuidade proporcional;
- autenticação não substitui autorização material.

Esses ciclos não criam novo `PER-ID` ou `TRN-ID`.

## 13. Planos e estado comercial

Quando informação de plano atual for exibida em `PER-009`, ela deve:

- vir de autoridade corrente;
- distinguir estado real de proposta;
- não inventar preço, benefício, renovação ou entitlement;
- não substituir `PER-301` como responsabilidade especializada de Planos e Comparação.

A Conta pode orientar a continuidade, mas não deve absorver o fluxo especializado.

## 14. Estados internos de experiência

Sem criar novos `PER-ID`s, Design pode representar estados internos necessários ao recorte, por exemplo:

- carregamento;
- contexto autenticado válido;
- Planos disponível;
- retorno de Planos;
- indisponibilidade temporária;
- erro recuperável;
- estado administrativo sem informação comercial adicional.

Esses estados não autorizam novas capacidades de Conta.

## 15. Erro e recuperação

Falha ao abrir Planos deve preservar a Pessoa em contexto administrativo seguro e compreensível.

A experiência não deve:

- presumir contratação;
- alterar plano por retry;
- duplicar ação comercial;
- ocultar falha como sucesso;
- inventar estado financeiro.

## 16. Privacidade e minimização

`PER-009` deve usar apenas os dados necessários ao contexto administrativo corrente e à continuidade voluntária para Planos.

A existência da superfície não autoriza centralizar ou expor, por inferência:

- dados sensíveis;
- credenciais;
- histórico financeiro detalhado;
- informações de terceiros;
- preferências não contratadas;
- dados de outras responsabilidades sem finalidade.

## 17. Reversibilidade

No recorte atual:

- permanecer na Conta é válido;
- não abrir Planos é válido;
- abrir Planos e retornar é válido;
- retornar não produz consequência comercial por si só.

A reversibilidade de contratação, downgrade, cancelamento e cobrança pertence às autoridades especializadas de `PER-301..304`.

## 18. Linguagem e claims

Evitar linguagem que:

- apresente Planos como obrigatórios;
- confunda navegação com contratação;
- sugira cobrança ao abrir a área;
- invente economia, benefício ou vantagem;
- pressione upgrade;
- trate plano pago como requisito universal de continuidade;
- transforme Conta em catálogo de capacidades não governadas.

## 19. Acessibilidade

O acesso a Planos e o retorno à Conta devem ser compreensíveis sem depender exclusivamente de cor, ícone, posição, animação ou som.

Estado de carregamento, erro, indisponibilidade e continuidade devem ser comunicáveis por tecnologias assistivas.

## 19. Conteúdo sintético

Conteúdo sintético para prototipação é permitido apenas quando claramente fictício e sem criar regra de produto.

Não se pode inventar como real:

- plano atual;
- preço;
- cobrança;
- data de renovação;
- método de pagamento;
- entitlement;
- desconto;
- condição promocional;
- status de contratação.

## 20. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer possui liberdade sobre composição, agrupamento, componentes, densidade, ritmo, iconografia, motion, responsividade e microinterações, preservando:

- escopo administrativo estreito;
- autenticação;
- voluntariedade;
- separação entre navegação e efeito comercial;
- minimização;
- acessibilidade;
- autoridades correntes de marca.

A liberdade visual não autoriza inventar a arquitetura total da Conta.

## 22. Limites para IA

IA não pode:

- criar novas áreas de Conta por plausibilidade;
- inventar configurações de segurança, privacidade, perfil ou notificações;
- inventar plano, preço, cobrança ou entitlement;
- promover `TRN-406/407`;
- criar novo `PER-ID` ou `TRN-ID`;
- transformar Planos em gate obrigatório;
- iniciar efeito financeiro;
- impor baseline visual;
- iniciar Product Engineering.

## 23. Critérios de aceite funcional

O consumo de `PER-009` é aceitável quando:

1. a superfície permanece autenticada;
2. seu escopo é explicitamente administrativo;
3. Planos é continuidade opcional;
4. abrir Planos exige ação consciente;
5. abrir Planos não seleciona plano;
6. abrir Planos não inicia cobrança;
7. abrir Planos não amplia consentimento;
8. `TRN-406` permanece contratada;
9. `TRN-407` permanece contratada;
10. retornar não cancela nem altera plano;
11. repetição de navegação é idempotente quanto a efeitos comerciais;
12. `PER-301` permanece responsabilidade especializada;
13. a arquitetura total de Conta não é inventada;
14. estados internos não criam novos IDs;
15. erro preserva estado seguro;
16. conteúdo sintético não se apresenta como real;
17. privacidade e minimização são preservadas;
18. acessibilidade não depende apenas de sinais visuais;
19. Design mantém liberdade criativa dentro das autoridades;
20. Product Engineering permanece não liberado.

## 24. Lacunas que permanecem abertas

Este Master não resolve:

- arquitetura completa de Conta;
- perfil;
- credenciais;
- autenticação técnica;
- recuperação de conta;
- MFA;
- segurança;
- arquitetura jurídica/operacional completa de direitos e retenção;
- notificações e alertas fora de responsabilidades já governadas;
- preferências gerais sem objeto governado;
- dispositivos/sessões;
- métodos de pagamento;
- histórico financeiro;
- faturamento;
- gateway;
- fiscal;
- proration;
- novas origens de Conta;
- validação ponta a ponta de `TRN-406/407`;
- implementação técnica.

Esses temas exigem autoridades próprias quando forem necessários.

## 25. Estado

```text
PER-009
→ DOCUMENTED IN GOVERNED SCOPE

MASTER
→ GKR-UX-PER009-MASTER-001 v0.1.0
→ CURRENT CANDIDATE

TRN-406
→ CONTRACTED / UNCHANGED

TRN-407
→ CONTRACTED / UNCHANGED

FULL ACCOUNT ARCHITECTURE
→ NOT DEFINED

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-301 — Planos e Comparação`.
