---
name: saas-msa-pruefung
description: Prüfung von SaaS-Abonnement- und Rahmenverträgen (MSA) mit Schwerpunkt auf AGB-Kontrolle (§§ 305–310 BGB), automatischer Verlängerung, Preiseskalation, Datenschutz (Art. 28 DSGVO), Haftungsbegrenzung und Vertragsstrafe (§ 339 BGB). Wird von /vertragsrecht:pruefen geladen, wenn ein SaaS- oder Abonnementvertrag erkannt wird.
language: de
triggers:
  - "saas"
  - "msa"
  - "softwarevertrag"
  - "abonnement"
  - "cloudvertrag"
  - "avv"
  - "rahmenvertrag"
---

# SaaS-/MSA-Prüfung

## Zweck

SaaS-Verträge haben ein anderes Risikoprofil als einmalige Lieferantenverträge. Die Kosten akkumulieren über Verlängerungen, die Daten häufen sich an, und die Wechselkosten wachsen monatlich. Dieser Skill prüft unter Berücksichtigung dieser Besonderheiten. Er führt die Standard-Playbook-Prüfung aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` durch und ergänzt sie um einen SaaS-spezifischen Prüfaufschlag für die Punkte, die bei Abonnementverträgen besonders gefährlich sind.

## Eingaben

- SaaS-/MSA-Vertrag (Datei-Upload oder Direkteingabe)
- Ggf. Auftragsformular (Order Form) separat
- AVV/DPA (falls als separates Dokument)
- Kontext: Auftraggeber oder Auftragnehmer?
- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert, aktive Akte prüfen. Falls keine aktive Akte, fragen.

## Ablauf

### Schritt 1: Playbook laden und Seite bestimmen

**Welche Seite?** Vor der Playbook-Anwendung ermitteln:
- Gegenpartei ist SaaS-Anbieter, der die Plattform verkauft → Käuferseite
- Das Unternehmen ist SaaS-Anbieter, Gegenpartei ist Kunde → Verkäuferseite
- Reseller/White-Label? → Fragen: „Auf welcher Seite steht [Unternehmen] – Anbieter oder Kunde?"

Aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` den zutreffenden Playbook-Abschnitt lesen. Falls nicht konfiguriert: Setup-Befehl nennen.

AGB-Kontrolle nach §§ 305–310 BGB:
- Einbeziehungsvoraussetzungen (§ 305 Abs. 2 BGB) prüfen
- Überraschende Klauseln (§ 305c BGB)
- Transparenzgebot (§ 307 Abs. 1 S. 2 BGB)
- Klauselverbote §§ 308, 309 BGB (direkt anwendbar gegenüber Verbrauchern; im B2B als Indiz, BGH, Urt. v. 31.10.1984 – VIII ZR 226/83, NJW 1985, 623)
- Bei B2B: § 310 Abs. 1 BGB – eingeschränkte Kontrolle, aber § 307 BGB gilt

### Schritt 2: Standard-Playbook-Prüfung

Alle Standard-Checkpunkte aus dem Lieferantenvertrag-Prüfungs-Skill anwenden: Haftung, Freistellung, IP, Datenschutz, Laufzeit/Kündigung, Gerichtsstand. Ergebnisse in die SaaS-spezifische Ausgabe integrieren.

### Schritt 3: SaaS-spezifischer Prüfaufschlag

#### 3.1 Automatische Verlängerung (§ 309 Nr. 9 BGB; § 307 BGB)

Der häufigste Weg, bei dem ein SaaS-Deal schiefläuft: niemand bemerkt das Kündigungsfenster, und das Unternehmen ist für ein weiteres Jahr zum höheren Preis gebunden.

Prüfen und mit CLAUDE.md-Positionen vergleichen:

| Element | Inhalt | Playbook-Position |
|---|---|---|
| Verlängerungslaufzeit | z. B. gleich wie Erstlaufzeit / länger / mehrjährig | [aus CLAUDE.md] |
| Kündigungsfrist | Tage vor Verlängerung | [aus CLAUDE.md] |
| Kündigungsform | E-Mail / Schriftform / Portal / Einschreiben | [aus CLAUDE.md] |
| Preis bei Verlängerung | gleich / CPI-begrenzt / jeweils aktueller Listenpreis | [aus CLAUDE.md] |

**B2C-Hinweis:** § 309 Nr. 9 BGB verbietet stillschweigende Verlängerungen um mehr als 1 Jahr und Kündigungsfristen von mehr als 3 Monaten. Im B2B-Bereich gilt § 307 BGB als Maßstab; übermäßige Kündigungsfristen können unwirksam sein. `[Trainingswissen – prüfen]`

**Fristenerfassung:** Genaues Verlängerungsdatum und Kündigungsfenster unabhängig von Beanstandungen extrahieren. Daten für den Verlängerungstracker-Skill erfassen.

#### 3.2 Preiseskalation

Prüfen und mit CLAUDE.md vergleichen:

| Element | Inhalt |
|---|---|
| Jährliche Erhöhungsklausel | fester %, VPI, unbegrenzt |
| Überverbrauch-Preise | Veröffentlichte Preisliste / Prämienrate / undefiniert |
| Umfang „Vergütung" | nur Abonnement / „Zusatzleistungen" weit definiert |

**AGB-Hinweis (§ 307 BGB):** Einseitige Preiserhöhungsklauseln ohne sachgerechten Grund oder ohne ausreichende Ankündigung sind gegenüber Verbrauchern regelmäßig unwirksam. Im B2B ist die Schwelle höher, aber § 307 BGB gilt. BGH, Urt. v. 15.11.2006 – VIII ZR 3/06, NJW 2007, 1054 – Preisanpassungsklausel. `[Trainingswissen – prüfen]`

#### 3.3 Datenportabilität und Exit

Wenn (nicht falls) das Unternehmen den Anbieter wechselt: Können die Daten mitgenommen werden?

| Element | Inhalt |
|---|---|
| Exportformat | offen/standardisiert / proprietär-dokumentiert / „wirtschaftlich zumutbar" |
| Export-Verfügbarkeit | Selbstbedienung jederzeit / auf Anfrage / nur bei Kündigung |
| Zugang nach Vertragsende | Tage nach Kündigung |
| Exportkosten | kostenlos / T&M / je GB oder Datensatz |
| Löschbestätigung | auf Anfrage / keine / Anbieter behält Derivate |

**DSGVO-Hinweis (Art. 20 DSGVO):** Datenportabilität ist für personenbezogene Daten ein Betroffenenrecht. Der AVV sollte Löschpflichten und Rückgabe nach Vertragsende regeln (Art. 28 Abs. 3 lit. g DSGVO). Anbieterbehalt „anonymisierter" Derivate: Playbook-Position aus CLAUDE.md prüfen.

#### 3.4 Verfügbarkeit und SLA

Nur relevant, wenn das Unternehmen vom Dienst abhängt. Bei Nice-to-have-Tools überspringen.

| Element | Inhalt |
|---|---|
| Verfügbarkeitszusage | Prozentsatz / „wirtschaftlich zumutbare Bemühung" |
| Messzeitraum | monatlich / quartalsweise / jährlich |
| Abhilfe | Service-Credits (Berechnung, Deckelung, ausschließliche Abhilfe?) |
| Wartungsfenster | definierter Zeitraum / Voranmeldung / unbegrenzt |
| Credit-als-ausschließliche-Abhilfe + Haftungsdeckel | Wechselwirkung prüfen |

**AGB-Hinweis:** Klauseln, die Service-Credits als ausschließliche Abhilfe für Ausfälle festschreiben und gleichzeitig die Haftung auf ein Minimum deckeln, können nach § 307 BGB unangemessen benachteiligend sein. `[Trainingswissen – prüfen]`

#### 3.5 Sub-Auftragsverarbeiter (Art. 28 Abs. 4 DSGVO)

Die Liste der Sub-Auftragsverarbeiter ändert sich über die Laufzeit des Abonnements. Das ist ein Datenschutzproblem mit SaaS-spezifischer Dynamik.

| Element | Inhalt |
|---|---|
| Genehmigungsmodell | allgemeine Genehmigung mit Widerspruchsrecht (Art. 28 II DSGVO) / spezifische Genehmigung |
| Benachrichtigungsfrist | Tage vor Hinzufügung |
| Widerspruchsrecht | ja / nein / Sonderkündigungsrecht |
| Sitz der Sub-Auftragsverarbeiter | EU/EWR / Drittland (Art. 46 DSGVO erforderlich) |

**Art. 28 DSGVO-Pflichtprüfung:** AVV muss abgeschlossen sein, wenn personenbezogene Daten verarbeitet werden. Pflichtinhalte nach Art. 28 Abs. 3 DSGVO: Gegenstand, Dauer, Art und Zweck der Verarbeitung; Art der personenbezogenen Daten; betroffene Personengruppen; Pflichten und Rechte des Verantwortlichen.

#### 3.6 Haftungsbegrenzung in SaaS-Kontext (§§ 305–310, 307 BGB)

Standard-Haftungsprüfung aus Lieferantenvertrag-Skill anwenden. Zusätzlich SaaS-spezifisch prüfen:

- **Datenverlust-Carveout:** Haftung für Datenverlust ausgeschlossen oder begrenzt? (Kann im Widerspruch zu DSGVO-Schadensersatz Art. 82 DSGVO stehen)
- **Haftungsdeckel + Credit-als-einzige-Abhilfe-Kombination:** Wenn Credits die einzige SLA-Abhilfe sind UND die Haftung auf wenige Monatsgebühren begrenzt ist, ist die Haftung de facto minimal.
- **Unbegrenzte Haftung für IP-Verletzungen:** Marktstandard, aber Wechselwirkung mit Gesamtdeckel prüfen.

#### 3.7 Vertragsstrafe (§§ 339, 343 BGB)

Falls Vertragsstrafe (z. B. bei SLA-Verstößen oder Datenschutzverstößen) vereinbart:
- Höhe angemessen? (§ 307 BGB; § 343 BGB Herabsetzungsrecht)
- Verhältnis zur Haftungsklausel: Ist die Vertragsstrafe auf den Haftungsdeckel angerechnet?
- Kumulationsproblem: Mehrere Vertragsstrafen-Tatbestände?

## Ausgabeformat

Memo mit folgendem Aufbau:

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

⚠️ Prüfer-Hinweis
[Quellen, gelesene Seiten, gekennzeichnete Punkte, Aktualitätsprüfung]

# SaaS-/MSA-Prüfung: [Anbieter] – [Vertragsbezeichnung]

**Seite:** [Käufer / Verkäufer]
**Jahreswert (ACV):** [Betrag / nicht angegeben – bitte nennen für Eskalationsrouting]
**Laufzeit:** [Dauer, Verlängerung]
**AVV:** [beigefügt / per URL referenziert / fehlt]

---

## Zusammenfassung

[3–5 Sätze: Was ist das Wichtigste, was muss der Anwalt wissen?]

---

## Befunde (nach Schweregrad)

### 🔴 Blockierend
[Befund, §-Verweis, Zitat, Redline-Vorschlag, Eskalations-Empfehlung]

### 🟠 Hoch
[…]

### 🟡 Mittel
[…]

### 🟢 Niedrig / Zur Kenntnis
[…]

---

## SaaS-spezifische Extrakte

| Verlängerungsdatum | Kündigungsfrist | Kündigungsform | Preis bei Verlängerung |
|---|---|---|---|
| [Datum] | [Tage] | [Form] | [Methode] |

---

## Empfohlene Redlines

[Konkrete Klausel-Formulierungsvorschläge, chirurgisch und minimal]

---

## Nächste Schritte
[Entscheidungsbaum gemäß CLAUDE.md]
```

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Normen und Rspr.:
- §§ 305–310 BGB – AGB-Recht
- § 307 Abs. 1 S. 2 BGB – Transparenzgebot; BGH, Urt. v. 09.05.2012 – XII ZR 79/10, NJW 2012, 2187 Rn. 25 – Transparenzgebot
- § 309 Nr. 7 BGB – Haftungsausschlussverbote
- § 309 Nr. 9 BGB – Vertragslaufzeit
- BGH, Urt. v. 15.11.2006 – VIII ZR 3/06, NJW 2007, 1054 – Preisanpassungsklausel
- BGH, Urt. v. 31.10.1984 – VIII ZR 226/83, NJW 1985, 623 – AGB B2B
- Art. 28 DSGVO – AVV; Art. 82 DSGVO – Datenschutz-Schadensersatz
- § 339 BGB – Vertragsstrafe; § 343 BGB – Herabsetzung

Kommentare:
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 12 ff.; § 309 Rn. 1 ff.
- Bonin, in: BeckOK BGB, 70. Ed. (Stand 01.02.2025), § 307 Rn. 1 ff.
- Ulmer/Brandner/Hensen, AGB-Recht, 13. Aufl. 2023, § 307 BGB Rn. 1 ff.
- Pfeiffer, in: Wolf/Lindacher/Pfeiffer, AGB-Recht, 7. Aufl. 2022, § 307 Rn. 1 ff.

## Risiken / typische Fehler

- **AVV fehlt, obwohl personenbezogene Daten verarbeitet werden:** Bußgeldrisiko Art. 83 Abs. 4 DSGVO; Haftungsrisiko Art. 82 DSGVO.
- **Automatische Verlängerung mit kurzer Frist und fehlende Kalenderüberwachung:** Für den Verlängerungstracker-Skill extrahieren.
- **Sub-Auftragsverarbeiter-Änderungen ohne Widerspruchsrecht:** Verstoß gegen Art. 28 Abs. 2 DSGVO bei spezifischer Genehmigung.
- **Credit-als-einzige-Abhilfe + Null-Haftung:** Wechselwirkung ergibt de-facto-Haftungsausschluss; im B2C regelmäßig unwirksam nach § 307 BGB.
- **CISG-Abwahl vergessen:** Falls der SaaS-Anbieter im Ausland sitzt, CISG ausschließen.
- **Berufsrechtlicher Hinweis:** § 43a Abs. 2 BRAO, § 203 StGB bei jeder Weitergabe beachten.
