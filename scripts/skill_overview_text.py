"""Beschreibungen aus Skill-Frontmatter für die öffentlichen Tabellen."""
from pathlib import Path
import re

import yaml

from readme_display import display_prose


def description(path: Path, *, limit: int | None = 240, vergaberolle: bool = False) -> str:
    with path.open(encoding="utf-8") as stream:
        if stream.readline().strip() != "---":
            return ""
        lines = []
        for line in stream:
            if line.rstrip() == "---":
                break
            lines.append(line)
        else:
            return ""
    meta = yaml.safe_load("".join(lines))
    if not isinstance(meta, dict) or not isinstance(meta.get("description"), str) or not meta["description"].strip():
        return ""
    text = " ".join(meta["description"].split())
    text = re.sub(r'\s+[—-]\s*Arbeitskontext:\s*[^.]+,\s*Schwerpunkt\s+[^.]+\.?', '', text)
    text = re.sub(r'\s+im Plugin\s+[^.:"`|]+(?=[:.])|\s+im Plugin\s+[^"`|]+$', '', text).strip()
    if vergaberolle:
        text = re.sub(r"\b(?:Paragrafen|Paragraphen)\s+(?=\d)", "§§ ", text)
        text = re.sub(r"\b(?:Paragraf|Paragraph)\s+(?=\d)", "§ ", text)
        text = re.sub(r"\b(?:Paragraf|Paragraph)-(?=\d)", "§-", text)
    else:
        text = display_prose(text)
    text = text.replace("|", r"\|")
    if limit is None or len(text) <= limit:
        return text
    if vergaberolle:
        cut = max(text.rfind(punct, 0, 225) for punct in (". ", "; ", ", "))
        if cut >= 120:
            text = text[:cut + 1].rstrip(" ,;:")
            return text if text.endswith((".", "!", "?")) else text + "."
        return text[:236].rstrip(" ,.;:") + "."
    return text[:limit - 3].rstrip() + "..."
