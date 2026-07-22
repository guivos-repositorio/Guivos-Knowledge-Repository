---
id: GEM-006-DISCLOSURE-RANKING-CONFLICT-POLICY-001
title: Política de Transparência, Ranking e Conflitos de Parceiros
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-006
---

# Política de Transparência, Ranking e Conflitos de Parceiros

## 1. Objetivo

Impedir que pagamento, comissão, patrocínio, exclusividade ou relação estratégica sejam apresentados como relevância neutra, qualidade ou independência.

## 2. Disclosures obrigatórios

Deverão ser identificados, quando aplicáveis:

- parceiro comercial;
- anunciante;
- patrocinador;
- comissão;
- afiliação;
- posição promovida;
- exclusividade;
- benefício financiado;
- conteúdo patrocinado;
- influência sobre ordenação;
- interesse econômico da Guivos;
- restrição de disponibilidade.

## 3. Posicionamento pago

Poderá existir somente quando:

- estiver claramente identificado;
- não for apresentado como recomendação neutra;
- o parceiro atender a requisitos mínimos;
- não eliminar alternativas legítimas;
- não comprometer segurança ou relevância;
- o participante puder compreender a natureza comercial.

## 4. Ranking orgânico

Deverá permanecer separado de:

- pagamento;
- comissão;
- volume comercial;
- patrocínio;
- relação societária;
- pressão do parceiro;
- verba de mídia.

Critérios orgânicos futuros deverão ser documentados e contestáveis.

## 5. Conflitos mínimos

| Conflito | Risco |
|---|---|
| parceiro paga e aparece primeiro | recomendação distorcida |
| parceiro financia e valida evento | evidência manipulada |
| patrocinador controla conteúdo | perda de independência |
| empresa financia participante | vigilância ou coerção |
| parceiro oferece e audita recompensa | emissão indevida |
| maior comissão influencia oferta | priorização inadequada |
| exclusividade elimina alternativas | redução de autonomia |
| tecnologia reutiliza dados | finalidade incompatível |
| parceiro acumula vários papéis | concentração de poder |
| dois canais reivindicam atribuição | remuneração duplicada |
| desconto fictício | benefício enganoso |
| organização social expõe beneficiários | exploração promocional |

## 6. Registro de conflito

```yaml
partner_conflict_id: string
relationship_id: string
conflict_type: string
affected_actors:
  - string
risk: string
disclosure:
  - string
preventive_controls:
  - string
monitoring:
  - string
interruption_conditions:
  - string
owner: string
status: open
```

## 7. Exclusividade

Uma exclusividade futura exigirá:

- justificativa legítima;
- duração e escopo limitados;
- análise de alternativas;
- impacto sobre participantes;
- risco de concentração;
- condição de saída;
- validação especializada.

Não será aprovada neste ciclo.

## 8. Patrocínio e conteúdo

Patrocinador poderá financiar produção ou distribuição, mas não deverá:

- alterar fatos;
- ocultar riscos;
- remover críticas legítimas;
- controlar evidência;
- exigir recomendação;
- expor beneficiários sem consentimento.

## 9. Fora do escopo

- algoritmo de ranking;
- inventário publicitário;
- contrato;
- comissão;
- exclusividade real;
- operação.
