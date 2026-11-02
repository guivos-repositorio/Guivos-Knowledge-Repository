---
id: GKR-UX-HOMES-PERSON-OC-CLOSURE-20261102
title: Plano de conclusão verificável das Homes Pessoa e Organizações e Coletivos
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-02
normative: false
---

# Fechamento priorizado — Pessoa e Organizações e Coletivos

## Escopo e estado confirmado

A direção determinou priorizar a conclusão das duas Homes. O fechamento deve distinguir **documentação**, **design validado**, **implementação comprovada** e **publicação autorizada**.

| Camada | Home Pessoa | Home Organizações e Coletivos |
| --- | --- | --- |
| Documento Mestre em main | 1.0.9 — presente | 1.0.10 — presente |
| Leia Primeiro em main | 1.0.6 — presente | 1.0.6 — presente |
| Manifesto compartilhado | 7.0.57 | 7.0.57 |
| Source Lock generativo compartilhado | 2.3.19 | 2.3.19 |
| Adendos temporais incorporados | M06, M09, M10 | M03, M06, M10 |
| Design final, responsividade e acessibilidade | Evidência de aceite ainda não conferida | Evidência de aceite ainda não conferida |
| Implementação web testada | Evidência ainda não conferida | Evidência ainda não conferida |
| Publicação dos adendos | Conteúdo não localizado anteriormente no HTML de gh-pages | Conteúdo não localizado anteriormente no HTML de gh-pages |

## Portões de conclusão

### G1 — Documentação e narrativa
Confirmar que os 11 movimentos da Pessoa e os 12 de O/C seguem íntegros; manter copy, CTAs, contratos de autonomia e hierarquia de evidências. Registrar divergências entre textos e artefatos visuais. **Estado:** versões e referências integradas; revisão visual ainda necessária.

### G2 — Design UX/UI
Conferir, por Home, desktop/mobile, Hero, header, navegação, imagens, movimentos, CTAs, contraste, estados, acessibilidade, responsividade e componentes específicos. **Requer evidência verificável de protótipo/design e aceite humano**, conforme Handoff 1.7.13. Não marcar como concluído por existência de Documento Mestre.

### G3 — Implementação
Inventariar URLs/repositórios do site e evidências de build, comportamento real, testes, performance, acessibilidade e conteúdo renderizado. Não presumir que o código foi implantado.

### G4 — Publicação e consistência pública
A PR #725 propõe separar merge documental de deploy, mas o risco de transição não foi sanado administrativamente. A publicação dos adendos depende de autorização separada, após controle seguro e inspeção do build. Não acionar workflow nem escrever na gh-pages.

### G5 — Aceite final separado
Registrar aceite por Home para: conformidade documental, Design, implementação e publicação. **Não emitir conclusão integral antecipada.**

## Próxima ação de maior valor
Iniciar o inventário de evidências visuais e de implementação **somente das duas Homes**, priorizando:
- Pessoa: M06/M09/M10, Hero, M11 gráfico vivo, entrada Jornada, autonomia e privacidade.
- O/C: M03/M06/M10, M08 Mapa de Pessoas, M09 circulação de valor, CTA Participar da Guivos, diferenças Organização × Coletivo.

## Governança
A PR #725 está com os dois checks aprovados no commit `197e5690bb2ed9bc8fa636029661e047edc59d18`, mas segue **bloqueada para merge**, pois falta comprovação de neutralização do gatilho automático. Este plano não autoriza merge, deployment, alteração operacional nem declara entrega final.
