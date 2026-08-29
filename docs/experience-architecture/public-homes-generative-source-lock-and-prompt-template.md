---
id: GKR-UX-HOMES-GENINPUT-001
title: Homes Públicas — Source Lock e Prompt Controlado para Ferramentas Generativas
status: active
version: 1.1.0
owner: Experience Architecture
last_updated: 2026-08-29
parent: GKR-UX-HOMES-DESIGN-HANDOFF-001
depends_on:
  - GKR-STATE-001
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
related:
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GPA-005
normative: true
maturity: generative_template_preserved_instantiation_suspended_during_full_corpus_audit
---

# Homes Públicas — Source Lock e Prompt Controlado para Ferramentas Generativas

## 0. Gate vigente durante a Auditoria Integral do GKR

Este documento continua normativo como **template e contrato de integridade** para uma futura execução generativa governada.

Ele não constitui autorização para criar ou executar um Source Lock enquanto a Auditoria Integral estiver aberta.

```text
TEMPLATE
→ PRESERVADO

MÉTODO DE SOURCE LOCK
→ PRESERVADO

NOVA INSTANCIAÇÃO OPERACIONAL
→ SUSPENSA DURANTE A AUDITORIA

PROMPT / FIGMA MAKE / WIREFRAME / UX / UI / PROTÓTIPO
→ NÃO AUTORIZADOS COMO NOVA EXECUÇÃO
```

A regra atual é:

> **TEMPLATE DE EXECUÇÃO ≠ AUTORIZAÇÃO PARA EXECUTAR.**

Source Locks e snapshots históricos permanecem evidência dos checkpoints em que foram emitidos. Uma futura instância exige fechamento dos gates aplicáveis, ato humano explícito de reativação e checkpoint pós-auditoria reconciliado.

As seções abaixo preservam integralmente o método que deverá ser retomado quando houver autorização própria.

---

## 1. Finalidade

Este documento transforma o controle semântico estabelecido por `GKR-UX-HOMES-DESIGN-HANDOFF-001` em um procedimento operacional reutilizável para exploração de Design com ferramentas generativas.

Ele define:

- como congelar as fontes de uma execução;
- quais metadados precisam acompanhar o input;
- como compor um prompt sem transferir autoridade arquitetural para a ferramenta;
- como distinguir decisão canônica, liberdade de Design, hipótese e lacuna;
- como registrar a saída para posterior validação humana;
- como impedir que outputs exploratórios se tornem decisões do GKR por inércia.

Este documento não cria wireframes, layouts, componentes, UI final ou identidade visual para nenhuma Home.

> **Ferramentas generativas recebem um contexto governado. Elas não recebem autoridade para completar a arquitetura da Guivos por conta própria.**

---

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

## 3. Unidade de execução governada

Cada uso relevante de Figma Make ou ferramenta generativa deve ser tratado como uma **execução identificável**.

Uma execução possui:

```text
SOURCE LOCK
+
FONTES AUTORIZADAS
+
OBJETIVO
+
PROMPT CONTROLADO
+
OUTPUT EXPLORATÓRIO
+
REGISTRO DE HIPÓTESES
+
VALIDAÇÃO HUMANA
```

Não existe uma execução governada quando apenas se envia uma instrução genérica como:

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

  design_freedoms:
    - "<aspecto que pode ser explorado>"

  forbidden_inferences:
    - "<decisão que a ferramenta não pode inventar>"

  content_state:
    real_content_available: "<yes | partial | no>"
    placeholders_allowed: true
    placeholder_rules: "<regras específicas>"

  open_questions:
    - "<lacuna ainda não governada>"

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

## 6. Pacotes autorizados das cinco Homes

A execução deve utilizar somente o pacote correspondente à Home em trabalho, salvo exceção registrada no Source Lock.

### 6.1 Home Pública — Pessoa

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-MASTER-001
+
GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001
```

Paths:

- `docs/experience-architecture/public-homes-design-handoff.md`;
- `docs/experience-architecture/public-home-master-document.md`;
- `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`.

### 6.2 Home Pública — Organizações e Coletivos

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-OC-MASTER-001
+
GKR-UX-HOME-OC-MEDIA-SUPPLY-001
```

Paths:

- `docs/experience-architecture/public-homes-design-handoff.md`;
- `docs/experience-architecture/public-home-organizations-collectives-master-document.md`;
- `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md`.

### 6.3 Home Pública — Guivos Mall

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-MALL-MASTER-001
+
GKR-UX-HOME-MALL-MEDIA-SUPPLY-001
```

Paths:

- `docs/experience-architecture/public-homes-design-handoff.md`;
- `docs/experience-architecture/public-home-mall-master-document.md`;
- `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md`.

### 6.4 Home Pública — Guivos Travel

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-TRAVEL-MASTER-001
+
GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001
```

Paths:

- `docs/experience-architecture/public-homes-design-handoff.md`;
- `docs/experience-architecture/public-home-travel-master-document.md`;
- `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`.

### 6.5 Home Pública — Guivos Media

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-MEDIA-MASTER-001
+
GPA-005
```

Paths:

- `docs/experience-architecture/public-homes-design-handoff.md`;
- `docs/experience-architecture/public-home-media-master-document.md`;
- `docs/product-architecture/media.md`.

---

## 7. Ordem de autoridade dentro do input

O prompt deve informar explicitamente à ferramenta que as fontes possuem funções diferentes.

```text
1. HANDOFF CANÔNICO
→ processo, uso de IA, limites da fase de Design

2. DOCUMENTO MESTRE
→ significado, identidade, narrativa, função e invariantes da Home

3. CONTRATO COMPLEMENTAR
→ relação especializada posterior ou arquitetura do produto aplicável

4. FONTES ADICIONAIS AUTORIZADAS
→ apenas para a dúvida registrada

5. REFERÊNCIAS EXTERNAS
→ inspiração sem autoridade
```

Benchmark, moodboard ou referência visual nunca sobe na hierarquia por ser visualmente convincente.

---

## 8. Tipos de informação dentro do prompt

Cada item relevante deve ser tratável como uma destas classes:

### CANÔNICO

Decisão governada por fonte autorizada.

### LIBERDADE DE DESIGN

Campo deliberadamente aberto para materialização.

### HIPÓTESE

Proposta criada para testar uma solução. Não é decisão da Guivos.

### LACUNA

Informação que as fontes não respondem e que exige decisão humana ou novo contrato.

### PLACEHOLDER

Conteúdo provisório usado para testar hierarquia ou composição sem afirmar realidade.

A ferramenta não deve converter automaticamente `HIPÓTESE`, `LACUNA` ou `PLACEHOLDER` em `CANÔNICO`.

---

## 9. Prompt-base controlado

O bloco abaixo é o **template canônico de montagem do prompt**. Ele deve ser preenchido para cada execução; não deve ser usado com campos vazios quando esses campos forem relevantes.

```text
Você está apoiando uma exploração de Design para a Guivos.

PAPEL DA FERRAMENTA
Você é instrumento de exploração e materialização. Você não possui autoridade para redefinir arquitetura de produto, narrativa, posicionamento, taxonomia, operação ou decisões canônicas da Guivos.

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

INVARIANTES QUE DEVEM SER PRESERVADOS
[LISTA DE INVARIANTES EXTRAÍDOS DAS FONTES]

LIBERDADES DE DESIGN NESTA EXECUÇÃO
[LISTA DO QUE PODE SER EXPLORADO]

PROIBIÇÕES DE INFERÊNCIA
Não invente ou altere:
[LISTA ESPECÍFICA]

Além disso, não trate ausência de definição como autorização para criar produto, funcionalidade, dado, parceiro, depoimento, métrica, prova, preço, oferta, campanha, disponibilidade, impacto ou promessa factual.

CONTEÚDO E DADOS
[INDICAR O QUE É REAL, O QUE É PARCIAL E O QUE É PLACEHOLDER]

Quando precisar de placeholder, deixe claro que é provisório e não o transforme em evidência real.

QUESTÕES ABERTAS
[LISTA]

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

## 15. Registro mínimo da execução

Após uma execução relevante, preservar:

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

Uma execução está pronta para ferramenta generativa quando:

1. a Home está identificada;
2. a fase está identificada;
3. o objetivo é específico;
4. o checkpoint do GKR está registrado;
5. as três fontes obrigatórias estão identificadas;
6. versões e paths estão registrados;
7. invariantes estão explícitos;
8. liberdades de Design estão explícitas;
9. proibições de inferência estão explícitas;
10. conteúdo real e placeholder estão diferenciados;
11. questões abertas estão registradas;
12. o output começa classificado como `EXPLORAÇÃO`.

Se esses itens não puderem ser preenchidos, a execução deve ser tratada como exploração não governada e não pode alimentar decisões oficiais sem reconciliação posterior.

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
PROMPT CONTROLADO
↓
EXPLORAÇÃO GENERATIVA
↓
VALIDAÇÃO
```

---

## 20. Síntese operacional

A menor unidade segura de trabalho não é o prompt isolado.

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

> **SOURCE LOCK E PROMPT CONTROLADO DEFINIDOS — PRONTOS PARA INSTANCIAÇÃO POR HOME — NENHUM OUTPUT VISUAL É CANÔNICO POR GERAÇÃO AUTOMÁTICA.**

### Estado vigente

```text
TEMPLATE
→ PRONTO E PRESERVADO

INSTANCIAÇÃO POR HOME
→ SUSPENSA DURANTE A AUDITORIA INTEGRAL

NOVA EXECUÇÃO GENERATIVA DE DESIGN
→ NÃO AUTORIZADA
```
