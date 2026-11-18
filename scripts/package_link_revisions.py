"""Verifizierte reine Paketlink-Korrektur ohne Änderung historischer Prüfbelege."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, unquote

MANIFEST = 'quality/hauptskills-2026-11-18/paketverweise.json'
ARCHIVE = 'quality/hauptskills-2026-11-18/paketlink-vorfassungen/'
LINK = re.compile(r'\]\(([^)\s]+)\)')
WEB = 'https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/'
PAGES = 'https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path='


def sha(data): return hashlib.sha256(data).hexdigest()


def load(path):
    def unique(pairs):
        result = {}
        for k,v in pairs:
            if k in result: raise ValueError('Doppeltes Feld im Paketlink-Nachweis')
            result[k]=v
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)


def safe(root, relative):
    if not isinstance(relative,str) or not relative or '\\' in relative:
        raise ValueError('Ungültiger Paketlink-Pfad')
    p=Path(relative)
    if p.is_absolute() or '..' in p.parts or (root/p).is_symlink():
        raise ValueError('Unzulässiger Paketlink-Pfad')
    target=(root/p).resolve()
    if not target.is_relative_to(root.resolve()):raise ValueError('Paketlink-Pfadausbruch')
    return target


def rows(root):
    path=root/MANIFEST
    if not path.exists():return []
    value=load(path)
    entries=value['files'] if isinstance(value,dict) else value
    if not isinstance(entries,list) or len({r['path'] for r in entries})!=len(entries):
        raise ValueError('Keine eindeutigen Paketlink-Nachweise')
    return entries


def previous_bytes(root, path, *, plugin=None):
    root,path=Path(root).resolve(),Path(path).resolve()
    relative=path.relative_to(root).as_posix()
    row=next((r for r in rows(root) if r['path']==relative),None)
    if row is None:return None
    if plugin is not None and row['plugin']!=plugin:raise ValueError('Paketlink-Plugin verwechselt')
    entries=load(root/'.claude-plugin/marketplace.json')['plugins']
    source=next((safe(root,p['source']) for p in entries if p['name']==row['plugin']),None)
    if source is None or not path.is_relative_to(source) or path.relative_to(source).parts[0] not in {'skills','references'} or path.suffix!='.md':
        raise ValueError('Keine zulässige Paketlink-Quelldatei')
    if row['archive']!=ARCHIVE+relative+'.txt':raise ValueError('Falsches Paketlink-Archiv')
    old=safe(root,row['archive']).read_bytes(); current=path.read_bytes()
    followup=row.get('main_revision_followup')
    if followup is not None:
        # Drei Hauptskills wurden nach der reinen Linkreparatur nochmals
        # redaktionell geglättet. Den mechanischen Zwischenschritt weiterhin
        # bytegenau prüfen; den heutigen Text ausschließlich über seinen
        # vollständigen Hauptskill-/Einzelprüfungsnachweis zulassen.
        from main_skill_revisions import REGISTRY, index, previous_bytes as main_previous_bytes
        expected_archive='quality/hauptskills-2026-11-18/paketlink-zwischenfassungen/'+relative+'.txt'
        if (not isinstance(followup,dict) or followup.get('registry')!=REGISTRY
                or followup.get('archive')!=expected_archive or relative not in index(root)):
            raise ValueError('Keine belegte Hauptskill-Fortsetzung der Paketlink-Korrektur')
        main_previous_bytes(root,path,plugin=row['plugin'])
        current=safe(root,expected_archive).read_bytes()
    if sha(old)!=row['before_sha256'] or sha(current)!=row['after_sha256']:
        raise ValueError('Paketlink-Datei seit Prüfung verändert')
    replacements={}
    for change in row['replacements']:
        original=change['old']; new=change['new']
        if original in replacements:raise ValueError('Doppelte Paketlink-Ersetzung')
        original_path,separator,anchor=original.partition('#')
        target=safe(root,change['target'])
        if (path.parent/unquote(original_path)).resolve()!=target or not target.is_file():
            raise ValueError('Paketlink-Ziel entspricht nicht dem vorhandenen Originalziel')
        kind=change['kind']
        if kind=='local_reference':
            if target != root/'references/zitierweise.md':raise ValueError('Ungeprüfte zentrale Paketabhängigkeit')
            copied=safe(root,change['copied_to'])
            if (copied != source/'references/zitierweise.md' or copied.read_bytes()!=target.read_bytes()
                    or sha(copied.read_bytes()) != change.get('copied_sha256')):
                raise ValueError('Zitierweise ist keine bytegleiche lokale Kopie')
            expected=os.path.relpath(copied,path.parent).replace(os.sep,'/')+separator+anchor
        elif kind=='prompt_download':
            if not target.is_relative_to(source) or not target.name.endswith(('-werkstatt.md','-schnellstart.md','-hauptproblem.md','-werkstatt.txt','-schnellstart.txt','-hauptproblem.txt')):
                raise ValueError('Keine eigenständige Promptdatei')
            expected=PAGES+quote(target.relative_to(root).as_posix(),safe='/')+separator+anchor
        elif kind=='public_repository':
            if target.relative_to(root).parts[0] not in {'testakten','quality'}:
                raise ValueError('Ungeprüftes öffentliches Paketlink-Ziel')
            expected=WEB+quote(target.relative_to(root).as_posix(),safe='/')+separator+anchor
        else:raise ValueError('Unbekannte Paketlink-Korrekturart')
        if new!=expected:raise ValueError('Paketlink verweist auf ein anderes Ziel')
        replacements[original]=new
    found=set()
    def replace(match):
        old_target=match[1]
        if old_target not in replacements:return match[0]
        found.add(old_target)
        return ']('+replacements[old_target]+')'
    revised=LINK.sub(replace,old.decode('utf-8')).encode('utf-8')
    if found!=set(replacements) or revised!=current:
        raise ValueError('Paketlink-Nachführung verändert mehr als belegte Markdown-Ziele')
    return old


def validate_all(root):
    root=Path(root).resolve()
    for row in rows(root):previous_bytes(root,safe(root,row['path']),plugin=row['plugin'])
    return len(rows(root))
