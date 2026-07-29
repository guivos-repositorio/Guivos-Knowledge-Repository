---
id: UXA-039
title: Validação Funcional Especializada e Reformulação da Experiência do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
parent: UXA-038
depends_on:
  - UXA-001
  - UXA-004
  - UXA-009
  - UXA-011-A1
  - UXA-024
  - UXA-025
  - UXA-038
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.41
normative: false
---

# Validação Funcional Especializada e Reformulação da Experiência do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente o contrato da experiência do Opportunity Boost e registra as reformulações necessárias antes da criação de qualquer wireframe.

A pergunta de validação é:

> **Uma Organização ou um Coletivo consegue configurar, revisar, acompanhar, pausar e encerrar uma campanha com orçamento e consequências compreensíveis, enquanto a pessoa reconhece imediatamente a natureza patrocinada, compreende por que está vendo o conteúdo e controla sua exposição sem que pagamento altere relevância orgânica, recomendação pessoal ou acesso ao catálogo?**

## 2. Resultado

A experiência é considerada **funcionalmente válida após reformulação**.

A validação confirma a viabilidade funcional do fluxo, mas não aprova design visual, textos jurídicos finais, algoritmo de entrega, política de categorias, perfil publicitário, cobrança, antifraude técnico, protótipo, testes com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. entrada do anunciante a partir de uma oportunidade ativa;
2. verificação de plano, oportunidade, capacidade e responsabilidade;
3. objetivo de distribuição;
4. critérios permitidos e exclusões obrigatórias;
5. orçamento, duração, limite diário e ausência de renovação automática;
6. prévia e revisão final;
7. avaliação e estados da campanha;
8. alterações materiais durante a campanha;
9. cartão patrocinado e explicação da distribuição;
10. ordenação, densidade e frequência;
11. experiência no Mapa;
12. controles da pessoa;
13. Boost Social Financiado;
14. relatório e atribuição;
15. cancelamento, saldo e reconciliação.

## 4. Lacunas identificadas

### 4.1 Entrada sem bloqueios suficientemente explícitos

O contrato previa confirmação de elegibilidade, mas não materializava os motivos pelos quais a ação `Impulsionar oportunidade` deveria permanecer indisponível.

### 4.2 Objetivo sem consequência operacional visível

Os objetivos permitidos estavam listados, porém faltava explicar que a escolha altera a métrica principal e não autoriza otimização por dados protegidos.

### 4.3 Resumo de público incompleto

A configuração não exigia um inventário final dos critérios utilizados, excluídos e indisponíveis antes do envio.

### 4.4 Prévia sem separação obrigatória entre orgânico e patrocinado

A prévia precisava demonstrar o espaço publicitário sem simular aumento de posição orgânica, confiança ou recomendação.

### 4.5 Alterações materiais durante a campanha

Não estava definido o efeito de mudança de preço, gratuidade, data, local, capacidade, responsável, elegibilidade ou risco após a ativação.

### 4.6 Estados insuficientes para bloqueio, recusa e esgotamento

O ciclo não distinguia inelegibilidade, rejeição, orçamento esgotado, capacidade esgotada e expiração da oportunidade.

### 4.7 Divulgação do Boost Social Financiado incompleta

A experiência precisava identificar financiador, beneficiário e ausência de autoridade do financiador, sem transformar apoio social em recomendação institucional.

### 4.8 Controles da pessoa sem escopo e reversibilidade

`Ocultar campanha`, `ocultar semelhantes` e `desativar patrocinadas` não esclareciam abrangência, duração, consequência ou forma de desfazer.

### 4.9 Densidade em cenários de baixa oferta orgânica

A regra de quatro itens orgânicos entre anúncios não declarava que a ausência de inventário orgânico suficiente deve reduzir a publicidade, e nunca aumentar sua densidade.

### 4.10 Ordenação objetiva e espaços patrocinados

Faltava declarar que filtros e ordenações por data, preço, distância ou disponibilidade não conferem ao anúncio posição orgânica equivalente.

### 4.11 Relatório sem distinção suficiente entre entrega e atribuição

As métricas estavam corretas, mas o painel precisava separar entrega, interação, atribuição candidata e resultado informado pelo anunciante.

### 4.12 Cancelamento e reconciliação sem percurso funcional completo

O contrato econômico previa saldo e reconciliação, mas a experiência ainda não descrevia confirmação, consequência e acesso ao histórico após o encerramento.

## 5. Reformulação aprovada

### 5.1 Gate de entrada

A ação para impulsionar deverá apresentar uma das condições:

- `Disponível para impulsionamento`;
- `Plano não elegível`;
- `Oportunidade ainda não aprovada`;
- `Oportunidade inativa ou expirada`;
- `Informações materiais desatualizadas`;
- `Capacidade insuficiente`;
- `Pendência de segurança ou moderação`;
- `Responsável institucional ausente`.

Cada bloqueio deverá explicar motivo, consequência e ação de correção. A contratação de plano não poderá substituir aprovação, capacidade ou segurança.

### 5.2 Objetivo e métrica principal

A campanha exigirá uma escolha única de objetivo. A interface deverá informar:

- métrica principal associada;
- eventos secundários disponíveis;
- ausência de garantia de resultado;
- critérios que não serão utilizados;
- impossibilidade de otimizar relevância pessoal, confiança ou impacto.

Nenhum objetivo será selecionado por padrão.

### 5.3 Inventário de público e exclusões

Antes da prévia, a interface mostrará:

```text
Critérios utilizados
→ região, idioma, categoria, modalidade, data, preço ou preferência geral permitida

Critérios excluídos
→ relato protegido, compreensão inicial, Momento Atual, Próximo Passo e inferências sensíveis

Alcance estimado
→ estimativa agregada, não garantia
```

A ausência de público suficiente deverá impedir ou limitar a campanha, sem ampliar silenciosamente os critérios.

### 5.4 Prévia fiel

A prévia deverá mostrar separadamente:

- cartão ou marcador patrocinado;
- selo comercial antes do conteúdo;
- posição publicitária candidata;
- primeiro resultado orgânico preservado;
- filtros objetivos aplicados;
- ação `Por que estou vendo isto?`;
- controles de ocultação e denúncia;
- variações para Lista, Explorar, Mapa e detalhe.

A prévia não poderá exibir pontuação de aderência ou selo de recomendação.

### 5.5 Revisão final do anunciante

Antes do envio, a superfície deverá consolidar:

- oportunidade impulsionada;
- responsável e financiador, quando houver;
- objetivo e métrica principal;
- critérios permitidos;
- critérios expressamente não utilizados;
- superfícies;
- orçamento total e limite diário;
- início, fim e regra de encerramento;
- preço ou gratuidade da oportunidade;
- capacidade declarada;
- ausência de renovação automática;
- ausência de garantia de entrega ou conversão;
- consequências de pausa, alteração material e cancelamento.

A confirmação será afirmativa e inicialmente desmarcada.

### 5.6 Alterações durante a campanha

Mudança material em preço, gratuidade, data, local, modalidade, responsável, elegibilidade, risco, capacidade ou condição comercial deverá:

1. pausar a campanha quando puder alterar a decisão da pessoa;
2. mostrar o item alterado;
3. exigir nova avaliação quando necessário;
4. impedir entrega com informação desatualizada;
5. preservar histórico e eventos válidos anteriores;
6. recalcular somente estimativas futuras.

Correções editoriais sem mudança de significado poderão continuar sem nova avaliação, mantendo histórico.

### 5.7 Estados reformulados

O ciclo passa a distinguir:

```text
rascunho
→ bloqueada por inelegibilidade | pronta para configurar
→ em avaliação
→ ajustes solicitados | rejeitada | aprovada
→ programada
→ ativa
→ limitada por frequência | limitada por capacidade
→ pausada pelo anunciante | pausada automaticamente
→ orçamento esgotado | capacidade esgotada | oportunidade expirada
→ suspensa por política
→ concluída | cancelada
→ reconciliada
```

Cada estado deverá mostrar motivo, impacto sobre entrega, saldo, ações possíveis e condição para retomada.

### 5.8 Boost Social Financiado

A unidade e a página de explicação deverão apresentar:

- `Impulsionamento social financiado`;
- Organização ou parceiro financiador;
- Coletivo beneficiário;
- oportunidade gratuita;
- finalidade declarada do financiamento;
- declaração de que o financiador não define relevância pessoal, seleção ou resultado;
- ausência de acesso do financiador a relatos, contexto da jornada ou lista de pessoas expostas.

### 5.9 Controles da pessoa

Os controles deverão possuir escopo conhecido:

- `Ocultar esta campanha` — remove a campanha específica nas superfícies aplicáveis;
- `Mostrar menos deste tipo` — ajusta uma preferência geral identificada;
- `Não mostrar oportunidades patrocinadas` — desativa inventário patrocinado nas superfícies que suportarem a opção;
- `Denunciar` — abre fluxo separado, sem ser tratado como preferência;
- `Revisar preferências` — permite consultar e desfazer escolhas.

Nenhuma escolha será pré-selecionada. Ocultar publicidade não reduz o catálogo orgânico, não altera acesso e não será interpretado como desinteresse na categoria orgânica.

### 5.10 Ordenação, densidade e frequência

- o primeiro resultado orgânico permanece orgânico;
- anúncios ocupam espaços próprios e identificados;
- ordenação objetiva não converte posição paga em posição orgânica;
- densidade máxima candidata permanece em 20%;
- duas unidades patrocinadas consecutivas continuam proibidas;
- havendo menos de quatro itens orgânicos disponíveis, a quantidade de anúncios será reduzida;
- ausência de inventário orgânico suficiente nunca autoriza aumentar densidade;
- limite de frequência será aplicado por campanha e superfície;
- ocultação e preferência negativa prevalecem sobre entrega contratada.

### 5.11 Mapa

No Mapa:

- marcador patrocinado terá forma e texto próprios;
- agrupamento indicará quantidade patrocinada e orgânica separadamente;
- o filtro de patrocinadas será reversível;
- ponto patrocinado não encobrirá ponto orgânico;
- distância não será apresentada como aderência;
- localização contínua e histórico sensível permanecerão proibidos;
- ausência de localização não impedirá exploração por região informada.

### 5.12 Relatório e atribuição

O relatório deverá separar quatro camadas:

1. **entrega** — impressões válidas, visibilidade, frequência e orçamento;
2. **interação** — cliques, detalhe, salvamentos e interesse agregado;
3. **atribuição candidata** — eventos compatíveis com a janela e instrumentação;
4. **resultado declarado** — informação fornecida pelo anunciante, identificada como autorrelato.

Não serão exibidas listas de visualizadores. Ausência de dado não será mostrada como zero. Impacto humano não será inferido a partir de alcance ou conversão.

### 5.13 Pausa, cancelamento e reconciliação

A experiência deverá mostrar antes da confirmação:

- entrega que será interrompida;
- eventos válidos já realizados;
- orçamento utilizado;
- saldo remanescente;
- tratamento candidato do saldo;
- possibilidade de revisão futura;
- motivo de eventual retenção legítima;
- acesso posterior ao relatório e histórico.

Pausar será reversível quando a causa permitir. Cancelar encerrará entrega futura e exigirá confirmação proporcional à ativação.

## 6. Critérios funcionais confirmados

Após a reformulação, a experiência demonstra que:

- somente anunciante e oportunidade elegíveis avançam;
- plano pago não substitui aprovação ou capacidade;
- objetivo não autoriza segmentação sensível;
- critérios utilizados e proibidos são visíveis;
- alcance estimado não é promessa;
- prévia diferencia publicidade de resultado orgânico;
- alteração material pausa entrega desatualizada;
- bloqueio, rejeição, esgotamento e expiração são estados distintos;
- Boost Social Financiado identifica financiador sem transferir autoridade;
- ocultação possui escopo e pode ser revista;
- ocultar anúncio não reduz acesso orgânico;
- baixa oferta orgânica reduz publicidade;
- ranking e ordenação orgânicos permanecem independentes;
- Mapa não transforma patrocínio em proximidade funcional;
- relatório distingue entrega, interação, atribuição e autorrelato;
- pausa, cancelamento e reconciliação possuem consequências conhecidas;
- nenhuma lista individual é entregue ao anunciante;
- publicidade permanece fora da jornada protegida e do Próximo Passo pessoal.

## 7. Proteções preservadas

- pagamento não aumenta relevância, confiança, impacto ou evidência;
- catálogo orgânico permanece acessível;
- compreensão inicial e contexto protegido não alimentam publicidade;
- preferências negativas não são contornadas;
- ausência de consentimento não é tratada como interesse;
- localização permanece opcional;
- dados sensíveis não são inferidos para segmentação;
- patrocinador não recebe autoridade sobre o beneficiário;
- métricas não são apresentadas como evolução humana;
- nenhuma urgência, culpa ou escassez artificial será utilizada;
- Engenharia de Produto permanece pausada.

## 8. Limites

Esta validação não:

- define textos jurídicos finais;
- aprova categorias publicitárias;
- define algoritmo de entrega ou leilão;
- define perfil publicitário individual;
- define política final de retenção ou consentimento;
- calibra densidade, frequência, CPM ou CPC;
- conclui custos, margem ou antifraude;
- implementa checkout, faturamento, saldo ou reembolso;
- cria wireframes;
- cria design visual;
- cria protótipo;
- executa teste com usuários;
- inicia campanha real, piloto ou produção;
- inicia Engenharia de Produto.

## 9. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar wireframes de baixa fidelidade do fluxo do anunciante;
2. criar wireframes do cartão patrocinado e da explicação de distribuição;
3. criar estados patrocinados para Lista e Mapa;
4. criar wireframe do relatório agregado;
5. validar funcionalmente os wireframes do Opportunity Boost;
6. validar preços, orçamentos e disposição a pagar;
7. definir política especializada de publicidade e categorias;
8. retomar a referência móvel da Home e a transição para a primeira Tela Hoje.

Nenhum ato é iniciado automaticamente.
