---
id: RP-002-PILOT-RESEARCH-BASE-DEC-001
title: Piloto — Decisão de Implementação do A4 Research Base
status: active
version: 1.0.1
owner: Guivos Research
last_updated: 2026-09-04
normative: false
parent: RP-002
maturity: implementation_target_approved_pre_configuration
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-IDENTITY-VAULT-DEC-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-OPS-REG-002
---

# Piloto — Decisão de Implementação do A4 Research Base

## 1. Finalidade

Este documento define o target documental do `A4 — Research Base` para o primeiro Dry Run Real `N=1` do `RP-002`.

O objetivo é transformar a arquitetura já aprovada — base de Research local, criptografada, pseudonimizada e materialmente separada do Identity Vault — em um contrato implementável futuramente, sem executar implantação nesta fase.

```text
A4 DOCUMENTATION TARGET
→ DECIDED

A4 OPERATIONAL CONFIGURATION
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 2. Papel da Research Base

A Research Base é o repositório operacional do conteúdo metodológico do episódio depois que a identidade direta é retirada do fluxo padrão.

Ela deve suportar:

- preparação e execução do episódio;
- registro do Momento e da Possibilidade;
- critérios e gates metodológicos;
- evidências Guivos `EG-0..EG-5`;
- benchmark;
- contextual fit;
- follow-up;
- New Momento;
- comparação longitudinal;
- consolidação do Episode Dossier;
- análise agregada posterior.

Ela **não** é o Identity Vault e **não** deve depender de nome, e-mail, telefone ou outro identificador direto para funcionar.

## 3. Boundary obrigatório

```text
IDENTITY VAULT A
→ direct identity + minimum operational data

RESEARCH BASE B
→ pseudonymized research content

LINKAGE KEY
→ separate, more restricted mapping
```

Regras:

- Research Base e Identity Vault não podem ser o mesmo diretório lógico ou o mesmo container apenas com subpastas;
- a Research Base não recebe a tabela de ligação nome ↔ `participant_id`;
- operadores que precisem apenas analisar Research não devem receber identidade direta por conveniência;
- o `participant_id` pseudonimizado é a chave operacional padrão dentro da Research Base.

## 4. Implementação-alvo

Para coerência com a arquitetura local privacy-first, o target inicial de A4 é:

```text
STORAGE
→ dedicated local encrypted storage

PRIMARY BOUNDARY
→ separate encrypted file-hosted volume

SOFTWARE TARGET
→ VeraCrypt stable release from official source

VOLUME TYPE
→ standard file-hosted volume

CLOUD SYNC
→ NO

AUTO-MOUNT
→ NO

HIDDEN VOLUME
→ NO

DYNAMIC / SPARSE MODE
→ NO
```

A seleção do mesmo mecanismo criptográfico usado como target de A3 não elimina a separação: A3 e A4 devem existir como **volumes distintos**, com escopos e acessos próprios.

A implementação real permanece adiada por `RP-002-PILOT-DOC-CLOSE-001`.

## 5. Identificador operacional

O Research Base deve operar por pseudônimo estável do piloto:

```text
participant_id
→ PILOT-P-<SEQUENCE>
```

Exemplo sintético:

```text
PILOT-P-TEST-001
```

O identificador:

- não deve conter nome;
- não deve conter e-mail;
- não deve conter telefone;
- não deve conter data de nascimento;
- não deve codificar atributo sensível;
- não deve ser previsível fora do contexto operacional mais do que o necessário.

Para `N=1`, numeração sequencial simples é aceitável como target operacional porque a chave de ligação permanece separada e o dataset é restrito. Se o piloto escalar, o esquema deve ser reavaliado.

## 6. Conteúdo permitido

A Research Base pode conter, quando necessário ao episódio:

- `participant_id`;
- `episode_id`;
- timestamps metodológicos;
- versão dos instrumentos aplicados;
- respostas e notas de Research pseudonimizadas;
- Momento;
- Possibilidade;
- critérios de elegibilidade metodológica;
- fit contextual;
- hipóteses;
- alternativas verificadas;
- benchmark;
- evidências `EG-0..EG-5`;
- status de ação significativa;
- follow-up;
- New Momento;
- comparação longitudinal;
- decisão GO / REVISE / STOP quando aplicável ao ciclo;
- logs metodológicos estritamente necessários.

## 7. Conteúdo proibido por padrão

Não armazenar na Research Base, por padrão:

- nome real;
- e-mail pessoal;
- telefone;
- CPF;
- RG;
- endereço residencial completo;
- documento de identidade;
- credenciais;
- senha;
- dados bancários;
- chave de ligação identidade ↔ pseudônimo;
- screenshots identificáveis desnecessários;
- anexos de recrutamento que revelem identidade;
- gravações de áudio/vídeo quando a gravação estiver desligada;
- informação sensível sem necessidade metodológica específica e base legal reavaliada.

Se um artefato externo útil contiver identificadores, ele deve ser minimizado/redigido antes de entrar na Research Base sempre que tecnicamente viável.

## 8. Estrutura lógica sugerida

O target documental adota estrutura simples e auditável:

```text
RESEARCH_BASE_ROOT
├── episodes/
│   └── <episode_id>/
│       ├── episode-record.md
│       ├── evidence/
│       ├── benchmark/
│       └── follow-up/
├── cycle/
│   ├── thresholds.md
│   └── cycle-summary.md
└── templates/
    └── synthetic-only-or-empty-templates
```

A estrutura pode ser ajustada antes da implementação se os instrumentos oficiais exigirem outra organização, desde que a separação e a pseudonimização sejam preservadas.

## 9. Episode ID

O `episode_id` deve ser distinto do `participant_id` para permitir mais de um episódio por Pessoa em fases futuras sem fundir identidade e ocorrência.

Target inicial:

```text
EP-<YYYY>-<SEQUENCE>
```

Exemplo sintético:

```text
EP-2026-TEST-001
```

O mapeamento entre `episode_id` e `participant_id` pode existir dentro da Research Base quando necessário ao método, pois ambos são pseudônimos. O mapeamento para identidade direta pertence à Linkage Key.

## 10. Acesso por função

Target documental:

```text
PILOT OWNER
→ READ / WRITE

DATA STEWARD
→ READ / WRITE

INTERVIEWER
→ minimum episode access when required

SUPPLY RESEARCHER / VERIFIER
→ only episode context required for supply research
→ no direct identity

BENCHMARK BLINDER
→ benchmark inputs only when role separation is used
→ no direct identity

ANALYST
→ pseudonymized dataset only
```

A política escrita não prova permissões reais. O gate operacional continuará `HOLD` até verificação futura.

## 11. Uso com IA

A Research Base não deve ser conectada integralmente a uma ferramenta de IA por padrão.

Fluxo-alvo:

```text
RESEARCH BASE
→ SELECT MINIMUM NECESSARY CONTEXT
→ REMOVE / CHECK DIRECT IDENTIFIERS
→ SUBMIT ONLY APPROVED PSEUDONYMIZED CONTEXT
→ RECEIVE OUTPUT
→ HUMAN REVIEW
→ STORE ONLY MATERIAL RESULT IF NEEDED
```

A8 definirá o operador/produto, controles e contrato aplicáveis antes de uso real.

## 12. Uso com Search / Web

O Search/Web não precisa receber o dossiê completo da Pessoa.

Fluxo-alvo:

```text
RESEARCH BASE
→ derive minimized search intent
→ remove direct identifiers
→ use only contextual attributes necessary to find/verify public supply
→ evaluate sources
→ store relevant evidence/reference back in Research Base
```

A9 documentará o método final.

## 13. Dados sensíveis e inferências

A experiência pode revelar informações delicadas mesmo sem solicitação explícita.

Regra de minimização:

- não criar campo sensível apenas porque a informação surgiu em conversa;
- registrar somente o que for material à hipótese ou segurança da recomendação;
- preferir abstração funcional quando o detalhe pessoal não for necessário;
- evitar transformar notas de Research em perfil amplo da Pessoa;
- qualquer necessidade recorrente de dado sensível exige reavaliação documental antes de uso sistemático.

## 14. Correção e exclusão

O desenho deve permitir localizar os registros por `participant_id` e/ou `episode_id` para:

- corrigir informação factual;
- remover artefato específico;
- excluir episódio;
- excluir o conjunto pseudonimizado vinculado à Pessoa quando aplicável;
- registrar fechamento sem manter conteúdo residual desnecessário.

O teste real pertence a `A7` e somente ocorrerá depois da implantação do stack.

## 15. Retenção

A4 não congela sozinho os prazos exatos.

```text
RETENTION BEHAVIOR
→ MUST FOLLOW A10

EXACT PERIODS
→ PENDING A10 DOCUMENTATION
```

A Research Base deve ser desenhada de modo que a retenção possa ser aplicada por categoria e episódio, sem depender de varredura manual impossível.

## 16. Backup

O backup da Research Base pertence a `A6`.

Regras herdadas:

- backup deve preservar criptografia;
- não criar cópia em cloud sync por conveniência;
- recuperação deve ser testável futuramente;
- backup não pode reintroduzir identidade direta no Research Base.

```text
A4 DOCUMENTED TARGET
≠ A6 PASS
```

## 17. Exportação e portabilidade operacional

O target deve usar formatos suficientemente simples para permitir:

- leitura sem software proprietário de banco de dados;
- correção manual controlada quando necessário;
- exportação para análise local;
- exclusão verificável;
- migração futura para infraestrutura mais madura.

Para `N=1`, formatos textuais e tabulares abertos são preferíveis a dependência precoce de banco complexo.

## 18. Logs

Não criar telemetria detalhada apenas por disponibilidade técnica.

Registrar somente logs necessários para:

- versão do instrumento;
- data do episódio;
- estado metodológico;
- correção/exclusão;
- eventos críticos de governança.

Logs também estão sujeitos a retenção e minimização.

## 19. Teste futuro de A4

Quando a implantação operacional for aberta, A4 deverá ser verificado somente com dados sintéticos antes de qualquer Pessoa real.

Teste-alvo futuro:

```text
T-RESEARCH-BASE-001
1. MOUNT EMPTY RESEARCH BASE
2. CREATE SYNTHETIC participant_id + episode_id
3. CREATE SYNTHETIC EPISODE RECORD
4. SAVE / READ / EDIT
5. CONFIRM NO DIRECT IDENTITY FIELD EXISTS
6. UNMOUNT
7. CONFIRM PLAINTEXT IS NOT AVAILABLE OUTSIDE APPROVED BOUNDARY
8. REMOUNT
9. EXPORT ONE SYNTHETIC RECORD
10. DELETE SYNTHETIC EPISODE
11. CONFIRM DELETION
12. CONFIRM NO REAL PARTICIPANT DATA WAS USED
```

Esse teste não deve ser executado durante a fase documental atual.

## 20. Subgates de A4

### A4-1 — Architecture Target

```text
SEPARATE LOCAL ENCRYPTED RESEARCH BASE
→ DECIDED
```

### A4-2 — Pseudonymization Contract

```text
participant_id / episode_id
→ DECIDED

DIRECT IDENTITY BY DEFAULT
→ PROHIBITED
```

### A4-3 — Data Schema / Content Boundary

```text
ALLOWED / PROHIBITED CONTENT
→ DOCUMENTED
```

### A4-4 — Access Model

```text
ROLE-BASED TARGET
→ DOCUMENTED

REAL PERMISSIONS
→ HOLD
```

### A4-5 — Encrypted Storage Configuration

```text
IMPLEMENTATION
→ DEFERRED

STATUS
→ HOLD
```

### A4-6 — Synthetic Functional Test

```text
T-RESEARCH-BASE-001
→ DOCUMENTED FOR FUTURE EXECUTION
→ NOT EXECUTED

STATUS
→ HOLD
```

## 21. Estado final

```text
A4 DOCUMENTATION
→ TARGET CLOSED

A4 IMPLEMENTATION
→ DEFERRED

A4 OPERATIONAL STATUS
→ HOLD

A5 — LINKAGE KEY DOCUMENTATION
→ NEXT

P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
