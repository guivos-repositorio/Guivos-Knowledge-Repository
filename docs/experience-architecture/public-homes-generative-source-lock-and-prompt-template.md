---
id: GKR-UX-HOMES-GENINPUT-001
title: Homes Públicas — Source Lock e Contrato de Consumo por Sistemas de IA
status: active
version: 3.0.0
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-HANDOFF-001
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
related:
  - GKR-UX-HOMES-DESIGN-CONSUMPTION-001
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
maturity: v6_tool_neutral_optional_ai_consumption
---

# Homes Públicas — Source Lock e Contrato de Consumo por Sistemas de IA

## 0. Estado tool-neutral

A Auditoria Integral está concluída. Este documento permanece ativo somente para uso opcional de IA.

```text
DESIGNER
→ MAY WORK WITHOUT AI
AI
→ OPTIONAL SUPPORT
V5 SOURCE LOCKS
→ HISTORICAL / FROZEN
V6 PER-HOME GUIDES
→ TO BE REISSUED AFTER CURRENT REMEDIATION
```

## 1. Finalidade

Este documento define contexto seguro quando a designer ou equipe decide utilizar IA como apoio. Ele não torna IA obrigatória e não cria uma etapa de Design.

## 2. Relação com o handoff canônico

A autoridade entre os dois documentos é:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
→ governa a fase de Design, o pacote de fontes, as liberdades e as fronteiras

GKR-UX-HOMES-GENINPUT-001
→ governa como uma execução generativa é preparada, registrada e validada
```

Este documento não substitui o handoff nem resume os Documentos Mestres.

Ele operacionaliza o princípio:

> **O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração. A validação reconecta forma e significado.**

---

## 3. Unidade opcional de uso de IA

Cada uso relevante de IA pode ser tratado como consulta ou exploração identificável.

```text
FONTES AUTORIZADAS
+
OBJETIVO
+
CLASSES DE INFORMAÇÃO
+
INVARIANTES
+
PROIBIÇÕES
+
PROPOSTA NÃO CANÔNICA
+
VALIDAÇÃO HUMANA, SE UTILIZADA
```

Não existe exigência de registrar cada interação nem de utilizar IA para criar a Home.

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

O prompt deve informar explicitamente à ferramenta que as fontes possuem funções diferentes.

```text
0. LEIA-PRIMEIRO / SOURCE LOCK OPERACIONAL DA EMISSÃO
→ congela checkpoint, lista de fontes, SHAs, objetivo e matriz daquela execução
→ não cria significado novo

1. AUTORIDADES COMUNS
→ Handoff = processo e boundary da fase
→ GENINPUT = método de Source Lock / prompt / classes
→ Readiness = contrato de produção e aceite Figma
→ Operational Flow = sequência sistema de IA de apoio → aprovação → Figma definitivo → aceite

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

## 8. Tipos de informação dentro do prompt

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

## 9. Template opcional para IA

```text
Você está apoiando o trabalho de Design da Guivos.
Apoie a designer sem redefinir produto, narrativa, autoridade, operação ou verdade canônica.

HOME
[HOME]

OBJETIVO
[OBJETIVO]

FONTES AUTORIZADAS
[IDs / VERSÕES / PATHS]

CANONICAL
[VERDADES]

DESIGN_CREATIVE
[CAMPOS LIVRES]

CONTENT_CANDIDATE
[COPY / LABELS]

DESIGN_HYPOTHESIS
[HIPÓTESES]

PROTOTYPE_PLACEHOLDER
[PROVISÓRIOS]

REAL_DATA_REQUIRED
[DADOS REAIS NECESSÁRIOS]

OPEN_QUESTION
[QUESTÕES]

PROHIBITED_INFERENCE
[VEDAÇÕES]

Não invente métricas, preço, parceiro, case, disponibilidade ou funcionalidade.
Não imponha estética, layout ou benchmark.
Não substitua a autoria da designer.
Qualquer proposta é apoio não canônico até decisão humana.
```

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

## 15. Registro opcional de apoio de IA

O registro é opcional. Quando uma proposta de IA influenciar materialmente uma direção apresentada, é útil preservar fontes, objetivo, hipóteses, placeholders e questões abertas.

O GKR não armazena nem governa o arquivo visual produzido pela designer.

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

Uma execução está pronta para ferramenta generativa quando:

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

Se esses itens não puderem ser preenchidos, a execução deve ser tratada como exploração não governada e não pode alimentar decisões oficiais sem reconciliação posterior.

---

## 18. Critérios de uso responsável de uma proposta de IA

Antes de incorporar uma proposta: preservar papel/pergunta-mãe; manter movimentos como significado e não layout; não aparentar dado fictício como real; não elevar referência externa a autoridade; identificar hipóteses e lacunas; preservar acessibilidade/responsividade; tratar a proposta como insumo da designer.

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
PROMPT CONTROLADO
↓
EXPLORAÇÃO GENERATIVA
↓
VALIDAÇÃO
```

---

## 20. Síntese operacional

```text
FONTES
+
OBJETIVO
+
CLASSES
+
PROPOSTA
+
DECISÃO HUMANA, SE UTILIZADA
```

> **IA pode apoiar a forma. Não pode inventar a Guivos que a forma representa.**

```text
AI CONTRACT
→ ACTIVE / OPTIONAL
DESIGNER
→ PRIMARY CREATIVE AUTHOR
V5
→ HISTORICAL / FROZEN
V6 GUIDES
→ PENDING CURRENT REMEDIATION
```
