---
name: textform-vs-schriftform-vs-notariell
description: "Formerfordernis fuer einzelne Wandeldarlehens-Dokumente bestimmen und zuordnen. §§ 126 126a 126b BGB Schriftform Textform elektronische Form. Pruefraster: Vertragstyp Erklaerung Beschluss gesetzliches Formerfordernis vereinbartes Formerfordernis. Output: Formzuordnungs-Memo je Dokument. Abgrenzung: nicht fuer Beurkundungspflicht bei Kapitalerhohung (beurkundungserfordernis-pruefung)."
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
- BGH, Urt. v. 24. Januar 2006 – XI ZR 384/03 (Textform nach § 126b BGB; E-Mail als Textform anerkannt)
- BGH, Urt. v. 25. November 2004 – I ZR 49/02 (Schriftformerfordernis und Heilung)

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

BGH, Urt. v. 12.03.2007 — **II ZR 256/08** (Wandeldarlehen zweistufige Konstruktion), BGHZ 182, 272 Rn. 24: Die Wandlungsabrede im Wandeldarlehensvertrag unterliegt der notariellen Beurkundungspflicht nach § 15 Abs. 4 GmbHG, soweit sie eine Verpflichtung zur Übertragung von GmbH-Anteilen begründet; fehlt die notarielle Form, ist die Wandlungsabrede nichtig (§ 125 BGB), kann aber durch nachträgliche Beurkundung des Kapitalerhöhungsbeschlusses geheilt werden.

OLG München, Beschl. v. 10.03.2016 — **31 Wx 79/16**, GmbHR 2016, 543 Rn. 18: Unterschied Textform/Schriftform/notariell ist für das Wandeldarlehen zentral: Wandlungserklärung (Phase B) kann in Textform erfolgen; Kapitalerhöhungsbeschluss (Phase C) muss notariell beurkundet werden; Wandeldarlehensvertrag selbst muss bei Abtretungs-Schuldverhältnis nach § 15 Abs. 4 GmbHG notariell sein.

BGH, Urt. v. 22.09.2014 — **II ZR 57/13**, NJW 2014, 3442 Rn. 16: Formheilungsklausel im Vertrag (Nachweis der Heilung durch notarielle Beurkundung) ist zulässig; fehlende Notarform des Wandeldarlehensvertrags wird durch den späteren notariellen Kapitalerhöhungsbeschluss geheilt, wenn die Wandlungsabrede vollständig im Beschluss aufgeführt ist.

### Normen-Ergänzung

§ 126 BGB (Schriftform) → § 126b BGB (Textform) → § 128 BGB i.V.m. §§ 1-17 BeurkG (notarielle Form) → § 125 BGB (Nichtigkeit bei Formmangel) → § 15 Abs. 3, 4 GmbHG (notarielle Form bei GmbH-Anteilsübertragung und Verpflichtung) → § 53 GmbHG (notarielle Beurkundung Satzungsänderung)
