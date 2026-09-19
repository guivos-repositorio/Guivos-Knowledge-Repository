---
id: GKR-UX-HOMES-GENINPUT-001
title: Homes Públicas — Source Lock, Brief de Design e Prompt Opcional para IA
status: active
version: 2.1.0
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-HANDOFF-001
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
related:
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GPA-005
  - GKR-UX-HOME-ADS-MASTER-001
  - GPA-007
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GPA-004
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GPA-006
normative: true
maturity: manual_first_ai_optional_source_lock_template
---

# Homes Públicas — Source Lock, Brief de Design e Prompt Opcional para IA

## 0. Gate pós-auditoria

A Auditoria Integral está concluída. Este template é a autoridade comum para preparar o Source Lock e o brief de consumo das oito Homes. Quando a designer optar por usar IA, o mesmo registro também governa o prompt e o contexto fornecidos à ferramenta.

```text
TEMPLATE
→ ACTIVE / 8 HOMES

V4 HISTORICAL SOURCE LOCKS
→ PROVENANCE ONLY WHEN CHECKPOINT-SUPERSEDED

V5 OPERATIONAL SOURCE LOCK
→ EMITTED / 8 OF 8 / FROZEN WITH SNAPSHOT V5

DESIGNER MANUAL CREATION
→ PRIMARY OPERATING MODEL

AI / GENERATIVE SUPPORT
→ OPTIONAL
→ TOOL-AGNOSTIC
```

A designer possui ampla liberdade criativa. Quando houver uso de IA, a ferramenta também pode propor forma, mas não pode completar lacunas de verdade factual ou arquitetura por inferência.

---

## 1. Finalidade

Este documento transforma o controle semântico estabelecido por `GKR-UX-HOMES-DESIGN-HANDOFF-001` em um procedimento operacional reutilizável para consumo humano pela designer e, opcionalmente, para apoio de sistemas de IA.

Ele define:

- como congelar as fontes de uma execução;
- quais metadados precisam acompanhar o input;
- como compor um brief de Design completo;
- como compor um prompt opcional de IA sem transferir autoridade arquitetural para a ferramenta;
- como distinguir decisão canônica, liberdade de Design, hipótese e lacuna;
- como registrar a saída para posterior validação humana;
- como impedir que outputs exploratórios se tornem decisões do GKR por inércia.

Este documento não cria wireframes, layouts, componentes, UI final ou identidade visual para nenhuma Home.

> **A designer recebe um contexto governado sem direção artística pré-imposta. Quando usar IA, a ferramenta recebe o mesmo contexto e nenhuma autoridade para completar a arquitetura da Guivos por conta própria.**

---

## 2. Relação com o handoff canônico

A autoridade entre os dois documentos é:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
→ governa a fase de Design, o pacote de fontes, as liberdades e as fronteiras

GKR-UX-HOMES-GENINPUT-001
→ governa como o Source Lock, o brief da designer e o uso opcional de IA são preparados, registrados e validados
```

Este documento não substitui o handoff nem resume os Documentos Mestres.

Ele operacionaliza o princípio:

> **O GKR governa o significado. A designer governa a expressão criativa. Sistemas de IA podem ampliar a exploração quando escolhidos pela designer. A validação reconecta forma e significado.**

---

## 3. Unidade de trabalho governada

Cada Home entregue à designer deve possuir uma **unidade de trabalho identificável**, baseada em Source Lock e brief. Se houver uso relevante de IA, esse uso também deve permanecer rastreável dentro da mesma unidade.

Uma execução possui:

```text
SOURCE LOCK
+
FONTES AUTORIZADAS
+
OBJETIVO
+
BRIEF DE DESIGN
+
PROMPT CONTROLADO, SE HOUVER IA
+
OUTPUT CRIATIVO / EXPLORATÓRIO
+
REGISTRO DE HIPÓTESES
+
VALIDAÇÃO HUMANA
```

Não existe uso governado de IA quando apenas se envia uma instrução genérica como:

> “Crie a Home da Guivos.”

Esse tipo de input transfere lacunas demais para a ferramenta e aumenta o risco de ela criar produto, narrativa, estrutura, prova ou linguagem não autorizados.

---

## 4. Source Lock

O **Source Lock** é o registro mínimo que congela o contexto de uma execução.

Ele deve ser preparado antes da geração.

### 4.1 Template normativo

```yaml
source_lock:
  execution_id: "<identificador único>"
  home: "<nome da Home>"
  home_authority_id: "<ID do Documento Mestre>"
  phase: "<arquitetura_visual | wireframe | ux | direcao_visual | ui | prototipo>"
  objective: "<o que esta execução precisa explorar>"

  gkr_checkpoint:
    repository: "guivos-repositorio/Guivos-Knowledge-Repository"
    commit_sha: "<SHA exato da main ou checkpoint aprovado>"

  authorized_sources:
    - role: "handoff"
      id: "GKR-UX-HOMES-DESIGN-HANDOFF-001"
      version: "<versão>"
      path: "docs/experience-architecture/public-homes-design-handoff.md"
    - role: "master"
      id: "<ID do Documento Mestre>"
      version: "<versão>"
      path: "<path>"
    - role: "complementary"
      id: "<ID do contrato complementar>"
      version: "<versão>"
      path: "<path>"

  additional_authorized_sources: []

  invariants:
    - "<decisão que não pode ser reinterpretada>"

  information_classes:
    canonical:
      - "<decisão que deve ser preservada>"
    design_creative:
      - "<aspecto deliberadamente aberto à criação>"
    content_candidate:
      - "<copy/tom/label proposto sujeito a aprovação>"
    design_hypothesis:
      - "<hipótese de solução a testar>"
    prototype_placeholder:
      - "<conteúdo provisório permitido>"
    real_data_required:
      - "<informação que exige fonte real>"
    open_question:
      - "<decisão ainda aberta com destino explícito>"
    prohibited_inference:
      - "<conteúdo/regra/claim que não pode ser inventado>"

  content_state:
    real_content_available: "<yes | partial | no>"
    placeholders_allowed: true
    placeholder_rules: "<regras específicas>"

  tool:
    name: "<ferramenta utilizada>"
    purpose: "exploração e materialização"

  expected_output_status: "EXPLORAÇÃO"
```

Os nomes de campos são um modelo operacional. Eles podem ser materializados em formulário, documento, issue, planilha ou outro mecanismo desde que o conteúdo semântico obrigatório seja preservado.

---

## 5. Integridade das fontes

### 5.1 Um único checkpoint

As fontes de uma execução devem, preferencialmente, ser extraídas do mesmo checkpoint do GKR.

Não combinar silenciosamente:

- Documento Mestre de um commit;
- reconciliação de outro commit;
- handoff copiado de uma versão anterior;
- decisões de conversa posteriores sem governança.

Se uma fonte mudar de forma material após o Source Lock, a execução deve ser:

- repetida; ou
- explicitamente revalidada contra a nova versão.

### 5.2 ID + versão + path + SHA

O Source Lock deve registrar:

- ID governado;
- versão do documento;
- path;
- SHA do checkpoint.

O nome do arquivo isolado não é prova suficiente de atualidade.

### 5.3 Documento integral como preferência

Quando a ferramenta permitir anexar ou consumir os documentos integrais, essa é a forma preferida.

Quando houver limitação de tamanho, pode-se utilizar **extrato controlado**, desde que:

- a origem seja identificada;
- a seleção seja humana e deliberada;
- não sejam removidas exceções que alterem o sentido;
- o extrato não seja apresentado como se fosse o documento integral;
- a hierarquia das fontes continue explícita.

> **Resumir para caber não autoriza simplificar o significado.**

---

## 6. Pacotes autorizados das oito Homes

A execução deve utilizar somente o pacote correspondente à Home em trabalho, salvo ampliação deliberada registrada no Source Lock.

### 6.0 Fontes comuns obrigatórias

Todas as oito Homes recebem exatamente estas quatro autoridades comuns do Manifesto v5:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.5.0` — `docs/experience-architecture/public-homes-design-handoff.md`;
2. `GKR-UX-HOMES-GENINPUT-001 v2.0.0` — `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — este documento;
3. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.0.0` — `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md`;
4. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v2.0.0` — `docs/experience-architecture/public-homes-design-delivery-operational-flow.md`.

Essas quatro fontes comuns não substituem as autoridades específicas da Home. Elas governam processo, taxonomia operacional, liberdade criativa, uso de IA, sequência de execução e critérios de produção/aceite.

### 6.1 Home Pública — Pessoa

Fontes específicas:

- `GKR-UX-HOME-MASTER-001 v1.0.2` — `docs/experience-architecture/public-home-master-document.md`;
- `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0` — `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`.

### 6.2 Home Pública — Organizações e Coletivos

Fontes específicas:

- `GKR-UX-HOME-OC-MASTER-001 v1.0.0` — `docs/experience-architecture/public-home-organizations-collectives-master-document.md`;
- `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0` — `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md`.

### 6.3 Home Pública — Guivos Mall

Fontes específicas:

- `GKR-UX-HOME-MALL-MASTER-001 v1.0.0` — `docs/experience-architecture/public-home-mall-master-document.md`;
- `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0` — `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md`.

### 6.4 Home Pública — Guivos Travel

Fontes específicas:

- `GKR-UX-HOME-TRAVEL-MASTER-001 v1.0.0` — `docs/experience-architecture/public-home-travel-master-document.md`;
- `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0` — `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`.

### 6.5 Home Pública — Guivos Media

Fontes específicas:

- `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.0` — `docs/experience-architecture/public-home-media-master-document.md`;
- `GPA-005 v1.2.0` — `docs/product-architecture/media.md`.

### 6.6 Home Pública — Guivos Ads

Fontes específicas:

- `GKR-UX-HOME-ADS-MASTER-001 v1.0.0` — `docs/experience-architecture/public-home-ads-master-document.md`;
- `GPA-007 v1.3.0` — `docs/product-architecture/ads.md`.

### 6.7 Home Pública — Guivos Business

Fontes específicas:

- `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0` — `docs/experience-architecture/public-home-business-source-lock.md`;
- `GKR-UX-HOME-BUSINESS-MASTER-001 v1.0.0` — `docs/experience-architecture/public-home-business-master-document.md`;
- `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0` — `docs/experience-architecture/public-home-business-conversion-authority-v2.md`;
- `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0` — `docs/experience-architecture/public-home-business-authority-contracts.md`;
- `GPA-004 v1.6.0` — `docs/product-architecture/business.md`.

### 6.8 Home Pública — Guivos Intelligence

Fontes específicas:

- `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0` — `docs/experience-architecture/public-home-intelligence-design-handoff.md`;
- `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0` — `docs/experience-architecture/public-home-intelligence-source-lock.md`;
- `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1` — `docs/experience-architecture/public-home-intelligence-master-document.md`;
- `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0` — `docs/product-architecture/intelligence-product-source-lock.md`;
- `GPA-006 v2.0.0` — `docs/product-architecture/intelligence.md`.

Os antigos GENINPUTs de checkpoints superados não entram como autoridade operacional do v5. A emissão gera um `00-LEIA-PRIMEIRO / SOURCE LOCK OPERACIONAL` novo para cada Home, contendo checkpoint, SHAs, fontes, matriz operacional e prompt preenchido.

---

## 7. Ordem de autoridade dentro do input

O brief deve informar à designer — e o prompt, quando houver IA — que as fontes possuem funções diferentes.

```text
0. LEIA-PRIMEIRO / SOURCE LOCK OPERACIONAL DA EMISSÃO
→ congela checkpoint, lista de fontes, SHAs, objetivo e matriz daquela execução
→ não cria significado novo

1. AUTORIDADES COMUNS
→ Handoff = processo e boundary da fase
→ GENINPUT = método de Source Lock / prompt / classes
→ Readiness = contrato de produção e aceite Figma
→ Operational Flow = compreensão humana → criação livre → IA opcional → revisão humana → entrega final

2. SOURCE LOCK / HANDOFF ESPECÍFICO VIGENTE DA HOME, QUANDO EXISTIR
→ congela decisões próprias daquela Home dentro de sua autoridade

3. DOCUMENTO MESTRE
→ significado, narrativa, função, percepção e invariantes da Home

4. AUTORIDADES COMPLEMENTARES / DE PRODUTO
→ resolvem identidade, fronteiras e contratos especializados aplicáveis

5. FONTE ADICIONAL DECLARADA
→ somente para dúvida concreta registrada

REFERÊNCIA EXTERNA / BENCHMARK / MOODBOARD
→ INSPIRATION_ONLY
→ SEM AUTORIDADE

HISTÓRICO / GENINPUT SUPERADO
→ NÃO ENTRA COMO AUTORIDADE OPERACIONAL
```

O `LEIA-PRIMEIRO` não pode sobrescrever os documentos que lista. Se houver conflito semântico, a execução deve parar e registrar a divergência para decisão humana, observando a precedência vigente das autoridades específicas da Home.

---

## 8. Tipos de informação dentro do brief e do prompt opcional

O template utiliza exatamente a mesma taxonomia de `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001`:

### CANONICAL

Decisão governada que deve ser preservada.

### DESIGN_CREATIVE

Campo deliberadamente aberto à criação da designer.

### CONTENT_CANDIDATE

Copy, tom, label ou formulação editorial proposta e sujeita a aprovação humana.

### DESIGN_HYPOTHESIS

Solução criada para testar uma interpretação de Design sem se tornar decisão da Guivos.

### PROTOTYPE_PLACEHOLDER

Conteúdo provisório usado para testar hierarquia, volume, ritmo ou comportamento.

### REAL_DATA_REQUIRED

Informação factual que exige fonte real antes de poder ser tratada como verdade pública.

### OPEN_QUESTION

Decisão ainda não necessária ou não governada, com destino explícito.

### PROHIBITED_INFERENCE

Conteúdo, regra ou claim que não pode ser criado para preencher a solução.

A ferramenta não deve promover qualquer classe a `CANONICAL` por inferência. Mudança de classe exige evidência ou aprovação humana conforme o caso.

---


### 8.1 Liberdade criativa de Design

Podem ser criados livremente, sem baseline visual pré-imposta pelo GKR: paleta, tipografia, imagens, ilustração, iconografia, composição, grid, respiro, linguagem gráfica, atmosfera, motion, componentes e tom de voz/copy não congelada.

Conteúdo verbal proposto pela designer ou pela IA deve ser rotulado como `CONTENT_CANDIDATE` até aprovação humana. O mesmo vale para qualquer direção visual: geração não equivale a aprovação.

Imagens podem ser selecionadas, produzidas ou geradas criativamente. Quando uma imagem puder ser interpretada como evidência de pessoa, parceiro, case, oferta, destino ou operação real, ela deve ser tratada como conceitual/ilustrativa até haver lastro verificável.

## 9. Brief-base e prompt opcional

O bloco abaixo funciona como **template canônico de brief para a designer** e também como prompt controlado quando houver uso de IA. Ele deve ser preenchido para cada Home; não deve ser usado com campos vazios quando esses campos forem relevantes.

```text
Você está apoiando o trabalho de Design para a Guivos. Este conteúdo serve primeiro como brief para a designer humana e, quando aplicável, como contexto controlado para um sistema de IA.

PAPEL DA DESIGNER / IA
A designer é a executora criativa principal. Se uma IA estiver sendo usada, ela é instrumento opcional de apoio. Nenhum dos dois recebe autoridade para redefinir arquitetura de produto, narrativa, posicionamento, taxonomia, operação ou decisões canônicas da Guivos.

HOME EM TRABALHO
[HOME]

FASE
[FASE]

OBJETIVO DESTA EXECUÇÃO
[OBJETIVO]

CHECKPOINT DO GKR
Repositório: guivos-repositorio/Guivos-Knowledge-Repository
Commit: [SHA]

FONTES AUTORIZADAS E ORDEM DE AUTORIDADE
1. [HANDOFF — ID, versão, path]
2. [DOCUMENTO MESTRE — ID, versão, path]
3. [CONTRATO COMPLEMENTAR — ID, versão, path]
4. [FONTES ADICIONAIS, se existirem]

Considere somente essas fontes como autoridade para esta exploração. Referências visuais externas, quando fornecidas, servem apenas como inspiração e não podem sobrescrever os documentos acima.

MATRIZ OPERACIONAL DE INFORMAÇÃO
CANONICAL
[DECISÕES QUE DEVEM SER PRESERVADAS]

DESIGN_CREATIVE
[O QUE PODE SER CRIADO LIVREMENTE]

CONTENT_CANDIDATE
[COPY / TOM / LABELS SUJEITOS A APROVAÇÃO]

DESIGN_HYPOTHESIS
[HIPÓTESES QUE PODEM SER TESTADAS SEM VIRAR DECISÃO]

PROTOTYPE_PLACEHOLDER
[CONTEÚDO PROVISÓRIO PERMITIDO E COMO DEVE SER MARCADO]

REAL_DATA_REQUIRED
[DADOS / CASES / PREÇOS / PARCEIROS / PROVAS QUE EXIGEM FONTE REAL]

OPEN_QUESTION
[QUESTÕES AINDA ABERTAS E SEU DESTINO]

PROHIBITED_INFERENCE
Não invente ou altere:
[LISTA ESPECÍFICA]

Além disso, não trate ausência de definição como autorização para criar produto, funcionalidade, dado, parceiro, depoimento, métrica, prova, preço, oferta, campanha, disponibilidade, impacto ou promessa factual.

CONTEÚDO E DADOS
[INDICAR O QUE É REAL, PARCIAL, CANDIDATO OU PLACEHOLDER]

Quando precisar de placeholder, deixe claro que é provisório e não o transforme em evidência real.

Se uma questão aberta for necessária para materializar a solução, trate a escolha como HIPÓTESE DE DESIGN identificada. Não a apresente como decisão canônica.

ENTREGÁVEL
[DESCREVER O ARTEFATO ESPERADO: mapa de página, wireframe, alternativa de arquitetura visual, UI, protótipo etc.]

REQUISITOS DE QUALIDADE
- preservar a função narrativa dos movimentos sem obrigação de transformá-los em blocos equivalentes;
- preservar a simplicidade percebida mesmo quando o sistema é complexo;
- manter coerência com a família Guivos sem copiar mecanicamente outra Home;
- considerar desktop e mobile quando fizer parte do objetivo;
- considerar acessibilidade e performance desde a exploração;
- não utilizar padrões de mercado como substitutos das decisões do GKR.

AUTOAUDITORIA OBRIGATÓRIA
Ao concluir a proposta, identifique separadamente:
1. decisões canônicas preservadas;
2. decisões de Design introduzidas;
3. hipóteses utilizadas;
4. placeholders utilizados;
5. lacunas ou conflitos encontrados;
6. qualquer ponto que exija validação humana antes de avançar.

STATUS DO OUTPUT
EXPLORAÇÃO — não canônico e não aprovado para implementação.
```

---

## 10. Regra para ferramentas que não produzem autoauditoria textual

Algumas ferramentas podem materializar diretamente uma interface sem devolver relatório textual suficiente.

Nesses casos, a autoauditoria não desaparece.

Ela deve ser registrada externamente pelo responsável pela execução, contendo pelo menos:

- o que foi preservado;
- o que foi proposto;
- quais hipóteses apareceram;
- quais placeholders foram usados;
- quais lacunas surgiram;
- qual é o estado do output.

A ausência de um relatório automático da ferramenta **não reduz a exigência de rastreabilidade**.

---

## 11. Protocolo de conteúdo real e placeholder

### Conteúdo real

Quando conteúdo real estiver disponível, sua origem e natureza devem ser mantidas.

### Conteúdo parcial

Quando houver apenas parte do conteúdo, a ferramenta pode explorar a composição sem inventar a parte ausente como fato.

### Placeholder

Placeholder pode testar:

- volume de texto;
- hierarquia;
- relação imagem-texto;
- ritmo;
- densidade;
- comportamento responsivo.

Placeholder não pode simular como real:

- parceria;
- case;
- impacto;
- depoimento;
- avaliação;
- preço;
- promoção;
- quantidade de usuários;
- disponibilidade;
- destino operacional;
- produto ainda inexistente;
- campanha vigente;
- autoridade externa.

> **Placeholder testa forma. Não cria verdade.**

---

## 12. Referências visuais e benchmarks

Referências externas podem ser incluídas no Source Lock em campo separado de `authorized_sources`.

Exemplo conceitual:

```yaml
visual_references:
  - name: "<referência>"
    purpose: "<o que se pretende observar>"
    authority: "inspiration_only"
```

A referência deve ter propósito explícito, como:

- ritmo;
- uso de espaço;
- relação tipográfica;
- comportamento de mídia;
- transição entre regiões;
- navegação;
- movimento.

Não usar referência para importar silenciosamente:

- estrutura de produto;
- modelo comercial;
- taxonomia;
- promessa;
- linguagem de conversão;
- componente obrigatório;
- estética integral de outra marca.

> **Referência inspira. Fonte governada decide.**

---

## 13. Como tratar uma lacuna descoberta pela ferramenta

Quando a materialização revelar uma decisão não governada:

```text
LACUNA IDENTIFICADA
↓
registrar a pergunta
↓
continuar com hipótese reversível, se possível
OU
pausar o ponto, se a decisão for estrutural
↓
validação humana
↓
se necessário, nova decisão no GKR
↓
novo Source Lock ou revalidação
```

A ferramenta não deve resolver definitivamente uma lacuna estrutural apenas porque precisa fechar um layout.

---

## 14. Promoção de uma hipótese

Uma hipótese visual ou funcional só pode deixar de ser hipótese por decisão explícita.

```text
OUTPUT GENERATIVO
→ EXPLORAÇÃO

seleção humana
→ CANDIDATO

validação estrutural
→ VALIDADO EM UX

validação visual
→ VALIDADO EM UI

nova decisão quando necessária
→ GKR atualizado

posterior autorização
→ APROVADO PARA HANDOFF DE ENGENHARIA
```

O arquivo do Figma ou a existência de uma tela refinada não altera sozinho o estado arquitetural.

---

## 15. Registro mínimo da unidade de trabalho e do uso opcional de IA

Para cada Home, preservar o registro mínimo da unidade de trabalho. Se houver uso relevante de IA, registrar também esse uso:

```yaml
execution_record:
  execution_id: "<ID>"
  source_lock: "<referência ao Source Lock>"
  tool: "<ferramenta>"
  output_location: "<onde o artefato está registrado>"
  output_status: "EXPLORAÇÃO"
  canonical_decisions_preserved: []
  design_decisions_introduced: []
  hypotheses: []
  placeholders: []
  open_questions: []
  validation_result: "<pending | rejected | candidate | ux_validated | ui_validated>"
```

O GKR não precisa armazenar toda iteração visual, mas deve ser possível reconstruir qual contexto produziu uma direção relevante.

---

## 16. Quando criar um novo Source Lock

Criar novo Source Lock quando houver mudança material em pelo menos um destes elementos:

- Home;
- objetivo;
- fase;
- checkpoint do GKR;
- Documento Mestre;
- contrato complementar;
- decisão canônica relevante;
- conteúdo real que altera substancialmente a composição;
- escopo do entregável.

Pequenas iterações visuais dentro da mesma hipótese podem permanecer sob o mesmo Source Lock, desde que a rastreabilidade não seja perdida.

---

## 17. Critérios de aceite antes de gerar

Uma unidade está pronta para consumo por IA quando a designer optar por esse caminho e:

1. a Home está identificada;
2. a fase está identificada;
3. o objetivo é específico;
4. o checkpoint do GKR está registrado;
5. o pacote obrigatório da Home está identificado;
6. versões e paths estão registrados;
7. invariantes estão explícitos;
8. liberdades de Design estão explícitas;
9. proibições de inferência estão explícitas;
10. conteúdo real e placeholder estão diferenciados;
11. questões abertas estão registradas;
12. o output começa classificado como `EXPLORAÇÃO`.

Se esses itens não puderem ser preenchidos, a IA não deve ser usada como fonte de apoio governado. A designer pode continuar manualmente dentro das autoridades disponíveis, desde que qualquer dúvida semântica material seja escalada em vez de inferida.

---

## 18. Critérios de aceite depois de gerar

Antes de promover um output a `CANDIDATO`, verificar:

1. a pergunta-mãe foi preservada quando aplicável;
2. o papel da Home não mudou;
3. os movimentos continuam semanticamente presentes sem obrigação de equivalência visual;
4. nenhum produto ou capacidade ganhou protagonismo indevido;
5. nenhuma informação fictícia aparenta ser real;
6. nenhuma referência externa passou a governar a Guivos;
7. hipóteses estão identificadas;
8. lacunas estão identificadas;
9. mobile não foi tratado apenas como desktop empilhado quando a solução exige adaptação real;
10. acessibilidade e performance não foram sacrificadas apenas por efeito visual;
11. a Home continua parte da mesma família Guivos sem se tornar cópia de outra Home;
12. o output continua reversível antes da validação.

---

## 19. Aplicação a novas Homes

Este template deve ser adotado por novas Homes depois que seus próprios documentos de autoridade forem convergidos.

A inclusão de uma nova Home não ocorre porque existe um pedido de geração visual.

A ordem permanece:

```text
ARQUITETURA DA HOME CONVERGIDA
↓
FONTES CANÔNICAS IDENTIFICADAS
↓
HANDOFF AUTORIZADO
↓
SOURCE LOCK
↓
BRIEF DE DESIGN
↓
CRIAÇÃO MANUAL DA DESIGNER
↓
IA OPCIONAL / PROMPT CONTROLADO, SE NECESSÁRIO
↓
VALIDAÇÃO
```

---

## 20. Síntese operacional

A menor unidade segura de trabalho não é o prompt isolado nem a ferramenta escolhida.

É:

```text
SOURCE LOCK
+
FONTES
+
PROMPT
+
OUTPUT CLASSIFICADO
+
VALIDAÇÃO
```

O objetivo não é tornar o processo burocrático. É permitir liberdade visual sem perder a arquitetura já construída.

> **A ferramenta pode propor forma. Não pode inventar a Guivos que a forma representa.**

Estado histórico do método:

> **SOURCE LOCK + BRIEF DE DESIGN DEFINIDOS — PROMPT DE IA OPCIONAL — PRONTOS PARA INSTANCIAÇÃO POR HOME — NENHUM OUTPUT VISUAL SE TORNA CANÔNICO SEM VALIDAÇÃO HUMANA.**

### Estado vigente

```text
TEMPLATE
→ ACTIVE / RECONCILED FOR 8 HOMES

V5 PER-HOME SOURCE LOCKS
→ EMITTED / 8 OF 8 / FROZEN IN delivery/design-handoff-v5

GENERATIVE EXECUTION
→ AUTHORIZED TO EXECUTE / NOT_STARTED
→ RELEASE AUTHORITY = GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.0.0
```