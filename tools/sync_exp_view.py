from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 ocorrência, encontrado {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, repl: str, label: str, flags: int = re.MULTILINE | re.DOTALL) -> str:
    new, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 match, encontrado {count}")
    return new


VIEW_SUMMARY = """`PAS-001-EXP-VIEW-001 1.0.0` consolida:

- `Minhas Experiências` como superfície principal de compreensão, acompanhamento, revisão e controle;
- áreas Agora, Próximas, Linha do tempo, Séries e episódios, Para validar e Arquivo;
- lista, cartões, calendário, linha do tempo, séries, episódios e mapa opcional;
- títulos funcionais, títulos neutros, privacidade visual e detalhamento progressivo;
- representação separada dos estados funcionais, ocorrência, participação, entrega, resultado, percepção, satisfação, evidências, memória, significado, autorização, contestação e propagação;
- experiências compartilhadas, coletivas e institucionais com autoridade limitada;
- entregas, resultados, efeitos positivos, negativos, neutros e ambivalentes;
- percepção e satisfação opcionais, evidências, memórias, significado e reflexão;
- explicabilidade por `Por que esta experiência está aqui?` e explicação de reconstrução retrospectiva;
- controles de confirmação, negação, incerteza, visibilidade, compartilhamento, contestação, correção e revogação;
- acessibilidade, consistência entre canais, dispositivos compartilhados, operação offline e falha segura;
- 30 comportamentos proibidos e 70 critérios de aceite."""


# Arquitetura de Produtos
path = "docs/product-architecture/index.md"
text = read(path)
text = replace_once(text, "version: 1.11.0", "version: 1.12.0", f"{path}: versão")
text = replace_once(text, "last_updated: 2026-07-16", "last_updated: 2026-07-17", f"{path}: data")
text = replace_once(
    text,
    "- `PAS-001-EXP-LIFECYCLE-001 1.0.0` — estados, transições, identificação, validação da ocorrência, planejamento, preparação, início, participação, recorrência, resultados, percepção, satisfação, evidências, memórias, significado, contestação, correção, revogação, propagação e falha segura.\n\nOs fundamentos consolidam:",
    "- `PAS-001-EXP-LIFECYCLE-001 1.0.0` — estados, transições, identificação, validação da ocorrência, planejamento, preparação, início, participação, recorrência, resultados, percepção, satisfação, evidências, memórias, significado, contestação, correção, revogação, propagação e falha segura;\n- `PAS-001-EXP-VIEW-001 1.0.0` — Minhas Experiências, áreas funcionais, cartões, linha do tempo, calendário, séries, episódios, estados independentes, privacidade, explicabilidade, compartilhamento, contestação, correção, revogação, acessibilidade e falha segura.\n\nOs fundamentos consolidam:",
    f"{path}: extensões",
)
text = replace_once(
    text,
    "- idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de `40%`.\n\nO próximo bloco deverá consolidar a visualização e o controle das Experiências.",
    "- idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, retenção, auditoria e falha segura.\n\n" + VIEW_SUMMARY + "\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de `60%`.\n\nO próximo bloco deverá consolidar os eventos funcionais das Experiências.",
    f"{path}: resumo",
)
rules = """781. `Minhas Experiências` é superfície de compreensão e controle, não feed social.
782. Ausência legítima de experiências não deve ser preenchida com publicidade.
783. Planejamento e ocorrência devem possuir representação visual distinta.
784. Cartões exibem recortes mínimos e não atribuem emoção ou transformação.
785. Experiências sensíveis suportam título neutro, prévia protegida e modo discreto.
786. Linha do tempo preserva momentos do fato, declaração, conhecimento e persistência.
787. Reconstrução retrospectiva exibe proveniência, lacunas e incerteza.
788. Calendário preserva precisão temporal e distingue previsão de ocorrência.
789. Séries e episódios mantêm identidades, participantes e estados próprios.
790. Localização é opcional, minimizada e proporcional.
791. Estados independentes não podem ser condensados em rótulo enganoso.
792. Confirmação de um participante não confirma os demais.
793. Organizações confirmam fatos institucionais, não percepção ou significado pessoal.
794. Entrega, resultado, percepção e satisfação permanecem visualmente distintos.
795. Efeitos negativos, neutros e ambivalentes permanecem registráveis.
796. Satisfação é opcional e ausência de resposta não produz inferência.
797. Evidência apresenta fonte, autoridade, escopo e limitações.
798. Memória permanece distinta de evidência e preserva autoria.
799. Significado e reflexão são opcionais e privados por padrão.
800. Experiência não confirma Evento de Vida ou transformação.
801. Relações comerciais são declaradas e não alteram ordenação funcional.
802. Publicidade permanece separada da linha do tempo funcional.
803. Todo registro oferece `Por que esta experiência está aqui?`.
804. Controles de ocultação, arquivamento, exclusão e revogação permanecem distintos.
805. Compartilhamento é granular, explicado e revogável.
806. Contestação material limita efeitos incompatíveis.
807. Correções são compensatórias, auditáveis e propagadas.
808. Revogação somente se conclui após propagação suficiente.
809. Retenção residual é explicada ao participante.
810. Busca sensível não alimenta publicidade ou perfis paralelos.
811. Canais limitados mostram menos informação, não informação incompatível.
812. Dispositivos compartilhados recebem proteção visual reforçada.
813. Operação offline distingue registro local de confirmação sincronizada.
814. Conflitos preservam versões, autoridade e histórico.
815. Retentativas não criam cartões, memórias ou compartilhamentos duplicados.
816. Inferências são identificadas, explicáveis e contestáveis.
817. Guivos Intelligence organiza e explica sem impor narrativa ou significado.
818. Produtos especializados preservam estados canônicos e controles equivalentes.
819. Métricas avaliam a interface, não o valor humano do participante.
820. `PAS-001-EXP-VIEW-001 1.0.0` eleva a Capacidade 08 para `60%`, mantém `In progress` e preserva o participante no controle.
"""
text = replace_once(
    text,
    "780. `PAS-001-EXP-LIFECYCLE-001 1.0.0` eleva a Capacidade 08 para `40%`, mantém `In progress` e preserva o participante no controle.\n\n## Documentos do domínio",
    "780. `PAS-001-EXP-LIFECYCLE-001 1.0.0` eleva a Capacidade 08 para `40%`, mantém `In progress` e preserva o participante no controle.\n" + rules + "\n## Documentos do domínio",
    f"{path}: regras",
)
text = replace_once(
    text,
    "- [PAS-001-EXP-LIFECYCLE-001 — Regras do Ciclo de Vida das Experiências](pas-001-experiencias-ciclo-de-vida.md)\n- [Guivos Journey]",
    "- [PAS-001-EXP-LIFECYCLE-001 — Regras do Ciclo de Vida das Experiências](pas-001-experiencias-ciclo-de-vida.md)\n- [PAS-001-EXP-VIEW-001 — Visualização e Controle da Capacidade de Experiências](pas-001-experiencias-visualizacao-controle.md)\n- [Guivos Journey]",
    f"{path}: link",
)
write(path, text)


# Roadmap
path = "docs/roadmap.md"
text = read(path)
text = replace_once(text, "version: 10.2.0", "version: 10.3.0", f"{path}: versão")
text = replace_once(text, "last_updated: 2026-07-16", "last_updated: 2026-07-17", f"{path}: data")
text = replace_once(text, "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 40%.", "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 60%.", f"{path}: estado")
text = replace_once(
    text,
    "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0` e `PAS-001-EXP-LIFECYCLE-001 1.0.0`.",
    "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0` e `PAS-001-EXP-VIEW-001 1.0.0`.",
    f"{path}: extensões",
)
text = replace_once(text, "O próximo trabalho deverá consolidar a visualização e o controle da `Capacidade 08 — Experiências`.", "O próximo trabalho deverá consolidar os eventos funcionais da `Capacidade 08 — Experiências`.", f"{path}: direção")
text = replace_once(
    text,
    "A Capacidade 08 está `In progress`, com progresso editorial de referência de `40%`.",
    VIEW_SUMMARY + "\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `60%`.",
    f"{path}: resumo",
)
text = text.replace("| 08 — Experiências | In progress | 40% |", "| 08 — Experiências | In progress | 60% |")
text = regex_once(
    text,
    r"## Ponto exato de retomada\n\n.*\Z",
    """## Ponto exato de retomada

Retomar nos **eventos funcionais da Capacidade 08 — Experiências**.

Próxima entrega:

1. agregado funcional principal e estrutura comum dos eventos;
2. famílias de identificação, validação, planejamento, participação, encerramento, resultados e memórias;
3. autoridade, finalidade, proveniência, sensibilidade e temporalidades;
4. eventos de visualização, controle, compartilhamento, contestação, correção e revogação;
5. idempotência, ordenação, concorrência, atomicidade e reconstrução;
6. retenção, auditoria, explicabilidade e falha segura.
""",
    f"{path}: retomada",
)
write(path, text)


# Knowledge Board
path = "docs/project/knowledge-board.md"
text = read(path)
text = replace_once(text, "version: 10.2.0", "version: 10.3.0", f"{path}: versão")
text = replace_once(text, "last_updated: 2026-07-16", "last_updated: 2026-07-17", f"{path}: data")
text = replace_once(
    text,
    "| PAS-001-EXP-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida das Experiências |",
    "| PAS-001-EXP-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida das Experiências |\n| PAS-001-EXP-VIEW-001 | Active 1.0.0 | Definir a visualização e o controle das Experiências |",
    f"{path}: ativo",
)
text = replace_once(
    text,
    "| Extensões normativas vigentes | `PAS-001-EXP-FOUNDATION-001 1.0.0` e `PAS-001-EXP-LIFECYCLE-001 1.0.0` |",
    "| Extensões normativas vigentes | `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0` e `PAS-001-EXP-VIEW-001 1.0.0` |",
    f"{path}: extensões",
)
text = replace_once(text, "| Progresso editorial de Experiências | `40%` |", "| Progresso editorial de Experiências | `60%` |", f"{path}: progresso")
text = replace_once(text, "| Foco imediato | Consolidar a visualização e o controle da Capacidade 08 — Experiências |", "| Foco imediato | Consolidar os eventos funcionais da Capacidade 08 — Experiências |", f"{path}: foco")
text = replace_once(
    text,
    "| 08 — Experiências | In progress — 40% | Fundamentos e ciclo de vida consolidados; visualização e controle são a próxima entrega |",
    "| 08 — Experiências | In progress — 60% | Fundamentos, ciclo de vida, visualização e controle consolidados; eventos funcionais são a próxima entrega |",
    f"{path}: tabela",
)
text = replace_once(
    text,
    "A Capacidade 08 está `In progress`, com progresso editorial de referência de `40%`.",
    VIEW_SUMMARY + "\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `60%`.",
    f"{path}: resumo",
)
text = text.replace("| Experiências | In progress — 40% |", "| Experiências | In progress — 60% |")
text = replace_once(
    text,
    "| Ciclo de Vida de Experiências | Normative 1.0.0 |",
    "| Ciclo de Vida de Experiências | Normative 1.0.0 |\n| Visualização e Controle de Experiências | Normative 1.0.0 |\n| Minhas Experiências | Superfície principal de compreensão, revisão e controle, distinta de feed social |\n| Privacidade visual de experiência | Títulos neutros, prévias protegidas, modo discreto, autenticação e restrição de mídias |",
    f"{path}: conceitos",
)
text = replace_once(
    text,
    "| PAS-001-EXP-LIFECYCLE-001 | Active 1.0.0 |\n| GLPA-001 |",
    "| PAS-001-EXP-LIFECYCLE-001 | Active 1.0.0 |\n| PAS-001-EXP-VIEW-001 | Active 1.0.0 |\n| GLPA-001 |",
    f"{path}: governança",
)
text = regex_once(
    text,
    r"## Próxima atividade\n\n.*\Z",
    """## Próxima atividade

Consolidar os **eventos funcionais da Capacidade 08 — Experiências**, incluindo agregado principal, estrutura comum, famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução, retenção, auditoria e falha segura.
""",
    f"{path}: próxima atividade",
)
write(path, text)


# Matriz de Consolidação Canônica
path = "docs/project/canonical-consolidation-matrix.md"
text = read(path)
text = replace_once(text, "version: 1.11.0", "version: 1.12.0", f"{path}: versão")
text = replace_once(text, "last_updated: 2026-07-16", "last_updated: 2026-07-17", f"{path}: data")
text = replace_once(
    text,
    "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos e ciclo de vida consolidados e progresso editorial de 40% |",
    "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos, ciclo de vida, visualização e controle consolidados e progresso editorial de 60% |",
    f"{path}: experiência",
)
text = replace_once(
    text,
    "| Ciclo de Vida das Experiências | Manter | PAS-001-EXP-LIFECYCLE-001 1.0.0 define dimensões independentes, estados, transições, identificação, validação da ocorrência, planejamento, participação, recorrência, resultados, memórias, correção, revogação, propagação, idempotência e falha segura |",
    "| Ciclo de Vida das Experiências | Manter | PAS-001-EXP-LIFECYCLE-001 1.0.0 define dimensões independentes, estados, transições, identificação, validação da ocorrência, planejamento, participação, recorrência, resultados, memórias, correção, revogação, propagação, idempotência e falha segura |\n| Visualização e Controle das Experiências | Manter | PAS-001-EXP-VIEW-001 1.0.0 define Minhas Experiências, áreas funcionais, cartões, linha do tempo, calendário, séries, episódios, estados independentes, privacidade, explicabilidade, compartilhamento, contestação, correção, revogação, acessibilidade e falha segura |\n| Minhas Experiências | Manter | Superfície principal de compreensão, acompanhamento, revisão e controle, distinta de feed social, mural de conquistas ou histórico comercial |\n| Privacidade visual de experiência | Manter | Títulos neutros, prévias protegidas, ocultação de participantes e localização, modo discreto, autenticação e restrição de mídias |",
    f"{path}: linhas",
)
text = replace_once(
    text,
    "As Capacidades 02, 03, 04, 05, 06 e 07 estão funcionalmente concluídas. `PAS-001-EXP-LIFECYCLE-001 1.0.0` mantém a Capacidade 08 como `In progress`, eleva o progresso editorial para 40% e consolida dimensões independentes, estados, transições, identificação, validação da ocorrência, planejamento, preparação, início, participação, recorrência, entregas, resultados, percepção, satisfação, evidências, memórias, significado, contestação, correção, revogação, propagação e consistência técnica, sem promover candidatos arquiteturais à Canon.",
    "As Capacidades 02, 03, 04, 05, 06 e 07 estão funcionalmente concluídas. `PAS-001-EXP-VIEW-001 1.0.0` mantém a Capacidade 08 como `In progress`, eleva o progresso editorial para 60% e consolida Minhas Experiências, áreas funcionais, cartões, linha do tempo, calendário, séries, episódios, estados independentes, participantes, entregas, resultados, percepção, satisfação, evidências, memórias, significado, privacidade, explicabilidade, compartilhamento, contestação, correção, revogação, acessibilidade e falha segura, sem promover candidatos arquiteturais à Canon.",
    f"{path}: reconciliação",
)
text = replace_once(
    text,
    "Consolidar a **visualização e o controle da Capacidade 08 — Experiências**, incluindo superfícies, cartões, linha do tempo, calendário, episódios, participantes, estados independentes, evidências, memórias, significado, privacidade, explicabilidade, contestação, correção, revogação, acessibilidade e falha segura.",
    "Consolidar os **eventos funcionais da Capacidade 08 — Experiências**, incluindo agregado principal, estrutura comum, famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução, retenção, auditoria e falha segura.",
    f"{path}: próxima revisão",
)
write(path, text)


# README
path = "README.md"
text = read(path)
text = text.replace("08 — Experiências, `In progress`, 40%", "08 — Experiências, `In progress`, 60%")
text = replace_once(
    text,
    "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0 e PAS-001-EXP-LIFECYCLE-001 1.0.0",
    "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0, PAS-001-EXP-LIFECYCLE-001 1.0.0 e PAS-001-EXP-VIEW-001 1.0.0",
    f"{path}: extensões",
)
text = replace_once(
    text,
    "A Capacidade 08 está **In progress**, com progresso editorial de referência de **40%**.",
    VIEW_SUMMARY + "\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de **60%**.",
    f"{path}: resumo",
)
text = regex_once(
    text,
    r"## Ponto exato de retomada\n\nRetomar na visualização e no controle da Capacidade 08 — Experiências\.\n\nPróxima entrega:\n\n.*?(?=\n## Product Engineering)",
    """## Ponto exato de retomada

Retomar nos eventos funcionais da Capacidade 08 — Experiências.

Próxima entrega:

- agregado principal e estrutura comum;
- famílias de eventos de identificação, validação, planejamento, participação, encerramento, resultados e memórias;
- autoridade, finalidade, proveniência, sensibilidade e temporalidades;
- eventos de visualização, controle, compartilhamento, contestação, correção e revogação;
- idempotência, ordenação, concorrência, atomicidade e reconstrução;
- retenção, auditoria, explicabilidade e falha segura.
""",
    f"{path}: retomada",
)
text = replace_once(
    text,
    "- [Ciclo de Vida das Experiências](docs/product-architecture/pas-001-experiencias-ciclo-de-vida.md)\n- [GLPA-001",
    "- [Ciclo de Vida das Experiências](docs/product-architecture/pas-001-experiencias-ciclo-de-vida.md)\n- [Visualização e Controle das Experiências](docs/product-architecture/pas-001-experiencias-visualizacao-controle.md)\n- [GLPA-001",
    f"{path}: link",
)
write(path, text)


# Página inicial do site
path = "docs/index.md"
text = read(path)
text = text.replace("Capacidade 08 — Experiências em desenvolvimento, `In progress`, 40%", "Capacidade 08 — Experiências em desenvolvimento, `In progress`, 60%")
text = replace_once(
    text,
    "- `PAS-001-EXP-FOUNDATION-001 1.0.0` e `PAS-001-EXP-LIFECYCLE-001 1.0.0` como extensões normativas vigentes da Capacidade 08;",
    "- `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0` e `PAS-001-EXP-VIEW-001 1.0.0` como extensões normativas vigentes da Capacidade 08;",
    f"{path}: extensões",
)
text = replace_once(text, "Consolidar a **visualização e o controle da Capacidade 08 — Experiências**.", "Consolidar os **eventos funcionais da Capacidade 08 — Experiências**.", f"{path}: missão")
text = replace_once(
    text,
    "As duas extensões de Experiências consolidam o vivido, suas distinções, titularidade, temporalidade, sensibilidade, estados, transições, validação da ocorrência, recorrência, resultados, memórias, correção, revogação e falha segura.",
    "As três extensões de Experiências consolidam o vivido, suas distinções, titularidade, ciclo de vida, Minhas Experiências, áreas funcionais, cartões, linha do tempo, calendário, séries, episódios, estados independentes, privacidade, explicabilidade, compartilhamento, correção, revogação e falha segura.",
    f"{path}: resumo",
)
text = replace_once(
    text,
    "- [Ciclo de Vida das Experiências](product-architecture/pas-001-experiencias-ciclo-de-vida.md)\n- [GLPA-001]",
    "- [Ciclo de Vida das Experiências](product-architecture/pas-001-experiencias-ciclo-de-vida.md)\n- [Visualização e Controle das Experiências](product-architecture/pas-001-experiencias-visualizacao-controle.md)\n- [GLPA-001]",
    f"{path}: link",
)
text = text.replace("| 08 — Experiências | In progress — 40% |", "| 08 — Experiências | In progress — 60% |")
text = replace_once(
    text,
    "Retomar na visualização e no controle da Capacidade 08 — Experiências, incluindo superfícies, cartões, linha do tempo, calendário, séries, episódios, participantes, estados independentes, evidências, memórias, significado, privacidade, explicabilidade, contestação, correção, revogação, acessibilidade e falha segura.",
    "Retomar nos eventos funcionais da Capacidade 08 — Experiências, incluindo agregado principal, estrutura comum, famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução, retenção, auditoria e falha segura.",
    f"{path}: retomada",
)
write(path, text)


# Navegação
path = "mkdocs.yml"
text = read(path)
text = replace_once(
    text,
    "      - PAS-001-EXP-LIFECYCLE-001 — Ciclo de Vida das Experiências: product-architecture/pas-001-experiencias-ciclo-de-vida.md\n      - Guivos Journey:",
    "      - PAS-001-EXP-LIFECYCLE-001 — Ciclo de Vida das Experiências: product-architecture/pas-001-experiencias-ciclo-de-vida.md\n      - PAS-001-EXP-VIEW-001 — Visualização e Controle das Experiências: product-architecture/pas-001-experiencias-visualizacao-controle.md\n      - Guivos Journey:",
    f"{path}: navegação",
)
write(path, text)


# Changelog
path = "CHANGELOG.md"
text = read(path)
entry = """## 0.40.0 — Experiences Visualization and Control

- Criação de `PAS-001-EXP-VIEW-001 — Visualização e Controle da Capacidade de Experiências`, versão `1.0.0`.
- Registro do documento como terceira extensão normativa da Capacidade 08 do `PAS-001 — Guivos Journey`.
- Manutenção da Capacidade 08 como `In progress` e elevação do progresso editorial de 40% para 60%.
- Consolidação de `Minhas Experiências` como superfície principal de compreensão, acompanhamento, revisão e controle.
- Definição das áreas Agora, Próximas, Linha do tempo, Séries e episódios, Para validar e Arquivo.
- Consolidação dos modos lista, cartões, linha do tempo, calendário, séries, episódios e mapa opcional.
- Definição de títulos funcionais, títulos neutros, privacidade visual, conteúdo sensível e detalhamento progressivo.
- Representação separada dos estados funcionais, ocorrência, temporalidade, relação individual, presença, participação, envolvimento, entrega, resultado, percepção, satisfação, evidências, memória, significado, autorização, contestação e propagação.
- Consolidação das experiências compartilhadas, coletivas e institucionais com proteção de terceiros e autoridade limitada.
- Separação visual entre entrega, resultado, efeitos, percepção, satisfação, evidência, memória, significado, Evento de Vida e transformação.
- Definição de explicabilidade por `Por que esta experiência está aqui?` e `Como este registro foi reconstruído?`.
- Consolidação de controles de confirmação, negação, incerteza, visibilidade, ocultação, arquivamento, compartilhamento, contestação, correção, revogação, exportação e exclusão.
- Definição de busca, filtros e ordenação neutra sem utilização de comissão, patrocínio, popularidade ou tempo de tela.
- Consolidação de acessibilidade técnica e cognitiva, consistência entre canais, interface conversacional e proteção de dispositivos compartilhados.
- Definição de operação offline, conflitos, idempotência visual, auditoria, explicabilidade de inferências e falha segura.
- Registro de 30 comportamentos proibidos e 70 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.12.0` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap e do Knowledge Board para `10.3.0`.
- Atualização da Matriz de Consolidação Canônica para `1.12.0`.
- Atualização do README e da página inicial do GKR.
- Preservação das Capacidades 02, 03, 04, 05, 06 e 07 como `Functionally complete`.
- Preservação da Capacidade 09 — Evolução Contínua como `Planned`.
- Definição dos eventos funcionais de Experiências como próximo ponto exato de retomada.

"""
text = replace_once(text, "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n", "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n" + entry, f"{path}: entrada")
write(path, text)

print("Sincronização de PAS-001-EXP-VIEW-001 concluída.")
