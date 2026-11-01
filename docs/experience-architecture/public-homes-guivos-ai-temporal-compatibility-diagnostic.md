---
id: GKR-UX-HOMES-GAI-TEMPORAL-COMPATIBILITY-DIAG-001
title: Diagnóstico preliminar — perspectivas temporais Guivos AI nas sete Homes
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Diagnóstico preliminar — sete Homes e conceito de futuro

## Escopo e autoridade

Revisão documental preliminar dos sete Documentos Mestres públicos vigentes em `main` (exceto Intelligence), diante das perspectivas **Retrospectiva / Contextual / Prospectiva**. Estas são lentes complementares, não motores, funções prontas, etapas obrigatórias ou previsões deterministas. Diferenciar **Guivos AI (capacidade/arquitetura)** de **Guivos Intelligence (produto/superfície)**. Manter `COMPREENDER ≠ DECIDIR`, `POSSIBILIDADE ≠ GARANTIA` e `RESULTADO ESPERADO ≠ RESULTADO COMPROVADO`.

**Este diagnóstico não altera nenhum Documento Mestre, Source Lock, Manifesto ou interface publicada.** A prioridade abaixo é recomendação analítica baseada na leitura textual das versões, não aprovação de mudança.

## Matriz inicial

| Home | Versão lida em main | Diagnóstico | Intervenção documental sugerida |
| --- | --- | --- | --- |
| Pessoa | 1.0.8 | **Ajuste pontual necessário** | Tornar inteligível a distinção entre trajetória, momento e possíveis caminhos no discurso de jornada, mantendo autonomia e sem inferir destino inevitável. |
| Organizações e Coletivos | 1.0.9 | **Ajuste pontual necessário** | Explicar contribuição potencial da oferta em diferentes horizontes, sem fabricar match, causalidade ou promessa de resultado. Preservar diferenças entre Organização e Coletivo. |
| Mall | 1.1.4 | **Já compatível no princípio; refinamento opcional** | Só acrescentar perspectiva temporal onde esclarecer a relação entre oportunidade vigente e possibilidade futura; não atribuir predição ou oferta inexistente. |
| Travel | 1.1.6 | **Já compatível no princípio; refinamento opcional** | Separar inspiração por experiências de afirmações factuais sobre destinos, disponibilidade e resultados futuros. |
| Media | 1.0.3 | **Já compatível no princípio; refinamento opcional** | O território editorial Futuro já é contemplado; considerar guardrail de pluralidade e incerteza, sem obrigar tríade temporal na Home. |
| Ads | 1.0.3 | **Já compatível no princípio; refinamento opcional** | Não converter contexto/relevância em vigilância, previsão de comportamento ou promessa de eficácia publicitária. |
| Business | 1.1.10 | **Revisão conceitual focalizada recomendada** | Distinguir indicadores observados, leitura contextual e cenários ou hipóteses prospectivas. Evitar divulgar produto futuro como capacidade atual. Exige atenção especial a autoridades Business e condição normativa do mestre. |

## Critérios de classificação

- **Já compatível no princípio:** a narrativa existente aceita o conceito sem mudança estrutural; eventual ajuste não deve ser forçado.
- **Ajuste pontual necessário:** a comunicação melhora com uma explicitação breve, preservando movimentos e narrativa existentes.
- **Revisão conceitual focalizada:** risco de interpretação operacional/analítica relevante justifica estudo dos Source Locks e contratos do produto antes de propor texto.

## Observações concretas da leitura

- Pessoa contém contexto, possibilidades e futuro, sem estrutura explícita da tríade.
- Organizações e Coletivos trata extensamente contexto, possibilidades e estados futuros, sem as três lentes como conceito editorial.
- Mall, Travel, Media e Ads já possuem narrativas próprias e não necessitam reproduzir a Home Intelligence. Media já menciona `Futuro` como território editorial; Ads contém linguagem contextual.
- Business, embora discuta amplamente Intelligence e possibilidades, não diferencia explicitamente histórico, presente e projeções como três classes de evidência no Documento Mestre revisado. Seu Documento Mestre declara `normative: true`, o que demanda cuidado reforçado.

## Sequência proposta

1. Concluir a PR #720 da Home Intelligence mediante decisão independente de integração e checks do último head.
2. Revisar primeiro **Pessoa / Organizações e Coletivos / Business** com os respectivos contratos, Source Locks e mecanismos de conteúdo, identificando precisamente os movimentos que aceitam pequenas alterações.
3. Rever Mall / Travel / Media / Ads apenas para riscos materiais; não alterar por uniformização forçada.
4. Preparar propostas em PRs próprias, separadas da PR #720 e sem promover autoridade de produto.
5. Antes de qualquer merge, validar os controles de CI, a autoridade do manifest, e a autorização expressa; publicação visual requer verificação posterior separada.

## Restrições

Aprovação da alternativa A para GPA-006 significa **v2.0.2 como referência normativa da Home Intelligence**, `2.0.3` como versão física posterior. Não autoriza promoção normativa, merge automático, implantação, testes ou operação da Guivos AI. **Nenhuma Home deve sugerir predição garantida, capacidades não existentes ou decisões automáticas feitas pela plataforma.**

## Estado

`preliminary_read_complete / no_home_master_changed / decision_required_before_normative_changes`.
