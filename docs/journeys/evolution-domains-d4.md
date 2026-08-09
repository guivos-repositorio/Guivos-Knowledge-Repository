---
id: GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001
title: Propagação dos Domínios de Evolução nas Jornadas Integradas — D4
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
normative: false
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
---

# Propagação dos Domínios de Evolução nas Jornadas Integradas — D4

## 1. Finalidade

Esta autoridade documental executa a frente D4 de propagação dos Domínios de Evolução para as vistas integradas de Pessoa, Coletivo e Organização.

Ela não cria uma nova capacidade do Guivos Journey, uma nova superfície, uma nova transição ou uma nova taxonomia. O vocabulário canônico permanece governado por `PAS-001-DOMAIN-MODEL-001`; a compatibilização com as capacidades permanece governada por `PAS-001-DOMAIN-RECON-001`.

D4 responde à pergunta:

> **Como os Domínios de Evolução aparecem na leitura integrada da jornada de cada participante?**

## 2. Regra de leitura em dois eixos

As jornadas passam a ser lidas simultaneamente por dois eixos:

```text
Eixo funcional
como a jornada acontece

Momento Atual
→ Objetivos
→ Eventos de Vida
→ Próximos Passos
→ Oportunidades
→ Experiências
→ Evidências
→ Evolução

×

Eixo de domínio
sobre qual área a jornada está tratando

JED-001 ... JED-009
```

Portanto:

```text
Domínio de Evolução
≠ etapa da jornada
≠ tela
≠ transição
≠ objetivo
≠ evento
≠ oportunidade
≠ experiência
≠ evidência
≠ score
≠ prova de evolução
```

## 3. Domínios canônicos

| ID | Domínio |
|---|---|
| `JED-001` | Saúde e Bem-estar |
| `JED-002` | Trabalho, Carreira e Estudos |
| `JED-003` | Vida Financeira |
| `JED-004` | Empreendedorismo e Projetos |
| `JED-005` | Relacionamentos e Vida Social |
| `JED-006` | Espiritualidade, Propósito e Valores |
| `JED-007` | Viagens, Lazer, Cultura e Novas Experiências |
| `JED-008` | Causas, Voluntariado e Contribuição |
| `JED-009` | Organização e Equilíbrio da Vida |

`Ainda estou descobrindo` permanece estado legítimo de exploração e não constitui décimo domínio.

`other_unmapped` permanece mecanismo de captura de uma área ainda não mapeada, sem reclassificação silenciosa.

## 4. Regras comuns às três jornadas

1. uma jornada pode ter `0..n` Domínios de Evolução relacionados;
2. multidomínio é estado legítimo e não exige escolha artificial de apenas um domínio;
3. um domínio pode ser declarado, confirmado, contextual ou apenas candidato, conforme autoridade e estado de confirmação;
4. domínio candidato não se torna confirmado por repetição, inferência ou conveniência técnica;
5. ausência de domínio conhecido não bloqueia a continuidade da jornada quando a capacidade aplicável permitir;
6. `Ainda estou descobrindo` não significa ausência de contexto, falta de evolução ou baixa maturidade;
7. `other_unmapped` não autoriza encaixe automático em um domínio existente;
8. vínculo de domínio não altera consentimento, finalidade, autoridade ou visibilidade;
9. domínio sensível não autoriza inferência de saúde, religião, condição financeira ou outra condição protegida;
10. plano pago, patrocínio ou capacidade comercial não altera domínio, prioridade humana ou relevância funcional;
11. domínio não é identidade permanente do participante;
12. domínio não mede mérito, valor, fé, saúde, sucesso financeiro ou evolução humana.

## 5. Jornada da Pessoa

### 5.1 Aplicabilidade

Todos os nove domínios podem ser relevantes à Pessoa, conforme contexto voluntariamente declarado, autorizado ou legitimamente confirmado.

| Domínio | Exemplos de contexto da Pessoa |
|---|---|
| `JED-001` Saúde e Bem-estar | hábitos, atividade física, sono, alimentação, autocuidado, prevenção, qualidade de vida |
| `JED-002` Trabalho, Carreira e Estudos | emprego, recolocação, carreira, estudo, curso, competência, certificação, liderança |
| `JED-003` Vida Financeira | orçamento, organização financeira, reserva, renda, dívida, planejamento financeiro |
| `JED-004` Empreendedorismo e Projetos | ideia, negócio, projeto pessoal, validação, parceiros, execução de iniciativa |
| `JED-005` Relacionamentos e Vida Social | família, amizades, vínculos, convivência, pertencimento, novas conexões |
| `JED-006` Espiritualidade, Propósito e Valores | fé, espiritualidade, propósito, valores, reflexão, comunidade religiosa escolhida |
| `JED-007` Viagens, Lazer, Cultura e Novas Experiências | viagens, hobbies, cultura, lazer, eventos, experiências desejadas |
| `JED-008` Causas, Voluntariado e Contribuição | voluntariado, causas, contribuição, participação comunitária, serviço |
| `JED-009` Organização e Equilíbrio da Vida | rotina, prioridades, tempo, equilíbrio, reorganização após mudanças |

### 5.2 Percurso semântico

A leitura integrada pode assumir, por exemplo:

```text
Pessoa
→ Momento Atual
→ domínio declarado/candidato
→ Direção
→ Objetivo
→ Próximo Passo
→ Oportunidades compatíveis e relevantes
→ Experiência
→ Evidências legítimas
→ Evolução reconhecida pelo participante
```

O domínio pode aparecer antes, durante ou depois da formulação de um Objetivo. A Guivos não deverá obrigar a Pessoa a classificar seu relato em um domínio para continuar uma jornada quando isso não for necessário.

### 5.3 Multidomínio

Exemplo:

```text
"Quero melhorar minha renda para conseguir fazer uma viagem"

JED-003 Vida Financeira
+
JED-007 Viagens, Lazer, Cultura e Novas Experiências
```

Outro exemplo:

```text
"Mudei de cidade e quero voltar a participar de uma comunidade de fé"

JED-005 Relacionamentos e Vida Social
+
JED-006 Espiritualidade, Propósito e Valores
+
Evento de Vida: mudança de cidade
```

A presença de múltiplos domínios não autoriza a Guivos a escolher unilateralmente qual é o mais importante.

## 6. Jornada do Coletivo

### 6.1 Natureza da associação

No Coletivo, o domínio descreve a área de evolução ou contribuição à qual uma iniciativa, necessidade, atividade, propósito ou experiência coletiva se relaciona.

O domínio não deverá antropomorfizar o Coletivo.

Exemplo:

```text
Coletivo relacionado a JED-001 Saúde e Bem-estar
≠ "o Coletivo está saudável"
```

A leitura correta pode ser:

```text
Coletivo
→ necessidade ou propósito coletivo
→ domínio(s) relacionado(s)
→ iniciativa/atividade
→ participantes e relações autorizadas
→ execução voluntária
→ evidências coletivas legítimas
→ resultados e aprendizados
```

### 6.2 Exemplos por domínio

| Domínio | Exemplos no contexto do Coletivo |
|---|---|
| `JED-001` | caminhada comunitária, promoção de bem-estar, prevenção, apoio a hábitos saudáveis |
| `JED-002` | grupo de estudos, capacitação, mentoria coletiva, desenvolvimento profissional |
| `JED-003` | educação financeira comunitária, apoio à organização econômica dos participantes |
| `JED-004` | rede de empreendedores, laboratório de projetos, iniciativa produtiva coletiva |
| `JED-005` | pertencimento, convivência, integração, redes de apoio, comunidade |
| `JED-006` | comunidade de fé, reflexão, valores compartilhados, propósito coletivo voluntário |
| `JED-007` | viagens em grupo, atividades culturais, lazer, experiências compartilhadas |
| `JED-008` | ação social, causa, voluntariado, mobilização, campanha comunitária |
| `JED-009` | organização de rotinas, coordenação de iniciativas, apoio à gestão da vida comunitária |

### 6.3 Autoridade e voluntariedade

O Coletivo pode propor atividades ou oportunidades relacionadas a um domínio, mas não pode atribuir silenciosamente um domínio pessoal a uma Pessoa.

```text
atividade coletiva em JED-006
≠ participante classificado como religioso
```

```text
atividade coletiva em JED-003
≠ participante classificado por situação financeira
```

Pertencimento ao Coletivo não cria automaticamente um `domain_link` pessoal confirmado.

## 7. Jornada da Organização

### 7.1 Natureza da associação

Na Organização, o domínio descreve a área à qual uma oportunidade, programa, iniciativa, responsabilidade institucional ou resultado autorizado se relaciona.

Não deverá ser usado para atribuir condição humana à Organização.

Exemplo:

```text
Organização relacionada a JED-001
= organização promove iniciativa de Saúde e Bem-estar
≠ organização possui estado de saúde
```

A leitura integrada pode ser:

```text
Organização
→ necessidade ou objetivo institucional autorizado
→ domínio(s) relacionado(s)
→ programa/oportunidade
→ público e elegibilidade
→ execução
→ experiências dos participantes quando legitimamente registradas
→ evidências institucionais autorizadas
→ resultados e revisão
```

### 7.2 Exemplos por domínio

| Domínio | Exemplos no contexto da Organização |
|---|---|
| `JED-001` | programas de saúde, segurança, prevenção, bem-estar e qualidade de vida |
| `JED-002` | emprego, capacitação, educação, desenvolvimento de competências e carreira |
| `JED-003` | educação financeira, benefícios ou iniciativas de segurança econômica dentro da finalidade autorizada |
| `JED-004` | apoio ao empreendedorismo, inovação, incubação, projetos e iniciativas |
| `JED-005` | pertencimento, integração, convivência, cultura relacional e redes de apoio |
| `JED-006` | propósito, valores, ética e iniciativas espirituais/religiosas apenas quando voluntárias e legitimamente aplicáveis |
| `JED-007` | viagens, cultura, lazer, experiências, eventos e programas relacionados |
| `JED-008` | responsabilidade social, voluntariado, causas, campanhas e contribuição comunitária |
| `JED-009` | organização de vida, apoio à rotina, equilíbrio e condições que facilitem participação e desenvolvimento |

### 7.3 Separações obrigatórias

```text
Domínio de Evolução
≠ segmento comercial
≠ plano da Organização
≠ Guivos Business
≠ público-alvo automático
≠ permissão para acessar contexto individual
```

Uma Organização pode publicar uma oportunidade relacionada a determinado domínio sem receber acesso ao histórico, estado, objetivos ou classificação individual das Pessoas.

## 8. Handoffs entre participantes

Os domínios podem ajudar a descrever a compatibilidade temática entre participantes, mas não substituem as regras de handoff.

Exemplo:

```text
Pessoa
→ interesse/objetivo em JED-008

Coletivo
→ ação social relacionada a JED-008

Organização
→ recurso ou programa relacionado a JED-008

Guivos
→ pode identificar compatibilidade contextual
→ ainda precisa aplicar autoridade, elegibilidade, relevância,
  proteção, voluntariedade e regras de cada handoff
```

Portanto:

```text
mesmo domínio
≠ match obrigatório
≠ recomendação automática
≠ compartilhamento automático
≠ autorização automática
≠ resultado garantido
```

## 9. Relação com Momento Atual, Objetivos e demais capacidades

Nas três jornadas, o domínio pode se relacionar com:

- condição ou assunto relevante no Momento Atual;
- Direção e Objetivos;
- impacto de Eventos de Vida;
- Próximos Passos;
- Oportunidades;
- Intervenções Contextuais, quando legítimas;
- Experiências;
- evidências;
- trajetórias de Evolução Contínua.

A associação não obriga que todos esses objetos existam simultaneamente.

Exemplo válido:

```text
Pessoa
→ JED-009 Organização e Equilíbrio da Vida
→ ainda sem Objetivo definido
→ "Ainda estou descobrindo"
→ exploração de possibilidades
```

## 10. Sensibilidade e proteção

Alguns domínios podem envolver dados pessoais sensíveis ou informações de alta sensibilidade contextual.

Especial atenção é obrigatória em:

- saúde física ou mental;
- religião, fé ou prática espiritual;
- finanças e vulnerabilidade econômica;
- relações familiares ou íntimas;
- causas que revelem crenças, condições ou associações protegidas;
- contexto de crianças, adolescentes ou pessoas vulneráveis quando aplicável.

O vínculo a um domínio não cria consentimento, base legal, autorização de processamento, autorização de compartilhamento ou direito de inferência.

## 11. Estado “Ainda estou descobrindo”

Este estado permite que a jornada prossiga sem forçar categorização prematura.

Pode ocorrer quando:

- o participante sabe que algo precisa mudar, mas ainda não sabe o quê;
- existem vários assuntos simultâneos;
- um Evento de Vida alterou prioridades;
- o participante quer explorar possibilidades antes de formular Objetivo;
- a informação disponível ainda não sustenta classificação segura.

```text
Ainda estou descobrindo
≠ JED-010
≠ ausência de propósito
≠ baixa maturidade
≠ falha de classificação
```

## 12. Estado `other_unmapped`

`other_unmapped` deve preservar uma necessidade ou área ainda não representada adequadamente pela taxonomia.

Ele não deverá ser usado como depósito permanente para evitar evolução da ontologia.

Qualquer futura promoção de uma nova área canônica exige governança própria e não pertence à D4.

## 13. Relação com UX

D4 é documental.

Ela não determina:

- nova tela de seleção de áreas;
- chips obrigatórios;
- cards obrigatórios;
- ordem visual dos domínios;
- pergunta obrigatória de classificação;
- nova superfície de onboarding;
- novo SVG;
- nova transição;
- score por domínio.

A materialização experiencial é assunto separado da D5.

## 14. Relação com grafo e Public Canon

D4 não define modelo físico de Neo4j, nós, relações, índices ou APIs. Isso permanece D6.

D4 também não altera o Guia Oficial/Public Canon. Isso permanece D7.

## 15. Resultado da frente

Após D4, as Jornadas Integradas passam a reconhecer explicitamente que:

1. `JED-001..JED-009` constituem o eixo canônico de áreas de evolução;
2. Pessoa, Coletivo e Organização usam os mesmos IDs, com semântica adequada à natureza de cada participante;
3. multidomínio é legítimo;
4. `Ainda estou descobrindo` permanece estado de exploração;
5. `other_unmapped` permanece mecanismo de extensibilidade;
6. vínculo de domínio não cria score, diagnóstico, prioridade humana, autoridade, consentimento ou prova de evolução;
7. nenhuma nova superfície, transição ou implementação é criada por esta propagação.

## 16. Fora de escopo

Permanecem fora de D4:

- D5 — UX, UXA, wireframes e SVGs;
- D6 — grafo, Neo4j e ontologia física;
- D7 — Guia Oficial/Public Canon;
- UXA-102/V5;
- Engenharia de Produto/W0-01;
- billing/gateway;
- processo posterior a `BND-002`;
- qualquer implementação de classificação ou recomendação.
