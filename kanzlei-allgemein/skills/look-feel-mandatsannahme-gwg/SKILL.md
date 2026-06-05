---
name: look-feel-mandatsannahme-gwg
description: "Look Feel Mandatsannahme GWG: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Look Feel Mandatsannahme GWG

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Look Feel Mandatsannahme GWG** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-look-and-feel` | Gestaltet Ausgaben des Kanzlei-Allgemein-Plugins hochwertig ruhig und edel. Anwendungsfall Plugin-Output soll innerhalb Cowork-Grenzen professionell aussehen ohne CSS-Abhaengigkeit. Werkzeuge Markdown-Dashboards Statuskarten Freigabeampeln blaeullich-silberne Grundtöne orangener Akzent. Output Formatierungsregelwerk für alle Plugin-Ausgaben mit Ampelfarben Statuskarten und Tabellenstruktur. Abgrenzung zu kanzlei-allgemein-schreibcanvas (Schriftsatzentwurf) und kanzlei-allgemein-qualitaetsgate-hardening. |
| `kanzlei-allgemein-mandatsannahme-gwg` | Führt Mandatsannahme und Geldwäscheprüfung für Kanzleien: Intake, Aktenanlage, Aktenzeichen, Kontoblatt, Konfliktcheck, Kataloggeschäft nach § 2 Abs. 1 Nr. 10 GwG, Identifizierung, Ausweiskopie, Handelsregister, wirtschaftlich Berechtigte, PEP, Hochrisiko, Verdachtsfall, BRAK-Dokumentation, Mandatsvereinbarung, Datenschutz- und KI-Hinweise. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Look Feel Mandatsannahme GWG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-look-and-feel`

**Fokus:** Gestaltet Ausgaben des Kanzlei-Allgemein-Plugins hochwertig ruhig und edel. Anwendungsfall Plugin-Output soll innerhalb Cowork-Grenzen professionell aussehen ohne CSS-Abhaengigkeit. Werkzeuge Markdown-Dashboards Statuskarten Freigabeampeln blaeullich-silberne Grundtöne orangener Akzent. Output Formatierungsregelwerk für alle Plugin-Ausgaben mit Ampelfarben Statuskarten und Tabellenstruktur. Abgrenzung zu kanzlei-allgemein-schreibcanvas (Schriftsatzentwurf) und kanzlei-allgemein-qualitaetsgate-hardening.

# Look and Feel


## Triage zu Beginn
1. Fuer welchen Kanzlei-soll die Ausgabe gestaltet werden: Schriftsatz, Rechnung, Dashboard, Mandantenbrief?
2. Wird die Ausgabe in Claude Cowork oder in einem anderen System angezeigt (Markdown-Grenzen beachten)?
3. Sollen Ampelstatus, Statuskarten oder Tabellenansichten eingesetzt werden?
4. Ist der Empfaenger der Ausgabe ein Anwalt, ein Sekretariat oder ein Mandant?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43 BRAO — Sorgfaltspflicht: umfasst auch klare und verstaendliche Kommunikation
- § 2 BORA — Gewissenhaftigkeit: Kanzlei-Ausgaben muessen korrekt und klar sein
- § 133 BGB — Auslegung: Unklarheiten in Kanzleischreiben gehen zu Lasten des Verfassers
- Art. 5 Abs. 1 DSGVO — Transparenz: Informationen an Mandanten muessen klar und verstaendlich sein

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill sorgt dafür, dass die Kanzlei-Workflows in Claude Cowork nicht wie lose Checklisten wirken, sondern wie ein ruhiges, hochwertiges Kanzlei-Cockpit. Er nutzt nur robuste Markdown-Mittel: klare Abschnitte, kurze Karten, Tabellen, Ampelstatus, Trennlinien und konsistente Benennungen.

## Designprinzipien

- Ruhig vor laut.
- Wenige starke Entscheidungen statt vieler Hinweise.
- Maximal drei nächste Schritte.
- Status immer sichtbar.
- Aktenname, Frist, Risiko und nächste Aktion oben.
- Keine dekorativen Symbole, keine unnötigen Trennzeichen, keine langen Textwände.
- Fachlich präzise, optisch luftig.

## Farb- und Tonwelt

Da Cowork-Markdown keine verlässliche freie CSS-Färbung garantiert, Farben als wiederkehrende Status- und Abschnittsbegriffe führen:

- `Nachtblau`: Kernarbeit, Akte, gerichtliche Arbeit, Kommandocenter.
- `Silber`: neutrale Struktur, Ablage, Register, Protokoll, Zusammenfassung.
- `Orange`: Aufmerksamkeit, Frist, Freigabe, offene Entscheidung.
- `Rot`: Stopper.
- `Grün`: freigegeben oder arbeitsfähig.

Nicht versuchen, HTML/CSS zu erzwingen, wenn Cowork es nicht sicher rendert.

## Standardlayout

Jede zentrale Ausgabe soll so beginnen:

```markdown
# Kanzlei-Allgemein-Plugin

## Kommandocenter

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
| | | | |

## Jetzt

1.
2.
3.
```

Danach erst Details.

## Kartenlogik

Für Kanzlei-Cowork-Ausgaben drei Kartentypen verwenden:

- `Statuskarte`: Akte, Ampel, Frist, Verantwortlicher.
- `Arbeitskarte`: Ziel, nächster Schritt, benötigte Unterlagen.
- `Freigabekarte`: was darf passieren, was darf noch nicht passieren.

## Stilregeln

- Überschriften kurz halten.
- Tabellen nur für Vergleich, Status oder Register nutzen.
- Keine verschachtelten Listen.
- Kein Marketingtext im Arbeitsmodus.
- Keine Scheinpräzision. Unbekanntes als `offen` markieren.
- Bei Risiken klar sein: `Nicht versenden`, `Nicht annehmen`, `Nicht buchen`, `Nicht melden`.

## Übergabe

Dieser Skill ergänzt besonders:

- `kanzlei-allgemein-kommandocenter`
- `kanzlei-allgemein-freundlicher-copilot`
- `kanzlei-allgemein-qualitaetsgate-hardening`
- `kanzlei-allgemein-kanzleitag-simulation`

## Ausgabe

- `assets/templates/cowork-designsystem.md`
- `assets/templates/cowork-dashboard.md`
- `assets/templates/cowork-statuskarte.md`
- `assets/templates/cowork-freigabekarte.md`

## 2. `kanzlei-allgemein-mandatsannahme-gwg`

**Fokus:** Führt Mandatsannahme und Geldwäscheprüfung für Kanzleien: Intake, Aktenanlage, Aktenzeichen, Kontoblatt, Konfliktcheck, Kataloggeschäft nach § 2 Abs. 1 Nr. 10 GwG, Identifizierung, Ausweiskopie, Handelsregister, wirtschaftlich Berechtigte, PEP, Hochrisiko, Verdachtsfall, BRAK-Dokumentation, Mandatsvereinbarung, Datenschutz- und KI-Hinweise.

# Mandatsannahme und Geldwäscheprüfung

## Zweck

Dieser Skill führt eine neue Mandatsanfrage von der ersten Nachricht bis zur strukturierten Mandatsannahme. Er verbindet Aktenanlage, Konfliktcheck, Honorarstart, Kontoblatt, Mandatsvereinbarung, Datenschutz- und KI-Hinweise mit einer dokumentierten GwG-Prüfung nach der BRAK-Systematik.

## Quellen und Stand

Vor produktiver Nutzung die aktuellen BRAK-Hinweise prüfen:

- BRAK Geldwäscheprävention: `https://www.brak.de/anwaltschaft/berufsrecht/geldwaeschepraevention/`
- GwG bei Gesetze im Internet: `https://www.gesetze-im-internet.de/gwg_2017/`
- FIU/goAML: `https://goaml.fiu.bund.de/`

Die BRAK verweist auf Auslegungs- und Anwendungshinweise, Muster-Dokumentationsbögen A bis D und aktuelle Hinweise zu goAML, GwGMeldV und künftigen EU-Vorgaben. Diese Unterlagen sind nicht durch das Plugin zu ersetzen.

## Sicherheitsregeln

- Keine Ausweisdokumente, PINs, Ausweisnummern, Bankzugänge oder Passwörter in öffentlichen Chat, Log oder ungeschützte Markdown-Dateien kopieren.
- Ausweiskopien, Handelsregisterauszüge, Transparenzregisterauszüge, Vollmachten und GwG-Dokumentation in einen geschützten Aktenordner legen.
- Ausweiskopien nur vermerken, nicht unnötig vollständig transkribieren.
- Keine Mandatsannahme behaupten, solange Konfliktcheck, Annahmeentscheidung, Honorar und GwG-Status nicht dokumentiert sind.
- Bei Verdachtsmomenten nicht normal weiterbearbeiten; Berufsträger oder GwG-Verantwortliche einschalten und keine unbedachte Mandanteninformation über Verdachtsprüfungen geben.
- Verdachtsmeldung, goAML, Unstimmigkeitsmeldung oder Mandatsablehnung nie automatisiert auslösen, sondern nur vorbereiten und zur Freigabe vorlegen.

## Geführter Ablauf

1. **Eingang erfassen**: E-Mail, beA, Brief, Messenger, Upload, Telefonnotiz oder persönlicher Besuch.
2. **Lead/Akquise vermerken**: Quelle, Empfehlungsgeber, Erstkontakt, zuständiger Anwalt, gewünschter Stundensatz oder RVG.
3. **Beteiligte erfassen**: Mandant, auftretende Person, wirtschaftlich Berechtigte, Gegner, verbundene Unternehmen, Zahlende, Dritte.
4. **Konfliktcheck vorbereiten**: Namen, Gesellschaften, UBOs, Gegner, frühere Mandate, Rechtsschutz, Versicherer.
5. **GwG-Anwendbarkeit prüfen**: Kataloggeschäft nach § 2 Abs. 1 Nr. 10 GwG oder kein GwG-Mandat.
6. **Aktenzeichen und Kontoblatt anlegen**: eigenes AZ, Debitor, Honorarweg, Vorschuss, Umsatzsteuer, Rechtsschutz, Fremdgeldverbot oder Fremdgeldhinweis.
7. **Identifizierung planen**: natürliche Person, juristische Person, Personengesellschaft, auftretende Person, Fernidentifizierung.
8. **Dokumente ablegen**: Ausweis, Handelsregister, Gesellschafterliste, Vollmacht, Transparenzregister, Strukturdiagramm, Adressnachweis.
9. **Risikobewertung erstellen**: niedrig, normal, erhöht, hoch, unklar.
10. **PEP/Hochrisiko/Sanktionen prüfen**: politisch exponierte Person, Familienangehörige, bekanntermaßen nahestehende Personen, Hochrisikostaat, ungewöhnliche Zahlungswege.
11. **Verdachts- und Ablehnungslogik prüfen**: Verdachtsmoment, Unstimmigkeit, unplausible Mittelherkunft, Strohmannrisiko, Immobilien-/Gesellschaftsbezug.
12. **Mandatsvereinbarung vorbereiten**: Umfang, Honorar, Haftungsbegrenzung, Vorschuss, Vollmacht, Datenschutz, KI-Hinweis, Kommunikationswege.
13. **Freigabeentscheidung protokollieren**: annehmen, nur nach Nachreichung, nur mit verstärkten Sorgfaltspflichten, ablehnen, Verdachtsprüfung.
14. **Reminder setzen**: fehlende Dokumente, Aktualisierung, Vorschuss, Unterschrift, Identitätsprüfung, periodische GwG-Review.

## GwG-Anwendbarkeit

Bei Rechtsanwältinnen und Rechtsanwälten ist besonders zu prüfen, ob ein Kataloggeschäft nach § 2 Abs. 1 Nr. 10 GwG vorliegt, etwa:

- Kauf oder Verkauf von Immobilien oder Gewerbebetrieben.
- Verwaltung von Geld, Wertpapieren oder sonstigen Vermögenswerten.
- Eröffnung oder Verwaltung von Bank-, Spar- oder Wertpapierkonten.
- Beschaffung von Mitteln zur Gründung, zum Betrieb oder zur Verwaltung von Gesellschaften.
- Gründung, Betrieb oder Verwaltung von Gesellschaften, Trusts oder ähnlichen Strukturen.
- Handeln im Namen und auf Rechnung des Mandanten bei Finanz- oder Immobilientransaktionen.
- Steuer-, Gesellschafts-, Immobilien-, M&A-, Treuhand- oder Strukturierungsmandat mit Transaktionsbezug.

Wenn kein Kataloggeschäft vorliegt, trotzdem Konfliktcheck, Identitätsplausibilität, Datenschutz und Honorar sauber dokumentieren.

## Identifizierung

### Natürliche Person

- Name, Geburtsdatum, Geburtsort, Staatsangehörigkeit, Anschrift.
- Art, Nummer, ausstellende Behörde und Gültigkeit des Ausweises nur soweit erforderlich dokumentieren.
- Anwesend oder abwesend prüfen.
- Auftreten auf eigene oder fremde Rechnung fragen.

### Juristische Person oder Personengesellschaft

- Firma, Rechtsform, Registernummer, Registergericht, Sitz, Geschäftsanschrift.
- Vertretungsberechtigte Personen.
- wirtschaftlich Berechtigte, Beteiligungsstruktur, Kontrollrechte.
- Handelsregister und bei Bedarf Transparenzregister/Strukturunterlagen.
- Auftretende Person und Vertretungsmacht prüfen.

## Risikofaktoren

Erhöhte Aufmerksamkeit bei:

- PEP, Familienangehörigen oder nahestehenden Personen.
- Hochrisikoländern oder unklarer Herkunft der Mittel.
- Immobilien, Gesellschaftsgründung, Treuhand, komplexer Beteiligungsstruktur.
- ungewöhnlichem Zeitdruck, Barzahlungen, Drittzahlungen oder Fremdgeldwunsch.
- nicht nachvollziehbarem wirtschaftlichem Zweck.
- fehlenden oder widersprüchlichen Dokumenten.
- Mandant will keine Identifizierung, keinen wirtschaftlich Berechtigten oder keine Mittelherkunft nennen.

## Ausgabe

- `assets/templates/mandatsannahme-gwg-start.md`
- `assets/templates/gwg-anwendbarkeit-kataloggeschaeft.md`
- `assets/templates/gwg-identifizierung-und-dokumente.md`
- `assets/templates/gwg-risikobewertung-mandat.md`
- `assets/templates/gwg-pep-sanktionen-transparenzregister.md`
- `assets/templates/gwg-verdachtsfall-entscheidungsvermerk.md`
- `assets/templates/mandatskontoblatt.md`
- `assets/templates/mandatsvereinbarung-ki-datenschutz-hinweis.md`

Danach an `kanzlei-allgemein-akte`, `kanzlei-allgemein-aktenzeichen`, `kanzlei-allgemein-mandatsvereinbarung`, `kanzlei-allgemein-fristen-monitor`, `kanzlei-allgemein-rechnung` und bei Unternehmensmandanten an `kanzlei-allgemein-handelsregisterabruf` übergeben.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
