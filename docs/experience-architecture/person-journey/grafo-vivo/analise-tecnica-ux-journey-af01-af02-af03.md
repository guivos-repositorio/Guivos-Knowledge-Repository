---
title: Grafo Vivo — Análise Técnica UX/Journey AF-01, AF-02 e AF-03
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: technical_evidence_for_specialist_review
---

# Grafo Vivo — Análise Técnica UX/Journey AF-01, AF-02 e AF-03

> **Análise de evidências para consulta à Arquitetura da Experiência, não parecer emitido em nome dessa autoridade.** A Direção da Guivos foi designada como decisora final do Grafo Vivo pelo [Registro AF-10](decisao-direcao-competencia-af10.md), condicionada à consulta técnica. Esta análise confronta fontes específicas e delimita recomendações **não vinculantes**. Não seleciona localização A/B/C, não cria tela ou transição, não aprova alteração de PER-008, API, Design, teste ou implantação.

## 1. Base de consulta verificada

- **PER-008 — Documento Mestre de Hoje**, `GKR-UX-PER008-MASTER-001`, v0.1.0: seções 1–6 e 11–14; mesma superfície para primeira entrada e retorno, sem criar segundo PER-ID; síntese contextual e continuidade, sem absorver especializações.
- **Orquestração UX/UI da Pessoa**, `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001`, v0.4.0: seções 1, 5, 13, 17 e 26–27; responsabilidades locais permanecem nos Masters e Registries.
- **Surface Registry**, `GKR-JOURNEY-SURFACE-REGISTRY-001`, v0.36.22: PER-008 validado no escopo; PER-010/011/012 são responsabilidades especializadas, não extensões implícitas de Hoje.
- **Transition Registry**, `GKR-JOURNEY-TRANSITION-REGISTRY-001`, v0.29.26: `TRN-007` e `TRN-008..013` integralmente validados documentalmente **no limite de cada autoridade**, não como prova de implementação técnica.
- **Consulta Focal UX/Journey** preparada e **Decisão AF-10 da Direção** no estudo do Grafo Vivo. A decisão AF-10 resolve a instância final deste escopo, não dispensa parecer especializado.

## 2. AF-01 — Até onde vai PER-008 — Hoje?

**Constatações em fontes vigentes:**
1. A finalidade de Hoje é sintetizar contexto legítimo e permitir que a Pessoa escolha agir ou não, sem fabricar urgência, objetivo, passos, evolução ou histórico (Master PER-008 §§1–6).
2. Primeira entrada e uso recorrente são **estados da mesma superfície**; por si sós não criam outra superfície/ID (Master §§1–2).
3. A primeira entrada pode legitimamente ter dados ausentes; personalização não escolhida não pode ser presumida (Master §4).
4. Hoje recorrente pode oferecer acesso a aprofundamentos especializados, quando os affordances forem aplicáveis, por transições já contratadas (Master §§5, 11–13; Orquestração §5).
5. A Orquestração não substitui o Master e não pode criar, por conveniência de UX, nova responsabilidade (Orquestração §§1, 17, 26–27).

**Interpretação técnica candidata, sujeita à autoridade UX/Journey:**
- **Explanação textual opcional do conteúdo atualmente elegível de Hoje** e **escuta acessível de conteúdo semanticamente equivalente** podem ser examinadas como estados/affordances leves **sem necessariamente criar superfície nova**. Esta é uma hipótese de compatibilidade, não permissão de integração de voz/IA.
- **Conversa breve de esclarecimento** só seria compatível em tese se não introduzir memória nova, simulação persistida ou alteração de objetos e se respeitar a competência cognitiva de GIA. A mera existência do chat não cria tal permissão.
- **Grafo transversal exploratório profundo, relatório narrado com inferências amplas, simulações e diálogo contínuo com retenção** extrapolam a evidência de suficiência do Master para afirmar enquadramento automático em Hoje.

**Conclusão AF-01 para consulta:** provável distinção útil entre (i) **explicar a síntese já permitida** e (ii) **instituir experiência ampliada**. A autoridade UX/Journey deve confirmar a fronteira e registrar seu fundamento. Nenhuma forma operacional fica aprovada.

## 3. AF-02 — Estado interno ou competência funcional distinta?

**Evidência:** o Surface Registry reconhece PER-008 — Hoje e PER-010/011/012; não foi localizada, no confronto atual, uma superfície própria de Grafo Vivo. A Orquestração §17 veda inventar um PER-ID em razão de lacuna de materialização.

| Hipótese de arranjo | Condição mínima a consultar | Achado |
| --- | --- | --- |
| **A — Dentro de Hoje** | Manter finalidade e limites de conteúdo de PER-008; nenhum efeito novo de domínio | **Possível objeto de exame para explicações leves**, insuficiente para expansão plena |
| **B — Hoje como entrada** | Reconhecer onde reside responsabilidade pela exploração expandida e se ela pode existir como estado sob competência já vigente ou requer nova responsabilidade | **Principal lacuna de competência**; não há surface contratada para assumir a experiência por simples desenho |
| **C — Distribuída** | Aprofundamentos de cada objeto permanecerem nas superfícies especializadas; plano de continuidade cognitiva transversal sem atribuir ação a Hoje | **Examinável no âmbito de cada domínio**, mas representação integrada continua sem atribuição demonstrada |

**Conclusão AF-02 para consulta:** **não é suficiente** a documentação atual para determinar que toda a exploração expandida seja estado de PER-008, nem que deva ser automaticamente uma superfície independente. São ambas hipóteses a decidir. A alternativa B é prioritária para exame, não vencedora.

## 4. AF-03 — Handoff, retorno e continuidade

### Contratos confirmados

| Origem | Handoff vigente | Destino | Limite |
| --- | --- | --- | --- |
| PER-007 | TRN-007 | PER-008 | Compreensão revisável → Hoje, sem nova autorização implícita |
| PER-008 | TRN-008 / retorno TRN-009 | PER-010 | Objetivos; navegação não cria/altera objetivo |
| PER-008 | TRN-010 / retorno TRN-011 | PER-011 | Passos; não iniciar/aceitar/concluir ao navegar |
| PER-008 | TRN-012 / retorno TRN-013 | PER-012 | Evolução; não confirmar baseline ou progresso |

`TRN-008`, `TRN-010` e `TRN-012` pertencem ao **Hoje recorrente** quando o acesso correspondente existe e é aplicável; a primeira entrada não precisa exibi-los. Não há handoffs diretos contratados entre PER-010, PER-011 e PER-012.

### Distinção a confirmar com UX/Journey

- **Estado interno de apresentação:** mudar de texto para escuta da mesma síntese, ocultar/abrir explicação ou focalizar uma relação **pode não representar transição de competência**, se não ocorrer mudança de responsabilidade, contexto ou efeito.
- **Aprofundamento em responsabilidade diferente:** acesso voluntário a espaço funcional distinto de Hoje **pode exigir handoff e retorno governados**; nenhuma transição específica de Grafo Vivo existe hoje neste conjunto validado.
- **Nó do grafo ligado a objetivo/passo/evolução:** relação semântica não é aresta de navegação. Ações devem seguir a autoridade do objeto e as transições realmente disponíveis, sem inventar atalhos especializados.
- **Voltar à síntese:** reconsultar contexto canônico elegível; não atribuir efeitos silenciosos. Para voz, interrupção e retomada requerem regras específicas de sessão/dados, não automaticamente um TRN.

**Conclusão AF-03 para consulta:** não existe evidência suficiente para declarar um contrato de entrada/retorno da modalidade expandida. Se a Direção e a autoridade UX/Journey vierem a reconhecer responsabilidade funcional distinta, deve-se examinar e eventualmente contratar o handoff por ato separado. O estudo **não cria número TRN**.

## 5. Casos de borda para resposta especializada

| Caso | Expectativa semanticamente segura | Pergunta ainda aberta |
| --- | --- | --- |
| Primeira entrada sem histórico | Síntese neutra/ausência legítima | O affordance leve é útil ou indevido? |
| Primeira entrada com compreensão revisada | Expor apenas contexto confirmado e autorizado | Explicação pode ser disparada antes da escolha de persistência? |
| Pessoa retorna a Hoje | Estado canônico reconsultado | Quais versões contextuais podem circular no grafo? |
| Interrompe áudio e conversa | Sem assumir persistência automática | Quem mantém contexto de sessão e por quanto tempo? |
| Clica em nó “Objetivo” | Consulta sem alteração material | Quando precisa abrir PER-010 via TRN-008? |
| Clica de Objetivo em Passo | Sem atalho direto presumido | Precisa retornar por TRN-009 e acessar via TRN-010? |
| Explora evolução hipotética | Hipótese ≠ evolução reconhecida | Qual competência distingue simulação e evidência real? |
| Revoga uso de informação | Derivados reavaliados conforme autoridade | Quais gates de Dados/Privacidade prevalecem? |

## 6. Quesitos de resposta para a Arquitetura da Experiência

Solicita-se manifestação verificável sobre:

1. **AF-01:** a separação entre explicação leve e experiência expandida respeita o Master de Hoje? Existem limites adicionais ou contradições específicas?
2. **AF-02:** há competência já reconhecida que possa abrigar o aprofundamento multimodal, ou é necessário ato de responsabilidade adicional? O que impede cada alternativa?
3. **AF-03:** quais interações seriam estados internos sem TRN, quais requereriam handoff/retorno, e qual autoridade poderia contratá-los?
4. **Transversal:** o tratamento de primeira entrada/retorno e a ausência legítima de histórico são adequados? Que dependências de GIA, PAS-001, Privacidade e Planos devem preceder a decisão final?

Para cada resposta: fonte e versão, interpretação, divergências, competência do signatário, efeitos admissíveis e ressalvas. **Não presumir resposta porque o arquivo foi publicado no PR.**

## 7. Encaminhamento para a Direção

**Síntese candidata (não parecer oficial de UX):**
- O Master atual permite argumentar a favor de **modos leves de acesso à síntese** como objeto de exame em PER-008;
- uma **experiência expandida** de Grafo Vivo não possui posição/competência e transição já adjudicadas;
- **B** separa melhor a hipótese de síntese e aprofundamento, mas depende do reconhecimento de competência e handoff, e não deve ser selecionada sem a consulta e decisão;
- **A e C** seguem alternativas abertas, sobretudo para acessibilidade e aprofundamentos especializados.

A Direção pode deliberar após receber pareceres especializados verificáveis e resolver os gates complementares. Este arquivo **não substitui** a manifestação especializada.

## 8. Situação de consulta e execução

- Documento de análise técnica: **preparado em PR rascunho**.
- Parecer formal emitido pela Arquitetura da Experiência: **não comprovado**.
- Destinatário pessoal/equipe revisora formalmente notificado: **não comprovado**.
- Decisão final A/B/C: **não emitida**.
- Revisão de Master, Surface Registry ou Transition Registry: **não realizada**.
- Implantação em [Jornada da Pessoa — Replit](https://replit.com/@guivos/Jornada-da-Pessoa): **não autorizada ou executada**.
- Revisão editorial do MENU GKR antes de merge: **pendente**.

**Próximo ato com valor decisório:** manifestação especializada atribuível sobre AF-01/02/03, registrada por canal aprovado, seguida de deliberação da Direção. Evitar novo ciclo de dossiês para suprir a ausência de um parecer efetivamente emitido.


## Atualização posterior — escolha da Alternativa B pela Direção (08/11/2026)

Após o estado histórico descrito acima, a Direção aprovou expressamente a **Alternativa B — Hoje como entrada para uma experiência expandida**. Ver [Registro de Decisão — Alternativa B](decisao-direcao-alternativa-b.md). Assim, quaisquer referências anteriores a “A/B/C não selecionadas” ou “B apenas prioritária para exame” registram a condição **anterior** à decisão e não o estado atual. Permanecem pendentes a responsabilidade formal do destino expandido, os contratos de superfície/transição e toda autorização operacional.
