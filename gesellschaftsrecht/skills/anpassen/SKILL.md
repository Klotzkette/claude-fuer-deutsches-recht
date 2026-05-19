---
name: anpassen
description: >
  Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung
  ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil,
  Eskalationskontakte, aktive Module (M&A / Governance / Kapitalmarkt / Gesellschaftsverwaltung),
  Wesentlichkeitsschwellen, Beschlussformat oder Mandatsworkspace-Pfade anpassen.
  Lädt, wenn der Nutzer „Profil ändern", „Konfiguration aktualisieren", „Einstellung anpassen"
  oder vergleichbare Formulierungen verwendet.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Profil ändern
  - Konfiguration aktualisieren
  - Einstellung anpassen
  - Schwellenwert ändern
  - Modul aktivieren
  - Eskalation aktualisieren
  - Beschlussformat anpassen
  - Praxisprofil bearbeiten
  - anpassen
argument-hint: "[Abschnitt oder Beschreibung der gewünschten Änderung]"
---

# Praxisprofil anpassen

## Zweck

Der Nutzer möchte eine einzelne Einstellung im Praxisprofil ändern — ein Risikoprofil, einen Eskalationskontakt, einen Modulschalter, ein Ausgabeformat — ohne das vollständige Ersteinrichtungs-Interview zu wiederholen und ohne YAML manuell zu bearbeiten.

## Eingaben

- Aktuelle CLAUDE.md (Praxisebene) und ggf. Unternehmensprofil
- Beschreibung der gewünschten Änderung (Freitext oder Abschnittsbenennung)
- Bei modulspezifischen Änderungen: ggf. neue Seed-Dokumente

## Rechtlicher Rahmen

Das Praxisprofil bildet den rechtlichen Rahmen der vom Nutzer betreuten Mandate ab. Änderungen an Wesentlichkeitsschwellen, Modulen oder Eskalationslogiken haben unmittelbare Auswirkungen auf sämtliche Skill-Ausgaben.

Relevante Vorschriften je Bereich (Referenz für Konsistenzprüfung):
- M&A-Wesentlichkeit: § 311 AktG, § 15 GmbHG, §§ 241 ff. AktG analog (Beschlussmängel GmbH); BGH, Urt. v. 23.09.2014 – II ZR 44/13, NZG 2014, 1332 Rn. 15 (Beschlussmängelrecht GmbH)
- Beschlussfassung: § 48 Abs. 2 GmbHG (schriftliches Verfahren GmbH); § 130 AktG (Niederschrift HV); BGH, Urt. v. 11.02.2008 – II ZR 187/06, NZG 2008, 381 Rn. 12 (Zustimmungspflicht bei schriftlichen GmbH-Beschlüssen)
- Mitbestimmung: MitbestG, DrittelbG — eine Moduländerung, die ein mitbestimmungspflichtiges Unternehmen betrifft, ist zu flaggen
- Kapitalmarkt: Art. 17 MAR (Ad-hoc), §§ 33 ff. WpHG (Stimmrechtsmitteilungen); Roth/Altmeppen, GmbHG, 11. Aufl. 2024, § 48 Rn. 10 ff.
- Kommentarliteratur allgemein: Baumbach/Hopt, HGB, 41. Aufl. 2024, § 105 Rn. 1 ff. (Personengesellschaften); Hüffer/Koch, AktG, 16. Aufl. 2024, Einl. Rn. 5 ff.

## Ablauf

### Schritt 1: Praxisprofil lesen

CLAUDE.md und Unternehmensprofil lesen. Falls das Plugin-Profil nicht existiert oder noch `[PLATZHALTER]`-Werte enthält:

> Sie haben die Ersteinrichtung noch nicht abgeschlossen. Führen Sie zunächst `/gesellschaftsrecht:kaltstart-interview` aus — die Anpassungsfunktion setzt ein bestehendes Praxisprofil voraus.

### Schritt 2: Anpassungsübersicht zeigen

Liste der konfigurierbaren Bereiche mit aktuellen Werten:

- **Unternehmen / Wer Sie sind** — Name, Branche, Rechtsform, Sitz, Tätigkeitssetting *(gemeinsam genutzt über alle Plugins — Änderungen wirken in `unternehmens-profil.md`)*
- **Aktive Module** — welche von M&A, Governance/Beschlussfassung, Kapitalmarkt, Gesellschaftsverwaltung aktiv sind. Ein- und Ausschalten ändert, welche Skills Setup-Hinweise einblenden.
- **Risikoprofil** — konservativ / ausgewogen / progressiv; Bedeutung für Due-Diligence-Wesentlichkeit und Offenlegungsumfang
- **Personen** — Transaktionsteam, verantwortlicher Geschäftsführer/Vorstand, Gesellschaftsverwaltungsverantwortlicher, Eskalationskette
- **M&A-Modul** — Wesentlichkeitsschwellen (Vertragswert, Mitarbeiteranzahl, Umsatz), zugelassene VDR-Plattformen, KI-Massenreview-Vertrauensstufe, Briefing-Turnus des Transaktionsteams
- **Governance-Modul** — Hausbeschlussformat, bevorzugte Unterzeichner, Ausschussstruktur, Notaranforderungen
- **Kapitalmarkt-Modul** — Berichterstattungskalender, BaFin-Meldepflichten, Hauptversammlungs-Turnus
- **Gesellschaftsverwaltungs-Modul** — Gesellschaftstabelle, Registerführung, Jahresabschluss-Pflichten
- **Ablauf** — Mandatsworkspaces, Schließungscheckliste, VDR-Pfad
- **Integrationen** — Box / Intralinks / Datasite / Handelsregister / Datenraum-Status und Fallbacks

### Schritt 3: Änderungswunsch erfragen

> Was möchten Sie anpassen? Wählen Sie einen Abschnitt, oder beschreiben Sie die Änderung in eigenen Worten.

### Schritt 4: Änderung durchführen

Aktuellen Wert zeigen, neuen Wert abfragen, Downstream-Auswirkungen erläutern, bestätigen, in die Konfiguration schreiben.

Beispiele:
- *Wesentlichkeitsschwelle 250.000 EUR → 500.000 EUR:* „`/Due-Diligence-Extraktion` und `/Material-Vertragsverzeichnis` verwenden künftig 500.000 EUR als Grenzwert. Bestehende Findings bleiben unverändert; bei rückwirkender Anwendung bitte neu ausführen."
- *Kapitalmarkt-Modul aktivieren:* „Beim nächsten Aufruf eines kapitalmarktrechtlichen Skills werden Sie nach Berichterstattungskalender und BaFin-Pflichten gefragt."
- *KI-Massenreview-Vertrauen „jede Zeile prüfen" → „10 % Stichprobe":* „`/KI-Tool-Übergabe` prüft künftig eine 10 %-Stichprobe statt jeder Extraktion."

### Schritt 5: Änderungen an Unternehmensprofil

Bei Änderungen an Unternehmensname, Branche, Sitz, Tätigkeitssetting, Rechtsform: in `unternehmens-profil.md` schreiben und hinweisen:

> Diese Änderung betrifft alle Plugins — jedes Plugin, das Ihren Jurisdiktionsbereich liest, sieht ab sofort [neuer Wert].

### Schritt 6: Abschluss

> Fertig. Ihre nächste Ausgabe spiegelt die Änderung wider. Weitere Anpassungen? Sie können `/gesellschaftsrecht:anpassen` jederzeit erneut aufrufen.

## Ausgabeformat

- Bestätigung der Änderung mit Vorher-/Nachher-Wert
- Hinweis auf betroffene Skills
- Ggf. Inkonsistenzwarnung (s. u.)

## Beispiel

**Szenario:** Wesentlichkeitsschwelle für Vertragsreview von 100.000 EUR auf 250.000 EUR erhöhen.

Ausgabe: „Wesentlichkeitsschwelle geändert: 100.000 EUR → 250.000 EUR. `/Due-Diligence-Extraktion` und `/Material-Vertragsverzeichnis` wenden den neuen Wert an. Bestehende Findings bleiben unverändert."

## Risiken und typische Fehler

- **Abschnitte löschen.** Wenn der Nutzer etwas „entfernen" möchte, Wert auf `[Nicht konfiguriert]` setzen und Auswirkung erläutern.
- **Interne Inkonsistenz ignorieren.** Wenn die Änderung das Profil inkonsistent macht (z.B. Kapitalmarkt-Modul deaktiviert + „BaFin-Kontakt" in Eskalationsmatrix; oder konservatives Risikoprofil + sehr hohe Schwellenwerte), Spannung flaggen.
- **Schutzfunktionen degradieren.** Das `[überprüfen]`-Flag, Quellenangaben auf abgerufenen Dokumenten und `[verifizieren]`-Tags auf zitierten Entscheidungen sind inhaltlich tragende Elemente — Trade-off vor Entfernung erläutern.
- **Mehrere Änderungen gleichzeitig.** Eine Änderung pro Durchlauf, kein Re-Interview.

## Quellenpflicht

Bei Änderungen, die rechtliche Schwellenwerte oder Verfahrensregeln betreffen:
- Einschlägige Norm zitieren: `§ 48 Abs. 2 GmbHG`, `Art. 17 Abs. 1 MAR`
- BGH-Entscheidungen: `BGH, Urt. v. 11.02.2008 – II ZR 187/06, NZG 2008, 381 Rn. 12`
- Kommentare im Bearbeiterstil: `Hüffer/Koch, AktG, 16. Aufl. 2024, § 130 Rn. 5`

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
