---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - UXA-065
  - UXA-066
  - UXA-067
  - UXA-068
  - UXA-069
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
normative: false
---

# Jornada Integrada da Pessoa

## 1. Início protegido e compreensão inicial

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada por texto ou voz
→ inventário e autorização
→ processamento visível
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje e continuidades autorizadas
```

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| Home pública | validado | UXA-020 | UXA-022 | UXA-021 | parcial: entrada protegida examinada em pacote próprio |
| entrada protegida, escolha e autorização | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | parcial: ligação com expressão guiada exige leitura conjunta |
| expressão guiada | validado | UXA-068 | UXA-068 | UXA-069 | parcial: saída para inventário depende das autoridades da UXA-034 |
| processamento e compreensão inicial | validado | UXA-023 | UXA-036 | UXA-037 | parcial: transições examinadas nos pacotes de origem, não ponta a ponta nesta seção |
| Tela Hoje e continuidade recorrente | validado | UXA-002 | UXA-006 | UXA-010 | não examinada como continuidade integral após a compreensão inicial |

As superfícies citadas possuem materialização e validação nos respectivos pacotes, mas isso não valida toda a jornada pessoal ponta a ponta.

## 2. Pessoa em Coletivos

```text
Explorar Coletivos
→ Resultados de Busca
→ Perfil Público
→ Revisão e Solicitação
→ Solicitação Pendente
→ resultado aprovado
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| descoberta e busca | validado | UXA-056 | UXA-060 | UXA-061 | parcial |
| Perfil Público | validado | UXA-056 | UXA-062 | UXA-063 | parcial |
| revisão e solicitação | validado | UXA-056 | UXA-064 | UXA-065 | parcial |
| Solicitação Pendente | validado | UXA-056 | UXA-066; estado aprovado reformulado por UXA-091/092 | UXA-067 para a família; UXA-092 para o estado aprovado corrente | handoffs 105/106/107/109 integrados por UXA-090; TRN-108 integrada por UXA-092 |
| Meus Coletivos | validado | UXA-056; UXA-059 | UXA-091; reformulação UXA-092 | UXA-092 | TRN-108 integralmente validada; TRN-110 parcial |
| Central de Atualizações | materializado | UXA-058; UXA-059 | UXA-093; 1 SVG móvel | validação funcional pendente | TRN-110 parcial com ambos os endpoints materializados; TRN-111 ausente |
| Início do Participante | reformulação pendente | UXA-059 | referência anterior não promovida nesta seção | — | ausente |

A UXA-093 materializa a Central de Atualizações sem validar a sequência completa de Coletivos. A central permanece uma superfície de triagem de mudanças, não um feed social ou substituto dos canais especializados.

## 3. Continuidade pós-aprovação validada

```text
COL-003 — decisão autorizada
→ resultado aprovado em PER-105
→ vínculo já formado
→ Pessoa escolhe “Ver em Meus Coletivos” ou “Agora não”
→ PER-106 — mesmo vínculo confirmado visível quando a navegação ocorre
```

A continuidade acima está **integralmente validada no escopo documental de `GKR-TRN-108`**. A navegação não cria o vínculo e a escolha de não abrir `Meus Coletivos` imediatamente não desfaz a aprovação.

## 4. Central de Atualizações materializada

`PER-107` passa a possuir uma referência móvel primária com:

- origem, tipo, contexto e autoridade da atualização;
- estado de leitura separado do estado substantivo do objeto;
- necessidade de ação e prazo legítimo quando existirem;
- ordenação por segurança, ação, prazo, preferência e recência;
- retorno a destinos já materializados quando aplicável;
- ausência explícita de ranking, popularidade, publicidade silenciosa ou pressão por engajamento.

A materialização não fecha `TRN-110`: o gatilho na origem, a preservação de contexto, retornos, concorrência, idempotência e a relação entre leitura e ação ainda precisam ser validados como um conjunto.

## 5. Decisões e proteções

- compartilhar pouco permanece legítimo;
- digitar não autoriza análise automática;
- gravação e transcrição possuem finalidade limitada;
- ajuda temporária não cria compreensão persistente;
- solicitação não equivale a aprovação;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- aprovação não cria função, autoridade, notificação ou presença obrigatória;
- `Meus Coletivos` separa participação de acompanhamento, solicitação, convite e pausa;
- `Meus Coletivos` não utiliza ranking, pontuação de dedicação, comparação ou contagem própria de não lidos;
- a Central de Atualizações preserva as naturezas dos objetos e não os reduz a feed único;
- marcar como lido não confirma presença, concordância, nova regra ou ação concluída;
- alertas de segurança exigem risco material e autoridade identificada;
- recusa, cancelamento e expiração são eventos distintos;
- leitura, rolagem e silêncio não equivalem a confirmação;
- transições ausentes são mostradas como lacunas.

## 6. Estado da vista

Esta vista permanece `draft` porque:

- a continuidade entre compreensão inicial e Tela Hoje não foi validada como conjunto;
- `PER-107` está materializada, mas ainda não validada funcionalmente;
- `PER-108` permanece com reformulação pendente;
- `TRN-110` continua parcial;
- `TRN-111` continua ausente;
- estados P0B adicionais de `Meus Coletivos` e da Central permanecem separados;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

O status `draft` não invalida referências locais e handoffs específicos já validados.

## 7. Próxima evolução possível

A próxima frente autorizável para a continuidade de Coletivos é **UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**.

A UXA-094 não é iniciada pela UXA-093 e depende de autorização separada.