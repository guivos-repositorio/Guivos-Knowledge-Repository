---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.14.0
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

A UXA-097 valida integralmente a continuidade `PER-007 → PER-008`. A primeira variante de Hoje não presume avanço, mudança anterior, urgência ou conteúdo comercial e usa somente condição confirmada, autorizada e vigente.

A jornada completa permanece `draft`: `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda não estão validadas ponta a ponta.

## 2. Descoberta de oportunidades validada como continuidade

A UXA-098 fecha a continuidade entre descoberta territorial e Detalhe:

```text
PER-201 — Mapa
↔ TRN-210 — mesma consulta
→ PER-202 — Lista territorial

PER-201 → TRN-204 → PER-203 — Detalhe
PER-202 → TRN-211 → PER-203 — Detalhe
```

Regras integradas:

- Mapa e Lista preservam contexto de atuação, região, busca, filtros, versão conhecida, seleção e permissões territoriais aplicáveis;
- a alternância não cria autorização, personalização ou relevância;
- Mapa e Lista conduzem à mesma oportunidade lógica em `PER-203`;
- o Detalhe revalida o estado material vigente antes de ação substantiva;
- expiração, pausa, indisponibilidade ou mudança de condição prevalecem sobre cartões obsoletos;
- abrir o Detalhe não equivale a interesse, inscrição, recomendação ou evolução;
- retorno preserva o contexto aplicável sem alterar consentimento ou ordenação.

O efeito externo posterior permanece em `TRN-205` e não foi validado pela UXA-098.

## 3. Planos como etapa transversal canônica

A UXA-100-A3 promove **Planos** como etapa canonicamente registrada da jornada da Pessoa. Ela não substitui Hoje, Explorar, Mapa ou Detalhe e não transforma assinatura em requisito para acessar oportunidades públicas.

Superfícies:

```text
PER-301 — Planos e comparação
├── TRN-401 → PER-302 — revisão de contratação
│   └── TRN-402 → PER-304 — resultado/recuperação
│       └── TRN-405 → PER-301
└── TRN-403 → PER-303 — downgrade/cancelamento
    └── TRN-404 → PER-304
        └── TRN-405 → PER-301
```

As cinco transições estão **localmente validadas** no pacote UXA-100. Isso não comprova gateway, cobrança real, proration ou execução técnica de entitlement.

Entrada voluntária continua prevista por Conta/Configurações. Como essa área genérica ainda não possui ID único no registro, a UXA-100-A3 não inventa uma transição de origem.

Entrada contextual legítima:

```text
correspondência personalizada adicional após cota Free
→ prévia limitada da camada personalizada
├── Explorar oportunidades públicas
├── Ver no Mapa
└── Conhecer planos
    → PER-301
```

A superfície específica de correspondência personalizada também não recebe ID novo nesta frente; o estado funciona como gatilho contextual documentado.

Referências canônicas:

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

Regras de jornada:

- a Pessoa pode acessar Planos voluntariamente sem atingir qualquer limite;
- `Guivos Free` permanece um plano real, funcional e não degradado artificialmente;
- após a cota de correspondências completas, somente a camada personalizada adicional pode ficar limitada;
- oportunidade pública, Explorar e Mapa permanecem acessíveis;
- `PER-301` apresenta matriz geral, ganho incremental `Free → Plus → Pro` e delta direto plano atual → alvo;
- comparação incremental não cria superfície própria;
- recorrência, preço mensal/anual e data de início aparecem antes da confirmação em `PER-302`;
- assinatura não amplia consentimento ou escopo de dados automaticamente;
- `PER-303` mostra o que será perdido ou reduzido antes de downgrade/cancelamento;
- cancelamento mostra data efetiva, plano posterior e interrupção da renovação;
- `PER-304` diferencia sucesso e falha, preservando Free/estado anterior quando não houver confirmação;
- pagamento não altera relevância, confiança, posição orgânica nem garantia de evolução.

A UXA-100-A2 forneceu a validação funcional visual; a UXA-100-A3 forneceu a identidade canônica.

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

## 5. Compreensão inicial → Hoje validada

`PER-007 → TRN-007 → PER-008` permanece integralmente validada pela UXA-097. Personalização utiliza somente base confirmada, autorizada e vigente; Hoje continua acessível sem personalização; repetição não cria avanço nem efeito duplicado.

## 6. Continuidades de Coletivos preservadas

- `COL-003 → PER-105 aprovado → PER-106` permanece validada em `TRN-108`;
- `PER-106 → PER-107` permanece validada em `TRN-110`;
- `PER-107 → PER-108` permanece validada em `TRN-111`.

## 7. Proteções preservadas

- conclusão da compreensão inicial não equivale a avanço humano;
- personalização não é condição para acessar Hoje;
- oportunidade publicada não é automaticamente recomendada;
- proximidade não equivale a relevância;
- patrocínio não compra relevância funcional;
- plano pago não compra relevância funcional;
- atingir cota personalizada do Free não oculta o catálogo público;
- Mapa/Lista não criam autorização territorial nova;
- abrir Detalhe não cria obrigação de agir;
- compartilhar pouco permanece legítimo;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- aprovação não cria função, autoridade ou presença obrigatória;
- estado canônico vigente prevalece sobre renderização anterior.

## 8. Estado da vista

Esta vista permanece `draft` porque:

- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda são parciais;
- `TRN-205` permanece parcial para efeito externo de oportunidade;
- as transições de Planos são locais e não representam cobrança ponta a ponta;
- as entradas genéricas de Conta/Configurações e de correspondência personalizada ainda não possuem transições canônicas de origem;
- estados P0B adicionais permanecem separados;
- áreas internas especializadas a partir de `PER-108` não foram validadas como conjunto;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

O status `draft` não invalida referências locais e transições específicas já validadas.

## 9. Estado da frente de Planos

A fragmentação e promoção canônica da Pessoa foi concluída pela UXA-100-A3 em `PER-301` a `PER-304` e `TRN-401` a `TRN-405`. Validação de cobrança real e futuras entradas contextuais permanece separada. Nenhuma próxima UXA é iniciada automaticamente.