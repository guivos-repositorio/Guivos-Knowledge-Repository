from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PA = DOCS / "product-architecture"


def rw(path, fn):
    text = path.read_text(encoding="utf-8")
    path.write_text(fn(text), encoding="utf-8")


def once(text, old, new, label):
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: {text.count(old)} occurrences")
    return text.replace(old, new, 1)


def ver(text, old, new, label):
    return once(text, f"version: {old}", f"version: {new}", label)

# Product Architecture index.
def product(text):
    text = ver(text, "1.25.0", "1.26.0", "product version")
    text = once(text,
        "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base com as extensões normativas, classifica estados e pontos de retomada históricos e define a hierarquia documental. Após o contrato final da Capacidade 01, o parecer vigente passa a `Conditionally ready — final PAS-001 audit required`.\n\nA Capacidade 01 está `Functionally complete — 100%` pelas extensões `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001`. Todas as nove capacidades estão funcionalmente concluídas.",
        "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` avalia os 15 gates, consolida supersessão e autoridade documental e emite `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.\n\nTodas as nove capacidades estão funcionalmente concluídas. O `PAS-001` permanece `Draft 0.5.0` até validação e publicação formal da edição candidata.", "product readiness")
    text = once(text, "A capacidade está `Functionally complete — 100%`; o próximo ponto é `PAS-001-AUDIT-001`.", "A capacidade está `Functionally complete — 100%`. A auditoria final foi concluída por `PAS-001-AUDIT-001 1.0.0`.", "product cap01")
    return once(text, "### Capacidade 01 — Captura de Contexto", "### Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, inventariou 54 extensões, validou links, versões, navegação e coerência entre camadas e autorizou a edição candidata `PAS-001 1.0.0`.\n\n### Capacidade 01 — Captura de Contexto", "product audit")
rw(PA / "index.md", product)

# Roadmap.
def roadmap(text):
    text = ver(text, "11.6.0", "11.7.0", "roadmap version")
    text = once(text, "- **Reconciliação vigente:** `PAS-001-RECON-001 1.0.0`.", "- **Reconciliação vigente:** `PAS-001-RECON-001 1.0.0`.\n- **Auditoria final vigente:** `PAS-001-AUDIT-001 1.0.0`.", "roadmap audit")
    text = once(text, "- **Parecer de prontidão:** `Conditionally ready — final PAS-001 audit required`.", "- **Parecer de prontidão:** `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.", "roadmap readiness")
    text = once(text, "- **Lacuna funcional bloqueante:** nenhuma no nível de especificação das capacidades; permanece obrigatória a auditoria final do `PAS-001`.", "- **Lacuna bloqueante:** nenhuma para iniciar a consolidação editorial; quatro ações editoriais não bloqueantes estão registradas.", "roadmap gap")
    text = once(text, "A Capacidade 01 foi concluída por `PAS-001-CC-CONTRACT-001 1.0.0`. O próximo trabalho deverá executar a **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey**, mantendo o `PAS-001` em `Draft 0.5.0` até a decisão formal de publicação.", "`PAS-001-AUDIT-001 1.0.0` concluiu a auditoria com parecer `Ready for consolidation`. O próximo trabalho deverá criar a **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0**, mantendo o arquivo vigente em `Draft 0.5.0` até decisão `Ready for publication`.", "roadmap direction")
    text = once(text, "## Capacidade 01 — Fechamento formal concluído", "## Auditoria final concluída\n\nA auditoria avaliou 15 gates, inventariou 54 extensões e registrou quatro ações editoriais não bloqueantes.\n\n## Capacidade 01 — Fechamento formal concluído", "roadmap section")
    return text.replace("Todas as capacidades do Journey estão funcionalmente concluídas; resta a auditoria final do `PAS-001`.", "Todas as capacidades estão funcionalmente concluídas; a próxima etapa é a edição candidata federada do `PAS-001 1.0.0`.")
rw(DOCS / "roadmap.md", roadmap)

# Board.
def board(text):
    text = ver(text, "11.6.0", "11.7.0", "board version")
    text = once(text, "| PAS-001-RECON-001 | Active 1.0.0 | Reconciliar autoridade, supersessão e prontidão do Journey |", "| PAS-001-RECON-001 | Active 1.0.0 | Reconciliar autoridade, supersessão e prontidão do Journey |\n| PAS-001-AUDIT-001 | Active 1.0.0 | Auditar os 15 gates e autorizar a consolidação editorial do PAS-001 |", "board row")
    pairs = [
    ("| Parecer de prontidão | `Conditionally ready — final PAS-001 audit required` |","| Parecer de prontidão | `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized` |"),
    ("| Lacuna bloqueante | Nenhuma lacuna funcional de capacidade; auditoria final do PAS-001 permanece obrigatória |","| Lacuna bloqueante | Nenhuma para iniciar a consolidação; quatro ações editoriais não bloqueantes registradas |"),
    ("| Frente ativa | Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey |","| Frente ativa | Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0 |"),
    ("| Estado da frente ativa | Auditoria normativa e editorial |","| Estado da frente ativa | Edição candidata autorizada; publicação ainda não autorizada |"),
    ("| Foco imediato | Criar `PAS-001-AUDIT-001` e decidir a prontidão para publicação do `PAS-001 1.0.0` |","| Foco imediato | Criar a edição candidata `PAS-001 1.0.0`, validar regressões e decidir `Ready for publication` |")]
    for i,(a,b) in enumerate(pairs): text = once(text,a,b,f"board {i}")
    return once(text, "## Capacidades do Journey", "## Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, registrou supersessão e autoridade e autorizou a edição candidata. A publicação de `1.0.0` permanece condicionada.\n\n## Capacidades do Journey", "board section")
rw(DOCS / "project" / "knowledge-board.md", board)

# Matrix.
def matrix(text):
    text = ver(text, "1.25.0", "1.26.0", "matrix version")
    if "## Auditoria final do PAS-001" in text: raise RuntimeError("matrix section exists")
    return text.rstrip() + "\n\n## Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` registra a matriz final de supersessão e o registro transversal de autoridade documental.\n\nCampos obrigatórios: seção original, conceito, documento substituto, decisão, ação editorial, necessidade de reabertura, documento pai, autoridade, dependências e critérios de reabertura.\n\nParecer: `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.\n"
rw(DOCS / "project" / "canonical-consolidation-matrix.md", matrix)

# Changelog.
def changelog(text):
    entry = """## 0.54.0 — PAS-001 Final Readiness Audit

- Criação de `PAS-001-AUDIT-001 1.0.0`.
- Avaliação e aprovação dos 15 gates de prontidão.
- Inventário de 54 extensões normativas e nove contratos finais ativos.
- Validação de metadados, links, versões, navegação e coerência entre camadas.
- Consolidação do mapa final, perguntas centrais, matriz de supersessão e registro de autoridade.
- Registro de quatro ações editoriais não bloqueantes e nenhum achado crítico ou alto aberto.
- Parecer `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.
- Manutenção do `PAS-001` em `Draft 0.5.0`; nenhuma publicação automática.
- Arquitetura e Matriz `1.26.0`; Roadmap e Board `11.7.0`.
- Próximo ponto: edição candidata consolidada e federada do `PAS-001 1.0.0`.


"""
    return once(text, "## 0.53.0 — Capture Context Final Contract", entry + "## 0.53.0 — Capture Context Final Contract", "changelog")
rw(ROOT / "CHANGELOG.md", changelog)

# PAS base.
def pas(text):
    text = once(text, "  - PAS-001-CC-CONTRACT-001\n", "  - PAS-001-CC-CONTRACT-001\n  - PAS-001-AUDIT-001\n", "pas related")
    return once(text, "> **Aviso normativo de reconciliação:** `PAS-001-RECON-001 1.0.0` estabelece que esta especificação-base permanece `Draft 0.5.0` e classifica o mapa e os pontos de retomada históricos. `PAS-001-CC-CONTRACT-001 1.0.0` conclui funcionalmente a Capacidade 01 e atualiza a prontidão para `Conditionally ready — final PAS-001 audit required`.", "> **Aviso normativo de reconciliação:** `PAS-001-RECON-001 1.0.0` estabelece que esta especificação-base permanece `Draft 0.5.0`. `PAS-001-CC-CONTRACT-001 1.0.0` conclui a Capacidade 01. `PAS-001-AUDIT-001 1.0.0` aprova os 15 gates e atualiza a prontidão para `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`, sem publicar a versão `1.0.0`.", "pas notice")
rw(PA / "pas-001-guivos-journey.md", pas)

# README.
def readme(text):
    text = once(text, "- **Parecer de prontidão:** `Conditionally ready — final PAS-001 audit required`", "- **Auditoria final:** PAS-001-AUDIT-001 1.0.0\n- **Parecer de prontidão:** `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`", "readme readiness")
    text = once(text, "- **Próxima frente:** `PAS-001-AUDIT-001` — Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey", "- **Próxima frente:** Edição Consolidada e Federada do `PAS-001 — Guivos Journey 1.0.0`", "readme next")
    text = once(text, "A capacidade está **Functionally complete — 100%**. Todas as nove capacidades do Journey estão funcionalmente concluídas; o `PAS-001` permanece em `Draft 0.5.0` até a auditoria final.", "A capacidade está **Functionally complete — 100%**. Todas as nove capacidades estão concluídas; a auditoria autoriza a edição candidata, mas o arquivo vigente permanece `Draft 0.5.0`.", "readme cap")
    text = once(text, "- [Contrato Final da Captura de Contexto](docs/product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md)", "- [Contrato Final da Captura de Contexto](docs/product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md)\n- [Auditoria Final do PAS-001](docs/product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md)", "readme link")
    return text.replace("Retomar na **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey**.", "Retomar na **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0**.")
rw(ROOT / "README.md", readme)

# Docs index.
def index(text):
    text = once(text, "- prontidão `Conditionally ready — final PAS-001 audit required`;", "- `PAS-001-AUDIT-001 1.0.0` como auditoria final vigente;\n- prontidão `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`;", "index readiness")
    text = once(text, "Executar a **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey** por `PAS-001-AUDIT-001`, preservando o `PAS-001` em `Draft 0.5.0` até a decisão formal de publicação.", "Criar a **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0**, preservando o arquivo vigente em `Draft 0.5.0` até validação e decisão `Ready for publication`.", "index mission")
    text = once(text, "- [Contrato Final da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md)", "- [Contrato Final da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md)\n- [Auditoria Final do PAS-001](product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md)", "index link")
    return once(text, "Retomar na **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey**.", "Retomar na **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0**.", "index resumption")
rw(DOCS / "index.md", index)

# MkDocs.
def mkdocs(text):
    return once(text, "      - PAS-001-CC-CONTRACT-001 — Contrato Final da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md", "      - PAS-001-CC-CONTRACT-001 — Contrato Final da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md\n      - PAS-001-AUDIT-001 — Auditoria Final de Prontidão: product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md", "mkdocs")
rw(ROOT / "mkdocs.yml", mkdocs)
print("canonical synchronization complete")
