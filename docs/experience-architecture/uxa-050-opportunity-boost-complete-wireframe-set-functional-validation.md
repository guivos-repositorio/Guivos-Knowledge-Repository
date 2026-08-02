---
id: UXA-050
title: Validação Funcional Transversal do Conjunto Completo de Wireframes do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-02
parent: UXA-049
depends_on:
  - UXA-005
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
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.52
normative: false
---

# Validação Funcional Transversal do Conjunto Completo de Wireframes do Opportunity Boost

## 1. Finalidade

Este documento valida transversalmente o conjunto completo de wireframes de baixa fidelidade do Opportunity Boost.

A validação deixa de examinar uma tela isolada e verifica se os artefatos formam uma experiência contínua e coerente entre:

- elegibilidade;
- configuração;
- prévia e revisão;
- avaliação;
- programação;
- entrega patrocinada;
- explicação e controles da pessoa;
- Lista e Mapa;
- gestão da campanha ativa;
- alteração material;
- pausa, limitação, cancelamento e encerramento;
- reconciliação;
- relatório agregado.

## 2. Pergunta de validação

> **Os 25 wireframes do Opportunity Boost formam um percurso funcional único, preservam a mesma campanha e a mesma versão aprovada, mantêm publicidade separada da relevância orgânica, protegem a autonomia e os dados da pessoa e conduzem do investimento ao relatório sem prometer entrega, conversão, causalidade, impacto ou devolução?**

## 3. Resultado

O conjunto é considerado **funcionalmente válido após consolidação transversal**.

Não foram identificadas contradições que exijam reformulação adicional dos arquivos vetoriais já validados.

A consolidação necessária ocorre no nível de governança da experiência e estabelece uma autoridade única para:

- identidade da campanha;
- versão aprovada;
- continuidade entre superfícies;
- transições de estado;
- separação entre controles da pessoa e métricas do anunciante;
- preservação da origem orgânica;
- histórico e reconciliação;
- cobertura por canal;
- limites anteriores a protótipo e teste.

## 4. Conjunto examinado

| Pacote | Responsabilidade | Quantidade de wireframes | Estado anterior |
|---|---|---:|---|
| UXA-040 e UXA-041 | fluxo inicial do anunciante | 5 | validado e reformulado |
| UXA-042 e UXA-043 | cartão, explicação e Boost Social Financiado | 6 | validado e reformulado |
| UXA-044 e UXA-045 | Lista e Mapa patrocinados | 4 | validado e reformulado |
| UXA-046 e UXA-047 | gestão da campanha ativa | 6 | validado e reformulado |
| UXA-048 e UXA-049 | relatório agregado | 4 | validado e reformulado |
| **Total** | experiência visual do Opportunity Boost | **25** | validação transversal neste incremento |

## 5. Percurso transversal validado

```text
oportunidade aprovada e ativa
→ gate de elegibilidade
→ objetivo único
→ critérios permitidos e excluídos
→ orçamento, duração e limite diário
→ prévia separada do orgânico
→ revisão e confirmação afirmativa
→ envio para avaliação
→ ajustes | rejeição | aprovação
→ programação condicionada aos gates
→ campanha ativa
→ cartão, Lista e Mapa patrocinados identificados
→ explicação e controles da pessoa
→ limitação | pausa | alteração material
→ conclusão | cancelamento | suspensão
→ reconciliação
→ relatório agregado
```

Nenhuma transição autoriza automaticamente a seguinte quando o gate correspondente não estiver atendido.

## 6. Lacunas transversais identificadas

### 6.1 Identidade da campanha distribuída entre documentos

Os pacotes preservavam a campanha em suas próprias superfícies, mas não existia uma regra transversal explícita exigindo a mesma identidade entre configuração, prévia, entrega, gestão, histórico e relatório.

### 6.2 Versão aprovada sem autoridade consolidada

Alterações materiais já interrompiam entrega desatualizada. Faltava registrar, em uma única autoridade, que cada evento de entrega e cada relatório devem permanecer vinculados à versão aprovada vigente no momento do evento.

### 6.3 Vocabulário de estado distribuído

Os estados estavam funcionalmente corretos em cada pacote, porém precisavam de uma leitura transversal que impedisse atalhos como:

- aprovação diretamente para ativa sem programação válida;
- pausa diretamente para retomada sem verificação;
- cancelamento tratado como reconciliação concluída;
- encerramento tratado como relatório final imediatamente disponível.

### 6.4 Controles da pessoa separados das métricas do anunciante apenas localmente

Cartão, explicação, Lista e Mapa já protegiam preferências e ocultação. O relatório já proibia lista individual. Faltava declarar transversalmente que ações da pessoa não podem se transformar em identificação, perfil retrospectivo ou lista exportável ao anunciante.

### 6.5 Cobertura por canal sem matriz consolidada

O conjunto utiliza computador e aplicativo móvel de forma intencional, mas ainda não havia uma declaração única de que ausência de uma referência em determinado canal não autoriza inferir responsividade, equivalência ou implementação automática.

### 6.6 Handoff entre encerramento, reconciliação e relatório

Gestão e relatório estavam coerentes, mas faltava explicitar que encerramento preserva histórico, inicia ou aguarda reconciliação e somente então pode apresentar dados reconciliados, sem bloquear consulta de dados provisórios ou em revisão.

## 7. Consolidação aprovada

### 7.1 Identidade única da campanha

Toda superfície deverá preservar:

- identificador único da campanha;
- oportunidade vinculada;
- anunciante responsável;
- financiador e beneficiário, quando houver;
- objetivo principal;
- período aprovado;
- orçamento total;
- versão aprovada vigente;
- estado atual;
- histórico de transições.

A interface poderá resumir esses elementos, mas não poderá substituir silenciosamente a campanha ou misturar resultados de campanhas diferentes.

### 7.2 Versão aprovada e instantâneo material

A versão aprovada deverá registrar, no mínimo:

- título e conteúdo material da oportunidade;
- preço ou gratuidade;
- data, local e modalidade;
- responsável;
- capacidade declarada;
- critérios permitidos;
- superfícies;
- objetivo e métrica principal;
- orçamento, limite diário e período.

Cada evento de entrega será associado à versão válida no momento em que ocorreu.

Alteração material:

1. não reescreve eventos anteriores;
2. interrompe nova entrega quando necessário;
3. gera nova versão candidata;
4. exige avaliação quando aplicável;
5. somente altera entrega futura após aprovação e retomada válida.

### 7.3 Autoridade das transições de estado

O conjunto consolidado reconhece:

```text
rascunho
→ bloqueada | pronta para configurar
→ em avaliação
→ ajustes solicitados | rejeitada | aprovada
→ programada
→ ativa
→ ativa com entrega reduzida
→ pausada pelo anunciante | pausada automaticamente
→ alteração material em avaliação
→ orçamento esgotado | capacidade esgotada | oportunidade expirada
→ suspensa por política
→ concluída | cancelada
→ em reconciliação | parcialmente reconciliada | reconciliada
```

Regras:

- aprovação não inicia entrega automaticamente;
- programação depende da permanência dos gates;
- limitação mantém campanha ativa com entrega reduzida;
- pausa interrompe novos eventos, preservando eventos válidos anteriores;
- retomada depende da resolução e verificação da causa;
- alteração material não retoma entrega automaticamente;
- cancelamento encerra entrega futura, mas não apaga histórico;
- conclusão ou cancelamento não significam reconciliação imediata;
- reconciliação não significa devolução automática;
- relatório poderá apresentar estados provisório, em revisão, parcialmente reconciliado e reconciliado.

### 7.4 Continuidade entre prévia e entrega

A unidade entregue deverá permanecer funcionalmente compatível com a prévia aprovada quanto a:

- natureza patrocinada anterior ao conteúdo;
- anunciante e financiador;
- oportunidade beneficiada;
- preço ou gratuidade;
- data, local e modalidade;
- controles de explicação, ocultação e denúncia;
- separação do resultado orgânico;
- critérios permitidos e excluídos.

Diferenças de composição responsiva não podem alterar o significado material.

### 7.5 Continuidade entre Lista e Mapa

Lista e Mapa deverão preservar:

- a mesma consulta territorial;
- filtros objetivos;
- contagens orgânicas e patrocinadas separadas;
- ordem orgânica independente;
- identificador compartilhado entre marcador e cartão;
- preferência publicitária distinta dos filtros de oportunidade;
- localização opcional;
- gate `Pesquisar nesta área` após movimentação do Mapa.

Selecionar um marcador não altera silenciosamente a ordem da Lista nem cria nova consulta.

### 7.6 Controles da pessoa e consequência operacional

Os controles permanecem:

- `Ocultar esta campanha`;
- `Mostrar menos deste tipo`;
- `Não mostrar oportunidades patrocinadas`;
- `Revisar preferências`;
- `Denunciar`;
- `Contestar uso de dados`.

Consequências transversais:

- preferência negativa prevalece sobre entrega contratada;
- ocultar publicidade não reduz catálogo orgânico;
- denúncia não é registrada como preferência;
- contestação de dados não é tratada como denúncia de conteúdo;
- desfazer uma preferência não inicia campanha ou personalização retroativa;
- o anunciante não recebe identidade, perfil, sequência individual ou lista das pessoas que utilizaram os controles.

### 7.7 Separação entre orgânico e patrocinado

Em todo o conjunto:

- pagamento amplia distribuição, não relevância;
- o primeiro resultado orgânico permanece orgânico;
- inventário patrocinado ocupa espaços identificados;
- baixa oferta orgânica reduz publicidade;
- marcador patrocinado não encobre oportunidade orgânica;
- correspondência orgânica legítima permanece explicada separadamente;
- exposição patrocinada não reclassifica silenciosamente interação orgânica;
- relatório preserva origem patrocinada, orgânica e indeterminada;
- dupla atribuição silenciosa permanece proibida.

### 7.8 Boost Social Financiado

A identidade do financiamento deverá permanecer contínua entre prévia, unidade entregue, explicação, gestão e relatório:

- financiador;
- Coletivo beneficiário;
- oportunidade gratuita;
- finalidade declarada;
- ausência de autoridade sobre relevância, seleção ou resultado;
- ausência de acesso a relatos protegidos ou lista de pessoas.

O financiamento não concede plano pago ao beneficiário e não transforma a oportunidade em recomendação institucional.

### 7.9 Orçamento, entrega e saldo

O conjunto distingue:

- orçamento total;
- valor reservado;
- valor utilizado;
- saldo não utilizado;
- limite diário;
- eventos válidos;
- eventos invalidados;
- eventos em revisão;
- tratamento candidato do saldo.

Nenhum wireframe promete:

- alcance mínimo;
- consumo integral do orçamento;
- conversão;
- extensão automática do período;
- retomada automática;
- crédito, estorno ou devolução.

### 7.10 Mensuração e evidência

O percurso completo preserva quatro camadas:

1. entrega;
2. interação;
3. atribuição candidata;
4. autorrelato.

A consolidação confirma:

- impressão não é atenção garantida;
- clique não é conversão;
- início não é conclusão;
- atribuição candidata não é causalidade;
- autorrelato não é evento instrumentado;
- conversão não comprova impacto humano;
- ausência de dado não é zero;
- supressão por agregação não é zero;
- relatório agregado não cria lista individual.

### 7.11 Histórico e auditabilidade funcional

O histórico deverá permitir compreender:

- criação da campanha;
- versão enviada;
- decisão de avaliação;
- programação;
- ativações, limitações e pausas;
- alterações materiais;
- cancelamento ou conclusão;
- revisões de eventos;
- versão da regra candidata de atribuição;
- estado de reconciliação.

Histórico funcional não define tecnologia de auditoria, retenção jurídica ou armazenamento.

### 7.12 Cobertura por canal

| Área | Computador | Aplicativo móvel | Estado |
|---|---|---|---|
| configuração do anunciante | materializada | não materializada | desktop validado |
| cartão e explicação | materializada | materializada | ambos validados |
| Lista e Mapa patrocinados | materializada | materializada | ambos validados |
| gestão da campanha | materializada | não materializada | desktop validado |
| relatório agregado | materializada | materializada | ambos validados |

A ausência de gestão e configuração móveis permanece uma lacuna conhecida, não uma autorização para assumir equivalência automática.

## 8. Critérios transversais confirmados

Após a consolidação, o conjunto demonstra que:

- a campanha mantém identidade única durante todo o percurso;
- eventos permanecem associados à versão aprovada correspondente;
- alterações materiais afetam somente entrega futura;
- estados possuem motivos, consequências e gates conhecidos;
- configuração não inicia entrega;
- aprovação não inicia entrega;
- pausa, limitação e cancelamento possuem efeitos distintos;
- prévia e unidade entregue preservam significado material;
- Lista e Mapa representam a mesma consulta;
- publicidade permanece separada da ordenação orgânica;
- controles da pessoa são reversíveis e não reduzem catálogo orgânico;
- preferências negativas prevalecem sobre contratos de entrega;
- anunciante e financiador não recebem lista de pessoas;
- dados protegidos não alimentam segmentação ou relatório;
- orçamento não garante entrega, conversão ou impacto;
- encerramento não apaga histórico;
- reconciliação não promete devolução;
- relatório não transforma associação em causalidade;
- canais materializados possuem limites explícitos;
- nenhum wireframe inicia Engenharia de Produto.

## 9. Invariantes do Opportunity Boost

As seguintes regras não poderão ser removidas por design, protótipo ou implementação posterior sem nova decisão governada:

1. pagamento não altera relevância orgânica;
2. publicidade é identificada antes do conteúdo;
3. contexto protegido não alimenta publicidade;
4. primeiro resultado orgânico permanece orgânico;
5. baixa oferta orgânica reduz publicidade;
6. preferência negativa prevalece sobre entrega contratada;
7. localização permanece opcional;
8. mudança material impede entrega desatualizada;
9. pausa preserva eventos válidos anteriores;
10. cancelamento preserva histórico;
11. anunciante não recebe lista de visualizadores;
12. atribuição candidata não é causalidade;
13. autorrelato não é evento instrumentado;
14. ausência ou supressão de dado não é zero;
15. saldo não é devolução confirmada;
16. conversão não comprova impacto humano.

## 10. Lacunas residuais não bloqueantes

Permanecem fora do conjunto validado:

- configuração móvel do anunciante;
- gestão móvel da campanha;
- estados completos de erro técnico;
- inventário insuficiente operacional;
- falha de atualização ou sincronização;
- experiência detalhada de preferências publicitárias;
- política final de categorias;
- política final de atribuição;
- limiar definitivo de agregação e privacidade;
- política final de reconciliação, saldo, crédito, estorno e disputa;
- textos jurídicos finais;
- acessibilidade técnica;
- algoritmo, antifraude e tecnologia de entrega;
- exportação real;
- protótipo e testes com usuários.

Essas lacunas não invalidam o conjunto de baixa fidelidade atual, mas impedem protótipo operacional ou desenvolvimento sem decisões adicionais.

## 11. Estado funcional

`functionally_valid_after_cross_artifact_consolidation — twenty-five Opportunity Boost wireframes form a coherent governed journey; campaign identity, approved version, state transitions, participant controls, organic separation, reporting boundaries and channel coverage consolidated; prototype and testing not authorized`.

## 12. Limites

Esta validação não:

- altera os 25 arquivos vetoriais;
- cria novo wireframe;
- define design final;
- define política jurídica, fiscal, contábil ou de privacidade final;
- define algoritmo, perfil publicitário ou antifraude;
- define implementação responsiva;
- cria protótipo navegável;
- realiza teste com Pessoas, Organizações ou Coletivos;
- cria checkout, cobrança, campanha real ou produção;
- retoma Engenharia de Produto.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. definir o próximo pacote de estados residuais do Opportunity Boost;
2. criar configuração e gestão móvel, se priorizadas;
3. criar estados de erro, inventário insuficiente e preferência publicitária;
4. definir protocolo de protótipo de baixa ou média fidelidade;
5. preparar plano de teste com Pessoas, Organizações e Coletivos;
6. desenvolver política especializada de publicidade, atribuição, agregação e reconciliação;
7. validar preços, orçamento, CPM, CPC, densidade e frequência.

Nenhum ato é iniciado automaticamente.
