---
id: GKR-UX-EVALUATION-REPUTATION-ADJUDICATION-PROGRESS-001
title: "Avaliação e Reputação — Estado do exame e preparação de adjudicação"
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-01
related:
  - UXA-057
  - GKR-UX-EVALUATION-REPUTATION-READ-FIRST-001
  - GKR-UX-EVALUATION-REPUTATION-D1-D4-EXAMINATION-001
  - GKR-UX-EVALUATION-REPUTATION-HANDOFF-MATRIX-001
normative: false
---

# Avaliação e Reputação — Estado do exame e preparação de adjudicação

Este documento registra o avanço conceitual posterior à consolidação D1–D5. É **não normativo**: organiza decisões candidatas, invariantes, bloqueios e dependências para adjudicação humana. Não seleciona alternativas, não cria telas, não estende Masters, não cria GKR-TRN e não libera Design ou Engenharia.

## 1. Estado geral

O exame conceitual D1–D5 foi concluído sem adjudicação. Em seguida, o trabalho foi reorganizado em nove blocos candidatos de decisão: A1 elegibilidade comum; A2 regras por categoria; A3 registro protegido e envio; A4 continuidade privada; A5 objeto público e identidade; A6 consentimento e destinos; A7 governança; A8 avaliação institucional Organização–Coletivo; A9 integração e aceitação individual dos handoffs.

Até esta atualização:

| Bloco | Escopo | Estado |
| --- | --- | --- |
| A1 | Elegibilidade comum | 6/6 decisões preparadas; 0 adjudicadas |
| A2 | Seis categorias de experiência | 6/6 preparadas; 0 adjudicadas |
| A3 | Registro protegido e envio | 5/5 preparadas; 0 adjudicadas |
| A4 | Continuidade privada permanente | 7/7 preparadas; 0 adjudicadas |
| A5 | Objeto público e identidade | 5/5 preparadas; 0 adjudicadas |
| A6 | Consentimento, destinos e execução pública | 6/6 preparadas; 0 adjudicadas |
| A7 | Resposta, contestação, denúncia, moderação e recurso | 5/5 examinadas e reconciliadas; 0 adjudicadas |
| A8 | Avaliação institucional Organização–Coletivo | 5/7 decisões examinadas; 0 adjudicadas |
| A9 | Integração e aceitação dos handoffs | Não iniciado |

A1–A7 totalizam **40 decisões candidatas examinadas/preparadas e 0 adjudicadas**. A8 está em curso. Nenhum dos 13 handoffs está autorizado.

## 2. A1 — elegibilidade comum

O exame preparou seis decisões: unidade avaliável delimitada; participação efetiva; legitimidade de quem avalia; evidência e verificação; temporalidade e duplicidade; estados de elegibilidade.

Invariantes candidatos incluem: inscrição ou vínculo não equivalem a experiência efetiva; participação verificada não comprova a verdade de toda narrativa; recorrências precisam de unidade própria; correções não devem gerar duplicidade; resultado de envio desconhecido deve ser reconciliado antes de nova tentativa.

## 3. A2 — regras específicas por categoria

Foram preparadas seis categorias: atividades de Coletivos; cursos/programas; oportunidades; participação continuada; execução institucional Organização–Coletivo; experiências externas/autodeclaradas.

Cada categoria deverá especializar a unidade, a participação suficiente, a evidência, a temporalidade e as exceções sem romper os invariantes comuns de A1. A execução institucional não nasce do contrato isoladamente. Experiência externa privada não se converte automaticamente em avaliação pública de terceiro.

## 4. A3 — registro protegido e envio

Cinco decisões foram preparadas: entrada contextual; formulário protegido e critérios versionados; rascunhos e revisão pré-envio; revalidação e envio idempotente; confirmação privada.

O envio privado não equivale a consentimento de publicação. Critérios devem distinguir não aplicável, omitido e informação insuficiente. Operação com resultado desconhecido exige reconciliação antes de retry. PER-108 e PER-203 continuam origens candidatas dependentes de auditoria e extensão expressa.

## 5. A4 — continuidade privada

Sete decisões foram preparadas: autoridade permanente; escopo; identidades, papéis e permissões; independência do contexto de origem e histórico; integração e sincronização; recuperação; proteção e retenção.

**H6 continua com origem indefinida.** PER-009 permanece hipótese e não autoridade aprovada. A continuidade deverá preservar unidade, avaliação, versões, operações, estados de publicação e casos de governança com ACL proporcional, sem transformar retenção justificada em retenção indefinida.

## 6. A5 — objeto público e identidade

Cinco decisões foram preparadas: objeto público individual; coleções/contexto; indicadores agregados e comparabilidade; modalidades de identidade pública; identificação indireta e atribuição incorreta.

Não há autorização para nota universal, ranking ou score institucional. Critérios com escala semelhante não são automaticamente comparáveis. Evidência privada não se torna pública por estar ligada a avaliação publicável. Risco de reidentificação deve considerar o conjunto de contexto, narrativa, atributos e múltiplos destinos.

## 7. A6 — consentimento, destinos e execução pública

Seis decisões foram preparadas: consentimento específico; escopo, versão e duração; destinos e responsabilidades; verificação e execução; mudanças e sincronização; retirada e continuidade privada.

Consentimento deve ser afirmativo, específico, verificável e separado do envio privado. Conteúdo, identidade, contexto, evidências, destinos e duração são dimensões distintas. Mudanças materiais não devem ampliar silenciosamente o consentimento. Retirada de consentimento, despublicação e eliminação privada são operações diferentes.

**H3 permanece bloqueado** até adjudicação de objeto público, identidade, consentimento, destinos, proteção, sincronização e auditoria dos Masters pertinentes.

## 8. A7 — governança

A7 foi decomposto e examinado em cinco decisões:

- **A7.1 / H8 — resposta institucional oficial:** manifestação da entidade, separada da avaliação original e sem poder de decisão sobre ela.
- **A7.2 / H9 — contestação formal:** questionamento fundamentado; recebimento ou admissibilidade não equivalem a procedência.
- **A7.3 / H10 — denúncia de privacidade, abuso ou fraude:** relato não equivale a prova; risco e mérito permanecem distintos.
- **A7.4 / H11 — moderação independente:** competência, conflito de interesse, instrução, decisão fundamentada e execução verificável.
- **A7.5 / H12 — recurso independente:** revisão de decisão recorrível por autoridade suficientemente independente.

A reconciliação preservou três níveis candidatos de informação — pública, procedimental e protegida — e a separação entre manifestação, caso, decisão, execução e recurso. Contestação ou denúncia não causam retirada automática. Recurso não causa suspensão, reversão ou republicação automática. Republicação continua dependente de consentimento público atualmente válido e das verificações aplicáveis.

**COL-007 não é painel universal de moderação.** Nenhuma autoridade de governança foi adjudicada.

## 9. A8 — contrato especializado de avaliação institucional

A8 foi decomposto em sete decisões. Cinco foram examinadas nesta atualização.

### A8.1 — unidade institucional avaliável

Foram examinadas entrega individual, fase, ciclo/período e composição controlada. A unidade deverá possuir identidade e limites estáveis, atribuição correta e prevenção de sobreposição. Contrato ou parceria não é a unidade avaliável por si só.

### A8.2 — execução efetiva e elegibilidade

Foram examinadas comprovação bilateral, evidência documental, fonte independente e verificação proporcional por categoria. Entrega, recebimento e aceite contratual permanecem conceitos distintos. Cancelamento antes do início não comprova experiência executada; execução parcial poderá exigir objeto próprio. Divergência não equivale automaticamente a fraude.

### A8.3 — entidade autora e representação

A entidade é a autora institucional; a Pessoa autenticada atua como representante operador. Mandato geral, específico para avaliações, por experiência ou combinado permanecem alternativas. Administração de perfil não concede automaticamente competência para avaliar. Revogação impede novos atos no escopo afetado, sem apagar autoria institucional histórica válida.

### A8.4 — critérios e evidências institucionais

O exame separou comprovação de execução, percepção institucional e alegação factual verificável. Critérios comuns, específicos, núcleo comum e modalidade permanecem alternativas. Evidências precisam de proveniência, pertinência, finalidade, proteção e versão. Informação comercial, contratual, pessoal ou operacional protegida não é publicável automaticamente.

### A8.5 — conflitos e reciprocidade

O exame distinguiu relação institucional, interesse, conflito relevante, coerção, retaliação, manipulação e alegação de fraude. Avaliações recíprocas, se futuramente admitidas, deverão ser independentes e não condicionadas uma à outra. Representação cruzada, dependência econômica, incentivos, entidades relacionadas e uso retaliatório da governança exigem regras próprias. Conflito do representante e conflito da entidade não são equivalentes.

### A8.6 e A8.7 — pendentes

Permanecem a examinar publicação e governança da avaliação institucional e, depois, integração e critérios de liberação de H13.

**H13 permanece bloqueado** até adjudicação expressa de A2.5/D1.5, conclusão do contrato especializado A8, origem e destino comprovados, mandato, proteção, governança, execução verificável e validação individual do handoff.

## 10. Invariantes transversais candidatos

1. Origem e destino precisam existir e possuir autoridade comprovada antes de qualquer handoff.
2. Unidade, categoria, versão, ator e mandato devem ser identificáveis.
3. Participação ou execução precisa ser verificada dentro do escopo pertinente.
4. Evidência de elegibilidade não é automaticamente evidência pública.
5. Registro privado, consentimento, publicação, governança e execução técnica possuem estados próprios.
6. Envio privado não significa publicação.
7. Consentimento não significa execução confirmada.
8. Decisão de governança não significa execução confirmada.
9. Resultado operacional desconhecido deve ser reconciliado antes de repetição.
10. Contestação e denúncia não produzem retirada automática.
11. Recurso não produz suspensão ou republicação automática.
12. Identidade privada e identidade pública são responsabilidades diferentes.
13. Correções e mudanças de contexto não devem reatribuir silenciosamente histórico.
14. Autoridades, conflitos de interesse e mandatos precisam ser verificáveis.
15. Nenhuma hipótese documental cria, por analogia, uma tela, rota, Master, GKR-TRN ou autoridade operacional.

## 11. Bloqueios e limites atuais

- **H3 — bloqueado:** publicação pública ainda depende das adjudicações A5/A6, auditoria dos Masters e validação.
- **H6 — origem indefinida:** continuidade privada permanente não possui superfície de origem aprovada.
- **H13 — bloqueado:** contrato especializado institucional A8 ainda está em exame.
- **H1, H2, H4, H5, H7–H12:** responsabilidades examinadas, mas não autorizadas.
- **0/13 handoffs autorizados.**
- **0 decisões A1–A8 adjudicadas.**
- Nenhuma extensão de Master, Surface Registry ou Transition Registry foi autorizada.

## 12. Próxima etapa sequencial

O exame deve retomar em **D18.7 — A8.6: Publicação e governança da avaliação institucional**, seguido de A8.7 e da reconciliação/preparação de adjudicação de A8. Somente depois deverá avançar para A9.

**Estado: DRAFT / NON-NORMATIVE / ADJUDICATION PREPARATION IN PROGRESS / A8 5 OF 7 EXAMINED / H3 AND H13 BLOCKED / H6 ORIGIN UNDEFINED / 0 OF 13 HANDOFFS AUTHORIZED / NO DESIGN OR ENGINEERING RELEASE.**
