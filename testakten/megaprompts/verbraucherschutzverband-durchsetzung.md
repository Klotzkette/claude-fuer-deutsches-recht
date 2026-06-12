# Megaprompt: verbraucherschutzverband-durchsetzung

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 106 Skills (gekuerzt fuer Chat-Fenster) des Plugins `verbraucherschutzverband-durchsetzung`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Verbraucherschutzverband Durchsetzung: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Rout…
2. **verbraucherverband-abhilfeklage-musterfeststellung-w-uklag** — Verbraucherschutzverband Durchsetzung: Abhilfeklage oder Musterfeststellung wählen. Abhilfeklage oder Musterfeststellung…
3. **finanzierung-interessenkonflikte** — Verbraucherschutzverband Durchsetzung: Finanzierung und Interessenkonflikte. Finanzierung und Interessenkonflikte im Fac…
4. **klageberechtigung-der-stelle-pruefen** — Verbraucherschutzverband Durchsetzung: Klageberechtigung der Stelle prüfen. Klageberechtigung der Stelle prüfen im Fachg…
5. **verbandsklageregister-vorbereiten** — Verbraucherschutzverband Durchsetzung: Verbandsklageregister vorbereiten. Verbandsklageregister vorbereiten im Fachgebie…
6. **uwg-verbraucherinteressen-pruefen** — Verbraucherschutzverband Durchsetzung: UWG-Verbraucherinteressen prüfen. UWG-Verbraucherinteressen prüfen im Fachgebiet …
7. **verbraucherverband-beweismittel-offenlegung-nutzen-kommunikation** — Verbraucherschutzverband Durchsetzung: Beweismittel-Offenlegung nutzen. Beweismittel-Offenlegung nutzen im Fachgebiet Ve…
8. **datenschutz-im-betroffenenpool** — Verbraucherschutzverband Durchsetzung: Datenschutz im Betroffenenpool. Datenschutz im Betroffenenpool im Fachgebiet Verb…

---

## Skill: `kaltstart-triage`

_Verbraucherschutzverband Durchsetzung: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# Verbraucherschutzverband Durchsetzung - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Verbraucherschutzverband Durchsetzung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Startfragen

1. Wer nutzt das Plugin: Laie, Verband, Kanzlei, Behörde, Unternehmen, Presse, Verwaltung oder Fachabteilung?
2. Welche Entscheidung steht jetzt an und welche Frist läuft?
3. Welche Dokumente liegen vor, welche fehlen und welche Quelle muss live geprüft werden?
4. Welche Behörde, welches Gericht, welches Register oder welcher private Akteur ist betroffen?
5. Soll am Ende ein Antrag, ein Widerspruch, eine Klage-/Eilantragslinie, ein Dashboard, ein Memo oder ein Schreiben entstehen?

## Workflow

1. Sachverhalt in Akte, Normpfad, Zuständigkeit, Frist, Beweis und Ziel zerlegen.
2. Die einschlägige Norm nicht aus dem Gedächtnis final behaupten, sondern als Live-Check gegen amtliche Quelle markieren.
3. Ablehnungs-, Kosten-, Zuständigkeits- und Beweisrisiken offen in einer Ampel führen.
4. Bei Mehr-Ebenen-Recht immer Bund, Land, Kommune, EU/international und Spezialgesetz trennen.
5. Ausgabe mit konkretem nächsten Schritt, offenen Rückfragen und einer kurzen Fassung für Nichtjuristen schließen.

## Verbraucherzentrale-Routing

- Bankgebühren/Zustimmungsfiktion: `vdg-101-bankentgelte-zustimmungsfiktion-serie`.
- Inkasso/Konzerninkasso/Nebenforderungen: `vdg-102-inkasso-konzerninkasso-musterfeststellung`.
- Fehlerhafte Checkout-Buttons: `vdg-103-bestellbutton-uklag-uwg-abmahnung`.
- Probeabo, Kündigungsbutton, automatische Verlängerung: `vdg-104-probeabo-widerruf-verbandsstrategie`.
- SCHUFA, Scoring, Restschuldbefreiung: `vdg-105-schufa-scoring-dsgvo-verbandsfall`.
- Diesel-/Fahrzeug-Serienfälle: `vdg-106-diesel-differenzschaden-serienfall`.

## Typische Ausgaben

- Prüfvermerk mit Normpfad und Live-Check-Liste
- Fristen- und Zuständigkeitsmatrix
- Entwurf für Antrag, Widerspruch, Klagebaustein oder Behördenbrief
- Dashboard-/Tracker-Eintrag mit Status, Risiko und nächster Aktion

## Red Flags

- blindes Zitieren nicht verifizierter Rechtsprechung oder alter Gesetzesstände
- falsche Behörde, falscher Rechtsweg oder unbemerkte Spezialzuständigkeit
- Gebühren-, Frist-, Präklusions-, Geheimschutz-, Datenschutz- oder Drittbetroffenenproblem
- politisch klingende Bewertung ohne saubere Rechtsgrundlage und Beleglogik

## Quellen- und Qualitätsregel

Primär mit amtlichen Gesetzestexten, Behördenhinweisen, Gerichtsentscheidungen mit Datum/Aktenzeichen und frei prüfbaren Quellen arbeiten. Literatur, Datenbanken hinter Paywalls und Fundstellen ohne Nutzerquelle nicht behaupten. Wenn Landesrecht, EU-Recht oder ausländisches Recht berührt ist, den Rechtsstand ausdrücklich live prüfen und die Ausgabe als Arbeitsfassung kennzeichnen.

---

## Skill: `verbraucherverband-abhilfeklage-musterfeststellung-w-uklag`

_Verbraucherschutzverband Durchsetzung: Abhilfeklage oder Musterfeststellung wählen. Abhilfeklage oder Musterfeststellung wählen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Abhilfeklage Oder Musterfeststellung W

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `finanzierung-interessenkonflikte`

_Verbraucherschutzverband Durchsetzung: Finanzierung und Interessenkonflikte. Finanzierung und Interessenkonflikte im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Finanzierung Und Interessenkonflikte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `klageberechtigung-der-stelle-pruefen`

_Verbraucherschutzverband Durchsetzung: Klageberechtigung der Stelle prüfen. Klageberechtigung der Stelle prüfen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Klageberechtigung Der Stelle Pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `verbandsklageregister-vorbereiten`

_Verbraucherschutzverband Durchsetzung: Verbandsklageregister vorbereiten. Verbandsklageregister vorbereiten im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Verbandsklageregister Vorbereiten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `uwg-verbraucherinteressen-pruefen`

_Verbraucherschutzverband Durchsetzung: UWG-Verbraucherinteressen prüfen. UWG-Verbraucherinteressen prüfen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Uwg Verbraucherinteressen Pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `verbraucherverband-beweismittel-offenlegung-nutzen-kommunikation`

_Verbraucherschutzverband Durchsetzung: Beweismittel-Offenlegung nutzen. Beweismittel-Offenlegung nutzen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Beweismittel Offenlegung Nutzen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `datenschutz-im-betroffenenpool`

_Verbraucherschutzverband Durchsetzung: Datenschutz im Betroffenenpool. Datenschutz im Betroffenenpool im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Verbraucherverband-Durchsetzung._

# Datenschutz Im Betroffenenpool

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VDuG; UKlaG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 13 BGB` — Verbraucherbegriff.
- `§ 14 BGB` — Unternehmerbegriff.
- `§ 312c BGB` — Fernabsatzvertrag.
- `§ 312d BGB` — Informationspflichten.
- `§ 355 Abs. 1 BGB` — Widerrufsrecht.
- `§ 357 BGB` — Rechtsfolgen des Widerrufs.
- `§ 434 BGB` — Sachmangel.
- `§ 475 BGB` — Verbrauchsgüterkauf.
- `§ 477 BGB` — Beweislastumkehr.
- `§ 5 UWG` — irrefuehrende geschäftliche Handlung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UKlaG, UWG, VDuG, KapMuG-Schnittstellen
- Qualifizierte Einrichtungen und Verbandsklagebefugnis
- Abmahnung, Unterlassung, Muster, Sammelverfahren
- Verjährungshemmung, Register, Vergleich und Vollstreckung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

