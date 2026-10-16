---
id: GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
title: Rodapé Global — Quadro de Controle de Gates FTR-01 a FTR-08
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-governance-traceability
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-HOME-MASTER-001
---

# Rodapé Global — Quadro de Controle FTR-01 a FTR-08

## 1. Finalidade e ordem de autoridade

**Painel de consulta e rastreabilidade, não ato de homologação.** Consolida decisões, evidências e impedimentos existentes até 16/10/2026 para impedir que merge de documentação, design aprovado, protótipo e interface em produção sejam confundidos.

Ler primeiro:
1. [Rodapé Institucional Global — Referência Validada](global-institutional-footer.md): `GKR-UX-GLOBAL-FOOTER-001 v1.0.0`, `normative: true`, referência visual/verbal aprovada em 14/10/2026.
2. [Rodapé Global — Arquitetura Candidata e Gates FTR](global-footer-surface-candidate.md): `GKR-UX-GLOBAL-FOOTER-SURFACE-001 v0.2.8`, `status: proposed`, `normative: false`, escopo lógico, decisões FTR-01/D1/D2 e auditoria exploratória FTR-03.
3. [Home Pública — Pessoa](public-home-master-document.md), §31: obrigação arquitetural de `Mapa do Ecossistema`, **sem** página/destino automaticamente definidos.

**Precedência:** o presente quadro não altera cópia, design, assinatura de marca, condições legais, gates nem hierarquia de autoridades. Em divergência, prevalecem os respectivos documentos de autoridade.

## 2. Estado executivo por gate

| Gate | Evidência documental atual | Pendência material / comprovação de encerramento | Responsabilidade de validação (função, não pessoa designada) | Estado |
|---|---|---|---|---|
| **FTR-01** — Arquitetura e módulos | R01–R06/R05A reconciliados; D1 aceita posição do Mapa após oito destinos; D2 aceito padrão `full` responsivo, com `compact` contextual e `minimal` excepcional | Revisão da hierarquia e registro de exceções por superfície, sem omitir `Receba novidades` nem criar URLs | Decisão de produto/experiência com revisão Brand/Design | **PARTIAL_NOT_CLOSED** |
| **FTR-02** — Destinos reais | Lista editorial e Mapa contratados na arquitetura, sem rotas comprovadas | Inventário por link: rótulo, URL, dono, disponibilidade e resultado de teste; política de ausência de destino, sobretudo Mapa | Responsável pelo destino/produto e navegação | **NOT_VERIFIED** |
| **FTR-03** — Coerência das oito Homes | 8/8 Masters reconciliados documentalmente; inspeção secundária do Replit relata 2 Homes com rota, divergências visuais/estruturais e seis sem Home própria naquele app | Capturas primárias versionadas da área final em desktop/mobile, por Home; avaliação Brand/Design, divergências e desfecho 8/8; não contar fallback nem relato de agente como homologação | Brand/Design e responsável pela Home | **OPEN_WITH_REPORTED_NONCONFORMITIES** |
| **FTR-04** — Legal/Privacidade | Textos jurídicos e captura voluntária previstos na referência | Validar dados institucionais, URLs, finalidade/base legal, consentimento quando aplicável, política, canais e fluxo de novidades | Legal/Privacidade e donos dos canais | **NOT_VERIFIED** |
| **FTR-05** — Responsividade e acessibilidade | Variantes de arquitetura D2 aceitas em escopo limitado; referência desktop aprovada | Implementar/prototipar estados reais e testar teclado, leitor de tela, foco, contraste, zoom, mobile e tablet | Design/Acessibilidade e QA | **NOT_TESTED** |
| **FTR-06** — Implementação | Componente compartilhado é proposta; auditoria Replit reporta `FlowFooter` exploratório e rodapé local adicional em O/C | Demonstrar componente coerente com conteúdo validado e cobertura das superfícies elegíveis sem duplicações, com evidência de código/versão | Engenharia/Produto | **NOT_IMPLEMENTATION_EVIDENCED** |
| **FTR-07** — Testes funcionais | Critérios documentados; agente Replit não encontrou execução FTR-03 específica | Executar testes rastreáveis de links, estados, formulário, responsividade, regressão, acessibilidade e falhas | QA/Engenharia | **NOT_EXECUTED** |
| **FTR-08** — Publicação | Nenhuma prova de deploy completo do rodapé; rotas públicas consultadas no Replit não mostraram as duas Homes no relato | Aprovação expressa de publicação, deploy real, URLs e verificação pós-publicação | Responsável pelo release/produto | **NOT_PUBLISHED_EVIDENCED** |

**Não há gate FTR-01..08 integralmente encerrado ou homologado por este quadro.** Os valores são rótulos descritivos de rastreabilidade, não IDs novos em registries globais. A ausência de evidência neste exame não prova inexistência em outras plataformas.

## 3. Decisões arquiteturais já registradas

- **FTR-01/D1 — POSITION_ACCEPTED:** `Mapa do Ecossistema` ao final de `Explore o ecossistema`, após os oito destinos já aprovados. Não significa que o link tem destino ou está ativo.
- **FTR-01/D2 — ARCHITECTURE_VARIANTS_ACCEPTED_SCOPED:** `full` responsivo como padrão das oito Homes; `compact` em páginas internas públicas justificadas; `minimal` somente em contextos sensíveis com contrato próprio. Não autoriza supressão de conteúdo, breakpoint arbitrário nem homologação de mobile.
- **Referência visual:** textos, paleta e composição da referência institucional de 14/10 permanecem válidos. Um acesso/QR do app surgido em iterações posteriores exige evidência visual identificada, URL/QR oficiais e decisão separada.
- **Separação de autoridade:** `Possibility, lived.` é assinatura global; `Descubra. Viva. Evolua.` é assinatura de jornada do rodapé.

## 4. Evidência disponível e qualidade

| Fonte | O que sustenta | O que **não** comprova |
|---|---|---|
| `GKR-UX-GLOBAL-FOOTER-001 v1.0.0` | Conteúdo e referência visual aprovados em 14/10 | Interface funcionando, mobile, URLs, consentimento, QR ou deploy |
| PRs #664, #669, #670, #671, #672, #673 | Reconciliação de arquitetura e decisões de posição/variantes na `main` | Execução de FTR-02..08 |
| PR #674, auditoria Replit registrada em v0.2.8 | Relato secundário de código e preview: 2 Homes com rotas identificadas, rodapé divergente, 6 Homes sem rota própria naquele aplicativo | Capturas primárias anexas no GKR, prova visual 8/8 ou causa da falha nas rotas públicas |
| PR #675 | Acesso distinto no MENU a referência oficial e arquitetura candidata | Promoção normativa ou entrega de produto |

## 5. Ordem de trabalho para conclusão **somente no GKR**

1. Consolidar o inventário de links/destinos FTR-02, com `NOT_VERIFIED` onde não houver fonte; **não criar URLs**.
2. Separar explicitamente responsabilidades institucionais de Legal/Privacidade FTR-04 e comprovação futura de implementação/testes FTR-05..08; **não nomear aprovadores individuais sem designação**.
3. Catalogar, quando disponíveis, evidências visuais primárias versionadas das oito Homes no FTR-03 e registrar as divergências sem atribuir aprovação tácita.
4. Conservar o documento e o MENU coerentes com a autoridade validada; todo avanço deverá apontar evidência, decisão competente, versão e data antes de promover estado.

**Fronteira explícita:** não modificar Replit, criar QR, anunciar lojas, ativar links, simular inscrição ou afirmar produção nesta fase documental. A implementação dependerá de deliberação própria após o GKR estar consistente.

## 6. Critério de atualização do painel

Cada atualização deve registrar: `gate`, `objeto/rota`, `fonte verificável`, `versão/data`, `responsável funcional`, `decisão`, `pendência` e `próxima condição de aceite`. Ausência de fonte mantém estado anterior; documentação mergeada **não** é homologação de execução.
