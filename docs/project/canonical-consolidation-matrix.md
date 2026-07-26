---
id: GKR-CANON-MATRIX-001
title: Matriz de Consolidação Canônica
status: active
version: 2.5.0
owner: Guivos
last_updated: 2026-07-26
depends_on:
  - GKR-STATE-001
related:
  - GKR-CANON-MATRIX-UXA-010
  - GKR-CANON-MATRIX-UXA-009
  - GKR-CANON-MATRIX-UXA-005
  - GKR-CANON-MATRIX-UXA-001
  - GKR-CANON-MATRIX-COD-017
  - GKR-R6-RESUMPTION-001
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - UXA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
  - UXA-010
  - M7.19.4
normative: false
---

# Matriz de Consolidação Canônica

## 1. Finalidade

Esta matriz registra decisões consolidadas de maior alcance e aponta para autoridades e documentos complementares que preservam o detalhamento.

## 2. Vocabulário de decisão

| Decisão | Significado |
|---|---|
| Manter | elemento permanece válido sem alteração estrutural |
| Refinar | elemento permanece, com precisão adicional |
| Unificar | elementos redundantes são consolidados sob uma autoridade |
| Remover do catálogo | candidato não integra o catálogo futuro, mas permanece rastreável |
| Pausar | trabalho permanece válido, sem execução adicional até nova autorização |
| Descoberta (`Discovery`) | hipótese e arquitetura inicial em desenvolvimento, sem implementação |
| Wireframe | hipótese visual estrutural para validação, sem design final ou implementação |
| Somente histórico (`Historical only`) | elemento permanece como evidência histórica |
| Pendente | depende de evidência ou autoridade competente |

## 3. Decisões estruturais vigentes

| Elemento em linguagem clara | Decisão | Referência técnica e situação |
|---|---|---|
| Repositório de Conhecimento da Guivos como fonte oficial | Manter | ADR-001 e governança vigente |
| Arquitetura de Fundação | Manter congelada | baseline A2-B3 |
| Guivos Journey | Manter | PAS-001 1.0.0 ativo; nove capacidades concluídas |
| Engenharia de Produto | Manter pausada | antes de W0-01; execução 0% |
| Modelo Econômico da Guivos | Manter documentariamente concluído | GEM-001 a GEM-010; validação real pendente |
| Remediação do repositório | Manter concluída | R1–R6 concluídos |
| Revisão da Arquitetura de Negócios | Manter ativa e pausar operacionalmente | após COD-017 e antes de BUS-CAND-010 |
| Resultados Empresariais | Manter ativos e pausados | 17 de 18 decisões; nenhuma submissão aberta |
| Validação externa e matriz de avaliação | Manter concluídas | 18 de 18 candidatos e 6 de 6 grupos avaliados |
| Decisões humanas 1 a 17 | Manter | COD-001 a COD-017 preservados |
| Registro de Decisões sobre Candidatos a Resultados | Manter ativo | CODR 0.33.0; 17 de 18 decisões |
| Registro de Candidatos a Resultados | Refinar | COR 0.29.0; 10 em validação, 2 incorporados e 6 rejeitados |
| Capacidade de reinvestimento responsável | Manter pendente | BUS-CAND-010 em validação; decisão não antecipada |
| Décima oitava submissão | Pendente | BA-STR-002-COD-SUB-018 não criado |
| Décima oitava decisão | Pendente | COD-018 não criado |
| Arquitetura da Experiência da Guivos | Descoberta | UXA-000 a UXA-004 integrados |
| Programa Inicial de Wireframes de Baixa Fidelidade | Wireframe | UXA-005 criado; método e critérios registrados |
| Tela Hoje | Refinar em wireframe | UXA-006 0.3.0; primeira validação funcional aplicada por UXA-010 |
| Detalhe de oportunidade | Wireframe | UXA-007; validação funcional pendente |
| Cadastro de oportunidade pela Organização | Wireframe | UXA-008; validação funcional pendente |
| Padrão de Linguagem Clara e Identificadores Técnicos | Refinar | UXA-009; nome completo antes do código e estados traduzidos |
| Validação Funcional e Reformulação da Tela Hoje | Manter | UXA-010; decisão humana e consequências registradas |
| Síntese do momento | Refinar | bloco condicional; omitido quando repetir um único item ou não acrescentar compreensão |
| Atenção principal | Manter | no máximo um item destacado; itens adicionais na Central de Intervenções |
| Contexto de atuação | Refinar | seletor explícito com `Agindo como` |
| Oportunidades na Tela Hoje | Refinar em wireframe | até dois cartões empilhados e em largura integral; nenhum preenchimento artificial |
| Coletivos e atividades na Tela Hoje | Refinar em wireframe | bloco somente com utilidade temporal |
| Navegação pessoal | Manter em descoberta | Hoje, Jornada, Explorar, Mapa e Eu |
| Validade do preço | Refinar | período até o qual o valor permanece vigente para novas adesões |
| Experiência da Organização | Descoberta | visão geral, oportunidades, programas, coletivos, resultados e gestão |
| Experiência do Coletivo | Descoberta | início, atividades, pessoas, mapa, recursos e gestão |
| Controle de relevância | Refinar em descoberta | explícito, explicável, ajustável e contestável |
| Fluxo de oportunidades | Refinar em descoberta | cadastro, avaliação, ativação, apresentação e encerramento separados |
| Preços e condições | Refinar em wireframe | preço principal, custo total, taxas, validade, cancelamento e relação comercial visíveis |
| Mapa | Descoberta | oportunidades, Organizações, Coletivos e atividades; localização de participantes bloqueada |
| Protótipo navegável | Pendente | não iniciado |
| Design visual | Pendente | não iniciado |
| Testes de usabilidade | Pendente | não iniciados |
| Resultados canônicos | Pendente | nenhum código ou catálogo canônico |
| Capacidades Empresariais | Pendente | posteriores aos Resultados Empresariais |
| Produtos especializados | Preservar para replanejamento | ordem histórica não autoriza início |
| Modelo Comercial e Entrada no Mercado | Pendente | posteriores às dependências arquiteturais |
| Validação de Mercado | Manter em paralelo | execução própria ainda pendente |
| Validador mecânico | Manter | workflow permanente do repositório |

## 4. Decisões sobre candidatos preservadas

| Candidato | Nome ou natureza | Decisão vigente |
|---|---|---|
| ECO-CAND-001 | candidato de resultado do ecossistema | Reformular aceito; nova avaliação pendente |
| ECO-CAND-002 | candidato de resultado do ecossistema | Reformular aceito; nova avaliação pendente |
| ECO-CAND-003 | candidato combinado do ecossistema | formulação combinada pendente de nova avaliação |
| ECO-CAND-004 | experiência como resultado | Rejeitado; conteúdo preservado na Jornada |
| ECO-CAND-005 | candidato incorporado | Incorporado em ECO-CAND-003 |
| ECO-CAND-006 | saúde relacional | Reformular aceito; nova avaliação pendente |
| ECO-CAND-007 | participação inclusiva, digna e efetiva | Reformular aceito; nova avaliação pendente |
| ECO-CAND-008 | participação protegida, justa e contestável | Reformular aceito; nova avaliação pendente |
| BUS-CAND-001 | autoridade constitucional | Rejeitado como Resultado Empresarial; obrigação de governança preservada |
| BUS-CAND-002 | candidato empresarial incorporado | Incorporado em BUS-CAND-003 |
| BUS-CAND-003 | valor sustentável | Reformular aceito; nova avaliação pendente |
| BUS-CAND-004 | legitimidade institucional sustentada | Reformular aceito |
| BUS-CAND-005 | continuidade econômica sustentável | Reformular aceito |
| BUS-CAND-006 | crescimento responsável e resiliente | Rejeitado como Resultado permanente; expansão responsável preservada |
| BUS-CAND-007 | aprendizado e adaptação institucionais | Rejeitado como Resultado permanente; capacidades preservadas |
| BUS-CAND-008 | saúde das relações de parceria | Rejeitado como Resultado permanente; governança de parceiros preservada |
| BUS-CAND-009 | coerência global com adequação contextual | Rejeitado como Resultado permanente; princípio arquitetural preservado |
| BUS-CAND-010 | capacidade de reinvestimento responsável | Em validação; decisão pendente |

## 5. Resultado da reformulação da Tela Hoje

A decisão consolidada:

- mantém a Tela Hoje como porta de entrada orientada por utilidade material;
- torna a síntese do momento condicional;
- preserva um único item principal;
- direciona itens críticos adicionais à Central de Intervenções;
- mantém o movimento atual antes das oportunidades;
- substitui cartões lado a lado por cartões empilhados em largura integral;
- condiciona Coletivos e atividades à utilidade temporal;
- preserva a navegação pessoal consolidada;
- não inicia protótipo, design visual, testes ou Engenharia de Produto.

## 6. Documento complementar vigente

O documento complementar vigente é `Matriz de Consolidação Canônica — Adendo da Reformulação Funcional da Tela Hoje`.

## 7. Próximo ato

Escolher entre validar funcionalmente o Detalhe de Oportunidade, validar funcionalmente o Cadastro pela Organização ou criar um estado alternativo selecionado da Tela Hoje.