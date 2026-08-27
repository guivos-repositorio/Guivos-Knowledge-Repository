---
id: GKR-JOURNEY-COLLECTIVE-001
title: Jornada Integrada do Coletivo
status: draft
version: 0.19.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-26
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001
  - UXA-014
  - UXA-016
  - UXA-018
  - UXA-019
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-066
  - UXA-067
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Jornada Integrada do Coletivo

## 1. Formação, decisão e continuidade da Pessoa

```text
presença pública
→ descoberta
→ solicitação
→ análise responsável
→ aprovação/recusa
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

| Etapa | Maturidade | Evidência | Continuidade |
|---|---|---|---|
| presença pública e descoberta | validado no recorte público | UXA-060/061/062/063; `UXA-016/018` apenas como histórico superseded | parcial entre famílias |
| solicitação | validado | UXA-064/065/066/067 | handoffs bilaterais posteriores validados nos gates |
| referência administrativa do responsável | evidência local do pacote, **não baseline final da UX principal** | UXA-086/087 | contratos especializados preservam maturidade própria; arquitetura principal pendente |
| gestão de solicitações do responsável | validado no fluxo especializado | UXA-088/089/090/092 | handoffs bilaterais governados no escopo próprio |
| aprovação → Meus Coletivos | validado | UXA-090/091/092 | TRN-108 integral |
| Meus Coletivos → Central | validado | UXA-092/093/094/096 | TRN-110 integral |
| Central corrente | **validado** | UXA-094/095/096 | TRN-110 e TRN-111 integrais |
| Início do Participante | **validado no recorte da Pessoa participante** | UXA-095/096 | **TRN-111 integral** |

A reconciliação pós-PR #313/#314 preserva os fluxos independentes acima, mas elimina a inferência de que `UXA-016/018` ou uma referência administrativa local já definam o wireframe principal autenticado final do Coletivo.

## 2. Operação do responsável

```text
representação e autoridade
→ arquitetura principal autenticada ainda a definir
→ gestão de solicitações
→ participantes e vínculos
→ comunicação oficial
→ atividades, consultas e decisões
→ proteção e moderação
→ relações institucionais
```

`COL-003` mantém validação no fluxo especializado de gestão de solicitações. `COL-002` conserva evidência administrativa local e contratos de navegação que tenham autoridade própria, mas **não é tratado como wireframe principal autenticado final**. `COL-004` a `COL-008` permanecem programadas/contratadas ou parcialmente cobertas e não são substituídas pelas superfícies da Pessoa.

```text
MATERIALIZAÇÃO ADMINISTRATIVA LOCAL
≠ ARQUITETURA PRINCIPAL FINAL

FLUXO ESPECIALIZADO VALIDADO
≠ JORNADA DO COLETIVO COMPLETA VALIDADA
```

## 3. Eixo de Domínios de Evolução

A D4 propaga `JED-001..JED-009` para a leitura integrada do Coletivo sem antropomorfizar o participante coletivo.

No Coletivo, um Domínio de Evolução descreve a área à qual uma necessidade, propósito, iniciativa, atividade, experiência ou contribuição coletiva se relaciona.

```text
Coletivo relacionado a JED-001 Saúde e Bem-estar
≠ “o Coletivo está saudável”
```

A leitura integrada pode ser:

```text
Coletivo
→ necessidade ou propósito coletivo
→ domínio(s) relacionado(s)
→ iniciativa/atividade
→ participantes e relações autorizadas
→ execução voluntária
→ evidências coletivas legítimas
→ resultados e aprendizados
```

| ID | Domínio | Exemplos no contexto do Coletivo |
|---|---|---|
| `JED-001` | Saúde e Bem-estar | caminhada comunitária, prevenção, promoção de bem-estar e hábitos saudáveis |
| `JED-002` | Trabalho, Carreira e Estudos | grupo de estudos, capacitação, mentoria e desenvolvimento profissional |
| `JED-003` | Vida Financeira | educação financeira comunitária e apoio à organização econômica dos participantes |
| `JED-004` | Empreendedorismo e Projetos | rede de empreendedores, laboratório de projetos e iniciativa produtiva coletiva |
| `JED-005` | Relacionamentos e Vida Social | pertencimento, convivência, integração, redes de apoio e comunidade |
| `JED-006` | Espiritualidade, Propósito e Valores | comunidade de fé, reflexão, valores compartilhados e propósito coletivo voluntário |
| `JED-007` | Viagens, Lazer, Cultura e Novas Experiências | viagens em grupo, cultura, lazer e experiências compartilhadas |
| `JED-008` | Causas, Voluntariado e Contribuição | ação social, causa, voluntariado, mobilização e campanha comunitária |
| `JED-009` | Organização e Equilíbrio da Vida | coordenação de iniciativas, organização de rotinas e apoio à vida comunitária |

O Coletivo pode propor uma atividade relacionada a um domínio, mas não atribui automaticamente esse domínio à Pessoa participante.

```text
atividade coletiva em JED-006
≠ participante classificado como religioso
```

```text
atividade coletiva em JED-003
≠ participante classificado por situação financeira
```

Multidomínio é legítimo. `Ainda estou descobrindo` pode existir quando o propósito, necessidade ou direção ainda está sendo compreendido. `other_unmapped` preserva áreas ainda não representadas adequadamente.

Regras desta vista:

- o mesmo domínio entre Coletivo e Pessoa não cria match, pertencimento, recomendação ou compartilhamento automático;
- domínio não transfere governança, autoridade ou visibilidade de dados;
- domínio não mede impacto, legitimidade ou maturidade do Coletivo;
- plano pago não altera domínio, relevância orgânica ou impacto;
- `domain_link` permanece semântico e pode ser `0..n`;
- D4 não cria superfície, SVG ou transição; a materialização experiencial permanece D5.

## 4. Planos como etapa transversal canônica

A UXA-100-A3 registra **Planos** canonicamente na jornada operacional do Coletivo. A UXA-100-A4 preserva um contrato documental de origem/retorno associado semanticamente a `COL-002`. Após a reconciliação pós-PR #313/#314, esse contrato não pode ser interpretado como prova de que `COL-002` seja o wireframe principal autenticado final.

A relação lógica preservada no fluxo especializado é:

```text
CONTEXTO ADMINISTRATIVO / COL-002 COMO RESPONSABILIDADE SEMÂNTICA
└── TRN-417 → COL-301 — Planos e comparação
    ├── TRN-411 → COL-302 — revisão de contratação
    │   └── TRN-412 → COL-304 — resultado/recuperação
    │       └── TRN-415 → COL-301
    ├── TRN-413 → COL-303 — downgrade/cancelamento
    │   └── TRN-414 → COL-304
    │       └── TRN-415 → COL-301
    ├── TRN-416 → BND-002 — contratação/dimensionamento assistido
    └── TRN-418 → contexto administrativo / COL-002 como responsabilidade semântica
```

`TRN-417/418` preservam a validação documental de seu **contrato especializado de navegação**. Elas mantêm a regra de que abrir Planos não seleciona tier nem inicia cobrança e que retornar não cancela assinatura ou altera capacidade. Isso não valida a futura composição, hierarquia, navegação principal ou wireframe final do Coletivo.

`TRN-411` a `TRN-415` continuam localmente validadas no pacote UXA-100. `TRN-416` permanece parcial porque o processo comercial posterior a `BND-002` não foi materializado. `BND-002` representa a necessidade de contratação/dimensionamento assistido quando o autoatendimento não for suficiente e não pertence semanticamente a um plano específico.

Entrada contextual permanece válida:

```text
criar atividade/oportunidade
→ limite do plano atingido ou publicação paga não incluída
├── manter rascunho / aguardar ciclo / alternativa gratuita aplicável
└── comparar planos
    → COL-301
```

Referência do fluxo especializado de Planos:

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

Regras:

- `COL-301` mostra plano atual e consumo do ciclo;
- compara `Livre → Mobiliza → Impacta → Rede`;
- comparação incremental pertence a `COL-301` e não cria tela própria;
- o delta direto plano atual → alvo permanece obrigatório;
- `COL-302` exibe preço mensal/anual, recorrência, início, pagador/beneficiário e método em simulação antes da confirmação;
- assinatura permanece separada de comissão, taxa do meio de pagamento e tributo;
- ações operacionais gratuitas válidas permanecem disponíveis;
- `COL-303` exige tratamento explícito de publicações gratuitas/pagas, administradores, núcleos/unidades, compromissos e exportação antes do downgrade;
- nenhum registro ou participante é apagado silenciosamente para efetivar redução de plano;
- `COL-304` diferencia sucesso de falha e preserva o estado anterior quando não houver confirmação;
- quando a contratação não puder ser concluída em autoatendimento, a jornada usa `BND-002` como fronteira assistida;
- plano pago não aumenta relevância orgânica, legitimidade ou impacto.

## 5. Handoffs críticos

| Ligação | Estado |
|---|---|
| COL-002 → COL-003 (`TRN-112`) | contrato/handoff preserva maturidade documental própria; não define wireframe principal final |
| COL-002 ↔ COL-301 (`TRN-417/418`) | **validadas como contrato especializado pela UXA-100-A4; não como prova de UI principal vigente** |
| PER-105 ↔ COL-003 (`TRN-105/106/107/109`) | integralmente validadas |
| COL-003 → PER-106 (`TRN-108`) | integralmente validada |
| PER-106 → PER-107 (`TRN-110`) | integralmente validada |
| PER-107 → PER-108 (`TRN-111`) | integralmente validada por UXA-096 |
| Coletivo ↔ Organização | contratada; materialização bilateral pendente |
| COL-301 → BND-002 (`TRN-416`) | **parcial; processo de contratação/dimensionamento assistido posterior não materializado** |

## 6. Efeito da UXA-100-A4 após a reconciliação

- preserva no pacote de Planos o contrato de origem/retorno associado semanticamente a `COL-002`;
- torna explícito em `COL-301` o retorno sem alteração comercial;
- preserva `TRN-417/418` no limite documental de navegação;
- não define arquitetura da informação principal do Coletivo;
- não transforma a materialização administrativa local em wireframe final;
- não altera a maturidade das transições comerciais internas ou de `BND-002`.

## 7. Princípios preservados

- responsável atua somente com autoridade concedida;
- apoio institucional não transfere governança;
- aprovação não cria função, moderação, autoridade ou presença;
- pertencimento, disponibilidade, papel aceito e autoridade permanecem separados;
- evento histórico não concede acesso interno;
- Central é triagem e Início é síntese; nenhum dos dois substitui canais especializados;
- atividade continua voluntária quando não houver compromisso previamente aceito;
- consulta não é votação universal nem obrigação de resposta;
- plano pago amplia capacidade, não legitimidade, relevância ou impacto;
- abrir Planos não cria intenção de contratação;
- atingir cota não reduz visibilidade das publicações existentes;
- pausa, recusa e saída não reduzem reputação;
- estado canônico mais recente prevalece sobre estado visual obsoleto;
- mesmo domínio entre participantes não transfere contexto pessoal ou autoridade;
- contrato de navegação especializado não define automaticamente a UX principal.

## 8. Estado da vista

Esta vista permanece `draft` porque:

- **a arquitetura da informação e o wireframe principal autenticado do Coletivo ainda não foram definidos**;
- `UXA-016/018` permanecem históricos `superseded`;
- `COL-002` possui evidência administrativa local, mas não é baseline final da experiência principal;
- participantes, comunicação e demais áreas do responsável continuam incompletos;
- estados P0B de superfícies da Pessoa permanecem separados;
- a relação Organização–Coletivo permanece contratada e não materializada;
- as transições comerciais internas de Planos continuam locais e `TRN-416` permanece parcial;
- cobrança real, gateway e processo assistido posterior a `BND-002` não foram implementados/validados ponta a ponta;
- os Domínios de Evolução foram propagados documentalmente por D4, mas ainda não foram materializados/validados como UX; isso permanece D5;
- outras continuidades ainda não foram examinadas como conjunto.

## 9. Estado da frente

A taxonomia vigente de planos permanece `Livre · Mobiliza · Impacta · Rede`. Os fluxos públicos, de participação, gestão de solicitações e Planos preservam suas maturidades próprias quando suportados por autoridade independente. D4 torna `JED-001..JED-009`, multidomínio, `Ainda estou descobrindo` e `other_unmapped` elementos explícitos desta vista, sem iniciar D5.

O próximo avanço da experiência principal autenticada deve partir dos fundamentos, papéis/jobs, arquitetura da informação e mapa de superfícies vigentes — **não do SVG histórico de UXA-016 nem da promoção automática de uma referência administrativa local**. Nenhuma próxima UXA é iniciada automaticamente.