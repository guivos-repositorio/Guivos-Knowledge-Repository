---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 2.0.1
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
normative: false
maturity: post_audit_v5_operational_flow_release_granted_pre_execution
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa como a designer deve consumir o pacote v5, usar Figma Make para prototipação e somente depois construir o Figma definitivo.

## 2. Gate de início

O gate de início foi satisfeito. A execução pode começar somente dentro deste fluxo, porque coexistem:

- snapshot v5 materializado e validado;
- Source Lock operacional da Home;
- `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.0.0 = GRANTED`.

A autorização de início não elimina os gates internos de revisão humana, direção criativa aprovada e aceite final.

## 3. Isolamento de contexto

Trabalhar uma Home por vez. Carregar `00-COMUM`, o `00-LEIA-PRIMEIRO` da Home e somente suas fontes específicas.

## 4. Fase A — compreensão humana

Antes de gerar:

1. ler o guia da Home;
2. ler Handoff e contrato de prontidão;
3. ler Master/autoridades específicas;
4. identificar `CANONICAL`, `DESIGN_CREATIVE`, `CONTENT_CANDIDATE`, `DESIGN_HYPOTHESIS`, `PROTOTYPE_PLACEHOLDER`, `REAL_DATA_REQUIRED`, `OPEN_QUESTION` e `PROHIBITED_INFERENCE`.

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

A aprovação da direção deve deixar um registro mínimo contendo:

- Home;
- versão/link ou identificador inequívoco do protótipo avaliado;
- data;
- responsável humano pela aprovação;
- direção selecionada;
- decisões criativas aceitas;
- conteúdo candidato aprovado/rejeitado;
- placeholders e dados reais ainda necessários;
- questões abertas não bloqueadoras;
- status final `DIREÇÃO APROVADA`.

Sem esse registro e sem aprovação humana da direção, não iniciar construção definitiva.

## 7. Fase D — Figma definitivo

A direção aprovada pode ser refinada livremente pela designer, preservando contratos. Alteração material da direção aprovada — como conceito de Hero, linguagem visual, arquitetura de navegação, composição global ou mudança equivalente — retorna ao gate humano antes do aceite final.

A solução criativa aprovada deve ser documentada no arquivo: tipografia, cores, estilos, componentes, assets e regras necessárias para consistência e handoff.

Essas foundations são consequência do Design, não baseline pré-imposta.

## 8. Fase E — aceite final

Executar o checklist de `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001`, incluindo continuidade de fontes/plugins/assets, controle do arquivo pela Guivos e revisão integrada das oito Homes.

O aceite final deve registrar, no mínimo:

- Home(s) entregues;
- arquivo Figma e versão avaliada;
- data;
- responsável humano pelo aceite;
- checklist de produção concluído;
- assets/fontes/plugins/licenças entregues ou documentados;
- pendências inexistentes ou explicitamente classificadas como não bloqueadoras;
- confirmação de controle/acesso da Guivos aos arquivos essenciais;
- status `FIGMA FINAL ACEITO`.

A conclusão operacional do serviço de Design deve ocorrer **depois** desse aceite. Condições financeiras e jurídicas permanecem no instrumento contratual aplicável, mas o GKR não considera a entrega concluída antes de `FIGMA FINAL ACEITO`.

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

`FLOW v2.0.1 READY / DESIGN PRODUCTION RELEASE GRANTED / FIGMA MAKE AUTHORIZED TO EXECUTE / NOT_STARTED / FINAL FIGMA REQUIRES HUMAN DIRECTION APPROVAL`.
