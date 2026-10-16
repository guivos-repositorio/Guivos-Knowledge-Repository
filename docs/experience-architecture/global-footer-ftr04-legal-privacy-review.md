---
id: GKR-UX-GLOBAL-FOOTER-FTR04-001
title: Rodapé Global — Matriz de Revisão Jurídica e Privacidade FTR-04
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-legal-privacy-evidence
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
  - GKR-UX-GLOBAL-FOOTER-FTR02-001
---

# Rodapé Global — Revisão Jurídica e Privacidade FTR-04

## 1. Finalidade, competência e limites

**Instrumento de conferência, não parecer jurídico nem aprovação regulatória.** Isola as afirmações e controles do rodapé que precisam de análise de Legal/Privacidade e confirmação de conteúdo, canais e comportamentos efetivos antes de publicação.

Referências que não podem ser substituídas:
- [Rodapé Institucional Global — Referência Validada](global-institutional-footer.md) v1.0.0, `normative: true`: preserva a decisão visual e textual do fundador de 14/10/2026.
- [Rodapé Global — Arquitetura Candidata](global-footer-surface-candidate.md) v0.2.8: módulos, D1/D2 e limites de implementação.
- [Quadro de Controle FTR](global-footer-ftr-control-board.md): posição e evidências dos oito gates.
- [Inventário FTR-02](global-footer-ftr02-destination-inventory.md): distingue rótulos visuais de destinos públicos verificados.

**Não se infere** conformidade legal do uso de uma frase aprovada, da existência de documento no GKR, da referência rasterizada ou de aprovação de Design. Responsabilidades abaixo são **funções de revisão**, não nomeação de pessoas.

## 2. Matriz de decisões e provas exigidas

| Item do rodapé | Fonte atual | Verificação necessária antes de declarar aprovado | Função competente | Estado |
|---|---|---|---|---|
| Identificação institucional na faixa inferior | Texto factual exibido na referência visual validada | Confirmar nome empresarial, identificação registral, atualidade, pertinência à entidade responsável pela experiência e forma adequada de publicação, sem transcrever novos dados neste instrumento | Jurídico / Institucional | NOT_VERIFIED |
| Uso da marca e do símbolo `®` | Referência visual validada e autoridades de marca | Conferir aplicação autorizada do símbolo e não estender presunção de proteção à assinatura verbal | Marca / Jurídico | NOT_VERIFIED |
| Direitos reservados / informações corporativas | Copy visual aprovado | Conferir formulação jurídica, abrangência, ano quando utilizado e vínculo à entidade correta | Jurídico | NOT_VERIFIED |
| Política de Privacidade | Link previsto no grupo Ajuda e na faixa inferior | URL canônica, versão publicada, responsável, data, conteúdo adequado à operação e correspondência com tratamentos efetivos | Privacidade / Jurídico | DESTINATION_NOT_VERIFIED |
| Termos de Uso | Link previsto no grupo Ajuda e na faixa inferior | URL canônica, versão aplicável, escopo de uso da plataforma e disponibilidade efetiva | Jurídico / Produto | DESTINATION_NOT_VERIFIED |
| Acessibilidade | Item previsto no grupo Ajuda | Canal ou página real, texto verificável, mecanismo para solicitações/feedback e compatibilidade com obrigações aplicáveis | Acessibilidade / Jurídico | DESTINATION_NOT_VERIFIED |
| Fale conosco e Central de Ajuda | Itens do grupo Ajuda | Titularidade dos canais, capacidade de atendimento, finalidade informada e proteção de dados recebidos | Atendimento / Privacidade | DESTINATION_NOT_VERIFIED |
| Receba novidades: finalidade | Bloco e descrição visual aprovados | Definir finalidade e natureza das comunicações, quem envia e quais dados serão usados; linguagem compreensível antes da submissão | Privacidade / Produto | PURPOSE_NOT_APPROVED |
| Receba novidades: base legal/consentimento | Campo de e-mail e botão na referência visual | Avaliar e documentar base legal cabível conforme fluxo real; mecanismo de manifestação quando necessário, sem presumir consentimento apenas pelo campo | Jurídico / Privacidade | LEGAL_BASIS_NOT_ADJUDICATED |
| Receba novidades: ciclo de dados | Contrato de integridade da referência oficial | Destino dos dados, controles de acesso, retenção, atendimento de direitos, inscrição e descadastramento, prevenção de coleta simulada | Privacidade / Engenharia | FLOW_NOT_VERIFIED |
| Receba novidades: estados de interface | Referência visual sem prova de execução | Validar foco, erro, feedback de sucesso real, inscrição duplicada e privacidade nas respostas | UX / Privacidade / QA | NOT_TESTED |
| Redes sociais e canais externos | Ícones da referência oficial | Confirmar titularidade, URLs reais e sinalização adequada da saída para terceiros sem alegar responsabilidade por ambientes externos | Comunicação / Privacidade | OFFICIAL_ACCOUNT_NOT_VERIFIED |
| Obter o app e QR (se incorporados depois) | Menção a possível iteração posterior, **não** incorporada automaticamente à referência normativa de 14/10 | Evidência visual oficial posterior, destino e URL/QR reais, alegações de disponibilidade verificadas, eventual aviso de loja/terceiro | Produto / Marca / Jurídico | OUT_OF_BASELINE_PENDING_EVIDENCE |
| Idioma, mercado e região | Possibilidade arquitetural, não funcionamento comprovado | Conferir jurisdição/mercado atendido e adequação de informações legais somente se o controle realmente existir | Jurídico / Produto | NOT_IMPLEMENTED_EVIDENCED |

**Critério geral:** texto juridicamente correto no documento não comprova fluxo de dados, acessibilidade, publicação nem disponibilidade; isso exige provas por tipo de gate FTR-02, FTR-05, FTR-06, FTR-07 e FTR-08.

## 3. Evidências mínimas para uma decisão FTR-04

Registrar para cada linha: (1) objeto, (2) regra ou competência aplicável identificada por responsável, (3) evidência documental primária e versão, (4) URL publicada quando pertinente, (5) fluxo efetivamente existente, (6) exame da função competente com data e resultado, (7) pendências e medidas de correção, (8) vínculo com FTR-02/05/06/07/08.

Um link com rótulo **Privacidade**, **Termos** ou **Acessibilidade**, sem destino verificado, não passa nesse critério. Um ícone de canal social ou um formulário visual não demonstra serviço ativo, dados armazenados nem consentimento válido.

### Decisão de ausência de funcionalidade

- Durante documentação/prototipação, descrever o recurso como não operacional sem simulá-lo.
- Para produção, não habilitar envio sem fluxo real e revisão de privacidade; não indicar inscrição concluída sem confirmação verificável.
- Para links jurídicos, não apresentar atalhos falsos, URLs vazias, caminhos genéricos ou encaminhamento ao GKR como substituto presumido de páginas públicas próprias.
- Preservar a arquitetura editorial da referência de 14/10; qualquer exclusão ou reescrita de elemento validado exige decisão de autoridade própria, não pode ser inferida da ausência momentânea de destino.

## 4. Fronteiras dos gates

`FTR-02` prova destinos e URLs; `FTR-04` prova suficiência da revisão jurídica e de privacidade; `FTR-05` comprova acessibilidade e responsividade; `FTR-06` requer implantação; `FTR-07` requer testes de comportamento; `FTR-08` requer aprovação e deploy verificável. Aprovar um desses gates **não aprova os demais**.

## 5. Estado e próximo ato verificável

`FTR-04 = MATRIX_DOCUMENTED / LEGAL_PRIVACY_REVIEW_NOT_ADJUDICATED / GATE_OPEN`.

Não há, neste exame, parecer jurídico formal anexado, mapa de tratamento de dados aprovado, destinos legais verificados ou comprovação do funcionamento do formulário de novidades. O quadro estabelece **o que precisa ser examinado**, não quais soluções jurídicas devem ser adotadas.

**Próxima ação admissível no GKR:** anexar evidências e decisões dos responsáveis funcionais por objeto, sem promoção automática de status, sem modificação de Replit, QR, URLs ou serviços.
