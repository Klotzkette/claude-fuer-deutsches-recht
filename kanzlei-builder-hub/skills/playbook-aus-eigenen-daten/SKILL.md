---
name: playbook-aus-eigenen-daten
description: "Kanzleieigenes Playbook aus vorhandenen Musterdokumenten und Vorlagen automatisch erstellen. Normen: technisch/intern, BRAO. Pruefraster: Dokumentenqualitaet, Kategorisierung, Normverankerung. Output: Kanzlei-Playbook aus eigenen Daten. Abgrenzung: nicht Standardvorlagen aus Plugin-Bibliothek."
---

# Skill: Playbook aus eigenen Daten

## Zweck

Aus echten, bereits abgeschlossenen Mandaten und Korrespondenzen wird ein
strukturiertes Vorgehens-Spielbuch (Playbook) destilliert, das anschließend
als wiederverwendbarer Skill, Auslöser oder Agentenrezept im Hintergrund
für gleichartige Vorgänge eingesetzt werden kann. Eingaben sind ausschließlich
die eigenen Daten der Anwältin oder des Anwalts: Outlook-Mails, Wordsschriftsätze,
Aktenexporte, Sprachnotizen, Excel-Trackings oder Notizdokumente.

Das Ergebnis ist kein generisches Muster, sondern ein an die tatsächliche
Arbeitsweise der Kanzlei angepasstes Spielbuch — mit den dort üblichen
Floskeln, Eskalationsstufen, Standardklauseln, Prüfreihenfolgen und
Mandantenansprachen.

## Eingaben

- **E-Mail-Korpus** (Outlook-Konnektor oder `.eml`/`.msg`-Exporte): typischerweise
  20–200 Mails aus einem oder mehreren ähnlichen Mandaten.
- **Schriftsätze und Anschreiben** (Word, PDF): mindestens 5 abgeschlossene
  Vergleichsfälle desselben Mandatstyps.
- **Notizen** (Markdown, Notizbuch-Exporte, Sprachprotokoll-Transkripte).
- **Tracking-Exporte** (Excel, CSV) aus Aktenverwaltung oder
  Fristenkalender — optional, schärft Fristenketten.
- **Mandantenkommunikations-Logs** aus `mandantenkommunikation/` — falls
  vorhanden.

Pflichtangabe der Nutzerin / des Nutzers:

- **Mandatstyp** (z. B. „Kündigungsschutzklage Arbeitnehmer", „NDA-Review
  Inbound", „Mietkündigung Vermieter", „GmbH-Gründung").
- **Erwarteter Wiederverwendungs-Kontext** (Mandantenkommunikation vs.
  interne Bearbeitung vs. Schriftsatzentwurf).
- **Vertraulichkeitsstufe** der Eingaben (anonymisiert vs. echte
  Mandantendaten — bei echten Daten greift § 43a Abs. 2 BRAO,
  § 203 StGB; siehe Risiken).

## Rechtlicher Rahmen

- **§ 43a Abs. 2 BRAO** — anwaltliche Verschwiegenheitspflicht; gilt auch
  bei Aufbereitung eigener Mandatsdaten zu Trainings- oder
  Mustergenerierungszwecken.
- **§ 203 Abs. 1 Nr. 3 StGB** — strafbewehrte Verletzung von Privatgeheimnissen.
- **§ 2 Abs. 3, § 50 BRAO** — Aktenführungs- und Aufbewahrungspflichten;
  Playbook-Ableitungen sind keine Akte, müssen aber nachvollziehbar bleiben.
- **Art. 6 Abs. 1 lit. f DSGVO** — berechtigtes Interesse an interner
  Arbeitsorganisation; Abwägung gegen schutzwürdige Mandanteninteressen.
- **Art. 32 DSGVO** — technische und organisatorische Maßnahmen
  (Zugriffsbeschränkung, Pseudonymisierung).
- **BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, BVerfGE 113, 29 Rn. 99** —
  Schutz des Vertrauensverhältnisses zwischen Anwalt und Mandant
  (Vertraulichkeit auch gegenüber technischen Hilfsmitteln).
- **BGH, Urt. v. 13.07.2021 – VI ZR 128/20, NJW 2021, 2956 Rn. 17** —
  Anforderungen an Anonymisierung in juristischen Veröffentlichungen,
  übertragbar auf interne Mustergenerierung.
- **EuGH, Urt. v. 04.05.2023 – C-487/21, ECLI:EU:C:2023:369 Rn. 45** —
  Auskunftsrecht nach Art. 15 DSGVO umfasst keine Geschäftsgeheimnisse
  (anwendbar bei Mandantenauskunftsersuchen zu intern abgeleiteten
  Spielbüchern).

Kommentare:

- Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 43a Rn. 41 ff.
  (Reichweite der Verschwiegenheitspflicht bei interner
  Wissensverarbeitung).
- Paal, in: Paal/Pauly, DS-GVO BDSG, 4. Aufl. 2024, Art. 6 Rn. 38
  (berechtigtes Interesse bei interner Arbeitsorganisation).
- Grüneberg, BGB, 84. Aufl. 2025, § 666 Rn. 4 (Rechenschafts- und
  Aufbewahrungspflichten als Hintergrund anwaltlicher Aktenführung).
- Fischer, StGB, 71. Aufl. 2024, § 203 Rn. 6a (Schweigepflicht bei
  EDV-gestützter Verarbeitung).

## Ablauf

1. **Vorab-Trennung Vertraulichkeitsstufen.** Eingaben werden nach
   Quelle markiert: (a) bereits anonymisierte Muster, (b) eigene
   Notizen ohne Personenbezug, (c) echte Mandatsdaten. Stufe (c)
   wird vor der Mustererkennung pseudonymisiert
   (Namen → `[MANDANT_1]`, `[GEGNER_1]`, IBAN/AZ → Token).
2. **Korpus-Indizierung.** Mails werden nach Sender, Empfänger,
   Datum, Mandatsbezug (aus Betreff/Aktenzeichen) gruppiert; Schriftsätze
   nach Verfahrensstadium (Anhörung, Klageerwiderung, Replik usw.)
   sortiert.
3. **Phasen-Extraktion.** Aus jedem Vergleichsfall wird der zeitliche
   Verlauf rekonstruiert: Erstkontakt → Sachverhaltsaufnahme →
   rechtliche Prüfung → Mandantenrücksprache → Schriftsatz/Anschreiben →
   Fristen → Eskalation → Abschluss. Phasen werden über Fälle hinweg
   geclustert.
4. **Sprachmuster-Extraktion.** Wiederkehrende Formulierungen werden
   typisiert: (a) Anrede- und Schlussformeln; (b) Standardklauseln in
   Aufforderungsschreiben (§ 286 BGB); (c) Eskalationssignale gegenüber
   der Gegenseite; (d) Mandanten-Erklärungen schwieriger Punkte in
   einfacher Sprache.
5. **Entscheidungs-Punkt-Identifikation.** Wo verzweigt das Vorgehen?
   Typische Bedingungen: außergerichtliche Einigung vs. Klage, Frist
   gewahrt vs. nicht gewahrt, Mandant zahlungsfähig vs. nicht. Diese
   Verzweigungen werden als Entscheidungsbaum erfasst.
6. **Fristen-Skelett.** Aus den Vergleichsfällen werden typische
   Fristen-Ketten herausgezogen (z. B. Klagefrist § 4 KSchG = 3 Wochen,
   Verjährungsbeginn § 199 BGB, Berufungsfrist § 517 ZPO = 1 Monat).
7. **Playbook-Generierung.** Aus 3–6 ergibt sich ein strukturiertes
   Spielbuch im Format `<mandatstyp>.playbook.md` mit Phasen-Liste,
   Klausel-Bibliothek, Entscheidungsbaum, Fristen-Skelett und
   Eskalationsmatrix.
8. **Verifikation.** Spielbuch wird gegen 2 weitere, nicht
   für die Generierung verwendete Vergleichsfälle gespiegelt:
   passt die Phasenabfolge? Treffen die Klauselvorschläge? Fehlende
   Schritte werden ergänzt.
9. **Ablage und Versionierung.** Spielbuch wird unter
   `playbooks/<mandatstyp>.playbook.md` abgelegt; Generierungs-Log
   (welche Quelldateien, welche Anonymisierung) unter
   `playbooks/<mandatstyp>.generierungslog.json`.
10. **Aktivierung als wiederverwendbarer Auslöser.** Optional: aus
    dem Spielbuch wird ein leichtgewichtiger Skill oder ein
    Agentenrezept erzeugt, das das Vorgehen bei neuen, gleichartigen
    Mandaten automatisch vorschlägt.

## Ausgabeformat

```
playbooks/
├── <mandatstyp>.playbook.md             # Hauptergebnis
├── <mandatstyp>.klauselbibliothek.md    # Wiederverwendbare Textbausteine
├── <mandatstyp>.fristen.yaml            # Fristen-Skelett, maschinenlesbar
├── <mandatstyp>.entscheidungsbaum.md    # Verzweigungspunkte
└── <mandatstyp>.generierungslog.json    # Audit-Trail
```

**`<mandatstyp>.playbook.md` Pflichtsektionen:**

1. Übersicht (Mandatstyp, typische Dauer, Hauptrisiken)
2. Phasen (mit Eingaben/Ausgaben pro Phase)
3. Sprachmuster nach Kontext (Mandant intern / Gegenseite / Gericht /
   Behörde)
4. Entscheidungsbaum (Knotenpunkte und Folgepfade)
5. Fristen-Skelett (mit Norm-Verweisen)
6. Eskalationsmatrix (Schwellenwerte, Zuständigkeiten)
7. Verifikationsstatus (gegen welche Fälle gespiegelt)
8. Quellenpflicht (welche Korpus-Dateien zur Generierung beitrugen —
   nur Hash-IDs, keine Mandantennamen)

## Beispiel

**Eingabe:** Eine Fachanwältin für Arbeitsrecht stellt einen Outlook-Ordner
mit 47 Mails aus drei abgeschlossenen Kündigungsschutzverfahren bereit,
dazu vier Word-Klageschriften und ein Excel-Tracking mit Verfahrensdauern.

**Ausgabe (Auszug aus `kündigungsschutz-arbeitnehmer.playbook.md`):**

```markdown
## Phase 2 — Sachverhaltsaufnahme (Tag 1–3 nach Erstkontakt)

Eingaben: Kündigungsschreiben, Arbeitsvertrag, Lohnabrechnungen
(letzte 6 Monate), Anhörungsprotokoll Betriebsrat (§ 102 BetrVG).

Standardfragen an Mandant:
- Datum des Zugangs der Kündigung? (Kritisch für § 4 KSchG, 3 Wochen).
- Wurde der Betriebsrat angehört? Liegt Anhörungsprotokoll vor?
- Schwerbehinderung, Schwangerschaft, Elternzeit, Mandatsträger?
  (Sonderkündigungsschutz § 168 SGB IX, § 17 MuSchG, § 18 BEEG,
  § 15 KSchG)
- Sozialauswahl: vergleichbare Arbeitnehmer im Betrieb?

Entscheidungspunkt:
- Frist § 4 KSchG noch offen? → Klagevorbereitung Phase 3.
- Frist abgelaufen? → § 5 KSchG nachträgliche Zulassung prüfen,
  Mandant über Erfolgsaussichten aufklären.
```

**Fristen-Skelett-Auszug (`kündigungsschutz-arbeitnehmer.fristen.yaml`):**

```yaml
phase: klageerhebung
norm: § 4 Satz 1 KSchG
dauer_tage: 21
fristbeginn: zugang_kündigung
folge_bei_versaeumnis: fiktion_der_wirksamkeit_§7_kschg
ausnahme: § 5 KSchG nachträgliche Zulassung
```

## Risiken und typische Fehler

- **Re-Identifikation trotz Pseudonymisierung.** Datums-Kombinationen,
  ungewöhnliche Sachverhalte und Standortangaben können Mandanten
  identifizierbar machen, auch wenn Namen ersetzt sind (BGH, NJW 2021,
  2956 Rn. 17). Anonymisierung muss mehrstufig sein.
- **Übergeneralisierung.** Wenige Vergleichsfälle führen zu Spielbüchern,
  die seltene Konstellationen ignorieren — daher Mindestkorpus
  (≥ 5 Vergleichsfälle pro Mandatstyp) und Verifikationsphase.
- **Klauselübernahme aus Mandantenkommunikation.** Wenn Standardklauseln
  aus realen Mails übernommen werden, können fremde Wortschöpfungen
  oder Mandanten-Geschäftsgeheimnisse mitwandern. Filterregel: nur
  generische Formulierungen ins Spielbuch.
- **Vermischung mit aktuellem Mandat.** Wird ein Spielbuch parallel
  zu einem laufenden Mandat erstellt, droht Datenleck zwischen Mandaten —
  daher strikte Trennung der Generierungs-Workspaces.
- **Veraltete Rechtsstände.** Spielbücher basieren auf Vergleichsfällen
  von gestern — Pflicht zur Auffrischung gegen aktuelle Rechtsprechung
  bei jedem Einsatz, gestützt durch den
  `regulierungs-aenderungs-monitor` und den `verlaengerungs-monitor`.
- **§ 203 StGB-Risiko bei Cloud-Verarbeitung.** Wenn die Generierung
  in einer Cloud-Umgebung läuft, sind die Anforderungen aus
  Fischer, StGB, § 203 Rn. 6a einzuhalten (Auftragsverarbeitungsvertrag,
  Verschwiegenheitsverpflichtung der Auftragsverarbeiterin).

## Quellenpflicht

Jedes generierte Spielbuch dokumentiert in `generierungslog.json`:

- Hash-IDs der Quelldateien (kein Klarname).
- Datum und Version der Generierung.
- Eingesetzte Anonymisierungs-Regelsätze.
- Verifikationsergebnisse gegen Vergleichsfälle.

Beim Einsatz des Spielbuchs auf ein neues Mandat erfolgt im
Mandatsworkspace ein Eintrag mit Spielbuch-Version und Treffer-Score.
Rechtsprechung und Kommentarstellen aus dem Spielbuch werden im
neuen Mandat auf Aktualität gegengeprüft (mindestens BGH/BAG/BFH der
letzten 24 Monate).
