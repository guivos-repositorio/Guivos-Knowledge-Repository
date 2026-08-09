---
title: Guivos Market Validation System
status: active
version: 1.5.0
owner: Guivos
last_updated: 2026-08-08
---

# Guivos Market Validation System

Este domínio organiza a validação de mercado da Guivos antes do lançamento e durante a evolução dos produtos.

## Objetivo

Transformar hipóteses internas em perguntas testáveis, coletar evidências de mercado e orientar decisões de produto com critérios explícitos.

## Princípios centrais

> A pesquisa não existe para provar que a Guivos é uma boa ideia. Ela existe para descobrir onde a proposta é forte, onde é fraca e o que precisa ser ajustado.

> A Guivos será construída com base em evidências e na participação das pessoas.

> Uma pergunta somente integra uma rodada quando a pessoa possui informação suficiente para avaliá-la de forma consciente.

> A validação não pressupõe que a pessoa já possua objetivo, plano ou próximo passo definido.

> O questionário público deve coletar o necessário com o menor esforço possível para quem participa.

## Documentos

- [VAL-001 — Framework de Validação de Mercado](VAL-001-framework-de-validacao-de-mercado.md) — versão 1.3.1;
- [VAL-002 — Pesquisa Oficial B2C](VAL-002-pesquisa-oficial-da-guivos.md) — versão 2.1.0, título público `Construindo a Guivos`;
- [VAL-002-A1 — Mapeamento da Pesquisa B2C para os Domínios de Evolução](VAL-002-A1-mapeamento-dominios-evolucao.md) — versão 1.0.0;
- [VAL-003 — Guia do Entrevistador](VAL-003-guia-do-entrevistador.md) — versão 1.2.1;
- [VAL-004 — Modelo de Consolidação e Análise](VAL-004-modelo-de-consolidacao-e-analise.md) — versão 1.3.1;
- [VAL-005 — Plano de Amostragem](VAL-005-plano-de-amostragem.md) — versão 1.2.1;
- [VAL-006 — Dashboard de Indicadores](VAL-006-dashboard-de-indicadores.md) — versão 1.3.1;
- [VAL-007 — Critérios de Decisão](VAL-007-criterios-de-decisao.md) — versão 1.3.1;
- [VAL-008 — Sinais Comportamentais](VAL-008-sinais-comportamentais.md) — versão 1.1.1;
- [VAL-009 — Estado de Execução e Gates de Evidência](VAL-009-status-de-execucao-e-gates-de-evidencia.md) — versão 1.0.0;
- [VAL-010 — Contrato de Intake, Evidência e Registro de Rodadas](VAL-010-contrato-de-intake-e-registro-de-rodadas.md) — versão 1.0.0.

## Sequência oficial

```mermaid
flowchart LR
    A["Hipótese"] --> B["Pesquisa curta"] --> C["Entrevistas"] --> D["Resultados"] --> E["Dashboard"] --> F["Decisão"] --> G["Ajustes"] --> H["Nova validação"]
```

A partir de VAL-009/010, a execução também precisa respeitar:

```text
método definido
→ instrumento identificado
→ aplicação comprovada
→ pré-teste comprovado
→ base recebida
→ base válida
→ qualidade avaliada
→ métricas reproduzíveis
→ decisão registrada
```

Nenhuma seta pode ser preenchida apenas por intenção, divulgação ou percepção geral.

## Estado metodológico

- instrumento público documental em versão `2.1.0`;
- duração estimada de 3 a 5 minutos;
- 19 perguntas;
- uma pergunta aberta obrigatória e uma opcional;
- linguagem direta ao participante;
- alternativas em primeira pessoa quando aplicável;
- no máximo duas escolhas em perguntas de seleção múltipla;
- apresentação oficial curta, com exemplos de saúde, carreira e espiritualidade;
- descoberta tardia e busca sem opção adequada medidas separadamente;
- IFO composto por `Q8` e `Q9`;
- compreensão medida pela resposta aberta `Q11`;
- relevância medida por `Q12`;
- contribuição medida por `Q15`;
- intenção medida por `Q16`;
- interesse em primeira experiência medido por `Q17`;
- barreiras medidas por `Q18`;
- coleta geográfica por estado ou Distrito Federal;
- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas.

Esses itens constituem **autoridade metodológica** e não comprovam que a aplicação, o pré-teste, a coleta ou qualquer resultado já tenham ocorrido.

## Rastreabilidade com os Domínios de Evolução do Journey

A pergunta 4 do `VAL-002` utiliza nove áreas da vida e uma alternativa combinada de incerteza/outra área.

Essas áreas contribuíram para o baseline arquitetural governado no `PAS-001-DOMAIN-MODEL-001`, sem alterar o questionário 2.1.0.

O `VAL-002-A1` registra o mapeamento explícito:

```text
4.1 → JED-001 Saúde e Bem-estar
4.2 → JED-002 Trabalho, Carreira e Estudos
4.3 → JED-003 Vida Financeira
4.4 → JED-004 Empreendedorismo e Projetos
4.5 → JED-005 Relacionamentos e Vida Social
4.6 → JED-006 Espiritualidade, Propósito e Valores
4.7 → JED-007 Viagens, Lazer, Cultura e Novas Experiências
4.8 → JED-008 Causas, Voluntariado e Contribuição
4.9 → JED-009 Organização e Equilíbrio da Vida
4.10 → Ainda estou descobrindo | other_unmapped
```

A escolha única na pesquisa serve ao método de pesquisa e **não restringe o Journey real a um único domínio**.

Também permanecem distintas:

```text
alternativa da pesquisa ≠ domínio confirmado da jornada
frequência de resposta ≠ eficácia da Guivos
resultado B2C ≠ evidência sobre Coletivos ou Organizações
```

## Decisões editoriais da versão 2.1.0

- perguntas `8` e `9` foram encurtadas;
- apresentação oficial foi condensada;
- perguntas passaram a conversar diretamente com “você”;
- alternativas redundantes foram consolidadas;
- antigas `Q14` e `Q15` foram unificadas;
- o instrumento foi reduzido de 20 para 19 perguntas;
- preço permanece fora da pesquisa conceitual;
- carga cognitiva passa a ser observada no pré-teste e no dashboard.

## Escopo inicial

A primeira aplicação valida a proposta B2C da Guivos, com foco em:

- momento atual e mudança desejada;
- descoberta tardia de oportunidades;
- busca sem opção adequada;
- esforço para encontrar algo relevante;
- compreensão da proposta;
- relevância contextual;
- situação de primeiro uso;
- utilidade esperada;
- contribuição percebida;
- intenção de experimentar;
- interesse em participar de primeira experiência;
- barreiras e diferenças entre segmentos.

Confiança operacional, recorrência, retenção, recomendação e pagamento serão validados posteriormente por protótipos, beta e comportamento real.

## Estado factual da execução

No checkpoint de 2026-08-08, o GKR não possui evidência integrada suficiente para declarar:

- pré-teste concluído;
- versão efetivamente publicada em uma rodada identificada;
- período real de aplicação;
- quantidade de respostas recebidas ou válidas;
- KPIs ou IGV calculados;
- decisão Go/Go com ajustes/Pivot/No-Go;
- product-market fit;
- disposição a pagar;
- retenção ou recorrência.

`VAL-009` e `VAL-010` definem exatamente o pacote de evidência necessário para promover esses fatos quando a base real estiver disponível.
