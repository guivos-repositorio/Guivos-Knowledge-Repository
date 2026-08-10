---
id: GKR-UX-HOME-AUDIT-001
title: Auditoria de Completude Pré-Wireframe da Home Pública
status: draft
version: 0.7.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-HANDOFF-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-001
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NARR-002
  - GKR-UX-HOME-NARR-003
  - GKR-UX-HOME-NARR-004
  - GKR-UX-HOME-NARR-005
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-002
  - GKR-UX-HOME-NAV-003
  - GKR-UX-HOME-SYS-001
  - GKR-UX-HOME-BENCH-001
  - GKR-UX-HOME-BENCH-002
  - GKR-UX-HOME-GTM-BOUNDARY-001
normative: false
---

# Auditoria de Completude Pré-Wireframe da Home Pública

## 1. Objetivo

Esta auditoria verifica se a documentação da Home pública possui definição estratégica suficiente para uma futura materialização conceitual sem obrigar designers, equipes ou ferramentas generativas a reinventar decisões de marca e experiência.

A auditoria não autoriza wireframe, Figma, UI, protótipo ou implementação.

Ela também não audita prontidão de lançamento, disponibilidade operacional dos produtos ou estratégia de Marketing/GTM.

Classificações:

- **DECIDIDO** — direção suficientemente consolidada;
- **DECIDIDO EM PRINCÍPIO** — arquitetura/semântica definida, com materialização ainda aberta;
- **DECIDIDO COM LAPIDAÇÃO POSTERIOR** — significado preservado, copy ou forma ainda aberta;
- **PODE SER RESOLVIDO DURANTE DESIGN** — liberdade legítima da futura etapa visual;
- **FORA DO ESCOPO / ETAPA POSTERIOR** — não deve bloquear o wireframe conceitual.

---

## 2. Resultado executivo

Estado geral:

> **A HOME ESTÁ ESTRATEGICAMENTE MADURA PARA UMA FUTURA EXPLORAÇÃO CONTROLADA DE WIREFRAME, MAS ESSA MATERIALIZAÇÃO AINDA DEPENDE DE AUTORIZAÇÃO EXPLÍCITA.**

Já estão suficientemente consolidados:

- posicionamento;
- tese da Hero;
- arquitetura narrativa;
- onze movimentos;
- distinção entre Realidade e Autoridade;
- agrupamento de referência em sete macroexperiências;
- transição entre Pertencimento e Ecossistema/Produtos;
- hierarquia interna do Movimento 08;
- conteúdo e prova;
- interação e ritmo;
- percepção visual;
- Header Persistente em princípio;
- launcher do ecossistema em princípio;
- separação da Journey em relação ao launcher;
- hierarquia Header × Hero × CTAs;
- acesso de Organizações e Coletivos;
- idioma/região;
- link `Mapa do Ecossistema` no rodapé;
- limites de autonomia, privacidade e não simulação.

A arquitetura distingue explicitamente:

```text
Pessoa / Organização / Coletivo
= quem participa

Journey / Travel / Mall / Media / Business / Intelligence / Ads
= como o ecossistema ganha forma e capacidade
```

A principal fronteira de escopo permanece:

> **disponibilidade de produtos no lançamento, páginas do lançamento, idiomas/regiões do lançamento e demais decisões de GTM não são requisitos da arquitetura conceitual da Home.**

Esses temas pertencem à futura estratégia de Marketing/GTM e aos gates de publicação/produção, conforme `GKR-UX-HOME-GTM-BOUNDARY-001`.

Conclusão:

> **estratégia suficientemente definida para futura materialização conceitual; lançamento e GTM permanecem deliberadamente fora desta frente.**

---

## 3. Decisões consolidadas

### 3.1 Posicionamento — DECIDIDO

A Home deve transmitir:

- futuro;
- possibilidade;
- simplicidade;
- confiança;
- humanidade;
- sofisticação sem complexidade;
- tecnologia sem frieza;
- escala global;
- ecossistema maior que a soma de seus produtos.

### 3.2 Pergunta-mãe — DECIDIDO COM LAPIDAÇÃO POSTERIOR

> **O que se torna possível quando você entra aqui?**

É a direção principal da Hero.

### 3.3 Sistema semântico da Hero — DECIDIDO COM LAPIDAÇÃO POSTERIOR

Camadas conceituais:

1. `O que se torna possível quando você entra aqui?`;
2. `Um mundo maior de possibilidades passa a fazer parte do seu.`;
3. `A Guivos conecta pessoas, organizações, conhecimento, oportunidades e experiências para tornar novos caminhos mais visíveis e possíveis.`

A futura copy pode lapidar redação, mas não remover o significado validado.

### 3.4 Assinatura `Do possível ao vivido` — DECIDIDO

Território complementar de prova, experiência e continuidade.

### 3.5 Cinco pilares — DECIDIDO

- possibilidade;
- pertencimento;
- conexão;
- realidade;
- autonomia.

### 3.6 Cadeia conceitual — DECIDIDO

`ENTRAR → AMPLIAR → DESCOBRIR → CONECTAR → ESCOLHER → EXPERIMENTAR → EVOLUIR`.

### 3.7 Onze movimentos narrativos — DECIDIDO

1. Hero;
2. Possibilidades Reais;
3. Amplitude;
4. Desconexão;
5. Guivos / Conexão;
6. Do Possível ao Vivido;
7. Pertencimento;
8. Ecossistema / Produtos;
9. Autoridade;
10. Autonomia e Confiança;
11. Descoberta.

### 3.8 Onze movimentos não equivalem a onze blocos visuais — DECIDIDO

Regra:

> **Os onze movimentos governam a progressão de significado; a Home não precisa materializá-los como onze blocos separados.**

### 3.9 Mapa de sete macroexperiências — DECIDIDO EM PRINCÍPIO

`GKR-UX-HOME-NARR-005` define a hipótese principal de agrupamento:

1. **Abrir o Horizonte** — Movimento 01;
2. **Ver o Real e Perceber a Amplitude** — Movimentos 02 + 03;
3. **Perceber a Desconexão e Entender o Papel da Guivos** — Movimentos 04 + 05;
4. **Ver o Possível Virar Experiência e Perceber Quem Faz Acontecer** — Movimentos 06 + 07;
5. **Compreender a Coerência do Ecossistema** — Movimento 08;
6. **Encontrar Substância sem Perder Autonomia** — Movimentos 09 + 10;
7. **Reabrir o Horizonte para a Descoberta** — Movimento 11.

Regra sintética:

> **Onze funções. Sete macroexperiências de referência. Uma única narrativa.**

Sete macroexperiências não significam sete seções técnicas obrigatórias. O design decide sua materialização espacial, não reinventa livremente o agrupamento estratégico.

### 3.10 Distinção Movimento 02 × Movimento 09 — DECIDIDO EM PRINCÍPIO

`GKR-UX-HOME-NARR-004` governa:

> **Movimento 02 prova que o universo de possibilidades é real. Movimento 09 prova que a Guivos possui substância, método e responsabilidade para atuar nesse universo.**

Regra curta:

> **02 = “isso existe”. 09 = “há razões para confiar em como a Guivos lida com isso”.**

A mesma fonte pode apoiar ambos, mas o mesmo bloco de conteúdo não deve ser repetido de forma idêntica.

### 3.11 Produtos subordinados à ideia maior — DECIDIDO

Produtos não dominam a abertura da Home.

### 3.12 Acesso e protagonismo são dimensões diferentes — DECIDIDO

> **acessível desde o início ≠ explicado desde o início ≠ protagonista desde o início.**

### 3.13 Header Persistente — DECIDIDO EM PRINCÍPIO

A arquitetura atual considera:

- Guivos / Home;
- `Sobre`;
- `Organizações e Coletivos`;
- compartilhar;
- idioma/região por globo;
- launcher do ecossistema por grade de pontos;
- `Login`;
- `Iniciar Jornada` como CTA de maior hierarquia e porta própria da Journey.

Layout, espaçamento, ordem material final, responsividade e tratamento visual permanecem para a futura etapa de design.

### 3.14 Launcher do Ecossistema — DECIDIDO EM PRINCÍPIO

Inventário conceitualmente aprovado nesta fase:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey não integra o launcher na hipótese principal atual.

### 3.15 Journey no Header — DECIDIDO EM PRINCÍPIO

> **Journey permanece parte do ecossistema, mas sua porta principal no Header é `Iniciar Jornada`, e não o launcher.**

Journey continua podendo aparecer no Movimento 08 e em acessos contextuais quando houver fundamento legítimo.

### 3.16 Participantes no Header — DECIDIDO EM PRINCÍPIO

A Pessoa é atendida naturalmente pela própria Home e por `Iniciar Jornada`.

Organizações e Coletivos recebem uma única porta dedicada de aprofundamento.

A página de destino permanece fora desta frente.

### 3.17 Idioma e região — DECIDIDO EM PRINCÍPIO

Existe controle compacto no Header, conceitualmente representado por globo.

Idioma e região são preferências distintas.

A superfície de seleção será materializada futuramente.

### 3.18 Compartilhar — DECIDIDO EM PRINCÍPIO

Existe intenção de controle utilitário de compartilhamento no Header.

Comportamento técnico não é definido nesta frente.

### 3.19 Mapa do Ecossistema — DECIDIDO NO LIMITE DESTA FRENTE

> **Nesta fase, `Mapa do Ecossistema` é somente um link no rodapé.**

A página, sua arquitetura, categorias, conteúdo e acessos internos ficam fora da frente atual.

### 3.20 Header × Hero × CTAs — DECIDIDO EM PRINCÍPIO

A relação de intenção fica definida:

> **Hero = descoberta e continuidade narrativa. Header = acesso persistente à Journey por `Iniciar Jornada`.**

A Hero não duplica `Iniciar Jornada` como CTA dominante na hipótese principal.

A copy final e a forma material do CTA de descoberta permanecem abertas.

### 3.21 Movimento 07 → 08 — DECIDIDO EM PRINCÍPIO

A transição entre pertencimento e produtos está definida por `GKR-UX-HOME-NARR-003`.

Regra:

> **Participantes respondem “quem”. Produtos e capacidades respondem “como”.**

A Home não deve criar correspondência automática:

```text
Pessoa → Journey
Organização → Business
Coletivo → produto específico
```

Consequências:

- Pessoa não é sinônimo de Journey;
- Organização não é sinônimo de Business;
- Coletivo mantém papel estrutural sem depender de produto homônimo;
- um mesmo participante pode se relacionar com diferentes capacidades conforme contexto;
- produtos materializam capacidades e não classificam participantes.

Regra de sequência:

> **Pertencimento primeiro. Materialização depois. Segmentação por produto, nunca.**

### 3.22 Movimento 08 — hierarquia do ecossistema — DECIDIDO EM PRINCÍPIO

A hierarquia narrativa é governada por `GKR-UX-HOME-NARR-002`:

- Journey — experiência e continuidade;
- Travel, Mall, Media, Business e Ads — manifestações especializadas;
- Intelligence — inteligência transversal.

Regra:

> **O Movimento 08 não é uma vitrine de produtos. É uma explicação da coerência do ecossistema.**

### 3.23 Sistema de conteúdo — DECIDIDO

Classes:

- institucional permanente;
- evidência real;
- editorial;
- ecossistema;
- navegação/ação.

### 3.24 Hierarquia de prova — DECIDIDO

Prova direta > história documentada > evidência institucional > métrica > depoimento > afirmação institucional.

### 3.25 Modelo das histórias — DECIDIDO

Contexto → possibilidade → decisão → experiência → consequência → continuidade.

### 3.26 Conteúdo vivo sem feed — DECIDIDO

Camadas permanente, editorial e temporal.

### 3.27 Guivos Media como fonte editorial futura — DECIDIDO CONCEITUALMENTE

Não existe autorização de integração técnica nesta frente.

### 3.28 Interação e movimento — DECIDIDO EM PRINCÍPIO

Movimento deve revelar, conectar e dar continuidade sem substituir clareza.

### 3.29 Autonomia do scroll — DECIDIDO

Nenhuma experiência pode obrigar o visitante a assistir animações ou aguardar narrativa bloqueante.

### 3.30 Desktop/mobile — DECIDIDO EM PRINCÍPIO

Mesma tese e hierarquia; composição pode variar.

### 3.31 Percepção visual — DECIDIDO

> **Futuro sem ficção. Tecnologia sem frieza. Sofisticação sem elitismo. Escala sem ruído. Humanidade sem clichê.**

### 3.32 Acessibilidade e resiliência — DECIDIDO EM PRINCÍPIO

A experiência deve funcionar com:

- teclado;
- leitor de tela;
- foco visível;
- redução de movimento;
- mídia indisponível;
- baixa conectividade;
- responsividade;
- internacionalização.

### 3.33 Anti-padrões — DECIDIDO

Existe repertório de rejeição narrativa, editorial, visual, interativa e de navegação.

---

## 4. Decisões que podem ser resolvidas durante design/copy

### DESIGN-01 — composição material do Header

Definir futuramente:

- ordem material dos elementos;
- espaçamentos;
- comportamento sticky/persistent exato;
- responsividade;
- apresentação do launcher;
- relação visual entre Login e `Iniciar Jornada`;
- tratamento dos ícones de compartilhar e globo.

A arquitetura semântica já está definida em princípio.

### DESIGN-02 — CTA da Hero

A função está definida como continuidade de descoberta.

A futura etapa de copy/design pode explorar:

- label primário;
- eventual ação secundária sem competir com a descoberta;
- forma visual;
- mecanismo material de continuidade dentro da própria Home.

A relação com `Iniciar Jornada` já está definida por `GKR-UX-HOME-NAV-003` e não deve ser reinventada pelo wireframe.

### DESIGN-03 — estratégia material de mídia da Hero

Podem ser exploradas:

- tipografia/composição sem mídia dominante;
- fotografia;
- vídeo;
- mídia híbrida;
- variação responsiva.

A Hero deve funcionar mesmo sem mídia carregada.

### DESIGN-04 — materialização das sete macroexperiências

O agrupamento estratégico de referência já está definido por `GKR-UX-HOME-NARR-005`.

O design poderá decidir:

- quantas regiões técnicas existirão;
- como as sete macroexperiências se conectam espacialmente;
- se uma macroexperiência usa uma ou mais composições internas;
- densidade;
- alternância de ritmo;
- transições;
- relação entre texto, mídia e prova;
- equivalência desktop/mobile.

O wireframe não deve voltar à premissa de que qualquer combinação entre os onze movimentos é igualmente válida.

### DESIGN-05 — materialização dos slots de prova

O wireframe pode especificar o papel de uma prova sem inventar o fato concreto.

Exemplos:

- história real documentada;
- fotografia autorizada;
- evidência institucional;
- métrica com fonte/período;
- conteúdo editorial;
- fallback quando a prova não estiver disponível.

A distribuição deve preservar `GKR-UX-HOME-NARR-004`: Movimento 02 e Movimento 09 possuem funções de prova diferentes.

### DESIGN-06 — percepção visual material

Permanecem para design:

- grid;
- tipografia;
- paleta;
- geometria;
- composição fotográfica;
- escala tipográfica;
- componentes;
- movimento;
- microinterações.

A direção perceptiva já está governada.

---

## 5. Temas explicitamente fora do gate pré-wireframe

Conforme `GKR-UX-HOME-GTM-BOUNDARY-001`, não bloqueiam o wireframe conceitual:

- quais produtos estarão operacionais no lançamento;
- ordem de lançamento dos produtos;
- teaser, beta, preview, waitlist ou `em breve`;
- produtos que receberão maior exposição comercial em determinada fase;
- calendário de lançamento;
- campanhas e canais de Marketing;
- regiões comerciais do lançamento;
- páginas que estarão publicadas no primeiro release;
- idiomas efetivamente ativados no primeiro release;
- destino final de produção de cada CTA;
- disponibilidade transacional de Travel ou Mall;
- disponibilidade self-service de Business ou Ads;
- interface pública própria de Intelligence;
- rollout de Journey;
- arquitetura da página `Mapa do Ecossistema`.

Esses pontos pertencem a Marketing/GTM, implementação, publicação ou outras frentes futuras.

---

## 6. Verdade operacional permanece obrigatória em produção

Retirar lançamento/GTM do gate de wireframe não autoriza simulação.

A futura Home publicada não poderá inventar:

- usuários;
- histórias;
- parceiros;
- Organizações;
- Coletivos;
- países de operação;
- números;
- resultados;
- funcionalidades;
- disponibilidade;
- personalização;
- claims de segurança ou conformidade.

Separação:

```text
wireframe conceitual
≠ claim público
≠ produção
≠ lançamento
```

Antes de publicação, a versão concreta deverá ser reconciliada com verdade operacional, direitos de uso, Legal, Produto, Tecnologia, Marketing/GTM e demais autoridades aplicáveis.

---

## 7. Matriz de prontidão

### Estratégia de marca
**ALTA**

### Hero — significado
**ALTA**

### Narrativa — onze movimentos
**ALTA**

### Agrupamento — sete macroexperiências
**ALTA EM PRINCÍPIO**

### Movimento 02 × Movimento 09
**ALTA EM PRINCÍPIO**

### Transição Pertencimento → Ecossistema
**ALTA EM PRINCÍPIO**

### Movimento 08 — hierarquia do ecossistema
**ALTA EM PRINCÍPIO**

### Conteúdo e prova — regras
**ALTA**

### Header — arquitetura conceitual
**ALTA**

### Header — materialização visual
**PARA DESIGN**

### Launcher — inventário conceitual
**ALTA**

### Journey — porta própria `Iniciar Jornada`
**DECIDIDO EM PRINCÍPIO**

### Participantes — Pessoa / Organizações e Coletivos
**ALTA EM PRINCÍPIO**

### Idioma/região — presença conceitual
**ALTA EM PRINCÍPIO**

### Mapa do Ecossistema — link no rodapé
**DECIDIDO**

### Mapa do Ecossistema — página
**INTENCIONALMENTE ADIADA / FORA DO ESCOPO**

### Interação e ritmo
**ALTA EM PRINCÍPIO**

### Percepção visual
**ALTA EM PRINCÍPIO**

### Estratégia de lançamento/GTM
**INTENCIONALMENTE FORA DO ESCOPO**

### UI específica
**INTENCIONALMENTE NÃO INICIADA**

### Wireframe
**ESTRATEGICAMENTE APTO PARA FUTURA EXPLORAÇÃO, MAS NÃO AUTORIZADO**

---

## 8. Gate recomendado para iniciar futura materialização

Antes de iniciar um wireframe governado da Home, exigir apenas:

1. autorização explícita para entrar na etapa de materialização;
2. confirmação de que o escopo continua restrito à Home pública;
3. adoção dos documentos desta frente como baseline de trabalho;
4. preservação da arquitetura dos onze movimentos e do agrupamento de referência em sete macroexperiências;
5. preservação da distinção Movimento 02 × Movimento 09;
6. preservação da transição 07 → 08 e da hierarquia do Movimento 08;
7. preservação da arquitetura vigente do Header;
8. preservação dos limites de prova, autonomia e privacidade;
9. definição do objetivo da rodada de wireframe — exploração, comparação ou convergência;
10. rastreabilidade entre proposta visual e requisitos da arquitetura.

Não é necessário, para esse gate:

- fechar lançamento;
- classificar produto como operacional/não operacional;
- definir GTM;
- definir mercados de lançamento;
- detalhar a página `Mapa do Ecossistema`;
- possuir todo o acervo real de mídia e histórias.

---

## 9. O que o futuro wireframe não poderá decidir sozinho

O designer ou ferramenta generativa não pode redefinir:

- o que a Guivos é;
- a pergunta-mãe;
- os cinco pilares;
- os onze movimentos;
- o agrupamento estratégico de referência em sete macroexperiências;
- a distinção `Movimento 02 — realidade ≠ Movimento 09 — autoridade`;
- o papel de Pessoas, Organizações e Coletivos;
- a separação `participante ≠ produto`;
- a regra `Participantes respondem “quem”; produtos e capacidades respondem “como”`;
- a ordem semântica dominante da narrativa;
- o papel estrutural dos produtos;
- Journey como porta própria `Iniciar Jornada` no Header;
- o inventário conceitual vigente do launcher;
- a hierarquia Journey / manifestações especializadas / Intelligence no Movimento 08;
- a existência do link `Mapa do Ecossistema` no rodapé;
- regras de autonomia;
- limites de personalização pública;
- regras de verdade e não simulação.

Também não poderá inventar uma estratégia de lançamento para preencher lacunas de design.

---

## 10. O que o futuro wireframe deverá decidir

A futura etapa deverá propor, entre outros:

- melhor materialização espacial das sete macroexperiências;
- quantidade de regiões técnicas necessária para essa materialização;
- estrutura espacial;
- densidade;
- hierarquia;
- posição material dos acessos definidos;
- relação Header / narrativa / rodapé;
- tradução visual da passagem `quem participa → como o ecossistema ganha forma`;
- forma de representar produtos sem catálogo;
- distribuição material das provas respeitando Realidade × Autoridade;
- Hero com fallback;
- comportamento desktop/mobile;
- estados sem mídia;
- arquitetura preliminar de componentes;
- princípios de movimento;
- acessibilidade estrutural.

---

## 11. Questões para futura auditoria de wireframe

Uma proposta futura deverá responder:

1. O visitante entende a ideia da Guivos antes dos produtos?
2. A página responde progressivamente à pergunta `O que se torna possível quando você entra aqui?`?
3. Os onze movimentos continuam semanticamente presentes mesmo sem onze seções?
4. As sete macroexperiências de referência são reconhecíveis como progressão de intenção?
5. A passagem Hero → Realidade é clara?
6. Realidade + Amplitude expandem o universo sem virar feed ou catálogo?
7. Desconexão + Conexão apresentam problema e papel da Guivos sem narrativa salvadora?
8. Do Possível ao Vivido + Pertencimento preservam protagonismo dos participantes?
9. A transição 07 → 08 evita qualquer mapeamento automático de participante para produto?
10. O Movimento 08 diferencia Journey, manifestações especializadas e Intelligence sem exigir arquitetura técnica?
11. O Movimento 02 mostra que o universo existe sem virar propaganda institucional?
12. O Movimento 09 demonstra substância da Guivos sem repetir emocionalmente o Movimento 02?
13. Autoridade é equilibrada por autonomia e limites?
14. A página faz a Guivos parecer ecossistema ou catálogo?
15. Existe amplitude sem promessa vazia?
16. Existe pertencimento?
17. Pessoas, Organizações e Coletivos possuem papel compreensível?
18. A Guivos aparece como facilitadora, não como heroína absoluta?
19. A tecnologia está subordinada à consequência humana?
20. A proposta poderia ser confundida com marketplace, IA, coaching ou portal de benefícios?
21. A página parece global sem ser genérica?
22. Existe sofisticação sem complexidade?
23. O design continua funcionando sem vídeo e sem animação?
24. O Header oferece acesso sem transformar a marca em catálogo?
25. O launcher preserva Journey fora de sua grade na hipótese vigente?
26. O Movimento 11 permanece encerramento narrativo próprio e não é absorvido pelo Footer?
27. `Mapa do Ecossistema` continua apenas como link no rodapé desta frente?
28. A solução desperta vontade de descobrir?
29. A proposta é reconhecivelmente Guivos e não uma cópia de benchmark?

---

## 12. Síntese de prontidão

A documentação já responde com alta confiança:

- o que a Home precisa significar;
- qual percepção de marca deve gerar;
- como a Hero abre a narrativa;
- como os onze movimentos constroem compreensão;
- como esses onze movimentos podem ser organizados em sete macroexperiências sem virarem onze caixas;
- por que Realidade e Autoridade possuem funções de prova diferentes;
- como Pertencimento conduz a Ecossistema sem segmentar participantes por produto;
- por que produtos não dominam a abertura;
- como o Movimento 08 explica coerência em vez de portfólio;
- como o Header oferece acessos sem catalogar a marca;
- como Journey se diferencia do launcher;
- como Organizações e Coletivos aparecem na navegação;
- como idioma/região entra no Header;
- qual é o limite atual do `Mapa do Ecossistema`;
- como provas devem funcionar sem ficção;
- como movimento e interação servem à narrativa;
- como autonomia e confiança são preservadas;
- que percepção visual deve ser buscada;
- o que deve ser rejeitado.

Não é necessário responder nesta frente:

> **o que estará disponível, clicável ou comercialmente priorizado no primeiro lançamento.**

Essa pergunta pertence à futura estratégia de Marketing/GTM e à preparação de produção/publicação.

Regra final:

> **A Home pode ser desenhada como arquitetura completa do ecossistema enquanto o ecossistema ainda está sendo construído. O que será ativado em cada lançamento é uma decisão posterior de Marketing/GTM, sujeita à verdade operacional.**