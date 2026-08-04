---
id: UXA-063
title: Validação Funcional e Reformulação do Perfil Público Móvel do Coletivo
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
related:
  - UXA-064
  - M7.65
normative: false
---

# Validação Funcional e Reformulação do Perfil Público Móvel do Coletivo

## 1. Finalidade

Este documento valida funcionalmente os quatro wireframes móveis materializados pela UXA-062 e registra as reformulações necessárias antes de iniciar a Solicitação de Participação.

A validação examina a família como uma continuidade única:

```text
origem orgânica, publicidade ou convite
→ compreender identidade, propósito e funcionamento
→ distinguir acompanhar, participar, solicitar ou aguardar
→ revisar regras, responsabilidade e relações
→ interpretar reputação contextual
→ utilizar proteção, canais públicos ou denúncia
→ retornar à origem sem perder contexto
```

A UXA-063 não cria novos SVGs, protótipo, identidade visual, teste com pessoas ou implementação.

## 2. Artefatos avaliados

| Artefato | Estado anterior | Resultado |
|---|---|---|
| Perfil Público com entrada aberta | materializado; pendente | reformulado e validado |
| Perfil Público com aprovação | materializado; pendente | reformulado e validado |
| Perfil Público com entradas indisponíveis | materializado; pendente | reformulado e validado |
| Apresentação protegida por convite | materializado; pendente | reformulado e validado |

Resultado da família:

- quatro SVGs materializados;
- quatro SVGs reformulados;
- quatro SVGs funcionalmente validados;
- zero novo SVG;
- zero pendência funcional dentro desta família.

## 3. Critérios aplicados

A revisão verificou:

1. origem identificada sem confundir busca, publicidade e convite;
2. retorno com consulta, região, posição ou convite preservados;
3. estado de entrada visível antes da ação;
4. separação entre acompanhar, participar e solicitar participação;
5. ausência de vínculo automático;
6. regras e dados revisáveis antes de confirmação;
7. contagens governadas sem ranking;
8. lista nominal protegida;
9. responsáveis e Organizações com autoridade delimitada;
10. reputação suficiente, insuficiente ou suprimida com contexto;
11. publicidade sem compra de legitimidade;
12. perfil protegido sem exposição incompatível;
13. canais públicos sem promessa de contato privado;
14. denúncia separada de avaliação;
15. ausência de antecipação das superfícies seguintes.

## 4. Achados e reformulações

### 4.1 Denominadores da reputação

O perfil com entrada aberta apresentava percentuais e total geral, mas não informava o denominador de cada dimensão.

Reformulação:

- `Descrição correspondeu: 91% · 82 respostas`;
- `Respeito e segurança: 94% · 84 respostas`;
- período e total geral preservados;
- método, distribuição e limitações continuam acessíveis.

Decisão validada:

> percentual público exige denominador por dimensão quando as quantidades de resposta puderem variar.

### 4.2 Compartilhamento não é recomendação

A ação genérica `Compartilhar` poderia ser lida como endosso.

Reformulação:

- ação alterada para `Compartilhar perfil` nos estados públicos;
- o documento mantém que compartilhar distribui referência permitida;
- recomendação continua uma experiência distinta da UXA-058;
- apresentação protegida permanece sem compartilhamento externo.

### 4.3 Canais públicos não são contato privado

O rótulo `Proteção e contato` poderia sugerir telefone, e-mail ou mensagem privada.

Reformulação:

- ação alterada para `Proteção e canais públicos` nos estados públicos;
- contato privado continua dependente de autorização e contrato específico;
- participar do mesmo Coletivo não autoriza mensagem direta.

### 4.4 Dados da solicitação

No estado mediante aprovação, a ausência de vínculo estava clara, mas o momento de envio dos dados precisava ser explícito.

Reformulação:

> **Só serão enviados dados revisados; a solicitação ainda não cria vínculo.**

Decisão validada:

- o perfil apresenta critérios e dados necessários;
- a futura superfície de solicitação revisará conteúdo e permissões;
- nenhum dado adicional será enviado apenas por tocar no perfil ou acompanhar o Coletivo.

### 4.5 Autoridade e publicidade

O perfil com entradas indisponíveis utilizava a mesma Organização como anunciante e responsável, criando ambiguidade entre relação comercial e autoridade operacional.

Reformulação:

- responsável operacional identificado como `Júlia Andrade`;
- anunciante preservado como `Associação Movimento Livre`;
- relação comercial desta visita permanece em bloco separado;
- controle `Por que este anúncio?` foi incluído na origem;
- publicidade não altera regras, reputação ou autoridade.

### 4.6 Reputação no estado fechado

O estado fechado utilizava uma descrição genérica de reputação.

Reformulação:

- quantidade verificada e período foram informados;
- alterações de período permanecem preservadas;
- fechamento operacional não reescreve avaliações anteriores;
- distribuição, mudanças e limitações possuem caminho próprio.

### 4.7 Proveniência do convite protegido

A apresentação protegida informava apenas que o convite vinha de pessoa identificada, sem mostrar quem era ou qual autoridade possuía.

Reformulação:

- remetente identificado como `Ana Ribeiro`;
- autoridade identificada como `responsável autorizada`;
- motivo do convite exibido antes da continuidade;
- acesso individual e proibição de encaminhamento permanecem claros;
- a revisão especializada continua necessária antes de qualquer vínculo.

### 4.8 Navegação do perfil protegido

A apresentação protegida aparecia com `Explorar` marcado como item ativo, apesar de ter origem exclusiva por convite e não ser encontrável.

Reformulação:

- nenhum item global aparece ativo;
- retorno principal é `Voltar ao convite`;
- saída foi renomeada para `Fechar apresentação`;
- a superfície não é representada como descoberta pública.

## 5. Resultado por estado

### 5.1 Entrada aberta

Validado porque:

- origem orgânica e retorno estão identificados;
- `Acompanhar` e `Participar` permanecem independentes;
- participação exige confirmação posterior;
- regras, contagem, responsável e relação institucional são visíveis;
- reputação apresenta total, período e denominadores por dimensão;
- canais públicos não sugerem acesso privado.

### 5.2 Aprovação

Validado porque:

- aprovação necessária aparece antes da ação;
- critérios, dados, responsável e prazo estimado são compreensíveis;
- somente dados revisados serão enviados no fluxo futuro;
- envio não cria vínculo;
- amostra insuficiente é apresentada sem nota implícita;
- Organização apoiadora não recebe solicitações automaticamente.

### 5.3 Entradas indisponíveis

Validado porque:

- motivo, revisão estimada e ausência de garantia estão explícitos;
- acompanhar não cria fila ou prioridade;
- anunciante e responsável operacional estão separados;
- a origem comercial oferece explicação;
- reputação permanece contextual e independente do fechamento;
- publicidade não compra qualidade ou recomendação.

### 5.4 Apresentação protegida

Validado porque:

- remetente, autoridade e motivo do convite aparecem antes da ação;
- identidade, território, contagem, responsáveis e atividades podem ser ocultados;
- compartilhamento externo e contato privado permanecem bloqueados;
- reputação pública pode ser suprimida por proteção;
- aceitar inicia revisão, não participação automática;
- a navegação não representa o perfil como resultado de Explorar.

## 6. Continuidade validada

### 6.1 Origem orgânica

```text
resultado de busca
→ Perfil Público
→ Ver origem ou Compartilhar perfil
→ voltar aos resultados
```

Busca, região e posição deverão ser preservadas.

### 6.2 Origem patrocinada

```text
resultado patrocinado identificado
→ Perfil Público
→ Por que este anúncio?
→ voltar ao perfil e aos resultados
```

A natureza comercial permanece visível antes do conteúdo e não altera a hierarquia orgânica.

### 6.3 Convite protegido

```text
convite autorizado
→ apresentação protegida
→ revisar remetente, autoridade, motivo e condições
→ aceitar revisão, recusar ou denunciar
→ voltar ao convite
```

O acesso não poderá ser transformado em resultado de busca ou perfil compartilhável.

## 7. Cobertura após validação

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Opportunity Boost | 46 | 36 | 10 |

A cobertura das famílias permanece separada. A UXA-063 não valida retrospectivamente o Opportunity Boost.

## 8. Decisões preservadas

Continuam vigentes:

- acompanhar não é participar;
- compartilhar não é recomendar;
- publicidade não é recomendação;
- contagem não é reputação;
- responsável operacional não é automaticamente anunciante ou apoiador;
- amostra insuficiente não é nota zero;
- proteção não é irregularidade;
- convite não cria participação;
- visualização não compartilha identidade;
- canal público não concede contato privado;
- avaliação, denúncia e recomendação permanecem objetos distintos.

## 9. Limites

Não são iniciados:

- Solicitação de Participação;
- confirmação de entrada aberta;
- solicitação mediante aprovação;
- revisão especializada de convite;
- Solicitação Pendente;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante;
- gestão do responsável;
- reputação detalhada;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 10. Critérios de saída

A família está funcionalmente validada porque:

- os quatro estados possuem decisão principal coerente;
- a exposição é proporcional ao risco;
- as origens permanecem distinguíveis;
- a autoridade é identificada sem propagação automática;
- reputação possui contexto suficiente ou supressão explícita;
- nenhum estado ativa vínculo ou contato indevido;
- a próxima superfície pode receber contexto sem reinterpretar o Perfil Público.

## 11. Próxima transição recomendada

**UXA-064 — Wireframes Móveis da Revisão e Solicitação de Participação em Coletivos.**

Escopo recomendado:

- revisão de entrada aberta antes da confirmação;
- revisão de solicitação mediante aprovação;
- revisão especializada de convite protegido;
- significado do vínculo;
- regras materiais;
- dados e permissões;
- confirmações inicialmente vazias;
- cancelamento anterior ao envio;
- resultado imediato de entrada aberta ou envio para análise.

A UXA-064 dependerá de autorização separada.
