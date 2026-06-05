---
name: abmahnung-urheberrecht-erfindungsmeldung
description: "Abmahnung Urheberrecht Erfindungsmeldung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Abmahnung Urheberrecht Erfindungsmeldung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Abmahnung Urheberrecht Erfindungsmeldung** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `abmahnung-urheberrecht` | Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte Unterlassungserklärung Deckelung Abmahnkosten § 97a Abs. 3 UrhG im privaten Bereich Filesharing-Praxis Lizenzanalogie § 97 Abs. 2 UrhG Schadensersatz. Output: Abmahnungsentwurf oder Reaktions-Memo auf erhaltene Abmahnung. Abgrenzung zu unterlassungsverlangen (MarkenG UWG PatG) und verletzungs-triage (Erstentscheidung). |
| `erfindungsmeldung-aufnahme` | Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungsgesetz. Prüfraster: Neuheit erfinderische Tätigkeit technischer Charakter EPUe Schutzfähigkeit Arbeitnehmererfindung Inanspruchnahme vs. Freistellung Frist 4 Monate § 6 ArbnErfG strategischer Wert. Output: Ersteinschaetzung Anmeldung/Weiterverfolgung/Ablehnung. Abgrenzung zu fto-triage (Freiheitsgrad) und schutzrechts-portfolio (Portfolioverwaltung). |
| `evvollzug-neu-002-urteilsverfuegung-beschlussverfuegung-und-zust` | EV-Vollzug: Unterschied Urteilsverfügung und Beschlussverfügung, Zustellwege und Vollziehungsmodalitäten im gewerblichen Rechtsschutz. Amts- vs. Parteizustellung, Fristfolgen, Strategiewahl für Marken-, Patent- und UWG-Fälle. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Abmahnung Urheberrecht Erfindungsmeldung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `abmahnung-urheberrecht`

**Fokus:** Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte Unterlassungserklärung Deckelung Abmahnkosten § 97a Abs. 3 UrhG im privaten Bereich Filesharing-Praxis Lizenzanalogie § 97 Abs. 2 UrhG Schadensersatz. Output: Abmahnungsentwurf oder Reaktions-Memo auf erhaltene Abmahnung. Abgrenzung zu unterlassungsverlangen (MarkenG UWG PatG) und verletzungs-triage (Erstentscheidung).

# Urheberrechtliche Abmahnung – § 97a UrhG

## Zweck

Dieser Skill behandelt das urheberrechtliche Abmahnverfahren nach § 97a UrhG
als notwendige Voraussetzung für die gerichtliche Geltendmachung von
Unterlassungs- und Schadensersatzansprüchen (§§ 97, 97a UrhG). Er deckt
sowohl die Gläubigerperspektive (Abmahnung verfassen, Unterlassungserklärung
einfordern) als auch die Schuldnerperspektive (Abmahnung prüfen, modifizierte
Unterlassungserklärung abgeben) ab. Schwerpunkte sind die formalen
Mindestanforderungen an die Abmahnung (§ 97a Abs. 2 UrhG), die Kostendeckelung
im privaten Bereich (§ 97a Abs. 3 UrhG) und die Berechnung des
Schadensersatzes nach der Lizenzanalogie (§ 97 Abs. 2 Satz 3 UrhG) –
insbesondere in Filesharing-Fällen.

Mandatsbezug: Abgemahnter Privatnutzer erhält Filesharing-Abmahnung; Rechteinhaber
möchte eigene Werke schützen; Streit über Höhe der Abmahnkosten und des Schadensersatzes.

## Eingaben

1. **Abmahngegenstand** – Welches Werk (Buch, Musik, Film, Foto, Software)?
 Wer ist Rechteinhaber (Urheber, Verwerter, Lizenznehmer mit Klagerecht)?
2. **Verletzungshandlung** – Öffentliche Zugänglichmachung (§ 19a UrhG) via
 Filesharing (BitTorrent, eDonkey), Download, Hosting? Zeitpunkt und Umfang?
3. **Personenkreis** – Privat- oder Unternehmensnutzer (für § 97a Abs. 3 UrhG
 maßgeblich)?
4. **IP-Adressdaten** – Gerichtlicher Auskunftsanspruch nach § 101 Abs. 9 UrhG
 beim Provider bereits erwirkt? Zuordnung zur Person gesichert?
5. **Vorangegangene Abmahnungen** – Wiederholungsgefahr bereits durch frühere
 Verletzung begründet?
6. **Empfangene Abmahnung** – Volltext, Absender, Frist, Forderungshöhe,
 beigefügte Unterlassungserklärung.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 97 UrhG** – Unterlassungs- und Schadensersatzanspruch bei Urheberrechts-
 verletzungen; § 97 Abs. 2 UrhG: Schadensersatz auch im Wege der Lizenzanalogie
 (Satz 3) oder nach tatsächlichem Schaden (Satz 1) oder Gewinnherausgabe
 (Satz 2, str.).
- **§ 97a Abs. 1 UrhG** – Abmahnung als notwendige Voraussetzung für
 Unterlassungsklage; Pflicht des Abmahnenden zur inhaltlichen Korrektheit.
- **§ 97a Abs. 2 UrhG** – Mindestinhalt: Abgemahnter, Rechteinhaber,
 Verletzungshandlung, geltend gemachter Anspruch, Kosten.
- **§ 97a Abs. 3 UrhG** – Kostendeckelung bei privater Erstnutzung auf 100 €
 Gegenstandswert (Erstattungsfähigkeit der Abmahnkosten auf diesen Betrag
 begrenzt), wenn Verstoß nicht im geschäftlichen Verkehr und keine erheblichen
 Rechtsverletzung vorliegt (§ 97a Abs. 3 Satz 1 Nr. 1 und 2 UrhG).
- **§ 97a Abs. 4 UrhG** – Kosten einer unberechtigten Abmahnung trägt der
 Abmahner; Gegenanspruch des Abgemahnten.
- **§ 101 UrhG** – Auskunftsanspruch gegen Verletzer und Provider (§ 101 Abs. 9
 UrhG: gerichtliche Anordnung erforderlich); Drittauskunft bei Filesharing.
- **§ 19a UrhG** – Recht der öffentlichen Zugänglichmachung; Filesharing erfüllt
 diesen Tatbestand durch das Anbieten im Peer-to-Peer-Netzwerk.
- **§ 44b UrhG** – Text und Data Mining (seit 2021); für Abmahnpraxis nicht
 unmittelbar relevant, aber bei KI-generierten Inhalten zu beachten.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "Tannöd": Zur Lizenzanalogie bei Filesharing: Der Rechteinhaber kann als
 Mindestschadensersatz den Betrag verlangen, den eine vernünftige Partei als
 angemessene Vergütung für die Gestattung der Nutzung vereinbart hätte;
 Filesharing ermöglicht unbegrenzte Verbreitung, was bei der Lizenzberechnung
 zu berücksichtigen ist; einzelne Downloads rechtfertigen einen Pauschalbetrag,
 da genaue Feststellung der Schadenshöhe nicht möglich ist (§ 287 ZPO).

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "Tauschbörse III": Zur Störerhaftung des Anschlussinhabers: Der Anschluss-
 inhaber haftet als Störer für Urheberrechtsverletzungen über seinen Anschluss,
 wenn er Prüfungspflichten verletzt hat (Sicherung des WLAN, Belehrung von
 Familienmitgliedern); sekundäre Darlegungslast des Anschlussinhabers zur
 Benennung möglicher alternativer Täter.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Für den Abmahnenden (Rechteinhaber)

1. **Rechteinhaberschaft prüfen** – Urheber (§ 7 UrhG), Rechteinhaber durch
 Übertragung (§ 31 UrhG), ausschließlicher Lizenznehmer mit Klagerecht?

2. **Verletzungshandlung dokumentieren** – Screenshot mit Zeitstempel, IP-Adresse,
 Portname, Dateiname; ggf. Privatgutachter für Filesharing-Fälle; Nachweis
 des Anmeldetags (§ 32 Abs. 1 MarkenG – hier: Veröffentlichungsdatum des Werks).

3. **Auskunft einholen (§ 101 Abs. 9 UrhG)** – Antrag beim Landgericht am
 Sitz des Providers auf gerichtliche Anordnung; Frist zur Datenspeicherung
 beachten (Vorratsdaten vs. Verbindungsdaten).

4. **Abmahnung verfassen (§ 97a Abs. 2 UrhG)** – Pflichtinhalt: Bezeichnung des
 Verletzers, des Rechteinhabers, der verletzten Rechte, der Verletzungshandlung,
 der geltend gemachten Ansprüche, der Abmahnkosten; konkrete und strafbewehrte
 Unterlassungserklärung beifügen; angemessene Reaktionsfrist setzen (i. d. R.
 7–14 Tage, ggf. kürzer bei dringlichen Fällen).

5. **Frist überwachen** – Bei Nichtreaktion oder unzureichender Erklärung:
 einstweilige Verfügung beim LG (§§ 935, 940 ZPO); Dringlichkeit beachten
 (Monatsfrist ab Kenntnis der Verletzung bei Verfügungen, h. M.).

6. **Schadensersatz geltend machen** – Lizenzanalogie (§ 97 Abs. 2 Satz 3 UrhG);
 Schätzung nach § 287 ZPO; Tabellen für übliche Lizenzgebühren (MFM-Tabelle
 für Fotos; GEMA-Tarife für Musik; BGH-Rspr. für Filesharing, vgl.
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Für den Abgemahnten (Schuldner)

1. **Abmahnung prüfen** – Formelle Anforderungen § 97a Abs. 2 UrhG erfüllt?
 Rechteinhaberschaft glaubhaft? Verletzungshandlung konkret beschrieben?

2. **Kostendeckelung § 97a Abs. 3 UrhG prüfen** – Privater Bereich? Erstmalige
 Verletzung? Kein erheblicher Verstoß? Wenn ja: Abmahnkosten auf Erstattung
 von Kosten aus 100 € Gegenstandswert begrenzt.

3. **Modifizierte Unterlassungserklärung abgeben** – Inhaltlich vollständig (alle
 zukünftigen gleichartigen Verletzungshandlungen erfassen; Dreier, § 97a Rn. 12);
 ohne Anerkenntnis der Rechtsverletzung und der Kostenforderung; Vertragsstrafe
 nach Hamburger Brauch (konkrete Summe nach billigem Ermessen).

4. **Kosten verhandeln** – Lizenzanalogie begründen oder anfechten; bei Filesharing
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

5. **Verjährung beachten** – § 102 UrhG i. V. m. §§ 195, 199 BGB: 3-Jahres-
 Regelverjährung; Beginn mit Kenntnis (§ 199 Abs. 1 BGB); 10-Jahres-Maximal-
 frist ab Verletzungshandlung (§ 199 Abs. 3 Nr. 1 BGB).

## Ausgabeformat

- **Abmahnschreiben** (Schriftsatz): Adressat, Verletzungshandlung, gerügte Normen,
 Aufforderung zur Unterlassungserklärung und Kostenzahlung, Frist.
- **Modifizierte Unterlassungserklärung** (Muster): Formulierung ohne Schuldanerkenntnis;
 Vertragsstrafe; Beschränkung auf konkrete Verletzungsart.
- **Verteidigungsmemo** (Gutachtenstil): Deckelungsprüfung § 97a Abs. 3 UrhG →
 Rechteinhaberschaft → Verletzungshandlung → sekundäre Darlegungslast.

## Beispiel

*Sachverhalt:* Privatperson P erhält Abmahnung wegen angeblicher Beteiligung
an einer Filesharing-Tauschbörse für einen Spielfilm; Forderung: 956 € Abmahnkosten
+ 500 € Schadensersatz.

*Verteidigungsmemo (Gutachtenstil):*

**Kostendeckelung:** P ist Privatperson und die Verletzung war nach Darstellung
des Abmahners einmalig (kein Wiederholungsfall, kein erheblicher Verstoß).
Die Abmahnkosten sind daher nach § 97a Abs. 3 Satz 1 UrhG auf die Erstattung
aus einem Gegenstandswert von 100 € begrenzt (Dreier, in: Dreier/Schulze, UrhG,
7. Aufl. 2022, § 97a Rn. 12). Aus 100 € Gegenstandswert ergibt sich nach dem
RVG für eine 1,3-Gebühr (Nr. 2300 VV RVG) ein Erstattungsbetrag von ca. 27,30 €
(zzgl. Auslagenpauschale); die geltend gemachten 956 € sind insoweit überhöht.

**Schadensersatz:** 500 € nach Lizenzanalogie ist bei einem Spielfilm vertretbar
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
kann P durch sekundäre Darlegungslast auf alternative Täter (Familienmitglieder)
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Empfehlung:** Modifizierte Unterlassungserklärung ohne Schuldanerkenntnis abgeben;
Kosten auf Deckelungsbetrag reduzieren; Schadensersatz verhandeln.

*(Reber, in: Schricker/Löwenheim, UrhR, 6. Aufl. 2020, § 97a Rn. 25.)*

## Risiken und typische Fehler

- **Unzureichende Unterlassungserklärung:** Zu enge Erklärung beseitigt Wiederholungs-
 gefahr nicht; Rechteinhaber kann sofort klagen (Reber, § 97a Rn. 25).
- **Fristen bei einstweiliger Verfügung:** Dringlichkeit entfällt, wenn Rechteinhaber
 mehr als 4–6 Wochen (je nach OLG-Praxis) nach Kenntnis zuwartete, ohne zu
 handeln.
- **Sekundäre Darlegungslast:** Pauschales Bestreiten genügt nicht (BGH
 "Tauschbörse III"); P muss konkret darlegen, wer sonst Zugang hatte.
- **IP-Adresszuordnung fehlerhaft:** Gutachtlich belegte Zuordnung angreifen;
 Richtigkeit der Ermittlung durch Privatgutachter in Frage stellen.
- **Deckelung bei erheblichem Verstoß ausgeschlossen:** § 97a Abs. 3 Satz 2
 UrhG; bei massenhaftem Uploading oder gewerblichem Kontext greift die
 Deckelung nicht.
- **Berufsrecht und Datenschutz:** § 43a Abs. 2 BRAO, § 203 StGB; Mandantendaten
 (insb. IP-Adressen) unterliegen der Verschwiegenheit.
- **Verjährung:** § 102 UrhG, §§ 195, 199 BGB; bei Unkenntnis beginnt Frist nicht
 zu laufen, aber 10-Jahres-Maximallust ab Verletzung (§ 199 Abs. 3 Nr. 1 BGB).

## Quellenpflicht

Alle Aussagen zu Abmahnvoraussetzungen, Kostendeckelung und Lizenzanalogie nach
`references/zitierweise.md`. BGH-Rspr. zur Störerhaftung und sekundären
Darlegungslast ist dynamisch; neuere Entscheidungen (insb. BGH seit 2018) immer
auch auf veränderte Rechtslage (Haftungsprivileg § 8 TMG a. F. → § 7 ff. DDG)
hin prüfen. Bei Streit über Deckelungsvoraussetzungen h. M. und Gegenauffassung
kenntlich machen.

## Triage-Fragen vor Urheberrechts-Abmahnung

Bevor die Abmahnung versandt wird, klaere:
1. Ist das urheberrechtlich geschuetzte Werk klar identifiziert und der Schutzbestand unstreitig (§ 2 I UrhG — Schoepfungshoehe)?
2. Handelt es sich um eine Privatperson (§ 97a III UrhG — Deckelung EUR 1.000) oder einen gewerblichen Verletzer?
3. Ist der Rechteinhaber eindeutig der Mandant (Werkvertrag, Arbeitsvertrag, Rechteabtretung)?
4. Ist die Verletzungshandlung noch andauernd oder bereits beendet (Wiederholungsgefahr vs. Erstbegehungsgefahr)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Korrektur: GRUR 2016, 176 → GRUR 2016, 191 (alle 3 Fundstellen). Verifiziert via dejure.org.
-->

## 2. `erfindungsmeldung-aufnahme`

**Fokus:** Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungsgesetz. Prüfraster: Neuheit erfinderische Tätigkeit technischer Charakter EPUe Schutzfähigkeit Arbeitnehmererfindung Inanspruchnahme vs. Freistellung Frist 4 Monate § 6 ArbnErfG strategischer Wert. Output: Ersteinschaetzung Anmeldung/Weiterverfolgung/Ablehnung. Abgrenzung zu fto-triage (Freiheitsgrad) und schutzrechts-portfolio (Portfolioverwaltung).

# Erfindungseingang — Erstprüfung

## Zweck

Diese Skill führt eine strukturierte Erstprüfung einer Erfindungsmeldung durch. Sie schirmt offensichtliche Ausschlussgründe ab, identifiziert kritische Fristen (insbesondere neuheitsschädliche Vorveröffentlichungen nach § 3 PatG) und empfiehlt eine von drei Handlungsoptionen: **WEITERVERFOLGEN** (Beauftragung einer Patentrecherche und Einschaltung eines Patentanwalts), **KLÄREN** (Rückfragen an den Erfinder oder Spezialisten) oder **ABLEHNEN** (mit konkreter Begründung).

Die Skill trifft keine Patentierbarkeitsaussage. Eine solche setzt eine vollständige Patentrecherche, Anspruchskonstruktion und das fachliche Urteil eines zugelassenen Patentanwalts voraus.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

Wenn der Nutzer keine Erfindungsmeldung eingereicht hat, werden folgende Angaben in einem Durchgang abgefragt:

1. **Was ist die Erfindung?** Beschreibung in eigenen Worten — was sie tut, wie sie funktioniert, was die Kernidee ist.
2. **Welches Problem wird gelöst?** Was war zuvor nicht möglich oder mangelhaft?
3. **Worin liegt der Unterschied zum Stand der Technik?** Was haben andere bisher gemacht, und was macht diese Erfindung anders?
4. **Wer hat erfunden, und wann?** Namen, Arbeitsverhältnis (Arbeitnehmer/Freier Mitarbeiter?), ungefähres Entstehungsdatum.
5. **Wurde die Erfindung bereits offenbart?** Publikation, Messe, Konferenz, Angebot, öffentliches Repository, Kundendemonstration (auch unter NDA). Wenn ja: wann und wie.
6. **Wird die Erfindung bereits genutzt oder ist sie geplant?** In Produktion, im Pilotbetrieb, auf der Roadmap oder noch auf dem Papier?
7. **Welches Technologiegebiet?** Software, Hardware, Mechanik, Biotechnologie, KI/ML, Chemie, Medizinprodukt etc.

Bei formeller Erfindungsmeldung (IDF oder Unternehmensformular): Felder daraus entnehmen, nur Fehlende erfragen.

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 1–5 PatG** — Patentierbarkeitsvoraussetzungen: Neuheit (§ 3), erfinderische Tätigkeit (§ 4), gewerbliche Anwendbarkeit (§ 5)
- **Art. 52–57 EPÜ** — Patentierbarkeit im europäischen Patentsystem; technischer Charakter als Voraussetzung; Art. 56 EPÜ erfinderische Tätigkeit (Aufgabe-Lösungs-Ansatz)
- **§§ 5–12 ArbnErfG** — Meldepflicht (§ 5), Inanspruchnahme durch den Arbeitgeber (§ 6 Abs. 1: Frist 4 Monate), unbeschränkte vs. beschränkte Inanspruchnahme; Vergütungspflicht (§§ 9 ff. ArbnErfG)
- **§ 3 Abs. 1 PatG** — Absolutes Neuheitserfordernis: jede Offenbarung vor dem Anmeldetag ist neuheitsschädlich; eine Schonfrist für Vorveröffentlichungen gilt im deutschen und europäischen Patentrecht nicht
- **§§ 1–3 GebrMG** — Gebrauchsmuster als schnellerer Schutzrechtsweg (keine erfinderische Tätigkeit im gleichen Maßstab, aber Neuheit + erfinderischer Schritt erforderlich)
- **§ 26 GeschGehG** — Geschäftsgeheimnis als Alternative bei mangelnder Erkennbarkeit der Verletzung

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Benkard/Melullis, PatG, 12. Aufl. 2023, § 3 Rn. 1 ff. (Neuheitsbegriff, Stand der Technik)
- Bartenbach/Volz, ArbnErfG, 6. Aufl. 2019, § 5 Rn. 1 ff. (Meldepflicht und Form) und § 9 Rn. 1 ff. (Vergütung)
- Mes, PatG/GebrMG, 5. Aufl. 2020, § 1 Rn. 20 ff. (technischer Charakter, Software- und KI-Erfindungen)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Meldung aufnehmen

Vorliegende Erfindungsmeldung vollständig lesen. Fehlen Angaben: Rückfragen gemäß Abschnitt "Eingaben" in einem Durchgang stellen. Unvollständige Meldungen nicht screenen — ein Screening von "einer neuen KI-Lösung für X" ohne technische Substanz ist schlechter als kein Screening.

**Arbeitnehmererfindung prüfen:** Wenn der Erfinder Arbeitnehmer ist, zunächst klären: Handelt es sich um eine Diensterfindung (§ 4 Abs. 2 ArbnErfG: Entstehung aus dem Arbeitverhältnis oder wesentlich auf betriebliche Erfahrungen/Tätigkeiten beruhend)? Wenn ja: Meldepflicht nach § 5 ArbnErfG auslösen und Inanspruchnahmefrist (4 Monate, § 6 Abs. 1) dokumentieren.

### Schritt 2: Sechs Prüfungsschirme

Jeden Schirm in der Reihenfolge abarbeiten. Ergebnis je Schirm: `✓ grün`, `🟡 unklar — Klärungsbedarf`, `🔴 Rote Flagge`.

#### Schirm 1: Neuheitssignale (§ 3 PatG, Art. 54 EPÜ)

**Rote Flaggen (🔴):**
- "Wir haben [bekannte Technik] auf [neues Gebiet] angewandt" — Anwendung bekannter Methoden ohne technische Besonderheit
- "Wettbewerber machen etwas Ähnliches" — Beschreibung selbst stellt Neuheit in Frage
- Merkmal findet sich bereits in öffentlich zugänglichen Produkten, Publikationen oder Patenten

**Grüne Flaggen (✓):**
- Neuer **Mechanismus** — nicht nur neue Anwendung, sondern neue technische Wirkungsweise
- Neue **Kombination** mit unerwartetem Ergebnis
- Lösung eines bisher ungelösten Problems mit spezifischer technischer Lehre

#### Schirm 2: Erfinderische Tätigkeit (§ 4 PatG, Art. 56 EPÜ)

EPA-Prüfungsansatz: Aufgabe-Lösungs-Ansatz. Würde ein Fachmann ausgehend vom nächstliegenden Stand der Technik und der zugrunde liegenden technischen Aufgabe zur beanspruchten Lösung gelangen?

**Rote Flaggen (🔴):**
- Kombinieren bekannter Elemente auf vorhersehbare Weise (predictable combination)
- Routinemäßige Optimierung bekannter Parameter ohne überraschenden Effekt
- "Obvious to try" — eine aus wenigen naheliegenden Alternativen ohne Hindernis

**Grüne Flaggen (✓):**
- Stand der Technik lehrte vom Lösungsweg ab (teaching away)
- Unerwarteter technischer Effekt (surprising effect)
- Langbekanntes Problem, das trotz Bemühungen bisher ungelöst geblieben ist

#### Schirm 3: Technischer Charakter und Schutzfähigkeit (Art. 52 EPÜ, § 1 PatG)

Software, KI/ML und Geschäftsmethoden: Nicht per se ausgeschlossen, aber technischer Charakter muss vorliegen. EPA: "technical character" — weitgehend jeder Bezug zur Technik genügt; Abgrenzung gilt auf der Ebene der erfinderischen Tätigkeit.

**Rote Flaggen (🔴):**
- Reine Geschäftsmethode ohne technische Umsetzung
- Mathematischer Algorithmus ohne technische Anwendung
- Ablauf menschlicher Tätigkeiten ohne computergestützte oder physische Komponente
- KI-Invention: Schutzbegehren richtet sich allein auf Funktion (empfehlen, klassifizieren, vorhersagen) ohne konkrete technische Mittel

**Grüne Flaggen (✓):**
- Technische Verbesserung des Computers selbst (Architektur, Sicherheit, Effizienz)
- Technische Mittel werden konkret beschrieben, nicht nur Ergebnisse beansprucht
- Einbettung in technisches Gebiet (Bildverarbeitung, Signalübertragung, Steuerung)

#### Schirm 4: Neuheitsschädliche Vorveröffentlichung / Fristen (§ 3 PatG)

Im deutschen und europäischen Patentrecht gilt **absolutes Neuheitserfordernis**: jede öffentliche Zugänglichmachung vor dem Anmeldetag ist neuheitsschädlich. Eine Schonfrist für Vorveröffentlichungen gilt nicht.

**Ausnahme:** § 3 Abs. 5 PatG (Ausstellungsprioritätsprinzip) und Art. 55 EPÜ (offensichtlicher Missbrauch oder Ausstellungsprivileg) — sehr eng, nicht als Sicherheitsnetz einplanen.

Kategorisierung:

**🔴 Wahrscheinlich neuheitsschädlich:**
- Öffentliche Veröffentlichung, Verkauf, Angebot, Messedemonstration, öffentliches Repository **vor dem Anmeldetag**
- Preprint, Konferenzbeitrag, Social-Media-Post, Blogbeitrag mit technischem Inhalt

**🟡 Fristdruck:**
- Veröffentlichung liegt vor, Anmeldung noch nicht erfolgt — **sofortiger Handlungsbedarf**

**✓ Unbedenklich:**
- Keine Offenbarung außerhalb vertraulicher Kanäle
- Kundenpräsentation unter NDA (Sorgfalt: NDA-Reichweite prüfen)

Konkret erfragen: Konferenzbeiträge (auch eingereicht, nicht nur angenommen), Preprints, öffentliche Repositories, Messeauftritte, Angebote an Kunden, Investorenpräsentationen ohne NDA.

#### Schirm 5: Erkennbarkeit einer Verletzung (Detectability)

Ist eine Verletzung am Markt erkennbar? Server-seitige Algorithmen, interne Fertigungsschritte und reine Datenverarbeitungsmethoden ohne erkennbare Außenwirkung sind schwer durchzusetzen.

**🔴 Geringe Erkennbarkeit:**
- Server-seitiger Algorithmus ohne erkennbares Ausgabemuster
- Internes Fertigungsverfahren (z. B. neuer Ätzschritt in Halbleiterproduktion)
- Trainings-Methodik für ML-Modell — nur durch aufwendige Tests erahnbar

Bei geringer Erkennbarkeit: Abwägung Patent vs. Geschäftsgeheimnis nach GeschGehG vornehmen. Wer die Entscheidung in der Praxis trifft: gemäß Unternehmensrichtlinie / Mandatsprofil.

**✓ Hohe Erkennbarkeit:**
- Konsumentenprodukt mit sichtbaren Merkmalen
- Veröffentlichte API, Protokoll, SDK
- Physischer Mechanismus in verteiltem Produkt

#### Schirm 6: Strategischer Wert

Passt die Erfindung zur Schutzrechtsstrategie des Unternehmens? Prüfung anhand des Mandatsprofils:

- **Offensiv (Durchsetzungsportfolio):** Ist der Anspruch breit und assertionsfähig?
- **Defensiv (Freedom to Operate):** Schützt die Anmeldung eine relevante Technologie?
- **Lizenz-/Erlösmodell:** Ist die Erfindung lizenzierbar und wer würde zahlen?
- **Kerntechnologie vs. Peripherie:** Kern hat höheren Wert.
- **Wettbewerbslandschaft:** In patentintensiven Sektoren (Pharma, Halbleiter) frühzeitig anmelden.

### Schritt 3: Erfindungsprüfungsvermerk erstellen

Format:

> **Erfindungsprüfungsvermerk — [Titel der Erfindung]**
>
> **Ergebnis: [WEITERVERFOLGEN / KLÄREN / ABLEHNEN]**
>
> *[Ein Satz — Begründung im Klartext.]*
>
> ---
>
> ### Prüfungsergebnisse
>
> | Prüfschirm | Ergebnis | Anmerkung |
> |---|---|---|
> | Neuheitssignale | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Erfinderische Tätigkeit | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Technischer Charakter | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Vorveröffentlichung / Fristen | [✓ / 🟡 / 🔴] | [einzeiliger Grund + Daten] |
> | Erkennbarkeit | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Strategischer Wert | [✓ / 🟡 / 🔴] | [Bezug zum Mandatsprofil] |
>
> ---
>
> ### Offene Punkte
>
> - [Frage / Klärungsbedarf]
>
> ### Nächste Schritte
>
> 1. **Patentrecherche beauftragen** — Suchanfrage für Patentanwalt mit Anspruchskonzepten, Erfindernamen, IPC-Klasse und bekannten Referenzen.
> 2. **Rückfrage an Erfinder** — Klärung offener Punkte zu [konkreten Punkten].
> 3. **An Patentanwalt übergeben** — bei Grenzfragen zum technischen Charakter oder zur Schutzstrategie.
> 4. **Ablehnen und Dankesschreiben** — Begründung archivieren.
> 5. **Geschäftsgeheimnis-Route** — Hinweis an zuständige Stelle gemäß GeschGehG.

### Schritt 4: Arbeitnehmererfindung — Pflichtprozess

Wenn der Erfinder Arbeitnehmer ist:

- **§ 5 ArbnErfG — Meldepflicht:** Erfinder hat unverzüglich zu melden. Form: schriftlich, Beschreibung der Erfindung, Entstehungsumstände.
- **§ 6 Abs. 1 ArbnErfG — Inanspruchnahmefrist:** Arbeitgeber hat **4 Monate** ab Eingang der Meldung, um unbeschränkt oder beschränkt in Anspruch zu nehmen. Frist läuft automatisch; Untätigkeit gilt als Freigabe.
- **§§ 9 ff. ArbnErfG — Vergütungspflicht:** Bei Inanspruchnahme entsteht Vergütungsanspruch. Bemessung nach den Richtlinien für die Vergütung von Arbeitnehmererfindungen im privaten Dienst (1959/zuletzt geändert). Faktoren: Erfindungswert, Anteilsfaktor, Mitarbeiterstellung.
- Frist im Vermerk dokumentieren und in das Fristenkontrollsystem des Mandanten eintragen.

## Ausgabeformat

Der Erfindungsprüfungsvermerk enthält: Titel, Ergebnis (WEITERVERFOLGEN / KLÄREN / ABLEHNEN), Prüftabelle, offene Punkte, nächste Schritte. Bei aktiver Mandatssache: Ausgabe in den Mandatsordner.

Kein internes Arbeitsnarrativ im Vermerk. Der Vermerk ist sofort verwendbar.

## Beispiel

**Eingabe:** "Neuer Cache-Algorithmus auf Basis eines erlernten Modells anstelle von LRU; im ersten Quartal dieses Jahres entwickelt, noch nicht veröffentlicht, Prototyp intern im Staging."

**Ergebnis (Beispiel):**

> **Erfindungsprüfungsvermerk — Lernbasierter Cache-Algorithmus**
>
> **Ergebnis: WEITERVERFOLGEN** — Neuheit und technischer Charakter sind prima facie gegeben; keine neuheitsschädliche Vorveröffentlichung erkennbar; strategische Relevanz in Abhängigkeit vom Mandatsprofil prüfen.
>
> | Prüfschirm | Ergebnis | Anmerkung |
> |---|---|---|
> | Neuheitssignale | 🟡 | Mechanismus neu, aber verwandte Literatur (ML-Caching) vorhanden — Recherche erforderlich |
> | Erfinderische Tätigkeit | 🟡 | Unerwarteter Effizienzgewinn behauptet — durch Recherche zu belegen |
> | Technischer Charakter | ✓ | Konkrete technische Verbesserung der Cache-Verwaltung |
> | Vorveröffentlichung | ✓ | Keine Offenbarung, intern und vertraulich |
> | Erkennbarkeit | 🟡 | Server-seitig: Abwägung Patent vs. Geschäftsgeheimnis empfohlen |
> | Strategischer Wert | 🟡 | Abhängig vom Mandatsprofil |

## Risiken und typische Fehler

- **Neuheitsschädliche Vorveröffentlichung übersehen:** Jede öffentliche Zugänglichmachung vor Anmeldetag zerstört die Patentierbarkeit weltweit (außer engen Ausnahmefällen). Eine Schonfrist für Vorveröffentlichungen gilt nicht.
- **ArbnErfG-Fristen versäumen:** Die 4-Monats-Inanspruchnahmefrist (§ 6 Abs. 1 ArbnErfG) läuft automatisch. Nicht im Fristenbuch eingetragen = Freigabe der Erfindung.
- **Patentierbarkeit bestätigen:** Die Skill trifft keine Patentierbarkeitsaussage. "Besteht die Erstprüfung" ist nicht "patentierbar".
- **Erkennbarkeitsfrage ignorieren:** Ein Patent auf eine nicht erkennbare Verletzungsform veröffentlicht das Know-how ohne Durchsetzungsmöglichkeit.
- **KI/Software-Erfindungen: technischen Charakter unterschätzen:** Der EPA bewertet technischen Charakter weit; nicht vorschnell ablehnen.

## Quellenpflicht

Jede Aussage zu Neuheit, erfinderischer Tätigkeit oder Vergütung muss auf konkreten Normen oder Entscheidungen beruhen. Pflichtquellen in jedem Vermerk:

- **Gesetzestext:** § 3, § 4, § 5 PatG; §§ 5, 6, 9 ff. ArbnErfG; Art. 52–56 EPÜ
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zur Neuheit oder erfinderischen Tätigkeit
- **Kommentar:** Benkard PatG oder Bartenbach/Volz ArbnErfG mit § und Randnummer
- Alle Quellen mit Fundstelle zitieren. Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen bei Erfindungsmeldung

Bevor die Erfindung aufgenommen und bewertet wird, klaere:
1. Liegt eine Diensterfindung (§ 4 ArbnErfG — Arbeitgeber hat Inanspruchnahmerecht) oder eine Freierfindung vor?
2. Laeuft die 4-Monats-Frist des § 6 I ArbnErfG fuer die Inanspruchnahme bereits?
3. Gibt es neuheitsschaedliche Vorveröffentlichungen (Veroeffentlichung vor Anmeldedatum)?
4. Besteht technischer Charakter im Sinne des EPÜ Art. 52 (Software: loest technisches Problem auf technischem Weg)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Korrektur: Zitat aus "Aktuelle Rechtsprechung"-Block entfernt (bei Zweifel loeschen).
-->

## 3. `evvollzug-neu-002-urteilsverfuegung-beschlussverfuegung-und-zust`

**Fokus:** EV-Vollzug: Unterschied Urteilsverfügung und Beschlussverfügung, Zustellwege und Vollziehungsmodalitäten im gewerblichen Rechtsschutz. Amts- vs. Parteizustellung, Fristfolgen, Strategiewahl für Marken-, Patent- und UWG-Fälle.

# EV-Vollzug 002: Urteilsverfügung, Beschlussverfügung und Zustellweg

## Zweck und Mandatsbezug

Dieser Skill klärt die praxiskritische Unterscheidung zwischen **Beschlussverfügung** (ohne mündliche Verhandlung, §§ 937 Abs. 2, 922 ZPO) und **Urteilsverfügung** (nach mündlicher Verhandlung) sowie die daraus folgenden **unterschiedlichen Vollziehungsmodalitäten**. Fehler bei der Zuordnung kosten die gesamte EV.

Mandatsbezug: Anwalt erhält telefonisch die Nachricht, die EV sei erlassen – ohne zu wissen, ob es sich um einen Beschluss oder ein Urteil handelt. Die Vollziehungsschritte sind verschieden. Dieser Skill strukturiert die Differenzierung und den konkreten Handlungsweg.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 937 Abs. 2 ZPO** – Erlass der einstweiligen Verfügung ohne mündliche Verhandlung (Beschlussverfügung) bei Dringlichkeit.
- **§ 922 Abs. 1 ZPO** – Beschlussverfügung: Zustellung durch Antragsteller (Parteizustellung).
- **§ 922 Abs. 2 ZPO** – Urteilsverfügung: Amtszustellung durch das Gericht.
- **§ 929 Abs. 2 ZPO** – Einmonatige Vollziehungsfrist; gilt für beide Verfügungsarten, Fristbeginn unterscheidet sich.
- **§ 936 ZPO** – Anwendbarkeit der Arrestvorschriften auf einstweilige Verfügungen.
- **§ 890 ZPO** – Ordnungsgeld, Ordnungshaft nach erfolgreichem Vollzug einer Unterlassungsverfügung.

### Strukturunterschiede

| Merkmal | Beschlussverfügung | Urteilsverfügung |
|---|---|---|
| Verfahrensweg | Ohne mündliche Verhandlung | Nach mündlicher Verhandlung |
| Rechtsgrundlage | § 937 Abs. 2 ZPO | § 922 Abs. 1 ZPO |
| Zustellung | Parteizustellung durch Antragsteller | Amtszustellung durch Gericht |
| Fristbeginn (§ 929 Abs. 2) | Zustellung an Antragsteller | Verkündung |
| Widerspruchsmöglichkeit | Ja, § 924 ZPO | Nein (Berufung) |
| Formelle Bezeichnung | „Beschluss" | „Urteil" |

## Kaltstart in 5 Fragen

1. **Verfahrensweg:** Hat das Gericht eine mündliche Verhandlung durchgeführt oder wurde die EV ohne Verhandlung erlassen?
2. **Dokumentenkopf:** Wie ist die Entscheidung überschrieben – „Beschluss" oder „Urteil"?
3. **Zustellungsnachweis:** Hat das Gericht bereits von Amts wegen zugestellt oder liegt die Zustellpflicht beim Antragsteller?
4. **Fristlage:** Wann wurde die Entscheidung dem Antragstelleranwalt übermittelt? Gibt es einen Zustellungsvermerk?
5. **Output:** Differenzierungsmatrix, Fristenblatt mit Vollziehungsschritten oder Kurznotiz für die Mandantenakte?

## Prüfprogramm

### Schritt 1 – Entscheidungsform identifizieren

- Titelseite der Entscheidung lesen: „Beschluss" oder „Urteil"?
- Beschluss ohne Tatbestand und Entscheidungsgründe in gesondertem Abschnitt deutet auf Beschlussverfügung hin.
- Enthält die Entscheidung einen Tenor mit Datum der Verkündung und Parteienvertretern im Rubrum? Dann Urteilsverfügung.

### Schritt 2 – Zustellungsverantwortung klären

- Bei **Beschlussverfügung:** Antragstelleranwalt muss aktiv werden; Parteizustellung beauftragen.
- Bei **Urteilsverfügung:** Gericht stellt von Amts wegen zu; Anwalt prüft lediglich, ob Amtszustellung erfolgt und fragt ggf. nach.
- Achtung: Auch bei Urteilsverfügung kann Parteizustellung ergänzend sinnvoll sein, wenn Amtszustellung erfahrungsgemäß langsam ist.

### Schritt 3 – Vollziehungsfrist berechnen

- Beschlussverfügung: Frist beginnt mit Eingang beim Antragstelleranwalt (Zustellung durch das Gericht an Partei).
- Urteilsverfügung: Frist beginnt mit Verkündung.
- Berechnung: § 187 Abs. 1, § 188 Abs. 2 BGB; Monatsfrist endet am selben Datum des Folgemonats.
- Fristende im Fristenbuch und elektronisch sichern.

### Schritt 4 – Strategische Entscheidung Beschlussverfügung

- Parteizustellung rasch beauftragen, da vollständige Kontrolle über Zeitpunkt liegt.
- Günstig: Schuldner kann nicht vor Zustellung reagieren.
- Risiko: Falsche Adresse führt zur gescheiterten Zustellung und Fristversäumnis.

### Schritt 5 – Widerspruchsstrategie antizipieren

- Nach Beschlussverfügung: Schuldner kann Widerspruch einlegen (§ 924 ZPO) und mündliche Verhandlung erzwingen.
- Antragsteller sollte Beweisunterlagen für Haupttermin vorbereiten.
- Nach Urteilsverfügung: Schuldner kann nur Berufung einlegen; Rechtsmittelfristen beachten.

## Typische Fallen

- **Bezeichnung „Beschluss" im Titel, aber nach mündlicher Verhandlung ergangen:** Kommt vor; genauer Blick auf Verfahrensprotokoll notwendig.
- **Urteilsverfügung, Amtszustellung verzögert:** Vollziehungsfrist läuft trotzdem ab Verkündung; nicht auf Gericht verlassen.
- **Widerspruch als Aufhebungsantrag missgedeutet:** Widerspruch führt zur mündlichen Verhandlung, nicht automatisch zur Aufhebung.
- **Doppelzustellung:** Amtszustellung und Parteizustellung bei Urteilsverfügung führen zu Verwirrung über Fristbeginn.

## Vollziehungshandlung nach Zustellung

Nach erfolgreicher Zustellung:
- Bei Unterlassungsverfügung: Vollzug ist die Zustellung selbst; es bedarf keiner weiteren Vollstreckungshandlung.
- Bei Handlungs- oder Herausgabeverfügung: Vollstreckung nach § 887 ff. ZPO separat einzuleiten.
- Zustellurkunde aufbewahren; für späteren Ordnungsmittelantrag (§ 890 ZPO) unverzichtbar.

## Output-Module

- **Differenzierungsmatrix:** Beschluss/Urteil, Zustellungsweg, Fristbeginn, Rechtsmittel.
- **Fristenblatt:** Datum Erlass, Datum Zustellung, Fristende, Vollziehungshandlung.
- **Kurznotiz Mandantenakte:** Entscheidungsform, Zustellauftrag erteilt am, Fristende.
- **Checkliste Parteizustellung** (für Beschlussverfügung): s. evvollzug-neu-001.

## Quellenregel

- [§ 937 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/937.html)
- [§ 922 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/922.html)
- [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html)
- Rechtsprechung nur mit Gericht, Datum, AZ und frei prüfbarer Quelle (openjur.de, bgh.de).
- Keine Kommentar-Blindzitate; bei offenen Fragen zur Gerichtspraxis: Live-Check.

## Anschluss-Skills

- `evvollzug-neu-001` – Vollziehungsfrist und Parteizustellung
- `evvollzug-neu-003` – Zustellung durch Gerichtsvollzieher im IP-Verfahren
- `evvollzug-neu-004` – beA-Zustellung bei einstweiligem Rechtsschutz
- `evvollzug-neu-005` – Ordnungsmittelantrag nach Vollzug
