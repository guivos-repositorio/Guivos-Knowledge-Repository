---
id: RP-002-PILOT-PRIV-001
title: Piloto — Controlador, Canal de Privacidade e Prontidão Jurídico-Operacional
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_privacy_preflight_partial
related:
  - RP-002-PILOT-OP-001
  - RP-002-PMF-001
---

# Piloto — Controlador, Canal de Privacidade e Prontidão Jurídico-Operacional

## 1. Finalidade

Este documento registra o estado verificável do primeiro blocker de privacidade do piloto `RP-002`:

> **quem é o agente que deverá assumir formalmente o papel de controlador do tratamento de dados do piloto e por qual canal uma Pessoa poderá exercer direitos e pedir esclarecimentos?**

A função deste registro é impedir duas formas de falsa segurança:

1. concluir que a entidade que aparece publicamente no site é automaticamente o controlador do piloto sem decisão formal sobre as operações de tratamento;
2. transformar um canal comercial ou institucional genérico em canal de privacidade sem designação e governança explícitas.

Este documento não substitui assessoria jurídica ou revisão de privacidade.

## 2. Estado executivo

| Item | Evidência atual | Estado |
|---|---|---|
| identidade institucional pública `Guivos Ltda` | exibida no site oficial Guivos | `PUBLICLY VERIFIED` |
| CNPJ `43.530.598/0001-33` | exibido no site oficial Guivos | `PUBLICLY VERIFIED` |
| existência de link público “Política de Privacidade” | exibido no rodapé do site oficial | `PUBLICLY VERIFIED` |
| conteúdo atual integral da Política de Privacidade | não foi validado por esta auditoria | `NOT VERIFIED` |
| Guivos Ltda formalmente designada controladora deste piloto | não há decisão operacional/jurídica localizada no GKR | `NOT FORMALLY CONFIRMED` |
| canal dedicado de privacidade do piloto | não localizado em fonte oficial verificável | `NOT VERIFIED` |
| encarregado/DPO aplicável e formalmente designado | não localizado | `NOT VERIFIED / APPLICABILITY REVIEW REQUIRED` |
| base legal do tratamento do piloto | não definida por este documento | `BLOCKER` |
| Participant 001 | depende dos itens críticos acima | `HOLD` |

Conclusão:

```text
IDENTIDADE INSTITUCIONAL PÚBLICA
→ VERIFICADA

CONTROLADOR DO PILOTO
→ NÃO FORMALMENTE CONFIRMADO

CANAL DE PRIVACIDADE
→ NÃO VERIFICADO

BASE LEGAL
→ BLOCKER

PARTICIPANT 001
→ HOLD
```

## 3. Evidência institucional pública encontrada

Em 27/08/2026, o site oficial da Guivos exibia no rodapé:

```text
Guivos Ltda ®
CNPJ: 43.530.598/0001-33
```

Também exibia acesso a:

- `Termos de Uso`;
- `Política de Privacidade`.

Fonte pública verificada:

<https://www.guivos.com/>

Essa evidência é suficiente para registrar que **Guivos Ltda é a identidade jurídica apresentada publicamente pelo ativo institucional consultado**.

Ela não é suficiente, sozinha, para registrar que Guivos Ltda já tomou a decisão formal de ser o controlador das operações específicas do Dry Run Real.

## 4. O que significa “controlador” para este gate

A definição operacional usada pelo piloto deve seguir a realidade das decisões sobre o tratamento, não apenas a marca exibida ao público.

A ANPD explica que o controlador é o agente que toma as principais decisões referentes ao tratamento de dados pessoais e responde pelas responsabilidades correspondentes perante os titulares.

Referência oficial:

<https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1>

Portanto, para fechar `P1 — Controlador formal`, deve existir evidência de quem decide, no piloto, elementos como:

- por que os dados serão tratados;
- quais categorias serão coletadas;
- quais ferramentas/operadores serão usados;
- quem terá acesso;
- quanto tempo os dados serão mantidos;
- quando haverá correção, limitação ou exclusão;
- quais follow-ups serão realizados;
- como incidentes serão tratados;
- como solicitações dos titulares serão respondidas.

Regra:

> **A identidade pública da empresa é evidência institucional; o papel de controlador depende da realidade decisória da operação.**

## 5. Candidato institucional mais plausível

Com a evidência disponível, a entidade pública que **deve ser avaliada formalmente** para assumir o papel de controlador do piloto é:

```text
GUIVOS LTDA
CNPJ 43.530.598/0001-33
```

Classificação correta neste momento:

```text
CANDIDATE CONTROLLER
→ GUIVOS LTDA

FORMAL CONTROLLER DECISION
→ PENDING
```

Este documento deliberadamente não promove `CANDIDATE` para `CONFIRMED`.

## 6. Por que o GKR não deve “decidir” o controlador por inferência

O GKR registra conhecimento e decisões autorizadas.

Ele não deve criar fatos jurídicos que ainda não ocorreram na operação.

Seria incorreto transformar:

```text
empresa aparece no site
```

em:

```text
empresa já decidiu finalidades, meios e responsabilidades do piloto
```

sem evidência material dessa decisão.

## 7. Canal de privacidade — estado atual

A auditoria não encontrou no GKR nem em fonte oficial verificável um endereço, formulário ou telefone explicitamente designado como **canal de privacidade / direitos do titular** para o piloto.

Não se deve promover automaticamente:

- e-mail comercial;
- e-mail de suporte;
- WhatsApp;
- canal de vendas;
- formulário genérico de contato;

para essa função apenas porque já existem.

Regra:

> **canal existente ≠ canal de privacidade designado.**

Estado:

```text
PRIVACY CHANNEL
→ NOT VERIFIED
→ BLOCKER
```

## 8. Política de Privacidade pública

O rodapé do site oficial exibe um link denominado `Política de Privacidade`.

A auditoria atual não conseguiu validar integralmente, de forma independente, o conteúdo e a versão vigente desse documento.

Por isso, este registro não afirma que a política atual já cubra:

- o piloto RP-002;
- pesquisa de Journey;
- benchmark;
- follow-up;
- dados pseudonimizados;
- uso de IA;
- operadores específicos;
- retenção do piloto;
- Evidence Guivos experimental.

Antes do Dry Run, é necessário verificar o conteúdo real da política/aviso aplicável e decidir se o piloto requer aviso específico complementar.

## 9. Aviso de privacidade do piloto

O `RP-002-PILOT-OP-001` já exige que o participante receba informação clara e proporcional antes da coleta.

Como referência estrutural, o aviso de privacidade da ANPD organiza informação sobre:

- tipos de dados;
- finalidades;
- como os dados são obtidos;
- armazenamento;
- compartilhamento;
- eliminação;
- segurança;
- direitos;
- contato.

Referência oficial, modificada em 01/07/2026:

<https://www.gov.br/anpd/pt-br/acesso-a-informacao/aviso-de-privacidade>

Isso não significa copiar o aviso da ANPD.

Significa usar transparência equivalente à realidade do piloto.

## 10. Direitos do titular que o canal precisa suportar

A ANPD apresenta, entre os direitos aplicáveis, informação, confirmação/acesso, correção, bloqueio, exclusão nas hipóteses cabíveis, eliminação em tratamentos baseados em consentimento quando aplicável, revogação do consentimento, informação sobre compartilhamento e revisão/explicação de decisões automatizadas quando aplicável.

Referência oficial:

<https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares>

Para o piloto, o canal escolhido precisa possuir processo operacional mínimo para:

```text
RECEBER
→ IDENTIFICAR A SOLICITAÇÃO
→ VERIFICAR O ESCOPO
→ LOCALIZAR O REGISTRO
→ CORRIGIR / LIMITAR / EXCLUIR QUANDO CABÍVEL
→ REGISTRAR A RESPOSTA
→ FECHAR O PEDIDO
```

A existência de um endereço de e-mail sem processo de atendimento não fecha o gate.

## 11. Encarregado / DPO

A ANPD descreve o encarregado como a pessoa natural ou jurídica indicada para atuar como canal de comunicação entre controlador, titulares e ANPD.

Referências oficiais:

<https://www.gov.br/anpd/pt-br/canais_atendimento/encarregado-de-dados-na-anpd>

<https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes/perguntas-frequentes>

A própria ANPD também registra que determinadas categorias de agentes de tratamento de pequeno porte podem possuir regras específicas de dispensa, desde que os requisitos regulatórios aplicáveis sejam efetivamente satisfeitos.

Portanto:

```text
NÃO LOCALIZAMOS ENCARREGADO
≠ PROVA DE NÃO CONFORMIDADE

POSSÍVEL DISPENSA
≠ DISPENSA AUTOMÁTICA
```

O piloto requer **avaliação de aplicabilidade**, e não suposição.

## 12. Fiscalização recente como sinal de materialidade

Em 2026, a ANPD informou monitoramento de empresas e órgãos públicos envolvendo obrigações relacionadas à indicação de encarregado e à disponibilização de canais de comunicação com titulares.

Referência oficial:

<https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-conclui-monitoramento-avaliar-sancao-empresas-orgaos-publicos>

Esse registro não é usado para afirmar que a Guivos está sujeita a uma medida específica.

Ele apenas reforça que o blocker não deve ser tratado como formalidade documental secundária.

## 13. Base legal continua separada

Mesmo que o controlador seja formalmente definido, o piloto ainda não está liberado enquanto a base legal não for documentada à luz dos fatos reais.

Este documento não presume:

- consentimento;
- legítimo interesse;
- execução de contrato;
- obrigação legal;
- proteção da vida;
- tutela da saúde;
- qualquer outra hipótese.

A base legal deve ser definida para as operações efetivas e revisada antes da coleta.

Referência oficial:

<https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes/perguntas-frequentes>

## 14. Decisão mínima necessária para promover P1 a PASS

`P1 — Controlador formal` só pode mudar para `PASS` quando existir registro aprovado contendo, no mínimo:

```text
CONTROLADOR DO PILOTO
→ razão social
→ CNPJ ou identificação aplicável
→ papel decisório declarado
→ responsável operacional pela decisão
→ data de vigência
→ escopo: Dry Run / piloto RP-002
```

A declaração deve corresponder à realidade operacional.

## 15. Decisão mínima necessária para promover P2 a PASS

`P2 — Canal de privacidade` só pode mudar para `PASS` quando houver:

```text
CANAL DESIGNADO
→ e-mail / formulário / outro meio verificável

PUBLICAÇÃO / COMUNICAÇÃO
→ participante consegue encontrá-lo

PROCESSO DE ATENDIMENTO
→ owner definido
→ registro de pedidos
→ correção / limitação / exclusão operáveis

TESTE
→ solicitação sintética recebida e fechada
```

## 16. Critério para canal dedicado

O canal pode ser operacionalmente simples no primeiro Dry Run, desde que seja:

- oficial;
- monitorado;
- verificável;
- informado ao participante;
- capaz de suportar o processo de direitos;
- separado o suficiente para não perder solicitações entre mensagens comerciais.

Não há exigência metodológica do RP-002 para construir sistema complexo antes do piloto.

A exigência é **funcionalidade real e governança**.

## 17. Evidence Matrix deste blocker

| Claim | Fonte | Força | Estado |
|---|---|---:|---|
| Guivos apresenta publicamente a razão `Guivos Ltda` | site oficial | alta para identidade pública | `SUPPORTED` |
| Guivos apresenta publicamente CNPJ `43.530.598/0001-33` | site oficial | alta para identidade pública | `SUPPORTED` |
| site expõe link `Política de Privacidade` | site oficial | alta | `SUPPORTED` |
| Guivos Ltda é o controlador formal do RP-002 | nenhuma decisão localizada | insuficiente | `UNPROVEN` |
| existe canal dedicado de privacidade | não localizado | insuficiente | `UNPROVEN` |
| existe encarregado aplicável/designado | não localizado | insuficiente | `UNPROVEN` |
| política pública cobre o RP-002 | conteúdo não validado | insuficiente | `UNPROVEN` |
| Participant 001 pode ser liberado | blockers permanecem | insuficiente | `NO` |

## 18. Atualização do gate de prontidão

Estado após esta auditoria:

```text
P1A — IDENTIDADE INSTITUCIONAL PÚBLICA
→ PASS

P1B — CONTROLADOR DO PILOTO FORMALMENTE DESIGNADO
→ HOLD

P2A — EXISTÊNCIA DE POLÍTICA PÚBLICA REFERENCIADA NO SITE
→ EVIDÊNCIA DE LINK, CONTEÚDO A VALIDAR

P2B — CANAL DE PRIVACIDADE DESIGNADO
→ HOLD

P2C — PROCESSO DE DIREITOS TESTADO NO CANAL REAL
→ HOLD

P3 — FINALIDADES / CATEGORIAS
→ PENDING FINALIZATION

P4 — BASE LEGAL
→ HOLD

PARTICIPANT 001
→ HOLD
```

## 19. Próxima sequência legítima

```text
1. FORMALIZAR QUEM É O CONTROLADOR DO PILOTO
↓
2. DEFINIR / APROVAR CANAL OFICIAL DE PRIVACIDADE
↓
3. VALIDAR POLÍTICA / AVISO APLICÁVEL AO PILOTO
↓
4. DEFINIR BASE LEGAL COM FATOS REAIS
↓
5. TESTAR DIREITOS NO CANAL REAL
↓
6. ATUALIZAR REGISTRO DE LIBERAÇÃO
```

Nenhum desses passos autoriza pular o registro de operadores, permissões, Safety Owner, Supply Verifier ou benchmark blind definidos em `RP-002-PILOT-OP-001`.

## 20. Regra final

> **O piloto não deve ganhar velocidade sacrificando verificabilidade jurídica e operacional. Ao mesmo tempo, privacidade proporcional não significa burocracia infinita: o objetivo é identificar claramente quem decide, informar a Pessoa, disponibilizar um canal funcional, minimizar dados e conseguir honrar direitos na prática.**

Até que essa realidade esteja formalizada:

```text
DRY RUN REAL
→ NOT RELEASED

PARTICIPANT 001
→ HOLD
```
