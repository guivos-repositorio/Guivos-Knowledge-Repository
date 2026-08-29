from pathlib import Path

p = Path('docs/governance-framework/brand-public-authority-propagation.md')
s = p.read_text(encoding='utf-8')

replacements = [
    ('version: 1.1.0', 'version: 1.2.0'),
    ('last_updated: 2026-08-27', 'last_updated: 2026-08-29'),
    ('  - ROADMAP-13.1.0', '  - ROADMAP-13.2.0'),
    ('| `GKR-STATE-001 v3.1.0` | `ABSORBED` | estado global já incorporado |', '| `GKR-STATE-001 v3.2.0` | `ABSORBED` | estado global já incorporado |'),
]
for old, new in replacements:
    count = s.count(old)
    if count != 1:
        raise SystemExit(f'expected exactly 1 occurrence of {old!r}, found {count}')
    s = s.replace(old, new)

for stale in ['ROADMAP-13.1.0', 'GKR-STATE-001 v3.1.0']:
    if stale in s:
        raise SystemExit(f'stale current reference survived: {stale}')

p.write_text(s, encoding='utf-8')
