---
id: RP-002-ECSR-001
title: Registro de Evidências e Estado das Claims
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-26
normative: false
parent: RP-002
---

# RP-002-ECSR-001 — Registro de Evidências e Estado das Claims

## 1. Finalidade

Este registro existe para impedir que resultados de naturezas diferentes sejam confundidos durante a evolução do `RP-002`.

A regra é:

```text
CANON EXISTENTE
≠ EVIDÊNCIA EXTERNA
≠ CONCLUSÃO DE RESEARCH
≠ SIMULAÇÃO
≠ HIPÓTESE
≠ VALIDAÇÃO GUIVOS REAL
```

## 2. Classes utilizadas

### CANONICAL EXISTING

Já possui autoridade normativa em documento vigente do GKR.

### EXTERNAL EVIDENCE

Sustentado por fontes reais externas, com limites de autoridade e temporalidade.

### RESEARCH CONVERGED

Conclusão conceitual que sobreviveu à investigação e aos contraexemplos, mas ainda não foi promovida pela arquitetura proprietária.

### SIMULATION SUPPORTED

Hipótese que apresentou coerência em simulação operacional, sem Pessoa real.

### FIELD HYPOTHESIS

Precisa ser testada empiricamente.

### NOT VALIDATED

Não existe evidência suficiente para claim positiva.

### REJECTED / REFORMULATED

Formulação descartada ou materialmente modificada pela investigação.

## 3. Register principal

| Claim | Estado | Evidência / fundamento | Limite |
|---|---|---|---|
| Oportunidade é meio, não Próximo Passo | CANONICAL EXISTING | PAS-001 | não redefine contratos |
| Experiência ≠ inscrição/compra/presença | CANONICAL EXISTING | PAS-001 Experiências | preserva autoridade canônica |
| Organização ≠ cliente Business | CANONICAL EXISTING | UXA-014 / GPA-004 | relação comercial separada |
| Coletivo não deve ser reduzido a mídia/popularidade | CANONICAL EXISTING | UXA-014 | não define métricas finais |
| Supply real existe nos nove Domínios | EXTERNAL EVIDENCE — STRONG | corpus internacional e local | não implica supply contextual para toda Pessoa |
| Não há evidência de escassez estrutural global | RESEARCH CONVERGED | densidade observada nos nove Domínios | não é TAM estatístico |
| Abundância global e escassez contextual coexistem | RESEARCH CONVERGED | corpus + gates + contraexemplos | depende de Source Coverage |
| Possibilidade é distinta de Oportunidade | RESEARCH CONVERGED | análise semântica e casos | ainda não é entidade canônica |
| Possibility Pattern pode organizar conhecimento persistente | RESEARCH CONVERGED / FIELD HYPOTHESIS | rounds semânticos + simulação | persistência e lifecycle não canonizados |
| Possibilidade Contextual deve ser temporária por padrão | RESEARCH CONVERGED | autoridade humana + minimização | estados ainda experimentais |
| Possibilidade só deve existir quando agrega valor | RESEARCH CONVERGED | teste de casos diretos e complexos | UX ainda a validar |
| Relevância pertence à relação Pessoa↔Oportunidade | RESEARCH CONVERGED | múltiplos contraexemplos | decisão canônica futura necessária |
| Fit e evidência devem permanecer separados | RESEARCH CONVERGED | casos Generation, Kiva, programas novos | modelagem final aberta |
| Gate crítico não pode ser compensado por score | RESEARCH CONVERGED / SIMULATION SUPPORTED | Generation × pessoa empregada | precisa validação operacional em escala |
| Supply habilitador é funcionalmente relevante | RESEARCH CONVERGED | childcare, transporte, internet, docs etc. | taxonomia final não definida |
| Discovery não deve depender de parceria | RESEARCH CONVERGED | fontes públicas/APIs/directories | requisitos legais/operacionais por fonte |
| Discovery ≠ Admission ≠ Partnership | RESEARCH CONVERGED | arquitetura de source/admission | integração canônica futura |
| Provider Claim não concede autoridade sobre fit | RESEARCH CONVERGED | source-authority model | claim lifecycle não canônico |
| Freshness deve ser proporcional por campo | RESEARCH CONVERGED | volatilidade de vagas, preço, prazo | regras técnicas futuras |
| UNKNOWN deve ser preservado | RESEARCH CONVERGED | safe failure | UX de incerteza ainda a validar |
| Source Coverage é necessária para interpretar gaps | RESEARCH CONVERGED | ausência de resultado ≠ ausência de supply | métrica não definida |
| Possibility Gap pode orientar criação de novo supply | FIELD HYPOTHESIS | demand + observed supply | precisa dados reais |
| Demand Intelligence possui valor B2B potencial | FIELD HYPOTHESIS | padrões de mercado + arquitetura Guivos | willingness to pay não provada |
| Contribution Intelligence pode ser ativo estratégico | FIELD HYPOTHESIS | grafo Contexto→Experiência→Contribuição | moat não provado |
| Evidence Guivos não deve ser comprável | RESEARCH CONVERGED | princípios de autoridade/economia | implementação futura |
| Status comercial não deve aumentar fit | RESEARCH CONVERGED | GEM + conflitos analisados | decisão arquitetural futura |
| Presença funcional básica não deveria depender de pagamento | RESEARCH CONVERGED | integridade da Journey | modelo operacional futuro |
| Comissão pode existir em transações legítimas | RESEARCH CONVERGED WITH BOUNDARY | GEM + precedentes de mercado | preço e aplicação não aprovados |
| Comissão não deve dirigir discovery | RESEARCH CONVERGED | conflito free-high-fit vs paid-lower-fit | requer governança de produto |
| Ads deve permanecer separado da relevância funcional | RESEARCH CONVERGED / CANON-ALIGNED | Ads + GEM + Opportunity Boost boundaries | detalhamento por produto |
| Organizações podem pagar por gestão, integração, operação e Intelligence | FIELD HYPOTHESIS | precedentes B2B + valor analisado | portfólio não aprovado |
| Coletivos podem preencher gaps de supply | EXTERNAL EVIDENCE / RESEARCH CONVERGED | casos locais e comunitários | escala variável |
| Sponsor não deve comprar governança do Coletivo | RESEARCH CONVERGED | autonomia + conflitos | contratos futuros |
| Efeito de rede de supply pode existir | FIELD HYPOTHESIS | modelo conceitual | não observado em escala Guivos |
| Efeito de rede de experiência/evidência pode existir | FIELD HYPOTHESIS | modelo conceitual | não observado em escala Guivos |
| IA/busca/memória isoladas não são moat suficiente | EXTERNAL EVIDENCE / RESEARCH CONVERGED | capacidades contemporâneas de grandes plataformas | cenário competitivo muda |
| Orquestração longitudinal pode diferenciar Guivos | FIELD HYPOTHESIS | análise competitiva | longitudinal lift não provado |
| Guivos pode reduzir espaço decisório | FIELD HYPOTHESIS | modelo de gates/fit | comportamento real não medido |
| Pessoa reconhecerá valor nas Possibilidades | NOT VALIDATED | nenhum piloto real | teste necessário |
| Guivos compreenderá Momento com precisão suficiente | NOT VALIDATED | nenhum piloto real | teste necessário |
| Guivos superará Google/IA em contextos complexos | NOT VALIDATED | apenas benchmark conceitual | benchmark cego necessário |
| Pessoa agirá a partir da entrega Guivos | NOT VALIDATED | nenhum comportamento real | piloto necessário |
| Pessoa retornará pós-experiência | NOT VALIDATED | nenhum comportamento real | piloto necessário |
| Evidence Guivos melhorará matching | NOT VALIDATED | hipótese longitudinal | longitudinal A/B necessário |
| Pessoa pagará | NOT VALIDATED | sem transação real | teste econômico posterior |
| Organização pagará | NOT VALIDATED | valor B2B plausível | piloto comercial necessário |
| Network effects reais ocorrerão | NOT VALIDATED | nenhum uso em escala | observação futura |
| Quatro modos Direct/Exploratory/Decisional/Longitudinal são arquitetura oficial | NOT VALIDATED | apenas simulação | não canonizar antes do piloto |
| Ranking universal de oportunidades é adequado | REJECTED | falhou na simulação | seleção deve depender do Episódio |
| Follow-up somente cronológico é suficiente | REJECTED | oportunidades possuem durações distintas | combinar tempo + estado da experiência |
| Uma oportunidade deve ter um único papel contextual | REJECTED | mentoring+course podem ser sequenciais/complementares | relação contextual necessária |
| “Resultado positivo” deve ser conversão final | REJECTED | descarte legítimo pode reduzir incerteza | contribuição é mais ampla |
| Mais tempo de tela implica mais valor | REJECTED | propósito orientado à experiência real | métricas futuras devem refletir Journey |

## 4. Claims de supply — força e cuidado

### 4.1 Forte

- existência de supply global em todos os nove Domínios;
- diversidade de agents;
- existência de supply comercial e não comercial;
- existência de Direct e Enabling Supply;
- supply pode ser gratuito e altamente relevante;
- Coletivos podem operar supply real.

### 4.2 Moderada

- densidade relativa por Domínio;
- cobertura territorial específica;
- prevalência de barreiras;
- qualidade média de tipos de provider.

Essas dimensões exigem amostragem mais sistemática para claims quantitativas.

## 5. Claims de evidência externa

O programa encontrou diferentes forças de evidência:

### Provider-reported

Exemplos:

- número de membros;
- sessões;
- negócios apoiados;
- empregos relatados;
- participantes.

Uso permitido:

> evidência de escala/adoption reportada pelo provider.

Uso inadequado:

> prova causal independente de transformação.

### Independent observational / review

Pode sustentar associações e padrões com maior independência, preservando limitações.

### Causal evidence

Quando existir, deve ser explicitamente diferenciada de survey, testimonial ou correlação.

O `RP-002` não presume causalidade pela reputação do provider.

## 6. Evidência Guivos futura

O piloto deverá separar:

```text
EXPERIENCE DECLARED
CONTRIBUTION DECLARED
OBSERVABLE CONSEQUENCE
RELATED ARTIFACT
EXTERNAL CONFIRMATION
```

Nenhum desses elementos isoladamente deve ser convertido automaticamente em score de evolução.

## 7. Claims econômicas

### Coerentes com o Economic Model

- revenue por serviço;
- revenue B2B;
- integration/infrastructure;
- transactions transparentes;
- Ads identificados;
- sponsorship transparente;
- licensing futuro governado;
- Intelligence agregada potencial.

### Não aprovadas

- preços;
- comissão padrão;
- planos específicos novos;
- produto autônomo de Contribution Intelligence;
- venda de benchmark de contribuição;
- arquitetura final de payer por fluxo.

## 8. Proibições sustentadas pela investigação

O programa trata como incompatíveis:

- venda de Journey individual;
- venda de vulnerabilidade;
- venda de score humano;
- pay-to-rank funcional;
- Evidence Guivos patrocinável;
- ocultação de alternativa melhor por dinheiro;
- inferência religiosa para targeting;
- falsa causalidade;
- sponsorship coercivo de Coletivos;
- opportunity discovery subordinado exclusivamente a partner inventory.

## 9. Status do PMF

```text
SUPPLY FEASIBILITY
→ strongly supported

CONCEPTUAL COHERENCE
→ strong

PILOT METHODOLOGY
→ ready

PERSON PMF
→ not validated

ORGANIZATION PMF
→ not validated

COLLECTIVE PMF
→ not validated

NETWORK FIT
→ not validated

UNIT ECONOMICS
→ not validated
```

## 10. Critério para alterar uma claim

Uma claim deve mudar de estado somente quando houver nova evidência proporcional.

Exemplos:

```text
FIELD HYPOTHESIS
→ SIMULATION SUPPORTED
```

não é equivalente a:

```text
FIELD HYPOTHESIS
→ FIELD VALIDATED
```

Da mesma forma:

```text
10 participantes gostaram
```

não autoriza:

```text
PMF VALIDATED
```

## 11. Contraevidência é parte do ativo

O programa deve preservar:

- casos em que Google foi melhor;
- oportunidades perdidas pela Guivos;
- falsos positivos;
- falsos negativos;
- contexto excessivo;
- Possibilidades consideradas óbvias ou artificiais;
- participantes que não agiram;
- experiências sem contribuição;
- experiências negativas;
- ausência de longitudinal lift;
- unwillingness to pay.

Uma evidência contrária não é ruído a ser removido.

É informação que protege a arquitetura contra autoengano.

## 12. Regra de futura promoção canônica

Para uma conclusão deste `RP-002` ser promovida à arquitetura oficial, recomenda-se preservar pelo menos:

1. problema arquitetural explícito;
2. relação com autoridade existente;
3. evidência externa quando aplicável;
4. casos reais;
5. contraexemplos;
6. limites;
7. impacto em outras arquiteturas;
8. decisão do owner apropriado;
9. documentação de mudança;
10. sincronização com contratos dependentes.

## 13. Próxima atualização deste registro

Após os primeiros dry runs reais, este documento deverá receber uma seção separada de **Field Evidence**, sem reescrever retrospectivamente o estado pré-piloto.

A rastreabilidade temporal precisa mostrar claramente:

> **o que acreditávamos antes de colocar a hipótese diante de Pessoas reais e o que mudou depois.**
