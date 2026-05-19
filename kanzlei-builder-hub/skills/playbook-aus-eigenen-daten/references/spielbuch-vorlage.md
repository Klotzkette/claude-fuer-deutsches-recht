# Spielbuch-Vorlage: `<mandatstyp>.playbook.md`

Diese Vorlage ist Pflicht-Skelett für jedes generierte Spielbuch.
Felder in `{{...}}` werden bei der Generierung gefüllt; abschnitte können
erweitert, aber nicht weggelassen werden.

---

```markdown
---
mandatstyp: {{mandatstyp_slug}}
version: {{semver}}
generiert_am: {{ISO-Datum}}
generiert_aus: {{anzahl_vergleichsfaelle}} Vergleichsfälle
verifiziert_gegen: {{anzahl_verifikationsfaelle}} Fälle
sprache: de
geltungsbereich: deutsches Recht
---

# Spielbuch: {{mandatstyp_klartext}}

## 1. Übersicht
- Typische Mandatsdauer: {{P25}} – {{P75}} Tage
- Hauptrisiken: {{risiko_top3}}
- Beteiligte Rechtsnormen: {{normen_liste}}
- Zuständige Gerichtsbarkeit: {{gerichtsbarkeit}}

## 2. Phasen

### Phase 1 — {{phasenname}}
- Dauer: {{P50}} Tage
- Eingaben: {{eingaben_liste}}
- Ausgaben: {{ausgaben_liste}}
- Standardfragen an Mandant:
  - {{frage_1}}
  - {{frage_2}}
- Standardprüfungen:
  - {{pruefung_1}}
- Standardklauseln/Textbausteine: siehe `klauselbibliothek.md` §§ {{ref}}
- Entscheidungspunkt: {{verzweigung_oder_keine}}

(weitere Phasen analog)

## 3. Sprachmuster nach Kontext

### Mandant intern (Beratungsgespräch / E-Mail)
- Anrede: {{stil}}
- Erläuterungsstil: {{stil}} (z. B. Bullet-Listen für komplexe Sachverhalte)
- Standardformulierungen:
  - {{formulierung_1}}

### Gegenseite (außergerichtlich)
- Stilebene: höflich-bestimmt, keine Drohgebärden
- Standardformulierungen (Mahnschreiben § 286 BGB, Auflösungsangebote § 9 KSchG, Vergleichsangebote § 779 BGB):
  - {{formulierung_1}}

### Gericht (Schriftsätze)
- Aufbau: Rubrum → Antrag → Sachverhalt → Rechtliche Würdigung → Beweisangebote
- Zitierweise: BGH/BAG-Pinpoint (Rn. X, nicht „Rn. X ff."), Kommentarbelege Bearbeiter/Werk/Aufl./Rn.

### Behörden
- Anrede: {{stil}}
- Verwendete Vordrucke / Standardformulare: {{liste}}

## 4. Entscheidungsbaum

```
Eingang prüfen
├─ Frist gewahrt? → Phase Klage/Antrag
│  ├─ Erfolgsaussicht > 60 % → Klage
│  └─ Erfolgsaussicht < 60 % → außergerichtl. Einigung
└─ Frist abgelaufen → § 5 KSchG / § 233 ZPO / Wiedereinsetzung
```

## 5. Fristen-Skelett

| Frist | Norm | Dauer | Beginn | Folge bei Versäumnis |
|---|---|---|---|---|
| {{frist_1}} | {{norm}} | {{dauer}} | {{beginn}} | {{folge}} |

## 6. Eskalationsmatrix

| Schwelle | Auslöser | Zuständigkeit | Aktion |
|---|---|---|---|
| niedrig | {{auslöser}} | Sachbearbeitung | Notiz im Mandat |
| mittel | {{auslöser}} | Mandatsverantwortliche | Mandantenrücksprache binnen 24 h |
| hoch | {{auslöser}} | Partner | Sofort-Telefonat + schriftliche Bestätigung |
| blockierend | {{auslöser}} | Geschäftsführung / Berufshaftpflichtversicherer | Meldung gem. AVB-RSW |

## 7. Verifikationsstatus

- Verifiziert gegen: {{fall_hash_1}}, {{fall_hash_2}}
- Trefferquote Phasenabfolge: {{prozent}} %
- Trefferquote Klauselvorschläge: {{prozent}} %
- Lücken: {{liste}}

## 8. Quellenpflicht

- Quell-Korpus (Hash-IDs, nicht entanonymisiert): {{liste}}
- Anonymisierungs-Regelsatz: `references/anonymisierungs-regeln.md` v{{x.y}}
- Letzte Rechtsprechungs-Auffrischung gegen `regulierungs-feed-monitor`-Lauf vom: {{Datum}}
- Verantwortlich (4-Augen): {{Anwalt}} + {{DSB/IT}}
```

---

## Zur Klauselbibliothek (`klauselbibliothek.md`)

- Jede Klausel mit eindeutiger ID (`KL-001` ...).
- Pro Klausel: Bezeichnung, Anwendungskontext, Wortlaut, Rechtsgrundlage,
  Gegen-Klauseln (wenn Gegenseite typischerweise widerspricht).
- Klauseln, die in Vergleichsfällen besonders häufig zum Erfolg
  beigetragen haben, werden mit Trefferzähler markiert.

## Zur Fristen-YAML (`fristen.yaml`)

- Maschinenlesbar für den `gerichtskalender-monitor`-Auslöser.
- Schema:

```yaml
- phase: <slug>
  norm: § X <Gesetz>
  dauer_tage: <int>
  fristbeginn: <slug>
  folge_bei_versaeumnis: <slug>
  ausnahme: <text>
```
