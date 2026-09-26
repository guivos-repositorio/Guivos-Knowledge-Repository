---
id: GKR-UX-PUBLISHER-APPLICATION-CONTRACT-001
title: Jornada de Organizações e Coletivos — Manifestação de Interesse e Inscrição em Oportunidades — Contrato Conceitual Bilateral
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-PER203-MASTER-001
  - GKR-UX-ORG-ACTIVE-OPPORTUNITY-MASTER-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Jornada de Organizações e Coletivos — Manifestação de Interesse e Inscrição em Oportunidades — Contrato Conceitual Bilateral

## 1. Finalidade

Este contrato define a semântica candidata para uma capacidade bilateral futura em que uma Pessoa possa manifestar interesse ou realizar uma inscrição em uma oportunidade dentro da Guivos e o publicador legítimo possa receber e administrar somente o recorte autorizado desse objeto.

O contrato existe antes de qualquer decisão de superfície, transição ou implementação.

```text
CAPACIDADE BILATERAL
≠ NOVA SUPERFÍCIE AUTOMÁTICA

OBJETO COMPARTILHADO
≠ JOURNEY COMPARTILHADA

INSCRIÇÃO INTERNA
≠ BND-001
```

## 2. Escopo

O publicador pode ser uma Organização ou um Coletivo somente quando a oportunidade e a autoridade aplicáveis sustentarem essa relação.

Este contrato não presume que toda oportunidade aceite inscrição interna. Uma oportunidade pode continuar usando `BND-001` e processo externo.

## 3. Modos de continuidade

### 3.1 Continuidade externa

```text
PER-203
→ REVISÃO CONSCIENTE
→ TRN-205
→ BND-001
→ AUTORIDADE EXTERNA
```

Depois de `BND-001`, a Guivos não presume inscrição, candidatura, compra, reserva, aprovação ou resultado.

### 3.2 Continuidade interna candidata

Quando houver autoridade própria:

```text
PESSOA
→ OPORTUNIDADE
→ AÇÃO CONSCIENTE DE MANIFESTAR INTERESSE OU INSCREVER-SE
→ COMPREENSÃO DE FINALIDADE E DADOS
→ AUTORIZAÇÃO / ENVIO
→ OBJETO BILATERAL
→ ESTADO ACOMPANHÁVEL

PUBLICADOR
→ RECEBE O MESMO OBJETO NO RECORTE AUTORIZADO
→ ANALISA / ADMINISTRA CONFORME AUTORIDADE
→ ATUALIZA ESTADO LEGÍTIMO
→ DEVOLVE CONTINUIDADE À PESSOA QUANDO APLICÁVEL
```

Esta sequência é conceitual. Ela não cria `GKR-SURF-*` nem `GKR-TRN-*`.

## 4. Objetos distintos

Devem permanecer semanticamente separados:

```text
VISUALIZAÇÃO
≠ SALVAMENTO
≠ MANIFESTAÇÃO DE INTERESSE
≠ INSCRIÇÃO
≠ ELEGIBILIDADE
≠ SELEÇÃO
≠ PARTICIPAÇÃO
≠ RESULTADO
```

Manifestação de interesse pode ser uma intenção leve e reversível quando legitimamente oferecida. Inscrição representa submissão consciente de um conjunto definido de informações para uma finalidade identificada.

Nenhum dos dois estados deve ser inferido apenas por navegação, tempo de permanência, clique exploratório, salvamento ou explicação de relevância.

## 5. Objeto bilateral mínimo

Quando uma inscrição interna existir, o objeto lógico pode conter somente o necessário e autorizado para sua finalidade, como classes conceituais:

- identidade ou referência necessária da Pessoa;
- oportunidade correspondente;
- publicador responsável;
- tipo de manifestação;
- informações fornecidas conscientemente para a inscrição;
- declarações ou respostas exigidas legitimamente;
- autorizações aplicáveis;
- estado corrente;
- data/hora material quando necessária;
- proveniência das informações;
- alterações materiais;
- solicitações de informação;
- decisão do publicador quando sua autoridade permitir;
- retirada/cancelamento pela Pessoa quando aplicável;
- evidência mínima de processamento e confirmação.

Este contrato não define formulário, campos obrigatórios universais, documentos, critérios seletivos ou prazo padrão.

## 6. Dados que não atravessam por padrão

O publicador não recebe automaticamente:

- Journey completa;
- objetivos pessoais não necessários;
- Próximos Passos privados;
- histórico pessoal amplo;
- inferências da Guivos;
- razões internas de recomendação;
- perfil psicológico;
- informações sensíveis sem finalidade e autoridade adequadas;
- outras relações da Pessoa;
- oportunidades salvas ou comparadas;
- comportamento de navegação não necessário;
- score, ranking ou reputação algorítmica da Pessoa.

```text
DADO DISPONÍVEL À GUIVOS
≠ DADO NECESSÁRIO AO PUBLICADOR
≠ DADO AUTORIZADO PARA COMPARTILHAMENTO
```

## 7. Relevância

A Guivos pode explicar à Pessoa por que uma oportunidade parece pertinente usando contexto autorizado conforme as autoridades da Journey.

Essa explicação não é automaticamente revelável ao publicador.

```text
RELEVÂNCIA PARA A PESSOA
≠ SCORE DO CANDIDATO

MATCH
≠ RANKING

CONTEXTO AUTORIZADO PARA PERSONALIZAÇÃO
≠ CONTEXTO AUTORIZADO PARA O PUBLICADOR
```

Se uma futura capacidade institucional de adequação ou triagem existir, deverá possuir finalidade, dados, explicabilidade, contestação e autoridade próprias. Este contrato não a cria.

## 8. Autoridade e consentimento

Antes de envio material, a Pessoa deve compreender, quando aplicável:

1. qual oportunidade está envolvida;
2. quem é o publicador/responsável;
3. qual ação está realizando;
4. quais informações serão compartilhadas;
5. para qual finalidade;
6. quais condições materiais se aplicam;
7. quais informações são obrigatórias ou opcionais;
8. como corrigir ou retirar quando permitido;
9. quais efeitos não são garantidos.

```text
AUTENTICAÇÃO
≠ CONSENTIMENTO

CONSENTIMENTO
≠ AUTORIDADE IRRESTRITA

INSCRIÇÃO
≠ CONSENTIMENTO PARA MARKETING

INSCRIÇÃO
≠ AUTORIZAÇÃO PARA ACESSAR A JOURNEY
```

Ausência de ação, silêncio ou navegação não equivalem a autorização.

## 9. Estados conceituais candidatos

Sem criar State Map paralelo, uma futura autoridade poderá precisar distinguir, conforme o caso:

- intenção não enviada;
- revisão antes do envio;
- envio em processamento;
- enviada e confirmada;
- recebida pelo publicador;
- informação adicional solicitada;
- aguardando ação da Pessoa;
- em análise;
- decisão pendente;
- aceita/selecionada quando a decisão pertencer ao publicador;
- não selecionada/recusada quando aplicável;
- retirada pela Pessoa;
- cancelada pelo publicador com fundamento aplicável;
- expirada;
- bloqueada por proteção, privacidade ou autoridade;
- falha recuperável;
- estado indeterminado;
- contestada;
- encerrada.

A lista é conceitual e deverá ser adjudicada contra cada tipo real de oportunidade antes de materialização.

## 10. Autoridade do publicador

Receber uma inscrição pode permitir ao publicador, conforme autoridade específica:

- consultar o objeto de inscrição;
- verificar informações legitimamente fornecidas;
- solicitar informação adicional necessária;
- registrar estado operacional;
- realizar decisão que efetivamente lhe pertença;
- comunicar continuidade material;
- corrigir informação institucional;
- encerrar processamento quando houver fundamento.

Não permite automaticamente:

- acessar contexto pessoal amplo;
- alterar dados pessoais declarados pela Pessoa;
- inferir atributos sensíveis;
- classificar valor humano;
- ranquear candidatos por critério oculto;
- usar dados para finalidade incompatível;
- transferir dados a outra parte sem fundamento;
- transformar inscrição em vínculo permanente;
- presumir participação, contratação ou resultado.

## 11. Pessoa — controles mínimos

Quando aplicável, a Pessoa deve poder:

- revisar antes de enviar;
- corrigir informação própria;
- cancelar antes do envio;
- acompanhar estado material;
- responder a solicitação legítima de informação;
- retirar a manifestação/inscrição quando permitido;
- compreender quando retirada não elimina obrigação ou retenção legítima já existente;
- contestar informação ou decisão quando houver canal/autoridade aplicável;
- retornar à oportunidade.

Retirada não deve ser convertida em punição algorítmica ou perda artificial de acesso a outras oportunidades.

## 12. Organização

Para Organização, `ORG-002` e `ORG-003` permanecem responsáveis pelo cadastro e pelo estado da oportunidade, não pela gestão de Pessoas inscritas.

Este contrato reconhece como lacuna a responsabilidade de receber/administrar inscrições internas de uma oportunidade institucional. Ele não amplia `ORG-003` por conveniência e não cria novo `ORG-ID`.

## 13. Coletivo

`COL-003` governa solicitação de participação no Coletivo e `COL-004` governa participantes e vínculos. Esses objetos não equivalem automaticamente a inscrição em uma atividade ou oportunidade publicada pelo Coletivo.

`COL-006` é a responsabilidade corrente de atividades e oportunidades, mas este contrato não presume que ela já governe o ciclo bilateral de inscrição. Essa relação deverá ser adjudicada antes de materialização.

## 14. Planos e capacidade comercial

Planos podem governar capacidade operacional, volume, histórico, analytics, exportação ou outras capacidades quando houver autoridade comercial e funcional suficiente.

Planos não ampliam por si só:

- finalidade;
- consentimento;
- autoridade sobre a Pessoa;
- acesso a contexto privado;
- legitimidade de tratamento;
- relevância orgânica;
- chance de seleção.

```text
PLANO SUPERIOR
≠ MAIS DIREITO SOBRE DADOS PESSOAIS

DASHBOARD
≠ ACESSO IRRESTRITO A DADOS

EXPORTAÇÃO
≠ EXPORTAÇÃO DE QUALQUER INFORMAÇÃO
```

Os entitlements específicos de visualização individual permanecem lacuna até contrato próprio.

## 15. Analytics, visualizações e agregados

O publicador pode futuramente receber visualizações operacionais ou analíticas sustentadas por finalidade e autoridade.

Devem permanecer distinguíveis:

- dado individual necessário à operação;
- dado agregado;
- indicador;
- evidência;
- inferência;
- informação indisponível ou protegida.

Este contrato não define KPI, gráfico, dashboard, threshold, score ou fórmula.

## 16. Proteção, minimização e retenção

A implementação futura deverá aplicar:

- minimização por finalidade;
- acesso proporcional ao papel;
- proteção de informação sensível;
- proveniência;
- correção;
- retenção limitada ao fundamento aplicável;
- revogação/retirada quando cabível;
- trilha suficiente para atos materiais;
- proteção contra uso secundário incompatível;
- não retaliação por exercício legítimo de controle.

Encerramento da inscrição não implica exclusão automática de toda informação quando existir obrigação legítima de retenção. Retenção legítima também não autoriza reutilização irrestrita.

## 17. Falha, concorrência e confirmação

```text
INTENÇÃO
≠ ENVIO

ENVIO
≠ RECEBIMENTO CONFIRMADO

RECEBIMENTO
≠ ANÁLISE

ANÁLISE
≠ DECISÃO

DECISÃO
≠ PARTICIPAÇÃO

PARTICIPAÇÃO
≠ RESULTADO
```

Repetição após falha não deve criar inscrições duplicadas silenciosamente.

Quando o estado não puder ser confirmado, a experiência deve preservar estado indeterminado em vez de fabricar sucesso ou falha.

## 18. Acessibilidade e linguagem

A compreensão de dados compartilhados, finalidade, estado, decisão e controles não pode depender exclusivamente de cor, posição, ícone, animação ou linguagem técnica.

Linguagem deve evitar pressão, urgência artificial, promessa de seleção e julgamento de valor da Pessoa.

## 19. IA — source lock

IA pode apoiar materialização somente dentro deste contrato e das autoridades superiores.

Ela não pode inventar:

- campos;
- critérios seletivos;
- score;
- ranking;
- automação decisória;
- motivos de recusa;
- dados adicionais;
- consentimentos;
- notificações;
- integrações;
- entitlements;
- novas superfícies ou transições.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 20. Critérios para futura adjudicação de superfície

Antes de criar ou expandir qualquer superfície, a frente deverá provar:

1. qual job não cabe nas responsabilidades existentes;
2. quem inicia a ação;
3. qual objeto lógico é compartilhado;
4. quais dados atravessam e por quê;
5. quem pode decidir cada estado;
6. como a Pessoa acompanha e controla o objeto;
7. como o publicador administra sem absorver a Journey;
8. quais estados exigem continuidade própria;
9. quais diferenças existem entre Organização e Coletivo;
10. quando o processo permanece externo em `BND-001`;
11. quais planos alteram capacidade sem alterar autoridade;
12. quais gaps permanecem sem ID.

## 21. Lacunas preservadas

Permanecem deliberadamente não definidos:

- Surface ID da perspectiva da Pessoa para inscrição interna;
- Surface ID da perspectiva da Organização para gestão de inscrições;
- eventual responsabilidade específica do Coletivo para inscrições em atividades/oportunidades;
- Transition IDs;
- formulário universal;
- campos obrigatórios;
- critérios de seleção;
- automação de decisão;
- score/ranking;
- notificações;
- integrações;
- retenção quantitativa;
- regras específicas por jurisdição;
- entitlements de visualização por plano;
- analytics/KPIs;
- protótipo;
- implementação.

## 22. Estado

```text
CONTRATO CONCEITUAL BILATERAL
→ CANDIDATO

NOVOS SURFACE IDs
→ NONE

NOVOS TRANSITION IDs
→ NONE

BND-001
→ PRESERVADO

ORG-003
→ NÃO EXPANDIDO PARA GESTÃO DE INSCRITOS

COL-003 / COL-004
→ NÃO RECLASSIFICADOS COMO INSCRIÇÃO EM OPORTUNIDADE

VISUAL BASELINE
→ NONE

PROTOTYPE
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ NOT RELEASED
```
