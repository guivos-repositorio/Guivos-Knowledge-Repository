---
id: GKR-CANON-MATRIX-UXA-030
title: Adendo à Matriz de Consolidação Canônica — Estado do Mapa sem Resultados
status: active
version: 0.1.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-STATE-001
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
related:
  - M7.31
normative: true
---

# Adendo à Matriz de Consolidação Canônica — Estado do Mapa sem Resultados

## 1. Finalidade

Este adendo registra a consolidação canônica do primeiro wireframe específico do Mapa de Oportunidades para uma consulta concluída sem resultados correspondentes.

## 2. Decisão consolidada

| Dimensão | Decisão canônica |
|---|---|
| Natureza | estado representa zero correspondências da consulta atual, não inexistência absoluta de oportunidades |
| Condição | zero somente após consulta concluída, região definida e ausência de falha material conhecida |
| Navegação | item `Mapa` permanece selecionado; alternância `Mapa ↔ Lista` preservada |
| Contexto | `Agindo como`, modalidade geral ou personalizada e estado de localização permanecem visíveis |
| Consulta | região, busca, filtros, total consolidado e momento de atualização não são apagados |
| Mensagem | `0 resultados correspondem a esta consulta` e `Consulta concluída · nenhuma falha conhecida` |
| Recuperação | ampliar região, alterar período, revisar filtros, editar busca e desfazer alteração são ações explícitas |
| Reversibilidade | cada ajuste declara o que muda e preserva as demais dimensões compatíveis |
| Mapa e Lista | apresentam o mesmo total zero, diagnóstico e ações para a mesma consulta |
| Falha de fonte | não pode ser apresentada como zero legítimo; deve identificar limitação e permitir nova tentativa |
| Indisponibilidade | utiliza mensagem própria e preserva a consulta |
| Baixa conectividade | declara atualização limitada e não produz conclusão absoluta |
| Localização | permanece opcional; ampliar região não autoriza posição ou rastreamento |
| Personalização | zero não autoriza recomendações pessoais nem preenchimento artificial antes do gate |
| Comércio | resultados patrocinados não podem ser inseridos para evitar estado vazio |
| Seleção anterior | não é apagada silenciosamente; incompatibilidade com a nova consulta é explicada |
| Acessibilidade | total, diagnóstico e ações são textuais e não dependem do mapa carregado |

## 3. Elementos materializados

A UXA-030 demonstra:

- `Mapa de Oportunidades`;
- `Agindo como: Pessoa`;
- `Exploração geral · sem personalização`;
- `Localização desativada · posição não acessada`;
- região manual distinta da posição pessoal;
- busca explícita preservada;
- `Mapa ↔ Lista`;
- `4 filtros ativos`;
- `0 resultados correspondem a esta consulta`;
- `Consulta concluída · nenhuma falha conhecida`;
- mensagem de ausência vinculada à busca, região e filtros atuais;
- `Ampliar região`;
- `Alterar período`;
- `Revisar filtros`;
- `Editar busca`;
- `Desfazer alteração`;
- resumo do contexto preservado;
- distinção textual entre ausência de resultados e falha de fonte;
- equivalência entre Mapa e Lista.

## 4. Proteções preservadas

- nenhum filtro é removido automaticamente;
- região não é ampliada sem confirmação;
- busca não é substituída silenciosamente;
- localização não é ativada;
- personalização não é iniciada para preencher o estado;
- publicidade não substitui correspondência funcional;
- falha técnica não é ocultada como ausência de dados;
- posição pessoal não é inferida a partir da região;
- seleção anterior não é apagada sem explicação;
- dado ausente não é completado por inferência.

## 5. Limites

Este adendo não valida o estado com usuários reais, não define algoritmo de busca, cobertura de fontes de produção, tecnologia cartográfica, geocodificação, rotas, design visual, protótipo, acessibilidade técnica ou desenvolvimento.

## 6. Marco

A integração deste incremento estabelece o marco **M7.31 — Estado do Mapa sem Resultados Criado**.
