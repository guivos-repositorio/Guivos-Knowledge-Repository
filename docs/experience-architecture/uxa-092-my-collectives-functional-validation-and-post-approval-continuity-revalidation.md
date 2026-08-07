---
id: UXA-092
title: Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-056
  - UXA-059
  - UXA-066
  - UXA-067
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-SURF-PER-107
  - GKR-TRN-108
  - GKR-TRN-110
  - GKR-JOURNEY-GAPS-001
  - M7.79
normative: false
---

# Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação

## 1. Finalidade

A UXA-092 valida funcionalmente a referência móvel de `GKR-SURF-PER-106 — Meus Coletivos`, revalida o estado aprovado corrente da família `GKR-SURF-PER-105 — Solicitação Pendente` e reexamina `GKR-TRN-108` como uma única continuidade pós-aprovação.

A frente responde:

> **A aprovação forma o vínculo de maneira inequívoca antes de qualquer navegação, e a Pessoa consegue reconhecer esse vínculo em Meus Coletivos sem confundir participação com solicitação, convite, acompanhamento, obrigação, ranking ou uma Central de Atualizações ainda ausente?**

## 2. Autoridades utilizadas

- UXA-056 — contrato funcional de descoberta, participação e `Meus Coletivos`;
- UXA-059 — programa P0A/P0B e regra de família funcional;
- UXA-066/067 — estados da solicitação na perspectiva da Pessoa;
- UXA-088/089 — decisão na perspectiva do responsável;
- UXA-090 — contrato integrado de identidade, estado canônico, autoridade, concorrência e efeito lógico único;
- UXA-091 — materialização de `PER-106` e refinamento inicial de `TRN-108`;
- registros de superfícies, transições, lacunas, jornadas, catálogo, galeria e rastreabilidade.

## 3. Gate funcional

O conjunto foi examinado em:

1. distinção entre participação, acompanhamento, solicitação, convite e pausa;
2. vínculo criado pela decisão autorizada, e não pelo clique de navegação;
3. continuidade opcional após o resultado aprovado;
4. preservação de preferências e ausência de função, autoridade ou notificação automática;
5. ausência de ranking, pontuação de dedicação, comparação ou sequência obrigatória;
6. minimização de dados e ausência de conteúdo protegido da Jornada pessoal;
7. não antecipação de `PER-107 — Central de Atualizações` ou `PER-108 — Início do Participante`;
8. correspondência do mesmo vínculo entre `COL-003`, resultado aprovado em `PER-105` e `PER-106`;
9. tolerância a repetição sem duplicar vínculo lógico;
10. possibilidade de não abrir `Meus Coletivos` imediatamente sem desfazer a aprovação.

Falha material em estado, autoridade, vínculo, voluntariedade ou fronteira com superfícies ausentes impede aprovação.

## 4. Diagnóstico da materialização UXA-091

A referência materializada não era aprovável sem ajuste por três razões:

1. `Meus Coletivos` dizia **“Todos os seus vínculos”** enquanto agrupava também solicitações e convites, que ainda não são vínculos confirmados;
2. a superfície utilizava referências a atualização/comunicado e contagem de não lidos que poderiam antecipar a responsabilidade própria de `PER-107`;
3. o estado aprovado de `PER-105` oferecia **“Salvar decisão”**, expressão ambígua porque a decisão e o vínculo já estavam registrados antes de qualquer ação da Pessoa.

Nenhum problema exigiu novo ID, nova superfície ou novo SVG.

## 5. Reformulação controlada

Foram reformulados somente os dois SVGs já existentes no escopo:

- `uxa-066-collective-pending-request-approved-mobile.svg`;
- `uxa-091-my-collectives-mobile.svg`.

Ajustes principais:

- `PER-105` explicita que a aprovação já está registrada e que abrir `Meus Coletivos` é opcional;
- a ação secundária `Salvar decisão` foi substituída por `Agora não`;
- `PER-106` passa a falar em **participações e estados relacionados**, não em vínculos indiscriminados;
- referências de atualização foram limitadas a informação pública disponível no próprio Coletivo;
- `PER-106` declara que não cria contagem de não lidos nem substitui a futura Central de Atualizações;
- solicitações, convites, acompanhamento e pausas permanecem categorias independentes.

## 6. Validação do estado aprovado de `PER-105`

**Resultado: validado após reformulação controlada.**

A versão corrente é aprovada porque:

- a autoridade e o fundamento permanecem identificados;
- o vínculo é declarado como criado antes da navegação;
- preferências de lista nominal e notificações continuam preservadas;
- nenhuma função, moderação, autoridade ou presença é atribuída pela aprovação;
- `Ver em Meus Coletivos` é uma continuidade opcional;
- `Agora não` deixa explícito que não navegar não cancela nem invalida a decisão;
- a superfície não promete `PER-107` ou `PER-108` como se já estivessem disponíveis.

A família `PER-105` volta a possuir validação funcional vigente em seus oito SVGs atuais.

## 7. Validação de `GKR-SURF-PER-106 — Meus Coletivos`

**Resultado: validada após reformulação controlada.**

A referência principal é suficiente no escopo P0A porque:

- distingue `Participando`, `Acompanhando`, `Solicitações`, `Convites` e `Pausadas`;
- não transforma essas categorias em etapas de progressão;
- apresenta o vínculo recém-aprovado como participante confirmado;
- não atribui função, autoridade, notificação ou presença obrigatória;
- não usa ranking, pontuação de dedicação ou comparação;
- permite informação pública mínima sem simular uma central de atualizações;
- mantém `PER-107` e `PER-108` como superfícies separadas;
- não exige os estados P0B de vazio, excesso de volume, falha de sincronização ou pausa detalhada para validar a responsabilidade principal P0A.

Os estados P0B continuam dívidas próprias de evolução e não invalidam a referência principal.

## 8. Revalidação de `GKR-TRN-108`

```text
COL-003 — aprovação confirmada por autoridade vigente
→ resultado aprovado observável em PER-105
→ vínculo já formado
→ escolha opcional “Ver em Meus Coletivos”
→ PER-106 — mesmo vínculo confirmado visível
```

**Resultado: integralmente validada.**

A ligação é promovível porque:

- a decisão autorizada e o estado canônico já são validados na origem;
- o resultado aprovado corrente de `PER-105` foi revalidado;
- `PER-106` foi validada;
- o mesmo vínculo atravessa a continuidade sem criar novo vínculo silencioso;
- o clique não é gate para a formação do vínculo;
- optar por `Agora não` apenas interrompe a navegação;
- repetição de abertura não pode duplicar participação;
- nenhuma função, reputação, notificação ou autoridade é criada no handoff;
- `PER-107` e `PER-108` não são necessários para completar esta ligação específica.

A classificação documental de `GKR-TRN-108` passa de `parcial` para **`integralmente validada`**.

## 9. Estado de `GKR-TRN-110`

`GKR-TRN-110 — Meus Coletivos → Central de Atualizações` permanece **`parcial`**.

A validação de `PER-106` resolve apenas a origem. `GKR-SURF-PER-107` continua ausente, portanto não há base para validar destino, efeito, retorno ou continuidade ponta a ponta.

A UXA-092 não materializa nem simula `PER-107`.

## 10. Resultado quantitativo

Após eventual integração:

- SVGs: 106;
- associações individuais: 106;
- perfis de rastreabilidade: 26;
- validações funcionais vigentes: **96**;
- pendentes de validação específica: **10**, exclusivamente os estados residuais da UXA-055;
- IDs granulares com referência visual: 28 de 40;
- responsabilidades sem SVG dedicado: 11;
- superfícies registradas: 40;
- transições registradas: 37;
- handoffs integralmente validados no fluxo de solicitação: **6**.

Nenhum SVG é criado ou removido pela UXA-092.

## 11. Efeito sobre maturidade

Após eventual integração:

- `GKR-SURF-PER-105` volta a `validado` sem ressalva de estado reformulado pendente;
- `GKR-SURF-PER-106` passa de `materializado` para `validado`;
- `GKR-TRN-108` passa de `parcial` para `integralmente validada`;
- `GKR-TRN-110` permanece `parcial`;
- `GKR-SURF-PER-107` continua ausente;
- `GKR-SURF-PER-108` continua com reformulação pendente;
- Jornadas da Pessoa e do Coletivo permanecem `draft`.

## 12. Limites

A UXA-092 não:

- materializa estados P0B adicionais de `Meus Coletivos`;
- materializa `PER-107` ou `PER-108`;
- valida `TRN-110`;
- cria novo SVG, superfície, transição ou ID;
- define API, banco, sincronização, notificações ou persistência;
- promove a Jornada da Pessoa ou do Coletivo;
- altera Resultados Empresariais;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-093.

## 13. Veredito

**Aprovada após reformulação controlada no escopo da superfície e da continuidade.**

`PER-106`, o estado aprovado corrente de `PER-105` e `TRN-108` possuem evidência funcional suficiente no escopo documental atual. A dívida seguinte permanece separada em `PER-107`/`TRN-110` e nos estados P0B ainda não materializados.

## 14. Próxima transição possível

Após eventual integração e autorização separada:

> **UXA-093 — Materialização Controlada da Central de Atualizações (`GKR-SURF-PER-107`).**

A UXA-093 não é iniciada por esta validação.
