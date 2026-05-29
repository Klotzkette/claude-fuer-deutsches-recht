#!/usr/bin/env python3
r"""
Echter YAML-Parser-Check für alle SKILL.md im Repo.
Fängt genau das ab, was 'claude plugin validate --strict' moniert:
- Unescapte " innerhalb von "..."-Strings (Quote-Sweep-Fehler)
- \& oder andere ungültige YAML-Escapes
- Defektes Frontmatter generell

Aufruf: python3 scripts/validate-yaml-frontmatter.py
Exit 0 bei OK, 1 bei Fehlern.
"""
import os, sys, re

try:
    import yaml
except ImportError:
    print("FEHLER: pyyaml fehlt. Installation: pip3 install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

errors = []
warnings = []

for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    for f in files:
        if f != 'SKILL.md':
            continue
        p = os.path.join(root, f)
        with open(p, encoding='utf-8') as fh:
            content = fh.read()
        if not content.startswith('---'):
            errors.append(f"{p}: keine Frontmatter")
            continue
        try:
            end_idx = content.index('\n---', 3)
        except ValueError:
            errors.append(f"{p}: Frontmatter nicht terminiert (--- fehlt)")
            continue
        fm_str = content[4:end_idx]
        try:
            fm = yaml.safe_load(fm_str)
        except yaml.YAMLError as e:
            errors.append(f"{p}: YAML-Parse-Fehler: {e}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{p}: Frontmatter ist kein Dict")
            continue
        # Pflichtfelder
        if 'name' not in fm:
            errors.append(f"{p}: 'name' fehlt")
        if 'description' not in fm:
            errors.append(f"{p}: 'description' fehlt")
        # name-Validierung
        name = fm.get('name', '')
        if not isinstance(name, str):
            errors.append(f"{p}: 'name' muss String sein, ist {type(name).__name__}")
        elif not re.match(r'^[a-z0-9-]{1,64}$', name):
            errors.append(f"{p}: 'name' '{name}' invalid (kebab-case, max 64)")
        # Ordnername == name
        skill_dir = os.path.basename(os.path.dirname(p))
        if name != skill_dir:
            errors.append(f"{p}: 'name' '{name}' != Ordnername '{skill_dir}'")
        # description-Validierung
        desc = fm.get('description', '')
        if not isinstance(desc, str):
            errors.append(f"{p}: 'description' muss String sein, ist {type(desc).__name__}")
        elif len(desc) > 1024:
            errors.append(f"{p}: 'description' zu lang ({len(desc)} > 1024)")
        elif len(desc) == 0:
            errors.append(f"{p}: 'description' leer")
        # XML-Tag-Verbot
        if isinstance(desc, str) and re.search(r'<[a-zA-Z]', desc):
            warnings.append(f"{p}: 'description' enthält möglicherweise XML-Tags")
        # Komma-Zahl-Pattern (Cowork-Validator)
        if isinstance(desc, str) and re.search(r'\d\s*,\s*\d', desc):
            errors.append(f"{p}: 'description' enthält Zahl-Komma-Zahl (Cowork bricht)")
        # Verbotene Felder
        for vk in ['triggers','when_to_use','language','rechtsgebiet','license','argument-hint','user-invocable','allowed_tools','tools','model','adapted_from','version','related_skills']:
            if vk in fm:
                errors.append(f"{p}: verbotenes Feld '{vk}'")
        # Unbekannte Felder
        allowed = {'name','description','allowed-tools'}
        for k in fm:
            if k not in allowed and k not in ['triggers','when_to_use','language','rechtsgebiet','license','argument-hint','user-invocable','allowed_tools','tools','model','adapted_from','version','related_skills']:
                warnings.append(f"{p}: unbekanntes Feld '{k}'")

# Plugin-Root CLAUDE.md (von Claude Code als Warnung gemeldet)
for d in sorted(os.listdir('.')):
    if not os.path.isdir(d) or d.startswith('.'):
        continue
    if not os.path.isfile(os.path.join(d, '.claude-plugin', 'plugin.json')):
        continue
    if os.path.isfile(os.path.join(d, 'CLAUDE.md')):
        errors.append(f"{d}/CLAUDE.md: Plugin-Root-CLAUDE.md wird nicht geladen — als Skill verschieben oder löschen")

print(f"validate-yaml-frontmatter: {len(errors)} Fehler, {len(warnings)} Warnungen")
if warnings:
    for w in warnings[:20]:
        print(f"  WARN: {w}")
if errors:
    for e in errors:
        print(f"  FEHLER: {e}", file=sys.stderr)
    sys.exit(1)

print("OK")
