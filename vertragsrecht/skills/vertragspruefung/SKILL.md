---
name: vertragspruefung
description: "Prüft einen Vertrag gegen das Kanzlei-Playbook nach deutschem Recht. Identifiziert Vertragsstruktur anhand der Titelseite, ordnet das Dokument dem richtigen Prüfpfad zu (Lieferantenvertrag, NDA, AGB-Klauselkontrolle, Dienstleistungsvertrag) und erstellt ein strukturiertes Rechtsprüfungsmemo. Lädt, wenn der Nutzer Vertrag prüfen, AGB prüfen, NDA prüfen, Klauselkontrolle oder einen Vertrag zur Analyse einreicht im Vertragsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Vertragsanalyse und Klauselkontrolle

## Arbeitsbereich

Prüft einen Vertrag gegen das Kanzlei-Playbook nach deutschem Recht. Identifiziert Vertragsstruktur anhand der Titelseite, ordnet das Dokument dem richtigen Prüfpfad zu (Lieferantenvertrag, NDA, AGB-Klauselkontrolle, Dienstleistungsvertrag) und erstellt ein strukturiertes Rechtsprüfungsmemo. Lädt, wenn der Nutzer "Vertrag prüfen", "AGB prüfen", "NDA prüfen", "Klauselkontrolle" oder einen Vertrag zur Analyse einreicht. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; §§ 305 ff. BGB, NDA, SaaS- — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Inhaltskontrolle Haftungsbeschränkungsklausel; § 307 BGB; Grenze
 der Freizeichnung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (§ 305c BGB; Überraschungsklausel; Leitnorm zur AGB-Kontrolle)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Transparenzgebot; § 307 Abs. 1 S. 2 BGB; Klauselkontrolle
 Zinsanpassungsklausel)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (§ 309 Nr. 8 BGB; unzulässige Einschränkung der Gewährleistungsrechte
 in AGB)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (§ 309 Nr. 7 lit. b BGB; Haftungsfreizeichnung für grobe Fahrlässigkeit
 in AGB unwirksam)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (§ 305 Abs. 2 BGB; AGB-Einbeziehung; Anforderungen im Verbraucher- und
 B2B-Bereich)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Drittlandübertragungen; Standardvertragsklauseln)
- **LG Aachen, Urteil vom 27.05.2026, 10 O 306/25** — Button-Lösung § 312j Abs. 3 BGB im Online-Glücksspiel: Die Schaltflächenbeschriftung "Wette abgeben" genügt nicht. Verstoß führt zu endgültiger Unwirksamkeit (§ 312j Abs. 4 BGB) und Rückabwicklung nach § 812 BGB — unabhängig von glücksspielrechtlichen Konzessionsfragen. Für die Vertragsprüfung digitaler B2C-Vertragsschlüsse bedeutet das: Button-Beschriftung isoliert prüfen, nur die Worte auf dem Button zählen (im Anschluss an EuGH C-249/21 Fuhrmann-2). (Quelle: Pressehinweis Gamesright/rightmart vom 28.05.2026; Volltext bei Aufnahme noch nicht veröffentlicht.)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 — Kanzleiprofil laden

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`.
Enthält es `[PLATZHALTER]`:

> Führen Sie zuerst `/vertragsrecht:vertragsrecht-kaltstart-interview` aus — ich
> benötige Ihr Playbook, bevor ich dagegen prüfen kann.

Lies auch `## Prüfungseinstellungen` → `routing_bestätigen`. Fehlt das
Feld: als `true` behandeln.

### Schritt 2 — Vertrag einlesen

Vom Dateipfad, SharePoint-Link, Datenbank-ID oder eingefügtem Text.
Falls kein Vertrag vorliegt: danach fragen.

### Schritt 3 — Dokumentstruktur erkennen (Titel zuerst)

Vor dem Lesen des Textkörpers extrahieren:
- Haupttitel (z. B. "Dienstleistungsrahmenvertrag", "Geheimhaltungsvereinbarung")
- Alle Anlage-, Anhang-, Nachtragstitel (z. B. "Anlage 1 — AVV", "Anhang B —
 Service-Level-Vereinbarung")

Das ist das Routing-Signal. Nicht auf Body-Keywords allein verlassen.

### Schritt 4 — Prüfpfad auswählen

| Dokumenttitel enthält | Prüfpfad |
|---|---|
| Geheimhaltungsvereinbarung, NDA, Vertraulichkeitsvereinbarung (als Hauptvertrag) | **nda-prüfung** |
| Dienstleistungsrahmenvertrag, Werkvertrag, Beratungsvertrag, Servicevertrag | **lieferanten-vertrag-prüfung** |
| SaaS-Vertrag, Softwarelizenz mit Laufzeit, Cloud-Dienste-Vertrag | **saas-vertrag-prüfung** (Overlay auf lieferanten-vertrag-prüfung) |
| Auftragsverarbeitungsvertrag, AVV (als Anlage oder eigenständig) | Hinweis für **lieferanten-vertrag-prüfung** → Datenschutz-Abschnitt |
| Service-Level-Vereinbarung, SLA (als Anlage) | Hinweis für **saas-vertrag-prüfung** → SLA-Abschnitt |
| Allgemeine Geschäftsbedingungen (AGB) | AGB-Kontrolle nach §§ 305–310 BGB; Routing je nach Hauptvertrag |

Mehrere Prüfpfade möglich. Häufige Kombinationen:
- Rahmenvertrag + AVV-Anlage → lieferanten-vertrag-prüfung, mit AVV-Hinweis
- SaaS-Vertrag + Bestellformular mit automatischer Verlängerung + SLA-Anlage →
 saas-vertrag-prüfung (deckt alle drei ab)
- AGB + Individualvertrag → AGB-Kontrolle + vertragsspezifische Prüfung

Bei echter Ambiguität nach Titellektüre: die ersten zwei Seiten des Textkörpers
lesen, dann routen.

### Schritt 5 — Routing bestätigen (wenn aktiviert)

Falls `routing_bestätigen: true` im Kanzleiprofil:

```
Ich prüfe dieses Dokument als: [Vertragstyp(en)].

Erkannte Dokumente:
- [Haupttitel] → [Prüfpfad]
- [Anlage A Titel] → [Behandlung]
- [Anlage B Titel] → [Behandlung]

Ist das korrekt? (ja / nein — oder korrigieren Sie mich)
```

Auf Bestätigung warten. Bei Korrektur: Anweisung übernehmen und fortfahren.

Falls `routing_bestätigen: false`: stillschweigend fortfahren. Routing-Entscheidung
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
- Ausgelöst durch "jeglichen Verstoß" — das macht die Haftungsbegrenzung
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

**Vertragstext:** "[vollständiger Klauseltext]"

**Bewertung:** [Begründung mit §§ und BGH-Belegen]

**Gegenentwurf:**
"[vorgeschlagene Formulierung]"

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Literatur nur als vom Nutzer bereitgestellte oder lizenziert live geprüfte Quelle mit exakter Fundstelle]*

---

## Eskalation

[Sofern erforderlich — mit Adressat und Handlungsempfehlung]
```

## Beispiel

**Szenario:** IT-Dienstleistungsrahmenvertrag, Verwender-Seite, eingereicht
durch Lieferanten. Klausel: "Haftung des Auftragnehmers ist ausgeschlossen,
soweit keine grobe Fahrlässigkeit oder kein Vorsatz vorliegt."

**Prüfung:**
- Klausel: Haftungsbeschränkung auf grobe Fahrlässigkeit/Vorsatz
- Bewertung: GELB — entspricht § 309 Nr. 7 lit. b BGB (Grenze im B2C),
 im B2B zulässig (§ 310 Abs. 1 BGB), aber prüfen, ob der vollständige
 Ausschluss für leichte Fahrlässigkeit auch Kardinalpflichten erfasst
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 freigezeichnet werden)
- Gegenentwurf: "Die Haftung für die Verletzung von Kardinalpflichten
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
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 Literaturfundstellen nicht beispielhaft erfinden; bei Bedarf Platzhalter "vom Nutzer bereitgestellte/lizenziert live geprüfte Quelle" verwenden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
