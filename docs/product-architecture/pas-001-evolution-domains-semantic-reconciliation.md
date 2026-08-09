---
id: PAS-001-DOMAIN-RECON-001
title: Reconciliação Semântica Pós-Publicação dos Domínios de Evolução no PAS-001
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
parent: PAS-001
normative: true
related:
  - GPA-000
  - GPA-001
  - PAS-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-FOUNDATION-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - PAS-001-EXP-CONTRACT-001
  - PAS-001-EC-FOUNDATION-001
  - PAS-001-EC-CONTRACT-001
---

# PAS-001-DOMAIN-RECON-001 — Reconciliação Semântica Pós-Publicação dos Domínios de Evolução no PAS-001

> **Decisão normativa:** `PAS-001-DOMAIN-MODEL-001` passa a ser autoridade ortogonal pós-publicação para interpretação do `PAS-001 1.0.0`, de `GPA-000` e das capacidades do Guivos Journey. Esta reconciliação promove o vocabulário `JED-001..JED-009` sem reescrever retroativamente a release auditada, sem alterar a contagem histórica de 54 extensões e sem autorizar implementação técnica, UX adicional, modelo físico de grafo ou tratamento de dados não previamente autorizado.

## 1. Finalidade

Esta autoridade executa a reconciliação semântica D1–D3 após a canonização dos Domínios de Evolução.

Ela resolve três necessidades:

1. **D1 — federação pós-publicação:** estabelecer como `PAS-001 1.0.0` e `GPA-000` devem ser lidos após a aprovação de `PAS-001-DOMAIN-MODEL-001`;
2. **D2 — propagação entre capacidades:** tornar explícito como os Domínios de Evolução se relacionam com Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas e Experiências;
3. **D3 — reconciliação terminológica de Evolução Contínua:** separar Domínio de Evolução, dimensão estrutural do Contexto Vivo e aspecto descritivo da mudança.

Esta autoridade não altera a responsabilidade funcional das nove capacidades do Journey.

## 2. Natureza pós-publicação e preservação histórica

O `PAS-001 1.0.0` foi publicado após auditoria, validação de release e inventário de **54 extensões especializadas**.

Essa contagem é histórica e permanece verdadeira para a release que foi auditada.

`PAS-001-DOMAIN-MODEL-001` e esta reconciliação surgiram posteriormente e não deverão ser utilizadas para afirmar retroativamente que a publicação original possuía 55, 56 ou outra quantidade de extensões auditadas.

A leitura correta passa a ser:

```text
PAS-001 1.0.0 publicado
+ nove contratos finais e 54 extensões da release auditada
+ PAS-001-DOMAIN-MODEL-001 como autoridade ortogonal pós-publicação
+ PAS-001-DOMAIN-RECON-001 como autoridade de reconciliação semântica pós-publicação
```

Portanto:

```text
adição pós-publicação
≠ alteração retroativa da evidência de release
≠ reexecução automática da auditoria histórica
≠ nova publicação do PAS-001
```

## 3. Regra de precedência

Para assuntos relacionados à taxonomia e associação de áreas da jornada:

1. `PAS-001-DOMAIN-MODEL-001` governa definição, IDs, fronteiras, multidomínio, sensibilidade, classificação e `domain_link`;
2. esta reconciliação governa a compatibilização desse modelo com `PAS-001`, `GPA-000` e capacidades especializadas;
3. os contratos especializados continuam governando estados, transições, eventos, integrações, KPIs, guardrails, cenários e regras próprias da capacidade;
4. onde uma expressão histórica como `dimensão` puder ser confundida com Domínio de Evolução, aplica-se a desambiguação desta reconciliação;
5. nenhum vínculo de domínio transfere autoridade entre capacidades.

Em caso de conflito semântico específico sobre Domínios de Evolução, prevalece a autoridade mais recente e especializada, sem apagar a evidência histórica da formulação anterior.

## 4. D1 — Federação do eixo de Domínios no PAS-001 e GPA-000

### 4.1 PAS-001

O `PAS-001` continua definindo **como** o Journey opera por meio de suas nove capacidades:

```text
Captura de Contexto
→ Contexto Vivo
→ Objetivos
→ Eventos de Vida
→ Próximos Passos
→ Oportunidades Ativas
→ Intervenções Contextuais
→ Experiências
→ Evolução Contínua
```

`PAS-001-DOMAIN-MODEL-001` adiciona o eixo ortogonal que responde **sobre o que** uma jornada está tratando.

A arquitetura consolidada deve ser lida como dois eixos independentes e cruzáveis:

```text
Eixo funcional: como o Journey opera
×
Eixo de domínio: sobre qual área a jornada trata
```

Os nove Domínios de Evolução são:

| ID | Domínio canônico |
|---|---|
| `JED-001` | Saúde e Bem-estar |
| `JED-002` | Trabalho, Carreira e Estudos |
| `JED-003` | Vida Financeira |
| `JED-004` | Empreendedorismo e Projetos |
| `JED-005` | Relacionamentos e Vida Social |
| `JED-006` | Espiritualidade, Propósito e Valores |
| `JED-007` | Viagens, Lazer, Cultura e Novas Experiências |
| `JED-008` | Causas, Voluntariado e Contribuição |
| `JED-009` | Organização e Equilíbrio da Vida |

`Ainda estou descobrindo` permanece estado legítimo de exploração e **não é décimo domínio**.

`Outra área` permanece mecanismo de extensibilidade e captura de necessidade ainda não mapeada, sem reclassificação silenciosa.

### 4.2 GPA-000 — Arquitetura de Produtos

Para fins de Arquitetura de Produtos, a descrição do Guivos Journey em `GPA-000` passa a ser interpretada conjuntamente com:

- `GPA-001 — Guivos Journey`;
- `PAS-001 — Guivos Journey Product Architecture Specification`;
- `PAS-001-DOMAIN-MODEL-001`;
- `PAS-001-DOMAIN-RECON-001`.

O eixo de Domínios de Evolução pertence ao **Guivos Journey / Experience Layer** como vocabulário transversal da jornada e não cria um oitavo Produto Especializado, uma décima capacidade ou uma nova camada arquitetural.

```text
Domínio de Evolução
≠ produto
≠ capacidade
≠ plano comercial
≠ participante
≠ tecnologia
```

### 4.3 Mapa arquitetural reconciliado

```text
Ecossistema Guivos
└── Experience Layer
    └── Guivos Journey
        ├── nove capacidades funcionais
        └── eixo transversal de Domínios de Evolução
            ├── JED-001 ... JED-009
            ├── multidomínio
            ├── Ainda estou descobrindo
            └── Outra área / other_unmapped
```

O eixo pode ser consumido por Guivos Intelligence e por produtos especializados somente dentro da autoridade, finalidade, proteção e handoff aplicáveis.

## 5. Contrato transversal mínimo

Quando uma capacidade precisar relacionar seu objeto funcional a uma área da jornada, deverá utilizar semanticamente o contrato definido por `PAS-001-DOMAIN-MODEL-001`:

```yaml
domain_link:
  domain_id: JED-001..JED-009 | other_unmapped | null
  subdomain: string_or_null
  participant_type: person | collective | organization
  relation_type: primary | secondary | contextual | candidate
  authority: participant_declared | authorized_source | guivos_candidate | professional | institutional
  confirmation_state: candidate | declared | confirmed | contested | withdrawn | unknown
  confidence: low | moderate | high | unknown
  sensitive: true | false | context_dependent
  purpose: string
  source_ref: string_or_null
  valid_from: datetime_or_null
  valid_until: datetime_or_null
  notes: string_or_null
```

Este contrato continua **semântico**.

Ele não declara:

- coluna de banco de dados;
- tabela;
- nó ou relação física de grafo;
- API;
- payload técnico definitivo;
- indexação;
- evento de software;
- UI obrigatória;
- coleta automática de dados;
- consentimento;
- implementação.

## 6. Regras transversais D2

As capacidades reconciliadas deverão preservar as seguintes invariantes:

1. objeto funcional sem domínio conhecido continua válido quando o contrato da capacidade permitir;
2. ausência de domínio não representa ausência de necessidade, objetivo, evento, movimento, oportunidade, experiência ou evolução;
3. um objeto pode possuir `0..n` associações de domínio;
4. multidomínio não exige escolha artificial de um único domínio principal;
5. relação `candidate` não se torna `confirmed` por repetição, probabilidade ou conveniência técnica;
6. declaração direta legítima do participante prevalece sobre inferência incompatível;
7. domínio contestado, retirado ou vencido não poderá permanecer sendo tratado como confirmação vigente;
8. domínio não define identidade, mérito, valor, diagnóstico ou prioridade humana;
9. domínio compatível não comprova relevância, progresso, resultado ou evolução;
10. informação sensível não adquire nova finalidade apenas por possuir `domain_link`;
11. vínculo de domínio não amplia consentimento, base, autorização, acesso ou compartilhamento;
12. histórico legítimo deve ser preservado sem reclassificação silenciosa.

## 7. D2 — Contexto Vivo

### 7.1 Oito dimensões estruturais permanecem válidas

As oito dimensões estruturais do Contexto Vivo permanecem:

- Identidade;
- Momento;
- Direção;
- Capacidades;
- Restrições;
- Preferências;
- Relacionamentos;
- Evolução.

Elas descrevem **como o contexto é representado**.

Os Domínios de Evolução descrevem **qual área da jornada está em foco**.

Portanto:

```text
Dimensão do Contexto Vivo ≠ Domínio de Evolução
```

Exemplos:

```text
JED-003 Vida Financeira
→ Momento: situação atual relevante
→ Direção: o que o participante deseja organizar
→ Capacidades: recursos e conhecimentos disponíveis
→ Restrições: obrigações ou limites relevantes
→ Preferências: formas aceitáveis de apoio
```

```text
JED-006 Espiritualidade, Propósito e Valores
→ Identidade: somente quando legitimamente declarada e relevante
→ Momento: contexto atual
→ Direção: prática, reflexão ou participação desejada
→ Relacionamentos: vínculos voluntariamente relevantes
```

Nenhum exemplo autoriza inferência de condição sensível não declarada.

### 7.2 Associação no Contexto Vivo

O Contexto Vivo poderá representar `0..n` domínios atualmente relevantes por meio de associações semânticas equivalentes a `domain_link`.

A associação deverá permanecer:

- contextual;
- temporal;
- revisável;
- contestável;
- proporcional à finalidade;
- separada da identidade permanente.

```text
domínio atualmente relevante
≠ identidade do participante
≠ prioridade permanente
≠ preferência comercial
```

### 7.3 Autoridade preservada

Guivos Intelligence poderá sugerir um domínio candidato, mas Contexto Vivo não deverá promover esse candidato silenciosamente a declaração ou confirmação.

Mudança de domínio não apaga estados históricos legítimos das oito dimensões.

## 8. D2 — Objetivos

### 8.1 Associação

Um Objetivo poderá possuir `0..n` `domain_link`.

Exemplos:

```text
Objetivo: correr primeira prova de 5 km
→ JED-001 Saúde e Bem-estar
```

```text
Objetivo: melhorar renda para financiar uma viagem internacional
→ JED-003 Vida Financeira
+ JED-007 Viagens, Lazer, Cultura e Novas Experiências
```

### 8.2 Autoria preservada

```text
domínio identificado
≠ objetivo criado
≠ objetivo confirmado
```

O domínio não concede à Guivos autoridade para inventar objetivo, prioridade, horizonte ou critério de sucesso.

Um Objetivo pode existir sem domínio classificado.

### 8.3 Ciclo de vida e histórico

Mudança, contestação ou retirada de um `domain_link`:

- não encerra automaticamente o Objetivo;
- não altera automaticamente sua prioridade;
- não converte objetivo pessoal em institucional;
- não apaga a associação histórica legítima;
- exige propagação controlada somente quando decisões dependentes utilizarem aquela classificação.

## 9. D2 — Eventos de Vida

### 9.1 Desambiguação de “dimensões afetadas”

Quando os contratos históricos de Eventos de Vida utilizarem a expressão `dimensões afetadas`, ela deverá ser interpretada como referência às **dimensões estruturais do Contexto Vivo**, salvo quando o texto declarar expressamente outro significado.

Domínios de Evolução afetados constituem relação separada.

A unidade funcional reconciliada poderá preservar, quando aplicável:

```text
Evento de Vida
├── dimensões do Contexto Vivo afetadas: 0..n
└── domain_links / Domínios de Evolução relacionados ou afetados: 0..n
```

### 9.2 Impacto avaliado, não presumido

Exemplo:

```text
Evento: mudança de cidade

possíveis dimensões do Contexto Vivo afetadas:
- Momento
- Restrições
- Relacionamentos
- Direção

possíveis Domínios de Evolução afetados, conforme contexto e evidência:
- JED-002 Trabalho, Carreira e Estudos
- JED-003 Vida Financeira
- JED-005 Relacionamentos e Vida Social
- JED-009 Organização e Equilíbrio da Vida
```

A ocorrência da mudança de cidade não confirma automaticamente nenhum desses impactos.

### 9.3 Sensibilidade

Um Evento de Vida não deverá utilizar o domínio como atalho para inferir:

- condição de saúde;
- situação financeira;
- estado emocional;
- religião;
- vulnerabilidade;
- significado pessoal.

Cada inferência continua dependente de finalidade, base, autoridade e proteção adequadas.

## 10. D2 — Próximos Passos

### 10.1 Associação

Um Próximo Passo proposto ou confirmado poderá possuir `0..n` `domain_link`.

O vínculo ajuda a explicar em qual área aquele movimento pode contribuir, mas não substitui:

- contexto atual;
- direção;
- objetivo;
- restrições;
- capacidades;
- dependências;
- risco;
- autoridade;
- confirmação aplicável.

### 10.2 Separações obrigatórias

```text
Próximo Passo em JED-001
≠ prova de melhora de saúde

Próximo Passo em JED-003
≠ prova de melhora financeira

Próximo Passo em JED-006
≠ prova de evolução espiritual
```

Executar, concluir, cancelar ou substituir um Próximo Passo não deverá alterar automaticamente a avaliação de Evolução Contínua.

## 11. D2 — Oportunidades Ativas

### 11.1 Associação e relevância

Uma Oportunidade Ativa poderá possuir `0..n` associações de domínio.

Essas associações poderão apoiar busca, filtros, explicação e avaliação contextual.

Porém:

```text
domínio compatível ≠ oportunidade relevante
```

Relevância continua dependente, conforme aplicável, de:

- Momento;
- Objetivos;
- Próximos Passos;
- Restrições;
- Preferências;
- localização ou modalidade;
- temporalidade;
- disponibilidade;
- elegibilidade;
- risco;
- custo;
- autoridade;
- finalidade;
- sensibilidade;
- proveniência;
- relações comerciais.

### 11.2 Publicidade e patrocínio

```text
patrocínio
≠ domínio mais relevante
≠ confirmação de domínio
≠ prioridade orgânica
```

Pagamento não poderá criar, elevar ou confirmar afinidade de domínio.

Domínio sensível não autoriza publicidade comportamental.

### 11.3 Fonte da classificação

A oportunidade poderá possuir classificação de domínio derivada de fonte institucional, curadoria, declaração autorizada ou Guivos Intelligence candidata.

A fonte e o estado de confirmação deverão permanecer distinguíveis quando materialmente relevantes.

## 12. D2 — Experiências

### 12.1 Associação

Uma Experiência poderá possuir `0..n` `domain_link`, conforme o contexto legitimamente reconhecido.

Exemplo:

```text
Experiência: participação em curso profissional
→ JED-002 Trabalho, Carreira e Estudos
```

Uma mesma experiência poderá atravessar mais de um domínio.

### 12.2 Experiência não comprova evolução

```text
experiência relacionada ao domínio
≠ resultado positivo
≠ transformação
≠ evolução no domínio
```

Presença, compra, participação, conclusão, satisfação ou recorrência não deverão ser usadas isoladamente para concluir evolução.

### 12.3 Significado e autoridade

O significado da experiência para a trajetória deve preservar:

- declaração do participante;
- evidências;
- contexto;
- limitações;
- temporalidade;
- incerteza;
- autoridade aplicável.

## 13. Intervenções Contextuais — preservação de fronteira

Intervenções Contextuais não integra o escopo documental principal de D2 porque a auditoria não encontrou ambiguidade estrutural equivalente à das demais capacidades.

Ainda assim, aplica-se a regra de `PAS-001-DOMAIN-MODEL-001`:

- domínio poderá explicar contexto da manifestação;
- domínio não amplia legitimidade para interromper;
- domínio não cria urgência;
- domínio sensível exige proteção reforçada;
- patrocínio não compra direito de intervenção.

Nenhum novo contrato de Intervenções é criado por esta reconciliação.

## 14. D3 — Evolução Contínua

### 14.1 Problema reconciliado

A formulação histórica de Evolução Contínua utiliza `dimensão` em pelo menos dois sentidos potencialmente confundíveis:

1. campo genérico preservado pela Trajetória de Evolução;
2. seção `Dimensões iniciais`, com uma lista heterogênea de recortes como profissional, financeira, física, cognitiva, comportamental, cultural, espiritual, cidadania e outros.

Após a canonização de `PAS-001-DOMAIN-MODEL-001`, essa terminologia não deverá ser interpretada como uma taxonomia concorrente aos nove Domínios de Evolução nem como substituta das oito dimensões estruturais do Contexto Vivo.

### 14.2 Vocabulário reconciliado

Passam a existir três conceitos explicitamente distintos:

| Conceito | Pergunta respondida | Autoridade |
|---|---|---|
| **Domínio de Evolução** | sobre qual área a trajetória está tratando? | `PAS-001-DOMAIN-MODEL-001` |
| **Dimensão do Contexto Vivo** | qual eixo estrutural do contexto está envolvido? | contratos de Contexto Vivo |
| **Aspecto descritivo da mudança** | que natureza ou recorte complementar ajuda a descrever a mudança? | Evolução Contínua, subordinado aos dois anteriores |

Regra:

```text
Domínio de Evolução
≠ Dimensão do Contexto Vivo
≠ Aspecto descritivo da mudança
```

### 14.3 Trajetória de Evolução reconciliada

A unidade funcional `Trajetória de Evolução` continua válida.

O campo histórico genérico `dimensão` deverá ser interpretado de forma desambiguada e, em novos artefatos derivados, preferencialmente representado por estruturas separadas:

```yaml
evolution_trajectory_semantics:
  domain_links: 0..n
  context_dimensions: 0..n
  change_aspects: 0..n
  direction: existing_contract
  baseline: existing_contract
  period: existing_contract
  observed_states: existing_contract
  changes: existing_contract
  related_events: existing_contract
  related_experiences: existing_contract
  related_objectives: existing_contract
  evidence: existing_contract
  interpretations: existing_contract
  confidence: existing_contract
  uncertainty: existing_contract
  contributing_factors: existing_contract
  contestations: existing_contract
  corrections: existing_contract
  permissions: existing_contract
  history: existing_contract
```

Essa representação é semântica e não constitui esquema técnico.

### 14.4 Reclassificação normativa da antiga seção “Dimensões iniciais”

A lista histórica deverá ser lida, a partir desta reconciliação, como **Aspectos descritivos iniciais da mudança**, e não como conjunto canônico de Domínios de Evolução.

A lista é preservada semanticamente:

- pessoal;
- relacional;
- familiar;
- social;
- comunitária;
- educacional;
- profissional;
- financeira;
- física;
- emocional declarada;
- cognitiva;
- comportamental;
- cultural;
- ambiental;
- espiritual ou religiosa declarada;
- autonomia;
- acessibilidade;
- participação;
- cuidado;
- cidadania.

Esses termos poderão ajudar a descrever a natureza de uma mudança quando houver finalidade e clareza, mas não deverão competir com `JED-001..JED-009`.

Exemplo:

```text
Domínio:
JED-002 Trabalho, Carreira e Estudos

Subárea:
transição de carreira

Dimensões do Contexto Vivo relevantes:
Momento + Direção + Capacidades + Restrições

Aspectos descritivos da mudança:
profissional + cognitiva + comportamental

Trajetória:
reorientação profissional
```

### 14.5 Multidomínio em Evolução Contínua

Uma Trajetória poderá referenciar mais de um domínio.

Exemplo:

```text
Trajetória: preparação para mudança de cidade e trabalho
→ JED-002 Trabalho, Carreira e Estudos
→ JED-003 Vida Financeira
→ JED-005 Relacionamentos e Vida Social
→ JED-009 Organização e Equilíbrio da Vida
```

Nenhum domínio precisa ser reduzido a outro.

### 14.6 Domínio não é score de evolução

Evolução Contínua não deverá produzir por padrão:

- nota global da pessoa;
- score obrigatório por domínio;
- média dos nove domínios;
- ranking entre participantes;
- “nível de evolução” humano;
- pontuação espiritual, financeira, social ou de saúde.

```text
mais evidências em um domínio
≠ mais valor humano

mais atividade em um domínio
≠ maior evolução

mais domínios ativos
≠ jornada melhor
```

### 14.7 Direção e significado

Evolução em um domínio continua podendo representar:

- descobrir;
- compreender;
- iniciar;
- aprender;
- desenvolver;
- fortalecer;
- organizar;
- adaptar;
- recuperar;
- manter;
- consolidar;
- experimentar;
- concluir;
- reorientar;
- pausar;
- abandonar legitimamente;
- reduzir impacto de uma restrição;
- reconhecer ausência de mudança;
- permanecer inconclusiva.

O significado deverá respeitar direção, baseline, evidência, autoridade e interpretação legítima do participante.

## 15. Compatibilidade por participante

Os `JED-*` pertencem ao vocabulário comum do Journey, mas sua interpretação permanece específica para Pessoa, Coletivo e Organização.

```text
trajetória da Pessoa
≠ trajetória do Coletivo
≠ trajetória da Organização
≠ indicador agregado
≠ impacto social amplo
```

Nenhuma capacidade poderá utilizar domínio compartilhado para transferir automaticamente resultados entre titulares.

Exemplo:

```text
Organização executa programa JED-002
≠ Pessoa evoluiu em JED-002
```

```text
Coletivo conclui ação JED-008
≠ todos os participantes evoluíram individualmente
```

## 16. Sensibilidade e finalidade

A associação de domínio não reduz as exigências de proteção.

Exigem cuidado reforçado quando aplicável:

- saúde;
- deficiência;
- condição emocional;
- religião e espiritualidade;
- finanças;
- emprego;
- família;
- sexualidade quando emergir no contexto;
- violência, trauma ou luto;
- localização protegida;
- crianças e adolescentes;
- vulnerabilidade.

Proibições preservadas:

- publicidade comportamental baseada em domínio sensível;
- manipulação de preço;
- ranking humano;
- discriminação;
- exposição indevida;
- inferência de mérito, fé, saúde, solvência ou valor pessoal;
- reutilização para finalidade incompatível.

## 17. Compatibilidade com Guivos Intelligence

Guivos Intelligence poderá continuar:

- classificando domínios como candidatos;
- sugerindo relações multidomínio;
- explicando a classificação;
- preservando confiança e incerteza;
- identificando `other_unmapped`;
- reconhecendo que o participante ainda está descobrindo.

Esta reconciliação não amplia sua autoridade.

```text
classificação por IA
≠ confirmação
≠ objetivo
≠ diagnóstico
≠ prioridade
≠ evolução
```

## 18. Regras de propagação e correção

Quando uma associação de domínio for criada, modificada, contestada, retirada ou expirar:

1. a origem e autoridade deverão permanecer rastreáveis;
2. consumidores materiais deverão receber correção proporcional quando a classificação tiver influenciado uma decisão vigente;
3. histórico legítimo não deverá ser sobrescrito silenciosamente;
4. conteúdo meramente arquivado não deverá ser reescrito para parecer que sempre utilizou a taxonomia atual;
5. correção de domínio não altera automaticamente fatos, eventos, experiências ou resultados;
6. classificações derivadas deverão ser reavaliadas quando dependerem materialmente da associação alterada;
7. ausência posterior de domínio não transforma o registro original em inválido.

## 19. Critérios de conformidade D1–D3

Uma futura edição de artefato do PAS-001 estará semanticamente conforme a esta reconciliação quando:

- utilizar `JED-001..JED-009` para Domínios de Evolução;
- preservar `Ainda estou descobrindo` como estado não taxonômico;
- preservar `Outra área` / `other_unmapped` sem encaixe silencioso;
- distinguir domínio de dimensão do Contexto Vivo;
- não reutilizar a antiga lista de Evolução Contínua como taxonomia concorrente;
- permitir multidomínio quando necessário;
- preservar autoridade e confirmação;
- não transformar domínio em score;
- não ampliar consentimento ou finalidade;
- manter histórico e contestação;
- não inferir implementação técnica.

## 20. Impacto documental desta decisão

Esta reconciliação possui efeito normativo prospectivo sobre a leitura de:

- `GPA-000`;
- `PAS-001`;
- `PAS-001-CV-CONTRACT-001`;
- `PAS-001-OBJ-CONTRACT-001`;
- `PAS-001-EV-FOUNDATION-001`;
- `PAS-001-EV-CONTRACT-001`;
- `PAS-001-PP-CONTRACT-001`;
- `PAS-001-OA-CONTRACT-001`;
- `PAS-001-EXP-CONTRACT-001`;
- `PAS-001-EC-FOUNDATION-001`;
- `PAS-001-EC-CONTRACT-001`.

Ela não altera retroativamente seus front matters, versões históricas ou evidências de auditoria.

Uma futura revisão consolidada desses documentos deverá incorporar o vocabulário desta autoridade sem apagar o histórico anterior.

## 21. Fora de escopo — D4 a D7

Esta frente **não** executa:

### D4 — jornadas integradas

Não altera:

- Jornada da Pessoa;
- Jornada do Coletivo;
- Jornada da Organização;
- registries de superfícies/transições.

### D5 — experiência e telas

Não cria nem modifica:

- UXA;
- SVG;
- wireframe;
- estado visual;
- fluxo de confirmação de domínio;
- Tela Hoje;
- expressão guiada;
- compreensão inicial.

### D6 — grafo e ontologia técnica

Não cria:

- nó físico `EvolutionDomain`;
- relação Neo4j;
- constraint;
- índice;
- Cypher;
- modelo lógico detalhado;
- modelo físico;
- POC;
- GraphRAG operacional.

### D7 — Public Canon

Não altera o Guia Oficial nem outros artefatos públicos.

## 22. Não autorizações

A aprovação deste documento não autoriza:

- Engenharia de Produto;
- W0-01;
- UXA-102/V5;
- coleta de dados adicional;
- tratamento de dados sensíveis;
- personalização automática;
- publicidade comportamental;
- score de evolução;
- implementação de IA;
- banco de dados;
- grafo físico;
- API;
- billing;
- lançamento de funcionalidade.

## 23. Estado após D1–D3

Após esta reconciliação:

| Área | Estado semântico |
|---|---|
| taxonomia `JED-001..JED-009` | canônica em `PAS-001-DOMAIN-MODEL-001` |
| PAS-001 | reconciliado por autoridade pós-publicação, sem reescrever a release auditada |
| GPA-000 | leitura reconciliada com o eixo transversal de domínios |
| Contexto Vivo | dimensões estruturais preservadas; domínio separado e ortogonal |
| Objetivos | `0..n` domínios sem criar autoria ou prioridade |
| Eventos de Vida | dimensões do Contexto Vivo separadas de domínios afetados |
| Próximos Passos | domínios opcionais sem provar progresso/evolução |
| Oportunidades Ativas | domínios podem compor contexto; compatibilidade não equivale a relevância |
| Experiências | domínios opcionais sem provar transformação/evolução |
| Evolução Contínua | domínio, dimensão de Contexto Vivo e aspecto descritivo separados |
| D4–D7 | não iniciados por esta autoridade |

## 24. Critérios de reabertura

Esta reconciliação deverá ser revista se ocorrer qualquer um dos seguintes eventos:

1. alteração da taxonomia canônica de `JED-001..JED-009`;
2. criação formal de novo Domínio de Evolução;
3. mudança material do contrato `domain_link`;
4. alteração estrutural das oito dimensões do Contexto Vivo;
5. mudança da unidade funcional de Evolução Contínua;
6. descoberta de conflito entre capacidade especializada e Domain Model;
7. autorização de D4, D5, D6 ou D7 que revele nova necessidade semântica;
8. alteração de governança de dados sensíveis que afete classificação por domínio.

## 25. Decisão final

> **D1–D3 ficam semanticamente reconciliados por autoridade normativa pós-publicação.**
>
> O `PAS-001 1.0.0` e suas 54 extensões auditadas permanecem evidência histórica intacta. `PAS-001-DOMAIN-MODEL-001` governa a taxonomia e `PAS-001-DOMAIN-RECON-001` governa sua leitura transversal nas capacidades existentes. Nenhuma jornada integrada, UX, SVG, ontologia física, Public Canon ou implementação é promovida por esta decisão.
