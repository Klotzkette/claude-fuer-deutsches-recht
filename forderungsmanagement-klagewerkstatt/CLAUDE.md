# Hauspflichten — forderungsmanagement-klagewerkstatt

Verbindliche Regeln für jeden Lauf in diesem Plugin. Gilt für beide Skills.

## Pflichtschritte

1. **Online-Zuständigkeitsprüfung** ist Pflicht. Vor jeder Auslieferung der Klageschrift sind beide Quellen abzurufen und im Output mit Abrufdatum auszuweisen:
   - <https://www.justizadressen.nrw.de/de/justiz/suche>
   - <https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php>
2. **Sachliche Zuständigkeit** rechnerisch (§§ 23 Nr. 1, 71 GVG; Sondertatbestände beachten).
3. **Örtliche Zuständigkeit** rechtlich (§§ 12, 13, 17, 24, 29, 29c, 38 ZPO; grenzüberschreitend Brüssel Ia VO 1215/2012).
4. **BeA-SAFE-ID** des Empfangsgerichts: wenn nicht aus den Quellen abrufbar, mit Hinweis „über beA-Adressbuch zu ergänzen" markieren.

## Stil

- **Zitierweise**: Pinpoint mit Randnummer; jüngere BGH-Entscheidungen zuerst; deutsche Kommentartradition (Bearbeiterstil mit Auflage, Jahr, Rn.).
- **Englische etablierte Begriffe** bleiben erhalten (NDA, SPA, MAC, Stakeholder, Compliance, BeA).
- **Auslöser** statt „Hooks"; **Agentenrezepte** statt „Cookbooks".
- **Memo** im Gutachtenstil nur auf ausdrückliche Anfrage.

## Format-/Banking-Wahl

- Am Anfang **einmal** fragen, welches Ergebnisformat gewünscht ist (DOCX + Markdown, zusätzlich Padlet?).
- Hausvorlage (DOCX) NICHT verändern, wenn der Nutzer einen Briefkopf mitgeliefert hat. Platzhalter respektieren.

## Plugin-Generator

- Output-Slug aus Kanzleinamen ableiten (lowercased, Umlaute transliteriert, Bindestriche).
- Erzeugtes Plugin enthält die Hausregeln fest verdrahtet und führt weiterhin die Online-Zuständigkeitsprüfung als Pflicht aus.

## Übergabe

- Bei drohender Zahlungsunfähigkeit der Beklagten an Liquiditätsplanung (`liquiditaetsplanung`).
- Bei einstweiligem Rechtsschutz / Mahnverfahren an `prozessrecht`.
- Wiederverwendung beim nächsten Mal über den Laufzeit-Skill `klage-aus-eigenem-skill`.
