# 13 — Internet-URL-Pflicht und Archivierung

**Kanzleihandbuch Zitierweise v4.0 — URL-Standard**
**Stand: Oktober 2025**

---

## A. URL-Pflicht

Gemaess Hauszitierregel C.1 ist bei jeder Entscheidung, die frei online zugänglich ist, die URL anzugeben. Quellen, die diese Pflicht auslösen:

- dejure.org (Rechtsprechungsnachweise, z.T. Volltext)
- openjur.de (Volltext OLG, LG, BSG, BAG u.a.)
- bundesgerichtshof.de (amtlicher BGH-Server)
- bundesverfassungsgericht.de (amtlicher BVerfG-Server)
- bundesfinanzhof.de (amtlicher BFH-Server)
- bverwg.de (amtlicher BVerwG-Server)
- bsg.bund.de (amtlicher BSG-Server)
- bundesarbeitsgericht.de (amtlicher BAG-Server)
- eur-lex.europa.eu (EuGH, EuG — EU-Recht)

---

## B. URL-Format

**Standard-Format:**
```
abrufbar unter: [URL] (abgerufen am TT.MM.JJJJ).
```

**Mit Archivlink:**
```
abrufbar unter: [URL] (abgerufen am TT.MM.JJJJ; archiviert unter: https://web.archive.org/web/[TIMESTAMP]/[URL]).
```

---

## C. Stabilitaetsstufen

| Quelle | Stabilität | Archivlink erforderlich? |
|---|---|---|
| bundesgerichtshof.de | Sehr hoch (staatlich) | Nein — zulässig |
| bundesverfassungsgericht.de | Sehr hoch (staatlich) | Nein — zulässig |
| bundesfinanzhof.de | Sehr hoch (staatlich) | Nein — zulässig |
| bverwg.de | Sehr hoch (staatlich) | Nein — zulässig |
| eur-lex.europa.eu | Sehr hoch (EU-amtlich) | Nein — zulässig |
| dejure.org | Hoch (stabil, 15+ Jahre) | Empfohlen, nicht zwingend |
| openjur.de | Mittel (privates Projekt) | Empfohlen |
| Sonstige private Server | Gering bis mittel | Ja — Pflicht (Kategorie B) |

---

## D. Wayback Machine — Archivierungsformat

**Archivlink-Format:**
```
https://web.archive.org/web/[14-stelliger-Timestamp]/[original-URL]
```

**Timestamp:** JJJJMMTTHHMMSSS (z.B. 20250901000000 für 01.09.2025 00:00:00)

**Beispiel:**
```
abrufbar unter: https://openjur.de/u/2312345.html (abgerufen am 01.10.2025; archiviert unter: https://web.archive.org/web/20250901000000/https://openjur.de/u/2312345.html).
```

---

## E. URLs in Druckerzeugnissen

In Schriftsaetzen und Handbuchdruckversionen werden URLs vollständig ausgeschrieben. Ein QR-Code kann ergänzt werden. Bei sehr langen URLs ist ein URL-Shortener zulässig, sofern der Link dauerhaft stabil ist (kanzleiinternes Linkmanagement empfohlen).

---

## F. Prüfpunkte URL-Audit

| Prüfpunkt | Pruefung |
|---|---|
| URL erreichbar | Manuell oder automatisiert testen |
| HTTPS | Nur HTTPS-URLs (kein HTTP) |
| Kein Redirect-Loop | Direktlink, kein Weiterleitung auf Suchseite |
| Abrufdatum vorhanden | Format TT.MM.JJJJ |
| Archivlink (wenn erford.) | Wayback-Machine-Link geprüft |

---

*Kanzleihandbuch Zitierweise v4.0 — URL-Standard. Stand: Oktober 2025.*
