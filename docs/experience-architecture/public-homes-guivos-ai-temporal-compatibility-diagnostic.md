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


## Revisão focalizada dos movimentos e contratos — Pessoa, O/C e Business

Esta seção foi elaborada por confronto direto dos Documentos Mestres de `main` e, para Business, também do Source Lock e do contrato de autoridades. **São propostas de pontos de inserção, sem alteração de autoridade ou copy congelada.**

| Home | Local específico | Compatibilidade e tratamento proposto | Restrições |
| --- | --- | --- | --- |
| Pessoa | **M04 — Desconexão; M05 — Guivos/Conexão** | Explicitar que compreender o momento atual depende de contexto, lacunas e relações, sem inferir diagnóstico da Pessoa. | Preservar a Guivos como facilitadora, não autora da trajetória. |
| Pessoa | **M06 — Da Possibilidade à Experiência** | Sugerir associação leve entre experiências já vividas, contexto atual e caminhos que a Pessoa pode explorar. | Não criar um ciclo obrigatório, nem prometer transformação. |
| Pessoa | **M09 — Autoridade; M10 — Autonomia e Confiança** | Distinguir evidência retrospectiva, interpretação contextual e possibilidade prospectiva; linguagem de incerteza apropriada. | Seção 28 já contém `INFERÊNCIA ≠ FATO`, `SINAL ≠ CERTEZA`, `TENDÊNCIA ≠ DESTINO`; não repetir tecnologia no Hero. |
| Organizações e Coletivos | **M03 — Da fragmentação à continuidade; M04 — Papel da Guivos** | Nomear continuidade como possibilidade situada no tempo e sujeita a evidência, não cadeia causal. | Não afirmar resultados de uma ação sem evidência. |
| Organizações e Coletivos | **M06 — Complementaridade; M08 — Mapa de Pessoas** | Distinção entre capacidade já existente, necessidade contextual e possíveis contribuições futuras, sem automatizar correspondências. | Não fabricar match, perfis de Pessoas ou demanda verificada. |
| Organizações e Coletivos | **M10 — Autoridade, evidência e proteção; M11 — Ecossistema** | Guardrail contra interpretar cenários ou horizontes futuros como oferta já entregue; explicar papel transversal de Intelligence quando útil. | Participantes distintos, igual legitimidade; Intelligence não é Guivos AI nem autor de decisões. |
| Business | **M07 — Guivos Intelligence (seções 14–16)** | Considerar distinção editorial entre indicadores observados ao longo do tempo, interpretação de contexto e cenários condicionais, sem alterar a promessa pública congelada. | Mudança no papel de Intelligence exige **nova decisão explícita** segundo Source Lock, seção 30. |
| Business | **Source Lock seções 14–15; Authority Contracts, Contrato 7** | Avaliar compatibilidade de cenários prospectivos apenas como hipóteses ou futuro condicionado, nunca recurso comprovadamente disponível. | Sem Journey individual, sem causalidade não demonstrada, sem acesso automático aos KPIs internos empresariais. |

### Referências para os pontos de inserção

- Pessoa: `public-home-master-document.md`, seção 13 (11 movimentos), seção 15 (M06), seção 28 (Tecnologia e Intelligence).
- Organizações e Coletivos: `public-home-organizations-collectives-master-document.md`, quadro dos 12 movimentos, especialmente M03, M04, M06, M08, M10 e M11.
- Business: `public-home-business-master-document.md`, seção 14 (M07); `public-home-business-source-lock.md`, seções 14, 15 e 30; `public-home-business-authority-contracts.md`, Contrato 7.

### Texto candidato puramente ilustrativo — não aprovado para publicação

**Pessoa:** “O que você já viveu, o momento em que está e os caminhos que ainda pode descobrir ajudam a ampliar sua compreensão — sem determinar suas escolhas.”

**Organizações e Coletivos:** “O que já existe pode ganhar novos contextos e abrir possibilidades futuras quando há contribuições legítimas, escolhas e condições reais.”

**Business (hipótese sujeita a decisão específica):** “Compreenda movimentos e tendências observados na Guivos e explore possibilidades para suas iniciativas, distinguindo informações conhecidas de cenários ainda não comprovados.”

Nenhum desses textos substitui slogans, Hero ou Supporting Copy congelados; Business exige adjudicação antes de qualquer inserção normativa.

### Próximo gate

Produzir proposta textual limitada para **Pessoa e Organizações/Coletivos** após revisão dos contratos de cada Home. Para **Business**, primeiro obter decisão específica sobre eventual alteração no papel narrativo de Intelligence, conforme seção 30 do Source Lock. As sete Homes não devem ganhar a tríade como ornamentação nem como recurso operacional declarado.
