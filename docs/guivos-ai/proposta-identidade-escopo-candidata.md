---
id: GKR-GAI-IDENTIDADE-ESCOPO-CANDIDATO-001
title: Guivos AI — Exame e proposta candidata de identidade e escopo
status: proposed_non_normative
version: 0.1.0
owner: Guivos — proposta para apreciação da Direção
last_updated: 2026-11-13
normative: false
related:
  - GAI-001
  - GAI-002
  - GIA-000
  - GIA-COG-001
  - GPA-006
  - ADR-008
---

# Guivos AI — Exame e proposta candidata de identidade e escopo

> **DOCUMENTO CANDIDATO — NÃO NORMATIVO.** Este exame não cria unidade de negócio, produto autônomo, autoridade arquitetural concorrente, implantação, seleção de provedores ou permissão de uso de dados reais. Não altera fontes superiores nem autoriza publicação funcional.

## 1. Objetivo e método

Confrontar os documentos de identidade de produto, inteligência do ecossistema e arquitetura cognitiva para separar **afirmações sustentadas**, **formulação candidata** e **decisões pendentes**. A existência de seção própria no menu do GKR é medida de navegação, não decisão sobre categoria de produto.

## 2. Autoridades examinadas

| Fonte | Estado e contribuição | Consequência para Guivos AI |
| --- | --- | --- |
| [GPA-006](../product-architecture/intelligence.md) | Produto Guivos Intelligence, com identidade e responsabilidades próprias | Guivos AI não é automaticamente o mesmo produto |
| [GAI-001](../intelligence-architecture/knowledge-model.md) | Modelo de conhecimento consolidado; fontes, aprendizado e recomendações | Fundamenta princípios de IA como meio da inteligência |
| [GAI-002](../intelligence-architecture/manifesto.md) | Manifesto consolidado da Inteligência do Ecossistema | Orienta finalidade, autonomia e explicabilidade |
| [GIA-000](../intelligence-architecture/index.md) | Arquitetura Intelligence ativa | Organiza modelos técnicos subordinados à autoridade do produto |
| [GIA-COG-001](../intelligence-architecture/cognitive-reference-architecture.md) | Arquitetura cognitiva ativa/normativa, conceitual e lógica | Governa referência cognitiva; não comprova operação |
| [ADR-008](../adr/ADR-008-cognitive-reference-architecture-placement-and-ownership.md) | Placement e ownership aprovados | GIA-COG é subordinada à GIA, não novo produto ou camada paralela |
| [Reconciliação temporal](../experience-architecture/home-intelligence-guivos-ai-temporal-reconciliation-proposed.md) | Estudo proposto/não normativo | Três perspectivas temporais ainda não são obrigação técnica |
| [Diagnóstico das Homes](../experience-architecture/public-homes-guivos-ai-temporal-compatibility-diagnostic.md) | Diagnóstico proposto/não normativo | Diferencia Guivos AI (capacidade/arquitetura) de Intelligence (produto/superfície) |

## 3. Achados sustentados

1. A inteligência artificial é **meio técnico**, não finalidade de evolução ou autoridade de decisão, conforme GAI-001 e GAI-002.
2. Inteligência do Ecossistema Guivos não se reduz a assistente, chatbot, LLM, banco de dados, grafo ou dashboard.
3. Guivos Intelligence conserva a autoridade de produto transversal; algoritmos, modelos e outras tecnologias não a substituem.
4. A arquitetura cognitiva possui placement definido em GIA e fronteiras de processamento, evidência, autorização e divulgação.
5. As lentes retrospectiva/contextual/prospectiva constam de estudos candidatos; não representam, por si, motores implementados.
6. Não há, entre as fontes examinadas, decisão suficiente para declarar Guivos AI uma **unidade de negócio** ou um **novo produto especializado independente**.

## 4. Definição candidata para discussão — não aprovada

> **Guivos AI** pode designar o conjunto governado de capacidades e mecanismos de inteligência artificial utilizados para apoiar a compreensão contextual, a organização de conhecimentos e evidências, a interpretação de relações e a apresentação de possibilidades explicáveis no ecossistema Guivos, sempre subordinado às autoridades de produto, arquitetura, dados, governança e participantes.

Esta redação é **hipótese editorial de identidade**, não alteração normativa. Sua adoção, mudança ou rejeição depende de decisão expressa.

### O que a hipótese não autoriza

- Instituir novo produto, serviço, camada soberana, equipe ou unidade comercial.
- Atribuir à Guivos AI titularidade sobre dados, decisões ou conhecimento canônico.
- Criar funções agentivas autônomas ou executar ações sem contratos e autorizações específicas.
- Selecionar GPT, Claude, Gemini, Neo4j ou qualquer infraestrutura como padrão vinculante.
- Declarar funcionalidades tecnicamente prontas, disponíveis ou em operação.

## 5. Responsabilidades candidatas para análise, sem ativação

| Eixo | Possibilidade em exame | Limite não negociável |
| --- | --- | --- |
| Compreensão | Assistir leitura de contextos e relações | Não inventar fatos nem decisões |
| Conhecimento | Apoiar recuperação e síntese de evidências | Preservar origem, qualidade e autoridade |
| Temporalidade | Relacionar registros, estado atual e cenários | Projeção não é certeza |
| Interação | Explicar análises e identificar perguntas relevantes | Participante pode contestar e corrigir |
| Orquestração | Integrar capacidades de IA mediante contratos futuros | Sem escolha antecipada de provedor, agente ou stack |
| Aprendizado | Melhorar interpretações dentro de regras válidas | Sem uso implícito de dados privados ou treinamento irrestrito |

## 6. Fronteiras candidatas

```text
FINALIDADE DO ECOSSISTEMA
  ├─ AUTORIDADES DE PRODUTO (ex.: GPA-006)
  ├─ INTELLIGENCE ARCHITECTURE (GIA / GAI / GIA-COG)
  ├─ CONHECIMENTO / EVIDÊNCIA / GRAFO / DADOS
  ├─ PLATAFORMA / IDENTIDADE / SEGURANÇA / GOVERNANÇA
  └─ CAPACIDADES DE IA — hipótese de agrupamento “Guivos AI”
          ↓
     OUTPUT ELEGÍVEL AO CONSUMIDOR
          ↓
     DECISÃO HUMANA / DOMÍNIO RESPONSÁVEL
```

O diagrama é **mapa argumentativo candidato**, não novo organograma normativo.

## 7. Quadro de lacunas e decisões pendentes

| ID | Questão para decisão | Alternativas ou critério | Estado |
| --- | --- | --- | --- |
| GAI-P01 | Qual a identidade formal de Guivos AI? | Marca/capacidade técnica; serviço transversal; outro enquadramento fundamentado | Pendente |
| GAI-P02 | Qual o limite exato perante Guivos Intelligence? | Delimitar responsabilidades sem duplicar GPA-006 | Pendente |
| GAI-P03 | Quais interfaces e experiências podem usar o nome? | Definir contexto, público, finalidade e consentimento | Pendente |
| GAI-P04 | Qual a autonomia de ações, agentes e automações? | Matriz por risco, permissão, auditoria e confirmação humana | Pendente |
| GAI-P05 | Como ficam provedores, roteamento, avaliação e fallback? | Contratos técnicos posteriores; evitar escolha prematura | Pendente |
| GAI-P06 | Qual memória pode existir, onde, e para quem? | Segregação, retenção, revogação, correção e proveniência | Pendente |
| GAI-P07 | Como mensurar qualidade e segurança? | Evidência, incerteza, explicabilidade, vieses e abstenção | Pendente |
| GAI-P08 | Três perspectivas temporais entram no contrato? | Examinar valor sem tornar etapas ou motores obrigatórios | Pendente |
| GAI-P09 | Quais gates autorizariam protótipo, teste e produção? | Decisões explícitas, ambientes e dados permitidos | Pendente |

## 8. Recomendação documental para apreciação

**Recomenda-se examinar primeiro GAI-P01 e GAI-P02**, pois o enquadramento determina o vocabulário, as fronteiras com Intelligence e o formato das demais especificações.

A recomendação é analítica e não aprova a definição da seção 4. Após decisão, atualizar somente os documentos afetados por mudança autorizada, mantendo encadeamento de proveniência.

## 9. Controle de mudança

- **Status:** `proposed_non_normative`.
- **Integração em main:** não autorizada por este documento.
- **Promoção normativa:** não autorizada.
- **Implantação, teste e produção:** não autorizados.
- **Próximo gate:** apreciação expressa da Direção quanto a GAI-P01/GAI-P02 e à redação candidata.
