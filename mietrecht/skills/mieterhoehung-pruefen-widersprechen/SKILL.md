---
name: mieterhoehung-pruefen-widersprechen
description: Mietersicht — pruefe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begruendung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. Pruefroutine deckt Textform Wartefrist Kappungsgrenze (zwanzig Prozent oder fuenfzehn Prozent in Spannungsgebieten) und Begruendungsmittel (Mietspiegel Sachverstaendigengutachten Vergleichswohnungen) ab. Erzeugt Entwurf mit Disclaimer.
---

# Mieterhöhung prüfen und widersprechen

## Disclaimer (Schlüsselstelle)

Diese Prüfung und der nachstehende Entwurf ersetzen **keine Rechtsberatung**. Vor Versand des Schreibens an den Vermieter ist eine anwaltliche oder mietervereinsseitige Kontrolle dringend zu empfehlen. Fristversäumnisse führen zu gesetzlicher Zustimmung nach § 558b Abs. 2 BGB.

## Workflow

### Schritt 1 — Daten beschaffen

- Mieterhöhungsverlangen im Wortlaut.
- Datum des Zugangs (Briefkasten-Eintrag, E-Mail-Empfang).
- Lage- und Ausstattungsprotokoll aus dem Skill `lage-und-ausstattung-erheben`.
- Auszug aus dem aktuellen amtlichen Mietspiegel der Stadt aus `references/mietspiegel-quellen.md`.

### Schritt 2 — Formprüfung

- **Textform** nach § 558a Abs. 1 BGB (Brief, Fax, E-Mail mit Unterschriftstext genügen).
- **Empfängerangabe** alle Mieter namentlich.
- **Begründung** auf Mietspiegel, Sachverständigengutachten oder drei Vergleichswohnungen gestützt (§ 558a Abs. 2 BGB).
- **Beilage** falls Mietspiegelauszug, dann gut lesbar.

### Schritt 3 — Wartefrist und Sperrjahr

- Die neue Miete darf frühestens **fünfzehn Monate** nach Einzug oder nach der letzten Erhöhung verlangt werden (§ 558 Abs. 1 BGB).
- Berechnung dokumentieren.

### Schritt 4 — Kappungsgrenze (§ 558 Abs. 3 BGB)

- Regelgrenze **zwanzig Prozent** in drei Jahren.
- In Gebieten der Kappungsgrenzenverordnung **fünfzehn Prozent** in drei Jahren — Prüfung anhand der Landesverordnung (siehe `references/mietspiegel-quellen.md`).

### Schritt 5 — Materielle Prüfung der ortsüblichen Vergleichsmiete

- Wohnlage einordnen.
- Spanne im qualifizierten Mietspiegel suchen.
- Einordnung innerhalb der Spanne nach Orientierungshilfe (Auf- und Abschlaege für Ausstattungsmerkmale).
- Vergleichsmiete je m² ermitteln, mit Wohnfläche multiplizieren.

### Schritt 6 — Reaktionsfristen

- **Zustimmungsfrist** § 558b Abs. 2 BGB. Ablauf des zweiten Kalendermonats nach Zugang.
- Bei Schweigen: Vermieter kann auf Zustimmung klagen (§ 558b Abs. 2 Satz 2 BGB).

### Schritt 7 — Entwurfsoptionen

- **Volle Zustimmung** wenn Begehren formal und materiell richtig ist.
- **Teilzustimmung** bis zur tatsächlich ortsüblichen Vergleichsmiete.
- **Verweigerung** bei Formfehlern, Verstoß gegen Wartefrist oder Kappungsgrenze.

## Schreiben-Entwurf

Erzeuge ein höflich-bestimmtes Schreiben mit:

1. Bezugnahme auf das Verlangen vom (Datum).
2. Rechtliche Prüfung punktweise (Form, Frist, Kappungsgrenze, ortsübliche Vergleichsmiete).
3. Eindeutige Erklärung (Zustimmung, Teilzustimmung, Verweigerung).
4. Aufforderung zur schriftlichen Bestätigung.
5. **Disclaimer am Ende** — Hinweis, dass dies kein anwaltliches Schreiben ist und der Mieter sich beraten lassen sollte.
