---
id: UXA-070
title: Programa Funcional do Ambiente de Simulação das Jornadas
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-30
parent: UXA-000
depends_on:
  - PAS-001
  - UXA-001
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-035
  - UXA-037
  - UXA-038
  - UXA-050
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-061
  - UXA-063
  - UXA-065
  - UXA-067
  - UXA-069
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
related:
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-071
  - M7.72
normative: false
---

# Programa Funcional do Ambiente de Simulação das Jornadas

## 1. Finalidade

Este documento define o programa funcional de um ambiente documental capaz de visualizar, relacionar e inspecionar as jornadas de **Pessoa**, **Coletivo** e **Organização** sem duplicar artefatos canônicos, ocultar lacunas ou transformar uma representação de arquitetura em produto implementado.

O ambiente deverá permitir responder:

> **Quem participa desta jornada, em qual papel, por quais superfícies passa, qual autoridade governa cada decisão, quais transições existem, qual é a maturidade de cada referência e onde ainda há lacunas?**

A UXA-070 estabelece estrutura, taxonomias, critérios de reutilização e regras de governança. Ela não cria aplicativo, protótipo navegável, motor de simulação, componentes técnicos ou novas telas do produto.

### Regra de leitura após a reconciliação de 2026-08-30

`UXA-015`, `UXA-016`, `UXA-017` e `UXA-018` estão `superseded` e permanecem neste documento somente como **proveniência histórica** quando mencionadas no corpo. Elas não são dependências nem autoridades funcionais vigentes da UXA-070.

O modelo funcional, as taxonomias e as regras de governança deste programa continuam úteis. Entretanto, afirmações temporais deste documento sobre quantidades, materialização, validação, lacunas ou “próximo ato” registram o **snapshot do estágio em que a UXA-070 foi criada** e não devem ser interpretadas como maturidade atual do corpus. Para estado vigente de Organização/Coletivo prevalecem `UXA-014`, `UXA-019`, `GKR-UX-ORGCOL-AUTH-JOBS-001`, `GKR-UX-ORGCOL-AUTH-IA-001` e os registries/autoridades atuais.

```text
JOBS + AUTHENTICATED IA
→ DEFINED DOCUMENTALLY
→ PRE-SURFACE-MAP

FINAL SURFACE MAP
→ PENDING

MAIN AUTHENTICATED WIREFRAMES
→ PENDING
```

Nenhuma leitura da UXA-070 reativa baselines `superseded` ou autoriza surface map, wireframe, UI, protótipo ou implementação.

## 2. Decisão estrutural

O ambiente será uma **camada de leitura e composição por referência**.

```text
artefatos e autoridades canônicas
→ registro de nós e transições
→ perspectivas por participante e papel
→ sobreposição de maturidade, autoridade e lacunas
→ cenários documentais inspecionáveis
```

Ele nunca se torna fonte de verdade sobre a experiência. Em caso de divergência, prevalecem os contratos, programas, wireframes, validações e registros canônicos referenciados.

## 3. O que significa simulação neste programa

Neste pacote, `simulação` significa:

- percorrer uma sequência documental possível;
- alternar a perspectiva de participantes e papéis;
- visualizar entradas, decisões, estados e saídas;
- identificar transições condicionais, protegidas ou pendentes;
- comparar o que cada participante conhece em um mesmo ponto;
- localizar autoridades, dependências e lacunas;
- verificar se uma continuidade possui cobertura materializada e validada.

Não significa:

- executar lógica de negócio;
- imitar comportamento de uma aplicação real;
- produzir dados sintéticos como se fossem fatos;
- prever decisões de pessoas;
- preencher estados ausentes por inferência;
- testar usabilidade ou desempenho;
- substituir protótipo ou implementação.

## 4. Participantes estruturais

O ambiente reconhecerá exatamente três participantes estruturais.

| Participante | Natureza | Responsabilidade de leitura |
|---|---|---|
| Pessoa | indivíduo que explora, decide, participa, revisa e controla seus conteúdos e vínculos | compreender momento, escolhas, consequências, proteção e continuidade |
| Coletivo | formação voluntária reunida por propósito, causa, território, prática ou objetivo compartilhado | compreender propósito, participação, governança, atividades, proteção e relações |
| Organização | entidade institucional com identidade, autoridade, recursos, processos e responsabilidades | compreender capacidade, compromissos, oportunidades, relações e prestação de contas |

Publicidade, Guivos Ads, patrocinador, especialista, responsável e visitante não serão elevados a participantes estruturais quando atuarem como papéis, autoridades ou operadores dentro das jornadas existentes.

## 5. Papéis e perspectivas contextuais

Um participante poderá aparecer em perspectivas diferentes sem se tornar outra entidade.

| Perspectiva | Participante-base | Limite |
|---|---|---|
| visitante público | Pessoa | conhece somente conteúdo público e não adquire vínculo |
| pessoa autenticada | Pessoa | acessa estados protegidos sem autorização automática de processamento |
| solicitante | Pessoa | acompanha uma solicitação sem controlar a decisão protegida |
| participante de Coletivo | Pessoa | possui vínculo e permissões conforme papel aceito |
| responsável por Coletivo | Pessoa atuando em nome do Coletivo | exerce somente autoridade explicitamente concedida |
| representante institucional | Pessoa atuando em nome da Organização | exerce somente autoridade da unidade e do papel apresentados |
| autoridade protegida ou especialista | Pessoa em função limitada | decide somente o processo protegido correspondente |
| Organização apoiadora | Organização | apoia sem adquirir propriedade ou direção do Coletivo |
| operador econômico identificado | Organização ou capacidade Guivos Ads | financia exposição sem comprar relevância, reputação ou autoridade |
| observador de governança | Arquitetura e governança | inspeciona fontes e maturidade sem agir como usuário do produto |

A troca de perspectiva deverá modificar apenas o que contratos e autoridades permitem visualizar ou decidir.

## 6. Famílias de jornadas inventariadas

As declarações de materialização/validação desta seção são preservadas como snapshot histórico do estágio da UXA-070. O estado vigente deve ser lido nos registries e pacotes de validação atuais.

### 6.1 Jornada da Pessoa — início, compreensão e continuidade

```text
Home pública
→ entrada protegida
→ acesso, quando necessário
→ escolha de modalidade
→ expressão guiada por texto ou voz
→ ajuda temporária solicitada, quando escolhida
→ inventário e autorização específica
→ processamento visível
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje e continuidades autorizadas
```

Autoridades principais no estágio registrado: UXA-020, UXA-023, UXA-034 a UXA-037 e UXA-068 a UXA-069.

No snapshot original da UXA-070, a família diretamente relacionada ao início protegido registrava 17 estados materializados e 17 validados. Essa contagem não é promovida a maturidade agregada vigente.

### 6.2 Jornada da Pessoa em Coletivos

A espinha dorsal P0A registrada no programa era:

```text
Explorar Coletivos
→ Resultados de Busca
→ Perfil Público
→ Revisão e Solicitação de Participação
→ Solicitação Pendente
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

No snapshot original, as cinco primeiras referências eram tratadas como materializadas e validadas, enquanto `Meus Coletivos`, Central de Atualizações e a reformulação do Início do Participante eram registradas como não iniciadas. Esses estados são históricos e não substituem a maturidade atual publicada pelas autoridades posteriores.

### 6.3 Jornada do responsável por Coletivo

A perspectiva do responsável deverá organizar:

```text
representação e autoridade
→ momento coletivo
→ solicitações e vínculos
→ comunicação oficial
→ atividades, consultas e decisões
→ proteção e moderação
→ relações institucionais
→ evidências e responsabilidades
```

No estágio da UXA-070, a Visão Geral do Responsável prevista na UXA-059 era registrada como não iniciada. Esse estado é **proveniência histórica**; a maturidade posterior deve ser lida nas UXA e registries vigentes e não pode ser regredida por este programa.

### 6.4 Jornada da Organização

A perspectiva institucional deverá relacionar:

```text
identidade, unidade e autoridade
→ momento institucional
→ responsabilidade material atual
→ jornadas e compromissos apoiados
→ capacidade e condições
→ oportunidades e programas
→ evidências de avanço institucional
→ relações com Coletivos e Organizações
→ decisões e Próximos Passos justificados
```

No estágio original da UXA-070, `UXA-015` e `UXA-017` eram usadas como referências materializadas/validadas da Visão Geral da Organização. Ambas estão hoje `superseded`; essa afirmação é preservada somente como **proveniência histórica** e não constitui baseline vigente nem dependência funcional. A experiência autenticada atual é governada pelas autoridades vigentes de Organização/Coletivo; Jobs + IA autenticada estão definidos em `pre-surface-map`, enquanto mapa final de superfícies e wireframes principais autenticados permanecem pendentes.

### 6.5 Relação entre Organização e Coletivo

A relação bilateral será tratada como jornada própria de governança:

```text
rascunho
→ proposta
→ avaliação bilateral
→ negociação
→ aprovação pelas duas autoridades
→ relação ativa
→ revisão
→ renovação, ajuste, pausa ou encerramento
```

Cada transição deverá preservar finalidade, autoridade, compromissos, recursos, dados, autonomia, contestação e saída.

### 6.6 Opportunity Boost como sobreposição comercial

Opportunity Boost não será tratado como participante nem como eixo obrigatório das jornadas humanas.

Ele será uma camada comercial identificada que poderá aparecer somente onde seu contrato permitir, preservando:

- separação entre conteúdo orgânico e patrocinado;
- publicidade identificada;
- ausência de compra de reputação ou legitimidade;
- ausência de autoridade sobre Pessoas ou Coletivos;
- no snapshot original do programa, 46 artefatos materializados, dos quais 36 validados e 10 pendentes; essa contagem é histórica e não representa maturidade agregada vigente.

## 7. Unidade funcional do ambiente

A unidade mínima será um **nó de jornada** referenciado.

Cada nó deverá registrar:

| Campo | Conteúdo |
|---|---|
| identificador do nó | chave estável do registro no ambiente |
| participante | Pessoa, Coletivo ou Organização |
| perspectiva ou papel | posição contextual autorizada |
| família de jornada | agrupamento funcional |
| superfície ou estado | nome compreensível da referência |
| artefato canônico | ID e caminho do documento ou SVG |
| autoridade governante | contrato, programa ou validação aplicável |
| canal | móvel, computador, público, protegido ou não definido |
| versão | versão do artefato referenciado |
| maturidade | estado controlado da seção 10 |
| entrada | condições para chegar ao nó |
| decisão principal | ação ou escolha material disponível |
| saída | efeitos e possíveis destinos |
| dados e conteúdos | itens apresentados, produzidos ou compartilhados |
| gate | autenticação, consentimento, autoridade ou aprovação necessária |
| reversibilidade | possibilidade e efeito de voltar, cancelar, pausar ou corrigir |
| lacunas | ausências ou incertezas conhecidas |
| supersessão | referência vigente, substituída ou arquivada |

O ambiente não deverá inventar valor para campos ainda não definidos.

## 8. Unidade funcional de transição

Cada ligação deverá ser registrada como transição explícita.

| Campo | Pergunta respondida |
|---|---|
| origem e destino | de onde para onde a jornada pode seguir? |
| participante e papel | quem percebe ou executa a transição? |
| tipo | qual taxonomia da seção 11 se aplica? |
| condição | o que precisa ser verdadeiro? |
| autoridade | quem pode decidir ou confirmar? |
| ação | qual ato inicia a mudança? |
| efeito | o que muda e o que permanece? |
| dados | qual conteúdo cruza a fronteira? |
| autorização | qual finalidade foi autorizada? |
| reversibilidade | é possível cancelar, corrigir ou retornar? |
| interrupção | o que acontece se a jornada parar? |
| tempo | é imediata, futura ou pendente? |
| evidência | qual documento sustenta a ligação? |
| lacuna | a transição está ausente, parcial ou contestada? |

Uma seta visual sem esses elementos não será considerada transição governada.

## 9. Módulos documentais previstos

O ambiente futuro deverá ser composto, no mínimo, por:

1. **seletor de participante e perspectiva**;
2. **mapa da jornada selecionada**;
3. **painel de detalhe do nó**;
4. **painel de detalhe da transição**;
5. **sobreposição de maturidade**;
6. **visão de autoridades e dependências**;
7. **visão de handoffs entre participantes**;
8. **fila de lacunas e continuidades ausentes**;
9. **painel de fontes, versões e supersessões**;
10. **vista textual ordenada equivalente ao mapa**.

Esses módulos são requisitos de organização documental, não componentes implementados.

## 10. Estados de maturidade

| Estado | Significado |
|---|---|
| contratado | responsabilidade definida por contrato funcional |
| programado | incluído em programa governado, sem materialização visual obrigatória |
| materializado | referência visual ou documental específica existente |
| validado | referência examinada por pacote de validação funcional |
| reformulação pendente | materialização existente com correção funcional ainda necessária |
| não iniciado | responsabilidade conhecida sem pacote de materialização iniciado |
| bloqueado | avanço impedido por dependência ou decisão não resolvida |
| supersedido | substituído por referência posterior identificada |
| arquivado | mantido apenas como histórico, fora do estado vigente |
| indeterminado | evidência insuficiente para classificar com segurança |

O ambiente deverá mostrar maturidade em texto e não somente por cor.

## 11. Tipos de transição

| Tipo | Uso |
|---|---|
| direta | continuidade imediata sustentada pela mesma perspectiva |
| condicional | depende de escolha, elegibilidade, estado ou informação |
| protegida | exige autenticação, consentimento ou autoridade específica |
| assíncrona | aguarda decisão, prazo, processamento ou evento futuro |
| handoff de autoridade | transfere a próxima decisão para outro papel legítimo |
| entre participantes | conecta Pessoa, Coletivo ou Organização sem fundir suas autoridades |
| externa | conduz a destino fora da superfície atual com origem identificada |
| reversível | permite retorno ou cancelamento com efeito conhecido |
| destrutiva | remove conteúdo, vínculo ou estado e exige confirmação apropriada |
| ausente | destino necessário conhecido, mas não materializado ou contratado |
| proibida | ligação que não poderá ocorrer por regra de proteção ou governança |

Uma transição poderá possuir mais de um tipo, desde que cada condição permaneça explícita.

## 12. Perspectivas de visualização

### 12.1 Por participante

Mostra somente nós e transições percebidos pela Pessoa, pelo Coletivo ou pela Organização.

### 12.2 Por papel

Mostra diferenças reais de autoridade entre visitante, solicitante, participante, responsável, representante institucional e autoridade protegida.

### 12.3 Por handoff

Expõe onde uma decisão sai de uma perspectiva e passa a outra, por exemplo:

```text
Pessoa envia solicitação
→ autoridade protegida analisa
→ Pessoa recebe estado ou decisão
→ eventual vínculo passa a ser governado pelo Coletivo
```

### 12.4 Por maturidade

Revela continuidade validada, materializada sem validação, programada, não iniciada, bloqueada ou ausente.

### 12.5 Por autoridade

Permite identificar qual documento governa cada nó e transição e quais permissões não podem ser presumidas.

### 12.6 Por finalidade e dados

Mostra onde conteúdo é apenas visualizado, compartilhado, temporariamente processado, autorizado para compreensão, persistido ou utilizado para personalização.

## 13. Filtros e rastreabilidade

O ambiente deverá permitir filtrar ou agrupar por:

- participante;
- perspectiva ou papel;
- família de jornada;
- canal;
- maturidade;
- pacote de materialização;
- pacote de validação;
- versão;
- autoridade;
- finalidade;
- tipo de transição;
- estado de autorização;
- presença de lacuna;
- referência vigente ou supersedida.

Cada nó deverá permitir rastrear dependências anteriores e continuidades posteriores sem alterar o artefato canônico.

## 14. Reutilização de artefatos canônicos

### 14.1 Referência, não cópia

O ambiente deverá apontar para o ID, caminho e versão do artefato existente. Não deverá copiar SVG, texto normativo ou conteúdo completo para criar uma segunda fonte.

### 14.2 Uma referência em múltiplas perspectivas

A mesma tela poderá aparecer em mais de uma jornada quando a superfície for realmente compartilhada. A diferença de perspectiva será registrada em metadados e transições, não por duplicação do arquivo.

### 14.3 Artefatos em modo somente leitura

Anotações, estados de maturidade, setas e comentários do ambiente permanecerão fora do arquivo canônico.

### 14.4 Versão fixada e atualização detectável

Cada uso deverá registrar versão e pacote de validação. Quando o artefato mudar, a referência será sinalizada como potencialmente desatualizada até reconciliação.

### 14.5 Sem transição inferida

Proximidade visual, numeração sequencial ou semelhança textual não autorizam uma ligação. Toda transição depende de autoridade documental identificada.

### 14.6 Sem promoção automática

A inclusão no ambiente não altera status, versão, maturidade, canonicidade ou prioridade do artefato.

### 14.7 Responsividade controlada

Um mesmo artefato poderá representar mais de um canal somente quando a autoridade vigente disser que a hierarquia não muda materialmente. Responsividade não cria referência automaticamente.

## 15. Registro de lacunas

O ambiente deverá tornar visíveis, no mínimo:

- superfície necessária ainda não iniciada;
- transição contratada sem referência visual;
- referência visual sem validação funcional;
- autoridade não resolvida;
- finalidade ou fronteira de dados não definida;
- papel sem permissão suficientemente explicada;
- entrada ou saída sem efeito conhecido;
- versão supersedida ainda referenciada;
- caminho inacessível ou artefato ausente;
- dependência bloqueadora;
- divergência entre registros;
- continuidade interrompida entre participantes.

Nenhuma lacuna será preenchida por tela genérica, conteúdo fictício ou seta presumida.

## 16. Cenários documentais mínimos

### 16.1 Início protegido da Pessoa

Deverá demonstrar a continuidade da Home pública até a compreensão inicial, distinguindo acesso, relato, ajuda temporária, autorização, processamento, persistência e personalização.

### 16.2 Descoberta e solicitação em Coletivos

Deverá percorrer Explorar, Busca, Perfil Público, Revisão, Solicitação e estados pendentes, encerrando na lacuna explicitamente registrada antes de `Meus Coletivos`.

### 16.3 Pessoa e Coletivo

Deverá mostrar mudança de autoridade entre decisão individual de solicitar, análise protegida, formação do vínculo e governança interna do Coletivo.

### 16.4 Organização e Coletivo

Deverá representar proposta, consentimento bilateral, relação ativa, revisão e saída, sem conceder propriedade ou autoridade automática a qualquer parte.

### 16.5 Aplicação institucional

Deverá conectar conhecimento individual validado ou generalizado a uma aplicação institucional somente quando PAS-001 e autoridades relacionadas permitirem, sem expor contexto pessoal individual indevido.

### 16.6 Sobreposição comercial

Deverá mostrar Opportunity Boost ou patrocínio apenas como camada identificada, sem alterar ordem orgânica, reputação, pertencimento, decisão protegida ou autoridade.

## 17. Regras de conteúdo e linguagem

O ambiente deverá:

- utilizar linguagem compreensível antes de identificadores técnicos;
- mostrar IDs e caminhos como rastreabilidade secundária;
- distinguir fato, inferência, estado documental e hipótese de continuidade;
- não chamar atividade, volume ou visualização de avanço humano;
- não afirmar que uma jornada está completa quando houver lacuna;
- não ocultar ausência de artefato por meio de cartões genéricos;
- não transformar programa futuro em funcionalidade existente;
- indicar claramente quando algo é cenário documental.

## 18. Acessibilidade documental

Uma futura materialização deverá:

- oferecer vista textual equivalente ao mapa;
- manter ordem lógica de leitura;
- identificar nós, transições e maturidade em texto;
- não depender de cor, posição ou animação;
- permitir navegação por teclado e tecnologia assistiva;
- fornecer títulos e descrições para artefatos visuais;
- preservar legibilidade com ampliação;
- permitir filtrar sem perder o contexto da seleção;
- anunciar mudanças de perspectiva e autoridade.

A UXA-070 não conclui acessibilidade técnica.

## 19. Governança e atualização

O ambiente deverá ser atualizado somente por pacote governado.

Uma atualização deverá registrar:

1. artefato ou autoridade alterada;
2. versão anterior e nova;
3. nós afetados;
4. transições afetadas;
5. mudança de maturidade;
6. lacunas abertas ou encerradas;
7. impacto em outras perspectivas;
8. necessidade de nova validação do mapa integrado.

Correções no ambiente não poderão alterar silenciosamente os documentos de origem.

## 20. Cobertura registrada no estágio da UXA-070

No snapshot original do programa, foram registradas as seguintes contagens:

| Família | Materializados | Validados | Pendentes conhecidos |
|---|---:|---:|---:|
| jornada pessoal relacionada ao início protegido | 17 | 17 | 0 |
| Coletivos | 22 | 22 | 0 entre os materializados |
| Opportunity Boost | 46 | 36 | 10 |

As contagens possuem escopos diferentes, não serão somadas como um único inventário global e **não representam a maturidade agregada vigente**. O estado atual deve ser obtido dos registries, catálogos e pacotes de validação vigentes.

No estágio histórico, a Organização possuía referências anteriores materializadas e validadas, incluindo sua Visão Geral. `UXA-015/017` estão hoje `superseded` e não constituem baseline funcional atual. A UXA-070 não declara cobertura visual institucional completa.

## 21. Critérios de saída do pacote

A UXA-070 estará programada quando:

- os três participantes estruturais estiverem definidos;
- papéis e perspectivas contextuais estiverem separados;
- as famílias mínimas de jornada estiverem inventariadas;
- o modelo de nó estiver definido;
- o modelo de transição estiver definido;
- maturidade e tipos de transição possuírem taxonomias controladas;
- módulos documentais e filtros estiverem especificados;
- regras de reutilização canônica estiverem estabelecidas;
- lacunas não puderem ser ocultadas ou preenchidas por suposição;
- cenários documentais mínimos estiverem identificados;
- limites entre programa, materialização e implementação estiverem explícitos;
- os registros de governança estiverem sincronizados;
- a validação mecânica do Repositório for aprovada.

## 22. Limites

A UXA-070 não:

- cria SVG, mapa integrado ou tela do ambiente;
- implementa software ou motor de simulação;
- cria protótipo navegável;
- testa jornadas com pessoas;
- define identidade visual;
- cria componentes, API, banco ou modelo de dados técnico;
- utiliza dados pessoais ou de produção;
- gera comportamento por IA;
- valida automaticamente artefatos existentes;
- resolve lacunas de `Meus Coletivos`;
- materializa Central de Atualizações, Início do Participante ou Visão Geral do Responsável;
- altera contratos de Organização, Coletivo ou Opportunity Boost;
- inicia UXA-071 por força deste documento;
- inicia Engenharia de Produto;
- reativa `UXA-015..018`;
- autoriza surface map, wireframe principal autenticado, UI, protótipo ou implementação.

## 23. Próxima transição registrada no estágio histórico

No estágio original, a recomendação era:

**UXA-071 — Materialização Documental do Mapa Integrado de Jornadas e Transições.**

Essa recomendação é **proveniência histórica**, não autorização nem próximo gate vigente. Qualquer continuidade atual deve seguir o Estado Atual/Roadmap e as autoridades vigentes após a auditoria integral.
