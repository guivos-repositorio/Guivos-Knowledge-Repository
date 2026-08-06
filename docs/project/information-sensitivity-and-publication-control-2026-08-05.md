---
id: GKR-INFO-CLASS-001
title: Controle de Sensibilidade e Publicação de Informações
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
related:
  - GKR-EXT-SOURCE-PRESERVATION-001
  - GKR-RUNBOOK-GH-CODEX-001
  - GKR-P0-CLOSURE-001
normative: false
---

# Controle de Sensibilidade e Publicação de Informações

## 1. Finalidade

Estabelecer uma classificação mínima para decidir o que pode ser registrado, resumido, referenciado ou publicado no Guivos Knowledge Repository.

O controle é necessário porque o repositório possui visibilidade pública.

## 2. Princípio central

A visibilidade do repositório prevalece sobre a conveniência editorial.

Nenhuma informação deverá ser publicada integralmente quando sua exposição puder causar:

- perda de controle sobre ativos;
- risco jurídico ou regulatório;
- exposição de dados pessoais;
- comprometimento de credenciais ou infraestrutura;
- prejuízo comercial ou negocial;
- revelação indevida de estratégia;
- violação de direitos de terceiros;
- conflito com obrigações contratuais.

## 3. Classes

| Classe | Definição | Tratamento no GKR público |
|---|---|---|
| `public` | conteúdo aprovado para divulgação externa | pode ser publicado após revisão |
| `internal` | conteúdo de trabalho sem segredo crítico, mas não destinado à divulgação irrestrita | somente síntese sanitizada, quando houver valor arquitetural |
| `confidential` | estratégia, ativos, contratos, dados comerciais, jurídicos ou operacionais protegidos | não publicar integralmente; registrar apenas metadados mínimos e disposição |
| `restricted` | credenciais, chaves, tokens, dados pessoais brutos, acessos, segredos técnicos ou evidência de alto impacto | publicação proibida; referência pública deve ser genérica e não operacional |

## 4. Regras de publicação

### 4.1 Conteúdo público

Pode ser publicado quando:

- a autoridade estiver clara;
- a versão estiver identificada;
- não houver dados pessoais ou segredos;
- direitos de publicação estiverem confirmados;
- o conteúdo não criar alegação superior à evidência disponível.

### 4.2 Conteúdo interno

O GKR público poderá registrar apenas:

- finalidade;
- estado;
- decisão de autoridade;
- dependências;
- riscos;
- resumo sem detalhes operacionais sensíveis.

O documento integral deve permanecer em ambiente controlado quando a divulgação não tiver sido aprovada.

### 4.3 Conteúdo confidencial

Somente poderão ser publicados:

- identificador de intake;
- categoria genérica;
- existência da fonte;
- estado de verificação;
- pacote responsável;
- decisão de não publicação.

Não deverão ser publicados valores, nomes, contas, contatos privados, números de registro, contratos, evidências, URLs de gestão, inventários detalhados ou dados que permitam reconstruir a informação protegida.

### 4.4 Conteúdo restrito

É proibido registrar no Git, em issues, PRs, comentários, logs ou documentação:

- tokens;
- senhas;
- chaves privadas;
- códigos de recuperação;
- cookies ou sessões;
- segredos de API;
- arquivos de credenciais;
- respostas individuais de pesquisa;
- dados pessoais não anonimizados;
- dumps de bancos ou configurações que contenham segredos.

## 5. Classificação das famílias auditadas

| Família | Classe mínima | Publicação permitida |
|---|---|---|
| documentos públicos institucionais aprovados | `public` | conteúdo aprovado e versionado |
| drafts de governança e arquitetura | `internal` | síntese, proveniência e disposição |
| família `GC-CON-001` | `internal` até revisão individual | metadados e resolução de linhagem; PDFs bloqueados |
| plano de proteção corporativa | `confidential` | somente existência, estado e pacote P3 |
| marcas, domínios, DNS e certificados | `confidential` | síntese sem inventário operacional |
| credenciais de registradores, DNS, GitHub ou nuvem | `restricted` | nenhuma publicação |
| contratos, comprovantes e documentos jurídicos | `confidential` ou `restricted` | metadados mínimos; íntegra fora do GKR |
| clientes, parceiros, faturamento e negociação | `confidential` | claims somente com autorização e evidência sanitizada |
| respostas brutas de pesquisa | `restricted` | apenas dados agregados e anonimizados |
| métricas agregadas aprovadas | `public` ou `internal` | conforme autorização de divulgação |
| runbooks sem segredos | `internal` | versão sanitizada pode ser publicada |
| tokens, chaves, sessões e dados de acesso | `restricted` | proibido |
| dados de localização e integração individual | `restricted` | proibido sem base legal, minimização e anonimização |

## 6. Gate antes do commit

Antes de criar ou atualizar um arquivo, o responsável deverá responder:

1. O repositório é público?
2. O conteúdo possui dados pessoais?
3. Há credenciais, URLs privadas ou identificadores operacionais?
4. Há estratégia, contrato, ativo ou negociação protegida?
5. A Guivos possui direito de publicação?
6. Uma síntese atenderia ao objetivo sem expor a íntegra?
7. A autoridade e o limite de maturidade estão explícitos?

Qualquer resposta de risco bloqueia o commit até sanitização ou mudança de destino.

## 7. Resposta a exposição acidental

Caso conteúdo sensível seja publicado:

1. interromper novas divulgações;
2. revogar imediatamente credenciais ou segredos afetados;
3. remover o conteúdo da superfície ativa;
4. avaliar limpeza de histórico quando necessária;
5. registrar o incidente em ambiente apropriado;
6. revisar logs, forks, artefatos e caches;
7. corrigir o controle que permitiu a exposição.

A simples exclusão de um arquivo não revoga um segredo já exposto.

## 8. Resultado do P0

A pendência de classificação de sigilo está encerrada no nível de controle.

A classificação individual de cada ativo ou evidência continuará sob responsabilidade do pacote temático correspondente, sem autorização para publicar conteúdo integral no GKR público.
