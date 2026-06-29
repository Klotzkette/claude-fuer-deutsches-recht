---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Datenschutzrecht DSGVO/BDSG: ordnet Rolle (Verantwortlicher, Auftragsverarbeiter, Betroffener), markiert Frist (Art. 33 Meldung 72h), wählt Norm (DSGVO Art. 5/6/13/15/28/32/33/35, BDSG, TTDSG) und Zuständigkeit (BfDI Bund), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Datenschutzrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Kernrouten zuerst

Starte nicht mit der Gesamtlandkarte. Ordne den Fall zuerst in eine dieser Arbeitsrouten ein und liefere danach das passende Produkt:

| Route | Sofortfrage | Arbeitsprodukt |
| --- | --- | --- |
| Betroffenenrecht | Auskunft, Löschung, Berichtigung, Widerspruch oder Kopie? | Fristenblatt mit Antwortentwurf |
| Datenpanne | Kenntniszeitpunkt, Risiko, betroffene Gruppen, Eindämmung? | 72-Stunden-Timeline mit Meldeentscheidung |
| Auftragsverarbeitung | Verantwortlicher, Auftragsverarbeiter oder gemeinsame Verantwortung? | Rollenmatrix und Vertragslückenliste |
| Aufsicht und Sanktion | Anhörung, Auskunftsverlangen, Anordnung oder Bußgeld? | Verteidigungstimeline mit Akten- und Beweisplan |
| Drittlandtransfer | Empfängerland, Tool, Standardklauseln, Zusatzmaßnahmen? | Transfer-Risiko- und Maßnahmenmatrix |
| Löschung und Aufbewahrung | Löschanspruch gegen gesetzliche Aufbewahrung oder Rechtsverteidigung? | Löschentscheidung mit Sperr- statt Löschalternative |

Wenn Fristdruck besteht, zuerst Kenntniszeitpunkt, Monatsfrist, 72-Stunden-Frist, Zuständigkeit und Beweisunterlagen sichern. Danach erst Detailnormen vertiefen.

## Fachlandkarte dieses Plugins

- `anwendungsfall-triage` — erste Rollen-, Fristen- und Output-Weiche
- `dsgvo-auskunft` — Auskunftsersuchen prüfen und beantworten
- `datenschutz-loeschpflicht-art-17-und-aufbewahrung` — Löschung, Sperrung und Aufbewahrung trennen
- `datenschutz-beschwerde-art-77-aufsichtsbehoerde` — Beschwerde- und Behördenpfad
- `datenpanne-meldung` — Meldeentscheidung und 72-Stunden-Timeline
- `dsv-meldung-art-33-pflichtangaben` — Pflichtangaben für Vorfallmeldung
- `avv-art-28-mindestinhalte-checkliste` — Auftragsverarbeitungsvertrag prüfen
- `avv-art-26-joint-controllership-deutsch` — AVV ART 26 Joint Controllership Deutsch
- `drittlandstransfer-tia-scc` — Transfer Impact Assessment und Standardklauseln
- `dokumente-intake` — Unterlagen sortieren und Lücken schließen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Datenschutzrecht sind Artikel 15, Artikel 17, Artikel 28, Artikel 33, Artikel 44 ff., Bundesdatenschutzgesetz und Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
