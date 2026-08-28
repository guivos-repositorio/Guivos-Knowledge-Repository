---
id: GKR-UX-HOME-AUDIT-002
title: Auditoria Consolidada de Integridade da Arquitetura da Home Pública
status: draft
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-28
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
related:
  - GKR-UX-HOME-MASTER-001
normative: false
maturity: reconciled_integrity_audit_pre_materialization
---

# Auditoria Consolidada de Integridade da Arquitetura da Home Pública

## 1. Finalidade

Esta auditoria consolida a leitura arquitetural da Home pública de `guivos.com` após os refinamentos sucessivos desta frente.

Nesta versão, o audit foi reconciliado com `GKR-UX-HOME-MASTER-001 v1.0.0`, com `GKR-UX-HOME-AUDIT-001 v0.9.0`, com o fechamento do domínio narrativo que atualizou `GKR-UX-HOME-NARR-005`, `GKR-UX-HOME-NARR-001` e `GKR-UX-HOME-VAL-001`, com `GKR-UX-HOME-NAV-001 v0.4.0`, reconciliado com a fronteira GTM vigente, e com `GKR-UX-HOME-HANDOFF-001 v0.2.0`, reconciliado com o Master e os refinamentos posteriores.

O Master é a autoridade de consumo vigente da Home. Esta auditoria verifica integridade entre camadas e não o substitui.

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

> **NENHUMA CONTRADIÇÃO ESTRUTURAL CRÍTICA FOI IDENTIFICADA NA INTERPRETAÇÃO VIGENTE DA ARQUITETURA DA HOME APÓS A RECONCILIAÇÃO NARRATIVA, DE NAVEGAÇÃO E DO HANDOFF.**

A arquitetura atual apresenta coerência entre:

- posicionamento;
- Hero;
- navegação;
- participantes;
- Produtos Especializados;
- Possibilidade, Mecanismo, eventual Oportunidade real e Experiência;
- sete macroexperiências;
- prova;
- autoridade;
- autonomia;
- mobile;
- fronteira com Marketing/GTM;
- briefing e critérios de futura materialização.

Do inventário de resíduos desta auditoria:

- `RES-01` foi **resolvido** pela reconciliação de `NAV-001 v0.4.0` com a fronteira GTM vigente;
- `RES-02` foi **resolvido** pela reconciliação de `NARR-001`;
- `RES-03` foi **resolvido** pela reconciliação de `HANDOFF-001 v0.2.0` com o Master e os refinamentos posteriores.

Conclusão de maturidade:

> **A arquitetura estratégica da Home está convergida dentro do escopo atual e não necessita de novos refinamentos conceituais isolados antes de uma futura etapa de materialização, salvo nova decisão explícita ou descoberta de contradição real.**

Isso não autoriza wireframe, Figma, UI, protótipo, implementação ou publicação.

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

MACROEXPERIÊNCIA 04 — DA POSSIBILIDADE À EXPERIÊNCIA + PERTENCIMENTO
├── Movimento 06 — Da Possibilidade à Experiência
└── Movimento 07 — Pertencimento

↓

MACROEXPERIÊNCIA 05 — COERÊNCIA DO ECOSSISTEMA
└── Movimento 08 — Ecossistema / Produtos
    ├── Journey — experiência e continuidade da jornada
    ├── Mall / Travel / Business / Media / Ads — Produtos Especializados com responsabilidades próprias
    └── Intelligence — Produto Especializado transversal de inteligência / Intelligence Layer

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

Todos os sete permanecem Produtos Especializados. Essa taxonomia comum não elimina responsabilidades distintas: Journey preserva experiência e continuidade da jornada; Intelligence preserva transversalidade; e os demais Produtos Especializados preservam suas responsabilidades próprias.

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

Nenhum refinamento posterior desloca a marca para uma interpretação de marketplace, superapp, rede social, plataforma de IA ou portfólio corporativo.

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

As três camadas semânticas da Hero são:

1. pergunta-mãe;
2. amplitude / pertencimento;
3. concretização do papel da Guivos.

A terceira camada vigente deve preservar conexão, pluralidade de participantes, Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências, distinguir Possibilidade de Oportunidade, limitar Oportunidades reais à materialização externa legítima quando fizerem sentido e não prometer resultado.

Autonomia permanece princípio transversal da Home e possui explicitação própria no Movimento 10; não é requisito adicional exclusivo da terceira camada da Hero.

Formalização:

> **camadas semânticas da Hero ≠ três massas de texto simultaneamente dominantes.**

O design futuro pode trabalhar hierarquia, ritmo, progressive disclosure e composição, desde que todas as funções semânticas permaneçam compreensíveis.

---

## 7. Auditoria de coerência — participantes × produtos

### Resultado

**COERENTE.**

A arquitetura vigente distingue:

```text
Pessoa / Organização / Coletivo
= quem participa

Journey / Travel / Mall / Business / Media / Ads / Intelligence
= Produtos Especializados com responsabilidades próprias
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

**COERENTE APÓS A RECONCILIAÇÃO DO DOMÍNIO NARRATIVO.**

A leitura vigente preserva a hierarquia reconciliada do Master:

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

Os sete permanecem Produtos Especializados, mas o Movimento 08 não os achata em papéis equivalentes.

Journey preserva experiência e continuidade da jornada e **não deve virar card equivalente por convenção**.

Business é Produto Especializado B2B e não equivale ao tipo estrutural `Organização`.

Intelligence é Produto Especializado transversal / Intelligence Layer, sem deixar de ser Produto Especializado e sem se tornar autoridade decisória totalizante.

Regras:

```text
Organização
≠ Business

Intelligence transversal
≠ nova classe estrutural

JOURNEY
≠ CARD EQUIVALENTE POR CONVENÇÃO

COMPREENDER
≠ DECIDIR
```

O Movimento 08 explica coerência e não replica o launcher.

Formalização:

> **launcher responde “onde ir”; Movimento 08 responde “por que responsabilidades diferentes pertencem à mesma Guivos”.**

A arquitetura rejeita sete cards equivalentes como tradução automática dos sete Produtos Especializados.

---

## 9. Auditoria de redundância — Movimentos 02, 06 e 09

### Resultado

**SEM REDUNDÂNCIA FUNCIONAL.**

Os três territórios são diferentes:

### Movimento 02

> **“Isso existe.”**

Mostra realidade rapidamente.

### Movimento 06

> **“Uma Possibilidade pode chegar à Experiência por agência e escolha.”**

Sua cadeia de referência é:

```text
POSSIBILIDADE
→ MECANISMO
→ OPORTUNIDADE REAL, quando houver materialização externa legítima
→ ESCOLHA
→ EXPERIÊNCIA
→ CONTRIBUIÇÃO / APRENDIZADO
→ NOVO MOMENTO
```

Nem toda Possibilidade exige Oportunidade externa e nenhuma etapa implica resultado garantido.

### Movimento 09

> **“Há razões para confiar em como a Guivos lida com isso.”**

Mostra origem, critérios, método, governança, transparência e evidência verificável.

A mesma história pode alimentar mais de uma função editorial, mas não deve ser repetida como o mesmo bloco visual em diferentes pontos da Home.

---

## 10. Auditoria de complexidade — Header

### Resultado

**ARQUITETURA SEMANTICAMENTE JUSTIFICADA, COM DENSIDADE VISUAL A SER CONTROLADA PELO DESIGN.**

O Header possui múltiplas funções conceituais que seriam excessivas se tratadas como links textuais de igual peso.

A própria arquitetura mitiga esse risco por:

- launcher compacto;
- globo;
- compartilhar como utilitário;
- hierarquia de exposição;
- compactação durante o scroll;
- condensação responsiva no mobile.

Portanto, não existe fundamento arquitetural para remover itens apenas por contagem.

Regra:

> **inventário do Header ≠ elementos de igual peso visual.**

---

## 11. Auditoria de complexidade — sete macroexperiências

### Resultado

**COERENTE, DESDE QUE NÃO SEJAM MATERIALIZADAS COMO SETE BLOCOS PESADOS E AUTOSSUFICIENTES.**

O agrupamento reduz a fragmentação dos onze movimentos.

Mas o futuro design não deve converter cada macroexperiência em uma seção corporativa repetitiva com título, subtítulo, cards, CTA e divisor.

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
- Intelligence subordinado à compreensão e sem substituir decisão;
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

# 17. Resíduos documentais e reconciliações

## RES-01 — disponibilidade operacional antes do wireframe em NAV-001

A versão anterior `GKR-UX-HOME-NAV-001 v0.3.0` continha formulação segundo a qual a disponibilidade operacional dos destinos deveria ser confirmada antes do wireframe e usava existência/estado público do destino como critério para determinados acessos contextuais.

`GKR-UX-HOME-NAV-001 v0.4.0` reconciliou essa fronteira com `GKR-UX-HOME-GTM-BOUNDARY-001` e passou a distinguir explicitamente:

```text
DESTINO CONCEITUAL GOVERNADO
≠ DESTINO OPERACIONAL ATIVO
≠ DECISÃO DE LANÇAMENTO
```

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

**RESOLVIDO — a reconciliação documental de NAV-001 com a fronteira GTM vigente foi concluída.**

---

## RES-02 — descrição antiga de Business em NARR-001

O audit original registrava que `GKR-UX-HOME-NARR-001` associava Business à participação de Organizações.

Esse resíduo foi removido na reconciliação narrativa de 28/08/2026.

Interpretação vigente:

> **Organização ≠ Guivos Business.**

Guivos Business é Produto Especializado B2B.

Organização é tipo estrutural de participante.

Classificação:

**RESOLVIDO — preservado apenas como registro da reconciliação desta auditoria.**

---

## RES-03 — handoff original antecedia os refinamentos posteriores

`GKR-UX-HOME-HANDOFF-001 v0.1.0` antecedia diversos refinamentos e continha, entre outros, a terceira camada antiga da Hero, `Do possível ao vivido.` como assinatura complementar, a cadeia conceitual anterior e formulações pré-reconciliação sobre Produtos.

`GKR-UX-HOME-HANDOFF-001 v0.2.0` reconciliou o briefing com o Master e os refinamentos posteriores, preservando sua riqueza operacional e corrigindo explicitamente:

- terceira camada da Hero;
- sistema verbal e assinatura institucional;
- `Possibilidade ≠ Oportunidade`;
- camada de Mecanismo específica da passagem do Movimento 06;
- Movimento 06 como `Da Possibilidade à Experiência`;
- modelo editorial longitudinal das histórias separado da cadeia específica do Movimento 06;
- sete Produtos Especializados e papel distinto de Journey;
- `Organização ≠ Business`;
- Intelligence como Produto Especializado transversal / Intelligence Layer;
- `COMPREENDER ≠ DECIDIR`;
- fronteira entre arquitetura conceitual, futuro wireframe, disponibilidade operacional e GTM;
- critérios de prova, acessibilidade, internacionalização, fallback, anti-padrões, matriz de aceitação, perguntas de revisão e prompts futuros;
- ausência de autorização automática de materialização.

Regra de consumo vigente:

> **GKR-UX-HOME-MASTER-001 permanece a autoridade de consumo. HANDOFF-001 v0.2.0 é um briefing reconciliado e pode ser usado como aprofundamento de Design futuro dentro da precedência vigente, sem substituir o Master.**

Classificação:

**RESOLVIDO — o risco de consumo documental do handoff anterior foi encerrado.**

---

## 18. Precedência operacional de leitura desta frente

Para evitar reintrodução de decisões superadas, utilizar a seguinte regra prática:

### Autoridade de consumo

1. `GKR-UX-HOME-MASTER-001`.

### Fundação e contratos

2. Fundação vigente da Guivos;
3. `UXA-020`;
4. `UXA-021`.

### Direção e aprofundamentos

5. `GKR-UX-HOME-001`;
6. `GKR-UX-HOME-VAL-001`;
7. `GKR-UX-HOME-NARR-001`;
8. `NARR-002`, `NARR-003`, `NARR-004` e `NARR-005` em seus respectivos domínios específicos.

### Navegação

9. `GKR-UX-HOME-NAV-001 v0.4.0` como arquitetura de navegação reconciliada;
10. `NAV-002`, `NAV-003` e `NAV-004` aprofundam seus respectivos refinamentos;
11. `GKR-UX-HOME-GTM-BOUNDARY-001` governa a fronteira entre arquitetura conceitual, disponibilidade operacional, publicação e lançamento.

### Sistemas transversais

12. `GKR-UX-HOME-SYS-001`.

### Handoff

13. `GKR-UX-HOME-HANDOFF-001 v0.2.0` como briefing reconciliado para futura materialização, subordinado ao Master e às autoridades especializadas de seus respectivos domínios.

### Auditoria

14. `GKR-UX-HOME-AUDIT-001 v0.9.0`;
15. esta auditoria consolidada para integridade entre as camadas.

Regra:

> **o Master governa consumo; documentos especializados aprofundam; o handoff traduz a arquitetura para futura execução de Design; auditorias verificam integridade; nenhum audit ou handoff reabre sozinho uma decisão convergida.**

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

### Resíduos documentais conhecidos neste audit

- nenhum resíduo documental permanece aberto entre `RES-01`, `RES-02` e `RES-03`.

O fechamento desses resíduos não elimina decisões deliberadamente abertas de copy, Design, operação, GTM ou implementação.

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

A recomendação de governança permanece:

> **tratar a arquitetura estratégica da Home pública como convergida dentro do escopo atual.**

Isso significa:

- não criar novos refinamentos apenas para aumentar detalhamento documental;
- não reabrir decisões já consolidadas sem novo fundamento;
- não transformar escolhas futuras de design em novas decisões estratégicas antecipadas;
- corrigir novos resíduos documentais somente quando puderem reintroduzir semântica superada;
- registrar nova exceção somente quando surgir conflito real, nova necessidade de produto ou nova decisão explícita do fundador/governança.

Regra de controle:

> **mais documentação não significa mais maturidade quando a arquitetura já responde ao problema.**

---

## 21. Gate para a próxima etapa

A próxima etapa de produto possível é uma futura exploração de materialização visual/wireframe.

Ela somente começa mediante autorização explícita.

Até essa autorização:

- nenhuma tela deve ser criada;
- nenhum Figma deve ser iniciado;
- nenhum wireframe deve ser tratado como aprovado;
- nenhuma implementação deve começar;
- nenhuma decisão de Marketing/GTM deve ser inferida.

A reconciliação de `HANDOFF-001 v0.2.0` foi concluída exclusivamente para encerrar o risco de consumo documental e **não constitui autorização de materialização**.

Estado final desta auditoria:

> **ARQUITETURA ESTRATÉGICA CONVERGIDA — AUDITORIA RECONCILIADA — RES-01 / RES-02 / RES-03 RESOLVIDOS — MATERIALIZAÇÃO NÃO AUTORIZADA.**
