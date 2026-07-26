---
id: UXA-001
title: Fundação da Arquitetura da Experiência da Guivos
status: active
version: 0.2.0
owner: Guivos Experience Architecture
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - GLPA-001
  - GIA-000
related:
  - UXA-020
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
normative: false
---

# UXA-001 — Fundação da Arquitetura da Experiência da Guivos

## 1. Problema central

O GKR já define com profundidade o que as capacidades do Guivos Journey devem governar, mas ainda precisa consolidar como Pessoas, Organizações e Coletivos navegarão entre essas capacidades, quais telas existirão, o que aparecerá primeiro, como a relevância será controlada e como as soluções especializadas serão integradas à experiência.

A pergunta central desta frente é:

> **Como transformar a arquitetura funcional da Guivos em uma experiência simples, contínua e útil, capaz de apoiar decisões e ações reais sem produzir dependência, pressão ou fragmentação?**

## 2. Decisão de natureza

A Guivos possuirá uma **arquitetura de experiência unificada**, com superfícies diferentes conforme:

- categoria do participante;
- papel exercido naquele momento;
- contexto autorizado;
- objetivo e Próximo Passo;
- responsabilidade institucional;
- canal e dispositivo;
- sensibilidade e privacidade;
- estado da relação com uma oportunidade, organização ou coletivo;
- estágio de entrada: visitante, jornada não iniciada ou jornada em continuidade.

Pessoa, Organização e Coletivo são categorias arquiteturais. Uma mesma conta humana poderá exercer papéis em mais de um participante, mediante autorização e troca explícita de contexto.

## 3. Princípios permanentes de experiência

1. **Utilidade antes de frequência.** A Guivos não será otimizada para tempo de tela ou acesso compulsivo.
2. **HOME antes de personalização.** A Guivos deverá apresentar propósito, início voluntário e controles antes de afirmar relevância pessoal.
3. **Hoje antes de feed.** Depois do início da jornada, a superfície recorrente deverá explicar o que é material no momento, não oferecer rolagem infinita.
4. **Jornada não linear.** Nenhuma tela deverá transformar as nove capacidades do Journey em pipeline obrigatório.
5. **Decisão com o participante.** A interface poderá explicar, comparar e propor, mas não decidir objetivo, prioridade ou compromisso humano.
6. **Relevância controlável.** Toda personalização material deverá ser explicável, ajustável e contestável.
7. **Clareza comercial.** Preço, patrocínio, comissão, subsídio e relação financeira deverão ser visíveis sem alterar relevância funcional.
8. **Silêncio legítimo.** Ausência de oportunidade, intervenção ou Próximo Passo é um estado válido.
9. **Detalhamento progressivo.** A tela apresenta primeiro o necessário para compreender e decidir; evidências, histórico e permissões permanecem acessíveis.
10. **Privacidade por padrão.** Informações sensíveis não devem aparecer em resumos, notificações ou telas compartilhadas sem necessidade.
11. **Ação no mundo real.** A experiência deverá facilitar participação, contratação, encontro, aprendizagem e realização fora da plataforma.
12. **Consistência entre canais.** Aplicativo, web e futuras interfaces deverão preservar a mesma semântica funcional.
13. **Acessibilidade estrutural.** A experiência deverá funcionar sem depender apenas de cor, gesto, áudio ou alta capacidade cognitiva.
14. **Exploração sem coerção.** A pessoa poderá conhecer o ecossistema sem iniciar sua jornada ou compartilhar contexto pessoal.
15. **Compreensão antes de indicação.** Conteúdo geral e indicação pessoal deverão permanecer distintos até existir contexto suficiente e autorizado.

## 4. Objetivos da Arquitetura da Experiência

A frente deverá produzir:

- mapa de jornadas por participante e papel;
- arquitetura global de entrada e navegação;
- inventário de telas e estados;
- responsabilidade e conteúdo mínimo de cada tela;
- fluxos críticos de entrada, descoberta, decisão, participação e revisão;
- padrões de cartões, listas, mapas, comparações, alertas e estados vazios;
- regras de frequência e retorno;
- wireframes de baixa fidelidade;
- protótipos navegáveis;
- hipóteses e roteiros de teste de usabilidade;
- contratos de handoff posteriores para Produto, UI, Engenharia, QA, Segurança, Jurídico, IA e Analytics.

## 5. Modelo de entrada e navegação global proposto

### 5.0 Página Inicial da Guivos — HOME

A HOME é uma superfície global anterior à navegação recorrente pessoal.

Responsabilidades:

- apresentar propósito e impacto da Guivos;
- convidar voluntariamente a iniciar a jornada;
- permitir relato do Momento Atual por modalidades autorizadas;
- apresentar a compreensão inicial para revisão;
- permitir conhecer as soluções do ecossistema sem personalização;
- direcionar a pessoa para autenticação, privacidade, ajuda e acessibilidade;
- conduzir à Tela Hoje somente depois do gate de compreensão.

A HOME poderá permanecer acessível por marca ou menu institucional depois do início da jornada, sem necessariamente ocupar uma posição na navegação móvel principal.

### 5.1 Navegação principal da Pessoa

| Destino | Responsabilidade |
|---|---|
| **Hoje** | concentrar o que mudou, o que merece atenção e o que pode apoiar o momento atual depois da compreensão inicial |
| **Jornada** | reunir Contexto, Objetivos, Próximos Passos, Experiências e Evolução |
| **Explorar** | descobrir Oportunidades, Organizações, Coletivos, conteúdos, serviços e experiências |
| **Mapa** | visualizar oportunidades, organizações, coletivos e eventos por localização autorizada |
| **Eu** | controlar contexto, preferências, privacidade, integrações, conta e plano |

A `Central de Intervenções` deverá permanecer acessível por um controle global de atenção, sem se tornar uma caixa de entrada infinita.

### 5.2 Navegação principal da Organização

| Destino | Responsabilidade |
|---|---|
| **Visão Geral** | estado institucional, itens de atenção e resultados operacionais |
| **Oportunidades** | criar, revisar, publicar, atualizar e encerrar oportunidades |
| **Programas e Públicos** | organizar jornadas, benefícios, campanhas e públicos autorizados |
| **Coletivos e Parcerias** | criar ou apoiar coletivos, alianças, causas e iniciativas |
| **Resultados** | acompanhar participação, disponibilidade, processos e evidências autorizadas |
| **Organização** | perfil, equipe, papéis, permissões, integrações, cobrança e conformidade |

### 5.3 Navegação principal do Coletivo

| Destino | Responsabilidade |
|---|---|
| **Início** | propósito, próximos acontecimentos, itens de atenção e visão resumida |
| **Atividades** | oportunidades, encontros, ações, desafios e experiências do coletivo |
| **Pessoas e Papéis** | membros, solicitações, papéis, equipes e governança |
| **Mapa e Agenda** | locais, eventos, disponibilidade e calendário compartilhado |
| **Recursos** | conteúdos, documentos, benefícios, parceiros e materiais |
| **Gestão** | regras, privacidade, moderação, permissões e integrações |

## 6. Troca de contexto e papel

Uma pessoa autenticada poderá:

- atuar em sua jornada pessoal;
- representar uma Organização;
- administrar ou participar de um Coletivo;
- alternar entre contextos por seletor explícito;
- visualizar claramente em nome de quem está realizando uma ação.

A interface nunca deverá permitir que uma ação institucional pareça pessoal ou que uma ação pessoal seja executada em nome de uma Organização ou Coletivo sem confirmação.

A HOME anterior ao início da jornada não deverá presumir que a pessoa está representando uma Organização ou Coletivo. Essa escolha deverá ser consciente e contextual.

## 7. Hierarquia de superfícies

### Nível 0 — Entrada global

- Página Inicial da Guivos;
- entrada e autenticação;
- início da jornada;
- compreensão inicial e confirmação;
- conhecimento do ecossistema.

### Nível 1 — Orientação recorrente

- Hoje;
- visão geral da Organização;
- início do Coletivo.

### Nível 2 — Domínios

- Jornada;
- Oportunidades;
- Explorar;
- Mapa;
- Programas;
- Atividades;
- Resultados.

### Nível 3 — Unidades

- objetivo;
- Próximo Passo;
- oportunidade;
- organização;
- coletivo;
- evento;
- experiência;
- intervenção;
- elemento de contexto.

### Nível 4 — Explicação e controle

- por que estou vendo;
- dados utilizados;
- fonte e autoridade;
- histórico;
- permissões;
- contestação;
- privacidade;
- auditoria compreensível.

## 8. Relação com os produtos especializados

O Journey permanece responsável pela experiência visível e contextual. Os produtos especializados fornecem capacidades e operações:

- Guivos Mall: produtos, serviços, preços, carrinho e transações;
- Guivos Travel: destinos, disponibilidade, reservas e viagens;
- Guivos Business: operações institucionais, públicos, programas e oportunidades organizacionais;
- Guivos Media: conteúdos e narrativas;
- Guivos Ads: publicidade explicitamente identificada;
- Guivos Intelligence: interpretação, comparação, explicação e candidatos de relevância.

A HOME poderá apresentar todas as soluções do ecossistema sem apagar sua origem ou transferir autoridade funcional.

Antes do gate de personalização, conteúdos serão gerais, institucionais, editoriais ou resultantes de busca explícita. A navegação não utilizará contexto presumido para afirmar relevância pessoal.

## 9. Frequência e recorrência

A frequência de acesso não será definida por uma meta universal. Ela deverá emergir de necessidades reais:

- mudança material no contexto;
- Próximo Passo ativo;
- oportunidade com janela temporal;
- atividade de Coletivo;
- processo externo em andamento;
- confirmação ou decisão pendente;
- registro de experiência;
- revisão voluntária da jornada.

A Guivos poderá ser útil diariamente para alguns participantes e esporadicamente para outros. Ambos os comportamentos são legítimos.

A HOME não deverá ser forçada a cada retorno. Depois do início da jornada, a Tela Hoje poderá se tornar a entrada recorrente preferencial.

## 10. Ordem inicial de detalhamento atualizada

1. Página Inicial da Guivos e início da jornada;
2. Tela Hoje e navegação global recorrente;
3. descoberta e detalhe de oportunidades;
4. controle de relevância;
5. mapa;
6. cadastro de oportunidade pela Organização;
7. perfil e operação de Coletivos;
8. integração com Contexto, Objetivos e Próximos Passos;
9. estados transacionais e experiências;
10. wireframes e testes.

A ordem representa dependência funcional, não cronologia obrigatória de desenvolvimento.

## 11. Gate desta fundação

| Critério | Estado |
|---|---|
| Arquitetura da Experiência separada de Engenharia de Produto | definido |
| Pessoa, Organização e Coletivo contemplados | definido |
| HOME anterior à experiência recorrente | definido pela UXA-020 |
| início voluntário e exploração geral | definido pela UXA-020 |
| personalização condicionada à compreensão | definido pela UXA-011-A1 e UXA-020 |
| navegação global recorrente | proposta e preservada |
| recorrência não compulsiva | definido |
| Tela Hoje como hipótese central recorrente | reformulada e validada funcionalmente |
| mapa de telas detalhado | UXA-003 |
| fluxos de oportunidades, organizações e coletivos | UXA-004 |
| wireframes | programa ativo; HOME textual e demais artefatos estruturais |
| validação com participantes | não iniciada |
| design visual e implementação | não iniciados |

## 12. Limites

Esta fundação não autoriza:

- texto final da HOME;
- identidade visual ou campanha de lançamento;
- formato técnico de voz ou arquivos;
- inferências sensíveis;
- protótipo navegável;
- teste de usabilidade;
- Engenharia de Produto;
- desenvolvimento ou produção.