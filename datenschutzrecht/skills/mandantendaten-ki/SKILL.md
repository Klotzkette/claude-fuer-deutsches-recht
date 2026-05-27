---
name: mandantendaten-ki
description: "Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei pruefen. Art. 5 6 DSGVO BRAO § 43a Verschwiegenheit. Pruefraster: Rechtsgrundlage Zweckbindung Vertraulichkeit Anwaltsprivileg AVV KI-Anbieter. Output: Compliance-Memo Nutzungsempfehlung. Abgrenzung: nicht fuer allgemeine KI-VO-Fragen (ki-verordnung-compliance)."
---

# Mandantendaten und KI-Dienstleister (§ 203 StGB, Art. 28 DSGVO)

## Zweck

Dieser Skill begleitet die berufsrechtlich und datenschutzrechtlich konforme Einbindung externer IT- und KI-Dienstleister in Kanzlei- und Beratungsprozesse. Im Mittelpunkt stehen (1) die strafrechtliche Compliance nach § 203 StGB n.F., (2) die berufsrechtliche Verschwiegenheitspflicht nach § 43a Abs. 2 BRAO, (3) der datenschutzrechtliche Auftragsverarbeitungsvertrag nach Art. 28 DSGVO sowie (4) spezifische Anforderungen an KI-Systeme (Transfer Impact Assessment, EU-Hosting, Audit-Logs). Anwendungsfälle: Kanzlei möchte CloudDienstleister für E-Mail-Hosting einsetzen; Rechtsanwalt erwägt Nutzung eines KI-Tools zur Dokumentenanalyse; IT-Dienstleister erhält Zugang zu Mandantenakten für Systemwartung.

## Eingaben

Das Modell benötigt:

- **Art des KI-/IT-Dienstleisters**: Name, Sitz (EU/Drittland), Geschäftsmodell, Trainingsnutzung personenbezogener Daten?
- **Verarbeitete Mandantendaten**: Welche Kategorien (Beratungsinhalte, Verfahrensdaten, persönliche Mandanteninformationen, Gesundheitsdaten Art. 9 DSGVO)?
- **Zugriffstiefe**: Reiner Speicherzugriff, aktive Datenverarbeitung, KI-gestützte Analyse (Training?)?
- **Bestehende Verträge**: Liegt bereits ein AVV nach Art. 28 DSGVO vor? AV-Klausel in AGB ausreichend?
- **Internationaler Datentransfer**: Daten in Drittland (USA, UK)? Welche Transfermechanismen (SCCs, Angemessenheitsbeschluss)?
- **Berufsträger**: Rechtsanwalt, Arzt, Steuerberater, Notar, Wirtschaftsprüfer?
- **Bisherige Sicherheitsmaßnahmen**: Verschlüsselung, Zugriffskontrollen, Audit-Logs vorhanden?

## Rechtlicher Rahmen

### Primärnormen

- **§ 203 Abs. 1 Nr. 3 StGB**: Rechtsanwälte als Berufsgeheimnisträger; unbefugte Offenbarung von Geheimnissen strafbar (Freiheitsstrafe bis 1 Jahr oder Geldstrafe).
- **§ 203 Abs. 3 Satz 2 StGB** (i.d.F. Gesetz v. 30.10.2017, BGBl. I S. 3618): Mitwirkende Personen (externe IT-/KI-Dienstleister) sind zulässig, wenn Berufsgeheimnisträger sie zur Geheimhaltung verpflichtet; keine strafrechtliche Verantwortlichkeit des Rechtsanwalts mehr für die bloße Weitergabe an vertraglich gebundene IT-Dienstleister.
- **§ 203 Abs. 4 StGB**: Mitwirkende Personen machen sich selbst strafbar, wenn sie das Geheimnis unbefugt offenbaren.
- **§ 43a Abs. 2 BRAO**: Verschwiegenheitspflicht des Rechtsanwalts gegenüber Mandanten; umfasst alle Informationen aus dem Mandatsverhältnis; gilt auch gegenüber Dritten, die in Kanzleiprozesse eingebunden werden.
- **Art. 28 DSGVO**: Auftragsverarbeitung; Pflicht zum schriftlichen Auftragsverarbeitungsvertrag (AVV); Mindestinhalt nach Art. 28 Abs. 3 DSGVO; Unterauftragnehmer genehmigungspflichtig (Art. 28 Abs. 2 DSGVO).
- **Art. 44 ff. DSGVO**: Internationale Datentransfers; Standardvertragsklauseln (SCCs) als primäres Instrument für Drittländer; Transfer Impact Assessment (TIA) bei Hochrisikoländern nach EuGH „Schrems II".
- **§ 2 Abs. 1 BORA**: Konkretisierung der Verschwiegenheitspflicht; Kanzlei-IT-Systeme müssen angemessene Sicherheit gewährleisten.

### Leitentscheidungen

1. BVerfG, Beschl. v. 12.10.2011 – 2 BvR 236/08, BVerfGE 129, 208 Rn. 180–200: Das Mandatsgeheimnis ist verfassungsrechtlich durch Art. 12 Abs. 1 GG und das allgemeine Persönlichkeitsrecht (Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1 GG) geschützt. Die Vertrauensbeziehung zwischen Rechtsanwalt und Mandant setzt absolute Verschwiegenheit voraus; staatliche Eingriffe (Durchsuchungen) bedürfen strenger Verhältnismäßigkeitsprüfung.

2. BGH, Urt. v. 27.04.2017 – I ZR 55/16, NJW 2017, 3308 Rn. 24–35: Im Kontext des Berufsgeheimnisschutzes stellt der BGH klar, dass die Weitergabe von Mandanteninformationen an Dritte ohne ausdrückliche oder konkludente Einwilligung des Mandanten eine Pflichtverletzung darstellt, auch wenn der Dritte zu Geheimhaltung verpflichtet ist – es sei denn, die Weitergabe ist zur Erfüllung des Mandats unbedingt erforderlich.

### Kommentarliteratur

1. Träger, in: Münchener Kommentar zum StGB, 4. Aufl. 2023, § 203 Rn. 80–120: Zu § 203 Abs. 3 Satz 2 StGB n.F. – Voraussetzungen der zulässigen Einbindung mitwirkender Personen: schriftliche Geheimhaltungsverpflichtung, Zweckbindung auf den Mandatsauftrag, faktische Zugangsbeschränkung; keine strafbefreiende Wirkung bei unkontrolliertem Zugang für KI-Trainingsnutzung.

2. Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 43a Rn. 50–90: Zur berufsrechtlichen Dimension der Verschwiegenheitspflicht gegenüber IT-Dienstleistern; Anforderungen an vertragliche Absicherung; Verhältnis von § 43a BRAO zu § 203 StGB; Pflicht zur sorgfältigen Auswahl und Überwachung externer Dienstleister.

## Ablauf

**Schritt 1 – Berufsrechtliche Zulässigkeitsprüfung (§ 203 StGB)**
- Ist der Dienstleister eine „mitwirkende Person" i.S.d. § 203 Abs. 3 Satz 2 StGB?
- Schriftliche Geheimhaltungsvereinbarung vorhanden (Pflicht)?
- Zugang auf das Erforderliche beschränkt (Need-to-know-Prinzip)?
- KI-Training mit Mandantendaten: Kategorisch unzulässig ohne informierte Einwilligung aller Mandanten; keine Ausnahme nach § 203 Abs. 3 StGB.

**Schritt 2 – Berufsrechtliche Compliance (§ 43a Abs. 2 BRAO)**
- Mandant informiert über Einbindung externer Dienste?
- Ggf. Einwilligung des Mandanten (bei sensiblen Verfahrensdaten empfohlen)?
- Sorgfältige Auswahl des Dienstleisters dokumentieren (§ 26 BORA: angemessene Sicherheit).

**Schritt 3 – Datenschutzrechtliche Prüfung (Art. 28 DSGVO)**
- AVV abgeschlossen? Mindestinhalt nach Art. 28 Abs. 3 DSGVO prüfen: Gegenstand, Dauer, Art, Zweck, Kategorien, Pflichten/Rechte.
- Unterauftragnehmer-Liste aktuell? Genehmigung nach Art. 28 Abs. 2 DSGVO (allgemein oder spezifisch)?
- Audit-Rechte vertraglich gesichert (Art. 28 Abs. 3 lit. h DSGVO)?

**Schritt 4 – Internationale Datentransfers (Art. 44 ff. DSGVO)**
- Sitz des Dienstleisters und aller Rechenzentren bestimmen.
- Bei Drittlandtransfer: Transfermechanismus (SCCs, Angemessenheitsbeschluss)?
- Transfer Impact Assessment (TIA) erstellen: Rechtslage im Empfängerland, Zugriffsrechte staatlicher Behörden (CLOUD Act, FISA 702 bei US-Diensten)?
- Ggf. zusätzliche technische Maßnahmen (Ende-zu-Ende-Verschlüsselung, EU-Only-Hosting).

**Schritt 5 – Technisch-organisatorische Maßnahmen (TOMs)**
- Verschlüsselung at-rest und in-transit (Art. 32 Abs. 1 lit. a DSGVO)?
- Zugangsprotokolle (Audit-Logs) für Mandantendaten?
- Löschkonzept nach Auftragsende?
- Incident-Response-Verfahren bei Datenpannen des Dienstleisters?

**Schritt 6 – Dokumentation und laufende Überwachung**
- Verfahrensverzeichnis nach Art. 30 DSGVO aktualisieren.
- Jährliche Überprüfung des Dienstleisters (Zertifizierungen, Sicherheitsnachweise).
- Geheimhaltungsvereinbarungen und AVV archivieren.

## Ausgabeformat

- **Prüfmemo** (intern): Berufsrechtliche und datenschutzrechtliche Zulässigkeit des konkreten KI-/IT-Dienstleisters.
- **AVV-Checkliste** (tabellarisch): Vorhandene vs. fehlende Klauseln nach Art. 28 Abs. 3 DSGVO.
- **TIA-Grundgerüst**: Länderspezifische Risikoeinschätzung für Drittlandtransfers.
- **Geheimhaltungsverpflichtung** (Vorlage): Vertragsmuster für mitwirkende Personen nach § 203 Abs. 3 Satz 2 StGB.

## Beispiel

**Sachverhalt**: Rechtsanwalt R möchte einen US-amerikanischen KI-Dienst (Serverstandort: Virginia, USA) für die Analyse von Vertragsunterlagen aus einem laufenden M&A-Mandat nutzen. Der Anbieter schließt in seinen AGB „Training mit Nutzerdaten nicht aus".

**Gutachtenstil**:

*§ 203 StGB*: Der Einsatz des US-KI-Dienstes setzt voraus, dass der Anbieter als „mitwirkende Person" i.S.d. § 203 Abs. 3 Satz 2 StGB qualifiziert wird und eine schriftliche Geheimhaltungsvereinbarung vorliegt. Die AGB-Klausel zum KI-Training macht den Dienst für die Verarbeitung von Mandantendaten unzulässig, da ein unkontrollierter Einsatz des Geheimnisses außerhalb des Mandatszwecks stattfinden würde; Strafbarkeit nach § 203 Abs. 1 Nr. 3 StGB droht (Träger, MüKoStGB, 4. Aufl. 2023, § 203 Rn. 95).

*§ 43a Abs. 2 BRAO*: Ohne informierte Einwilligung des Mandanten und ohne vertragliche Sicherstellung der Nicht-Trainingsnutzung liegt eine berufsrechtliche Pflichtverletzung vor (Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 43a Rn. 68).

*Art. 28/44 DSGVO*: Ein AVV nach Art. 28 DSGVO ist abzuschließen; wegen des US-Transfers sind SCCs erforderlich, ergänzt durch TIA angesichts FISA 702-Zugriffsmöglichkeiten. EU-Only-Hosting oder Ende-zu-Ende-Verschlüsselung sind als Schutzmaßnahmen zu vereinbaren.

*Ergebnis*: Der Dienst ist in der beschriebenen Form nicht einsetzbar. Alternativ: EU-basierter Anbieter mit AVV, EU-Hosting und vertraglichem Trainingsverbot.

## Risiken und typische Fehler

- **KI-Training mit Mandantendaten**: Unzulässig ohne ausdrückliche Einwilligung jedes Mandanten; AGB-Klausel schließt Training nicht aus – Anbieter sorgfältig prüfen.
- **Fehlende Geheimhaltungsvereinbarung**: § 203 Abs. 3 Satz 2 StGB entbindet nur bei schriftlicher Verpflichtung; ohne Vertrag: Strafbarkeit des Rechtsanwalts möglich.
- **AVV-Lücken**: Viele Cloud-Dienste bieten Standard-AVV an, die Unterauftragnehmer-Änderungen ohne spezifische Genehmigung erlauben – Risiko nach Art. 28 Abs. 2 DSGVO.
- **TIA vergessen**: Ohne TIA bei US-Diensten: Verstoß gegen Art. 44 ff. DSGVO; Bußgeld bis 20 Mio. EUR / 4 % Jahresumsatz (Art. 83 Abs. 5 DSGVO).
- **Keine Audit-Logs**: Fehlt ein lückenloses Zugangsprotokoll, kann im Schadensfall nicht nachgewiesen werden, wer auf Mandantendaten zugegriffen hat.
- **Berufsrecht und Strafrecht kumulieren**: § 43a BRAO-Verstöße führen zu Berufsrechtssanktionen (§§ 113 ff. BRAO); § 203 StGB begründet Strafbarkeit; beide Ebenen unabhängig voneinander.

## Quellenpflicht

Alle Aussagen sind nach `references/zitierweise.md` zu belegen. Mindestens zwei Rspr.-Belege im BGH-Stil, zwei Kommentarbelege im Bearbeiter-Stil. Bei Hinweisen zur KI-Nutzung ohne gesicherte Rspr. ausdrücklich auf Kommentarliteratur und EDSA-Leitlinien (insb. EDSA-Leitlinien 07/2020 zu Art. 46 DSGVO) verweisen.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Anpassungen von § 203 StGB, neuen BRAO-Berufsordnungsregeln zur KI-Nutzung, EU-KI-VO-Umsetzungsrechtsakten sowie Änderungen am EU-US Data Privacy Framework (DPF).

**Querverweise:**
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — AVV-Prüfung für den konkreten KI-Dienstleister
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Vollständige TIA-Methodik bei US- oder Drittland-KI-Diensten
- **ki-richtlinie-kanzleien** (geplant ab v3.3.0): Kanzleiweite KI-Nutzungsrichtlinien, Rollen und Freigabeprozesse für den Einsatz von KI-Werkzeugen in der Rechtsberatung. Querverweis sobald Plugin verfügbar.

## Aktuelle Rechtsprechung (v14.2)

- BGH, Urt. v. 15.06.2021 — AnwSt (R) 1/21, NJW 2021, 2883 Rn. 28: Berufsgeheimnis nach § 43a Abs. 2 BRAO gilt für alle dem Anwalt anvertrauten Tatsachen — Eingabe in KI-System ist Offenbarung an Dritten, die berufsrechtlicher Rechtfertigung nach § 43e BRAO bedarf.
- BGH, Urt. v. 10.11.2020 — 5 StR 264/20, NStZ 2021, 156 Rn. 18: § 203 Abs. 4 StGB (n.F.) setzt voraus, dass der KI-Dienstleister über die strafrechtliche Tragweite der Verschwiegenheitspflicht belehrt wurde; fehlende Belehrung kann strafrechtliche Mitverantwortung begründen.
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 182: US-Anbieter unterliegen strukturellen behördlichen Zugriffsrechten (FISA, CLOUD Act); Mandatsdaten bei US-KI-Diensten sind drittlandrechtlich und berufsrechtlich doppelt zu bewerten.
- BVerfG, Beschl. v. 12.10.2021 — 2 BvR 1368/21, NJW 2022, 55 Rn. 44: Berufsgeheimnis ist verfassungsrechtlich geschützt (Art. 12 GG); IT-Systeme, die Mandatsdaten verarbeiten, müssen den Schutz strukturell sicherstellen.

## Triage zu Beginn

1. Welche Mandatsdaten sollen verarbeitet werden? (personenbezogen oder nur nicht-personenbezogen)
2. Wer ist der KI-Anbieter? (EU/EWR oder Drittland)
3. Ist eine AVV nach Art. 28 DSGVO und eine berufsrechtliche Verschwiegenheitsverpflichtung vorhanden?
4. Werden Mandatsdaten zu Trainingszwecken des Anbieters verwendet? (no-training-Check)

## Output-Template — Mandantendaten-KI-Prüfvermerk

**Adressat:** Kanzlei intern / DSB — Tonfall: sachlich-juristisch

```
Mandantendaten-KI-Prüfvermerk [DATUM]
Kanzlei: [NAME] | Beruf: [BERUF]
KI-Anbieter: [NAME, SITZ]
Produkt: [NAME]

Datenschutz (AVV Art. 28 DSGVO):
AVV vorhanden: ja / nein
TOM-Anlage: vorhanden / fehlend
Drittlandtransfer: ja (TIA?) / nein

Berufsrecht (§ 43e BRAO / Parallelnorm):
Verschwiegenheitsklausel (Textform): ja / nein
Belehrung §§ 203/204 StGB: ja / nein
No-training: ja / nein / unklar

Ergebnis:
DSGVO: GRUEN / GELB / ROT
Berufsrecht: GRUEN / GELB / ROT
Empfehlung: freigegeben / Nachverhandlung erforderlich / nicht freigegeben
```
