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
        "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos e 06 — Oportunidades Ativas",
        "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas e 07 — Intervenções Contextuais",
        "README completed capabilities",
    )
    text = replace_once(
        text,
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 90%",
        "- **Próxima capacidade:** 08 — Experiências, `Planned`, 0%",
        "README next capability",
    )
    text = replace_once(
        text,
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001, PAS-001-IC-VIEW-001, PAS-001-IC-EVENT-001 e PAS-001-IC-INTEGRATION-001, todas em 1.0.0",
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001, PAS-001-IC-VIEW-001, PAS-001-IC-EVENT-001, PAS-001-IC-INTEGRATION-001 e PAS-001-IC-CONTRACT-001, todas em 1.0.0",
        "README extensions",
    )
    marker = """- proteção de terceiros, coletivos, dispositivos compartilhados e integrações temporárias;
- observabilidade, explicabilidade, auditoria e reconstrução.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **90%**."""
    addition = """- proteção de terceiros, coletivos, dispositivos compartilhados e integrações temporárias;
- observabilidade, explicabilidade, auditoria e reconstrução.

`PAS-001-IC-CONTRACT-001 1.0.0` consolida:

- 80 KPIs em 16 famílias de indicadores sistêmicos;
- baseline funcional segmentada antes de metas permanentes;
- painel de saúde com 17 visões e cinco níveis de desempenho;
- 28 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- critérios de conclusão, lacunas bloqueantes e não bloqueantes;
- contrato final de singularidade, titularidade, responsabilidades, limites, entradas, admissão e saídas;
- silêncio como resultado funcional legítimo;
- atenção e interruptibilidade como dimensões distintas de consentimento;
- importância, urgência e temporalidade separadas;
- sensibilidade, privacidade, fadiga, frequência, canais e autonomia;
- neutralidade comercial, proteção de terceiros e separação de Guivos Ads;
- confiabilidade, correção, revogação, explicabilidade, auditoria e critérios de reabertura.

A Capacidade 07 está **Functionally complete**, com progresso editorial de referência de **100%**."""
    text = replace_once(text, marker, addition, "README contract section")
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*?\n## Product Engineering",
        """## Ponto exato de retomada

Retomar nos fundamentos iniciais da Capacidade 08 — Experiências.

Próxima entrega:

- finalidade e pergunta central da capacidade;
- singularidade da experiência vivida;
- distinção entre atividade, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida;
- titularidade, participantes, papéis e autoridade;
- temporalidade, duração, intensidade e recorrência;
- sensibilidade, privacidade e informações de terceiros;
- relações com Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas e Intervenções Contextuais;
- estados, transições, responsabilidades, limites e comportamentos proibidos iniciais.

A Capacidade 08 permanece `Planned` até a aprovação de sua primeira extensão normativa.

## Product Engineering""",
        "README resumption",
    )
    text = text.replace(
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `90%`.",
        "As Capacidades 06 — Oportunidades Ativas e 07 — Intervenções Contextuais estão `Functionally complete`; a Capacidade 08 — Experiências permanece `Planned`.",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 90% |",
        "| 07 — Intervenções Contextuais | Functionally complete — 100% |",
    )
    text = replace_once(
        text,
        "- [Integrações Funcionais das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-integracoes-funcionais.md)",
        "- [Integrações Funcionais das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-integracoes-funcionais.md)\n- [Contrato Final das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)",
        "README contract link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(readme): concluir Intervenções Contextuais")


def update_home() -> None:
    path = Path("docs/index.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida e 05 — Próximos Passos funcionalmente concluídas;",
        "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas e 07 — Intervenções Contextuais funcionalmente concluídas;",
    )
    text = text.replace(
        "- Capacidade 06 — Oportunidades Ativas funcionalmente concluída, `Functionally complete`, 100%;\n- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 90%;",
        "- Capacidade 06 — Oportunidades Ativas funcionalmente concluída, `Functionally complete`, 100%;\n- Capacidade 07 — Intervenções Contextuais funcionalmente concluída, `Functionally complete`, 100%;\n- Capacidade 08 — Experiências preservada como `Planned`, 0%;",
    )
    text = text.replace(
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0` e `PAS-001-IC-INTEGRATION-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0`, `PAS-001-IC-INTEGRATION-001 1.0.0` e `PAS-001-IC-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
    )
    text = text.replace(
        "Consolidar os **KPIs, guardrails, cenários e contrato final da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar os **fundamentos iniciais da Capacidade 08 — Experiências**.",
    )
    text = text.replace(
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As cinco extensões de Intervenções Contextuais consolidam fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos e integrações funcionais com capacidades, produtos, organizações, profissionais, canais e sistemas externos, preservando finalidade, autoridade, minimização, neutralidade, revogação e falha segura.",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final.",
    )
    text = replace_once(
        text,
        "- [Integrações Funcionais das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-integracoes-funcionais.md)",
        "- [Integrações Funcionais das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-integracoes-funcionais.md)\n- [Contrato Final das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)",
        "home contract link",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 90% |",
        "| 07 — Intervenções Contextuais | Functionally complete — 100% |",
    )
    text = replace_once(
        text,
        "Retomar nos KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão, lacunas bloqueantes e não bloqueantes, critérios de reabertura e contrato final da Capacidade 07 — Intervenções Contextuais.",
        "Retomar nos fundamentos iniciais da Capacidade 08 — Experiências, incluindo singularidade, definição da experiência vivida, distinção entre atividade, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida, além de titularidade, temporalidade, sensibilidade, relações, estados, limites e integrações iniciais. A capacidade permanece `Planned` até a aprovação de sua primeira extensão normativa.",
        "home resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(index): concluir Intervenções Contextuais")


def update_product_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.4", "version: 1.9.0", "architecture version")
    text = replace_once(
        text,
        "- `PAS-001-IC-INTEGRATION-001 1.0.0` — contrato comum, titularidade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, canais, observabilidade e falha segura.",
        "- `PAS-001-IC-INTEGRATION-001 1.0.0` — contrato comum, titularidade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, canais, observabilidade e falha segura.\n- `PAS-001-IC-CONTRACT-001 1.0.0` — 80 KPIs, 16 famílias, 28 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas, reabertura e contrato final.",
        "architecture extension list",
    )
    marker = """- proteção de terceiros, coletivos, dispositivos compartilhados e integrações temporárias;
- observabilidade, explicabilidade, auditoria e reconstrução.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `90%`.

O próximo bloco deverá consolidar os KPIs, guardrails, cenários e contrato final das Intervenções Contextuais."""
    addition = """- proteção de terceiros, coletivos, dispositivos compartilhados e integrações temporárias;
- observabilidade, explicabilidade, auditoria e reconstrução.

O contrato final consolida:

- 80 KPIs organizados em 16 famílias;
- baseline funcional segmentada antes de metas permanentes;
- painel de saúde com 17 visões e cinco níveis de desempenho;
- 28 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- critérios de conclusão, lacunas bloqueantes e não bloqueantes;
- singularidade centrada na decisão responsável entre manifestar-se e permanecer em silêncio;
- contrato final de titularidade, responsabilidades, limites, entradas, admissão e saídas;
- atenção e interruptibilidade separadas de consentimento;
- importância, urgência e temporalidade como dimensões independentes;
- silêncio, espera, adiamento e recusa como resultados legítimos;
- neutralidade comercial, proteção sensível, confiabilidade, explicabilidade e auditoria;
- critérios formais de reabertura normativa.

A Capacidade 07 está **Functionally complete**, com progresso editorial de referência de `100%`.

O próximo bloco deverá consolidar os fundamentos iniciais da Capacidade 08 — Experiências, que permanece `Planned` até a aprovação de sua primeira extensão normativa."""
    text = replace_once(text, marker, addition, "architecture contract section")
    final_rules = """645. As integrações funcionais estão consolidadas por `PAS-001-IC-INTEGRATION-001 1.0.0`.
646. Sinal não representa necessidade.
647. Identificação não representa candidatura.
648. Candidatura não representa admissão.
649. Admissão não representa apresentação.
650. Programação não representa entrega.
651. Envio não representa entrega.
652. Entrega não representa visualização.
653. Visualização não representa compreensão.
654. Compreensão não representa concordância.
655. Atenção não representa consentimento.
656. Disponibilidade técnica não representa interruptibilidade.
657. Importância não representa urgência.
658. Urgência comercial não representa urgência funcional.
659. Pergunta não representa obrigação.
660. Sugestão não cria compromisso.
661. Lembrete não cria compromisso novo.
662. Alerta exige fundamento material.
663. Ação material exige autorização.
664. Silêncio é resultado funcional legítimo.
665. Espera não representa abandono.
666. Ausência de resposta não representa recusa.
667. Adiamento não representa rejeição.
668. Recusa não representa fracasso.
669. Fadiga reduz pressão.
670. Horários protegidos prevalecem sobre intervenções não críticas.
671. Conteúdo sensível exige proteção reforçada.
672. Publicidade permanece separada.
673. Comissão não cria urgência.
674. Patrocínio não aumenta prioridade.
675. Contexto sensível não alimenta publicidade.
676. Organizações não recebem a jornada integral.
677. Terceiros não formam perfis paralelos.
678. Produtos especializados governam suas operações.
679. Intervenções Contextuais governa a manifestação, não a transação.
680. Guivos Intelligence pode sugerir, mas não impor.
681. Platform Layer transporta, mas não define relevância humana.
682. Integrações não transferem titularidade.
683. Reprocessamento não duplica efeitos.
684. Eventos fora de ordem não criam estados impossíveis.
685. Conflitos não são sobrescritos silenciosamente.
686. Correções não reescrevem o passado.
687. Revogação somente termina após propagação suficiente.
688. Falha parcial não representa sucesso integral.
689. Métricas avaliam o sistema.
690. `PAS-001-IC-CONTRACT-001 1.0.0` conclui funcionalmente a Capacidade 07, com progresso editorial de referência de `100%`, e o participante permanece no controle.
"""
    text = replace_once(
        text,
        "645. A Capacidade 07 está `In progress`, com progresso editorial de referência de `90%`, e o participante permanece no controle das integrações funcionais.\n",
        final_rules,
        "architecture final rules",
    )
    text = replace_once(
        text,
        "- [PAS-001-IC-INTEGRATION-001 — Integrações Funcionais das Intervenções Contextuais](pas-001-intervencoes-contextuais-integracoes-funcionais.md)",
        "- [PAS-001-IC-INTEGRATION-001 — Integrações Funcionais das Intervenções Contextuais](pas-001-intervencoes-contextuais-integracoes-funcionais.md)\n- [PAS-001-IC-CONTRACT-001 — Contrato Final das Intervenções Contextuais](pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md)",
        "architecture contract link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(arquitetura): concluir Intervenções Contextuais")


def update_roadmap() -> None:
    path = Path("docs/roadmap.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.5.0", "version: 10.0.0", "roadmap version")
    text = replace_once(
        text,
        "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida` e `05 — Próximos Passos`.",
        "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas` e `07 — Intervenções Contextuais`.",
        "roadmap completed capabilities",
    )
    text = text.replace(
        "- **Capacidade concluída:** `06 — Oportunidades Ativas`, `Functionally complete`, 100%.\n- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 90%.",
        "- **Capacidade concluída:** `06 — Oportunidades Ativas`, `Functionally complete`, 100%.\n- **Capacidade concluída:** `07 — Intervenções Contextuais`, `Functionally complete`, 100%.\n- **Próxima capacidade:** `08 — Experiências`, `Planned`, 0%.",
    )
    text = text.replace(
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0` e `PAS-001-IC-INTEGRATION-001 1.0.0`.",
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0`, `PAS-001-IC-EVENT-001 1.0.0`, `PAS-001-IC-INTEGRATION-001 1.0.0` e `PAS-001-IC-CONTRACT-001 1.0.0`.",
    )
    text = text.replace(
        "O próximo trabalho deverá consolidar as integrações funcionais da `Capacidade 07 — Intervenções Contextuais`.",
        "O próximo trabalho deverá consolidar os fundamentos iniciais da `Capacidade 08 — Experiências`, preservada como `Planned` até a aprovação de sua primeira extensão normativa.",
    )
    text = text.replace("## Capacidade 07 ativa", "## Capacidade 07 concluída")
    marker = """- proteção de terceiros, coletivos e dispositivos compartilhados;
- observabilidade, explicabilidade, auditoria e reconstrução.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `90%`."""
    addition = """- proteção de terceiros, coletivos e dispositivos compartilhados;
- observabilidade, explicabilidade, auditoria e reconstrução.

`PAS-001-IC-CONTRACT-001 1.0.0` consolida:

- 80 KPIs em 16 famílias;
- baseline funcional segmentada;
- painel de saúde e cinco níveis de desempenho;
- 28 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- critérios de conclusão, lacunas bloqueantes e não bloqueantes;
- singularidade, titularidade, responsabilidades, limites, entradas, admissão e saídas;
- silêncio funcional, atenção, interruptibilidade, importância, urgência, sensibilidade, fadiga, frequência, canais e autonomia;
- neutralidade comercial, proteção de terceiros, confiabilidade, explicabilidade e auditoria;
- critérios formais de reabertura normativa.

A Capacidade 07 está `Functionally complete`, com progresso editorial de referência de `100%`."""
    text = replace_once(text, marker, addition, "roadmap contract section")
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress | 90% |",
        "| 07 — Intervenções Contextuais | Functionally complete | 100% |",
    )
    text = text.replace(
        "Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 07.",
        "Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 08.",
    )
    text = text.replace(
        "- não reabrir as Capacidades 02, 03, 04, 05 ou 06 sem fundamento formal;",
        "- não reabrir as Capacidades 02, 03, 04, 05, 06 ou 07 sem fundamento formal;",
    )
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*\Z",
        """## Ponto exato de retomada

Retomar nos **fundamentos iniciais da Capacidade 08 — Experiências**.

Próxima entrega:

1. finalidade e pergunta central;
2. singularidade da experiência vivida;
3. distinção entre atividade, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida;
4. titularidade, participantes, papéis e autoridade;
5. temporalidade, duração, intensidade e recorrência;
6. sensibilidade, privacidade e informações de terceiros;
7. relações com Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas e Intervenções Contextuais;
8. estados e transições iniciais;
9. responsabilidades e limites;
10. comportamentos proibidos e critérios de aceite iniciais.

A Capacidade 08 permanece `Planned` até a aprovação de sua primeira extensão normativa.
""",
        "roadmap resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(roadmap): concluir Intervenções Contextuais")


def update_board() -> None:
    path = Path("docs/project/knowledge-board.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.5.0", "version: 10.0.0", "board version")
    text = replace_once(
        text,
        "| PAS-001-IC-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Intervenções Contextuais |",
        "| PAS-001-IC-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Intervenções Contextuais |\n| PAS-001-IC-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Intervenções Contextuais |",
        "board asset",
    )
    text = text.replace(
        "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos` e `06 — Oportunidades Ativas` |\n| Capacidade ativa | `07 — Intervenções Contextuais` |\n| Estado da capacidade ativa | `In progress` |\n| Extensão normativa vigente | `PAS-001-IC-INTEGRATION-001 1.0.0` |\n| Progresso editorial de Intervenções Contextuais | `90%` |",
        "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas` e `07 — Intervenções Contextuais` |\n| Próxima capacidade | `08 — Experiências` |\n| Estado da próxima capacidade | `Planned` |\n| Extensão normativa vigente | `PAS-001-IC-CONTRACT-001 1.0.0` |\n| Progresso editorial de Intervenções Contextuais | `100%` |",
    )
    text = text.replace(
        "| Foco imediato | Consolidar KPIs, guardrails, cenários e contrato final das Intervenções Contextuais |",
        "| Foco imediato | Consolidar os fundamentos iniciais da Capacidade 08 — Experiências |",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 90% | Fundamentos, ciclo de vida, visualização, controle, eventos e integrações consolidados; contrato final é a próxima entrega |",
        "| 07 — Intervenções Contextuais | Functionally complete — 100% | Seis extensões normativas, 80 KPIs, 28 guardrails, baseline, cenários e contrato final consolidados |",
    )
    marker = """- proteção de terceiros, coletivos, dispositivos compartilhados e integrações temporárias;
- observabilidade, explicabilidade, auditoria e reconstrução.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `90%`."""
    addition = """- proteção de terceiros, coletivos, dispositivos compartilhados e integrações temporárias;
- observabilidade, explicabilidade, auditoria e reconstrução.

### KPIs, guardrails, cenários e contrato final

- 80 KPIs em 16 famílias de indicadores sistêmicos;
- baseline funcional segmentada antes de metas permanentes;
- painel de saúde com 17 visões e cinco níveis de desempenho;
- 28 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- critérios de conclusão, lacunas bloqueantes e não bloqueantes;
- singularidade da decisão entre manifestar-se e permanecer em silêncio;
- contrato final de titularidade, responsabilidades, limites, entradas, admissão e saídas;
- silêncio funcional, atenção, interruptibilidade, importância, urgência, sensibilidade, fadiga, frequência, canais e autonomia;
- neutralidade comercial, proteção de terceiros e separação de Guivos Ads;
- confiabilidade, correção, revogação, explicabilidade, auditoria e critérios de reabertura.

A Capacidade 07 está `Functionally complete`, com progresso editorial de referência de `100%`."""
    text = replace_once(text, marker, addition, "board contract section")
    text = text.replace(
        "| Intervenções Contextuais | In progress — 90% |",
        "| Intervenções Contextuais | Functionally complete — 100% |",
    )
    text = replace_once(
        text,
        "| Integrações Funcionais de Intervenções Contextuais | Normative 1.0.0 |",
        "| Integrações Funcionais de Intervenções Contextuais | Normative 1.0.0 |\n| Contrato Final de Intervenções Contextuais | Normative 1.0.0 |\n| Baseline de Intervenções Contextuais | Construída antes de metas permanentes e segmentada por comportamento, canal, finalidade, sensibilidade, fadiga e estado |\n| Guardrail de Intervenções Contextuais | Regra crítica cuja violação não pode ser compensada por média positiva |\n| Conclusão funcional de Intervenções Contextuais | Contratos essenciais concluídos; não equivale a implementação ou validação em produção |",
        "board concepts",
    )
    text = text.replace("| Roadmap | 9.5.0 |", "| Roadmap | 10.0.0 |")
    text = text.replace("| Knowledge Board | 9.5.0 |", "| Knowledge Board | 10.0.0 |")
    text = replace_once(
        text,
        "| PAS-001-IC-INTEGRATION-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-IC-INTEGRATION-001 | Active 1.0.0 |\n| PAS-001-IC-CONTRACT-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "board governance",
    )
    text = replace_once(
        text,
        "Consolidar os **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários, critérios de conclusão, lacunas, reabertura e contrato final das Intervenções Contextuais**.",
        "Consolidar os **fundamentos iniciais da Capacidade 08 — Experiências**, incluindo singularidade, experiência vivida, distinções fundamentais, titularidade, temporalidade, sensibilidade, relações, estados, limites e integrações iniciais. A capacidade permanece `Planned` até a aprovação de sua primeira extensão normativa.",
        "board next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(board): concluir Intervenções Contextuais")


def update_matrix() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.4", "version: 1.9.0", "matrix version")
    text = text.replace(
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com fundamentos, ciclo de vida, visualização, controle, eventos e integrações funcionais consolidados e progresso editorial de 90% |",
        "| Intervenções Contextuais | Manter | Capacidade 07 funcionalmente concluída por seis extensões normativas, 80 KPIs, 28 guardrails, baseline, cenários e progresso editorial de 100% |",
    )
    text = replace_once(
        text,
        "| Integrações Funcionais das Intervenções Contextuais | Manter | PAS-001-IC-INTEGRATION-001 1.0.0 define contrato comum, titularidade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, canais, observabilidade e falha segura |",
        "| Integrações Funcionais das Intervenções Contextuais | Manter | PAS-001-IC-INTEGRATION-001 1.0.0 define contrato comum, titularidade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, canais, observabilidade e falha segura |\n| KPIs, Guardrails, Cenários e Contrato Final das Intervenções Contextuais | Manter | PAS-001-IC-CONTRACT-001 1.0.0 define 80 KPIs, 16 famílias, 28 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas, reabertura e contrato final |",
        "matrix contract document",
    )
    text = replace_once(
        text,
        "| Controle de frequência de intervenção | Manter | Limites globais, por categoria e por canal, governados por finalidade, fadiga, preferência e mudança material |",
        "| Controle de frequência de intervenção | Manter | Limites globais, por categoria e por canal, governados por finalidade, fadiga, preferência e mudança material |\n| Baseline de Intervenções Contextuais | Manter | Referência empírica anterior a metas permanentes, segmentada por comportamento, canal, finalidade, sensibilidade, fadiga, estado e maturidade |\n| Guardrail de Intervenções Contextuais | Manter | Regra crítica de tolerância zero cuja violação interrompe o fluxo e não pode ser compensada por média positiva |\n| Conclusão funcional de Intervenções Contextuais | Manter | Reconhecimento de que os contratos essenciais estão definidos, distinto de implementação, operação ou validação quantitativa |",
        "matrix contract concepts",
    )
    text = text.replace(
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-INTEGRATION-001 1.0.0` consolida as integrações funcionais da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 90% e governa titularidade, finalidade, autoridade, minimização, proveniência, temporalidades, consentimento, sincronização, divergência, revogação, propagação, prevenção de ciclos, capacidades, produtos, organizações, profissionais, canais, sistemas externos, observabilidade, explicabilidade, auditoria e falha segura, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02, 03, 04, 05, 06 e 07 estão funcionalmente concluídas. `PAS-001-IC-CONTRACT-001 1.0.0` conclui a Capacidade 07, eleva o progresso editorial para 100% e consolida 80 KPIs, 16 famílias, 28 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas, singularidade, titularidade, responsabilidades, limites, neutralidade, privacidade, confiabilidade, explicabilidade, auditoria e reabertura normativa, sem promover candidatos arquiteturais à Canon.",
    )
    text = replace_once(
        text,
        "Consolidar os **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão, lacunas bloqueantes e não bloqueantes, critérios de reabertura e contrato final da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar os **fundamentos iniciais da Capacidade 08 — Experiências**, incluindo singularidade, experiência vivida, distinções fundamentais, titularidade, temporalidade, sensibilidade, relações, estados, limites e integrações iniciais. A capacidade permanece `Planned` até a aprovação de sua primeira extensão normativa.",
        "matrix next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(canon): concluir Intervenções Contextuais")


def update_mkdocs() -> None:
    path = Path("mkdocs.yml")
    text = path.read_text(encoding="utf-8")
    marker = "      - PAS-001-IC-INTEGRATION-001 — Integrações Funcionais das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-integracoes-funcionais.md"
    text = replace_once(
        text,
        marker,
        marker + "\n      - PAS-001-IC-CONTRACT-001 — Contrato Final das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md",
        "mkdocs nav",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(site): adicionar contrato final de Intervenções Contextuais")


def update_changelog() -> None:
    path = Path("CHANGELOG.md")
    text = path.read_text(encoding="utf-8")
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    entry = """## 0.37.0 — Contextual Interventions Final Contract

- Criação de `PAS-001-IC-CONTRACT-001 — KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Intervenções Contextuais`, versão `1.0.0`.
- Registro do documento como sexta extensão normativa e contrato final da Capacidade 07 do `PAS-001 — Guivos Journey`.
- Consolidação de 80 KPIs organizados em 16 famílias.
- Definição dos princípios, unidades, segmentações e janelas de medição.
- Consolidação da baseline funcional anterior a metas permanentes.
- Definição do painel de saúde com 17 visões e dos níveis Crítico, Instável, Adequado, Confiável e Maduro.
- Registro de 28 guardrails de tolerância zero e de seu tratamento obrigatório.
- Consolidação dos cenários funcionalmente ideais de silêncio, pergunta mínima, lembrete, alerta, ação autorizada, intervenção sensível, apresentação de oportunidade, Evento de Vida, recorrência, comunicação coletiva, consistência entre canais, contestação e execução externa.
- Consolidação dos cenários alternativos de contexto incompleto, identidade incerta, canal indisponível, fontes conflitantes, fadiga elevada, integração indisponível, entrega parcial, resposta ambígua e ausência de resposta.
- Consolidação dos cenários limite de risco crítico, dispositivo compartilhado, obrigação institucional, sistema externo indisponível, contestação após entrega, revogação em processamento, múltiplas urgências, dependência de terceiro e evento fora de ordem.
- Registro de 40 critérios de conclusão funcional.
- Definição de lacunas não bloqueantes pertencentes a design, engenharia, segurança, dados, operação e validação.
- Declaração de inexistência de lacuna funcional bloqueante conhecida na baseline normativa.
- Consolidação da finalidade e singularidade da Capacidade 07.
- Consolidação de titularidade, responsabilidades, limites, entradas, admissão, saídas, estados e dimensões.
- Definição do comportamento menos intrusivo suficiente como regra de seleção.
- Consolidação do silêncio como resultado funcional legítimo.
- Separação entre atenção, interruptibilidade, importância, urgência e temporalidade.
- Consolidação de sensibilidade, privacidade, fadiga, frequência, canais, autonomia e controles.
- Definição dos papéis e limites de Guivos Intelligence, Platform Layer, produtos, organizações e profissionais.
- Consolidação da neutralidade comercial e da proteção de terceiros.
- Definição de confiabilidade, explicabilidade, auditoria, contestação, correção, revogação e critérios de reabertura.
- Registro de 45 regras fundamentais finais.
- Atualização da Arquitetura de Produtos para `1.9.0` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap e do Knowledge Board para `10.0.0`.
- Atualização da Matriz de Consolidação Canônica para `1.9.0`.
- Atualização do README e da página inicial do GKR.
- Substituição do estado da Capacidade 07 de `In progress` por `Functionally complete`.
- Elevação do progresso editorial de referência de 90% para 100%.
- Preservação das Capacidades 02, 03, 04, 05 e 06 como `Functionally complete`.
- Preservação da Capacidade 08 — Experiências como `Planned`.
- Definição dos fundamentos iniciais de Experiências como próximo ponto exato de retomada.

"""
    text = replace_once(text, marker, marker + entry, "changelog header")
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(changelog): registrar contrato final de Intervenções Contextuais")


def validate() -> None:
    contract = Path("docs/product-architecture/pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md").read_text(encoding="utf-8")
    checks = {
        "contract start": "# 3272. Bloco final da Capacidade de Intervenções Contextuais" in contract,
        "contract end": "# 3365. Conclusão e continuidade normativa" in contract,
        "no generated ids": 'id="' not in contract,
        "contract kpis": "IC-KPI-080" in contract,
        "contract guardrails": "28 guardrails" in contract,
        "README complete": "Functionally complete — 100%" in Path("README.md").read_text(encoding="utf-8"),
        "home complete": "Functionally complete — 100%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.9.0" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 10.0.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 10.0.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.9.0" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "nav": "pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.37.0 — Contextual Interventions Final Contract" in Path("CHANGELOG.md").read_text(encoding="utf-8"),
        "next experiences": "fundamentos iniciais da Capacidade 08" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
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
    branch = os.environ.get("TARGET_BRANCH", "ic-contract-20260716")
    run("git", "push", "origin", f"HEAD:{branch}")


if __name__ == "__main__":
    main()
