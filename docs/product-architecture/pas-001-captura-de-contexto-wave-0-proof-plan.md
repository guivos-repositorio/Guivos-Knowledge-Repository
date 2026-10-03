---
id: PAS-001-CC-W0-POC-001
title: Plano de Provas Técnicas da Onda 0
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-W0-ENV-001
  - PAS-001-CC-UIC-NFR-SECURITY-001
  - PAS-001-CC-UIC-READINESS-001
---

# PAS-001-CC-W0-POC-001 — Plano de Provas Técnicas da Onda 0

> POC reduz incerteza técnica. Não é produção, não é decisão permanente e não substitui evidência de integração quando seu ambiente ou mecanismo não é representativo.

## 1. Regras gerais

Cada prova deverá registrar:

- `poc_id`;
- hipótese;
- requisito e ADR relacionados;
- ambiente;
- dados utilizados;
- configuração;
- método reproduzível;
- critérios de sucesso e falha;
- resultado observado;
- limitações;
- risco residual;
- recomendação;
- validade temporal;
- owner e aprovador.

## 2. POC-01 — Persistência, concorrência e idempotência

### Hipótese

É possível persistir o agregado e publicar fatos funcionais sem perda de atomicidade, sobrescrita silenciosa ou duplicidade material.

### Escopo

- versão esperada;
- conflito concorrente;
- chave de idempotência;
- mesma chave com payload divergente;
- persistência e publicação;
- retry após falha parcial;
- reconstrução a partir de estado e eventos.

### Cenários mínimos

1. dois comandos concorrentes sobre a mesma versão;
2. retry do mesmo comando após timeout;
3. mesma chave com payload material diferente;
4. persistência concluída e publicação indisponível;
5. publicação duplicada;
6. evento fora de ordem;
7. reconstrução após falha de projeção.

### Critérios de sucesso

- nenhuma atualização válida é perdida silenciosamente;
- conflito retorna código estável;
- retry idêntico retorna resultado anterior;
- payload divergente é rejeitado;
- evento é publicável após recuperação;
- duplicidade não produz novo efeito material;
- replay não cria novo fato humano.

### Evidências

`EV-003`, `EV-007`, `EV-015`.

## 3. POC-02 — Conteúdo protegido e multimodalidade mínima

### Hipótese

É possível manter conteúdo protegido separado do registro funcional, com integridade, acesso temporário, expiração e exclusão por camada.

### Escopo

- uma mídia binária representativa;
- documento textual protegido;
- referência opaca;
- hash e proveniência;
- criptografia;
- acesso temporário;
- quarentena;
- retenção e exclusão;
- backup e restore;
- rotação de chave.

### Cenários mínimos

1. upload válido;
2. tipo declarado incompatível;
3. mídia maliciosa;
4. referência expirada;
5. acesso sem finalidade;
6. exclusão lógica e física;
7. restore após revogação;
8. derivado órfão;
9. rotação de chave.

### Critérios de sucesso

- conteúdo bruto não entra no registro funcional;
- referência não é enumerável;
- acesso exige política válida;
- mídia não confiável permanece isolada;
- restore não reativa conteúdo excluído ou revogado;
- integridade é verificável;
- derivado mantém vínculo com a fonte;
- exclusão por camada produz evidência.

### Evidências

`EV-008`, `EV-009`, `EV-016`.

## 4. POC-03 — Mensageria, consumidor, correção e revogação

### Hipótese

É possível coordenar efeitos distribuídos e comprovar aplicação de correção e revogação sem confundir entrega com conclusão.

### Escopo

- consumidor mínimo;
- registro de finalidade e retenção;
- entrega duplicada;
- retry e backoff;
- consumidor offline;
- dead letter ou quarentena equivalente;
- correção;
- revogação;
- tracking de confirmação;
- retenção residual;
- kill switch.

### Cenários mínimos

1. consumidor online;
2. consumidor atrasado;
3. consumidor incompatível;
4. consumidor comprometido;
5. correção parcialmente aplicada;
6. revogação com retenção residual legítima;
7. revogação sem resposta no prazo;
8. suspensão e retomada controlada.

### Critérios de sucesso

- entrega não marca aplicação automaticamente;
- bloqueio central impede novos recortes;
- consumidor atrasado é detectado;
- retenção residual possui fundamento e validade;
- kill switch impede novas mensagens;
- aplicação é rastreável por versão contratual;
- falha crítica é escalada.

### Evidências

`EV-006`, `EV-012`, `EV-014`.

## 5. POC-04 — Busca protegida e índice revogável

### Hipótese

É possível recuperar conteúdo autorizado com filtro anterior à busca, isolamento entre participantes e reconstrução a partir do registro funcional.

### Escopo

- política `prohibited`;
- `metadata_only`;
- índice privado do participante;
- finalidade e escopo;
- snippets redigidos;
- correção;
- revogação;
- índice temporário;
- reconstrução;
- avaliação vetorial opcional.

### Cenários mínimos

1. conteúdo proibido para índice;
2. metadado permitido;
3. tentativa de consulta cruzada;
4. finalidade incompatível;
5. revogação durante cache ativo;
6. correção após indexação;
7. índice perdido e reconstruído;
8. embedding revogado, quando testado.

### Critérios de sucesso

- zero resultado entre participantes;
- filtro ocorre antes da recuperação;
- conteúdo proibido não produz índice;
- revogação remove novos resultados dentro do SLO candidato;
- correção atualiza estado visível;
- índice pode ser reconstruído sem se tornar fonte de verdade;
- snippet não amplia exposição.

### Evidências

`EV-010`, com apoio de `EV-004`, `EV-006` e `EV-007`.

## 6. POC-05 — Observabilidade segura e recuperação

### Hipótese

É possível observar fluxos críticos, diagnosticar falhas e medir SLOs sem registrar conteúdo sensível bruto.

### Escopo

- correlação opaca;
- logs redigidos;
- métricas de negócio técnico;
- tracing;
- alertas;
- backlog por idade;
- propagação de correção e revogação;
- RPO/RTO;
- falha de observabilidade;
- runbooks.

### Cenários mínimos

1. comando rejeitado;
2. conflito de versão;
3. consumidor atrasado;
4. backlog crescente;
5. revogação fora do SLO;
6. restauração após falha;
7. conteúdo proibido injetado em campo de erro;
8. perda parcial de telemetria.

### Critérios de sucesso

- zero conteúdo sensível bruto em logs;
- fluxo C0/C1 é correlacionável;
- alerta identifica risco sem expor conteúdo;
- SLIs são calculáveis;
- RPO e RTO são medidos;
- falha de observabilidade gera degradação segura;
- runbook possui owner e condição de escalonamento.

### Evidências

`EV-005`, `EV-008`, `EV-013`.

## 7. POC-06 — Segurança de modelos e Intelligence

### Hipótese

É possível usar modelo para derivação limitada sem permitir que conteúdo capturado altere instruções de sistema, conceda autoridade ou seja tratado como confirmação humana.

### Escopo

- conteúdo textual e multimodal como dado;
- prompt injection;
- versionamento de modelo e prompt;
- classificação de saída;
- proveniência;
- minimização;
- revogação de derivados;
- ausência de autoridade;
- saída insegura ou incerta.

### Cenários mínimos

1. instrução maliciosa no texto capturado;
2. instrução maliciosa em documento;
3. tentativa de confirmar fato via modelo;
4. tentativa de ampliar finalidade;
5. saída com confiança insuficiente;
6. mudança de versão do modelo;
7. revogação da fonte;
8. consumidor solicitando dado excessivo.

### Critérios de sucesso

- conteúdo não altera instruções de sistema;
- modelo não confirma nem autoriza;
- saída permanece interpretação ou hipótese;
- versão e proveniência são rastreáveis;
- revogação alcança derivados aplicáveis;
- dado excessivo é minimizado ou negado;
- comportamento inseguro falha fechado.

### Evidência

`EV-011`, com apoio de `EV-004`, `EV-006` e `EV-016`.

## 8. Ordem recomendada

```text
POC-01
  ├──→ POC-02
  ├──→ POC-03
  └──→ POC-04
          ↓
        POC-05
          ↓
        POC-06
```

POC-06 pode iniciar antes como análise isolada, mas só produz evidência válida quando usa contratos, classificação e controles representativos.

## 9. Critérios de encerramento de POC

Uma POC termina como:

- `validated`: hipótese comprovada no escopo;
- `partially_validated`: parte comprovada e limitações registradas;
- `rejected`: hipótese não suportada;
- `inconclusive`: método ou ambiente insuficiente;
- `superseded`: substituída por prova posterior.

Somente `validated` e `partially_validated` com risco aceito podem informar ADR. Nenhuma POC autoriza produção.

## 10. Critérios de interrupção

Interromper imediatamente quando:

- houver dado não autorizado;
- ocorrer vazamento cruzado;
- segredo for exposto;
- revogação falhar em bloquear novos usos;
- tecnologia exigir relaxar autoridade normativa;
- mídia maliciosa escapar da quarentena;
- modelo produzir ação material não autorizada;
- método não permitir reprodução.

## 11. Saída para ADRs

Cada POC deverá alimentar o registro de decisões com:

- requisito comprovado ou não;
- limites observados;
- custos e complexidade;
- riscos;
- portabilidade;
- impacto operacional;
- decisão recomendada;
- necessidade de prova adicional.