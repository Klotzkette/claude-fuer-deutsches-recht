---
name: spezial-ueber-schriftsatz-brief-und-memo-bausteine
description: "Ueber: Schriftsatz-, Brief- und Memo-Bausteine im Plugin gesellschaftsgruender; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung."
---

# Ueber: Schriftsatz-, Brief- und Memo-Bausteine

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `gesellschaftsgruender`. Ausgangspunkt ist: Gründungsassistent deutsche Gesellschaften (GmbH UG GbR OHG KG GmbH und Co KG PartG mbB gGmbH). Von Rechtsformwahl über Gesellschaftsvertrag und Geschäftsführervertrag bis Notar Handelsregister Gewerbeamt Finanzamt Transparenzregister. MoPeG DiRUG GwG. Kein Ersatz für Anwaltsberatung.

Er führt durch **Schriftsatz-, Brief- und Memo-Bausteine** im Themenfeld **Ueber**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.


## Fachlicher Zuschnitt

- **Thema:** Ueber.
- **Arbeitsfokus:** Schriftsatz-, Brief- und Memo-Bausteine.
- **Plugin-Rahmen:** Anfängerfreundlicher Gründungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, SHA, Cap Table, Notar, Handelsregister, Bank/KYC, Behörden....
- **Qualitätsanspruch:** Antworte nicht mit einer austauschbaren Standard-Checkliste. Nutze die Fachlogik dieses Plugins, benenne die konkret einschlägigen Normgruppen, Behörden, Register, Fristen, Dokumente oder Verfahrenshandlungen und trenne sichere Punkte von Live-Check-Bedarf.
- **Eloquenz und Nutzen:** Führe die Nutzerin oder den Nutzer wie eine erfahrene Fachperson: kurze Orientierung, präzise Rückfragen, dann ein verwertbares Produkt mit Varianten, Gegenargumenten und nächstem Handgriff.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Standard-Bausteine für Gründungsbetreuung

| Baustein | Adressat | Inhalt | Norm |
| --- | --- | --- | --- |
| Anmeldungstext HRB | Registergericht | Firma, Sitz, Gegenstand, Stammkapital, GF | § 8 GmbHG / § 36 AktG |
| Notarauftrag | Notar | Vertragsbeurkundung, Anmeldung, Beglaubigungen | §§ 2, 15 GmbHG / § 23 AktG |
| Gewerbeanzeige | Gewerbeamt | Tätigkeit, Sitz, GF/Inhaber | § 14 GewO |
| Transparenzregister-Eintragung | Bundesanzeiger | wirtschaftlich Berechtigte | §§ 19, 20 GwG |
| Mandantenmemo Rechtsformwahl | Mandant | Vor-/Nachteile, Empfehlung, To-dos | – |
| Geschäftsführervertrag | GF | Vergütung, Befreiung § 181 BGB, Wettbewerbsverbot, Kündigung | §§ 35, 43 GmbHG |

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Bausteinwahl:** Welcher Output ist nötig? Notarauftrag bei Gründung GmbH/AG; Mandantenmemo bei Rechtsformwahl; Geschäftsführervertrag separat (nicht Teil Gesellschaftsvertrag, denn Gesellschaftsvertrag nur "organschaftliches" Verhältnis; Anstellungsverhältnis ist eigenständig).
3. **Pflichtbestandteile prüfen:** Anmeldungstext HRB enthält Firma, Sitz, Gegenstand, Stammkapital, GF mit Vertretungsregelung (§ 8 GmbHG). Gewerbeanzeige erforderlich vor Geschäftsbeginn, sonst Bußgeld § 146 Abs. 2 GewO.
4. **Befreiung § 181 BGB:** Bei Ein-Personen-GmbH zwingend Insichgeschäfts-Befreiung im Gesellschaftsvertrag und konkrete Erteilung; sonst kann GF mit sich selbst nicht wirksam kontrahieren.
5. **Anschluss:** Geschäftsführervertrag-Skill `spezial-geschaeftsfuehrervertrag-livequellen-check`; bei Transparenzregister `gesellschaftsgruender-transparenzregister`.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
