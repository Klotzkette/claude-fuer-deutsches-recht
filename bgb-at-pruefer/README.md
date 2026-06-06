# BGB AT Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bgb-at-pruefer`) | [`bgb-at-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-at-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Anfechtung / Irrtum — Restaurant-Kette Pohlmann-Ofenkaess, Erbenstraße Leipzig** (`anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig`) | [Gesamt-PDF lesen](../testakten/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig/gesamt-pdf/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig_gesamt.pdf) | [`testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig.zip) |
| **BGB BT — Holzofen, Lieferkette, Bürgschaft, GoA und Brandschaden** (`bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt`) | [Gesamt-PDF lesen](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/gesamt-pdf/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt_gesamt.pdf) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip) |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Großes Prüfplugin zum BGB Allgemeiner Teil. Es führt durch Vertragsschluss, Willenserklärungen, Zugang, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung. Der Formteil ist mit qES, beA, § 130e ZPO und § 46h ArbGG verschaltet. Neu verschaltet sind digitale Elemente, Updatehinweise, App-/Portalzugang, Reparaturverlangen und Right-to-Repair-Fragen als allgemeinzivilrechtlicher Router in BGB-BT, AGB-Recht und Produktrecht. Ziel ist ein schöner, schneller und trotzdem präziser Workflow für Klausur, Ausbildung, Kanzleivermerk und Mandatsarbeit.

Experimentelles Werkzeug. Keine Rechtsberatung, keine Gewähr. Gesetzestext und Rechtsprechung müssen im konkreten Fall geprüft werden. Literatur- oder Kommentarstellen dürfen nur genutzt werden, wenn sie vom Nutzer bereitgestellt wurden oder über eine lizenzierte Quelle live verifiziert sind.

## Schnellstart

/plugin install bgb-at-pruefer@claude-fuer-deutsches-recht

Starte mit dem Skill [Kaltstart-Triage](./skills/kaltstart-triage/SKILL.md). Der Einstieg fragt den Fall in einer kompakten Reihenfolge ab, baut eine Themenkarte und schlägt danach die passenden Spezial-Skills vor.

## Was das Plugin besonders gut kann

- aus einem unsortierten BGB-AT-Sachverhalt einen Anspruchsbaum bauen
- Angebot, Annahme, Zugang, Fristen und digitale Erklärungsketten auseinanderziehen
- Minderjährigenfälle mit §§ 104-113 BGB sauber prüfen
- Anfechtung mit Auslegung, Frist, Gegner und Folgen prüfen
- Stellvertretung, Vollmacht, Rechtsschein und § 181 BGB trennen
- Form, Nichtigkeit, Gesetzesverbot, Sittenwidrigkeit und Bedingung als Wirksamkeitsfragen einordnen
- elektronische Form, qES-Zugang, beA-Einreichung und prozessuale Formfiktion auseinanderhalten
- Waren mit digitalen Elementen, Updatehinweise, AGB-Abweichungen und Reparaturverlangen in die richtigen Spezial-Skills routen
- aus dem Ergebnis Gutachten, Mandatsmemo, Schriftsatzbaustein, Rückfragenbrief oder Trainingsfall machen

## Empfohlener Workflow

1. Fallfrage festnageln: Wer will was von wem, und auf welcher Anspruchsebene liegt das Problem?
2. Erklärungskette bauen: Jede Erklärung mit Datum, Kanal, Absender, Empfänger, Zugang und Inhalt erfassen.
3. BGB-AT-Themenkarte erstellen: Geschäftsfähigkeit, Willenserklärung, Vertragsschluss, Auslegung, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingung, Fristen.
4. Spezial-Skills laden: Der Allgemein-Skill schlägt zwei bis fünf passende Folge-Skills vor.
5. Arbeitsprodukt wählen: Klausurlösung, Memo, Schriftsatzbaustein, Fristenvermerk oder Training.

## Skill-Auswahl

Die früher sehr lange Einzelskill-Tabelle ist in verdichtete Kompendium-Skills überführt. Nutze für die Auswahl die automatisch gepflegte Übersicht unten; die Kompendien enthalten die früheren Einzelthemen als Unterabschnitte mit ihren Prüfprogrammen, Normankern und Ausgabeformaten.

## Quellen- und Aktualitätsanker

- Aktueller BGB-Gesetzestext: https://www.gesetze-im-internet.de/bgb/
- Interne Struktur: [references/bgb-at-pruefprogramm.md](./references/bgb-at-pruefprogramm.md)
- Rechtsstandsregel: [references/rechtsstand-und-quellen.md](./references/rechtsstand-und-quellen.md)

## Gute Begleiter

- [methodenlehre-buergerliches-recht](../methodenlehre-buergerliches-recht) für Auslegung, Gutachtenstil und Anspruchsdenken.
- [subsumtions-pruefer](../subsumtions-pruefer) für generische Tatbestandsarbeit.
- [schriftform-und-textform-bgb](../schriftform-und-textform-bgb) für tiefe Form-, Textform- und Zugangskonstellationen.
- [bereicherungs-und-anfechtungsrecht-pruefer](../bereicherungs-und-anfechtungsrecht-pruefer) für Rückabwicklung nach unwirksamem Vertrag.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abgabe-willenserklaerung` | Klausurfall zur Abgabe einer Willenserklärung nach §§ 116 ff. BGB: willentliche Entäußerung unter Anwesenden und Abwesenden, Botenproblematik, E-Mail und Plattform-Postfach, Widerruf vor Abgabe. Output: Gutachtenstil-Lösung mit Subsumtio... |
| `agb-einbeziehung-amtlicher-zpo-anfechtung` | Prüft AGB-Einbeziehung nach §§ 305 bis 310 BGB: ausdrücklicher und konkludenter Hinweis, zumutbare Kenntnisnahmemöglichkeit, Überraschungsklauseln § 305c BGB, Inhaltskontrolle §§ 307 bis 309 BGB. Klausurfall mit vollständiger Subsumtions... |
| `agb-einbeziehung-schnittstelle` | Prüft AGB-Einbeziehung nach §§ 305 bis 310 BGB: ausdrücklicher und konkludenter Hinweis, zumutbare Kenntnisnahmemöglichkeit, Überraschungsklauseln § 305c BGB, Inhaltskontrolle §§ 307 bis 309 BGB. Klausurfall mit vollständiger Subsumtions... |
| `amtlicher-bgb-zpo-normcheck` | Amtlicher Normcheck für BGB-AT-Fälle: gleicht Geschäftsfähigkeit, Willenserklärung, Form, Zugang, Vertragsschluss, Stellvertretung, Fristen, Verjährung und ZPO-Schnittstellen gegen die aktuelle Gesetze-im-Internet-Fassung ab im BGB AT: p... |
| `anfechtung-routing` | Routing-Skill für Anfechtung nach §§ 119 bis 124 und § 142 BGB: Prüfsituation in Klausur oder Mandat — Anfechtungsgrund bestimmen, Anfechtungserklärung und Gegner prüfen, Frist berechnen, Ausschlüsse und Folgen nach §§ 122 und 142 BGB da... |
| `anfechtung-vor-auslegung` | Klausurmethodik: Prüfungsreihenfolge Auslegung vor Anfechtung im BGB Allgemeiner Teil — Begründung des Vorrangs der Auslegung, Abgrenzung Inhaltsirrtum und falsa demonstratio, Konsequenzen für Klausuraufbau und Praxismandat. |
| `anfechtungsfolgen-paragraphen-142-122` | Klausurfall zu Anfechtungsfolgen nach §§ 142 und 122 BGB: ex-tunc-Nichtigkeit des angefochtenen Rechtsgeschäfts, Rückabwicklung nach §§ 812 ff. BGB, Vertrauensschaden des Anfechtungsgegners und Abgrenzung zum Erfüllungsinteresse. |
| `anfechtungsfolgen-paragraphen-anspruchsaufbau` | Klausurfall zu Anfechtungsfolgen nach §§ 142 und 122 BGB: ex-tunc-Nichtigkeit des angefochtenen Rechtsgeschäfts, Rückabwicklung nach §§ 812 ff. BGB, Vertrauensschaden des Anfechtungsgegners und Abgrenzung zum Erfüllungsinteresse im BGB A... |
| `anfechtungsfrist-erklaerung-annahmefrist` | Prüft Anfechtungsfrist und Bestätigungstatbestand: Frist bei Irrtumsanfechtung nach § 121 BGB (unverzüglich) und bei arglistiger Täuschung nach § 124 BGB (ein Jahr), Fristbeginn, Bestätigung nach § 144 BGB als Ausschlussgrund im BGB AT:... |
| `anfechtungsfrist-erklaerung-bestaetigung` | Prüft Anfechtungsfrist und Bestätigungstatbestand: Frist bei Irrtumsanfechtung nach § 121 BGB (unverzüglich) und bei arglistiger Täuschung nach § 124 BGB (ein Jahr), Fristbeginn, Bestätigung nach § 144 BGB als Ausschlussgrund. |
| `annahmefrist-verspaetung-paragraphen-147-149` | Klausurfall zur Annahmefrist nach §§ 147 bis 149 BGB: Annahme unter Anwesenden sofort, unter Abwesenden in angemessener Frist, verspätete Annahme als neues Angebot und Rechtsfolgen des Verspätungsanzeigeverzichts nach § 149 BGB. |
| `anspruchsaufbau-zivilrecht-bgb-at` | Strukturhilfe für den zivilrechtlichen Anspruchsaufbau im BGB Allgemeiner Teil: Anspruchsgrundlage lokalisieren, Tatbestandsmerkmale prüfen, Rechtsfolge feststellen, Einwendungen und Einreden abarbeiten. Klausurorientiert mit Gutachten-... |
| `auslegung-paragraphen-133-157` | Klausurfall zur Auslegung von Willenserklärungen und Verträgen nach §§ 133 und 157 BGB: natürliche Auslegung, normative Auslegung nach objektivem Empfängerhorizont, falsa demonstratio non nocet, ergänzende Vertragsauslegung bei Lücken. |
| `auslegung-sachverhalt-bgb-at-erklaerungskette` | Methodik zur Sachverhaltsanalyse und Fallfrage-Auslegung in BGB-AT-Klausuren: Trennung von Tatsachen und rechtlicher Qualifikation, Identifikation des relevanten Lebenssachverhalts, strukturierte Fallfragebeantwortung im Gutachtenstil im... |
| `auslegung-sachverhalt-und-fallfrage` | Methodik zur Sachverhaltsanalyse und Fallfrage-Auslegung in BGB-AT-Klausuren: Trennung von Tatsachen und rechtlicher Qualifikation, Identifikation des relevanten Lebenssachverhalts, strukturierte Fallfragebeantwortung im Gutachtenstil. |
| `bedingung-befristung-paragraphen-158-163` | Klausurfall zu Bedingung und Befristung nach §§ 158 bis 163 BGB: aufschiebende und auflösende Bedingung, Zeitbestimmung, Vereitelung des Bedingungseintritts nach § 162 BGB, Rückwirkung nach § 159 BGB und Zwischenverfügungen. |
| `cic-vorvertragliche-pflichten-schnittstelle` | Klausurfall zu culpa in contrahendo nach §§ 280 Abs. 1 und 311 Abs. 2 BGB: Aufnahme von Vertragsverhandlungen, vorvertragliche Aufklärungs- und Schutzpflichten, Verschulden bei Vertragsschluss und Schadensersatz bei Abbruch oder Täuschung. |
| `digitale-elemente-reparaturrecht-router` | Router-Skill für digitale Elemente und Reparaturrecht im BGB-AT-Kontext: Abgrenzung zu §§ 327 ff. BGB (Verträge über digitale Produkte), Zugang digitaler Erklärungen, elektronische Form und Schnittstelle zum allgemeinen Vertragsrecht. |
| `duldungs-anscheinsvollmacht` | Klausurfall zu Duldungs- und Anscheinsvollmacht im BGB AT nach BGH-Rechtsprechung: Voraussetzungen der Duldungsvollmacht (Kenntnis und Dulden), Anscheinsvollmacht (Erkennbarkeit bei pflichtgemäßer Sorgfalt) und Rechtsfolgen für Vertragsp... |
| `eigenschaftsirrtum-paragraph-119-2` | Klausurfall zum Eigenschaftsirrtum nach § 119 Abs. 2 BGB: Begriff der verkehrswesentlichen Eigenschaft einer Person oder Sache, Abgrenzung zum Motivirrtum, Wertirrtum und Eigenschaftsirrtum bei Kunstwerken und Vertragspersonen. |
| `eigenschaftsirrtum-paragraph-einseitige` | Klausurfall zum Eigenschaftsirrtum nach § 119 Abs. 2 BGB: Begriff der verkehrswesentlichen Eigenschaft einer Person oder Sache, Abgrenzung zum Motivirrtum, Wertirrtum und Eigenschaftsirrtum bei Kunstwerken und Vertragspersonen im BGB AT:... |
| `einseitige-geschaefte-minderjaehrige` | Klausurfall zu einseitigen Rechtsgeschäften Minderjähriger nach § 111 BGB: Kündigung, Anfechtung oder Rücktritt durch oder gegenüber Minderjährigem, sofortige Verwerfung ohne Einwilligung, Unterschied zum zweiseitigen Vertrag. |
| `einseitige-geschaefte-minderjaehrige-paragraph-111` | Klausurfall zu einseitigen Rechtsgeschäften Minderjähriger nach § 111 BGB: Kündigung, Anfechtung oder Rücktritt durch oder gegenüber Minderjährigem, sofortige Verwerfung ohne Einwilligung, Unterschied zum zweiseitigen Vertrag im BGB AT:... |
| `einwilligung-genehmigung-paragraphen-107` | Klausurfall zu Einwilligung und Genehmigung bei beschränkt Geschäftsfähigen nach §§ 107 bis 109 BGB: schwebende Unwirksamkeit, Genehmigungsfiktion nach § 108 Abs. 2 BGB, Widerrufsrecht des Vertragspartners und Wirkung der Genehmigung ex... |
| `einwilligung-genehmigung-paragraphen-107-bis-109` | Klausurfall zu Einwilligung und Genehmigung bei beschränkt Geschäftsfähigen nach §§ 107 bis 109 BGB: schwebende Unwirksamkeit, Genehmigungsfiktion nach § 108 Abs. 2 BGB, Widerrufsrecht des Vertragspartners und Wirkung der Genehmigung ex... |
| `elektronische-bea-elektronischer-zugang` | Prüfungslinie für elektronische form bea qes formfiktion: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im BGB AT: prüft konkret die einschlägige... |
| `elektronische-form-bea-qes-formfiktion` | Prüfungslinie für elektronische form bea qes formfiktion im BGB AT: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeit... |
| `elektronischer-zugang-und-plattformen` | Prüft elektronischen Zugang von Willenserklärungen nach § 130 BGB: E-Mail-Postfach, Plattform-Postfächer, automatisierte Systeme, Zeitpunkt der Kenntnisnahmemöglichkeit und Empfangsbereitschaft im B2B- und B2C-Bereich. |
| `ergaenzende-vertragsauslegung` | Klausurfall zur ergänzenden Vertragsauslegung nach §§ 133 und 157 BGB: planwidrige Regelungslücke feststellen, hypothetischen Parteiwillen ermitteln, Abgrenzung zu dispositiven Gesetzesnormen und Grenze der Auslegung zur richterlichen Re... |
| `erklaerungsbewusstsein-potentielles` | Klausurfall zu Erklärungsbewusstsein und potentiellem Erklärungsbewusstsein: Mindestvoraussetzung des Willenserklärungstatbestands, h.M. und Mindermeinung zum potentiellen Bewusstsein, Trierer Weinversteigerungsfall und Konsequenzen für... |
| `erklaerungsbewusstsein-und-potentielles-bewusstsein` | Klausurfall zu Erklärungsbewusstsein und potentiellem Erklärungsbewusstsein: Mindestvoraussetzung des Willenserklärungstatbestands, h.M. und Mindermeinung zum potentiellen Bewusstsein, Trierer Weinversteigerungsfall und Konsequenzen für... |
| `erklaerungskette-tableau` | Tableau zur Darstellung von Erklärungsketten im BGB Allgemeiner Teil: mehrstufige Willenserklärungen, Vertretungsketten, Genehmigungsvorgänge und Übertragungen. Strukturhilfe für Klausur und Mandatsaufnahme mit Flussdiagramm-Ansatz. |
| `erwerbsgeschaeft-dienst-arbeit` | Klausurfall zur Ermächtigung Minderjähriger zu Erwerbsgeschäften nach §§ 112 und 113 BGB: Ermächtigung zum selbstständigen Betrieb eines Erwerbsgeschäfts oder zur Dienstleistung/Arbeit, Umfang der Geschäftsfähigkeit und gerichtliche Gene... |
| `erwerbsgeschaeft-dienst-formnichtigkeit` | Klausurfall zur Ermächtigung Minderjähriger zu Erwerbsgeschäften nach §§ 112 und 113 BGB: Ermächtigung zum selbstständigen Betrieb eines Erwerbsgeschäfts oder zur Dienstleistung/Arbeit, Umfang der Geschäftsfähigkeit und gerichtliche Gene... |
| `fallaufnahme-pruefprogramm-prozessform` | Strukturiertes Fallaufnahme- und Prüfprogramm für BGB-AT-Mandate und Klausuren: Sachverhalt vollständig erfassen, Mandatsrolle klären, Prüfprogramm erstellen, offene Tatsachenfragen identifizieren und Prüfungsschwerpunkte setzen im BGB A... |
| `fallaufnahme-und-pruefprogramm` | Strukturiertes Fallaufnahme- und Prüfprogramm für BGB-AT-Mandate und Klausuren: Sachverhalt vollständig erfassen, Mandatsrolle klären, Prüfprogramm erstellen, offene Tatsachenfragen identifizieren und Prüfungsschwerpunkte setzen. |
| `form-und-prozessform` | Klausurfall zu Formvorschriften nach §§ 125 bis 129 BGB und prozessualer Formfrage: Schriftform, notarielle Beurkundung, elektronische Form, Heilung von Formmängeln und Auswirkungen auf Beweisbarkeit und Prozess. |
| `formnichtigkeit-paragraphen-125-129` | Klausurfall zur Formnichtigkeit nach §§ 125 bis 129 BGB: gesetzliche und rechtsgeschäftliche Formvorschriften, vollständige oder teilweise Nichterfüllung, Teilnichtigkeit nach § 139 BGB, arglistige Berufung auf Formmangel und Heilungstat... |
| `fristen-berechnung-paragraphen-186-193` | Klausurfall zur Fristenberechnung nach §§ 186 bis 193 BGB: Beginn einer Frist, Ereignisfrist und Kalenderfrist, Fristablauf am letzten Tag, Verlängerung bei Sonn- und Feiertagen nach § 193 BGB und Berechnung von Anfechtungs- und Verjähru... |
| `geschaeftsfaehigkeit-paragraphen-104-bis-106` | Klausurfall zu Geschäftsfähigkeit nach §§ 104 bis 106 BGB: Geschäftsunfähigkeit unter sieben Jahren und bei dauerhafter Bewusstseinsabwesenheit, beschränkte Geschäftsfähigkeit von sieben bis siebzehn Jahren und Abgrenzungsfragen. |
| `gesetzesverbot-sittenwidrigkeit` | Klausurfall zu Gesetzesverstoß nach § 134 BGB und Sittenwidrigkeit nach § 138 BGB: Verbotsgesetze im Zivilrecht, Gesamtnichtigkeit oder Teilnichtigkeit, Wucher nach § 138 Abs. 2 BGB und Ausbeutungsgeschäfte mit sittenwidrigem Lohnabstand. |
| `gesetzesverbot-sittenwidrigkeit-gutachtenstil` | Klausurfall zu Gesetzesverstoß nach § 134 BGB und Sittenwidrigkeit nach § 138 BGB: Verbotsgesetze im Zivilrecht, Gesamtnichtigkeit oder Teilnichtigkeit, Wucher nach § 138 Abs. 2 BGB und Ausbeutungsgeschäfte mit sittenwidrigem Lohnabstand... |
| `gutachtenstil-und-klausurtechnik` | Methodik-Skill für Gutachtenstil und Klausurtechnik im Zivilrecht BGB AT: OTSE-Schema (Obersatz — Tatbestand — Subsumtion — Ergebnis), Urteilsstil vs. Gutachtenstil, häufige Aufbaufehler, Zeitmanagement und Schwerpunktsetzung. |
| `handeln-im-fremden-namen-offenkundigkeit` | Klausurfall zum Handeln im fremden Namen nach § 164 Abs. 1 BGB: Offenkundigkeitsprinzip, Abgrenzung zum Eigengeschäft, Handeln unter fremdem Namen und verdeckte Stellvertretung sowie Geschäft für den, den es angeht. |
| `insichgeschaeft-paragraph-181` | Klausurfall zum Insichgeschäft nach § 181 BGB: Selbstkontrahieren und Mehrfachvertretung, Ausnahmen bei lediglich rechtlich vorteilhaften Geschäften oder ausdrücklich gestatteten Insichgeschäften, BGH-Linie zur GmbH und schwebende Unwirk... |
| `insichgeschaeft-paragraph-irrtumsanfechtung` | Klausurfall zum Insichgeschäft nach § 181 BGB: Selbstkontrahieren und Mehrfachvertretung, Ausnahmen bei lediglich rechtlich vorteilhaften Geschäften oder ausdrücklich gestatteten Insichgeschäften, BGH-Linie zur GmbH und schwebende Unwirk... |
| `invitatio-ad-offerendum-und-werbung` | Klausurfall zur Abgrenzung von Angebot und invitatio ad offerendum nach §§ 145 bis 147 BGB: Werbung im Schaufenster und Online-Shop als bloße Aufforderung zur Angebotsabgabe, verbindliche Preisauszeichnung, automatisierte Bestellbestätig... |
| `irrtumsanfechtung-paragraph-119-1` | Klausurfall zur Irrtumsanfechtung nach § 119 Abs. 1 BGB: Inhaltsirrtum versus Erklärungsirrtum, Motivirrtum als unbeachtlicher Irrtum, Kausalität und Unverzüglichkeit, Schadensersatz nach § 122 BGB. Prüfraster für Examens- und Anwaltsprü... |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im BGB-AT-Prüfer. Fragt Fallfrage, Rolle, Anspruchsziel, Tatsachen, Fristen, Erklärungen, Beteiligte und Wunsch-Output ab, baut einen schönen Arbeitsplan und schlägt passende Fachmodule aus diesem... |
| `kauf-im-internet-und-auktionen` | Prüft Vertragsschluss beim Online-Kauf und Internet-Auktionen: invitatio ad offerendum vs. Angebot, automatisierte Annahmeerklärungen, eBay-Versteigerungsregeln nach § 156 BGB und BGH-Rechtsprechung zu Scheinversteigerungen, Fernabsatzre... |
| `klausurloesungen-fehlerdiagnose` | Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüfungsreihenfolge (Auslegung vor Anfechtung), übersehene Normen wie § 122 BGB und § 179 BGB, unvollständige Subsumtion.... |
| `klausurloesungen-fehlerdiagnose-konsens` | Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüfungsreihenfolge (Auslegung vor Anfechtung), übersehene Normen wie § 122 BGB und § 179 BGB, unvollständige Subsumtion.... |
| `konsens-dissens-paragraphen-154-155` | Prüft offenen und versteckten Dissens nach §§ 154 und 155 BGB: fehlende Einigung über Nebenpunkte, Vorbehalt der Beurkundung, ergänzende Vertragsauslegung als Heilungsmechanismus, Abgrenzung von Anfechtung und Dissens. Klausurfall mit Lö... |
| `minderjaehrige-fehlsubsumtion` | Klausurhilfe zu häufigen Fehlsubsumtionen bei Minderjährigen-Geschäften nach §§ 104 bis 113 BGB: Abgrenzung lediglich rechtlich vorteilhafter Geschäfte von neutralen und nachteiligen Geschäften, typische Klausurfehler und Korrekturansatz. |
| `missbrauch-vertretungsmacht` | Klausurfall zum Missbrauch der Vertretungsmacht: kollusives Zusammenwirken von Vertreter und Drittem zum Nachteil des Vertretenen, Kenntnis oder Kennenmüssen des Dritten, Rechtsfolge der Unwirksamkeit analog § 138 BGB oder § 242 BGB. BGH... |
| `output-gutachten-memo-schriftsatz` | Output-Skill für BGB-AT-Ergebnisse: Klausurlösung im Gutachtenstil, praxisnahes Mandatsmemo, Subsumtionsraster und Schriftsatzbaustein — abhängig vom Arbeitsziel und Mandantenkontext strukturiert aufbereitet. |
| `paragraphen-cic-vorvertragliche-ergaenzende` | Klausurfall zur Fristenberechnung nach §§ 186 bis 193 BGB: Beginn einer Frist, Ereignisfrist und Kalenderfrist, Fristablauf am letzten Tag, Verlängerung bei Sonn- und Feiertagen nach § 193 BGB und Berechnung von Anfechtungs- und Verjähru... |
| `personen-rechtsfaehigkeit-handlungsfaehigkeit` | Prüft Rechtsfähigkeit und Handlungsfähigkeit natürlicher und juristischer Personen nach §§ 1 bis 14 BGB: Beginn und Ende der Rechtsfähigkeit bei natürlichen Personen, Geschäftsfähigkeit §§ 104 bis 113 BGB, Deliktsfähigkeit § 828 BGB, Par... |
| `personen-rechtsfaehigkeit-privatautonomie` | Prüft Rechtsfähigkeit und Handlungsfähigkeit natürlicher und juristischer Personen nach §§ 1 bis 14 BGB: Beginn und Ende der Rechtsfähigkeit bei natürlichen Personen, Geschäftsfähigkeit §§ 104 bis 113 BGB, Deliktsfähigkeit § 828 BGB, Par... |
| `privatautonomie-trennungs-abstraktionsprinzip` | Klausurfall zu Privatautonomie, Trennungs- und Abstraktionsprinzip im BGB: Verpflichtungsgeschäft und Verfügungsgeschäft als rechtlich selbständige Akte, Kausalität und Abstraktion, Fehleridentität als Ausnahme, Kondiktion nach § 812 BGB... |
| `rechtlich-vorteilhaft-paragraph-107` | Klausurfall zu lediglich rechtlich vorteilhaften Rechtsgeschäften nach § 107 BGB: Minderjähriger erwirbt ohne Einwilligung des Vertreters, wenn das Geschäft keinen rechtlichen Nachteil bringt. Abgrenzung zu wirtschaftlichen Vorteilen, ge... |
| `rechtsschein-redteam` | Red-Team-Skill für Rechtsschein-Argumentation im BGB AT: Vollmachtsrechtsschein, Duldungs- und Anscheinsvollmacht nach BGH-Rechtsprechung, Entgegenstehende Argumente prüfen, schwache Rechtsschein-Positionen identifizieren. |
| `schweigen-erklaerungswert-stellvertretung` | Prüft den Erklärungswert des Schweigens im BGB: Schweigen als Ausnahme von der Regel keine Willenserklärung, kaufmännisches Bestätigungsschreiben, vertraglich vereinbarter Erklärungswert, § 362 HGB und Sonderfälle im Verbraucherrecht. Kl... |
| `schweigen-und-erklaerungswert` | Prüft den Erklärungswert des Schweigens im BGB: Schweigen als Ausnahme von der Regel keine Willenserklärung, kaufmännisches Bestätigungsschreiben, vertraglich vereinbarter Erklärungswert, § 362 HGB und Sonderfälle im Verbraucherrecht. Kl... |
| `stellvertretung-routing-paragraphen-164-181` | Routing-Skill zur Stellvertretung nach §§ 164 bis 181 BGB: Vollmachtserteilung und -erlöschen, Offenkundigkeit des Handelns im fremden Namen, Duldungs- und Anscheinsvollmacht, Vertreter ohne Vertretungsmacht §§ 177 bis 179 BGB und Insich... |
| `taeuschung-drohung-paragraph-123` | Klausurfall zur Anfechtung wegen arglistiger Täuschung oder widerrechtlicher Drohung nach § 123 BGB: Täuschungshandlung und Kausalität, Drohung mit dem versprochenen empfindlichen Übel, Anfechtungsfrist ein Jahr nach § 124 BGB und Aussch... |
| `taschengeld-paragraph-110` | Klausurfall zur Taschengeldparagraph nach § 110 BGB: Minderjähriger bewirkt Leistung aus eigenen Mitteln, die ihm zu freiem Verfügen überlassen wurden. Abgrenzung zu Schenkung, Aufwendungsersatz und zur beschränkten Geschäftsfähigkeit na... |
| `taschengeld-paragraph-uebermittlungsirrtum` | Klausurfall zur Taschengeldparagraph nach § 110 BGB: Minderjähriger bewirkt Leistung aus eigenen Mitteln, die ihm zu freiem Verfügen überlassen wurden. Abgrenzung zu Schenkung, Aufwendungsersatz und zur beschränkten Geschäftsfähigkeit na... |
| `training-fallvarianten` | Trainings-Skill mit Fallvarianten zu BGB-AT-Kernthemen für Examensvorbereitung: Variationen zu Geschäftsfähigkeit, Anfechtung, Stellvertretung und Zugang — unterschiedliche Schwierigkeitsgrade, Mustersubsumtionen und Selbstkontrollfragen. |
| `training-fallvarianten-digitale-elemente` | Trainings-Skill mit Fallvarianten zu BGB-AT-Kernthemen für Examensvorbereitung: Variationen zu Geschäftsfähigkeit, Anfechtung, Stellvertretung und Zugang — unterschiedliche Schwierigkeitsgrade, Mustersubsumtionen und Selbstkontrollfragen... |
| `uebermittlungsirrtum-paragraph-120` | Klausurfall zum Übermittlungsirrtum nach § 120 BGB: fehlerhafte Übermittlung durch Boten oder Fernkommunikation, Gleichstellung mit dem Erklärungsirrtum nach § 119 Abs. 1 BGB, Anfechtungsrecht des Erklärenden und Schadensersatz nach § 12... |
| `verfuegung-nichtberechtigter-paragraph-185` | Prüft Verfügung eines Nichtberechtigten nach § 185 BGB: Einwilligung und nachträgliche Genehmigung des Berechtigten, Heilung durch spätere Berechtigung, Abgrenzung zum gutgläubigen Erwerb nach §§ 932 ff. BGB. Klausurfall mit Subsumtionsr... |
| `verjaehrung-grundschema-paragraphen-194-218` | Klausurfall zum Verjährungsrecht nach §§ 194 bis 218 BGB: regelmäßige Verjährungsfrist drei Jahre nach § 195 BGB mit Fristbeginn § 199 BGB, Hemmung §§ 203 bis 213 BGB, Neubeginn § 212 BGB, Einrede der Verjährung und Folge nach § 214 BGB.... |
| `vertragsschluss-antrag-abgabe` | Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschungsgründe, Annahmefrist unter An- und Abwesenden, verspätete und abgeänderte Annahme sowie Zeitpunkt des Vertragsschlu... |
| `vertragsschluss-antrag-annahme` | Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschungsgründe, Annahmefrist unter An- und Abwesenden, verspätete und abgeänderte Annahme sowie Zeitpunkt des Vertragsschlu... |
| `vertreter-ohne-vertretungsmacht` | Klausurfall zum vollmachtlosen Vertreter nach §§ 177 bis 179 BGB: schwebende Unwirksamkeit des Vertreterhandelns, Genehmigung des Vertretenen nach § 177 BGB, Widerrufsrecht des Dritten nach § 178 BGB, Haftung des Vertreters auf Erfüllung... |
| `vertreter-ohne-vertretungsmacht-paragraphen-177-179` | Klausurfall zum vollmachtlosen Vertreter nach §§ 177 bis 179 BGB: schwebende Unwirksamkeit des Vertreterhandelns, Genehmigung des Vertretenen nach § 177 BGB, Widerrufsrecht des Dritten nach § 178 BGB, Haftung des Vertreters auf Erfüllung... |
| `vollmacht-erteilung-umfang-erloeschen` | Klausurfall zu Vollmachtserteilung, Vollmachtsumfang und Erlöschen der Vollmacht nach §§ 167 bis 169 BGB: Innen- und Außenvollmacht, Spezial- und Generalvollmacht, Widerruf, Erlöschen nach § 168 BGB und Rechtsscheinwirkung nach §§ 170 bi... |
| `willenserklaerung-tatbestand` | Klausurfall zum Tatbestand der Willenserklärung: objektiver Erklärungstatbestand, Rechtsbindungswille, Erklärungsbewusstsein und potentielles Bewusstsein, Abgrenzung zu Gefälligkeiten und sozialtypischem Verhalten. Prüfraster für §§ 116... |
| `willenserklaerung-wucher-ausbeutung-zugang` | Klausurfall zum Tatbestand der Willenserklärung: objektiver Erklärungstatbestand, Rechtsbindungswille, Erklärungsbewusstsein und potentielles Bewusstsein, Abgrenzung zu Gefälligkeiten und sozialtypischem Verhalten. Prüfraster für §§ 116... |
| `wucher-und-ausbeutung-paragraph-138-2` | Klausurfall zu Wucher und wucherähnlichen Geschäften nach § 138 Abs. 2 BGB: Leistung und Gegenleistung in auffälligem Missverhältnis, Ausbeutung einer Zwangslage oder Unerfahrenheit, subjektives Wucherelement, Abgrenzung zur Sittenwidrig... |
| `zugang-paragraph-130` | Klausurfall zum Zugang empfangsbedürftiger Willenserklärungen nach § 130 BGB: Machtbereich des Empfängers, gewöhnliche Kenntnisnahmemöglichkeit, Widerruf vor oder gleichzeitig mit Zugang, Empfangsbote, digitale Postfächer und Zugangsvere... |
| `zugangsvereitelung-annahmeverweigerung` | Zugangsvereitelung Annahmeverweigerung im Plugin Bgb At Pruefer im BGB AT: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `zugangsvereitelung-und-annahmeverweigerung` | Klausurfall zur Zugangsvereitelung und Annahmeverweigerung bei Willenserklärungen: bewusstes Abschneiden des Zugangswegs durch den Empfänger, fiktiver Zugang nach § 242 BGB, Abgrenzung zur Annahmeverweigerung bei körperlichen Leistungen... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
