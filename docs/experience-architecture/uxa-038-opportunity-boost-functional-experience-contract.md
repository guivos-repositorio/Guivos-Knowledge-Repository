---
id: UXA-038
title: Opportunity Boost — Contrato Funcional da Experiência
status: active
version: 0.2.0
owner: Guivos Experience Architecture
last_updated: 2026-07-28
parent: UXA-000
depends_on:
  - UXA-004
  - UXA-009
  - UXA-011-A1
  - UXA-024
  - UXA-025
  - GEM-007-A1
related:
  - UXA-039
  - GEM-010-A2
  - GPA-007
  - M7.41
normative: false
---

# Opportunity Boost — Contrato Funcional da Experiência

## 1. Finalidade

Definir como o Opportunity Boost será criado, identificado, distribuído, explicado, controlado, pausado e encerrado sem ser confundido com relevância orgânica ou recomendação pessoal.

## 2. Princípio de apresentação

> **Impulsionamento amplia distribuição publicitária; não altera a avaliação funcional da oportunidade.**

Toda unidade patrocinada deverá ser reconhecível antes de qualquer interação. Pagamento não modifica qualidade, confiança, aderência, impacto, prioridade orgânica ou posição de Próximo Passo.

## 3. Gate de entrada do anunciante

A ação `Impulsionar oportunidade` somente poderá ficar disponível quando:

- o anunciante possuir plano elegível ou financiamento social válido;
- a oportunidade estiver aprovada e ativa;
- o responsável institucional estiver identificado;
- preço, gratuidade e condições materiais estiverem atualizados;
- datas, local, modalidade e disponibilidade estiverem vigentes;
- houver capacidade para atender demanda adicional;
- não existir pendência crítica de segurança ou moderação.

Estados de bloqueio visíveis:

- `Plano não elegível`;
- `Oportunidade ainda não aprovada`;
- `Oportunidade inativa ou expirada`;
- `Informações materiais desatualizadas`;
- `Capacidade insuficiente`;
- `Pendência de segurança ou moderação`;
- `Responsável institucional ausente`.

Cada bloqueio mostrará motivo, consequência e ação de correção. Contratar plano não substitui aprovação, atualização, segurança ou capacidade.

## 4. Superfícies permitidas

- Explorar;
- busca;
- listas de oportunidades;
- categorias e coleções públicas;
- Mapa;
- detalhe, em módulo separado;
- páginas públicas da Organização ou do Coletivo responsável.

## 5. Superfícies bloqueadas

- entrada protegida;
- compreensão inicial;
- consentimento, autorização ou revisão de dados;
- Próximo Passo da Tela Hoje;
- Jornada como recomendação individual;
- alertas pessoais sem opt-in próprio;
- segurança, privacidade, contestação e suporte.

## 6. Cartão impulsionado

O cartão deverá apresentar:

- selo `Patrocinado` ou `Impulsionado` antes do conteúdo;
- título e tipo da oportunidade;
- Organização ou Coletivo responsável;
- data, modalidade e localização aplicável;
- preço, gratuidade ou condição material;
- capacidade ou prazo quando relevante;
- ação `Ver detalhes`;
- ação `Por que estou vendo isto?`;
- ações de ocultar e denunciar.

Não deverá apresentar:

- selo de recomendação;
- aderência pessoal aumentada pelo pagamento;
- pontuação artificial;
- urgência criada pelo anúncio;
- afirmação de que a Guivos recomenda o anunciante;
- posição patrocinada como se fosse posição orgânica.

## 7. Por que estou vendo isto?

A explicação deverá distinguir:

```text
Motivo da distribuição
→ campanha paga identificada

Critérios utilizados
→ região, idioma, categoria, modalidade, data, preço ou preferência geral permitida

Critérios não utilizados
→ relato protegido, compreensão inicial, Momento Atual, Próximo Passo e inferências sensíveis

Controles
→ ocultar, revisar preferências ou denunciar
```

Quando a oportunidade também possuir correspondência orgânica legítima, a interface deverá separar:

- razão orgânica;
- condição patrocinada;
- critérios de cada uma;
- ausência de influência do pagamento sobre a correspondência.

## 8. Ordenação, densidade e frequência

- inventário patrocinado e orgânico serão separados;
- o primeiro resultado orgânico permanecerá orgânico;
- espaços patrocinados serão identificados e não participarão silenciosamente da ordenação orgânica;
- duas unidades patrocinadas não aparecerão consecutivamente;
- a densidade candidata máxima será de 20%;
- havendo oferta orgânica suficiente, existirão quatro itens orgânicos entre anúncios;
- havendo menos de quatro itens orgânicos disponíveis, a quantidade de anúncios será reduzida;
- ausência de inventário orgânico suficiente nunca autoriza aumentar densidade;
- filtros objetivos de data, preço, distância, modalidade e elegibilidade continuarão obrigatórios;
- ocultação e preferência negativa prevalecerão sobre entrega contratada;
- repetição excessiva será evitada por limite de frequência por campanha e superfície.

## 9. Mapa

No Mapa, o Boost utilizará:

- marcador visual próprio;
- identificação textual acessível;
- agrupamento com quantidades patrocinadas e orgânicas separadas;
- filtro reversível `Mostrar oportunidades patrocinadas`;
- detalhe com anunciante, período e motivo da exibição;
- ausência de uso de localização contínua ou histórico sensível;
- preservação de pontos orgânicos sem encobrimento por marcadores pagos.

O marcador patrocinado não indicará maior qualidade, confiança, aderência ou proximidade funcional. Distância não será apresentada como recomendação.

## 10. Fluxo do anunciante

```text
Gestão da oportunidade
→ Impulsionar oportunidade
→ verificar elegibilidade e bloqueios
→ escolher objetivo de distribuição
→ selecionar critérios permitidos
→ revisar critérios excluídos
→ definir orçamento, duração e limite diário
→ revisar superfícies e prévia
→ revisar responsabilidade, capacidade e condições
→ confirmar sem opção pré-selecionada
→ enviar para avaliação
→ acompanhar campanha
→ pausar, corrigir, cancelar ou encerrar
→ consultar relatório e reconciliação
```

A interface deverá mostrar que:

- o Boost é separado do plano;
- o orçamento não garante resultados;
- a oportunidade continuará sujeita à moderação;
- capacidade e disponibilidade precisam permanecer atualizadas;
- o ranking orgânico não será alterado;
- não existe renovação automática por padrão;
- mudança material poderá pausar a campanha.

## 11. Objetivo e métrica principal

O anunciante deverá escolher uma única finalidade principal:

- ampliar visualizações válidas;
- levar pessoas ao detalhe;
- aumentar salvamentos;
- estimular declaração de interesse;
- iniciar inscrição ou contratação legítima;
- divulgar atividade ou programa em região permitida.

Nenhum objetivo será selecionado por padrão.

A superfície deverá mostrar:

- métrica principal associada;
- eventos secundários;
- ausência de garantia;
- critérios proibidos;
- impossibilidade de otimizar relevância pessoal, confiança ou impacto.

Não serão objetivos permitidos:

- aumentar relevância pessoal;
- forçar recomendação;
- obter dados protegidos;
- manipular avaliações;
- garantir conversão ou impacto.

## 12. Resumo de critérios e alcance

Antes da prévia, a interface apresentará:

- critérios utilizados;
- critérios excluídos;
- superfícies previstas;
- alcance estimado agregado;
- aviso de que estimativa não é garantia;
- eventual limitação por público insuficiente.

A ausência de público suficiente deverá reduzir ou impedir a campanha, sem ampliação silenciosa de critérios.

## 13. Prévia e revisão final

A prévia deverá demonstrar:

- selo comercial antes do conteúdo;
- cartão ou marcador patrocinado;
- espaço publicitário separado;
- primeiro resultado orgânico preservado;
- filtros objetivos aplicados;
- explicação da distribuição;
- controles de ocultação e denúncia;
- variações para Explorar, Lista, Mapa e detalhe.

Antes do envio, o anunciante revisará:

- oportunidade e responsável;
- financiador, quando houver;
- objetivo e métrica principal;
- critérios utilizados e excluídos;
- superfícies;
- orçamento total e limite diário;
- início, fim e regra de encerramento;
- preço ou gratuidade;
- capacidade declarada;
- ausência de renovação automática;
- ausência de garantia;
- efeitos de pausa, alteração material e cancelamento.

A confirmação será afirmativa e inicialmente desmarcada.

## 14. Alterações materiais durante a campanha

Mudança em preço, gratuidade, data, local, modalidade, responsável, elegibilidade, risco, capacidade ou condição comercial deverá:

1. pausar a campanha quando puder alterar a decisão da pessoa;
2. mostrar a informação alterada;
3. exigir nova avaliação quando necessário;
4. impedir entrega com informação desatualizada;
5. preservar histórico e eventos válidos anteriores;
6. recalcular somente estimativas futuras.

Correções editoriais sem mudança material poderão continuar, mantendo histórico.

## 15. Estados visíveis

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

Cada estado deverá explicar:

- motivo;
- consequência sobre entrega;
- efeito sobre orçamento e saldo;
- ação possível;
- condição para retomada.

## 16. Boost Social Financiado

Quando aplicável, a unidade e a explicação deverão apresentar:

- `Impulsionamento social financiado`;
- Organização ou parceiro financiador;
- Coletivo beneficiário;
- oportunidade gratuita;
- finalidade declarada do financiamento;
- declaração de que o financiador não define relevância pessoal, seleção ou resultado;
- ausência de acesso do financiador a relatos, contexto da jornada ou lista de pessoas expostas.

O financiamento não transforma a oportunidade em recomendação institucional nem concede plano pago ao Coletivo Livre.

## 17. Controles da pessoa

O participante poderá:

- abrir a oportunidade;
- compreender a relação comercial;
- ocultar a campanha específica;
- mostrar menos de um tipo identificado;
- revisar preferências gerais;
- desativar oportunidades patrocinadas nas superfícies que suportarem a opção;
- denunciar conteúdo ou informação;
- contestar uso indevido de dados;
- desfazer preferências anteriores.

Escopos:

- `Ocultar esta campanha` remove a campanha específica nas superfícies aplicáveis;
- `Mostrar menos deste tipo` altera preferência geral identificada;
- `Não mostrar oportunidades patrocinadas` desativa o inventário patrocinado suportado;
- `Denunciar` abre fluxo separado e não é tratado como preferência.

Nenhuma escolha será pré-selecionada. Ocultar publicidade não reduzirá acesso ao catálogo orgânico nem será interpretado como desinteresse na categoria orgânica.

## 18. Relatório do anunciante

O painel deverá separar:

### Entrega

- orçamento total, utilizado e remanescente;
- período e status;
- impressões válidas e visíveis;
- frequência média;
- tráfego inválido removido.

### Interação

- cliques válidos;
- visualizações do detalhe;
- salvamentos;
- interesses agregados;
- início de inscrição ou contratação, quando disponível.

### Atribuição candidata

- eventos compatíveis com janela e instrumentação;
- origem orgânica preservada nos relatórios internos;
- ausência de dupla atribuição silenciosa.

### Resultado declarado

- informação fornecida pelo anunciante;
- identificação explícita como autorrelato;
- distinção de evento instrumentado.

Ausência de dado não será apresentada como zero. Nenhuma lista de visualizadores será fornecida. Métricas não serão apresentadas como impacto humano comprovado.

## 19. Pausa, cancelamento e reconciliação

Antes de pausar ou cancelar, a experiência deverá mostrar:

- entrega futura afetada;
- eventos válidos já realizados;
- orçamento utilizado;
- saldo remanescente;
- tratamento candidato do saldo;
- possibilidade de retomada;
- motivo de eventual retenção legítima;
- acesso posterior ao relatório e histórico.

Pausa será reversível quando a causa permitir. Cancelamento encerrará entrega futura e exigirá confirmação proporcional à ativação.

## 20. Acessibilidade e linguagem

- identificação patrocinada não dependerá apenas de cor;
- leitores de tela anunciarão a natureza comercial antes do conteúdo;
- preço e condições permanecerão compreensíveis;
- controles de ocultação e denúncia serão acessíveis;
- estados explicarão motivo, consequência e próxima ação;
- não serão usados padrões de urgência, culpa ou escassez artificial;
- cancelamento e pausa terão complexidade proporcional à ativação.

## 21. Estado funcional

`functionally_valid_after_reformulation — advertiser flow, participant controls, sponsored disclosure, state model and reporting boundaries established; wireframes and evidence pending`.

## 22. Limites

Este contrato não cria design final, algoritmo, compra de mídia, checkout, cobrança, perfil publicitário individual, política final de categorias, antifraude técnico, protótipo, teste ou desenvolvimento.

A experiência deverá passar por wireframes, validação dos wireframes e testes com Pessoas, Organizações e Coletivos antes de qualquer operação.
