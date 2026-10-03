---
id: GEM-004-ELIGIBILITY-FUNDED-ACCESS-001
title: Elegibilidade e Acesso Financiado
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-004
---

# Elegibilidade e Acesso Financiado

## 1. Objetivo

Definir critérios conceituais para atribuição de acesso gratuito, pago, organizacional, patrocinado, social, profissional ou híbrido, preservando transparência, equidade, privacidade e limites de autoridade.

## 2. Princípios

1. elegibilidade deverá ser objetiva e compreensível;
2. financiador e beneficiário serão papéis distintos;
3. financiamento não concede autoridade automática;
4. condição do beneficiário será protegida;
5. término do financiamento deverá preservar o gratuito;
6. critérios não poderão explorar vulnerabilidade;
7. acesso deverá ser revogável e auditável;
8. dados serão minimizados;
9. exceções materiais exigirão justificativa;
10. nenhuma regra é implementada por este documento.

## 3. Critérios candidatos

A elegibilidade poderá considerar:

- tipo de ator;
- produto ou programa;
- organização vinculada;
- grupo autorizado;
- território;
- idade ou capacidade legal, quando aplicável;
- requisito de segurança;
- disponibilidade operacional;
- capacidade contratada futura;
- convite legítimo;
- status do parceiro;
- necessidade de serviço especializado;
- participação em programa social;
- duração de patrocínio;
- critérios objetivos de benefício.

## 4. Fontes de financiamento

### Gratuito estrutural

Financiado pela sustentabilidade geral e reinvestimento do ecossistema.

### Pagamento individual

A pessoa paga pela ampliação e também recebe o benefício principal.

### Organização financiadora

Empresa ou instituição paga para pessoas ou grupos elegíveis.

### Patrocinador

Ator financia acesso, experiência, conteúdo ou benefício com retorno transparente e limitado.

### Programa social ou recurso vinculado

Recurso destinado a grupo, causa ou finalidade específica.

### Parceiro ou profissional

Ator financia acesso próprio a ferramentas e capacidades proporcionais ao papel.

### Híbrido

Combinação transparente de fontes, sem cobrança duplicada oculta.

## 5. Registro mínimo

```yaml
eligibility_rule_id: string
access_archetype: string
beneficiary_type: string
funding_source: string
payer: string | null
criteria:
  - string
duration: string | null
renewal_condition: string | null
data_required:
  - string
funder_access_limits:
  - string
termination_effect: string
free_continuity: true
appeal_available: true
status: candidate
```

## 6. Acesso financiado por organização

Deverão ser explícitos:

- objetivo do programa;
- capacidades financiadas;
- pessoas elegíveis;
- período;
- dados acessíveis à organização;
- relatórios permitidos;
- direito de recusa quando aplicável;
- efeito do desligamento ou término;
- continuidade no gratuito;
- forma de contestação.

A organização não poderá:

- acessar contexto pessoal sem finalidade e autoridade legítimas;
- utilizar o plano para vigilância;
- alterar evidências individuais;
- condicionar direitos básicos ao vínculo;
- punir recusa de forma incompatível;
- manter acesso após término sem fundamento.

## 7. Acesso patrocinado ou social

Deverão ser registrados:

- fonte econômica;
- finalidade;
- grupo beneficiário;
- executor;
- duração;
- retorno permitido ao financiador;
- divulgação do patrocínio;
- dados compartilhados;
- independência da Guivos;
- término e transição.

A condição social ou econômica do beneficiário não poderá ser exposta além do necessário.

## 8. Elegibilidade proibida ou condicionada

Não será admissível usar para exploração ou pressão:

- doença;
- medo;
- solidão;
- fé;
- sofrimento emocional;
- vulnerabilidade financeira;
- urgência artificial;
- pontuação como valor humano;
- condição social exposta desnecessariamente;
- dado sensível sem finalidade legítima.

Critérios sensíveis poderão existir apenas quando necessários para proteção, acessibilidade ou benefício legítimo, com governança reforçada.

## 9. Contestação e correção

Toda decisão material de elegibilidade deverá possuir, futuramente:

- razão compreensível;
- fonte dos dados;
- possibilidade de correção;
- canal de contestação;
- revisão humana quando necessária;
- registro da decisão;
- tratamento de erro;
- prazo proporcional.

## 10. Encerramento do financiamento

O término deverá:

- ser comunicado;
- preservar dados e direitos;
- indicar capacidades afetadas;
- permitir exportação;
- preservar acesso gratuito;
- evitar exclusão abrupta;
- remover acessos do financiador;
- permitir novo financiamento ou upgrade futuro.

## 11. Fora do escopo

- critérios finais por programa;
- contratos;
- preços;
- subsídios monetários;
- seleção de patrocinadores;
- operação de benefícios;
- implementação.
