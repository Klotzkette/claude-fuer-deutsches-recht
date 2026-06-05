---
name: bafin-laufender-beschwerde-anhoerung
description: "Bafin Laufender Beschwerde Anhoerung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bafin Laufender Beschwerde Anhoerung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bafin Laufender Beschwerde Anhoerung** im Plugin Factoring Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bafin-tatbestand-factoring-laufender-forderungsankauf-rahmenvert` | BaFin Tatbestand Factoring laufender Forderungsankauf Rahmenvertrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |
| `beschwerde-und-anhoerung-bafin-factoring` | Beschwerde und Anhörung BaFin Factoring: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |
| `bilanzierung-true-sale-ausbuchung-wirtschaftliches-risiko` | Bilanzierung True Sale Ausbuchung wirtschaftliches Risiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |

## Arbeitsweg

Im Plugin Factoring Recht gilt für **Bafin Laufender Beschwerde Anhoerung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bafin-tatbestand-factoring-laufender-forderungsankauf-rahmenvert`

**Fokus:** BaFin Tatbestand Factoring laufender Forderungsankauf Rahmenvertrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# BaFin Tatbestand Factoring laufender Forderungsankauf Rahmenvertrag

## Fachkern: BaFin Tatbestand Factoring laufender Forderungsankauf Rahmenvertrag
- **Spezialgegenstand:** BaFin Tatbestand Factoring laufender Forderungsankauf Rahmenvertrag. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Der Tatbestand des Factorings in § 1 Abs. 1a Satz 2 Nr. 9 KWG ist auf drei Tragesäulen aufgebaut:

1. **Laufender Ankauf** – nicht einzelner, einmaliger Ankauf, sondern regelmäßiges Geschäftsmodell.
2. **Forderungen** – Geldforderungen aus Lieferungen und Leistungen, abgrenzbar von Darlehensforderungen.
3. **Auf Grundlage von Rahmenverträgen** – wiederkehrende Vertragsstruktur zwischen Factor und Verkäufer.

Optional: **mit oder ohne Rückgriff** – also echtes und unechtes Factoring sind beide erfasst.

Wer alle drei Säulen erfüllt, ist Finanzdienstleistungsinstitut nach § 1 Abs. 1a Satz 1 KWG mit voller Aufsichtsfolge: Erlaubnispflicht (§ 32 KWG), Mindestkapital (§ 33 KWG), Geschäftsleiteranforderungen (§ 25c KWG), GwG-Pflichten, MaRisk-Anwendung. Dieser Skill prüft die Tatbestandsmerkmale einzeln.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Ein Geschäftsmodell soll auf die Erlaubnispflicht hin geprüft werden.
- Eine BaFin-Anfrage zur Geschäftsabgrenzung soll vorbereitet werden.
- Ein bestehender Factor untersucht, ob sich neue Geschäftsfelder noch im Tatbestand bewegen.
- In einer Untersagungsverfügung der BaFin (§ 37 KWG) ist der Tatbestand streitig.

Fragen zum Einstieg:
- Wer ist Käufer der Forderungen (Mandant)?
- Wie oft und in welcher Frequenz werden Forderungen angekauft?
- Gibt es einen Rahmenvertrag, oder nur Einzelverkäufe?
- Welche Forderungen genau (Lieferung, Werk, Dienstleistung, Darlehen)?
- Übernimmt der Käufer das Ausfallrisiko oder nicht?

## Rechtlicher Rahmen

- **§ 1 Abs. 1a Satz 1 KWG**: Finanzdienstleistungsinstitute, die Finanzdienstleistungen für andere gewerbsmäßig oder in einem Umfang erbringen, der einen in kaufmännischer Weise eingerichteten Geschäftsbetrieb erfordert.
- **§ 1 Abs. 1a Satz 2 Nr. 9 KWG**: Factoring als Finanzdienstleistung – "der laufende Ankauf von Forderungen auf der Grundlage von Rahmenverträgen mit oder ohne Rückgriff".
- **BaFin-Merkblatt zum Tatbestand des Factoring**: Auslegungshilfe, kein Gesetz, aber Verwaltungspraxis.
- **§ 32 KWG**: Erlaubnispflicht.
- **§ 33 KWG**: Anfangskapital für Factor: nach derzeitigem Stand 730.000 EUR.
- **§ 25c KWG**: Geschäftsleiteranforderungen.
- **§ 54 KWG**: Strafvorschrift bei erlaubnislosem Betrieb.
- **§ 2 Abs. 6 KWG**: Bereichsausnahmen.

## / Schritt für Schritt

1. **Verkäuferkreis bestimmen**: Wer verkauft die Forderungen an den Factor (eine Person, mehrere, Konzern)?
2. **Rahmenvertrag identifizieren**: Liegt ein schriftlicher Rahmenvertrag mit laufender Verpflichtung vor? Oder nur einzelne, ungebundene Ankäufe?
3. **Laufendkeit prüfen**: Frequenz, Volumen, Dauer der Geschäftsbeziehung. BaFin hat keine harte Schwelle, aber regelmäßige Wiederholung ist erforderlich.
4. **Forderungstyp prüfen**: Geldforderungen aus Lieferungen und Leistungen? Darlehensforderungen sind nicht im Factoring-Tatbestand, ggf. Kreditgeschäft im Sinne § 1 Abs. 1 Satz 2 Nr. 2 KWG.
5. **Forderungskauf prüfen**: Echter Verkauf (Forderung wird Eigentum des Factors) oder bloße Sicherungsabtretung?
6. **Mit/ohne Rückgriff prüfen**: Beides ist erfasst – relevant nur für die wirtschaftliche Einordnung.
7. **Bereichsausnahmen prüfen**: Konzerninterne Geschäfte (§ 2 KWG), Treuhandgeschäfte ohne Gefahrentragung.

## Trade-off-Matrix

| Geschäftsmodell | Tatbestand erfüllt? | Erläuterung |
|---|---|---|
| Einmaliger Forderungsverkauf zwischen Konzerngesellschaften | Nein | Keine Laufendkeit, ggf. Bereichsausnahme |
| Sporadische Forderungsverkäufe ohne Rahmenvertrag | Grenzfall | Wahrscheinlich nicht, aber Beweislast beim Anbieter |
| Rahmenvertrag mit monatlichem Ankauf | Ja | Eindeutig erfasst |
| Ankauf von Darlehensforderungen | Nein, aber ggf. § 1 Abs. 1 Satz 2 Nr. 2 KWG (Kreditgeschäft) | Andere Erlaubnisstruktur |
| Forfaitierung von Einzel-Großforderungen | Grenzfall | Bei wiederholter Praxis ggf. Tatbestand |
| Reverse Factoring (vom Käufer initiiert) | Ja, wenn laufend und mit Rahmenvertrag | BaFin hat Reverse-Factoring grundsätzlich als KWG-relevant eingestuft |

## Praxistipps

- **Rahmenvertrag nicht umgehen**: Versuche, das Geschäft als "Einzelverkäufe ohne Rahmenvertrag" zu strukturieren, sind in der BaFin-Praxis durchsichtig. Wenn faktisch ein laufendes Geschäft entsteht, greift der Tatbestand.
- **Konzernausnahme klären**: § 2 Abs. 6 KWG hat keine umfassende Konzernausnahme für Factoring – Vorsicht bei intercompany-Lösungen.
- **Schwellen mehr Indizien, nicht Tatbestandsmerkmal**: Es gibt keine harte Schwelle (z. B. 10 Forderungen oder 1 Mio. EUR), aber Volumen und Frequenz sind Auslegungshilfen.
- **Schriftform empfohlen**: Auch wenn kein Schriftformerfordernis besteht, sollte der Rahmenvertrag schriftlich sein – wegen Dokumentations- und Aufsichtspflichten.
- **Voranfrage als Schutzmechanismus**: Bei unklaren Sachverhalten BaFin-Voranfrage stellen, die Antwort gilt als Vertrauenstatbestand.

## Mustertexte

**Tatbestandsvermerk**

"In dem Mandat … plant der Mandant ein Geschäft, in dem die [X-GmbH] gegenüber der [Y-AG] sechsmal jährlich Forderungspakete in Höhe von je 200.000 EUR zum Verkauf anbietet. Es besteht ein Rahmenvertrag mit Laufzeit zwei Jahre, automatische Verlängerung. Echtes Factoring. Tatbestandsmerkmale: (1) laufender Ankauf – ja, bei 6 Ankäufen pro Jahr über zwei Jahre; (2) Forderungen aus Lieferungen und Leistungen – ja; (3) Rahmenvertrag – ja. Ergebnis: Tatbestand § 1 Abs. 1a Satz 2 Nr. 9 KWG erfüllt; Erlaubnispflicht."

**Klausel im Rahmenvertrag (klarstellend)**

"Dieser Rahmenvertrag regelt den fortlaufenden Ankauf von Forderungen aus Lieferungen und Leistungen der Verkäuferin durch die Käuferin nach Maßgabe der Einzelvereinbarungen. Die Parteien gehen davon aus, dass die Käuferin als Finanzdienstleistungsinstitut im Sinne des § 1 Abs. 1a Satz 2 Nr. 9 KWG handelt."

**BaFin-Voranfrage (Auszug)**

"Wir bitten um Mitteilung, ob das beigefügte Geschäftsmodell den Tatbestand des laufenden Forderungsankaufs auf der Grundlage von Rahmenverträgen im Sinne des § 1 Abs. 1a Satz 2 Nr. 9 KWG erfüllt. Insbesondere bitten wir um Stellungnahme zu folgenden Aspekten: (1) Auslegung des Merkmals 'laufend' bei einer Frequenz von … pro Jahr; (2) Behandlung gruppeninterner Geschäfte; (3) Abgrenzung zu sonstigen Forderungsfinanzierungen."

## Typische Fehler

- Annahme, ein nur mündlicher Rahmenvertrag liege nicht vor – BaFin schaut auf das wirtschaftliche Bild.
- Verkennen, dass auch unechtes Factoring (mit Rückgriff) erfasst ist.
- Vertretene Auffassung, Reverse-Factoring sei aufsichtsfrei – derzeit nicht haltbar.
- Übersehen, dass die Erlaubnispflicht nicht nur den Käufer (Factor), sondern auch faktische Vermittlungs- und Plattformkonstruktionen treffen kann.
- Nachträgliche Konstruktion einer "Einzelfall"-Struktur, um Erlaubnispflicht zu vermeiden.

## Edge Cases und Sonderkonstellationen

- **EU-Pass für Auslandsfactoren**: Ein in einem anderen EU-Staat zugelassener Factor darf grundsätzlich grenzüberschreitend in Deutschland tätig werden – Anzeigeverfahren statt voller Erlaubnis.
- **Crowd-Factoring-Plattformen**: Plattformen, die Forderungen an Kleininvestoren vermitteln, können sowohl KWG (eigener Forderungsankauf) als auch WpHG/VermAnlG-Tatbestand auslösen.
- **Tokenisierung von Forderungen**: Forderungen als Krypto-Werte oder Security Tokens – ggf. zusätzliche Erlaubnispflicht nach KWG/WpHG/eWpG.
- **Konzernfinanzierungsgesellschaften**: Wenn eine Konzern-Finance-Gesellschaft systematisch Konzernforderungen ankauft, kann je nach Außenwirkung KWG greifen.
- **Mortgage Servicing**: Forderungen aus grundpfandrechtlich gesicherten Krediten – Sonderfall, ggf. § 1 Abs. 1 Satz 2 Nr. 2 KWG (Kreditgeschäft) statt Factoring.
- **Trade-Receivables-Securitization**: Verkauf an SPV mit ABS-Strukturierung – Aufsicht trifft sowohl Originator (Verkäufer) als auch SPV; § 18a KWG zu Verbriefungen beachten.
- **PSD2/PSD3-Bezug**: Sobald Kontoinformationsdienste eingebunden sind, greift ZAG.

## Querverweise

- `aufsichtsrechtliche-schnellampel-kwg-zag`
- `erlaubnisantrag-32-kwg-unterlagen-geschaeftsleiter`
- `beschwerde-und-anhoerung-bafin-factoring`
- `factoringtyp-true-false-reverse-maturity`

## Quellen Stand 06/2026

- KWG § 1 Abs. 1a Satz 2 Nr. 9, § 2, § 32, § 33, § 54.
- BaFin-Merkblatt zum Tatbestand des Factoring, in der jeweils aktuellen Fassung auf bafin.de.
- Gesetzesbegründung zum Jahressteuergesetz 2009 (Einführung des Factoring-Tatbestands).
- BaFin-Veröffentlichungen zur Praxis der Erlaubnisverfahren.
- BVerwG zu Untersagungsverfügungen bei erlaubnislosem Betrieb (jeweils prüfen).

## 2. `beschwerde-und-anhoerung-bafin-factoring`

**Fokus:** Beschwerde und Anhörung BaFin Factoring: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Beschwerde und Anhörung BaFin Factoring

## Fachkern: Beschwerde und Anhörung BaFin Factoring
- **Spezialgegenstand:** Beschwerde und Anhörung BaFin Factoring. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die BaFin greift im Factoring-Bereich auf mehreren Wegen ein: **Sonderprüfung** (§ 44 KWG), **Anhörung** (§ 28 VwVfG), **Untersagungsverfügung** (§ 37 KWG bei erlaubnislosem Betrieb), **Anordnungen zur Geschäftsorganisation** (§ 25a KWG), **Bußgeld** (§ 56 KWG). Vor belastenden Maßnahmen muss BaFin den Betroffenen anhören. Die Anhörungsphase ist die wichtigste Gelegenheit, das Verfahren noch zu drehen – Tatsachen klarstellen, Rechtsauffassung darlegen, mildere Mittel anbieten.

Dieser Skill konstruiert die Antwortstrategie auf BaFin-Anhörungen und das taktische Vorgehen bei Beschwerden gegen BaFin-Maßnahmen (Widerspruchsverfahren entfällt seit 1.1.2017 weitgehend, Klage zum VG Frankfurt nach § 49 Abs. 1 KWG).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Eine Anhörung der BaFin (Schreiben mit Frist zur Stellungnahme) liegt auf dem Tisch.
- Eine Untersagungsverfügung oder Bußgeldandrohung wurde zugestellt.
- Der Mandant erwägt Beschwerde gegen Maßnahmen oder gegen das Verhalten der Geschäftsleitung.
- Eine Sonderprüfung nach § 44 KWG wurde angekündigt.

Fragen zum Einstieg:
- Welche Maßnahme steht im Raum (Untersagung, Auflage, Bußgeld, Sonderprüfung)?
- Welche Frist nennt das BaFin-Schreiben?
- Welche Tatsachen wirft BaFin vor (erlaubnisloses Geschäft, mangelhafte Organisation, GwG-Verstöße)?
- Ist die Geschäftsleitung anwaltlich vertreten, ist Akteneinsicht erfolgt?
- Liegt schon eine Anordnung mit Sofortvollzug vor?

## Rechtlicher Rahmen

- **§ 28 VwVfG**: Anhörung Beteiligter vor belastendem Verwaltungsakt.
- **§§ 32, 33, 37 KWG**: Erlaubnispflicht und Untersagung erlaubnislosen Betriebs.
- **§ 25a, 25b KWG**: Anforderungen an die Geschäftsorganisation und Risikomanagement.
- **§ 44 KWG**: Sonderprüfung – BaFin kann Prüfer entsenden.
- **§ 49 KWG**: Rechtsweg – Anfechtungsklage zum VG Frankfurt am Main; Widerspruchsverfahren nur eingeschränkt.
- **§ 56 KWG**: Bußgeldvorschriften.
- **VwGO §§ 80, 113**: Vorläufiger Rechtsschutz, Anfechtungsklage.
- **GG Art. 19 Abs. 4**: Rechtsschutzgarantie.
- **§ 29 VwVfG**: Akteneinsicht.

## / Schritt für Schritt

1. **Fristen sichern**: Anhörungsfrist notieren, gegebenenfalls Fristverlängerung beantragen (begründet).
2. **Akteneinsicht beantragen**: § 29 VwVfG – Einsicht in alle Akten der BaFin zum Vorgang.
3. **Sachverhalt rekonstruieren**: Welche konkreten Vorgänge wirft BaFin vor, welche Belege liegen vor?
4. **Tatsachen versus Wertungen trennen**: Was ist unstreitig, was bestreitet der Mandant?
5. **Rechtliche Verteidigungslinie**: Tatbestand bestreiten, Bereichsausnahme, mildere Mittel, Verhältnismäßigkeit.
6. **Stellungnahme verfassen**: Strukturiert nach Sachverhalt, Rechtslage, Antrag/Stellungnahme.
7. **Bei belastender Verfügung Klage prüfen**: § 49 KWG, VG Frankfurt; eventuell § 80 Abs. 5 VwGO einstweiliger Rechtsschutz.

## Trade-off-Matrix

| Lage | Option | Risiko |
|---|---|---|
| BaFin wirft erlaubnislosen Betrieb vor, sachlich richtig | Erlaubnis nachträglich beantragen, Geschäft pausieren | Verfahren dauert Monate, Strafverfahren droht |
| BaFin wirft erlaubnislosen Betrieb vor, sachlich falsch | Bestreiten, Tatbestandsausnahme darlegen | Risiko der Untersagung trotzdem |
| Organisationsanordnung | Umsetzung anbieten, Vorlage Konzept | Anordnung wird konkretisiert |
| Bußgeldandrohung | Stellungnahme mit Milderungsgründen | Bußgeld kann verhängt werden |
| Sofortvollzug | Antrag § 80 Abs. 5 VwGO sofort | Schnelle Entscheidungsbedarf |
| Sonderprüfung | Mitwirken, Berater einschalten | Findings können belastend sein |

## Praxistipps

- **Schnell reagieren**: BaFin gewährt typischerweise vier Wochen Anhörungsfrist – bei komplexen Sachverhalten Fristverlängerung formal beantragen.
- **Akteneinsicht zwingend**: Ohne Akteneinsicht keine substantiierte Stellungnahme. Akten enthalten oft anonyme Anzeigen, frühere Vorgänge, interne Vermerke.
- **Tatsachenbasis prüfen**: BaFin stützt sich häufig auf Anzeigen, Pressemeldungen, Verbraucherbeschwerden – Belastbarkeit prüfen.
- **Verhältnismäßigkeit anbringen**: Auch wenn der Tatbestand zutrifft, ist die Maßnahme häufig nur dann rechtmäßig, wenn keine milderen Mittel möglich sind.
- **Vergleichsverfahren**: BaFin verhandelt grundsätzlich, etwa über Auflagenlast statt Untersagung.

## Mustertexte

**Antrag auf Akteneinsicht**

"Sehr geehrte Damen und Herren, in der Angelegenheit … (Az. …) zeigen wir die Vertretung der … an und beantragen Akteneinsicht gemäß § 29 VwVfG. Bitte stellen Sie uns die vollständige Akte zur Einsicht zur Verfügung oder gestatten Sie die Einsichtnahme in Ihren Räumen. Zugleich beantragen wir Verlängerung der Anhörungsfrist um drei Wochen bis zum …"

**Stellungnahme zur Anhörung (Auszug)**

"Mit Schreiben vom … haben Sie unserer Mandantin mitgeteilt, dass beabsichtigt ist, gemäß § 37 KWG die Untersagung der Geschäftstätigkeit zu verfügen. Hierzu nehmen wir wie folgt Stellung:

I. Sachverhalt: Die Mandantin betreibt … [Sachverhaltsdarstellung].

II. Rechtliche Bewertung: Der Tatbestand des § 1 Abs. 1a Satz 2 Nr. 9 KWG ist nicht erfüllt, da [Tatbestandsargument]. Hilfsweise: Die beabsichtigte Untersagung wäre unverhältnismäßig, weil [Verhältnismäßigkeit].

III. Anregung: Wir regen an, das Verfahren bei Erfüllung folgender Auflagen einzustellen: [Auflagen]."

**Klage gegen Untersagungsverfügung**

"Anfechtungsklage gem. § 42 VwGO gegen die Verfügung der BaFin vom … (Az. …). Die Verfügung verletzt die Klägerin in ihren Rechten aus Art. 12 Abs. 1 GG. Die Tatbestandsvoraussetzungen des § 37 KWG liegen nicht vor. Antrag: Die Verfügung wird aufgehoben. Hilfsweise: Antrag § 80 Abs. 5 VwGO Anordnung der aufschiebenden Wirkung."

## Typische Fehler

- Anhörungsfrist verstreichen lassen ohne Verlängerung – Argumente werden präkludiert.
- Stellungnahme ohne Akteneinsicht – unsubstantiiert.
- Tatsachenstreitigkeiten und Rechtsfragen mischen – BaFin erkennt das und nutzt es.
- Verzicht auf einstweiligen Rechtsschutz, obwohl Sofortvollzug droht.
- Unterschätzen der parallelen strafrechtlichen Ermittlungen (§ 54 KWG).

## Edge Cases und Sonderkonstellationen

- **Verwertungs-/Auswerteverbot**: Wenn Anhörungsrechte verletzt wurden, können Beweise einem Verwertungsverbot unterliegen – im Klageverfahren rügen.
- **Geheimhaltungsinteressen Dritter**: Akteneinsicht kann eingeschränkt werden bei berechtigten Geheimhaltungsinteressen anderer Beteiligter; Schwärzung verlangen.
- **Parallel laufende staatsanwaltschaftliche Ermittlungen**: Eine Untersagungsverfügung der BaFin kann strafrechtliche Ermittlungen auslösen oder umgekehrt – Strafverteidiger einschalten.
- **Whistleblower-Anzeigen**: Wenn die BaFin auf Anzeige eines Mitarbeiters reagiert (§ 4d FinDAG), arbeitsrechtliche Folgen bedenken.
- **Internationale Koordinationsverfahren**: BaFin koordiniert mit anderen Aufsichtsbehörden (ESMA, EBA) – Frage stellt sich, ob ausländische Behörden betroffen sind.
- **Verfassungsbeschwerde**: Bei Grundrechtsverletzung durch BaFin-Verfügung Verfassungsbeschwerde nach Erschöpfung des Rechtswegs (Art. 19 Abs. 4 GG, Art. 12 Abs. 1 GG).
- **Streitwert-Festsetzung**: Bei aufsichtsrechtlichen Klagen Streitwert nach wirtschaftlichem Interesse, häufig Jahresumsatz – Gerichtskosten beachten.

## Querverweise

- `bafin-tatbestand-factoring-laufender-forderungsankauf-rahmenvert`
- `aufsichtsrechtliche-schnellampel-kwg-zag`
- `erlaubnisantrag-32-kwg-unterlagen-geschaeftsleiter`

## Quellen Stand 06/2026

- KWG §§ 25a, 25b, 32, 37, 44, 49, 56.
- VwVfG §§ 28, 29 zur Anhörung und Akteneinsicht.
- VwGO §§ 42, 80, 113 zum verwaltungsgerichtlichen Rechtsschutz.
- BaFin-Veröffentlichungen zur Verwaltungspraxis (aktueller Stand auf bafin.de).
- BVerwG zur Verhältnismäßigkeit aufsichtsrechtlicher Maßnahmen.

## 3. `bilanzierung-true-sale-ausbuchung-wirtschaftliches-risiko`

**Fokus:** Bilanzierung True Sale Ausbuchung wirtschaftliches Risiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Bilanzierung True Sale Ausbuchung wirtschaftliches Risiko

## Fachkern: Bilanzierung True Sale Ausbuchung wirtschaftliches Risiko
- **Spezialgegenstand:** Bilanzierung True Sale Ausbuchung wirtschaftliches Risiko. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Für den Factoringkunden ist die **bilanzielle Ausbuchung der Forderung** (Off-Balance) oft das eigentliche Geschäftsziel. Sie senkt die Bilanzsumme, verbessert Bilanzkennzahlen (Eigenkapitalquote, Umschlagshäufigkeit) und ist Voraussetzung für viele Kreditkonditionen. Bilanziell ist die Ausbuchung kein juristischer Selbstläufer: Sie setzt **True Sale** voraus – einen echten Forderungsverkauf mit Übergang des wirtschaftlichen Eigentums, nicht nur eine zivilrechtliche Abtretung mit Sicherungscharakter.

Maßstab nach **HGB (§ 246 HGB, IDW RS HFA 8)**: Ausbuchung, wenn das **wirtschaftliche Eigentum** vollständig übergegangen ist und der Verkäufer keine wesentlichen Risiken zurückbehält. Maßstab nach **IFRS 9** komplexer: Risk-and-Reward-Test plus Control-Test. Dieser Skill prüft die zentralen Stellschrauben.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Der Mandant will Forderungen bilanziell ausbuchen und braucht eine rechtssichere Strukturierung.
- Der Wirtschaftsprüfer beanstandet die Ausbuchung – Argumente werden gesucht.
- Bei Konsolidierungspflicht prüfen Sie die Behandlung von Factoring-Zweckgesellschaften.
- Im IFRS-Konzernabschluss steht die Off-Balance-Behandlung zur Disposition.

Fragen zum Einstieg:
- HGB oder IFRS, oder beides parallel?
- Echtes oder unechtes Factoring (Bonitätsrisiko)?
- Welche Rückgriffsrechte, Garantien, Rückkaufverpflichtungen bestehen?
- Wird ein laufender Sicherheitseinbehalt vereinbart, in welcher Höhe?
- Wer verantwortet das Inkasso, der Factor oder der Kunde?

## Rechtlicher Rahmen

- **HGB § 246 Abs. 1**: Ausweis aller Vermögensgegenstände, soweit wirtschaftlicher Eigentümer.
- **HGB § 252**: Vorsichtsprinzip, Realisationsprinzip.
- **IDW RS HFA 8** (Bilanzierung von Forderungsverkäufen / Forderungsabtretungen): Konkretisierung True-Sale-Anforderungen.
- **HGB § 252 Abs. 1 Nr. 4**: Risikobetrachtung, Bewertung mit Wertberichtigung.
- **IFRS 9 (Financial Instruments)**: Risk-and-Reward, Continuing-Involvement, Control-Test.
- **IFRS 10**: Konsolidierung von Zweckgesellschaften.
- **§ 290 HGB**: Konsolidierungspflicht.
- **§§ 4, 5 EStG**: Steuerliches Maßgeblichkeitsprinzip.

## / Schritt für Schritt

1. **Vertragstyp festlegen**: Echtes Factoring (Bonitätsrisiko übergeht) versus unechtes Factoring (Rückgriff bleibt).
2. **Risikoinventur**: Welche Risiken (Bonität, Verität, Reklamation, Zinsänderung, Wechselkurs) bleiben beim Verkäufer?
3. **Schwellenwerte für True Sale**: Wenn mehr als 5–10 Prozent der Risiken zurückbleiben, droht IFRS Continuing Involvement.
4. **Sicherheitenstruktur prüfen**: Reklamationsreserve, Veritätshaftung, Sperrkonten – tragen sie das Risiko zurück?
5. **HGB versus IFRS abgleichen**: HGB ist toleranter, IFRS strenger.
6. **Konsolidierungsfragen klären**: Wenn Forderungen an Factoring-SPV verkauft werden, IFRS 10 Konsolidierungs-Test.
7. **Wirtschaftsprüfer einbinden**: True-Sale-Opinion einholen bei größeren Strukturen.

## Trade-off-Matrix

| Vertragsstruktur | Ausbuchung HGB | Ausbuchung IFRS |
|---|---|---|
| Echtes Factoring ohne Rückgriff | Ja | Ja, sofern Risiken < 10 Prozent |
| Unechtes Factoring mit voller Bonitätshaftung | Nein | Nein |
| Echtes Factoring mit 10 Prozent Sicherheitseinbehalt | Ja (idR) | Borderline, Continuing Involvement prüfen |
| Inhouse-Factoring mit Servicer-Rolle des Verkäufers | Schwierig | Schwierig (Control-Test) |
| Reverse Factoring | Komplex, abhängig von Käuferinitiative | Komplex, abhängig von Kontrolle |
| Maturity Factoring (Fälligkeitsfactoring) | Ja, wenn Bonitätsrisiko übergeht | Ja, wenn Risiko-Reward-Test bestanden |

## Praxistipps

- **Klare Trennung Bonität vs. Verität**: Veritätshaftung ist im echten Factoring üblich und steht der Ausbuchung nicht entgegen. Bonitätshaftung dagegen verhindert Ausbuchung.
- **Sicherheitseinbehalt begrenzt**: Reklamationsreserve max. 10 Prozent, sonst IFRS-Risk-Test gefährdet.
- **Servicer-Rolle problematisch**: Wenn der Verkäufer weiter das Inkasso durchführt, droht IFRS Continuing Involvement (Control-Test).
- **Externe True-Sale-Opinion**: Bei großen Strukturen Gutachten eines Wirtschaftsprüfers einholen – schafft Bilanzsicherheit.
- **Stille Reserven beachten**: Bei stiller Zession (debitor wird nicht informiert) ist die wirtschaftliche Trennung schwerer zu argumentieren.

## Mustertexte

**Klausel im Factoringvertrag (True Sale)**

"Die Parteien vereinbaren einen Forderungskauf im Sinne des § 433 BGB. Der Factor erwirbt die Forderung mit allen Chancen und Risiken. Insbesondere geht das Bonitätsrisiko vollständig auf den Factor über. Der Verkäufer haftet ausschließlich für die Verität (Bestand und Einredefreiheit) der Forderung. Eine Bonitätshaftung wird ausdrücklich ausgeschlossen."

**Klausel Reklamationsreserve (Ausbuchungs-kompatibel)**

"Der Factor behält von jedem Kaufpreis 7 Prozent als Reklamationsreserve ein. Diese Reserve dient ausschließlich zur Sicherung von Veritätsansprüchen und wird nach 90 Tagen ohne Beanstandung freigegeben. Die Reserve betrifft nicht das Bonitätsrisiko, das vollständig beim Factor verbleibt."

**Memo an Wirtschaftsprüfer (Auszug)**

"Gegenstand: Bilanzierung Factoringgeschäft mit [Factor]. Vertragsstruktur: Echter Forderungsverkauf ohne Rückgriff, Veritätshaftung des Verkäufers, Reklamationsreserve 7 Prozent mit Freigabe nach 90 Tagen. Servicer-Funktion: Forderungen werden offen abgetreten, Inkasso durch Factor. Ergebnis: Voraussetzungen IDW RS HFA 8 für Ausbuchung nach HGB sind erfüllt, da wirtschaftliches Eigentum übergeht. IFRS 9: Risk-and-Reward-Test bestanden, Continuing Involvement < 10 Prozent."

## Typische Fehler

- Verträge mischen Bonitäts- und Veritätshaftung, dadurch Ausbuchung gefährdet.
- Sicherheitseinbehalt zu hoch (> 10 Prozent), IFRS-Continuing-Involvement greift.
- Verkäufer behält Servicer-Rolle, dadurch IFRS-Control-Test problematisch.
- HGB-Ausbuchung wird ohne IFRS-Bewertung übernommen, im Konzernabschluss bricht das.
- Steuerliche Folgen (Maßgeblichkeit) übersehen.

## Querverweise

- `echtes-und-unechtes-factoring-risikoverteilung`
- `factoringvertrag-rahmenvertrag-forderungskauf-kaufpreis-sicherhe`
- `factoringtyp-true-false-reverse-maturity`
- `full-service-factoring-inhouse-factoring-ausschnittsmodell`

## Quellen Stand 06/2026

- HGB §§ 246, 252, 290 zur Bilanzierung und Konsolidierung.
- IDW RS HFA 8 zur Bilanzierung von Forderungsverkäufen.
- IFRS 9 zu Financial Instruments (Risk-and-Reward, Control-Test).
- IFRS 10 zur Konsolidierung von Zweckgesellschaften.
- IDW Stellungnahmen und Veröffentlichungen, jeweils in der aktuellen Fassung.
