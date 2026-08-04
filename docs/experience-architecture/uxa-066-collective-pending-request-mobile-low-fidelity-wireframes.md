---
id: UXA-066
title: Wireframes Móveis da Solicitação Pendente em Coletivos
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
  - UXA-064
  - UXA-065
related:
  - UXA-067
  - M7.68
normative: false
---

# Wireframes Móveis da Solicitação Pendente em Coletivos

## 1. Finalidade

Este documento materializa a quinta referência P0A do programa UXA-059: a Solicitação Pendente móvel da Pessoa.

A família transforma o comprovante transitório da UXA-064 em acompanhamento contínuo governado, sem reutilizar o comprovante como tela de gestão.

A experiência deverá permitir responder:

> **Qual é o estado real da minha solicitação, quem possui autoridade para agir, qual prazo foi informado, quais dados estão em análise, o que precisa de mim e qual consequência cada evento produz?**

A UXA-066 cria wireframes de baixa fidelidade. Não cria protótipo, identidade visual, política jurídica, API, esquema de dados, automação de decisão ou implementação.

## 2. Continuidade materializada

```text
Perfil Público
→ revisão e envio
→ comprovante transitório
→ Solicitação Pendente
→ aguardar decisão ou responder informação adicional
→ cancelar, ser aprovada, recusada ou expirar
→ retornar ao Perfil Público ou abrir o Coletivo
```

O acesso futuro por `Meus Coletivos` permanece reservado. A UXA-066 não apresenta essa superfície como disponível.

## 3. Decisão de família

Solicitação Pendente não é uma única tela genérica. O estado altera materialmente hierarquia, decisão principal, risco, dados, consequência e continuidade.

Foram materializados oito SVGs:

1. solicitação aguardando decisão do Coletivo;
2. solicitação em análise protegida;
3. informação adicional solicitada;
4. revisão da resposta adicional;
5. solicitação cancelada pela pessoa;
6. solicitação aprovada;
7. solicitação recusada;
8. solicitação expirada.

## 4. Inventário

| Estado | Arquivo | Decisão principal |
|---|---|---|
| aguardando decisão | `uxa-066-collective-pending-request-awaiting-decision-mobile.svg` | atualizar estado ou cancelar conscientemente |
| análise protegida | `uxa-066-collective-pending-request-protected-analysis-mobile.svg` | atualizar estado protegido, cancelar ou denunciar |
| informação adicional | `uxa-066-collective-pending-request-additional-information-required-mobile.svg` | preparar resposta, contestar finalidade ou cancelar |
| revisão da resposta | `uxa-066-collective-pending-request-additional-information-review-mobile.svg` | confirmar envio da resposta revisada |
| cancelada | `uxa-066-collective-pending-request-cancelled-mobile.svg` | compreender consequência e retornar ao perfil |
| aprovada | `uxa-066-collective-pending-request-approved-mobile.svg` | abrir o Coletivo sem alterar escolhas |
| recusada | `uxa-066-collective-pending-request-refused-mobile.svg` | compreender fundamento e retornar com proteção |
| expirada | `uxa-066-collective-pending-request-expired-mobile.svg` | compreender regra temporal e decidir se recomeça futuramente |

## 5. Regras transversais

### 5.1 Estado verificável

Cada tela apresenta:

- estado atual em linguagem direta;
- data e hora da última atualização material;
- identificador do processo;
- autoridade responsável;
- consequência atual;
- diferença entre prazo estimado e garantia.

Atualizar a tela não cria nova decisão nem altera posição em fila.

### 5.2 Solicitação não é participação

Enquanto pendente:

- não existe acesso interno;
- não existe função;
- não existe autoridade;
- não existe presença em lista de participantes;
- não existe contato privado automático;
- não existe comunicação comercial autorizada.

### 5.3 Autoridade delimitada

A Pessoa deve saber:

- quem solicitou ou registrou o evento;
- qual papel possui autoridade;
- se a análise é comum ou especializada;
- que Organização apoiadora não recebe dados ou autoridade automaticamente.

### 5.4 Dados proporcionais

A superfície mostra:

- dados enviados;
- dados explicitamente não enviados;
- finalidade da análise;
- bloqueio de edição durante decisão, quando aplicável;
- caminho para ver o conteúdo exato;
- tratamento posterior sujeito à regra informada.

Nenhum wireframe define a base jurídica definitiva, o período técnico de retenção ou a tecnologia de consentimento.

### 5.5 Cancelamento consciente

Cancelar:

- exige confirmação antes da ação destrutiva;
- encerra a análise sem criar vínculo;
- não equivale a recusa do Coletivo;
- não gera penalidade reputacional automática;
- bloqueia novos usos incompatíveis dos dados;
- preserva somente o registro necessário conforme regra aplicável.

A confirmação destrutiva poderá ser modal ou variação da mesma superfície; não exige SVG próprio nesta materialização.

### 5.6 Eventos futuros

A solicitação poderá receber:

- pedido de informação adicional;
- aprovação;
- recusa;
- expiração;
- cancelamento pela pessoa;
- mudança material de regras exigindo nova revisão.

Cada evento deverá identificar fundamento, autoridade, data, consequência e ação disponível.

## 6. Estado aguardando decisão

O estado principal apresenta:

- recebimento e última atualização;
- responsável autorizado;
- prazo estimado e data correspondente;
- dados em análise;
- próximos eventos possíveis;
- ação de atualização sem prioridade artificial;
- cancelamento com confirmação.

Atraso não é apresentado como recusa. Silêncio não é aprovação.

## 7. Análise protegida

O estado protegido altera materialmente risco e visibilidade.

Ele preserva:

- nome reduzido do Coletivo;
- identificador protegido;
- remetente e autoridade;
- equipe especializada sem exposição desnecessária;
- alegação do remetente como não verificada;
- dados mínimos;
- localização, Jornada, contatos e outros vínculos ocultos;
- cancelamento e denúncia separados.

Cancelar ou denunciar não cria exposição pública automática.

## 8. Informação adicional

### 8.1 Pedido recebido

A tela informa:

- pergunta exata;
- finalidade declarada;
- autoridade solicitante;
- formato de resposta aceito;
- prazo e regra de expiração;
- dados proibidos;
- efeito da espera sobre a análise;
- opção de responder, preferir não informar, contestar ou cancelar.

A ausência de resposta não é descrita como recusa voluntária.

### 8.2 Revisão antes do envio

A resposta adicional exige:

- conteúdo editável;
- destinatário e finalidade;
- dados não incluídos;
- vínculo exclusivo com a solicitação;
- confirmação inicialmente vazia;
- cancelamento sem envio.

Enviar a resposta não cria vínculo nem garante aprovação.

## 9. Resultados

### 9.1 Cancelada

O resultado distingue decisão da Pessoa de recusa do Coletivo e informa tratamento posterior dos dados.

Uma nova solicitação exige nova revisão; o histórico não funciona como confirmação reutilizável.

### 9.2 Aprovada

A aprovação apresenta:

- autoridade e fundamento;
- vínculo de participante confirmado;
- visibilidade inicial preservada;
- notificações não ativadas automaticamente;
- ausência de função, moderação ou autoridade automática;
- ação para abrir o ambiente interno.

A UXA-066 não reformula o Início do Participante.

### 9.3 Recusada

A recusa apresenta fundamento proporcional e deixa claro que não é:

- sanção;
- suspensão;
- avaliação pública;
- nota sobre a Pessoa;
- autorização de contato privado.

Revisão formal, quando aplicável, deverá ter regra, prazo e autoridade próprios. A UXA-066 não materializa o processo completo de contestação.

### 9.4 Expirada

Expiração significa encerramento temporal sem aprovação ou recusa.

Ela não será convertida em:

- consentimento;
- recusa voluntária;
- punição;
- baixa reputação.

Nova tentativa exige nova revisão e não reutiliza dados silenciosamente.

## 10. Navegação

As telas utilizam `Eu` como contexto pessoal ativo, mas não criam `Meus Coletivos`.

Entradas atuais:

- comprovante transitório salvo;
- Perfil Público com solicitação existente;
- convite protegido.

Saídas atuais:

- Perfil Público;
- ambiente interno após aprovação;
- registro salvo.

A futura UXA de `Meus Coletivos` deverá conectar a estas superfícies sem duplicar seu conteúdo.

## 11. Cobertura visual proposta

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Coletivos — revisão e solicitação | 5 | 5 | 0 |
| Coletivos — Solicitação Pendente | 8 | 0 | 8 |
| **Total de Coletivos** | **22** | **14** | **8** |
| Opportunity Boost | 46 | 36 | 10 |

As contagens permanecem separadas.

## 12. Decisões preservadas

- acompanhar não é participar;
- solicitação não é aprovação;
- comprovante não é acompanhamento contínuo;
- prazo estimado não é promessa;
- atraso não é recusa;
- expiração não é recusa;
- cancelamento da Pessoa não é recusa do Coletivo;
- informação adicional não garante aprovação;
- apoio institucional não concede autoridade ou dados;
- acessibilidade não é condição de elegibilidade;
- alegação não verificada não é fato;
- decisão sobre vínculo não é reputação da Pessoa.

## 13. Limites

Não são iniciados:

- validação funcional dos oito SVGs;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- fila e gestão do responsável;
- contestação completa da recusa;
- política jurídica;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 14. Critérios de saída do pacote

O pacote estará materializado quando:

- os oito SVGs existirem;
- espera, ação necessária e resultado forem distinguíveis;
- autoridade, prazo, dados e consequência estiverem visíveis;
- cancelamento, recusa e expiração não forem confundidos;
- o estado protegido preservar exposição mínima;
- nenhuma superfície futura for apresentada como disponível;
- a validação mecânica do Repositório for aprovada.

## 15. Próxima transição recomendada

**UXA-067 — Validação Funcional e Reformulação da Solicitação Pendente Móvel em Coletivos.**

A UXA-067 deverá avaliar os oito estados como uma continuidade única antes de iniciar `Meus Coletivos`.

A validação depende de autorização separada.
