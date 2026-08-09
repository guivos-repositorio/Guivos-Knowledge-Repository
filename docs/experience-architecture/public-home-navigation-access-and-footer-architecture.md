---
id: GKR-UX-HOME-NAV-001
title: Arquitetura de Navegação, Acessos e Footer da Home Pública
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: GKR-UX-HOME-HANDOFF-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-001
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GEB-P01-F01
  - GEB-P01-F02
  - GEB-P01-F03
  - GEB-P01-F04
  - GEB-P01-F06
normative: false
---

# Arquitetura de Navegação, Acessos e Footer da Home Pública

## 1. Finalidade

Este documento define a arquitetura conceitual de navegação e acesso da Home pública de `guivos.com`.

Ele esclarece como produtos, serviços, páginas institucionais, áreas utilitárias e caminhos de suporte podem permanecer acessíveis sem transformar a Home em catálogo, portal corporativo ou inventário de links.

A decisão central é:

> **disponibilidade de navegação não implica protagonismo narrativo.**

Um produto pode estar acessível desde o primeiro viewport por meio da navegação e, ainda assim, somente receber explicação e destaque institucional quando a narrativa da Home tiver construído contexto suficiente.

Este documento não define layout, posição final, tamanho, comportamento visual específico de dropdown, mega menu, drawer, modal, sticky header ou outro componente.

Ele define função, hierarquia, relação entre caminhos, regras de exposição e critérios para futura materialização.

---

## 2. Escopo estrito

Esta especificação governa somente os elementos de navegação e acesso relacionados à Home pública.

Pode definir acesso para:

- Guivos Journey;
- Guivos Travel;
- Guivos Mall;
- Guivos Media;
- Guivos Business;
- Guivos Intelligence;
- Guivos Ads;
- futuras manifestações oficialmente integradas ao ecossistema;
- Sobre a Guivos;
- propósito, visão e conteúdo institucional;
- Central de Ajuda;
- Fale Conosco;
- Trabalhe Conosco;
- Imprensa;
- Parceiros, quando aplicável;
- páginas legais;
- acessibilidade;
- segurança e privacidade;
- login/entrada para participantes existentes.

Esta especificação não governa os fluxos internos desses destinos.

A existência de um link para Travel não inicia UX de Travel.

A existência de um link para Mall não inicia UX de Mall.

A existência de login não inicia a experiência autenticada.

---

## 3. Dois sistemas coexistentes

A Home possui dois sistemas diferentes e complementares.

### 3.1 Sistema narrativo

Responde progressivamente à pergunta-mãe da Home por meio dos onze movimentos definidos em `GKR-UX-HOME-NARR-001`.

Sua função é fazer o visitante compreender a Guivos.

### 3.2 Sistema de navegação

Permite que visitantes com intenção já formada encontrem diretamente um destino sem precisar percorrer toda a narrativa.

Sua função é orientar e permitir acesso.

Os dois sistemas coexistem.

A pessoa não precisa terminar a narrativa para acessar Guivos Travel.

Ao mesmo tempo, o visitante que ainda não conhece a Guivos não deve ser recebido por uma lista de sete produtos como explicação da marca.

Regra:

> **a narrativa governa significado; a navegação garante liberdade.**

---

## 4. As quatro camadas de acesso

A arquitetura conceitual da Home deve admitir quatro camadas.

### 4.1 Navegação global / Header

Função:

- orientação imediata;
- acesso direto a destinos importantes;
- reconhecimento da arquitetura geral;
- entrada de usuários existentes;
- suporte a visitantes com intenção prévia.

Produtos podem estar acessíveis a partir daqui.

Eles não precisam dominar visualmente o Header.

### 4.2 Acesso contextual ao longo da narrativa

Função:

- transformar conteúdo em continuidade;
- permitir que uma história, oportunidade ou experiência leve naturalmente ao produto ou ambiente correspondente;
- evitar CTAs genéricos.

Exemplos conceituais:

- história de viagem → acesso a Guivos Travel;
- conteúdo editorial → acesso a Guivos Media;
- iniciativa de Organização → acesso ao ambiente institucional aplicável;
- oportunidade comercial ou institucional → acesso ao destino pertinente.

Regra:

> **produto pode aparecer cedo como destino contextual sem precisar aparecer cedo como categoria dominante.**

### 4.3 Movimento 08 — Ecossistema / Produtos

Função:

- apresentar explicitamente a arquitetura de produtos;
- explicar por que existem diferentes manifestações;
- mostrar como elas pertencem à mesma tese;
- permitir acesso direto a cada uma.

É o principal momento de protagonismo institucional dos produtos dentro da narrativa.

### 4.4 Footer / mapa completo

Função:

- oferecer navegação completa;
- suportar tarefas utilitárias;
- expor páginas institucionais, suporte e legal;
- servir de fallback de orientação;
- permitir acesso mesmo quando determinado caminho não merece espaço no Header.

O Footer pode ser mais completo que a navegação principal.

---

## 5. Header — princípio geral

O Header deve equilibrar simplicidade e acessibilidade.

Ele não deve tentar representar toda a estrutura da empresa em uma única linha.

Deve permitir três naturezas de intenção:

1. **entender** — conhecer a Guivos;
2. **descobrir** — explorar o ecossistema e possibilidades;
3. **acessar** — chegar a um produto, suporte ou conta já conhecida.

O Header pode conter agrupadores semânticos em vez de apenas nomes de produtos.

Exemplos de territórios conceituais possíveis:

- Explorar;
- Ecossistema;
- Para Organizações;
- Sobre;
- Ajuda;
- Entrar.

Esses nomes não são copy final aprovada.

---

## 6. Produtos no Header

Guivos Journey, Travel, Mall, Media, Business, Intelligence e Ads podem estar disponíveis desde o primeiro viewport.

A recomendação conceitual é que sejam acessíveis por um agrupador como **Ecossistema**, **Produtos** ou equivalente futuro, em vez de ocupar individualmente toda a navegação principal.

Objetivo:

- garantir descoberta rápida por quem já conhece um produto;
- preservar uma primeira camada simples;
- impedir que a Guivos pareça conglomerado de marcas independentes;
- permitir expansão futura sem aumentar indefinidamente a navegação primária.

Cada produto, quando apresentado na navegação expandida, pode receber uma descrição funcional curta para reduzir dependência do nome de marca.

Exemplo conceitual:

- Guivos Journey — jornada e próximos passos;
- Guivos Travel — viagens e experiências;
- Guivos Mall — produtos e serviços;
- Guivos Media — histórias, conhecimento e conteúdo;
- Guivos Business — Organizações e oportunidades;
- Guivos Intelligence — inteligência e contexto;
- Guivos Ads — mídia e presença.

Essas descrições são placeholders semânticos e deverão ser reconciliadas com os contratos oficiais de cada produto antes da copy final.

---

## 7. Regra de protagonismo dos produtos

A navegação pode tornar os produtos encontráveis imediatamente.

A narrativa só deve torná-los protagonistas após o visitante compreender a ideia maior.

Formalização:

> **acessível desde o início ≠ explicado desde o início ≠ protagonista desde o início.**

A sequência recomendada é:

```text
HEADER
produto encontrável

↓

NARRATIVA
marca e tese compreendidas

↓

MOVIMENTO 08
produto explicado como manifestação do ecossistema
```

---

## 8. Acessos contextuais aos produtos

A Home pode apontar para produtos antes do Movimento 08 quando o acesso nasce naturalmente do conteúdo.

Critérios:

1. existe contexto suficiente;
2. o destino é coerente com o que a pessoa acabou de ver;
3. o CTA não interrompe a narrativa principal;
4. o produto é destino, não explicação da marca;
5. o acesso não cria falsa disponibilidade;
6. o destino operacional existe ou possui estado público legítimo.

Exemplo:

> uma experiência de viagem documentada pode oferecer `Explorar experiências` e conduzir a Travel.

Não é necessário inserir um bloco chamado “Guivos Travel” naquele momento.

---

## 9. Movimento 08 como vitrine institucional do ecossistema

O Movimento 08 possui a função principal de apresentar os produtos de forma estruturada.

Mensagem conceitual:

> **um ecossistema, diferentes formas de tornar possibilidades acessíveis, conectadas e vivíveis.**

Cada produto deve ser apresentado como manifestação da mesma tese, não como negócio independente.

A futura composição pode usar:

- caminhos;
- áreas especializadas;
- narrativas;
- módulos;
- cards;
- outra solução visual.

Nenhum formato está fechado.

O requisito é:

> **a coerência entre os produtos deve ser mais perceptível que a quantidade de produtos.**

---

## 10. Sobre a Guivos

`Sobre` possui relevância institucional suficiente para ser encontrável no Header e no Footer.

Pode futuramente agrupar caminhos como:

- Sobre a Guivos;
- Essência;
- Propósito;
- Missão;
- Visão;
- Princípios;
- Como a Guivos funciona;
- história institucional, quando houver;
- imprensa;
- Trabalhe Conosco.

Não é obrigatório que todos estejam expostos no mesmo nível.

A função é responder a visitantes que chegam com intenção institucional:

> **quem é esta organização e no que acredita?**

---

## 11. Trabalhe Conosco

`Trabalhe Conosco` deve ser encontrável, mas não precisa ocupar espaço nobre da navegação primária.

Destino recomendado conceitualmente:

- dentro de `Sobre` / `Empresa` ou equivalente;
- replicado no Footer.

Justificativa:

- é importante;
- possui intenção específica;
- não define a proposta de valor da Home;
- visitantes interessados sabem procurar em estrutura institucional.

---

## 12. Central de Ajuda

A Central de Ajuda é uma função utilitária.

Ela deve ser facilmente encontrável por participantes existentes e por visitantes com dúvidas, sem competir narrativamente com a tese da Home.

Pode aparecer:

- em área utilitária do Header;
- em menu de suporte;
- obrigatoriamente no Footer;
- em estados específicos quando contexto de ajuda existir.

A nomenclatura futura pode ser:

- Ajuda;
- Central de Ajuda;
- Suporte.

A escolha final pertence à fase de IA/copy.

---

## 13. Fale Conosco

`Fale Conosco` deve ser tratado como caminho institucional/utilitário.

Pode ser agrupado em:

- Ajuda;
- Empresa;
- Footer.

A Home não deve transformar contato em CTA narrativo dominante.

---

## 14. Imprensa

A área de imprensa deve ser encontrável principalmente por usuários com intenção específica.

Destinos preferenciais:

- Sobre / Empresa;
- Footer.

Não precisa ocupar navegação primária isolada.

---

## 15. Páginas legais e confiança

Páginas como:

- Termos de Uso;
- Política de Privacidade;
- Cookies;
- preferências de privacidade;
- acessibilidade;
- segurança;
- outras obrigações legais;

devem estar acessíveis de forma previsível, principalmente no Footer e quando o contexto exigir.

Esses caminhos não precisam ocupar a narrativa principal para comunicar confiança.

Confiança também deve ser percebida pelo comportamento da Home.

---

## 16. Login / Entrar

O acesso para participantes existentes deve permanecer facilmente encontrável.

Regra:

> **usuário existente precisa acessar; visitante novo precisa compreender.**

O login pode ocupar área utilitária do Header sem se tornar o CTA narrativo principal da Hero.

A presença de login não autoriza personalização pública nem inicia fluxo autenticado nesta frente.

---

## 17. Possível taxonomia conceitual do Header

Como hipótese de arquitetura de informação, não como copy ou layout final:

```text
GUIVOS

Explorar
Ecossistema
Para Organizações
Sobre

Ajuda
Entrar
```

Dentro de `Ecossistema`, futuramente:

```text
Journey
Travel
Mall
Media
Business
Intelligence
Ads
```

Dentro de `Sobre`, futuramente:

```text
Sobre a Guivos
Propósito e princípios
Imprensa
Trabalhe Conosco
```

Essa taxonomia deverá ser validada por testes de arquitetura de informação antes de materialização final.

---

## 18. Possível arquitetura conceitual do Footer

O Footer deve funcionar como mapa completo, não apenas repetição do Header.

Estrutura hipotética:

### Guivos

- O que é a Guivos;
- Como funciona;
- propósito;
- possibilidades.

### Ecossistema

- Journey;
- Travel;
- Mall;
- Media;
- Business;
- Intelligence;
- Ads.

### Empresa

- Sobre;
- Trabalhe Conosco;
- Imprensa;
- Parceiros, se houver página própria legítima.

### Suporte

- Central de Ajuda;
- Fale Conosco;
- Acessibilidade;
- Segurança, quando aplicável.

### Legal

- Privacidade;
- Termos;
- Cookies;
- preferências e demais documentos aplicáveis.

### Presença / Social

- canais oficiais legitimamente mantidos.

Nenhum nome ou agrupamento desta seção é copy final.

---

## 19. Footer como fallback de encontrabilidade

Uma página não precisa estar no Header para ser importante.

O Footer permite que caminhos específicos permaneçam previsíveis sem aumentar a carga cognitiva inicial.

Regra:

> **baixo protagonismo não significa baixa encontrabilidade.**

Exemplos típicos:

- Trabalhe Conosco;
- Imprensa;
- Termos;
- Privacidade;
- Acessibilidade.

---

## 20. Navegação desktop e mobile

A hierarquia semântica deve ser equivalente em desktop e mobile.

O mobile pode usar:

- drawer;
- accordions;
- grupos progressivos;
- outra solução apropriada.

Não deve:

- esconder produtos essenciais;
- eliminar caminhos institucionais relevantes;
- inverter hierarquias;
- transformar o menu em lista plana muito extensa;
- exigir precisão motora inadequada;
- depender de hover.

---

## 21. Acessibilidade da navegação

A futura materialização deve assegurar:

- navegação por teclado;
- foco visível;
- labels compreensíveis;
- compatibilidade com leitor de tela;
- estado expandido/recolhido anunciado;
- ordem lógica;
- alvo de toque adequado;
- ausência de dependência exclusiva de hover;
- controle sobre abertura/fechamento;
- retorno de foco adequado.

---

## 22. Comportamento do Header

Este documento não determina se o Header será fixo, sticky, transparente, compacto ou adaptativo.

Qualquer solução futura deverá preservar:

- acesso previsível;
- legibilidade;
- baixo ruído;
- autonomia;
- ausência de mudança inesperada;
- navegação disponível sem bloquear conteúdo.

Um Header pode reduzir visualmente durante scroll, mas não deve ocultar caminhos de forma confusa.

---

## 23. CTA da Hero versus navegação

A navegação e o CTA da Hero possuem funções diferentes.

### Navegação

Atende intenção existente.

Exemplo:

> “Eu já quero Travel.”

### CTA da Hero

Cria continuidade narrativa.

Exemplo conceitual:

> “Quero descobrir.”

O CTA principal da Hero não precisa competir com `Entrar`, `Ajuda` ou acesso direto aos produtos.

---

## 24. CTAs ao longo da Home

CTAs devem nascer do contexto.

Hierarquia:

1. ação principal coerente com o movimento;
2. acesso contextual opcional;
3. navegação global sempre disponível.

Exemplos:

- história → conhecer história completa;
- experiência → explorar experiências;
- ecossistema → conhecer produto;
- autoridade → conhecer evidência/metodologia;
- final → continuar descobrindo.

Evitar repetir o mesmo CTA comercial em todas as seções.

---

## 25. Relação com Pessoas, Organizações e Coletivos

A navegação poderá oferecer caminhos específicos para diferentes participantes quando necessário.

Isso não deve criar três marcas ou três Homes concorrentes.

Regra:

> **uma Home, uma tese, múltiplas portas de aprofundamento.**

Uma área como `Para Organizações` pode existir se houver valor claro e destino legítimo.

Coletivos devem permanecer representados na arquitetura do ecossistema, mesmo que a solução futura não crie item de menu isolado com esse nome.

---

## 26. Internacionalização

A arquitetura deve tolerar:

- nomes maiores em outros idiomas;
- expansão de labels;
- diferentes convenções de navegação;
- domínios ou subdomínios futuros;
- diferenças regulatórias por país;
- páginas legais locais.

O design não deve depender de labels extremamente curtos para funcionar.

---

## 27. SEO e encontrabilidade não devem governar a narrativa

Páginas institucionais, produtos e ajuda podem ser plenamente indexáveis e acessíveis sem ocupar protagonismo na Hero.

SEO não é justificativa suficiente para transformar a Home em catálogo de links ou texto redundante.

Arquitetura de informação e narrativa devem colaborar sem se confundirem.

---

## 28. Anti-padrões

Rejeitar ou revisar uma proposta quando:

1. todos os produtos ocupam a navegação primária individualmente sem necessidade;
2. o Header parece menu de conglomerado;
3. o visitante precisa rolar para encontrar um produto que já conhece;
4. acesso direto a Travel/Mall/Media é removido em nome da narrativa;
5. páginas institucionais importantes ficam escondidas;
6. Ajuda compete com a proposta principal;
7. Trabalhe Conosco ocupa protagonismo indevido;
8. o Footer é incompleto ou decorativo;
9. mobile perde caminhos existentes no desktop;
10. hover é requisito para navegação;
11. mega menu vira catálogo promocional;
12. cada produto usa linguagem visual independente a ponto de fragmentar a marca;
13. login vira CTA principal da Hero;
14. páginas legais são difíceis de encontrar;
15. a Home exige percorrer os 11 movimentos para acessar um destino conhecido.

---

## 29. Critérios de aceitação

Uma futura arquitetura de navegação será considerada aderente quando:

- produtos forem acessíveis imediatamente sem dominar a primeira percepção;
- a marca permanecer maior que a soma dos produtos;
- Sobre for facilmente encontrável;
- Ajuda e login estiverem disponíveis sem disputar a narrativa;
- Trabalhe Conosco e Imprensa forem encontráveis por arquitetura institucional;
- Footer funcionar como mapa completo;
- produtos forem explicados de forma destacada no momento narrativo adequado;
- CTAs contextuais levarem naturalmente a destinos relevantes;
- desktop e mobile preservarem hierarquia;
- a navegação puder crescer sem se tornar inventário;
- nenhuma área pública simular disponibilidade inexistente.

---

## 30. Perguntas obrigatórias de revisão

Antes de aprovar um futuro Header/Footer, responder:

1. Quem já conhece Travel consegue acessá-lo rapidamente?
2. Quem nunca ouviu falar de Guivos entende a marca antes de ser bombardeado por produtos?
3. A navegação parece uma única empresa/ecossistema?
4. Sobre a Guivos está encontrável?
5. Central de Ajuda está encontrável?
6. Trabalhe Conosco está encontrável sem ocupar protagonismo excessivo?
7. O Footer cobre mapa institucional, suporte e legal?
8. Mobile preserva todos os caminhos necessários?
9. Algum item existe apenas porque concorrentes usam?
10. Algum item de navegação está tentando compensar uma arquitetura narrativa mal resolvida?

---

## 31. Prompt para futura arquitetura de informação

```text
Projete a arquitetura de navegação da Home pública de Guivos.com sem desenhar ainda a interface final.

Princípio obrigatório: disponibilidade de navegação não implica protagonismo narrativo.

A Home precisa permitir acesso imediato a Guivos Journey, Travel, Mall, Media, Business, Intelligence e Ads para quem já sabe onde quer ir, mas esses produtos não podem dominar a primeira percepção da marca.

Organize a navegação de modo progressivo. Considere um agrupador de ecossistema/produtos, caminhos para entender a Guivos, explorar, atender Organizações, acessar ajuda e entrar em uma conta existente.

Sobre a Guivos deve ser facilmente encontrável. Central de Ajuda deve funcionar como utilidade. Trabalhe Conosco e Imprensa podem ficar dentro de estrutura institucional e no Footer. Privacidade, Termos, Cookies, acessibilidade e demais páginas legais devem ser previsíveis e fáceis de localizar.

O Footer deve funcionar como mapa completo da organização e do ecossistema.

Diferencie:
1. navegação global;
2. acessos contextuais ao longo da Home;
3. apresentação institucional dos produtos no Movimento 08;
4. mapa completo no Footer.

Não crie um catálogo de produtos no Header. Não obrigue a pessoa a percorrer a narrativa para acessar um produto conhecido. Preserve a mesma hierarquia semântica em desktop e mobile.

Entregue:
- taxonomia proposta;
- níveis de navegação;
- racional de cada item;
- destinos agrupados;
- Header conceitual;
- Footer conceitual;
- diferenças desktop/mobile;
- riscos;
- itens ainda abertos para teste.
```

---

## 32. Síntese de controle

A arquitetura deve permitir simultaneamente:

> **quem não conhece a Guivos, compreender; quem quer explorar, descobrir; quem já conhece um produto, acessar; quem procura a empresa, encontrar; quem precisa de ajuda, resolver; quem busca informação legal, localizar.**

Sem transformar a Home em inventário.

Regra final:

> **a Home conta uma história enquanto a navegação preserva liberdade.**
