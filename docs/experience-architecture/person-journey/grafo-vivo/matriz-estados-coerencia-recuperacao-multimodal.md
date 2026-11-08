---
title: Grafo Vivo — Matriz de Estados de Coerência e Recuperação Multimodal
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: diagnostic_non_operational
---

# Grafo Vivo — Matriz de Estados de Coerência e Recuperação Multimodal

> **Diagnóstico documental condicionado.** Este documento explora como a experiência poderá se recuperar de interrupções, divergências de contexto e indisponibilidades. Não é contrato técnico, enumeração oficial de estados, máquina de estados para execução, SLA, design aprovado, autorização de testes, API, alteração normativa ou criação de novos IDs oficiais.

## 1. Problema e princípio

O Grafo Vivo oferece três modalidades candidatas: **Explorar visualmente**, **Escutar a análise** e **Conversar com a Guivos Intelligence**. Uma interrupção ou atualização não pode transformar informação antiga em fato atual, ampliar consentimento nem obrigar a Pessoa a recomeçar a Jornada.

A experiência deve procurar **continuidade segura e coerência explicável**, não a aparência enganosa de sincronização instantânea.

## 2. Autoridades que permanecem intactas

- **PER-007:** compreensão revisável, decisões distintas sobre persistência e personalização; uso temporário não significa retenção posterior.
- **PER-008:** Hoje como síntese contextual, primeira entrada ou retorno; ausência legítima de conteúdo e continuidade sem personalização.
- **PER-010/011/012 e PAS-001:** autoria de objetivos, controle dos próximos passos e reconhecimento de evolução pertencem aos seus contratos.
- **GPA-006 e GIA-COG-001:** Intelligence governa interpretação e explicações, sem decidir pela Pessoa.
- **Surface/Transition Registries:** estados multimodais não criam telas nem handoffs adicionais.
- **Privacidade, Dados, Segurança:** versões, caches, retenção e transferências requerem autorizações competentes.

## 3. Estados locais candidatos para exame

| Estado local | Significado de experiência | Regra de segurança |
| --- | --- | --- |
| M0 — Coerente e disponível | Modalidade usa contexto elegível e versão identificável | Não implica que as demais modalidades estejam sincronizadas |
| M1 — Atualização em análise | Informação recebida ainda está sob interpretação, validação ou consolidação | Não apresentar hipótese como alteração confirmada |
| M2 — Derivado desatualizado | Grafo, resposta ou relatório usa versão anterior, mas existe contexto mais recente | Identificar versão e evitar afirmação enganosa de atualidade |
| M3 — Interrompido recuperável | Áudio, conversa ou visualização sofreu interrupção sem invalidar toda a sessão | Retomar somente a partir do ponto permitido |
| M4 — Parcialmente indisponível | Um serviço falha, mas há alternativas legítimas | Não inventar resultados nem forçar outra modalidade |
| M5 — Autorização alterada | Permissão foi revogada ou reduzida no curso do uso | Restringir imediatamente novos usos incompatíveis |
| M6 — Conflito/versão concorrente | Duas alterações divergem ou uma atualização chega fora de ordem | Não eleger um fato arbitrariamente; consultar fonte/versão competente |
| M7 — Sessão encerrada ou expirada | Continuidade deixa de ser autorizada ou viável | Descartar contexto efêmero conforme política; não prometer recuperação universal |
| M8 — Reconstrução elegível | Derivados podem ser recompostos de fontes governadas após correção/falha | Validar finalidade e permissões antes de recomputar |

Os rótulos M0–M8 são **referências locais do estudo**, não valores de banco, eventos de arquitetura, novos códigos de erro ou estados normativos.

## 4. Matriz de incidentes e recuperação

| Incidente | Detectar / comunicar | Conduta conceitual | Não fazer |
| --- | --- | --- | --- |
| Grok TTS interrompe narração | Informar pausa/falha de áudio e referência de análise | Oferecer texto equivalente; retomar trecho se versão e permissões permitirem | Declarar narração concluída ou gerar informações inventadas |
| Conversa por voz perde conexão | Indicar que a resposta ou captura foi interrompida | Preservar somente contexto autorizado, conferir se a última mensagem chegou e permitir retomada | Duplicar envio, gravar continuação presumida |
| Transcrição duvidosa | Sinalizar trecho incerto quando material | Solicitar confirmação pontual antes de consolidar | Alterar memória por reconhecimento incerto |
| Neo4j/grafo indisponível | Comunicar falha de relações, não de toda a Jornada | Oferecer síntese autorizada baseada em fonte canônica, se disponível | Fabricar nós ou apresentar cache como verdade recente |
| Grafo em versão anterior | Indicar atualização pendente ou divergência temporal material | Reavaliar subgrafo elegível sem deslocar contexto do usuário abruptamente | Trocar relações silenciosamente quando isso altera significado |
| Contexto muda durante narração | Identificar versão do relatório versus contexto vigente | Oferecer atualização, pausa ou continuidade qualificada conforme efeito e permissão | Reproduzir conteúdo inválido como se fosse atual |
| Pessoa corrige declaração no chat | Distinguir correção de nova hipótese | Verificar autoridade e revigorar projeções afetadas quando autorizado | Apagar origem ou sobrescrever domínio por inferência |
| Revogação durante sessão de voz | Reconhecer alteração de finalidade/escopo | Cessar novos usos incompatíveis e tratar derivados conforme política aplicável | Continuar enviando dados ao provedor com autorização antiga |
| Duas sessões alteram contexto | Identificar concorrência temporal e proveniência | Consultar versão canônica e aplicar regras futuras de resolução | “Última resposta do modelo vence” |
| Resposta do modelo chega atrasada | Comparar contexto/versão e permissão utilizados | Qualificar, descartar ou reavaliar saída obsoleta conforme risco | Sobrescrever resultado mais novo |
| Sessão expira durante exploração | Indicar necessidade de continuidade legítima | Reautenticar quando necessário; preservar só o que for permitido | Reabrir acesso a conteúdo privado sem autorização |
| Falha parcial na geração de relatório | Indicar incompletude | Oferecer apenas trechos confiáveis e identificáveis, ou alternativa textual | Tratar análise parcial como relatório final |
| Reconexão repete mensagem/evento | Reconhecer possível duplicidade | Exigir exame de idempotência e versão futura | Duplicar memória, objetivos, passos ou evidências |
| Revogação após relatório armazenado | Sinalizar restrição de acesso/uso | Examinar áudio, texto, transcrições e caches derivados | Prometer exclusão total imediata em terceiros sem contrato |

## 5. Regras de continuidade entre modalidades

**Explorar → Escutar:** transmitir apenas foco contextual e versão de análise legitimamente disponíveis; narração pode ampliar explicação, mas não concluir ou confirmar fatos.

**Escutar → Conversar:** a pergunta pode referir-se ao trecho narrado, mas o provedor de voz recebe somente contexto mínimo necessário. Falar não representa autorização de persistência.

**Conversar → Explorar:** informação declarada só aparece como contexto consolidado após os gates aplicáveis. Hipóteses e cenários devem ser identificáveis e isolados.

**Retomar após interrupção:** permitir escolha de modalidade, sem obrigação de repetir informações já autorizadas e ainda disponíveis; não recuperar material que não deveria ter sido persistido.

## 6. Exemplo sintético — relatório interrompido por mudança de contexto

1. A Pessoa ouve um relatório baseado na referência contextual A.
2. Em outra sessão, corrige uma disponibilidade que altera materialmente algumas possibilidades.
3. A correção é validada pela autoridade do dado, conforme o contrato aplicável.
4. A Intelligence passa a ter uma referência atualizada B.
5. O player deve distinguir **relatório A** de **contexto B**, podendo pausar ou qualificar a reprodução de trechos afetados.
6. A Pessoa pode pedir nova análise para B, quando disponível e autorizada, ou continuar por texto.
7. Nenhuma alteração em objetivos ou passos decorre exclusivamente dessa troca de versão.

## 7. Exemplo sintético — perda de rede durante conversa com Grok

1. A Pessoa faz pergunta falada.
2. A ligação se interrompe antes de haver confirmação de recebimento.
3. A interface não presume que o conteúdo foi recebido ou armazenado.
4. Se existir estado de sessão autorizado, pode oferecer retomada e evitar processamento duplicado.
5. Se não existir estado legítimo recuperável, informa a limitação e oferece novo envio voluntário ou texto.
6. A transcrição, se obtida, ainda demanda tratamento de qualidade e autorização.

## 8. Hierarquia de recuperação candidata

| Prioridade | Princípio | Implicação |
| --- | --- | --- |
| 1 | Segurança, privacidade e autorização | Nunca recuperar dado mediante permissão revogada |
| 2 | Integridade de fonte e versões | Reconsultar registro competente antes de declarar estado atual |
| 3 | Continuidade de contexto legítimo | Evitar perda desnecessária do que pode ser preservado |
| 4 | Acessibilidade e alternativas | Conteúdo essencial não deve depender exclusivamente de áudio ou grafo |
| 5 | Conveniência e fluidez | Retomada de posição, foco e modo apenas quando permissível |

Esse ordenamento é **proposta de avaliação**, não regra normativa que adjudica outras autoridades.

## 9. Integrações envolvidas e falhas isoláveis

- **Grok/xAI Voice e TTS, candidato:** falha de áudio não deve indisponibilizar toda a compreensão textual.
- **Gemini ou outra transcrição:** erro/latência não deve virar alteração automática de contexto.
- **Neo4j Aura, candidato:** indisponibilidade de projeção não destrói a fonte governada.
- **Guivos Intelligence/modelos:** resposta atrasada ou contraditória requer referência de contexto e incerteza; não deve inventar autoridade.
- **Jornada / serviços canônicos:** falha de autorização ou fonte de verdade bloqueia ação de domínio até recuperação legítima.
- **Caches de grafo e relatórios:** só podem ser lidos/revalidados segundo autorizações correntes; políticas de retenção pendentes.
- **Interface multimodal:** deve comunicar interrupção, atualização e alternativas em linguagem acessível.

## 10. Lacunas a adjudicar futuramente

| Referência local | Questão pendente | Competência a consultar |
| --- | --- | --- |
| Q-01 | Quais estados são realmente reconhecidos e em qual superfície? | UX/Journey, Surface Registry |
| Q-02 | Qual critério de materialidade exige pausar a narração? | GIA, UX, Dados |
| Q-03 | Como retomar conversa sem memória persistente autorizada? | Privacidade, GIA, Engenharia |
| Q-04 | Qual semântica técnica de versão e resolução de concorrência? | Dados/Engenharia, PAS-001 |
| Q-05 | Quando utilizar síntese canônica sem projeção Neo4j? | Intelligence, Journey |
| Q-06 | Que retenção/recuperação de áudio Grok e demais provedores admitem? | Segurança, Jurídico/Privacidade, contratos |
| Q-07 | Como garantir alternativas acessíveis em redes móveis instáveis? | UX e acessibilidade |
| Q-08 | Como classificar falha parcial, degradação segura e indisponibilidade completa? | Engenharia, Observabilidade, Segurança |
| Q-09 | Como propagam-se correções/revogações a artefatos antigos? | Dados, Privacidade, GIA |
| Q-10 | Quais capacidades estão disponíveis em cada plano vigente? | Contratos comerciais, sem inventar entitlements |

Q-xx são referências apenas deste quadro, **não IDs oficiais**.

## 11. Parecer condicionado

A recuperação multimodal deve **preservar a autoridade e a verdade temporal**, mesmo ao custo de interromper parte da experiência. Continuidade não significa manter todos os serviços sempre disponíveis; significa oferecer caminhos legítimos, transparentes e acessíveis para prosseguir, sem duplicar efeitos ou apresentar material incorreto.

**Próxima atividade recomendada:** quadro consolidado de gates de prontidão conceitual, distinguindo o que já foi documentado do que depende de adjudicação de UX/Journey, Segurança/Privacidade, GIA, Dados, Planos e Engenharia.

**Estado:** estudo exclusivamente documental e condicionado. Nenhuma implementação, Design operacional, APIs, testes, alterações normativas, novo PER-ID, merge ou publicação autorizada.
