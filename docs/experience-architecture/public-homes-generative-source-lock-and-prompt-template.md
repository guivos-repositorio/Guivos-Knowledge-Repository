---
id: GKR-UX-HOMES-GENINPUT-001
title: Homes Públicas — Source Lock e Contrato de Consumo para Designer e Sistemas de IA
status: active
version: 3.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: v6_designer_ai_consumption_contract_candidate
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
---

# Homes Públicas — Source Lock e Contrato de Consumo para Designer e Sistemas de IA

## 1. Finalidade

Este documento define como uma Home recebe um contexto fechado, rastreável e seguro para:

- leitura humana;
- trabalho da designer;
- uso opcional de IA;
- revisão e autoauditoria.

Ele não é um prompt para criar Figma automaticamente.

## 2. Unidade de trabalho

A menor unidade segura é:

```text
HOME
+
CHECKPOINT
+
AUTHORIZED SOURCES
+
INVARIANTS
+
EIGHT INFORMATION CLASSES
+
REAL DATA RULES
+
PROHIBITED INFERENCES
+
OPEN QUESTIONS
```

Uma instrução solta para “criar a Home da Guivos” não constitui contexto governado.

## 3. Autoria

```text
DESIGNER
→ HUMAN CREATIVE OWNER
→ DECIDES / CURATES / AUTHORS

AI
→ OPTIONAL ASSISTANT

AI OUTPUT
→ CANDIDATE

AI OUTPUT
≠ CANONICAL TRUTH
≠ DESIGN APPROVAL
≠ OFFICIAL FIGMA
```

## 4. Source Lock v6

Cada `00-LEIA-PRIMEIRO` deverá materializar um Source Lock equivalente a:

```yaml
source_lock:
  home: "<nome>"
  purpose: "design source package"
  gkr_checkpoint:
    commit: "<sha>"
  authorized_sources:
    - id: "<GKR-ID>"
      version: "<version>"
      path: "<path>"
      blob_sha: "<sha>"
      role: "<master | product | authority | media_supply | common>"
  reading_order:
    human: []
    ai_context: []
  canonical_invariants: []
  design_creative: []
  content_candidate: []
  design_hypothesis: []
  prototype_placeholder: []
  real_data_required: []
  open_questions: []
  prohibited_inference: []
  visual_references:
    authority: "INSPIRATION_ONLY"
    items: []
```

Os nomes podem variar; o conteúdo semântico é obrigatório.

## 5. Integridade das fontes

As fontes do snapshot devem vir do mesmo checkpoint canônico.

Cada fonte deve possuir:

- ID;
- versão;
- path;
- blob SHA;
- função no pacote.

Se uma fonte mudar materialmente depois da emissão, a Home afetada deve ser revalidada antes de nova execução.

## 6. Pacote comum v6

Todas as Homes consomem:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v2.0.0`;
2. `GKR-UX-HOMES-GENINPUT-001 v3.0.0`;
3. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v2.0.0`;
4. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.0`.

As fontes específicas são definidas no Manifesto v6.

## 7. Ordem de consumo humano

A designer deve começar por:

1. `00-LEIA-PRIMEIRO`;
2. Master da Home;
3. contratos/Source Locks específicos;
4. autoridades de Produto quando presentes;
5. reconciliações editoriais/mídia;
6. fontes comuns quando precisar aprofundar método e aceite.

O `00-LEIA-PRIMEIRO` pode indicar outra ordem quando houver dependência específica.

## 8. Ordem de contexto para IA

IA deve receber apenas o necessário para a tarefa.

### Síntese

`LEIA-PRIMEIRO + Master + fonte diretamente relevante`.

### Ideação visual

`LEIA-PRIMEIRO + Master + Handoff`.

### Content Design

`LEIA-PRIMEIRO + Master + autoridades de copy/brand aplicáveis`.

### Auditoria

`LEIA-PRIMEIRO + artefato/candidato + fontes que governam os critérios auditados`.

Não carregar documentos das oito Homes simultaneamente por conveniência.

## 9. Oito classes

### CANONICAL

Verdade vigente. Deve sobreviver à materialização.

### DESIGN_CREATIVE

Liberdade da designer: identidade visual, tipografia, cor, composição, mídia, motion, componentes e outras escolhas não congeladas.

### CONTENT_CANDIDATE

Texto/label/tom proposto e ainda não aprovado.

### DESIGN_HYPOTHESIS

Solução reversível de UX/Design que testa interpretação sem alterar produto.

### PROTOTYPE_PLACEHOLDER

Conteúdo provisório para testar forma/volume/hierarquia.

### REAL_DATA_REQUIRED

Informação que precisa de lastro para parecer factual.

### OPEN_QUESTION

Decisão ainda aberta. Pode exigir solução tolerante à variabilidade, mas não resposta inventada.

### PROHIBITED_INFERENCE

Regra, claim, dado ou relação que não pode ser criada para preencher uma lacuna.

## 10. Regra de promoção

```text
AI SUGGESTION
→ CANDIDATE

DESIGN HYPOTHESIS
→ HYPOTHESIS

PLACEHOLDER
→ PLACEHOLDER

HUMAN APPROVAL
→ MAY APPROVE DESIGN DIRECTION

EVIDENCE / GOVERNED DECISION
→ MAY CHANGE INFORMATION CLASS
```

Aparência refinada não promove classe.

## 11. Conteúdo e mídia

A designer pode selecionar, produzir ou gerar conteúdo visual livremente.

Quando imagem, vídeo ou texto puder ser interpretado como:

- pessoa real;
- cliente;
- parceiro;
- case;
- depoimento;
- destino operado;
- oferta;
- campanha;
- produto disponível;
- resultado;
- métrica;

ele deve ter lastro ou permanecer claramente conceitual/provisório.

## 12. Benchmarks e referências

Referências externas devem ser identificadas como `INSPIRATION_ONLY`.

Podem inspirar:

- ritmo;
- composição;
- navegação;
- motion;
- tratamento de mídia;
- comportamento responsivo;
- linguagem gráfica.

Não podem importar silenciosamente:

- modelo de produto;
- taxonomia;
- promessa;
- claim;
- dado;
- modelo comercial;
- autoridade;
- identidade institucional de outra marca.

```text
REFERENCE INSPIRES
SOURCE GOVERNS
```

## 13. Uso do arquivo histórico guivos.com 2.0

`guivos.com 2.0` pode ser consultado pela designer como referência de ativos, sistema existente e decisões anteriores.

Seu uso é opcional.

```text
guivos.com 2.0
→ REFERENCE / CONSULTATION

guivos.com 2.0
≠ CURRENT HOME AUTHORITY
≠ MANDATORY VISUAL BASELINE
```

## 14. Contrato para IA

Quando IA for utilizada, a instrução pode seguir este modelo:

> Você está apoiando o trabalho de Design da Home **[HOME]** da Guivos.  
> Use somente as fontes autorizadas no Source Lock como verdade de produto.  
> Preserve todos os itens `CANONICAL` e `PROHIBITED_INFERENCE`.  
> Trate `DESIGN_CREATIVE` como espaço aberto à criatividade da designer.  
> Propostas de copy são `CONTENT_CANDIDATE`.  
> Propostas de UX/forma ainda não aprovadas são `DESIGN_HYPOTHESIS`.  
> Conteúdo sem lastro é `PROTOTYPE_PLACEHOLDER` ou `REAL_DATA_REQUIRED`, conforme o caso.  
> Não transforme ausência de informação em fato, funcionalidade, parceiro, métrica, oferta, preço, disponibilidade ou promessa.  
> Seu papel é apoiar análise, ideação ou auditoria. A designer mantém autoria e decisão.

O artefato esperado deve ser especificado conforme a tarefa: síntese, alternativas, mapa de informação, Content Design candidato, crítica, checklist ou outra forma de apoio.

## 15. IA não é obrigatória

Se a designer não utilizar IA:

- nenhum passo substitutivo é exigido;
- o Source Lock continua sendo seu guia de leitura;
- a entrega continua plenamente válida.

## 16. Lacuna descoberta durante Design

Quando Design ou IA revelar uma decisão não governada:

```text
LACUNA
↓
CLASSIFICAR

SE NÃO BLOQUEADORA
→ OPEN_QUESTION
→ CRIAR SOLUÇÃO TOLERANTE À VARIAÇÃO

SE BLOQUEADORA
→ PARAR O PONTO AFETADO
→ CONSULTAR / DECIDIR / RECONCILIAR NO GKR
```

Não preencher silenciosamente.

## 17. Conteúdo variável

A solução deve tolerar, quando aplicável:

- tradução mais longa;
- ausência/presença de imagem;
- ausência/presença de preço;
- indisponibilidade;
- erro;
- loading;
- empty state;
- diferentes comprimentos de título;
- labels de proveniência/patrocínio;
- dados reais substituindo placeholders.

Variabilidade previsível não é motivo para inventar dado.

## 18. Registro mínimo de uma sessão de IA

Se uma saída de IA for usada materialmente na direção de Design, registrar no trabalho da designer ou na documentação de decisão:

- Home;
- finalidade;
- fontes usadas;
- ferramenta, quando relevante;
- principais hipóteses incorporadas;
- conteúdo candidato incorporado;
- itens rejeitados ou corrigidos, quando material.

Não é necessário registrar cada uso trivial de IA.

## 19. Autoauditoria

Antes de aprovar uma direção:

- [ ] fonte correta por Home;
- [ ] nenhum documento de outra Home governou por engano;
- [ ] `CANONICAL` preservado;
- [ ] liberdade visual permaneceu livre;
- [ ] conteúdo candidato identificado;
- [ ] placeholders não parecem prova;
- [ ] dados factuais possuem lastro;
- [ ] inferências proibidas ausentes;
- [ ] desktop/mobile preservam significado;
- [ ] acessibilidade essencial considerada;
- [ ] IA não foi tratada como autoridade;
- [ ] nenhuma lacuna de produto foi resolvida apenas porque era necessário desenhar.

## 20. Estado

```text
SOURCE LOCK / DESIGNER + AI CONSUMPTION CONTRACT
→ v3.0.0 CANDIDATE

V6 SNAPSHOT
→ NOT_EMITTED

AI
→ OPTIONAL / NON-AUTHORITATIVE

OFFICIAL DESIGN AUTHOR
→ HUMAN DESIGNER

DIRECT GKR/AI FIGMA MATERIALIZATION
→ OUT_OF_SCOPE
```
