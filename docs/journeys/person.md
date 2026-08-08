---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.15.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-002
  - UXA-004
  - UXA-006
  - UXA-007
  - UXA-010
  - UXA-012
  - UXA-020
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-028
  - UXA-029
  - UXA-036
  - UXA-037
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-067
  - UXA-069
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-101
normative: false
---

# Jornada Integrada da Pessoa

## 1. Início protegido e compreensão inicial

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada
→ inventário e autorização
→ processamento visível
→ compreensão inicial revisável
→ TRN-007 integralmente validada
→ primeira Tela Hoje
→ experiência recorrente e continuidades autorizadas
```

A UXA-097 valida integralmente `PER-007 → PER-008`. A primeira variante de Hoje não presume avanço, mudança anterior, urgência ou conteúdo comercial e usa somente condição confirmada, autorizada e vigente.

A jornada completa permanece `draft`: `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda não estão validadas ponta a ponta.

## 2. Descoberta de oportunidades e saída consciente

A UXA-098 fecha a continuidade entre descoberta territorial e Detalhe; a UXA-101 fecha V4 até a fronteira externa:

```text
PER-201 — Mapa
↔ TRN-210 — mesma consulta
→ PER-202 — Lista territorial

PER-201 → TRN-204 → PER-203 — Detalhe
PER-202 → TRN-211 → PER-203 — Detalhe

PER-203
→ “Ver como participar”
→ estado de revisão de saída em PER-203
→ confirmar destino/responsável/dados e limites
→ TRN-205
→ BND-001 — autoridade externa
```

Regras integradas:

- Mapa e Lista preservam contexto de atuação, região, busca, filtros, versão conhecida, seleção e permissões territoriais aplicáveis;
- Mapa e Lista conduzem à mesma oportunidade lógica em `PER-203`;
- o Detalhe revalida estado material vigente antes de ação substantiva;
- abrir o Detalhe não equivale a interesse, inscrição, recomendação ou evolução;
- selecionar `Ver como participar` ainda não sai da Guivos: abre estado de revisão dentro de `PER-203`;
- a revisão identifica explicitamente ambiente externo e responsável;
- a Pessoa vê o que acompanha ou não acompanha a transição;
- continuar exige ação afirmativa e revalidação do destino conhecido/autorizado;
- destino ausente, inválido ou materialmente alterado bloqueia redirecionamento silencioso;
- `Voltar ao detalhe` é caminho legítimo e sem penalidade;
- alcançar `BND-001` transfere autoridade ao terceiro; a Guivos não presume inscrição, reserva, compra ou contratação concluída;
- retornar posteriormente não presume resultado externo.

Referência visual reformulada e revalidada pela UXA-101:

![Detalhe e revisão de saída](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg)

## 3. Planos como etapa transversal canônica

A UXA-100-A3 promove **Planos** como etapa canonicamente registrada da jornada da Pessoa. Ela não substitui Hoje, Explorar, Mapa ou Detalhe e não transforma assinatura em requisito para acessar oportunidades públicas.

```text
PER-301 — Planos e comparação
├── TRN-401 → PER-302 — revisão de contratação
│   └── TRN-402 → PER-304 — resultado/recuperação
│       └── TRN-405 → PER-301
└── TRN-403 → PER-303 — downgrade/cancelamento
    └── TRN-404 → PER-304
        └── TRN-405 → PER-301
```

As cinco transições estão **localmente validadas**; isso não comprova gateway, cobrança real, proration ou execução técnica de entitlement.

Entrada voluntária continua prevista por Conta/Configurações. Como essa área genérica ainda não possui ID único no registro, a UXA-100-A3 não inventa transição de origem.

Entrada contextual legítima:

```text
correspondência personalizada adicional após cota Free
→ prévia limitada da camada personalizada
├── Explorar oportunidades públicas
├── Ver no Mapa
└── Conhecer planos → PER-301
```

Regras de jornada:

- `Guivos Free` permanece plano real e funcional;
- oportunidade pública, Explorar e Mapa permanecem acessíveis;
- comparação geral e incremental pertencem a `PER-301`;
- recorrência, preço e consequência aparecem antes da confirmação;
- assinatura não amplia consentimento ou escopo de dados automaticamente;
- downgrade/cancelamento explicita capacidades e data efetiva;
- falha preserva Free/estado anterior quando não houver confirmação;
- pagamento não altera relevância, confiança, posição orgânica nem garantia de evolução.

## 4. Pessoa em Coletivos

```text
Explorar Coletivos
→ Resultados de Busca
→ Perfil Público
→ Revisão e Solicitação
→ Solicitação Pendente
→ resultado aprovado
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

| Etapa | Maturidade | Referência | Evidência | Continuidade integrada |
|---|---|---|---|---|
| descoberta e busca | validado | UXA-060 | UXA-061 | parcial |
| Perfil Público | validado | UXA-062 | UXA-063 | parcial |
| revisão e solicitação | validado | UXA-064 | UXA-065 | parcial |
| Solicitação Pendente | validado | UXA-066 | UXA-067; estado aprovado UXA-092 | TRN-105/106/107/109 por UXA-090; TRN-108 por UXA-092 |
| Meus Coletivos | validado | UXA-091/092/094 | UXA-092/094 | TRN-108 e TRN-110 integralmente validadas |
| Central de Atualizações | validado | UXA-093/094/095/096 | UXA-094; versão corrente UXA-096 | TRN-110 e TRN-111 integralmente validadas |
| Início do Participante | validado | UXA-095/096 | UXA-096 | TRN-111 integralmente validada |

## 5. Proteções preservadas

- conclusão da compreensão inicial não equivale a avanço humano;
- personalização não é condição para acessar Hoje;
- oportunidade publicada não é automaticamente recomendada;
- proximidade não equivale a relevância;
- patrocínio e plano pago não compram relevância funcional;
- atingir cota personalizada do Free não oculta catálogo público;
- abrir Detalhe não cria obrigação de agir;
- sair para ambiente externo não amplia consentimento nem transfere a jornada pessoal por padrão;
- compartilhar pouco permanece legítimo;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- aprovação não cria função, autoridade ou presença obrigatória;
- estado canônico vigente prevalece sobre renderização anterior.

## 6. Estado da vista

Esta vista permanece `draft` porque:

- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda são parciais;
- as transições de Planos são locais e não representam cobrança ponta a ponta;
- entradas genéricas de Conta/Configurações e correspondência personalizada ainda não possuem transições canônicas de origem;
- estados P0B adicionais permanecem separados;
- áreas internas especializadas a partir de `PER-108` não foram validadas como conjunto;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

`TRN-205` deixa de ser motivo de `draft`: a UXA-101 a valida integralmente **até `BND-001`**, sem validar o processo externo posterior.

## 7. Estado atual

V1, V2, V3 e V4 estão encerradas nos respectivos limites documentais. A frente de Planos está canonicamente registrada. V5 não foi iniciada e nenhuma etapa de Engenharia de Produto foi autorizada automaticamente.