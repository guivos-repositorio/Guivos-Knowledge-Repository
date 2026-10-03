---
id: PAS-001-CC-UIC-STORAGE-INDEX-001
title: Armazenamento Multimodal e Indexação Sensível da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-UIC-001
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
---

# PAS-001-CC-UIC-STORAGE-INDEX-001 — Armazenamento Multimodal e Indexação Sensível

> **Estado:** `Draft 0.1.0 — Storage and sensitive indexing technically defined`.
>
> Este documento resolve logicamente `UIC01-GAP-003` e `UIC01-GAP-008`. Ele não escolhe banco, object storage, mecanismo de busca, nuvem, biblioteca criptográfica ou topologia física.

## 1. Objetivo

Definir como a UIC-01 deverá armazenar, proteger, localizar, corrigir, revogar, excluir e reconstruir conteúdo e metadados sem transformar índices, caches, projeções ou derivados em sistema de registro.

A arquitetura deverá preservar:

1. separação entre conteúdo multimodal e registro funcional;
2. rastreabilidade entre original, transcrição, interpretação, confirmação e autorização;
3. minimização por finalidade;
4. revogação de novos usos;
5. correção compensatória e imutável;
6. distinção entre exclusão lógica, física e criptográfica;
7. isolamento entre participantes;
8. impossibilidade de ampliar autoridade por indexação.

## 2. Camadas lógicas de persistência

| Camada | Conteúdo | Autoridade |
|---|---|---|
| Registro funcional | estados, eventos, versões, autorizações, correções e revogações | sistema de registro da UIC-01 |
| Conteúdo protegido | mídia original, documentos, texto sensível e anexos | referência protegida vinculada ao registro funcional |
| Derivados controlados | transcrições, miniaturas, embeddings, classificações e interpretações | derivados rastreáveis, nunca fatos humanos por si mesmos |
| Índices protegidos | tokens, metadados, filtros e referências pesquisáveis | mecanismo de localização, não autoridade |
| Projeções e caches | visões de leitura e resultados temporários | descartáveis e reconstruíveis |
| Evidências técnicas | hashes, versões, confirmações de processamento e trilhas permitidas | comprovação técnica, não conteúdo funcional substituto |

Nenhuma camada poderá substituir silenciosamente o registro funcional.

## 3. Identificadores e referências

- `capture_record_id` identifica o agregado funcional;
- `capture_input_id` identifica permanentemente uma entrada original;
- `content_object_id` identifica um objeto protegido, sem significado funcional embutido;
- `derivative_id` identifica um derivado e exige `source_reference`;
- `index_entry_id` identifica uma entrada de índice revogável;
- `snapshot_id` identifica uma fotografia reconstruível do estado;
- hashes comprovam integridade e não substituem identidade;
- IDs físicos de storage, fila ou mecanismo de busca não deverão aparecer como IDs funcionais públicos.

## 4. Matriz de armazenamento multimodal

| Categoria | Forma preferencial | Inline permitido | Integridade | Retenção-base | Indexação-base |
|---|---|---:|---|---|---|
| Texto curto não sensível | registro funcional ou referência | condicional | hash + versão | finalidade | metadados/protegida |
| Texto pessoal ou sensível | referência protegida | excepcional | hash + versão | finalidade | protegida ou proibida |
| Voz e áudio | objeto protegido | não | hash do original | finalidade | metadados; conteúdo protegido |
| Imagem | objeto protegido | não | hash do original | finalidade | metadados; derivados controlados |
| Vídeo | objeto protegido | não | hash do original | finalidade | metadados; derivados controlados |
| Documento | objeto protegido | não | hash do original | finalidade | metadados; conteúdo protegido |
| Seleção estruturada | registro funcional | sim | versão do schema | funcional | metadados |
| Resposta estruturada | registro funcional | sim | versão do schema | funcional | metadados/protegida |
| Dado importado | objeto ou registro segregado | condicional | hash + proveniência | finalidade | conforme classificação |
| Transcrição | derivado protegido | não para sensível | fonte + versão | acompanha fonte | protegida |
| Interpretação | derivado protegido | não para sensível | fontes + versão | finalidade | protegida ou proibida |
| Confirmação humana | registro funcional | sim | evento + versão | funcional | metadados |
| Autorização | registro funcional segregado | sim, sem segredo | evento + versão | prazo autorizado | metadados restritos |
| Correção | evento compensatório | sim | causalidade | funcional | atualização compensatória |
| Revogação | processo funcional | sim | causalidade | funcional | remoção/bloqueio imediato |
| Snapshot | armazenamento protegido | não | hash + versão | operacional | não pesquisável por conteúdo |

## 5. Regras de conteúdo inline

Conteúdo inline somente será admitido quando todas as condições forem verdadeiras:

1. o schema permitir explicitamente;
2. o tamanho estiver dentro do limite lógico definido para a implementação;
3. a classificação não for `highly_sensitive`;
4. o conteúdo não for binário;
5. logs e telemetria não capturarem o payload;
6. a finalidade autorizar persistência funcional;
7. a exclusão e a revogação puderem ser aplicadas de forma verificável.

Quando qualquer condição falhar, deverá ser usada referência protegida.

## 6. Criptografia e gestão de chaves

A implementação deverá garantir:

- criptografia em trânsito para todas as comunicações materiais;
- criptografia em repouso para conteúdo protegido, snapshots, backups e índices sensíveis;
- possibilidade de segregação de chaves por ambiente, classe de sensibilidade ou domínio de proteção;
- rotação de chaves sem perda de rastreabilidade;
- proibição de chaves, tokens e segredos em payloads funcionais;
- evidência de acesso a operações criptográficas administrativas;
- capacidade de exclusão criptográfica quando a exclusão física imediata não for tecnicamente possível;
- tratamento explícito de caches e réplicas durante rotação, revogação e exclusão.

A escolha de KMS, HSM ou biblioteca permanece para ADR tecnológico posterior.

## 7. Retenção

### 7.1 Modos

| Modo | Regra |
|---|---|
| Temporária | expira ao final da sessão ou janela operacional definida |
| Vinculada à finalidade | persiste enquanto a finalidade e a base autorizadora estiverem válidas |
| Persistente autorizada | exige autorização explícita, prazo ou critério de revisão |
| Residual técnica | somente quando necessária para integridade, obrigação ou recuperação, sem novo uso funcional |

### 7.2 Regras

- retenção do derivado não poderá exceder silenciosamente a da fonte;
- autorização expirada bloqueia novos usos mesmo antes da eliminação física;
- backup não amplia prazo funcional;
- retenção residual deverá ser marcada, inacessível a fluxos comuns e periodicamente revisada;
- dados de terceiros, menores e altamente sensíveis exigem política reforçada;
- cada classe deverá possuir `retention_policy_id` versionado.

## 8. Exclusão

| Modalidade | Uso |
|---|---|
| Lógica | retirada imediata do uso funcional e das projeções |
| Física | remoção do conteúdo dos armazenamentos ativos |
| Criptográfica | inutilização por destruição ou segregação definitiva de chave |
| Expiração | remoção automática por política temporal |
| Residual controlada | preservação mínima, segregada e sem novo uso |

A conclusão de exclusão exige evidência por camada. Remover do índice não equivale a remover do registro, do objeto, do cache ou do backup.

## 9. Correção

- o conteúdo original e seus eventos não são sobrescritos como se nunca tivessem existido;
- a correção cria nova versão ou referência compensatória;
- derivados afetados são marcados como superseded, invalidated ou pending_rebuild;
- índices são atualizados por compensação;
- consumidores recebem mensagem de correção e confirmam aplicação quando exigido;
- reconstrução deverá produzir o estado corrigido sem apagar a história causal;
- resultados antigos não podem continuar sendo apresentados como atuais.

## 10. Revogação

A revogação deverá:

1. bloquear novas leituras e novos usos no ponto de autorização;
2. retirar resultados dos índices e caches ativos;
3. invalidar links temporários e credenciais derivadas;
4. emitir mensagem funcional de revogação;
5. acompanhar confirmações dos consumidores;
6. marcar conteúdo residual como indisponível para uso funcional;
7. preservar somente evidência mínima permitida;
8. gerar alerta quando algum consumidor não confirmar dentro do SLO.

Revogação distribuída concluída e bloqueio imediato são estados distintos.

## 11. Backups e restauração

- backups deverão ser criptografados e segregados por ambiente;
- restauração não poderá reativar conteúdo revogado ou expirado;
- após restore, deverão ser reaplicados tombstones, revogações, correções e políticas de retenção;
- testes de restauração deverão comprovar integridade e isolamento;
- conteúdo residual em backup não poderá ser pesquisado ou utilizado operacionalmente;
- a janela máxima de perda e o tempo de recuperação serão definidos no documento de SLOs;
- restauração deverá registrar evidência sem expor conteúdo bruto.

## 12. Política de indexação

### 12.1 Classes

| Classe | Descrição |
|---|---|
| `prohibited` | nenhum conteúdo ou derivado pesquisável |
| `metadata_only` | apenas metadados minimizados e autorizados |
| `protected` | conteúdo ou representação pesquisável em domínio protegido |
| `participant_private` | pesquisável somente pelo participante ou representante autorizado |
| `purpose_scoped` | pesquisável por consumidor autorizado para finalidade específica |
| `temporary` | índice de sessão ou processamento com expiração curta |

### 12.2 Regras invariantes

1. índice não é sistema de registro;
2. resultado de busca não amplia finalidade, autoridade ou prazo;
3. consultas deverão ser escopadas por participante antes de filtros de conteúdo;
4. nenhum resultado poderá misturar participantes;
5. snippets respeitam a classificação do conteúdo original;
6. interpretações e hipóteses preservam sua natureza no resultado;
7. conteúdo não confirmado não poderá ser rotulado como fato confirmado;
8. entradas possuem fonte, versão, finalidade e política de revogação;
9. índice incompatível com a versão do contrato deverá ser isolado ou reconstruído;
10. logs de consulta não poderão conter conteúdo sensível bruto.

## 13. Embeddings e representações vetoriais

Embeddings são derivados potencialmente sensíveis.

- deverão possuir `source_reference`, `model_reference`, versão e finalidade;
- não poderão ser reutilizados para finalidade diferente sem nova autorização;
- deverão ser revogáveis e reconstruíveis;
- não poderão ser exportados como substitutos neutros do conteúdo;
- deverão ser segregados entre participantes;
- risco de reidentificação deverá ser considerado;
- consultas vetoriais deverão aplicar autorização antes da recuperação material;
- retenção não poderá exceder a fonte sem justificativa formal.

## 14. Pipeline de indexação

```text
Fonte autorizada
  -> classificação e finalidade
  -> minimização
  -> política de índice
  -> geração de representação permitida
  -> validação de isolamento
  -> gravação da entrada versionada
  -> confirmação técnica
  -> disponibilidade para consulta autorizada
```

Falha em qualquer etapa mantém o conteúdo fora do índice ou em quarentena.

## 15. Pipeline de consulta

```text
Ator autenticado
  -> autoridade e finalidade
  -> escopo do participante
  -> política de sensibilidade
  -> consulta minimizada
  -> recuperação protegida
  -> filtragem pós-recuperação
  -> redaction e apresentação
  -> evidência permitida
```

Autorização após a recuperação é insuficiente. O escopo deverá ser aplicado antes de recuperar conteúdo material.

## 16. Logs, métricas e telemetria

Permitidos:

- IDs opacos;
- códigos de política;
- versões;
- latências;
- contagens;
- estados técnicos;
- códigos de erro;
- indicadores de redaction.

Proibidos por padrão:

- conteúdo bruto;
- transcrição integral;
- documento;
- mídia;
- prompt contendo dados pessoais;
- embedding;
- segredo;
- autorização material completa;
- snippet sensível.

## 17. Reconstrução

A reconstrução deverá combinar:

1. histórico funcional válido;
2. snapshot compatível, quando disponível;
3. correções e revogações posteriores;
4. políticas atuais de acesso e retenção;
5. referências de conteúdo ainda autorizadas.

Ela não deverá:

- reativar conteúdo revogado;
- republicar eventos como novas manifestações;
- reconstruir índice proibido;
- converter derivado em confirmação;
- perder proveniência ou natureza da informação.

## 18. Falhas seguras

| Falha | Comportamento seguro |
|---|---|
| Política ausente | negar persistência material ou indexação |
| Chave indisponível | indisponibilidade controlada, sem fallback em claro |
| Índice atrasado | resultado incompleto explicitado, sem ampliar escopo |
| Revogação pendente | bloquear novos usos |
| Derivado sem fonte | quarentena |
| Restore incompatível | impedir ativação |
| Hash divergente | isolar conteúdo e abrir incidente |
| Consumidor sem confirmação | manter acompanhamento e impedir conclusão distribuída |

## 19. Testes obrigatórios

1. isolamento entre participantes;
2. proibição de conteúdo altamente sensível inline;
3. expiração de índice temporário;
4. bloqueio imediato após revogação;
5. reconstrução sem reativação;
6. restore com reaplicação de tombstones;
7. correção de derivado e índice;
8. retenção do derivado limitada pela fonte;
9. consulta vetorial com autorização prévia;
10. ausência de conteúdo bruto em logs;
11. segregação de backups;
12. incompatibilidade de schema em índice;
13. exclusão lógica, física e criptográfica rastreáveis;
14. acesso por finalidade;
15. preservação da natureza de interpretação e hipótese.

## 20. Evidências mínimas

- matriz de classes de armazenamento implementada;
- inventário de políticas de retenção;
- relatório de criptografia por camada;
- teste de restauração;
- teste de revogação e remoção de índice;
- teste de isolamento;
- prova de redaction de logs;
- inventário de derivados;
- relatório de entradas incompatíveis ou em quarentena;
- métricas de latência de correção e revogação.

## 21. Gaps resolvidos

- `UIC01-GAP-003 — armazenamento multimodal`: `Resolved by technical definition`;
- `UIC01-GAP-008 — busca e indexação sensível`: `Resolved by technical definition`.

A resolução documental não equivale a implementação comprovada. A Onda 0 deverá produzir as evidências exigidas.

## 22. Limites

Este documento não escolhe tecnologia, não autoriza produção, não define preço ou capacidade física e não transforma índice, embedding, cache, transcrição ou interpretação em fato humano ou autoridade funcional.