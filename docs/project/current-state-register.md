---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.36.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-11
depends_on:
  - GKR-FUNDAMENTOS-CONSOLIDADO-001
  - GKR-MODELO-EVOLUCAO-CONSOLIDADO-001
  - GKR-UX-HOME-CONSOLIDATED-001
  - GTM-CONSOLIDATED-001
  - GEM-CONSUMPTION-001
  - GEM-M0-M6-CONSUMPTION-001
  - GKR-GOV-CONSUMPTION-001
related:
  - GEA-000
  - PAS-001
  - GPA-000
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-AUDIT-002
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-101
  - VAL-009
  - VAL-010
  - ADR-007
  - M7.88
normative: true
---

# Registro do Estado Atual

## 1. Finalidade

Este documento apresenta o **estado vigente da Guivos e do Guivos Knowledge Repository em linguagem de consumo**, sem exigir a leitura dos ciclos técnicos que produziram cada decisão.

Detalhes de validação, históricos, contratos, IDs e artefatos especializados permanecem disponíveis no corpus interno do repositório.

---

## 2. Estado geral

| Dimensão | Estado vigente |
|---|---|
| GKR-STATE-001 | **2.36.0** |
| Era arquitetural | GE-2 — Knowledge |
| Marco funcional | **M7.88** |
| Última UXA funcional numerada | **UXA-101** |
| Próxima UXA | **UXA-102/V5 não iniciada** |
| Fundamentos | consolidados |
| Modelo fundamental da evolução | consolidado |
| Arquitetura de produtos | consolidada |
| Guivos Journey | PAS-001 1.0.0 ativo como especificação arquitetural |
| Home Pública | arquitetura estratégica consolidada |
| Home de Organizações e Coletivos | P1→P5 concluídos; gate pré-materialização satisfeito |
| Wireframe da Home Pública | **não integra o processo vigente** |
| Engenharia de Produto | pausada antes de W0-01 |
| Validação de mercado | método governado; resultado real depende de evidência de execução |
| Portugal | candidato condicionado; não operação ativa comprovada |
| Neo4j | tecnologia primária de referência para grafo; implementação não presumida |

---

## 3. Fundamentos vigentes

A Guivos existe para ampliar e acelerar jornadas de evolução por meio de possibilidades relevantes para cada contexto.

Princípios transversais:

- evolução como propósito;
- oportunidade como meio;
- autonomia do participante;
- tecnologia como meio;
- ecossistema como estrutura;
- contexto como requisito de relevância;
- conhecimento como ativo institucional;
- simplicidade para quem utiliza e compreende.

A Guivos não define um caminho universal de sucesso ou evolução.

---

## 4. Participantes

Três tipos estruturais permanecem vigentes:

### Pessoa

Vive sua própria jornada e preserva autoridade sobre seu caminho.

### Organização

Entidade institucional com identidade, autoridade, responsabilidades, recursos, processos e capacidade de atuação.

### Coletivo

Formação voluntária de Pessoas em torno de algo compartilhado, capaz de mobilização, criação e realização coletiva.

Separações obrigatórias:

```text
Pessoa ≠ Organização ≠ Coletivo
participante ≠ produto
Organização ≠ Guivos Business
comunidade ≠ produto Guivos
tipo estrutural ≠ papel contextual
```

---

## 5. Domínios de Evolução do Journey

O baseline canônico possui nove Domínios de Evolução:

1. Saúde e Bem-estar;
2. Trabalho, Carreira e Estudos;
3. Vida Financeira;
4. Empreendedorismo e Projetos;
5. Relacionamentos e Vida Social;
6. Espiritualidade, Propósito e Valores;
7. Viagens, Lazer, Cultura e Novas Experiências;
8. Causas, Voluntariado e Contribuição;
9. Organização e Equilíbrio da Vida.

`Ainda estou descobrindo` é estado transversal de exploração, não um décimo domínio.

Domínio não representa identidade, score, diagnóstico, mérito, objetivo automático ou prova de evolução.

---

## 6. Arquitetura do ecossistema e dos produtos

```text
GUIVOS
│
├── EXPERIÊNCIA E CONTINUIDADE
│   └── Journey
│
├── MANIFESTAÇÕES ESPECIALIZADAS
│   ├── Travel
│   ├── Mall
│   ├── Media
│   ├── Business
│   └── Ads
│
└── INTELIGÊNCIA TRANSVERSAL
    └── Intelligence
```

Nenhum produto isolado é a Guivos.

`Guivos Mall` é o nome canônico. `Marketplace` permanece somente como referência histórica quando necessária à rastreabilidade.

---

## 7. Home Pública

A Home Pública possui duas perspectivas da mesma Guivos.

### Pessoa

> **O que pode se tornar possível para mim?**

A narrativa mostra possibilidades antes de produtos e preserva descoberta, autonomia e confiança.

### Organizações e Coletivos

> **O que podemos tornar possível juntos?**

P1→P5 fecharam:

- macroexperiências;
- Header, Hero e CTAs;
- conteúdo, prova e evidência;
- handoff para Design/UX/UI;
- reauditoria final de prontidão.

O gate documental de pré-materialização foi satisfeito.

Decisão posterior de processo:

> **a Home Pública atual não utiliza wireframe como etapa.**

A antiga materialização low-fidelity da Home não possui autoridade visual corrente e não deve ser utilizada como referência de Design.

Figma, UI e implementação continuam dependendo de decisão própria.

---

## 8. Jornadas e experiência

O Guivos Journey permanece a camada de experiência e continuidade do ecossistema.

Estrutura funcional de referência:

```text
Momento Atual
→ Objetivos / direções
→ Próximos Passos
→ Oportunidades
→ Experiências
→ Evidências e aprendizados
→ novo Momento Atual
```

A jornada não é um funil comercial e aceita pausas, retornos, mudanças de direção, multidomínio e ausência legítima de ação.

Registros técnicos de telas, superfícies e transições permanecem internos e não devem governar a Home Pública quando forem anteriores à arquitetura estratégica consolidada dessa Home.

---

## 9. Planos e monetização

### Pessoa

Free · Plus · Pro.

### Coletivo

Livre · Mobiliza · Impacta · Rede.

### Organização

Conecta · Eleva · Transforma.

Planos e preços são instrumentos econômicos, não níveis de mérito ou evolução.

O estado vigente **não adota uma economia genérica de pontos ou créditos como motor central da evolução**. Incentivos, reconhecimento e recompensas, quando existirem, precisam preservar:

```text
progresso ≠ reconhecimento ≠ recompensa econômica
```

---

## 10. Go-to-Market

Sequência territorial candidata:

```text
Belo Horizonte
→ São Paulo
→ amplificação nacional seletiva
→ Portugal / Lisboa
→ Porto somente após gate
→ novo país somente mediante nova decisão
```

Meta de referência de longo prazo: **1 milhão de Pessoas em M60**.

Esses marcos são planejamento e não prova de execução.

Portugal permanece candidato condicionado. Não estão comprovados por esta documentação piloto executado, entidade local, operação ativa ou equipe local.

---

## 11. Pesquisa e validação

A primeira frente de validação de mercado é B2C.

O método distingue:

```text
método definido
→ instrumento identificado
→ aplicação comprovada
→ base recebida
→ métricas reproduzíveis
→ decisão registrada
```

Documentação metodológica não é tratada como prova de aplicação ou resultado.

O programa de pesquisa do ecossistema possui evidências qualificadas e sínteses preliminares, mas pesquisa não promove automaticamente conclusões à Canon.

---

## 12. Arquitetura, dados e IA

Neo4j permanece tecnologia primária de referência para a camada de grafo.

```text
reference_selected
≠ POC
≠ provisioned
≠ integrated
≠ production
```

Não é correto afirmar, sem evidência própria, que cluster, Aura, GraphRAG, GDS, Power BI ou dados pessoais reais estejam implementados no grafo.

Guivos Intelligence é uma capacidade transversal de compreensão responsável e não equivale a acesso irrestrito a Pessoas ou membros de Coletivos.

---

## 13. Dados, privacidade e autoridade

```text
dado declarado
≠ dado observado
≠ dado inferido
≠ dado confirmado

acesso ao ecossistema
≠ autorização de uso de dados

relação Organização–Coletivo
≠ propriedade ou controle
```

Uma Organização não recebe automaticamente dados de membros de um Coletivo.

Uma inferência não se torna fato apenas porque foi produzida por IA.

---

## 14. Economia e finanças

A arquitetura econômica está mais madura do que a evidência monetária real.

No horizonte M0–M6:

- custos e capacidades possuem estrutura governada;
- parte dos pools possui benchmarks ou fórmulas;
- entradas materiais ainda permanecem `TBD`;
- estrutura de caixa possui prontidão documental;
- prontidão monetária completa ainda não está estabelecida.

Por isso, burn, runway e necessidade definitiva de capital não devem ser apresentados com falsa precisão enquanto faltarem entradas materiais.

---

## 15. Regra de estado operacional

```text
conceito
≠ decisão
≠ arquitetura
≠ materialização
≠ implementação
≠ operação
≠ evidência real
```

O GKR descreve capacidades em maturidade arquitetural superior à maturidade operacional. Essa diferença precisa permanecer explícita.

---

## 16. Navegação do GKR

A navegação pública passa a ser organizada por **assunto**, não pelo histórico do processo de construção.

O menu expõe documentos mestres de leitura e impressão.

Contratos, auditorias, wireframes históricos, validações, changelogs e matrizes permanecem disponíveis internamente quando necessários, mas deixam de funcionar como portas principais de navegação.

> **Complexidade de governança interna não deve ser transferida para quem precisa compreender a Guivos.**

---

## 17. Próximas decisões

Próximos avanços dependem de autorização específica.

Em particular:

- não há autorização automática de materialização visual da Home;
- não há autorização automática de Engenharia de Produto;
- não há promoção automática de mercados candidatos;
- não há promoção automática de preços, projeções ou resultados de pesquisa para fatos realizados.
