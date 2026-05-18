---
name: dsar-response
description: >
  Bearbeitung von Betroffenenanfragen nach Art. 15–22 DSGVO: geführter Ablauf von
  Eingangsklassifikation über Identitätsprüfung und Systemabfrage bis zum
  Antwortentwurf. Fristen nach Art. 12 Abs. 3 DSGVO werden automatisch berechnet.
  Ausnahmen nach §§ 34, 35 BDSG werden geprüft.
language: de
triggers:
  - "Betroffenenanfrage"
  - "Auskunftsanfrage"
  - "DSAR"
  - "Löschantrag"
  - "Widerspruch"
  - "Art. 15"
  - "Art. 17"
  - "Art. 21"
  - "Datenkopie"
---

# Betroffenenanfragen – Art. 15–22 DSGVO

## Zweck

Strukturierter Workflow zur vollständigen Bearbeitung eingehender Betroffenenanfragen. Vom ersten Eingang bis zum versandfertigen Antwortentwurf: Klassifikation, Fristberechnung, Identitätsprüfung, Systemabfrage, Ausnahmenprüfung und formgerechte Antwort. Alle Fristen werden aus dem Eingangsdatum berechnet; Verlängerungsoptionen nach Art. 12 Abs. 3 Satz 2 DSGVO werden geprüft.

## Eingaben

- Art der Anfrage (Auskunft, Berichtigung, Löschung, Einschränkung, Datenportabilität, Widerspruch, Einwilligungswiderruf)
- Eingangsdatum der Anfrage
- Name, E-Mail-Adresse oder sonstige Angaben des Antragstellers
- Praxisprofil aus `CLAUDE.md` (Systemliste, Identifikationsstandard, DSB)
- Optional: Dokument oder E-Mail der Anfrage

## Ablauf

1. **Eingangsklassifikation.**
   - Anfrage-Art bestimmen: Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung (Art. 18), Datenportabilität (Art. 20), Widerspruch (Art. 21), Einwilligungswiderruf (Art. 7 Abs. 3)?
   - Mehrfachanfragen erkennen (häufig: kombinierter Auskunfts- und Löschantrag).
   - Handelt es sich um ein Auskunftsersuchen nach IFG/UIG statt DSGVO? (Abgrenzung bei öffentlichen Stellen)

2. **Fristberechnung.**
   - Grundfrist: 1 Monat ab Eingang, Art. 12 Abs. 3 Satz 1 DSGVO.
   - Verlängerung um bis zu 2 Monate möglich bei Komplexität oder Vielzahl von Anfragen, Art. 12 Abs. 3 Satz 2 DSGVO.
   - **Verlängerung erfordert Mitteilung an Betroffenen innerhalb der 1-Monatsfrist** mit Begründung.
   - Fristende berechnen: [Eingangsdatum + 1 Monat] = [Datum]. Verlängerung bis [Datum + 2 Monate].
   - Wochenenden und Feiertage: § 193 BGB, Art. 3 Abs. 4 EuGH-Verfahrensordnung (natürliches Monatsende).

3. **Identitätsverifikation.**
   - Ist die Identität des Antragstellers ausreichend nachgewiesen?
   - Standard aus `CLAUDE.md` anwenden.
   - Art. 12 Abs. 6 DSGVO: Bei begründeten Zweifeln kann zusätzliche Information angefordert werden – aber **keine unverhältnismäßige Identifikationshürde** (vgl. EDSA-Leitlinien 01/2022 zu DSAR, Abschn. 3.2).
   - Identitätsprüfung bei Online-Diensten: Konto-Login-Bestätigung oder sichere Alternative; keine Ausweis-Kopien ohne konkreten Zweck (Daten dürfen nicht für andere Zwecke genutzt werden).

4. **Systemabfrage.**
   - Alle relevanten Systeme aus der Systemliste in `CLAUDE.md` durchgehen.
   - Kategorien: CRM, ERP, E-Mail-Archiv, Protokolldateien, Backups, Cloud-Dienste, Sub-AV-Systeme.
   - Für jeden Treffer: Datenkategorie, Verarbeitungszweck, Rechtsgrundlage, Empfänger, Speicherfrist notieren.
   - Keine eigenmächtige Löschung vor Abschluss der Prüfung (Dokumentationspflicht Art. 5 Abs. 2 DSGVO).

5. **Ausnahmenprüfung.**
   - § 34 BDSG (Auskunftsverweigerung, z.B. zur Abwehr von Straftaten, Geschäftsgeheimnisse)
   - § 35 BDSG (eingeschränkte Löschung, z.B. gesetzliche Aufbewahrungsfristen)
   - Art. 17 Abs. 3 DSGVO (kein Löschrecht bei gesetzlicher Aufbewahrungspflicht, Geltendmachung/Verteidigung von Rechtsansprüchen)
   - Art. 15 Abs. 4 DSGVO (Datenkopie darf Rechte Dritter nicht beeinträchtigen)
   - Berufsgeheimnisschutz bei Kanzleien / medizinischen Einrichtungen (§ 203 StGB)
   - Für jede angewandte Ausnahme: konkrete Norm und Begründung dokumentieren.

6. **Antwortentwurf erstellen.**
   - Adressierung korrekt (Name, Adresse aus Anfrage).
   - Positiv-Auskunft oder begründete Ablehnung/Einschränkung.
   - Bei Auskunft: vollständige Informationen nach Art. 15 Abs. 1 DSGVO (alle 9 Ziffern) + ggf. Datenkopie Art. 15 Abs. 3 DSGVO.
   - Hinweis auf Beschwerderecht bei Aufsichtsbehörde (Art. 77 DSGVO) in jedem Ablehnungsschreiben.
   - Hinweis auf Klagerecht Art. 79 DSGVO.
   - Keine Gebühren für Erstauskunft; bei offenkundig unbegründeten oder exzessiven Folgeanfragen: angemessenes Entgelt oder Ablehnung nach Art. 12 Abs. 5 DSGVO.

7. **Dokumentation.**
   - Eingang, Frist, Bearbeitungsschritte, Ausnahmen, Ergebnis im Datenschutzregister erfassen.
   - Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht).

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 12 Abs. 3, 4, 5, 6 DSGVO (Fristen, Kosten, Identitätsprüfung)
- Art. 15 DSGVO (Auskunftsrecht, Inhalt)
- Art. 16 DSGVO (Berichtigung)
- Art. 17 DSGVO (Löschung, Ausnahmen)
- Art. 18 DSGVO (Einschränkung)
- Art. 20 DSGVO (Datenportabilität)
- Art. 21 DSGVO (Widerspruch)
- Art. 77 DSGVO (Beschwerderecht Aufsichtsbehörde)
- §§ 34, 35 BDSG (Auskunfts- und Löscheinschränkungen)
- EuGH, Urt. v. 26.10.2023 – C-307/22 (FT/BFI), NJW 2023, 3548 – Umfang Datenkopie Art. 15 Abs. 3 DSGVO `[Modellwissen – prüfen]`
- BGH, Urt. v. 15.06.2021 – VI ZR 576/19, NJW 2021, 3179 – Auskunftsumfang Art. 15 DSGVO im Arbeitsrecht
- Kamlah, in: Plath, DSGVO/BDSG, 3. Aufl. 2021, Art. 15 Rn. 1 ff.
- Dix, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 15 Rn. 1 ff.
- Schulze, in: BeckOK DSGVO, 16. Ed. (Stand 01.11.2024), Art. 15 Rn. 1 ff.

## Ausgabeformat

1. **Kopfzeile:** Anfrage-Art, Eingangsdatum, Fristdaten (1 Monat / Verlängerung), Bearbeiter
2. **Klassifikations-Ergebnis**
3. **Identitätsverifikations-Status**
4. **Systemabfrage-Ergebnisse** (Tabelle: System | Datenfund | Zweck | Rechtsgrundlage | Frist)
5. **Ausnahmenprüfung** (tabellarisch: Norm | anwendbar | Begründung)
6. **Antwortentwurf** (druckreif, Briefkopf-Format, ohne Plugin-Kommentare im Text)
7. **Dokumentations-Eintrag für Datenschutzregister**

## Beispiel (Auskunftsanfrage)

**Sachverhalt:** Frau M. stellt am 03.06.2024 per E-Mail eine Auskunftsanfrage gemäß Art. 15 DSGVO und bittet zusätzlich um Herausgabe einer Datenkopie (Art. 15 Abs. 3 DSGVO). Kein Kundenkonto, Identität nur per E-Mail bekannt.

**Frist:** Grundfrist endet am 03.07.2024. Verlängerung (Art. 12 Abs. 3 Satz 2 DSGVO) bis 03.09.2024 möglich; Mitteilung an Frau M. spätestens 03.07.2024 erforderlich.

**Identität:** E-Mail-Adresse allein reicht bei reinen Newsletter-Abonnenten aus, wenn keine weiteren personenbezogenen Daten verarbeitet werden. Vgl. EDSA-Leitlinien 01/2022, Abschn. 3.2: Verhältnismäßigkeit der Verifikation.

**Datenkopie (Art. 15 Abs. 3 DSGVO):** Der EuGH hat in EuGH, Urt. v. 26.10.2023 – C-307/22 (FT/BFI) festgestellt, dass Art. 15 Abs. 3 DSGVO eine vollständige Kopie der verarbeiteten personenbezogenen Daten (nicht nur eine Zusammenfassung) umfasst. `[Modellwissen – prüfen]` Sofern Rechte Dritter tangiert (Art. 15 Abs. 4 DSGVO), sind betroffene Passagen zu schwärzen.

**Ausnahmen:** § 34 BDSG: keine einschlägigen Tatbestände. Art. 17 Abs. 3 DSGVO: nicht relevant (kein Löschantrag). Keine weiteren Ausnahmen erkennbar.

**Antwortentwurf-Auszug:**
> Sehr geehrte Frau M., vielen Dank für Ihre Anfrage vom 03.06.2024. Gemäß Art. 15 Abs. 1 DSGVO teilen wir Ihnen mit, dass wir folgende personenbezogene Daten über Sie verarbeiten: [Auflistung]. Die Verarbeitung erfolgt zu folgenden Zwecken: [Zwecke], auf Grundlage von [Rechtsgrundlagen]. Im Übrigen stehen Ihnen die in Art. 16–21 DSGVO genannten Rechte zu. Sollten Sie mit unserer Antwort nicht zufrieden sein, steht Ihnen das Beschwerderecht bei der zuständigen Aufsichtsbehörde ([LfDI/BfDI]) gemäß Art. 77 DSGVO sowie das Klagerecht nach Art. 79 DSGVO zu.

## Risiken / typische Fehler

- **Fristversäumnis:** Art. 12 Abs. 4 DSGVO – Untätigkeit gilt als Ablehnung, eröffnet Klagerecht Art. 79 DSGVO und Beschwerde Art. 77 DSGVO. Fristmitteilung bei Verlängerung ist eigenständige Pflicht.
- **Unvollständige Systemabfrage:** Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht) verpflichtet zu nachweisbarer vollständiger Prüfung. Backup-Systeme und Archive werden häufig vergessen.
- **Übermäßige Identitätshürde:** Passverlangen ohne Anlass verletzt Art. 12 Abs. 6 DSGVO; EDSA warnt vor übermäßiger Identifizierung als faktischem Abwehrmittel.
- **§ 34 BDSG-Ausnahmen ohne Dokumentation:** Ausnahme muss einzelfallbezogen begründet sein; pauschale Verweigerung „wegen Geschäftsgeheimnisse" ist nicht ausreichend.
- **Datenkopie-Format:** Art. 15 Abs. 3 DSGVO verlangt keine bestimmte Form; ein „strukturiertes, maschinenlesbares Format" ist bei Art. 20 DSGVO (Portabilität) vorgeschrieben, nicht bei Art. 15 Abs. 3 DSGVO – Verwechslung vermeiden.
- **Verjährung von Schadensersatzansprüchen:** BGH, Urt. v. 12.07.2022 – VI ZR 7/21, NJW 2022, 3071: Art. 82 DSGVO-Schadensersatz setzt einen konkreten Schaden voraus, aber schon Kontrollverlust kann genügen. Fehlerhaft bearbeitete Betroffenenanfragen begründen Haftungsrisiko.
