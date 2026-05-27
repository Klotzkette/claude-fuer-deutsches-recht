---
name: allgemein
description: "Einstieg und Orientierung im Bereicherungs- und Anfechtungsrecht-Prüfer-Plugin. Klärt Weichenstellung zwischen §§ 812 ff. BGB, AnfG und §§ 129-147 InsO, KI-Screening von Schuldnerakten, § 135 Gesellschafterdarlehen, Verteidigung des Anfechtungsgegners und Routing zu allen 43 Spezial-Skills."
---

# Bereicherungs- und Anfechtungsrecht-Prüfer — Allgemein

## Worum geht es?

Dieses Plugin prueft mechanisch, welcher Regelungskreis bei Vermoegensverschie­bungen einschlaegig ist: das Bereicherungsrecht der §§ 812 ff. BGB, die ausserinsolvenzliche Glaeubigeranfechtung nach dem AnfG oder die Insolvenzanfechtung nach §§ 129 bis 147 InsO. Es unterstuetzt Anwaelte und Berater bei der Subsumtion, bei der Anspruchsformulierung und bei der Erstellung von Schriftsaetzen. Das Plugin ersetzt keine Rechtsberatung und gibt keinen Rechtsrat an Mandanten.

Die Weichenstellung zwischen den drei Regelungskreisen ist die haeufigste Fehlerquelle in der Praxis: Ein Bereicherungsanspruch setzt keinen Titel voraus und keinen Insolvenzantrag; eine AnfG-Anfechtung benoetigt einen vollstreckbaren Titel ausserhalb der Insolvenz; eine InsO-Anfechtung setzt ein eroeffnetes Insolvenzverfahren voraus. Dieses Plugin arbeitet diese Abgrenzung systematisch durch.

## Wann brauchen Sie diese Skill?

- Sie wollen pruefen, ob eine Vermoegenverschiebung bereicherungsrechtlich, ausserinsolvenzlich oder insolvenzrechtlich angegriffen werden kann.
- Sie sind Insolvenzverwalter und pruefen Anfechtungsansprueche gegen Glaeubiger oder Dritte.
- Sie sind Vollstreckungsglaeubiger und wollen eine Vermoegensverschiebung des Schuldners anfechten (AnfG).
- Sie muessen als Anfechtungsgegner Verteidigungsargumente strukturieren.
- Sie erstellen Klageschriften, Anfechtungsanzeigen oder Warnhinweise in bereicherungs- oder anfechtungsrechtlichen Mandaten.

## Fachbegriffe (kurz erklaert)

- **Leistungskondiktion** — Rueckforderungsanspruch wegen einer Leistung ohne Rechtsgrund (§ 812 Abs. 1 S. 1 Alt. 1 BGB); setzt bewusste und zweckgerichtete Vermehrung fremden Vermoegens voraus.
- **Eingriffskondiktion** — Bereicherungsanspruch bei Eingriff in eine fremde Rechtsposition mit Zuweisungsgehalt ohne Leistungsbeziehung (§ 812 Abs. 1 S. 1 Alt. 2 BGB).
- **Entreicherung** — Einrede des Bereicherten, soweit er das Erlangte nicht mehr hat (§ 818 Abs. 3 BGB); bei Boesglaeuigkeit ausgeschlossen (§ 819 BGB).
- **AnfG-Anfechtung** — Ausserinsolvenzliche Glaeubigeranfechtung durch Vollstreckungsglaeubiger mit Titel; schuetzt vor Vereitelung der Zwangsvollstreckung.
- **Kongruente Deckung** — Befriedigung oder Sicherung, die dem Glaeubiger so zustand; nach § 130 InsO anfechtbar bei Zahlungsunfaehigkeit und Kenntnis.
- **Inkongruente Deckung** — Befriedigung oder Sicherung, die so nicht oder nicht zu der Zeit beansprucht werden konnte (§ 131 InsO); erleichterte Anfechtbarkeit.
- **Bargeschäft** — unmittelbarer Austausch gleichwertiger Leistungen; schützt nach § 142 InsO, bleibt bei § 133 InsO aber nur geschützt, wenn keine erkannte Unlauterkeit des Schuldners hinzukommt.
- **Vorsatzanfechtung** — Anfechtung wegen Benachteiligungsvorsatzes des Schuldners und Kenntnis des Anfechtungsgegners (§ 133 InsO bzw. § 3 AnfG); laengste Anfechtungsfrist.

## Rechtsgrundlagen

- §§ 812 bis 822 BGB — Bereicherungsrecht (Leistungs-, Nichtleistungskondiktion, Umfang, Ausschluesse).
- §§ 1 bis 15 AnfG — Ausserinsolvenzliche Glaeubigeranfechtung.
- §§ 129 bis 147 InsO — Insolvenzanfechtung (Grundtatbestand, Deckungsanfechtung, Vorsatz, Rechtsfolgen).
- § 142 InsO — Bargeschaeftsprivileg.
- §§ 195 und 199 BGB — Regelmaessige Verjaehrung drei Jahre, Beginn mit Jahresende.
- § 15 AnfG — Verjaehrung AnfG-Anfechtungsanspruch drei Jahre.
- § 146 InsO — Verjährung des Insolvenzanfechtungsanspruchs nach den Regeln der regelmäßigen Verjährung des BGB.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer hat was an wen geleistet, wann, gegen welche Gegenleistung?
2. Weichenstellung treffen: Liegt ein eroeffnetes Insolvenzverfahren vor? Liegt ein vollstreckbarer Titel vor?
3. Passenden Regelungskreis auswaehlen: Skill `weichenstellung-bereicherung-oder-anfechtung` oder `triage-vermoegensverschiebung-erfassen`.
4. Fristen pruefen: Skill `verjaehrung-bereicherung-anfechtung-fristen`.
5. Anspruchsgutachten oder Schriftsatz erstellen mit dem Spezial-Skill des gewaaehlten Regelungskreises.

## Skill-Tour (was gibt es hier?)

**Triage und Weichenstellung**

- `triage-vermoegensverschiebung-erfassen` — Erster Schritt zur strukturierten Erfassung der Vermoegenverschiebung fuer alle drei Regelungskreise.
- `weichenstellung-bereicherung-oder-anfechtung` — Triage-Entscheidung: welcher Regelungskreis ist einschlaegig.
- `falsche-wiese-warnung-bereicherung-anfechtung` — Erkennt typische Falschverortungen und leitet zum richtigen Regelungskreis weiter.
- `parallel-und-konkurrenz-pruefung` — Prueft alle drei Regelungskreise gleichzeitig auf Anspruchskonkurrenzen.

**Bereicherungsrecht — Grundtatbestaende**

- `leistungskondiktion-grundtatbestand-812-i-1-alt-1` — Leistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 1 BGB im Vier-Schritt-Schema.
- `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` — Nichtleistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 2 BGB.
- `leistungsbegriff-bewusste-zweckgerichtete-mehrung` — Definiert den Leistungsbegriff im Bereicherungsrecht.
- `eingriffskondiktion-zuweisungsgehalt` — Eingriffskondiktion bei Eingriff in fremde Rechtspositionen.

**Bereicherungsrecht — Spezialtatbestaende**

- `condictio-indebiti-813-bgb` — Rueckforderung trotz Erfuellung einer einredebehafteten Verbindlichkeit.
- `verfuegung-eines-nichtberechtigten-816-bgb` — Anspruch des Berechtigten nach § 816 BGB.
- `bereicherung-eines-dritten-822-bgb` — Bereicherungsanspruch gegen Dritten bei unentgeltlicher Weitergabe.
- `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` — Bereicherungsausgleich in Drei- und Mehrpersonenverhaeltnissen.

**Bereicherungsrecht — Umfang und Ausschluesse**

- `umfang-der-herausgabe-818-bgb-und-entreicherung` — Umfang der Bereicherungshaftung und Entreicherungseinrede.
- `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` — Verschaerfte Haftung bei Boesglaeuigkeit oder Rechtshaengigkeit.
- `ausschluss-814-bgb-kenntnis-der-nichtschuld` — Ausschluss bei Kenntnis der Nichtschuld.
- `ausschluss-817-bgb-gesetzes-und-sittenverstoss` — Ausschluss bei eigenem Gesetzes- oder Sittenverstoss.

**Bereicherungsrecht — Konkurrenz**

- `konkurrenz-bereicherung-vertraglich-deliktisch` — Verhaeltnis Bereicherungsrecht zu vertraglichen und deliktischen Anspruechen.
- `konkurrenz-bereicherung-anfechtung-und-vindikation` — Anspruchskonkurrenzen zwischen Bereicherungsrecht, Anfechtung und § 985 BGB.

**Ausserinsolvenzliche Anfechtung (AnfG)**

- `anfg-grundtatbestand-und-anfechtungsberechtigte` — Grundvoraussetzungen der ausserinsolvenzlichen Glaeubigeranfechtung.
- `anfg-vorsatzanfechtung-3-i` — Vorsatzanfechtung nach § 3 Abs. 1 AnfG mit Zehn-Jahres-Frist.
- `anfg-unentgeltliche-leistung-4` — Anfechtung unentgeltlicher Leistungen nach § 4 AnfG.
- `anfg-mittelbare-benachteiligung-und-kongruenz` — Kongruenz und mittelbare Glaeubigerbenachteiligung im AnfG.
- `anfg-rechtsfolge-rueckgewaehr-11` — Duldungspflicht und Wertersatz nach § 11 AnfG.
- `anfg-fristen-und-anfechtungszeitraum` — Anfechtungsfristen im AnfG: zehn Jahre Vorsatz, vier Jahre unentgeltlich.
- `anfg-einreden-und-verteidigung-anfechtungsgegner` — Verteidigung des Anfechtungsgegners gegen AnfG-Klage.
- `anfg-anfechtungsklage-prozessuales` — Prozessuales zur AnfG-Anfechtungsklage.

**Insolvenzanfechtung (§§ 129 ff. InsO)**

- `inso-grundtatbestand-129-glaeubigerbenachteiligung` — Grundtatbestand Insolvenzanfechtung: Rechtshandlung und Glaeubigerbenachteiligung.
- `inso-kongruente-deckung-130` — Kongruente Deckungsanfechtung nach § 130 InsO.
- `inso-inkongruente-deckung-131` — Inkongruente Deckungsanfechtung nach § 131 InsO.
- `inso-unmittelbar-nachteilige-rechtshandlungen-132` — Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO.
- `inso-vorsatzanfechtung-133` — Vorsatzanfechtung nach § 133 InsO mit Zehn-Jahres-Grundfrist, Vier-Jahres-Deckungsfrist und § 133 Abs. 3.
- `inso-unentgeltliche-leistung-134` — Anfechtung unentgeltlicher Leistungen nach § 134 InsO.
- `inso-gesellschafterdarlehen-135` — Gesellschafterdarlehen, gleichgestellte Forderungen, Drittdarlehen mit Gesellschaftersicherheit.
- `inso-bargeschaeft-142` — Bargeschäft nach § 142 InsO ohne starre 30-Tage-Regel.
- `inso-rechtsfolge-rueckgewaehr-143-bis-147` — Rechtsfolgen der Insolvenzanfechtung nach §§ 143 bis 147 InsO.
- `inso-ki-anfechtungsansprueche-schuldnerakten` — KI-gestütztes Screening von Schuldnerakten auf mögliche Anfechtungsansprüche mit Beleg- und Human-Review-Matrix.
- `inso-verteidigung-anfechtungsgegner` — Verteidigung gegen Insolvenzanfechtung aus Sicht des Anfechtungsgegners.

**Verjaehrung und Fristen**

- `verjaehrung-bereicherung-anfechtung-fristen` — Verjaehrungsfristen im Ueberblick fuer alle drei Regelungskreise.

**Output-Skills**

- `output-klageschrift-bereicherungsklage` — Klageschrift aus Bereicherungsrecht §§ 812 ff. BGB aufbauen.
- `output-anfechtungsanzeige-insolvenzverwalter` — Anschreiben des Insolvenzverwalters an Anfechtungsgegner erstellen.
- `output-anfechtungsklage-anfg` — Klageschrift fuer AnfG-Anfechtungsklage des Vollstreckungsglaeubigers.
- `output-warnhinweis-und-pruefungsdokument` — Pflicht-Header und Warnblock fuer alle Pruefungsdokumente.

**Mandatssteuerung**

- `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` — Erkennt Komplexitaetsindikatoren und empfiehlt Fachanwalt.

## Worauf besonders achten

- **Weichenstellung zuerst** — Die Verwechslung von Bereicherungsrecht, AnfG und InsO-Anfechtung ist der haeufigste systematische Fehler; `weichenstellung-bereicherung-oder-anfechtung` immer zuerst aufrufen.
- **Insolvenzeroefffnung als Voraussetzung** — InsO-Anfechtung durch Insolvenzverwalter setzt eroeffnetes Verfahren voraus; ohne Eroeffnungsbeschluss ist nur AnfG einschlaegig.
- **Bargeschäft bei InsO-Anfechtung prüfen** — § 142 InsO schützt echten gleichwertigen Austausch; bei § 133 InsO zusätzlich erkannte Unlauterkeit prüfen.
- **Vorsatzanfechtung Reform 2017** — § 133 InsO wurde durch das Anfechtungsreformgesetz 2017 erheblich verändert; allgemeine Zehn-Jahres-Frist, Vier-Jahres-Frist für Deckungshandlungen und Zwei-Jahres-Regel bei § 133 Abs. 4 sauber trennen.
- **KI nur beleggebunden einsetzen** — KI darf Kandidaten und Indizien aus Schuldnerakten aufbereiten, aber § 133-Wertungen und komplexe Dreiecksverhältnisse nicht final entscheiden.
- **Entreicherungseinrede rechtzeitig pruefen** — § 818 Abs. 3 BGB wird haeufig vergessen; bei Boesglaeuigkeit (§ 819 BGB) greift sie jedoch nicht.

## Typische Fehler

- Mandant hat keinen Titel, will aber AnfG-Anfechtung betreiben — AnfG setzt vollstreckbaren Titel voraus.
- Bereicherungsanspruch wird geltend gemacht, obwohl ein vertraglicher Anspruch vorgeht und keine Subsidiaritaet ueberprueft wurde.
- Vorsatzanfechtung nach § 133 InsO wird mit der alten Rechtslage oder mit falscher Vier-Jahres-Pauschale argumentiert.
- Dreimonatsfrist des § 130 InsO wird von der Antragstellung, nicht von der Eroeffnung her berechnet.
- Warnhinweis auf fehlenden Rechtsberatungscharakter fehlt im Dokument.

## Querverweise

- `insolvenzrecht` — Fuer den uebergeordneten insolvenzrechtlichen Kontext (Eroeffnungsgruende, Antragspflicht).
- `insolvenzplan-starug-planwerkstatt` — Wenn Anfechtungsrisiken in der Plangestaltung beeinflusst werden sollen.
- `bereicherungs-und-anfechtungsrecht-pruefer` — Dieses Plugin ist bereits das spezialisierte Werkzeug.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB §§ 812 ff. in der geltenden Fassung
- InsO §§ 129 ff. in der Fassung nach dem AnfRefG 2017
- AnfG in der geltenden Fassung
