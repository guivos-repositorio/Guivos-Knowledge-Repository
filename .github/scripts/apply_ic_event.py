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


def event_summary(prefix: str = "") -> str:
    bullets = [
        "distinção entre comando, proposta e evento funcional reconhecido",
        "persistência funcional suficiente antes da publicação de eventos materiais",
        "agregado `Registro de Intervenção Contextual` e estrutura comum versionada",
        "identidade, participante, ator, destinatário, papel, autoridade, fonte, finalidade e proveniência",
        "temporalidades de fato, solicitação, observação, conhecimento, avaliação, reconhecimento, persistência, publicação, aplicação, entrega, resposta, propagação e correção",
        "correlação e causalidade funcional sem fabricação de relação causal",
        "classificação de sensibilidade, minimização de payload e retenção proporcional",
        "declaração obrigatória de publicidade, patrocínio, comissão, afiliação e demais relações comerciais",
        "19 famílias de eventos funcionais de identificação, avaliação, admissão, comportamento, programação, entrega, resposta, preferências, execução externa, correção, revogação, integração e falhas",
        "deduplicação semântica e versão esperada do agregado",
        "avaliação de atenção, interruptibilidade, urgência, fadiga e frequência sem inferência de consentimento",
        "admissão separada de apresentação, entrega, visualização, resposta e transação",
        "comportamento principal explícito entre agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar e silenciar",
        "programação, prontidão e revalidação anterior à entrega",
        "apresentação, entrega técnica, visualização, resposta e ausência de resposta como fatos distintos",
        "adiamento, silêncio, recusa, ocultação, bloqueio e preferências com contratos próprios",
        "execução externa sob autoridade do produto ou sistema executor",
        "contestação, correção compensatória, cancelamento, expiração, encerramento e reabertura",
        "revogação concluída somente após propagação suficiente",
        "idempotência, ordenação, concorrência, atomicidade, reconstrução, compatibilidade, explicabilidade, auditoria e falha segura",
    ]
    return "\n".join(f"{prefix}- {item};" for item in bullets[:-1]) + f"\n{prefix}- {bullets[-1]}."


def update_readme() -> None:
    path = Path("README.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 60%",
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 80%",
    )
    text = text.replace(
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001 e PAS-001-IC-VIEW-001, todas em 1.0.0",
        "- **Extensões vigentes de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001, PAS-001-IC-LIFECYCLE-001, PAS-001-IC-VIEW-001 e PAS-001-IC-EVENT-001, todas em 1.0.0",
    )
    marker = """- falha segura, sincronização pendente, conflitos e auditoria compreensível.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **60%**."""
    addition = """- falha segura, sincronização pendente, conflitos e auditoria compreensível.

`PAS-001-IC-EVENT-001 1.0.0` consolida:

""" + event_summary() + """

A Capacidade 07 está **In progress**, com progresso editorial de referência de **80%**."""
    text = replace_once(text, marker, addition, "README event section")
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*?\n## Product Engineering",
        """## Ponto exato de retomada

Retomar nas integrações funcionais da Capacidade 07 — Intervenções Contextuais.

Próxima entrega:

- contrato funcional comum de integração;
- finalidade, minimização, identidade e autoridade;
- integrações com Captura de Contexto e Contexto Vivo;
- integrações com Objetivos, Eventos de Vida, Próximos Passos e Oportunidades Ativas;
- relações com Experiências e Evolução Contínua;
- limites da Guivos Intelligence e da Platform Layer;
- integrações com produtos especializados, organizações e profissionais;
- canais, calendários, localização, fontes públicas e sistemas externos;
- sincronização, revogação, propagação e prevenção de ciclos;
- neutralidade comercial, observabilidade, auditoria e falha segura.

## Product Engineering""",
        "README resumption",
    )
    text = text.replace(
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `60%`.",
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `80%`.",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 60% |",
        "| 07 — Intervenções Contextuais | In progress — 80% |",
    )
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
    text = text.replace(
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 60%;",
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 80%;",
    )
    text = text.replace(
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0` e `PAS-001-IC-VIEW-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
        "- `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0` e `PAS-001-IC-EVENT-001 1.0.0` como extensões normativas vigentes da Capacidade 07;",
    )
    text = text.replace(
        "Consolidar os **contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar as **integrações funcionais da Capacidade 07 — Intervenções Contextuais**.",
    )
    text = text.replace(
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As três extensões de Intervenções Contextuais consolidam fundamentos, ciclo de vida, Central de Intervenções, Fila de Atenção, mensagens, justificativas, controles, preferências, acessibilidade, privacidade, relações comerciais e falha segura.",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As quatro extensões de Intervenções Contextuais consolidam fundamentos, ciclo de vida, visualização, controle, agregado funcional, estrutura comum e 19 famílias de eventos com autoridade, temporalidade, correção, revogação, idempotência, reconstrução e falha segura.",
    )
    text = replace_once(
        text,
        "- [Visualização e Controle das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)",
        "- [Visualização e Controle das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-visualizacao-controle.md)\n- [Eventos Funcionais das Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-eventos-funcionais.md)",
        "home link",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 60% |",
        "| 07 — Intervenções Contextuais | In progress — 80% |",
    )
    text = replace_once(
        text,
        "Retomar nos contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
        "Retomar nas integrações funcionais da Capacidade 07 — Intervenções Contextuais com Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos.",
        "home resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(index): avançar eventos de Intervenções Contextuais")


def update_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.2", "version: 1.8.3", "architecture version")
    text = replace_once(
        text,
        "- `PAS-001-IC-VIEW-001 1.0.0` — Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura.",
        "- `PAS-001-IC-VIEW-001 1.0.0` — Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura.\n- `PAS-001-IC-EVENT-001 1.0.0` — agregado funcional, estrutura comum, 19 famílias de eventos, autoridade, finalidade, temporalidade, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura.",
        "architecture extension",
    )
    marker = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `60%`.

O próximo bloco deverá consolidar os contratos dos eventos funcionais das Intervenções Contextuais."""
    addition = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

Os contratos dos eventos funcionais consolidam:

""" + event_summary() + """

A Capacidade 07 está **In progress**, com progresso editorial de referência de `80%`.

O próximo bloco deverá consolidar as integrações funcionais das Intervenções Contextuais."""
    text = replace_once(text, marker, addition, "architecture event section")
    text = text.replace(
        "555. A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`, e o participante permanece no controle da visualização e do controle.",
        "555. A visualização e o controle das Intervenções Contextuais estão consolidados por `PAS-001-IC-VIEW-001 1.0.0`.",
    )
    rules_marker = "555. A visualização e o controle das Intervenções Contextuais estão consolidados por `PAS-001-IC-VIEW-001 1.0.0`.\n\n## Documentos do domínio"
    rules = """555. A visualização e o controle das Intervenções Contextuais estão consolidados por `PAS-001-IC-VIEW-001 1.0.0`.
556. Comando, proposta e evento funcional permanecem conceitos distintos.
557. Evento material somente é publicado após persistência funcional suficiente.
558. O Registro de Intervenção Contextual preserva identidade, estado, decisões, preferências, correções, revogações e falhas.
559. Mudança material de finalidade, destinatário, comportamento ou impacto exige novo agregado ou ciclo.
560. Todo evento declara tipo, versão contratual, agregado, versões, autoridade, finalidade, temporalidades, proveniência, sensibilidade e idempotência.
561. Identificadores de eventos são únicos, imutáveis e não reutilizáveis.
562. Consumidores rejeitam versões incompatíveis de forma segura e preservam eventos desconhecidos.
563. Versão do agregado impede sobrescrita silenciosa, regressão, duplicidade e concorrência não detectada.
564. Participante, ator, destinatário, terceiro, organização e executor externo permanecem distintos.
565. Acesso técnico e presença de dados não ampliam autoridade.
566. Finalidades genéricas de engajamento, conversão, receita ou retenção não justificam contexto pessoal ou sensível.
567. Tempo do fato, solicitação, conhecimento, avaliação, persistência, publicação, entrega, resposta, propagação e correção permanecem distintos.
568. Correlação não representa causalidade funcional.
569. A causalidade não pode ser inferida por clique, proximidade temporal, abertura de aplicativo ou localização.
570. Proveniência reconstrói a cadeia desde a fonte até o consumidor e o efeito.
571. Sensibilidade governa payload, logs, consumidores, retenção, visualização, notificação e compartilhamento.
572. Payloads são minimizados e não carregam narrativas integrais quando recortes funcionais forem suficientes.
573. Relações comerciais são declaradas e não elevam relevância, urgência ou prioridade.
574. As 19 famílias de eventos preservam responsabilidades e significados próprios.
575. Identificação não representa candidatura e candidatura não autoriza entrega, notificação, execução ou compartilhamento.
576. Duplicidade semântica deve ser reconhecida mesmo com identificadores distintos.
577. Mudança material de finalidade exige nova avaliação e pode exigir novo agregado.
578. Excesso de autoridade bloqueia novos efeitos, limita automação e exige correção auditável.
579. Avaliação contextual declara critérios, contexto utilizado, exclusões, limitações, incerteza, alternativas e custo de interrupção.
580. Atenção avaliada não representa consentimento ou intenção.
581. Disponibilidade técnica do canal não representa interruptibilidade.
582. Promoção, comissão, estoque, campanha e meta comercial não fundamentam urgência funcional.
583. Fadiga elevada reduz pressão, frequência e intensidade.
584. Admissão não representa apresentação, entrega, visualização, resposta ou autorização transacional.
585. Um comportamento principal deve permanecer explícito em cada decisão de intervenção.
586. Agir exige autorização vigente, executor identificado, escopo delimitado, risco compatível e reversibilidade suficiente.
587. Programação declara janela, fuso, canal, validade, reavaliação, cancelamento e horários protegidos.
588. Autorização, validade, canal, sensibilidade, fadiga, preferências, revogações e conflitos são revalidados antes da entrega.
589. Apresentação, entrega técnica, visualização, resposta e ação externa permanecem fatos distintos.
590. Confirmação técnica de entrega não representa leitura, compreensão, concordância, interesse, consentimento ou execução.
591. Resposta ambígua não produz efeito material sem esclarecimento.
592. Ausência de resposta não representa recusa, desinteresse ou julgamento.
593. Adiamento não representa recusa e silêncio é evento funcional legítimo.
594. Preferências produzem efeitos dentro de seu escopo e não reescrevem eventos anteriores.
595. Relação comercial oculta limita apresentação e gera incidente de governança.
596. Execução externa permanece sob autoridade do produto ou sistema executor.
597. Contestação material limita efeitos, preserva evidências e pode exigir avaliação humana.
598. Correções são compensatórias e não apagam eventos históricos.
599. Revogação somente se conclui após bloqueio e propagação suficiente aos consumidores relevantes.
600. Reprocessamento, ordenação, concorrência, atomicidade, reconstrução e falha segura preservam o controle do participante; a Capacidade 07 está `In progress`, com progresso editorial de referência de `80%`.

## Documentos do domínio"""
    text = replace_once(text, rules_marker, rules, "architecture rules")
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
    text = text.replace(
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 60%.",
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 80%.",
    )
    text = text.replace(
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0` e `PAS-001-IC-VIEW-001 1.0.0`.",
        "- **Extensões normativas vigentes de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`, `PAS-001-IC-LIFECYCLE-001 1.0.0`, `PAS-001-IC-VIEW-001 1.0.0` e `PAS-001-IC-EVENT-001 1.0.0`.",
    )
    text = text.replace(
        "O próximo trabalho deverá consolidar os contratos dos eventos funcionais da `Capacidade 07 — Intervenções Contextuais`.",
        "O próximo trabalho deverá consolidar as integrações funcionais da `Capacidade 07 — Intervenções Contextuais`.",
    )
    marker = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`."""
    addition = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria.

`PAS-001-IC-EVENT-001 1.0.0` consolida:

""" + event_summary() + """

A Capacidade 07 está `In progress`, com progresso editorial de referência de `80%`."""
    text = replace_once(text, marker, addition, "roadmap event section")
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress | 60% |",
        "| 07 — Intervenções Contextuais | In progress | 80% |",
    )
    text = replace_regex(
        text,
        r"## Ponto exato de retomada\n.*\Z",
        """## Ponto exato de retomada

Retomar nas **integrações funcionais das Intervenções Contextuais**.

Próxima entrega:

1. contrato funcional comum de integração;
2. identidade, finalidade, autoridade, minimização, proveniência e sensibilidade;
3. integração com Captura de Contexto e Contexto Vivo;
4. integração com Objetivos, Eventos de Vida, Próximos Passos e Oportunidades Ativas;
5. relações com Experiências e Evolução Contínua;
6. limites da Guivos Intelligence e da Platform Layer;
7. integrações com Guivos Business, Mall, Travel, Media e Ads;
8. organizações, profissionais, canais, calendários, localização e fontes públicas;
9. sistemas externos, execução, sincronização e reconciliação;
10. pausa, desconexão, revogação e propagação;
11. prevenção de ciclos, neutralidade comercial, observabilidade, auditoria e falha segura.
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
    text = text.replace(
        "| Extensão normativa vigente | `PAS-001-IC-VIEW-001 1.0.0` |",
        "| Extensão normativa vigente | `PAS-001-IC-EVENT-001 1.0.0` |",
    )
    text = text.replace(
        "| Progresso editorial de Intervenções Contextuais | `60%` |",
        "| Progresso editorial de Intervenções Contextuais | `80%` |",
    )
    text = text.replace(
        "| Foco imediato | Consolidar os contratos dos eventos funcionais das Intervenções Contextuais |",
        "| Foco imediato | Consolidar as integrações funcionais das Intervenções Contextuais |",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | In progress — 60% | Fundamentos, ciclo de vida, visualização e controle consolidados; eventos funcionais são a próxima entrega |",
        "| 07 — Intervenções Contextuais | In progress — 80% | Fundamentos, ciclo de vida, visualização, controle e eventos funcionais consolidados; integrações são a próxima entrega |",
    )
    marker = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `60%`."""
    addition = """- falha segura, sincronização pendente, conflitos, operação sem conexão e auditoria compreensível.

### Eventos funcionais

""" + event_summary() + """

A Capacidade 07 está `In progress`, com progresso editorial de referência de `80%`."""
    text = replace_once(text, marker, addition, "board event section")
    text = text.replace(
        "| Intervenções Contextuais | In progress — 60% |",
        "| Intervenções Contextuais | In progress — 80% |",
    )
    text = replace_once(
        text,
        "| Visualização e Controle de Intervenções Contextuais | Normative 1.0.0 |",
        "| Visualização e Controle de Intervenções Contextuais | Normative 1.0.0 |\n| Eventos Funcionais de Intervenções Contextuais | Normative 1.0.0 |\n| Registro de Intervenção Contextual | Agregado que preserva identidade, estado, decisões, preferências, correções, revogações e falhas |\n| Evento funcional de intervenção | Fato reconhecido, versionado, persistido e publicado dentro da autoridade e finalidade declaradas |\n| Relação comercial do evento de intervenção | Metadado obrigatório que não altera relevância, urgência ou prioridade funcional |",
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
    text = replace_once(
        text,
        "Consolidar os **contratos dos eventos funcionais das Intervenções Contextuais**, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
        "Consolidar as **integrações funcionais das Intervenções Contextuais** com capacidades do Journey, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos, preservando finalidade, minimização, autoridade, sincronização, revogação, neutralidade comercial, observabilidade e falha segura.",
        "board next",
    )
    path.write_text(text, encoding="utf-8")
    commit(str(path), "docs(board): registrar eventos de Intervenções Contextuais")


def update_matrix() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.8.2", "version: 1.8.3", "matrix version")
    text = text.replace(
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com fundamentos, ciclo de vida, visualização e controle consolidados e progresso editorial de 60% |",
        "| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com fundamentos, ciclo de vida, visualização, controle e eventos funcionais consolidados e progresso editorial de 80% |",
    )
    text = replace_once(
        text,
        "| Visualização e Controle das Intervenções Contextuais | Manter | PAS-001-IC-VIEW-001 1.0.0 define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais e consistência entre canais |",
        "| Visualização e Controle das Intervenções Contextuais | Manter | PAS-001-IC-VIEW-001 1.0.0 define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais e consistência entre canais |\n| Eventos Funcionais das Intervenções Contextuais | Manter | PAS-001-IC-EVENT-001 1.0.0 define agregado funcional, estrutura comum, 19 famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria |",
        "matrix document",
    )
    text = replace_once(
        text,
        "| Controle de intervenção | Manter | Responder, adiar, silenciar, recusar, ocultar, bloquear, contestar, corrigir e revogar permanecem ações distintas |",
        "| Controle de intervenção | Manter | Responder, adiar, silenciar, recusar, ocultar, bloquear, contestar, corrigir e revogar permanecem ações distintas |\n| Registro de Intervenção Contextual | Manter | Agregado principal que preserva identidade, estado, decisões, preferências, correções, revogações e falhas |\n| Evento funcional de intervenção | Manter | Fato reconhecido, versionado, imutável e publicado após persistência funcional suficiente |\n| Contrato de evento de intervenção | Manter | Estrutura comum com agregado, versões, participante, ator, autoridade, finalidade, temporalidades, proveniência, sensibilidade, idempotência e retenção |",
        "matrix concepts",
    )
    text = text.replace(
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-VIEW-001 1.0.0` consolida a visualização e o controle da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 60% e define Central de Intervenções, Fila de Atenção, cartões, justificativas, histórico, controles, preferências, acessibilidade, privacidade, relações comerciais, consistência entre canais e falha segura, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-EVENT-001 1.0.0` consolida os contratos dos eventos funcionais da Capacidade 07, mantém seu estado `In progress`, eleva o progresso editorial para 80% e define agregado, estrutura comum, 19 famílias, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria, sem promover candidatos arquiteturais à Canon.",
    )
    text = text.replace(
        "Consolidar os **contratos dos eventos funcionais da Capacidade 07 — Intervenções Contextuais**, incluindo estrutura comum, autoridade, temporalidade, correlação, identificação, avaliação, admissão, seleção de comportamento, programação, apresentação, entrega, resposta, adiamento, silêncio, contestação, correção, revogação, propagação, idempotência, ordenação, concorrência e falha segura.",
        "Consolidar as **integrações funcionais da Capacidade 07 — Intervenções Contextuais** com as capacidades do Journey, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos.",
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
    entry = """## 0.36.3 — Contextual Interventions Functional Event Contracts

- Criação de `PAS-001-IC-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Intervenções Contextuais`, versão `1.0.0`.
- Registro do documento como quarta extensão normativa da Capacidade 07 do `PAS-001 — Guivos Journey`.
- Distinção normativa entre comando, proposta e evento funcional reconhecido.
- Exigência de persistência funcional suficiente antes da publicação de eventos materiais.
- Definição do agregado `Registro de Intervenção Contextual`.
- Formalização da estrutura comum versionada dos eventos, incluindo agregado, versões, participante, ator, papel, autoridade, fonte, finalidade, comportamento, canal, sensibilidade, correlação, causalidade, idempotência, temporalidades, proveniência, relação comercial, permissões, payload, consumidores e retenção.
- Consolidação da identidade permanente do agregado e dos critérios para novo ciclo ou novo agregado.
- Separação entre participante, ator, destinatário, terceiro, organização e executor externo.
- Limitação da autoridade de declaração, solicitação, confirmação, avaliação, execução, correção e revogação.
- Proibição de finalidades genéricas de engajamento, conversão, receita, personalização ou retenção para uso de contexto pessoal ou sensível.
- Definição das temporalidades de fato, solicitação, observação, conhecimento, avaliação, reconhecimento, persistência, publicação, aplicação, entrega, resposta, propagação e correção.
- Separação entre correlação e causalidade funcional.
- Consolidação de proveniência, sensibilidade, minimização de payload e declaração de relações comerciais.
- Definição de 19 famílias de eventos funcionais.
- Consolidação dos eventos de identificação, candidatura, finalidade, autoridade e avaliação contextual.
- Definição dos eventos de atenção, interruptibilidade, urgência, sensibilidade, fadiga e frequência.
- Consolidação dos eventos de admissão, rejeição, encaminhamento humano e silêncio após avaliação.
- Definição dos eventos de seleção de comportamento entre agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar e silenciar.
- Consolidação dos eventos de programação, prontidão, apresentação e entrega.
- Separação entre confirmação técnica de entrega, visualização, compreensão, concordância, interesse, resposta, consentimento e ação externa.
- Definição dos eventos de resposta, ambiguidade, ausência de resposta, adiamento, silêncio, recusa, ocultação e bloqueio.
- Consolidação dos eventos de preferências, horários protegidos, modo discreto e resumos.
- Definição dos eventos comerciais e tratamento de relações comerciais ocultas.
- Consolidação dos eventos de execução externa sob autoridade do produto ou sistema executor.
- Definição dos eventos de contestação, limitação de efeitos e correção compensatória.
- Consolidação dos eventos de cancelamento, expiração, encerramento, reabertura e novo ciclo.
- Definição da revogação e de sua conclusão somente após propagação suficiente.
- Consolidação dos eventos de integração, sincronização, reconciliação e conflitos.
- Formalização de idempotência, duplicidade semântica, ordenação, concorrência e atomicidade funcional.
- Definição dos eventos de falha, recuperação, falha segura e falha parcial.
- Consolidação de reconstrução, retenção proporcional, logs minimizados, responsabilidades de produtores e consumidores, compatibilidade, explicabilidade e auditoria.
- Registro de métricas sistêmicas, 25 comportamentos proibidos e 45 critérios de aceite.
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
        "event families": "19. falha, recuperação e reconstrução" in normative,
        "README 80": "In progress — 80%" in Path("README.md").read_text(encoding="utf-8"),
        "home 80": "In progress — 80%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.8.3" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 9.4.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 9.4.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.8.3" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "nav": "pas-001-intervencoes-contextuais-eventos-funcionais.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.36.3 — Contextual Interventions Functional Event Contracts" in Path("CHANGELOG.md").read_text(encoding="utf-8"),
        "next integrations": "integrações funcionais" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
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
    branch = os.environ.get("GITHUB_HEAD_REF") or os.environ["GITHUB_REF_NAME"]
    run("git", "push", "origin", f"HEAD:{branch}")


if __name__ == "__main__":
    main()
