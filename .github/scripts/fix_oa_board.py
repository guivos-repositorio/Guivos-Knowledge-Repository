from __future__ import annotations

import os
import subprocess
from pathlib import Path


def run(*args: str) -> None:
    subprocess.run(args, check=True)


path = Path("docs/project/knowledge-board.md")
text = path.read_text(encoding="utf-8")

malformed = """| PAS-001-OA-EVENT-001 | Active 1.0.0 |
| PAS-001-OA-INTEGRATION-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais das Oportunidades Ativas |
| PAS-001-OA-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Oportunidades Ativas |"""
corrected = """| PAS-001-OA-EVENT-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais das Oportunidades Ativas |
| PAS-001-OA-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Oportunidades Ativas |"""
if malformed not in text:
    raise SystemExit("Malformed institutional rows not found")
text = text.replace(malformed, corrected, 1)

governance = """| PAS-001-OA-EVENT-001 | Active 1.0.0 |
| GLPA-001 | Approved 1.1.1 |"""
governance_corrected = """| PAS-001-OA-EVENT-001 | Active 1.0.0 |
| PAS-001-OA-INTEGRATION-001 | Active 1.0.0 |
| GLPA-001 | Approved 1.1.1 |"""
if governance not in text:
    raise SystemExit("Governance insertion point not found")
text = text.replace(governance, governance_corrected, 1)

path.write_text(text, encoding="utf-8")
run("git", "diff", "--check")
run("git", "add", str(path))
run("git", "commit", "-m", "fix(board): corrigir registro de integrações de Oportunidades Ativas")
run("git", "rm", ".github/scripts/fix_oa_board.py")
run("git", "commit", "-m", "chore(automation): remover correção temporária")
branch = os.environ.get("GITHUB_HEAD_REF") or os.environ["GITHUB_REF_NAME"]
run("git", "push", "origin", f"HEAD:{branch}")
