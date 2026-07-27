---
id: GKR-CHANGELOG-1.50.0
status: active
version: 1.50.0
owner: Guivos
last_updated: 2026-07-27
related:
  - UXA-026
  - UXA-027
  - GKR-CANON-MATRIX-UXA-027
  - M7.28
normative: false
---

# Histórico de Alterações 1.50.0 — UXA-027

## Resumo

Validação funcional especializada e reformulação do estado do Mapa de Oportunidades com localização desativada.

## Resultado

O estado é considerado **funcionalmente válido após reformulação**.

## Alterações principais

- criada a UXA-027;
- UXA-026 atualizada para versão 0.2.0 e estado ativo;
- wireframe vetorial reformulado;
- adicionada confirmação `Posição não acessada`;
- região manual diferenciada da posição pessoal;
- salvamento demonstrado no cartão;
- origem manual para rota demonstrada;
- ativação de localização aproximada marcada como opcional;
- estado global elevado ao marco M7.28;
- roadmap, painel, marcos, programa de wireframes, navegação e páginas de entrada atualizados.

## Proteções

- localização não se torna requisito universal;
- recusa de permissão não bloqueia busca, Mapa, Lista, Detalhe ou salvamento;
- região manual não é interpretada como posição atual;
- salvamento não autoriza rastreamento;
- rota não inicia sem origem válida;
- linguagem personalizada permanece bloqueada sem gate;
- endereços protegidos não são contornados.

## Fora de escopo

- tecnologia cartográfica;
- coordenadas e geocodificação;
- rotas reais;
- versão para computador;
- design visual;
- protótipo navegável;
- teste de usabilidade;
- Engenharia de Produto.
