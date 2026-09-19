---
id: GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
title: Homes Públicas — Prontidão de Produção de Design e Contrato Figma/IA
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: post_audit_design_production_readiness_pre_release
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-HOME-MASTERS-REMEDIATION-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-BRAND-SIGNATURE-001
  - GOG-001
---

# Homes Públicas — Prontidão de Produção de Design e Contrato Figma/IA

## 1. Finalidade

Esta autoridade prepara as oito Homes públicas da Guivos para uma contratação real de Design em que Figma Make ou ferramenta equivalente pode ser usada para prototipação antes da construção definitiva no Figma.

O objetivo é reduzir a zero os findings materiais documentais antes do release de produção, sem transformar documentação em direção artística.

## 2. Resultado executivo

Baseline auditada: `main @ fada353688e26047a8eb8f45a8de67af0aa9b3d0`.

Estado desta revisão:

- arquitetura semântica das oito Homes: documentada e reconciliada;
- método de handoff: reconciliado pós-auditoria;
- template generativo: expandido para oito Homes;
- contrato de protótipo e entrega Figma: definido por esta autoridade;
- pacote v5: preparado pelo Manifesto v5, ainda dependente de emissão pós-merge;
- Design Production Release: não concedido por este documento.

## 3. Princípio superior — significado governado, criatividade livre

A Guivos não quer engessar a designer. Identidade visual não é um input canônico obrigatório desta frente.

Pertencem à liberdade criativa da designer:

- tipografia e escalas tipográficas;
- paleta e relações cromáticas;
- fotografia, vídeo, imagem gerada, ilustração e iconografia;
- grid, composição, densidade, respiro e ritmo;
- componentes e linguagem gráfica;
- motion, microinterações e atmosfera;
- tratamento visual de Header, Hero, CTAs e seções;
- tom de voz, headlines de apoio e microcopy quando não houver texto literal congelado;
- forma de tornar as oito Homes reconhecíveis como uma família sem repetir o mesmo template.

Não existe obrigação de reproduzir visual histórico, snapshot antigo, palette anterior, fonte anterior ou estética pré-existente.

Depois da aprovação humana da direção de protótipo, a solução escolhida passa a ser a baseline criativa daquela entrega e deve ser documentada no Figma final.

## 4. O que permanece governado

A liberdade visual não pode alterar:

- nomes oficiais de Guivos e Produtos Especializados;
- papéis de Pessoa, Organização e Coletivo;
- papel e fronteira de cada Home;
- `Possibilidade ≠ Oportunidade`;
- `COMPREENDER ≠ DECIDIR` e demais invariantes de Intelligence;
- distinção entre relevância orgânica, publicidade, recomendação e destaque;
- regras de autonomia, privacidade, causalidade e explicabilidade;
- realidade operacional, disponibilidade, preço, parceiro, case, métrica ou prova;
- assinatura institucional quando utilizada: `Possibility, lived.` / `Possibilidade, vivida.`;
- copy explicitamente classificada como congelada por autoridade específica.

## 5. Auditoria de produção — findings de baseline

### F-01 — snapshot v4 superado

O snapshot v4 nasceu de `f900318af746ba25e3bb18d18bfddee5654620c7`; a baseline desta auditoria está 785 commits à frente. Cinco das 31 fontes do v4 sofreram alteração, incluindo Handoff comum, Masters Pessoa/O/C e seus GENINPUTs.

Decisão: v4 permanece histórico e não pode ser entregue como pacote atual.

### F-02 — gates temporais da Auditoria Integral estavam obsoletos

Handoff, Manifest, Template e Flow ainda continham linguagem de suspensão durante auditoria, embora a auditoria global esteja concluída.

Decisão: reconciliar os quatro documentos para estado pós-auditoria.

### F-03 — template ainda descrevia cinco Homes

Decisão: `GKR-UX-HOMES-GENINPUT-001 v2.0.0` cobre as oito Homes.

### F-04 — Source Locks operacionais apontavam checkpoints antigos

Pessoa/O-C já estavam explicitamente reclassificados como evidência histórica; Mall, Travel, Media, Business, Ads e Intelligence também registravam checkpoints anteriores.

Decisão: o pacote v5 não usa GENINPUT histórico como autoridade operacional. Cada `LEIA-PRIMEIRO` do v5 funciona como Source Lock operacional daquela Home e registra o checkpoint exato da emissão.

### F-05 — aceite final do Figma não estava suficientemente determinístico

Decisão: este documento estabelece o contrato mínimo de produção e aceite sem definir estética.

### F-06 — conteúdo aberto precisava de classificação por estágio

Decisão: toda informação não consolidada deve usar uma das classes da seção 8.

### F-07 — ausência de identidade visual canônica

Reclassificação humana: **não é gap**. É liberdade deliberada de Design.

## 6. Pacote fonte v5 por Home

Três autoridades comuns acompanham todas as Homes:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.5.0`;
2. `GKR-UX-HOMES-GENINPUT-001 v2.0.0`;
3. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.0.0`.

Fontes específicas:

### Pessoa
- `GKR-UX-HOME-MASTER-001 v1.0.2`;
- `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### Organizações e Coletivos
- `GKR-UX-HOME-OC-MASTER-001 v1.0.0`;
- `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### Mall
- `GKR-UX-HOME-MALL-MASTER-001 v1.0.0`;
- `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`;
- contratos Mall de `GKR-HOME-MASTERS-REMEDIATION-001 v1.3.0`.

### Travel
- `GKR-UX-HOME-TRAVEL-MASTER-001 v1.0.0`;
- `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`;
- contratos Travel de `GKR-HOME-MASTERS-REMEDIATION-001 v1.3.0`.

### Media
- `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.0`;
- `GPA-005 v1.2.0`.

### Ads
- `GKR-UX-HOME-ADS-MASTER-001 v1.0.0`;
- `GPA-007 v1.3.0`.

### Business
- `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0`;
- `GKR-UX-HOME-BUSINESS-MASTER-001 v1.0.0`;
- `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
- `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
- `GPA-004 v1.6.0`.

### Intelligence
- `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
- `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
- `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1`;
- `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
- `GPA-006 v2.0.0`.

O snapshot v5 deve capturar todas as fontes do mesmo commit canônico pós-merge e registrar seus SHAs.

## 7. Regra de isolamento para IA

Uma execução de Figma Make trabalha uma Home por vez. Não carregar documentos específicos das oito Homes simultaneamente.

A ferramenta deve receber: `LEIA-PRIMEIRO/SOURCE LOCK` daquela Home + três fontes comuns + fontes específicas daquela Home.

Output inicial obrigatório: `EXPLORAÇÃO / NÃO CANÔNICA`.

## 8. Classes obrigatórias de informação

- `CANONICAL` — deve ser preservado;
- `DESIGN CREATIVE` — pode ser criado livremente pela designer;
- `CONTENT CANDIDATE` — copy/tom proposto, sujeito a aprovação humana;
- `PROTOTYPE PLACEHOLDER` — permitido para testar estrutura; nunca pode parecer fato real;
- `REAL DATA REQUIRED` — preço, disponibilidade, case, parceiro, métrica, depoimento ou prova que exige fonte;
- `PROHIBITED INFERENCE` — não pode ser criado para preencher layout.

Nenhuma lacuna deve ser silenciosamente convertida em realidade.

## 9. Conteúdo, imagem e mídia

A designer pode selecionar, produzir ou gerar imagens e mídia de acordo com sua criatividade. O GKR não prescreve estética.

Regras de integridade:

- imagem conceitual não pode ser apresentada como case/evidência real;
- logos de terceiros exigem relação/autorização aplicável;
- preço, avaliação, número de usuários, disponibilidade e resultados não podem ser inventados;
- conteúdo gerado para protótipo deve ser reconhecível internamente como candidato ou placeholder;
- no Figma final, assets externos devem possuir origem/licença ou condição de uso registrada;
- mídia essencial deve possuir fallback e não pode carregar sozinha o significado da página.

## 10. Figma Make — gate obrigatório de protótipo

A exploração generativa antecede a construção definitiva.

Sequência obrigatória:

1. carregar pacote v5 isolado da Home;
2. gerar exploração/protótipo;
3. executar autoauditoria contra Source Lock;
4. revisão humana de significado, conteúdo, UX, responsividade e direção criativa;
5. registrar decisões aceitas, rejeitadas e lacunas;
6. somente após aprovação humana, construir/refinar o Figma definitivo.

A designer não é obrigada a copiar a proposta do Figma Make. A ferramenta serve para visualizar e testar possibilidades.

## 11. Contrato mínimo do Figma definitivo

O contrato abaixo governa qualidade e editabilidade, não estética.

Cada Home entregue deve possuir:

- versão desktop e mobile completas;
- comportamento intermediário/responsivo resolvido ou documentado;
- frames e layers nomeados de forma compreensível;
- Auto Layout/constraints quando contribuírem para responsividade e manutenção;
- componentes reutilizáveis para padrões recorrentes;
- variants/properties/states quando um componente possuir comportamentos diferentes;
- estados necessários da navegação e interações principais;
- Header, menus/launcher, CTAs e scroll representados conforme aplicável;
- protótipo navegável das interações essenciais;
- tratamento de loading/empty/error/unavailable apenas quando a Home realmente exigir esses estados;
- organização de assets;
- indicação de origem/licença para assets externos aplicáveis;
- documentação das escolhas criativas aprovadas: cores, tipografia, estilos, componentes e demais foundations criadas pela designer;
- acessibilidade considerada desde a solução: contraste, foco, teclado, texto ampliado, reduced motion, touch targets, mídia e ordem semântica;
- internacionalização tolerando expansão/contração de texto;
- nenhuma dependência de hover ou motion para entendimento essencial.

A foundations page ou biblioteca visual criada pela designer é **entrega derivada da direção aprovada**, não identidade canônica pré-imposta.

## 12. Coerência entre as oito Homes

Objetivo: uma mesma Guivos, oito expressões adequadas ao papel de cada Home.

```text
MESMA FAMÍLIA
≠ MESMO TEMPLATE

PERSONALIDADE DIFERENTE
≠ MARCA DIFERENTE
```

A coerência pode emergir de qualidade, princípios, interação, linguagem e sistema criado pela designer. Não é necessário forçar mesmas cores, mesmos blocos ou mesma composição.

## 13. Critérios de aceite do protótipo

Antes de iniciar o Figma definitivo:

- zero divergência material de significado;
- nenhum produto/participante confundido;
- nenhuma informação fictícia apresentada como fato;
- mobile possui solução própria, não mero empilhamento automático;
- a direção criativa foi aprovada por humano;
- copy candidata relevante foi aprovada ou marcada para substituição;
- questões abertas possuem destino explícito.

## 14. Critérios de aceite do Figma final

A entrega pode ser aceita quando:

1. as oito Homes contratadas estão completas no escopo combinado;
2. desktop/mobile e responsividade estão resolvidos;
3. componentes e estados recorrentes são reutilizáveis;
4. protótipo demonstra interações essenciais;
5. nenhum asset essencial está ausente;
6. nenhuma fonte/asset externo essencial tem condição de uso desconhecida;
7. não existem claims, parceiros, dados ou disponibilidade fictícios sem rótulo;
8. acessibilidade estrutural está considerada;
9. foundations criadas pela designer estão documentadas no arquivo;
10. a solução permanece fiel aos contratos semânticos;
11. a solução preserva criatividade e originalidade, sem se reduzir a template de benchmark;
12. não há finding material aberto.

## 15. Gate de emissão v5 e release

Antes de qualquer início definitivo:

```text
MERGE DO PACOTE DE PRONTIDÃO
↓
CAPTURAR MAIN PÓS-MERGE
↓
REVALIDAR 26/26 FONTES CANÔNICAS DO MANIFESTO V5
↓
GERAR 8 LEIA-PRIMEIRO / SOURCE LOCKS OPERACIONAIS
↓
MATERIALIZAR SNAPSHOT EXTERNO V5
↓
VALIDAR REPRODUTIBILIDADE / ISOLAMENTO
↓
SEMANTIC + MECHANICAL
↓
REVISÃO INDEPENDENTE
↓
ZERO FINDING MATERIAL ABERTO
↓
ATO HUMANO EXPLÍCITO DE DESIGN PRODUCTION RELEASE
```

## 16. Estado

```text
DESIGN PRODUCTION READINESS DOCUMENTATION
→ PREPARED

VISUAL IDENTITY CANONICALIZATION
→ NOT REQUIRED / DELIBERATELY DESIGN-OWNED

V5 SNAPSHOT
→ NOT YET EMITTED

DESIGN PRODUCTION RELEASE
→ NOT_GRANTED

FIGMA MAKE EXECUTION
→ NOT YET RELEASED

FINAL FIGMA PRODUCTION
→ NOT YET RELEASED
```
