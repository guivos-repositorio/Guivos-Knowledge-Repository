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
        "- **Próxima capacidade:** 08 — Experiências, `Planned`, 0%",
        "- **Capacidade ativa:** 08 — Experiências, `In progress`, 20%",
        "README active capability",
    )
    text = replace_once(
        text,
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001, PAS-001-IC-VIEW-001, PAS-001-IC-EVENT-001, PAS-001-IC-INTEGRATION-001 e PAS-001-IC-CONTRACT-001, todas em 1.0.0",
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001, PAS-001-IC-VIEW-001, PAS-001-IC-EVENT-001, PAS-001-IC-INTEGRATION-001 e PAS-001-IC-CONTRACT-001, todas em 1.0.0\n- **Extensão vigente de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0",
        "README experience extension",
    )
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*?\n## Product Engineering",
        """## Capacidade 08 — Experiências

`PAS-001-EXP-FOUNDATION-001 1.0.0` consolida:

- finalidade, pergunta central, singularidade e valor entregue;
- Experiência como vivência efetivamente situada no tempo;
- distinções entre atividade, presença, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida;
- `Registro de Experiência` como unidade funcional;
- identidade, titularidade, participantes, papéis e autoridade;
- experiências compartilhadas, coletivas, institucionais, físicas, digitais e híbridas;
- origem, intenção, candidatura e reconhecimento da ocorrência;
- temporalidades, duração, intensidade, recorrência, episódios e continuidade;
- presença, envolvimento, agência, autonomia e expectativas;
- contexto mínimo, sensibilidade, privacidade, acessibilidade, segurança e proteção de terceiros;
- entregas, resultados, satisfação, evidências, memórias, significado e reflexão;
- limites para transformação, Eventos de Vida e Evolução Contínua;
- relações com as capacidades do Journey, Guivos Intelligence, Platform Layer, produtos, organizações e profissionais;
- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades, limites e comportamentos proibidos.

A Capacidade 08 está **In progress**, com progresso editorial de referência de **20%**.

## Ponto exato de retomada

Retomar nas regras do ciclo de vida da Capacidade 08 — Experiências.

Próxima entrega:

- identificação, candidatura e validação da ocorrência;
- planejamento, preparação, prontidão e início;
- presença, participação, envolvimento e acompanhamento;
- pausa, retomada, conclusão, interrupção, cancelamento e expiração;
- recorrência, séries, episódios e continuidade;
- entregas, resultados, percepções e satisfação;
- evidências, memórias, significado e reflexão;
- contestação, correção, revogação e propagação;
- ordenação, concorrência, reconstrução e falha segura.

## Product Engineering""",
        "README resumption",
    )
    text = text.replace(
        "As Capacidades 06 — Oportunidades Ativas e 07 — Intervenções Contextuais estão `Functionally complete`; a Capacidade 08 — Experiências permanece `Planned`.",
        "As Capacidades 06 — Oportunidades Ativas e 07 — Intervenções Contextuais estão `Functionally complete`; a Capacidade 08 — Experiências está `In progress`, com progresso editorial de referência de `20%`.",
    )
    text = text.replace(
        "| 08 — Experiências | Planned |",
        "| 08 — Experiências | In progress — 20% |",
    )
    text = replace_once(
        text,
        "- [Contrato Final das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)",
        "- [Contrato Final das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)\n- [Fundamentos Iniciais de Experiências](docs/product-architecture/pas-001-experiencias-fundamentos-iniciais.md)",
        "README experience link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(readme): iniciar Capacidade de Experiências")


def update_home() -> None:
    path = Path("docs/index.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "- Capacidade 08 — Experiências preservada como `Planned`, 0%;",
        "- Capacidade 08 — Experiências em desenvolvimento, `In progress`, 20%;",
    )
    text = replace_once(
        text,
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0`, `PAS-001-IC-INTEGRATION-001 1.0.0` e `PAS-001-IC-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0`, `PAS-001-IC-INTEGRATION-001 1.0.0` e `PAS-001-IC-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 07;\n- `PAS-001-EXP-FOUNDATION-001 1.0.0` como primeira extensão normativa da Capacidade 08;",
        "home extension",
    )
    text = text.replace(
        "Consolidar os **fundamentos iniciais da Capacidade 08 — Experiências**.",
        "Consolidar as **regras do ciclo de vida da Capacidade 08 — Experiências**.",
    )
    text = text.replace(
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final.",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final. A primeira extensão de Experiências consolida o vivido, suas distinções, titularidade, temporalidade, sensibilidade, relações, estados e limites iniciais.",
    )
    text = replace_once(
        text,
        "- [Contrato Final das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)",
        "- [Contrato Final das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)\n- [Fundamentos Iniciais de Experiências](product-architecture/pas-001-experiencias-fundamentos-iniciais.md)",
        "home link",
    )
    text = text.replace(
        "| 08 — Experiências | Planned |",
        "| 08 — Experiências | In progress — 20% |",
    )
    text = replace_once(
        text,
        "Retomar nos fundamentos iniciais da Capacidade 08 — Experiências, incluindo singularidade, definição da experiência vivida, distinção entre atividade, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida, além de titularidade, temporalidade, sensibilidade, relações, estados, limites e integrações iniciais. A capacidade permanece `Planned` até a aprovação de sua primeira extensão normativa.",
        "Retomar nas regras do ciclo de vida da Capacidade 08 — Experiências, incluindo identificação, candidatura, validação da ocorrência, planejamento, preparação, início, participação, acompanhamento, pausa, retomada, conclusão, interrupção, cancelamento, recorrência, episódios, entrega, resultado, percepção, satisfação, evidência, memória, significado, contestação, correção, revogação, propagação e falha segura.",
        "home resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(index): iniciar Capacidade de Experiências")


def update_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.9.0", "version: 1.10.0", "architecture version")
    marker = """A Capacidade 07 está **Functionally complete**, com progresso editorial de referência de `100%`.

O próximo bloco deverá consolidar os fundamentos iniciais da Capacidade 08 — Experiências, que permanece `Planned` até a aprovação de sua primeira extensão normativa."""
    addition = """A Capacidade 07 está **Functionally complete**, com progresso editorial de referência de `100%`.

## Capacidade 08 ativa

### Capacidade 08 — Experiências

A extensão normativa vigente é:

- `PAS-001-EXP-FOUNDATION-001 1.0.0` — finalidade, pergunta central, definição canônica, singularidade, distinções, Registro de Experiência, titularidade, participantes, temporalidades, sensibilidade, entregas, resultados, evidências, memórias, significado, relações, estados, eventos, controles e limites iniciais.

Os fundamentos consolidam:

- Experiência como vivência efetivamente situada no tempo;
- distinção entre atividade, presença, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida;
- `Registro de Experiência` como unidade funcional;
- identidade, titularidade, papéis e autoridade;
- experiências compartilhadas, coletivas, institucionais, físicas, digitais e híbridas;
- origem, intenção, candidatura e validação proporcional da ocorrência;
- temporalidades, duração, intensidade, recorrência, episódios e continuidade;
- presença, envolvimento, agência, autonomia e expectativas;
- contexto mínimo, sensibilidade, privacidade, acessibilidade, segurança e proteção de terceiros;
- entregas, resultados, satisfação, evidências, memórias, significado e reflexão;
- limites para transformação, Eventos de Vida e Evolução Contínua;
- relações com as capacidades do Journey, Intelligence, Platform Layer, produtos, organizações e profissionais;
- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e comportamentos proibidos.

A Capacidade 08 está **In progress**, com progresso editorial de referência de `20%`.

O próximo bloco deverá consolidar as regras do ciclo de vida das Experiências."""
    text = replace_once(text, marker, addition, "architecture experience section")
    rules_marker = "690. `PAS-001-IC-CONTRACT-001 1.0.0` conclui funcionalmente a Capacidade 07, com progresso editorial de referência de `100%`, e o participante permanece no controle.\n\n## Documentos do domínio"
    rules = """690. `PAS-001-IC-CONTRACT-001 1.0.0` conclui funcionalmente a Capacidade 07, com progresso editorial de referência de `100%`, e o participante permanece no controle.
691. Experiência representa o vivido, não a atividade prevista ou a transação.
692. Compra, reserva, contratação, entrega e presença não comprovam experiência concluída.
693. Atividade, presença, participação, percepção, resultado, satisfação, memória, significado e transformação permanecem distintos.
694. Uma atividade pode produzir experiências diferentes para participantes diferentes.
695. Participação não comprova percepção, aprendizagem, satisfação ou transformação.
696. Entrega não representa utilização, benefício, resultado ou experiência positiva.
697. Resultado não esgota a experiência.
698. Satisfação não representa benefício objetivo, segurança ou transformação.
699. Evidência sustenta afirmações, mas não representa a experiência integral.
700. Memória é revisável e não constitui reprodução exata e imutável do ocorrido.
701. Significado pertence ao participante ou coletivo autorizado e não pode ser imposto.
702. Experiência não representa transformação automaticamente.
703. Experiência somente origina Evento de Vida após avaliação própria da capacidade competente.
704. Objetivos governam progresso, prioridade, revisão e conclusão.
705. Próximos Passos governam movimentos e não são concluídos pela experiência.
706. Oportunidade, interesse, inscrição, contratação, participação e experiência permanecem distintos.
707. Intervenções Contextuais pode apoiar, mas não declarar a vivência sem fundamento.
708. Consumo de conteúdo não comprova atenção, compreensão, aprendizagem ou aplicação.
709. Produto executor governa transação, entrega, atendimento e operação.
710. O Registro de Experiência preserva identidade, contexto, temporalidades, participantes, percepções, resultados, evidências, memórias, significados, correções e permissões.
711. Mudança material pode exigir novo episódio, ciclo ou Registro de Experiência.
712. A experiência pertence a quem a viveu; pagamento, patrocínio ou registro técnico não transferem titularidade.
713. Experiências compartilhadas preservam percepções, memórias e significados individuais.
714. Registros coletivos não substituem registros pessoais.
715. Organizações confirmam fatos institucionais, não percepção ou transformação pessoal.
716. Modalidade física, digital ou híbrida não determina intensidade, qualidade ou significado.
717. Classificações de experiência são funcionais e não avaliativas.
718. Origem não representa autoria total ou controle sobre a experiência.
719. Experiências involuntárias exigem proteção reforçada.
720. Convite, inscrição, presença confirmada e experiência iniciada permanecem distintos.
721. Candidatura de experiência não representa ocorrência confirmada.
722. Ocorrência deve preservar incerteza quando as evidências forem insuficientes.
723. Momentos previsto, inicial, de participação, percepção, encerramento, resultado, memória e significado permanecem distintos.
724. Duração não representa intensidade, qualidade ou significado.
725. Intensidade não representa valor, impacto ou transformação.
726. Recorrência não comprova hábito, compromisso, identidade ou evolução.
727. Baixa autonomia limita inferências e automações.
728. Contexto utilizado deve ser mínimo, autorizado e proporcional.
729. Experiências sensíveis exigem privacidade, minimização e proteção de terceiros.
730. Relações comerciais não alteram a interpretação do vivido nem fabricam transformação.
731. Guivos Intelligence organiza e propõe, mas não impõe significado, emoção ou transformação.
732. `PAS-001-EXP-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 08, com progresso editorial de referência de `20%`, e o participante permanece no controle.

## Documentos do domínio"""
    text = replace_once(text, rules_marker, rules, "architecture experience rules")
    text = replace_once(
        text,
        "- [PAS-001-IC-CONTRACT-001 — Contrato Final das Intervenções Contextuais](pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)",
        "- [PAS-001-IC-CONTRACT-001 — Contrato Final das Intervenções Contextuais](pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)\n- [PAS-001-EXP-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Experiências](pas-001-experiencias-fundamentos-iniciais.md)",
        "architecture link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(arquitetura): iniciar Capacidade de Experiências")


def update_roadmap() -> None:
    path = Path("docs/roadmap.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 10.0.0", "version: 10.1.0", "roadmap version")
    text = replace_once(
        text,
        "- **Próxima capacidade:** `08 — Experiências`, `Planned`, 0%.",
        "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 20%.",
        "roadmap active capability",
    )
    text = replace_once(
        text,
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0`, `PAS-001-IC-INTEGRATION-001 1.0.0` e `PAS-001-IC-CONTRACT-001 1.0.0`.",
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0`, `PAS-001-IC-INTEGRATION-001 1.0.0` e `PAS-001-IC-CONTRACT-001 1.0.0`.\n- **Extensão normativa vigente de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`.",
        "roadmap extension",
    )
    text = replace_once(
        text,
        "O próximo trabalho deverá consolidar os fundamentos iniciais da `Capacidade 08 — Experiências`, preservada como `Planned` até a aprovação de sua primeira extensão normativa.",
        "O próximo trabalho deverá consolidar as regras do ciclo de vida da `Capacidade 08 — Experiências`.",
        "roadmap direction",
    )
    marker = """A Capacidade 07 está `Functionally complete`, com progresso editorial de referência de `100%`.

## Progresso das capacidades do Journey"""
    addition = """A Capacidade 07 está `Functionally complete`, com progresso editorial de referência de `100%`.

## Capacidade 08 ativa

### Capacidade 08 — Experiências

`PAS-001-EXP-FOUNDATION-001 1.0.0` consolida:

- finalidade, pergunta central, definição canônica, singularidade e valor entregue;
- Experiência como vivência efetivamente situada no tempo;
- distinções entre atividade, presença, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida;
- Registro de Experiência, identidade, titularidade, participantes, papéis e autoridade;
- experiências compartilhadas, coletivas, institucionais, físicas, digitais e híbridas;
- origem, intenção, candidatura e validação da ocorrência;
- temporalidades, duração, intensidade, recorrência, episódios e continuidade;
- presença, envolvimento, agência, autonomia e expectativas;
- contexto, sensibilidade, privacidade, acessibilidade, segurança e terceiros;
- entregas, resultados, satisfação, evidências, memórias, significado e reflexão;
- relações com todas as capacidades do Journey;
- limites da Intelligence, Platform Layer, produtos, organizações e profissionais;
- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e limites.

A Capacidade 08 está `In progress`, com progresso editorial de referência de `20%`.

## Progresso das capacidades do Journey"""
    text = replace_once(text, marker, addition, "roadmap experience section")
    text = text.replace(
        "| 08 — Experiências | Planned | 0% |",
        "| 08 — Experiências | In progress | 20% |",
    )
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*\Z",
        """## Ponto exato de retomada

Retomar nas **regras do ciclo de vida da Capacidade 08 — Experiências**.

Próxima entrega:

1. dimensões independentes do ciclo de vida;
2. identificação, candidatura e validação da ocorrência;
3. planejamento, preparação, prontidão e início;
4. presença, participação, envolvimento e acompanhamento;
5. pausa, retomada, conclusão, interrupção, cancelamento e expiração;
6. recorrência, séries, episódios e continuidade;
7. entregas, resultados, percepções e satisfação;
8. evidências, memórias, significado e reflexão;
9. contestação, correção, revogação e propagação;
10. idempotência, ordenação, concorrência, reconstrução e falha segura.
""",
        "roadmap resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(roadmap): iniciar Capacidade de Experiências")


def update_board() -> None:
    path = Path("docs/project/knowledge-board.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 10.0.0", "version: 10.1.0", "board version")
    text = replace_once(
        text,
        "| PAS-001-IC-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Intervenções Contextuais |",
        "| PAS-001-IC-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Intervenções Contextuais |\n| PAS-001-EXP-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais da Capacidade de Experiências |",
        "board asset",
    )
    text = text.replace(
        "| Próxima capacidade | `08 — Experiências` |\n| Estado da próxima capacidade | `Planned` |\n| Extensão normativa vigente | `PAS-001-IC-CONTRACT-001 1.0.0` |\n| Progresso editorial de Intervenções Contextuais | `100%` |",
        "| Capacidade ativa | `08 — Experiências` |\n| Estado da capacidade ativa | `In progress` |\n| Extensão normativa vigente | `PAS-001-EXP-FOUNDATION-001 1.0.0` |\n| Progresso editorial de Experiências | `20%` |",
    )
    text = text.replace(
        "| Foco imediato | Consolidar os fundamentos iniciais da Capacidade 08 — Experiências |",
        "| Foco imediato | Consolidar as regras do ciclo de vida da Capacidade 08 — Experiências |",
    )
    text = text.replace(
        "| 08 — Experiências | Planned | — |",
        "| 08 — Experiências | In progress — 20% | Fundamentos iniciais consolidados; ciclo de vida é a próxima entrega |",
    )
    marker = """A Capacidade 07 está `Functionally complete`, com progresso editorial de referência de `100%`.

## Conceitos internos preservados"""
    addition = """A Capacidade 07 está `Functionally complete`, com progresso editorial de referência de `100%`.

## Consolidação inicial da Capacidade 08 — Experiências

### Fundamentos iniciais

- pergunta central sobre o que foi efetivamente vivido, em qual contexto e com qual forma de participação;
- singularidade centrada no vivido e na distinção entre ocorrência, percepção, resultado, memória, significado e transformação;
- Experiência definida como vivência efetivamente situada no tempo;
- distinção entre atividade, presença, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida;
- Registro de Experiência como unidade funcional;
- identidade, titularidade, participantes, papéis e autoridade;
- experiências compartilhadas, coletivas, institucionais, físicas, digitais e híbridas;
- tipos, origem, intenção, convite, inscrição, candidatura e validação da ocorrência;
- temporalidades, início, encerramento, duração, intensidade, recorrência, episódios e continuidade;
- presença, envolvimento, agência, autonomia e expectativas;
- contexto mínimo, sensibilidade, privacidade, acessibilidade, segurança e proteção de terceiros;
- entregas, resultados, satisfação, evidências, memórias, significado e reflexão;
- relações com Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Intervenções Contextuais e Evolução Contínua;
- limites da Guivos Intelligence, Platform Layer, produtos especializados, organizações e profissionais;
- neutralidade comercial, estados, eventos, controles, explicabilidade, responsabilidades e comportamentos proibidos.

A Capacidade 08 está `In progress`, com progresso editorial de referência de `20%`.

## Conceitos internos preservados"""
    text = replace_once(text, marker, addition, "board experience section")
    text = replace_once(
        text,
        "| Intervenções Contextuais | Functionally complete — 100% |",
        "| Intervenções Contextuais | Functionally complete — 100% |\n| Experiências | In progress — 20% |\n| Fundamentos de Experiências | Normative 1.0.0 |\n| Registro de Experiência | Agregado que preserva identidade, contexto, temporalidades, participantes, percepções, resultados, evidências, memórias, significados, correções e permissões |\n| Experiência | Vivência efetivamente situada no tempo; distinta de atividade, presença, participação, entrega, resultado e transformação |\n| Significado da experiência | Interpretação opcional, pessoal ou coletiva autorizada, revisável e não imposta |",
        "board concepts",
    )
    text = text.replace("| Roadmap | 10.0.0 |", "| Roadmap | 10.1.0 |")
    text = text.replace("| Knowledge Board | 10.0.0 |", "| Knowledge Board | 10.1.0 |")
    text = replace_once(
        text,
        "| PAS-001-IC-CONTRACT-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-IC-CONTRACT-001 | Active 1.0.0 |\n| PAS-001-EXP-FOUNDATION-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "board governance",
    )
    text = replace_once(
        text,
        "Consolidar os **fundamentos iniciais da Capacidade 08 — Experiências**, incluindo singularidade, experiência vivida, distinções fundamentais, titularidade, temporalidade, sensibilidade, relações, estados, limites e integrações iniciais. A capacidade permanece `Planned` até a aprovação de sua primeira extensão normativa.",
        "Consolidar as **regras do ciclo de vida da Capacidade 08 — Experiências**, incluindo identificação, candidatura, validação da ocorrência, planejamento, preparação, início, participação, acompanhamento, pausa, retomada, conclusão, interrupção, cancelamento, recorrência, episódios, entrega, resultado, percepção, satisfação, evidência, memória, significado, contestação, correção, revogação, propagação e falha segura.",
        "board next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(board): registrar fundamentos de Experiências")


def update_matrix() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.9.0", "version: 1.10.0", "matrix version")
    marker = "| KPIs, Guardrails, Cenários e Contrato Final das Intervenções Contextuais | Manter | PAS-001-IC-CONTRACT-001 1.0.0 define 80 KPIs, 16 famílias, 28 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas, reabertura e contrato final |"
    rows = marker + """
| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos iniciais consolidados e progresso editorial de 20% |
| Fundamentos Iniciais da Capacidade de Experiências | Manter | PAS-001-EXP-FOUNDATION-001 1.0.0 define finalidade, pergunta central, singularidade, distinções, titularidade, temporalidade, sensibilidade, relações, estados, eventos, controles e limites iniciais |
| Experiência | Refinar | Vivência efetivamente situada no tempo; distinta de atividade, presença, participação, entrega, resultado, satisfação, memória, significado e transformação |
| Registro de Experiência | Manter | Agregado funcional que preserva identidade, contexto, temporalidades, participantes, entregas, resultados, percepções, evidências, memórias, significados, correções e permissões |
| Titularidade da experiência | Manter | Pertence a quem viveu; pagamento, patrocínio, organização, fornecimento ou registro técnico não transferem titularidade |
| Experiência e transformação | Refinar | Experiência pode contribuir para transformação, mas não a confirma automaticamente |
| Significado da experiência | Manter | Interpretação opcional, revisável e atribuída pelo participante ou coletivo autorizado |
| Memória da experiência | Refinar | Representação preservada ou reconstruída, distinta da reprodução exata do ocorrido |"""
    text = replace_once(text, marker, rows, "matrix experience rows")
    text = replace_regex(
        text,
        r"## Reconciliação mais recente\n.*?\n## Próxima revisão",
        """## Reconciliação mais recente

As Capacidades 02, 03, 04, 05, 06 e 07 estão funcionalmente concluídas. `PAS-001-EXP-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 08, substitui seu estado `Planned` por `In progress`, estabelece progresso editorial de 20% e consolida a experiência vivida, distinções fundamentais, Registro de Experiência, titularidade, participantes, temporalidades, sensibilidade, entregas, resultados, evidências, memórias, significado, relações, estados, eventos, controles e limites iniciais, sem promover candidatos arquiteturais à Canon.

## Próxima revisão""",
        "matrix reconciliation",
    )
    text = replace_regex(
        text,
        r"## Próxima revisão\n.*\Z",
        """## Próxima revisão

Consolidar as **regras do ciclo de vida da Capacidade 08 — Experiências**, incluindo identificação, candidatura, validação da ocorrência, planejamento, preparação, início, participação, acompanhamento, pausa, retomada, conclusão, interrupção, cancelamento, recorrência, episódios, entrega, resultado, percepção, satisfação, evidência, memória, significado, contestação, correção, revogação, propagação e falha segura.
""",
        "matrix next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(canon): consolidar fundamentos de Experiências")


def update_mkdocs() -> None:
    path = Path("mkdocs.yml")
    text = path.read_text(encoding="utf-8")
    marker = "      - PAS-001-IC-CONTRACT-001 — Contrato Final das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md"
    text = replace_once(
        text,
        marker,
        marker + "\n      - PAS-001-EXP-FOUNDATION-001 — Fundamentos de Experiências: product-architecture/pas-001-experiencias-fundamentos-iniciais.md",
        "mkdocs experience nav",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(site): adicionar fundamentos de Experiências")


def update_changelog() -> None:
    path = Path("CHANGELOG.md")
    text = path.read_text(encoding="utf-8")
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    entry = """## 0.38.0 — Experiences Initial Foundations

- Criação de `PAS-001-EXP-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Experiências`, versão `1.0.0`.
- Registro do documento como primeira extensão normativa da Capacidade 08 do `PAS-001 — Guivos Journey`.
- Substituição do estado da Capacidade 08 de `Planned` por `In progress` e estabelecimento do progresso editorial inicial de 20%.
- Definição da finalidade, pergunta central, singularidade e valor entregue pela capacidade.
- Definição canônica de Experiência como vivência efetivamente situada no tempo.
- Distinção entre experiência, atividade, presença, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação, Evento de Vida, progresso e evolução.
- Definição do fluxo canônico inicial e do `Registro de Experiência` como unidade funcional.
- Consolidação de identidade, titularidade, participantes, papéis e autoridade.
- Definição das experiências compartilhadas, coletivas, institucionais, físicas, digitais e híbridas.
- Consolidação de tipos, origem, intenção, convite, inscrição, candidatura e reconhecimento da ocorrência.
- Definição das temporalidades de previsão, início, participação, ocorrência, percepção, encerramento, resultado, registro, memória, significado, correção e revogação.
- Consolidação de duração, intensidade, recorrência, episódios, continuidade, presença, envolvimento, agência, autonomia e expectativas.
- Definição de contexto mínimo, sensibilidade, privacidade, acessibilidade, segurança e proteção de terceiros.
- Consolidação de entregas, resultados, satisfação, evidências, memórias, significado e reflexão.
- Limitação da transformação, de Eventos de Vida e de Evolução Contínua a avaliações próprias das capacidades competentes.
- Consolidação das relações com Objetivos, Próximos Passos, Oportunidades Ativas e Intervenções Contextuais.
- Definição dos limites da Guivos Intelligence, da Platform Layer, dos produtos especializados, das organizações e dos profissionais.
- Preservação da neutralidade comercial e proibição de utilização de experiências sensíveis para publicidade ou engajamento.
- Registro dos estados funcionais, estado da informação, relação individual, eventos iniciais, controles, explicabilidade, responsabilidades e limites.
- Registro de 25 comportamentos proibidos e 42 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.10.0` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap e do Knowledge Board para `10.1.0`.
- Atualização da Matriz de Consolidação Canônica para `1.10.0`.
- Atualização do README e da página inicial do GKR.
- Preservação das Capacidades 02, 03, 04, 05, 06 e 07 como `Functionally complete`.
- Preservação da Capacidade 09 — Evolução Contínua como `Planned`.
- Definição das regras do ciclo de vida de Experiências como próximo ponto exato de retomada.

"""
    text = replace_once(text, marker, marker + entry, "changelog header")
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(changelog): registrar fundamentos de Experiências")


def validate() -> None:
    normative = Path("docs/product-architecture/pas-001-experiencias-fundamentos-iniciais.md").read_text(encoding="utf-8")
    checks = {
        "normative start": "# 3366. Finalidade da capacidade" in normative,
        "normative end": "# 3452. Critérios de aceite e continuidade" in normative,
        "no generated ids": 'id="' not in normative,
        "active 20 README": "Capacidade ativa:** 08 — Experiências, `In progress`, 20%" in Path("README.md").read_text(encoding="utf-8"),
        "home 20": "Experiências | In progress — 20%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.10.0" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 10.1.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 10.1.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.10.0" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "nav": "pas-001-experiencias-fundamentos-iniciais.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.38.0 — Experiences Initial Foundations" in Path("CHANGELOG.md").read_text(encoding="utf-8"),
        "next lifecycle": "regras do ciclo de vida" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validation failed: " + ", ".join(failed))
    run("git", "diff", "--check")


def main() -> None:
    update_readme()
    update_home()
    update_architecture()
    update_roadmap()
    update_board()
    update_matrix()
    update_mkdocs()
    update_changelog()
    validate()
    branch = os.environ["GITHUB_REF_NAME"]
    run("git", "push", "origin", f"HEAD:{branch}")


if __name__ == "__main__":
    main()
