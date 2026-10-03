---
id: GKR-CHANGELOG-1.42.0
title: Histórico de Alterações 1.42.0 — Página Inicial da Guivos
status: historical
version: 1.42.0
owner: Guivos
last_updated: 2026-07-26
related:
  - GKR-STATE-001
  - ROADMAP-11.95.0
  - UXA-000
  - UXA-010
  - UXA-020
  - GKR-CANON-MATRIX-UXA-020
  - M7.21
normative: false
---

# Histórico de Alterações 1.42.0 — Página Inicial da Guivos

## Adicionado

- `UXA-020 — Página Inicial da Guivos e Início da Jornada`;
- contrato funcional da Página Inicial pública anterior à Tela Hoje;
- entrada protegida e separada para o início da jornada;
- wireframe textual de baixa fidelidade da Página Inicial pública;
- wireframe textual de entrada do ambiente protegido;
- estados de visitante, pessoa sem jornada, relato em andamento, relato em análise, compreensão disponível e jornada iniciada;
- relato do Momento Atual por texto, voz, arquivos e perguntas progressivas dentro do ambiente protegido;
- compartilhamento mínimo e progressivo;
- gate de compreensão e personalização;
- acesso geral às soluções do ecossistema antes do início da jornada;
- Painel de Conhecimento 11.95.0;
- Marcos Arquiteturais 4.93.0 — M7.21;
- Adendo da Matriz de Consolidação Canônica para UXA-020.

## Alterado

- Arquitetura da Experiência atualizada para `0.14.0`;
- Fundação da Arquitetura da Experiência atualizada para `0.2.0`;
- Experiência Diária e Tela Hoje atualizada para `0.2.0`;
- Programa Inicial de Wireframes atualizado para `0.3.0`;
- Wireframe da Tela Hoje atualizado para `0.5.0`;
- Validação Funcional da Tela Hoje atualizada para `0.3.0` e marcada como ativa;
- Página Inicial da Guivos e Início da Jornada atualizada para `0.2.0` e marcada como ativa;
- Compreensão do Momento, Evidência de Avanço e Explicabilidade atualizada para `0.2.0`;
- Registro do Estado Atual atualizado para `1.48.0`;
- Roadmap Arquitetural atualizado para `11.95.0`;
- Painel de Conhecimento central atualizado para `11.95.0`;
- Marcos Arquiteturais centrais atualizados para `4.93.0`;
- Matriz de Consolidação Canônica central atualizada para `2.14.0`;
- Tela Hoje reposicionada de primeira entrada pessoal para entrada recorrente após a compreensão inicial;
- Página Inicial pública separada do ambiente protegido de relato e processamento.

## Decisões consolidadas

- a Página Inicial apresenta propósito, impacto e soluções do ecossistema;
- iniciar a jornada é voluntário;
- conhecer o ecossistema não exige compartilhamento de contexto pessoal;
- a Página Inicial pública não coleta texto pessoal, voz, arquivos ou fontes externas;
- o relato acontece somente após transição consciente para ambiente protegido;
- autenticação e autorização compatíveis antecedem persistência, processamento multimodal, fontes externas e personalização material;
- a Guivos não afirma compreender a pessoa antes do relato;
- a compreensão inicial deve ser revisável, corrigível, limitável e rejeitável;
- indicação pessoal exige base suficiente e autorizada;
- conteúdo geral, publicidade e relevância pessoal permanecem distintos;
- **Guivos Mall** é o nome oficial do shopping do ecossistema;
- **Guivos Ads** é o nome oficial da solução de anúncios e patrocínios;
- Guivos Journey, Guivos Mall, Guivos Travel, Guivos Business, Guivos Media, Guivos Intelligence e Guivos Ads mantêm identidade própria;
- a navegação recorrente `Hoje`, `Jornada`, `Explorar`, `Mapa` e `Eu` permanece preservada.

## Sequência pessoal consolidada

```text
Página Inicial da Guivos
→ decisão voluntária de iniciar a jornada
→ autenticação e explicação de privacidade, quando necessárias
→ ambiente protegido para relato do Momento Atual
→ compreensão inicial revisável
→ correção, limitação e autorização
→ Tela Hoje
```

## Preservado

- Resultados Empresariais em 18 de 18 decisões humanas;
- distribuição de candidatos em 9 em validação, 3 fundidos e 6 rejeitados;
- Resultados aprovados e códigos canônicos em zero;
- `BUS-CAND-005` em validação após receber `BUS-CAND-010`;
- decisões e contratos das experiências de Organizações e Coletivos;
- gate obrigatório de alinhamento à Fundação;
- presença companheira sem intimidade artificial ou coerção;
- privacidade, acessibilidade, recusa, pausa, correção e exclusão;
- Engenharia de Produto pausada antes de W0-01.

## Limites

Este incremento não cria:

- texto final de marketing;
- identidade visual;
- arquivo gráfico definitivo da Página Inicial;
- protótipo navegável;
- teste de usabilidade;
- reconhecimento técnico de voz;
- formatos definitivos de arquivos;
- modelo de inteligência artificial;
- componentes, interfaces de programação ou implementação;
- Resultado canônico, AQS-O01 ou Capacidade Empresarial.
