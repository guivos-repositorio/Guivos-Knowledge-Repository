---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.35.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
parent: UXA-000
related:
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - UXA-042
  - UXA-043
  - UXA-044
  - UXA-045
  - UXA-046
  - UXA-047
  - UXA-048
  - UXA-049
  - UXA-050
  - UXA-051
  - UXA-052
  - UXA-053
  - UXA-054
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência em wireframes de baixa fidelidade. O objetivo é validar organização, hierarquia, conteúdo, ações e continuidade antes de identidade visual ou implementação.

## 2. Regra de ordem

Os identificadores preservam a ordem histórica de criação. Eles não determinam a ordem das telas.

```text
Página Inicial pública
→ explicação do ambiente protegido
→ acesso, quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ processamento temporário visível e interrompível
→ compreensão inicial apresentada como hipótese
→ revisão por afirmação
→ decisões sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 3. Artefatos pela ordem funcional

1. Página Inicial e início da jornada — UXA-020;
2. validação da Home pública — UXA-021;
3. wireframe da Home para computador — UXA-022;
4. validação do início protegido — UXA-023;
5. wireframe móvel do início protegido — UXA-034;
6. validação do wireframe móvel do início protegido — UXA-035;
7. wireframe móvel da compreensão inicial — UXA-036;
8. validação da compreensão inicial — UXA-037;
9. wireframe da Tela Hoje — UXA-006;
10. wireframe móvel do Mapa — UXA-024;
11. validações e estados do Mapa — UXA-025 a UXA-033;
12. wireframe do Detalhe — UXA-007;
13. wireframe do Cadastro pela Organização — UXA-008;
14. contrato funcional reformulado do Opportunity Boost — UXA-038;
15. validação funcional especializada do Opportunity Boost — UXA-039;
16. wireframes do fluxo do anunciante para computador — UXA-040;
17. validação e reformulação dos wireframes do anunciante — UXA-041;
18. cartão patrocinado e explicação — UXA-042;
19. validação e reformulação do cartão e da explicação — UXA-043;
20. estados patrocinados para Lista e Mapa — UXA-044;
21. validação e reformulação dos estados patrocinados — UXA-045;
22. gestão da campanha ativa para computador — UXA-046;
23. validação e reformulação da gestão para computador — UXA-047;
24. relatório agregado — UXA-048;
25. validação e reformulação do relatório agregado — UXA-049;
26. validação transversal de 25 wireframes — UXA-050;
27. configuração móvel do anunciante — UXA-051;
28. validação e reformulação da configuração móvel — UXA-052;
29. gestão móvel da campanha ativa — UXA-053;
30. validação e reformulação da gestão móvel — UXA-054.

## 4. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo;
- representam prioridade e relação funcional, não acabamento;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não autorizam protótipo de alta fidelidade.

Wireframe gráfico não equivale a validação funcional. Validação funcional não equivale a teste de usabilidade, design ou desenvolvimento.

## 5. O que deverá ser validado

### 5.1 Primeira entrada e início protegido

- A pessoa entende que saiu da Home pública?
- Nenhum relato pessoal é solicitado antes da explicação?
- Dados de acesso e conteúdo da jornada são distinguíveis?
- Criar conta permanece separado de autorizar processamento?
- Explorar sem personalização permanece saída legítima?
- Texto, voz, arquivo e perguntas são alternativas equivalentes?
- A revisão antecede autorização específica?
- Autorizações começam desmarcadas?
- Recusar impede processamento?

### 5.2 Compreensão inicial

- Somente conteúdos autorizados entram no processamento?
- Interromper impede tarefa oculta?
- Afirmações confirmadas, inferidas e desconhecidas são separadas?
- A compreensão é percebida como hipótese, não diagnóstico?
- Nenhuma resposta começa selecionada?
- Corrigir interpretação preserva o relato original?
- Persistência e personalização são escolhas independentes?
- Base insuficiente evita hipótese artificial e pressão?

### 5.3 Mapa e superfícies recorrentes

- Mapa e Lista representam a mesma consulta?
- Quantidade, filtros e ordenação são compreensíveis?
- Relação comercial está separada da relevância?
- Dados ausentes são apresentados sem inferência?
- Cobertura, falha e indisponibilidade são distinguíveis?

### 5.4 Opportunity Boost — configuração para computador validada

A UXA-041 confirmou, após reformulação:

- gates atendido, limitado e bloqueado;
- objetivo único sem seleção automática;
- critérios escolhidos e revisáveis;
- critérios protegidos excluídos;
- público insuficiente sem ampliação silenciosa;
- orçamento, limite diário e duração sem promessa;
- base principal coerente e sem CPM/CPC simultâneos;
- estimativa distinguível de garantia;
- ausência de renovação automática;
- primeiro resultado orgânico anterior ao anúncio;
- confirmações desmarcadas;
- envio sem entrega;
- cancelamento com retorno ao rascunho e histórico preservado.

### 5.5 Opportunity Boost — configuração móvel validada

A UXA-052 confirmou, após reformulação:

- a mesma campanha, rascunho e versão nas cinco telas;
- progresso explícito e uma responsabilidade principal por etapa;
- condição limitada preservada no percurso;
- regras de exceção apresentadas como não ativas;
- objetivo escolhido por ação explícita;
- critérios revisáveis ou removíveis;
- estimativa provisória, datada e sujeita a recálculo;
- renovação automática como estado informativo desativado;
- controles da pessoa identificados como demonstração;
- cancelamento com revisão e confirmação separadas.

### 5.6 Opportunity Boost — cartão e explicação validados

A UXA-043 confirmou, após reformulação:

- natureza patrocinada anterior ao conteúdo;
- primeiro resultado orgânico antes do anúncio;
- anunciante, financiador e beneficiário compreensíveis;
- publicidade distinguível de recomendação;
- critérios objetivos utilizados e protegidos excluídos;
- ausência de lista de visualizadores;
- ocultação, redução, desativação e reversão com escopos próprios;
- denúncia separada de contestação de dados;
- ocultação sem redução do catálogo orgânico.

### 5.7 Opportunity Boost — Lista e Mapa patrocinados validados

A UXA-045 confirmou:

- uma consulta territorial compartilhada;
- contagens orgânicas e pagas separadas;
- primeiro resultado orgânico antes da unidade paga;
- inventário patrocinado fora da ordenação orgânica;
- filtros e preferência publicitária separados;
- marcadores patrocinados distinguíveis;
- seleção sem alteração da ordem da Lista;
- localização opcional;
- `Pesquisar nesta área` após decisão explícita;
- pouca oferta orgânica reduzindo publicidade.

### 5.8 Opportunity Boost — gestão para computador validada

A UXA-047 confirmou:

- campanha programada distinta de ativa;
- início condicionado à permanência dos gates;
- orçamento total, reservado, utilizado e saldo separados;
- indicadores operacionais com período e atualização;
- entrega reduzida distinta de pausa;
- limitação sem aceleração de orçamento ou prorrogação automática;
- pausa voluntária, automática e suspensão por política distintas;
- eventos anteriores preservados durante a pausa;
- retomada bloqueada até resolução e verificação;
- alteração material comparando versões;
- descarte sem retomada automática;
- cancelamento bloqueado até motivo e confirmações completas;
- estados finais e reconciliação separados;
- histórico preservado;
- saldo como candidato, não devolução confirmada.

### 5.9 Opportunity Boost — gestão móvel validada

A UXA-054 confirmou, após reformulação:

- seis telas preservando campanha, oportunidade, anunciante e versão;
- programação distinta de atividade;
- ausência de janela de medição distinta de zero;
- consequência explícita do gate atendido com limite;
- estado ativo normal sem limitação corrente;
- entrega reduzida com causa e verificação datadas;
- orçamento total, utilizado, saldo, limite e período compreensíveis;
- limitação sem aceleração ou prorrogação automática;
- pausa com causa e horário;
- novos eventos válidos interrompidos e registros técnicos tardios separados;
- retomada indisponível com causa explícita;
- comparação vertical de versões em tela pequena;
- versão aprovada em somente leitura e candidata não aprovada;
- nova avaliação e descarte sem retomada implícita;
- revisão de pausa distinta de execução;
- cancelamento exigindo motivo e confirmações independentes;
- estados finais, reconciliação e relatório separados.

### 5.10 Opportunity Boost — relatório agregado validado

A UXA-049 confirmou:

- entrega, interação, atribuição candidata e autorrelato em camadas distintas;
- proveniência e estado junto de cada camada;
- orçamento total, utilizado e saldo separados;
- `não disponível`, `não exibido por agregação` e zero separados;
- atribuição em agregados por tipo de evento;
- ausência de linha ou sequência individual;
- regra candidata versionada;
- origem patrocinada, orgânica e indeterminada preservadas;
- autorrelato não verificado e não somado;
- reconciliação por tipo e unidade;
- saldo sem promessa de crédito ou devolução;
- ausência de inferência de causalidade ou impacto humano.

### 5.11 Opportunity Boost — conjunto transversal

A UXA-050 confirma, para os 25 artefatos examinados naquele incremento:

- identidade da campanha;
- versão aprovada vinculada aos eventos;
- alteração material sem reescrita histórica;
- autoridade das transições;
- configuração e aprovação sem entrega automática;
- Lista e Mapa mantendo a mesma consulta;
- controles da pessoa sem identificação para o anunciante;
- orgânico e patrocinado separados até o relatório;
- orçamento, saldo e reconciliação sem promessa financeira;
- histórico e regra candidata preservados.

Os onze artefatos móveis criados pelas UXA-051 e UXA-053 não integram retrospectivamente essa validação transversal.

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou escolha consciente |
| preenchimento cinza | resumo, informação ou ação indisponível |
| texto sublinhado | ação secundária ou explicação |
| estado textual nomeado | posição funcional independente de cor |
| círculo vazio | escolha única ainda não realizada |
| caixa vazia | confirmação ainda não concedida |
| caixa preenchida | escolha realizada conscientemente |
| borda tracejada | limitação, regra de exceção ou aviso |
| selo textual anterior | natureza patrocinada antes do conteúdo |
| ação indisponível textual | condição ainda não atendida |
| comparação lado a lado | versões em tela ampla quando legível |
| comparação vertical | versões em tela móvel ou estreita |
| camada numerada | entrega, interação, atribuição candidata ou autorrelato |
| rótulo de proveniência | instrumentado, calculado, declarado ou indisponível |
| progresso móvel | posição no fluxo sem autorização automática |
| estado móvel de campanha | situação operacional, orçamento, motivo e ação |

Cor, iconografia e tipografia não possuem significado definitivo.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Home pública | web para computador | 1.440 × 2.200 |
| Início protegido — quatro estados | aplicativo móvel | 390 × 844 cada |
| Compreensão inicial — cinco estados | aplicativo móvel | 390 × 844 cada |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa e estados móveis | aplicativo móvel | 390 × 844 |
| Mapa com e sem resultados | web para computador | 1.440 × 1.024 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |
| Configuração do anunciante — cinco estados | computador e aplicativo móvel | 1.440 × 1.024 e 390 × 844 |
| Cartão e explicação | móvel e computador | 390 × 844 e 1.440 × 1.024 |
| Lista e Mapa patrocinados | móvel e computador | 390 × 844 e 1.440 × 1.024 |
| Gestão da campanha — seis estados | computador e aplicativo móvel | 1.440 × 1.024 e 390 × 844 |
| Relatório agregado — quatro estados | computador e aplicativo móvel | 1.440 × 1.024 e 390 × 844 |

## 8. Relação entre os wireframes

```text
oportunidade aprovada e ativa
→ elegibilidade para impulsionamento
→ objetivo e critérios
→ orçamento e duração
→ prévia e confirmação
→ envio para avaliação
→ aprovação e programação
→ campanha ativa
→ cartão | Lista | Mapa patrocinados
→ explicação e controles
→ limitação | pausa | alteração material
→ conclusão | cancelamento | suspensão
→ reconciliação
→ relatório agregado
```

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| Página Inicial e Início | UXA-020 | primeira entrada | contrato textual |
| Wireframe e validação da Home | UXA-021; UXA-022 | Home | validação e arquivo vetorial |
| Início Protegido | UXA-023; UXA-034; UXA-035 | início protegido | contrato, quatro SVGs e validação |
| Compreensão Inicial | UXA-036; UXA-037 | compreensão inicial | cinco SVGs e validação |
| Mapa e estados | UXA-024 a UXA-033 | Mapa | arquivos móveis, desktop e validações |
| Fluxo do anunciante para computador | UXA-040; UXA-041 | painel institucional | cinco SVGs e validação |
| Configuração móvel do anunciante | UXA-051; UXA-052 | painel institucional móvel | cinco SVGs reformulados e validados |
| Cartão e explicação | UXA-042; UXA-043 | experiência da pessoa | seis SVGs e validação |
| Lista e Mapa patrocinados | UXA-044; UXA-045 | Mapa e Lista | quatro SVGs e validação |
| Gestão para computador | UXA-046; UXA-047 | painel institucional | seis SVGs e validação |
| Gestão móvel | UXA-053; UXA-054 | painel institucional móvel | seis SVGs reformulados e validados |
| Relatório agregado | UXA-048; UXA-049 | painel institucional | quatro SVGs e validação |
| Validação transversal | UXA-050 | anunciante e participante | consolidação de 25 wireframes |

## 10. Resultados validados e materializados

A UXA-038 a UXA-054 demonstram contrato, configuração, entrega, explicação, Lista, Mapa, gestão desktop e móvel e relatório funcionalmente validados em seus respectivos pacotes.

A cobertura total do Opportunity Boost passa a:

- 36 wireframes materializados;
- 36 wireframes funcionalmente validados por pacote;
- 25 artefatos preservados sob a autoridade transversal histórica da UXA-050.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, armazenamento, IA, textos finais, responsividade, tablet, acessibilidade técnica, algoritmo publicitário, tecnologia cartográfica, política final de atribuição, agregação, reconciliação, cobrança, protótipo, teste de usabilidade ou Engenharia de Produto.

Estados completos de erro, inventário insuficiente e preferência publicitária permanecem não concluídos.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. criar estados de erro, inventário insuficiente e preferência publicitária;
2. validar transversalmente os 36 artefatos, se priorizado;
3. definir protocolo de protótipo de baixa ou média fidelidade;
4. preparar plano de teste com Pessoas, Organizações e Coletivos;
5. criar a referência móvel da Home;
6. validar a transição para a primeira Tela Hoje;
7. criar referência do início protegido e da compreensão para computador;
8. criar referência para tablet, caso priorizada.

Nenhuma etapa posterior é iniciada automaticamente.
