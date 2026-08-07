---
id: GKR-JOURNEY-ORGANIZATION-001
title: Jornada Integrada da Organização
status: draft
version: 0.5.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-004
  - UXA-007
  - UXA-008
  - UXA-012
  - UXA-013
  - UXA-014
  - UXA-015
  - UXA-017
  - UXA-019
  - UXA-024
  - UXA-025
  - UXA-028
  - UXA-029
  - UXA-038
  - UXA-055
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-098
  - UXA-100
normative: false
---

# Jornada Integrada da Organização

## 1. Continuidade institucional

```text
identidade, unidade e autoridade
→ visão geral institucional
→ responsabilidade material atual
→ oportunidades e programas
→ relações com Coletivos e Organizações
→ compromissos e recursos
→ evidências e resultados permitidos
→ revisão, renovação, ajuste, pausa ou encerramento
```

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| fundação institucional | contratado | UXA-014 | — | — | não examinada |
| Visão Geral da Organização | validado | UXA-014 | UXA-015 | UXA-017 | parcial |
| responsabilidade material atual | contratado | UXA-014 | presente parcialmente na Visão Geral | UXA-017 no escopo da referência | parcial |
| cadastro de oportunidades | validado | UXA-004 | UXA-008 | UXA-013 | **publicação → descoberta validada por UXA-098** |
| descoberta Mapa/Lista e detalhe | validado | UXA-004 | UXA-024; UXA-028; UXA-007 | UXA-025; UXA-029; UXA-012 | **TRN-203/204/210/211 integralmente validadas por UXA-098** |
| relação Organização–Coletivo | contratado | UXA-019 | — | — | ausente |
| patrocínio e Opportunity Boost | materializado | UXA-038 | UXA-040 a UXA-054 | UXA-041 a UXA-055 conforme pacote | parcial |
| Planos e cobrança | **materializado candidato** | GEM-004 / UXA-100 | tela dedicada UXA-100 | validação funcional pendente | não integrada canonicamente |
| evidências e resultados institucionais | indeterminado | referências dispersas | matriz integrada ausente | — | não examinada |

A validação de uma tela institucional ou de um fluxo de cadastro não equivale à validação integral da jornada institucional.

## 2. Publicação → descoberta validada

A UXA-098 formaliza:

```text
ORG-003
→ oportunidade aprovada e ativa
→ autoridade e informações materiais vigentes
→ TRN-203
→ candidata à descoberta em PER-201
```

A ativação:

- torna a oportunidade elegível ao inventário de descoberta;
- não garante impressão, posição, alcance ou recomendação;
- não concede à Organização autoridade sobre relevância individual;
- não converte patrocínio em prioridade orgânica;
- permanece subordinada a disponibilidade, elegibilidade, proteção, atualização e moderação aplicáveis.

Pausa, expiração, encerramento ou alteração material prevalecem sobre cartões ou detalhes anteriormente renderizados. Reprocessamento do mesmo estado não duplica oportunidade nem prioridade.

## 3. Continuidade até o Detalhe

A oportunidade mantém a mesma identidade lógica em Mapa, Lista e Detalhe.

- `TRN-210`: Mapa e Lista preservam a mesma consulta;
- `TRN-204`: Mapa abre o Detalhe preservando origem e estado;
- `TRN-211`: Lista abre o mesmo Detalhe preservando origem e estado;
- `TRN-205`: eventual efeito externo posterior permanece separado e parcial.

A Organização continua responsável por manter preço, disponibilidade, local, modalidade, capacidade, elegibilidade, risco, responsável e demais informações materiais atualizados.

## 4. Planos como etapa transversal candidata

A UXA-100 inclui **Planos** na jornada institucional da Organização. A tela pode ser acessada voluntariamente pela administração e também quando uma capacidade contratual/comercial for atingida.

```text
Administração
→ Planos
→ plano atual + consumo do ciclo
→ comparar Business Start / Growth / Scale
→ manter, mudar ou solicitar proposta
→ revisão da contratação quando aplicável
→ pagamento simulado ou processo comercial governado
→ retorno à operação institucional
```

Entrada contextual:

```text
criar nova oportunidade/programa
→ capacidade do ciclo atingida
├── arquivar / agendar / manter rascunho quando aplicável
└── comparar planos
    → Planos
```

A tela candidata dedicada é:

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

A tela deve:

- mostrar plano atual, uso e período do ciclo;
- comparar `Business Start → Business Growth → Business Scale`;
- evidenciar somente ganhos incrementais por degrau;
- oferecer delta direto do plano atual para o escolhido;
- tratar Scale como proposta comercial e capacidade dimensionada, não checkout definitivo;
- no downgrade, informar redução de oportunidades, publicações ativas, administradores, unidades, Coletivos relacionados, analytics e integrações;
- separar capacidade comercial de relevância, confiança, legitimidade e resultado.

A etapa é materialização candidata da UXA-100 e ainda não cria superfície ou transição canônica.

## 5. Relação com Coletivos

```text
rascunho
→ proposta
→ avaliação bilateral
→ negociação
→ aprovação pelas duas autoridades
→ relação ativa
→ revisão
→ renovação, ajuste, pausa ou encerramento
```

| Campo | Organização | Coletivo | Estado da integração |
|---|---|---|---|
| autoridade | representante institucional autorizado | responsável autorizado pelo Coletivo | contratada pela UXA-019 |
| superfície de proposta | não materializada especificamente | não materializada especificamente | ausente |
| avaliação e negociação | contratada | contratada | não materializada |
| aprovação bilateral | contratada | contratada | não validada |
| relação ativa e revisão | contratada | contratada | não materializada |
| saída, pausa e encerramento | contratada | contratada | não materializada |

A relação preserva finalidade, compromissos, recursos, autonomia, dados, contestação e saída. Apoio ou patrocínio não concede propriedade, direção ou acesso irrestrito a dados.

## 6. Limites de visibilidade

- publicação não equivale a distribuição garantida;
- dados pessoais individuais não são expostos por padrão;
- resultados agregados dependem de finalidade e autoridade;
- publicidade não compra legitimidade, reputação ou relevância funcional;
- plano pago amplia capacidade institucional, não relevância orgânica;
- atingir limite do plano não altera retroativamente a legitimidade de publicações existentes;
- representante institucional atua somente dentro da unidade e do papel apresentados;
- cobertura incompleta permanece indicada como lacuna.

## 7. Estado da vista

Esta vista permanece `draft` porque:

- a relação Organização–Coletivo não possui materialização bilateral específica;
- a matriz institucional completa ainda não existe;
- `TRN-201` permanece parcial e `TRN-202` localmente validada;
- integrações patrocinadas com Mapa/Lista (`TRN-304`/`TRN-306`) permanecem parciais;
- Planos é etapa candidata sem superfície/transição canônica;
- evidências e resultados institucionais continuam sem matriz integrada.

A UXA-098 fecha especificamente `TRN-203`, `TRN-204`, `TRN-210` e `TRN-211`, sem promover a jornada institucional completa.

## 8. Próxima evolução possível

A UXA-100 adiciona Planos à leitura institucional sem promover a jornada. A próxima decisão desta frente é validar funcionalmente as telas e definir superfícies/transições somente após essa validação.