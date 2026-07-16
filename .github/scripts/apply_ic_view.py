from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Missing marker: {label}")
    return text.replace(old, new, 1)


def replace_regex(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Regex marker count for {label}: {count}")
    return updated


def commit(path: str, message: str) -> None:
    run("git", "add", path)
    run("git", "commit", "-m", message)


def update_readme() -> None:
    path = Path("README.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 40%",
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 60%",
        "README progress",
    )
    text = replace_once(
        text,
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001 e PAS-001-IC-LIFECYCLE-001, ambas em 1.0.0",
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001 e PAS-001-IC-VIEW-001, todas em 1.0.0",
        "README extensions",
    )
    marker = """- compartilhamento, revogação, propagação, retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **40%**."""
    addition = """- compartilhamento, revogação, propagação, retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

`PAS-001-IC-VIEW-001 1.0.0` consolida:

- `Central de Intervenções` como superfície principal de compreensão e controle;
- `Fila de Atenção` como recorte temporário do que pode justificar atenção atual ou próxima;
- ausência legítima de intervenções, sem preenchimento artificial por anúncios ou mensagens de engajamento;
- agrupamento e ordenação funcional sem comissão, patrocínio, clique, margem ou meta comercial;
- cartões minimizados, títulos funcionais e títulos neutros para conteúdo sensível;
- separação entre estado funcional, informação, autorização, temporalidade, entrega, resposta, atenção, fadiga, sensibilidade e operação externa;
- comportamentos visuais de pergunta, informação, sugestão, lembrete, alerta, confirmação, ação, espera, observação e silêncio;
- explicações `Por que estou vendo isto?` e `Por que agora?`;
- fonte, autoridade, validade, incerteza, importância, urgência e relações comerciais visíveis;
- histórico, busca, filtros, resposta, adiamento, silêncio, recusa, ocultação, bloqueio, contestação, correção e revogação;
- preferências de frequência, horários protegidos, canais, categorias, intensidade, resumos e controles de fadiga;
- notificações protegidas, consistência entre canais e superfícies de produto;
- acessibilidade técnica e cognitiva, linguagem proporcional e privacidade visual;
- proteção de saúde, finanças, jurídico, religião, voluntariado, coletivos e terceiros;
- falha segura, sincronização pendente, conflitos e auditoria compreensível.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **60%**."""
    text = replace_once(text, marker, addition, "README view section")
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*?\n## Product Engineering",
        """## Ponto exato de retomada

Retomar nos contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais.

Próxima entrega:

- estrutura comum e agregado funcional;
- autoridade, finalidade, proveniência e sensibilidade;
- temporalidades, correlação e causalidade funcional;
- eventos de identificação, avaliação e admissão;
- seleção de comportamento, programação e prontidão;
- apresentação, entrega e resposta;
- adiamento, silêncio, recusa e bloqueio;
- contestação, correção e revogação;
- propagação, idempotência, ordenação e concorrência;
- reconstrução, auditoria e falha segura.

## Product Engineering""",
        "README resumption",
    )
    text = text.replace(
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `40%`.",
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `60%`.",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 40% |",
        "| 07 — Intervenções Contextuais | In progress — 60% |",
    )
    text = replace_once(
        text,
        "- [Ciclo de Vida das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md)",
        "- [Ciclo de Vida das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md)\n- [Visualização e Controle das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "README link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(readme): avançar visualização de Intervenções Contextuais")


def update_home() -> None:
    path = Path("docs/index.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 40%;",
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 60%;",
    )
    text = text.replace(
        "- `PAS-001-IC-FOUNDATION-001 1.0.0` e `PAS-001-IC-LIFECYCLE-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0` e `PAS-001-IC-VIEW-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
    )
    text = text.replace(
        "Consolidar os **comportamentos funcionais da visualização e do controle da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar os **contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais**.",
    )
    text = text.replace(
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As duas extensões de Intervenções Contextuais consolidam fundamentos e ciclo de vida, incluindo decisões de manifestação, estados independentes, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência e falha segura.",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As três extensões de Intervenções Contextuais consolidam fundamentos, ciclo de vida, Central de Intervenções, Fila de Atenção, mensagens, justificativas, controles, preferências, acessibilidade, privacidade, relações comerciais e falha segura.",
    )
    text = replace_once(
        text,
        "- [Ciclo de Vida das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md)",
        "- [Ciclo de Vida das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md)\n- [Visualização e Controle das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "home link",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 40% |",
        "| 07 — Intervenções Contextuais | In progress — 60% |",
    )
    text = replace_once(
        text,
        "Retomar nos comportamentos funcionais da visualização e do controle da Capacidade 07 — Intervenções Contextuais, incluindo central de intervenções, fila de atenção, mensagens, perguntas, lembretes, alertas, justificativas, histórico, adiamento, silêncio, frequência, horários protegidos, canais, preferências, acessibilidade, privacidade, relações comerciais e consistência entre superfícies.",
        "Retomar nos contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
        "home resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(index): avançar visualização de Intervenções Contextuais")


def update_product_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.1", "version: 1.8.2", "architecture version")
    current = """A extensão normativa vigente é:

- `PAS-001-IC-FOUNDATION-001 1.0.0` — finalidade, pergunta central, singularidade, decisões possíveis, oportunidade de intervenção, silêncio, atenção, interruptibilidade, urgência, sensibilidade, fadiga, canais, autonomia, controles, relações, estados e eventos iniciais."""
    replacement = """As extensões normativas vigentes são:

- `PAS-001-IC-FOUNDATION-001 1.0.0` — finalidade, pergunta central, singularidade, decisões possíveis, oportunidade de intervenção, silêncio, atenção, interruptibilidade, urgência, sensibilidade, fadiga, canais, autonomia, controles, relações, estados e eventos iniciais.
- `PAS-001-IC-LIFECYCLE-001 1.0.0` — dimensões independentes, estados, transições, identificação, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência e falha segura.
- `PAS-001-IC-VIEW-001 1.0.0` — Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura."""
    text = replace_once(text, current, replacement, "architecture extensions")
    marker = """- retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `40%`.

O próximo bloco deverá consolidar os comportamentos funcionais da visualização e do controle das Intervenções Contextuais."""
    addition = """- retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A visualização e o controle consolidam:

- `Central de Intervenções` como superfície principal de compreensão, decisão e controle;
- `Fila de Atenção` como recorte temporal do que pode exigir atenção atual ou próxima;
- ausência legítima sem preenchimento por anúncios, recomendações artificiais ou mensagens de engajamento;
- agrupamentos e ordenação por risco, prazo, confirmação, reversibilidade, impacto e sensibilidade, sem influência comercial;
- cartões minimizados, títulos funcionais e títulos neutros;
- estados e dimensões independentes de informação, autorização, temporalidade, entrega, resposta, atenção, fadiga, sensibilidade e operação externa;
- perguntas, informações, sugestões, lembretes, alertas, confirmações, ações, espera, observação e silêncio com contratos visuais próprios;
- detalhamento progressivo e explicações `Por que estou vendo isto?` e `Por que agora?`;
- fonte, autoridade, incerteza, validade, importância, urgência e relações comerciais visíveis;
- histórico imutável, correções compensatórias, busca, filtros e controles principais;
- resposta, adiamento, silêncio, recusa, ocultação, bloqueio, contestação, correção e revogação;
- preferências de frequência, horários protegidos, canais, categorias, intensidade, resumos e fadiga;
- notificações, e-mail, canais conversacionais, calendário e superfícies de produtos com consistência de estado;
- acessibilidade técnica e cognitiva, linguagem proporcional, ambiente, dispositivo e privacidade visual;
- proteção de terceiros e de intervenções de saúde, finanças, jurídico, religião, voluntariado, institucionais, coletivas e comerciais;
- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `60%`.

O próximo bloco deverá consolidar os contratos dos eventos funcionais das Intervenções Contextuais."""
    text = replace_once(text, marker, addition, "architecture view section")
    text = text.replace(
        "415. A Capacidade 07 permanece planejada até sua primeira extensão normativa.",
        "415. A Capacidade 07 foi iniciada normativamente por sua primeira extensão.",
    )
    text = text.replace(
        "463. A Capacidade 07 está `In progress`, com progresso editorial de referência de `20%`.",
        "463. Os fundamentos de Intervenções Contextuais estão consolidados por `PAS-001-IC-FOUNDATION-001 1.0.0`.",
    )
    text = text.replace(
        "509. A Capacidade 07 está `In progress`, com progresso editorial de referência de `40%`.",
        "509. O ciclo de vida das Intervenções Contextuais está consolidado por `PAS-001-IC-LIFECYCLE-001 1.0.0`.",
    )
    rules_marker = "510. O participante permanece no controle do ciclo de vida das Intervenções Contextuais.\n\n## Documentos do domínio"
    rules = """510. O participante permanece no controle do ciclo de vida das Intervenções Contextuais.
511. Central de Intervenções não é caixa de entrada infinita.
512. Fila de Atenção não representa todas as intervenções existentes.
513. Nem toda intervenção requer atenção imediata.
514. Ausência de intervenção é estado legítimo.
515. Contagem não representa qualidade, produtividade ou evolução.
516. Ordenação funcional não utiliza receita, patrocínio ou clique.
517. Cartões utilizam minimização e detalhamento progressivo.
518. Conteúdo sensível exige título neutro.
519. Estado funcional, informação, autorização, temporalidade, entrega e resposta permanecem distintos.
520. Pergunta não representa obrigação.
521. Sugestão não cria compromisso.
522. Lembrete não cria compromisso novo.
523. Alerta exige fundamento material.
524. Confirmação precede efeitos relevantes.
525. Entrega não representa visualização.
526. Visualização não representa compreensão.
527. Compreensão não representa concordância.
528. Atenção não representa consentimento.
529. Ausência de resposta não representa recusa.
530. Adiamento não representa rejeição.
531. Silêncio não representa falha.
532. Recusa não gera penalidade.
533. Importância não representa urgência.
534. Prazo promocional não representa prazo funcional.
535. Escassez comercial não fabrica urgência.
536. Relações comerciais permanecem visíveis.
537. Guivos Ads permanece separado de intervenções funcionais.
538. O participante controla frequência, canais, horários, categorias e intensidade.
539. Horários protegidos prevalecem sobre intervenções não críticas.
540. Fadiga reduz frequência e intensidade.
541. Fadiga não autoriza pressão adicional.
542. Intervenções sensíveis não expõem conteúdo em prévias públicas.
543. Terceiros não formam perfis paralelos.
544. Intervenções coletivas preservam decisões individuais.
545. Processos externos permanecem sob autoridade do executor.
546. Conflitos não são ocultados.
547. Correções preservam histórico.
548. Revogação permanece visível até propagação suficiente.
549. Falha parcial não representa sucesso integral.
550. Sincronização pendente não representa estado definitivo.
551. Acessibilidade técnica e cognitiva são obrigatórias.
552. Métricas avaliam a capacidade.
553. A interface não maximiza notificações ou tempo de tela.
554. O silêncio deve ser tão acessível quanto a resposta.
555. A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`, e o participante permanece no controle da visualização e do controle.

## Documentos do domínio"""
    text = replace_once(text, rules_marker, rules, "architecture rules")
    text = replace_once(
        text,
        "- [PAS-001-IC-LIFECYCLE-001 — Ciclo de Vida das Intervenções Contextuais](pas-001-intervencoes-contextuais-ciclo-de-vida.md)",
        "- [PAS-001-IC-LIFECYCLE-001 — Ciclo de Vida das Intervenções Contextuais](pas-001-intervencoes-contextuais-ciclo-de-vida.md)\n- [PAS-001-IC-VIEW-001 — Visualização e Controle das Intervenções Contextuais](pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "architecture link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(arquitetura): registrar visualização de Intervenções Contextuais")


def update_roadmap() -> None:
    path = Path("docs/roadmap.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.2.0", "version: 9.3.0", "roadmap version")
    text = text.replace(
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 40%.",
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 60%.",
    )
    text = text.replace(
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0` e `PAS-001-IC-LIFECYCLE-001 1.0.0`.",
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0` e `PAS-001-IC-VIEW-001 1.0.0`.",
    )
    text = text.replace(
        "O próximo trabalho deverá consolidar os comportamentos funcionais da visualização e do controle da `Capacidade 07 — Intervenções Contextuais`.",
        "O próximo trabalho deverá consolidar os contratos dos eventos funcionais da `Capacidade 07 — Intervenções Contextuais`.",
    )
    marker = """- propagação, retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `40%`."""
    addition = """- propagação, retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

`PAS-001-IC-VIEW-001 1.0.0` consolida:

- Central de Intervenções e Fila de Atenção como superfícies distintas;
- ausência legítima, contagens não avaliativas, agrupamentos e ordenação funcional neutra;
- cartões minimizados, títulos funcionais e títulos neutros;
- estados e dimensões independentes;
- perguntas, informações, sugestões, lembretes, alertas, confirmações e ações contextuais;
- espera, observação, silêncio, detalhamento, justificativas e proveniência;
- importância, urgência, prazo, sensibilidade e relações comerciais visíveis;
- histórico, correções, busca, filtros e controles principais;
- resposta, adiamento, silêncio, recusa, ocultação, bloqueio, contestação, correção e revogação;
- frequência, horários protegidos, canais, categorias, intensidade, resumos e fadiga;
- notificações, e-mail, canais conversacionais, calendário e superfícies especializadas;
- consistência entre canais, acessibilidade, linguagem e privacidade visual;
- proteção de intervenções sensíveis, coletivas, institucionais, comerciais e de terceiros;
- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`."""
    text = replace_once(text, marker, addition, "roadmap view section")
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress | 40% |",
        "| 07 — Intervenções Contextuais | In progress | 60% |",
    )
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*\Z",
        """## Ponto exato de retomada

Retomar nos **contratos dos eventos funcionais das Intervenções Contextuais**.

Próxima entrega:

1. estrutura comum do evento e agregado funcional;
2. identidade, participante, ator, papel e autoridade;
3. finalidade, proveniência, sensibilidade e permissões;
4. temporalidades, correlação e causalidade funcional;
5. eventos de identificação, candidatura, avaliação e admissão;
6. eventos de seleção de comportamento, programação e prontidão;
7. eventos de apresentação, entrega, resposta e ausência de resposta;
8. eventos de adiamento, silêncio, recusa, ocultação e bloqueio;
9. eventos de contestação, correção e revogação;
10. propagação, idempotência, ordenação, concorrência e atomicidade;
11. reconstrução, auditoria, compatibilidade e falha segura.
""",
        "roadmap resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(roadmap): avançar Intervenções Contextuais")


def update_board() -> None:
    path = Path("docs/project/knowledge-board.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.2.0", "version: 9.3.0", "board version")
    text = replace_once(
        text,
        "| PAS-001-IC-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida das Intervenções Contextuais |",
        "| PAS-001-IC-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida das Intervenções Contextuais |\n| PAS-001-IC-VIEW-001 | Active 1.0.0 | Definir a visualização e o controle das Intervenções Contextuais |",
        "board asset",
    )
    text = text.replace(
        "| Extensão normativa vigente | `PAS-001-IC-LIFECYCLE-001 1.0.0` |",
        "| Extensão normativa vigente | `PAS-001-IC-VIEW-001 1.0.0` |",
    )
    text = text.replace(
        "| Progresso editorial de Intervenções Contextuais | `40%` |",
        "| Progresso editorial de Intervenções Contextuais | `60%` |",
    )
    text = text.replace(
        "| Foco imediato | Consolidar visualização e controle das Intervenções Contextuais |",
        "| Foco imediato | Consolidar os contratos dos eventos funcionais das Intervenções Contextuais |",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 40% | Fundamentos e ciclo de vida consolidados; visualização e controle são a próxima entrega |",
        "| 07 — Intervenções Contextuais | In progress — 60% | Fundamentos, ciclo de vida, visualização e controle consolidados; eventos funcionais são a próxima entrega |",
    )
    marker = """- retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `40%`."""
    addition = """- retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

### Visualização e controle

- Central de Intervenções como superfície principal e Fila de Atenção como recorte temporal distinto;
- ausência legítima de intervenções e contagens sem uso avaliativo;
- agrupamentos e ordenação funcional sem influência de receita, patrocínio, clique ou meta comercial;
- cartões com minimização, detalhamento progressivo, títulos funcionais e títulos neutros;
- estados funcionais e dimensões de informação, autorização, temporalidade, entrega, resposta, atenção, fadiga, sensibilidade e operação externa apresentados separadamente;
- perguntas, informações, sugestões, lembretes, alertas, confirmações e ações com conteúdos próprios;
- espera, observação e silêncio apresentados como estados legítimos;
- justificativas `Por que estou vendo isto?` e `Por que agora?`;
- fonte, autoridade, incerteza, validade, importância, urgência, prazo e relações comerciais visíveis;
- histórico, correções, busca, filtros e controles de resposta, adiamento, silêncio, recusa, ocultação, bloqueio, contestação e revogação;
- preferências de frequência, horários protegidos, canais, categorias, intensidade, resumos e controles de fadiga;
- notificações, e-mail, canais conversacionais, calendário e superfícies de produto consistentes;
- acessibilidade técnica e cognitiva, linguagem proporcional e privacidade visual;
- proteção de terceiros e de intervenções sensíveis, coletivas, institucionais e comerciais;
- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`."""
    text = replace_once(text, marker, addition, "board view section")
    text = text.replace(
        "| Intervenções Contextuais | In progress — 40% |",
        "| Intervenções Contextuais | In progress — 60% |",
    )
    text = replace_once(
        text,
        "| Ciclo de Vida de Intervenções Contextuais | Normative 1.0.0 |",
        "| Ciclo de Vida de Intervenções Contextuais | Normative 1.0.0 |\n| Visualização e Controle de Intervenções Contextuais | Normative 1.0.0 |\n| Central de Intervenções | Superfície principal de compreensão, decisão e controle das manifestações |\n| Fila de Atenção de Intervenções | Recorte temporário do que pode justificar atenção atual ou próxima |\n| Privacidade visual de intervenção | Controles de título neutro, prévia, autenticação, modo discreto e histórico protegido |",
        "board concepts",
    )
    text = text.replace("| Roadmap | 9.2.0 |", "| Roadmap | 9.3.0 |")
    text = text.replace("| Knowledge Board | 9.2.0 |", "| Knowledge Board | 9.3.0 |")
    text = replace_once(
        text,
        "| PAS-001-IC-LIFECYCLE-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-IC-LIFECYCLE-001 | Active 1.0.0 |\n| PAS-001-IC-VIEW-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "board governance",
    )
    text = replace_once(
        text,
        "Consolidar os **comportamentos funcionais da visualização e do controle das Intervenções Contextuais**, incluindo central de intervenções, fila de atenção, mensagens, perguntas, lembretes, alertas, justificativas, histórico, adiamento, silêncio, frequência, horários protegidos, canais, preferências, acessibilidade, privacidade, relações comerciais e consistência entre superfícies.",
        "Consolidar os **contratos dos eventos funcionais das Intervenções Contextuais**, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
        "board next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(board): registrar visualização de Intervenções Contextuais")


def update_matrix() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.1", "version: 1.8.2", "matrix version")
    text = text.replace(
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com fundamentos e ciclo de vida consolidados e progresso editorial de 40% |",
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com fundamentos, ciclo de vida, visualização e controle consolidados e progresso editorial de 60% |",
    )
    text = replace_once(
        text,
        "| Ciclo de Vida das Intervenções Contextuais | Manter | PAS-001-IC-LIFECYCLE-001 1.0.0 define dimensões independentes, estados, transições, identificação, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência e falha segura |",
        "| Ciclo de Vida das Intervenções Contextuais | Manter | PAS-001-IC-LIFECYCLE-001 1.0.0 define dimensões independentes, estados, transições, identificação, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência e falha segura |\n| Visualização e Controle das Intervenções Contextuais | Manter | PAS-001-IC-VIEW-001 1.0.0 define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais e consistência entre canais |",
        "matrix document",
    )
    text = replace_once(
        text,
        "| Intervenção comercial | Refinar | Comunicação identificada, separada da funcional e proibida de utilizar contexto sensível ou urgência fabricada |",
        "| Intervenção comercial | Refinar | Comunicação identificada, separada da funcional e proibida de utilizar contexto sensível ou urgência fabricada |\n| Central de Intervenções | Manter | Superfície principal de compreensão e controle, distinta de caixa de entrada infinita, feed social ou canal publicitário |\n| Fila de Atenção de Intervenções | Manter | Recorte temporário do que pode justificar atenção atual ou próxima, distinto do conjunto total de intervenções |\n| Privacidade visual de intervenção | Manter | Títulos neutros, modo discreto, prévias protegidas, autenticação proporcional e histórico restrito |\n| Controle de intervenção | Manter | Responder, adiar, silenciar, recusar, ocultar, bloquear, contestar, corrigir e revogar permanecem ações distintas |",
        "matrix concepts",
    )
    text = text.replace(
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-LIFECYCLE-001 1.0.0` consolida o ciclo de vida da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 40% e define dimensões, estados, transições, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência, ordenação, concorrência e falha segura, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-VIEW-001 1.0.0` consolida a visualização e o controle da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 60% e define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura, sem promover candidatos arquiteturais à Canon.",
    )
    text = text.replace(
        "Consolidar as **regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais**, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "Consolidar os **contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais**, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(canon): consolidar visualização de Intervenções Contextuais")


def update_mkdocs() -> None:
    path = Path("mkdocs.yml")
    text = path.read_text(encoding="utf-8")
    marker = "      - PAS-001-IC-LIFECYCLE-001 — Ciclo de Vida das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md"
    text = replace_once(
        text,
        marker,
        marker + "\n      - PAS-001-IC-VIEW-001 — Visualização e Controle das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md",
        "mkdocs nav",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(site): adicionar visualização de Intervenções Contextuais")


def update_changelog() -> None:
    path = Path("CHANGELOG.md")
    text = path.read_text(encoding="utf-8")
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    entry = """## 0.36.2 — Contextual Interventions Visualization and Control

- Criação de `PAS-001-IC-VIEW-001 — Visualização e Controle das Intervenções Contextuais`, versão `1.0.0`.
- Registro do documento como terceira extensão normativa da Capacidade 07 do `PAS-001 — Guivos Journey`.
- Definição da Central de Intervenções como superfície principal de compreensão e controle.
- Definição da Fila de Atenção como recorte temporário do que pode justificar atenção atual ou próxima.
- Reconhecimento da ausência legítima de intervenções, sem preenchimento por anúncios ou mensagens de engajamento.
- Limitação de contagens como instrumentos de organização, sem equivalência a produtividade, qualidade, sucesso ou evolução.
- Consolidação de agrupamentos e ordenação funcional por risco, prazo, confirmação, reversibilidade, impacto e sensibilidade, sem influência de comissão, patrocínio, clique, margem ou meta comercial.
- Definição dos cartões de intervenção, conteúdo mínimo, títulos funcionais e títulos neutros.
- Separação visual entre estado funcional, informação, autorização, temporalidade, entrega, resposta, atenção, fadiga, sensibilidade e operação externa.
- Definição dos comportamentos visuais de pergunta, informação, sugestão, lembrete, alerta, confirmação, ação, espera, observação e silêncio.
- Consolidação do detalhamento progressivo e das justificativas `Por que estou vendo isto?` e `Por que agora?`.
- Definição da apresentação de fonte, autoridade, incerteza, validade temporal, importância, urgência, prazo e relações comerciais.
- Separação visual e funcional de Guivos Ads.
- Consolidação das relações com outras capacidades e dos processos externos.
- Definição do histórico, correções, busca, filtros e controles principais.
- Consolidação das ações de responder, adiar, silenciar, recusar, ocultar, bloquear, contestar, corrigir e revogar.
- Definição das preferências de frequência, horários protegidos, canais, categorias, intensidade, resumos e controles de fadiga.
- Consolidação das notificações, e-mail, canais conversacionais, calendário e superfícies de produtos.
- Definição da consistência entre canais e do detalhamento progressivo.
- Consolidação da acessibilidade técnica e cognitiva, linguagem proporcional, ambiente, dispositivo e privacidade visual.
- Proteção das informações de terceiros e das intervenções coletivas, institucionais, de saúde, financeiras, jurídicas, religiosas, sociais, de voluntariado e comerciais.
- Proibição de converter promoções e escassez comercial em urgência funcional.
- Definição da falha de apresentação, falha parcial, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.
- Registro dos eventos funcionais iniciais da visualização, métricas sistêmicas, responsabilidades, limites, critérios de aceite e 45 regras fundamentais.
- Atualização da Arquitetura de Produtos para `1.8.2` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap para `9.3.0`, do Knowledge Board para `9.3.0` e da Matriz de Consolidação Canônica para `1.8.2`.
- Atualização do README e da página inicial do GKR.
- Manutenção da Capacidade 07 no estado `In progress` e elevação do progresso editorial de referência de 40% para 60%.
- Preservação das Capacidades 02, 03, 04, 05 e 06 como `Functionally complete`.
- Preservação da Capacidade 08 — Experiências como `Planned`.
- Definição dos contratos dos eventos funcionais das Intervenções Contextuais como próximo ponto exato de retomada.

"""
    text = replace_once(text, marker, marker + entry, "changelog header")
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(changelog): registrar visualização de Intervenções Contextuais")


def validate() -> None:
    checks = {
        "normative start": "# 2967. Finalidade da visualização e do controle" in Path("docs/product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md").read_text(encoding="utf-8"),
        "normative end": "# 3064. Continuidade normativa" in Path("docs/product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md").read_text(encoding="utf-8"),
        "no generated ids": 'id="' not in Path("docs/product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md").read_text(encoding="utf-8"),
        "README 60": "In progress — 60%" in Path("README.md").read_text(encoding="utf-8"),
        "home 60": "In progress — 60%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.8.2" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 9.3.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 9.3.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.8.2" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "nav": "pas-001-intervencoes-contextuais-visualizacao-controle.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.36.2 — Contextual Interventions Visualization and Control" in Path("CHANGELOG.md").read_text(encoding="utf-8"),
        "next events": "contratos dos eventos funcionais" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validation failed: " + ", ".join(failed))
    run("git", "diff", "--check")


def main() -> None:
    update_readme()
    update_home()
    update_product_architecture()
    update_roadmap()
    update_board()
    update_matrix()
    update_mkdocs()
    update_changelog()
    validate()
    branch = os.environ.get("GITHUB_HEAD_REF") or os.environ["GITHUB_REF_NAME"]
    run("git", "push", "origin", f"HEAD:{branch}")


if __name__ == "__main__":
    main()
