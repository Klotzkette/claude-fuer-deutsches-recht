---
name: mahnbescheid-fristennotiz-zv-titel-zv
description: "Mahnbescheid Fristennotiz ZV Titel ZV: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mahnbescheid Fristennotiz ZV Titel ZV

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mahnbescheid Fristennotiz ZV Titel ZV** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-mahnbescheid-fristennotiz-und-naechster-schritt` | Mahnbescheid: Fristennotiz und nächster Schritt im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `zv-titel-klausel-zustellung` | Gläubiger hat Urteil oder sonstigen Titel und prüft vor Vollstreckungsbeginn die drei formalen Voraussetzungen. §§ 704 724 750 ZPO Titel Klausel Zustellung. Prüfraster: vollstreckbarer Titel Vollstreckungsklausel Urkundsbeamter/Notar/Insolvenzgericht Klauselumschreibung §§ 727 ff. qualifizierte Klausel bei bedingten Titeln Wartefrist § 750 Abs. 1. Output: Drei-Saeulen-Prüfprotokoll und Handlungsempfehlung. Abgrenzung zu zv-kommandocenter (Routing) und zv-mahnbescheid-online (Titelerlangung). |
| `zv-kontensuche-drittschuldner` | Gläubiger hat Urteil aber kein bekanntes Konto oder Arbeitgeber des Schuldners. § 802l ZPO Drittauskunfte. Prüfraster: Rentenversicherung Bund Bundeszentralamt für Steuern Kontenabruf Kraftfahrt-Bundesamt Schuldnerverzeichnis § 882b ZPO. Output: Drittsauskunfts-Antrag und Auswertungs-Protokoll. Abgrenzung zu zv-vermögensauskunft-gv (Gläubigerantrag auf EV durch GV) und zv-pfueb-bank (nach Kontoermittlung). |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **Mahnbescheid Fristennotiz ZV Titel ZV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-mahnbescheid-fristennotiz-und-naechster-schritt`

**Fokus:** Mahnbescheid: Fristennotiz und nächster Schritt im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Mahnbescheid: Fristennotiz und nächster Schritt

## Spezialwissen: Mahnbescheid: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Mahnbescheid: Fristennotiz und nächster Schritt / mahnbescheid fristennotiz und naechster schritt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Mahnbescheid** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `zv-titel-klausel-zustellung`

**Fokus:** Gläubiger hat Urteil oder sonstigen Titel und prüft vor Vollstreckungsbeginn die drei formalen Voraussetzungen. §§ 704 724 750 ZPO Titel Klausel Zustellung. Prüfraster: vollstreckbarer Titel Vollstreckungsklausel Urkundsbeamter/Notar/Insolvenzgericht Klauselumschreibung §§ 727 ff. qualifizierte Klausel bei bedingten Titeln Wartefrist § 750 Abs. 1. Output: Drei-Saeulen-Prüfprotokoll und Handlungsempfehlung. Abgrenzung zu zv-kommandocenter (Routing) und zv-mahnbescheid-online (Titelerlangung).

# Drei-Säulen-Prüfung: Titel, Klausel, Zustellung

## Fachkern: Drei-Säulen-Prüfung: Titel, Klausel, Zustellung

- **Spezialfrage (Drei-Säulen-Prüfung: Titel, Klausel, Zustellung):** vollstreckbarer Titel Vollstreckungsklausel Urkundsbeamter/Notar/Insolvenzgericht Klauselumschreibung §§ 727 ff. qualifizierte Klausel bei bedingten Titeln Wartefrist § 750 Abs. 1. Output: Drei-Saeulen-Prüfprotokoll und Handlungsempfehlung. Abgrenzung zu zv-kommandocenter (Routing) und zv-mahnbescheid-online (Titelerlangung).
- **Prüfzugriff:** Sachverhalt, Norm, Zugang/Form/Frist oder Anspruchsvoraussetzung zuerst klären; Rechtsprechung erst danach als verifizierten Beleg nutzen.


## Aufgabe

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtsgrundlagen

- **§ 704 ZPO** – Vollstreckungstitel: rechtskräftige oder vorläufig vollstreckbare Endurteile.
- **§ 794 ZPO** – sonstige Vollstreckungstitel: Vergleiche, Kostenfestsetzungsbeschlüsse, notarielle Urkunden mit Unterwerfung (Abs. 1 Nr. 5), Schiedssprüche (Nr. 4a), europäische Vollstreckungstitel.
- **§ 724 ZPO** – vollstreckbare Ausfertigung mit Klauselvermerk: "Vorstehende Ausfertigung wird dem ... zum Zwecke der Zwangsvollstreckung erteilt".
- **§ 725 ZPO** – einfache Klausel: erteilt durch Urkundsbeamten der Geschäftsstelle.
- **§§ 726, 730 ZPO** – qualifizierte Klausel: bei bedingtem Titel, Zug-um-Zug-Verurteilung, Sicherheitsleistung; Erteilung durch Rechtspfleger nach Beweis der Bedingung.
- **§§ 727, 729 ZPO** – titelumschreibende Klausel: bei Rechtsnachfolge auf Gläubiger- oder Schuldnerseite (Erbe, Abtretung, Insolvenzanfechtung).
- **§ 732 ZPO** – Erinnerung gegen Klauselerteilung (vom Schuldner gegen den Gläubiger).
- **§ 768 ZPO** – Klauselgegenklage: materielle Einwendungen gegen die Klauselvoraussetzung.
- **§ 750 ZPO** – Zustellung des Titels (mit Klausel) an den Schuldner vor Beginn der Vollstreckung; bei Klauseln nach §§ 726 ff. ZPO zusätzlich die ihre Erteilung bestätigenden Urkunden, sowie Wartefrist von 2 Wochen (§ 750 Abs. 2 ZPO).
- **§ 798 ZPO** – Zustellung von Vollstreckungsbescheid, Kostenfestsetzungsbeschluss und Schiedsspruch von Amts wegen.

### Sondertitel ohne klassische Klausel

- **Vollstreckungsbescheid** § 796 Abs. 1 ZPO – Klausel von Gesetzes wegen ("Klausel kraft Gesetzes"); keine gesonderte Klausel nötig.
- **Tabellenauszug nach § 201 InsO** – wirkt wie rechtskräftiges Urteil; vollstreckbare Ausfertigung wird durch das Insolvenzgericht erteilt.
- **Versäumnisurteil** – sofort vollstreckbar, aber nur gegen Sicherheitsleistung § 708 Nr. 2 ZPO.
- **Europäischer Vollstreckungstitel (EuVTVO)** – Klausel des Ursprungsgerichts genügt; keine Vollstreckbarerklärung in Deutschland.

## Workflow

1. **Titel sichten**: Original, Ausfertigung oder Abschrift? Nur Ausfertigung ist tauglich.
2. **Klausel suchen**: Auf der Rückseite des Titels oder als gesonderter Vermerk. Klauselformel: "Vorstehende Ausfertigung wird dem [Gläubiger] zum Zwecke der Zwangsvollstreckung erteilt. [Ort], [Datum], [Unterschrift Urkundsbeamter/Rechtspfleger/Notar]".
3. **Klausel beschaffen**, wenn sie fehlt:
 - Bei Gerichtsurteilen: Antrag an Urkundsbeamten der Geschäftsstelle des ausgangs Gerichts § 725 ZPO.
 - Bei notariellen Urkunden: Antrag an den Notar selbst § 797 Abs. 2 ZPO.
 - Bei Vollstreckungsbescheid: keine gesonderte Klausel nötig.
 - Bei qualifizierter Klausel (§§ 726, 730 ZPO): Antrag an Rechtspfleger mit Beweis der Bedingung (Urkundenbeweis oder öffentliche Urkunde).
 - Bei Rechtsnachfolge (§§ 727 ff. ZPO): Erbschein, Abtretungsurkunde, Insolvenzgerichtsbeschluss als Beweismittel.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **Wartefrist beachten**: bei qualifizierter Klausel 2 Wochen ab Zustellung § 750 Abs. 2 ZPO.
6. **Ampel setzen**: Säulen grün → weiter; Säulen gelb/rot → fehlende Säule beschaffen, dann erneut prüfen.

## Typische Fehlerquellen

- **Klausel fehlt** – Anwalt versucht zu vollstrecken aus einfacher Urteilsabschrift. Klausel binnen 1-2 Werktagen beim ausgangs Gericht zu holen.
- **Falscher Adressat** – Klausel auf "Gläubiger" lautet, der Anspruch wurde abgetreten. Umschreibung nach § 727 ZPO nötig.
- **Zustellung an Schuldner vergessen** – häufig bei Sicherungsmaßnahmen. § 750 ZPO ist Vollstreckungsvoraussetzung, nicht heilbar durch nachträgliche Zustellung (str.; sicherster Weg: erneute Maßnahme nach erfolgter Zustellung).
- **Klausel zwar erteilt, aber nicht zugestellt** – die qualifizierte Klausel mit den Bedingungs-Beweisurkunden muss dem Schuldner ebenfalls zugestellt werden § 750 Abs. 2 ZPO.
- **Sicherheitsleistung** bei vorläufig vollstreckbarem Urteil – muss erbracht und nachgewiesen sein, sonst nur Sicherungsmaßnahmen § 720a ZPO.

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
DREI-SÄULEN-CHECK [Mandant] [Az]

Titel:
 Art: [Endurteil / VB / Vergleich / notarielle Urkunde / ...]
 Datum: [DD.MM.JJJJ]
 Aussteller: [Gericht / Notar / Verwalter]
 Ausfertigung: [vorhanden / nur Abschrift – nachfordern]

Klausel:
 Vorhanden: [JA / NEIN]
 Art: [einfach § 725 / qualifiziert §§ 726, 730 / umgeschrieben §§ 727 ff.]
 Erteilung am: [DD.MM.JJJJ durch ...]
 Falls fehlt: [Antrag an ... mit Anlagen ...]

Zustellung:
 Erfolgt am: [DD.MM.JJJJ – Urkunde Nr. ...]
 An wen: [Schuldner / gesetzl. Vertreter / Zustellungsbevollmächtigter]
 Wartefrist: [2 Wochen § 750 Abs. 2 ZPO eingehalten / läuft bis DD.MM.JJJJ]

Ampel: [GRÜN: vollstreckbar / GELB: 1 Baustein offen / ROT: Stopp]

Nächster Schritt: [...]
```

## Qualitätsgates

- Niemals eine Säule "annehmen" oder "abkürzen" – die Prüfung ist binär.
- Bei Tabellenauszug § 201 InsO immer prüfen, ob die Forderung im Verfahren bestritten wurde (Wirkung § 178 InsO).
- Bei vorläufig vollstreckbarem Urteil: Sicherheitsleistung erbringen und gegen Quittung dokumentieren.

## Querverweise

- `zv-mahnbescheid-online` – Mahnverfahren bis zum Titel.
- `zv-notarielle-urkunde-grundschuld` – Klauselerteilung durch Notar.
- `zv-tabellenauszug-201-inso` – vollstreckbare Ausfertigung des Tabellenauszugs.
- `prozessrecht/vollstreckung` – Hub-Skill und Übergang in das gesamte Vollstreckungsthema.


<!-- AUDIT 27.05.2026 bundle_055
Halluzinations-Reparatur: BGH VII ZB 23/16 (NOT_FOUND) entfernt.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Zustellerfordernis § 750 Abs. 2 ZPO; Nachweisurkunden; Heilung nach § 189 ZPO).
Verifiziert via dejure.org.
-->

## 3. `zv-kontensuche-drittschuldner`

**Fokus:** Gläubiger hat Urteil aber kein bekanntes Konto oder Arbeitgeber des Schuldners. § 802l ZPO Drittauskunfte. Prüfraster: Rentenversicherung Bund Bundeszentralamt für Steuern Kontenabruf Kraftfahrt-Bundesamt Schuldnerverzeichnis § 882b ZPO. Output: Drittsauskunfts-Antrag und Auswertungs-Protokoll. Abgrenzung zu zv-vermögensauskunft-gv (Gläubigerantrag auf EV durch GV) und zv-pfueb-bank (nach Kontoermittlung).

# Kontensuche und Drittschuldnerermittlung


## Triage zu Beginn

1. Liegt ein vollstreckbarer Titel vor und ist die Forderung mindestens 500 EUR (§ 802l Abs. 1 ZPO)?
2. War eine Vermögensauskunft des Schuldners bereits unergiebig oder ist der Aufenthalt unbekannt?
3. Sollen alle drei Auskunftsstellen abgefragt werden (DRV, BZSt, KBA) oder nur eine?
4. Ist der Schuldner ein Unternehmen — dann Handelsregistereintrag als Informationsquelle?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 802l ZPO — Drittauskünfte (DRV Bund, BZSt/§ 24c KWG, KBA)
- § 802c ZPO — Vermögensauskunft (primäre Quelle)
- § 802d ZPO — Sperrfrist 2 Jahre für erneute Vermögensauskunft
- § 882b ZPO — Schuldnerverzeichnis
- § 93 Abs. 7 AO — Kontenabrufverfahren BZSt
- § 24c KWG — Kontenevidenzzentrale BaFin/BZSt

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Bevor eine Forderungspfändung Sinn ergibt, muss der Drittschuldner bekannt sein. Dieser Skill beschafft die Daten, ohne unnötige PfÜB ins Leere zu werfen.

## Startet bei

- Titel vorhanden, aber kein Konto, kein Arbeitgeber, keine sonstige Forderung des Schuldners bekannt
- Frühere Versuche ergebnislos
- Vermögensauskunft des Schuldners liegt vor oder Sperrfrist hindert sie nicht

## Rechtsgrundlagen

- § 802l ZPO – Drittauskünfte des Gerichtsvollziehers
- § 93 Abs. 7 AO – Kontenabrufverfahren über das BZSt
- § 24c KWG – Kontenevidenzzentrale der BaFin
- § 802c ZPO – primäre Quelle: Vermögensauskunft
- § 882b ZPO – Schuldnerverzeichnis
- § 33 StVG – Halterauskunft KBA

## Workflow

1. **Schuldnerverzeichnis abfragen** über das zentrale Vollstreckungsportal der Länder (`vollstreckungsportal.de`). Kostenpflichtig.
2. **Vorhandene Vermögensauskunft einsehen**, falls noch nicht zwei Jahre alt.
3. **Drittauskunft § 802l ZPO** durch den Gerichtsvollzieher beantragen, sobald Forderung mindestens 500 EUR und Vermögensauskunft erfolglos oder Schuldner nicht erreichbar:
 - **Deutsche Rentenversicherung Bund**: aktueller Arbeitgeber oder Rentenzahlstelle
 - **Bundeszentralamt für Steuern (BZSt)**: Kontostammdaten nach § 24c KWG, alle deutschen Kreditinstitute mit Konten des Schuldners
 - **Kraftfahrt-Bundesamt**: KFZ-Halterauskunft
4. **Ausländische Konten**: nicht über § 802l erreichbar, aber EU-Kontenpfändungsbeschluss (EuKtPVO) ist Alternative über `zv-pfueb-bank`.
5. **Plausibilitätsprüfung**: Auskunft veraltet sich. Konten existieren ggf. nicht mehr, Arbeitgeber gewechselt.
6. **Anschluss**: bekannte Bank → `zv-pfueb-bank`, bekannter Arbeitgeber → `zv-pfueb-arbeitsentgelt`.

## Voraussetzungen § 802l ZPO im Einzelnen

- Forderung mindestens 500 EUR (§ 802l Abs. 1 ZPO).
- Schuldner hat seinen gewöhnlichen Aufenthalt unbekannt **oder** Vermögensauskunft hat keine Befriedigung erwarten lassen **oder** Vermögensauskunft wurde nicht abgegeben.
- Antrag stets über den Gerichtsvollzieher; der Gerichtsvollzieher leitet die Anfragen weiter und übermittelt das Ergebnis.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
DRITTSCHULDNERSUCHE [Mandant] gegen [Schuldner]

Titel: [Art, Datum]
Forderungshöhe: EUR x (≥ 500 EUR? ja/nein)
VA-Stand: [vorhanden, Datum / fehlt / unergiebig]
Beantragte Auskünfte: [DRV / BZSt / KBA]
Geschätzte Dauer: 4-8 Wochen ab GV-Antrag
Folgeskill: [zv-pfueb-bank / -arbeitsentgelt / ...]

WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals § 802l ZPO unterhalb der Bagatellgrenze 500 EUR beantragen.
- Niemals BZSt-Kontenabruf ohne erfolglose Vermögensauskunft oder unbekannten Aufenthalt.
- Daten sind sensibel – Datenschutz beachten, Auskunft nur für konkrete Vollstreckung.
- Doppelte Abfragen vermeiden (Kostenfalle).

<!-- AUDIT 27.05.2026
Problem : BGH VII ZB 14/20 vom 15.07.2021, NJW 2021, 3046 – Beschluss auf dejure.org nicht auffindbar (NOT_FOUND). Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=15.07.2021&Aktenzeichen=VII+ZB+14%2F20
Ersatz : BGH, Beschl. v. 22.01.2015 – I ZB 77/14, NJW 2015, 2509 (§ 802l ZPO, Drittauskünfte). Verifiziert: https://dejure.org/2015,17779
Aktion : Zeile ersetzt
-->

## Querverweise

- `zv-vermoegensauskunft-gv` – Hauptquelle vor § 802l
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-kommandocenter`
- `zv-elektronische-zustellung-2027`
