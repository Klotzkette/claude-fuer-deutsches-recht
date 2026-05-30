# selbstvertreter-sozialgericht

## Direkt-Download

| Datei | Download |
| --- | --- |
| Plugin-ZIP (`selbstvertreter-sozialgericht`) | [selbstvertreter-sozialgericht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/selbstvertreter-sozialgericht.zip) |
| Kleine Testakte "Heizkosten und Eilantrag" | [testakte-selbstvertreter-sozialgericht-heizkosten-eilantrag.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-selbstvertreter-sozialgericht-heizkosten-eilantrag.zip) |

Die Testakte liegt im Repository unter [`testakten/selbstvertreter-sozialgericht-heizkosten-eilantrag/`](../testakten/selbstvertreter-sozialgericht-heizkosten-eilantrag/) und wird im Release als separates ZIP bereitgestellt. Sie ist **kein Teil des Plugins**, sondern nur Material zum Ausprobieren.

### Installation

1. `selbstvertreter-sozialgericht.zip` herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `selbstvertreter-sozialgericht.zip` hochladen.

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

Ein Plugin für Bürgerinnen und Bürger, die sich beim Sozialgericht selbst vertreten — ohne Anwalt. Es führt vom Bescheid über Widerspruch, Klage und Eilantrag bis zu Gutachten, Termin, Urteil und Berufung.

## Für wen ist das?

Sie sind versichert oder beziehen Sozialleistungen. Sie haben einen Bescheid bekommen und sind nicht einverstanden. Sie haben keinen Anwalt oder können sich keinen leisten. Dieses Plugin hilft Ihnen Schritt für Schritt.

## Was leistet das Plugin?

- Sie bekommen einen Anfänger-Workflow, der Bescheid, Frist, Notlage und nächste Schritte in einfacher Sprache ordnet.
- Sie lernen, wie das Widerspruchsverfahren läuft.
- Sie lernen, wie eine Klage beim Sozialgericht funktioniert.
- Sie lernen, wann ein Eilantrag nötig ist.
- Sie verstehen die wichtigsten Bereiche: Pflegegrad, Krankenkasse, Bürgergeld, Erwerbsminderungs-Rente, Grad der Behinderung.
- Sie können vor dem Absenden einen Sanity-Check durchführen.
- Sie können Rechtsprechung mit dem Rechtsprechungschat einordnen, ohne Fundstellen zu erfinden.
- Sie sehen mit dem Zulassungsgrenzen-Check, ob Berufung, Nichtzulassungsbeschwerde oder BSG-Verfahren realistisch sind.
- Sie sehen, wann Sie doch besser einen Anwalt, Sozialverband, Beratungshilfe oder PKH nutzen sollten.

## Doppelt einfache Sprache

Jede Skill hat einen extra Block "In einfacher Sprache". Dort stehen ganz kurze Sätze. Pro Satz nur ein Gedanke. So können auch Menschen mit wenig Lese-Übung mitkommen.

## Wichtig vorweg

- Vor dem Sozialgericht und dem Landessozialgericht brauchen Sie keinen Anwalt (§ 73 SGG).
- Das Verfahren ist für Versicherte und Leistungsempfänger kostenfrei (§ 183 SGG).
- Das Gericht ermittelt die Wahrheit selbst (Amtsermittlung § 103 SGG). Das hilft Laien.
- Sie können die Klage auf der Geschäftsstelle des Sozialgerichts diktieren (§ 90 SGG).

## Was kann das Plugin nicht?

- Keine richtige Rechtsberatung. Bei kniffligen Fällen brauchen Sie eine Anwältin oder einen Anwalt.
- Keine Garantie, dass Sie gewinnen.
- Keine Pruefung Ihres Bescheids im Einzelnen.

Bei Unsicherheit: Wenden Sie sich an eine Beratungsstelle (Sozialverband VdK, SoVD, Diakonie, Caritas) oder beantragen Sie Beratungshilfe. Bei BSG-Verfahren besteht Vertretungszwang; bei schwierigen medizinischen Gutachten ist anwaltliche oder verbandliche Hilfe oft sinnvoll.

## Aufbau einer Skill

1. Worum geht es?
2. In einfacher Sprache (3 bis 5 kurze Saetze)
3. Wann brauchen Sie diese Skill?
4. Fachbegriffe
5. Rechtsgrundlagen
6. Schritt-fuer-Schritt-Anleitung
7. Worauf Sie besonders achten muessen
8. Typische Fehler
9. Querverweise
10. Quellen und Aktualitaet

## Stand

Mai 2026. Hinweise zu Reformen sind eingebaut. Bei Unsicherheit prüfen Sie unter www.sozialgerichtsbarkeit.de oder im aktuellen Gesetz.

## Lizenz

Apache-2.0 OR MIT.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 80 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Selbstvertreter-Sozialgericht-Plugin. Fragt Erfahrungslevel, Bescheid, Behörde, Ziel, Fristen, Notlage, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills vor und füh... |
| `amtsermittlungsgrundsatz-103-sgg` | Das Gericht ermittelt für Sie § 103 SGG. Amtsermittlung im Sozialprozess für Buerger ohne Anwalt ein grosser Vorteil. Was das Gericht von Amts wegen tut und was Sie trotzdem mitliefern. |
| `anfaenger-workflow-sozialgericht` | Geführter Anfänger-Workflow für Bürgerinnen und Bürger vor dem Sozialgericht: erklärt Bescheid, Widerspruch, Klage, Eilantrag, Amtsermittlung, Kostenfreiheit, Belege und Termin in einfacher Sprache und routet zu passenden Sozialgerichts-... |
| `anfechtungsklage-54-sgg` | Die Anfechtungsklage nach § 54 Abs. 1 SGG. Wann passt sie. Beispiele Bescheid weghaben Sanktion aufheben. Antrag Mustertext für Buerger ohne Anwalt. |
| `anlagen-bezeichnen-und-sortieren-sozialgericht` | Anlagen zur Klage richtig bezeichnen sortieren und nummerieren. K-Anlagen für Klaeger Anlagenverzeichnis Lesbarkeit. Tipps für Buerger im SG-Verfahren. |
| `anwaltskosten-bei-erfolg-erstattung` | Anwaltskosten bei Erfolg vor dem SG erstattet bekommen. RVG-Saetze Streitwert PKH Beiordnung. Praxis für Buerger und ihre Anwaelte. |
| `anwaltszwang-pruefen-73-sgg` | Brauchen Sie einen Anwalt vor dem Sozialgericht? § 73 SGG erklärt. Vor SG und LSG kein Anwaltszwang. Vor dem BSG aber schon. Was Sie als Buerger selbst machen koennen. |
| `arbeitslosengeld-i-sgb-iii` | Arbeitslosengeld I nach SGB III. Anspruch Sperrzeit Hoehe Wartezeit Arbeitsagentur. Streit um Sperrzeit oder Hoehe ALG I für Buerger ohne Anwalt. |
| `arztberichte-vorlegen-laien-leitfaden` | Arzt-Atteste und Befundberichte gezielt einholen und vorlegen. Was Sie vom Arzt erbitten und wie. Konkrete Formulierungen für Laien Mustertext. |
| `beratungshilfe-vor-widerspruch-brh` | Beratungshilfe nach BerHG für kostenlose Anwaltsberatung VOR Widerspruch und Klage. Antrag beim Amtsgericht Berechtigungsschein 15 EUR Eigenanteil. |
| `berufung-lsg-144-sgg-wertgrenze-750` | Berufung zum LSG nach § 144 SGG. Wertgrenze 750 EUR und laufende Leistungen über 1 Jahr. Mustertext für Buerger ohne Anwalt mit Hinweis auf Anwaltsempfehlung. |
| `berufung-zulassung-besondere-bedeutung` | Zulassung der Berufung trotz fehlender Wertgrenze. Grundsaetzliche Bedeutung Divergenz Verfahrensfehler § 144 Abs. 2 SGG. Praxis für Buerger ohne Anwalt. |
| `beweismittel-im-sozialgericht-uebersicht` | Welche Beweismittel gelten am SG. Urkundenbeweis Zeugen Sachverständige Augenscheinsobjekte Parteivernehmung. Praktische Tipps für Laien zum Beweis-Aufbau. |
| `buergergeld-jobcenter-sgb-ii` | Buergergeld nach SGB II. Streit mit Jobcenter zu Regelbedarf KdU Sanktion 2023-Reform Schonvermögen Karenzzeit. Praxis-Leitfaden Widerspruch Klage Eilantrag für Buerger. |
| `dokumenten-erzeugung-pdf-laien-sozialgericht` | PDF-Dateien für SG-Klage erstellen. Word zu PDF Fotos zu PDF Scannen mit Smartphone gratis Tools. Praktischer Leitfaden für Buerger ohne EDV-Kenntnisse. |
| `dolmetscher-beim-sozialgericht-laien` | Dolmetscher beim SG nach § 185 GVG. Kostenfrei für Buerger mit Sprachschwierigkeiten. Antrag muendliche Verhandlung Gebaerdensprache. |
| `eilantrag-86b-sgg-grundlagen` | Eilrechtsschutz nach § 86b SGG für Buerger. Aufschiebende Wirkung und einstweilige Anordnung. Anordnungsanspruch Anordnungsgrund existenzielle Leistungen Pflegegrad Buergergeld Krankenkasse. |
| `eilantrag-buergergeld-jobcenter` | Eilantrag beim SG gegen Jobcenter. Buergergeld gestoppt Sanktion Vorlaeufige Leistung. § 86b Abs. 2 SGG einstweilige Anordnung. Glaubhaftmachung Existenzminimum Mustertext. |
| `eilantrag-erfolgsaussichten-checkliste` | Checkliste zur Beurteilung Ihrer Eilantrags-Chancen vor dem Sozialgericht. Anordnungsanspruch und Anordnungsgrund Glaubhaftmachung typische Stolpersteine. |
| `eilantrag-krankenkassen-leistung` | Eilantrag wenn die Krankenkasse Behandlung Hilfsmittel oder Therapie ablehnt § 86b Abs. 2 SGG. Schwere und unumkehrbare Gesundheitsschaeden Mustertext für Buerger. |
| `eilantrag-pflegekassen-pflegehilfsmittel` | Eilantrag gegen Pflegekasse wenn Pflegehilfsmittel Pflegegrad oder Verhinderungspflege blockiert wird. § 86b Abs. 2 SGG Mustertext für betroffene Personen oder Angehoerige. |
| `einfache-sprache-tipps-fuer-alle-anliegen` | Tipps zur klaren und einfachen Sprache für eigene Schriftsaetze. Wie Sie verstaendlich formulieren ohne Behoerdendeutsch. Beispiele für Buerger. |
| `einreichung-fax-und-grenzen-sozialgericht` | Fax beim SG einreichen Vorteile und Grenzen. Sendebericht als Beweis Telefax-Nummer prüfen Frist halten. Hinweis Fax wird abgeschafft Alternativen vorhanden. |
| `einreichung-mein-justizpostfach-mjp-sozialgericht` | Mein Justizpostfach (MJP) für Buerger seit 2024. Online-Einreichung von Klagen und Schriftsaetzen beim Sozialgericht. Anmeldung Identifikation PDF-Anlagen Sicherheit. |
| `einreichung-papierform-sozialgericht-mit-abschriften` | Klage und Schriftsatz per Post beim SG einreichen. Abschriften für Gegner und Akte. Adressierung Einschreiben Empfangsbestätigung. Praktischer Versandweg für Buerger. |
| `entschaedigung-sgb-xiv-opferleistungen` | Soziales Entschaedigungsrecht SGB XIV seit 2024. Opfer von Gewalttaten Anerkennung Entschaedigung Reha. Reform OEG/BVG. Praktischer Leitfaden für Betroffene. |
| `erwerbsminderungs-rente-streit-sgb-vi` | EM-Rente nach §§ 43 240 SGB VI. Volle teilweise EM Wartezeit Pflichtbeitraege Berufsschutz vor 1961. Strategie für Buerger bei Ablehnung durch DRV. |
| `fahrtkosten-zeugen-pkh-erstattung` | Fahrtkosten Zeugenauslagen und Erstattungen im SG-Verfahren. JVEG für Zeugen Sachverständige und Sie selbst. Praktischer Leitfaden. |
| `feststellungsklage-55-sgg` | Die Feststellungsklage nach § 55 SGG. Wenn ein Rechtsverhältnis geklaert werden muss. Versicherungspflicht Versicherungsstatus berechtigtes Interesse Mustertext. |
| `fristen-berechnen-sgg-laien` | Alle wichtigen Fristen im SG-Verfahren ueberblicken. Widerspruch Klage Berufung Eilantrag Verlaengerung. Berechnungstipps für Buerger ohne Anwalt. |
| `fristenbuch-fuehren-laien-sozialgericht` | Fristen sicher organisieren und nicht verpassen. Fristenkalender Erinnerungen Excel Papier Smartphone. Praktischer Leitfaden für Buerger ohne Anwalt. |
| `fristverlaengerung-sozialgericht-laien` | Fristverlaengerung im SG-Verfahren beantragen. Welche Fristen sind verlaengerbar welche nicht. Mustertext für Buerger. Begründung Stellungnahme zum Gutachten. |
| `gerichtskostenfreiheit-183-sgg` | Kein Geld für das Gericht. § 183 SGG erklärt die Kostenfreiheit für Versicherte Leistungsempfaenger und Behinderte. Wer zahlt was und was nicht. Anwaltskosten Fahrtkosten Auslagen. |
| `grad-der-behinderung-gdb-sgb-ix` | Grad der Behinderung (GdB) Streit nach SGB IX. Versorgungsamt VMG Tabellen Merkzeichen G aG B H Bl Gl. Schwerbehindertenausweis ab GdB 50. Mustertext für Buerger. |
| `grundsicherung-sgb-xii` | Grundsicherung im Alter und bei Erwerbsminderung nach SGB XII. Sozialamt Antrag Bedarfsberechnung Vermögen. Abgrenzung zum Buergergeld für Buerger. |
| `klage-zur-niederschrift-90-sgg` | Klage auf der Geschäftsstelle des SG diktieren § 90 SGG. Wer kann das wie laeuft das ab welche Termine welche Unterlagen mitbringen. Praktischer Leitfaden für Buerger. |
| `klage-zusammenstellen-bundle-sozialgericht` | Komplette Klage als Paket zusammenstellen. Schriftsatz Anlagen Anlagenverzeichnis für Gericht und Gegner. Checkliste für Buerger ohne Anwalt. |
| `klagearten-uebersicht-sgg` | Welche Klage passt zu Ihrem Fall. Anfechtungs- Verpflichtungs- Leistungs- Feststellungs- und Untätigkeitsklage nach §§ 54 55 88 SGG. Mit Entscheidungshilfe und Mustern. |
| `klagebegruendung-laienleitfaden` | Wie Sie Ihre Klage ohne Anwalt sinnvoll begründen. Sachverhalt Rechtsverletzung Beweismittel Antrag Aufbau und Mustertexte für Buerger vor dem Sozialgericht. |
| `kostenfrei-vs-aufwendungsersatz-193-sgg` | Aufwendungsersatz nach § 193 SGG. Bei Erfolg muss Beklagte notwendige außergerichtliche Kosten erstatten. Anwalt Fahrtkosten Auslagenpauschale. Antrag stellen. |
| `kostenrisiko-vs-kostenfreiheit-laien` | Was kostet Sie ein SG-Verfahren wirklich? Gerichtskostenfreiheit § 183 SGG Anwaltskosten Gutachterkosten § 109 SGG Mutwilligkeit § 192 SGG. Überblick für Buerger. |
| `krankenkassen-leistungsablehnung-sgb-v` | Streit mit der Krankenkasse nach SGB V. Leistungsablehnung Behandlung Hilfsmittel Therapie Krankengeld. Mustertext für Buerger Widerspruch Klage. |
| `ladung-termin-sozialgericht-vorbereitung` | Die Ladung zum SG-Termin verstehen. Was steht im Brief was tun was mitbringen Anwesenheitspflicht Vertretung. Praktische Hinweise für Buerger ohne Anwalt. |
| `leistungsklage-54-sgg` | Die Leistungsklage nach § 54 Abs. 5 SGG. Wenn die Behoerde konkret zahlen oder handeln muss. Schlichte Geldforderung Beispiele Mustertext für Buerger. |
| `medizinische-gutachten-strategie-laien` | Strategie mit medizinischen Gutachten im SG-Verfahren. Wie laeuft Gutachten Welche Fragen welcher Arzt. Vorbereitung Untersuchung und Reaktion auf Gutachten. |
| `nichtzulassungsbeschwerde-bsg-160a-sgg` | Nichtzulassungsbeschwerde zum BSG nach § 160a SGG. Wenn LSG Revision nicht zugelassen hat. Grundsatzbedeutung Divergenz Verfahrensmangel mit Anwalt. |
| `oertliche-zustaendigkeit-57-sgg` | Welches Sozialgericht in welcher Stadt? § 57 SGG erklärt die örtliche Zuständigkeit. Wohnort Sitz der Behoerde Sondervorschriften. Wie Sie das richtige SG finden. |
| `orientierung-selbstvertreter-sozialgericht` | Einstieg für Bürger ohne Anwalt vor dem Sozialgericht. Überblick über Anfänger-Workflow, Widerspruch, Klage, Eilantrag, Pflegegrad, Krankenkasse, Bürgergeld, Erwerbsminderungsrente, GdB, Sanity-Check, Rechtsprechungschat, Rechtsmittelgre... |
| `pflegegrad-streit-mdk-pflegekasse-sgb-xi` | Pflegegrad-Streit nach SGB XI. MD-Gutachten Module Punkte für Pflegegrad 1 bis 5. Pflegeprotokoll Widerspruch Klage Eilantrag. Praxis-Leitfaden für Betroffene und Angehoerige. |
| `pkh-anwaltsbeiordnung-erfolgsaussicht` | Erfolgsaussicht in der PKH-Prüfung. Wann bewilligt das SG PKH wann nicht. Mutwilligkeit Beweise Klagebegründung als Hebel. Tipps für den Buerger ohne Anwalt. |
| `pkh-vor-sozialgericht-73a-sgg` | Prozesskostenhilfe (PKH) vor dem Sozialgericht § 73a SGG i.V.m. ZPO. Voraussetzungen Erfolgsaussicht Mutwilligkeit Erklärung wirtschaftlicher Verhältnisse Anwaltsbeiordnung. |
| `rechtsprechungschat-sozialgericht` | Geführter Rechtsprechungschat für Selbstvertreter im Sozialgerichtsverfahren. Hilft, BSG-, LSG-, BVerfG- und EuGH-Rechtsprechung zu Sozialleistungen, Eilrechtsschutz, Amtsermittlung, Gutachten und Berufung zu finden, zu verstehen und lai... |
| `revision-bsg-160-sgg` | Revision zum BSG § 160 SGG. Anwaltszwang Zulassung Grundsatzfrage. Wann lohnt das Verfahren. Hinweise für Buerger nach LSG-Urteil. |
| `sachverstaendigen-wahlrecht-109-sgg` | Eigenes Gutachten nach § 109 SGG. Versicherter kann eigenen Gutachter waehlen. Eigenkosten Erstattung Wann sinnvoll. Mustertext Antrag. |
| `saeumnis-im-termin-sozialgericht` | Wenn Sie zum SG-Termin nicht erscheinen koennen oder unterlassen haben. Folgen § 137 SGG Entschuldigung Wiedereinsetzung Verlegung. Tipps für Buerger. |
| `sanity-check-selbstvertretung-sozialgericht` | Letzter Sanity-Check vor Widerspruch, Klage, Eilantrag, Stellungnahme, Termin oder Berufung im Sozialgerichtsverfahren. Prüft Frist, Bescheidkette, richtige Klageart, Eilbedürftigkeit, Belege, medizinische Unterlagen, Antrag, Kostenfreih... |
| `sozialgericht-zustaendigkeit-51-sgg` | Welche Streitigkeiten gehoeren vor das Sozialgericht? § 51 SGG erklärt. Abgrenzung zu Verwaltungsgericht Arbeitsgericht Amtsgericht. Wann ist das SG zuständig und wann nicht. |
| `sozialleistungen-uebersicht-sgb` | Überblick aller Sozialleistungen und Sozialgesetzbuecher. SGB I bis SGB XIV. Wer ist zuständig für was. Welche Leistung in welchem Buch. Praktischer Leitfaden für Buerger. |
| `teilstattgabe-vollstattgabe-verstehen` | Was bedeutet Vollabhilfe Teilabhilfe Zurückweisung im Widerspruchsbescheid. Wie Sie die Entscheidung lesen und was wann zu tun ist. Mit Beispielen aus typischen Sozialleistungen. |
| `terminvorbereitung-laien-checkliste-sozialgericht` | Detaillierte Vorbereitung auf den SG-Termin. Was sage ich was nehme ich mit was muss ich vorher wissen. Vor allem zum Vortrag zum Antrag und zur Reaktion auf Fragen. |
| `typische-fehler-selbstvertreter-sozialgericht` | Die häufigsten Fehler von Buergern ohne Anwalt vor dem SG. Frist Form Belege Antrag. Liste der Stolpersteine und wie Sie sie vermeiden. |
| `unfallversicherung-bg-anerkennung-sgb-vii` | Streit mit der Berufsgenossenschaft SGB VII. Arbeitsunfall Wegeunfall Berufskrankheit Anerkennung MdE Rente Unfallrente. Praktischer Leitfaden für Versicherte. |
| `untaetigkeitsklage-88-sgg` | Die Untätigkeitsklage nach § 88 SGG. Wenn die Behoerde nichts tut nach 6 Monaten oder Widerspruchsbehoerde nach 3 Monaten. Mustertext und Praxis für Buerger. |
| `urteil-sozialgericht-was-jetzt` | Sie haben das Urteil des SG bekommen. Was bedeutet das was sind die naechsten Schritte. Berufung Revision oder akzeptieren. Praxis für Buerger. |
| `vergleich-vorschlag-101-sgg` | Vergleich im Sozialprozess § 101 SGG. Was bedeutet das wann lohnt es sich worauf achten Bedenkzeit Widerruf. Tipps für Buerger im Termin. |
| `verhalten-im-saal-sozialgericht-laienleitfaden` | Wie verhalte ich mich im Sitzungssaal des SG. Anrede Aufstehen Ehrenamtliche Richter ehrlich antworten ruhig bleiben. Praktischer Leitfaden für Buerger ohne Anwalt. |
| `verpflichtungsklage-54-sgg` | Die Verpflichtungsklage nach § 54 Abs. 1 SGG. Behoerde soll begehrten Bescheid erlassen. EM-Rente Pflegegrad GdB Beispiele Mustertext für Buerger. |
| `versand-selbst-zurechnung-laien-sozialgericht` | Beweise für den Versand sicher organisieren. Einlieferungsschein Rückschein Fax-Sendebericht MJP-Quittung Empfangsstempel. Aufbewahrung Frist-Sicherung. |
| `video-verhandlung-110a-sgg` | Video-Verhandlung beim SG nach § 110a SGG. Wer kann teilnehmen Technik Vorbereitung Verlauf. Praktische Hinweise für Buerger mit gesundheitlichen Einschraenkungen. |
| `wann-doch-anwalt-grenzfaelle-sozialgericht` | Wann sollten Sie als Buerger doch einen Anwalt einschalten. Komplexe medizinische Fragen mehrere Bescheide LSG-Verfahren Beratungshilfe PKH. Entscheidungshilfe. |
| `widerspruch-begruendung-laienleitfaden` | Wie Sie Ihren Widerspruch ohne Anwalt sinnvoll begründen. Tatsachen Beweismittel Gegenargumente. Aufbau Mustertexte und konkrete Beispiele für typische Streitthemen. |
| `widerspruch-gegen-gutachten-laien` | Wie Sie sich gegen ein negatives Gutachten wehren. Schriftliche Stellungnahme Frage nach Erlaeuterung neuer Beweisantrag. Schritte für den Buerger ohne Anwalt. |
| `widerspruch-ohne-anwalt-einreichen` | Wie und wo Sie den Widerspruch einreichen. Brief Einschreiben Fax Mein Justizpostfach persoenliche Abgabe zur Niederschrift. Sicherer Versandweg für Buerger ohne Anwalt. |
| `widerspruch-vorverfahren-78-sgg` | Das Vorverfahren nach § 78 SGG erklärt. Vor jeder Klage muessen Sie Widerspruch einlegen. Welche Behoerde was prüft und wie das Ganze ablaeuft. Mit Mustertext. |
| `widerspruchsbescheid-was-jetzt` | Sie haben den Widerspruchsbescheid bekommen. Was nun? Klagefrist 1 Monat § 87 SGG. Klage einreichen oder akzeptieren. Wegweiser für Buerger nach dem Widerspruchsbescheid. |
| `widerspruchsfrist-84-sgg` | Die Widerspruchsfrist nach § 84 SGG ist ein Monat. Hier lernen Sie genau Berechnung Bekanntgabefiktion vier Tage nach Postaufgabe Wochenenden Feiertage. Mit Beispielen. |
| `wiedereinsetzung-frist-67-sgg` | Wenn Sie eine Frist verpasst haben § 67 SGG Wiedereinsetzung in den vorigen Stand. Wann möglich was vortragen welche Beweise. Mit Mustertext für Buerger ohne Anwalt. |
| `wohngeld-und-sozialhilfe-grenzfaelle` | Abgrenzung Wohngeld zu Sozialhilfe. Wer bekommt was und welches Gericht ist zuständig. Wohngeld Verwaltungsgericht Sozialhilfe Sozialgericht. |
| `zeugenbeweis-sozialgericht-373-zpo-analog` | Zeugen vor dem Sozialgericht. §§ 373 ff. ZPO analog. Beweisthema Adressen Zeugenvernehmung. Wann lohnt sich Zeugenbeweis für Buerger ohne Anwalt. |
| `zulassungsgrenzen-check-sozialgericht` | Zulassungs- und Rechtsmittelgrenzen im Sozialgerichtsverfahren: § 144 SGG 750 EUR, laufende Leistungen über ein Jahr, Erstattungsstreitigkeiten 10.000 EUR, Berufungszulassung, Nichtzulassungsbeschwerde, Revision, BSG-Anwaltszwang und Kos... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
