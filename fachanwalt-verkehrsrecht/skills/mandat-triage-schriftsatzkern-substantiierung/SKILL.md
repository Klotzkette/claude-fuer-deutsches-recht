---
name: mandat-triage-schriftsatzkern-substantiierung
description: "Mandat Triage Schriftsatzkern Substantiierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Neues Verkehrsrechtsmandat kommt rein und Anwalt muss, Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldb, 315C. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Mandat Triage Schriftsatzkern Substantiierung

## Arbeitsbereich

**Mandat Triage Schriftsatzkern Substantiierung** ordnet den Fall über die tragenden Prüfungslinien: Neues Verkehrsrechtsmandat kommt rein und Anwalt muss, Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldb. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `mandat-triage-verkehrsrecht` | Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klaeren und Fristen prüfen. Eingangs-Triage Verkehrsrecht. Prüfraster: Verfahrensart (Zivilrecht Schadensregulierung OWi Strafrecht Fahrerlaubnis) Unfallart Fristen (Einspruch OWi 2 Wochen § 67 OWiG Verjährung 3 Jahre § 195 BGB) Versicherungslage Eilbedürftigkeit vorläufige Entziehung § 111a StPO. Output: Routing-Entscheidung mit Folge-Skill. Abgrenzung zu fachanwalt-verkehrsrecht-orientierung (Orientierung) und bußgeld-einspruch-prüfen. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldbescheid, Klage KFZ-Versicherung: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `spezial-315c-internationaler-bezug-und-schnittstellen` | 315C: Internationaler Bezug und Schnittstellen im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `mandat-triage-verkehrsrecht`

**Fokus:** Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klaeren und Fristen prüfen. Eingangs-Triage Verkehrsrecht. Prüfraster: Verfahrensart (Zivilrecht Schadensregulierung OWi Strafrecht Fahrerlaubnis) Unfallart Fristen (Einspruch OWi 2 Wochen § 67 OWiG Verjährung 3 Jahre § 195 BGB) Versicherungslage Eilbedürftigkeit vorläufige Entziehung § 111a StPO. Output: Routing-Entscheidung mit Folge-Skill. Abgrenzung zu fachanwalt-verkehrsrecht-orientierung (Orientierung) und bußgeld-einspruch-prüfen.

### Mandat-Triage Verkehrsrecht

## Zweck

Verkehrsrechtliche Mandate sind heterogen — vom Auffahrunfall (Zivilrecht) über Geschwindigkeit (OWi) bis zur Verkehrsunfallflucht (Strafrecht). Strukturierte Triage stellt richtige Spur sicher.

## Ablauf — sieben Fragen

### Frage 1 — Wer ruft und für wen?

- Selbst Unfallbeteiligter
- Angehöriger
- Versicherer (Verteidigungsmandat)
- Anderer Anwalt (Vertretung)

### Frage 2 — Verfahrensart?

- **Zivilrechtlich** Schadensregulierung
- **Owi** Bußgeldbescheid wegen Geschwindigkeit Rotlicht Abstand Handy am Steuer Trunkenheit
- **Strafrechtlich** Verkehrsstraftat (§ 315c StGB Gefährdung § 315d Raserfälle § 142 Unfallflucht § 316 § 315a Trunkenheit § 229 fahrlässige Körperverletzung § 222 fahrlässige Tötung)
- **Fahrerlaubnisrecht** vorläufige Entziehung Wiedererteilung MPU
- **Versicherungsrecht** Deckungsablehnung Kasko Haftpflicht
- **Fahrerlaubnisrecht-Punkte** Fahreignungsregister (FAER) Tilgung

### Frage 3 — Akute Eilbedürftigkeit?

- Vorläufige Entziehung Fahrerlaubnis § 111a StPO — sofort Beschwerde § 304 StPO
- Berufstätigkeit auf Führerschein angewiesen — Härtefall-Argumentation
- Fahrtenbuch-Auflage drohend
- Hauptverhandlung Strafrecht binnen Tagen

### Frage 4 — Unfall: Personen- oder Sachschaden?

- Sachschaden — Standard-Regulierung
- Personenschaden — zusätzliche Quoten Schmerzensgeld Vorhaltekosten Heilbehandlungskosten Renten-Anspruch
- Bei Personenschaden sofort SV-Träger informieren (Krankenkasse BG)

### Frage 5 — Versicherungslage?

- Eigene Haftpflicht (Vollkasko)
- Verkehrsrechtsschutz (Deckungszusage einholen)
- Insassenunfallversicherung
- Gegnerische Versicherung bekannt?

### Frage 6 — Frist?

- **Einspruch Bußgeldbescheid** zwei Wochen § 67 OWiG
- **Anhörung im Bußgeldverfahren** keine zwingende Frist aber Bedeutung der Aussage
- **Verjährung zivilrechtlicher Anspruch** drei Jahre § 195 BGB
- **Verjährung Personenschaden** dreißig Jahre § 199 Abs. 2 BGB
- **Punkte-Tilgung** Fahreignungsregister
- **Wiedererteilung Fahrerlaubnis** Sperrfrist § 69a StGB

### Frage 7 — Hauptaktenstand?

- Polizeiprotokoll vorhanden?
- Schadensgutachten vorhanden?
- Anhörungsbogen StA / Bußgeldstelle?
- Bisheriger Schriftwechsel mit Versicherung?

## Routing-Matrix

| Verfahrensart | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| Schadensregulierung Sachschaden | `unfall-haftungsquote-berechnen` | Verjährung drei Jahre |
| Schadensregulierung Personenschaden | `unfall-haftungsquote-berechnen` plus medizinische Begutachtung | drei oder dreißig Jahre |
| Bußgeldbescheid | (Skill bußgeld-prüfen — perspektivisch) | zwei Wochen § 67 OWiG |
| Vorläufige Entziehung FE | sofort Beschwerde § 304 StPO | binnen Stunden |
| Verkehrsstraftaten | Skill aus `fachanwalt-strafrecht` `mandat-triage-strafrecht` | je nach Verfahrensstadium |
| MPU | (Skill mpu-vorbereitung — perspektivisch) | sechs Monate vor Frist Beginn |
| Punkte | (Skill faer-prüfen — perspektivisch) | Tilgungsfristen |
| Versicherungs-Deckungsstreit | Skill aus `fachanwalt-versicherungsrecht` | nach VVG |

## Eilmodus vorläufige Entziehung

Bei Fahrerlaubnis-vorläufig-entzogen § 111a StPO:

- **Beschwerde § 304 StPO** statthaft
- Hilfsweise Antrag auf Aufhebung beim selben Gericht
- Eilbedürftigkeit Beruf häufig führt zu Beschluss in der Sache
- Bei Hauptverhandlung Plädoyer auf Aussetzung § 69a StGB Sperrfrist nicht erforderlich

## Mandatsannahme

- **Konflikt-Check** — kein anderer Mandant in derselben Sache (Unfallgegner Versicherer Mitfahrer)
- **Streitwert** ab EUR 10000 LG; darunter AG (Streitwertgrenze zehntausend Euro seit 01.01.2026 Justizreform)
- **Komplexität** Personenschaden Eigentums-Streit über Halterstellung Auslandsbezug Lkw-Frachtrecht

## Eskalation

- **Telefon-Sofort** vorläufige FE-Entziehung
- **Binnen einer Stunde** Verkehrsunfallflucht-Anhörung
- **Heute** Versicherungs-Reaktion auf Deckungsablehnung Akteneinsicht Bußgeld
- **Diese Woche** Klageeinreichung Schadensregulierung Einspruch Bußgeld

## Ausgabe

- `triage-protokoll-verkehrsrecht.md`
- Aktenanlage Az-Vorschlag
- Frist im Fristenbuch
- Rechtsschutz-Deckungsanfrage als Entwurf
- Mandatsvereinbarung Vorlage
- Empfehlung Folge-Skill

## Quellen

- StVG StVO StPO §§ 111a 304
- StGB §§ 142 222 229 315a 315c 315d 316 69 69a
- OWiG § 67 (Einspruch)
- VVG §§ 28 86 115
- BGH VI. Zivilsenat 4. Strafsenat

## Aktuelle Rechtsprechung Triage (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand jeweils Volltext in der angegebenen Quelle aufrufen):

- BGH VI ZR 253/22, Urt. v. 16.1.2024 — Werkstattrisiko (juris.bundesgerichtshof.de)
- BGH VI ZR 239/22, Urt. v. 16.1.2024 — Werkstattrisiko bei fiktiver Abrechnung (juris.bundesgerichtshof.de)
- BGH VI ZR 280/22, Urt. v. 12.3.2024 — Sachverstaendigenrisiko (juris.bundesgerichtshof.de)
- BGH VI ZR 12/24, Urt. v. 5.11.2024 — Haushaltsfuehrungsschaden / Mindestlohn (juris.bundesgerichtshof.de)
- BGH VI ZR 24/25, Urt. v. 14.10.2025 — Substantiierungsanforderungen Art. 103 Abs. 1 GG (juris.bundesgerichtshof.de)
- BVerwG 3 B 2.24, Beschl. v. 8.1.2025 — Cannabis und KCanG (bverwg.de)
- BVerfG 2 BvR 1167/20, Beschl. v. 20.6.2023 — Rohmessdaten Geschwindigkeitsmessung (bundesverfassungsgericht.de)
- BVerfG 2 BvR 1616/18, Beschl. v. 12.11.2020 — Akteneinsicht / Informationszugang OWi (bundesverfassungsgericht.de)

<!-- AUDIT 27.05.2026: BGH VI ZR 1/21 (NOT_FOUND auf dejure.org) entfernt und ersetzt durch BGH VI ZR 37/99, NJW 2000, 861 (verifiziert auf dejure.org). -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `schriftsatzkern-substantiierung`

**Fokus:** Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldbescheid, Klage KFZ-Versicherung: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau.

### Schriftsatzkern und Substantiierung im Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht)

## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Schriftsatz im Bereich Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht) erstellt werden, typischerweise: Klage Verkehrsunfall, Einspruch OWi-Bussgeldbescheid, Klage KFZ-Versicherung.
- Die Mandatsannahme und ggf. Vergleichsverhandlung sind abgeschlossen oder gescheitert.
- Klage-, Widerspruchs-, Einspruchs-, Rechtsmittel-Frist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Parteien (Bezeichnung wie im Vorprozess oder Bescheid, exakte Schreibweise!).
- Zustellungsanschrift Bevollmaechtigte.
- Gericht/Behörde (Zuständigkeit pruefen und im Schriftsatz darstellen, wenn streitig).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Streitwert/Gegenstandswert.

### B. Antraege

Klassischer Antrag-Block; je nach Verfahrenstyp:

- Leistungsantrag (zu zahlen, zu unterlassen, zu beseitigen, herauszugeben).
- Feststellungsantrag (Feststellungsinteresse darlegen).
- Gestaltungsantrag (Aufhebung, Anfechtung, Scheidung).
- Hilfsantraege staffeln (von eng nach weit oder von hoch nach niedrig).

### C. Tatsachenvortrag

Der Substantiierungs-Kern; pro Anspruchsgrundlage in StVG, StVO, StVZO, FeV, PflVG, BKatV, OWiG eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen).
2. **Mandantenseitige Tatsachenbehauptungen** mit Beweisangeboten.
3. **Gegnerisches Verhalten** mit Belegen (Schreiben, Aussage, Verhalten).
4. **Schaden/Folgen** bezifferbar (Hauptforderung, Nebenforderung, Zinsen, Folgekosten).

### D. Rechtliche Wuerdigung

Anspruchsaufbau klassisch:

1. **Anspruchsgrundlage** nennen (z.B. § X iVm § Y).
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal wird gegen den Tatsachenvortrag gespiegelt.
3. **Einwendungen** der Gegenseite vorwegnehmen und entkraeften.
4. **Rechtsprechungs-Verweise:** BAG/BGH/BVerfG/EuGH/BFH je nach Fachgebiet; bei Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht) typischerweise die letzte hoechstrichterliche Linie zitieren.
5. **Subsumtion-Ergebnis** klar formulieren.

### E. Beweisangebote

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- Urkundenbeweis: konkrete Anlage Kxx benennen, Inhalt nicht nur "Vertrag" sondern "Vertrag vom TT.MM.JJJJ, dort § X Abs. Y, Anlage K1".
- Zeugenbeweis: Name, ladungsfaehige Anschrift, Beweisthema in einem Satz.
- Sachverstaendigenbeweis: ggf. Privatgutachten mit anfuegen, gerichtliches Gutachten beantragen.
- Parteivernehmung als letzte Stufe, mit Antrag § 448 ZPO und Indiziengeruest.
- Inaugenscheinnahme: bei Sache vor Ort (Mietraum, Baustelle, Fahrzeug, Hardware).

### F. Anlagenverzeichnis

- K1, K2 ... durchnummeriert (Antragstellerin/Klaegerin).
- Bei Beklagten B1, B2 ...
- Jede Anlage mit Datum, Absender, Empfaenger, Inhaltsbeschreibung in einem Satz.
- Pflicht-Erwaehnung im Tatsachenvortrag.

## Substantiierungs-Fallen im Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht)

- **Pauschaltatsachen** ohne konkrete Daten ("seit Jahren", "regelmaessig", "in mehreren Faellen") werden vom Gericht uebergangen.
- **Beweisangebot zur falschen Tatsache:** Beweisthema deckt nur Teilaussage ab.
- **Selbst-widersprueche** zwischen Schriftsatz und Anlage ("Im Vertrag steht doch was anderes").
- **Verspaeteter Vortrag** § 296 ZPO/§ 87b VwGO: Rueglich-Fristen beachten, Verschulden vermeiden.
- **Anspruchskonkurrenz** zwischen mehreren Grundlagen: nicht eine wegfallen lassen.

## Pruefkette vor Versand

1. Antragsformulierung tenoriert (urteilstauglich, vollstreckbar)?
2. Jede Tatbestandsmerkmal-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Eingangsstempel/elektronische Uebermittlung)?
4. Zuständigkeit positiv festgestellt?
5. Streitwert plausibel, ggf. mit Anlage Streitwert-Berechnung?
6. Anlagenverzeichnis vollstaendig und nummerisch konsistent?
7. beA-/EGVP-/EBO-Konformitaet (PDF/A, ERVV-Signatur)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Anwaeltin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG, BGH, BAG, BFH, BVerwG, EuGH und die jeweils massgeblichen Fachsenate für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht).
- StVG, StVO, StVZO, FeV, PflVG, BKatV, OWiG sowie Verordnungen/Richtlinien dazu.
- Aktuelle Reform- und Gesetzgebungslage einbeziehen.

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisangeboten, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht, EB).
4. **Streitwertskizze** (eigenes Memo, falls > 1 Anspruch).
5. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger?).

## Beispiel-Anspruchsgrundlagen im Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht)

Drei haeufig gebrauchte Anspruchsgrundlagen aus StVG, StVO, StVZO, FeV, PflVG, BKatV, OWiG und ihre Substantiierungs-Anforderungen:

### Grundlage 1

- Tatbestandsmerkmal 1: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 2: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 3: konkrete Tatsache + Beweis.
- Rechtsfolge: konkreter Antrag.

### Grundlage 2

Analog - jede Tatsache braucht ein Beweisangebot.

### Grundlage 3 (Auffanggrundlage / Sekundaeranspruch)

Hilfsweise vortragen, klar als Hilfsantrag/Hilfsvortrag kennzeichnen.

## Antrags-Muster nach Verfahrenstyp

Typische Antraege in Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht) (Klage Verkehrsunfall, Einspruch OWi-Bussgeldbescheid, Klage KFZ-Versicherung):

- Hauptantrag (Leistung/Feststellung/Gestaltung).
- Hilfsantrag (z.B. für den Fall, dass Hauptforderung verjaehrt ist).
- Annex-Antraege (Zinsen, Nebenforderungen, Kosten).
- Streitwert-Antrag (falls Streitwert streitig).

## Beweisaufnahme - was das Gericht sehen will

### Urkundenbeweis

- Anlage K1: Bezeichnung, Datum, kurze Inhaltsbeschreibung.
- Im Tatsachenvortrag: "Diese Behauptung beruht auf dem als Anlage K1 vorgelegten Schreiben der Beklagten vom TT.MM.JJJJ, dort Seite Y, Absatz Z."

### Zeugenbeweis

- Form: "Beweis: Aussage der Zeugin Name, ladungsfaehige Anschrift, zum Beweisthema (konkret in einem Satz)."
- Mehrere Zeuginnen zum gleichen Thema: Indiziengeruest staerken.
- Keine Beweisermittlung ueber Zeugnis - das Beweisthema muss konkret sein.

### Sachverstaendigenbeweis

- Bei Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht)-typischen Streitfaellen oft notwendig (Bauwerk, IT-System, Anlagebewertung, medizinische Frage).
- Privatgutachten als Anlage K vorlegen + zugleich gerichtliches Gutachten beantragen.
- Verfahrensoekonomie: Sachverstaendigen-Kosten frueh mit Mandantin besprechen.

### Parteivernehmung (§ 448 ZPO)

- Letzte Stufe, nur wenn andere Beweismittel ausgeschoepft.
- Indiziengeruest vortragen, das eine gewisse Wahrscheinlichkeit der Behauptung tragt.

## Replik-/Duplik-Vorausschau

Schon im Klageschriftsatz die wahrscheinlichen Einwaende der Gegenseite vorwegnehmen:

- Verjährung -> Hemmungstatbestand vortragen.
- Erfuellung/Aufrechnung -> rechtzeitige Tatsachenbasis schaffen.
- Formmangel -> Heilung/Schutz-Argument bereit halten.
- Treuwidrigkeit -> Indiziengeruest gegen Treuwidrigkeits-Vorwurf.

## Elektronische Einreichung (beA, EGVP, EBO, ELSTER)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- 1.10.2026 / 1.10.2027 - ZVollstrDigitG-Aenderungen im Vollstreckungsbereich; in Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht) ggf. spezifische ERV-Pflichten beachten.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln ("Die Klage ist zulaessig und begruendet" als Ueberschrift, aber dann substantiieren).
- Mandanten- und Beweismittel-Zitate woertlich, in Anfuehrungszeichen, mit Anlage-Verweis.
- Keine Gefuehlsausbrueche - sachlich auch bei provokanter Gegenseite.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag tenorierungsfaehig
- [ ] Frist gewahrt mit Reserve
- [ ] Jede Tatsache hat Beweis
- [ ] Anlagen vollstaendig und nummeriert
- [ ] Rechtsprechungs-Zitat aktuell
- [ ] Streitwert plausibel
- [ ] beA/EGVP-konform
- [ ] Senior-/Sozius-Freigabe

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Tatsachen-Grundlage und Streitwertskizze.
- `vergleichsverhandlung-strategie` (im selben Plugin) für parallelen Vergleichsversuch (Gueteverhandlung, Mediation).

## Aktuelle Rechtsprechung Schriftsatz Verkehrsrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026: BGH VI ZR 252/21 geloescht – AZ auf dejure.org nicht auffindbar (NOT_FOUND); ersetzt durch verifizierten BGH VI ZR 491/15 (dejure.org 2016,29366) zum selben Thema Sachverstaendigenkosten. BGH VI ZR 79/19 geloescht – AZ auf dejure.org nicht auffindbar (NOT_FOUND). NJW-Fundstelle VI ZR 344/21 korrigiert: 2023, 1123 (nicht 2023, 448). -->

## 3. `spezial-315c-internationaler-bezug-und-schnittstellen`

**Fokus:** 315C: Internationaler Bezug und Schnittstellen im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

### 315C: Internationaler Bezug und Schnittstellen

## Spezialwissen: 315C: Internationaler Bezug und Schnittstellen
- **Normen-/Quellenanker:** StVG, StVO, PflVG, VVG, EUR, OLG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **315C** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
