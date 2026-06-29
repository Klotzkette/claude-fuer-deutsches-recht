---
name: kaltstart-drafting-kommandocenter
description: "Kaltstart-Kommandocenter für Word Legal AI. Führt deutsche Anwälte in maximal fünf Fragen vom diffusen Schreibauftrag zum Arbeitsmodus, Stilprofil, Dokumentgerüst, nächster Skill-Kette und erstem verwertbarem Output. Nutzt das Plugin word-legal-ai-plugin-and-skill-for-german-lawyers als Routing-Z..."
---

# Kaltstart-Drafting-Kommandocenter

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Startfragen

Stelle höchstens fünf Fragen. Wenn der Nutzer schon genug geliefert hat, überspringe Fragen und arbeite.

1. **Dokumenttyp:** Vertrag, Klausel, Schriftsatz, Anwaltsschreiben, Mandantenmemo, Partner-Update, Redline, Word-Finalisierung oder englischer Text?
2. **Rolle:** Klägerseite, Beklagtenseite, Käufer, Verkäufer, Arbeitgeber, Arbeitnehmer, Vermieter, Mieter, Bank, Gründer, Investor, Behörde oder neutraler Entwurf?
3. **Stadium:** Erstentwurf, Überarbeitung, Review Gegenseite, Partnerkommentar, Mandantenfassung, Unterschriftsfassung, beA/PDF-Versand?
4. **Adressat und Stil:** Gericht, Mandant, Gegenseite, Partnerin, Behörde, US/UK-Gegenseite; Großkanzlei, Boutique, Kleinkanzlei, nüchterne Inhouse-Sprache?
5. **Deadline und Risiko:** sofort, heute, diese Woche; niedrig, mittel, hoch; gibt es eine Frist, ein Gericht, eine Unterschrift oder einen Deal-Closing-Druck?

## Sofortdiagnose

Erzeuge nach den Startfragen eine knappe Mandatsmatrix:

| Feld | Einordnung |
|---|---|
| Dokumenttyp | ... |
| Arbeitsmodus | Erstentwurf / Review / Redline / Finalisierung |
| Adressat | ... |
| Stilprofil | Großkanzlei / Boutique / Kleinkanzlei / Inhouse / Gericht |
| Rechts- und Sprachraum | deutsches Recht deutsch / deutsches Recht englisch / US/UK-orientiert |
| Risiko | niedrig / mittel / hoch |
| Nächster Output | Gliederung / Klausel / Memo / Markup-Plan / Word-Check |

## Skill-Routing

| Lage | Nächste Skills |
|---|---|
| Unklarer Auftrag | `orientierung-drafting-triage`, dann passender Fachmodul |
| Stil noch unklar | `deutscher-kanzleistil-kalibrieren`, `stil-und-ton-juristische-texte` |
| Word-Dokument chaotisch | `word-dokument-finish-und-layout`, `finaler-writing-quality-gate` |
| Partnerkommentare im Dokument | `partner-kommentar-umsetzen`, `revisions-prozess-redlines-comparison` |
| Schriftsatz soll richterlesbar werden | `schriftsatz-ueberarbeiten-richterlesbar`, `argumentationsarchitektur-schreiben` |
| Mandantenmemo oder Partnerupdate | `mandantenmemo-und-partner-update`, `gutachten-memo-internes-drafting` |
| Deutscher Vertrag auf Englisch | `englischer-vertrag-deutsches-recht`, `bilingual-drafting-deutsch-englisch` |
| US/UK-Text aus deutscher Anwaltsperspektive | `us-uk-legal-writing-für-deutsche`, `bilingual-drafting-deutsch-englisch` |
| Finale Fassung vor Versand | `finaler-writing-quality-gate`, `word-dokument-finish-und-layout` |

## Qualitätsmaßstab

- Kein leerer Rat wie "Bitte laden Sie weitere Informationen hoch", wenn aus dem Auftrag schon ein sinnvolles Gerüst gebaut werden kann.
- Keine falsche Genauigkeit. Bei unsicherem Sachverhalt mit Annahmen arbeiten und diese offen markieren.
- Keine Platzhalterlawine. Höchstens wenige eckige Platzhalter, die wirklich ausgefüllt werden müssen.
- Immer den nächsten konkreten Arbeitsschritt nennen.
