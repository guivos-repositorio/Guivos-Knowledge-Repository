---
id: GEM-005-INCENTIVE-FAMILY-CATALOG-001
title: Catálogo de Famílias de Incentivo
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Catálogo de Famílias de Incentivo

## 1. Objetivo

Organizar famílias estáveis para progresso, reconhecimento e recompensa, permitindo comparação, governança e validação sem aprovar programas operacionais.

## 2. IF-01 — Progresso e Marcos

Reconhece avanço em jornada, objetivo, aprendizagem ou experiência.

Exemplos candidatos:

- conclusão de etapa;
- marco de objetivo;
- participação continuada;
- aprendizagem registrada.

Limites:

- não apagar histórico por inatividade;
- não exigir gasto;
- não criar obrigação diária artificial;
- não representar valor humano;
- não gerar recompensa econômica automática.

## 3. IF-02 — Reconhecimento Simbólico

Registra contribuição ou participação sem valor econômico direto.

Exemplos candidatos:

- selo;
- certificado;
- agradecimento;
- credencial contextual;
- destaque editorial.

Limites:

- critério e fonte explícitos;
- não comercialização;
- contexto e validade claros;
- correção disponível;
- não representar reputação universal.

## 4. IF-03 — Pontos de Recompensa

Unidades acumuláveis com possibilidade futura de resgate em benefícios definidos.

Dependências:

- fonte de financiamento;
- regra de emissão;
- saldo rastreável;
- validade;
- catálogo ou benefício;
- resgate;
- reversão;
- controles contra duplicidade.

Nenhuma quantidade ou taxa de conversão é definida nesta versão.

## 5. IF-04 — Descontos e Condições Especiais

Benefícios comerciais oferecidos pela Guivos ou parceiros.

Exemplos candidatos:

- desconto;
- isenção promocional;
- tarifa especial;
- condição de compra;
- acesso temporário.

Limites:

- preço de referência legítimo;
- ausência de desconto fictício;
- prazo e disponibilidade compreensíveis;
- responsabilidade do fornecedor;
- nenhuma compra adicional oculta.

## 6. IF-05 — Produtos, Serviços e Experiências

Recompensa material ou experiencial.

Exemplos candidatos:

- produto;
- curso;
- consulta;
- ingresso;
- viagem;
- serviço profissional.

Limites:

- disponibilidade;
- qualidade;
- segurança;
- responsabilidade;
- cancelamento e substituição;
- dados mínimos para entrega.

## 7. IF-06 — Acesso e Capacidade

Liberação de capacidade não essencial.

Exemplos candidatos:

- módulo adicional;
- período ampliado;
- integração;
- suporte adicional;
- capacidade extra.

Limites:

- não bloquear valor essencial;
- início e encerramento claros;
- retorno ao gratuito;
- nenhuma cobrança automática após o benefício.

## 8. IF-07 — Incentivos Patrocinados

Recompensa financiada por patrocinador, organização ou parceiro.

Limites:

- financiador identificado;
- finalidade declarada;
- recursos vinculados;
- independência da Guivos;
- acesso limitado a dados;
- ausência de controle sobre evidências.

## 9. IF-08 — Incentivos Sociais e Comunitários

Reconhecimento ou recompensa por contribuição a causas, comunidades e voluntariado.

Limites:

- organização responsável verificada;
- contribuição e impacto separados;
- proteção das pessoas beneficiárias;
- segurança da atividade;
- ausência de competição sobre vulnerabilidade;
- eventual recompensa com fonte identificada.

## 10. IF-09 — Doação ou Direcionamento de Benefício

Permite direcionar recompensa para causa, organização ou pessoa elegível.

Limites:

- consentimento;
- finalidade;
- rastreabilidade;
- destinatário verificado;
- transparência sobre retenções futuras;
- ausência de apropriação indevida.

## 11. IF-10 — Incentivos Organizacionais

Benefícios oferecidos por empresas e instituições.

Exemplos candidatos:

- capacitação;
- voluntariado empresarial;
- reconhecimento interno;
- benefício corporativo;
- participação em programa.

Limites:

- participação voluntária quando aplicável;
- ausência de vigilância;
- dados individuais protegidos;
- não punição automática por não participação;
- término do vínculo com transição clara.

## 12. Registro mínimo de família

```yaml
incentive_family_id: string
name: string
layer:
  progress |
  recognition |
  economic_reward
purpose: string
eligible_events:
  - string
beneficiaries:
  - string
funding_required: boolean
evidence_required:
  - string
risks:
  - string
prohibited_outcomes:
  - string
status: conceptually_defined
```

## 13. Regra de classificação

Um programa poderá combinar famílias, mas deverá registrar separadamente:

- a função de cada família;
- o evento correspondente;
- a evidência;
- o financiador;
- o benefício;
- a responsabilidade;
- o ciclo de vida.

## 14. Fora do escopo

- programas comerciais;
- quantidade de pontos;
- preços;
- catálogo operacional;
- parceiros específicos;
- implementação.
