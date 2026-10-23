"""Falldaten zu sicherungsübertragenen Markenrechten im Insolvenz-Asset-Deal."""

from textwrap import dedent


def _text(value: str) -> str:
    return dedent(value).strip()


def _document(path: str, kind: str, title: str, *paragraphs: str, sections=None, tables=None):
    item = {"path": path, "kind": kind, "title": title}
    if paragraphs:
        item["paragraphs"] = [_text(paragraph) for paragraph in paragraphs]
    if sections is not None:
        item["sections"] = sections
    if tables is not None:
        item["tables"] = tables
    return item


def _section(heading: str, *paragraphs: str, tables=None):
    item = {
        "heading": heading,
        "paragraphs": [_text(paragraph) for paragraph in paragraphs],
    }
    if tables is not None:
        item["tables"] = tables
    return item


def _table(headers, rows):
    return {"headers": headers, "rows": rows}


def _mail(path: str, title: str, sender: str, to: str, cc: str, date: str,
          subject: str, body: str, attachments=()):
    def addresses(value):
        if not value:
            return []
        if isinstance(value, str):
            return [part.strip() for part in value.split(";") if part.strip()]
        return list(value)

    return {
        "path": path,
        "kind": "eml",
        "title": title,
        "from": sender,
        "to": addresses(to),
        "cc": addresses(cc),
        "date": date,
        "subject": subject,
        "body": _text(body),
        "attachments": list(attachments),
    }


def _sheet(name: str, headers, rows, *notes: str):
    return {
        "name": name,
        "headers": headers,
        "rows": rows,
        "notes": [_text(note) for note in notes],
    }


def _xlsx(path: str, title: str, sheets):
    return {"path": path, "kind": "xlsx", "title": title, "sheets": sheets}


def _csv(path: str, title: str, headers, rows):
    return {
        "path": path,
        "kind": "csv",
        "title": title,
        "headers": headers,
        "rows": rows,
    }


CASE = {
    "slug": "markenrechte-sicherungsuebertragung-insolvenz-mannheim",
    "title": "Rheinpuls Audio – sicherungsübertragene Marken im Insolvenzverkauf",
    "short_title": "Rheinpuls Audio – Marken im Asset Deal",
    "plugin": "fachanwalt-urheber-medienrecht",
    "summary": _text("""
        Die Kurpfalz Tonwerke GmbH aus Mannheim hat mehrere Marken zur Sicherung einer
        Betriebsmittelfinanzierung übertragen. Nach Eröffnung des Insolvenzverfahrens
        führte die Insolvenzverwalterin ein Bieterverfahren durch und unterzeichnete
        mit einer Erwerberin aus Schwetzingen einen Asset-Kaufvertrag, der die Marken
        einschließt. Das Closing ist kurzfristig angekündigt. Die heutige
        Sicherheitennehmerin bestreitet, einer Übertragung zugestimmt zu haben; Akte,
        Register, Darlehenskonto und Verwertungsunterlagen enthalten voneinander
        abweichende Angaben zu Rechtsbestand, Sicherungsumfang, Saldo und Reichweite
        früherer Erklärungen.
    """),
    "scenario": _text("""
        Bearbeitungsstand ist Freitag, 23. Oktober 2026, 10:30 Uhr. Die
        Insolvenzverwalterin teilte am Vorabend mit, dass der Asset Purchase Agreement
        bereits am 20. Oktober 2026 beiderseits unterzeichnet worden sei. Das Closing
        soll am Montag, 26. Oktober 2026, um 10:00 Uhr stattfinden. Nach dem Vertrag
        sollen drei registrierte Marken zusammen mit Domains, Gestaltungen,
        Warenbestand und technischen Anlagen auf die Schwetzinger Resonanz GmbH
        übergehen. Die Erwerberin plant die sofortige Fortführung unter den bisherigen
        Zeichen und hat intern bereits die erfolgreiche Übernahme gefeiert.

        Ursprüngliche Darlehensgeberin war die Neckarbrücke Finanzierungs GmbH aus
        Heidelberg. Sie übertrug 2025 die Darlehensforderung und die zugehörigen
        Sicherheiten an die Rebenpfad Sicherheiten GmbH aus Deidesheim. Die
        Sicherungsabrede von 2024 nennt zwei eingetragene deutsche Marken und eine
        damals erst vorbereitete Unionsmarke. Mehrere Fassungen der Anlage 1, eine
        spätere Registereintragung und eine ältere Vertriebslizenz lassen offen, welche
        Rechte in welchem Umfang erfasst und belastet sind. Der im Gläubigerkonto
        ausgewiesene Betrag weicht zudem von den Bankunterlagen der Schuldnerin ab.

        Die Akte endet vor dem angekündigten Closing. Sie enthält Erklärungen aller
        Seiten, einen unterzeichneten Kaufvertrag und operative Vorbereitungen, aber
        keine abschließende rechtliche Einordnung des Sicherungs- oder
        Verwertungsgeschehens.
    """),
    "parties": [
        {
            "name": "Rebenpfad Sicherheiten GmbH",
            "role": "heutige Sicherheitennehmerin und Mandantin",
            "address": "Weinbogen 14, 67146 Deidesheim",
            "email": "geschaeftsleitung@rebenpfad-sicherheiten.example",
        },
        {
            "name": "Kurpfalz Tonwerke GmbH",
            "role": "Insolvenzschuldnerin und frühere operative Markenverwenderin",
            "address": "Hafenbogen 17, 68159 Mannheim",
            "email": "post@kurpfalz-tonwerke.example",
        },
        {
            "name": "Dr. Helena Aydin",
            "role": "Insolvenzverwalterin über das Vermögen der Kurpfalz Tonwerke GmbH",
            "address": "Augustaanlage 81, 68165 Mannheim",
            "email": "insolvenz@aydin-partner.example",
        },
        {
            "name": "Neckarbrücke Finanzierungs GmbH",
            "role": "ursprüngliche Darlehensgeberin und Sicherheitennehmerin",
            "address": "Ufergarten 8, 69120 Heidelberg",
            "email": "kreditservice@neckarbruecke-finanz.example",
        },
        {
            "name": "Schwetzinger Resonanz GmbH",
            "role": "unterzeichnende Asset-Erwerberin",
            "address": "Spargelring 22, 68723 Schwetzingen",
            "email": "transaktion@schwetzinger-resonanz.example",
        },
        {
            "name": "Lina Ebert",
            "role": "Geschäftsführerin der Schwetzinger Resonanz GmbH",
            "address": "Spargelring 22, 68723 Schwetzingen",
            "email": "lina.ebert@schwetzinger-resonanz.example",
        },
        {
            "name": "Janis Heller",
            "role": "ehemaliger Geschäftsführer der Kurpfalz Tonwerke GmbH",
            "address": "Rheinkai 6, 68159 Mannheim",
            "email": "janis.heller@kurpfalz-tonwerke.example",
        },
        {
            "name": "Dr. Mira Yilmaz",
            "role": "Bewertungssachverständige für Marken und sonstiges IP",
            "address": "Königstuhlpassage 11, 69117 Heidelberg",
            "email": "mira.yilmaz@zeichenwert.example",
        },
        {
            "name": "Amtsgericht Mannheim – Insolvenzgericht",
            "role": "Insolvenzgericht, Aktenzeichen 8 IN 233/26",
            "address": "Schlossbezirk 1, 68161 Mannheim",
            "email": "insolvenzgericht-mannheim@justizkontakt.example",
        },
    ],
    "questions": [
        "Ordnen Sie die Beteiligten, die Rechtskette und den zeitlichen Ablauf bis zum angekündigten Closing vollständig.",
        "Bestimmen Sie für jede der drei registrierten Marken gesondert, welche Urkunden und Erklärungen für den behaupteten Sicherungserwerb vorliegen und welche Angaben noch fehlen.",
        "Prüfen Sie, welche Bedeutung Registerstand, Anlage 1, Nachtrag, Forderungsverkauf und Schuldneranzeige jeweils für die Rechtspositionen der Beteiligten haben können.",
        "Prüfen Sie Abschluss, Abrufe, Auszahlungsvoraussetzungen, begrenzte Waiver und die tatsächliche Valutierung jeder Darlehenstranche getrennt anhand der Erklärungen beider Vertragsseiten und der Bankbelege.",
        "Klären Sie den offenen Darlehenssaldo anhand von Vertrag, Zession, Buchungsjournal, neutraler Saldenstaffel und Bankbelegen. Rechnen Sie die Zinsen nach der vereinbarten act/360-Methode nach und weisen Sie streitige Zahlungszuordnungen in getrennten Szenarien aus.",
        "Erfassen Sie sämtliche Erklärungen der Sicherheitennehmerinnen gegenüber Schuldnerin, Verwalterin und Erwerberin und grenzen Sie Zustimmung, Gesprächsbereitschaft, Preisvorstellung und bloße Kenntnis voneinander ab.",
        "Analysieren Sie den unterzeichneten Asset-Kaufvertrag einschließlich Anlagen, Offenlegung, Vollzugsmechanik, Kaufpreisallokation und Rechtsfolgen eines ausbleibenden Mitwirkungsdokuments.",
        "Ordnen Sie die insolvenzrechtlichen und markenrechtlichen Fragen der Verwertungsbefugnis, Absonderung, Verfügung und eines möglichen Erlösbezugs, ohne Parteibehauptungen als feststehend zu übernehmen.",
        "Ermitteln Sie, welche Fristen und tatsächlichen Vollzugsschritte bis und nach dem 26. Oktober 2026 aktenkundig sind und welche nur intern geplant wurden.",
        "Berücksichtigen Sie die Vertriebslizenz und die abweichenden Nutzungsangaben bei der Bewertung dessen, was wirtschaftlich übertragen werden soll.",
        "Erstellen Sie eine beweisorientierte Dokumenten- und Widerspruchsmatrix mit Quellenangabe für jede tragende Tatsache.",
        "Formulieren Sie die erforderliche kurzfristige Reaktion der Sicherheitennehmerin adressatengerecht, ohne ungeklärte Tatsachen als bewiesen darzustellen.",
        "Kennzeichnen Sie, welche Originale, Registerbelege, Zustellnachweise, Kontenabstimmungen und Kommunikationsdaten vor einer abschließenden Beurteilung nachzufordern wären.",
    ],
    "ambiguities": [
        "Die unterschriebene Sicherungsabrede verweist auf eine Anlage 1 mit dem Stand 15. Februar 2024; im Datenraum liegen zwei in Einzelheiten abweichende Fassungen.",
        "Die Unionsmarke RHEINPULS AUDIO war bei Abschluss der Sicherungsabrede nur als Anmeldung vorgesehen und wurde erst später angemeldet und eingetragen.",
        "Für die Wort-/Bildmarke MANNHEIM MODULAR nennt die Registerabschrift einen früheren Prioritätstag als die Sicherheitenliste.",
        "Alle Register weisen weiterhin die Schuldnerin als Inhaberin aus; eine Umschreibung auf eine Sicherheitennehmerin ist nicht dokumentiert.",
        "Der Forderungskauf 2025 nennt Sicherheiten pauschal, während seine Anlage nur zwei Registernummern vollständig wiedergibt.",
        "Eine Zahlung von 15.000 Euro nach Abtretungsanzeige ging an die ursprüngliche Darlehensgeberin und wurde bei den Beteiligten unterschiedlich gebucht.",
        "Die Schuldnerin bezeichnet eine weitere Zahlung von 7.500 Euro als Tilgung; das Gläubigerkonto behandelt sie als Zinszahlung.",
        "Die Bankbelege stimmen bei den beiden Auszahlungen über insgesamt 220.000 Euro überein; offen bleibt, ob sämtliche vertraglichen Auszahlungsvoraussetzungen erfüllt oder nur für die erste Tranche begrenzt zurückgestellt waren.",
        "Der CP-Vermerk gibt die erste Tranche trotz fehlender Registeroriginale, Versicherungsabtretung und Hainblick-Unterlage begrenzt frei. Für die zweite Tranche liegt ein formgerechter Abruf, aber kein gleichartiger aktualisierter CP-Beschluss vor.",
        "Die neutrale Saldenstaffel lässt sich aus Wertstellungen und act/360-Zinsperioden nachrechnen. Sie bestätigt jedoch weder die Gläubigerbuchung noch die Schuldnerzuordnung der Zahlungen über 7.500 und 15.000 Euro.",
        "Eine Vertriebslizenz wird im Datenraum als nicht exklusiv geführt, während eine spätere E-Mail dem Vertriebspartner Gebietsschutz zusagt.",
        "Die Verwalterin bestätigte zunächst, vor einer Übertragung erneut Rücksprache zu halten, unterzeichnete den APA aber ohne weitere Freigabe der Sicherheitennehmerin.",
        "Eine E-Mail der Sicherheitennehmerin nennt eine wirtschaftliche Untergrenze, erklärt im selben Text jedoch ausdrücklich, dass keine Freigabe erteilt werde.",
        "Das Gläubigerausschussprotokoll genehmigt das Paketangebot, gibt aber die Markenrechte als streitbelastet wieder und nennt keine gesonderte Zustimmung der Sicherheitennehmerin.",
        "Bewertungsgutachten, Käuferangebot und Kaufvertrag ordnen den drei Marken unterschiedliche Einzel- und Paketwerte zu.",
        "Der APA verspricht einen Rechtsübergang zum Closing, begrenzt zugleich Eigentumszusagen und legt das Risiko der behaupteten Sicherungsübertragung offen.",
        "Die Closing-Liste führt eine Unterschrift der Sicherheitennehmerin als erwünscht, aber nicht als Vollzugsbedingung.",
        "Die Erwerberin geht intern von uneingeschränkter Nutzung ab Closing aus, obwohl die offengelegte Lizenz und die Sicherungsanzeige in ihrem Datenraum lagen.",
    ],
    "documents": [
        _document(
            "01_Finanzierungsanfrage_Kurpfalz_Tonwerke.docx",
            "docx",
            "Finanzierungsanfrage der Kurpfalz Tonwerke GmbH",
            """
            Die Kurpfalz Tonwerke GmbH entwickelt und vertreibt modulare Audiogeräte,
            Lautsprecherbausätze und Zubehör für kleine Veranstaltungsorte. Das
            Unternehmen beschäftigt am Standort Mannheim 24 Arbeitnehmerinnen und
            Arbeitnehmer. Geschäftsführer Janis Heller beantragt eine revolvierende
            Betriebsmittelfinanzierung von bis zu 240.000 Euro. Der Mittelbedarf wird
            mit Vorfinanzierungen für Gehäuse, Elektronikkomponenten und den Ausbau des
            Direktvertriebs begründet.
            """,
            """
            Als wesentliche immaterielle Werte nennt die Anfrage die deutsche Wortmarke
            KURPFALZKLANG, die deutsche Wort-/Bildmarke MANNHEIM MODULAR und das für
            eine internationale Produktlinie vorbereitete Zeichen RHEINPULS AUDIO. Der
            Umsatz unter KURPFALZKLANG habe 2023 rund 1,46 Millionen Euro betragen. Für
            MANNHEIM MODULAR werden 530.000 Euro ausgewiesen. Die Produktlinie
            RHEINPULS befinde sich vor der Markteinführung; eine Anmeldung beim EUIPO
            sei für das zweite Quartal 2024 vorgesehen.
            """,
            """
            Die Finanzplanung erwartet ab Juni 2024 steigende Zahlungseingänge. Der
            Anhang zur Anfrage führt eine bestehende Warenkreditlinie der
            Kurpfalzbank eG über 90.000 Euro auf. Unter der Überschrift
            „Sicherheiten“ heißt es, die Marken seien unbelastet. Eine handschriftliche
            Randnotiz aus dem Kreditgespräch lautet dagegen: „Hainblick-Vertrag und
            Gebietsschutz noch ansehen.“ Der Kreditaktenindex bezeichnet eine von Janis
            Heller am 6. Februar 2024 unterzeichnete Papieranfrage. Das vorliegende DOCX
            gibt Inhalt und Randnotiz wieder, enthält aber keine Abbildungen der
            Unterschrift oder Handschrift.
            """,
        ),
        _document(
            "02_Darlehensvertrag_15-02-2024.pdf",
            "pdf",
            "Vertragsinhalt des Darlehensvertrags vom 15. Februar 2024",
            sections=[
                _section(
                    "1. Vertragsparteien und Kreditrahmen",
                    """
                    Die Neckarbrücke Finanzierungs GmbH, Ufergarten 8, 69120
                    Heidelberg, gewährt der Kurpfalz Tonwerke GmbH, Hafenbogen 17,
                    68159 Mannheim, einen Betriebsmittelkredit bis zu einem Höchstbetrag
                    von 240.000 Euro. Abrufe bedürfen der Textform und können bis zum
                    30. Juni 2024 erfolgen. Auszahlungen erfolgen auf das Geschäftskonto
                    DE21 6709 0010 8842 6170 03 der Darlehensnehmerin.
                    """,
                ),
                _section(
                    "2. Verzinsung und Rückzahlung",
                    """
                    Der jeweils ausstehende Kapitalbetrag wird mit 7,20 Prozent jährlich
                    verzinst. Zinsen sind quartalsweise nachträglich fällig. Der gesamte
                    offene Kapitalbetrag ist am 31. Dezember 2025 zurückzuzahlen. Vorzeitige
                    Tilgungen sind ohne Vorfälligkeitsentgelt zulässig; die
                    Darlehensnehmerin soll im Verwendungszweck angeben, ob eine Zahlung
                    auf Kapital, Zinsen oder Kosten erfolgt.
                    """,
                    """
                    Bei Zahlungsverzug werden eingehende Beträge zunächst auf Kosten,
                    dann auf fällige Zinsen und zuletzt auf Kapital gebucht, sofern die
                    Darlehensgeberin keine andere Zuordnung bestätigt. Kontoauszüge der
                    Darlehensgeberin gelten als Saldenmitteilung, nicht als
                    Schuldanerkenntnis.
                    """,
                    """
                    Die Zinsen werden taggenau nach act/360 berechnet. Der Valutatag einer
                    Auszahlung oder Tilgung ist der erste Tag des jeweils neuen
                    Kapitalsaldos; der Tag vor der nächsten Saldoänderung ist der letzte Tag
                    der vorangehenden Zinsperiode. Rundungen erfolgen je Periode auf zwei
                    Dezimalstellen. Die Darlehensgeberin stellt zu jedem Quartalsende eine
                    Zinsabrechnung mit Kapitalbasis, Tagen und Rechenweg bereit.
                    """,
                ),
                _section(
                    "3. Sicherheiten",
                    """
                    Vor der ersten Auszahlung bestellt die Darlehensnehmerin die in einer
                    gesonderten Sicherungsabrede bezeichneten Markenrechte. Außerdem tritt
                    sie Ansprüche aus der Produkthaftpflichtversicherung ab. Der
                    Darlehensgeberin ist gestattet, Forderung und Sicherheiten gemeinsam
                    auf ein verbundenes Unternehmen oder einen Finanzinvestor zu
                    übertragen. Die Sicherheitenabrede bestimmt Umfang, Nutzung und
                    Verwertung gesondert.
                    """,
                ),
                _section(
                    "4. Informationspflichten und Kündigung",
                    """
                    Die Darlehensnehmerin informiert unverzüglich über Vollstreckungen,
                    Insolvenzanträge, die Aufgabe wesentlicher Produktlinien und
                    Verfügungen über geschützte Kennzeichen. Ein wichtiger Grund zur
                    Kündigung liegt insbesondere vor, wenn fällige Beträge trotz einer
                    Nachfrist von zehn Bankarbeitstagen nicht bezahlt werden oder eine
                    wesentliche Sicherheit gefährdet wird.
                    """,
                ),
                _section(
                    "5. Schlussbestimmungen und Ausfertigungsvermerk",
                    """
                    Nebenabreden bestehen nach dem Vertragstext nicht. Änderungen und
                    Ergänzungen sollen in Textform dokumentiert werden. Heidelberg ist
                    als Gerichtsstand vereinbart, soweit gesetzlich zulässig. Der
                    Kreditaktenindex vermerkt je eine von Sonja Wieland und Armin Chandra
                    für die Darlehensgeberin sowie von Janis Heller für die
                    Darlehensnehmerin am 15. Februar 2024 unterzeichnete Papierausfertigung.
                    Das vorliegende PDF ist eine inhaltliche Vertragsabschrift und enthält
                    weder die Papieroriginale noch Abbildungen der Unterschriften.
                    """,
                ),
            ],
            tables=[
                _table(
                    ["Vertragsparameter", "Vereinbarung"],
                    [
                        ["Kreditrahmen", "höchstens 240.000 EUR"],
                        ["Abruffrist", "Textformabrufe bis 30.06.2024"],
                        ["Auszahlungskonto", "DE21 6709 0010 8842 6170 03"],
                        ["Zinsmethode", "7,20 % p.a.; act/360; quartalsweise nachträglich"],
                        ["Endfälligkeit", "31.12.2025"],
                    ],
                )
            ],
        ),
        _mail(
            "02A_Abruf_Tranche_1_16-02-2024.eml",
            "Textformabruf der ersten Darlehenstranche",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "Sonja Wieland <sonja.wieland@neckarbruecke-finanz.example>",
            "Leila Werner <leila.werner@kurpfalz-tonwerke.example>",
            "2024-02-16T08:22:00+01:00",
            "KT-2024-021 – Abruf 1 über 180.000 EUR zum 19.02.2024",
            """
            Guten Morgen Frau Wieland,

            hiermit rufen wir unter dem Darlehensvertrag KT-2024-021 vom
            15. Februar 2024 einen Betrag von 180.000 Euro ab. Bitte schreiben Sie die
            Valuta am 19. Februar 2024 unserem im Vertrag bezeichneten Geschäftskonto
            DE21 6709 0010 8842 6170 03 gut. Der Betrag wird für bereits bestellte
            Elektronikkomponenten, Gehäuse und laufende Lohnzahlungen verwendet.

            Das Auszahlungskonto ist unverändert. Darlehensvertrag,
            Sicherungsvereinbarung, Anlage 1 und Gesellschafterbeschluss wurden Ihrer
            Kreditabteilung übergeben. Uns ist bekannt, dass Ihre interne
            Auszahlungskontrolle noch offene Registerunterlagen und den
            Hainblick-Vertrag ausweist. Dieser Abruf enthält keine Bitte, auf die
            vertraglich geschuldeten Unterlagen endgültig zu verzichten.

            Bitte bestätigen Sie Freigabe und Ausführung unter Angabe der
            Zahlungsreferenz.

            Freundliche Grüße
            Janis Heller
            """,
            attachments=(
                "02_Darlehensvertrag_15-02-2024.pdf",
                "03_Gesellschafterbeschluss_Sicherheiten.docx",
                "04_Sicherungsuebertragung_Marken_15-02-2024.pdf",
                "05_Anlage_1_Markenbestand.xlsx",
            ),
        ),
        _xlsx(
            "02B_CP_Check_und_Waiver_Tranche_1.xlsx",
            "Auszahlungsvoraussetzungen, Freigabe und begrenzter Waiver für Tranche 1",
            [
                _sheet(
                    "CP_Pruefung",
                    ["Nr.", "Auszahlungsvoraussetzung", "Aktenbeleg", "Stand 19.02.2024 08:30", "Entscheidung", "Nachfrist"],
                    [
                        [1, "Darlehensvertrag in der Kreditakte als unterzeichnet protokolliert", "02_Darlehensvertrag_15-02-2024.pdf; Originalregister K-17", "erfüllt; vorliegendes PDF nur Abschrift", "Freigabe", "-"],
                        [2, "Gesellschafterzustimmung und Vertretungsprüfung", "03_Gesellschafterbeschluss_Sicherheiten.docx; HR-Prüfvermerk", "erfüllt; Papieroriginal laut Aktenindex eingesehen", "Freigabe", "-"],
                        [3, "Sicherungsabrede und Anlage 1", "04_Sicherungsuebertragung_Marken_15-02-2024.pdf; 05_Anlage_1_Markenbestand.xlsx", "zwei DE-Marken bestimmt; RHEINPULS als künftige Anmeldung bezeichnet", "Freigabe mit Dokumentennachlauf", "Anmeldenummer binnen 2 Bankarbeitstagen nach Anmeldung"],
                        [4, "Textformabruf und Auszahlungskonto", "02A_Abruf_Tranche_1_16-02-2024.eml", "erfüllt; 180.000 EUR; Valuta 19.02.2024", "Freigabe", "-"],
                        [5, "Aktuelle amtliche Registerauszüge der zwei DE-Marken", "Unterlagenliste CP-4", "offen; nur interne Ausdrucke", "begrenzter Waiver für Tranche 1", "29.02.2024"],
                        [6, "Abtretung Ansprüche Produkthaftpflichtversicherung", "Darlehensvertrag Ziffer 3", "offen; Abtretungsformular nicht zurück", "begrenzter Waiver für Tranche 1", "29.02.2024"],
                        [7, "Offenlegung Hainblick-Vertrag und Gebietsschutz", "Finanzierungsanfrage; Gesprächsnotiz", "offen; Vertrag nicht in Kreditakte", "begrenzter Waiver für Tranche 1", "15.03.2024"],
                        [8, "Keine Änderung von Kontoinhaberin oder IBAN", "Abrufmail; Stammdatenabgleich", "erfüllt", "Freigabe", "-"],
                    ],
                    "Status bedeutet nur, was die Kreditkontrolle am Entscheidungszeitpunkt geprüft hat. Ein Waiver ersetzt weder eine fehlende Urkunde noch eine spätere Prüfung der Wirksamkeit der Sicherheit.",
                ),
                _sheet(
                    "Freigabeentscheidung",
                    ["Feld", "Festlegung"],
                    [
                        ["Freigabe-ID", "CP-KT-2024-021-T1"],
                        ["Entscheidungszeit", "19.02.2024 08:37 CET"],
                        ["Freigegebener Höchstbetrag", "180.000 EUR"],
                        ["Valuta", "19.02.2024"],
                        ["Entscheidende Personen", "Sonja Wieland, Kredit; Armin Chandra, Marktfolge"],
                        ["Umfang des Waivers", "nur zeitliche Nachreichung der Positionen 5 bis 7; nur Tranche 1"],
                        ["Nicht erlassen", "Unterlagenpflichten, Sicherheitenbestellung, Offenlegungspflichten, Rechte bei Unrichtigkeit"],
                        ["Keine Folgefreigabe", "Tranche 2 erfordert neuen Textformabruf und erneute Kreditentscheidung"],
                        ["Ergebnis", "Tranche 1 zur Ausführung freigegeben"],
                    ],
                    "Die Freigabe ist ein interner Marktfolgeentscheid. Sie bestätigt keine Registerumschreibung und keinen Verzicht auf die vereinbarte Versicherungsabtretung.",
                ),
                _sheet(
                    "Offene_Punkte",
                    ["Punkt", "Verantwortlich", "Frist", "Stand bei Freigabe", "Folge in der Akte"],
                    [
                        ["Amtliche DE-Registerauszüge", "Kurpfalz Tonwerke", "29.02.2024", "offen", "spätere Registerabschriften vorhanden; Eingang 2024 nicht belegt"],
                        ["Versicherungsabtretung", "Kurpfalz Tonwerke", "29.02.2024", "offen", "kein Abtretungsformular in der Arbeitsakte"],
                        ["Hainblick-Vertrag", "Kurpfalz Tonwerke", "15.03.2024", "offen", "erst später in Insolvenzakte greifbar"],
                        ["EUIPO-Anmeldenummer RHEINPULS", "Kurpfalz Tonwerke", "2 Bankarbeitstage nach Anmeldung", "Anmeldung noch nicht erfolgt", "Anmeldung 09.04.2024; Übermittlung an Kreditakte nicht belegt"],
                    ],
                    "Nicht belegte Erledigung ist nicht als erfüllt zu behandeln. Die Liste hält die begrenzte Reichweite der Freigabe ausdrücklich fest.",
                ),
            ],
        ),
        _document(
            "03_Gesellschafterbeschluss_Sicherheiten.docx",
            "docx",
            "Gesellschafterbeschluss zur Finanzierung und Markenbesicherung",
            """
            Die alleinige Gesellschafterin Marlene Vogt hält am 14. Februar 2024 in
            Mannheim eine außerordentliche Gesellschafterversammlung ab. Sie stimmt dem
            Darlehensvertrag mit einem Höchstbetrag von 240.000 Euro und der Bestellung
            von Sicherheiten an den wesentlichen Marken der Gesellschaft zu. Der
            Geschäftsführer wird ermächtigt, die hierfür erforderlichen Erklärungen
            abzugeben und Registerunterlagen beizubringen.
            """,
            """
            Im Beschlusstext werden KURPFALZKLANG und MANNHEIM MODULAR mit ihren
            deutschen Registernummern genannt. RHEINPULS AUDIO erscheint nur in einem
            Klammerzusatz: „nach Anmeldung, sofern Finanzierung noch valutiert“. Eine
            Anlage ist im Gesellschaftsordner nicht abgeheftet. Der Gesellschaftsordner
            verzeichnet ein von Marlene Vogt und Janis Heller unterzeichnetes
            Papierprotokoll mit handschriftlich ergänzter Uhrzeit 18:40 Uhr. Das
            vorliegende DOCX ist dessen inhaltliche Abschrift und enthält keine
            Abbildungen von Unterschriften oder Handschrift.
            """,
            """
            Der Beschluss enthält keine Wertangabe und keine Aussage zu einer bereits
            bestehenden Vertriebslizenz. Im letzten Absatz wird der Geschäftsführer
            angewiesen, die laufende Nutzung der Zeichen im normalen Geschäftsbetrieb
            zu sichern und ohne erneuten Gesellschafterbeschluss keine endgültige
            Veräußerung vorzunehmen.
            """,
        ),
        _document(
            "04_Sicherungsuebertragung_Marken_15-02-2024.pdf",
            "pdf",
            "Vertragsinhalt der Vereinbarung über die Sicherungsübertragung von Markenrechten",
            sections=[
                _section(
                    "1. Präambel",
                    """
                    Die Vereinbarung wird zwischen der Neckarbrücke Finanzierungs GmbH
                    als Sicherheitennehmerin und der Kurpfalz Tonwerke GmbH als
                    Sicherungsgeberin geschlossen. Sie nimmt auf den Darlehensvertrag
                    vom selben Tag Bezug. Die Parteien bezeichnen die Marken als einen
                    wesentlichen Bestandteil des Unternehmenswerts und wollen der
                    Sicherheitennehmerin eine Sicherheit für sämtliche Ansprüche aus der
                    Finanzierung verschaffen.
                    """,
                ),
                _section(
                    "2. Gesicherte Ansprüche und Sicherungszweck",
                    """
                    Gesichert werden alle gegenwärtigen und künftigen Ansprüche aus dem
                    Darlehensvertrag vom 15. Februar 2024 bis zu einem Höchstbetrag von
                    300.000 Euro einschließlich Zinsen, Kosten und Aufwendungen der
                    Sicherheitenverwaltung. Rückgezahlte Beträge leben bei einem neuen
                    Abruf nur wieder auf, soweit der Darlehensvertrag einen solchen Abruf
                    zulässt. Dieser Forderungskreis ist der abschließende
                    Sicherungszweck; andere gegenwärtige oder künftige Forderungen der
                    Sicherheitennehmerin werden nicht einbezogen.
                    """,
                ),
                _section(
                    "3. Übertragene Rechte",
                    """
                    Die Sicherungsgeberin überträgt die in Anlage 1 einzeln bezeichneten
                    Marken mit allen zugehörigen vermögenswerten Rechten auf die
                    Sicherheitennehmerin. Soweit eine in Anlage 1 bezeichnete Marke erst
                    angemeldet oder eingetragen wird, soll die Übertragung mit Entstehung
                    beziehungsweise Erwerb des Rechts wirksam werden. Nicht registrierte
                    Unternehmenskennzeichen, Domains, Designs und Urheberrechte werden
                    nur erfasst, wenn sie in Anlage 1 ausdrücklich aufgeführt sind.
                    """,
                    """
                    Die Sicherungsgeberin erklärt, zur Verfügung befugt zu sein. Sie legt
                    bestehende Lizenzen offen und wird ohne schriftliche Zustimmung keine
                    ausschließlichen Rechte einräumen, auf Marken verzichten oder den
                    Schutzumfang einschränken. Eine Umschreibung im Register kann von der
                    Sicherheitennehmerin verlangt werden, ist aber nach dem Vertragstext
                    keine Voraussetzung der Übertragung.
                    """,
                ),
                _section(
                    "4. Rücklizenz und laufende Verwaltung",
                    """
                    Die Sicherheitennehmerin räumt der Sicherungsgeberin eine unentgeltliche,
                    nicht ausschließliche und bis zur Verwertungsreife widerrufliche
                    Lizenz für den gewöhnlichen Geschäftsbetrieb ein. Die
                    Sicherungsgeberin trägt Verlängerungsgebühren, überwacht Fristen und
                    führt Angriffe auf den Markenbestand nach Abstimmung. Einnahmen aus
                    bereits offengelegten einfachen Lizenzen verbleiben bis zum Widerruf
                    bei ihr.
                    """,
                ),
                _section(
                    "5. Verwertungsreife und Verfahren",
                    """
                    Verwertungsreife tritt ein, wenn der Darlehensvertrag wirksam
                    gekündigt oder der Rückzahlungsbetrag bei Endfälligkeit nicht
                    beglichen ist. Vor einer Verwertung soll die Sicherheitennehmerin eine
                    Nachfrist von zehn Bankarbeitstagen setzen und die beabsichtigte Art
                    der Verwertung ankündigen. Ein freihändiger Verkauf ist zulässig,
                    sofern ein nachvollziehbares Marktverfahren oder eine unabhängige
                    Bewertung zugrunde liegt.
                    """,
                ),
                _section(
                    "6. Freigabe und Übertragung",
                    """
                    Nach endgültiger Befriedigung gibt die Sicherheitennehmerin die
                    Sicherheiten frei. Sie darf die gesicherten Ansprüche nur zusammen
                    mit den akzessorisch oder treuhänderisch gebundenen Rechten
                    übertragen. Der Erwerber tritt in die Pflichten aus dieser
                    Vereinbarung ein. Die Sicherungsgeberin soll über einen Wechsel der
                    Sicherheitennehmerin unterrichtet werden.
                    """,
                ),
                _section(
                    "7. Ausfertigungs- und Anlagenvermerk",
                    """
                    Der Kreditaktenindex bezeichnet eine am 15. Februar 2024 von den
                    Parteien unterzeichnete Papierausfertigung und vermerkt bei Janis
                    Heller den Empfang von Anlage 1. Das vorliegende PDF gibt den
                    Vertragsinhalt wieder, enthält aber weder die Papierausfertigung noch
                    Abbildungen der Unterschriften. Anlage 1 liegt in der Arbeitsakte als
                    gesonderte XLSX mit einem Schuldnerkürzel und ohne Unterschriftsblock
                    der Darlehensgeberin vor.
                    """,
                ),
            ],
        ),
        _xlsx(
            "05_Anlage_1_Markenbestand.xlsx",
            "Anlage 1 und abweichende Fassungen des Markenbestands",
            [
                _sheet(
                    "Anlage_unterschrieben",
                    ["Pos.", "Zeichen", "Art", "Registernummer", "Status 15.02.2024", "Bemerkung"],
                    [
                        [1, "KURPFALZKLANG", "DE-Wortmarke", "30 2020 059 412", "eingetragen", "Klassen 9, 15, 35"],
                        [2, "MANNHEIM MODULAR", "DE-Wort-/Bildmarke", "30 2021 227 861", "eingetragen", "Klassen 9, 15, 41"],
                        [3, "RHEINPULS AUDIO", "geplante Unionswortmarke", "Nummer folgt", "Anmeldung Q2/2024", "Klassen 9, 15, 35"],
                    ],
                    "Diese Fassung trägt oben rechts das Kürzel JH und den Datumsstempel 15.02.2024. Eine Unterschrift der Darlehensgeberin fehlt auf dem Tabellenblatt.",
                ),
                _sheet(
                    "Datenraum_Fassung",
                    ["Pos.", "Zeichen", "Art", "Registernummer", "Priorität/Anmeldung", "Lizenz"],
                    [
                        [1, "KURPFALZKLANG", "DE-Wortmarke", "30 2020 059 412", "18.09.2020", "keine"],
                        [2, "MANNHEIM MODULAR", "DE-Wort-/Bildmarke", "30 2021 227 816", "04.06.2021", "Hainblick Audiohandel"],
                        [3, "RHEINPULS AUDIO", "Unionswortmarke", "018993742", "09.04.2024", "keine"],
                    ],
                    "Die Registernummer in Zeile 2 endet hier auf 816. Registerauszug und unterschriebene Fassung nennen 861. Das Blatt wurde laut Dateieigenschaften am 26.08.2026 geändert.",
                ),
                _sheet(
                    "Fristen",
                    ["Zeichen", "Schutzbeginn", "Schutzende laut interner Liste", "Gebührenstatus", "Quelle"],
                    [
                        ["KURPFALZKLANG", "18.09.2020", "18.09.2030", "bezahlt", "Markenverwaltung 05/2026"],
                        ["MANNHEIM MODULAR", "04.06.2021", "04.06.2031", "bezahlt", "Markenverwaltung 05/2026"],
                        ["RHEINPULS AUDIO", "09.04.2024", "09.04.2034", "bezahlt", "EUIPO-Kontoauszug fehlt"],
                    ],
                    "Die Tabelle gibt interne Fristnotizen wieder und enthält keine amtlichen Gebührenbelege.",
                ),
            ],
        ),
        _mail(
            "06_Auszahlung_und_Unterlagen.eml",
            "Auszahlungsbestätigung der ursprünglichen Darlehensgeberin",
            "Sonja Wieland <sonja.wieland@neckarbruecke-finanz.example>",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "kreditakte@neckarbruecke-finanz.example",
            "2024-02-19T09:14:00+01:00",
            "Auszahlung 180.000 EUR / Markenunterlagen",
            """
            Guten Morgen Herr Heller,

            Ihren Textformabruf vom 16. Februar haben wir unter
            KT-2024-021-T1 erfasst. Die erste Tranche über 180.000 Euro ist nach der
            begrenzten Marktfolgefreigabe CP-KT-2024-021-T1 soeben mit Valuta heute
            angewiesen worden. Uns liegen die Vertragsabschriften, die
            Sicherungsvereinbarung und Ihre Markenliste mit dem Kürzel JH vor. Die
            Originale der beiden deutschen Registerauszüge sollen nachgereicht werden.
            Für RHEINPULS AUDIO reicht uns für diese Tranche zunächst die im Antrag
            bezeichnete Nachanmeldungsklausel; bitte senden Sie die Anmeldenummer
            unmittelbar nach Einreichung.

            Im Gespräch hatten Sie erwähnt, dass Hainblick in Nordbaden bevorzugt
            beliefert wird. In unserer Akte befindet sich dazu noch kein Vertrag. Ich
            nehme den Punkt in die Unterlagenliste auf. Die Auszahlung erfolgt dadurch
            heute nicht verzögert.

            Freundliche Grüße
            Sonja Wieland
            """,
            attachments=(
                "02_Darlehensvertrag_15-02-2024.pdf",
                "04_Sicherungsuebertragung_Marken_15-02-2024.pdf",
                "05_Anlage_1_Markenbestand.xlsx",
            ),
        ),
        _mail(
            "06A_Abruf_Tranche_2_03-05-2024.eml",
            "Textformabruf der zweiten Darlehenstranche",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "Sonja Wieland <sonja.wieland@neckarbruecke-finanz.example>",
            "Leila Werner <leila.werner@kurpfalz-tonwerke.example>; kreditakte@neckarbruecke-finanz.example",
            "2024-05-03T10:11:00+02:00",
            "KT-2024-021 – Abruf 2 über 40.000 EUR zum 07.05.2024",
            """
            Sehr geehrte Frau Wieland,

            hiermit rufen wir weitere 40.000 Euro aus dem Kreditrahmen KT-2024-021 ab.
            Gewünschte Valuta ist Dienstag, der 7. Mai 2024. Auszahlungskonto bleibt
            DE21 6709 0010 8842 6170 03. Wir verwenden die Mittel für die
            Vorfinanzierung der ersten Serie RP-01, insbesondere Audiointerfaces und
            Gehäuseteile.

            RHEINPULS AUDIO wurde am 9. April 2024 beim EUIPO angemeldet. Die
            Anmeldenummer ist in unserer Markenverwaltung 018993742; den amtlichen
            Anmeldebeleg hat die Markenkanzlei noch nicht an unsere Buchhaltung
            übersandt. Die offenen Punkte aus Ihrer Freigabe vom 19. Februar bleiben
            davon unberührt. Bitte teilen Sie uns mit, ob Sie für diesen Abruf weitere
            Unterlagen benötigen.

            Freundliche Grüße
            Janis Heller
            """,
            attachments=("02_Darlehensvertrag_15-02-2024.pdf",),
        ),
        _document(
            "06B_SEPA_Ausfuehrungsbelege_Tranchen.pdf",
            "pdf",
            "Bankseitiges Auszahlungsavis und SEPA-Ausführungsnachweise",
            sections=[
                _section(
                    "1. Aussteller und Konten",
                    """
                    Rhein-Neckar Clearing AG, elektronischer Firmenkundenauszug für die
                    Neckarbrücke Finanzierungs GmbH. Belastungskonto ist
                    DE63 6725 0010 0091 4432 18. Empfängerkonto beider Zahlungen ist das
                    im Darlehensvertrag bezeichnete Geschäftskonto der Kurpfalz Tonwerke
                    GmbH, DE21 6709 0010 8842 6170 03. Der Auszug wurde am 8. Mai 2024
                    unter der Export-ID RNC-KT-2024-021 erzeugt.
                    """,
                ),
                _section(
                    "2. Ausgeführte Überweisungen",
                    """
                    Beide Aufträge tragen den Status „endgültig gebucht“. Rückruf,
                    Rücklastschrift oder Empfängerablehnung sind im Statusprotokoll bis
                    zum Exportzeitpunkt nicht vermerkt. Die End-to-End-Referenzen stimmen
                    mit dem Kreditkonto und den Gutschriften auf dem Schuldnerkonto
                    überein.
                    """,
                    tables=[
                        _table(
                            ["Auftrag", "Einreichung", "Ausführung/Valuta", "Betrag EUR", "End-to-End-Referenz", "Bankreferenz", "Status"],
                            [
                                ["Tranche 1", "19.02.2024 08:46", "19.02.2024", 180000, "KT-2024-021-T1", "RNC240219084612771", "endgültig gebucht"],
                                ["Tranche 2", "06.05.2024 15:18", "07.05.2024", 40000, "KT-2024-021-T2", "RNC240506151844203", "endgültig gebucht"],
                            ],
                        )
                    ],
                ),
                _section(
                    "3. Abstimmungsvermerk",
                    """
                    Summe der beiden Belastungen: 220.000 Euro. Summe der beiden
                    Gutschriften im kreditrelevanten Bankauszug der Darlehensnehmerin:
                    220.000 Euro. Differenz: 0 Euro. Der Nachweis belegt die Ausführung,
                    nicht die Erfüllung sämtlicher Auszahlungsvoraussetzungen oder die
                    rechtliche Wirksamkeit einer Sicherheit.
                    """,
                ),
            ],
        ),
        _csv(
            "07_Darlehenskonto_Neckarbruecke.csv",
            "Buchungsjournal der ursprünglichen Darlehensgeberin",
            ["Buchungstag", "Wertstellung", "Buchungstext", "Soll_EUR", "Haben_EUR", "Kapitalsaldo_EUR", "Hinweis"],
            [
                ["19.02.2024", "19.02.2024", "Auszahlung Tranche 1", "180000.00", "0.00", "180000.00", "Abruf 02A; E2E KT-2024-021-T1"],
                ["31.03.2024", "31.03.2024", "Vertragszins Q1/2024", "1512.00", "0.00", "180000.00", "180.000 x 7,20 % x 42/360"],
                ["02.04.2024", "02.04.2024", "Zahlung Zinsen Q1", "0.00", "1512.00", "180000.00", "Zinskonto ausgeglichen"],
                ["07.05.2024", "07.05.2024", "Auszahlung Tranche 2", "40000.00", "0.00", "220000.00", "Abruf 06A; E2E KT-2024-021-T2"],
                ["30.06.2024", "30.06.2024", "Vertragszins Q2/2024", "3716.00", "0.00", "220000.00", "180.000 x 7,20 % x 36/360 + 220.000 x 7,20 % x 55/360"],
                ["02.07.2024", "02.07.2024", "Zahlung Zinsen Q2", "0.00", "3716.00", "220000.00", "Zinskonto ausgeglichen"],
                ["30.08.2024", "30.08.2024", "Tilgung", "0.00", "20000.00", "200000.00", "Verwendungszweck: Tilgung"],
                ["30.09.2024", "30.09.2024", "Vertragszins Q3/2024", "3920.00", "0.00", "200000.00", "220.000 x 7,20 % x 60/360 + 200.000 x 7,20 % x 32/360"],
                ["02.10.2024", "02.10.2024", "Zahlung Zinsen Q3", "0.00", "3920.00", "200000.00", "Zinskonto ausgeglichen"],
                ["31.12.2024", "31.12.2024", "Vertragszins Q4/2024", "3680.00", "0.00", "200000.00", "200.000 x 7,20 % x 92/360"],
                ["03.01.2025", "03.01.2025", "Zahlung Zinsen Q4", "0.00", "3680.00", "200000.00", "Zinskonto ausgeglichen"],
                ["31.03.2025", "31.03.2025", "Vertragszins Q1/2025", "3600.00", "0.00", "200000.00", "200.000 x 7,20 % x 90/360"],
                ["31.03.2025", "31.03.2025", "Zahlung 7.500 EUR", "0.00", "7500.00", "200000.00", "Zahlungszweck Kapital; Gläubigerbuchung vollständig Zinsen/Kosten; Zuordnung streitig"],
                ["31.07.2025", "31.07.2025", "Saldo bei Forderungsverkauf", "0.00", "0.00", "200000.00", "Gläubigerbehauptung: Zinsen/Kosten 6.841,64 EUR; neutrale Kontrolle in 07A"],
            ],
        ),
        _xlsx(
            "07A_Kreditkonto_und_Saldenstaffel.xlsx",
            "Neutrale Kreditkonto- und Saldenstaffel mit Zuordnungsszenarien",
            [
                _sheet(
                    "Objektive_Geldfluesse",
                    ["Valuta", "Vorgang", "Auszahlung an Schuldnerin EUR", "Abfluss Schuldnerkonto EUR", "Zufluss Gläubigerkonto EUR", "Empfänger", "Primärbeleg", "Belegstatus"],
                    [
                        ["19.02.2024", "Tranche 1", 180000, 0, 0, "Kurpfalz Tonwerke", "06B SEPA; 08 Schuldnerkonto", "beidseitig belegt"],
                        ["02.04.2024", "Zinszahlung Q1/2024", 0, 1512, 1512, "Neckarbrücke", "07 Kreditjournal; 08 Schuldnerkonto", "beidseitig belegt"],
                        ["07.05.2024", "Tranche 2", 40000, 0, 0, "Kurpfalz Tonwerke", "06B SEPA; 08 Schuldnerkonto", "beidseitig belegt"],
                        ["02.07.2024", "Zinszahlung Q2/2024", 0, 3716, 3716, "Neckarbrücke", "07 Kreditjournal; 08 Schuldnerkonto", "beidseitig belegt"],
                        ["30.08.2024", "Tilgung", 0, 20000, 20000, "Neckarbrücke", "07 Kreditjournal; 08 Schuldnerkonto", "Zuordnung Kapital unstreitig"],
                        ["02.10.2024", "Zinszahlung Q3/2024", 0, 3920, 3920, "Neckarbrücke", "07 Kreditjournal; 08 Schuldnerkonto", "beidseitig belegt"],
                        ["03.01.2025", "Zinszahlung Q4/2024", 0, 3680, 3680, "Neckarbrücke", "07 Kreditjournal; 08 Schuldnerkonto", "beidseitig belegt"],
                        ["31.03.2025", "Zahlung mit Zweck bitte Kapital", 0, 7500, 7500, "Neckarbrücke", "07 Kreditjournal; 08 Schuldnerkonto", "Geldfluss belegt; Zuordnung streitig"],
                        ["30.09.2025", "Zahlung nach Abtretungsanzeige", 0, 15000, 15000, "Neckarbrücke", "08 Schuldnerkonto; Empfangsangabe", "Belastung und Empfang belegt"],
                        ["10.10.2025", "Weiterleitung gleicher Betrag", 0, 0, 15000, "Rebenpfad", "08 Empfängerkonto; 15 Gläubigerkonto", "Eingang belegt; Schuldnerbezug bestritten"],
                    ],
                    "Auszahlungen sind keine negativen Zahlungen. Die Weiterleitung vom 10.10.2025 ist kein zweiter Geldabfluss der Schuldnerin. Sie steht deshalb nur in der Spalte Zufluss Gläubigerkonto.",
                ),
                _sheet(
                    "Zinsstaffel_bis_3107",
                    ["Periode von", "bis ausschließlich", "Tage act/360", "Kapital EUR", "Rechenweg", "Vertragszins EUR", "Fälligkeit", "Zahlung/Status"],
                    [
                        ["19.02.2024", "01.04.2024", 42, 180000, "180.000 x 7,20 % x 42/360", 1512, "31.03.2024", "1.512 am 02.04.2024"],
                        ["01.04.2024", "07.05.2024", 36, 180000, "180.000 x 7,20 % x 36/360", 1296, "30.06.2024", "Teil Q2"],
                        ["07.05.2024", "01.07.2024", 55, 220000, "220.000 x 7,20 % x 55/360", 2420, "30.06.2024", "Q2 gesamt 3.716; Zahlung 02.07."],
                        ["01.07.2024", "30.08.2024", 60, 220000, "220.000 x 7,20 % x 60/360", 2640, "30.09.2024", "Teil Q3"],
                        ["30.08.2024", "01.10.2024", 32, 200000, "200.000 x 7,20 % x 32/360", 1280, "30.09.2024", "Q3 gesamt 3.920; Zahlung 02.10."],
                        ["01.10.2024", "01.01.2025", 92, 200000, "200.000 x 7,20 % x 92/360", 3680, "31.12.2024", "Zahlung 03.01.2025"],
                        ["01.01.2025", "01.04.2025", 90, 200000, "200.000 x 7,20 % x 90/360", 3600, "31.03.2025", "Zahlung 7.500; Zuordnung streitig"],
                    ],
                    "Valutatag ist erster Tag des neuen Saldos; bis-Datum ist nicht mitgezählt. Jede Zeile lässt sich aus Vertrag, Kalendertagen und Kapitalstand nachrechnen.",
                ),
                _sheet(
                    "Szenarien_31_07_2025",
                    ["Szenario", "Behandlung Zahlung 7.500", "Kapital 31.07. EUR", "offener Zins 31.07. EUR", "Gesamt 31.07. EUR", "Kontrollhinweis"],
                    [
                        ["A Schuldnerweisung", "7.500 vollständig Kapital; Q1-Zins bleibt offen", 192500, 8258.50, 200758.50, "3.600 Q1 + 3.503,50 Q2 (91 Tage) + 1.155 Juli"],
                        ["B Vertragskaskade", "3.600 Q1-Zins; Rest 3.900 Kapital", 196100, 4745.62, 200845.62, "3.569,02 Q2 (91 Tage) + 1.176,60 Juli"],
                        ["C Gläubigerkonto", "7.500 vollständig Zinsen/Kosten; Kapital unverändert", 200000, 6841.64, 206841.64, "act/360 ab 01.04. ergibt 4.840; Differenz 2.001,64 unbelegt"],
                    ],
                    "Die Tabelle entscheidet die rechtliche Zuordnung nicht. Sie trennt nachrechenbare Rechenfolgen von der im Forderungskauf übernommenen Gläubigerbuchung.",
                ),
                _sheet(
                    "Zahlung_15_000",
                    ["Datum", "Kontoereignis", "Betrag EUR", "Referenz", "Objektiver Befund", "offene Rechts-/Buchungsfrage"],
                    [
                        ["30.09.2025", "Belastung Schuldnerkonto an Neckarbrücke", 15000, "Darlehen Tilgung / Abstimmung SW", "Abfluss belegt", "Wirkung trotz Abtretungsanzeige"],
                        ["10.10.2025", "Gutschrift Rebenpfad von Neckarbrücke", 15000, "Kaufpreisabrechnung Portfolio KT", "Zufluss belegt", "Identität mit Schuldnerzahlung und Wertstellung"],
                        ["10.10.2025", "Buchung Rebenpfad auf Portfoliokonto", 15000, "nicht Schuldnerkonto", "keine Forderungsminderung gebucht", "Weiterleitungsklausel aus Forderungskauf"],
                    ],
                    "Betragsgleichheit, zeitlicher Zusammenhang und Portfolio-Kürzel sind Indizien, ersetzen aber das fehlende Weiterleitungsavis der Neckarbrücke nicht.",
                ),
                _sheet(
                    "Szenarien_04_03_2026",
                    ["Szenario", "Kapital EUR", "Zinsen bis 01.01.2026 EUR", "Zinsen 01.01.–04.03. EUR", "Kosten EUR", "Gesamt EUR", "Rechenkontrolle"],
                    [
                        ["A Schuldnerweisung", 177500, 13908.50, 2201, 450, 194059.50, "177.500 x 7,20 % x 62/360 = 2.201"],
                        ["B Vertragskaskade", 188238.04, 3501.23, 2334.15, 450, 194523.42, "188.238,04 x 7,20 % x 62/360 = 2.334,15"],
                        ["C Gläubigerkonto", 200000, 12810, 2480, 450, 215740, "200.000 x 7,20 % x 62/360 = 2.480"],
                    ],
                    "Szenario B wendet die Zahlung vom 30.09.2025 zunächst auf bis dahin errechnete Zinsen von 7.138,04 EUR und mit 7.861,96 EUR auf Kapital an. Alle Perioden werden einzeln auf Cent gerundet.",
                ),
                _sheet(
                    "Kontrollsummen",
                    ["Kontrolle", "Soll EUR", "Ist EUR", "Differenz EUR", "Ergebnis"],
                    [
                        ["Darlehensauszahlungen laut Abrufen/SEPA", 220000, 220000, 0, "stimmt"],
                        ["Gutschriften Schuldnerkonto", 220000, 220000, 0, "stimmt"],
                        ["Zinsen Q1 bis Q4/2024 nach act/360", 12828, 12828, 0, "stimmt mit Zahlungen"],
                        ["Unstreitige Kapitaltilgung 30.08.2024", 20000, 20000, 0, "stimmt"],
                        ["Zahlung 31.03.2025 Geldfluss", 7500, 7500, 0, "nur Zuordnung offen"],
                        ["Zahlung 30.09./Weiterleitung 10.10.2025", 15000, 15000, 0, "Forderungsgutschrift offen"],
                        ["Gläubigerzins 31.07. minus act/360 bei Gläubigerzuordnung", 6841.64, 4840, 2001.64, "nicht abgestimmt"],
                    ],
                    "Kontrollsummen belegen Geldflüsse und Rechenwege, nicht die rechtliche Entscheidung zwischen den Zuordnungsszenarien.",
                ),
            ],
        ),
        _document(
            "08_Kontoauszuege_Schuldnerin.pdf",
            "pdf",
            "Kontotypischer Archivexport des Geschäftskontos der Kurpfalz Tonwerke GmbH",
            sections=[
                _section(
                    "1. Konto- und Exportangaben",
                    """
                    Kurpfalzbank eG, BIC KUPFDE66XXX. Kontoinhaberin ist die Kurpfalz
                    Tonwerke GmbH; IBAN DE21 6709 0010 8842 6170 03. Der PDF-Export
                    KPB-ARCHIV-20260904-771 umfasst die nachfolgend bezeichneten
                    Originalauszugsseiten aus dem Onlinearchiv. Er wurde am 4. September
                    2026 von Leila Werner erzeugt. Buchungstag, Valuta, End-to-End-Referenz,
                    Anfangs- und Endsaldo werden unverändert aus den Archivdatensätzen
                    wiedergegeben.
                    """,
                    tables=[
                        _table(
                            ["Auszug", "Zeitraum", "Anfangssaldo EUR", "Endsaldo EUR", "Seitenstatus"],
                            [
                                ["2024/02-04", "16.02.–19.02.2024", 74320.18, 203504.36, "vollständig"],
                                ["2024/04-01", "01.04.–02.04.2024", 112444.10, 110932.10, "vollständig"],
                                ["2024/05-02", "06.05.–08.05.2024", 58410.22, 87702.38, "vollständig"],
                                ["2024/07-01", "01.07.–02.07.2024", 166201.77, 162485.77, "vollständig"],
                                ["2024/08-11", "29.08.–30.08.2024", 131440.91, 109327.54, "vollständig"],
                                ["2024/10-01", "01.10.–02.10.2024", 122800.00, 117294.22, "vollständig"],
                                ["2025/01-01", "02.01.–03.01.2025", 108933.45, 105253.45, "vollständig"],
                                ["2025/03-06", "29.03.–31.03.2025", 97310.55, 87755.20, "vollständig"],
                                ["2025/09-18", "29.09.–30.09.2025", 83110.18, 65684.09, "vollständig"],
                            ],
                        )
                    ],
                ),
                _section(
                    "2. Kreditrelevante Originalbuchungszeilen",
                    """
                    Nicht kreditbezogene Umsätze der jeweiligen kurzen Auszugszeiträume
                    bleiben auf den Originalseiten erhalten, werden in dieser
                    Kontrolltabelle aber nicht nochmals aufgelistet. Die angegebenen
                    Anfangs- und Endsalden beziehen sich jeweils auf die vollständige
                    Auszugsseite und sind deshalb keine bloßen Teilsalden.
                    """,
                    tables=[
                        _table(
                            ["Buchung", "Valuta", "Soll EUR", "Haben EUR", "Buchungstext", "End-to-End-Referenz", "Auszug"],
                            [
                                ["19.02.2024", "19.02.2024", "", 180000, "Neckarbrücke / Darlehen Tranche 1", "KT-2024-021-T1", "2024/02-04"],
                                ["02.04.2024", "02.04.2024", 1512, "", "Zins KT-2024-021 Q1", "KT-2024-021-ZQ1", "2024/04-01"],
                                ["07.05.2024", "07.05.2024", "", 40000, "Neckarbrücke / Darlehen Tranche 2", "KT-2024-021-T2", "2024/05-02"],
                                ["02.07.2024", "02.07.2024", 3716, "", "Zins KT-2024-021 Q2", "KT-2024-021-ZQ2", "2024/07-01"],
                                ["30.08.2024", "30.08.2024", 20000, "", "Tilgung Darlehen 150224", "KT-2024-021-TILG1", "2024/08-11"],
                                ["02.10.2024", "02.10.2024", 3920, "", "Zins KT-2024-021 Q3", "KT-2024-021-ZQ3", "2024/10-01"],
                                ["03.01.2025", "03.01.2025", 3680, "", "Zins KT-2024-021 Q4", "KT-2024-021-ZQ4", "2025/01-01"],
                                ["31.03.2025", "31.03.2025", 7500, "", "Tilgung 1/2025, bitte Kapital", "KT-2024-021-TILG2", "2025/03-06"],
                                ["30.09.2025", "30.09.2025", 15000, "", "Darlehen Tilgung / Abstimmung SW", "KT-2024-021-TILG3", "2025/09-18"],
                            ],
                        )
                    ],
                ),
                _section(
                    "3. Empfängerseitiger Kontrollbeleg vom 10. Oktober 2025",
                    """
                    Der von Rebenpfad für die Kontenabstimmung bereitgestellte
                    Buchungszeilenexport ihres Kontos weist am 10. Oktober 2025 eine
                    Gutschrift von 15.000 Euro durch Neckarbrücke aus. Der Text lautet
                    „Kaufpreisabrechnung Portfolio KT“, End-to-End-Referenz
                    „NB-PORT-KT-1010“. Die Betragsgleichheit und der zeitliche Zusammenhang
                    sind belegt; eine ausdrückliche Schuldnerreferenz oder ein
                    Weiterleitungsavis fehlt.
                    """,
                    tables=[
                        _table(
                            ["Buchung", "Valuta", "Haben EUR", "Auftraggeber", "Referenz", "Status"],
                            [["10.10.2025", "10.10.2025", 15000, "Neckarbrücke Finanzierungs GmbH", "NB-PORT-KT-1010", "endgültig gebucht"]],
                        )
                    ],
                ),
            ],
        ),
        _document(
            "09_Registerauszug_KURPFALZKLANG.pdf",
            "pdf",
            "Fiktive Registerabschrift zur deutschen Wortmarke KURPFALZKLANG",
            """
            Deutsches Patent- und Markenamt – Arbeitsabschrift aus dem Register,
            abgerufen am 3. September 2026. Registernummer 30 2020 059 412. Zeichen:
            KURPFALZKLANG. Markenform: Wortmarke. Anmeldetag und Prioritätstag:
            18. September 2020. Eintragung: 12. Januar 2021. Schutzende laut Abschrift:
            18. September 2030.
            """,
            """
            Eingetragene Inhaberin ist die Kurpfalz Tonwerke GmbH, Hafenbogen 17,
            68159 Mannheim. Vertreter ist laut Register die Kanzlei Faber & Loos,
            Mannheim. Die Waren- und Dienstleistungen umfassen Audiogeräte,
            Lautsprecher, elektronische Signalprozessoren und Einzelhandelsleistungen
            für Audiotechnik in den Klassen 9 und 35 sowie Musikinstrumentenzubehör in
            Klasse 15.
            """,
            """
            Im sichtbaren Registerverlauf ist keine Rechtsübertragung eingetragen.
            Unter „sonstige Verfahren“ ist ein am 16. Mai 2025 erledigter Widerspruch
            vermerkt. Die Abschrift enthält den Hinweis, dass registerfremde
            schuldrechtliche Vereinbarungen nicht wiedergegeben werden.
            """,
        ),
        _document(
            "10_Registerauszug_MANNHEIM_MODULAR.pdf",
            "pdf",
            "Fiktive Registerabschrift zur deutschen Wort-/Bildmarke MANNHEIM MODULAR",
            """
            Deutsches Patent- und Markenamt – Arbeitsabschrift aus dem Register,
            abgerufen am 3. September 2026. Registernummer 30 2021 227 861. Das Zeichen
            besteht aus den Wörtern MANNHEIM MODULAR und einer stilisierten blauen
            Wellenform. Anmeldetag: 4. Juni 2021. Für einen Teil der Waren wird in der
            Historie ein Prioritätsvermerk vom 28. Mai 2021 genannt. Eintragung:
            19. November 2021.
            """,
            """
            Inhaberin ist die Kurpfalz Tonwerke GmbH. Erfasst sind modulare
            Audiosysteme, Gehäuse und Steuergeräte der Klasse 9, Musikinstrumente und
            Zubehör der Klasse 15 sowie Durchführung von Workshops und
            Produktvorführungen der Klasse 41. Eine Sicherungsübertragung ist im
            Register nicht vermerkt.
            """,
            """
            Die Abschrift weist eine Lizenzanzeige vom 7. März 2023 zugunsten Hainblick
            Audiohandel e.K. aus, bezeichnet als „einfache Lizenz, Gebiet Deutschland,
            Ende 31.12.2027“. Die elektronische Akte zur Lizenzanzeige wurde im
            Datenraum nicht bereitgestellt. Die Registernummer weicht von der auf einem
            Datenraum-Tabellenblatt genannten Endziffer 816 ab.
            """,
        ),
        _document(
            "11_Registerauszug_RHEINPULS_AUDIO.pdf",
            "pdf",
            "Fiktive EUIPO-Registerabschrift zur Unionsmarke RHEINPULS AUDIO",
            """
            Amt der Europäischen Union für geistiges Eigentum – nicht beglaubigte
            Onlineabschrift, Abruf 3. September 2026. Unionsmarkennummer 018993742.
            Zeichen: RHEINPULS AUDIO. Markenart: Wortmarke. Anmeldung: 9. April 2024.
            Veröffentlichung: 2. Mai 2024. Eintragung: 30. August 2024. Schutzende:
            9. April 2034.
            """,
            """
            Als Inhaberin wird die Kurpfalz Tonwerke GmbH mit der damaligen Anschrift
            Industriestraße 44, 68169 Mannheim geführt. Vertreter ist in dieser
            Abschrift nicht eingetragen. Die Marke umfasst Audiointerfaces,
            Lautsprecher und herunterladbare Steuerungssoftware in Klasse 9,
            Musikinstrumentenzubehör in Klasse 15 und Online-Einzelhandelsdienste in
            Klasse 35.
            """,
            """
            Die Registerhistorie zeigt weder eine Übertragung noch eine eingetragene
            Lizenz. Ein im Datenraum als „EUIPO-Kontoauszug“ benanntes Gebührendokument
            fehlt. Die Abschrift enthält keine Aussage dazu, ob eine frühere
            Vereinbarung auch künftig entstehende Rechte erfasst.
            """,
        ),
        _document(
            "12_Vertriebs_und_Lizenzvertrag_Hainblick.docx",
            "docx",
            "Vertriebs- und Lizenzvertrag mit Hainblick Audiohandel e.K.",
            sections=[
                _section(
                    "1. Vertrag und Gebiet",
                    """
                    Der Vertrag vom 20. Februar 2023 wird zwischen der Kurpfalz Tonwerke
                    GmbH und Hainblick Audiohandel e.K., Bergpfad 5, 69121 Heidelberg,
                    geschlossen. Hainblick erhält das Recht, Produkte der Linie
                    MANNHEIM MODULAR in Deutschland zu vertreiben und das Zeichen in
                    Katalogen, Ladengeschäften und im eigenen Webshop zu benutzen. Der
                    gedruckte Vertrag bezeichnet die Lizenz als nicht ausschließlich.
                    """,
                ),
                _section(
                    "2. Laufzeit und Vergütung",
                    """
                    Der Vertrag läuft fest bis zum 31. Dezember 2027 und verlängert sich
                    jeweils um zwölf Monate, wenn er nicht sechs Monate vorher
                    gekündigt wird. Hainblick zahlt eine umsatzabhängige Markenlizenz von
                    zwei Prozent des Nettoumsatzes, mindestens jedoch 18.000 Euro pro
                    Kalenderjahr. Für 2025 weist die Abrechnung 21.640 Euro aus.
                    """,
                ),
                _section(
                    "3. Gebietsschutz und Übertragung",
                    """
                    § 4 Abs. 3 sieht lediglich vor, dass die Herstellerin während der
                    Vertragslaufzeit keinen weiteren Fachhändler mit einem exklusiven
                    Gebiet in Nordbaden bestellt. Eine E-Mail von Janis Heller vom
                    15. Januar 2024, die als Ausdruck hinter dem Vertrag liegt, lautet:
                    „Für Nordbaden bleibt ihr bis Ende 2027 unser einziger autorisierter
                    Händler.“ Hainblick bestätigte mit „Danke für die Exklusivität“. Ein
                    förmlicher Nachtrag wurde nicht unterzeichnet.
                    """,
                ),
                _section(
                    "4. Inhaberwechsel",
                    """
                    Nach § 11 soll die Herstellerin Hainblick über einen Wechsel des
                    Markeninhabers informieren. Der Vertrag enthält kein ausdrückliches
                    Kündigungsrecht bei Insolvenz. Rechte und Pflichten aus dem Vertrag
                    dürfen von der Herstellerin im Rahmen einer Übertragung des
                    Geschäftsbetriebs auf einen Rechtsnachfolger übertragen werden;
                    Hainblick soll mindestens zehn Werktage vorher benachrichtigt werden.
                    """,
                ),
            ],
        ),
        _document(
            "13_Forderungskauf_18-08-2025.pdf",
            "pdf",
            "Vertrag über den Verkauf der Darlehensforderung und Sicherheiten",
            sections=[
                _section(
                    "1. Verkäuferin, Käuferin und Stichtag",
                    """
                    Die Neckarbrücke Finanzierungs GmbH verkauft der Rebenpfad
                    Sicherheiten GmbH mit Vertrag vom 18. August 2025 mehrere
                    Unternehmensfinanzierungen. Für die Finanzierung der Kurpfalz
                    Tonwerke GmbH ist der wirtschaftliche Übergang auf den 31. Juli 2025
                    festgelegt. Die Abtretungen sollen mit Zahlung des anteiligen
                    Kaufpreises eintreten. Ausführung und Eingang des anteiligen
                    Kaufpreises sowie der Eintritt der Vollzugsbedingung werden gesondert
                    im Bank- und Closingbeleg vom 25. August 2025 dokumentiert.
                    """,
                ),
                _section(
                    "2. Forderung gegen Kurpfalz Tonwerke GmbH",
                    """
                    Anlage F bezeichnet einen Kapitalbetrag von 200.000 Euro und
                    abgegrenzte Vertragszinsen von 6.841,64 Euro zum Stichtag. Der
                    Forderungskaufpreis für diese Position beträgt 164.000 Euro. Die
                    Verkäuferin garantiert nicht die Zahlungsfähigkeit der Schuldnerin,
                    erklärt aber, ihr seien außer den in der Anlage vermerkten Einreden
                    keine Gegenrechte bekannt.
                    """,
                ),
                _section(
                    "3. Mitübertragene Sicherheiten",
                    """
                    Mit der Forderung werden alle akzessorischen und nicht
                    akzessorischen Sicherheiten sowie Ansprüche aus den jeweiligen
                    Sicherheitenabreden übertragen. Die Käuferin tritt in die
                    treuhänderischen Bindungen und Freigabepflichten ein. Anlage S nennt
                    KURPFALZKLANG mit der Registernummer 30 2020 059 412 und MANNHEIM
                    MODULAR mit der Registernummer 30 2021 227 861. In der Folgezeile
                    steht „einschließlich angemeldeter Marke RHEINPULS AUDIO, Nummer
                    derzeit nicht in Kreditakte“.
                    """,
                    """
                    Die Verkäuferin händigt die Kreditakte elektronisch aus. Sie
                    verpflichtet sich, Zahlungen, die nach dem Vollzug noch bei ihr
                    eingehen und wirtschaftlich auf verkaufte Forderungen entfallen,
                    innerhalb von fünf Bankarbeitstagen weiterzuleiten. Eigene
                    Aufrechnungen mit Nachforderungen aus der Kaufpreisabrechnung sind
                    nur nach vorheriger Mitteilung zulässig.
                    """,
                ),
                _section(
                    "4. Erklärungen und Ausfertigungsvermerk",
                    """
                    Die Verkäuferin erklärt, keine Marke verwertet oder freigegeben zu
                    haben. Sie weist darauf hin, dass die Register weiterhin die
                    Schuldnerin nennen. Der Vertragsindex bezeichnet Papierausfertigungen
                    mit Pauline Roth und Tarek Mansour für Rebenpfad sowie Sonja Wieland
                    und Armin Chandra für Neckarbrücke. Das vorliegende PDF ist eine
                    Inhaltsabschrift ohne Abbildungen dieser Unterschriften. Der
                    elektronische Vollzug ist in Dokument 13A, die übergebene Kreditakte
                    in Dokument 13B festgehalten.
                    """,
                ),
            ],
            tables=[
                _table(
                    ["Forderung", "Kapital EUR", "Zinsen EUR", "Sicherheiten laut Anlage S"],
                    [
                        ["KT-2024-021", 200000, 6841.64, "zwei DE-Marken; RHEINPULS AUDIO ohne Nummer"],
                    ],
                )
            ],
        ),
        _document(
            "13A_Zessionsvollzug_und_Kaufpreisbeleg_25-08-2025.pdf",
            "pdf",
            "Bankbeleg und Closingbestätigung zum Forderungskauf",
            sections=[
                _section(
                    "1. Bedingung und Zahlungsauftrag",
                    """
                    Nach Ziffer 2.3 des Forderungskaufvertrags tritt die Abtretung mit
                    Eingang des anteiligen Kaufpreises ein. Rebenpfad wies am 25. August
                    2025 um 09:02 Uhr 164.000 Euro von ihrem Konto
                    DE44 5465 0010 0028 7719 04 an Neckarbrücke an. Der Auftrag trägt die
                    End-to-End-Referenz RP-NB-KT-2024-021-CLOSE.
                    """,
                    tables=[
                        _table(
                            ["Auftraggeberin", "Empfängerin", "Betrag EUR", "Ausführung/Valuta", "Bankreferenz", "Status"],
                            [["Rebenpfad Sicherheiten GmbH", "Neckarbrücke Finanzierungs GmbH", 164000, "25.08.2025", "WBP250825090217644", "endgültig gebucht"]],
                        )
                    ],
                ),
                _section(
                    "2. Empfängergutschrift und Bedingungseintritt",
                    """
                    Der Firmenkontoauszug der Neckarbrücke weist die Gutschrift am
                    25. August 2025 um 11:31 Uhr mit Valuta desselben Tages und identischer
                    End-to-End-Referenz aus. Der gemeinsame Closinglog setzt den
                    Bedingungseintritt auf 11:35 Uhr. Rechtlicher Vollzug ist danach der
                    25. August 2025 um 11:35 Uhr; der vertragliche wirtschaftliche Stichtag
                    bleibt der 31. Juli 2025.
                    """,
                    tables=[
                        _table(
                            ["Kontrolle", "Soll EUR", "Ist EUR", "Differenz EUR", "Zeitstempel"],
                            [
                                ["anteiliger Kaufpreis KT-2024-021", 164000, 164000, 0, "Gutschrift 25.08.2025 11:31"],
                                ["Vollzugsbedingung Kaufpreiszahlung", 164000, 164000, 0, "Closinglog 25.08.2025 11:35"],
                            ],
                        )
                    ],
                ),
                _section(
                    "3. Reichweite des Belegs",
                    """
                    Der Beleg weist den Zahlungsfluss und den vertraglich bestimmten
                    Vollzugszeitpunkt nach. Er bestätigt nicht die Höhe der verkauften
                    Forderung, die richtige Behandlung der Zahlung über 7.500 Euro oder
                    die Bestimmtheit der ohne Registernummer bezeichneten Unionsmarke.
                    Die übertragenen Aktenbestandteile und Lücken stehen in Dokument 13B.
                    """,
                ),
            ],
        ),
        _xlsx(
            "13B_Kreditaktenuebergabe_25-08-2025.xlsx",
            "Übergabeprotokoll der Kredit- und Sicherheitenakte KT-2024-021",
            [
                _sheet(
                    "Uebergabeliste",
                    ["Nr.", "Aktenbestandteil", "Format/Stand", "übergeben", "Prüfhinweis Rebenpfad"],
                    [
                        [1, "Darlehensvertrag 15.02.2024", "Papieroriginal laut Neckarbrücke-Index; digitale Inhaltsabschrift", "25.08.2025", "Signaturabbildung nicht Teil des Datenexports"],
                        [2, "Sicherungsabrede 15.02.2024", "Papieroriginal laut Index; digitale Inhaltsabschrift", "25.08.2025", "Anlage gesondert prüfen"],
                        [3, "Anlage 1 Markenbestand", "XLSX mit JH-Kürzel; mehrere Fassungen", "25.08.2025", "RHEINPULS ohne Nummer in ursprünglicher Fassung"],
                        [4, "Abrufe Tranche 1 und 2", "EML 16.02. und 03.05.2024", "25.08.2025", "Textform und Beträge stimmen"],
                        [5, "CP-Check Tranche 1", "XLSX 19.02.2024", "25.08.2025", "begrenzte Waiver; offene Unterlagen"],
                        [6, "SEPA-Ausführungsbelege", "Bankexport bis 08.05.2024", "25.08.2025", "Valutierung 220.000 EUR belegt"],
                        [7, "Kreditjournal und Zinsabrechnungen", "CSV; Kontoauszüge", "25.08.2025", "Zahlung 7.500 EUR anders bezeichnet als gebucht"],
                        [8, "Amtliche Registerunterlagen", "zwei DE-Ausdrucke", "25.08.2025", "keine Umschreibung"],
                        [9, "EUIPO-Anmeldebeleg RHEINPULS", "nicht in Kreditakte", "nein", "Nummer aus Schuldnermail, Primärbeleg fehlt"],
                        [10, "Versicherungsabtretung", "nicht in Kreditakte", "nein", "offener CP-Punkt"],
                        [11, "Hainblick-Vertrag", "nicht in Kreditakte", "nein", "Lizenz-/Gebietsschutzrisiko"],
                    ],
                    "Übergeben wurde ein verschlüsselter Export mit Index KT-2024-021-TRANSFER-01. Fehlende Unterlagen bleiben ausdrücklich als fehlend gekennzeichnet.",
                ),
                _sheet(
                    "Uebergabekontrolle",
                    ["Feld", "Wert"],
                    [
                        ["Export bereitgestellt", "25.08.2025 12:06 CET"],
                        ["Download Rebenpfad abgeschlossen", "25.08.2025 12:41 CET"],
                        ["Dateien laut Manifest", 18],
                        ["Dateien technisch übertragen", 18],
                        ["Differenz", 0],
                        ["Manifest-Hash", "SHA256 5d7e61d9...b214"],
                        ["Quittierende Rollen", "Armin Chandra / Pauline Roth"],
                        ["Vorbehalt", "keine Saldenbestätigung und keine Bestätigung der Wirksamkeit einzelner Sicherheiten"],
                    ],
                    "Die Namensangabe dokumentiert die elektronische Freigabe im Closinglog; die Arbeitsmappe enthält keine Bildsignaturen.",
                ),
            ],
        ),
        _mail(
            "14_Anzeige_Forderungsabtretung.eml",
            "Anzeige des Gläubigerwechsels an die Schuldnerin",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "kreditservice@neckarbruecke-finanz.example",
            "2025-08-25T15:32:00+02:00",
            "Darlehen KT-2024-021 – neuer Gläubiger und Sicherheitenverwaltung",
            """
            Sehr geehrter Herr Heller,

            die Neckarbrücke Finanzierungs GmbH hat ihre Ansprüche aus dem
            Darlehensvertrag vom 15. Februar 2024 mit Wirkung zum heutigen Tag an die
            Rebenpfad Sicherheiten GmbH abgetreten. Der Übergang umfasst nach unserer
            Vereinbarung auch die Rechte aus der Sicherungsübertragung der Marken
            KURPFALZKLANG, MANNHEIM MODULAR und RHEINPULS AUDIO. Künftige Zahlungen
            leisten Sie bitte ausschließlich auf das im beigefügten Schreiben genannte
            Konto der Rebenpfad Sicherheiten GmbH.

            Der uns übergebene Saldo zum 31. Juli 2025 beträgt 206.841,64 Euro,
            bestehend aus 200.000 Euro Kapital und 6.841,64 Euro Zinsen. Falls Ihre
            Buchhaltung hiervon abweicht, senden Sie uns bitte die Buchungsbelege. Die
            bisherigen Nutzungsbefugnisse an den Marken werden durch den
            Gläubigerwechsel zunächst nicht geändert.

            Freundliche Grüße
            Pauline Roth
            """,
            attachments=(
                "13_Forderungskauf_18-08-2025.pdf",
                "13A_Zessionsvollzug_und_Kaufpreisbeleg_25-08-2025.pdf",
            ),
        ),
        _mail(
            "14A_Empfangsbestaetigung_Glaeubigerwechsel.eml",
            "Empfangsbestätigung der Schuldnerin zur Abtretungsanzeige",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "kreditservice@neckarbruecke-finanz.example; Leila Werner <leila.werner@kurpfalz-tonwerke.example>",
            "2025-08-26T09:08:00+02:00",
            "AW: Darlehen KT-2024-021 – neuer Gläubiger und Sicherheitenverwaltung",
            """
            Sehr geehrte Frau Roth,

            wir bestätigen den Eingang Ihrer Nachricht vom 25. August 2025 nebst
            Forderungskaufvertrag. Unsere Kreditorenstammdaten werden auf das von Ihnen
            mitgeteilte Konto umgestellt. Diese Empfangsbestätigung ist keine Anerkennung
            des genannten Saldos; unsere Buchhaltung gleicht insbesondere die Zahlung vom
            31. März 2025 noch ab.

            Bitte richten Sie künftige Zinsabrechnungen zusätzlich an Frau Werner. Die
            laufende Nutzung der Marken setzen wir entsprechend Ihrer Mitteilung zunächst
            fort.

            Freundliche Grüße
            Janis Heller
            """,
            attachments=("14_Anzeige_Forderungsabtretung.eml",),
        ),
        _xlsx(
            "15_Forderungskonto_Rebenpfad.xlsx",
            "Forderungskonto und interne Saldenabstimmung der Rebenpfad Sicherheiten GmbH",
            [
                _sheet(
                    "Saldo",
                    ["Datum", "Vorgang", "Kapital Soll EUR", "Zinsen/Kosten Soll EUR", "Zahlung EUR", "Zuordnung", "Kapitalsaldo EUR"],
                    [
                        ["31.07.2025", "Übernommener Anfangssaldo", 200000, 6841.64, 0, "laut Verkäuferin", 200000],
                        ["25.08.2025", "Vollzug Forderungskauf", 0, 0, 0, "wirtschaftlicher Übergang 31.07.", 200000],
                        ["30.09.2025", "Zahlung Schuldnerin an Altgläubigerin", 0, 0, 15000, "nicht auf Schuldnerkonto gebucht", 200000],
                        ["10.10.2025", "Eingang Neckarbrücke", 0, 0, 15000, "Kaufpreisabrechnung Portfolio KT", 200000],
                        ["31.12.2025", "Vertragszins bis Endfälligkeit", 0, 5968.36, 0, "Zinslauf", 200000],
                        ["15.02.2026", "Mahnkosten", 0, 450, 0, "Schreiben 16", 200000],
                        ["01.09.2026", "Zinsfortschreibung/Verfahrenskosten", 0, 9714, 0, "interne Berechnung", 200000],
                        ["01.09.2026", "Gesamt", 200000, 22974, 0, "ohne Gutschrift 15.000", 200000],
                    ],
                    "Der Eingang vom 10.10.2025 wurde im Portfoliokauf-Verrechnungskonto erfasst. Ob er wirtschaftlich eine von der Schuldnerin geleistete Tilgung weiterleitete, ist in dieser Arbeitsmappe nicht entschieden.",
                    "Dieses Blatt bildet die unveränderte Parteibuchung von Rebenpfad ab. Die davon getrennte act/360-Nachrechnung und Kontrollsumme steht in 07A_Kreditkonto_und_Saldenstaffel.xlsx.",
                ),
                _sheet(
                    "Gegenrechnung_Schuldnerin",
                    ["Position", "Betrag EUR", "Quelle", "Behandlung Rebenpfad"],
                    [
                        ["Auszahlungen", 220000, "Kontoauszüge", "anerkannt"],
                        ["Tilgung 30.08.2024", -20000, "Kontoauszug", "anerkannt"],
                        ["Zahlung 31.03.2025", -7500, "Verwendungszweck Kapital", "Zinsen/Kosten"],
                        ["Zahlung 30.09.2025", -15000, "an Neckarbrücke nach Anzeige", "nicht als Schuldnerzahlung"],
                        ["Kapital nach Sicht Schuldnerin", 177500, "Mail 17", "bestritten"],
                    ],
                    "Die Gegenrechnung bildet eine Parteidarstellung ab und ist keine Freigabe oder Saldenbestätigung.",
                ),
                _sheet(
                    "Kontrollabgleich",
                    ["Stichtag/Position", "Rebenpfad EUR", "neutrale Kontrolle EUR", "Differenz EUR", "Einordnung"],
                    [
                        ["Kapital 31.07.2025 – Szenario Schuldnerweisung", 200000, 192500, 7500, "Zuordnung Zahlung 31.03. streitig"],
                        ["Kapital 31.07.2025 – Vertragskaskade", 200000, 196100, 3900, "Q1-Zins 3.600; Rest Kapital"],
                        ["Zinsen/Kosten 31.07.2025 bei Gläubigerzuordnung", 6841.64, 4840, 2001.64, "Kosten-/Rechenbeleg fehlt"],
                        ["Zahlung 30.09./Eingang 10.10.2025", 0, 15000, -15000, "keine Forderungsgutschrift trotz Geldeingang"],
                        ["Zins 31.07.–31.12.2025 bei 200.000 Kapital", 5968.36, 6160, -191.64, "act/360: 154 Tage"],
                    ],
                    "Die Kontrollwerte stammen aus Dokument 07A. Negative Differenzen bedeuten nicht automatisch ein Guthaben; sie markieren ungeklärte Parteibuchungen.",
                ),
                _sheet(
                    "Sicherheiten",
                    ["Zeichen", "Nummer", "Übernahme im Forderungskauf", "Registerumschreibung", "interne Einstufung"],
                    [
                        ["KURPFALZKLANG", "30 2020 059 412", "ja, ausdrücklich", "nein", "bestellt"],
                        ["MANNHEIM MODULAR", "30 2021 227 861", "ja, ausdrücklich", "nein", "bestellt; Lizenz prüfen"],
                        ["RHEINPULS AUDIO", "018993742", "nur Name, Nummer fehlt", "nein", "Rechtskette offen"],
                    ],
                    "Die Einstufung stammt aus der Kreditverwaltung und ersetzt keine Prüfung der Originalurkunden.",
                ),
            ],
        ),
        _document(
            "16_Endfaelligkeit_und_Zahlungsaufforderung.docx",
            "docx",
            "Zahlungsaufforderung und Anzeige der Verwertungsreife",
            """
            Die Rebenpfad Sicherheiten GmbH teilt der Kurpfalz Tonwerke GmbH mit
            Schreiben vom 15. Februar 2026 mit, dass das Darlehen am 31. Dezember 2025
            endfällig geworden sei. Ausgewiesen werden 200.000 Euro Kapital, 12.810
            Euro Zinsen bis zum 31. Dezember 2025 und 450 Euro Kosten. Die Zahlung soll
            bis zum Ablauf des 3. März 2026 auf das Konto der Rebenpfad Sicherheiten GmbH
            erfolgen. Die Frist entspricht zehn Bankarbeitstagen nach dem im
            Versandprotokoll ausgewiesenen Zugang am 17. Februar 2026.
            """,
            """
            Das Schreiben verweist auf die Sicherungsübertragung der Marken. Es
            kündigt an, nach fruchtlosem Ablauf der Frist eine konkrete
            Verwertungsankündigung zu übersenden. Zugleich bietet Rebenpfad ein Gespräch
            über eine abgestimmte Kontenklärung und einen geordneten Verkauf einzelner
            Produktlinien an. Die Zahlungsaufforderung selbst widerruft die Rücklizenz
            noch nicht und legt noch keine Verwertungsart fest.
            """,
            """
            Im letzten Absatz heißt es, die Annahme von Teilzahlungen stelle weder eine
            Stundung noch eine Freigabe von Sicherheiten dar. Der Versandindex nennt
            Pauline Roth und Tarek Mansour als elektronisch freigebende Personen. Das
            vorliegende DOCX ist die Inhaltsabschrift ohne Unterschriftsbilder. Versand
            und Zugang werden gemeinsam mit dem späteren Sicherungsfallschreiben im
            Zustellstatus 16C dokumentiert.
            """,
        ),
        _document(
            "16A_Sicherungsfall_und_Verwertungsankuendigung_04-03-2026.pdf",
            "pdf",
            "Sicherungsfall und konkrete Ankündigung des Verwertungsverfahrens",
            sections=[
                _section(
                    "1. Eintritt der Verwertungsreife",
                    """
                    Rebenpfad erklärt gegenüber der Kurpfalz Tonwerke GmbH am 4. März
                    2026, das Darlehen sei seit dem 31. Dezember 2025 endfällig. Die am
                    17. Februar 2026 zugestellte Zahlungsaufforderung habe eine Nachfrist
                    bis zum Ablauf des 3. März 2026 gesetzt. Bis 4. März 2026, 08:00 Uhr,
                    sei weder auf dem Forderungskonto noch auf dem in der
                    Zahlungsaufforderung genannten Bankkonto eine weitere Zahlung
                    eingegangen. Rebenpfad beruft sich daher auf Ziffer 5 der
                    Sicherungsabrede.
                    """,
                ),
                _section(
                    "2. Saldo und ausdrücklich offener Zuordnungskonflikt",
                    """
                    Rebenpfad verfolgt ihren Buchsaldo, kennzeichnet jedoch die Zahlungen
                    vom 31. März und 30. September 2025 sowie die Zinskontrolle als
                    streitig. Selbst die niedrigeren neutralen Rechenszenarien weisen am
                    4. März 2026 eine erhebliche unbezahlte Hauptforderung aus. Die
                    Verwertungsankündigung enthält deshalb keine Saldenanerkennung der
                    Schuldnerin und nimmt der Kontenabstimmung nicht vorweg.
                    """,
                    tables=[
                        _table(
                            ["Position/Szenario", "Kapital EUR", "Zinsen EUR", "Kosten EUR", "Gesamt EUR", "Status"],
                            [
                                ["Buchsaldo Rebenpfad 04.03.2026", 200000, 15290, 450, 215740, "bestritten; 12.810 bis 31.12. plus 2.480 act/360"],
                                ["Neutral A – Schuldnerweisung", 177500, 16109.50, 450, 194059.50, "7.500 und 15.000 als Kapital; Zinsen offen"],
                                ["Neutral B – Vertragskaskade", 188238.04, 5835.38, 450, 194523.42, "Zahlungen zuerst auf fällige Zinsen"],
                            ],
                        )
                    ],
                ),
                _section(
                    "3. Beabsichtigte Art und Zeit der Verwertung",
                    """
                    Rebenpfad kündigt einen dokumentierten beschränkten Bieterprozess für
                    die in Anlage 1 bezeichneten Marken an. Ab 7. März 2026 sollen nach
                    Vertraulichkeitsvereinbarung mindestens fünf strategische Erwerber
                    angesprochen werden. Verbindliche Angebote sind bis 18. März 2026,
                    12:00 Uhr, einzuholen. Eine unabhängige indikative Bewertung und eine
                    Gegenüberstellung sämtlicher Angebote sollen der Entscheidung
                    vorausgehen. Ein Zuschlag oder freihändiger Verkauf soll frühestens am
                    20. März 2026 und nur zum wirtschaftlich besten nachvollziehbaren
                    Angebot erfolgen.
                    """,
                    """
                    Kurpfalz Tonwerke kann bis zur Zuschlagsentscheidung durch vollständige
                    Zahlung oder eine schriftliche Stillhaltevereinbarung die Verwertung
                    abwenden. Die Rücklizenz wird nicht sofort widerrufen; ein Widerruf
                    wird für den Zeitpunkt eines wirksamen Übertragungsvertrags angekündigt.
                    Die bestehende Hainblick-Lizenz und die offene Reichweite hinsichtlich
                    RHEINPULS AUDIO sind jedem Bieter offenzulegen.
                    """,
                ),
                _section(
                    "4. Freigabe und Versandfassung",
                    """
                    Der Versandindex nennt Pauline Roth und Tarek Mansour als am 4. März
                    2026 um 08:31 Uhr elektronisch freigebende Personen. Diese PDF-Fassung
                    enthält gedruckte Namen und Funktionen, aber keine Abbildungen
                    handschriftlicher Unterschriften. Versandweg, Nachrichten-ID und
                    Zustellereignisse stehen in den E-Mails 16B und 16C.
                    """,
                ),
            ],
        ),
        _mail(
            "16B_Versand_Sicherungsfallschreiben.eml",
            "Versand des Sicherungsfallschreibens an die Schuldnerin",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "Leila Werner <leila.werner@kurpfalz-tonwerke.example>; Tarek Mansour <tarek.mansour@rebenpfad-sicherheiten.example>",
            "2026-03-04T08:46:00+01:00",
            "KT-2024-021 – Sicherungsfall und Verwertungsverfahren",
            """
            Sehr geehrter Herr Heller,

            nach fruchtlosem Ablauf der bis gestern gesetzten Nachfrist übersenden wir
            das beigefügte Sicherungsfallschreiben. Darin bezeichnen wir die beabsichtigte
            Art und den Zeitplan der Verwertung. Der niedrigste aus der neutralen
            Saldenstaffel folgende Betrag bleibt erheblich offen; die Kontenstreitigkeiten
            über 7.500 Euro, 15.000 Euro und die Zinsbuchungen werden ausdrücklich nicht
            vorweggenommen.

            Eine gleichlautende Papierfassung ist heute unter
            NBX-RS-20260304-77291 an den Geschäftssitz versandt worden. Bitte teilen Sie
            uns bis 9. März mit, ob Sie eine vollständige Zahlung, eine
            Stillhaltevereinbarung oder einen abgestimmten Unternehmensverkauf erörtern
            wollen.

            Freundliche Grüße
            Pauline Roth
            """,
            attachments=(
                "16A_Sicherungsfall_und_Verwertungsankuendigung_04-03-2026.pdf",
                "07A_Kreditkonto_und_Saldenstaffel.xlsx",
            ),
        ),
        _mail(
            "16C_Zustellnachweis_Sicherungsfallschreiben.eml",
            "Elektronischer Zustellstatus der Zahlungsaufforderung und Verwertungsankündigung",
            "Kurier Nordbaden Statusdienst <status@kurier-nordbaden.example>",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "Tarek Mansour <tarek.mansour@rebenpfad-sicherheiten.example>",
            "2026-03-05T10:18:00+01:00",
            "Zustellstatus KT-2024-021 / NBX-RS-20260304-77291",
            """
            Automatischer Zustellbericht für Rebenpfad Sicherheiten GmbH.

            Vorgang NBX-EIN-20260216-18314, Zahlungsaufforderung KT-2024-021:
            eingeliefert 16.02.2026 09:12 Uhr; zugestellt am Geschäftssitz der Kurpfalz
            Tonwerke GmbH am 17.02.2026 10:06 Uhr; angenommen von Leila Werner,
            Empfangsberechtigte; Status endgültig.

            Vorgang NBX-RS-20260304-77291, Sicherungsfall und
            Verwertungsankündigung: eingeliefert 04.03.2026 09:03 Uhr; zugestellt am
            Geschäftssitz am 05.03.2026 10:11 Uhr; angenommen von Leila Werner,
            Empfangsberechtigte; Status endgültig.

            Die elektronischen Ereignisprotokolle sind unter den genannten Vorgängen im
            Kundenkonto archiviert. Dieser Statusbericht bestätigt Übergabe, Inhalt oder
            rechtliche Wirkung der Sendungen werden vom Zustelldienst nicht geprüft.
            """,
            attachments=(),
        ),
        _mail(
            "17_Einwendungen_Schuldnerin.eml",
            "Einwendungen der Schuldnerin gegen den geforderten Saldo",
            "Janis Heller <janis.heller@kurpfalz-tonwerke.example>",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "Leila Werner <leila.werner@kurpfalz-tonwerke.example>",
            "2026-02-19T18:06:00+01:00",
            "Saldo KT-2024-021 und Marken",
            """
            Sehr geehrte Frau Roth,

            Ihren Kapitalbetrag von 200.000 Euro kann unsere Buchhaltung nicht
            nachvollziehen. Neben den 20.000 Euro aus August 2024 haben wir am 31. März
            2025 weitere 7.500 Euro mit dem eindeutigen Hinweis „bitte Kapital“ und am
            30. September 2025 noch einmal 15.000 Euro gezahlt. Dass die letzte Zahlung
            versehentlich an Neckarbrücke ging, ändert aus unserer Sicht nichts daran,
            dass sie dort angekommen ist. Frau Wieland hatte die Zahlung telefonisch
            bestätigt.

            Wir kommen deshalb vor Zinsen auf 177.500 Euro. Die Zinsberechnung lässt
            sich aus Ihrem Schreiben nicht nachrechnen. Bitte beachten Sie außerdem,
            dass MANNHEIM MODULAR bis Ende 2027 an Hainblick lizenziert ist. RHEINPULS
            wurde erst nach dem Sicherheitenvertrag angemeldet; ich finde dazu in
            unserem unterschriebenen Ordner keinen Nachtrag.

            Die Gesellschaft will eine Gesamtlösung und kann die Zeichen nicht aus dem
            laufenden Betrieb herauslösen. Die Sicherungsübertragung war nach unserem
            damaligen Verständnis eine Absicherung, kein sofortiger Wechsel des
            Marktauftritts. Einer isolierten Verwertung der Marken stimmen wir derzeit
            nicht zu.

            Mit freundlichen Grüßen
            Janis Heller
            """,
            attachments=("08_Kontoauszuege_Schuldnerin.pdf",),
        ),
        _document(
            "18_Beschluss_vorlaeufige_Insolvenzverwaltung.pdf",
            "pdf",
            "Beschluss über vorläufige Insolvenzverwaltung vom 21. Juli 2026",
            """
            Amtsgericht Mannheim, Insolvenzgericht, 8 IN 233/26. In dem Verfahren über
            den Antrag der Kurpfalz Tonwerke GmbH vom 20. Juli 2026 wird am 21. Juli
            2026 um 11:20 Uhr Dr. Helena Aydin zur vorläufigen Insolvenzverwalterin
            bestellt. Verfügungen der Schuldnerin bedürfen der Zustimmung der
            vorläufigen Verwalterin. Maßnahmen der Zwangsvollstreckung werden
            einstweilen untersagt, soweit gesetzlich vorgesehen.
            """,
            """
            Die vorläufige Verwalterin soll Vermögen sichern, die wirtschaftliche Lage
            prüfen und die Fortführungsmöglichkeiten untersuchen. Die Schuldnerin hat
            Bücher, elektronische Zugangsdaten, Verträge, Schutzrechtsunterlagen und
            sonstige Geschäftsunterlagen herauszugeben. Drittschuldner werden darauf
            hingewiesen, Zahlungen nur unter Beachtung des Zustimmungsvorbehalts zu
            leisten.
            """,
            """
            Der Beschluss enthält keine Feststellung zu Eigentum oder
            Verwertungsbefugnissen an einzelnen Markenrechten. Im Anlagenverzeichnis des
            Insolvenzantrags sind die drei Zeichen als „betriebsnotwendiges IP;
            Sicherheitenanzeige Rebenpfad, Umfang streitig“ aufgeführt. Die
            Zustellungsurkunde an Rebenpfad ist auf den 26. Juli 2026 datiert.
            """,
        ),
        _document(
            "19_Insolvenzeroeffnungsbeschluss_01-09-2026.pdf",
            "pdf",
            "Beschluss über die Eröffnung des Insolvenzverfahrens",
            """
            Amtsgericht Mannheim, Insolvenzgericht, 8 IN 233/26. Das
            Insolvenzverfahren über das Vermögen der Kurpfalz Tonwerke GmbH,
            Hafenbogen 17, 68159 Mannheim, wird am 1. September 2026 um 09:00 Uhr wegen
            Zahlungsunfähigkeit und Überschuldung eröffnet. Zur Insolvenzverwalterin
            wird Rechtsanwältin Dr. Helena Aydin, Augustaanlage 81, 68165 Mannheim,
            bestellt.
            """,
            """
            Insolvenzgläubiger werden aufgefordert, ihre Forderungen bis zum 6. Oktober
            2026 anzumelden. Der Berichtstermin und Termin zur Prüfung der angemeldeten
            Forderungen wird auf den 18. November 2026 bestimmt. Personen, die
            Gegenstände oder Rechte der Masse beanspruchen oder Sicherungsrechte geltend
            machen, sollen der Verwalterin Gegenstand, Rechtsgrund und Belege mitteilen.
            """,
            """
            Verfügungen der Schuldnerin sind ab Verfahrenseröffnung nur nach Maßgabe der
            Insolvenzordnung wirksam. Der Beschluss enthält keine Einzelfallentscheidung
            über die in der Vermögensübersicht aufgeführten Marken. Die öffentliche
            Bekanntmachung wurde am 1. September 2026 um 10:12 Uhr veranlasst.
            """,
        ),
        _xlsx(
            "20_IP_Inventar_Insolvenzverwaltung.xlsx",
            "IP-Inventar der Insolvenzverwaltung",
            [
                _sheet(
                    "Registrierte_Rechte",
                    ["ID", "Recht", "Nummer", "Registerinhaber", "Belastung laut Akte", "Datenraumstatus"],
                    [
                        ["IP-01", "KURPFALZKLANG", "30 2020 059 412", "Kurpfalz Tonwerke GmbH", "Sicherungsübertragung Rebenpfad behauptet", "Auszug vorhanden"],
                        ["IP-02", "MANNHEIM MODULAR", "30 2021 227 861", "Kurpfalz Tonwerke GmbH", "Sicherung; Hainblick-Lizenz", "Vertrag und Auszug vorhanden"],
                        ["IP-03", "RHEINPULS AUDIO", "018993742", "Kurpfalz Tonwerke GmbH", "Erfassung durch Nachanmeldungsklausel offen", "Auszug vorhanden"],
                    ],
                    "Erstellt am 28.08.2026 aus Kreditakte, Registerabschriften und Angaben des Geschäftsführers.",
                ),
                _sheet(
                    "Weitere_Assets",
                    ["ID", "Asset", "Inhaberin laut Unterlagen", "Vertragsbezug", "Bemerkung"],
                    [
                        ["IP-04", "Domain kurpfalzklang.example", "Kurpfalz Tonwerke GmbH", "Providervertrag", "Transfercode beim Administrator"],
                        ["IP-05", "Domain rheinpuls-audio.example", "Marlene Vogt laut Providerexport", "Nutzungsüberlassung mündlich", "Umschreibung offen"],
                        ["IP-06", "Produktdesign RP-01", "Urheberangaben uneinheitlich", "Designerrechnungen", "keine Registerrecherche"],
                        ["IP-07", "Social-Media-Konten", "Unternehmensprofile", "Plattformbedingungen", "Zugang gesichert"],
                        ["IP-08", "Kundendatenbank", "Kurpfalz Tonwerke GmbH", "CRM-Export", "datenschutzrechtlich gesondert"],
                    ],
                    "Weitere Assets sind nicht Bestandteil der Sicherheitenliste vom 15.02.2024, soweit dort nicht ausdrücklich bezeichnet.",
                ),
                _sheet(
                    "Offene_Unterlagen",
                    ["Unterlage", "angefordert am", "Quelle", "Stand 01.09.2026"],
                    [
                        ["Original Anlage 1", "24.07.2026", "Geschäftsführer", "Scan in zwei Fassungen"],
                        ["EUIPO-Anmeldebeleg", "24.07.2026", "ehemalige Markenkanzlei", "nicht eingegangen"],
                        ["Lizenzanzeige Hainblick", "05.08.2026", "Markenkanzlei", "Registerauszug genügt nicht"],
                        ["Saldenabstimmung Rebenpfad", "27.07.2026", "Rebenpfad", "Kontoauszug angekündigt"],
                    ],
                    "Die Liste dokumentiert den Beschaffungsstand und keine rechtliche Bewertung.",
                ),
            ],
        ),
        _mail(
            "21_Anzeige_Sicherungsrechte_an_Verwalterin.eml",
            "Anzeige der Sicherungsrechte im eröffneten Verfahren",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "Dr. Helena Aydin <insolvenz@aydin-partner.example>",
            "Tarek Mansour <tarek.mansour@rebenpfad-sicherheiten.example>",
            "2026-09-04T11:48:00+02:00",
            "8 IN 233/26 – Markenrechte und Darlehen KT-2024-021",
            """
            Sehr geehrte Frau Dr. Aydin,

            Rebenpfad ist Inhaberin der Darlehensforderung aus dem Vertrag vom
            15. Februar 2024 und der zusammen mit ihr übertragenen Sicherheiten. Dazu
            gehören nach unserer Akte die Marken KURPFALZKLANG, MANNHEIM MODULAR und
            RHEINPULS AUDIO. Der zum Eröffnungsstichtag geführte Gesamtsaldo beträgt
            nach unserem Forderungskonto 222.974 Euro. Die beigefügte neutrale
            Saldenstaffel weist wegen der streitigen Zahlungen und abweichender
            Zinsbuchungen niedrigere Kontrollszenarien aus. Wir behaupten deshalb nicht,
            dass der Buchsaldo bereits abgestimmt ist; eine erhebliche unbezahlte
            Hauptforderung besteht in sämtlichen Szenarien.

            Wir widersprechen vorsorglich jeder Verfügung oder Belastung der Marken
            ohne unsere vorherige ausdrückliche schriftliche Zustimmung. Das gilt auch
            für eine Veräußerung zusammen mit anderen Vermögensgegenständen. Eine
            Teilnahme an Gesprächen oder die Mitteilung einer Preisvorstellung ist keine
            Freigabe. Registerumschreibungen sind bislang nicht veranlasst worden.

            Für eine abgestimmte Gesamtlösung stehen wir zur Verfügung. Bitte übersenden
            Sie uns vor einer Entscheidung das Vermarktungskonzept, die Bewertung und
            eingehende Angebote. Wegen der kurzfristigen Fortführung bitten wir um
            direkte Kommunikation mit beiden Unterzeichnern unserer Geschäftsführung.

            Freundliche Grüße
            Pauline Roth
            """,
            attachments=(
                "04_Sicherungsuebertragung_Marken_15-02-2024.pdf",
                "07A_Kreditkonto_und_Saldenstaffel.xlsx",
                "13_Forderungskauf_18-08-2025.pdf",
                "13A_Zessionsvollzug_und_Kaufpreisbeleg_25-08-2025.pdf",
                "15_Forderungskonto_Rebenpfad.xlsx",
                "16A_Sicherungsfall_und_Verwertungsankuendigung_04-03-2026.pdf",
            ),
        ),
        _mail(
            "22_Antwort_Insolvenzverwalterin_07-09.eml",
            "Antwort der Insolvenzverwalterin zur Sicherheitenanzeige",
            "Dr. Helena Aydin <insolvenz@aydin-partner.example>",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>",
            "Tarek Mansour <tarek.mansour@rebenpfad-sicherheiten.example>; projekt-kurpfalz@aydin-partner.example",
            "2026-09-07T16:21:00+02:00",
            "AW: 8 IN 233/26 – Markenrechte und Darlehen KT-2024-021",
            """
            Sehr geehrte Frau Roth,

            wir haben Ihre Anzeige erhalten und die behauptete Sicherungsübertragung im
            Datenraum kenntlich gemacht. Die Rechtskette und der Umfang, insbesondere
            hinsichtlich RHEINPULS AUDIO, werden noch geprüft. Auch die von der
            Schuldnerin vorgelegten Zahlungsbelege sind in die Abstimmung einzubeziehen.

            Der Geschäftsbetrieb wird derzeit im Rahmen einer Investorenlösung
            vermarktet. Wir wollen die Marken wegen ihrer Verbindung mit Vorräten,
            Produktunterlagen, Domains und Kundenbeziehungen in einem Paket anbieten.
            Vor einer Übertragung der Marken werden wir erneut mit Ihnen Rücksprache
            halten. Die Aufnahme Ihrer Unterlagen in den Datenraum oder Gespräche über
            einen Erlösverteilungsschlüssel bedeuten keine Anerkennung der angemeldeten
            Rechtsposition.

            Mit freundlichen Grüßen
            Dr. Helena Aydin
            Insolvenzverwalterin
            """,
            attachments=(),
        ),
        _document(
            "23_Bewertung_Markenportfolio_Zeichenwert.pdf",
            "pdf",
            "Bewertung des Markenportfolios durch Zeichenwert Partnerschaft",
            sections=[
                _section(
                    "1. Auftrag und Bewertungsstichtag",
                    """
                    Dr. Mira Yilmaz wurde von der vorläufigen Insolvenzverwalterin am
                    10. August 2026 beauftragt, eine indikative Bandbreite für die drei
                    registrierten Marken zu ermitteln. Bewertungsstichtag ist der
                    31. Juli 2026. Die Bewertung dient der Vorbereitung eines
                    Investorenprozesses und ist kein Rechtsgutachten zum Eigentum oder
                    zu Belastungen.
                    """,
                ),
                _section(
                    "2. Unterlagen und Annahmen",
                    """
                    Verwendet wurden Umsatzlisten 2023 bis Juni 2026, Marketingbudgets,
                    Registerabschriften, der Hainblick-Vertrag und eine vorläufige
                    Sicherheitenliste. Vollständige Rohdaten zur Deckungsbeitragsrechnung
                    lagen nicht vor. Für die Ertragswertbetrachtung wird angenommen,
                    dass die Zeichen mit den Produktunterlagen und Vertriebskanälen
                    weitergenutzt werden können.
                    """,
                    """
                    Die Sachverständige weist darauf hin, dass eine isolierte Verwertung
                    ohne Domains, Gestaltungen und Warenbestand voraussichtlich einen
                    deutlichen Abschlag auslöst. Die Reichweite des Gebietsschutzes von
                    Hainblick konnte nicht abschließend geklärt werden. Das Risiko wurde
                    pauschal mit einem Bandbreitenabschlag berücksichtigt.
                    """,
                ),
                _section(
                    "3. Ergebnisse",
                    """
                    Für eine Nutzung im fortgeführten Geschäft wird ein Gesamtwert der
                    drei Marken von 410.000 bis 560.000 Euro abgeleitet. Bei isolierter
                    Verwertung unter Zeitdruck wird eine Bandbreite von 145.000 bis
                    235.000 Euro angesetzt. KURPFALZKLANG trägt den größten Anteil wegen
                    der Umsätze und der Bekanntheit im regionalen Fachhandel.
                    """,
                    tables=[
                        _table(
                            ["Zeichen", "Fortführungswert EUR", "isolierter Wert EUR", "wesentliche Unsicherheit"],
                            [
                                ["KURPFALZKLANG", "230.000–300.000", "80.000–120.000", "Umsatzabgrenzung"],
                                ["MANNHEIM MODULAR", "120.000–170.000", "45.000–75.000", "Hainblick-Lizenz"],
                                ["RHEINPULS AUDIO", "60.000–90.000", "20.000–40.000", "kurze Benutzungshistorie"],
                            ],
                        )
                    ],
                ),
                _section(
                    "4. Sensitivität und Grenzen",
                    """
                    Die obere Bandbreite setzt eine zeitnahe Fortführung und
                    kontinuierliche Lieferfähigkeit voraus. Bei Verlust der Domain
                    rheinpuls-audio.example oder einer exklusiven Bindung wesentlicher
                    Händler sinkt der angenommene Wert. Das Gutachten bewertet weder die
                    Wirksamkeit der Sicherungsübertragung noch die Befugnis einer
                    bestimmten Person zur Veräußerung.
                    """,
                ),
            ],
        ),
        _document(
            "24_Bieterprozess_Informationsmemorandum.pdf",
            "pdf",
            "Informationsmemorandum und Verfahrensbrief für den Bieterprozess",
            sections=[
                _section(
                    "1. Transaktionsgegenstand",
                    """
                    Angeboten werden die für eine Fortführung des Audiogeschäfts
                    erforderlichen Vermögensgegenstände der Kurpfalz Tonwerke GmbH. Dazu
                    zählen Maschinen, Vorräte, ausgewählte Verträge, Produktunterlagen,
                    Domains und die registrierten Marken KURPFALZKLANG, MANNHEIM
                    MODULAR und RHEINPULS AUDIO. Ein Erwerb von Geschäftsanteilen ist
                    nicht vorgesehen.
                    """,
                ),
                _section(
                    "2. Verfahren und Termine",
                    """
                    Interessenbekundungen waren bis zum 8. September 2026 einzureichen.
                    Verbindliche Angebote werden bis zum 25. September 2026, 12:00 Uhr,
                    erbeten. Managementgespräche finden zwischen dem 14. und 18.
                    September statt. Als angestrebter Unterzeichnungstermin wird der
                    16. Oktober, als mögliches Closing der Zeitraum 23. bis 30. Oktober
                    2026 genannt.
                    """,
                ),
                _section(
                    "3. Sicherheiten und Lizenz",
                    """
                    Rebenpfad Sicherheiten GmbH behauptet Rechte aus einer
                    Sicherungsübertragung. Diese Behauptung und die wesentlichen
                    Urkunden sind im Datenraum unter 4.3 offengelegt. Die
                    Insolvenzverwaltung führt Gespräche über eine abgestimmte
                    Verwertung. Bieter sollen ihr Angebot sowohl als Gesamtpreis als
                    auch mit einer nachvollziehbaren Allokation auf Marken, sonstiges IP,
                    Vorräte und Anlagevermögen abgeben.
                    """,
                    """
                    Für MANNHEIM MODULAR ist ein Vertriebs- und Lizenzvertrag mit
                    Hainblick Audiohandel e.K. offengelegt. Der Vertrag bezeichnet die
                    Lizenz als nicht ausschließlich; eine ergänzende E-Mail kann als
                    weitergehender Gebietsschutz verstanden werden. Die Erwerberin soll
                    angeben, ob sie den Vertrag übernehmen oder eine andere Regelung
                    anstreben will.
                    """,
                ),
                _section(
                    "4. Vorbehalte",
                    """
                    Das Memorandum begründet keinen Anspruch auf Abschluss eines
                    Vertrags. Die Insolvenzverwaltung kann das Verfahren ändern,
                    Verhandlungen mit einzelnen Interessenten führen oder das Verfahren
                    beenden. Rechtliche und wirtschaftliche Prüfungen bleiben den
                    Bietern überlassen; verbindlich sind ausschließlich die Regelungen
                    eines unterzeichneten Kaufvertrags.
                    """,
                ),
            ],
        ),
        _xlsx(
            "25_Datenraum_QA_und_Zugriffe.xlsx",
            "Fragen- und Zugriffsprotokoll des Transaktionsdatenraums",
            [
                _sheet(
                    "Q_and_A",
                    ["Nr.", "Datum", "Bieter", "Frage", "Antwort Insolvenzverwaltung", "Status"],
                    [
                        [1, "11.09.2026", "Schwetzinger Resonanz GmbH", "Wer ist materiell Inhaber der drei Marken?", "Register nennt Schuldnerin; Rebenpfad behauptet Sicherungsübertragung. Urkunden in 4.3.", "beantwortet 12.09."],
                        [2, "11.09.2026", "Schwetzinger Resonanz GmbH", "Ist Zustimmung von Rebenpfad Closing-Bedingung?", "Abstimmung läuft; Vertragsentwurf regelt Vollzugsrisiko.", "teilweise beantwortet"],
                        [3, "15.09.2026", "Audioquadrat Betriebsgesellschaft mbH", "Ist Hainblick exklusiver Händler?", "Vertrag sagt nicht ausschließlich; ergänzende Mail offengelegt.", "beantwortet 16.09."],
                        [4, "17.09.2026", "Palatina Markenwerke GmbH", "Kann nur KURPFALZKLANG erworben werden?", "Gesamtangebot bevorzugt; Einzelangebot zulässig.", "beantwortet 18.09."],
                        [5, "22.09.2026", "Schwetzinger Resonanz GmbH", "Wer unterschreibt DPMA- und EUIPO-Umschreibungsformulare?", "Insolvenzverwaltung bereitet Formulare vor; Rebenpfad wird angesprochen.", "beantwortet 23.09."],
                        [6, "24.09.2026", "Schwetzinger Resonanz GmbH", "Besteht ein Unterlassungs- oder Veräußerungsverbot?", "Kein gerichtliches Verbot bekannt; Widerspruch Rebenpfad offengelegt.", "beantwortet 24.09."],
                    ],
                    "Die Antworten geben den Kommunikationsstand im Bieterprozess wieder. Sie ändern die im Datenraum offengelegten Verträge nicht.",
                ),
                _sheet(
                    "Zugriffe_IP_Ordner",
                    ["Unternehmen", "Nutzer", "erster Zugriff", "letzter Zugriff", "Dateien geöffnet", "Downloadpaket"],
                    [
                        ["Schwetzinger Resonanz GmbH", "l.ebert", "09.09.2026 08:41", "19.10.2026 17:03", 37, "4.3 vollständig am 13.09."],
                        ["Audioquadrat Betriebsgesellschaft mbH", "due.diligence", "10.09.2026 12:16", "27.09.2026 10:44", 29, "ohne Kontenblatt"],
                        ["Palatina Markenwerke GmbH", "m.klee", "12.09.2026 09:09", "25.09.2026 09:50", 14, "nur IP-Ordner"],
                    ],
                    "Das Protokoll belegt Dateiöffnungen, nicht die Kenntnisnahme jedes einzelnen Inhalts.",
                ),
                _sheet(
                    "Ordner_4_3",
                    ["Datei", "eingestellt", "Version", "Hinweis im Datenraum"],
                    [
                        ["Sicherungsuebertragung_15-02-2024.pdf", "05.09.2026", "Inhaltsabschrift; Papieroriginal nur im Aktenindex", "keine Signaturabbildungen; Rechtsposition bestritten"],
                        ["Anlage_1_Markenbestand.xlsx", "05.09.2026", "drei Tabellenblätter", "abweichende Registernummer beachten"],
                        ["Forderungskauf_18-08-2025.pdf", "06.09.2026", "vollständig", "RHEINPULS ohne Nummer"],
                        ["Anzeige_Rebenpfad_04-09-2026.pdf", "06.09.2026", "Maildruck", "keine Freigabe erklärt"],
                        ["Hainblick_Vertrag.docx", "08.09.2026", "Vertrag plus Mailausdruck", "Lizenzumfang offen"],
                    ],
                    "Der Sicherheitenhinweis war für alle drei zugelassenen Bieter sichtbar.",
                ),
            ],
        ),
        _document(
            "26_Verbindliches_Angebot_Schwetzinger_Resonanz.pdf",
            "pdf",
            "Verbindliches Angebot der Schwetzinger Resonanz GmbH",
            sections=[
                _section(
                    "1. Angebot und Erwerbsstruktur",
                    """
                    Die Schwetzinger Resonanz GmbH bietet am 25. September 2026 den
                    Erwerb der im Informationsmemorandum bezeichneten Vermögenswerte im
                    Wege eines Asset Deals an. Das Unternehmen plant, Entwicklung,
                    Montage und Vertrieb am Standort Mannheim mit zunächst 18
                    Beschäftigten fortzuführen. Das Angebot ist bis zum 9. Oktober 2026
                    bindend und steht unter dem Vorbehalt eines ausverhandelten
                    Kaufvertrags.
                    """,
                ),
                _section(
                    "2. Kaufpreis",
                    """
                    Der angebotene Barkaufpreis beträgt 960.000 Euro. Davon entfallen
                    nach der Preisallokation der Bieterin 320.000 Euro auf die drei
                    registrierten Marken, 110.000 Euro auf Domains, Produktunterlagen
                    und Gestaltungen, 220.000 Euro auf Vorräte, 180.000 Euro auf
                    Maschinen und 130.000 Euro auf Kundenbeziehungen und sonstigen
                    Geschäftswert.
                    """,
                    """
                    Die Bieterin ist bereit, nach abschließender Bestätigung der
                    übergehenden Vorräte bis zu 20.000 Euro zusätzlich zu zahlen. Eine
                    Anzahlung von zehn Prozent kann binnen zwei Bankarbeitstagen nach
                    Unterzeichnung geleistet werden. Eine Finanzierungsklausel wird
                    nicht verlangt.
                    """,
                ),
                _section(
                    "3. Marken und bekannte Rechte Dritter",
                    """
                    Das Angebot setzt voraus, dass die Bieterin die Zeichen ab Closing
                    für den übernommenen Geschäftsbetrieb nutzen kann. Die Unterlagen
                    zur behaupteten Sicherungsübertragung und zum Hainblick-Vertrag sind
                    geprüft worden. Die Bieterin akzeptiert eine kaufvertragliche
                    Offenlegung dieser Punkte, erwartet aber die Mitwirkung der
                    Insolvenzverwaltung an Registeranträgen und an der Abwehr
                    entgegenstehender Verfügungen.
                    """,
                ),
                _section(
                    "4. Vollzug",
                    """
                    Als Closing-Termin wird der 26. Oktober 2026 vorgeschlagen. Bis dahin
                    sollen Mietzustimmung, Betriebsübergangsinformation und ein
                    abgestimmtes IP-Übertragungsset vorliegen. Eine Zustimmung der
                    Rebenpfad Sicherheiten GmbH wird in der Angebotsfassung als
                    „angestrebte Vollzugsunterlage“ bezeichnet, aber nicht ausdrücklich
                    als Bedingung formuliert.
                    """,
                ),
            ],
        ),
        _xlsx(
            "27_Bietervergleich_und_Erloesallokation.xlsx",
            "Interner Bietervergleich der Insolvenzverwaltung",
            [
                _sheet(
                    "Gesamtangebote",
                    ["Bieter", "Barkaufpreis EUR", "Markenallokation EUR", "Arbeitsplätze", "Bedingungen", "interne Rangfolge"],
                    [
                        ["Schwetzinger Resonanz GmbH", 960000, 320000, 18, "Mietzustimmung; Vertrag; IP-Set", 1],
                        ["Audioquadrat Betriebsgesellschaft mbH", 810000, 285000, 14, "Finanzierung; Markenfreigabe", 2],
                        ["Palatina Markenwerke GmbH", 390000, 390000, 0, "nur drei Marken und zwei Domains", 3],
                    ],
                    "Die Rangfolge berücksichtigt neben dem Preis die Fortführung, Vollzugssicherheit und Abwicklung der übrigen Assets.",
                ),
                _sheet(
                    "Verhandlung_Schwetzingen",
                    ["Position", "Angebot 25.09. EUR", "Einigung 20.10. EUR", "Änderung EUR", "Bemerkung"],
                    [
                        ["Maschinen", 180000, 180000, 0, "unverändert"],
                        ["Vorräte", 220000, 220000, 0, "Bestandskorridor vereinbart"],
                        ["drei Marken", 320000, 340000, 20000, "Erhöhung im Paket"],
                        ["sonstiges IP", 110000, 120000, 10000, "Domains und Unterlagen"],
                        ["Goodwill/Auftragsbestand", 130000, 120000, -10000, "Umverteilung"],
                        ["Gesamt", 960000, 980000, 20000, "finaler Festkaufpreis"],
                    ],
                    "Die Allokation wurde für Abrechnung und interne Erlöszuordnung verhandelt. Sie ist keine Einzelbewertung der Rechte.",
                ),
                _sheet(
                    "Abzuege_Arbeitspapier",
                    ["Position", "Basis EUR", "Satz", "Rechnerischer Betrag EUR", "Status"],
                    [
                        ["Feststellungskosten Marken", 340000, "4 %", 13600, "nur Szenario"],
                        ["Verwertungskosten Marken", 340000, "5 %", 17000, "streitig/offen"],
                        ["Gutachten anteilig", 340000, "pauschal", 9500, "Rechnung vorhanden"],
                        ["Netto vor Forderung", 340000, "", 299900, "keine Auszahlungsfreigabe"],
                    ],
                    "Dieses Blatt enthält eine interne Modellrechnung. Es dokumentiert weder die rechtliche Zulässigkeit einzelner Abzüge noch eine Einigung mit Rebenpfad.",
                ),
            ],
        ),
        _document(
            "28_Protokoll_Glaeubigerausschuss_30-09-2026.pdf",
            "pdf",
            "Protokoll der Sitzung des vorläufigen Gläubigerausschusses",
            sections=[
                _section(
                    "1. Sitzung und Teilnehmende",
                    """
                    Der vorläufige Gläubigerausschuss tagt am 30. September 2026 von
                    14:00 bis 15:35 Uhr in Mannheim. Anwesend sind die drei
                    Ausschussmitglieder, Dr. Helena Aydin, ihr Projektleiter Moritz
                    Kern und die M&A-Beraterin Hanne Riedel. Rebenpfad und die Bieter
                    nehmen nicht teil.
                    """,
                ),
                _section(
                    "2. Bericht zum Bieterprozess",
                    """
                    Die Insolvenzverwalterin stellt drei Angebote vor. Das Angebot aus
                    Schwetzingen weist den höchsten Gesamtpreis und die größte Zahl
                    übernommener Arbeitsplätze auf. Der IP-Einzelbieter bietet für Marken
                    und zwei Domains 390.000 Euro, übernimmt aber weder Personal noch
                    Vorräte. Die Bewertung sieht im Fortführungsfall für die Marken eine
                    Bandbreite von 410.000 bis 560.000 Euro.
                    """,
                ),
                _section(
                    "3. Sicherungsrechte",
                    """
                    Dr. Aydin berichtet, Rebenpfad beanspruche die drei Marken. Zwei
                    deutsche Marken seien in den Sicherheitenurkunden eindeutig genannt;
                    bei der späteren Unionsmarke bestehe zusätzlicher Klärungsbedarf.
                    Rebenpfad habe einer Veräußerung nicht zugestimmt, aber Bereitschaft
                    zu einer wirtschaftlichen Abstimmung signalisiert. Der Ausschuss
                    erörtert, dass jeder Vertragsentwurf die Rechtsbehauptung offenlegen
                    müsse.
                    """,
                ),
                _section(
                    "4. Beschluss",
                    """
                    Der Ausschuss stimmt einstimmig der Fortführung der Verhandlungen mit
                    der Schwetzinger Resonanz GmbH auf Grundlage eines Kaufpreises von
                    mindestens 960.000 Euro zu. Die Insolvenzverwalterin darf den Vertrag
                    nach abschließender Prüfung und bei wirtschaftlich mindestens
                    gleichwertigen Bedingungen unterzeichnen. Der Beschluss enthält
                    keine Erklärung im Namen von Rebenpfad und keine gesonderte
                    Feststellung der Verfügungsbefugnis über die Marken.
                    """,
                ),
            ],
        ),
        _mail(
            "29_Preiskorridor_aber_keine_Freigabe.eml",
            "Korrespondenz über Preisuntergrenze und fehlende Freigabe",
            "Tarek Mansour <tarek.mansour@rebenpfad-sicherheiten.example>",
            "Dr. Helena Aydin <insolvenz@aydin-partner.example>",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>; Moritz Kern <moritz.kern@aydin-partner.example>",
            "2026-10-02T12:37:00+02:00",
            "Markenpaket – wirtschaftlicher Korridor",
            """
            Sehr geehrte Frau Dr. Aydin,

            nach Durchsicht des Gutachtens erscheint uns für die drei Marken eine
            Allokation unter 325.000 Euro im Gesamtpaket wirtschaftlich nicht
            vertretbar. Wenn ein belastbares Gesamtangebot diesen Betrag erreicht und
            der offene Darlehenssaldo sowie die Abzüge transparent abgestimmt werden,
            können wir kurzfristig über eine Freigabe gegen Zahlung sprechen.

            Diese Mitteilung ist weder eine Zustimmung zu einem bestimmten Angebot noch
            eine Freigabe oder Genehmigung einer Verfügung. Dafür benötigen wir die
            vollständige Vertragsfassung, die endgültige Allokation und eine
            schriftliche Vereinbarung über Vollzug und Erlös. Unser Schreiben vom
            4. September bleibt bestehen.

            Die von Ihnen genannte Zahlung von 15.000 Euro an Neckarbrücke prüfen wir
            intern. Eine Kontenabstimmung darf den Verkaufsprozess nicht verdecken, ist
            aber vor einer Erlösabrechnung erforderlich.

            Mit freundlichen Grüßen
            Tarek Mansour
            """,
            attachments=("23_Bewertung_Markenportfolio_Zeichenwert.pdf",),
        ),
        _document(
            "30_Unterzeichneter_Asset_Purchase_Agreement.pdf",
            "pdf",
            "Unterzeichneter Asset Purchase Agreement vom 20. Oktober 2026",
            sections=[
                _section(
                    "1. Parteien und Hintergrund",
                    """
                    Verkäuferin ist Dr. Helena Aydin ausschließlich in ihrer Eigenschaft
                    als Insolvenzverwalterin über das Vermögen der Kurpfalz Tonwerke
                    GmbH. Käuferin ist die Schwetzinger Resonanz GmbH, vertreten durch
                    ihre Geschäftsführerin Lina Ebert. Der Vertrag nimmt auf das am
                    1. September 2026 eröffnete Insolvenzverfahren und den seit August
                    geführten Bieterprozess Bezug.
                    """,
                    """
                    Die Käuferin will den Audiogeschäftsbetrieb mit wesentlichen
                    Vermögensgegenständen fortführen. Die Parteien halten fest, dass
                    Rebenpfad Sicherheiten GmbH Rechte an den Marken beansprucht und
                    einer Übertragung bislang nicht in einer gesonderten Vereinbarung
                    zugestimmt hat. Einzelheiten stehen in Anlage 3.4.
                    """,
                ),
                _section(
                    "2. Kaufgegenstände",
                    """
                    Die Verkäuferin verkauft die in Anlage 2.1 aufgeführten Maschinen,
                    Vorräte, Produktunterlagen, Domains, Social-Media-Konten und
                    registrierten Marken. Zu den Marken gehören KURPFALZKLANG,
                    MANNHEIM MODULAR und RHEINPULS AUDIO mit den in den
                    Registerabschriften bezeichneten Waren und Dienstleistungen.
                    Kundendaten werden nur übertragen, soweit die gesonderten
                    Voraussetzungen des Übertragungskonzepts erfüllt sind.
                    """,
                    """
                    Nicht übertragen werden Bankguthaben, Steuererstattungsansprüche,
                    Forderungen aus Lieferungen vor Closing und Ansprüche gegen Organe.
                    Die Domain rheinpuls-audio.example wird wegen des abweichenden
                    Providerkontos nur nach erfolgreicher Mitwirkung von Marlene Vogt
                    übertragen; der Festkaufpreis wird bei einem Scheitern nicht
                    automatisch reduziert.
                    """,
                ),
                _section(
                    "3. Übertragung der Marken",
                    """
                    Die Verkäuferin überträgt die Marken mit wirtschaftlicher Wirkung
                    zum Closing auf die Käuferin, soweit ihr eine Verfügung hierüber
                    möglich ist. Die Käuferin nimmt die Übertragung an. Die
                    Verkäuferin unterzeichnet die als Anlage 3.1 beigefügten
                    Registerformulare und wird weitere zumutbare Erklärungen abgeben.
                    Die Käuferin kann Umschreibungsanträge nach Closing einreichen.
                    """,
                    """
                    Der Vertrag verpflichtet die Verkäuferin, bis zum Closing erneut
                    eine Mitwirkungserklärung von Rebenpfad anzufordern. Das Ausbleiben
                    dieser Erklärung ist nach Ziffer 8 keine aufschiebende Bedingung.
                    Eine Freistellung wegen der Rechtsbehauptung von Rebenpfad wird
                    nicht gewährt. Die Käuferin behält ihre im Vertrag ausdrücklich
                    geregelten Rechte bei Nichterfüllung einzelner Übergabepflichten.
                    """,
                ),
                _section(
                    "4. Übernommene Verträge und Hainblick",
                    """
                    Der Vertriebs- und Lizenzvertrag mit Hainblick Audiohandel e.K. wird
                    der Käuferin als zu übernehmender Vertrag angeboten. Die
                    Verkäuferin wird Hainblick über den Betriebsübergang informieren.
                    Soweit eine Zustimmung zur Vertragsübernahme erforderlich ist,
                    führen Verkäuferin und Käuferin die Vertragsbeziehung bis zur
                    Entscheidung im Innenverhältnis nach dem im Vertrag beschriebenen
                    Abrechnungsmodell fort.
                    """,
                    """
                    Die Parteien kennen die E-Mail vom 15. Januar 2024 zur behaupteten
                    Exklusivität in Nordbaden. Die Verkäuferin übernimmt keine Gewähr
                    dafür, dass der gedruckte Vertrag oder die E-Mail den Umfang der
                    Rechte abschließend wiedergibt.
                    """,
                ),
                _section(
                    "5. Kaufpreis und Allokation",
                    """
                    Der Festkaufpreis beträgt 980.000 Euro. Eine Anzahlung von 98.000
                    Euro wird binnen eines Bankarbeitstages auf das Treuhandkonto der
                    Insolvenzverwaltung gezahlt. Der Restbetrag von 882.000 Euro muss
                    spätestens am Closing-Tag unwiderruflich gutgeschrieben sein. Die
                    Kaufpreisallokation dient der internen und steuerlichen Zuordnung;
                    sie enthält keine Garantie eines Einzelwerts.
                    """,
                    tables=[
                        _table(
                            ["Vermögensgruppe", "Allokation EUR"],
                            [
                                ["Maschinen und Betriebsausstattung", 180000],
                                ["Vorräte", 220000],
                                ["KURPFALZKLANG, MANNHEIM MODULAR, RHEINPULS AUDIO", 340000],
                                ["Domains, Produktunterlagen und sonstiges IP", 120000],
                                ["Goodwill und Auftragsbestand", 120000],
                                ["Gesamt", 980000],
                            ],
                        )
                    ],
                ),
                _section(
                    "6. Beschaffenheitsvereinbarungen und Haftung",
                    """
                    Die Vermögensgegenstände werden in ihrem Zustand am Closing
                    erworben. Die Verkäuferin erklärt, dass ihr außer den in Anlage 3.4
                    bezeichneten Rechten keine weiteren konkreten Verfügungen über die
                    Marken bekannt sind. Eine Garantie unbelasteten Rechtserwerbs wird
                    nicht übernommen. Vorsatz, ausdrücklich übernommene Pflichten und
                    Ansprüche wegen Verletzung von Leben, Körper oder Gesundheit bleiben
                    von den Haftungsbegrenzungen unberührt.
                    """,
                ),
                _section(
                    "7. Handlungen bis zum Closing",
                    """
                    Die Verkäuferin führt den Betrieb im bisherigen Umfang fort und
                    nimmt ohne Zustimmung der Käuferin keine außergewöhnlichen
                    Verfügungen über die Kaufgegenstände vor. Sie informiert Rebenpfad
                    über Unterzeichnung und Termin, fordert eine Mitwirkungserklärung an
                    und leitet eine eingehende Antwort an die Käuferin weiter. Die
                    Käuferin bereitet Registeranträge vor, reicht sie aber vor Closing
                    nicht ein.
                    """,
                ),
                _section(
                    "8. Closing",
                    """
                    Das Closing findet am 26. Oktober 2026 um 10:00 Uhr in den Räumen
                    der Insolvenzverwaltung oder per Videokonferenz statt. Bedingungen
                    sind die vollständige Kaufpreiszahlung, die Zustimmung des
                    Vermieters zur Nutzungsüberlassung und das Ausbleiben einer
                    vollziehbaren behördlichen oder gerichtlichen Untersagung. Eine
                    Zustimmung oder Freigabe von Rebenpfad ist nicht als Bedingung
                    aufgeführt.
                    """,
                    """
                    Beim Closing werden Übergabeprotokoll, Schlüssel, Datenraumexport,
                    Domaincodes und die von der Verkäuferin unterzeichneten
                    Registerformulare übergeben. Nutzen und Lasten gehen nach
                    Feststellung des Vollzugs um 10:15 Uhr auf die Käuferin über. Die
                    Käuferin darf ab diesem Zeitpunkt den übernommenen Marktauftritt
                    verwenden, vorbehaltlich der offengelegten Rechte Dritter.
                    """,
                ),
                _section(
                    "9. Rücktritt und Vollzugsstörungen",
                    """
                    Ist eine Closing-Bedingung bis zum 30. Oktober 2026 nicht erfüllt,
                    kann jede Partei nach Maßgabe des Vertrags zurücktreten, sofern sie
                    die Nichterfüllung nicht überwiegend verursacht hat. Das bloße
                    Ausbleiben einer Registerumschreibung am Closing-Tag berechtigt
                    nicht zum Rücktritt. Bei einer gerichtlichen Untersagung der
                    Markenübertragung führen die Parteien innerhalb von fünf
                    Bankarbeitstagen Gespräche über eine Anpassung; eine automatische
                    Kaufpreisminderung ist nicht festgelegt.
                    """,
                ),
                _section(
                    "10. Mitteilungen, Recht und Unterschriften",
                    """
                    Mitteilungen erfolgen an die im Vertrag genannten
                    Transaktionsadressen. Es gilt deutsches Recht. Gerichtsstand ist,
                    soweit zulässig, Mannheim. Die PDF-Fassung enthält auf Seite 38 die
                    qualifizierten elektronischen Signaturvermerke von Dr. Helena Aydin
                    am 20. Oktober 2026 um 17:42 Uhr und Lina Ebert am selben Tag um
                    18:06 Uhr. Der Signaturbericht bezeichnet das Dokument als
                    unverändert seit Abschluss der zweiten Signatur.
                    """,
                ),
                _section(
                    "11. Anlage 3.4 – offengelegte Rechtsbehauptungen",
                    """
                    Anlage 3.4 gibt die Sicherungsabrede vom 15. Februar 2024, den
                    Forderungskauf vom 18. August 2025, die Anzeige von Rebenpfad vom
                    4. September 2026 und die E-Mail zum Preiskorridor vom 2. Oktober
                    2026 wieder. Daneben werden der Hainblick-Vertrag und die E-Mail zur
                    Exklusivität aufgeführt. Die Anlage hält fest, dass zwischen
                    Insolvenzverwaltung und Rebenpfad keine Freigabe- oder
                    Erlösvereinbarung unterzeichnet ist.
                    """,
                ),
            ],
        ),
        _xlsx(
            "31_Closing_Checkliste_Stand_22-10-2026.xlsx",
            "Closing-Checkliste der Insolvenzverwaltung",
            [
                _sheet(
                    "Bedingungen",
                    ["Nr.", "Punkt", "Verantwortlich", "Fällig", "Status 22.10.", "Nachweis"],
                    [
                        [1, "Anzahlung 98.000 EUR", "Käuferin", "21.10.2026", "erfüllt", "Treuhandkonto 21.10. 11:08"],
                        [2, "Restkaufpreis 882.000 EUR", "Käuferin", "26.10.2026 09:30", "Bankavis angekündigt", "noch kein Geldeingang"],
                        [3, "Vermieterzustimmung", "Insolvenzverwaltung", "23.10.2026", "Entwurf abgestimmt", "Original fehlt"],
                        [4, "keine vollziehbare Untersagung", "beide Parteien", "26.10.2026", "derzeit keine bekannt", "Abfrage vor Closing"],
                    ],
                    "Nur die in Ziffer 8 APA genannten Punkte werden in diesem Blatt als Bedingungen geführt.",
                ),
                _sheet(
                    "IP_Uebergabe",
                    ["Dokument oder Zugang", "Unterzeichner/Quelle", "Status", "Übergabezeitpunkt", "Bemerkung"],
                    [
                        ["DPMA-Antrag KURPFALZKLANG", "Dr. Aydin", "unterzeichnet", "Closing", "Rebenpfad-Signaturfeld leer"],
                        ["DPMA-Antrag MANNHEIM MODULAR", "Dr. Aydin", "unterzeichnet", "Closing", "Lizenzanzeige beifügen"],
                        ["EUIPO-Übertragungsantrag RHEINPULS AUDIO", "Dr. Aydin", "unterzeichnet", "Closing", "Vollmacht Käuferin offen"],
                        ["Mitwirkungserklärung Rebenpfad", "Rebenpfad", "nicht eingegangen", "erwünscht vor Closing", "keine Closing-Bedingung"],
                        ["Domaincode kurpfalzklang.example", "IT Insolvenzverwaltung", "vorhanden", "Closing", "versiegelter Export"],
                        ["Domain rheinpuls-audio.example", "Marlene Vogt", "Zustimmung per Mail zugesagt", "nach Closing möglich", "abweichendes Providerkonto"],
                        ["Marken- und Designarchiv", "IT Insolvenzverwaltung", "Export erstellt", "Closing", "Prüfsumme im Übergabeprotokoll"],
                    ],
                    "Die Liste beschreibt den operativen Vorbereitungsstand. Sie enthält keine Feststellung, welche Unterschrift für einen Rechtsübergang genügt.",
                ),
                _sheet(
                    "Kommunikation",
                    ["Adressat", "Mitteilung", "Versand geplant", "Status", "Vorlage"],
                    [
                        ["Rebenpfad", "Unterzeichnung und Closing", "22.10.2026", "gesendet 16:18", "Mail 32"],
                        ["Hainblick", "Betriebsübergang/Vertragskontakt", "26.10.2026 10:30", "vorbereitet", "Entwurf H-4"],
                        ["Beschäftigte", "Vollzugsinformation", "26.10.2026 10:20", "vorbereitet", "Entwurf P-2"],
                        ["Presse/Fachhandel", "Fortführung", "26.10.2026 11:00", "Käuferin verantwortet", "Entwurf nicht im Datenraum"],
                    ],
                    "Versandzeiten nach dem Closing sind Planwerte und keine Zugangsbelege.",
                ),
            ],
        ),
        _mail(
            "32_Mitteilung_Verwertung_und_Closing.eml",
            "Mitteilung der Insolvenzverwalterin über Unterzeichnung und Closing",
            "Dr. Helena Aydin <insolvenz@aydin-partner.example>",
            "Pauline Roth <pauline.roth@rebenpfad-sicherheiten.example>; Tarek Mansour <tarek.mansour@rebenpfad-sicherheiten.example>",
            "Moritz Kern <moritz.kern@aydin-partner.example>",
            "2026-10-22T16:18:00+02:00",
            "8 IN 233/26 – Verwertung des Geschäftsbetriebs und Closing am 26.10.2026",
            """
            Sehr geehrte Frau Roth, sehr geehrter Herr Mansour,

            wir teilen Ihnen mit, dass wir den Asset Purchase Agreement mit der
            Schwetzinger Resonanz GmbH am 20. Oktober 2026 unterzeichnet haben. Der
            Festkaufpreis beträgt 980.000 Euro; hiervon sind im Vertrag 340.000 Euro den
            drei registrierten Marken zugeordnet. Das Closing ist für Montag, den
            26. Oktober 2026, 10:00 Uhr, vorgesehen. Die Anzahlung ist eingegangen.

            Ihre Rechtsbehauptung, die Sicherungsvereinbarung und Ihre Erklärung vom
            2. Oktober sind im Vertrag offengelegt. Nach unserer Auffassung kann die
            Transaktion in der vereinbarten Form vollzogen werden. Unabhängig davon
            halten wir eine Mitwirkungs- und Erlösvereinbarung weiterhin für sinnvoll.
            Eine vorbereitete Mitwirkungserklärung liegt bei; sie sieht eine Verwahrung
            des auf die Marken entfallenden Nettoerlöses bis zur Saldenabstimmung vor.

            Falls Sie die Erklärung unterzeichnen, benötigen wir sie bis Freitag,
            23. Oktober 2026, 14:00 Uhr. Der Closing-Termin bleibt nach dem Vertrag auch
            bei Ausbleiben der Erklärung bestehen. Die Registerformulare sind von mir
            unterzeichnet und werden beim Closing an die Käuferin übergeben.

            Mit freundlichen Grüßen
            Dr. Helena Aydin
            """,
            attachments=(
                "30_Unterzeichneter_Asset_Purchase_Agreement.pdf",
                "31_Closing_Checkliste_Stand_22-10-2026.xlsx",
            ),
        ),
        _mail(
            "33_Interne_Mail_Erwerberin_Geschafft.eml",
            "Interne E-Mail der Erwerberin nach Vertragsunterzeichnung",
            "Lina Ebert <lina.ebert@schwetzinger-resonanz.example>",
            "Projektteam Resonanz <projektteam@schwetzinger-resonanz.example>",
            "geschaeftsfuehrung@schwetzinger-resonanz.example",
            "2026-10-20T19:24:00+02:00",
            "Geschafft – Kurpfalzklang kommt zu uns",
            """
            Liebes Projektteam,

            beide Signaturen sind drauf. Nach den intensiven Wochen dürfen wir uns
            heute freuen: Am Montag übernehmen wir Betrieb, Vorräte und die drei Marken.
            Die 98.000 Euro Anzahlung gehen morgen früh raus. Für 10:15 Uhr nach dem
            Closing könnt ihr die neue Startseite und die Händlernachricht vorbereiten.

            Helena hat erläutert, dass Rebenpfad weiter über die Sicherung und den Erlös
            diskutiert. Das ist im Vertrag offengelegt und soll das Closing nicht
            verschieben. Die Registerformulare bekommen wir von der Verwalterin. Bitte
            trotzdem keine Formulierung verwenden, wonach ein Register die Umschreibung
            schon bestätigt hätte.

            Für Hainblick bleibt der bestehende Vertrieb zunächst bestehen. Das Team
            Recht klärt anschließend, ob die Mail von 2024 mehr als den gedruckten
            Vertrag verspricht. Bis dahin gehen keine neuen Händlerzusagen für
            Nordbaden heraus.

            Danke an alle – das war ein Kraftakt.
            Lina
            """,
            attachments=(),
        ),
        _document(
            "34_Gespraechsvermerk_23-10-2026.docx",
            "docx",
            "Gesprächsvermerk zur Videokonferenz am 23. Oktober 2026",
            sections=[
                _section(
                    "1. Teilnehmende und Anlass",
                    """
                    Die Videokonferenz beginnt am 23. Oktober 2026 um 09:05 Uhr und
                    endet um 09:42 Uhr. Für Rebenpfad nehmen Pauline Roth und Tarek
                    Mansour teil. Für die Insolvenzverwaltung nehmen Dr. Helena Aydin
                    und Moritz Kern teil. Anlass ist die am Vorabend übersandte
                    Mitteilung über den unterzeichneten Asset Purchase Agreement und das
                    für Montag angekündigte Closing.
                    """,
                ),
                _section(
                    "2. Erklärungen von Rebenpfad",
                    """
                    Pauline Roth erklärt, Rebenpfad habe weder die Marken freigegeben
                    noch der Veräußerung zugestimmt. Die E-Mail vom 2. Oktober habe nur
                    einen wirtschaftlichen Gesprächskorridor genannt. Rebenpfad könne
                    die beigefügte Mitwirkungserklärung nicht unterzeichnen, solange
                    Saldo, Rechtsumfang, Abzüge und Verwahrungsmechanik nicht abgestimmt
                    seien.
                    """,
                    """
                    Tarek Mansour fragt, wann die endgültige Vertragsfassung entstanden
                    sei und weshalb die in der Nachricht vom 7. September angekündigte
                    Rücksprache erst nach der Unterzeichnung erfolge. Er verweist auf die
                    Zahlung von 15.000 Euro und erklärt, deren Behandlung müsse getrennt
                    von der Frage einer Freigabe geklärt werden.
                    """,
                ),
                _section(
                    "3. Erklärungen der Insolvenzverwaltung",
                    """
                    Dr. Aydin erklärt, das Gesamtangebot sei für Masse, Beschäftigte und
                    Fortführung wirtschaftlich überlegen. Der Vertrag lege die
                    Rechtsbehauptung von Rebenpfad offen und mache deren gesonderte
                    Zustimmung nicht zur Closing-Bedingung. Sie hält an dem für Montag
                    geplanten Vollzug fest. Der auf die Marken allokierte Betrag werde
                    zunächst auf dem Verfahrenskonto identifizierbar gehalten; eine
                    endgültige Erlösabrechnung sei noch nicht erstellt.
                    """,
                    """
                    Moritz Kern bestätigt, dass die Käuferin die Formulare nach Closing
                    einreichen dürfe. Eine Übermittlung der finalen APA-Fassung an
                    Rebenpfad vor Unterzeichnung sei nicht erfolgt. Er sagt zu, den
                    Signaturbericht und die aktuelle Bestätigung über die Anzahlung noch
                    am Vormittag zu übersenden.
                    """,
                ),
                _section(
                    "4. Ergebnis des Gesprächs",
                    """
                    Eine Mitwirkungs-, Freigabe- oder Erlösvereinbarung kommt in der
                    Videokonferenz nicht zustande. Rebenpfad hält an ihrer Erklärung
                    fehlender Zustimmung fest. Die Insolvenzverwaltung hält am
                    Closing-Termin fest. Die Beteiligten vereinbaren keinen weiteren
                    Gesprächstermin; Dr. Aydin bleibt nach eigener Aussage am Freitag
                    bis 18:00 Uhr erreichbar.
                    """,
                    """
                    Der Vermerk wird um 10:18 Uhr von Pauline Roth aus ihren Notizen
                    erstellt. Eine von allen Teilnehmenden gebilligte Niederschrift liegt
                    nicht vor. Die Aufzeichnung der Videokonferenz war deaktiviert.
                    """,
                ),
            ],
        ),
    ],
}
