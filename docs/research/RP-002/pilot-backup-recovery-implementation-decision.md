---
id: RP-002-PILOT-BACKUP-RECOVERY-DEC-001
title: Piloto — Decisão de Implementação do A6 Backup e Recovery
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: implementation_target_approved_pre_configuration
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-IDENTITY-VAULT-DEC-001
  - RP-002-PILOT-RESEARCH-BASE-DEC-001
  - RP-002-PILOT-LINKAGE-KEY-DEC-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
---

# Piloto — Decisão de Implementação do A6 Backup e Recovery

## 1. Finalidade

Este documento define o target documental do `A6 — Backup / Recovery` do stack local privacy-first do `RP-002`.

O objetivo é garantir que perda, corrupção ou falha do armazenamento primário não resulte em improvisação, cópia insegura ou restauração impossível.

A implantação e o teste real permanecem adiados durante a fase de fechamento documental.

```text
A6 DOCUMENTATION TARGET
→ DECIDED

A6 OPERATIONAL CONFIGURATION
→ HOLD

RECOVERY TEST
→ NOT EXECUTED
```

## 2. Princípios

O backup deve preservar os mesmos princípios do armazenamento primário:

- criptografia em repouso;
- minimização;
- separação entre identidade, linkage e Research;
- ausência de cloud sync por padrão;
- acesso restrito;
- possibilidade de exclusão e expiração;
- recuperação testável;
- nenhum segredo no GKR.

Regra:

> **Backup não pode criar uma cópia menos protegida do que a origem.**

## 3. Escopo

Componentes sujeitos à política de A6:

```text
IDENTITY VAULT
→ BACKUP REQUIRED BEFORE REAL RELEASE

RESEARCH BASE
→ BACKUP REQUIRED BEFORE REAL RELEASE

LINKAGE KEY
→ BACKUP ONLY IF NECESSARY FOR RECOVERY MODEL
→ MUST REMAIN MORE RESTRICTED
```

A necessidade de backup da Linkage Key deve ser avaliada de forma proporcional: evitar tanto perda irreversível da ligação quanto duplicação desnecessária de um artefato de reidentificação.

## 4. Arquitetura-alvo

Para o primeiro `N=1`, o target é um backup local criptografado em meio separado do armazenamento primário.

```text
PRIMARY STORAGE
→ local encrypted boundaries

BACKUP STORAGE
→ separate encrypted local medium / boundary

DEFAULT CLOUD BACKUP
→ NO

PLAIN BACKUP
→ PROHIBITED
```

O meio exato será selecionado somente na fase operacional, desde que cumpra os critérios documentados aqui.

## 5. Separação

Os backups devem preservar a separação lógica dos componentes.

```text
IDENTITY BACKUP
≠ RESEARCH BACKUP

LINKAGE BACKUP
→ separate / more restricted when used
```

Não criar um único pacote desprotegido contendo identidade + linkage + Research apenas para facilitar recuperação.

Se um mesmo meio físico for utilizado futuramente, os boundaries criptográficos e controles de acesso devem continuar separados.

## 6. Conteúdo do backup

O backup deve conter somente o necessário para reconstruir o estado autorizado do componente.

Não incluir por conveniência:

- arquivos temporários;
- exports esquecidos;
- screenshots;
- downloads intermediários;
- logs excessivos;
- cópias antigas fora da política de retenção;
- credenciais ou passphrases armazenadas junto do backup.

## 7. Segredos e recovery material

```text
PASSWORDS / PASSPHRASES
→ NOT IN GKR
→ NOT IN BACKUP DATASET

KEYFILES / RECOVERY MATERIAL
→ NOT IN GKR
→ MUST NOT BE STORED WITH THE SAME ENCRYPTED PAYLOAD AS ITS ONLY PROTECTION
```

A estratégia concreta de custódia de segredo será definida e testada na fase operacional sem registrar o segredo no repositório.

## 8. Frequência

Para `N=1`, a política documental prioriza backup após mudanças materiais, em vez de automação complexa precoce.

Target:

```text
BACKUP EVENT
→ after creation of a material authorized record set
→ after material correction when continued retention is required
→ before/after structural migration when applicable

BACKGROUND CONTINUOUS SYNC
→ NO
```

A frequência poderá ser aumentada em escala futura.

## 9. Versionamento e retenção de backups

Backups não devem contornar A10.

Regras:

- manter somente versões necessárias para recuperação;
- evitar histórico indefinido;
- aplicar expiração proporcional;
- quando dados forem excluídos do primário, a política deve definir como e quando deixam de existir em backups recuperáveis;
- qualquer restauração deve reaplicar exclusões/correções posteriores conhecidas.

Os prazos exatos serão congelados em A10.

## 10. Recovery

Backup sem restauração comprovável não fecha A6.

Teste futuro obrigatório:

```text
T-RECOVERY-001
1. USE SYNTHETIC DATA ONLY
2. CREATE ENCRYPTED PRIMARY TEST RECORDS
3. CREATE ENCRYPTED BACKUP
4. SIMULATE PRIMARY UNAVAILABLE
5. RESTORE TO CLEAN APPROVED BOUNDARY
6. CONFIRM IDENTITY / RESEARCH / LINKAGE SEPARATION
7. CONFIRM SYNTHETIC RECORD INTEGRITY
8. CONFIRM NO PLAINTEXT RESIDUAL COPY CREATED
9. DELETE TEST DATA AND TEST BACKUP
10. RECORD NON-SECRET RESULT
```

O teste não deve ser executado durante a fase documental atual.

## 11. Recovery objective

Para o primeiro piloto, não há necessidade de definir RTO/RPO empresarial complexo.

Critério mínimo:

```text
RECOVERY OBJECTIVE
→ restore an internally consistent authorized pilot state
→ without weakening privacy boundaries
→ before any continuation with real participant data
```

Se a operação escalar ou se tornar contínua, RTO/RPO formais deverão ser definidos.

## 12. Correção e exclusão após restore

Toda restauração deve considerar eventos posteriores ao snapshot, incluindo:

- revogação;
- correção;
- exclusão;
- fechamento;
- mudança de retenção.

Não é permitido restaurar um backup antigo e reintroduzir deliberadamente dados que já deveriam permanecer excluídos.

## 13. Evidência futura

A evidência operacional de A6 deve registrar somente informações não secretas, como:

- componente testado;
- data do teste;
- tipo de meio/boundary sem expor localização sensível desnecessária;
- resultado de backup;
- resultado de restore;
- resultado de verificação de separação;
- resultado de limpeza do teste;
- falhas e correções.

Não registrar no GKR:

- passphrase;
- keyfile;
- serial de dispositivo quando desnecessário;
- caminho físico excessivamente revelador;
- conteúdo de participante.

## 14. Falha de backup/recovery

Qualquer falha material mantém:

```text
A6
→ HOLD

PARTICIPANT 001
→ HOLD
```

Falha não deve ser mascarada por criação de cópia manual não criptografada.

## 15. Subgates de A6

```text
A6-1 BACKUP PRINCIPLES / SCOPE
→ DOCUMENTED

A6-2 SEPARATION MODEL
→ DOCUMENTED

A6-3 RETENTION INTERFACE
→ DOCUMENTED / EXACT PERIODS PENDING A10

A6-4 REAL ENCRYPTED BACKUP
→ HOLD

A6-5 RECOVERY TEST
→ HOLD

A6-6 POST-TEST CLEANUP
→ HOLD

A6 OVERALL
→ OPERATIONAL HOLD
```

## 16. Estado final

```text
A6 DOCUMENTATION
→ TARGET CLOSED

A6 IMPLEMENTATION
→ DEFERRED

A6 OPERATIONAL STATUS
→ HOLD

NEXT DOCUMENTAL BLOCK
→ A8 OPENAI API
→ A9 SEARCH / WEB

A7
→ REMAINS OPERATIONAL HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
