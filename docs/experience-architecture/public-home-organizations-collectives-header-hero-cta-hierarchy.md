---
id: GKR-UX-HOME-OC-NAV-001
title: Hierarquia entre Header, Hero e CTAs da Home Pública de Organizações e Coletivos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-11
parent: GKR-UX-HOME-OC-MASTER-001
depends_on:
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-AUDIT-001
  - GKR-UX-HOME-OC-NARR-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-003
  - GKR-UX-HOME-NAV-004
related:
  - GKR-UX-HOME-HANDOFF-001
  - UXA-014
  - UXA-019
normative: false
---

# Hierarquia entre Header, Hero e CTAs da Home Pública de Organizações e Coletivos

## 1. Finalidade

Este documento executa o **P2 da prontidão pré-materialização** da Home Pública de Organizações e Coletivos e resolve em princípio `OC-GAP-02 — Header, Hero e hierarquia de CTAs` identificado por `GKR-UX-HOME-OC-AUDIT-001`.

Ele define o contrato semântico entre:

- o Header global da Guivos;
- o estado de navegação quando o visitante já está em `Organizações e Coletivos`;
- a Hero da segunda Home;
- `Iniciar Jornada`;
- o CTA de descoberta da Hero;
- a bifurcação final Organização / Coletivo;
- o retorno à Home Pública principal;
- o comportamento conceitual em desktop e mobile.

Este documento não define:

- layout;
- pixels;
- grid;
- breakpoint final;
- componente;
- estilo de estado ativo;
- URL;
- autenticação;
- onboarding;
- cadastro;
- planos;
- preços;
- GTM;
- wireframe;
- Figma;
- SVG;
- protótipo;
- UI final;
- implementação;
- UXA-102/V5.

Decisão central:

> **A Home Pública de Organizações e Coletivos pertence à mesma navegação global da Guivos. A Hero conduz compreensão; o Header preserva liberdade de acesso; a bifurcação Organização / Coletivo só assume protagonismo após a narrativa comum.**

---

## 2. Uma Guivos, um Header público global

A segunda Home não deve criar um Header B2B, institucional ou específico para parceiros.

Ela permanece dentro da mesma Guivos e herda, em princípio, o sistema global de navegação pública estabelecido por `GKR-UX-HOME-NAV-001`, `003` e `004`.

Portanto, a arquitetura conceitual continua considerando:

```text
GUIVOS / HOME
SOBRE
ORGANIZAÇÕES E COLETIVOS

COMPARTILHAR
IDIOMA / REGIÃO
LAUNCHER DO ECOSSISTEMA
LOGIN
INICIAR JORNADA
```

A diferença é contextual:

> **na Home Pública principal, `Organizações e Coletivos` é um destino; nesta segunda Home, ele identifica o contexto público atual.**

Isso não exige um segundo sistema de navegação.

---

## 3. Estado atual de `Organizações e Coletivos`

Quando o visitante estiver nesta página, `Organizações e Coletivos` deverá ser semanticamente reconhecível como o contexto atual.

O design futuro poderá materializar esse estado por:

- ênfase;
- indicador;
- tratamento tipográfico;
- estado `aria-current` ou equivalente;
- outra solução acessível e coerente.

Este documento não define a forma visual.

Regras:

1. o item não deve parecer um segundo CTA de conversão;
2. o visitante deve conseguir compreender em qual porta pública está;
3. o estado atual não cria uma submarca;
4. o Header continua sendo Guivos, e não `Guivos Business`;
5. a navegação não deve abrir automaticamente um menu de Organização/Coletivo porque o visitante entrou nesta página.

---

## 4. Retorno à Home Pública principal

A marca Guivos / acesso à Home permanece o caminho primário de retorno à Home Pública principal.

Regra:

> **a segunda Home é uma perspectiva da Guivos, não uma área isolada da qual o visitante precise “sair”.**

Não é necessário criar um botão dominante `Voltar para pessoas` ou equivalente.

A arquitetura deve permitir retorno natural à Home principal pela própria identidade global da marca.

Em mobile, esse caminho precisa permanecer igualmente encontrável.

---

## 5. Função da Hero

A Hero da segunda Home abre a perspectiva compartilhada de Organizações e Coletivos.

Pergunta-mãe vigente:

> **O que podemos tornar possível juntos?**

Essa formulação está suficientemente consolidada para orientar Design, embora lapidação editorial futura continue permitida desde que preserve:

- capacidade;
- possibilidade;
- participação;
- complementaridade;
- abertura;
- ausência de promessa causal;
- ausência de venda imediata.

A Hero precisa fazer o visitante pensar algo próximo de:

> **“Existe uma forma maior de compreender aquilo que nossa Organização ou Coletivo já consegue mobilizar, realizar ou tornar possível.”**

Ela não deve perguntar primeiro:

- `Quer vender mais?`;
- `Quer alcançar usuários?`;
- `Quer anunciar?`;
- `Quer cadastrar sua empresa?`;
- `Quer criar sua comunidade?`;
- `Qual plano deseja contratar?`.

---

## 6. Hero não deve antecipar a bifurcação

A narrativa comum precisa acontecer antes da divisão entre Organização e Coletivo.

Portanto, a hipótese principal rejeita no primeiro viewport dois CTAs dominantes como:

```text
SOU ORGANIZAÇÃO
SOU COLETIVO
```

Razões:

1. o visitante ainda não compreendeu por que ambos pertencem ao mesmo ecossistema;
2. a página perderia sua tese compartilhada;
3. a escolha antecipada transformaria a Home em roteador de segmento;
4. seria maior o risco de Organização = Business;
5. seria maior o risco de Coletivo = comunidade da Guivos;
6. a página se aproximaria de landing pages B2B convencionais.

Regra:

> **primeiro pertencimento ao mesmo ecossistema; depois diferenciação de participação.**

---

## 7. CTA da Hero — função fechada, copy aberta

O CTA primário da Hero possui a mesma natureza de baixo compromisso da Home Pública principal:

> **continuar a descoberta dentro da própria página.**

Sua função é levar o visitante da pergunta de abertura para o reconhecimento de capacidades e iniciativas que já existem.

Territórios de copy elegíveis para exploração posterior incluem:

- `Descubra como isso pode se conectar`;
- `Entenda como podemos participar juntos`;
- `Veja como isso ganha continuidade`;
- `Explore essa possibilidade`;
- formulações equivalentes.

Nenhuma dessas redações é copy final.

O CTA da Hero não deve, por padrão:

- abrir cadastro;
- pedir dados;
- solicitar CNPJ ou registro institucional;
- solicitar criação de Coletivo;
- iniciar onboarding;
- abrir Business;
- abrir Ads;
- abrir formulário comercial;
- abrir seleção Organização / Coletivo;
- duplicar os CTAs do Movimento 11.

Destino semântico:

```text
HERO
→ continuidade da própria narrativa
→ Macro 02 — reconhecimento + desconexão
```

O mecanismo material — scroll, anchor, transição ou equivalente — permanece para design e implementação futura.

---

## 8. `Iniciar Jornada` mantém significado global

`Iniciar Jornada` continua pertencendo ao Header global como porta própria da **Guivos Journey**.

Sua semântica não muda porque o visitante está na Home de Organizações e Coletivos.

Regra obrigatória:

> **`Iniciar Jornada` não significa cadastrar Organização, cadastrar Coletivo, contratar Business ou iniciar onboarding institucional.**

A presença desse CTA protege uma característica essencial do ecossistema:

> uma pessoa continua sendo Pessoa mesmo quando chega à Guivos representando, criando ou participando de uma Organização ou Coletivo.

Assim, quem deseja iniciar sua própria Journey continua tendo esse caminho disponível.

---

## 9. Prevenção de ambiguidade de `Iniciar Jornada`

Nesta segunda Home existe um risco específico:

> um visitante pode interpretar `Iniciar Jornada` como `começar a jornada da minha Organização ou Coletivo`.

A futura materialização precisa reduzir essa ambiguidade sem redefinir o CTA global.

Pode fazê-lo por contexto, arquitetura de informação, rótulo acessível, destino inequívoco ou solução equivalente.

Não está autorizado neste documento:

- renomear `Iniciar Jornada` para `Cadastrar Organização`;
- trocar o CTA global por `Participar como Organização`;
- trocar o CTA global por `Criar Coletivo`;
- remover Journey do Header apenas porque a página tem outro protagonista inicial.

Teste obrigatório:

> **um visitante deve conseguir distinguir `iniciar minha Journey` de `descobrir como minha Organização ou Coletivo participa`.**

---

## 10. Relação Hero × Header no primeiro viewport

A hierarquia perceptiva conceitual deve ser:

```text
1. pergunta / mensagem da Hero
2. compreensão breve do território de Organizações e Coletivos
3. continuidade de descoberta da Hero
4. disponibilidade persistente de `Iniciar Jornada` no Header
5. demais acessos globais e utilitários
```

`Iniciar Jornada` pode continuar sendo o CTA de maior hierarquia **dentro do Header**, sem superar a Hero como foco dominante da página.

Regra:

> **a hierarquia global do Header não pode sequestrar a hierarquia narrativa da segunda Home.**

---

## 11. Não criar CTA comercial concorrente na Hero

A Hero não deve possuir um CTA comercial paralelo como:

- `Fale com vendas`;
- `Solicite demonstração`;
- `Conheça os planos`;
- `Anuncie agora`;
- `Cadastre sua empresa`.

Essas possibilidades poderão existir em jornadas posteriores quando houver fundamento de produto, oferta e GTM.

Na Home pública compartilhada, antecipá-las criaria uma leitura incorreta:

```text
Organizações e Coletivos
=
público pagador / canal comercial
```

A página precisa primeiro explicar participação, complementaridade, valor e confiança.

---

## 12. Inventário do Header nesta página

Em princípio, permanece o mesmo inventário global.

### Identidade e institucional

- Guivos / Home;
- Sobre;
- Organizações e Coletivos — contexto atual.

### Ecossistema e utilidades

- Compartilhar;
- Idioma / Região;
- launcher do ecossistema;
- Login;
- Iniciar Jornada.

Não é necessário adicionar ao Header público desta página:

- `Organização`;
- `Coletivo`;
- `Planos`;
- `Preços`;
- `Parceiros`;
- `Anunciantes`;
- `Empresas`;
- `ONGs`;
- `Instituições`;
- `Cadastrar`.

Esses itens, se um dia existirem, dependerão de necessidade governada posterior.

---

## 13. Launcher do ecossistema

O launcher mantém a mesma semântica global:

> **acesso rápido a ambientes conhecidos da Guivos.**

O inventário vigente continua:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey permanece fora do launcher e utiliza `Iniciar Jornada` como porta própria.

Nesta segunda Home, uma proteção adicional é necessária:

> **a presença de Business ou Ads no launcher não deve fazer o visitante concluir que esses produtos definem a participação de Organizações.**

Launcher é navegação.

Movimento 10 é explicação estrutural.

Movimento 11 é continuidade de participação.

São funções diferentes.

---

## 14. Login

`Login` continua significando retomada de uma relação já existente com a Guivos.

A Home de Organizações e Coletivos não deve presumir, neste estágio, se o login abrirá:

- contexto pessoal;
- seletor de Organização;
- seletor de Coletivo;
- área institucional;
- outro ambiente autenticado.

Essa decisão pertence às experiências autenticadas e à implementação.

Regra pública:

> **Login permanece acesso; não se torna CTA narrativo.**

---

## 15. Compartilhar e idioma/região

Compartilhar e idioma/região permanecem utilidades globais.

A segunda Home não cria regras próprias incompatíveis com a Home principal.

Idioma e região continuam distintos.

A região selecionada não equivale a conhecimento pessoal sobre o visitante nem autoriza inferência sobre a Organização ou Coletivo representado.

---

## 16. Comportamento persistente durante scroll

A segunda Home herda o princípio de `GKR-UX-HOME-NAV-004`:

> **o Header permanece disponível sem permanecer dominante.**

Ele pode compactar durante a narrativa.

Não deve:

- desaparecer completamente como padrão;
- aumentar pressão comercial durante a rolagem;
- transformar `Iniciar Jornada` em banner sticky;
- mudar de arquitetura a cada macroexperiência;
- trocar o Header global por um Header de produto ao chegar ao Movimento 10;
- exibir progressivamente botões `Organização` / `Coletivo` antes do fechamento.

A bifurcação final pertence ao conteúdo da página, não ao comportamento oportunista do Header.

---

## 17. Relação com as sete macroexperiências próprias

O Header atravessa as sete macroexperiências definidas por `GKR-UX-HOME-OC-NARR-001` sem pertencer a nenhuma delas:

1. Abrir o campo de possibilidades;
2. Reconhecer o que já existe e perceber a desconexão;
3. Entender a Guivos e quem participa;
4. Perceber complementaridade e ampliar os contextos;
5. Compreender valor, diversidade e escala;
6. Encontrar confiança e compreender as capacidades da Guivos;
7. Escolher como continuar participando.

A orientação permanece estável enquanto o significado evolui.

---

## 18. Quando a bifurcação pode ganhar protagonismo

A separação Organização / Coletivo torna-se ação dominante somente no **Movimento 11 / Macro 07**, após o visitante compreender:

- por que a página existe;
- o problema da fragmentação;
- o papel da Guivos;
- os três tipos estruturais de participantes;
- complementaridade;
- múltiplos contextos de evolução;
- circulação de valor;
- escala responsável;
- confiança;
- capacidades do ecossistema.

Somente então a pergunta muda de:

> `O que podemos tornar possível juntos?`

para:

> `Como você participa?`

---

## 19. CTAs finais — função

Os dois caminhos finais possuem função equivalente e não devem sugerir hierarquia de importância entre Organização e Coletivo.

### Organização

Significado vigente:

> **Descobrir como participar como Organização.**

### Coletivo

Significado vigente:

> **Descobrir como participar como Coletivo.**

A copy pode ser lapidada posteriormente.

A função não pode mudar para:

- contratar;
- comprar;
- cadastrar imediatamente;
- criar conta obrigatoriamente;
- solicitar proposta como único caminho;
- entrar em Business automaticamente;
- criar comunidade dentro da Guivos.

---

## 20. Destino semântico dos CTAs finais

Os CTAs finais abrem **jornadas públicas específicas de compreensão e participação**.

Arquitetura conceitual:

```text
HOME PÚBLICA — ORGANIZAÇÕES E COLETIVOS
                ↓
        narrativa compartilhada
                ↓
       M11 — COMO PARTICIPAR?
          ↙             ↘
 ORGANIZAÇÃO            COLETIVO
     ↓                    ↓
jornada pública       jornada pública
específica            específica
     ↓                    ↓
adesão / cadastro / operação somente quando aplicável e governado
```

Não é necessário definir a URL desses destinos para liberar futura exploração conceitual de wireframe.

---

## 21. Igualdade de dignidade entre os dois caminhos

A futura materialização não deve tratar:

- Organização como caminho principal e Coletivo como secundário;
- Coletivo como caminho social e Organização como caminho comercial;
- Organização como pagador e Coletivo como beneficiário;
- um dos dois como extensão do outro.

Regra:

> **os participantes possuem naturezas estruturais distintas, mas igual legitimidade dentro do ecossistema.**

A forma visual pode variar conforme clareza, mas não pode introduzir hierarquia de dignidade não governada.

---

## 22. A Pessoa continua presente sem terceiro CTA final

A ausência de um terceiro CTA `Pessoa` no fechamento não exclui a Pessoa do ecossistema.

A razão é arquitetural:

- a Home Pública principal já é a porta predominante da perspectiva da Pessoa;
- `Iniciar Jornada` permanece disponível globalmente;
- esta segunda Home aprofunda especificamente Organização e Coletivo.

Portanto, o fechamento não deve virar:

```text
Pessoa | Organização | Coletivo
```

porque isso dissolveria a função específica desta página.

---

## 23. Mapa de intenções

A página deve permitir distinguir as seguintes intenções:

| Intenção | Caminho conceitual |
|---|---|
| Quero entender esta perspectiva da Guivos | Hero → continuar descoberta |
| Quero voltar à Home principal | Guivos / Home |
| Quero iniciar minha própria Journey | `Iniciar Jornada` |
| Já possuo relação com a Guivos | `Login` |
| Quero acessar um produto conhecido | launcher |
| Quero conhecer a instituição Guivos | `Sobre` |
| Quero ajustar idioma/região | controle global |
| Quero compartilhar esta página | compartilhar |
| Quero entender como minha Organização participa | narrativa → CTA final Organização |
| Quero entender como meu Coletivo participa | narrativa → CTA final Coletivo |

Esses caminhos não devem aparecer com o mesmo peso visual.

---

## 24. Hierarquia de ação ao longo da página

### Macro 01 — Hero

Ação dominante:

> continuar descobrindo.

### Macros 02 a 05

Ação dominante:

> compreender a narrativa.

CTAs contextuais podem existir futuramente apenas quando não substituírem a sequência comum.

### Macro 06 — confiança + capacidades

Ação dominante:

> compreender substância e coerência.

Produtos podem ter acessos contextuais, mas não devem sequestrar a preparação para participação.

### Macro 07 — participação

Ação dominante:

> escolher qual jornada pública de participação aprofundar: Organização ou Coletivo.

---

## 25. CTAs contextuais intermediários

A futura página pode possuir links contextuais de baixo peso quando houver necessidade legítima, por exemplo para:

- conhecer uma evidência;
- entender um princípio de confiança;
- aprofundar uma capacidade do ecossistema.

Mas esses acessos não podem:

- criar uma terceira narrativa paralela;
- transformar cada macroexperiência em bloco de conversão;
- antecipar a escolha Organização / Coletivo;
- interromper a compreensão comum;
- produzir pressão comercial crescente.

Regra:

> **persistência do Header reduz a necessidade de repetir ações globais dentro do conteúdo.**

---

## 26. Desktop

No desktop, a segunda Home pode preservar diretamente o inventário amplo do Header global.

A materialização futura deverá equilibrar:

- Hero dominante;
- contexto atual de `Organizações e Coletivos` compreensível;
- `Iniciar Jornada` disponível sem confusão;
- launcher reconhecível como ecossistema;
- Login acessível;
- utilidades secundárias;
- ausência de navegação B2B adicional.

A composição material permanece para Design.

---

## 27. Mobile

Mobile preserva a mesma arquitetura de intenção.

Não cria uma segunda lógica de participação.

Requisitos:

1. Guivos / Home permanece diretamente encontrável;
2. `Iniciar Jornada` continua reconhecível como ação global;
3. deve existir acesso claro à navegação restante;
4. `Organizações e Coletivos` precisa estar reconhecível como contexto atual na primeira superfície de navegação quando não couber diretamente;
5. Login, launcher e idioma/região permanecem a no máximo uma camada clara de navegação, em princípio;
6. a Hero continua dominando a entrada;
7. não transformar a primeira tela em seletor Organização / Coletivo;
8. os dois CTAs finais permanecem equivalentes em significado mesmo que sua composição responsiva seja sequencial.

Regra:

> **mobile condensa navegação; não condensa a tese.**

---

## 28. Acessibilidade do estado atual

O contexto atual não pode depender somente de:

- cor;
- sublinhado decorativo;
- animação;
- posição visual implícita.

A futura implementação precisa fornecer semântica acessível equivalente a `página atual` quando aplicável.

Também deve preservar:

- navegação por teclado;
- foco visível;
- ordem compreensível;
- nomes acessíveis de controles;
- retorno de foco em superfícies abertas;
- contraste adequado.

---

## 29. Relação com UXA-015 e UXA-016

Os wireframes autenticados de Organização e Coletivo não governam o Header desta Home pública.

Portanto:

```text
Header público da Guivos
≠
Header da Visão Geral da Organização
≠
Header do Início do Coletivo
```

A página pública ainda não possui autoridade representada, unidade selecionada, papel autenticado ou governança operacional ativa.

Esses estados somente pertencem aos ambientes autenticados apropriados.

---

## 30. Anti-padrões específicos

Rejeitar proposta futura que:

- crie Header `Para Empresas` separado;
- substitua a marca Guivos por Guivos Business;
- transforme `Organizações e Coletivos` em menu de produtos;
- coloque `Organização` e `Coletivo` como dois botões dominantes na Hero;
- transforme `Iniciar Jornada` em onboarding institucional;
- remova Journey do Header sem decisão arquitetural superior;
- faça `Business` parecer destino obrigatório de Organizações;
- faça `Coletivo` abrir criação de comunidade sem contexto;
- use CTA `Acesse nossos usuários`;
- use CTA `Venda mais` como ação principal;
- repita CTAs comerciais em todas as macros;
- esconda a Home principal como se o visitante tivesse mudado de produto;
- transforme mobile em menu corporativo completamente diferente.

---

## 31. Matriz de decisão

| Elemento | Estado no P2 |
|---|---|
| Mesmo Header global da Guivos | DECIDIDO EM PRINCÍPIO |
| `Organizações e Coletivos` como contexto atual | DECIDIDO EM PRINCÍPIO |
| Guivos / Home como retorno à Home principal | DECIDIDO |
| Pergunta `O que podemos tornar possível juntos?` | DECIDIDO COM LAPIDAÇÃO POSTERIOR |
| Função da Hero | DECIDIDA |
| CTA da Hero = continuar descoberta | DECIDIDO EM PRINCÍPIO |
| Copy final do CTA da Hero | PARA COPY |
| Bifurcação na Hero | REJEITADA |
| `Iniciar Jornada` = Journey | DECIDIDO |
| `Iniciar Jornada` = cadastro de Organização/Coletivo | REJEITADO |
| Launcher global | HERDADO |
| Login global | HERDADO |
| Persistência do Header | HERDADA |
| CTAs finais Organização / Coletivo | DECIDIDOS EM FUNÇÃO |
| URLs dos CTAs finais | ETAPA POSTERIOR |
| Igualdade de hierarquia semântica entre Organização e Coletivo | DECIDIDA |
| Composição visual desktop | PARA DESIGN |
| Composição visual mobile | PARA DESIGN dentro das regras |

---

## 32. Testes de aderência

Uma futura proposta de materialização deve responder `sim` a estas perguntas:

1. O visitante percebe que continua dentro da mesma Guivos?
2. O Header parece global, e não B2B?
3. A Hero domina o primeiro viewport?
4. `Organizações e Coletivos` está reconhecível como contexto atual?
5. A Hero abre possibilidade antes de pedir segmentação?
6. O CTA da Hero continua a descoberta em vez de converter?
7. Organização e Coletivo permanecem unidos durante a narrativa comum?
8. `Iniciar Jornada` continua significando Journey?
9. É difícil confundir `Iniciar Jornada` com cadastro institucional?
10. Business permanece apenas um produto do ecossistema?
11. A bifurcação só ganha protagonismo no final?
12. Organização e Coletivo possuem igual dignidade na escolha final?
13. A Pessoa continua com acesso global sem virar terceiro CTA desta página?
14. O mobile preserva a mesma arquitetura de intenção?
15. O visitante consegue retornar à Home principal sem esforço?
16. Login e launcher permanecem acessos, não narrativa?
17. O Header não aumenta pressão comercial durante scroll?
18. A página poderia funcionar sem qualquer CTA comercial?

Falha material nesses testes exige revisão antes de wireframe governado.

---

## 33. Resultado do P2

Com este documento, `OC-GAP-02` passa de bloqueador aberto para:

> **RESOLVIDO EM PRINCÍPIO — FUNÇÃO E HIERARQUIA DEFINIDAS; MATERIALIZAÇÃO VISUAL PERMANECE ABERTA.**

Ainda permanecem bloqueadores de pré-materialização:

- **P3 / OC-GAP-03 — Conteúdo, prova e evidência por movimento**;
- **P4 / OC-GAP-04 — Handoff específico para Design/UX/UI**;
- **P5 — Reauditoria final de prontidão**.

Nenhuma decisão deste P2 autoriza wireframe.

---

## 34. Síntese de controle

```text
HEADER GLOBAL
→ Guivos permanece Guivos
→ acesso e liberdade persistem

HERO
→ O que podemos tornar possível juntos?
→ continuar descobrindo

NARRATIVA COMUM
→ compreender antes de segmentar

INICIAR JORNADA
→ Journey
→ não onboarding institucional

MOVIMENTO 11
→ Como você participa?
→ Organização | Coletivo
→ jornadas públicas específicas
```

Formulação final:

> **Nesta segunda Home, o Header preserva a liberdade de navegar pela Guivos, a Hero abre a pergunta compartilhada e a página conquista o direito de separar Organização e Coletivo somente depois de explicar por que ambos pertencem ao mesmo ecossistema.**
