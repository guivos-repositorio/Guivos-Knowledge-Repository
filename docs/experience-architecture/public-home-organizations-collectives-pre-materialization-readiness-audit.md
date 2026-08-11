---
id: GKR-UX-HOME-OC-AUDIT-001
title: Auditoria de Prontidão Pré-Materialização da Home Pública de Organizações e Coletivos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-11
parent: GKR-UX-HOME-OC-MASTER-001
depends_on:
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-AUDIT-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-003
  - GKR-UX-HOME-NAV-004
  - GKR-UX-HOME-SYS-001
  - GKR-UX-HOME-NARR-005
  - UXA-014
  - UXA-019
related:
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
normative: false
---

# Auditoria de Prontidão Pré-Materialização da Home Pública de Organizações e Coletivos

## 1. Finalidade

Esta auditoria verifica se a documentação vigente da **Home Pública — Organizações e Coletivos** já contém definição suficiente para uma futura materialização governada em wireframe, UX, UI, protótipo ou Figma sem obrigar Design a reinventar decisões estratégicas.

A auditoria parte da `main` integrada após o PR #244 e do Documento Mestre `GKR-UX-HOME-OC-MASTER-001`.

Ela não autoriza:

- wireframe;
- Figma;
- SVG;
- protótipo;
- UI final;
- implementação;
- UXA-102/V5;
- Engenharia de Produto;
- publicação da página em produção.

---

## 2. Resultado executivo

Estado geral:

> **A HOME DE ORGANIZAÇÕES E COLETIVOS ESTÁ NARRATIVAMENTE MADURA, MAS AINDA NÃO ESTÁ PRONTA PARA UMA MATERIALIZAÇÃO GOVERNADA.**

O Documento Mestre já consolida com alta confiança:

- tese da página;
- relação com a Home Pública principal;
- pergunta de abertura;
- onze movimentos narrativos;
- diferença entre Pessoa, Organização e Coletivo;
- regra `participante ≠ produto`;
- regra `Organização ≠ Guivos Business`;
- papel da Guivos como conexão, contexto e continuidade;
- complementaridade entre participantes;
- múltiplas dimensões de evolução;
- circulação de valor e escala responsável;
- confiança, governança, privacidade e autonomia;
- inteligência responsável;
- hierarquia do ecossistema e dos produtos;
- bifurcação final entre Organização e Coletivo;
- limites contra B2B convencional, marketplace, rede social e catálogo de produtos.

Porém, quatro decisões de materialização ainda exigiriam interpretação livre de Design se um wireframe começasse agora:

1. agrupamento dos onze movimentos em macroexperiências próprias desta página;
2. arquitetura específica de Header, Hero e CTAs nesta segunda Home;
3. mapa de conteúdo, prova e evidência por movimento;
4. handoff próprio para Design/UX/UI, incluindo status da copy e limites de herança da Home principal.

Esses quatro pontos são **bloqueadores do gate de wireframe governado**.

Conclusão curta:

```text
arquitetura narrativa
= pronta

arquitetura pré-materialização
= incompleta

wireframe governado
= ainda não autorizado nem recomendado
```

---

## 3. O que pode ser herdado da Home Pública principal

A segunda Home pertence à mesma Guivos. Portanto, nem toda decisão precisa ser duplicada.

### 3.1 Posicionamento e percepção de marca — HERDADO

Continuam válidos:

- futuro;
- possibilidade;
- simplicidade;
- confiança;
- humanidade;
- escala global;
- tecnologia sem frieza;
- sofisticação sem elitismo;
- ecossistema maior que a soma dos produtos.

A página não precisa criar uma linguagem visual B2B própria.

### 3.2 Sistema visual transversal — HERDADO EM PRINCÍPIO

O contrato `GKR-UX-HOME-SYS-001` continua válido como direção transversal:

> **Futuro sem ficção. Tecnologia sem frieza. Sofisticação sem elitismo. Escala sem ruído. Humanidade sem clichê.**

Também permanecem aplicáveis:

- respiro como sinal de confiança;
- densidade variável;
- fotografia contextual e não corporativa genérica;
- movimento subordinado ao significado;
- experiência funcional sem vídeo ou animação;
- ausência de estética futurista genérica;
- ausência de luxo como representação de evolução.

### 3.3 Acessibilidade, redução de movimento e resiliência — HERDADO

A futura materialização deve funcionar com:

- teclado;
- leitor de tela;
- foco visível;
- contraste adequado;
- redução de movimento;
- mídia indisponível;
- baixa conectividade;
- responsividade;
- internacionalização.

### 3.4 Verdade, prova e não simulação — HERDADO COMO REGRA

Permanecem proibidos:

- pessoas fictícias apresentadas como reais;
- Organizações fictícias apresentadas como parceiras;
- Coletivos fictícios apresentados como participantes reais;
- métricas sem fonte e período;
- resultados inventados;
- países de atuação não confirmados;
- disponibilidade operacional simulada;
- claims de segurança, conformidade ou inteligência sem base governada.

### 3.5 Hierarquia do ecossistema — HERDADA

Permanece:

```text
GUIVOS

├── EXPERIÊNCIA E CONTINUIDADE
│   └── Journey
│
├── MANIFESTAÇÕES ESPECIALIZADAS
│   ├── Travel
│   ├── Mall
│   ├── Media
│   ├── Business
│   └── Ads
│
└── INTELIGÊNCIA TRANSVERSAL
    └── Intelligence
```

A segunda Home não pode reinventar essa hierarquia.

### 3.6 Limite Marketing/GTM — HERDADO

Não bloqueiam o wireframe conceitual futuro:

- produtos disponíveis no primeiro lançamento;
- calendário de lançamento;
- mercados ativados;
- páginas efetivamente publicadas no primeiro release;
- disponibilidade transacional;
- preços e planos;
- estratégia comercial;
- URLs finais dos CTAs.

A verdade operacional continuará obrigatória antes de produção.

---

## 4. O que não pode ser simplesmente herdado

### 4.1 Os sete agrupamentos da Home principal não são os agrupamentos desta página

`GKR-UX-HOME-NARR-005` organiza os onze movimentos da Home orientada à Pessoa.

A Home de Organizações e Coletivos possui onze funções diferentes:

1. abrir o horizonte;
2. reconhecer capacidades existentes;
3. perceber fragmentação e continuidade;
4. compreender o papel da Guivos;
5. compreender quem participa;
6. perceber complementaridade;
7. ampliar dimensões de evolução;
8. compreender circulação de valor e escala;
9. construir confiança;
10. compreender capacidades do ecossistema;
11. descobrir como participar.

Reutilizar mecanicamente as sete macroexperiências da Home principal faria Design forçar significados diferentes dentro de uma estrutura que não foi criada para esta página.

### 4.2 O handoff da Home principal não é o handoff desta página

`GKR-UX-HOME-HANDOFF-001` parte da pergunta:

> `O que se torna possível quando você entra aqui?`

Seu protagonista inicial é a Pessoa.

A segunda Home parte de:

> `O que podemos tornar possível juntos?`

Seu protagonista inicial é Organização / Coletivo.

Portanto, o handoff principal pode fornecer padrões, mas não pode ser entregue isoladamente a Design como especificação desta página.

### 4.3 A arquitetura do Header da Home principal não governa automaticamente o destino `Organizações e Coletivos`

Os documentos `GKR-UX-HOME-NAV-001`, `003` e `004` foram criados para a Home pública principal e tratam `Organizações e Coletivos` como um **destino de navegação**.

Eles não definem ainda o comportamento quando o visitante já está dentro desse destino.

Assim, precisam ser esclarecidos para esta página:

- estado ativo ou equivalente de `Organizações e Coletivos`;
- permanência do mesmo Header global ou adaptação controlada;
- significado de `Iniciar Jornada` dentro desta página;
- risco de `Iniciar Jornada` ser interpretado como onboarding de Organização/Coletivo;
- relação entre CTA da Hero e CTAs finais `Organização` / `Coletivo`;
- hierarquia no primeiro viewport;
- comportamento mobile da navegação nesta página;
- retorno à Home pública principal.

### 4.4 O sistema geral de prova precisa de um mapa específico

A hierarquia de prova global continua válida, mas a segunda Home precisa indicar **onde e para quê** a prova aparece.

Sem esse mapa, Design pode transformar a página em:

- mural de logos;
- coleção de cases corporativos;
- depoimentos genéricos;
- métricas de alcance;
- publicidade institucional;
- afirmações abstratas sem evidência.

---

## 5. Lacunas bloqueadoras

### OC-GAP-01 — Macroexperiências e ritmo narrativo

**Estado: BLOQUEADOR**

Existe sequência semântica de onze movimentos, mas não existe agrupamento próprio para materialização.

É necessário definir:

- quais movimentos podem compartilhar uma macroexperiência;
- quais precisam permanecer perceptivelmente separados;
- ritmo entre impacto, reconhecimento, compreensão, prova, confiança e reabertura;
- transições que não transformem a página em onze caixas empilhadas;
- equivalência desktop/mobile sem reduzir significado.

O documento deve preservar a regra:

> **onze movimentos governam significado; não significam onze seções visuais obrigatórias.**

### OC-GAP-02 — Header, Hero e hierarquia de CTAs

**Estado: BLOQUEADOR**

A página já possui pergunta de Hero e bifurcação final, mas não possui contrato de ação do primeiro viewport.

É necessário decidir em princípio:

- função do CTA da Hero;
- se a Hero apenas continua a descoberta ou antecipa participação;
- como o Header global se comporta dentro da segunda Home;
- como `Iniciar Jornada` preserva seu significado sem sugerir cadastro de Organização/Coletivo;
- como Login, launcher, idioma/região e `Sobre` permanecem acessíveis;
- como `Organizações e Coletivos` é representado no estado atual da navegação;
- como os CTAs finais assumem protagonismo apenas após compreensão suficiente.

Proteção obrigatória:

> **a página não pode converter o primeiro viewport em `cadastre sua empresa` ou `crie seu coletivo`.**

### OC-GAP-03 — Conteúdo, prova e evidência por movimento

**Estado: BLOQUEADOR**

É necessário mapear quais movimentos são predominantemente:

- tese;
- reconhecimento;
- demonstração de realidade;
- exemplo conceitual;
- evidência real;
- autoridade;
- explicação estrutural;
- ação.

A adaptação deve indicar, pelo menos, a função de prova nos movimentos:

- 02 — demonstrar que as capacidades e iniciativas existem no mundo real;
- 06 — demonstrar complementaridade sem inventar relações;
- 08 — mostrar circulação de valor sem transformar volume em prova de evolução;
- 09 — provar substância, responsabilidade, governança e limites;
- 10 — materializar coerência do ecossistema sem catálogo.

Também deve definir fallback para estágio inicial com poucas evidências reais.

### OC-GAP-04 — Handoff específico para Design/UX/UI

**Estado: BLOQUEADOR**

O Documento Mestre é uma fonte estratégica, não um brief de materialização.

Um handoff próprio deve separar claramente:

- significado obrigatório;
- copy de trabalho;
- copy final ainda aberta;
- conteúdo que pode ser condensado;
- conteúdo que não pode desaparecer;
- decisões herdadas da Home principal;
- decisões específicas da segunda Home;
- anti-padrões;
- critérios de aceite de wireframe;
- instruções para ferramentas generativas.

Sem esse artefato, existe risco de os aproximadamente onze movimentos serem tratados como texto final e produzirem uma página excessivamente longa, institucional ou didática.

---

## 6. Lacunas não bloqueadoras, mas que precisam de proteção

### OC-GAP-05 — Fronteira com superfícies autenticadas

`UXA-015` e `UXA-016` já possuem wireframes de Visão Geral da Organização e Início do Coletivo.

Esses artefatos pertencem a experiências internas/autenticadas.

A nova Home pública não deve reutilizá-los como modelo visual ou estrutural.

Regra:

```text
Home Pública — Organizações e Coletivos
≠ Visão Geral da Organização
≠ Início do Coletivo
```

Os documentos antigos podem fornecer verdade funcional sobre responsabilidades, autonomia, dados e governança, mas não o layout da nova Home.

### OC-GAP-06 — Destino final da bifurcação

O significado dos caminhos já está decidido:

- `Descobrir como participar como Organização`;
- `Descobrir como participar como Coletivo`.

Não é necessário definir URL, cadastro, plano ou onboarding para liberar um wireframe conceitual.

É necessário apenas preservar que os dois caminhos abrem **jornadas específicas de compreensão e participação**, não conversão comercial obrigatória.

### OC-GAP-07 — Copy final

A pergunta-mãe `O que podemos tornar possível juntos?` e o contrato semântico estão suficientemente consolidados.

A redação pública final de títulos, subtítulos, microcopy e CTAs pode ser lapidada depois.

Essa lapidação não deve reabrir a tese.

---

## 7. Matriz de prontidão

| Dimensão | Estado |
|---|---|
| Posicionamento da marca | ALTO |
| Tese da página | ALTO |
| Pergunta de Hero | ALTO COM LAPIDAÇÃO POSTERIOR |
| Relação com a Home principal | ALTO |
| Ontologia Pessoa / Organização / Coletivo | ALTO |
| Participante ≠ produto | ALTO |
| Organização ≠ Business | ALTO |
| Onze movimentos narrativos | ALTO |
| Confiança, dados e autonomia | ALTO |
| Hierarquia do ecossistema | ALTO |
| Bifurcação Organização / Coletivo | ALTO EM PRINCÍPIO |
| Direção visual transversal | HERDÁVEL / ALTO EM PRINCÍPIO |
| Acessibilidade e resiliência | HERDÁVEL / ALTO EM PRINCÍPIO |
| Macroexperiências próprias | LACUNA BLOQUEADORA |
| Header / Hero / CTAs desta página | LACUNA BLOQUEADORA |
| Mapa de conteúdo e prova | LACUNA BLOQUEADORA |
| Handoff específico para Design | LACUNA BLOQUEADORA |
| URLs finais / onboarding | ETAPA POSTERIOR |
| Marketing/GTM | FORA DO GATE |
| Wireframe | AINDA NÃO PRONTO |
| UI / Figma / protótipo | NÃO INICIADOS |

---

## 8. Sequência recomendada para fechar a prontidão

Antes de qualquer materialização visual, executar nesta ordem:

### P1 — Agrupamento narrativo próprio

Criar o mapa de macroexperiências da Home de Organizações e Coletivos.

Objetivo:

> transformar onze funções em uma progressão visual controlável sem perder significado.

### P2 — Navegação, Header e hierarquia de ação

Definir a relação:

```text
Header global
×
Hero da segunda Home
×
continuidade de descoberta
×
Iniciar Jornada
×
participação como Organização / Coletivo
```

### P3 — Conteúdo e prova

Criar mapa de prova e conteúdo específico, herdando `GKR-UX-HOME-SYS-001` sem duplicá-lo integralmente.

### P4 — Handoff para Design/UX/UI

Criar briefing específico que transforme as decisões anteriores em contrato utilizável por designer, agência ou ferramenta generativa.

### P5 — Reauditoria final

Reexecutar o gate pré-materialização.

Somente depois dessa reauditoria deverá existir uma decisão humana separada sobre iniciar wireframe.

---

## 9. O que não precisa ser criado antes do gate

Não é necessário criar agora:

- benchmark B2B separado;
- nova identidade visual;
- design system exclusivo para Organizações e Coletivos;
- nova taxonomia de produtos;
- planos e preços;
- páginas operacionais de Organização;
- páginas operacionais de Coletivo;
- cadastro;
- onboarding;
- arquitetura técnica;
- protótipo navegável;
- assets finais de fotografia ou vídeo;
- casos de sucesso fictícios para preencher espaços.

A segunda Home deve parecer parte da mesma Guivos, não uma submarca corporativa.

---

## 10. Gate futuro para autorizar wireframe

A futura materialização só deverá avançar quando estiverem verdadeiras todas as condições:

1. Documento Mestre permanece a autoridade semântica da página;
2. existe agrupamento de macroexperiências específico;
3. Header, Hero e CTAs possuem hierarquia de intenção definida;
4. `Iniciar Jornada` não é confundido com onboarding de Organização/Coletivo;
5. existe mapa de conteúdo e prova por movimento;
6. existem fallbacks para ausência de mídia ou prova real;
7. existe handoff específico para Design/UX/UI;
8. o handoff distingue copy de trabalho de copy final;
9. `UXA-015/016` são tratados somente como referências funcionais internas, não como modelo da Home pública;
10. desktop e mobile preservam a mesma transformação perceptiva;
11. acessibilidade e redução de movimento continuam obrigatórias;
12. produtos permanecem subordinados à ideia maior;
13. Organização não é reduzida a Business;
14. Coletivo não é transformado em produto ou comunidade criada pela Guivos;
15. o encerramento permanece em descoberta e participação, não em pressão de cadastro;
16. existe rastreabilidade entre cada macroexperiência e os movimentos do Documento Mestre;
17. uma decisão humana explícita autoriza a materialização.

---

## 11. Perguntas para futura auditoria do wireframe

Uma proposta visual futura deverá responder, no mínimo:

1. A página parece uma segunda perspectiva da mesma Guivos?
2. O visitante entende sua própria capacidade antes de conhecer produtos?
3. A página evita linguagem e estética de landing page SaaS/B2B convencional?
4. Organização e Coletivo são distintos sem parecer dois produtos?
5. A Pessoa continua reconhecível como centro da própria jornada?
6. A Guivos aparece como conexão e contexto, não como proprietária da transformação?
7. A fragmentação e a continuidade são compreendidas sem diagrama técnico obrigatório?
8. Complementaridade aparece sem reduzir o sistema a oferta × demanda?
9. Escala aparece como diversidade de capacidades, não apenas volume?
10. Confiança é sustentada por substância e prova, não por estética?
11. Intelligence não parece mecanismo de acesso irrestrito a pessoas ou dados?
12. Produtos aparecem tarde e com hierarquia coerente?
13. Business não parece produto obrigatório de toda Organização?
14. A página funciona sem animação e sem vídeo?
15. O Header continua previsível e inequívoco dentro da segunda Home?
16. `Iniciar Jornada` mantém significado próprio?
17. Os CTAs de Organização e Coletivo surgem no momento correto?
18. O design evita parecer dashboard autenticado?
19. Mobile preserva narrativa e bifurcação sem excesso de densidade?
20. A página termina abrindo um próximo caminho em vez de fechar uma venda?

---

## 12. Decisão desta auditoria

A auditoria não identifica necessidade de reabrir a tese, a ontologia dos participantes ou os onze movimentos.

A lacuna atual não é estratégica de alto nível.

Ela é de **tradução controlada entre narrativa e materialização**.

Portanto:

> **NÃO INICIAR WIREFRAME AINDA.**

Próximo estado recomendado:

```text
Documento Mestre integrado
        ↓
Auditoria de prontidão
        ↓
P1 Macroexperiências
        ↓
P2 Header / Hero / CTAs
        ↓
P3 Conteúdo / Prova
        ↓
P4 Handoff Design / UX / UI
        ↓
Reauditoria
        ↓
DECISÃO HUMANA SOBRE MATERIALIZAÇÃO
```

Regra final:

> **A Home de Organizações e Coletivos já sabe o que precisa significar. Antes de ser desenhada, ainda precisa definir com precisão como esse significado será entregue a Design sem que Design tenha de completar a estratégia por conta própria.**