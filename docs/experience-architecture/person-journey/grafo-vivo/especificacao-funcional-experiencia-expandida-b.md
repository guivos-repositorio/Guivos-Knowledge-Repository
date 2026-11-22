---
title: Grafo Vivo — Especificação Funcional Candidata da Experiência Expandida (Alternativa B)
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: functional_specification_candidate_pending_adjudication
---

# Grafo Vivo — Especificação Funcional Candidata da Experiência Expandida (Alternativa B)

> **Alternativa B aprovada pela Direção como posicionamento funcional conceitual:** PER-008 — Hoje é ponto de entrada voluntário para experiência expandida. **Este documento é especificação candidata, não contrato vigente**. Não cria superfície, PER-ID, TRN-ID, contrato de API, política de dados, entitlement, layout obrigatório ou autorização de implementação.

## 1. Objetivo e fontes preservadas

Definir o comportamento mínimo examinável de **entrar, explorar, escutar, conversar, alternar e retornar** a partir do Grafo Vivo sem absorver a responsabilidade dos objetos especializados.

Fontes confrontadas:
- [Decisão expressa pela Alternativa B](decisao-direcao-alternativa-b.md) e [Decisão de competência AF-10](decisao-direcao-competencia-af10.md);
- Master `GKR-UX-PER008-MASTER-001` v0.1.0: §§1–6, 11–14, 15–22;
- Orquestração `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001` v0.4.0: §§1, 5, 13, 23–27;
- Surface Registry `GKR-JOURNEY-SURFACE-REGISTRY-001` v0.36.22;
- Transition Registry `GKR-JOURNEY-TRANSITION-REGISTRY-001` v0.29.26;
- PER-007, PER-010, PER-011, PER-012, PAS-001, GPA-006, GIA-COG-001 e políticas aplicáveis;
- [Experiência nos Quatro Momentos](experiencia-quatro-momentos.md), [Sincronização e Versionamento](contrato-conceitual-sincronizacao-versionamento.md) e [Coerência e Recuperação Multimodal](matriz-estados-coerencia-recuperacao-multimodal.md).

A escolha da Alternativa B **não outorga competência de domínio à interface** nem decide se o destino expandido será um estado sob responsabilidade existente ou uma nova responsabilidade contratada.

## 2. Topologia funcional candidata

```text
PER-007 — Compreensão Inicial Revisável
   └─ TRN-007 (já validada) → PER-008 — Hoje
                                      │
                                      │ entrada contextual, voluntária
                                      ▼
                            [Grafo Vivo expandido]
                             │       │       │
                          Explorar  Escutar  Conversar
                             └───────┴───────┘
                                      │
                         retorno neutro a Hoje
                                      ▼
                              PER-008 — Hoje
```

**Os conectores entre Hoje e o destino expandido são apenas relações conceituais a contratar.** Não representam TRN vigente, permissão de navegação ou alteração no Registry.

**Manter os contratos existentes:** do Hoje recorrente, `TRN-008/009` com PER-010, `TRN-010/011` com PER-011, `TRN-012/013` com PER-012, somente quando aplicáveis. Não inferir atalhos diretos PER-010↔PER-011↔PER-012.

## 3. Entrada: o que a Pessoa encontra em Hoje

**Proposta mínima a decidir:**

1. O Hoje conserva a **síntese contextual** e não exibe grafo como desempenho, pontuação humana, catálogo ou feed obrigatório.
2. Havendo contexto elegível à finalidade, oferece um acesso discreto a **“Explorar minha Jornada”** (rótulo ilustrativo, não CTA oficial) com explicação breve do caráter contextual.
3. A Pessoa escolhe entrar ou permanecer em Hoje; não há início automático de gravação, áudio, conversa, persistência ou personalização.
4. Primeira entrada pode legitimamente não conter histórico e **não precisa expor** todos os affordances do Hoje recorrente.
5. Contexto parcial, ausência de relações sustentadas ou revogação de autorização devem resultar em estado honesto de indisponibilidade/parcialidade, não em nós ou progresso fabricados.
6. A existência da entrada visual não resolve a decisão sobre **competência do destino** ou cria transição normativa.

**A ser adjudicado:** elegibilidade do acesso em primeiro Hoje versus Hoje recorrente; nome definitivo do acesso; nível de síntese compartilhável; contrato de entrada/retorno.

## 4. Chegada à experiência expandida

Ao entrar voluntariamente, a proposta é apresentar:

- **Contexto atual legível**, com indicação do que está confirmado, incompleto, hipotético ou pendente de revisão, quando permitido;
- **três modalidades equivalentes de aprofundamento**, sem imposição de uso e sem sugerir que uma seja necessária;
- **referência temporal e de versão** da compreensão usada na exploração, se essa informação existir legitimamente;
- **comandos explícitos de retornar, revisar contexto e interromper**; ações materiais devem seguir suas autoridades próprias;
- **ausência legítima** como resultado possível (nada de linha do tempo ou evolução fictícia).

**Questão aberta:** quem é a autoridade funcional do destino e se essa chegada será estado sob competência já registrada ou responsabilidade separada.

## 5. Modalidades candidatas

| Modalidade | Função legítima pretendida | Não pode fazer por si |
| --- | --- | --- |
| **Explorar** | Exibir relações, áreas de evolução, fatos, contextos, possibilidades e suas proveniências/temporalidades elegíveis; permitir foco, zoom e explicação do significado de conexões | Transformar ligação semântica em navegação autorizada ou criação/edição de objetivo, passo ou evolução |
| **Escutar** | Gerar sob demanda narrativa contextual sobre uma versão identificável; pausar, interromper, retomar quando permitido, oferecer alternativa textual | Afirmar causalidade/progresso não comprovados, reproduzir informação revogada ou registrar áudio indefinidamente por padrão |
| **Conversar** | Perguntar, esclarecer contexto, receber novas informações e explorar hipóteses com a Intelligence; exibir incerteza e pedir validação quando apropriado | Persistir cada frase como fato, autorizar personalização, agir em objetos de domínio ou tratar hipótese como histórico confirmado |

**Princípio comum:** as três modalidades representam perspectivas da **mesma compreensão governada e autorizada**; não geram três verdades independentes. A camada de apresentação/voz não se torna autoridade cognitiva.

## 6. Alternância e continuidade entre modalidades

Exemplo de sequência apenas funcional:

```text
Explorar relação
 → pedir explicação textual
 → escutar análise desse contexto
 → interromper narração
 → perguntar à Intelligence sobre o mesmo contexto
 → receber pergunta de esclarecimento
 → revisar resposta e seu status epistemológico
 → atualizar visão elegível ou manter hipótese separada
 → retornar a Hoje
```

**Regras candidatas:**
- Alternar modalidade é **escolha de apresentação** quando a responsabilidade funcional não muda. Não criar TRN a cada alternância sem justificativa de domínio.
- Preservar somente **referências mínimas, contexto de sessão permitido, foco atual e versão da compreensão**, segundo autoridade de dados.
- A fala de saída só narrará conteúdo disponível à finalidade e à versão; texto equivalente deve estar acessível.
- Quando conteúdo muda enquanto a Pessoa escuta, conversa ou explora, informar eventual **desatualização**; não substituir silenciosamente narrativa, grafo ou interpretações.
- Ao sair/voltar, **não** salvar edição incompleta, concluir passo, reconhecer evolução ou conceder nova autorização.

## 7. Estados funcionais locais propostos — sem IDs oficiais

| Estado local candidato | Condição | Resposta esperada |
| --- | --- | --- |
| Entrada elegível | Contexto revisado/autorizado compatível com finalidade | Acesso opcional a aprofundamento |
| Entrada indisponível ou parcial | Sem informação elegível/relações suficientes | Explicar limites sem exigir preenchimento artificial |
| Contexto em consulta | Sistema obtém versão autorizada | Indicação neutra de processamento, sem afirmar sucesso |
| Exploração ativa | Conjunto de relações sustentadas | Grafo navegável na própria apresentação, com proveniência |
| Escuta ativa | Narração permitida e disponível | Texto equivalente, pausar/parar e indicação de origem |
| Conversa ativa | Sessão voluntária | Perguntas contextuais e status de inferência/declaração |
| Hipótese ou informação nova | Pessoa introduz afirmação não validada | Separar uso temporário, confirmação e eventual persistência |
| Contexto desatualizado | Versão/revogação/alteração concorrente | Avisar, reconsultar e bloquear reutilização indevida |
| Falha parcial de áudio | Provedor indisponível | Fallback textual sem invalidar o grafo inteiro |
| Falha parcial da visualização | Grafo não apresentado | Perspectiva textual acessível sem fabricar relações |
| Saída/retorno | Pessoa decide encerrar exploração | Volta neutra a Hoje com reconsulta do estado canônico |

Esses nomes **não são máquina de estados aprovada** e não constituem novas superfícies.

## 8. Aprendizado Contextual Contínuo — passagem de informação

```text
Declaração recebida (texto/voz/anexo)
 → origem e finalidade identificadas
 → interpretação/hipótese separada da declaração
 → uso local de sessão, se legítimo
 → verificação de lacunas e confirmação proporcional
 → decisão independente de persistência e personalização
 → atualização governada (se autorizada)
 → projeções elegíveis para grafo/narração/conversa
```

- **Sessão ≠ memória persistida ≠ personalização**.
- Informação nova não se torna fato confirmado apenas por surgir na conversa.
- Correção, contestação e revogação exigem reavaliação de derivados, caches e narrativas segundo as autoridades de dados.
- Neo4j, se futuramente utilizado, é **projeção da compreensão governada**, não fonte de verdade dos objetos de domínio.
- Nenhum esquema, prazo de retenção ou trânsito para fornecedor é autorizado por este documento.

## 9. Fronteiras de responsabilidade

| Camada | Competência a preservar |
| --- | --- |
| **PER-008 — Hoje** | Síntese atual, convite opcional a aprofundamento e retorno neutro, conforme contrato a decidir |
| **Destino expandido** | Exploração integrada e modos de apresentação; autoridade funcional ainda pendente |
| **Guivos Intelligence** | Compreender, identificar lacunas, perguntar, aprofundar, reavaliar, validar e direcionar, sob GPA-006/GIA-COG-001 |
| **PER-007 e dados** | Revisão consciente, escolhas independentes sobre persistência/personalização, proveniência e correção |
| **PER-010/011/012** | Objetivos, Próximos Passos e Evolução; mudanças materiais somente por suas superfícies/autoridades |
| **Orquestração e Registries** | Fluxo de responsabilidade, origem, destino, retorno, estados e maturidade das transições |
| **Provedores e infraestrutura** | Execução técnica eventual de processamento/voz/projeção; sem autoridade cognitiva ou de domínio |

## 10. Casos críticos de saída e recuperação

1. **Saída voluntária:** retornar ao contexto legítimo de Hoje sem criar progresso ou confirmar sugestão.
2. **Interrupção de narração para conversar:** interromper áudio, manter apenas foco/versão elegível, permitir fala ou texto; não recomeçar conteúdo desatualizado automaticamente.
3. **Sessão encerrada:** não prometer retomada de conteúdo efêmero quando persistência não autorizada.
4. **Revogação:** impedir uso futuro de conteúdo que perdeu autorização e reavaliar suas projeções/derivados segundo autoridade específica.
5. **Mudança concorrente:** comparar versões; evitar que um relatório antigo apareça como diagnóstico atual.
6. **Falha de fornecedor de voz:** manter caminho textual acessível sem declarar indisponibilidade total da Jornada.
7. **Nó com ação sobre domínio:** exibir explicação e, se houver acesso autorizado, remeter à superfície responsável pelo objeto, sem ação automática.

## 11. Quesitos para a próxima deliberação da Direção

A **Alternativa B já foi selecionada**. Restam escolhas distintas, a serem solicitadas expressamente:

| Questão | Opção 1 | Opção 2 | Critério |
| --- | --- | --- | --- |
| **Competência do destino** | Estado expandido de responsabilidade já existente, mediante demonstração de compatibilidade | Responsabilidade funcional distinta a contratar | Não sobrecarregar Hoje nem criar IDs por conveniência |
| **Entrada em Hoje** | Oferecer apenas em Hoje recorrente quando aplicável | Também na primeira entrada, se contexto suficiente | Não presumir histórico nem impor acesso |
| **Saída/retorno** | Estado de apresentação sob contrato existente, se comprovado | Handoff e retorno dedicados sujeitos a Registry | Mudança real de competência, contexto e efeito |
| **Retomada de sessão** | Sem persistência por padrão | Persistência separada, opt-in, sob regras aprovadas | PER-007, finalidade, retenção, revogação e segurança |

**Parecer de instrução, não seleção:** recomenda-se **examinar primeiro a competência do destino**. Só então é seguro adjudicar se entrada/retorno são mudanças de superfície com nova transição. Não formular nomes/IDs oficiais antes desse exame.

## 12. Gate de prontidão para a implementação

A decisão B, por si, **não aprova** implementação no workspace [Jornada da Pessoa](https://replit.com/@guivos/Jornada-da-Pessoa). Antes de solicitar execução, preservar esta sequência de evidências:

1. Competência do destino e entrada/retorno adjudicados e reconciliados nas autoridades aplicáveis.
2. Contratos de memória, consentimento, privacidade, voz, acessibilidade, falha, versão e provedores examinados.
3. Auditoria **somente de leitura** do Replit mediante autorização própria, confrontando a tela “Composição da Pessoa” com a arquitetura efetiva.
4. Plano incremental explícito com escopo, dados sintéticos, risco, recuperação e critérios de aceite.
5. Autorização específica de Design/desenvolvimento/testes/publicação conforme cada alcance.

**Estado deste documento:** especificação funcional candidata preparada em PR rascunho; nenhuma mudança nos Masters/Registries, no GKR publicado ou no Replit.


## Atualização posterior de decisão (08/11/2026)

A Direção selecionou expressamente a **possibilidade 2 — responsabilidade funcional distinta** para o destino expandido. Ver [Registro de Decisão — Responsabilidade Distinta](decisao-direcao-responsabilidade-distinta.md). Assim, a alternativa “estado de responsabilidade existente” mencionada nos quesitos anteriores fica preservada como hipótese histórica **não selecionada**; o próximo exame deverá tratar de **contratos de entrada e retorno**, elegibilidade na primeira entrada e representação documental da responsabilidade, sem criar automaticamente nova superfície, PER-ID, TRN-ID ou autorização operacional.
