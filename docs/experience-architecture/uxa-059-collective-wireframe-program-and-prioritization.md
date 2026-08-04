---
id: UXA-059
title: Programa e Priorização dos Wireframes de Coletivos
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-03
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-016
  - UXA-018
  - UXA-019
  - UXA-056
  - UXA-057
  - UXA-058
related:
  - UXA-060
  - M7.61
normative: false
---

# Programa e Priorização dos Wireframes de Coletivos

## 1. Finalidade

Este documento transforma os contratos funcionais das UXA-056, UXA-057 e UXA-058 em um programa controlado de materialização de wireframes de baixa fidelidade para Pessoas, responsáveis por Coletivos e Organizações legitimamente relacionadas.

O programa define:

- quais superfícies precisam existir;
- em que ordem deverão ser materializadas;
- quais estados pertencem à mesma família funcional;
- quando um estado exige wireframe separado;
- qual canal deverá ser priorizado;
- quais dependências impedem avanço prematuro;
- como validar cada conjunto antes de criar o seguinte;
- como preservar cobertura contratual sem transformar cada estado em uma tela independente.

A UXA-059 não cria SVG, protótipo, design visual, componente técnico ou implementação.

## 2. Pergunta do programa

O programa deverá permitir responder:

> **Qual é a menor sequência de superfícies capaz de tornar descoberta, participação, comunicação, proteção, avaliação e gestão de Coletivos compreensíveis, sem criar dezenas de telas desconectadas ou antecipar decisões ainda não validadas?**

Para a pessoa participante, a sequência deverá responder:

> **Como encontro um Coletivo, compreendo suas condições, decido participar, acompanho meus vínculos, recebo informações importantes, interajo com proteção e saio quando desejar?**

Para o responsável, deverá responder:

> **Como apresento o Coletivo, analiso vínculos, comunico, protejo participantes, respondo avaliações e administro responsabilidades sem receber autoridade ou dados além do necessário?**

## 3. Decisão central

Os 88 estados obrigatórios registrados nas UXA-056, UXA-057 e UXA-058 permanecerão como cobertura contratual, mas não serão convertidos automaticamente em 88 telas ou 88 SVGs.

Um estado somente exigirá wireframe separado quando alterar materialmente pelo menos uma destas dimensões:

1. hierarquia da informação;
2. decisão principal disponível;
3. autoridade da pessoa autenticada;
4. público ou visibilidade;
5. dados apresentados ou compartilhados;
6. consequência do estado;
7. proteção ou risco;
8. navegação ou continuidade;
9. canal necessário;
10. necessidade de recuperação após erro.

Mudanças apenas textuais, confirmações simples, mensagens transitórias, indicadores menores ou ações desabilitadas poderão permanecer como anotações ou variações dentro de uma mesma família.

## 4. Cobertura contratual preservada

| Contrato | Estados obrigatórios | Responsabilidade principal |
|---|---:|---|
| UXA-056 | 20 | descoberta, perfil público, entrada, vínculo, `Meus Coletivos` e gestão de participação |
| UXA-057 | 24 | avaliação, reputação, resposta, contestação e agregação |
| UXA-058 | 44 | atualizações, comunicação, recomendações, contato, notificações, proteção e moderação |
| Total | 88 | cobertura integral a ser demonstrada pelo programa |

A cobertura será controlada por matriz de estado para família de wireframe. Estado coberto não significa necessariamente SVG exclusivo.

## 5. Princípios de materialização

### 5.1 Jornada antes de catálogo de telas

A ordem seguirá decisões reais da pessoa e do responsável, não a ordem numérica dos documentos nem a quantidade de funcionalidades.

### 5.2 Superfície antes de estado residual

Primeiro será validada a superfície principal. Estados alternativos serão materializados somente quando a hierarquia base estiver compreensível.

### 5.3 Pessoa antes de operação avançada

Descoberta, decisão de entrada, continuidade e ambiente interno da pessoa antecederão painéis extensos de gestão.

### 5.4 Proteção desde o primeiro wireframe

Privacidade, consentimento, origem, autoridade, denúncia, pausa e saída não serão adicionados apenas ao final.

### 5.5 Canal conforme responsabilidade

- experiências da pessoa: móvel primeiro;
- gestão densa do responsável: computador primeiro;
- triagem urgente do responsável: móvel somente quando houver caso legítimo;
- perfil público: móvel primeiro, com computador posterior apenas se a hierarquia mudar;
- responsividade não gera automaticamente um novo artefato.

### 5.6 Um cenário canônico por referência

Cada wireframe principal utilizará um cenário coerente e reutilizável, preservando nomes, estados, papéis, atividades e relações entre superfícies.

### 5.7 Sem rede social genérica

O programa não cria perfil social global, seguidores entre pessoas, ranking, feed infinito, popularidade como relevância ou mensagem privada automática.

### 5.8 Sem publicidade interna silenciosa

Opportunity Boost, publicidade ou patrocínio não serão inseridos em comunicados, discussões, perguntas, atividades ou mensagens privadas sem contrato próprio e identificação explícita.

## 6. Estrutura do programa

O programa será dividido em quatro níveis:

```text
P0A — espinha dorsal das superfícies
→ P0B — estados críticos da espinha dorsal
→ P1 — participação interna e operação recorrente
→ P2 — confiança, recomendação, contato e proteção avançada
```

Cada nível depende da validação funcional do anterior. A integração de um wireframe não autoriza automaticamente a criação do próximo.

## 7. P0A — Espinha dorsal das superfícies

A primeira onda deverá materializar exatamente nove referências principais.

| Ordem | Superfície | Canal inicial | Decisão principal |
|---:|---|---|---|
| 1 | Explorar Coletivos | móvel | escolher uma categoria, busca ou contexto de exploração |
| 2 | Resultados de Busca | móvel | compreender e comparar resultados sem confundir relevância, patrocínio e popularidade |
| 3 | Perfil Público do Coletivo | móvel | conhecer propósito, funcionamento, regras, reputação disponível e forma de entrada |
| 4 | Solicitação de Participação | móvel | revisar significado do vínculo, dados, regras e confirmação |
| 5 | Solicitação Pendente | móvel | compreender estado, prazo, responsável, cancelamento e próximos eventos possíveis |
| 6 | Meus Coletivos | móvel | acompanhar participações, acompanhamentos, solicitações, convites e pausas |
| 7 | Central de Atualizações | móvel | identificar o que mudou, de qual Coletivo veio e se exige ação |
| 8 | Início do Participante | móvel | compreender propósito, momento, comunicação, atividades e participação sem pressão |
| 9 | Visão Geral do Responsável | computador | reconhecer autoridade, solicitações, comunicação, proteção e responsabilidades atuais |

### 7.1 Resultado esperado

A P0A deverá demonstrar a continuidade:

```text
Explorar
→ buscar ou navegar
→ conhecer o perfil público
→ revisar participação
→ acompanhar solicitação
→ retornar por Meus Coletivos
→ receber atualizações
→ entrar no ambiente interno
```

Para o responsável:

```text
representar o Coletivo
→ compreender o momento operacional
→ revisar solicitações e participantes
→ comunicar com autoridade
→ tratar proteção e moderação
→ revisar configurações e evidências
```

### 7.2 Limite da P0A

A P0A não materializará ainda:

- todos os estados vazios e de erro;
- comunicação detalhada;
- avaliação completa;
- mensagens privadas;
- recomendação;
- moderação completa;
- configurações avançadas;
- responsividade total.

Ela deverá, contudo, reservar navegação e pontos de entrada para essas responsabilidades.

## 8. P0B — Estados críticos da espinha dorsal

Após validação das nove referências, serão materializados estados que alteram decisões essenciais.

### 8.1 Descoberta

- busca sem resultados;
- filtros e origem da descoberta;
- resultado patrocinado identificado, quando aplicável fora dos canais internos;
- falha de busca com conteúdo orgânico preservado;
- localização desativada ou território manual, quando material.

### 8.2 Perfil público

- entrada aberta;
- entrada mediante aprovação;
- Coletivo não listado ou protegido;
- entradas temporariamente fechadas;
- reputação com base insuficiente;
- Coletivo encerrado.

### 8.3 Participação

- revisão de regras e dados;
- informação adicional solicitada;
- entrada confirmada;
- solicitação recusada ou expirada;
- cancelamento da solicitação;
- convite recebido.

### 8.4 Continuidade pessoal

- `Meus Coletivos` sem vínculos;
- solicitações e convites;
- participações pausadas;
- Central sem atualização relevante;
- agrupamento por excesso de volume;
- falha de sincronização ou baixa conectividade.

### 8.5 Responsável

- gestão de solicitações;
- gestão de participantes e papéis;
- configurações de visibilidade;
- autoridade insuficiente;
- ausência de responsabilidade urgente.

Os estados poderão ser agrupados em placas de estados quando preservarem a mesma hierarquia e canal.

## 9. P1 — Participação interna e operação recorrente

A P1 materializará as famílias necessárias para o funcionamento cotidiano do Coletivo.

### 9.1 Comunicação do participante

1. lista de comunicados;
2. comunicado oficial e histórico de atualização;
3. alerta de segurança;
4. lista de discussões;
5. discussão aberta e sintetizada;
6. lista de perguntas;
7. pergunta aguardando resposta;
8. pergunta com resposta de participante;
9. pergunta com resposta oficial;
10. conversa de atividade;
11. consulta aberta;
12. decisão registrada;
13. pessoas e papéis;
14. arquivos e recursos;
15. preferências de notificação.

### 9.2 Operação do responsável

1. criação e revisão de comunicado;
2. seleção de público e prioridade;
3. perguntas sem resposta;
4. gestão de discussões;
5. comunicação de atividade;
6. registro de consulta e decisão;
7. fila de solicitações;
8. detalhe de participante e vínculo;
9. gestão de papéis aceitos;
10. perfil público e visibilidade;
11. painel operacional agregado;
12. relação com Organização apoiadora, quando material.

### 9.3 Regra de separação

Comunicado, discussão, pergunta, consulta, decisão e conversa de atividade não serão reunidos em um único chat ou feed.

## 10. P2 — Confiança, recomendação, contato e proteção avançada

A P2 materializará responsabilidades que dependem de vínculos e canais já compreensíveis.

### 10.1 Avaliação e reputação

- convite voluntário para avaliar;
- elegibilidade confirmada ou negada;
- seleção do objeto e contexto;
- avaliação estruturada;
- comentário e visibilidade;
- revisão anterior ao envio;
- avaliação enviada, atualizada ou retirada;
- resumo público com base suficiente;
- resumo público com base insuficiente;
- distribuição por dimensão;
- comentário público verificado;
- resposta oficial;
- contestação e revisão;
- alteração material separando períodos;
- fonte externa identificada;
- painel agregado do responsável;
- conflito ou incentivo identificado;
- denúncia separada da avaliação.

### 10.2 Compartilhamento, convite e recomendação

- compartilhar referência;
- enviar convite;
- recomendação pessoal;
- recomendação institucional;
- sugestão da Guivos;
- publicidade identificada;
- recomendações recebidas;
- preferência ou recusa de recomendações.

### 10.3 Contato entre pessoas

- solicitação contextual de contato;
- contato aceito;
- contato recusado ou expirado;
- mensagem privada;
- revogação do contato;
- conversa bloqueada.

### 10.4 Proteção e moderação

- pausa e saída;
- suspensão preventiva;
- remoção;
- denúncia enviada;
- conteúdo em revisão;
- proteção temporária;
- conteúdo limitado ou removido;
- conteúdo restaurado;
- recurso e decisão revisada;
- grupo protegido com contato restrito;
- baixa conectividade e falha de envio.

## 11. Famílias funcionais

Uma família de wireframe reúne estados que compartilham:

- finalidade;
- objeto principal;
- público;
- autoridade;
- canal;
- navegação de entrada e saída.

Exemplos:

| Família | Estados que poderão compartilhar referência |
|---|---|
| Busca | resultados, filtros, origem e ordenação |
| Perfil público | entrada aberta, aprovação e fechado, quando a hierarquia permanecer equivalente |
| Solicitação | revisão, pendência, informação adicional e resultado |
| Meus Coletivos | participando, acompanhando, convites, solicitações e pausas |
| Atualizações | conteúdo, vazio, agrupamento e falha |
| Comunicados | lista, detalhe, atualização e confirmação de leitura |
| Perguntas | aguardando, participante, oficial e resposta atualizada |
| Avaliação | critérios, comentário, revisão, envio e atualização |
| Moderação | triagem, proteção, decisão, restauração e recurso |

Um conjunto poderá conter mais de um SVG quando a decisão ou hierarquia mudar materialmente.

## 12. Regra para criar SVG separado

Criar novo SVG quando ocorrer ao menos uma destas condições:

- ação principal diferente;
- autoridade diferente;
- mudança entre público, participante e responsável;
- dado sensível passa a ser exibido ou ocultado;
- risco exige proteção própria;
- estado vazio altera a proposta da superfície;
- erro altera continuidade ou recuperação;
- canal muda de móvel para computador por necessidade funcional;
- a pessoa precisa revisar ou conceder novo consentimento;
- o objeto muda, como Coletivo para atividade ou avaliação.

Não criar novo SVG apenas por:

- mudança de título;
- variação pequena de conteúdo;
- ação secundária desabilitada;
- confirmação transitória;
- contador diferente;
- cor, ícone ou estilo;
- responsividade sem mudança de hierarquia.

## 13. Canais prioritários

| Responsabilidade | Canal inicial | Justificativa |
|---|---|---|
| descoberta, perfil, participação e continuidade | móvel | decisão pessoal recorrente e contextual |
| comunicação e atividades | móvel | consulta e resposta no cotidiano |
| avaliação pela pessoa | móvel | experiência posterior e voluntária |
| gestão de solicitações e comunicação | computador | densidade, comparação e autoridade operacional |
| moderação e configuração | computador | contexto, evidência e revisão |
| triagem urgente do responsável | móvel posterior | somente após validar o fluxo principal |
| perfil público para computador | posterior | somente se a hierarquia exigir adaptação própria |

Tablet não será materializado inicialmente.

## 14. Cenário canônico

A primeira onda utilizará um Coletivo de referência capaz de demonstrar:

- propósito compreensível;
- modalidade híbrida;
- atuação territorial sem expor localização sensível;
- entrada mediante aprovação;
- atividade futura;
- participação e acompanhamento distintos;
- Organização apoiadora sem autoridade automática;
- comunicados e perguntas existentes;
- reputação com base limitada;
- acessibilidade ainda parcialmente confirmada;
- responsável com autoridade delimitada;
- possibilidade de pausa, saída e denúncia.

O cenário deverá permanecer consistente entre superfícies. Dados reais, nomes de pessoas reais ou informações sensíveis não serão utilizados.

## 15. Navegação mínima da pessoa

```text
Descobrir
├── Explorar Coletivos
├── Resultados de busca
└── Perfil público

Meus Coletivos
├── Participando
├── Acompanhando
├── Solicitações
├── Convites
└── Pausados

Coletivo
├── Início
├── Comunicados
├── Discussões
├── Perguntas e respostas
├── Atividades
├── Pessoas e papéis
├── Arquivos e recursos
├── Decisões
└── Sobre, regras e proteção

Atualizações
├── Importantes
├── Precisa de ação
├── Perguntas e respostas
├── Atividades
├── Discussões
├── Convites e recomendações
└── Contatos
```

Essa arquitetura é funcional e poderá ser refinada após validação. Ela não define navegação técnica final.

## 16. Navegação mínima do responsável

```text
Visão Geral
├── Solicitações e participantes
├── Comunicação
├── Perguntas e respostas
├── Atividades
├── Decisões e governança
├── Perfil público e descoberta
├── Avaliações e reputação
├── Moderação e proteção
├── Pessoas, papéis e autoridades
├── Relações e recursos
└── Configurações
```

A visibilidade de cada área dependerá do papel e da autoridade.

## 17. Relação com o Início do Coletivo existente

As UXA-016 e UXA-018 permanecem referências históricas e funcionais do ambiente interno do participante.

A nova materialização deverá:

- preservar propósito antes de atividade;
- manter pertencimento, disponibilidade, papel e autoridade separados;
- incorporar a Central de Atualizações e os canais especializados sem virar feed;
- distinguir perfil público, ambiente interno e gestão;
- refletir estados de participação da UXA-056;
- reservar reputação conforme UXA-057;
- incorporar comunicação e proteção conforme UXA-058;
- revisar o SVG existente em incremento próprio.

O SVG atual não será apagado ou declarado inválido antes da integração de uma substituição validada.

## 18. Relação com Organizações

Wireframes de Coletivos deverão mostrar, quando material:

- Organização relacionada;
- natureza do vínculo;
- apoio, patrocínio ou operação conjunta;
- limites de autoridade;
- dados compartilhados;
- recursos envolvidos;
- possibilidade de contestação ou encerramento.

A relação não transformará Organização em proprietária do Coletivo nem participante em cliente ou beneficiário automático.

## 19. Publicidade e distribuição

A descoberta pública poderá apresentar publicidade identificada conforme os contratos do Opportunity Boost.

Porém:

- primeiro resultado orgânico permanece preservado;
- publicidade não será apresentada como recomendação;
- patrocínio não compra reputação;
- canais internos não receberão publicidade silenciosa;
- mensagens privadas não receberão inserção patrocinada;
- conteúdo protegido não alimentará segmentação;
- preferência negativa permanecerá reversível e respeitada.

## 20. Critérios de entrada de um pacote de wireframes

Um pacote somente poderá começar quando possuir:

1. contrato funcional aplicável integrado;
2. cenário e pergunta da superfície definidos;
3. público e autoridade identificados;
4. canal inicial justificado;
5. estados incluídos e excluídos declarados;
6. dados necessários e dados proibidos definidos;
7. navegação anterior e posterior conhecida;
8. riscos e proteções mapeados;
9. relação com superfícies existentes registrada;
10. autorização humana separada.

## 21. Critérios de saída de um pacote

Um pacote somente poderá ser encerrado quando:

1. referências de baixa fidelidade estiverem materializadas;
2. cada SVG possuir documento de autoridade;
3. estados cobertos estiverem mapeados;
4. estados não cobertos permanecerem explícitos;
5. navegação e continuidade forem demonstradas;
6. hierarquia, ações e autoridade forem compreensíveis;
7. privacidade, consentimento, proteção e saída estiverem visíveis;
8. validação mecânica estiver aprovada;
9. validação funcional estiver registrada em incremento separado ou no pacote autorizado;
10. nenhuma implementação ou protótipo for declarado por inferência.

## 22. Limite recomendado de cada incremento

Para manter revisão humana possível:

- até três superfícies principais por incremento;
- até seis SVGs quando houver estados alternativos;
- uma responsabilidade dominante;
- um canal principal;
- uma matriz explícita de cobertura;
- validação funcional antes de ampliar para o próximo conjunto.

Exceções exigirão justificativa e autorização explícita.

## 23. Gate de alinhamento à Fundação

Cada conjunto deverá demonstrar aderência a:

- Essência;
- Propósito;
- Missão Operacional;
- Visão de Longo Prazo;
- Constituição;
- Princípios Permanentes;
- presença companheira;
- autonomia;
- voluntariedade;
- explicabilidade;
- privacidade;
- proteção;
- contestação;
- saída legítima.

Falha material impede avanço.

## 24. Matriz mínima de rastreabilidade

Cada futuro documento deverá conter:

| Campo | Conteúdo obrigatório |
|---|---|
| contrato de origem | UXA-056, UXA-057 ou UXA-058 |
| família funcional | descoberta, vínculo, comunicação, avaliação, contato ou gestão |
| estados cobertos | identificadores ou descrições exatas |
| estados excluídos | motivo e pacote futuro |
| público | pessoa, participante, responsável, moderador ou Organização |
| autoridade | ação permitida e limite |
| dados | exibidos, compartilhados e proibidos |
| canal | móvel ou computador |
| entrada | superfície anterior |
| saída | superfície ou estado posterior |
| risco | privacidade, segurança, coerção, discriminação ou fraude |
| validação | mecânica, funcional e transversal |

## 25. Métricas do programa

O programa poderá acompanhar:

- estados contratuais mapeados;
- famílias definidas;
- referências materializadas;
- referências validadas;
- estados ainda sem cobertura;
- riscos ainda sem representação;
- inconsistências entre pessoa e responsável;
- navegações sem continuidade;
- variantes de canal justificadas.

Não serão métricas de sucesso:

- quantidade de telas;
- velocidade de produção isolada;
- volume de componentes;
- número de interações;
- popularidade do Coletivo;
- quantidade de mensagens;
- número de participantes.

## 26. Dependências especializadas

Antes da P2 completa, poderão ser necessários contratos ou políticas adicionais para:

- moderação operacional;
- privacidade e retenção de comunicação;
- segurança e resposta a risco;
- proteção de menores e grupos sensíveis;
- estatística de reputação;
- notificações e canais externos;
- acessibilidade técnica;
- uso de arquivos e links externos;
- internacionalização e tradução.

Ausência de política especializada não impede wireframe exploratório, mas impede declarar a solução pronta para protótipo ou produção.

## 27. Critérios de priorização

Uma superfície terá prioridade maior quando combinar:

1. necessidade para compreender a jornada principal;
2. risco de confusão entre público, participante e responsável;
3. dependência para outras superfícies;
4. decisão irreversível ou material;
5. exposição de dados ou autoridade;
6. proteção de grupos sensíveis;
7. frequência provável de uso;
8. necessidade de corrigir ambiguidade existente;
9. capacidade de validar múltiplos contratos;
10. ausência de alternativa já materializada.

Receita, publicidade, popularidade ou facilidade técnica não determinarão a prioridade arquitetural.

## 28. Ordem recomendada dos próximos incrementos

Após integração e autorizações separadas, a ordem recomendada será:

1. **UXA-060 — Wireframes Móveis de Explorar Coletivos e Resultados de Busca**;
2. validação funcional da UXA-060;
3. perfil público e formas de entrada;
4. fluxo de participação e estados da solicitação;
5. `Meus Coletivos`;
6. Central de Atualizações;
7. reformulação do Início do Participante;
8. Visão Geral do Responsável;
9. estados críticos da P0B;
10. comunicação e operação da P1;
11. reputação, recomendações, contato e proteção da P2;
12. validação transversal do percurso completo.

Somente o primeiro incremento recebe identificador antecipado. Os demais serão nomeados e numerados quando autorizados, evitando reservar uma sequência rígida antes da aprendizagem.

## 29. Situação após integração

Após integração da UXA-059:

- os 88 estados permanecerão contratados;
- nove referências formarão a espinha dorsal prioritária;
- nenhum novo wireframe estará materializado;
- UXA-016 e UXA-018 permanecerão vigentes até reformulação própria;
- o programa geral UXA-005 reconhecerá a nova frente;
- a cobertura do Opportunity Boost permanecerá em 46 wireframes;
- protótipo, teste e Engenharia de Produto permanecerão não iniciados;
- o próximo pacote recomendado será a UXA-060.

## 30. Critérios de aceite

A UXA-059 poderá avançar quando:

1. os 88 estados forem preservados como cobertura contratual;
2. estado não equivaler automaticamente a tela;
3. nove superfícies principais formarem uma continuidade compreensível;
4. pessoa e responsável possuírem experiências separadas;
5. móvel e computador forem escolhidos por responsabilidade;
6. o Início existente for preservado até substituição validada;
7. comunicação não for reduzida a feed ou chat único;
8. avaliação não anteceder experiência elegível;
9. contato privado depender de consentimento;
10. publicidade permanecer identificada e fora dos canais internos;
11. pacotes possuírem critérios de entrada e saída;
12. incrementos permanecerem pequenos e revisáveis;
13. nenhum wireframe for criado neste incremento;
14. nenhuma implementação, protótipo ou teste for antecipado;
15. Engenharia de Produto permanecer pausada.

## 31. Limites

Este programa não:

- cria SVG;
- define design visual;
- define componentes;
- cria protótipo;
- executa teste de usabilidade;
- define tecnologia de busca, chat ou notificação;
- estabelece algoritmo de recomendação ou reputação;
- conclui políticas jurídicas ou operacionais;
- altera preços, planos ou Modelo Econômico;
- altera Resultados Empresariais;
- altera os 46 wireframes do Opportunity Boost;
- inicia Engenharia de Produto.

## 32. Próximo ato recomendado

Após integração e nova autorização separada, o próximo ato recomendado será:

> **UXA-060 — Wireframes Móveis de Explorar Coletivos e Resultados de Busca**

Escopo inicial recomendado:

- Explorar Coletivos;
- resultados com busca e filtros;
- busca sem resultados;
- origem da descoberta e publicidade identificada quando aplicável.

A UXA-060 deverá permanecer em baixa fidelidade, móvel primeiro e sem criar perfil público, participação ou gestão no mesmo incremento.

Nenhum ato posterior é iniciado automaticamente.
