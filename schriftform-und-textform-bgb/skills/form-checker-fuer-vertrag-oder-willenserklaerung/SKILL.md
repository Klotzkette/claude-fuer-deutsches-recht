---
name: form-checker-fuer-vertrag-oder-willenserklaerung
description: "Wenn es um Form-Checker — Vertrag oder Willenserklärung in Schriftform und Textform im BGB geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

# Form-Checker — Vertrag oder Willenserklärung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor dem Check

1. **Rechtsgeschäftstyp:** Welches Rechtsgeschäft soll geprüft werden (Kaufvertrag, Mietvertrag, Kündigung, Bürgschaft, Grundstückskauf)?
2. **Gesetzliches oder vertragliches Formerfordernis:** Ist die Form gesetzlich vorgeschrieben oder nur vertraglich vereinbart (Paragraf 127 BGB)?
3. **Sanktion:** Was ist die Rechtsfolge bei Formverstoß — Nichtigkeit (Paragraf 125 S. 1 BGB) oder Anfechtbarkeit?
4. **Heilungsmöglichkeit:** Ist der Formfehler heilbar (Grundstück: Paragraf 311b Abs. 1 S. 2 BGB, Bürgschaft: Paragraf 766 S. 3 BGB)?
5. **Elektronische Form:** Kann qES (Paragraf 126a BGB) die Schriftform ersetzen, oder ist die Papierform zwingend?

## Zentrale Normen (ergänzend)
- Paragraf 125 BGB (Nichtigkeit bei Formmangel — gesetzlich und vertraglich)
- Paragraf 127 BGB (Vertragliche Formvorschriften — im Zweifel schwächer als gesetzliche)
- Paragraf 139 BGB (Teilnichtigkeit)
- Paragraf 140 BGB (Umdeutung)
- Paragraf 311b BGB (Grundstück — Heilung)
- Paragraf 623 BGB (Kündigungsschutz Arbeitsrecht — Schriftformzwang)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtsgrundlagen

- Paragrafen 125-129 BGB — Formerfordernisse und Sanktionen
- Spezialregeln: Paragraf 14 Absatz 4 TzBfG, Paragraf 623 BGB, Paragraf 568 BGB, Paragraf 656a BGB, Paragraf 578 in Verbindung mit Paragraf 550 BGB, Paragraf 766 BGB und Paragraf 311b BGB.

## Workflow

### Entscheidungsbaum Form-Checker

```
SCHRITT 1 — Art des Rechtsgeschäfts identifizieren
─────────────────────────────────────────────────────
Welches Rechtsgeschäft liegt vor?

→ Grundstückskauf / Grundstücksschenkung
 → Notarielle Beurkundung Paragraf 311b BGB
 → Heilung durch Auflassung + Eintragung

→ GmbH-Anteilsübertragung
 → Notarielle Beurkundung Paragraf 15 GmbHG

→ Ehevertrag / Scheidungsfolgenvereinbarung
 → Notarielle Beurkundung Paragraf 1410 BGB

→ Erbvertrag
 → Notarielle Beurkundung Paragraf 2276 BGB

→ Schenkungsversprechen (nicht sofortige Handschenkung)
 → Notarielle Beurkundung Paragraf 518 BGB

→ Wohnraummiete-Kündigung
 → Schriftform Paragraf 568 Abs. 1 BGB
 → qES möglich, aber Zugang mit prüfbarer Signatur erforderlich

→ Gewerberaummietvertrag länger als ein Jahr
 → Textform nach Paragraf 578 Absatz 1 in Verbindung mit Paragraf 550 BGB
 → Erklärender, lesbarer Inhalt, dauerhafter Datenträger und vollständige Vertragskette prüfen
 → Bei Altverträgen Entstehungs- und Änderungsdatum nach Artikel 229 Paragraf 70 EGBGB einordnen

→ Maklervertrag Wohnraum (Kauf)
 → Textform Paragraf 656a BGB
 → E-Mail-Austausch reicht, kein Bereicherungsanspruch bei Verstoß

→ Bürgschaft (Nicht-Kaufmann)
 → Schriftform Paragraf 766 BGB
 → Originalunterschrift Bürge

→ Verbraucherdarlehensvertrag
 → Schriftform Paragraf 492 BGB
 → Bei Verstoß: Paragraf 494 BGB (Anpassungsfolge, keine Nichtigkeit)

→ Befristeter Arbeitsvertrag
 → Schriftform vor Arbeitsbeginn Paragraf 14 Abs. 4 TzBfG
 → Keine Heilung, bei Verstoß: unbefristetes Arbeitsverhältnis

→ Kündigung Arbeitsvertrag / Aufhebungsvertrag
 → Schriftform Paragraf 623 BGB
 → direkte elektronische Form ausgeschlossen
 → Papier empfohlen; im Arbeitsgerichtsverfahren Paragraf 46h ArbGG gesondert prüfen

→ Mieterhöhungsverlangen
 → Textform Paragraf 558a Abs. 1 BGB (E-Mail zulässig)

→ Verbraucherwiderruf
 → Textform (Paragraf 355 BGB i.V.m. Widerrufsbelehrung)

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
→ Nichtigkeit Paragraf 125 S. 1 BGB (gesetzliche Form)
→ Nur Zweifelsregel Paragraf 125 S. 2 BGB (gewillkürte Form)
→ Spezialfolge (Paragraf 494 BGB, Paragraf 16 TzBfG)
→ Heilung möglich? (Paragraf 311b Abs. 1 S. 2, Paragraf 766 S. 3, Paragraf 518 Abs. 2 BGB)

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
| Wohnraummiete-Kündigung | Schriftform Paragraf 568 | Papier + Bote |
| Gewerberaummiete über ein Jahr | Textform nach Paragraf 578 Absatz 1 und Paragraf 550 | E-Mail oder anderes dauerhaft speicherbares Dokument; Vertragskette sichern |
| Maklervertrag Wohnraum | Textform Paragraf 656a | E-Mail + Bestätigung |
| Bürgschaft | Schriftform Paragraf 766 | Papier + Originalunterschrift |
| Arbeitsbefristung | Schriftform Paragraf 14 TzBfG | Papier vor Arbeitsbeginn |
| Kündigung Arbeitsverhältnis | Schriftform Paragraf 623 | Papier + Bote |
| Mieterhöhung | Textform Paragraf 558a | E-Mail |
| Verbraucherwiderruf | Textform | E-Mail / Brief |

### Klausel-Vorschlag allgemein: einfache Schriftformklausel

```
Änderungen und Ergänzungen dieses Vertrages bedürfen der Schriftform
gemäß Paragraf 126 BGB. Dies gilt auch für die Aufhebung dieser Klausel.
```

### Klausel-Vorschlag: qualifizierte Schriftformklausel (doppelt)

```
Änderungen und Ergänzungen dieses Vertrages — einschließlich dieser
Schriftformklausel — bedürfen der Schriftform gemäß Paragraf 126 BGB.
Mündliche Nebenabreden sind ausgeschlossen. Auf das Schriftformerfordernis
kann nur durch eine schriftliche Vereinbarung beider Parteien verzichtet werden.
```

## Fallstricke

- **Formfreiheit vs. Formklausel**: Auch wenn das Gesetz keine Form vorschreibt, kann ein vertraglich vereinbartes Schriftformerfordernis gelten (Paragraf 127 BGB). Immer den Vertrag auf Schriftformklauseln prüfen.
- Paragraf 305b BGB: Individuelle Abreden gehen AGB einschließlich einer doppelten Formklausel vor. Eine solche Klausel ist kein verlässlicher Ausschluss mündlicher Individualabreden; BGH, Beschluss vom 25. Januar 2017, XII ZR 69/16.
- **Formhierarchie**: Wer Textform hat, hat noch keine Schriftform. Wer Schriftform hat, hat automatisch auch Textform gewahrt.
