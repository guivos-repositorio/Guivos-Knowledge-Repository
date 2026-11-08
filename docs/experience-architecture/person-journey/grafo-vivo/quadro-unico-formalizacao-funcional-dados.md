---
title: Grafo Vivo — Quadro Único de Formalização Funcional e Dados Mínimos
status: conceptual_study
version: 0.2.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: approved_documentary_baseline_deepened_pending_normative_authorization
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

## 9. Eficácia e limites (histórico e estado atualizado)

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
