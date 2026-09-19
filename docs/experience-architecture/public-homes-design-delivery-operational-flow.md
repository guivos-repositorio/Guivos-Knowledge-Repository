---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 3.0.0
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-SOURCE-READINESS-REMEDIATION-001
related:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
normative: false
maturity: tool_agnostic_manual_first_source_readiness_flow
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa como a designer deve consumir o pacote documental das oito Homes públicas e como sistemas de IA podem ser utilizados opcionalmente como apoio.

Ele **não** exige Figma Make, protótipo gerado por IA, arquivo preliminar ou qualquer ferramenta específica antes da criação manual.

```text
DESIGNER HUMANA
→ EXECUTORA CRIATIVA PRINCIPAL

IA
→ APOIO OPCIONAL

GKR
→ FONTE GOVERNADA DE SIGNIFICADO / FUNÇÃO / LIMITES / FATOS

FERRAMENTA ESPECÍFICA
→ NÃO OBRIGATÓRIA
```

## 2. Gate de início

A execução externa somente deve começar quando existir pacote documental vigente, validado e explicitamente liberado para uso externo.

O snapshot v5 permanece histórico e congelado. Esta remediação prepara uma nova baseline de fontes antes de nova emissão.

O gate de início não autoriza Product Engineering, publicação ou implementação.

## 3. Isolamento de contexto

Trabalhar uma Home por vez.

O contexto inicial deve conter:

1. autoridades comuns vigentes;
2. `LEIA-PRIMEIRO / SOURCE LOCK` da Home;
3. Documento Mestre da Home;
4. somente autoridades específicas daquela Home necessárias à execução;
5. referências adicionais apenas quando declaradas e justificadas.

Não carregar indiscriminadamente todo o GKR ou documentos específicos de múltiplas Homes.

## 4. Fase A — compreensão humana obrigatória

Antes de criar, a designer deve:

1. ler o `LEIA-PRIMEIRO`;
2. compreender o Handoff comum;
3. ler o Documento Mestre;
4. ler contratos/source locks específicos aplicáveis;
5. identificar:
   - `CANONICAL`;
   - `DESIGN_CREATIVE`;
   - `CONTENT_CANDIDATE`;
   - `DESIGN_HYPOTHESIS`;
   - `PROTOTYPE_PLACEHOLDER`;
   - `REAL_DATA_REQUIRED`;
   - `OPEN_QUESTION`;
   - `PROHIBITED_INFERENCE`;
6. registrar dúvida material em vez de preencher lacuna semanticamente.

## 5. Fase B — criação livre da designer

Depois da compreensão humana, a designer pode criar manualmente sua direção usando as ferramentas que considerar adequadas.

Podem ser definidos livremente:

- tipografia;
- paleta;
- direção de arte;
- fotografia;
- vídeo;
- ilustração;
- iconografia;
- composição;
- grid;
- ritmo;
- respiro;
- motion;
- componentes;
- linguagem gráfica;
- atmosfera;
- responsividade;
- microcopy e tom não congelados.

A designer não é obrigada a:

- usar Figma Make;
- usar IA;
- gerar protótipo automatizado;
- seguir benchmark visual;
- reproduzir identidade histórica;
- usar template pré-existente;
- transformar movimentos narrativos em quantidade fixa de seções.

## 6. Caminho opcional — sistemas de IA

Se a designer decidir usar IA, o uso deve ser subordinado ao mesmo Source Lock.

A IA pode apoiar:

- exploração de alternativas;
- ideação de composição;
- copy candidata;
- variações responsivas;
- hipóteses visuais;
- análise de consistência;
- autoauditoria;
- documentação auxiliar.

A IA não pode:

- redefinir a Home;
- criar produto ou funcionalidade;
- transformar questão aberta em decisão;
- inventar dado, parceiro, preço, disponibilidade, métrica ou prova;
- promover hipótese a `CANONICAL`;
- impor direção artística à designer.

Todo output de IA começa como material não canônico e sujeito à decisão humana da designer e da Guivos.

## 7. Revisão humana da direção

A revisão deve avaliar:

- fidelidade semântica;
- clareza;
- criatividade e originalidade;
- autonomia da Pessoa;
- fronteiras entre participantes e produtos;
- conteúdo candidato;
- responsividade;
- acessibilidade;
- estados;
- dados e provas;
- hipóteses introduzidas;
- compatibilidade entre liberdade criativa e verdade governada.

A direção pode ser:

```text
APROVADA
→ pode continuar para refinamento e entrega final

APROVADA COM AJUSTES
→ ajustes obrigatórios registrados

REJEITADA
→ designer retorna à criação sem perda de liberdade criativa
```

## 8. Entrega final de Design

A entrega final deve refletir a direção aprovada e permanecer fiel aos contratos documentais.

A ferramenta concreta de Design — Figma ou equivalente adotado no contrato — é decisão operacional da frente de Design, não requisito ontológico do GKR.

Quando Figma for a ferramenta contratada, o arquivo final deve atender aos requisitos de editabilidade, controle, assets, licenças, componentes, responsividade, acessibilidade e continuidade definidos pela autoridade de prontidão vigente.

## 9. Aceite final

O aceite deve registrar, no mínimo:

- Home(s) entregues;
- artefato/arquivo e versão avaliados;
- data;
- responsável humano pelo aceite;
- checklist de produção concluído;
- assets/fontes/plugins/licenças documentados quando aplicável;
- pendências inexistentes ou classificadas;
- confirmação de controle/acesso da Guivos aos artefatos essenciais;
- status final `DESIGN FINAL ACEITO`.

```text
DESIGN FINAL ACEITO
≠ IMPLEMENTAÇÃO
≠ PRODUCT ENGINEERING RELEASE
```

## 10. Regra de mudança

Se uma decisão semântica mudar depois do Source Lock:

1. interromper somente a Home afetada;
2. reconciliar impacto;
3. atualizar autoridades;
4. revalidar o pacote;
5. emitir novo checkpoint se a mudança for material.

Melhoria puramente criativa pode ocorrer sem reemissão desde que não altere contrato semântico.

## 11. Estados

```text
PACOTE FONTE PRONTO
→ documentação suficiente e validada

CRIAÇÃO EM DESIGN
→ trabalho criativo em curso

DIREÇÃO EM REVISÃO
→ proposta submetida à Guivos

DIREÇÃO APROVADA
→ direção humana selecionada

DESIGN FINAL CANDIDATO
→ entrega final em avaliação

DESIGN FINAL ACEITO
→ entrega de Design aceita
```

## 12. Estado desta autoridade

```text
FLOW
→ v3.0.0

OPERATING MODEL
→ MANUAL-FIRST
→ AI-OPTIONAL
→ TOOL-AGNOSTIC

FIGMA MAKE
→ NOT REQUIRED

NEW SOURCE PACKAGE
→ UNDER REMEDIATION

PRODUCT ENGINEERING
→ NOT RELEASED
```