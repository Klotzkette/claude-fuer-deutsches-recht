---
name: textform-vs-schriftform-vs-notariell
description: "Formerfordernis für einzelne Wandeldarlehens-Dokumente bestimmen und zuordnen. §§ 126 126a 126b BGB Schriftform Textform elektronische Form. Prüfraster: Vertragstyp Erklärung Beschluss gesetzliches Formerfordernis vereinbartes Formerfordernis. Output: Formzuordnungs-Memo je Dokument. Abgrenzung: nicht für Beurkundungspflicht bei Kapitalerhohung (beurkundungserfordernis-prüfung)."
---

# Textform vs. Schriftform vs. Notarielle Beurkundung

## Zweck

Dieser Skill klärt die drei Formstufen für Wandeldarlehensverträge und gibt eine praktische Empfehlung. Für das Standard-Wandeldarlehen (zweistufige Konstruktion) genügt Textform (§ 126b BGB). Phase B des Lebenszyklus.

## Eingaben

- Vertragsart: Wandeldarlehensvertrag, Gesellschafterbeschluss, Kapitalerhöhungsbeschluss, Anteilsübertragung?
- Beteiligungsstruktur: GmbH oder UG?
- Wandlungsmechanismus: einstufig oder zweistufig?
- Bereits gewählte Form im Vertragsentwurf?
- DocuSign oder andere qualifizierte elektronische Signatur gewünscht?

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform: lesbare Erklärung auf dauerhaftem Datenträger, keine Unterschrift erforderlich; DocuSign reicht)
- § 126 BGB (Schriftform: eigenhändige Namensunterschrift auf Originalurkunde; beidseitige Originalausfertigung erforderlich)
- § 126a BGB (Elektronische Form: qualifizierte elektronische Signatur nach eIDAS)
- § 127 BGB (Gewillkürte Form: strenger als gesetzliche Mindestform möglich)
- § 128 BGB (Notarielle Beurkundung: Lesung, Genehmigung, Unterschrift vor Notar)
- § 15 Abs. 3, Abs. 4 GmbHG (Beurkundungspflicht Anteilsübertragung)
- § 53 Abs. 2 GmbHG (Notarielle Beurkundung Kapitalerhöhungsbeschluss)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Formstufe für jeden Vertragsteil bestimmen

| Dokument | Mindestform | Empfehlung |
|---|---|---|
| Wandeldarlehensvertrag (zweistufig) | Textform § 126b BGB | Textform + DocuSign |
| Wandlungserklärung Lender | Textform § 126b BGB | Textform (E-Mail genügt) |
| Wandlungsmitteilung Gesellschaft | Textform § 126b BGB | Textform |
| Gesellschafterbeschluss Kapitalerhöhung | Notarielle Beurkundung § 53 Abs. 2 GmbHG | Notariell |
| Übernahmeerklärung neue Anteile | Notarielle Beurkundung § 55 Abs. 2 GmbHG | Notariell |
| Eintragungsanmeldung Handelsregister | Notarielle Beglaubigung § 78 GmbHG | Notariell |

### 2. Textform (§ 126b BGB) erläutern
Voraussetzungen: lesbare Erklärung auf dauerhaftem Datenträger (PDF, E-Mail), Person des Erklärenden erkennbar, Abschluss der Erklärung erkennbar (z. B. Name am Ende). DocuSign ist ausreichend (kein Erfordernis qualifizierter elektronischer Signatur). Vorteil: einfach, schnell, kostengünstig, fernabstimmungsfähig.

### 3. Schriftform (§ 126 BGB) – wann nötig?
Eigenhändige Namensunterschrift unter Originalurkunde. Für Wandeldarlehen nicht gesetzlich vorgeschrieben, kann aber vertraglich vereinbart werden (z. B. für Vertragsänderungen). Risiko: Verlust des Originals macht Nachweis schwierig.

### 4. Notarielle Beurkundung (§ 128 BGB) – wann zwingend?
Pflicht bei Kapitalerhöhungsbeschluss (§ 53 Abs. 2 GmbHG), Übernahmeerklärung (§ 55 Abs. 2 GmbHG), Satzungsänderung, Anteilsübertragung (§ 15 Abs. 4 GmbHG). Kosten: nach GNotKG, i.d.R. 0.5 % bis 1 % des Gegenstandswerts.

### 5. DocuSign-Praxis für Textform
Authentifizierungsstufe wählen: E-Mail-OTP ausreichend für Textform. SMS-OTP oder Personalausweis-ID für höheres Vertrauensniveau. Audit Trail herunterladen und zehn Jahre archivieren (Abgabenordnung § 147 AO). Jede Partei erhält signierte PDF.

### 6. Heilungsmechanismus
Bei Formverstoß (§ 125 BGB: Formmangel → Nichtigkeit): Heilung durch Vollziehung des Rechtsgeschäfts möglich, falls das Gesetz dies vorsieht oder die Parteien es vereinbaren (§ 9.4 Heilungsklausel). Für Wandeldarlehen: § 9.3/9.4 vorsorglich aufnehmen.

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Textform-Vertrag mit einstufiger Anteilsabtretung | Formnichtigkeit § 125 BGB | Konstruktion unklar | Zweistufige Konstruktion |
| Kapitalerhöhung ohne Notar | HR-Eintragung unmöglich | Notar noch nicht beauftragt | Notar beauftragt |
| DocuSign ohne Audit Trail | Beweisnot bei Streit | Trail unvollständig | Vollständiger Audit Trail |
| Schriftform vertraglich vereinbart, aber nur E-Mail | Vertrag in Schwebezustand | Auslegungsfrage | Klare Formregelung |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/unterzeichnung-elektronisch-docusign/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. eIDAS-VO 910/2014, GNotKG. Bei Änderung BGB-Formvorschriften aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 126 BGB (Schriftform) → § 126b BGB (Textform) → § 128 BGB i.V.m. §§ 1-17 BeurkG (notarielle Form) → § 125 BGB (Nichtigkeit bei Formmangel) → § 15 Abs. 3, 4 GmbHG (notarielle Form bei GmbH-Anteilsübertragung und Verpflichtung) → § 53 GmbHG (notarielle Beurkundung Satzungsänderung)
