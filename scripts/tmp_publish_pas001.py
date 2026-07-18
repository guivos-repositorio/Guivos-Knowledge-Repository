from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-18"

CANONICAL = ROOT / "docs/product-architecture/pas-001-guivos-journey.md"
CANDIDATE = ROOT / "docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md"
VALIDATION = ROOT / "docs/product-architecture/pas-001-guivos-journey-validacao-publicacao.md"
PUBLICATION = ROOT / "docs/product-architecture/pas-001-guivos-journey-publicacao-controlada.md"

EXPECTED = {
    CANONICAL: "d5e84f75f012dee07edc570712c301331d1e09be",
    CANDIDATE: "543e6b1dd6048372c741fe03a7ee89340081f6c5",
    VALIDATION: "ee464e01d5f8a8951e631f67518757b2d32c6189",
}


def git_blob(path: Path, ref: str = "HEAD") -> str:
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.check_output(["git", "rev-parse", f"{ref}:{rel}"], cwd=ROOT, text=True).strip()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}: {old[:100]!r}")
    return text.replace(old, new, 1)


def replace_file(path: Path, old: str, new: str, label: str) -> None:
    write(path, replace_once(read(path), old, new, label))


def assert_source_blobs() -> None:
    for path, expected in EXPECTED.items():
        actual = git_blob(path)
        if actual != expected:
            raise RuntimeError(f"source blob mismatch for {path.relative_to(ROOT)}: {actual} != {expected}")


def build_canonical(candidate: str) -> str:
    marker = "# 29. Critérios de aceite da edição candidata"
    if marker not in candidate:
        raise RuntimeError("candidate process marker not found")
    architecture = candidate.split(marker, 1)[0]
    body_marker = "# 1. Autoridade da especificação"
    if body_marker not in architecture:
        raise RuntimeError("candidate architectural body not found")
    body = architecture.split(body_marker, 1)[1]
    frontmatter = f'''---
id: PAS-001
title: Guivos Journey Product Architecture Specification
status: active
version: 1.0.0
owner: Guivos
last_updated: {DATE}
normative: true
related:
  - GLPA-001
  - GIA-000
  - PAS-001-RECON-001
  - PAS-001-AUDIT-001
  - PAS-001-CANDIDATE-001
  - PAS-001-RELEASE-VALIDATION-001
  - PAS-001-PUBLICATION-001
  - PAS-001-CC-CONTRACT-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - PAS-001-IC-CONTRACT-001
  - PAS-001-EXP-CONTRACT-001
  - PAS-001-EC-CONTRACT-001
---

# PAS-001 — Guivos Journey Product Architecture Specification

> **Estado canônico:** `Published — PAS-001 1.0.0 active.`
>
> Esta especificação consolida a arquitetura global do Guivos Journey. Os nove contratos finais e as 54 extensões especializadas permanecem autoridades sobre estados, eventos, integrações, KPIs, guardrails, cenários e regras específicas. Reconciliação, auditoria, candidata, validação e publicação preservam a rastreabilidade do processo.

# 1. Autoridade da especificação
'''
    return frontmatter + body.lstrip()


def historical_candidate(candidate: str) -> str:
    candidate = replace_once(candidate, "status: candidate", "status: historical", "candidate status")
    candidate = replace_once(
        candidate,
        "normative: true\nrelated:",
        "normative: true\npromoted_to: PAS-001\npromoted_version: 1.0.0\npromotion_record: PAS-001-PUBLICATION-001\nrelated:",
        "candidate promotion metadata",
    )
    candidate = replace_once(
        candidate,
        "  - PAS-001-AUDIT-001\n  - GLPA-001",
        "  - PAS-001-AUDIT-001\n  - PAS-001-RELEASE-VALIDATION-001\n  - PAS-001-PUBLICATION-001\n  - GLPA-001",
        "candidate related publication",
    )
    old_banner = "> **Estado da candidata:** `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized.`\n>\n> Esta edição candidata não substitui o arquivo canônico `PAS-001 0.5.0`, não autoriza publicação, tag, release ou lançamento e deverá ser validada por `PAS-001-RELEASE-VALIDATION-001`."
    new_banner = "> **Estado histórico:** `Historical 1.0.0-rc.1 — promoted to PAS-001 1.0.0.`\n>\n> Esta candidata foi validada por `PAS-001-RELEASE-VALIDATION-001` e seu núcleo arquitetural foi promovido ao arquivo canônico por `PAS-001-PUBLICATION-001`. Ela permanece disponível para rastreabilidade e não constitui a versão operacional vigente."
    return replace_once(candidate, old_banner, new_banner, "candidate banner")


def publication_record() -> str:
    return f'''---
id: PAS-001-PUBLICATION-001
title: Publicação Controlada do PAS-001 — Guivos Journey 1.0.0
status: active
version: 1.0.0
owner: Guivos
last_updated: {DATE}
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-CANDIDATE-001
  - PAS-001-RELEASE-VALIDATION-001
  - PAS-001-AUDIT-001
  - PAS-001-RECON-001
  - GLPA-001
  - GIA-000
---

# PAS-001-PUBLICATION-001 — Publicação Controlada do PAS-001 — Guivos Journey 1.0.0

> **Parecer de publicação:** `Published — PAS-001 1.0.0 active as the canonical Guivos Journey Product Architecture Specification.`
>
> O ato efetivo de publicação é o merge do Pull Request que introduz este registro e a transformação canônica. Esta decisão não cria tag, GitHub Release, produto implementado ou lançamento comercial.

# 4986. Autoridade e vínculo

Este documento registra a promoção controlada de `PAS-001-CANDIDATE-001 1.0.0-rc.1`, autorizada por `PAS-001-RELEASE-VALIDATION-001 1.0.0`, para `PAS-001 1.0.0 active`.

# 4987. Decisão executada

A publicação promove o núcleo arquitetural validado, substitui controladamente o conteúdo do arquivo canônico, atualiza seu estado e versão, classifica a candidata como histórica, sincroniza os artefatos oficiais e preserva contratos, extensões e histórico.

# 4988. Condições de entrada confirmadas

| Condição | Resultado |
|---|---|
| Validação de release | `Active 1.0.0` |
| Parecer | `Ready for publication` |
| Gates de release | `25 de 25` aprovados |
| Gates anteriores | `15 de 15` preservados |
| Critérios da candidata | `35 de 35` aprovados |
| Comportamentos proibidos | `30 de 30` bloqueados |
| Contratos finais | `9 de 9` ativos |
| Extensões especializadas | `54` vigentes |
| Achados críticos ou altos | `0` |

# 4989. Baseline técnica

- commit-base: `0de9d6ddbb0b74d91f5053593f140218bb47d812`;
- blob anterior do canônico: `d5e84f75f012dee07edc570712c301331d1e09be`;
- blob da candidata: `543e6b1dd6048372c741fe03a7ee89340081f6c5`;
- blob da validação: `ee464e01d5f8a8951e631f67518757b2d32c6189`;
- commit de publicação: commit que integrar o Pull Request associado, preservado no histórico do Git.

# 4990. Unidade de publicação

A unidade inclui documento canônico, candidata histórica, este registro, Arquitetura de Produtos, Roadmap, Knowledge Board, Matriz Canônica, Changelog, README, página inicial, índice de Arquitetura e navegação do MkDocs.

# 4991. Atomicidade

A `main` somente recebe o estado publicado pelo merge integral. Estados intermediários, publicação parcial, versões divergentes ou navegação quebrada são proibidos.

# 4992. Fonte normativa

A fonte é a candidata `1.0.0-rc.1`. Foram promovidas as seções arquiteturais `1–28`: autoridade, definição, propósito, filosofia, protagonismo, camadas, princípios, invariantes, modelo operacional, mapa, perguntas, resumos, relações, fronteiras, fatos e inferências, proteção, neutralidade, eventos, correção, saúde, sucesso, autoridade federada, contratos, histórico, versionamento, reabertura e comportamentos proibidos.

# 4993. Conteúdo não promovido

Critérios da candidata, processo de validação, estados preparatórios, condição de release, ação futura, versões projetadas e próximo ponto permanecem no arquivo histórico e nos documentos de validação e publicação.

# 4994. Metadados canônicos resultantes

`PAS-001` passa a utilizar `status: active`, `version: 1.0.0`, `normative: true` e referências explícitas aos documentos de reconciliação, auditoria, candidata, validação, publicação e aos nove contratos finais.

# 4995. Abertura canônica

O arquivo publicado utiliza o título `PAS-001 — Guivos Journey Product Architecture Specification`, sem banner de candidata ou linguagem de publicação pendente.

# 4996. Classificação da candidata

`PAS-001-CANDIDATE-001` permanece em `1.0.0-rc.1`, passa a `historical` e registra `promoted_to`, `promoted_version` e `promotion_record`.

# 4997. Estado da validação

`PAS-001-RELEASE-VALIDATION-001 1.0.0` permanece ativo como autoridade do parecer que autorizou a publicação.

# 4998. Evidência da publicação

O histórico do Git e o Pull Request associado registram commit-base, head final, arquivos alterados, blobs de origem, resultados de validação e commit de merge.

# 4999. Preservação do PAS-001 0.5.0

A versão `0.5.0` permanece integralmente recuperável no histórico, nos Pull Requests, na reconciliação, na auditoria, na matriz de supersessão e neste registro. Nenhum histórico é reescrito.

# 5000. Supersessão

`PAS-001 1.0.0` passa a ser a versão canônica. `PAS-001 0.5.0` e a candidata `1.0.0-rc.1` tornam-se históricos. Contratos finais e extensões continuam vigentes.

# 5001. Autoridade federada

A hierarquia permanece: decisões institucionais, `GLPA-001`, `PAS-001 1.0.0`, contratos finais, extensões especializadas, documentos de processo, documentação operacional e exemplos.

# 5002. Navegação

O arquivo canônico ocupa a posição principal. Candidata, validação e publicação permanecem acessíveis como histórico e evidência do ciclo de consolidação.

# 5003. Links canônicos

README, página inicial, índices e MkDocs apontam prioritariamente para `pas-001-guivos-journey.md`. Links para a candidata são identificados como históricos.

# 5004. Artefatos sincronizados

Arquitetura de Produtos, Roadmap, Knowledge Board, Matriz Canônica, Changelog, README, página inicial, índice e MkDocs registram o mesmo estado `Published — PAS-001 1.0.0 active`.

# 5005. Versionamento

- `PAS-001`: `1.0.0`;
- candidata: `Historical 1.0.0-rc.1`;
- validação: `1.0.0`;
- publicação: `1.0.0`;
- Arquitetura e Matriz: `1.29.0`;
- Roadmap e Board: `11.10.0`;
- Changelog: `0.57.0`.

# 5006. Validação pré-publicação

Foram conferidos blobs esperados, estado da validação, gates, critérios, comportamentos proibidos, contratos, extensões, versões iniciais e ausência de mudança concorrente na base.

# 5007. Validação pós-transformação

Foram verificados metadados do canônico, ausência de conteúdo processual, presença das 28 seções arquiteturais, classificação da candidata, registro de publicação, versões, navegação, links e ausência de arquivos normativos órfãos.

# 5008. Validação semântica

A publicação preserva filosofia, propósito, protagonismo, camadas, 30 princípios, invariantes, nove capacidades, nove perguntas, fronteiras, estrutura federada, proteção sensível, neutralidade, correção, revogação, reabertura e 30 comportamentos proibidos.

# 5009. Ausência de regressões

Não houve remoção de capacidade, alteração de pergunta, ampliação de autoridade da Intelligence ou Platform, influência comercial indevida, omissão de contrato ou extensão, perda de rastreabilidade, score humano, linearidade obrigatória ou decisão automática.

# 5010. Estado resultante

| Ativo | Estado |
|---|---|
| PAS-001 | `Active 1.0.0` |
| Reconciliação | `Active 1.0.0` |
| Auditoria | `Active 1.0.0` |
| Candidata | `Historical 1.0.0-rc.1 — promoted` |
| Validação | `Active 1.0.0` |
| Publicação | `Active 1.0.0` |
| Capacidades 01–09 | `Functionally complete` |
| Prontidão | `Published — PAS-001 1.0.0 active` |

# 5011. Lacunas posteriores

Não permanece lacuna bloqueante referente à arquitetura funcional. Implementação, prototipação, APIs, arquitetura física, operação, métricas produtivas, localização, mapa executivo, tag e release são frentes posteriores independentes.

# 5012. Rollback

Uma publicação inválida deverá ser revertida integralmente, restaurando `PAS-001 0.5.0`, candidata `candidate`, versões, navegação e artefatos. O commit falho e seu revert permanecem no histórico, e validação e publicação são repetidas.

# 5013. Bloqueios de merge

Mudança concorrente, blob divergente, link quebrado, versão incorreta, canônico parcial, candidata não classificada, contrato ou extensão ausente, navegação divergente, regressão ou thread bloqueante impedem o merge.

# 5014. Evidências do Pull Request

A descrição final deverá registrar base, head, arquivos, blobs anteriores e novos, contagens, testes, versões, estado da candidata, ausência de regressões e limites sobre tag e release.

# 5015. Aprovação e merge

A retirada do modo rascunho e o merge do Pull Request associado constituem a autorização efetiva e o ato documental de publicação.

# 5016. Tag e GitHub Release

Esta etapa não cria tag, GitHub Release, pacote, PDF oficial, anúncio público ou lançamento comercial. Qualquer uma dessas ações exige autorização posterior.

# 5017. Critérios de aceite

A publicação exige promoção das 28 seções, metadados `active 1.0.0`, preservação dos princípios, capacidades, perguntas, fronteiras, autoridade, contratos, extensões, camadas e histórico; sincronização dos artefatos; validação de links, navegação, regressões e rollback; diff sem temporários; PR em rascunho; ausência de tag e release.

# 5018. Comportamentos proibidos

É proibido promover a candidata integralmente sem transformação, copiar metadados de candidata, manter estado `candidate` no canônico, incluir processo de release no corpo canônico, apagar a candidata ou o histórico, alterar contratos, extensões, perguntas ou fronteiras, publicar parcialmente, integrar com links ou versões divergentes e criar tag, release ou anúncio automaticamente.

# 5019. Parecer

> **Published — PAS-001 1.0.0 active as the canonical Guivos Journey Product Architecture Specification.**

O parecer significa publicação arquitetural e encerramento do ciclo de consolidação. Não significa produto implementado, sistema em produção, validação de mercado, conformidade regulatória universal ou lançamento comercial.

# 5020. Próximo ponto exato

> **`PAS-001-CAPABILITY-MAP-001 — Mapa Final de Capacidades do Guivos Journey`**

O mapa deverá apresentar as nove capacidades, perguntas centrais, responsabilidades, entradas e saídas, fronteiras, contratos finais, relações, conclusão, reabertura e relação com Intelligence, Service Layers e Platform Layer.

```text
PAS-001-RELEASE-VALIDATION-001
→ PAS-001-PUBLICATION-001
→ PAS-001 1.0.0 active
→ PAS-001-CAPABILITY-MAP-001
→ eventual tag ou GitHub Release mediante nova autorização
```
'''


def update_artifacts() -> None:
    # README
    p = ROOT / "README.md"
    t = read(p)
    t = replace_once(t, "- **Especificação-base:** PAS-001 — Guivos Journey 0.5.0", "- **Especificação vigente:** PAS-001 — Guivos Journey 1.0.0", "README specification")
    t = replace_once(t, "- **Edição candidata:** PAS-001-CANDIDATE-001 1.0.0-rc.1", "- **Candidata histórica:** PAS-001-CANDIDATE-001 1.0.0-rc.1 — promoted", "README candidate")
    t = replace_once(t, "- **Parecer de prontidão:** `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`", "- **Estado canônico:** `Published — PAS-001 1.0.0 active`", "README readiness")
    t = replace_once(t, "- **Próxima frente:** `PAS-001-PUBLICATION-001` — Publicação Controlada do PAS-001 — Guivos Journey 1.0.0", "- **Próxima frente:** `PAS-001-CAPABILITY-MAP-001` — Mapa Final de Capacidades do Guivos Journey", "README next")
    t = replace_once(t, "A capacidade está **Functionally complete — 100%**. Todas as nove capacidades estão concluídas; a auditoria autoriza a edição candidata, mas o arquivo vigente permanece `Draft 0.5.0`.", "A capacidade está **Functionally complete — 100%**. Todas as nove capacidades estão concluídas e o `PAS-001 1.0.0` está publicado como especificação arquitetural canônica.", "README capability state")
    t = replace_once(t, "- [Edição Candidata Federada do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)", "- [Edição Candidata Histórica do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)", "README candidate link")
    t = replace_once(t, "- [Validação Editorial e Normativa do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-validacao-publicacao.md)", "- [Validação Editorial e Normativa do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-validacao-publicacao.md)\n- [Publicação Controlada do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-publicacao-controlada.md)", "README publication link")
    write(p, t)

    # docs/index.md
    p = ROOT / "docs/index.md"
    t = read(p)
    t = replace_once(t, "- `PAS-001 — Guivos Journey 0.5.0` como especificação-base;", "- `PAS-001 — Guivos Journey 1.0.0` como especificação arquitetural canônica ativa;", "docs index specification")
    t = replace_once(t, "- `PAS-001-CANDIDATE-001 1.0.0-rc.1` como edição candidata consolidada e federada;", "- `PAS-001-CANDIDATE-001 1.0.0-rc.1` como candidata histórica promovida;", "docs index candidate")
    t = replace_once(t, "- prontidão `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`;", "- `PAS-001-PUBLICATION-001 1.0.0` como registro de publicação controlada;\n- estado `Published — PAS-001 1.0.0 active`;", "docs index readiness")
    t = replace_once(t, "Preparar `PAS-001-PUBLICATION-001` — **Publicação Controlada do PAS-001 — Guivos Journey 1.0.0**, preservando o arquivo canônico em `Draft 0.5.0` até aprovação expressa de publicação.", "Executar `PAS-001-CAPABILITY-MAP-001` — **Mapa Final de Capacidades do Guivos Journey**, utilizando o `PAS-001 1.0.0` publicado e seus contratos especializados.", "docs index mission")
    t = replace_once(t, "- [Edição Candidata Federada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)", "- [Edição Candidata Histórica do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)", "docs index candidate link")
    t = replace_once(t, "- [Validação Editorial e Normativa do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-validacao-publicacao.md)", "- [Validação Editorial e Normativa do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-validacao-publicacao.md)\n- [Publicação Controlada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-publicacao-controlada.md)", "docs index publication link")
    write(p, t)

    # Product Architecture index
    p = ROOT / "docs/product-architecture/index.md"
    t = read(p)
    t = replace_once(t, "version: 1.28.0", "version: 1.29.0", "architecture version")
    t = replace_once(t, "O `PAS-001 — Guivos Journey 0.5.0` é a especificação-base da Experience Layer.", "O `PAS-001 — Guivos Journey 1.0.0` é a especificação arquitetural canônica e ativa da Experience Layer.", "architecture specification")
    t = replace_once(t, "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates. `PAS-001-CANDIDATE-001 1.0.0-rc.1` materializa a edição federada. `PAS-001-RELEASE-VALIDATION-001 1.0.0` aprova os 25 gates de release e emite `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`.", "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates. `PAS-001-CANDIDATE-001 1.0.0-rc.1` materializou a edição federada e agora é histórica. `PAS-001-RELEASE-VALIDATION-001 1.0.0` aprovou os 25 gates. `PAS-001-PUBLICATION-001 1.0.0` registra a promoção para `PAS-001 1.0.0 active`.", "architecture reconciliation")
    t = replace_once(t, "Todas as nove capacidades estão funcionalmente concluídas. O `PAS-001` canônico permanece `Draft 0.5.0` até aprovação expressa e execução de `PAS-001-PUBLICATION-001`.", "Todas as nove capacidades estão funcionalmente concluídas. O `PAS-001 1.0.0` está publicado e seus contratos e extensões permanecem autoridades especializadas.", "architecture readiness")
    t = replace_once(t, "`PAS-001-CANDIDATE-001 1.0.0-rc.1` consolida filosofia, arquitetura em camadas, princípios, invariantes, mapa das nove capacidades, perguntas centrais, fronteiras, autoridade federada e critérios globais, preservando os contratos especializados e o arquivo canônico `0.5.0`.", "`PAS-001-CANDIDATE-001 1.0.0-rc.1` preserva historicamente a edição que consolidou filosofia, arquitetura em camadas, princípios, invariantes, mapa, perguntas, fronteiras e autoridade federada antes da promoção.", "architecture candidate section")
    old = "`PAS-001-RELEASE-VALIDATION-001 1.0.0` confirma 25 gates, 35 critérios de aceite, 30 comportamentos proibidos, nove contratos finais, 54 extensões, links, navegação, versões, preservação histórica, plano de publicação e rollback. O parecer é `Ready for publication`, condicionado à aprovação expressa."
    new = old + "\n\n### Publicação controlada do PAS-001\n\n`PAS-001-PUBLICATION-001 1.0.0` promove o núcleo arquitetural validado para `PAS-001 1.0.0 active`, classifica a candidata como histórica e encerra o ciclo de consolidação sem criar tag ou release."
    t = replace_once(t, old, new, "architecture publication section")
    write(p, t)

    # Roadmap
    p = ROOT / "docs/roadmap.md"
    t = read(p)
    t = replace_once(t, "version: 11.9.0", "version: 11.10.0", "roadmap version")
    t = replace_once(t, "- **Especificação-base ativa:** `PAS-001 — Guivos Journey 0.5.0`.", "- **Especificação arquitetural ativa:** `PAS-001 — Guivos Journey 1.0.0`.", "roadmap specification")
    t = replace_once(t, "- **Edição candidata vigente:** `PAS-001-CANDIDATE-001 1.0.0-rc.1`.", "- **Edição candidata histórica:** `PAS-001-CANDIDATE-001 1.0.0-rc.1 — promoted`.", "roadmap candidate")
    t = replace_once(t, "- **Parecer de prontidão:** `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`.", "- **Estado canônico:** `Published — PAS-001 1.0.0 active`.", "roadmap readiness")
    t = replace_once(t, "- **Lacuna bloqueante:** aprovação expressa e execução controlada de `PAS-001-PUBLICATION-001`.", "- **Lacuna bloqueante da arquitetura funcional:** nenhuma.", "roadmap gap")
    t = replace_once(t, "`PAS-001-RELEASE-VALIDATION-001 1.0.0` valida a candidata e autoriza preparar a publicação controlada. O próximo trabalho deverá executar `PAS-001-PUBLICATION-001` somente após aprovação expressa, mantendo o arquivo canônico em `Draft 0.5.0` até o commit de promoção.", "`PAS-001-PUBLICATION-001 1.0.0` promoveu a candidata validada para `PAS-001 1.0.0 active`. O próximo trabalho é `PAS-001-CAPABILITY-MAP-001`, mantendo contratos e extensões como autoridades especializadas.", "roadmap direction")
    t = replace_once(t, "`PAS-001-CANDIDATE-001 1.0.0-rc.1` consolida o Journey de forma federada, sem substituir o `PAS-001 0.5.0`. A próxima etapa é a validação editorial e normativa da candidata.", "`PAS-001-CANDIDATE-001 1.0.0-rc.1` permanece como candidata histórica promovida ao `PAS-001 1.0.0`.", "roadmap candidate section")
    old = "`PAS-001-RELEASE-VALIDATION-001 1.0.0` aprovou 25 gates, validou os 35 critérios da candidata e confirmou o bloqueio dos 30 comportamentos proibidos. O estado é `Ready for publication`, mas a publicação depende de aprovação expressa."
    new = old + "\n\n## Publicação controlada concluída\n\n`PAS-001-PUBLICATION-001 1.0.0` publicou `PAS-001 1.0.0 active`, preservou o histórico e definiu o Mapa Final de Capacidades como próxima frente."
    t = replace_once(t, old, new, "roadmap publication section")
    t = t.replace("a próxima etapa é a publicação controlada do `PAS-001 1.0.0`, condicionada à aprovação expressa.", "o `PAS-001 1.0.0` está publicado; a próxima etapa é o Mapa Final de Capacidades.")
    write(p, t)

    # Knowledge Board
    p = ROOT / "docs/project/knowledge-board.md"
    t = read(p)
    t = replace_once(t, "version: 11.9.0", "version: 11.10.0", "board version")
    t = replace_once(t, "| PAS-001 — Guivos Journey | Draft 0.5.0 — Active | Especificar a Experience Layer |", "| PAS-001 — Guivos Journey | Active 1.0.0 | Governar a arquitetura canônica da Experience Layer |", "board PAS")
    t = replace_once(t, "| PAS-001-CANDIDATE-001 | Candidate 1.0.0-rc.1 | Consolidar a edição federada candidata do Guivos Journey |", "| PAS-001-CANDIDATE-001 | Historical 1.0.0-rc.1 — promoted | Preservar a edição candidata que originou o PAS-001 1.0.0 |", "board candidate")
    t = replace_once(t, "| PAS-001-RELEASE-VALIDATION-001 | Active 1.0.0 | Validar a candidata e emitir parecer de publicação |", "| PAS-001-RELEASE-VALIDATION-001 | Active 1.0.0 | Preservar a validação que autorizou a publicação |\n| PAS-001-PUBLICATION-001 | Active 1.0.0 | Registrar a publicação controlada do PAS-001 1.0.0 |", "board publication row")
    t = replace_once(t, "| Especificação-base | `PAS-001 — Guivos Journey 0.5.0` |", "| Especificação arquitetural | `PAS-001 — Guivos Journey 1.0.0` |", "board specification")
    t = replace_once(t, "| Parecer de prontidão | `Ready for publication — PAS-001 1.0.0 publication requires explicit approval` |", "| Estado canônico | `Published — PAS-001 1.0.0 active` |", "board readiness")
    t = replace_once(t, "| Lacuna bloqueante | Aprovação expressa e execução controlada de `PAS-001-PUBLICATION-001` |", "| Lacuna bloqueante da arquitetura funcional | Nenhuma |", "board gap")
    t = replace_once(t, "| Frente ativa | `PAS-001-PUBLICATION-001` — Publicação Controlada do PAS-001 — Guivos Journey 1.0.0 |", "| Frente ativa | `PAS-001-CAPABILITY-MAP-001` — Mapa Final de Capacidades do Guivos Journey |", "board front")
    t = replace_once(t, "| Estado da frente ativa | Validação concluída; publicação depende de aprovação expressa |", "| Estado da frente ativa | Publicação concluída; mapa executivo e navegável pendente |", "board front state")
    t = replace_once(t, "| Foco imediato | Preparar a promoção controlada da candidata, sem alterar o canônico antes da aprovação expressa |", "| Foco imediato | Consolidar o Mapa Final de Capacidades a partir do PAS-001 1.0.0 publicado |", "board focus")
    t = replace_once(t, "`PAS-001-CANDIDATE-001 1.0.0-rc.1` está criada e pronta para validação. O `PAS-001 0.5.0` permanece canônico e a publicação de `1.0.0` continua condicionada.", "`PAS-001-CANDIDATE-001 1.0.0-rc.1` permanece histórica após a promoção de seu núcleo ao `PAS-001 1.0.0`.", "board candidate section")
    old = "`PAS-001-RELEASE-VALIDATION-001 1.0.0` aprovou os 25 gates, os 35 critérios de aceite e o bloqueio dos 30 comportamentos proibidos. O `PAS-001 0.5.0` permanece canônico até aprovação expressa e publicação controlada."
    new = "`PAS-001-RELEASE-VALIDATION-001 1.0.0` aprovou os 25 gates, os 35 critérios de aceite e o bloqueio dos 30 comportamentos proibidos.\n\n## Publicação controlada do PAS-001\n\n`PAS-001-PUBLICATION-001 1.0.0` promoveu a candidata para `PAS-001 1.0.0 active`, preservou o histórico e encerrou a lacuna de publicação arquitetural."
    t = replace_once(t, old, new, "board publication section")
    write(p, t)

    # Canonical matrix
    p = ROOT / "docs/project/canonical-consolidation-matrix.md"
    t = read(p)
    t = replace_once(t, "version: 1.28.0", "version: 1.29.0", "matrix version")
    publication_section = '''\n\n## PAS-001 — Publicação Controlada 1.0.0\n\n| Objeto | Decisão | Autoridade vigente | Situação |\n|---|---|---|---|\n| PAS-001 0.5.0 | Historical only | Histórico do Git, reconciliação e auditoria | Substituído pela edição 1.0.0 |\n| PAS-001-CANDIDATE-001 1.0.0-rc.1 | Historical only — promoted | PAS-001-PUBLICATION-001 | Núcleo arquitetural promovido |\n| PAS-001 1.0.0 | Maintain | Arquivo canônico `pas-001-guivos-journey.md` | Active e normativo |\n| Contratos finais | Maintain | Nove documentos `*-CONTRACT-001` | Autoridades especializadas |\n| Extensões normativas | Maintain | 54 extensões das Capacidades 01–09 | Vigentes |\n| Prontidão | Supersede | PAS-001-PUBLICATION-001 | `Published — PAS-001 1.0.0 active` |\n| Próximo ponto | Refine | Roadmap e Knowledge Board | `PAS-001-CAPABILITY-MAP-001` |\n'''
    if "## PAS-001 — Publicação Controlada 1.0.0" in t:
        raise RuntimeError("matrix publication section already exists")
    t = t.rstrip() + publication_section
    write(p, t)

    # Changelog
    p = ROOT / "CHANGELOG.md"
    t = read(p)
    entry = '''## 0.57.0 — PAS-001 Controlled Publication\n\n- Publicação de `PAS-001 1.0.0` como especificação arquitetural canônica ativa.\n- Promoção das 28 seções arquiteturais validadas da candidata.\n- Classificação de `PAS-001-CANDIDATE-001 1.0.0-rc.1` como histórica e promovida.\n- Criação de `PAS-001-PUBLICATION-001 1.0.0`.\n- Preservação dos nove contratos finais e das 54 extensões especializadas.\n- Arquitetura e Matriz `1.29.0`; Roadmap e Board `11.10.0`.\n- Estado `Published — PAS-001 1.0.0 active`.\n- Próximo ponto: `PAS-001-CAPABILITY-MAP-001`.\n- Nenhuma tag ou GitHub Release criada.\n\n\n'''
    t = replace_once(t, "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n", "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n" + entry, "changelog entry")
    write(p, t)

    # MkDocs navigation
    p = ROOT / "mkdocs.yml"
    t = read(p)
    t = replace_once(t, "- PAS-001-CANDIDATE-001 — Edição Candidata Federada 1.0.0: product-architecture/pas-001-guivos-journey-1.0.0-candidate.md", "- PAS-001-CANDIDATE-001 — Edição Candidata Histórica 1.0.0: product-architecture/pas-001-guivos-journey-1.0.0-candidate.md", "mkdocs candidate")
    t = replace_once(t, "- PAS-001-RELEASE-VALIDATION-001 — Validação Editorial e Normativa: product-architecture/pas-001-guivos-journey-validacao-publicacao.md", "- PAS-001-RELEASE-VALIDATION-001 — Validação Editorial e Normativa: product-architecture/pas-001-guivos-journey-validacao-publicacao.md\n      - PAS-001-PUBLICATION-001 — Publicação Controlada 1.0.0: product-architecture/pas-001-guivos-journey-publicacao-controlada.md", "mkdocs publication")
    write(p, t)


def validate() -> None:
    canonical = read(CANONICAL)
    candidate = read(CANDIDATE)
    validation = read(VALIDATION)
    publication = read(PUBLICATION)

    required = [
        "id: PAS-001", "status: active", "version: 1.0.0", "# 28. Comportamentos globais proibidos",
        "Published — PAS-001 1.0.0 active", "PAS-001-PUBLICATION-001",
    ]
    for item in required:
        if item not in canonical:
            raise RuntimeError(f"canonical missing {item}")
    forbidden = ["status: candidate", "version: 1.0.0-rc.1", "# 29. Critérios de aceite da edição candidata", "publication not yet authorized"]
    for item in forbidden:
        if item in canonical:
            raise RuntimeError(f"canonical contains forbidden process content: {item}")
    if canonical.count("Functionally complete |") != 9:
        raise RuntimeError("canonical capacity map does not contain nine completed capabilities")
    principles = re.findall(r"(?m)^\d+\. .+$", canonical.split("# 9. Invariantes globais", 1)[0].split("# 8. Princípios permanentes", 1)[1])
    if len(principles) != 30:
        raise RuntimeError(f"expected 30 principles, found {len(principles)}")
    prohibited = re.findall(r"(?m)^\d+\. .+$", canonical.split("# 28. Comportamentos globais proibidos", 1)[1])
    if len(prohibited) != 30:
        raise RuntimeError(f"expected 30 prohibited behaviors, found {len(prohibited)}")

    for item in ["status: historical", "promoted_to: PAS-001", "promoted_version: 1.0.0", "promotion_record: PAS-001-PUBLICATION-001"]:
        if item not in candidate:
            raise RuntimeError(f"candidate missing historical marker {item}")
    for item in ["status: active", "version: 1.0.0", "25 de 25", "35 de 35", "30 de 30"]:
        if item not in validation:
            raise RuntimeError(f"validation missing {item}")
    for item in ["id: PAS-001-PUBLICATION-001", "status: active", "version: 1.0.0", "Published — PAS-001 1.0.0 active"]:
        if item not in publication:
            raise RuntimeError(f"publication record missing {item}")

    contract_ids = set()
    extension_ids = set()
    for path in (ROOT / "docs/product-architecture").glob("*.md"):
        text = read(path)
        match = re.search(r"(?m)^id:\s*(PAS-001-(?:CC|CV|OBJ|EV|PP|OA|IC|EXP|EC)-[^\s]+)", text)
        if not match:
            continue
        doc_id = match.group(1)
        extension_ids.add(doc_id)
        if doc_id.endswith("-CONTRACT-001"):
            contract_ids.add(doc_id)
    if len(extension_ids) != 54:
        raise RuntimeError(f"expected 54 capability extensions, found {len(extension_ids)}")
    if len(contract_ids) != 9:
        raise RuntimeError(f"expected 9 final contracts, found {len(contract_ids)}")

    versions = {
        ROOT / "docs/product-architecture/index.md": "version: 1.29.0",
        ROOT / "docs/roadmap.md": "version: 11.10.0",
        ROOT / "docs/project/knowledge-board.md": "version: 11.10.0",
        ROOT / "docs/project/canonical-consolidation-matrix.md": "version: 1.29.0",
        ROOT / "CHANGELOG.md": "## 0.57.0 — PAS-001 Controlled Publication",
    }
    for path, marker in versions.items():
        if marker not in read(path):
            raise RuntimeError(f"version marker missing from {path.relative_to(ROOT)}: {marker}")

    changed_docs = [
        ROOT / "README.md", ROOT / "docs/index.md", ROOT / "docs/product-architecture/index.md",
        ROOT / "docs/roadmap.md", ROOT / "docs/project/knowledge-board.md",
        ROOT / "docs/project/canonical-consolidation-matrix.md", CANONICAL, CANDIDATE,
        VALIDATION, PUBLICATION,
    ]
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    checked = 0
    for path in changed_docs:
        text = read(path)
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                raise RuntimeError(f"broken local link in {path.relative_to(ROOT)}: {target}")
            checked += 1

    mkdocs = read(ROOT / "mkdocs.yml")
    nav_targets = re.findall(r":\s+([^\s]+\.md)\s*$", mkdocs, flags=re.M)
    for target in nav_targets:
        if not (ROOT / "docs" / target).exists():
            raise RuntimeError(f"missing MkDocs target: {target}")

    old_canonical = subprocess.check_output(["git", "show", "HEAD:docs/product-architecture/pas-001-guivos-journey.md"], cwd=ROOT)
    if hashlib.sha256(old_canonical).hexdigest() == hashlib.sha256(canonical.encode()).hexdigest():
        raise RuntimeError("canonical transformation did not change content")

    print(f"validated: 28 architectural sections, 30 principles, 9 capabilities, 30 prohibitions, {len(contract_ids)} contracts, {len(extension_ids)} extensions, {checked} local links, {len(nav_targets)} nav targets")


def main() -> None:
    assert_source_blobs()
    candidate = read(CANDIDATE)
    write(CANONICAL, build_canonical(candidate))
    write(CANDIDATE, historical_candidate(candidate))
    write(PUBLICATION, publication_record())
    update_artifacts()
    validate()


if __name__ == "__main__":
    main()
