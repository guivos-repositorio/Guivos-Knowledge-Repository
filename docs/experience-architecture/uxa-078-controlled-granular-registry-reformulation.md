---
id: UXA-078
title: Reformulação Controlada dos Registros Granulares de Transições e Superfícies
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-076
  - UXA-077
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.51.0
  - M7.72
normative: false
---

# Reformulação Controlada dos Registros Granulares de Transições e Superfícies

## 1. Finalidade

A UXA-078 reformula os registros granulares materializados pela UXA-076 para responder exclusivamente aos cinco achados obrigatórios da UXA-077.

O pacote corrige integridade documental. Ele não:

- cria telas ou funcionalidades;
- fecha lacunas de produto;
- valida jornadas ponta a ponta;
- promove os registros para `active`;
- inicia protótipo, aplicação, motor, testes ou Engenharia de Produto.

## 2. Base de trabalho

Base autorizada:

```text
main
5cf49e7da345164b9755ae75986e9f5316ae0c1f
```

Artefatos reformulados:

- `docs/journeys/surface-registry.md`;
- `docs/journeys/transition-registry.md`.

Artefatos sincronizados:

- `docs/journeys/index.md`;
- `docs/journeys/screen-catalog.md`;
- `docs/journeys/gaps.md`;
- `docs/experience-architecture/index.md`;
- `docs/project/current-state-register.md`;
- `docs/roadmap.md`.

## 3. Resultado quantitativo

| Registro | Antes | Depois | Motivo da variação |
|---|---:|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 36 | 40 | separação de mapa, lista, detalhe e fronteira externa |
| transições documentais | 34 | 37 | divisão de mapa/lista e retornos orgânicos |
| endpoints em texto livre | 2 | 0 | resolução por IDs controlados |

As novas entradas são referências documentais. Elas não representam implementação ou aumento automático do escopo do produto.

## 4. Correções executadas

### 4.1 F01 — endpoints estáveis

Foram criados ou utilizados endpoints controlados:

- `GKR-SURF-BND-001` — fronteira externa identificada;
- `GKR-SURF-PER-201` — Mapa de Oportunidades;
- `GKR-SURF-PER-202` — Lista de Oportunidades.

A transição `GKR-TRN-205` passa a terminar em `GKR-SURF-BND-001`.

A transição `GKR-TRN-304` passa a terminar em `GKR-SURF-PER-201`. O retorno à lista é registrado separadamente por `GKR-TRN-306`.

### 4.2 F02 — Coletivos e oportunidades

`GKR-SURF-PER-102` permanece exclusivamente como **Resultados de Busca de Coletivos**.

Foram criadas superfícies próprias para oportunidades:

- `GKR-SURF-PER-201` — Mapa de Oportunidades;
- `GKR-SURF-PER-202` — Lista de Oportunidades;
- `GKR-SURF-PER-203` — Detalhe de Oportunidade.

Os cartões permanecem componentes dos artefatos de mapa e lista nesta versão. Não são declarados como nó independente.

### 4.3 F03 — publicação institucional e detalhe

`GKR-SURF-ORG-003` é restringido ao estado institucional **oportunidade aprovada para ativação ou ativa**.

O Detalhe de Oportunidade percebido pela Pessoa passa a ser representado por `GKR-SURF-PER-203`.

A divisão preserva:

- a autoridade institucional da Organização;
- a perspectiva de decisão da Pessoa;
- a ausência de continuidade integrada validada entre publicação e consumo.

### 4.4 F04 — estados residuais

A materialização de `GKR-SURF-COM-005` e a evidência de `GKR-TRN-305` passam a apontar para **UXA-055**.

Os dez estados residuais continuam:

- materializados;
- sem validação funcional específica integrada;
- sem promoção automática.

### 4.5 F05 — campos obrigatórios

O registro de superfícies passa a apresentar, para cada ID:

- artefato canônico e caminho;
- versão;
- decisão principal;
- dados e conteúdos;
- gate;
- reversibilidade;
- supersessão;
- observação de escopo.

Quando a evidência não permite um valor seguro, o campo é registrado como:

- `indeterminado`;
- `ausente`;
- `não examinado`.

Nenhum campo é preenchido por inferência.

## 5. Preservação de identificadores

IDs anteriores foram preservados quando o significado permaneceu válido.

| ID | Tratamento |
|---|---|
| GKR-SURF-PER-102 | preservado e restringido à busca de Coletivos |
| GKR-SURF-ORG-003 | preservado como estado institucional; significado misto removido |
| GKR-SURF-COM-005 | preservado; materialização corrigida para UXA-055 |
| GKR-TRN-203 a GKR-TRN-205 | preservados com endpoints e domínios corrigidos |
| GKR-TRN-304 e GKR-TRN-305 | preservados com destino ou evidência corrigidos |

Novos IDs foram usados somente quando a divisão exigia nova referência estável.

## 6. Matriz de atendimento

| Achado UXA-077 | Resultado da UXA-078 |
|---|---|
| F01 — endpoints em texto livre | corrigido documentalmente |
| F02 — busca de Coletivos usada para oportunidades | corrigido documentalmente |
| F03 — publicação misturada com detalhe | corrigido documentalmente |
| F04 — fonte residual incorreta | corrigido para UXA-055 |
| F05 — campos obrigatórios ausentes | campos adicionados por ID |

A classificação `corrigido documentalmente` não equivale a validação funcional. O atendimento deverá ser examinado em novo pacote.

## 7. Estados preservados

Permanecem `draft`:

- `GKR-JOURNEY-SURFACE-REGISTRY-001`, versão 0.2.0;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`, versão 0.2.0;
- Jornada Integrada da Pessoa;
- Jornada Integrada do Coletivo;
- Jornada Integrada da Organização.

Continuam `active` nos limites anteriormente aprovados:

- visão geral das Jornadas Integradas;
- handoffs resumidos;
- cenários documentais;
- catálogo agregado;
- registro observacional de lacunas.

## 8. Lacunas não fechadas

Permanecem abertas:

- continuidade entre compreensão inicial e Tela Hoje;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação bilateral de solicitações;
- relação Organização–Coletivo materializada;
- matriz institucional completa;
- validação dos dez estados residuais do Opportunity Boost;
- efeitos externos de oportunidades;
- matriz integrada de erros, retornos e interrupções.

A fronteira externa identificada apenas estabiliza o endpoint; não valida o efeito externo.

## 9. Limites

A UXA-078 não executa as ressalvas não bloqueadoras da UXA-077 como ampliação de escopo. Portanto:

- os campos de transição continuam agrupados nas colunas existentes;
- a cobertura permanece seletiva e não exaustiva;
- `COM` continua sendo agrupamento documental, não participante estrutural.

## 10. Próxima transição possível

A próxima evolução documental possível é:

**UXA-079 — Revalidação Funcional dos Registros Granulares Reformulados.**

A UXA-079 não é iniciada por este pacote e exige autorização separada.

Protótipo, aplicação, motor, teste com pessoas e Engenharia de Produto permanecem não iniciados.
