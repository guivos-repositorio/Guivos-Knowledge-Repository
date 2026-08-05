---
id: UXA-071
title: Materialização Documental do Mapa Integrado de Jornadas e Transições
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
related:
  - UXA-005
  - GKR-JOURNEYS-001
  - GKR-JOURNEYS-SCREEN-CATALOG-001
  - GKR-JOURNEYS-GAPS-001
  - UXA-072
  - M7.73
normative: false
---

# Materialização Documental do Mapa Integrado de Jornadas e Transições

## 1. Finalidade

A UXA-071 materializa, dentro do Guivos Knowledge Repository, a primeira seção documental integrada para inspecionar jornadas de **Pessoa**, **Coletivo** e **Organização**.

A seção organiza referências existentes, explicita transições, alterna perspectivas, mostra maturidade e registra lacunas. Ela não cria telas de produto, não executa lógica de negócio e não substitui as autoridades de origem.

## 2. Seção criada

A materialização está localizada em `docs/journeys/` e é publicada no menu principal como **Jornadas Integradas**.

| Módulo | Referência |
|---|---|
| visão geral e seletor de perspectivas | `docs/journeys/index.md` |
| jornada da Pessoa | `docs/journeys/person.md` |
| jornada do Coletivo | `docs/journeys/collective.md` |
| jornada da Organização | `docs/journeys/organization.md` |
| handoffs e fronteiras de autoridade | `docs/journeys/handoffs.md` |
| cenários documentais | `docs/journeys/scenarios.md` |
| fila de lacunas | `docs/journeys/gaps.md` |
| catálogo físico de telas | `docs/journeys/screen-catalog.md` |
| registro estruturado | `docs/journeys/registry.yml` |

## 3. Método

A materialização utiliza três unidades:

1. **nó de jornada**, que referencia uma superfície, estado ou responsabilidade;
2. **transição governada**, que registra condição, autoridade, efeito e evidência;
3. **lacuna explícita**, que impede a aparência de continuidade quando a cobertura não existe.

Cada referência preserva ID, caminho, versão e autoridade documental. Os SVGs permanecem em `docs/assets/wireframes/` e são usados em modo somente leitura.

## 4. Inventário físico

Foram catalogados **97 SVGs existentes**.

| Grupo físico | SVGs | Observação |
|---|---:|---|
| telas-base e superfícies gerais | 12 | âncoras, oportunidades, mapas, Organização e Coletivo |
| continuidade pessoal diretamente relacionada | 17 | materializados e validados |
| Coletivos | 22 | materializados e validados |
| Opportunity Boost | 46 | 36 validados e 10 pendentes |
| **Total físico** | **97** | não representa uma única jornada completa |

As contagens permanecem separadas. O total físico não promove cobertura funcional, maturidade ou completude.

## 5. Jornadas materializadas por referência

### 5.1 Pessoa

```text
Home pública
→ entrada protegida
→ expressão guiada por texto ou voz
→ inventário e autorização
→ processamento visível
→ compreensão inicial revisável
→ continuidade autorizada
```

A seção apresenta os 17 estados diretamente relacionados e usa Home pública e Tela Hoje como âncoras externas à contagem.

### 5.2 Pessoa em Coletivos

```text
Explorar
→ Resultados
→ Perfil Público
→ Revisão e Solicitação
→ Solicitação Pendente
→ lacuna: Meus Coletivos
```

A continuidade é interrompida de forma explícita antes de `Meus Coletivos`.

### 5.3 Coletivo e responsável

A seção organiza descoberta, participação, estados pendentes e autoridade protegida. Gestão recorrente, Central de Atualizações e Visão Geral do Responsável permanecem lacunas.

### 5.4 Organização

A Visão Geral da Organização e o cadastro de oportunidade são referenciados. A cobertura institucional completa e o fluxo bilateral Organização–Coletivo permanecem parciais.

### 5.5 Sobreposição comercial

Opportunity Boost aparece como camada comercial identificada. Não é participante, não adquire autoridade e não altera relevância orgânica, reputação ou decisões protegidas.

## 6. Handoffs materializados

A seção documenta, entre outros:

- Pessoa pública → Pessoa autenticada;
- Pessoa → autoridade protegida do Coletivo;
- autoridade protegida → Pessoa solicitante;
- Pessoa aprovada → vínculo governado pelo Coletivo;
- Organização → Coletivo em relação bilateral;
- Organização anunciante → Guivos Ads como operador econômico identificado.

O handoff transfere somente a próxima responsabilidade autorizada. Não transfere propriedade, identidade, dados ou autoridade geral.

## 7. Lacunas reveladas

A materialização confirma como prioridades:

1. `Meus Coletivos`;
2. Central de Atualizações;
3. reformulação do Início do Participante;
4. Visão Geral do Responsável;
5. matriz de cobertura institucional;
6. fluxo visual bilateral Organização–Coletivo;
7. validação dos 10 estados residuais do Opportunity Boost;
8. validação funcional da própria seção integrada.

## 8. Critérios de saída

A UXA-071 está materializada quando:

- a seção de primeiro nível existe;
- Pessoa, Coletivo e Organização possuem vistas próprias;
- há vista de handoffs, cenários, lacunas e catálogo;
- os 97 SVGs são referenciados sem cópia;
- maturidade e autoridade aparecem em texto;
- continuidades ausentes são visíveis;
- o mapa possui equivalente textual;
- a navegação MkDocs inclui a seção;
- a validação mecânica do repositório é aprovada.

## 9. Limites

A UXA-071 não:

- valida funcionalmente o mapa integrado;
- cria protótipo navegável;
- implementa aplicativo, motor, API, banco ou componentes;
- cria novos wireframes de produto;
- resolve as lacunas identificadas;
- testa com pessoas;
- inicia Engenharia de Produto;
- altera Resultados Empresariais ou baseline comercial.

## 10. Próxima transição

**UXA-072 — Validação Funcional do Mapa Integrado de Jornadas e Transições.**

A validação deverá verificar sequência, autoridade, visibilidade, reversibilidade, cobertura, acessibilidade documental e ausência de transições presumidas. Ela dependerá de autorização separada.
