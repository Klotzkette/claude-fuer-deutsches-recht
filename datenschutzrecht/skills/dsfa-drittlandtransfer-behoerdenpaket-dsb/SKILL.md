---
name: dsfa-drittlandtransfer-behoerdenpaket-dsb
description: "Dsfa Drittlandtransfer Behördenpaket DSB im Datenschutzrecht: prüft konkret Behördenfähiges Dokumentations- und Antwortpaket für, Bestellungspflicht für Datenschutzbeauftragten prüfen, Pruefung wann eine DSFA nach Art, Abgleich einer Verarbeitung mit der BfDI-Pflichtliste nach. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Dsfa Drittlandtransfer Behördenpaket DSB

## Arbeitsbereich

**Dsfa Drittlandtransfer Behördenpaket DSB** ordnet den Fall über die tragenden Prüfungslinien: Behördenfähiges Dokumentations- und Antwortpaket für, Bestellungspflicht für Datenschutzbeauftragten prüfen, Pruefung wann eine DSFA nach Art. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `drittlandtransfer-behoerdenpaket-output` | Behördenfähiges Dokumentations- und Antwortpaket für Drittlandtransfers erstellen: Deckvermerk, Transferregister, DPF/SCC/TIA-Nachweise, TOMs, Subprozessoren, Maßnahmenplan und Antwort an deutsche Datenschutzaufsicht. |
| `dsb-bestellungspflicht-pruefung` | Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung. Output: Bestellungsprüfmemo Empfehlung. Abgrenzung: nicht für Aufgaben des DSB (Art. 39 DSGVO). |
| `dsfa-art-35-dsgvo-trigger-und-anwendungsbereich` | Pruefung wann eine DSFA nach Art. 35 DSGVO ueberhaupt erforderlich ist. Trigger-Pruefung Anwendungsbereich Schwellwert. Generalklausel Art. 35 Abs. 1 voraussichtlich hohes Risiko; Regelbeispiele Art. 35 Abs. 3; Pflichtlisten Art. 35 Abs. 4 BfDI. Output: Triage-Vermerk DSFA-pflichtig oder nicht. |
| `dsfa-bfdi-und-laender-blacklist` | Abgleich einer Verarbeitung mit der BfDI-Pflichtliste nach Art. 35 Abs. 4 DSGVO und mit den Listen der Landesdatenschutzbehoerden. Output: dokumentierter Listenabgleich mit Trefferanalyse und ggf. Verweis auf zwingende DSFA. |
| `dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii` | Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO: Aktenstruktur Versionierung Aufbewahrung Beweiswert. Output: DSFA-Akte mit Aktenuebersicht und Aufbewahrungsregeln. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `drittlandtransfer-behoerdenpaket-output`

**Fokus:** Behördenfähiges Dokumentations- und Antwortpaket für Drittlandtransfers erstellen: Deckvermerk, Transferregister, DPF/SCC/TIA-Nachweise, TOMs, Subprozessoren, Maßnahmenplan und Antwort an deutsche Datenschutzaufsicht.

### Drittlandtransfer-Behördenpaket-Output

## Zweck

Dieser Skill erstellt aus vorhandenen Prüfungen ein geordnetes Paket für Datenschutzaufsichtsbehörden, interne Audits, DSB-Berichte oder Geschäftsführungsfreigaben. Er sammelt nicht nur Dokumente, sondern macht sichtbar, warum der Transfer erlaubt, eingeschränkt erlaubt oder vorläufig gestoppt ist.

## Startsignal

Dieses Fachmodul, wenn der Nutzer sagt:

- "Die Aufsichtsbehörde fragt nach dem US-Transfer."
- "Wir brauchen ein Paket, das wir vorlegen können."
- "Bitte druckreif dokumentieren."
- "Zeig, dass DPF/SCC/TIA geprüft wurden."
- "Wir müssen nachweisen, dass ein Anbieter gelistet oder nicht gelistet ist."

## Eingangslogik

1. Liegt bereits ein TIA vor? Wenn nein, `us-transfer-tia-dokumentation` vorschlagen und den fehlenden Kern extrahieren.
2. Liegen SCC vor? Wenn unklar, `standardvertragsklauseln-scc-paket` vorschlagen.
3. Liegt ein DPF-Nachweis vor? Wenn nein, Abruf/Prüfung als `nicht verifiziert` markieren und Nachholung als Sofortmaßnahme setzen.
4. Ist die Behördenfrist bekannt? Wenn ja, Ausgabe nach Frist priorisieren.

## Paketstruktur

### 1. Deckvermerk

Erstelle einen klaren Vermerk:

- Aktenzeichen/Behördenbezug.
- Verantwortliche Stelle und Datenschutzkontakt.
- Betroffener Dienst/Transfer.
- Kurzentscheidung: DPF / SCC + TIA / BCR / Art. 49 / Stop.
- Standdatum.
- Liste der beigefügten Nachweise.
- Offene Punkte und Nachreichungsangebot.

### 2. Entscheidungsmatrix

| Frage | Ergebnis | Nachweis | Risiko | Maßnahme |
|---|---|---|---|---|
| Gibt es einen Drittlandtransfer? | Ja/Nein | Transferregister | ... | ... |
| Ist ein Angemessenheitsbeschluss einschlägig? | Ja/Nein/Teilweise | DPF-Check | ... | ... |
| Sind SCC/BCR erforderlich? | Ja/Nein | Vertrag/Annex | ... | ... |
| Liegt ein TIA vor? | Ja/Nein | TIA-Vermerk | ... | ... |
| Sind Subprozessoren prüfbar? | Ja/Nein | Subprozessorliste | ... | ... |
| Sind ergänzende Maßnahmen ausreichend? | Ja/Nein/Offen | TOM-Matrix | ... | ... |

### 3. Anlagenverzeichnis

Nummeriere die Anlagen:

1. Transferregister-Auszug.
2. DPF-Prüfvermerk mit Abrufdatum.
3. AVV/DPA.
4. SCC mit Modul- und Annex-I-III-Übersicht.
5. TIA-Vermerk.
6. TOM-/Security-Anlage.
7. Subprozessoren-Archiv.
8. Datenschutzhinweis-/VVT-Auszug.
9. Managemententscheidung.
10. Review-Kalender und Maßnahmenplan.

### 4. Behördenantwort

Formuliere neutral, präzise und ohne Überbehauptung:

- Was geprüft wurde.
- Welche Rechtsgrundlage aktuell herangezogen wird.
- Warum Safe Harbor/Privacy Shield nicht als aktuelle Grundlage genutzt werden.
- Ob DPF trägt und für welchen Scope.
- Falls DPF nicht trägt: welche SCC/BCR/TIA-Maßnahmen greifen.
- Welche Lücken erkannt und bis wann geschlossen werden.

**Keine falsche Sicherheit:** Wenn ein Nachweis fehlt, schreibe nicht "liegt vor", sondern "wird bis [Datum] nachgereicht" oder "ist beim Anbieter angefordert".

## Drei Standardszenarien

### A. US-Anbieter aktiv DPF-gelistet

Output-Schwerpunkt:

- DPF-Check als Hauptnachweis.
- Scope-Abgleich.
- Transferregister und AVV.
- TOMs und Subprozessoren als Kontrollnachweise.
- Review alle 6 bis 12 Monate und bei Zertifizierungsablauf.

### B. US-Anbieter nicht oder nicht passend DPF-gelistet

Output-Schwerpunkt:

- SCC-Modulwahl.
- TIA mit Drittlandsrecht/Praxis und Zusatzmaßnahmen.
- Subprozessoren.
- Entscheidung "Freigabe mit Auflagen" oder "Stop".
- Keine Berufung auf DPF für diesen Transfer.

### C. Altfall Safe Harbor/Privacy Shield

Output-Schwerpunkt:

- Historische Grundlage ausdrücklich als überholt markieren.
- Zeitraum und Datenflüsse abgrenzen.
- Aktuelle Ersatzgrundlage festlegen.
- Nachbereinigung von Datenschutzhinweisen, AVV, VVT und Einkaufsakten.

## Druckreifes Ausgabeformat

Wenn der Nutzer "ausdrucken", "vorlegen", "Behörde" oder "Aktenvermerk" sagt, liefere:

1. **Einseitige Executive Summary**.
2. **Vollvermerk** mit Tabellen.
3. **Anlagenliste**.
4. **Antwortschreiben**.
5. **Offene-Punkte-Liste** mit Eigentümer und Datum.

## Qualitätsgate vor Abschluss

- Stimmen Rechtsträgernamen überall überein?
- Ist der genaue Transfer benannt, nicht nur der Anbieter?
- Sind DPF/SCC/TIA logisch konsistent?
- Gibt es keine Behauptung "Shield gültig"?
- Sind Dokumentstände datiert?
- Sind offene Punkte sichtbar statt versteckt?
- Ist die nächste Wiedervorlage gesetzt?

## Quellen und Aktualität

- Stand: 05/2026.
- DSGVO Art. 5 Abs. 2, Art. 24, Art. 28, Art. 30, Art. 44-49.
- EU-US Data Privacy Framework-Angemessenheitsbeschluss vom 10.07.2023.
- Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914.
- EDSA Recommendations 01/2020.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `dsb-bestellungspflicht-pruefung`

**Fokus:** Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung. Output: Bestellungsprüfmemo Empfehlung. Abgrenzung: nicht für Aufgaben des DSB (Art. 39 DSGVO).

### DSB-Bestellungspflicht und -Anforderungen

## Zweck

Häufige Lücke in Unternehmen: Pflicht zur DSB-Bestellung wird nicht erkannt. Dieses Skill prüft Pflicht, Anforderungen an DSB und löst Folge-Probleme (Interessens-Konflikt, externe vs. interne Bestellung).

## Eingaben

- Unternehmens-Typ (öffentlich privat)
- Beschäftigten-Zahl
- Verarbeitungs-Tätigkeiten (Übersicht aus VVT)
- Bestand DSB ja/nein
- Bei Bestand: Person und Rolle (intern extern)

## Schritt 1 — Pflicht-Tatbestände Art. 37 DSGVO

### Lit. a) Öffentliche Stelle / Behörde

- **Pflicht** unabhängig von Größe
- Außer Gerichte in Justizfunktion

### Lit. b) Kerntätigkeit umfangreiche regelmäßige systematische Überwachung

- **Kerntätigkeit** das Geschäft selbst (nicht nur Mittel zur Geschäftsführung)
- **Umfangreich** Skalierung
- **Regelmäßig systematisch** Dauerhaft strukturiert
- **Überwachung** Beobachtung Verhalten Profilbildung

#### Beispiele

- Online-Verhaltens-Tracking Werbe-Netzwerke
- Vermarkter mit Profiling
- Telematik-Versicherer
- Standort-Verfolgung
- CCTV im großen Stil

### Lit. c) Kerntätigkeit umfangreiche Verarbeitung besondere Kategorien

- **Art. 9 DSGVO** Daten (Gesundheit Religion Sexual-Orientierung etc.)
- **Strafrechtliche Daten** Art. 10
- **Umfangreich**

#### Beispiele

- Krankenhäuser
- Religions-Gemeinschaften
- Personalvermittler mit Diversity-Daten
- Strafvollzug-Dienstleister
- Genetik-/Genom-Labore

## Schritt 2 — § 38 BDSG Deutsche Erweiterung

### Schwellenwert

- **In der Regel mindestens 20 Personen**
- **Ständig mit automatisierter Verarbeitung beschäftigt**
- Bei Pflicht zur DSFA (Art. 35) auch bei weniger Personen
- Bei geschäftsmäßiger Verarbeitung zum Zweck der Übermittlung anonymen Übermittlung Markt- oder Meinungsforschung

### "Personen" im Sinne § 38 BDSG

- Mitgezählt werden **eigene Beschäftigte** des Verantwortlichen (Voll- und Teilzeit, Aushilfen, Auszubildende, Werkstudenten, freie Mitarbeiter mit Datenzugriff)
- **Auftragsverarbeiter-Personal zählt NICHT mit** — dieses gehört zum Auftragsverarbeiter, der selbst die DSB-Pflicht prüft
- Entscheidend ist die Ständigkeit der automatisierten Verarbeitung, nicht das Beschäftigungs-Volumen

### Kombination

- EU-DSGVO und § 38 BDSG nebeneinander
- Strengstes Kriterium gilt

## Schritt 3 — Anforderungen DSB Art. 37 Abs. 5 6 DSGVO

### Fachliche Eignung

- **Berufliche Qualifikation** Datenschutz
- **Fachwissen** DSGVO BDSG
- **Spezialwissen** der Branche
- Zertifizierungen: TÜV, GDD, DIA, BvD u.a.

### Persönliche Eignung

- Zuverlässigkeit
- Vertrauenswürdig
- Bei Insolvenz / Strafverfahren prüfen

## Schritt 4 — Stellung DSB Art. 38 DSGVO

### Unabhängigkeit

- **Keine Weisungs-Bindung** in Datenschutz-Fragen
- **Berichts-Linie** an oberste Leitung
- **Schutz vor Abberufung** wegen Aufgaben-Wahrnehmung

### Ressourcen-Pflicht

- **Zeitliche Verfügbarkeit** ausreichend
- **Sachliche Ausstattung** Büro IT Reisekosten
- **Fortbildungs-Budget**
- **Externe Hilfe** wenn nötig

### Schutz vor Kündigung / Abberufung

- **§ 6 Abs. 4 BDSG** Kündigungs-Schutz analog § 4f
- Bei Beendigungs-Schutz auch nach Amtszeit
- Außerordentliche Kündigung nur bei wichtigem Grund

### Schweigepflicht

- DSB unterliegt Schweige-Pflicht
- Auch nach Beendigung

## Schritt 5 — Interne vs. externe Bestellung

### Interner DSB

- **Aus Belegschaft**
- **Voll- oder Teilzeit-DSB-Aufgabe**
- **Vorteil:** Insider-Kenntnis
- **Nachteil:** Interessens-Konflikt-Risiko

### Externer DSB

- **Beratung durch externe Firma / Anwalts-Kanzlei**
- **Vertragliche Bestellung**
- **Vorteil:** Unabhängigkeit Spezialisierung
- **Nachteil:** Externe Person ohne Insider-Kenntnis

### Konzern-DSB

- Ein DSB für mehrere Konzern-Gesellschaften
- Erlaubt § 38 Abs. 1 BDSG ("für mehrere Stellen")
- Konzern-Bestellungs-Akte
- Kommunikations-Linie zu allen Gesellschaften

## Schritt 6 — Interessens-Konflikt-Prüfung

### Problematische Doppelrollen

#### Geschäftsführer / Vorstand

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- ErwGr 97 DSGVO zur Unabhängigkeits-Anforderung
- Strikte Trennung erforderlich

#### IT-Leitung

- Verarbeitung verantwortlich + Datenschutz kontrollierend
- Konflikt häufig
- Strikt: Trennung erforderlich

#### Personalleitung

- Personal-Verarbeitung steuernd + Datenschutz kontrollierend
- Konflikt häufig

#### Compliance-Officer

- Bei klar getrennten Bereichen möglich
- Bei umfassender Compliance-Verantwortung Konflikt

### Unproblematische Rollen

- IT-Sicherheits-Beauftragter (komplementär)
- Externer Anwalt (unabhängig)
- Externe Beratung (klar)

### Bei Konflikt

- **Auswechslung** des DSB
- **Externe Bestellung**
- **Strukturelle Anpassung** der internen Rollen

## Schritt 7 — Aufgaben DSB Art. 39 DSGVO

### Pflicht-Aufgaben

a) **Information und Beratung** Verantwortlicher und Beschäftigte

b) **Überwachung** Einhaltung DSGVO und Datenschutz-Vorschriften

c) **Beratung** zu DSFA und deren Überwachung

d) **Zusammenarbeit** Aufsichtsbehörde

e) **Anlaufstelle Aufsichtsbehörde** für Fragen Beratung

### Zusätzlich

- Mit-wirkung VVT
- Beratung bei AVV-Erstellung
- Schulung Mitarbeiter
- Datenpanne-Bewertung

## Schritt 8 — Meldung Aufsichtsbehörde Art. 37 Abs. 7 DSGVO

### Pflicht zur Veröffentlichung

- Kontakt-Daten DSB
- Mitteilung an Aufsichtsbehörde
- Online-Meldung möglich

### Form

- Schriftlich elektronisch
- Aufsichtsbehörde wo Verantwortlicher Hauptniederlassung
- Inhalt: Name Anschrift Telefon E-Mail

### Bei Änderungen

- Update bei Wechsel DSB
- Bei Wechsel der Aufsichtsbehörden-Zuständigkeit

## Schritt 9 — Bestellungs-Akt

### Form

- **Schriftlich** empfohlen
- **Stellenbeschreibung** mit Aufgaben Rechten
- **Vertrag** bei externem DSB
- **Bestellungs-Urkunde** intern

### Inhalt

- Bestellungs-Datum
- Aufgaben gemäß Art. 39 DSGVO
- Ressourcen-Zusage
- Berichts-Linie
- Vertraulichkeits-Pflicht
- Beendigungs-Regelung

## Schritt 10 — Bei Verstoß

### Sanktionen

- **Art. 83 Abs. 4 DSGVO** bis 10 Mio EUR oder 2 Prozent Konzernumsatz
- **Aufsichts-Anordnung** zur Bestellung
- **Reputations-Schaden**

### Folge-Probleme

- Datenpannen ohne DSB schwerer beherrschbar
- DSFA-Lücken
- Aufsichts-Behörden-Audit kritisch

## Schritt 11 — Beratungs-Schritte

### Erstprüfung

1. **Beschäftigten-Zahl** über 20 mit automatisierter Verarbeitung?
2. **Verarbeitungs-Typ** Kerntätigkeit mit Überwachung oder besonderen Kategorien?
3. **Öffentliche Stelle**?
4. **Bei Bejahung**: DSB-Pflicht — sofort Bestellung erforderlich

### Wenn DSB vorhanden

1. **Eignungs-Prüfung** Qualifikation aktuell?
2. **Stellung** Unabhängigkeit gewährleistet?
3. **Interessens-Konflikt** vorhanden?
4. **Ressourcen** ausreichend?
5. **Meldung** Aufsichtsbehörde erfolgt?

### Wenn DSB-Lücke

1. **Sofortige Bestellung** intern oder extern
2. **Aufsichtsbehörde** informieren
3. **VVT-Eintrag** DSB-Daten
4. **Datenschutz-Hinweise** Webseite aktualisieren

## Schritt 12 — Außerhalb Pflicht — freiwillige Bestellung

### Vorteile

- **Compliance-Sicherheit**
- **Vorbereitung** Wachstum
- **Audit-Vorbereitung**
- **Mandanten-Vertrauen**

### Empfehlung

- Bei jeder Verarbeitung besonderer Kategorien (auch wenn nicht "umfangreich")
- Bei Cookie-Tracking selbst bei kleiner Webseite
- Bei jeder grenz-überschreitenden Verarbeitung

## Verzahnung mit anderen Skills

- `verarbeitungsverzeichnis-vvt-generator` — VVT mit DSB-Bezeichnung
- `dsfa-erstellung` — DSB-Beratung
- `avv-pruefung` — DSB-Beratung
- `datenpanne-meldung` — DSB-Eskalation
- `mandantendaten-ki` — DSB im Kanzlei-Kontext
- `anwendungsfall-triage` — Eingangsprüfung

## Ausgabe

- `dsb-pruefung-{unternehmen}.md` mit Pflicht-Analyse Anforderungs-Prüfung Konflikt-Bewertung
- Bei DSB-Lücke: Bestellungs-Pflicht-Bestätigung + Bestellungs-Vorbereitung
- Bei externem DSB: Vertrags-Entwurf
- Bei internem DSB: Stellenbeschreibung
- Aufsichts-Behörden-Meldung-Vorbereitung
- Frist im Fristenbuch (Bestellung unverzüglich)

## Quellen

- DSGVO Art. 37 38 39 83; ErwGr 97 DSGVO
- BDSG §§ 5 6 38
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BfDI Praxis-Empfehlungen
- DSK Kurzpapier
- GDD und BvD Standards

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Öffentliche oder private Stelle? (Art. 37 Abs. 1 lit. a DSGVO vs. § 38 BDSG)
2. Bei privater Stelle: Anzahl Personen, die ständig mit automatisierter Verarbeitung beschäftigt sind (§ 38 Abs. 1 BDSG: ab 20)?
3. Verarbeitung besonderer Kategorien (Art. 9 DSGVO) oder umfangreiche Überwachung?
4. Bestehender DSB: Interessenkonflikt (leitende Verarbeitungsverantwortung)?

## Output-Template — DSB-Prüfvermerk

**Adressat:** Geschäftsführung / Compliance — Tonfall: sachlich-juristisch

```
DSB-Bestellungspflicht-Prüfvermerk [DATUM]
Organisation: [NAME]

Bestellungspflicht-Prüfung:
Öffentliche Stelle (Art. 37 Abs. 1 lit. a DSGVO): ja / nein
Kerntätigkeit umfangreiche Überwachung (Art. 37 Abs. 1 lit. b): ja / nein
Besondere Kategorien umfangreich (Art. 37 Abs. 1 lit. c): ja / nein
§ 38 BDSG: [X] Personen staendig automatisiert → ab 20: Pflicht

Ergebnis Bestellungspflicht: JA / NEIN

Aktueller DSB (falls bestellt):
Name: [NAME] | intern / extern
Interessenkonflikt-Check: kein Konflikt / Konflikt (Grund: [...])
Qualifikation ausreichend: ja / nein / unklar

Empfehlung: DSB bestellen (bis [FRIST]) / DSB wechseln / kein Handlungsbedarf
```

## 3. `dsfa-art-35-dsgvo-trigger-und-anwendungsbereich`

**Fokus:** Pruefung wann eine DSFA nach Art. 35 DSGVO ueberhaupt erforderlich ist. Trigger-Pruefung Anwendungsbereich Schwellwert. Generalklausel Art. 35 Abs. 1 voraussichtlich hohes Risiko; Regelbeispiele Art. 35 Abs. 3; Pflichtlisten Art. 35 Abs. 4 BfDI. Output: Triage-Vermerk DSFA-pflichtig oder nicht.

### DSFA Trigger und Anwendungsbereich nach Art. 35 DSGVO

## Zweck

Dieser Skill liefert eine strukturierte Erstpruefung der Frage, ob für eine konkrete Verarbeitungstaetigkeit eine Datenschutz-Folgenabschaetzung (DSFA) nach Art. 35 DSGVO durchzufuehren ist. Ergebnis ist ein Triage-Vermerk mit klarer Aussage DSFA-pflichtig, optional oder entbehrlich und einer Begruendung mit Norm-Anker.

## Wann dieses Modul hilft

- Vor Einfuehrung einer neuen Verarbeitungstaetigkeit
- Bei wesentlicher Aenderung einer bestehenden Verarbeitung (Art. 35 Abs. 11 DSGVO)
- Bei Aufnahme eines neuen Auftragsverarbeiters, neuer Technologie oder neuer Datenkategorie
- Wenn die interne Compliance, der DSB oder eine Aufsichtsbehoerde die Frage stellt
- Vor Erstellung einer vollstaendigen DSFA (Vorab-Triage)

## Rechtlicher Rahmen

- Art. 35 Abs. 1 DSGVO Generalklausel: DSFA verpflichtend wenn eine Form der Verarbeitung, insbesondere bei Verwendung neuer Technologien, aufgrund Art, Umfang, Umstaenden und Zwecken voraussichtlich ein hohes Risiko für die Rechte und Freiheiten natuerlicher Personen zur Folge hat.
- Art. 35 Abs. 3 DSGVO Regelbeispiele:
 - lit. a systematische und umfassende Bewertung persönlicher Aspekte einschliesslich Profiling und darauf gestuetzter automatisierter Entscheidung mit Rechtswirkung
 - lit. b umfangreiche Verarbeitung besonderer Kategorien nach Art. 9 Abs. 1 oder von Daten ueber strafrechtliche Verurteilungen nach Art. 10
 - lit. c systematische umfangreiche Ueberwachung oeffentlich zugaenglicher Bereiche
- Art. 35 Abs. 4 DSGVO Pflichtliste der Aufsichtsbehoerde (BfDI bzw. zuständige Landesbehoerde) — sogenannte Blacklist.
- Art. 35 Abs. 5 DSGVO optionale Whitelist der Aufsichtsbehoerde.
- Art. 35 Abs. 10 DSGVO Ausnahme bei gesetzlicher Grundlage mit bereits durchgefuehrter allgemeiner DSFA durch den Gesetzgeber.
- EDSA-Leitlinien WP 248 rev.01 (uebernommen durch EDSA), insbesondere die 9 Kriterien zur Bestimmung von voraussichtlich hohem Risiko.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Kurzbeschreibung der Verarbeitung in maximal 10 Saetzen: Zweck, Datenarten, Betroffenenkreise, Technologie, Drittlandbezug, Aufbewahrung. Ohne diese Beschreibung ist die Trigger-Pruefung nicht moeglich.
2. **Verhaeltnismaessigkeitspruefung.** In dieser Stufe nur grobe Plausibilitaet: Liegt ein offensichtliches Missverhaeltnis von Zweck und Eingriff vor? Falls ja, ist die DSFA bereits aus diesem Grund angezeigt.
3. **Risikoanalyse Trigger-Ebene.** Pruefen der 9 EDSA-Kriterien:
 - Bewertung oder Scoring
 - automatisierte Entscheidung mit Rechtswirkung
 - systematische Ueberwachung
 - besondere Kategorien Art. 9 oder Art. 10
 - umfangreiche Verarbeitung
 - Zusammenfuehrung oder Abgleich von Datensaetzen
 - schutzbeduerftige Personen (Kinder, Patienten, Beschaeftigte)
 - neue Technologien (KI, Biometrie, IoT)
 - Verhinderung der Ausübung von Betroffenenrechten
4. **Massnahmen.** Pruefen ob bereits getroffene risikomindernde Massnahmen den Schwellwert unter hohes Risiko druecken (Pseudonymisierung, Anonymisierung, technische Beschraenkung). Ergebnis dokumentieren.
5. **Restrisiko / Schwellwertergebnis.** Drei moegliche Ergebnisse:
 - DSFA-PFLICHTIG (Art. 35 Abs. 3, Abs. 4 oder mindestens 2 EDSA-Kriterien)
 - DSFA-EMPFOHLEN (1 EDSA-Kriterium, Grenzfall)
 - DSFA-ENTBEHRLICH (kein Kriterium erfuellt, Blacklist nicht einschlaegig)
6. **Konsultation / Genehmigung.** DSB nach Art. 35 Abs. 2 DSGVO anhoeren. Triage-Vermerk gegenzeichnen lassen und in Verarbeitungsverzeichnis nach Art. 30 verlinken.

## Mustertext / Template

```
DSFA-TRIAGE-VERMERK [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME, ROLLE]
Vorpruefer: [NAME] | DSB-Anhörung: [DATUM]

1. Kurzbeschreibung
[Zweck, Datenarten, Betroffene, Technologie, Drittlandbezug, Aufbewahrung]

2. Pruefung Art. 35 Abs. 3 DSGVO (Regelbeispiele)
- lit. a Profiling mit Rechtswirkung: ja / nein — [Begruendung]
- lit. b besondere Kategorien umfangreich: ja / nein — [Begruendung]
- lit. c öffentlicher Bereich Ueberwachung: ja / nein — [Begruendung]

3. Pruefung Art. 35 Abs. 4 DSGVO BfDI-/Landes-Blacklist
- Einschlaegig: ja / nein — [Listen-Position]

4. EDSA-Kriterien WP 248 rev.01 (Anzahl erfuellt)
- [X] von 9

5. Ergebnis
[ ] DSFA PFLICHTIG nach Art. 35 [Abs. 1 / Abs. 3 / Abs. 4]
[ ] DSFA EMPFOHLEN (Grenzfall, Dokumentation der Nicht-DSFA)
[ ] DSFA ENTBEHRLICH (Dokumentation der Begruendung)

6. Naechster Schritt
[ ] Vollstaendige DSFA durchfuehren (Skill dsfa-template-deutsch-vollvorlage)
[ ] Negative Triage-Dokumentation ablegen (Art. 5 Abs. 2 DSGVO Rechenschaftspflicht)

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Typische Fehler

- Triage wird muendlich erledigt, kein Vermerk angelegt — Verstoss gegen Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO.
- Nur Art. 35 Abs. 3 geprueft, Generalklausel Abs. 1 uebersehen — auch ausserhalb der Regelbeispiele kann DSFA-Pflicht bestehen.
- Blacklist der eigenen Landesbehoerde uebersehen (siehe Skill dsfa-bfdi-und-laender-blacklist).
- Negative Triage nicht dokumentiert — bei spaeterem Aufsichtsverfahren kein Nachweis.
- DSB nicht beteiligt obwohl Art. 35 Abs. 2 ausdruecklich Anhörung verlangt.
- Wesentliche Aenderung uebersehen — Re-Triage nach Art. 35 Abs. 11 notwendig.

## Querverweise

- `datenschutzrecht/skills/dsfa-bfdi-und-laender-blacklist/SKILL.md` — Blacklist-Abgleich
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md` — EDSA-Kriterien im Detail
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage nach positiver Triage
- `datenschutzrecht/skills/dsfa-typische-fehler-bei-erstpruefung/SKILL.md` — Fehlerquellen Erstpruefung
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Plugin-weite Triage
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36 DSGVO (Verordnung EU 2016/679)
- Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht)
- § 67 BDSG (Pflichtliste BfDI)
- EDSA-Leitlinien WP 248 rev.01 zur DSFA
- BfDI: bfdi.bund.de — aktuelle Blacklist und Whitelist live pruefen
- Landesdatenschutzbehoerden (LfDI BW, LDA Bayern u.a.) — eigene Listen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle oder lizenziertem Live-Zugriff

## 4. `dsfa-bfdi-und-laender-blacklist`

**Fokus:** Abgleich einer Verarbeitung mit der BfDI-Pflichtliste nach Art. 35 Abs. 4 DSGVO und mit den Listen der Landesdatenschutzbehoerden. Output: dokumentierter Listenabgleich mit Trefferanalyse und ggf. Verweis auf zwingende DSFA.

### BfDI- und Länder-Blacklist Abgleich

## Zweck

Dieser Skill fuehrt einen sauberen Abgleich einer konkreten Verarbeitungstaetigkeit mit der Pflichtliste der zuständigen Aufsichtsbehoerde nach Art. 35 Abs. 4 DSGVO (Blacklist) und mit der Whitelist nach Art. 35 Abs. 5 DSGVO durch. Ergebnis ist ein dokumentierter Listenabgleich, der die Erforderlichkeit oder Entbehrlichkeit einer DSFA stuetzt.

## Wann dieses Modul hilft

- In der DSFA-Trigger-Pruefung (Schwellwertanalyse)
- Bei einer Aufsichtsanfrage zur Begruendung einer durchgefuehrten oder unterlassenen DSFA
- Bei wesentlichen Aenderungen der Verarbeitung
- Wenn unklar ist, welche Landesdatenschutzbehoerde zuständig ist (Sitzland-Pruefung)

## Rechtlicher Rahmen

- Art. 35 Abs. 4 DSGVO: Aufsichtsbehoerden erstellen und veröffentlichen Listen der Verarbeitungstaetigkeiten, für die eine DSFA durchzufuehren ist.
- Art. 35 Abs. 5 DSGVO: Aufsichtsbehoerden koennen Listen veröffentlichen, für die keine DSFA erforderlich ist (Whitelist).
- Art. 35 Abs. 6 DSGVO: Listen werden dem Ausschuss EDSA uebermittelt, Koehaerenzverfahren bei grenzueberschreitenden Verarbeitungen.
- § 40 BDSG: Zuständigkeit der Landesdatenschutzbehoerden für den nicht-öffentlichen Bereich.
- § 67 BDSG verweist auf die Pflichtliste im öffentlichen Bereich des Bundes.
- EDSA-Leitlinien WP 248 rev.01 als Auslegungshilfe.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welche Verarbeitung soll abgeglichen werden? Konkrete Bezeichnung, Branche, eingesetzte Technologie, Datenkategorien.
2. **Verhaeltnismaessigkeitspruefung.** Zustaendige Aufsichtsbehoerde ermitteln: Bund (BfDI) für öffentliche Stellen des Bundes, Telekommunikation und Postwesen; Länder für den nicht-öffentlichen Bereich, sortiert nach Sitzland des Verantwortlichen.
3. **Risikoanalyse Listenabgleich.** Aktuelle Blacklist der zuständigen Behörde live abrufen (bfdi.bund.de bzw. Landesbehoerde). Treffer dokumentieren mit konkretem Listenpunkt und Datum des Abrufs.
4. **Massnahmen.** Pruefen ob die Verarbeitung exakt unter einen Listenpunkt faellt oder nur partiell. Bei partieller Deckung: Begruendung warum trotzdem oder warum nicht DSFA-pflichtig.
5. **Restrisiko.** Falls Blacklist-Treffer: DSFA zwingend. Falls Whitelist-Treffer: DSFA entbehrlich, Dokumentation der Whitelist-Position. Falls weder noch: Pruefung nach Art. 35 Abs. 1 und Abs. 3 DSGVO erforderlich.
6. **Konsultation / Genehmigung.** Listenabgleich dem DSB vorlegen, gegenzeichnen lassen, in das Verarbeitungsverzeichnis nach Art. 30 verlinken.

## Mustertext / Template

```
LISTENABGLEICH NACH ART. 35 ABS. 4 / ABS. 5 DSGVO [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME, SITZLAND]
Zustaendige Aufsichtsbehoerde: [BfDI / LfDI BW / LDA Bayern / ...]

Quelle Blacklist (Stand): [URL, Abrufdatum]
Quelle Whitelist (Stand): [URL, Abrufdatum]

Pruefung Blacklist
- Listenpunkt 1: [Bezeichnung] — Treffer ja / nein — Begruendung
- Listenpunkt 2: [Bezeichnung] — Treffer ja / nein — Begruendung
- ...

Pruefung Whitelist
- Listenpunkt: [Bezeichnung] — Treffer ja / nein — Begruendung

Ergebnis
[ ] BLACKLIST-TREFFER — DSFA zwingend nach Art. 35 Abs. 4 DSGVO
[ ] WHITELIST-TREFFER — DSFA entbehrlich nach Art. 35 Abs. 5 DSGVO
[ ] KEIN LISTENTREFFER — Pruefung nach Art. 35 Abs. 1, 3 DSGVO fortsetzen

Naechster Schritt: [Vollstaendige DSFA / Dokumentation / Weiterleitung an Skill]

Unterschrift: ____________________
```

## Praxishinweise zur Zuständigkeit

- Nicht-öffentlicher Bereich: Landesdatenschutzbehoerde am Sitz des Verantwortlichen.
- Oeffentlicher Bereich Bund (Bundesbehoerden, Telekommunikation, Post): BfDI.
- Oeffentlicher Bereich Land: jeweilige Landesdatenschutzbehoerde.
- Grenzueberschreitende Verarbeitung Art. 56 DSGVO: Federfuehrungsbehoerde am Sitz der Hauptniederlassung.
- Konzern mit mehreren Sitzlaendern: Hauptniederlassung nach Art. 4 Nr. 16 DSGVO bestimmen.

## Typische Fehler

- Nur BfDI geprueft, Landesbehoerde uebersehen — im nicht-öffentlichen Bereich ist regelmaessig die Landesbehoerde des Sitzlandes zuständig.
- Listenstand veraltet — Listen werden fortgeschrieben, immer aktuelles Datum dokumentieren.
- Partielle Deckung als Volltreffer behandelt — Listenpunkte sind typenoffen, aber konkret zu pruefen.
- Whitelist als Freibrief verstanden — Whitelist entlastet nur, wenn die Verarbeitung exakt zur Listenposition passt.
- Keine Dokumentation des Abrufdatums — Aufsicht kann den Stand nicht nachvollziehen.
- Grenzueberschreitende Verarbeitung: Federfuehrungsbehoerde nach Art. 56 DSGVO uebersehen.
- Konzerngesellschaften mit Sitz in mehreren Bundeslaendern: jede Gesellschaft hat eigene Aufsicht; nicht zentralisieren.
- Konflikt Bundes- versus Landesliste: bei Doppelpflicht die strengere Vorgabe anwenden.

## Beispielfaelle

- Kreditscoring-Plattform: regelmaessig auf mehreren Landeslisten (Scoring + automatisierte Entscheidung).
- Patientenakte mit Cloud-Speicherung: meist auf BfDI- bzw. Landesliste (besondere Kategorien Art. 9 + neue Technologie).
- Videoueberwachung Bahnhofsvorplatz: Art. 35 Abs. 3 lit. c DSGVO unmittelbar und zusaetzlich Listentreffer wegen öffentlichem Bereich.
- KI-Personalauswahl: regelmaessig Listentreffer wegen Profiling und neuen Technologien.

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md` — Trigger-Pruefung
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md` — Wenn kein Listentreffer
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Bei Blacklist-Treffer
- `datenschutzrecht/skills/spezial-dpia-dokumentenmatrix-und-lueckenliste/SKILL.md` — Dokumentenmatrix
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 4, 5, 6 DSGVO
- § 40, § 67 BDSG
- BfDI: bfdi.bund.de — Pflichtliste und Whitelist (live pruefen)
- LfDI Baden-Wuerttemberg, LDA Bayern, BlnBDI Berlin, HmbBfDI Hamburg, HBDI Hessen, LfDI Rheinland-Pfalz, LfD Niedersachsen, LDI NRW, ULD Schleswig-Holstein, LfDI Saarland, SaechsDSB, LfD Sachsen-Anhalt, TLfDI, LfD Mecklenburg-Vorpommern, LfDI Bremen, LfD Brandenburg — eigene Listen abrufen
- EDSA-Leitlinien WP 248 rev.01
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 5. `dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii`

**Fokus:** Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO: Aktenstruktur Versionierung Aufbewahrung Beweiswert. Output: DSFA-Akte mit Aktenuebersicht und Aufbewahrungsregeln.

### DSFA-Dokumentation und Rechenschaftspflicht

## Zweck

Strukturierte Dokumentation einer DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO. Ergebnis dieses Skills ist eine vollstaendige DSFA-Akte mit Aktenuebersicht, Versionierung, Aufbewahrungsregeln und Beweiswertbeurteilung. Ziel ist die jederzeitige Vorlagefaehigkeit gegenueber Aufsicht, Gericht oder DSB.

## Wann dieses Modul hilft

- Nach Abschluss einer DSFA, vor Archivierung
- Bei Aufsichtsanfrage zur Vorlage der DSFA
- Bei Audit durch DSB oder externen Pruefer
- Bei Wechsel des DSB oder des Verantwortlichen — Aktenuebergabe
- Bei wesentlicher Aenderung (Versionierung)

## Rechtlicher Rahmen

- Art. 5 Abs. 2 DSGVO: Rechenschaftspflicht — der Verantwortliche muss die Einhaltung der Grundsaetze nachweisen koennen.
- Art. 24 DSGVO: Verantwortung des für die Verarbeitung Verantwortlichen.
- Art. 30 DSGVO: Verzeichnis von Verarbeitungstaetigkeiten — DSFA-Verweis.
- Art. 35 Abs. 11 DSGVO: Re-Pruefungspflicht.
- Art. 58 Abs. 1 lit. a DSGVO: Auskunftsbefugnis der Aufsicht.
- § 257 HGB, § 147 AO für Aufbewahrungsfristen kaufmaennischer und steuerlicher Unterlagen — DSFA ist nicht kaufmaennisches Dokument, aber an die Verarbeitungstaetigkeit gekoppelt.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welcher Verarbeitungsvorgang? Eindeutige Akten-Identifikation (z. B. VV-Nummer, DSFA-Aktenzeichen).
2. **Verhaeltnismaessigkeitspruefung.** Pruefung welche Dokumente in die DSFA-Akte gehoeren — Vollstaendigkeit ohne Ueberfrachtung.
3. **Risikoanalyse.** Beweiswertrisiken pruefen — fehlende Unterschriften, fehlende Versionen, fehlende Datierungen, unklare Verantwortlichkeiten.
4. **Massnahmen.** Strukturierte Aktenfuehrung in standardisierter Form (digital signiert, mit Datum und Versionierung).
5. **Restrisiko.** Beweiswertbeurteilung — wie sicher ist die DSFA bei Aufsichtsverfahren? Ergaenzungen oder Bekraeftigungen.
6. **Konsultation / Genehmigung.** DSB bestaetigt Vollstaendigkeit; Aufbewahrung und Zugriffsrechte regeln.

## Aktenstruktur DSFA

```
DSFA-AKTE Aktenzeichen: [VV-XX-DSFA-YYYY-NN]
Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]
DSB: [NAME]

01 Deckblatt mit Versionshistorie
02 Schwellwertanalyse / Triage-Vermerk (Skill dsfa-art-35-dsgvo-trigger-und-anwendungsbereich)
03 Listenabgleich (Skill dsfa-bfdi-und-laender-blacklist)
04 WP-248-Pruefung (Skill dsfa-edpb-leitlinien-9-19-anwendung)
05 Methodenwahl-Memo (Skill dsfa-methodik-cnil-pia-vs-bsfd-bsi)
06 Vollstaendige DSFA (Skill dsfa-template-deutsch-vollvorlage)
07 Risikomatrix (Skill dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden)
08 TIA falls Drittlandtransfer (Skill dsfa-für-internationale-datentransfers)
09 KI-FRIA falls Hochrisiko-KI (Skill dsfa-für-ki-systeme-schnittstelle-art-26-kivo)
10 Stakeholder-Konsultation (Skill dsfa-stakeholder-konsultation-art-35-9)
11 DSB-Stellungnahme
12 Vorabkonsultation Art. 36 (falls erfolgt)
13 Freigabe Verantwortlicher
14 Verweis Verarbeitungsverzeichnis Art. 30
15 Revisionsplan (Skill dsfa-update-bei-aenderungen-und-revision)
16 Korrespondenz mit Aufsichtsbehoerde (falls)
17 Beweismittel: Datenflussdiagramm, AVV, SCC, TOM-Konzept

Versionsverzeichnis
| Version | Datum | Aenderung | Autor | Freigabe |

Zugriffskonzept
- Lesend: [Liste der berechtigten Personen]
- Schreibend: [Verantwortlicher, DSB, dokumentierender Mitarbeiter]
- Aufsichtsbehoerde: auf Anforderung Vollzugriff
```

## Aufbewahrungsregeln

- DSFA muss waehrend der gesamten Dauer der Verarbeitungstaetigkeit aufbewahrt werden.
- Nach Ende der Verarbeitung mindestens für den Zeitraum etwaiger Anspruchsverjaehrungen (Art. 82 DSGVO; immaterieller Schaden) — Empfehlung: 5 Jahre nach Ende der Verarbeitung; bei öffentlichen Stellen oft 10 Jahre.
- Alte Versionen nicht loeschen, sondern archivieren.
- Bei Anbieterwechsel: Uebergabe der Akte einschliesslich aller Versionen.
- Bei steuerlich relevanten Verarbeitungen ggf. § 147 AO 10 Jahre.

## Beweiswertkriterien

- Datierung und Unterschrift jedes Dokuments
- Versionierung und Aenderungshistorie
- Klare Autorenschaft (Wer hat dokumentiert, wer hat beschlossen?)
- DSB-Anhörung dokumentiert mit Datum
- Quellenverzeichnis (Aufsichtshinweise, Leitlinien, Rechtsprechung)
- Verweis auf Verarbeitungsverzeichnis und AVV

## Typische Fehler

- DSFA wird im Mail-Anhang verteilt, aber nicht in einer strukturierten Akte gefuehrt.
- Versionen werden ueberschrieben — alte Versionen unwiederbringlich verloren.
- DSB-Stellungnahme nur muendlich — kein Nachweis.
- Aktenzeichen fehlt — DSFA nicht zuordenbar.
- Aufbewahrungsfrist nicht definiert — DSFA wird mit Mitarbeiter-Personalakte vernichtet.
- Zugriffsrechte ungeregelt — DSFA mit personenbezogenen Risikobeschreibungen offen einsehbar.
- Beweismittel (Datenflussdiagramm) nicht beigefuegt — DSFA bleibt abstrakt.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage
- `datenschutzrecht/skills/dsfa-update-bei-aenderungen-und-revision/SKILL.md` — Versionierung
- `datenschutzrecht/skills/verarbeitungsverzeichnis-vvt-generator/SKILL.md` — VV Art. 30 Verlinkung
- `datenschutzrecht/skills/spezial-dpia-dokumentenmatrix-und-lueckenliste/SKILL.md` — Dokumentenmatrix
- `datenschutzrecht/skills/spezial-datenschutzrecht-compliance-dokumentation-und-akte/SKILL.md` — Aktenfuehrung allg.
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 5 Abs. 2 DSGVO
- Art. 24, 30, 35, 58, 82 DSGVO
- § 147 AO; § 257 HGB (Bezugsfristen)
- EDSA-Leitlinien WP 248 rev.01
- BfDI / Landesbehoerden — Hinweise zur Rechenschaftspflicht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
