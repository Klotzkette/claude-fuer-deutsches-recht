# BGB AT Prüfer

Großes Prüfplugin zum BGB Allgemeiner Teil. Es führt durch Vertragsschluss, Willenserklärungen, Zugang, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung. Der Formteil ist mit qES, beA, § 130e ZPO und § 46h ArbGG verschaltet. Ziel ist ein schöner, schneller und trotzdem präziser Workflow für Klausur, Ausbildung, Kanzleivermerk und Mandatsarbeit.

Experimentelles Werkzeug. Keine Rechtsberatung, keine Gewähr. Gesetzestext und Rechtsprechung müssen im konkreten Fall geprüft werden. Literatur- oder Kommentarstellen dürfen nur genutzt werden, wenn sie vom Nutzer bereitgestellt wurden oder über eine lizenzierte Quelle live verifiziert sind.

## Direkt-Download

| Datei | Direkt-Download |
| --- | --- |
| **Plugin-ZIP: BGB AT Prüfer** | [bgb-at-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-at-pruefer.zip) |
| **Testakte: bgb at altfraenkische werkstatt** | [testakte-bgb-at-altfraenkische-werkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-at-altfraenkische-werkstatt.zip) |

Für den ZIP-Upload das einzelne Plugin-ZIP verwenden, nicht das komplette Repository-ZIP.

## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **bgb at altfraenkische werkstatt** | [testakte-bgb-at-altfraenkische-werkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-at-altfraenkische-werkstatt.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| BGB AT Prüfer (`bgb-at-pruefer`, dieses Plugin) | [bgb-at-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-at-pruefer.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Schnellstart

/plugin install bgb-at-pruefer@claude-fuer-deutsches-recht

Starte mit dem Skill [allgemein](./skills/allgemein/SKILL.md). Der Einstieg fragt den Fall in einer kompakten Reihenfolge ab, baut eine Themenkarte und schlägt danach die passenden Spezial-Skills vor.

## Was das Plugin besonders gut kann

- aus einem unsortierten BGB-AT-Sachverhalt einen Anspruchsbaum bauen
- Angebot, Annahme, Zugang, Fristen und digitale Erklärungsketten auseinanderziehen
- Minderjährigenfälle mit §§ 104-113 BGB sauber prüfen
- Anfechtung mit Auslegung, Frist, Gegner und Folgen prüfen
- Stellvertretung, Vollmacht, Rechtsschein und § 181 BGB trennen
- Form, Nichtigkeit, Gesetzesverbot, Sittenwidrigkeit und Bedingung als Wirksamkeitsfragen einordnen
- elektronische Form, qES-Zugang, beA-Einreichung und prozessuale Formfiktion auseinanderhalten
- aus dem Ergebnis Gutachten, Mandatsmemo, Schriftsatzbaustein, Rückfragenbrief oder Trainingsfall machen

## Empfohlener Workflow

1. Fallfrage festnageln: Wer will was von wem, und auf welcher Anspruchsebene liegt das Problem?
2. Erklärungskette bauen: Jede Erklärung mit Datum, Kanal, Absender, Empfänger, Zugang und Inhalt erfassen.
3. BGB-AT-Themenkarte erstellen: Geschäftsfähigkeit, Willenserklärung, Vertragsschluss, Auslegung, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingung, Fristen.
4. Spezial-Skills laden: Der Allgemein-Skill schlägt zwei bis fünf passende Folge-Skills vor.
5. Arbeitsprodukt wählen: Klausurlösung, Memo, Schriftsatzbaustein, Fristenvermerk oder Training.

## Skills

| Skill | Beschreibung |
| --- | --- |
| [allgemein](./skills/allgemein/SKILL.md) | Einstieg, Schnelltriage und Workflow-Routing im BGB-AT-Prüfer. Fragt Fallfrage, Rolle, Anspruchsziel, Tatsachen, Fristen, Erklärungen, Beteiligte und Wunsch-Output ab, baut einen schönen Arbeitsplan und schlägt passende Spezial-Skills aus diesem Plugin vor. |
| [bgb-at-fallaufnahme-und-pruefprogramm](./skills/bgb-at-fallaufnahme-und-pruefprogramm/SKILL.md) | Fallaufnahme für BGB-AT-Konstellationen mit sauberem Prüfprogramm: Sachverhalt, Anspruchsziel, Personen, Erklärungen, Kommunikationswege, Zeitpunkte, Form, Genehmigungen, Vollmachten, Anfechtung und Fristen. |
| [anspruchsaufbau-zivilrecht-bgb-at](./skills/anspruchsaufbau-zivilrecht-bgb-at/SKILL.md) | Anspruchsaufbau im Zivilrecht mit präziser Einordnung von BGB-AT-Themen in Anspruch entstanden, erloschen und durchsetzbar; vermeidet freischwebende Vorprüfungen und baut ein sauberes Gutachten. |
| [gutachtenstil-und-klausurtechnik](./skills/gutachtenstil-und-klausurtechnik/SKILL.md) | Gutachtenstil, Klausurtechnik und Schwerpunktsetzung für BGB AT: Obersatz, Definition, Subsumtion, Ergebnis, Streitstand nur wenn entscheidungserheblich, mit verständlicher Priorisierung. |
| [auslegung-sachverhalt-und-fallfrage](./skills/auslegung-sachverhalt-und-fallfrage/SKILL.md) | Sachverhalts- und Fallfrageauslegung bei BGB-AT-Fällen: trennt Tatsachen, Wertungen, Hinweise, Bearbeitervermerk und verdeckte Probleme, bevor materiellrechtlich geprüft wird. |
| [privatautonomie-trennungs-abstraktionsprinzip](./skills/privatautonomie-trennungs-abstraktionsprinzip/SKILL.md) | Grundlagen-Skill zu Privatautonomie, Rechtsgeschäft, Verpflichtung und Verfügung, Trennungs- und Abstraktionsprinzip; ordnet BGB-AT-Fragen in Vertrag, Verfügung und Rückabwicklung ein. |
| [personen-rechtsfaehigkeit-und-handlungsfaehigkeit](./skills/personen-rechtsfaehigkeit-und-handlungsfaehigkeit/SKILL.md) | Prüft Rechtsfähigkeit, Verbraucher- und Unternehmerrolle, Wohnsitz, Organe und Handlungsfähigkeit als Vorfragen für BGB-AT-Fälle und Vertragsprüfungen. |
| [geschaeftsfaehigkeit-paragraphen-104-bis-106](./skills/geschaeftsfaehigkeit-paragraphen-104-bis-106/SKILL.md) | Prüfung von Geschäftsunfähigkeit und beschränkter Geschäftsfähigkeit nach §§ 104 bis 106 BGB mit Altersgrenzen, natürlicher Einsichtsfähigkeit und Rechtsfolge für Willenserklärungen. |
| [rechtlich-vorteilhaft-paragraph-107](./skills/rechtlich-vorteilhaft-paragraph-107/SKILL.md) | Prüft § 107 BGB: rechtlich lediglich vorteilhafte Geschäfte Minderjähriger, rechtliche Nachteile, neutrale Geschäfte und Abgrenzung zu wirtschaftlicher Vorteilhaftigkeit. |
| [taschengeld-paragraph-110](./skills/taschengeld-paragraph-110/SKILL.md) | Prüft § 110 BGB beim Minderjährigen: Bewirken der vertragsmäßigen Leistung mit überlassenen Mitteln, Raten, Kredit, Teilzahlung, digitale Zahlungen und Genehmigungsrisiken. |
| [einwilligung-genehmigung-paragraphen-107-bis-109](./skills/einwilligung-genehmigung-paragraphen-107-bis-109/SKILL.md) | Prüft Einwilligung, Genehmigung, schwebende Unwirksamkeit und Widerruf bei Minderjährigengeschäften nach §§ 107 bis 109 BGB mit sauberem Fristen- und Erklärungsrouting. |
| [einseitige-geschaefte-minderjaehrige-paragraph-111](./skills/einseitige-geschaefte-minderjaehrige-paragraph-111/SKILL.md) | Prüft einseitige Rechtsgeschäfte Minderjähriger nach § 111 BGB, insbesondere Kündigung, Anfechtung, Rücktritt, Vollmachtserteilung und Zugang gegenüber dem Minderjährigen. |
| [erwerbsgeschaeft-dienst-arbeit-paragraphen-112-113](./skills/erwerbsgeschaeft-dienst-arbeit-paragraphen-112-113/SKILL.md) | Prüft §§ 112 und 113 BGB bei Minderjährigen im Erwerbsgeschäft, Dienst- oder Arbeitsverhältnis einschließlich Reichweite der Ermächtigung und Abgrenzung zu Einzelgeschäften. |
| [willenserklaerung-tatbestand](./skills/willenserklaerung-tatbestand/SKILL.md) | Prüft den Tatbestand der Willenserklärung: objektiver Erklärungstatbestand, Handlungswille, Erklärungsbewusstsein, Geschäftswille, Rechtsbindungswille und Abgrenzung zur Gefälligkeit. |
| [erklaerungsbewusstsein-und-potentielles-bewusstsein](./skills/erklaerungsbewusstsein-und-potentielles-bewusstsein/SKILL.md) | Vertieft Erklärungsbewusstsein und potentielles Erklärungsbewusstsein bei versehentlichen Erklärungen, digitalen Klicks, Signaturen und Verkehrsschutz. |
| [abgabe-willenserklaerung](./skills/abgabe-willenserklaerung/SKILL.md) | Prüft Abgabe einer Willenserklärung unter Anwesenden und Abwesenden, Boten, E-Mail, Plattformen, Brief, Machtbereich und willentliche Entäußerung. |
| [zugang-paragraph-130](./skills/zugang-paragraph-130/SKILL.md) | Prüft Zugang empfangsbedürftiger Willenserklärungen nach § 130 BGB: Machtbereich, gewöhnliche Kenntnisnahmemöglichkeit, Widerruf, Empfangsbote und digitale Postfächer. |
| [elektronischer-zugang-und-plattformen](./skills/elektronischer-zugang-und-plattformen/SKILL.md) | Prüft elektronischen Zugang über E-Mail, Kundenportal, Messenger, Plattformkonto, Signaturdienst und automatisierte Systeme mit BGB-AT-Zugang, Form und Beweisrisiko. |
| [zugangsvereitelung-und-annahmeverweigerung](./skills/zugangsvereitelung-und-annahmeverweigerung/SKILL.md) | Prüft Zugangsvereitelung, Annahmeverweigerung, verspätete Kenntnisnahme und erneuten Zustellversuch bei empfangsbedürftigen Willenserklärungen. |
| [schweigen-und-erklaerungswert](./skills/schweigen-und-erklaerungswert/SKILL.md) | Prüft Schweigen als Nicht-Erklärung und Ausnahmen: kaufmännisches Bestätigungsschreiben, vereinbarte Erklärungswirkung, Treu und Glauben, AGB-Grenzen und Verbraucherschutz. |
| [vertragsschluss-antrag-annahme](./skills/vertragsschluss-antrag-annahme/SKILL.md) | Prüft Vertragsschluss durch Antrag und Annahme nach §§ 145 ff. BGB einschließlich essentialia negotii, Rechtsbindungswillen, Bindung und Annahmeerklärung. |
| [invitatio-ad-offerendum-und-werbung](./skills/invitatio-ad-offerendum-und-werbung/SKILL.md) | Grenzt Angebot von invitatio ad offerendum, Werbung, Preisschild, Katalog, Online-Shop, Plattformlisting und unverbindlicher Verhandlungsaufforderung ab. |
| [annahmefrist-verspaetung-paragraphen-147-149](./skills/annahmefrist-verspaetung-paragraphen-147-149/SKILL.md) | Prüft Annahmefrist, verspätete Annahme, verspätet zugegangene Annahme und Mitteilungspflichten nach §§ 147 bis 149 BGB. |
| [kauf-im-internet-und-auktionen](./skills/kauf-im-internet-und-auktionen/SKILL.md) | Prüft Vertragsschluss im Internet, Online-Auktion, Sofortkauf, Warenkorb, Bestellbutton, Bestätigungs-E-Mail und Plattformbedingungen im BGB-AT-Raster. |
| [konsens-dissens-paragraphen-154-155](./skills/konsens-dissens-paragraphen-154-155/SKILL.md) | Prüft Konsens, offenen und versteckten Dissens nach §§ 154 und 155 BGB sowie essentialia, Nebenpunkte, Auslegung und Vertragsrettung. |
| [auslegung-paragraphen-133-157](./skills/auslegung-paragraphen-133-157/SKILL.md) | Prüft Auslegung von Willenserklärungen und Verträgen nach §§ 133 und 157 BGB: wirklicher Wille, objektiver Empfängerhorizont, Treu und Glauben, Verkehrssitte und Kontext. |
| [ergaenzende-vertragsauslegung](./skills/ergaenzende-vertragsauslegung/SKILL.md) | Prüft ergänzende Vertragsauslegung bei planwidriger Lücke, hypothetischem Parteiwillen, dispositivem Recht und Grenzen zur unzulässigen Vertragsneuschöpfung. |
| [bedingung-befristung-paragraphen-158-163](./skills/bedingung-befristung-paragraphen-158-163/SKILL.md) | Prüft Bedingung und Befristung nach §§ 158 bis 163 BGB: aufschiebend, auflösend, Potestativbedingung, Bedingungsausfall, Treuwidrigkeit und Rechtsfolgen. |
| [formnichtigkeit-paragraphen-125-129](./skills/formnichtigkeit-paragraphen-125-129/SKILL.md) | Prüft Formvorschriften und Formnichtigkeit nach §§ 125 bis 129 BGB: gesetzliche Form, vereinbarte Form, Schriftform, elektronische Form, Textform, notarielle Form und Heilung. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| [gesetzesverbot-sittenwidrigkeit-paragraphen-134-138](./skills/gesetzesverbot-sittenwidrigkeit-paragraphen-134-138/SKILL.md) | Prüft Nichtigkeit wegen Gesetzesverstoß und Sittenwidrigkeit nach §§ 134 und 138 BGB mit Verbotszweck, Gesamtwürdigung, Teilnichtigkeit und Rückabwicklung. |
| [wucher-und-ausbeutung-paragraph-138-2](./skills/wucher-und-ausbeutung-paragraph-138-2/SKILL.md) | Prüft Wucher und wucherähnliche Geschäfte nach § 138 Abs. 2 BGB: auffälliges Missverhältnis, Schwächesituation, Ausbeutung, subjektive Kenntnis und Gesamtwürdigung. |
| [anfechtung-routing](./skills/anfechtung-routing/SKILL.md) | Routing-Skill für Anfechtung nach §§ 119 bis 124 und § 142 BGB: Anfechtungsgrund, Erklärung, Gegner, Frist, Ausschluss, Folgen und Alternativen. |
| [irrtumsanfechtung-paragraph-119-1](./skills/irrtumsanfechtung-paragraph-119-1/SKILL.md) | Prüft Inhalts- und Erklärungsirrtum nach § 119 Abs. 1 BGB einschließlich Abgrenzung zu Motivirrtum, Kalkulationsirrtum, Auslegung und Vertragsrisiko. |
| [eigenschaftsirrtum-paragraph-119-2](./skills/eigenschaftsirrtum-paragraph-119-2/SKILL.md) | Prüft Eigenschaftsirrtum nach § 119 Abs. 2 BGB: verkehrswesentliche Eigenschaften von Person oder Sache, Wertabgrenzung, Beschaffenheit und Gewährleistungs-Schnittstelle. |
| [uebermittlungsirrtum-paragraph-120](./skills/uebermittlungsirrtum-paragraph-120/SKILL.md) | Prüft § 120 BGB bei falscher Übermittlung durch Boten, technische Systeme, Übersetzung, Diktat, Plattformfehler und Kommunikationsketten. |
| [taeuschung-drohung-paragraph-123](./skills/taeuschung-drohung-paragraph-123/SKILL.md) | Prüft Anfechtung wegen arglistiger Täuschung oder widerrechtlicher Drohung nach § 123 BGB mit Kausalität, Dritten, Wissenszurechnung und Jahresfrist. |
| [anfechtungsfrist-erklaerung-bestaetigung](./skills/anfechtungsfrist-erklaerung-bestaetigung/SKILL.md) | Prüft Anfechtungserklärung, Anfechtungsgegner, Fristen nach §§ 121 und 124 BGB und Bestätigung nach § 144 BGB einschließlich Fristenlauf und Zugang. |
| [anfechtungsfolgen-paragraphen-142-122](./skills/anfechtungsfolgen-paragraphen-142-122/SKILL.md) | Prüft Folgen der Anfechtung nach §§ 142 und 122 BGB: rückwirkende Nichtigkeit, Vertrauensschaden, Kenntnis, Rückabwicklung, Kondiktion und Risikohinweise. |
| [stellvertretung-routing-paragraphen-164-181](./skills/stellvertretung-routing-paragraphen-164-181/SKILL.md) | Routing-Skill zur Stellvertretung nach §§ 164 bis 181 BGB: eigene Erklärung, fremder Name, Vertretungsmacht, Wissenszurechnung, Vollmacht, Missbrauch, Insichgeschäft und Vertreter ohne Vertretungsmacht. |
| [handeln-im-fremden-namen-offenkundigkeit](./skills/handeln-im-fremden-namen-offenkundigkeit/SKILL.md) | Prüft Handeln im fremden Namen und Offenkundigkeitsprinzip: ausdrückliche Offenlegung, unternehmensbezogenes Geschäft, Geschäft für den, den es angeht, und Eigengeschäft. |
| [vollmacht-erteilung-umfang-erloeschen](./skills/vollmacht-erteilung-umfang-erloeschen/SKILL.md) | Prüft Vollmachtserteilung, Innen-/Außenvollmacht, Umfang, Auslegung, Erlöschen, Widerruf, Rechtsschein und Nachweis der Vollmacht. |
| [duldungs-anscheinsvollmacht](./skills/duldungs-anscheinsvollmacht/SKILL.md) | Prüft Duldungs- und Anscheinsvollmacht als Rechtsscheinvertretung: zurechenbarer Rechtsschein, Vertrauen, Gutgläubigkeit und Abgrenzung zur bloßen Gefälligkeit. |
| [missbrauch-vertretungsmacht](./skills/missbrauch-vertretungsmacht/SKILL.md) | Prüft Missbrauch der Vertretungsmacht: Innenverstoß trotz Außenmacht, Evidenz, Kollusion, Treuwidrigkeit und Folgen für Vertrag und Haftung. |
| [insichgeschaeft-paragraph-181](./skills/insichgeschaeft-paragraph-181/SKILL.md) | Prüft § 181 BGB bei Insichgeschäft, Mehrvertretung, Selbstkontrahieren, Gestattung, Erfüllung einer Verbindlichkeit und Genehmigung. |
| [vertreter-ohne-vertretungsmacht-paragraphen-177-179](./skills/vertreter-ohne-vertretungsmacht-paragraphen-177-179/SKILL.md) | Prüft Vertreter ohne Vertretungsmacht nach §§ 177 bis 179 BGB: schwebende Unwirksamkeit, Genehmigung, Widerruf, Haftung des Vertreters und Minderjährigenschutz. |
| [verfuegung-nichtberechtigter-paragraph-185](./skills/verfuegung-nichtberechtigter-paragraph-185/SKILL.md) | Prüft Verfügung eines Nichtberechtigten nach § 185 BGB: Einwilligung, Genehmigung, Verfügungsbefugnis, Priorität, Eigentümerstellung und Rückwirkungsfragen. |
| [fristen-berechnung-paragraphen-186-193](./skills/fristen-berechnung-paragraphen-186-193/SKILL.md) | Berechnet Fristen nach §§ 186 bis 193 BGB: Ereignisfrist, Beginn, Ende, Wochen, Monate, Jahre, Sonnabend, Sonntag, Feiertag und dokumentierter Fristenvermerk. |
| [verjaehrung-grundschema-paragraphen-194-218](./skills/verjaehrung-grundschema-paragraphen-194-218/SKILL.md) | Prüft Verjährung nach §§ 194 bis 218 BGB: Anspruch, Fristdauer, Fristbeginn, Kenntnis, Hemmung, Neubeginn, Einrede, Nebenrechte und Rücktrittssperre. |
| [agb-einbeziehung-schnittstelle-paragraphen-305-310](./skills/agb-einbeziehung-schnittstelle-paragraphen-305-310/SKILL.md) | Schnittstellen-Skill zu AGB im BGB AT: Einbeziehung, überraschende Klausel, Vorrang der Individualabrede, Transparenz und Inhaltskontrolle als Folgeproblem. |
| [cic-vorvertragliche-pflichten-schnittstelle](./skills/cic-vorvertragliche-pflichten-schnittstelle/SKILL.md) | Schnittstellen-Skill zur culpa in contrahendo: vorvertragliches Schuldverhältnis, Schutzpflichten, Aufklärung, Abbruch von Verhandlungen und Abgrenzung zu BGB-AT-Wirksamkeitsfragen. |
| [bgb-at-output-gutachten-memo-schriftsatz](./skills/bgb-at-output-gutachten-memo-schriftsatz/SKILL.md) | Erstellt aus BGB-AT-Prüfungen wahlweise Gutachten, Klausurlösung, Mandatsmemo, Schriftsatzbaustein, Fristenvermerk, Anspruchsmatrix oder Rückfragenbrief. |
| [bgb-at-training-fallvarianten](./skills/bgb-at-training-fallvarianten/SKILL.md) | Erzeugt und variiert BGB-AT-Trainingsfälle mit anonymen, fiktiven Personen, Lernzielen, Lösungsskizze, Abwandlungen und typischen Fehlern für Ausbildung und Kanzleitraining. |

## Quellen- und Aktualitätsanker

- Aktueller BGB-Gesetzestext: https://www.gesetze-im-internet.de/bgb/
- Interne Struktur: [references/bgb-at-pruefprogramm.md](./references/bgb-at-pruefprogramm.md)
- Rechtsstandsregel: [references/rechtsstand-und-quellen.md](./references/rechtsstand-und-quellen.md)

## Gute Begleiter

- [methodenlehre-buergerliches-recht](../methodenlehre-buergerliches-recht) für Auslegung, Gutachtenstil und Anspruchsdenken.
- [subsumtions-pruefer](../subsumtions-pruefer) für generische Tatbestandsarbeit.
- [schriftform-und-textform-bgb](../schriftform-und-textform-bgb) für tiefe Form-, Textform- und Zugangskonstellationen.
- [bereicherungs-und-anfechtungsrecht-pruefer](../bereicherungs-und-anfechtungsrecht-pruefer) für Rückabwicklung nach unwirksamem Vertrag.
