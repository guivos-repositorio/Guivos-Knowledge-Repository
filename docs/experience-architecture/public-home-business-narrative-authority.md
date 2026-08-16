---
id: GKR-UX-HOME-BUSINESS-NARRATIVE-001
title: Autoridade Narrativa — Home Pública — Guivos Business
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-16
parent: GKR-BUSINESS-CONTINUITY-001
depends_on:
  - GPA-004
  - GKR-BUSINESS-CONTINUITY-001
  - GKR-STATE-001
  - ROADMAP-12.79.0
normative: true
---

# Autoridade Narrativa — Home Pública — Guivos Business

## 1. Finalidade

Este documento registra a **arquitetura narrativa convergida da Home Pública do Guivos Business** após a reconciliação do produto e as validações realizadas em conversa até 2026-08-16.

Ele governa:

- a tese humana que orienta a Home;
- a hierarquia de significado da narrativa;
- a ordem dos movimentos narrativos;
- o papel relativo de Journey, Programas de Incentivo, benefícios, Pontos Guivos, ecossistema e Guivos Intelligence;
- as fronteiras que futuras etapas de copy, conversão, Documento Mestre, Source Lock e Design devem preservar.

Este documento **não é**:

- Documento Mestre da Home;
- Source Lock;
- wireframe;
- UI;
- protótipo;
- handoff para Design;
- contrato final de conversão;
- especificação comercial de preços, limites, SLA ou entitlements.

A progressão governada permanece:

```text
ARQUITETURA NARRATIVA     → CONVERGIDA NESTE DOCUMENTO
→ CONTRATOS DE AUTORIDADE → PRÓXIMA ETAPA
→ CONVERSÃO               → NÃO CONVERGIDA
→ DOCUMENTO MESTRE        → NÃO EXISTE
→ SOURCE LOCK             → NÃO EXISTE
→ somente depois: Design
```

## 2. Relação com a arquitetura funcional do Guivos Business

A arquitetura funcional/comercial de `GPA-004` permanece válida e não é substituída por esta autoridade.

O Guivos Business continua possuindo duas ofertas principais no contrato de produto:

```text
GUIVOS BUSINESS
├── PROGRAMAS DE INCENTIVO
└── GUIVOS JOURNEY CUSTEADO PELA EMPRESA
```

A Home, porém, **não precisa reproduzir a taxonomia comercial como hierarquia narrativa**.

Regra:

> **Arquitetura funcional do produto ≠ ordem de significado da Home.**

Na Home, o Guivos Journey deve aparecer antes dos Programas de Incentivo porque a narrativa é governada pela evolução humana, não pela enumeração das ofertas comerciais.

## 3. Centro narrativo

A decisão principal desta autoridade é:

> **O produto não é o protagonista; a evolução humana é.**

A Home do Guivos Business deve ser narrada a partir do impacto positivo que uma empresa pode exercer ao criar melhores condições para a evolução das pessoas.

Duas expressões complementares são válidas e podem ser utilizadas em diferentes momentos da comunicação:

> **Ajudar seres humanos a terem uma vida melhor.**

> **Apoiar pessoas em sua evolução.**

Elas não são concorrentes.

A primeira expressa a direção humana mais ampla. A segunda expressa o meio pelo qual o Business contribui para essa direção.

A relação conceitual é:

```text
PROPÓSITO NARRATIVO
Ajudar seres humanos a terem uma vida melhor
↓
MEIO
Apoiar pessoas em sua evolução
↓
PRINCÍPIO
Criar condições e possibilidades sem decidir por elas
quem devem se tornar
```

A expressão “vida melhor” pode abranger ser melhor naquilo que a pessoa faz, vive, busca, constrói ou deseja para sua própria vida. Ela **não autoriza** empresa ou Guivos a criar um critério universal de pessoa melhor, score humano, classificação moral ou obrigação de evolução.

## 4. Base conceitual preservada — Checkpoint 2

A base validada anteriormente permanece integralmente vigente.

### 4.1 Tese

> **Quando uma empresa amplia possibilidades para as pessoas, novas possibilidades também se abrem para a própria empresa.**

### 4.2 Protagonista

> **A empresa é o protagonista comercial; as pessoas são o centro humano do valor criado.**

A Home fala com a empresa, mas não reduz pessoas a objeto operacional, mecanismo de produtividade ou métrica empresarial.

### 4.3 Problema

> **Como criar relações mais relevantes, ampliar possibilidades e compreender movimentos sem reduzir pessoas a números, pontos ou mecanismos de controle?**

### 4.4 Promessa

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

### 4.5 Pergunta-mãe

> **O que sua empresa pode tornar possível para as pessoas?**

## 5. Hierarquia de significado

A arquitetura narrativa deve preservar a seguinte hierarquia:

```text
AJUDAR SERES HUMANOS A TEREM UMA VIDA MELHOR
↓
APOIAR PESSOAS EM SUA EVOLUÇÃO
↓
A EMPRESA CRIA CONDIÇÕES
↓
A PESSOA ESCOLHE SEU CAMINHO
↓
GUIVOS JOURNEY
amplia acesso à evolução
↓
RECONHECIMENTO E INCENTIVOS
apoiam e estimulam movimentos legítimos
↓
BENEFÍCIOS
abrem novas possibilidades
↓
ECOSSISTEMA GUIVOS
expande o universo de possibilidades
↓
GUIVOS INTELLIGENCE
ajuda a empresa a compreender movimentos de forma responsável
↓
GUIVOS BUSINESS
organiza essa capacidade em escala
```

Consequências:

1. Journey vem antes de Programas de Incentivo na Home;
2. Programas de Incentivo apoiam a evolução e não dominam a proposta de valor;
3. Pontos Guivos são mecanismo secundário, não narrativa principal;
4. Intelligence fecha um ciclo de compreensão, não transforma a Home em dashboard;
5. planos aparecem somente após a compreensão do propósito e das capacidades;
6. produtos do ecossistema não devem ser apresentados como catálogo antes das possibilidades humanas que viabilizam.

## 6. Arquitetura narrativa convergida — 10 movimentos

### Movimento 01 — O que sua empresa pode tornar possível para as pessoas?

**Função:** abrir pela possibilidade.

Pergunta-mãe:

> **O que sua empresa pode tornar possível para as pessoas?**

Promessa:

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

Este movimento não deve começar por Journey, Incentivos, Pontos, planos, dashboards ou lista de funcionalidades.

### Movimento 02 — Empresas também podem ajudar seres humanos a terem uma vida melhor

**Função:** estabelecer o propósito humano da relação Business.

A empresa pode criar condições, ampliar acesso, reconhecer movimentos, abrir oportunidades e tornar novas possibilidades viáveis.

A Home deve transmitir que empresas podem participar positivamente de histórias de evolução humana sem assumir autoridade sobre a vida das pessoas.

### Movimento 03 — Apoiar a evolução não é escolher o caminho

**Função:** estabelecer autonomia como princípio.

Formulação de referência:

> **Sua empresa pode apoiar a evolução das pessoas sem decidir por elas quem devem se tornar.**

Estrutura:

```text
EMPRESA
cria condições e amplia acesso
↓
GUIVOS
abre caminhos e possibilidades
↓
PESSOA
escolhe o que faz sentido para sua própria vida
```

Assinatura semântica de referência:

> **A empresa apoia. A pessoa escolhe.**

### Movimento 04 — Amplie o acesso à evolução

**Função:** apresentar o Guivos Journey como primeira evidência concreta da tese humana do Business.

Formulação validada:

> **Sua empresa pode oferecer acesso ao Guivos Journey e permitir que seus funcionários encontrem caminhos, experiências e possibilidades de evolução relevantes para suas próprias vidas.**

Princípio complementar:

> **Sua empresa amplia o acesso. Cada pessoa escolhe o próprio caminho.**

Distinção que deve permanecer clara:

```text
JOURNEY B2C
→ a própria pessoa contrata seu acesso

JOURNEY VIA GUIVOS BUSINESS
→ a empresa custeia o acesso para seus funcionários
```

Em ambos os casos continua sendo **Guivos Journey**.

O financiamento empresarial não autoriza:

- Journey corporativa criada pela empresa;
- trilha pessoal controlada pela empresa;
- seleção empresarial dos temas de evolução da pessoa;
- exposição do conteúdo individual da Journey;
- transformação de evolução pessoal em obrigação corporativa.

### Movimento 05 — Reconheça movimentos. Incentive novos passos.

**Função:** introduzir Programas de Incentivo como apoio à evolução e às relações humanas, não como produto protagonista.

Princípio:

> **Reconhecer um movimento positivo também pode ajudar alguém a continuar avançando.**

Podem existir iniciativas legítimas relacionadas, conforme contexto, a exemplos como:

**Funcionários**

- aprendizagem;
- assiduidade;
- segurança;
- participação;
- inovação;
- sustentabilidade;
- reconhecimento;
- metas legítimas;
- conquistas.

**Clientes**

- fidelização;
- recorrência;
- indicação;
- participação;
- relacionamento;
- ativação.

Progressão narrativa:

```text
MOVIMENTO
↓
RECONHECIMENTO
↓
INCENTIVO
↓
NOVA POSSIBILIDADE
```

Evitar como lógica principal:

```text
AÇÃO
↓
GANHE PONTOS
```

### Movimento 06 — Transforme reconhecimento em novas possibilidades

**Função:** mostrar que um benefício pode continuar criando valor depois do reconhecimento inicial.

Formulação de referência:

> **Um incentivo pode fazer mais do que reconhecer o que já aconteceu. Ele também pode abrir o que vem depois.**

Progressão:

```text
RECONHECIMENTO
↓
BENEFÍCIO
↓
ESCOLHA
↓
NOVA POSSIBILIDADE
```

Pontos Guivos podem aparecer apenas como mecanismo secundário, por exemplo:

> **Pontos Guivos podem ser utilizados como uma das formas de acesso a possibilidades elegíveis dentro do ecossistema.**

A Home não deve transformar saldo, lote, validade, liquidação, equivalência econômica, orçamento pré-pago ou checkout em narrativa principal.

Essas regras continuam governadas pela arquitetura funcional/econômica própria do produto.

### Movimento 07 — Uma possibilidade pode levar a muitas outras

**Função:** tornar concreto o efeito de ecossistema sem transformar a Home em catálogo de produtos Guivos.

Direção narrativa:

> **Diferentes áreas da vida. Diferentes possibilidades. Um ecossistema que pode conectá-las.**

Formulação de referência:

> **O que começa como uma oportunidade pode continuar em diferentes áreas da vida.**

A Home deve priorizar **exemplos concretos da vida** antes de listar Journey, Travel ou Mall.

Áreas narrativas possíveis incluem:

```text
VIDA DA PESSOA
├── finanças
├── saúde e bem-estar
├── desenvolvimento
├── viagens e experiências
├── produtos e presentes
├── interesses
├── relações
└── outras possibilidades
```

Exemplos narrativos concretos de referência:

- **Pode começar com o desejo de organizar melhor a vida financeira.** Encontrar caminhos para aprender, planejar e tomar decisões.
- **Pode estar relacionado à saúde e ao bem-estar.** Descobrir possibilidades que ajudem a cuidar melhor de si e da própria qualidade de vida.
- **Pode virar uma viagem ou uma nova experiência.** Conhecer um lugar, viver algo diferente ou ampliar a própria perspectiva.
- **Pode tornar possível algo que a pessoa deseja ou precisa.** Um produto, um presente, uma experiência ou outra possibilidade disponível no ecossistema.
- **Pode ainda revelar um próximo passo que ela nem estava procurando no início.**

Journey, Travel, Mall e outras capacidades do ecossistema podem aparecer como infraestrutura que viabiliza essas possibilidades, mas não devem substituir a vida da pessoa como unidade narrativa principal.

Princípio:

> **A Guivos não determina que tipo de evolução deve acontecer. Ela aumenta o universo de possibilidades a partir do qual cada pessoa pode escolher.**

### Movimento 08 — Compreenda para continuar apoiando melhor

**Função:** apresentar Guivos Intelligence como capacidade de compreensão responsável após participação e movimentos reais.

Pergunta de referência:

> **O que sua empresa pode compreender para criar iniciativas cada vez mais relevantes?**

Leituras elegíveis podem incluir, conforme contrato e autoridade do Intelligence:

- participação;
- utilização;
- recorrência;
- tendências;
- interesses agregados;
- movimentos ao longo do tempo;
- aderências;
- lacunas;
- oportunidades observáveis.

Progressão:

```text
EMPRESA CRIA POSSIBILIDADES
↓
PESSOAS PARTICIPAM
↓
MOVIMENTOS ACONTECEM
↓
GUIVOS INTELLIGENCE
↓
EMPRESA COMPREENDE MELHOR
↓
NOVAS INICIATIVAS PODEM SER CRIADAS
```

Princípio:

> **Compreender não significa vigiar.**

Não expor à empresa Journey individual, score de evolução, vulnerabilidade pessoal, intenção individual ou explicação protegida de relevância.

A integração analítica não constitui movimento narrativo separado. Pode aparecer como extensão positiva do Intelligence:

> **A inteligência gerada na Guivos também pode ser conectada ao ambiente analítico da sua empresa, ampliando a visão sobre suas próprias iniciativas.**

Não utilizar como proposta pública central a formulação defensiva “a Guivos não precisa substituir seus sistemas”.

### Movimento 09 — Da primeira iniciativa à operação em grande escala

**Função:** introduzir a capacidade operacional e comercial somente depois de compreendido o propósito.

Os planos vigentes permanecem:

```text
START
→ Comece a operar

GROWTH
→ Acompanhe e compreenda

SCALE
→ Interprete e integre

ENTERPRISE
→ Governe em alta complexidade e escala
```

Os planos não representam mérito, evolução moral ou qualidade da empresa. Regulam capacidade, escala, Intelligence, integração, governança e serviço conforme contratos futuros.

A Home não deve congelar nesta etapa preços, limites quantitativos, SLA, API, SSO, usuários ou entitlements ainda não formalizados.

### Movimento 10 — Voltar ao que realmente importa

**Função:** fechar retornando à pergunta inicial com significado ampliado.

Pergunta:

> **O que sua empresa pode tornar possível para as pessoas?**

Síntese de referência:

> **Amplie o acesso. Reconheça movimentos. Abra novas possibilidades.**

Síntese humana de referência:

> **Apoie pessoas em sua evolução e ajude seres humanos a terem uma vida melhor.**

Promessa:

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

A conversão comercial final ainda não está congelada por esta autoridade.

## 7. Progressão narrativa consolidada

A sequência semântica é:

```text
POSSIBILIDADE
↓
PROPÓSITO HUMANO
↓
AUTONOMIA
↓
JOURNEY
↓
RECONHECIMENTO E INCENTIVOS
↓
BENEFÍCIOS
↓
POSSIBILIDADES DA VIDA / ECOSSISTEMA
↓
INTELLIGENCE
↓
ESCALA
↓
SÍNTESE E FUTURA CONVERSÃO
```

Os dez movimentos não obrigam dez seções visuais independentes. Design poderá combinar movimentos desde que preserve a progressão semântica, as hierarquias e as fronteiras desta autoridade após Source Lock apropriado.

## 8. Regra específica de Pontos Guivos na Home

Pontos Guivos permanecem funcionalmente válidos e economicamente governados por `GPA-004`, mas **não são a narrativa da Home**.

Regra normativa:

> **Pontos Guivos são mecanismo; evolução humana e novas possibilidades são significado.**

A Home não deve se posicionar como:

- plataforma de pontos;
- programa de rewards genérico;
- cashback corporativo;
- carteira de benefícios como identidade principal;
- sistema em que “mais pontos” significa “mais evolução”.

A complexidade técnica dos Pontos não deve receber peso narrativo proporcional à sua complexidade operacional.

## 9. Fronteiras de posicionamento

A Home Business não deve se converter em:

1. plataforma de RH;
2. LMS/LXP ou universidade corporativa;
3. plataforma de fidelidade/pontos como identidade principal;
4. dashboard empresarial como proposta central;
5. versão empresarial do Journey controlada pela companhia;
6. pacote de Guivos Ads;
7. catálogo de produtos do ecossistema;
8. mecanismo de avaliação da qualidade humana das pessoas;
9. promessa causal não demonstrada de produtividade, retenção, saúde ou performance;
10. instrumento de vigilância individual.

## 10. Relação entre Journey e Incentivos

A ordem narrativa está explicitamente congelada neste checkpoint:

```text
PRIMEIRO
→ EVOLUÇÃO HUMANA
→ AUTONOMIA
→ GUIVOS JOURNEY

DEPOIS
→ RECONHECIMENTO
→ PROGRAMAS DE INCENTIVO
→ BENEFÍCIOS
→ MECÂNICAS COMO PONTOS, QUANDO PERTINENTES
```

Isso não altera a possibilidade comercial de a empresa contratar apenas Programas de Incentivo, apenas acessos Journey ou ambas as ofertas.

## 11. O que permanece aberto

Esta autoridade não congela:

- copy final integral de todos os movimentos;
- CTA principal e secundário;
- experiência de qualificação comercial;
- formulários, etapas ou lógica de conversão;
- Documento Mestre;
- Source Lock;
- arquitetura visual;
- wireframe;
- UI;
- protótipo;
- preços;
- limites quantitativos;
- SLA;
- entitlements finais;
- detalhes operacionais de Points, pagamentos, liquidação ou expiração já governados em outras autoridades.

## 12. Próximo ponto governado

Com a arquitetura narrativa convergida, a próxima etapa da Home Pública do Guivos Business é:

> **CONTRATOS DE AUTORIDADE**

Essa etapa deverá definir, movimento a movimento, o que a Home:

- pode afirmar;
- precisa preservar;
- não pode sugerir;
- deve remeter a autoridades específicas do produto ou ecossistema.

Somente depois devem avançar conversão, Documento Mestre, Source Lock e Design.