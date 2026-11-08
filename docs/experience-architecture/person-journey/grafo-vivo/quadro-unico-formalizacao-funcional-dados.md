---
title: Grafo Vivo — Quadro Único de Formalização Funcional e Dados Mínimos
status: conceptual_study
version: 0.6.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: focal_readiness_assessment_conditional_documentary_only
---

# Grafo Vivo — Quadro Único de Formalização Funcional e Dados Mínimos

> **Instrumento único de consolidação para decisão, não contrato normativo.** Reúne decisões expressamente aprovadas, requisitos candidatos, lacunas e próximos atos competentes relativos ao destino funcional do Grafo Vivo e aos dois sentidos da passagem Hoje ↔ Grafo Vivo. Não cria novos identificadores, superfícies, transições, APIs ou política de tratamento de dados, nem autoriza implementação ou publicação.

## 1. Autoridades e evidências de partida

- [Alternativa B](decisao-direcao-alternativa-b.md), [responsabilidade distinta](decisao-direcao-responsabilidade-distinta.md), [entrada/retorno/modalidades](decisao-direcao-entrada-retorno-modalidades.md), [primeiro Hoje](decisao-direcao-primeiro-hoje.md), [CT-01/CT-02](decisao-direcao-ct01-ct02.md), [diretriz R2](decisao-direcao-r2.md) e [adoção das minutas como base](decisao-direcao-minutas-base.md).
- [Duas minutas de transição](minutas-contratos-transicao-entrada-retorno.md) e [contrato funcional candidato de passagem/retorno](contrato-funcional-candidato-passagem-retorno.md).
- Master PER-008 `GKR-UX-PER008-MASTER-001` **v0.1.0**; Orquestração `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001` **v0.4.0**.
- Surface Registry `GKR-JOURNEY-SURFACE-REGISTRY-001` **v0.36.22**; Transition Registry `GKR-JOURNEY-TRANSITION-REGISTRY-001` **v0.29.26**.
- PER-007, PER-010/011/012, PAS-001, GPA-006 v2.0.2, GIA-COG-001, regras de segurança, privacidade, proveniência, [ciclo de vida](matriz-ciclo-vida-informacao-contextual.md), [sincronização](contrato-conceitual-sincronizacao-versionamento.md) e [recuperação](matriz-estados-coerencia-recuperacao-multimodal.md).

**Convenção:** **APROVADO** significa diretriz conceitual expressa da Direção; **CANDIDATO** significa requisito para exame, não contrato vigente; **PENDENTE** indica decisão/autoridade ausente. A redação não reinterpreta aprovações anteriores como autorização operacional.

## 2. Identidade funcional do destino — quadro unificado

| Dimensão | Conteúdo | Estado |
| --- | --- | --- |
| Nome descritivo | Grafo Vivo da Jornada da Pessoa — experiência expandida | **APROVADO conceitualmente**, sem nome oficial de superfície |
| Posicionamento | **Alternativa B:** entrada por PER-008 — Hoje | **APROVADO** |
| Competência | Responsabilidade funcional **distinta**, conforme R2, sem absorver Hoje ou domínios especializados | **APROVADO**, ainda não registrada no Surface Registry |
| Três perspectivas | Explorar, Escutar e Conversar como modalidades internas | **APROVADO**, sem TRN por alternância |
| Apresentação visual | Pode integrar composição existente ou assumir apresentação própria sem confundir identidade funcional com número de telas | **PENDENTE de Design/contrato posterior** |
| Participante e proteção | Pessoa autenticada, acesso contextual voluntário e finalidade permitida | **Diretriz APROVADA; critérios técnicos CANDIDATOS** |
| Primeiro Hoje | Acesso opcional quando há contexto legítimo suficiente; sem histórico anterior obrigatório | **APROVADO** |
| Owner e autoridades | Experiência/Jornada governa contratos UX; Intelligence interpretação; domínios e privacidade conservam suas competências | **Mapeamento CANDIDATO**, sem nova delegação oficial |
| Estado de maturidade | Responsabilidade conceitual reconhecida, ainda sem contrato/validação operativos | **Fato documental; representação formal PENDENTE** |
| Identificador | Nenhum novo PER-ID ou GKR-SURF-ID atribuído | **NÃO AUTORIZADO nesta etapa** |
| Alteração de Registry | Preparar reconciliação da responsabilidade distinta | **CT-01 APROVADO como planejamento; edição PENDENTE** |

**Critério de identidade:** antes de atribuir qualquer ID, a autoridade de Jornada deverá demonstrar por que a responsabilidade não pode ser representada apenas como competência genérica de Hoje e qual é sua unidade registrável. A **R2 já foi escolhida como diretriz**; não reabrir R1/R3 sem nova deliberação.

## 3. Dois handoffs — decisões fixadas versus cláusulas candidatas

| Cláusula | Hoje → Grafo Vivo | Grafo Vivo → Hoje | Estado |
| --- | --- | --- | --- |
| Origem/destino | Hoje → destino distinto a formalizar | Destino distinto → Hoje | **Diretriz APROVADA; identificador PENDENTE** |
| Ato da Pessoa | Abertura explícita e voluntária | Saída explícita, com recuperação segura quando necessária | **APROVADO conceitualmente** |
| Elegibilidade | Contexto suficiente e legitimamente permitido inclusive no primeiro Hoje | Saída não condicionada a concluir conversa/atividade | **Princípio APROVADO; teste de suficiência CANDIDATO** |
| Contexto de passagem | Mínimo autorizado para finalidade e modo, não payload completo | Referência mínima de navegação e reconsulta do estado canônico | **CANDIDATO** |
| Autorização | Nenhuma concessão implícita de retenção, personalização ou voz | Nenhuma persistência ou aceite implícitos | **Fronteira APROVADA; política PENDENTE** |
| Efeito material | Não cria/aceita objetivos, passos, evolução ou consentimento | Retorno neutro; nenhum registro de conclusão/progresso | **APROVADO conceitualmente** |
| Versão e proveniência | Verificar vigência/estado epistemológico antes da apresentação | Reconsultar compreensão canônica e não afirmar atualização sem evidência | **CANDIDATO técnico** |
| Falha e idempotência | Cancelar/repetir sem efeitos duplicados; informar parcialidade | Retorno recuperável sem efeito duplicado nem sucesso inventado | **CANDIDATO técnico** |
| Representação no Transition Registry | Contrato específico próprio, ainda sem TRN | Contrato específico próprio, ainda sem TRN | **CT-02 APROVADO como necessidade; registro PENDENTE** |

**Não reutilizar** `TRN-007` (PER-007 → PER-008) nem `TRN-008..013` (pares Hoje ↔ PER-010/011/012); as validações vigentes não migram para Grafo Vivo por analogia.

## 4. Matriz mínima de dados e permissões — necessidade lógica, sem API ou banco

| Informação/referência | Uso na entrada | Uso no retorno | Gate/risco | Estado |
| --- | --- | --- | --- | --- |
| Autenticação/sessão vigente | Comprovar acesso legítimo à Jornada | Comprovar retorno seguro | Nunca transmitir credenciais como contexto do grafo | **CANDIDATO** |
| Origem e destino funcionais | Vincular abertura à entrada Hoje | Reconstituir rota de volta | Destino ainda sem identidade oficial no Registry | **Conceito aprovado; contrato PENDENTE** |
| Finalidade e categoria permitida | Selecionar contexto aplicável à exploração, escuta e conversa | Restringir eventual reconsulta | Não presumir consentimento por navegação | **CANDIDATO sob Privacidade/PAS** |
| Referência de versão/vigência contextual | Detectar conteúdo alterado e narrativas obsoletas | Consultar estado canônico | Versão só pode ser utilizada se autoridade definir sua origem | **CANDIDATO sob dados/GIA** |
| Proveniência e status epistemológico | Distinguir declaração, hipótese, confirmação e lacuna | Não consolidar hipótese como fato | Registro/apresentação proporcional e contestável | **CANDIDATO sob GIA/PER-007** |
| Escolhas independentes de persistência e personalização | Respeitar negativa ou revogação | Evitar salvamento no retorno | **Sessão ≠ memória ≠ personalização** | **Fronteira APROVADA; mecanismo PENDENTE** |
| Foco atual/seleção de nó | Continuar exploração escolhida | Retorno neutro, quando aplicável | Não vincular nó a ação de domínio | **CANDIDATO opcional** |
| Disponibilidade de áudio e consentimento próprio | Somente ao iniciar efetivamente interação de voz autorizada | Parar saída/processamento conforme política | Provedor de voz, retenção e STT/TTS não autorizados | **PENDENTE** |
| Sinais de correção/revogação | Não reutilizar conteúdo invalidado | Reconsultar e invalidar derivados | Caches, áudios, projeções e múltiplos motores de IA | **CANDIDATO técnico** |
| Contexto transcrito/conversado | Somente para finalidade e janela legítimas | Não exportar transcrição por padrão | Distinguir fala de fato confirmado e hipótese | **PENDENTE de política** |

**Não transportar por padrão:** grafo integral, histórico integral da Pessoa, áudio bruto, transcrições completas, dados sensíveis desnecessários, tokens de autenticação, cópia da memória persistida, objetos de domínio mutáveis ou logs para fornecedores externos.

A arquitetura de integração candidata (GPT/Claude/Gemini, eventualmente Grok para voz, Neo4j como projeção) **não autoriza processamento por qualquer provedor**. Projeção no grafo não se torna fonte de verdade de objetivos, passos ou evolução.

## 5. Estados de decisão e integridade informacional

**Estados lógicos candidatos para cada afirmação:** recebida/declarada; interpretada como hipótese; pendente de esclarecimento; confirmada pela Pessoa quando pertinente; elegível ao uso de sessão; elegível à persistência após escolha própria; revogada ou corrigida. Esses estados **não são enums ou esquema oficial**.

**Invariantes de projeto a submeter posteriormente:**
1. A visualização e a narração devem refletir a mesma compreensão governada e versões compatíveis; divergência deve ser sinalizada, não ocultada.
2. Uma informação surgida durante Conversar não ingressa automaticamente em memória persistente, personalização ou mudança material da Jornada.
3. A Pessoa pode revisar/corrigir; revogação exige reavaliação dos derivados que usam a informação.
4. A navegação do grafo não cria links autorizados entre Objetivos, Próximos Passos e Evolução fora dos contratos vigentes.
5. Falha de áudio não deve derrubar a Jornada; fallback textual, interrupção e saída devem existir quando tecnicamente viáveis e autorizados.
6. Retomada de sessão não é prometida sem política explícita de armazenamento, expiração e consentimento.

## 6. Gaps reais e suas autoridades

| Gate | Questão pendente | Autoridade de referência | Próximo ato necessário |
| --- | --- | --- | --- |
| **F-01** | Como registrar R2 e sua maturidade, sem criar IDs por conveniência? | Surface Registry / Arquitetura da Experiência | Decisão específica de representação formal e eventual identificação |
| **F-02** | Quais cláusulas finais dos dois contratos e como formalizá-los? | Transition Registry / Orquestração | Revisão dos handoffs e autorização normativa expressa |
| **D-01** | O que caracteriza contexto suficiente por modo no primeiro Hoje? | PER-007, PER-008, GIA, Privacidade | Critério documental de elegibilidade e ausência |
| **D-02** | Qual fonte autoritativa emite versão, finalidade e proveniência? | GIA/PAS-001/Dados | Contrato de contexto e versionamento autorizado |
| **D-03** | Qual retenção admissível para sessão, texto, transcrição e áudio? | PER-007, Privacidade, Segurança | Escolhas independentes, prazos e revogação definidos por autoridade |
| **D-04** | Quais projeções podem atingir Neo4j e motores externos? | GIA, Arquitetura de Dados, Privacidade | Minimização e contrato de fornecedor aprovado |
| **X-01** | Como tratar fallback, falhas, acessibilidade, concorrência e idempotência? | UX/Engenharia/Segurança | Critérios de aceite e validação posterior |
| **O-01** | Qual a compatibilidade com a dashboard publicada? | Replit Jornada da Pessoa | Auditoria somente leitura mediante autorização própria |

**Os marcadores F/D/X/O são rótulos locais de trabalho deste quadro; não são novos IDs oficiais.**

## 7. Pacote concentrado para a próxima decisão da Direção

Este quadro reduz as próximas deliberações a **duas matérias centrais**, sem repetir decisões consolidadas:

**A — Representação e maturidade funcional:** ratificar que R2, já escolhida, deverá ser formalizada como responsabilidade distinta no Surface Registry **somente após** definição competente da identidade, do owner e da maturidade documental, sem obrigar nova tela física e sem editar ainda o Registry. O ponto realmente novo para deliberação é **qual nível de formalização se pretende autorizar na etapa seguinte**, não se R2 deve ser reescolhida.

**B — Contratos mínimos de contexto e dados:** avaliar os princípios do envelope lógico (finalidade, proveniência, versão, escolhas de persistência/personalização, uso de sessão mínimo, correção/revogação, não transferência automática de conteúdo e fallback), como **base de aprofundamento técnico**, sem declarar base legal, prazo de retenção, esquema, API, fornecedor ou autorização operacional.

**Recomendação de encaminhamento:** aprovar o **quadro único como baseline documental de instrução** e autorizar, em passo posterior e separado, a elaboração de propostas de reconciliação normativa com alterações explicitamente delimitadas; **não aprovar agora** edição de Registry nem integração real.

## 8. Decisão posterior da Direção — baseline documental A+B (08/11/2026)

A Direção respondeu **“de acordo, segue”** à solicitação de **adotar este quadro único como baseline documental de instrução e autorizar o aprofundamento conjunto das frentes A (identidade/representação funcional) e B (contexto/dados mínimos)**.

**Alcance da aprovação:** este quadro passa a ser a **referência documental central de trabalho** para preparar propostas de formalização, sem promover suas cláusulas candidatas a norma, política de dados, contrato operacional, autorização de alteração de Registry ou implantação. Decisões anteriores preservam sua própria proveniência e hierarquia.

### 8.1 Frente A — proposta consolidada de representação funcional R2

| Campo de eventual registro | Proposta para confronto, não campo validado | Fundamento ou gate |
| --- | --- | --- |
| Unidade registrável | **Responsabilidade funcional de experiência expandida contextual**, distinta da síntese de Hoje | R2 e CT-01 já aprovados como diretriz; forma concreta de registro pendente |
| Descrição de finalidade | Ajudar a Pessoa a compreender relações e possibilidades por Explorar, Escutar e Conversar, sem ações materiais de domínio | Não absorver PER-010/011/012 nem interpretação soberana da GIA |
| Sujeito e proteção | Pessoa em contexto de Jornada autenticada, com finalidade, autorização e informação elegíveis | Compatibilizar com PER-007, PER-008 e Privacidade |
| Origem contextual | PER-008 — Hoje, inclusive primeira entrada legitimamente elegível | Alternativa B e decisão sobre Primeiro Hoje |
| Destino do retorno | PER-008 — Hoje, com reconsulta do estado canônico | Entrada/retorno aprovados conceitualmente |
| Competência decisória | Direção da Guivos decide formalização do Grafo Vivo neste escopo | Owner de manutenção e instância de validação técnica **a ratificar**, sem presumir delegação |
| Domínios relacionados | PER-010/011/012 permanecem autoridades de seus objetos | Relações gráficas não instituem links ou operações automáticas |
| Estado candidato inicial | **Em definição / não validado** até ato expresso e evidências próprias | Nunca copiar status “validado” da superfície Hoje |
| Tipo de superfície visual | **Não adjudicado**; identidade funcional não implica necessariamente tela independente | Design e arquitetura visual dependem de autorização posterior |
| Identificador | **A atribuir somente por ato próprio, se necessário** | Não reservar nem inventar número PER/Surface |
| Dependências | Master PER-008, Orquestração, Registries, PER-007, GIA, PAS-001 e contratos de dados | Confrontar antes de qualquer edição normativa |

**Condições de aceitação para minuta normativa de Surface Registry:** (a) identificar unidade de responsabilidade sem duplicar Hoje; (b) owner competente confirmado; (c) estado/maturidade não operacional fundamentado; (d) origem/destino rastreáveis; (e) critérios de proteção/ausência; (f) nenhum novo ID por simples pressuposto; (g) diff apresentado separadamente à Direção.

### 8.2 Frente B — contrato mínimo de contexto, aprofundado

| Momento | Conjunto lógico mínimo candidato | Proibição ou exceção |
| --- | --- | --- |
| **Antes da entrada** | Comprovação de sessão legítima; finalidade do aprofundamento; escopo do contexto permitido; sinal de suficiência | Não abrir áudio, memória ou transmissão externa por simples navegação |
| **Na entrada** | Referência da origem Hoje, foco opcional, referência à compreensão/versão elegível e proveniência quando a autoridade as fornecer | Não enviar histórico integral, credenciais, grafo integral ou transcrição inteira |
| **Ao Explorar** | Nós/relações derivados de contexto permitido, status de declaração/hipótese/confirmado e período de validade | Não converter conexão em fato canônico, objetivo, passo, evolução ou ação de domínio |
| **Ao Escutar** | Conteúdo narrável compatível com versão e finalidade, com alternativa textual e comando de parada | Não fazer áudio sob demanda virar consentimento de gravação ou retenção; fornecedor pendente |
| **Ao Conversar** | Foco/versão autorizados, texto recebido e novos dados tratados inicialmente conforme status epistemológico | Não persistir toda fala como fato nem compartilhar com motor externo não autorizado |
| **Ao mudar de modalidade** | Foco atual e referência temporal/versão minimizados, se legítimos | Não criar nova autorização nem nova fonte de verdade a cada alternância |
| **Ao corrigir/revogar** | Sinal de invalidade/revisão da fonte e derivados cuja manutenção seja permitida | Não reutilizar cache, grafo, narrativa ou contexto desautorizado |
| **No retorno a Hoje** | Referência mínima de navegação + **reconsulta ao estado canônico** e permissões | Não carregar conteúdo efêmero de sessão ou declarar persistência por padrão |
| **Em falha** | Estado de erro identificável e alternativa segura conforme capacidade efetiva | Não afirmar sucesso, retomada, gravação inexistente ou consistência não verificada |

**Suficiência por modalidade (critério candidato e qualitativo):**
- **Explorar:** existe ao menos uma relação/tema ou evidência contextual legítima que suporte representação compreensível; na ausência, explicar limites sem fabricar nós.
- **Escutar:** existe conteúdo textual contextual elegível para narração, com versão adequada; falta de voz não pode ocultar a alternativa textual.
- **Conversar:** existe contexto de finalidade legítima e possibilidade de diálogo sem extrapolar memória ou personalização; informação nova será tratada como declaração até revisão pertinente.
- Um limiar numérico de clareza **não é criado** nem exigido por esta análise.

**Escolhas independentes:**
1. **Uso de sessão** só no escopo necessário e autorizado.
2. **Persistência** exige escolha apropriada e regras de retenção/revogação ainda a formalizar.
3. **Personalização** exige decisão independente da persistência conforme PER-007.
4. **Gravação/transcrição/voz e fornecedor externo** exigem avaliação de dados, transferência e autorização por modalidade; não são efeitos da entrada.
5. **Dados sensíveis e derivados** exigem minimização, finalidade e tratamento autorizados conforme privacidade e segurança.

### 8.3 Compatibilidade de A+B nos dois handoffs

| Verificação comum | Entrada Hoje → Grafo Vivo | Retorno Grafo Vivo → Hoje |
| --- | --- | --- |
| Fonte de verdade | Consultar a compreensão governada para contexto elegível | Reconsultar estado canônico autorizado |
| Responsabilidade | Troca conceitual para destino R2 formalizável | Volta à responsabilidade Hoje sem efeitos materiais |
| Conteúdo | Minimizado conforme finalidade e versão | Não persistir nem transportar narrativa/transcrição por padrão |
| Falhas | Sem abertura afirmada se a passagem não puder ocorrer de modo legítimo | Saída segura quando viável; não confirmar estado não reconsultado |
| Idempotência | Ação repetida não cria autorização nem registro duplicado | Retorno repetido não conclui ou altera objetos |
| Revogação | Não carregar informação desautorizada | Não reapresentar derivado cujo uso tenha sido revogado |
| Autoridade a formalizar | Surface Registry + contrato próprio no Transition Registry | Contrato próprio de retorno + Orquestração compatível |

### 8.4 Portas de aprovação remanescentes

**Próximo pacote documental a preparar:** um **diff candidato explicitamente delimitado**, não aplicado, com proposta de representação no Surface Registry e localização dos dois contratos no Transition Registry. Deixar campos de identificação dependentes de decisão competente; não modificar arquivo normativo até nova autorização expressa.

**Gates de dados prévios a uma adoção normativa ou operacional:** origem/semântica de versão, categoria de contexto/finalidade, regra de suficiência, tratamento de revogação, eventual retenção, segurança, acessibilidade e fornecedores precisam de validação própria. Um contrato de transição não concede permissão de tratamento de dados.

**Ato reservado à Direção:** decidir se autoriza produzir apenas diffs normativos candidatos para revisão, depois decidir separadamente se alguma alteração será efetivamente aplicada. O uso deste baseline não autoriza publicação, merge, design, API, teste, acesso ao Replit ou implantação.

---

## 9. Propostas de diff normativo **NÃO APLICADAS** — autorização documental da Direção (08/11/2026)

A Direção autorizou expressamente, nesta conversa, **preparar as duas propostas de alteração normativa exclusivamente para revisão, sem modificar os Registries vigentes**. Estes trechos foram elaborados **neste quadro único**, evitando outro documento fragmentado. **São modelos de edição futura, não patches executáveis prontos para aplicação.** O diff ilustrativo utiliza marcadores entre colchetes para indicar campos cuja autoridade e identificação ainda não foram decididas. **Nenhum marcador entre colchetes representa ID oficial nem deve ser copiado literalmente para um Registry.**

### 9.1 Diff candidato A — Surface Registry v0.36.22

**Arquivo-alvo (somente referência):** `docs/journeys/surface-registry.md`. **Seção:** `## 4. Inventário principal`. **Âncora exata verificada:** linha `GKR-SURF-PER-008 | Tela Hoje`. A tabela possui nove colunas: ID, Superfície/estado/responsabilidade, Perspectiva e família, Canal, Maturidade, Autoridade, Materialização, Validação e Detalhamento obrigatório.

**Proposta de adição, não aplicada:**

```diff
 # Contexto: manter intacta a linha vigente de GKR-SURF-PER-008 — Tela Hoje.
+| [ID DO DESTINO A DEFINIR POR ATO PRÓPRIO] | Grafo Vivo — experiência expandida contextual (responsabilidade distinta) | Pessoa autenticada; Explorar/Escutar/Conversar | protegido | candidato documental; NÃO validado | [OWNER/CONTRATO FUNCIONAL A RATIFICAR]; decisões da Direção B/R2/CT-01 | sem baseline visual corrente; não implementado | sem transições validadas; entrada e retorno dependem de contratos futuros | [DETALHAMENTO PESSOA A RECONCILIAR] |
```

**Observações para eventual diff efetivo:** (i) não modificar contagem estrutural de **61 IDs** sem ato formal que atribua efetivamente um novo ID; (ii) não copiar a maturidade “validado” de Hoje; (iii) não interpretar “responsabilidade distinta” como imposição de tela visual adicional; (iv) ratificar owner, referência de contrato, detalhamento e proteção antes de qualquer inclusão; (v) revisar simultaneamente arquivos auxiliares referidos pela coluna de detalhamento, somente se houver autorização expressa. **Não foi inserida linha no Registry.**

### 9.2 Diff candidato B — Transition Registry v0.29.26

**Arquivo-alvo (somente referência):** `docs/journeys/transition-registry.md`. **Seção:** `## 4. Jornada pessoal`. **Âncora exata verificada:** `GKR-TRN-007 | PER-007 | PER-008` e linhas vigentes de `GKR-TRN-008..013`. A tabela possui cinco colunas: ID, Origem, Destino, Estado e Evidência/lacuna principal.

**Proposta de adição, não aplicada:**

```diff
 # Contexto: manter intactos TRN-007 e TRN-008..013, inclusive suas maturidades.
+| [ID DA TRANSIÇÃO DE ENTRADA A DEFINIR] | PER-008 | [DESTINO GRAFO VIVO A DEFINIR] | contrato candidato; NÃO validado | Primeiro Hoje ou recorrente, contexto legitimamente elegível; ação voluntária; finalidade/versão/proveniência mínimas; sem consentimento ou efeito material implícitos; falha, revogação e idempotência pendentes de validação |
+| [ID DA TRANSIÇÃO DE RETORNO A DEFINIR] | [ORIGEM GRAFO VIVO A DEFINIR] | PER-008 | contrato candidato; NÃO validado | Saída explícita e neutra; reconsulta ao estado canônico; interrupção de áudio; nenhuma gravação, persistência ou conclusão automática; recuperação e idempotência pendentes de validação |
```

**Observações para eventual diff efetivo:** (i) os dois contratos são de **sentidos opostos**, não reversão automática de um só; (ii) não reutilizar `TRN-007..013`; (iii) resolver o identificador do destino pelo processo competente antes de formalizar origem/destino; (iv) não alterar a contagem atual de **76 transições** antes da adjudicação da inclusão; (v) coerência, proteção e maturidade devem ser verificadas com Master PER-008, Orquestração, PER-007, Privacidade, PAS-001/GIA; (vi) nenhum status de validação técnica foi concedido.

### 9.3 Registro de impacto e não alteração

| Alvo | Situação após este trabalho |
| --- | --- |
| `surface-registry.md` | **Inalterado** — diff candidato apenas transcrito acima |
| `transition-registry.md` | **Inalterado** — diff candidato apenas transcrito acima |
| Master PER-008 / Orquestração | **Inalterados** |
| IDs, totais e maturidades oficiais | **Inalterados**; placeholders não são IDs |
| Dados, persistência, voz e fornecedores | **Sem autorização operacional**, contratos por autoridade ainda pendentes |
| Este quadro único | Atualizado para **v0.3.0** com propostas para revisão |
| PR #730 | Continua **draft**, sem merge/publicação |

### 9.4 Gate de decisão posterior

As propostas serão aptas para **revisão de possível alteração normativa**, não para aplicação automática, quando a Direção examinar: **(a)** representação e identificação do destino e owner; **(b)** identidade e maturidade dos dois handoffs; **(c)** critérios de contexto/versão/permissão/retorno; **(d)** diferenças colaterais de contagens, detalhamento de Pessoa e orquestração. Qualquer alteração de Registry exigirá **autorização expressa separada** da Direção e a substituição fundamentada dos placeholders. A edição efetiva não está autorizada.

---

## 10. Decisão posterior da Direção — diffs como referência documental (08/11/2026)

A Direção respondeu expressamente **“de acordo, segue”** à recomendação de **aprovar os dois diffs candidatos como referência para futura formalização**, mantendo a atribuição de identificadores e a edição efetiva dos Registries condicionadas a autorizações posteriores.

**Escopo exato do ato:**
- O **diff candidato A — Surface Registry** é adotado como referência de revisão para representar a responsabilidade funcional distinta R2, sem atribuição de ID, owner final ou maturidade validada.
- O **diff candidato B — Transition Registry** é adotado como referência de revisão para os **dois contratos próprios** Hoje → Grafo Vivo e Grafo Vivo → Hoje, sem criação de TRNs ou validação de cláusulas operacionais.
- As propostas continuam **não aplicadas** e não são autoridade normativa. Os placeholders deverão ser resolvidos por ato específico antes de qualquer edição.
- Nenhuma mudança nos totais, versões, IDs, estados ou maturidades vigentes dos Registries decorre desta aprovação.

### Portas decisórias subsequentes

1. **Identidade e competência:** decidir formalmente a representação, o owner e a maturidade documental do destino, com fundamento na autoridade da Jornada e sem impor uma tela visual por inferência.
2. **Contratos de transição:** confrontar as cláusulas propostas com a identidade formal do destino e os contratos de dados, privacidade e versão; submeter duas minutas de alteração efetiva, separadamente.
3. **Autorização normativa:** exigir ato expresso da Direção antes de modificar Surface Registry, Transition Registry, Master PER-008, Orquestração ou seus documentos dependentes.
4. **Autorização operacional:** auditoria Replit, Design, APIs, integração de provedores, testes e implantação permanecem fora deste ato.
5. **Publicação GKR:** PR #730 continua rascunho e não deve ser mesclado/publicado sem autorização e reconciliação editorial.

O efeito desta decisão é **estabilizar o material de referência**, evitando reabrir a escolha conceitual da Alternativa B, R2 ou a necessidade dos dois handoffs, e **não elevar os diffs a contratos vigentes**.

---

## 11. Instrução integrada de identificação, maturidade e dados — autorização da Direção (08/11/2026)

A Direção respondeu **“de acordo, segue”** à recomendação de **resolver documentalmente as pendências de identificação e maturidade da responsabilidade do Grafo Vivo e requisitos de contexto/dados**, sem atribuir novos IDs ou aplicar alterações normativas. Este aprofundamento permanece dentro do **quadro único**, não abre acervo paralelo e **não é uma adjudicação de identificadores**.

### 11.1 Identidade — proposta decisória focal

| Questão | Critério de avaliação | Resultado desta instrução |
| --- | --- | --- |
| Existe competência própria? | Já demonstrada por B, R2, CT-01 | **Sim, aprovada conceitualmente pela Direção** |
| O Grafo Vivo é só estado de Hoje? | Contrastar com Master PER-008 e decisão de responsabilidade distinta | **Não**; não voltar à hipótese R1 sem nova decisão |
| É necessariamente uma tela visual separada? | Competência funcional ≠ materialização visual | **Não definido e não pressuposto** |
| Pode reutilizar PER-008 como identificação do destino? | PER-008 identifica Hoje, não o destino distinto | **Não recomendado**; criaria ambiguidade de autoridade |
| Identificação oficial nova pode ser dada agora? | Regime e autoridade de numeração, impacto no detalhamento e contagem ainda não adjudicados | **Não**; atribuir somente após autorização específica |
| Qual a maturidade a sugerir? | R2 reconhecida documentalmente, sem contrato vigente, testes ou validação | **Candidata/não validada**; nomenclatura exata conforme convenções do Registry a aprovar |
| Qual fonte auxiliar é necessária? | `surface-registry-person-details.md` v0.23.8 detalha contextos, precondições, retornos e autoridade por superfície | **Reconciliar esse detalhamento** na futura proposta normativa; não basta linha no inventário |
| Quem mantém contrato e conteúdo? | Competências de Jornada/UX, Intelligence, dados, privacidade, segurança | **Responsáveis por domínio devem ser explicitados**; nenhuma delegação nova por inferência |

**Recomendação para decisão posterior:** autorizar, por ato específico, a **formalização de uma entrada de responsabilidade funcional candidata e ainda não validada**, com identificação oficial **a decidir pelo processo competente**, sem exigir tela visual própria. Nesta etapa, o nome “Grafo Vivo — experiência expandida contextual” continua **designação descritiva**, não título normativo fixado.

### 11.2 Representação e maturidade — efeitos documentais condicionados

Se uma futura entrada for aprovada, deverão ser coordenados, com diff próprio e autorização expressa:

1. `surface-registry.md`: identificação formal, responsabilidade, canal, maturidade, autoridades e referências;
2. `surface-registry-person-details.md`: estado, job, entrada/retorno, permissão, dados, ações, falhas e contrato de superfície da Pessoa;
3. `transition-registry.md`: **duas** passagens direcionais, identificadas conforme o destino oficial, sem tocar `TRN-007..013`;
4. Master PER-008 e Orquestração: **somente o ajuste mínimo efetivamente exigido**, depois de exame de competência e sem absorver o Grafo Vivo;
5. contagens, rastreabilidade e versão: atualizar **somente se e quando** identificadores e contratos forem formalmente incluídos.

**Estado dos documentos nesta etapa:** todos os itens acima continuam sem edição. O Surface Registry segue v0.36.22, com 61 IDs estruturais; o Transition Registry segue v0.29.26, com 76 transições.

### 11.3 Dados — critérios de elegibilidade por finalidade (propostas, não política)

| Dimensão | Critério candidato verificável | Não se deve inferir |
| --- | --- | --- |
| Sessão | Existe acesso legítimo da Pessoa ao contexto da Jornada | Autorização para compartilhar com provedor externo |
| Finalidade | A informação é necessária à modalidade e ao tema escolhido | Uso ilimitado para treinamento, retenção ou publicidade |
| Origem/proveniência | A fonte e seu caráter declarado, inferido ou confirmado são distinguíveis | Que inferência seja fato validado |
| Atualidade | Referência canônica ou indicador de vigência suficiente para explicar o estado | Que versão hipotética seja contrato de versionamento |
| Suficiência Explorar | Existe ao menos relação/tema sustentado, ou mensagem de ausência legítima | Criação de nós artificiais para preencher a tela |
| Suficiência Escutar | Existe conteúdo textual contextual lícito e narrável | Que qualquer serviço de áudio esteja autorizado |
| Suficiência Conversar | Há finalidade legítima para diálogo e esclarecimento contextual | Que toda fala se torne memória persistida |
| Primeiro Hoje | Informações permitidas e pertinentes estão disponíveis mesmo sem histórico | Histórico, progresso ou evolução presumidos |
| Retorno | Estado canônico de Hoje reconsultável conforme permissão | Salvamento automático da conversa ou da exploração |
| Correção/revogação | Há mecanismo a definir para invalidar derivados quando necessário | Direito de reutilizar caches, narrativas e projeções após revogação |

**Sem decisão técnica nesta etapa:** fonte de verdade das versões, categorias de dados efetivamente admitidas, base jurídica, consentimentos por finalidade, prazos de retenção, critérios de dados sensíveis e eventuais envios a GPT/Claude/Gemini/Grok/Neo4j. Esses pontos exigem contratos próprios com autoridades de dados, Intelligence, Privacidade e Segurança.

### 11.4 Envelope lógico mínimo para revisão de contrato — sem payload/API

**Na entrada, candidato:** referência de origem Hoje; sessão autorizada sem credenciais; finalidade; categorias de contexto elegível; referência de versão quando existente; proveniência/status epistemológico necessário; estado das escolhas independentes de persistência/personalização; foco opcional. **Não** transferir áudio bruto, histórico integral ou transcrição completa por padrão.

**Durante a experiência, candidato:** contexto minimizado e versão compatível para Explorar/Escutar/Conversar; qualquer nova declaração permanece distinguível de hipótese, revisão, confirmação e persistência; alternância de modos não autoriza efeitos de domínio.

**No retorno, candidato:** referência mínima da rota de volta, finalização da apresentação não autorizada e reconsulta do estado canônico de Hoje; nenhuma marcação automática de progresso, objetivo, passo, consentimento, gravação ou memória.

### 11.5 Matriz decisória consolidada para a próxima autorização

As aprovações B, R2, CT-01/02, minutas e diffs **já estão encerradas no nível conceitual/documental**. Não reapresentá-las à Direção como escolhas abertas.

**Decisão nova 1 — nível de formalização:** autorizar ou não, em ato distinto, **redigir uma proposta completa de alteração coordenada** de Surface Registry e detalhamento da Pessoa, ainda **sem aplicá-la e sem atribuir IDs**, usando maturidade “candidata/não validada” sujeita a compatibilidade editorial. Se houver pretensão de aplicação, identificar formalmente o destino primeiro.

**Decisão nova 2 — contrato de dados:** autorizar ou não a produção de critérios de elegibilidade e transferência de contexto como **contrato documental candidato de dados**, sujeito a fontes de verdade e política de privacidade antes de qualquer implementação. Isso **não** aprova envio a fornecedores nem retenção.

**Dependência material:** sem destino formalmente identificado e sem governança de dados adequada, os dois contratos de transição não devem ser promovidos a “validados”. Somente após essas decisões cabe um pedido específico de alterações normativas; somente depois um pedido operacional de inspeção Replit.

---

## 12. Autorização e preparação conjunta A+B — formalização coordenada e contrato candidato de dados (08/11/2026)

A Direção aprovou, nesta conversa, **preparar a proposta coordenada e o contrato candidato de contexto e dados no mesmo quadro único**, sem editar documentos normativos, atribuir identificadores, autorizar processamento externo ou implantar. Os dois blocos seguintes são **instrumentos de revisão**, não cláusulas contratuais vigentes.

### 12.1 Frente A — proposta coordenada de alterações **não aplicadas**

**Dependências documentais verificadas:**
- `docs/journeys/surface-registry.md` **v0.36.22**: inventário de nove campos e total estrutural de 61 IDs;
- `docs/journeys/surface-registry-person-details.md` **v0.23.8**: detalhamento obrigatório de treze campos, vinculado ao mesmo identificador da superfície; não é outro inventário;
- `docs/journeys/transition-registry.md` **v0.29.26**: cinco campos por transição, total de 76 transições; `TRN-007..013` preservadas;
- Master PER-008 v0.1.0 e Orquestração v0.4.0: competências, variantes de Hoje e continuidade sem absorção.

**Proposta alinhada em três linhas editoriais futuras, sem criar IDs:**

1. **Inventário de superfície (9 colunas)** — adicionar, **somente após decisão de identificação**, uma responsabilidade protegida e própria: “Grafo Vivo — experiência expandida contextual”, Pessoa autenticada, maturidade **contrato funcional candidato / não validado**, autoridade e owner a ratificar, sem baseline visual corrente e sem handoffs validados. Diferenciar expressamente de `GKR-SURF-PER-008`.
2. **Detalhamento obrigatório da Pessoa (13 colunas)** — registrar o **mesmo identificador futuro**, se autorizado, nos campos ID, autoridade corrente, estado/versão, entrada, decisão principal, saída, dados e conteúdos, gate, reversibilidade, supersessão, continuidade, lacuna e escopo. A redação abaixo indica como preencher cada campo sem criar identificadores.
3. **Transition Registry (5 colunas)** — acrescentar futuramente **dois contratos distintos**, entrada voluntária `PER-008 → [DESTINO A FORMALIZAR]` e retorno neutro `[DESTINO] → PER-008`, com identificadores próprios a adjudicar, sem reaproveitar TRN atual.

**Proposta de conteúdo dos treze campos para o detalhamento da Pessoa, não aplicada:**

| Campo do detalhamento | Texto candidato / restrição |
| --- | --- |
| ID | **[MESMO ID FUTURO APROVADO NO SURFACE REGISTRY]**, placeholder, não identificador oficial |
| Autoridade corrente | [AUTORIDADE/OWNER A RATIFICAR] + decisões B/R2/CT-01/02 + quadro único candidato; não reivindicar Master oficial inexistente |
| Estado/versão | Contrato funcional candidato, não validado; versão oficial somente após ato próprio |
| Entrada | Hoje/PER-008, primeiro ou recorrente, quando houver contexto legitimamente elegível e escolha explícita |
| Decisão principal | Compreender e explorar contexto, relações, lacunas e possibilidades através de Explorar/Escutar/Conversar; sem efeito material |
| Saída | Retorno expresso e neutro a Hoje; contrato próprio a formalizar; não pressupor TRN existente |
| Dados e conteúdos | Contexto mínimo por finalidade e modo, versão, proveniência, estado epistemológico, escolhas de sessão/persistência/personalização |
| Gate | Pessoa autenticada; contexto apropriado; permissões pertinentes; sem autorização implícita de fornecedor/voz/persistência |
| Reversibilidade | Retornar, interromper, corrigir, revogar quando aplicável; sem gravação/salvamento automático |
| Supersessão | Não substitui PER-008, PER-007, PER-010/011/012, PAS-001 ou GIA |
| Continuidade | Entrada/retorno apenas candidatos; nenhuma validação transferida de TRN-007..013 |
| Lacuna | ID, owner, classificação de maturidade exata, contrato de dados, versão, privacidade, acessibilidade, fornecedores, implementação |
| Observação de escopo | Responsabilidade funcional distinta R2, com três modalidades internas; não implica tela visual autônoma |

**Cruzamentos obrigatórios na revisão:** registro do destino e respectivo detalhamento devem usar **a mesma unidade identificadora futura**, a maturidade não pode exceder evidências reais, e os dois contratos de transição exigem destino oficialmente definido. Se a aplicação demandar alterações no Master PER-008 ou Orquestração, instruir **deltas mínimos separados** e submetê-los à Direção; não alterar fontes por consequência automática.

### 12.2 Frente B — contrato documental candidato de contexto e dados

**Objeto lógico:** limitar o que pode ser usado, derivado, apresentado e mantido durante a entrada a partir de Hoje, a alternância entre modalidades e o retorno. **Sem API, esquema de banco, base legal, prazo de retenção, provedor autorizado ou implementação.**

| Cláusula candidata | Requisito para exame | Gate que ainda depende da autoridade |
| --- | --- | --- |
| **B01 — Fonte de verdade** | Identificar a fonte canônica do estado atual; grafo e voz são projeções, não autoridades de domínio | GIA/PAS-001 e arquitetura de dados devem confirmar referências e responsabilidades |
| **B02 — Finalidade e minimização** | Usar apenas contexto relevante à finalidade e modo selecionados | Privacidade deve avaliar categorias, especialmente sensíveis, e fundamento admissível |
| **B03 — Suficiência** | Entrada elegível depende de contexto pertinente e permitido, não de histórico completo ou score fixo | PER-007/PER-008/GIA devem definir testes qualitativos verificáveis |
| **B04 — Versão e temporalidade** | Informar referência de compreensão ou vigência quando houver; invalidar derivado desatualizado | Modelo de versionamento e fonte autorizada ainda não decididos |
| **B05 — Proveniência e epistemologia** | Distinguir declaração, inferência, lacuna, correção e confirmação da Pessoa | Autoridades cognitivas devem definir atualização/contestação da interpretação |
| **B06 — Uso de sessão** | Permitir somente processamento transitório legítimo necessário ao serviço | Política de sessão, expiração e descarte pendentes; negar memória não equivale automaticamente a negar uso de sessão |
| **B07 — Persistência** | Nenhum salvamento de conversa, áudio ou relações por simples entrada/retorno | Decisão separada da Pessoa e política de retenção a formalizar |
| **B08 — Personalização** | Exige escolha própria, independentemente de persistência | PER-007/Privacidade; não inferir opt-in por interação |
| **B09 — Voz e transcrição** | Escutar e Conversar exigem autorização e fallback textual proporcionais | STT/TTS, retenção/gravação, Grok ou outros fornecedores são candidatos, não aprovados |
| **B10 — Terceiros e grafo** | Nenhuma transmissão automática do contexto inteiro a motores ou Neo4j | Contratos de minimização, transferência e segregação aguardam autoridade de dados/segurança |
| **B11 — Revogação e correção** | Reavaliar derivados, sessão, cache, texto e narração vinculados a dado corrigido ou revogado | Regras de invalidação, proveniência e eventual eliminação/propagação a definir |
| **B12 — Retorno e continuidade** | Reconsultar Hoje, evitar efeitos materiais, falha honesta e operação idempotente | UX/Segurança/Engenharia devem validar recuperação e ausência de ações duplicadas |

**Critérios candidatos de admissibilidade por modalidade, sem tornar histórico obrigatório:**

- **Explorar:** permitir quando houver tema, aspecto ou conexão sustentada por contexto disponível; a ausência de relações suficientes pode ser comunicada honestamente, sem forjar um grafo.
- **Escutar:** permitir narração de uma compreensão textual efetivamente elegível, com referência temporal e alternativa textual; falta de provedor de voz não equivale à falta de compreensão.
- **Conversar:** permitir esclarecimento contextual dentro da finalidade, distinguindo nova declaração de fato confirmado; a Pessoa deve poder corrigir e escolher separadamente se algo será guardado ou personalizado.
- **Alternância:** preservar contexto mínimo autorizado e compatibilidade de versão, sem criar permissões, histórico ou contratos TRN extras.

**Exemplos de aceitação documental futura:**

| Situação | Resultado esperado, ainda candidato |
| --- | --- |
| Primeiro Hoje sem histórico prévio | Acesso opcional quando há contexto útil; não exibir progresso ou trajetória inventados |
| Pessoa recusa personalização | Manter apenas funções que tenham base legítima independente; não personalizar |
| Pessoa corrige informação durante áudio | Parar/sinalizar conteúdo possivelmente desatualizado antes de afirmar nova versão |
| Permissão é revogada | Não reutilizar dado desautorizado e tratar seus derivados conforme política competente |
| Contexto insuficiente para explorar | Explicação de ausência e continuidade segura, em vez de nós fictícios |
| Falha de provedor de voz | Texto equivalente quando viável; saída disponível e nenhuma gravação presumida |
| Retorno repetido | Não criar objetivo, passo, evolução, consentimento, evento material ou gravação duplicados |
| Retorno com reconsulta indisponível | Não afirmar síntese atualizada sem confirmação; disponibilizar recuperação apropriada |

### 12.3 Questões remanescentes e critério para próxima decisão

A Direção **já autorizou a preparação conjunta A+B**, não a aplicação dos conteúdos. As questões que efetivamente exigem nova autorização são:

1. **Forma oficial de identificação e owner** do destino R2, compatível com as regras atuais de alocação de IDs e sem reserva por inferência.
2. **Maturidade exata** a registrar na futura entrada de Surface Registry e detalhamento Pessoa, sem alegar validação.
3. **Aprovação por autoridade competente dos contratos de dados**, especialmente fonte de versão, categorias, critérios de suficiência, privacidade, retenção, revogação e fornecedores.
4. **Aceite específico do pacote coordenado de mudanças normativas**, com diff final rastreável e autorização expressa de edição.
5. **Gate operacional separado** para auditoria Replit, seguido de Design, APIs, implementação e testes conforme autorização posterior.

**Próxima recomendação:** submeter à Direção um parecer focal com a proposta mais restrita de identificação/maturidade e dependências de dados, decidindo expressamente se existe base suficiente para autorizar a formalização normativa ou se ainda é necessária reconciliação especializada. Não repetir a aprovação conceitual de B, R2, CT-01/02 ou das minutas.

---

## 13. Parecer focal de prontidão para formalização normativa — instrução documental (08/11/2026)

> **Parecer analítico condicionado, não aprovação normativa.** A Direção autorizou elaborar o exame de prontidão sobre **(1) identidade/maturidade funcional** e **(2) suficiência dos contratos de contexto e dados**. Esta análise é preparada pelo trabalho documental do GKR; **não se apresenta como parecer independente de especialista, decisão da autoridade de privacidade ou validação operacional**. A decisão de editar Registries continua reservada a ato expresso posterior.

### 13.1 Quesito 1 — identidade e maturidade estão suficientemente fundamentadas?

**Resposta:** **suficientes para preparar uma minuta formal completa de representação R2, mas insuficientes para inserir de imediato uma nova entrada oficial no Surface Registry.**

| Elemento | Evidência e conclusão |
| --- | --- |
| Competência | **Suficiente conceitualmente:** Alternativa B, responsabilidade distinta e R2 foram aprovadas expressamente |
| Limite com Hoje | **Suficiente conceitualmente:** PER-008 permanece síntese e origem/retorno, não destino funcional absorvente |
| Tipo de representação | **Suficiente como diretriz:** reconhecer responsabilidade funcional; tela física/visual independente não foi decidida |
| Identificação oficial | **Insuficiente:** não foi definido o ato competente de atribuição, nem o identificador da unidade registrável |
| Owner e autoridade de manutenção | **Insuficiente:** responsáveis podem ser mapeados, mas não delegados por inferência |
| Maturidade | **Suficiente para vedar status “validado”; insuficiente para escolher automaticamente o rótulo normativo final** |
| Detalhamento obrigatório | **Lacuna delimitada:** inclusão deverá ser reconciliada com `surface-registry-person-details.md` v0.23.8, em seus 13 campos |
| Impacto de contagem | **Não autorizável agora:** 61 IDs no Surface Registry v0.36.22, sem incremento nesta etapa |

**Parecer:** manter R2 **candidata e não validada** em documentos de instrução. Para promoção a entrada no Registry, exigir identificação formal, owner, maturidade exata e diff coordenado do detalhamento da Pessoa. Não simular novo ID nem escolher número a partir de sequência aparente.

### 13.2 Quesito 2 — o contrato de contexto e dados está apto a sustentar contratos formais?

**Resposta:** **o conjunto B01–B12 é suficiente como checklist de revisão e especificação candidata, mas insuficiente para declarar contratos de dados aprovados ou transições formalmente validadas.**

| Lacuna crítica | Estado | Efeito sobre a formalização |
| --- | --- | --- |
| Fonte canônica de versão e proveniência | **Aberta** | Não é possível garantir detecção/propagação consistente de revisões e narrativas obsoletas |
| Suficiência objetiva por modalidade | **Parcial** | Critérios qualitativos propostos, não aceitos formalmente pelas autoridades de PER-007/PER-008/GIA |
| Categorias e finalidades permitidas | **Aberta** | Não há decisão de minimização e tratamento por categoria sensível |
| Sessão, expiração e descarte | **Aberta** | Não há contrato de ciclo de vida efêmero; negar persistência não elimina automaticamente usos legítimos da sessão |
| Persistência e personalização | **Princípio de separação aprovado; mecanismos abertos** | Não se pode presumir consentimento, retenção ou reaproveitamento posterior |
| Voz, transcrição, armazenamento e fornecedores | **Aberta** | Não há autorização para processar dados por Grok ou outros provedores por esta via |
| Neo4j, grafo derivado e caches | **Aberta** | Não há política de projeção, invalidação, retenção ou reversão de derivados |
| Interrupção, falha, idempotência e acessibilidade | **Especificação candidata** | Não são casos validados em software, nem critérios finais aceitos de UX/segurança |
| Retorno neutro e proteção dos domínios | **Diretriz conceitual aprovada** | Não permite atribuir a novos TRNs a maturidade das transições existentes |

**Parecer:** o contrato candidato permite **preparação controlada de propostas normativas**, mas **não** sustenta aprovação de tratamento de dados ou implantação. O escopo dos próximos contratos deve ser limitado a referências e condições lógicas; qualquer execução que exija dados reais, provedores ou retenção depende de deliberação competente.

### 13.3 Parecer geral e gradação de prontidão

| Objeto | Prontidão documental | Pode avançar agora? |
| --- | --- | --- |
| Alternativa B, R2, três modos, acesso primeiro Hoje | Diretriz conceitual aprovada | Sim, como premissa de documentos candidatos, sem nova votação |
| Minuta coordenada de Surface Registry + detalhamento Pessoa | Parcial; campos e estrutura conhecidos | **Sim, para redação e revisão sem aplicação** |
| Identificador e owner oficiais do destino | Não resolvidos | **Não**, sem decisão específica |
| Inclusão efetiva no Surface Registry | Bloqueada por identificação, autoridade e maturidade final | **Não** |
| Duas minutas de transição | Base documental aprovada; destino ainda não identificado | **Sim, para revisão não aplicada** |
| Inclusão e validação no Transition Registry | Bloqueada por destino, dados e gates | **Não** |
| Contrato de dados B01–B12 | Candidato com lacunas relevantes | **Sim, para análise de suficiência com autoridades; não como política vigente** |
| Inspeção Replit/Design/implantação | Sem ato operacional | **Não** |

**Conclusão focal:** **prontidão parcial, exclusivamente documental**. Não há fundamento para elevar qualquer uma das três entradas propostas a estado validado nem para formalizar imediatamente os Registries. Os pontos faltantes são específicos e não justificam reabrir B, R2, CT-01/02 ou a aprovação das minutas.

### 13.4 Próxima decisão realmente necessária

**Recomendação de deliberação focal — opção P1:** a Direção poderá **autorizar apenas a preparação de um dossiê de competência e identificação oficial**, com critérios e alternativas fundamentadas de alocação de unidade registrável e owner, preservando os números não atribuídos, e **encaminhar B01–B12 para reconciliação documental especializada de dados/privacidade**. Isso não cria IDs, não modifica fontes normativas e não declara parecer de especialista que não ocorreu.

**Alternativa P2 — aplicação normativa imediata:** **não recomendada**, porque identificação/owner, versão canônica e critérios de dados permanecem abertos. Sua adoção exigiria novo ato expresso da Direção com fundamentação e resolução das dependências, não pode ser inferida desta análise.

**Próximo gate operacional:** somente após regras normativas e de dados suficientes, e mediante autorização independente, examinar a implementação na dashboard da Jornada da Pessoa no Replit.

---

## 14. Eficácia e limites (histórico e estado atualizado)

| Objeto | Situação |
| --- | --- |
| Alternativa B, R2, competência distinta, entrada, retorno, três modos, primeiro Hoje | **Aprovados conceitualmente pela Direção** |
| Duas minutas de handoff | **Aprovadas como base documental** |
| Este quadro único de formalização e dados mínimos | **Aprovado pela Direção como baseline documental de instrução**; não é política de dados, contrato normativo nem autorização de execução |
| Surface/Transition Registries, Master PER-008 e Orquestração | **Não alterados** |
| Novos PER/TRN/Surface IDs e políticas oficiais de dados | **Não criados** |
| Auditoria, Design, API, testes, implantação ou publicação no Replit | **Não autorizados** |
| PR #730 / GKR | **Rascunho, sem merge/publicação** |

A aprovação de uma diretriz conceitual **não** implica sua validação operacional. As autoridades vigentes continuam fonte de verdade até eventual ato formal de atualização.
