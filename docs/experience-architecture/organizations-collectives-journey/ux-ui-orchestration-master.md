---
id: GKR-UX-ORGCOL-JOURNEY-ORCHESTRATION-001
title: Jornada de Organizações e Coletivos — Documento Mestre de Orquestração UX/UI
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: true
maturity: ux_orchestration_authority_candidate
depends_on:
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-DOCUMENTARY-COMPLETENESS-001
---

# Jornada de Organizações e Coletivos — Documento Mestre de Orquestração UX/UI

## 1. Finalidade

Este documento governa a **orquestração ponta a ponta da Jornada de Organizações e Coletivos** para orientar Design, IA de apoio, Produto, UX, prototipação e futura implementação.

Os Documentos Mestres por superfície governam responsabilidades locais. Esta autoridade candidata governa **como essas responsabilidades funcionam em conjunto**, preservando participante ativo, contexto, representação, autoridade, estados, transições, bilateralidade, proteção, evidências, planos e continuidade.

Ela não cria nova superfície ou transição e não substitui Surface Registry, Transition Registry, State Map, Priority Flows, Masters ou autoridades comerciais específicas.

```text
MASTER DE SUPERFÍCIE
→ RESPONSABILIDADE LOCAL

ORQUESTRAÇÃO
→ CONTEXTO + AUTORIDADE + ESTADO + CONTINUIDADE
→ HANDOFFS + RETORNOS + BILATERALIDADE
→ COMPORTAMENTO TRANSVERSAL

PROTÓTIPO UX/UI
→ MATERIALIZA AS REGRAS
→ NÃO CRIA VERDADE DE PRODUTO
```

## 2. Princípio de experiência

Organização e Coletivo devem ser percebidos como experiências coerentes e contínuas, não como coleções de telas independentes.

Em qualquer momento material, a experiência deve tornar compreensível:

1. quem está atuando;
2. em nome de qual participante;
3. qual contexto ou unidade está ativo;
4. qual papel e autoridade se aplicam;
5. qual objeto ou responsabilidade está em foco;
6. qual estado é real;
7. o que pode ser feito agora;
8. o que depende de outra pessoa, contraparte ou aprovação;
9. o que mudou após uma ação;
10. como retornar, interromper, revisar, contestar ou continuar.

```text
VISÍVEL
≠ AUTORIZADO

PERTENCER
≠ REPRESENTAR
≠ APROVAR
≠ ADMINISTRAR

NAVEGAR
≠ CONFIRMAR

CONTEXTO SEMELHANTE
≠ AUTORIDADE TRANSPORTÁVEL
```

## 3. Modelo de orquestração

A espinha transversal é:

```text
PESSOA AUTENTICADA
→ PARTICIPANTE REPRESENTADO
→ CONTEXTO / UNIDADE
→ PAPEL
→ AUTORIDADE
→ MOMENTO
→ OBJETO / RESPONSABILIDADE
→ PRÓXIMO PASSO LEGÍTIMO
→ AÇÃO OU DECISÃO
→ PROCESSAMENTO / HANDOFF QUANDO NECESSÁRIO
→ ESTADO CONFIRMADO
→ CONTINUIDADE COERENTE
```

A Pessoa permanece agente humano. Organização e Coletivo permanecem contextos de atuação com governança própria.

## 4. Contexto ativo e troca de contexto

Toda ação material deve ocorrer em contexto identificável.

A troca entre Organização, Coletivo, unidade ou papel deve revalidar autoridade e dados aplicáveis. Não transportar silenciosamente:

- permissões;
- seleção pendente;
- informação protegida;
- decisão em processamento;
- objeto pertencente a outro contexto;
- representação;
- aprovação;
- filtros que alterem significado material.

A troca de contexto não precisa impor uma solução visual específica. Design pode escolher seletor, navegação, menu ou outro padrão compatível.

## 5. Organização — continuidade principal

A experiência da Organização deve preservar a continuidade entre:

```text
ORG-001 — VISÃO GERAL
→ OPORTUNIDADES / PROGRAMAS
→ MANIFESTAÇÕES E INSCRIÇÕES
→ RELAÇÕES ORGANIZAÇÃO–COLETIVO
→ RESPONSABILIDADES E EVIDÊNCIAS
→ PLANOS / CAPACIDADES CONTEXTUAIS QUANDO APLICÁVEL
```

A Visão Geral sintetiza Momento, atenção e Próximos Passos. Ela não absorve as fontes de verdade dos demais objetos.

A Organização não deve ser confundida com Guivos Business. Seus planos `Conecta · Eleva · Transforma` permanecem distintos de `Start · Growth · Scale · Enterprise`.

## 6. Coletivo — continuidade principal

A experiência do Coletivo deve preservar a continuidade entre:

```text
COL-002 — VISÃO GERAL / INÍCIO
→ SOLICITAÇÕES
→ PARTICIPANTES E VÍNCULOS
→ COMUNICAÇÃO OFICIAL
→ ATIVIDADES / CONSULTAS / DECISÕES
→ PROTEÇÃO / MODERAÇÃO
→ RELAÇÃO ORGANIZAÇÃO–COLETIVO
→ PLANOS / CAPACIDADES CONTEXTUAIS QUANDO APLICÁVEL
```

O Coletivo não deve ser antropomorfizado. Ações pertencem a pessoas com papel e autoridade adequados.

Planos `Livre · Mobiliza · Impacta · Rede` governam capacidades comerciais aplicáveis; não redefinem legitimidade, governança ou autoridade humana.

## 7. Bilateralidade Organização ↔ Coletivo

A relação O↔C deve ser orquestrada como **um mesmo objeto bilateral com perspectivas distintas**.

```text
ORGANIZAÇÃO
→ ORG-004 / ORG-005 / ORG-006

COLETIVO
→ COL-008

OBJETO RELACIONAL
→ MESMO ESCOPO GOVERNADO
→ PERSPECTIVAS E AUTORIDADES DISTINTAS
```

A experiência deve preservar:

- quem propôs;
- quem precisa responder;
- estado corrente;
- escopo;
- compromissos;
- consentimentos;
- uso de marca quando aplicável;
- contestação;
- encerramento;
- responsabilidades remanescentes.

Uma contraparte não se torna recurso interno da outra.

## 8. Oportunidades e manifestações

Na continuidade de oportunidades, distinguir publicação, descoberta, manifestação/inscrição e gestão institucional.

```text
ORG-002
→ CADASTRO

ORG-003
→ OPORTUNIDADE APROVADA / ATIVA

PESSOA
→ DESCOBERTA / DETALHE / DECISÃO

PER-204
↔ ORG-008
→ CONTINUIDADE BILATERAL INTERNA CONTRATADA
```

`TRN-213..216` preservam a continuidade contratada aplicável. Retornos contextuais não recebem novos IDs por simetria.

Publicação não garante distribuição, candidatura, relevância ou resultado.

## 9. Solicitações, participantes e vínculos do Coletivo

A orquestração deve distinguir:

```text
SOLICITAÇÃO
≠ APROVAÇÃO
≠ VÍNCULO FORMADO
≠ PARTICIPAÇÃO ATIVA
≠ AUTORIDADE DE GOVERNANÇA
```

A aprovação legítima pode formar vínculo conforme autoridade vigente; a continuidade operacional posterior não deve repetir aprovação nem inferir persistência técnica.

Participantes pertinentes podem ser exibidos nas superfícies adequadas, respeitando finalidade, minimização, autoridade e proteção.

## 10. Comunicação, atividades e decisões

Comunicação oficial, atividade, consulta e decisão são responsabilidades relacionadas, mas não equivalentes.

```text
COMUNICAR
≠ DECIDIR

PARTICIPAR
≠ APROVAR

ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO
```

A UI deve tornar compreensível quando uma manifestação é informativa, participativa, consultiva ou decisória e qual autoridade produz efeito.

## 11. Responsabilidades, evidências e prestação de contas

`ORG-007` apoia localização e compreensão de responsabilidades, compromissos, resultados autorizados e evidências sem se tornar fonte de verdade de todos os objetos referenciados.

Preservar:

```text
CORRELAÇÃO
≠ CAUSALIDADE

CONFIRMADO
≠ IMPACTO PROVADO

SEM EVIDÊNCIA
≠ SEM RESULTADO

DESCONHECIDO
≠ ZERO
```

Proveniência, escopo, suficiência, contestação e limites de conclusão devem permanecer acessíveis quando materiais.

## 12. Autoridade como responsabilidade transversal

Organização & Autoridade e Coletivo & Autoridade não constituem superfícies exclusivas.

A autoridade deve atravessar a experiência de modo proporcional à ação.

A UI pode tornar papel e capacidade de atuação compreensíveis, mas não deve converter visibilidade em permissão nem substituir governança por RBAC presumido.

## 13. Estados transversais

A orquestração deve acomodar, quando aplicáveis:

- autoridade válida;
- autoridade insuficiente;
- aprovação adicional necessária;
- responsável ausente;
- informação incompleta;
- proteção;
- contestação;
- indisponibilidade;
- pausa;
- expiração;
- encerramento;
- responsabilidades remanescentes;
- contexto alterado;
- dado desatualizado.

Estado alternativo não é erro de Design e não deve ser ocultado para preservar happy path.

## 14. Ação, processamento e feedback

Toda ação material deve distinguir, quando aplicável:

```text
AÇÃO DISPONÍVEL
→ AÇÃO CONSCIENTE
→ PROCESSANDO
→ SUCESSO CONFIRMADO
   ou
→ FALHA RECUPERÁVEL
   ou
→ ESTADO INDETERMINADO
```

A interface não deve antecipar sucesso. Repetição após incerteza deve evitar efeito duplicado quando houver risco material.

## 15. Retorno, interrupção e retomada

```text
VOLTAR
≠ DESFAZER

SAIR DA SUPERFÍCIE
≠ CANCELAR PROCESSO

REENTRAR
≠ REEXECUTAR AÇÃO

RETRY
≠ DUPLICAR EFEITO
```

Retornos devem reconsultar estado corrente quando a informação puder ter sido alterada por outra pessoa ou contraparte.

## 16. Planos e capacidades

Planos devem aparecer de forma contextual, sem dominar responsabilidades operacionais.

```text
PLANO
→ CAPACIDADE COMERCIAL APLICÁVEL

PLANO
≠ AUTORIDADE HUMANA
≠ LEGITIMIDADE
≠ RELEVÂNCIA
≠ IMPACTO
≠ EVIDÊNCIA
```

A experiência pode explicar capacidade indisponível ou alternativa de plano quando existir autoridade comercial correspondente. Não inventar entitlement técnico, limite, métrica ou benefício.

## 17. Proteção, privacidade e minimização

A orquestração deve preservar:

- necessidade e finalidade;
- minimização;
- separação entre contexto pessoal e institucional;
- proteção de participantes;
- contestação e correção quando aplicáveis;
- revalidação de autoridade;
- não exposição de informação protegida por mera encontrabilidade.

```text
ENCONTRÁVEL
≠ REVELÁVEL

AGREGADO
≠ LIVRE DE GOVERNANÇA

HISTÓRICO
≠ RETENÇÃO ILIMITADA
```

## 18. Organização↔Organização e Coletivo↔Coletivo

As duas necessidades conceituais são reconhecidas, mas a evidência corrente não justifica superfície, lifecycle ou transições próprias.

A orquestração não pode preencher essas lacunas por analogia.

```text
O↔O
→ NECESSIDADE CONCEITUAL RECONHECIDA
→ SEM ID DEDICADO JUSTIFICADO

C↔C
→ NECESSIDADE CONCEITUAL RECONHECIDA
→ SEM ID DEDICADO JUSTIFICADO
```

## 19. Aprendizados e evidências do Coletivo

Aprendizados e evidências permanecem responsabilidade transversal.

A experiência pode apoiar compreensão de resultados autorizados e evidências pertinentes sem criar `COL-*` exclusivo ou inferir aprendizado apenas pela ocorrência de atividade.

## 20. Prioridade de atenção

Quando múltiplos elementos disputarem atenção, priorizar:

1. segurança, proteção, direito ou obrigação material;
2. processo iniciado que exija ação;
3. prazo real;
4. contestação ou autoridade insuficiente;
5. continuidade da tarefa atual;
6. responsabilidade pendente;
7. contexto informativo;
8. capacidade comercial contextual.

Plano ou promoção não ultrapassa responsabilidade material apenas por valor comercial.

## 21. Prototipação UX/UI — cobertura mínima

Uma prototipação integrada deve conseguir demonstrar, sem afirmar implementação:

- entrada autenticada com contexto compreensível;
- Visão Geral de Organização;
- Visão Geral/Início de Coletivo;
- troca de contexto com revalidação;
- oportunidade: cadastro → ativa → manifestações;
- continuidade bilateral PER-204 ↔ ORG-008 quando aplicável;
- solicitações de Coletivo;
- participantes e vínculos;
- comunicação oficial;
- atividades, consultas e decisões;
- proteção e moderação;
- relação O↔C nas duas perspectivas;
- responsabilidades e evidências;
- autoridade insuficiente;
- contestação;
- indisponibilidade;
- retorno e retomada;
- plano/capacidade contextual quando legítimo;
- estado vazio;
- falha recuperável.

Isso não exige um frame por item.

## 22. Liberdade de Design

Este documento governa significado, continuidade e comportamento transversal, não estética.

Design pode decidir composição, grid, componentes, navegação visual, tipografia conforme autoridade de marca, cores, imagens, iconografia, densidade, motion, microinterações, responsividade e quantidade de frames.

A liberdade visual não pode alterar participante, autoridade, responsabilidade, estado, transição, evidência, plano ou significado governado.

## 23. IA — source lock

IA utilizada para Design ou prototipação deve operar em source lock com o GKR e consumir esta autoridade junto dos Masters necessários.

```text
NÃO ESTÁ GOVERNADO NO GKR
→ NÃO INVENTAR
→ SINALIZAR LACUNA
→ NÃO CRIAR SUPERFÍCIE
→ NÃO CRIAR TRANSIÇÃO
→ NÃO CRIAR PERMISSÃO
→ NÃO CRIAR ENTITLEMENT
→ NÃO CRIAR MÉTRICA
```

IA é consumidora da verdade de produto, não sua autora.

## 24. Critérios executivos de aceite

Uma materialização orientada por esta autoridade é semanticamente aceitável quando:

1. Organização e Coletivo parecem experiências contínuas;
2. participante, contexto, papel e autoridade permanecem compreensíveis;
3. troca de contexto revalida autoridade;
4. Organização e Coletivo não são artificialmente simétricos;
5. bilateralidade O↔C preserva duas perspectivas;
6. ações materiais distinguem processamento e resultado;
7. estados alternativos são representáveis;
8. retornos não produzem mutação silenciosa;
9. plano não substitui autoridade;
10. evidência não vira causalidade ou impacto por inferência;
11. proteção e minimização permanecem preservadas;
12. O↔O e C↔C não são inventados;
13. IA não cria verdade de produto;
14. Design mantém liberdade criativa;
15. protótipo não é confundido com implementação;
16. Product Engineering não é liberado por esta autoridade.

## 25. Ordem recomendada de consumo

```text
LEIA PRIMEIRO
→ ESTE DOCUMENTO DE ORQUESTRAÇÃO
→ JORNADAS INTEGRADAS O/C
→ JOBS / AUTORIDADE
→ ARQUITETURA DA INFORMAÇÃO
→ MAPA DE SUPERFÍCIES
→ MAPA DE ESTADOS
→ FLUXOS PRIORITÁRIOS
→ MASTER DA SUPERFÍCIE EM CONSTRUÇÃO
→ REGISTRIES / AUTORIDADE ESPECÍFICA QUANDO NECESSÁRIO
```

## 26. Boundary de maturidade

Esta autoridade candidata organiza o consumo da verdade documental já existente. Ela não reabre o checkpoint de completude estrutural e não promove maturidade de superfície ou transição.

```text
DOCUMENTARY COMPLETENESS
→ PASS / PRESERVED

NEW GKR-SURF-*
→ NONE

NEW GKR-TRN-*
→ NONE

HIGH-FIDELITY DELIVERY
→ NOT_RECEIVED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED BY THIS DOCUMENT

PRODUCT ENGINEERING
→ NOT_RELEASED
```

## 27. Estado

```text
O/C JOURNEY UX/UI ORCHESTRATION
→ CANDIDATE

ROLE
→ MASTER / END-TO-END ORCHESTRATION
→ DESIGN + AI + PROTOTYPING CONSUMPTION

DOCUMENTARY COMPLETENESS
→ PRESERVED / PASS

NEW SURFACE / TRANSITION IDS
→ NONE

VISUAL BASELINE
→ NONE CREATED BY THIS DOCUMENT

AI
→ SOURCE-LOCKED TO GKR

PRODUCT ENGINEERING
→ NOT RELEASED
```
