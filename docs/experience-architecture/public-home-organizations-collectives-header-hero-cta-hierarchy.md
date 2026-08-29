---
id: GKR-UX-HOME-OC-NAV-001
title: Hierarquia entre Header, Hero e CTAs da Home Pública de Organizações e Coletivos
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-29
parent: GKR-UX-HOME-OC-MASTER-001
depends_on:
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-NARR-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-003
  - GKR-UX-HOME-NAV-004
related:
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOME-OC-AUDIT-001
  - GKR-UX-HOME-HANDOFF-001
  - UXA-014
  - UXA-019
normative: false
maturity: reconciled_navigation_detail_pre_materialization
---

# Hierarquia entre Header, Hero e CTAs da Home Pública de Organizações e Coletivos

## 1. Finalidade e função atual

Este documento nasceu como o **P2 da prontidão pré-materialização** da Home Pública de Organizações e Coletivos e, naquele checkpoint, resolveu em princípio `OC-GAP-02 — Header, Hero e hierarquia de CTAs` identificado por `GKR-UX-HOME-OC-AUDIT-001`.

Depois da reconstrução documental de `GKR-UX-HOME-OC-MASTER-001 v1.0.0` e da reconciliação narrativa de `GKR-UX-HOME-OC-NARR-001 v0.2.0`, sua função atual é preservar e aprofundar o **contrato especializado de navegação, Hero e hierarquia de ação** da Home O/C, sem competir com o Documento Mestre como autoridade de consumo vigente.

Ele preserva detalhe próprio sobre:

- o Header global da Guivos;
- o estado de navegação quando o visitante já está em `Organizações e Coletivos`;
- a Hero desta perspectiva pública;
- `Iniciar Jornada`;
- o CTA de descoberta da Hero;
- a bifurcação final Organização / Coletivo;
- o retorno à Home Pública principal;
- o comportamento conceitual em desktop e mobile;
- acessibilidade e prevenção de ambiguidades de intenção.

Estado de autoridade:

```text
GKR-UX-HOME-OC-MASTER-001 v1.0.0
→ autoridade de consumo vigente da Home O/C

GKR-UX-HOME-OC-NAV-001 v0.2.0
→ detalhe especializado reconciliado de navegação / Hero / CTAs
→ não autoriza materialização
```

Este documento não define nem autoriza:

- layout;
- pixels;
- grid;
- breakpoint final;
- componente;
- estilo visual de estado ativo;
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
- UXA-102/V5;
- retomada de Product Engineering.

Durante a auditoria integral:

```text
DETALHE NAVEGACIONAL RECONCILIADO
≠ DESIGN VIGENTE
≠ WIREFRAME AUTORIZADO
≠ UI APROVADA
≠ IMPLEMENTAÇÃO AUTORIZADA
```

Decisão central preservada:

> **A Home Pública de Organizações e Coletivos pertence à mesma navegação global da Guivos. A Hero conduz compreensão; o Header preserva liberdade de acesso; a bifurcação Organização / Coletivo só assume protagonismo após a narrativa comum.**

---

## 2. Uma Guivos, um Header público global

A Home O/C não deve criar um Header B2B, institucional ou específico para parceiros.

Ela permanece dentro da mesma Guivos e herda semanticamente o sistema global de navegação pública estabelecido por `GKR-UX-HOME-NAV-001`, `003` e `004`, sempre interpretado sob a autoridade atual do Master O/C e sob o bloqueio de materialização da auditoria integral.

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

> **na Home Pública principal, `Organizações e Coletivos` é um destino; nesta Home, ele identifica o contexto público atual.**

Isso não exige um segundo sistema de navegação.

---

## 3. Estado atual de `Organizações e Coletivos`

Quando o visitante estiver nesta página, `Organizações e Coletivos` deverá ser semanticamente reconhecível como o contexto atual.

Se uma materialização visual vier a ser explicitamente autorizada por ato governado posterior à auditoria integral, esse estado poderá ser expresso por solução como:

- ênfase;
- indicador;
- tratamento tipográfico;
- estado `aria-current` ou equivalente;
- outra solução acessível e coerente.

Nenhuma dessas possibilidades define agora a forma visual.

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

> **a Home O/C é uma perspectiva da Guivos, não uma área isolada da qual o visitante precise “sair”.**

Não é necessário criar um botão dominante `Voltar para pessoas` ou equivalente.

A arquitetura deve permitir retorno natural à Home principal pela própria identidade global da marca.

Em mobile, esse caminho precisa permanecer igualmente encontrável.

---

## 5. Função da Hero

A Hero da Home O/C abre a perspectiva compartilhada de Organizações e Coletivos.

Pergunta-mãe vigente:

> **O que podemos tornar possível juntos?**

Essa formulação permanece semanticamente consolidada pelo Master vigente. Lapidação editorial futura continua possível somente se preservar:

- capacidade;
- possibilidade;
- participação;
- complementaridade;
- abertura;
- ausência de promessa causal;
- ausência de venda imediata.

A eventual lapidação de copy não constitui autorização atual de Design ou materialização.

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

Territórios de copy elegíveis para lapidação futura incluem:

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
- solicitar localização;
- solicitar criação de Coletivo;
- ativar voz ou microfone;
- ativar câmera;
- solicitar upload ou arquivo;
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

Scroll, anchor, transição ou mecanismo equivalente permanecem indefinidos. O contrato semântico deste CTA não autoriza sua materialização durante a auditoria integral.

---

## 8. `Iniciar Jornada` mantém significado global

`Iniciar Jornada` continua pertencendo ao Header global como porta própria da **Guivos Journey — Experience Layer**.

Sua semântica não muda porque o visitante está na Home de Organizações e Coletivos.

Regra obrigatória:

> **`Iniciar Jornada` não significa cadastrar Organização, cadastrar Coletivo, contratar Business ou iniciar onboarding institucional.**

A presença desse CTA protege uma característica essencial do ecossistema:

> uma pessoa continua sendo Pessoa mesmo quando chega à Guivos representando, criando ou participando de uma Organização ou Coletivo.

Assim, quem deseja iniciar sua própria Journey continua tendo esse caminho disponível.

---

## 9. Prevenção de ambiguidade de `Iniciar Jornada`

Nesta Home existe um risco específico:

> um visitante pode interpretar `Iniciar Jornada` como `começar a jornada da minha Organização ou Coletivo`.

Qualquer materialização futura, se vier a ser explicitamente autorizada, deverá reduzir essa ambiguidade sem redefinir o CTA global.

Isso poderá ocorrer por contexto, arquitetura de informação, rótulo acessível, destino inequívoco ou solução equivalente, sem que este documento escolha agora a solução material.

Não está autorizado:

- renomear `Iniciar Jornada` para `Cadastrar Organização`;
- trocar o CTA global por `Participar como Organização`;
- trocar o CTA global por `Criar Coletivo`;
- remover Journey do Header apenas porque a página tem outro protagonista inicial.

Teste obrigatório preservado:

> **um visitante deve conseguir distinguir `iniciar minha Journey` de `descobrir como uma Organização ou Coletivo pode participar`.**

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

> **a hierarquia global do Header não pode sequestrar a hierarquia narrativa da Home O/C.**

---

## 11. Não criar CTA comercial concorrente na Hero

A Hero não deve possuir um CTA comercial paralelo como:

- `Fale com vendas`;
- `Solicite demonstração`;
- `Conheça os planos`;
- `Anuncie agora`;
- `Cadastre sua empresa`.

Esses caminhos somente podem existir futuramente quando houver fundamento de produto, oferta, GTM, disponibilidade operacional e autorização governada específica.

Na Home pública compartilhada, antecipá-los criaria uma leitura incorreta:

```text
OrganIZAÇÕES E COLETIVOS
=
público pagador / canal comercial
```

A página precisa primeiro explicar participação, complementaridade, valor e confiança.

---

## 12. Inventário do Header nesta página

Permanece o mesmo inventário global de referência.

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

Esses itens, se um dia vierem a existir como navegação pública, dependerão de necessidade e autorização governadas posteriores.

---

## 13. Launcher do ecossistema

O launcher mantém a mesma semântica global:

> **acesso rápido a ambientes conhecidos da Guivos.**

O inventário conceitual vigente continua:

- Guivos Travel;
- Guivos Ads;
- Guivos Media;
- Guivos Business;
- Guivos Intelligence;
- Guivos Mall.

Esses seis destinos pertencem à família de **Produtos Especializados**. `Guivos Intelligence` é, adicionalmente, o **Produto Especializado transversal / Intelligence Layer** do ecossistema.

`Guivos Journey` permanece fora do launcher porque é a **Experience Layer** e utiliza `Iniciar Jornada` como porta própria no Header.

Nesta Home, uma proteção adicional é necessária:

> **a presença de Business ou Ads no launcher não deve fazer o visitante concluir que esses produtos definem a participação de Organizações.**

```text
LAUNCHER
→ navegação para Produtos Especializados

MOVIMENTO 10
→ explicação estrutural das camadas e Produtos

MOVIMENTO 11
→ continuidade conceitual de participação
```

São funções diferentes.

Presença conceitual no launcher não equivale a disponibilidade operacional, publicação ou decisão de lançamento.

---

## 14. Login

`Login` continua significando retomada de uma relação já existente com a Guivos.

A Home de Organizações e Coletivos não deve presumir, neste estágio, se o login abrirá:

- contexto pessoal;
- seletor de Organização;
- seletor de Coletivo;
- área institucional;
- outro ambiente autenticado.

Essa decisão pertence às experiências autenticadas e à implementação governada futura.

Regra pública:

> **Login permanece acesso; não se torna CTA narrativo.**

---

## 15. Compartilhar e idioma/região

Compartilhar e idioma/região permanecem utilidades globais.

A Home O/C não cria regras próprias incompatíveis com a Home principal.

Idioma e região continuam distintos.

A região selecionada não equivale a conhecimento pessoal sobre o visitante nem autoriza inferência sobre a Organização ou Coletivo representado.

---

## 16. Comportamento persistente durante scroll

A Home O/C herda o princípio de `GKR-UX-HOME-NAV-004`:

> **o Header permanece disponível sem permanecer dominante.**

Conceitualmente, ele pode compactar durante a narrativa quando houver materialização futuramente autorizada.

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

O Header atravessa as sete macroexperiências definidas por `GKR-UX-HOME-OC-NARR-001 v0.2.0` sem pertencer a nenhuma delas:

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

A separação Organização / Coletivo torna-se ação dominante somente no **Movimento 11 / Macro 07**, após o visitante compreender, em nível público:

- por que a página existe;
- o problema da fragmentação e da falta de contexto suficiente;
- o papel da Guivos;
- os três tipos estruturais de participantes;
- complementaridade sem match fabricado;
- os nove Domínios de Evolução como vocabulário canônico, sem taxonomia visual obrigatória;
- a distinção `Possibilidade ≠ Oportunidade` e o papel de Mecanismo quando necessário;
- circulação de valor e supply;
- escala responsável;
- confiança por autoridade, evidência e proteção;
- capacidades e camadas do ecossistema.

Somente então a pergunta pode mudar da abertura compartilhada para a continuidade de participação.

No Master vigente, o fechamento é formulado como:

> **Como podemos continuar daqui?**

A pergunta histórica `Como você participa?` permanece como evidência da intenção original de bifurcação, mas não substitui a formulação vigente do Master.

---

## 19. CTAs finais — função

Os dois caminhos finais possuem função equivalente e não devem sugerir hierarquia de importância ou legitimidade entre Organização e Coletivo.

### Organização

Significado vigente:

> **Descobrir como uma Organização pode participar.**

### Coletivo

Significado vigente:

> **Descobrir como um Coletivo pode participar.**

A copy pode ser lapidada posteriormente por frente governada apropriada.

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

Os CTAs finais representam **dois caminhos conceituais distintos de continuidade de participação**.

Arquitetura vigente:

```text
HOME PÚBLICA — ORGANIZAÇÕES E COLETIVOS
                ↓
        narrativa compartilhada
                ↓
       M11 — continuidade
          ↙             ↘
 ORGANIZAÇÃO            COLETIVO
     ↓                    ↓
continuidade          continuidade
conceitual própria    conceitual própria
```

Esses caminhos permanecem conceituais até que destinos operacionais sejam formalmente autorizados e comprovados.

Eles não definem agora:

- URL;
- cadastro;
- adesão;
- onboarding;
- operação;
- tela autenticada;
- Business;
- formulário comercial;
- fluxo técnico posterior.

A experiência autenticada posterior, quando vier a ser materializada e autorizada, preservará arquitetura própria. Seus jobs, autoridade, IA, superfícies e wireframes não são transportados para esta Home.

---

## 21. Igualdade de dignidade entre os dois caminhos

Qualquer materialização futura, se autorizada, não deve tratar:

- Organização como caminho principal e Coletivo como secundário;
- Coletivo como caminho social e Organização como caminho comercial;
- Organização como pagador e Coletivo como beneficiário;
- um dos dois como extensão do outro.

Regra:

> **os participantes possuem naturezas estruturais distintas, mas igual legitimidade dentro do ecossistema.**

A eventual forma visual pode variar conforme clareza, mas não pode introduzir hierarquia de dignidade não governada.

---

## 22. A Pessoa continua presente sem terceiro CTA final

A ausência de um terceiro CTA `Pessoa` no fechamento não exclui a Pessoa do ecossistema.

A razão é arquitetural:

- a Home Pública principal já é a porta predominante da perspectiva da Pessoa;
- `Iniciar Jornada` permanece disponível globalmente;
- esta Home aprofunda especificamente Organização e Coletivo.

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
| Quero acessar um Produto Especializado conhecido | launcher |
| Quero conhecer a instituição Guivos | `Sobre` |
| Quero ajustar idioma/região | controle global |
| Quero compartilhar esta página | compartilhar |
| Quero entender como uma Organização pode participar | narrativa → continuidade final Organização |
| Quero entender como um Coletivo pode participar | narrativa → continuidade final Coletivo |

Esses caminhos não devem aparecer com o mesmo peso perceptivo.

---

## 24. Hierarquia de ação ao longo da página

### Macro 01 — Hero

Ação dominante:

> continuar descobrindo.

### Macros 02 a 05

Ação dominante:

> compreender a narrativa.

Acessos contextuais somente podem existir quando preservarem a sequência comum e forem posteriormente autorizados para a materialização correspondente.

### Macro 06 — confiança + capacidades

Ação dominante:

> compreender substância, autoridade e coerência.

Produtos podem existir como destinos conceituais governados, mas não devem sequestrar a preparação para participação.

### Macro 07 — participação

Ação dominante:

> reconhecer qual continuidade conceitual aprofundar: Organização ou Coletivo.

---

## 25. CTAs contextuais intermediários

Em uma materialização futuramente autorizada, a página poderá possuir links contextuais de baixo peso quando houver necessidade legítima, por exemplo para:

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

A existência desta regra não autoriza agora a criação desses CTAs.

---

## 26. Desktop

A arquitetura desktop deve preservar a possibilidade de acesso direto ao inventário amplo do Header global, sem transformar a barra em catálogo ou portal corporativo.

Se a materialização vier a ser autorizada, deverá equilibrar:

- Hero dominante;
- contexto atual de `Organizações e Coletivos` compreensível;
- `Iniciar Jornada` disponível sem confusão;
- launcher reconhecível como acesso aos Produtos Especializados;
- Login acessível;
- utilidades secundárias;
- ausência de navegação B2B adicional.

A composição material não é definida nem autorizada por este documento.

---

## 27. Mobile

Mobile preserva a mesma arquitetura de intenção, mas é uma **solução semântica própria**, não simples empilhamento do desktop.

Não cria uma segunda lógica de participação.

Requisitos semânticos para eventual materialização autorizada:

1. Guivos / Home permanece diretamente encontrável;
2. `Iniciar Jornada` continua reconhecível como ação global e porta da Journey;
3. deve existir acesso claro à navegação restante;
4. `Organizações e Coletivos` precisa estar reconhecível como contexto atual na primeira superfície de navegação quando não couber diretamente;
5. Login, launcher e idioma/região permanecem a no máximo uma camada clara de navegação, em princípio;
6. a Hero continua dominando a entrada;
7. não transformar a primeira tela em seletor Organização / Coletivo;
8. os dois caminhos finais permanecem equivalentes em significado mesmo que sua futura composição responsiva seja sequencial;
9. launcher e eventual menu geral não devem se tornar semanticamente indistinguíveis.

Regra:

> **mobile condensa navegação; não condensa a tese.**

---

## 28. Acessibilidade do estado atual

O contexto atual não pode depender somente de:

- cor;
- sublinhado decorativo;
- animação;
- posição visual implícita.

Se houver implementação futuramente autorizada, ela deverá fornecer semântica acessível equivalente a `página atual` quando aplicável.

Também deverá preservar:

- navegação por teclado;
- foco visível;
- ordem compreensível;
- nomes acessíveis de controles;
- retorno de foco em superfícies abertas;
- contraste adequado;
- comportamento compreensível com `prefers-reduced-motion` ou equivalente;
- conteúdo essencial independente de hover, gesto complexo ou mídia rica.

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

```text
VERDADE PÚBLICA SOBRE AUTORIDADE
≠ ARQUITETURA DA INFORMAÇÃO AUTENTICADA
≠ RBAC
≠ MENU INTERNO
```

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
- transforme mobile em menu corporativo completamente diferente;
- exija dados pessoais, localização, voz/microfone, câmera ou upload para compreender a Hero ou continuar a narrativa pública;
- transporte menus, papéis, RBAC ou superfícies autenticadas para o Header público.

---

## 31. Matriz de decisão vigente

| Elemento | Estado vigente |
|---|---|
| Mesmo Header global da Guivos | PRESERVADO / HERDADO |
| `Organizações e Coletivos` como contexto atual | DECIDIDO |
| Guivos / Home como retorno à Home principal | DECIDIDO |
| Pergunta `O que podemos tornar possível juntos?` | VIGENTE NO MASTER |
| Função da Hero | DECIDIDA |
| CTA da Hero = continuar descoberta | DECIDIDO |
| Copy final do CTA da Hero | ABERTA; NÃO MATERIALIZADA |
| Bifurcação na Hero | REJEITADA |
| `Iniciar Jornada` = Journey / Experience Layer | DECIDIDO |
| `Iniciar Jornada` = cadastro de Organização/Coletivo | REJEITADO |
| Launcher de Produtos Especializados | HERDADO |
| Login global | HERDADO |
| Persistência do Header | HERDADA |
| Continuidade final Organização / Coletivo | DECIDIDA EM FUNÇÃO CONCEITUAL |
| Destinos operacionais dos caminhos finais | NÃO DEFINIDOS / NÃO AUTORIZADOS |
| Igual legitimidade entre Organização e Coletivo | DECIDIDA |
| Composição visual desktop | NÃO MATERIALIZADA / NÃO AUTORIZADA |
| Composição visual mobile | NÃO MATERIALIZADA / NÃO AUTORIZADA |
| Wireframe / Figma / SVG / protótipo / UI | BLOQUEADOS DURANTE A AUDITORIA INTEGRAL |

---

## 32. Testes de aderência

Qualquer materialização futura, somente se vier a ser explicitamente autorizada após os gates de governança aplicáveis, deverá responder `sim` a estas perguntas:

1. O visitante percebe que continua dentro da mesma Guivos?
2. O Header parece global, e não B2B?
3. A Hero domina o primeiro viewport?
4. `Organizações e Coletivos` está reconhecível como contexto atual?
5. A Hero abre possibilidade antes de pedir segmentação?
6. O CTA da Hero continua a descoberta em vez de converter?
7. Organização e Coletivo permanecem unidos durante a narrativa comum?
8. `Iniciar Jornada` continua significando Journey?
9. É difícil confundir `Iniciar Jornada` com cadastro institucional?
10. Business permanece apenas um Produto Especializado do ecossistema?
11. A bifurcação só ganha protagonismo no final?
12. Organização e Coletivo possuem igual legitimidade na escolha final?
13. A Pessoa continua com acesso global sem virar terceiro CTA desta página?
14. O mobile preserva a mesma arquitetura de intenção?
15. O visitante consegue retornar à Home principal sem esforço?
16. Login e launcher permanecem acessos, não narrativa?
17. O Header não aumenta pressão comercial durante scroll?
18. A página poderia funcionar sem qualquer CTA comercial?
19. A compreensão pública não exige dados pessoais, localização, voz/microfone, câmera ou upload?
20. Nenhum papel, menu, RBAC ou fluxo autenticado foi transportado para a superfície pública?

Falha material nesses testes exigirá revisão da proposta correspondente. Estes testes não constituem autorização para produzir agora wireframe, Figma, SVG, protótipo, UI ou implementação.

---

## 33. Proveniência histórica e estado atual

No checkpoint original de 11/08/2026, este documento registrou `OC-GAP-02` como:

> **RESOLVIDO EM PRINCÍPIO — FUNÇÃO E HIERARQUIA DEFINIDAS; MATERIALIZAÇÃO VISUAL PERMANECE ABERTA.**

Naquele momento, ainda eram tratados como próximos gates P3, P4 e P5 da antiga sequência de prontidão.

Esse enquadramento é **histórico**, não o estado operacional atual.

Depois das reconstruções e reauditorias posteriores:

```text
P2 / OC-GAP-02
→ proveniência histórica deste detalhe especializado

P3 / P4 / P5
→ não são próximos passos operacionais vigentes deste documento

GKR-UX-HOME-OC-MASTER-001 v1.0.0
→ autoridade de consumo atual

GKR-UX-HOME-OC-NARR-001 v0.2.0
→ detalhe narrativo reconciliado

GKR-UX-HOME-OC-NAV-001 v0.2.0
→ detalhe navegacional reconciliado

AUDITORIA INTEGRAL DO GKR
→ EM CURSO

MATERIALIZAÇÃO VISUAL NOVA
→ NÃO AUTORIZADA
```

Nenhuma decisão preservada deste documento reabre wireframe, Figma, SVG, protótipo, UI, implementação, UXA-102/V5 ou Product Engineering.

---

## 34. Síntese de controle

```text
HEADER GLOBAL
→ Guivos permanece Guivos
→ acesso e liberdade persistem
→ Organizações e Coletivos = contexto atual nesta Home

HERO
→ O que podemos tornar possível juntos?
→ continuar descobrindo
→ sem coleta de contexto pessoal necessária para compreender

NARRATIVA COMUM
→ compreender antes de segmentar
→ nove Domínios como vocabulário, não layout obrigatório
→ Possibilidade ≠ Oportunidade

INICIAR JORNADA
→ Guivos Journey / Experience Layer
→ não onboarding institucional

LAUNCHER
→ Produtos Especializados
→ Travel / Ads / Media / Business / Intelligence / Mall
→ presença conceitual ≠ disponibilidade operacional

MOVIMENTO 11
→ Como podemos continuar daqui?
→ Organização | Coletivo
→ continuidades conceituais distintas
→ igual legitimidade
→ destinos operacionais ainda não definidos
```

Formulação final:

> **Nesta Home, o Header preserva a liberdade de navegar pela mesma Guivos, a Hero abre a pergunta compartilhada e a página conquista o direito de separar Organização e Coletivo somente depois de explicar por que ambos pertencem ao mesmo ecossistema — sem converter esse contrato semântico em autorização de materialização durante a auditoria integral.**
