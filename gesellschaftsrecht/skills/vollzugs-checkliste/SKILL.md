---
name: vollzugs-checkliste
description: "Vollzugscheckliste für M&A-Transaktionen nach deutschem Recht – was blockiert den Vollzug (Closing), kritischer Pfad, Tage bis Vollzug. Selbstaktualisierend: nimmt neue Einträge aus DD-Findings und Anlage-Erstellung auf. Trigger: „Vollzugscheckliste\", „Closing-Checkliste\", „was fehlt noch zum Closing\", „Checklisten-Status\", „zur Checkliste hinzufügen\"."
---

# Vollzugscheckliste M&A

## Zweck

Transaktionen werden vollzogen, wenn die Checkliste abgearbeitet ist. Vollständig. Nichts fehlt. Dieser Skill pflegt die Liste, nimmt neue Einträge aus dem DD-Prozess auf und zeigt dem Team, was blockiert.

## Rechtlicher Rahmen (deutsches M&A-Recht)

- **Signing / Vollzug (Closing):** In deutschen M&A-Transaktionen finden Signing (Vertragsschluss) und Closing (Vollzug) häufig zeitlich auseinander statt; dazwischen liegen aufschiebende Bedingungen (Conditions Precedent, „CPs").
- **Vollzugsbedingungen:** Im SPA (Share Purchase Agreement) geregelt – typischerweise kartellrechtliche Freigabe, behördliche Genehmigungen, Zustimmungen Dritter (Change-of-Control-Klauseln), Gesellschafterbeschlüsse.
- **Kartellrecht:** §§ 35 ff. GWB (Bundeskartellamt / BKartA), EU-Fusionskontrollverordnung (FKVO) Art. 4 ff.; ggf. Anmeldepflicht bei BKartA und/oder EU-Kommission.
- **Außenwirtschaft:** § 55 AWV (Außenwirtschaftsverordnung) – FDI-Prüfung durch BMWi/BMWK bei Erwerb durch Nicht-EU-Erwerber; § 5 AWG (kritische Infrastruktur).
- **Hauptversammlungsbeschluss:** § 179a AktG – Übertragung des gesamten Gesellschaftsvermögens erfordert HV-Beschluss; § 293 AktG (Unternehmensvertrag).
- **Insolvenzantragspflicht:** § 15a GmbHG – spätestens 3 Wochen nach Zahlungsunfähigkeit / Überschuldung; relevant bei Distressed M&A.
- **Abtretung Geschäftsanteile:** § 15 Abs. 3, 4 GmbHG – notarielle Form für Abtretungsvertrag.

## Checklisten-Datei

Unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/mandate/[code]/vollzugs-checkliste.yaml`. Struktur:

```yaml
deal_code: "Projekt Falke"
zieldatum_vollzug: [DATUM]
signing_datum: [DATUM]
zuletzt_aktualisiert: [DATUM]

vollzugsbedingungen:
  - id: VB-001
    punkt: "Kartellrechtliche Freigabe Bundeskartellamt"
    kategorie: "Behördliche Genehmigung"
    verantwortlich: "Käufer-Anwalt"
    faellig: 2025-06-15
    status: "Angemeldet 01.04.2025; Wartefrist läuft (§ 40 Abs. 1 GWB: 1 Monat)"
    blockierend: true
    quelle: "SPA § 7.1(a)"

  - id: VB-002
    punkt: "Zustimmung Acme GmbH – Change-of-Control § 14 Rahmenvertrag"
    kategorie: "Zustimmung Dritter"
    verantwortlich: "Zielgesellschaft – Frau Schmitt"
    faellig: 2025-06-20
    status: "Anfrage versandt 10.04.2025; keine Antwort"
    blockierend: true
    quelle: "DD-Finding VB-002; Anlage 4.3(a) Nr. 7; Rahmenvertrag § 14"

vollzugslieferungen:
  - id: VL-001
    punkt: "Handelsregister-Gesellschafterliste (aktuell, § 40 GmbHG)"
    kategorie: "Gesellschaftsrechtlich"
    verantwortlich: "Ziel-Anwalt"
    faellig: 2025-06-28
    status: "Nicht begonnen"
    blockierend: true
    quelle: "SPA § 2.3(b)(iv)"

  - id: VL-002
    punkt: "Freigabe Gesellschafterdarlehen / Sicherheiten (§ 30 GmbHG)"
    kategorie: "Kapital / Darlehen"
    verantwortlich: "Ziel-Anwalt"
    faellig: 2025-06-25
    status: "In Bearbeitung"
    blockierend: true
    quelle: "SPA § 5.3(c)"
```

## Modi

### Modus 1: Initialisierung aus dem SPA

Unterschriebenes (oder quasi-finales) SPA lesen. Extrahieren:
- Jede Vollzugsbedingung (Abschnittsüberschriften variieren je SPA)
- Jede Vollzugslieferung (Vollzugslieferungsliste oder entsprechender Abschnitt)
- Jeden Covenant mit Vorvertrags-Frist

Jeder Punkt wird zu einem Checklisten-Eintrag mit Quellverweis auf den SPA-Abschnitt.

**Regelungsaspekte vor Befüllung recherchieren:**

*Fusionskontrolle:* BKartA: §§ 35–43 GWB; EU-FKVO: Art. 4, 7. Anmeldeschwellen prüfen (§ 35 GWB: kombinierter Umsatz >500 Mio. EUR UND mind. 2 Parteien >25 Mio. EUR in DE; EU-FKVO: kombinierter Weltumsatz >5 Mrd. EUR UND EU-Umsatz jeder mind. 2 Parteien >250 Mio. EUR). Wartefrist § 40 GWB: 1 Monat, verlängerbar auf 4 Monate. Vollzugsverbot bis Freigabe (§ 41 GWB). `[Modellwissen — prüfen; aktuelle Schwellen beim BKartA verifizieren]`

*FDI-Prüfung:* § 55 AWV – bei Erwerb von ≥25 % der Stimmrechte durch Nicht-EU/EWR-Erwerber in bestimmten Sektoren (Rüstung, Energie, kritische Infrastruktur, Medien); Prüffrist 4 Monate nach Vollständigkeitserklärung. `[Modellwissen — prüfen; aktuelle AWV-Sektoren verifizieren]`

*Material Adverse Change/MAC:* Deutschen SPA-Formulierungen fehlt häufig eine MAC-Definition im US-Stil; stattdessen oft „wesentliche nachteilige Veränderung" oder spezifische Auslösetatbestände. Formulierung im SPA prüfen und anwendbares Recht (typisch: deutsches Recht, § 313 BGB Wegfall der Geschäftsgrundlage) analysieren. Keine Übernahme von US-MAC-Auslegung.

### Modus 2: Einspeisung aus DD (der „selbstaktualisierend"-Teil)

Modus 2 wird ausgelöst, wenn ein vorgelagerter Skill ein Finding mit einer Vorvertrags-Handlung produziert:

- **dd-findings-extraktion Findings** – jedes Finding, das mit einer Vollzugshandlung markiert ist (Zustimmung, Gesellschafterbeschluss, Organentscheidung, behördliche Einreichung, Freigabe, Ablösung)
- **wesentliche-vertraege-anlage CoC-/Abtretungspunkte** – während der Anlage-Erstellung aufgedeckte Change-of-Control-Bestimmungen, Abtretungsbeschränkungen
- **dealteam-zusammenfassung** – aggregiert Findings und deckt manchmal Vollzugspunkte auf, die ein mechanisches Lesen einzelner Extraktions-Memos übersehen würde

Übergabeschema:

```yaml
uebergabe:
  # Pflichtfelder
  punkt: "[Gegenpartei oder Handlung, eine Zeile]"
  kategorie: "[Zustimmung Dritter | Gesellschafter-/Organentscheidung | Behördliche Einreichung | Ablösung/Kündigung | Treuhand/Einbehalt | Vollzugslieferung]"
  quelle: "[Vertragsname / gesetzliche Norm / VDR-Pfad]"
  blockierend: true
  schweregrad: "[🔴 / 🟠 / 🟡 / 🟢 — aus vorgelagertem Skill übernommen]"

  # Felder für Zustimmung / Drittmaßnahme
  gegenpartei: "[z. B. Acme GmbH]"
  buerge: "[z. B. Bürgschaft des Käufer-Mutterunternehmens erforderlich, oder k. A.]"
  bedingungen: "[substantielle Bedingung der Gegenpartei — z. B. 'Ersatzbürgschaft des Käufer-Mutterunternehmens vor Wirksamkeit der Zustimmung erforderlich']"
  ankuendigungsfrist: "[z. B. 30 Tage vor Vollzug, oder konkretes Datum]"

  # Felder für Gesellschafterentscheidung
  genehmigungsgremium: "[Gesellschafter | Vorstand | Aufsichtsrat | Behörde]"
  genehmigungsschwelle: "[z. B. 75 % der Stimmen für § 179a AktG-Beschluss]"
  normquelle: "[z. B. § 179a AktG; Gesellschaftsvertrag § 8]"

  # Timing
  geschaetzte_dauer: "[z. B. 30 Tage]"
  muss_erfolgen_vor: "[z. B. Vollzug | Signing | Ende der Wartepflicht]"
```

### Modus 3: Status-Update

```
/gesellschaftsrecht:vollzugs-checkliste
VB-002: Acme GmbH hat geantwortet, Zustimmungsformular liegt vor, benötigt Gegenzeichnung
```

### Modus 4: Was blockiert

```markdown
[ARBEITSERGEBNIS-HEADER — per Plugin-Konfiguration ## Ergebnisse]

> Dieser Statusbericht leitet sich aus dem SPA, DD-Findings und internen Deal-Unterlagen ab. Er übernimmt deren Vertraulichkeits- und Geheimnisschutz-Status – Verteilung außerhalb des Vertraulichkeitskreises (Gegenpartei, breitere Geschäftsteams) kann den Schutz aufheben.

## Vollzugschecklisten-Status — [Deal-Code] — [Datum]

**Zieldatum Vollzug:** [Datum] ([N] Tage)
**Punkte:** [N] gesamt — [N] erledigt, [N] in Bearbeitung, [N] nicht begonnen

### 🔴 Blockierend und gefährdet

| ID | Punkt | Fällig | Status | Tage bis Fälligkeit |
|---|---|---|---|---|
| [VB-XXX] | [Punkt] | [Datum] | [Status] | **[N]** |

### 🟡 Blockierend, im Zeitplan

[gleiche Tabelle]

### ✅ Erledigt

[N] Punkte — [zusammengefasste Liste]

### Nicht blockierend (nach Vollzug, informatorisch)

[N] Punkte

---

**Kritischer Pfad:** [Der/die Punkt(e), bei deren Verzögerung sich das Vollzugsdatum verschiebt]
```

## Kritische-Pfad-Analyse

Nicht alle blockierenden Punkte sind gleichwertig. Eine Zustimmung mit 30 Tagen Vorlaufzeit ist kritischer Pfad. Ein Handelsregister-Auszug mit 3 Tagen Vorlaufzeit nicht.

Für jeden blockierenden Punkt: Erledigungszeit schätzen. Punkte, bei denen `(Fälligkeitsdatum - heute) < geschätzte Dauer`, sind gefährdet. Diese kommen an den Anfang jedes Statusberichts.

## Integration: datenraum-monitor-Agent

Der Agent prüft die Checkliste täglich, zieht ggf. Statusupdates aus E-Mail/Slack, wenn verbunden, und postet den „Was blockiert"-Bericht in den Deal-Team-Kanal.

## Folgenreiche-Handlung-Sperre (Vollzugsfreigabe)

**Vor Ausstellung einer „vollzugsbereit / alle VB erfüllt"-Bestätigung oder eines Vollzugsmemos:** Falls Rolle **Nichtjurist**:

> Die Bescheinigung, dass Vollzugsbedingungen erfüllt sind, hat rechtliche Folgen – sie ist das Signal, das den Geldfluss und die nachvertraglichen Verpflichtungen auslöst. Vor Ausstellung mit einem Rechtsanwalt besprechen.

## Quellen und Zitierweise

- §§ 35–43 GWB (Fusionskontrolle BKartA)
- §§ 4, 7 EU-FKVO
- §§ 55 ff. AWV, § 5 AWG (FDI-Prüfung)
- § 179a AktG (HV-Beschluss Vermögensübertragung)
- § 15 Abs. 3, 4 GmbHG (Abtretungsform)
- § 40 GmbHG (Gesellschafterliste)
- § 313 BGB (Wegfall Geschäftsgrundlage / MAC)

Zitierweise nach `../../references/zitierweise.md`.

Kommentarliteratur:
- MüKoGmbHG/Fleischer, 4. Aufl. 2022, § 15 Rn. 90 ff. (Abtretungsform).
- Hüffer/Koch, AktG, 16. Aufl. 2023, § 179a Rn. 5 ff.
- BGH, Urt. v. 08.01.2019 – KVZ 57/17, NJW 2019, 1067 (Fusionskontrolle, Vollzugsverbot).

## Was dieser Skill nicht tut

- Er holt keine Zustimmungen ein, stellt keine Anträge, erstellt keine Dokumente. Er verfolgt, dass dies geschehen muss.
- Er entscheidet nicht, was blockiert – das SPA entscheidet das. Dieser Skill liest das SPA.
- Er vollzieht den Deal nicht. Er sagt dir, wann du es kannst.
