---
id: UXA-043
title: Validação Funcional e Reformulação dos Wireframes do Cartão Patrocinado e da Explicação do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-29
parent: UXA-042
depends_on:
  - UXA-004
  - UXA-005
  - UXA-009
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - UXA-042
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.45
normative: false
---

# Validação Funcional e Reformulação dos Wireframes do Cartão Patrocinado e da Explicação do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente os seis wireframes criados pela UXA-042 e registra as reformulações necessárias para que cartão, explicação, controles e Boost Social Financiado preservem transparência comercial, autonomia, separação orgânica e proteção de dados.

A pergunta de validação é:

> **A pessoa reconhece antes da interação que o conteúdo é patrocinado, entende quem pagou e por quê, distingue distribuição paga de recomendação e correspondência orgânica, conhece os critérios utilizados e excluídos e consegue ocultar, reduzir, desativar, revisar, denunciar ou contestar sem perder o catálogo orgânico?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova design visual, textos jurídicos finais, algoritmo, perfil publicitário, política de categorias, precificação, cobrança, acessibilidade técnica, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. cartão patrocinado padrão para aplicativo móvel;
2. explicação patrocinada padrão para aplicativo móvel;
3. cartão patrocinado padrão para computador;
4. explicação patrocinada padrão para computador;
5. cartão móvel do Boost Social Financiado;
6. explicação móvel do Boost Social Financiado;
7. identificação comercial anterior ao conteúdo;
8. ordem entre primeiro resultado orgânico e espaço patrocinado;
9. anunciante, financiador e beneficiário;
10. preço ou gratuidade;
11. critérios utilizados e não utilizados;
12. correspondência orgânica eventualmente coexistente;
13. ocultação, redução, desativação e reversão de preferências;
14. denúncia e contestação de dados;
15. acessibilidade e linguagem clara.

## 4. Lacunas identificadas

### 4.1 Denúncia e contestação combinadas no móvel

A explicação móvel apresentava `Denunciar conteúdo ou uso indevido`, reunindo em uma única ação dois fluxos funcionalmente distintos:

- problema no conteúdo ou na informação da oportunidade;
- possível uso indevido de dados ou critérios de distribuição.

A combinação poderia ocultar o destino, a consequência e a governança própria de cada ação.

### 4.2 Controles móveis incompletos

A versão móvel não apresentava de forma explícita todos os escopos estabelecidos pelo contrato:

- ocultar somente a campanha;
- mostrar menos daquele tipo;
- desativar oportunidades patrocinadas;
- revisar e desfazer preferências.

A ação genérica `Revisar publicidade e preferências` não permitia compreender a diferença entre os efeitos.

### 4.3 Primeiro resultado orgânico apenas declarado na variação social

O cartão do Boost Social Financiado dizia que o primeiro resultado orgânico estava preservado acima, mas não materializava esse resultado no próprio artefato.

A declaração sem representação visual não demonstrava a ordem funcional e poderia permitir interpretação divergente na etapa posterior de design.

### 4.4 Coexistência entre correspondência orgânica e distribuição paga não explicitada

A explicação para computador separava inventário orgânico e patrocinado, mas não indicava como informar a pessoa quando a mesma oportunidade também possuísse correspondência orgânica legítima.

Sem essa regra visível, pagamento e aderência orgânica poderiam ser percebidos como uma única razão.

### 4.5 Ação genérica de controles

Os cartões utilizavam `Mais opções`, expressão que não informava que o destino continha controles de publicidade, preferências, denúncia e contestação.

### 4.6 Financiamento social sem declaração direta de não recomendação

A variação social descrevia ausência de autoridade do financiador, mas a explicação não afirmava diretamente que financiamento amplia distribuição e não constitui recomendação.

## 5. Reformulação aprovada

### 5.1 Taxonomia de controles

Os controles passam a utilizar nomes e escopos distintos:

- `Ocultar esta campanha` — remove somente a campanha específica;
- `Mostrar menos deste tipo` — altera uma preferência geral identificada;
- `Não mostrar oportunidades patrocinadas` — desativa o inventário patrocinado nas superfícies suportadas;
- `Revisar e desfazer preferências` — permite compreender e reverter escolhas anteriores;
- `Denunciar conteúdo ou informação` — abre o fluxo de integridade da oportunidade;
- `Contestar uso indevido de dados` — abre o fluxo separado de privacidade e governança.

Nenhuma escolha começa selecionada.

### 5.2 Controles móveis completos

A explicação móvel padrão e a explicação social financiada passam a apresentar todos os controles essenciais sem depender de uma ação genérica.

Denúncia e contestação permanecem separadas e não são registradas como preferência publicitária.

### 5.3 Ordem orgânica materializada no Boost Social Financiado

O cartão social passa a demonstrar:

```text
primeiro resultado orgânico
→ espaço de impulsionamento social financiado
→ próximos resultados orgânicos
```

A oportunidade financiada não substitui o primeiro resultado orgânico e não participa silenciosamente da ordenação.

### 5.4 Correspondência orgânica coexistente

A explicação para computador passa a informar que, quando existir correspondência orgânica legítima para a mesma oportunidade, a interface deverá apresentar separadamente:

- razão orgânica;
- condição patrocinada;
- critérios de cada uma;
- ausência de influência do pagamento sobre a correspondência.

O exemplo reformulado também declara quando não existe correspondência orgânica naquele caso.

### 5.5 Destino compreensível dos controles

`Mais opções` é substituído por `Controles do anúncio`.

A ocultação imediata também informa `só este anúncio`, evitando que a pessoa interprete a ação como exclusão da categoria ou do catálogo orgânico.

### 5.6 Divulgação social financiada

A explicação social passa a declarar:

> **Financiamento amplia distribuição; não é recomendação.**

Também diferencia:

- Coletivo beneficiário;
- financiador;
- finalidade;
- gratuidade;
- critérios gerais usados;
- dados não utilizados ou compartilhados;
- poderes não concedidos ao financiador;
- controles disponíveis para a pessoa.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- a natureza comercial aparece antes do título e da ação principal;
- cor, borda ou ícone não são o único meio de identificação;
- o primeiro resultado orgânico aparece antes do espaço patrocinado;
- publicidade não é apresentada como recomendação, qualidade, confiança ou impacto;
- anunciante, financiador e beneficiário possuem rótulos próprios;
- preço ou gratuidade são compreensíveis;
- critérios utilizados são gerais, objetivos e visíveis;
- relato protegido, compreensão inicial, Momento Atual, Próximo Passo, mensagens e inferências sensíveis permanecem excluídos;
- o anunciante ou financiador não recebe lista de visualizadores;
- correspondência orgânica e distribuição paga são explicadas separadamente quando coexistirem;
- ocultação remove somente a campanha específica;
- redução, desativação e reversão possuem efeitos diferentes;
- denúncia e contestação são fluxos distintos;
- preferências negativas prevalecem sobre entrega contratada;
- ocultar publicidade não reduz busca, filtros, Lista, Mapa ou catálogo orgânico;
- financiamento social não transfere autoridade nem concede plano pago ao Coletivo beneficiário;
- nenhuma campanha, cobrança ou perfil publicitário é criado pelos artefatos.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-042-sponsored-card-mobile.svg`;
2. `uxa-042-sponsored-explanation-mobile.svg`;
3. `uxa-042-sponsored-card-desktop.svg`;
4. `uxa-042-sponsored-explanation-desktop.svg`;
5. `uxa-042-social-financed-card-mobile.svg`;
6. `uxa-042-social-financed-explanation-mobile.svg`.

Os artefatos permanecem em baixa fidelidade, com dimensões de referência de 390 × 844 pixels para móvel e 1.440 × 1.024 pixels para computador.

## 8. Proteções preservadas

- pagamento não compra relevância, recomendação, confiança, qualidade ou impacto;
- compreensão inicial, Momento Atual e Próximo Passo não alimentam publicidade;
- mensagens, relatos e inferências sensíveis permanecem excluídos;
- primeiro resultado orgânico permanece orgânico;
- baixa oferta orgânica reduz publicidade;
- duas unidades patrocinadas consecutivas permanecem proibidas;
- densidade candidata máxima permanece em 20%;
- nenhum financiador seleciona pessoas ou recebe autoridade funcional;
- nenhum controle é pré-selecionado;
- ocultação não reduz o catálogo orgânico;
- nenhuma métrica é apresentada como impacto humano comprovado.

## 9. Limites

Esta validação não cria:

- estados patrocinados para Lista ou Mapa;
- gestão de campanha ativa;
- relatório agregado do anunciante;
- design visual final;
- protótipo navegável;
- teste com usuários;
- algoritmo, perfil publicitário ou motor de entrega;
- política jurídica, fiscal ou contábil final;
- checkout, cobrança ou Engenharia de Produto.

## 10. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar os wireframes dos estados patrocinados para Lista e Mapa;
2. validar funcionalmente e reformular esses estados;
3. criar os wireframes de gestão da campanha ativa;
4. criar o wireframe do relatório agregado;
5. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
6. testar posteriormente disclosure, densidade, frequência e controles com Pessoas, Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
