---
id: GKR-EXT-SOURCE-PRESERVATION-001
title: Decisão de Preservação e Referência de Fontes Externas
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
  - GKR-LINEAGE-GC-CON-001-001
related:
  - GKR-INFO-CLASS-001
  - GKR-P0-CLOSURE-001
normative: false
---

# Decisão de Preservação e Referência de Fontes Externas

## 1. Finalidade

Definir como PDFs, rascunhos, planos, manuscritos, evidências operacionais e demais fontes externas devem ser preservados sem criar autoridade concorrente, expor informação sensível ou poluir o Guivos Knowledge Repository.

Esta decisão encerra a pendência do P0 sobre armazenar ou apenas referenciar fontes históricas.

## 2. Contexto determinante

O repositório `guivos-repositorio/Guivos-Knowledge-Repository` possui visibilidade pública.

Consequentemente, o GKR não deve ser utilizado como arquivo indiscriminado de:

- documentos internos integrais;
- contratos, comprovantes ou evidências jurídicas;
- listas de ativos, domínios, contas ou acessos;
- dados pessoais ou respostas individuais de pesquisa;
- credenciais, tokens, chaves ou segredos;
- materiais de terceiros sem autorização de publicação;
- variantes documentais com linhagem conflitante.

## 3. Decisão

O padrão oficial de intake para fontes externas será **reference-first**.

Isso significa que o GKR público preservará, quando adequado:

1. identificador de intake;
2. título ou descrição sanitizada;
3. tipo documental;
4. versão e status declarados na origem;
5. data conhecida ou aproximada;
6. responsável ou origem, quando publicável;
7. classificação de sensibilidade;
8. disposição de autoridade;
9. relação com documentos integrados;
10. hash criptográfico somente quando o arquivo tiver sido recebido em ambiente controlado e o hash puder ser publicado sem expor informação indevida.

O arquivo binário ou texto integral permanecerá fora do repositório público por padrão.

## 4. Destino físico

Fontes integrais deverão permanecer em um repositório documental controlado, com acesso compatível com sua classificação.

O P0 não define uma plataforma específica. O destino futuro deverá possuir:

- controle de acesso;
- histórico de versões;
- registro de responsável;
- retenção e descarte;
- capacidade de calcular e preservar hashes;
- segregação entre conteúdo público, interno, confidencial e restrito;
- trilha de auditoria.

Uma referência pública nunca deverá revelar caminho privado, URL assinada, credencial, nome de conta, segredo ou estrutura que facilite acesso indevido.

## 5. Exceção para incorporação integral

Uma fonte externa somente poderá ser copiada integralmente para o GKR quando todos os gates abaixo forem atendidos:

1. titularidade ou licença de publicação confirmada;
2. classificação `public` confirmada;
3. ausência de dados pessoais, segredos e informação comercial protegida;
4. linhagem documental resolvida;
5. relação com a Canon explicitada;
6. necessidade arquitetural demonstrada;
7. revisão editorial e de segurança concluída;
8. branch e PR próprios;
9. validação mecânica aprovada;
10. autorização explícita de integração.

## 6. Família `GC-CON-001`

Para a família `GC-CON-001`:

- nenhum PDF externo será importado como release canônica;
- nenhuma variante será publicada como `1.0`;
- os arquivos deverão ser individualizados antes de qualquer intake físico;
- hashes somente serão calculados em ambiente controlado;
- o GKR poderá manter metadados e a resolução de linhagem;
- eventual manuscrito consolidado deverá receber processo editorial, evidência, revisão e autorização próprios.

A ausência de hashes públicos não invalida a resolução de autoridade já registrada. Ela apenas mantém pendente a identificação física de cada exemplar.

## 7. Estados de preservação

| Estado | Significado |
|---|---|
| `reference_only` | metadados e disposição registrados; conteúdo integral fora do GKR |
| `controlled_archive` | conteúdo integral em ambiente restrito e auditável |
| `public_copy_authorized` | cópia integral autorizada após todos os gates |
| `hash_pending` | arquivo conhecido, mas ainda não recebido em ambiente controlado |
| `publication_blocked` | publicação proibida por sigilo, direitos, dados pessoais ou conflito de linhagem |
| `discard_authorized` | descarte formal permitido após retenção e revisão aplicáveis |

## 8. Regra de autoridade

Referenciar, arquivar ou calcular o hash de uma fonte não a promove à Canon.

A autoridade somente poderá mudar por meio do pipeline institucional de evidência, consolidação, validação, auditoria e decisão formal.

## 9. Resultado do P0

A pendência de destino das fontes históricas está encerrada no nível de controle:

- padrão adotado: `reference_only` no GKR público;
- conteúdo integral: ambiente controlado, quando necessário;
- hashes: condicionados ao intake físico autorizado;
- publicação integral: exceção sujeita a gates;
- promoção canônica: não autorizada por esta decisão.
