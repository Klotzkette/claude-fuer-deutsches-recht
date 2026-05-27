---
name: ki-governance-anpassen
description: "Geführte Anpassung Ihres KI-Governance-Praxisprofils – eine Einstellung ändern, ohne das vollständige Kaltstart-Interview neu zu starten. Risikoeinstellung, Eskalationskontakte, Use-Case-Register-Einträge, Vendor-KI-Positionen, KI-Richtlinien-Commitments, Folgenabschätzungs-Hausformat oder Mandats-Workspace-Pfade anpassen. Verwenden, wenn der Nutzer sagt „ändere mein [Ding]\", „Profil aktualisieren\", „Konfiguration bearbeiten\", „Playbook anpassen\" oder „anpassen\"."
---

# /anpassen

## Zweck

Der Nutzer hat `/ki-governance:ki-governance-anpassen` eingegeben. Er möchte etwas in seinem Praxisprofil
ändern – eine Risikoeinstellung, einen Eskalationskontakt, eine Playbook-Position, eine
Jurisdiktion, ein Ausgabeformat – ohne das gesamte Kaltstart-Interview neu zu starten und
ohne YAML manuell zu bearbeiten.

## Eingaben

- Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
  und `unternehmens-profil.md` (eine Ebene höher)
- Beschreibung der gewünschten Änderung vom Nutzer

## Ablauf

1. **Konfiguration lesen.** CLAUDE.md und unternehmens-profil.md lesen. Falls CLAUDE.md nicht
   existiert oder noch `[PLATZHALTER]`-Werte enthält:

   > Sie haben noch kein Setup durchgeführt. Führen Sie zuerst `/ki-governance:ki-governance-kaltstart-interview`
   > aus – anpassen dient der Anpassung eines bereits vorhandenen Profils.

2. **Anpassbare Karte anzeigen.** Auflisten, was im Profil steht, gruppiert, mit
   einzeiliger Zusammenfassung des aktuellen Werts:

   - **Unternehmen / Wer Sie sind** – Name, Branche, Jurisdiktionen, Phase, Praxiskontext
     *(geteilt über alle Plugins – Änderungen fließen durch `unternehmens-profil.md`)*
   - **Regulatorischer Fußabdruck** – KI-VO, DSGVO/BDSG, sektorspezifische Regelwerke
     im Anwendungsbereich
   - **Risikoeinstellung** – konservativ / mittig / progressiv, was das für Triage- und
     Folgenabschätzungs-Ausgaben bedeutet
   - **Personen** – Governance-Team, KI-Risikobeauftragter, Eskalationskette, Genehmiger
   - **Use-Case-Register** – genehmigte / bedingte / nie-Einträge und zugehörige Bedingungen
   - **KI-System-Inventar** – je System: Rolle (Anbieter / Betreiber usw.) und Risikoklasse
     nach KI-VO. `/ki-governance:ki-inventar` für den dedizierten Editor verwenden.
   - **Vendor-KI-Governance** – Trainings-auf-Daten, Haftung, Modell-Änderungsmeldung,
     Art. 28 DSGVO AVV, Art. 11 KI-VO Technische Dokumentation und andere Positionen
   - **KI-Richtlinien-Commitments** – öffentliche oder interne Commitments, gegen die das
     Plugin abgleicht
   - **Folgenabschätzungs-Hausformat** – FRIA-/DSFA-Abschnittsreihenfolge, Risiko-Scoring-Format,
     Stakeholder-Framing
   - **Ablauf** – Aufnahme-Pfad, Ausgabeformat, Mandats-Workspace-Pfade, Prüfkadenz für
     den Policy-Monitor
   - **Integrationen** – was verbunden ist (Slack, Dokumentenspeicher, geplante Aufgaben),
     was zurückfällt

3. **Fragen, was geändert werden soll.**

   > Was möchten Sie anpassen? Wählen Sie einen Abschnitt oder beschreiben Sie die Änderung
   > in eigenen Worten.

4. **Änderung vornehmen.** Aktuellen Wert zeigen, neuen Wert abfragen, nachgelagerte
   Auswirkungen erklären, bestätigen, in Konfiguration schreiben.

   Beispiele für nachgelagerte Erklärungen:
   - *Risikoeinstellung mittig → konservativ:* „Ich werde mehr Anwendungsfälle als bedingt
     statt genehmigt markieren, mehr Folge-Prüfungen zur Folgenabschätzung einleiten und
     konservativere Vendor-KI-Redlines empfehlen."
   - *Eskalationskontakt hinzufügen:* „Jeder Skill, der Eskalationen weiterleitet
     (`/anwendungsfall-triage`, `/ki-anbieter-prüfung`, `/regulierungs-lücken-analyse`), wird diesen Kontakt
     nun auf den relevanten Risikostufen einschließen."
   - *Neuer Use-Case-Register-Eintrag:* „`/anwendungsfall-triage` gleicht beim nächsten Lauf
     gegen diesen Eintrag ab. Bestehende Folgenabschätzungen werden nicht neu geschrieben –
     führen Sie sie neu aus, wenn Sie die neue Position darin gespiegelt sehen möchten."

5. **Bei Änderungen am gemeinsamen Profil** (Unternehmensname, Branche, Jurisdiktionen,
   Praxiskontext):
   `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` schreiben
   und vermerken:

   > Diese Änderung betrifft alle Plugins – jedes Plugin, das Ihren Jurisdiktionsfußabdruck
   > liest, sieht jetzt [neuer Wert].

6. **Abschluss.**

   > Erledigt. Ihr nächstes Ergebnis wird die Änderung widerspiegeln. Noch etwas? Sie können
   > `/ki-governance:ki-governance-anpassen` jederzeit ausführen.

## Quellen und Zitierweise

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

Downstream-Auswirkungen von Konfigurationsänderungen können folgende Normen betreffen:
- Art. 26, 27, 50 KI-VO (VO 2024/1689) – Betreiberpflichten, FRIA, Transparenz `[Primärquelle]`
- Art. 35 DSGVO – DSFA-Pflicht `[Primärquelle]`
- Art. 28 DSGVO – Auftragsverarbeitung `[Primärquelle]`

## Ausgabeformat

Interaktiver Dialog: Karte → Auswahl → aktueller Wert / neuer Wert → Bestätigung → Schreiben.

## Risiken / typische Fehler

- **Abschnitt nicht löschen.** Falls der Nutzer etwas „entfernen" möchte, auf
  `[Nicht konfiguriert]` setzen und erklären, was das für das Plugin-Verhalten bedeutet.
  („Das Entfernen Ihrer Eskalationskette bedeutet, dass `/anwendungsfall-triage` eskalationswürdige
  Punkte markiert, aber nicht an eine bestimmte Person weiterleitet.")
- **Interne Inkonsistenz markieren.** Falls die Änderung das Profil inkonsistent machen würde
  (z. B. Risikoeinstellung progressiv + Eskalation „alles geht an den GC"; oder „KI-VO im
  Anwendungsbereich" + „keine Systeme für EU markiert"), Spannung aufzeigen und fragen,
  welche Seite der Nutzer möchte.
- **Leitplanken-Degradation markieren.** Falls der Nutzer eine Leitplanke deaktivieren
  möchte („`[prüfen]`-Flag nicht mehr hinzufügen", „Zitats-Warnung weglassen"), erklären,
  wovor die Leitplanke schützt, und die Trade-offs bestätigen. Strukturelle Leitplanken:
  - `[prüfen]`-Markierungs-Mechanismus (zeigt dem Nutzer, wann juristisches Urteil
    erforderlich ist) – tragend, nicht entfernen.
  - Quellenattribuierungs-Tags auf abgerufenem Inhalt – tragend, nicht entfernen.
  - `[prüfen]`-Tags auf zitierten Normen/Vorschriften – tragend, nicht entfernen.
- **Eine Änderung auf einmal.** Nicht das gesamte Interview neu stellen. Bei mehreren
  Änderungen sequenziell vorgehen und jede vor dem Weitermachen bestätigen.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 49: Profilbasierte KI-Entscheidungen fallen unter Art. 22 DSGVO — Anpassung der Risikoeinstellung muss DSGVO-Widerspruchsrecht berucksichtigen.
- EuGH, Urt. v. 04.10.2024 — C-203/22 (Dun & Bradstreet), NJW 2025, 56 Rn. 38: Betreiber algorithmischer Systeme muss Entscheidungslogik verstaendlich offenlegen — Anpassungen der Offenlegungsklauseln im Praxisprofil muss Art. 22 Abs. 3 DSGVO beruecksichtigen.
- BGH, Urt. v. 19.06.2018 — VI ZR 184/17, NJW 2018, 2877 Rn. 15: Interne Organisationspflichten bei technischen Systemen — KI-Governance-Aenderungen muessen konsistent in alle verbundenen Prozesse eingepflegt werden.
- BVerwG, Urt. v. 04.04.2019 — 2 C 4/18, NVwZ 2019, 1283 Rn. 22: Transparenz algorithmischer Entscheidungen als Pflicht auch im Verwaltungsbereich; Eskalationsmatrix-Aenderungen muessen nachvollziehbar dokumentiert werden.

## Zentrale Normen (Paragrafenkette)
- Art. 5 KI-VO — verbotene Praktiken (jede Profileinstellung muss dagegen gecheckt werden)
- Art. 26/29 KI-VO — Betreiberpflichten (Anpassungen an Hochrisiko-Einstellungen)
- Art. 22 DSGVO — automatisierte Einzelentscheidungen
- Art. 35 DSGVO — DSFA-Ausloeser
- § 87 Abs. 1 Nr. 6 BetrVG — Mitbestimmungsrecht bei Mitarbeiter-KI

## Kommentarliteratur
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 26 Rn. 5: Betreiberpflichten und Governance-Dokumentation.
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10: Widerspruchsrecht und Konfigurationsanforderungen.

## Triage zu Beginn
1. Welcher Abschnitt des Praxisprofils soll geaendert werden — Risikoeinstellung, Register, Eskalation?
2. Hat die Aenderung nachgelagerte Auswirkungen auf andere Skills (Triage, Folgenabschaetzung)?
3. Betrifft die Aenderung die Eskalationsmatrix — wer ist neuer Genehmiger?
4. Wird eine Leitplanke degradiert — welche Schutzfunktion entfaellt?
5. Sind Aenderungen am gemeinsamen Profil (unternehmens-profil.md) betroffen?

## Output-Template — Profil-Aenderungsbestaetigung
**Adressat:** KI-Governance-Verantwortlicher — Tonfall: knapp, bestaedigend
```
PROFIL-AENDERUNGSBESTAETIGUNG
[DATUM] — Geaenderter Abschnitt: [ABSCHNITT]

Alte Einstellung: [ALTER WERT]
Neue Einstellung: [NEUER WERT]

Nachgelagerte Auswirkungen:
- [SKILL X]: [BESCHREIBUNG AUSWIRKUNG]
- [SKILL Y]: [BESCHREIBUNG AUSWIRKUNG]

Leitplanken: [KEINE DEGRADATION / DEGRADIERT: BESCHREIBUNG UND BESTAETIGUNG]

Naechste Pruefung: [DATUM]
Geaendert von: [NAME], [DATUM]
```
