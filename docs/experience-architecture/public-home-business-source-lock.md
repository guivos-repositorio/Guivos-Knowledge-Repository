---
id: GKR-UX-HOME-BUSINESS-SOURCELOCK-001
title: Source Lock — Home Pública — Guivos Business
status: active
version: 1.1.11
owner: Experience Architecture
last_updated: 2026-09-21
parent: GKR-UX-HOME-BUSINESS-MASTER-001
depends_on:
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
  - GKR-STATE-001
  - ROADMAP-12.79.0
normative: true
---

# Source Lock — Home Pública — Guivos Business

## 1. Finalidade

Este documento consolida o **Source Lock da Home Pública do Guivos Business** após a convergência do Documento Mestre.

Seu papel é:

- congelar as fontes vigentes que governam a produção externa de Design da Home Business e as futuras etapas autorizadas;
- eliminar ambiguidades entre formulações anteriores e o Documento Mestre vigente;
- registrar as invariantes que não podem ser reinterpretadas por Design, UX, UI, ferramentas generativas ou implementação futura;
- separar claramente o que está congelado do que continua aberto;
- impedir que lacunas comerciais, visuais ou operacionais sejam preenchidas por inferência.

Este Source Lock **não é** o ato que concede Design Release; esse ato comum já está `GRANTED` para produção externa pela designer. O Source Lock também não é:

- wireframe;
- UI;
- protótipo;
- handoff para ferramenta generativa;
- especificação técnica do configurador;
- tabela comercial final;
- autorização de implementação ou publicação.

Regra:

> **Source Lock congela a fonte. Não autoriza, por si só, a materialização.**

## 2. Checkpoint do Source Lock

```text
HOME
Guivos Business

FASE
Source Lock reconciliado para handoff designer-first

ORIGIN CHECKPOINT
main @ 41dd34ca7f2a22776b8eea57d99ef1b77db82969
→ HISTORICAL PROVENANCE

RECONCILIATION
→ 2026-09-19
→ CURRENT DESIGNER-FIRST / AI-OPTIONAL CONTRACT APPLIES

DOCUMENTO MESTRE
GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.5

CONVERSÃO VIGENTE
GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.1

CONTRATOS DE AUTORIDADE
GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.4

ARQUITETURA FUNCIONAL
GPA-004 v1.7.2
```

Objetivo do lock:

> preservar uma fonte pública única, coerente e auditável para a produção externa vigente de Design da Home Business, sem reabrir decisões já validadas nem antecipar decisões comerciais ainda não congeladas.

## 3. Pacote de fontes autorizado

Para a produção externa de Design da Home Business, o pacote específico de autoridade deve ser restrito a:

1. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001` — este Source Lock;
2. `GKR-UX-HOME-BUSINESS-MASTER-001` v1.1.5 — `docs/experience-architecture/public-home-business-master-document.md`;
3. `GKR-UX-HOME-BUSINESS-CONVERSION-002` v1.0.0 — `docs/experience-architecture/public-home-business-conversion-authority-v2.md`;
4. `GKR-UX-HOME-BUSINESS-AUTHORITY-001` v1.0.3 — `docs/experience-architecture/public-home-business-authority-contracts.md`;
5. `GPA-004` v1.6.0 — arquitetura funcional vigente do Guivos Business.

Não adicionar automaticamente:

- checkpoints anteriores;
- rascunhos de conversa;
- benchmarks externos;
- outras Homes;
- materiais de pricing ainda não formalizados;
- telas internas;
- documentos de Ads;
- documentos históricos de Journey que não sejam necessários para resolver uma dúvida concreta.

Qualquer ampliação do pacote exige dúvida específica e decisão deliberada.

## 4. Ordem de autoridade

Quando houver dúvida futura, aplicar:

```text
NÍVEL 0
GKR-UX-HOME-BUSINESS-SOURCELOCK-001
→ governa o que está congelado para materialização

NÍVEL 1
GKR-UX-HOME-BUSINESS-MASTER-001
→ governa narrativa, arquitetura pública, movimentos e expressão da Home

NÍVEL 2
GKR-UX-HOME-BUSINESS-CONVERSION-002
→ governa contratação online e modelos de implementação/operação

NÍVEL 3
GKR-UX-HOME-BUSINESS-AUTHORITY-001
→ governa fronteiras de autoridade entre pessoa, empresa, Business, Journey, Incentivos, ecossistema e Intelligence

NÍVEL 4
GPA-004
→ governa arquitetura funcional/comercial do produto

HISTÓRICO
→ explica como decisões foram construídas
→ não substitui o estado vigente
```

Se uma formulação histórica divergir do Documento Mestre, prevalece o Documento Mestre salvo nova decisão explicitamente governada.

## 5. Centro semântico congelado

Pergunta-mãe:

> **O que sua empresa pode tornar possível para as pessoas?**

Tese:

> **Quando uma empresa amplia possibilidades para as pessoas, novas possibilidades também se abrem para a própria empresa.**

Promessa:

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

Princípio humano:

```text
PROPÓSITO
Ajudar seres humanos a terem uma vida melhor
↓
MEIO
Apoiar pessoas em sua evolução
↓
PRINCÍPIO
Criar condições e possibilidades sem decidir por elas
quem devem se tornar
```

Guardrail humano:

> **Empresas não definem quem as pessoas devem se tornar. Podem, porém, ampliar as condições e possibilidades para que elas construam vidas melhores.**

Assinatura de autonomia:

> **A empresa apoia. A pessoa escolhe.**

Esses elementos não podem ser substituídos silenciosamente por uma proposta centrada em produto, pontos, dashboard, produtividade, fidelidade ou software de RH.

## 6. Arquitetura pública congelada — 10 movimentos

A progressão semântica vigente é:

```text
01 — POSSIBILIDADE
O que sua empresa pode tornar possível para as pessoas?

02 — PROPÓSITO
Empresas também podem ajudar seres humanos a terem uma vida melhor

03 — AUTONOMIA
A empresa apoia. A pessoa escolhe.

04 — JOURNEY
Amplie o acesso à evolução

05 — INCENTIVOS
Reconheça. Incentive. Abra novas possibilidades.

06 — ECOSSISTEMA
Diferentes áreas da vida. Diferentes possibilidades.

07 — INTELLIGENCE
Compreenda os movimentos dentro da Guivos

08 — PLANOS
Encontre a capacidade adequada para sua empresa

09 — CONFIGURADOR / CONTRATAÇÃO
Configure. Compare. Contrate.

10 — SÍNTESE
O que sua empresa pode tornar possível?
```

Os dez movimentos são funções semânticas, não obrigação de dez blocos visuais equivalentes.

A materialização de Design pode agrupar movimentos, desde que preserve ordem de compreensão, significado e capacidade de reconhecimento de cada função.

## 7. Movimento 01 — Hero

Congelar:

### Headline

> **O que sua empresa pode tornar possível para as pessoas?**

### Supporting copy de referência

> **Amplie o acesso à evolução, reconheça movimentos positivos e crie novas possibilidades para funcionários e clientes.**

### Promessa

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

### CTA principal

> **Descubra o que sua empresa pode tornar possível**

### CTA secundário

> **Conheça o Guivos Business**

O primeiro contato não deve ser dominado por:

- Journey como produto isolado;
- Incentivos como plataforma de campanhas;
- planos;
- preços;
- dashboard;
- configurador;
- lista de funcionalidades;
- linguagem de RH;
- mecanismos transacionais.

## 8. Movimento 02 — Propósito

Preservar a direção:

> **Empresas também podem ajudar seres humanos a terem uma vida melhor.**

Formulações de referência:

> **Empresas fazem parte da vida das pessoas de muitas formas. E também podem criar condições para que novos caminhos, experiências e possibilidades se tornem acessíveis.**

> **Ajudar seres humanos a terem uma vida melhor também pode significar ajudá-los a avançar naquilo que fazem, vivem, buscam ou desejam construir para suas próprias vidas.**

Não transformar `vida melhor` em score, padrão universal, promessa de performance empresarial ou obrigação de evolução.

## 9. Movimento 03 — Autonomia

Congelar:

> **Apoiar a evolução não é escolher o caminho.**

> **Sua empresa pode criar condições, ampliar acesso e abrir novas possibilidades sem decidir pelas pessoas quem elas devem se tornar.**

Estrutura de autoridade:

```text
SUA EMPRESA
cria condições e amplia acesso
↓
GUIVOS
conecta caminhos e possibilidades
↓
CADA PESSOA
escolhe o que faz sentido para sua própria vida
```

Assinatura:

> **A empresa apoia. A pessoa escolhe.**

## 10. Movimento 04 — Guivos Journey

Congelar a formulação principal:

> **Sua empresa pode oferecer acesso ao Guivos Journey e permitir que seus funcionários encontrem caminhos, experiências e possibilidades de evolução relevantes para suas próprias vidas.**

Supporting copy:

> **Sua empresa amplia o acesso. Cada pessoa escolhe o próprio caminho.**

Invariante:

```text
EMPRESA
custeia o acesso
↓
GUIVOS JOURNEY
apresenta caminhos, experiências e possibilidades relevantes
↓
FUNCIONÁRIO
escolhe sua própria jornada
```

Não inferir:

- Journey Corporativo;
- Journey Business;
- trilha empresarial obrigatória;
- seleção empresarial de temas pessoais;
- exposição de Journey individual à empresa;
- transformação do Journey em LMS/LXP.

## 11. Movimento 05 — Incentivos

Congelar a arquitetura pública unificada:

> **Reconheça. Incentive. Abra novas possibilidades.**

Formulação principal de referência:

> **Sua empresa pode reconhecer movimentos, incentivar novos passos e tornar novas possibilidades acessíveis para funcionários e clientes.**

Formulação complementar:

> **Um incentivo pode reconhecer algo que aconteceu, estimular algo que está começando ou simplesmente tornar possível algo que antes não estava ao alcance daquela pessoa.**

O movimento pode comunicar reconhecimento, estímulo, viabilização e abertura de possibilidades.

Não separar `Benefícios` como movimento público autônomo.

Não reduzir a seção a lista de KPIs empresariais, campanhas de assiduidade ou recompensas pelo passado.

## 12. Pontos Guivos — exclusão pública congelada

Regra:

> **Pontos Guivos não aparecem na Home Pública do Guivos Business.**

Pontos permanecem capacidade funcional/econômica do produto, mas são mecanismo interno para efeitos da narrativa desta Home.

Não mencionar publicamente nesta Home:

- saldo;
- acumular pontos;
- trocar pontos;
- pontuação;
- carteira;
- lotes;
- validade;
- equivalência;
- checkout por pontos;
- liquidação;
- orçamento pré-pago.

A ausência pública de Pontos não altera sua arquitetura funcional em `GPA-004`.

## 13. Movimento 06 — Ecossistema

Congelar:

> **Uma possibilidade pode levar a muitas outras.**

> **Diferentes áreas da vida. Diferentes possibilidades. Um ecossistema que pode conectá-las.**

A unidade narrativa é a vida da pessoa antes do catálogo de produtos.

Dimensões possíveis:

- finanças;
- saúde e bem-estar;
- desenvolvimento;
- viagens e experiências;
- produtos e presentes;
- interesses;
- relações;
- outras possibilidades.

Journey, Travel, Mall e outras capacidades podem aparecer como infraestrutura secundária.

Princípio:

> **A Guivos não determina que tipo de evolução deve acontecer. Ela aumenta o universo de possibilidades a partir do qual cada pessoa pode escolher.**

Não transformar esta seção em grade de logos/produtos Guivos.

## 14. Movimento 07 — Guivos Intelligence

Congelar a direção principal:

> **Entenda como as pessoas participam, utilizam e se movimentam entre as possibilidades que escolhem dentro do ecossistema Guivos.**

Supporting copy de referência:

> **Visualize participação, recorrência, utilização, interesses agregados e movimentos ao longo do tempo para compreender cada vez melhor suas iniciativas dentro da Guivos.**

### Significado analítico preservado — expressão visual livre

A solução de Design deve conseguir tornar compreensíveis conceitos como participação, utilização, recorrência, evolução temporal, tendências, interesses agregados, movimentos e distribuições quando forem relevantes à narrativa.

Esses conceitos governam **o que precisa ser comunicável**, não **como deve ser representado visualmente**.

Nenhum dashboard, KPI, gráfico, card, tabela ou linguagem analítica específica é obrigatório. A designer pode escolher qualquer forma de expressão visual adequada — inclusive soluções que não utilizem esses recursos — desde que preserve significado, evidência, privacidade, hierarquia e os limites de autoridade vigentes.

Quando números, indicadores ou exemplos forem apresentados como reais, exigem fonte e autoridade aplicáveis. Representações conceituais não podem ser confundidas com prova operacional.

### CTA congelado

> **Conheça o Guivos Intelligence**

Destino arquitetônico:

```text
HOME GUIVOS BUSINESS
↓
MOVIMENTO INTELLIGENCE
↓
CONHEÇA O GUIVOS INTELLIGENCE
↓
HOME PRÓPRIA DO GUIVOS INTELLIGENCE
```

A autoridade documental da Home própria do Guivos Intelligence já existe. O destino deve ser preservado sem inventar URL pública, publicação ou disponibilidade operacional enquanto essas superfícies não forem formalmente liberadas.

## 15. Fronteiras do Intelligence preservadas

A Home comunica positivamente o que Intelligence entrega; não precisa carregar a copy principal com explicações defensivas sobre o que ele não faz.

Ainda assim, qualquer materialização de Design deve preservar silenciosamente:

- Intelligence analisa aquilo que ocorre e é legitimamente conhecido dentro do ecossistema Guivos;
- não transforma interesse em condição;
- não transforma intenção em diagnóstico;
- não cria score individual de evolução;
- não expõe Journey individual à empresa;
- não atribui causalidade empresarial sem base válida;
- não se torna auditor automático de KPIs internos da empresa.

Essas fronteiras são governadas por `GKR-UX-HOME-BUSINESS-AUTHORITY-001`.

## 16. Movimento 08 — Planos

Congelar os quatro planos e sua direção:

```text
START
Comece a operar.

GROWTH
Acompanhe e compreenda.

SCALE
Interprete e integre.

ENTERPRISE
Governe em alta complexidade e escala.
```

O pricing de referência vigente, governado economicamente e refletido em `docs/plans/business.md`, é:

| Plano | Mensal | Anual |
|---|---:|---:|
| Start | R$ 299,00 | R$ 2.990,00 |
| Growth | R$ 799,00 | R$ 7.990,00 |
| Scale | a partir de R$ 1.990,00 | contrato anual |
| Enterprise | sob consulta | contrato anual |

Esses valores constituem **baseline comercial de referência vigente no GKR**. Eles não equivalem, isoladamente, a autorização automática de cobrança, publicação irrestrita da oferta ou inferência de entitlements ainda não formalizados.

A Home deve permitir comparação entre planos por matriz, tabela ou interação equivalente.

A existência do comparativo **não autoriza inventar**:

- preços diferentes da baseline comercial vigente;
- limites quantitativos;
- número de usuários;
- quantidade de campanhas;
- SLA;
- API;
- SSO;
- entitlements;
- suporte específico por plano;
- funcionalidades exclusivas ainda não formalizadas.

Regra:

> **Plano governa capacidade; não representa qualidade humana, mérito ou nível de evolução.**

## 17. Movimento 09 — Configurador e contratação

Congelar:

> **Configure. Compare. Contrate.**

Supporting copy:

> **Encontre a configuração adequada para sua empresa, compare as capacidades disponíveis, conheça o valor e contrate online.**

O componente deve ser concebido como **configurador comercial**, não apenas calculadora simples.

A composição Self-service deve preservar as seguintes dimensões, quando aplicáveis e formalizadas:

| Dimensão | Papel |
|---|---|
| Oferta | Programas de Incentivo, Journey custeado ou ambas |
| Escala | participantes, acessos e demais volumes formalizados |
| Intelligence | profundidade/capacidades aplicáveis |
| Integrações | eventos, conexões e integrações autorizadas |
| Governança | requisitos de gestão e controle |
| Nível de serviço | entitlement contratual aplicável |
| Implementação/operação | Self-service, suporte ou gerenciado |
| Orçamento de incentivo | recurso pré-pago separado da assinatura |
| Acessos Journey custeados | relação econômica própria |

Regra congelada de leitura:

```text
CONFIGURAÇÃO ESCOLHIDA
→ REQUISITOS DE CAPACIDADE
→ PLANO QUE SUPORTA INTEGRALMENTE OS REQUISITOS
→ VALOR DA CONFIGURAÇÃO
```

O plano não é escolhido apenas pelo preço nem resulta de uma soma arbitrária de módulos. Ele representa a camada de capacidade que comporta a configuração contratada.

O valor deve ser legível em parcelas distintas:

```text
PLANO BUSINESS
+ COMPONENTES VARIÁVEIS APLICÁVEIS
+ SERVIÇOS ADICIONAIS, QUANDO CONTRATADOS

ORÇAMENTO PRÉ-PAGO DE INCENTIVO
→ RECURSO OPERACIONAL SEPARADO
```

Os thresholds quantitativos, entitlements, SLAs, preços unitários e fórmulas exatas ainda não formalizados não podem ser inventados pelo Design ou pelo configurador conceitual.

Resultado conceitual:

```text
PLANO / CONFIGURAÇÃO
+
CAPACIDADES
+
VALOR OU ESTIMATIVA
+
MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
+
PRÓXIMO PASSO
```

## 18. Contratação online — regra congelada

> **A contratação do Guivos Business é online.**

Fluxo de referência:

```text
CONFIGURAÇÃO
↓
VALOR
↓
CONTRATAÇÃO ONLINE
↓
PAGAMENTO / FORMALIZAÇÃO
↓
IMPLEMENTAÇÃO
```

Não reintroduzir como categorias paralelas de contratação:

- Online;
- Assistida;
- Especializada.

Essas categorias foram supersedidas.

## 19. Modelos de implementação/operação congelados

A diferença entre operações ocorre depois da contratação e é representada por:

### Self-service

A empresa contrata online, acessa a plataforma, configura e opera com autonomia.

### Com apoio do suporte

A empresa contrata e paga online normalmente. Depois da contratação, o suporte Guivos acompanha a continuidade da implementação quando necessário.

### Gerenciado

A empresa contrata online e, depois, a implementação/operação recebe participação mais profunda da Guivos conforme complexidade e contrato.

Síntese:

> **Self-service quando possível. Suporte quando necessário. Operação gerenciada quando a complexidade exigir.**

Não converter `Com apoio do suporte` em etapa comercial obrigatória anterior à compra.

## 20. Escala global congelada como princípio

A Home e o configurador devem nascer preparados conceitualmente para adaptação por mercado, quando aplicável, em dimensões como:

- idioma;
- país/região;
- moeda;
- entidade contratante;
- faturamento;
- tributação;
- meios de pagamento;
- disponibilidade de produtos/capacidades;
- requisitos regulatórios;
- privacidade;
- suporte;
- modelo de implementação/operação.

Isso não autoriza afirmar disponibilidade universal.

Não pressupor estruturalmente:

```text
BRASIL
+
REAL
+
VENDEDOR HUMANO
+
CONTRATO MANUAL
```

## 21. Movimento 10 — Síntese

Congelar:

### Headline

> **O que sua empresa pode tornar possível para as pessoas?**

### Síntese

> **Amplie o acesso. Reconheça movimentos. Abra novas possibilidades.**

### Síntese humana

> **Apoie pessoas em sua evolução e ajude seres humanos a terem uma vida melhor.**

### Promessa

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

### CTA principal

> **Descubra o que sua empresa pode tornar possível**

O CTA pode conduzir ao configurador/qualificação apropriado sem exigir contato humano como primeira etapa.

## 22. Percepção que precisa sobreviver à materialização

A Home não pode terminar parecendo:

- software de RH;
- LMS/LXP;
- plataforma de pontos;
- programa de cashback/rewards;
- software de fidelidade;
- dashboard empresarial;
- catálogo de produtos Guivos;
- página de pricing sem narrativa;
- plataforma de Ads;
- ferramenta de controle individual das pessoas.

A percepção pretendida é:

```text
VIDA MELHOR
↓
EVOLUÇÃO
↓
POSSIBILIDADES
↓
A EMPRESA PODE APOIAR
↓
A GUIVOS TORNA ESSA CAPACIDADE OPERÁVEL
↓
ESCALA GLOBAL
```

## 23. Liberdades correntes de Design

No regime comum vigente, `DESIGN PRODUCTION RELEASE = GRANTED` para produção externa pela designer. Dentro das invariantes semânticas e funcionais deste Source Lock, a designer pode explorar:

- grid;
- composição;
- agrupamento visual dos dez movimentos;
- ritmo e número de dobras;
- hierarquia tipográfica;
- direção de imagem;
- tratamento visual do Journey;
- representação do ecossistema;
- representação conceitual do Intelligence;
- apresentação e comparação dos planos;
- interação do configurador;
- estados Self-service / Suporte / Gerenciado;
- Header, navegação e CTAs;
- responsividade desktop/mobile;
- microinterações e motion conceituais;
- tipografia provisória;
- iconografia.

Essas liberdades não podem alterar significado, autoridade ou promessas congeladas neste Source Lock.

## 24. Proibições de inferência

Não inventar como vigentes:

- clientes;
- logos de empresas clientes;
- depoimentos;
- cases;
- quantidade de empresas;
- quantidade de pessoas atendidas;
- países ativos;
- moedas ativas;
- preços diferentes da baseline comercial vigente;
- descontos não formalizados;
- limites por plano;
- SLA;
- entitlements;
- integrações disponíveis;
- APIs disponíveis;
- SSO;
- formas de pagamento;
- condições tributárias;
- métricas reais de Intelligence;
- dados reais de usuários;
- dashboards operacionais prontos;
- percentuais de participação;
- resultados empresariais causais;
- funcionalidades do configurador ainda não especificadas;
- URL pública do Guivos Intelligence;
- disponibilidade universal de contratação;
- suporte 24/7;
- operação gerenciada em todos os mercados.

Não transformar exemplos em capacidades vigentes.

## 25. Placeholders permitidos durante Design

Durante Design, quando necessário para testar hierarquia, volume, comportamento ou compreensão, podem ser utilizados rótulos explícitos, por exemplo:

- `[EMPRESA — EXEMPLO NÃO REAL]`;
- `[VISUALIZAÇÃO ANALÍTICA — CONCEITUAL]`;
- `[INDICADOR — EXEMPLO / NÃO REAL]`;
- `[RELAÇÃO OU TENDÊNCIA — ILUSTRATIVA]`;
- `[PREÇO — A DEFINIR]`, somente quando a dimensão ainda não possuir baseline vigente;
- `[LIMITE DO PLANO — A DEFINIR]`;
- `[MOEDA — CONFORME MERCADO]`;
- `[CONFIGURAÇÃO — EXEMPLO]`;
- `[INTEGRAÇÃO — NÃO DEFINIDA]`.

Placeholders devem ser inequivocamente não reais.

## 26. Lacunas deliberadamente abertas

Continuam fora deste Source Lock:

- condições finais de publicação/oferta dos preços e variações comerciais por mercado;
- limites e entitlements dos quatro planos;
- fórmula comercial do configurador;
- pricing por participante/acesso;
- preço de Journey custeado por empresa;
- níveis comerciais exatos de Intelligence;
- critérios exatos para Self-service, Suporte e Gerenciado;
- SLA;
- integrações e APIs finais;
- SSO;
- meios de pagamento por mercado;
- moedas suportadas;
- países suportados;
- regras fiscais e tributárias;
- arquitetura técnica do checkout/contratação;
- URL pública final e disponibilidade externa da Home Guivos Intelligence, quando ainda não formalizadas;
- o Documento Mestre da Home Guivos Intelligence **já existe** e não é lacuna futura;
- representações analíticas finais, indicadores e dados exatos do Intelligence;
- direção visual final da Home Business.

A produção externa de Design deve sinalizar essas lacunas quando materialmente relevantes, sem resolvê-las por inferência.

## 27. Contexto procedimental atual de Design

O regime corrente das oito Homes é governado pelas autoridades comuns posteriores a este Source Lock histórico:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.7.4
→ DESIGNER-FIRST
→ 8 / 8 HOMES

GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.3.1
→ DESIGN PRODUCTION RELEASE = GRANTED
→ EXTERNAL DESIGNER PRODUCTION

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED DESIGN / FIGMA
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```

Este Source Lock não concede sozinho Design Release nem implementação. Ele funciona como fonte semântica do Business dentro do pacote comum vigente e deve ser consumido em conjunto com as autoridades comuns atuais.

## 28. Conjunto corrente de fontes do Business

O consumo corrente da Home Business é resolvido pelo Manifesto canônico vigente no `main`.

Usar:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.7.4` como autoridade comum de handoff;
2. este Source Lock `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.9`;
3. `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.5`;
4. `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.1`;
5. `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.4`;
6. `GPA-004 v1.7.2`.

```text
SOURCE OF TRUTH
→ CURRENT MAIN

AUTHORIZED WHITELIST
→ CURRENT MANIFEST

SNAPSHOT / CANDIDATE
→ NOT REQUIRED

HISTORICAL PACKAGE
→ NOT OPERATIONAL INPUT
```

O conjunto somente pode ser reduzido se uma autoridade posterior absorver explicitamente as mesmas fronteiras sem perda semântica.

## 29. Autoauditoria do Source Lock

Antes de qualquer consumo de handoff para Design, confirmar:

- a pergunta-mãe permanece intacta?;
- evolução humana continua anterior ao produto?;
- a empresa apoia sem decidir o caminho da pessoa?;
- Journey aparece antes de Incentivos?;
- Journey financiado pela empresa não virou Journey controlado pela empresa?;
- Incentivos reconhecem, estimulam, viabilizam e abrem possibilidades?;
- Benefícios não reapareceram como movimento separado?;
- Pontos permanecem fora da Home?;
- ecossistema é apresentado pela vida da pessoa antes dos produtos?;
- Intelligence é visual e positivo sem inventar métricas reais?;
- CTA `Conheça o Guivos Intelligence` foi preservado?;
- Start, Growth, Scale e Enterprise permanecem comparáveis sem entitlements inventados?;
- o configurador aparece como mais do que calculadora de preço?;
- contratação continua online?;
- Self-service, Suporte e Gerenciado são modelos de implementação/operação, não formas diferentes de contratação?;
- suporte entra depois da contratação quando esse modelo é aplicável?;
- escala global não foi reduzida a Brasil + Real?;
- nenhum país, preço, moeda, cliente, KPI ou integração foi inventado como vigente?;
- a Home continua parecendo Guivos e não SaaS B2B genérico?;
- o Design preserva o regime designer-first, IA opcional e liberdade visual sem redefinir o produto?

## 30. Regra de mudança

Depois da integração deste Source Lock, qualquer alteração em:

- pergunta-mãe;
- tese;
- promessa;
- ordem semântica;
- Journey;
- papel dos Incentivos;
- exclusão pública de Pontos;
- papel do Intelligence;
- CTA para Intelligence;
- planos;
- contratação online;
- modelos de implementação/operação;
- princípio de escala global;

exige nova decisão explícita e atualização governada do Source Lock ou autoridade superior.

Design não pode alterar esses elementos por preferência estética.

## 31. Estado procedimental corrente

Este Source Lock integra o conjunto canônico corrente da Home Business.

```text
CURRENT MAIN
→ PRIMARY SOURCE OF TRUTH

CURRENT MANIFEST
→ RESOLVES AUTHORIZED VERSIONS

DESIGN PRODUCTION RELEASE
→ GRANTED

DESIGNER
→ CREATIVE AUTHOR

AI
→ OPTIONAL / DESIGNER-CONTROLLED

SNAPSHOT / CANDIDATE / REISSUE
→ NOT A PRECONDITION

GKR
→ DOES NOT CREATE OR ADVANCE DESIGN FILES

PRODUCT ENGINEERING
→ NOT RELEASED
```

Qualquer alteração semântica futura deve atualizar esta autoridade ou autoridade superior existente; não exige criar novo snapshot por padrão.

## 32. Síntese

> **O Source Lock congela o que a Home Guivos Business precisa significar. A forma poderá ser explorada depois; o significado não pode ser reinventado pela forma.**