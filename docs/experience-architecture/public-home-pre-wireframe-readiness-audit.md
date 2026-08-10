---
id: GKR-UX-HOME-AUDIT-001
title: Auditoria de Completude Pré-Wireframe da Home Pública
status: draft
version: 0.5.0
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
- tese e sistema semântico da Hero;
- arquitetura narrativa;
- onze movimentos;
- conteúdo e prova;
- interação e ritmo;
- percepção visual;
- Header Persistente em princípio;
- launcher do ecossistema em princípio;
- separação da Journey em relação ao launcher;
- relação entre Header, Hero e CTAs em princípio;
- acesso de Organizações e Coletivos;
- idioma/região;
- link `Mapa do Ecossistema` no rodapé;
- limites de autonomia, privacidade e não simulação;
- separação entre arquitetura da Home e Marketing/GTM.

A relação de ação do primeiro viewport está agora definida em princípio:

> **Hero = descoberta e continuidade narrativa. Header = acesso persistente à Journey por `Iniciar Jornada`.**

Consequentemente, a Hero não deve duplicar `Iniciar Jornada` como CTA dominante na hipótese principal vigente.

A disponibilidade dos produtos no lançamento, páginas do lançamento, idiomas/regiões do lançamento e demais decisões de GTM continuam fora dos requisitos da arquitetura conceitual da Home.

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

Design pode combinar funções sem eliminar significado.

### 3.9 Produtos subordinados à ideia maior — DECIDIDO

Produtos não dominam a abertura da Home.

### 3.10 Acesso e protagonismo são dimensões diferentes — DECIDIDO

> **acessível desde o início ≠ explicado desde o início ≠ protagonista desde o início.**

### 3.11 Header Persistente — DECIDIDO EM PRINCÍPIO

A arquitetura atual considera:

- Guivos / Home;
- `Sobre`;
- `Organizações e Coletivos`;
- compartilhar;
- idioma/região por globo;
- launcher do ecossistema por grade de pontos;
- `Login`;
- `Iniciar Jornada` como CTA de maior hierarquia dentro do Header e porta própria da Journey.

Layout, espaçamento, ordem material final, responsividade e tratamento visual permanecem para design.

### 3.12 Launcher do Ecossistema — DECIDIDO EM PRINCÍPIO

Inventário conceitualmente aprovado nesta fase:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey não integra o launcher na hipótese principal vigente.

### 3.13 Journey no Header — DECIDIDO EM PRINCÍPIO

> **Journey permanece parte do ecossistema, mas sua porta principal no Header é `Iniciar Jornada`, e não o launcher.**

Journey continua podendo aparecer no Movimento 08 e em acessos contextuais quando houver fundamento legítimo.

### 3.14 Participantes no Header — DECIDIDO EM PRINCÍPIO

A Pessoa é atendida naturalmente pela própria Home e por `Iniciar Jornada`.

Organizações e Coletivos recebem uma única porta dedicada de aprofundamento.

A página de destino permanece fora desta frente.

### 3.15 Idioma e região — DECIDIDO EM PRINCÍPIO

Existe controle compacto no Header, conceitualmente representado por globo.

Idioma e região são preferências distintas.

A superfície de seleção será materializada futuramente.

### 3.16 Compartilhar — DECIDIDO EM PRINCÍPIO

Existe intenção de controle utilitário de compartilhamento no Header.

Comportamento técnico não é definido nesta frente.

### 3.17 Mapa do Ecossistema — DECIDIDO NO LIMITE DESTA FRENTE

> **Nesta fase, `Mapa do Ecossistema` é somente um link no rodapé.**

A página, sua arquitetura, categorias, conteúdo e acessos internos ficam fora da frente atual.

### 3.18 Hierarquia Header × Hero × CTAs — DECIDIDO EM PRINCÍPIO

A Home separa duas camadas de ação:

```text
Header Persistente
→ orientação + acessos permanentes + decisão de iniciar Journey

Hero
→ abertura narrativa + continuidade de descoberta
```

Regra de controle:

> **A Hero deve fazer a pessoa querer continuar entendendo; o Header deve permitir que ela aja quando já souber o que quer fazer.**

Consequências:

- `Iniciar Jornada` permanece no Header;
- Hero não duplica `Iniciar Jornada` como CTA dominante na hipótese principal;
- CTA da Hero possui função de continuar a descoberta dentro da própria Home;
- Login permanece utilitário;
- launcher permanece acesso direto para intenção já conhecida;
- Header não pode sequestrar a hierarquia perceptiva da Hero.

### 3.19 CTA da Hero — DECIDIDO EM FUNÇÃO / COPY ABERTA

A função comportamental é:

> **continuar a descoberta dentro da própria Home.**

Territórios de copy como `Descubra a Guivos`, `Explore possibilidades`, `Comece a explorar` ou equivalentes permanecem apenas como hipóteses de redação.

O mecanismo material de continuidade permanece para design.

### 3.20 Sistema de conteúdo — DECIDIDO

Classes:

- institucional permanente;
- evidência real;
- editorial;
- ecossistema;
- navegação/ação.

### 3.21 Hierarquia de prova — DECIDIDO

Prova direta > história documentada > evidência institucional > métrica > depoimento > afirmação institucional.

### 3.22 Modelo das histórias — DECIDIDO

Contexto → possibilidade → decisão → experiência → consequência → continuidade.

### 3.23 Conteúdo vivo sem feed — DECIDIDO

Camadas permanente, editorial e temporal.

### 3.24 Guivos Media como fonte editorial futura — DECIDIDO CONCEITUALMENTE

Não existe autorização de integração técnica nesta frente.

### 3.25 Interação e movimento — DECIDIDO EM PRINCÍPIO

Movimento deve revelar, conectar e dar continuidade sem substituir clareza.

### 3.26 Autonomia do scroll — DECIDIDO

Nenhuma experiência pode obrigar o visitante a assistir animações ou aguardar narrativa bloqueante.

### 3.27 Desktop/mobile — DECIDIDO EM PRINCÍPIO

Mesma tese e hierarquia; composição pode variar.

### 3.28 Percepção visual — DECIDIDO

> **Futuro sem ficção. Tecnologia sem frieza. Sofisticação sem elitismo. Escala sem ruído. Humanidade sem clichê.**

### 3.29 Acessibilidade e resiliência — DECIDIDO EM PRINCÍPIO

A experiência deve funcionar com:

- teclado;
- leitor de tela;
- foco visível;
- redução de movimento;
- mídia indisponível;
- baixa conectividade;
- responsividade;
- internacionalização.

### 3.30 Anti-padrões — DECIDIDO

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

### DESIGN-02 — materialização do CTA de descoberta da Hero

A relação semântica com `Iniciar Jornada` **não está mais aberta**.

A futura etapa de copy/design deverá resolver apenas:

- label final do CTA de descoberta;
- aparência e hierarquia visual material;
- affordance;
- scroll, anchor ou mecanismo equivalente;
- eventual microcopy;
- comportamento responsivo.

O CTA deve continuar a narrativa pública e não duplicar `Iniciar Jornada` como ação dominante na Hero sem nova decisão explícita de arquitetura.

### DESIGN-03 — estratégia material de mídia da Hero

Podem ser exploradas:

- tipografia/composição sem mídia dominante;
- fotografia;
- vídeo;
- mídia híbrida;
- variação responsiva.

A Hero deve funcionar mesmo sem mídia carregada.

### DESIGN-04 — composição dos onze movimentos

Decidir:

- quantos blocos visuais existirão;
- quais movimentos podem compartilhar uma composição;
- densidade;
- alternância de ritmo;
- transições;
- relação entre texto, mídia e prova.

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

### Hero — função do CTA de descoberta
**ALTA EM PRINCÍPIO**

### Hero — copy/materialização do CTA
**PARA DESIGN/COPY**

### Narrativa
**ALTA**

### Conteúdo e prova — regras
**ALTA**

### Header — arquitetura conceitual
**ALTA**

### Header — materialização visual
**PARA DESIGN**

### Relação Header × Hero × CTAs
**ALTA EM PRINCÍPIO**

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
4. preservação da arquitetura narrativa e do Header vigente;
5. preservação da hierarquia `Hero = descoberta` versus `Header = Iniciar Jornada`;
6. preservação dos limites de prova, autonomia e privacidade;
7. definição do objetivo da rodada de wireframe — exploração, comparação ou convergência;
8. rastreabilidade entre proposta visual e requisitos da arquitetura.

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
- o papel de Pessoas, Organizações e Coletivos;
- a ordem semântica dominante da narrativa;
- o papel estrutural dos produtos;
- Journey como porta própria `Iniciar Jornada` no Header;
- a função de descoberta do CTA da Hero;
- a separação entre CTA da Hero e `Iniciar Jornada`;
- o inventário conceitual vigente do launcher;
- a existência do link `Mapa do Ecossistema` no rodapé;
- regras de autonomia;
- limites de personalização pública;
- regras de verdade e não simulação.

Também não poderá inventar uma estratégia de lançamento para preencher lacunas de design.

---

## 10. O que o futuro wireframe deverá decidir

A futura etapa deverá propor, entre outros:

- melhor agrupamento visual dos movimentos;
- estrutura espacial;
- densidade;
- hierarquia;
- posição material dos acessos definidos;
- relação Header / Hero / narrativa / rodapé;
- tratamento visual do CTA da Hero;
- forma de representar produtos sem catálogo;
- slots e distribuição de prova;
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
17. A Hero convida a descobrir em vez de duplicar `Iniciar Jornada`?
18. `Iniciar Jornada` continua disponível no Header sem dominar a Hero?
19. O launcher preserva Journey fora de sua grade na hipótese vigente?
20. `Mapa do Ecossistema` continua apenas como link no rodapé desta frente?
21. A solução desperta vontade de descobrir?
22. A proposta é reconhecivelmente Guivos e não uma cópia de benchmark?

---

## 12. Síntese de prontidão

A documentação já responde com alta confiança:

- o que a Home precisa significar;
- qual percepção de marca deve gerar;
- como a Hero abre a narrativa;
- como os onze movimentos constroem compreensão;
- por que produtos não dominam a abertura;
- como o Header oferece acessos sem catalogar a marca;
- como Journey se diferencia do launcher;
- como a Hero se diferencia de `Iniciar Jornada`;
- como o primeiro viewport acomoda descoberta e decisão sem misturá-las;
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
