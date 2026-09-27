---
id: GKR-UX-ORG-OPPORTUNITY-APPLICATIONS-CONTRACT-001
title: Jornada de Organizações e Coletivos — Organização — Manifestações de Interesse e Inscrições em Oportunidades — Contrato Funcional Candidato
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-PUBLISHER-APPLICATION-CONTRACT-001
  - GKR-UX-ORG-ACTIVE-OPPORTUNITY-MASTER-001
  - GKR-UX-PERSON-INTERNAL-OPPORTUNITY-APPLICATION-CONTRACT-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Organização — Manifestações de Interesse e Inscrições em Oportunidades — Contrato Funcional Candidato

## 1. Finalidade

Este contrato define a responsabilidade funcional candidata da Organização para **receber e administrar o recorte autorizado de manifestações de interesse e inscrições internas** vinculadas a oportunidades publicadas sob sua autoridade.

A responsabilidade possui identidade de superfície adjudicada como `GKR-SURF-ORG-008`. Este contrato ainda não adjudica nenhuma nova transição.

```text
CONTRATO FUNCIONAL
→ GKR-SURF-ORG-008 ADJUDICADA

RECEBER OBJETO BILATERAL
≠ ACESSAR JOURNEY DA PESSOA

PUBLICAR OPORTUNIDADE
≠ GERENCIAR INSCRITOS
```

`GKR-SURF-ORG-008` identifica esta responsabilidade própria. Nenhum novo `GKR-TRN-*` é criado por este contrato.

## 2. Fronteira com ORG-002 e ORG-003

`ORG-002` continua responsável por cadastro, revisão e envio institucional da oportunidade.

`ORG-003` continua responsável pelo estado aprovado/ativo, correção, pausa e encerramento da oportunidade e por sua elegibilidade para descoberta.

A nova responsabilidade candidata começa somente quando existe um **objeto bilateral interno legitimamente enviado pela Pessoa**.

```text
ORG-002
→ CADASTRA A OPORTUNIDADE

ORG-003
→ GOVERNA A OPORTUNIDADE ATIVA

OBJETO BILATERAL RECEBIDO
→ RESPONSABILIDADE CANDIDATA DE MANIFESTAÇÕES / INSCRIÇÕES
```

Não se deve ampliar `ORG-003` para gestão de Pessoas por conveniência.

## 3. Relação com a perspectiva da Pessoa

A perspectiva da Pessoa permanece separada.

```text
PER-203
→ TRN-212
→ PER-204
→ AÇÃO CONSCIENTE / ENVIO LEGÍTIMO
→ OBJETO BILATERAL

ORGANIZAÇÃO
→ RECEBE SOMENTE O RECORTE AUTORIZADO DO MESMO OBJETO
```

A Organização não recebe a Journey, o contexto privado usado para personalização nem as razões internas de relevância.

A continuidade bilateral `PER-204 → ORG-008` está formalizada por `GKR-TRN-213`, contratada para o envio consciente e recebimento do mesmo objeto no recorte autorizado. A continuidade institucional `ORG-003 → ORG-008` está formalizada separadamente por `GKR-TRN-214`, sem criar ou receber objeto por si só.

## 4. Dois objetos operacionais distintos

### 4.1 Manifestação de interesse

A Organização pode, quando a oportunidade sustentar esse modo:

- reconhecer a manifestação consciente;
- identificar a oportunidade correspondente;
- identificar a referência necessária da Pessoa;
- compreender o estado corrente da manifestação;
- registrar processamento operacional legítimo;
- respeitar retirada quando aplicável.

Manifestação de interesse:

```text
≠ INSCRIÇÃO
≠ CANDIDATURA
≠ ELEGIBILIDADE
≠ SELEÇÃO
≠ PARTICIPAÇÃO
```

Ela não autoriza solicitar automaticamente dados adicionais nem reutilizar campos, critérios ou estados de inscrição.

### 4.2 Inscrição

Quando houver inscrição interna legítima, a Organização pode receber somente o conjunto conscientemente enviado e necessário à finalidade identificada.

Pode administrar, conforme autoridade real:

- recebimento;
- validação operacional;
- informação legitimamente necessária;
- solicitação de complemento;
- estado de análise;
- decisão que efetivamente pertença à Organização;
- comunicação material;
- encerramento;
- retirada/cancelamento quando aplicável.

Inscrição não equivale a elegibilidade confirmada, seleção, contratação, participação ou resultado.

## 5. Job próprio

A Pessoa autorizada atuando pela Organização deve conseguir:

1. compreender em qual Organização e oportunidade está atuando;
2. distinguir manifestação de interesse de inscrição;
3. consultar somente objetos que sua autoridade permite;
4. compreender estado, proveniência e momento material;
5. identificar informação ausente sem inferi-la;
6. solicitar complemento somente quando necessário e legítimo;
7. registrar estado operacional sem fabricar decisão;
8. realizar decisão somente quando ela pertencer à Organização;
9. comunicar continuidade material à Pessoa quando aplicável;
10. corrigir informação institucional sem alterar declaração da Pessoa;
11. respeitar retirada, contestação, retenção e encerramento;
12. retornar ao contexto da oportunidade sem misturar gestão da oportunidade com gestão de inscrições.

Esse job persiste além de `ORG-003` e possui objeto, estados e autoridade próprios.

## 6. Dados visíveis à Organização

O contrato admite, quando necessários e autorizados:

- identidade ou referência mínima da Pessoa;
- oportunidade correspondente;
- tipo do objeto: manifestação ou inscrição;
- informações fornecidas conscientemente para aquela finalidade;
- declarações/respostas legitimamente requeridas;
- proveniência;
- estado corrente;
- datas/horas materiais quando necessárias;
- alterações materiais;
- solicitações legítimas de informação;
- decisão institucional quando aplicável;
- retirada/cancelamento;
- evidência mínima de processamento e confirmação.

```text
DADO EXISTENTE NA GUIVOS
≠ DADO VISÍVEL À ORGANIZAÇÃO

DADO DA JOURNEY
≠ DADO DA INSCRIÇÃO

DADO NECESSÁRIO
≠ DADO DESEJÁVEL POR CONVENIÊNCIA
```

## 7. Dados não visíveis por padrão

A Organização não recebe automaticamente:

- Journey completa;
- objetivos privados;
- Próximos Passos;
- histórico pessoal amplo;
- outras oportunidades salvas ou comparadas;
- comportamento de navegação não necessário;
- razões internas de recomendação;
- inferências da Guivos;
- perfil psicológico;
- dados sensíveis sem fundamento;
- outras relações da Pessoa;
- score, ranking ou reputação algorítmica;
- contexto usado exclusivamente para personalização da Pessoa.

## 8. Relevância, elegibilidade e seleção

Devem permanecer separados:

```text
RELEVÂNCIA PARA A PESSOA
≠ ELEGIBILIDADE

ELEGIBILIDADE
≠ SELEÇÃO

MATCH
≠ SCORE DO CANDIDATO

VOLUME DE INTERESSE
≠ QUALIDADE DA PESSOA

PLANO PAGO
≠ PRIORIDADE HUMANA
```

A Organização não recebe automaticamente a explicação privada de por que a Guivos apresentou a oportunidade à Pessoa.

Critérios seletivos, score, ranking, automação decisória ou recomendação institucional exigem autoridade própria e não são criados aqui.

## 9. Autoridade institucional

A experiência deve distinguir:

```text
ACESSAR
≠ CONSULTAR DADOS INDIVIDUAIS

CONSULTAR
≠ SOLICITAR COMPLEMENTO

SOLICITAR
≠ DECIDIR

DECIDIR
≠ REPRESENTAR AUTORIDADE IRRESTRITA
```

A autoridade deve ser revalidada quando houver mudança de Organização, oportunidade, papel, contexto ou ato material.

Quando a autoridade for insuficiente, o sistema deve bloquear somente o ato não autorizado e preservar o que puder ser legitimamente consultado ou retomado.

## 10. Estados funcionais candidatos

Sem criar State Map paralelo, a responsabilidade pode precisar distinguir conforme o objeto real:

- nenhuma manifestação/inscrição;
- recebida;
- confirmação pendente;
- informação adicional necessária;
- aguardando Pessoa;
- em análise;
- decisão pendente;
- aceita/selecionada quando aplicável;
- não selecionada/recusada quando aplicável;
- retirada pela Pessoa;
- cancelada pela Organização com fundamento;
- oportunidade alterada materialmente;
- oportunidade pausada/encerrada;
- expirada;
- bloqueada por autoridade, proteção ou privacidade;
- contestada;
- falha recuperável;
- estado indeterminado;
- encerrada.

Manifestação de interesse não herda automaticamente estados seletivos da inscrição.

## 11. Ações e controles

Quando autorizada, a Organização pode precisar:

- abrir o objeto;
- consultar dados autorizados;
- filtrar/organizar por estados operacionais legítimos;
- solicitar complemento necessário;
- registrar mudança de estado;
- tomar decisão pertencente à Organização;
- corrigir informação institucional;
- responder contestação;
- encerrar processamento;
- retornar à oportunidade;
- consultar trilha material quando necessária e permitida.

Este contrato não define busca, filtros, ordenação, bulk actions, colunas, dashboard, KPI ou layout final.

## 12. Alteração material da oportunidade

Se a oportunidade for alterada depois de manifestações/inscrições:

- o efeito sobre objetos existentes deve ser explicitamente adjudicado;
- não se presume que consentimento anterior cubra finalidade ou condição material nova;
- Pessoas afetadas devem receber continuidade proporcional quando aplicável;
- a Organização não pode reescrever retroativamente o que a Pessoa enviou;
- estado indeterminado deve ser usado quando o efeito ainda não estiver confirmado.

```text
ALTERAR OPORTUNIDADE
≠ ALTERAR INSCRIÇÃO DA PESSOA

NOVA CONDIÇÃO MATERIAL
≠ CONSENTIMENTO ANTERIOR AUTOMATICAMENTE SUFICIENTE
```

## 13. Retirada, cancelamento e encerramento

```text
RETIRADA DA PESSOA
≠ RECUSA DA ORGANIZAÇÃO

CANCELAMENTO DA OPORTUNIDADE
≠ RECUSA INDIVIDUAL

ENCERRAMENTO DA INSCRIÇÃO
≠ EXCLUSÃO AUTOMÁTICA DE TODO DADO
```

Retenção legítima deve ser limitada ao fundamento aplicável e não autoriza uso secundário incompatível.

Retirada não pode produzir punição algorítmica ou perda artificial de acesso a outras oportunidades.

## 14. Falha, concorrência e idempotência

A responsabilidade deve tratar:

- recebimento sem confirmação suficiente;
- retry;
- duplicidade;
- atualização concorrente;
- decisão conflitante;
- alteração material durante análise;
- autoridade revogada;
- dependência indisponível;
- objeto protegido;
- estado local divergente do bilateral.

```text
RECEBIDO
≠ ANALISADO

ANALISADO
≠ DECIDIDO

RETRY
≠ NOVO OBJETO AUTOMÁTICO

INTERFACE ATUALIZADA
≠ ESTADO BILATERAL CONFIRMADO
```

## 15. Visualizações e analytics

A Organização pode futuramente receber visualizações operacionais ou analíticas quando houver autoridade funcional e comercial específica.

Devem permanecer separados:

- dado individual necessário;
- agregado;
- indicador;
- evidência;
- inferência;
- informação protegida ou indisponível.

Este contrato não cria:

- dashboard;
- KPI;
- funil;
- taxa de conversão;
- score;
- ranking;
- previsão;
- benchmark;
- fórmula;
- threshold;
- audiência estimada.

## 16. Planos

Planos podem futuramente governar capacidade operacional, volume, histórico, exportação, analytics ou integrações quando isso estiver contratualmente definido.

Planos não ampliam:

- finalidade;
- consentimento;
- acesso a contexto privado;
- autoridade sobre a Pessoa;
- critérios seletivos;
- relevância orgânica;
- chance de seleção;
- prioridade humana.

```text
PLANO SUPERIOR
≠ MAIS DADOS PESSOAIS

EXPORTAÇÃO
≠ DIREITO DE EXPORTAR QUALQUER DADO

ANALYTICS
≠ PERFIL INDIVIDUAL IRRESTRITO
```

## 17. Proteção, minimização e proveniência

Materialização futura deve preservar:

- minimização por finalidade;
- acesso proporcional ao papel;
- proveniência;
- distinção entre declaração da Pessoa e informação institucional;
- proteção de dados sensíveis;
- correção;
- contestação;
- retenção limitada;
- trilha material suficiente;
- não retaliação;
- proteção contra uso secundário incompatível.

A Organização não pode alterar uma declaração da Pessoa como se fosse sua própria fonte.

## 18. Acessibilidade e linguagem

Estado, ação, autoridade, origem dos dados e consequência material devem ser compreensíveis sem depender exclusivamente de cor, posição, ícone ou animação.

A linguagem não deve:

- prometer seleção;
- transformar ausência de dado em inadequação;
- julgar valor humano;
- criar urgência artificial;
- apresentar inferência como fato;
- sugerir que maior atividade institucional concede prioridade sobre Pessoas.

## 19. IA — source lock

IA pode apoiar exploração e materialização somente dentro das autoridades do GKR.

Ela não pode inventar:

- novos ORG-IDs além de `ORG-008`;
- TRN-ID;
- campos;
- documentos obrigatórios;
- critérios seletivos;
- score/ranking;
- decisão automática;
- motivos de recusa;
- dados adicionais;
- finalidade;
- consentimento;
- notificações;
- integrações;
- entitlements;
- dashboard/KPI;
- layout final.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 20. Adjudicação da identidade de superfície

A identidade `GKR-SURF-ORG-008` foi adjudicada porque os critérios cumulativos abaixo estão satisfeitos:

1. job próprio diferente de cadastrar/ativar a oportunidade;
2. objeto bilateral próprio;
3. estados persistentes após recebimento;
4. autoridade institucional própria;
5. consulta e processamento independentes de `ORG-003`;
6. solicitação de complemento/decisão/encerramento pertencentes ao objeto;
7. retorno à oportunidade sem eliminar a responsabilidade;
8. impossibilidade de absorção legítima por superfície existente;
9. diferenças com eventual responsabilidade de Coletivo preservadas;
10. continuidade com `PER-204` suficientemente definida para adjudicar transições.

## 21. Lacunas preservadas

Permanecem deliberadamente não definidos:

- retorno dedicado a partir de `ORG-008`;
- continuidade bilateral de resposta/atualização que exija transição própria;
- campos/documentos por oportunidade;
- critérios de elegibilidade/seleção;
- automação decisória;
- notificações;
- integrações;
- retenção quantitativa;
- regras por jurisdição;
- entitlements por plano;
- analytics/KPIs;
- bulk actions;
- protótipo;
- implementação.

## 22. Estado

```text
RESPONSABILIDADE FUNCIONAL DA ORGANIZAÇÃO
→ CANDIDATA

SURFACE ID
→ GKR-SURF-ORG-008
→ ADJUDICADA

TRANSITION IDs
→ GKR-TRN-213 = PER-204 → ORG-008 / CONTRATADA
→ GKR-TRN-214 = ORG-003 → ORG-008 / CONTRATADA
→ RETORNOS DEDICADOS = NONE

ORG-002
→ PRESERVADO

ORG-003
→ PRESERVADO / NÃO EXPANDIDO PARA GESTÃO DE INSCRITOS

PER-204
→ PERSPECTIVA DA PESSOA PRESERVADA

BND-001
→ PROCESSO EXTERNO PRESERVADO

VISUAL BASELINE
→ NONE

PROTOTYPE
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ NOT RELEASED
```
