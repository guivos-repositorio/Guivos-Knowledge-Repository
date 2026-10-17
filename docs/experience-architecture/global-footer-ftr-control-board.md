---
id: GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
title: Rodapé Global — Quadro de Controle de Gates FTR-01 a FTR-08
status: proposed
version: 0.1.11
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
| **FTR-01** — Arquitetura e módulos | R01–R06/R05A reconciliados; D1 aceita posição do Mapa após oito destinos; D2 aceito padrão `full` responsivo, com `compact` contextual e `minimal` excepcional | D4: política delimitada aprovada para Mapa demonstrativo sem link no protótipo e sem link fictício em produção; D3 (hierarquia), D5 (exceções por rota) e D6 (app/QR) permanecem pendentes, conforme [arquitetura candidata](global-footer-surface-candidate.md) | Decisão de produto/experiência com revisão Brand/Design | **PARTIAL_NOT_CLOSED** |
| **FTR-02** — Destinos reais | [Inventário editorial FTR-02](global-footer-ftr02-destination-inventory.md) registrado: 9 explorações (incluindo Mapa), 4 institucionais, 5 ajudas, 2 jurídicos inferiores e 6 ícones sociais; FTR-02/D1: `guivos.com` como domínio global principal e `guivos.us` como opção por país; FTR-02/D2: fundador confirmou registro dos dois domínios em 16/10/2026 (inventário v0.1.3); DNS, HTTPS, rotas e destinos individuais ainda não verificados | Inventário por link: rótulo, URL, dono, disponibilidade e resultado de teste; política de ausência de destino, sobretudo Mapa | Responsável pelo destino/produto e navegação | **DOMAIN_ROLE_AND_REGISTRATION_CONFIRMED / DESTINATIONS_NOT_VERIFIED / GATE_OPEN** |
| **FTR-03** — Coerência das oito Homes | 8/8 Masters reconciliados documentalmente; inspeção secundária do Replit relata 2 Homes com rota, divergências visuais/estruturais e seis sem Home própria naquele app | Capturas primárias versionadas da área final em desktop/mobile, por Home; avaliação Brand/Design, divergências e desfecho 8/8; não contar fallback nem relato de agente como homologação | Brand/Design e responsável pela Home | **OPEN_WITH_REPORTED_NONCONFORMITIES** |
| **FTR-04** — Legal/Privacidade | [Matriz de revisão FTR-04](global-footer-ftr04-legal-privacy-review.md) documentada: identificação, links legais, canais, novidades e eventual app/QR | Validar dados institucionais, URLs, finalidade/base legal, consentimento quando aplicável, política, canais e fluxo de novidades | Legal/Privacidade e donos dos canais | **MATRIX_DOCUMENTED / LEGAL_PRIVACY_REVIEW_NOT_ADJUDICATED** |
| **FTR-05** — Responsividade e acessibilidade | [Matriz FTR-05](global-footer-ftr05-responsive-accessibility-matrix.md) documentada: variantes D2, 16 ensaios candidatos, evidências por Home e exceções por rota; referência desktop aprovada | Implementar/prototipar estados reais e testar teclado, leitor de tela, foco, contraste, zoom, mobile e tablet | Design/Acessibilidade e QA | **MATRIX_DOCUMENTED / TESTS_NOT_EXECUTED** |
| **FTR-06** — Implementação | [Contrato FTR-06](global-footer-ftr06-implementation-integrity.md) documentado: 12 evidências de integridade, cobertura das oito Homes, destinos e prevenção de duplicidades; auditoria Replit secundária | Demonstrar componente coerente com conteúdo validado e cobertura das superfícies elegíveis sem duplicações, com evidência de código/versão | Engenharia/Produto | **CONTRACT_DOCUMENTED / IMPLEMENTATION_NOT_EVIDENCED** |
| **FTR-07** — Testes funcionais | [Protocolo FTR-07](global-footer-ftr07-functional-regression-protocol.md) documentado: 18 casos de testes e regressão, nenhum executado | Executar testes rastreáveis de links, estados, formulário, responsividade, regressão, acessibilidade e falhas | QA/Engenharia | **PROTOCOL_DOCUMENTED / TESTS_NOT_EXECUTED** |
| **FTR-08** — Publicação | [Protocolo FTR-08](global-footer-ftr08-release-verification.md) documentado: fases R0-R8, 13 provas de release e Go/No-go; sem publicação comprovada | Aprovação expressa de publicação, deploy real, URLs e verificação pós-publicação | Responsável pelo release/produto | **RELEASE_PROTOCOL_DOCUMENTED / PUBLICATION_NOT_EVIDENCED** |

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

## 7. Reconciliação FTR-02/D2 — registro dos domínios (16/10/2026)

A confirmação expressa do fundador de que `guivos.com` e `guivos.us` estão registrados com a Guivos foi documentada no [Inventário editorial FTR-02 v0.1.3](global-footer-ftr02-destination-inventory.md), PR #689 `MERGED`. Isto satisfaz a **confirmação institucional declaratória do registro**, sem equipará-la a documentação de registrador ou prova de resolução DNS. A deliberação FTR-02/D1 do papel dos domínios permanece vigente (PR #687).

**Situação:** `FTR-02/D1 = DOMAIN_ROLE_ACCEPTED_SCOPED`; `FTR-02/D2 = DOMAIN_REGISTRATION_CONFIRMED_BY_FOUNDER`; `FTR-02 = DOMAIN_ROLE_AND_REGISTRATION_CONFIRMED / DESTINATIONS_NOT_VERIFIED / GATE_OPEN`. Nenhum dos destinos editoriais do rodapé foi homologado como funcional; `VERIFIED_FOR_PRODUCTION = 0` na matriz de links até verificação individual. A próxima evidência requerida é o mapeamento de URLs reais por destino, testadas e autorizadas; dados técnicos de DNS/hospedagem só quando forem necessários para validação específica. Não solicitar novamente comprovação declaratória de que os domínios estão registrados.

O gate FTR-01 permanece `PARTIAL_NOT_CLOSED`, com D3..D6 sob análise documental após a PR #688 `MERGED`. Nenhuma implantação ou alteração no Replit decorre desta atualização.

## 8. Deliberação FTR-01/D4 — estado do Mapa sem URL (16/10/2026)

O fundador aceitou a política delimitada registrada em [Arquitetura Candidata v0.2.11 §6.7](global-footer-surface-candidate.md): demonstração inativa em protótipo, **nenhum link clicável fictício em produção** e ativação futura somente após destino real homologado. O aceite não adjudica a apresentação visual final de um item sem destino, nem substitui a validação FTR-02.

**Situação:** `FTR-01/D4 = UNAVAILABLE_DESTINATION_POLICY_ACCEPTED_SCOPED`; `FTR-01/D3 = PROPOSED_NOT_ACCEPTED`; `FTR-01/D5..D6 = DECISION_REQUIRED`; `FTR-01 = PARTIAL_NOT_CLOSED`. Sem mudanças técnicas ou alterações no Replit.
