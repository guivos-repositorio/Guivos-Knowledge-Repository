---
id: UXA-100-A4
title: Reconciliação Taxonômica e Revalidação das Materializações de Planos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
depends_on:
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GEM-004-A3
related:
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-STATE-001
normative: false
---

# Reconciliação Taxonômica e Revalidação das Materializações de Planos

## 1. Finalidade

A UXA-100-A4 reconcilia a taxonomia global de planos definida em `GEM-004-A3` com as materializações já criadas pela UXA-100 e registra a revalidação funcional necessária após a substituição de nomenclatura em seis SVGs.

Esta frente **não substitui nem reescreve os contratos históricos de UXA-100, UXA-100-A1, UXA-100-A2 ou UXA-100-A3**. Esses documentos permanecem preservados como evidência do estado em que a materialização original foi criada, auditada e promovida.

A A4 atua como overlay posterior de nomenclatura e interpretação.

## 2. Taxonomia aplicada

| Contexto | Taxonomia vigente |
|---|---|
| Pessoa | Free · Plus · Pro |
| Coletivo | Livre · Mobiliza · Impacta · Rede |
| Organização | Conecta · Eleva · Transforma |

Guivos Business `Start · Growth · Scale · Enterprise` permanece produto especializado e **não se torna quarto participante da UXA-100**.

## 3. Equivalência funcional

| Nomenclatura original UXA-100 | Nomenclatura vigente | Preservação |
|---|---|---|
| Coletivo Gestão | Coletivo Mobiliza | preço, benefícios, limites, estado e decisão preservados |
| Coletivo Impacto | Coletivo Impacta | preço, benefícios, limites, estado e decisão preservados |
| Coletivo Enterprise | Coletivo Rede | capacidade contratada, limites e handoff preservados |
| Business Start usado na jornada da Organização | Organização Conecta | preço, benefícios, limites, estado e decisão preservados |
| Business Growth usado na jornada da Organização | Organização Eleva | preço, benefícios, limites, estado e decisão preservados |
| Business Scale usado na jornada da Organização | Organização Transforma | preço, benefícios, limites, estado e decisão preservados |

A equivalência é taxonômica, não econômica entre produtos. **Organização Transforma ≠ Guivos Business Enterprise.**

## 4. Ativos sincronizados

Os mesmos caminhos e IDs visuais são preservados.

### 4.1 Coletivo

- `uxa-100-collective-plans-screen-desktop.svg`;
- `uxa-100-collective-plans-payments-flow-board.svg`;
- `uxa-100-collective-plan-incremental-benefits-comparison.svg`.

### 4.2 Organização

- `uxa-100-organization-plans-screen-desktop.svg`;
- `uxa-100-organization-plans-payments-flow-board.svg`;
- `uxa-100-organization-plan-incremental-benefits-comparison.svg`.

### 4.3 Pessoa

Os três SVGs de Pessoa não foram alterados porque `Free · Plus · Pro` já estava consistente:

- `uxa-100-person-plans-screen-mobile.svg`;
- `uxa-100-person-plans-payments-flow-board.svg`;
- `uxa-100-person-plan-incremental-benefits-comparison.svg`.

## 5. Escopo das alterações visuais

A sincronização dos seis SVGs altera somente:

- nomes comerciais dos planos;
- microcópia necessária para remover a associação entre Organização e Guivos Business;
- microcópia de `BND-002`/handoff para expressar contratação ou dimensionamento assistido quando necessário;
- guardrails conceituais de que plano não compra relevância, legitimidade, impacto ou evolução.

Não altera:

- identidade do arquivo;
- hierarquia estrutural da tela;
- ação principal;
- preço do participante;
- capacidade ou cota;
- ordem dos estados;
- pagador ou beneficiário;
- tratamento de sucesso/falha;
- tratamento de downgrade/cancelamento;
- quantidade de superfícies;
- quantidade de transições;
- perfil de rastreabilidade.

## 6. Revalidação funcional

A inspeção da A4 verifica os seis ativos modificados contra os contratos já aprovados pela UXA-100-A2 e contra o overlay `GEM-004-A3`.

### 6.1 Critérios

1. a mudança é somente taxonômica/semântica;
2. preços e capacidades dos participantes permanecem idênticos;
3. nenhuma opção paga passa a ser pré-selecionada;
4. alternativas gratuitas/operacionais permanecem disponíveis;
5. nenhuma oportunidade pública é ocultada;
6. assinatura permanece separada de transação, comissão, taxa e tributo;
7. falha não presume ativação;
8. downgrade/cancelamento continuam explicitando consequências;
9. plano pago não compra relevância, confiança, legitimidade, impacto ou evolução;
10. Organização permanece separada de Guivos Business;
11. `BND-002` não é apresentado como plano ou checkout;
12. repetição da mesma intenção continua sem duplicação lógica.

### 6.2 Resultado

| Grupo | SVGs | Resultado |
|---|---:|---|
| Pessoa | 3 | preservados; validação anterior permanece vigente |
| Coletivo | 3 | sincronizados e **revalidados por equivalência funcional** |
| Organização | 3 | sincronizados e **revalidados por equivalência funcional** |
| **Total UXA-100** | **9** | **9/9 com validação funcional vigente** |

Nenhuma pendência específica é introduzida pela mudança taxonômica.

## 7. BND-002

A A4 aplica a semântica vigente de `GEM-004-A3`:

> **BND-002 = fronteira de contratação/dimensionamento assistido quando uma intenção deixa de ser autonomamente configurável.**

Consequências:

- `TRN-416` continua `parcial`;
- `TRN-426` continua `parcial`;
- nenhum processo posterior à fronteira é considerado validado;
- nenhum plano recebe direito automático a handoff;
- nenhuma nova transição é criada.

## 8. Fragmentação e contagens preservadas

A A4 não altera as contagens promovidas pela UXA-100-A3:

| Indicador | Estado após A4 |
|---|---:|
| SVGs canônicos | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| SVGs com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |
| novos SVGs | **0** |
| novos `SURF` | **0** |
| novos `TRN` | **0** |
| novos `BND` | **0** |

Os perfis `R29`, `R30` e `R31` permanecem associados a Pessoa, Coletivo e Organização.

## 9. Guivos Business fora da materialização

A taxonomia Business `Start · Growth · Scale · Enterprise` é reconhecida conceitualmente, mas a A4 não:

- cria `BUS-*`;
- cria tela de Planos Business;
- cria checkout Business;
- copia preço ou entitlement de Organização;
- cria correspondência `Conecta ↔ Start`, `Eleva ↔ Growth` ou `Transforma ↔ Scale/Enterprise`;
- cria nova jornada.

## 10. Precedência

Após integração deste incremento:

1. `GEM-004-A3` governa nomenclatura e leitura conceitual;
2. `UXA-100-A4` governa a reconciliação dessas nomenclaturas com os nove ativos UXA-100;
3. `UXA-100/A1/A2/A3` permanecem autoridades históricas para estrutura, materialização, auditoria e promoção, exceto onde a A4 substitui explicitamente a nomenclatura;
4. IDs, estados e maturidades anteriores permanecem intactos.

## 11. Limites

A A4 não:

- cria oferta pública;
- cria cobrança real ou gateway;
- define preço/entitlement de Guivos Business;
- promove jornada;
- valida processo posterior a `BND-002`;
- inicia UXA-102/V5;
- inicia Engenharia de Produto.

## 12. Veredito

> **Reconciliação aprovada por equivalência funcional: seis SVGs sincronizados em nomenclatura/microcópia, três SVGs de Pessoa preservados, 9/9 ativos UXA-100 com validação vigente, nenhuma nova superfície/transição/fronteira e nenhuma promoção de maturidade.**
