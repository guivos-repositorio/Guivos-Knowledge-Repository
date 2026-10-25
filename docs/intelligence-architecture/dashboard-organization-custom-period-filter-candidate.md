---
id: GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-CUSTOM-PERIOD-CANDIDATE-001
title: Dashboard Organização — Filtro de Período por Calendário (Contrato Candidato)
status: draft
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-10-18
normative: false
maturity: visual_prototype_interaction_candidate
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-CANDIDATE-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-DESIGN-HANDOFF-CANDIDATE-001
  - GKR-INTELLIGENCE-DASHBOARD-ORGANIZATION-VISUAL-PROTOTYPE-DECISION-CANDIDATE-001
  - GKR-BRAND-COLOR-PALETTE-001
  - GKR-BRAND-TYPOGRAPHY-001
---

# Dashboard Organização — Filtro de Período por Calendário

> **Contrato candidato de experiência demonstrativa, não nova definição de KPI ou autorização para consumo real de dados.** Complementa a seleção por trimestre com intervalo livre de data inicial e data final.

## 1. Finalidade

Permitir que a Organização examine informações por um período escolhido diretamente no calendário, além dos períodos predefinidos existentes. A experiência deve ser compartilhada por **todas as nove áreas internas V01..V09 que apresentem leituras sujeitas a período**, sem implementações divergentes de filtro em cada tela.

A navegação Analytics continua contextual; este contrato não cria superfície, transição, fonte, entitlement ou direito de divulgação novos.

## 2. Modos de escolha

1. **Período predefinido:** preservar opções de trimestre já disponíveis e a respectiva apresentação em português (ex.: `3º trimestre de 2025`). Não substituir nem eliminar a escolha existente.
2. **Período personalizado:** disponibilizar item `Selecionar datas` ou `Período personalizado`; ao escolher, abrir calendário para selecionar **data inicial e data final**. O exemplo ilustrativo mostra uma faixa de dias escolhida no calendário.
3. **Representação após aplicar:** o seletor deve exibir o período escolhido, por exemplo `20/10/2026 a 29/10/2026`, em vez de um trimestre que não corresponda ao recorte.
4. **Retorno ao trimestre:** mudar novamente para opção predefinida deve restaurar aquele período sem preservar rótulo de seleção personalizada.

## 3. Interação do calendário

- Seleção em duas etapas: primeiro clique define início, segundo clique define fim; destacar visualmente os dois extremos e todos os dias inclusos na faixa.
- O mesmo dia pode ser usado como início e fim. Se o usuário escolher fim anterior ao início, adotar uma regra consistente (ordenar as datas ou reiniciar o intervalo), com comunicação acessível.
- Exibir mês e ano, navegação entre meses, dias da semana em português e campos legíveis para data inicial/final no formato **dd/mm/aaaa**.
- Permitir confirmar (**Aplicar**) somente quando a seleção estiver válida; oferecer **Cancelar** sem alterar o filtro aplicado e opção de limpar/redefinir conforme UX.
- Disponibilizar interação por teclado, foco visível, labels para leitor de tela, estados selecionados anunciáveis, tamanho de alvo apropriado e responsividade mobile.
- Respeitar datas locais de calendário, sem deslocamento involuntário por timezone/UTC. Não impor retroativamente limite temporal, janela máxima ou histórico permitido sem contrato futuro.
- Quando houver dados indisponíveis no recorte escolhido, preservar `NO_DATA`, `INSUFFICIENT_DATA` ou demais estados; nunca preencher com números inventados como se fossem observações.

## 4. Aplicação transversal e comparação

- O filtro de período deve ter uma **fonte de estado visual compartilhada**, propagada de maneira consistente às nove áreas e aos seus cards, séries, tabelas e gráficos que realmente dependam de tempo.
- Leituras intrinsecamente estáticas ou sem granularidade definida devem indicar indisponibilidade de recorte de forma útil, sem fabricar séries ou resultados.
- Preservar `Área de atuação` e demais filtros existentes; o período apenas **restringe** a seleção, nunca expande escopo de acesso ou exposição.
- Preservar a opção `Comparar com período anterior`. Para intervalo personalizado, a demonstração pode comparar com a **janela imediatamente anterior de mesma duração em dias corridos**, explicitando os dois intervalos. Para trimestres, manter a semântica já existente quando equivalente e legitimamente comparável.
- Nunca misturar coortes, populações, denominadores, tipos de evento ou critérios de evidência só para viabilizar comparação. Se não houver janela/contrato comparável, exibir estado seguro ou desabilitar a comparação naquele contexto.
- Uma mudança de Organização/unidade/papel, quando aplicável, não pode transportar dados ou filtros que ampliem o escopo autorizado; implementação operacional futura exige enforcement no serving.

## 5. Identidade visual e comportamento de componentes

- Consumir o mesmo **design system** de `Jornada de Organizações e Coletivos` para Organização: fundo `#FFFFFF`, foco/seleção Purple 4 `#5D34A9`, superfícies selecionadas Purple 2 `#EDE9FE`, divisórias Gray 3 `#E3E3E3`, texto Black 2 `#232323`; apenas os 30 tokens oficiais para UI.
- Calendário, seletor e botões devem adotar o mesmo padrão de bordas, espessura, raios, ícones e densidade visual do restante da experiência de Organização; não adicionar identidade Pink de Coletivo.
- Aplicar hierarquia Goldplay conforme a autoridade tipográfica vigente, sem inventar estilos canônicos.
- Apresentar datas, mês e dias da semana em português; mensagem de interface concisa, sem exposição de termos documentais, IDs ou estados internos de governança.

## 6. Limites de prototipação e maturidade

- Uma representação interativa no projeto Replit do Dashboard Organização pode operar apenas sobre dados **totalmente sintéticos** e estado local de demonstração, sem API, banco real, autenticação real ou exportação.
- A interface visual não valida o contrato de período de nenhum KPI. O Anexo C continua como autoridade para janela, coorte, granularidade, fórmula, disclosure, freshness e suficiência antes de consumo operacional.
- Os **39 KPIs** permanecem `proposed / NOT_READY`; os **14 refinamentos** permanecem não canônicos; os gates `G-ORG-01..07` permanecem inalterados.
- Não usar filtros de datas/segmentos para revelar dados protegidos ou reconstruir valores suprimidos por diferença entre recortes.
- Nenhuma alteração neste documento autoriza produto em produção, dados reais, serviços, API, RBAC ou transição canônica.

## 7. Critérios de aceite demonstrativo

- [ ] Trimestres continuam disponíveis.
- [ ] Existe entrada clara para período personalizado, com seleção de início/fim.
- [ ] Intervalo aplicado é inclusivo, formatado dd/mm/aaaa e visível no controle.
- [ ] Cancelar não altera o período vigente; Aplicar exige intervalo válido.
- [ ] Alterar período atualiza as leituras temporais disponíveis nas nove áreas, sem resultados ficticiamente derivados de números fixos.
- [ ] Comparação com período anterior respeita janela temporal equivalente e informa período comparado.
- [ ] Filtros complementares e estados de dados permanecem coerentes.
- [ ] Calendário é acessível via teclado/leitor de tela e adequado a desktop/mobile.
- [ ] Cores, tipografia, contornos e controles permanecem consistentes com a Jornada de Organizações.
- [ ] Sem conexão com dados reais nem promoção de KPI/gates.

**Saída documental:** `DRAFT / NON-NORMATIVE / VISUAL PROTOTYPE INTERACTION CANDIDATE`. O ato de merge, se ocorrer, apenas integra este contrato candidato ao GKR.
