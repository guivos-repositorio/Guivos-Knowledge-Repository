# Proposta de liberação controlada — Neo4j AuraDB (somente conectividade)

**Estado:** PROPOSTA — sujeita a revisão e decisão institucional GKR/GIA. Não é autorização operacional vigente.

**Data:** 2026-10-29  
**Rastreabilidade:** Issue #718; Jornada da Pessoa (Replit); ADR-007; ADR-008; GIA-COG-001; GAI-001.

## Objetivo e limites
Verificar exclusivamente a conectividade entre o ambiente isolado da Jornada da Pessoa e uma instância Neo4j AuraDB já criada pelo responsável pelo projeto. A verificação proposta é uma única transação de leitura contendo `RETURN 1`, sem leitura de nós, arestas ou propriedades, sem gravação, criação de schema, migração, dados reais da Pessoa ou Graph Analytics.

**Autorização expressa do titular, já relatada:** avançar na integração Neo4j com dados sintéticos e validar conectividade. Essa manifestação não substitui as demais atribuições de aprovação previstas na governança.

## Estado técnico constatado (não homologado)
- As quatro variáveis `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` e `NEO4J_DATABASE` estão presentes no Replit, sem leitura de seus valores.
- Driver oficial, adaptador preparatório e comando privado read-only estão presentes; checklist operacional existe.
- Última execução informada: 461 testes locais aprovados, em 24 arquivos; 17 testes de memória e 6 do checklist/comandos.
- `memory:readiness` e prontidão específica para conectividade retornam `ready:false`.
- Nenhuma conexão efetiva, verificação TLS, autenticação ou uso de AuraDB foi comprovado.
- `MEMORY_OPERATIONAL_RELEASE=false` permanece; `cognition:false` e `asr:false` públicos permanecem.

## Condições necessárias antes de liberar um teste
1. **Identidade e escopo:** identificar instância, banco, hostname autorizado, operador com UID, limites e finalidade; registrar referência de autorização verificável.
2. **Ambiente:** atestar e verificar isolamento de desenvolvimento, sem endpoints públicos ou dados da Pessoa.
3. **Segurança e acesso:** TLS e hostname permitido, menor privilégio, segredos somente no Replit, redaction de logs, limite de conexão, timeout, kill switch e possibilidade de revogação.
4. **Privacidade, retenção e ownership:** estabelecer responsabilidades legítimas, ausência de dados reais enviados na POC, política de logs, armazenamento, descarte e tratamento de falhas.
5. **Custos:** confirmar plano e condições da instância pré-existente; não provisionar recursos adicionais, e não transferir orçamentos de provedores cognitivos.
6. **Responsabilidade e evidência:** vincular aprovações reais por competência (com responsável, data, validade e limites). Os campos `_REF` não comprovam aprovação só por estarem preenchidos.
7. **Liberação institucional específica:** decisão expressa GKR/GIA sobre o teste somente leitura e mudança governada de `MEMORY_OPERATIONAL_RELEASE` para o âmbito limitado, apenas após todos os controles.

## Critério de sucesso
Um teste autorizado e auditável `RETURN 1` em sessão READ, resultado esperado `1`, evidência de conectividade TLS/autenticação, horário, ambiente e identificador de execução, sem credenciais ou informações de banco em logs. Caso qualquer gate falhe, nenhuma conexão deve ocorrer.

## Depois do teste
Voltar o kill switch ao estado restritivo; registrar os resultados e eventuais custos; anexar evidências à Issue #718; considerar, em decisão separada, testes de CRUD com corpus sintético e esquema aprovado. Graph Analytics, ASR e cognição pública permanecem fora do escopo.

## Decisão pendente
Esta proposta **não altera** ADR-007/ADR-008 nem autoriza sua implementação física ou uso de dados reais. A autoridade institucional competente deve aceitar, alterar ou rejeitar o escopo e documentar a decisão antes de qualquer conexão.
