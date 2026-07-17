from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def replace_once(content: str, old: str, new: str, path: str) -> str:
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: esperado 1 ocorrência, encontradas {count}: {old[:120]!r}")
    return content.replace(old, new, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_once(text, "- **Capacidade ativa:** 08 — Experiências, `In progress`, 20%", "- **Capacidade ativa:** 08 — Experiências, `In progress`, 40%", path)
    text = replace_once(
        text,
        "- **Extensão vigente de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0",
        "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0 e PAS-001-EXP-LIFECYCLE-001 1.0.0",
        path,
    )
    old = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades, limites e comportamentos proibidos.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de **20%**.\n\n## Ponto exato de retomada\n\nRetomar nas regras do ciclo de vida da Capacidade 08 — Experiências.\n\nPróxima entrega:\n\n- identificação, candidatura e validação da ocorrência;\n- planejamento, preparação, prontidão e início;\n- presença, participação, envolvimento e acompanhamento;\n- pausa, retomada, conclusão, interrupção, cancelamento e expiração;\n- recorrência, séries, episódios e continuidade;\n- entregas, resultados, percepções e satisfação;\n- evidências, memórias, significado e reflexão;\n- contestação, correção, revogação e propagação;\n- ordenação, concorrência, reconstrução e falha segura.\n"""
    new = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades, limites e comportamentos proibidos.\n\n`PAS-001-EXP-LIFECYCLE-001 1.0.0` consolida:\n\n- dimensões independentes de estado funcional, informação, ocorrência, temporalidade, relação individual, presença, participação, envolvimento, entrega, resultado, percepção, satisfação, evidências, memória, significado, autorização, contestação e propagação;\n- estados funcionais desde identificação até arquivamento, revogação e falha;\n- transições válidas e proibição de conversões indevidas entre planejamento, presença, participação, resultado, satisfação, significado e transformação;\n- identificação, fontes, deduplicação, candidatura, rejeição e validação de autoridade, identidade, temporalidade e ocorrência;\n- reconstrução retrospectiva com preservação de incerteza, proveniência e eventos ausentes;\n- planejamento, preparação, prontidão, início, presença, participação, envolvimento e acompanhamento proporcional;\n- pausa, retomada, conclusão, interrupção, cancelamento e expiração;\n- recorrência, séries, episódios e continuidade;\n- entrega, resultado, percepção, satisfação e efeitos positivos, negativos, neutros ou ambivalentes;\n- evidências, memórias, significado e reflexão opcionais;\n- candidaturas limitadas para Eventos de Vida e possível transformação;\n- contestação, correção compensatória, revogação e propagação proporcional;\n- idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de **40%**.\n\n## Ponto exato de retomada\n\nRetomar na visualização e no controle da Capacidade 08 — Experiências.\n\nPróxima entrega:\n\n- superfícies principais de experiências;\n- linha do tempo, calendário, séries e episódios;\n- cartões e detalhamento progressivo;\n- participantes, presença, participação e estados independentes;\n- entregas, resultados, percepções e satisfação;\n- evidências, memórias, significado e reflexão;\n- privacidade visual, conteúdo sensível e proteção de terceiros;\n- explicabilidade, histórico, contestação e correção;\n- revogação, compartilhamento e controles do participante;\n- acessibilidade, consistência entre canais e falha segura.\n"""
    text = replace_once(text, old, new, path)
    text = text.replace("progresso editorial de referência de `20%`", "progresso editorial de referência de `40%`")
    text = replace_once(text, "| 08 — Experiências | In progress — 20% |", "| 08 — Experiências | In progress — 40% |", path)
    text = replace_once(
        text,
        "- [Fundamentos Iniciais de Experiências](docs/product-architecture/pas-001-experiencias-fundamentos-iniciais.md)",
        "- [Fundamentos Iniciais de Experiências](docs/product-architecture/pas-001-experiencias-fundamentos-iniciais.md)\n- [Ciclo de Vida das Experiências](docs/product-architecture/pas-001-experiencias-ciclo-de-vida.md)",
        path,
    )
    write(path, text)


def update_docs_index() -> None:
    path = "docs/index.md"
    text = read(path)
    text = replace_once(text, "- Capacidade 08 — Experiências em desenvolvimento, `In progress`, 20%;", "- Capacidade 08 — Experiências em desenvolvimento, `In progress`, 40%;", path)
    text = replace_once(
        text,
        "- `PAS-001-EXP-FOUNDATION-001 1.0.0` como primeira extensão normativa da Capacidade 08;",
        "- `PAS-001-EXP-FOUNDATION-001 1.0.0` e `PAS-001-EXP-LIFECYCLE-001 1.0.0` como extensões normativas vigentes da Capacidade 08;",
        path,
    )
    text = replace_once(text, "Consolidar as **regras do ciclo de vida da Capacidade 08 — Experiências**.", "Consolidar a **visualização e o controle da Capacidade 08 — Experiências**.", path)
    text = replace_once(
        text,
        "A primeira extensão de Experiências consolida o vivido, suas distinções, titularidade, temporalidade, sensibilidade, relações, estados e limites iniciais.",
        "As duas extensões de Experiências consolidam o vivido, suas distinções, titularidade, temporalidade, sensibilidade, estados, transições, validação da ocorrência, recorrência, resultados, memórias, correção, revogação e falha segura.",
        path,
    )
    text = replace_once(
        text,
        "- [Fundamentos Iniciais de Experiências](product-architecture/pas-001-experiencias-fundamentos-iniciais.md)",
        "- [Fundamentos Iniciais de Experiências](product-architecture/pas-001-experiencias-fundamentos-iniciais.md)\n- [Ciclo de Vida das Experiências](product-architecture/pas-001-experiencias-ciclo-de-vida.md)",
        path,
    )
    text = replace_once(text, "| 08 — Experiências | In progress — 20% |", "| 08 — Experiências | In progress — 40% |", path)
    text = replace_once(
        text,
        "Retomar nas regras do ciclo de vida da Capacidade 08 — Experiências, incluindo identificação, candidatura, validação da ocorrência, planejamento, preparação, início, participação, acompanhamento, pausa, retomada, conclusão, interrupção, cancelamento, recorrência, episódios, entrega, resultado, percepção, satisfação, evidência, memória, significado, contestação, correção, revogação, propagação e falha segura.",
        "Retomar na visualização e no controle da Capacidade 08 — Experiências, incluindo superfícies, cartões, linha do tempo, calendário, séries, episódios, participantes, estados independentes, evidências, memórias, significado, privacidade, explicabilidade, contestação, correção, revogação, acessibilidade e falha segura.",
        path,
    )
    write(path, text)


def update_mkdocs() -> None:
    path = "mkdocs.yml"
    text = read(path)
    text = replace_once(
        text,
        "      - PAS-001-EXP-FOUNDATION-001 — Fundamentos de Experiências: product-architecture/pas-001-experiencias-fundamentos-iniciais.md",
        "      - PAS-001-EXP-FOUNDATION-001 — Fundamentos de Experiências: product-architecture/pas-001-experiencias-fundamentos-iniciais.md\n      - PAS-001-EXP-LIFECYCLE-001 — Ciclo de Vida das Experiências: product-architecture/pas-001-experiencias-ciclo-de-vida.md",
        path,
    )
    write(path, text)


def update_product_architecture() -> None:
    path = "docs/product-architecture/index.md"
    text = read(path)
    text = replace_once(text, "version: 1.10.0", "version: 1.11.0", path)
    text = replace_once(
        text,
        "A extensão normativa vigente é:\n\n- `PAS-001-EXP-FOUNDATION-001 1.0.0` — finalidade, pergunta central, definição canônica, singularidade, distinções, Registro de Experiência, titularidade, participantes, temporalidades, sensibilidade, entregas, resultados, evidências, memórias, significado, relações, estados, eventos, controles e limites iniciais.",
        "As extensões normativas vigentes são:\n\n- `PAS-001-EXP-FOUNDATION-001 1.0.0` — finalidade, pergunta central, definição canônica, singularidade, distinções, Registro de Experiência, titularidade, participantes, temporalidades, sensibilidade, entregas, resultados, evidências, memórias, significado, relações, estados, eventos, controles e limites iniciais;\n- `PAS-001-EXP-LIFECYCLE-001 1.0.0` — estados, transições, identificação, validação da ocorrência, planejamento, preparação, início, participação, recorrência, resultados, percepção, satisfação, evidências, memórias, significado, contestação, correção, revogação, propagação e falha segura.",
        path,
    )
    old = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e comportamentos proibidos.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de `20%`.\n\nO próximo bloco deverá consolidar as regras do ciclo de vida das Experiências.\n"""
    new = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e comportamentos proibidos.\n\nO ciclo de vida consolida:\n\n- dimensões independentes do estado da experiência;\n- estados funcionais e transições válidas, proibidas e retrospectivas;\n- identificação, fontes, deduplicação, candidatura, rejeição e validação da ocorrência;\n- planejamento, preparação, prontidão, início, presença, participação, envolvimento e acompanhamento proporcional;\n- pausa, retomada, conclusão, interrupção, cancelamento e expiração;\n- recorrência, séries, episódios e continuidade;\n- entrega, resultado, percepção, satisfação e efeitos ambivalentes;\n- evidências, memórias, significado e reflexão opcionais;\n- contestação, correção compensatória, revogação e propagação;\n- idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de `40%`.\n\nO próximo bloco deverá consolidar a visualização e o controle das Experiências.\n"""
    text = replace_once(text, old, new, path)
    rules = """732. `PAS-001-EXP-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 08, com progresso editorial de referência de `20%`, e o participante permanece no controle.\n733. O ciclo de vida separa estado funcional, informação, ocorrência, temporalidade, relação individual, presença, participação, envolvimento, entrega, resultado, percepção, satisfação, evidência, memória, significado, autorização, contestação e propagação.\n734. Identificação não representa candidatura aceita ou ocorrência.\n735. Candidatura não representa experiência vivida.\n736. Planejamento não representa início.\n737. Preparação não representa prontidão.\n738. Prontidão não representa presença ou participação.\n739. Início técnico isolado não representa início funcional.\n740. Presença não representa participação.\n741. Participação não representa envolvimento integral.\n742. Envolvimento não representa satisfação, resultado ou transformação.\n743. Conclusão não representa satisfação ou significado.\n744. Interrupção preserva resultados e percepções parciais.\n745. Cancelamento anterior ao início não deve ser apresentado como experiência vivida.\n746. Expiração exige nova validação antes de eventual reativação.\n747. Experiências recorrentes devem possuir séries e episódios distinguíveis.\n748. Episódios podem possuir participantes e estados diferentes.\n749. Continuidade não pode ser presumida apenas por repetição técnica.\n750. Entrega permanece separada da experiência e do resultado.\n751. Resultado preserva fonte, período, limitações e incerteza causal.\n752. Percepção pertence ao participante.\n753. Satisfação é opcional e não pode ser pressionada.\n754. Efeitos negativos, neutros e ambivalentes devem permanecer registráveis.\n755. Evidência somente sustenta afirmações dentro de seu escopo.\n756. Memória preserva autoria, privacidade, terceiros e revisões.\n757. Significado não pode ser imposto por fornecedor, patrocinador ou sistema.\n758. Reflexão é opcional e sua ausência não torna a experiência incompleta.\n759. Experiência somente envia candidatura para Evento de Vida, sem confirmá-lo.\n760. Possível transformação permanece sob avaliação de capacidade competente.\n761. Contestação pode atingir ocorrência, datas, participantes, entrega, resultado, percepção, evidência, memória, significado, uso e propagação.\n762. Correções são compensatórias e auditáveis.\n763. Revogação bloqueia novos usos e depende de propagação suficiente.\n764. Capacidades consumidoras recebem apenas recortes necessários e decidem dentro de sua própria autoridade.\n765. Reprocessamento idempotente não duplica experiências, episódios, resultados, memórias ou propagações.\n766. Duplicidade semântica deve ser avaliada mesmo sem identificador técnico comum.\n767. Eventos fora de ordem preservam momento do fato, declaração, conhecimento e persistência.\n768. Atualizações concorrentes preservam versão, autoridade, conflitos e histórico.\n769. Percepção do participante não pode ser sobrescrita por fornecedor.\n770. Falha parcial não produz sucesso integral aparente.\n771. Estado funcional deve ser reconstruível a partir do histórico válido.\n772. Ausência de informação suficiente produz estado desconhecido ou validação pendente.\n773. Falha segura reduz automação, propagação e exposição sensível.\n774. Retenção é proporcional à finalidade, sensibilidade, autorização e necessidade legítima.\n775. Arquivamento não autoriza publicidade ou exposição indefinida.\n776. O participante compreende origem, validação, inferências, incertezas e propagação.\n777. O participante pode confirmar, negar, corrigir, ocultar, compartilhar, contestar e revogar.\n778. A capacidade não avalia mérito, fé, valor humano ou evolução pela quantidade de experiências.\n779. Visualização posterior deverá preservar dimensões independentes, privacidade, explicabilidade e controle.\n780. `PAS-001-EXP-LIFECYCLE-001 1.0.0` eleva a Capacidade 08 para `40%`, mantém `In progress` e preserva o participante no controle.\n"""
    text = replace_once(
        text,
        "732. `PAS-001-EXP-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 08, com progresso editorial de referência de `20%`, e o participante permanece no controle.\n",
        rules,
        path,
    )
    text = replace_once(
        text,
        "- [PAS-001-EXP-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Experiências](pas-001-experiencias-fundamentos-iniciais.md)",
        "- [PAS-001-EXP-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Experiências](pas-001-experiencias-fundamentos-iniciais.md)\n- [PAS-001-EXP-LIFECYCLE-001 — Regras do Ciclo de Vida das Experiências](pas-001-experiencias-ciclo-de-vida.md)",
        path,
    )
    write(path, text)


def update_roadmap() -> None:
    path = "docs/roadmap.md"
    text = read(path)
    text = replace_once(text, "version: 10.1.0", "version: 10.2.0", path)
    text = replace_once(text, "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 20%.", "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 40%.", path)
    text = replace_once(
        text,
        "- **Extensão normativa vigente de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`.",
        "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0` e `PAS-001-EXP-LIFECYCLE-001 1.0.0`.",
        path,
    )
    text = replace_once(text, "O próximo trabalho deverá consolidar as regras do ciclo de vida da `Capacidade 08 — Experiências`.", "O próximo trabalho deverá consolidar a visualização e o controle da `Capacidade 08 — Experiências`.", path)
    old = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e limites.\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `20%`.\n"""
    new = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e limites.\n\n`PAS-001-EXP-LIFECYCLE-001 1.0.0` consolida:\n\n- dimensões independentes de estado funcional, informação, ocorrência, temporalidade, relação individual, presença, participação, envolvimento, entrega, resultado, percepção, satisfação, evidência, memória, significado, autorização, contestação e propagação;\n- estados funcionais, transições válidas, proibidas e retrospectivas;\n- identificação, fontes, deduplicação, candidatura, rejeição e validação da ocorrência;\n- reconstrução retrospectiva, planejamento, preparação, prontidão e início;\n- presença, participação, envolvimento e acompanhamento proporcional;\n- pausa, retomada, conclusão, interrupção, cancelamento e expiração;\n- recorrência, séries, episódios e continuidade;\n- entregas, resultados, percepções, satisfação e efeitos ambivalentes;\n- evidências, memórias, significado e reflexão opcionais;\n- contestação, correção compensatória, revogação e propagação;\n- idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `40%`.\n"""
    text = replace_once(text, old, new, path)
    text = replace_once(text, "| 08 — Experiências | In progress | 20% |", "| 08 — Experiências | In progress | 40% |", path)
    text = replace_once(
        text,
        "- não iniciar outro produto antes da conclusão funcional suficiente do Journey.",
        "- não tratar planejamento como experiência vivida;\n- não tratar presença como participação;\n- não tratar participação como satisfação ou transformação;\n- não apresentar experiência interrompida como concluída;\n- não reativar experiência expirada sem nova validação;\n- não impor percepção, memória ou significado;\n- não apagar histórico por correção destrutiva;\n- não declarar revogação concluída antes de propagação suficiente;\n- não transformar recorrência em evolução;\n- não utilizar experiências sensíveis para publicidade;\n- não apresentar falha parcial como sucesso integral;\n- não iniciar outro produto antes da conclusão funcional suficiente do Journey.",
        path,
    )
    old = """Retomar nas **regras do ciclo de vida da Capacidade 08 — Experiências**.\n\nPróxima entrega:\n\n1. dimensões independentes do ciclo de vida;\n2. identificação, candidatura e validação da ocorrência;\n3. planejamento, preparação, prontidão e início;\n4. presença, participação, envolvimento e acompanhamento;\n5. pausa, retomada, conclusão, interrupção, cancelamento e expiração;\n6. recorrência, séries, episódios e continuidade;\n7. entregas, resultados, percepções e satisfação;\n8. evidências, memórias, significado e reflexão;\n9. contestação, correção, revogação e propagação;\n10. idempotência, ordenação, concorrência, reconstrução e falha segura.\n"""
    new = """Retomar na **visualização e no controle da Capacidade 08 — Experiências**.\n\nPróxima entrega:\n\n1. superfícies principais e arquitetura de informação;\n2. linha do tempo, calendário, séries e episódios;\n3. cartões, agrupamentos e detalhamento progressivo;\n4. participantes, presença, participação e envolvimento;\n5. estados funcionais e dimensões independentes;\n6. entregas, resultados, percepções e satisfação;\n7. evidências, memórias, significado e reflexão;\n8. privacidade visual, sensibilidade e proteção de terceiros;\n9. histórico, explicabilidade, contestação, correção e revogação;\n10. acessibilidade, consistência entre canais e falha segura.\n"""
    text = replace_once(text, old, new, path)
    write(path, text)


def update_board() -> None:
    path = "docs/project/knowledge-board.md"
    text = read(path)
    text = replace_once(text, "version: 10.1.0", "version: 10.2.0", path)
    text = replace_once(
        text,
        "| PAS-001-EXP-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais da Capacidade de Experiências |",
        "| PAS-001-EXP-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais da Capacidade de Experiências |\n| PAS-001-EXP-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida das Experiências |",
        path,
    )
    text = replace_once(text, "| Extensão normativa vigente | `PAS-001-EXP-FOUNDATION-001 1.0.0` |", "| Extensões normativas vigentes | `PAS-001-EXP-FOUNDATION-001 1.0.0` e `PAS-001-EXP-LIFECYCLE-001 1.0.0` |", path)
    text = replace_once(text, "| Progresso editorial de Experiências | `20%` |", "| Progresso editorial de Experiências | `40%` |", path)
    text = replace_once(text, "| Foco imediato | Consolidar as regras do ciclo de vida da Capacidade 08 — Experiências |", "| Foco imediato | Consolidar a visualização e o controle da Capacidade 08 — Experiências |", path)
    text = replace_once(text, "| 08 — Experiências | In progress — 20% | Fundamentos iniciais consolidados; ciclo de vida é a próxima entrega |", "| 08 — Experiências | In progress — 40% | Fundamentos e ciclo de vida consolidados; visualização e controle são a próxima entrega |", path)
    old = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e comportamentos proibidos.\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `20%`.\n"""
    new = """- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e comportamentos proibidos.\n\n### Ciclo de vida\n\n- dimensões independentes de estado funcional, informação, ocorrência, temporalidade, relação individual, presença, participação, envolvimento, entrega, resultado, percepção, satisfação, evidência, memória, significado, autorização, contestação e propagação;\n- estados funcionais desde identificação até arquivamento, revogação e falha;\n- transições válidas, proibidas e retrospectivas;\n- identificação, fontes, deduplicação, candidatura, rejeição e validação de autoridade, identidade, temporalidade e ocorrência;\n- reconstrução retrospectiva, planejamento, preparação, prontidão e início;\n- presença, participação, envolvimento e acompanhamento proporcional;\n- pausa, retomada, conclusão, interrupção, cancelamento e expiração;\n- recorrência, séries, episódios e continuidade;\n- entrega, resultado, percepção, satisfação e efeitos ambivalentes;\n- evidências, memórias, significado e reflexão opcionais;\n- contestação, correção compensatória, revogação e propagação;\n- idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `40%`.\n"""
    text = replace_once(text, old, new, path)
    text = replace_once(text, "| Experiências | In progress — 20% |", "| Experiências | In progress — 40% |", path)
    text = replace_once(
        text,
        "| Fundamentos de Experiências | Normative 1.0.0 |",
        "| Fundamentos de Experiências | Normative 1.0.0 |\n| Ciclo de Vida de Experiências | Normative 1.0.0 |\n| Estado funcional da experiência | Identificada, Candidata, Em validação, Rejeitada, Planejada, Em preparação, Pronta, Iniciada, Em andamento, Pausada, Retomada, Concluída, Interrompida, Cancelada, Expirada, Contestada, Corrigida, Revogada, Arquivada ou Falha |\n| Ocorrência da experiência | Não avaliada, possível, provável, parcialmente confirmada, confirmada, divergente, contestada, não confirmada ou impossível de determinar |",
        path,
    )
    text = text.replace("| Roadmap | 10.1.0 |", "| Roadmap | 10.2.0 |")
    text = text.replace("| Knowledge Board | 10.1.0 |", "| Knowledge Board | 10.2.0 |")
    text = replace_once(
        text,
        "| PAS-001-EXP-FOUNDATION-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-EXP-FOUNDATION-001 | Active 1.0.0 |\n| PAS-001-EXP-LIFECYCLE-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        path,
    )
    text = replace_once(
        text,
        "Consolidar as **regras do ciclo de vida da Capacidade 08 — Experiências**, incluindo identificação, candidatura, validação da ocorrência, planejamento, preparação, início, participação, acompanhamento, pausa, retomada, conclusão, interrupção, cancelamento, recorrência, episódios, entrega, resultado, percepção, satisfação, evidência, memória, significado, contestação, correção, revogação, propagação e falha segura.",
        "Consolidar a **visualização e o controle da Capacidade 08 — Experiências**, incluindo superfícies, cartões, linha do tempo, calendário, séries, episódios, participantes, estados independentes, entregas, resultados, evidências, memórias, significado, privacidade, explicabilidade, contestação, correção, revogação, acessibilidade e falha segura.",
        path,
    )
    write(path, text)


def update_matrix() -> None:
    path = "docs/project/canonical-consolidation-matrix.md"
    text = read(path)
    text = replace_once(text, "version: 1.10.0", "version: 1.11.0", path)
    text = replace_once(
        text,
        "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos iniciais consolidados e progresso editorial de 20% |",
        "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos e ciclo de vida consolidados e progresso editorial de 40% |",
        path,
    )
    text = replace_once(
        text,
        "| Fundamentos Iniciais da Capacidade de Experiências | Manter | PAS-001-EXP-FOUNDATION-001 1.0.0 define finalidade, pergunta central, singularidade, distinções, titularidade, temporalidade, sensibilidade, relações, estados, eventos, controles e limites iniciais |",
        "| Fundamentos Iniciais da Capacidade de Experiências | Manter | PAS-001-EXP-FOUNDATION-001 1.0.0 define finalidade, pergunta central, singularidade, distinções, titularidade, temporalidade, sensibilidade, relações, estados, eventos, controles e limites iniciais |\n| Ciclo de Vida das Experiências | Manter | PAS-001-EXP-LIFECYCLE-001 1.0.0 define dimensões independentes, estados, transições, identificação, validação da ocorrência, planejamento, participação, recorrência, resultados, memórias, correção, revogação, propagação, idempotência e falha segura |\n| Estado funcional da experiência | Refinar | Identificação, candidatura, validação, planejamento, preparação, início, andamento, pausa, retomada, conclusão, interrupção, cancelamento, expiração, contestação, correção, revogação, arquivamento e falha permanecem estados distinguíveis |\n| Ocorrência da experiência | Refinar | Possibilidade, probabilidade, confirmação parcial, confirmação, divergência, contestação, não confirmação e impossibilidade de determinar preservam incerteza |",
        path,
    )
    text = replace_once(
        text,
        "As Capacidades 02, 03, 04, 05, 06 e 07 estão funcionalmente concluídas. `PAS-001-EXP-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 08, substitui seu estado `Planned` por `In progress`, estabelece progresso editorial de 20% e consolida a experiência vivida, distinções fundamentais, Registro de Experiência, titularidade, participantes, temporalidades, sensibilidade, entregas, resultados, evidências, memórias, significado, relações, estados, eventos, controles e limites iniciais, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02, 03, 04, 05, 06 e 07 estão funcionalmente concluídas. `PAS-001-EXP-LIFECYCLE-001 1.0.0` mantém a Capacidade 08 como `In progress`, eleva o progresso editorial para 40% e consolida dimensões independentes, estados, transições, identificação, validação da ocorrência, planejamento, preparação, início, participação, recorrência, entregas, resultados, percepção, satisfação, evidências, memórias, significado, contestação, correção, revogação, propagação e consistência técnica, sem promover candidatos arquiteturais à Canon.",
        path,
    )
    text = replace_once(
        text,
        "Consolidar as **regras do ciclo de vida da Capacidade 08 — Experiências**, incluindo identificação, candidatura, validação da ocorrência, planejamento, preparação, início, participação, acompanhamento, pausa, retomada, conclusão, interrupção, cancelamento, recorrência, episódios, entrega, resultado, percepção, satisfação, evidência, memória, significado, contestação, correção, revogação, propagação e falha segura.",
        "Consolidar a **visualização e o controle da Capacidade 08 — Experiências**, incluindo superfícies, cartões, linha do tempo, calendário, episódios, participantes, estados independentes, evidências, memórias, significado, privacidade, explicabilidade, contestação, correção, revogação, acessibilidade e falha segura.",
        path,
    )
    write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    block = """## 0.39.0 — Experiences Lifecycle\n\n- Criação de `PAS-001-EXP-LIFECYCLE-001 — Regras do Ciclo de Vida das Experiências`, versão `1.0.0`.\n- Registro do documento como segunda extensão normativa da Capacidade 08 do `PAS-001 — Guivos Journey`.\n- Manutenção da Capacidade 08 como `In progress` e elevação do progresso editorial de 20% para 40%.\n- Consolidação de 18 dimensões independentes do ciclo de vida.\n- Definição dos estados funcionais desde identificação até arquivamento, revogação e falha.\n- Definição dos estados da informação, ocorrência, temporalidade, presença, participação, envolvimento, entrega, resultado, percepção, satisfação, evidências, memória, significado, autorização, contestação e propagação.\n- Consolidação das transições válidas, proibidas e retrospectivas.\n- Definição das regras de identificação, fontes, deduplicação, candidatura, rejeição preliminar e validação.\n- Consolidação da validação de autoridade, identidade, participantes, temporalidade e ocorrência.\n- Definição da reconstrução retrospectiva com preservação de proveniência, lacunas e incerteza.\n- Consolidação de planejamento, preparação, prontidão, início, presença, participação, envolvimento e acompanhamento proporcional.\n- Definição de pausa, retomada, conclusão, interrupção, cancelamento e expiração.\n- Consolidação de recorrência, séries, episódios e continuidade.\n- Separação normativa entre entrega, resultado, percepção, satisfação, evidência, memória, significado e transformação.\n- Reconhecimento de efeitos positivos, negativos, neutros e ambivalentes.\n- Consolidação de contestação, correção compensatória, revogação e propagação proporcional.\n- Definição de idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n- Registro de 30 comportamentos proibidos e 58 critérios de aceite.\n- Atualização da Arquitetura de Produtos para `1.11.0` e inclusão da extensão na navegação do MkDocs.\n- Atualização do Roadmap e do Knowledge Board para `10.2.0`.\n- Atualização da Matriz de Consolidação Canônica para `1.11.0`.\n- Atualização do README e da página inicial do GKR.\n- Preservação das Capacidades 02, 03, 04, 05, 06 e 07 como `Functionally complete`.\n- Preservação da Capacidade 09 — Evolução Contínua como `Planned`.\n- Definição da visualização e do controle de Experiências como próximo ponto exato de retomada.\n\n"""
    text = replace_once(text, marker, marker + block, path)
    write(path, text)


def main() -> None:
    update_product_architecture()
    update_roadmap()
    update_board()
    update_matrix()
    update_readme()
    update_docs_index()
    update_mkdocs()
    update_changelog()


if __name__ == "__main__":
    main()
