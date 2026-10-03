---
id: RP-002-DAF-001
title: Discovery, Admission, Proveniência e Freshness
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-26
normative: false
parent: RP-002
---

# RP-002-DAF-001 — Discovery, Admission, Proveniência e Freshness

## 1. Objetivo

Este documento consolida as conclusões de pesquisa sobre como a Guivos pode descobrir supply real sem depender de cadastro prévio de Organizações e Coletivos, preservando autoridade da fonte, proveniência, disponibilidade, elegibilidade, freshness, conflitos e separação entre presença funcional e relação comercial.

## 2. Princípio central

> **A Guivos não deve depender de Organizações ou Coletivos se cadastrarem primeiro para que uma oportunidade legítima possa ser descoberta.**

Uma oportunidade pode ser identificada a partir de fontes públicas, integrações, APIs, diretórios, plataformas, participantes, profissionais, curadoria ou Intelligence.

O responsável poderá posteriormente reivindicar, verificar e gerenciar aspectos sob sua autoridade.

## 3. Separações obrigatórias

```text
DISCOVERY
≠ ADMISSION
≠ ACTIVE OPPORTUNITY
≠ PRESENTATION
≠ RECOMMENDATION
≠ PARTNERSHIP
≠ SPONSORSHIP
≠ TRANSACTION
```

Consequências:

- descoberta não significa aprovação;
- aprovação funcional não significa relevância individual;
- relevância individual não significa recomendação definitiva;
- parceiro não é automaticamente mais relevante;
- não parceiro não é automaticamente menos relevante;
- patrocinado não é sinônimo de oportunidade funcional prioritária.

## 4. Fontes de discovery

O programa identificou como origens legítimas possíveis:

- fornecedor direto;
- Organização;
- Coletivo;
- profissional;
- participante;
- parceiro;
- curadoria;
- Guivos Intelligence;
- produto especializado Guivos;
- API ou feed;
- sistema público;
- catálogo institucional;
- site oficial;
- fonte pública estruturada;
- plataforma agregadora;
- search/indexação web;
- dataset público.

Nenhuma origem recebe autoridade universal.

## 5. Exemplos de infraestrutura externa de discovery

A investigação considerou referências como:

- APIs de eventos;
- EURES para mercado de trabalho europeu;
- dados estruturados de `Event`, `JobPosting`, `LocalBusiness`, `Organization`, `Product` e outros tipos na web;
- diretórios institucionais e governamentais;
- plataformas de voluntariado, mentoring e educação;
- sistemas de agenda e reservas.

Estrutura de dados não equivale a verdade.

> **Structured ≠ verified. Indexed ≠ available. Listed ≠ eligible.**

## 6. Canonical Opportunity × Source Assertions

Uma oportunidade pode aparecer em múltiplas fontes.

O modelo de pesquisa recomendado é:

```text
CANONICAL OPPORTUNITY
│
├── Source Assertion A
├── Source Assertion B
├── Source Assertion C
└── Provider Claim
```

Cada assertion preserva:

- fonte;
- timestamp;
- campo afirmado;
- valor;
- autoridade;
- confiança;
- validade temporal;
- intermediários;
- transformações;
- conflitos.

A oportunidade canônica não deve apagar automaticamente divergências entre fontes.

## 7. Entity Resolution

Deduplicação é requisito crítico em escala.

Exemplos de duplicação:

- evento no site oficial e em plataforma de tickets;
- vaga no site da empresa, job board e agregador;
- curso no provider e no marketplace educacional;
- mesmo Coletivo listado em diretório, rede social e fonte local.

O sistema precisa responder:

> **Essas representações descrevem o mesmo objeto funcional?**

Sinais possíveis:

- identificador original;
- responsável;
- nome;
- URL canônica;
- datas;
- localização;
- descrição;
- provider IDs;
- relações institucionais.

A resolução automática deve preservar possibilidade de revisão e merge/split posterior.

## 8. Proveniência

Todo fato material precisa ser rastreável até sua origem.

Registro de proveniência recomendado:

```text
fonte original
→ identificador original
→ timestamp de captura
→ intermediários
→ normalizações
→ transformações
→ enriquecimentos
→ correções
→ limitações
→ relação comercial
```

A proveniência responde não apenas “de onde veio?”, mas também:

> **o que aconteceu com este dado até ele chegar à apresentação atual?**

## 9. Autoridade da fonte

Fonte não é sinônimo de autoridade para todo campo.

Exemplos:

### Provider

Pode normalmente confirmar:

- características do programa;
- preço;
- horário;
- requisitos;
- disponibilidade sob sua gestão;
- políticas próprias.

Não pode confirmar:

- relevância absoluta para a Pessoa;
- que a experiência causará transformação;
- que o participante evoluiu;
- que determinada prioridade humana é correta.

### Instituição pública

Pode possuir autoridade sobre seus próprios programas, requisitos e atos oficiais.

Não possui autoridade automática sobre fit individual.

### Participante

Possui autoridade privilegiada sobre:

- preferências declaradas;
- experiência vivida;
- percepção;
- correções de seu contexto;
- contribuição que relata.

Não possui autoridade universal para declarar fato do provider ou resultado de outras Pessoas.

### Intelligence

Pode produzir:

- hipóteses;
- classificação;
- matching;
- detecção de padrões;
- análise de incerteza.

Não deve converter inferência em fato confirmado.

## 10. Provider Claim

Uma oportunidade descoberta sem parceria pode posteriormente ser “claimed” pelo responsável.

Claim pode permitir:

- confirmar identidade;
- corrigir fatos;
- atualizar disponibilidade;
- gerenciar agenda;
- informar requisitos;
- disponibilizar integração;
- fornecer documentação.

Claim não concede autoridade sobre:

- fit individual;
- ranking funcional;
- Evidence Guivos;
- relato da Pessoa;
- classificação de transformação;
- visibilidade garantida.

## 11. Admission

Admission responde:

> **Esta oportunidade possui qualidade mínima suficiente para entrar na camada funcional Guivos?**

Não responde:

> **Esta é a melhor oportunidade para esta Pessoa?**

## 12. Gates de Admission consolidados

```text
G1 EXISTENCE
→ o objeto existe?

G2 IDENTITY
→ sabemos qual oportunidade é?

G3 RESPONSIBLE ACTOR / LEGITIMACY
→ há agente identificável e legitimidade suficiente?

G4 POSSIBILITY MATERIALIZATION
→ existe relação plausível com uma Possibilidade ou Próximo Passo legítimo?

G5 AVAILABILITY
→ existe janela funcional utilizável?

G6 ACCESS
→ modalidade, território e recursos tornam acesso material possível?

G7 ELIGIBILITY
→ a Pessoa atende requisitos conhecidos?

G8 RISK / SENSITIVITY
→ há riscos, regulação ou restrições que exigem tratamento adicional?

G9 COMMERCIAL TRANSPARENCY
→ relações econômicas estão identificadas?

G10 EVIDENCE / INFORMATION SUFFICIENCY
→ sabemos o suficiente para explicar o que sabemos e o que não sabemos?
```

A ordem pode variar operacionalmente, mas as dimensões não devem ser colapsadas em um único score opaco.

## 13. Evidence não é requisito absoluto de existência

Uma oportunidade nova pode ser:

- legítima;
- disponível;
- adequada;
- pouco estudada.

Ela não deve ser automaticamente excluída apenas por falta de Evidence Guivos.

Regra proporcional:

> **quanto maior o risco, a sensibilidade e a força da claim de benefício, maior deve ser o threshold de evidência.**

## 14. Freshness

### 14.1 Princípio

Oportunidade é objeto temporal.

Informação correta ontem pode estar errada hoje.

Campos críticos incluem:

- prazo;
- vagas;
- disponibilidade;
- preço;
- horário;
- local;
- elegibilidade;
- requisitos;
- responsável;
- política de acesso.

### 14.2 Freshness por campo

O programa rejeita um único `last_updated` como suficiente para toda a oportunidade.

Exemplo:

```text
nome do programa
→ estável

preço
→ muda ocasionalmente

vagas
→ alta volatilidade

prazo de inscrição
→ crítico / temporal
```

Cada campo material deve possuir validade proporcional.

## 15. Estado informacional × disponibilidade

Não confundir:

```text
INFORMAÇÃO DESATUALIZADA
≠
OPORTUNIDADE INDISPONÍVEL
```

Se não sabemos se ainda há vagas, o estado correto pode ser:

> **availability = unknown / requires confirmation**

Não:

> **unavailable**

nem:

> **available**

## 16. UNKNOWN é estado legítimo

A investigação consolida um guardrail essencial:

> **não completar campos materiais por inferência quando a fonte não sustenta o valor.**

Se custo, elegibilidade ou vaga é desconhecido:

```text
UNKNOWN
```

A apresentação deve refletir isso.

## 17. Participant Reports como sinais

Participante pode informar:

- “o evento foi cancelado”;
- “o preço estava diferente”;
- “não havia acessibilidade prometida”;
- “a organização disse que não havia vagas”.

Esse relato pode:

- abrir contestação;
- reduzir confiança;
- acionar revalidação;
- pausar apresentação;
- gerar correção.

Não deve automaticamente transformar uma experiência individual em verdade universal.

## 18. Source Coverage

### 18.1 Definição de pesquisa

`Source Coverage` representa o grau em que a Guivos possui fontes suficientes, confiáveis e atuais para observar supply em determinada categoria, território ou Possibilidade.

### 18.2 Por que importa

Sem cobertura de fontes:

```text
“não encontrei oportunidade”
```

pode significar:

```text
“não procurei em lugares suficientes”
```

### 18.3 Gap com confiança

```text
DEMANDA
+
BAIXO SUPPLY OBSERVADO
+
SOURCE COVERAGE ALTO
=
GAP COM MAIOR CONFIANÇA
```

## 19. Opportunity Coverage × Source Coverage

São dimensões distintas.

### Opportunity Coverage

O que foi efetivamente observado e qualificado.

### Source Coverage

Qual a qualidade do sistema de observação.

Essa separação reduz falsos diagnósticos de escassez.

## 20. Demand-led Acquisition

Em vez de capturar toda a internet indiscriminadamente, a investigação propõe uma estratégia orientada a demanda contextual:

```text
Possibility Patterns prioritários
↓
territórios / públicos
↓
fontes confiáveis
↓
supply suficiente
↓
qualidade e freshness
↓
expansão progressiva
```

Isso pode reduzir custo e complexidade de cold start.

## 21. Não parceiro pode ser funcionalmente visível

O programa considera legítimo apresentar supply de fonte pública sem relação comercial quando:

- a fonte permite uso adequado;
- proveniência é preservada;
- fatos são suficientemente confiáveis;
- relacionamento é transparente;
- não há falsa alegação de parceria;
- direitos e limites aplicáveis são respeitados.

## 22. Integração paga e qualidade factual

Uma Organização pode pagar por integração ou capacidade operacional.

Se uma API paga fornece:

- atualização mais frequente;
- agenda;
- vagas;
- cancelamentos;
- elegibilidade mais clara;

isso pode melhorar **qualidade factual**.

Mas:

> **o pagamento pela API não aumenta o fit da oportunidade.**

## 23. Conflitos entre fontes

Quando fontes divergem:

```text
Source A: gratuito
Source B: R$ 50
Provider atual: R$ 80
```

O sistema não deve escolher silenciosamente apenas o valor conveniente.

Deve avaliar:

- autoridade;
- timestamp;
- escopo;
- versão;
- intermediário;
- possibilidade de contato/claim.

## 24. Falha segura

Quando não for possível estabelecer estado confiável, a Guivos deve preferir:

- silêncio contextual;
- `requires confirmation`;
- revalidação;
- apresentação da incerteza;
- alternativa melhor sustentada.

Não deve fabricar disponibilidade.

## 25. Risco operacional principal

Depois da investigação de supply, o principal risco não é “o mundo não tem oportunidades”.

O risco se torna:

> **conseguir normalizar, verificar, atualizar, explicar e contextualizar milhões de objetos heterogêneos sem degradar confiança.**

## 26. Requisitos futuros de engenharia derivados pela pesquisa

Sem autorizar implementação, o `RP-002` identifica necessidades prováveis:

- canonical opportunity identity;
- source assertion model;
- provenance graph;
- field-level validity;
- freshness rules;
- source authority mapping;
- dedup/entity resolution;
- contest/revalidation lifecycle;
- gap/source coverage metrics;
- provider claim;
- safe fallback;
- commercial relation separation.

Qualquer handoff para Engenharia deverá partir dos contratos canônicos pertinentes, não diretamente deste Research Program.
