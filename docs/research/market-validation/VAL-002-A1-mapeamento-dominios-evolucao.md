---
id: VAL-002-A1
title: Mapeamento da Pesquisa B2C para os Domínios de Evolução do Guivos Journey
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
parent: VAL-002
related:
  - VAL-001
  - VAL-002
  - PAS-001
  - PAS-001-DOMAIN-MODEL-001
---

# VAL-002-A1 — Mapeamento da Pesquisa B2C para os Domínios de Evolução do Guivos Journey

## 1. Finalidade

Este documento estabelece a rastreabilidade semântica entre a pergunta 4 do `VAL-002 — Pesquisa Oficial B2C da Guivos` e o `PAS-001-DOMAIN-MODEL-001 — Modelo Canônico dos Domínios de Evolução do Guivos Journey`.

Ele **não altera**:

- o texto da pesquisa;
- os códigos das alternativas;
- a versão 2.1.0 do instrumento;
- os critérios de aplicação;
- os KPIs;
- resultados de pesquisa;
- estados de evidência.

O objetivo é registrar como um conjunto de opções criado para pesquisa contribuiu para o vocabulário arquitetural do Journey.

## 2. Pergunta de origem

Pergunta 4 do VAL-002:

> **Qual área da sua vida você mais gostaria de cuidar, fortalecer ou transformar?**

Escolha apenas uma.

A escolha única é uma decisão metodológica do instrumento de pesquisa para permitir priorização e análise. Ela **não significa** que o Guivos Journey deva limitar a jornada real a um único domínio.

## 3. Mapeamento canônico

| Código VAL-002 | Alternativa do instrumento | Mapeamento arquitetural | Observação |
|---|---|---|---|
| `4.1` | Saúde e bem-estar | `JED-001 — Saúde e Bem-estar` | correspondência direta |
| `4.2` | Trabalho, carreira ou estudos | `JED-002 — Trabalho, Carreira e Estudos` | o domínio consolida os três eixos em uma família canônica |
| `4.3` | Situação financeira | `JED-003 — Vida Financeira` | nome arquitetural mais amplo que a formulação da pesquisa |
| `4.4` | Empreendedorismo ou projetos pessoais | `JED-004 — Empreendedorismo e Projetos` | aplicabilidade expandida também a Coletivos e Organizações |
| `4.5` | Relacionamentos e vida social | `JED-005 — Relacionamentos e Vida Social` | correspondência direta |
| `4.6` | Espiritualidade e propósito | `JED-006 — Espiritualidade, Propósito e Valores` | “Valores” é extensão arquitetural governada; não altera a alternativa da pesquisa |
| `4.7` | Viagens, lazer e novas experiências | `JED-007 — Viagens, Lazer, Cultura e Novas Experiências` | “Cultura” é extensão arquitetural governada; não altera a alternativa da pesquisa |
| `4.8` | Causas ou voluntariado | `JED-008 — Causas, Voluntariado e Contribuição` | “Contribuição” amplia o domínio sem alterar o código da pesquisa |
| `4.9` | Organização geral da vida | `JED-009 — Organização e Equilíbrio da Vida` | “Equilíbrio” é contextual e não constitui score ou padrão universal |
| `4.10` | Ainda não sei ou escolheria outra área | **sem domínio único** | decomposto em estado “Ainda estou descobrindo” e mecanismo `other_unmapped` |

## 4. Regra especial para 4.10

A alternativa `4.10` combina duas situações diferentes para fins de pesquisa:

1. a pessoa ainda não sabe qual área deseja priorizar;
2. a pessoa escolheria uma área que não está representada nas opções.

Na arquitetura do Journey, esses conceitos devem permanecer separados.

### 4.1 Ainda não sei

Mapeia para o estado transversal:

```text
Ainda estou descobrindo
```

Esse estado:

- não é décimo domínio;
- não é falha;
- não exige classificação automática;
- permite exploração sem pressão para definir Objetivo;
- preserva a possibilidade de permanecer sem domínio enquanto não houver clareza.

### 4.2 Outra área

Mapeia para:

```text
other_unmapped
```

O texto livre, quando fornecido, deverá ser preservado como expressão original.

A Guivos poderá posteriormente avaliar se o conteúdo:

- cabe em um domínio existente;
- representa nova subárea;
- permanece sem mapeamento;
- fornece evidência para futura revisão da taxonomia.

Nenhuma dessas decisões deverá ser feita silenciosamente em prejuízo da expressão do participante.

## 5. Relação com as perguntas 5 e 6

A própria pesquisa já admite estados de descoberta e incerteza.

Exemplos do VAL-002:

- `5.2` — “Tenho uma ideia, mas ainda estou explorando possibilidades.”;
- `5.3` — “Sinto que algo precisa mudar, mas ainda não sei exatamente o quê.”;
- `5.7` — “Ainda não sei responder.”;
- `6.1` — “Quero ter mais clareza ou escolher uma direção.”;
- `6.2` — “Quero conhecer novas possibilidades.”;
- `6.8` — “Ainda não sei exatamente o que desejo.”

Essas alternativas são semanticamente compatíveis com a decisão arquitetural de manter **exploração e ausência de direção como estados legítimos**.

Elas não devem ser usadas isoladamente para inferir domínio, diagnóstico, vulnerabilidade ou prioridade.

## 6. Pesquisa ≠ jornada operacional

A pesquisa solicita escolha única na pergunta 4.

O Journey operacional, por outro lado, deverá admitir:

```text
0 domínio confirmado
1 domínio
2 ou mais domínios relacionados
outro ainda não mapeado
estado de exploração
```

Exemplo:

```text
Pesquisa:
Pessoa escolhe 4.3 — Situação financeira

Journey real, posteriormente:
JED-003 Vida Financeira
+
JED-007 Viagens, Lazer, Cultura e Novas Experiências
+
JED-002 Trabalho, Carreira e Estudos
```

A resposta da pesquisa não deverá congelar a jornada futura da pessoa.

## 7. Pesquisa ≠ evidência de eficácia

A existência das alternativas e o seu uso como baseline semântico não comprovam:

- aceitação de mercado;
- prioridade populacional de qualquer domínio;
- eficácia da Guivos em qualquer área;
- capacidade operacional;
- disponibilidade de serviços;
- PMF;
- retenção;
- disposição a pagar;
- evolução de participantes.

Resultados somente poderão ser declarados mediante base reproduzível e gates de evidência do sistema VAL.

## 8. Compatibilidade por participante

O VAL-002 é um instrumento B2C e, portanto, sua redação original é orientada à Pessoa.

A promoção para `PAS-001-DOMAIN-MODEL-001` amplia o **vocabulário arquitetural**, e não o escopo estatístico da pesquisa.

Assim:

```text
opção B2C da Pessoa
→ contribui para nome do domínio
→ domínio recebe interpretação própria para Pessoa, Coletivo e Organização
```

Não é permitido usar resultados da pesquisa B2C como evidência automática sobre necessidades de Coletivos ou Organizações.

## 9. Invariantes

```text
alternativa de pesquisa ≠ domínio confirmado da jornada
escolha única na pesquisa ≠ jornada de domínio único
4.10 ≠ décimo domínio
texto livre ≠ classificação automática
frequência de resposta ≠ eficácia da Guivos
preferência declarada ≠ comportamento real
resultado B2C ≠ evidência sobre Coletivos ou Organizações
```

## 10. Autoridade resultante

- `VAL-002` continua autoridade sobre o instrumento de pesquisa;
- `PAS-001-DOMAIN-MODEL-001` é autoridade sobre os Domínios de Evolução do Journey;
- `VAL-002-A1` governa somente a rastreabilidade entre os dois.
