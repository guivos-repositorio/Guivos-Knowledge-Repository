---
id: GKR-UX-EVALUATION-REPUTATION-AUTHORITY-001
title: Avaliação e Reputação — Autoridade Canônica
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
depends_on:
  - UXA-057
related:
  - GKR-JOURNEY-PERSON-FUNCTIONAL-COMPLETENESS-001
  - GKR-UX-EVALUATION-REPUTATION-HUMAN-ADJUDICATION-DOSSIER-001
  - GKR-UX-EVALUATION-REPUTATION-PERSON-SURFACE-PARTITION-001
  - GKR-UX-EVALUATION-REPUTATION-CONTEXTUAL-DISPLAY-AUTHORITY-001
  - GKR-UX-EVALUATION-REPUTATION-RESPONSE-GOVERNANCE-001
  - GKR-UX-EVALUATION-REPUTATION-HANDOFF-MATRIX-001
---

# Avaliação e Reputação — Autoridade Canônica

## 1. Finalidade

Esta autoridade consolida a decisão canônica da Guivos sobre **avaliações de experiências e reputação contextual**.

Ela governa o significado, as fronteiras e as autoridades do domínio. Não cria, por si só, tela, rota, `PER-ID`, `ORG-ID`, `COL-ID`, `TRN-ID`, implementação, algoritmo de ranking ou identidade visual.

## 2. Regra central

A Guivos não trata reputação como uma nota universal sobre uma Pessoa, Organização, Coletivo ou oportunidade.

O contrato canônico é:

```text
EXPERIÊNCIA REAL E DELIMITADA
→ ELEGIBILIDADE E PROVENIÊNCIA
→ AVALIAÇÃO PROTEGIDA
→ OBJETO PRIVADO AUTORITATIVO
→ PUBLICAÇÃO AUTORIZADA
→ OBJETO PÚBLICO DISTINTO
→ APRESENTAÇÃO CONTEXTUAL
→ AGREGAÇÃO E INDICADORES COM LIMITES
```

Governança de resposta, contestação, denúncia, moderação e recurso permanece separada da autoria da avaliação.

## 3. Doze invariantes-mãe

1. **Experiência antes de reputação.** Não existe reputação legítima sem experiência identificável e relação suficiente com o objeto avaliado.
2. **Especificidade de objeto e contexto.** Avaliação pertence a objeto, unidade, edição, etapa, período ou relação materialmente delimitados.
3. **Evidência vinculada ao claim.** Evidência comprova somente aquilo que seu escopo sustenta.
4. **Autoridade privada canônica.** A avaliação submetida possui continuidade privada autoritativa própria.
5. **Separação público/privado.** Publicação não transforma o registro privado em objeto público nem desclassifica toda a origem.
6. **Separação identidade/visibilidade.** Identificação pública, identidade interna, comentário e contribuição agregada possuem escopos próprios.
7. **Autoridade vinculada à finalidade.** Capacidade técnica, acesso, representação, confirmação, resposta, moderação e publicação não são poderes intercambiáveis.
8. **Integridade temporal e versionada.** Critérios, estados, mudanças materiais e políticas precisam permanecer interpretáveis no tempo.
9. **Projeção não é autoridade.** Perfil, busca, feed, cache, índice, analytics, exportação e notificação não substituem o estado competente.
10. **Governança independente e não retaliatória.** Resposta, contestação, denúncia, moderação e recurso têm competências separadas.
11. **Sem propagação universal de reputação.** Uma avaliação não migra automaticamente entre edição, atividade, curso, Coletivo, Organização, certificador, executor ou outra identidade relacionada.
12. **Não ressurreição e integridade histórica.** Restore, backup, replay, cache ou mudança de política não reativam silenciosamente estado legitimamente encerrado ou descartado.

## 4. Unidade avaliável

Uma avaliação precisa ser vinculada, conforme aplicável, a:

- objeto avaliado;
- tipo do objeto;
- unidade, edição, atividade, turma, oportunidade, serviço ou relação;
- etapa efetivamente vivida;
- período;
- papel da Pessoa;
- estado de verificação;
- versão de critérios;
- visibilidade;
- conflitos de interesse e incentivos materialmente relevantes.

Experiências materialmente distintas podem gerar avaliações distintas. Atualização da mesma experiência não deve criar múltiplas avaliações artificiais.

## 5. Elegibilidade e evidência

A elegibilidade depende de relação suficiente entre Pessoa, objeto e experiência.

Categorias de evidência permanecem distinguíveis:

- verificada pela Guivos;
- confirmada por responsável competente;
- declarada pela Pessoa;
- externa identificada;
- insuficiente, conflitante ou revogada.

Visualização, interesse, convite, vínculo social, anúncio, clique ou inscrição em etapa diferente não comprovam automaticamente experiência posterior.

Uma inscrição válida pode comprovar a experiência da própria inscrição quando essa for a etapa avaliada.

## 6. Continuidade privada autoritativa — R1

A avaliação submetida possui um objeto privado autoritativo, aqui referenciado conceitualmente como **R1**.

R1 preserva, quando necessário:

- identidade lógica estável;
- objeto e contexto;
- autoria;
- respostas estruturadas;
- versão de critérios;
- estado de verificação;
- proveniência;
- lifecycle;
- histórico material;
- relações com evidências, publicação e governança.

`R1` não é formulário, cache, índice, log, exportação, confirmação visual ou backup.

### 6.1 Retenção

Continuidade não implica retenção eterna.

Retenção deve ser:

- vinculada a finalidade legítima;
- específica por componente;
- minimizada;
- privada por padrão;
- protegida;
- versionada;
- compatível com exclusão, anonimização ou pseudonimização quando aplicáveis;
- não ressuscitável por backup, restore ou replay.

Evidências, logs, derivados, embeddings, resumos, índices, analytics, caches e exports não recebem retenção ilimitada apenas por derivarem de R1.

## 7. Publicação — P1

Quando houver autoridade suficiente, R1 pode originar um **objeto público distinto**, aqui referenciado conceitualmente como **P1**.

```text
R1
→ PUBLICAÇÃO AUTORIZADA
→ P1
```

`P1 ≠ R1`.

P1 possui:

- identidade pública própria;
- escopo autorizado;
- proveniência suficiente;
- lifecycle;
- versionamento;
- estado de visibilidade;
- relações públicas permitidas;
- semântica de retirada, limitação, substituição ou encerramento.

Publicação alcança somente o conteúdo autorizado. Não converte automaticamente evidência, participação sensível, identidade interna ou outros dados privados em informação pública.

## 8. Identidade e visibilidade da autora

A Pessoa pode, quando o contexto permitir, usar modalidades como:

- nome e perfil públicos;
- nome reduzido;
- identificação como participante verificado sem nome público;
- comentário privado ao responsável;
- contribuição estruturada agregada sem comentário público.

A Guivos pode manter identificação interna mínima para integridade, prevenção de duplicidade, contestação e moderação sem torná-la pública.

Responsável pelo objeto não recebe identidade protegida apenas por possuir poder de resposta ou contestação.

## 9. Reputação contextual

Reputação é leitura contextual de evidências e avaliações, não nota universal.

Uma apresentação pode reunir:

- quantidade de avaliações verificadas;
- período;
- distribuição por dimensão;
- respostas não aplicáveis ou insuficientes;
- comentários públicos;
- respostas oficiais;
- alterações materiais;
- metodologia e limitações;
- fontes externas claramente separadas.

Amostra insuficiente não significa reputação positiva, negativa ou inexistência de experiências.

## 10. Indicadores e comparabilidade

Percentuais, distribuições e comparações só podem ser apresentados quando houver contexto suficiente para interpretação.

Devem preservar, conforme aplicável:

- objeto;
- dimensão;
- denominador;
- período;
- versão;
- estado de verificação;
- base suficiente;
- limitações.

Quantidade de avaliações, popularidade, publicidade, plano contratado, receita, seguidores ou permanência na plataforma não constituem reputação ou qualidade por si sós.

Satisfação não comprova impacto.

## 11. Alterações materiais

Avaliações permanecem vinculadas ao contexto vivido.

Mudanças materiais em conteúdo, responsáveis, preço, regras, modalidade, local, requisitos, segurança, acessibilidade, dados, governança ou condições equivalentes devem permanecer distinguíveis.

Avaliações anteriores não são silenciosamente reescritas para representar condição posterior.

## 12. Resposta, contestação, denúncia, moderação e recurso

As competências são separadas.

### 12.1 Resposta oficial

Representante competente pode responder sem:

- editar avaliação;
- exigir alteração;
- expor identidade protegida;
- retaliar;
- criar contato privado obrigatório.

### 12.2 Contestação

Contestação exige fundamento específico e não equivale a remoção.

Discordância com crítica, impacto comercial ou avaliação desfavorável não são, isoladamente, fundamento suficiente.

### 12.3 Denúncia

Denúncia é procedimento próprio para risco, fraude, abuso, discriminação, assédio, segurança, ilegalidade ou uso indevido de dados.

Denúncia não é nota baixa e não comprova infração por si só.

### 12.4 Moderação

Medidas materiais pertencem a autoridade competente e devem ser proporcionais, fundamentadas e rastreáveis.

Responsável avaliado não é autoridade universal sobre a crítica dirigida a si.

### 12.5 Recurso

Decisão material recorrível precisa de instância de revisão compatível com sua gravidade e com conflitos de interesse aplicáveis.

## 13. Relações Organização↔Coletivo

Relações institucionais podem ser avaliadas somente quando a unidade da relação, execução, período, representação, evidências e competências estiverem suficientemente delimitados.

Negociação, contrato, valor financeiro ou vínculo institucional não equivalem a reputação.

Publicação ampla depende de autoridade especializada, especialmente por poder envolver:

- confidencialidade;
- dados pessoais;
- informação comercial sensível;
- múltiplas partes;
- coexecução;
- pessoas legitimamente afetadas.

`ORG-005` e `COL-008` não recebem, por analogia, autoridade de reputação pública UXA-057.

## 14. Autoridade de superfície

Este documento resolve a autoridade semântica do domínio, mas **não transforma uma superfície em autoridade canônica de R1**.

Em especial:

```text
PER-009
→ pode funcionar como ponto administrativo transversal quando expressamente integrado
→ não é autoridade canônica da avaliação
→ não recebe painel de avaliações por analogia
```

PER-103, PER-203, COL-002, ORG-001, COL-007 ou qualquer outra superfície somente recebem responsabilidades UXA-057 mediante extensão explícita do contrato correspondente.

Quando não existir superfície adequada, deve-se registrar a lacuna em vez de inventar rota ou ID.

## 15. Handoffs

Nenhum handoff nasce apenas desta autoridade.

Qualquer transição futura precisa comprovar:

- origem existente;
- destino existente;
- autoridade de ambos;
- identidade de objeto/edição/etapa;
- autoria ou mandato;
- proveniência;
- revalidação;
- proteção;
- retorno;
- falha e interrupção;
- idempotência.

## 16. Limites

Esta autoridade não:

- define wireframes;
- cria nota universal;
- cria ranking de Pessoas;
- define algoritmo de recomendação;
- define limiar estatístico final;
- define política jurídica operacional completa;
- cria superfície ou transição;
- escolhe cobertura inicial de lançamento;
- libera Design;
- libera Product Engineering.

## 17. Estado canônico

```text
UXA-057 DOMAIN AUTHORITY
→ GKR-UX-EVALUATION-REPUTATION-AUTHORITY-001
→ NORMATIVE / ACTIVE

PRIVATE REVIEW AUTHORITY
→ DOMAIN CONTRACT, NOT PER-009

PER-009
→ POSSIBLE ADMINISTRATIVE ENTRY ONLY
→ NO AUTHORITY BY ANALOGY

SURFACES / TRANSITIONS
→ REQUIRE EXPLICIT MATERIALIZATION

DESIGN
→ NOT RELEASED BY THIS DOCUMENT

PRODUCT ENGINEERING
→ NOT RELEASED
```
