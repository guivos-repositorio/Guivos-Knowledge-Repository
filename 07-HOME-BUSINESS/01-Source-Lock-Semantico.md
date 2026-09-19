---
id: GKR-UX-HOME-BUSINESS-SOURCELOCK-001
title: Source Lock — Home Pública — Guivos Business
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-16
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

- congelar as fontes vigentes que podem governar a futura materialização da Home Business;
- eliminar ambiguidades entre formulações anteriores e o Documento Mestre vigente;
- registrar as invariantes que não podem ser reinterpretadas por Design, UX, UI, ferramentas generativas ou implementação futura;
- separar claramente o que está congelado do que continua aberto;
- impedir que lacunas comerciais, visuais ou operacionais sejam preenchidas por inferência.

Este Source Lock **não é**:

- autorização de Design;
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
Source Lock pré-Design

CHECKPOINT DO GKR
main @ 41dd34ca7f2a22776b8eea57d99ef1b77db82969

DOCUMENTO MESTRE
GKR-UX-HOME-BUSINESS-MASTER-001 v1.0.0

CONVERSÃO VIGENTE
GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0

CONTRATOS DE AUTORIDADE
GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0

ARQUITETURA FUNCIONAL
GPA-004 v1.6.0
```

Objetivo do lock:

> preservar uma fonte pública única, coerente e auditável para a futura materialização da Home Business, sem reabrir decisões já validadas nem antecipar decisões comerciais ainda não congeladas.

## 3. Pacote de fontes autorizado

Para qualquer futura materialização da Home Business, o pacote inicial de autoridade deve ser restrito a:

1. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001` — este Source Lock;
2. `GKR-UX-HOME-BUSINESS-MASTER-001` v1.0.0 — `docs/experience-architecture/public-home-business-master-document.md`;
3. `GKR-UX-HOME-BUSINESS-CONVERSION-002` v1.0.0 — `docs/experience-architecture/public-home-business-conversion-authority-v2.md`;
4. `GKR-UX-HOME-BUSINESS-AUTHORITY-001` v1.0.0 — `docs/experience-architecture/public-home-business-authority-contracts.md`;
5. `GPA-004` v1.6.0 — arquitetura funcional vigente do Guivos Business.

A autoridade narrativa anterior permanece histórica e explicativa, mas **não deve ser adicionada automaticamente ao pacote inicial de materialização**, pois o Documento Mestre já incorpora os refinamentos de precedência posteriores.

Não adicionar automaticamente:

- conversão v1 supersedida;
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

A futura materialização pode agrupar movimentos, desde que preserve ordem de compreensão, significado e capacidade de reconhecimento de cada função.

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

### Direção visual congelada

A futura materialização deve demonstrar Intelligence prioritariamente de forma visual, podendo utilizar representações de:

- dashboard;
- KPIs;
- gráficos;
- evolução temporal;
- participação;
- utilização;
- recorrência;
- tendências;
- interesses agregados;
- movimentos e distribuições.

Essas representações não autorizam métricas, números ou layout final inventados como reais.

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

A Home própria do Intelligence ainda não existe. O destino deve ser preservado sem inventar URL ou disponibilidade pública.

## 15. Fronteiras do Intelligence preservadas

A Home comunica positivamente o que Intelligence entrega; não precisa carregar a copy principal com explicações defensivas sobre o que ele não faz.

Ainda assim, qualquer futura materialização deve preservar silenciosamente:

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

A Home deve permitir comparação entre planos por matriz, tabela ou interação equivalente.

A existência do comparativo **não autoriza inventar**:

- preços;
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

Fatores candidatos podem incluir, quando formalizados:

- número de pessoas;
- oferta;
- plano/capacidade;
- tipo de operação;
- Intelligence;
- integrações;
- governança;
- serviço;
- mercado.

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

## 23. Liberdades futuras de Design

Somente após autorização procedimental específica para incluir Business na fase de Design, poderão ser explorados:

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
- preços;
- descontos;
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

## 25. Placeholders permitidos em futura exploração

Quando houver autorização de Design, poderão ser utilizados rótulos explícitos, por exemplo:

- `[EMPRESA — EXEMPLO NÃO REAL]`;
- `[DASHBOARD INTELLIGENCE — CONCEITUAL]`;
- `[KPI — EXEMPLO / NÃO REAL]`;
- `[GRÁFICO — DADO ILUSTRATIVO]`;
- `[PREÇO — A DEFINIR]`;
- `[LIMITE DO PLANO — A DEFINIR]`;
- `[MOEDA — CONFORME MERCADO]`;
- `[CONFIGURAÇÃO — EXEMPLO]`;
- `[INTEGRAÇÃO — NÃO DEFINIDA]`.

Placeholders devem ser inequivocamente não reais.

## 26. Lacunas deliberadamente abertas

Continuam fora deste Source Lock:

- preços finais;
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
- URL e Documento Mestre da futura Home Guivos Intelligence;
- dashboard final e KPIs exatos do Intelligence;
- direção visual final da Home Business.

A materialização futura deve sinalizar essas lacunas, não resolvê-las por inferência.

## 27. Bloqueio procedimental de Design

O handoff canônico vigente `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.1.0 cobre explicitamente seis Homes:

1. Pessoa;
2. Organizações e Coletivos;
3. Mall;
4. Travel;
5. Media;
6. Ads.

**Guivos Business ainda não está incluído nessa autorização.**

Consequência:

```text
SOURCE LOCK BUSINESS
→ PODE SER CONGELADO

DESIGN BUSINESS
→ AINDA NÃO AUTORIZADO

FERRAMENTA GENERATIVA
→ AINDA NÃO DEVE RECEBER EXECUÇÃO OPERACIONAL PARA BUSINESS
```

Este Source Lock não amplia silenciosamente o escopo do handoff canônico.

## 28. Pacote futuro de handoff do Business

Quando houver autorização explícita para Design, o pacote mínimo recomendado será:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` em versão que inclua Guivos Business;
2. este Source Lock;
3. `GKR-UX-HOME-BUSINESS-MASTER-001`;
4. `GKR-UX-HOME-BUSINESS-CONVERSION-002`;
5. `GKR-UX-HOME-BUSINESS-AUTHORITY-001`;
6. `GPA-004` v1.6.0 ou autoridade posterior vigente.

O pacote poderá ser reduzido somente se uma autoridade posterior consolidar explicitamente as mesmas fronteiras.

## 29. Autoauditoria do Source Lock

Antes de qualquer futura materialização, confirmar:

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
- Design só começou após autorização procedimental própria?

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

## 31. Próxima etapa

Após integração deste Source Lock, o próximo ponto governado é:

> **INCLUSÃO DO GUIVOS BUSINESS NO HANDOFF CANÔNICO DE DESIGN / AUTORIZAÇÃO PROCEDIMENTAL DE DESIGN**

Somente depois dessa autorização devem começar arquitetura visual, wireframe, UI ou protótipo do Guivos Business.

## 32. Síntese

> **O Source Lock congela o que a Home Guivos Business precisa significar. A forma poderá ser explorada depois; o significado não pode ser reinventado pela forma.**