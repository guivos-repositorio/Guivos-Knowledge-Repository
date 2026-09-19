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
related:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-HOMES-DESIGN-INPUT-HARDENING-V6-001
normative: false
maturity: human_first_ai_optional_design_flow
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa como a designer deve consumir o pacote documental das Homes públicas e transformá-lo em Design.

O fluxo é **human-first**:

```text
PACOTE GOVERNADO
↓
COMPREENSÃO HUMANA
↓
CRIAÇÃO DA DESIGNER
↓
IA OPCIONAL, QUANDO ÚTIL
↓
REVISÃO HUMANA
↓
REFINAMENTO / ENTREGA FINAL
↓
ACEITE
```

Nenhuma ferramenta específica de prototipação, geração ou edição é etapa obrigatória.

## 2. Gate de início

O gate de Design Production Release foi concedido. A execução externa de Design pode começar quando a Home possuir um pacote vigente e validado.

O início não elimina:

- revisão humana;
- necessidade de preservar a verdade documental;
- validação de dados, claims, parceiros, preços e disponibilidade;
- aceite final do serviço de Design.

## 3. Isolamento de contexto

Trabalhar uma Home por vez.

A designer deve iniciar por:

1. guia `LEIA-PRIMEIRO` da Home;
2. Documento Mestre da Home;
3. autoridades comuns;
4. somente as fontes específicas necessárias para aprofundar dúvidas ou fronteiras.

Não carregar indiscriminadamente documentos das oito Homes em uma mesma sessão de trabalho.

## 4. Fase A — compreensão humana

Antes de desenhar:

1. compreender papel, público, tese e pergunta-mãe/princípio equivalente;
2. compreender movimentos narrativos e hierarquia de ação;
3. compreender participantes, Produtos Especializados e fronteiras;
4. identificar fatos que exigem dado real;
5. identificar questões deliberadamente abertas;
6. identificar inferências proibidas;
7. distinguir:
   - `CANONICAL`;
   - `DESIGN_CREATIVE`;
   - `CONTENT_CANDIDATE`;
   - `DESIGN_HYPOTHESIS`;
   - `PROTOTYPE_PLACEHOLDER`;
   - `REAL_DATA_REQUIRED`;
   - `OPEN_QUESTION`;
   - `PROHIBITED_INFERENCE`.

A designer não precisa reconstruir a história do GKR para compreender a Home.

## 5. Fase B — criação da designer

A criação é manual e livre dentro das fronteiras semânticas.

Pertencem à designer, salvo decisão literal congelada:

- identidade visual;
- tipografia;
- paleta;
- fotografia, ilustração e imagem;
- composição;
- grid;
- ritmo;
- densidade;
- iconografia;
- motion;
- microinterações;
- aparência de componentes;
- linguagem gráfica;
- atmosfera;
- solução responsiva;
- agrupamento físico dos movimentos;
- copy e tom classificados como candidatos.

```text
LIBERDADE DE DESIGN
≠ REDEFINIÇÃO DE PRODUTO
≠ INVENÇÃO FACTUAL
```

## 6. Fase C — uso opcional de IA

IA pode ser usada pela designer para:

- explorar alternativas;
- testar composições;
- gerar referências;
- apoiar copy candidata;
- organizar hipóteses;
- acelerar tarefas operacionais.

Se usada, deve consumir o **mesmo pacote governado**.

```text
IA
→ FERRAMENTA OPCIONAL

OUTPUT DE IA
→ NÃO CANÔNICO POR PADRÃO

PROMPT
→ ADAPTADOR DO PACOTE
→ NÃO NOVA AUTORIDADE
```

A ausência de uso de IA não reduz a validade da entrega.

## 7. Fase D — revisão humana da direção

Revisar:

- fidelidade semântica;
- clareza da experiência;
- criatividade e originalidade;
- hierarquia de informação;
- responsividade;
- acessibilidade;
- conteúdo candidato;
- placeholders;
- dados/provas;
- hipóteses introduzidas;
- coerência com a família Guivos sem uniformização artificial.

A revisão deve distinguir:

```text
ERRO SEMÂNTICO
→ CORRIGIR

DIVERGÊNCIA CRIATIVA
→ AVALIAR HUMANAMENTE

PREFERÊNCIA ESTÉTICA
→ NÃO RECLASSIFICAR COMO REGRA DO GKR
```

## 8. Fase E — refinamento e entrega final da designer

A direção escolhida pode ser refinada pela designer até a entrega final.

A solução final deve documentar no ambiente de Design escolhido o necessário para continuidade profissional, quando aplicável:

- foundations criadas;
- componentes;
- assets;
- estados;
- regras responsivas;
- comportamento;
- fontes/licenças;
- dependências;
- anotações de handoff.

Esses elementos são consequência da criação da designer, não inputs canônicos pré-impostos pelo GKR.

## 9. Fase F — aceite final

O aceite final deve comprovar:

- aderência aos documentos governados;
- ausência de redefinição indevida de produto;
- ausência de claims inventados;
- responsividade;
- acessibilidade;
- integridade dos assets e dependências;
- entrega dos arquivos acordados contratualmente;
- pendências inexistentes ou explicitamente não bloqueadoras.

O formato final pode estar em Figma ou outra ferramenta definida no contrato de Design. O GKR não exige ferramenta específica.

```text
DESIGN FINAL ACEITO
≠ IMPLEMENTAÇÃO
≠ PRODUCT ENGINEERING RELEASE
```

## 10. Regra de mudança após o handoff

Se a **verdade semântica** mudar depois do Source Lock/pacote emitido:

1. interromper a parte afetada;
2. reconciliar o GKR;
3. avaliar impacto;
4. emitir novo checkpoint quando material.

Melhoria puramente criativa não exige mudança do GKR.

## 11. Estado

```text
FLOW v3.0.0
→ HUMAN-FIRST
→ MANUAL DESIGN = PRIMARY PATH
→ AI = OPTIONAL
→ TOOL REQUIREMENT = NONE
→ VISUAL IDENTITY = DESIGN-OWNED
→ PRODUCT ENGINEERING = NOT RELEASED
```
