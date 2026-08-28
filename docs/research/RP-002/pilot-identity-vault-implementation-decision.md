---
id: RP-002-PILOT-IDENTITY-VAULT-DEC-001
title: Piloto — Decisão de Implementação do A3 Identity Vault
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: implementation_target_approved_pre_configuration
related:
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-STACK-PROP-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-OPS-REG-001
---

# Piloto — Decisão de Implementação do A3 Identity Vault

## 1. Finalidade

Este documento define o mecanismo de implementação-alvo do `A3 — Identity Vault` para o primeiro Dry Run Real `N=1` do `RP-002`.

Ele transforma a arquitetura já aprovada — armazenamento local criptografado, dedicado, sem cloud sync por padrão e separado da Research Base — em uma configuração executável.

Este documento **não comprova que a configuração já existe** e não promove `A3` para `PASS`.

Estado:

```text
A3 IMPLEMENTATION TARGET
→ DECIDED

A3 OPERATIONAL CONFIGURATION
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 2. Contrato herdado

O `RP-002-PILOT-STACK-DEC-001`, o `RP-002-PILOT-OP-001` e o `RP-002-PILOT-DATA-LAW-001` exigem que o Identity Vault:

- seja local e dedicado;
- possua criptografia em repouso realmente configurada;
- não esteja em cloud sync por padrão;
- permaneça materialmente separado da Research Base;
- seja acessível apenas às funções autorizadas;
- contenha somente identidade e operação mínimas;
- permita correção e exclusão;
- não seja confundido com o GKR;
- não contenha o dossiê rico de Research.

A existência de senha no sistema operacional, isoladamente, não satisfaz esse contrato.

## 3. Implementação selecionada

Para a configuração inicial em Windows, o target aprovado é:

```text
SOFTWARE
→ VeraCrypt

VOLUME TYPE
→ standard file-hosted volume

ROLE
→ dedicated local encrypted Identity Vault

CLOUD STORAGE
→ NO

AUTO-MOUNT
→ NO

HIDDEN VOLUME
→ NO

DYNAMIC / SPARSE CONTAINER
→ NO
```

O arquivo-container deve existir em raiz local não sincronizada e dedicada ao piloto.

Nome lógico recomendado:

```text
identity-vault.hc
```

O caminho físico real do dispositivo não deve ser registrado no GKR quando isso expuser informação operacional desnecessária.

## 4. Evidência técnica da escolha

A documentação oficial do VeraCrypt suporta criação de volume hospedado em arquivo, montado como volume criptografado para leitura e escrita.

Fontes oficiais verificadas em 2026-08-27:

- documentação: <https://veracrypt.io/en/Documentation.html>
- tutorial de container: <https://veracrypt.io/en/Beginner%27s%20Tutorial.html>
- criação de volumes: <https://veracrypt.io/en/Creating%20New%20Volumes.html>
- downloads oficiais: <https://veracrypt.io/en/Downloads.html>
- requisitos e precauções de segurança: <https://veracrypt.io/en/Security%20Requirements%20and%20Precautions.html>

Na verificação realizada, a release estável publicada era `1.26.29`, datada de 2026-06-09.

Regra operacional:

> **usar a versão estável corrente obtida da origem oficial no momento da configuração e verificar sua autenticidade/integridade pelos mecanismos oficiais disponíveis.**

O número de versão observado acima registra evidência temporal; não transforma `1.26.29` em versão eternamente congelada.

## 5. Alternativa Windows nativa considerada

A solução `VHD/VHDX + BitLocker` não foi selecionada como mecanismo primário do Identity Vault.

Razões:

1. VHD/VHDX cria uma fronteira de disco virtual, mas a documentação Microsoft registra limitações para uso de BitLocker em volumes contidos em VHD em cenários documentados;
2. a habilitação completa do BitLocker também depende de edição/licenciamento Windows compatível;
3. para `N=1`, um container VeraCrypt file-hosted cria diretamente a fronteira criptografada dedicada exigida pelo piloto, sem particionar o disco físico.

Fontes Microsoft consultadas:

- BitLocker overview: <https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/>
- gerenciamento de VHD/VHDX: <https://learn.microsoft.com/windows-server/storage/disk-management/manage-virtual-hard-disks>
- VHDX / BitLocker limitation: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/deploy-windows-on-a-vhd--native-boot?view=windows-11>

Essa decisão não rejeita BitLocker como proteção adicional do dispositivo/volume host quando disponível. Apenas não o utiliza como boundary primário de A3.

## 6. Parâmetros do container

Target inicial para `N=1`:

```text
VOLUME
→ STANDARD

HOSTING
→ FILE-HOSTED

SIZE
→ 256 MiB FIXED

DYNAMIC MODE
→ OFF

FILESYSTEM
→ NTFS

ENCRYPTION
→ AES

KDF
→ Argon2id, quando disponível na versão estável configurada
```

A documentação atual do VeraCrypt lista `Argon2id` e `PBKDF2` entre os algoritmos de derivação suportados.

O tamanho de `256 MiB` é deliberadamente pequeno porque o Identity Vault deve conter apenas estrutura mínima de identidade/operação, não áudio, vídeo, transcrições ricas ou dossiê de Research.

Se houver necessidade real de expansão, isso deve ser revisado antes de ampliar o escopo de conteúdo.

## 7. Segredo de acesso

O segredo do volume:

```text
MUST BE CREATED LOCALLY
→ YES

MUST BE UNIQUE
→ YES

MUST BE STORED IN GKR
→ NO

MUST BE SENT IN CHAT
→ NO

MUST BE STORED INSIDE THE SAME VOLUME
→ NO
```

A documentação VeraCrypt recomenda senha forte com mais de 20 caracteres.

Fonte:

<https://veracrypt.io/en/Choosing%20Passwords%20and%20Keyfiles.html>

Para `N=1`, o target inicial é usar uma passphrase forte e única sem tornar keyfile obrigatório. Keyfiles poderão ser reavaliados quando houver necessidade de múltiplos operadores, token físico ou política de recuperação mais madura.

Nenhuma senha, PIM, keyfile, recovery material ou segredo deve entrar no GKR.

## 8. Localização e cloud sync

O container deve ficar em diretório local dedicado que não pertença a:

- OneDrive;
- Google Drive;
- Dropbox;
- iCloud Drive;
- pasta corporativa sincronizada;
- compartilhamento de rede;
- pasta cujo comportamento de sincronização não esteja confirmado.

Forma lógica:

```text
LOCAL_NON_SYNC_ROOT
└── Guivos-RP002
    └── Identity
        └── identity-vault.hc
```

Antes de A3 passar, deve existir verificação operacional de que a localização real não é sincronizada por serviço cloud.

## 9. Política de montagem e sessão

Target de segurança operacional:

```text
AUTO-MOUNT
→ OFF

PASSWORD CACHE
→ OFF

MOUNT
→ somente durante operação necessária

UNMOUNT AFTER USE
→ REQUIRED

AUTO-UNMOUNT AFTER INACTIVITY
→ ENABLED

POWER-SAVING AUTO-UNMOUNT
→ ENABLED WHEN SUPPORTED
```

Valor inicial recomendado para inatividade:

```text
15 MINUTES
```

A documentação VeraCrypt oferece auto-unmount após período sem leitura/escrita e opção de unmount ao entrar em modo de economia de energia.

Fontes:

- <https://veracrypt.io/en/Program%20Menu.html>
- <https://veracrypt.io/en/Hibernation%20File.html>

A documentação também alerta que criptografia de disco protege dados em repouso, não elimina dados descriptografados que possam permanecer em RAM ou em artefatos produzidos por outros programas. Portanto, aplicações usadas com o vault devem ser minimizadas e não devem criar cópias temporárias fora do boundary deliberadamente.

## 10. Conteúdo permitido

O Identity Vault poderá conter somente os campos proporcionais definidos pelo `RP-002-PILOT-DATA-LAW-001`, quando necessários:

- `participant_id`;
- nome;
- canal de contato;
- confirmação `18+` / faixa etária mínima;
- cidade/região somente quando material ao episódio;
- idioma quando relevante;
- disponibilidade quando relevante;
- status de recrutamento;
- notice/consent version/status/timestamp;
- status de follow-up;
- direitos/correção/exclusão e fechamento operacional.

Não coletar por padrão:

- CPF;
- RG;
- endereço residencial completo;
- documento de identidade;
- data de nascimento completa;
- dados bancários;
- senhas;
- credenciais de terceiros;
- dados sensíveis não necessários;
- transcrição identificável rica;
- dossiê do Momento.

## 11. Boundary com Research Base e Linkage Key

```text
IDENTITY VAULT A
→ direct identity + minimum operations

RESEARCH BASE B
→ pseudonymized research content
→ separate encrypted boundary

LINKAGE KEY
→ not inside Research Base
→ access more restricted
```

A3 não autoriza criar A4 ou A5 dentro do mesmo container apenas por conveniência.

O Research Base terá decisão/configuração própria.

## 12. Papéis e acesso

A política-alvo é:

```text
PILOT OWNER
→ ALLOWED

DATA STEWARD
→ ALLOWED

INTERVIEWER
→ only minimum operational access when explicitly required

SUPPLY RESEARCHER / VERIFIER
→ NO DIRECT IDENTITY ACCESS BY DEFAULT

BENCHMARK BLINDER
→ NO DIRECT IDENTITY ACCESS BY DEFAULT

ANALYST
→ NO DIRECT IDENTITY ACCESS BY DEFAULT
```

A política escrita não prova permissão real. A3 somente pode passar após verificação no dispositivo configurado.

## 13. Teste sintético obrigatório — T-IDENTITY-001

Nenhum dado real deve ser usado para fechar A3.

Dataset sintético mínimo:

```text
participant_id: PILOT-P-TEST-001
name: TEST USER
contact: test@example.invalid
age_gate: 18+ TEST
recruitment_status: TEST_ONLY
consent_status: TEST_ONLY
```

Fluxo:

```text
1. MOUNT EMPTY VAULT
2. CREATE SYNTHETIC RECORD
3. SAVE
4. READ BACK
5. EDIT ONE FIELD
6. UNMOUNT
7. CONFIRM VAULT IS NOT ACCESSIBLE AS PLAINTEXT WHILE UNMOUNTED
8. REMOUNT WITH LOCALLY HELD SECRET
9. CONFIRM UPDATED RECORD
10. DELETE SYNTHETIC RECORD
11. UNMOUNT
12. CONFIRM NO REAL PARTICIPANT DATA WAS USED
```

O teste não substitui `A7 — correction/deletion drill`, que será repetido depois sobre o stack-alvo completo.

## 14. Subgates de A3

### A3-1 — Implementation Target

```text
VeraCrypt standard fixed file-hosted volume
→ DECIDED
```

### A3-2 — Software Acquisition / Integrity

Critério:

- obter software da fonte oficial;
- registrar versão instalada sem registrar segredo;
- verificar integridade/autenticidade pelos mecanismos oficiais disponíveis.

Estado:

```text
HOLD
```

### A3-3 — Encrypted Container

Critério:

- container padrão criado;
- tamanho fixo;
- criptografia configurada;
- montagem/desmontagem funcional.

Estado:

```text
HOLD
```

### A3-4 — Non-Sync Location

Critério:

- localização local dedicada;
- ausência de cloud sync verificada.

Estado:

```text
HOLD
```

### A3-5 — Access Controls

Critério:

- owner funcional definido;
- acesso coerente com Pilot Owner / Data Steward;
- password cache desabilitado;
- auto-mount desabilitado;
- sessão/unmount coerentes com esta decisão.

Estado:

```text
HOLD
```

### A3-6 — Synthetic Functional Test

Critério:

- `T-IDENTITY-001` executado integralmente;
- remount comprovado;
- nenhum dado real utilizado.

Estado:

```text
HOLD
```

## 15. Backup não pertence ao fechamento de A3

A arquitetura exige backup criptografado e recuperação testada, mas esse controle pertence a `A6`.

Logo:

```text
A3 PASS
≠ A6 PASS
```

A3 pode comprovar o armazenamento primário e continuar com `A6` em `HOLD` até o teste próprio de backup/recovery.

A documentação VeraCrypt recomenda backup regular de dados importantes e descreve criação de volume separado para backup seguro.

Fonte:

<https://veracrypt.io/en/How%20to%20Back%20Up%20Securely.html>

## 16. Estado de gates após esta decisão

```text
A1 — RESEARCH MAILBOX
→ PASS

A3-1 — IMPLEMENTATION TARGET
→ DECIDED

A3-2 — SOFTWARE / INTEGRITY
→ HOLD

A3-3 — ENCRYPTED CONTAINER
→ HOLD

A3-4 — NON-SYNC LOCATION
→ HOLD

A3-5 — ACCESS CONTROLS
→ HOLD

A3-6 — SYNTHETIC TEST
→ HOLD

A3 — IDENTITY VAULT
→ HOLD

A4 — RESEARCH BASE
→ HOLD

A5 — LINKAGE KEY
→ HOLD

A6 — BACKUP / RECOVERY
→ HOLD

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

## 17. Próximo ato material

O próximo ato não é documental.

É configurar o componente local de forma sintética:

```text
INSTALL / VERIFY VERACRYPT
→ CREATE identity-vault.hc OUTSIDE CLOUD SYNC
→ CONFIGURE SESSION CONTROLS
→ EXECUTE T-IDENTITY-001
→ RECORD ONLY NON-SECRET EVIDENCE
```

Somente após essa execução A3 poderá ser reavaliado para `PASS`.
