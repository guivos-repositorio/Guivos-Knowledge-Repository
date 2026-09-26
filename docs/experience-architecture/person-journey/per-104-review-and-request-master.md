---
id: GKR-UX-PER104-MASTER-001
title: Jornada da Pessoa — PER-104 — Revisão e Solicitação — Documento Mestre de Superfície
version: 0.1.0
status: active
maturity: current_surface_design_definition
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
depends_on:
  - UXA-056
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-PER103-MASTER-001
  - GKR-SURF-PER-105
  - GKR-TRN-103
  - GKR-TRN-104
normative: true
---

# Jornada da Pessoa — PER-104 — Revisão e Solicitação — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-104 — Revisão e Solicitação` para designer humana, IA opcional, Produto, UX, Research, Privacidade e Engenharia.

A superfície existe para que a Pessoa **revise conscientemente o significado do vínculo que pretende iniciar, os dados e permissões necessários, as regras e consequências aplicáveis e, somente então, confirme ou abandone o ato**.

`PER-104` não é a solicitação pendente, não é a análise do responsável e não é prova de participação.

## 2. Papel na Jornada

```text
PER-103 — PERFIL PÚBLICO DO COLETIVO
→ DECIDIR CONSCIENTEMENTE INICIAR PARTICIPAÇÃO
→ TRN-103 / PARTIAL
→ PER-104 — REVISÃO E SOLICITAÇÃO
→ REVISAR / EDITAR / CANCELAR / CONFIRMAR

QUANDO HOUVER SOLICITAÇÃO SUJEITA A ANÁLISE
→ TRN-104 / PARTIAL
→ PER-105 — SOLICITAÇÃO PENDENTE
```

Abrir `PER-104` não envia solicitação e não cria participação.

## 3. Trabalho da Pessoa

A superfície deve permitir que a Pessoa:

1. reconheça qual Coletivo está prestes a solicitar entrada ou ingressar;
2. compreenda o modelo de entrada aplicável;
3. revise o significado do vínculo que pretende criar;
4. revise regras essenciais e consequências materiais;
5. compreenda critérios legítimos aplicáveis, quando existirem;
6. revise somente informações necessárias à finalidade;
7. compreenda permissões efetivamente necessárias;
8. saiba quem analisará a solicitação quando houver aprovação;
9. compreenda prazo estimado como estimativa, nunca garantia;
10. identifique o que acontecerá após a confirmação;
11. edite informações revisáveis antes do efeito;
12. volte ou cancele antes da confirmação;
13. confirme de forma explícita e não pré-selecionada.

## 4. Origem e contexto recebido

A entrada corrente é `TRN-103`, proveniente de `PER-103`.

Pode ser preservado somente o contexto necessário para revisão, incluindo:

- identificador lógico do Coletivo;
- identidade pública necessária do Coletivo;
- modelo de entrada declarado;
- regras e critérios materiais aplicáveis;
- informações já fornecidas legitimamente e necessárias ao ato;
- contexto mínimo necessário para retorno.

O handoff não autoriza transferência indiscriminada de histórico de busca, interesses inferidos, contexto sensível da Journey ou dados sem finalidade.

`TRN-103` permanece `partial`.

## 5. Modelo de entrada

A superfície deve tornar compreensível qual modelo governa o ato.

### 5.1 Entrada aberta

Quando a autoridade aplicável determinar entrada aberta, a confirmação consciente pode ativar o vínculo **somente quando todos os requisitos legítimos estiverem atendidos**.

Este Master não inventa destino de superfície ou transição ponta a ponta que não esteja contratada no Transition Registry.

### 5.2 Entrada mediante aprovação

Quando a entrada exigir aprovação, a Pessoa deve compreender antes do envio:

- critérios legítimos;
- informações necessárias;
- prazo estimado sem garantia;
- quem analisa;
- possibilidade de cancelar;
- que o envio não equivale a aprovação;
- que o vínculo ainda não existe.

A confirmação produz solicitação, não aprovação.

### 5.3 Entrada por convite

Convite não cria participação automática. Quando o contexto aplicável vier de convite, a Pessoa continua com autoridade para aceitar, recusar, ignorar ou denunciar conforme o contrato correspondente.

Este Master não inventa handoff de convite ausente do Registry.

## 6. Conteúdo que precisa ser compreendido

Antes de qualquer confirmação material, a superfície deve tornar revisáveis e compreensíveis, conforme aplicável:

- Coletivo de destino;
- propósito suficiente para contextualizar o vínculo;
- modelo de entrada;
- regras essenciais;
- consequências materiais da confirmação;
- critérios legítimos;
- dados necessários;
- permissões necessárias;
- responsável ou papel autorizado que analisará, quando aplicável;
- prazo estimado, quando existir;
- condição posterior esperada sem promessa de resultado.

A superfície não precisa repetir integralmente o Perfil Público. Deve preservar o contexto necessário para uma decisão consciente.

## 7. Dados e captura

A captura deve obedecer minimização e finalidade.

Pode solicitar apenas informação necessária ao modelo de entrada e à análise legitimamente contratada.

Não pode exigir, inferir ou reutilizar silenciosamente:

- dados sensíveis sem autoridade e necessidade legítimas;
- histórico de busca;
- contexto privado da Journey;
- localização precisa quando não necessária;
- preferências inferidas;
- dados de outros vínculos;
- informações destinadas a finalidade diferente.

Campos adicionais não podem existir apenas porque podem ser úteis futuramente.

## 8. Permissões e consentimento

Permissões devem ser específicas, compreensíveis e proporcionais.

```text
ABRIR PER-104
≠ CONSENTIR

REVISAR
≠ CONSENTIR

PREENCHER
≠ ENVIAR

CONFIRMAR
→ ATO EXPLÍCITO APLICÁVEL
```

Nenhuma confirmação ou consentimento começa selecionado.

Uma autorização não pode ser ampliada silenciosamente para outras finalidades, outros Coletivos ou outras partes do ecossistema.

## 9. Regras materiais e alteração posterior

Regras essenciais devem estar disponíveis antes da confirmação.

Se uma regra material for alterada depois de uma solicitação e antes da ativação do vínculo, a autoridade `UXA-056` exige **nova revisão antes da ativação**.

A interface não pode tratar silêncio, permanência na tela ou uso anterior como aceite de regra material alterada.

## 10. Critérios e análise

Critérios devem ser legítimos, pertinentes e compreensíveis na medida necessária para a Pessoa decidir.

Quando houver análise:

- deve ficar claro que existe análise;
- deve ficar claro quem ou qual papel autorizado analisa;
- não pode haver promessa de aprovação;
- prazo estimado não pode ser apresentado como SLA garantido sem autoridade;
- envio não pode ser apresentado como participação;
- a Pessoa não deve receber pontuação implícita de mérito como consequência deste fluxo.

## 11. Ações

A superfície pode oferecer, conforme aplicável:

- revisar;
- editar;
- voltar;
- cancelar;
- confirmar entrada;
- enviar solicitação.

As ações precisam preservar semântica distinta.

```text
VOLTAR
≠ CANCELAR UMA SOLICITAÇÃO JÁ ENVIADA

CANCELAR ANTES DO ENVIO
≠ RECUSA DO COLETIVO

CONFIRMAR
≠ APROVAÇÃO

ENVIAR SOLICITAÇÃO
≠ PARTICIPAÇÃO
```

## 12. Confirmação

A confirmação é um ato afirmativo.

Ela deve:

- ocorrer somente após revisão suficiente;
- identificar o efeito que será produzido;
- não estar pré-selecionada;
- não ser disparada por navegação passiva;
- evitar ambiguidade entre salvar rascunho, enviar solicitação e ativar vínculo;
- impedir que repetição involuntária da mesma intenção seja apresentada como múltiplas solicitações.

O mecanismo técnico de idempotência permanece fora deste contrato.

## 13. Continuidade para PER-105

Para o modelo de entrada mediante aprovação, a continuidade documental corrente é:

```text
PER-104 — REVISÃO E SOLICITAÇÃO
→ CONFIRMAÇÃO EXPLÍCITA
→ SOLICITAÇÃO AUTORIZADA ENVIADA
→ TRN-104 / PARTIAL
→ PER-105 — SOLICITAÇÃO PENDENTE
```

`TRN-104` permanece `partial`.

A criação deste Master não promove maturidade da transição.

## 14. Retorno, edição e abandono

Antes do efeito material, a Pessoa deve poder retornar, editar o que for legitimamente editável ou abandonar o ato.

Abandono antes do envio:

- não cria solicitação;
- não cria vínculo;
- não compartilha identidade com o responsável apenas por ter iniciado revisão;
- não deve ser interpretado como recusa institucional;
- não deve gerar pressão para concluir.

Depois do envio, cancelamento pertence ao ciclo da solicitação e às autoridades correspondentes, não a um simples estado pré-envio de `PER-104`.

## 15. Privacidade

A superfície não pode:

- compartilhar a identidade da Pessoa com o Coletivo antes do ato que legitimamente exige esse compartilhamento;
- revelar contexto de descoberta além do necessário;
- presumir vínculo religioso, político, profissional, esportivo, terapêutico, comunitário ou sensível;
- converter intenção de solicitar em perfil sensível;
- expandir consentimento;
- capturar dados sem finalidade;
- tornar dados opcionais obrigatórios por desenho;
- ocultar consequência material de uma permissão.

## 16. Estados internos

Estados de `PER-104` podem incluir, conforme aplicável:

- revisão inicial;
- edição de informação necessária;
- regra ou permissão em revisão;
- validação de informação;
- pronto para confirmar;
- confirmação em processamento;
- erro recuperável antes do efeito;
- alteração material que exige nova revisão;
- abandono antes do envio.

Esses estados pertencem à mesma superfície e **não criam novo `PER-ID`**.

## 17. Processamento visível

Quando a confirmação estiver sendo processada:

- não apresentar efeito como concluído antes de confirmação legítima;
- evitar repetição involuntária;
- preservar possibilidade de recuperação quando o resultado estiver incerto;
- não fabricar solicitação, aprovação ou vínculo;
- não converter demora em recusa.

## 18. Erro e recuperação

Em erro recuperável:

- preservar dados legitimamente fornecidos quando seguro e apropriado;
- explicar que o efeito pode não ter sido concluído;
- permitir tentativa consciente quando aplicável;
- não duplicar solicitação;
- não afirmar aprovação, recusa ou participação sem autoridade;
- não ampliar permissões para recuperar o fluxo.

Quando o estado material do envio for incerto, a experiência deve favorecer revalidação antes de repetir o efeito.

## 19. Linguagem

Evitar linguagem que:

- prometa aprovação;
- trate solicitação como participação;
- pressione a Pessoa a concluir;
- transforme prazo estimado em garantia;
- esconda quem analisará;
- normalize coleta excessiva;
- apresente consentimento como condição genérica para tudo;
- trate regras como irrelevantes ou inevitáveis;
- presuma pertencimento antes do vínculo.

## 20. Acessibilidade

Informações essenciais, regras, permissões, erros, consequências e ação de confirmação devem ser compreensíveis sem depender exclusivamente de:

- cor;
- posição;
- ícone;
- imagem;
- motion;
- hover.

A ordem de leitura e foco deve preservar a compreensão do ato antes da confirmação.

## 21. Dados reais e sintéticos

Nenhum Coletivo, responsável, critério, prazo, regra, permissão, dado pessoal ou resultado pode ser inventado e apresentado como real.

Dados sintéticos podem ser usados em exploração de Design somente quando inequivocamente fictícios.

## 22. Liberdade de Design

Não existe baseline visual obrigatório para `PER-104`.

A designer possui liberdade sobre composição, agrupamento, densidade, componentes, ritmo, mídia, interação e responsividade, preservando:

- semântica do ato;
- clareza das consequências;
- distinção entre revisão, envio e vínculo;
- privacidade e minimização;
- acessibilidade;
- authorities de marca vigentes, incluindo a tipografia oficial quando aplicável.

O Master governa **o que a superfície precisa significar e permitir**, não sua forma visual final.

## 23. Limites para IA

IA pode apoiar exploração e documentação, mas não pode:

- inventar critérios, regras, permissões ou responsáveis;
- inventar dados pessoais ou preencher dados ausentes como fatos;
- marcar confirmação ou consentimento por padrão;
- enviar solicitação;
- criar vínculo;
- prometer aprovação;
- transformar prazo estimado em garantia;
- ampliar consentimento;
- reutilizar contexto sensível sem autoridade;
- criar novo `PER-ID`;
- promover `TRN-103` ou `TRN-104`;
- inventar continuidade de entrada aberta ou convite;
- impor baseline visual;
- iniciar Product Engineering.

## 24. Critérios de aceite

`PER-104` está documentalmente pronto para consumo de Design quando:

1. o Coletivo de destino é reconhecível;
2. o modelo de entrada aplicável é compreensível;
3. o significado do vínculo é revisável antes do efeito;
4. regras essenciais e consequências materiais são compreensíveis;
5. critérios legítimos são apresentados quando aplicáveis;
6. somente dados necessários são solicitados;
7. permissões são específicas e proporcionais;
8. nenhuma confirmação começa selecionada;
9. quem analisa é compreensível quando houver aprovação;
10. prazo estimado não é apresentado como garantia;
11. envio não é confundido com aprovação;
12. solicitação não é confundida com participação;
13. a Pessoa pode editar, voltar ou abandonar antes do efeito;
14. confirmação é afirmativa e semanticamente inequívoca;
15. alteração material posterior exige nova revisão antes da ativação;
16. privacidade e minimização são preservadas;
17. erros não fabricam resultado;
18. repetição involuntária não deve produzir múltiplos pedidos lógicos;
19. `TRN-103` permanece partial;
20. `TRN-104` permanece partial;
21. estados internos não criam nova superfície;
22. acessibilidade não depende de pistas exclusivamente visuais;
23. dados sintéticos não se passam por reais;
24. liberdade criativa da designer é preservada;
25. IA não recebe autoridade de produto;
26. Product Engineering permanece não liberado.

## 25. Gaps preservados

Permanecem fora deste Master:

- promoção de `TRN-103` ou `TRN-104`;
- definição técnica de idempotência;
- continuidade ponta a ponta de entrada aberta quando não registrada;
- continuidade ponta a ponta de convite quando não registrada;
- implementação de backend;
- política detalhada de decisão do responsável;
- `PER-105` e seus estados pós-envio;
- Product Engineering.

## 26. Estado de liberação

```text
PER-104 MASTER
→ CURRENT SURFACE DESIGN DEFINITION

DESIGN
→ RELEASED FOR DOCUMENTARY CONSUMPTION

AI
→ OPTIONAL / DESIGNER-CONTROLLED

TRN-103
→ PARTIAL / UNCHANGED

TRN-104
→ PARTIAL / UNCHANGED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-105 — Solicitação Pendente`.
