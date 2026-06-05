---
name: betreiber-mitverschulden-betriebsanleitung
description: "Betreiber Mitverschulden Betriebsanleitung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Betreiber Mitverschulden Betriebsanleitung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Betreiber Mitverschulden Betriebsanleitung** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `betreiber-mitverschulden-und-fehlbedienung` | Prüft Betreiber-Mitverschulden: missachtete Anleitung, fehlende Wartung, Umgehung von Schutzfunktionen, Schulungslücken und Logspuren. |
| `betriebsanleitung-sprache-und-warnhinweise` | Prüft Betriebsanleitung, Sicherheitsinformationen, digitale Anleitung, Sprache, Restgefahren und Verständlichkeit für Zielgruppen. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Betreiber Mitverschulden Betriebsanleitung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `betreiber-mitverschulden-und-fehlbedienung`

**Fokus:** Prüft Betreiber-Mitverschulden: missachtete Anleitung, fehlende Wartung, Umgehung von Schutzfunktionen, Schulungslücken und Logspuren.


# Betreiber-Mitverschulden und Fehlbedienung

## Fachkern: Betreiber-Mitverschulden und Fehlbedienung
- **Spezialgegenstand:** Betreiber-Mitverschulden und Fehlbedienung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Wenn ein Roboter Schäden anrichtet, hängt die Haftungsverteilung wesentlich davon ab, ob der Betreiber die Anleitung beachtet, Wartung dokumentiert, Schutzfunktionen aktiv gelassen und Personal geschult hat. Aus Sicht des Herstellers ist Mitverschulden des Betreibers oft die einzige Möglichkeit, der vollen ProdHaftG-Haftung zu entgehen. Aus Sicht des Betreibers (oder seines Geschädigten) wird umgekehrt geprüft, ob der Hersteller seinen Pflichten zur "vernünftigerweise vorhersehbaren Fehlanwendung" (Art. 6 MaschinenVO; § 3 ProdSG; Art. 9 KI-VO) genügt hat. Dieser Skill liefert das Prüfschema, eine Indizienliste und Vorlagen für Schriftsätze.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller-Verteidigung, Betreiber-Anspruchsdurchsetzung, Versicherer, Geschädigter, Sachverständiger.
2. **Vorfall:** Personenschaden, Sachschaden, Produktionsausfall, Datenpanne durch Fehlbedienung.
3. **Robotertyp und Schutzkonzept:** Welche Schutzfunktionen sind vorhanden, welche aktiv im Vorfall?
4. **Schulungs- und Wartungsstand:** Aktuell? Dokumentiert?
5. **Unterlagen:** Anleitung, Risikobeurteilung, Wartungsprotokolle, Schulungsnachweise, Logs, Fotos, Zeugenaussagen, Vorfallbericht.

## Rechtlicher Rahmen

- **§ 254 BGB** Mitverschulden.
- **§ 6 Abs. 1 ProdHaftG** Haftungsausschluss; **§ 6 Abs. 3 ProdHaftG** Mitverschulden.
- **VO (EU) 2024/2853** (neue ProdHaftRL, Geltung 09.12.2026): Art. 13 Abs. 2 Beweiserleichterungen; Art. 11 Haftungsbefreiung des Wirtschaftsakteurs.
- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.7 Information, Nr. 1.1.2(c) vernünftigerweise vorhersehbare Fehlanwendung.
- **KI-VO** Art. 9 Abs. 4: Risikomanagement muss vorhersehbare Missbrauchsfälle (Foreseeable Misuse) abdecken.
- **§ 823 BGB** Verkehrssicherungspflichten beider Seiten.
- **ArbSchG**, **BetrSichV** Betreiberpflichten zur Unterweisung und Wartung.

## Schritt für Schritt

1. **Tatsachen sammeln** chronologisch; nicht bewerten, sondern fixieren.
2. **Logs auswerten.** Wer hat wann welche Funktion benutzt? Wurde ein Schutzkreis gebrückt? Welche Software-Version?
3. **Anleitung prüfen** auf konkrete Warnungen und Pflichten: Wartungsintervalle, Schulungserfordernisse, bestimmungsgemäße Verwendung.
4. **Vorhersehbarkeit der Fehlanwendung.** Wurde sie in der Risikobeurteilung des Herstellers berücksichtigt? Falls nein: Hersteller-Pflichtverletzung.
5. **Betreiberorganisation.** § 130 OWiG-Analyse: Aufsichtspflicht-Verletzung? Verantwortliche Person benannt?
6. **Mitarbeiter-Verhalten.** Schulungsstand, Unterweisungsnachweise; Anweisungslage; Druck/Stress als Erklärungsfaktor.
7. **Mitverschuldensquote.** Vorschlag erarbeiten unter Berücksichtigung BGH-Rspr. zu § 254 BGB; ggf. gestuft (Vollverschulden Betreiber 100 %, anteilig 30/70, etc.).
8. **Schriftsatz / Memo.** Trennung Tatsachen, technische Bewertung, rechtliche Würdigung; Sachverständigenbeweis vorschlagen.

## Trade-off-Matrix

| Argument Hersteller | Pro | Contra | Gegenstrategie Betreiber |
|---|---|---|---|
| Anleitung nicht befolgt | klar dokumentiert | "Anleitung war 250 Seiten, intransparent" | KISS-Prinzip; Quick-Start-Guide |
| Schutzfunktion deaktiviert | Logspur sichtbar | "Werkseitig deaktiviert" / "vom Servicetechniker" | Verantwortlichkeitsketten dokumentieren |
| Mitarbeiter unqualifiziert | Schulungsnachweise fehlen | "Hersteller hat keine Schulung angeboten" | Schulungsangebot vertraglich vereinbaren |
| Wartung versäumt | Lücke im Plan | "Hersteller-Service nicht verfügbar" | SLA prüfen; Wartungstickets archivieren |

## Praxistipps

- **Logs sofort sichern** (Schreibsperre, Hash) – nicht überschreiben lassen.
- **Brücken/Bypässe** physisch fotografieren.
- **Schulungsnachweise** mit Datum und Unterschrift; nicht nur Listenhaken.
- **Wartungsverträge** auf SLA prüfen; bei verspäteter Wartung des Herstellers ist Mitverschulden des Betreibers reduziert.
- **Sachverständiger** mit Robotik-Erfahrung wählen, nicht nur Maschinenbau-Generalist.

## Mustertexte

**Auszug Klageschrift Geschädigter (Replik auf Mitverschuldensvortrag):**

> Soweit die Beklagte einwendet, der Kläger habe Schutzfunktionen umgangen, ist dies sachlich unzutreffend. Ausweislich des Wartungsprotokolls vom 12.03.2026 (Anlage K12) wurde die Schutzfunktion durch die von der Beklagten beauftragte Service-Firma am 10.03.2026 deaktiviert und nicht wieder aktiviert. Die Verantwortung hierfür trifft den Hersteller im Wege der Erfüllungsgehilfenhaftung § 278 BGB. Die "vernünftigerweise vorhersehbare Fehlanwendung" gemäß Art. 6 MaschinenVO umfasste zudem den hier vorliegenden Fall; die Risikobeurteilung der Beklagten (Anlage K7, S. 23) selbst weist hierauf hin, ohne hinreichende Gegenmaßnahmen vorzusehen.

**Vermerkpassage Versicherer (Anteil 30/70):**

> Nach Auswertung der Logs (Hash-protokolliert am 02.04.2026 durch Sachverständigen Dipl.-Ing. M.) erscheint eine Quote 30 % Geschädigter / 70 % Hersteller angemessen. Mitverschuldenstragend: nicht aktualisierte Software-Version am Betreiber-Cobot trotz vom Hersteller bereitgestelltem OTA-Update; herstellerseits jedoch fehlende Hinweisplicht-Erfüllung gemäß Art. 9 Abs. 4 KI-VO bei der konkret aufgetretenen Konstellation.

## Typische Fehler

- **Anleitung als "Schutzwall"** für Hersteller, ohne deren tatsächliche Lesbarkeit zu prüfen.
- **Wartungslücken pauschal** dem Betreiber zugerechnet, obwohl Hersteller-Service nicht verfügbar war.
- **Logs nicht gesichert** – Beweismittel ist überschrieben.
- **"Vernünftigerweise vorhersehbare Fehlanwendung"** unterschätzt im Hersteller-Risikomanagement.
- **§ 130 OWiG-Verantwortlicher** nicht benannt – Betreiberorganisation angreifbar.

## Querverweise

- `deliktische-haftung-paragraph-823-bgb`
- `beweislast-und-offenlegung-produkthaftung`
- `arbeitsschutz-betrsichv-robotik`

## Quellen Stand 06/2026

- § 254 BGB; § 823 BGB; § 278 BGB.
- ProdHaftG § 6.
- VO (EU) 2024/2853 (neue ProdHaftRL), Art. 11, 13.
- VO (EU) 2023/1230 (MaschinenVO), Art. 6, Anhang III.
- VO (EU) 2024/1689 (KI-VO), Art. 9.
- ArbSchG; BetrSichV; § 130 OWiG.
- Live-Verifikation auf eur-lex.europa.eu, bundesgerichtshof.de, dejure.org; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 2. `betriebsanleitung-sprache-und-warnhinweise`

**Fokus:** Prüft Betriebsanleitung, Sicherheitsinformationen, digitale Anleitung, Sprache, Restgefahren und Verständlichkeit für Zielgruppen.


# Betriebsanleitung, Sprache und Warnhinweise

## Fachkern: Betriebsanleitung, Sprache und Warnhinweise
- **Spezialgegenstand:** Betriebsanleitung, Sprache und Warnhinweise wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Die Betriebsanleitung ist ein Sicherheitsbauteil im juristischen Sinn: Fehler in Sprache, Verständlichkeit, Vollständigkeit oder Warnhinweisen lösen Konstruktions- oder Instruktionsfehler nach § 1 ProdHaftG, § 823 BGB und neuer Produkthaftungs-RL (EU) 2024/2853 aus. Die MaschinenVO VO (EU) 2023/1230 erlaubt erstmals **digitale** Anleitungen unter Bedingungen (Art. 10 Abs. 7 sowie Anhang III Nr. 1.7.4) – ein Paradigmenwechsel. Bei KI-Funktionen verlangt Art. 13 KI-VO eine Gebrauchsanweisung mit besonderem Inhalt. Dieser Skill prüft Anleitung und Warnhinweise auf Compliance und Haftungsrobustheit.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, technischer Redakteur, Marktüberwachung, Anwalt im Haftungsstreit.
2. **Produkt:** Industrieroboter, Cobot, Service-Roboter, Verbraucher-Robotik (z. B. Saugroboter).
3. **Zielgruppe:** Fachkraft, Endverbraucher, Pflegekraft, Patient, behindertengerecht?
4. **Sprache:** Welche Amtssprachen des Inverkehrbringens?
5. **Format:** Papier, PDF, Online, AR-/VR-Anleitung; Anleitung auf dem Roboter selbst?

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.7 Information und Warnhinweise; Art. 10 Abs. 7 zur digitalen Form; Geltung ab 20.01.2027.
- **Maschinen-RL 2006/42/EG** (Übergang bis 19.01.2027) verlangt Anleitung in Amtssprachen des Mitgliedstaats des Inverkehrbringens.
- **ProdSG / GPSR** VO (EU) 2023/988: Information für Verbraucher.
- **ProdHaftG / VO (EU) 2024/2853 (neu)**: Instruktionsfehler als Produktfehler.
- **§ 823 BGB**: ständige Rspr. des BGH zu Instruktionspflichten (Hersteller muss vor Gefahren in vernünftigerweise vorhersehbarer Verwendung warnen).
- **KI-VO** Art. 13 Transparenz; Art. 26 Abs. 1 Pflichten der Betreiber, Anleitung zu beachten; Art. 50 Transparenz bei interaktiven KI-Systemen.
- **GS-Zeichen / TÜV** ProdSG § 21 als ergänzendes Qualitätssignal.
- **Sprachenregime**: Amtssprache des Mitgliedstaats; in Deutschland deutsch (zumindest für Sicherheits- und Warninhalte).

## Schritt für Schritt

1. **Zielgruppenanalyse.** Fachkraft oder Endverbraucher? Sprachniveau, Vorbildung, Sinneseinschränkungen.
2. **Inhalt nach Anhang III Nr. 1.7 MaschinenVO**: Identifikation, Beschreibung, bestimmungsgemäße Verwendung, Restrisiken, Aufstellung/Anschluss, Bedienung, Wartung, Außerbetriebnahme, Schaltpläne, Lärm-/Vibrationsemissionen.
3. **KI-spezifischer Inhalt** Art. 13 Abs. 3 KI-VO: Identität Anbieter, Zweck, Leistungsmerkmale, Genauigkeit/Robustheit/Sicherheit-Grenzen, Human-Oversight-Maßnahmen, Lebensdauer, Wartung.
4. **Restrisiken explizit benennen.** Risikobeurteilung als Anhang oder zusammengefasst.
5. **Warnhinweise** nach ANSI Z535 / ISO 3864 / ISO 7010: Signalwort (GEFAHR/WARNUNG/VORSICHT/HINWEIS) + Pictogramm + Folge + Vermeidung.
6. **Digitale Anleitung** Anhang III Nr. 1.7.4 MaschinenVO: Verfügbarkeit per QR/URL, Auffindbarkeit für 10 Jahre, papierne Sicherheitsinformationen "free of charge upon request" mind. zwei Jahre nach Inverkehrbringen.
7. **Sprache** der einschlägigen Amtssprache des MS des Inverkehrbringens; Sicherheitsinhalte vor allem.
8. **Verständlichkeitstest** mit Probanden der Zielgruppe; bei Verbraucherprodukten Lesetest auf Schulniveau 8.
9. **Versionierung** und Archivierung; Anleitung ist Teil der technischen Dokumentation 10 Jahre (Art. 11 MaschinenVO; Art. 18 KI-VO).

## Trade-off-Matrix

| Frage | Konservativ | Modern | Empfehlung |
|---|---|---|---|
| Papier-Anleitung | immer | nur digital | bei MaschinenVO-Geltung digital + Sicherheits-Auszug Papier |
| Sprachen | nur Amtssprache | nur Englisch | nur Amtssprache; English ergänzend |
| Warnsymbole | viele | wenige Schlüsselbilder | nach Risiko priorisieren |
| Online-Updates | jährlich | rolling | Versionsstand sichtbar; alte Versionen auffindbar |

## Praxistipps

- **Quick-Start-Card** in jeder Sprache der Hauptmärkte; Sicherheitskern in einer Seite.
- **AR-Overlay** für Wartung – aber Papier-Notfallseite immer.
- **Übersetzung** durch Fachübersetzer mit Sicherheitskenntnis – nicht maschinell ohne Review.
- **Symbol-Glossar** als Pull-Out.
- **Akustische Warnung** bei interaktiver Robotik – Sprache zusätzlich zu Display.

## Mustertexte

**Warnhinweis (ANSI Z535/ISO 3864 Format):**

> WARNUNG. Quetschgefahr durch Cobot-Arm. Nicht in den Bewegungsraum greifen, solange die LED grün leuchtet. Bei Wartung Schlüsselschalter auf "Service"; nur autorisiertes Personal.

**Auszug digitale Anleitung – Hinweis auf Papier-Auszug:**

> Diese Anleitung ist digital unter https://[…]/manuals/[Seriennummer] in der jeweils gültigen Fassung verfügbar. Sicherheitsinformationen sind in gedruckter Form Bestandteil der Lieferung. Auf schriftliche Anforderung an [Adresse] senden wir Ihnen innerhalb von zwei Jahren nach Inverkehrbringen eine vollständige Papierfassung kostenfrei zu (Art. 10 Abs. 7 MaschinenVO).

**KI-Transparenz (Art. 13 Abs. 3 KI-VO, Auszug):**

> Das im Roboter integrierte KI-System "VisionCobot 3" dient der Hinderniserkennung im Cobot-Arbeitsraum. Trainingsdatenbasis: 2,8 Mio. annotierte Frames in den in Anlage B genannten Kontexten. Bekannte Genauigkeitsgrenzen: bei Gegenlicht über 80.000 Lux Recall-Reduktion um bis zu 12 %. Menschliche Kontrolle: jederzeitiges Not-Halt per Schlüssel; Override via Operator-Konsole. Lebensdauer-Garantie: 5 Jahre.

## Typische Fehler

- **Unverständliche Sprache** durch wörtliche Maschinenübersetzung.
- **Risikobeurteilung als alleinige Informationsquelle**; Anleitung nicht abgeleitet.
- **Pauschale Warnungen** ("Vorsicht! Achtung!") ohne konkrete Folge/Vermeidung.
- **Sprachversion fehlt** in einem Mitgliedstaat.
- **Digitale Anleitung** ohne Auffindbarkeit nach 10 Jahren – Hersteller-Pflichtverletzung.

## Querverweise

- `ce-zeichen-fehlgebrauch-und-abmahnung`
- `betreiber-mitverschulden-und-fehlbedienung`
- `barrierefreiheit-und-inklusion-robotik`

## Quellen Stand 06/2026

- VO (EU) 2023/1230 (MaschinenVO), Art. 10, 11, Anhang III Nr. 1.7.
- RL 2006/42/EG (bis 19.01.2027).
- VO (EU) 2023/988 (GPSR).
- VO (EU) 2024/1689 (KI-VO), Art. 13, 18, 26, 50.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- ProdHaftG; § 823 BGB.
- ISO 3864; ISO 7010; ANSI Z535.
- Live-Verifikation auf eur-lex.europa.eu, baua.de, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
