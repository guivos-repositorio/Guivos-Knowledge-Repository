---
id: GKR-RUNBOOK-GH-CODEX-001
title: Runbook Operacional de GitHub CLI, Codex e Workspace
status: draft
version: 0.2.0
owner: Guivos Repository Operations
last_updated: 2026-08-06
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

## 12. Recuperação controlada de workflows não iniciados

Este procedimento aplica-se quando um evento válido de `push` ou integração foi registrado, mas os workflows esperados não foram iniciados, inclusive após uma indisponibilidade do GitHub Actions ou Pages.

A recuperação é operacional. Ela não altera o estado documental, não cria autoridade arquitetural e não autoriza o início de uma frente posterior.

### 12.1 Pré-condições

Antes de qualquer disparo manual:

1. confirmar no status oficial do GitHub que Actions e Pages estão operacionais;
2. identificar o SHA atual da `main` e registrá-lo como alvo da recuperação;
3. confirmar que a `main` não avançou para outro commit sem revisão do escopo;
4. verificar se já existem execuções em fila, em andamento ou concluídas para o SHA alvo;
5. confirmar que não há PR aberto ou implantação concorrente capaz de produzir evidência ambígua;
6. confirmar que os workflows permanecem ativos e que o disparo manual está habilitado;
7. interromper o procedimento se qualquer precondição não puder ser comprovada.

Comandos auxiliares:

```bash
gh api repos/guivos-repositorio/Guivos-Knowledge-Repository/git/ref/heads/main
gh run list --branch main --limit 20
```

### 12.2 Ordem obrigatória de recuperação

Executar um workflow por vez, sempre sobre a branch `main` e somente depois de validar o resultado da etapa anterior.

#### Etapa 1 — validação semântica

Workflow: `GKR Semantic State Validation`.

Objetivo: confirmar que o estado semântico do GKR permanece sincronizado antes da geração ou publicação de artefatos.

#### Etapa 2 — publicação documental

Workflow: `Publish GKR Documentation`.

Objetivo: confirmar:

- `mkdocs build --strict` aprovado;
- PDF gerado e carregado como artefato;
- site gerado e carregado como artefato;
- ausência de job concorrente de deploy nesse workflow.

#### Etapa 3 — deploy canônico

Workflow: `Deploy GKR to GitHub Pages`.

Objetivo: executar uma única publicação canônica por `mkdocs gh-deploy`, confirmar a atualização da branch `gh-pages` e verificar que não ocorreu colisão com outro mecanismo de deploy.

Não iniciar a etapa seguinte enquanto a anterior estiver em fila, em andamento, cancelada ou com falha.

### 12.3 Execução pela interface do GitHub

Para cada workflow habilitado:

1. abrir a aba **Actions** do repositório;
2. selecionar o workflow pelo nome exato;
3. selecionar **Run workflow**;
4. escolher a branch `main`;
5. confirmar o disparo;
6. registrar o número e o identificador da execução;
7. acompanhar até a conclusão antes de prosseguir.

### 12.4 Execução pelo GitHub CLI

Em workspace autenticado:

```bash
gh workflow run semantic-state.yml --ref main
gh workflow run publish-docs.yml --ref main
gh workflow run deploy-pages.yml --ref main
```

Os comandos representam a ordem de recuperação, mas não devem ser executados em sequência automática. Entre eles, consultar e validar a execução correspondente:

```bash
gh run list --branch main --limit 20
gh run view <RUN_ID>
```

### 12.5 Evidências obrigatórias

O checkpoint de recuperação deverá registrar:

- SHA alvo da `main`;
- nome, número e identificador de cada workflow run;
- evento `workflow_dispatch`;
- horário de início e conclusão;
- conclusão de cada job;
- artefatos gerados pela publicação documental;
- commit resultante na branch `gh-pages`, quando houver deploy;
- confirmação de que houve apenas um mecanismo de publicação;
- falhas, avisos ou limitações observadas.

As evidências deverão ser registradas no PR ou no checkpoint de governança relacionado. Uma execução sobre SHA diferente não comprova a recuperação do SHA alvo.

### 12.6 Critérios de parada e proibições

Interromper a recuperação quando:

- o SHA da `main` mudar durante o procedimento;
- surgir execução concorrente;
- qualquer workflow falhar;
- os artefatos esperados não forem produzidos;
- o deploy tentar utilizar mecanismo diferente do canônico;
- a evidência não puder ser vinculada inequivocamente ao alvo.

É proibido:

- criar commit vazio, artificial ou sem mudança substantiva apenas para disparar CI;
- executar publicação ou deploy antes da validação semântica;
- repetir workflows bem-sucedidos sem causa registrada;
- ampliar o escopo para UXA-085, Engenharia de Produto, P2–P9 ou outra frente não autorizada;
- interpretar o disparo operacional como promoção de estado ou autorização de merge.

## 13. Resultado do P0

A pendência operacional sobre `gh`, autenticação, Codex e workspace está encerrada no nível de runbook.

Este documento não afirma que todo ambiente futuro já estará corretamente configurado. Ele define o procedimento de verificação, persistência, segurança e recuperação aplicável.
