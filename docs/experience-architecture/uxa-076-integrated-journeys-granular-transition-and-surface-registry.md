---
id: UXA-076
title: Registro Granular de Transições e Superfícies das Jornadas Integradas
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - GKR-JOURNEYS-001
related:
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.49.0
  - M7.72
normative: false
---

# Registro Granular de Transições e Superfícies das Jornadas Integradas

## 1. Finalidade

A UXA-076 materializa registros granulares para superfícies e transições das Jornadas Integradas, conforme evolução documental recomendada pela UXA-075.

O objetivo é permitir que cada superfície e cada ligação relevante possuam identificador estável, perspectiva, maturidade, autoridade, evidência, estado de continuidade e lacuna associada.

A UXA-076 não cria novas telas, contratos ou comportamentos de produto. Ela registra, por referência, o que já existe, o que está contratado e o que permanece ausente.

## 2. Base governada

Base de trabalho: `main` em `7c997e65714afb506d94e4f68929079db33b45a7`.

A materialização parte das seguintes autoridades:

- UXA-070 para campos de nós, transições, maturidade e tipos de ligação;
- UXA-074 para limites de evidência e ressalvas da validação;
- UXA-075 para a decisão seletiva de status;
- vistas vigentes de Pessoa, Coletivo, Organização, handoffs, cenários, catálogo e lacunas.

## 3. Artefatos materializados

A UXA-076 cria dois registros complementares:

1. `docs/journeys/surface-registry.md` — cadastro granular de superfícies, estados e responsabilidades conhecidas;
2. `docs/journeys/transition-registry.md` — cadastro granular de transições documentais, incluindo ligações parciais, ausentes e não examinadas.

Os dois registros permanecem `draft` até validação funcional específica.

## 4. Convenção de identificadores

### 4.1 Superfícies

Formato:

```text
GKR-SURF-<PARTICIPANTE>-NNN
```

Participantes e perspectivas usam os agrupamentos:

- `PER` — Pessoa;
- `COL` — Coletivo;
- `ORG` — Organização;
- `COM` — camada comercial identificada.

### 4.2 Transições

Formato:

```text
GKR-TRN-NNN
```

O identificador da transição não implica implementação. Ele apenas estabiliza a referência documental.

## 5. Campos obrigatórios do registro de superfícies

Cada superfície ou estado declara:

- identificador;
- participante-base;
- perspectiva ou papel;
- família de jornada;
- nome da superfície ou responsabilidade;
- canal;
- maturidade primária;
- autoridade governante;
- referência materializada;
- evidência de validação;
- entrada conhecida;
- saída conhecida;
- continuidade integrada;
- lacuna associada;
- observação de escopo.

## 6. Campos obrigatórios do registro de transições

Cada transição declara:

- identificador;
- origem;
- destino;
- participante e perspectiva;
- tipo de transição;
- condição;
- autoridade;
- ação iniciadora;
- efeito conhecido;
- dados ou conteúdos que atravessam a fronteira;
- autorização ou gate;
- reversibilidade;
- interrupção;
- tempo;
- evidência;
- estado da transição;
- lacuna associada.

Quando a evidência for insuficiente, o campo é registrado como `indeterminado`, `ausente` ou `não examinado`, sem preenchimento por inferência.

## 7. Escopo inicial materializado

O registro inicial cobre, em granularidade documental:

- início protegido e compreensão inicial da Pessoa;
- continuidade para Tela Hoje;
- descoberta, busca, Perfil Público, revisão e solicitação em Coletivos;
- estados pendentes na perspectiva da Pessoa;
- superfícies ausentes previstas para continuidade em Coletivos;
- operação do responsável pelo Coletivo como ausência explícita;
- Visão Geral institucional e oportunidades;
- relação Organização–Coletivo;
- Opportunity Boost como camada comercial identificada;
- handoffs prioritários já registrados pela UXA-075.

## 8. Regras de interpretação

- uma superfície registrada não equivale a uma tela implementada;
- uma transição registrada como `parcial` não equivale a continuidade validada;
- origem e destino materializados em pacotes distintos não comprovam integração ponta a ponta;
- autoridade contratual não equivale a interface materializada;
- retorno visível para a Pessoa não comprova operação interna do responsável;
- estado `ausente` deve permanecer visível;
- o registro não fecha lacunas nem altera prioridades de produto;
- o registro não substitui artefatos canônicos.

## 9. Critérios de aceitação da materialização

- [x] identificadores estáveis definidos;
- [x] superfícies e responsabilidades conhecidas registradas individualmente;
- [x] transições prioritárias registradas individualmente;
- [x] autoridade, evidência e lacunas mantidas separadas;
- [x] ligações parciais, ausentes e não examinadas permanecem explícitas;
- [x] nenhuma jornada foi promovida;
- [x] nenhuma lacuna de produto foi fechada;
- [x] nenhum protótipo ou componente técnico foi iniciado.

## 10. Resultado controlado

A UXA-076 materializa uma primeira versão granular e rastreável dos registros de superfícies e transições.

O pacote não:

- promove as vistas de Pessoa, Coletivo ou Organização;
- valida os novos registros;
- cria SVG, wireframe, protótipo ou aplicação;
- executa lógica de negócio;
- fecha lacunas de produto;
- inicia Engenharia de Produto.

## 11. Próxima transição recomendada

A próxima transição recomendada é:

**UXA-077 — Validação Funcional do Registro Granular de Transições e Superfícies**, mediante autorização separada.

A UXA-077 não está iniciada.
