---
id: GKR-UX-HOMES-PERSON-OC-TEMPORAL-GATES-001
title: Gates de decisão editorial e de Source Lock — Pessoa e Organizações e Coletivos
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Decisões ainda necessárias — Pessoa e Organizações e Coletivos

## Estado verificado

A branch candidata contém:
- Home Pessoa 1.0.9: adendos **não vigentes** M06, M09, M10.
- Home O/C 1.0.10: adendos **não vigentes** M03, M06, M10.
- Leia Primeiro Pessoa 1.0.6 e O/C 1.0.6: referências candidatas alinhadas.
- Manifesto 7.0.57 candidato: referências alinhadas aos dois Mestres, mas Source Lock generativo preservado em 2.3.17.

A direção autorizou **preparação documental**, não promoção normativa, integração ou publicação.

## Gate E — decisão sobre seis adendos

**E1 — Aprovar a redação para futura integração documental (recomendação editorial condicionada):** autorizar a transformação dos seis adendos candidatos em texto editorial vigente dentro de seus movimentos, com remoção do rótulo *não vigente*, mantendo os limites de evidência, autonomia, privacidade, não previsão e não causalidade. Não autoriza merge nem publicação.

**E2 — Solicitar ajustes:** não promover antes de reescrita dirigida.

**E3 — Não incorporar:** conservar como diagnóstico histórico.

## Gate S — Source Lock generativo compartilhado

O arquivo `GKR-UX-HOMES-GENINPUT-001` em `main` declara **v2.3.18**, `active`, `normative: true`, mas o Manifesto 7.0.56 (e o candidato 7.0.57) nomeia **v2.3.17** como referência de consumo. Além disso, o Source Lock 2.3.18 ainda aponta internamente para Pessoa 1.0.7 e O/C 1.0.7. A divergência é **documental real**. O frontmatter por si só não decide a autoridade de consumo diante de um Manifesto divergente.

**S1 — Autorizar apenas correção coordenada de referências (recomendação, condicionada a E1):** após revisão de impacto, preparar uma versão candidata posterior do Source Lock que referencie as versões aprovadas dos Mestres e propor atualização expressa da versão referenciada pelo Manifesto; preservar contratos e limites normativos existentes. A mudança de versão consumida exige decisão específica da direção.

**S2 — Preservar o congelamento atual:** não modificar Source Lock ou referência do Manifesto até uma auditoria específica de promoção 2.3.17/2.3.18.

**S3 — Revisar a autoridade e a história de versionamento antes de decidir:** aprofundar trilha documental e gates prévios, sem mudança de fontes.

## Pré-condições para PR

1. Deliberações E e S específicas, não inferidas de um simples “de acordo”.
2. Reconferir versão dos oito Mestres e referências atuais em main.
3. Executar checks mecânico e semântico no SHA final.
4. Solicitar autorização de merge por PR e commit, independente da decisão editorial.
5. Publicação e operações exigem autorizações próprias.

**Estado:** `decisions_E_and_S_pending / candidate_branch_only / no_merge_no_deploy`.
