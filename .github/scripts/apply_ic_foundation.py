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


def regex_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Regex marker count for {label}: {count}")
    return updated


def commit(paths: list[str], message: str) -> None:
    run("git", "add", *paths)
    run("git", "commit", "-m", message)


def update_readme() -> None:
    path = Path("README.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- **Próxima frente oficial:** 07 — Intervenções Contextuais, `Planned / concept consolidated`",
        "- **Capacidade ativa:** 07 — Intervenções Contextuais, `In progress`, 20%",
        "README active capability",
    )
    text = replace_once(
        text,
        "- **Extensões vigentes de Oportunidades Ativas:** PAS-001-OA-FOUNDATION-001, PAS-001-OA-LIFECYCLE-001, PAS-001-OA-VIEW-001, PAS-001-OA-EVENT-001, PAS-001-OA-INTEGRATION-001 e PAS-001-OA-CONTRACT-001, todas em 1.0.0",
        "- **Extensões vigentes de Oportunidades Ativas:** PAS-001-OA-FOUNDATION-001, PAS-001-OA-LIFECYCLE-001, PAS-001-OA-VIEW-001, PAS-001-OA-EVENT-001, PAS-001-OA-INTEGRATION-001 e PAS-001-OA-CONTRACT-001, todas em 1.0.0\n- **Extensão vigente de Intervenções Contextuais:** PAS-001-IC-FOUNDATION-001 1.0.0",
        "README extension",
    )
    section = """## Capacidade 07 — Intervenções Contextuais

`PAS-001-IC-FOUNDATION-001 1.0.0` consolida:

- finalidade, pergunta central, singularidade e valor entregue;
- Intervenção Contextual como manifestação deliberada, proporcional e explicável;
- decisão entre agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar ou silenciar;
- silêncio como resultado funcional legítimo;
- oportunidade de intervenção, admissão e fluxo canônico;
- distinção entre sinal, notificação, publicidade, ação, transação e intervenção;
- reatividade, proatividade, gatilhos e não gatilhos;
- contexto mínimo, atenção, interruptibilidade, importância e urgência;
- temporalidade, sensibilidade, fadiga, frequência e repetição;
- intensidade, escalonamento, desescalonamento e canais;
- explicabilidade por `Por que estou vendo isto?` e `Por que agora?`;
- autonomia, autoridade, papéis funcionais e controles do participante;
- horários protegidos, adiamento, recusa, ocultação e bloqueio;
- proteção de saúde, finanças, jurídico, religião, voluntariado e terceiros;
- separação entre intervenções funcionais, comerciais, institucionais e coletivas;
- relações com todas as capacidades do Journey;
- limites da Guivos Intelligence, Platform Layer, produtos especializados e Guivos Ads;
- estados, eventos, responsabilidades, limites e comportamentos proibidos iniciais.

A Capacidade 07 está **In progress**, com progresso editorial de referência de **20%**.

"""
    text = replace_once(text, "## Ponto exato de retomada\n", section + "## Ponto exato de retomada\n", "README section")
    start = text.index("## Ponto exato de retomada")
    end = text.index("## Product Engineering")
    point = """## Ponto exato de retomada

Retomar nas regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais.

Próxima entrega:

- identificação e candidatura;
- avaliação e admissão;
- programação, espera e apresentação;
- resposta, adiamento e silêncio;
- cancelamento e expiração;
- contestação e correção;
- escalonamento e desescalonamento;
- controle de frequência e fadiga;
- propagação, idempotência e falha segura.

"""
    text = text[:start] + point + text[end:]
    text = replace_once(
        text,
        "A Capacidade 06 está `Functionally complete`; a próxima frente oficial é a Capacidade 07 — Intervenções Contextuais, ainda `Planned / concept consolidated`.",
        "A Capacidade 06 está `Functionally complete`; a Capacidade 07 — Intervenções Contextuais está `In progress`, com progresso editorial de referência de `20%`.",
        "README engineering state",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | Planned / concept consolidated |",
        "| 07 — Intervenções Contextuais | In progress — 20% |",
    )
    text = replace_once(
        text,
        "- [Contrato Final das Oportunidades Ativas](docs/product-architecture/pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md)",
        "- [Contrato Final das Oportunidades Ativas](docs/product-architecture/pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md)\n- [Fundamentos Iniciais de Intervenções Contextuais](docs/product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md)",
        "README quick link",
    )
    path.write_text(text, encoding="utf-8")
    commit([str(path)], "docs(readme): ativar Intervenções Contextuais")


def update_index() -> None:
    path = Path("docs/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- Capacidade 07 — Intervenções Contextuais como próxima frente oficial, ainda `Planned / concept consolidated`;",
        "- Capacidade 07 — Intervenções Contextuais em desenvolvimento, `In progress`, 20%;",
        "index active capability",
    )
    text = replace_once(
        text,
        "- `PAS-001-OA-FOUNDATION-001 1.0.0`, `PAS-001-OA-LIFECYCLE-001 1.0.0`, `PAS-001-OA-VIEW-001 1.0.0`, `PAS-001-OA-EVENT-001 1.0.0`, `PAS-001-OA-INTEGRATION-001 1.0.0` e `PAS-001-OA-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 06;",
        "- `PAS-001-OA-FOUNDATION-001 1.0.0`, `PAS-001-OA-LIFECYCLE-001 1.0.0`, `PAS-001-OA-VIEW-001 1.0.0`, `PAS-001-OA-EVENT-001 1.0.0`, `PAS-001-OA-INTEGRATION-001 1.0.0` e `PAS-001-OA-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 06;\n- `PAS-001-IC-FOUNDATION-001 1.0.0` como primeira extensão normativa vigente da Capacidade 07;",
        "index extension",
    )
    text = replace_once(
        text,
        "Consolidar os **fundamentos iniciais da Capacidade 07 — Intervenções Contextuais**.",
        "Consolidar as **regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais**.",
        "index mission",
    )
    text = replace_once(
        text,
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final.",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. A primeira extensão de Intervenções Contextuais consolida finalidade, decisões de manifestação, silêncio, atenção, urgência, sensibilidade, fadiga, canais, autonomia e limites.",
        "index summary",
    )
    text = replace_once(
        text,
        "- [Contrato Final das Oportunidades Ativas](product-architecture/pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md)",
        "- [Contrato Final das Oportunidades Ativas](product-architecture/pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md)\n- [Fundamentos Iniciais de Intervenções Contextuais](product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md)",
        "index quick link",
    )
    text = text.replace(
        "| 07 — Intervenções Contextuais | Planned / concept consolidated |",
        "| 07 — Intervenções Contextuais | In progress — 20% |",
    )
    text = replace_once(
        text,
        "Retomar nos fundamentos iniciais da Capacidade 07 — Intervenções Contextuais, preservando seu estado `Planned / concept consolidated` até a aprovação da primeira extensão normativa.",
        "Retomar nas regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "index resumption",
    )
    path.write_text(text, encoding="utf-8")
    commit([str(path)], "docs(index): ativar Intervenções Contextuais")


def update_architecture() -> None:
    path = Path("docs/product-architecture/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.7.0", "version: 1.8.0", "architecture version")
    old = "A próxima frente oficial é a Capacidade 07 — Intervenções Contextuais, que permanece `Planned / concept consolidated` até sua primeira extensão normativa."
    new = """### Capacidade 07 — Intervenções Contextuais

A extensão normativa vigente é:

- `PAS-001-IC-FOUNDATION-001 1.0.0` — finalidade, pergunta central, singularidade, decisões possíveis, oportunidade de intervenção, silêncio, atenção, interruptibilidade, urgência, sensibilidade, fadiga, canais, autonomia, controles, relações, estados e eventos iniciais.

Os fundamentos iniciais consolidam:

- Intervenção Contextual como manifestação deliberada, proporcional e explicável;
- singularidade centrada na decisão responsável entre manifestar-se ou permanecer em silêncio;
- decisões de agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar ou silenciar;
- silêncio como resultado funcional legítimo;
- oportunidade candidata e oportunidade admitida de intervenção;
- fluxo canônico de sinal ou solicitação até intervenção, silêncio e reavaliação;
- distinção entre intervenção, notificação, publicidade, comando, tarefa, oportunidade, transação e conteúdo editorial;
- reatividade, proatividade, gatilhos legítimos e não gatilhos comerciais;
- contexto mínimo, atenção, interruptibilidade, importância, urgência e temporalidade;
- sensibilidade, fadiga, frequência, repetição, intensidade, escalonamento e desescalonamento;
- seleção e consistência de canais;
- explicabilidade por motivo, momento, dados, fontes, autoridade, incertezas e controles;
- autonomia, autoridade limitada e papéis funcionais distintos;
- horários protegidos, adiamento, recusa, ocultação, bloqueio e silêncio;
- proteção de saúde, finanças, jurídico, religião, voluntariado, organizações, coletivos e terceiros;
- separação entre intervenções funcionais, comerciais e institucionais;
- relações governadas com as capacidades concluídas do Journey;
- limites da Guivos Intelligence, Platform Layer, produtos especializados e Guivos Ads;
- estados, eventos, responsabilidades, limites e comportamentos proibidos iniciais.

A Capacidade 07 está **In progress**, com progresso editorial de referência de `20%`.

O próximo bloco deverá consolidar as regras do ciclo de vida das Intervenções Contextuais."""
    text = replace_once(text, old, new, "architecture capability section")
    marker = "416. O participante permanece no controle do contrato final de Oportunidades Ativas.\n\n## Documentos do domínio"
    rules = """416. O participante permanece no controle do contrato final de Oportunidades Ativas.
417. Intervenções Contextuais governa se, quando, como e com qual intensidade a Guivos se manifesta.
418. Sinal não representa necessidade, urgência, autorização ou intervenção.
419. Oportunidade de intervenção exige utilidade legítima superior ao custo provável da interrupção.
420. Silêncio é resultado funcional legítimo e não representa falha.
421. Agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar e silenciar possuem significados distintos.
422. Ação material exige autorização e permanece sob responsabilidade do produto executor.
423. Pergunta solicita o mínimo necessário e permite recusa ou resposta posterior.
424. Informação deve distinguir fato, estimativa, hipótese, fonte, validade e limitação.
425. Sugestão não cria compromisso, prioridade, Objetivo, Próximo Passo ou transação.
426. Lembrete recupera algo conhecido e não cria novo compromisso.
427. Alerta exige risco, prazo ou mudança material e não pode operar como promoção.
428. Confirmação deve preceder compartilhamento sensível, inscrição, contratação, pagamento ou efeito irreversível.
429. Aguardar e observar são decisões legítimas, distintas de abandono e vigilância.
430. Intervenção proativa exige controles reforçados de finalidade, relevância, atenção, frequência, sensibilidade e silêncio.
431. Clique, rolagem, tempo de tela, popularidade, comissão, margem, patrocínio e estoque não são gatilhos funcionais.
432. Contexto de decisão deve ser mínimo, autorizado e temporalmente adequado.
433. Atenção não representa consentimento.
434. Interruptibilidade avalia adequação de interromper, não disponibilidade técnica do canal.
435. Importância e urgência permanecem dimensões distintas.
436. Urgência somente pode decorrer de risco, prazo real, perda objetiva, segurança, obrigação ou necessidade declarada.
437. Escassez promocional, meta comercial e pressão social não fabricam urgência.
438. Sensibilidade governa conteúdo, título, prévia, canal, autenticação, horário, retenção e compartilhamento.
439. Fadiga elevada reduz frequência, agrupa, adia, simplifica, suspende ou silencia.
440. Repetição exige mudança material, prazo real, solicitação, regra autorizada ou falha de entrega.
441. Intensidade crítica exige fundamento forte e nunca pode ser utilizada para publicidade.
442. Canal deve considerar finalidade, urgência, sensibilidade, acessibilidade, preferência e ambiente.
443. Toda intervenção deve explicar por que ocorreu e por que naquele momento.
444. Autonomia exige adiamento, recusa, ocultação, controle de frequência, escolha de canal, revogação e silêncio.
445. Intervenções Contextuais decide a manifestação, não Objetivos, Próximos Passos, interesse, transações, progresso ou transformação.
446. O participante controla categorias, canais, frequência, horários, intensidade, fontes, organizações, localização e silêncio.
447. Horários protegidos devem ser respeitados, salvo exceção legítima previamente definida.
448. Adiamento não representa recusa e recusa não produz penalidade ou julgamento.
449. Conteúdo sensível exige título neutro, canal protegido, ausência de prévia pública e retenção limitada.
450. Intervenções comerciais devem permanecer identificadas e separadas das funcionais.
451. Contexto sensível não pode alimentar publicidade ou pressão comercial.
452. Organizações somente originam comunicações dentro de sua autoridade.
453. Intervenções coletivas preservam contexto coletivo e confirmação individual.
454. Informações de terceiros não formam perfis independentes.
455. Capacidades do Journey fornecem recortes e solicitações sem transferir decisão.
456. Oportunidades Ativas fornece relevância e janela; Intervenções Contextuais decide quando, como ou se apresentar.
457. Guivos Intelligence pode detectar, estimar, resumir, justificar e propor silêncio, mas não impor intervenção.
458. Platform Layer sustenta filas, canais, entrega e observabilidade sem definir urgência humana.
459. Produtos especializados executam ações autorizadas e não determinam prioridade pessoal.
460. Guivos Ads opera contratos próprios e permanece separado de alertas, lembretes, perguntas e intervenções sensíveis.
461. Falha parcial não representa entrega integral.
462. Métricas futuras avaliarão o sistema, não o valor, mérito, fé, disciplina ou produtividade do participante.
463. A Capacidade 07 está `In progress`, com progresso editorial de referência de `20%`.
464. O participante permanece no controle dos fundamentos de Intervenções Contextuais.

## Documentos do domínio"""
    text = replace_once(text, marker, rules, "architecture rules")
    text = replace_once(
        text,
        "- [PAS-001-OA-CONTRACT-001 — Contrato Final das Oportunidades Ativas](pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md)",
        "- [PAS-001-OA-CONTRACT-001 — Contrato Final das Oportunidades Ativas](pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md)\n- [PAS-001-IC-FOUNDATION-001 — Fundamentos Iniciais de Intervenções Contextuais](pas-001-intervencoes-contextuais-fundamentos-iniciais.md)",
        "architecture document link",
    )
    path.write_text(text, encoding="utf-8")
    commit([str(path)], "docs(arquitetura): consolidar fundamentos de Intervenções Contextuais")


def update_roadmap() -> None:
    path = Path("docs/roadmap.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.0.0", "version: 9.1.0", "roadmap version")
    text = replace_once(
        text,
        "- **Próxima frente oficial:** `07 — Intervenções Contextuais`, `Planned / concept consolidated`.",
        "- **Capacidade ativa:** `07 — Intervenções Contextuais`, `In progress`, 20%.",
        "roadmap active capability",
    )
    text = replace_once(
        text,
        "- **Extensões normativas vigentes:** `PAS-001-OA-FOUNDATION-001 1.0.0`, `PAS-001-OA-LIFECYCLE-001 1.0.0`, `PAS-001-OA-VIEW-001 1.0.0`, `PAS-001-OA-EVENT-001 1.0.0`, `PAS-001-OA-INTEGRATION-001 1.0.0` e `PAS-001-OA-CONTRACT-001 1.0.0`.",
        "- **Extensões normativas vigentes de Oportunidades Ativas:** `PAS-001-OA-FOUNDATION-001 1.0.0`, `PAS-001-OA-LIFECYCLE-001 1.0.0`, `PAS-001-OA-VIEW-001 1.0.0`, `PAS-001-OA-EVENT-001 1.0.0`, `PAS-001-OA-INTEGRATION-001 1.0.0` e `PAS-001-OA-CONTRACT-001 1.0.0`.\n- **Extensão normativa vigente de Intervenções Contextuais:** `PAS-001-IC-FOUNDATION-001 1.0.0`.",
        "roadmap extensions",
    )
    text = replace_once(
        text,
        "O próximo trabalho deverá consolidar os fundamentos iniciais da `Capacidade 07 — Intervenções Contextuais`, sem alterar seu estado até a aprovação normativa.",
        "O próximo trabalho deverá consolidar as regras do ciclo de vida da `Capacidade 07 — Intervenções Contextuais`.",
        "roadmap direction",
    )
    insertion = """## Capacidade 07 ativa

### Capacidade 07 — Intervenções Contextuais

`PAS-001-IC-FOUNDATION-001 1.0.0` consolida:

- finalidade, pergunta central, singularidade e valor entregue;
- manifestação deliberada, proporcional e explicável;
- decisões de agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar ou silenciar;
- silêncio como decisão funcional legítima;
- oportunidade candidata e oportunidade admitida de intervenção;
- fluxo canônico de avaliação e manifestação;
- distinções entre intervenção, sinal, notificação, publicidade, ação e transação;
- intervenções reativas e proativas;
- gatilhos legítimos e não gatilhos de engajamento ou receita;
- entradas mínimas e contexto autorizado;
- atenção, interruptibilidade, importância, urgência e temporalidade;
- sensibilidade, fadiga, frequência, repetição e intensidade;
- escalonamento, desescalonamento, canais e consistência;
- conteúdo mínimo, explicabilidade e justificativa temporal;
- autonomia, autoridade, papéis e controles do participante;
- horários protegidos, adiamento, recusa, ocultação e bloqueio;
- proteção de intervenções sensíveis e de terceiros;
- separação entre comunicações funcionais, comerciais, institucionais e coletivas;
- relações com todas as capacidades do Journey;
- limites da Guivos Intelligence, Platform Layer, produtos especializados e Guivos Ads;
- estados, eventos, responsabilidades, limites e comportamentos proibidos iniciais.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `20%`.

"""
    text = replace_once(text, "## Progresso das capacidades do Journey\n", insertion + "## Progresso das capacidades do Journey\n", "roadmap capability section")
    text = text.replace(
        "| 07 — Intervenções Contextuais | Planned / concept consolidated | 10% |",
        "| 07 — Intervenções Contextuais | In progress | 20% |",
    )
    start = text.index("## Ponto exato de retomada")
    point = """## Ponto exato de retomada

Retomar nas **regras do ciclo de vida das Intervenções Contextuais**.

Próxima entrega:

1. identificação e candidatura;
2. avaliação e admissão;
3. programação, espera e prontidão;
4. apresentação e entrega;
5. resposta, adiamento e silêncio;
6. cancelamento e expiração;
7. contestação e correção;
8. escalonamento e desescalonamento;
9. controle de frequência e fadiga;
10. propagação, idempotência, ordenação, concorrência e falha segura.
"""
    text = text[:start] + point
    path.write_text(text, encoding="utf-8")
    commit([str(path)], "docs(roadmap): ativar Intervenções Contextuais")


def update_board() -> None:
    path = Path("docs/project/knowledge-board.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 9.0.0", "version: 9.1.0", "board version")
    text = replace_once(
        text,
        "| PAS-001-OA-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Oportunidades Ativas |",
        "| PAS-001-OA-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Oportunidades Ativas |\n| PAS-001-IC-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais das Intervenções Contextuais |",
        "board asset row",
    )
    old_front = """| Próxima frente oficial | `07 — Intervenções Contextuais` |
| Estado da próxima frente | `Planned / concept consolidated` |
| Contrato final vigente | `PAS-001-OA-CONTRACT-001 1.0.0` |
| Progresso editorial de Oportunidades Ativas | `100%` |"""
    new_front = """| Capacidade ativa | `07 — Intervenções Contextuais` |
| Estado da capacidade ativa | `In progress` |
| Extensão normativa vigente | `PAS-001-IC-FOUNDATION-001 1.0.0` |
| Progresso editorial de Intervenções Contextuais | `20%` |"""
    text = replace_once(text, old_front, new_front, "board current front")
    text = replace_once(
        text,
        "| Foco imediato | Consolidar fundamentos iniciais de Intervenções Contextuais |",
        "| Foco imediato | Consolidar o ciclo de vida das Intervenções Contextuais |",
        "board focus",
    )
    text = replace_once(
        text,
        "| 07 — Intervenções Contextuais | Planned / concept consolidated | Agir, perguntar, esperar ou silenciar |",
        "| 07 — Intervenções Contextuais | In progress — 20% | Fundamentos iniciais consolidados; ciclo de vida é a próxima entrega |",
        "board capacity row",
    )
    section = """## Consolidação da Capacidade 07 — Intervenções Contextuais

### Fundamentos iniciais

- finalidade centrada em decidir se, quando, como e com qual intensidade a Guivos deve se manifestar;
- pergunta central sobre razão legítima, momento adequado e possibilidade de silêncio;
- Intervenção Contextual como manifestação deliberada, proporcional e explicável;
- singularidade de transformar contexto, relevância e temporalidade em decisão responsável de manifestação;
- decisões de agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar ou silenciar;
- silêncio como resultado legítimo e não como falha;
- oportunidade candidata e oportunidade admitida de intervenção;
- fluxo canônico desde sinal, fato, mudança ou solicitação até reavaliação;
- distinção entre intervenção, notificação, publicidade, recomendação, tarefa, oportunidade, experiência e transação;
- intervenções reativas e proativas com controles proporcionais;
- gatilhos legítimos e proibição de clique, tempo de tela, popularidade, comissão, patrocínio e estoque como gatilhos funcionais;
- entradas mínimas e uso de contexto autorizado;
- atenção separada de consentimento e interruptibilidade separada de disponibilidade técnica;
- importância e urgência como dimensões independentes;
- urgência legítima baseada em risco, prazo, segurança, perda objetiva ou necessidade declarada;
- sensibilidade, fadiga, frequência, repetição, intensidade e escalonamento;
- seleção de canal, consistência entre superfícies, conteúdo mínimo e explicabilidade;
- autonomia, autoridade, papéis funcionais e controles do participante;
- horários protegidos, adiamento, recusa, ocultação, bloqueio e silêncio;
- proteção reforçada de saúde, finanças, jurídico, religião, social, voluntariado e terceiros;
- intervenções comerciais identificadas e separadas das funcionais;
- relações governadas com as capacidades do Journey;
- limites da Guivos Intelligence, Platform Layer, produtos especializados e Guivos Ads;
- estados, eventos, responsabilidades, limites e comportamentos proibidos iniciais.

A Capacidade 07 está `In progress`, com progresso editorial de referência de `20%`.

"""
    text = replace_once(text, "## Conceitos internos preservados\n", section + "## Conceitos internos preservados\n", "board foundation section")
    text = replace_once(
        text,
        "| Oportunidades Ativas | Functionally complete — 100% |",
        "| Oportunidades Ativas | Functionally complete — 100% |\n| Intervenções Contextuais | In progress — 20% |\n| Fundamentos de Intervenções Contextuais | Normative 1.0.0 |\n| Oportunidade de intervenção | Condição em que a utilidade legítima potencial supera o custo provável da interrupção |\n| Silêncio contextual | Decisão funcional legítima de não manifestação |\n| Atenção contextual | Capacidade provável de receber e compreender uma manifestação; não representa consentimento |\n| Interruptibilidade | Adequação contextual de interromper o participante |\n| Fadiga de intervenção | Custo acumulado de manifestações recentes que deve reduzir pressão e frequência |",
        "board concepts",
    )
    text = text.replace("| Roadmap | 9.0.0 |", "| Roadmap | 9.1.0 |")
    text = text.replace("| Knowledge Board | 9.0.0 |", "| Knowledge Board | 9.1.0 |")
    text = replace_once(
        text,
        "| PAS-001-OA-CONTRACT-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-OA-CONTRACT-001 | Active 1.0.0 |\n| PAS-001-IC-FOUNDATION-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "board governance",
    )
    text = replace_once(
        text,
        "Consolidar os **fundamentos iniciais da Capacidade 07 — Intervenções Contextuais**, mantendo-a `Planned / concept consolidated` até aprovação normativa.",
        "Consolidar as **regras do ciclo de vida das Intervenções Contextuais**, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "board next activity",
    )
    path.write_text(text, encoding="utf-8")
    commit([str(path)], "docs(board): registrar fundamentos de Intervenções Contextuais")


def update_matrix_and_mkdocs() -> None:
    path = Path("docs/project/canonical-consolidation-matrix.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, "version: 1.7.0", "version: 1.8.0", "matrix version")
    old = "| Intervenção Contextual | Manter | Decisão de agir, perguntar, esperar, observar ou silenciar |"
    new = """| Intervenções Contextuais | Refinar | Capacidade 07 em desenvolvimento, com primeira extensão normativa e progresso editorial de 20% |
| Fundamentos Iniciais de Intervenções Contextuais | Manter | PAS-001-IC-FOUNDATION-001 1.0.0 define singularidade, decisões, silêncio, atenção, urgência, sensibilidade, fadiga, canais, autonomia, relações e limites |
| Intervenção Contextual | Refinar | Manifestação deliberada, proporcional e explicável que pode agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar ou silenciar |
| Oportunidade de intervenção | Manter | Condição em que a utilidade legítima potencial supera o custo provável da interrupção |
| Oportunidade admitida de intervenção | Manter | Candidatura com finalidade, autoridade, relevância, momento, risco, sensibilidade e canal suficientemente avaliados |
| Silêncio contextual | Manter | Resultado funcional legítimo de não manifestação atual, distinto de falha |
| Atenção contextual | Refinar | Capacidade provável de receber e compreender uma manifestação; não representa consentimento |
| Interruptibilidade | Manter | Adequação de interromper o participante em determinado momento e canal |
| Urgência de intervenção | Refinar | Proximidade temporal baseada em risco, prazo, segurança, perda objetiva, obrigação ou necessidade declarada |
| Fadiga de intervenção | Manter | Custo acumulado de manifestações recentes que deve reduzir frequência, intensidade ou produzir silêncio |
| Intensidade de intervenção | Refinar | Silenciosa, passiva, discreta, normal, destacada ou crítica, sempre proporcional |
| Horário protegido | Manter | Período em que intervenções são limitadas conforme preferências e exceções legítimas |
| Intervenção comercial | Refinar | Comunicação identificada, separada da funcional e proibida de utilizar contexto sensível ou urgência fabricada |"""
    text = replace_once(text, old, new, "matrix intervention concepts")
    text = replace_once(
        text,
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-OA-CONTRACT-001 1.0.0` consolida 75 KPIs em 15 famílias, 24 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas e contrato final, eleva Oportunidades Ativas para 100% e preserva neutralidade comercial, privacidade, confiabilidade, explicabilidade e controle do participante, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02, 03, 04, 05 e 06 estão funcionalmente concluídas. `PAS-001-IC-FOUNDATION-001 1.0.0` inicia normativamente a Capacidade 07, altera seu estado para `In progress`, estabelece progresso editorial de 20% e consolida finalidade, oportunidade de intervenção, silêncio, atenção, interruptibilidade, urgência, sensibilidade, fadiga, canais, autonomia, relações, responsabilidades e limites, sem promover candidatos arquiteturais à Canon.",
        "matrix reconciliation",
    )
    text = replace_once(
        text,
        "Consolidar os **fundamentos iniciais da Capacidade 07 — Intervenções Contextuais**, mantendo seu estado `Planned / concept consolidated` até a primeira extensão normativa.",
        "Consolidar as **regras do ciclo de vida da Capacidade 07 — Intervenções Contextuais**, incluindo identificação, candidatura, avaliação, admissão, programação, espera, apresentação, resposta, adiamento, silêncio, cancelamento, expiração, contestação, correção, escalonamento, frequência, propagação e falha segura.",
        "matrix next review",
    )
    path.write_text(text, encoding="utf-8")

    mkdocs = Path("mkdocs.yml")
    nav = mkdocs.read_text(encoding="utf-8")
    marker = "      - PAS-001-OA-CONTRACT-001 — Contrato Final das Oportunidades Ativas: product-architecture/pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md"
    if marker not in nav:
        raise RuntimeError("Missing MkDocs OA contract entry")
    nav = nav.replace(
        marker,
        marker + "\n      - PAS-001-IC-FOUNDATION-001 — Fundamentos de Intervenções Contextuais: product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md",
        1,
    )
    mkdocs.write_text(nav, encoding="utf-8")
    commit([str(path), str(mkdocs)], "docs(canon): consolidar fundamentos de Intervenções Contextuais")


def update_changelog_and_finish() -> None:
    path = Path("CHANGELOG.md")
    text = path.read_text(encoding="utf-8")
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    if marker not in text:
        raise RuntimeError("Missing changelog header")
    entry = """## 0.36.0 — Contextual Interventions Capability Foundation

- Criação de `PAS-001-IC-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Intervenções Contextuais`, versão `1.0.0`.
- Registro do documento como primeira extensão normativa da Capacidade 07 do `PAS-001 — Guivos Journey`.
- Definição da finalidade de governar se, quando, como e com qual intensidade a Guivos deverá se manifestar.
- Consolidação da pergunta central sobre razão legítima, momento adequado e possibilidade de silêncio.
- Definição da Intervenção Contextual como manifestação deliberada, proporcional e explicável.
- Consolidação da singularidade de transformar contexto, relevância e temporalidade em decisão responsável entre manifestação e silêncio.
- Definição das decisões de agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar e silenciar.
- Reconhecimento do silêncio como resultado funcional legítimo e distinto de falha.
- Definição da oportunidade candidata e da oportunidade admitida de intervenção.
- Consolidação do fluxo canônico desde sinal, fato, mudança ou solicitação até intervenção, silêncio e reavaliação.
- Separação entre intervenção, notificação técnica, publicidade, recomendação, comando, tarefa, oportunidade, experiência, transação e conteúdo editorial.
- Definição de intervenções reativas e proativas, com controles reforçados para manifestações proativas.
- Consolidação de gatilhos legítimos e proibição de clique, rolagem, tempo de tela, popularidade, comissão, margem, patrocínio e estoque como gatilhos funcionais.
- Definição de entradas mínimas e contexto de decisão minimizado.
- Separação entre atenção, consentimento e interruptibilidade.
- Separação entre importância e urgência e definição de urgência legítima.
- Definição de temporalidade, sensibilidade, fadiga, frequência, repetição, intensidade, escalonamento e desescalonamento.
- Consolidação dos canais e da consistência entre superfícies.
- Definição do conteúdo mínimo, da explicabilidade e da justificativa `Por que agora?`.
- Consolidação de autonomia, autoridade limitada, papéis funcionais e controles do participante.
- Definição de horários protegidos, adiamento, recusa, ocultação e bloqueio.
- Proteção de intervenções de saúde, finanças, jurídico, religião, espiritualidade, social e voluntariado.
- Separação entre intervenções funcionais, comerciais, institucionais e coletivas.
- Proteção de informações de terceiros.
- Definição das relações com Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Experiências e Evolução Contínua.
- Definição dos limites da Guivos Intelligence, Platform Layer, produtos especializados e Guivos Ads.
- Registro dos estados e eventos funcionais iniciais.
- Consolidação das responsabilidades, limites, comportamentos proibidos e critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.8.0` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap para `9.1.0`, do Knowledge Board para `9.1.0` e da Matriz de Consolidação Canônica para `1.8.0`.
- Atualização do README e da página inicial do GKR.
- Alteração da Capacidade 07 de `Planned / concept consolidated` para `In progress`.
- Estabelecimento do progresso editorial de referência de Intervenções Contextuais em 20%.
- Preservação das Capacidades 02, 03, 04, 05 e 06 como `Functionally complete`.
- Preservação da Capacidade 08 — Experiências como `Planned`.
- Definição do ciclo de vida de Intervenções Contextuais como próximo ponto exato de retomada.

"""
    text = text.replace(marker, marker + entry, 1)
    path.write_text(text, encoding="utf-8")

    normative_path = Path("docs/product-architecture/pas-001-intervencoes-contextuais-fundamentos-iniciais.md")
    normative = normative_path.read_text(encoding="utf-8")
    checks = {
        "start section": "# 2752. Finalidade da capacidade" in normative,
        "end section": "# 2837. Critérios de aceite e continuidade" in normative,
        "plain fences": 'id="' not in normative,
        "foundation id": "id: PAS-001-IC-FOUNDATION-001" in normative,
        "foundation state": "estado `Planned / concept consolidated` da Capacidade 07 por `In progress`" in normative,
        "README state": "07 — Intervenções Contextuais | In progress — 20%" in Path("README.md").read_text(encoding="utf-8"),
        "index state": "07 — Intervenções Contextuais | In progress — 20%" in Path("docs/index.md").read_text(encoding="utf-8"),
        "architecture version": "version: 1.8.0" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "architecture state": "A Capacidade 07 está **In progress**" in Path("docs/product-architecture/index.md").read_text(encoding="utf-8"),
        "roadmap version": "version: 9.1.0" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "roadmap state": "| 07 — Intervenções Contextuais | In progress | 20% |" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
        "board version": "version: 9.1.0" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "board state": "| 07 — Intervenções Contextuais | In progress — 20% |" in Path("docs/project/knowledge-board.md").read_text(encoding="utf-8"),
        "matrix version": "version: 1.8.0" in Path("docs/project/canonical-consolidation-matrix.md").read_text(encoding="utf-8"),
        "navigation": "pas-001-intervencoes-contextuais-fundamentos-iniciais.md" in Path("mkdocs.yml").read_text(encoding="utf-8"),
        "changelog": "## 0.36.0 — Contextual Interventions Capability Foundation" in text,
        "next lifecycle": "regras do ciclo de vida" in Path("docs/roadmap.md").read_text(encoding="utf-8"),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError("Validation failed: " + ", ".join(failed))

    for checked_path in [
        normative_path,
        Path("README.md"),
        Path("docs/index.md"),
        Path("docs/product-architecture/index.md"),
        Path("docs/roadmap.md"),
        Path("docs/project/knowledge-board.md"),
        Path("docs/project/canonical-consolidation-matrix.md"),
        Path("mkdocs.yml"),
    ]:
        if 'id="' in checked_path.read_text(encoding="utf-8"):
            raise RuntimeError(f"Generated fence id found in {checked_path}")

    run("git", "diff", "--check")
    run("git", "add", "CHANGELOG.md")
    run("git", "rm", ".github/workflows/apply-approved-ic-foundation.yml")
    run("git", "rm", ".github/scripts/apply_ic_foundation.py")
    run("git", "commit", "-m", "docs(changelog): registrar fundamentos de Intervenções Contextuais")
    branch = os.environ.get("GITHUB_HEAD_REF") or os.environ["GITHUB_REF_NAME"]
    run("git", "push", "origin", f"HEAD:{branch}")


def main() -> None:
    update_readme()
    update_index()
    update_architecture()
    update_roadmap()
    update_board()
    update_matrix_and_mkdocs()
    update_changelog_and_finish()


if __name__ == "__main__":
    main()
