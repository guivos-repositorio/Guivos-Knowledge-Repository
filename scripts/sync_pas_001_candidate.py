from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 anchor, found {count}")
    return text.replace(old, new, 1)


# Preserve canonical PAS-001 exactly as Draft 0.5.0.
pas = read("docs/product-architecture/pas-001-guivos-journey.md")
if "status: draft" not in pas or "version: 0.5.0" not in pas:
    raise RuntimeError("PAS-001 canonical file is not Draft 0.5.0")
if "PAS-001-CANDIDATE-001" in pas:
    raise RuntimeError("PAS-001 canonical file must remain untouched by candidate synchronization")

# README
path = "README.md"
t = read(path)
t = replace_once(t,
    "- **Auditoria final:** PAS-001-AUDIT-001 1.0.0\n- **Parecer de prontidão:** `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`\n- **Próxima frente:** Edição Consolidada e Federada do `PAS-001 — Guivos Journey 1.0.0`",
    "- **Auditoria final:** PAS-001-AUDIT-001 1.0.0\n- **Edição candidata:** PAS-001-CANDIDATE-001 1.0.0-rc.1\n- **Parecer de prontidão:** `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`\n- **Próxima frente:** `PAS-001-RELEASE-VALIDATION-001` — Validação Editorial e Normativa da Edição Candidata",
    "README status")
t = replace_once(t,
    "- [Auditoria Final do PAS-001](docs/product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md)",
    "- [Auditoria Final do PAS-001](docs/product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md)\n- [Edição Candidata Federada do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)",
    "README candidate link")
write(path, t)

# Docs home
path = "docs/index.md"
t = read(path)
t = replace_once(t,
    "- `PAS-001-AUDIT-001 1.0.0` como auditoria final vigente;\n- prontidão `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`;",
    "- `PAS-001-AUDIT-001 1.0.0` como auditoria final vigente;\n- `PAS-001-CANDIDATE-001 1.0.0-rc.1` como edição candidata consolidada e federada;\n- prontidão `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`;",
    "docs index status")
t = replace_once(t,
    "Criar a **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0**, preservando o arquivo vigente em `Draft 0.5.0` até validação e decisão `Ready for publication`.",
    "Executar a **Validação Editorial e Normativa da Edição Candidata do PAS-001 — Guivos Journey 1.0.0**, preservando o arquivo canônico em `Draft 0.5.0` até decisão formal `Ready for publication`.",
    "docs index mission")
t = replace_once(t,
    "- [Auditoria Final do PAS-001](product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md)",
    "- [Auditoria Final do PAS-001](product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md)\n- [Edição Candidata Federada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)",
    "docs index candidate link")
write(path, t)

# Product Architecture index
path = "docs/product-architecture/index.md"
t = read(path)
t = replace_once(t, "version: 1.26.0", "version: 1.27.0", "architecture version")
t = replace_once(t,
    "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` avalia os 15 gates, consolida supersessão e autoridade documental e emite `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.\n\nTodas as nove capacidades estão funcionalmente concluídas. O `PAS-001` permanece `Draft 0.5.0` até validação e publicação formal da edição candidata.\n\n### Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, inventariou 54 extensões, validou links, versões, navegação e coerência entre camadas e autorizou a edição candidata `PAS-001 1.0.0`.",
    "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates e autorizou a consolidação editorial. `PAS-001-CANDIDATE-001 1.0.0-rc.1` materializa a edição candidata federada e emite `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.\n\nTodas as nove capacidades estão funcionalmente concluídas. O `PAS-001` canônico permanece `Draft 0.5.0` até validação e aprovação formal de publicação.\n\n### Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, inventariou 54 extensões, validou links, versões, navegação e coerência entre camadas.\n\n### Edição candidata do PAS-001\n\n`PAS-001-CANDIDATE-001 1.0.0-rc.1` consolida filosofia, arquitetura em camadas, princípios, invariantes, mapa das nove capacidades, perguntas centrais, fronteiras, autoridade federada e critérios globais, preservando os contratos especializados e o arquivo canônico `0.5.0`.",
    "architecture candidate section")
write(path, t)

# Roadmap
path = "docs/roadmap.md"
t = read(path)
t = replace_once(t, "version: 11.7.0", "version: 11.8.0", "roadmap version")
t = replace_once(t,
    "- **Auditoria final vigente:** `PAS-001-AUDIT-001 1.0.0`.\n- **Extensões vigentes da Capacidade 01:**",
    "- **Auditoria final vigente:** `PAS-001-AUDIT-001 1.0.0`.\n- **Edição candidata vigente:** `PAS-001-CANDIDATE-001 1.0.0-rc.1`.\n- **Extensões vigentes da Capacidade 01:**",
    "roadmap candidate")
t = replace_once(t,
    "- **Parecer de prontidão:** `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.\n- **Lacuna bloqueante:** nenhuma para iniciar a consolidação editorial; quatro ações editoriais não bloqueantes estão registradas.",
    "- **Parecer de prontidão:** `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.\n- **Lacuna bloqueante:** validação editorial e normativa da candidata ainda não executada.",
    "roadmap readiness")
t = replace_once(t,
    "`PAS-001-AUDIT-001 1.0.0` concluiu a auditoria com parecer `Ready for consolidation`. O próximo trabalho deverá criar a **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0**, mantendo o arquivo vigente em `Draft 0.5.0` até decisão `Ready for publication`.",
    "`PAS-001-CANDIDATE-001 1.0.0-rc.1` materializa a edição consolidada e federada. O próximo trabalho deverá executar `PAS-001-RELEASE-VALIDATION-001`, mantendo o arquivo canônico em `Draft 0.5.0` até decisão formal `Ready for publication`.",
    "roadmap direction")
t = replace_once(t,
    "## Auditoria final concluída\n\nA auditoria avaliou 15 gates, inventariou 54 extensões e registrou quatro ações editoriais não bloqueantes.",
    "## Auditoria final concluída\n\nA auditoria avaliou 15 gates, inventariou 54 extensões e registrou quatro ações editoriais não bloqueantes.\n\n## Edição candidata concluída\n\n`PAS-001-CANDIDATE-001 1.0.0-rc.1` consolida o Journey de forma federada, sem substituir o `PAS-001 0.5.0`. A próxima etapa é a validação editorial e normativa da candidata.",
    "roadmap candidate section")
write(path, t)

# Knowledge Board
path = "docs/project/knowledge-board.md"
t = read(path)
t = replace_once(t, "version: 11.7.0", "version: 11.8.0", "board version")
t = replace_once(t,
    "| PAS-001-AUDIT-001 | Active 1.0.0 | Auditar os 15 gates e autorizar a consolidação editorial do PAS-001 |",
    "| PAS-001-AUDIT-001 | Active 1.0.0 | Auditar os 15 gates e autorizar a consolidação editorial do PAS-001 |\n| PAS-001-CANDIDATE-001 | Candidate 1.0.0-rc.1 | Consolidar a edição federada candidata do Guivos Journey |",
    "board candidate row")
t = replace_once(t,
    "| Parecer de prontidão | `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized` |\n| Lacuna bloqueante | Nenhuma para iniciar a consolidação; quatro ações editoriais não bloqueantes registradas |",
    "| Parecer de prontidão | `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized` |\n| Lacuna bloqueante | `PAS-001-RELEASE-VALIDATION-001` ainda não executado |",
    "board readiness")
t = replace_once(t,
    "| Frente ativa | Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0 |\n| Estado da frente ativa | Edição candidata autorizada; publicação ainda não autorizada |",
    "| Frente ativa | `PAS-001-RELEASE-VALIDATION-001` — Validação Editorial e Normativa da Edição Candidata |\n| Estado da frente ativa | Candidata `1.0.0-rc.1` criada; validação e publicação ainda não autorizadas |",
    "board active front")
t = replace_once(t,
    "| Foco imediato | Criar a edição candidata `PAS-001 1.0.0`, validar regressões e decidir `Ready for publication` |",
    "| Foco imediato | Validar a candidata contra os 15 gates, contratos finais, autoridade, supersessão, links, versões e navegação |",
    "board focus")
t = replace_once(t,
    "## Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, registrou supersessão e autoridade e autorizou a edição candidata. A publicação de `1.0.0` permanece condicionada.",
    "## Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, registrou supersessão e autoridade e autorizou a edição candidata.\n\n## Edição candidata do PAS-001\n\n`PAS-001-CANDIDATE-001 1.0.0-rc.1` está criada e pronta para validação. O `PAS-001 0.5.0` permanece canônico e a publicação de `1.0.0` continua condicionada.",
    "board candidate section")
write(path, t)

# Canonical Matrix
path = "docs/project/canonical-consolidation-matrix.md"
t = read(path)
t = replace_once(t, "version: 1.26.0", "version: 1.27.0", "matrix version")
t = replace_once(t,
    "## Reconciliação mais recente\n\nAs Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0` mantêm a Capacidade 09 como `In progress — 90%` e consolidam finalidade, Trajetória de Evolução, direção, baseline, estados, transições, visualização, estrutura comum, 19 famílias de eventos, contrato comum de integração, identidade, associação, autoridade, minimização, proveniência, temporalidades, evidências, interpretações, confiança, incerteza, causalidade, sincronização, prevenção de ciclos, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.\n\n## Próxima revisão\n\nConsolidar **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Capacidade 09 — Evolução Contínua**, incluindo critérios de conclusão, lacunas bloqueantes e não bloqueantes e critérios de reabertura.\n\n## Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` registra a matriz final de supersessão e o registro transversal de autoridade documental.\n\nCampos obrigatórios: seção original, conceito, documento substituto, decisão, ação editorial, necessidade de reabertura, documento pai, autoridade, dependências e critérios de reabertura.\n\nParecer: `Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized`.",
    "## Reconciliação mais recente\n\nTodas as nove capacidades estão funcionalmente concluídas. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, consolidou a matriz final de supersessão e o registro transversal de autoridade. `PAS-001-CANDIDATE-001 1.0.0-rc.1` aplica essas decisões em uma edição federada, preservando o `PAS-001 0.5.0` e as 54 extensões especializadas.\n\n## Edição candidata do PAS-001\n\n| Conceito | Decisão | Situação |\n|---|---|---|\n| PAS-001 0.5.0 | Manter | Permanece versão canônica até aprovação formal de publicação |\n| PAS-001-CANDIDATE-001 1.0.0-rc.1 | Manter como candidata | Consolida filosofia, camadas, princípios, invariantes, capacidades, perguntas, fronteiras e autoridade federada |\n| Contratos e extensões especializadas | Manter | Permanecem autoridade detalhada e não são duplicados integralmente |\n| Pergunta central do Contexto Vivo | Refinar | Remove a formulação totalizante e preserva representação revisável do contexto atual |\n| Pergunta central de Objetivos | Refinar | Substitui desejo de evoluir por direções conscientemente assumidas |\n| Estado de prontidão | Refinar | `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized` |\n\n## Próxima revisão\n\nExecutar `PAS-001-RELEASE-VALIDATION-001`, comparando a candidata com os 15 gates, contratos finais, matriz de supersessão, registro de autoridade, `GLPA-001`, `GIA-000`, links, versões e navegação.\n\n## Auditoria final do PAS-001\n\n`PAS-001-AUDIT-001 1.0.0` permanece como autoridade da consolidação. Campos obrigatórios: seção original, conceito, documento substituto, decisão, ação editorial, necessidade de reabertura, documento pai, autoridade, dependências e critérios de reabertura.\n\nParecer vigente: `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.",
    "matrix final block")
write(path, t)

# Changelog
path = "CHANGELOG.md"
t = read(path)
entry = """## 0.55.0 — PAS-001 Federated Candidate Edition

- Criação de `PAS-001-CANDIDATE-001 1.0.0-rc.1`.
- Consolidação federada da filosofia, propósito, arquitetura em camadas, princípios, invariantes, mapa das nove capacidades, perguntas centrais, fronteiras e autoridade documental.
- Aplicação dos refinamentos editoriais do Contexto Vivo e de Objetivos registrados pela auditoria.
- Preservação das 54 extensões normativas e dos nove contratos finais como autoridades especializadas.
- Manutenção do arquivo canônico `PAS-001` em `Draft 0.5.0`, sem alteração de conteúdo.
- Parecer `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.
- Arquitetura e Matriz `1.27.0`; Roadmap e Board `11.8.0`.
- Próximo ponto: `PAS-001-RELEASE-VALIDATION-001`.


"""
t = replace_once(t, "## 0.54.0 — PAS-001 Final Readiness Audit", entry + "## 0.54.0 — PAS-001 Final Readiness Audit", "changelog entry")
write(path, t)

# MkDocs navigation
path = "mkdocs.yml"
t = read(path)
t = replace_once(t,
    "      - PAS-001-AUDIT-001 — Auditoria Final de Prontidão: product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md",
    "      - PAS-001-AUDIT-001 — Auditoria Final de Prontidão: product-architecture/pas-001-guivos-journey-auditoria-final-prontidao.md\n      - PAS-001-CANDIDATE-001 — Edição Candidata Federada 1.0.0: product-architecture/pas-001-guivos-journey-1.0.0-candidate.md",
    "mkdocs candidate nav")
write(path, t)

# Final validation
checks = {
    "README.md": ["PAS-001-CANDIDATE-001 1.0.0-rc.1", "Candidate ready for validation"],
    "docs/index.md": ["PAS-001-CANDIDATE-001 1.0.0-rc.1", "PAS-001-RELEASE-VALIDATION-001"],
    "docs/product-architecture/index.md": ["version: 1.27.0", "### Edição candidata do PAS-001"],
    "docs/roadmap.md": ["version: 11.8.0", "PAS-001-CANDIDATE-001 1.0.0-rc.1"],
    "docs/project/knowledge-board.md": ["version: 11.8.0", "Candidate 1.0.0-rc.1"],
    "docs/project/canonical-consolidation-matrix.md": ["version: 1.27.0", "PAS-001-RELEASE-VALIDATION-001"],
    "CHANGELOG.md": ["## 0.55.0 — PAS-001 Federated Candidate Edition"],
    "mkdocs.yml": ["PAS-001-CANDIDATE-001 — Edição Candidata Federada 1.0.0"],
}
for file_path, needles in checks.items():
    content = read(file_path)
    for needle in needles:
        if needle not in content:
            raise RuntimeError(f"validation failed: {needle!r} missing from {file_path}")

candidate = read("docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md")
for needle in ["id: PAS-001-CANDIDATE-001", "version: 1.0.0-rc.1", "# 35. Próximo ponto exato"]:
    if needle not in candidate:
        raise RuntimeError(f"candidate validation failed: {needle}")

print("PAS-001 candidate synchronization completed successfully")
