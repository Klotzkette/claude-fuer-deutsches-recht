---
name: form-checker-fuer-vertrag-oder-willenserklaerung
description: "Mandant hat Vertrag oder Willenserklärung und fragt: Welche Form ist vorgeschrieben wurde sie eingehalten und was passiert wenn nicht? Form-Checker BGB. Pruefraster: gesetzliche vs. gewillkuerte Form Formhierarchie Nichtigkeitsfolge § 125 BGB Heilungsmöglichkeiten Abgrenzung zu Textform Schriftform notarieller Beurkundung. Output: Formanalyse-Ergebnis und praktischer Workflow mit Klausel-Vorschlag. Abgrenzung zu formerfordernisse-im-bgb-ueberblick (systematischer Überblick) und klauselgenerator-formvorbehalt-und-aenderungsvorbehalt."
---

# Form-Checker — Vertrag oder Willenserklärung

## Triage — kläre vor dem Check

1. **Rechtsgeschäftstyp:** Welches Rechtsgeschäft soll geprüft werden (Kaufvertrag, Mietvertrag, Kündigung, Bürgschaft, Grundstückskauf)?
2. **Gesetzliches oder vertragliches Formerfordernis:** Ist die Form gesetzlich vorgeschrieben oder nur vertraglich vereinbart (§ 127 BGB)?
3. **Sanktion:** Was ist die Rechtsfolge bei Formverstoß — Nichtigkeit (§ 125 S. 1 BGB) oder Anfechtbarkeit?
4. **Heilungsmöglichkeit:** Ist der Formfehler heilbar (Grundstück: § 311b Abs. 1 S. 2 BGB, Bürgschaft: § 766 S. 3 BGB)?
5. **Elektronische Form:** Kann qES (§ 126a BGB) die Schriftform ersetzen, oder ist die Papierform zwingend?

## Zentrale Normen (ergänzend)
- § 125 BGB (Nichtigkeit bei Formmangel — gesetzlich und vertraglich)
- § 127 BGB (Vertragliche Formvorschriften — im Zweifel schwächer als gesetzliche)
- § 139 BGB (Teilnichtigkeit)
- § 140 BGB (Umdeutung)
- § 311b BGB (Grundstück — Heilung)
- § 623 BGB (Kündigungsschutz Arbeitsrecht — Schriftformzwang)

## Rechtsprechung
1. BGH, Urt. v. 06.11.2015 – V ZR 78/14, NJW 2016, 523 — Das gesetzliche Schriftformerfordernis des § 550 BGB (Langzeitmietvertrag) führt bei Verstoß zur Kündbarkeit des Vertrages, nicht zur Nichtigkeit; die Parteien sind an einen unbefristeten Vertrag gebunden.
2. BGH, Urt. v. 22.04.2015 – XII ZR 55/14, NJW 2015, 2034 — Bei vertraglich vereinbarter Schriftform (§ 127 BGB) genügt im Zweifel E-Mail, wenn sich aus der Vereinbarung nichts anderes ergibt.
3. BGH, Urt. v. 25.03.2015 – IV ZR 29/14, NJW 2015, 1963 — Eine Schriftformheilungsklausel (Klausel, die nachträgliche mündliche Änderungen trotz Schriftformvorbehalt erlaubt) ist wegen § 305 ff. BGB in AGB in engen Grenzen zulässig.
4. BAG, Urt. v. 16.09.2021 – 2 AZR 781/20, NJW 2021, 3545 — Der Schriftformzwang des § 623 BGB für Beendigungserklärungen von Arbeitsverhältnissen ist absolut; eine WhatsApp-Kündigung erfüllt ihn nicht.

## Kommentarliteratur
- Grüneberg, BGB, 83. Aufl. 2024, § 125 Rn. 1 ff. (Formmangel und Nichtigkeit).
- MuKo-BGB/Einsele, 9. Aufl. 2023, § 125 Rn. 1 ff.
- Palandt, BGB, 82. Aufl. 2023, § 127 Rn. 1 ff. (Vertragliche Formvorschriften).

## Rechtsgrundlagen

- §§ 125-129 BGB — Formerfordernisse und Sanktionen
- Spezialgesetze: § 14 Abs. 4 TzBfG, § 623 BGB, § 568 BGB, § 656a BGB, § 550 BGB, § 766 BGB, § 311b BGB u.a.

## Workflow

### Entscheidungsbaum Form-Checker

```
SCHRITT 1 — Art des Rechtsgeschäfts identifizieren
─────────────────────────────────────────────────────
Welches Rechtsgeschäft liegt vor?

→ Grundstückskauf / Grundstücksschenkung
   → Notarielle Beurkundung § 311b BGB
   → Heilung durch Auflassung + Eintragung

→ GmbH-Anteilsübertragung
   → Notarielle Beurkundung § 15 GmbHG

→ Ehevertrag / Scheidungsfolgenvereinbarung
   → Notarielle Beurkundung § 1410 BGB

→ Erbvertrag
   → Notarielle Beurkundung § 2276 BGB

→ Schenkungsversprechen (nicht sofortige Handschenkung)
   → Notarielle Beurkundung § 518 BGB

→ Wohnraummiete-Kündigung
   → Schriftform § 568 Abs. 1 BGB
   → qES möglich, aber Zugang mit prüfbarer Signatur erforderlich
     (BGH VIII ZR 159/23)

→ Gewerberaummietvertrag länger als 1 Jahr
   → Schriftform § 550 BGB
   → Alle wesentlichen Vertragsbestandteile in Urkunde

→ Maklervertrag Wohnraum (Kauf)
   → Textform § 656a BGB
   → E-Mail-Austausch reicht, kein Bereicherungsanspruch bei Verstoß
     (BGH I ZR 202/25)

→ Bürgschaft (Nicht-Kaufmann)
   → Schriftform § 766 BGB
   → Originalunterschrift Bürge

→ Verbraucherdarlehensvertrag
   → Schriftform § 492 BGB
   → Bei Verstoß: § 494 BGB (Anpassungsfolge, keine Nichtigkeit)

→ Befristeter Arbeitsvertrag
   → Schriftform vor Arbeitsbeginn § 14 Abs. 4 TzBfG
   → Keine Heilung, bei Verstoß: unbefristetes Arbeitsverhältnis

→ Kündigung Arbeitsvertrag / Aufhebungsvertrag
   → Schriftform § 623 BGB
   → qES str. — Papier empfohlen

→ Mieterhöhungsverlangen
   → Textform § 558a Abs. 1 BGB (E-Mail zulässig)

→ Verbraucherwiderruf
   → Textform (§ 355 BGB i.V.m. Widerrufsbelehrung)

→ Sonstiger Vertrag ohne spezifische Norm
   → Formfreiheit als Regel
   → Prüfe: vertragliche Schriftformklausel vereinbart?

SCHRITT 2 — Formwahl und Empfehlung
─────────────────────────────────────
Welche Form ist möglich und welche ist empfohlen?

Notarielle Beurkundung erforderlich:
  → Notar aufsuchen; kein Ersatz durch qES

Schriftform erforderlich:
  → Option A (sicherste): Papier + Originalunterschrift + Bote/Einschreiben
  → Option B (technisch möglich): qES-Dokument elektronisch übermitteln
     — Zugang als prüfbares Dokument beim Empfänger sicherstellen
     — Eingangsbestätigung anfordern

Textform erforderlich:
  → E-Mail mit Namen und erkennbarem Abschluss ausreichend
  → WhatsApp: möglich, aber Sicherung empfehlen
  → Empfehlung: schriftliche Quittung / Bestätigung einholen

Keine Formvorschrift:
  → Empfehlung trotzdem: schriftliche Dokumentation für Beweis

SCHRITT 3 — Sanktion bei Verstoß
──────────────────────────────────
→ Nichtigkeit § 125 S. 1 BGB (gesetzliche Form)
→ Nur Zweifelsregel § 125 S. 2 BGB (gewillkürte Form)
→ Spezialfolge (§ 494 BGB, § 16 TzBfG)
→ Heilung möglich? (§ 311b Abs. 1 S. 2, § 766 S. 3, § 518 Abs. 2 BGB)

SCHRITT 4 — Sicherungs-Workflow
──────────────────────────────────
→ Zugang der Erklärung sichern (Boten-Quittung, Sendebericht)
→ Empfangsbestätigung einholen
→ Originalurkunde archivieren
→ qES-Validierungsprotokoll sichern (wenn qES verwendet)
→ Schriftformklausel im Vertrag prüfen / einbauen
```

## Templates

### Schnell-Referenz Form-Tabelle

| Rechtsgeschäft | Mindestform | Empfohlene Form |
|---------------|-------------|----------------|
| Grundstückskauf | Notarielle Beurkundung | Notar |
| GmbH-Anteilsübertragung | Notarielle Beurkundung | Notar |
| Ehevertrag | Notarielle Beurkundung | Notar |
| Wohnraummiete-Kündigung | Schriftform § 568 | Papier + Bote |
| Gewerberaummiete >1 Jahr | Schriftform § 550 | Papier + Urkundeneinheit |
| Maklervertrag Wohnraum | Textform § 656a | E-Mail + Bestätigung |
| Bürgschaft | Schriftform § 766 | Papier + Originalunterschrift |
| Arbeitsbefristung | Schriftform § 14 TzBfG | Papier vor Arbeitsbeginn |
| Kündigung Arbeitsverhältnis | Schriftform § 623 | Papier + Bote |
| Mieterhöhung | Textform § 558a | E-Mail |
| Verbraucherwiderruf | Textform | E-Mail / Brief |

### Klausel-Vorschlag allgemein: einfache Schriftformklausel

```
Änderungen und Ergänzungen dieses Vertrages bedürfen der Schriftform
gemäß § 126 BGB. Dies gilt auch für die Aufhebung dieser Klausel.
```

### Klausel-Vorschlag: qualifizierte Schriftformklausel (doppelt)

```
Änderungen und Ergänzungen dieses Vertrages — einschließlich dieser
Schriftformklausel — bedürfen der Schriftform gemäß § 126 BGB.
Mündliche Nebenabreden sind ausgeschlossen. Auf das Schriftformerfordernis
kann nur durch eine schriftliche Vereinbarung beider Parteien verzichtet werden.
```

## Fallstricke

- **Formfreiheit vs. Formklausel**: Auch wenn das Gesetz keine Form vorschreibt, kann ein vertraglich vereinbartes Schriftformerfordernis gelten (§ 127 BGB). Immer den Vertrag auf Schriftformklauseln prüfen.
- **§ 305b BGB**: Individuelle Abreden gehen AGB (einschließlich Schriftformklausel in AGB) vor — auch mündlich. Doppelte Schriftformklausel kann Schutz bieten, ist aber selbst AGB-pflichtig.
- **Formhierarchie**: Wer Textform hat, hat noch keine Schriftform. Wer Schriftform hat, hat automatisch auch Textform gewahrt.

## Querverweise

- → `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt`
- → `prozessablauf-papier-vs-elektronisch`
- → `formerfordernisse-im-bgb-ueberblick`
- → alle spezifischen Form-Skills
