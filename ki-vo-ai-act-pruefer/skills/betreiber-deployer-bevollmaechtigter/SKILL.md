---
name: betreiber-deployer-bevollmaechtigter
description: "Unternehmen oder Behörde setzt ein Hochrisiko-KI-System, GPAI-System oder allgemeinen Chatbot ein und fragt nach Betreiberpflichten. Art. 26 KI-VO: bestimmungsgemaesse Verwendung, menschliche Aufsicht, Eingabedaten, Protokolle, Vorfallmeldungen, Informationspflichten; Art. 27 Grundrechte-Folgenabschaetzung. Besonderer Fokus: Off-label-Nutzung durch Mitarbeitende, Zweckaenderung, Art. 25 Anbieterwerden, Governance für allgemeine Chatbots in Hochrisiko-Kontexten. Output: Betreiber-Compliance-Checkliste mit Fehlgebrauchs- und Re-Evaluationsplan im Ki Vo Ai Act Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Betreiber-Pflichten (Deployer) — Art. 26 und 27 KI-VO

## Arbeitsbereich

Unternehmen oder Behörde setzt ein Hochrisiko-KI-System, GPAI-System oder allgemeinen Chatbot ein und fragt nach Betreiberpflichten. Art. 26 KI-VO: bestimmungsgemaesse Verwendung, menschliche Aufsicht, Eingabedaten, Protokolle, Vorfallmeldungen, Informationspflichten; Art. 27 Grundrechte-Folgenabschaetzung. Besonderer Fokus: Off-label-Nutzung durch Mitarbeitende, Zweckaenderung, Art. 25 Anbieterwerden, Governance für allgemeine Chatbots in Hochrisiko-Kontexten. Output: Betreiber-Compliance-Checkliste mit Fehlgebrauchs- und Re-Evaluationsplan. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Art. 5 Verbote ab 02.02.2025, Art. 51-55 GPAI ab 02.08.2025, Hochrisiko Anhang III ab 02.08.2026, Hochrisiko Anhang I ab 02.08.2027, schwerwiegender Vorfall 15 Tage / 2 Tage (Tod).
- Tragende Normen verifizieren: KI-VO (EU 2024/1689) Art. 3, 5 (Verbote), 6 (Hochrisiko), 8-15 (Anforderungen), 16, 26 (Pflichten Anbieter/Betreiber), 50 (Transparenz), 51-55 (GPAI), 73, 99 (Sanktionen) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter, Betreiber, Importeur, Händler, Marktüberwachungsbehörde (BNetzA/BMDV), benannte Stelle, EU-AI-Office, AI Board.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung Art. 47, technische Dokumentation Anhang IV, Risikomanagement-System Art. 9, Datengovernance Art. 10, FRIA (Fundamental Rights Impact Assessment) Art. 27, EU-Datenbank-Registrierung Art. 49 — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Betreiber sind natürliche oder juristische Personen, Behörden, Einrichtungen oder sonstige Stellen, die ein KI-System unter eigener Verantwortung verwenden. Dieser Skill prüft die Pflichten beim Einsatz von Hochrisiko-KI und ergänzt einen Governance-Check für allgemeine Chatbots/GPAI-Systeme, die intern zweckwidrig für Hochrisiko-Kontexte genutzt werden könnten.

## Pflicht 1 — Bestimmungsgemäße Verwendung

Betreiber müssen Hochrisiko-KI-Systeme nach der Gebrauchsanweisung des Anbieters verwenden.

Prüffragen:
- Liegt die Gebrauchsanweisung vor und ist sie intern umgesetzt?
- Ist der interne Use Case vom Anbieterzweck gedeckt?
- Werden Prompt-Vorlagen, Workflows, Rollenrechte oder Schnittstellen so gestaltet, dass keine unzulässige Zweckänderung entsteht?
- Gibt es ein Freigabeverfahren für neue KI-Use-Cases?

## Sonderthema — Mitarbeitende nutzen ein allgemeines KI-Tool hochriskant

Wenn Mitarbeitende ein allgemeines Tool entgegen der Zweckbestimmung für Personal, Kredit, Bildung, Verwaltung, Justiz oder andere Anhang-III-Kontexte einsetzen, prüfe die Organisationsverantwortung:

| Befund | Einordnung |
|---|---|
| Klare Richtlinie, Schulung, Rollenrechte, Logging, Sperren; isolierter Verstoß | Compliance-/Incident-Thema; Nutzung beenden, dokumentieren, nachschulen, ggf. Daten/Output entfernen |
| Fachabteilung nutzt es wiederholt und Führung weiß davon | tatsächlicher Betreiberzweck kann kippen; `hochrisiko-art-6-abs-2-anhang-iii` neu prüfen |
| Tool ist technisch offen und Hochrisiko-Nutzung naheliegend | vorhersehbarer Fehlgebrauch; Kontrollen, Warnungen, Freigaben und Re-Evaluation erforderlich |
| Betreiber ändert Zweck oder System wesentlich | `anbieter-werden-art-25` prüfen; Anbieterpflichten können ausgelöst werden |

Mindestmaßnahmen:
- KI-Richtlinie mit erlaubten und verbotenen Use Cases
- KI-Kompetenz/Schulung nach Art. 4
- Rollen- und Zugriffskonzept für sensible Bereiche
- Prompt- und Datenklassifizierungsregeln
- Logging/Audit für sensible Workflows
- Freigabeprozess für neue KI-Use-Cases
- Re-Evaluation bei Zweckänderung, Modellwechsel, neuer Integration oder auffälliger Nutzung

## Pflicht 2 — Menschliche Aufsicht

Betreiber müssen die vom Anbieter vorgesehenen Aufsichtsmaßnahmen tatsächlich umsetzen.

Prüffragen:
- Sind Aufsichtspersonen benannt und geschult?
- Können sie Output verstehen, kritisch prüfen, übersteuern oder stoppen?
- Ist Aufsicht mehr als nur formale Abzeichnung?
- Gibt es Eskalationsregeln bei Fehlern, Bias, Halluzinationen, Drift oder ungewöhnlichen Outputs?

## Pflicht 3 — Eingabedaten und Nutzungskontext

Wenn Betreiber Eingabedaten kontrollieren, müssen diese relevant und repräsentativ für den vorgesehenen Zweck sein.

Prüffragen:
- Welche Eingabedaten werden vom Betreiber bereitgestellt?
- Sind personenbezogene, vertrauliche oder besondere Daten betroffen?
- Sind die Daten zweckgeeignet und aktuell?
- Wird verhindert, dass Mitarbeitende sensible Personal-, Kredit-, Gesundheits- oder Justizdaten in allgemeine Tools eingeben?

## Pflicht 4 — Protokolle und Nachvollziehbarkeit

Betreiber müssen Protokolle nach Maßgabe der KI-VO und anderer Rechtsvorschriften aufbewahren.

Prüffragen:
- Welche Logs erzeugt das System?
- Sind Prompt, Eingabe, Output, Nutzer, Zeitpunkt, Version und Entscheidungspfad nachvollziehbar?
- Wie werden Datenschutz, Geheimnisschutz und Löschpflichten berücksichtigt?
- Können Off-label-Nutzungen erkannt werden?

## Pflicht 5 — Überwachung, Meldung und Unterbrechung

Betreiber müssen bei ernsthaften Risiken, Fehlfunktionen oder schwerwiegenden Vorfällen reagieren und ggf. Anbieter sowie Behörden informieren.

Prüffragen:
- Gibt es ein Verfahren für Incidents und Near Misses?
- Wer entscheidet über Pausierung des Systems?
- Werden Outputs korrigiert, zurückgenommen oder betroffene Personen informiert?
- Ist `marktueberwachung-meldung-vorfaelle-art-72-bis-79` einzuschalten?

## Pflicht 6 — Informationspflicht gegenüber Betroffenen

Wenn ein Hochrisiko-KI-System für Entscheidungen gegenüber natürlichen Personen eingesetzt wird, ist transparent zu machen, dass KI beteiligt ist, soweit dies nicht ohnehin offensichtlich ist oder spezieller geregelt ist.

Prüffragen:
- Wer ist betroffen?
- Welche Entscheidung oder Vorbereitung wird beeinflusst?
- Welche Information erhält die Person?
- Gibt es Rechte auf Auskunft, menschliche Überprüfung oder Beschwerde nach KI-VO, DSGVO oder Fachrecht?

## Grundrechte-Folgenabschätzung — Art. 27 KI-VO

Prüfe Art. 27 insbesondere bei:
- öffentlichen Stellen
- privaten Betreibern, soweit sie Hochrisiko-KI für bestimmte wesentliche Dienste einsetzen
- Konstellationen mit Beschäftigung, Bildung, Kredit, Versicherung, Sozialleistungen, Justiznähe oder sonstiger Machtasymmetrie

Inhalt:
- Beschreibung des Systems und Zwecks
- betroffene Personen/Gruppen
- Nutzungsfrequenz und Dauer
- Risiken für Grundrechte
- menschliche Aufsicht und Abhilfemaßnahmen
- Daten- und Governance-Konzept
- Verbindung zur DSGVO-Datenschutz-Folgenabschätzung

## Output-Template — Betreiber-Compliance-Check

```text
BETREIBER-COMPLIANCE-CHECK ART. 26/27 KI-VO
Datum: [DATUM]
System: [NAME]
Betreiber: [NAME]
Risikoklasse: [HOCHRISIKO / UNKLAR / ALLGEMEINES GPAI-SYSTEM]

1. Zweck und Gebrauchsanweisung
[Anbieterzweck, interner Zweck, Abweichungen]

2. Off-label-/Fehlgebrauchsrisiko
[isolierter Verstoß / vorhersehbarer Fehlgebrauch / geduldete Hochrisiko-Nutzung / Zweckänderung]
[Maßnahmen: Richtlinie, Schulung, Sperren, Logging, Freigabe]

3. Art. 26-Pflichten
- bestimmungsgemäße Verwendung: [...]
- menschliche Aufsicht: [...]
- Eingabedaten: [...]
- Protokolle: [...]
- Überwachung/Vorfälle: [...]
- Information Betroffener: [...]

4. Art. 27 Grundrechte-Folgenabschätzung
[erforderlich / nicht erforderlich / offen]
[Begründung]

5. Anbieterwerden Art. 25
[Risiko ja/nein/offen]

6. Nächste Skills
[hochrisiko-art-6-abs-2-anhang-iii / anbieter-werden-art-25 / output-betreiber-checkliste-und-folgenabschaetzung / marktueberwachung-meldung-vorfaelle-art-72-bis-79]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 4, Nr. 12, Nr. 13 und Nr. 23, Art. 4, Art. 25, Art. 26 und Art. 27 KI-VO. Keine Rechtsberatung.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
