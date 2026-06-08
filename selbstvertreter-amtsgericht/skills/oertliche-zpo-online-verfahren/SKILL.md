---
name: oertliche-zpo-online-verfahren
description: "Oertliche ZPO Online Verfahren im Selbstvertretung am Amtsgericht: prüft konkret Bestimmung des örtlich zuständigen Amtsgerichts nach §§ 12, Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026, Rechtsmittelfrist 1 Monat nach § 517 ZPO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Oertliche ZPO Online Verfahren

## Arbeitsbereich

**Oertliche ZPO Online Verfahren** ordnet den Fall über die tragenden Prüfungslinien: Bestimmung des örtlich zuständigen Amtsgerichts nach §§ 12, Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026, Rechtsmittelfrist 1 Monat nach § 517 ZPO. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `oertliche-zuständigkeit-12-37-zpo` | Bestimmung des örtlich zuständigen Amtsgerichts nach §§ 12 ff. ZPO. Allgemeiner Gerichtsstand am Wohnsitz des Beklagten Besondere Gerichtsstaende Erfuellungsort unerlaubte Handlung Niederlassung. Wahlrecht und ausschließliche Gerichtsstaende erklärt. |
| `online-verfahren-11-buch-zpo-experimentell` | Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026. Vollständig digitales Zivilverfahren bestimmte Streitwerte teilnehmende Amtsgerichte. Aktuelle Normen-Verortung prüfen. Vergleich Praesenz-Verfahren Vorteile Risiken Strukturierte Eingabe-Masken. Teilnahme. |
| `rechtsmittelfrist-517-zpo` | Rechtsmittelfrist 1 Monat nach § 517 ZPO. Beginn mit Zustellung des vollständigen Urteils Notfrist keine Verlaengerung. Berechnung mit § 187 188 BGB Praeklusion bei Versaeumnis Wiedereinsetzung in Ausnahmefaellen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: ZPO §§ 78, 79, 129, 253, 495a, 511, 517, GVG §§ 23, 71, SGG §§ 73, 78, 87, 90, 144, 160; §23 GVG; §511 ZPO-Grenzen, Klage — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `oertliche-zuständigkeit-12-37-zpo`

**Fokus:** Bestimmung des örtlich zuständigen Amtsgerichts nach §§ 12 ff. ZPO. Allgemeiner Gerichtsstand am Wohnsitz des Beklagten Besondere Gerichtsstaende Erfuellungsort unerlaubte Handlung Niederlassung. Wahlrecht und ausschließliche Gerichtsstaende erklärt.

# Welches Amtsgericht ist oertlich zuständig?

## Worum geht es?

Es reicht nicht zu wissen, dass das AG zuständig ist — Sie muessen wissen, **welches** AG. Deutschland hat ueber 600 Amtsgerichte. Die ZPO regelt das in §§ 12 ff. Regel: Sie klagen am Wohnsitz des Beklagten ("allgemeiner Gerichtsstand"). Es gibt aber **besondere Gerichtsstaende**, an denen Sie als Klaeger waehlen koennen. Und es gibt **ausschliessliche Gerichtsstaende**, die alle anderen verdraengen.

## Wann brauchen Sie diese Skill?

- Sie wissen nicht, an welchem Ort Sie klagen koennen.
- Der Beklagte wohnt weit weg und Sie wollen einen naeheren Gerichtsstand pruefen.
- Sie haben eine Mietsache (Sondergerichtsstand!).

## Fachbegriffe (kurz erklaert)

- **Allgemeiner Gerichtsstand**: Standard-Gerichtsstand am Wohnsitz/Sitz des Beklagten.
- **Besonderer Gerichtsstand**: Zusaetzliche Gerichtsstaende, an denen Sie wahlweise klagen koennen.
- **Ausschliesslicher Gerichtsstand**: Verdraengt andere Gerichtsstaende, Wahlfreiheit entfaellt.
- **Erfuellungsort**: Der Ort, an dem eine Vertragsleistung zu erbringen ist.

## Rechtsgrundlagen

- **§ 12 ZPO** — Grundsatz: Allgemeiner Gerichtsstand vorrangig.
- **§ 13 ZPO** — Allg. Gerichtsstand natuerlicher Person = Wohnsitz.
- **§ 17 ZPO** — Allg. Gerichtsstand juristischer Person = Sitz.
- **§ 21 ZPO** — Niederlassungs-Gerichtsstand.
- **§ 29 ZPO** — Gerichtsstand des Erfuellungsorts.
- **§ 29a ZPO** — Ausschliesslicher Gerichtsstand für Wohnraummietsachen (Lage des Mietobjekts).
- **§ 29c ZPO** — Verbraucher-Gerichtsstand (Wohnsitz des Verbrauchers).
- **§ 32 ZPO** — Gerichtsstand der unerlaubten Handlung (Tatort).
- **§§ 38–40 ZPO** — Gerichtsstandsvereinbarung.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Ausschliesslichen Gerichtsstand pruefen

Wenn Ihr Streit unter eine **ausschliessliche** Zuständigkeit faellt, koennen Sie nirgends sonst klagen. Wichtigste Faelle:

- **Wohnraummietsache (§ 29a ZPO)**: Lage der Mietsache.
- **Dingliche Klagen ueber Grundstuecke (§ 24 ZPO)**: Lage des Grundstuecks.
- **Insolvenzanfechtung, gesellschaftsrechtliche Streitigkeiten**: jeweils Spezialregeln.

### Schritt 2 — Allgemeiner Gerichtsstand des Beklagten

Wenn nicht ausschliesslich: Wohnsitz/Sitz des Beklagten ist Standard.

- Natuerliche Person: Wohnsitz nach § 7 BGB. Im Zweifel meldete-Adresse.
- Juristische Person: Satzungssitz (Handelsregister).
- Unternehmer ohne Firmensitz: Niederlassung (§ 21 ZPO).

### Schritt 3 — Besondere Gerichtsstaende — Sie haben Wahlfreiheit

**Erfuellungsort § 29 ZPO**: Ort, an dem die geschuldete Leistung zu erbringen war.

- Geldschulden: Wohnsitz des Glaeubigers (= bei Schickschuld § 270 BGB — die genaue Anwendung ist streitig; im Zweifel BGH-Rechtsprechung pruefen).
- Werkleistung: Ort der Werkerbringung.
- Lieferung: Lieferort.

**Unerlaubte Handlung § 32 ZPO**: Tatort. Beispiele:

- Verkehrsunfall: Unfallort.
- Persoenlichkeitsverletzung: Ort der Verletzung oder Erscheinen.
- Online-Delikte: Ort, an dem die Webseite abrufbar ist (mit BGH-Einschraenkungen).

**Niederlassung § 21 ZPO**: Wenn der Beklagte (z. B. Unternehmen) eine Niederlassung hat und der Streit aus deren Geschaeften stammt.

**Verbraucher § 29c ZPO**: Bei Haustuergeschaeften am Wohnsitz des Verbrauchers. Skill `verbrauchergerichtsstand-29c-zpo`.

### Schritt 4 — Gerichtsstandsvereinbarung pruefen

Wenn beide Parteien im Vertrag einen Gerichtsstand vereinbart haben: § 38 ZPO.

- Unter Kaufleuten freie Vereinbarung.
- Bei Verbrauchern enge Voraussetzungen.

Faustregel: Mit einem Verbraucher kann ein anderer Gerichtsstand i. d. R. **nicht** wirksam vereinbart werden.

### Schritt 5 — Gerichts-Wahl bei Mehrfach-Zuständigkeit

Mehrere Gerichtsstaende gleichzeitig moeglich? Sie waehlen als Klaeger. § 35 ZPO. Aber: Praktische Erwaegungen — Anfahrt für Sie, Anfahrt für Zeugen, Sprache des Gerichts (falls dolmetscherpflichtig). Skill `dolmetscher-185-gvg`.

### Schritt 6 — Beim falschen Gericht eingeklagt?

Beklagter ruegt Unzuständigkeit in der Klageerwiderung; Gericht verweist auf Antrag nach § 281 ZPO. Wenn Beklagter ruegelos verhandelt: Gericht wird zuständig (§ 39 ZPO).

## Worauf Sie besonders achten muessen

- **Mietsache § 29a ZPO**: Ausschliesslich am Lagrort der Wohnung. Wenn Vermieter in Hamburg sitzt und Wohnung in Muenchen ist: Muenchen!
- **Online-Streit**: BGH hat Kriterien zur "bestimmungsgemaessen" Abrufbarkeit entwickelt. Bei Online-Kaufstreitigkeiten z. B. § 29c ZPO und § 32 ZPO konkurrieren.
- **Erfuellungsort bei Geldschulden**: Die alte Streitfrage Bring- vs. Schickschuld. Pruefen Sie Vertragsregelung; ansonsten ist die Streitfrage in der Praxis für Sie als Laien schwer aufzuloesen — fragen Sie ggf. die Rechtsantragsstelle (Skill `einreichung-rechtsantragsstelle-selbst`).

## Typische Fehler

- "Ich klage am eigenen Wohnsitz, das ist am bequemsten." → Nur wenn ein Gerichtsstand das hergibt (Verbrauchergerichtsstand, Erfuellungsort Schickschuld o. ae.). Sonst wird verwiesen.
- "Im Vertrag steht 'Gerichtsstand: Berlin'." → Bei Verbrauchern oft unwirksam (§ 38 ZPO eng).
- "Bei online bestellter Ware kann ich am Sitz des Online-Shops klagen." → Eher Verbrauchergerichtsstand am eigenen Wohnsitz pruefen (§ 29c ZPO).

## Querverweise

- `verbrauchergerichtsstand-29c-zpo` — Verbraucher-Vorteile.
- `sachliche-zuständigkeit-amtsgericht-23-gvg` — Welche Gerichtsstufe?
- `ausnahmen-streitwertgrenze-23-nr-2-gvg` — Mietsache, Reisevertrag.
- `klageschrift-pflichtbestandteile-253-zpo` — Klage erstellen.

## Quellen und Aktualitaet

Stand: 05/2026. §§ 12 ff. ZPO unveraendert. BGH-Rechtsprechung zum Erfuellungsort und Gerichtsstand bei Online-Delikten beachten — bei Unsicherheit Rechtsantragsstelle einschalten.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `online-verfahren-11-buch-zpo-experimentell`

**Fokus:** Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026. Vollständig digitales Zivilverfahren bestimmte Streitwerte teilnehmende Amtsgerichte. Aktuelle Normen-Verortung prüfen. Vergleich Praesenz-Verfahren Vorteile Risiken Strukturierte Eingabe-Masken. Teilnahme.

# Online-Verfahren — das neue digitale Zivilverfahren

## Worum geht es?

Seit 2025 gibt es in Deutschland ein **experimentelles vollstaendig digitales Zivilverfahren** ("Online-Verfahren"). Es ermoeglicht, einen Zivilrechtsstreit von Anfang bis Ende ueber eine Internet-Plattform zu fuehren — ohne Papier, ohne persönliche Termine vor Ort. Das Verfahren ist in einem neuen Buch der ZPO (vermutlich 11. Buch) verankert und gilt zunaechst nur an **teilnehmenden Amtsgerichten** und für **bestimmte Streit-Typen**.

**Wichtig:** Die genaue Norm-Verortung (Paragraphennummer, Geltungsbereich, Schwellenwerte) ist im laufenden Gesetzgebungs- und Erprobungs-Verfahren. **Verifizieren Sie die aktuellen Normen in amtliche/freie Quellen oder lizenzierte Datenbanken und auf der Webseite Ihres oertlich zuständigen Amtsgerichts.**

## In einfacher Sprache

Es gibt ein neues Online-Gericht. Sie machen alles am Computer. Sie reichen die Klage ein. Sie sehen die Antwort der Gegenseite am Bildschirm. Manchmal gibt es ein Video-Treffen. Das gibt es nur bei einigen Gerichten und nur für bestimmte Streit-Themen.

## Wann brauchen Sie diese Skill?

- Sie wollen klagen und Ihr Amtsgericht bietet das Online-Verfahren an.
- Sie wurden in einem Online-Verfahren verklagt.
- Sie wollen wissen, ob das Online-Verfahren für Ihren Fall passt.

## Fachbegriffe (kurz erklaert)

- **Online-Verfahren**: Ein voll-digitales Zivilverfahren auf einer Internet-Plattform.
- **Experimentier-Klausel**: Eine Gesetzesregelung, die ein neues Verfahren erstmal in einem Test-Modus zulaesst.
- **Strukturierte Eingabe-Maske**: Ein Formular auf der Plattform, in das Sie Ihren Sachverhalt Schritt für Schritt eintippen.
- **Teilnehmende Gerichte**: Nicht jedes Amtsgericht bietet das Online-Verfahren an. Eine Liste finden Sie auf der Webseite der Justiz Ihres Bundeslandes.

## Rechtsgrundlagen (Stand 2026)

- **11. Buch ZPO (Online-Verfahren)** — neues Buch der Zivilprozessordnung, eingefuehrt mit dem Gesetz zur Förderung digitaler Justiz-Verfahren (genaues Inkrafttreten und Paragraphen verifizieren).
- **§ 128a ZPO** — Video-Verhandlung (auch im klassischen Verfahren moeglich, vgl. `video-verhandlung-128a-zpo`).
- **§ 130a ZPO** — elektronische Einreichung (gilt auch im klassischen Verfahren).

**Verifizieren Sie die aktuelle Rechtslage** in amtliche/freie Quellen oder lizenzierte Datenbanken — die Normen-Nummerierung und der Anwendungsbereich des Online-Verfahrens werden im Erprobungs-Zeitraum noch praezisiert.

## Was unterscheidet das Online-Verfahren vom normalen Verfahren?

| Merkmal | Normales Verfahren | Online-Verfahren |
|-----------------------|------------------------------------------|---------------------------------------------------------|
| Klage einreichen | Papier oder MJP oder § 130a ZPO | Strukturierte Eingabe-Maske auf der Plattform |
| Klageschrift | Freier Text in Word/PDF | Vorgegebene Felder (Antrag, Sachverhalt, Beweise) |
| Schriftverkehr | E-Mail, Post, MJP | Plattform-internes Postfach |
| Termin | Im Gerichtssaal | Video-Konferenz auf der Plattform |
| Urteil | Schriftlich per Post | Im Plattform-Postfach |
| Akteneinsicht | Geschaeftsstelle, Anwalt | Plattform jederzeit |

## Vorteile

- **Niedrigschwellig**: Strukturierte Maske hilft Laien, alles Wichtige anzugeben.
- **Kein Papier**: Alles digital.
- **Termin von zuhause**: Per Video, kein Anreise-Stress.
- **Schneller**: Erprobte Standard-Wege, weniger Wartezeit.

## Risiken und Grenzen

- **Nicht für komplexe Faelle**: Schwierige Sachverhalte (medizinische Gutachten, technische Details) lassen sich in der Eingabe-Maske nur eingeschraenkt darstellen.
- **Technik-Voraussetzungen**: Sie brauchen Computer, stabile Internet-Verbindung, Webcam, Mikrofon.
- **Identifikation**: Sie muessen sich elektronisch ausweisen (z.B. Mein Justizpostfach, eID Personalausweis).
- **Akten-Backup**: Sie sollten regelmaessig Kopien Ihrer Eingaben lokal speichern (z.B. als PDF herunterladen).
- **Nicht ueberall verfuegbar**: Nur an teilnehmenden Amtsgerichten.
- **Nicht für alle Streit-Typen**: Bestimmte Sachgebiete koennen ausgeschlossen sein.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Pruefen, ob Ihr Amtsgericht teilnimmt

Schauen Sie auf der Webseite der Justiz Ihres Bundeslandes oder direkt auf der Webseite des oertlich zuständigen Amtsgerichts nach. Beispiele:

- Justizportal Bund-Länder
- "Online-Verfahren" als Stichwort suchen.
- Bei der Geschaeftsstelle des Amtsgerichts nachfragen.

### Schritt 2 — Pruefen, ob Ihr Streit-Typ zugelassen ist

Das Online-Verfahren ist nicht für alle Streit-Typen offen. Typisch zugelassen sind z.B. Zahlungsklagen unter einem bestimmten Streitwert. Lesen Sie die Bedingungen der Plattform.

### Schritt 3 — Auf der Plattform registrieren

Identifikation typisch ueber:
- **Mein Justizpostfach (MJP)** — siehe `einreichung-mein-justizpostfach-mjp-2024`.
- **eID** mit dem Personalausweis und einem Lesegeraet/Smartphone-NFC.
- Login-Daten ueber Bund-ID-Verfahren.

### Schritt 4 — Klage in der Eingabe-Maske erfassen

Die Plattform fuehrt Sie durch:
- Antrag (was wollen Sie?)
- Beklagter (Name, Adresse)
- Sachverhalt (was ist passiert?)
- Beweise (welche Beweise haben Sie?)
- Anlagen (PDF hochladen)

Speichern Sie regelmaessig (die Plattform speichert meistens automatisch).

### Schritt 5 — Einreichen und Vorschuss zahlen

- Eingabe-Maske absenden.
- Plattform berechnet die Gerichtskosten.
- Zahlung per SEPA-Lastschrift, Ueberweisung oder Karte.
- Sobald gezahlt: Klage wird zugestellt.

### Schritt 6 — Reaktion der Gegenseite abwarten

Sie sehen im Plattform-Postfach, wenn die Gegenseite antwortet. Sie reagieren wieder ueber die Maske.

### Schritt 7 — Video-Termin

Wenn ein Termin stattfindet, bekommen Sie einen Link. Loggen Sie sich rechtzeitig ein (z.B. 15 Min. vorher). Achten Sie auf:
- Ruhiger Raum, kein Hintergrund-Laerm.
- Webcam auf Augenhoehe.
- Stabile Internet-Verbindung.
- Personalausweis griffbereit für Identitaets-Pruefung.

### Schritt 8 — Urteil im Plattform-Postfach

Das Urteil erscheint im Plattform-Postfach. Laden Sie es als PDF herunter und speichern Sie es lokal.

## Worauf Sie besonders achten muessen

- **Speichern Sie alles lokal als PDF.** Wenn die Plattform mal nicht laeuft, sind Sie nicht hilflos.
- **Pruefen Sie die Fristen.** Auch im Online-Verfahren gelten die normalen Fristen der ZPO.
- **Lassen Sie sich nicht von der Eingabe-Maske eingeengen**: Wenn Ihr Sachverhalt komplexer ist, fuegen Sie ein ergaenzendes PDF als Anlage hinzu.
- **Bei Zweifel: klassisches Verfahren waehlen.** Das Online-Verfahren ist freiwillig.

## Typische Fehler

- **Fehler:** Plattform für hochkomplexe Faelle nutzen — Eingabe-Maske ist zu eng. → **So vermeiden:** Bei komplexen Faellen klassisches Verfahren waehlen.
- **Fehler:** Plattform-Postfach nicht regelmaessig pruefen — Fristen verpasst. → **So vermeiden:** Mehrmals pro Woche einloggen oder Benachrichtigungs-E-Mail aktivieren.
- **Fehler:** Lokale Sicherungs-Kopien vergessen. → **So vermeiden:** Nach jeder Eingabe als PDF herunterladen.
- **Fehler:** Bei Video-Termin technische Probleme — kein Backup-Geraet. → **So vermeiden:** Vor dem Termin Funktion testen, Smartphone als Backup griffbereit.

## Querverweise

- `einreichung-mein-justizpostfach-mjp-2024` — MJP als Identifikations-Variante
- `video-verhandlung-128a-zpo` — Video-Verhandlung allgemein
- `klageschrift-pflichtbestandteile-253-zpo` — Inhalte der Klageschrift (auch in der Eingabe-Maske noetig)
- `wann-doch-anwalt-grenzfaelle` — Bei komplexen Faellen Anwalt erwaegen

## Quellen und Aktualitaet

Stand: 05/2026. Das Online-Verfahren wurde 2025 als Experimentier-Verfahren eingefuehrt; die genaue Norm-Verortung im 11. Buch ZPO und der Anwendungsbereich werden im laufenden Erprobungs-Zeitraum praezisiert. **Verifizieren Sie die aktuelle Rechtslage in amtliche/freie Quellen oder lizenzierte Datenbanken und auf der Webseite Ihres oertlich zuständigen Amtsgerichts vor Klageeinreichung.**

## 3. `rechtsmittelfrist-517-zpo`

**Fokus:** Rechtsmittelfrist 1 Monat nach § 517 ZPO. Beginn mit Zustellung des vollständigen Urteils Notfrist keine Verlaengerung. Berechnung mit § 187 188 BGB Praeklusion bei Versaeumnis Wiedereinsetzung in Ausnahmefaellen.

# Berufungsfrist: 1 Monat — keine Verlaengerung

## Worum geht es?

Die Berufungsfrist betraegt 1 Monat ab Zustellung des vollstaendigen schriftlichen Urteils. Sie ist eine **Notfrist** — keine Verlaengerung moeglich. Wenn Sie die Frist versaeumen, ist das Urteil rechtskraeftig und kann nicht mehr angegriffen werden. Diese Skill warnt vor der Frist und zeigt Berechnung.

## Wann brauchen Sie diese Skill?

- Sie haben ein Urteil bekommen.
- Sie ueberlegen Berufung.
- Sie sind unsicher, wann die Frist endet.

## Fachbegriffe (kurz erklaert)

- **Rechtsmittelfrist**: Frist für Einlegung eines Rechtsmittels.
- **Notfrist**: Nicht verlaengerbar.
- **Rechtskraft**: Endgueltige Verbindlichkeit des Urteils.

## Rechtsgrundlagen

- **§ 517 ZPO** — Berufungsfrist 1 Monat.
- **§ 520 II ZPO** — Berufungsbegruendungs-Frist 2 Monate (mit Verlaengerungsmoeglichkeit).
- **§ 224 I ZPO** — Notfrist nicht verlaengerbar.
- **§ 187, 188 BGB** — Fristberechnung.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Zustellung des Urteils

Frist beginnt mit Zustellung des **vollstaendigen schriftlichen Urteils** — nicht mit Verkuendung oder Empfang einer ersten Information.

Notieren Sie:

- Tag der Zustellung.
- Posteingangs-Stempel.
- Gelber Umschlag aufbewahren.

### Schritt 2 — Fristberechnung

§ 187 II BGB i. V. m. § 188 II BGB:

- Frist beginnt am Tag nach Zustellung.
- 1 Monat = gleicher Tag im Folgemonat.

Beispiel: Zustellung 15.5.2026 → Frist beginnt 16.5.2026 → Frist endet 15.6.2026.

Beispiel: Zustellung 31.5.2026 → Folgemonat hat keinen 31. → Frist endet 30.6.2026.

### Schritt 3 — Wochenende und Feiertag

§ 193 BGB: Wenn Frist-Ende auf Wochenende/Feiertag faellt, verschiebt sich auf naechsten Werktag.

Beispiel: Frist endet 15.6.2026 (Montag) → ok.
Frist endet 14.6.2026 (Sonntag) → Verschiebung auf 15.6.2026 (Montag).

### Schritt 4 — Vorfrist setzen

In Ihrem Fristen-Buch (Skill `fristen-buch-fuehren-laien`):

- Vorfrist: 1 Woche vor Frist-Ende.
- Zweite Vorfrist: 3 Tage vor.
- Erinnerung am letzten Tag.

### Schritt 5 — Berufung rechtzeitig einlegen

Innerhalb der Frist schriftlich (oder elektronisch ueber MJP) an das **Landgericht** (nicht ans AG).

Skill `berufung-amtsgericht-511-zpo`.

Bei Eile: Selbst-Einreichung der Berufungsschrift (§ 78 III ZPO erlaubt es). Begruendung dann mit Anwalt.

### Schritt 6 — Begruendungs-Frist 2 Monate

§ 520 II ZPO: **2 Monate** ab Zustellung des Urteils.

Wichtig: Begruendungs-Frist laeuft ab **Zustellung**, **nicht** ab Einlegung der Berufung. Wenn Sie also 4 Wochen mit Berufung warten, haben Sie nur 4 Wochen für Begruendung.

Verlaengerung der Begruendungs-Frist moeglich nach § 520 II 3 ZPO (auf Antrag, durch Vorsitzenden).

### Schritt 7 — Bei Versaeumnis

Wenn Berufungsfrist versaeumt:

- Urteil wird rechtskraeftig.
- Wiedereinsetzung nur bei "ohne Verschulden" (§ 233 ZPO).
- Schwer zu bekommen.

### Schritt 8 — Wenn unsicher

Bei Unsicherheit lieber **eher** Berufung einlegen als zu spaet. Sie koennen die Berufung spaeter zuruecknehmen, wenn Sie sich anders entscheiden.

Bei Selbst-Einlegung muessen Sie aber bedenken: ohne Anwalt für Begruendung droht trotzdem Verwerfung.

### Schritt 9 — PKH parallel

Wenn Sie sich Berufung nicht leisten koennen:

- PKH-Antrag innerhalb der Berufungsfrist stellen.
- PKH-Antrag hemmt die Frist (BGH).

Skill `prozesskostenhilfe-pkh-114-zpo`.

## Worauf Sie besonders achten muessen

- **Notfrist 1 Monat** — keine Verlaengerung.
- **Beginn mit Zustellung**, nicht Verkuendung.
- **Begruendungs-Frist 2 Monate**, ab Zustellung (nicht Einlegung).
- **PKH-Antrag** kann Frist hemmen.

## Typische Fehler

- "Frist beginnt mit Verkuendung." → Falsch — mit Zustellung.
- "Verlaengerung der Berufungsfrist." → Nicht moeglich.
- "Ich begruende, wenn ich Zeit habe." → Begruendungs-Frist 2 Monate parallel.

## Querverweise

- `berufung-amtsgericht-511-zpo` — Berufung einlegen.
- `berufungs-zulassung-niedrig-streitwert` — Zulassung.
- `fristen-berechnen-187-188-bgb` — Berechnung.
- `wiedereinsetzung-frist-233-zpo` — Wiedereinsetzung.

## Quellen und Aktualitaet

Stand: 05/2026. § 517 ZPO unveraendert.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
