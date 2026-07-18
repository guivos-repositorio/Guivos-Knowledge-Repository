from __future__ import annotations

from pathlib import Path
import runpy
import subprocess
import traceback

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, check=check, text=True, capture_output=True)


def configure() -> None:
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")


try:
    runpy.run_path(str(ROOT / "scripts/sync_pas_recon.py"), run_name="__main__")
except Exception:
    error = traceback.format_exc()
    git("reset", "--hard", "HEAD")
    (ROOT / "sync-pas-recon-error.txt").write_text(error, encoding="utf-8")
    configure()
    git("add", "sync-pas-recon-error.txt")
    git("commit", "-m", "record PAS reconciliation sync error [skip ci]")
    git("push", "origin", "HEAD")
    raise
else:
    for relative in [
        "scripts/run_sync_pas_recon.py",
        "scripts/patch_sync_pas_recon.py",
        "sync-pas-recon-error.txt",
    ]:
        path = ROOT / relative
        if path.exists():
            path.unlink()
    configure()
    git("add", "-A")
    status = git("status", "--porcelain").stdout.strip()
    if status:
        git("commit", "-m", "remove PAS reconciliation diagnostic files")
        git("push", "origin", "HEAD")
