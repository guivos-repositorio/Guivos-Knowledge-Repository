---
id: GKR-UX-HOME-AUDIT-001
title: Auditoria de Completude Pré-Wireframe da Home Pública
status: draft
version: 0.9.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-28
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
  - GKR-UX-HOME-NAV-004
  - GKR-UX-HOME-SYS-001
  - GKR-UX-HOME-BENCH-001
  - GKR-UX-HOME-BENCH-002
  - GKR-UX-HOME-GTM-BOUNDARY-001
related:
  - GKR-UX-HOME-MASTER-001
normative: false
maturity: reconciled_pre_wireframe_readiness_audit
---

# Auditoria de Completude Pré-Wireframe da Home Pública

## 1. Objetivo

Esta auditoria verifica se a documentação da Home pública possui definição estratégica suficiente para uma futura materialização conceitual sem obrigar designers, equipes ou ferramentas generativas a reinventar decisões de marca e experiência.

Nesta versão, o audit foi reconciliado com `GKR-UX-HOME-MASTER-001 v1.0.0` e com o estado narrativo consolidado após a reconciliação de `GKR-UX-HOME-NARR-005`, `GKR-UX-HOME-NARR-001` e `GKR-UX-HOME-VAL-001`.

O Master é a autoridade de consumo vigente da Home. Este audit funciona como verificação de prontidão e não o substitui.

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
- agrupamento de referência em sete macroexperiências;
- distinção `Possibilidade ≠ Oportunidade`;
- camada de `Mecanismo` na passagem da Possibilidade à Experiência;
- distinção entre Realidade e Autoridade;
- transição entre Pertencimento e Ecossistema/Produtos;
- taxonomia dos sete Produtos Especializados;
- Guivos Business como Produto Especializado B2B, sem equivalência `Organização = Business`;
- Guivos Intelligence como Produto Especializado transversal / Intelligence Layer, sem autoridade decisória totalizante;
- conteúdo e prova;
- interação e ritmo;
- percepção visual;
- Header Persistente em princípio;
- comportamento persistente do Header durante scroll e mobile;
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

Journey / Travel / Mall / Business / Media / Ads / Intelligence
= Produtos Especializados com responsabilidades próprias
```

E preserva:

```text
Possibilidade
≠ Oportunidade

Compreender
≠ Decidir
```

A principal correção de escopo permanece:

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

1. `O que se torna possível quando você entra aqui?`
2. `Um mundo maior de possibilidades passa a fazer parte do seu.`
3. `A Guivos conecta Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências para tornar novas Possibilidades mais visíveis e aproximar Oportunidades reais quando elas fizerem sentido.`

A futura copy pode lapidar redação, mas não remover:

- conexão;
- pluralidade de participantes;
- Pessoas, Organizações e Coletivos;
- conhecimento;
- caminhos e experiências;
- distinção entre Possibilidade e Oportunidade;
- Oportunidades reais apenas quando houver materialização externa legítima e fizerem sentido;
- ausência de promessa de resultado.

Autonomia permanece princípio transversal da Home e possui explicitação própria no Movimento 10; não é requisito adicional exclusivo da terceira camada da Hero.

### 3.4 Movimento 06 e assinatura institucional — DECIDIDO

O Movimento 06 é:

> **Da Possibilidade à Experiência.**

A expressão histórica `Do possível ao vivido.` não funciona como assinatura complementar da Home nem como segunda assinatura institucional da Guivos.

Quando a assinatura institucional da marca for utilizada, sua aplicação deve obedecer à autoridade de Marca vigente.

A cadeia de referência do Movimento 06 é:

```text
POSSIBILIDADE
→ MECANISMO
→ OPORTUNIDADE REAL, quando houver materialização externa legítima
→ ESCOLHA
→ EXPERIÊNCIA
→ CONTRIBUIÇÃO / APRENDIZADO
→ NOVO MOMENTO
```

Ela não é funil obrigatório e não representa resultado garantido.

### 3.5 Cinco pilares — DECIDIDO

- possibilidade;
- pertencimento;
- conexão;
- realidade;
- autonomia.

### 3.6 Cadeia conceitual — DECIDIDO

`ENTRAR → AMPLIAR → DESCOBRIR → COMPREENDER / CONECTAR → ESCOLHER → EXPERIMENTAR → APRENDER / EVOLUIR`.

### 3.7 Onze movimentos narrativos — DECIDIDO

1. Hero;
2. Possibilidades Reais;
3. Amplitude;
4. Desconexão;
5. Guivos / Conexão;
6. Da Possibilidade à Experiência;
7. Pertencimento;
8. Ecossistema / Produtos;
9. Autoridade;
10. Autonomia e Confiança;
11. Descoberta.

### 3.8 Onze movimentos não equivalem a onze blocos visuais — DECIDIDO

Os onze movimentos são funções estratégicas, não seções técnicas obrigatórias.

### 3.9 Agrupamento em sete macroexperiências — DECIDIDO EM PRINCÍPIO

A hipótese principal governada por `GKR-UX-HOME-NARR-005` é:

1. Abrir o Horizonte — Movimento 01;
2. Ver o Real e Perceber a Amplitude — Movimentos 02 + 03;
3. Perceber a Desconexão e Entender o Papel da Guivos — Movimentos 04 + 05;
4. Da Possibilidade à Experiência + Pertencimento — Movimentos 06 + 07;
5. Compreender a Coerência do Ecossistema — Movimento 08;
6. Encontrar Substância sem Perder Autonomia — Movimentos 09 + 10;
7. Reabrir o Horizonte para a Descoberta — Movimento 11.

Regra:

> **Onze funções. Sete macroexperiências de referência. Uma única narrativa.**

Sete macroexperiências não equivalem a sete seções técnicas obrigatórias.

### 3.10 Movimento 02 × Movimento 09 — DECIDIDO

Governado por `GKR-UX-HOME-NARR-004`:

> **Movimento 02 prova que o universo de possibilidades é real. Movimento 09 prova que a Guivos possui substância, método e responsabilidade para atuar nesse universo.**

Regra curta:

> **02 = “isso existe”. 09 = “há razões para confiar em como a Guivos lida com isso”.**

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

Layout, espaçamento, ordem material final e tratamento visual permanecem para design.

### 3.14 Comportamento persistente do Header — DECIDIDO EM PRINCÍPIO

Governado por `GKR-UX-HOME-NAV-004`.

Regra principal:

> **O Header da Guivos deve permanecer disponível sem permanecer dominante. Ele orienta enquanto a narrativa conduz.**

Consequências:

- o Header não desaparece completamente durante longos trechos como comportamento padrão;
- pode compactar após a Hero;
- a Hero continua dominando o primeiro viewport;
- `Iniciar Jornada` permanece disponível sem pressão crescente;
- a arquitetura do Header não muda a cada macroexperiência;
- mobile condensa sem criar uma segunda arquitetura de navegação;
- controles condensados permanecem, em regra, a uma camada de navegação de distância;
- launcher e eventual menu geral mantêm semânticas diferentes;
- contraste e acessibilidade prevalecem sobre transparência estética.

### 3.15 Launcher do Ecossistema — DECIDIDO EM PRINCÍPIO

Inventário conceitualmente aprovado nesta fase:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey não integra o launcher na hipótese principal atual.

### 3.16 Journey no Header — DECIDIDO EM PRINCÍPIO

> **Journey permanece parte do ecossistema, mas sua porta principal no Header é `Iniciar Jornada`, e não o launcher.**

Journey continua podendo aparecer no Movimento 08 e em acessos contextuais quando houver fundamento legítimo.

### 3.17 Participantes no Header — DECIDIDO EM PRINCÍPIO

A Pessoa é atendida naturalmente pela própria Home e por `Iniciar Jornada`.

Organizações e Coletivos recebem uma única porta dedicada de aprofundamento.

A página de destino permanece fora desta frente.

### 3.18 Idioma e região — DECIDIDO EM PRINCÍPIO

Existe controle compacto no Header, conceitualmente representado por globo.

Idioma e região são preferências distintas.

A superfície de seleção será materializada futuramente.

### 3.19 Compartilhar — DECIDIDO EM PRINCÍPIO

Existe intenção de controle utilitário de compartilhamento no Header.

Comportamento técnico não é definido nesta frente.

### 3.20 Mapa do Ecossistema — DECIDIDO NO LIMITE DESTA FRENTE

> **Nesta fase, `Mapa do Ecossistema` é somente um link no rodapé.**

A página, sua arquitetura, categorias, conteúdo e acessos internos ficam fora da frente atual.

### 3.21 Header × Hero × CTAs — DECIDIDO EM PRINCÍPIO

A relação de intenção fica definida:

> **Hero = descoberta e continuidade narrativa. Header = acesso persistente à Journey por `Iniciar Jornada`.**

A Hero não duplica `Iniciar Jornada` como CTA dominante na hipótese principal.

A copy final e a forma material do CTA de descoberta permanecem abertas.

### 3.22 Movimento 07 → 08 — DECIDIDO EM PRINCÍPIO

A transição entre pertencimento e produtos está definida por `GKR-UX-HOME-NARR-003`.

Regra:

> **Participantes respondem “quem”. Produtos e capacidades respondem “como”.**

A Home não deve criar correspondência automática:

```text
Pessoa → Journey
Organização → Business
Coletivo → produto específico
```

Regra de sequência:

> **Pertencimento primeiro. Materialização depois. Segmentação por produto, nunca.**

### 3.23 Movimento 08 — Produtos Especializados — DECIDIDO EM PRINCÍPIO

O Movimento 08 deve preservar a hierarquia reconciliada do Master:

```text
GUIVOS
│
├── JOURNEY
│   └── experiência e continuidade da jornada
│
├── MALL / TRAVEL / BUSINESS / MEDIA / ADS
│   └── Produtos Especializados com responsabilidades próprias
│
└── INTELLIGENCE
    └── Produto Especializado transversal de inteligência
```

Os sete permanecem **Produtos Especializados** dentro de uma única Guivos; essa taxonomia comum não elimina as responsabilidades distintas do Movimento 08.

Journey preserva seu papel de experiência e continuidade e **não deve virar card equivalente por convenção**.

O Intelligence possui papel transversal / Intelligence Layer sem deixar de ser Produto Especializado e sem se tornar autoridade decisória totalizante.

Business é Produto Especializado B2B e não equivale ao tipo estrutural `Organização`.

Regra:

> **O Movimento 08 não é uma vitrine de produtos nem um launcher ampliado. É uma explicação da coerência entre responsabilidades diferentes dentro da mesma Guivos.**

### 3.24 Sistema de conteúdo — DECIDIDO

Classes:

- institucional permanente;
- evidência real;
- editorial;
- ecossistema;
- navegação/ação.

### 3.25 Hierarquia de prova — DECIDIDO

Prova direta > história documentada > evidência institucional > métrica > depoimento > afirmação institucional.

### 3.26 Modelo editorial das histórias — DECIDIDO

O modelo editorial canônico é:

```text
CONTEXTO
→ POSSIBILIDADE
→ DECISÃO
→ EXPERIÊNCIA
→ CONSEQUÊNCIA
→ CONTINUIDADE
```

Pergunta editorial de continuidade:

> **E depois?**

`Mecanismo` e eventual `Oportunidade real` não são etapas editoriais obrigatórias. Quando uma história estiver explicando especificamente o Movimento 06, aplica-se a cadeia mais rica definida em `3.4`, sem convertê-la em funil obrigatório nem promessa de resultado.

A Guivos não deve apropriar-se da agência do participante.

### 3.27 Conteúdo vivo sem feed — DECIDIDO

Camadas permanente, editorial e temporal.

### 3.28 Guivos Media como fonte editorial futura — DECIDIDO CONCEITUALMENTE

Não existe autorização de integração técnica nesta frente.

### 3.29 Interação e movimento — DECIDIDO EM PRINCÍPIO

Movimento deve revelar, conectar e dar continuidade sem substituir clareza.

### 3.30 Autonomia do scroll — DECIDIDO

Nenhuma experiência pode obrigar o visitante a assistir animações ou aguardar narrativa bloqueante.

### 3.31 Desktop/mobile — DECIDIDO EM PRINCÍPIO

Mesma tese, mesma arquitetura de intenção e mesma hierarquia; composição e densidade podem variar.

### 3.32 Percepção visual — DECIDIDO

> **Futuro sem ficção. Tecnologia sem frieza. Sofisticação sem elitismo. Escala sem ruído. Humanidade sem clichê.**

### 3.33 Acessibilidade e resiliência — DECIDIDO EM PRINCÍPIO

A experiência deve funcionar com:

- teclado;
- leitor de tela;
- foco visível;
- redução de movimento;
- mídia indisponível;
- baixa conectividade;
- responsividade;
- internacionalização.

### 3.34 Anti-padrões — DECIDIDO

Existe repertório de rejeição narrativa, editorial, visual, interativa e de navegação.

---

## 4. Decisões que podem ser resolvidas durante design/copy

### DESIGN-01 — composição material do Header

A futura etapa poderá definir:

- altura inicial e compacta;
- breakpoint;
- ordem material final dentro dos núcleos aprovados;
- espaçamentos;
- transparência ou superfície sólida;
- formato de compactação;
- tratamento visual de Login e `Iniciar Jornada`;
- formato do launcher;
- tipo de navegação mobile;
- exposição direta ou em primeira camada de Login, globo e launcher no mobile;
- animação específica;
- comportamento técnico sticky/fixed equivalente.

Não poderá redefinir a persistência semântica e os limites estabelecidos em `GKR-UX-HOME-NAV-004`.

### DESIGN-02 — CTA da Hero

A função está definida como continuidade de descoberta.

A futura etapa de copy/design pode explorar:

- label primário;
- eventual ação secundária sem competir com a descoberta;
- forma visual;
- mecanismo material de continuidade dentro da própria Home.

A relação com `Iniciar Jornada` já está definida por `GKR-UX-HOME-NAV-003`.

### DESIGN-03 — estratégia material de mídia da Hero

Podem ser exploradas:

- tipografia/composição sem mídia dominante;
- fotografia;
- vídeo;
- mídia híbrida;
- variação responsiva.

A Hero deve funcionar mesmo sem mídia carregada.

### DESIGN-04 — materialização das sete macroexperiências

A hipótese de agrupamento estratégico já está definida por `GKR-UX-HOME-NARR-005`.

O design poderá decidir:

- quantas regiões técnicas serão necessárias;
- como cada macroexperiência ocupa o espaço;
- continuidade entre regiões;
- densidade;
- alternância de ritmo;
- transições;
- relação entre texto, mídia e prova.

Não deverá reorganizar arbitrariamente os onze movimentos como se qualquer combinação fosse equivalente.

### DESIGN-05 — materialização dos slots de prova

O wireframe pode especificar o papel de uma prova sem inventar o fato concreto.

Exemplos:

- história real documentada;
- fotografia autorizada;
- evidência institucional;
- métrica com fonte/período;
- conteúdo editorial;
- fallback quando a prova não estiver disponível.

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

### Narrativa
**ALTA**

### Agrupamento em macroexperiências
**ALTA EM PRINCÍPIO**

### Distinção Possibilidade × Oportunidade
**ALTA**

### Movimento 06 — Possibilidade → Experiência
**ALTA EM PRINCÍPIO**

### Distinção Realidade × Autoridade
**ALTA**

### Transição Pertencimento → Ecossistema
**ALTA EM PRINCÍPIO**

### Movimento 08 — coerência dos Produtos Especializados
**ALTA EM PRINCÍPIO**

### Conteúdo e prova — regras
**ALTA**

### Header — arquitetura conceitual
**ALTA**

### Header — comportamento persistente / scroll / mobile
**ALTA EM PRINCÍPIO**

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
3. adoção de `GKR-UX-HOME-MASTER-001` como autoridade de consumo e dos documentos especializados como baseline de aprofundamento;
4. preservação da arquitetura narrativa, das sete macroexperiências, da transição 07 → 08, do Movimento 08 e do Header vigentes;
5. preservação do comportamento do Header estabelecido em `GKR-UX-HOME-NAV-004`;
6. preservação da distinção `Possibilidade ≠ Oportunidade`, da camada de Mecanismo e da ausência de garantia de resultado;
7. preservação dos limites de prova, autonomia e privacidade;
8. definição do objetivo da rodada de wireframe — exploração, comparação ou convergência;
9. rastreabilidade entre proposta visual e requisitos da arquitetura.

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
- o agrupamento estratégico das sete macroexperiências sem justificativa e revisão de arquitetura;
- a distinção `Possibilidade ≠ Oportunidade`;
- o papel do Mecanismo na passagem da Possibilidade à Experiência;
- a distinção Movimento 02 × Movimento 09;
- o papel de Pessoas, Organizações e Coletivos;
- a separação `participante ≠ produto`;
- a regra `Participantes respondem “quem”; produtos e capacidades respondem “como”`;
- a ordem semântica dominante da narrativa;
- os sete Produtos Especializados e suas responsabilidades estruturais;
- Journey como experiência e continuidade da jornada, sem equivalência automática a um card dos demais Produtos no Movimento 08;
- Business como Produto Especializado B2B, não como sinônimo de Organização;
- Intelligence como Produto Especializado transversal / Intelligence Layer, com `COMPREENDER ≠ DECIDIR`;
- Journey como porta própria `Iniciar Jornada` no Header;
- o inventário conceitual vigente do launcher;
- a persistência semântica do Header e seus limites de comportamento;
- a existência do link `Mapa do Ecossistema` no rodapé;
- regras de autonomia;
- limites de personalização pública;
- regras de verdade e não simulação.

Também não poderá inventar uma estratégia de lançamento para preencher lacunas de design.

---

## 10. O que o futuro wireframe deverá decidir

A futura etapa deverá propor, entre outros:

- estrutura espacial;
- quantidade de regiões técnicas necessárias para materializar as sete macroexperiências;
- densidade;
- hierarquia visual;
- posição material dos acessos definidos;
- altura e compactação do Header;
- comportamento visual do Header entre Hero e narrativa;
- solução responsiva mobile dentro da hierarquia vigente;
- relação Header / narrativa / rodapé;
- tradução visual da passagem `quem participa → como o ecossistema ganha forma`;
- forma de representar Produtos Especializados sem catálogo;
- slots e distribuição de prova;
- Hero com fallback;
- estados sem mídia;
- arquitetura preliminar de componentes;
- princípios de movimento;
- acessibilidade estrutural.

---

## 11. Questões para futura auditoria de wireframe

Uma proposta futura deverá responder:

1. O visitante entende a ideia da Guivos antes dos produtos?
2. A página responde progressivamente à pergunta `O que se torna possível quando você entra aqui?`?
3. A narrativa faz a realidade aparecer cedo sem depender de prova fictícia?
4. A Guivos parece ecossistema ou catálogo?
5. Existe amplitude sem promessa vazia?
6. Existe pertencimento?
7. Pessoas, Organizações e Coletivos possuem papel compreensível?
8. A Guivos aparece como facilitadora, não como heroína absoluta?
9. A autonomia permanece perceptível?
10. A tecnologia está subordinada à consequência humana?
11. A proposta poderia ser confundida com marketplace, IA, coaching ou portal de benefícios?
12. A página parece global sem ser genérica?
13. Existe sofisticação sem complexidade?
14. O design continua funcionando sem vídeo e sem animação?
15. Os produtos entram narrativamente no momento correto?
16. O Header oferece acesso sem transformar a marca em catálogo?
17. O Header permanece previsível durante a rolagem sem dominar a narrativa?
18. A compactação do Header reduz espaço sem remover caminhos essenciais?
19. No mobile, os acessos condensados permanecem a uma camada de distância?
20. Launcher e navegação geral preservam funções diferentes?
21. O launcher preserva Journey fora de sua grade na hipótese vigente?
22. A transição 07 → 08 evita qualquer mapeamento automático de participante para produto?
23. O Movimento 08 preserva Journey como experiência e continuidade, mantém os demais Produtos Especializados com responsabilidades próprias e preserva o papel transversal do Intelligence sem criar nova classe estrutural?
24. Business permanece distinto do tipo estrutural Organização?
25. Movimento 02 e Movimento 09 cumprem funções diferentes de prova?
26. O Movimento 06 distingue Possibilidade, Mecanismo, eventual Oportunidade real, escolha e Experiência sem parecer funil garantido?
27. As sete macroexperiências preservam os onze significados sem parecer onze seções?
28. `Mapa do Ecossistema` continua apenas como link no rodapé desta frente?
29. A solução desperta vontade de descobrir?
30. A proposta é reconhecivelmente Guivos e não uma cópia de benchmark?
---

## 12. Síntese de prontidão

A documentação já responde com alta confiança:

- o que a Home precisa significar;
- qual percepção de marca deve gerar;
- como a Hero abre a narrativa;
- como os onze movimentos constroem compreensão;
- como esses movimentos se agrupam em sete macroexperiências de referência;
- como Possibilidade, Mecanismo, eventual Oportunidade real, escolha e Experiência se distinguem;
- como Realidade e Autoridade cumprem papéis diferentes;
- como Pertencimento conduz a Ecossistema sem segmentar participantes por produto;
- por que produtos não dominam a abertura;
- como o Movimento 08 explica coerência entre sete Produtos Especializados em vez de portfólio, preservando Journey como experiência e continuidade e Intelligence como Produto Especializado transversal;
- como Business permanece distinto de Organização;
- como Intelligence amplia compreensão sem substituir decisão;
- como o Header oferece acessos sem catalogar a marca;
- como o Header se comporta durante scroll e mobile sem desaparecer ou dominar;
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

Estado deste audit:

> **PRONTIDÃO ESTRATÉGICA PRÉ-WIREFRAME RECONCILIADA — MATERIALIZAÇÃO NÃO AUTORIZADA.**
