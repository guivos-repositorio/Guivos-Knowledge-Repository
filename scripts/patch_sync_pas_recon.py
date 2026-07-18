from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "scripts/sync_pas_recon.py"
text = path.read_text(encoding="utf-8")
old = '    anchor = "| Conceito | Decisão | Situação |\\n|---|---|---|\\n"\n'
new = '    anchor = "## Conceitos funcionais do Journey\\n\\n| Conceito | Decisão | Situação |\\n|---|---|---|\\n"\n'
if text.count(old) != 1:
    raise RuntimeError(f"expected one matrix anchor assignment, found {text.count(old)}")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
error = root / "sync-pas-recon-error.txt"
if error.exists():
    error.unlink()
