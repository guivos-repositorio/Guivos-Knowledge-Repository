---
title: Grafo Vivo — Verificação do Destinatário e Canal de Submissão AF-10
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: routing_verification_inconclusive
---

# Grafo Vivo — Verificação do Destinatário e Canal de Submissão AF-10

> **Verificação de roteamento inconclusiva, não submissão.** Não contém parecer emitido pela Arquitetura da Experiência, despacho da direção, ato de delegação ou autorização de implementação. Nenhuma alternativa A/B/C de localização funcional foi escolhida.

## 1. Pergunta examinada

É possível identificar, **a partir de fonte verificável do repositório**, (i) a instância com competência para receber e decidir AF-10 e (ii) um canal institucional cuja utilização corresponda a submissão formal, para posterior consulta AF-01/02/03 sobre o Grafo Vivo?

A minuta de referência é [Minuta de Encaminhamento Institucional AF-10](minuta-encaminhamento-institucional-af10.md).

## 2. Verificações realizadas

| Fonte examinada | Achado verificável | Limite do achado |
| --- | --- | --- |
| `GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001` v0.4.0 | `owner: Arquitetura da Experiência da Guivos`, governança de continuidade entre responsabilidades e fonte normativa transversal | O campo `owner` não indica pessoa/órgão com delegação nominativa para adjudicação |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` v0.36.22 | Mesma área de ownership; define responsabilidades e maturidade das superfícies | Não prova que o titular do arquivo possa instituir novo PER-ID sem ato |
| `GKR-JOURNEY-TRANSITION-REGISTRY-001` v0.29.26 | Mesma área de ownership; registra transições e limites | Não identifica canal formal de consulta ou instrumento de aprovação |
| `GKR-UX-PERSON-JOURNEY-READ-FIRST-001` v0.2.0 | Orienta a leitura a partir da Journey, Registries, autoridades específicas e Masters; diferencia Design e Engenharia | Roteamento de leitura não equivale a roteamento de decisão |
| `ADR-001` | GKR é registro oficial do conhecimento aprovado | GitHub e sua rastreabilidade não significam que abrir arquivo/PR seja consulta institucional |
| `ADR-006` | GKA governa o conhecimento; não substitui arquitetura, cria produtos ou decide implantação | Não é o órgão adjudicador por inferência |
| `A2-METHOD-001` v2.0.0 | Hipóteses não passam à Canon sem validação/consolidação; método não substitui engenharia/privacidade | Não nomeia a instância decisória específica de AF-10 |
| `GEA-AUDIT-001` v2.0.0 | Auditoria verifica integridade, não cria verdade por inferência | PASS documental não substitui aprovação funcional |
| `.github/CODEOWNERS` na branch | Não localizado no caminho convencional consultado | Ausência desse arquivo não prova ausência de outro regime de aprovação |
| `.github/PULL_REQUEST_TEMPLATE.md`, `CONTRIBUTING.md` | Não localizados nos caminhos consultados | Não comprova inexistência de procedimento fora do repositório |
| Busca de código por termos de competência/autorização | Não produziu referência suficientemente específica para uma cadeia formal de delegação | Busca negativa é limitada pela indexação e não estabelece fato absoluto |

**Achado focal:** há fonte documental para **endereçamento temático preliminar** à Arquitetura da Experiência, mas não há prova suficiente para definir **destinatário institucional habilitado, canal de submissão e eficácia de uma decisão**. A validade da consulta continua condicionada à confirmação pelo responsável competente da governança.

## 3. Resultado por componente do roteamento

| Dimensão | Estado | Consequência |
| --- | --- | --- |
| Área técnica para análise de UX/Journey | **Identificada**: Arquitetura da Experiência da Guivos | Pode orientar a busca do destinatário |
| Instância ou pessoa autorizada a receber submissão AF-10 | **Não confirmada** | Não endereçar formalmente por suposição |
| Poder decisório sobre PER-008 e Surface/Transition Registries em conjunto | **Não comprovado** | Não adjudicar A/B/C por conta própria |
| Canal institucional de consulta | **Não confirmado** | Não chamar PR, comentário ou mensagem de submissão formal |
| Instrumento com eficácia para alterar contratos/registries | **Não confirmado** | Não criar ato normativo candidato como se fosse vigente |
| Minuta AF-10 e anexos documentais | **Preparados** | Aptos somente a revisão e encaminhamento após validação |
| Resposta formal da instância competente | **Não recebida** | AF-01/02/03/10 continuam abertos |

## 4. Critério para destravar o encaminhamento

A informação mínima a obter por ato legítimo da direção ou governança é:

1. **Destinatário:** instância/pessoa responsável e sua competência para receber a consulta;
2. **Canal:** mecanismo no qual um envio seria efetivamente recebido e reconhecido;
3. **Instrumento:** tipo de resposta que poderia decidir ou remeter a decisão;
4. **Alcance:** quais partes de PER-008, Surface Registry e Transition Registry a instância pode analisar, recomendar ou alterar;
5. **Evidência:** referência documental/decisão que sustenta a delegação.

**Somente após essas confirmações:** encaminhar a minuta AF-10 efetivamente pelo canal reconhecido, registrar envio/protocolo e aguardar resposta. **Não registrar como submetido enquanto não houver evento de envio comprovado.**

## 5. Relação com a implantação na Jornada da Pessoa

A intenção da direção de implantar o Grafo Vivo na dashboard `https://replit.com/@guivos/Jornada-da-Pessoa` permanece **condicionada à suficiência de materiais e autorizações necessárias**.

O atual workspace, seu código e suas integrações **não foram inspecionados nesta etapa**. A tela “Composição da Pessoa” fornecida pela direção permanece baseline visual de planejamento, não prova de readiness.

AF-10 não aprova por si mesmo persistência contínua, Grok/voz, Neo4j, APIs, Design, auditoria do Replit, testes ou implantação.

## 6. Pendência editorial separada

O comentário de navegação do `mkdocs.yml` restringe a promoção de documentos `draft/proposed` ao MENU sem autoridade superior que os declare fonte operacional. O PR de estudo contém itens de navegação para `conceptual_study`. A pendência deve ser saneada **antes de qualquer merge/publicação** por via editorial competente, mantendo o índice e a rastreabilidade em Git. Este exame **não modifica o menu**.

## 7. Parecer final e próximo ato

**Resultado:** roteamento **não verificável de modo suficiente** nas fontes consultadas. A Arquitetura da Experiência da Guivos é a área técnica indicada, mas **não se comprovou destinatário nominal, canal ou instrumento decisório com eficácia específica**.

**Próxima ação útil:** obter da direção ou da governança uma indicação **expressa e rastreável** de destinatário, canal e instrumento para AF-10. Não produzir outros dossiês sobre o mesmo vazio como substituto dessa decisão. Com essa indicação, a minuta existente está pronta para a revisão final e o envio permitido.

**Estado:** PR documental em rascunho, consulta não submetida, sem novas decisões normativas ou operacionais.


## Atualização posterior de status — decisão da Direção em 08/11/2026

A Direção **aprovou expressamente** sua atribuição como **instância de decisão final para o Grafo Vivo**, mediante consultas técnicas às autoridades pertinentes, e o **GKR/GitHub como meio de registro**. Ver [Registro de Decisão AF-10](decisao-direcao-competencia-af10.md). As constatações anteriores deste documento retratam o **estado antes dessa decisão** e não devem ser utilizadas para afirmar que a instância decisória final continua indefinida. **Não houve ainda parecer técnico de UX/Journey, seleção A/B/C, consulta formal comprovada ou autorização operacional.** O instrumento para modificações especializadas de Masters/Registries ainda exige ato próprio.
