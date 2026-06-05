---
name: mieterhoehung-widersprechen
description: "Mieterhoehung Widersprechen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mieterhoehung Widersprechen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mieterhoehung Widersprechen** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. Prüfroutine deckt Textform Wartefrist Kappungsgrenze (zwanzig Prozent oder fuenfzehn Prozent in Spannungsgebieten) und Begründungsmittel (Mietspiegel Sachverständigengutachten Vergleichswohnungen) ab. Erzeugt Entwurf mit Disclaimer. |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen). Prüfroutine deckt Textform Wartefrist (fuenfzehn Monate seit Einzug oder letzter Erhoehung) Kappungsgrenze (zwanzig Prozent oder fuenfzehn Prozent in Spannungsgebieten) Zustimmungsfrist (zwei Monate plus Ablauf des Kalendermonats) und Begründungsmittel ab. Spiegelt den Prüf-Skill `mieterhoehung-prüfen-widersprechen` aus der Mietersicht. Erzeugt fertiges Schreiben mit Disclaimer. |
| `mietkaution-rueckforderung` | Prüffeld für mietkaution rueckforderung: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **Mieterhoehung Widersprechen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mieterhoehung-pruefen-widersprechen`

**Fokus:** Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. Prüfroutine deckt Textform Wartefrist Kappungsgrenze (zwanzig Prozent oder fuenfzehn Prozent in Spannungsgebieten) und Begründungsmittel (Mietspiegel Sachverständigengutachten Vergleichswohnungen) ab. Erzeugt Entwurf mit Disclaimer.

# Mieterhöhung prüfen und widersprechen

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieterhöhung prüfen und widersprechen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Disclaimer (Schlüsselstelle)

Diese Prüfung und der nachstehende Entwurf ersetzen **keine Rechtsberatung**. Vor Versand des Schreibens an den Vermieter ist eine anwaltliche oder mietervereinsseitige Kontrolle dringend zu empfehlen. Fristversäumnisse führen zu gesetzlicher Zustimmung nach § 558b Abs. 2 BGB.

## Workflow

### Schritt 1 — Daten beschaffen

- Mieterhöhungsverlangen im Wortlaut.
- Datum des Zugangs (Briefkasten-Eintrag, E-Mail-Empfang).
- Lage- und Ausstattungsprotokoll aus dem Skill `lage-und-ausstattung-erheben`.
- Auszug aus dem aktuellen amtlichen Mietspiegel der Stadt aus `references/mietspiegel-quellen.md`.

### Schritt 2 — Formprüfung

- **Textform** nach § 558a Abs. 1 BGB (Brief, Fax, E-Mail mit Unterschriftstext genügen).
- **Empfängerangabe** alle Mieter namentlich.
- **Begründung** auf Mietspiegel, Sachverständigengutachten oder drei Vergleichswohnungen gestützt (§ 558a Abs. 2 BGB).
- **Beilage** falls Mietspiegelauszug, dann gut lesbar.

### Schritt 3 — Wartefrist und Sperrjahr

- Die neue Miete darf frühestens **fünfzehn Monate** nach Einzug oder nach der letzten Erhöhung verlangt werden (§ 558 Abs. 1 BGB).
- Berechnung dokumentieren.

### Schritt 4 — Kappungsgrenze (§ 558 Abs. 3 BGB)

- Regelgrenze **zwanzig Prozent** in drei Jahren.
- In Gebieten der Kappungsgrenzenverordnung **fünfzehn Prozent** in drei Jahren — Prüfung anhand der Landesverordnung (siehe `references/mietspiegel-quellen.md`).

### Schritt 5 — Materielle Prüfung der ortsüblichen Vergleichsmiete

- Wohnlage einordnen.
- Spanne im qualifizierten Mietspiegel suchen.
- Einordnung innerhalb der Spanne nach Orientierungshilfe (Auf- und Abschlaege für Ausstattungsmerkmale).
- Vergleichsmiete je m² ermitteln, mit Wohnfläche multiplizieren.

### Schritt 6 — Reaktionsfristen

- **Zustimmungsfrist** § 558b Abs. 2 BGB. Ablauf des zweiten Kalendermonats nach Zugang.
- Bei Schweigen: Vermieter kann auf Zustimmung klagen (§ 558b Abs. 2 Satz 2 BGB).

### Schritt 7 — Entwurfsoptionen

- **Volle Zustimmung** wenn Begehren formal und materiell richtig ist.
- **Teilzustimmung** bis zur tatsächlich ortsüblichen Vergleichsmiete.
- **Verweigerung** bei Formfehlern, Verstoß gegen Wartefrist oder Kappungsgrenze.

## Schreiben-Entwurf

Erzeuge ein höflich-bestimmtes Schreiben mit:

1. Bezugnahme auf das Verlangen vom (Datum).
2. Rechtliche Prüfung punktweise (Form, Frist, Kappungsgrenze, ortsübliche Vergleichsmiete).
3. Eindeutige Erklärung (Zustimmung, Teilzustimmung, Verweigerung).
4. Aufforderung zur schriftlichen Bestätigung.
5. **Disclaimer am Ende** — Hinweis, dass dies kein anwaltliches Schreiben ist und der Mieter sich beraten lassen sollte.

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- **BGH 28.04.2021, VIII ZR 22/20**: Qualifizierter Mietspiegel (§ 558d BGB) — Anforderungen an wissenschaftliche Erstellung; Vermutungswirkung nur bei substantiierter Erschuetterung des Erstellungsverfahrens (z. B. methodische Maengel) entkraeftbar. Quelle: dejure.org/2021,15412.
- **BGH 21.11.2012, VIII ZR 46/12**: Wirksamkeit des Mieterhoehungsverlangens; Mietspiegelauszug muss beigefuegt sein, wenn das Verlangen darauf gestuetzt wird; sonst formal unwirksam. Quelle: dejure.org/2012,38221.
- **BGH 18.10.2017, VIII ZR 28/17**: Mieterhoehung auf Grundlage Sachverstaendigengutachten — Gutachten muss konkrete Vergleichswohnungen heranziehen, nicht nur Pauschalmietspiegel-Daten. Quelle: dejure.org/2017,40850.
- **BVerfG 25.03.2021, 2 BvF 1/20** (Berliner Mietendeckel-Beschluss): Landesrechtlicher Mietendeckel verfassungswidrig (Bundesrecht abschliessend; §§ 556d ff. BGB Bundeskompetenz). Quelle: bundesverfassungsgericht.de / dejure.org/2021,7050.
- **Gesetzeslage 2026:** Mietpreisbremse § 556d BGB durch Bundesgesetzgeber verlaengert; konkrete Geltungsdauer und Spannungs-Gebiets-Verordnungen der Laender vor Versand pruefen.

Vor Zitieren weiterer Aktenzeichen Live-Verifikation per dejure.org / bundesgerichtshof.de.

## Paragrafenkette

§§ 558, 558a, 558b, 558c, 558d BGB

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `mieterhoehungsverlangen-erstellen`

**Fokus:** Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen). Prüfroutine deckt Textform Wartefrist (fuenfzehn Monate seit Einzug oder letzter Erhoehung) Kappungsgrenze (zwanzig Prozent oder fuenfzehn Prozent in Spannungsgebieten) Zustimmungsfrist (zwei Monate plus Ablauf des Kalendermonats) und Begründungsmittel ab. Spiegelt den Prüf-Skill `mieterhoehung-prüfen-widersprechen` aus der Mietersicht. Erzeugt fertiges Schreiben mit Disclaimer.

# Mieterhöhungsverlangen erstellen (Vermieter / Hausverwaltung)

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieterhöhungsverlangen erstellen (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Disclaimer (Schlüsselstelle)

Ein formal oder materiell fehlerhaftes Mieterhöhungsverlangen ist unwirksam — der Mieter darf zustimmen verweigern. Wer die Wartefrist oder die Kappungsgrenze verletzt verliert das Verlangen ganz. Vor Versand großer Mieterhöhungen oder bei zweifelhafter Mietspiegel-Einordnung ist eine fachanwaltliche Prüfung dringend empfohlen.

## Workflow

### Schritt 1 — Daten zusammenstellen

- Aktueller Mietvertrag mit Vertragsdatum.
- Bisherige Nettokaltmiete und Datum der letzten Erhöhung.
- Lage- und Ausstattungsprotokoll aus dem Skill `lage-und-ausstattung-erheben`.
- Auszug aus dem aktuellen amtlichen Mietspiegel der Stadt aus `references/mietspiegel-quellen.md`.
- Bei Begründung durch Vergleichswohnungen: drei konkrete Wohnungen mit Adresse Ausstattung und Höhe der Miete.

### Schritt 2 — Wartefrist (§ 558 Abs. 1 BGB)

- Die neue Miete darf frühestens **fünfzehn Monate** nach Einzug oder nach Wirksamwerden der letzten Erhöhung verlangt werden.
- Berechnung dokumentieren — sonst Risiko der Unwirksamkeit.

### Schritt 3 — Kappungsgrenze (§ 558 Abs. 3 BGB)

- Regelgrenze **zwanzig Prozent** in drei Jahren.
- In Gebieten der Kappungsgrenzenverordnung **fünfzehn Prozent** in drei Jahren (siehe `references/mietspiegel-quellen.md`).
- Berechnung der gesamten Erhöhung gegenüber der vor drei Jahren geschuldeten Miete dokumentieren.

### Schritt 4 — Materielle Begründung

- Ortsübliche Vergleichsmiete aus dem qualifizierten Mietspiegel ermitteln (Spanne + Orientierungshilfe).
- Einordnung der konkreten Wohnung innerhalb der Spanne nachvollziehbar darstellen.
- Wenn kein qualifizierter Mietspiegel vorliegt: einfacher Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen.

### Schritt 5 — Formale Anforderungen (§ 558a BGB)

- **Textform** ausreichend (Brief Fax E-Mail mit Unterschriftstext).
- **Adressierung** alle im Mietvertrag genannten Mieter namentlich.
- **Erklärung** der Vermieter verlangt Zustimmung zur Erhöhung auf einen konkreten neuen Betrag ab einem konkreten Termin.
- **Begründung** mit Verweis auf Mietspiegel Gutachten oder Vergleichswohnungen.
- **Beilagen** Mietspiegelauszug gut lesbar oder Gutachten als Kopie oder Vergleichswohnungen-Aufstellung.

### Schritt 6 — Wirkungszeitpunkt und Zustimmungsfrist

- Wirksame Erhöhung erfolgt erst mit **Beginn des dritten Kalendermonats nach Zugang** des Verlangens (§ 558b Abs. 1 BGB).
- Mieter hat **Zustimmungsfrist** bis zum Ablauf des zweiten Kalendermonats nach Zugang (§ 558b Abs. 2 BGB).
- Bei Schweigen oder Verweigerung kann Klage auf Zustimmung erhoben werden — Klagefrist drei Monate nach Ablauf der Zustimmungsfrist.

### Schritt 7 — Prüfroutine vor Versand

- Wartefrist fünfzehn Monate erfüllt.
- Kappungsgrenze eingehalten.
- Mietspiegel oder Gutachten oder drei Vergleichswohnungen als Begründung beigefügt.
- Alle Mieter namentlich adressiert.
- Wirksamkeitstermin korrekt berechnet (Beginn des dritten Kalendermonats nach Zugang).
- Bei Mietpreisbremse-Gebiet prüfen ob die neue Miete nach Erhöhung noch innerhalb der Vergleichsmiete plus zehn Prozent liegt.

## Schreiben-Entwurf

Erzeuge ein Schreiben mit:

1. Adresse aller Mieter namentlich.
2. Bezugnahme auf den Mietvertrag (Datum Mietsache).
3. Bisherige Miete und neue Miete in Euro mit Wirksamkeitstermin.
4. Begründung mit Bezug auf den amtlichen Mietspiegel (Stadt Jahr Spaltennummer) oder Gutachten oder Vergleichswohnungen.
5. Berechnung der ortsüblichen Vergleichsmiete und Einordnung der konkreten Wohnung.
6. Nachweis Wartefrist und Kappungsgrenze.
7. Hinweis auf Zustimmungsfrist nach § 558b Abs. 2 BGB.
8. **Disclaimer** — Hinweis dass dies ein Vermieter-Verlangen ist und der Mieter sich beraten lassen kann.

## Hinweis zur Mietpreisbremse

In Gebieten mit Mietpreisbremse darf eine Erhöhung bei bestehendem Mietverhältnis grundsaetzlich erfolgen — die Mietpreisbremse begrenzt nur die Neuvermietung. Aber: bei Neuvermietung ist eine Miete über ortsübliche Vergleichsmiete plus zehn Prozent unzulässig (§ 556d BGB). Bei Folgeerhöhungen im laufenden Verhältnis gilt nur die Kappungsgrenze.

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- **Berliner Mietendeckel nicht als BGH-Mietrecht zitieren:** Die Kompetenzfrage wurde durch BVerfG, Beschluss vom 25.03.2021 - 2 BvF 1/20, entschieden. Für Mietpreisbremse/Rückzahlung nach §§ 556d ff. BGB immer eine gesondert verifizierte BGH-Entscheidung mit Datum und Aktenzeichen heranziehen.
- **BVerfG 25.03.2021, 2 BvF 1/20, 2 BvL 4/20, 2 BvL 5/20** (Berliner Mietendeckel-Beschluss): Landesrechtlicher Mietendeckel (Berlin) ist mangels Gesetzgebungskompetenz des Landes verfassungswidrig (Bundesrecht abschliessend). Quelle: bundesverfassungsgericht.de / dejure.org/2021,7050.
- **BGH 28.04.2021, VIII ZR 22/20**: Qualifizierter Mietspiegel — Anforderungen an wissenschaftliche Erstellung; Erschuetterung der Vermutungswirkung nur bei substantiierten Maengeln des Mietspiegel-Erstellungsverfahrens. Quelle: dejure.org/2021,15412.
- **BGH 18.03.2020, VIII ZR 64/19** (Bauwerksmaengel als Mietminderungsgrund — vor Mieterhoehungsausgleich pruefen): Erhebliche Maengel mindern auch die Bezugsbasis der Vergleichsmiete. Quelle: dejure.org/2020,4895.
- **Gesetzeslage Mai 2026:** Bei Erstellung Stand der Mietpreisbremsen-Verordnungen der Laender pruefen; Kappungsgrenzenverordnungen je Bundesland; § 556d BGB-Verlaengerung durch Bundesgesetzgeber (Beschluss 2025 — vor Ausgabe Bundesgesetzblatt-Verifikation).

Vor Zitieren weiterer Entscheidungen Live-Verifikation per dejure.org / bundesgerichtshof.de mit Datum und Aktenzeichen.

## Paragrafenkette

§§ 558, 558a, 558b BGB — Begruendungsmittel, Wartefrist, Kappungsgrenze

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `mietkaution-rueckforderung`

**Fokus:** Prüffeld für mietkaution rueckforderung: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Mietkaution-Rückforderung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietkaution-Rückforderung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Nach Auszug aus der Wohnung ist die Rückforderung der Mietkaution ein häufiges Streitthema. Strukturierte Bearbeitung des Mieter-Anspruchs.

## Eingaben

- Mietvertrag mit Kautions-Vereinbarung
- Kautions-Höhe und Nachweis Bareinzahlung
- Auszugs-Datum
- Übergabe-Protokoll
- Letzter Betriebskosten-Abrechnungs-Stand
- Bisheriger Schriftwechsel
- Bei Anlage: Bank-Nachweis Anlage

## Schritt 1 — Höchstgrenze § 551 BGB

- **Maximal drei Monatsmieten netto kalt**
- Bei überhöhter Kaution Rückforderungs-Anspruch des Überschusses
- **BGH 30.06.2004, VIII ZR 243/03**: Begrenzung § 551 Abs. 1 BGB auf 3 Monatsmieten netto-kalt; Ueberschreitung partial unwirksam (dejure.org/2004,2143).

## Schritt 2 — Anlage-Pflicht § 551 Abs. 3 BGB

### Vermieter-Pflicht

- **Insolvenzgesichert getrennt vom eigenen Vermögen**
- **Übliche Verzinsung** (Spar-Konto-Zinssatz)
- **Erträge** stehen dem Mieter zu
- **Banken-Konto** typisch — gesondertes "Mietkauto-Konto"

### Verstoß-Folge

- Mieter-Anspruch auf vorzeitige Rückforderung
- Schadensersatz wegen Pflichtverletzung
- **BGH 09.06.2010, VIII ZR 189/09**: Insolvenzgesicherte Anlage als Schutzzweck § 551 Abs. 3 BGB; bei Pflichtverletzung Schadensersatzanspruch (dejure.org/2010,11320).

## Schritt 3 — Abrechnungs-Pflicht des Vermieters

### Angemessene Frist

- **BGH 18.01.2006, VIII ZR 71/05**: Abrechnungsfrist nach Mietende ueblicherweise sechs Monate; konkrete Hoechstdauer einzelfallabhaengig (dejure.org/2006,484).
- Bei längerer Frist Recht-fertigungsbedarf des Vermieters
- Bei kurzfristigen Konstellationen drei Monate

### Inhalt der Abrechnung

- Auflistung Mängel-Beseitigungs-Kosten
- Offene Mietforderungen
- Betriebskosten-Saldo
- Zinsen auf Kaution
- Verbleibender Betrag zur Rückzahlung

## Schritt 4 — Einbehalts-Voraussetzungen

### Offene Mietforderungen

- Rückständige Mieten
- Mietminderungs-Streit
- Verzinsung

### Schaden an der Wohnung

- **Nicht** für gewöhnliche Abnutzung
- **Schadensersatz** für übermäßige Abnutzung § 538 BGB iVm § 280 BGB

### Nachzahlung Betriebskosten

- **Sicherheits-Einbehalt** zulässig bis Abrechnung der laufenden Periode
- **BGH 18.01.2006, VIII ZR 71/05**: Vermieter darf Teil der Kaution bis zur naechsten Betriebskostenabrechnung einbehalten, wenn Nachforderung zu erwarten (dejure.org/2006,484).

### Schönheitsreparaturen

- **Wirksamkeit der Klausel** prüfen — viele Klauseln unwirksam
- **BGH 18.03.2015, VIII ZR 185/14** (Aufgabe der „starren" Fristenplaene): Klauseln, die Schoenheitsreparaturen-Pflicht ohne Beruecksichtigung des konkreten Verschleisses vorschreiben, sind unwirksam (dejure.org/2015,4682).
- **BGH 22.08.2018, VIII ZR 277/16**: Schoenheitsreparaturen-Klausel bei unrenoviert uebernommener Wohnung — § 538 BGB; ohne Ausgleich unwirksam (dejure.org/2018,21586).

## Schritt 5 — Forderungs-Schreiben

```
[Briefkopf Mieter]

[Datum]

An [Vermieter mit Adresse]

Per Einschreiben

Mietkaution für [Anschrift Mietsache]
Rückforderung der Kaution

Sehr geehrte Damen und Herren,

ich bin am [Auszugsdatum] aus der oben genannten Wohnung
ausgezogen. Die Übergabe ist gemäß Protokoll vom [Datum]
ohne Beanstandungen erfolgt.

Eine Kautions-Abrechnung haben Sie mir bislang nicht
vorgelegt. Die angemessene Abrechnungs-Frist von sechs
Monaten ist mittlerweile abgelaufen.

Ich fordere Sie auf, die Kaution in Höhe von EUR [Betrag]
zzgl. der zugehörigen Zinsen bis zum [Frist + zwei Wochen]
an mich zurückzuzahlen.

Konto: [Bankverbindung]

Sollte die Zahlung nicht erfolgen, behalte ich mir
gerichtliche Schritte vor — einschließlich Forderung
der Anwaltskosten gem. § 286 BGB.

Mit freundlichen Grüßen
```

## Schritt 6 — Mahnverfahren

### Vorteil

- Schnell und kostengünstig
- Mahnbescheid bei AG zentralisiert
- Bei Widerspruch des Vermieters Übergang in streitiges Verfahren

### Streitwert

- Bezifferte Forderung Kaution plus Zinsen plus Anwaltskosten

## Schritt 7 — Klageverfahren

### Sachlich

- AG bei Wohnraum-Mietsache § 23 Nr. 2 a) GVG ausschließlich

### Örtlich

- AG des Belegenheits-Orts § 29a ZPO

### Beweislast

- **Mieter** beweist Auszug und Kautions-Zahlung
- **Vermieter** beweist Einbehalts-Berechtigung (Schaden Forderung)

## Schritt 8 — Verjährung

- **Drei Jahre** § 195 BGB
- Ab Schluss des Jahres in dem Anspruch entstanden und Mieter Kenntnis hat (Auszug)
- Verlängerung über Mahnverfahren etc.

## Schritt 9 — Spezielle Konstellationen

### Bankbürgschaft als Kaution

- Anspruch auf Rückgabe der Bürgschaftsurkunde
- Vermieter darf nur bei festgestelltem Anspruch ziehen

### Sparbuch verpfändet

- Pfandfreigabe nach Abrechnung

### Wechsel des Eigentümers während Mietzeit

- Kautions-Verwaltung wechselt auf Erwerber § 566a BGB
- Erwerber haftet
- Veräußerer haftet subsidiär § 566a Satz 2 BGB

### Sonderfälle Tod Insolvenz Vermieter

- Bei Insolvenz Vermieter — Kaution insolvenzgeschützt durch separate Anlage
- Bei Verstoß Vermieters: Schadensersatz Vermögensmischung

## Schritt 10 — Sonderfall Gewerbe-Miete

- § 551 BGB **nicht** anwendbar
- Vertragliche Vereinbarung gilt
- AGB-Kontrolle Klausel
- BGH 19.06.2013, XII ZR 137/12 (Gewerbemiete, Buergschaft als Kaution; § 307 BGB-Kontrolle; dejure.org/2013,13420).

## Schritt 11 — Strategie

### Pro Mieter

- Schadensbild prüfen vor Übergabe
- Übergabe-Protokoll fördern (Foto-Dokumentation)
- Mietvertrags-Klauseln prüfen (Schönheitsreparaturen Renovierung Klausel oft unwirksam)
- Mängel-Anzeigen während Mietzeit gewahrt?

### Vermieter-Sicht (Verteidigung)

- Übergabe-Protokoll mit konkreten Mängel-Befunden
- Sachverständigen-Gutachten bei Schaden
- Belege zu Kosten

## Schritt 12 — Beweissicherung Mieter

- **Übergabe-Protokoll** mit Fotos
- **Kautions-Quittung** Originaleinzahlung
- **Mängel-Anzeigen** im Mietverlauf
- **Schadens-Fotos** vor und nach
- **Schlüssel-Rückgabe-Quittung**

## Ausgabe

- `kaution-rueckforderung-{az}.md`
- Forderungs-Schreiben Vorlage
- Mahnbescheid-Vorbereitung
- Klage-Erstentwurf
- Frist im Fristenbuch (Verjährung drei Jahre)
- Streitwert-Schätzung

## Quellen

- BGB §§ 538 280 286 551 566a
- ZPO §§ 29a 689 ff. (Mahnverfahren)
- GVG § 23
- BGH VIII. Zivilsenat nur mit Datum, Aktenzeichen und frei prüfbarer Quelle

---

## Audit-Hinweis

**Datum:** 27.05.2026

Bei diesem Skill wurden drei halluzinierte BGH-Aktenzeichen entfernt oder ersetzt:
