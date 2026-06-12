# Megaprompt: verlagsrecht-buchpreisbindung

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 51 Skills des Plugins `verlagsrecht-buchpreisbindung`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt …
2. **abmahnung-buchpreisbindung** — Buchpreisbindungsgesetz: Abmahnung wegen Preisbindungsverstoßes — BuchPrG §§ 9–11, Abmahnung verfassen und beantworten, …
3. **e-uebersetzungsrechte** — Verlagsrecht: Nutzungsrechte für E-Book, Print, Hörbuch und Audio im Verlagsvertrag — Abgrenzung der Nutzungsarten, Buch…
4. **honorar-vorschuss-absatzhonorar-und-abrechnung** — Verlagsrecht: Autorenhonorar, Vorschuss, Absatzhonorar, Nachvergütung und Abrechnungspflicht nach VerlG §§ 22–28, UrhG §…
5. **preisbindungsstreit-verlegerrecht** — Buchpreisbindungsgesetz: Preisbindungsstreit vor Gericht — Unterlassungsklage, Auskunfts- und Schadensersatzansprüche (B…
6. **redaktionsvertrag-freelancer-und-arbeitnehmer** — Verlagsrecht: Redaktionsverträge mit Freelancern und Arbeitnehmern — Abgrenzung Werkvertrag, Dienstvertrag, Arbeitsverhä…
7. **subskriptionspreis-e** — Buchpreisbindungsgesetz: Subskriptionspreise, Einführungspreise und Aktionspreise — BuchPrG § 7 Preisänderung, Fristenre…
8. **auslandsrechte-rezensionsexemplar** — Verlagsrecht: Auslandsrechte, Sanktionsregimes und Exportkontrolle — EU-Sanktionen, US-OFAC, verbotene Lizenznehmer, Due…
9. **e-book-preisbindung-und-plattformrabatte** — Buchpreisbindungsgesetz: E-Book-Preisbindung, Plattformgebühren, Rabatte durch Amazon, Apple und andere Anbieter — BuchP…
10. **presserecht-gegendarstellung-und-unterlassung** — Verlagsrecht: Presserecht, Gegendarstellung und Unterlassungsansprüche — Landespressegesetze, Meinungsfreiheit, Schmähkr…
11. **verlagsinsolvenz-rechte-rueckfall-und-lagerbestand** — Verlagsrecht: Verlagsinsolvenz — Rückfall von Nutzungsrechten an Autoren, Lagerbestandsverwertung, InsO §§ 103–119, UrhG…
12. **fachzeitschrift-peer-review-und-haftung** — Verlagsrecht: Fachzeitschriften, Peer-Review-Verfahren, Haftung für fehlerhafte Fachinformation und Autorenrechte — UrhG…
13. **autor-herausgeber-mitwirkende-rechtekette** — Verlagsrecht: Rechtekette bei Sammelwerken — Autor, Herausgeber, Mitwirkende, Übersetzer und Verlag; Klärung von Urheber…
14. **buchhandelsvertrag-konditionen-und-remission** — Verlagsrecht: Buchhandelsvertrag zwischen Verlag und Buchhandel — Konditionenabkommen, Remissionsrecht, Retourenquoten, …
15. **verlagsvertrag-redaktionsvertrag** — Verlagsrecht: Hauptpflichten aus dem Verlagsvertrag, Rechteübertragung nach UrhG §§ 31 ff. und VerlG sowie Rückrufrechte…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext ordnet der Ski..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Verlagsrecht Buchpreisbindung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verlagsrecht und Buchpreisbindung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen. Tragende Normen (VerlG, BuchPrG, UrhG §§ 32, 32a, 40) werden nicht aus Modellwissen finalisiert, sondern über die zugelassenen Live-Quellen geprüft.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Sofortrisiken zuerst markieren** — Fristen, Zustellung, Form, Zuständigkeit, Beweis-, Kosten- und Haftungsrisiken benennen.
2. **Aktenlandkarte bauen** — Welche Dateien sind Original, welche nur Behauptung; was fehlt für einen verwertbaren nächsten Schritt?
3. **Rolle klären** — Mandant, Gegner, Behörde, Gericht, betroffene Stelle; mit welchem Ziel und welcher Reichweite?
4. **Ziel bestimmen** — Prüfung, Entwurf, Antrag, Anmeldung, Schriftsatz, Verteidigung, Dashboard, Memo, Red-Team?
5. **Rechtsquellen trennen** — Normtext, Behördenpraxis, Rechtsprechung, Vertrag, technischer Standard und Praxisroutine getrennt halten.
6. **Fachmodule auswählen** — Drei bis sieben passende Skills aus diesem Plugin nennen mit Begründung, warum sie jetzt nützlich sind.
7. **Erste verwertbare Ausgabe liefern** — Kurze Lagekarte mit nächstem Schritt oder erstem Entwurf, statt einer langen abstrakten Abhandlung.

## Fachlicher Anker — Verlagsrecht und Buchpreisbindung

Tragende Anker: VerlG, BuchPrG, UrhG §§ 32, 32a, 40. Tatsächliche Fundstellen werden über dejure.org, openJur, gesetze-im-internet.de, BGH-/BVerfG-/EuGH-/EuG-Datenbank live geprüft und nicht aus Modellwissen finalisiert.

---

## Skill: `abmahnung-buchpreisbindung`

_Buchpreisbindungsgesetz: Abmahnung wegen Preisbindungsverstoßes — BuchPrG §§ 9–11, Abmahnung verfassen und beantworten, Unterlassungserklärung, Schadensersatz und Prozessstrategie im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec..._

# Verl-041 · Abmahnung Buchpreisbindung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Abmahnungen wegen Buchpreisbindungsverstößen sind das häufigste Durchsetzungsinstrument im deutschen Buchhandel. Kläre, wie eine wirksame Abmahnung aussieht, wie Empfänger reagieren sollten und welche Kosten und Risiken auf beiden Seiten entstehen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG § 9 Abs. 1 | Unterlassungsanspruch gegen Preisbindungsverstoß | https://www.gesetze-im-internet.de/buchprg/__9.html |
| BuchPrG § 9 Abs. 2 | Schadensersatzanspruch | https://www.gesetze-im-internet.de/buchprg/__9.html |
| BuchPrG § 10 | Klageberechtigung des Börsenvereins | https://www.gesetze-im-internet.de/buchprg/__10.html |
| BuchPrG § 11 | Einstweiliger Rechtsschutz | https://www.gesetze-im-internet.de/buchprg/__11.html |
| BuchPrG § 13 | Bußgeld: bis 5.000 € | https://www.gesetze-im-internet.de/buchprg/__13.html |
| UWG § 13 | Abmahnkosten: Erstattungspflicht | https://dejure.org/gesetze/UWG/13.html |
| ZPO § 935 | Einstweilige Verfügung | https://dejure.org/gesetze/ZPO/935.html |

## Wer kann abmahnen?

### Aktivlegitimation (§ 9 BuchPrG)
- **Verleger**: Direkter Anspruch gegen jeden Händler, der Bücher unter dem festgesetzten Preis verkauft.
- **Importeur**: Bei Importen.
- **Buchhandel**: Mitbewerber, der durch den Verstoß benachteiligt wird.
- **Börsenverein des Deutschen Buchhandels e.V.** (§ 10 BuchPrG): Besonderes Klagerecht; kann unabhängig von eigenem Schaden vorgehen.

### Abgemahnt werden kann
- Buchhandlungen, Online-Händler, Amazon-Marketplace-Händler.
- Verlage (wenn sie selbst Preisbindung nicht korrekt festsetzen).
- Importeure ohne eigene Preisfestsetzung.

## Aufbau einer wirksamen Abmahnung

### Mindestinhalte
1. **Absender**: Vollständiger Name, Adresse, Vertreter (ggf. Rechtsanwalt).
2. **Adressat**: Vollständige Firmierung des Verletzers.
3. **Verstoßbeschreibung**: Konkreter Titel (ISBN), festgesetzter Ladenpreis, angebotener Preis, Datum und URL des Angebots.
4. **Verstoßgrundlage**: BuchPrG §§ 3, 5; Verletzungstatbestand klar benennen.
5. **Unterlassungsaufforderung**: Aufforderung, den Verstoß sofort zu beenden und künftig zu unterlassen.
6. **Vertragsstrafe**: Unterlassungserklärung mit Vertragsstrafe für Wiederholung; Höhe nennen (empfohlen: 5.000–10.000 € pro Verstoß).
7. **Kostenforderung**: Anwaltskosten; Streitwert für Kostenberechnung.
8. **Frist**: Kurze Frist für Reaktion (24–72 Stunden bei dringendem Online-Verstoß; 5–7 Werktage sonst).

### Dokumentation des Verstoßes
- Screenshot des Angebots mit URL, Datum, Uhrzeit.
- VLB-Ausdruck: Nachweis des festgesetzten Ladenpreises.
- Testbestellung: Quittung über tatsächlichen Kaufpreis (wenn physischer Kauf).

## Reaktion auf eine empfangene Abmahnung

### Optionen
1. **Unterlassungserklärung unterzeichnen**: Verstoß eingestehen; Vertragsstrafe bei Wiederholung akzeptieren; Kosten zahlen.
 - Vorteil: Schnelle Erledigung; Schutz vor teurerer einstweiliger Verfügung.
 - Risiko: Vertragsstrafe bei späterem Verstoß; Eingeständnis für Schadensersatzklage.

2. **Modifizierte Unterlassungserklärung**: Unterlassung erklären, aber Vertragsstrafe-Höhe oder Formulierung modifizieren.
 - Abmahner muss neue Formulierung akzeptieren oder Verfügung beantragen.

3. **Ablehnen**: Abmahner trägt dann Risiko und muss einstweilige Verfügung beantragen.
 - Nur sinnvoll, wenn Abmahnung offensichtlich unbegründet oder Verstoß nicht vorlag.

4. **Schutzschrift**: Beim zuständigen Gericht einreichen, um Gegendarstellung bei Verfügungsantrag zu sichern.

### Frist und Dringlichkeit
- Abmahnungen mit kurzen Fristen (24–48 h): Anwalt sofort einschalten.
- Nach Verfügungserlass: Widerspruch innerhalb von 2 Wochen (§ 924 ZPO).

## Kosten der Abmahnung

### Anwaltskosten (nach RVG)
- Streitwert typisch 15.000–30.000 € für Buchpreisbindungsabmahnung.
- Anwaltsgebühren (1,3-fache Geschäftsgebühr): Bei Streitwert 30.000 € ca. 1.000–1.500 € netto.
- Der Abgemahnte muss die Kosten des Abmahnenden erstatten, wenn die Abmahnung berechtigt ist.

### Vertragsstrafe bei Wiederholung
- Einmal unterschriebene Unterlassungserklärung; jeder weitere Verstoß: Vertragsstrafe.
- Vertragsstrafe muss bezahlt werden, auch ohne Klage; bei Nicht-Zahlung: Klage auf Vertragsstrafe.

## Börsenverein: Massenabmahnungen

- Börsenverein mahnt jährlich Dutzende von Händlern ab.
- Kontakt für Verstoß-Meldungen: preisbindung@boersenverein.de
- Verlag kann Verstoß melden; Börsenverein mahnt im eigenen Namen ab → Kosten trägt Börsenvereins-Fonds.

## Typische Fallen

- **Abmahnung ohne Quellennachweis**: Abmahnung ohne Screenshot und VLB-Ausdruck → angreifbar; Abgemahnter kann Vollständigkeit bestreiten.
- **Falsche Fristlänge**: Abgemahnte hat 24 Stunden Frist erhalten; Anwalt ist im Urlaub; Einstweilige Verfügung wird beantragt → keine Fristverlängerung ohne Zustimmung.
- **Modifizierte Unterlassungserklärung abgelehnt**: Abmahner besteht auf Original-Formulierung; Verfahren eskaliert → Kosten steigen.
- **Wiederholungsverstoß**: Händler hat Unterlassungserklärung unterschrieben; Amazon-Algorithmus senkt Preis erneut → Vertragsstrafe fällig; Händler muss Amazon sofort anschreiben.

## Checkliste Abmahnung

### Abmahnender
- [ ] Verstoß-Screenshot mit URL, Datum, Preis dokumentiert
- [ ] VLB-Ausdruck: Festgesetzter Ladenpreis belegt
- [ ] Adressat korrekt identifiziert (Handelsregistereintrag prüfen)
- [ ] Abmahnung vollständig (alle Pflichtangaben)
- [ ] Frist angemessen gesetzt
- [ ] Kosten berechnet und genannt

### Abgemahnter
- [ ] Anwalt sofort einschalten (auch bei kurzer Frist)
- [ ] Verstoß-Sachverhalt intern klären
- [ ] Optionen abgewogen (unterzeichnen / ablehnen / modifizieren)
- [ ] Schutzschrift vorbereiten (falls Ablehnung)
- [ ] Amazon / Plattform sofort instruieren, Preis zu korrigieren

## Quellenreferenzen

- BuchPrG §§ 9–11: https://www.gesetze-im-internet.de/buchprg/
- UWG § 13 (Abmahnkosten): https://dejure.org/gesetze/UWG/13.html
- BGH „Buchpreisbindung Abmahnung" I ZR 173/09: https://www.bgh.de
- Börsenverein, Preisbindungsdurchsetzung: https://www.boersenverein.de
- ZPO §§ 935 ff.: https://dejure.org/gesetze/ZPO/935.html

## Output-Formate

- **Abmahnungs-Entwurf**: Vollständige, juristische korrekte Abmahnung
- **Dokumentations-Paket**: Screenshot, VLB-Ausdruck, Zeitstempel
- **Unterlassungserklärung**: Standardformulierung mit Vertragsstrafe
- **Ablehnungs-Schreiben**: Wenn Abmahnung unbegründet
- **Schutzschriften-Entwurf**: Für zuständiges Gericht

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 41 UrhG
- § 32d UrhG
- § 32a UrhG
- § 6 BuchPrG
- § 32 UrhG
- § 7 BuchPrG
- § 38 UrhG
- § 3 BuchPrG
- § 31 UrhG
- § 4 UrhG
- § 14 UrhG
- § 51 UrhG

### Leitentscheidungen

- EuGH C-174/15
- BGH I ZR 198/13
- BGH I ZR 136/20
- EuGH C-299/23
- EuGH C-202/12

---

## Skill: `e-uebersetzungsrechte`

_Verlagsrecht: Nutzungsrechte für E-Book, Print, Hörbuch und Audio im Verlagsvertrag — Abgrenzung der Nutzungsarten, Buchpreisbindung je Ausgabe, Plattformverträge und Lizenzketten im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec..._

# Verl-006 · E-Book, Print, Hörbuch und Audio: Nutzungsrechte und Preisbindung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Verlage müssen für jede **Ausgabeform** (Print, E-Book, Hörbuch, Audiostream, PDF-Datenbank) sowohl die **Nutzungsrechte** sauber eingeräumt haben als auch die **Preisbindungsregeln** korrekt anwenden. Dieser Skill systematisiert diese Ausgabenspezifik und klärt Plattformverträge, Lizenzketten und Vergütungsfragen für multimediale Verlagswerke.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 15 | Verwertungsrechte: Vervielfältigung, Verbreitung, öffentliche Zugänglichmachung | https://dejure.org/gesetze/UrhG/15.html |
| UrhG § 16 | Vervielfältigungsrecht | https://dejure.org/gesetze/UrhG/16.html |
| UrhG § 17 | Verbreitungsrecht (Erschöpfung!) | https://dejure.org/gesetze/UrhG/17.html |
| UrhG § 19a | Recht der öffentlichen Zugänglichmachung (Online) | https://dejure.org/gesetze/UrhG/19a.html |
| UrhG § 31 Abs. 1 | Nutzungsartenspezifität | https://dejure.org/gesetze/UrhG/31.html |
| BuchPrG § 2 | Geltungsbereich: Bücher, Noten, kartografische Erzeugnisse | https://www.gesetze-im-internet.de/buchprg/__2.html |
| BuchPrG § 2 Abs. 1 Nr. 3 | E-Books als preisgebundene Produkte | https://www.gesetze-im-internet.de/buchprg/__2.html |
| EU-VO 2017/1128 | Portabilität digitaler Inhalte im Binnenmarkt | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1128 |

## Nutzungsarten im Verlagsvertrag: Abgrenzung

### Print-Rechte
- **Vervielfältigung und Verbreitung** von gedruckten Exemplaren (§§ 16, 17 UrhG).
- Erschöpfung des Verbreitungsrechts nach § 17 Abs. 2 UrhG bei Erstverkauf; Bibliotheksausleihe, Antiquariatshandel zulässig.
- Einschließt: Hardcover, Paperback, Taschenbuch, Sonderausgabe, Großdruck, Lizenzausgabe (Buchgemeinschaft).

### E-Book-Rechte
- **Vervielfältigung + öffentliche Zugänglichmachung** (§ 19a UrhG); kein Erschöpfungsgrundsatz.
- Formate: EPUB, EPUB3, PDF, MOBI, AZW (Kindle); jedes Format ist eine eigenständige Verwertungshandlung.
- DRM-Nutzung (Digital Rights Management): Verlag darf technische Schutzmaßnahmen einsetzen (§ 95a UrhG).
- **Preisbindung**: BuchPrG § 2 Abs. 1 Nr. 3 — E-Books unterliegen der Buchpreisbindung, wenn deutschsprachig und für den deutschen Markt bestimmt.

### Hörbuch-Rechte
- **Lesevortrag** (§ 17 UrhG Verbreitung, wenn CD) oder **öffentliche Zugänglichmachung** (§ 19a UrhG, wenn Download/Stream).
- Leistungsschutzrecht des Sprechers (§§ 73 ff. UrhG): Sprecherlizenz erforderlich.
- GEMA-Pflicht bei Musikunterlegung.
- Preisbindung: Hörbuche auf physischem Datenträger → BuchPrG; Download/Stream → streitig, aber i.d.R. nicht preisgebunden.

### Audiostream / Podcast-Derivate
- Rein audiovisuelle Nutzungen außerhalb des körperlichen Datenträgers unterliegen grundsätzlich nicht der Buchpreisbindung.
- Zusätzliche Nutzungsrechte nötig: Synchronisation (§ 24 UrhG a.F.), Bearbeitung (§ 23 UrhG n.F.).

### Kombinationsprodukte / Bundle
- E-Book + Print-Bundle: Ist der Gesamtpreis ein preisgebundener Preis?
- BGH: Bundle kann separate Preisbindungspflicht je Komponente auslösen; keine Umgehung durch Bündelung.

## Plattformverträge und Lizenzketten

### Amazon KDP / Apple Books
- Plattformvertrag überträgt kein Urheberrecht; Verlag bleibt Rechteinhaber.
- Plattformgebühren: Amazon 30 % (KU: Seitenhonorar), Apple 30 %.
- **Preisbindungs-Compliance**: Verlag muss den gebundenen Preis auch auf Plattformen durchsetzen (BuchPrG § 5); Plattform ist Letztabnehmer.

### Spotify / Audible / Storytel (Audiostreaming)
- Kein Anwendungsbereich des BuchPrG (kein körperliches Buch, kein E-Book im engeren Sinne).
- Lizenzverhandlung: Verlag schließt Plattformvertrag; Autor erhält Anteil aus Sublizenzerlösen.
- Auskunftsanspruch des Autors nach § 32d UrhG gilt auch für Streamingerlöse.

### Portabilität (EU-VO 2017/1128)
- Abonnenten digitaler Inhalte dürfen E-Books und Hörbücher bei Reisen innerhalb der EU nutzen.
- Konsequenz: Territorial beschränkte Lizenzen können EU-rechtlich unterlaufen werden.
- Verlagsverträge mit territorial beschränkten Nutzungsrechten: Prüfen, ob EU-Portabilitätsrecht Auswirkung hat.

## Vergütung je Ausgabe

| Ausgabe | Typischer Honorarsatz | Berechnungsbasis |
|---------|----------------------|-----------------|
| Hardcover | 10–15 % NLP | Nettoladenpreis |
| Taschenbuch | 6–10 % NLP | Nettoladenpreis |
| E-Book | 20–25 % Verlagseinnahmen | Plattformerlös nach Abzug Gebühr |
| Hörbuch Download | 20–25 % Verlagseinnahmen | Nach Plattformgebühren |
| Streaming | nach Einheit oder Prozentsatz | Plattformabrechnung |
| Sublizenz | 50–75 % der Lizenzeinnahmen | Lizenzgebühr |

## Typische Fallen

- **E-Book-Recht nicht separat vereinbart**: Frühere Verträge (vor 2000) enthalten keine E-Book-Klausel; § 31a UrhG-Widerrufsrecht des Autors kann greifen.
- **Hörbuch-Sprecherlizenz vergessen**: Verlag schließt Vertrag mit Produktionsfirma, nicht aber mit Sprecher; Leistungsschutzrecht verletzt.
- **Erschöpfung bei E-Books falsch angenommen**: Käufer eines E-Books darf es nicht weiterverkaufen; kein Erschöpfungsgrundsatz (EuGH, C-128/11 — UsedSoft; für E-Books anders als für Software).
- **Bundle-Preisbindung unterlaufen**: Verlag senkt E-Book-Preis durch Bundle-Konstruktion unter den gebundenen Preis; BuchPrG § 5 verletzt.
- **DRM und Barrierefreiheit**: EU-Barrierefreiheitsrichtlinie (EAA) verpflichtet ab 2025 zu zugänglichen E-Books; DRM darf Barrierefreiheits-Nutzung nicht blockieren.

## Checkliste Mehrfachausgaben-Verlagsvertrag

- [ ] Jede Nutzungsart einzeln aufgeführt (UrhG § 31 Abs. 1)
- [ ] E-Book-Rechte und Formate benannt
- [ ] Hörbuch-Rechte mit Sprecherentgelt-Passus
- [ ] Streaming-/Plattformvergütung und Abrechnungsmodalität
- [ ] Sublizenz-Beteiligungsquoten für jede Ausgabe
- [ ] Preisbindungspflicht für E-Book-Plattformen vertraglich verankert
- [ ] EU-Portabilitätsverordnung berücksichtigt (territorial beschränkte Klauseln prüfen)

## Quellenreferenzen

- BuchPrG § 2: https://www.gesetze-im-internet.de/buchprg/__2.html
- UrhG §§ 15–19a: https://dejure.org/gesetze/UrhG/19a.html
- EU-VO 2017/1128 (Portabilität): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1128
- EuGH, C-128/11, UsedSoft: https://eur-lex.europa.eu
- BGH „E-Book-Preisbindung", KZR 25/14: https://www.bgh.de

## Output-Formate

- **Nutzungsrechte-Matrix**: Alle Ausgaben × Nutzungsarten × Rechtsstatus
- **Preisbindungs-Ampel je Ausgabe**: Print / E-Book / Hörbuch / Stream
- **Plattformvertrags-Check**: KDP, Apple, Audible, Spotify — Compliance
- **Honorarübersicht**: Tantiemensätze je Ausgabe
- **Checkliste unbekannte Nutzungsarten** für Altverträge (§ 31a UrhG)

---

## Skill: `honorar-vorschuss-absatzhonorar-und-abrechnung`

_Verlagsrecht: Autorenhonorar, Vorschuss, Absatzhonorar, Nachvergütung und Abrechnungspflicht nach VerlG §§ 22–28, UrhG §§ 32 und 32a, 32d — Berechnung, Angemessenheit und Auskunft im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec..._

# Verl-005 · Honorar, Vorschuss, Absatzhonorar und Abrechnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Klärt alle vergütungsrechtlichen Fragen im Verlagsvertrag: Wie wird das Honorar berechnet? Was gilt als angemessene Vergütung? Wann ist ein Vorschuss fällig? Wie funktioniert die Absatzhonorar-Abrechnung? Wann entsteht ein Nachvergütungsanspruch (Bestseller-Paragraf)? Grundlage sind VerlG §§ 22–28 und UrhG §§ 32, 32a, 32d.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| VerlG § 22 | Honoraranspruch des Autors; Entstehung | https://www.gesetze-im-internet.de/verlg/__22.html |
| VerlG § 23 | Berechnung des Honorars nach Auflage | https://www.gesetze-im-internet.de/verlg/__23.html |
| VerlG § 24 | Abrechnung: Fristen und Form | https://www.gesetze-im-internet.de/verlg/__24.html |
| VerlG § 28 | Neue Auflagen: neuer Honoraranspruch | https://www.gesetze-im-internet.de/verlg/__28.html |
| UrhG § 32 | Angemessene Vergütung; Anpassungsanspruch | https://dejure.org/gesetze/UrhG/32.html |
| UrhG § 32a | Nachvergütung bei besonderem Erfolg | https://dejure.org/gesetze/UrhG/32a.html |
| UrhG § 32d | Auskunftsanspruch des Urhebers | https://dejure.org/gesetze/UrhG/32d.html |
| UrhG § 36 | Gemeinsame Vergütungsregeln | https://dejure.org/gesetze/UrhG/36.html |
| DSM-RL Art. 18 | Angemessenheitsprinzip für Urheber | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |
| DSM-RL Art. 20 | Vertragsanpassungsmechanismus | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Honorartypen im Überblick

### 1. Pauschalhonorar
- Einmalige Zahlung für alle Nutzungen oder eine bestimmte Auflage.
- Vorteil für Verlag: Planungssicherheit.
- Risiko für Autor: Kein Nachvergütungsanspruch, es sei denn, § 32a UrhG greift.

### 2. Absatzhonorar (Tantieme)
- Prozentualer Anteil am **Nettoladenpreis** (NLP) jedes verkauften Exemplars.
- Übliche Sätze nach gemeinsamen Vergütungsregeln (VS/Verleger):
 - Hardcover: 10–15 % NLP
 - Taschenbuch: 6–10 % NLP
 - E-Book: 20–25 % NLP (abhängig von Plattformgebühren)
- Berechnung: Menge × NLP × Prozentsatz = Honorar je Abrechnung.

### 3. Auflagenhonorar
- Pauschalzahlung pro Auflage oder pro 1.000 Exemplare (VerlG § 23).
- Neue Auflage → neuer Honoraranspruch (VerlG § 28).

### 4. Vorschuss (Advance)
- Zahlung bei Vertragsabschluss oder Manuskriptablieferung gegen zukünftige Honorare.
- Wird gegen zukünftige Tantiemen verrechnet (earn-out); nicht zurückzahlbar, sofern der Verlag das Werk erscheinen lässt (übliche Vertragsklausel).
- Rückzahlungspflicht: Nur bei Rücktritt wegen Autoren-Verschuldens; streitig bei Nichterscheinen des Verlags.

## Angemessene Vergütung (§ 32 UrhG)

### Prüfungsmaßstab
1. **Gemeinsame Vergütungsregeln** (§ 36 UrhG): Zwischen Berufsverbänden (VS — Verband der Schriftsteller, Verleger-Verbände) ausgehandelte Tarife gelten als Richtsatz.
2. **Branchenübliche Vergütung**: Wenn keine gemeinsamen Vergütungsregeln, dann Vergleich mit branchenüblicher Praxis.
3. **Anpassungsanspruch**: Ist vereinbarte Vergütung unangemessen niedrig → Autor kann Anpassung auf angemessene Vergütung verlangen (kein Rücktritt nötig).

### Berechnung der Unangemessenheit
- Verhältnis: vereinbarte Vergütung zu erzieltem Erlös des Verlags aus Werknutzung.
- BGH-Rechtsprechung: „Auffälliges Missverhältnis" bei Abweichung > 100 % gegenüber angemessenem Wert (BGH „Bestseller", I ZR 174/18).

## Nachvergütung (§ 32a UrhG — Bestseller-Paragraf)

### Voraussetzungen
- Vereinbarte Vergütung steht in **auffälligem Missverhältnis** zu tatsächlichen Erträgen.
- „Auffällig" = erhebliche Überschreitung der Erwartungen beim Vertragsabschluss.
- Erträge des Verlags aus Werknutzung (Tantiemen aus Lizenzen, Verlagserlös etc.) müssen bekannt oder ermittelbar sein.

### Geltendmachung
- Schriftliche Geltendmachung gegenüber Verlag.
- Ggf. vorherige Auskunft nach § 32d UrhG.
- Klage auf Abänderung des Vertrags auf angemessene Beteiligung.

## Auskunftsanspruch (§ 32d UrhG)

- Autor kann **jährlich** Auskunft verlangen: Art und Umfang der Nutzung, Erlöse, weitere Sublizenzen.
- Gilt auch für Urheber, die Rechte an Verleger weiterübertragen haben (Kette).
- **DSM-RL Art. 19**: Stärkung des Transparenzanspruchs auf EU-Ebene; Mitgliedstaaten müssen angemessene Auskunftsmechanismen bereitstellen.
- Klagerecht: Bei Verweigerung der Auskunft → Auskunftsklage; ggf. Stufenklage (Auskunft + Zahlung).

## Abrechnungspflicht (VerlG § 24)

- Verlag muss **mindestens einmal jährlich** abrechnen (VerlG § 24), bei Absatzhonorar detailliert nach Ausgaben, Mengen, Preisen.
- Abrechnung muss enthalen: Auflage, verkaufte Exemplare, Remittenden, Belegexemplare, Freiexemplare, Nettoladenpreis, Honorarsatz.
- **Einsichtsrecht**: Autor kann Belegeinsicht in Verlagsbücher verlangen (§ 24 VerlG analog § 810 BGB).
- Frist für Einwände: Üblich 3–6 Monate nach Zugang der Abrechnung; Einwände schriftlich.

## Typische Fallen

- **Pauschalhonorare unterschätzen den Werterfolg**: Autor erhält einmalig Pauschale; bei Bestseller-Erfolg greift § 32a UrhG.
- **Verjährung der Auskunftsansprüche**: §§ 195, 199 BGB; regelmäßige Verjährungsfrist 3 Jahre ab Jahresende; monatliche Abrechnung schafft keine rückwirkenden Ansprüche.
- **NLP vs. Bruttoladenpreis**: MwSt. ist kein Teil des NLP; viele Verträge rechnen unklar; Klarheit verlangen.
- **Remittenden abgezogen**: Verlag darf nur tatsächlich remittierte Exemplare abziehen; fiktive Remittenden-Rückstellungen sind unzulässig.
- **Sublizenzerlöse vergessen**: Übersetzungslizenzen, Film-Optionen, E-Book-Plattform-Tantiemen — alle müssen in § 32d-Auskunft erscheinen.

## Checkliste Honorarprüfung

- [ ] Honorartyp (Pauschale, Absatz, Auflage) klar vereinbart
- [ ] Berechnungsbasis (NLP, gebundener Ladenpreis) definiert
- [ ] Abrechnungsrhythmus (mindestens jährlich) vereinbart
- [ ] Vorschuss: earn-out-Mechanismus und Rückzahlungsklausel geprüft
- [ ] § 32a UrhG Nachvergütungsklausel oder Ausschlussklausel geprüft
- [ ] § 32d Auskunftsrecht explizit geregelt
- [ ] Sublizenz-Beteiligungsquote vereinbart

## Quellenreferenzen

- VerlG §§ 22–28: https://www.gesetze-im-internet.de/verlg/
- UrhG § 32: https://dejure.org/gesetze/UrhG/32.html
- UrhG § 32a: https://dejure.org/gesetze/UrhG/32a.html
- UrhG § 32d: https://dejure.org/gesetze/UrhG/32d.html
- BGH „Klauseltausch" I ZR 174/18: https://www.bgh.de
- DSM-RL Art. 18–20: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- Börsenverein Honorartarife: https://www.boersenverein.de

## Output-Formate

- **Honorarberechnungssheet**: Absatzhonorar nach Auflagen und Ausgaben
- **Angemessenheitsprüfung**: Vergleich mit gemeinsamen Vergütungsregeln
- **Auskunftsschreiben** nach § 32d UrhG
- **Nachvergütungsklage-Vorprüfung**: Missverhältnis-Berechnung
- **Abrechnungsrüge**: Formelles Einwandsschreiben gegen Verlagsabrechnung

---

## Skill: `preisbindungsstreit-verlegerrecht`

_Buchpreisbindungsgesetz: Preisbindungsstreit vor Gericht — Unterlassungsklage, Auskunfts- und Schadensersatzansprüche (BuchPrG §§ 9–11), Gerichtszuständigkeit und Prozessstrategie im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec..._

# Verl-042 · Preisbindungsstreit: Unterlassung und Auskunft

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Führt durch das **gerichtliche Verfahren** bei Preisbindungsstreitigkeiten: Unterlassungsklage, einstweilige Verfügung, Auskunftsanspruch und Schadensersatz. Er klärt Zuständigkeiten, Fristen, Beweisanforderungen und strategische Optionen für Verlage und Buchhandel.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG § 9 | Unterlassungs- und Schadensersatzansprüche | https://www.gesetze-im-internet.de/buchprg/__9.html |
| BuchPrG § 10 | Klageberechtigung Börsenverein | https://www.gesetze-im-internet.de/buchprg/__10.html |
| BuchPrG § 11 | Einstweiliger Rechtsschutz | https://www.gesetze-im-internet.de/buchprg/__11.html |
| ZPO §§ 935–945 | Einstweilige Verfügung | https://dejure.org/gesetze/ZPO/935.html |
| ZPO § 890 | Vollstreckung: Ordnungsgeld, Ordnungshaft | https://dejure.org/gesetze/ZPO/890.html |
| GKG | Gerichtskostengesetz: Streitwert und Gerichtskosten | https://www.gesetze-im-internet.de/gkg/ |

## Gerichtszuständigkeit

### Sachliche Zuständigkeit
- Preisbindungssachen: Landgericht (LG) als erstinstanzliches Gericht (§ 13 GVG i.V.m. BuchPrG).
- Keine Amtsgerichts-Zuständigkeit.

### Örtliche Zuständigkeit
- **Allgemeiner Gerichtsstand**: Am Sitz des Beklagten (§ 17 ZPO).
- **Besonderer Gerichtsstand für unerlaubte Handlungen** (§ 32 ZPO): Auch am Ort des Verstoßes (Lieferort, Serverstandort bei Online-Verstoß).
- Vorzugsgerichte für Buchpreisbindung: LG Frankfurt am Main, LG Hamburg, LG München I — erfahrene Kammern für Preisbindungssachen.

## Einstweilige Verfügung (§ 11 BuchPrG i.V.m. ZPO §§ 935 ff.)

### Voraussetzungen
- **Verfügungsanspruch**: Glaubhaftmachung des Preisbindungsverstoßes.
- **Verfügungsgrund (Dringlichkeit)**: Online-Verstoß löst i.d.R. Dringlichkeit aus; 1-Monat-Frist ab Kenntnis (Dringlichkeitsvermutung erschüttert bei längerem Zuwarten).

### Verfahren
1. Antrag beim LG; kein zwingender Anwaltszwang, aber praktisch notwendig.
2. Antragsteller legt eidesstattliche Versicherung bei (statt Zeugenbeweis).
3. Gericht entscheidet ohne mündliche Verhandlung (ex parte) oder mit kurzer Verhandlung.
4. Beschluss ergeht innerhalb von Tagen; Zustellung an Beklagten durch Gerichtsvollzieher.

### Vollstreckung (§ 890 ZPO)
- Zuwiderhandlung gegen Verfügung: Ordnungsgeld bis 250.000 €; Ordnungshaft bis 6 Monate.
- Antrag auf Ordnungsmittel beim LG nach festgestelltem Verstoß.

### Widerspruch (§ 924 ZPO)
- Beklagter kann Widerspruch einlegen; dann mündliche Verhandlung.
- Widerspruchsfrist: 2 Wochen.

## Hauptsacheverfahren

### Unterlassungsklage
- Klage auf dauerhafte Unterlassung des Preisbindungsverstoßes.
- Streitwert: Typisch 15.000–30.000 € für Buchpreisbindungssachen.
- Beweislast: Kläger muss Verstoß beweisen; Beklagter muss Rechtmäßigkeit (z.B. Ausnahme § 6 BuchPrG) beweisen.

### Schadensersatz (§ 9 Abs. 2 BuchPrG)
- Voraussetzung: Verschulden des Verletzers.
- Berechnung:
 - Entgangener Gewinn des Klägers (schwer zu beziffern).
 - Lizenzanalogie: Welche Lizenz hätte Verletzer zahlen müssen?
 - Verletzergewinn: Wie viel hat Verletzer durch den Verstoß verdient?
- Auskunftsanspruch: Kläger kann Auskunft über Umfang des Verstoßes verlangen (Stufenklage).

## Auskunftsanspruch

### Anspruchsgrundlage
- § 9 BuchPrG i.V.m. allgemeinem Auskunftsanspruch.
- Auskunft über: Anzahl verkaufter Exemplare unter dem gebundenen Preis; erzielte Preise; Herkunft der Exemplare.

### Stufenklage (ZPO § 254)
1. Stufe 1: Auskunft über Umfang des Verstoßes.
2. Stufe 2: Eidesstattliche Versicherung der Richtigkeit der Auskunft.
3. Stufe 3: Zahlung des sich aus der Auskunft ergebenden Schadensersatzbetrags.

## Prozessstrategie

### Für Kläger (Verlag / Buchhandel)
- Erst einstweilige Verfügung für sofortigen Stopp; dann Hauptsache für Schadensersatz.
- Testbestellung für Beweiszwecke.
- VLB-Ausdruck als Urkundenbeweis für Ladenpreis.
- Börsenverein einbeziehen (§ 10 BuchPrG): Entlastet Kläger.

### Für Beklagten (Händler / Verlag)
- Vorwurf-Sachverhalt intern aufklären: War Preis korrekt? Systemfehler?
- Wenn Verstoß lag: Schnell korrigieren; Unterlassungserklärung unterzeichnen → Kosten minimieren.
- Wenn kein Verstoß: Klage mit Ausnahme § 6 BuchPrG begründen; Beweislast liegt beim Kläger.

## Verjährung

- UWG § 11-ähnlich: Verjährungsfrist 6 Monate ab Kenntnis von Verstoß und Verletzer.
- Ohne Kenntnis: 3 Jahre (§§ 195, 199 BGB).
- **Wichtig**: Dringlichkeit für einstweilige Verfügung erlischt nach ca. 4–6 Wochen ohne Handeln.

## Typische Fallen

- **Dringlichkeit verpasst**: Verlag wartet 6 Wochen mit dem Antrag → Gericht verneint Dringlichkeit → kein einstweiliger Rechtsschutz möglich.
- **Falsche Zuständigkeit**: Antrag beim Amtsgericht statt Landgericht → unzuständig; Kosten; Zeitverlust.
- **Schadensnachweis fehlt**: Schadensersatzklage ohne Auskunftsanspruch → Schaden nicht bezifferbar.
- **Vollstreckungsfehler**: Verfügung zugestellt, aber Vollstreckung nicht beantragt → Zuwiderhandlung bleibt sanktionslos.

## Checkliste Preisbindungsstreit

### Vorbereitung
- [ ] Verstoß dokumentiert (Screenshot, VLB, Testbestellung)
- [ ] Anwalt eingeschaltet
- [ ] LG-Zuständigkeit bestimmt
- [ ] Dringlichkeitsfrist prüfen: Wann erstmals Kenntnis?

### Antrag
- [ ] Verfügungsantrag mit eidesstattlicher Versicherung eingereicht
- [ ] Zustellung vollzogen

### Nach Verfügungserlass
- [ ] Verstoß-Monitoring aktiv (hat Antragsgegner aufgehört?)
- [ ] Ordnungsmittelantrag bei Zuwiderhandlung

## Quellenreferenzen

- BuchPrG §§ 9–11: https://www.gesetze-im-internet.de/buchprg/
- ZPO §§ 935–945: https://dejure.org/gesetze/ZPO/935.html
- BGH „Buchpreisbindung-Schadensersatz" I ZR 125/03: https://www.bgh.de
- OLG Frankfurt (Buchpreisbindung einstweilige Verfügung): https://openjur.de
- Börsenverein, Klageberechtigung § 10 BuchPrG: https://www.boersenverein.de

## Output-Formate

- **Verfügungsantrags-Entwurf**: Vollständig mit Glaubhaftmachung
- **Streitwert-Kalkulation**: Für Kostenschätzung
- **Auskunftsklage-Stufenplan**: Stufe 1–3 mit Antragsformulierungen
- **Widerspruchs-Schriftsatz** (für Beklagten)
- **Monitoring-Protokoll** nach Verfügungserlass

---

## Skill: `redaktionsvertrag-freelancer-und-arbeitnehmer`

_Verlagsrecht: Redaktionsverträge mit Freelancern und Arbeitnehmern — Abgrenzung Werkvertrag, Dienstvertrag, Arbeitsverhältnis; Scheinwerkvertrag, Urheberrecht und Sozialversicherung im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtspr..._

# Verl-023 · Redaktionsvertrag, Freelancer und Arbeitnehmer

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Verlage beschäftigen **Redakteure, Lektoren, Übersetzer, Fotografen und Grafiker** sowohl als Arbeitnehmer als auch als freie Mitarbeiter. Die Abgrenzung zwischen echten Freelancern und Scheinselbständigen ist rechtlich komplex und hat erhebliche Konsequenzen für Sozialversicherungspflicht, Urheberrecht und Haftung. Kläre alle relevanten Dimensionen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BGB § 631 | Werkvertrag: Erfolg geschuldet | https://dejure.org/gesetze/BGB/631.html |
| BGB § 611a | Arbeitnehmerstellung: persönliche Abhängigkeit | https://dejure.org/gesetze/BGB/611a.html |
| SGB IV § 7 | Beschäftigung: Sozialversicherungspflicht | https://www.gesetze-im-internet.de/sgb_4/__7.html |
| UrhG § 43 | Urheberrecht in Arbeitsverhältnissen | https://dejure.org/gesetze/UrhG/43.html |
| UrhG § 31 | Nutzungsrechtseinräumung durch Freiberufler | https://dejure.org/gesetze/UrhG/31.html |
| UrhG § 32 | Angemessene Vergütung für freie Mitarbeiter | https://dejure.org/gesetze/UrhG/32.html |
| KSA § 1 | Künstlersozialversicherung: Abgabepflicht des Verwerters | https://www.gesetze-im-internet.de/ksvg/ |

## Vertragstypen im Verlag

### 1. Werkvertrag (BGB § 631)
- Freelancer schuldet einen **bestimmten Erfolg**: z.B. fertiges Manuskript, fertige Übersetzung, fertiges Lektorat.
- Keine Weisungsgebundenheit bezüglich Weg und Zeitplanung.
- Vergütung nach Abnahme des Werks.
- Urheberrecht: Bleibt beim Urheber; Nutzungsrechte müssen ausdrücklich eingeräumt werden.

### 2. Dienstvertrag (BGB § 611)
- Dienstleister schuldet eine **Tätigkeit** (z.B. laufendes Lektorat, Redaktionsarbeit), keinen definierten Erfolg.
- Größere Weisungsgebundenheit als beim Werkvertrag.
- Bei starker Weisungsgebundenheit und Eingliederung → Gefahr der Arbeitnehmereigenschaft.

### 3. Arbeitsvertrag (BGB § 611a)
- Arbeitnehmer ist in die Betriebsorganisation eingegliedert und persönlich abhängig.
- Verlag bestimmt Ort, Zeit und Art der Arbeit.
- Urheberrecht (§ 43 UrhG): Bei Schöpfung in Erfüllung des Arbeitsverhältnisses → Verlag hat umfassendes Nutzungsrecht kraft Arbeitsvertrag und Verkehrsüblichkeit.

## Scheinselbständigkeit: Abgrenzungskriterien

| Merkmal | Freelancer (echt) | Scheinselbständig |
|---------|------------------|------------------|
| Eigene Betriebsstätte | Ja | Nein |
| Mehrere Auftraggeber | Ja (i.d.R.) | Nein (nur ein Auftraggeber) |
| Unternehmerisches Risiko | Ja | Nein |
| Weisungsgebundenheit | Gering | Hoch |
| Eingliederung in Betrieb | Nein | Ja |
| Eigene Arbeitszeit | Selbst bestimmt | Vorgegeben |

### Statusfeststellungsverfahren (DRV)
- Sozialversicherungsträger (Deutsche Rentenversicherung Bund) kann auf Antrag feststellen, ob eine Beschäftigung vorliegt.
- Verlag kann proaktiv Antrag stellen zur Rechtssicherheit.
- Im Nachhinein: Nachzahlung von Sozialversicherungsbeiträgen für 4 Jahre (vorsätzlich: 30 Jahre).

## Urheberrecht in Arbeitsverhältnissen (§ 43 UrhG)

- Urheber-Eigenschaft des Arbeitnehmers bleibt bestehen; Urheberrecht ist unveräußerlich.
- Nutzungsrechte: Verlag erhält kraft Arbeitsvertrag oder betrieblicher Übung alle für die übliche Verwertung nötigen ausschließlichen Nutzungsrechte.
- **Grenzen**: Nutzungen, die weit über den betrieblichen Zweck hinausgehen (z.B. Verkauf an Dritte), erfordern zusätzliche Vereinbarung mit dem Arbeitnehmer.
- Nachvergütung (§ 32a UrhG): Gilt auch für Arbeitnehmer-Urheber; bei besonderem Erfolg.

## Künstlersozialversicherung (KSA)

### Abgabepflicht des Verlags
- Verlage, die Werke von freien Künstlern und Publizisten verwerten, müssen **Künstlersozialabgabe** auf die Honorarsumme zahlen.
- Abgabesatz 2024: Ca. 5 % der Honorarsumme (variiert jährlich).
- Pflicht gilt für: Aufträge an freie Autoren, Fotografen, Illustratoren, Übersetzer, Grafiker.

### Was zählt zur Bemessungsgrundlage?
- Alle Honorarzahlungen an selbständige Künstler und Publizisten.
- Nicht enthalten: Auslagenersatz, Mehrwertsteuer, Reisekosten.

### Konsequenzen bei Nichtabführung
- Nachforderung durch Künstlersozialkasse (KSK) für bis zu 4 Jahre.
- Bußgeld; in Einzelfällen strafrechtliche Relevanz.

## Freelancer-Vertrag: Mindestinhalte

1. **Werkbeschreibung**: Genauer Gegenstand (z.B. „Lektorat des Manuskripts X von ca. 80.000 Zeichen").
2. **Abgabetermin** / Leistungszeitraum.
3. **Vergütung** und Zahlungsmodalität; Angemessenheitsprüfung (§ 32 UrhG).
4. **Nutzungsrechtseinräumung**: Alle benötigten Nutzungsarten ausdrücklich aufführen.
5. **Freistellungsklausel**: Freelancer stellt Verlag von Ansprüchen Dritter frei.
6. **Vertraulichkeit**: NDA für unveröffentlichte Manuskripte.
7. **KSA-Hinweis**: Honorar zzgl. KSA des Verlags.

## Typische Fallen

- **Scheinselbständigkeit unerkannt**: Verlag beschäftigt Freelancer seit Jahren exklusiv, täglich präsent; Sozialversicherungsprüfung → Nachzahlung 4 Jahre.
- **Keine Nutzungsrechtseinräumung**: Verlag zahlt Freelancer für Übersetzung; Vertrag schweigt über Rechte → Zweckübertragungsregel; Verlag hat nur Mindestrechte.
- **KSA nicht abgeführt**: Kleiner Verlag zahlt Honorare an freie Autoren ohne KSA-Abführung → Nachforderung durch KSK.
- **§ 32a UrhG bei Bestseller**: Freier Übersetzer fordert Nachvergütung für Bestseller-Übersetzung; Verlag hat keine Öffnungsklausel im Vertrag.

## Checkliste Redaktionsvertrag

- [ ] Vertragstyp korrekt gewählt (Werkvertrag, nicht verdeckter Arbeitsvertrag)
- [ ] Werkbeschreibung präzise
- [ ] Nutzungsrechtseinräumung vollständig
- [ ] Vergütung angemessen (§ 32 UrhG)
- [ ] KSA-Pflicht geprüft und abgeführt
- [ ] Vertraulichkeit (NDA) vereinbart
- [ ] Freistellungsklausel enthalten

## Quellenreferenzen

- BGB § 611a: https://dejure.org/gesetze/BGB/611a.html
- UrhG § 43: https://dejure.org/gesetze/UrhG/43.html
- SGB IV § 7: https://www.gesetze-im-internet.de/sgb_4/__7.html
- KSVG: https://www.gesetze-im-internet.de/ksvg/
- BSG, Urt. v. 14.03.2018 – B 12 R 3/17 R (Scheinselbständigkeit Journalist): https://www.bundessozialgericht.de

## Output-Formate

- **Statusprüfungs-Checkliste**: Freelancer oder Arbeitnehmer
- **Werkvertrag-Muster**: Für Lektoren, Übersetzer, Fotografen
- **KSA-Berechnungssheet**: Honorarsumme × Abgabesatz
- **Nutzungsrechts-Klausel**: Standardformulierung für Freelancer-Verträge
- **Statusfeststellungsantrag-Briefing** für DRV

---

## Skill: `subskriptionspreis-e`

_Buchpreisbindungsgesetz: Subskriptionspreise, Einführungspreise und Aktionspreise — BuchPrG § 7 Preisänderung, Fristenregelungen, Preisbindungs-Compliance bei temporären Preissenkungen im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht..._

# Verl-012 · Subskriptionspreis, Einführungspreis und Aktionspreis

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Verlage nutzen **Subskriptions-, Einführungs- und Aktionspreise**, um Nachfrage anzukurbeln. Alle diese Preismodelle sind unter dem BuchPrG zulässig — aber nur unter strikten Bedingungen: Der temporäre Preis muss selbst als gebundener Ladenpreis festgesetzt werden, und nach Ablauf muss der reguläre Preis wieder durchgesetzt werden. Kläre das gesamte Regelwerk.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG § 3 | Festsetzungspflicht: jeder Preis muss förmlich festgesetzt werden | https://www.gesetze-im-internet.de/buchprg/__3.html |
| BuchPrG § 7 | Preisänderung und Preisaufhebung durch Verleger | https://www.gesetze-im-internet.de/buchprg/__7.html |
| BuchPrG § 5 | Letztabnehmer-Bindung; auch temporäre Preise sind bindend | https://www.gesetze-im-internet.de/buchprg/__5.html |
| BuchPrG § 9 | Ansprüche bei Verstoß | https://www.gesetze-im-internet.de/buchprg/__9.html |
| UWG § 5 | Irreführende Werbung mit Preisangaben | https://dejure.org/gesetze/UWG/5.html |
| PAngV | Preisangabenverordnung — korrekte Auszeichnung | https://www.gesetze-im-internet.de/pangv/ |

## Subskriptionspreis

### Definition
- Ein **Subskriptionspreis** ist ein reduzierter Preis, der vor Erscheinen des Werks für Vorbestellungen angeboten wird.
- Klassisch bei teuren Fachwerken, Nachschlagewerken, Loseblatt-Sammlungen.

### Rechtliche Einordnung
- Der Subskriptionspreis ist ein selbständiger, befristeter gebundener Ladenpreis (§ 3 BuchPrG).
- Verlag setzt den Subskriptionspreis förmlich fest und teilt ihn dem Buchhandel mit.
- Nach Ablauf der Subskriptionsfrist (typisch: bei Erscheinen) gilt automatisch der höhere Normalpreis.
- **Kein automatisches Recht** des Buchhandels, Exemplare zum Subskriptionspreis zu verkaufen, wenn die Frist abgelaufen ist, auch wenn Kunde noch nicht abgeholt hat.

### Dokumentation
- Subskriptionsfrist muss klar definiert und kommuniziert sein.
- VLB-Meldung: Beide Preise (Subskription und Normal) mit Gültigkeitsdaten.
- Buchhandel muss über Fristende rechtzeitig informiert werden.

## Einführungspreis

### Definition
- Ein **Einführungspreis** ist ein reduzierter Ladenpreis für die ersten Wochen/Monate nach Erscheinen.
- Ziel: Aufmerksamkeit generieren, Erstplatzierung im Buchhandel fördern, Rezensionsexemplare stimulieren.

### Rechtliche Einordnung
- Einführungspreis = temporärer gebundener Ladenpreis (§ 7 BuchPrG).
- Nach Ablauf der Einführungsphase muss der höhere Preis als neuer Ladenpreis festgesetzt und kommuniziert werden.
- **Preiserhöhung nach Einführungsphase**: Für Exemplare, die der Buchhandel noch nicht verkauft hat, gilt der neue höhere Preis → Buchhandel kann auf Einführungspreis-Exemplaren sitzen bleiben, die er zu höherem Preis verkaufen muss.

### Praxis-Problem
- Buchhandel hält Einführungspreis-Exemplare zurück, um sie nach Preiserhöhung günstiger als die Neulieferung anzubieten → rechtlich unzulässig: auch für Altexemplare gilt der neue gebundene Preis.
- Ausnahme: § 6 BuchPrG-Ausnahme (Mängelexemplar, Remittend) einschlägig.

## Aktionspreise

### Definition
- Ein **Aktionspreis** ist ein zeitlich, räumlich oder anlassbezogen begrenzter reduzierter Preis.
- Beispiele: Buchmesse-Aktionspreis, Weihnachts-Aktionspreis, Geburtstagsaktion des Verlags.

### Rechtliche Einordnung
- Auch Aktionspreise sind gebundene Ladenpreise (§ 3 BuchPrG); nur wenn der Verleger sie als solche förmlich festsetzt, sind sie bindend.
- **Einheitlichkeit**: Ein Aktionspreis gilt für alle Händler gleich; der Verleger darf nicht einem Händler exklusiv einen günstigeren Aktionspreis gewähren → Wettbewerbsverzerrung und ggf. § 9 BuchPrG-Verstoß.
- Zeitliche Begrenzung im VLB dokumentieren.

## Kommunikation an den Buchhandel (§ 4 BuchPrG)

- Alle Preisänderungen müssen dem Buchhandel **rechtzeitig und eindeutig** mitgeteilt werden.
- Form: Schriftlich (E-Mail, EDI-Datenstrom über VLB, Verlagsrundschreiben).
- Inhalt: Neue Preise, gültig ab Datum, Ablauf (falls befristet).
- **Frühzeitigkeit**: Buchhandel benötigt Vorlauf für Umpreisungsaktionen im Laden.

## E-Book-Aktionspreise und Plattformen

- Amazon KDP, Apple Books erlauben temporäre Preisreduktionen.
- Verlag muss sicherstellen: reduzierter E-Book-Preis = neuer gebundener Ladenpreis für die Aktionsdauer.
- Nach Aktion: Preis automatisch zurückgesetzt → VLB-Meldung und Plattformseitige Einstellung müssen synchron sein.
- **„Countdown Deals"** (KDP): Sonderaktions-Mechanismus; Preisbindungs-Compliance bleibt Verlagspflicht.

## Irreführungsverbot (UWG § 5, PAngV)

- Einführungspreis darf nicht als dauerhafter Normalpreis deklariert werden.
- „Früher X €, jetzt Y €"-Werbung nur zulässig, wenn „früher"-Preis tatsächlich für angemessenen Zeitraum gegolten hat (PAngV § 11).
- Fingierte Ursprungspreise → UWG § 5 (irreführende Angaben).

## Typische Fallen

- **Einführungspreis ohne Enddatum**: Buchhandel verkauft unbegrenzt zu Einführungspreis; Verlag hat versäumt, Preiserhöhung zu kommunizieren → rechtlich schwierig durchsetzbar.
- **Aktionspreis nur für einen Händler**: Exklusiv-Aktion für einen Großhändler → diskriminiert andere Buchhandlungen; ggf. UWG-Verstoß.
- **Plattform-Sonderaktionen ohne Verlagsfreigabe**: Plattform senkt E-Book-Preis ohne Rückfrage → Verlag haftet für Preisbindungsverstoß.
- **Subskriptionspreis nach Erscheinen**: Buchhandel bietet Buch nach Erscheinen noch zum Subskriptionspreis an, weil er keine Preisänderungsmitteilung erhalten hat → Verantwortung beim Verlag für rechtzeitige Kommunikation.

## Checkliste Temporäre Preise

- [ ] Temporärer Preis förmlich als gebundener Ladenpreis festgesetzt (§ 3 BuchPrG)
- [ ] Gültigkeitsdaten in VLB eingetragen
- [ ] Buchhandel rechtzeitig über Preisänderung informiert (§ 4 BuchPrG)
- [ ] E-Book-Plattformen synchron mit VLB-Daten
- [ ] Nach Aktionsende: Regulären Preis wieder aktiv geschaltet und mitgeteilt
- [ ] Werbung: Ursprungspreis-Angaben konform mit PAngV

## Quellenreferenzen

- BuchPrG §§ 3, 7: https://www.gesetze-im-internet.de/buchprg/
- PAngV: https://www.gesetze-im-internet.de/pangv/
- UWG § 5: https://dejure.org/gesetze/UWG/5.html
- OLG Hamburg, Urt. v. 07.02.2019 (E-Book-Aktionspreis): https://openjur.de
- Börsenverein, FAQ Buchpreisbindung: https://www.boersenverein.de

## Output-Formate

- **Preiskalender**: Alle aktiven und geplanten Preisfenster mit Gültigkeitsdaten
- **Kommunikationsprotokoll**: Wann wurde welcher Preis an Buchhandel gemeldet
- **Compliance-Checkliste Plattformen**: E-Book-Aktionen auf Richtigkeit geprüft
- **UWG-Werbungscheck**: Preisangaben in Werbematerialien
- **Aktionspreis-Briefing** für Buchhandel

---

## Skill: `auslandsrechte-rezensionsexemplar`

_Verlagsrecht: Auslandsrechte, Sanktionsregimes und Exportkontrolle — EU-Sanktionen, US-OFAC, verbotene Lizenznehmer, Due Diligence und Compliance-Anforderungen für internationale Lizenzverträge im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege..._

# Verl-038 · Auslandsrechte, Sanktionen und Exportkontrolle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Verlage, die Lizenzen an ausländische Verlage vergeben, müssen **Sanktionsrecht** und Exportkontrolle beachten. Lizenzen an Verlage in sanktionierten Ländern (z.B. Russland, Iran, Nordkorea) können gegen EU-Sanktionsverordnungen oder US-OFAC-Regelungen verstoßen. Kläre die Compliance-Anforderungen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| EU-Sanktionsverordnungen | z.B. VO (EU) Nr. 833/2014 (Russland), Nr. 267/2012 (Iran) | https://eur-lex.europa.eu |
| AWG § 4 | Außenwirtschaftsgesetz: Verbotene Geschäfte | https://www.gesetze-im-internet.de/awg/__4.html |
| AWV | Außenwirtschaftsverordnung: Genehmigungspflichten | https://www.gesetze-im-internet.de/awv/ |
| US OFAC Regulations | US-Sanktionslisten (SDN List) | https://ofac.treasury.gov |
| GWG §§ 10 ff. | Geldwäschegesetz: Sorgfaltspflichten | https://www.gesetze-im-internet.de/gwg_2017/ |
| StGB §§ 34, 18 | Außenwirtschaftsstrafrecht | https://dejure.org/gesetze/AWG/18.html |

## Sanktionsrecht und Buchrechte: Grundlagen

### Was sind Sanktionen?
- Sanktionen sind staatliche oder internationale Maßnahmen, die wirtschaftliche Transaktionen mit bestimmten Ländern, Unternehmen oder Personen verbieten.
- **EU-Sanktionen**: Verordnungen des Rates der EU; unmittelbar anwendbar in allen Mitgliedstaaten.
- **US-OFAC**: Office of Foreign Assets Control; US-Sanktionen haben extraterritoriale Wirkung (betreffen auch deutsche Verlage bei US-Dollar-Zahlungen oder US-Verträgen).

### Sind Buchlizenzen Sanktionsgegenstand?
- Grundsatz: Kulturelle Güter (Bücher, Lizenzen) sind häufig **ausgenommen** von Sanktionen.
- Ausnahmen:
 - Technologietransfer (Dual-Use-Güter: Bücher mit militärischen oder nuklearen Inhalten).
 - Lizenzen an sanktionierte Personen (SDN-Liste, EU-Sanktionsliste).
 - Zahlungen in sanktionierten Währungen oder über sanktionierten Finanzinstitute.

## EU-Sanktionen: Russland (Beispiel VO 833/2014)

### Verbotene Transaktionen
- Zahlungen an von der EU gelistete russische Personen und Organisationen.
- Technologietransfer (technische Spezifikationsbücher, Dual-Use-Materialien).

### Buchlizenzen in der Praxis
- Kulturelle Ausnahmen: Bücher als solche sind i.d.R. nicht verbotene Güter.
- **Zahlungsweg**: Auch wenn Buch erlaubt, kann Zahlungstransfer über russische Banken blockiert sein.
- **Listung des Lizenznehmers**: Wenn russischer Verlag auf SDN- oder EU-Sanktionsliste → Vertrag verboten.

### Sorgfaltspflichten (GWG § 10)
- Verlag muss Geschäftspartner auf Sanktionslisten prüfen (Know-Your-Customer, KYC).
- Screening-Tools: EU-Sanktionsliste (EUR-Lex), US-SDN-Liste (OFAC), nationale Sanktionslisten.
- Dokumentation: KYC-Prüfung dokumentieren; Ergebnis aufbewahren.

## US-OFAC: Extraterritoriale Wirkung

- Deutschen Verlage, die USD-Zahlungen empfangen oder US-Korrespondenzbanken nutzen, können US-Sanktionen unterfallen.
- **OFAC-SDN-Liste**: Specially Designated Nationals — jede Transaktion mit gelisteten Personen ist für US-Personen und oft auch Nicht-US-Personen verboten.
- Deutsche Verlage: Direkte Anwendbarkeit zweifelhaft; aber USD-Clearing durch US-Banken kann OFAC-Compliance erfordern.
- **Secondary Sanctions**: US kann Sanktionen gegen Nicht-US-Unternehmen verhängen, die mit sanktionierten Ländern Geschäfte machen.

## Due-Diligence-Checkliste für Auslandslizenzen

### Schritt 1: Ländercheck
- Ist das Zielland von EU- oder US-Sanktionen betroffen?
- Ist das Zielland auf FATF-Grauer oder -Schwarzer Liste (Geldwäscherisiko)?

### Schritt 2: Lizenznehmers-Screening
- Lizenznehmers-Name und Eigentümerstruktur prüfen.
- Screening gegen EU-Sanktionsliste, US-SDN-Liste, Interpol-Liste.
- PEP-Screening (Politically Exposed Persons).

### Schritt 3: Vertragsdokumentation
- Zahlungswährung und Zahlungsweg: EUR über SEPA sicher; USD über US-Korrespondenzbank prüfen.
- Vertragsklausel: „Lizenzgeber und Lizenznehmer bestätigen, keiner Sanktionsliste zu unterfallen. Bei Aufnahme auf Sanktionsliste: sofortige Vertragsauflösung."
- Sanktionsklausel: Vertrag erlischt automatisch bei Listung einer Partei.

### Schritt 4: Monitoring
- Laufende Überwachung: Sind Vertragsparteien nach Vertragsschluss gelistet worden?
- Jährliches Re-Screening.

## Dual-Use-Bücher

- Dual-Use: Waren, Software, Technologien, die zivil und militärisch genutzt werden können.
- Einschlägig für Verlage: Technische Handbücher, Chemie, Biotechnologie, Kryptographie-Bücher.
- EU-Dual-Use-VO (VO (EU) 2021/821): Ausführgenehmigungspflicht für gelistete Güter.
- Bücher als solche: Nur in Extremfällen Dual-Use; aber Know-how-Transfer kann relevant sein.

## Typische Fallen

- **Sanktions-Listing nach Vertragsschluss**: Russischer Verlag wird kurz nach LOI auf Sanktionsliste gesetzt → bestehender Vertrag muss beendet werden; aufgelaufene Advance-Zahlungen blockiert.
- **USD-Zahlungsweg und US-Banken**: Verlag akzeptiert USD-Advance; Zahlung über US-Korrespondenzbank → OFAC-Compliance-Problem.
- **KYC-Dokumentation fehlt**: Behördenprüfung zeigt, dass Verlag keine Sanktionsscreening-Dokumentation geführt hat → GWG-Bußgeld.
- **Dual-Use-Buch nicht erkannt**: Technisches Handbuch mit Anwendungen für Waffensysteme → Exportgenehmigung erforderlich.

## Checkliste Auslandslizenzen Sanktions-Compliance

- [ ] Zielland auf Sanktionsliste geprüft (EU, US-OFAC)
- [ ] Lizenznehmers-Screening: EU-Sanktionsliste, SDN-Liste, PEP
- [ ] Zahlungswährung und -weg geprüft (kein USD über US-Banken bei sanktioniertem Land)
- [ ] Sanktionsklausel im Lizenzvertrag
- [ ] KYC-Dokumentation aufbewahrt
- [ ] Dual-Use-Relevanz des Werkes geprüft
- [ ] Jahres-Re-Screening geplant

## Quellenreferenzen

- EU-Sanktionsliste: https://eur-lex.europa.eu/content/sanctions/sanctions.html
- US-OFAC SDN-Liste: https://ofac.treasury.gov/sanctions-list-search
- AWG: https://www.gesetze-im-internet.de/awg/
- EU Dual-Use-VO 2021/821: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821
- GWG: https://www.gesetze-im-internet.de/gwg_2017/

## Output-Formate

- **Sanktions-Screening-Protokoll**: Ergebnis je Vertragspartner dokumentiert
- **Sanktionsklausel-Muster** für Lizenzverträge
- **Länder-Risikomatrix**: Sanktions- und Exportkontrollrisiko je Zielmarkt
- **KYC-Dokumentationsvorlage**
- **Dual-Use-Prüfprotokoll** für technische Werke

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 41 UrhG
- § 32d UrhG
- § 32a UrhG
- § 6 BuchPrG
- § 32 UrhG
- § 7 BuchPrG
- § 38 UrhG
- § 3 BuchPrG
- § 31 UrhG
- § 4 UrhG
- § 14 UrhG
- § 51 UrhG

### Leitentscheidungen

- EuGH C-174/15
- BGH I ZR 198/13
- BGH I ZR 136/20
- EuGH C-299/23
- EuGH C-202/12

---

## Skill: `e-book-preisbindung-und-plattformrabatte`

_Buchpreisbindungsgesetz: E-Book-Preisbindung, Plattformgebühren, Rabatte durch Amazon, Apple und andere Anbieter — BuchPrG § 2 Abs. 1 Nr. 3, Durchsetzung und Vertragsgestaltung im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-013 · E-Book-Preisbindung und Plattformrabatte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Die E-Book-Preisbindung ist ein Spezialbereich mit erheblichem Konfliktpotenzial zwischen Verlagsrecht und Plattformverträgen. Kläre, welche E-Books preisgebunden sind, wie Plattformgebühren und Rabatte behandelt werden, welche Vertragsklauseln mit Amazon, Apple und anderen notwendig sind und wie Verstöße durchgesetzt werden.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG § 2 Abs. 1 Nr. 3 | E-Books als preisgebundene Produkte | https://www.gesetze-im-internet.de/buchprg/__2.html |
| BuchPrG § 3 | Preisfestsetzung durch Verleger / Importeur | https://www.gesetze-im-internet.de/buchprg/__3.html |
| BuchPrG § 5 | Letztabnehmer-Bindung | https://www.gesetze-im-internet.de/buchprg/__5.html |
| BuchPrG § 9 | Ansprüche bei Verstoß | https://www.gesetze-im-internet.de/buchprg/__9.html |
| EU-VO 2017/1128 | Portabilität digitaler Inhalte | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1128 |
| UrhG § 19a | Recht der öffentlichen Zugänglichmachung (Online-Vertrieb) | https://dejure.org/gesetze/UrhG/19a.html |

## E-Books im Geltungsbereich des BuchPrG

### Seit 2016: Gesetzliche Preisbindung
- BuchPrG § 2 Abs. 1 Nr. 3 (Fassung seit 01.01.2016): E-Books sind ausdrücklich preisgebunden.
- Voraussetzungen:
 1. E-Book ist ein „Buch" im Sinne des BuchPrG (Sprachwerk als elektronische Ausgabe)
 2. Erscheinen in Deutschland oder Import für deutschen Markt
 3. Nicht ausgenommen nach § 6 BuchPrG

### Geltungsbereich: Was ist ein E-Book?
- EPUB, PDF, MOBI (Kindle), AZW: Alle Formate, die den Buchinhalt digital als Sprachwerk übermitteln.
- Nicht erfasst: Apps mit Buchinhalt (wenn App-Funktion im Vordergrund), reine Audios, interaktive Lernspiele.
- Grenzfall: Enhanced E-Books (mit Videos, interaktiven Elementen): Einzelfallbewertung nötig.

## Plattformgebühren und der gebundene Preis

### Grundprinzip
- Der Verlag setzt den **Endkundenpreis** (gebundener Ladenpreis) fest.
- Plattformgebühren (Amazon 30 %, Apple Books 30 %, etc.) werden vom Verlag getragen, nicht vom Endkunden.
- Endkunde zahlt genau den gebundenen Preis; Plattform erhält ihren Anteil davon.

### Amazon KDP — Preisgestaltung
- KDP-Direktvertrieb: Autor/Verlag setzt Preis in KDP-Dashboard; Amazon verkauft zum festgesetzten Preis.
- KDP-Select: Enthält Kindle Unlimited (Streaming); Vergütung nach gelesenen Seiten, kein fester Ladenpreis für KU-Nutzung → KU unterliegt nicht der Buchpreisbindung (kein Kauf).
- **Amazon Price Match**: Amazon kann E-Book-Preis senken, wenn dasselbe Buch anderswo günstiger angeboten wird → Verstoß gegen Preisbindung durch den billigeren Anbieter; Amazon „spiegelt" den Verstoß.

### Apple Books
- Verleger setzt Preis im App Store Connect; Apple behält 30 %.
- Apple-Werbemaßnahmen (z.B. „Deal of the Day"): Nur zulässig, wenn Verlag temporären Aktionspreis festsetzt (§ 7 BuchPrG).

### Tolino / Thalia
- Deutsches Konsortium; engere Verlagsabsprachen; Preisbindungs-Compliance üblicherweise vertraglich verankert.

### Google Play Books
- Verlag setzt Preis; Google behält Plattformgebühr; Endkundenpreis muss gebunden sein.

## Vertragsgestaltung mit Plattformen

### Mindestklauseln im Plattformvertrag
1. Endkundenpreis = vom Verlag festgesetzter gebundener Ladenpreis
2. Plattform darf keine Preissenkungen ohne Verlagsfreigabe vornehmen
3. Aktionspreise nur nach Freigabe und förmlicher Preisfestsetzung durch Verlag
4. Pflicht zur sofortigen Rücknahme von Preissenkungen bei Verlags-Aufforderung
5. Reporting-Pflicht: Monatliche Absatzberichte mit Preisen und Aktionszeiträumen

### Price-Parity-Klauseln (kritisch!)
- Manche Plattformverträge enthalten Most-Favored-Nation (MFN) / Price-Parity-Klauseln: „Verlag muss denselben Preis auf unserer Plattform haben wie anderswo."
- EU-Kartellrecht: Price-Parity-Klauseln durch Amazon wurden von Kartellbehörden (Bundeskartellamt, EU-Kommission) beanstandet.
- **Vorsicht**: Price-Parity führt dazu, dass Verlag E-Book-Preis nicht auf anderen Plattformen günstiger setzen darf → kann Innovationsbarriere sein.

## Durchsetzung der E-Book-Preisbindung

### § 9 BuchPrG — Ansprüche
- Anspruchsberechtigte: Andere Verleger, Importeure, der Buchhandel, der Börsenverein.
- Ansprüche: Unterlassung (§ 9 Abs. 1 BuchPrG), Schadensersatz, Auskunft.
- Prozessual: Einstweilige Verfügung möglich bei offensichtlichem Preisbindungsverstoß.

### Börsenverein als Klageberechtigter (§ 10 BuchPrG)
- Börsenverein des Deutschen Buchhandels e.V. ist klagebefugt.
- Klagt regelmäßig gegen Online-Händler, die E-Books unter gebundenem Preis anbieten.

### Monitoring
- Verlage sollten automatisierte Preis-Monitoring-Tools einsetzen (z.B. Bookwire, EPUB-Crawler).
- Bei erkanntem Verstoß: Abmahnung an Händler/Plattform, ggf. Kündigung des Plattformvertrags.

## Typische Fallen

- **KDP-Preisanpassung automatisch**: Amazon senkt E-Book-Preis automatisch wegen Price-Match → Verlag hat Preisbindungsverstoß nicht begangen, aber muss Amazon auffordern, den gebundenen Preis wiederherzustellen.
- **Keine förmliche Preisfestsetzung für E-Book**: Verlag veröffentlicht E-Book über KDP ohne eigenständige Preisfestsetzung nach § 3 BuchPrG → formaler Mangel; kann durch nachträgliche Meldung geheilt werden.
- **Bundle mit App**: E-Book-Inhalt in App-Bundle unter dem Ladenpreis → je nach Produktgestaltung Preisbindungsverstoß.
- **Aktionspreise nicht dokumentiert**: Plattform führt Aktion durch; Verlag kann nicht nachweisen, dass temporäre Preissenkung förmlich festgesetzt war → Verstoß-Risiko.

## Checkliste E-Book-Preisbindung

- [ ] E-Book als preisgebundenes Produkt klassifiziert
- [ ] Ladenpreis für jedes Format separat festgesetzt und in VLB gemeldet
- [ ] Plattformverträge auf Preisbindungs-Klauseln geprüft
- [ ] Monitoring-System für Plattformpreise eingerichtet
- [ ] Aktionspreise förmlich festgesetzt und mit Ablaufdatum gemeldet
- [ ] Amazon Price-Match-Risiko bekannt und Verfahren definiert

## Quellenreferenzen

- BuchPrG § 2: https://www.gesetze-im-internet.de/buchprg/__2.html
- Bundeskartellamt, Amazon E-Book-Verfahren (2012/2017): https://www.bundeskartellamt.de
- BGH „E-Book" KZR 25/14 (Preisbindung E-Books): https://www.bgh.de
- EU-VO 2017/1128: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32017R1128
- Börsenverein, E-Book-Preisbindung: https://www.boersenverein.de

## Output-Formate

- **Plattform-Compliance-Tabelle**: Alle E-Book-Plattformen × Preis × Status
- **Vertragscheck Plattformvertrag**: Preisbindungsklauseln vorhanden / fehlend / mangelhaft
- **Monitoring-Bericht**: Preisabweichungen der letzten 30 Tage
- **Abmahnungsentwurf** bei Preisbindungsverstoß durch Plattform
- **MFN-Klausel-Risikoanalyse**

---

## Skill: `presserecht-gegendarstellung-und-unterlassung`

_Verlagsrecht: Presserecht, Gegendarstellung und Unterlassungsansprüche — Landespressegesetze, Meinungsfreiheit, Schmähkritik, Unterlassung und Schadensersatz bei Pressedelikten im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-031 · Presserecht, Gegendarstellung und Unterlassung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Verlage und Zeitschriften operieren im Spannungsfeld zwischen **Pressefreiheit** (GG Art. 5) und dem Schutz von Persönlichkeitsrechten, Unternehmensreputation und Datenschutz. Kläre die presserechtlichen Grundlagen, das Gegendarstellungsrecht, Unterlassungsansprüche und die Haftung für Presseberichte.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| GG Art. 5 Abs. 1 | Presse-, Meinungs- und Rundfunkfreiheit | https://www.gesetze-im-internet.de/gg/art_5.html |
| GG Art. 1 Abs. 1 i.V.m. Art. 2 Abs. 1 | Allgemeines Persönlichkeitsrecht | https://www.gesetze-im-internet.de/gg/art_1.html |
| LPG (Landespressegesetze) | Länderspezifische Presseregelungen; Gegendarstellungsrecht | (länderspezifisch; z.B. § 11 LPG Bayern) |
| BGB § 823 | Haftung für Pressedelikte | https://dejure.org/gesetze/BGB/823.html |
| BGB § 824 | Kreditgefährdung durch unwahre Tatsachen | https://dejure.org/gesetze/BGB/824.html |
| StGB §§ 186, 187 | Üble Nachrede, Verleumdung | https://dejure.org/gesetze/StGB/186.html |
| UrhG § 50 | Berichterstattung über aktuelle Ereignisse | https://dejure.org/gesetze/UrhG/50.html |

## Pressefreiheit und ihre Grenzen

### Geschützte Betätigungen
- Berichterstattung über Personen des öffentlichen Lebens.
- Recherche, Beschaffung von Informationen.
- Meinungsäußerungen, Kommentare, Kritik.
- Satire (mit gewissen Einschränkungen).

### Grenzen der Pressefreiheit
- Unwahre Tatsachenbehauptungen: Nicht von Pressefreiheit gedeckt.
- Schmähkritik: Angriff ohne Sachbezug, der allein auf Verunglimpfung zielt → kein Schutz durch Meinungsfreiheit.
- Verletzung der Intimsphäre: Auch bei öffentlichem Interesse gibt es absolute Schutzbereiche.
- Verdachtsberichterstattung: Nur zulässig bei ausreichendem Mindestbestand an Beweistatsachen und Anhörung des Betroffenen.

## Gegendarstellung

### Anspruchsgrundlage
- Landespressegesetze: Betroffene Person hat Anspruch auf Veröffentlichung einer Gegendarstellung.
- Voraussetzung: Veröffentlichung von Tatsachenbehauptungen (nicht Meinungen), die die Person betreffen.
- Keine Prüfung der Richtigkeit durch Redaktion; Veröffentlichungspflicht besteht auch bei Zweifeln.

### Form und Fristen
- Gegendarstellung: Schriftlich; vom Betroffenen oder Bevollmächtigten unterzeichnet.
- Frist: Einreichung innerhalb von (je nach Landesgesetz) 3 Monaten nach Veröffentlichung.
- Umfang: Darf nicht unverhältnismäßig länger sein als der Originalbericht.
- Verlag muss die Gegendarstellung: In derselben Ausgabe (Online: unverzüglich), gleiche Schriftgröße, gleiches Layout.

### Verweigerungsgründe
- Gegendarstellung enthält strafbare Inhalte.
- Gegendarstellung bezieht sich nicht auf Tatsachenbehauptungen (sondern Meinungen).
- Gegendarstellung ist offensichtlich unwahr.

## Unterlassungsanspruch bei Pressedelikten

### Anspruchsgrundlage
- § 823 Abs. 1 BGB i.V.m. § 1004 BGB analog: Betroffener kann Unterlassung unwahren oder persönlichkeitsverletzenden Berichterstattung verlangen.
- § 824 BGB: Kreditgefährdung; unwahre Tatsachen, die geeignet sind, den Kredit oder das Fortkommen zu gefährden.

### Verfahren
1. **Abmahnung**: Betroffener fordert Unterlassung; Frist 24–72 Stunden (presserechtlich dringend).
2. **Unterlassungserklärung**: Verlag gibt strafbewehrte Erklärung ab (Vertragsstrafe bei Zuwiderhandlung).
3. **Einstweilige Verfügung**: Wenn Unterlassungserklärung verweigert; Gericht kann innerhalb von Stunden entscheiden.
4. **Hauptsacheklage**: Dauerhafte gerichtliche Unterlassung.

### Schadensersatz und Geldentschädigung
- Immaterieller Schaden (Geldentschädigung): Bei schwerwiegender, schuldhafter Persönlichkeitsrechtsverletzung; Höhe je nach Schwere und Verbreitung.
- Materieller Schaden: Entgangene Geschäfte, Rufschaden (schwer zu beziffern, aber möglich).

## Verdachtsberichterstattung

### Voraussetzungen (BGH-Rechtsprechung)
1. Mindestbestand an Belegen für den Verdacht.
2. Anhörung des Betroffenen vor Veröffentlichung (Stellungnahme einholen).
3. Berichterstattung als Verdacht kennzeichnen (nicht als feststehende Tatsache).
4. Verhältnismäßigkeit: Öffentliches Interesse überwiegt Persönlichkeitsschutz.

### Online-Berichte und Löschungsansprüche
- Nicht aktualisierte Online-Artikel über abgeschlossene Verfahren können Persönlichkeitsrechte verletzen (Recht auf Vergessenwerden).
- EuGH, C-131/12 (Google Spain): Recht auf Löschung aus Suchmaschinenindex.
- BGH „Recht auf Vergessenwerden I und II" (2019): Deutsche Regelung für Online-Presseberichte.

## Satire und Kunstfreiheit

- Satire ist von Art. 5 Abs. 3 GG (Kunstfreiheit) oder Art. 5 Abs. 1 (Meinungsfreiheit) geschützt.
- Grenzen: Satire darf nicht als Tarnmantel für ernsthafte Tatsachenbehauptungen dienen.
- Kennzeichnung als Satire / Parodie wichtig; Verwechslungsgefahr mit echter Berichterstattung vermeiden.

## Typische Fallen

- **Verdachtsberichterstattung ohne Anhörung**: Verlag berichtet über Korruptionsverdacht ohne Stellungnahme → Unterlassung und Gegendarstellung.
- **Meinung als Tatsache formuliert**: „Das Unternehmen hat betrogen" ist Tatsachenbehauptung, nicht Meinung → muss wahr sein.
- **Online-Artikel nicht aktualisiert**: Berichterstattung über Ermittlungsverfahren; Verfahren längst eingestellt; Artikel online noch abrufbar → Löschungsanspruch.
- **Gegendarstellung verspätet oder zu lang**: Formfehler führt zu Ablehnung; Betroffener verliert Anspruch.

## Checkliste Presserechtliche Prüfung

- [ ] Tatsachenbehauptungen von Meinungsäußerungen getrennt
- [ ] Verdachtsberichterstattung: Mindestbelege vorhanden, Betroffener angehört
- [ ] Online-Archiv: Abgeschlossene Verfahren aktualisiert oder mit Nachtrag versehen
- [ ] Gegendarstellungs-Eingang: Form und Frist geprüft, Veröffentlichungspflicht bewertet
- [ ] Satire: Deutlich als solche erkennbar

## Quellenreferenzen

- GG Art. 5: https://www.gesetze-im-internet.de/gg/art_5.html
- BGB §§ 823, 824: https://dejure.org/gesetze/BGB/823.html
- BVerfG „Lüth" BVerfGE 7, 198: https://www.bverfg.de
- BGH „Recht auf Vergessenwerden I" VI ZR 405/18: https://www.bgh.de
- EuGH C-131/12 (Google Spain): https://eur-lex.europa.eu

## Output-Formate

- **Presserechtliche Risikoprüfung**: Bericht auf Persönlichkeitsrechtsrisiken analysiert
- **Gegendarstellungs-Vorlage**: Formelles Anforderungsschreiben
- **Unterlassungserklärung** (strafbewehrt)
- **Abmahnungs-Antwort**: Reaktion auf presserechtliche Abmahnung
- **Online-Archiv-Audit**: Berichte mit Aktualisierungsbedarf identifiziert

---

## Skill: `verlagsinsolvenz-rechte-rueckfall-und-lagerbestand`

_Verlagsrecht: Verlagsinsolvenz — Rückfall von Nutzungsrechten an Autoren, Lagerbestandsverwertung, InsO §§ 103–119, UrhG §§ 41–42 und praktische Schritte für betroffene Autoren im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-025 · Verlagsinsolvenz: Rechterückfall und Lagerbestand

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Die **Insolvenz eines Verlags** ist für Autoren ein Worst-Case-Szenario: Honorare bleiben aus, Bücher werden nicht mehr vertrieben, Nutzungsrechte sind unklar. Kläre die Rechtslage beim Verlagsinsolvenzverfahren, die Möglichkeiten des Rechterückfalls, den Umgang mit Lagerbeständen und die Schritte, die betroffene Autoren unternehmen müssen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| InsO § 103 | Wahlrecht des Insolvenzverwalters bei gegenseitigen Verträgen | https://www.gesetze-im-internet.de/inso/__103.html |
| InsO § 108 | Fortsetzung von Dienst- und Arbeitsverhältnissen | https://www.gesetze-im-internet.de/inso/__108.html |
| InsO § 119 | Unwirksamkeit von Lösungsklauseln | https://www.gesetze-im-internet.de/inso/__119.html |
| InsO § 35 | Insolvenzmasse: alle pfändbaren Rechte des Schuldners | https://www.gesetze-im-internet.de/inso/__35.html |
| UrhG § 41 | Rückruf wegen Nichtausübung | https://dejure.org/gesetze/UrhG/41.html |
| VerlG § 7 | Rücktritt bei Nichterscheinen | https://www.gesetze-im-internet.de/verlg/__7.html |
| BGB § 346 | Rücktrittsfolgen: Rückgewähr | https://dejure.org/gesetze/BGB/346.html |

## Verlagsinsolvenz: Basisszenarien

### Szenario 1: Verlag stellt Betrieb ein (vorläufige Insolvenz)
- Vorläufiger Insolvenzverwalter übernimmt; prüft ob Fortführung oder Zerschlagung.
- Bis zur Eröffnung: Verlag kann keine neuen Verträge eingehen; laufende Verträge bleiben bestehen.

### Szenario 2: Insolvenzeröffnung
- Insolvenzverwalter (IV) tritt in alle Verlagsverträge ein (§ 103 InsO).
- IV hat **Wahlrecht**: Verlagsvertrag erfüllen (Honorar zahlen, Buch weiter vertreiben) oder nicht erfüllen (Vertrag gilt als nicht erfüllt; Autor hat Schadensersatzanspruch als einfache Insolvenzforderung).

### Szenario 3: Masselosigkeit / Scheitern der Fortführung
- Insolvenzverfahren wird mangels Masse eingestellt.
- Autor erhält keine Honorare; Nutzungsrechte fallen zurück (§ 41 UrhG nach Wartefrist).

## Das Wahlrecht des Insolvenzverwalters (§ 103 InsO)

- IV kann für jeden Verlagsvertrag wählen:
 - **Erfüllung wählen**: IV zahlt ausstehende Honorare aus Insolvenzmasse und kann Nutzungsrechte weiterhin ausüben.
 - **Nichterfüllung wählen / schweigen**: Der Verlagsvertrag gilt als nicht erfüllt; Autor hat Schadensersatzanspruch; Nutzungsrechte fallen zurück.
- **Wichtig**: Schweigen des IV = Nichterfüllung nach Fristsetzung durch den Autor (§ 103 Abs. 2 InsO).
- **Fristsetzung durch Autor**: Autor schreibt IV an und fordert ihn auf, binnen angemessener Frist (2–4 Wochen) zu wählen.

## Rechterückfall an Autor

### Nach Nichterfüllungswahl des IV
- Nutzungsrechte fallen kraft Gesetzes an Autor zurück; keine gesonderte Erklärung nötig.
- Autor kann Rechte an neuen Verlag weiterlizenzieren.
- Schadensersatz (ausstehende Honorare, entgangener Gewinn): Als einfache Insolvenzforderung zur Tabelle anmelden.

### UrhG § 41 — Rückruf wegen Nichtausübung (zusätzliches Instrument)
- Wenn IV die Nutzungsrechte nicht ausübt und Interessen des Autors erheblich beeinträchtigt: § 41 UrhG-Rückruf möglich.
- Frist: Rückruf nach 2 Jahren Nichtausübung; Ankündigung 3 Monate vorher.
- Praktisch: Oft schneller als § 103 InsO-Weg; hängt von tatsächlichem Vertriebsstopp ab.

## Forderungsanmeldung zur Insolvenztabelle

### Was anmelden?
- Ausstehende Honoraransprüche.
- Vorschüsse, die noch nicht durch Tantiemen verdient sind (nicht rückzahlbar, wenn Verlag die Erscheinungspflicht nicht erfüllt hat).
- Schadensersatz aus Rücktritt.

### Wie anmelden?
- Formular: Forderungsanmeldung beim Insolvenzverwalter.
- Frist: Anmeldefrist in Bekanntmachung des Insolvenzverfahrens (Bundesanzeiger); typisch 3 Monate.
- Quote: Einfache Forderungen erhalten typisch 2–20 % der Forderungssumme; Masseverbindlichkeiten werden vorrangig befriedigt.

## Lagerbestandsverwertung

- Lagerbestände (Bücher im Verlagslager) sind Teil der Insolvenzmasse.
- IV kann entscheiden: Bücher weiter verkaufen, Lager abverkaufen oder Bücher makulieren.
- **Preisbindung**: Auch in der Insolvenz gilt die Preisbindung für lieferbare Bücher, solange der Ladenpreis nicht förmlich aufgehoben wurde.
- Notverkauf zu Ramschpreisen: Nur zulässig, wenn Verlag den Preis zuvor aufgehoben hat oder wenn es sich um Mängelexemplare handelt.
- Übernahme des Verlagsprogramms durch Erwerber: Käufer tritt in bestehende Verlagsverträge ein (§ 25 UmwG analog oder vertragliche Gestaltung); Zustimmung der Autoren erforderlich.

## Schutzklauseln im Verlagsvertrag (präventiv)

1. **Insolvenzklausel (Vorsicht!)**: Klauseln, die den Vertrag bei Insolvenz des Verlags automatisch beenden, sind nach § 119 InsO unwirksam.
2. **Rückruf-Klausel**: Vertraglich vereinbartes Rückrufrecht bei Einstellung des Vertriebs, Insolvenzantrag oder Verstoß gegen Erscheinungspflicht.
3. **Treuhandkonto für Vorschüsse**: Vorschussbetrag auf Treuhandkonto; fällt nicht in Insolvenzmasse des Verlags.
4. **Mindestumsatzklausel**: Wenn Umsatz unter X → Autor kann Rücktritt erklären.

## Typische Fallen

- **Fristsetzung an IV vergessen**: Autor wartet passiv; IV wählt nicht → Limbo-Zustand über Monate.
- **Forderung nicht angemeldet**: Anmeldefrist versäumt → Forderung grundsätzlich ausgeschlossen (§ 177 InsO).
- **Nutzungsrecht-Rückfall nicht beansprucht**: Autor nimmt an, Rechte seien von allein zurückgefallen, wartet → Unklarheit; IV bestreitet Rückfall.
- **Verlagsübernahme ohne Zustimmung**: Erwerber des insolventen Verlags will weiter Bücher verkaufen; ohne Autorenvertragsübernahme ist dies rechtswidrig.

## Checkliste Verlagsinsolvenz

- [ ] Insolvenzbekanntmachung im Bundesanzeiger gefunden
- [ ] Fristsetzung an IV nach § 103 Abs. 2 InsO gesendet (Frist: 2–4 Wochen)
- [ ] Forderungsanmeldung zur Tabelle eingereicht (ausstehende Honorare, Schadensersatz)
- [ ] Anmeldefrist beachtet (aus Bekanntmachung)
- [ ] Bei Nichtausübung: § 41 UrhG-Rückruf-Ankündigung gesendet
- [ ] Neuen Verlag suchen / Selbstveröffentlichung prüfen

## Quellenreferenzen

- InsO §§ 103, 119: https://www.gesetze-im-internet.de/inso/__103.html
- UrhG § 41: https://dejure.org/gesetze/UrhG/41.html
- VerlG § 7: https://www.gesetze-im-internet.de/verlg/__7.html
- BGH, Urt. v. 25.10.2012 – IX ZR 207/11 (Insolvenz und Verlagsvertrag): https://www.bgh.de
- Insolvenzbekanntmachungen: https://www.insolvenzbekanntmachungen.de

## Output-Formate

- **Fristsetzungs-Schreiben** an Insolvenzverwalter (§ 103 Abs. 2 InsO)
- **Forderungsanmeldung**: Standardformular mit Berechnung
- **Rückruf-Ankündigung** nach § 41 UrhG
- **Nutzungsrecht-Rückfall-Erklärung** (für neuen Verlag)
- **Neuen-Verlagsvertrag-Briefing**: Was braucht der neue Verlag an Unterlagen

---

## Skill: `fachzeitschrift-peer-review-und-haftung`

_Verlagsrecht: Fachzeitschriften, Peer-Review-Verfahren, Haftung für fehlerhafte Fachinformation und Autorenrechte — UrhG §§ 38 und 32d, wissenschaftliche Publikationsstandards im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-029 · Fachzeitschrift, Peer Review und Haftung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Wissenschaftliche und juristische Fachzeitschriften unterliegen einem eigenen Rechtsregime: Urheberrechte der Autoren bei Zeitschriftenbeiträgen, Zweitveröffentlichungsrecht, Peer-Review-Vertraulichkeit, Haftung für fehlerhafte Fachinformationen und die Retraction-Praxis. Kläre diese spezifischen Fragen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 38 | Urheberrecht an Beiträgen in Periodika | https://dejure.org/gesetze/UrhG/38.html |
| UrhG § 38 Abs. 4 | Zweitveröffentlichungsrecht nach 12 Monaten | https://dejure.org/gesetze/UrhG/38.html |
| UrhG § 32 | Angemessene Vergütung (auch für Journalisten) | https://dejure.org/gesetze/UrhG/32.html |
| UrhG § 32d | Auskunftsanspruch | https://dejure.org/gesetze/UrhG/32d.html |
| BGB § 823 | Haftung für Fachinformations-Fehler | https://dejure.org/gesetze/BGB/823.html |
| PressR | Presserecht der Länder; Gegendarstellungsrecht | (länderspezifisch) |
| DSM-RL Art. 17 | Plattformhaftung für Zeitschriften-Uploads | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Urheberrecht an Zeitschriftenbeiträgen (§ 38 UrhG)

### Grundregel (§ 38 Abs. 1 UrhG)
- Autor überträgt durch Einreichung des Beitrags an die Zeitschrift i.d.R. das ausschließliche Nutzungsrecht für den Erstdruck.
- Nach 1 Jahr (bei entgeltlichen Zeitschriften) fällt das ausschließliche Nutzungsrecht automatisch zurück; Autor kann dann das einfache Nutzungsrecht anderweitig verwerten.

### Zweitveröffentlichungsrecht (§ 38 Abs. 4 UrhG)
- Beim Urheber verbleibend: Nach 12 Monaten nach Erstveröffentlichung darf der Autor den Beitrag **in einer frei zugänglichen Datenbank** (Repositorium) zugänglich machen.
- Voraussetzung: Beitrag erschien in einer überwiegend institutionell geförderten periodischen Sammlung (wissenschaftliche Zeitschrift).
- Nur die **angenommene Manuskriptversion** (nicht das Verlags-PDF).
- Einschränkung: Nur für wissenschaftliche Beiträge, nicht für Tageszeitungen / Meinungsartikel.

### Vergütung (§ 32 UrhG)
- Fachzeitschriftenbeiträge werden oft unentgeltlich eingereicht (insbes. Wissenschaft).
- § 32 UrhG: Unangemessene Unentgeltlichkeit ist nicht automatisch unwirksam; bei entsprechendem Branchenbrauch kann Unentgeltlichkeit angemessen sein.
- Journalisten: Gemeinsame Vergütungsregeln für redaktionelle Inhalte; Ansprüche aus § 32 UrhG.

## Peer Review: Rechtliche Aspekte

### Vertraulichkeit
- Peer Review ist typisch doppelt blind (weder Reviewer noch Autor wissen voneinander).
- Vertraulichkeitsvereinbarung: Reviewer verpflichtet sich zur Nichtveröffentlichung des Manuskripts.
- Kein gesetzliches Schweigeprivileg; nur vertragliche Vertraulichkeit.

### Reviewer-Haftung
- Reviewer kann persönlich für fehlerhafte Begutachtung haften (z.B. wenn wissenschaftliche Daten zu Unrecht als gefälscht bezeichnet werden → Persönlichkeitsrechtsverletzung, Verleumdung).
- Verlag haftet nicht für subjektive Reviewer-Urteile; aber für grob fahrlässige organisatorische Mängel im Peer-Review-Prozess.

### Haftung für verweigerte Publikation
- Verlag hat grundsätzlich Publikationsfreiheit; kann Beiträge ablehnen.
- Grenzen: Keine sittenwidrige Diskriminierung; Monopolstellung bei Leitjournalen kann Kontrahierungszwang begründen (GWB §§ 18, 19).

## Haftung für fehlerhafte Fachinformationen

### Grundsatz
- Verlage haften nicht für inhaltliche Fehler in Fachbeiträgen (kein Beratungsvertrag).
- **Ausnahmen**:
 - Verlag hat eigene Expertise beworben und besonderes Vertrauen in Richtigkeit geweckt.
 - Offensichtliche Fehler, die ein Fachlektorat hätte erkennen müssen.
 - Fehler in Lehrbüchern, auf die Studenten in Prüfungen vertrauen → höhere Sorgfaltspflicht?

### Retraction und Richtigstellung
- Retraction: Zurückziehen eines veröffentlichten Beitrags wegen Fehler, Plagiats oder Datenfälschung.
- Prozess: Redaktion beschließt Retraction; Retraction-Mitteilung wird in Zeitschrift veröffentlicht.
- Retraction Watch: Datenbank für zurückgezogene wissenschaftliche Artikel.
- Rechtliche Konsequenz: Retraction löst keinen automatischen Schadensersatz aus; betroffener Autor kann aber auf Unterlassung des Retraction-Hinweises klagen, wenn Retraction unberechtigt.

## Gegendarstellungsrecht in Fachzeitschriften

- Landespressegesetze: Gegendarstellungsrecht gilt für periodisch erscheinende Druckerzeugnisse.
- Voraussetzung: Tatsachenbehauptung im Artikel (nicht Meinungsäußerung).
- Gegendarstellung: Gleiche Stelle, gleiche Schrift, ohne redaktionelle Kommentierung.
- Online-Zeitschriften: Umstrittener Anwendungsbereich; ggf. presserechtliche Vorschriften für Online-Publikationen.

## Open-Access-Pflicht und Zeitschriften (§ 38 Abs. 4 UrhG, DSM-RL)

- § 38 Abs. 4 UrhG: Unabdingbares Zweitveröffentlichungsrecht für wissenschaftliche Autoren nach 12 Monaten.
- Verlag kann dieses Recht nicht vertraglich ausschließen.
- DSM-RL Art. 25: Verbot der Umgehung; Verlag darf keine Klauseln nutzen, die das Zweitveröffentlichungsrecht aushöhlen.

## Typische Fallen

- **Vertrag schließt Zweitveröffentlichungsrecht aus**: Klausel unwirksam (§ 38 Abs. 4 UrhG ist unabdingbar per § 38 Abs. 4 S. 4 UrhG).
- **Reviewer veröffentlicht Manuskript**: Reviewer bricht Vertraulichkeit → Vertragsstrafe; aber schwer zu verfolgen ohne Beweis.
- **Retraction ohne Grund**: Redaktion retrachtet Artikel ohne wissenschaftliche Grundlage → Autor kann auf Löschung des Retraction-Hinweises klagen.
- **Fachbuch-Haftungsklausel in AGB**: Im B2B-Bereich weitgehend wirksam; im B2C-Bereich (Verbraucher) eingeschränkt.

## Checkliste Fachzeitschrift

- [ ] Autorenvertrag: Zweitveröffentlichungsrecht nach § 38 Abs. 4 UrhG ausdrücklich zugestanden
- [ ] Peer-Review-Vertraulichkeitsvereinbarung für alle Reviewer
- [ ] Retraction-Prozess dokumentiert und transparent
- [ ] Haftungsdisclaimer für Fachinhalte AGB-rechtlich geprüft
- [ ] Gegendarstellungs-Prozess für periodische Online-Fachzeitschrift definiert
- [ ] OA-Pflichten für geförderte Autoren im Autorenformular abgefragt

## Quellenreferenzen

- UrhG § 38: https://dejure.org/gesetze/UrhG/38.html
- DSM-RL Art. 17, 25: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- Retraction Watch: https://retractionwatch.com
- BGH „Fachzeitschrift" I ZR 44/10: https://www.bgh.de
- GWB §§ 18, 19: https://dejure.org/gesetze/GWB/18.html

## Output-Formate

- **Autorenvertrag-Check**: Zweitveröffentlichungsrecht, OA-Kompatibilität
- **Peer-Review-NDA**: Standardformular für Reviewer
- **Retraction-Protokoll**: Kriterien, Prozess, Kommunikation
- **Haftungsdisclaimer-Check**: AGB-Klauseln für Fachinhalte
- **Gegendarstellungs-Checkliste**: Formal, materiell, Frist

---

## Skill: `autor-herausgeber-mitwirkende-rechtekette`

_Verlagsrecht: Rechtekette bei Sammelwerken — Autor, Herausgeber, Mitwirkende, Übersetzer und Verlag; Klärung von Urheber-, Nutzungs- und Vergütungsrechten nach UrhG und VerlG im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-003 · Autor, Herausgeber, Mitwirkende: Rechtekette im Sammelwerk

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Verlagsprojekte mit mehreren Beteiligten — Herausgeberbände, Anthologien, wissenschaftliche Festschriften, Lehrwerke — erfordern eine sorgfältige **Rechtekette**: Wer hat welche Urheberrechte, wer hat welche Nutzungsrechte eingeräumt, wer hat welchen Vergütungsanspruch? Dieser Skill kartiert alle Beteiligten, ihre Rollen und ihre Rechtsposition systematisch.

## Rechtsgrundlagen

| Norm | Regelungsgehalt | Quelle |
|------|----------------|--------|
| UrhG § 2 | Schutzfähige Werke: Sprachwerke, Sammelwerke, Übersetzungen | https://dejure.org/gesetze/UrhG/2.html |
| UrhG § 4 | Sammelwerke und Datenbankwerke | https://dejure.org/gesetze/UrhG/4.html |
| UrhG § 8 | Miturheber: gemeinschaftliche Schöpfung | https://dejure.org/gesetze/UrhG/8.html |
| UrhG § 9 | Werkverbindung: selbständige Werke | https://dejure.org/gesetze/UrhG/9.html |
| UrhG § 31 | Nutzungsrechtseinräumung | https://dejure.org/gesetze/UrhG/31.html |
| UrhG § 32 | Angemessene Vergütung | https://dejure.org/gesetze/UrhG/32.html |
| UrhG § 32d | Auskunftsanspruch | https://dejure.org/gesetze/UrhG/32d.html |
| VerlG § 1 | Verlagsvertrag mit dem Urheber | https://www.gesetze-im-internet.de/verlg/__1.html |
| VerlG §§ 28 ff. | Honorar und Abrechnung | https://www.gesetze-im-internet.de/verlg/ |
| DSM-RL Art. 19 | Transparenzpflicht gegenüber Urhebern | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Beteiligte Parteien und ihre Rollen

### 1. Alleinautor
- Einziger Schöpfer des Werks; alle Urheberrechte liegen bei ihm.
- Kann alle Nutzungsrechte im Verlagsvertrag vollständig einräumen.

### 2. Miturheber (§ 8 UrhG)
- Mehrere haben gemeinsam ein Werk geschaffen; Beiträge sind nicht trennbar.
- Nutzungsrechte können nur gemeinschaftlich eingeräumt werden; einzelne Miturheber können nicht allein handeln.
- Verfügungen über Anteile am Gesamtwerk erfordern Zustimmung aller.

### 3. Werkverbindung (§ 9 UrhG)
- Mehrere Autoren verbinden selbständige Werke zu einem gemeinsamen Werk (z.B. Text + Illustrationen).
- Jeder behält sein Urheberrecht; gemeinschaftliche Rechteausübung nach Vereinbarung.

### 4. Herausgeber eines Sammelwerks (§ 4 UrhG)
- Schöpferische Eigenleistung bei Auswahl und Anordnung der Beiträge → eigenes Urheberrecht an der Sammlung.
- Kein Urheberrecht an den Einzelbeiträgen der Autoren.
- Verlagsvertrag mit dem Herausgeber regelt Rechte an der Sammlung; separate Verträge mit Beitragsautoren nötig.

### 5. Beitragsautoren (Kapitelautoren, Essayisten)
- Jeder hält sein Urheberrecht am eigenen Beitrag.
- Nutzungsrechtseinräumung an Herausgeber oder Verlag durch separate Autorenverträge oder Erklärungen.
- Vergütungsanspruch nach § 32 UrhG; gemeinsame Vergütungsregeln anwendbar.

### 6. Übersetzer
- Übersetzung ist ein selbständiges Schutzwerk (§ 3 UrhG).
- Übersetzer benötigt Lizenz des Originalautors/Verlags; Verlagsvertrag für Übersetzung separat (VerlG § 35).
- Eigener Vergütungsanspruch; ggf. eigener Auskunftsanspruch nach § 32d UrhG.

### 7. Illustratoren, Fotografen, Kartografen
- Bildwerke (§ 2 Abs. 1 Nr. 5 UrhG) sind eigenständig geschützt.
- Nutzungsrechtseinräumung durch separate Bildrechte-Verträge oder Werk-/Dienstverträge.
- Bei Auftragsarbeiten: Kein automatischer Rechteübergang; schriftliche Einräumung erforderlich.

## Rechteketten-Analyse

### Schritt 1: Identifikation aller Werkteile
Liste alle Komponenten des Gesamtwerks:
- Haupttext (Autor/Autoren)
- Kapitel (ggf. verschiedene Autoren)
- Vorwort, Einleitung, Nachwort (Herausgeber oder Dritte)
- Abbildungen, Fotos, Grafiken
- Tabellen, Karten, Diagramme
- Übersetzungen
- Register, Index (Sonderfall: Leistungsschutz oder Datenbankrecht)

### Schritt 2: Prüfung jeder Nutzungsrechtseinräumung
Für jede Komponente prüfen:
- Liegt eine schriftliche Nutzungsrechtseinräumung vor?
- Welche Nutzungsarten sind erfasst (§ 31 Abs. 1 UrhG)?
- Exklusiv oder nicht-exklusiv?
- Zeitlich und räumlich begrenzt?
- Vergütung vereinbart und angemessen (§ 32 UrhG)?

### Schritt 3: Lücken und Risiken
- Fehlende Verträge mit Beitragsautoren → Verlag hat kein Recht zur Veröffentlichung
- Unklare Nutzungsarten → Zweckübertragungsregel (§ 31 Abs. 5 UrhG) schließt Lücken restriktiv
- Kein Auskunftsanspruch geregelt → Beitragsautoren können § 32d UrhG geltend machen
- Übersetzungsrechte nicht gesichert → Fremdsprachige Ausgabe rechtswidrig

## Vergütungsansprüche und Auskunft

### § 32 UrhG — Angemessene Vergütung
- Jeder Urheber hat Anspruch auf angemessene Vergütung.
- Unangemessene Vergütung → Anpassungsanspruch; ggf. Klage.
- Gemeinsame Vergütungsregeln (§ 36 UrhG) zwischen Verbänden schaffen Vermutungswirkung.

### § 32a UrhG — Nachvergütung (Bestseller-Paragraf)
- Stellt sich heraus, dass vereinbarte Vergütung in auffälligem Missverhältnis zu tatsächlichen Erträgen steht → Anspruch auf weitere Beteiligung.
- Gilt für alle Miturheber und Beitragsautoren anteilig.

### § 32d UrhG — Auskunftsanspruch
- Jeder Urheber kann jährlich Auskunft über Art und Umfang der Werknutzung sowie erzielte Vergütungen verlangen.
- DSM-RL Art. 19 gibt EU-rechtliche Grundlage für verstärkte Transparenzpflichten.

## Typische Fallen

- **Fehlende Verträge mit Beitragsautoren**: Häufig bei Tagungsbänden oder Festschriften; ohne schriftliche Nutzungsrechtseinräumung kein Veröffentlichungsrecht.
- **Herausgeber-Rolle überschätzt**: Herausgeber hat kein Recht, im Namen der Beitragsautoren Lizenzen zu vergeben, sofern keine Vollmacht vorliegt.
- **Übersetzungsrechte nicht separat gesichert**: Originalverlag hat oft keine Lizenz für alle Sprachversionen.
- **Bildrechte vergessen**: Fotos in der Originalveröffentlichung decken nicht automatisch die Nutzung in digitalen Ausgaben ab.
- **Miturheber-Blockade**: Bei § 8 UrhG-Situationen kann ein Miturheber die Verwertung blockieren.

## Checkliste Rechtekette

- [ ] Liste aller Werkteile mit Urhebern erstellt
- [ ] Für jeden Werkteil: schriftlicher Nutzungsrechtsvertrag vorhanden
- [ ] Nutzungsarten vollständig und klar benannt
- [ ] Vergütung angemessen und nachvollziehbar (§ 32 UrhG)
- [ ] Auskunftsklausel (§ 32d UrhG / DSM-RL Art. 19) vertraglich geregelt
- [ ] Drittmaterial (Bilder, Tabellen) mit eigenem Rechtenachweis

## Quellenreferenzen

- UrhG §§ 4, 8, 9: https://dejure.org/gesetze/UrhG/8.html
- UrhG § 32d: https://dejure.org/gesetze/UrhG/32d.html
- DSM-Richtlinie 2019/790 Art. 19: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- BGH, Urt. v. 20.01.1994 – I ZR 322/91 (Miturheber Sammelwerk): https://www.bgh.de
- VerlG §§ 28 ff.: https://www.gesetze-im-internet.de/verlg/

## Output-Formate

- **Rechtekettenmatrix**: Alle Werkteile × Nutzungsarten × Rechtsstatus
- **Lückenliste**: Fehlende Verträge, offene Nutzungsarten
- **Vergütungsübersicht**: Alle Beitragsautoren mit Vergütungsansprüchen
- **Muster-Beitragsautorenvertrag**: Standardisiertes Kurzformular für Sammelwerke

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 41 UrhG
- § 32d UrhG
- § 32a UrhG
- § 6 BuchPrG
- § 32 UrhG
- § 7 BuchPrG
- § 38 UrhG
- § 3 BuchPrG
- § 31 UrhG
- § 4 UrhG
- § 14 UrhG
- § 51 UrhG

### Leitentscheidungen

- EuGH C-174/15
- BGH I ZR 198/13
- BGH I ZR 136/20
- EuGH C-299/23
- EuGH C-202/12

---

## Skill: `buchhandelsvertrag-konditionen-und-remission`

_Verlagsrecht: Buchhandelsvertrag zwischen Verlag und Buchhandel — Konditionenabkommen, Remissionsrecht, Retourenquoten, Auslieferungsverträge und Buchpreisbindungs-Compliance im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-032 · Buchhandelsvertrag, Konditionen und Remission

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Der **Buchhandelsvertrag** zwischen Verlag (oder Auslieferung) und Buchhandlung ist die Grundlage des Buchvertriebssystems. Er regelt Rabatte, Zahlungsbedingungen, Remissionsrechte und Buchpreisbindungs-Pflichten. Analysiere die typischen Konditionenmodelle und die Remissions-Praxis.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG §§ 3–5 | Preisbindung, Verpflichtung des Buchhandels zum gebundenen Preis | https://www.gesetze-im-internet.de/buchprg/ |
| BuchPrG § 4 | Buchhandel als Vertragspartner: Preisbindungsklausel | https://www.gesetze-im-internet.de/buchprg/__4.html |
| HGB §§ 343 ff. | Handelsrecht: Kaufmann, Handelsgeschäft | https://dejure.org/gesetze/HGB/343.html |
| HGB § 377 | Untersuchungs- und Rügeobliegenheit beim Handelskauf | https://dejure.org/gesetze/HGB/377.html |
| BGB §§ 305 ff. | AGB-Recht: Konditionenabkommen als AGB | https://dejure.org/gesetze/BGB/305.html |
| BGB § 448 | Gefahrübergang beim Kauf | https://dejure.org/gesetze/BGB/448.html |

## Konditionensystem im Buchhandel

### Barsortimentsrabatt vs. Direktbezug
- **Barsortiment** (Grossist: Libri, KNV/VVA, Umbreit): Buchhandel kauft beim Barsortiment; Verlag liefert an Barsortiment.
 - Verlagsrabatt an Barsortiment: 40–50 % des Ladenpreises.
 - Barsortiment verkauft an Buchhandel mit 20–25 % Buchhandelsrabatt.
- **Direktbezug**: Buchhandel bestellt direkt beim Verlag oder dessen Auslieferung.
 - Buchhandelsrabatt: Typisch 30–40 % je nach Bestellgröße.
 - Kleinbuchhandlungen: 25–30 %.
 - Großfilialketten: 35–45 %.

### Konditionenabkommen des Börsenvereins
- Konditionenabkommen zwischen Verlegerverbänden und Buchhandelsverbänden legt Grundrabattrahmen fest.
- Sonderkonditionen: Verhandlung möglich, aber darf nicht zu Buchpreisbindungsverstoß führen.

### Zahlungsbedingungen
- Netto-Zahlungsziel: 30–90 Tage nach Rechnungserhalt.
- Skonto: 2–3 % bei Zahlung innerhalb von 10 Tagen üblich.
- Factoring: Manche Verlage/Auslieferungen nutzen Factoring; Buchhandel zahlt an Factor.

## Remission (Rücksendungsrecht)

### Remissionsrecht des Buchhandels
- Buchhandel darf unverkaufte Bücher an Verlag/Auslieferung zurücksenden.
- Grundlage: Vertragsklausel (nicht gesetzlich); im Buchhandel historisch als „Kommissionsähnliches" Recht etabliert.
- **Remissionsquote**: Prozentsatz der Liefermenge, die zurückgesandt werden darf; üblich 30–60 %.
- Bedingung: Rücksendung in verkaufsfähigem Zustand; Buchhandel trägt Rücksendungskosten (oft).

### Remission und Buchpreisbindung
- Remittierte Exemplare werden vom Verlag als Remittenden reklassifiziert.
- Kennzeichnung bei Wiederverkauf als Remittend unter Ladenpreis (§ 6 BuchPrG) erforderlich.
- Verlag sollte keine Abmahnung riskieren, wenn Remittenden ohne Kennzeichnung erneut als Neuware verkauft werden.

### Remissionsklausel im Buchhandelsvertrag
- Klare Regelung: Remissionsfenster (z.B. Bücher die 2 Jahre oder mehr im Lager), maximale Remissionsquote, Konditionierung (gut verkaufte Titel: keine Remission).
- Beschädigte Remittenden: Buchhandel haftet für Schäden durch sachgemäßen Umgang; ungerechtfertigte Beschädigungen → Schadensersatz.

## Auslieferungsvertrag

### Typischer Inhalt
1. Lagerhaltung: Auslieferung lagert den Verlagsbestand.
2. Auftragsabwicklung: Bestellungen annehmen, kommissionieren, versenden.
3. Abrechnung: Wöchentliche oder monatliche Abrechnung über Umsatz, Remittenden, Bestände.
4. Versicherung: Lagerware versichert durch Auslieferung (oder Verlag trägt Risiko).
5. Lagerkostenmodell: Flat-Rate oder per-Exemplar-Kosten; Lagergebühren für Slow-Mover.
6. Exklusivität: Häufig exklusive Auslieferung in DACH; eigene Vertriebskanäle behalten.

### Kündigung des Auslieferungsvertrags
- Verlag trägt Lagerbestand aus; Auslieferung stellt neue Bestellungen ein.
- Übergangszeit: Typisch 3–6 Monate für geordneten Wechsel.
- Lagerbestandsübertragung: Dokumentation aller Exemplare, Zustand, ISBN; Inventar bei Übergabe.

## Buchpreisbindungs-Compliance im Buchhandelsvertrag

### Pflichten des Buchhandels (§ 4 BuchPrG)
- Buchhandel verpflichtet sich im Vertrag, den gebundenen Ladenpreis einzuhalten.
- Verlag kann Buchhandelsvertrag kündigen oder Belieferung einstellen, wenn Buchhandel systematisch Preisbindung verletzt.

### Meldesystem für Verstöße
- Verlag informiert Buchhandel über Preisänderungen rechtzeitig (EDI, VLB-Update, Preisliste).
- Bei Buchhandels-Verstoß: Abmahnung (intern) → Kündigungsandrohung → Kündigung des Liefervertrags.

## Typische Fallen

- **Remissionsrecht ohne Quoten-Klausel**: Buchhandel sendet beliebig zurück; Verlag hat keine Kontrolle.
- **Konditionenrabatt und Buchpreisbindung**: Höherer Rabatt an bevorzugte Buchhandlung → wenn Endkundenpeis trotzdem stimmt, kein Verstoß; Rabatt ist Verlagssache.
- **Auslieferungsvertrag ohne Versicherungsklausel**: Lager brennt ab; Verlag hat keinen Ersatzanspruch.
- **Beschädigte Remittenden als Neuware reklassifiziert**: Auslieferung verbucht zurückgesandtes beschädigtes Exemplar als neu → Verkauf ohne Mängelkennzeichnung → Preisbindungsverstoß.

## Checkliste Buchhandelsvertrag

- [ ] Rabattstaffel und Zahlungsbedingungen klar vereinbart
- [ ] Remissionsquote und Remissionsfenster begrenzt
- [ ] Buchpreisbindungsklausel (§ 4 BuchPrG) im Vertrag
- [ ] Auslieferungsvertrag: Versicherung, Lagerkosten, Kündigung geregelt
- [ ] Remittend-Kennzeichnungspflicht im Vertrag festgehalten
- [ ] Kommunikationswege für Preisänderungen definiert (EDI, E-Mail)

## Quellenreferenzen

- BuchPrG § 4: https://www.gesetze-im-internet.de/buchprg/__4.html
- HGB § 377: https://dejure.org/gesetze/HGB/377.html
- Börsenverein, Konditionenabkommen: https://www.boersenverein.de
- Barsortiment Libri: https://www.libri.de
- BGH, Urt. v. 29.05.2018 – I ZR 171/16 (Buchhandelsvertrag): https://www.bgh.de

## Output-Formate

- **Konditionenvergleich**: Aktueller Vertrag vs. Marktstandard
- **Remissions-Analyse**: Remissionsquoten und Kostenwirkung
- **Buchhandelsvertrag-Muster**: Mindestklauseln
- **Auslieferungsvertrag-Review**: Versicherung, Kündigung, Kosten
- **Preisbindungs-Compliance-Checkliste** für Buchhandel

---

## Skill: `verlagsvertrag-redaktionsvertrag`

_Verlagsrecht: Hauptpflichten aus dem Verlagsvertrag, Rechteübertragung nach UrhG §§ 31 ff. und VerlG sowie Rückrufrechte nach VerlG §§ 7–8, UrhG §§ 41–42 systematisch prüfen im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Verl-002 · Verlagsvertrag: Hauptpflichten, Rechteübertragung, Rückruf

## Arbeitsbereich

Verlagsrecht: Hauptpflichten aus dem Verlagsvertrag, Rechteübertragung nach UrhG §§ 31 ff. und VerlG sowie Rückrufrechte nach VerlG §§ 7–8, UrhG §§ 41–42 systematisch prüfen. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

Analysiert den Verlagsvertrag nach seinen **synallagmatischen Hauptpflichten**: Manuskriptablieferung und Erscheinungspflicht (VerlG §§ 1–4), Rechteübertragung (UrhG §§ 31–44) sowie die wechselseitigen **Rückrufrechte** beider Seiten (VerlG §§ 7–8, UrhG §§ 41–42). Er bereitet den Sachverhalt für Vertragsreview, Verhandlung oder Streitbeilegung auf.

## Rechtsgrundlagen

| Norm | Regelungsgehalt | Quelle |
|------|----------------|--------|
| VerlG § 1 | Verlagsvertrag: gegenseitige Pflichten Verlag / Autor | https://www.gesetze-im-internet.de/verlg/__1.html |
| VerlG § 2 | Manuskriptablieferung: Form, Frist, Vollständigkeit | https://www.gesetze-im-internet.de/verlg/__2.html |
| VerlG § 5 | Erscheinungspflicht des Verlags: angemessene Frist | https://www.gesetze-im-internet.de/verlg/__5.html |
| VerlG § 7 | Rücktrittrecht des Autors bei Nichterscheinen | https://www.gesetze-im-internet.de/verlg/__7.html |
| VerlG § 8 | Gegenseitiger Rücktritt bei Verschulden | https://www.gesetze-im-internet.de/verlg/__8.html |
| UrhG § 31 | Einräumung von Nutzungsrechten | https://dejure.org/gesetze/UrhG/31.html |
| UrhG § 31a | Einräumung für unbekannte Nutzungsarten | https://dejure.org/gesetze/UrhG/31a.html |
| UrhG § 41 | Rückruf wegen Nichtausübung | https://dejure.org/gesetze/UrhG/41.html |
| UrhG § 42 | Rückruf wegen gewandelter Überzeugung | https://dejure.org/gesetze/UrhG/42.html |

## Prüfprogramm Hauptpflichten

### A. Autorenpflichten (§ 2 VerlG)

1. **Ablieferungspflicht**: Manuskript in vereinbarter Form (Dateiformat, Stil, Umfang), zum vereinbarten Termin.
2. **Vollständigkeit**: Alle Teile (Text, Register, Abbildungsvorlagen, Metadaten) müssen übergeben sein.
3. **Mängelfreiheit**: Keine Rechtsverletzungen Dritter (Plagiat, Persönlichkeitsrechte, Drittrechte an Fotos).
4. **Exklusivität**: Sofern vereinbart, kein Parallelvertrag mit anderem Verlag für dasselbe Werk.
5. **Mitwirkungspflichten**: Korrekturen, Druckfahnen, Registererstellung auf Aufforderung des Verlags.

### B. Verlagspflichten

1. **Erscheinungspflicht** (§ 5 VerlG): Erscheinen innerhalb angemessener, üblicherweise vertraglich bestimmter Frist nach Ablieferung.
2. **Verbreitungspflicht**: Aktiver Vertrieb, Aufnahme in den Buchhandel, Pflege der Lieferfähigkeit.
3. **Honorarpflicht**: Zahlung der vereinbarten Vergütung, Abrechnung (§§ 28 ff. VerlG, § 32 UrhG).
4. **Belegexemplare**: Übergabe von Freiexemplaren gemäß Vertrag.
5. **Pflege des Titels**: Keine willkürliche Einstellung der Lieferfähigkeit.

### C. Rechteübertragung

- **Umfang**: § 31 Abs. 5 UrhG — Zweckübertragungsregel: Im Zweifel nur die für den Vertragszweck erforderlichen Rechte.
- **Nutzungsartenspezifität**: Jede Nutzungsart (§ 15 UrhG: Vervielfältigung, Verbreitung, öffentliche Zugänglichmachung) ist einzeln zu benennen.
- **Unbekannte Nutzungsarten** (§ 31a UrhG): Widerrufsrecht des Autors binnen 3 Monaten nach Mitteilung der neuen Nutzungsart; Vergütungspflicht.
- **Ausschließliche vs. einfache Lizenz**: Ausschließliche Lizenz schließt Vergabe weiterer Lizenzen durch den Urheber aus.

## Rückrufrechte im Detail

### 1. VerlG § 7 — Rücktritt des Autors wegen Nichterscheinen
- Voraussetzung: Verlag erscheint das Werk nicht innerhalb angemessener Frist oder einer gesetzten Nachfrist.
- Rechtsfolge: Rücktritt vom Vertrag; Rechte fallen an Autor zurück; Vorschuss-Rückzahlung streitig (§ 346 BGB).
- Fristsetzen: Schriftlich, mit Androhung des Rücktritts, angemessene Frist (i.d.R. 3–6 Monate je nach Werktyp).

### 2. VerlG § 8 — Gegenseitiger Rücktritt bei Verschulden
- Autor liefert nicht → Verlag kann nach erfolgloser Fristsetzung zurücktreten, Schadensersatz verlangen.
- Verlag verletzt Erscheinungspflicht schuldhaft → Autor kann Rücktritt + Schadensersatz geltend machen.

### 3. UrhG § 41 — Rückruf wegen Nichtausübung
- Voraussetzung: Ausschließliches Nutzungsrecht; Verlag übt es nicht aus; Interessen des Urhebers erheblich beeinträchtigt.
- Sperrfrist: 2 Jahre nach Einräumung des Rechts oder – bei Pflichtwerken – 1 Jahr nach Ablieferung.
- Verfahren: Schriftliche Ankündigung → Ausübungsfrist 3 Monate → dann Rückruf.
- Rechtsfolge: Nutzungsrecht erlischt, Vergütungsanspruch bleibt (§ 41 Abs. 4 UrhG).

### 4. UrhG § 42 — Rückruf wegen gewandelter Überzeugung
- Voraussetzung: Dem Urheber ist das Festhalten am Werk aufgrund gewandelter Überzeugung nicht mehr zumutbar.
- Entschädigung: Angemessene Entschädigung des Verlags für Aufwendungen und entgangenen Gewinn.
- Rechtsfolge: Nutzungsrecht erlischt; bei gleicher Veröffentlichung später → Erstrecht des früheren Verlags.
- Fallgruppen: Politische Überzeugungsänderung, wissenschaftlicher Erkenntnisstand, Persönlichkeitsverletzung.

## Typische Fallen

- **Verschweigen von Fristsetzungsdefiziten**: § 7 VerlG-Rücktritt setzt ordnungsgemäße Nachfrist voraus; formfrei, aber klar und schriftlich ist Best Practice.
- **§ 41 UrhG-Sperrfrist wird vergessen**: Kein Rückruf in den ersten 2 Jahren möglich; Mandant muss warten.
- **Zweckübertragungsregel (§ 31 Abs. 5 UrhG) verkannt**: „Alle Rechte"-Klauseln übertragen nicht automatisch unbekannte Nutzungsarten.
- **Entschädigungspflicht bei § 42 UrhG unterschätzt**: Kann erheblich sein, wenn Verlag bereits in Produktion gegangen ist.
- **Gegenseitige Abhängigkeiten**: Autorenverzug und Verlagsverzug können sich gegenseitig aufheben; Beweislast sorgfältig prüfen.

## Checkliste für Vertragscheck

- [ ] Ablieferungsklausel enthält Format, Umfang, Frist
- [ ] Erscheinungsklausel enthält Deadline oder angemessene Frist
- [ ] Nutzungsarten einzeln aufgeführt (§ 31 Abs. 1 UrhG)
- [ ] Unbekannte Nutzungsarten-Klausel vorhanden (§ 31a UrhG)
- [ ] Rückrufbedingungen geregelt (Sperrfrist, Entschädigung)
- [ ] Honorar und Abrechnung vollständig geregelt (§§ 28 ff. VerlG)
- [ ] Belegexemplare-Klausel vorhanden

## Quellenreferenzen

- VerlG: https://www.gesetze-im-internet.de/verlg/
- UrhG §§ 31, 41, 42: https://dejure.org/gesetze/UrhG/41.html
- § 41 UrhG / Rückruf wegen Nichtausübung nicht mit ungeprüften Fundstellen blind belegen. Als frei prüfbarer Anker kommt BGH, Urteil vom 26.03.2009 - I ZR 153/06 (Reifen Progressiv) in Betracht; vor Ausgabe stets Sachverhalt, Datum, Aktenzeichen und Quelle live verifizieren.
- OLG Frankfurt, Urt. v. 04.11.2014 – 11 U 75/13 (Verlagsvertrag Erscheinungspflicht): https://openjur.de

## Output-Formate

- **Pflichtenprofil**: Tabelle Autor vs. Verlag mit Erfüllungsstatus
- **Rückruf-Ampel**: Voraussetzungen von §§ 41, 42 UrhG und VerlG §§ 7–8 geprüft
- **Fristenplan**: Ankündigungs- und Ausübungsfristen
- **Entwurf Rückrufschreiben**: Ankündigung nach § 41 UrhG oder Rücktritt nach § 7 VerlG
- **Rechteübertragungsmatrix**: Nutzungsarten mit Übertragungsstatus

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

