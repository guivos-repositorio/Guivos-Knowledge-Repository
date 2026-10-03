---
id: GEM-003
title: Arquitetura de Receitas
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-000
depends_on:
  - GEM-002
  - GEM-002-DEPENDENCY-VALIDATION-CHECKPOINT-001
related:
  - GEM-003-REVENUE-FAMILY-CATALOG-001
  - GEM-003-REVENUE-FAMILY-CONTRACT-001
  - GEM-003-DISCLOSURE-CONFLICT-POLICY-001
  - M6.2
---

# GEM-003 — Arquitetura de Receitas

## 1. Objetivo

Definir as famílias de receita economicamente admissíveis para o Ecossistema Guivos, estabelecendo pagadores, beneficiários, recebedores, eventos econômicos, bases de cobrança candidatas, conflitos, disclosures, condições de validação e interrupção.

## 2. Pergunta arquitetural

> Quais formas de receita são compatíveis com o valor gerado pela Guivos, quem paga por esse valor, em quais condições a captura é legítima e quais limites impedem que a monetização comprometa propósito, autonomia, confiança ou sustentabilidade?

## 3. Sequência de referência

```text
valor realizado ou capacidade legitimamente disponibilizada
→ contraprestação compreensível
→ mecanismo de receita transparente
→ captura proporcional
→ compartilhamento aplicável
→ reinvestimento responsável
```

Não é admissível tratar atenção, vulnerabilidade, dados pessoais ou influência oculta como atalhos de monetização.

## 4. Conceitos

### Família de receita

Categoria estável que agrupa mecanismos com natureza econômica, pagadores, eventos geradores, bases de cobrança, riscos e regras de governança semelhantes.

### Mecanismo de receita

Aplicação específica de uma família a produto, segmento, oferta ou relação econômica.

### Pagador

Ator que assume a obrigação econômica.

### Beneficiário

Ator que recebe o benefício principal. Poderá ser diferente do pagador.

### Recebedor econômico

Ator que recebe parcela do fluxo financeiro.

### Evento econômico

Fato que poderá originar, alterar, suspender, reverter ou encerrar obrigação econômica.

### Base de cobrança

Unidade ou referência futura de cálculo da contraprestação.

### Disclosure econômico

Informação necessária para tornar compreensíveis pagamento, recebedores, comissão, patrocínio, influência, dados, renovação, cancelamento e conflitos.

## 5. Separações canônicas

- valor total transacionado não é receita da Guivos;
- reserva não é receita reconhecida;
- caixa recebido não é receita definitiva;
- receita bruta não é receita líquida;
- receita não é margem;
- margem não é lucro;
- lucro não é sustentabilidade;
- repasse não é receita integral;
- investimento, dívida e aporte não são receita operacional;
- pontos, créditos e cashback não são receita;
- audiência não é consentimento;
- clique não é valor comprovado;
- pagamento não concede autoridade;
- comissão não torna recomendação neutra.

## 6. Famílias iniciais

1. RF-01 — acesso recorrente e assinatura;
2. RF-02 — intermediação comercial;
3. RF-03 — soluções B2B;
4. RF-04 — serviços profissionais;
5. RF-05 — licenciamento e uso de tecnologia;
6. RF-06 — publicidade e mídia;
7. RF-07 — patrocínio e ativação de marca;
8. RF-08 — conteúdo, produção e propriedade intelectual;
9. RF-09 — ferramentas e serviços para parceiros;
10. RF-10 — distribuição, indicação e afiliação;
11. RF-11 — Intelligence, analytics e insights autorizados;
12. RF-12 — infraestrutura, integração e operação.

## 7. Requisitos mínimos de admissibilidade

Uma família somente poderá avançar quando:

1. houver referência explícita ao fluxo de valor;
2. pagador, beneficiário e recebedor estiverem identificados;
3. a contraprestação for compreensível;
4. eventos econômicos e reversões estiverem definidos;
5. custos, riscos e repasses forem reconhecidos;
6. dados e autoridades envolvidos forem explícitos;
7. conflitos e disclosures forem tratados;
8. impacto sobre o gratuito for avaliado;
9. contestação, cancelamento e reparação forem possíveis;
10. hipóteses e evidências de validação estiverem registradas.

## 8. Estados

- `candidate`;
- `conceptually_admissible`;
- `validation_required`;
- `approved_for_test`;
- `suspended`;
- `rejected`;
- `retired`.

`Conceptually_admissible` não equivale a preço, contrato, faturamento ou autorização operacional.

## 9. Limites desta versão

O GEM-003 não define:

- preços;
- percentuais;
- comissões específicas;
- margens;
- planos finais;
- descontos;
- metas de faturamento;
- unit economics;
- tratamento tributário;
- reconhecimento contábil;
- parceiros específicos;
- meios de pagamento;
- implementação.

## 10. Critérios de conclusão

- linguagem e separações definidas;
- doze famílias catalogadas;
- pagadores, beneficiários e recebedores mapeados;
- eventos e bases de cobrança catalogados;
- contrato canônico publicado;
- disclosures e conflitos definidos;
- concentração e resiliência classificadas;
- framework de validação estabelecido;
- oito cenários e treze gates documentados;
- pendências do GEM-004 explícitas.
