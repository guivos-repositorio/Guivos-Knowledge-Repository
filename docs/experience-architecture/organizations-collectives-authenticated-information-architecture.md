---
id: GKR-UX-ORGCOL-AUTH-IA-001
title: Organizações e Coletivos — Arquitetura da Informação da Experiência Autenticada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-27
normative: false
maturity: authenticated_information_architecture_defined_pre_surface_map
depends_on:
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - UXA-014
  - UXA-019
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-UX-ORGCOL-SUPPLY-VALUE-001
  - UXA-100-A3
  - UXA-100-A4
---

# Organizações e Coletivos — Arquitetura da Informação da Experiência Autenticada

## 1. Finalidade

Este documento define a **Arquitetura da Informação** da futura experiência autenticada de Organização e Coletivo.

Ele transforma os atores, limites de autoridade e jobs já reconciliados em uma estrutura coerente de informação, sem antecipar o mapa final de superfícies, wireframes, UI ou implementação.

A pergunta desta etapa é:

> **Como o conhecimento e o trabalho de uma Organização ou de um Coletivo devem ser agrupados para que a pessoa autenticada compreenda contexto, responsabilidade, propósito, operação, relações, evidência e Próximos Passos sem perder autoridade ou autonomia?**

```text
ARQUITETURA DA INFORMAÇÃO
≠ SITEMAP FINAL
≠ MENU VISUAL FINAL
≠ WIREFRAME
≠ UI
≠ RBAC TÉCNICO
≠ IMPLEMENTAÇÃO
```

## 2. Princípios de arquitetura

A IA deverá obedecer aos seguintes princípios:

1. **contexto antes de ação** — a pessoa precisa compreender em nome de quem e com qual autoridade está atuando;
2. **síntese antes de volume** — a entrada autenticada precisa organizar o Momento e a atenção material, não despejar métricas;
3. **objeto antes de canal** — oportunidades, relações, compromissos, decisões e evidências devem possuir contexto próprio, não ficar presos a caixas genéricas de mensagens;
4. **autoridade antes de confirmação** — atos materiais precisam explicitar quem pode decidir;
5. **responsabilidade sem controle indevido** — Organização e Coletivo devem agir sem adquirir autoridade automática sobre a Journey individual;
6. **operação separada de evidência** — atividade realizada não equivale a avanço ou impacto;
7. **comercial separado de relevância** — Planos, Ads, patrocínio e capacidade comercial não organizam o núcleo da experiência;
8. **proteção e contestação como estrutura** — correção, divergência, pausa e saída não são exceções periféricas;
9. **maturidade especializada preservada** — fluxos já validados mantêm autoridade própria sem serem confundidos com a experiência principal;
10. **Organização ≠ Coletivo** — semelhança funcional não obriga paridade artificial de navegação.

## 3. Modelo estrutural comum

As duas experiências compartilham cinco camadas lógicas, mas não precisam possuir os mesmos agrupamentos internos.

```text
CAMADA 0 — CONTEXTO E AUTORIDADE
↓
CAMADA 1 — SÍNTESE DO MOMENTO
↓
CAMADA 2 — DOMÍNIOS DE TRABALHO
↓
CAMADA 3 — GOVERNANÇA, EVIDÊNCIA E CONTINUIDADE
↓
CAMADA 4 — CAPACIDADES ESPECIALIZADAS / CONTEXTUAIS
```

### 3.1 Camada 0 — Contexto e autoridade

Deve responder continuamente:

- qual participante está ativo;
- qual unidade ou contexto se aplica;
- qual papel está ativo;
- quais limites materiais de autoridade existem;
- quando outra aprovação é necessária.

Essa camada é estrutural e transversal. Ela não é definida aqui como header, menu, card ou componente.

### 3.2 Camada 1 — Síntese do Momento

Deve responder:

- o que está acontecendo agora;
- o que exige atenção;
- por quê;
- quais movimentos estão em andamento;
- qual Próximo Passo faz sentido;
- quais incertezas ou bloqueios existem.

A síntese referencia objetos de trabalho; ela não deve duplicar silenciosamente suas fontes de verdade.

### 3.3 Camada 2 — Domínios de trabalho

Agrupa os objetos sobre os quais Organização ou Coletivo efetivamente operam.

Cada participante possui domínios próprios definidos adiante.

### 3.4 Camada 3 — Governança, evidência e continuidade

Abrange, conforme o participante:

- autoridade;
- compromissos;
- decisões;
- proteção;
- riscos;
- contestação;
- evidências;
- revisão;
- encerramento.

Esses temas podem aparecer dentro de domínios de trabalho específicos; esta camada expressa sua função transversal e não exige uma única seção visual.

### 3.5 Camada 4 — Capacidades especializadas / contextuais

Inclui capacidades que devem ser acessíveis quando necessárias, mas não podem dominar a identidade da experiência principal, por exemplo:

- Planos e capacidade comercial;
- fluxos patrocinados já governados;
- fronteiras especializadas com produtos da Guivos;
- processos assistidos quando o autoatendimento não for suficiente.

## 4. Regra de contexto persistente

A IA deverá preservar a noção de **contexto ativo** em qualquer futuro mapa de superfícies.

Contexto ativo significa a combinação relevante de:

```text
participante
+ unidade / escopo
+ papel
+ autoridade
+ objeto de trabalho quando aplicável
```

Mudança de contexto não pode transportar automaticamente:

- permissões;
- dados;
- filtros;
- decisões pendentes;
- autoridade de aprovação;
- contexto pessoal protegido.

Quando uma pessoa possuir múltiplos papéis, a arquitetura deverá tornar a troca compreensível e reversível sem fundir identidades institucionais ou coletivas.

## 5. Arquitetura da Informação — Organização

A experiência autenticada da Organização será organizada em **cinco domínios principais de informação** e uma capacidade comercial especializada.

```text
ORGANIZAÇÃO
├── Visão Geral
├── Oportunidades e Programas
├── Relações
├── Responsabilidades e Evidências
├── Organização e Autoridade
└── Planos e Capacidade [especializado / contextual]
```

Os nomes acima são rótulos funcionais de IA. A copy final de interface poderá ser refinada em etapa própria sem alterar a responsabilidade semântica de cada domínio.

## 6. Organização — Visão Geral

### Pergunta funcional

> **O que está acontecendo na Organização, o que exige responsabilidade agora e como sua atuação está apoiando jornadas?**

### Conteúdo pertencente à síntese

- contexto institucional ativo;
- Momento institucional em poucas palavras;
- atenção material e motivo;
- mudanças relevantes;
- oportunidades/programas em movimento;
- relações que exigem decisão ou revisão;
- responsabilidades, riscos ou prazos materiais;
- avanço reconhecido quando houver evidência suficiente;
- Próximos Passos justificados;
- estados desconhecidos ou contestados que alterem decisão.

### Conteúdo que não deve dominar

- faturamento isolado;
- visualizações;
- quantidade de anúncios;
- ranking;
- volume bruto de publicações;
- compra de mídia;
- comparação de planos sem gatilho contextual.

### Regra

A Visão Geral é uma **síntese referencial**, não um repositório paralelo. O detalhe permanece no objeto responsável.

## 7. Organização — Oportunidades e Programas

### Finalidade

Agrupar o trabalho relacionado ao que a Organização oferece, opera ou habilita legitimamente.

### Objetos de informação

- oportunidade;
- programa/iniciativa;
- estado de publicação;
- disponibilidade;
- elegibilidade;
- condições de acesso;
- capacidade;
- responsáveis;
- alterações materiais;
- evidência operacional associada quando autorizada;
- relação com Domínios de Evolução sem acesso automático ao contexto individual.

### Jobs suportados

- `ORG-J03` no recorte material aplicável;
- `ORG-J04`;
- partes de `ORG-J06`;
- `ORG-J09`.

### Preservações

Fluxos especializados de cadastro, publicação, descoberta e detalhe já validados continuam autoridades próprias. A IA deverá conectá-los; não recriá-los como se estivessem ausentes.

```text
OPORTUNIDADE PUBLICADA
≠ DISTRIBUIÇÃO GARANTIDA
≠ RELEVÂNCIA
≠ IMPACTO
```

## 8. Organização — Relações

### Finalidade

Agrupar relações institucionais que possuam finalidade, autoridade, compromissos, recursos, dados ou responsabilidades materialmente relevantes.

### Objetos de informação

- relação Organização ↔ Coletivo;
- relação Organização ↔ Organização quando legitimamente aplicável;
- proposta;
- finalidade;
- escopo;
- autoridades;
- compromissos;
- recursos;
- condições econômicas;
- dados e privacidade;
- uso de marca;
- riscos e conflitos;
- revisão;
- contestação;
- pausa;
- encerramento.

### Jobs suportados

- `ORG-J05`;
- `ORG-J08` no recorte relacional;
- `BIL-J01..BIL-J06`.

### Regra

A relação é um objeto bilateral. A versão exibida à Organização não pode apagar a autoridade ou a perspectiva da contraparte.

## 9. Organização — Responsabilidades e Evidências

### Finalidade

Permitir que a Organização compreenda o que assumiu, o que está em risco, o que foi realizado e o que pode ou não ser afirmado com evidência.

### Objetos de informação

- responsabilidade;
- compromisso;
- prazo;
- risco;
- dependência;
- correção;
- evidência;
- resultado autorizado;
- limitação;
- fator externo;
- revisão;
- prestação de contas.

### Jobs suportados

- `ORG-J02` no aprofundamento;
- `ORG-J03`;
- `ORG-J06`;
- `ORG-J08`;
- `ORG-J09`.

### Regra de evidência

```text
ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO

CORRELAÇÃO
≠ CAUSALIDADE

AUSÊNCIA DE EVIDÊNCIA
→ DEVE PODER SER DECLARADA
```

## 10. Organização — Organização e Autoridade

### Finalidade

Concentrar a identidade institucional e o contexto necessário para atuar legitimamente.

### Objetos de informação

- identidade institucional;
- unidade/contexto;
- estado de verificação quando aplicável;
- representação;
- papéis funcionais;
- limites de autoridade;
- responsáveis;
- capacidade/ disponibilidade declarada;
- informações institucionais materiais;
- regras de correção e contestação do contexto.

### Jobs suportados

- `ORG-J01`;
- `ORG-J03`;
- `ORG-J08` no recorte de identidade/autoridade.

### Limites

Este domínio não define ainda:

- cadastro técnico de usuários;
- convite;
- RBAC final;
- matriz técnica de permissões;
- autenticação;
- MFA;
- administração de segurança.

Esses temas exigirão autoridade técnica própria quando Product Engineering for reativada.

## 11. Organização — Planos e Capacidade

### Natureza

Capacidade especializada/contextual.

O fluxo canônico de Planos da Organização já existe no pacote `UXA-100` e preserva a taxonomia `Conecta · Eleva · Transforma`.

### Regras de IA

- deve ser acessível quando a pessoa busca capacidade comercial ou atinge um limite legítimo;
- pode possuir entrada secundária explícita para consulta;
- não deve estruturar a Visão Geral em torno de upsell;
- não pode alterar relevância orgânica, legitimidade ou acesso ao contexto pessoal;
- deve retornar ao contexto anterior sem mudar estado quando não houver contratação confirmada.

```text
PLANO
≠ IDENTIDADE DA ORGANIZAÇÃO
≠ RELEVÂNCIA
≠ AUTORIDADE
```

## 12. Arquitetura da Informação — Coletivo

A experiência autenticada do Coletivo será organizada em **sete domínios principais de informação** e uma capacidade comercial especializada.

```text
COLETIVO
├── Início
├── Atividades e Oportunidades
├── Participação
├── Governança e Proteção
├── Relações
├── Aprendizados e Evidências
├── Coletivo e Autoridade
└── Planos e Capacidade [especializado / contextual]
```

A maior granularidade relativa ao Coletivo decorre da necessidade de manter participação voluntária, governança, moderação e proteção claramente distinguíveis da atividade em si.

## 13. Coletivo — Início

### Pergunta funcional

> **O que estamos construindo juntos, o que precisa de atenção e qual próximo movimento faz sentido para o propósito compartilhado?**

### Conteúdo pertencente à síntese

- propósito e contexto coletivo;
- papel/autoridade da pessoa autenticada;
- Momento coletivo;
- atenção principal e motivo;
- próxima atividade ou ação relevante;
- participação ou necessidade material;
- decisões abertas;
- relações que exigem atenção;
- avanço/aprendizado quando houver evidência;
- Próximos Passos justificados;
- estados desconhecidos ou contestados relevantes.

### Conteúdo que não deve dominar

- feed;
- curtidas;
- ranking de membros;
- streaks;
- volume de notificações;
- quantidade bruta de publicações;
- compra de plano.

### Regra

O Início é síntese do contexto coletivo, não rede social genérica.

## 14. Coletivo — Atividades e Oportunidades

### Finalidade

Agrupar aquilo que o Coletivo está organizando, vivendo, oferecendo ou habilitando de forma legítima.

### Objetos de informação

- atividade;
- ação;
- iniciativa;
- oportunidade;
- agenda/materialidade temporal quando necessária;
- recursos necessários;
- responsáveis voluntariamente aceitos;
- acessibilidade/proteção aplicável;
- estado;
- disponibilidade;
- dependências;
- relação com Domínios de Evolução sem classificar automaticamente participantes.

### Jobs suportados

- `COL-J02` no aprofundamento;
- `COL-J03`;
- `COL-J06`;
- partes de `COL-J08`;
- `COL-J11`.

### Regra

Atividade coletiva não cria obrigação individual e domínio da atividade não classifica automaticamente a Pessoa participante.

## 15. Coletivo — Participação

### Finalidade

Agrupar entrada, pertencimento, papéis e vínculos sem transformar pessoas em recurso do Coletivo.

### Objetos de informação

- solicitação;
- estado de análise;
- pertencimento;
- papel aceito;
- responsabilidade atribuída;
- participação atual quando legitimamente necessária;
- pausa;
- saída;
- vínculo;
- restrição ou condição legítima de participação.

### Jobs suportados

- `COL-J04`;
- partes de `COL-J05` e `COL-J10`.

### Preservações

Os fluxos especializados de solicitação, gestão de solicitações, `Meus Coletivos`, Central e Início da Pessoa participante preservam maturidades próprias.

A IA do responsável pelo Coletivo não absorve as superfícies pessoais da Pessoa participante.

```text
PARTICIPANTE
≠ ADMINISTRADOR
≠ MODERADOR
≠ REPRESENTANTE
```

## 16. Coletivo — Governança e Proteção

### Finalidade

Agrupar decisões e mecanismos que preservam legitimidade, voluntariedade, segurança e contestabilidade.

### Objetos de informação

- regra de governança;
- decisão aberta;
- consulta quando aplicável;
- autoridade necessária;
- comunicação oficial relacionada a decisão/governança;
- moderação;
- proteção;
- acessibilidade;
- denúncia;
- conflito;
- contestação;
- medida temporária;
- suspensão;
- revisão.

### Jobs suportados

- `COL-J05`;
- `COL-J10`;
- `COL-J11`.

### Regra

A posse de acesso técnico não substitui a regra de governança do Coletivo.

## 17. Coletivo — Relações

### Finalidade

Agrupar relações com Organizações e outros Coletivos sem perda de autonomia.

### Objetos de informação

Mantém o contrato lógico definido em `UXA-019`:

- finalidade;
- escopo;
- autoridades;
- compromissos;
- recursos;
- dados;
- marca;
- influência;
- patrocínio;
- conflitos;
- revisão;
- contestação;
- pausa;
- encerramento.

### Jobs suportados

- `COL-J07`;
- `COL-J10` no recorte relacional;
- `BIL-J01..BIL-J06`.

### Regra

```text
APOIO
≠ PROPRIEDADE

PATROCÍNIO
≠ GOVERNO

INFRAESTRUTURA
≠ AUTORIDADE SOBRE PERTENCIMENTO
```

## 18. Coletivo — Aprendizados e Evidências

### Finalidade

Permitir que o Coletivo compreenda o que ocorreu e o que foi aprendido sem reduzir avanço a popularidade ou atividade bruta.

### Objetos de informação

- ação realizada;
- participação autorizada;
- aprendizado;
- evidência;
- contribuição;
- limitação;
- resultado coletivo autorizado;
- correção;
- revisão.

### Jobs suportados

- `COL-J08`;
- `COL-J02` no aprofundamento;
- `COL-J11`.

### Regra

```text
MAIS MEMBROS
≠ MAIS AVANÇO

MAIS PUBLICAÇÕES
≠ MAIS CONTRIBUIÇÃO

ATIVIDADE
≠ IMPACTO
```

## 19. Coletivo — Coletivo e Autoridade

### Finalidade

Concentrar o contexto constitutivo necessário à atuação legítima.

### Objetos de informação

- identidade;
- propósito;
- contexto;
- regra de governança;
- representação;
- papéis;
- limites de autoridade;
- responsáveis legitimamente atribuídos;
- necessidades e recursos estruturais quando materialmente aplicáveis;
- relações constitutivas relevantes;
- correção/contestação de informação do Coletivo.

### Jobs suportados

- `COL-J01`;
- partes de `COL-J03`, `COL-J05` e `COL-J10`.

### Limite

A IA não define sistema técnico de cargos, permissões ou usuários.

## 20. Coletivo — Planos e Capacidade

### Natureza

Capacidade especializada/contextual.

O pacote existente preserva a taxonomia `Livre · Mobiliza · Impacta · Rede`.

### Regras de IA

- acesso contextual quando houver necessidade legítima de capacidade;
- possibilidade de consulta explícita sem converter a experiência em funil de upsell;
- retorno ao contexto sem alteração comercial quando nenhuma contratação ocorrer;
- plano pago não altera pertencimento, relevância, legitimidade, domínio ou impacto.

## 21. Objetos transversais

A futura experiência deverá manter objetos conceitualmente distinguíveis mesmo quando forem apresentados juntos.

| Objeto | Responsabilidade semântica |
|---|---|
| Contexto ativo | em nome de quem, onde e com qual autoridade a pessoa atua |
| Atenção material | o que exige consideração agora e por quê |
| Próximo Passo | ação ou decisão justificada, com autoridade necessária |
| Oportunidade | materialização concreta de um caminho possível |
| Programa / iniciativa | conjunto institucional organizado de ações/condições |
| Atividade coletiva | ação ou experiência organizada pelo Coletivo |
| Relação | acordo bilateral com finalidade, limites e ciclo de vida |
| Compromisso | obrigação ou condição assumida por participante identificado |
| Recurso | meio financeiro ou não financeiro com finalidade e restrições |
| Decisão | escolha sujeita à autoridade ou governança aplicável |
| Evidência | informação usada para sustentar uma afirmação limitada |
| Resultado / aprendizado | mudança ou compreensão registrada sem inferência automática de impacto |
| Plano / capacidade | capacidade comercial especializada, separada de relevância e autoridade |

A existência de referência cruzada não transforma objetos distintos em uma entidade única.

## 22. Regra de fonte de verdade e síntese

A Visão Geral da Organização e o Início do Coletivo devem compor sínteses a partir dos domínios responsáveis.

Exemplo conceitual:

```text
RELAÇÃO EM REVISÃO
→ fonte de verdade = objeto Relação
→ pode gerar Atenção na síntese
→ ação leva ao contexto da Relação
→ decisão atualiza a Relação
→ síntese reflete o novo estado
```

Evitar:

```text
mesma decisão mantida independentemente
em múltiplas áreas
→ estados divergentes
→ autoridade ambígua
```

## 23. Relações bilaterais — simetria de fatos, assimetria de ações

Uma relação Organização ↔ Coletivo precisa preservar o mesmo núcleo factual para as duas partes:

- participantes;
- natureza;
- finalidade;
- escopo aprovado;
- compromissos;
- recursos;
- dados;
- condições;
- estado;
- prazo/revisão;
- divergências registradas.

Porém, as ações disponíveis podem ser diferentes porque dependem da autoridade de cada lado.

```text
FATO COMPARTILHADO
≠ MESMA AUTORIDADE
≠ MESMA AÇÃO DISPONÍVEL
```

## 24. Atenção como vista derivada, não domínio autônomo

“Atenção” não constitui um banco de trabalho independente.

Ela é uma leitura derivada de objetos que possuem estado material, por exemplo:

- aprovação pendente;
- compromisso atrasado;
- risco;
- informação material incompleta;
- relação em revisão;
- decisão contestada;
- atividade sem responsável necessário;
- capacidade atingida;
- dado ou consentimento ausente.

A origem precisa continuar identificável e corrigível.

## 25. Próximo Passo como orientação, não autoridade

O Próximo Passo pode aparecer transversalmente, mas deve apontar para um objeto e uma autoridade.

```text
PRÓXIMO PASSO
→ contexto
→ motivo
→ objeto afetado
→ evidência / incerteza
→ autoridade necessária
→ alternativas
```

A IA não deve criar uma “caixa de tarefas” que transforme recomendações, possibilidades e decisões em obrigações equivalentes.

## 26. Busca, filtros e notificações

Esta etapa não define mecanismo final de busca, filtros ou notificações.

Contudo, qualquer materialização futura deverá preservar:

- contexto ativo;
- autoridade;
- origem do objeto;
- diferença entre atenção, informação e ação;
- proteção de dados;
- ausência de transporte silencioso entre Organização, Coletivo e Pessoa.

Nenhuma notificação pode se tornar fonte de verdade superior ao objeto que a originou.

## 27. Relação com Produtos Especializados

A experiência autenticada de Organização ou Coletivo não absorve Produtos Especializados.

### Guivos Business

Pode oferecer capacidades institucionais e analíticas à Organização, mas:

```text
ORGANIZAÇÃO
≠ GUIVOS BUSINESS
```

### Guivos Ads

Pode oferecer mídia ou Opportunity Boost quando legitimamente aplicável, mas compra de mídia não entra como eixo de relevância.

### Guivos Intelligence

Pode apoiar compreensão de contexto e evidências dentro de finalidade e autoridade, mas não se torna autoridade de decisão.

### Guivos Journey

Conecta atuação institucional/coletiva às jornadas humanas sem transferir controle sobre objetivos pessoais.

### Mall, Travel e Media

Podem materializar handoffs especializados quando houver autoridade própria, sem transformar a IA autenticada em catálogo de produtos Guivos.

## 28. O que a arquitetura não deve produzir

### Organização

Não deve convergir para:

- CRM genérico;
- painel de vendas;
- gerenciador de anúncios;
- BI de receita como centro da experiência;
- catálogo institucional sem contexto;
- painel de impacto não evidenciado.

### Coletivo

Não deve convergir para:

- rede social genérica;
- feed como estrutura central;
- fórum sem governança;
- ranking de membros;
- painel de engajamento compulsório;
- ferramenta de captura comercial da comunidade.

## 29. Estados transversais que a futura IA materializada precisa suportar

Sem definir ainda superfícies, o mapa seguinte deverá conseguir acomodar estados como:

- sem atenção material;
- informação incompleta;
- aguardando autoridade;
- aguardando contraparte;
- bloqueado por proteção/privacidade;
- contestado;
- alteração material pendente;
- risco urgente;
- pausado;
- encerrado com obrigações remanescentes;
- capacidade atingida;
- informação sensível protegida;
- baixa conectividade quando relevante;
- operação internacional quando legítima.

Esses estados não exigem necessariamente telas próprias.

## 30. Critérios de qualidade da IA

A arquitetura pode ser considerada definida para avançar ao mapa de superfícies quando:

1. contexto e autoridade precedem ação;
2. Organização possui agrupamentos próprios coerentes com sua responsabilidade institucional;
3. Coletivo possui agrupamentos próprios coerentes com propósito, participação e governança;
4. relações bilaterais preservam núcleo factual compartilhado e autoridades distintas;
5. fluxos especializados existentes possuem pontos de conexão sem serem confundidos com UX principal;
6. evidência permanece separada de atividade e impacto;
7. Planos permanecem especializados/contextuais;
8. Produtos Especializados não são absorvidos pela identidade do participante;
9. síntese não se torna fonte paralela de verdade;
10. decisões de tela, layout, componente e RBAC permanecem adiadas.

## 31. Decisões explicitamente adiadas

Este documento não define:

- quantidade final de telas;
- IDs de novas superfícies;
- sitemap navegável final;
- ordem visual final de menu;
- desktop/mobile;
- dashboard;
- cards;
- tabelas;
- componentes;
- densidade;
- estados responsivos;
- regras técnicas de permissão;
- wireframes;
- UI;
- protótipo;
- implementação.

Também não reativa `UXA-015..018`, não inicia `UXA-102/V5` e não reativa Product Engineering.

## 32. Estado após esta definição

```text
FOUNDATIONS / ROLES
→ RECONCILED

FUNCTIONAL ACTORS / AUTHORITIES / JOBS
→ DEFINED

AUTHENTICATED INFORMATION ARCHITECTURE
→ DEFINED FOR SURFACE-MAP INPUT

SURFACE / STATE MAP
→ NOT YET DEFINED

PRIORITY FLOWS
→ NOT YET DEFINED AS MAIN AUTHENTICATED EXPERIENCE

MAIN AUTHENTICATED WIREFRAMES
→ NOT YET DEFINED

UXA-102 / V5
→ NOT STARTED

PRODUCT ENGINEERING
→ PAUSED
```

## 33. Próximo ato documental permitido

Após validação deste incremento, o próximo ato permitido nesta frente é:

> **materializar o mapa lógico de superfícies e estados da experiência autenticada de Organização e Coletivo, preservando os IDs e fluxos especializados já existentes e sem produzir wireframes.**

O mapa deverá decidir quais responsabilidades de IA exigem superfície própria, quais podem coexistir e como os estados se conectam, sem antecipar composição visual.