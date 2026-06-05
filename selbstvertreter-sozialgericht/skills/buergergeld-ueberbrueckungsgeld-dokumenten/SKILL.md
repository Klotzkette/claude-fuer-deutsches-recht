---
name: buergergeld-ueberbrueckungsgeld-dokumenten
description: "Buergergeld Ueberbrueckungsgeld Dokumenten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Buergergeld Ueberbrueckungsgeld Dokumenten

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Buergergeld Ueberbrueckungsgeld Dokumenten** im Plugin Selbstvertretung vor dem Sozialgericht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `buergergeld-ueberbrueckungsgeld` | Buergergeld Ueberbrueckungsgeld bei Haftentlassung. Skill klaert die Sondervorschrift fuer Haftentlassene den Anspruch auf Soforthilfe Bedarfsfeststellung im JVA-Kontext und Schnittstelle zu Sozialamt. Liefert Pruefraster. |
| `dokumenten-erzeugung-pdf-laien-sozialgericht` | PDF-Dateien für SG-Klage erstellen. Word zu PDF Fotos zu PDF Scannen mit Smartphone gratis Tools. Praktischer Leitfaden für Buerger ohne EDV-Kenntnisse. |
| `dolmetscher-beim-sozialgericht-laien` | Dolmetscher beim SG nach § 185 GVG. Kostenfrei für Buerger mit Sprachschwierigkeiten. Antrag muendliche Verhandlung Gebaerdensprache. |
| `dsgvo-art-15-auskunft-sozialakte` | DSGVO Artikel 15 Auskunft zur Sozialakte. Skill erklaert das Auskunftsrecht ueber gespeicherte personenbezogene Daten beim Sozialleistungstraeger Verhaeltnis zu § 25 SGB X Akteneinsicht Frist Form Kostenfreiheit und Beschwerde bei Aufsichtsbehoerde. Liefert Vorlage. |
| `eilantrag-86b-sgg-grundlagen` | Eilrechtsschutz nach § 86b SGG für Buerger. Aufschiebende Wirkung und einstweilige Anordnung. Anordnungsanspruch Anordnungsgrund existenzielle Leistungen Pflegegrad Buergergeld Krankenkasse. |

## Arbeitsweg

Im Plugin Selbstvertretung vor dem Sozialgericht gilt für **Buergergeld Ueberbrueckungsgeld Dokumenten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `buergergeld-ueberbrueckungsgeld`

**Fokus:** Buergergeld Ueberbrueckungsgeld bei Haftentlassung. Skill klaert die Sondervorschrift fuer Haftentlassene den Anspruch auf Soforthilfe Bedarfsfeststellung im JVA-Kontext und Schnittstelle zu Sozialamt. Liefert Pruefraster.

# Buergergeld Ueberbrueckungsgeld

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Buergergeld Ueberbrueckungsgeld` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Tatbestand

Haftentlassener hat unmittelbar nach Entlassung Anspruch auf Existenzsicherung.

## Anspruchsgrundlagen

- § 7 SGB II Buergergeld bei Erwerbsfaehigkeit.
- § 19 SGB XII Sozialhilfe bei Erwerbsunfaehigkeit.

## Vorbereitung waehrend Haft

- Antrag fruehzeitig stellen (mindestens 4-6 Wochen vor Entlassung).
- Sozialdienst der JVA hilft.
- Personalausweis prueffen.

## Sofortleistungen

- Bargeld zur Ueberbrueckung.
- KdU bei festem Wohnsitz.
- Kontoeroeffnung (P-Konto wegen Pfaendung von Geldstrafen).

## Schnittstelle

- Jobcenter zustaendig bei Erwerbsfaehigkeit.
- Sozialamt bei Erwerbsunfaehigkeit.
- Wenn Wohnsitz unklar: oertliche Zustaendigkeit nach § 36 SGB II klaeren.

## Pruefraster

1. Antrag fruehzeitig?
2. JVA-Sozialdienst eingebunden?
3. Personalausweis vorhanden?
4. Wohnsitz?
5. Kontoeroeffnung?

## 2. `dokumenten-erzeugung-pdf-laien-sozialgericht`

**Fokus:** PDF-Dateien für SG-Klage erstellen. Word zu PDF Fotos zu PDF Scannen mit Smartphone gratis Tools. Praktischer Leitfaden für Buerger ohne EDV-Kenntnisse.

# PDFs erzeugen — Schritt fuer Schritt

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `PDFs erzeugen — Schritt fuer Schritt` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Fuer MJP (Mein Justizpostfach) brauchen Sie PDFs. Auch Mails und viele Behoerden wollen PDFs. Diese Skill zeigt, wie Sie PDFs erstellen — auch ohne teure Software.

## In einfacher Sprache

PDF ist ein Datei-Format. Damit koennen Sie Dokumente sicher versenden. Auch ohne dass jemand sie veraendert. Wir zeigen Ihnen, wie Sie PDFs machen.

## Wann brauchen Sie diese Skill?

- Sie wollen mit MJP an das SG schreiben.
- Sie haben Papier-Dokumente und brauchen sie digital.
- Sie sind unsicher mit Computern.

## Fachbegriffe (kurz erklaert)

- **PDF**: "Portable Document Format" — eine sichere Datei, die ueberall gleich aussieht.
- **Scannen**: Papier in eine Datei verwandeln.
- **OCR**: Texterkennung (selten noetig fuer SG).

## Rechtsgrundlagen

- **§ 65a SGG** — Elektronische Einreichung.
- Verwaltungsvorschriften des MJP.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Word zu PDF

Wenn Sie die Klage am Computer schreiben:

**In Microsoft Word**:
1. Datei → Speichern unter
2. Format waehlen: PDF
3. Speichern

**In LibreOffice (gratis)**:
1. Datei → Als PDF exportieren
2. Standard-Einstellungen → OK

**Online-Tool gratis** (wenn Sie keinen Office-Programm haben):
1. www.smallpdf.com oder www.ilovepdf.com
2. Word-Datei hochladen
3. PDF herunterladen

### Schritt 2 — Foto / Scan mit Smartphone

**Mit Adobe Scan (gratis, Android und iPhone)**:
1. App installieren (Adobe Scan).
2. Dokument fotografieren.
3. App glaettet und korrigiert Foto.
4. "Speichern als PDF".

**Mit Microsoft Lens (gratis)**:
1. App installieren (Microsoft Lens).
2. Dokument fotografieren.
3. App optimiert.
4. "Speichern als PDF".

**Mit Kamera-App** (Notloesung):
1. Dokument fotografieren.
2. Foto auf den Computer laden.
3. Online umwandeln (smallpdf, ilovepdf).

### Schritt 3 — Mehrere Seiten zusammenfuehren

In Adobe Scan und Microsoft Lens koennen Sie mehrere Seiten in EIN PDF einscannen. Druecken Sie nach jedem Bild "Weiter" und nicht "Speichern". Erst am Ende speichern.

Online: smallpdf.com hat ein Tool "PDF zusammenfuehren".

### Schritt 4 — Pruefen, was im PDF steht

- Oeffnen Sie das PDF.
- Sind alle Seiten dabei?
- Ist alles lesbar?
- Stehen die Seiten richtig herum?

Wenn nicht: neu machen.

### Schritt 5 — Dateigroesse pruefen

- Klicken Sie mit rechter Maus → Eigenschaften → Groesse.
- Pro Datei nicht mehr als ca. 20 MB (MJP-Limit beachten).
- Zu gross? Mit smallpdf.com "PDF komprimieren".

### Schritt 6 — Datei sinnvoll benennen

Schlecht: "Dok1.pdf"
Gut: "K3-Hausarzt-Mueller-2026-02-01.pdf"

So weiss jeder sofort, was drin ist.

### Schritt 7 — Mehrere PDFs ordnen

Speichern Sie alle Klage-PDFs in einem Ordner. Sortieren Sie alphabetisch:

- 00-Klage.pdf (Schriftsatz)
- K1-Bescheid.pdf
- K2-Widerspruchsbescheid.pdf
- K3-Hausarzt.pdf
- usw.

## Worauf Sie besonders achten muessen

- **Lesbarkeit**: dunkler Text auf hellem Hintergrund. Bei alten Belegen kann es kritisch werden.
- **Foto-Qualitaet**: gerade halten, ausreichend Licht, Schatten vermeiden.
- **Privates schwaerzen**: Was nicht zum Streit gehoert, vorher schwaerzen (z.B. Geburtsdaten Familienmitglieder).
- **Sicheres Tool**: smallpdf, ilovepdf, Adobe Scan sind grundsaetzlich vertrauenswuerdig.

## Typische Fehler

- Foto schief → Dokument nochmal scannen
- Text unscharf → besseres Licht, gerades Halten
- Datei zu gross → komprimieren
- Privates nicht geschwaerzt → Datenschutz beachten

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `einreichung-mein-justizpostfach-mjp-sozialgericht` — MJP-Versand
- `anlagen-bezeichnen-und-sortieren-sozialgericht` — Anlagen ordnen
- `klage-zusammenstellen-bundle-sozialgericht` — Komplett-Paket

## Quellen und Aktualitaet

Stand: 05/2026. Apps und Tools veraendern sich. Bei Fragen: lokale Computer-Beratung, VHS-Kurs, Familie / Bekannte fragen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `dolmetscher-beim-sozialgericht-laien`

**Fokus:** Dolmetscher beim SG nach § 185 GVG. Kostenfrei für Buerger mit Sprachschwierigkeiten. Antrag muendliche Verhandlung Gebaerdensprache.

# Dolmetscher beim SG

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Dolmetscher beim SG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Wenn Sie kein oder nur wenig Deutsch sprechen — oder gehoerlos sind — koennen Sie einen Dolmetscher bekommen. Auf Staatskosten. Diese Skill zeigt das.

## In einfacher Sprache

Sie sprechen kein gutes Deutsch. Oder Sie sind gehoerlos. Sie haben Recht auf einen Dolmetscher. Der Staat zahlt. Wir zeigen Ihnen, wie.

## Wann brauchen Sie diese Skill?

- Sie sprechen kein oder nur wenig Deutsch.
- Sie sind gehoerlos.
- Sie verstehen die Gerichts-Sprache nicht.

## Fachbegriffe (kurz erklaert)

- **Dolmetscher**: Person, die uebersetzt.
- **Gebaerdensprache**: Sprache fuer Gehoerlose.
- **§ 185 GVG**: Recht auf Sprachmittler.

## Rechtsgrundlagen

- **§ 185 GVG** — Sprachmittlung.
- **§ 191a GVG** — Schriftliche Uebersetzung von Urteilen.
- **§ 110 SGG i.V.m. GVG** — Anwendbarkeit beim SG.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Antrag stellen

So frueh wie moeglich beim SG:

```
Sozialgericht [Ort] [Ort, Datum]

Az: [...]

Antrag auf Beistellung eines Dolmetschers

Sehr geehrte Damen und Herren,

ich beherrsche die deutsche Sprache nicht ausreichend. Meine Muttersprache ist [Sprache].

Ich beantrage, fuer den Termin am [Datum] sowie fuer die Untersuchung beim Sachverstaendigen am [Datum] einen Dolmetscher fuer [Sprache] zu bestellen.

Mit freundlichen Gruessen
```

### Schritt 2 — Sprache angeben

- Genaue Sprache (z.B. "Tuerkisch", "Arabisch (Syrisches Arabisch)")
- Bei Gebaerdensprache: DGS (Deutsche Gebaerdensprache)

### Schritt 3 — Im Termin

- Dolmetscher sitzt neben Ihnen oder am Tisch.
- Uebersetzt alles fuer Sie.
- Sie sprechen in Ihrer Muttersprache, Dolmetscher uebersetzt fuer das Gericht.

### Schritt 4 — Kosten

Sie zahlen nichts. Staatskasse uebernimmt.

### Schritt 5 — Bei schriftlichen Unterlagen

Schriftliche Uebersetzung des Urteils oder anderer Schriftstuecke ist eingeschraenkter. Aber: § 191a GVG sieht das fuer Schwerhoerige / Gehoerlose vor.

### Schritt 6 — Selbst mitgebrachter Dolmetscher

Manchmal moeglich (z.B. Familienmitglied), aber:

- Muss neutral sein
- Gericht entscheidet, ob das ausreicht
- Bei wichtigen Verfahren lieber Berufsdolmetscher

### Schritt 7 — Wenn Schwierigkeiten bei der Verstaendigung

Sagen Sie sofort: "Ich habe das nicht verstanden, bitte langsamer." Der Dolmetscher hilft dann.

## Worauf Sie besonders achten muessen

- **Sprache genau benennen** (Dialekt nennen, wenn relevant).
- **Antrag fruehzeitig**: das Gericht muss Dolmetscher organisieren.
- **Bei Aerzte-Untersuchungen**: ebenfalls Dolmetscher beantragen (Gericht muss organisieren).
- **Gebaerdensprache** und Schriftdolmetscher fuer Gehoerlose anerkannt.

## Typische Fehler

- Antrag zu spaet → kein Dolmetscher verfuegbar
- Falsche Sprache angegeben (Dialekt) → Verstaendigungs-Probleme
- "Bekannte kann uebersetzen" als Notloesung → bei wichtigen Punkten besser Profi

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `ladung-termin-sozialgericht-vorbereitung` — Ladung
- `terminvorbereitung-laien-checkliste-sozialgericht` — Vorbereitung
- `verhalten-im-saal-sozialgericht-laienleitfaden` — Verhalten

## Quellen und Aktualitaet

Stand: 05/2026. § 185 GVG aktuell. Praxis-erprobt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `dsgvo-art-15-auskunft-sozialakte`

**Fokus:** DSGVO Artikel 15 Auskunft zur Sozialakte. Skill erklaert das Auskunftsrecht ueber gespeicherte personenbezogene Daten beim Sozialleistungstraeger Verhaeltnis zu § 25 SGB X Akteneinsicht Frist Form Kostenfreiheit und Beschwerde bei Aufsichtsbehoerde. Liefert Vorlage.

# Dsgvo Art 15 Auskunft Sozialakte

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Dsgvo Art 15 Auskunft Sozialakte` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Anspruch

Art. 15 DSGVO: Recht auf Auskunft ueber verarbeitete personenbezogene Daten.

## Verhaeltnis zu § 25 SGB X

- DSGVO und SGB X stehen parallel.
- Versicherte koennen sich auf beide Anspruchsgrundlagen berufen.

## Inhalt der Auskunft

- Welche Daten werden verarbeitet?
- Verarbeitungszweck.
- Empfaenger der Daten.
- Speicherdauer.
- Herkunft der Daten.

## Frist und Form

- 1 Monat ab Antragseingang.
- Schriftlich, elektronisch oder muendlich.

## Kostenfreiheit

- Erste Auskunft kostenfrei.
- Bei wiederholten Auskuenften Kostenpauschale moeglich.

## Beschwerde

- Datenschutzbeauftragter des Bundes (BfDI) bei Bundesbehoerden.
- Landesdatenschutzbeauftragte bei Landesbehoerden.
- Beschwerde formlos.

## Vorlage

"Hiermit beantrage ich nach Art. 15 DSGVO Auskunft ueber alle zu meiner Person verarbeiteten personenbezogenen Daten. Insbesondere bitte ich um Mitteilung der Datenkategorien, der Empfaenger, der Speicherdauer und der Herkunft. Hilfsweise beantrage ich Akteneinsicht nach § 25 SGB X."

## Pruefraster

1. Antrag formuliert?
2. Frist gewahrt?
3. Vollstaendigkeit der Auskunft pruefen?
4. Beschwerde an Aufsichtsbehoerde noetig?

## 5. `eilantrag-86b-sgg-grundlagen`

**Fokus:** Eilrechtsschutz nach § 86b SGG für Buerger. Aufschiebende Wirkung und einstweilige Anordnung. Anordnungsanspruch Anordnungsgrund existenzielle Leistungen Pflegegrad Buergergeld Krankenkasse.

# Eilrechtsschutz beim Sozialgericht — § 86b SGG

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eilrechtsschutz beim Sozialgericht — § 86b SGG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Manchmal kann man nicht Monate auf eine Entscheidung warten. Wenn das Geld nicht kommt, der Strom abgeschaltet wird, ein Medikament dringend gebraucht wird — dann brauchen Sie einen Eilantrag. Diese Skill zeigt die Grundlagen.

## In einfacher Sprache

Manchmal ist es dringend. Sie brauchen Geld oder Hilfe sofort. Dann gibt es den Eilantrag. Das Gericht entscheidet schnell. Manchmal innerhalb von wenigen Tagen.

## Wann brauchen Sie diese Skill?

- Ihre Leistung wurde eingestellt und das Geld fehlt zum Leben.
- Die Krankenkasse weigert sich, eine dringende Behandlung zu bezahlen.
- Das Jobcenter zahlt nicht oder zu wenig.
- Die Pflegekasse blockiert noetige Hilfsmittel.

## Fachbegriffe (kurz erklaert)

- **Eilantrag**: Schneller Antrag, damit das Gericht vorlaeufig regelt.
- **Aufschiebende Wirkung**: Eine Massnahme der Behoerde wird gestoppt, bis entschieden ist.
- **Einstweilige Anordnung**: Das Gericht ordnet vorlaeufig etwas an (z.B. dass Sie Geld bekommen).
- **Anordnungsanspruch**: Sie haben wahrscheinlich Recht in der Hauptsache.
- **Anordnungsgrund**: Ohne sofortige Hilfe drohen schwere Nachteile.

## Rechtsgrundlagen

- **§ 86b Abs. 1 SGG** — Aufschiebende Wirkung (bei Anfechtung).
- **§ 86b Abs. 2 SGG** — Einstweilige Anordnung (bei Verpflichtung / Leistung).
- **§ 86a SGG** — Grundsatz: Widerspruch hat aufschiebende Wirkung; Ausnahmen z.B. § 39 SGB II.
- **§ 920 ZPO analog** — Glaubhaftmachung von Anspruch und Grund.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Welche Eilantrags-Art?

Zwei Varianten:

- **§ 86b Abs. 1 SGG**: Wenn ein Bescheid Sie belastet, der aufschiebende Wirkung verloren hat (z.B. Sanktion nach SGB II). Sie beantragen, dass die aufschiebende Wirkung angeordnet wird → der Bescheid wird gestoppt.
- **§ 86b Abs. 2 SGG**: Wenn Sie eine Leistung wollen, die Sie nicht bekommen (z.B. Buergergeld, Pflegehilfsmittel). Sie beantragen einstweilige Anordnung → das Gericht ordnet vorlaeufig die Leistung an.

### Schritt 2 — Pruefen, was Sie brauchen

Fuer beide gilt: Sie muessen zwei Dinge glaubhaft machen:

1. **Anordnungsanspruch**: Sie haben in der Hauptsache wahrscheinlich Recht.
2. **Anordnungsgrund**: Ohne Eilentscheidung drohen Ihnen schwere oder unumkehrbare Nachteile.

Wichtig: nicht beweisen, nur glaubhaft machen (eidesstattliche Versicherung reicht oft).

### Schritt 3 — Schriftsatz aufsetzen

Beispiel fuer Buergergeld-Eilantrag:

```
Sozialgericht [Ort] [Ort, Datum]

In dem Verfahren

[Ihr Name]
[Adresse]

— Antragsteller —

gegen

Jobcenter [Ort]
[Adresse]

— Antragsgegner —

wegen Buergergeld (Eilantrag)

stelle ich folgende ANTRAEGE:

1. Im Wege der einstweiligen Anordnung nach § 86b Abs. 2 SGG wird der Antragsgegner verpflichtet, mir vorlaeufig Buergergeld ab [Datum] in der Hoehe der Regelbedarfsstufe 1 zu gewaehren.

2. Hilfsweise: Mir vorlaeufig einen Vorschuss in Hoehe des geltenden Regelbedarfs (Regelbedarfsstufe 1) zu gewaehren.

3. Prozesskostenhilfe wird beantragt; eine Erklaerung ueber persoenliche und wirtschaftliche Verhaeltnisse liegt bei.

GRUENDE:

I. Sachverhalt
[Was ist passiert? Bescheid vom..., Widerspruch eingelegt am..., Geld fehlt seit...]

II. Anordnungsanspruch
[Warum habe ich wahrscheinlich Recht? Z.B. Vermoegen unter Schonbetrag, Bedarfsgemeinschaft falsch berechnet, keine Mitwirkungsverletzung]

III. Anordnungsgrund
Ohne Buergergeld kann ich meine Miete und meinen Lebensunterhalt nicht bezahlen. Ich verfuege nur ueber Kontoguthaben von [Betrag]. Mein letzter Einkauf erfolgte am [Datum]. Ich kann derzeit keine Lebensmittel mehr bezahlen.

Eidesstattliche Versicherung:
[Siehe unten]

Anlagen:
- Ausgangsbescheid
- Widerspruch
- Kontoauszuege letzte 3 Monate
- Mietvertrag
- Eidesstattliche Versicherung

[Unterschrift]
```

### Schritt 4 — Anlagen vorbereiten

- Bescheid und Widerspruchsbescheid
- Kontoauszuege (zeigt, wieviel Geld noch da ist)
- Mietvertrag (zeigt Verpflichtungen)
- Aerztliche Atteste (bei Gesundheits-Eilantrag)
- Bestaetigungen ueber unbezahlte Rechnungen

### Schritt 5 — Beim SG einreichen

Nicht beim Widerspruchsverfahren! Eilantrag geht direkt zum Sozialgericht.

- Schriftlich, per Fax, oder zur Niederschrift auf der Geschaeftsstelle
- Auch per Mein Justizpostfach

### Schritt 6 — Entscheidung abwarten

Das SG entscheidet meist innerhalb von 1 bis 4 Wochen. Bei akuten Faellen (Strom-Abschaltung, lebenswichtige Medikamente) auch innerhalb von Tagen.

## Worauf Sie besonders achten muessen

- **Glaubhaftmachung statt Beweis**: Eidesstattliche Versicherung ist Ihr wichtigstes Werkzeug.
- **Konkret werden**: "Ich habe kein Geld" reicht nicht; "Mein Konto zeigt 12,40 EUR Stand vom 1.5." ist konkret.
- **Hauptsache nicht vergessen**: Eilantrag ist nur vorlaeufig. Sie muessen trotzdem Widerspruch / Klage in der Hauptsache fuehren.
- **Eilantrag-Verfahren ist auch kostenfrei** beim SG (§ 183 SGG).

## Typische Fehler

- Eilantrag ans Jobcenter statt ans SG → SG ist zustaendig
- Anordnungsgrund nicht konkret → "drohende Notlage" mit Zahlen und Daten belegen
- Eidesstattliche Versicherung vergessen → immer beilegen
- Hauptsache versaeumt (kein Widerspruch / Klage) → parallel laufen lassen

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `eilantrag-buergergeld-jobcenter` — Spezialfall Buergergeld
- `eilantrag-krankenkassen-leistung` — Spezialfall Krankenkasse
- `eilantrag-pflegekassen-pflegehilfsmittel` — Spezialfall Pflege
- `eilantrag-erfolgsaussichten-checkliste` — Pruefung der Chancen
- `widerspruch-vorverfahren-78-sgg` — parallel Widerspruch

## Quellen und Aktualitaet

Stand: 05/2026. § 86b SGG aktuell. BVerfG hat Anforderungen an effektiven Eilrechtsschutz hochgehalten (Art. 19 Abs. 4 GG). Bei akuten Faellen Geschaeftsstelle anrufen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
