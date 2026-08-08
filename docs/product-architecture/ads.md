---
id: GPA-007
title: Guivos Ads
status: consolidated
version: 1.3.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GEM-007-ADS-ECONOMIC-ROLE-001
  - GEM-007-A1
  - UXA-038
  - UXA-099
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
---

# Guivos Ads

## Papel

Guivos Ads é o produto responsável pela publicidade, mídia patrocinada e soluções para anunciantes dentro do Ecossistema Guivos.

## Escopo principal

- campanhas publicitárias;
- mídia patrocinada;
- formatos nativos identificados;
- ativações de marca;
- patrocínios;
- segmentação permitida;
- mensuração de campanhas;
- soluções para anunciantes e parceiros;
- Opportunity Boost.

## Opportunity Boost

O Opportunity Boost é o mecanismo de distribuição patrocinada de oportunidades, atividades e programas já amplamente materializado na Arquitetura da Experiência.

Sua responsabilidade inclui receber configuração e orçamento, avaliar elegibilidade publicitária, distribuir somente em inventário patrocinado permitido, identificar a natureza comercial, limitar frequência e orçamento, medir eventos válidos, remover tráfego inválido e permitir pausa, cancelamento e reconciliação.

## Integração vigente com as jornadas

O baseline atual registra cinco famílias comerciais:

- `COM-001` — configuração do anunciante;
- `COM-002` — cartão patrocinado e explicação;
- `COM-003` — estados patrocinados de lista/mapa;
- `COM-004` — gestão de campanha ativa e relatórios;
- `COM-005` — dez estados residuais, validados especificamente pela UXA-099.

As galerias canônicas de Opportunity Boost reúnem **46 SVGs**: 20 de configuração/exposição e 26 de operação, relatórios e estados residuais.

A continuidade com o contexto orgânico ainda não está integralmente fechada:

- `TRN-304` — Ads → Mapa Journey: parcial;
- `TRN-305` — campanha → estado residual: parcial, embora `COM-005` esteja validado;
- `TRN-306` — Ads → Lista Journey: parcial.

`TRN-301` e `TRN-302` também permanecem parciais; `TRN-303` está localmente validada.

O mapeamento completo está na [Matriz de Integração dos Produtos com as Jornadas](specialized-products-journey-integration-matrix.md).

## Limites

Guivos Ads não substitui Journey, Mall, Travel, Business, Media ou Intelligence.

O produto não poderá comprar relevância orgânica, alterar Próximo Passo pessoal, utilizar compreensão protegida para segmentação, transformar pagamento em recomendação, conceder ao anunciante acesso indevido ao participante ou prometer conversão/impacto.

## Relações principais

- Journey preserva relevância orgânica e controles pessoais;
- Business preserva identidade e responsabilidade institucional do anunciante quando aplicável;
- Intelligence apoia mensuração agregada sem segmentação sensível;
- Mall e Travel preservam transação ou reserva quando aplicável;
- a superfície anfitriã preserva contexto, acessibilidade e segurança.

## Regra de representação

A natureza patrocinada deve ser perceptível sempre que material. Ads não precisa dominar visualmente a superfície, mas relação comercial, responsável, controles e separação do orgânico não podem ser ocultados.

A regra completa está em [Política de Representação e Handoffs entre Produtos](specialized-products-experience-and-handoff-policy.md).

## Estado

**Opportunity Boost está conceitualmente definido e amplamente materializado/validado em seus artefatos de experiência.**

Permanecem incompletas as ligações ponta a ponta indicadas no registro de transições e a implementação técnica/operacional real. Materialização e validação documental não equivalem a implementação.
