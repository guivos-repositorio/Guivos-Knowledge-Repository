---
id: GKR-BUSINESS-HOME-CONTINUITY-001
title: Checkpoint de Continuidade — Home Pública — Guivos Business — 2026-08-16
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-16
parent: GKR-BUSINESS-CONTINUITY-001
depends_on:
  - GKR-UX-HOME-BUSINESS-NARRATIVE-001
  - GPA-004
  - GKR-BUSINESS-CONTINUITY-001
  - GKR-STATE-001
  - ROADMAP-12.79.0
normative: false
---

# Checkpoint de Continuidade — Home Pública — Guivos Business — 2026-08-16

## 1. Finalidade

Preservar o ponto exato de continuidade da Home Pública do Guivos Business após as validações narrativas realizadas entre a ressincronização de `GPA-004` v1.6.0 e 2026-08-16.

Este checkpoint sucede, para fins de retomada da Home Business, o estado descrito em `GKR-BUSINESS-CONTINUITY-001` v1.1.0 no qual o Checkpoint 3 ainda constava como não convergido.

A autoridade normativa da nova arquitetura narrativa é:

> `GKR-UX-HOME-BUSINESS-NARRATIVE-001` — **Autoridade Narrativa — Home Pública — Guivos Business**.

## 2. Base técnica no momento da abertura desta atualização

```text
REPOSITÓRIO
Guivos-Knowledge-Repository

MAIN DE PARTIDA
20c6927cfdf9ea1644ac34bbe7bc377d1e70433f

ÚLTIMO MARCO FUNCIONAL
M7.88

ÚLTIMA UXA NUMERADA
UXA-101

GKR-STATE-001
2.37.0

ROADMAP
12.79.0
```

Esta atualização de Experience Architecture **não cria novo marco funcional**, não inicia `UXA-102/V5` e não retoma Product Engineering.

## 3. Estado da Home antes deste checkpoint

Após a PR #273, a Home Business estava registrada assim:

```text
CHECKPOINT 2
→ base conceitual validada

CHECKPOINT 3
→ arquitetura narrativa iniciada
→ não convergida
→ movimentos 6 e 9 exigiam reformulação
```

Desde então houve nova rodada de validação conceitual em conversa.

O estado acima não representa mais o ponto atual da construção da Home.

## 4. Decisão estrutural principal validada

A narrativa do Guivos Business não deve ser governada pela enumeração dos produtos ou pela complexidade das suas mecânicas.

Decisão validada:

> **O produto não é o protagonista; a evolução humana é.**

A Home passa a ser orientada por duas expressões complementares:

> **Ajudar seres humanos a terem uma vida melhor.**

> **Apoiar pessoas em sua evolução.**

A primeira representa a direção humana mais ampla. A segunda representa como o Business contribui para essa direção.

“Vida melhor” pode se relacionar àquilo que os seres humanos fazem, vivem, buscam ou querem construir para suas vidas, sem que empresa ou Guivos definam um score universal de pessoa melhor.

## 5. Checkpoint 2 permanece preservado

Continuam validados:

**Tese**

> **Quando uma empresa amplia possibilidades para as pessoas, novas possibilidades também se abrem para a própria empresa.**

**Protagonista**

> **A empresa é o protagonista comercial; as pessoas são o centro humano do valor criado.**

**Problema**

> **Como criar relações mais relevantes, ampliar possibilidades e compreender movimentos sem reduzir pessoas a números, pontos ou mecanismos de controle?**

**Promessa**

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

**Pergunta-mãe**

> **O que sua empresa pode tornar possível para as pessoas?**

## 6. Checkpoint 5 — arquitetura narrativa convergida

A nova sequência foi validada integralmente e substitui o estado narrativo não convergido do Checkpoint 3.

```text
01 — O QUE SUA EMPRESA PODE TORNAR POSSÍVEL PARA AS PESSOAS?
02 — EMPRESAS TAMBÉM PODEM AJUDAR SERES HUMANOS A TEREM UMA VIDA MELHOR
03 — APOIAR A EVOLUÇÃO NÃO É ESCOLHER O CAMINHO
04 — AMPLIE O ACESSO À EVOLUÇÃO
05 — RECONHEÇA MOVIMENTOS. INCENTIVE NOVOS PASSOS.
06 — TRANSFORME RECONHECIMENTO EM NOVAS POSSIBILIDADES
07 — UMA POSSIBILIDADE PODE LEVAR A MUITAS OUTRAS
08 — COMPREENDA PARA CONTINUAR APOIANDO MELHOR
09 — DA PRIMEIRA INICIATIVA À OPERAÇÃO EM GRANDE ESCALA
10 — O QUE SUA EMPRESA PODE TORNAR POSSÍVEL?
```

A progressão de significado é:

```text
POSSIBILIDADE
→ PROPÓSITO HUMANO
→ AUTONOMIA
→ JOURNEY
→ RECONHECIMENTO E INCENTIVOS
→ BENEFÍCIOS
→ POSSIBILIDADES DA VIDA / ECOSSISTEMA
→ INTELLIGENCE
→ ESCALA
→ SÍNTESE E FUTURA CONVERSÃO
```

## 7. Journey passa a preceder Programas de Incentivo na narrativa

Validação explícita:

> **Programa de Incentivo deve vir depois do Journey na Home.**

Razão:

- a evolução humana deve ser a evidência principal;
- Journey materializa diretamente a possibilidade de a empresa apoiar a evolução sem escolher o caminho da pessoa;
- Programas de Incentivo passam a apoiar e reforçar essa evolução, em vez de dominar a proposta de valor pública.

Isso não altera a taxonomia funcional de `GPA-004`, que continua reconhecendo duas ofertas principais e permite contratação independente ou conjunta.

## 8. Formulação preferida para Journey Business

A formulação validada como mais clara é:

> **Sua empresa pode oferecer acesso ao Guivos Journey e permitir que seus funcionários encontrem caminhos, experiências e possibilidades de evolução relevantes para suas próprias vidas.**

Ela deve ser preferida a formulações vagas como “ampliar o acesso das pessoas” porque explicita:

- quem contrata: a empresa;
- quem recebe: seus funcionários;
- o que é oferecido: acesso ao Guivos Journey;
- qual o valor: caminhos, experiências e possibilidades de evolução relevantes para a própria vida.

Princípio complementar:

> **Sua empresa amplia o acesso. Cada pessoa escolhe o próprio caminho.**

## 9. Pontos Guivos deixam de ser eixo narrativo

Validação explícita:

> **Pontos não devem ser a narrativa da Home.**

Pontos Guivos permanecem funcionalmente relevantes, mas entram apenas como mecanismo secundário de benefício/pagamento para possibilidades elegíveis.

A Home deve se diferenciar das plataformas tradicionais de pontos, rewards, cashback ou fidelidade por colocar no centro:

```text
EVOLUÇÃO HUMANA
↓
JORNADAS
↓
EXPERIÊNCIAS
↓
RECONHECIMENTO
↓
INCENTIVOS
↓
NOVAS POSSIBILIDADES
```

A complexidade operacional de pontos permanece em `GPA-004` e autoridades econômicas aplicáveis, não precisa ser ensinada na narrativa principal da Home.

## 10. Refinamento final do Movimento 07

A apresentação inicial do ecossistema como simples sequência de produtos:

```text
Journey · Travel · Mall
```

não deve comandar o movimento.

O Movimento 07 deve primeiro demonstrar **possibilidades concretas em diferentes áreas da vida**.

Direção validada:

> **Diferentes áreas da vida. Diferentes possibilidades. Um ecossistema que pode conectá-las.**

Exemplos narrativos de referência:

- vida financeira: aprender, planejar e tomar melhores decisões para a própria realidade;
- saúde e bem-estar: descobrir possibilidades que ajudem a cuidar de si e da qualidade de vida;
- viagens e experiências: conhecer lugares, viver algo diferente e ampliar perspectivas;
- produtos e presentes: tornar possível algo desejado, necessário ou significativo;
- desenvolvimento, interesses, relações e outras dimensões: permitir que uma possibilidade revele outra que a pessoa ainda não havia considerado.

Journey, Travel, Mall e demais capacidades continuam presentes como infraestrutura do ecossistema, mas a unidade narrativa principal é **a vida da pessoa**, não o catálogo de produtos.

Princípio:

> **A Guivos não determina que tipo de evolução deve acontecer. Ela aumenta o universo de possibilidades a partir do qual cada pessoa pode escolher.**

## 11. Intelligence — estado preservado

Intelligence deve aparecer como capacidade de compreender para continuar apoiando melhor.

Não apresentar como dashboard central, vigilância ou importação obrigatória de toda a base empresarial.

A antiga ideia de um movimento específico para explicar que “a Guivos não substitui os sistemas da empresa” permanece descartada.

Integração analítica pode aparecer positivamente como extensão do Intelligence, conforme contrato e autoridade técnica futura.

## 12. Estado atual de convergência

```text
TESE                       → VALIDADA
PROTAGONISTA               → VALIDADO
PROBLEMA                   → VALIDADO
PROMESSA                   → VALIDADA
PERGUNTA-MÃE               → VALIDADA
ARQUITETURA NARRATIVA      → CONVERGIDA / CHECKPOINT 5
AUTORIDADE NARRATIVA       → REGISTRADA EM GKR-UX-HOME-BUSINESS-NARRATIVE-001
CONTRATOS DE AUTORIDADE    → NÃO INICIADOS
CONVERSÃO                  → NÃO CONVERGIDA
DOCUMENTO MESTRE           → NÃO EXISTE
SOURCE LOCK                → NÃO EXISTE
WIREFRAME / UI / PROTÓTIPO → NÃO EXISTEM
DESIGN                     → NÃO AUTORIZADO
```

## 13. Preservações

Esta atualização não:

- altera `M7.88`;
- inicia `UXA-102/V5`;
- retoma Product Engineering;
- muda as duas ofertas principais da arquitetura funcional de `GPA-004`;
- transforma Pontos em produto principal;
- cria Journey corporativa controlada pela empresa;
- transforma Intelligence em módulo Business;
- incorpora Ads ao Business;
- define preços, limites, SLA ou entitlements finais;
- cria Documento Mestre;
- cria Source Lock;
- autoriza Design.

## 14. Próximo ponto exato

A próxima etapa governada da Home Pública do Guivos Business é:

> **CONTRATOS DE AUTORIDADE**

Objetivo da próxima etapa:

- definir o que cada movimento pode afirmar;
- definir o que cada movimento precisa preservar;
- definir o que cada movimento não pode sugerir;
- vincular afirmações às autoridades corretas do produto/ecossistema.

Somente após essa etapa devem avançar conversão, Documento Mestre, Source Lock e Design.

## 15. Instrução de retomada

Ao retomar a Home Guivos Business:

1. ler `GPA-004` v1.6.0 ou autoridade posterior;
2. ler `GKR-UX-HOME-BUSINESS-NARRATIVE-001`;
3. usar este checkpoint como ponto de continuidade;
4. preservar integralmente o Checkpoint 2;
5. tratar o Checkpoint 5 como arquitetura narrativa convergida;
6. não retornar Programas de Incentivo à frente do Journey na narrativa sem nova decisão explícita;
7. não voltar a colocar Pontos no centro da Home;
8. preservar a vida da pessoa como unidade narrativa do Movimento 07;
9. iniciar pelos **Contratos de Autoridade**;
10. não avançar para Design antes de Documento Mestre e Source Lock apropriados.