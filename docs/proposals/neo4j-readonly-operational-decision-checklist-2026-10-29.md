# Checklist consolidado de decisão — conectividade Neo4j AuraDB (POC)

**Estado: revisão pendente. Este documento não concede, por si só, liberação operacional.**
Relacionamentos: PR #719; Issue #718; ADR-007; ADR-008; GIA-COG-001.

## Evidência técnica já obtida
- O titular autorizou uma tentativa privada **somente leitura** com consulta fixa `RETURN 1`.
- Quatro variáveis Neo4j presentes; `MEMORY_OPERATOR_UID` corresponde ao processo; URI possui sintaxe e esquema TLS válidos; HOST equivale ao hostname da URI; DATABASE possui formato válido.
- `memory:config-check` retornou `ok:true`, `networkAttempted:false`, sem expor valores.
- Nenhuma validação DNS, TLS real, autenticação ou acesso ao banco ocorreu.
- Readiness operacional continua fechado; `MEMORY_OPERATIONAL_RELEASE=false`.

## Escopo único proposto
Uma única transação READ `RETURN 1`, sem leitura de nós/arestas, gravação, schema, Graph Analytics, serviços cognitivos, dados reais ou dados sintéticos armazenados. O uso deve estar limitado a ambiente de desenvolvimento efetivamente isolado.

## Decisão institucional consolidada — campos a revisar
| Dimensão | Evidência exigida |
| --- | --- |
| Scope | Escopo, finalidade, uma tentativa, duração e limites |
| Host scope | Identificação inequívoca da instância/database autorizados em registro privado, confrontados independentemente no painel Aura |
| Ownership | Autoridade competente GIA/GKR e responsável legal/técnico |
| Private access | Autenticação real do operador, permissões, acesso restrito ao teste |
| Security | TLS, allowlist, timeout, logging sanitizado, controle de revogação e kill switch |
| Privacy | Nenhuma consulta à Pessoa, tratamento de logs e restrições de dados |
| Retention | Prazo e descarte de logs e artefatos de teste |
| Cost | Plano real da instância Aura, titular da cobrança e eventuais limites; não usar orçamento de IA |
| Synthetic corpus | Sem corpus para o teste read-only; não gravar dados nem carregar fixtures |
| Operational approval | Aprovação por competência expressa para esta tentativa e para rever o gate, com data e validade |

**Referências:** `MEMORY_SCOPE_REF`, `MEMORY_HOST_SCOPE_REF`, `MEMORY_OWNERSHIP_REF`, `MEMORY_PRIVATE_ACCESS_REF`, `MEMORY_SECURITY_REF`, `MEMORY_PRIVACY_REF`, `MEMORY_RETENTION_REF`, `MEMORY_COST_REF`, `MEMORY_SYNTHETIC_CORPUS_REF`, `MEMORY_OPERATIONAL_APPROVAL_REF`. Essas referências podem apontar a uma decisão consolidada *aprovada*, mas um texto/URL preenchido não comprova aprovação.

## Qualificação de ambiente
A última auditoria indicou falha de isolamento: `NODE_ENV=development` falso, `MEMORY_ENVIRONMENT=isolated-development` falso e marcador gerenciado ainda indicando produção. **Não falsificar ou sobrescrever marcadores gerenciados**. Identificar um workspace/execução realmente de desenvolvimento e reproduzir nele as configurações seguras.

## Critérios de liberação e de conclusão
Antes: responsáveis e decisões rastreáveis, ambiente qualificado, gates explícitos satisfeitos e alteração governada/reversível de `MEMORY_OPERATIONAL_RELEASE`. Durante: uma tentativa apenas de `RETURN 1`, sem credenciais em logs. Depois: desligar execução e kill switch; anexar resultados saneados e quaisquer custos; avaliação humana e atualização da Issue #718. Falhas implicam interrupção.

## Decisão
**Pendente** — sem assinaturas ou revisões institucionais registradas neste documento. Não se deve considerar a aprovação genérica do titular como preenchimento de todas as dimensões.
