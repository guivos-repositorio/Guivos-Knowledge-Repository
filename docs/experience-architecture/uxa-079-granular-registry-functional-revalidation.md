---
id: UXA-079
title: Revalidação Funcional dos Registros Granulares Reformulados
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-076
  - UXA-077
  - UXA-078
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.52.0
  - M7.72
normative: false
---

# Revalidação Funcional dos Registros Granulares Reformulados

## 1. Finalidade

A UXA-079 revalida documentalmente os registros granulares reformulados pela UXA-078 e verifica se os cinco achados bloqueadores da UXA-077 foram efetivamente resolvidos.

A etapa examina integridade funcional documental. Ela não:

- promove automaticamente os registros para `active`;
- declara jornadas completas ou validadas ponta a ponta;
- fecha lacunas de produto;
- cria telas, protótipo, aplicação ou motor;
- inicia testes com pessoas ou Engenharia de Produto.

## 2. Base revalidada

Base de trabalho:

```text
main
2547df6a403c493e9e17cf6c8af6405b8c468705
```

Artefatos examinados:

- `docs/journeys/surface-registry.md`, versão 0.2.0;
- `docs/journeys/transition-registry.md`, versão 0.2.0;
- `docs/journeys/surface-registry-person-details.md`, versão 0.1.0;
- `docs/journeys/surface-registry-collective-details.md`, versão 0.1.0;
- `docs/journeys/surface-registry-organization-details.md`, versão 0.1.0;
- `docs/journeys/surface-registry-commercial-boundary-details.md`, versão 0.1.0;
- UXA-077 como parecer bloqueador anterior;
- UXA-078 como autoridade da reformulação.

Escopo quantitativo confirmado:

- 40 superfícies, estados, responsabilidades ou fronteiras;
- 37 transições documentais;
- 74 referências de endpoint, considerando origem e destino de cada transição;
- zero endpoint em texto livre.

## 3. Método

A revalidação foi executada em oito eixos:

1. unicidade e estabilidade dos identificadores;
2. resolução determinística de todas as origens e destinos;
3. separação entre Coletivos, oportunidades e estado institucional;
4. coerência entre participante, perspectiva e família funcional;
5. rastreabilidade de autoridade, materialização e validação;
6. presença dos campos obrigatórios por superfície;
7. preservação de incerteza, lacunas e estados não examinados;
8. ausência de promoção, implementação ou fechamento implícito.

## 4. Resultado executivo

**Parecer: aprovado com ressalvas no escopo funcional documental.**

Os cinco bloqueios da UXA-077 foram resolvidos de forma suficiente para retirar o impedimento funcional documental. Os registros podem seguir para uma eventual promoção controlada em pacote separado.

A aprovação não significa:

```text
registro aprovado documentalmente
≠ jornada completa
≠ continuidade ponta a ponta validada
≠ superfície implementada
≠ prontidão para protótipo
≠ autorização de Engenharia de Produto
```

## 5. Revalidação dos cinco achados

### F01 — endpoints estáveis

**Resultado: aprovado.**

- todas as 37 transições utilizam IDs registrados em origem e destino;
- as 74 referências de endpoint resolvem para entradas do registro de superfícies;
- `GKR-TRN-205` termina em `GKR-SURF-BND-001`;
- `GKR-TRN-304` termina em `GKR-SURF-PER-201`;
- `GKR-TRN-306` registra separadamente o retorno para `GKR-SURF-PER-202`;
- não restam destinos como `destino externo identificado` ou `superfície orgânica de origem` em texto livre.

A fronteira externa permanece documental e não presume integração técnica ou resultado externo.

### F02 — separação entre Coletivos e oportunidades

**Resultado: aprovado.**

- `GKR-SURF-PER-102` permanece exclusivo dos Resultados de Busca de Coletivos;
- o domínio de oportunidades utiliza `GKR-SURF-PER-201`, `GKR-SURF-PER-202` e `GKR-SURF-PER-203`;
- nenhuma transição de publicação ou consumo de oportunidades utiliza a busca de Coletivos;
- mapa, lista e detalhe possuem responsabilidades e evidências próprias.

### F03 — publicação institucional e detalhe percebido pela Pessoa

**Resultado: aprovado.**

- `GKR-SURF-ORG-003` representa o estado institucional de oportunidade aprovada para ativação ou ativa;
- `GKR-SURF-PER-203` representa o Detalhe de Oportunidade percebido pela Pessoa ou visitante;
- `GKR-TRN-203` registra a passagem entre publicação e descoberta como `não examinada`;
- a separação preserva autoridade institucional, perspectiva de consumo e lacuna de integração.

### F04 — rastreabilidade dos estados residuais

**Resultado: aprovado.**

- `GKR-SURF-COM-005` utiliza UXA-055 como materialização;
- `GKR-TRN-305` utiliza UXA-055 como evidência;
- os dez estados residuais permanecem sem validação funcional específica integrada;
- nenhuma referência anterior é usada para promover esses estados.

### F05 — campos obrigatórios por superfície

**Resultado: aprovado.**

As 40 entradas possuem detalhamento por ID, distribuído de forma controlada em quatro arquivos:

| Detalhamento | Entradas |
|---|---:|
| Pessoa | 19 |
| Coletivo | 8 |
| Organização | 7 |
| camada comercial e fronteira | 6 |
| **Total** | **40** |

Cada entrada explicita:

- artefato canônico e caminho;
- versão;
- entrada;
- decisão principal;
- saída;
- dados e conteúdos;
- gate;
- reversibilidade;
- supersessão;
- continuidade;
- lacuna;
- observação de escopo.

Valores sem evidência suficiente permanecem `indeterminado`, `ausente` ou `não examinado`.

## 6. Matriz de decisão

| Critério | Resultado |
|---|---|
| IDs de superfície únicos | aprovado |
| IDs de transição únicos | aprovado |
| contagens declaradas | aprovado |
| resolução das 74 referências de endpoint | aprovado |
| separação entre Coletivos e oportunidades | aprovado |
| separação entre publicação e detalhe | aprovado |
| rastreabilidade para UXA-055 | aprovado |
| campos obrigatórios das 40 entradas | aprovado |
| preservação de incerteza e lacunas | aprovado |
| ausência de promoção ou implementação implícita | aprovado |
| cobertura exaustiva do ecossistema | não declarada |
| continuidade ponta a ponta | não aprovada por esta etapa |

## 7. Ressalvas preservadas

### R01 — campos de transição agregados

Condição e ação, efeito e dados, além de reversibilidade, interrupção e tempo, continuam agrupados em colunas compostas. O conteúdo é suficiente para esta revalidação, mas a separação futura poderá melhorar inspeção mecânica.

### R02 — cobertura seletiva

Os registros não constituem inventário exaustivo de todas as superfícies e transições do ecossistema. A aprovação vale somente para o conjunto explicitamente registrado.

### R03 — camada comercial

O prefixo `COM` permanece um agrupamento documental. Ele não cria participante estrutural adicional nem concede autoridade comercial sobre reputação, relevância ou decisão humana.

## 8. Prontidão para promoção controlada

A revalidação considera os registros aptos a uma **promoção documental controlada**, desde que executada em ato separado e limitada aos instrumentos de registro.

Uma eventual promoção não poderá:

- alterar a maturidade das entradas individuais;
- converter estados `ausente`, `parcial` ou `não examinado` em completos;
- promover automaticamente as jornadas da Pessoa, Coletivo ou Organização;
- fechar lacunas;
- declarar implementação.

## 9. Estado após o parecer

Permanecem `draft` até eventual promoção separada:

- `GKR-JOURNEY-SURFACE-REGISTRY-001`, versão 0.2.0;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`, versão 0.2.0;
- os quatro detalhamentos obrigatórios;
- Jornada Integrada da Pessoa;
- Jornada Integrada do Coletivo;
- Jornada Integrada da Organização.

Continuam `active` dentro dos limites já aprovados:

- visão geral das Jornadas Integradas;
- handoffs resumidos;
- cenários documentais;
- catálogo agregado;
- registro observacional de lacunas.

## 10. Limites preservados

A UXA-079 não:

- modifica os registros revalidados;
- promove qualquer artefato;
- fecha lacunas de produto;
- cria ou altera wireframes e SVGs;
- inicia protótipo, aplicação ou motor;
- inicia testes com pessoas;
- inicia Engenharia de Produto.

## 11. Próxima transição possível

A próxima evolução documental possível é:

**UXA-080 — Promoção Controlada dos Registros Granulares e Sincronização Pós-Revalidação.**

A UXA-080 não é iniciada por este pacote e exige autorização separada.
