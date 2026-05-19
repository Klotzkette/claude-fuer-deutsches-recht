---
name: vertragspruefung
description: >
  Prüft einen Vertrag gegen das Kanzlei-Playbook nach deutschem Recht.
  Identifiziert Vertragsstruktur anhand der Titelseite, ordnet das Dokument
  dem richtigen Prüfpfad zu (Lieferantenvertrag, NDA, AGB-Klauselkontrolle,
  Dienstleistungsvertrag) und erstellt ein strukturiertes Rechtsprüfungsmemo.
  Lädt, wenn der Nutzer „Vertrag prüfen", „AGB prüfen", „NDA prüfen",
  „Klauselkontrolle" oder einen Vertrag zur Analyse einreicht.
language: de
triggers:
  - "Vertrag prüfen"
  - "AGB prüfen"
  - "Klauselkontrolle"
  - "NDA prüfen"
  - "Vertragsanalyse"
  - "Vertragsreview"
  - "Vertrag einreichen"
  - "Inhaltskontrolle"
  - "Vertragsgestaltung prüfen"
---

# Vertragsanalyse und Klauselkontrolle

## Zweck

Diese Skill prüft einen eingereichten Vertrag systematisch gegen das
Kanzlei-Playbook aus dem Kanzleiprofil. Sie ist das zentrale Werkzeug für
die Vertragsanalyse im täglichen Kanzleibetrieb:

- AGB-Kontrolle: Einbeziehungsprüfung (§ 305 BGB), Überraschungsklauseln
  (§ 305c BGB), Inhaltskontrolle (§ 307 BGB), Klauselverbote (§§ 308, 309 BGB)
- Gewährleistungs- und Schadensersatzklauseln (§§ 437 ff., 634 ff., 280 ff. BGB)
- Haftungsbeschränkungen und -ausschlüsse
- Datenschutz und AVV (Art. 28 DSGVO)
- Laufzeit, Kündigung und automatische Verlängerung
- Verbraucherrechtliche Besonderheiten (§§ 312 ff. BGB, Widerrufsrecht)

Lädt, wenn der Nutzer einen Vertrag zur Prüfung einreicht.

## Eingaben

- Den zu prüfenden Vertrag: Dateipfad, SharePoint-Link, Datenbankkennung
  oder direkt eingefügter Text
- Optional: Hinweis auf die Mandatsseite (Verwender/Vertragspartner-Seite),
  wenn nicht aus dem Vertrag erkennbar
- Optional: Aktives Mandat (Kürzel), wenn Mandatsarbeitsbereiche aktiviert sind

## Rechtlicher Rahmen

### AGB-Kontrolle (§§ 305–310 BGB)

**Stufe 1 — Einbeziehung (§ 305 BGB):**
- Ausdrücklicher Hinweis auf AGB vor Vertragsschluss?
- Zumutbare Möglichkeit der Kenntnisnahme?
- Einverständnis des Vertragspartners?
- Sonderfall: § 305 Abs. 2 BGB gilt nicht im unternehmerischen Verkehr
  (§ 310 Abs. 1 BGB); dort genügt kaufmännische Üblichkeit

**Stufe 2 — Überraschende und mehrdeutige Klauseln (§ 305c BGB):**
- Ist die Klausel nach den Gesamtumständen so ungewöhnlich, dass der
  Vertragspartner nicht mit ihr rechnet?
- Mehrdeutige Klauseln gehen zulasten des Verwenders (§ 305c Abs. 2 BGB)

**Stufe 3 — Inhaltskontrolle (§ 307 BGB):**
- Unangemessene Benachteiligung durch Abweichung von wesentlichen Grundgedanken
  der gesetzlichen Regelung (§ 307 Abs. 2 Nr. 1 BGB)?
- Transparenzgebot: Ist die Klausel klar und verständlich formuliert?
  (§ 307 Abs. 1 S. 2 BGB)
- Im B2B-Bereich gilt § 307 BGB vollumfänglich, §§ 308, 309 BGB nur als
  Indizien (§ 310 Abs. 1 S. 2 BGB)

**Stufe 4 — Klauselverbote (§§ 308, 309 BGB):**
- § 308 Nr. 1 BGB: Angemessene Fristen
- § 308 Nr. 4 BGB: Änderungsvorbehalte
- § 309 Nr. 7 BGB: Haftungsausschluss für Körperverletzung und grobe
  Fahrlässigkeit (absolutes Verbot)
- § 309 Nr. 8 BGB: Gewährleistungsverkürzung

### Schadensersatz (§§ 280 ff. BGB)

- § 280 Abs. 1 BGB — Schadensersatz wegen Pflichtverletzung (Grundnorm)
- § 280 Abs. 3 i.V.m. § 281 BGB — Schadensersatz statt der Leistung
- § 280 Abs. 2 i.V.m. § 286 BGB — Verzugsschadensersatz
- § 276 BGB — Vertretenmüssen; § 276 Abs. 3: Vorsatzausschluss unzulässig
- § 278 BGB — Haftung für Erfüllungsgehilfen

### Gewährleistung (§§ 437 ff., 634 ff. BGB)

- § 437 BGB — Rechte des Käufers bei Sachmangel
- § 439 BGB — Nacherfüllung als primärer Rechtsbehelf
- § 438 BGB — Verjährung der Mängelrechte (2 Jahre Regelfall, 5 Jahre bei
  Bauwerken)
- § 309 Nr. 8 lit. b aa BGB — Verkürzungsverbot: Mindestgewährleistung
  bei neu hergestellten Sachen
- § 634 BGB — Rechte des Bestellers beim Werkvertrag
- § 634a BGB — Verjährung beim Werkvertrag

### Verbraucherrecht (§§ 312 ff. BGB)

- §§ 312, 312b BGB — Verbraucherverträge, Fernabsatzverträge
- § 312g BGB — Widerrufsrecht; § 355 BGB — Ausübung; § 356 BGB — Fristen
- § 312j BGB — Pflichten im elektronischen Geschäftsverkehr
- § 475 BGB — Verbrauchsgüterkauf: Abweichungen von Gewährleistungsrecht
  zu Lasten des Verbrauchers unzulässig

### Datenschutz (DSGVO / BDSG)

- Art. 28 DSGVO — Auftragsverarbeitungsvertrag (AVV); zwingend bei
  Auftragsverarbeitung personenbezogener Daten
- Art. 28 Abs. 3 DSGVO — Mindestinhalt des AVV
- Art. 46 DSGVO — Drittlandübertragungen; Standardvertragsklauseln

### Leitentscheidungen

- BGH, Urt. v. 25.10.2016 – VI ZR 516/15, NJW 2017, 1104 Rn. 14
  (Inhaltskontrolle Haftungsbeschränkungsklausel; § 307 BGB; Grenze
  der Freizeichnung)
- BGH, Urt. v. 09.04.2014 – VIII ZR 404/12, NJW 2014, 2100 Rn. 30
  (§ 305c BGB; Überraschungsklausel; Leitnorm zur AGB-Kontrolle)
- BGH, Urt. v. 19.11.2019 – XI ZR 9/18, NJW 2020, 461 Rn. 22 ff.
  (Transparenzgebot; § 307 Abs. 1 S. 2 BGB; Klauselkontrolle
  Zinsanpassungsklausel)
- BGH, Urt. v. 14.01.2020 – VIII ZR 163/18, NJW 2020, 1431 Rn. 25
  (§ 309 Nr. 8 BGB; unzulässige Einschränkung der Gewährleistungsrechte
  in AGB)
- BGH, Urt. v. 08.12.2011 – VII ZR 111/11, NJW 2012, 1431 Rn. 20
  (§ 309 Nr. 7 lit. b BGB; Haftungsfreizeichnung für grobe Fahrlässigkeit
  in AGB unwirksam)
- BGH, Urt. v. 29.06.2011 – VIII ZR 212/08, BGHZ 190, 115 Rn. 20 ff.
  (§ 305 Abs. 2 BGB; AGB-Einbeziehung; Anforderungen im Verbraucher- und
  B2B-Bereich)
- EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2613 (Schrems II;
  Drittlandübertragungen; Standardvertragsklauseln)

### Kommentarliteratur

- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 305 Rn. 3 (Einbeziehung AGB);
  § 305c Rn. 5 (Überraschungsklausel); § 307 Rn. 1 (Inhaltskontrolle)
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 45 (Transparenzgebot);
  § 309 Rn. 80 (Klauselverbote im Einzelnen)
- Wolf/Lindacher/Pfeiffer, AGB-Recht, 7. Aufl. 2020, § 307 BGB Rn. 100
  (Generalklausel; Praxisrelevanz; Doppelautoren-Kommentar)
- Coester-Waltjen, in: Staudinger, BGB, Neubearbeitung 2022, § 307 Rn. 200
- Lehmann-Richter, in: BeckOGK BGB, 70. Ed. (Stand 01.08.2024), § 307 Rn. 150

## Ablauf

### Schritt 1 — Kanzleiprofil laden

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`.
Enthält es `[PLATZHALTER]`:

> Führen Sie zuerst `/vertragsrecht:kaltstart-interview` aus — ich
> benötige Ihr Playbook, bevor ich dagegen prüfen kann.

Lies auch `## Prüfungseinstellungen` → `routing_bestaetigen`. Fehlt das
Feld: als `true` behandeln.

### Schritt 2 — Vertrag einlesen

Vom Dateipfad, SharePoint-Link, Datenbank-ID oder eingefügtem Text.
Falls kein Vertrag vorliegt: danach fragen.

### Schritt 3 — Dokumentstruktur erkennen (Titel zuerst)

Vor dem Lesen des Textkörpers extrahieren:
- Haupttitel (z. B. „Dienstleistungsrahmenvertrag", „Geheimhaltungsvereinbarung")
- Alle Anlage-, Anhang-, Nachtragstitel (z. B. „Anlage 1 — AVV", „Anhang B —
  Service-Level-Vereinbarung")

Das ist das Routing-Signal. Nicht auf Body-Keywords allein verlassen.

### Schritt 4 — Prüfpfad auswählen

| Dokumenttitel enthält | Prüfpfad |
|---|---|
| Geheimhaltungsvereinbarung, NDA, Vertraulichkeitsvereinbarung (als Hauptvertrag) | **nda-pruefung** |
| Dienstleistungsrahmenvertrag, Werkvertrag, Beratungsvertrag, Servicevertrag | **lieferanten-vertrag-pruefung** |
| SaaS-Vertrag, Softwarelizenz mit Laufzeit, Cloud-Dienste-Vertrag | **saas-vertrag-pruefung** (Overlay auf lieferanten-vertrag-pruefung) |
| Auftragsverarbeitungsvertrag, AVV (als Anlage oder eigenständig) | Hinweis für **lieferanten-vertrag-pruefung** → Datenschutz-Abschnitt |
| Service-Level-Vereinbarung, SLA (als Anlage) | Hinweis für **saas-vertrag-pruefung** → SLA-Abschnitt |
| Allgemeine Geschäftsbedingungen (AGB) | AGB-Kontrolle nach §§ 305–310 BGB; Routing je nach Hauptvertrag |

Mehrere Prüfpfade möglich. Häufige Kombinationen:
- Rahmenvertrag + AVV-Anlage → lieferanten-vertrag-pruefung, mit AVV-Hinweis
- SaaS-Vertrag + Bestellformular mit automatischer Verlängerung + SLA-Anlage →
  saas-vertrag-pruefung (deckt alle drei ab)
- AGB + Individualvertrag → AGB-Kontrolle + vertragsspezifische Prüfung

Bei echter Ambiguität nach Titellektüre: die ersten zwei Seiten des Textkörpers
lesen, dann routen.

### Schritt 5 — Routing bestätigen (wenn aktiviert)

Falls `routing_bestaetigen: true` im Kanzleiprofil:

```
Ich prüfe dieses Dokument als: [Vertragstyp(en)].

Erkannte Dokumente:
- [Haupttitel] → [Prüfpfad]
- [Anlage A Titel] → [Behandlung]
- [Anlage B Titel] → [Behandlung]

Ist das korrekt? (ja / nein — oder korrigieren Sie mich)
```

Auf Bestätigung warten. Bei Korrektur: Anweisung übernehmen und fortfahren.

Falls `routing_bestaetigen: false`: stillschweigend fortfahren. Routing-Entscheidung
oben im Prüfungsmemo protokollieren.

### Schritt 6 — Prüfung durchführen

Den jeweiligen Prüfpfad vollständig abarbeiten. Bei mehreren Prüfpfaden:
sequenziell abarbeiten und Ausgabe in einem einzigen Memo zusammenführen.

**Struktur der Klauselprüfung (für jede prüfungsrelevante Klausel):**

1. **Klausel** — Volltext (kein Trunkieren)
2. **Bewertung** — GRÜN / GELB / ROT (nach Playbook-Kriterien)
3. **Begründung** — konkrete Abweichung vom Playbook oder zwingendes Recht;
   mit §§ und BGH-Belegen
4. **Gegenentwurf** — vorgeschlagene Formulierung mit Begründung
5. **Eskalation** — wenn die Entscheidung die Zeichnungsbefugnis übersteigt

| Bewertung | Kriterium | Maßnahme |
|---|---|---|
| **GRÜN** | Entspricht Playbook-Standard oder ist vorteilhafter | Nur zum Bewusstsein vermerken |
| **GELB** | Außerhalb Standard, aber im verhandelbaren Marktbereich | Gegenentwurf mit Fallback-Position; geschäftliche Auswirkung benennen |
| **ROT** | Außerhalb akzeptabler Grenzen; wesentliches Risiko; zwingendes Recht verletzt | Konkretes Risiko; marktübliche Alternative; Eskalationsweg empfehlen |

**Prüf-Schwerpunkte:**

**AGB-Einbeziehung (§ 305 BGB):**
Wurde auf AGB hingewiesen? War Kenntnisnahme zumutbar möglich?
Im B2B-Bereich nach § 310 Abs. 1 BGB weniger strenge Anforderungen,
aber trotzdem Hinweiserfordernis prüfen.

**Überraschungsklauseln (§ 305c BGB):**
Versteckte Haftungsausschlüsse in ungewohnten Stellen? Ungewöhnlich
weitgehende Rechte des Verwenders? Scharf auf Klauseln prüfen, die
der Vertragspartner nach dem äußeren Erscheinungsbild nicht erwarten würde.

**Inhaltskontrolle / Transparenzgebot (§ 307 BGB):**
Klare, verständliche Formulierung? Abweichung von gesetzlichem Leitbild?
Unangemessene Benachteiligung? Im B2B: ist die Benachteiligung so erheblich,
dass sie für einen redlich und verständig denkenden Kaufmann inakzeptabel wäre?

**Haftungsbeschränkung:**
- Carve-outs zwingend nach § 309 Nr. 7 lit. a BGB (Körperverletzung) und
  § 276 Abs. 3 BGB (Vorsatz) vorhanden?
- Cap-Betrag: welches Vielfaches der Vergütung?
- Symmetrie: unterschiedliche Caps für beide Seiten?
- Schadensersatz statt der Leistung (§ 281 BGB): welche Schwelle?

**Gewährleistung (§§ 437 ff., 634 ff. BGB):**
- Verjährungsfrist: kürzer als § 438 Abs. 1 Nr. 3 BGB (2 Jahre)?
  Grenze nach § 309 Nr. 8 lit. b aa BGB beachten
- Mängelrechte eingeschränkt? Nacherfüllungspflicht ausgeschlossen?
- Bei Werkvertrag: Abnahme (§ 640 BGB) und Verjährung (§ 634a BGB)

**Freistellung / Freistellungsklauseln (§ 257 BGB):**
- Einseitig zulasten einer Partei?
- Ausgelöst durch „jeglichen Verstoß" — das macht die Haftungsbegrenzung
  faktisch wirkungslos?
- Verfahren: Benachrichtigung, Verteidigungsrecht, Vergleichszustimmung?

**Datenschutz (Art. 28 DSGVO):**
- AVV vorhanden bei Auftragsverarbeitung personenbezogener Daten?
- Unterauftragnehmer: Genehmigungsvorbehalt oder nur Benachrichtigung?
- Löschfristen nach Vertragsende?
- Drittlandübertragung: Standardvertragsklauseln oder anderer Mechanismus?

**Laufzeit und Kündigung:**
- Ordentliche Kündigung: zulässig oder nur fristgebundene außerordentliche?
- Automatische Verlängerung: Ankündigungsfrist? Bei Verbrauchern
  § 309 Nr. 9 BGB beachten (max. 3 Monate Ankündigungsfrist)
- Vertragsstrafe (§ 339 BGB): angemessen? Herabsetzungsrecht nach
  § 343 BGB anwendbar?

**Verbraucherrechtliche Checks (bei B2C):**
- Widerrufsrecht (§ 312g BGB) ordnungsgemäß belehrt?
- Formvorschriften für Fernabsatz (§§ 312c, 312d BGB)?
- Schutzvorschriften §§ 307 ff. BGB im vollem Umfang anwendbar (§ 310 Abs. 3 BGB)?

### Schritt 7 — Eskalationsprüfung

Falls eine Abweichung die Zeichnungsbefugnis des Prüfers übersteigt
(gemäß Eskalationsmatrix im Kanzleiprofil): **eskalations-hinweis** aufrufen
und Eskalationsanfrage formulieren.

### Schritt 8 — Folgeangebote

- Mandantenzusammenfassung für Geschäftsführung/Vorstand
- Redline-Dokument (.docx mit Änderungsverfolgung)
- Eintrag in Fristen-Tracker (bei automatischer Verlängerung)
- Mandatsakte aktualisieren (wenn Mandatsarbeitsbereich aktiviert)

## Ausgabeformat

```markdown
[ARBEITSERGEBNIS-KENNZEICHNUNG]

# Vertragsprüfung: [Vertragspartner] — [Vertragstyp]
**Prüfdatum:** [Datum]
**Mandatsseite:** [Verwender / Vertragspartner-Seite]
**Routing:** [angewandte Prüfpfade]
**Ergebnis:** [UNTERZEICHNUNGSREIF / ÄNDERUNGEN ERFORDERLICH / ESKALATION]

---

## Zusammenfassung

[3–5 Sätze: Gesamtbewertung, kritischste Abweichung, Handlungsempfehlung]

---

## Klauselanalyse

### [Klausel-Überschrift] — [GRÜN / GELB / ROT]

**Vertragstext:** „[vollständiger Klauseltext]"

**Bewertung:** [Begründung mit §§ und BGH-Belegen]

**Gegenentwurf:**
„[vorgeschlagene Formulierung]"

*Begründung: [z. B. BGH, Urt. v. 25.10.2016 – VI ZR 516/15, NJW 2017, 1104;
Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 307 Rn. 45]*

---

## Eskalation

[Sofern erforderlich — mit Adressat und Handlungsempfehlung]
```

## Beispiel

**Szenario:** IT-Dienstleistungsrahmenvertrag, Verwender-Seite, eingereicht
durch Lieferanten. Klausel: „Haftung des Auftragnehmers ist ausgeschlossen,
soweit keine grobe Fahrlässigkeit oder kein Vorsatz vorliegt."

**Prüfung:**
- Klausel: Haftungsbeschränkung auf grobe Fahrlässigkeit/Vorsatz
- Bewertung: GELB — entspricht § 309 Nr. 7 lit. b BGB (Grenze im B2C),
  im B2B zulässig (§ 310 Abs. 1 BGB), aber prüfen, ob der vollständige
  Ausschluss für leichte Fahrlässigkeit auch Kardinalpflichten erfasst
  (BGH BGHZ 174, 1 Rn. 15 ff.: Kardinalpflichten dürfen nicht durch AGB
  freigezeichnet werden)
- Gegenentwurf: „Die Haftung für die Verletzung von Kardinalpflichten
  bleibt in Höhe des vertragstypischen, vorhersehbaren Schadens bestehen."

## Risiken und typische Fehler

- **Haftungsbeschränkung und Freistellung isoliert lesen.** Eine faktisch
  unbegrenzte Freistellungsklausel macht den Haftungsdeckel wirkungslos —
  immer beide gemeinsam bewerten.
- **B2B/B2C-Unterscheidung vergessen.** Im B2C gelten §§ 308, 309 BGB
  unmittelbar; im B2B nur § 307 BGB direkt, §§ 308, 309 BGB als Indizien.
  Das Playbook muss die typische Kundensituation ausweisen.
- **Automatische Verlängerung ohne Fristen-Check.** Eine automatische
  Verlängerung mit kurzer Kündigungsfrist kann faktisch zu einem Lock-in
  führen. Bei Verbrauchern § 309 Nr. 9 BGB beachten.
- **AVV vergessen.** Wenn der Vertrag Zugang zu personenbezogenen Daten
  des Mandanten beinhaltet und kein AVV beigefügt ist: ROT-Markierung,
  da Art. 28 DSGVO zwingend ist.
- **Klauseln trunkieren.** Bedingte Sätze immer vollständig zitieren —
  verkürzte Wiedergabe kann den Sinn entstellen.

## Quellenpflicht

Jede Klauselbewertung muss belegen:
- Den einschlägigen Paragraphen (§ 305c, § 307, § 309 Nr. 7 BGB etc.)
- Mindestens eine BGH-Entscheidung in korrekter Zitierweise
- Mindestens einen Kommentarbeleg im Bearbeiterstil „Bearbeiter, in: Werk"
  (z. B. Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 307 Rn. 45;
  Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 309 Rn. 90)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
