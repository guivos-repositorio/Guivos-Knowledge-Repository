---
id: UXA-082
title: Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-081
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
related:
  - GKR-JOURNEYS-001
  - GKR-STATE-001
  - ROADMAP-12.55.0
normative: false
---

# Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas

## 1. Finalidade

A UXA-082 valida a Galeria Visual Integrada como instrumento de inspeção e verifica se sua organização permite examinar assertividade, sequência, cobertura e dependências sem confundir inventário visual com jornada validada.

A etapa também reorganiza a priorização das lacunas com base em dependência funcional, autoridade, valor de continuidade e esforço documental.

## 2. Base examinada

```text
main
df57e0b99ddd2b1d779e72f51a2f314f5b00d111
```

Foram examinados:

- o índice da Galeria Visual Integrada;
- as cinco páginas temáticas da galeria;
- os 97 vínculos para SVGs canônicos;
- o Catálogo Integrado de Telas;
- o Registro Granular de Superfícies e Estados;
- o Registro Granular de Transições;
- o registro de lacunas;
- as autoridades e validações de origem indicadas por família.

## 3. Método

A validação aplicou cinco critérios:

1. **completude mecânica** — existência e resolução dos vínculos visuais;
2. **ordem funcional** — sequência compatível com as transições registradas;
3. **rastreabilidade** — distinção entre SVG, superfície, estado, transição e validação;
4. **legibilidade de inspeção** — capacidade de percorrer entrada, decisão, saída, retorno e handoff;
5. **priorização por dependência** — superfícies de origem e autoridade precedem efeitos a jusante.

## 4. Confirmações

Permanecem confirmados:

| Indicador | Resultado |
|---|---:|
| SVGs referenciados | 97 |
| SVGs com validação funcional de origem | 87 |
| SVGs sem validação específica | 10 |
| IDs granulares com referência visual direta ou agrupada | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |

As cinco páginas temáticas e os vínculos canônicos são mecanicamente utilizáveis como inventário visual.

## 5. Achados funcionais e visuais

### F01 — ordem funcional incorreta na página da Pessoa

A página `screen-gallery-person.md` apresenta:

```text
Home pública + Tela Hoje
→ Início protegido
→ Compreensão inicial
→ Expressão Guiada do Momento Atual
```

O Registro Granular de Transições estabelece a sequência funcional:

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada
→ inventário e autorização
→ processamento
→ compreensão inicial revisável
→ Tela Hoje
```

A Tela Hoje não deve permanecer agrupada com a Home como se ambas ocupassem o início da jornada. A expressão guiada também deve preceder a compreensão inicial.

### F02 — ausência de rota integrada de inspeção

O índice separa os SVGs por domínio, mas não fornece uma rota explícita entre:

- entrada e experiência recorrente da Pessoa;
- publicação institucional e descoberta de oportunidades;
- solicitação da Pessoa e decisão do responsável;
- aprovação e continuidade no Coletivo;
- exposição patrocinada e retorno ao contexto orgânico.

A galeria permite localizar telas, mas ainda não permite percorrer a jornada integrada com segurança.

### F03 — rastreabilidade agrupada insuficiente para assertividade

As páginas associam conjuntos de SVGs a conjuntos de IDs. Essa agregação é válida para inventário, porém não informa, por arquivo:

- papel do SVG na sequência;
- estado principal ou alternativo;
- transição de entrada;
- transição de saída;
- retorno ou interrupção;
- lacuna relacionada.

A ausência dessa camada impede usar a galeria como parecer de assertividade por tela.

### F04 — versões documentais divergentes

O índice da galeria foi corrigido mecanicamente para `draft` 0.1.1, enquanto resumos vigentes ainda registram `draft` 0.1.0. A divergência não altera os SVGs, mas impede promoção documental antes de reconciliação.

### F05 — prioridade de Coletivos invertida por dependência

A fila anterior colocava `GKR-SURF-PER-106` — Meus Coletivos — antes de `GKR-SURF-COL-002` e `GKR-SURF-COL-003`.

Entretanto:

- `GKR-TRN-112` conduz da Visão Geral do Responsável para a gestão de solicitações;
- `GKR-TRN-108` parte da gestão de solicitações e produz o vínculo percebido em Meus Coletivos;
- `GKR-TRN-110` depende de Meus Coletivos para abrir a Central de Atualizações;
- `GKR-TRN-111` depende da Central para abrir o Início do Participante.

A ordem governada deve começar pelas superfícies de autoridade do responsável.

## 6. Veredito

**Não aprovada para promoção até reformulação controlada.**

A galeria está aprovada somente como:

- inventário visual centralizado;
- ponto de acesso aos 97 SVGs;
- instrumento de identificação de cobertura e ausências.

Ela ainda não está aprovada como:

- sequência funcional integrada;
- matriz de assertividade por tela;
- evidência de continuidade ponta a ponta;
- base suficiente para promoção das jornadas ou início de produto.

A galeria permanece `draft`.

## 7. Priorização governada

### 7.1 Trilha documental imediata

1. corrigir a ordem funcional da página da Pessoa;
2. separar Home pública e Tela Hoje na estrutura de inspeção;
3. criar rota integrada entre as cinco páginas;
4. registrar por grupo ou SVG o papel na sequência, transições e lacunas;
5. reconciliar versões e estados documentais;
6. submeter a galeria a nova validação antes de promoção.

### 7.2 Primeira frente futura de materialização

Após a estabilização da galeria, a continuidade operacional de Coletivos deverá seguir esta dependência:

| Ordem | Superfície | ID | Justificativa |
|---:|---|---|---|
| 1 | Visão Geral do Responsável | GKR-SURF-COL-002 | origem protegida da operação do responsável |
| 2 | gestão completa de solicitações | GKR-SURF-COL-003 | autoridade que analisa, solicita complemento, aprova ou recusa |
| 3 | Meus Coletivos | GKR-SURF-PER-106 | efeito do vínculo aprovado percebido pela Pessoa |
| 4 | Central de Atualizações | GKR-SURF-PER-107 | continuidade dos vínculos ativos |
| 5 | Início do Participante | GKR-SURF-PER-108 | entrada operacional no Coletivo selecionado |

Essa ordem substitui a priorização anterior apenas como decisão documental. Nenhuma superfície é iniciada nesta etapa.

### 7.3 Dívidas de validação em trilha separada

Devem permanecer separadas da fila de novas telas:

1. `GKR-TRN-007` — compreensão inicial → Tela Hoje;
2. `GKR-TRN-203`, `GKR-TRN-210` e `GKR-TRN-211` — publicação, mapa, lista e detalhe;
3. `GKR-TRN-305` — dez estados residuais da UXA-055;
4. matriz integrada de erros, retornos e interrupções.

Esses itens exigem validação ou contrato integrado, não necessariamente novos SVGs.

## 8. Limites

A UXA-082 não:

- modifica SVGs;
- cria ou redesenha telas;
- corrige a estrutura da galeria;
- promove a galeria;
- fecha lacunas;
- valida individualmente os dez estados da UXA-055;
- inicia materialização de Coletivos;
- cria protótipo navegável;
- inicia aplicação, motor, teste com pessoas ou Engenharia de Produto.

## 9. Próxima transição possível

A próxima transição documental possível é:

**UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção.**

A UXA-083 dependerá de autorização separada.
