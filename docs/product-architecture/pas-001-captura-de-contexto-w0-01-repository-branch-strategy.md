---
id: PAS-001-CC-W0-01-REPO-001
title: Estratégia de Repositório, Branches e Revisão do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-01-OWNERS-001
  - PAS-001-CC-W0-01-PIPELINE-001
---

# PAS-001-CC-W0-01-REPO-001 — Estratégia de Repositório, Branches e Revisão

## 1. Repositório proposto

```text
guivos-repositorio/Guivos-Capture-Context
```

O repositório deverá ser:

- privado;
- criado somente após autorização específica;
- separado do GKR;
- vinculado às autoridades do GKR por IDs e links;
- destinado à implementação, testes, contratos executáveis e evidências;
- incapaz de alterar autoridade normativa apenas por decisão de código.

## 2. Branch principal

A branch principal será `main`.

Controles obrigatórios:

- push direto proibido;
- force push proibido;
- exclusão proibida;
- merge somente por pull request;
- checks obrigatórios;
- aprovação obrigatória;
- conversas de revisão resolvidas;
- aprovação invalidada após mudança material no head;
- commit assinado quando a capacidade estiver disponível e aprovada;
- branch atualizada ou comprovadamente baseada no baseline aceito.

## 3. Padrões de branch

| Prefixo | Uso |
|---|---|
| `feat/` | capacidade funcional ou técnica |
| `fix/` | correção de defeito |
| `adr/` | decisão arquitetural |
| `chore/` | automação, estrutura ou manutenção |
| `docs/` | documentação operacional |
| `security/` | controle ou correção de segurança |
| `test/` | fixture ou suíte de testes |

Formato:

```text
<prefixo>/<story-id>-<descricao-curta>
```

Exemplos:

```text
feat/w0-01-st-001-project-structure
adr/adr-tcc-001-language-framework
chore/w0-01-st-003-minimum-pipeline
docs/w0-01-st-005-evidence-template
security/w0-01-st-008-secret-scanning
```

## 4. Estratégia de integração

- branches curtas;
- um objetivo verificável por PR;
- sem rebase ou force push após aprovação, salvo correção explicitamente revalidada;
- merge commit como padrão inicial para preservar contexto, salvo ADR ou política posterior;
- squash permitido apenas quando não destruir rastreabilidade entre commits, requisito e evidência;
- nenhuma branch promove automaticamente ambiente ou versão.

## 5. Requisitos do pull request

Todo PR deverá declarar:

```yaml
story_ids: string[]
requirement_ids: string[]
architecture_references: string[]
adr_references: string[]
risk_ids: string[]
expected_evidence_ids: string[]
data_classes: string[]
authority_impact: none | reviewed
security_impact: none | reviewed
breaking_change: boolean
rollback_reference: string | null
```

O corpo deverá incluir:

- objetivo;
- escopo incluído e excluído;
- comportamento esperado;
- critérios de aceite;
- testes executados;
- riscos novos ou alterados;
- evidências previstas;
- impacto em contratos;
- estratégia de reversão;
- declaração de ausência de dados reais e segredos.

## 6. Aprovações mínimas

| Tipo de mudança | Revisores obrigatórios |
|---|---|
| estrutura e automação | Engineering ou Platform/DevOps |
| domínio | Architecture + Engineering |
| contratos e schemas | Architecture + Engineering + Quality |
| identidade, segurança ou privacidade | Security/Privacy + Architecture |
| evidência | Quality/Evidence |
| segredo, chave ou credencial | Security/Privacy + Platform/DevOps |
| risco critical | governança + autoridade técnica competente |

CODEOWNERS deverá materializar essas regras após owners nominais definidos.

## 7. Commits

Formato recomendado:

```text
<tipo>(<escopo>): <descrição>
```

Tipos mínimos:

- `feat`;
- `fix`;
- `test`;
- `docs`;
- `adr`;
- `security`;
- `chore`.

O commit deverá ser:

- intencional;
- limitado ao objetivo;
- livre de segredo;
- rastreável a uma história ou decisão;
- reversível sem alterar significado histórico;
- produzido por identidade reconhecida.

## 8. Versionamento

### Contratos e schemas

Usar SemVer:

- major: incompatibilidade deliberada;
- minor: extensão compatível;
- patch: correção sem alteração semântica incompatível.

### Implementação

Durante a Onda 0:

```text
0.<incremento>.<revisão>
```

A versão não representa produção ou estabilidade pública.

### Evidências

A evidência referencia:

- commit SHA;
- versão da implementação;
- versão do contrato;
- configuração;
- ambiente;
- dataset sintético;
- hash do artefato.

## 9. Releases e tags

Tags somente poderão ser criadas quando:

- pacote tiver decisão formal;
- checks obrigatórios estiverem válidos;
- evidências aplicáveis existirem;
- riscos estiverem atualizados;
- tag não sugerir produção.

Formato proposto:

```text
w0-01-foundation-v0.1.0
w0-02-domain-v0.2.0
```

## 10. Mudanças emergenciais

No W0-01 não existe produção e não há justificativa para bypass permanente.

Correção emergencial deverá:

- criar branch específica;
- registrar risco ou incidente;
- manter PR;
- executar checks mínimos;
- exigir revisão posterior imediata quando houver contenção excepcional;
- não alterar autoridade funcional.

## 11. Critérios de aceite

A estratégia estará executada quando:

- repositório privado existir;
- `main` estiver protegida;
- templates estiverem instalados;
- CODEOWNERS refletir owners nominais;
- branch de teste comprovar bloqueio de push direto;
- PR de teste comprovar checks e revisão;
- regras forem documentadas no próprio repositório;
- EV-018 registrar configuração, resultado e hash.

## 12. Limites

Este documento não cria o repositório, não altera configurações do GitHub e não autoriza código. Ele define o contrato para uma execução posterior.
