---
name: beweissicherung-einstweilige-verfuegung
description: "Beweissicherung Einstweilige Verfuegung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beweissicherung Einstweilige Verfuegung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beweissicherung Einstweilige Verfuegung** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beweissicherung` | Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: §§ 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl, Verfahrensablauf. Output: Antrag auf selbständiges Beweisverfahren. Abgrenzung: nicht einstweilige Verfuegung. |
| `chronologie` | Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabellarische Sachverhaltschronologie. Abgrenzung: nicht vollständige Klageschrift. |
| `einstweilige-verfuegung` | Antrag auf einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprüche formulieren. Normen: §§ 935 940 ZPO. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Zuständigkeit, Arrest-Abgrenzung. Output: Antragsschrift einstweilige Verfuegung. Abgrenzung: nicht Berufungsrecht §§ 511 ff. ZPO. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Beweissicherung Einstweilige Verfuegung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beweissicherung`

**Fokus:** Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: §§ 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl, Verfahrensablauf. Output: Antrag auf selbständiges Beweisverfahren. Abgrenzung: nicht einstweilige Verfuegung.

# Aufbewahrungspflicht und Beweissicherung

## Zweck

Erstellung, Aktualisierung oder Aufhebung von Beweissicherungs- und Aufbewahrungsanordnungen für Mandate im deutschen Zivil- und Wirtschaftsrecht. Ziel ist die Vermeidung der Beweisvereitelung (§§ 286, 444 ZPO) und die Sicherung von Beweismitteln für ein bevorstehendes oder laufendes Gerichtsverfahren – ggf. im Wege des Selbständigen Beweisverfahrens (§§ 485 ff. ZPO).

> **Kein US-Legal-Hold-System.** Das deutsche Recht kennt keine umfassende parteiengetriebene Discovery-Hold-Pflicht. Aufbewahrungspflichten entstehen aus gesetzlichen Vorschriften und aus dem Grundsatz der Prozessförderungs­pflicht; eine Vernichtung beweis­erheblicher Dokumente kann Beweisvereitelung darstellen.

## Eingaben

- Aktives Mandat (Slug)
- Modus: `--anordnen`, `--aktualisieren`, `--aufheben`, `--status`
- Betroffene Dokumentenkategorien und Custodians (Personen/Abteilungen, die Dokumente halten)
- Aufbewahrungsanlass: laufendes Verfahren / angekündigtes Verfahren / Behördenanfrage

## Ablauf

### 1. Aufbewahrungspflichten prüfen

**Handels- und steuerrechtliche Pflichtfristen:**
| Kategorie | Frist | Rechtsgrundlage |
|---|---|---|
| Handelsbücher, Inventare, Jahresabschlüsse | 10 Jahre | § 257 Abs. 4 HGB |
| Buchungsbelege | 10 Jahre | § 257 Abs. 4 HGB, § 147 Abs. 3 AO |
| Handels- und Geschäftsbriefe | 6 Jahre | § 257 Abs. 4 HGB |
| Sonstige steuerlich relevante Unterlagen | 6 Jahre | § 147 Abs. 1 Nr. 5 AO |
| Lohnunterlagen (SV-relevant) | 10 Jahre | § 28f Abs. 2 SGB IV |

**Prozessuale Aufbewahrungspflicht:**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Konsequenzen der Beweisvereitelung:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 286 ZPO: Freie Beweiswürdigung kann vernichtungsbedingte Nachteile zulasten der vernichtenden Partei ziehen.
- §§ 339 ff. StGB: Strafbarkeit wegen Beweisvereitelung / Urkundenunterdrückung (§ 274 StGB) bei vorsätzlicher Vernichtung.

### 2. Beweissicherungs-Anordnung erstellen (`--anordnen`)

Inhalt der Anordnung:
- Adressaten (Custodians): Namen, Funktion, Abteilung
- Betroffene Dokumentenarten: E-Mails, Verträge, Buchungsbelege, CAD-Dateien, Systemlogs
- Zeitraum der zu sichernden Unterlagen
- Löschverbot: Ausdrückliches Verbot, betreffende Daten zu löschen, zu überschreiben oder zu ändern
- Aufbewahrungsort und -format
- Überprüfungsintervall
- Kontaktperson für Rückfragen
- Geltungsdauer / Aufhebungsvorbehalt

### 3. Selbständiges Beweisverfahren (§§ 485 ff. ZPO)

Wenn Beweismittel außerhalb des Prozesses gesichert werden müssen (z. B. drohende Veränderung von Sachzustand, Mängel, Bauschäden):

- Antrag nach § 485 ZPO: Beantragung der Beweissicherung durch das Prozessgericht (oder nach § 486 ZPO beim Amtsgericht des Ortes)
- Inhalt: Beweisthema, Beweismittel (Sachverständiger, Augenschein), Benennung des Antragsgegners
- Wirkung: Gutachten bindet das spätere Prozessgericht grundsätzlich (§ 493 ZPO)
- Fristen: §§ 486 Abs. 2, 487 ZPO

### 4. Statusbericht (`--status`)

Tabelle aller aktiven Sicherungsanordnungen im Portfolio mit:
- Mandat-Slug
- Datum der Anordnung
- Betroffene Custodians
- Überprüfungsdatum
- Aufhebungsvoraussetzungen

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 257 HGB; § 147 AO (Aufbewahrungsfristen).
- § 274 StGB (Urkundenunterdrückung), § 339 StGB (Rechtsbeugung, nur für Richter und Beamte).

## Ausgabeformat

### Beweissicherungs-Anordnung

```
BEWEISSICHERUNGS-ANORDNUNG
Mandat: [Slug]
Datum: TT.MM.JJJJ
Erstellt von: [Anwalt]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO / § 203 StGB

──────────────────────────────────────────────
ANORDNUNG ZUR AUFBEWAHRUNG VON UNTERLAGEN
──────────────────────────────────────────────

An: [Name, Funktion, Abteilung]

Betreff: Aufbewahrungspflicht im Zusammenhang mit [Sachverhaltskurzbezeichnung]

Aufgrund eines bevorstehenden / laufenden Rechtsstreits [Aktenzeichen oder Sachverhalt]
ordnen wir an, folgende Unterlagen bis auf Weiteres aufzubewahren:

Betroffene Dokumente:
1. Alle E-Mails und sonstigen Korrespondenzen betreffend [Thema] ab [Datum]
2. Verträge und Anlagen zu [Projekt]
3. [weitere Kategorien]

LÖSCHVERBOT: Es ist untersagt, die oben bezeichneten Unterlagen zu löschen, zu
vernichten, zu überschreiben oder anderweitig unzugänglich zu machen.

Nächste Überprüfung: TT.MM.JJJJ
Kontakt: [Anwalt, Kanzlei, Telefon]
```

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Zu enger Anwendungsbereich:** Custodians und Dokumentenkategorien zu eng gewählt; alle betroffenen Abteilungen und IT-Systeme (E-Mail-Archiv, Cloud-Speicher) einschließen.
- **Datenschutzkollision:** Aufbewahrungspflicht und DSGVO-Löschpflicht können kollidieren; bei Widerspruch gilt prozessuale Sicherungspflicht im Zweifel (vgl. Art. 17 Abs. 3 lit. e DSGVO: Aufbewahrung für Rechtsstreitigkeiten).
- **Selbständiges Beweisverfahren zu spät:** Nach Sachzustandsveränderung ist keine Beweissicherung mehr möglich; § 485 ZPO-Antrag frühzeitig stellen.

<!-- AUDIT 27.05.2026 bundle_040
-->

## 2. `chronologie`

**Fokus:** Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabellarische Sachverhaltschronologie. Abgrenzung: nicht vollständige Klageschrift.

# Sachverhalts-Chronologie

## Triage — kläre vor der Erstellung

1. **Modus:** Arbeitschronologie (intern, vollständig), Schriftsatz-Chronologie (aufbereitet) oder Zeugenchronologie (gefültert)?
2. **Dokumentenbasis:** Liegen die Quellen vor (Verträge, E-Mails, Schriftsätze, Anlagen)?
3. **Zeitraum:** Welcher Zeitraum ist mandatsrelevant — gibt es einen frühesten relevanten Stichtag?
4. **Lücken:** Gibt es bekannte Zeiträume, für die keine Dokumente vorliegen?
5. **Prozessuale Funktion:** Für Sachverhaltsdarstellung (§ 253 ZPO), Zeugenvernehmung (§§ 373 ff. ZPO) oder Berufungsbegründung (§ 520 Abs. 3 ZPO)?

## Zentrale Normen
- § 253 Abs. 2 Nr. 1 ZPO (Anforderungen an die Klageschrift — vollständiger Sachvortrag)
- § 138 ZPO (Erklärungspflicht der Parteien — Vollständigkeit und Wahrheitspflicht)
- § 373 ff. ZPO (Zeugenbeweis — Grundlage der Zeugenchronologie)
- § 520 Abs. 3 ZPO (Berufungsbegründung — tatsächliche Angaben)
- § 286 ZPO (Freie Beweiswuerdigung — Chronologie als Hilfsmittel)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Aufbau einer mandatsbezogenen Sachverhalts-Chronologie aus vorliegenden Dokumenten, Schriftsätzen, Verträgen, E-Mails und Anlagen. Die Chronologie dient als Grundlage für Sachverhaltsdarstellungen im Schriftsatz (§ 253 Abs. 2 Nr. 1 ZPO), Zeugenvernehmungsvorbereitung (§§ 373 ff. ZPO), Berufungsbegründung (§ 520 Abs. 3 ZPO) und interne Mandatsbriefings.

Drei Modi:
- **Arbeitschronologie** – intern, vollständig, mit Lückenmarkierungen
- **Sachverhaltsdarstellungs-Chronologie** – aufbereitet für den Schriftsatz, urteilsstilgerecht
- **Zeugenchronologie** – gefiltert auf einen bestimmten Zeugen für Vernehmungsvorbereitung

## Eingaben

- Aktives Mandat (Slug)
- Hochgeladene Dokumente: Verträge, Korrespondenz, E-Mails, Protokolle, Rechnungen, Sachverständigengutachten, Gerichtsentscheidungen
- Wahl des Modus: `--arbeits` | `--sachverhalt` | `--zeuge=[Name]`
- Optional: bekannte Schlüsseldaten (z. B. Vertragsschluss, Fälligkeitsdatum, Kündigungserklärung)

## Ablauf

1. **Dokumente parsen:** Alle hochgeladenen Dateien auf datierte Ereignisse scannen. Datum, Uhrzeit (soweit angegeben), Ereignisbeschreibung, Quelle (Dokumentenbezeichnung, Anlage-Nr.) und beteiligte Personen extrahieren.

2. **Deduplizierung:** Gleiche Ereignisse aus verschiedenen Quellen zusammenführen; Widersprüche markieren als `[WIDERSPRUCH: Quelle A gibt X an, Quelle B gibt Y an]`.

3. **Mandatstheorien-Tagging:** Jedes Ereignis nach Relevanz für die Mandatstheorie markieren:
 - 🔑 Kernereig­nis (unmittelbar anspruchsbegründend oder -ausschließend)
 - ⚠️ Risikopunkt (könnte gegen Mandantin sprechen)
 - 📎 Hintergrundinformation
 - ❓ Ungeklärt / Beleg fehlt

4. **Lücken identifizieren:** Zeiträume ohne belegte Ereignisse und inhaltliche Lücken (z. B. fehlende Zugangsbestätigung, unklare Übergabe) als `[LÜCKE: Zeitraum MM/JJJJ bis MM/JJJJ – kein Beleg]` markieren.

5. **Modus anwenden:**
 - *Arbeitschronologie:* Vollständige Liste mit Quellenangaben und Anmerkungen.
 - *Sachverhaltsdarstellung:* Fließtext im Urteilsstil, Ereignisse in der dritten Person, Beweisquellen als Fußnoten.
 - *Zeugenchronologie:* Nur Ereignisse mit Beteiligung des Zeugen; Ergänzung um mögliche Wissenslücken des Zeugen.

6. **Versionierung:** Neue Chronologien als `chronology-v[N].md` im Mandatsordner speichern.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

### Arbeitschronologie (Tabelle)

| Datum | Ereignis | Quelle / Anlage | Beteiligte | Tag | Anmerkung |
|---|---|---|---|---|---|
| 12.03.2022 | Abschluss Werkvertrag | Anlage K1 (Vertrag v. 12.03.2022) | Kl., Bekl. | 🔑 | Unterschriften vorhanden |
| 15.04.2022 | Fristsetzung Mängelbeseitigung (Schreiben Kl.) | Anlage K3 | Kl. → Bekl. | 🔑 | Zugang streitig |
| [LÜCKE] | Zeitraum 16.04. – 30.05.2022 | – | – | ❓ | Keine Korrespondenz vorhanden |

### Sachverhaltsdarstellung (Fließtext-Modus)

> Am 12. März 2022 schlossen die Parteien einen Werkvertrag über die Erstellung einer Software (Anlage K1). Mit Schreiben vom 15. April 2022, dem Beklagten zugegangen am 17. April 2022 (Anlage K2: Rückschein), setzte die Klägerin eine Nachfrist zur Mängelbeseitigung bis zum 1. Mai 2022.
>
> *Beweis für Zugang: Zeugnis des Herrn Anton Mayer, [Anschrift]; Anlage K2 (Zustellungsnachweis).*

## Risiken / typische Fehler

- **Unklarer Zugangszeitpunkt:** Zugangsnachweis für Mahnungen und Fristsetzungen ist entscheidend für Verzugsbeginn (§ 286 Abs. 1 BGB); fehlende Belege zwingend als Lücke markieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Veraltete Chronologie:** Nach jedem Mandat-Update (`/mandat-update`) die Chronologie ergänzen; veraltete Versionen archivieren.
- **Zeugenchronologie zu weit gefasst:** Nur mandatsrelevante Ereignisse einbeziehen; nicht alle Ereignisse, an denen der Zeuge beteiligt war.
- **Datenschutz:** Personenbezogene Daten Dritter nur soweit erforderlich; DSGVO-Minimierungsgrundsatz (Art. 5 Abs. 1 lit. c DSGVO) beachten.

## 3. `einstweilige-verfuegung`

**Fokus:** Antrag auf einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprüche formulieren. Normen: §§ 935 940 ZPO. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Zuständigkeit, Arrest-Abgrenzung. Output: Antragsschrift einstweilige Verfuegung. Abgrenzung: nicht Berufungsrecht §§ 511 ff. ZPO.

# Einstweilige Verfügung – §§ 935, 940 ZPO

## Zweck

Dieser Skill begleitet das Verfahren der einstweiligen Verfügung als Instrument des vorläufigen
Rechtsschutzes für nicht auf Geld gerichtete Ansprüche. Typische Mandate: wettbewerbsrechtliche
Unterlassungsverfügungen (§ 935 ZPO), Sicherungsverfügungen bei drohender Beweisvereitelung
oder Vermögensverschiebung, Regelungsverfügungen (§ 940 ZPO) bei Arbeitsverhältnissen,
Presserecht oder Urheberrecht. Auf Antragsgegnerseite: Schutzschrift, Widerspruch, Berufung,
Schadensersatz nach § 945 ZPO.

## Eingaben

Das Modell benötigt:

1. **Anspruchsgrundlage**: materiell-rechtlicher Anspruch (z. B. § 8 UWG, § 97 UrhG,
 § 1004 BGB analog, §§ 823, 1004 BGB)
2. **Dringlichkeit**: Wann hat der Antragsteller Kenntnis erlangt? (1-Monats-Frist im UWG;
 sonstige Materie: je nach Eilbedürftigkeit)
3. **Glaubhaftmachungsmittel**: eidesstattliche Versicherung, Urkunden, Screenshots,
 Sachverständigengutachten
4. **Gericht**: zuständiges LG (sachliche Zuständigkeit bei Streitwert > EUR 10.000 i. d. F. seit 1.1.2026;
 UWG: § 14 UWG; Veröffentlichungsstreitigkeiten ohne Rücksicht auf Streitwert ausschließlich LG § 71 Abs. 2 Nr. 7 GVG; spezialisierte Pressekammern § 72a Abs. 1 Nr. 5 GVG)
5. **Gegnerische Schutzschrift**: liegt eine bekannte Schutzschrift im ZSSR vor?

## Rechtlicher Rahmen

### Normen

- **§ 935 ZPO** – Sicherungsverfügung: Gefährdung der Verwirklichung eines Rechts durch
 Veränderung des bestehenden Zustands
- **§ 940 ZPO** – Regelungsverfügung: zur Abwendung wesentlicher Nachteile oder Verhinderung
 drohender Gewalt oder aus anderen Gründen nötig
- **§ 936 ZPO** – Anwendung der Vorschriften über einstweiligen Arrest (§§ 916 ff. ZPO)
- **§ 937 ZPO** – Zuständigkeit: Gericht der Hauptsache; bei Dringlichkeit Gericht des
 Aufenthaltsortes
- **§ 940a ZPO** – Besondere Voraussetzungen bei Räumungsverfügungen
- **§ 942 ZPO** – Zuständigkeit des Amtsgerichts bei besonderer Dringlichkeit
- **§ 943 ZPO** – Vollziehung der einstweiligen Verfügung (innerhalb 1 Monat ab Erlass)
- **§ 944 ZPO** – Vorabentscheidung des Gerichts
- **§ 945 ZPO** – Schadensersatzpflicht des Antragstellers bei von Anfang an ungerechtfertigter
 oder aufgehobener Verfügung (str.: Gefährdungshaftung, unabh. von Verschulden)
- **§ 945a ZPO** – Schutzschriftenregister ZSSR (Einreichung elektronisch; 6 Monate gültig)
- **§ 294 ZPO** – Glaubhaftmachung (kein Vollbeweis; eidesstattliche Versicherung ausreichend)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Zum Verfügungsgrund im UWG-Recht; die Dringlichkeitsvermutung des § 12 Abs. 1 UWG entfällt,
 wenn der Antragsteller durch eigenes Zögern zeigt, dass er die Sache selbst nicht für dringlich
 hält; eigenes widersprüchliches Verhalten (Selbstwiderlegung der Dringlichkeit) begründet die
 Unzulässigkeit des Antrags.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Gebietet Art. 103 Abs. 1 GG, dem Antragsgegner vor Erlass einer einstweiligen Verfügung
 rechtliches Gehör zu gewähren, sofern dies ohne Rechtsnachteile für den Antragsteller möglich
 ist; nur bei echter Dringlichkeit ist eine Beschlussverfügung ohne Anhörung verfassungsgemäß.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 der Antragsteller muss die Hauptsacheentscheidung vorwegnehmen; bei Leistungsverfügungen
 (Erfüllungsverfügungen) gilt ein strengerer Maßstab als bei bloßen Unterlassungsverfügungen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 der Schadensersatzanspruch entsteht verschuldensunabhängig; erforderlich ist nur, dass die
 Verfügung von Anfang an ungerechtfertigt war oder aufgehoben wird.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Prüfung Verfügungsanspruch**: Materiell-rechtlicher Anspruch mit überwiegender
 Wahrscheinlichkeit glaubhaft? Anspruchsgrundlage, Tatbestand, keine offensichtlichen
 Einwendungen.
2. **Prüfung Verfügungsgrund**:
 - § 935 ZPO: Gefährdung durch Veränderung des bestehenden Zustands
 - § 940 ZPO: Notwendigkeit zur Abwendung wesentlicher Nachteile
 - UWG: Dringlichkeitsvermutung (§ 12 Abs. 1 UWG), aber Selbstwiderlegung prüfen
 (BGH – "Fischdose")
3. **Glaubhaftmachung** (§ 294 ZPO): Eidesstattliche Versicherung des Antragstellers
 über Sachverhalt und Kenntnis; Urkunden, Screenshots mit Datumsstempel beifügen.
4. **Antragstellung** beim zuständigen LG:
 - Beschlussantrag (ohne mündliche Verhandlung; nur bei echter Dringlichkeit;
 BVerfG – "Waffengleichheit" beachten)
 - Urteilsantrag nach mündlicher Verhandlung (Regelfall § 937 Abs. 2 ZPO)
5. **Vollziehung** (§ 929 Abs. 2 ZPO analog): Innerhalb 1 Monat ab Erlass zustellen lassen;
 bei Beschlussverfügung: Zustellung durch Gerichtsvollzieher oder per Anwaltszustellung.
6. **Abschlussschreiben** an Antragsgegner: Aufforderung zur Abgabe einer Hauptsache-
 Unterlassungserklärung, damit kein Hauptsacheverfahren notwendig wird.
7. **Widerspruch des Gegners** (§ 924 ZPO analog): Führt zur mündlichen Verhandlung;
 Gericht hebt Verfügung auf oder bestätigt sie (§ 925 ZPO).
8. **Schutzschrift** (§ 945a ZPO) auf Antragsgegnerseite: Einreichung ins ZSSR
 (www.zssr.de); Inhalt: Sachverhalt, Rechtsausführungen gegen Verfügungsanspruch und
 Verfügungsgrund, Beweismittel; 6-Monatsgültigkeit.

## Ausgabeformat

- **Antragsschrift einstweilige Verfügung** (vollständig; Verfügungsanspruch, Verfügungsgrund,
 Glaubhaftmachungsmittel, Anträge)
- **Eidesstattliche Versicherung** (Entwurf für Antragsteller)
- **Schutzschrift** (für Antragsgegner; Gliederung: Sachverhalt → Verfügungsanspruch fehlt →
 Verfügungsgrund fehlt → Beweisangebote)
- **Widerspruchsschriftsatz** (§ 924 ZPO)
- **Rechtliches Memo** zur Erfolgsaussicht und zu § 945 ZPO-Risiken

## Beispiel

**Sachverhalt**: Modehändler M betreibt einen Webshop und verletzt die Marke der Klägerin K
durch identische Verwendung des Wortzeichens. K hat am 15.05.2025 Kenntnis erhalten. K
beabsichtigt, am 05.06.2025 eine einstweilige Verfügung beim LG Hamburg zu beantragen.

**Prüfung (Gutachtenstil)**:

*Verfügungsanspruch (§ 935 ZPO)*: K hat gegen M einen markenrechtlichen Unterlassungsanspruch
nach § 14 Abs. 2 Nr. 1, Abs. 5 MarkenG (identische Kollision). Glaubhaftmachung durch
Screenshots des Webshops (mit Datum) und eidesstattliche Versicherung der Geschäftsführerin.
Verfügungsanspruch überwiegend wahrscheinlich.

*Verfügungsgrund (§ 935 ZPO)*: Dringlichkeit nach § 12 Abs. 1 UWG analog; Kenntnis seit
15.05.2025; Antragstellung am 05.06.2025 (21 Tage). Dringlichkeit gewahrt; keine
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Gehörsproblem*: Beschlussverfügung ohne Anhörung nur bei tatsächlicher Dringlichkeit zulässig
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Urteilsverfügung nach mündlicher Verhandlung beantragen, um § 945 ZPO-Risiko zu minimieren.

## Risiken und typische Fehler

- **Selbstwiderlegung der Dringlichkeit**: Antragsteller hat seit mehr als 1 Monat Kenntnis
 und wartet → Verfügungsgrund entfällt (BGH – "Fischdose").
- **§ 945 ZPO-Haftung**: Antragsteller haftet verschuldensunabhängig, wenn Verfügung von
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Abwägung des Prozessrisikos vor Antragstellung!
- **Fehlende Vollziehung** (§ 929 Abs. 2 ZPO analog): Beschlussverfügung nicht binnen 1 Monat
 zugestellt → Verfügung wird wirkungslos; neue Antragstellung erforderlich.
- **Zu weit gefasste Verfügungsanträge**: Klageantrag muss hinreichend bestimmt sein (§ 253
 Abs. 2 Nr. 2 ZPO); Vorsicht bei "insbesondere"-Anträgen.
- **Kein Schutz durch Schutzschrift**: Schutzschrift läuft nach 6 Monaten ab (§ 945a Abs. 3
 ZPO); rechtzeitige Verlängerung beachten.
- **Berufsrecht**: § 43a Abs. 2 BRAO – keine Interessenkollision bei paralleler Abmahnung
 mehrerer Mitbewerber; § 203 StGB – Mandantendaten sichern.

## Quellenpflicht

Jede Aussage zu Verfügungsanspruch, Verfügungsgrund, Glaubhaftmachung und § 945 ZPO-Haftung
ist nach `references/zitierweise.md` zu belegen. BGH-Urteile mit vollem Zitat (Datum, Az.,
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
mit Bearbeiter, Werk, Aufl., §, Rn. Streitstände (insbes. zu § 945 ZPO Verschulden) offen
darstellen.
