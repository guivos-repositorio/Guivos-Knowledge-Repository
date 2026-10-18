---
id: GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-VISUAL-PROTOTYPE-DECISION-CANDIDATE-001
title: Dashboard Organização — Instrumento Candidato de Decisão para Prototipação Visual
status: draft
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-10-18
normative: false
maturity: pre_authorization_visual_prototype_decision
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-CANDIDATE-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-HANDOFF-CANDIDATE-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-BRAND-COLOR-PALETTE-001
  - GKR-BRAND-TYPOGRAPHY-001
---

# Dashboard Organização — Decisão Candidata de Prototipação Visual

> **Instrumento de decisão, não autorização.** A integração do contrato de Design (PR #704) e do Handoff de Design (PR #705) ao GKR não aprova nem inicia prototipação no Replit. O presente documento é candidato, não normativo, sujeito à adjudicação institucional específica.

## 1. Pergunta de decisão

Pode-se autorizar, em ato separado e explicitamente delimitado, um **protótipo visual de demonstração** do Dashboard Organização, com cenários 100% artificiais, sem serviços reais, autenticação produtiva ou implantação?

A decisão deve separar:
1. **Aprovação documental deste instrumento:** registra critérios e escopo de avaliação; não inicia o protótipo.
2. **Autorização futura da prototipação visual:** habilita somente trabalho demonstrativo dentro de limites definidos, após escolha do espaço de trabalho, responsáveis e aceite de critérios.
3. **Autorização operacional:** permanece distinta e condicionada a gates, contratos, autoridades e revisões próprios.

**Estado atual da pergunta:** NOT AUTHORIZED — DECISION PREPARATION ONLY.

## 2. Escopo visual que poderá ser considerado

| Elemento demonstrável | Limite |
|---|---|
| Cabeçalho de Organização e Analytics contextual | Identidade de Organização fictícia; nenhuma identidade real ou login operacional |
| Nove agrupamentos V01..V09 | Navegação **interna** demonstrativa, sem criar `GKR-SURF-*`, `GKR-TRN-*` ou rotas de produto canônicas |
| Cards, gráficos, tabelas e legendas | Fixtures artificiais claramente identificadas; sem afirmar medição real |
| Filtros e comparação de períodos | Interação local com dados simulados; não representar consulta real ou autoridade concedida |
| Mapas e grafos | Nós, territórios e vínculos sintéticos; agregação e supressão demonstrativas |
| Oito estados de visualização | Demonstrar `AVAILABLE`, `LOADING`, `NO_DATA`, `INSUFFICIENT_DATA`, `SUPPRESSED_BY_POLICY`, `SOURCE_DELAYED`, `NOT_ENTITLED` e `ERROR` com fixtures |
| Desktop, tablet e mobile | Responsividade, foco, teclado, contraste, redução de movimento e alternativas tabulares |
| Experiência visual Guivos | Canvas `#FFFFFF`; somente os 30 tokens da paleta oficial para UI; Goldplay conforme escala oficial (inclusive Display 60/60 SemiBold) |

O designer possui liberdade de composição, hierarquia, fotografia, disposição e linguagem visual, respeitando as autoridades acima. O handoff não prescreve um wireframe obrigatório.

## 3. Exclusões explícitas

- **Dados:** nenhuma fonte real, dados pessoais, dados institucionais privados, Journey individual, dados reais da Guivos, importação/exportação ou consulta à produção.
- **Backend:** nenhuma API real, banco conectado, autenticação, autorização/RBAC técnico, billing, webhooks, processamento ou integrações.
- **Produto:** nenhuma publicação operacional, ativação de funcionalidades, criação de direitos comerciais, migração de plano ou alteração de navegação canônica.
- **Métricas:** nenhuma promoção de KPI para READY, inferência de denominadores ou impacto, cálculo de economia verdadeira ou ranking reputacional.
- **Contextos:** não fundir Dashboard Organização, Home autenticada, Guivos Business Dashboard e Dashboard Coletivo.
- **Protótipo:** não chamar o simulador de painel funcional/atualizado em tempo real, nem apresentar valores como evidências da operação real.

O protótipo, se futuramente autorizado, deve exibir aviso persistente e inequívoco: **“DEMONSTRAÇÃO — DADOS FICTÍCIOS. NÃO REPRESENTA A OPERAÇÃO REAL.”**

## 4. Governança de estados e segurança demonstrativa

- `NOT_ENTITLED` representa exclusivamente indisponibilidade de capacidade/entitlement comercial quando é legítimo mostrar tal condição. **Negativa de autorização** ocorre fora da renderização, antes do acesso, e não deve produzir convite a upgrade nem revelar o objeto protegido.
- `NO_DATA` não equivale a zero. `INSUFFICIENT_DATA` não autoriza estimativa. `SOURCE_DELAYED` não é dado atualizado. `SUPPRESSED_BY_POLICY` não expõe magnitudes aproximadas.
- Trocar Organização, unidade ou papel no protótipo demonstra descarte de contexto e reavaliação conceitual, **não** constitui RBAC implementado.
- Funis, mapas e grafos são recursos visuais condicionais e não implicam fontes de verdade existentes, acordos bilaterais ou privacidade validada.
- Fixtures devem ser sintéticas e isoladas, com valores declaradamente ilustrativos; não reutilizar informações reais ou sensíveis para criar “exemplos realistas”.

## 5. Pacote de decisão antes de iniciar Replit

| Critério decisório | Evidência mínima | Situação |
|---|---|---|
| Documento e precedência | PRs #704/#705 integradas, referências vigentes | DOCUMENTED |
| Alcance do trabalho | Visual demonstrativo, sem backend ou dados reais | PROPOSED |
| Identidade visual | Paleta normativa e escala Goldplay consultadas | DOCUMENTED |
| Fixture e aviso | Dataset inteiramente artificial e aviso persistente | TO_DEFINE |
| Local de prototipação | Projeto Replit novo e distinto dos dashboards existentes, nome e finalidade aprovados | TO_DECIDE |
| Responsabilidade | Owner Intelligence; Design/UX consultado; decisão de execução institucional | TO_DECIDE |
| Critérios de aceitação | Revisão responsiva, estados, acessibilidade e fidelidade | PROPOSED |
| Autoridade de execução | Consentimento explícito separado para iniciar prototipação visual | NOT AUTHORIZED |

A decisão futura deve identificar expressamente **qual repositório/projeto Replit**, quem revisa o protótipo e quais arquivos ou ações estão autorizados. A preparação deste pacote não supre esses campos.

## 6. Checklist de aceite de eventual protótipo demonstrativo

- [ ] Nove agrupamentos internos, navegáveis, sem expansão da navegação canônica.
- [ ] Todos os números e gráficos com fixtures artificiais e aviso persistente.
- [ ] Oito estados acessíveis; autorização negada não confundida com `NOT_ENTITLED`.
- [ ] Cenários: leitura disponível, vazia/insuficiente, suprimida/atrasada e mudança de contexto.
- [ ] Cards, séries, tabelas, mapas e grafos só onde houver sentido e com alternativa textual/tabular.
- [ ] Canvas `#FFFFFF`, 30 tokens cromáticos oficiais exclusivamente e Goldplay oficial.
- [ ] Experiência em desktop, tablet e mobile, incluindo teclado, leitor de tela e movimento reduzido.
- [ ] Nenhuma integração, dados reais, API, RBAC técnico, exportação ou publicação de produto.
- [ ] Nenhum KPI promovido e gates analíticos preservados.
- [ ] Revisão visual por Design/UX e verificação documental por Intelligence antes de qualquer maturidade adicional.

## 7. Gates analíticos — inalterados

Todos os **39 KPIs do Anexo C** permanecem `proposed / NOT_READY`. As **14 leituras complementares** permanecem não canônicas. `G-ORG-01..07` continuam com os estados do documento mestre; especificamente `G-ORG-05 = BLOCKED` e `G-ORG-07 = NOT_AUTHORIZED`. Não inferir fechamento dos demais gates a partir de demonstração com fixtures.

## 8. Matriz de decisão proposta

| Opção | Significado | Recomendação |
|---|---|---|
| A — Apenas documentação | Aceitar o instrumento como candidato de governança, sem protótipo | **Estado atual** |
| B — Autorizar protótipo visual isolado | Ato posterior e expresso; fixtures; projeto Replit separado; exclusões mantidas | **Candidata para próxima deliberação** |
| C — Autorizar dashboard operacional | Dados reais, RBAC, integrações, KPIs e gates resolvidos | **Não elegível nesta maturidade** |

## 9. Saída e decisão pendente

**Resultado desta PR, se integrada:** GKR passa a registrar um **instrumento candidato de decisão**, sem execução em Replit e sem adjudicar autorização de prototipação.

**Próxima decisão humana necessária:** autorizar ou não, em ato separado, a **Opção B** com projeto identificado e limites explícitos. Até esse ato: `REPLIT NOT STARTED / VISUAL PROTOTYPE NOT AUTHORIZED / OPERATIONAL ENGINEERING BLOCKED`.
