---
id: GKR-UPDATE-PROGRAM-001
title: Programa Controlado de Atualização do Guivos Knowledge Repository
status: proposed
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-04
depends_on:
  - GKR-UPDATES-INVENTORY-001
  - GKR-STATE-001
  - ADR-003
  - ADR-004
  - ADR-005
related:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
  - GE2-SYNC-008
  - GEA-000
  - GPA-000
  - GBA-000
  - GEM-000
  - UXA-000
  - VAL-STATUS
  - GOG-001
normative: false
---

# Programa Controlado de Atualização do Guivos Knowledge Repository

## 1. Finalidade

Este programa transforma o inventário de atualizações acumuladas em uma sequência segura de pacotes independentes.

Seu objetivo é atualizar o repositório sem:

- misturar correção editorial com nova decisão arquitetural;
- apresentar intenção como execução;
- transformar arquivo externo em autoridade;
- atualizar o Public Canon antes de tecnologia, operação, jurídico e privacidade;
- promover preço, produto, território, domínio ou entidade sem evidência;
- reabrir frentes congeladas ou pausadas por implicação;
- produzir uma grande alteração sem revisão intermediária;
- perder rastreabilidade entre fonte, decisão, consumidor e publicação.

## 2. Regra de execução

Cada pacote deverá possuir:

1. autorização própria para criação;
2. branch própria baseada na `main` vigente;
3. objetivo único e fronteiras explícitas;
4. fontes e autoridades identificadas;
5. classificação de maturidade;
6. matriz de documentos afetados;
7. validação mecânica;
8. validação semântica, quando aplicável;
9. Pull Request em rascunho;
10. autorização separada para integração.

A integração de um pacote não autoriza o seguinte.

## 3. Sequência geral

```text
P0 — Intake de evidências e bloqueio de autoridade
→ P1 — Ressincronização semântica global
→ P2 — Arquitetura de referência de tecnologia e grafo
→ P3 — Governança de marca, naming, domínios e ativos digitais
→ P4 — Atualização de evidências de mercado e validação empresarial
→ P5 — Arquitetura institucional, jurídica e da Fundação
→ P6 — Verdade operacional pública, privacidade e superfícies legais
→ P7 — Internacionalização e programa territorial
→ P8 — Rebaseline de produtos e ecossistema
→ P9 — Consolidação global e nova edição do Public Canon
```

P0 e P1 poderão ser preparados em sequência curta. Os pacotes P2 a P8 dependem das fontes aplicáveis. P9 somente poderá ocorrer após a conclusão ou classificação explícita das dependências anteriores.

## 4. Tipos de pacote

| Tipo | Finalidade | Pode criar decisão canônica? |
|---|---|---|
| Intake | registrar fonte, proveniência, escopo e maturidade | não |
| Correção | alinhar superfícies a autoridades existentes | não cria decisão temática |
| Arquitetura | definir responsabilidade, modelo e referência | sim, mediante gates próprios |
| Evidência | incorporar dados, execução e resultados verificáveis | não automaticamente |
| Política | definir regras jurídicas, operacionais ou de governança | sim, com autoridade competente |
| Publicação | traduzir autoridades vigentes para comunicação pública | não redefine arquitetura |
| Consolidação | sincronizar estado e consumidores após pacotes | não cria fatos retroativamente |

## 5. P0 — Intake de Evidências e Bloqueio de Autoridade

### 5.1 Objetivo

Criar um registro controlado das fontes recentes antes de qualquer promoção canônica.

### 5.2 Escopo inicial

- arquitetura Neo4j;
- plano de proteção corporativa de marca e ativos digitais;
- estado operacional de `guivos.ai`;
- domínios registrados, titulares, finalidade e estado;
- eventual Fundação Guivos e `guivos.org`;
- expansão ou intenção territorial;
- resultados posteriores da validação de mercado;
- parceiros, clientes, campanhas, contas e integrações operacionais;
- políticas, contratos e documentos jurídicos existentes.

### 5.3 Entregáveis

1. registro de fontes e proveniência;
2. matriz `afirmação → evidência → autoridade → maturidade`;
3. classificação de cada item como:
   - observado;
   - confirmado;
   - decidido;
   - planejado;
   - recomendado;
   - contratado;
   - implementado;
   - operacional;
   - contestado;
   - desconhecido;
4. lista de documentos ausentes;
5. mapa de informações públicas, internas, restritas e sensíveis;
6. recomendação de aceite, devolução, quarentena ou descarte documental.

### 5.4 Gates

- fonte identificável;
- data e versão conhecidas;
- responsável ou origem conhecida;
- natureza do documento compreendida;
- escopo e limitações explícitos;
- ausência de promoção automática;
- proteção de segredos, credenciais, dados pessoais e ativos sensíveis.

### 5.5 Fora do escopo

- atualizar estado global;
- criar ADR técnico;
- publicar lista completa de domínios;
- declarar Fundação constituída;
- declarar expansão executada;
- atualizar Public Canon.

### 5.6 Condição de saída

Todas as novidades relevantes deverão possuir fonte, classificação de maturidade e autoridade candidata antes de seguir para pacotes temáticos.

## 6. P1 — Ressincronização Semântica Global

### 6.1 Objetivo

Corrigir as superfícies globais usando exclusivamente fatos e autoridades já integrados à `main`.

### 6.2 Documentos principais

- `README.md`;
- `docs/index.md`;
- `CHANGELOG.md`;
- `mkdocs.yml`;
- `docs/project/canonical-consolidation-matrix.md`;
- eventuais índices de histórico e adendos;
- `scripts/validate_gkr.py` ou validador semântico separado;
- workflow de validação, se necessário.

### 6.3 Correções obrigatórias

- alinhar o marco das páginas de entrada ao `GKR-STATE-001`;
- remover estados antigos apresentados como vigentes;
- publicar os documentos recentes na navegação adequada;
- consolidar ou indexar os adendos posteriores;
- estabelecer política do changelog raiz;
- reduzir duplicação de estados extensos nas páginas de entrada;
- manter o Registro do Estado Atual como autoridade única;
- preservar históricos sem atribuir-lhes vigência.

### 6.4 Validação semântica mínima

O pacote deverá propor controle automatizado para verificar:

1. o marco exibido no README e na Home corresponde ao Registro do Estado Atual;
2. versões ou IDs globais referenciados existem;
3. documentos ativos obrigatórios possuem navegação ou exceção declarada;
4. o próximo ato descrito nas entradas não contradiz o Roadmap;
5. a Matriz central reconhece os adendos posteriores;
6. páginas de resumo não promovem preço, operação ou implementação além das autoridades.

### 6.5 Dependências

- nenhuma fonte externa necessária;
- usa somente a `main` vigente;
- poderá ocorrer logo após a integração do presente programa.

### 6.6 Fora do escopo

- Neo4j;
- domínios;
- Fundação;
- internacionalização;
- atualização de mercado;
- revisão pública temática;
- UXA-071.

### 6.7 Condição de saída

As superfícies globais deverão comunicar um único estado, uma única sequência e uma navegação compatível com os ativos integrados.

## 7. P2 — Arquitetura de Referência de Tecnologia e Grafo

### 7.1 Objetivo

Estabelecer a propriedade e a maturidade das decisões tecnológicas relacionadas ao Grafo Global, analytics e consumo executivo.

### 7.2 Dependência principal

P0 deverá registrar a fonte `Guivos_Arquitetura_Neo4j.pdf` e confirmar sua natureza.

### 7.3 Entregáveis candidatos

- fundação da Technology and Engineering Architecture;
- arquitetura de referência do Grafo Global;
- ADR de seleção tecnológica, se os gates forem atendidos;
- separação entre:
  - arquitetura permanente;
  - arquitetura de referência;
  - tecnologia selecionada;
  - prova de conceito;
  - ambiente provisionado;
  - produção;
- relação entre Neo4j, Graph Analytics, Guivos Intelligence, GraphRAG, Lakehouse ou Warehouse e Power BI;
- modelo inicial de segurança, privacidade, residência, continuidade, custo e observabilidade;
- critérios de substituição e portabilidade.

### 7.4 Decisões que exigem evidência adicional

- provedor de nuvem;
- região e disponibilidade contratadas;
- tier e preço;
- SLA;
- volume e performance;
- retenção e residência de dados;
- backup e recuperação;
- conectores e licenças;
- realidade de produção.

AWS somente poderá ser registrada como escolha quando existir uma fonte verificável. A existência de Neo4j Aura não autoriza presumir uma arquitetura AWS própria.

### 7.5 Gates

- ownership arquitetural definido;
- alinhamento com GEA, GIA, Product Architecture e Governance;
- independência conceitual preservada;
- avaliação de segurança e privacidade;
- avaliação de custo e lock-in;
- diferenciação entre recomendação e implementação;
- documentação oficial e data de revisão;
- estratégia de saída.

### 7.6 Fora do escopo

- provisionamento;
- código;
- migração;
- ingestão de dados reais;
- dashboard produtivo;
- Product Engineering.

## 8. P3 — Governança de Marca, Naming, Domínios e Ativos Digitais

### 8.1 Objetivo

Transformar o plano externo de proteção em um sistema governado, sem divulgar informações sensíveis nem presumir execução.

### 8.2 Dependência principal

P0 deverá registrar o plano de proteção e as evidências reais de titularidade, registro e controle.

### 8.3 Entregáveis candidatos

- política de naming e lançamento;
- modelo de inventário de marca e ativos digitais;
- níveis de criticidade;
- ownership e RACI;
- controles mínimos de domínio, DNS, e-mail e certificados;
- processo de aquisição, transferência, renovação e encerramento;
- monitoramento e resposta a incidente;
- classificação público, interno, restrito e secreto;
- matriz de marcas e nomes oficiais;
- auditoria transversal do nome Guivos Mall.

### 8.4 Regra de proteção

O GKR não deverá publicar:

- credenciais;
- códigos de recuperação;
- dados completos de registrador;
- contatos de contingência restritos;
- detalhes capazes de facilitar tomada de conta;
- inventário defensivo completo;
- vulnerabilidades ou incidentes ainda não tratados.

### 8.5 Gates

- validação jurídica especializada;
- titularidade comprovada;
- nomes oficiais reconciliados;
- controles técnicos diferenciados de recomendações;
- nenhuma afirmação de registro internacional sem protocolo;
- nenhuma afirmação de cobertura sem contrato ou evidência;
- revisão de confidencialidade.

### 8.6 Fora do escopo

- depósito de marca;
- compra de domínio;
- contratação de TMCH ou bloqueio;
- alteração de DNS;
- enforcement real;
- divulgação de inventário restrito.

## 9. P4 — Evidências de Mercado e Validação Empresarial

### 9.1 Objetivo

Atualizar o sistema de validação e os registros empresariais somente a partir de execução observável.

### 9.2 Dependências

- baseline `VAL-STATUS` vigente;
- fontes posteriores registradas pelo P0;
- definição do instrumento realmente aplicado;
- dados brutos e regras de qualidade disponíveis.

### 9.3 Entregáveis candidatos

- status de execução da pesquisa;
- versão do formulário aplicado;
- plano de amostragem executado;
- pré-teste e correções;
- planilha ou pipeline de tratamento;
- KPIs, IGV e gates calculados;
- relatório de qualidade e limitações;
- registro de entrevistas, landing pages, campanhas ou testes comerciais;
- vínculo com Candidate Outcomes;
- recomendações de manter, reformular, fundir, rejeitar ou continuar validando.

### 9.4 Regra central

```text
dado observado
→ qualidade e denominador
→ interpretação limitada
→ gate previsto
→ decisão humana
```

Não será aceita:

```text
interesse declarado
→ demanda confirmada
→ preço aprovado
→ Outcome canônico
```

### 9.5 Gates

- instrumento e versão identificados;
- consentimento e privacidade adequados;
- amostra e limitações descritas;
- denominadores reproduzíveis;
- resultados anteriores não misturados sem mapeamento;
- ausência de promoção automática de preços ou Outcomes;
- separação entre B2C, B2B, território e segmento.

### 9.6 Fora do escopo

- lançamento comercial;
- preço oficial;
- valuation;
- capacidade empresarial automática;
- Go-to-Market completo.

## 10. P5 — Arquitetura Institucional, Jurídica e da Fundação

### 10.1 Objetivo

Definir o estado institucional da eventual Fundação Guivos e suas relações com o ecossistema somente após evidência jurídica e decisão formal.

### 10.2 Dependências

- P0 com documentos de constituição, intenção ou estudo;
- P3 para marca e ativos;
- parecer jurídico e tributário;
- definição de titularidade e governança;
- relação com holding ou entidades operacionais.

### 10.3 Entregáveis candidatos

- distinção entre iniciativa social, programa interno, instituto, associação e fundação;
- propósito, escopo e beneficiários;
- governança e autoridade;
- financiamento e prestação de contas;
- relação com voluntariado, pontos, patrocínios e causas;
- separação de dados, marca, contratos e responsabilidades;
- critérios de uso de `guivos.org`;
- estado jurídico e operacional textual.

### 10.4 Gates

- forma jurídica validada;
- decisão formal de criação ou manutenção como hipótese;
- responsáveis identificados;
- funding e obrigações transparentes;
- conflito de interesse tratado;
- relação comercial e social separadas;
- política de dados e proteção de beneficiários;
- nenhuma aproximação religiosa coerciva ou condicionamento de benefício.

### 10.5 Fora do escopo

- constituição jurídica pelo GKR;
- captação;
- promessa pública de impacto;
- emissão de pontos sem cobertura;
- uso público de `guivos.org` sem estado comprovado.

## 11. P6 — Verdade Operacional Pública, Privacidade e Superfícies Legais

### 11.1 Objetivo

Alinhar o que a Guivos afirma publicamente ao que está realmente disponível, autorizado e protegido.

### 11.2 Dependências

- P0 para realidade operacional;
- P2 para tecnologia e dados;
- P3 para domínios e identidade;
- P5 para estado institucional;
- parecer jurídico e de privacidade.

### 11.3 Escopo candidato

- estado de `guivos.ai`;
- sites e produtos disponíveis;
- voz e transcrição;
- arquivos e extrações;
- localização;
- calendário;
- integrações;
- cookies e analytics;
- consentimento e finalidades;
- retenção, correção, exclusão e revogação;
- informações de terceiros;
- crianças e adolescentes, quando aplicável;
- termos de uso;
- política de privacidade;
- página oficial de domínios, aplicativos e contatos;
- atualização do Guia Oficial somente após os contratos especializados.

### 11.4 Regra de verdade operacional

Cada capacidade pública deverá possuir um estado explícito:

- disponível;
- piloto limitado;
- em desenvolvimento;
- planejada;
- indisponível;
- descontinuada;
- desconhecida.

### 11.5 Gates

- base legal e finalidade;
- operação correspondente;
- linguagem pública não enganosa;
- acessibilidade;
- segurança;
- consentimento separado quando necessário;
- canais de contato e exercício de direitos;
- revisão jurídica.

### 11.6 Fora do escopo

- liberar funcionalidade;
- operar IA;
- coletar dados;
- publicar políticas sem validação competente;
- declarar segurança absoluta.

## 12. P7 — Internacionalização e Programa Territorial

### 12.1 Objetivo

Governar decisões de país, idioma, domínio, marca, compliance e operação sem confundir proteção defensiva com lançamento.

### 12.2 Dependências

- P0 para evidência de intenção ou operação;
- P3 para marcas e domínios;
- P6 para superfícies legais;
- evidência de mercado e capacidade operacional;
- parecer local quando necessário.

### 12.3 Entregáveis candidatos

- taxonomia de estado territorial;
- scorecard de mercados;
- diferenciação entre:
  - proteção de marca;
  - domínio defensivo;
  - presença institucional;
  - validação de mercado;
  - piloto;
  - operação comercial;
- requisitos de idioma, suporte, moeda, pagamentos, tributos e dados;
- programa específico para Colômbia, Portugal ou outro país somente quando houver fonte;
- sequência de expansão e gates de saída.

### 12.4 Gates

- demanda ou hipótese identificada;
- capacidade de atendimento;
- titularidade e marca;
- privacidade e residência de dados;
- pagamentos e tributos;
- suporte e idioma;
- risco e reversibilidade;
- nenhum país apresentado como lançado sem operação comprovada.

### 12.5 Fora do escopo

- lançamento internacional;
- registro de marca;
- abertura de empresa;
- contratação local;
- compra automática de domínio.

## 13. P8 — Rebaseline de Produtos e Ecossistema

### 13.1 Objetivo

Atualizar a Arquitetura de Produtos e suas relações após evidências, decisões institucionais, tecnologia de referência e Business Capabilities suficientes.

### 13.2 Dependências

- P2 a P7, conforme o produto;
- Business Outcomes ainda sem Canon devem permanecer identificados;
- BA-CAP-001 não poderá ser presumida como concluída;
- Product Engineering continuará pausada até autorização própria.

### 13.3 Escopo candidato

- Guivos Journey;
- Guivos Mall;
- Guivos Travel;
- Guivos Business;
- Guivos Media;
- Guivos Intelligence;
- Guivos Ads;
- participantes Pessoa, Coletivo e Organização;
- relações entre produtos e Platform Layer;
- estado público, planejado e implementado;
- sobreposições comerciais;
- arquitetura da Fundação, quando aplicável;
- nomes e domínios oficiais.

### 13.4 Hipóteses em quarentena

Concepts como Passport, Mapa de Vida, rankings, tribos, desafios e recompensas deverão passar por avaliação própria de:

- aderência à Fundação;
- utilidade real;
- coerção e dependência;
- comparação social;
- segurança comportamental;
- privacidade;
- financiamento;
- fraude;
- impacto sobre autonomia;
- autoridade de produto.

Nenhum deles será incorporado por reaproveitamento de apresentações ou conversas anteriores.

### 13.5 Gates

- ownership arquitetural;
- necessidade e Outcome relacionados;
- capacidade correspondente;
- relação com produto e experiência;
- maturidade e evidência;
- limites econômicos e comerciais;
- proteção da Pessoa;
- ausência de duplicidade entre produtos;
- nomenclatura e marca reconciliadas.

### 13.6 Fora do escopo

- implementação;
- protótipo;
- backlog técnico;
- lançamento;
- alteração automática de planos e preços.

## 14. P9 — Consolidação Global e Nova Edição do Public Canon

### 14.1 Objetivo

Sincronizar o estado global e publicar uma nova tradução pública somente depois que os pacotes aplicáveis estiverem concluídos ou explicitamente classificados como pendentes.

### 14.2 Documentos candidatos

- Registro do Estado Atual;
- Roadmap;
- Painel de Conhecimento;
- Marcos Arquiteturais;
- Matriz de Consolidação Canônica;
- README;
- docs/index;
- CHANGELOG raiz;
- mkdocs;
- GEA;
- Product Architecture;
- Business Architecture;
- Economic Model;
- Intelligence Architecture;
- glossário;
- public/index;
- Guia Oficial da Guivos;
- índices de histórico.

### 14.3 Entregáveis

- uma única declaração de estado;
- matriz de decisões consolidada;
- navegação atualizada;
- changelog global consistente;
- glossário reconciliado;
- nova edição do Public Canon;
- política de arquivos históricos;
- tratamento dos ZIPs antigos da raiz sem exclusão automática;
- relatório final de consistência.

### 14.4 Gates

- todos os fatos públicos possuem autoridade;
- planos permanecem identificados como planos;
- produtos e operações possuem maturidade explícita;
- nenhuma informação restrita foi publicada;
- políticas jurídicas e de privacidade estão aprovadas, quando necessárias;
- validação mecânica aprovada;
- validação semântica aprovada;
- links e navegação aprovados;
- nenhuma frente futura foi iniciada por implicação.

### 14.5 Fora do escopo

- implementação técnica;
- lançamento de produto;
- operação internacional;
- campanha comercial;
- constituição de entidade;
- exclusão de histórico sem decisão própria.

## 15. Matriz de dependências

| Pacote | Depende de | Pode avançar sem evidência externa? |
|---|---|---|
| P0 | presente programa | sim, para criar o registro; fontes precisam ser entregues |
| P1 | estado atual integrado | sim |
| P2 | P0 técnico | não |
| P3 | P0 jurídico e de ativos | não |
| P4 | P0 de mercado e dados | não |
| P5 | P0 institucional; P3 parcial | não |
| P6 | P0; P2; P3; P5 conforme escopo | não |
| P7 | P0; P3; P6; evidência territorial | não |
| P8 | P2 a P7 conforme impacto; Business Architecture | parcialmente |
| P9 | pacotes anteriores concluídos ou classificados | não |

## 16. Prioridade

| Prioridade | Pacote | Justificativa |
|---|---|---|
| Urgente | P1 | entradas públicas do repositório contradizem o estado vigente |
| Alta | P0 | novidades não podem avançar sem fonte e maturidade |
| Alta | P2 | arquitetura Neo4j precisa de ownership e classificação antes de uso |
| Alta | P3 | marca e domínios exigem governança e proteção sensível |
| Alta | P6 | promessas públicas de dados dependem de políticas e verdade operacional |
| Média | P4 | evidência de mercado deve alimentar decisões, sem interromper governança |
| Média | P5 | Fundação depende de decisão e documentação jurídica |
| Média | P7 | internacionalização depende de capacidade e evidência territorial |
| Média | P8 | rebaseline de produto depende das definições anteriores |
| Final | P9 | consolida e publica o resultado dos pacotes |

## 17. Regra para trabalhos paralelos

P1 poderá ocorrer antes do fechamento completo do P0 porque usa somente autoridades já integradas.

P2, P3 e P4 poderão ser preparados em paralelo após seus respectivos itens do P0, desde que:

- cada um possua branch e PR próprios;
- não alterem as mesmas autoridades globais simultaneamente;
- não promovam fatos não verificados;
- a integração seja sequenciada;
- P9 permaneça bloqueado.

## 18. Controles de mudança

### 18.1 Matriz de impacto obrigatória

Todo pacote deverá declarar:

| Campo | Conteúdo esperado |
|---|---|
| fonte | documento, registro, dado ou decisão |
| autoridade proprietária | arquitetura ou domínio responsável |
| maturidade anterior | estado antes do pacote |
| maturidade proposta | estado após integração |
| consumidores | documentos afetados |
| fronteiras | o que não muda |
| rollback | como reverter ou superseder |
| revisão | condições futuras de reabertura |

### 18.2 Proibições

- pacote temático amplo sem inventário de fontes;
- atualização pública anterior à autoridade;
- uso de `consolidated`, `active`, `operational` ou `available` sem critério;
- declaração de parceria sem evidência;
- declaração de registro ou domínio sem titularidade e estado;
- declaração de tecnologia em produção com base em recomendação;
- declaração de preço oficial com base em baseline candidata;
- declaração de impacto social sem evidência;
- criação de nova sigla ou produto sem ownership;
- exclusão de histórico para ocultar divergência.

## 19. Critérios de aceite do programa

O programa será considerado pronto para integração documental quando:

- todos os achados do inventário possuírem pacote ou decisão de não tratar;
- a ordem respeitar dependências arquiteturais;
- P0 e P1 estiverem claramente separados;
- tecnologia, jurídico, mercado, Fundação, público, internacionalização e produto possuírem gates próprios;
- o Public Canon permanecer no final;
- nenhuma implementação estiver autorizada;
- UXA-071 permanecer não iniciada;
- cada pacote exigir autorização e integração separadas.

## 20. Estado proposto

```text
Program: GKR-UPDATE-PROGRAM-001
Version: 0.1.0
Nature: non-normative controlled plan
Global state changed: no
Global versions changed: no
Milestone created: no
Canonical thematic decisions created: no
Implementation authorized: no
UXA-071 started: no
First executable package recommended: P1 — Global Semantic Resynchronization
Parallel evidence package recommended: P0 — Evidence Intake and Authority Lock
```

## 21. Próxima transição recomendada

Após integração deste programa e mediante nova autorização separada:

> **Executar P1 — Ressincronização Semântica Global, limitado às autoridades já existentes na `main`.**

P0 deverá ser iniciado por autorização própria quando as fontes e evidências que serão entregues estiverem definidas.
