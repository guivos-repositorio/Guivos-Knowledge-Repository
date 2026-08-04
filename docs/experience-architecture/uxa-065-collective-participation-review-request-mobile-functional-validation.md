---
id: UXA-065
title: Validação Funcional e Reformulação da Revisão e Solicitação de Participação Móvel em Coletivos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-062
  - UXA-063
  - UXA-064
related:
  - UXA-066
  - M7.67
normative: false
---

# Validação Funcional e Reformulação da Revisão e Solicitação de Participação Móvel em Coletivos

## 1. Finalidade

Este documento valida funcionalmente os cinco wireframes móveis materializados pela UXA-064 e registra as reformulações necessárias antes de qualquer materialização da Solicitação Pendente.

A família foi examinada como um percurso único:

```text
Perfil Público
→ revisão consciente
→ confirmação de entrada aberta ou envio para análise
→ confirmação imediata ou comprovante transitório
→ retorno seguro
→ futura Solicitação Pendente, mediante autorização separada
```

A UXA-065 não cria novos SVGs, protótipo, teste com pessoas, política jurídica ou implementação.

## 2. Artefatos avaliados

| Artefato | Estado anterior | Resultado |
|---|---|---|
| revisão de entrada aberta | materializado; pendente | reformulado e validado |
| entrada aberta confirmada | materializado; pendente | reformulado e validado |
| revisão mediante aprovação | materializado; pendente | reformulado e validado |
| comprovante de envio | materializado; pendente | reformulado e validado |
| revisão protegida de convite | materializado; pendente | reformulado e validado |

Resultado da família:

- cinco SVGs materializados;
- cinco SVGs reformulados;
- cinco SVGs funcionalmente validados;
- zero novo SVG;
- zero pendência funcional dentro desta família.

## 3. Critérios aplicados

A revisão verificou:

1. significado do vínculo antes da ação;
2. diferença entre entrada aberta, aprovação e convite;
3. dados enviados e dados protegidos;
4. permissões separadas da participação;
5. confirmações vazias e não coercitivas;
6. cancelamento visível antes do envio;
7. autoridade e prazo sem promessa indevida;
8. entrada confirmada sem função automática;
9. comprovante separado de Solicitação Pendente;
10. convite protegido sem exposição indevida;
11. marketing, notificações e contato privado separados;
12. continuidade sem antecipar superfícies futuras;
13. acessibilidade sem virar condição de entrada;
14. alegações protegidas sem aparência de fato verificado.

## 4. Achados e reformulações

### 4.1 Visibilidade aparentemente escolhida

A revisão de entrada aberta informava `visibilidade escolhida`, mas não oferecia escolha materializada.

Reformulação:

- estado inicial definido como `não aparecer na lista nominal`;
- o dado enviado passa a registrar essa preferência inicial;
- mudança posterior permanece em controle próprio;
- nenhuma visibilidade pública é inferida pelo silêncio.

Decisão validada:

> ausência de escolha explícita não poderá ser apresentada como preferência escolhida.

### 4.2 Confirmação sem superfície inexistente

A confirmação de entrada aberta oferecia `Revisar minha participação` e um comprovante não materializado.

Reformulação:

- ação secundária alterada para `Voltar ao Perfil Público`;
- identificador do registro aparece na própria confirmação;
- `Salvar confirmação` não cria nova superfície;
- o acesso ao ambiente interno existente permanece como ação principal.

### 4.3 Pausa e saída sem promessa absoluta

A confirmação afirmava pausa e saída sem penalidade reputacional, antecipando política futura.

Reformulação:

- pausa e saída exigirão revisão de consequências antes da confirmação;
- a UXA-065 não define política final de reputação, sanção ou encerramento;
- mudança material de regra continua exigindo nova revisão consciente.

### 4.4 Cancelamento antes e depois do envio

A revisão mediante aprovação poderia misturar cancelamento atual e cancelamento futuro.

Reformulação:

- `Cancelar agora` é explicitado como ação sem envio de dados;
- cancelamento posterior permanece reservado à futura Solicitação Pendente;
- prazo estimado permanece distinto de promessa;
- silêncio e espera permanecem distintos de aprovação.

### 4.5 Acessibilidade fora da confirmação obrigatória

Acessibilidade aparecia dentro de uma confirmação obrigatória junto a regras e segurança.

Reformulação:

- a confirmação obrigatória cobre regras essenciais e segurança;
- `solicitar recurso de acessibilidade` passa a caminho separado;
- necessidade de acessibilidade não é tratada como obrigação de concordância.

### 4.6 Redação de envio sem base jurídica presumida

As revisões utilizavam `Autorizo somente o envio`, embora a base jurídica de produção não esteja definida.

Reformulação:

- redação alterada para `Confirmo que desejo enviar`;
- a ação continua consciente e condicionada;
- política jurídica, retenção e tecnologia de consentimento permanecem posteriores.

### 4.7 Comprovante sem navegação fictícia

O comprovante oferecia `Acompanhar em Solicitações`, antecipando uma superfície ainda não criada.

Reformulação:

- o acompanhamento contínuo aparece como ainda não materializado;
- a futura Solicitação Pendente é identificada como pacote separado;
- `Voltar ao Perfil Público` torna-se a ação principal;
- `Salvar comprovante` preserva o registro sem criar acompanhamento.

Decisão validada:

> comprovante transitório não poderá simular disponibilidade da superfície contínua.

### 4.8 Eventos futuros sem garantia operacional

O comprovante afirmava que cada evento teria fundamento, autoridade e consequência identificados.

Reformulação:

- a regra passa a `deverá identificar`;
- a formulação governa o futuro sem declarar implementação existente;
- informação adicional, decisão e cancelamento continuam não materializados.

### 4.9 Alegação do convite protegida

O convite apresentava vínculo comunitário prévio como condição declarada sem distinguir a origem da afirmação.

Reformulação:

- o dado passa a `alegação do remetente, não verificada`;
- a pessoa poderá revisar ou contestar antes do envio;
- a alegação não comprova elegibilidade;
- somente dados mínimos revisados seguem para análise.

### 4.10 Confidencialidade proporcional

O convite podia sugerir proteção absoluta.

Reformulação:

- confidencialidade depende das condições apresentadas;
- não é declarada garantia absoluta;
- recusa ou denúncia não cria penalidade automática nem exposição pública;
- contato privado e compartilhamento externo permanecem bloqueados.

## 5. Resultado por estado

### 5.1 Revisão de entrada aberta

Validada porque:

- vínculo e consequência aparecem antes da ação;
- visibilidade inicial é explícita;
- dados enviados e protegidos são distinguíveis;
- notificações, contato e marketing permanecem separados;
- confirmações começam vazias;
- cancelamento não envia dados.

### 5.2 Entrada aberta confirmada

Validada porque:

- vínculo ativo e ausência de papel automático estão claros;
- visibilidade e comunicação preservam o estado confirmado;
- nenhuma gestão futura é simulada;
- registro e retorno permanecem disponíveis;
- abertura do Coletivo não altera escolhas.

### 5.3 Revisão mediante aprovação

Validada porque:

- envio não cria vínculo;
- dados declarados podem ser editados;
- autoridade e prazo estão identificados sem promessa;
- cancelamento atual e futuro estão separados;
- acessibilidade permanece recurso próprio;
- Organização apoiadora não recebe dados automaticamente.

### 5.4 Comprovante transitório

Validado porque:

- comprova envio sem criar participação;
- mantém responsável, estimativa e identificador;
- não funciona como Solicitação Pendente;
- eventos futuros são apresentados como possibilidades governadas;
- retorno e salvamento não antecipam gestão contínua.

### 5.5 Revisão protegida de convite

Validada porque:

- remetente, autoridade, motivo e validade estão visíveis;
- alegação não verificada é identificada;
- contestação anterior ao envio é possível;
- confidencialidade não é apresentada como garantia absoluta;
- envio de dados mínimos não ativa participação;
- recusa e denúncia permanecem independentes.

## 6. Continuidade validada

### 6.1 Entrada aberta

```text
Perfil Público
→ Revisar participação
→ Confirmar participação
→ Participação confirmada
→ Abrir Coletivo ou voltar ao Perfil Público
```

### 6.2 Aprovação

```text
Perfil Público
→ Revisar solicitação
→ Enviar solicitação
→ Comprovante transitório
→ voltar ao Perfil Público
→ futura Solicitação Pendente
```

### 6.3 Convite protegido

```text
convite autorizado
→ Revisar convite protegido
→ revisar ou contestar alegação
→ recusar, denunciar ou enviar dados mínimos
→ análise especializada futura
```

## 7. Cobertura após validação

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Coletivos — revisão e solicitação | 5 | 5 | 0 |
| Opportunity Boost | 46 | 36 | 10 |

## 8. Decisões preservadas

Continuam vigentes:

- acompanhar não é participar;
- solicitação não é aprovação;
- convite não cria vínculo;
- silêncio não é confirmação;
- apoio institucional não concede autoridade ou dados;
- canal público não concede contato privado;
- marketing não é ativado pela participação;
- proteção não é irregularidade;
- comprovante não é estado contínuo;
- acessibilidade não é condição de elegibilidade;
- alegação não verificada não é fato comprovado.

## 9. Limites

Não são iniciados:

- Solicitação Pendente;
- informação adicional, recusa ou expiração;
- contestação ou cancelamento após envio;
- gestão de solicitações;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- gestão do responsável;
- política jurídica;
- protótipo, teste, identidade visual ou implementação.

## 10. Critérios de saída

A família está funcionalmente validada porque:

- os cinco estados possuem decisão principal coerente;
- nenhuma escolha é inferida sem controle;
- dados e consequências aparecem antes da ação;
- autoridade é identificada sem promessa;
- nenhuma superfície inexistente é apresentada como disponível;
- proteção e acessibilidade permanecem proporcionais;
- o próximo pacote poderá receber contexto sem reinterpretar os estados anteriores.

## 11. Próxima transição recomendada

**UXA-066 — Wireframes Móveis da Solicitação Pendente em Coletivos.**

O pacote deverá materializar acompanhamento contínuo, prazo, autoridade, cancelamento, informação adicional, decisão e continuidade sem reutilizar o comprovante como tela de gestão.

A UXA-066 não é iniciada por esta validação e depende de autorização separada.
