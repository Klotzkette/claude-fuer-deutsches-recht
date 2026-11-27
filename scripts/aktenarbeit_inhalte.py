"""Stellt die belegte Korrespondenz und den zugehörigen Arbeitsvermerk einer Fallakte zusammen."""

from __future__ import annotations

import json
from pathlib import Path
import re
from zipfile import ZipFile

from aktenarbeit_prueffragen import PRUEFFRAGEN
from aktenarbeit_quellen import attached_mail, evidence_excerpt, extract, german_date, local_bytes, local_reference, saetze, source_name
from akteneingang.quellen import DATA

FAMILIEN = {
    "eml": ("brief", "E-Mail"), "brief": ("brief", "Brief"),
    "notiz": ("vermerk", "Interne Notiz"), "chat": ("protokoll", "Gesprächsprotokoll"),
    "tabelle": ("protokoll", "Arbeitsliste"),
}
# Für technische Vorfall-, Straf- und Kontrolldossiers werden nur die
# redigierten Aussagen des Posteingangs und Belegbezeichnungen verwendet.
VERFAHRENSAKTE = re.compile(
    r"straf|ransom|cyber|datensicherheit|phishing|nis2|btm-|bet[aä]e?ubung|drohne|sanktion|exportkontrolle|"
    r"dual-use|stalking|gewaltschutz|terror|waffe|munition|militaer|biotech|gentech|biowaff|"
    r"kritis|drohung|angriff|pentest|it-sicherheit|malware|biometri|infektion", re.I
)
BELEGE = {".eml", ".docx", ".pdf", ".csv", ".txt", ".md", ".xlsx", ".jpg", ".jpeg", ".png"}
STOFF = {".docx", ".pdf", ".eml", ".csv", ".md", ".txt", ".xlsx"}

# Entscheidungstragende Anlagen bei zwei Vorgängen mit parallelen Losen
# und Wertungen. Es werden stets die Texte der bezeichneten Akte gelesen.
WERTUNGSUNTERLAGEN = {
    "interstate-09-brueckenneubau": {
        "01_losplanung.docx": "Absatz 7", "10_widerspruch_talbogen.eml": "Nachrichtentext",
    },
    "interstate-11-it-baupruefung": {
        "04_bieterfrage_und_antwort.txt": "Textabsatz 3", "06_wertungsbogen.xlsx": "Aufstellung!A6",
    },
}


def postquellen(root):
    """Jede redigierte Nachricht bleibt über JSON-Datei und JSON-Pointer nachlesbar."""
    result = {}
    for name in ("a-f", "g-q", "r-z", "lokal", "weitere"):
        path = DATA / f"{name}.json"
        for key, record in json.loads(path.read_text(encoding="utf-8")).items():
            fall = key if "/" in key else "testakten/" + key
            escaped = key.replace("~", "~0").replace("/", "~1")
            sources = [f"{path.relative_to(root).as_posix()}#/{escaped}/unterlagen/{i}"
                       for i in range(len(record["unterlagen"]))]
            result[fall] = record, sources
    return result


def aus_grundakte(root, item):
    folder = item["ordner"]
    addresses = []
    if folder and (root / folder / "Grundakte").is_dir():
        addresses = [p.relative_to(root).as_posix() for p in (root / folder / "Grundakte").rglob("*")
                     if p.is_file() and p.suffix.lower() in BELEGE]
    if not addresses:
        for location in item["archive"]:
            with ZipFile(root / location) as archive:
                names = [n for n in archive.namelist() if Path(n).suffix.lower() in BELEGE]
            basis = [n for n in names if "grundakte" in Path(n.lower()).parts]
            if not basis:
                basis = [n for n in names if not any(x in n.lower() for x in (
                    "nachreich", "lösung", "loesung", "musterantwort", "readme", "hinweisblatt", "vorlage"
                ))]
            if any(n.lower().endswith(".eml") for n in basis):
                addresses = [location + "!" + n for n in basis]
                break
    return sorted(addresses, key=lambda a: (source_name(a).lower(), a))


def titel(root, key, item, ersatz):
    path = root / item["seite"]
    if key.endswith(".zip") or (item["ordner"] and Path(item["ordner"]) != Path(item["seite"]).parent
                                 and len(list(Path(path.parent).glob("*/"))) > 1):
        return ersatz
    headings = re.findall(r"^#\s+(.+?)\s*$", path.read_text(encoding="utf-8"), re.M)
    return re.sub(r"^\d+\.\s+", "", headings[0]).strip() if headings else ersatz


def dokument(mail, fall):
    art, familie = FAMILIEN[mail["typ"]]
    sender, sep, address = mail["von"].partition(" <")
    unit = address.rstrip(">") if sep else (familie if mail["typ"] == "eml" else "")
    doc = {"kind": art, "title": mail["titel"], "sender": sender, "unit": unit,
           "recipient": f"An {mail['an']}" if mail.get("an") else "", "date": german_date(mail.get("datum")),
           "case": fall}
    texte = mail["text"]
    if mail["typ"] == "tabelle":
        rows = [[t.strip() for t in s.split("|")] for s in texte]
        if len(rows[0]) > 1 and all(len(row) == len(rows[0]) for row in rows):
            doc["sections"] = [{"table": {"headers": rows[0], "rows": rows[1:]}}]
            return doc
    doc["sections"] = [{"paragraphs": texte}]
    return doc


def benutzbare_post(root, address):
    mail = attached_mail(local_bytes(root, address))
    if not mail or not 80 <= sum(map(len, mail["text"])) <= 6500:
        return None
    body = "\n".join(mail["text"])
    if any(tag in body for tag in ("-----Original Message-----", "<html", "Content-Type:", "\ufffd")):
        return None
    return mail


def originalnachricht(root, item, sources):
    for address in sources:
        if address.lower().endswith(".eml") and (mail := benutzbare_post(root, address)):
            return mail, address
    raise ValueError(f"Kein lesbares Eingangsschreiben: {item['id']}")


def fundstellen(root, key, addresses, query, vorgabe):
    ergebnis = []
    for address in addresses:
        data = local_bytes(root, address)
        if VERFAHRENSAKTE.search(key) or Path(source_name(address)).suffix.lower() not in STOFF:
            quote, point = "", ""
        else:
            paragraphs = extract(data, address)
            point = vorgabe.get(source_name(address))
            if point:
                quote = next(text for text, stelle in paragraphs if stelle == point)
            else:
                quote, point = evidence_excerpt(paragraphs, query)
        ergebnis.append({"address": address, "name": source_name(address), "point": point, "quote": quote})
    return ergebnis


def formulierfeld(address):
    suffix = Path(source_name(address)).suffix.lower()
    if suffix in (".csv", ".xlsx"):
        return "Welche Zeile trägt den Ansatz? Rechenweg, abweichende Werte und Stichtag festhalten."
    if suffix == ".eml":
        return "Welche Aussage stammt aus eigener Wahrnehmung? Rückfrage und empfangene Antwort festhalten."
    if suffix in (".jpg", ".jpeg", ".png"):
        return "Welches Detail lässt sich erkennen? Bildausschnitt, Aufnahmesituation und Grenzen der Aussage vermerken."
    return "Welche Passage trägt die Aussage? Seite oder Abschnitt eintragen und einen verbleibenden Widerspruch benennen."


def akte(root, key, item, redaktion):
    restricted = bool(VERFAHRENSAKTE.search(key))
    vorgabe = WERTUNGSUNTERLAGEN.get(item["id"], {})
    if key in redaktion:
        record, origins = redaktion[key]
        docs = record["unterlagen"]
        original = [local_reference(key, name) for name in record["bezug"]]
        # Der gesonderte Brief ist eine eigenständige, bereits in der Akte
        # überlieferte Dokumentgattung. Gleiches gilt für Chats und Arbeitslisten.
        idx = next((i for art in ("brief", "chat", "tabelle") for i, doc in enumerate(docs) if doc["typ"] == art), 0)
        if idx == 0:
            idx = next((i for i, d in enumerate(docs) if d["typ"] == "notiz" and re.search(
                r"Telefonnotiz|Aktennotiz|Übergabe|Rückruf|Gespräch|Abstimmung", d["titel"], re.I)), 0)
        src, origin = docs[idx], origins[idx]
        if src["typ"] == "eml" and not restricted:
            for address in original:
                if address.lower().endswith(".eml") and (mail := benutzbare_post(root, address)):
                    src, origin = mail, address
                    break
        post, post_origin = docs[0], origins[0]
        neben_index = next((i for i in range(1, len(docs)) if docs[i]["typ"] != "tabelle"), 1)
        neben, neben_origin = docs[neben_index], origins[neben_index]
    else:
        sources = aus_grundakte(root, item)
        src, origin = originalnachricht(root, item, sources)
        post, post_origin = src, origin
        neben = None
        neben_origin = None
        other = [s for s in sources if s != origin and Path(source_name(s)).suffix.lower() in STOFF]
        # Zwei fachlich verschiedene Unterlagen der Grundakte, bevorzugt
        # Entscheidungsvorlagen, Verträge und die Sicht eines anderen Beteiligten.
        docs = [s for s in other if s.lower().endswith((".docx", ".pdf"))]
        mails = [s for s in other if s.lower().endswith(".eml")]
        if vorgabe:
            original = [next(s for s in other if source_name(s) == name) for name in vorgabe]
        else:
            original = list(dict.fromkeys((*docs[:1], *mails[:1], *other)))[:2]
    fall = titel(root, key, item, post["titel"])
    working = {"kind":"vermerk", "sender":"Fallbearbeitung",
               "case": fall, "title": post["titel"],
               "sections": [{"heading":"Anliegen im Wortlaut", "paragraphs": [
                   " · ".join(filter(None, [post["von"], german_date(post.get("datum"))])),
                   *post["text"],
               ]}]}
    evidence = []
    if neben:
        if neben["typ"] == "tabelle":
            source_section = dokument(neben, fall)["sections"][0]
            working["sections"].append({"heading": neben["titel"], **source_section})
        else:
            evidence.append({"title": neben["titel"], "source": " · ".join(filter(None, [
                FAMILIEN[neben["typ"]][1], neben["von"], german_date(neben.get("datum"))])),
                             "text":"\n".join(neben["text"])})
    belegliste = fundstellen(root, key, original, post["titel"] + " " + " ".join(post["text"]), vorgabe)
    for beleg in belegliste[:3]:
        evidence.append({"title":beleg["name"], "source": beleg["point"],
                         "text": ("„" + beleg["quote"] + "“") if beleg["quote"] else ""})
    working["evidence"] = evidence
    name = source_name(original[0]) if original else post["titel"]
    # Greife den konkreten Fragesatz aus der Akte auf. Wo der Auftrag als
    # Arbeitsbitte formuliert ist, bleibt dessen Gegenstand über den Betreff benannt.
    fragen = []
    for paragraph in [*post["text"], post["titel"]]:
        fragen.extend(s.strip() for s in saetze(paragraph)
                      if s.endswith("?") and 16 <= len(s) <= 210)
    kontakt = post["von"].split(" <", 1)[0]
    antwort = f"Antwort an {kontakt} auf die Frage „{fragen[0]}“" if fragen else (
        f"Was lässt sich {kontakt} zum Anliegen „{post['titel']}“ belegt mitteilen?")
    working["fields"] = [f"Abgleich mit „{name}“: {formulierfeld(name)}", antwort]
    if item["id"] in PRUEFFRAGEN:
        working["fields"].insert(0, PRUEFFRAGEN[item["id"]])
    letter = dokument(src, fall)
    if "#/" not in origin:
        letter["reference"] = source_name(origin)
    return fall, letter, working, FAMILIEN[src["typ"]][1], list(dict.fromkeys(filter(
        None, [origin, post_origin, neben_origin, *original])))
