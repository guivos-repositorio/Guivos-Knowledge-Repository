---
id: GKR-UX-D5-C1-001
title: Contrato de Materialização das Superfícies de Direção, Movimento e Evolução
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: UXA-000
normative: false
related:
  - PAS-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-EC-VIEW-001
  - GKR-UX-D5-A-001
  - GKR-UX-D5-B-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# GKR-UX-D5-C1-001 — Contrato de Materialização das Superfícies de Direção, Movimento e Evolução

## 1. Finalidade

A D5-C1 fecha o degrau arquitetural necessário antes de qualquer wireframe de `Meus Objetivos`, `Meus Próximos Passos` ou `Minha Evolução`.

A frente não desenha telas. Ela:

1. reconcilia para fins de Experience Architecture as expressões legadas que podem colidir com os Domínios de Evolução;
2. define três responsabilidades próprias da Jornada da Pessoa;
3. atribui identificadores estáveis às responsabilidades;
4. define os handoffs mínimos entre `PER-008 — Tela Hoje` e essas responsabilidades;
5. estabelece gates, entradas, saídas, reversibilidade e privacidade mínimos;
6. preserva a autoridade dos contratos funcionais do PAS-001;
7. prepara materializações visuais futuras sem iniciá-las.

A D5-C1 não cria SVG, não valida interface e não inicia Engenharia de Produto.

## 2. Autoridade e precedência

A autoridade funcional permanece nos contratos especializados:

- `PAS-001-OBJ-VIEW-001` — `Meus Objetivos`;
- `PAS-001-PP-VIEW-001` — `Meus Próximos Passos`;
- `PAS-001-EC-VIEW-001` — `Minha Evolução`.

A autoridade semântica dos Domínios de Evolução permanece em:

- `PAS-001-DOMAIN-MODEL-001`;
- `PAS-001-DOMAIN-RECON-001`.

Esta frente traduz essas autoridades para responsabilidades e handoffs da Experience Architecture. Ela não reescreve retroativamente os contratos publicados do PAS-001.

Em caso de divergência:

```text
contrato funcional especializado
+ autoridade canônica de Domínios
→ governam a semântica

D5-C1
→ governa somente a materialização arquitetural da experiência
```

## 3. Problema arquitetural resolvido

D5-A e D5-B puderam reformular superfícies existentes in-place.

D5-C não possui esse caminho porque o registro granular anterior à D5-C1 não continha responsabilidade própria para:

- `Meus Objetivos`;
- `Meus Próximos Passos`;
- `Minha Evolução`.

`PER-008 — Tela Hoje` não pode absorver essas três responsabilidades sem perder separação funcional.

A regra passa a ser:

```text
Hoje
= síntese recorrente + escolha consciente de aprofundamento

Meus Objetivos
= direção e controle de objetivos

Meus Próximos Passos
= movimentos contextuais e seu controle

Minha Evolução
= trajetórias, mudanças, continuidades, evidências e interpretações
```

Portanto:

```text
Hoje sintetiza
≠ Hoje substitui as capacidades especializadas
```

## 4. Reconciliação terminológica para Experience Architecture

### 4.1 Objetivos — “área ou dimensão contextual”

O contrato histórico de `Meus Objetivos` admite organização por `área ou dimensão contextual`.

A partir da D5-C1, para Experience Architecture, essa expressão deve ser desdobrada em dois conceitos distintos:

```text
área da jornada
→ Domínio de Evolução / domain_link

dimensão contextual
→ dimensão estrutural do Contexto Vivo, quando a intenção for estrutural
```

Nunca deverá existir um único filtro visual chamado `dimensão` que misture os dois conceitos.

Exemplo:

```text
Objetivo: assumir uma posição de liderança

Área da jornada:
Trabalho, Carreira e Estudos

Contexto relacionado:
Direção · Capacidades · Restrições
```

O Domínio de Evolução:

- pode organizar ou filtrar objetivos;
- pode relacionar `0..n` áreas;
- não define prioridade;
- não cria o Objetivo;
- não comprova progresso;
- não define critério de sucesso;
- não altera autoria;
- não transforma objetivo pessoal em institucional.

### 4.2 Próximos Passos — “área da vida”

O contrato histórico de `Meus Próximos Passos` admite organização por `área da vida`.

Para Experience Architecture, `área da vida` passa a ser expressão pública/legada compatível com **Área da jornada**, cuja referência semântica é um `domain_link` governado por `PAS-001-DOMAIN-MODEL-001`.

A superfície deverá preferir linguagem pública compreensível como:

- `Área da jornada`;
- ou o nome do domínio quando o contexto já estiver claro.

O identificador interno `JED-*` não é rótulo obrigatório de interface.

Um Próximo Passo poderá possuir `0..n` relações de domínio, mas:

```text
domínio relacionado
≠ prioridade
≠ prontidão
≠ obrigação
≠ urgência
≠ recomendação comercial
≠ prova de execução
```

### 4.3 Evolução Contínua — “dimensão”

`PAS-001-EC-VIEW-001` utiliza historicamente `dimensão` em vários pontos de representação.

A D5-C1 aplica a desambiguação já governada por `PAS-001-DOMAIN-RECON-001` e exige que qualquer futura materialização identifique qual dos três conceitos está sendo representado:

1. **Domínio de Evolução** — sobre qual área a trajetória trata;
2. **dimensão estrutural do Contexto Vivo** — como o contexto é estruturalmente representado;
3. **aspecto descritivo da mudança** — natureza/faceta complementar da mudança.

Exemplo governado:

```text
Domínio
Trabalho, Carreira e Estudos

Trajetória
Transição para posição de liderança

Aspectos observados
profissional · cognitivo · comportamental

Contexto relacionado
Direção · Capacidades · Restrições
```

A interface futura não poderá reduzir esses elementos a um único campo genérico `Dimensão`.

### 4.4 Regra prospectiva

A reconciliação da D5-C1 é prospectiva para a Experience Architecture.

Ela não apaga termos históricos dos contratos publicados e não altera a evidência da release do PAS-001.

## 5. Novas responsabilidades canônicas da Jornada da Pessoa

A D5-C1 cria três responsabilidades granulares, todas inicialmente com maturidade **contratada** e sem materialização visual.

| ID | Responsabilidade | Capacidade governante | Papel principal |
|---|---|---|---|
| `GKR-SURF-PER-010` | `Meus Objetivos` | Capacidade 03 — Objetivos | compreender, organizar e controlar direções e objetivos |
| `GKR-SURF-PER-011` | `Meus Próximos Passos` | Capacidade 05 — Próximos Passos | compreender, organizar e controlar movimentos contextuais |
| `GKR-SURF-PER-012` | `Minha Evolução` | Capacidade 09 — Evolução Contínua | compreender e controlar trajetórias, mudanças, continuidades e interpretações |

Esses IDs representam responsabilidades de superfície.

Eles não representam:

- três módulos implementados;
- três rotas técnicas;
- três tabelas;
- três serviços;
- três componentes de frontend;
- três produtos separados.

## 6. PER-010 — Meus Objetivos

### 6.1 Entrada mínima

Entrada canônica inicial:

```text
PER-008 — Hoje
→ TRN-008
→ PER-010 — Meus Objetivos
```

A entrada exige:

- Pessoa autenticada;
- ação consciente de aprofundamento;
- preservação do contexto recorrente vigente;
- nenhuma criação automática de Objetivo pela navegação.

### 6.2 Responsabilidade

`PER-010` deverá futuramente materializar, sem redefinir o contrato funcional:

- visão geral de objetivos;
- portfólio e estados;
- prioridades declaradas e sugeridas separadamente;
- critérios, marcos, progresso e evidências quando legítimos;
- conflitos e dependências;
- revisão, pausa, retomada, retirada, conclusão e histórico;
- controles de privacidade e compartilhamento;
- organização/filtro por Área da jornada quando útil.

### 6.3 Domínios

`PER-010` poderá representar `0..n domain_link` por Objetivo.

A área não precisa ocupar obrigatoriamente o cartão resumido, especialmente em contexto sensível.

### 6.4 Saída mínima

Retorno canônico inicial:

```text
PER-010
→ TRN-009
→ PER-008
```

Retornar a Hoje:

- não altera Objetivo;
- não confirma sugestão;
- não muda prioridade;
- não cria progresso;
- não encerra revisão em aberto sem ação correspondente.

## 7. PER-011 — Meus Próximos Passos

### 7.1 Entrada mínima

```text
PER-008 — Hoje
→ TRN-010
→ PER-011 — Meus Próximos Passos
```

A navegação:

- não inicia automaticamente um passo;
- não confirma uma proposta;
- não converte sugestão em decisão;
- não cria urgência artificial.

### 7.2 Responsabilidade

`PER-011` deverá futuramente organizar:

- portfólio ativo;
- propostas e alternativas;
- estados como pronto, agendado, em andamento, bloqueado e pausado;
- dependências e bloqueios;
- responsabilidades;
- recorrências;
- resultados recentes;
- histórico;
- filtros e agrupamentos, inclusive por Área da jornada quando útil.

### 7.3 Domínios

A área é metadado contextual e revisável.

```text
Área da jornada
≠ prioridade do passo
≠ prontidão
≠ obrigação
≠ agenda
≠ mérito
```

Em conteúdos sensíveis, o título e a área podem exigir minimização ou ocultação até ação consciente.

### 7.4 Saída mínima

```text
PER-011
→ TRN-011
→ PER-008
```

O retorno não marca passo como concluído, visto, aceito ou executado.

## 8. PER-012 — Minha Evolução

### 8.1 Entrada mínima

```text
PER-008 — Hoje
→ TRN-012
→ PER-012 — Minha Evolução
```

A navegação não presume que existe mudança, progresso ou trajetória reconhecida.

Ausência de evolução reconhecida permanece estado legítimo.

### 8.2 Responsabilidade

`PER-012` deverá futuramente permitir compreender e controlar:

- trajetórias em acompanhamento;
- mudanças reconhecidas ou ainda em avaliação;
- estabilidade, manutenção, oscilação, regressão, recuperação e reorientação quando legitimamente definidas;
- períodos;
- baselines;
- direções;
- observações;
- evidências;
- confiança e incerteza;
- interpretações alternativas;
- contestações e correções;
- histórico;
- privacidade e compartilhamento.

### 8.3 Representação sem score humano

É proibido usar `PER-012` como:

- placar global;
- roda da vida com nota obrigatória;
- ranking;
- percentual geral de evolução da Pessoa;
- diagnóstico médico ou psicológico;
- avaliação espiritual;
- perfil determinístico;
- relatório comercial de vulnerabilidade.

### 8.4 Domínio, trajetória e aspecto

A representação futura deverá separar:

```text
Domínio de Evolução
→ sobre o que a trajetória trata

Trajetória
→ unidade temporal/contextual acompanhada

Aspecto descritivo da mudança
→ natureza complementar observada

Dimensão do Contexto Vivo
→ eixo estrutural contextual relacionado
```

### 8.5 Saída mínima

```text
PER-012
→ TRN-013
→ PER-008
```

Retornar não confirma interpretação, baseline, direção, mudança ou compartilhamento.

## 9. Handoffs contratados

A D5-C1 registra seis transições bidirecionais mínimas:

| ID | Origem | Destino | Estado | Efeito permitido |
|---|---|---|---|---|
| `GKR-TRN-008` | PER-008 | PER-010 | contratada | abrir Meus Objetivos sem mutação automática |
| `GKR-TRN-009` | PER-010 | PER-008 | contratada | retornar a Hoje preservando estado legítimo |
| `GKR-TRN-010` | PER-008 | PER-011 | contratada | abrir Meus Próximos Passos sem iniciar movimento |
| `GKR-TRN-011` | PER-011 | PER-008 | contratada | retornar a Hoje sem concluir/aceitar passo |
| `GKR-TRN-012` | PER-008 | PER-012 | contratada | abrir Minha Evolução sem presumir mudança |
| `GKR-TRN-013` | PER-012 | PER-008 | contratada | retornar a Hoje sem confirmar interpretação |

Essas transições permanecem `contratadas` porque as novas responsabilidades não possuem SVG e não foram examinadas como experiência ponta a ponta.

## 10. Por que não existem handoffs diretos entre PER-010, PER-011 e PER-012 nesta frente

Os contratos funcionais possuem relações legítimas entre Objetivo, Próximo Passo e Evolução, mas relação semântica não equivale automaticamente a navegação direta.

A D5-C1 não cria:

```text
PER-010 ↔ PER-011
PER-011 ↔ PER-012
PER-010 ↔ PER-012
```

Esses handoffs somente poderão ser adicionados quando uma materialização posterior demonstrar decisão, contexto, dados transferidos, retorno, privacidade e necessidade real de navegação direta.

## 11. Papel da Tela Hoje

`PER-008` permanece o hub recorrente mínimo da Pessoa.

A relação governada é:

```text
Hoje
├── direção atual → Meus Objetivos
├── movimento atual → Meus Próximos Passos
└── mudança/continuidade relevante → Minha Evolução
```

Isso não obriga Hoje a exibir três cards permanentes.

A materialização visual futura poderá definir hierarquia adaptativa, desde que:

- não sobrecarregue Hoje;
- não revele conteúdo sensível por padrão;
- não pressione a Pessoa a possuir Objetivo, Passo ou trajetória;
- preserve acesso consciente às superfícies especializadas.

## 12. Gates mínimos

### 12.1 Autenticação

As três superfícies são protegidas e pertencem à Pessoa autenticada.

### 12.2 Autoridade

Navegação não amplia autoridade da Guivos para:

- criar Objetivo;
- confirmar proposta;
- iniciar Próximo Passo;
- reconhecer evolução;
- coletar dado adicional;
- compartilhar conteúdo;
- classificar domínio sensível.

### 12.3 Atualidade

Antes de ação substantiva, a futura materialização deverá distinguir conteúdo atual, possivelmente desatualizado, contestado, retirado ou desconhecido conforme o contrato governante.

### 12.4 Reversibilidade

Voltar para Hoje deve permanecer ação segura e sem penalidade.

## 13. Privacidade e sensibilidade

Os três espaços podem concentrar conteúdo altamente sensível.

Exemplos incluem:

- saúde;
- saúde emocional;
- religião/espiritualidade;
- finanças;
- trabalho;
- família e relacionamentos;
- vulnerabilidades;
- dados de terceiros.

A D5-C1 exige que futuras materializações preservem:

- minimização;
- títulos neutros quando necessário;
- ocultação de área/domínio quando exposição revelar contexto sensível;
- autenticação proporcional;
- controle de compartilhamento;
- distinção entre declarado, observado, inferido e confirmado;
- contestação, correção e retirada;
- ausência de publicidade contextual baseada em vulnerabilidade.

`domain_link` sensível não é autorização de tratamento adicional.

## 14. Relação com Domínios de Evolução

O padrão transversal das três responsabilidades é:

```text
PER-010 — Objetivo
→ 0..n domain_link

PER-011 — Próximo Passo
→ 0..n domain_link

PER-012 — Trajetória de Evolução
→ 0..n domain_link
```

Em todos os casos:

```text
domínio conhecido
≠ domínio obrigatório

domínio candidato
≠ domínio confirmado

mesmo domínio em dois objetos
≠ mesma prioridade
≠ dependência automática
≠ recomendação automática
≠ compartilhamento automático
```

## 15. Contagens após D5-C1

A D5-C1 cria responsabilidades e transições documentais, mas nenhum ativo visual.

| Indicador | Antes | Após D5-C1 |
|---|---:|---:|
| SVGs canônicos | 118 | **118** |
| associações individuais | 118 | **118** |
| perfis de rastreabilidade | 31 | **31** |
| superfícies/estados/fronteiras | 54 | **57** |
| transições documentais | 60 | **66** |
| IDs com referência visual | 42 | **42** |
| responsabilidades sem SVG dedicado | 10 | **13** |
| fronteiras sem tela | 2 | **2** |

A proporção passa a ser `42 de 57` IDs com referência visual.

## 16. Maturidade

Estado das novas responsabilidades:

```text
PER-010 contratado
PER-011 contratado
PER-012 contratado
```

Estado dos novos handoffs:

```text
TRN-008..013 contratados
```

Nenhuma dessas unidades é promovida a:

- programada;
- materializada;
- validada;
- implementada.

## 17. Critérios de aceitação

| Critério | Resultado |
|---|---|
| Objetivos separa Domínio de Evolução de dimensão estrutural do Contexto Vivo | atendido |
| Próximos Passos reconcilia `área da vida` com Área da jornada/domain_link | atendido |
| Minha Evolução separa domínio, dimensão contextual e aspecto descritivo | atendido |
| PER-008 não absorve responsabilidades especializadas | atendido |
| três responsabilidades recebem IDs próprios | atendido |
| entradas e retornos mínimos com Hoje são definidos | atendido |
| navegação não cria mutação funcional automática | atendido |
| sensibilidade e minimização permanecem explícitas | atendido |
| nenhum handoff direto entre 010/011/012 é inventado | atendido |
| nenhum SVG é criado | atendido |
| 118 SVGs permanecem | atendido |
| D6/D7/V5/Engenharia não são iniciadas | atendido |

## 18. Fora do escopo

A D5-C1 não autoriza:

- SVG de `PER-010`;
- SVG de `PER-011`;
- SVG de `PER-012`;
- validação funcional das novas superfícies;
- validação ponta a ponta de `TRN-008..013`;
- handoff direto entre as três novas superfícies;
- alteração de `PER-008` nesta frente;
- D6 — grafo/Neo4j/ontologia física;
- D7 — Public Canon;
- UXA-102/V5;
- Engenharia de Produto ou W0-01;
- implementação de banco, API, eventos ou `domain_link`;
- score humano, roda da vida obrigatória ou ranking de evolução;
- publicidade comportamental por domínio sensível.

## 19. Sequência posterior possível

A D5-C1 cria somente o contrato arquitetural.

Materialização visual deverá ocorrer em autorizações separadas e preferencialmente por responsabilidade:

```text
D5-C1 — contrato arquitetural
→ materialização de Meus Objetivos, quando autorizada
→ materialização de Meus Próximos Passos, quando autorizada
→ materialização de Minha Evolução, quando autorizada
```

A ordem posterior não é autorizada por este documento e poderá ser reavaliada antes de cada frente.

## 20. Estado resultante

Com a D5-C1, a Experience Architecture deixa de tratar `Meus Objetivos`, `Meus Próximos Passos` e `Minha Evolução` apenas como contratos abstratos de Product Architecture e passa a reconhecer suas responsabilidades e handoffs mínimos de forma rastreável.

O resultado é:

```text
PER-008 — Hoje
├── TRN-008 → PER-010 — Meus Objetivos → TRN-009 → PER-008
├── TRN-010 → PER-011 — Meus Próximos Passos → TRN-011 → PER-008
└── TRN-012 → PER-012 — Minha Evolução → TRN-013 → PER-008
```

Tudo permanece documental e contratado. Nenhuma tela nova, implementação ou validação é presumida.
