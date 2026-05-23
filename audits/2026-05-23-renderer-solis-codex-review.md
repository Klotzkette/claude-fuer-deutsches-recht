# Codex-Audit-Anfrage 2026-05-23: Urteils-Renderer + Solis-Schulungsakte

@codex review

## Kontext

In v5.7.0 wurde das Plugin `urteilsbauer-relationsmacher` mit einem
Python-Renderer (`render_urteil.py`) und einer kompletten Schulungs-
akte „Solis Vision X Smartglasses" ausgeliefert. Der Renderer erzeugt
DOCX und PDF im Gerichtslayout nach § 313 ZPO. Die Schulungsakte
deckt CISG, kollidierende AGB (CH vs DE), Incoterm FOB Galway, DSGVO
als Eingriffsnorm.

## Bitte-an-Codex

Bitte prüfe in **zwei Bereichen**:

### Bereich 1 — Renderer-Code

Datei: `urteilsbauer-relationsmacher/skills/dokumente-rendern-urteil-docx/assets/render_urteil.py`

- **Code-Qualität:** Funktionen sauber strukturiert? Fehlerbehandlung
  bei fehlenden Eingabe-Dateien? Type-Hints?
- **Layout-Konformität:** Arial 11pt, Zeilenabstand, Seitenränder
  passen zum geforderten § 313 ZPO-Layout?
- **Modi-Logik:** `--typ urteil|versaeumnis|beschluss|relation` —
  schaltet der Code wirklich zwischen den unterschiedlichen
  Strukturen?
- **Sicherheits-Risiken:** Pfad-Injection, unsichere DOCX/PDF-
  Operationen?

### Bereich 2 — Solis-Schulungsakte

Verzeichnis: `testakten/solis-vision-x-smartglasses/`

- **Klagschrift (eingang/01_klagschrift.md):** ist die Klagschrift
  zivilprozessual sauber (Rubrum, Sachanträge, Begründung mit
  CISG-Argumentation, FOB Galway)?
- **AGB-Knock-out (anlagen K1 + B1):** sind die kollidierenden AGB
  realistisch widersprüchlich? Wäre der Knock-out nach BGH-
  Rechtsprechung tatsächlich anzunehmen?
- **DSGVO als Eingriffsnorm (Art. 6 + Art. 9):** ist die
  argumentative Konstruktion „DSGVO als international zwingendes
  Recht" haltbar?
- **Incoterm FOB Galway:** ist die FOB-Klausel mit den daraus
  folgenden Gefahr-Übergangs-Konsequenzen richtig dargestellt?
- **Tenor + Tatbestand + Entscheidungsgründe (output/):** ist das
  fertige Urteil juristisch konsistent zur Akte?
- **Streitwert 1577 EUR** (Testkauf 1197 + Gutachten 380) — passt
  die Streitwert-Berechnung zu § 3 ZPO + § 48 GKG?
- **Beweisbeschluss (gerichtsakte/beweisbeschluss.md):** § 358a
  ZPO-konform?
- **Protokoll der mündlichen Verhandlung:** § 160 ZPO-konform?

## Schweregrad-Bitte

**P1** juristisch falsch oder Code-Sicherheits-Bug, **P2**
handwerklicher Mangel (z.B. Form, Bezeichnungen), **P3** Stil oder
Format.

## Was passiert mit Findings

Renderer-Fixes und Akten-Korrekturen folgen in separaten Hotfix-PRs.
Dieser PR ist eine reine Review-Anforderung.
