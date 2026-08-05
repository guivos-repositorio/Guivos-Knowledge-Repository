---
id: UXA-077
title: Validação Funcional do Registro Granular de Transições e Superfícies
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.50.0
  - M7.72
normative: false
---

# Validação Funcional do Registro Granular de Transições e Superfícies

## 1. Finalidade

A UXA-077 valida documentalmente a primeira versão dos registros granulares materializados pela UXA-076.

O exame verifica se os registros permitem inspecionar superfícies, estados, responsabilidades, transições, autoridades, evidências e lacunas sem:

- misturar participantes ou famílias funcionais;
- criar ligações por inferência;
- confundir materialização com validação;
- substituir artefatos canônicos;
- declarar jornada completa;
- iniciar produto, protótipo ou Engenharia de Produto.

## 2. Base validada

Base de trabalho: `main` em `5c8b5642aed3e03de5d54fc997a7b60162ced69c`.

Artefatos examinados:

- `docs/journeys/surface-registry.md`, versão 0.1.0;
- `docs/journeys/transition-registry.md`, versão 0.1.0;
- UXA-070 como programa funcional;
- UXA-076 como autoridade de materialização;
- contratos, wireframes e validações referenciados pelas entradas auditadas.

Escopo quantitativo declarado e confirmado:

- 36 superfícies, estados, responsabilidades ou ausências conhecidas;
- 34 transições documentais;
- identificadores sem duplicidade dentro de cada registro.

## 3. Método

A validação foi executada em sete eixos:

1. integridade dos identificadores;
2. resolução de origem e destino;
3. coerência entre participante, perspectiva e família;
4. rastreabilidade de autoridade, materialização e validação;
5. conformidade com os campos da UXA-070 e da UXA-076;
6. preservação de estados parciais, ausentes e não examinados;
7. ausência de promoção, fechamento de lacunas ou implementação implícita.

## 4. Resultado executivo

**Parecer: não aprovado até correção obrigatória.**

Os registros constituem uma base documental útil e preservam corretamente diversas lacunas. Entretanto, ainda não podem ser promovidos porque existem inconsistências de endpoint, mistura entre famílias funcionais, referência incorreta de evidência e incompletude de campos obrigatórios.

```text
materialização granular confirmada
≠ integridade funcional aprovada
≠ promoção para active
≠ jornada ponta a ponta validada
```

## 5. Aspectos aprovados

### 5.1 Identificadores e contagens

- 36 entradas de superfície ou responsabilidade foram confirmadas;
- 34 transições foram confirmadas;
- os IDs `GKR-SURF-*` e `GKR-TRN-*` não se repetem dentro de seus registros;
- Pessoa, Coletivo, Organização e camada comercial permanecem distinguíveis.

### 5.2 Vocabulário de maturidade

Os estados utilizados no registro de superfícies pertencem ao vocabulário controlado da UXA-070:

- contratado;
- programado;
- materializado;
- validado;
- reformulação pendente;
- não iniciado;
- indeterminado.

### 5.3 Preservação de incerteza

Os registros mantêm visíveis estados como:

- parcial;
- ausente;
- não examinado;
- localmente validada;
- contratada sem materialização.

A validação local não foi apresentada como continuidade ponta a ponta.

### 5.4 Limites de produto

Não foram identificados:

- criação de tela por atribuição de ID;
- fechamento automático de lacunas;
- promoção das vistas de Pessoa, Coletivo ou Organização;
- execução de lógica de negócio;
- início de protótipo ou Engenharia de Produto.

## 6. Achados obrigatórios

### F01 — Endpoints sem identificador estável

**Severidade:** bloqueadora.

As transições abaixo possuem destino em texto livre:

- `GKR-TRN-205` → `destino externo identificado`;
- `GKR-TRN-304` → `superfície orgânica de origem`.

Isso impede resolução determinística e viola o objetivo de estabilizar origem e destino.

**Correção obrigatória:** criar endpoints documentais controlados ou decompor as transições para que cada origem e destino resolva para um ID registrado. Um destino externo poderá ser representado por uma fronteira documental identificada, sem transformar entidade externa em participante estrutural.

### F02 — Mistura entre busca de Coletivos e descoberta de oportunidades

**Severidade:** bloqueadora.

`GKR-SURF-PER-102` representa `Resultados de Busca` da jornada de Coletivos, governada pelas UXA-056, UXA-060 e UXA-061.

Entretanto:

- `GKR-TRN-203` usa essa superfície como destino de uma oportunidade publicada;
- `GKR-TRN-204` usa a mesma superfície como origem para selecionar uma oportunidade.

A entrada não representa catálogo, mapa, lista ou resultado de oportunidades.

**Correção obrigatória:** registrar superfícies próprias de descoberta de oportunidades — incluindo mapa, lista, cartão ou detalhe conforme fontes UXA-004, UXA-024 a UXA-033 e UXA-007/UXA-012 — e remapear as transições sem reutilizar a busca de Coletivos.

### F03 — Conflito entre estado institucional publicado e detalhe percebido pela Pessoa

**Severidade:** alta e bloqueadora.

`GKR-SURF-ORG-003` é nomeada `oportunidade publicada`, mas aponta para UXA-007 e UXA-012, que governam o **Detalhe de Oportunidade** percebido pela Pessoa.

A mesma entrada combina:

- estado do ciclo de publicação da Organização;
- superfície pública de consulta;
- referências de descoberta dispersas.

**Correção obrigatória:** separar o estado institucional de publicação da superfície de detalhe percebida pela Pessoa. Cada entrada deverá possuir participante-base, perspectiva, materialização e validação coerentes.

### F04 — Rastreabilidade incorreta dos dez estados residuais

**Severidade:** alta e bloqueadora.

As entradas:

- `GKR-SURF-COM-005`;
- `GKR-TRN-305`;

atribuem os dez estados residuais a `UXA-047 a UXA-054 conforme pacote`.

A fonte específica dos dez estados residuais é a **UXA-055**, que materializa dez referências móveis ainda não validadas funcionalmente.

**Correção obrigatória:** registrar UXA-055 como materialização dos estados residuais, manter validação ausente e separar referências anteriores somente quando sustentarem partes específicas da continuidade.

### F05 — Campos obrigatórios incompletos no registro de superfícies

**Severidade:** alta e bloqueadora.

A UXA-070 exige, por nó, elementos como:

- artefato canônico e caminho;
- versão;
- decisão principal;
- dados e conteúdos;
- gate;
- reversibilidade;
- supersessão.

A UXA-076 também declarou `observação de escopo` como campo obrigatório.

O registro atual não apresenta esses campos de forma individual por entrada.

**Correção obrigatória:** ampliar a tabela ou criar blocos de detalhe por ID. Valores ainda desconhecidos deverão ser registrados como `indeterminado`, `ausente` ou `não examinado`, nunca omitidos.

## 7. Ressalvas não bloqueadoras

### R01 — Campos de transição agregados

O registro reúne em uma mesma coluna:

- condição e ação;
- efeito e dados;
- reversibilidade, interrupção e tempo.

O conteúdo geralmente está presente, mas a agregação reduz inspeção mecânica e comparação entre transições. Recomenda-se separar os campos ou adicionar blocos de detalhe por ID.

### R02 — Cobertura seletiva

O registro é uma primeira versão e não cobre todas as superfícies e transições existentes no repositório. Essa condição é aceitável enquanto o escopo inicial permanecer explícito e não for apresentado como inventário completo.

### R03 — Camada comercial

O prefixo `COM` funciona como agrupamento documental. Ele não transforma Opportunity Boost, Guivos Ads ou anunciante em participante estrutural adicional.

## 8. Matriz de decisão

| Critério | Resultado |
|---|---|
| IDs únicos | aprovado |
| contagens declaradas | aprovado |
| vocabulário de maturidade | aprovado |
| preservação de lacunas | aprovado |
| origem e destino resolvíveis | não aprovado |
| separação entre famílias | não aprovado |
| rastreabilidade de evidência | não aprovado |
| campos obrigatórios de superfície | não aprovado |
| prontidão para promoção | não aprovada |
| prontidão para protótipo ou implementação | não avaliada e não autorizada |

## 9. Estado dos registros após o parecer

Permanecem `draft`:

- `GKR-JOURNEY-SURFACE-REGISTRY-001`;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
- Jornada Integrada da Pessoa;
- Jornada Integrada do Coletivo;
- Jornada Integrada da Organização.

Continuam `active` dentro dos limites já aprovados:

- visão geral das Jornadas Integradas;
- handoffs resumidos;
- cenários documentais;
- catálogo agregado;
- registro observacional de lacunas.

## 10. Correção exigida

A reformulação deverá, no mínimo:

1. resolver todos os endpoints por identificador;
2. criar superfícies próprias para descoberta e detalhe de oportunidades;
3. separar publicação institucional de consulta pela Pessoa;
4. corrigir a rastreabilidade dos estados residuais para UXA-055;
5. completar os campos obrigatórios do registro de superfícies;
6. preservar IDs existentes quando o significado não mudar;
7. documentar qualquer supersessão ou divisão de entrada;
8. manter lacunas e estados não examinados explícitos.

## 11. Limites preservados

A UXA-077 não:

- corrige os registros;
- promove qualquer registro para `active`;
- fecha lacunas de produto;
- cria wireframes, SVGs ou telas;
- inicia protótipo, aplicação ou motor;
- inicia testes com pessoas;
- inicia Engenharia de Produto.

## 12. Próxima transição recomendada

A próxima transição documental recomendada é:

**UXA-078 — Reformulação Controlada dos Registros Granulares de Transições e Superfícies**, mediante autorização separada.

Após a reformulação, uma nova validação funcional deverá ocorrer em pacote próprio. A UXA-078 não está iniciada.
