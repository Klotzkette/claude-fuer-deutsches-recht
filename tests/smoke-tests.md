# Smoke-Tests

Diese Datei beschreibt drei-Schritt-Szenarien, mit denen man die fachschweren Plugins schnell auf grundsätzliche Funktionsfähigkeit prüfen kann. Ein Smoke-Test bestätigt nicht die juristische Richtigkeit jeder Antwort — er stellt nur sicher, dass die Plugin-Skills den Eingangsdatenraum lesen, die richtigen Skills aufrufen und einen erwartbaren Output-Skelett liefern.

Vorgehen pro Test:

1. Das genannte Plugin laden (`/plugin load <plugin>` bzw. Auswahl im Plugin-Marketplace).
2. Den jeweils unter „Eingang" genannten Datenraum (i. d. R. eine der Testakten unter `testakten/`) als Arbeitsbereich öffnen.
3. Den Kaltstart-Skill des Plugins aufrufen, wie unter „Schritt 1" benannt.
4. Den im Test benannten Folgeskill anstoßen und prüfen, ob der „Erwartete Output" sichtbar wird.

Wenn der Output nicht erscheint oder der Skill abbricht: das Plugin ist nicht funktionsfähig, ein Bugfix muss her, kein Release.

---

## liquiditaetsplanung

**Eingang:** `testakten/fortbestehensprognose-paragrafix-gmbh/` (oder ein eigener BWA-Ordner mit drei Monatsabschlüssen).

**Schritt 1 — Kaltstart:** `/liquiditaetsplanung:liquiditaetsvorschau-3wochen` → liest BWAs/SuSa/Bankbelege, fragt nach Zielhorizont (13/26/52 Wochen) und Aggregations-Ebene.

**Schritt 2 — Plan bauen:** `/liquiditaetsplanung:liquiditaetsvorschau-3-6-12-monate` → ruft `werkzeuge/build_liquiditaetsplan.py` mit den extrahierten JSON-Plan-Keys.

**Erwarteter Output:** `liquiditaetsplan-<mandant>-<datum>.xlsx` mit allen Pflicht­zeilen (Bestand Start, Einnahmen, Ausgaben, Cash Flow Woche, Liquidität Woche Ende) und mindestens einem Bemerkungs-Sheet mit Liquiditätsquote / Annahmen.

**Abbruchkriterium:** XLSX wird nicht erzeugt **oder** Liquiditätsquoten-Formel fehlt **oder** Wochen-Summenzeilen rechnen nicht durch (alle Wochen-Summen müssen Formeln sein, keine Hardcodes).

---

## insolvenzrecht (Fortbestehensprognose)

**Eingang:** `testakten/fortbestehensprognose-paragrafix-gmbh/`.

**Schritt 1 — Kaltstart:** `/insolvenzrecht:insolvenzrecht-kaltstart-interview` → liest Jahresabschluss, ausstehende Forderungen, Bürgschaften, Sanierungsoptionen.

**Schritt 2 — Prognose:** `/insolvenzrecht:liquiditaetsvorschau-insolvenzrechtlich` → 13-Wochen-Plan und Fortbestehensprognose-Skizze.

**Erwarteter Output:** Liquiditätsplan-XLSX **und** ein Markdown-Memo zur Fortbestehensprognose mit den fünf BGH-Prüfpunkten (Zahlungs(un)fähigkeit nach IDW S 11, positive Fortführungsprognose, Maßnahmenkatalog, zeitlicher Horizont, Annahmen).

**Abbruchkriterium:** Memo enthält keine BGH-Zitierung mit Randnummer **oder** Liquiditätsplan endet im negativen Bestand ohne Maßnahmenkommentar.

---

## fluggastrechte

**Eingang:** `testakten/fluggastrechte-familie-braeutigam/`.

**Schritt 1 — Kaltstart:** `/fluggastrechte:fluggastrechte-kaltstart-interview` → erkennt Buchung, Annullierung, Anschlussflug, Passagieranzahl, Entfernung.

**Schritt 2 — Anspruch & Schreiben:** Skill für Ausgleichszahlung nach VO (EG) 261/2004.

**Erwarteter Output:** Schreiben an Airline mit korrektem Ausgleichsbetrag (250 / 400 / 600 €) je nach Streckenlänge, EuGH-Aktenzeichen im richtigen Format (`C-83/10`, `C-402/07`, nicht „2007/402"), Fristsetzung.

**Abbruchkriterium:** EuGH-Aktenzeichen im Schreiben falsch formatiert **oder** Ausgleichsbetrag passt nicht zur Streckenlänge.

---

## sozialrecht (Eingliederungshilfe)

**Eingang:** `testakten/sozialrecht-rollstuhl-tannenberg/`.

**Schritt 1 — Kaltstart:** `/sozialrecht-kanzlei:sozialrecht-kanzlei-kaltstart-interview` → liest Bescheid, ärztliche Stellungnahmen, Versorgungsvorschläge.

**Schritt 2 — Widerspruch:** Widerspruchsschrift gegen Kostenträger.

**Erwarteter Output:** Widerspruchsschrift mit Bezugnahme auf §§ SGB IX (insbesondere § 99 ff. SGB IX zur Eingliederungshilfe), Frist (1 Monat ab Bekanntgabe), Anträgen (1. Aufhebung, 2. Bewilligung, 3. Akteneinsicht).

**Abbruchkriterium:** Fristhinweis fehlt **oder** SGB-Norm-Zitate sind veraltet (Eingliederungshilfe ist seit BTHG 2020 in SGB IX, **nicht mehr** in SGB XII §§ 53 ff.).

---

## betreuungsrecht

**Eingang:** `testakten/betreuung-hildegard-sauer/`.

**Schritt 1 — Kaltstart:** `/betreuungsrecht:betreuungsrecht-kaltstart-interview` → erkennt Verfahrensart (Erstbestellung / Verlängerung / Aufgabenkreis-Erweiterung), Betroffene, Aufgabenkreise.

**Schritt 2 — Stellungnahme:** Betreuerstellungnahme nach § 1863 BGB n. F. (Stand BtOG-Reform 2023).

**Erwarteter Output:** Strukturierte Stellungnahme mit Aufgabenkreisen, Erforderlichkeitsprüfung, Wünschen des Betreuten, Einwilligungsvorbehalt-Vorschlag falls passend, Hinweis auf Vermögenssorge-Anlagenform.

**Abbruchkriterium:** Skill zitiert noch §§ 1896 ff. BGB **a. F.** statt §§ 1814 ff. BGB n. F. (Reform 01.01.2023).

**Zusatz-Eingang Kontodaten:** `testakten/betreuung-schmalfeld-kontodaten-vertraege/`.

**Zusatz-Schritt — Verdachtsprüfung:** `/betreuungsrecht:kontodaten-vertragsverdacht-pruefung` → liest Kontoauszüge, Vertragsregister und Verdachtsliste.

**Erwarteter Zusatz-Output:** Ampeltabelle mit akuten Treffern für angebliche Sicherheitskautionen, Fernwartung/Sicherheitssoftware, Auslandsanlage, Spanien-Reservierung und Windpark-Beteiligung; private Hilfezahlungen werden nur als belegbedürftig, nicht pauschal als Betrug eingeordnet.

**Zusatz-Abbruchkriterium:** Output behauptet ohne Beweis Betrug oder Geschäftsunfähigkeit **oder** behandelt Fernwartungszugriff nicht als eigenes Sofortschutzthema.

---

## berufsrecht-ki-vertragspruefung

**Eingang:** Eigener Mandantenvertrag (NDA, Werkvertrag, Dienstvertrag) als PDF.

**Schritt 1 — Kaltstart:** `/berufsrecht-ki-vertragspruefung:berufsrecht-ki-vertragspruefung-kaltstart-interview` → fragt nach Vertragsart, Parteien, Risikofokus.

**Schritt 2 — Gutachten:** `/berufsrecht-ki-vertragspruefung:gutachten-erstellen`.

**Erwarteter Output:** Gutachten-Skizze mit Hinweis auf Berufspflichten (insbesondere § 43e BRAO zum KI-Einsatz in der Anwaltskanzlei), Mandatsgeheimnis (§ 203 StGB), DSGVO-Risiken bei Datenexport an LLM-Provider.

**Abbruchkriterium:** Gutachten enthält keinen § 43e-BRAO-Hinweis **oder** behauptet pauschal, KI-Vertragsprüfung sei mit anwaltlicher Verschwiegenheit unvereinbar (sie ist es nicht, wenn die Datenflüsse korrekt gestaltet sind).

---

## einfache-leichte-sprache-jura

**Eingang:** `testakten/einfache-leichte-sprache-jura-mandantenbrief/`.

**Schritt 1 — Kaltstart:** `/einfache-leichte-sprache-jura:elsj-kommandocenter` → fragt Modus (Einfache Sprache oder Leichte Sprache), Zielgruppe, Medium und gewünschte Vollständigkeit ab.

**Schritt 2 — Übertragung:** `/einfache-leichte-sprache-jura:elsj-einfache-sprache` oder `/einfache-leichte-sprache-jura:elsj-leichte-sprache`.

**Erwarteter Output:** Verständliche Fassung mit sichtbarer Frist, erklärten Wörtern wie Bescheid, Widerspruch und Akteneinsicht, erhaltener Handlungsoption und juristischem Sicherungsvermerk.

**Abbruchkriterium:** Frist, Rechtsfolge oder Handlungsoption fehlen **oder** der Leichte-Sprache-Entwurf behauptet eine Nutzerprüfung, obwohl nur ein Entwurf erzeugt wurde.

---

## anlagen-zu-schriftsaetzen

**Eingang:** Ein Schriftsatz-Entwurf (PDF/DOCX) + Ordner mit 5–10 Anlagen in unterschiedlichen Formaten.

**Schritt 1 — Kaltstart:** `/anlagen-zu-schriftsaetzen:anlagen-zu-schriftsaetzen` → wählt Modus 1 (Auto-Benennung), 2 (Schriftsatz folgt) oder 3 (Prüfmodus).

**Schritt 2 — Konvolut bauen:** `python3 werkzeuge/build_anlagenkonvolut.py --eingang <ordner> --ausgang <ziel> --praefix K`.

**Erwarteter Output:** `Anlagenkonvolut.pdf` mit Lesezeichen pro Anlage, Stempel **Anlage K 7** in Arial 12 pt oben rechts auf Seite 1 jeder Anlage, `Anlagenverzeichnis.md` und `Anlagenverzeichnis.pdf`.

**Abbruchkriterium:** Stempel überlappt mit Seiteninhalt **oder** Lesezeichen springen auf die falsche Anlage **oder** Anlagenverzeichnis listet nicht alle Anlagen.

---

## forderungsmanagement-klagewerkstatt

**Eingang:** Eigener Forderungsfall (Rechnung, Mahnungen, Korrespondenz) oder `testakten/inkasso-zahlungsklage-modefuchs/`.

**Schritt 1 — Kaltstart:** `/forderungsmanagement-klagewerkstatt:klagevorlage-aus-eigenen-mustern` → erkennt Hauptforderung, Mahnverlauf, B2B/B2C-Konstellation.

**Schritt 2 — Verzugszinsen:** `python3 werkzeuge/verzugszins_rechner.py --forderung <eur> --beginn <datum> --art b2b`.

**Schritt 3 — Inkasso-Gate:** `/forderungsmanagement-klagewerkstatt:inkasso-zahlungsklage-ersteller` oder `python forderungsmanagement-klagewerkstatt/scripts/inkasso_claim_gate.py --input testakten/inkasso-zahlungsklage-modefuchs/08_claim_gate_input.json`.

**Erwarteter Output:** Aufstellung mit allen Basiszinsperioden zwischen Verzugsbeginn und Berechnungstag, taggenaue Zinsen, Endsumme. Beim ModeFuchs-Fall zusätzlich: Hauptforderung 698,00 EUR `ROT`, Nebenforderungen 99,84 EUR `GELB`, keine Klage über 797,84 EUR.

**Abbruchkriterium:** Aufschlag-Prozentpunkte falsch (B2B 9, B2C 5) **oder** Basiszins für eine Periode fehlt — dann ist die `BASISZINS`-Tabelle im Skript zu aktualisieren. Beim ModeFuchs-Fall: Hauptforderung wird trotz Zahlung als klagefähig ausgegeben.

---

## phishing-vorfall-pruefer

**Eingang:** `testakten/phishing-vorfall-mayer-sparkasse-berlin/`.

**Schritt 1 — Skill:** `/phishing-vorfall-pruefer:phishing-vorfall-pruefen` → erkennt Call-ID-Spoofing, pushTAN, streitige Autorisierung, § 675v-Bankeinwand, Banklogs und Ombudsmann-Quote.

**Schritt 2 — Gate:** `python phishing-vorfall-pruefer/scripts/phishing_case_gate.py --input testakten/phishing-vorfall-mayer-sparkasse-berlin/08_case_gate_input.json`.

**Erwarteter Output:** `damage_matches_transactions: true`, Erstattung dem Grunde `GRUEN`, grobe Fahrlässigkeit `GELB`, Bankpflichten/Monitoring `GRUEN`, Prozessfreigabe `GELB`. Der Fall darf nicht als sicherer Selbstläufer erscheinen.

**Abbruchkriterium:** Wenn das Plugin allein aus der TAN-Weitergabe automatisch "verloren" macht oder umgekehrt die grobe Fahrlässigkeit ausblendet.

---

## zwangsverwaltung-zvg (versteigerung)

**Eingang:** `testakten/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau/`.

**Schritt 1 — Portal:** `/zwangsverwaltung-zvg:zvg-portal-recherche` → übernimmt Suchparameter, Abrufdatum und Trefferzahl aus `01_zvg_portal_rechercheprotokoll.md`.

**Schritt 2 — Bieter:** `/zwangsverwaltung-zvg:zvg-bieterangebot-bewertung` → wertet Grundbuch, Gutachten, Mietnotiz und Angebot aus.

**Schritt 3 — Termin:** `/zwangsverwaltung-zvg:zvg-versteigerungsteilnahme` → erstellt Termincheck mit Sicherheitsleistung, geringstem Gebot, Bietlimit und roten Schwellen.

**Erwarteter Output:** Es wird klar zwischen umgangssprachlichem Mindestgebot und rechtlichem geringstem Gebot unterschieden. Bietlimit 525.000 EUR, Sicherheitsleistung 68.500 EUR und die Risiken Innenzustand, Nutzung, WEG/Sonderumlage und bestehenbleibende Rechte werden sichtbar.

**Abbruchkriterium:** Wenn das Plugin das geringste Gebot als wirtschaftliches Maximalgebot behandelt, Sicherheitsleistung vergisst oder die fiktive Portalakte als echten Treffer ausgibt.

---

## kanzlei-cowork (rechnungserstellung-rvg)

**Eingang:** Mandatsdatenraum mit Streitwert, Tätigkeitsbeschreibung, Auslagen.

**Schritt 1 — Kaltstart:** `/kanzlei-cowork:kanzlei-cowork-kaltstart-interview`.

**Schritt 2 — Rechnung & Plausibilisieren:** `python3 werkzeuge/rvg_gebuehrenrechner.py --wert 25000 --faktor 1.3` zum schnellen Quercheck.

**Erwarteter Output:** Netto / USt. / Brutto in deutscher Zahlenschreibweise (Komma als Dezimaltrenner). Bei Streitwert 25.000 € und Faktor 1,3: einfache Gebühr 874,00 €, gewichtet 1.136,20 €, mit Pauschale 1.156,20 € netto.

**Abbruchkriterium:** Einfache Gebühr stimmt nicht mit RVG Anlage 2 überein **oder** Pauschale Nr. 7002 überschreitet 20 €.

---

## Hinweis zur Nutzung

Diese Smoke-Tests sind absichtlich kurz. Sie ersetzen keine fachliche Prüfung, sondern dienen vor jedem Release als „Geht der Skill überhaupt los?"-Kontrolle. Wer einen Skill substantiell ändert, sollte den entsprechenden Smoke-Test einmal durchspielen.
