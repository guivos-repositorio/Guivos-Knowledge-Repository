---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 2.0.0
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
normative: false
maturity: post_audit_v5_operational_flow_pre_release
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa como a designer deve consumir o pacote v5, usar Figma Make para prototipação e somente depois construir o Figma definitivo.

## 2. Gate de início

Não iniciar execução enquanto faltar qualquer item:

- snapshot v5 materializado e validado;
- Source Lock operacional da Home;
- Design Production Release humano explícito.

## 3. Isolamento de contexto

Trabalhar uma Home por vez. Carregar `00-COMUM`, o `00-LEIA-PRIMEIRO` da Home e somente suas fontes específicas.

## 4. Fase A — compreensão humana

Antes de gerar:

1. ler o guia da Home;
2. ler Handoff e contrato de prontidão;
3. ler Master/autoridades específicas;
4. identificar `CANONICAL`, `DESIGN CREATIVE`, `CONTENT CANDIDATE`, `PROTOTYPE PLACEHOLDER`, `REAL DATA REQUIRED` e `PROHIBITED INFERENCE`.

## 5. Fase B — Figma Make / protótipo exploratório

A ferramenta recebe ampla liberdade visual e nenhum direito de redefinir a Guivos.

Output: `EXPLORAÇÃO / NÃO CANÔNICA`.

A designer pode iterar, combinar ou rejeitar propostas da ferramenta.

## 6. Fase C — revisão humana obrigatória

Revisar:

- fidelidade semântica;
- clareza e experiência;
- criatividade/originalidade;
- conteúdo candidato;
- responsividade;
- acessibilidade;
- estados;
- dados/provas;
- hipóteses introduzidas.

Registrar o que foi aceito, rejeitado e o que precisa ser resolvido.

Sem aprovação humana da direção, não iniciar construção definitiva.

## 7. Fase D — Figma definitivo

A direção aprovada pode ser refinada livremente pela designer, preservando contratos.

A solução criativa aprovada deve ser documentada no arquivo: tipografia, cores, estilos, componentes, assets e regras necessárias para consistência e handoff.

Essas foundations são consequência do Design, não baseline pré-imposta.

## 8. Fase E — aceite final

Executar o checklist de `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001`.

Estados:

- `EXPLORAÇÃO`;
- `PROTÓTIPO CANDIDATO`;
- `DIREÇÃO APROVADA`;
- `FIGMA FINAL CANDIDATO`;
- `FIGMA FINAL ACEITO`.

`FIGMA FINAL ACEITO` não equivale a implementação, produção ou Product Engineering.

## 9. Regra de mudança após aprovação

Se uma decisão semântica mudar depois do Source Lock, interromper a Home afetada, reconciliar o impacto e emitir novo checkpoint quando material.

Uma melhoria puramente criativa que não altera contrato pode ocorrer dentro do processo de Design e ser consolidada no Figma final.

## 10. Estado

`FLOW v2 READY / EXECUTION NOT RELEASED UNTIL V5 SNAPSHOT + HUMAN DESIGN PRODUCTION RELEASE`.
