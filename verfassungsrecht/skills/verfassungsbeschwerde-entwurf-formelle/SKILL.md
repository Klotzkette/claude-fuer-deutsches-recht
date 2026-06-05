---
name: verfassungsbeschwerde-entwurf-formelle
description: "Verfassungsbeschwerde Entwurf Formelle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verfassungsbeschwerde Entwurf Formelle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verfassungsbeschwerde Entwurf Formelle** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verfassungsbeschwerde-entwurf` | Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster: Beschwerdeführerbefugnis Beschwerdeobjekt Rechtswegerschoepfung Frist Grundrechtsverletzung. Output: Verfassungsbeschwerde-Schriftsatz mit Zulässigkeit Begründung. Abgrenzung: nicht für abstrakte oder konkrete Normenkontrolle. |
| `formelle-verfassungsmaessigkeit` | Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG Verfahren Art. 76-78 GG Ausfertigung Art. 82 GG. Output: Formelle Prüfmemo mit Ergebnis. Abgrenzung: nicht für materielle Verfassungsmäßigkeit (grundrechtsprüfung). |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung Subsidiaritaet Sperrwirkung. Output: Kompetenzprüfmemo Ergebnis mit Fundstellen. Abgrenzung: nicht für formelles Gesetzgebungsverfahren (formelle-verfassungsmäßigkeit). |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Verfassungsbeschwerde Entwurf Formelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verfassungsbeschwerde-entwurf`

**Fokus:** Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster: Beschwerdeführerbefugnis Beschwerdeobjekt Rechtswegerschoepfung Frist Grundrechtsverletzung. Output: Verfassungsbeschwerde-Schriftsatz mit Zulässigkeit Begründung. Abgrenzung: nicht für abstrakte oder konkrete Normenkontrolle.

# Verfassungsbeschwerde-Entwurf

## Fachkern: Verfassungsbeschwerde-Entwurf
- **Spezialgegenstand:** Verfassungsbeschwerde-Entwurf wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Disclaimer (Schlüsselstelle, mehrfach)

Die Verfassungsbeschwerde ist der zentrale Rechtsbehelf zum BVerfG, mit existentiellen Folgen für Mandanten. Sie unterliegt strengen Zulässigkeitsanforderungen, der Monatsfrist nach § 93 Abs. 1 BVerfGG und hohen Substantiierungsanforderungen (§ 23 Abs. 1, § 92 BVerfGG). Dieser Entwurf ist **kein Ersatz** für die Bearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Vor jeder Einreichung ist eine fachanwaltliche Prüfung dringend erforderlich.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Pinpoint pro tragender Aussage.

## Zulässigkeitsprüfung

Die Verfassungsbeschwerde durchläuft eine **strenge Zulässigkeitsprüfung**. Schon ein einziger Mangel führt zur Verwerfung als unzulässig.

### 1. Zuständigkeit des BVerfG (Art. 93 Abs. 1 Nr. 4a GG, § 90 BVerfGG)

Verfassungsbeschwerde gegen Akte der **deutschen öffentlichen Gewalt**.

### 2. Beschwerdefähigkeit

- **Natürliche Personen:** alle Träger von Grundrechten (Art. 19 Abs. 3 GG analog).
- **Juristische Personen des Privatrechts:** soweit das Grundrecht ihrem Wesen nach auf sie anwendbar ist (Art. 19 Abs. 3 GG).
- **Inländische juristische Personen** sowie nach BVerfG-Rspr. auch **juristische Personen aus EU-Mitgliedstaaten** (Pinpoint live nachsehen).
- **Juristische Personen des öffentlichen Rechts:** grundsätzlich **nicht** beschwerdefähig (Confusio); Ausnahmen: Universitäten (Art. 5 Abs. 3 GG), Religionsgemeinschaften (Art. 4 GG), Rundfunkanstalten (Art. 5 Abs. 1 S. 2 GG).

### 3. Beschwerdegegenstand

Akt der **deutschen öffentlichen Gewalt:**

- Gerichtliche Entscheidungen (Urteile, Beschlüsse) — häufigster Fall.
- Verwaltungsakte.
- Gesetze (Rechtssatzverfassungsbeschwerde).
- Realakte.

**Ausschluss:** Akte ausländischer und supranationaler Organe (mit Ausnahme der "Solange-Rechtsprechung" zum Unionsrecht).

### 4. Beschwerdebefugnis

Der Beschwerdeführer muss schlüssig darlegen, durch den angegriffenen Akt **in eigenen Grundrechten oder grundrechtsgleichen Rechten** möglicherweise verletzt zu sein:

- **Selbst** — eigene Grundrechtsbetroffenheit (nicht Popularklage).
- **Gegenwärtig** — schon eingetreten oder mit hinreichender Sicherheit zu erwarten.
- **Unmittelbar** — ohne weiteren Vollzugsakt; bei Gesetzen erfordert dies regelmäßig, dass der Vollzug auf einen Verwaltungsakt erst gewartet werden kann; bei untergesetzlichen Normen Unmittelbarkeit nur, wenn die Norm ohne Umsetzungsakt direkt wirkt.

**Gegenwärtig + unmittelbar bei Gesetzen:** Ausnahmen bei Vorbereitungspflichten oder bei Strafnormen, deren Vollzug nicht abgewartet werden kann (Risiko strafrechtlicher Verfolgung).

### 5. Rechtswegerschöpfung (§ 90 Abs. 2 S. 1 BVerfGG)

- Vor Anrufung des BVerfG muss der **gesamte fachgerichtliche Rechtsweg** ausgeschöpft sein.
- Erfasst alle Instanzen einschließlich Nichtzulassungsbeschwerde, Revision usw.
- Bei Rechtssatzverfassungsbeschwerde gegen ein Gesetz: regelmäßig kein Rechtsweg vorhanden, daher entfällt die Erschöpfung; ggf. **vorrangige Subsidiarität** beachten.

### 6. Subsidiarität (über Rechtswegerschöpfung hinaus)

Beschwerdeführer muss alle ihm zumutbaren Möglichkeiten genutzt haben, eine **Grundrechtsverletzung schon vor den Fachgerichten** zu rügen. Dazu gehört insbesondere, **verfassungsrechtliche Argumente bereits dort vorzutragen** (Rügeobliegenheit).

Bei Gesetzen ohne Rechtsweg: zumutbar muss der Bürger ggf. eine Feststellungsklage erheben, in deren Rahmen die Norm inzident geprüft wird.

### 7. Frist (§ 93 BVerfGG)

- **Einzelakte:** ein Monat ab Zustellung oder Bekanntgabe (§ 93 Abs. 1 BVerfGG).
- **Gesetze und sonstige Rechtsnormen:** ein Jahr nach Inkrafttreten (§ 93 Abs. 3 BVerfGG).
- **Wiedereinsetzung in den vorigen Stand** möglich (§ 93 Abs. 2 BVerfGG, strenge Voraussetzungen).

### 8. Form und Substantiierung (§ 23 Abs. 1, § 92 BVerfGG)

- **Schriftform** mit eigenhändiger Unterschrift (oder elektronisch nach § 23a BVerfGG).
- **Bezeichnung des angegriffenen Hoheitsakts.**
- **Bezeichnung des verletzten Grundrechts/grundrechtsgleichen Rechts.**
- **Vortrag der Tatsachen,** aus denen sich die Verletzung ergibt.
- **Vortrag zum Rechtsweg** und zur Erschöpfung.
- Hohe Anforderungen: Pinpoint-Verweise auf BVerfG-Rspr. erwartet, soweit einschlägig.

### 9. Allgemeines Rechtsschutzbedürfnis

Regelmäßig zu bejahen, wenn die Voraussetzungen 1–8 erfüllt sind. Ausnahmen bei Erledigung (dann ggf. Fortsetzungsfeststellungsinteresse, insbesondere bei Wiederholungsgefahr oder tiefen Eingriffen).

## Annahme zur Entscheidung (§ 93a BVerfGG)

Die Verfassungsbeschwerde wird nur **angenommen**, wenn:

- ihr **grundsätzliche verfassungsrechtliche Bedeutung** zukommt (§ 93a Abs. 2 lit. a BVerfGG), **oder**
- sie zur Durchsetzung der vom BVerfG in seiner Rechtsprechung anerkannten Grundrechte angezeigt ist; das ist insbesondere der Fall, wenn dem Beschwerdeführer durch die Versagung der Entscheidung **ein besonders schwerer Nachteil** entsteht (§ 93a Abs. 2 lit. b BVerfGG).

## Aufbau einer Verfassungsbeschwerde

```
An das Bundesverfassungsgericht
Schlossbezirk 3
76131 Karlsruhe

In dem Verfassungsbeschwerdeverfahren
des Herrn/der Frau [Name]
[Anschrift]
- Beschwerdeführer/in -

Verfahrensbevollmächtigte:
Rechtsanwältin/Rechtsanwalt [Name]
[Kanzleianschrift]

gegen
[Bezeichnung der angegriffenen Maßnahme — z. B. Urteil des BGH vom ... — Az. ... ; Beschluss des OLG ... ; § ... XYZ-Gesetz]

wegen Verletzung von Art. ___ GG

erhebe ich namens und in Vollmacht des Beschwerdeführers/der Beschwerdeführerin

VERFASSUNGSBESCHWERDE

und beantrage,
1. festzustellen, dass [angegriffener Akt] den Beschwerdeführer / die Beschwerdeführerin in seinen / ihren Grundrechten aus Art. ___ GG verletzt;
2. den angegriffenen Akt aufzuheben und die Sache zur erneuten Entscheidung zurückzuverweisen [bei Gerichtsentscheidungen];
 bzw. die angegriffene Norm für nichtig zu erklären [bei Rechtssatzverfassungsbeschwerde];
3. die Kosten des Verfahrens und die notwendigen Auslagen des Beschwerdeführers / der Beschwerdeführerin der Staatskasse aufzuerlegen.

A. Sachverhalt
[Sachverhalt mit Aktenbezug. Pinpoint zu jeder tatsächlichen Aussage aus den Akten.]

B. Zulässigkeit
I. Zuständigkeit
II. Beschwerdefähigkeit
III. Beschwerdegegenstand
IV. Beschwerdebefugnis
 1. Selbst
 2. Gegenwärtig
 3. Unmittelbar
V. Rechtswegerschöpfung (§ 90 Abs. 2 BVerfGG)
VI. Subsidiarität
VII. Frist (§ 93 BVerfGG)
VIII. Substantiierung (§ 23 Abs. 1, § 92 BVerfGG)
IX. Rechtsschutzbedürfnis

C. Begründetheit
Die Verfassungsbeschwerde ist begründet. [Angegriffener Akt] verletzt den Beschwerdeführer in seinem Grundrecht aus Art. ___ GG.

I. Schutzbereich
[Aufruf Skill grundrechtsprüfung]

II. Eingriff

III. Verfassungsrechtliche Rechtfertigung
 1. Schranke
 2. Verhältnismäßigkeit
 [Aufruf Skill verhältnismäßigkeit]
 3. Sonstige Schranken-Schranken

IV. Spezifische verfassungsrechtliche Verstöße
[BVerfG-Pinpoints konkret]

D. Annahmegründe (§ 93a Abs. 2 BVerfGG)
[Begründung grundsätzliche verfassungsrechtliche Bedeutung oder schwerer Nachteil]

E. Eilantrag (§ 32 BVerfGG)
[optional, falls einstweilige Anordnung erforderlich]

Anlagen
1. Vollmacht
2. Kopie des angegriffenen Akts
3. Kopien aller fachgerichtlichen Entscheidungen
4. ...

[Ort, Datum]
[Unterschrift Rechtsanwalt/Rechtsanwältin]
```

## Aktuelle Rechtsprechung & Leitsätze

Stand 05/2026. Vor Verwendung im Schriftsatz Pinpoint (Rn., Tenor) auf [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) verifizieren.

- BVerfG, Beschl. v. 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Eingriffsschwellen bei polizeirechtlicher Datenerhebung; Übergangsfortgeltung bis 31.12.2025; methodisch Pinpoint für Verhältnismäßigkeit/Wesentlichkeit.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 2466/19 (Trojaner I) — präventiv-polizeirechtliche Quellen-TKÜ / Online-Durchsuchung, PolG NRW im Wesentlichen verfassungskonform.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 180/23 (Trojaner II) — strafprozessuale Quellen-TKÜ teilweise nichtig (Niedrig-Strafrahmen).
- BVerfG, Beschl. v. 24.03.2021 — 1 BvR 2656/18 u. a. (Klimabeschluss) — intertemporale Freiheitssicherung; Art. 20a GG; subjektive Schutzpflicht.

## Zentrale Normen (Paragrafenkette)

§§ 90-95 BVerfGG (Verfassungsbeschwerde: Zulässigkeit, Frist, Annahme) — § 93a BVerfGG (Annahme zur Entscheidung) — § 32 BVerfGG (Einstweilige Anordnung) — §§ 1-3 BVerfGG (Zustaendigkeit BVerfG)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Praxishinweise

- **Vollmacht beifügen** — nach § 22 BVerfGG.
- **Eilantrag nach § 32 BVerfGG** parallel erwägen, wenn die Hauptsacheentscheidung nicht abgewartet werden kann.
- **Kostenerstattung:** § 34a BVerfGG bei Erfolg.
- **Frist striktest** überwachen — Wiedereinsetzung bei Verschulden in eigenen Reihen kaum möglich.

## Disclaimer-Wiederholung (vor jedem Output)

Eine Verfassungsbeschwerde ist eine der anspruchsvollsten Schriftsätze der deutschen Rechtsordnung. Dieser Entwurf ist **kein Ersatz** für die anwaltliche Mandatsbearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Insbesondere die Substantiierungsanforderungen und die strenge Subsidiarität führen in der Praxis zu hohen Verwerfungsquoten.

## 2. `formelle-verfassungsmaessigkeit`

**Fokus:** Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG Verfahren Art. 76-78 GG Ausfertigung Art. 82 GG. Output: Formelle Prüfmemo mit Ergebnis. Abgrenzung: nicht für materielle Verfassungsmäßigkeit (grundrechtsprüfung).

# Formelle Verfassungsmäßigkeit prüfen

## Fachkern: Formelle Verfassungsmäßigkeit prüfen
- **Spezialgegenstand:** Formelle Verfassungsmäßigkeit prüfen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Disclaimer

Die formelle Verfassungsmäßigkeit kann im Streitfall nur durch das BVerfG verbindlich geklärt werden (Verwerfungsmonopol Art. 100 Abs. 1 GG). Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Jede Aussage benötigt BVerfG-Pinpoint (Az. + Rn. + URL).

## Prüfungsschritte

### Schritt 1 — Verfahren (Art. 76–82 GG)

#### 1a. Einbringung (Art. 76 GG)

- **Initiativrecht:** Bundesregierung, Bundestag (aus der Mitte, § 76 GOBT: Fraktion oder 5 % der Abgeordneten), Bundesrat.
- **Erster Durchgang:** Bei Initiative aus Bundesregierung oder Bundesrat ist die jeweils andere Seite zur Stellungnahme zu hören (Art. 76 Abs. 2, 3 GG).

#### 1b. Drei Lesungen im Bundestag (§§ 78–86 GOBT)

- **Erste Lesung:** Aussprache (oder Überweisung ohne Aussprache), Überweisung an den federführenden Ausschuss.
- **Zweite Lesung:** Beratung auf Grundlage der Ausschussempfehlung, Einzelabstimmung über Änderungsanträge.
- **Dritte Lesung:** Schlussabstimmung; nur noch Änderungsanträge zu in zweiter Lesung beschlossenen Änderungen.

#### 1c. Bundesrat (Art. 77, 78 GG)

Erste Frage: **Zustimmungs- oder Einspruchsgesetz?**

- **Zustimmungsgesetz** — wenn das GG dies ausdrücklich anordnet (z. B. Art. 84 Abs. 1 GG bei Eingriff in Landesverwaltung, Art. 105 Abs. 3 GG bei Steuern, deren Aufkommen den Ländern zufließt). Ohne Zustimmung des Bundesrats kommt das Gesetz **nicht zustande**.
- **Einspruchsgesetz** — Regelfall. Bundesrat kann nur Einspruch erheben; der Bundestag kann diesen mit absoluter (bzw. Zweidrittel-)Mehrheit zurückweisen (Art. 77 Abs. 4 GG).

**Vermittlungsausschuss** (Art. 77 Abs. 2 GG): Beide Häuser können ihn anrufen; Voraussetzung für Bundesrats-Einspruch in der Regel.

#### 1d. Ausfertigung (Art. 82 Abs. 1 S. 1 GG)

- Ausfertigung durch den **Bundespräsidenten**.
- Prüfungsrecht streitig: hM beschränkt auf formelles und evident materielles Verfassungsrecht; der Bundespräsident hat materielle Prüfungskompetenz nur bei offensichtlichen, schwerwiegenden Verstößen.
- **Gegenzeichnung** (Art. 58 GG): erforderlich.

#### 1e. Verkündung (Art. 82 Abs. 1 S. 1 GG)

- Verkündung im **Bundesgesetzblatt** (BGBl. Teil I bei materiellen Gesetzen).
- **Inkrafttreten** (Art. 82 Abs. 2 GG): der vom Gesetz selbst bestimmte Zeitpunkt; sonst der vierzehnte Tag nach Ablauf des Tages der Verkündung.

### Schritt 2 — Bestimmtheitsgebot

Aus dem **Rechtsstaatsprinzip** (Art. 20 Abs. 3 GG) folgt:

- **Normklarheit** — der Bürger muss die Rechtslage erkennen können.
- **Vorhersehbarkeit** — Eingriffsvoraussetzungen müssen vorhersehbar sein.
- **Justiziabilität** — die Anwendung muss gerichtlich überprüfbar sein.

**Stufenverhältnis:** Je intensiver der Grundrechtseingriff, desto höher die Bestimmtheitsanforderungen. Bei strafrechtlichen Normen verschärft durch Art. 103 Abs. 2 GG (`nullum crimen sine lege`).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 3 — Zitiergebot (Art. 19 Abs. 1 S. 2 GG)

- **Geltung:** bei Grundrechtseinschränkungen durch oder aufgrund eines Gesetzes.
- **Pflicht:** das einschränkende Gesetz muss das eingeschränkte Grundrecht unter Angabe des Artikels nennen.
- **Folge bei Verstoß:** Nichtigkeit der Norm.
- **Reichweite (Auslegung BVerfG):** Zitiergebot gilt **nur** für nachkonstitutionelle, gezielt grundrechtseinschränkende Gesetze. Vorkonstitutionelle Gesetze und solche, die Grundrechte nur ausgestalten (z. B. Eigentumsausgestaltung Art. 14 Abs. 1 S. 2 GG), unterliegen ihm nicht.

**Praktische Anwendung:** Im Eingangsabschnitt des Gesetzes (vor § 1) findet sich häufig die Formulierung "Das Grundrecht auf … (Art. … GG) wird durch dieses Gesetz eingeschränkt."

### Schritt 4 — Wesentlichkeitstheorie und Parlamentsvorbehalt

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kerngedanke:** Wesentliche Entscheidungen muss der Gesetzgeber selbst treffen; sie dürfen nicht der Exekutive (Verordnungsgeber, Verwaltung) überlassen werden.

**Wesentlich** im verfassungsrechtlichen Sinn ist eine Entscheidung insbesondere:

- Grundrechtsrelevanz (je grundrechtsintensiver, desto wesentlicher)
- Politische Bedeutung
- Eingriffsintensität gegenüber Bürger und Gemeinwesen

**Konsequenz:** Der Gesetzgeber muss die wesentlichen Voraussetzungen, Maßstäbe und Verfahrensregeln **selbst** im förmlichen Gesetz festlegen — keine Generalklauseln, keine pauschale Delegation an die Exekutive.

**Verhältnis zu Art. 80 Abs. 1 S. 2 GG** (Inhalt, Zweck und Ausmaß der Verordnungsermächtigung): das Zitiergebot des Art. 80 ist ein Sonderfall der Wesentlichkeitstheorie für Rechtsverordnungen.

### Schritt 5 — Allgemeinheit des Gesetzes (Art. 19 Abs. 1 S. 1 GG)

- **Einzelfallgesetz-Verbot:** Ein Grundrecht einschränkendes Gesetz muss "allgemein und nicht nur für den Einzelfall" gelten.
- **Folge bei Verstoß:** Verfassungswidrigkeit.

### Schritt 6 — Wesensgehaltsgarantie (Art. 19 Abs. 2 GG)

- In keinem Fall darf ein Grundrecht in seinem **Wesensgehalt** angetastet werden.
- Diese "Schranken-Schranke" bildet die absolute Untergrenze jeder Grundrechtseinschränkung.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 76-78 GG (Gesetzgebungsverfahren) — Art. 79 GG (Verfassungsaenderung) — Art. 19 Abs. 1 Satz 2 GG (Zitiergebot) — Art. 80 GG (Verordnungsermaechtigung, formelle Anforderungen) — Art. 82 GG (Ausfertigung und Verkuendung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Format

```
FORMELLE VERFASSUNGSMÄSSIGKEIT

Prüfungsgegenstand: <Gesetz / Norm>

1. Verfahren
 - Initiativrecht (Art. 76 GG): ___
 - Erste Lesung: ___
 - Ausschussüberweisung: ___
 - Zweite Lesung: ___
 - Dritte Lesung / Schlussabstimmung: ___
 - Bundesrat (Art. 77, 78 GG): [Zustimmung / Einspruch] — Ergebnis: ___
 - Vermittlungsausschuss: ___
 - Ausfertigung (Art. 82 GG): ___
 - Verkündung BGBl.: ___

2. Form
 - Bestimmtheitsgebot: ___
 - Zitiergebot (Art. 19 Abs. 1 S. 2 GG): ___
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - Einzelfallverbot (Art. 19 Abs. 1 S. 1 GG): ___
 - Wesensgehalt (Art. 19 Abs. 2 GG): ___

BVerfG-Pinpoints
- ___

Ergebnis: [formell verfassungsgemäß / formell verfassungswidrig — Grund: ___]
```

## Disclaimer-Wiederholung

Auch eine sorgfältige Prüfung der formellen Verfassungsmäßigkeit ersetzt nicht die anwaltliche Mandatsbearbeitung. Die verbindliche Verwerfung obliegt allein dem BVerfG.

## 3. `gesetzgebungskompetenz-pruefen`

**Fokus:** Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung Subsidiaritaet Sperrwirkung. Output: Kompetenzprüfmemo Ergebnis mit Fundstellen. Abgrenzung: nicht für formelles Gesetzgebungsverfahren (formelle-verfassungsmäßigkeit).

# Gesetzgebungskompetenz prüfen

## Fachkern: Gesetzgebungskompetenz prüfen
- **Spezialgegenstand:** Gesetzgebungskompetenz prüfen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Disclaimer

Die Bestimmung der Gesetzgebungskompetenz ist hochkomplex und im Streitfall vom BVerfG zu entscheiden (Art. 93 Abs. 1 Nr. 2, 2a GG abstrakte Normenkontrolle; Art. 100 Abs. 1 GG konkrete Normenkontrolle). Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Jede Aussage benötigt BVerfG-Pinpoint.

## Prüfungsschritte

### Schritt 1 — Materie bestimmen

Was regelt das Gesetz inhaltlich? Schwerpunkt (Subject-Matter-Test):

- Hauptregelungsgehalt identifizieren
- Bei Überschneidungen: Schwerpunkt der Regelung entscheidet, nicht die formale Benennung (st. Rspr.)

### Schritt 2 — Bund oder Land?

**Grundregel Art. 70 Abs. 1 GG:** Länder haben das Recht der Gesetzgebung, soweit das GG nicht dem Bund Gesetzgebungsbefugnisse verleiht.

### Schritt 3 — Ausschließliche Gesetzgebung des Bundes (Art. 71, 73 GG)

Bei Materie in Katalog Art. 73 GG: nur Bund. Länder nur, wenn ausdrücklich Bundesgesetz sie ermächtigt (Art. 71 GG).

**Kerngebiete Art. 73 GG:**

- Auswärtige Angelegenheiten, Verteidigung (Nr. 1)
- Staatsangehörigkeit (Nr. 2)
- Freizügigkeit, Passwesen, Ein- und Auswanderung (Nr. 3)
- Währungs-, Geld- und Münzwesen, Maße und Gewichte, Zeitbestimmung (Nr. 4)
- Zölle und Handelseinheit (Nr. 5)
- Luftverkehr (Nr. 6) — Eisenbahnen des Bundes (Nr. 6a)
- Post- und Telekommunikation (Nr. 7)
- Bundesbeamte (Nr. 8)
- Gewerblicher Rechtsschutz, Urheberrecht, Verlagsrecht (Nr. 9)
- Zusammenarbeit Bund–Länder Kriminalpolizei, Verfassungsschutz, Schutz vor internationalem Terrorismus (Nr. 9a, 10)
- Statistik für Bundeszwecke (Nr. 11)
- Waffenrecht, Sprengstoffrecht (Nr. 12)
- Versorgung Kriegsbeschädigter (Nr. 13)
- Kernenergiefriedliche Nutzung (Nr. 14)
- Staatshaftung (Nr. 15)
- Reproduktionsmedizin und Gentechnik (Nr. 15a)

### Schritt 4 — Konkurrierende Gesetzgebung (Art. 72, 74 GG)

Bei Materie in Katalog Art. 74 GG: Länder dürfen, soweit Bund nicht.

**Drei Untergruppen** nach Art. 72 Abs. 2 GG und Art. 72 Abs. 3 GG:

#### 4a. Kernbereich — Bund kann ohne weitere Voraussetzungen (Art. 72 Abs. 1 GG)

Alle Nummern Art. 74 Abs. 1 GG, die nicht in 4b oder 4c stehen.

#### 4b. Erforderlichkeitsklausel Art. 72 Abs. 2 GG

Bund darf nur, wenn und soweit die Herstellung gleichwertiger Lebensverhältnisse im Bundesgebiet oder die Wahrung der Rechts- oder Wirtschaftseinheit im gesamtstaatlichen Interesse eine bundesgesetzliche Regelung erforderlich macht.

**Betroffene Nummern Art. 74 Abs. 1 GG:** 4, 7, 11, 13, 15, 19a, 20, 22, 25, 26.

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 4c. Abweichungsgesetzgebung Art. 72 Abs. 3 GG

Länder können vom Bundesrecht abweichende Regelungen treffen bei:

- Nr. 1 Jagdwesen (ohne Recht der Jagdscheine)
- Nr. 2 Naturschutz und Landschaftspflege (ohne allgemeine Grundsätze, Recht des Artenschutzes oder Meeresnaturschutz)
- Nr. 3 Bodenverteilung
- Nr. 4 Raumordnung
- Nr. 5 Wasserhaushalt (ohne stoff- oder anlagenbezogene Regelungen)
- Nr. 6 Hochschulzulassung und Hochschulabschlüsse
- Nr. 7 (eingefügt) Grundsteuer

Lex posterior gilt zwischen Bund und Land bei Abweichungsgesetzen (Art. 72 Abs. 3 S. 3 GG).

### Schritt 5 — Annexkompetenz und Sachzusammenhang

**Ungeschriebene Bundeskompetenzen** (Auslegung):

- **Kraft Sachzusammenhang** (Sachkompetenz): Bund darf eine Materie regeln, wenn sie mit einer ausdrücklich zugewiesenen Materie so verzahnt ist, dass die ausdrückliche Kompetenz ohne sie nicht sinnvoll auszuüben wäre.
- **Kraft Natur der Sache:** Materien, die der Sache nach nur einheitlich auf Bundesebene zu regeln sind.
- **Annex (Annexkompetenz):** Bund darf Verfahrens- und Vollzugsregelungen erlassen, wenn er die Hauptmaterie regelt.

Achtung: Restriktive Anwendung. Pinpoint-Recherche zwingend.

### Schritt 6 — Verwaltungskompetenz prüfen (Art. 83 ff. GG)

Gesetzgebungskompetenz nicht verwechseln mit Verwaltungskompetenz:

- Art. 83 GG: Grundsatz Landeseigenverwaltung
- Art. 85 GG: Bundesauftragsverwaltung
- Art. 86 GG: Bundeseigenverwaltung

### Schritt 7 — Ergebnis und Konsequenzen

- **Kompetenzgemäß:** weiter zur formellen und materiellen Verfassungsmäßigkeit.
- **Kompetenzwidrig:** Gesetz ist insgesamt nichtig (Verwerfungsmonopol BVerfG, Art. 100 Abs. 1 GG).
- **Teilkompetenzwidrigkeit:** nur die kompetenzfremden Regelungen sind nichtig, sofern abtrennbar.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 70-74 GG (Kompetenzverteilung) — Art. 72 Abs. 2 GG (Erforderlichkeitsklausel) — Art. 72 Abs. 3 GG (Abweichungskompetenz) — Art. 31 GG (Bundesrecht bricht Landesrecht) — Art. 93 Abs. 1 Nr. 2 GG (abstrakte Normenkontrolle)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Format

```
GESETZGEBUNGSKOMPETENZ-PRÜFUNG

Prüfungsgegenstand: <Gesetz / Norm>

1. Materiebestimmung (Schwerpunkt): ___
2. Einschlägige Norm:
 - [ ] Art. 73 GG Nr. ___ (ausschließlich Bund)
 - [ ] Art. 74 GG Nr. ___ (konkurrierend)
 - [ ] Kernbereich Art. 72 Abs. 1 GG
 - [ ] Erforderlichkeitsklausel Art. 72 Abs. 2 GG — Prüfung: ___
 - [ ] Abweichungsgesetzgebung Art. 72 Abs. 3 GG
 - [ ] Ungeschriebene Kompetenz: ___
 - [ ] Art. 70 GG (Landeskompetenz)
3. BVerfG-Pinpoint zur Materie: ___
4. Ergebnis: [kompetenzgemäß / kompetenzwidrig / teilkompetenzwidrig]
```

## Disclaimer-Wiederholung

Diese Kompetenzprüfung ist eine strukturierte Modellauswertung; die verbindliche Verwerfung obliegt allein dem BVerfG (Art. 100 Abs. 1 GG).
