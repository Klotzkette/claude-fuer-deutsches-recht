---
name: eskalations-marker
description: Ordnet ein Vertragsproblem dem richtigen Genehmiger per Eskalationsmatrix aus dem Praxisprofil zu und erstellt die Genehmigungsanfrage. Laden, wenn der Nutzer fragt „wer muss das genehmigen", „eskalieren", „braucht das GC-Freigabe", „Genehmigung einholen" oder ein anderer Skill ein Problem identifiziert, das die Kompetenz des Prüfers übersteigt.
language: de
triggers:
  - "eskalation"
  - "genehmigung"
  - "eskalieren"
  - "wer genehmigt"
  - "playbook-verstoß"
  - "freigabe"
---

# Eskalationsregeln

## Zweck

Jede Rechtsabteilung hat eine Eskalationsmatrix – geschrieben oder ungeschrieben. Dieser Skill liest die geschriebene (in `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`), ordnet ein Vertragsproblem darin ein, nennt den Genehmiger beim Namen und entwirft die Anfrage – damit der Jurist nicht abends schnell eine „hast du kurz?"-E-Mail schreibt.

## Eingaben

- Beschreibung des Problems (direkt oder Verweis auf Prüfvermerk)
- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Eskalation`
- Jahreswert/ACV des Vertrags (für Betrags-Schwellenwerte)

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert, aktive Akte prüfen. Ausgaben im Akten-Ordner speichern.

## Ablauf

### Schritt 1: Matrix laden

`~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Eskalation` lesen. Falls fehlend oder vage: Hinweis, dass das Praxisprofil ergänzt werden muss.

**Welche Seite?** Käufer- oder Verkäufer-Playbook bestimmt, ob ein Begriff innerhalb der Fallback-Positionen liegt oder eine automatische Eskalation auslöst. Seite im Entwurf vermerken.

### Schritt 2: Problem einordnen

Was wird eskaliert?

- **Betrags-Schwelle:** Vertragswert übersteigt Genehmigungskompetenz
- **Klausel-Abweichung:** Ein Begriff liegt außerhalb der Playbook-Fallback-Positionen; eine erfahrenere Person muss entscheiden, ob Akzeptanz gerechtfertigt ist
- **Automatischer Eskalationsauslöser:** Immer-Eskalieren-Liste (z. B. unbegrenzte Haftung, IP-Abtretung, Datenschutzverstoß ohne Remediation, LkSG-Pflichtverletzung)
- **Geschäftliche Entscheidung:** Keine Rechtsfrage, sondern ein Thema für den Business-Owner

Dinge nicht eskalieren, die eigentlich in Ordnung sind. Wenn der Begriff innerhalb der Fallback-Positionen liegt, braucht er keine Eskalation.

### Schritt 3: Genehmiger bestimmen

Zutreffende Matrixzeile auswählen. Konkrete Person oder Rolle nennen – keine abstrakte „Führungsebene".

### Schritt 4: Anfrage entwerfen

Vorlage (immer verwenden):

```markdown
Betreff: Genehmigung erforderlich – [Vertrag] mit [Vertragspartner] – [Problembezeichnung]

[Name],

ich bitte um Genehmigung zu folgendem Vertragspunkt:

**Vertrag:** [Bezeichnung und Vertragspartner]
**ACV:** [Jahreswert]
**Klausel / Problem:** [§ X – Kurzbezeichnung]

**Was der Vertrag sagt:**
> „[wörtliches Zitat der betroffenen Klausel]"

**Was unser Playbook sagt:**
[Standard-Position aus CLAUDE.md] / [Fallback-Position aus CLAUDE.md]

**Warum das eskaliert:**
[Ein Satz: Betrags-Schwelle / Abweichung außerhalb Fallback / automatischer Auslöser / Geschäftsentscheidung]

**Risiko bei Akzeptanz ohne Änderung:**
🔴/🟠/🟡 [Rechtliches Risiko] | 🔴/🟠/🟡 [Geschäftliche Reibung]
[Konkrete Folge: z. B. „Unbegrenzte Haftung für Datenpannen; typischer Schaden bei mittelgroßem Verstoß XXX EUR"]

**Optionen:**

1. **Akzeptieren** – [Bedingung oder unkonditioniert]
   Konsequenz: [was das bedeutet, z. B. „unbegrenzte Haftung bleibt bestehen; kein Deckungsschutz D&O"]

2. **Verhandeln** – Redline: [konkrete Formulierung]
   Verhandlungsspielraum: [einschätzen, ob Markt-Standard / Gegenseite wird wahrscheinlich...]

3. **Ablehnen** – [Begründung gegenüber Gegenseite]

**Empfehlung:** Option [N] – [ein Satz Begründung]

**Entscheidung bis:** [Datum] (Verhandlungsdeadline oder Vertragsabschluss-Termin)

Bei Rückfragen stehe ich gerne zur Verfügung.

[Absender]
```

### Schritt 5: Nicht versenden

Entwurf anzeigen, Anwalt sendet. Niemals ohne ausdrückliche Bestätigung absenden.

## Ausgabeformat

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

## Eskalation: [Vertrag] mit [Vertragspartner] – [Klausel]

**Eskalationsgrund:** [Betrags-Schwelle / Klausel-Abweichung / Automatischer Auslöser / Geschäftsentscheidung]
**Genehmiger:** [Person/Rolle aus CLAUDE.md]
**Kontaktweg:** [Slack / E-Mail / Meeting]
**Seite:** [Käufer/Verkäufer – welches Playbook wurde angewendet]

---

[Entwurf der Genehmigungsanfrage gemäß Vorlage oben]

---

⚠️ Prüfer-Hinweis: Vor dem Versand prüfen, ob der Entwurf die Sachlage korrekt wiedergibt und keine privilegierten Informationen unbeabsichtigt preisgibt.
```

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen:
- § 164 ff. BGB – Vertretungsmacht; Vollmacht
- § 177 BGB – Genehmigung vollmachtlosen Handelns
- § 43a Abs. 2 BRAO – anwaltliche Verschwiegenheitspflicht
- Bei LkSG-Eskalation: §§ 5–8 LkSG – Sorgfaltspflichten, Risikoanalyse, Präventionsmaßnahmen
- Bei DSGVO-Eskalation: Art. 33, 34 DSGVO – Melde- und Benachrichtigungspflichten

## Risiken / typische Fehler

- **Zu viel eskalieren:** Wenn alles eskaliert wird, verliert die Matrix ihre Wirkung. Nur wirkliche Überschreitungen eskalieren.
- **Entscheidung vorwegnehmen:** Der Entwurf bietet Optionen – er trifft keine Entscheidung. Der Genehmiger entscheidet.
- **Frist vergessen:** Ohne Entscheidungs-Datum läuft die Verhandlung. Immer ein Datum nennen.
- **Privilegierter Inhalt außerhalb des Kreises:** Genehmigungsanfragen intern halten; § 43a Abs. 2 BRAO, § 203 StGB beachten.
