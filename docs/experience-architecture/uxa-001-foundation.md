---
id: UXA-001
title: Fundação da Arquitetura da Experiência da Guivos
status: active
version: 0.1.0
owner: Guivos Experience Architecture
last_updated: 2026-07-25
parent: UXA-000
depends_on:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - GLPA-001
  - GIA-000
related:
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
normative: false
---

# UXA-001 — Fundação da Arquitetura da Experiência da Guivos

## 1. Problema central

O GKR já define com profundidade o que as capacidades do Guivos Journey devem governar, mas ainda não consolida como Pessoas, Organizações e Coletivos navegarão entre essas capacidades, quais telas existirão, o que aparecerá primeiro, como a relevância será controlada e como as soluções especializadas serão integradas à experiência.

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
- estado da relação com uma oportunidade, organização ou coletivo.

Pessoa, Organização e Coletivo são categorias arquiteturais. Uma mesma conta humana poderá exercer papéis em mais de um participante, mediante autorização e troca explícita de contexto.

## 3. Princípios permanentes de experiência

1. **Utilidade antes de frequência.** A Guivos não será otimizada para tempo de tela ou acesso compulsivo.
2. **Hoje antes de feed.** A superfície inicial deverá explicar o que é material no momento, não oferecer rolagem infinita.
3. **Jornada não linear.** Nenhuma tela deverá transformar as nove capacidades do Journey em pipeline obrigatório.
4. **Decisão com o participante.** A interface poderá explicar, comparar e propor, mas não decidir objetivo, prioridade ou compromisso humano.
5. **Relevância controlável.** Toda personalização material deverá ser explicável, ajustável e contestável.
6. **Clareza comercial.** Preço, patrocínio, comissão, subsídio e relação financeira deverão ser visíveis sem alterar relevância funcional.
7. **Silêncio legítimo.** Ausência de oportunidade, intervenção ou Próximo Passo é um estado válido.
8. **Detalhamento progressivo.** A tela apresenta primeiro o necessário para compreender e decidir; evidências, histórico e permissões permanecem acessíveis.
9. **Privacidade por padrão.** Informações sensíveis não devem aparecer em resumos, notificações ou telas compartilhadas sem necessidade.
10. **Ação no mundo real.** A experiência deverá facilitar participação, contratação, encontro, aprendizagem e realização fora da plataforma.
11. **Consistência entre canais.** Aplicativo, web e futuras interfaces deverão preservar a mesma semântica funcional.
12. **Acessibilidade estrutural.** A experiência deverá funcionar sem depender apenas de cor, gesto, áudio ou alta capacidade cognitiva.

## 4. Objetivos da Experience Architecture

A frente deverá produzir:

- mapa de jornadas por participante e papel;
- arquitetura global de navegação;
- inventário de telas e estados;
- responsabilidade e conteúdo mínimo de cada tela;
- fluxos críticos de entrada, descoberta, decisão, participação e revisão;
- padrões de cartões, listas, mapas, comparações, alertas e estados vazios;
- regras de frequência e retorno;
- wireframes de baixa fidelidade;
- protótipos navegáveis;
- hipóteses e roteiros de teste de usabilidade;
- contratos de handoff posteriores para Produto, UI, Engenharia, QA, Segurança, Jurídico, IA e Analytics.

## 5. Modelo de navegação global proposto

### 5.1 Navegação principal da Pessoa

| Destino | Responsabilidade |
|---|---|
| **Hoje** | concentrar o que mudou, o que merece atenção e o que pode apoiar o momento atual |
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

## 7. Hierarquia de superfícies

### Nível 1 — Orientação

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

A navegação poderá apresentar conteúdos desses produtos sem apagar sua origem ou transferir autoridade funcional.

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

## 10. Ordem inicial de detalhamento

1. tela `Hoje` e navegação global;
2. descoberta e detalhe de oportunidades;
3. controle de relevância;
4. mapa;
5. cadastro de oportunidade pela Organização;
6. perfil e operação de Coletivos;
7. integração com Contexto, Objetivos e Próximos Passos;
8. estados transacionais e experiências;
9. wireframes e testes.

## 11. Gate desta fundação

| Critério | Estado |
|---|---|
| Experience Architecture separada de Product Engineering | definido |
| Pessoa, Organização e Coletivo contemplados | definido |
| navegação global inicial | proposta |
| recorrência não compulsiva | definido |
| tela Hoje como hipótese central | proposta |
| mapa de telas detalhado | UXA-003 |
| fluxos de oportunidades, organizações e coletivos | UXA-004 |
| wireframes | não iniciados |
| validação com participantes | não iniciada |
