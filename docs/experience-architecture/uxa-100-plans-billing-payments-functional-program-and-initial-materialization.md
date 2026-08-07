---
id: UXA-100
title: Programa Funcional e Materialização Inicial de Planos, Cobrança e Pagamentos
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-UPGRADE-DOWNGRADE-CANCELLATION-POLICY-001
  - GEM-COMMERCIAL-BASELINE-001
  - GEM-003-PAYER-BENEFICIARY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - UXA-011-A1
  - UXA-070
  - GKR-STATE-001
normative: false
---

# Programa Funcional e Materialização Inicial de Planos, Cobrança e Pagamentos

## 1. Finalidade

A UXA-100 abre uma frente transversal para tornar compreensíveis, em baixa fidelidade, os fluxos de **plano, cobrança, pagamento, comparação de benefícios e efeito de limites comerciais** para os três participantes estruturais da Guivos:

- Pessoa;
- Coletivo;
- Organização.

A frente deriva da baseline comercial candidata do GEM-004. Ela **não autoriza oferta pública, checkout real, cobrança, gateway, implantação, desenvolvimento ou publicação de preços como proposta comercial vigente**.

A materialização inicial utiliza placas de fluxo e placas complementares de comparação incremental para validar continuidade e hierarquia antes de fracionar estados em superfícies finais ou registrá-los como IDs canônicos.

## 2. Pergunta funcional

A experiência deverá responder, sem coerção:

> **Qual plano está ativo, o que ele inclui, qual limite foi alcançado, quais alternativas gratuitas permanecem válidas, o que muda ao escolher outro plano, quais benefícios o plano superior acrescenta em relação ao imediatamente anterior, quem paga e quem recebe o benefício, qual é a recorrência e o que acontece em sucesso, falha, downgrade ou cancelamento?**

Para a Pessoa existe uma pergunta adicional obrigatória:

> **Como limitar correspondências personalizadas do Guivos Free sem esconder oportunidades públicas nem transformar pagamento em condição para descobrir oportunidades?**

## 3. Autoridades e limites preservados

### 3.1 Baseline comercial candidata

A UXA-100 materializa somente referências já documentadas em GEM-004-A1 e GEM-004-A2.

Os valores exibidos nos wireframes são **preços candidatos para simulação documental**.

### 3.2 Oportunidade pública não é ofuscada

O estado visual limitado do Guivos Free recai sobre uma **correspondência personalizada adicional após a cota semanal**, não sobre a existência da oportunidade pública.

A experiência deverá preservar:

- catálogo público no Explorar;
- Mapa;
- informações públicas essenciais;
- segurança, preço da oportunidade, prazo e responsabilidade quando a oferta já estiver acessível publicamente.

É proibido desfocar uma oportunidade pública apenas para ocultar sua existência e pressionar upgrade.

### 3.3 Pagamento não altera relevância

Plano pago não poderá:

- elevar posição orgânica;
- alterar relevância funcional;
- aumentar veracidade ou confiança institucional;
- representar evolução humana superior;
- ocultar alternativa gratuita legítima.

### 3.4 Assinatura é distinta de transação

A superfície deverá distinguir:

```text
assinatura da plataforma
≠ preço de atividade ou oportunidade
≠ comissão
≠ taxa do meio de pagamento
≠ tributo
```

### 3.5 Parâmetros não definidos

A UXA-100 não inventa:

- gateway ou adquirente;
- bandeira, PIX, boleto ou carteira como método oficial;
- tokenização;
- prazo de tolerância após falha;
- pró-rata;
- crédito entre ciclos;
- data fiscal definitiva;
- política tributária;
- trial com conversão automática.

Nos wireframes, pagamento aparece apenas como **método autorizado em simulação**.

## 4. Decisão estrutural

Planos e cobrança não serão inseridos em `COM-*`, pois a família `COM-*` vigente representa Opportunity Boost/publicidade.

A UXA-100 também não cria ainda IDs canônicos de superfície ou transição.

Primeiro serão validados dois conjuntos complementares:

1. três placas de fluxo:
   - Pessoa — móvel;
   - Coletivo — computador;
   - Organização — computador;
2. três placas de comparação incremental:
   - Pessoa — Free → Plus → Pro;
   - Coletivo — Livre → Gestão → Impacto → Enterprise;
   - Organização — Start → Growth → Scale.

Somente uma validação funcional posterior poderá decidir:

- quantas superfícies canônicas devem existir;
- quais estados merecem SVG separado;
- quais IDs serão registrados;
- quais transições serão integradas ao registro global.

## 5. Espinha dorsal transversal

```text
Plano e cobrança
→ plano atual + uso + limites
→ comparação voluntária
→ mostrar plano atual
→ mostrar benefício herdado
→ mostrar somente o delta adicional do plano superior
→ seleção afirmativa, sem pré-seleção
→ revisão da contratação
→ pagador + beneficiário
→ preço + periodicidade + recorrência
→ método autorizado em simulação
→ confirmar
→ processamento
├── sucesso → ativação rastreável + confirmação
└── falha → nenhuma ativação presumida + recuperação

plano ativo
→ downgrade ou cancelamento
→ revisar consequência e data aplicável
→ mostrar exatamente quais capacidades deixam de estar disponíveis
→ confirmar
→ registrar estado futuro
```

### 5.1 Regra de comparação incremental

A comparação terá duas leituras complementares:

1. **matriz geral**, para entender todos os planos;
2. **delta incremental**, para responder o que o plano superior acrescenta ao plano imediatamente inferior.

A apresentação deverá utilizar a lógica:

```text
plano superior
= tudo o que permanece do plano anterior
+ capacidades adicionais exclusivas deste degrau
```

A comparação incremental não deverá repetir benefícios herdados como se fossem novos.

Quando o plano atual da Pessoa, Coletivo ou Organização for conhecido, a interface deverá também resumir o **delta direto entre o plano atual e o plano escolhido**, mesmo quando houver um ou mais degraus intermediários.

Exemplo: se uma Pessoa no Free selecionar Pro, a comparação direta `Free → Pro` deverá consolidar todos os incrementos aplicáveis de Plus e Pro, sem exigir que a Pessoa reconstrua mentalmente duas colunas intermediárias.

No downgrade, a mesma regra será invertida: a revisão deverá destacar **somente as capacidades que deixarão de estar disponíveis ou terão limite reduzido**, sem sugerir perda de direitos universais ou de dados protegidos.

Quando houver alternativa Enterprise/Scale:

```text
comparar plano
→ necessidade contratual
→ mostrar capacidades adicionais candidatas
→ solicitar proposta comercial
→ processo comercial governado
```

Não haverá checkout autônomo fictício para Enterprise/Scale.

## 6. Pessoa

### 6.1 Planos candidatos

| Plano | Mensal | Anual | Correspondências personalizadas completas |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | 2 por semana |
| Guivos Plus | R$ 24,90 | R$ 249,00 | sem cota semanal fixa, sujeito a uso justo |
| Guivos Pro | R$ 49,90 | R$ 499,00 | sem cota semanal fixa, com análise ampliada |

### 6.2 Comparação incremental da Pessoa

#### Plus em relação ao Free

O Guivos Plus herda os benefícios do Free e acrescenta:

- correspondências personalizadas completas sem cota semanal fixa, sujeitas a uso justo;
- explicação completa sobre a relação entre oportunidade e contexto autorizado;
- filtros avançados;
- alertas personalizados;
- histórico ampliado;
- planos salvos, lembretes e acompanhamento ampliado;
- exportação padrão;
- capacidade ampliada de processamento e inteligência;
- integrações limitadas quando autorizadas;
- suporte ampliado.

#### Pro em relação ao Plus

O Guivos Pro herda os benefícios do Plus e acrescenta:

- análises aprofundadas e comparativas;
- organização autorizada entre diferentes áreas da jornada;
- maior capacidade de processamento e inteligência;
- relatórios pessoais ampliados;
- exportações avançadas;
- integrações autorizadas ampliadas;
- suporte prioritário;
- acesso antecipado a capacidades aprovadas para teste, quando aplicável e informado.

Nenhum desses incrementos altera relevância orgânica, garante resultado ou transforma pagamento em condição para evolução.

### 6.3 Estado Free com cota esgotada

Após duas correspondências completas abertas na semana, uma correspondência adicional poderá manter visíveis:

- categoria;
- modalidade;
- localidade;
- prazo;
- natureza gratuita ou paga;
- indicação de que existe relação com contexto autorizado;
- período de renovação da cota.

Poderão permanecer limitados na correspondência personalizada:

- identidade completa da correspondência personalizada;
- justificativa detalhada;
- análise de aderência;
- relação ampliada com Momento Atual e Próximo Passo;
- comparação personalizada.

Devem permanecer acessíveis no mesmo estado:

- `Explorar oportunidades públicas`;
- `Ver no Mapa`;
- `Conhecer o Guivos Plus`.

### 6.4 Compra e mudança

A Pessoa deverá revisar antes da confirmação:

- plano escolhido;
- preço candidato;
- mensal ou anual;
- recorrência;
- pagador;
- beneficiário;
- início informado;
- método autorizado em simulação;
- benefícios adicionais em relação ao plano atual;
- downgrade e cancelamento;
- ausência de promessa de resultado.

## 7. Coletivo

### 7.1 Planos candidatos

| Plano | Mensal | Anual | Atividades/mês | Oportunidades/mês | Ativas | Publicação paga |
|---|---:|---:|---:|---:|---:|---|
| Livre | R$ 0,00 | R$ 0,00 | 1 gratuita | 1 gratuita | 2 | não |
| Gestão | R$ 89,90 | R$ 899,00 | 4 | 4 | 6 | sim |
| Impacto | R$ 249,90 | R$ 2.499,00 | 15 | 15 | 20 | sim |
| Enterprise | sob consulta | contrato anual | capacidade contratada | capacidade contratada | capacidade contratada | sim |

### 7.2 Comparação incremental do Coletivo

#### Gestão em relação ao Livre

O Coletivo Gestão preserva as capacidades do Livre e acrescenta ou amplia:

- até cinco administradores;
- quatro atividades por mês;
- quatro oportunidades por mês;
- até seis publicações simultaneamente ativas;
- atividades e oportunidades gratuitas ou pagas;
- inscrições, cobrança e gestão de vagas;
- cupons e condições comerciais básicas;
- categorias e indicadores ampliados;
- exportação básica;
- integrações limitadas;
- gestão ampliada de participantes;
- suporte prioritário.

#### Impacto em relação ao Gestão

O Coletivo Impacto preserva as capacidades do Gestão e acrescenta ou amplia:

- até quinze administradores;
- quinze atividades por mês;
- quinze oportunidades por mês;
- até vinte publicações simultaneamente ativas;
- ofertas patrocinadas ou financiadas;
- até cinco núcleos ou programas;
- categorias completas;
- indicadores históricos e de impacto;
- gestão de parceiros e patrocinadores;
- cupons e condições ampliados;
- exportação completa;
- integrações avançadas;
- dashboards ampliados;
- suporte especializado.

#### Enterprise em relação ao Impacto

O Coletivo Enterprise preserva as capacidades aplicáveis do Impacto e acrescenta capacidades dimensionadas por contrato:

- atividades, oportunidades e publicações sem limite padrão fixo, sujeitos à capacidade contratada;
- categorias completas e personalizáveis;
- múltiplos núcleos, unidades, territórios e programas;
- administradores e papéis conforme contrato;
- API, SSO e integrações dedicadas;
- integração com Power BI;
- dashboards e indicadores personalizados;
- importação e exportação em massa;
- domínio ou ambiente configurável, quando tecnicamente aprovado;
- treinamento e implantação assistida;
- gerente dedicado;
- SLA;
- governança e suporte contratados.

### 7.3 Limite no Coletivo Livre

Ao atingir cota ou tentar publicação paga, a superfície deverá preservar:

- publicações existentes e sua visibilidade;
- rascunho;
- opção de aguardar o próximo ciclo;
- encerramento/agendamento quando aplicável;
- alternativa de manter a nova publicação gratuita quando funcionalmente possível;
- comparação voluntária com Gestão/Impacto.

O upgrade não poderá ser apresentado como aumento de relevância orgânica.

### 7.4 Enterprise

Enterprise utiliza solicitação de proposta comercial e dimensionamento; não recebe checkout autônomo fictício.

## 8. Organização

### 8.1 Planos candidatos

| Plano | Mensal | Anual | Novas oportunidades/programas | Ativas | Administradores | Unidades |
|---|---:|---:|---:|---:|---:|---:|
| Business Start | R$ 299,00 | R$ 2.990,00 | 10/mês | 15 | 3 | 1 |
| Business Growth | R$ 799,00 | R$ 7.990,00 | 50/mês | 75 | 10 | até 5 |
| Business Scale | a partir de R$ 1.990,00 | contrato anual | capacidade contratada | capacidade contratada | conforme contrato | múltiplas |

### 8.2 Comparação incremental da Organização

#### Business Growth em relação ao Business Start

Business Growth preserva as capacidades do Start e acrescenta ou amplia:

- até dez administradores;
- até cinco unidades;
- até cinquenta novas oportunidades ou programas por mês;
- até setenta e cinco publicações simultaneamente ativas;
- até dez Coletivos relacionados administráveis;
- analytics avançados e agregados;
- automações;
- exportação completa;
- integrações limitadas;
- exportação compatível com Power BI;
- gestão ampliada de elegibilidade;
- suporte prioritário.

#### Business Scale em relação ao Business Growth

Business Scale preserva as capacidades aplicáveis do Growth e acrescenta capacidades dimensionadas por contrato:

- capacidade de publicações dimensionada;
- múltiplas unidades;
- administradores e Coletivos relacionados conforme contrato;
- governança avançada;
- SSO;
- API;
- integração dedicada com Power BI;
- dashboards personalizados;
- exportações automatizadas;
- implantação assistida;
- atendimento dedicado;
- SLA;
- condições comerciais e faturamento personalizados.

### 8.3 Limite e alternativas

Quando a Organização atingir capacidade, deverão estar visíveis:

- limite e consumo atual;
- período de renovação;
- efeito exato do upgrade;
- arquivar, agendar ou manter rascunho quando aplicável;
- separação entre capacidade comercial e relevância das oportunidades.

### 8.4 Business Scale

Scale utiliza processo comercial solicitado pela Organização, com proposta e capacidade contratada. Não há checkout autônomo simulado como se preço e escopo fossem autoatendimento definitivo.

## 9. Pagador e beneficiário

Toda revisão de contratação deverá distinguir explicitamente:

- quem paga;
- quem recebe o benefício do plano;
- quem poderá cancelar;
- qual escopo de dados é necessário à cobrança.

Pagamento por terceiro não transfere automaticamente:

- autoridade sobre a Pessoa;
- autoridade sobre Coletivo;
- acesso à jornada pessoal;
- acesso a dados sensíveis;
- poder de alterar relevância, recomendação ou resultado.

## 10. Falha de pagamento

A simulação de falha deverá informar:

- pagamento não confirmado;
- ativação não presumida;
- plano/estado anterior identificável;
- acesso gratuito e direitos essenciais preservados;
- caminho para tentar novamente ou revisar método autorizado;
- ausência de duplicação de cobrança por simples reenvio da mesma intenção.

A UXA-100 não define duração de `grace_period`.

## 11. Downgrade e cancelamento

A experiência deverá:

- ficar na mesma área de Plano e cobrança;
- mostrar estado atual e estado futuro;
- explicar capacidades que deixarão de estar disponíveis ou terão limite reduzido;
- usar a comparação incremental invertida para não ocultar consequências materiais;
- preservar dados, direitos e acesso gratuito conforme políticas aplicáveis;
- exigir confirmação afirmativa;
- emitir evidência/registro da solicitação.

A UXA-100 não presume pró-rata, estorno ou crédito entre ciclos.

## 12. Materialização inicial

### 12.1 Pessoa — móvel

![Placa de fluxo de planos e pagamentos da Pessoa](../assets/wireframes/uxa-100-person-plans-payments-flow-board.svg)

[Visualizar SVG do fluxo](../assets/wireframes/uxa-100-person-plans-payments-flow-board.svg)

![Comparação incremental dos planos da Pessoa](../assets/wireframes/uxa-100-person-plan-incremental-benefits-comparison.svg)

[Visualizar SVG da comparação incremental](../assets/wireframes/uxa-100-person-plan-incremental-benefits-comparison.svg)

O conjunto contém:

1. Plano e cobrança no Guivos Free;
2. correspondência personalizada adicional em prévia limitada;
3. comparação geral Free / Plus / Pro;
4. comparação incremental `Free → Plus` e `Plus → Pro`;
5. revisão de contratação;
6. pagamento confirmado;
7. pagamento não confirmado;
8. downgrade/cancelamento como continuidade prevista.

### 12.2 Coletivo — computador

![Placa de fluxo de planos e pagamentos do Coletivo](../assets/wireframes/uxa-100-collective-plans-payments-flow-board.svg)

[Visualizar SVG do fluxo](../assets/wireframes/uxa-100-collective-plans-payments-flow-board.svg)

![Comparação incremental dos planos do Coletivo](../assets/wireframes/uxa-100-collective-plan-incremental-benefits-comparison.svg)

[Visualizar SVG da comparação incremental](../assets/wireframes/uxa-100-collective-plan-incremental-benefits-comparison.svg)

O conjunto contém:

1. Plano e cobrança no Coletivo Livre;
2. limite/publicação paga não incluída;
3. comparação geral Livre / Gestão / Impacto / Enterprise;
4. comparação incremental `Livre → Gestão → Impacto → Enterprise`;
5. revisão de contratação Gestão;
6. pagamento confirmado ou não confirmado;
7. downgrade/cancelamento;
8. Enterprise via proposta comercial.

### 12.3 Organização — computador

![Placa de fluxo de planos e pagamentos da Organização](../assets/wireframes/uxa-100-organization-plans-payments-flow-board.svg)

[Visualizar SVG do fluxo](../assets/wireframes/uxa-100-organization-plans-payments-flow-board.svg)

![Comparação incremental dos planos da Organização](../assets/wireframes/uxa-100-organization-plan-incremental-benefits-comparison.svg)

[Visualizar SVG da comparação incremental](../assets/wireframes/uxa-100-organization-plan-incremental-benefits-comparison.svg)

O conjunto contém:

1. Plano e cobrança no Business Start;
2. capacidade e alternativas;
3. comparação geral Start / Growth / Scale;
4. comparação incremental `Start → Growth → Scale`;
5. revisão de contratação Growth;
6. pagamento confirmado ou não confirmado;
7. downgrade/cancelamento;
8. Scale por proposta comercial.

## 13. Critérios para futura validação funcional

A materialização somente poderá ser promovida quando uma validação posterior confirmar que:

1. alternativa gratuita permanece visível e funcional;
2. nenhuma oportunidade pública é ocultada para vender plano;
3. preview limitado do Free não se confunde com catálogo público;
4. plano atual, limite e consumo são compreensíveis;
5. nenhuma opção paga vem pré-selecionada;
6. preço, periodicidade e recorrência aparecem antes da confirmação;
7. pagador e beneficiário são distinguíveis;
8. sucesso não é presumido antes de confirmação;
9. falha não remove direitos essenciais;
10. cancelamento/downgrade são acessíveis;
11. Enterprise/Scale não fingem checkout autônomo;
12. assinatura não se confunde com taxa transacional;
13. pagamento não promete melhor relevância, confiança ou evolução;
14. parâmetros financeiros ainda indefinidos permanecem indefinidos;
15. cada plano superior explicita os benefícios/capacidades adicionais em relação ao plano imediatamente inferior;
16. benefícios herdados não são repetidos como se fossem incrementais;
17. quando há plano atual conhecido, o delta direto entre plano atual e plano escolhido é compreensível;
18. no downgrade, as capacidades perdidas ou reduzidas são apresentadas antes da confirmação.

## 14. Fora do escopo

A UXA-100 não:

- altera GEM-004;
- valida preços no mercado;
- registra superfícies ou transições canônicas;
- cria checkout real;
- integra gateway;
- cria cobrança;
- cria nota fiscal;
- define pró-rata, crédito ou grace period;
- implementa entitlement;
- publica oferta comercial;
- promove jornadas;
- inicia Engenharia de Produto.

## 15. Estado da frente

A UXA-100 é **programa e materialização inicial candidata**.

Os seis SVGs — três placas de fluxo e três comparações incrementais — permanecem **não validados funcionalmente** até uma frente posterior específica.

Sua existência documental não constitui integração à `main`, lançamento, implementação ou operação.