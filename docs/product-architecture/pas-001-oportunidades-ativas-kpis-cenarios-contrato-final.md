---
id: PAS-001-OA-CONTRACT-001
title: KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Oportunidades Ativas
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-15
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
  - PAS-001-OA-EVENT-001
  - PAS-001-OA-INTEGRATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-OA-CONTRACT-001 — KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Oportunidades Ativas

## 1. Autoridade e vínculo

Este documento é a **sexta extensão normativa e o contrato final da Capacidade 06 — Oportunidades Ativas** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 2061 a 2666, consolidadas por `PAS-001-OA-FOUNDATION-001 1.0.0`, `PAS-001-OA-LIFECYCLE-001 1.0.0`, `PAS-001-OA-VIEW-001 1.0.0`, `PAS-001-OA-EVENT-001 1.0.0` e `PAS-001-OA-INTEGRATION-001 1.0.0`, além da autoridade do `PAS-001 0.5.0` e das extensões concluídas de Contexto Vivo, Objetivos, Eventos de Vida e Próximos Passos.

Esta extensão substitui normativamente o estado `In progress` da Capacidade 06 por `Functionally complete` e eleva seu progresso editorial de referência de `90%` para `100%`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade da especificação-base ou das capacidades concluídas.

# 2667. Bloco final da Capacidade de Oportunidades Ativas

Este documento consolida:

- indicadores funcionais;
- baseline inicial;
- painel de saúde;
- níveis de desempenho;
- guardrails de tolerância zero;
- cenários funcionalmente ideais;
- cenários alternativos;
- cenários limite;
- critérios de conclusão;
- lacunas bloqueantes e não bloqueantes;
- contrato funcional final.

Os indicadores deverão avaliar a qualidade da capacidade e do sistema, não o mérito, a produtividade, o consumo, a disciplina, a fé, o sucesso ou o valor humano do participante.

# 2668. Finalidade dos indicadores

Os indicadores deverão permitir avaliar se a capacidade:

1. admite oportunidades legítimas;
2. limita a autoridade das fontes;
3. mantém disponibilidade atualizada;
4. representa elegibilidade com incerteza adequada;
5. avalia relevância sem manipulação;
6. preserva neutralidade comercial;
7. explica por que uma oportunidade foi apresentada;
8. mantém publicidade separada;
9. protege oportunidades sensíveis;
10. preserva alternativas públicas, gratuitas e não patrocinadas;
11. mantém o participante no controle;
12. distingue visualização, interesse, inscrição, aceitação, contratação e participação;
13. governa processos externos sem absorvê-los;
14. integra fontes com finalidade e minimização;
15. opera com idempotência, ordenação e concorrência;
16. permite contestação e correção;
17. propaga revogações;
18. reduz esforço e fadiga;
19. preserva explicabilidade e auditoria;
20. admite a ausência legítima de oportunidades.

# 2669. Princípios de medição

A medição deverá observar:

- finalidade funcional;
- proporcionalidade;
- não julgamento;
- proteção de dados;
- segmentação por contexto;
- distinção entre fatos e estimativas;
- explicabilidade;
- revisão periódica;
- ausência de metas arbitrárias;
- prevalência dos guardrails;
- distinção entre indicador do sistema e comportamento humano;
- impossibilidade de compensar risco crítico por média positiva.

Nenhuma média positiva deverá compensar violação crítica de guardrail.

# 2670. Unidades de medição

As métricas poderão utilizar:

- quantidade;
- proporção;
- taxa;
- tempo;
- distribuição;
- incidência;
- recorrência;
- severidade;
- cobertura;
- completude;
- atualidade;
- esforço declarado;
- esforço observado no fluxo;
- divergência;
- atraso de processamento;
- número de correções;
- número de contestações;
- concentração por fornecedor ou relação comercial.

Os indicadores deverão ser analisados por período, canal, origem, categoria, sensibilidade, fonte, relação comercial, estado funcional, disponibilidade, elegibilidade, finalidade e tipo de participante quando necessário.

# 2671. Famílias de indicadores

Os KPIs serão organizados em 15 famílias:

1. admissão e ativação;
2. fontes e autoridade;
3. disponibilidade;
4. elegibilidade;
5. relevância e compatibilidade;
6. transparência e neutralidade comercial;
7. descoberta, apresentação e ordenação;
8. relação e controle do participante;
9. processos e resultados externos;
10. privacidade, sensibilidade e terceiros;
11. integrações, sincronização e revogação;
12. confiabilidade e consistência;
13. explicabilidade, proveniência e auditoria;
14. acessibilidade, esforço e fadiga;
15. ausência, diversidade e equilíbrio do ecossistema.

# 2672. Família 1 — Admissão e ativação

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-001` | Candidaturas com identidade, fonte e finalidade suficientes | Mede admissibilidade mínima |
| `OA-KPI-002` | Candidaturas rejeitadas corretamente antes da ativação | Avalia bloqueio de fraude, proibição, exploração ou fonte inválida |
| `OA-KPI-003` | Duplicidades semânticas identificadas antes da ativação | Mede prevenção de registros equivalentes |
| `OA-KPI-004` | Ativações com critérios e limitações registrados | Avalia integridade do limiar funcional |
| `OA-KPI-005` | Itens de catálogo ativados sem avaliação funcional | Mede colapso entre disponibilidade e oportunidade ativa |

# 2673. Família 2 — Fontes e autoridade

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-006` | Fontes com identidade e autoridade validadas | Mede confiabilidade institucional |
| `OA-KPI-007` | Afirmações aceitas além do escopo da fonte | Mede ampliação indevida de autoridade |
| `OA-KPI-008` | Conflitos de interesse identificados e controlados | Avalia transparência da fonte |
| `OA-KPI-009` | Fontes desatualizadas com efeitos limitados | Mede proteção contra informação envelhecida |
| `OA-KPI-010` | Correções de fonte propagadas aos consumidores | Avalia consistência após correção |

# 2674. Família 3 — Disponibilidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-011` | Oportunidades ativas com disponibilidade avaliada | Mede cobertura da dimensão operacional |
| `OA-KPI-012` | Disponibilidades com fonte, data e validade explícitas | Avalia rastreabilidade temporal |
| `OA-KPI-013` | Oportunidades indisponíveis apresentadas como disponíveis | Mede violação crítica de veracidade |
| `OA-KPI-014` | Mudanças materiais de disponibilidade propagadas | Avalia atualização entre canais |
| `OA-KPI-015` | Retornos à disponibilidade submetidos a nova avaliação | Mede prevenção de reativação automática |

# 2675. Família 4 — Elegibilidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-016` | Avaliações de elegibilidade com requisitos e autoridade decisória | Mede completude da análise |
| `OA-KPI-017` | Estimativas apresentadas como confirmação ou aprovação | Mede colapso semântico |
| `OA-KPI-018` | Elegibilidades condicionadas com pendências visíveis | Avalia clareza das condições |
| `OA-KPI-019` | Critérios sensíveis minimizados e autorizados | Mede proteção reforçada |
| `OA-KPI-020` | Decisões externas de elegibilidade preservadas como externas | Avalia limite de responsabilidade |

# 2676. Família 5 — Relevância e compatibilidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-021` | Oportunidades apresentadas com justificativa compreensível | Mede explicabilidade da relevância |
| `OA-KPI-022` | Relevâncias avaliadas com contexto mínimo necessário | Avalia minimização |
| `OA-KPI-023` | Relevâncias reavaliadas após mudança material | Mede atualidade funcional |
| `OA-KPI-024` | Critérios desfavoráveis e incertezas preservados | Avalia ausência de persuasão seletiva |
| `OA-KPI-025` | Relevância influenciada por receita, clique ou patrocínio | Mede violação de neutralidade |

# 2677. Família 6 — Transparência e neutralidade comercial

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-026` | Oportunidades patrocinadas claramente identificadas | Mede transparência comercial |
| `OA-KPI-027` | Comissões, afiliações e exclusividades declaradas | Avalia completude econômica |
| `OA-KPI-028` | Alternativas sem comissão preservadas na comparação | Mede neutralidade do ecossistema |
| `OA-KPI-029` | Relações comerciais alteradas com histórico e revisão | Avalia governança de mudanças |
| `OA-KPI-030` | Interferências comerciais sobre ordem ou relevância | Mede violação crítica |

# 2678. Família 7 — Descoberta, apresentação e ordenação

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-031` | Descobertas com origem identificável | Mede rastreabilidade |
| `OA-KPI-032` | Apresentações autorizadas por Intervenções Contextuais | Avalia separação de responsabilidades |
| `OA-KPI-033` | Ordenações com critérios funcionais explicáveis | Mede neutralidade da lista |
| `OA-KPI-034` | Áreas publicitárias separadas da lista funcional | Avalia distinção visual e semântica |
| `OA-KPI-035` | Ausência de oportunidades tratada sem preenchimento artificial | Mede respeito ao silêncio funcional |

# 2679. Família 8 — Relação e controle do participante

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-036` | Visualizações convertidas indevidamente em interesse | Mede inferência proibida |
| `OA-KPI-037` | Ações de salvar, descartar, ocultar e contestar disponíveis | Avalia controle efetivo |
| `OA-KPI-038` | Interesses declarados com escopo e validade compreensíveis | Mede clareza da manifestação |
| `OA-KPI-039` | Retiradas de interesse processadas sem penalidade | Avalia reversibilidade |
| `OA-KPI-040` | Ocultações e limitações de reapresentação respeitadas | Mede aderência à preferência |

# 2680. Família 9 — Processos e resultados externos

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-041` | Inscrições iniciadas com autorização e destino explícitos | Mede consciência da ação |
| `OA-KPI-042` | Inscrições tratadas indevidamente como aceitação | Mede separação de estados |
| `OA-KPI-043` | Contratações recebidas como fatos externos delimitados | Avalia limite do agregado |
| `OA-KPI-044` | Participações interpretadas como resultado ou evolução | Mede ampliação indevida de significado |
| `OA-KPI-045` | Processos externos com estado, protocolo e pendências visíveis | Avalia acompanhamento confiável |

# 2681. Família 10 — Privacidade, sensibilidade e terceiros

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-046` | Oportunidades sensíveis com títulos e notificações minimizados | Mede proteção da superfície |
| `OA-KPI-047` | Buscas sensíveis utilizadas para publicidade | Mede violação crítica |
| `OA-KPI-048` | Compartilhamentos sensíveis com finalidade e destinatário explícitos | Avalia consentimento e minimização |
| `OA-KPI-049` | Dados de terceiros utilizados além da finalidade | Mede risco de perfil paralelo |
| `OA-KPI-050` | Retenções sensíveis revisadas e reduzidas | Avalia proporcionalidade temporal |

# 2682. Família 11 — Integrações, sincronização e revogação

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-051` | Integrações com finalidade, autoridade e escopo válidos | Mede admissibilidade técnica e funcional |
| `OA-KPI-052` | Recortes com excesso de informação | Avalia minimização |
| `OA-KPI-053` | Sincronizações divergentes com estado provisório explícito | Mede tratamento seguro de conflito |
| `OA-KPI-054` | Revogações propagadas integralmente | Mede interrupção efetiva de novos usos |
| `OA-KPI-055` | Integrações temporárias encerradas na validade prevista | Avalia expiração e retenção |

# 2683. Família 12 — Confiabilidade e consistência

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-056` | Efeitos duplicados por reprocessamento | Mede idempotência |
| `OA-KPI-057` | Estados impossíveis por eventos fora de ordem | Mede ordenação |
| `OA-KPI-058` | Conflitos de versão resolvidos sem sobrescrita | Avalia concorrência |
| `OA-KPI-059` | Falhas parciais apresentadas como sucesso integral | Mede veracidade operacional |
| `OA-KPI-060` | Recuperações concluídas com estado reconstruído | Avalia resiliência |

# 2684. Família 13 — Explicabilidade, proveniência e auditoria

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-061` | Decisões materiais com explicação disponível | Mede transparência |
| `OA-KPI-062` | Oportunidades com proveniência reconstruível | Avalia origem e transformação |
| `OA-KPI-063` | Correções com valor anterior e efeitos visíveis | Mede integridade histórica |
| `OA-KPI-064` | Fluxos integralmente reconstruíveis em auditoria | Avalia rastreabilidade |
| `OA-KPI-065` | Contestações resolvidas com fundamento e impacto explicados | Avalia justiça funcional |

# 2685. Família 14 — Acessibilidade, esforço e fadiga

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-066` | Informações materiais acessíveis sem navegação excessiva | Mede esforço de compreensão |
| `OA-KPI-067` | Comparações acessíveis por teclado e leitor de tela | Avalia inclusão |
| `OA-KPI-068` | Notificações repetidas sem mudança material | Mede fadiga provocada pelo sistema |
| `OA-KPI-069` | Ações reversíveis com desfazimento disponível | Avalia recuperabilidade |
| `OA-KPI-070` | Esforço médio para localizar custos, riscos e condições | Mede clareza operacional |

# 2686. Família 15 — Ausência, diversidade e equilíbrio do ecossistema

| KPI | Indicador | Avaliação |
|---|---|---|
| `OA-KPI-071` | Ausências legítimas preservadas sem anúncios substitutos | Mede integridade do estado vazio |
| `OA-KPI-072` | Cobertura de alternativas públicas, gratuitas e comunitárias | Avalia diversidade funcional |
| `OA-KPI-073` | Concentração de apresentações por fornecedor ou parceiro | Mede risco de dependência comercial |
| `OA-KPI-074` | Comparações com diversidade material de alternativas | Avalia amplitude real de escolha |
| `OA-KPI-075` | Oportunidades incompatíveis apresentadas para preencher volume | Mede pressão artificial do catálogo |

# 2687. Baseline funcional

Antes da definição de metas permanentes, a Guivos deverá construir uma baseline real.

A baseline deverá considerar:

- canal;
- categoria do participante;
- categoria e sensibilidade da oportunidade;
- origem e autoridade da fonte;
- estado funcional;
- estado da informação;
- disponibilidade;
- elegibilidade;
- relevância;
- relação comercial;
- relação individual do participante;
- modalidade e localização;
- janela temporal;
- integração;
- processo externo;
- volume operacional;
- maturidade do produto.

Metas não deverão ser copiadas de marketplaces, redes sociais, plataformas publicitárias, sistemas de recomendação comercial ou produtos de maximização de conversão.

# 2688. Painel de saúde da capacidade

O painel deverá possuir, no mínimo, visões de:

1. admissão e ativação;
2. fontes e autoridade;
3. disponibilidade;
4. elegibilidade;
5. relevância;
6. neutralidade comercial;
7. descoberta e apresentação;
8. controle do participante;
9. processos externos;
10. privacidade e sensibilidade;
11. integrações e revogação;
12. confiabilidade;
13. explicabilidade e auditoria;
14. acessibilidade, esforço e fadiga;
15. diversidade e equilíbrio;
16. guardrails.

O painel não deverá produzir pontuação de qualidade humana, consumo, sucesso, mérito, produtividade ou evolução do participante.

# 2689. Níveis de desempenho funcional

A capacidade poderá ser classificada como:

## Crítico

Existem violações de guardrail ou riscos materiais não controlados.

## Instável

A capacidade opera, mas apresenta falhas recorrentes, inconsistências, desatualização ou controle insuficiente.

## Adequado

Os contratos centrais funcionam e os riscos críticos estão controlados.

## Confiável

A capacidade apresenta consistência, explicabilidade, baixa incidência de falhas e controle efetivo.

## Maduro

A capacidade opera com baseline estável, integração segura, diversidade funcional e melhoria sistêmica contínua.

Nenhum nível superior poderá ser atribuído enquanto houver guardrail crítico violado.

# 2690. Guardrails de tolerância zero

A capacidade possuirá 24 guardrails obrigatórios:

1. ativação de oportunidade apenas por existência em catálogo, página, anúncio ou base externa;
2. fabricação de relevância por comissão, patrocínio, margem, estoque, clique, popularidade ou tempo de tela;
3. ocultação de alternativas públicas, gratuitas ou não patrocinadas;
4. apresentação de oportunidade indisponível como disponível;
5. inferência de interesse por busca, visualização, localização ou consumo de conteúdo;
6. utilização de contexto sensível para publicidade, precificação ou pressão comercial;
7. criação ou confirmação automática de Objetivo ou Próximo Passo;
8. apresentação de elegibilidade estimada como aprovação ou acesso garantido;
9. apresentação de disponibilidade como reserva, acesso ou benefício garantido;
10. tratamento de inscrição como aceitação;
11. tratamento de aceitação como contratação, participação ou resultado;
12. tratamento de compra, contratação ou participação como progresso ou evolução humana;
13. omissão de patrocínio, comissão, afiliação, exclusividade ou vantagem financeira;
14. ocultação de custo total, risco material ou condição relevante;
15. ampliação da autoridade de fornecedor, profissional, organização, produto ou integração;
16. acesso organizacional à jornada pessoal integral sem finalidade e autorização;
17. formação de perfil independente de terceiro;
18. revogação apresentada como concluída antes da propagação suficiente;
19. efeito material duplicado por reprocessamento;
20. sobrescrita silenciosa de conflito de versão ou fonte;
21. estado impossível produzido por evento fora de ordem;
22. falha parcial apresentada como sucesso integral;
23. uso de escassez, medo, culpa, vergonha, urgência fabricada ou padrão manipulativo;
24. preenchimento da ausência legítima com anúncios ou opções incompatíveis.

# 2691. Tratamento de violação de guardrail

Uma violação deverá produzir:

1. interrupção do fluxo afetado;
2. limitação de efeitos;
3. registro auditável;
4. classificação de severidade;
5. notificação interna;
6. comunicação ao participante quando necessária;
7. correção ou compensação;
8. recomposição de recortes;
9. bloqueio de novo processamento;
10. análise de causa;
11. validação da recuperação;
12. revisão do contrato ou da implementação.

A média dos demais indicadores não poderá neutralizar a violação.

# 2692. Cenários funcionalmente ideais

Os cenários ideais deverão demonstrar que a capacidade:

- admite meios legítimos;
- explica origem e autoridade;
- representa disponibilidade e elegibilidade com precisão proporcional;
- preserva neutralidade comercial;
- protege contexto sensível;
- permite comparação real;
- mantém o participante no controle;
- integra serviços sem transferir decisão;
- registra fatos externos sem ampliar significado.

# 2693. Cenário ideal — Oportunidade pública validada

Fluxo:

```text
programa público identificado
→ fonte oficial validada
→ requisitos e prazo extraídos
→ disponibilidade e elegibilidade avaliadas
→ relevância contextual explicada
→ oportunidade ativada
→ Intervenções Contextuais decide apresentar ou silenciar
→ participante consulta, salva ou descarta
```

Critérios:

- fonte oficial preservada;
- ausência de comissão;
- requisitos e prazos visíveis;
- elegibilidade distinta de aprovação;
- alternativas preservadas.

# 2694. Cenário ideal — Descoberta por contexto autorizado

Um recorte mínimo de Contexto Vivo poderá apoiar a descoberta quando:

- a finalidade estiver explícita;
- os campos utilizados forem necessários;
- a justificativa estiver disponível;
- o participante puder limitar ou revogar;
- o recorte não for reutilizado para publicidade.

# 2695. Cenário ideal — Oportunidade patrocinada

Uma oportunidade patrocinada poderá permanecer ativa quando:

- atingir o mesmo limiar funcional das demais;
- o patrocínio estiver visível;
- a relevância não depender do patrocínio;
- alternativas não patrocinadas permanecerem disponíveis;
- a ordenação funcional não for alterada.

# 2696. Cenário ideal — Vínculo consciente com Próximo Passo

Fluxo:

```text
Próximo Passo confirmado
→ função necessária identificada
→ oportunidades compatíveis avaliadas
→ alternativas comparadas
→ participante escolhe vincular uma opção
→ Próximos Passos registra o vínculo por contrato próprio
```

A oportunidade não deverá criar, priorizar, iniciar ou concluir o passo automaticamente.

# 2697. Cenário ideal — Oportunidade sensível

O cenário deverá utilizar:

- título neutro;
- finalidade específica;
- visualização minimizada;
- acesso restrito;
- notificações discretas;
- autoridade profissional quando necessária;
- compartilhamento limitado;
- revogação;
- ausência de publicidade baseada no contexto.

# 2698. Cenário ideal — Oportunidade institucional ou coletiva

O cenário deverá distinguir:

- oportunidade global;
- regras institucionais;
- disponibilidade coletiva;
- elegibilidade individual;
- relação individual;
- conteúdo público;
- conteúdo privado;
- responsabilidades próprias da organização.

Obrigação institucional não deverá ser apresentada como interesse pessoal.

# 2699. Cenário ideal — Disponibilidade atualizada

Uma fonte autorizada poderá informar alteração de vagas, estoque, agenda ou janela.

A capacidade deverá:

- versionar a mudança;
- preservar o estado anterior;
- reavaliar relevância e apresentação;
- notificar interessados quando material;
- impedir falsa garantia.

# 2700. Cenário ideal — Comparação comercial e não comercial

A comparação deverá incluir, quando aplicável:

- opção comercial;
- opção pública;
- opção gratuita;
- alternativa comunitária;
- custos totais;
- riscos;
- elegibilidade;
- disponibilidade;
- relação comercial.

Não deverá existir vencedor universal sem fundamento legítimo.

# 2701. Cenário ideal — Processo externo

Fluxo:

```text
participante declara interesse
→ requisitos e dados enviados são apresentados
→ participante confirma
→ inscrição, reserva ou contratação é iniciada no produto responsável
→ retorno externo atualiza fatos objetivos
→ Oportunidades Ativas preserva o recorte necessário
```

O processo externo não deverá redefinir a jornada.

# 2702. Cenário ideal — Resultado externo recebido

Entrega, atendimento, participação ou conclusão externa poderão ser registrados como fatos objetivos.

Esses fatos não deverão confirmar automaticamente:

- satisfação;
- aprendizado;
- progresso;
- transformação;
- conclusão de objetivo;
- Evento de Vida.

# 2703. Cenários alternativos

Cenários alternativos representam situações legítimas que não constituem falha da capacidade nem do participante.

# 2704. Nenhuma oportunidade compatível

O sistema deverá aceitar:

```text
Nenhuma oportunidade compatível foi identificada neste momento.
```

Não deverá:

- reduzir os critérios;
- preencher o espaço com anúncios;
- pressionar ampliação de permissões;
- criar necessidade artificial;
- interpretar ausência como falha.

# 2705. Informação insuficiente

A oportunidade poderá permanecer:

- candidata;
- em avaliação;
- ativa com condição limitada;
- não apresentada.

A incerteza deverá ser visível.

# 2706. Elegibilidade desconhecida

O sistema deverá apresentar:

- requisitos conhecidos;
- campos ausentes;
- autoridade decisória;
- necessidade de verificação;
- possibilidade de contestação.

Não deverá presumir aprovação ou rejeição.

# 2707. Abertura futura

A oportunidade poderá ser preservada quando:

- a previsão possuir fonte;
- a data ou condição estiver clara;
- não for apresentada como disponível agora;
- notificações forem controláveis;
- a validade for definida.

# 2708. Lista de espera

A lista de espera deverá permanecer distinta de:

- vaga disponível;
- reserva;
- aceitação;
- aprovação;
- acesso garantido.

# 2709. Custo não confirmado

A interface deverá indicar:

- valores conhecidos;
- custos possíveis;
- responsável pela cobrança;
- necessidade de confirmação;
- impacto sobre a comparação.

# 2710. Comparação incompleta

Quando dados essenciais estiverem ausentes, a comparação deverá:

- marcar campos desconhecidos;
- evitar pontuação definitiva;
- permitir consulta às fontes;
- preservar as diferenças conhecidas;
- impedir conclusão enganosa.

# 2711. Participante sem interesse

A ausência de interesse deverá:

- não gerar penalidade;
- não reduzir valor pessoal;
- não aumentar pressão;
- permitir descarte ou ocultação;
- limitar reapresentação.

# 2712. Categoria ocultada

A ocultação deverá ser respeitada no escopo escolhido.

A categoria somente poderá reaparecer quando:

- o participante solicitar;
- o período expirar;
- houver alteração material relevante;
- a regra de ocultação permitir revisão.

# 2713. Fonte desconectada

O sistema deverá:

- interromper novas coletas;
- preservar fatos históricos legítimos;
- indicar desatualização;
- reduzir automações;
- manter o último estado válido;
- informar efeitos materiais.

# 2714. Conflito entre fontes

A capacidade deverá:

- preservar versões;
- considerar autoridade e temporalidade;
- apresentar estado provisório;
- limitar automações;
- permitir contestação;
- evitar escolha comercial silenciosa.

# 2715. Oportunidade ativa ainda não apresentada

A oportunidade poderá permanecer ativa sem ser apresentada quando:

- o momento for inadequado;
- houver fadiga;
- a sensibilidade exigir silêncio;
- não existir necessidade de decisão;
- Intervenções Contextuais decidir aguardar.

# 2716. Oportunidade pausada ou indisponível

O estado deverá:

- preservar histórico;
- interromper novas apresentações incompatíveis;
- informar causa e possível retorno;
- oferecer alternativas quando apropriado;
- não representar encerramento automático.

# 2717. Cenários limite

Cenários limite deverão demonstrar o comportamento diante de risco elevado, incerteza, fraude, falha ou tentativa de ampliação indevida de autoridade.

# 2718. Identidade incerta

O sistema deverá:

- impedir associação automática;
- limitar efeitos pessoais;
- não apresentar;
- não compartilhar;
- solicitar confirmação proporcional;
- preservar o sinal como pendente.

# 2719. Associação incorreta

A capacidade deverá:

- interromper novos usos;
- recompor recortes;
- notificar consumidores;
- reavaliar oportunidades afetadas;
- preservar auditoria;
- eliminar ou anonimizar dados indevidos quando aplicável.

# 2720. Fonte excede autoridade

A afirmação deverá ser:

- rejeitada;
- reduzida ao fato legítimo;
- marcada como interpretação externa;
- impedida de confirmar estado material;
- auditada.

# 2721. Relação comercial ocultada

A identificação deverá produzir:

- pausa ou bloqueio da apresentação;
- registro de incidente;
- reavaliação de neutralidade;
- preservação de evidências;
- correção da transparência;
- revisão de oportunidades afetadas.

# 2722. Exploração de vulnerabilidade

A capacidade deverá bloquear:

- segmentação comercial sensível;
- urgência baseada em medo;
- aumento de preço por vulnerabilidade;
- publicidade derivada de Evento de Vida sensível;
- pressão baseada em saúde, renda, fé, violência ou dependência.

# 2723. Escassez comercial usada como urgência pessoal

O sistema deverá distinguir:

- quantidade confirmada;
- estimativa;
- janela real;
- alta procura;
- mensagem promocional;
- urgência funcional do participante.

Escassez comercial não deverá produzir prioridade pessoal automática.

# 2724. Alternativa gratuita suprimida

A supressão deverá ser tratada como violação crítica de neutralidade.

O sistema deverá:

- restaurar a alternativa;
- revisar a ordenação;
- identificar a causa;
- impedir recorrência;
- auditar impacto.

# 2725. Indisponibilidade apresentada como disponibilidade

A capacidade deverá:

- interromper novas ações;
- corrigir o estado;
- notificar afetados quando necessário;
- oferecer alternativas;
- preservar a origem da informação incorreta;
- reavaliar a fonte.

# 2726. Elegibilidade inferida sem fundamento

A avaliação deverá ser reduzida a `não avaliada`, `informação insuficiente` ou `exige verificação`.

Nenhuma ação material deverá depender da inferência indevida.

# 2727. Interesse inferido por comportamento

Busca, visualização, localização, clique, tempo de tela ou consumo de conteúdo não poderão produzir:

- interesse declarado;
- contato com fornecedor;
- inscrição;
- prioridade;
- publicidade sensível.

# 2728. Transação interpretada como evolução

Compra, contratação, reserva, pagamento ou participação deverão permanecer fatos externos.

A capacidade não deverá atribuir:

- progresso;
- transformação;
- sucesso;
- mérito;
- conclusão de objetivo.

# 2729. Ciclo automático entre oportunidade e Próximo Passo

A capacidade deverá impedir:

```text
oportunidade ativa
→ passo sugerido
→ oportunidade priorizada porque existe o passo
→ prioridade do passo aumentada pela oportunidade
→ nova sugestão automática
```

Cada capacidade deverá governar sua própria decisão.

# 2730. Revogação pendente

Enquanto a propagação não for concluída:

- o estado deverá permanecer pendente;
- novos usos deverão ser bloqueados;
- consumidores deverão ser identificados;
- falhas deverão ser visíveis;
- sucesso integral não deverá ser declarado.

# 2731. Duplicidade, evento fora de ordem ou falha parcial

O sistema deverá:

- verificar idempotência;
- preservar versões;
- impedir transição impossível;
- registrar efeitos aplicados e pendentes;
- permitir recuperação;
- informar risco de duplicidade;
- reconstruir o estado.

# 2732. Critérios de conclusão funcional

A Capacidade 06 será considerada funcionalmente concluída quando:

1. possuir fundamentos normativos;
2. possuir ciclo de vida completo;
3. possuir visualização e controle;
4. possuir contratos de eventos;
5. possuir integrações funcionais;
6. distinguir candidatura, avaliação, ativação e apresentação;
7. distinguir disponibilidade, elegibilidade e relevância;
8. separar estado da oportunidade e relação do participante;
9. separar situação transacional externa da jornada;
10. preservar titularidade, papéis e autoridade;
11. limitar a autoridade das fontes;
12. preservar neutralidade comercial;
13. separar publicidade da lista funcional;
14. preservar alternativas não patrocinadas;
15. suportar ausência legítima de oportunidades;
16. proteger oportunidades sensíveis;
17. proteger informações de terceiros;
18. permitir contestação e correção;
19. governar pausa, indisponibilidade, expiração, encerramento e cancelamento;
20. governar revogação e propagação;
21. operar com idempotência, ordenação e concorrência;
22. definir falha segura;
23. preservar explicabilidade e auditoria;
24. possuir indicadores e baseline;
25. possuir guardrails de tolerância zero;
26. possuir cenários ideal, alternativo e limite;
27. manter o participante no controle;
28. não possuir lacuna funcional bloqueante conhecida.

# 2733. Lacunas não bloqueantes

Não impedem a conclusão funcional:

- definição de metas numéricas após baseline;
- implementação técnica;
- desenho visual definitivo;
- schemas físicos;
- APIs;
- estruturas de banco;
- modelos finais de autorização;
- infraestrutura de eventos;
- dashboards operacionais;
- testes automatizados;
- modelos definitivos de busca e ordenação;
- integrações com fornecedores específicos;
- políticas regulatórias por país;
- contratos comerciais específicos;
- observabilidade operacional definitiva;
- documentação de suporte.

Esses itens pertencem às fases de design, engenharia, segurança, dados, operação e validação.

# 2734. Lacunas bloqueantes

Seriam bloqueantes:

- ausência de titularidade;
- ausência de autoridade;
- impossibilidade de distinguir oportunidade, oferta e anúncio;
- impossibilidade de distinguir disponibilidade, elegibilidade e relevância;
- ausência de controle do participante;
- interesse inferido automaticamente;
- omissão de relações comerciais;
- interferência de receita sobre relevância;
- ocultação de alternativas não patrocinadas;
- exploração comercial de vulnerabilidade;
- ausência de proteção sensível;
- ausência de revogação;
- inexistência de contestação ou correção;
- duplicidade material não controlada;
- ausência de falha segura;
- transferência de decisão às integrações;
- utilização de transações como medida de evolução.

Nenhuma lacuna funcional bloqueante é conhecida na baseline normativa proposta.

# 2735. Finalidade do contrato final

O contrato final governa como a Guivos identifica, valida, organiza e apresenta meios disponíveis que podem apoiar a jornada atual do participante.

A capacidade deverá apoiar descoberta e decisão sem converter a jornada em:

- catálogo infinito;
- feed publicitário;
- mecanismo de pressão comercial;
- sistema de vigilância;
- ranking de consumo;
- comparação de mérito;
- avaliação de sucesso humano.

# 2736. Singularidade funcional

A singularidade da Capacidade de Oportunidades Ativas é governar a relevância atual de meios disponíveis, legítimos e potencialmente compatíveis para uma jornada específica.

Ela não governa:

- direção existencial;
- definição de objetivo;
- decisão de movimento;
- momento de interrupção;
- transação;
- entrega;
- experiência vivida;
- evolução humana.

# 2737. Titularidade

Toda avaliação pessoal de oportunidade deverá possuir participante titular identificável.

A titularidade não deverá ser transferida por:

- fornecedor;
- patrocinador;
- organização;
- profissional;
- produto especializado;
- integração;
- recomendação;
- execução externa;
- autoridade técnica.

# 2738. Responsabilidades

A capacidade será responsável por:

- identificar candidatos;
- validar fontes;
- limitar autoridade;
- avaliar completude;
- representar disponibilidade;
- representar elegibilidade;
- avaliar relevância;
- registrar riscos e sensibilidade;
- declarar relações comerciais;
- governar ativação;
- produzir recortes para apresentação;
- apoiar busca e comparação;
- registrar relações do participante;
- vincular oportunidades a Próximos Passos de forma controlada;
- acompanhar fatos externos necessários;
- permitir contestação e correção;
- produzir eventos;
- integrar consumidores;
- governar revogação;
- preservar histórico.

# 2739. Limites

A capacidade não será responsável por:

- definir Objetivos;
- criar compromissos pessoais;
- decidir pelo participante;
- governar o momento da intervenção;
- operar publicidade;
- concluir transações;
- prestar serviços;
- garantir disponibilidade;
- garantir elegibilidade;
- garantir aprovação;
- garantir benefício;
- confirmar experiência;
- medir evolução humana;
- diagnosticar;
- substituir profissionais;
- atribuir fé, mérito, disciplina, sucesso ou valor moral.

# 2740. Entradas

A capacidade poderá receber:

- contexto autorizado;
- necessidades;
- preferências;
- restrições;
- Objetivos;
- Eventos de Vida;
- Próximos Passos;
- pesquisas;
- catálogos;
- programas;
- produtos;
- serviços;
- benefícios;
- vagas;
- eventos;
- fontes públicas;
- informações institucionais;
- sinais externos;
- relações comerciais;
- contestações;
- correções;
- autorizações.

# 2741. Admissão

Uma entrada somente deverá produzir oportunidade candidata quando houver:

- identidade mínima;
- fonte identificável;
- finalidade legítima;
- autoridade suficiente para os fatos declarados;
- participante ou público possível;
- temporalidade compreensível;
- ausência de proibição imediata;
- proteção proporcional à sensibilidade.

A candidatura não representa ativação.

# 2742. Saídas

A capacidade poderá produzir:

- oportunidades candidatas;
- oportunidades ativas;
- justificativas de relevância;
- avaliações de disponibilidade;
- avaliações de elegibilidade;
- alertas de risco;
- declarações comerciais;
- comparações;
- alternativas;
- recortes para Intervenções Contextuais;
- vínculos propostos com Próximos Passos;
- solicitações de reavaliação;
- eventos funcionais;
- notificações controladas;
- histórico;
- correções;
- propagações de revogação.

# 2743. Estados e dimensões

O contrato final preserva separadamente:

1. estado funcional da oportunidade;
2. estado da informação;
3. disponibilidade;
4. elegibilidade;
5. relevância;
6. risco;
7. sensibilidade;
8. relação comercial;
9. relação individual do participante;
10. decisão de apresentação;
11. vínculo com Próximo Passo;
12. situação transacional externa.

Nenhuma dimensão deverá substituir automaticamente as demais.

# 2744. Relações com outras capacidades

A capacidade deverá:

- receber recortes mínimos de Contexto Vivo;
- utilizar Objetivos como direção, sem governá-los;
- reavaliar oportunidades após Eventos de Vida;
- apoiar Próximos Passos como meio, alternativa ou recurso;
- solicitar a Intervenções Contextuais decisão de apresentar, aguardar ou silenciar;
- encaminhar participação efetiva a Experiências;
- impedir que volume, compra ou participação sejam utilizados diretamente por Evolução Contínua.

Cada capacidade consumidora deverá governar sua própria decisão.

# 2745. Neutralidade comercial

A capacidade deverá preservar:

- comissão como metadado de transparência;
- patrocínio sem aumento de relevância;
- publicidade separada da lista funcional;
- alternativas públicas, gratuitas e não patrocinadas;
- ordenação sem margem, clique, estoque ou investimento publicitário;
- ausência legítima sem preenchimento comercial.

# 2746. Privacidade e sensibilidade

A capacidade deverá aplicar:

- minimização;
- finalidade específica;
- títulos neutros;
- notificações discretas;
- acesso proporcional;
- busca sensível protegida;
- retenção limitada;
- proteção de terceiros;
- ausência de publicidade derivada de contexto sensível;
- revogação e propagação.

# 2747. Confiabilidade

A capacidade deverá operar com:

- contratos versionados;
- persistência antes de publicação;
- idempotência;
- ordenação;
- concorrência segura;
- correção compensatória;
- prevenção de ciclos;
- sincronização reconciliável;
- último estado válido;
- degradação controlada;
- falha segura;
- reconstrução.

# 2748. Explicabilidade e auditoria

O participante deverá poder compreender:

- por que uma oportunidade foi apresentada;
- quais dados foram utilizados;
- qual fonte foi consultada;
- qual autoridade existia;
- quais incertezas permanecem;
- quais relações comerciais existem;
- quais consumidores receberam recortes;
- quais efeitos foram produzidos;
- como contestar;
- como revogar.

A auditoria deverá reconstruir a cadeia desde a fonte até o processamento, a apresentação, a interação, a correção ou a revogação.

# 2749. Critérios de reabertura normativa

A capacidade poderá ser reaberta quando houver:

- nova responsabilidade funcional;
- mudança incompatível de contrato;
- novo risco material;
- alteração regulatória com efeito arquitetural;
- evidência de lacuna bloqueante;
- nova categoria de participante;
- nova integração estrutural;
- conflito com outra capacidade concluída;
- necessidade de major version.

Implementação técnica, refinamento visual ou definição de metas posteriores à baseline não exigem reabertura normativa por si mesmos.

# 2750. Regras fundamentais finais

1. Existência não representa relevância.
2. Catálogo não representa Oportunidade Ativa.
3. Candidatura não representa ativação.
4. Ativação não representa apresentação.
5. Apresentação não representa visualização.
6. Visualização não representa interesse.
7. Interesse não representa compromisso.
8. Inscrição não representa aceitação.
9. Aceitação não representa contratação.
10. Contratação não representa participação.
11. Participação não representa resultado.
12. Resultado não representa evolução.
13. Disponibilidade não representa elegibilidade.
14. Elegibilidade não representa aprovação.
15. Relevância não representa obrigação.
16. Fonte somente confirma fatos dentro de sua autoridade.
17. Comissão não altera relevância.
18. Patrocínio não altera prioridade.
19. Publicidade permanece separada.
20. Alternativas não patrocinadas permanecem elegíveis.
21. Custos, riscos e condições materiais permanecem visíveis.
22. Contexto sensível não alimenta publicidade.
23. Escassez comercial não fabrica urgência pessoal.
24. Ausência de oportunidade é estado legítimo.
25. Organizações não recebem a jornada pessoal integral.
26. Dados de terceiros não formam perfis paralelos.
27. Integrações não transferem decisão.
28. Produtos especializados governam transações e entregas.
29. Intervenções Contextuais governa o momento da apresentação.
30. Próximos Passos governa movimentos.
31. Objetivos governa direção e progresso.
32. Experiências governa o vivido.
33. Evolução Contínua governa mudança humana.
34. Revogação interrompe novos usos.
35. Revogação somente termina após propagação suficiente.
36. Reprocessamento não duplica efeitos.
37. Eventos fora de ordem não criam estados impossíveis.
38. Conflitos não são resolvidos silenciosamente.
39. Correção não reescreve histórico.
40. Falha parcial não representa sucesso integral.
41. Métricas avaliam o sistema.
42. O participante permanece no controle.

# 2751. Continuidade normativa

`PAS-001-OA-CONTRACT-001 1.0.0` é registrado como a **sexta extensão normativa e o contrato final da Capacidade 06 — Oportunidades Ativas**.

A extensão:

- preserva fundamentos, ciclo de vida, visualização, eventos e integrações;
- preserva o `PAS-001 0.5.0`;
- preserva as Capacidades 02, 03, 04 e 05 como `Functionally complete`;
- substitui o estado da Capacidade 06 por `Functionally complete`;
- eleva o progresso editorial de referência de `90%` para `100%`;
- consolida 75 KPIs em 15 famílias;
- consolida 24 guardrails de tolerância zero;
- define baseline, painel de saúde e níveis de desempenho;
- consolida cenários funcionalmente ideais, alternativos e limite;
- define critérios de conclusão, lacunas e reabertura;
- preserva neutralidade comercial, privacidade, confiabilidade, explicabilidade e controle;
- não identifica lacuna funcional bloqueante na baseline normativa;
- define a Capacidade 07 — Intervenções Contextuais como próxima frente oficial.

A Capacidade 07 deverá permanecer `Planned / concept consolidated` até a aprovação de sua primeira extensão normativa.

O próximo bloco será:

> **Fundamentos iniciais da Capacidade 07 — Intervenções Contextuais, incluindo singularidade, decisão entre agir, perguntar, lembrar, aguardar, observar ou silenciar, autoridade, oportunidade de intervenção, atenção, urgência, sensibilidade, fadiga, canais, autonomia, limites e relação com as demais capacidades do Journey.**
