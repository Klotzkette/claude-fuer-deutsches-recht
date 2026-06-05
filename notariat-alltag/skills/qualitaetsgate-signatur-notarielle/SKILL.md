---
name: qualitaetsgate-signatur-notarielle
description: "Qualitaetsgate Signatur Notarielle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Qualitaetsgate Signatur Notarielle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Qualitaetsgate Signatur Notarielle** im Plugin Notariat Alltag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notariat-055-qualitaetsgate-vor-signatur-und-einreichung` | Notariat im Alltag: Qualitätsgate vor Signatur und Einreichung. Systematische letzte Prüfung aller Dokumente vor der elektronischen Signatur und Einreichung beim Registergericht oder Grundbuchamt. |
| `notariat-056-notarielle-bescheinigung-vertretungsbescheinigung-u` | Notariat im Alltag: Notarielle Bescheinigung – Vertretungsbescheinigung und Registerstand. Bescheinigungen nach § 21 BNotO, Vertretungsberechtigungsbescheinigung und aktuelle Registerstandsbescheinigungen. |
| `notariat-057-remote-vorbereitung-ohne-unzulaessige-fernbeurkundu` | Notariat im Alltag: Remote-Vorbereitung ohne unzulässige Fernbeurkundung. Was remote vorbereitet werden darf, Grenzen der Fernkommunikation, zulässige digitale Zusammenarbeit und Terminvorbereitung. |

## Arbeitsweg

Im Plugin Notariat Alltag gilt für **Qualitaetsgate Signatur Notarielle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `notariat-055-qualitaetsgate-vor-signatur-und-einreichung`

**Fokus:** Notariat im Alltag: Qualitätsgate vor Signatur und Einreichung. Systematische letzte Prüfung aller Dokumente vor der elektronischen Signatur und Einreichung beim Registergericht oder Grundbuchamt.

# Notariat im Alltag: Qualitätsgate vor Signatur und Einreichung

## Zweck und Anwendungsbereich

Das Qualitätsgate ist der letzte Prüfpunkt, bevor ein Dokument signiert und bei Behörden eingereicht wird. Fehler nach der Einreichung kosten Zeit, Rang und ggf. Haftung. Dieser Skill strukturiert eine vollständige Vorprüfung.

Rechtsgrundlagen: § 17 BeurkG (Belehrung und Vollständigkeit), DONot §§ 1–56 (Aktenführung), § 12 HGB (HR-Anmeldung), GBO § 13 (Antrag), § 19 BNotO (Haftung), ERVV (Signaturformat), GNotKG (Kostenfestsetzung).

## Qualitätsgate: 10-Punkte-Prüfung

**1. Personalien und Identität:**
- Alle Namen korrekt geschrieben (Vor- und Nachname, Firmierung)?
- Geburtsdaten korrekt?
- Adressen aktuell?

**2. Vertretungsmacht:**
- Vollmachten vorhanden und inhaltlich ausreichend?
- Registerauszüge aktuell (max. 3 Monate)?
- § 181 BGB-Befreiung dort wo nötig dokumentiert?

**3. Gegenstand der Einreichung:**
- Flurstücksnummer / Handelsregisternummer korrekt?
- Betrag / Nennwert korrekt?
- Rechtsgeschäft vollständig beschrieben?

**4. Formvoraussetzungen:**
- Richtige Form gewählt (Beurkundung / Beglaubigung / Ausfertigung / Abschrift)?
- PDF/A-Konformität geprüft?
- qeS korrekt angebracht und gültig?

**5. Anlagen:**
- Alle Anlagen vorhanden und in richtiger Reihenfolge?
- Anlagenverzeichnis vollständig?
- Beglaubigte Anlagen korrekt beglaubigt?

**6. Fristen:**
- Einreichungsfrist eingehalten (Zwischenverfügungs-Frist, Anmeldepflicht)?
- Wartefrist abgelaufen?

**7. Kosten:**
- Kostennote stimmt mit Gegenstandswert und KV überein?
- Kostenschuldner korrekt?

**8. GwG:**
- GwG-Dokumentation vollständig?
- Transparenzregister-Abfrage archiviert?

**9. Signatur und Dateiformat:**
- qeS-Zertifikat gültig?
- Keine Änderungen nach Signatur?
- Dateiformat kompatibel mit Zielsystem?

**10. Vier-Augen:**
- Zweite Person hat alle Punkte bestätigt?

## Qualitätsgate für Fälligkeitsmitteilung (besonders kritisch)

Vor jeder Fälligkeitsmitteilung:
- [ ] Auflassungsvormerkung eingetragen
- [ ] Negativattest / Vorkaufsrechtszeugnis
- [ ] Steuerliche Unbedenklichkeit
- [ ] Löschungsunterlagen
- [ ] GwG-Check vollständig
- [ ] Alle sonstigen Vertragsbedingungen erfüllt
- [ ] Vier-Augen-Prüfung abgeschlossen

## Qualitätsgate für Handelsregisteranmeldung

- [ ] Alle erforderlichen Anlagen (Beschluss, Gesellschafterliste, Satzung)?
- [ ] qeS des Notars korrekt?
- [ ] § 6 Abs. 2-Erklärung vorhanden (GmbH-GF)?
- [ ] Einzahlungsnachweis (Kapitalerhöhung)?
- [ ] Vollständige Satzungsfassung (Satzungsänderung)?

## Qualitätsgate für Grundbuchantrag

- [ ] Bewilligungen in richtiger Form (öffentlich beglaubigt)?
- [ ] Steuerliche Unbedenklichkeit (bei Eigentumsumschreibung)?
- [ ] Vollmachten aktuell?
- [ ] Rangstelle korrekt?

## Prüfprogramm

- Wurde ein formalisiertes Qualitätsgate-Protokoll ausgefüllt?
- Vier-Augen-Prüfung von zweiter qualifizierter Person bestätigt?
- Alle 10 Punkte abgehakt?

## Typische Fallen

- Signatur auf falschem Dokument (alte Version).
- Anlage fehlt → Zurückweisung.
- Falsche Flurstücksnummer → Rangverlust.
- Fälligkeitsmitteilung ohne vollständige Checkliste → Schadensersatz.
- qeS-Zertifikat abgelaufen → Einreichung scheitert.

## Rechtsquellen

- § 19 BNotO (Haftung): https://dejure.org/gesetze/BNotO/19.html
- § 17 BeurkG: https://dejure.org/gesetze/BeurkG/17.html
- ERVV (Signatur): https://www.gesetze-im-internet.de/ervv/
- GBO § 13: https://dejure.org/gesetze/GBO/13.html
- BNotK Qualitätshinweise: https://www.bnotk.de

## Output-Formate

- **Qualitätsgate-Protokoll** (alle 10 Punkte, je Einreichungstyp)
- **Fälligkeitsmitteilungs-Checkliste** (Vier-Augen)
- **HR-Anmeldungs-Gate** (Checkliste)
- **Grundbuchantrag-Gate** (Checkliste)
- **Fehlerbehebungsleitfaden** (wenn Qualitätsgate einen Mangel findet)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

## 2. `notariat-056-notarielle-bescheinigung-vertretungsbescheinigung-u`

**Fokus:** Notariat im Alltag: Notarielle Bescheinigung – Vertretungsbescheinigung und Registerstand. Bescheinigungen nach § 21 BNotO, Vertretungsberechtigungsbescheinigung und aktuelle Registerstandsbescheinigungen.

# Notariat im Alltag: Notarielle Bescheinigung – Vertretungsbescheinigung, Registerstand

## Zweck und Anwendungsbereich

Notarielle Bescheinigungen nach § 21 BNotO sind ein häufig unterschätztes, aber wichtiges Instrument. Sie bestätigen Tatsachen, die der Notar aus öffentlichen Registern oder seiner eigenen Wahrnehmung kennt. Dieser Skill klärt Voraussetzungen, Inhalte und Abgrenzungen.

Rechtsgrundlagen: § 21 BNotO (notarielle Bescheinigung), § 20 BNotO (Beratung), § 39 BeurkG (Beglaubigung), § 21 FamFG (Registerauskunft), HGB § 15 (negative Publizität), EGBGB Art. 11 (Formstatut), GNotKG KV Nr. 25200 (Bescheinigungsgebühr).

## § 21 BNotO: Bescheinigung über Tatsachen

Der Notar kann Bescheinigungen ausstellen über:
- Den Inhalt öffentlicher Register (Handelsregister, Grundbuch, Grundbuchauszüge)
- Die Vertretungsmacht einer Person (Vertretungsbescheinigung)
- Sonstige Tatsachen, die der Notar kennt oder zuverlässig prüfen kann

**Abgrenzung zur Beglaubigung:** Die Bescheinigung bestätigt Tatsachen; die Beglaubigung bestätigt die Echtheit einer Unterschrift oder die Übereinstimmung einer Abschrift mit dem Original.

## Vertretungsbescheinigung

Die Vertretungsbescheinigung bestätigt, dass eine bestimmte Person eine Gesellschaft oder Institution rechtswirksam vertreten kann. Inhalt:
- Name der vertretenen Gesellschaft und Registernummer
- Name des Vertreters
- Art der Vertretungsmacht (Einzel- oder Gesamtvertretung, § 181 BGB-Befreiung)
- Datum des Registerauszugs, auf den sich die Bescheinigung stützt

**Verwendung:** Für ausländische Register, Notariate, Gerichte, die einen aktuellen deutschen HR-Auszug nicht direkt abrufen können.

## Registerstandsbescheinigung

Bestätigt den aktuellen Stand eines deutschen Registers (Handelsregister, Grundbuch) zu einem bestimmten Datum. Wichtig für:
- Auslandsgeschäfte (ausländisches Notariat braucht Beweis über deutschen Registerstand)
- M&A-Transaktionen (Closing-Bestätigung des Registerinhalts)
- Kreditvergabe (aktueller Gesellschafterbestand der GmbH)

## Grenzen der Bescheinigung

Der Notar bescheinigt nur Tatsachen, die er korrekt prüfen kann:
- Registerinhalte: nur auf Basis eines aktuellen Auszugs
- Vertretungsmacht: nur was aus dem Register ersichtlich ist (keine Unterschreitung der Vertretungsmacht durch interne Satzungsregeln, die nicht eingetragen sind)
- Keine Aussagen über die wirtschaftliche Lage oder Bonität der Gesellschaft

## Form und Sprache

Bescheinigungen können auf Wunsch zweisprachig (Deutsch + Fremdsprache) ausgestellt werden. Sie benötigen die Unterschrift des Notars und das Amtssiegel. Apostille oder Legalisation ggf. erforderlich für die Verwendung im Ausland.

## Kostenhinweise

Bescheinigung nach § 21 BNotO: KV Nr. 25200 GNotKG. Gegenstandswert: Wert des bescheinigten Vorgangs. Mindestgebühr beachten.

## Prüfprogramm

- Ist der Inhalt der Bescheinigung korrekt und vollständig aus dem Register ersichtlich?
- Ist der Registerauszug aktuell (max. 3 Monate)?
- Ist die Bescheinigung auf die im Ausland/bei der Behörde benötigte Form abgestimmt?
- Apostille oder Legalisation nötig?
- Zweisprachige Fassung gewünscht?

## Typische Fallen

- Veralteter Registerauszug als Basis → Bescheinigung überholt.
- Bescheinigung bestätigt interne Vertretungseinschränkungen, die nicht eingetragen sind → falsche Angabe.
- Keine Apostille für Auslandsverwendung.
- Bescheinigung über Tatsachen, die der Notar nicht aus dem Register kennt → Haftungsrisiko.

## Rechtsquellen

- § 21 BNotO: https://dejure.org/gesetze/BNotO/21.html
- § 39 BeurkG: https://dejure.org/gesetze/BeurkG/39.html
- GNotKG KV Nr. 25200: https://www.gesetze-im-internet.de/gnotkg/
- EGBGB Art. 11: https://dejure.org/gesetze/EGBGB/11.html
- BNotK Bescheinigungen: https://www.bnotk.de

## Output-Formate

- **Vertretungsbescheinigung-Muster** (§ 21 BNotO)
- **Registerstandsbescheinigung-Muster**
- **Zweisprachige Bescheinigung** (DE/EN)
- **Apostille-Checkliste** (bei Auslandsverwendung)
- **Mandantenmail** (Zweck der Bescheinigung erläutern)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

## 3. `notariat-057-remote-vorbereitung-ohne-unzulaessige-fernbeurkundu`

**Fokus:** Notariat im Alltag: Remote-Vorbereitung ohne unzulässige Fernbeurkundung. Was remote vorbereitet werden darf, Grenzen der Fernkommunikation, zulässige digitale Zusammenarbeit und Terminvorbereitung.

# Notariat im Alltag: Remote-Vorbereitung ohne unzulässige Fernbeurkundung

## Zweck und Anwendungsbereich

Die Digitalisierung verleitet zu der Annahme, man könne Beurkundungen vollständig remote abwickeln. Dieser Skill klärt, was vor dem Termin remote erlaubt ist, welche Schritte zwingend persönlich stattfinden müssen und wie ein optimaler Remote-Vorbereitungsprozess aussieht.

Rechtsgrundlagen: §§ 6–35 BeurkG (Beurkundungsverfahren – Präsenzerfordernis), § 13 BeurkG (Vorlesen in Gegenwart), § 16 BeurkG (Dolmetscher), § 16a BNotO (Videobeurkundung – begrenzt), §§ 40a–40e BeurkG (Online-Beglaubigung), § 29 BNotO (Verschwiegenheit bei Kommunikation), DSGVO (Datenschutz).

## Was ist remote zulässig?

| Tätigkeit | Remote zulässig? |
|---|---|
| Entwurfserstellung und -versand | Ja |
| Sachverhaltsaufnahme per Telefon/Video | Ja (kein Beurkundungsakt) |
| Identifizierung per Video-KYC | Nur für Online-Beglaubigung (§ 40a BeurkG) |
| Korrekturen am Entwurf besprechen | Ja |
| Erläuterung des Entwurfs | Ja (aber Belehrung nach § 17 BeurkG beim Termin) |
| Vollmacht vorausfüllen | Ja |
| GwG-Unterlagen anfordern | Ja |
| Beurkundung selbst | NEIN (§ 13 BeurkG: Gegenwart erforderlich) |
| Unterschriftsbeglaubigung | NEIN (Ausnahme: Online-Beglaubigung § 40a BeurkG) |

## Zulässige Online-Beglaubigung (§§ 40a–40e BeurkG)

Seit 2022: Unterschriftsbeglaubigung kann unter bestimmten Voraussetzungen online erfolgen:
- Beteiligter nutzt qualifizierte elektronische Signatur (qeS) nach eIDAS
- Notar und Beteiligter kommunizieren per Videokonferenz
- Identifizierung über zugelassenes Videoident-Verfahren
- Geltungsbereich begrenzt auf bestimmte Urkunden

## Optimaler Remote-Vorbereitungsprozess

1. **Sachverhaltsaufnahme** (Telefon/Video, 30 Min.)
2. **GwG-Unterlagen-Anforderung** per E-Mail
3. **Entwurf erstellen und versenden** (Entwurfsversand + Wartefrist §17 Abs. 2a BeurkG)
4. **Entwurfsreview per Video** (Fragen klären, Änderungen besprechen)
5. **Termin vereinbaren** (erst nach Ablauf Wartefrist)
6. **Terminerinnerung** mit Unterlagen-Checkliste (was mitbringen?)
7. **Präsenztermin** (Identifizierung, Vorlesen, Belehrung, Unterzeichnung)

## Datenschutz bei Remote-Kommunikation

- Videocalls: nur über datenschutzkonforme Plattformen (DSGVO, Art. 32)
- Dokumentenversand: beN oder verschlüsseltes PDF
- Aufzeichnung von Videocalls: nur mit Einwilligung; für Beurkundungszwecke nicht geeignet
- Speicherung von Videokonferenzdaten: begrenzte Aufbewahrung

## Häufige Fehler bei Remote-Zusammenarbeit

- Notar erteilt „Vorab-Belehrung" per Video, die die formelle Belehrung beim Termin ersetzen soll → unzulässig.
- Notar nimmt Änderungswünsche per Video entgegen ohne beide Parteien gleichzeitig einzubeziehen → Unparteilichkeitsrisiko.
- Mandant möchte Beurkundung per Video-Call → ausdrückliche Aufklärung: nur in gesetzlich geregelten Ausnahmefällen.

## Prüfprogramm

- Ist der geplante Schritt eine Beurkundungshandlung (Präsenz erforderlich) oder eine Vorbereitungsmaßnahme?
- Liegt eine gesetzliche Grundlage für die Online-Beglaubigung vor?
- Remote-Kommunikation DSGVO-konform?
- Entwurfsversand dokumentiert?

## Typische Fallen

- Belehrung remote erteilt, nicht wiederholt beim Termin → §17 BeurkG-Mangel.
- Beurkundung via Zoom ohne gesetzliche Basis → nichtige Urkunde.
- Entwurfsänderungen remote vereinbart, aber nicht in aktualisiertem Entwurf festgehalten.

## Rechtsquellen

- § 13 BeurkG: https://dejure.org/gesetze/BeurkG/13.html
- §§ 40a–40e BeurkG: https://dejure.org/gesetze/BeurkG/40a.html
- § 16a BNotO: https://dejure.org/gesetze/BNotO/16a.html
- DSGVO Art. 32: https://dejure.org/gesetze/DSGVO/32.html
- BNotK Online-Beurkundung: https://www.bnotk.de

## Output-Formate

- **Remote-Vorbereitungsplan** (Schritt für Schritt)
- **Zulässigkeits-Entscheidungsbaum** (was remote geht, was nicht)
- **Video-Terminagenda** (Entwurfsreview, kein Beurkundungsakt)
- **DSGVO-Prüfung Kommunikationstool**
- **Mandantenmail** (Vorbereitung remote, Präsenztermin nötig)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de
