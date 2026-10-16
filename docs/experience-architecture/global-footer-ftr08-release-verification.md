---
id: GKR-UX-GLOBAL-FOOTER-FTR08-001
title: Rodapé Global — Protocolo de Publicação e Verificação Pós-Implantação FTR-08
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-release-and-post-deployment-evidence
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
  - GKR-UX-GLOBAL-FOOTER-FTR02-001
  - GKR-UX-GLOBAL-FOOTER-FTR04-001
  - GKR-UX-GLOBAL-FOOTER-FTR05-001
  - GKR-UX-GLOBAL-FOOTER-FTR06-001
  - GKR-UX-GLOBAL-FOOTER-FTR07-001
---

# Rodapé Global — Protocolo FTR-08 de Publicação e Verificação Pós-Implantação

## 1. Propósito, autoridade e situação inicial

**Protocolo de governança de publicação, não ordem de implantação.** O FTR-08 somente poderá atestar um release real do rodapé se houver decisão competente, artefato implantado e verificação independente dos destinos públicos. A publicação no GKR de documentação ou merges de PRs documentais não representam liberação da interface Guivos.

Precedência:
- [Rodapé Institucional Oficial](global-institutional-footer.md) v1.0.0: conteúdo e referência visual normativa.
- [Arquitetura Candidata](global-footer-surface-candidate.md) v0.2.8: decisões FTR-01/D1/D2 e limites de aplicação, sem obrigação de implementar na presente etapa.
- [Quadro de Controle FTR](global-footer-ftr-control-board.md): acompanhamento conjunto.
- [Inventário de Destinos FTR-02](global-footer-ftr02-destination-inventory.md): comprovação de links e contas.
- [Matriz Jurídica e Privacidade FTR-04](global-footer-ftr04-legal-privacy-review.md): matérias institucionais, dados e consentimento.
- [Matriz Responsiva e Acessibilidade FTR-05](global-footer-ftr05-responsive-accessibility-matrix.md): evidências reais de comportamento adaptativo.
- [Contrato de Integridade FTR-06](global-footer-ftr06-implementation-integrity.md): componente, composição e versão.
- [Protocolo de Testes FTR-07](global-footer-ftr07-functional-regression-protocol.md): execução verificável dos cenários.

**Estado atual:** `FTR-08 = RELEASE_PROTOCOL_DOCUMENTED / PUBLICATION_NOT_EVIDENCED / GATE_OPEN`. Não existe, por esta documentação, aceite de release ou publicação.

## 2. Modelo de decisão e fases

| Fase | Condição verificável | Quem revisa (função, sem pessoas nomeadas) | Evidência de conclusão |
|---|---|---|---|
| R0 — Escopo de release | Definir superfícies/rotas incluídas e excluídas, variante e diferença frente ao conteúdo aprovado, com justificativas | Produto / Arquitetura de Experiência | Escopo e baseline aprovados, datados |
| R1 — Prontidão editorial e de destinos | Confirmar textos/identidade oficiais, Mapa, links reais, contas e comportamento de indisponibilidade | Brand / Produto / responsáveis pelos destinos | Versões do GKR, FTR-01/02/03 e tabela de URLs |
| R2 — Prontidão jurídica e privacidade | Validar identificação institucional, termos, privacidade, canais e integração de novidades se houver | Jurídico / Privacidade | Decisões FTR-04 com fonte primária |
| R3 — Prontidão visual, técnica e acessível | Obter evidências FTR-03/05/06 por Home e variante efetiva | Design / Acessibilidade / Engenharia | Relatórios, capturas primárias e versão do componente |
| R4 — QA e regressão | Executar cenários relevantes de FTR-07, classificar falhas e bloquear defeitos críticos sem exceção aprovada | QA / Produto | Resultados com PASS/FAIL/BLOCKED e decisão documentada |
| R5 — Go/No-go formal | Decidir de maneira explícita com base nos gates e riscos restantes; nenhum merge do GKR substitui essa decisão | Autoridade de release / Produto | Registro `GO` ou `NO_GO` com data e escopo |
| R6 — Implantação autorizada | Publicar somente release autorizado; registrar build, commit, ambiente, domínio e procedimento de retorno | Engenharia / Operação de Release | Identificador do deploy e evidência técnica |
| R7 — Verificação externa | Abrir rotas públicas reais, validar conteúdo e links de fora do ambiente de desenvolvimento, comparar com baseline e registrar erros | QA / Operação / Design | Capturas e resultados por URL/dispositivo com data |
| R8 — Monitoramento e encerramento | Definir responsável por incidentes, verificação de serviços, correções e rollback; encerrar apenas após critérios satisfeitos | Produto / Engenharia / Operação | Aceite pós-implantação, incidentes tratados e trilha de auditoria |

As fases são **propostas para governança**, não autorização de publicação nem novos gates globalmente adjudicados.

## 3. Checklist de evidências para um release

| ID | Item obrigatório | Resultado atual |
|---|---|---|
| FTR08-P01 | Escopo da versão, lista de oito Homes cobertas e exceções aprovadas quando aplicáveis | NOT_EVIDENCED |
| FTR08-P02 | Referência oficial, copy, assinatura e variantes reconciliadas, com aprovação de divergências | NOT_EVIDENCED |
| FTR08-P03 | URLs canônicas, links legais, redes oficiais e destino do Mapa verificados ou explicitamente bloqueados | BLOCKED_BY_FTR02 |
| FTR08-P04 | Revisão jurídica e privacidade concluída para as funções efetivamente oferecidas | BLOCKED_BY_FTR04 |
| FTR08-P05 | Evidência primária visual por Home e viewport, com aceites Brand/Design | BLOCKED_BY_FTR03_FTR05 |
| FTR08-P06 | Artefato do componente global identificado, testável e sem duplicações indevidas | BLOCKED_BY_FTR06 |
| FTR08-P07 | Relatório de execução dos casos críticos e regressão, com defeitos tratados | BLOCKED_BY_FTR07 |
| FTR08-P08 | Registro explícito de decisão Go/No-go para versão/escopo, com autoridade identificada | NOT_AUTHORIZED |
| FTR08-P09 | Commit/build, release ID, ambiente público e domínio canônico com titularidade verificada | NOT_EVIDENCED |
| FTR08-P10 | Evidência de implantação e teste de abertura externa das rotas incluídas | NOT_EVIDENCED |
| FTR08-P11 | Testes pós-deploy de navegação, privacidade, novidades, status de links e acessibilidade relevante | NOT_EVIDENCED |
| FTR08-P12 | Plano de rollback e responsabilidades de incidente/continuidade | NOT_EVIDENCED |
| FTR08-P13 | Registro de aceite pós-implantação com data, resultados, exceções e divergências | NOT_EVIDENCED |

Nenhuma linha se converte em `PASS` por declaração geral de prontidão, existência de build local, aprovação de design ou sucesso dos workflows de documentação.

## 4. Evidência pública versus ambiente de desenvolvimento

O registro FTR-03 na arquitetura candidata reportou que os previews internos do aplicativo Replit permitiam inspeções parciais, enquanto endereços públicos testados não renderizavam as duas Homes identificadas. Essa observação **não é prova de causa, nem prova de implantação corrigida**. A publicação somente pode ser comprovada por URL real, versão e comportamento observados em acesso público apropriado, com evidência preservada.

Não presumir que o repositório documental GKR e os domínios de produto compartilham estado de deploy. O site publicado do GKR comprova **documentação**, não experiência do produto.

## 5. Registro mínimo de Go/No-go

Para cada proposta de release, preencher:

- **Versão e superfícies**: artefato, SHA, ambientes, oito Homes elegíveis e exclusões justificadas.
- **Referências**: IDs/versões da autoridade visual, arquitetural e contratos FTR relacionados.
- **Gates**: decisões de FTR-01 a FTR-07 e evidências, com dependências abertas explícitas.
- **Riscos e limitações**: falhas, indisponibilidades, impacto de dados e experiência da pessoa.
- **Decisão**: `GO`, `NO_GO` ou `DEFERRED`, autoridade competente, data, alcance, condições e validade.
- **Operação**: executor, plano de retorno, verificações externas e responsáveis pelo pós-implantação.

**Sem decisão registrada, o estado é `NO_AUTHORIZED_RELEASE`**. Não executar deploy por inferência a partir deste protocolo.

## 6. Critério de encerramento do FTR-08

Encerrar somente se: decisão Go aplicável existir; a versão exata tiver sido implantada em ambiente público aprovado; as rotas incluídas apresentarem o rodapé correto sem duplicação; links e informações legais funcionarem conforme seus contratos; o fluxo de novidades não simular processamento; acessibilidade e regressão relevantes tiverem resultado verificável; e o aceite pós-deploy for documentado.

A inexistência de implantação comprovada mantém `PUBLICATION_NOT_EVIDENCED` mesmo quando todos os checklists documentais estiverem completos.

**Fronteira:** nenhuma execução, deploy, QR oficial, ligação de app ou mudança no Replit nesta etapa de GKR.
