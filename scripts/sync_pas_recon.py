from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-18"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one anchor, found {count}: {old[:100]!r}")
    write(path, text.replace(old, new, 1))


def regex_once(path: str, pattern: str, replacement: str, flags: int = 0) -> None:
    text = read(path)
    new, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{path}: regex anchor not found exactly once: {pattern}")
    write(path, new)


def numbered_items(section: str) -> list[int]:
    return [int(n) for n in re.findall(r"(?m)^(\d+)\. ", section)]


def validate_contract() -> None:
    text = read("docs/product-architecture/pas-001-guivos-journey-reconciliacao-fechamento.md")
    headings = [int(n) for n in re.findall(r"(?m)^# (\d+)\.", text)]
    expected = list(range(4492, 4566))
    if headings != expected:
        raise RuntimeError(f"invalid section sequence: {headings[:3]}...{headings[-3:] if headings else []}")
    prohibited = re.search(r"# 4554\.[\s\S]*?(?=# 4555\.)", text)
    acceptance = re.search(r"# 4555\.[\s\S]*?(?=# 4556\.)", text)
    if not prohibited or numbered_items(prohibited.group(0)) != list(range(1, 21)):
        raise RuntimeError("expected 20 prohibited behaviors")
    if not acceptance or numbered_items(acceptance.group(0)) != list(range(1, 53)):
        raise RuntimeError("expected 52 acceptance criteria")
    required = [
        "Not ready — Capability 01 closure required.",
        "PAS-001-CC-LIFECYCLE-001",
        "PAS-001-CC-EVENT-INTEGRATION-001",
        "PAS-001-CC-CONTRACT-001",
        "Registro de Captura de Contexto",
    ]
    for value in required:
        if value not in text:
            raise RuntimeError(f"missing required contract value: {value}")


def update_pas_base() -> None:
    path = "docs/product-architecture/pas-001-guivos-journey.md"
    replace_once(path, "last_updated: 2026-07-13", f"last_updated: {DATE}")
    replace_once(path, "  - AR-001\n  - DR-001", "  - AR-001\n  - PAS-001-RECON-001\n  - DR-001")
    replace_once(
        path,
        "# PAS-001 — Guivos Journey Product Architecture Specification\n",
        "# PAS-001 — Guivos Journey Product Architecture Specification\n\n"
        "> **Aviso normativo de reconciliação:** `PAS-001-RECON-001 1.0.0` estabelece que esta especificação-base permanece `Draft 0.5.0`, classifica o mapa e os pontos de retomada históricos conforme as extensões posteriores e registra a prontidão como `Not ready — Capability 01 closure required`.\n",
    )
    replace_once(
        path,
        "## 7. Mapa de Capacidades do Journey\n\n| Capacidade | Pergunta central | Estado |",
        "## 7. Mapa de Capacidades do Journey\n\n> **Estado histórico:** a tabela abaixo registra o estado editorial da versão `0.5.0`. Os estados efetivos são governados por `PAS-001-RECON-001 1.0.0` e pelos contratos finais das capacidades.\n\n| Capacidade | Pergunta central | Estado |",
    )
    replace_once(
        path,
        "## 45. Ponto de retomada\n\nRetomar na Capacidade 02 — Contexto Vivo, definindo os estados funcionais de cada dimensão e, em seguida, as regras de atualização e envelhecimento.",
        "## 45. Ponto de retomada\n\nO ponto de retomada original desta versão é histórico.\n\nRetomar no **Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto**, por meio de `PAS-001-CC-LIFECYCLE-001`.",
    )


def update_product_architecture() -> None:
    path = "docs/product-architecture/index.md"
    replace_once(path, "version: 1.21.0", "version: 1.22.0")
    replace_once(
        path,
        "O `PAS-001 — Guivos Journey 0.5.0` é a especificação-base da Experience Layer.\n\n### Capacidade 02 — Contexto Vivo",
        "O `PAS-001 — Guivos Journey 0.5.0` é a especificação-base da Experience Layer.\n\n"
        "### Reconciliação e prontidão do PAS-001\n\n"
        "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base com as 51 extensões normativas das Capacidades 02 a 09, classifica estados e pontos de retomada históricos, define a hierarquia documental e registra o parecer `Not ready — Capability 01 closure required`.\n\n"
        "A Capacidade 01 permanece `Substantially complete` e deverá ser concluída por `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001`.\n\n"
        "### Capacidade 02 — Contexto Vivo",
    )
    replace_once(
        path,
        "A próxima frente oficial é a Reconciliação e o Fechamento do `PAS-001 — Guivos Journey`, com revisão da Capacidade 01, consolidação do mapa de capacidades e avaliação de prontidão para `PAS-001 1.0.0`.",
        "`PAS-001-RECON-001 1.0.0` conclui a avaliação de prontidão, preserva as Capacidades 02 a 09 como `Functionally complete`, mantém a Capacidade 01 como `Substantially complete` e impede o avanço direto para `PAS-001 1.0.0`.\n\nA próxima frente oficial é o **Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto**, por meio de `PAS-001-CC-LIFECYCLE-001`.",
    )


def update_roadmap() -> None:
    path = "docs/roadmap.md"
    replace_once(path, "version: 11.2.0", "version: 11.3.0")
    replace_once(
        path,
        "- **Especificação-base ativa:** `PAS-001 — Guivos Journey 0.5.0`.\n",
        "- **Especificação-base ativa:** `PAS-001 — Guivos Journey 0.5.0`.\n"
        "- **Reconciliação vigente:** `PAS-001-RECON-001 1.0.0`.\n"
        "- **Parecer de prontidão:** `Not ready — Capability 01 closure required`.\n"
        "- **Lacuna bloqueante:** ausência de fechamento funcional formal da Capacidade 01 — Captura de Contexto.\n",
    )
    replace_once(
        path,
        "O próximo trabalho deverá realizar a Reconciliação e o Fechamento do `PAS-001 — Guivos Journey`, revisar a Capacidade 01, consolidar o mapa final de capacidades e avaliar a prontidão para `PAS-001 1.0.0`.",
        "A reconciliação do `PAS-001 — Guivos Journey` foi concluída por `PAS-001-RECON-001 1.0.0`. O próximo trabalho deverá consolidar o **Ciclo de Vida e os Estados Funcionais da Capacidade 01 — Captura de Contexto**, sem avançar diretamente para `PAS-001 1.0.0`.",
    )
    regex_once(
        path,
        r"## Ponto exato de retomada\n\nRetomar na \*\*Reconciliação e Fechamento do PAS-001 — Guivos Journey\*\*\.\n\nPróxima entrega:\n\n1\. revisar o estado da Capacidade 01 — Captura de Contexto;\n2\. atualizar o Mapa de Capacidades do Journey;\n3\. consolidar as extensões normativas das Capacidades 02 a 09;\n4\. resolver divergências residuais e disposições substituídas;\n5\. avaliar a prontidão para `PAS-001 1\.0\.0` e definir o próximo ciclo de Product Engineering\.",
        "## Ponto exato de retomada\n\nRetomar no **Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto**.\n\nPróxima entrega:\n\n1. criar `PAS-001-CC-LIFECYCLE-001`;\n2. consolidar o `Registro de Captura de Contexto`;\n3. definir estados independentes e transições;\n4. governar síntese, confirmação, autorização, persistência temporária, contestação e encerramento;\n5. preparar eventos, integrações e contrato final da Capacidade 01.",
    )


def update_board() -> None:
    path = "docs/project/knowledge-board.md"
    replace_once(path, "version: 11.2.0", "version: 11.3.0")
    replace_once(
        path,
        "| PAS-001 — Guivos Journey | Draft 0.5.0 — Active | Especificar a Experience Layer |\n",
        "| PAS-001 — Guivos Journey | Draft 0.5.0 — Active | Especificar a Experience Layer |\n"
        "| PAS-001-RECON-001 | Active 1.0.0 | Reconciliar autoridade, supersessão e prontidão do Journey |\n",
    )
    replace_once(
        path,
        "| Especificação-base | `PAS-001 — Guivos Journey 0.5.0` |\n",
        "| Especificação-base | `PAS-001 — Guivos Journey 0.5.0` |\n"
        "| Reconciliação vigente | `PAS-001-RECON-001 1.0.0` |\n"
        "| Parecer de prontidão | `Not ready — Capability 01 closure required` |\n"
        "| Lacuna bloqueante | Fechamento funcional formal da Capacidade 01 — Captura de Contexto |\n"
        "| Extensões projetadas da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` |\n",
    )
    replace_once(path, "| Frente ativa | Reconciliação e Fechamento do `PAS-001 — Guivos Journey` |", "| Frente ativa | Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto |")
    replace_once(path, "| Estado da frente ativa | Próxima frente oficial |", "| Estado da frente ativa | Próximo ciclo normativo |")
    replace_once(path, "| Foco imediato | Reconciliar e fechar o PAS-001 — Guivos Journey, revisar a Capacidade 01 e avaliar prontidão para 1.0.0 |", "| Foco imediato | Criar `PAS-001-CC-LIFECYCLE-001` e iniciar o fechamento formal da Capacidade 01 |")
    replace_once(path, "| 01 — Captura de Contexto | Substantially complete | Fluxo e contrato registrados |", "| 01 — Captura de Contexto | Substantially complete | Fechamento formal requerido; ciclo de vida, eventos/integrações e contrato final projetados |")


def update_matrix() -> None:
    path = "docs/project/canonical-consolidation-matrix.md"
    replace_once(path, "version: 1.21.0", "version: 1.22.0")
    anchor = "| Conceito | Decisão | Situação |\n|---|---|---|\n"
    rows = (
        "| Reconciliação do PAS-001 | Manter | `PAS-001-RECON-001 1.0.0` governa hierarquia, supersessão, inventário e prontidão |\n"
        "| Prontidão para PAS-001 1.0.0 | Refinar | Estado vigente `Not ready — Capability 01 closure required` |\n"
        "| Mapa de Capacidades da seção 7 | Histórico | Estados da versão 0.5.0 substituídos pelas extensões normativas |\n"
        "| Captura de Contexto | Refinar | `Substantially complete`; requer fechamento formal por três extensões |\n"
        "| Registro de Captura de Contexto | Manter | Unidade funcional recomendada para sessão, entradas, síntese, confirmações e histórico |\n"
        "| Sessão de Captura de Contexto | Refinar | Ciclo próprio, estados independentes, encerramento e falha segura |\n"
        "| Síntese inicial suficientemente confirmada | Refinar | Substitui a noção de contexto inicial como verdade completa ou autorização universal |\n"
        "| Persistência temporária | Manter | Alternativa legítima sem incorporação automática ao Contexto Vivo |\n"
        "| Distância para Evolução | Restringir | Linguagem estratégica não normativa; não pode operar como score, percentual ou ranking humano |\n"
        "| Ativação e apresentação de oportunidade | Refinar | Oportunidades governa ativação; Intervenções governa apresentação |\n"
        "| Experiência e evolução | Refinar | Vivência e trajetória de mudança permanecem conceitos funcionalmente distintos |\n"
        "| Edição PAS-001 1.0.0 | Planejar | Especificação consolidada e federada após fechamento da Capacidade 01 e auditoria final |\n"
    )
    replace_once(path, anchor, anchor + rows)


def update_readme() -> None:
    path = "README.md"
    replace_once(
        path,
        "- **Próxima frente:** Reconciliação e Fechamento do PAS-001 — Guivos Journey\n",
        "- **Reconciliação vigente:** PAS-001-RECON-001 1.0.0\n"
        "- **Parecer de prontidão:** `Not ready — Capability 01 closure required`\n"
        "- **Próxima frente:** Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto\n",
    )
    replace_once(
        path,
        "- [PAS-001 — Guivos Journey](docs/product-architecture/pas-001-guivos-journey.md)\n",
        "- [PAS-001 — Guivos Journey](docs/product-architecture/pas-001-guivos-journey.md)\n"
        "- [Reconciliação e Prontidão do Guivos Journey](docs/product-architecture/pas-001-guivos-journey-reconciliacao-fechamento.md)\n",
    )
    regex_once(
        path,
        r"## Ponto exato de retomada\n\nRetomar na \*\*Reconciliação e Fechamento do PAS-001 — Guivos Journey\*\*\.\n\nPróxima entrega:\n\n(?:- .*\n)+\n\n## Product Engineering",
        "## Ponto exato de retomada\n\nRetomar no **Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto**.\n\nPróxima entrega:\n\n- criar `PAS-001-CC-LIFECYCLE-001`;\n- consolidar o Registro de Captura de Contexto;\n- definir estados, transições, autorizações, contestação e encerramento;\n- preparar eventos, integrações e contrato final;\n- preservar o `PAS-001` em `0.5.0` até a auditoria final.\n\n## Product Engineering",
        flags=re.MULTILINE,
    )
    replace_once(
        path,
        "As Capacidades 02 a 09 estão funcionalmente concluídas. A próxima frente é a Reconciliação e o Fechamento do `PAS-001 — Guivos Journey`.",
        "As Capacidades 02 a 09 estão funcionalmente concluídas. `PAS-001-RECON-001 1.0.0` registra que a Capacidade 01 permanece `Substantially complete` e bloqueia o avanço direto para `PAS-001 1.0.0`.",
    )


def update_docs_index() -> None:
    path = "docs/index.md"
    replace_once(
        path,
        "- `PAS-001 — Guivos Journey 0.5.0` como especificação-base;\n",
        "- `PAS-001 — Guivos Journey 0.5.0` como especificação-base;\n"
        "- `PAS-001-RECON-001 1.0.0` como reconciliação normativa vigente;\n"
        "- prontidão `Not ready — Capability 01 closure required`;\n",
    )
    replace_once(
        path,
        "Realizar a **Reconciliação e o Fechamento do PAS-001 — Guivos Journey**, revisar a Capacidade 01, consolidar o mapa de capacidades e avaliar a prontidão para `PAS-001 1.0.0`.",
        "Consolidar o **Ciclo de Vida e os Estados Funcionais da Capacidade 01 — Captura de Contexto**, iniciando seu fechamento formal por `PAS-001-CC-LIFECYCLE-001`.",
    )
    replace_once(
        path,
        "- [PAS-001 — Guivos Journey](product-architecture/pas-001-guivos-journey.md)\n",
        "- [PAS-001 — Guivos Journey](product-architecture/pas-001-guivos-journey.md)\n"
        "- [Reconciliação e Prontidão do Guivos Journey](product-architecture/pas-001-guivos-journey-reconciliacao-fechamento.md)\n",
    )
    replace_once(path, "Retomar na **Reconciliação e Fechamento do PAS-001 — Guivos Journey**.", "Retomar no **Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto**.")


def update_mkdocs() -> None:
    path = "mkdocs.yml"
    replace_once(
        path,
        "      - PAS-001 — Guivos Journey: product-architecture/pas-001-guivos-journey.md\n",
        "      - PAS-001 — Guivos Journey: product-architecture/pas-001-guivos-journey.md\n"
        "      - PAS-001-RECON-001 — Reconciliação e Prontidão: product-architecture/pas-001-guivos-journey-reconciliacao-fechamento.md\n",
    )


def update_changelog() -> None:
    path = "CHANGELOG.md"
    entry = """
## 0.50.0 — PAS-001 Reconciliation and Readiness

- Criação de `PAS-001-RECON-001 — Reconciliação, Supersessão e Prontidão do Guivos Journey`, versão `1.0.0`.
- Registro da hierarquia normativa, regra de especificidade, temporalidade documental e categorias de reconciliação.
- Reconciliação das 51 extensões normativas das Capacidades 02 a 09 com o `PAS-001 0.5.0`.
- Classificação do mapa e dos pontos de retomada históricos da especificação-base.
- Preservação das Capacidades 02 a 09 como `Functionally complete`.
- Manutenção da Capacidade 01 — Captura de Contexto como `Substantially complete`.
- Registro do parecer `Not ready — Capability 01 closure required` para `PAS-001 1.0.0`.
- Definição de `Registro de Captura de Contexto` como unidade funcional recomendada.
- Definição do caminho de fechamento por `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001`.
- Reconciliação dos conceitos Oportunidade Ativa, Experiência, Evolução Contínua, Distância para Evolução, contexto inicial confirmado e primeiro valor.
- Definição de matriz de supersessão, registro de autoridade, gates e estados de prontidão.
- Registro de 20 comportamentos proibidos e 52 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.22.0`.
- Atualização do Roadmap e do Knowledge Board para `11.3.0`.
- Atualização da Matriz de Consolidação Canônica para `1.22.0`.
- Manutenção do `PAS-001` em `0.5.0`.
- Atualização do README, da página inicial e da navegação do MkDocs.
- Definição do Ciclo de Vida e Estados Funcionais da Capacidade 01 como próximo ponto exato.

"""
    replace_once(path, "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n", "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n" + entry)


def validate_outputs() -> None:
    checks = {
        "docs/product-architecture/index.md": ["version: 1.22.0", "PAS-001-RECON-001 1.0.0", "PAS-001-CC-LIFECYCLE-001"],
        "docs/roadmap.md": ["version: 11.3.0", "Not ready — Capability 01 closure required", "Ciclo de Vida e Estados Funcionais"],
        "docs/project/knowledge-board.md": ["version: 11.3.0", "PAS-001-RECON-001", "PAS-001-CC-EVENT-INTEGRATION-001"],
        "docs/project/canonical-consolidation-matrix.md": ["version: 1.22.0", "Distância para Evolução", "Edição PAS-001 1.0.0"],
        "CHANGELOG.md": ["## 0.50.0 — PAS-001 Reconciliation and Readiness"],
        "README.md": ["Reconciliação vigente", "Ciclo de Vida e Estados Funcionais"],
        "docs/index.md": ["PAS-001-RECON-001 1.0.0", "Ciclo de Vida e Estados Funcionais"],
        "mkdocs.yml": ["PAS-001-RECON-001 — Reconciliação e Prontidão"],
        "docs/product-architecture/pas-001-guivos-journey.md": ["version: 0.5.0", "Not ready — Capability 01 closure required", "Estado histórico"],
    }
    for path, values in checks.items():
        text = read(path)
        for value in values:
            if value not in text:
                raise RuntimeError(f"{path}: missing validation value {value!r}")
    if "version: 1.0.0" in read("docs/product-architecture/pas-001-guivos-journey.md")[:200]:
        raise RuntimeError("PAS-001 version advanced unexpectedly")


def cleanup_and_commit() -> None:
    for relative in ["scripts/sync_pas_recon.py", ".github/workflows/sync-pas-recon.yml"]:
        path = ROOT / relative
        if path.exists():
            path.unlink()
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True, cwd=ROOT)
    subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True, cwd=ROOT)
    subprocess.run(["git", "add", "-A"], check=True, cwd=ROOT)
    status = subprocess.run(["git", "status", "--porcelain"], check=True, cwd=ROOT, capture_output=True, text=True)
    if not status.stdout.strip():
        return
    subprocess.run(["git", "commit", "-m", "synchronize PAS-001 reconciliation artifacts"], check=True, cwd=ROOT)
    subprocess.run(["git", "push", "origin", "HEAD"], check=True, cwd=ROOT)


def main() -> None:
    validate_contract()
    update_pas_base()
    update_product_architecture()
    update_roadmap()
    update_board()
    update_matrix()
    update_readme()
    update_docs_index()
    update_mkdocs()
    update_changelog()
    validate_outputs()
    cleanup_and_commit()


if __name__ == "__main__":
    main()
