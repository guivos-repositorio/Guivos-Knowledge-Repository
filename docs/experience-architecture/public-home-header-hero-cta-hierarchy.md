---
id: GKR-UX-HOME-NAV-003
title: Hierarquia entre Header Persistente, Hero e CTAs da Home Pública
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-NAV-002
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-002
  - GKR-UX-HOME-NAV-004
  - GKR-UX-HOME-GTM-BOUNDARY-001
normative: false
---

# Hierarquia entre Header Persistente, Hero e CTAs da Home Pública

## 1. Finalidade

Este documento refina a arquitetura da Home pública de `guivos.com` para distinguir com precisão:

- a função do **Header Persistente**;
- a função narrativa da **Hero**;
- o papel de `Iniciar Jornada`;
- o papel do CTA de descoberta da Hero;
- a relação entre Login, launcher, acessos institucionais e continuidade narrativa;
- a hierarquia de intenção do primeiro viewport.

A finalidade é evitar que a Home apresente dois ou mais CTAs com significado concorrente logo na entrada.

Este documento não define URL, implementação, onboarding, autenticação, disponibilidade operacional, estratégia de lançamento ou Marketing/GTM.

O comportamento de persistência, compactação, scroll e mobile do Header é aprofundado por `GKR-UX-HOME-NAV-004`.

---

## 2. Decisão central

A Home possui duas camadas de ação com responsabilidades diferentes:

```text
HEADER PERSISTENTE
→ oferece caminhos permanentes e decisões já conhecidas

HERO
→ inicia a narrativa e convida a continuar descobrindo
```

Na hipótese principal vigente:

> **`Iniciar Jornada` pertence ao Header Persistente como porta própria da Journey.**

> **A Hero possui função de descoberta e continuidade da própria Home; ela não deve duplicar `Iniciar Jornada` como CTA principal.**

Essa separação preserva a lógica de que a Home deve ser compreendida antes de exigir que o visitante escolha um caminho de maior compromisso.

---

## 3. Dois estados legítimos do visitante

O primeiro viewport deve atender simultaneamente a dois estados legítimos sem misturá-los.

### Estado A — ainda estou entendendo

A pessoa chegou para descobrir:

- o que é a Guivos;
- o que existe aqui;
- por que o ecossistema existe;
- o que pode se tornar possível.

A continuidade adequada é a própria narrativa da Home.

### Estado B — já quero avançar

A pessoa já compreendeu, já conhece a Guivos ou chegou com intenção explícita de começar sua jornada.

A continuidade adequada é `Iniciar Jornada` no Header.

Regra:

> **A Home não deve obrigar quem já decidiu a percorrer toda a narrativa; também não deve obrigar quem ainda está entendendo a iniciar uma jornada.**

---

## 4. Função do Header Persistente

O Header é uma camada permanente de orientação e acesso.

Ele responde:

> **“Se eu já sei o que quero fazer, onde está o caminho?”**

Na arquitetura vigente, ele contém conceitualmente:

- Guivos / Home;
- `Sobre`;
- `Organizações e Coletivos`;
- compartilhar;
- idioma/região por globo;
- launcher do ecossistema por grade de pontos;
- `Login`;
- `Iniciar Jornada`.

O Header não deve tentar contar a história da Home.

Ele deve permanecer suficientemente simples para não competir com a Hero.

Regra complementar de comportamento:

> **O Header permanece disponível sem permanecer dominante; ele pode compactar durante a rolagem, mas não deve desaparecer completamente como comportamento padrão.**

---

## 5. Função da Hero

A Hero é a abertura narrativa da Home.

Ela responde:

> **“Por que eu deveria continuar olhando?”**

Seu sistema semântico permanece:

1. `O que se torna possível quando você entra aqui?`
2. `Um mundo maior de possibilidades passa a fazer parte do seu.`
3. explicação breve do papel da Guivos conectando pessoas, organizações, conhecimento, oportunidades e experiências.

A ação da Hero deve estar alinhada a esse estado de compreensão inicial.

Por isso, sua função comportamental primária é:

> **continuar descobrindo.**

---

## 6. CTA da Hero — função fechada, copy aberta

O significado do CTA da Hero fica definido em princípio como:

> **continuar a descoberta dentro da própria Home.**

Territórios de copy elegíveis para exploração futura incluem, sem aprovação de redação final:

- `Descubra a Guivos`;
- `Explore possibilidades`;
- `Comece a explorar`;
- `Veja o que existe aqui`;
- outras formulações equivalentes de baixo compromisso e alta continuidade.

A copy final permanece para etapa posterior.

O CTA da Hero não deve, por padrão:

- exigir login;
- iniciar onboarding;
- pedir dados pessoais;
- abrir um produto específico;
- abrir o launcher;
- levar diretamente a Travel, Mall, Business, Media, Intelligence ou Ads;
- duplicar `Iniciar Jornada`;
- criar urgência comercial.

Seu destino semântico é o aprofundamento da narrativa pública, especialmente a passagem da Hero para o território de **Possibilidades Reais**.

O mecanismo material — scroll, anchor, transição ou solução equivalente — permanece para design/implementação futura.

---

## 7. `Iniciar Jornada` — função no Header

`Iniciar Jornada` permanece como CTA de maior hierarquia **dentro do Header**.

Sua função é:

- oferecer uma porta persistente para a Journey;
- atender quem já possui intenção de avançar;
- permanecer disponível enquanto a pessoa percorre a Home;
- evitar que a narrativa precise repetir chamadas de conversão em todos os movimentos.

Regra:

> **o visitante pode descobrir pela Hero e iniciar pela Journey quando estiver pronto; a Home não precisa escolher por ele o momento dessa transição.**

A presença persistente de `Iniciar Jornada` não autoriza nesta frente definir:

- URL;
- autenticação;
- onboarding;
- captura de contexto;
- fluxo posterior;
- disponibilidade operacional;
- regra de lançamento.

Durante a rolagem, sua disponibilidade pode permanecer constante sem que sua pressão visual aumente.

---

## 8. Não duplicar `Iniciar Jornada` na Hero

Na hipótese principal, a Hero **não repete** `Iniciar Jornada` como seu CTA dominante.

Razões:

1. o Header já mantém essa ação permanentemente disponível;
2. a Hero tem função de abrir horizonte, não de antecipar compromisso;
3. dois CTAs equivalentes gerariam competição de intenção;
4. a repetição reduziria a distinção entre `descobrir a Guivos` e `entrar na Journey`;
5. a Home perderia parte da progressão `curiosidade → compreensão → confiança → decisão`;
6. a página poderia se aproximar de uma landing page de conversão convencional.

Formalização:

> **Hero = descoberta. Header = acesso persistente à Journey.**

---

## 9. Uma ação dominante por camada

Não existe uma única ação “primária” para toda a Home independentemente do contexto.

A hierarquia é contextual:

### Dentro da Hero

A ação dominante é **continuar descobrindo**.

### Dentro do Header

A ação de maior hierarquia é **Iniciar Jornada**.

### Dentro do launcher

A função é **acessar diretamente um ambiente conhecido do ecossistema**.

### Login

A função é **retomar uma relação existente**.

### Sobre / Organizações e Coletivos

A função é **aprofundamento institucional**.

Essa separação evita que todos os caminhos sejam tratados visualmente como conversões equivalentes.

---

## 10. Hierarquia perceptiva do primeiro viewport

Sem determinar layout, o primeiro viewport deve preservar aproximadamente esta prioridade de atenção:

```text
1. mensagem da Hero
2. compreensão / possibilidade
3. continuidade de descoberta da Hero
4. disponibilidade persistente de Iniciar Jornada no Header
5. demais acessos de navegação e utilidade
```

`Iniciar Jornada` pode ser o CTA mais destacado do Header sem se tornar o elemento visual dominante da página inteira.

A tese da Hero continua sendo o principal foco perceptivo da entrada.

Regra:

> **hierarquia do Header não pode sequestrar a hierarquia narrativa da Hero.**

---

## 11. Mapa de intenções do primeiro viewport

A arquitetura deve permitir os seguintes caminhos sem ambiguidade:

| Intenção | Caminho conceitual |
|---|---|
| Quero entender o que é a Guivos | Hero → continuar descoberta |
| Quero começar minha jornada | `Iniciar Jornada` |
| Já tenho conta / quero retornar | `Login` |
| Já sei qual produto procuro | launcher do ecossistema |
| Quero conhecer a empresa | `Sobre` |
| Sou Organização ou Coletivo / quero entender esse papel | `Organizações e Coletivos` |
| Quero ajustar idioma ou região | globo |
| Quero compartilhar a Guivos | compartilhar |

O visitante não deve precisar interpretar todos esses caminhos antes de compreender a Hero.

---

## 12. Efeito da persistência sobre a narrativa

Como `Iniciar Jornada` permanece disponível no Header enquanto a pessoa percorre a Home, a narrativa não precisa repetir a mesma chamada em cada movimento.

Isso permite:

- menos ruído;
- menos pressão comercial;
- mais espaço para histórias e evidências;
- CTAs contextuais coerentes com cada conteúdo;
- maior sensação de controle;
- decisão de entrada na Journey no tempo do visitante.

Regra:

> **persistência deve reduzir repetição, não aumentar pressão.**

O comportamento material de persistência segue `GKR-UX-HOME-NAV-004`.

---

## 13. Relação com os CTAs contextuais

Os movimentos da Home podem possuir CTAs contextuais quando houver fundamento semântico.

Exemplos conceituais:

- história → aprofundar história;
- conteúdo → continuar conteúdo;
- experiência → conhecer contexto;
- produto no Movimento 08 → aprofundar manifestação do ecossistema.

Esses CTAs não devem competir com a função permanente de `Iniciar Jornada`.

Eles continuam o contexto que a pessoa está vendo naquele momento.

> **CTA contextual = continuidade do conteúdo atual.**

> **Iniciar Jornada = decisão transversal disponível durante toda a Home.**

---

## 14. Relação com o Movimento 11 — Descoberta

O Movimento 11 continua governado pela função de **abrir continuidade**, não de encerrar a Home como uma página de venda.

A presença persistente de `Iniciar Jornada` permite que o fechamento mantenha linguagem de descoberta sem obrigação de converter o visitante para Journey.

A forma material e a copy do CTA final permanecem abertas para etapa posterior.

O Movimento 11 não deve contradizer a autonomia construída ao longo da página.

---

## 15. Mobile e responsividade — equivalência semântica

A futura solução mobile pode reorganizar ou condensar controles, mas deve preservar:

- acesso à Home;
- compreensão da Hero;
- continuidade de descoberta;
- encontrabilidade de `Iniciar Jornada`;
- encontrabilidade de Login;
- acesso ao launcher do ecossistema;
- acesso a idioma/região;
- acesso institucional essencial.

A arquitetura não exige que todos os elementos permaneçam simultaneamente visíveis em uma única linha no mobile.

Ela exige equivalência de função e hierarquia.

`GKR-UX-HOME-NAV-004` acrescenta que caminhos condensados devem permanecer, em regra, a uma camada de navegação de distância e que launcher e eventual menu geral não devem se tornar semanticamente indistinguíveis.

---

## 16. Anti-padrões

Rejeitar ou revisar uma proposta se:

1. a Hero usa `Iniciar Jornada` como botão dominante enquanto o mesmo CTA já está permanentemente destacado no Header, sem justificativa forte;
2. a Hero oferece três ou mais CTAs de igual peso;
3. Login compete com `Iniciar Jornada`;
4. launcher compete visualmente com a mensagem da Hero;
5. o Header vira catálogo de produtos;
6. a pessoa precisa escolher produto antes de compreender a Guivos;
7. o CTA de descoberta exige cadastro;
8. o CTA de descoberta abre fluxo de Journey sem comunicar essa mudança de intenção;
9. o Header ocupa atenção maior que a tese da Hero;
10. a persistência é usada para repetir pressão comercial durante o scroll;
11. a versão mobile remove ou esconde de forma imprevisível a principal continuidade;
12. a página repete `Iniciar Jornada` em múltiplos movimentos sem função nova;
13. o Header desaparece completamente durante longos trechos como comportamento padrão;
14. a compactação move alvos de forma imprevisível;
15. launcher e menu geral mobile parecem o mesmo controle apesar de terem funções diferentes.

---

## 17. Critérios de aceitação

A relação Header/Hero é aderente quando:

- a pessoa entende a mensagem antes de sentir pressão para agir;
- existe um caminho claro para continuar explorando a Home;
- `Iniciar Jornada` permanece encontrável para quem já decidiu;
- descoberta e início de Journey possuem intenções diferentes;
- Login é claramente utilitário;
- launcher é claramente acesso ao ecossistema, não explicação da marca;
- nenhuma ação exige que o visitante revele contexto para compreender a Home;
- a persistência do Header reduz repetição de CTAs;
- a tese da Hero domina perceptivamente o primeiro viewport;
- mobile preserva a mesma arquitetura de intenção;
- Header pode compactar sem desaparecer nem aumentar pressão perceptiva.

---

## 18. Liberdade de design preservada

Este documento não define:

- posição em pixels;
- altura do Header;
- cor do CTA;
- formato do botão;
- ícone específico;
- animação;
- breakpoint;
- label final do CTA de descoberta;
- microcopy;
- abertura do launcher;
- estado autenticado;
- destino operacional de `Iniciar Jornada`.

O comportamento conceitual de scroll, compactação e mobile é governado por `GKR-UX-HOME-NAV-004`; sua materialização técnica e visual permanece aberta.

---

## 19. Síntese de controle

Arquitetura de ação do primeiro viewport:

```text
HEADER PERSISTENTE
├── Sobre
├── Organizações e Coletivos
├── Compartilhar
├── Idioma / Região
├── Launcher
│   ├── Travel
│   ├── Ads
│   ├── Media
│   ├── Business
│   ├── Intelligence
│   └── Mall
├── Login
└── Iniciar Jornada
    └── porta própria da Journey

HERO
├── pergunta-mãe
├── amplitude / pertencimento
├── concretização do papel da Guivos
└── CTA de descoberta
    └── continua a própria Home
```

Regra final:

> **A Hero deve fazer a pessoa querer continuar entendendo; o Header deve permitir que ela aja quando já souber o que quer fazer.**
