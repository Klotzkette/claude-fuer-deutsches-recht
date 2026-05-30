---
name: cowork-cloud-kollaboration-drafting
description: "Mandantengeheimnis-konformes Drafting in der Cloud (Claude Cowork; Office 365; Google Workspace). Rechtlicher Rahmen § 43a Abs. 2 BRAO; § 203 StGB; § 26 BORA und Art. 28 DSGVO. Auftragsverarbeitungsvertrag ist Voraussetzung. Sensible Daten: Mandantenname; Aktenzeichen; Sachverhalt. Pseudonymisierung im Entwurf; Mandantendaten erst in finaler Fassung. Versionierung. Zwei-Faktor-Authentifizierung. Mit Pitfall-Liste zu WhatsApp; E-Mail und Cloud ohne Auftragsverarbeitungsvertrag."
---

# Cowork und Cloud-Kollaboration im Drafting

## Zweck

Cloud-Tools wie Claude Cowork, Microsoft Office 365 oder Google Workspace sind aus dem juristischen Drafting nicht mehr wegzudenken. Sie ermöglichen schnelle Zusammenarbeit, Versionierung, KI-Unterstützung. Sie sind aber zugleich der häufigste Angriffsvektor auf das Mandantengeheimnis. Dieser Skill klärt den rechtlichen Rahmen und liefert eine praktische Vorgehensweise für sicheres Drafting in der Cloud.

Er ist nicht nur Datenschutzbelehrung. Er gibt konkrete Drafting-Empfehlungen: Welche Daten dürfen in welcher Phase in welches Tool. Wann pseudonymisieren. Wann erst nach Abschluss des Drafts die Mandantendaten einfügen.

## Eingaben

- Genutzte Cloud-Tools in Ihrer Kanzlei
- Bestehende Auftragsverarbeitungsverträge mit den Anbietern
- Mandatscharakter (Standardmandat, Hochrisiko, internationale Beteiligung)
- Geräteumfeld (kanzleieigene Geräte, BYOD, Remote)
- Verteilungskreis (interne Co-Drafter, externe Kolleginnen, Mandant)

## Rechtlicher und methodischer Rahmen

- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht der Anwältin und des Anwalts.
- § 203 Abs. 1 Nr. 3 StGB: Strafbarkeit der Verletzung von Privatgeheimnissen.
- § 203 Abs. 3 und Abs. 4 StGB: Mitwirkende Personen und externe Dienstleister; Voraussetzungen der zulässigen Einbindung.
- § 26 BORA: Sorgfalt bei Mitarbeiterinnen und Mitarbeitern sowie Dritten.
- Art. 5 DSGVO: Grundsätze (Rechtmäßigkeit, Zweckbindung, Datenminimierung, Integrität und Vertraulichkeit).
- Art. 28 DSGVO: Auftragsverarbeitung; schriftlicher Vertrag mit allen Pflichtinhalten erforderlich.
- Art. 32 DSGVO: Sicherheit der Verarbeitung (Pseudonymisierung; Verschlüsselung; Belastbarkeit; Wiederherstellbarkeit; regelmäßige Überprüfung).
- Art. 44 ff. DSGVO: Drittlandübermittlungen; insbesondere Schrems-II-Risiken bei US-Anbietern.
- BSI-Grundschutz und Empfehlungen der Bundesrechtsanwaltskammer zur Nutzung von Cloud-Diensten in Kanzleien.

## Ablauf / Checkliste

1. **Vor Tool-Nutzung: Auftragsverarbeitungsvertrag prüfen.** Liegt ein schriftlicher Auftragsverarbeitungsvertrag nach Art. 28 DSGVO vor? Sonst keine Mandantendaten in dieses Tool.
2. **Datenklassifikation klären.** Welche Information ist sensibel? Mandantenname, Aktenzeichen, Sachverhalt, Gegenseite. Auch eine harmlos wirkende Mandatsbezeichnung kann den Identifizierungskreis offenbaren.
3. **Pseudonymisierung im Drafting-Prozess.** Während der Konzept- und Klauselarbeit: "Mandant", "Mandantin", "Gegenseite", "Anlage 1" statt Klarnamen. Konkrete Beträge ggf. durch Platzhalter ersetzen.
4. **Erst in finaler Fassung die Klarnamen einsetzen.** Vorher Mandantendaten in einer geschützten Umgebung halten (lokal oder in einer kanzleieigenen, klassifizierten Cloud).
5. **Versionsführung mit klaren Stempeln.** v0 lokal, v1 Cloud-Entwurf pseudonymisiert, v2 mit Mandantendaten in geschützter Umgebung, v-final unterschriftsreif.
6. **Zwei-Faktor-Authentifizierung verbindlich.** Für alle Cloud-Dienste; ohne Ausnahme.
7. **Geräte- und Pfadhygiene.** Keine Mandantendaten auf privaten Cloud-Speichern, nicht in privaten Mail-Konten, nicht auf privaten Handys ohne Mobile Device Management.
8. **Berechtigungskonzept Cowork-Räume.** Nur die Personen mit Zugang, die Zugang brauchen. Externe Drafter aus dem Cowork-Raum entfernen, sobald ihre Phase endet.
9. **Logging und Audit.** Aktivitätsprotokolle aktivieren; bei Bedarf Audit prüfen.
10. **Notfallplan.** Was ist zu tun bei Datenleck (Art. 33, 34 DSGVO Meldepflichten innerhalb von 72 Stunden)?

### Sensitivitäts-Matrix

| Datenkategorie | Sensitivität | Maßnahme |
|---|---|---|
| Mandantenname | hoch | Pseudonym im Entwurf |
| Aktenzeichen | hoch | nur in geschützter Umgebung |
| Sachverhalt mit personenbeziehbaren Daten | hoch | Pseudonym; finale Fassung lokal |
| Klauselrohling ohne Bezug | niedrig | unbedenklich in Cloud |
| Vergleichsbetrag | mittel | Platzhalter im Entwurf |
| Strafrechtliche Vorwürfe | sehr hoch | nur Onpremise oder klassifizierte Cloud |
| Gesundheitsdaten (Art. 9 DSGVO) | sehr hoch | nur Onpremise oder klassifizierte Cloud |

### Pseudonymisierungs-Konventionen

```
Mandant     -> "Mandant" oder "M"
Gegenseite  -> "Gegenseite" oder "G"
Aktenzeichen -> "AZ-001"
Datum konkret -> "TT.MM.JJJJ" als Platzhalter
Betrag konkret -> "[Betrag]" oder "X Euro"
Adressen   -> "Anschrift M" / "Anschrift G"
```

## Typische Drafting-Fehler

- **WhatsApp, private E-Mail, Privat-Cloud.** Mandantendaten ohne Auftragsverarbeitungsvertrag und ohne Verschlüsselung sind ein Bruch von § 203 StGB.
- **Cloud-Anbieter ohne Auftragsverarbeitungsvertrag.** Selbst kostenlose Tools verarbeiten Daten; ohne Auftragsverarbeitungsvertrag tabu.
- **Klarnamen im Cowork-Raum von Anfang an.** Auch wenn der Anbieter geprüft ist, gehört das in die geschützte Umgebung.
- **Versionsdurcheinander.** Ohne klare Versionsstempel werden Entwürfe mit Klarnamen versehentlich extern geteilt.
- **Externe Drafter behalten Zugriff.** Nach Projektende vergessene Berechtigungen sind ein klassischer Fehler.
- **Keine Zwei-Faktor-Authentifizierung.** Passwort allein ist 2026 kein Schutz mehr.
- **Drittlandübermittlung übersehen.** Bei US-Cloud-Anbietern Schrems-II-Aspekte und Standardvertragsklauseln prüfen.
- **Bring-your-own-Device ohne Mobile Device Management.** Mandantendaten auf privaten Geräten ohne kontrollierten Trennungslogik.

## Ausgabeformat

- Sensitivitäts-Einschätzung für das konkrete Mandat.
- Empfehlung der Tool-Wahl pro Drafting-Phase.
- Pseudonymisierungsplan für Entwurfsphase.
- Checkliste vor Versand: Klarnamen ersetzt? Zwei-Faktor aktiv? Cowork-Berechtigungen aktuell?

## Beispiele

### Beispiel Cowork-Konzept für Vertragsdraft

```
Phase 1 (Konzept):
- Klauselbausteine in Cowork, vollständig pseudonymisiert.
- Mandant = "M", Gegenseite = "G", Beträge = "[Betrag]".

Phase 2 (Erstentwurf):
- Pseudonymisierter Entwurf in Cowork.
- Querverweise per Word-Formatvorlagen.

Phase 3 (Mandantenfreigabe):
- Übernahme in lokale Word-Umgebung der Kanzlei.
- Klarnamen einsetzen, mit Mandant abstimmen.

Phase 4 (Versand an Gegenseite):
- Versand aus klassifizierter Kanzleiumgebung über beA, AnwaltsCloud oder verschlüsselte E-Mail.
- Metadaten vor Versand entfernen.
```

### Beispiel Verstoss-Szenario

Ein Anwalt schickt einen NDA-Entwurf für einen prominenten Mandanten über sein privates Gmail-Konto an einen externen Steuerberater. Folge: Verstoß gegen § 203 StGB (kein zulässiges Outsourcing nach § 203 Abs. 3 StGB), § 43a BRAO und Art. 32 DSGVO. Strafrechtliches Risiko, berufsrechtliche Maßnahme, Meldepflicht nach Art. 33, 34 DSGVO.

## Querverweise

- `word-formatvorlagen-querverweise-track-changes` für sichere Word-Hygiene vor Cloud-Upload
- `revisions-prozess-redlines-comparison` für Versionsführung
- `orientierung-drafting-triage` für die Anfangsbewertung der Risikolage
- `geheimhaltung-nda-vertraulichkeit` für NDA-Klauseln, die das selbe Schutzgut adressieren

## Quellen (Stand 05/2026)

- § 43a Abs. 2 BRAO; § 203 Abs. 1 Nr. 3, Abs. 3 und Abs. 4 StGB; § 26 BORA; gesetze-im-internet.de und brak.de.
- Art. 5, 28, 32, 33, 34, 44 ff. DSGVO; dsgvo-gesetz.de.
- Empfehlungen der Bundesrechtsanwaltskammer zur Cloud-Nutzung: vom Nutzer zu prüfen, brak.de.
- Schrems-II-Urteil EuGH und Folgepraxis: vom Nutzer zu verifizieren (EuGH, Urt. v. 16. Juli 2020, Rs. C-311/18).
- `references/zitierweise.md` für Belegpflicht.
