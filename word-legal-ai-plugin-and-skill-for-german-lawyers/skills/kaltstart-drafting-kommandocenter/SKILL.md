---
name: kaltstart-drafting-kommandocenter
description: "Kaltstart-Kommandocenter für Word Legal AI. Führt deutsche Anwälte in maximal fünf Fragen vom diffusen Schreibauftrag zum Arbeitsmodus, Stilprofil, Dokumentgerüst, nächster Skill-Kette und erstem verwertbarem Output. Nutzt das Plugin word-legal-ai-plugin-and-skill-for-german-lawyers als Routing-Zentrale für Verträge, Schriftsätze, Mandantenmemos, Anwaltsschreiben, Redlines, Word-Finalisierung und US/UK-English-Drafting."
---

# Kaltstart-Drafting-Kommandocenter

## Zweck

Dieser Skill ist der schönere Einstieg in das Plugin. Er nimmt einen rohen Auftrag wie "mach daraus bitte einen guten Schriftsatz", "Partnerin will das in Word sauber haben" oder "wir brauchen den englischen Vertrag nach deutschem Recht" und verwandelt ihn sofort in eine Arbeitsstrecke.

Er arbeitet nicht akademisch. Er stellt wenige Fragen, entscheidet dann, welcher Modus passt, und schlägt die nächsten Skills aus diesem Plugin vor. Wenn genügend Material vorliegt, liefert er sofort ein erstes Gerüst oder eine erste überarbeitete Passage.

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

## Output

Gib immer drei Dinge aus:

1. **Arbeitsmodus:** Was wird jetzt konkret gemacht?
2. **Skill-Kette:** Zwei bis fünf passende Skills aus diesem Plugin.
3. **Erster Output:** Gliederung, Klauselgerüst, Schriftsatzgerüst, Redline-Plan oder Stilprofil.

## Qualitätsmaßstab

- Kein leerer Rat wie "Bitte laden Sie weitere Informationen hoch", wenn aus dem Auftrag schon ein sinnvolles Gerüst gebaut werden kann.
- Keine falsche Genauigkeit. Bei unsicherem Sachverhalt mit Annahmen arbeiten und diese offen markieren.
- Keine Platzhalterlawine. Höchstens wenige eckige Platzhalter, die wirklich ausgefüllt werden müssen.
- Immer den nächsten konkreten Arbeitsschritt nennen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
