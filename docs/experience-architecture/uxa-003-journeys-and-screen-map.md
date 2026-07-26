---
id: UXA-003
title: Mapa Inicial de Jornadas e Telas
status: active
version: 0.1.0
owner: Guivos Experience Architecture
last_updated: 2026-07-25
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-002
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
related:
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
normative: false
---

# UXA-003 — Mapa Inicial de Jornadas e Telas

## 1. Finalidade

Este documento define o inventário inicial de superfícies da Guivos e sua relação com as jornadas de Pessoa, Organização e Coletivo.

O mapa representa responsabilidades e relações. Ele não define layout final, número definitivo de telas, tecnologia, componentes ou sequência obrigatória.

## 2. Arquitetura global de entrada

```text
Acesso ou convite
→ autenticação e segurança
→ escolha ou criação do participante
→ seleção do contexto de atuação
→ configuração progressiva
→ superfície inicial correspondente
```

Contextos de atuação:

- Jornada pessoal;
- Organização representada;
- Coletivo administrado ou integrado.

## 3. Telas globais compartilhadas

| Tela | Responsabilidade |
|---|---|
| Entrada e autenticação | acesso, recuperação, segurança e consentimentos essenciais |
| Seletor de contexto | alternar explicitamente entre Pessoa, Organização e Coletivo |
| Busca global | localizar oportunidades, organizações, coletivos, conteúdos e experiências |
| Central de Intervenções | reunir decisões, confirmações, alertas, lembretes e histórico |
| Central de privacidade | permissões, finalidades, integrações, compartilhamentos e revogações |
| Ajuda e contestação | suporte, denúncia, correção, recurso e explicações |
| Preferências | idioma, acessibilidade, canais, frequência e personalização |

## 4. Jornada da Pessoa

### 4.1 Descoberta e primeira entrada

| Tela | Conteúdo principal |
|---|---|
| Apresentação da Guivos | proposta de valor, limites e exemplos concretos |
| Escolha de intenção inicial | o que deseja compreender, construir, resolver ou explorar |
| Captura progressiva de contexto | voz, texto, escolhas rápidas e fontes autorizadas |
| Compreensão inicial | síntese do que a Guivos entendeu, com origem e incertezas |
| Confirmação e controle | confirmar, corrigir, limitar, adiar ou apagar |
| Primeiro movimento | objetivo, Próximo Passo ou oportunidade inicial, sem pipeline obrigatório |

### 4.2 Navegação recorrente

| Área | Telas iniciais |
|---|---|
| Hoje | início diário; atenção; movimento atual; oportunidades; coletivos; perto de mim; registro do vivido |
| Jornada | visão geral; Meu Contexto Hoje; Meus Objetivos; Meus Próximos Passos; Experiências; Evolução |
| Explorar | Oportunidades; Organizações; Coletivos; Conteúdos; Serviços e Produtos; Viagens e Experiências |
| Mapa | mapa geral; filtros; detalhes locais; rotas e agendas; itens salvos |
| Eu | conta; contexto; interesses; privacidade; integrações; notificações; plano; histórico |

### 4.3 Meu Contexto Hoje

Subtelas ou estados:

- síntese do momento;
- dimensões do contexto;
- mudanças recentes;
- itens para revisar;
- conflitos;
- origem e uso das informações;
- permissões;
- integrações;
- histórico;
- correção e contestação.

### 4.4 Meus Objetivos

Subtelas ou estados:

- visão geral;
- objetivos ativos;
- em exploração;
- pausados e bloqueados;
- concluídos e retirados;
- detalhe do objetivo;
- critérios e marcos;
- conflitos e dependências;
- histórico;
- privacidade e compartilhamento.

### 4.5 Meus Próximos Passos

Subtelas ou estados:

- visão geral;
- passo principal;
- prontos;
- agendados;
- em andamento;
- bloqueados;
- propostas e alternativas;
- agenda e janelas;
- compartilhados;
- recorrentes;
- detalhe do passo;
- resultados;
- histórico.

### 4.6 Minhas Oportunidades

Subtelas ou estados:

- visão geral;
- para considerar;
- busca;
- filtros;
- mapa;
- comparação;
- salvas;
- interesses declarados;
- processos iniciados;
- ocultadas;
- histórico;
- preferências de relevância;
- fontes e relações comerciais;
- detalhe da oportunidade.

### 4.7 Experiências e Evolução

Subtelas ou estados:

- experiências recentes;
- experiências em andamento;
- confirmação de participação;
- resultado e percepção;
- evidências autorizadas;
- memórias privadas;
- mudanças reconhecidas;
- trajetórias por objetivo ou período;
- incertezas e revisões;
- exportação ou compartilhamento autorizado.

## 5. Jornada da Organização

### 5.1 Entrada institucional

| Tela | Conteúdo principal |
|---|---|
| Criar ou reivindicar Organização | identidade, natureza e vínculo legítimo |
| Verificação institucional | documentos, domínio, responsáveis e autoridade |
| Perfil público | nome, propósito, descrição, locais, canais e transparência |
| Equipe e papéis | proprietário, administrador, editor, analista, atendimento e auditor |
| Configuração de privacidade | dados institucionais, públicos e operações autorizadas |
| Configuração comercial | cobrança, relação financeira, patrocínio e integrações |

### 5.2 Visão Geral da Organização

Deverá apresentar:

- estado de verificação;
- oportunidades ativas, em revisão e expirando;
- processos ou inscrições em andamento;
- atividades e programas próximos;
- itens que exigem atenção;
- disponibilidade e capacidade;
- alterações materiais;
- visão resumida de resultados autorizados;
- alertas de conformidade;
- equipe e permissões pendentes.

### 5.3 Oportunidades da Organização

Telas:

- lista e estados;
- criar oportunidade;
- modelos reutilizáveis;
- rascunhos;
- em avaliação;
- ativas;
- pausadas;
- indisponíveis;
- expiradas e encerradas;
- inscrições e processos;
- disponibilidade;
- elegibilidade;
- preço e condições;
- locais e modalidades;
- versão e histórico;
- contestação e correção;
- resultados operacionais.

### 5.4 Programas e Públicos

Telas:

- programas institucionais;
- jornadas corporativas;
- benefícios;
- campanhas;
- públicos autorizados;
- convites;
- critérios de acesso;
- calendário;
- recursos;
- resultados e evidências;
- integrações.

### 5.5 Resultados

A Organização poderá acompanhar somente dados compatíveis com sua autoridade e finalidade:

- visualizações agregadas;
- interesses declarados;
- inscrições;
- reservas;
- disponibilidade;
- participação confirmada;
- resultados operacionais;
- feedback autorizado;
- qualidade da informação;
- alterações e correções;
- relações comerciais.

Não deverá receber perfil paralelo ou contexto pessoal não autorizado.

## 6. Jornada do Coletivo

### 6.1 Criação ou entrada

| Tela | Conteúdo principal |
|---|---|
| Criar Coletivo | nome, propósito, tipo, visibilidade e regras iniciais |
| Descobrir Coletivo | busca, mapa, relação com interesses e objetivos |
| Perfil público | propósito, atividades, regras, responsáveis e formas de participação |
| Solicitar entrada | informações necessárias, finalidade e decisão do Coletivo |
| Aceitar convite | papel, regras, privacidade e notificações |
| Configurar participação | identidade visível, canais, interesses e permissões |

### 6.2 Início do Coletivo

Deverá apresentar:

- propósito e síntese;
- próxima atividade;
- itens de atenção;
- oportunidades do Coletivo;
- calendário;
- solicitações e convites;
- recursos recentes;
- parceiros e apoios;
- resultados ou evidências coletivas autorizadas;
- estado de moderação e governança.

### 6.3 Atividades

Telas:

- calendário;
- oportunidades;
- encontros;
- causas e ações;
- desafios;
- experiências;
- inscrições;
- presença e participação;
- resultados;
- histórico.

A experiência não deverá ser reduzida a feed infinito. Atualizações deverão estar vinculadas a atividades, decisões, recursos ou relações do Coletivo.

### 6.4 Pessoas e Papéis

Telas:

- membros;
- solicitações;
- convites;
- líderes e moderadores;
- equipes ou núcleos;
- papéis;
- permissões;
- participação pausada;
- saída e remoção;
- histórico de governança.

### 6.5 Recursos e relações

Telas:

- conteúdos;
- documentos;
- locais;
- equipamentos;
- benefícios;
- Organizações apoiadoras;
- especialistas;
- oportunidades compartilhadas;
- fontes externas;
- regras de uso.

## 7. Tela de detalhe de uma Organização

Deverá apresentar:

- identidade e verificação;
- propósito e descrição;
- categoria e atuação;
- locais e modalidades;
- oportunidades ativas;
- Coletivos relacionados;
- programas;
- avaliações ou sinais permitidos;
- relações comerciais com a Guivos;
- acessibilidade;
- formas de contato;
- políticas, termos e contestação;
- salvar, seguir ou limitar exposição.

## 8. Tela de detalhe de um Coletivo

Deverá apresentar:

- nome, propósito e tipo;
- visibilidade;
- responsáveis;
- regras e critérios de entrada;
- localização ou abrangência;
- atividades próximas;
- oportunidades;
- membros ou quantidade, conforme privacidade;
- Organizações relacionadas;
- recursos;
- calendário;
- forma de participar;
- controles de notificação;
- denúncia, saída e privacidade.

## 9. Tela de detalhe de uma oportunidade

Deverá conter, conforme aplicável:

1. título e tipo;
2. Organização, Coletivo ou fonte responsável;
3. descrição e finalidade;
4. por que pode ser relevante;
5. relação com objetivo ou Próximo Passo;
6. disponibilidade;
7. data, prazo e validade;
8. local, distância ou modalidade;
9. preço, gratuidade, subsídio e custo total conhecido;
10. condições de pagamento ou cancelamento;
11. elegibilidade e documentos;
12. acessibilidade;
13. riscos e limitações;
14. relação comercial, patrocínio ou comissão;
15. fonte e última atualização;
16. comparação e alternativas;
17. ações: salvar, interessar, iniciar, ocultar, compartilhar ou contestar;
18. privacidade e dados utilizados.

## 10. Estados transversais obrigatórios

Toda família de telas deverá prever:

- carregamento;
- informação parcial;
- estado vazio;
- falha segura;
- indisponibilidade;
- expiração;
- conflito;
- contestação;
- correção;
- sensibilidade;
- ausência de autorização;
- participação encerrada;
- histórico.

## 11. Ordem para wireframes

1. Hoje — Pessoa;
2. detalhe da oportunidade;
3. Minhas Oportunidades;
4. Explorar;
5. mapa;
6. criação de oportunidade — Organização;
7. visão geral da Organização;
8. detalhe e início do Coletivo;
9. criação e gestão do Coletivo;
10. Jornada: Contexto, Objetivos e Próximos Passos.
