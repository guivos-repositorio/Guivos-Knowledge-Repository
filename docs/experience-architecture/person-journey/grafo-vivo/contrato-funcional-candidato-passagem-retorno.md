---
title: Grafo Vivo — Contrato Funcional Candidato de Passagem e Retorno Hoje ↔ Experiência Expandida
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: functional_handoff_candidate_pending_adjudication
---

# Grafo Vivo — Contrato Funcional Candidato de Passagem e Retorno Hoje ↔ Experiência Expandida

> **Contrato funcional candidato, não vigente.** A Direção aprovou a Alternativa B, o destino com responsabilidade funcional distinta, a entrada voluntária, o retorno neutro, a alternância interna Explorar/Escutar/Conversar e a elegibilidade opcional no primeiro Hoje com contexto legítimo suficiente. **Este documento detalha as condições de passagem e retorno para exame, sem criar PER-ID, TRN-ID, superfície, API, política de dados, autorização de Design, teste ou implantação.**

## 1. Autoridades e decisões de partida

| Fonte | Alcance preservado |
| --- | --- |
| [Alternativa B — decisão da Direção](decisao-direcao-alternativa-b.md) | PER-008 — Hoje como entrada contextual para experiência expandida |
| [Responsabilidade distinta — decisão](decisao-direcao-responsabilidade-distinta.md) | Grafo Vivo expandido possui função distinta da síntese de Hoje e dos domínios especializados |
| [Entrada, retorno e modos — decisão](decisao-direcao-entrada-retorno-modalidades.md) | Entrada/saída explícitas; retorno neutro; três modalidades internas |
| [Elegibilidade no primeiro Hoje — decisão](decisao-direcao-primeiro-hoje.md) | Primeiro acesso elegível sem histórico prévio obrigatório, sem convite universal |
| `GKR-UX-PER008-MASTER-001` v0.1.0 | Hoje é síntese, distingue primeira entrada e estado recorrente, não fabrica histórico/progresso |
| `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001` v0.4.0 | Continuidade e contexto mínimo, sem absorver autoridades de Master, Registries ou Planos |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` v0.36.22 | Responsabilidades já reconhecidas; Grafo Vivo ainda sem registro oficial |
| `GKR-JOURNEY-TRANSITION-REGISTRY-001` v0.29.26 | TRN-007 e TRN-008..013 conservam seus pares e maturidade, sem novos handoffs presumidos |
| PER-007, PER-010/011/012, PAS-001, GPA-006, GIA-COG-001, Privacidade | Revisão, escolhas de dados, fronteiras de domínio e compreensão governada |

**Nota de competência:** GKR/GitHub registra instruções e decisões expressas da Direção nesta conversa. A redação deste candidato não constitui adjudicação automática das cláusulas abaixo.

## 2. Contrato lógico candidato — sem números de transição

```text
PER-007 → [TRN-007 vigente] → PER-008 — Hoje
                                   │
                           ação explícita elegível
                                   ▼
                     Grafo Vivo — responsabilidade distinta
                      ┌───────────┼───────────┐
                  Explorar      Escutar     Conversar
                      └───────────┼───────────┘
                             sair/retornar
                                   ▼
                          PER-008 — Hoje
                      (reconsulta autorizada)
```

A passagem **Hoje ↔ Grafo Vivo** acima é uma **fronteira funcional a formalizar**, não uma transição existente no Registry. Explorar/Escutar/Conversar são modos internos aprovados conceitualmente; não recebem TRNs próprios por padrão.

## 3. Matriz de pré-condições e elegibilidade

| Condição | Entrada | Efeito na experiência |
| --- | --- | --- |
| Pessoa legitimamente em PER-008 — Hoje | Necessária | Nenhum desvio da revisão PER-007/TRN-007 |
| Ação voluntária de abertura | Necessária | Acesso não inicia gravação, memória ou personalização |
| Contexto apropriado à finalidade | Necessário | Sem dados legítimos, explicar ausência e não fabricar nós |
| Suficiência proporcional ao modo | A verificar | Permitir aprofundamento limitado quando apropriado; não prometer totalidade |
| Permissões vigentes para uso contextual | Necessárias para cada categoria de dado | Não inferir aceite de finalidade extra |
| Primeira entrada sem histórico | **Não impede por si só** | Mostrar presente, lacunas e possibilidades sustentadas |
| Hoje recorrente | Elegível quando aplicável | Reconsultar estado canônico para evitar visão desatualizada |
| Persistência/personalização recusadas | Não equivalem a acesso proibido por padrão | Oferecer somente uso de sessão admissível, se a autoridade autorizar; sem retenção implícita |
| Fonte de conteúdo revogada | Não elegível para aquela finalidade | Não reutilizar projeção ou áudio derivado |

**Ainda falta adjudicar** quais conjuntos de dados/categorias são indispensáveis para cada modalidade, o método de comprovar a suficiência e o tratamento de escolha negativa para retenção. Não criar limiar numérico ou score de clareza como requisito oficial por inferência.

## 4. Envelope de passagem candidato — dados mínimos, sem esquema oficial

| Campo lógico | Para que serviria | Limite de autoridade |
| --- | --- | --- |
| Referência da sessão autorizada | Associar abertura à Pessoa legitimamente autenticada | Não é token de autenticação, ID persistente novo ou autorização ampliada |
| Origem funcional = Hoje | Permitir retorno correto | Não reutiliza TRN-008..013 |
| Versão/revisão da compreensão contextual | Informar conteúdo vigente e detectar desatualização | A versão deve existir ou ser definida pela autoridade de dados |
| Categorias de contexto disponíveis | Determinar modalidades elegíveis | Sem transferência de dados sensíveis desnecessários |
| Estado das escolhas de persistência e personalização | Impedir retenção ou uso incompatível | Escolhas permanecem independentes e revisáveis |
| Referência de proveniência/temporalidade | Separar declarado, confirmado, hipótese e desatualizado | Não transforma declaração em fato |
| Foco opcional do aprofundamento | Continuar relação ou tema escolhido conscientemente | Não cria objeto nem navegação especializada |
| Política aplicável de retenção de sessão | Limitar uso transitório | **Não definida neste documento**; exigir ato específico |

O envelope é **lista de necessidades lógicas a validar**, não payload de API, modelo Neo4j, base legal definida ou aprovação de transferência a GPT/Claude/Gemini/Grok.

## 5. Processo candidato de entrada

1. Pessoa acessa Hoje por continuidade legítima; a síntese permanece primeira responsabilidade.
2. Quando existir contexto adequado, Hoje pode exibir acesso opcional ao Grafo Vivo (inclusive na primeira entrada).
3. Pessoa aciona o acesso explicitamente.
4. Antes de apresentar qualquer informação, verificar finalidade, escopo permitido e versão contextual atual.
5. Resolver apenas a projeção elegível; se ausente ou parcial, mostrar lacunas e modos realmente disponíveis.
6. Abrir o destino expandido sem iniciar por padrão gravação, transcrição, reprodução de áudio, persistência ou ação material.
7. Manter controle visível de retorno e alternativas acessíveis.

**Condições de não entrada:** autorização insuficiente para conteúdo requisitado, perda de sessão legítima, versão inválida sem recuperação segura ou falha que impeça apresentar qualquer contexto permitido. A experiência não deve simular sucesso.

## 6. Processo candidato de retorno

1. Pessoa aciona retorno explícito ou ocorre condição de recuperação que exige voltar à Jornada.
2. Interromper saídas em andamento cuja continuidade não seja autorizada (ex.: narração ativa).
3. Descartar ou manter estado efêmero **somente** segundo futura regra de sessão/consentimento.
4. Reconsultar a referência canônica vigente de Hoje, considerando atualização, correção, revogação e permissões.
5. Exibir síntese atual compatível com o Master PER-008.
6. Não criar, confirmar ou modificar objetivos, passos, evolução, oportunidades, consentimento ou cobrança no retorno.

**Ponto a decidir:** possibilidade de sair mesmo durante erro/indisponibilidade da modalidade. Recomendação para adjudicação: sempre fornecer saída segura quando a sessão legítima existir.

## 7. Estados de passagem candidatos e recuperação

| Estado ou evento | Resposta funcional proposta | Efeito indevido a evitar |
| --- | --- | --- |
| Convite elegível | Entrada contextual, sem pressão | Tornar o grafo requisito para continuar |
| Contexto parcial | Comunicar limitações e modalidade possível | Exibir progresso fictício |
| Abertura em processamento | Estado neutro, cancelável | Marcar abertura como conclusão |
| Entrada concluída | Mostrar versão elegível e controles | Considerar entrada como permissão de gravação |
| Atualização concorrente do contexto | Detectar divergência e reconsultar, com aviso proporcional | Substituir interpretação silenciosamente |
| Falha só de áudio | Oferecer explicação textual | Declarar toda a Jornada indisponível |
| Falha só de grafo | Disponibilizar perspectiva textual elegível | Forjar nós ou conexões |
| Interrupção de voz pela conversa | Parar reprodução e manter foco permitido | Persistir áudio por padrão |
| Revogação de permissão | Invalidar uso futuro de derivados e revisar estado | Continuar narrando dado desautorizado |
| Duplo clique/retry de entrada | Uma navegação lógica sem efeitos materiais duplicados | Criar sessão/registro material duplicado |
| Retorno em rede instável | Recuperar saída quando possível, não afirmar estado atualizado sem confirmação | Declarar retorno concluído antes de estado real |

**Maturidade:** são comportamentos candidatos e cenários de exame, não uma máquina de estados oficial, SLA ou validação operacional.

## 8. Idempotência, concorrência e contexto versionado

- Repetir entrada/saída não cria consentimento, duplicação de objetos ou eventos materiais por padrão.
- Uma eventual “versão da compreensão” deve ser governada pela fonte responsável; não reutilizar conteúdo de versão ultrapassada como atual.
- Se a Pessoa corrigir contexto durante narração, indicar desatualização antes de nova interpretação.
- Se houver novas declarações na conversa, distinguir informação usada temporariamente, hipótese e confirmação consciente antes de eventual persistência.
- A mudança de modo **não deve** renovar permissões nem reiniciar o ciclo cognitivo como outra verdade.
- Retomada entre sessões não é garantida sem decisão específica de persistência/retenção.

## 9. Fronteiras de domínio e navegação

| Objeto | O que a experiência pode propor | O que permanece fora da competência do Grafo Vivo |
| --- | --- | --- |
| Hoje | Explicar contexto e abrir/retornar ao aprofundamento | Alterar finalidade de síntese, fabricar atenção ou progresso |
| Objetivos — PER-010 | Exibir relação contextual e explicar proveniência | Criar/aceitar/priorizar/editar objetivo |
| Próximos Passos — PER-011 | Explicar possibilidade e vínculo com contexto | Assumir/iniciar/concluir passo |
| Evolução — PER-012 | Apresentar evidência ou hipótese com rótulo epistemológico adequado | Reconhecer progresso, baseline ou trajetória por visualização |
| Intelligence | Produzir compreensão governada, expor incerteza e lacunas | Transferir autoridade cognitiva ao provedor de voz ou à projeção do grafo |

**Sem atalhos criados:** TRN-008..013 regulam pares específicos envolvendo Hoje recorrente; uma ligação semântica entre Objetivo e Passo não cria navegação direta PER-010↔PER-011.

## 10. Matriz de adjudicação remanescente para a Direção

| Ponto | Questão a decidir posteriormente | Consequência |
| --- | --- | --- |
| CT-01 | Como representar responsabilidade distinta no Surface Registry, com qual maturidade e sem criar ID por conveniência? | Reconciliação de competência |
| CT-02 | A passagem Hoje → Grafo e o retorno serão contratos formais de transição em Registry? | Identificação de origem/destino, contrato, revisão e eventual numeração, **somente após ato expresso** |
| CT-03 | O que define elegibilidade suficiente do primeiro Hoje para cada modo? | Teste documental de dados/finalidade e estados de ausência |
| CT-04 | Qual conjunto mínimo de referências de versão e estado de autorização será consumido? | Contrato de dados e privacidade |
| CT-05 | Qual comportamento de saída/interrupção/cancelamento tem precedência em falha parcial? | UX, segurança e acessibilidade |
| CT-06 | Quando, se houver opt-in separado, a sessão poderá ser recuperada depois? | Política de persistência e retenção |
| CT-07 | Quem produz e valida a narração multimodal, e sob quais contratos de fornecedores? | GIA/Privacidade/Engenharia e processamento externo |

CT-xx são **marcadores locais para esta matriz**, não IDs oficiais do GKR ou do sistema.

## 11. Limites de eficácia e próximos gates

**Já aprovado pela Direção:** Alternativa B, responsabilidade funcional distinta, entrada voluntária, retorno neutro, alternância interna das modalidades, acesso opcional no primeiro Hoje com contexto elegível.

**Ainda candidato:** envelope de passagem, estados, dados mínimos, critérios operacionais, política de sessão, tratamento de falha, mecanismos de versão e eventual necessidade de novas transições registradas.

**Não autorizado:** mudança de PER-008/Orquestração/Surface Registry/Transition Registry; novo PER/TRN-ID; definição de API, tecnologia, política de retenção, design visual; inspeção/testes/implementação do workspace Replit; merge ou publicação.

**Encaminhamento recomendado:** submeter à Direção, nesta conversa, deliberação focal sobre **CT-01 e CT-02** (representação da responsabilidade distinta e necessidade de contratos formais de passagem/retorno). Após decisão, examinar critérios e dados com as autoridades especializadas antes de qualquer alteração normativa ou desenvolvimento.
