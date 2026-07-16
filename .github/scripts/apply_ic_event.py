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
    text = text.replace("`In progress`, 60%", "`In progress`, 80%")
    text = text.replace(
        "PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001 e PAS-001-IC-VIEW-001, todas em 1.0.0",
        "PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001, PAS-001-IC-VIEW-001 e PAS-001-IC-EVENT-001, todas em 1.0.0",
    )
    marker = """- falha segura, sincronização pendente, conflitos e auditoria compreensível.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **60%**."""
    addition = """- falha segura, sincronização pendente, conflitos e auditoria compreensível.

`PAS-001-IC-EVENT-001 1.0.0` consolida:

- distinção entre comando, proposta e evento funcional;
- persistência anterior à publicação de eventos materiais;
- `Registro de Intervenção Contextual` como agregado principal;
- estrutura comum com identidade, versão, autoridade, finalidade, temporalidades, correlação, proveniência, sensibilidade, idempotência e retenção;
- 19 famílias de eventos funcionais;
- eventos de identificação, candidatura, finalidade, autoridade e avaliação contextual;
- eventos de sensibilidade, fadiga, frequência, admissão e seleção de comportamento;
- eventos de programação, prontidão, apresentação, entrega, visualização e resposta;
- eventos de adiamento, silêncio, recusa, ocultação, bloqueio e preferências;
- eventos comerciais e de execução externa;
- eventos de contestação, correção, cancelamento, expiração e encerramento;
- revogação, propagação, integração e sincronização;
- idempotência, duplicidade semântica, ordenação, concorrência e atomicidade funcional;
- falha segura, reconstrução, retenção, compatibilidade, explicabilidade e auditoria.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **80%**."""
    text = replace_once(text, marker, addition, "README event section")
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*?\n## Product Engineering",
        """## Ponto exato de retomada

Retomar nas integrações funcionais da Capacidade 07 — Intervenções Contextuais.

Próxima entrega:

- integração com Captura de Contexto e Contexto Vivo;
- integração com Objetivos, Eventos de Vida e Próximos Passos;
- integração com Oportunidades Ativas, Experiências e Evolução Contínua;
- contratos com Guivos Intelligence e Platform Layer;
- integração com Mall, Travel, Business, Media, Ads e demais produtos;
- organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos;
- finalidade, minimização, autoridade, proveniência e neutralidade comercial;
- sincronização, revogação, propagação, observabilidade e falha segura.

## Product Engineering""",
        "README resumption",
    )
    text = text.replace("`In progress`, com progresso editorial de referência de `60%`", "`In progress`, com progresso editorial de referência de `80%`")
    text = text.replace("| 07 — Intervenções Contextuais | In progress — 60% |", "| 07 — Intervenções Contextuais | In progress — 80% |")
    text = replace_once(
        text,
        "- [Visualização e Controle das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "- [Visualização e Controle das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)\n- [Eventos Funcionais das Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-eventos-funcionais.md)",
        "README link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(readme): avançar eventos de Intervenções Contextuais")


def update_home() -> None:
    path = Path("docs/index.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace("`In progress`, 60%", "`In progress`, 80%")
    text = text.replace(
        "`PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0` e `PAS-001-IC-VIEW-001 1.0.0`",
        "`PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0` e `PAS-001-IC-EVENT-001 1.0.0`",
    )
    text = text.replace(
        "Consolidar os **contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar as **integrações funcionais da Capacidade 07 — Intervenções Contextuais**.",
    )
    text = text.replace(
        "As três extensões de Intervenções Contextuais consolidam fundamentos, ciclo de vida, Central de Intervenções, Fila de Atenção, mensagens, justificativas, controles, preferências, acessibilidade, privacidade, relações comerciais e falha segura.",
        "As quatro extensões de Intervenções Contextuais consolidam fundamentos, ciclo de vida, visualização, controle e contratos de eventos, incluindo agregado funcional, 19 famílias de eventos, autoridade, temporalidade, proveniência, idempotência, revogação, reconstrução e falha segura.",
    )
    text = replace_once(
        text,
        "- [Visualização e Controle das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "- [Visualização e Controle das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)\n- [Eventos Funcionais das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-eventos-funcionais.md)",
        "home link",
    )
    text = text.replace("| 07 — Intervenções Contextuais | In progress — 60% |", "| 07 — Intervenções Contextuais | In progress — 80% |")
    text = replace_regex(
        text,
        r"## Ponto de retomada\n.*\Z",
        """## Ponto de retomada

Retomar nas integrações funcionais da Capacidade 07 — Intervenções Contextuais, incluindo Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos, com finalidade, minimização, autoridade, sincronização, revogação, propagação, neutralidade comercial, observabilidade e falha segura.
""",
        "home resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(index): avançar eventos de Intervenções Contextuais")


def update_product_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.2", "version: 1.8.3", "architecture version")
    text = replace_once(
        text,
        "- `PAS-001-IC-VIEW-001 1.0.0` — Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura.",
        "- `PAS-001-IC-VIEW-001 1.0.0` — Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura.\n- `PAS-001-IC-EVENT-001 1.0.0` — agregado funcional, estrutura comum, 19 famílias de eventos, autoridade, temporalidade, proveniência, sensibilidade, revogação, idempotência, concorrência, reconstrução e auditoria.",
        "architecture extension",
    )
    marker = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `60%`.

O próximo bloco deverá consolidar os contratos dos eventos funcionais das Intervenções Contextuais."""
    addition = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

Os contratos dos eventos funcionais consolidam:

- distinção entre comando, proposta e evento reconhecido;
- persistência funcional anterior à publicação;
- `Registro de Intervenção Contextual` como agregado principal;
- identidade permanente e nova identidade diante de mudança material;
- estrutura comum com versão contratual, versão do agregado, participante, ator, autoridade, finalidade, temporalidades, correlação, causalidade, proveniência, sensibilidade, relação comercial, permissões e retenção;
- 19 famílias de eventos;
- eventos de identificação, candidatura, finalidade, autoridade e avaliação contextual;
- eventos de sensibilidade, fadiga, frequência, admissão e seleção de comportamento;
- eventos de programação, prontidão, apresentação, entrega, visualização e resposta;
- eventos de adiamento, silêncio, recusa, ocultação, bloqueio e preferências;
- eventos comerciais, de execução externa, contestação e correção;
- eventos de cancelamento, expiração, encerramento, revogação, integração e sincronização;
- idempotência, duplicidade semântica, ordenação, concorrência e atomicidade funcional;
- falha segura, reconstrução, retenção, produtores, consumidores, compatibilidade, explicabilidade e auditoria.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `80%`.

O próximo bloco deverá consolidar as integrações funcionais das Intervenções Contextuais."""
    text = replace_once(text, marker, addition, "architecture event section")
    text = text.replace(
        "555. A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`, e o participante permanece no controle da visualização e do controle.",
        "555. A visualização e o controle estão consolidados por `PAS-001-IC-VIEW-001 1.0.0`.",
    )
    rules_marker = "555. A visualização e o controle estão consolidados por `PAS-001-IC-VIEW-001 1.0.0`.\n\n## Documentos do domínio"
    event_rules = """555. A visualização e o controle estão consolidados por `PAS-001-IC-VIEW-001 1.0.0`.
556. Comando, proposta e evento são conceitos distintos.
557. Evento material somente é publicado após persistência funcional suficiente.
558. Registro de Intervenção Contextual é o agregado funcional principal.
559. Identidade do agregado é permanente enquanto finalidade e impacto permanecerem materialmente equivalentes.
560. Mudança material de finalidade, destinatário, comportamento ou impacto cria novo agregado.
561. Todo evento possui identificador único, versão contratual e versão do agregado.
562. Participante, ator, destinatário, terceiro e executor externo permanecem distintos.
563. Acesso técnico não amplia autoridade.
564. Finalidade genérica de engajamento, conversão, receita ou retenção não autoriza contexto sensível.
565. Momento do fato, conhecimento, avaliação, persistência, publicação, entrega, resposta, propagação e correção permanecem separados.
566. Correlação não representa causalidade.
567. Proveniência deve reconstruir a cadeia desde a fonte até o efeito.
568. Payloads devem ser minimizados conforme finalidade e sensibilidade.
569. Relação comercial deve permanecer declarada e não altera prioridade funcional.
570. Identificação não representa candidatura e candidatura não representa admissão.
571. Admissão não representa apresentação, entrega ou autorização transacional.
572. Seleção de comportamento possui exatamente um comportamento principal.
573. Programação não representa prontidão ou entrega.
574. Apresentação não representa entrega técnica confirmada.
575. Entrega confirmada não representa leitura, compreensão, concordância, interesse ou consentimento.
576. Visualização não altera interesse ou prioridade.
577. Resposta ambígua não produz efeito material.
578. Ausência de resposta não representa recusa ou desinteresse.
579. Adiamento não representa recusa e silêncio não representa falha.
580. Preferências produzem efeitos somente dentro de seu escopo e não reescrevem histórico.
581. Relação comercial oculta limita apresentação e gera incidente de governança.
582. Execução externa permanece sob autoridade do produto ou sistema executor.
583. Contestação material limita efeitos e automações.
584. Correções são compensatórias e não reescrevem eventos históricos.
585. Revogação somente termina após propagação suficiente.
586. Reprocessamento não duplica eventos ou efeitos materiais.
587. Duplicidade semântica deve ser reconhecida além do identificador técnico.
588. Eventos fora de ordem não criam estados impossíveis.
589. Alterações concorrentes exigem versão esperada e reconciliação explícita.
590. Operações compostas declaram atomicidade, compensações e condições de falha.
591. Falha preserva o último estado válido e impede falsa entrega.
592. Falha parcial não representa sucesso integral.
593. Estado deve ser reconstruível por eventos válidos, versões, correções, revogações e reconciliações.
594. Retenção e logs são proporcionais e minimizados.
595. Produtores e consumidores validam contrato, autoridade, finalidade, versão, idempotência e sensibilidade.
596. Mudanças incompatíveis exigem nova versão contratual.
597. Explicabilidade e auditoria devem reconstruir fatos, decisões, consumidores e efeitos.
598. Métricas dos eventos avaliam o sistema, não o participante.
599. A Capacidade 07 está `In progress`, com progresso editorial de referência de `80%`, e o participante permanece no controle dos eventos funcionais.

## Documentos do domínio"""
    text = replace_once(text, rules_marker, event_rules, "architecture event rules")
    text = replace_once(
        text,
        "- [PAS-001-IC-VIEW-001 — Visualização e Controle das Intervenções Contextuais](pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "- [PAS-001-IC-VIEW-001 — Visualização e Controle das Intervenções Contextuais](pas-001-intervencoes-contextuais-visualizacao-controle.md)\n- [PAS-001-IC-EVENT-001 — Eventos Funcionais das Intervenções Contextuais](pas-001-intervencoes-contextuais-eventos-funcionais.md)",
        "architecture link",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(arquitetura): registrar eventos de Intervenções Contextuais")


def update_roadmap() -> None:
    path = Path("docs/roadmap.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.3.0", "version: 9.4.0", "roadmap version")
    text = text.replace("`In progress`, 60%", "`In progress`, 80%")
    text = text.replace(
        "`PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0` e `PAS-001-IC-VIEW-001 1.0.0`",
        "`PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0` e `PAS-001-IC-EVENT-001 1.0.0`",
    )
    text = text.replace(
        "O próximo trabalho deverá consolidar os contratos dos eventos funcionais da `Capacidade 07 — Intervenções Contextuais`.",
        "O próximo trabalho deverá consolidar as integrações funcionais da `Capacidade 07 — Intervenções Contextuais`.",
    )
    marker = """A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`."""
    addition = """`PAS-001-IC-EVENT-001 1.0.0` consolida:

- distinção entre comando, proposta e evento;
- persistência anterior à publicação;
- Registro de Intervenção Contextual como agregado funcional;
- estrutura comum, identidade, versão, autoridade, finalidade, temporalidade, proveniência, sensibilidade e minimização;
- 19 famílias de eventos funcionais;
- identificação, candidatura, finalidade, autoridade e avaliação contextual;
- sensibilidade, fadiga, frequência, admissão e seleção de comportamento;
- programação, prontidão, apresentação, entrega, visualização e resposta;
- adiamento, silêncio, recusa, ocultação, bloqueio e preferências;
- relações comerciais e execução externa;
- contestação, correção, cancelamento, expiração e encerramento;
- revogação, integração, sincronização e propagação;
- idempotência, duplicidade semântica, ordenação, concorrência e atomicidade;
- falha segura, reconstrução, retenção, compatibilidade, explicabilidade e auditoria.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `80%`."""
    text = replace_once(text, marker, addition, "roadmap event section")
    text = text.replace("| 07 — Intervenções Contextuais | In progress | 60% |", "| 07 — Intervenções Contextuais | In progress | 80% |")
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*\Z",
        """## Ponto exato de retomada

Retomar nas **integrações funcionais das Intervenções Contextuais**.

Próxima entrega:

1. contrato funcional comum de integração;
2. Captura de Contexto e Contexto Vivo;
3. Objetivos, Eventos de Vida e Próximos Passos;
4. Oportunidades Ativas, Experiências e Evolução Contínua;
5. Guivos Intelligence e Platform Layer;
6. Mall, Travel, Business, Media, Ads e demais produtos;
7. organizações, profissionais e canais externos;
8. calendários, localização, fontes públicas e sistemas externos;
9. finalidade, minimização, autoridade, proveniência e neutralidade comercial;
10. sincronização, revogação, propagação e prevenção de ciclos;
11. observabilidade, auditoria e falha segura.
""",
        "roadmap resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(roadmap): avançar eventos de Intervenções Contextuais")


def update_board() -> None:
    path = Path("docs/project/knowledge-board.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.3.0", "version: 9.4.0", "board version")
    text = replace_once(
        text,
        "| PAS-001-IC-VIEW-001 | Active 1.0.0 | Definir a visualização e o controle das Intervenções Contextuais |",
        "| PAS-001-IC-VIEW-001 | Active 1.0.0 | Definir a visualização e o controle das Intervenções Contextuais |\n| PAS-001-IC-EVENT-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais das Intervenções Contextuais |",
        "board asset",
    )
    text = text.replace("| Extensão normativa vigente | `PAS-001-IC-VIEW-001 1.0.0` |", "| Extensão normativa vigente | `PAS-001-IC-EVENT-001 1.0.0` |")
    text = text.replace("| Progresso editorial de Intervenções Contextuais | `60%` |", "| Progresso editorial de Intervenções Contextuais | `80%` |")
    text = text.replace("| Foco imediato | Consolidar os contratos dos eventos funcionais das Intervenções Contextuais |", "| Foco imediato | Consolidar as integrações funcionais das Intervenções Contextuais |")
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 60% | Fundamentos, ciclo de vida, visualização e controle consolidados; eventos funcionais são a próxima entrega |",
        "| 07 — Intervenções Contextuais | In progress — 80% | Fundamentos, ciclo de vida, visualização, controle e eventos funcionais consolidados; integrações são a próxima entrega |",
    )
    marker = """A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`."""
    addition = """### Eventos funcionais

- comando, proposta e evento permanecem distintos;
- eventos materiais são publicados somente após persistência suficiente;
- Registro de Intervenção Contextual é o agregado principal;
- estrutura comum preserva identidade, versão, autoridade, finalidade, temporalidades, correlação, proveniência, sensibilidade, idempotência e retenção;
- 19 famílias organizam os eventos;
- identificação, candidatura, finalidade, autoridade e avaliação contextual possuem fatos próprios;
- sensibilidade, fadiga, frequência, admissão e seleção de comportamento permanecem explícitas;
- programação, prontidão, apresentação, entrega, visualização e resposta permanecem separadas;
- adiamento, silêncio, recusa, ocultação, bloqueio e preferências possuem eventos próprios;
- relações comerciais e execução externa preservam autoridade e transparência;
- contestação, correção, cancelamento, expiração e encerramento preservam histórico;
- revogação, integração, sincronização e propagação são governadas;
- idempotência, duplicidade semântica, ordenação, concorrência e atomicidade impedem estados impossíveis;
- falha segura, reconstrução, retenção, compatibilidade, explicabilidade e auditoria são obrigatórias.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `80%`."""
    text = replace_once(text, marker, addition, "board event section")
    text = text.replace("| Intervenções Contextuais | In progress — 60% |", "| Intervenções Contextuais | In progress — 80% |")
    text = replace_once(
        text,
        "| Visualização e Controle de Intervenções Contextuais | Normative 1.0.0 |",
        "| Visualização e Controle de Intervenções Contextuais | Normative 1.0.0 |\n| Eventos Funcionais de Intervenções Contextuais | Normative 1.0.0 |\n| Registro de Intervenção Contextual | Agregado funcional principal da capacidade |\n| Evento funcional de intervenção | Fato reconhecido, versionado, minimizado e publicado após persistência suficiente |",
        "board concepts",
    )
    text = text.replace("| Roadmap | 9.3.0 |", "| Roadmap | 9.4.0 |")
    text = text.replace("| Knowledge Board | 9.3.0 |", "| Knowledge Board | 9.4.0 |")
    text = replace_once(
        text,
        "| PAS-001-IC-VIEW-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-IC-VIEW-001 | Active 1.0.0 |\n| PAS-001-IC-EVENT-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "board governance",
    )
    text = replace_regex(
        text,
        r"## Próxima atividade\n.*\Z",
        """## Próxima atividade

Consolidar as **integrações funcionais das Intervenções Contextuais**, incluindo Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos, com finalidade, minimização, autoridade, sincronização, revogação, propagação, neutralidade comercial, observabilidade e falha segura.
""",
        "board next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(board): registrar eventos de Intervenções Contextuais")


def update_matrix() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.2", "version: 1.8.3", "matrix version")
    text = text.replace(
        "Capacidade 07 em desenvolvimento, com fundamentos, ciclo de vida, visualização e controle consolidados e progresso editorial de 60%",
        "Capacidade 07 em desenvolvimento, com fundamentos, ciclo de vida, visualização, controle e eventos funcionais consolidados e progresso editorial de 80%",
    )
    text = replace_once(
        text,
        "| Visualização e Controle das Intervenções Contextuais | Manter | PAS-001-IC-VIEW-001 1.0.0 define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais e consistência entre canais |",
        "| Visualização e Controle das Intervenções Contextuais | Manter | PAS-001-IC-VIEW-001 1.0.0 define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais e consistência entre canais |\n| Eventos Funcionais das Intervenções Contextuais | Manter | PAS-001-IC-EVENT-001 1.0.0 define agregado, estrutura comum, 19 famílias, autoridade, temporalidade, proveniência, sensibilidade, idempotência, concorrência, reconstrução e auditoria |",
        "matrix document",
    )
    text = replace_once(
        text,
        "| Controle de intervenção | Manter | Responder, adiar, silenciar, recusar, ocultar, bloquear, contestar, corrigir e revogar permanecem ações distintas |",
        "| Controle de intervenção | Manter | Responder, adiar, silenciar, recusar, ocultar, bloquear, contestar, corrigir e revogar permanecem ações distintas |\n| Registro de Intervenção Contextual | Manter | Agregado principal que preserva identidade, estado, comportamento, temporalidade, entrega, resposta, preferências, correções, revogações e falhas |\n| Evento funcional de intervenção | Manter | Fato reconhecido, imutável, versionado e publicado após persistência suficiente |\n| Família de eventos de intervenção | Manter | Organização normativa em 19 famílias funcionais |",
        "matrix concepts",
    )
    text = text.replace(
        "`PAS-001-IC-VIEW-001 1.0.0` consolida a visualização e o controle da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 60% e define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura",
        "`PAS-001-IC-EVENT-001 1.0.0` consolida os eventos funcionais da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 80% e define agregado, estrutura comum, 19 famílias, autoridade, temporalidade, proveniência, sensibilidade, revogação, idempotência, concorrência, reconstrução e auditoria",
    )
    text = text.replace(
        "Consolidar os **contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais**, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
        "Consolidar as **integrações funcionais da Capacidade 07 — Intervenções Contextuais**, incluindo Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos, com finalidade, minimização, autoridade, sincronização, revogação, propagação, neutralidade comercial, observabilidade e falha segura.",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(canon): consolidar eventos de Intervenções Contextuais")


def update_mkdocs() -> None:
    path = Path("mkdocs.yml")
    text = path.read_text(encoding="utf-8")
    marker = "      - PAS-001-IC-VIEW-001 — Visualização e Controle das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md"
    text = replace_once(
        text,
        marker,
        marker + "\n      - PAS-001-IC-EVENT-001 — Eventos Funcionais das Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-eventos-funcionais.md",
        "mkdocs nav",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(site): adicionar eventos de Intervenções Contextuais")


def update_changelog() -> None:
    path = Path("CHANGELOG.md")
    text = path.read_text(encoding="utf-8")
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    entry = """## 0.36.3 — Contextual Interventions Functional Events

- Criação de `PAS-001-IC-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Intervenções Contextuais`, versão `1.0.0`.
- Registro do documento como quarta extensão normativa da Capacidade 07 do `PAS-001 — Guivos Journey`.
- Distinção entre comando, proposta e evento funcional reconhecido.
- Definição da persistência funcional anterior à publicação de eventos materiais.
- Definição do `Registro de Intervenção Contextual` como agregado principal.
- Consolidação da identidade permanente do agregado e da criação de novo agregado diante de mudança material.
- Definição da estrutura comum do evento, identificador, versão contratual, versão do agregado, participante, ator, destinatário, papel, autoridade, fonte, finalidade, comportamento, canal, sensibilidade, correlação, causalidade, idempotência, temporalidades, proveniência, relação comercial, permissões, minimização, consumidores e retenção.
- Consolidação de temporalidades independentes e da separação entre correlação e causalidade.
- Definição de proveniência reconstruível e payload minimizado.
- Consolidação de 19 famílias de eventos funcionais.
- Definição dos eventos de identificação, candidatura, finalidade, autoridade e avaliação contextual.
- Definição dos eventos de sensibilidade, fadiga, frequência, admissão e seleção de comportamento.
- Definição dos eventos de programação, prontidão, apresentação, entrega, visualização e resposta.
- Definição dos eventos de adiamento, silêncio, recusa, ocultação, bloqueio e preferências.
- Definição dos eventos comerciais e de execução externa.
- Definição dos eventos de contestação, correção, cancelamento, expiração e encerramento.
- Consolidação dos eventos de revogação, integração, sincronização e propagação.
- Definição da idempotência, duplicidade semântica, ordenação, concorrência e atomicidade funcional.
- Consolidação dos eventos de falha, falha segura, falha parcial e recuperação.
- Definição da reconstrução, retenção, logs minimizados, responsabilidades de produtores e consumidores, compatibilidade, explicabilidade e auditoria.
- Registro das métricas sistêmicas, comportamentos proibidos e critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.8.3` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap para `9.4.0`, do Knowledge Board para `9.4.0` e da Matriz de Consolidação Canônica para `1.8.3`.
- Atualização do README e da página inicial do GKR.
- Manutenção da Capacidade 07 no estado `In progress` e elevação do progresso editorial de referência de 60% para 80%.
- Preservação das Capacidades 02, 03, 04, 05 e 06 como `Functionally complete`.
- Preservação da Capacidade 08 — Experiências como `Planned`.
- Definição das integrações funcionais das Intervenções Contextuais como próximo ponto exato de retomada.

"""
    text = replace_once(text, marker, marker + entry, "changelog header")
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(changelog): registrar eventos de Intervenções Contextuais")


def validate() -> None:
    normative = Path("docs/product-architecture/pas-001-intervencoes-contextuais-eventos-funcionais.md").read_text(encoding="utf-8")
    checks = {
        "normative start": "# 3065. Finalidade dos contratos de eventos" in normative,
        "normative end": "# 3164. Continuidade normativa" in normative,
        "no generated ids": 'id="' not in normative,
        "README 80": "In progress — 80%" in Path("README.md").read_text(encoding="utf-8"),
        "home 80": "In progress — 80%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.8.3" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 9.4.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 9.4.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.8.3" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "nav": "pas-001-intervencoes-contextuais-eventos-funcionais.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.36.3 — Contextual Interventions Functional Events" in Path("CHANGELOG.md").read_text(encoding="utf-8"),
        "next integrations": "integrações funcionais" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
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
