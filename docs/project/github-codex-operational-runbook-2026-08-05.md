---
id: GKR-RUNBOOK-GH-CODEX-001
title: Runbook Operacional de GitHub CLI, Codex e Workspace
status: draft
version: 0.1.0
owner: Guivos Repository Operations
last_updated: 2026-08-05
depends_on:
  - GKR-AUD-ACCUMULATED-003
related:
  - GKR-INFO-CLASS-001
  - GKR-P0-CLOSURE-001
normative: false
---

# Runbook Operacional de GitHub CLI, Codex e Workspace

## 1. Finalidade

Separar os procedimentos de execução do repositório das decisões arquiteturais da Guivos.

A instalação do GitHub CLI, a autenticação, o uso de workspace, a execução no Codex e a abertura de pull requests são controles operacionais. Eles não alteram o estado do ecossistema, não criam capacidades e não promovem documentos à Canon.

## 2. Modelo de operação

A operação pode ocorrer por dois caminhos complementares:

1. **ChatGPT com conector GitHub:** caminho preferencial para leitura, auditoria, criação de branches, atualização de arquivos, pull requests e acompanhamento de workflows;
2. **workspace Codex com GitHub CLI:** caminho auxiliar para tarefas que exigem shell, execução local, testes extensos, manipulação de muitos arquivos ou ferramentas não disponíveis no conector.

O usuário pode continuar aprovando e solicitando o trabalho pelo chat. O workspace Codex não exige que a condução do projeto seja transferida para sua interface.

## 3. Pré-requisitos do workspace

Em um ambiente confiável, verificar:

```bash
gh --version
gh auth status
gh repo view guivos-repositorio/Guivos-Knowledge-Repository
```

Resultado esperado:

- `gh` disponível no `PATH`;
- autenticação válida;
- acesso ao repositório confirmado;
- permissões compatíveis com a tarefa.

## 4. Persistência do GitHub CLI

Para evitar reinstalação manual em ambientes novos, o GitHub CLI deverá ser incluído em um dos seguintes mecanismos:

- imagem base do workspace;
- script de inicialização;
- arquivo de configuração do ambiente;
- etapa de bootstrap idempotente.

O bootstrap deverá:

1. verificar se `gh` já existe;
2. instalar somente quando necessário;
3. utilizar fonte oficial do pacote;
4. confirmar a versão instalada;
5. não gravar tokens na imagem;
6. falhar de forma explícita quando a instalação não for concluída.

## 5. Autenticação

A autenticação deverá utilizar fluxo seguro do GitHub em ambiente confiável.

Comando de diagnóstico:

```bash
gh auth status
```

Quando a autenticação não estiver disponível, utilizar o fluxo interativo apropriado:

```bash
gh auth login
```

Regras obrigatórias:

- não registrar tokens no repositório;
- não colar tokens em documentos, issues, PRs ou comentários;
- não inserir credenciais em scripts versionados;
- preferir armazenamento seguro fornecido pelo ambiente;
- revogar imediatamente qualquer credencial exposta;
- usar apenas os escopos necessários.

## 6. Verificação do contexto

Antes de modificar o repositório:

```bash
git status
git branch --show-current
git remote -v
gh repo view guivos-repositorio/Guivos-Knowledge-Repository
```

Confirmar:

- repositório correto;
- branch correta;
- ausência de alterações inesperadas;
- remoto correto;
- escopo autorizado na conversa ou no ticket de trabalho.

## 7. Fluxo governado de alteração

### 7.1 Preparação

1. ler `GKR-STATE-001` e autoridades relacionadas;
2. confirmar pacote e limites;
3. verificar se existe branch ou PR anterior;
4. evitar duplicação de trabalho;
5. criar branch a partir da baseline autorizada.

### 7.2 Execução

1. alterar somente arquivos pertencentes ao escopo;
2. preservar front matter, IDs e autoridade;
3. não copiar informação sensível;
4. produzir commits descritivos;
5. não iniciar pacotes posteriores por inferência.

### 7.3 Validação

Executar os controles disponíveis no repositório, incluindo, quando aplicável:

```bash
python scripts/validate_gkr.py
git diff --check
mkdocs build --strict --site-dir /tmp/gkr-site
git status --short
```

O workflow oficial no GitHub continua sendo a evidência final dos gates do PR.

### 7.4 Pull request

O PR deverá registrar:

- objetivo;
- escopo;
- arquivos alterados;
- autoridades preservadas;
- validações;
- itens fora do escopo;
- base e head verificáveis;
- riscos ou pendências.

Nenhum merge deverá ocorrer sem autorização explícita.

## 8. Quando usar o conector GitHub

Preferir o conector quando a tarefa envolver:

- inspeção de PRs, branches, commits e arquivos;
- leitura e atualização documental;
- criação de branches e PRs;
- acompanhamento de workflows;
- revisão de metadados;
- alterações pequenas ou médias com conteúdo conhecido.

## 9. Quando usar o workspace Codex

Utilizar o workspace quando a tarefa exigir:

- execução de ferramentas locais;
- testes que dependam de ambiente completo;
- refatoração de muitos arquivos;
- geração ou processamento de artefatos;
- depuração de CI com reprodução local;
- manipulação que o conector não suporte adequadamente.

O uso do workspace não substitui branch, PR, validação e autorização.

## 10. Falhas comuns

### `gh: command not found`

Causa provável: GitHub CLI ausente ou fora do `PATH`.

Tratamento:

1. verificar a imagem e o bootstrap;
2. instalar por mecanismo persistente;
3. reabrir o shell;
4. executar `gh --version`.

### autenticação inválida

Tratamento:

1. executar `gh auth status`;
2. renovar o login em ambiente confiável;
3. confirmar conta e host corretos;
4. verificar permissões sem ampliar escopos desnecessariamente.

### repositório não encontrado

Tratamento:

1. confirmar `owner/name`;
2. verificar autenticação;
3. verificar permissões;
4. confirmar remoto e organização.

### novo workspace perdeu a configuração

Tratamento:

1. corrigir imagem ou script de inicialização;
2. tornar o bootstrap idempotente;
3. não depender de instalação manual da sessão anterior.

### estado do chat diverge do Git

Tratamento:

1. consultar PR, branch e commit atuais;
2. usar o Git como prova de execução;
3. corrigir o resumo de continuidade;
4. não recriar trabalho já existente.

### execução aparentemente infinita

Tratamento:

1. interromper a execução quando possível;
2. verificar processo, logs e conectividade;
3. reduzir a tarefa a uma etapa verificável;
4. reabrir o ambiente somente após preservar alterações versionadas;
5. evitar alegar conclusão sem commit ou resultado observável.

## 11. Segurança operacional

É proibido incluir em comandos compartilhados ou documentação:

- tokens reais;
- senhas;
- chaves privadas;
- segredos de API;
- cookies;
- códigos de recuperação;
- conteúdo de arquivos de credenciais.

Exemplos devem utilizar placeholders inequívocos e nunca valores reutilizáveis.

## 12. Resultado do P0

A pendência operacional sobre `gh`, autenticação, Codex e workspace está encerrada no nível de runbook.

Este documento não afirma que todo ambiente futuro já estará corretamente configurado. Ele define o procedimento de verificação, persistência, segurança e recuperação aplicável.
