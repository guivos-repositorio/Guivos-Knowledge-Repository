---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.18.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001
  - GKR-UX-D5-C1-001
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
  - UXA-100-A4
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

## 2. Eixo de Domínios de Evolução

A D4 propaga para esta vista o vocabulário canônico de `PAS-001-DOMAIN-MODEL-001` e a reconciliação de `PAS-001-DOMAIN-RECON-001`.

A Jornada da Pessoa passa a ser lida em dois eixos simultâneos:

```text
como a jornada acontece
×
sobre qual área da vida/evolução a jornada está tratando
```

Todos os nove Domínios de Evolução podem ser relevantes à Pessoa, conforme contexto declarado, autorizado ou legitimamente confirmado:

| ID | Domínio | Exemplos de contexto da Pessoa |
|---|---|---|
| `JED-001` | Saúde e Bem-estar | hábitos, atividade física, sono, alimentação, autocuidado, prevenção, qualidade de vida |
| `JED-002` | Trabalho, Carreira e Estudos | emprego, recolocação, carreira, cursos, estudos, competências, certificações, liderança |
| `JED-003` | Vida Financeira | orçamento, reserva, renda, dívida, planejamento e organização financeira |
| `JED-004` | Empreendedorismo e Projetos | ideia, negócio, projeto pessoal, validação, parceiros e execução |
| `JED-005` | Relacionamentos e Vida Social | família, amizades, convivência, pertencimento e novas conexões |
| `JED-006` | Espiritualidade, Propósito e Valores | fé, espiritualidade, propósito, valores, reflexão e comunidade escolhida |
| `JED-007` | Viagens, Lazer, Cultura e Novas Experiências | viagens, hobbies, cultura, lazer, eventos e experiências desejadas |
| `JED-008` | Causas, Voluntariado e Contribuição | voluntariado, causas, participação comunitária, contribuição e serviço |
| `JED-009` | Organização e Equilíbrio da Vida | rotina, prioridades, tempo, equilíbrio e reorganização após mudanças |

Uma leitura semântica possível é:

```text
Pessoa
→ Momento Atual
→ domínio declarado/candidato
→ Direção
→ Objetivo
→ Próximo Passo
→ Oportunidades compatíveis e relevantes
→ Experiência
→ Evidências legítimas
→ Evolução reconhecida pelo participante
```

O domínio pode aparecer antes, durante ou depois da formulação de um Objetivo. A Pessoa não deverá ser obrigada a classificar seu relato para continuar quando a capacidade aplicável não exigir essa classificação.

Multidomínio é legítimo. Exemplo:

```text
"Quero melhorar minha renda para conseguir fazer uma viagem"
→ JED-003 Vida Financeira
+ JED-007 Viagens, Lazer, Cultura e Novas Experiências
```

`Ainda estou descobrindo` permanece estado legítimo de exploração e não constitui `JED-010`. `other_unmapped` preserva uma área ainda não representada adequadamente pela taxonomia e não autoriza reclassificação silenciosa.

Regras desta vista:

- `domain_link` pode ser `0..n` e permanece associação semântica, temporal e revisável;
- domínio candidato não equivale a domínio confirmado;
- domínio não é identidade permanente da Pessoa;
- domínio não é diagnóstico, score, prioridade humana ou prova de evolução;
- saúde, espiritualidade, finanças e outros contextos sensíveis preservam finalidade, autoridade e proteção próprias;
- plano pago, patrocínio ou oferta comercial não altera domínio nem relevância funcional;
- D4 não cria nova tela, pergunta obrigatória, chip, card, SVG ou transição;
- D5-A e D5-B materializam o eixo em superfícies já existentes;
- D5-C1 cria somente as responsabilidades e handoffs mínimos de Objetivos, Próximos Passos e Evolução, ainda sem SVG.

## 3. Direção, movimento e evolução a partir de Hoje

A D5-C1 reconhece três responsabilidades especializadas que já possuíam autoridade funcional no PAS-001, mas não possuíam identidade própria no registro granular da Experience Architecture.

A estrutura passa a ser:

```text
PER-008 — Hoje
├── TRN-008 → PER-010 — Meus Objetivos
│   └── TRN-009 → PER-008
├── TRN-010 → PER-011 — Meus Próximos Passos
│   └── TRN-011 → PER-008
└── TRN-012 → PER-012 — Minha Evolução
    └── TRN-013 → PER-008
```

As três responsabilidades e as seis transições estão **contratadas**, sem materialização visual própria e sem validação ponta a ponta.

### 3.1 PER-010 — Meus Objetivos

`PER-010` governa a compreensão, organização e controle dos objetivos da Pessoa, preservando estados, prioridades, critérios, marcos, progresso/evidências legítimas, conflitos, histórico, privacidade e revisão conforme `PAS-001-OBJ-VIEW-001`.

Um objetivo pode possuir `0..n domain_link`, mas:

```text
Domínio de Evolução
≠ Objetivo
≠ prioridade
≠ critério de sucesso
≠ progresso
```

Para a futura UX, `área da jornada` deve ser distinguida de `dimensão estrutural do Contexto Vivo`.

### 3.2 PER-011 — Meus Próximos Passos

`PER-011` governa movimentos contextuais, não uma lista coercitiva de tarefas.

Pode organizar passos por estado, prioridade, prontidão, dependência, responsabilidade, período e Área da jornada. A formulação histórica `área da vida` é lida, para Experience Architecture, como Área da jornada vinculada semanticamente ao modelo de Domínios.

```text
domínio relacionado
≠ obrigação
≠ urgência
≠ prontidão
≠ execução
```

### 3.3 PER-012 — Minha Evolução

`PER-012` governa a compreensão e o controle de trajetórias, mudanças, continuidades, baselines, direções, evidências, confiança, incerteza, interpretações, contestações e histórico.

A futura materialização deve preservar explicitamente:

```text
Domínio de Evolução
≠ dimensão estrutural do Contexto Vivo
≠ aspecto descritivo da mudança
≠ trajetória
≠ score
```

`Minha Evolução` não poderá ser convertida em roda da vida obrigatória, ranking, percentual global da Pessoa, diagnóstico ou avaliação espiritual.

### 3.4 Papel de Hoje

`PER-008` permanece síntese recorrente, não dashboard completo das três capacidades.

A leitura é:

```text
Hoje sintetiza
→ direção atual, quando relevante
→ movimento atual, quando relevante
→ mudança ou continuidade relevante, quando legítima

superfícies especializadas
→ aprofundam e oferecem controle
```

Isso não exige três cards permanentes em Hoje e não autoriza exposição de conteúdo sensível por padrão.

### 3.5 Handoffs não contratados

A D5-C1 não cria navegação direta entre:

- `PER-010 ↔ PER-011`;
- `PER-011 ↔ PER-012`;
- `PER-010 ↔ PER-012`.

Relação semântica entre Objetivo, Próximo Passo e Evolução não é evidência suficiente de necessidade de navegação direta.

## 4. Descoberta de oportunidades e saída consciente

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

## 5. Planos como etapa transversal canônica

A UXA-100-A3 promove **Planos** como etapa canonicamente registrada da jornada da Pessoa. A UXA-100-A4 fecha a identidade documental de sua origem voluntária sem criar uma tela artificial de Conta.

```text
PER-009 — Conta e configurações
├── TRN-406 → PER-301 — Planos e comparação
│   ├── TRN-401 → PER-302 — revisão de contratação
│   │   └── TRN-402 → PER-304 — resultado/recuperação
│   │       └── TRN-405 → PER-301
│   ├── TRN-403 → PER-303 — downgrade/cancelamento
│   │   └── TRN-404 → PER-304
│   │       └── TRN-405 → PER-301
│   └── TRN-407 → PER-009 — retorno sem alteração de plano
```

`TRN-401` a `TRN-405` permanecem **localmente validadas**. `TRN-406/407` ficam **contratadas**, pois `PER-009` possui identidade canônica suficiente para o handoff, mas ainda não possui materialização visual própria que sustente validação ponta a ponta.

Abrir Planos por `TRN-406` não seleciona plano, não inicia cobrança, não consome cota e não amplia consentimento. Retornar por `TRN-407` não cancela assinatura nem altera o plano atual.

Entrada contextual legítima permanece:

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

## 6. Pessoa em Coletivos

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

## 7. Proteções preservadas

- conclusão da compreensão inicial não equivale a avanço humano;
- personalização não é condição para acessar Hoje;
- abrir Meus Objetivos não cria, confirma ou prioriza objetivo;
- abrir Meus Próximos Passos não inicia, aceita ou conclui movimento;
- abrir Minha Evolução não presume mudança, progresso ou evolução reconhecida;
- conteúdo sensível nas três superfícies especializadas exige minimização e controle;
- oportunidade publicada não é automaticamente recomendada;
- proximidade não equivale a relevância;
- patrocínio e plano pago não compram relevância funcional;
- atingir cota personalizada do Free não oculta catálogo público;
- abrir Planos voluntariamente não cria intenção de compra;
- abrir Detalhe não cria obrigação de agir;
- sair para ambiente externo não amplia consentimento nem transfere a jornada pessoal por padrão;
- compartilhar pouco permanece legítimo;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- aprovação não cria função, autoridade ou presença obrigatória;
- estado canônico vigente prevalece sobre renderização anterior;
- mesmo domínio entre Pessoa, Coletivo e Organização não cria match, recomendação ou compartilhamento automático.

## 8. Estado da vista

Esta vista permanece `draft` porque:

- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda são parciais;
- `PER-010`, `PER-011` e `PER-012` ainda não possuem materialização própria e `TRN-008..013` permanecem contratadas;
- as transições comerciais internas de Planos são locais e não representam cobrança ponta a ponta;
- `PER-009` ainda não possui materialização própria e `TRN-406/407` permanecem contratadas;
- estados P0B adicionais permanecem separados;
- áreas internas especializadas a partir de `PER-108` não foram validadas como conjunto;
- D5-A e D5-B materializam Domínios em superfícies existentes, enquanto a materialização visual de D5-C permanece pendente por responsabilidade;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

`TRN-205` deixa de ser motivo de `draft`: a UXA-101 a valida integralmente **até `BND-001`**, sem validar o processo externo posterior.

## 9. Estado atual

V1, V2, V3 e V4 estão encerradas nos respectivos limites documentais. A frente de Planos está canonicamente registrada e sua origem voluntária possui identidade formal pela UXA-100-A4. D4 torna `JED-001..JED-009`, multidomínio, `Ainda estou descobrindo` e `other_unmapped` elementos explícitos desta vista. D5-A e D5-B materializam parte desse eixo em superfícies já existentes. A D5-C1 contrata `PER-010..012` e `TRN-008..013` sem criar SVG. V5/UXA-102, D6, D7 e Engenharia de Produto não foram iniciados automaticamente.