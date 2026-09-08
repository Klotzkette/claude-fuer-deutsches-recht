"""Hält ausdrücklich umgestellte README-Seiten dezimal und navigierbar."""

import re
import unicodedata

OPT_IN = '<!-- decimal-headings -->'
ALIAS = '<!-- decimal-anchor -->'


def title_text(text: str) -> str:
    return re.sub(r'^\d+(?:\.\d+)*\.\s+', '', text.strip())


def anchor(text: str) -> str:
    text = re.sub(r'[`*_~]', '', text).lower()
    return ''.join(c for c in text if c in '-_' or c.isspace() or unicodedata.category(c)[0] in 'LMN').replace(' ', '-').replace('\t', '-')


def normalize_decimal_headings(text: str) -> str:
    if OPT_IN not in text:
        return text
    counters = [0] * 6
    seen = {}
    fence = None
    skip_alias_blank = False
    lines = []
    for line in text.splitlines():
        if skip_alias_blank:
            skip_alias_blank = False
            if not line:
                continue
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append(line)
            continue
        if fence is None and re.fullmatch(r'<!-- decimal-anchor --> <a id="[^"]+"></a>', line):
            skip_alias_blank = True
            continue
        heading = re.match(r'^(#{1,6})\s+(.+?)\s*$', line) if fence is None else None
        if not heading:
            lines.append(line)
            continue
        level = len(heading.group(1))
        title = title_text(heading.group(2))
        for parent in range(level - 1):
            counters[parent] = max(counters[parent], 1)
        counters[level - 1] += 1
        counters[level:] = [0] * (6 - level)
        number = '.'.join(str(n) for n in counters[:level])
        base = anchor(title)
        count = seen.get(base, 0)
        seen[base] = count + 1
        stable = base if count == 0 else f'{base}-{count}'
        lines.extend([f'{ALIAS} <a id="{stable}"></a>', '', f'{heading.group(1)} {number}. {title}'])
    return '\n'.join(lines) + '\n'
