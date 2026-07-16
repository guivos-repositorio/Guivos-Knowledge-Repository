from __future__ import annotations

import subprocess
from pathlib import Path


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Missing marker: {label}")
    return text.replace(old, new, 1)


def commit(path: str, message: str) -> None:
    run("git", "add", path)
    run("git", "commit", "-m", message)


def update_readme() -> None:
    path = Path("README.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 20%",
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 40%",
        "README progress",
    )
    text = replace_once(
        text,
        "- **Extensão vigente de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001 1.0.0",
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001 e PAS-001-IC-LIFECYCLE-001, ambas em 1.0.0",
        "README extensions",
    )
    marker = "A Capacidade 07 está **In progress**, com progresso editorial de referência de **20%**."
    lifecycle = """`PAS-001-IC-LIFECYCLE-001 1.0.0` consolida:

- dimensões independentes de estado funcional, informação, autorização, temporalidade, entrega, relação do participante, atenção, fadiga, sensibilidade e operação externa;
- estados funcionais desde identificação até encerramento, contestação, correção e falha;
- transições válidas e proibição de estados impossíveis;
- identificação por solicitação, sinal, mudança contextual, prazo, risco e sistema externo;
- deduplicação, candidatura, rejeição preliminar e avaliação formal;
- avaliações de finalidade, autoridade, relevância, temporalidade, atenção, interruptibilidade, urgência, importância, sensibilidade, fadiga, frequência, canal, reversibilidade, risco e alternativas;
- admissão simples e condicionada, rejeição e seleção de comportamento principal;
- programação, reprogramação, prontidão, espera, entrega, apresentação e execução externa;
- resposta, ausência de resposta, adiamento, recusa, ocultação e bloqueio;
- silêncio pós-avaliação, solicitado, por fadiga ou por sensibilidade;
- cancelamento, expiração, encerramento, contestação, correção e reabertura;
- escalonamento, desescalonamento e encaminhamento humano;
- repetição, recorrência, agrupamento e controles globais, por categoria e por canal;
- horários protegidos, mudanças materiais e intervenções sensíveis;
- compartilhamento, revogação, propagação, retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **40%**."""
    text = replace_once(text, marker, lifecycle, "README lifecycle summary")
    start = text.index("## Ponto exato de retomada")
    end = text.index("## Product Engineering")
    replacement = """## Ponto exato de retomada

Retomar nos comportamentos funcionais da visualização e do controle da Capacidade 07 — Intervenções Contextuais.

Próxima entrega:

- central de intervenções e fila de atenção;
- mensagens, perguntas, lembretes, alertas e confirmações;
- justificativas `Por que estou vendo isto?` e `Por que agora?`;
- histórico e estados de entrega;
- adiamento, silêncio, recusa, ocultação e bloqueio;
- controles de frequência, horários protegidos, canais e preferências;
- acessibilidade, privacidade e intervenções sensíveis;
- relações comerciais e separação de publicidade;
- consistência entre superfícies e falha segura.

"""
    text = text[:start] + replacement + text[end:]
    text = text.replace(
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `20%`.",
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `40%`.",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 20% |",
        "| 07 — Intervenções Contextuais | In progress — 40% |",
    )
    text = replace_once(
        text,
        "- [Fundamentos Iniciais de Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md)",
        "- [Fundamentos Iniciais de Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md)\n- [Ciclo de Vida das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md)",
        "README quick link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(readme): avançar ciclo de Intervenções Contextuais")


def update_index() -> None:
    path = Path("docs/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 20%;",
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 40%;",
        "index progress",
    )
    text = replace_once(
        text,
        "- `PAS-001-IC-FOUNDATION-001 1.0.0` como primeira extensão normativa vigente da Capacidade 07;",
        "- `PAS-001-IC-FOUNDATION-001 1.0.0` e `PAS-001-IC-LIFECYCLE-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
        "index extensions",
    )
    text = replace_once(
        text,
        "Consolidar as **regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar os **comportamentos funcionais da visualização e do controle da Capacidade 07 — Intervenções Contextuais**.",
        "index mission",
    )
    text = replace_once(
        text,
        "A primeira extensão de Intervenções Contextuais consolida finalidade, decisões de manifestação, silêncio, atenção, urgência, sensibilidade, fadiga, canais, autonomia e limites.",
        "As duas extensões de Intervenções Contextuais consolidam fundamentos e ciclo de vida, incluindo decisões de manifestação, estados independentes, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência e falha segura.",
        "index summary",
    )
    text = replace_once(
        text,
        "- [Fundamentos Iniciais de Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md)",
        "- [Fundamentos Iniciais de Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md)\n- [Ciclo de Vida das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md)",
        "index quick link",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 20% |",
        "| 07 — Intervenções Contextuais | In progress — 40% |",
    )
    text = replace_once(
        text,
        "Retomar nas regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "Retomar nos comportamentos funcionais da visualização e do controle da Capacidade 07 — Intervenções Contextuais, incluindo central de intervenções, fila de atenção, mensagens, perguntas, lembretes, alertas, justificativas, histórico, adiamento, silêncio, frequência, horários protegidos, canais, preferências, acessibilidade, privacidade, relações comerciais e consistência entre superfícies.",
        "index resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(index): avançar ciclo de Intervenções Contextuais")


def update_roadmap() -> None:
    path = Path("docs/roadmap.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.1.0", "version: 9.2.0", "roadmap version")
    text = replace_once(
        text,
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 20%.",
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 40%.",
        "roadmap progress",
    )
    text = replace_once(
        text,
        "- **Extensão normativa vigente de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`.",
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0` e `PAS-001-IC-LIFECYCLE-001 1.0.0`.",
        "roadmap extensions",
    )
    text = replace_once(
        text,
        "O próximo trabalho deverá consolidar as regras do ciclo de vida da `Capacidade 07 — Intervenções Contextuais`.",
        "O próximo trabalho deverá consolidar os comportamentos funcionais da visualização e do controle da `Capacidade 07 — Intervenções Contextuais`.",
        "roadmap direction",
    )
    marker = "A Capacidade 07 está `In progress`, com progresso editorial de referência de `20%`."
    lifecycle = """`PAS-001-IC-LIFECYCLE-001 1.0.0` consolida:

- dimensões independentes de estado funcional, informação, autorização, temporalidade, entrega, relação, atenção, fadiga, sensibilidade e operação externa;
- estados e transições do ciclo, com proibição de atalhos e estados impossíveis;
- identificação por solicitação, sinais, contexto, prazos, riscos e sistemas externos;
- deduplicação, candidatura, rejeição preliminar e avaliação formal;
- finalidade, autoridade, relevância, temporalidade, atenção, interruptibilidade, urgência, importância, sensibilidade, fadiga, frequência, canal, reversibilidade, risco e alternativas;
- admissão simples e condicionada, rejeição e seleção de comportamento;
- programação, prontidão, espera, entrega, apresentação e execução externa;
- resposta, ausência de resposta, adiamento, recusa, ocultação e bloqueio;
- silêncio pós-avaliação, solicitado, por fadiga e por sensibilidade;
- cancelamento, expiração, encerramento, contestação, correção e reabertura;
- escalonamento, desescalonamento, encaminhamento humano, repetição, recorrência, agrupamento e controle de frequência;
- horários protegidos, intervenções sensíveis, compartilhamento e revogação;
- propagação, retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `40%`."""
    text = replace_once(text, marker, lifecycle, "roadmap lifecycle summary")
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress | 20% |",
        "| 07 — Intervenções Contextuais | In progress | 40% |",
    )
    start = text.index("## Ponto exato de retomada")
    replacement = """## Ponto exato de retomada

Retomar nos **comportamentos funcionais da visualização e do controle das Intervenções Contextuais**.

Próxima entrega:

1. central de intervenções e fila de atenção;
2. mensagens, perguntas, lembretes, alertas e confirmações;
3. justificativas `Por que estou vendo isto?` e `Por que agora?`;
4. estados de entrega, resposta e histórico;
5. adiamento, silêncio, recusa, ocultação e bloqueio;
6. frequência, agrupamento, recorrência e horários protegidos;
7. canais, preferências e consistência entre superfícies;
8. acessibilidade e carga cognitiva;
9. privacidade e intervenções sensíveis;
10. relações comerciais e separação de publicidade;
11. contestação, correção e falha segura;
12. eventos iniciais da visualização e do controle.
"""
    text = text[:start] + replacement
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(roadmap): avançar Intervenções Contextuais")


def update_board() -> None:
    path = Path("docs/project/knowledge-board.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.1.0", "version: 9.2.0", "board version")
    foundation_row = "| PAS-001-IC-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais das Intervenções Contextuais |"
    text = replace_once(
        text,
        foundation_row,
        foundation_row + "\n| PAS-001-IC-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida das Intervenções Contextuais |",
        "board asset row",
    )
    text = replace_once(
        text,
        "| Extensão normativa vigente | `PAS-001-IC-FOUNDATION-001 1.0.0` |",
        "| Extensão normativa vigente | `PAS-001-IC-LIFECYCLE-001 1.0.0` |",
        "board current extension",
    )
    text = replace_once(
        text,
        "| Progresso editorial de Intervenções Contextuais | `20%` |",
        "| Progresso editorial de Intervenções Contextuais | `40%` |",
        "board progress",
    )
    text = replace_once(
        text,
        "| Foco imediato | Consolidar o ciclo de vida das Intervenções Contextuais |",
        "| Foco imediato | Consolidar visualização e controle das Intervenções Contextuais |",
        "board focus",
    )
    text = replace_once(
        text,
        "| 07 — Intervenções Contextuais | In progress — 20% | Fundamentos iniciais consolidados; ciclo de vida é a próxima entrega |",
        "| 07 — Intervenções Contextuais | In progress — 40% | Fundamentos e ciclo de vida consolidados; visualização e controle são a próxima entrega |",
        "board capability row",
    )
    marker = "A Capacidade 07 está `In progress`, com progresso editorial de referência de `20%`."
    lifecycle = """### Ciclo de vida

- dimensões independentes de estado funcional, informação, autorização, temporalidade, entrega, relação do participante, atenção, fadiga, sensibilidade e operação externa;
- estados desde identificação, candidatura e avaliação até entrega, resposta, silêncio, correção, falha e encerramento;
- transições fundamentais e proibição de atalhos funcionais;
- identificação por solicitação, sinal, mudança contextual, prazo, risco e sistema externo;
- deduplicação, candidatura, rejeição preliminar e avaliação formal;
- avaliação de finalidade, autoridade, relevância, temporalidade, atenção, interruptibilidade, urgência, importância, sensibilidade, fadiga, frequência, canal, reversibilidade, risco e alternativas;
- admissão simples e condicionada, rejeição e seleção de comportamento principal;
- programação, reprogramação, janela de entrega, prontidão, bloqueio e espera;
- entrega, entrega parcial, confirmação técnica, falha e apresentação;
- resposta, ausência de resposta, adiamento, recusa, ocultação e bloqueio;
- silêncio pós-avaliação, solicitado, por fadiga e por sensibilidade;
- cancelamento, expiração, encerramento, contestação, correção e reabertura;
- escalonamento, desescalonamento, encaminhamento humano, repetição, recorrência e agrupamento;
- controles globais, por categoria e por canal, com respeito a horários protegidos;
- intervenções sensíveis, compartilhamento, revogação e propagação;
- retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `40%`."""
    text = replace_once(text, marker, lifecycle, "board lifecycle summary")
    text = text.replace(
        "| Intervenções Contextuais | In progress — 20% |",
        "| Intervenções Contextuais | In progress — 40% |",
    )
    text = replace_once(
        text,
        "| Fundamentos de Intervenções Contextuais | Normative 1.0.0 |",
        "| Fundamentos de Intervenções Contextuais | Normative 1.0.0 |\n| Ciclo de Vida de Intervenções Contextuais | Normative 1.0.0 |\n| Estado funcional da intervenção | Identificada, Candidata, Em avaliação, Admitida, Programada, Aguardando, Pronta, Em entrega, Entregue, Respondida, Adiada, Silenciada, Cancelada, Expirada, Contestada, Corrigida, Falha ou Encerrada |\n| Estado de entrega da intervenção | Não iniciada, preparada, enviada, parcialmente entregue, entregue, confirmada, falha, pendente, bloqueada ou cancelada |\n| Relação do participante com intervenção | Não apresentada, apresentada, visualizada, respondida, aceita, recusada, adiada, ignorada, ocultada, bloqueada, contestada ou encerrada |",
        "board concepts",
    )
    text = text.replace("| Roadmap | 9.1.0 |", "| Roadmap | 9.2.0 |")
    text = text.replace("| Knowledge Board | 9.1.0 |", "| Knowledge Board | 9.2.0 |")
    text = replace_once(
        text,
        "| PAS-001-IC-FOUNDATION-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-IC-FOUNDATION-001 | Active 1.0.0 |\n| PAS-001-IC-LIFECYCLE-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "board governance",
    )
    text = replace_once(
        text,
        "Consolidar as **regras do ciclo de vida das Intervenções Contextuais**, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "Consolidar os **comportamentos funcionais da visualização e do controle das Intervenções Contextuais**, incluindo central de intervenções, fila de atenção, mensagens, perguntas, lembretes, alertas, justificativas, histórico, adiamento, silêncio, frequência, horários protegidos, canais, preferências, acessibilidade, privacidade, relações comerciais e consistência entre superfícies.",
        "board next activity",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(board): registrar ciclo de Intervenções Contextuais")


def update_matrix() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.0", "version: 1.8.1", "matrix version")
    text = replace_once(
        text,
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com primeira extensão normativa e progresso editorial de 20% |",
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com fundamentos e ciclo de vida consolidados e progresso editorial de 40% |",
        "matrix capability",
    )
    foundation = "| Fundamentos Iniciais de Intervenções Contextuais | Manter | PAS-001-IC-FOUNDATION-001 1.0.0 define singularidade, decisões, silêncio, atenção, urgência, sensibilidade, fadiga, canais, autonomia, relações e limites |"
    text = replace_once(
        text,
        foundation,
        foundation + "\n| Ciclo de Vida das Intervenções Contextuais | Manter | PAS-001-IC-LIFECYCLE-001 1.0.0 define dimensões independentes, estados, transições, identificação, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência e falha segura |",
        "matrix lifecycle document",
    )
    text = replace_once(
        text,
        "| Intervenção comercial | Refinar | Comunicação identificada, separada da funcional e proibida de utilizar contexto sensível ou urgência fabricada |",
        "| Intervenção comercial | Refinar | Comunicação identificada, separada da funcional e proibida de utilizar contexto sensível ou urgência fabricada |\n| Estado funcional da intervenção | Refinar | Identificada, Candidata, Em avaliação, Admitida, Programada, Aguardando, Pronta, Em entrega, Entregue, Respondida, Adiada, Silenciada, Cancelada, Expirada, Contestada, Corrigida, Falha ou Encerrada |\n| Estado de entrega da intervenção | Manter | Dimensão própria que não representa leitura, compreensão, concordância, interesse ou consentimento |\n| Relação do participante com intervenção | Manter | Apresentação, visualização, resposta, aceitação, recusa, adiamento, ocultação, bloqueio e contestação permanecem estados individuais distintos |\n| Admissão de intervenção | Refinar | Exige finalidade, autoridade, relevância, temporalidade, risco, sensibilidade, frequência e canal compatíveis |\n| Silêncio pós-avaliação | Manter | Resultado auditável quando a manifestação não produzir utilidade suficiente |\n| Controle de frequência de intervenção | Manter | Limites globais, por categoria e por canal, governados por finalidade, fadiga, preferência e mudança material |",
        "matrix lifecycle concepts",
    )
    text = replace_once(
        text,
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 07, altera seu estado para `In progress`, estabelece progresso editorial de 20% e consolida finalidade, oportunidade de intervenção, silêncio, atenção, interruptibilidade, urgência, sensibilidade, fadiga, canais, autonomia, relações, responsabilidades e limites, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-LIFECYCLE-001 1.0.0` consolida o ciclo de vida da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 40% e governa dimensões independentes, estados, transições, identificação, candidatura, avaliação, admissão, programação, entrega, resposta, silêncio, frequência, revogação, idempotência, ordenação, concorrência e falha segura, sem promover candidatos arquiteturais à Canon.",
        "matrix reconciliation",
    )
    text = replace_once(
        text,
        "Consolidar as **regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais**, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "Consolidar os **comportamentos funcionais da visualização e do controle da Capacidade 07 — Intervenções Contextuais**, incluindo central de intervenções, fila de atenção, mensagens, perguntas, lembretes, alertas, justificativas, histórico, adiamento, silêncio, frequência, horários protegidos, canais, preferências, acessibilidade, privacidade, relações comerciais e consistência entre superfícies.",
        "matrix next review",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(canon): consolidar ciclo de Intervenções Contextuais")


def update_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.0", "version: 1.8.1", "architecture version")
    marker = "A Capacidade 07 está **In progress**, com progresso editorial de referência de `20%`.\n\nO próximo bloco deverá consolidar as regras do ciclo de vida das Intervenções Contextuais."
    lifecycle = """O ciclo de vida consolida:

- dimensões independentes de estado funcional, informação, autorização, temporalidade, entrega, relação do participante, atenção, fadiga, sensibilidade e operação externa;
- estados funcionais desde identificação e candidatura até entrega, resposta, silêncio, correção, falha e encerramento;
- transições válidas e proibição de atalhos e estados impossíveis;
- identificação por solicitação, sinal, mudança contextual, prazo, risco e sistema externo;
- deduplicação, candidatura, rejeição preliminar e início da avaliação;
- avaliação de finalidade, autoridade, relevância, temporalidade, atenção, interruptibilidade, urgência, importância, sensibilidade, fadiga, frequência, canal, reversibilidade, risco e alternativas;
- conclusão da avaliação, admissão simples e condicionada, rejeição e seleção de comportamento principal;
- programação, reprogramação, janela de entrega, prontidão, bloqueio, espera e retomada;
- entrega, entrega parcial, confirmação técnica, falha e apresentação;
- resposta, ausência de resposta, adiamento, recusa, ocultação e bloqueio;
- silêncio pós-avaliação, solicitado, por fadiga e por sensibilidade;
- cancelamento, expiração, encerramento, contestação, correção, reabertura e nova intervenção;
- escalonamento, desescalonamento e encaminhamento humano;
- repetição, recorrência, agrupamento, supressão de duplicidade e controles globais, por categoria e por canal;
- horários protegidos, mudanças materiais, intervenções sensíveis, compartilhamento, revogação e propagação;
- retroatividade, idempotência, ordenação, concorrência, falha segura e reconstrução.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `40%`.

O próximo bloco deverá consolidar os comportamentos funcionais da visualização e do controle das Intervenções Contextuais."""
    text = replace_once(text, marker, lifecycle, "architecture lifecycle section")
    rule_marker = "464. O participante permanece no controle dos fundamentos de Intervenções Contextuais.\n\n## Documentos do domínio"
    rules = """464. O participante permanece no controle dos fundamentos de Intervenções Contextuais.
465. Estado funcional, informação, autorização, temporalidade, entrega, relação, atenção, fadiga, sensibilidade e operação externa permanecem dimensões independentes.
466. Sinal não representa necessidade confirmada.
467. Identificação não representa candidatura.
468. Candidatura não representa admissão.
469. Admissão não representa apresentação.
470. Programação não representa entrega.
471. Entrega não representa visualização.
472. Visualização não representa compreensão.
473. Compreensão não representa concordância.
474. Resposta não representa progresso.
475. Atenção não representa consentimento.
476. Disponibilidade técnica não representa interruptibilidade.
477. Importância não representa urgência.
478. Urgência comercial não representa urgência funcional.
479. Silêncio e espera são decisões funcionais legítimas.
480. Adiamento não representa recusa e recusa não representa fracasso.
481. Ausência de resposta não representa desinteresse definitivo.
482. Repetição exige fundamento novo, prazo real, solicitação, regra autorizada ou falha confirmada.
483. Fadiga reduz frequência e intensidade e nunca autoriza aumento de pressão.
484. Horários protegidos prevalecem sobre manifestações não críticas.
485. Conteúdo sensível exige minimização, título neutro, canal protegido e retenção limitada.
486. Publicidade permanece separada da intervenção funcional.
487. Comissão não altera relevância e patrocínio não aumenta prioridade.
488. Escassez comercial não fabrica urgência.
489. Produtos especializados executam suas próprias operações.
490. Intervenções governa o momento da manifestação, não o objetivo do participante.
491. Guivos Intelligence pode sugerir e explicar, mas não impor manifestação.
492. Platform Layer entrega mensagens sem definir relevância humana.
493. Ação material exige autoridade e autorização.
494. Admissão exige finalidade, autoridade, relevância, temporalidade, risco, sensibilidade, frequência e canal compatíveis.
495. Mudança material exige reavaliação antes da entrega.
496. Confirmação técnica de entrega não representa leitura, compreensão, concordância, interesse ou consentimento.
497. Contestação limita efeitos materiais e correção não reescreve histórico.
498. Revogação interrompe novos usos e somente termina após propagação suficiente.
499. Reprocessamento não duplica candidatura, admissão, programação, entrega, alerta, lembrete, resposta, contestação ou revogação.
500. Eventos fora de ordem não criam estados impossíveis.
501. Conflitos concorrentes não são sobrescritos silenciosamente.
502. Falha preserva o último estado válido e impede falsa entrega.
503. Falha parcial não representa sucesso integral.
504. Terceiros não formam perfis paralelos.
505. Intervenções recorrentes exigem finalidade, frequência, limite, janela, expiração, revisão e controle.
506. Agrupamento não oculta urgências, sensibilidades ou relações comerciais distintas.
507. Métricas futuras avaliam o sistema, não o participante.
508. O ciclo apoia decisões reais e não maximiza notificações ou tempo de tela.
509. A Capacidade 07 está `In progress`, com progresso editorial de referência de `40%`.
510. O participante permanece no controle do ciclo de vida das Intervenções Contextuais.

## Documentos do domínio"""
    text = replace_once(text, rule_marker, rules, "architecture lifecycle rules")
    text = replace_once(
        text,
        "- [PAS-001-IC-FOUNDATION-001 — Fundamentos Iniciais de Intervenções Contextuais](pas-001-intervencoes-contextuais-fundamentos-iniciais.md)",
        "- [PAS-001-IC-FOUNDATION-001 — Fundamentos Iniciais de Intervenções Contextuais](pas-001-intervencoes-contextuais-fundamentos-iniciais.md)\n- [PAS-001-IC-LIFECYCLE-001 — Ciclo de Vida das Intervenções Contextuais](pas-001-intervencoes-contextuais-ciclo-de-vida.md)",
        "architecture document link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(arquitetura): registrar ciclo de Intervenções Contextuais")


def update_mkdocs() -> None:
    path = Path("mkdocs.yml")
    text = path.read_text(encoding="utf-8")
    old = "      - PAS-001-IC-FOUNDATION-001 — Fundamentos de Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md"
    text = replace_once(
        text,
        old,
        old + "\n      - PAS-001-IC-LIFECYCLE-001 — Ciclo de Vida das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md",
        "mkdocs lifecycle entry",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(site): adicionar ciclo de Intervenções Contextuais")


def update_changelog() -> None:
    path = Path("CHANGELOG.md")
    text = path.read_text(encoding="utf-8")
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    entry = """## 0.36.1 — Contextual Interventions Lifecycle Rules

- Criação de `PAS-001-IC-LIFECYCLE-001 — Regras do Ciclo de Vida das Intervenções Contextuais`, versão `1.0.0`.
- Registro do documento como segunda extensão normativa da Capacidade 07 do `PAS-001 — Guivos Journey`.
- Definição da finalidade do ciclo desde identificação até encerramento, correção ou nova manifestação.
- Consolidação das dimensões independentes de estado funcional, informação, autorização, temporalidade, entrega, relação do participante, atenção, fadiga, sensibilidade e operação externa.
- Definição dos estados funcionais de Identificada, Candidata, Em avaliação, Admitida, Programada, Aguardando, Pronta, Em entrega, Entregue, Respondida, Adiada, Silenciada, Cancelada, Expirada, Contestada, Corrigida, Falha e Encerrada.
- Definição dos estados da informação, entrega, relação do participante, temporalidade, fadiga, sensibilidade e autorização.
- Consolidação das transições fundamentais e das transições funcionalmente proibidas.
- Definição da identificação por solicitação, sinal, mudança contextual, prazo, risco e sistema externo.
- Consolidação da deduplicação inicial, candidatura e rejeição preliminar.
- Definição das avaliações de finalidade, autoridade, relevância, temporalidade, atenção, interruptibilidade, urgência, importância, sensibilidade, fadiga, frequência, canal, reversibilidade, risco, alternativas e custo de interrupção.
- Definição dos tratamentos para informação insuficiente e solicitação proporcional de informação.
- Consolidação da admissão simples e condicionada, rejeição após avaliação e seleção de comportamento principal.
- Definição dos contratos de agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar e silenciar.
- Consolidação de programação, reprogramação, janela de entrega, prontidão, bloqueio, espera e retomada.
- Definição da entrega, entrega parcial, confirmação técnica, falha de entrega, apresentação e relação com execução externa.
- Consolidação das respostas, ausência de resposta, adiamento, recusa, ocultação e bloqueio.
- Definição do silêncio pós-avaliação, solicitado, por fadiga e por sensibilidade.
- Consolidação de cancelamento, expiração, encerramento, contestação, correção, reabertura e criação de nova intervenção diante de mudança material.
- Definição de escalonamento, desescalonamento e encaminhamento humano.
- Consolidação de repetição, recorrência, agrupamento, supressão de duplicidade e controles de frequência global, por categoria e por canal.
- Definição dos horários protegidos e da reavaliação por mudança material.
- Proteção de intervenções de saúde, finanças, jurídico, religião, espiritualidade, social, voluntariado, institucionais, comerciais, coletivas e relacionadas a terceiros.
- Definição do compartilhamento, revogação e propagação suficiente.
- Consolidação de retroatividade, idempotência, ordenação, concorrência, estados impossíveis, falha segura, falha parcial e reconstrução.
- Registro dos eventos funcionais do ciclo, responsabilidades, limites, critérios de aceite e 45 regras fundamentais.
- Atualização da Arquitetura de Produtos para `1.8.1` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap para `9.2.0`, do Knowledge Board para `9.2.0` e da Matriz de Consolidação Canônica para `1.8.1`.
- Atualização do README e da página inicial do GKR.
- Manutenção da Capacidade 07 no estado `In progress` e elevação do progresso editorial de referência de 20% para 40%.
- Preservação das Capacidades 02, 03, 04, 05 e 06 como `Functionally complete`.
- Preservação da Capacidade 08 — Experiências como `Planned`.
- Definição da visualização e do controle das Intervenções Contextuais como próximo ponto exato de retomada.

"""
    text = replace_once(text, marker, marker + entry, "changelog header")
    path.write_text(text, encoding="utf-8")

    artifact = Path("docs/product-architecture/pas-001-intervencoes-contextuais-ciclo-de-vida.md").read_text(encoding="utf-8")
    checks = {
        "artifact start": "# 2838. Finalidade do ciclo de vida" in artifact,
        "artifact end": "# 2966. Continuidade normativa" in artifact,
        "no generated ids": 'id="' not in artifact,
        "artifact progress": "de `20%` para `40%`" in artifact,
        "README progress": "In progress — 40%" in Path("README.md").read_text(encoding="utf-8"),
        "index progress": "In progress — 40%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 9.2.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 9.2.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.8.1" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.8.1" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "navigation": "pas-001-intervencoes-contextuais-ciclo-de-vida.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.36.1 — Contextual Interventions Lifecycle Rules" in text,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validation failed: " + ", ".join(failed))
    run("git", "diff", "--check")
    commit(str(path), "docs(changelog): registrar ciclo de Intervenções Contextuais")
    run("git", "push", "origin", "HEAD:ic-lifecycle-20260716")


def main() -> None:
    update_readme()
    update_index()
    update_roadmap()
    update_board()
    update_matrix()
    update_architecture()
    update_mkdocs()
    update_changelog()


if __name__ == "__main__":
    main()
