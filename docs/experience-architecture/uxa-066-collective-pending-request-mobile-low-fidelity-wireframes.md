---
id: UXA-066
title: Wireframes Móveis da Solicitação Pendente em Coletivos
status: draft
version: 0.2.0
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
  - UXA-064
  - UXA-065
related:
  - UXA-067
  - UXA-068
  - M7.69
normative: false
---

# Wireframes Móveis da Solicitação Pendente em Coletivos

## 1. Finalidade

Este documento materializa a quinta referência P0A do programa UXA-059: a Solicitação Pendente móvel da Pessoa.

A família transforma o comprovante transitório da UXA-064 em acompanhamento contínuo governado, sem reutilizar o comprovante como tela de gestão.

A UXA-067 reformulou e validou funcionalmente os oito SVGs desta família.

A experiência permite responder:

> **Qual é o estado real da minha solicitação, quem possui autoridade para agir, qual estimativa foi informada, quais dados estão vinculados ao processo, o que exige uma decisão minha e qual consequência cada evento produz?**

A UXA-066 não cria protótipo, identidade visual, política jurídica, API, esquema de dados, automação de decisão ou implementação.

## 2. Continuidade validada

```text
Perfil Público
→ revisão e envio
→ comprovante transitório
→ Solicitação Pendente
→ aguardar decisão ou escolher como responder a um pedido adicional
→ cancelar, ser aprovada, recusada ou expirar
→ retornar ao Perfil Público ou abrir o Coletivo
```

O acesso futuro por `Meus Coletivos` permanece reservado. Esta família não apresenta essa superfície como disponível.

## 3. Inventário validado

| Estado | Arquivo | Decisão principal |
|---|---|---|
| aguardando decisão | `uxa-066-collective-pending-request-awaiting-decision-mobile.svg` | verificar atualização ou cancelar conscientemente |
| análise protegida | `uxa-066-collective-pending-request-protected-analysis-mobile.svg` | verificar atualização protegida, cancelar solicitação ou denunciar |
| informação adicional solicitada | `uxa-066-collective-pending-request-additional-information-required-mobile.svg` | responder, preferir não informar, contestar ou cancelar |
| revisão da resposta | `uxa-066-collective-pending-request-additional-information-review-mobile.svg` | revisar e confirmar conteúdo ou preferência antes do envio |
| cancelada | `uxa-066-collective-pending-request-cancelled-mobile.svg` | compreender consequência e retornar ao perfil |
| aprovada | `uxa-066-collective-pending-request-approved-mobile.svg` | abrir o Coletivo sem alterar escolhas |
| recusada | `uxa-066-collective-pending-request-refused-mobile.svg` | compreender fundamento, proteção e limites de revisão |
| expirada | `uxa-066-collective-pending-request-expired-mobile.svg` | compreender regra temporal e recomeço condicionado |

## 4. Resultado da UXA-067

Os oito SVGs foram reformulados e validados.

Foram consolidados:

- verificação de estado sem alteração de fila ou prioridade;
- estimativa distinta de promessa;
- correção material sem edição silenciosa durante análise;
- autoridade protegida limitada ao processo;
- remetente separado de quem analisa e decide;
- pedido adicional sem obrigação de revelar informação;
- resposta, preferência, contestação e cancelamento como caminhos distintos;
- decisão pausada separada de processamento ativo;
- descarte do rascunho separado do cancelamento da solicitação;
- envio adicional com consequência compreensível;
- tratamento posterior governado sem garantia técnica ou jurídica absoluta;
- aprovação sem função, autoridade, presença ou notificação automática;
- recusa separada de sanção, reputação e denúncia;
- expiração separada de recusa e consentimento;
- recomeço condicionado à disponibilidade vigente;
- ausência de navegação para superfícies futuras.

## 5. Estado aguardando decisão

O estado principal apresenta:

- recebimento e última atualização;
- responsável autorizado;
- estimativa e data correspondente sem garantia;
- dados vinculados à análise;
- próximos eventos possíveis;
- ação de verificação que não altera fila;
- cancelamento com confirmação própria;
- orientação para cancelar e revisar novo pedido quando houver dado material incorreto.

Atraso não é recusa. Silêncio não é aprovação.

## 6. Análise protegida

O estado protegido preserva:

- nome reduzido do Coletivo;
- identificador protegido;
- remetente separado da equipe de análise;
- autoridade especializada limitada ao processo;
- alegação do remetente identificada como não verificada;
- dados mínimos;
- localização, Jornada, contatos e outros vínculos ocultos;
- verificação, cancelamento e denúncia como ações distintas.

Cancelar ou denunciar não cria exposição pública automática.

## 7. Informação adicional

### 7.1 Pedido recebido

A tela informa:

- pergunta exata;
- finalidade declarada;
- autoridade solicitante;
- formato de resposta aceito;
- prazo e regra de eventual expiração;
- dados não incluídos;
- efeito da pausa sobre a decisão;
- opção de responder, preferir não informar, contestar ou cancelar.

O pedido exige decisão da Pessoa, não revelação obrigatória. A ausência de resposta não é recusa voluntária.

### 7.2 Revisão antes do envio

A resposta ou preferência exige:

- conteúdo editável;
- destinatário e finalidade;
- dados não incluídos;
- vínculo exclusivo com a solicitação;
- confirmação inicialmente vazia;
- descarte do rascunho sem cancelar a solicitação;
- retorno sem envio;
- explicação de que o envio poderá retomar a análise.

Enviar não cria vínculo nem garante aprovação.

## 8. Resultados

### 8.1 Cancelada

O resultado distingue decisão da Pessoa de recusa do Coletivo e informa tratamento posterior conforme regra apresentada, sem garantia técnica absoluta.

Uma nova solicitação exige nova revisão; o histórico não funciona como confirmação reutilizável.

### 8.2 Aprovada

A aprovação apresenta:

- autoridade e fundamento;
- vínculo de participante confirmado;
- visibilidade inicial preservada;
- notificações não ativadas automaticamente;
- ausência de função, moderação, autoridade ou presença obrigatória;
- continuidade para o ambiente interno sem declarar superfícies futuras como reformuladas.

### 8.3 Recusada

A recusa apresenta fundamento proporcional e deixa claro que não é sanção, reputação, avaliação pública ou autorização de contato privado.

Revisão formal somente poderá aparecer quando houver contrato, regra, prazo e autoridade próprios. Denúncia permanece separada.

### 8.4 Expirada

Expiração significa encerramento temporal sem aprovação ou recusa.

Nova tentativa somente poderá ser iniciada quando entradas estiverem disponíveis, com nova revisão e sem preenchimento silencioso de dados anteriores.

## 9. Cobertura visual validada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Coletivos — revisão e solicitação | 5 | 5 | 0 |
| Coletivos — Solicitação Pendente | 8 | 8 | 0 |
| **Total de Coletivos** | **22** | **22** | **0** |
| Opportunity Boost | 46 | 36 | 10 |

## 10. Decisões preservadas

- acompanhar não é participar;
- solicitação não é aprovação;
- comprovante não é acompanhamento contínuo;
- consultar não altera fila;
- estimativa não é promessa;
- pedido adicional não é obrigação de revelar;
- preferir não informar não é recusa voluntária;
- descartar resposta não cancela solicitação;
- cancelamento da Pessoa não é recusa do Coletivo;
- recusa não é reputação ou sanção;
- expiração não é recusa ou consentimento;
- denúncia não é revisão formal;
- apoio institucional não concede autoridade ou dados;
- evento futuro não é garantia de implementação.

## 11. Limites

Não são iniciados:

- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- fila e gestão do responsável;
- revisão formal completa da recusa;
- política jurídica;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto;
- Expressão Guiada do Momento Atual;
- ambiente de simulação das jornadas.

## 12. Critérios de saída concluídos

A família está materializada e funcionalmente validada porque:

- os oito SVGs existem e foram reformulados;
- espera, ação necessária e resultado são distinguíveis;
- autoridade, estimativa, dados e consequência estão visíveis;
- cancelamento, recusa e expiração não se confundem;
- o estado protegido preserva exposição mínima;
- informação adicional preserva voluntariedade;
- nenhuma superfície futura é apresentada como disponível;
- a validação mecânica do Repositório deverá ser aprovada no pacote da UXA-067.

## 13. Próxima transição recomendada

**UXA-068 — Expressão Guiada do Momento Atual por Texto e Voz.**

A UXA-068 deverá materializar a orientação anterior ao relato, a captura multimodal guiada, perguntas adaptativas, síntese estruturada e revisão antes da compreensão inicial.

A UXA-068 não é iniciada por esta atualização e depende de autorização separada.
