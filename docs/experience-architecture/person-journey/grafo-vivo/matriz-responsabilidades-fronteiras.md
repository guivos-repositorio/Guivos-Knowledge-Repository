---
title: Grafo Vivo — Matriz de Responsabilidades e Fronteiras Funcionais
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: exploratory_non_operational
---

# Grafo Vivo — Matriz de Responsabilidades e Fronteiras Funcionais

> **Exame documental conceitual, sem adjudicação de competência.** A matriz distingue responsabilidades correntes verificadas dos comportamentos candidatos do Grafo Vivo. Não autoriza nova superfície, fluxo, permissão, API ou implementação; não cria IDs oficiais.

## 1. Objetivo e base

Aproximar a experiência candidata **Explorar / Escutar / Conversar** das autoridades existentes, identificando o que pode ser apresentado, entendido, atualizado ou armazenado sem que o grafo ou o motor de voz se torne autoridade de domínio.

Referências examinadas:
- `GKR-UX-PER007-MASTER-001` — Compreensão Inicial Revisável;
- `GKR-UX-PER008-MASTER-001` — Hoje;
- `GKR-UX-PER010-MASTER-001` — Meus Objetivos;
- `GKR-UX-PER011-MASTER-001` — Meus Próximos Passos;
- `GKR-UX-PER012-MASTER-001` — Minha Evolução;
- `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001`;
- GPA-006 / Guivos Intelligence; GIA-COG-001; PAS-001; Surface Registry; Transition Registry.

**Regra:** o estudo não substitui a leitura da versão vigente das autoridades e não define precedência ou estados além delas.

## 2. Matriz de responsabilidade por capacidade

| Capacidade | Autoridade/responsabilidade vigente | Grafo Vivo — comportamento candidato, dependente de gate | Fronteira |
| --- | --- | --- | --- |
| Revisão da compreensão inicial | PER-007 | Pode explicar e visualizar apenas afirmações elegíveis, segundo permissões existentes | Não confirmar compreensão em nome da Pessoa |
| Persistência da compreensão | PER-007 e autoridades de dados/privacidade | Pode consultar decisão vigente antes de usar memória | Visualizar/escutar/conversar não autoriza persistência |
| Personalização | Escolha independente, PER-007 + autoridades posteriores | Apresentar resultados contextualizados somente no escopo autorizado | Persistência ≠ personalização |
| Síntese do presente | PER-008 — Hoje | Exploração/escuta de contexto coerente; localização funcional não adjudicada | Hoje não é dashboard de performance humana |
| Objetivos | PER-010 + PAS-001 Objetivos | Representar objetivo existente, sua origem e relações explicáveis | Nó não cria, aceita, prioriza, edita ou conclui objetivo |
| Próximos Passos | PER-011 + PAS-001 Próximos Passos | Explicar relações e condições de passos legitimamente existentes | Sugestão ≠ passo aceito ou executado |
| Evolução e trajetória | PER-012 + PAS-001 Evolução | Exibir comparações temporais fundamentadas e suas incertezas | Mudança de grafo ≠ reconhecimento de evolução |
| Compreensão, inferência e lacunas | GPA-006 / Guivos Intelligence, GIA-COG-001 | Produzir explicações e relações candidatas | Inteligência não assume autoria das escolhas da Pessoa |
| Projeção gráfica | Responsabilidade de interface a delimitar | Renderizar subgrafo filtrado; permitir consulta por origem | Grafo não é fonte de verdade nem entidade PAS-001 automática |
| Relatório narrado | Responsabilidade nova a examinar | Gerar narração de versão contextual autorizada | Áudio não comprova, decide, valida ou persiste nada por escuta |
| Conversa multimodal | Responsabilidade de interação e Intelligence a examinar | Receber perguntas e informações, explicar e propor contextualização | Motor de voz não decide retenção, consentimento ou mudança de domínio |
| Oportunidades reais | Fontes e contratos competentes da Journey | Exibir apenas oportunidades com status/eligibilidade verificados | Possibilidade hipotética ≠ Oportunidade Ativa |
| Experiências comprovadas | Autoridades de Experiência/evidência | Mostrar aprendizado declarado distinto de experiência verificada | Afirmação oral ≠ prova de realização |

## 3. Matriz operacional de eventos — somente conceitual

| Evento de interface | Ler | Interpretar | Possível alteração | Governança necessária |
| --- | --- | --- | --- | --- |
| Abrir Hoje | Estado canônico autorizado | Síntese legitimamente permitida | Nenhuma por abertura | PER-008 + autorizações vigentes |
| Selecionar nó | Subgrafo/proveniência elegíveis | Explicação contextual | Nenhuma | Acesso e minimização |
| Perguntar sobre conexão | Nó e contexto permitido | Intelligence explica sem inventar causalidade | Nenhuma automática | GIA-COG-001 + finalidade |
| Dizer “comecei um curso” | Nova mensagem ou transcrição | Classificar declaração, tempo e relações candidatas | Consolidação **somente quando autorizada**, possivelmente com validação | PER-007/decisões vigentes + governança de dados |
| Dizer “e se eu fizesse um curso?” | Hipótese temporária | Comparar cenário | Nenhuma no contexto real | Isolamento de simulação |
| Selecionar caminho de possibilidade | Cenário/oportunidade verificada | Explicação e condições | Nenhum objetivo/passo presumido | PAS-001 e autoridades de oportunidade |
| Abrir Meu Objetivo | Objeto existente | Visão apropriada | Apenas ações governadas por PER-010 | TRN-008/009 |
| Abrir Próximo Passo | Estado de passo existente | Explicação de dependências | Apenas ações governadas por PER-011 | TRN-010/011 |
| Abrir Minha Evolução | Trajetórias e evidências permitidas | Contextualização temporal | Apenas ações governadas por PER-012 | TRN-012/013 |
| Iniciar narração | Versão/snapshot autorizados | Roteiro pela Intelligence e síntese de voz | Nenhuma por escutar | Finalidade, minimização e versionamento |
| Interromper para perguntar | Trecho narrado e contexto mínimo | Diálogo dirigido | Alteração só em fluxo governado independente | Consentimento, revisão e sincronismo |
| Corrigir informação | Fonte original e objetos derivados | Verificar efeitos e inconsistências | Correção por autoridade competente, seguida de invalidação derivada | Direitos, proveniência, caches, relatórios e memória |
| Revogar autorização | Escopos concedidos | Reavaliar possibilidades de uso | Desabilitar usos e projeções não elegíveis | Retenção, exclusão, auditoria e revogação |

Esta tabela **não é contrato de API ou eventos**, nem autorização para gravar dados.

## 4. Matriz RACI conceitual — não substitui donos canônicos

**Legenda:** R = executor candidato; A = autoridade a consultar em documento vigente; C = consulta funcional; I = recebe estado/resultado permitido. A tabela não delega poder decisório novo.

| Atividade | Pessoa | Journey / domínio competente | Intelligence | Interface Grafo | Voz (Grok candidato) |
| --- | --- | --- | --- | --- | --- |
| Declarar ou corrigir uma informação | Decisão/autoria | A + R, conforme domínio | C / interpretação assistiva | I | Canal opcional |
| Autorizar persistência/personalização | Decisão afirmativa | A + R por PER-007/autoridades aplicáveis | C, uso condicionado | I | Não decide |
| Compreender contexto | C, validação/revisão | C / dados governados | R, sob GPA-006/GIA | Apresenta resultado permitido | Vocaliza conteúdo autorizado |
| Registrar objetivo ou passo | Decide/autoriza | A + R em PER-010/011 e PAS-001 | Pode sugerir | Não grava por inferência | Não grava por inferência |
| Mostrar mudança contextual | Revisa/contesta | A sobre dados canônicos | Interpreta relações | Renderiza projeção | Explica quando solicitado |
| Reconhecer trajetória/evolução | Revisa/controla | A + R em PER-012 e PAS-001 | Interpretação assistiva | Visualiza se permitido | Narração de conclusão fundamentada |
| Produzir relatório falado | Escolhe escutar | A sobre escopo/dados | R sobre conteúdo contextual | Opcional sincronização | R técnico de síntese, sem autoridade semântica |

Os termos RACI aqui são **didáticos**; competência final deve ser adjudicada pelos registros oficiais antes de especificação de engenharia.

## 5. Fluxos autorizados existentes que não podem ser estendidos por inferência

```text
PER-007 --TRN-007--> PER-008
PER-008 --TRN-008--> PER-010 --TRN-009--> PER-008
PER-008 --TRN-010--> PER-011 --TRN-011--> PER-008
PER-008 --TRN-012--> PER-012 --TRN-013--> PER-008
```

Sem handoffs diretos contratados entre PER-010, PER-011 e PER-012. A relação semântica no grafo não permite criar links que os contornem. Não está adjudicado se modos de explorar/escutar/conversar pertencem a estados em PER-008, aprofundamentos existentes ou outra estrutura autorizada futuramente.

## 6. Fronteiras de informação e integração

1. **Identidade e autorização:** cada consulta deriva da sessão e dos escopos de finalidade; não compartilhar contexto entre participantes por associação relacional.
2. **Fonte canônica:** registrar objetos de domínio na autoridade competente. Neo4j, se escolhido, é projeção/memória relacional; não substitui o registro de objetivos, passos, experiências ou decisões de consentimento.
3. **Intelligence:** interpretar informações e relações, apontar lacunas e explicar; não tomar decisões da Pessoa.
4. **Grafo:** apresentar subconjunto permitido e explicável; expor origem e temporalidade sem material sensível excessivo.
5. **Voz:** Grok/xAI é candidato para saída TTS e conversa em tempo real; não pode assumir gravação de memória por simples fala, nem receber dados além do necessário.
6. **Sincronização:** se mudança autorizada afetar uma afirmação derivada, considerar invalidação de conexões, caches, narrativas e relatórios antigos, preservando rastreabilidade apropriada.
7. **Simulações:** espaços hipotéticos são isolados. A Pessoa dizer “e se...” não altera objetivos, dinheiro disponível, competências nem tempo real.
8. **Observabilidade:** monitoramento técnico minimizado, sem captura indiscriminada de relatos pessoais.

## 7. Lacunas que exigem decisão

| Lacuna | Pergunta a resolver | Quem deve ser consultado |
| --- | --- | --- |
| L-01 — Posição UX | As três modalidades podem existir como estados legítimos de Hoje? | UX/Journey, Surface/Transition Registry |
| L-02 — Memória posterior | Qual escopo de persistência cobre novas informações de conversas recorrentes? | PER-007, Privacidade/Dados, GIA |
| L-03 — Objetos do grafo | Quais nós/arestas representam objetos PAS-001 versus inferências temporárias? | PAS-001, GIA/Intelligence |
| L-04 — Síntese temporal | Como narrar mudanças sem criar evolução por inferência? | PER-012, GIA |
| L-05 — Handoff | Como abrir aprofundamentos sem novos atalhos não contratados? | Transition Registry, UX/Journey |
| L-06 — Motor de voz | Que contexto mínimo, retenção, interrupções e custos são admissíveis no Grok? | Segurança/Privacidade, Engenharia, GIA |
| L-07 — Correção e revogação | Como propagar correções a projeções, áudio e snapshots? | Dados/Journey, GIA, Segurança |
| L-08 — Oferta comercial | Quais funcionalidades podem depender de planos existentes? | Contratos de Planos/Produto; não presumir cotas |

## 8. Caminho de continuidade

Recomendação documental: produzir **Exame de Compatibilidade e Lacunas da Entrada do Grafo Vivo em PER-008**, verificando se os comportamentos candidatos se encaixam em responsabilidades já reconhecidas ou necessitam adjudicação explícita. Não aprovar de antemão uma nova tela, transição, entitlement ou implementação.

**Estado final:** matriz candidata consolidada para análise. Não altera autoridades vigentes nem constitui aprovação técnica.
