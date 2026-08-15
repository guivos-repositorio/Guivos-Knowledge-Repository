---
id: GKR-BUSINESS-CONTINUITY-001
title: Guivos Business — Checkpoint de Continuidade e Decisões Validadas
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-15
depends_on:
  - GPA-004
  - GKR-STATE-001
related:
  - PAS-001
  - GPA-006
  - GPA-007
  - ROADMAP-12.79.0
normative: false
---

# Guivos Business — Checkpoint de Continuidade e Decisões Validadas

## 1. Finalidade

Este documento existe para **preservar com precisão o ponto de continuidade do trabalho do Guivos Business**, evitando que decisões já validadas em conversas fiquem dependentes da memória de um chat específico.

Ele é um **checkpoint de recuperação**, não uma autoridade paralela de produto. Em caso de conflito, prevalecem `GPA-004 — Guivos Business`, `GKR-STATE-001` e as autoridades temáticas específicas mais recentes.

Seu papel é registrar quatro coisas que precisam permanecer recuperáveis em qualquer nova conversa:

1. o que foi validado;
2. o que foi explicitamente descartado ou superado;
3. o que permanece em aberto;
4. qual é o próximo ponto exato de continuidade.

## 2. Checkpoint do repositório que encerrou a reconciliação anterior

A PR **#271 — `GKR: reconciliar Guivos Business e decisões validadas em chat`** foi integrada em 2026-08-15.

Estado resultante:

```text
main
= 38122cc7b091e38b2152be357a3849a75734c2a7

PR #271
= MERGED

head final da PR
= a6cc72cecd53b7c6757d49b8bf16a84ce83d97c0

GKR Semantic State Validation #388
= SUCCESS

GKR Mechanical Validation #733
= SUCCESS
```

A PR #271 consolidou `GPA-004` v1.5.0, `GKR-STATE-001` v2.37.0 e `ROADMAP-12.79.0`, sem iniciar a Home Pública do Guivos Business e sem alterar os snapshots congelados de Design v1/v2.

## 3. Separações canônicas que não devem ser reabertas sem nova decisão explícita

```text
Organização ≠ Guivos Business
Empresa no contrato Business ≠ novo tipo estrutural de participante
Guivos Business ≠ Guivos Ads
Guivos Intelligence ≠ módulo do Guivos Business
Guivos Journey ≠ módulo controlado pela empresa
custeio empresarial do Journey ≠ propriedade da Journey
Programa de Pontos ≠ identidade integral do Business
Pontos Guivos ≠ medida de evolução
Pontos Guivos ≠ pagamento do plano Journey
VALOR DE IMPACTO LIBERADO ≠ Pontos Guivos
VALOR DE IMPACTO LIBERADO ≠ impacto realizado
VALOR DE IMPACTO LIBERADO ≠ impacto comprovado
```

No raciocínio comercial específico do Business, a arquitetura começa pela **EMPRESA**. `Organização` continua sendo o tipo estrutural de participante na ontologia geral do ecossistema.

## 4. Pergunta fundadora do Guivos Business

A direção humana validada para o produto é:

> **Como podemos ajudar os seres humanos a terem uma vida melhor?**

A empresa pode criar condições, acesso, incentivos, benefícios e possibilidades. Ela não define quem a pessoa deve se tornar e não adquire autoridade sobre a evolução individual.

A formulação arquitetural segura é:

```text
EMPRESA
→ amplia condições e possibilidades

PESSOA
→ escolhe, participa e decide dentro de sua autonomia

GUIVOS
→ conecta capacidades e experiências coerentes com seu propósito
```

## 5. Portfólio funcional v1 validado

A arquitetura não deve proliferar famílias apenas para aumentar o catálogo. O portfólio funcional validado possui **duas ofertas principais**.

### 5.1 Oferta 1 — Programas de Incentivo

A empresa contrata a capacidade de estruturar programas em que objetivos legítimos são convertidos em regras, eventos verificáveis e benefícios.

O mesmo núcleo atende dois recortes comerciais principais:

```text
PROGRAMAS DE INCENTIVO
├── Funcionários
│   └── engajamento, reconhecimento, assiduidade,
│       comprometimento observável, desempenho, treinamento,
│       segurança, inovação, sustentabilidade, impacto etc.
│
└── Clientes
    └── fidelização, recorrência, aquisição, indicação,
        ativação, campanhas e relacionamento
```

Esses recortes **não exigem dois motores de produto diferentes**. São lentes comerciais diferentes sobre o mesmo núcleo funcional.

Objetos conceituais do núcleo:

```text
Programa
→ Campanha
→ Participante
→ Evento
→ Regra
→ Resultado
→ Orçamento/financiamento
→ Intelligence
```

Uma regra interpreta um evento legitimamente recebido ou produzido:

```text
EVENTO
+
CONDIÇÕES
→ RESULTADO
```

Resultados possíveis incluem:

- Pontos Guivos;
- benefício direto elegível;
- `VALOR DE IMPACTO LIBERADO` quando houver finalidade social legítima.

A Guivos executa a regra; a empresa define o critério empresarial legítimo. Conceitos subjetivos como “comprometimento” devem ser traduzidos pela empresa em eventos/condições observáveis e verificáveis antes de serem executados pela plataforma.

### 5.2 Oferta 2 — Guivos Journey custeado pela EMPRESA

Não existe novo produto chamado `Journey para Empresas`, `Journey Business`, `Journey Corporativo` ou `Journey Patrocinado`.

> **Continua sendo Guivos Journey. O que muda é quem paga o acesso.**

Fluxo:

```text
EMPRESA
→ contrata/custeia acessos elegíveis
→ PESSOA utiliza o Guivos Journey normal
→ PESSOA escolhe livremente suas jornadas
→ Guivos Intelligence pode produzir leitura agregada autorizada
```

Regras validadas:

- a empresa **não restringe temas de evolução**;
- o Journey financiado pela empresa deve preservar a experiência normal e os planos/regras existentes do produto;
- a empresa não cria “jornadas internas” próprias para transformar Journey em LMS, curso, trilha obrigatória ou lista de tarefas corporativas;
- o perfil pode identificar de forma discreta que o acesso é custeado por uma empresa;
- o custeio pode terminar, mas a identidade e o histórico pessoal pertencem à relação da pessoa com a Guivos, sujeitos às regras futuras de acesso do produto;
- a empresa não recebe conteúdo individual de Journey por financiar o acesso.

## 6. Caminho explicitamente descartado — Journey corporativa criada pela empresa

Foi explorada e rejeitada a ideia de permitir à empresa criar jornadas próprias de evolução interna, desafios bonificados, cursos ou tarefas corporativas dentro do Journey.

Motivo da rejeição:

- aproxima o produto de LMS/LXP/universidade corporativa;
- transforma evolução em tarefa bonificada;
- desloca a essência da Guivos para cumprimento corporativo;
- cria duplicação com soluções já existentes no mercado;
- enfraquece a autonomia da pessoa.

Portanto:

```text
EMPRESA PAGA O JOURNEY
≠
EMPRESA CRIA O JOURNEY
```

## 7. Programa de Pontos — arquitetura validada

### 7.1 Um saldo para a pessoa, origens rastreáveis internamente

A experiência desejada é de **um saldo único de Pontos Guivos por pessoa**.

Internamente, a Guivos preserva origem/lotes para auditoria, validade, reversão, liquidação e reconciliação.

```text
Programa Empresa X → +500
Programa Empresa Y → +300

SALDO DA PESSOA → 800 Pontos Guivos
```

A origem não fragmenta a experiência em múltiplas carteiras corporativas visíveis.

### 7.2 Orçamento empresarial pré-pago

A empresa carrega previamente orçamento para financiar o programa.

Na visão empresarial, a leitura validada é:

```text
CARREGADO
CONCEDIDO
DISPONÍVEL
```

`Concedido` significa que o valor já foi consumido/alocado pelo programa empresarial no momento em que os pontos foram entregues à pessoa.

Para a empresa:

```text
PONTO CONCEDIDO
=
ORÇAMENTO EMPRESARIAL JÁ UTILIZADO/ALOCADO
```

A empresa **não precisa enxergar** a estrutura interna de lastro da Guivos em estados como “comprometido”, “em circulação” ou “liquidado”. Esses estados podem existir internamente, mas não são a linguagem administrativa da empresa.

### 7.3 O que a empresa vê depois da concessão

Foi descartada a ideia de mostrar à empresa uma decomposição como:

```text
pontos disponíveis aos participantes
pontos não utilizados
pontos expirados
```

A informação considerada pertinente para a empresa é **onde os pontos efetivamente utilizados foram consumidos dentro do ecossistema**.

Exemplo:

```text
Mall ...... 10%
Travel .... 70%
Journey ... 20%
           ----
           100%
```

Regras da métrica:

- o denominador contém somente pontos efetivamente utilizados;
- não entram pontos ainda guardados pela pessoa;
- não entram pontos expirados;
- a distribuição fecha 100% entre as áreas exibidas;
- a empresa não recebe histórico individual de consumo.

### 7.4 Utilização no ecossistema

Pontos podem ser utilizados em possibilidades pagas elegíveis de:

- Guivos Mall;
- Guivos Travel;
- possibilidades pagas apresentadas normalmente pelo Guivos Journey.

No Journey, a regra é especialmente importante:

```text
INTENÇÃO
→ CONTEXTO
→ PERTINÊNCIA
→ POSSIBILIDADE
→ somente depois: FORMA DE PAGAMENTO
```

Pontos **não alteram descoberta, relevância, prioridade, recomendação ou Next Step**.

A pessoa com pontos e a pessoa sem pontos seguem o mesmo Journey. A diferença é apenas a forma de acesso a uma possibilidade paga elegível.

### 7.5 Pontos não pagam o plano Journey

Para utilizar pontos em uma possibilidade apresentada pelo Journey, a pessoa precisa ser participante do Journey segundo a estrutura normal de planos.

```text
PLANO JOURNEY
→ pago normalmente quando for um plano pago

POSSIBILIDADE PAGA ELEGÍVEL
→ pode aceitar dinheiro, pontos ou forma mista
```

Não existe compra do plano Journey com Pontos Guivos nesta arquitetura.

### 7.6 Organizações e Coletivos não precisam “aceitar pontos”

Quando uma Organização ou Coletivo oferece uma possibilidade paga elegível dentro do ecossistema, **não é necessário que opere uma carteira própria de pontos ou escolha manualmente aceitar pontos como moeda**.

A arquitetura validada é de intermediação pela Guivos:

```text
PESSOA
→ paga na plataforma Guivos
   com dinheiro, pontos ou forma mista elegível
→ GUIVOS processa a transação
→ GUIVOS realiza repasse financeiro
→ ORGANIZAÇÃO / COLETIVO / FORNECEDOR
```

O participante econômico recebe valor financeiro conforme a relação comercial aplicável. A origem dos Pontos Guivos utilizados pela pessoa não precisa ser conhecida pelo fornecedor.

A elegibilidade econômica do meio de pagamento é governada pela Guivos e pelo contrato da possibilidade, não por um “botão aceitar pontos” da Organização/Coletivo.

### 7.7 Pagamento misto

A direção de produto validada considera **Pontos + dinheiro** uma opção interessante e desejável para possibilidades elegíveis.

```text
PREÇO
=
PONTOS
+
DINHEIRO COMPLEMENTAR
```

A mecânica detalhada de checkout, estorno, liquidação e tributação permanece fora deste checkpoint.

### 7.8 Equivalência econômica

A relação `X pontos = Y reais` **já possui regra validada/funcionando no ecossistema** e não deve ser rediscutida nesta frente.

O checkpoint apenas preserva essa decisão e impede que futuras retomadas tratem a equivalência como problema ainda não resolvido.

## 8. Expiração e saldos — direção validada, parâmetros ainda não congelados

A direção aceita é que Pontos Guivos possam possuir validade para a pessoa. O exemplo discutido foi **24 meses**, mas o prazo exato não está congelado por este checkpoint.

Quando pontos da pessoa expirarem, a direção conceitual discutida é que o valor correspondente **não retorne automaticamente à empresa de origem**, podendo ser destinado à sustentação do ecossistema e/ou a causas apoiadas pela Guivos, sujeito a futura regra econômica específica.

Separadamente, orçamento empresarial pré-pago **nunca concedido** pode admitir estorno à empresa conforme contrato, inclusive com taxas administrativas quando aplicáveis.

Portanto:

```text
SALDO EMPRESARIAL NÃO CONCEDIDO
→ pode permanecer empresarial / ser transferido / ser estornado conforme contrato

PONTOS JÁ CONCEDIDOS À PESSOA
→ não retornam automaticamente à empresa de origem
```

Os percentuais, prazo de validade, destinação econômica e regras de estorno ainda exigem autoridade própria antes de implementação.

## 9. VALOR DE IMPACTO LIBERADO

Impacto **não é uma terceira família independente do Guivos Business**.

`VALOR DE IMPACTO LIBERADO` é uma possível mecânica/saída dentro de Programas de Incentivo quando houver finalidade social legítima.

Exemplo conceitual:

```text
AÇÃO ELEGÍVEL
→ VALOR DE IMPACTO LIBERADO
→ PARTICIPANTE ESCOLHE ENTRE CAUSAS ELEGÍVEIS
→ EMPRESA FINANCIA A DESTINAÇÃO
```

O valor:

- não entra no saldo pessoal de Pontos Guivos;
- não pode ser utilizado no Mall ou Travel;
- não é dinheiro livre da pessoa;
- não prova que o impacto foi efetivamente realizado.

A escolha entre causas elegíveis é mais coerente com a proposta do que uma destinação completamente pré-definida pela empresa quando o objetivo for participação real da pessoa.

## 10. Guivos Intelligence no Business — escopo validado

O Intelligence Business deve utilizar **dados, interações e eventos gerados ou legitimamente conhecidos dentro do ecossistema Guivos**.

Não deve depender de a Guivos ingerir bases internas de RH, folha, vendas, produtividade, absenteísmo, CRM ou ERP para funcionar.

Separação validada:

```text
GUIVOS
→ mede o que acontece na Guivos
→ organiza indicadores e padrões
→ oferece Intelligence

EMPRESA
→ possui seus KPIs internos
→ pode combinar os indicadores Guivos com seus próprios dados
→ realiza sua análise e toma decisões
```

Integrações podem enviar **eventos mínimos necessários** para acionar regras, por exemplo:

```text
RH → regra de assiduidade cumprida
CRM → indicação convertida
ERP → evento elegível confirmado
LMS externo → treinamento concluído
```

Isso **não significa** importar toda a base interna para o Intelligence.

### 10.1 Exemplo corrigido — assiduidade

Guivos pode mostrar:

- quantidade de pessoas que receberam incentivo pela regra de assiduidade;
- quantidade de concessões;
- Pontos Guivos concedidos;
- recorrência e participação no programa;
- evolução desses eventos dentro da Guivos.

Guivos não deve declarar, apenas com esses dados:

> “A assiduidade da empresa aumentou X%.”

Esse KPI pertence à operação interna da empresa.

Uma saída inteligente legítima pode ser:

> A quantidade de concessões relacionadas à assiduidade aumentou no período. Esse movimento também aparece nos seus indicadores internos de assiduidade?

### 10.2 Comparações mensais como diferenciação de plano superior

Foi validada a direção de que planos superiores possam receber **comparações recorrentes com o período anterior**, produzidas pelo Guivos Intelligence a partir de dados Guivos.

Exemplo:

```text
MÊS ATUAL
versus
MÊS ANTERIOR
→ variações
→ movimentos relevantes
→ síntese Intelligence
```

Essa capacidade pode funcionar como diferencial comercial de um plano mais alto, mas o plano exato e o entitlement ainda não estão congelados.

### 10.3 Exportação/API para BI da empresa como diferenciação superior

Também foi validada a direção de permitir, em planos mais altos, que a empresa leve indicadores Guivos para sua própria arquitetura analítica.

```text
GUIVOS INTELLIGENCE
→ exportação estruturada / API
→ Power BI / Tableau / Looker / Data Lake da empresa
→ empresa combina com seus próprios KPIs
```

A Guivos fornece a inteligência do seu ecossistema; a empresa faz os cruzamentos com a inteligência do próprio negócio em seu ambiente.

## 11. Intelligence relacionado ao Journey custeado pela empresa

Quando a empresa também custeia Guivos Journey para uma população elegível, o Intelligence pode produzir leitura **agregada e protegida** de sinais originados das escolhas das pessoas.

Exemplos de leitura possível:

- interesses de evolução agregados;
- tendências temporais;
- temas emergentes;
- movimentos de interesse;
- aderência entre interesses agregados e benefícios/iniciativas cadastrados pela empresa;
- lacunas de cobertura;
- sinais de subutilização quando a utilização também for conhecida pela Guivos.

Regras semânticas obrigatórias:

```text
interesse ≠ condição
intenção ≠ diagnóstico
tema ≠ problema
escolha ≠ causa
```

Não existe `score de evolução individual` para a empresa.

A empresa não recebe a Journey individual, o tema pessoal específico, a intenção da pessoa ou a explicação de por que determinada possibilidade apareceu.

Toda métrica agregada deve declarar sua base/denominador corretamente, por exemplo:

> 31% dos participantes ativos com jornadas elegíveis analisadas no período.

Não usar “31% dos funcionários” quando essa não for a base real.

## 12. Benefícios e iniciativas já oferecidos pela empresa

Uma direção validada para o Intelligence é permitir que a empresa informe benefícios/iniciativas que já oferece, por exemplo:

- plano de saúde;
- educação financeira;
- bolsa de estudos;
- curso de idiomas;
- voluntariado;
- programa de inovação;
- outros benefícios corporativos.

O objetivo não é transformar Guivos em ERP de benefícios, mas permitir uma leitura agregada do tipo:

```text
O QUE AS PESSOAS BUSCAM
↕
O QUE A EMPRESA JÁ OFERECE
```

Daí podem surgir leituras como:

- aderência;
- lacuna;
- subutilização;
- baixa aderência observada.

O Intelligence pode apresentar fato, contexto, interpretação e uma pergunta relevante sem precisar terminar sempre em uma recomendação automática.

## 13. Arquitetura dos planos — direção comercial validada

Os nomes vigentes permanecem:

```text
Start
Growth
Scale
Enterprise
```

O plano **não define qual oferta a empresa pode contratar**. Uma empresa pode contratar:

- apenas Programas de Incentivo;
- apenas acessos Guivos Journey;
- ambas as ofertas.

A função do plano é governar nível de capacidade, escala, Intelligence, integração, governança e serviço.

Separação conceitual:

```text
OFERTA
= o que a empresa utiliza

PLANO BUSINESS
= até onde vão capacidade, Intelligence,
  governança, integração e serviço
```

A arquitetura econômica discutida separa:

```text
1. assinatura do plano Business
2. produtos/ofertas contratados
3. escala / participantes / acessos
4. orçamento pré-pago de incentivos
5. serviços adicionais quando aplicáveis
```

O orçamento pré-pago de incentivo não deve ser confundido com a assinatura do plano.

### 13.1 Progressão funcional de referência

A direção de valor discutida foi:

```text
START
→ operar

GROWTH
→ acompanhar e compreender melhor

SCALE
→ interpretar, segmentar e integrar

ENTERPRISE
→ governar em alta complexidade/escala
```

Detalhes como limites, preços, quantidade de usuários, SSO, API, SLA, multiunidade e atendimento dedicado ainda precisam ser formalizados antes de virar entitlement contratual.

### 13.2 Serviço

Foi discutida e aceita como direção a separação entre capacidade tecnológica e nível de serviço:

```text
PLANO
= capacidade tecnológica/comercial

SERVIÇO
= quanto a Guivos participa da implantação/operação
```

Possíveis níveis trabalhados:

- Self-service;
- Assisted;
- Managed.

Os nomes e escopos ainda não estão congelados como oferta comercial final.

## 14. Economia e monetização — fronteiras validadas

Receitas diretas do Business podem incluir, conforme futura modelagem:

- assinatura do plano;
- escala/participantes;
- acessos Journey contratados;
- Intelligence avançado;
- exportações/API/integrações;
- serviços Assisted/Managed;
- taxas operacionais transparentes quando aplicáveis.

Separadamente, a circulação criada pelo ecossistema pode gerar receita em:

- Mall;
- Travel;
- possibilidades pagas transacionadas via Journey;
- outras relações comerciais do ecossistema.

A empresa que entra pelo Business também pode, de forma completamente independente, tornar-se cliente do Guivos Ads.

### 14.1 Ads permanece totalmente distinto

A existência de oportunidade econômica cruzada **não transforma Ads em módulo Business**.

```text
BUSINESS
→ relação B2B de capacidades, programas, benefícios e Intelligence

ADS
→ publicidade, patrocínio, impulsionamento e exposição comercial paga
```

Uma mesma empresa pode contratar ambos, mas são contratos e produtos independentes.

Receita de Ads deve ser atribuída a Ads, não ao P&L do Business apenas porque a empresa também é cliente Business.

### 14.2 Business precisa ser sustentável por si

Mall, Travel, Journey e Ads podem ampliar o valor econômico de uma conta Business, mas isso é **upside do ecossistema**.

A modelagem não deve depender de receita de outros produtos para esconder um Business estruturalmente deficitário.

## 15. Caminhos descartados ou superados

Não retomar automaticamente os seguintes caminhos:

1. **Dois tipos de pontos/créditos visíveis para a pessoa** — rejeitado por burocratizar a experiência.
2. **Transformar evolução em caça a pontos** — rejeitado por conflitar com o propósito da Guivos.
3. **Journey temática limitada pela empresa** — rejeitada porque distorce as escolhas da pessoa e enviesaria o Intelligence.
4. **Journey criada pela empresa / curso corporativo bonificado** — rejeitada por aproximar a Guivos de LMS/LXP e retirar autonomia.
5. **Impacto como terceira família independente do Business** — rejeitado; impacto permanece mecânica possível dentro de Programas de Incentivo.
6. **Catálogo separado de possibilidades de Organizações/Coletivos para pontos** — rejeitado; Journey governa a descoberta e pontos atuam somente como forma de acesso/pagamento.
7. **Empresa acompanhando individualmente onde cada pessoa gastou pontos** — rejeitado; somente leitura agregada compatível com finalidade e privacidade.
8. **Dashboard empresarial mostrando pontos não utilizados/expirados como informação principal** — rejeitado; a métrica validada de destino considera somente pontos efetivamente usados.
9. **Guivos importando toda a base interna da empresa para provar antes/depois de KPIs corporativos** — rejeitado como arquitetura padrão por prejudicar escala e criar dependência de dados empresariais heterogêneos.
10. **Ads como módulo do Business** — explicitamente rejeitado. Ads é produto distinto.

## 16. Itens ainda não congelados

Os seguintes temas permanecem abertos ou precisam de autoridade específica antes de implementação:

- preços de Start, Growth, Scale e Enterprise;
- limites quantitativos e entitlements finais dos planos;
- preço/faixa de escala por participante;
- preço dos acessos Journey custeados pela empresa;
- definição final de Self-service / Assisted / Managed;
- regra detalhada de validade dos pontos e prazo exato;
- destino econômico e percentuais relativos a pontos expirados;
- política detalhada de estorno/reversão/fraude;
- regra detalhada de consumo de múltiplos lotes de pontos;
- outras origens autorizadas de Pontos Guivos além de Programas Business;
- internacionalização e multi-moeda dos pontos;
- detalhes operacionais de pagamento misto;
- comissão, taxa ou margem específica da Guivos em cada transação;
- regras fiscais, contábeis, jurídicas e de liquidação;
- arquitetura técnica de API/exportação Business;
- thresholds mínimos de agregação/coorte do Intelligence;
- composição exata do resumo mensal Intelligence por plano;
- Home Pública do Guivos Business.

A equivalência econômica `X pontos = Y reais` **não está nesta lista** porque já existe regra validada e não deve ser reaberta nesta frente.

## 17. Estado da Home Pública do Guivos Business

A Home Pública do Guivos Business **ainda não foi iniciada**.

Não existem ainda, como autoridade convergida específica do Business:

- Documento Mestre da Home;
- Source Lock;
- arquitetura narrativa aprovada;
- wireframe;
- protótipo;
- handoff para Design.

A Home não deve ser derivada visualmente da Home de Organizações e Coletivos e não deve tratar Ads como parte do Business.

## 18. Próximo ponto exato de continuidade

Após a integração da PR #271 e deste checkpoint de continuidade, a arquitetura de produto do Business possui base suficiente para uma retomada assertiva.

O próximo ato **não é automático**. Se houver autorização para avançar a Home Pública do Guivos Business, a sequência correta é:

```text
TESE
→ PROTAGONISTA
→ PROBLEMA
→ PROMESSA
→ ARQUITETURA NARRATIVA
→ CONTRATOS DE AUTORIDADE
→ CONVERSÃO
→ DOCUMENTO MESTRE
→ SOURCE LOCK
→ somente depois: Design
```

Se a decisão for aprofundar produto/economia antes da Home, o ponto de retomada é **planos, unit economics e regras econômicas ainda abertas**, sem reabrir as decisões já listadas como validadas neste checkpoint.

## 19. Instrução de retomada para novas conversas

Ao retomar Guivos Business em uma nova conversa:

1. ler `GPA-004`;
2. ler este checkpoint `GKR-BUSINESS-CONTINUITY-001`;
3. confirmar o `main` atual e qualquer PR aberta;
4. não inferir que temas listados em `Itens ainda não congelados` já foram decididos;
5. não reabrir decisões validadas sem nova solicitação explícita;
6. preservar **Business ≠ Ads** em toda arquitetura, narrativa e monetização;
7. preservar que Journey continua sendo Journey e que a empresa apenas pode custear acesso, não possuir a jornada pessoal.