---
id: GKR-UX-HOME-AUDIT-002
title: Auditoria Consolidada de Integridade da Arquitetura da Home Pública
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-AUDIT-001
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
  - GKR-UX-HOME-GTM-BOUNDARY-001
  - GKR-UX-HOME-AUDIT-001
normative: false
---

# Auditoria Consolidada de Integridade da Arquitetura da Home Pública

## 1. Finalidade

Esta auditoria consolida a leitura arquitetural da Home pública de `guivos.com` após os refinamentos sucessivos desta frente.

Seu objetivo não é criar novas seções, wireframe, UI ou Marketing/GTM.

Ela verifica quatro dimensões:

1. coerência entre documentos;
2. redundância de funções;
3. risco de complexidade perceptiva;
4. lacunas arquiteturais reais versus itens deliberadamente deixados para etapas futuras.

A auditoria também impede que documentos anteriores sejam lidos isoladamente e reintroduzam hipóteses já superadas.

---

## 2. Resultado executivo

Resultado:

> **NENHUMA CONTRADIÇÃO ESTRUTURAL CRÍTICA FOI IDENTIFICADA NA INTERPRETAÇÃO VIGENTE DA ARQUITETURA DA HOME.**

A arquitetura atual apresenta coerência entre:

- posicionamento;
- Hero;
- navegação;
- participantes;
- produtos;
- sete macroexperiências;
- prova;
- autoridade;
- autonomia;
- mobile;
- fronteira com Marketing/GTM.

Foram identificados **três resíduos documentais de menor precedência**, descritos nesta auditoria, que não alteram a arquitetura vigente porque já possuem refinamentos posteriores explícitos.

Conclusão de maturidade:

> **A arquitetura estratégica da Home está convergida dentro do escopo atual e não necessita de novos refinamentos conceituais isolados antes de uma futura etapa de materialização, salvo nova decisão explícita ou descoberta de contradição real.**

Isso não autoriza wireframe, Figma, UI, protótipo, implementação ou merge.

---

## 3. Arquitetura vigente em uma leitura única

A Home deve ser interpretada como três sistemas coordenados:

```text
NAVEGAÇÃO PERSISTENTE
→ oferece liberdade de acesso

NARRATIVA PROGRESSIVA
→ constrói compreensão

PROVA + AUTONOMIA
→ transforma compreensão em confiança sem coerção
```

A navegação não conta a história.

A narrativa não deve impedir quem já sabe onde quer ir.

A prova não deve substituir significado nem transformar a página em relatório institucional.

---

## 4. Leitura integral da Home

```text
HEADER PERSISTENTE
├── Guivos / Home
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

↓

MACROEXPERIÊNCIA 01 — ABRIR O HORIZONTE
└── Movimento 01 — Hero

↓

MACROEXPERIÊNCIA 02 — VER O REAL E PERCEBER A AMPLITUDE
├── Movimento 02 — Possibilidades Reais
└── Movimento 03 — Amplitude

↓

MACROEXPERIÊNCIA 03 — DESCONEXÃO → CONEXÃO
├── Movimento 04 — Desconexão
└── Movimento 05 — Guivos / Conexão

↓

MACROEXPERIÊNCIA 04 — DO POSSÍVEL AO VIVIDO + PERTENCIMENTO
├── Movimento 06 — Do Possível ao Vivido
└── Movimento 07 — Pertencimento

↓

MACROEXPERIÊNCIA 05 — COERÊNCIA DO ECOSSISTEMA
└── Movimento 08 — Ecossistema / Produtos
    ├── Journey — experiência e continuidade
    ├── Travel / Mall / Media / Business / Ads — manifestações especializadas
    └── Intelligence — inteligência transversal

↓

MACROEXPERIÊNCIA 06 — AUTORIDADE + AUTONOMIA
├── Movimento 09 — Autoridade
└── Movimento 10 — Autonomia e Confiança

↓

MACROEXPERIÊNCIA 07 — REABRIR O HORIZONTE
└── Movimento 11 — Descoberta

↓

RODAPÉ
└── Mapa do Ecossistema → link
    + composição adicional deliberadamente não fechada nesta frente
```

Regra:

> **Onze funções. Sete macroexperiências de referência. Uma única narrativa.**

---

## 5. Auditoria de coerência — posicionamento

### Resultado

**COERENTE.**

A arquitetura preserva:

- possibilidade antes de produto;
- futuro sem ficção científica;
- tecnologia sem frieza;
- humanidade sem clichê;
- escala sem transformar a Home em catálogo;
- simplicidade sem superficialidade;
- autonomia sem passividade.

Nenhum refinamento posterior deslocou a marca para uma interpretação de marketplace, superapp, rede social, plataforma de IA ou portfólio corporativo.

---

## 6. Auditoria de coerência — Header × Hero

### Resultado

**COERENTE, COM RISCO DE LITERALIZAÇÃO VISUAL CONTROLADO.**

A arquitetura separa corretamente:

```text
Header
= caminhos para intenção já formada

Hero
= abrir horizonte e fazer continuar descobrindo
```

`Iniciar Jornada` pertence ao Header.

O CTA da Hero pertence à continuidade da própria Home.

Não existe necessidade estratégica de repetir `Iniciar Jornada` dentro da Hero.

### Regra adicional de controle

As três camadas semânticas da Hero:

1. pergunta-mãe;
2. amplitude / pertencimento;
3. concretização do papel da Guivos;

**não significam obrigação de apresentar três blocos textuais longos simultaneamente com o mesmo peso visual.**

Formalização:

> **camadas semânticas da Hero ≠ três massas de texto simultaneamente dominantes.**

O design futuro pode trabalhar hierarquia, ritmo, progressive disclosure e composição, desde que todas as funções semânticas permaneçam compreensíveis.

Isso é necessário para proteger simplicidade e impacto.

---

## 7. Auditoria de coerência — participantes × produtos

### Resultado

**COERENTE.**

A arquitetura vigente distingue:

```text
Pessoa / Organização / Coletivo
= quem participa

Journey / Travel / Mall / Media / Business / Intelligence / Ads
= como o ecossistema ganha forma e capacidade
```

Não existe correspondência 1:1.

Portanto:

- Pessoa ≠ Journey;
- Organização ≠ Business;
- Coletivo não depende de produto homônimo;
- produto não cria tipo de participante.

A passagem Movimento 07 → 08 preserva corretamente esta separação.

---

## 8. Auditoria de coerência — Movimento 08

### Resultado

**COERENTE APÓS OS REFINAMENTOS NARR-002 E NARR-003.**

A leitura correta é:

- Journey — experiência e continuidade;
- Travel, Mall, Media, Business e Ads — manifestações especializadas;
- Intelligence — inteligência transversal.

O Movimento 08 explica coerência e não replica o launcher.

Formalização:

> **launcher responde “onde ir”; Movimento 08 responde “por que isso pertence à mesma Guivos”.**

A arquitetura rejeita sete cards equivalentes como tradução automática dos sete componentes.

---

## 9. Auditoria de redundância — Movimentos 02, 06 e 09

### Resultado

**SEM REDUNDÂNCIA FUNCIONAL APÓS NARR-004.**

Os três territórios são diferentes:

### Movimento 02

> **“Isso existe.”**

Mostra realidade rapidamente.

### Movimento 06

> **“Isso pode sair do possível e chegar à experiência.”**

Mostra processo, escolha, experiência e continuidade.

### Movimento 09

> **“Há razões para confiar em como a Guivos lida com isso.”**

Mostra origem, critérios, método, governança, transparência e evidência verificável.

A mesma história pode alimentar mais de uma função editorial, mas não deve ser repetida como o mesmo bloco visual em diferentes pontos da Home.

---

## 10. Auditoria de complexidade — Header

### Resultado

**ARQUITETURA SEMANTICAMENTE JUSTIFICADA, COM DENSIDADE VISUAL A SER CONTROLADA PELO DESIGN.**

O Header possui oito funções conceituais principais.

Isso seria excessivo se todas fossem tratadas como links textuais de igual peso.

A própria arquitetura já mitiga esse risco por:

- launcher compacto;
- globo;
- compartilhar como utilitário;
- hierarquia de exposição;
- compactação durante o scroll;
- condensação responsiva no mobile.

Portanto, não existe fundamento arquitetural para remover itens neste momento.

Regra:

> **inventário do Header ≠ oito elementos de igual peso visual.**

---

## 11. Auditoria de complexidade — sete macroexperiências

### Resultado

**COERENTE, DESDE QUE NÃO SEJAM MATERIALIZADAS COMO SETE BLOCOS PESADOS E AUTOSSUFICIENTES.**

O agrupamento reduz a fragmentação dos onze movimentos.

Mas o futuro design não deve converter cada macroexperiência em uma seção corporativa com:

- título;
- subtítulo;
- três cards;
- CTA;
- divisor;

repetidos sete vezes.

Formalização:

> **macroexperiência ≠ template de seção.**

O ritmo deve variar entre impacto, descoberta e compreensão.

---

## 12. Auditoria de complexidade — prova

### Resultado

**COERENTE.**

A Home não deve acumular provas apenas para parecer grande.

A hierarquia vigente continua adequada:

```text
prova direta
> história documentada
> evidência institucional
> métrica
> depoimento
> afirmação institucional
```

Poucas evidências fortes continuam preferíveis a volume artificial.

---

## 13. Auditoria de comportamento — scroll e mobile

### Resultado

**COERENTE.**

A solução vigente evita dois extremos:

1. Header fixo pesado ocupando a experiência;
2. Header imprevisível que desaparece e obriga o visitante a procurá-lo.

Regra consolidada:

> **o Header permanece disponível sem permanecer dominante.**

No mobile:

> **mesma arquitetura, menor simultaneidade.**

Condensar é permitido.

Remover ou enterrar caminhos essenciais não é.

---

## 14. Auditoria de autonomia

### Resultado

**COERENTE E TRANSVERSAL.**

A autonomia não está restrita ao Movimento 10.

Ela aparece em:

- exploração pública;
- CTA da Hero de baixo compromisso;
- ausência de falsa personalização;
- escolha do momento de `Iniciar Jornada`;
- scroll não bloqueante;
- ausência de urgência artificial;
- Intelligence subordinada à decisão humana;
- prova sem causalidade exagerada.

O Movimento 10 funciona como explicitação de um princípio já vivido ao longo da Home.

---

## 15. Auditoria de fechamento — Movimento 11

### Resultado

**COERENTE.**

O Movimento 11 não precisa se transformar em fechamento de venda porque `Iniciar Jornada` já permanece disponível no Header.

Isso permite encerrar a narrativa com abertura de continuidade:

> **compreendi → confio → continuo livre → quero descobrir.**

A copy e a forma final permanecem para etapa posterior.

---

## 16. Auditoria do rodapé

### Resultado

**INTENCIONALMENTE PARCIAL.**

Está decidido apenas:

> **deve existir um link para `Mapa do Ecossistema`.**

Não está decidido nesta frente:

- composição completa do rodapé;
- demais links institucionais;
- suporte;
- legal;
- social;
- geografia;
- arquitetura da futura página `Mapa do Ecossistema`.

Essa abertura é deliberada e não deve ser preenchida por inferência.

Regra:

> **link Mapa do Ecossistema ≠ definição da página ≠ definição integral do rodapé.**

---

# 17. Resíduos documentais identificados

## RES-01 — disponibilidade operacional antes do wireframe em NAV-001

`GKR-UX-HOME-NAV-001 v0.3.0` ainda contém formulação residual segundo a qual a disponibilidade operacional dos destinos deveria ser confirmada antes do wireframe e usa verdade operacional como critério para determinados acessos contextuais.

Essa formulação é anterior à fronteira consolidada em `GKR-UX-HOME-GTM-BOUNDARY-001`.

Interpretação vigente:

> **disponibilidade de lançamento e ativação operacional não são gate da arquitetura conceitual nem do futuro wireframe.**

Verdade operacional continua obrigatória antes de publicação e ativação concreta.

Portanto:

```text
arquitetura / wireframe
≠
disponibilidade de lançamento
```

Classificação:

**RESÍDUO DOCUMENTAL SUPERADO — não é lacuna arquitetural.**

---

## RES-02 — descrição antiga de Business em NARR-001

A descrição resumida original do Movimento 08 em `GKR-UX-HOME-NARR-001` associa Business à participação de Organizações.

Essa formulação foi refinada e substituída no domínio específico por `GKR-UX-HOME-NARR-002` e `GKR-UX-HOME-NARR-003`.

Interpretação vigente:

> **Organização ≠ Guivos Business.**

Guivos Business é produto B2B especializado.

Organização é tipo estrutural de participante.

Classificação:

**RESÍDUO DOCUMENTAL SUPERADO — não é lacuna arquitetural.**

---

## RES-03 — handoff original antecede os refinamentos posteriores

`GKR-UX-HOME-HANDOFF-001 v0.1.0` foi criado antes de:

- NARR-002;
- NARR-003;
- NARR-004;
- NARR-005;
- NAV-002;
- NAV-003;
- NAV-004;
- GTM-BOUNDARY-001;
- AUDIT-001 em suas revisões posteriores.

Ele permanece válido como briefing-base, mas não deve ser utilizado isoladamente como snapshot final da arquitetura.

Regra de consumo:

> **HANDOFF-001 deve ser lido junto aos refinamentos posteriores desta frente. Em conflito específico, prevalece o refinamento posterior do mesmo domínio.**

Classificação:

**RISCO DE CONSUMO DOCUMENTAL — não é falha da arquitetura.**

---

## 18. Precedência operacional de leitura desta frente

Para evitar reintrodução de decisões superadas, utilizar a seguinte regra prática:

### Fundação e contratos

1. Fundação vigente da Guivos;
2. `UXA-020`;
3. `UXA-021`.

### Direção da Home

4. `GKR-UX-HOME-001`;
5. `GKR-UX-HOME-VAL-001`.

### Narrativa específica

6. `GKR-UX-HOME-NARR-001` como base;
7. `NARR-002`, `NARR-003`, `NARR-004` e `NARR-005` prevalecem em seus respectivos domínios específicos.

### Navegação

8. `GKR-UX-HOME-NAV-001` como base;
9. `NAV-002`, `NAV-003` e `NAV-004` prevalecem em seus respectivos refinamentos.

### Sistemas transversais e fronteira

10. `GKR-UX-HOME-SYS-001`;
11. `GKR-UX-HOME-GTM-BOUNDARY-001`.

### Auditoria

12. `GKR-UX-HOME-AUDIT-001`;
13. esta auditoria consolidada para integridade entre as camadas.

---

## 19. Lacunas reais restantes

Não foram encontradas lacunas estratégicas críticas que exijam nova arquitetura antes de uma futura materialização.

Permanecem deliberadamente abertos:

### Copy

- redação final da Hero;
- label final do CTA de descoberta;
- copy das macroexperiências;
- microcopy de navegação.

### Design

- layout;
- grid;
- tipografia;
- paleta;
- composição;
- fotografia/vídeo;
- altura exata do Header;
- breakpoints;
- forma do menu mobile;
- movimento e microinterações;
- número final de regiões técnicas.

### Rodapé

- composição adicional além do link `Mapa do Ecossistema`.

### Etapas posteriores

- Marketing/GTM;
- disponibilidade de produtos;
- ativação por mercado;
- operação concreta dos destinos;
- arquitetura da página `Mapa do Ecossistema`;
- fluxos internos de produtos;
- implementação.

Esses itens não justificam continuar aumentando a arquitetura conceitual da Home nesta frente.

---

## 20. Decisão de convergência

A partir desta auditoria, a recomendação de governança é:

> **tratar a arquitetura estratégica da Home pública como convergida dentro do escopo atual.**

Isso significa:

- não criar novos refinamentos apenas para aumentar detalhamento documental;
- não reabrir decisões já consolidadas sem novo fundamento;
- não transformar escolhas futuras de design em novas decisões estratégicas antecipadas;
- registrar nova exceção somente quando surgir conflito real, nova necessidade de produto ou nova decisão explícita do fundador/governança.

Regra de controle:

> **mais documentação não significa mais maturidade quando a arquitetura já responde ao problema.**

---

## 21. Gate para a próxima etapa

A próxima etapa possível é uma futura exploração de materialização visual/wireframe.

Ela somente começa mediante autorização explícita.

Até essa autorização:

- nenhuma tela deve ser criada;
- nenhum Figma deve ser iniciado;
- nenhum wireframe deve ser tratado como aprovado;
- nenhuma implementação deve começar;
- nenhuma decisão de Marketing/GTM deve ser inferida.

Estado final desta auditoria:

> **ARQUITETURA ESTRATÉGICA CONVERGIDA — MATERIALIZAÇÃO NÃO AUTORIZADA.**
