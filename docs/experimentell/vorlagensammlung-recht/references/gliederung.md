# Gliederung in Vorlagen — dauerhafte verbindliche Regel

Diese Regel gilt für **alle** Vorlagen, Verträge, Schriftsätze, Anträge,
Schreiben, Beschlüsse, Plädoyers, Pläne und sonstigen Textdokumente in
diesem Repository. Sie gilt ohne Bestandsschutz für **menschliche
Mitwirkende** und für **alle Sprachmodelle und Agenten** gleichermaßen,
insbesondere Codex, Claude, Perplexity und nachfolgende Systeme. Bei jeder
neuen oder überarbeiteten Vorlage ist diese Regel aktiv anzuwenden.

## 1. Nummerierung

**Ausschließlich dezimale Nummerierung:**

```
1
1.1
1.1.1
1.1.1.1
```

**Verboten** sind:

- Römische Ziffern (`I.`, `II.`, `III.`, `IV.`, `iv)` …)
- Großbuchstaben (`A.`, `B.`, `C.` …)
- Kleinbuchstaben (`a)`, `b)`, `c)` …)
- Paragrafen-Klauselüberschriften als Gliederungsersatz (`§ 1`,
  `§ 2` …)
- Kombinationen aus Buchstaben und Zahlen (`A.1`, `B.2`, `II.1` …)
- Klammer-Buchstaben in Präambeln und Erwägungsgründen (`(A)`, `(B)`,
  `(C)`)
- Mischformen wie `A. I. 1. a) aa)` (deutscher Verlagsstil)

**Zulässig** bleibt das Paragrafenzeichen nur als **Normzitat** im
Fließtext, etwa `§ 32 BVerfGG`, `§ 174 InsO` oder `§ 1 GWB`. Es ist keine
Gliederungsnummer für Vorlagen und Verträge. Vertragsklauseln werden daher
als `1. Vertragsgegenstand`, `2. Pflichten`, `3. Vergütung` und darunter
als `1.1`, `1.2`, `2.1` gegliedert.

Bei Verträgen gilt zusätzlich: Eine Präambel steht nicht unnummeriert vor
dem Vertragstext. Wenn sie gebraucht wird, ist sie Abschnitt
`1. Präambel / Gegenstand`. Die Schlussbestimmungen müssen dann
ausdrücklich regeln, dass Abschnitt 1 Bestandteil des Vertrags ist und
Regelungsgehalt hat.

Hintergrund: Beim Querverweisen verlieren Leserinnen und Leser in
gemischten Hierarchien sofort die Orientierung. Dezimale Nummerierung
ist eindeutig, ohne Lookup-Tabelle lesbar und maschinenstabil.

### Beispiele

**Richtig:**

```markdown
## 1. Vertragsparteien

1.1 Verkäufer

Verkäuferin ist die …

1.1.1 Sitz und Vertretung

Sitz ist …

1.2 Käufer

Käuferin ist die …
```

**Falsch:**

```markdown
## I. Vertragsparteien

1. Verkäufer

a) Sitz und Vertretung

aa) Sitz

bb) Vertretung
```

## 2. Leerzeile zwischen Gliederungspunkt und Inhalt

Zwischen einer Gliederungsüberschrift und dem zugehörigen Text **muss**
eine Leerzeile stehen. Das gilt für jede Ebene, auch für fett gesetzte
Gliederungszeilen.

**Richtig:**

```markdown
## 2. Vertragsgegenstand

2.1 Hauptleistung des Verkäufers

Die Verkäuferin überträgt …

2.2 Gegenleistung des Käufers

Die Käuferin zahlt …
```

**Falsch (Text klebt an der Überschrift, fast nicht lesbar):**

```markdown
## 2. Vertragsgegenstand
2.1 Hauptleistung des Verkäufers
Die Verkäuferin überträgt …
2.2 Gegenleistung des Käufers
Die Käuferin zahlt …
```

## 3. Einrückung

Einrückung dient nur der **visuellen Hierarchie**, nicht dem Selbstzweck.

- Hauptebenen (`1.`, `2.`, `3.` …) **nicht** einrücken.
- Unterebenen (`1.1`, `1.2`) **nicht** einrücken — die dezimale Nummer
  trägt die Hierarchie selbst.
- Aufzählungen (`-`, `*`) folgen Markdown-Konvention: zwei Leerzeichen
  Einrückung pro Verschachtelungsebene, mehr nicht.
- Bei Markdown-Quelltext gilt ferner: **keine** vier-Leerzeichen-
  Einrückungen, weil Markdown diese als Codeblock interpretiert.

Zu starke Einrückung läuft am rechten Rand aus und macht den Text
optisch zerfleddert. Die dezimale Nummerierung ersetzt visuelle
Einrückung als Hierarchiesignal.

## 4. Eindeutigkeit der Verweise

Querverweise im Text und in Bearbeitungshinweisen referenzieren die
Gliederung **vollständig**:

- Richtig: „siehe Abschnitt 3.2.1"
- Falsch: „siehe a) oben" — mehrdeutig, weil mehrere `a)` im Dokument
  existieren können.

## 5. Geltung

Verbindlich für:

- Neue Vorlagen im Repository.
- Überarbeitungen bestehender Vorlagen — bei jeder inhaltlichen
  Berührung einer Vorlage wird die Gliederung mitkorrigiert.
- Pull-Request-Bodies, CHANGELOG-Einträge, README-Abschnitte — wenn
  dort Vorlagentext in größeren Auszügen wiedergegeben wird.

Nicht verbindlich für:

- Externe Zitate aus Gerichtsentscheidungen, die naturgemäß die
  Originalgliederung der zitierten Quelle behalten.

## 6. Eval-Harness

`scripts/check-gliederung.py` prüft im CI-Lauf, dass keine römischen
Ziffern, keine Buchstaben-Gliederung, keine Buchstaben-Zahlen-Mischformen
und keine Verlagsstil-Mischungen in Vorlagen vorkommen. Der Check prüft
außerdem, dass nach Gliederungsüberschriften Leerzeilen stehen.
