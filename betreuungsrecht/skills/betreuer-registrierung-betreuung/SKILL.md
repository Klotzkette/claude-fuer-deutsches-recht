---
name: betreuer-registrierung-betreuung
description: "Betreuer Registrierung Betreuung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Betreuer Registrierung Betreuung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Betreuer Registrierung Betreuung** im Plugin Betreuungsrecht (§§ 1814 ff. BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `betreuer-als-erbe` | Prüffeld für betreuer als erbe: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `betreuer-registrierung` | Erklärt die Abgrenzung beruflicher / ehrenamtlicher (privater) Betreuer nach BtOG seit 01.01.2023 sowie den Weg zur Registrierung als beruflicher Betreuer nach Paragraphen 23 ff. BtOG und der Betreuerregistrierungsverordnung. Behandelt Sachkundenachweis (270 Stunden, Anerkennung für Volljuristen und Sozialarbeiter), Berufshaftpflicht 250000 EUR pro Fall und 1000000 EUR jaehrlich, Eignungsgespraech bei der Stammbehoerde, Vergueturung nach VBVG, Bestandsbetreuer-Übergangsregelung Paragraph 32 BtOG, Subsidiaritaetsprinzip Paragraph 1816 Abs. 5 BGB. Verwenden bei Fragen wie 'Wie werde ich Berufsbetreuer', 'Sachkunde Betreuer', 'Anerkennung als Volljurist', 'Vergueturung Betreuer', 'Berufshaftpflicht Betreuer', 'Subsidiaritaet ehrenamtlich beruflich'. |
| `betreuung-anwaltskosten-rvg` | Anwaltskosten im Betreuungsverfahren: RVG, Verfahrenspflegerbestellung, Verfahrenskostenhilfe nach § 76 FamFG. Empfehlung Mandantenkommunikation Kosten. |

## Arbeitsweg

Im Plugin Betreuungsrecht (§§ 1814 ff. BGB) gilt für **Betreuer Registrierung Betreuung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `betreuer-als-erbe`

**Fokus:** Prüffeld für betreuer als erbe: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Betreuer als Erbe und Beschenkter

## Wann diesen Skill aufrufen

Immer dann, wenn die Frage steht, ob ein **Berufsbetreuer** im Sinne des § 19 Abs. 2 BtOG durch den Betreuten oder dessen Angehörige durch Verfügung von Todes wegen (Erbe, Vermächtnis, Auflage) oder durch lebzeitige Zuwendung bedacht werden darf, und welche zivil- und berufsrechtlichen Folgen sich daraus ergeben. Auch wenn die Frage nur dem Anschein nach erbrechtlich ist (Erbschein, Pflichtteil), aber der Erbe **gerade der Berufsbetreuer** des Erblassers ist.

Der Skill greift nicht, wenn der Bedachte **ehrenamtlicher** Betreuer im Sinne der §§ 21, 22 BtOG ist — für diese gilt § 30 BtOG nicht. Hierzu siehe Skill `betreuer-registrierung` zur Abgrenzung.

## Aktuelle Rechtsprechung (Stand 05/2026, Live-Verifikation zwingend)

- BGH, Urteil vom 02.07.2025 - IV ZR 93/24: Strukturanaloge Bestätigung der Trennung von Berufsrecht und Erbrecht. Eine Zuwendung von Todes wegen an den behandelnden Arzt ist nicht deshalb unwirksam, weil sie gegen § 32 Abs. 1 S. 1 (M)BO-Ä verstößt. Die Berufsordnung ist kein Verbotsgesetz i.S.d. § 134 BGB; die Testierfreiheit (Art. 14 GG) überwiegt; § 138 BGB bleibt Einzelfallprüfung. Übertragbarkeit der Argumentationsstruktur auf § 30 BtOG-Konstellationen ist sehr nahe liegend, BGH hat zu § 30 BtOG aber noch nicht ausdrücklich entschieden. Quelle: bundesgerichtshof.de PM 2025/2025122.html.
- OLG Nürnberg (Live-Verifikation erforderlich für Aktenzeichen und Datum): bestätigte vor BGH-Entscheidung bereits, dass § 30 BtOG kein § 134 BGB-Verbotsgesetz ist, das Testament wirksam bleibt, aber berufsrechtliche Sanktion droht.
- Weitere Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, dejure.org oder openjur.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflichtbestandteile der Antwort

Eine vollständige Antwort enthält mindestens:

1. die Norm § 30 BtOG mit Verbotsumfang und Ausnahmen,
2. die Leitentscheidung des OLG Nürnberg,
3. die Trennung zwischen erbrechtlicher Wirksamkeit und berufsrechtlicher Sanktion,
4. die Prüfung des § 138 BGB im Einzelfall,
5. einen Hinweis auf die Ausschlagungsfrist und die berufsrechtliche Folgenabwägung.

## I. Verbotsnorm § 30 BtOG

§ 30 Abs. 1 BtOG (seit 01.01.2023, BGBl. I 2021 S. 882) untersagt **beruflichen** Betreuern im Sinne des § 19 Abs. 2 BtOG die Annahme von Geld oder geldwerten Leistungen vom Betreuten, ausdrücklich auch im Rahmen von **Verfügungen von Todes wegen**.

Ausnahmen (§ 30 Abs. 2 BtOG):

- geringwertige Aufmerksamkeiten,
- Aufwendungsersatz nach § 1877 Abs. 3 BGB.

Gestattung (§ 30 Abs. 3 BtOG): durch das Betreuungsgericht ausnahmsweise möglich, **aber nur zu Lebzeiten des Betreuten**. Eine nachträgliche Genehmigung nach dem Erbfall ist nach herrschender Meinung nicht mehr möglich.

Sanktion: Widerruf der Registrierung als beruflicher Betreuer nach § 27 BtOG wegen Unzuverlaessigkeit.

## II. Leitentscheidung OLG Nürnberg

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

### Drei amtliche Leitsätze

1. Die nach § 30 Abs. 1 S. 1 und S. 2 BtOG untersagte Annahme einer Zuwendung von Todes wegen durch einen Berufsbetreuer stellt einen Verstoß gegen seine **Berufspflichten** dar, **nicht** jedoch einen Verstoß gegen ein gesetzliches Verbot im Sinne des § 134 BGB.
2. Die entsprechende letztwillige Verfügung des Erblassers und der Vermögensübergang nach § 1922 Abs. 1 BGB sind in solchen Fällen im Hinblick auf den umfassenden Schutz der Testierfreiheit **wirksam**.
3. Diese gesetzgeberische Wertung ist auch bei der Prüfung der **Sittenwidrigkeit** der letztwilligen Verfügung zu berücksichtigen.

### Sachverhalt in Kuerze

Ein Berufsbetreuer war von dem Betreuten in einem nur teilweise eigenhändigen Testament als Alleinerbe eingesetzt. Das Nachlassgericht (AG Schwabach) versagte den Erbschein unter Hinweis auf § 30 BtOG und Formunwirksamkeit. Das OLG Nürnberg gab der Beschwerde des Betreuers statt.

### Tragende Gründe

- § 30 BtOG richtet sich **einseitig** an den Berufsbetreuer und ist Berufsrecht, kein Verbotsgesetz mit zivilrechtlicher Nichtigkeitsfolge.
- Die Testierfreiheit (Art. 14 Abs. 1 GG i.V.m. § 1937 BGB) würde durch eine Nichtigkeitsfolge unverhältnismäßig eingeschraenkt.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## III. Trennung erbrechtliche Wirksamkeit / berufsrechtliche Sanktion

| Ebene | Folge nach OLG Nürnberg |
|---|---|
| Erbrechtliche Wirksamkeit | Testament und Vermögensübergang nach § 1922 BGB wirksam |
| § 134 BGB | Keine Nichtigkeit |
| § 138 BGB | Nur bei Hinzutreten besonderer Umstände (Ausnutzung der Vertrauensstellung) |
| Berufsrecht | Verstoß gegen Berufspflichten; Widerruf der Registrierung nach § 27 BtOG möglich |
| Nachträgliche Gestattung nach § 30 Abs. 3 BtOG | Nach Erbfall nicht mehr möglich |

## IV. Sittenwidrigkeit nach § 138 Abs. 1 BGB

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Die blosse gesetzgeberische Wertung des § 30 BtOG führt aber **nicht automatisch** zur Sittenwidrigkeit — sonst würde die bewusste Entscheidung des Gesetzgebers gegen eine Verbotsnorm im Sinne des § 134 BGB unterlaufen.

Prüfungsraster im Einzelfall (kumulativ erforderlich):

- besonderes Schutzbedürfnis des Erblassers (Alter, Krankheit, Vereinsamung),
- Nähe und Vertrauensstellung des Betreuers,
- Initiative des Betreuers bei der Testamentserrichtung,
- fehlende sachliche Rechtfertigung der Zuwendung,
- gegebenenfalls Isolation des Erblassers gegenüber Angehörigen.

## V. Herausgabepflichten nach dem Erbfall

### 1. Erbrechtlich: keine Herausgabe

Da das Testament wirksam ist, scheidet der Erbschaftsanspruch nach § 2018 BGB aus: der Berufsbetreuer ist **wahrer Erbe**, nicht Erbschaftsbesitzer mit angemasstem Recht. Auch §§ 2287, 2288 BGB scheiden aus, da keine lebzeitige Schenkung vorliegt. Eine Leistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 1 BGB scheitert am wirksamen Rechtsgrund.

**Pflichtteilsansprueche** nach §§ 2303 ff. BGB der pflichtteilsberechtigten Angehörigen bleiben **unberuehrt** — diese werden durch § 30 BtOG nicht tangiert.

### 2. Betreuungsrechtlich: Schlussabwicklung nach § 1872 BGB

Mit dem Tod des Betreuten endet das Amt des Betreuers ipso iure (§ 1871 Abs. 1 BGB n.F.). Nachwirkende Pflichten:

- § 1872 Abs. 1 BGB: Herausgabe des verwalteten Vermögens und aller Unterlagen an den Betreuten, dessen Erben oder sonstigen Berechtigten.
- § 1872 Abs. 4 BGB i.V.m. § 1865 BGB: Schlussrechnungslegung gegenüber dem Berechtigten auf Verlangen.

**Pointe:** Erbe ist der Berufsbetreuer selbst. Gläubiger und Schuldner der Vermögensherausgabe fallen in einer Person zusammen — der Anspruch nach § 1872 BGB erlischt durch **Konfusion** (vgl. § 1976 BGB analog).

Die Schlussrechnungslegung gegenüber dem **Betreuungsgericht** (§ 1872 Abs. 4 S. 2 BGB) bleibt jedoch bestehen, weil sie der Prüfung des Vermögensbestands während der Betreuung dient. Praktisch bedeutsam: das Gericht kann hier berufsrechtliche Auffälligkeiten feststellen und an die Betreuungsbehörde melden.

### 3. Sonderkonstellation: Betreuer als Miterbe

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 4. Übersicht mögliche Ansprueche Dritter

| Anspruchsteller | Anspruchsgrundlage | Bestand nach OLG Nürnberg |
|---|---|---|
| Gesetzliche / zuvor eingesetzte Erben | § 2018 BGB | Kein angemasstes Erbrecht |
| Gesetzliche Erben | § 812 Abs. 1 S. 1 Alt. 1 BGB | Rechtsgrund: wirksames Testament |
| Pflichtteilsberechtigte | §§ 2303 ff. BGB | Bleibt unberuehrt |
| Erbe gegen sich selbst | § 1872 BGB | Erlischt durch Konfusion |
| Betreuungsbehörde | § 27 BtOG | Berufsrechtlich, kein Verfall |
| Staatsanwaltschaft | §§ 263, 266 StGB ggf. mit §§ 73 ff. StGB | Nur bei Untreue oder Betrug im Einzelfall |
| Miterben gegen Betreuer-Miterbe | §§ 1872, 666 BGB | Auskunft und Rechnungslegung zur Verwaltungszeit |

Eine gesetzliche Pflicht zur Herausgabe des Erlangten an den Staat oder die Aufsichtsbehörde sieht das BtOG **nicht** vor. § 30 BtOG enthält keinen Verfallstatbestand vergleichbar §§ 73 ff. StGB oder § 17 OWiG.

## VI. Beratungspraxis vor Annahme der Erbschaft

Der Berufsbetreuer steht vor einer doppelten Abwägung:

- **Wirtschaftlicher Erwerb** des Nachlasses einerseits,
- **berufliche Existenz** (drohender Widerruf der Registrierung nach § 27 BtOG) andererseits.

Entscheidungsdaten:

- Ausschlagungsfrist **sechs Wochen** ab Kenntnis vom Anfall und vom Berufungsgrund (§ 1944 BGB), gegenüber dem Nachlassgericht zu erklären.
- Eine nachträgliche Anzeige beim Betreuungsgericht mit Antrag auf Gestattung ist nach Wortlaut des § 30 Abs. 3 BtOG **nicht mehr aussichtsreich**, weil die Gestattung nur lebzeitig möglich ist.
- Bei Ausschlagung tritt die gesetzliche Erbfolge bzw. die nächste testamentarische Anordnung in Kraft.
- Bei Annahme: Risiko des Registrierungswiderrufs realistisch einkalkulieren, gegebenenfalls Aufgabe der Berufstätigkeit erwägen.

## VII. Methodische Einordnung

Die Entscheidung des OLG Nürnberg ist Ausdruck der sauberen Trennung zwischen **Berufsrecht** (sanktioniert den Betreuer) und **materiellem Erbrecht** (sanktioniert den Vorgang nicht, weil der Erblasser frei testiert). Diese Trennung dient der verfassungsrechtlich geschuetzten Testierfreiheit (Art. 14 Abs. 1 GG) und vermeidet eine vom Gesetzgeber nicht angeordnete Doppelsanktion.

Die Faustformel "Berufsbetreuer darf nicht erben" ist daher zu pauschal und in dieser Form **falsch**. Richtig ist: Der Berufsbetreuer darf zivilrechtlich erben, riskiert aber sein Berufsrecht. Gleichwohl ist nicht jeder solche Erwerbsvorgang berufsrechtlich gleich zu bewerten — die Sittenwidrigkeitsprüfung des § 138 BGB bleibt der Einzelfallprüfung vorbehalten.

## VIII. Offene Folgefragen

- Wie verhalten sich andere OLG zur Frage der Sittenwidrigkeit ohne notarielle Beurkundung — eine Klärung durch den BGH steht aus.
- Was geschieht bei späterer Nichtigerklärung des Testaments durch Anfechtung (§§ 2078, 2080 BGB)? Dann greifen die Rückabwicklungsmechanismen über § 2018 BGB ein.
- Wie wirkt die Konfusion auf Drittansprueche (Pflichtteilsbelastung, Pflichtteilsergänzung nach § 2325 BGB)?

## IX. Zitierhinweise im Antworttext

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Pinpoint-Zitierung mit Randnummer und juengere Entscheidungen zuerst.

## 2. `betreuer-registrierung`

**Fokus:** Erklärt die Abgrenzung beruflicher / ehrenamtlicher (privater) Betreuer nach BtOG seit 01.01.2023 sowie den Weg zur Registrierung als beruflicher Betreuer nach Paragraphen 23 ff. BtOG und der Betreuerregistrierungsverordnung. Behandelt Sachkundenachweis (270 Stunden, Anerkennung für Volljuristen und Sozialarbeiter), Berufshaftpflicht 250000 EUR pro Fall und 1000000 EUR jaehrlich, Eignungsgespraech bei der Stammbehoerde, Vergueturung nach VBVG, Bestandsbetreuer-Übergangsregelung Paragraph 32 BtOG, Subsidiaritaetsprinzip Paragraph 1816 Abs. 5 BGB. Verwenden bei Fragen wie 'Wie werde ich Berufsbetreuer', 'Sachkunde Betreuer', 'Anerkennung als Volljurist', 'Vergueturung Betreuer', 'Berufshaftpflicht Betreuer', 'Subsidiaritaet ehrenamtlich beruflich'.

# Berufliche und ehrenamtliche Betreuung; Weg zur Registrierung

## Wann diesen Skill aufrufen

Wenn der Nutzer wissen will, **wer** überhaupt Betreuer werden darf, **wie** sich beruflicher und ehrenamtlicher Betreuer unterscheiden, oder **wie** die Registrierung als beruflicher Betreuer nach §§ 23 ff. BtOG abläuft. Auch wenn die Frage nur scheinbar berufsrechtlich klingt (Vergueturung, Haftpflicht), aber im Kern auf den Status als Berufsbetreuer abzielt.

## Triage — kläre vor Beratung zur Registrierung
1. Ist die Person bereits als Berufsbetreuer registriert (Bestandsbetreuer § 32 BtOG) oder Erstregistrierung?
2. Liegt ein Volljurist-Abschluss vor? Dann kürzte Sachkunde-Route (§ 23 Abs. 3 BtOG i.V.m. BtRegV).
3. Wird Berufshaftpflicht 250.000 / 1.000.000 EUR nachgewiesen?
4. Ehrenamtlich oder beruflich? § 30 BtOG (Zuwendungsverbot) gilt nur für Berufsbetreuer.
5. Subsidiarität: Besteht Vorrang einer ehrenamtlichen Lösung (§ 1816 Abs. 5 BGB)?

## Aktuelle Rechtsprechung (Stand 05/2026, Live-Verifikation vor Verwendung)

- BGH, Beschluss vom 24.09.2025 - XII ZB 513/24: Bei der Bestellung eines Verhinderungsbetreuers gelten die Auswahlkriterien des § 1816 BGB. Der Wunsch der/des Betroffenen, durch eine nahe Angehörige (hier: Mutter) betreut zu werden, hat Vorrang vor der Bestellung eines Berufsbetreuers. Wenn Zweifel an der Eignung der gewünschten Person bestehen, muss das Gericht von Amts wegen ermitteln (§ 26 FamFG) und die Wunschperson persönlich anhören. Quelle: bundesgerichtshof.de / dejure.org.
- Weitere Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesgerichtshof.de, dejure.org, openjur.de) verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## I. Der "rechtliche Betreuer" als Oberbegriff

Der Gesetzgeber spricht systematisch vom **rechtlichen Betreuer** im Sinne des § 1814 Abs. 1 BGB n.F. — er handelt für volljährige Personen, die ihre Angelegenheiten wegen Krankheit oder Behinderung ganz oder teilweise rechtlich nicht selbst besorgen können.

Drei Erscheinungsformen:

1. **Ehrenamtliche Betreuer mit familiaerer Bindung** (§ 21 BtOG) — meist Angehörige.
2. **Ehrenamtliche Betreuer ohne familiaere Bindung** (§ 22 BtOG) — verpflichtet zum Abschluss einer Vereinbarung mit einem anerkannten Betreuungsverein (§ 15 BtOG).
3. **Berufliche Betreuer** (§§ 19 Abs. 2, 23 ff. BtOG) — Personen, die Betreuungen entgeltlich und berufsmaessig führen.

## II. Ehrenamtlicher (privater) Betreuer

Eine Privatperson, die die Betreuung **unentgeltlich** im Sinne des § 1878 BGB n.F. führt. Sie erhält nur eine **pauschale Aufwandsentschädigung** nach § 1878 BGB i.V.m. § 22 JVEG (derzeit 425 EUR pro Jahr).

Rekrutierung typischerweise aus dem familiaeren oder freundschaftlichen Umfeld; nach § 22 BtOG aber auch fremde Personen möglich, sofern Vereinbarung mit einem Betreuungsverein besteht.

**Keine Sachkundeprüfung** — die persönliche Eignung prüfen die Betreuungsgerichte im Einzelfall.

Wichtig für die Praxis: § 30 BtOG (Annahmeverbot von Zuwendungen) gilt **nicht** für ehrenamtliche Betreuer. Angehörige dürfen testamentarisch bedacht werden, ohne berufsrechtliche Bedenken.

## III. Beruflicher Betreuer

Legaldefinition § 19 Abs. 2 BtOG: derjenige, der Betreuungen **berufsmaessig** führt.

Förmliche Feststellung der Berufsmaessigkeit durch das Gericht nach § 1 Abs. 2 VBVG; vermutet bei:

- mindestens elf Betreuungen oder
- Tätigkeit mit mehr als 20 Wochenstunden.

Erscheinungsformen:

- Freiberuflich (über 80 Prozent der Fälle).
- **Vereinsbetreuer** (§ 14 BtOG, angestellt bei einem anerkannten Betreuungsverein).
- **Behördenbetreuer** (§ 5 BtOG) — nachrangig.

Vergueturung nach **VBVG** (Vormuender- und Betreuervergueturungsgesetz) in Form monatlicher Fallpauschalen. Staffelung nach drei Faktoren:

- Qualifikation (Vergütungstabelle A, B oder C),
- Wohnsitz des Betreuten (stationär oder ambulant),
- Vermögensstatus (mittellos oder vermögend).

Für volljuristisch qualifizierte Betreuer (Tabelle C): monatliche Pauschalen zwischen ungefähr 200 EUR und 320 EUR pro Fall. Hauptberuflich tragfähig bei rund 40 Fällen.

## IV. Subsidiaritaet — Vorrang des Ehrenamts

Zentrale Wertentscheidung des Reformgesetzgebers: **§ 1816 Abs. 5 BGB n.F.** Das Gericht darf einen beruflichen Betreuer nur bestellen, wenn keine geeignete ehrenamtliche Person zur Verfügung steht.

Ausdruck des verfassungsrechtlichen Selbstbestimmungs- und Verhältnismäßigkeitsgrundsatzes (Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1 GG).

## V. Übersicht der Unterschiede

| Merkmal | Beruflicher Betreuer | Ehrenamtlicher Betreuer |
|---|---|---|
| Rechtsgrundlage | §§ 19 Abs. 2, 23 ff. BtOG | §§ 21, 22 BtOG |
| Registrierung | Pflicht (§ 23 BtOG) | Nicht erforderlich |
| Sachkundenachweis | 270 Stunden Sachkundelehrgang oder Anerkennung (§ 23 Abs. 3 BtOG) | Nicht erforderlich |
| Vergueturung | Fallpauschalen nach VBVG | Aufwandspauschale § 1878 BGB |
| Bestellung | Vorschlag der Stammbehörde; Subsidiaritaet beachten | Vorrang vor Beruf nach § 1816 Abs. 5 BGB |
| Berufshaftpflicht | Pflicht: 250.000 EUR pro Fall und 1.000.000 EUR jaehrlich | Nicht erforderlich |
| § 30 BtOG (Zuwendungsverbot) | Erfasst | Nicht erfasst |
| Anzahl Betreuungen typisch | Vollzeit etwa 40 Fälle | Meist 1, selten mehrere |

## VI. Weg in die Berufsbetreuung — Registrierung nach §§ 23 ff. BtOG

### 1. Antrag bei der Stammbehörde

Antrag bei der **oertlich zuständigen Betreuungsbehörde** ("Stammbehörde", § 23 Abs. 1 S. 1 BtOG): diejenige Behörde, in deren Bezirk der Sitz beziehungsweise hilfsweise der Wohnsitz des Betreuers liegt.

Einzelheiten: **Betreuerregistrierungsverordnung (BtRegV)** vom 26.10.2022 (BGBl. I S. 1934).

Erst die Registrierung eroeffnet die Bestellung durch das Betreuungsgericht und begründet einen Vergütungsanspruch.

### 2. Materielle Voraussetzungen (§ 23 Abs. 1 BtOG)

Kumulativ:

a) **Persönliche Eignung und Zuverlaessigkeit** (Nr. 1), nachgewiesen durch:

- erweitertes Führungszeugnis (§ 30a BZRG),
- Auskunft aus dem Schuldnerverzeichnis (§ 882b ZPO),
- gegebenenfalls Bescheinigung in Steuersachen.

b) **Ausreichende Sachkunde** (Nr. 2 i.V.m. Abs. 3) in den Bereichen:

- Betreuungs- und Unterbringungsrecht,
- dazugehoeriges Verfahrensrecht,
- Personen- und Vermögenssorge,
- sozialrechtliches Unterstützungssystem,
- Kommunikation mit erkrankten oder behinderten Personen.

c) **Berufshaftpflichtversicherung** für Vermögensschäden:

- Mindestversicherungssumme **250.000 EUR pro Versicherungsfall**,
- **1.000.000 EUR jaehrlich** insgesamt.

### 3. Sachkundenachweis (§ 23 Abs. 3 BtOG i.V.m. §§ 7 ff. BtRegV)

Der **Sachkundelehrgang** umfasst nach BtRegV in der Regel **270 Zeitstunden** modular aufgebauten Unterrichts.

Anerkennung ganz oder teilweise möglich bei:

- **Volljuristen** (Rechtswissenschaft mit Erstem und Zweitem Staatsexamen) — weitreichende Anerkennung; regelmäßig nur ergänzende Module zu Kommunikation und sozialrechtlichem Unterstützungssystem nachzuweisen.
- **Sozialarbeiter und Sozialpaedagogen** (Bachelor oder Diplom) — weitgehende Anerkennung.
- **Sonstige einschlägige Abschlüsse** (Psychologie, Pflegewissenschaft) — Teilanerkennung möglich.

**Bestandsbetreuer**, die vor dem 01.01.2020 bereits berufsmaessig bestellt waren, gelten qua Übergangsregelung **§ 32 BtOG** ohne weiteren Nachweis als sachkundig.

### 4. Verfahren

- Antragstellung bei der Stammbehörde.
- **Persönliches Eignungsgespräch** (§ 24 BtOG i.V.m. § 4 BtRegV).
- Bei positivem Ergebnis: Eintragung in das Betreuerregister.
- Übermittlung der Registrierungsdaten an die Betreuungsgerichte des Zuständigkeitsbereichs.
- Bestellung durch Beschluss des Gerichts in konkreten Verfahren nach § 1816 BGB n.F.

### 5. Widerruf und Aufsicht (§§ 25 bis 27 BtOG)

Rücknahme oder Widerruf der Registrierung nach **§ 27 BtOG** bei:

- Wegfall der persönlichen Eignung oder Zuverlaessigkeit,
- groben Berufspflichtverletzungen, insbesondere bei Verstößen gegen **§ 30 BtOG** (Annahmeverbot).

Laufende Aufsicht: Stammbehörde nach §§ 25, 26 BtOG.

## VII. Rechtsanwalt als Berufsbetreuer

Berufsbegleitende Tätigkeit als Berufsbetreuer ist berufsrechtlich grundsaetzlich zulässig (§ 7 BRAO im Umkehrschluss), bedarf aber der **Anzeige bei der zuständigen Rechtsanwaltskammer**.

Steuerlich: nicht klassischer Katalogberuf des § 18 EStG, in der Praxis aber regelmäßig entsprechend behandelt; im Zweifel mit Steuerberater prüfen.

Sachkunde: aufgrund der juristischen Qualifikation regelmäßig **erheblich verkürzter** Sachkundeweg, lediglich Erganzungsmodule zu Kommunikation und sozialrechtlichem System nachzuweisen.

## VIII. Pflicht-Erinnerungen für Antworten

Bei Beratung zur Berufsbetreuung immer mitnehmen:

- Subsidiaritaet gegenüber dem Ehrenamt (§ 1816 Abs. 5 BGB).
- § 30 BtOG und seine Konsequenzen (siehe Skill `betreuer-als-erbe`).
- Pflichtbestellung Berufshaftpflicht 250.000 / 1.000.000 EUR.
- Sachkundeanrechnung für Volljuristen.
- Bestandsschutz nach § 32 BtOG für Altbetreuer vor 01.01.2020.

## IX. Zitierhinweise im Antworttext

- BtOG vom 04.05.2021, BGBl. I S. 882, in Kraft seit 01.01.2023.
- BtRegV vom 26.10.2022, BGBl. I S. 1934.
- BGB §§ 1814, 1816 Abs. 5, 1865, 1871, 1872, 1877, 1878 (jeweils n.F.).
- VBVG §§ 7 ff. für die Vergueturung.

## 3. `betreuung-anwaltskosten-rvg`

**Fokus:** Anwaltskosten im Betreuungsverfahren: RVG, Verfahrenspflegerbestellung, Verfahrenskostenhilfe nach § 76 FamFG. Empfehlung Mandantenkommunikation Kosten.

# Betreuung: Anwaltskosten

## Spezialwissen: Betreuung: Anwaltskosten
- **Spezialgegenstand:** Betreuung: Anwaltskosten / betreuung anwaltskosten rvg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** RVG, FamFG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
