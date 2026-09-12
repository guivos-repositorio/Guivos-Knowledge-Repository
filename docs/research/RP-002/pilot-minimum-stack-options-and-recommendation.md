---
id: RP-002-PILOT-STACK-PROP-001
title: Piloto — Stack Mínimo do Primeiro Dry Run — Opções e Recomendação
status: draft
version: 0.1.1
owner: Guivos Research
last_updated: 2026-09-04
normative: false
parent: RP-002
maturity: proposed_not_approved
related:
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-OPS-REG-002
  - RP-002-PILOT-NOTICE-CONSENT-002
---

# Piloto — Stack Mínimo do Primeiro Dry Run — Opções e Recomendação

## 1. Finalidade

Este documento compara arquiteturas mínimas para executar o primeiro Dry Run Real do `RP-002` com uma Pessoa, reduzindo superfície de dados, operadores externos e complexidade operacional.

Ele não aprova nenhuma ferramenta nova.

Estado:

```text
STACK TARGET
→ PROPOSED

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 2. Princípios da decisão

O primeiro Dry Run é `N=1` e deve priorizar:

1. minimização de dados;
2. separação material entre identidade e Research;
3. menor número possível de operadores externos;
4. correção e exclusão executáveis;
5. pseudonimização antes de IA e pesquisa externa;
6. ausência de gravação;
7. baixo custo de reversão;
8. nenhuma dependência de infraestrutura definitiva de produto;
9. possibilidade de testar o método antes de escalar a operação;
10. transparência suficiente para a Pessoa participante.

Regra:

> **O primeiro Dry Run não precisa reproduzir a arquitetura tecnológica futura da Guivos. Precisa provar o método com segurança proporcional e rastreável.**

## 3. Opção A — Stack mínimo privacy-first — RECOMENDADA PARA N=1

### 3.1 Visão

```text
RECRUTAMENTO / NOTICE / CONSENTIMENTO
→ mailbox dedicada de Research sob @guivos.com
→ Hostinger Mail

IDENTITY VAULT
→ armazenamento local criptografado A
→ sem sincronização cloud por padrão

RESEARCH BASE
→ armazenamento local criptografado B
→ separado do Identity Vault
→ somente pseudônimos

IA
→ OpenAI API dedicada ao RP-002
→ contexto mínimo pseudonimizado
→ sem identificadores diretos

SEARCH / WEB
→ pesquisa pública
→ queries minimizadas
→ sem identificadores diretos

PRIVACIDADE / DIREITOS
→ privacidade@guivos.com / privacy@guivos.com
→ Hostinger Mail
```

### 3.2 Por que esta é a recomendação inicial

Para `N=1`, esta opção:

- evita criar um repositório cloud de participantes antes de necessidade real;
- reduz o número de processadores externos que recebem identidade;
- torna Identity Vault e Research Base materialmente separáveis;
- permite executar correção, limitação e exclusão localmente;
- reduz risco de compartilhamento acidental em Drive colaborativo;
- mantém a arquitetura de IA independente da identidade;
- permite abandonar ou reformular o piloto sem migração complexa.

Trade-offs:

- exige disciplina de backup e recuperação;
- exige criptografia realmente configurada, não apenas declarada;
- colaboração simultânea fica limitada;
- não é arquitetura recomendada para escala futura;
- permissões precisam ser verificadas no dispositivo real.

## 4. Componente A1 — Mailbox dedicada de Research

A recomendação é criar um canal separado do canal de direitos, por exemplo:

```text
pesquisa@guivos.com
research@guivos.com
```

O endereço final ainda precisa de decisão e provisionamento.

Finalidades permitidas propostas:

- convite/recrutamento;
- agendamento;
- envio do Notice aprovado;
- captura da manifestação de consentimento;
- comunicações necessárias ao ciclo;
- follow-up previsto.

Não usar `privacidade@guivos.com` como caixa normal de recrutamento apenas porque já existe.

### Estado

```text
MAILBOX RESEARCH
→ PROPOSED
→ NOT PROVISIONED
→ HOLD
```

## 5. Componente A2 — Consentimento por trilha versionada de e-mail

Para `N=1`, uma plataforma de formulários não é obrigatória se a prova puder ser produzida de forma clara e versionada.

Fluxo proposto:

```text
GUIVOS
→ envia Notice final com VERSION_ID
→ solicita manifestação explícita

PESSOA
→ responde de forma inequívoca

GUIVOS
→ registra:
   participant_id
   notice_version
   consent_status
   timestamp
   scope
```

O conteúdo identificável da manifestação permanece no ambiente operacional aprovado e **não entra no GKR**.

Uma resposta genérica como `ok` não deve ser tratada como consentimento sem contexto suficiente.

## 6. Componente A3 — Identity Vault local criptografado

### Conteúdo

Somente o mínimo necessário:

- `participant_id`;
- nome;
- contato;
- confirmação `18+`;
- status de recrutamento;
- notice/consent status;
- chave de ligação;
- status de direitos/exclusão.

### Requisitos

```text
LOCAL STORAGE
→ dedicated

ENCRYPTION AT REST
→ REQUIRED

CLOUD SYNC
→ OFF BY DEFAULT

ACCESS
→ Pilot Owner / Data Steward only

BACKUP
→ encrypted, controlled, tested

DELETION
→ executable and tested
```

A mera existência de senha no sistema operacional não prova este gate.

### Estado

```text
IDENTITY STORAGE
→ TARGET ARCHITECTURE PROPOSED
→ NOT CONFIGURED
→ HOLD
```

## 7. Componente A4 — Research Base local criptografada e separada

A Research Base não deve conter identidade direta.

Conteúdo previsto:

- `participant_id` pseudônimo;
- `episode_id`;
- síntese do Momento revisada;
- objetivos/restrições/preferências materiais;
- Possibilidades;
- oportunidades;
- gates `G1–G10`;
- fontes/freshness;
- benchmark;
- decisão/ação;
- experiência;
- contribuição;
- observações metodológicas.

Requisitos:

```text
DIRECT IDENTIFIERS
→ NO

LINKAGE KEY
→ NO

SENSITIVE DATA BY DEFAULT
→ NO

SEPARATE STORAGE BOUNDARY
→ YES

ENCRYPTION
→ REQUIRED
```

### Estado

```text
RESEARCH STORAGE
→ TARGET ARCHITECTURE PROPOSED
→ NOT CONFIGURED
→ HOLD
```

## 8. Componente A5 — OpenAI API como ferramenta de IA candidata

### Razão da recomendação

Quando IA for necessária ao Dry Run, a proposta é utilizar um **projeto/API empresarial dedicado à Guivos**, e não tratar uma conta individual de ChatGPT como infraestrutura aprovada do piloto.

A OpenAI informa que, por padrão, dados de clientes de produtos empresariais e da API não são usados para treinar modelos.

Fontes oficiais:

- <https://openai.com/business-data/>
- <https://openai.com/pt-BR/policies/data-processing-addendum/>
- <https://openai.com/enterprise-privacy/>

A documentação empresarial também informa que inputs e outputs da API são removidos dos sistemas após 30 dias no regime padrão, salvo exigência legal, e que Zero Data Retention pode estar disponível para clientes/endpoints elegíveis.

### Regra de envio

```text
DIRECT IDENTIFIER
→ NEVER BY DEFAULT

NAME / EMAIL / PHONE
→ DO NOT SEND

LINKAGE KEY
→ NEVER

RAW IDENTIFIABLE TRANSCRIPT
→ DO NOT SEND

SENSITIVE DATA NOT NEEDED
→ DO NOT SEND

CONTEXT
→ pseudonymized + minimized + task-scoped
```

### Estado

```text
OPENAI API
→ CANDIDATE / RECOMMENDED
→ NOT YET APPROVED
→ ACCOUNT / PROJECT / DATA CONTROL CONFIGURATION NOT VERIFIED
→ HOLD
```

Este documento não presume elegibilidade a ZDR.

## 9. Componente A6 — Search / Web

O supply público pode ser pesquisado sem expor identidade direta.

Exemplo aceitável:

```text
curso de análise de dados noturno remoto Brasil
```

Evitar:

```text
João da Silva, 36 anos, email X, mora em Y e está desempregado...
```

Regra:

```text
IDENTIDADE DIRETA NA QUERY
→ NO

CONTEXTO NECESSÁRIO
→ MINIMIZED

DADO SENSÍVEL
→ NO BY DEFAULT
```

O fornecedor/ferramenta real ainda deve ser registrado antes do uso operacional com contexto pessoal.

### Estado

```text
SEARCH / WEB
→ METHOD DEFINED
→ OPERATOR NOT YET APPROVED
→ HOLD
```

## 10. Sessão do primeiro Dry Run

Para reduzir operadores no primeiro ciclo, a recomendação é:

```text
PRESENCIAL / LOCAL
→ PREFERRED WHEN PRACTICABLE
```

Se a sessão for remota, a plataforma de videoconferência/mensageria passa a ser novo componente do stack e precisa de registro próprio antes do uso.

Gravação permanece:

```text
AUDIO
→ OFF

VIDEO
→ OFF
```

## 11. Opção B — Google Workspace Business — alternativa para colaboração e escala

### Arquitetura possível

```text
Google Forms
→ recrutamento / consentimento

Google Drive / Sheets
→ Identity Vault restrito

Google Drive / Sheets
→ Research Base separada

OpenAI API
→ IA pseudonimizada

Search / Web
→ queries minimizadas
```

### Condições obrigatórias antes de aprovação

Não usar o Drive já existente como prova suficiente.

A opção só pode ser promovida se houver:

- tenant Google Workspace controlado pela Guivos Ltda;
- edição/plano confirmado;
- Cloud Data Processing Addendum aplicável/verificado;
- usuários e permissões reais auditados;
- MFA/controles relevantes configurados;
- pastas/arquivos dedicados ao piloto;
- Identity Vault e Research Base separados;
- retenção e exclusão testadas;
- transferência internacional avaliada;
- Notice atualizado com o operador real.

O Google informa que o Google Workspace oferece Cloud Data Processing Addendum para obrigações de processador e que certas edições oferecem controles de regiões de dados.

Fontes oficiais:

- <https://knowledge.workspace.google.com/admin/compliance/privacy-compliance-and-records-for-google-workspace-and-cloud-identity>
- <https://knowledge.workspace.google.com/admin/compliance/data-covered-by-data-regions>

### Estado

```text
GOOGLE WORKSPACE BUSINESS
→ SCALE OPTION
→ NOT CURRENTLY VERIFIED FOR RP-002
→ NOT APPROVED
```

## 12. Por que o Google Drive conectado atualmente não é promovido

A auditoria encontrou infraestrutura documental Guivos em Google Drive, mas não encontrou artefato `RP-002`/piloto nem evidência suficiente de que o ambiente conectado seja o tenant empresarial juridicamente destinado ao tratamento de participantes.

Logo:

```text
DRIVE EXISTS
≠ WORKSPACE BUSINESS VERIFIED
≠ DPA VERIFIED FOR THIS ACCOUNT
≠ PILOT STORAGE APPROVED
```

## 13. Comparativo

| Critério | Opção A — Local privacy-first | Opção B — Workspace Business |
|---|---|---|
| adequada a N=1 | **alta** | média |
| operadores externos de storage | **menor** | maior |
| colaboração | baixa | **alta** |
| configuração inicial | média | média/alta |
| exclusão simples | **alta se bem configurada** | alta se permissões/processos corretos |
| dependência cloud | **baixa** | alta |
| escalabilidade | baixa | **alta** |
| necessidade de contrato cloud adicional | menor | **sim** |
| risco de compartilhamento acidental | menor | exige governança forte |
| reversibilidade | **alta** | média |

## 14. Recomendação

Para o **primeiro Dry Run real com uma única Pessoa**, a recomendação de Research é:

> **Adotar a Opção A — stack mínimo privacy-first — como arquitetura-alvo do Participant 001, sem promover qualquer componente para PASS até configuração e teste reais.**

Isso permite testar a hipótese central antes de assumir uma infraestrutura colaborativa de maior escala.

A Opção B deve ser reavaliada quando:

- houver mais operadores humanos;
- múltiplos participantes simultâneos;
- necessidade real de colaboração;
- necessidade de automação de forms/workflows;
- requisitos de auditoria centralizada superarem a simplicidade local.

## 15. Gates necessários para aprovar a Opção A

```text
A1 — research mailbox provisioned + tested
A2 — final Notice version linked to consent flow
A3 — Identity Vault encrypted/configured
A4 — Research Base encrypted/configured
A5 — linkage key physically/logically separated
A6 — encrypted backup tested
A7 — correction + deletion drill executed
A8 — OpenAI API Guivos account/project verified
A9 — API data controls and DPA status recorded
A10 — Search/Web operator/method approved
A11 — exact retention periods approved
A12 — Notice updated with final stack
A13 — legal/privacy final review
```

Até lá:

```text
P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD
```

## 16. Decisões que este documento NÃO toma

Este documento não:

- cria os mailboxes de Research;
- configura criptografia;
- escolhe formato final de banco/arquivo local;
- cria conta da OpenAI API;
- concede ZDR;
- aprova Google Workspace;
- define prazos finais de retenção;
- substitui revisão jurídica;
- autoriza Participant 001.

## 17. Próximo ato após aprovação da arquitetura-alvo

Se a Opção A for aprovada como target do primeiro Dry Run, a ordem operacional recomendada é:

```text
1. provisionar mailbox de Research
2. configurar os dois storages locais criptografados
3. testar separação e exclusão
4. configurar OpenAI API dedicada
5. aprovar Search/Web
6. congelar retenção
7. atualizar Notice v0.1 → próxima versão
8. concluir P2C
9. revisão jurídica/privacidade final
10. avaliar Participant 001
```

## 18. Estado final

```text
RECOMMENDED TARGET
→ OPTION A — LOCAL PRIVACY-FIRST

DECISION STATUS
→ PROPOSED / NOT APPROVED

P2C
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