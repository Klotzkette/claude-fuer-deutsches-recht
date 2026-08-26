---
name: workflow-chronologie-und-belegmatrix
description: "Für Workflow: Chronologie und Belegmatrix: ordnet Akte, Belege und Lücken; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
---

# Workflow: Chronologie und Belegmatrix

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Chronologie-Aufbau

### Schritt 1 – Zeitachse anlegen

Folgende Ereignisse chronologisch erfassen:

| Datum | Ereignis | Beteiligte | Beleg | Status |
|---|---|---|---|---|
| [Datum] | Schutzrecht angemeldet | Mandant | Registerauszug | Gesichert |
| [Datum] | Schutzrecht eingetragen | DPMA/EUIPO | Urkunde | Gesichert |
| [Datum] | Verletzungshandlung erstmals | Verletzer | Screenshot | Gesichert |
| [Datum] | Erstkenntnis Mandant | Mandant | Eidesstattliche Versicherung | Glaubhaft |
| [Datum] | Abmahnung versandt | Mandant | Abmahnschreiben | Gesichert |
| [Datum] | Reaktion Gegenseite | Gegenseite | Antwortschreiben | Gesichert |
| [Datum] | EV beantragt | Mandant | Antragsschrift | Gesichert |
| [Datum] | EV erlassen | Gericht | EV-Beschluss | Gesichert |
| [Datum] | EV vollzogen | GV | Zustellurkunde | Gesichert |
| [Datum] | Verstoß gegen EV | Verletzer | Screenshot | Zu belegen |

### Schritt 2 – Lücken identifizieren

**Lückenkategorien:**

1. **Beleg fehlt ganz:** Ereignis ist beschrieben, aber kein Beweismittel vorhanden.
 → Mandant befragen; nachbeschaffen; eidesstattliche Versicherung?

2. **Beleg unvollständig:** Screenshot ohne Datum; Kaufbeleg ohne Produktangabe.
 → Beleg ergänzen; Screenshot mit Timestamp wiederholen.

3. **Zeitachse unklar:** Mandant weiß nicht genau, wann Erstkenntnis war.
 → Erinnerungsprotokoll; E-Mail-Suche; Browserverlauf.

4. **Beweiskette unterbrochen:** Zwischen Verletzungshandlung und Schaden fehlen Verbindungsglieder.
 → Sachverständigengutachten? Zusätzliche Zeugen?

### Schritt 3 – Belegmatrix erstellen

```
BELEGMATRIX
Mandat: [Mandant ./. Gegenseite]

Spalten: Ereignis | Datum | Beleg | Beweismittelart | Beweiswert | Status
Zeilen: Je ein Ereignis

Legende Status:
G = Gesichert (Beleg vorhanden und geprüft)
P = Plausibel (Ereignis plausibel, Beleg fehlt noch)
L = Lücke (Ereignis unbekannt oder unbelegt)
```

| # | Ereignis | Datum | Beleg | Beweismittelart | Beweiswert | Status |
|---|---|---|---|---|---|---|
| 1 | Schutzrecht eingetragen | _______ | Registerauszug | Urkunde | Hoch | G |
| 2 | Verletzungshandlung | _______ | Screenshot + URL | Augenschein | Mittel | G |
| 3 | Erstkenntnis Mandant | _______ | EV-Antrag Datum | Eidesstattliche Vers. | Mittel | P |
| 4 | Abmahnung zugestellt | _______ | Einschreiben-Rückschein | Urkunde | Hoch | G |
| 5 | EV erlassen | _______ | Beschluss | Urkunde | Hoch | G |
| 6 | EV vollzogen | _______ | Zustellurkunde | Urkunde | Hoch | G |
| 7 | Verstoß gegen EV | _______ | Screenshot nach EV | Augenschein | Mittel | L |

## Besondere Chronologie-Fragen im IP-Recht

### Dringlichkeitszeitachse (EV)

- Wann wurde Verletzung erstmals bekannt (Erstkenntnis)?
- Wie lange zwischen Erstkenntnis und EV-Antrag?
- War Zeitverzögerung begründet (Beweissammlung, Abmahnfrist)?
- Kritische Schwelle: Je nach Gericht 4–8 Wochen.

### Prioritätszeitachse (Marke)

- Wann wurde Voranmeldung eingereicht (Prioritätsdatum)?
- Wann wurde Marke veröffentlicht?
- Wann war Widerspruchsfrist?
- Wann eingetragen?

### Verletzungszeitraum (Schadensersatz)

- Wann begann die Verletzung?
- Wann endete sie (oder endet sie noch)?
- Wie häufig und in welchem Umfang?
- Diese Daten bestimmen die Höhe des Schadensersatzes.

## Lücken-Schließ-Strategie

| Lückentyp | Methode |
|---|---|
| Erstkenntnis unklar | E-Mail-Postfach durchsuchen; Browserverlauf; Zeuge |
| Verletzungsnachweis fehlt | Testkauf; erneuter Screenshot; Wayback Machine |
| Datum der Verletzungshandlung | Domain-Registrierungsdaten; Wayback Machine; Archiv |
| Schaden nicht bezifferbar | Sachverständiger; Lizenzanalogie-Recherche |
| Schutzrecht-Gültigkeit | Live-Abfrage DPMA/EUIPO; Jahresgebühren-Check |

## Output-Format Chronologie

**Kurz-Chronologie für EV-Antrag:**
```
[Datum] – Marke X eingetragen beim DPMA (Anlage 1)
[Datum] – Erstkenntnis der Verletzung durch Y (eidesstattliche Versicherung, Anlage 2)
[Datum] – Screenshot der Verletzungshandlung auf website.de (Anlage 3)
[Datum] – Abmahnung Y versandt (Anlage 4)
[Datum] – Y hat nicht reagiert / hat Abmahnung abgelehnt
[Datum] – EV-Antrag beim LG [Stadt]
```

**Detail-Belegmatrix:** Vollständige Tabelle für interne Akte und Qualitätsprüfung.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Anschluss-Skills

- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand und Belegaufbau
- `workflow-dokumentenintake` – Dokumentenerfassung
- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag
- `spezial-klausel-beweislast-und-darlegungslast` – Beweislastverteilung
