"""Falldaten: Software-IP, Kreditsicherheiten und Asset Deal in der Insolvenz.

Die Datei enthält ausschließlich Eingangs- und Originalunterlagen. Sie bewertet weder
die Wirksamkeit einzelner Klauseln noch die Rang- oder Verfügungsfragen.
"""

from __future__ import annotations

from typing import Any


def _section(title: str, *paragraphs: str) -> dict[str, Any]:
    return {"heading": title, "paragraphs": list(paragraphs)}


def _doc(
    path: str,
    kind: str,
    title: str,
    *,
    paragraphs: list[str] | None = None,
    sections: list[dict[str, Any]] | None = None,
    tables: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"path": path, "kind": kind, "title": title}
    if paragraphs:
        item["paragraphs"] = paragraphs
    if sections:
        decimal_sections: list[dict[str, Any]] = []
        for index, section in enumerate(sections, start=1):
            normalized = dict(section)
            raw_title = str(normalized.get("heading", "")).strip()
            if raw_title.startswith("§ "):
                title_parts = raw_title.split(" ", 2)
                raw_title = title_parts[2] if len(title_parts) == 3 else raw_title[2:]
            first_token = raw_title.split(" ", 1)[0] if raw_title else ""
            if first_token.endswith(".") and first_token[:-1].isdigit():
                raw_title = raw_title.split(" ", 1)[1] if " " in raw_title else ""
            raw_title = f"{index}. {raw_title}"
            normalized["heading"] = raw_title
            decimal_sections.append(normalized)
        item["sections"] = decimal_sections
    if tables:
        item["tables"] = tables
    return item


def _mail(
    path: str,
    title: str,
    *,
    sender: str,
    to: list[str],
    date: str,
    subject: str,
    body: str,
    cc: list[str] | None = None,
    attachments: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "path": path,
        "kind": "eml",
        "title": title,
        "from": sender,
        "to": to,
        "cc": cc or [],
        "date": date,
        "subject": subject,
        "body": body,
        "attachments": attachments or [],
    }


def _xlsx(path: str, title: str, sheets: list[dict[str, Any]]) -> dict[str, Any]:
    return {"path": path, "kind": "xlsx", "title": title, "sheets": sheets}


def _csv(
    path: str,
    title: str,
    headers: list[str],
    rows: list[list[Any]],
) -> dict[str, Any]:
    return {
        "path": path,
        "kind": "csv",
        "title": title,
        "headers": headers,
        "rows": rows,
        "tables": [{"title": title, "headers": headers, "rows": rows}],
    }


def _employment_contract(
    *,
    path: str,
    employee: str,
    address: str,
    role: str,
    contract_date: str,
    start_date: str,
    annual_salary: str,
    monthly_salary: str,
    workplace: str,
    probation: str,
    notice: str,
    ip_clause: str,
    side_activity_clause: str,
    preexisting_clause: str,
    oss_clause: str,
    employee_sign_date: str,
    employer_signatory: str,
) -> dict[str, Any]:
    return _doc(
        path,
        "docx",
        f"Arbeitsvertrag {employee}",
        sections=[
            _section(
                "Arbeitsvertrag und Vertragsparteien",
                f"Zwischen der Kurpfalz Taxware GmbH, Im Neuenheimer Feld 583, 69120 Heidelberg, vertreten durch die Geschäftsführung, nachfolgend Arbeitgeberin, und {employee}, {address}, nachfolgend Arbeitnehmerin oder Arbeitnehmer, wird am {contract_date} folgender Arbeitsvertrag geschlossen.",
                "Die Parteien halten alle Abreden in diesem Vertrag und seinen ausdrücklich bezeichneten Anlagen fest. Mündliche Nebenabreden bestehen bei Unterzeichnung nicht.",
            ),
            _section(
                "1. Beginn, Dauer und Probezeit",
                f"Das Arbeitsverhältnis beginnt am {start_date} und wird auf unbestimmte Zeit geschlossen. {probation}",
                "Eine ordentliche Kündigung vor dem vereinbarten Beginn ist ausgeschlossen. Das Recht zur außerordentlichen Kündigung aus wichtigem Grund bleibt unberührt.",
            ),
            _section(
                "2. Tätigkeit und organisatorische Zuordnung",
                f"Die Beschäftigung erfolgt als {role}. Zum Aufgabenbereich gehören Konzeption, Entwicklung, Dokumentation, Review, Fehleranalyse und Pflege der im Zuständigkeitsbereich liegenden Bestandteile der Produkte FiscusPilot Kanzlei und FiscusPilot Mittelstand.",
                "Die Arbeitnehmerin oder der Arbeitnehmer berichtet fachlich an die Leitung Engineering und organisatorisch an die Geschäftsführung. Eine andere gleichwertige, den Kenntnissen und Fähigkeiten entsprechende Aufgabe kann unter Wahrung billigen Ermessens zugewiesen werden.",
            ),
            _section(
                "3. Arbeitsort und mobiles Arbeiten",
                f"Regelmäßiger Arbeitsort ist {workplace}. Mobiles Arbeiten innerhalb Deutschlands ist nach der jeweils geltenden betrieblichen Regelung und nach Abstimmung im Team möglich.",
                "Dienstreisen zu Kunden, Rechenzentren und betrieblichen Veranstaltungen sind im zumutbaren Umfang Bestandteil der Tätigkeit. Ein dauerhafter Wechsel des Arbeitsorts bedarf einer Vereinbarung in Textform.",
            ),
            _section(
                "4. Arbeitszeit",
                "Die regelmäßige Arbeitszeit beträgt 40 Stunden pro Woche ausschließlich der Ruhepausen und wird grundsätzlich auf Montag bis Freitag verteilt. Beginn und Ende richten sich nach der betrieblichen Gleitzeitregelung und den Erfordernissen des Teams.",
                "Notwendige Mehrarbeit ist nur auf Anordnung oder mit vorheriger Genehmigung zu leisten. Bis zu zehn Mehrarbeitsstunden im Kalendermonat sind mit der Vergütung abgegolten, soweit dies gesetzlich zulässig ist; darüber hinausgehende Stunden werden durch Freizeit ausgeglichen oder vergütet.",
            ),
            _section(
                "5. Vergütung",
                f"Die jährliche Bruttovergütung beträgt {annual_salary}; dies entspricht einer monatlichen Bruttovergütung von {monthly_salary}, zahlbar jeweils zum letzten Bankarbeitstag des Monats auf ein benanntes Konto.",
                "Freiwillige Sonderzahlungen, Boni oder Sachleistungen begründen auch bei wiederholter Gewährung keinen Anspruch für die Zukunft, sofern sie nicht in einer gesonderten Zielvereinbarung verbindlich zugesagt sind.",
            ),
            _section(
                "6. Urlaub und Arbeitsverhinderung",
                "Der jährliche Erholungsurlaub beträgt 30 Arbeitstage bei einer Fünftagewoche. Zuerst wird der gesetzliche Urlaub, anschließend der vertragliche Mehrurlaub eingebracht. Urlaub ist unter Berücksichtigung betrieblicher Belange frühzeitig abzustimmen.",
                "Arbeitsunfähigkeit ist unverzüglich samt voraussichtlicher Dauer mitzuteilen. Die gesetzlichen Nachweis- und Fortzahlungspflichten gelten; die Arbeitgeberin kann einen ärztlichen Nachweis ab dem ersten Krankheitstag verlangen.",
            ),
            _section(
                "7. Vertraulichkeit, Datenschutz und IT-Sicherheit",
                "Über Geschäfts- und Betriebsgeheimnisse, Quellcode, nicht veröffentlichte Produktpläne, Sicherheitsbefunde, Kundendaten, Steuerdaten und Vertragskonditionen ist während und nach dem Arbeitsverhältnis Stillschweigen zu bewahren. Die Pflicht gilt nicht für offenkundige Informationen oder gesetzlich zulässige Meldungen.",
                "Zugänge sind personenbezogen zu verwenden. Quellcode und Produktdaten dürfen nur in freigegebenen Repositorien und Systemen gespeichert werden. Sicherheitsvorfälle, versehentliche Veröffentlichungen und der Verlust von Zugangsmitteln sind unverzüglich an die Leitung Engineering und die Datenschutzkoordination zu melden.",
            ),
            _section(
                "8. Arbeitsergebnisse und Nutzungsrechte",
                ip_clause,
                "Für Computerprogramme nehmen die Parteien ergänzend auf § 69b UrhG Bezug. Soweit dieser Vertrag konkrete weitergehende Nutzungsbefugnisse beschreibt, gelten sie im Rahmen des gesetzlich Zulässigen.",
                "Urheberpersönlichkeitsrechte bleiben unberührt. Soweit eine gesonderte Mitwirkung für Anmeldung, Dokumentation oder Übertragung erforderlich ist, wird sie auf angemessene Anforderung geleistet; notwendige Auslagen trägt die Arbeitgeberin.",
            ),
            _section(
                "9. Vorbestehende Werke, Werkzeuge und Kenntnisse",
                preexisting_clause,
                "Allgemeine berufliche Kenntnisse, Erfahrungen, Methoden und nicht geheimhaltungsbedürftige Fähigkeiten werden durch diese Regelung nicht erfasst. Eine Einbringung weiterer vorbestehender Software bedarf einer vorherigen Dokumentation in Textform.",
            ),
            _section(
                "10. Open Source und Drittsoftware",
                oss_clause,
                "Für jede eingebrachte Drittkomponente sind mindestens Name, Version, Bezugsquelle, Lizenzkennung und der Einsatzort im Repository zu dokumentieren. Lizenztexte und Copyright-Hinweise dürfen nicht entfernt werden.",
            ),
            _section(
                "11. Nebentätigkeiten",
                side_activity_clause,
                "Gesetzliche Arbeitszeitgrenzen, berechtigte Geheimhaltungsinteressen und Wettbewerbsverbote sind auch bei einer gestatteten Nebentätigkeit einzuhalten. Änderungen des Umfangs oder Inhalts sind erneut anzuzeigen.",
            ),
            _section(
                "12. Diensterfindungen und Verbesserungsvorschläge",
                "Für Erfindungen und technische Verbesserungsvorschläge gilt das Arbeitnehmererfindungsgesetz. Meldungen sind unverzüglich in einer Weise einzureichen, die Aufgabe, Entstehung und beteiligte Personen erkennen lässt.",
            ),
            _section(
                "13. Arbeitsmittel und Rückgabe",
                "Überlassene Geräte, Schlüssel, Token, Unterlagen und Datenträger bleiben Eigentum der Arbeitgeberin. Spätestens bei Ende des Arbeitsverhältnisses sind sie vollständig zurückzugeben; betriebliche Daten auf privaten Systemen sind nach abgestimmter Übergabe zu löschen.",
                "Ein Zurückbehaltungsrecht an Quellcode, Zugangsdaten, Dokumentationen oder Kundendaten ist ausgeschlossen, soweit gesetzlich zulässig.",
            ),
            _section(
                "14. Kündigung und Freistellung",
                notice,
                "Kündigungen bedürfen der gesetzlichen Schriftform. Die Arbeitgeberin kann nach Ausspruch einer Kündigung unter Fortzahlung der Vergütung und Anrechnung offener Urlaubs- und Freizeitausgleichsansprüche freistellen, soweit berechtigte Interessen dies tragen.",
            ),
            _section(
                "15. Ausschlussfrist",
                "Ansprüche aus dem Arbeitsverhältnis sind innerhalb von drei Monaten nach Fälligkeit in Textform geltend zu machen und, wenn die Gegenseite sie ablehnt oder sich nicht binnen zwei Wochen erklärt, binnen weiterer drei Monate gerichtlich geltend zu machen. Die Klausel gilt nicht für gesetzlich unverzichtbare Ansprüche, Mindestlohn, Vorsatz oder Schäden an Leben, Körper oder Gesundheit.",
            ),
            _section(
                "16. Schlussbestimmungen",
                "Änderungen und Ergänzungen dieses Vertrags sollen in Textform festgehalten werden, soweit nicht gesetzlich eine strengere Form gilt. Individuelle Abreden bleiben unberührt.",
                "Sollte eine Bestimmung unwirksam sein oder werden, bleibt der Vertrag im Übrigen bestehen. Die Parteien werden die unwirksame Regelung durch eine zulässige Regelung ersetzen, die dem dokumentierten wirtschaftlichen Zweck möglichst nahekommt.",
            ),
            _section(
                "Unterschriften",
                f"Heidelberg, {contract_date} — Kurpfalz Taxware GmbH, {employer_signatory}, handschriftlich unterzeichnet.",
                f"Heidelberg, {employee_sign_date} — {employee}, handschriftlich unterzeichnet. Jede Partei bestätigt den Erhalt einer gegengezeichneten Ausfertigung.",
            ),
        ],
    )


def _customer_license(
    *,
    path: str,
    title: str,
    customer: str,
    customer_address: str,
    contract_date: str,
    product: str,
    users: str,
    term: str,
    fee: str,
    deployment: str,
    transfer_clause: str,
    special_clause: str,
    customer_signatory: str,
    vendor_signatory: str,
) -> dict[str, Any]:
    return _doc(
        path,
        "docx",
        title,
        sections=[
            _section(
                "Vertragsparteien und Gegenstand",
                f"Zwischen der Kurpfalz Taxware GmbH, Im Neuenheimer Feld 583, 69120 Heidelberg, und {customer}, {customer_address}, wird am {contract_date} dieser Softwarelizenz- und Pflegevertrag geschlossen.",
                f"Vertragsgegenstand ist {product} für {users}. Bereitstellungsmodell: {deployment}. Funktionsbeschreibungen und Systemvoraussetzungen ergeben sich aus Anlage 1.",
            ),
            _section(
                "1. Nutzungsumfang",
                "Die Kundin erhält für die Vertragsdauer ein einfaches, nicht ausschließliches Recht, die Software im vereinbarten Umfang für eigene interne Geschäfts- und Beratungszwecke zu nutzen. Eine Bearbeitung ist nur für vertragsgemäße Konfigurationen und gesetzlich zwingend gestattete Handlungen zulässig.",
                "Vervielfältigungen sind nur als technisch erforderliche Installations-, Arbeits- und Sicherungskopien zulässig. Copyright-, Lizenz- und Herkunftsvermerke sind beizubehalten.",
            ),
            _section(
                "2. Zugänge und Verantwortlichkeiten",
                "Zugänge sind natürlichen Personen zuzuordnen und vor Zugriffen Dritter zu schützen. Die Kundin sorgt für aktuelle Endgeräte, Browser und lokale Sicherungsabläufe, soweit das Bereitstellungsmodell dies verlangt.",
                "Die Anbieterin dokumentiert wesentliche Änderungen, stellt Release-Hinweise bereit und unterhält während der Servicezeiten einen Supportkanal.",
            ),
            _section(
                "3. Vergütung",
                f"Die vereinbarte Vergütung beträgt {fee}. Rechnungen sind 14 Tage nach Zugang ohne Abzug fällig. Reise- und Fremdkosten werden nur nach vorheriger Freigabe gesondert berechnet.",
            ),
            _section(
                "4. Laufzeit und Kündigung",
                term,
                "Das Recht zur Kündigung aus wichtigem Grund bleibt bestehen. Kündigungen bedürfen mindestens der Textform. Bei Vertragsende werden Exporte in den dokumentierten Standardformaten bereitgestellt, soweit sie vom gewählten Modul unterstützt werden.",
            ),
            _section(
                "5. Übertragung und Vertragswechsel",
                transfer_clause,
            ),
            _section(
                "6. Pflege und Verfügbarkeit",
                "Pflege umfasst Fehlerkorrekturen, gesetzlich veranlasste Regelupdates im vereinbarten Modul und reguläre Releases. Eine bestimmte steuerliche oder wirtschaftliche Entscheidung wird durch die Software nicht geschuldet.",
                "Geplante Wartungen sollen fünf Werktage vorher angekündigt werden. Zeiten höherer Gewalt, kundenseitiger Störungen und angekündigter Wartung werden bei der Verfügbarkeitsmessung nach Anlage 2 behandelt.",
            ),
            _section(
                "7. Datenschutz und Vertraulichkeit",
                "Die Parteien behandeln vertrauliche Unterlagen und Zugangsdaten geheim. Soweit die Anbieterin personenbezogene Daten im Auftrag verarbeitet, gilt die gesonderte Vereinbarung zur Auftragsverarbeitung einschließlich der dort benannten Unterauftragnehmer.",
            ),
            _section(
                "8. Besondere Vereinbarung",
                special_clause,
            ),
            _section(
                "9. Haftung und Mängel",
                "Die gesetzlichen Mängelrechte gelten mit der Maßgabe, dass die Kundin reproduzierbare Fehler samt Umgebung und Arbeitsschritten meldet. Bei leichter Fahrlässigkeit haftet die Anbieterin nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den vertragstypisch vorhersehbaren Schaden; zwingende Haftung bleibt unberührt.",
            ),
            _section(
                "10. Schlussbestimmungen und Unterschriften",
                "Änderungen dieses Vertrags bedürfen der Textform, soweit keine strengere Form gesetzlich vorgeschrieben ist. Es gilt deutsches Recht. Anlagen 1 bis 3 sind Vertragsbestandteil.",
                f"Heidelberg, {contract_date} — Kurpfalz Taxware GmbH, {vendor_signatory}, handschriftlich unterzeichnet.",
                f"{customer.split(',')[0]}, {contract_date} — {customer_signatory}, handschriftlich unterzeichnet.",
            ),
        ],
    )


CASE: dict[str, Any] = {
    "slug": "kurpfalz-taxware-software-ip-insolvenz",
    "title": "FiscusPilot zwischen Kreditsicherheit und Insolvenzverkauf",
    "short_title": "FiscusPilot – Software-IP in der Insolvenz",
    "plugin": "fachanwalt-urheber-medienrecht",
    "summary": (
        "Die Rhenus Kreditbank AG finanzierte die Heidelberger Kurpfalz Taxware GmbH. "
        "Nutzungsrechte an der Steuersoftware FiscusPilot wurden der Bank zur Sicherheit "
        "eingeräumt; Lizenzforderungen wurden in einer späteren Urkunde gesondert "
        "sicherungsabgetreten. Nach Eröffnung des Insolvenzverfahrens hat die Verwalterin "
        "einen Asset Purchase Agreement mit der Weinberg Digital Solutions GmbH aus "
        "Deidesheim unterzeichnet und den kurzfristigen Vollzug angekündigt."
    ),
    "scenario": (
        "Die Sicherheitennehmerin erhält am 22. Oktober 2026 erstmals die nahezu vollständige "
        "Produkt- und Dealakte. Fünf unterschiedlich gefasste Arbeitsverträge, ein früher "
        "Freelancer-Beitrag, uneinheitliche Open-Source-Dokumentation, kundenbezogene "
        "Übertragungsklauseln und getrennte Sicherheitenurkunden erschweren die tatsächliche "
        "Rechtezuordnung. Der Insolvenzverwalter kündigt Closing für den 28. Oktober an; die "
        "Erwerberin teilt bereits ihre Vorfreude auf Produkt und Team mit. Die Bank benötigt "
        "eine belastbare Prüfung ihrer Rechtsposition und der verfügbaren Handlungsoptionen."
    ),
    "parties": [
        {
            "name": "Rhenus Kreditbank AG",
            "role": "Sicherheitennehmerin und Darlehensgeberin",
            "address": "Augustaanlage 33, 68165 Mannheim",
            "email": "workout@rhenus-kreditbank.example",
        },
        {
            "name": "Kurpfalz Taxware GmbH",
            "role": "Insolvenzschuldnerin und Softwareanbieterin",
            "address": "Im Neuenheimer Feld 583, 69120 Heidelberg",
            "email": "office@kurpfalz-taxware.example",
        },
        {
            "name": "Dr. Friederike Mohn",
            "role": "Insolvenzverwalterin über das Vermögen der Kurpfalz Taxware GmbH",
            "address": "Kanzlei Mohn & Partner, Friedrich-Ebert-Anlage 22, 69117 Heidelberg",
            "email": "mohn@insolvenzkanzlei-mohn.example",
        },
        {
            "name": "Weinberg Digital Solutions GmbH",
            "role": "Unterzeichnete Erwerberin des operativen Softwaregeschäfts",
            "address": "Weinstraße 61, 67146 Deidesheim",
            "email": "transaktion@weinberg-digital.example",
        },
        {
            "name": "Silke Brandt",
            "role": "Leiterin Restrukturierung der Rhenus Kreditbank AG",
            "address": "Augustaanlage 33, 68165 Mannheim",
            "email": "silke.brandt@rhenus-kreditbank.example",
        },
        {
            "name": "Martin Reuter",
            "role": "Ehemaliger Geschäftsführer der Kurpfalz Taxware GmbH",
            "address": "Bergheimer Straße 126, 69115 Heidelberg",
            "email": "martin.reuter@kurpfalz-taxware.example",
        },
        {
            "name": "Dr. Lena Vogt",
            "role": "Senior Backend Engineer und frühere technische Leiterin",
            "address": "Ladenburger Straße 18, 69120 Heidelberg",
            "email": "lena.vogt@kurpfalz-taxware.example",
        },
        {
            "name": "Lukas Binder",
            "role": "Ehemaliger freier Entwickler des Altmoduls TaxEngine Classic",
            "address": "Carl-Theodor-Straße 9, 68723 Schwetzingen",
            "email": "lukas@binder-software.example",
        },
        {
            "name": "Müller & Reiter Steuerberatung PartG mbB",
            "role": "Kanzleikundin mit On-Premise-Lizenz und Escrow-Nachtrag",
            "address": "Sofienstraße 12, 69115 Heidelberg",
            "email": "it@mueller-reiter.example",
        },
        {
            "name": "PfalzForm Maschinenbau GmbH",
            "role": "Mittelstandskundin mit Cloud-Abonnement",
            "address": "Floßwörthstraße 48, 68199 Mannheim",
            "email": "finanzen@pfalzform.example",
        },
    ],
    "questions": [
        "Welche urheberrechtlichen Nutzungsrechte und sonstigen Softwarepositionen lassen sich für jedes Repository und jedes Release lückenlos von Beschäftigten, Freelancern und Drittkomponenten herleiten?",
        "Welchen sachlichen und zeitlichen Umfang haben die der Bank eingeräumten Sicherheiten, und welche Rechte, Versionen, Dokumentationen, Kennzeichen und Nebenrechte werden von den Urkunden und Anlagen tatsächlich erfasst?",
        "Wie verhalten sich die Sicherung der Software-Nutzungsrechte und die gesonderte Sicherungsabtretung von Lizenzforderungen zueinander, insbesondere bei Zahlungen vor und nach Verfahrenseröffnung?",
        "Welche insolvenzrechtlichen Positionen und Verfahrensschritte kommen für die Bank angesichts des bereits unterzeichneten APA und des angekündigten Closings in Betracht?",
        "Welche Bestimmungen des APA setzen die Verfügungsbefugnis, Freigaben, Zustimmungen oder die Übertragbarkeit von Kundenverträgen voraus, und welche Vollzugsunterlagen fehlen noch?",
        "Welche Kundenverträge können nach ihrem Wortlaut übergeleitet werden, welche Zustimmungen oder Mitteilungen sind vorgesehen und welche Forderungen sind dem verkauften Geschäft wirtschaftlich zugeordnet?",
        "Welche Bedeutung haben der Freelancer-Vorbestand BinderRules, private Vorarbeiten einzelner Beschäftigter und die dokumentierten Open-Source-Komponenten für die angebotene Rechtekette?",
        "Welche Tatsachen und Originalnachweise müssen vor dem 28. Oktober 2026 gesichert oder bei Verwalterin, Erwerberin, Beschäftigten, Kunden und technischen Dienstleistern angefordert werden?",
        "Welche kurzfristigen und welche verhandlungsorientierten Handlungsoptionen hat die Bank, ohne die rechtliche oder wirtschaftliche Bewertung vorwegzunehmen?",
    ],
    "ambiguities": [
        "Die Anlage zum Sicherungsvertrag nennt FiscusPilot 3.x und Nachfolgeversionen, während mehrere produktive Repositories historische Namen und eigenständige Module tragen.",
        "Das Altmodul BinderRules wurde vor Gründung einzelner Repositories entwickelt; Vertrag, Vorbestandsanlage, Rechnung und spätere E-Mail verwenden unterschiedliche Modulbezeichnungen.",
        "Bei zwei Beschäftigten werden private Vorarbeiten erwähnt; nicht alle referenzierten Anlagen liegen unterschrieben oder in derselben Fassung vor.",
        "Der Open-Source-Scan nennt eine AGPL-Komponente im Repository, während die technische Notiz ihren Einsatz auf eine interne Build-Umgebung beschränkt sieht.",
        "Die Bank erhielt nach Aktenlage nicht von allen Kunden bestätigte Abtretungsanzeigen; mehrere Debitoren zahlten weiterhin auf das operative Konto der Schuldnerin.",
        "Die Forderungsmatrix unterscheidet wiederkehrende Lizenzentgelte, Pflege, Projektleistungen und Gutschriften, ohne jede Position eindeutig einem Vertrag zuzuordnen.",
        "Ein Kundenvertrag verlangt vorherige schriftliche Zustimmung zum Vertragsübergang, ein anderer enthält nur eine Informationspflicht und ein dritter einen Escrow-Mechanismus.",
        "Der APA verkauft Software, Dokumentation, Domains, Kundenbeziehungen und ausgewählte Forderungen, verwendet aber bei einzelnen Positionen die Einschränkung 'soweit übertragbar und verfügbar'.",
        "Die Verwalterin hat der Bank den unterschriebenen APA erst nach Signing übersandt; aus den Unterlagen geht nicht hervor, wann und mit welchem Inhalt die Erwerberin die Sicherheitenurkunden gesehen hat.",
        "Die Bewertung setzt uneingeschränkte Fortführung der wesentlichen Kundenverträge und Verfügbarkeit des Entwicklungsteams voraus; dokumentierte Zustimmungen liegen nur teilweise vor.",
        "Die Closing-Checkliste führt eine Bankfreigabe als 'nicht erforderlich laut Verkäuferseite', während die technische Datenraumliste eine Freigabe noch als offen markiert.",
        "Nicht abschließend geklärt ist, welche Quellcode-Kopien, Signaturschlüssel, Build-Artefakte und Cloud-Zugänge am angekündigten Vollzugstag tatsächlich übergeben werden sollen.",
    ],
    "documents": [],
}


CASE["documents"].extend(
    [
        _mail(
            "01_Mandat/01_Anfrage_Rhenusbank.eml",
            "Mandatsanfrage der Rhenus Kreditbank",
            sender="Silke Brandt <silke.brandt@rhenus-kreditbank.example>",
            to=["ip-team@kanzlei-kornmarkt.example"],
            cc=["vorstandsstab@rhenus-kreditbank.example"],
            date="Thu, 22 Oct 2026 08:17:00 +0200",
            subject="Eilig: FiscusPilot / Sicherheiten und angekündigtes Closing am 28.10.",
            body=(
                "Guten Morgen,\n\nunsere Kreditnehmerin Kurpfalz Taxware GmbH befindet sich seit "
                "15. September im eröffneten Insolvenzverfahren. Wir halten eine Urkunde über "
                "die Sicherung von Software-Nutzungsrechten aus 2023 und eine gesonderte "
                "Sicherungsabtretung der Lizenzforderungen aus 2024. Frau Dr. Mohn hat uns gestern "
                "den bereits beiderseits unterschriebenen Asset Purchase Agreement mit Weinberg "
                "Digital Solutions übersandt. Vollzug soll am Mittwoch, 28. Oktober, erfolgen.\n\n"
                "Bitte prüfen Sie anhand der beigefügten Akte, welche Rechtsposition wir tatsächlich "
                "haben, welche Unterlagen noch fehlen und welche kurzfristigen Handlungsoptionen "
                "bestehen. Uns ist besonders wichtig, dass Software-Rechte und Forderungen getrennt "
                "betrachtet werden. Wir benötigen zunächst eine belastbare Tatsachen- und Fragenliste; "
                "eine abschließende Stellungnahme ist noch nicht beauftragt.\n\n"
                "Mit freundlichen Grüßen\nSilke Brandt\nLeiterin Restrukturierung"
            ),
            attachments=[
                "05_Finanzierung_Sicherheiten/02_Sicherungsvertrag_IP.docx",
                "05_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx",
                "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx",
                "06_Insolvenz_AssetDeal/06_Mail_Verwalter_Vollzug.eml",
            ],
        ),
        _doc(
            "01_Mandat/02_Fallnotiz_Sachstand.docx",
            "docx",
            "Interne Fallnotiz der Bank zum Sachstand",
            sections=[
                _section(
                    "Anlass und Auftrag",
                    "Bearbeiterin: Silke Brandt, Restrukturierung. Stand der Notiz: 22. Oktober 2026, 07:30 Uhr. Die Notiz bündelt den bislang bekannten tatsächlichen Ablauf und ersetzt keine rechtliche Prüfung.",
                    "Die Bank möchte bis spätestens 26. Oktober eine geordnete Rechte- und Dokumentenmatrix, eine Liste der ungeklärten Tatsachen und einen Überblick über mögliche nächste Schritte erhalten.",
                ),
                _section(
                    "Kredit und Sicherheiten",
                    "Die Bank gewährte der Kurpfalz Taxware GmbH im März 2023 ein Investitionsdarlehen über 2.400.000 EUR. Die Valuta diente laut Verwendungsnachweis der Cloud-Migration, der Entwicklung des Mittelstandsmoduls und dem Vertriebsausbau.",
                    "Zeitgleich wurde ein Sicherungsvertrag zu Software-Nutzungsrechten unterzeichnet. Im Februar 2024 folgte eine separate Globalzession gegenwärtiger und künftiger Forderungen aus Softwarelizenz, Pflege und Support. Der operative Zahlungsverkehr lief weiterhin über Konten der Schuldnerin.",
                ),
                _section(
                    "Insolvenz und Verwertung",
                    "Am 15. September 2026 eröffnete das Amtsgericht Heidelberg das Insolvenzverfahren und bestellte Dr. Friederike Mohn zur Insolvenzverwalterin. Am 21. Oktober ging bei der Bank eine E-Mail mit einem am 19. Oktober unterzeichneten APA ein.",
                    "Die Verwalterin kündigt den Vollzug zum 28. Oktober an. Die Bank war weder an den Vertragsverhandlungen beteiligt noch hat sie nach dem internen Posteingang bislang eine Freigabe- oder Verzichtserklärung abgegeben.",
                ),
                _section(
                    "Technische Hinweise aus dem ersten Datenraumabruf",
                    "Die Produktfamilie wird teils als FiscusPilot, teils als TaxEngine, KanzleiCloud oder LedgerFlow bezeichnet. Die Repository-Liste umfasst sechs aktive und zwei archivierte Projekte. Ein Freelancer-Vertrag aus 2017 und fünf Arbeitsverträge liegen vor.",
                    "Ein automatisierter Lizenzscan vom 7. Oktober markiert drei Komponenten zur manuellen Prüfung. Die Bank hat keinen eigenen Zugriff auf Quellcode oder Build-Systeme; vorliegend sind Exportlisten und PDF-Auszüge.",
                ),
            ],
        ),
        _xlsx(
            "01_Mandat/03_Chronologie.xlsx",
            "Chronologie Finanzierung, Entwicklung und Insolvenz",
            [
                {
                    "name": "Chronologie",
                    "headers": ["Datum", "Ereignis", "Beteiligte", "Beleg", "Offener Punkt"],
                    "rows": [
                        ["14.06.2017", "Freelancer-Rahmenvertrag TaxEngine Classic", "Kurpfalz Taxware / Lukas Binder", "03_Personal_Rechtekette/08_Freelancer_Rahmenvertrag_Lukas_Binder.docx", "Anlage 2 in welcher Fassung?"],
                        ["01.04.2019", "Arbeitsbeginn Lena Vogt", "Kurpfalz Taxware / Vogt", "03_Personal_Rechtekette/01_Arbeitsvertrag_Lena_Vogt.docx", "TaxParse-Stand bei Einbringung"],
                        ["01.08.2020", "Arbeitsbeginn Jonas Eberle", "Kurpfalz Taxware / Eberle", "03_Personal_Rechtekette/02_Arbeitsvertrag_Jonas_Eberle.docx", "FormKit-Repository"],
                        ["15.02.2021", "Arbeitsbeginn Esra Kaya", "Kurpfalz Taxware / Kaya", "03_Personal_Rechtekette/03_Arbeitsvertrag_Esra_Kaya.docx", "keiner"],
                        ["01.11.2022", "Arbeitsbeginn Marek Nowak", "Kurpfalz Taxware / Nowak", "03_Personal_Rechtekette/04_Arbeitsvertrag_Marek_Nowak.docx", "LedgerLens-Schnittstelle"],
                        ["15.03.2023", "Darlehen und IP-Sicherungsvertrag", "Rhenusbank / Kurpfalz Taxware", "05_Finanzierung_Sicherheiten/01_Darlehensvertrag_Rhenusbank.pdf", "Register- und Repository-Bezug"],
                        ["01.02.2024", "Sicherungsabtretung Lizenzforderungen", "Rhenusbank / Kurpfalz Taxware", "05_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx", "Kundenanzeigen"],
                        ["01.05.2024", "Arbeitsbeginn Nina Scholl", "Kurpfalz Taxware / Scholl", "03_Personal_Rechtekette/05_Arbeitsvertrag_Nina_Scholl.docx", "ReceiptCam-Anlage"],
                        ["11.08.2026", "Zahlungsstockung und Stillhaltebitte", "Kurpfalz Taxware / Rhenusbank", "05_Finanzierung_Sicherheiten/19_Mahnung_Stillhaltebitte_und_Bankantwort.pdf", "insolvenzrechtliche Wirkung der erbetenen Stillhaltung"],
                        ["19.08.2026", "Kündigung, Fälligstellung und Verwertungsanzeige", "Rhenusbank / Kurpfalz Taxware / vorläufige Verwalterin", "05_Finanzierung_Sicherheiten/20_Kuendigung_Faelligstellung_Verwertungsanzeige.pdf", "Durchsetzung und Erlöszuordnung bleiben rechtlich zu prüfen"],
                        ["15.09.2026", "Eröffnung Insolvenzverfahren", "AG Heidelberg / Dr. Mohn", "06_Insolvenz_AssetDeal/01_Insolvenzeroeffnungsbeschluss_AG_Heidelberg.pdf", "Rechtskraftvermerk"],
                        ["07.10.2026", "Open-Source-Scan exportiert", "Verwalterteam / CodeAudit Süd", "02_Unternehmen_Produkt/06_SBOM_Open_Source.xlsx", "AGPL-Treffer"],
                        ["12.10.2026", "Bewertung abgeschlossen", "Bergstraße Advisory", "06_Insolvenz_AssetDeal/03_Bewertung_Software_und_Vertraege.pdf", "Annahmen zur Rechtekette"],
                        ["19.10.2026", "APA beiderseits unterzeichnet", "Dr. Mohn / Weinberg Digital", "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx", "Vollzugsvoraussetzungen"],
                        ["21.10.2026", "APA an Bank übersandt", "Dr. Mohn / Rhenusbank", "06_Insolvenz_AssetDeal/06_Mail_Verwalter_Vollzug.eml", "Zeitpunkt Datenraumzugang"],
                        ["28.10.2026", "angekündigtes Closing", "Verwalterin / Erwerberin", "06_Insolvenz_AssetDeal/05_Closing_Checkliste.xlsx", "Übergabe und Freigaben"],
                    ],
                },
                {
                    "name": "Fristen_und_Termine",
                    "headers": ["Termin", "Uhrzeit", "Vorgang", "Quelle", "Verantwortlich"],
                    "rows": [
                        ["23.10.2026", "16:00", "Datenraumfragen der Bank bündeln", "Mandatsmail", "Kanzlei / Bank"],
                        ["26.10.2026", "12:00", "Besprechung Bank und externe Beratung", "Kalendereintrag", "Silke Brandt"],
                        ["27.10.2026", "10:00", "Closing Call laut Checkliste", "APA-Checkliste", "Verwalterin / Erwerberin"],
                        ["28.10.2026", "09:00", "technische Übergabe beginnt", "Verwaltermail", "Engineering Leads"],
                        ["28.10.2026", "14:00", "Kaufpreiszahlung und Closing-Bestätigung vorgesehen", "APA", "Parteien des APA"],
                    ],
                },
            ],
        ),
        _xlsx(
            "01_Mandat/04_Beteiligte_und_Kontakte.xlsx",
            "Beteiligten- und Kontaktliste",
            [
                {
                    "name": "Beteiligte",
                    "headers": ["Organisation", "Person", "Rolle", "Ort", "E-Mail", "Letzter Kontakt"],
                    "rows": [
                        ["Rhenus Kreditbank AG", "Silke Brandt", "Leitung Restrukturierung", "Mannheim", "silke.brandt@rhenus-kreditbank.example", "22.10.2026"],
                        ["Kurpfalz Taxware GmbH", "Martin Reuter", "ehemaliger Geschäftsführer", "Heidelberg", "martin.reuter@kurpfalz-taxware.example", "18.09.2026"],
                        ["Mohn & Partner", "Dr. Friederike Mohn", "Insolvenzverwalterin", "Heidelberg", "mohn@insolvenzkanzlei-mohn.example", "21.10.2026"],
                        ["Weinberg Digital Solutions GmbH", "Leonhard Kern", "Geschäftsführer Erwerberin", "Deidesheim", "kern@weinberg-digital.example", "21.10.2026"],
                        ["Kurpfalz Taxware GmbH", "Dr. Lena Vogt", "Senior Backend / technische Koordination", "Heidelberg", "lena.vogt@kurpfalz-taxware.example", "20.10.2026"],
                        ["Binder Software", "Lukas Binder", "früherer Freelancer", "Schwetzingen", "lukas@binder-software.example", "08.10.2026"],
                        ["Bergstraße Advisory GmbH", "Dipl.-Kfm. Arvid Seitz", "Bewerter", "Mannheim", "seitz@bergstrasse-advisory.example", "12.10.2026"],
                        ["CodeAudit Süd GmbH", "Meike Lorenz", "Open-Source-Scan", "Heidelberg", "lorenz@codeaudit-sued.example", "07.10.2026"],
                    ],
                },
                {
                    "name": "Kommunikationswege",
                    "headers": ["Thema", "Primärkontakt", "Stellvertretung", "Kanal", "Hinweis"],
                    "rows": [
                        ["Sicherheitenunterlagen", "Silke Brandt", "Jan Küster", "verschlüsselter Datenraum", "keine Weitergabe an Erwerberin ohne Abstimmung"],
                        ["Insolvenzakte", "Dr. Friederike Mohn", "RA Carlotta Frey", "Mohn-Datenraum", "Fragenliste gesammelt senden"],
                        ["Quellcode/Build", "Dr. Lena Vogt", "Esra Kaya", "GitLab Export", "produktiver Zugriff nur über Verwalterteam"],
                        ["Kundenverträge", "Nora Schenk", "Marek Nowak", "ERP Export", "mehrere Scans ohne Anlagen"],
                        ["Closing", "Carlotta Frey", "Leonhard Kern", "Videokonferenz", "Termin 27.10., 10:00 Uhr"],
                    ],
                },
            ],
        ),
    ]
)


CASE["documents"].extend(
    [
        _doc(
            "05_Finanzierung_Sicherheiten/01_Darlehensvertrag_Rhenusbank.pdf",
            "pdf",
            "Investitionsdarlehensvertrag Rhenus Kreditbank",
            sections=[
                _section(
                    "Vertragsparteien und Datum",
                    "Darlehensvertrag Nr. RK-2023-4471 vom 15. März 2023 zwischen der Rhenus Kreditbank AG, Augustaanlage 33, 68165 Mannheim, als Bank und der Kurpfalz Taxware GmbH, Im Neuenheimer Feld 583, 69120 Heidelberg, als Darlehensnehmerin.",
                    "Für die Darlehensnehmerin handelt Geschäftsführer Martin Reuter. Für die Bank handeln die Prokuristinnen Silke Brandt und Beate Abele gemeinschaftlich.",
                ),
                _section(
                    "Darlehensbetrag und Auszahlung",
                    "Die Bank stellt einen Betrag von 2.400.000,00 EUR bereit. Die Auszahlung erfolgt nach Erfüllung der in Anlage 1 bezeichneten Auszahlungsvoraussetzungen in zwei Tranchen auf das Geschäftskonto der Darlehensnehmerin bei der Heidelberger Volksbank.",
                    "Tranche 1 über 1.600.000,00 EUR ist für Cloud-Migration und Entwicklungsleistungen, Tranche 2 über 800.000,00 EUR für Produktlaunch und Vertriebsausbau vorgesehen. Nicht verwendete Beträge sind auf Anforderung zurückzuführen.",
                ),
                _section(
                    "Laufzeit und Tilgung",
                    "Das Darlehen endet am 31. März 2028. Ab dem 30. Juni 2024 sind am Ende jedes Kalenderquartals Tilgungsraten von 50.000,00 EUR zu zahlen; die verbleibende Restschuld wird am Laufzeitende fällig. Freiwillige Sondertilgungen von mindestens 100.000,00 EUR sind mit fünf Bankarbeitstagen Vorankündigung möglich.",
                ),
                _section(
                    "Zinsen und Kosten",
                    "Der Nominalzins beträgt 5,40 Prozent jährlich und ist quartalsweise nachträglich zahlbar. Bei Zahlungsverzug gilt der vertragliche Zinssatz zuzüglich fünf Prozentpunkten, soweit nicht ein niedrigerer Schaden nachgewiesen wird. Ein einmaliges Bearbeitungsentgelt von 18.000,00 EUR ist am Valutatag der ersten Tranche als gesonderte Kontobelastung zu zahlen; es mindert nicht den Kapitalabruf.",
                ),
                _section(
                    "Verwendungsnachweise",
                    "Die Darlehensnehmerin legt quartalsweise eine Mittelverwendungsübersicht mit Rechnungsbelegen für Beträge ab 25.000,00 EUR vor. Abweichungen von mehr als zehn Prozent zwischen den Budgetgruppen bedürfen vorheriger Zustimmung der Bank in Textform.",
                ),
                _section(
                    "Finanzinformationen und Kennzahlen",
                    "Bis 30 Tage nach Quartalsende sind BWA, Summen- und Saldenliste, Liquiditätsstatus und Entwicklung der wiederkehrenden Jahresumsätze einzureichen. Der Mindestbestand liquider Mittel beträgt 350.000,00 EUR; der jährlich wiederkehrende Umsatz soll zum jeweiligen Jahresende mindestens 2.100.000,00 EUR betragen.",
                ),
                _section(
                    "Sicherheiten",
                    "Zur Sicherung sämtlicher gegenwärtiger, künftiger und bedingter Ansprüche der Bank aus diesem Vertrag bestellt die Darlehensnehmerin die in Anlage 2 bezeichneten Sicherheiten. Dazu gehören insbesondere ein gesonderter Sicherungsvertrag über Software-Nutzungsrechte und ein Kontoguthabenpfandrecht.",
                    "Weitere Sicherheiten können bei wesentlicher Verschlechterung der wirtschaftlichen Verhältnisse verlangt werden, soweit ein berechtigtes Sicherungsinteresse besteht. Die Parteien halten fest, dass Forderungen aus Softwareverträgen zum Vertragsdatum noch nicht abgetreten werden.",
                ),
                _section(
                    "Zusicherungen der Darlehensnehmerin",
                    "Die Darlehensnehmerin erklärt bei Unterzeichnung, rechtswirksam gegründet und zum Abschluss des Vertrags befugt zu sein. Sie erklärt ferner, nach ihrem Kenntnisstand über die für den gewöhnlichen Geschäftsbetrieb erforderlichen Rechte an FiscusPilot zu verfügen und keine anderweitige Sicherung an diesen Rechten bestellt zu haben.",
                ),
                _section(
                    "Verfügungen und wesentliche Veränderungen",
                    "Außerhalb des gewöhnlichen Geschäftsbetriebs dürfen wesentliche Softwarerechte, Unternehmensteile und Kundenbestände nur mit vorheriger Zustimmung der Bank veräußert oder belastet werden. Übliche Kundenlizenzen und Pflegeverträge bleiben zulässig, sofern sie zu marktgerechten Bedingungen geschlossen werden.",
                ),
                _section(
                    "Kündigungsereignisse",
                    "Die Bank kann aus wichtigem Grund kündigen, insbesondere bei länger als 15 Bankarbeitstage ausstehenden Zahlungen, wesentlichen unrichtigen Angaben, nicht geheilten Vertragsverletzungen, Zahlungseinstellung oder Antrag auf Eröffnung eines Insolvenzverfahrens. Soweit eine Abhilfe möglich ist, wird grundsätzlich eine Frist von zehn Bankarbeitstagen gesetzt.",
                ),
                _section(
                    "Mitteilungen",
                    "Vertragsmitteilungen sind an workout@rhenus-kreditbank.example beziehungsweise finance@kurpfalz-taxware.example zu richten; Kündigungen und Sicherheitenfreigaben bedürfen der gesetzlichen oder vertraglich vereinbarten Form. Adressänderungen sind unverzüglich mitzuteilen.",
                ),
                _section(
                    "Schlussbestimmungen",
                    "Es gilt deutsches Recht. Gerichtsstand ist, soweit zulässig, Mannheim. Änderungen und Ergänzungen dieses Vertrags bedürfen mindestens der Textform, soweit nicht eine strengere Form vorgeschrieben ist. Anlagen 1 bis 4 sind Vertragsbestandteil.",
                ),
                _section(
                    "Unterschriften",
                    "Mannheim, 15.03.2023 — Rhenus Kreditbank AG, Silke Brandt und Beate Abele, jeweils handschriftlich unterzeichnet.",
                    "Heidelberg, 15.03.2023 — Kurpfalz Taxware GmbH, Martin Reuter, handschriftlich unterzeichnet. Der Scan enthält die Paraphen aller Unterzeichnenden auf den Anlagen 1 bis 4.",
                ),
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/02_Sicherungsvertrag_IP.docx",
            "docx",
            "Sicherungsvertrag über Software-Nutzungsrechte",
            sections=[
                _section(
                    "Vertragsparteien und Bezug",
                    "Sicherungsvertrag vom 15. März 2023 zwischen der Kurpfalz Taxware GmbH als Sicherungsgeberin und der Rhenus Kreditbank AG als Sicherheitennehmerin. Der Vertrag bezieht sich auf den Darlehensvertrag RK-2023-4471 desselben Datums.",
                    "Die Parteien bezeichnen die Sicherheitenbestellung als ergänzende Kreditsicherheit. Besitz, Betrieb und gewöhnliche Kundenlizenzierung sollen bis zu einem Verwertungsereignis bei der Sicherungsgeberin verbleiben.",
                ),
                _section(
                    "Sicherungszweck und gesicherte Ansprüche",
                    "Sicherungszweck ist die Sicherung sämtlicher gegenwärtigen, künftigen und bedingten Ansprüche der Bank gegen die Sicherungsgeberin aus dem Darlehensvertrag RK-2023-4471, seiner Durchführung, Kündigung und Rückabwicklung einschließlich Zinsen, Kosten und angemessener Rechtsverfolgungskosten. Die Haftungsobergrenze der Sicherheit beträgt 3.200.000,00 EUR zuzüglich Verwertungskosten.",
                ),
                _section(
                    "Bezeichnete Software",
                    "Erfasst werden die in Anlage S-1 aufgeführten Programme und Module der Produktfamilie FiscusPilot, insbesondere FiscusPilot Kanzlei, FiscusPilot Mittelstand, TaxEngine/Core, DocFlow, LedgerFlow, Webportal, mobile Belegerfassung sowie zugehörige Schnittstellen, Administrationswerkzeuge, Dokumentationen und Testbestände.",
                    "Die Bezeichnungen in Anlage S-1 schließen dort ausdrücklich genannte frühere Namen und technisch-organisatorische Nachfolgefassungen ein. Kunden- und personenbezogene Daten sind nicht Gegenstand der Rechtebestellung.",
                ),
                _section(
                    "Rechtseinräumung zur Sicherheit",
                    "Die Sicherungsgeberin räumt der Bank an der bezeichneten Software alle ihr zustehenden ausschließlichen Nutzungsrechte zur Sicherheit ein, soweit diese Rechte übertragbar oder einräumbar sind. Die Rechtseinräumung ist räumlich und zeitlich unbeschränkt und umfasst Quell- und Objektcode, Vervielfältigung, Verbreitung, Bearbeitung, Portierung, Verbindung, öffentliche Zugänglichmachung, Hosting, SaaS-Nutzung, Unterlizenzierung und die Weiterübertragung im Rahmen einer zulässigen Verwertung.",
                    "Die Parteien wollen auch im Sicherungszeitraum entstehende Updates, Upgrades, Module und Dokumentationen erfassen, sofern sie der Sicherungsgeberin zustehen und der bezeichneten Produktfamilie zugeordnet werden. Die Sicherungsgeberin wird erforderliche Einzelakte und Zustimmungen auf Anforderung dokumentieren.",
                ),
                _section(
                    "Ausübung im gewöhnlichen Geschäftsbetrieb",
                    "Die Bank gestattet der Sicherungsgeberin widerruflich, die gesicherten Rechte im gewöhnlichen Geschäftsbetrieb auszuüben, die Software zu entwickeln, zu pflegen, zu hosten und Endkunden einfache Nutzungsrechte zu marktüblichen Bedingungen einzuräumen. Ausschließliche Lizenzen, Übertragungen des Produktgeschäfts und weitere Sicherheiten bedürfen vorheriger Zustimmung der Bank.",
                ),
                _section(
                    "Repositorien und Hinterlegung",
                    "Die Sicherungsgeberin führt aktuelle Quellcodes in den in Anlage S-2 bezeichneten Repositorien und erstellt zum Quartalsende ein verschlüsseltes Backup. Auf Verlangen erhält die Bank eine Hashliste und eine Bestätigung des technischen Verwahrers; produktive Zugangsdaten sollen nur bei Eintritt eines Verwertungsereignisses übergeben werden.",
                ),
                _section(
                    "Zusicherungen und Informationspflichten",
                    "Die Sicherungsgeberin erklärt, nach ihrer Dokumentation Inhaberin der für den Geschäftsbetrieb erforderlichen Nutzungsrechte zu sein. Sie legt der Bank auf Anforderung Verträge mit wesentlichen Entwicklerinnen, Entwicklern und Auftragnehmern sowie eine Liste wesentlicher Drittkomponenten vor.",
                    "Streitigkeiten über Herkunft oder Umfang der Rechte, wesentliche Lizenzverstöße, Verlust von Repositorien, Verfügungen Dritter und Pfändungen sind unverzüglich mitzuteilen. Die Bank darf die Dokumentation durch zur Vertraulichkeit verpflichtete Sachverständige prüfen lassen.",
                ),
                _section(
                    "Verfügungsbeschränkungen im Innenverhältnis",
                    "Die Sicherungsgeberin verpflichtet sich, die gesicherten Rechte außerhalb gewöhnlicher Kundenlizenzen weder zu übertragen noch anderweitig zu belasten, aufzugeben oder über ausschließliche Rechte zu verfügen, solange die Bank nicht vorher in Textform zustimmt. Gesetzlich zwingende Verfügungsbefugnisse Dritter werden durch diese Vereinbarung nicht beschrieben.",
                ),
                _section(
                    "Verwertungsereignis und Verwertungsablauf",
                    "Ein Verwertungsereignis liegt vor, wenn gesicherte Ansprüche fällig und nicht erfüllt sind, der Darlehensvertrag wirksam aus wichtigem Grund beendet wurde oder ein Insolvenzverfahren beantragt wird, soweit die Verwertung rechtlich zulässig ist. Die Bank zeigt der Sicherungsgeberin die beabsichtigte Verwertung an und berücksichtigt berechtigte Interessen an einem geordneten Weiterbetrieb.",
                    "Die Verwertung kann nach Maßgabe der anwendbaren Vorschriften durch Lizenzierung, Verkauf oder Übertragung der gesicherten Rechtspositionen erfolgen. Die Bank darf fachkundige Dritte einschalten; Erlöse werden nach Abzug angemessener Kosten auf die gesicherten Ansprüche angerechnet.",
                ),
                _section(
                    "Freigabe und Rückgewähr",
                    "Soweit der realisierbare Wert aller Sicherheiten die gesicherten Ansprüche auf Dauer um mehr als 20 Prozent übersteigt, wird die Bank auf Verlangen Sicherheiten nach ihrer Wahl freigeben. Nach vollständiger und endgültiger Erfüllung aller gesicherten Ansprüche werden die zur Sicherheit eingeräumten Rechte zurückgewährt.",
                ),
                _section(
                    "Mitteilungen bei Krise und Verfahren",
                    "Die Sicherungsgeberin unterrichtet die Bank unverzüglich über drohende Zahlungsunfähigkeit, Insolvenzanträge, vorläufige Sicherungsmaßnahmen und die Bestellung einer Verwalterin oder eines Verwalters. Sie gestattet der Bank, dieser Person eine Vertragskopie und die Anlagen zu übermitteln.",
                ),
                _section(
                    "Schlussbestimmungen",
                    "Es gilt deutsches Recht. Gerichtsstand ist, soweit zulässig, Mannheim. Änderungen, Freigaben und Zustimmungen sollen in Textform dokumentiert werden. Anlagen S-1 bis S-3 sind Vertragsbestandteil; bei Widersprüchen geht der Vertragstext vor.",
                ),
                _section(
                    "Unterschriften",
                    "Mannheim, 15.03.2023 — Rhenus Kreditbank AG, Silke Brandt und Beate Abele, handschriftlich unterzeichnet.",
                    "Heidelberg, 15.03.2023 — Kurpfalz Taxware GmbH, Martin Reuter, handschriftlich unterzeichnet. Jede Partei bestätigt den Erhalt einer gegengezeichneten Ausfertigung samt Anlagen.",
                ),
            ],
        ),
        _xlsx(
            "05_Finanzierung_Sicherheiten/03_Anlage_IP_Rechtebestand.xlsx",
            "Anlagen S-1 und S-2 zum IP-Sicherungsvertrag",
            [
                {
                    "name": "S-1_Produkte_Rechte",
                    "headers": ["Pos.", "Produkt/Modul", "Frühere Bezeichnung", "Version am 15.03.2023", "Rechteart laut Anlage", "Nachfolge erfasst", "Bemerkung"],
                    "rows": [
                        [1, "FiscusPilot Kanzlei", "TaxEngine Kanzlei", "3.9", "ausschließliche Nutzungsrechte soweit vorhanden", "ja", "inklusive Wartungsstände"],
                        [2, "FiscusPilot Mittelstand", "LedgerPilot", "3.9", "ausschließliche Nutzungsrechte soweit vorhanden", "ja", "inklusive LedgerFlow"],
                        [3, "TaxEngine / Core", "TaxEngine Classic", "3.9", "Quell-/Objektcode und Dokumentation", "ja", "Altmodule und Adapter"],
                        [4, "DocFlow", "Document Service", "3.9", "Software und Handbuch", "ja", "Drittkomponenten vorbehalten"],
                        [5, "FiscusPilot Web", "KanzleiCloud Web", "3.9", "Webclient und Designs", "ja", "FormKit-Anteil laut Entwicklerakte"],
                        [6, "LedgerFlow", "Import Hub", "0.8", "Importmodule", "ja", "Vorbestand in Mitarbeitervertrag"],
                        [7, "Mobile Belegerfassung", "Receipt Capture PoC", "Konzeptstand", "künftige Erweiterung", "ja", "noch kein produktives Release"],
                        [8, "Kundendokumentation", "Handbuch/Knowledge Base", "Stand 02/2023", "Texte, Grafiken, Anleitungen", "ja", "Autorenliste separat"],
                    ],
                },
                {
                    "name": "S-2_Repositorien",
                    "headers": ["Repository-Bezeichnung 2023", "Serverpfad 2023", "Backup", "Zugriffsverantwortung", "Heutige Entsprechung", "Abgleichstatus"],
                    "rows": [
                        ["fiscuspilot-core", "git/core/fiscuspilot", "quartalsweise", "Lena Vogt", "git/platform/fiscuspilot-core", "Pfad geändert"],
                        ["kanzlei-web", "git/web/kanzlei", "quartalsweise", "Jonas Eberle", "git/apps/fiscuspilot-web", "umbenannt"],
                        ["taxengine-legacy", "git/archive/taxengine", "halbjährlich", "Lena Vogt", "git/archive/taxengine-legacy", "gleichartig"],
                        ["ledger-import", "git/modules/ledger", "quartalsweise", "Marek Nowak", "git/modules/ledger-flow", "umbenannt"],
                        ["deployment", "git/ops/deployment", "quartalsweise", "Esra Kaya", "git/ops/platform-deploy", "umbenannt"],
                        ["receipt-capture", "noch anzulegen", "nicht festgelegt", "nicht festgelegt", "git/apps/receipt-capture", "nach Vertrag entstanden"],
                    ],
                },
                {
                    "name": "S-3_Rechtenachweise",
                    "headers": ["Person/Quelle", "Dokument", "Datum", "Im Bankdatenraum 2023", "Aktueller Fund", "Hinweis"],
                    "rows": [
                        ["Lukas Binder", "Freelancer-Rahmenvertrag und Anlage 2", "14.06.2017", "Rahmenvertrag ohne farbige Anlage", "vollständiger Scan laut Verwalterin", "Anlagenfassung vergleichen"],
                        ["Dr. Lena Vogt", "Arbeitsvertrag und V-1", "20.03.2019", "ja", "ja", "Archiv TaxParse fehlt"],
                        ["Jonas Eberle", "Arbeitsvertrag und E-1", "10.07.2020", "Arbeitsvertrag", "Anlage nur einseitig signiert", "FormKit"],
                        ["Esra Kaya", "Arbeitsvertrag und Policy", "29.01.2021", "ja", "ja", "Policy später geändert"],
                        ["Marek Nowak", "Arbeitsvertrag und N-1", "14.10.2022", "Arbeitsvertrag", "Anlage unvollständig", "LedgerLens"],
                        ["Nina Scholl", "Arbeitsvertrag und S-1", "12.04.2024", "bei Bestellung noch nicht beschäftigt", "Deckblatt ohne Dateiliste", "ReceiptCam"],
                    ],
                },
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx",
            "docx",
            "Sicherungsabtretung der Lizenz-, Pflege- und Supportforderungen",
            sections=[
                _section(
                    "Vertragsparteien und Anlass",
                    "Vereinbarung vom 1. Februar 2024 zwischen der Kurpfalz Taxware GmbH als Zedentin und der Rhenus Kreditbank AG als Zessionarin. Die Parteien beziehen sich auf das Darlehen RK-2023-4471 und stellen fest, dass dieser Vertrag die Forderungssicherheit gesondert vom IP-Sicherungsvertrag regelt.",
                ),
                _section(
                    "Sicherungszweck und gesicherte Forderungen der Bank",
                    "Sicherungszweck der Abtretung ist die Sicherung aller gegenwärtigen, künftigen und bedingten Ansprüche der Bank aus der gesamten Geschäftsverbindung mit der Zedentin, insbesondere Kapital, Zinsen, Kosten und Rückabwicklungsansprüche aus dem Darlehen RK-2023-4471.",
                ),
                _section(
                    "Abgetretene Kundenforderungen",
                    "Die Zedentin tritt der Bank sämtliche gegenwärtigen und künftigen Geldforderungen gegen in- und ausländische Kunden aus Softwarelizenzen, Softwareabonnements, Pflege, Support, Hosting, Updateleistungen und den in diesen Verträgen vereinbarten Nebenleistungen ab. Erfasst werden auch Forderungen aus Vertragsverlängerung, Preisanpassung und Beendigung, soweit sie an die Stelle einer erfassten Forderung treten.",
                    "Nicht erfasst sind reine Hardwareverkäufe, Reisekostenerstattungen, Steuern, durchlaufende Posten und individuell beauftragte Beratungsprojekte, soweit diese nicht Bestandteil eines kombinierten Softwarevertrags sind. Gutschriften mindern die jeweilige Forderung.",
                ),
                _section(
                    "Entstehung und Bestimmbarkeit",
                    "Die Abtretung soll mit Entstehung der jeweiligen Forderung wirksam werden. Die Zedentin führt ein Debitorenregister, aus dem Kunde, Vertrag, Rechnungsnummer, Leistungsart, Fälligkeit, Gutschriften und Zahlung hervorgehen. Die Bank erhält monatlich einen Export.",
                ),
                _section(
                    "Einziehungsbefugnis",
                    "Die Bank ermächtigt die Zedentin widerruflich, die abgetretenen Forderungen im eigenen Namen einzuziehen und Zahlungen auf ihre im Register angegebenen Geschäftskonten entgegenzunehmen. Die Zedentin darf Zahlungsziele bis 30 Tage und marktübliche Gutschriften gewähren; weitergehende Stundungen und Erlasse über 10.000,00 EUR je Kunde bedürfen der Zustimmung der Bank.",
                ),
                _section(
                    "Offenlegung und Zahlungsumleitung",
                    "Die Bank kann die Abtretung gegenüber einzelnen oder allen Drittschuldnern offenlegen und Zahlung an sich oder ein benanntes Konto verlangen, wenn ein Kündigungsereignis nach dem Darlehensvertrag vorliegt, Finanzberichte länger als 20 Tage ausstehen oder der Wert der offenen erfassten Forderungen 1.500.000,00 EUR unterschreitet. Die Zedentin unterzeichnet auf Anforderung vorbereitete Abtretungsanzeigen.",
                ),
                _section(
                    "Zusicherungen der Zedentin",
                    "Die Zedentin erklärt, die Forderungen seien, soweit im Debitorenregister nicht anders markiert, weder abgetreten noch verpfändet und nach ihrer Kenntnis frei von vertraglichen Abtretungsverboten. Einwendungen, Aufrechnungen, Kündigungen und Streitigkeiten über mehr als 5.000,00 EUR werden im monatlichen Export kenntlich gemacht.",
                ),
                _section(
                    "Prüf- und Auskunftsrechte",
                    "Die Bank darf nach angemessener Vorankündigung Verträge, Rechnungen, Zahlungsbelege und Debitorenkonten prüfen oder durch zur Vertraulichkeit verpflichtete Dritte prüfen lassen. Bei einem Kündigungsereignis kann die Prüfung ohne Vorankündigung während üblicher Geschäftszeiten erfolgen.",
                ),
                _section(
                    "Verwertung und Anrechnung",
                    "Nach Widerruf der Einziehungsbefugnis zieht die Bank offengelegte Forderungen nach Maßgabe der anwendbaren Vorschriften ein. Zahlungseingänge werden nach Abzug notwendiger Einziehungskosten auf die gesicherten Forderungen angerechnet. Die Bank informiert die Zedentin über wesentliche Einziehungsmaßnahmen.",
                ),
                _section(
                    "Freigabe und Vertragsende",
                    "Übersteigt der realisierbare Gesamtwert der Sicherheiten die gesicherten Forderungen auf Dauer um mehr als 20 Prozent, gibt die Bank auf Verlangen Sicherheiten nach ihrer Wahl frei. Nach vollständiger und endgültiger Erfüllung der gesicherten Ansprüche tritt die Bank noch bestehende Forderungen zurück.",
                ),
                _section(
                    "Mitteilungen und Schlussbestimmungen",
                    "Insolvenzanträge, Pfändungen in Debitorenforderungen und wesentliche Änderungen des Abrechnungssystems sind unverzüglich mitzuteilen. Es gilt deutsches Recht; Gerichtsstand ist, soweit zulässig, Mannheim. Änderungen und Freigaben sollen in Textform festgehalten werden.",
                ),
                _section(
                    "Unterschriften",
                    "Mannheim, 01.02.2024 — Rhenus Kreditbank AG, Silke Brandt und Jan Küster, handschriftlich unterzeichnet.",
                    "Heidelberg, 01.02.2024 — Kurpfalz Taxware GmbH, Martin Reuter, handschriftlich unterzeichnet. Anlage F-1 mit Debitorenliste Stand Januar 2024 ist paraphiert.",
                ),
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/05_Abtretungsanzeige_Muster.pdf",
            "pdf",
            "Abtretungsanzeige und dokumentierte Versandliste",
            sections=[
                _section(
                    "Mustertext",
                    "Sehr geehrte Damen und Herren, die Kurpfalz Taxware GmbH hat gegenwärtige und künftige Forderungen aus Ihrem Software-, Pflege- und Supportvertrag zur Sicherheit an die Rhenus Kreditbank AG abgetreten. Bis zu einer abweichenden schriftlichen Mitteilung der Bank können Sie weiterhin mit schuldbefreiender Wirkung auf das bisherige, in der Rechnung bezeichnete Konto der Kurpfalz Taxware GmbH zahlen.",
                    "Bitte bestätigen Sie lediglich den Erhalt dieser Anzeige und teilen Sie bestehende Einwendungen, Gutschriften oder entgegenstehende Vertragsregelungen mit. Diese Anzeige ändert Leistungsumfang, Laufzeit und Ansprechpartner des Softwarevertrags nicht.",
                ),
                _section(
                    "Ausfertigung",
                    "Muster datiert auf den 12. Februar 2024. Unterzeichnet von Martin Reuter für die Kurpfalz Taxware GmbH und Silke Brandt für die Rhenus Kreditbank AG. Interner Vermerk: 'Versand nach Auswahl aus F-1, zunächst Top 25'.",
                ),
            ],
            tables=[
                {
                    "title": "Versand- und Rückmeldestatus aus Bankordner",
                    "headers": ["Kunde", "Versanddatum", "Versandart", "Empfang bestätigt", "Einwendung/Hinweis"],
                    "rows": [
                        ["Müller & Reiter PartG mbB", "14.02.2024", "Einschreiben und E-Mail", "19.02.2024", "Zustimmung zur Vertragsübernahme unberührt"],
                        ["PfalzForm Maschinenbau GmbH", "nicht auf Liste; Vertrag später", "", "", ""],
                        ["Auer & Hain StBG mbH", "15.02.2024", "E-Mail", "keine gesonderte Bestätigung", "Versandprotokoll vorhanden"],
                        ["Neckarblick Treuhand KG", "14.02.2024", "Einschreiben", "20.02.2024", "Abtretungsverbot im Vertrag erwähnt"],
                        ["Rheinauer Pumpenbau GmbH", "nicht auf Liste; Vertrag später", "", "", ""],
                        ["Schwarz & Vetter PartG mbB", "15.02.2024", "E-Mail", "16.02.2024", "keine Einwendung"],
                    ],
                }
            ],
        ),
        _xlsx(
            "05_Finanzierung_Sicherheiten/06_Rechnungen_und_Forderungen.xlsx",
            "Rechnungs- und Forderungsmatrix zum 30. September 2026",
            [
                {
                    "name": "Offene_Forderungen",
                    "headers": ["Rechnung", "Kunde", "Vertrag", "Leistungsart", "Rechnungsdatum", "Fällig", "Brutto EUR", "Offen EUR", "Zahlungskonto", "Abtretungshinweis"],
                    "rows": [
                        ["KTW-2026-9044", "Müller & Reiter", "MR-2024-01", "Pflege Q4/2026", "01.09.2026", "15.09.2026", 5533.5, 5533.5, "Heidelberger Volksbank", "Fußzeile Rhenusbank"],
                        ["KTW-2026-9121", "PfalzForm", "PF-2025-05", "Cloud Oktober 2026", "20.09.2026", "01.10.2026", 9282, 9282, "Heidelberger Volksbank", "kein Hinweis"],
                        ["KTW-2026-9148", "Auer & Hain", "AH-2022-09", "Lizenz/Hosting Oktober", "25.09.2026", "05.10.2026", 1725.5, 1725.5, "Sparkasse Heidelberg", "Fußzeile Rhenusbank"],
                        ["KTW-2026-8877", "Neckarblick Treuhand", "NT-2023-11", "Jahrespflege", "15.08.2026", "29.08.2026", 50932, 42000, "Heidelberger Volksbank", "offengelegt 2024"],
                        ["KTW-2026-9160", "Rheinauer Pumpenbau", "RP-2026-02", "Cloud Oktober", "28.09.2026", "08.10.2026", 6783, 6783, "Heidelberger Volksbank", "kein Hinweis"],
                        ["KTW-2026-8734", "Weingut Sonnenhang", "WS-2025-07", "Migration Projekt", "30.07.2026", "13.08.2026", 14280, 7140, "Sparkasse Heidelberg", "Projektleistung markiert"],
                        ["KTW-2026-9155", "Schwarz & Vetter", "SV-2021-03", "Pflege Oktober", "27.09.2026", "07.10.2026", 3094, 3094, "Heidelberger Volksbank", "offengelegt 2024"],
                        ["KTW-2026-9066", "Kurpfalz Logistik", "KL-2024-09", "Cloud September", "05.09.2026", "19.09.2026", 5117, 5117, "Heidelberger Volksbank", "kein Hinweis"],
                    ],
                },
                {
                    "name": "Abgrenzung",
                    "headers": ["Rechnung", "Lizenz EUR", "Pflege/Support EUR", "Hosting EUR", "Projekt EUR", "USt EUR", "Gutschrift EUR", "Zuordnung Sicherheit intern"],
                    "rows": [
                        ["KTW-2026-9044", 0, 4650, 0, 0, 883.5, 0, "erfasst"],
                        ["KTW-2026-9121", 5800, 900, 1100, 0, 1482, 0, "erfasst"],
                        ["KTW-2026-9148", 950, 0, 500, 0, 275.5, 0, "erfasst"],
                        ["KTW-2026-8877", 0, 42800, 0, 0, 8132, -8932, "erfasst, Gutschrift klären"],
                        ["KTW-2026-9160", 3900, 600, 1200, 0, 1083, 0, "erfasst"],
                        ["KTW-2026-8734", 0, 0, 0, 12000, 2280, 0, "Projekt – Zuordnung offen"],
                        ["KTW-2026-9155", 0, 2100, 500, 0, 494, 0, "erfasst"],
                        ["KTW-2026-9066", 3000, 400, 900, 0, 817, 0, "erfasst"],
                    ],
                },
                {
                    "name": "Summen_Alter",
                    "headers": ["Altersklasse", "Anzahl", "Brutto offen EUR", "davon bestritten EUR", "davon nach Eröffnung fakturiert EUR"],
                    "rows": [
                        ["noch nicht fällig", 31, 162440, 0, 68420],
                        ["1–30 Tage", 47, 218730, 14300, 0],
                        ["31–60 Tage", 18, 94480, 22150, 0],
                        ["61–90 Tage", 9, 57110, 18000, 0],
                        ["> 90 Tage", 12, 83690, 42600, 0],
                        ["Gesamt", 117, 616450, 97050, 68420],
                    ],
                },
                {
                    "name": "Zahlungen_nach_Eroeffnung",
                    "headers": ["Datum", "Kunde", "Rechnung", "Betrag EUR", "Eingangskonto", "Buchungstext", "Weiterleitung Bank"],
                    "rows": [
                        ["16.09.2026", "Kurpfalz Logistik", "KTW-2026-8990", 5117, "Heidelberger Volksbank", "Cloud 09/26", "nein"],
                        ["18.09.2026", "Auer & Hain", "KTW-2026-8971", 1725.5, "Sparkasse Heidelberg", "Lizenz 09/26", "nein"],
                        ["22.09.2026", "Müller & Reiter", "KTW-2026-8870", 5533.5, "Heidelberger Volksbank", "Pflege 09/26", "nein"],
                        ["28.09.2026", "Schwarz & Vetter", "KTW-2026-9002", 3094, "Heidelberger Volksbank", "Pflege 09/26", "nein"],
                        ["01.10.2026", "PfalzForm", "KTW-2026-9121", 9282, "Heidelberger Volksbank", "Cloud Oktober", "nein; Rechnung in Hauptblatt noch als offen"],
                    ],
                },
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/07_Rechnung_Mueller_Reiter_2026_09.pdf",
            "pdf",
            "Rechnung KTW-2026-9044 an Müller & Reiter",
            paragraphs=[
                "Kurpfalz Taxware GmbH, Im Neuenheimer Feld 583, 69120 Heidelberg. Rechnung KTW-2026-9044 vom 1. September 2026 an Müller & Reiter Steuerberatung PartG mbB, Sofienstraße 12, 69115 Heidelberg. Kundennummer K-1017, Vertrag MR-2024-01.",
                "Leistungszeitraum 1. Oktober bis 31. Dezember 2026. Zahlbar bis 15. September 2026 auf IBAN DE44 6729 0000 0044 7711 02 bei der Heidelberger Volksbank.",
                "Fußzeile: Forderungen aus Lizenz-, Pflege- und Supportverträgen sind an die Rhenus Kreditbank AG sicherungsabgetreten. Zahlungen sind bis zu einer abweichenden Mitteilung weiterhin auf das bezeichnete Konto zu leisten.",
            ],
            tables=[
                {
                    "title": "Rechnungspositionen",
                    "headers": ["Pos.", "Beschreibung", "Menge", "Einzelpreis EUR", "Netto EUR"],
                    "rows": [
                        [1, "FiscusPilot Enterprise Pflege Q4/2026", 1, 4650, 4650],
                        [2, "Nettosumme", "", "", 4650],
                        [3, "Umsatzsteuer 19 %", "", "", 883.5],
                        [4, "Rechnungsbetrag", "", "", 5533.5],
                    ],
                }
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/08_Rechnung_PfalzForm_2026_Q4.pdf",
            "pdf",
            "Rechnung KTW-2026-9121 an PfalzForm Maschinenbau",
            paragraphs=[
                "Kurpfalz Taxware GmbH, Im Neuenheimer Feld 583, 69120 Heidelberg. Rechnung KTW-2026-9121 vom 20. September 2026 an PfalzForm Maschinenbau GmbH, Floßwörthstraße 48, 68199 Mannheim. Kundennummer M-2044, Vertrag PF-2025-05.",
                "Leistungsmonat Oktober 2026. Zahlbar zum 1. Oktober 2026 auf IBAN DE44 6729 0000 0044 7711 02 bei der Heidelberger Volksbank. Auf dem im Datenraum vorhandenen PDF fehlt die in neueren Rechnungslayouts verwendete Abtretungsfußzeile.",
                "ERP-Notiz vom 2. Oktober: Zahlungseingang wurde importiert, der Ausgleichslauf blieb wegen einer Kontosperre im Status 'Vorschlag'.",
            ],
            tables=[
                {
                    "title": "Rechnungspositionen",
                    "headers": ["Pos.", "Beschreibung", "Menge", "Einzelpreis EUR", "Netto EUR"],
                    "rows": [
                        [1, "FiscusPilot Mittelstand Cloud", 1, 5800, 5800],
                        [2, "Premium-Support", 1, 900, 900],
                        [3, "Cloudbetrieb Deutschland", 1, 1100, 1100],
                        [4, "Nettosumme", "", "", 7800],
                        [5, "Umsatzsteuer 19 %", "", "", 1482],
                        [6, "Rechnungsbetrag", "", "", 9282],
                    ],
                }
            ],
        ),
        _csv(
            "05_Finanzierung_Sicherheiten/09_Offene_Posten_Export.csv",
            "ERP-Export offene Posten vom 30. September 2026",
            ["Debitor", "Kunde", "Rechnung", "Belegdatum", "Fälligkeit", "Brutto_EUR", "Offen_EUR", "Mahnstufe", "Vertragsart", "Hinweis"],
            [
                [1017, "Müller & Reiter", "KTW-2026-9044", "01.09.2026", "15.09.2026", 5533.5, 5533.5, 1, "Pflege", "Escrow-Rückfrage"],
                [2044, "PfalzForm", "KTW-2026-9121", "20.09.2026", "01.10.2026", 9282, 9282, 0, "Cloud", "Zahlung 01.10 noch nicht ausgeglichen"],
                [1029, "Auer & Hain", "KTW-2026-9148", "25.09.2026", "05.10.2026", 1725.5, 1725.5, 0, "Lizenz/Hosting", ""],
                [1088, "Neckarblick Treuhand", "KTW-2026-8877", "15.08.2026", "29.08.2026", 50932, 42000, 2, "Pflege", "Gutschrift 8.932 EUR noch ungebucht"],
                [2051, "Rheinauer Pumpenbau", "KTW-2026-9160", "28.09.2026", "08.10.2026", 6783, 6783, 0, "Cloud", ""],
                [2077, "Weingut Sonnenhang", "KTW-2026-8734", "30.07.2026", "13.08.2026", 14280, 7140, 3, "Projekt", "Teilzahlung"],
                [1112, "Schwarz & Vetter", "KTW-2026-9155", "27.09.2026", "07.10.2026", 3094, 3094, 0, "Pflege", ""],
                [2091, "Kurpfalz Logistik", "KTW-2026-9066", "05.09.2026", "19.09.2026", 5117, 5117, 1, "Cloud", ""],
                [1134, "Kanzlei Ufer & Sohn", "KTW-2026-8818", "06.08.2026", "20.08.2026", 11876.2, 11876.2, 2, "Jahreslizenz", "Mängelanzeige Support"],
                [2110, "Bergwerk Präzision GmbH", "KTW-2026-8950", "25.08.2026", "08.09.2026", 15470, 15470, 2, "Cloud/Projekt", "Aufteilung fehlt"],
                [1168, "Steuerteam Plankstadt", "KTW-2026-9008", "28.08.2026", "11.09.2026", 3927, 3927, 1, "Pflege", "Kündigung zum Jahresende"],
                [2122, "Rhein-Neckar Guss GmbH", "KTW-2026-9014", "29.08.2026", "12.09.2026", 8330, 4165, 1, "Cloud", "hälftige Zahlung"],
                [1192, "Kanzlei Marktbrücke", "KTW-2026-8661", "01.07.2026", "15.07.2026", 22491, 22491, 3, "Migration/Pflege", "Vergleichsgespräch"],
                [2140, "Pfälzer Kabeltechnik", "KTW-2026-9130", "22.09.2026", "06.10.2026", 5950, 5950, 0, "Cloud", ""],
                [1211, "Treuhand am Schloss", "KTW-2026-9170", "29.09.2026", "13.10.2026", 4641, 4641, 0, "Pflege", ""],
            ],
        ),
        _xlsx(
            "05_Finanzierung_Sicherheiten/10_Bankkonto_Umsatzliste.xlsx",
            "Kontoumsätze mit Kundenbezug nach Verfahrenseröffnung",
            [
                {
                    "name": "HVoba_771102",
                    "headers": ["Buchung", "Valuta", "Auftraggeber", "Verwendungszweck", "Betrag EUR", "Zuordnung", "Weiterverwendung"],
                    "rows": [
                        ["16.09.2026", "16.09.2026", "Kurpfalz Logistik GmbH", "KTW-2026-8990 Cloud 09/26", 5117, "Lizenz/Cloud", "Massekonto-Sweep 19.09."],
                        ["22.09.2026", "22.09.2026", "Müller & Reiter PartG mbB", "KTW-2026-8870 Pflege 09/26", 5533.5, "Pflege", "Massekonto-Sweep 23.09."],
                        ["28.09.2026", "28.09.2026", "Schwarz & Vetter PartG mbB", "KTW-2026-9002", 3094, "Pflege", "Massekonto-Sweep 30.09."],
                        ["01.10.2026", "01.10.2026", "PfalzForm Maschinenbau GmbH", "KTW-2026-9121 Oktober", 9282, "Cloud", "Massekonto-Sweep 02.10."],
                        ["06.10.2026", "06.10.2026", "Rheinauer Pumpenbau GmbH", "Cloud September Nachlauf", 6783, "Cloud", "Massekonto-Sweep 07.10."],
                    ],
                },
                {
                    "name": "Sparkasse_3390",
                    "headers": ["Buchung", "Valuta", "Auftraggeber", "Verwendungszweck", "Betrag EUR", "Zuordnung", "Weiterverwendung"],
                    "rows": [
                        ["18.09.2026", "18.09.2026", "Auer & Hain StBG mbH", "KTW-2026-8971 Lizenz 09/26", 1725.5, "Lizenz/Hosting", "Massekonto 21.09."],
                        ["24.09.2026", "24.09.2026", "Weingut Sonnenhang KG", "Teilzahlung Migration", 7140, "Projekt", "Massekonto 25.09."],
                        ["02.10.2026", "02.10.2026", "Treuhand am Schloss", "Pflege 10/26", 4641, "Pflege", "Massekonto 05.10."],
                    ],
                },
                {
                    "name": "Kontenstatus",
                    "headers": ["Konto", "Inhaber", "Status", "Verfügungsberechtigung seit 15.09.", "Saldo 30.09. EUR", "Abtretungsbezug im Buchungstext"],
                    "rows": [
                        ["HVoba ...1102", "Kurpfalz Taxware GmbH", "eingeschränkt", "Dr. Mohn / Kanzlei", 38422.18, "teilweise"],
                        ["Sparkasse ...3390", "Kurpfalz Taxware GmbH", "eingeschränkt", "Dr. Mohn / Kanzlei", 12908.44, "teilweise"],
                        ["Massekonto ...8841", "Dr. Mohn für Kurpfalz Taxware", "aktiv", "Dr. Mohn", 217443.09, "keine Einzelzuordnung"],
                        ["Rhenus Sicherheitenkonto ...2208", "Rhenus Kreditbank AG", "kein Zahlungseingang", "Rhenus Kreditbank", 0, "in Offenlegungsentwurf genannt"],
                    ],
                },
            ],
        ),
    ]
)


CASE["documents"].extend(
    [
        _xlsx(
            "05_Finanzierung_Sicherheiten/12_Anlage_1_Auszahlungsvoraussetzungen.xlsx",
            "Anlage 1 zum Darlehensvertrag – Auszahlungsvoraussetzungen und Freigaben",
            [
                {
                    "name": "Tranche_1",
                    "headers": ["Nr.", "Auszahlungsvoraussetzung", "Sollbeleg", "Fundstelle/Eingang", "Status", "Waiver/Restpunkt", "Prüfer", "Freigabe"],
                    "rows": [
                        [1, "Darlehensvertrag RK-2023-4471 und Anlagen 1 bis 4 beiderseits unterzeichnet", "gegenseitige Ausfertigung", "Kreditakte K-01; 15.03.2023", "erfüllt", "kein Vorbehalt", "Jan Küster, 16.03.2023", ""],
                        [2, "IP-Sicherungsvertrag samt Anlagen S-1 bis S-3 beiderseits unterzeichnet", "Vertrag und Anlagen", "Sicherheitenakte S-01; 15.03.2023", "erfüllt", "Repository-Pfadabgleich bleibt laufende Informationspflicht", "Silke Brandt, 16.03.2023", ""],
                        [3, "Kontoguthabenpfandrecht und Kontoverbindung der Darlehensnehmerin bestätigt", "Pfandanzeige und Kontobestätigung", "Sicherheitenakte S-04; HVoba-Bestätigung 16.03.2023", "erfüllt", "Pfandurkunde ist nicht Bestandteil der vorliegenden IP-Prüfakte", "Jan Küster, 16.03.2023", ""],
                        [4, "Geschäftsführerbefugnis und Gesellschafterzustimmung für Kreditaufnahme", "Registerauszug und Gesellschafterbeschluss", "Legal K-03/K-04; 16.03.2023", "erfüllt", "kein Vorbehalt", "Beate Abele, 16.03.2023", ""],
                        [5, "Budget Cloud-Migration und Entwicklung mindestens 1.600.000 EUR", "Budget FP-MIG-2023-02", "Finance K-05; 16.03.2023", "erfüllt", "Mittelumschichtungen über zehn Prozent bleiben zustimmungspflichtig", "Silke Brandt, 16.03.2023", ""],
                        [6, "Abruf über 1.600.000 EUR mit Empfängerkonto und Verwendungszweck", "Abrufschreiben der Darlehensnehmerin", "05_Finanzierung_Sicherheiten/13_Abruf_Tranche_1.eml; 16.03.2023", "erfüllt", "kein Vorbehalt", "Jan Küster, 17.03.2023", ""],
                        [7, "Einzugsermächtigung für Bearbeitungsentgelt 18.000 EUR", "gesonderte Belastungsermächtigung", "Abrufmail Ziffer 3; 16.03.2023", "erfüllt", "Gebühr mindert den Bruttokapitalabruf nicht", "Jan Küster, 17.03.2023", ""],
                        [8, "Keine Kündigungstatsache, kein Insolvenzantrag und keine wesentliche nachteilige Veränderung", "Geschäftsführerbestätigung", "Compliance K-07; 16.03.2023", "erfüllt", "Kenntnisstand nur bis Freigabe", "Beate Abele, 17.03.2023", ""],
                        [9, "Vier-Augen-Freigabe der Bank", "Freigabevermerk", "Zahlungsworkflow PAY-2023-0317-44", "erfüllt", "Ausführung frühestens 20.03.2023", "Silke Brandt / Beate Abele, 17.03.2023", "17.03.2023, 15:42"],
                        ["Kontrolle", "", "", "", "=COUNTIF(E6:E14,\"erfüllt\")+COUNTIF(E6:E14,\"erfüllt mit dokumentierter Abweichung\")+COUNTIF(E6:E14,\"verzichtet\")", "9 von 9 Voraussetzungen müssen entschieden sein", "=COUNTA(G6:G14)", "=IF(AND(E15=9,G15=9),\"Freigabefähig\",\"Sperre\")"],
                    ],
                },
                {
                    "name": "Tranche_2",
                    "headers": ["Nr.", "Auszahlungsvoraussetzung", "Sollbeleg", "Fundstelle/Eingang", "Status", "Waiver/Restpunkt", "Prüfer", "Freigabe"],
                    "rows": [
                        [1, "Ordnungsgemäßer Abruf über 800.000 EUR mindestens einen Bankarbeitstag vor Auszahlung", "Abrufmail", "05_Finanzierung_Sicherheiten/16_Abruf_Tranche_2.eml; 30.06.2023", "erfüllt", "Ausführung am folgenden Bankarbeitstag", "Jan Küster, 30.06.2023", ""],
                        [2, "Mindestens 1.350.000 EUR förderfähige Verwendung der ersten Tranche nachgewiesen", "Mittelverwendungsübersicht und Belegliste", "05_Finanzierung_Sicherheiten/15_Verwendungsnachweis_Tranche_1.pdf; 29.06.2023", "erfüllt", "anerkannt 1.438.600 EUR; Marketingrechnung 42.000 EUR nicht angerechnet", "Silke Brandt, 30.06.2023", ""],
                        [3, "Cloud-Migrationsmeilenstein M2 technisch abgenommen", "Abnahmeprotokoll M2", "Tech CP-2.3; 28.06.2023", "erfüllt", "kein Vorbehalt", "Beate Abele, 30.06.2023", ""],
                        [4, "Aktualisiertes Budget für Produktlaunch und Vertriebsausbau", "Budget FP-LAUNCH-2023-06", "Finance CP-2.4; 29.06.2023", "erfüllt", "Budgetobergrenzen bleiben verbindlich", "Silke Brandt, 30.06.2023", ""],
                        [5, "Original des Provider-Abnahmebelegs über 76.000 EUR", "Originalrechnung und Abnahme", "Scan vollständig; Original beim Provider angefordert", "verzichtet", "Einmaliger schriftlicher Waiver WA-2023-06-02 vom 30.06.2023; Original bis 14.07.2023 nachzureichen; keine Änderung von Zusicherungen", "Silke Brandt / Beate Abele, 30.06.2023", ""],
                        [6, "BWA, Liquiditätsstatus und wiederkehrender Jahresumsatz zum 31.05.2023", "Finanzreporting", "Reporting CP-2.6; 29.06.2023", "erfüllt", "kein Vorbehalt", "Jan Küster, 30.06.2023", ""],
                        [7, "Keine fällige Vertragsverletzung und kein Insolvenzantrag", "Geschäftsführerbestätigung", "Compliance CP-2.7; 30.06.2023", "erfüllt", "Kenntnisstand bis Freigabe", "Beate Abele, 30.06.2023", ""],
                        [8, "Aktualisierte Repository- und Backupbestätigung", "Hashliste Q2/2023 und Verwahrerbestätigung", "Tech CP-2.8; 29.06.2023", "erfüllt mit dokumentierter Abweichung", "Receipt-Capture-Repository noch nicht angelegt; nach Anlage S-2 nicht Auszahlungshindernis", "Jan Küster, 30.06.2023", ""],
                        [9, "Vier-Augen-Freigabe der Bank", "Freigabevermerk", "Zahlungsworkflow PAY-2023-0630-19", "erfüllt", "Bruttovaluta 800.000 EUR; keine weitere Gebühr", "Silke Brandt / Beate Abele, 30.06.2023", "30.06.2023, 15:42"],
                        ["Kontrolle", "", "", "", "=COUNTIF(E6:E14,\"erfüllt\")+COUNTIF(E6:E14,\"erfüllt mit dokumentierter Abweichung\")+COUNTIF(E6:E14,\"verzichtet\")", "9 von 9 Voraussetzungen müssen entschieden sein", "=COUNTA(G6:G14)", "=IF(AND(E15=9,G15=9),\"Freigabefähig\",\"Sperre\")"],
                    ],
                },
                {
                    "name": "Freigabeprotokoll",
                    "headers": ["Tranche", "Abruf", "Bruttokapital EUR", "Gebühr EUR", "Netto-Liquidität EUR", "CP-Kontrolle", "Freigabe", "Ausführung"],
                    "rows": [
                        [1, "16.03.2023", 1600000, 18000, "=C6-D6", "=Tranche_1!H14", "Silke Brandt / Beate Abele, 17.03.2023", "20.03.2023"],
                        [2, "30.06.2023", 800000, 0, "=C7-D7", "=Tranche_2!H14", "Silke Brandt / Beate Abele, 30.06.2023", "03.07.2023"],
                        ["Kontrolle", "", "=SUM(C6:C7)", "=SUM(D6:D7)", "=SUM(E6:E7)", "", "Bruttokapital = Netto-Liquidität + Gebühr", "=IF(C8=E8+D8,\"OK\",\"FEHLER\")"],
                    ],
                },
            ],
        ),
        _mail(
            "05_Finanzierung_Sicherheiten/13_Abruf_Tranche_1.eml",
            "Abruf der ersten Darlehenstranche",
            sender="Martin Reuter <finance@kurpfalz-taxware.example>",
            to=["Silke Brandt <silke.brandt@rhenus-kreditbank.example>"],
            cc=["Nora Schenk <nora.schenk@kurpfalz-taxware.example>", "kreditauszahlung@rhenus-kreditbank.example"],
            date="Thu, 16 Mar 2023 10:24:00 +0100",
            subject="RK-2023-4471 – Abruf Tranche 1 über 1.600.000 EUR",
            body=(
                "Sehr geehrte Frau Brandt,\n\nnamens der Kurpfalz Taxware GmbH rufe ich aus dem "
                "gestern unterzeichneten Darlehen RK-2023-4471 die erste Tranche in Höhe von "
                "1.600.000,00 EUR mit Valuta 20. März 2023 ab. Bitte schreiben Sie die Bruttovaluta "
                "dem Geschäftskonto IBAN DE44 6729 0000 0044 7711 02 bei der Heidelberger Volksbank "
                "gut. Verwendungszweck sind die Cloud-Migration und die Entwicklungsleistungen gemäß "
                "Budget FP-MIG-2023-02.\n\nWir ermächtigen die Bank, das Bearbeitungsentgelt von "
                "18.000,00 EUR am selben Valutatag gesondert auf diesem Geschäftskonto zu belasten. "
                "Der Kapitalabruf beträgt unverändert 1.600.000,00 EUR; nach der separaten "
                "Gebührenbuchung verbleibt ein Netto-Liquiditätszufluss von 1.582.000,00 EUR.\n\n"
                "Wir bestätigen, dass die Angaben in der beigefügten CP-Liste vollständig sind und "
                "uns seit Unterzeichnung kein Kündigungsgrund, Insolvenzantrag oder eine wesentliche "
                "nachteilige Veränderung bekannt geworden ist.\n\nMit freundlichen Grüßen\nMartin Reuter\nGeschäftsführer"
            ),
            attachments=["05_Finanzierung_Sicherheiten/12_Anlage_1_Auszahlungsvoraussetzungen.xlsx"],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/14_Auszahlungsanzeigen_und_SEPA_Belege.pdf",
            "pdf",
            "Auszahlungsanzeigen und SEPA-Ausführungsbelege der Rhenus Kreditbank",
            sections=[
                _section(
                    "Kreditkonto und Prüfzweck",
                    "Bankbestätigung der Rhenus Kreditbank AG für Darlehen RK-2023-4471. Die nachstehenden Buchungen trennen die Bruttoziehungen auf dem Darlehenskonto, die Zahlungen auf das Geschäftskonto und das gesondert belastete Bearbeitungsentgelt.",
                    "Die Bestätigung wurde am 4. Juli 2023 aus dem Zahlungsverkehrssystem erstellt und am 5. Juli 2023 von Silke Brandt und Beate Abele im Vier-Augen-Prinzip unterzeichnet. Sie ersetzt keine Prüfung der in Anlage 1 dokumentierten Auszahlungsvoraussetzungen.",
                ),
                _section(
                    "Erste Tranche",
                    "Nach Freigabe PAY-2023-0317-44 wurde das Darlehenskonto am 20. März 2023 mit 1.600.000,00 EUR belastet. Unter der End-to-End-Referenz RK20234471T1 wurde derselbe Bruttobetrag dem Geschäftskonto der Kurpfalz Taxware GmbH gutgeschrieben.",
                    "Das Bearbeitungsentgelt von 18.000,00 EUR wurde am selben Tag als eigene Belastungsbuchung ENTG-RK2023-4471 auf dem Geschäftskonto vereinnahmt. Es reduzierte weder den Kapitalabruf noch die Darlehenshauptforderung. Der Netto-Liquiditätszufluss aus den beiden Kontobuchungen betrug 1.582.000,00 EUR.",
                ),
                _section(
                    "Zweite Tranche",
                    "Nach Freigabe PAY-2023-0630-19 wurde das Darlehenskonto am 3. Juli 2023 mit weiteren 800.000,00 EUR belastet. Der Betrag wurde unter der End-to-End-Referenz RK20234471T2 vollständig dem Geschäftskonto gutgeschrieben. Eine weitere Gebühr wurde nicht erhoben.",
                ),
                _section(
                    "Kontrollvermerk",
                    "Bruttoziehungen: 1.600.000,00 EUR plus 800.000,00 EUR gleich 2.400.000,00 EUR. Kontogutschriften: 2.400.000,00 EUR. Gesonderte Gebührenbelastung: 18.000,00 EUR. Gesamter Netto-Liquiditätszufluss: 2.382.000,00 EUR.",
                    "Die Buchungsreferenzen wurden mit den Kontoauszügen 21/2023 und 76/2023 der Heidelberger Volksbank abgeglichen. Rückruf oder Rücklastschrift sind im Bankjournal nicht verzeichnet.",
                ),
            ],
            tables=[
                {
                    "title": "Ausführungsjournal",
                    "headers": ["Valuta", "Vorgang", "Darlehenskonto EUR", "Geschäftskonto EUR", "Referenz", "Status"],
                    "rows": [
                        ["20.03.2023", "Bruttoauszahlung Tranche 1", 1600000, 1600000, "RK20234471T1", "ausgeführt 09:18"],
                        ["20.03.2023", "Bearbeitungsentgelt", 0, -18000, "ENTG-RK2023-4471", "gebucht 09:19"],
                        ["03.07.2023", "Bruttoauszahlung Tranche 2", 800000, 800000, "RK20234471T2", "ausgeführt 08:44"],
                        ["Kontrolle", "", 2400000, 2382000, "Differenz 18.000 EUR = Gebühr", "abgestimmt"],
                    ],
                }
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/15_Verwendungsnachweis_Tranche_1.pdf",
            "pdf",
            "Mittelverwendungs- und CP-Nachweis für die zweite Tranche",
            sections=[
                _section(
                    "Erklärung und Zeitraum",
                    "Von der Kurpfalz Taxware GmbH am 29. Juni 2023 unterzeichnete Mittelverwendungsübersicht für den Zeitraum 20. März bis 28. Juni 2023. Bezug: Darlehen RK-2023-4471, Budget FP-MIG-2023-02 und Auszahlungsvoraussetzungen der zweiten Tranche.",
                    "Geschäftsführer Martin Reuter und Prokuristin Nora Schenk bestätigen, dass die gelisteten Aufwendungen bezahlt oder zur Zahlung freigegeben, der Cloud-Migration beziehungsweise Entwicklung zugeordnet und nicht bereits in einer anderen Nachweisposition enthalten sind.",
                ),
                _section(
                    "Bankprüfung",
                    "Die Bank erkannte Belege über 1.438.600,00 EUR als vertragsgemäße Mittelverwendung an. Eine Marketingrechnung über 42.000,00 EUR wurde wegen fehlender Zuordnung zur Cloud-Migration oder Entwicklung nicht angerechnet.",
                    "Für einen Provider-Abnahmebeleg über 76.000,00 EUR lag ein vollständiger Scan vor; das Original sollte bis 14. Juli 2023 nachgereicht werden. Silke Brandt und Beate Abele genehmigten am 30. Juni 2023 den einmaligen Waiver WA-2023-06-02 nur hinsichtlich der Vorlage des Originals. Zusicherungen, Verwendungsbindung und Nachlieferungspflicht blieben unberührt.",
                ),
                _section(
                    "Meilenstein und Freigabe",
                    "Das technische Abnahmeprotokoll M2 vom 28. Juni 2023 bestätigt die Migration der Entwicklungs- und Testumgebung, den Parallelbetrieb des Regelkerns und die Wiederanlaufprobe. Die Bank bewertete damit die CP-Schwelle von 1.350.000,00 EUR und den technischen Meilenstein als erfüllt.",
                    "Diese Prüfung bestätigt die dokumentierte Verwendung für den Auszahlungsvorgang. Sie ist keine abschließende Anerkennung sämtlicher Kosten als förderfähig, bilanziell aktivierbar oder frei von Rechten Dritter.",
                ),
            ],
            tables=[
                {
                    "title": "Anerkannte Mittelverwendung",
                    "headers": ["Beleggruppe", "Zeitraum", "Eingereicht EUR", "Anerkannt EUR", "Prüfhinweis"],
                    "rows": [
                        ["Cloudprovider und Datenmigration", "03–06/2023", 524800, 524800, "einschließlich Providerbeleg 76.000 EUR mit Original-Waiver"],
                        ["Interne Entwicklungskosten", "03–06/2023", 486400, 486400, "Projektzeiten Tax Core und Mittelstand"],
                        ["Externe Entwicklung und Tests", "03–06/2023", 236900, 236900, "Rechnungen und Abnahmen vorhanden"],
                        ["Security, CI/CD und Entwicklungswerkzeuge", "03–06/2023", 190500, 190500, "Budgetgruppe Technik"],
                        ["Marketing Produktlaunch", "06/2023", 42000, 0, "nicht auf CP-Schwelle angerechnet"],
                        ["Summe", "", 1480600, 1438600, "CP-Schwelle 1.350.000 EUR überschritten"],
                    ],
                }
            ],
        ),
        _mail(
            "05_Finanzierung_Sicherheiten/16_Abruf_Tranche_2.eml",
            "Abruf der zweiten Darlehenstranche mit Mittelverwendungsnachweis",
            sender="Martin Reuter <finance@kurpfalz-taxware.example>",
            to=["Silke Brandt <silke.brandt@rhenus-kreditbank.example>"],
            cc=["Nora Schenk <nora.schenk@kurpfalz-taxware.example>", "kreditauszahlung@rhenus-kreditbank.example"],
            date="Fri, 30 Jun 2023 09:11:00 +0200",
            subject="RK-2023-4471 – Abruf Tranche 2 über 800.000 EUR / CP-Nachweise",
            body=(
                "Sehr geehrte Frau Brandt,\n\nwir rufen die zweite Tranche des Darlehens "
                "RK-2023-4471 in Höhe von 800.000,00 EUR mit Valuta am 3. Juli 2023 ab. Bitte "
                "überweisen Sie die Bruttovaluta ohne weiteren Gebührenabzug auf das bereits "
                "bestätigte Geschäftskonto bei der Heidelberger Volksbank. Die Mittel werden für "
                "Produktlaunch und Vertriebsausbau nach Budget FP-LAUNCH-2023-06 eingesetzt.\n\n"
                "Beigefügt sind die fortgeschriebene Anlage 1 und der unterzeichnete Nachweis über "
                "1.438.600,00 EUR anerkannte Verwendung der ersten Tranche. Hinsichtlich des "
                "Providerbelegs über 76.000,00 EUR bitten wir ausschließlich für das Papieroriginal "
                "um den in der Checkliste beschriebenen befristeten Waiver; der vollständige Scan "
                "liegt vor.\n\nWir bestätigen, dass keine andere Auszahlungsvoraussetzung offen ist "
                "und seit der ersten Auszahlung kein Kündigungsgrund oder Insolvenzantrag eingetreten "
                "ist.\n\nMit freundlichen Grüßen\nMartin Reuter\nGeschäftsführer"
            ),
            attachments=[
                "05_Finanzierung_Sicherheiten/12_Anlage_1_Auszahlungsvoraussetzungen.xlsx",
                "05_Finanzierung_Sicherheiten/15_Verwendungsnachweis_Tranche_1.pdf",
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/17_Schuldnerkontoauszug_Valuta.pdf",
            "pdf",
            "Kontoauszüge der Darlehensnehmerin zu den Darlehensvaluten",
            sections=[
                _section(
                    "Konto und Herkunft",
                    "Auszüge 21/2023 und 76/2023 des Geschäftskontos der Kurpfalz Taxware GmbH bei der Heidelberger Volksbank, IBAN DE44 6729 0000 0044 7711 02. Elektronischer Zweitauszug vom 5. Juli 2023 mit institutsseitiger Dokument-ID HVB-KTW-2023-771102.",
                    "Dargestellt sind nur die für die Kreditvalutierung maßgeblichen Buchungen und die jeweiligen Tagessalden. Sonstige Umsätze des Geschäftskontos wurden im Datenraum aus Datenschutz- und Prüfungsgründen ausgeblendet; die laufende Auszugsnummerierung ist erhalten.",
                ),
                _section(
                    "Abgleich",
                    "Die Gutschriften tragen dieselben End-to-End-Referenzen wie das Ausführungsjournal der Rhenus Kreditbank. Die gesonderte Entgeltbelastung ist unmittelbar nach der ersten Bruttogutschrift gebucht. Für beide Gutschriften bestehen keine Rückgabe- oder Stornobuchungen.",
                ),
            ],
            tables=[
                {
                    "title": "Valutabuchungen",
                    "headers": ["Auszug", "Buchung", "Valuta", "Buchungstext", "Betrag EUR", "Tagessaldo nach Buchung EUR", "Referenz"],
                    "rows": [
                        ["21/2023", "20.03.2023", "20.03.2023", "Rhenus Kreditbank / Darlehen Tranche 1", 1600000, 1814382.11, "RK20234471T1"],
                        ["21/2023", "20.03.2023", "20.03.2023", "Rhenus Kreditbank / Bearbeitungsentgelt", -18000, 1796382.11, "ENTG-RK2023-4471"],
                        ["76/2023", "03.07.2023", "03.07.2023", "Rhenus Kreditbank / Darlehen Tranche 2", 800000, 1252118.73, "RK20234471T2"],
                    ],
                },
                {
                    "title": "Kontrollrechnung",
                    "headers": ["Größe", "Tranche 1 EUR", "Tranche 2 EUR", "Gesamt EUR"],
                    "rows": [
                        ["Bruttogutschrift", 1600000, 800000, 2400000],
                        ["separate Gebührenbelastung", -18000, 0, -18000],
                        ["Netto-Liquiditätszufluss", 1582000, 800000, 2382000],
                    ],
                },
            ],
        ),
        _xlsx(
            "05_Finanzierung_Sicherheiten/18_Darlehenskonto_und_Saldo.xlsx",
            "Darlehenskonto RK-2023-4471 und Forderungsstand zur Verfahrenseröffnung",
            [
                {
                    "name": "Kapitalbewegungen",
                    "notes": [
                        "Kontoblatt der Rhenus Kreditbank; Soll bezeichnet eine Bruttoziehung, Haben eine kapitalmindernde Zahlung.",
                        "Die am 30.06.2026 fällige Rate über 50.000 EUR wurde nicht bezahlt und ist deshalb nicht als Tilgung gebucht.",
                    ],
                    "headers": ["Pos.", "Valuta", "Vorgang", "Soll/Bruttoziehung EUR", "Haben/Tilgung EUR", "Kapitalstand EUR", "Bankreferenz", "Beleg/Status"],
                    "rows": [
                        [1, "20.03.2023", "Auszahlung Tranche 1", 1600000, 0, "=D6-E6", "RK20234471T1", "Ausführungsbeleg 14 / Kontoauszug 17"],
                        [2, "03.07.2023", "Auszahlung Tranche 2", 800000, 0, "=F6+D7-E7", "RK20234471T2", "Ausführungsbeleg 14 / Kontoauszug 17"],
                        [3, "30.06.2024", "planmäßige Tilgung", 0, 50000, "=F7+D8-E8", "KTW-TILG-2024-02", "Zahlungseingang Rhenus 30.06.2024"],
                        [4, "30.09.2024", "planmäßige Tilgung", 0, 50000, "=F8+D9-E9", "KTW-TILG-2024-03", "Zahlungseingang Rhenus 30.09.2024"],
                        [5, "31.12.2024", "planmäßige Tilgung", 0, 50000, "=F9+D10-E10", "KTW-TILG-2024-04", "Zahlungseingang Rhenus 31.12.2024"],
                        [6, "31.03.2025", "planmäßige Tilgung", 0, 50000, "=F10+D11-E11", "KTW-TILG-2025-01", "Zahlungseingang Rhenus 31.03.2025"],
                        [7, "30.06.2025", "planmäßige Tilgung", 0, 50000, "=F11+D12-E12", "KTW-TILG-2025-02", "Zahlungseingang Rhenus 30.06.2025"],
                        [8, "30.09.2025", "planmäßige Tilgung", 0, 50000, "=F12+D13-E13", "KTW-TILG-2025-03", "Zahlungseingang Rhenus 30.09.2025"],
                        [9, "31.12.2025", "planmäßige Tilgung", 0, 50000, "=F13+D14-E14", "KTW-TILG-2025-04", "Zahlungseingang Rhenus 31.12.2025"],
                        [10, "31.03.2026", "planmäßige Tilgung", 0, 50000, "=F14+D15-E15", "KTW-TILG-2026-01", "Zahlungseingang Rhenus 31.03.2026"],
                        ["Kontrolle", "15.09.2026", "Bruttoziehungen / Tilgungen / Kapital", "=SUM(D6:D15)", "=SUM(E6:E15)", "=D16-E16", "=IF(F16=2000000,\"OK\",\"FEHLER\")", "2.400.000 - 400.000 = 2.000.000 EUR"],
                    ],
                },
                {
                    "name": "Zinsen_Gebuehren",
                    "notes": [
                        "Vertragszins 5,40 Prozent p.a.; für das Bankkontoblatt wird die vertraglich praktizierte 30/360-Methode verwendet.",
                        "Ab 20.08.2026 ist der Gesamtverzugszins von 10,40 Prozent p.a. auf das fällig gestellte Kapital angesetzt; die rechtliche Durchsetzbarkeit, die tagesgenaue Abgrenzung und insolvenzrechtliche Zinsbegrenzungen bleiben zu prüfen.",
                    ],
                    "headers": ["Pos.", "Zeitraum", "Tage 30/360", "Zinsbasis EUR", "Satz p.a.", "Soll EUR", "Bezahlt EUR", "Offen EUR", "Buchungsreferenz/Einordnung"],
                    "rows": [
                        [1, "20.03.–31.03.2023", 10, 1600000, 0.054, "=ROUND(C6*D6*E6/360,2)", "=F6", "=F6-G6", "ZINS-2023-Q1 / bezahlt 31.03.2023"],
                        [2, "01.04.–30.06.2023", 90, 1600000, 0.054, "=ROUND(C7*D7*E7/360,2)", "=F7", "=F7-G7", "ZINS-2023-Q2 / bezahlt 30.06.2023"],
                        [3, "01.07.–02.07.2023", 2, 1600000, 0.054, "=ROUND(C8*D8*E8/360,2)", "=F8", "=F8-G8", "ZINS-2023-Q3a / bezahlt 30.09.2023"],
                        [4, "03.07.–30.09.2023", 88, 2400000, 0.054, "=ROUND(C9*D9*E9/360,2)", "=F9", "=F9-G9", "ZINS-2023-Q3b / bezahlt 30.09.2023"],
                        [5, "01.10.–31.12.2023", 90, 2400000, 0.054, "=ROUND(C10*D10*E10/360,2)", "=F10", "=F10-G10", "ZINS-2023-Q4 / bezahlt 31.12.2023"],
                        [6, "01.01.–31.03.2024", 90, 2400000, 0.054, "=ROUND(C11*D11*E11/360,2)", "=F11", "=F11-G11", "ZINS-2024-Q1 / bezahlt 31.03.2024"],
                        [7, "01.04.–30.06.2024", 90, 2400000, 0.054, "=ROUND(C12*D12*E12/360,2)", "=F12", "=F12-G12", "ZINS-2024-Q2 / bezahlt 30.06.2024"],
                        [8, "01.07.–30.09.2024", 90, 2350000, 0.054, "=ROUND(C13*D13*E13/360,2)", "=F13", "=F13-G13", "ZINS-2024-Q3 / bezahlt 30.09.2024"],
                        [9, "01.10.–31.12.2024", 90, 2300000, 0.054, "=ROUND(C14*D14*E14/360,2)", "=F14", "=F14-G14", "ZINS-2024-Q4 / bezahlt 31.12.2024"],
                        [10, "01.01.–31.03.2025", 90, 2250000, 0.054, "=ROUND(C15*D15*E15/360,2)", "=F15", "=F15-G15", "ZINS-2025-Q1 / bezahlt 31.03.2025"],
                        [11, "01.04.–30.06.2025", 90, 2200000, 0.054, "=ROUND(C16*D16*E16/360,2)", "=F16", "=F16-G16", "ZINS-2025-Q2 / bezahlt 30.06.2025"],
                        [12, "01.07.–30.09.2025", 90, 2150000, 0.054, "=ROUND(C17*D17*E17/360,2)", "=F17", "=F17-G17", "ZINS-2025-Q3 / bezahlt 30.09.2025"],
                        [13, "01.10.–31.12.2025", 90, 2100000, 0.054, "=ROUND(C18*D18*E18/360,2)", "=F18", "=F18-G18", "ZINS-2025-Q4 / bezahlt 31.12.2025"],
                        [14, "01.01.–31.03.2026", 90, 2050000, 0.054, "=ROUND(C19*D19*E19/360,2)", "=F19", "=F19-G19", "ZINS-2026-Q1 / bezahlt 31.03.2026"],
                        [15, "01.04.–30.06.2026", 90, 2000000, 0.054, "=ROUND(C20*D20*E20/360,2)", 0, "=F20-G20", "ZINS-2026-Q2 / fällig 30.06.2026, unbezahlt"],
                        [16, "01.07.–19.08.2026", 49, 2000000, 0.054, "=ROUND(C21*D21*E21/360,2)", 0, "=F21-G21", "laufender Vertragszins bis Fälligstellung"],
                        [17, "01.07.–19.08.2026", 49, 77000, 0.104, "=ROUND(C22*D22*E22/360,2)", 0, "=F22-G22", "Verzugszins auf Rate 50.000 + Quartalszins 27.000"],
                        [18, "20.08.–14.09.2026", 25, 2000000, 0.104, "=ROUND(C23*D23*E23/360,2)", 0, "=F23-G23", "Gesamtverzugszins nach Zugang der Fälligstellung"],
                        ["Kontrolle", "bis Eröffnung 15.09.2026, 09:00", "", "", "", "=SUM(F6:F23)", "=SUM(G6:G23)", "=SUM(H6:H23)", "Soll = bezahlt + offen"],
                    ],
                },
                {
                    "name": "Gebuehr_Valuta",
                    "notes": ["Das Bearbeitungsentgelt wurde als eigene Kontobelastung vereinnahmt; es mindert weder die Bruttoziehung noch die Darlehenshauptforderung."],
                    "headers": ["Vorgang", "Bruttokapital EUR", "separate Gebühr EUR", "Netto-Liquidität EUR", "Kontrolle", "Beleg"],
                    "rows": [
                        ["Tranche 1 / 20.03.2023", 1600000, 18000, "=B6-C6", "=IF(B6=C6+D6,\"OK\",\"FEHLER\")", "Belege 13, 14 und 17"],
                        ["Tranche 2 / 03.07.2023", 800000, 0, "=B7-C7", "=IF(B7=C7+D7,\"OK\",\"FEHLER\")", "Belege 14, 16 und 17"],
                        ["Gesamt", "=SUM(B6:B7)", "=SUM(C6:C7)", "=SUM(D6:D7)", "=IF(B8=C8+D8,\"OK\",\"FEHLER\")", "2.400.000 = 18.000 + 2.382.000 EUR"],
                    ],
                },
                {
                    "name": "Saldo_15_09_2026",
                    "notes": [
                        "Forderungsstand der Bank unmittelbar vor Verfahrenseröffnung; nach Verfahrenseröffnung anfallende Zinsen und Kosten sind nicht eingerechnet.",
                        "Die Aufstellung ist weder Anerkenntnis der insolvenzrechtlichen Einordnung noch Nachweis eines Absonderungsrechts oder einer zulässigen Verwertung.",
                    ],
                    "headers": ["Position", "Betrag EUR", "Formel/Quelle", "Status", "Rechtlicher Prüfpunkt"],
                    "rows": [
                        ["Darlehenskapital", "=Kapitalbewegungen!F16", "2.400.000 Ziehungen abzüglich 400.000 Tilgungen", "fällig gestellt", "Wirksamkeit und Reichweite der Kündigung prüfen"],
                        ["Zinsen bis Eröffnung", "=Zinsen_Gebuehren!H24", "Kontoblatt Zinsen_Gebuehren", "offen", "Zinslauf und 30/360-Abgrenzung prüfen"],
                        ["Bearbeitungsentgelt", 0, "18.000 EUR am 20.03.2023 vollständig verbucht", "kein offener Betrag", "keine erneute Addition zur Hauptforderung"],
                        ["Gesamtforderung vor Sicherheitenanrechnung", "=SUM(B6:B8)", "Kapital plus offene Zinsen", "zur Tabelle angemeldet", "Feststellung im Insolvenzverfahren offen"],
                        ["bei der Bank eingegangene Sicherheitenerlöse", 0, "Sicherheitenkonto bis 22.10.2026 ohne Eingang", "keine Anrechnung", "Masseeingänge und Erlöszuordnung gesondert prüfen"],
                        ["Nettoforderung nach Bankeingängen", "=B9-B10", "keine Zahlung an Bank dokumentiert", "vorläufig", "Sicherheitenabrechnung Blatt 21 bleibt fortzuschreiben"],
                        ["Kontrolle", "=IF(ROUND(B11,2)=2057234.42,\"OK\",\"FEHLER\")", "Sollwert 2.057.234,42 EUR", "rechnerisch", "keine Aussage zu Rang oder Durchsetzbarkeit"],
                    ],
                },
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/19_Mahnung_Stillhaltebitte_und_Bankantwort.pdf",
            "pdf",
            "Mahnung, Stillhaltebitte und befristete Bankantwort",
            sections=[
                _section(
                    "Mahnung der Bank vom 17. Juli 2026",
                    "Die Rhenus Kreditbank AG mahnte unter dem Aktenzeichen RK-2023-4471/M1 die am 30. Juni 2026 fällige Tilgungsrate von 50.000,00 EUR und den Quartalszins von 27.000,00 EUR, zusammen 77.000,00 EUR. Bis zum Tagesabschluss 16. Juli war kein Eingang verbucht.",
                    "Die Bank setzte vorsorglich eine Abhilfefrist von zehn Bankarbeitstagen ab Zugang, spätestens bis 3. August 2026, und wies auf die Kündigungstatbestände des Darlehensvertrags hin. Das Schreiben wurde am 17. Juli als Einwurf-Einschreiben und parallel als signierte PDF an finance@kurpfalz-taxware.example versandt; der Zustellnachweis weist den Einwurf am 20. Juli um 09:12 Uhr aus.",
                ),
                _section(
                    "Fristablauf und Kontoprüfung",
                    "Die Restrukturierungsakte vermerkt am 4. August 2026: kein Zahlungseingang, keine Rücklastschrift und keine belastbare Zahlungszusage. Die zehn Bankarbeitstage nach dokumentiertem Zugang waren mit Ablauf des 3. August verstrichen. Die ausstehende Juni-Rate ist innerhalb des Kapitalstands von 2.000.000,00 EUR enthalten und wird nicht zusätzlich zum Kapital addiert.",
                ),
                _section(
                    "Stillhaltebitte der Darlehensnehmerin vom 11. August 2026",
                    "Geschäftsführer Martin Reuter teilte der Bank per signierter E-Mail um 08:17 Uhr mit, dass die Gesellschaft die fälligen 77.000,00 EUR derzeit nicht zahlen könne. Er verwies auf den an diesem Morgen beim Amtsgericht Heidelberg eingereichten Eigenantrag wegen Zahlungsunfähigkeit und Überschuldung und bat darum, bis 15. September 2026 von Kündigung, Offenlegung der Forderungsabtretung und Verwertung der IP-Sicherheit abzusehen.",
                    "Die Nachricht ging um 08:18 Uhr im Funktionspostfach workout@rhenus-kreditbank.example ein und wurde um 08:31 Uhr im System RKB-DMS-2026-8841 registriert. Beigefügt waren die Eingangsbestätigung des Insolvenzgerichts und eine 13-Wochen-Liquiditätsübersicht. Eine konkrete Zahlung oder zusätzliche Sicherheit wurde nicht angeboten.",
                ),
                _section(
                    "Antwort der Bank vom 12. August 2026",
                    "Silke Brandt und Jan Küster bestätigten für die Bank den Eingang, lehnten Stundung, Erlass und einen Stillhaltezeitraum bis 15. September jedoch ab. Ausschließlich zur Abstimmung mit dem zu bestellenden vorläufigen Verwalter sagte die Bank zu, bis einschließlich 18. August 2026 keine technische Selbsthilfe, Drittschuldneransprache oder Verwertungshandlung einzuleiten.",
                    "Die Antwort bezeichnet diese kurze operative Zurückhaltung ausdrücklich nicht als Verzicht auf Kündigungs-, Fälligstellungs-, Sicherungs- oder Anfechtungsrechte und nicht als Fortsetzungszusage. Ob und in welchem Umfang diese Erklärung trotz des Wortlauts eine rechtlich relevante Stillhaltewirkung entfaltet, bleibt offen.",
                ),
                _section(
                    "Zugang und Aktenkette",
                    "Die Bankantwort wurde am 12. August um 14:06 Uhr per signierter E-Mail an Martin Reuter und Nora Schenk übermittelt; der Mailserver der Schuldnerin bestätigte die Annahme um 14:06:37 Uhr. Am 18. August übergab die Bank Dr. Friederike Mohn als vorläufiger Insolvenzverwalterin Kopien des Darlehensvertrags, des IP-Sicherungsvertrags und der Forderungsabtretung. Eine Zustimmung zur Fortführung oder Veräußerung wurde dabei nicht erklärt.",
                ),
            ],
            tables=[
                {
                    "title": "Post- und Zugangsprotokoll",
                    "headers": ["Datum/Uhrzeit", "Dokument", "Absender", "Empfänger", "Nachweis", "Ergebnis"],
                    "rows": [
                        ["17.07.2026, 15:44", "Mahnung RK-2023-4471/M1", "Rhenus Kreditbank", "Kurpfalz Taxware", "Einschreiben RKB884100771", "Einwurf 20.07., 09:12"],
                        ["11.08.2026, 08:18", "Stillhaltebitte und Eigenantragsnachweis", "Kurpfalz Taxware", "Rhenus Kreditbank", "Mail-Gateway RKB-DMS-2026-8841", "angenommen und registriert"],
                        ["12.08.2026, 14:06", "Bankantwort RK-2023-4471/S1", "Rhenus Kreditbank", "Martin Reuter / Nora Schenk", "SMTP-Annahme KTW-MX-44209", "zugestellt 14:06:37"],
                        ["18.08.2026, 11:24", "Sicherheitenkopien", "Rhenus Kreditbank", "Dr. Friederike Mohn", "Datenraumquittung MOHN-DR-1198", "heruntergeladen 12:03"],
                    ],
                }
            ],
        ),
        _doc(
            "05_Finanzierung_Sicherheiten/20_Kuendigung_Faelligstellung_Verwertungsanzeige.pdf",
            "pdf",
            "Kündigung, Fälligstellung und Anzeige der beabsichtigten Sicherheitenverwertung",
            sections=[
                _section(
                    "Erklärung der Bank vom 19. August 2026",
                    "Die Rhenus Kreditbank AG kündigt das Darlehen RK-2023-4471 aus wichtigem Grund mit sofortiger Wirkung und stellt sämtliche offenen Ansprüche fällig. Das Schreiben ist von Silke Brandt und Beate Abele gemeinschaftlich unterzeichnet und an die Kurpfalz Taxware GmbH, Geschäftsführer Martin Reuter, sowie in Kopie an die vorläufige Insolvenzverwalterin Dr. Friederike Mohn gerichtet.",
                ),
                _section(
                    "Bezeichnete Kündigungsgründe",
                    "Die Bank stützt die Kündigung auf die seit 30. Juni ausstehende Tilgungsrate und den Quartalszins, den ergebnislosen Ablauf der bis 3. August gesetzten Abhilfefrist, die im Schreiben vom 11. August erklärte gegenwärtige Zahlungsunfähigkeit und den Eigenantrag auf Eröffnung eines Insolvenzverfahrens. Sie hält fest, dass ihre operative Zurückhaltung bis 18. August keine Stundung oder Vertragsänderung war.",
                    "Die Frage, ob einzelne vertragliche Kündigungs- oder Verwertungsregelungen im Insolvenzkontext wirksam, durchsetzbar oder zwingend beschränkt sind, wird im Schreiben nicht abschließend beantwortet und bleibt ausdrücklich rechtlicher Prüfung vorbehalten.",
                ),
                _section(
                    "Forderungsbetrag am 19. August 2026",
                    "Die Bank beziffert vorläufig 2.000.000,00 EUR Kapital, 27.000,00 EUR unbezahlten Quartalszins, 14.700,00 EUR laufenden Vertragszins vom 1. Juli bis 19. August und 1.089,98 EUR Verzugszins auf die seit 30. Juni fälligen 77.000,00 EUR. Die Summe beträgt 2.042.789,98 EUR. Die unbezahlte Tilgungsrate von 50.000,00 EUR ist Teil des genannten Kapitalstands und wird nicht nochmals addiert.",
                    "Ab 20. August führt das Bankkonto den vertraglichen Gesamtverzugszins von 10,40 Prozent jährlich auf den fällig gestellten Kapitalbetrag. Die Abrechnung zum 15. September 2026 befindet sich in Beleg 18; spätere Zinsen, Kosten und insolvenzrechtliche Beschränkungen sind dort nicht vorweggenommen.",
                ),
                _section(
                    "IP-Sicherheit und Verwertungsanzeige",
                    "Unter Bezug auf den Sicherungsvertrag vom 15. März 2023 zeigt die Bank die beabsichtigte Verwertung der dort bezeichneten Software-Nutzungsrechte an. Die Schuldnerin soll Repositorien, Backups, Hashlisten, Dokumentationen, Build-Umgebungen und Zugänge unverändert erhalten und außerhalb des gewöhnlichen Fortführungsbetriebs keine Rechte übertragen, ausschließlich lizenzieren, weiter belasten oder aufgeben.",
                    "Die Bank kündigt keine technische Selbsthilfe und keine sofortige Abschaltung an. Sie verlangt eine abgestimmte Bestandsaufnahme mit der vorläufigen Verwalterin und behält Lizenzierung, Verkauf oder Übertragung nur im rechtlich zulässigen Verfahren vor. Umfang, Priorität, Insolvenzfestigkeit und Verwertungsbefugnis der IP-Sicherheit bleiben streitig und sind anhand der Entwickler-, Vorbestands- und Drittkomponentenakten zu prüfen.",
                ),
                _section(
                    "Forderungsabtretung und Einziehungsbefugnis",
                    "Die Bank widerruft gegenüber der Schuldnerin mit Zugang die Einziehungsbefugnis aus der Sicherungsabtretung vom 1. Februar 2024 und fordert eine taggleiche Debitorenliste, Zahlungseingangsübersicht und Kennzeichnung sämtlicher Einwendungen. Sie nennt das Sicherheitenkonto mit der Endung 2208 als vorgesehenes Zielkonto.",
                    "Das Schreiben selbst ist keine Offenlegung gegenüber einzelnen Kunden. Die Bank erklärt, dass vor einer Drittschuldneransprache die Vertragsverbote, der Stand des Insolvenzantrags und die Abstimmung mit der vorläufigen Verwalterin geprüft werden. Bis zur Verfahrenseröffnung ist keine versandte individuelle Zahlungsumleitung aktenkundig; die rechtliche Wirkung des Widerrufs und späterer Masseeingänge bleibt offen.",
                ),
                _section(
                    "Zugang und Vorbehalte",
                    "Der Kurier übergab das Original am 20. August 2026 um 08:41 Uhr am Geschäftssitz der Schuldnerin an Office-Managerin Eva Hartmann; Empfangsbeleg CNR-260820-441 ist beigefügt. Die vorläufige Verwalterin erhielt um 08:05 Uhr eine qualifiziert signierte PDF über das besondere elektronische Postfach und bestätigte um 09:22 Uhr die Kenntnisnahme.",
                    "Eine Freigabe der Sicherheiten, Zustimmung zu einem Asset Deal oder Verzichtserklärung ist mit dem Schreiben nicht verbunden.",
                ),
            ],
            tables=[
                {
                    "title": "Vorläufige Forderungsaufstellung zum 19.08.2026",
                    "headers": ["Position", "Betrag EUR", "Zeitraum/Basis", "Hinweis"],
                    "rows": [
                        ["Kapital", 2000000, "2.400.000 Ziehungen ./. 400.000 Tilgungen", "50.000 Juni-Rate darin enthalten"],
                        ["Quartalszins Q2/2026", 27000, "90/360 × 2.000.000 × 5,40 %", "fällig 30.06.2026"],
                        ["laufender Vertragszins", 14700, "49/360 × 2.000.000 × 5,40 %", "01.07.–19.08.2026"],
                        ["Verzugszins auf 77.000 EUR", 1089.98, "49/360 × 77.000 × 10,40 %", "vorläufig"],
                        ["Gesamt", 2042789.98, "", "ohne spätere Zinsen und Kosten"],
                    ],
                },
                {
                    "title": "Zustellung",
                    "headers": ["Empfänger", "Übermittlung", "Zugang", "Nachweis"],
                    "rows": [
                        ["Kurpfalz Taxware GmbH", "Originalkurier", "20.08.2026, 08:41", "CNR-260820-441 / Eva Hartmann"],
                        ["Dr. Friederike Mohn, vorläufige Verwalterin", "qualifiziert signierte PDF", "20.08.2026, 08:05", "eBO-Quittung RKB-EB-2026-198"],
                    ],
                },
            ],
        ),
        _xlsx(
            "05_Finanzierung_Sicherheiten/21_Anlage_F1_und_Sicherheitenabrechnung.xlsx",
            "Anlage F-1 und vorläufige Sicherheitenabrechnung",
            [
                {
                    "name": "F-1_Stand_31_01_2024",
                    "notes": [
                        "Paraphierte administrative Startliste zur Sicherungsabtretung vom 01.02.2024; die Abtretungsklausel verweist für die Bestimmbarkeit zusätzlich auf das fortlaufende Debitorenregister.",
                        "Die Liste beantwortet nicht abschließend, ob einzelne Abtretungsverbote, Einwendungen oder spätere Vertragsänderungen die Sicherheit beschränken.",
                    ],
                    "headers": ["Debitor", "Kunde", "Vertrag", "Leistungsarten", "Vertragsbeginn", "Abtretungsbeschränkung laut Register", "Anzeige vorgesehen", "Stand 31.01.2024"],
                    "rows": [
                        [1017, "Müller & Reiter", "MR-2024-01", "Lizenz/Pflege", "01.02.2024", "Zahlungsabtretung zulässig; Vertragsübertragung zustimmungspflichtig", "Top 25", "Vertrag unterzeichnet"],
                        [1029, "Auer & Hain", "AH-2022-09", "Lizenz/Hosting", "01.10.2022", "Anzeige in Textform vorgesehen", "Top 25", "laufend"],
                        [1088, "Neckarblick Treuhand", "NT-2023-11", "Lizenz/Pflege", "01.12.2023", "vertragliches Abtretungsverbot vermerkt", "nur nach Legal-Prüfung", "laufend"],
                        [1112, "Schwarz & Vetter", "SV-2021-03", "Lizenz/Pflege", "01.04.2021", "kein Verbot im Register", "Top 25", "laufend"],
                        [1134, "Kanzlei Ufer & Sohn", "KU-2020-04", "Jahreslizenz/Support", "01.05.2020", "Einwendungen bleiben erhalten", "Top 25", "laufend"],
                        [1168, "Steuerteam Plankstadt", "SP-2021-08", "Pflege/Support", "01.09.2021", "kein Verbot im Register", "Top 25", "laufend"],
                        [1192, "Kanzlei Marktbrücke", "KM-2022-06", "Migration/Pflege", "01.07.2022", "Projektanteile gesondert abzugrenzen", "nach Abgrenzung", "laufend"],
                        [1211, "Treuhand am Schloss", "TS-2020-12", "Pflege", "01.01.2021", "kein Verbot im Register", "Top 25", "laufend"],
                        ["Kontrolle", "8 Debitoren", "", "", "", "", "", "Startliste; spätere Kunden über Monatsregister"],
                    ],
                },
                {
                    "name": "Hauptforderung_15_09",
                    "notes": ["Übernahme aus Beleg 18; der Betrag ist eine Bankrechnung und keine Feststellung zur Tabelle oder zum Rang."],
                    "headers": ["Position", "Betrag EUR", "Quelle", "Anrechnung", "Prüfstatus"],
                    "rows": [
                        ["Kapital", 2000000, "18_Darlehenskonto_und_Saldo / Kapitalbewegungen", 0, "Fälligkeit und Anmeldung prüfen"],
                        ["offene Zinsen bis Eröffnung", 57234.42, "18_Darlehenskonto_und_Saldo / Zinsen_Gebuehren", 0, "Berechnung und insolvenzrechtliche Behandlung prüfen"],
                        ["Gesamtforderung", "=SUM(B6:B7)", "Kontrollsumme", "=SUM(D6:D7)", "vorläufig 2.057.234,42 EUR"],
                        ["bei Bank eingegangene Sicherheitenerlöse", 0, "Sicherheitenkonto ...2208", 0, "bis 22.10.2026 kein Eingang"],
                        ["Nettoforderung nach Bankeingängen", "=B8-B9", "", "=D8+D9", "keine Anrechnung von Masseeingängen vor Rechtsklärung"],
                        ["IP-Haftungsobergrenze laut Sicherungsvertrag", 3200000, "Vertrag 15.03.2023", "", "zuzüglich Verwertungskosten; keine Wertzusage"],
                        ["Kontrolle", "=IF(ROUND(B10,2)=2057234.42,\"OK\",\"FEHLER\")", "Sollwert", "", "rechnerisch"],
                    ],
                },
                {
                    "name": "Sicherheiten_22_10",
                    "notes": [
                        "Arbeitsstand der Bank vom 22.10.2026; Werte verschiedener Gegenstände dürfen ohne Rechts- und Erlöszuordnung nicht addiert oder mit der Hauptforderung saldiert werden.",
                        "Der APA ist unterzeichnet, aber für den 28.10.2026 noch nicht vollzogen; die vertragliche Kaufpreiszuordnung ist keine anerkannte Sicherheitenbewertung.",
                    ],
                    "headers": ["Sicherheit/Position", "Nominal/Indikator EUR", "davon streitig EUR", "Bankeingang EUR", "Stichtag/Quelle", "Einordnung/offener Punkt"],
                    "rows": [
                        ["Software und Dokumentation", 1050000, "", 0, "APA-Zuordnung 19.10.2026", "kein Verwertungserlös; Rechteumfang, Vorrang und Erlöszuordnung offen"],
                        ["offene Kundenforderungen brutto", 616450, 97050, 0, "OP-Matrix 30.09.2026", "Nominalwert; Einwendungen und Abtretungsverbote prüfen"],
                        ["davon nach Eröffnung fakturiert", 68420, "", 0, "OP-Matrix 30.09.2026", "im Bruttobestand enthalten; Entstehung und Massezuordnung prüfen"],
                        ["nach Eröffnung auf Schuldnerkonten eingegangen", 43316, 7140, 0, "Kontoumsatzliste bis 02.10.2026", "7.140 EUR Projektleistung; übrige Abtretungsreichweite ebenfalls offen"],
                        ["Bank-Sicherheitenkonto ...2208", 0, 0, 0, "Kontenstatus 22.10.2026", "kein Drittschuldner zahlte an die Bank"],
                        ["rechnerisch unbestrittener OP-Nominalwert", "=B7-C7", 0, 0, "616.450 ./. 97.050", "keine Abzinsung, Ausfallquote oder Erlösprognose"],
                        ["APA-Gesamtkaufpreis", 1850000, "", 0, "unterschriebener APA", "umfasst weitere Assets und Fortführungswerte; Closing offen"],
                    ],
                },
                {
                    "name": "Zahlungseingaenge",
                    "notes": ["Kontrollauszug der acht identifizierten Eingänge; sämtliche Beträge wurden auf Schuldner- oder Massekonten gebucht, nicht an die Bank gezahlt."],
                    "headers": ["Datum", "Kunde", "Rechnung/Zweck", "Betrag EUR", "Kategorie", "Folgekonto", "Bankanrechnung", "Rechts-/Abgrenzungsfrage"],
                    "rows": [
                        ["16.09.2026", "Kurpfalz Logistik", "KTW-2026-8990", 5117, "Cloud", "Massekonto-Sweep 19.09.", 0, "Abtretung und Absonderung offen"],
                        ["18.09.2026", "Auer & Hain", "KTW-2026-8971", 1725.5, "Lizenz/Hosting", "Massekonto 21.09.", 0, "Abtretung und Einwendungen offen"],
                        ["22.09.2026", "Müller & Reiter", "KTW-2026-8870", 5533.5, "Pflege", "Massekonto-Sweep 23.09.", 0, "Anzeige 2024; Erlöszuordnung offen"],
                        ["24.09.2026", "Weingut Sonnenhang", "Teilzahlung Migration", 7140, "Projekt", "Massekonto 25.09.", 0, "reine Projektforderung möglicherweise nicht erfasst"],
                        ["28.09.2026", "Schwarz & Vetter", "KTW-2026-9002", 3094, "Pflege", "Massekonto-Sweep 30.09.", 0, "Anzeige 2024; Erlöszuordnung offen"],
                        ["01.10.2026", "PfalzForm", "KTW-2026-9121", 9282, "Cloud", "Massekonto-Sweep 02.10.", 0, "später Vertrag; Monatsregister und Anzeige offen"],
                        ["02.10.2026", "Treuhand am Schloss", "Pflege 10/26", 4641, "Pflege", "Massekonto 05.10.", 0, "Entstehung nach Eröffnung prüfen"],
                        ["06.10.2026", "Rheinauer Pumpenbau", "Cloud September Nachlauf", 6783, "Cloud", "Massekonto-Sweep 07.10.", 0, "später Vertrag; Abtretungsreichweite offen"],
                        ["Kontrolle", "", "", "=SUM(D6:D13)", "", "", "=SUM(G6:G13)", "43.316 EUR identifiziert; 0 EUR bei Bank"],
                    ],
                },
                {
                    "name": "Kontrolle_offene_Punkte",
                    "notes": ["Die Liste hält bewusst Rechts- und Tatsachenfragen offen und ist vor jeder Verwertung, Forderungsanmeldung oder Kaufpreisfreigabe fortzuschreiben."],
                    "headers": ["Kontrolle/Frage", "Wert/Status", "Formel/Beleg", "Nächster Abgleich", "Verantwortung"],
                    "rows": [
                        ["Hauptforderung vor Sicherheitenerlösen", 2057234.42, "Blatt Hauptforderung_15_09", "Forderungsanmeldung und Zinsprüfung", "Rhenus / Verwalterin"],
                        ["bei Bank eingegangene Erlöse", 0, "Sicherheitenkonto ...2208", "laufender Kontoabgleich", "Rhenus"],
                        ["identifizierte Masseeingänge", "=Zahlungseingaenge!D14", "acht Kontobuchungen", "Rechnungs- und Leistungszeiträume einzeln zuordnen", "Verwalterin / Rhenus"],
                        ["Projektanteil in Masseeingängen", 7140, "Weingut Sonnenhang", "Abtretungsumfang nach Vertragsart prüfen", "Legal"],
                        ["unbestrittener OP-Nominalwert rechnerisch", "=Sicherheiten_22_10!B11", "616.450 ./. 97.050", "Zahlungen, Gutschriften und Ausfallquote aktualisieren", "Finance"],
                        ["IP-Wert", "nicht festgestellt", "APA-Zuordnung 1.050.000 nur Indikator", "Rechtekette, OSS, Vorbestände und Vorrang prüfen", "Legal / Technik"],
                        ["Kündigung und Widerruf Einziehungsbefugnis", "Zugang 20.08.2026 dokumentiert", "Beleg 20", "Wirksamkeit und Insolvenzfolgen prüfen", "Legal"],
                        ["Freigabe oder Bankzustimmung zum APA", "nicht dokumentiert", "Banknotiz 22.10.2026", "vor Closing 28.10.2026 klären", "Verwalterin / Rhenus"],
                        ["Nettoforderung nach tatsächlichen Bankeingängen", "=B6-B7", "nur Bankeingänge anrechenbar", "nach jeder Zahlung aktualisieren", "Rhenus"],
                    ],
                },
            ],
        ),
    ]
)


CASE["documents"].extend(
    [
        _customer_license(
            path="04_Kunden_Lizenzen/01_Lizenzvertrag_Mueller_Reiter.docx",
            title="Softwarelizenz- und Pflegevertrag Müller & Reiter",
            customer="Müller & Reiter Steuerberatung PartG mbB",
            customer_address="Sofienstraße 12, 69115 Heidelberg",
            contract_date="18.01.2024",
            product="FiscusPilot Kanzlei Enterprise 4.x einschließlich Tax Core, Mandantenportal und DocFlow",
            users="bis zu 80 namentlich zugeordnete Nutzerinnen und Nutzer an drei Kanzleistandorten",
            term=(
                "Der Vertrag beginnt am 1. Februar 2024 und hat eine feste Erstlaufzeit bis 31. Januar 2027. Er verlängert sich jeweils um zwölf Monate, wenn er nicht neun Monate vor Laufzeitende gekündigt wird. Das Pflegejahr entspricht dem Kalenderjahr; im ersten und letzten Teiljahr wird zeitanteilig abgerechnet."
            ),
            fee=(
                "48.000,00 EUR netto einmalige Lizenzvergütung und 18.600,00 EUR netto jährliche Pflegevergütung, jeweils zuzüglich gesetzlicher Umsatzsteuer. Die Lizenzvergütung wurde nach Abnahme der Migration fällig; Pflege wird jährlich im Voraus berechnet"
            ),
            deployment="On-Premise-Container im Rechenzentrum der Kundin mit gesondertem Cloud-Mandantenportal",
            transfer_clause=(
                "Die Anbieterin darf diesen Vertrag oder einzelne Rechte und Pflichten daraus nur mit vorheriger schriftlicher Zustimmung der Kundin auf einen Dritten übertragen. Die Zustimmung darf nicht unbillig verweigert werden, wenn der Dritte fachlich und wirtschaftlich zur Fortführung von Pflege, Datenschutz und Vertraulichkeit in der Lage ist. Keine Zustimmung ist bei Gesamtrechtsnachfolge erforderlich. Eine Unterbeauftragung technischer Leistungen bleibt nach Maßgabe der Auftragsverarbeitungsvereinbarung möglich."
            ),
            special_clause=(
                "Der jeweils freigegebene Quellcode der On-Premise-Komponenten, Build-Anleitung und Abhängigkeitsliste werden quartalsweise bei Rhein-Neckar Escrow e.K. hinterlegt. Die Kundin kann die Herausgabe nach den Bedingungen des Escrow-Nachtrags verlangen, insbesondere wenn ein Insolvenzverfahren über das Vermögen der Anbieterin eröffnet wird und Pflegeleistungen nicht binnen 30 Kalendertagen nach schriftlicher Aufforderung fortgeführt werden. Der Nachtrag bestimmt eigenständig den Umfang einer zulässigen Nutzung nach Herausgabe."
            ),
            customer_signatory="StB Dr. Helena Müller, Partnerin",
            vendor_signatory="Martin Reuter, Geschäftsführer",
        ),
        _customer_license(
            path="04_Kunden_Lizenzen/02_Lizenzvertrag_PfalzForm.docx",
            title="Cloud-Abonnement PfalzForm Maschinenbau",
            customer="PfalzForm Maschinenbau GmbH",
            customer_address="Floßwörthstraße 48, 68199 Mannheim",
            contract_date="06.05.2025",
            product="FiscusPilot Mittelstand Cloud mit LedgerFlow, Cash View und Steuerterminkalender",
            users="bis zu 120 aktive Accounts einschließlich fünf Administratoren",
            term=(
                "Der Vertrag beginnt am 1. Juni 2025 und läuft zunächst 24 Monate. Danach verlängert er sich auf unbestimmte Zeit und kann mit drei Monaten Frist zum Monatsende gekündigt werden. Für die ersten 24 Monate ist eine ordentliche Kündigung ausgeschlossen."
            ),
            fee=(
                "7.800,00 EUR netto je Monat zuzüglich gesetzlicher Umsatzsteuer, davon 6.900,00 EUR für Cloud-Lizenz und Betrieb sowie 900,00 EUR für Premium-Support. Mehrnutzer werden mit 42,00 EUR netto je aktivem Account und Monat abgerechnet"
            ),
            deployment="mandantengetrennter Cloudbetrieb in deutschen Rechenzentren",
            transfer_clause=(
                "Die Anbieterin darf den Vertrag auf ein verbundenes Unternehmen oder auf einen Erwerber des gesamten FiscusPilot-Mittelstand-Geschäfts übertragen, wenn sie die Kundin mindestens 30 Tage vorher in Textform informiert und der neue Anbieter die Datenschutz-, Verfügbarkeits- und Supportpflichten übernimmt. Führt der Wechsel nachweisbar zu einer wesentlichen Verschlechterung, kann die Kundin innerhalb von 30 Tagen nach Information zum Wechselzeitpunkt kündigen. Andere Übertragungen bedürfen der Zustimmung der Kundin."
            ),
            special_clause=(
                "Für den produktiven LedgerFlow-Import werden die in Anlage 3 bezeichneten ERP-Felder verarbeitet. Änderungen des Mapping-Schemas werden zunächst in einer Testumgebung bereitgestellt. Die Kundin erhält monatlich einen verschlüsselten Datenexport; Quellcode oder Build-Unterlagen sind nicht geschuldet."
            ),
            customer_signatory="Katrin Damm, kaufmännische Geschäftsführerin",
            vendor_signatory="Nora Schenk, Prokuristin",
        ),
        _customer_license(
            path="04_Kunden_Lizenzen/03_Lizenzvertrag_Auer_Hain.docx",
            title="Lizenzvertrag Steuerkanzlei Auer & Hain",
            customer="Auer & Hain Steuerberatungsgesellschaft mbH",
            customer_address="Mannheimer Straße 29, 68723 Schwetzingen",
            contract_date="22.09.2022",
            product="FiscusPilot Kanzlei Professional 3.8 mit Mandantenportal",
            users="25 Beschäftigte und bis zu 300 Mandantenzugänge",
            term=(
                "Der Vertrag beginnt am 1. Oktober 2022 und läuft zwölf Monate. Er verlängert sich jeweils um weitere zwölf Monate, wenn nicht eine Partei mit sechs Monaten Frist zum Laufzeitende in Textform kündigt."
            ),
            fee=(
                "1.450,00 EUR netto je Monat zuzüglich gesetzlicher Umsatzsteuer; enthalten sind Pflege, Hosting des Mandantenportals und fünf Supportstunden je Quartal. Weitere Leistungen werden mit 145,00 EUR netto je Stunde berechnet"
            ),
            deployment="lokale Kanzleiinstallation des Regelkerns mit gehostetem Mandantenportal",
            transfer_clause=(
                "Eine Abtretung einzelner Zahlungsansprüche der Anbieterin ist zulässig; die Kundin ist darüber in Textform zu unterrichten und behält ihre Einwendungen. Der Übergang des gesamten Vertrags auf einen Erwerber der Produktlinie ist der Kundin vorab mitzuteilen. Widerspricht die Kundin innerhalb von vier Wochen aus einem wichtigen, in der Person des Erwerbers liegenden Grund, werden die Parteien eine Fortführungs- oder Beendigungslösung abstimmen."
            ),
            special_clause=(
                "Bei dauerhafter Einstellung des Mandantenportals stellt die Anbieterin einen vollständigen Datenexport und eine Beschreibung der Exportfelder bereit. Ein Anspruch auf Herausgabe von Quellcode wird nicht vereinbart. Die lokale Installation darf nach Vertragsende für reine Lesefunktionen weitere sechs Monate betrieben werden."
            ),
            customer_signatory="StB Rafael Auer, Geschäftsführer",
            vendor_signatory="Martin Reuter, Geschäftsführer",
        ),
        _xlsx(
            "04_Kunden_Lizenzen/04_Kundenvertragsmatrix.xlsx",
            "Matrix wesentlicher Kundenverträge und Überleitungsklauseln",
            [
                {
                    "name": "Top_Kunden",
                    "headers": ["Kunde", "Ort", "Produkt", "ARR netto EUR", "Vertragsstand", "Überleitungsklausel", "Mitteilung/Zustimmung", "Status 21.10."],
                    "rows": [
                        ["Müller & Reiter PartG mbB", "Heidelberg", "Kanzlei Enterprise", 18600, "18.01.2024", "vorherige schriftliche Zustimmung; Gesamtrechtsnachfolge ausgenommen", "Zustimmung", "nicht erteilt; Escrow-Mail eingegangen"],
                        ["PfalzForm Maschinenbau GmbH", "Mannheim", "Mittelstand Cloud", 93600, "06.05.2025", "Produktgeschäftserwerber bei 30-Tage-Information", "Information", "Entwurf Mitteilung, nicht versandt"],
                        ["Auer & Hain StBG mbH", "Schwetzingen", "Kanzlei Professional", 17400, "22.09.2022", "Vorabmitteilung; Widerspruch aus wichtigem Grund", "Mitteilung", "keine Mitteilung dokumentiert"],
                        ["Neckarblick Treuhand KG", "Heidelberg", "Kanzlei Enterprise", 42800, "11.11.2023", "Abtretung nur mit Zustimmung außer Konzern", "Zustimmung", "Telefonnotiz positiv, Schriftform offen"],
                        ["Rheinauer Pumpenbau GmbH", "Mannheim", "Mittelstand Cloud", 68400, "02.02.2026", "Übertragung Produktbereich nach Information", "Information", "Schreiben vorbereitet"],
                        ["Weingut Sonnenhang KG", "Deidesheim", "Mittelstand Cloud", 22800, "04.07.2025", "keine ausdrückliche Klausel im Bestellformular", "unklar", "AGB-Fassung 2024 fehlt"],
                        ["Schwarz & Vetter Rechtsanwälte PartG mbB", "Heidelberg", "Kanzlei Professional", 31200, "17.03.2021", "Zustimmung für Vertragsübernahme", "Zustimmung", "Anfrage 20.10. versandt"],
                        ["Kurpfalz Logistik GmbH", "Hockenheim", "Mittelstand Cloud", 51600, "09.09.2024", "verbundene Unternehmen oder Betriebserwerber", "Information", "nicht dokumentiert"],
                    ],
                },
                {
                    "name": "Vertragsunterlagen",
                    "headers": ["Kunde", "Hauptvertrag", "Anlagen vollständig", "AVV", "Letzte Rechnung", "Abtretungsanzeige", "Datenraumhinweis"],
                    "rows": [
                        ["Müller & Reiter", "Originalscan", "Anlagen 1–3 und Escrow-Nachtrag", "unterzeichnet", "09/2026", "Bestätigung 2024 vorhanden", "Escrow-Hinterlegung Q2/2026 fehlt"],
                        ["PfalzForm", "Originalscan", "Anlagen 1–3", "unterzeichnet", "Q4/2026", "keine Kundenbestätigung", "Cloud-Export aktuell"],
                        ["Auer & Hain", "Originalscan", "Anlage 2 fehlt", "unterzeichnet", "10/2026", "Versandprotokoll 2024", "Bestellformular im CRM"],
                        ["Neckarblick Treuhand", "PDF mit Signatur", "Preisblatt fehlt", "unterzeichnet", "10/2026", "keine", "Telefonnotiz ohne Teilnehmer"],
                        ["Rheinauer Pumpenbau", "E-Signatur", "vollständig", "unterzeichnet", "10/2026", "keine", "Mitteilungsentwurf"],
                        ["Weingut Sonnenhang", "Bestellformular", "AGB-Verweis", "unterzeichnet", "10/2026", "keine", "AGB nicht im Kundenordner"],
                    ],
                },
                {
                    "name": "Umsatzabgleich",
                    "headers": ["Kundengruppe", "Verträge", "ARR CRM EUR", "ARR Buchhaltung EUR", "Differenz EUR", "Bemerkung"],
                    "rows": [
                        ["Kanzlei Cloud", 105, 1248000, 1233600, -14400, "Gutschriften und pausierte Accounts"],
                        ["Kanzlei On-Premise", 44, 612000, 619800, 7800, "Projektpflege in Buchhaltung enthalten"],
                        ["Mittelstand Cloud", 83, 1189200, 1166400, -22800, "zwei Kündigungen noch im CRM"],
                        ["Mobile Pilot", 18, 75600, 68400, -7200, "drei unberechnete Pilotmonate"],
                    ],
                },
            ],
        ),
        _mail(
            "04_Kunden_Lizenzen/05_Mail_Kunde_Source_Escrow.eml",
            "Kundenmail zu Escrow und angekündigtem Anbieterwechsel",
            sender="Dr. Helena Müller <helena.mueller@mueller-reiter.example>",
            to=["Dr. Friederike Mohn <mohn@insolvenzkanzlei-mohn.example>"],
            cc=["it@mueller-reiter.example", "nora.schenk@kurpfalz-taxware.example"],
            date="Wed, 21 Oct 2026 15:36:00 +0200",
            subject="FiscusPilot: Escrow-Hinterlegung und Anfrage zur Vertragsübernahme",
            body=(
                "Sehr geehrte Frau Dr. Mohn,\n\nwir haben heute von Frau Schenk erfahren, dass das "
                "FiscusPilot-Geschäft möglicherweise kurzfristig auf Weinberg Digital Solutions "
                "übergehen soll. Unser Vertrag vom 18. Januar 2024 sieht für eine Vertragsübernahme "
                "unsere vorherige schriftliche Zustimmung vor. Eine Entscheidung können wir erst "
                "treffen, wenn uns Betriebskonzept, Ansprechpartner, Datenschutzunterlagen und "
                "Supportzusagen der Erwerberin vorliegen.\n\nBitte teilen Sie außerdem mit, ob der "
                "Quellcode-Stand für das dritte Quartal 2026 bei Rhein-Neckar Escrow hinterlegt wurde. "
                "Der Escrow-Dienst hat auf unsere gestrige Anfrage noch nicht geantwortet. Wir möchten "
                "den Betrieb stabil halten und bitten um einen Gesprächstermin vor einem Vollzug.\n\n"
                "Mit freundlichen Grüßen\nDr. Helena Müller"
            ),
            attachments=["04_Kunden_Lizenzen/01_Lizenzvertrag_Mueller_Reiter.docx"],
        ),
    ]
)


CASE["documents"].extend(
    [
        _employment_contract(
            path="03_Personal_Rechtekette/01_Arbeitsvertrag_Lena_Vogt.docx",
            employee="Dr. Lena Vogt",
            address="Ladenburger Straße 18, 69120 Heidelberg",
            role="Senior Backend Engineer und Team Lead Tax Core",
            contract_date="20.03.2019",
            start_date="01.04.2019",
            annual_salary="72.000,00 EUR brutto",
            monthly_salary="6.000,00 EUR brutto",
            workplace="Im Neuenheimer Feld 583, 69120 Heidelberg",
            probation="Die ersten sechs Monate gelten als Probezeit; während dieser kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.",
            notice="Nach der Probezeit beträgt die Kündigungsfrist für beide Parteien drei Monate zum Quartalsende. Verlängert sich die Frist für eine Kündigung durch die Arbeitgeberin kraft Gesetzes, gilt dieselbe verlängerte Frist auch für eine Kündigung durch die Arbeitnehmerin.",
            ip_clause=(
                "Die Arbeitnehmerin räumt der Arbeitgeberin an allen in Erfüllung ihrer arbeitsvertraglichen Aufgaben oder unter wesentlicher Nutzung betrieblicher Mittel geschaffenen Programmen, Quell- und Objektcodes, Datenmodellen, Regelwerken, Schnittstellen, Dokumentationen, Tests, Entwürfen und sonstigen Arbeitsergebnissen mit ihrer Entstehung ausschließliche, zeitlich, räumlich und inhaltlich unbeschränkte Nutzungsrechte für alle bei Vertragsschluss bekannten Nutzungsarten ein. Erfasst sind insbesondere Vervielfältigung, Verbreitung, öffentliche Zugänglichmachung, Vermietung, Hosting, Bearbeitung, Verbindung mit anderen Produkten, Übersetzung, Portierung, Unterlizenzierung und Übertragung an Dritte einschließlich Rechtsnachfolger und Erwerber von Betrieben oder Produktlinien. Die Rechte gelten für Zwischen- und Endstände; die Vergütung ist mit dem Gehalt abgegolten, soweit zwingendes Recht nichts anderes bestimmt."
            ),
            side_activity_clause=(
                "Jede entgeltliche Nebentätigkeit und jede fortlaufende unentgeltliche Softwareentwicklung außerhalb rein privater Lernübungen bedarf der vorherigen schriftlichen Zustimmung der Arbeitgeberin. Die Zustimmung ist zu erteilen, wenn Arbeitsleistung, Wettbewerbsinteressen, Geheimhaltung und gesetzliche Arbeitszeit nicht beeinträchtigt werden. Beiträge zu öffentlichen Repositories gelten als anzeigepflichtige Softwareentwicklung; die Anzeige benennt Projekt, Lizenz und geplanten Umfang."
            ),
            preexisting_clause=(
                "Als vorbestehendes Werk wird ausschließlich die von der Arbeitnehmerin vor dem 1. April 2019 privat entwickelte Parserbibliothek TaxParse 1.3 gemäß Anlage V-1 mit dem dort abgedruckten SHA-256-Hash festgehalten. Das Eigentum am Vorbestand verbleibt bei der Arbeitnehmerin. Sie räumt der Arbeitgeberin hieran ein unwiderrufliches, einfaches, weltweites und zeitlich unbeschränktes Recht ein, TaxParse in FiscusPilot zu vervielfältigen, zu bearbeiten, mit anderen Modulen zu verbinden und gemeinsam mit FiscusPilot an Kunden und Rechtsnachfolger weiterzugeben. Andere private Bibliotheken sind nicht eingebracht."
            ),
            oss_clause=(
                "Open-Source-Software darf in produktiven Quellcode nur nach vorheriger schriftlicher Freigabe durch die Leitung Engineering und die Compliance-Verantwortliche aufgenommen werden. Die Freigabe muss Lizenz, Version, geplante Verteilung und etwaige Pflichten dokumentieren. Komponenten mit Copyleft- oder Netzwerk-Copyleft-Bedingungen dürfen ohne ausdrückliche Zustimmung der Geschäftsführung weder statisch noch dynamisch mit FiscusPilot verbunden oder als Bestandteil eines angebotenen Dienstes eingesetzt werden."
            ),
            employee_sign_date="20.03.2019",
            employer_signatory="Martin Reuter, Geschäftsführer",
        ),
        _employment_contract(
            path="03_Personal_Rechtekette/02_Arbeitsvertrag_Jonas_Eberle.docx",
            employee="Jonas Eberle",
            address="Meerfeldstraße 44, 68163 Mannheim",
            role="Frontend Software Engineer",
            contract_date="10.07.2020",
            start_date="01.08.2020",
            annual_salary="60.000,00 EUR brutto",
            monthly_salary="5.000,00 EUR brutto",
            workplace="Heidelberg; an bis zu drei Tagen pro Woche kann nach Teamabstimmung mobil gearbeitet werden",
            probation="Die ersten drei Monate sind Probezeit. Während der Probezeit beträgt die Kündigungsfrist zwei Wochen.",
            notice="Nach Ablauf der Probezeit gelten die gesetzlichen Kündigungsfristen. Jede gesetzliche Verlängerung der Arbeitgeberfrist gilt in gleichem Umfang für den Arbeitnehmer.",
            ip_clause=(
                "Der Arbeitnehmer räumt der Arbeitgeberin an Software, Gestaltungen, Texten und Dokumentationen, die er im Rahmen konkret übertragener Arbeitsaufgaben für FiscusPilot schafft, ausschließliche, weltweite und zeitlich unbeschränkte Nutzungsrechte ein. Die Arbeitgeberin darf diese Arbeitsergebnisse in allen bekannten Formen nutzen, bearbeiten, mit anderen Werken verbinden, vervielfältigen, verbreiten, online bereitstellen und Kunden oder Erwerbern der Produktlinie Nutzungsrechte einräumen. Ergebnisse, die ohne Bezug zu den übertragenen Aufgaben, ohne betriebliche Informationen und ohne betriebliche Mittel in der Freizeit entstehen, werden von dieser Klausel nicht erfasst."
            ),
            side_activity_clause=(
                "Nebentätigkeiten sind spätestens zwei Wochen vor Aufnahme in Textform mit Auftraggeber, Gegenstand und regelmäßigem Zeitumfang anzuzeigen. Eine Zustimmung ist nicht erforderlich, sofern keine Konkurrenztätigkeit, kein Einsatz vertraulicher Informationen, keine Nutzung betrieblicher Systeme und keine Beeinträchtigung der Arbeitsleistung vorliegen. Die Arbeitgeberin kann eine Tätigkeit aus einem konkret benannten betrieblichen Grund untersagen oder mit Auflagen versehen."
            ),
            preexisting_clause=(
                "Der Arbeitnehmer bezeichnet in Anlage E-1 das vor dem Arbeitsverhältnis öffentlich entwickelte Projekt FormKit helpers, Repository-Stand 8f21d91 vom 30. Juni 2020. FormKit helpers bleibt Vorbestand des Arbeitnehmers und ist unter der MIT-Lizenz veröffentlicht. Eine Verwendung in FiscusPilot richtet sich nach dem in Anlage E-1 wiedergegebenen Lizenztext; darüber hinaus werden keine ausschließlichen Rechte am Vorbestand eingeräumt. Individuell für die Arbeitgeberin geschaffene Adapter und Oberflächen fallen unter Abschnitt 8 dieses Vertrags."
            ),
            oss_clause=(
                "Komponenten mit MIT-, BSD- oder Apache-2.0-Lizenz dürfen ohne Einzelfreigabe verwendet werden, wenn sie auf der jeweils aktuellen Allowlist stehen und mit Version, Quelle und Lizenztext im NOTICE-Verzeichnis dokumentiert werden. Andere Lizenzen, insbesondere GPL-, AGPL-, LGPL-, MPL- oder quelloffene Lizenzen mit zusätzlichen Nutzungsbeschränkungen, bedürfen vor dem ersten Commit einer Freigabe durch Engineering und Legal."
            ),
            employee_sign_date="13.07.2020",
            employer_signatory="Martin Reuter, Geschäftsführer",
        ),
        _employment_contract(
            path="03_Personal_Rechtekette/03_Arbeitsvertrag_Esra_Kaya.docx",
            employee="Esra Kaya",
            address="Schriesheimer Straße 27, 68526 Ladenburg",
            role="DevOps und Security Engineer",
            contract_date="29.01.2021",
            start_date="15.02.2021",
            annual_salary="67.200,00 EUR brutto",
            monthly_salary="5.600,00 EUR brutto",
            workplace="Im Neuenheimer Feld 583, Heidelberg, sowie die jeweils beauftragten Rechenzentrumsstandorte",
            probation="Eine Probezeit von sechs Monaten wird vereinbart. Während dieser Zeit kann jede Partei mit einer Frist von zwei Wochen kündigen.",
            notice="Nach der Probezeit kann das Arbeitsverhältnis mit einer Frist von sechs Wochen zum Quartalsende gekündigt werden. Längere gesetzliche Arbeitgeberfristen gelten beiderseits.",
            ip_clause=(
                "Die Arbeitnehmerin räumt der Arbeitgeberin sämtliche übertragbaren ausschließlichen Nutzungsrechte an allen dienstlich erstellten Infrastrukturdefinitionen, Skripten, Richtlinien, Automatisierungen, Konfigurationen, Sicherheitsregeln, Programmen, Dokumentationen und sonstigen Ergebnissen ein. Die Rechtseinräumung ist räumlich und zeitlich unbeschränkt und umfasst Bearbeitung, Vervielfältigung, Verbreitung, öffentliche Zugänglichmachung, SaaS- und Hosting-Nutzung, Unterlizenzierung sowie Übertragung im Ganzen oder für einzelne Produkte. Für bei Vertragsschluss unbekannte Nutzungsarten verpflichtet sich die Arbeitnehmerin zu einer gesonderten Rechtseinräumung gegen die gesetzlich vorgesehene Vergütung, sobald die Arbeitgeberin die Nutzung schriftlich anzeigt."
            ),
            side_activity_clause=(
                "Eine technische oder kaufmännische Nebentätigkeit sowie jede Tätigkeit von regelmäßig mehr als acht Stunden im Monat bedarf vorheriger Zustimmung in Textform. Fachvorträge und Lehrveranstaltungen bis zu vier Stunden monatlich sind lediglich anzuzeigen, sofern keine vertraulichen Inhalte, Kundenbeispiele oder internen Sicherheitsinformationen verwendet werden. Die Mitarbeit an Sicherheitsprojekten mit unmittelbarem Bezug zu Steuersoftware gilt als zustimmungspflichtig."
            ),
            preexisting_clause=(
                "Die Arbeitnehmerin erklärt, keine vorbestehende Software, Infrastrukturvorlagen oder fremden Zugangsmittel in die Tätigkeit einzubringen. Allgemeine, nicht verkörperte Kenntnisse und Befehlsfolgen aus der bisherigen Berufspraxis bleiben frei. Werden später eigene Vorlagen benötigt, müssen sie vor der Übernahme mit Herkunft, Datum und Lizenz in einer von beiden Parteien unterzeichneten Ergänzung erfasst werden."
            ),
            oss_clause=(
                "Die Open-Source-Richtlinie 1.2 vom 1. März 2021 ist als Anlage K-2 einbezogen. Danach ist jede Abhängigkeit vor produktiver Nutzung im Komponentenregister zu erfassen. Starkes Copyleft und Netzwerk-Copyleft sind für ausgelieferte Software, Container und angebotene Netzwerkdienste bis zu einer gemeinsamen Freigabe durch Security, Engineering und Geschäftsführung gesperrt. Werkzeuge der Build-Umgebung sind ebenfalls zu erfassen, werden jedoch nach dem dokumentierten Einsatzzweck gesondert bewertet."
            ),
            employee_sign_date="29.01.2021",
            employer_signatory="Martin Reuter, Geschäftsführer",
        ),
        _employment_contract(
            path="03_Personal_Rechtekette/04_Arbeitsvertrag_Marek_Nowak.docx",
            employee="Marek Nowak",
            address="Seckenheimer Hauptstraße 112, 68239 Mannheim",
            role="Data Engineer und Integration Specialist",
            contract_date="14.10.2022",
            start_date="01.11.2022",
            annual_salary="75.600,00 EUR brutto",
            monthly_salary="6.300,00 EUR brutto",
            workplace="Heidelberg mit vereinbartem mobilem Arbeitsanteil von bis zu 60 Prozent",
            probation="Die ersten sechs Monate gelten als Probezeit; die Kündigungsfrist beträgt in dieser Zeit zwei Wochen.",
            notice="Im Anschluss an die Probezeit gilt eine Frist von drei Monaten zum Monatsende. Gesetzlich längere Fristen zugunsten des Arbeitnehmers bleiben unberührt und gelten auch für dessen Eigenkündigung.",
            ip_clause=(
                "An Arbeitsergebnissen, die der Arbeitnehmer aufgrund einer dokumentierten Aufgabe für Datenimporte, Schnittstellen oder FiscusPilot-Module erstellt, erhält die Arbeitgeberin ausschließliche, weltweite und zeitlich unbeschränkte Nutzungsrechte für Vervielfältigung, Bearbeitung, Verbindung, Verbreitung, Bereitstellung als Dienst, Unterlizenzierung und Übertragung zusammen mit dem jeweiligen Produkt. Nicht erfasst sind allgemein einsetzbare Methoden, abstrakte Datenmodelle und Werkzeuge, die der Arbeitnehmer außerhalb konkreter Aufgaben ohne Unternehmensdaten entwickelt; sobald solche Bestandteile in ein betriebliches Repository übernommen werden sollen, ist Abschnitt 9 anzuwenden."
            ),
            side_activity_clause=(
                "Die bereits mitgeteilte selbständige Beratung unter der Bezeichnung LedgerLens Analytics ist bis zu sechs Stunden pro Woche gestattet. Sie darf weder für Steuerkanzleien oder Softwareanbieter aus dem Kunden- und Wettbewerberkreis der Arbeitgeberin erbracht werden noch Quellcode, Datenmodelle oder Arbeitsmittel der Arbeitgeberin nutzen. Der Arbeitnehmer übermittelt quartalsweise eine Liste der Auftraggeber und zeigt wesentliche Änderungen vorab an; andere Nebentätigkeiten bedürfen der Zustimmung in Textform."
            ),
            preexisting_clause=(
                "Als Vorbestand ist der CSV-Mapper LedgerLens 0.9 mit den in Anlage N-1 bezeichneten Dateien und Hashwerten ausgenommen. Soweit die dort einzeln aufgeführten Adapterdateien in ledger-flow kopiert werden, räumt der Arbeitnehmer der Arbeitgeberin ein einfaches, unwiderrufliches, weltweites und zeitlich unbeschränktes Recht zur Nutzung, Bearbeitung und Weitergabe als Teil von FiscusPilot ein. Die übrige LedgerLens-Anwendung und spätere unabhängige Fassungen bleiben außerhalb des Vertrags."
            ),
            oss_clause=(
                "Open-Source-Komponenten dürfen entsprechend der im Engineering-Wiki bereitgestellten Richtlinie eingesetzt werden. Vor jedem produktiven Merge sind Paketname, Version, Lizenz und Quelle in der Merge-Request-Vorlage anzugeben. Für Komponenten mit Pflichten zur Quelloffenlegung, zur Weiterlizenzierung abgeleiteter Werke oder zur Bereitstellung von Netzwerkquellcode ist eine ausdrückliche Freigabe in Textform erforderlich; die zum Unterzeichnungsdatum im Wiki abrufbare Richtlinienfassung wird im Vertrag nicht als Anlage wiedergegeben."
            ),
            employee_sign_date="17.10.2022",
            employer_signatory="Martin Reuter, Geschäftsführer",
        ),
        _employment_contract(
            path="03_Personal_Rechtekette/05_Arbeitsvertrag_Nina_Scholl.docx",
            employee="Nina Scholl",
            address="Neckarauer Waldweg 31, 68199 Mannheim",
            role="Mobile und Quality Engineer",
            contract_date="12.04.2024",
            start_date="01.05.2024",
            annual_salary="68.400,00 EUR brutto",
            monthly_salary="5.700,00 EUR brutto",
            workplace="Heidelberg und im Rahmen der Mobile-Work-Vereinbarung die Wohnanschrift der Arbeitnehmerin",
            probation="Die ersten sechs Monate des Arbeitsverhältnisses sind Probezeit. Während der Probezeit kann mit zwei Wochen Frist gekündigt werden.",
            notice="Nach der Probezeit gilt für beide Parteien eine Kündigungsfrist von vier Wochen zum Fünfzehnten oder zum Ende eines Kalendermonats. Gesetzliche Verlängerungen der Frist für die Arbeitgeberin gelten auch für die Arbeitnehmerin.",
            ip_clause=(
                "Die Arbeitnehmerin räumt der Arbeitgeberin im gesetzlich größtmöglichen Umfang ausschließliche, übertragbare und unterlizenzierbare Nutzungsrechte an den im Zusammenhang mit ihren dienstlichen Aufgaben geschaffenen mobilen Anwendungen, Testautomatisierungen, Bildverarbeitungsabläufen, Benutzeroberflächen, Dokumentationen und Designs ein. Die Rechte gelten weltweit für die Dauer des gesetzlichen Schutzes und umfassen insbesondere Nutzung in Quell- und Objektform, Bearbeitung, Portierung, Verbindung mit Cloud-Diensten, App-Store-Vertrieb, SaaS-Betrieb und Übertragung an einen Erwerber der FiscusPilot-Produkte."
            ),
            side_activity_clause=(
                "Nebentätigkeiten sind vor Aufnahme in Textform zu beantragen. Die am 8. April 2024 per E-Mail beschriebene unentgeltliche Mitarbeit am gemeinnützigen Projekt RadKarte Rhein-Neckar ist im Umfang von höchstens fünf Stunden monatlich gestattet; eine Nutzung betrieblicher Geräte, Arbeitszeit oder Bibliotheken ist ausgeschlossen. Veröffentlichungen zu mobiler Belegerfassung oder OCR bedürfen einer erneuten Abstimmung."
            ),
            preexisting_clause=(
                "Die Arbeitnehmerin hat das private Projekt ReceiptCam mit Bildzuschnitt und Belichtungskorrektur als möglichen Vorbestand angezeigt. Nach dem Vertrag soll nur der in Anlage S-1 durch Dateinamen und Hashwerte bezeichnete Stand ausgenommen bleiben; für ausdrücklich übernommene Dateien soll ein einfaches, dauerhaftes Recht zur Integration in FiscusPilot gelten. In der bei Unterzeichnung ausgehändigten Vertragsmappe ist Anlage S-1 mit 'Fassung folgt nach erstem Code Review' bezeichnet."
            ),
            oss_clause=(
                "Zugelassene Mobile-Pakete dürfen verwendet werden, wenn in der Paketdatei ein SPDX-Ausdruck, die Bezugsquelle und die Version erfasst sind und der automatisierte Lizenzcheck ohne Sperrhinweis endet. Pakete mit unbekannter Lizenz oder Copyleft-Wirkung sowie kopierte Codebeispiele aus Foren dürfen erst nach dokumentierter Prüfung übernommen werden. Die Arbeitnehmerin pflegt die Hinweise im About-Dialog und in der NOTICE-Datei des Mobile-Releases."
            ),
            employee_sign_date="15.04.2024",
            employer_signatory="Martin Reuter, Geschäftsführer",
        ),
        _xlsx(
            "03_Personal_Rechtekette/06_Rechte_und_Nebentaetigkeiten_Matrix.xlsx",
            "Auswertung der Personalunterlagen ohne rechtliche Bewertung",
            [
                {
                    "name": "Vertragsvergleich",
                    "headers": ["Person", "Rolle", "Beginn", "Jahresgehalt bei Vertrag", "Rechteklausel", "Nebentätigkeit", "Vorbestand", "Open Source"],
                    "rows": [
                        ["Dr. Lena Vogt", "Backend/Team Lead", "01.04.2019", 72000, "dienstliche und mit Betriebsmitteln geschaffene Ergebnisse; ausschließliche Rechte", "vorherige schriftliche Zustimmung", "TaxParse 1.3; einfache Integrationslizenz", "Einzelfreigabe; Copyleft nur Geschäftsführung"],
                        ["Jonas Eberle", "Frontend", "01.08.2020", 60000, "konkret übertragene Aufgaben; Freizeitprojekte ausgenommen", "Anzeige; Untersagung nur bei Grund", "FormKit helpers; MIT", "Allowlist für permissive Lizenzen"],
                        ["Esra Kaya", "DevOps/Security", "15.02.2021", 67200, "dienstliche Ergebnisse; bekannte und spätere Nutzungen getrennt", "Zustimmung ab Technikbezug oder acht Stunden", "keiner erklärt", "Richtlinie 1.2; dreistufige Freigabe"],
                        ["Marek Nowak", "Data/Integration", "01.11.2022", 75600, "dokumentierte Aufgaben; Methoden und unabhängige Tools ausgenommen", "LedgerLens bis sechs Stunden/Woche", "LedgerLens 0.9; selektive Lizenz", "Wiki-Richtlinie ohne Anlage"],
                        ["Nina Scholl", "Mobile/QA", "01.05.2024", 68400, "dienstliche Mobile-, Test- und Design-Ergebnisse", "RadKarte per Vorabmail gestattet", "ReceiptCam; Anlage als nachzureichen markiert", "SPDX und automatischer Check"],
                    ],
                },
                {
                    "name": "Anlagenstatus",
                    "headers": ["Person", "Anlage", "In Personalakte", "Unterschriften", "Technischer Bezug", "Abweichung/Frage"],
                    "rows": [
                        ["Dr. Lena Vogt", "V-1 TaxParse", "Scan, 3 Seiten", "beide Initialen auf Seite 3", "Hash nennt Archiv taxparse-1.3.zip", "Archiv selbst fehlt im Datenraum"],
                        ["Jonas Eberle", "E-1 FormKit", "nur Lizenztext und URL", "nur Arbeitnehmer", "Commit 8f21d91", "Gegenzeichnung Arbeitgeberseite fehlt"],
                        ["Esra Kaya", "K-2 OSS-Richtlinie 1.2", "vollständig", "Empfangsbestätigung Arbeitnehmerin", "Policy-Stand 2021", "spätere Richtlinie 2.0"],
                        ["Marek Nowak", "N-1 LedgerLens", "Seite 1 und Hashliste", "beide auf Seite 1", "vier Adapterdateien", "Seite 2 mit Beschreibung fehlt"],
                        ["Nina Scholl", "S-1 ReceiptCam", "Deckblatt 'Fassung folgt'", "beide auf Deckblatt", "keine Hashwerte", "spätere Code-Review-Anlage nicht gefunden"],
                    ],
                },
                {
                    "name": "Aktuelle_Vergütung",
                    "headers": ["Person", "Vertragsgehalt", "Letzte Anpassung", "Aktuelles Jahresbrutto", "Quelle"],
                    "rows": [
                        ["Dr. Lena Vogt", 72000, "01.01.2025", 84000, "Gehaltsnachtrag 10.12.2024"],
                        ["Jonas Eberle", 60000, "01.01.2026", 72000, "Gehaltsmail 18.12.2025"],
                        ["Esra Kaya", 67200, "01.07.2025", 78000, "Nachtrag 20.06.2025"],
                        ["Marek Nowak", 75600, "01.01.2026", 81000, "Nachtrag 15.12.2025"],
                        ["Nina Scholl", 68400, "keine", 68400, "Arbeitsvertrag"],
                    ],
                },
            ],
        ),
        _doc(
            "03_Personal_Rechtekette/07_Uebergabeprotokoll_Marek_Nowak.pdf",
            "pdf",
            "Übergabeprotokoll LedgerFlow nach Freistellung",
            sections=[
                _section(
                    "Termin und Teilnehmende",
                    "Videotermin am 18. September 2026, 10:00 bis 11:20 Uhr. Teilnehmende: Marek Nowak, Dr. Lena Vogt, Carlotta Frey für das Verwalterteam und Esra Kaya für den technischen Betrieb.",
                ),
                _section(
                    "Übergebene Gegenstände",
                    "Marek Nowak erläuterte die Repositories ledger-flow und die Importspezifikationen im Confluence-Bereich LF. Offene Merge Requests 481 bis 486 wurden Dr. Lena Vogt zugewiesen. Ein lokaler Testdatensatz wurde nach Bildschirmfreigabe gelöscht; produktive Kundendaten befanden sich nach Erklärung von Herrn Nowak nicht auf seinem Privatgerät.",
                    "Der Zugang zum betrieblichen GitLab wurde nach dem Termin deaktiviert. Das Firmen-Notebook KTW-NB-118, ein YubiKey und ein Mobiltelefon wurden am Empfang der Kanzlei Mohn abgegeben.",
                ),
                _section(
                    "LedgerLens-Hinweis",
                    "Herr Nowak erklärte, vier kleine Adapterdateien stammten aus seinem früheren Projekt LedgerLens. Er verwies auf Anlage N-1 zum Arbeitsvertrag und sagte, die produktiven Dateien seien danach stark verändert worden. Er konnte im Termin nicht angeben, ob die fehlende zweite Seite der Anlage jemals gegengezeichnet wurde.",
                ),
                _section(
                    "Bestätigung",
                    "Das Protokoll wurde von Carlotta Frey erstellt. Marek Nowak bestätigte am 19. September per E-Mail die Geräteübergabe, ergänzte jedoch den Satz: 'Meine Rechteposition zu LedgerLens bleibt entsprechend dem Arbeitsvertrag unberührt.' Eine weitergehende Bestätigung liegt nicht vor.",
                ),
            ],
        ),
        _doc(
            "03_Personal_Rechtekette/08_Freelancer_Rahmenvertrag_Lukas_Binder.docx",
            "docx",
            "Rahmenvertrag freie Softwareentwicklung Lukas Binder",
            sections=[
                _section(
                    "Vertragsparteien",
                    "Zwischen der Kurpfalz Taxware GmbH, damals Rohrbacher Straße 77, 69115 Heidelberg, vertreten durch Geschäftsführer Martin Reuter, und Herrn Lukas Binder, Binder Software, Carl-Theodor-Straße 9, 68723 Schwetzingen, wird am 14. Juni 2017 dieser Rahmenvertrag über freie Softwareentwicklung geschlossen.",
                    "Der Auftragnehmer erbringt seine Leistungen selbständig, ist in der Wahl von Arbeitszeit und Arbeitsort frei und schuldet die in Einzelaufträgen bezeichneten Ergebnisse und Abstimmungen. Ein Arbeitsverhältnis wird nicht begründet.",
                ),
                _section(
                    "Leistungsgegenstand",
                    "Gegenstand ist die Konzeption und Implementierung eines Regel- und Normalisierungsmoduls für das Produkt TaxEngine Classic einschließlich Umsatzsteuer-Zeiträumen, Fristenlogik, Importvalidierung, Tests und technischer Dokumentation. Einzelheiten, Meilensteine und Abnahmen werden in Leistungsabrufen festgelegt.",
                ),
                _section(
                    "Mitwirkung und Systeme",
                    "Die Auftraggeberin stellt fachliche Spezifikationen und anonymisierte Beispieldaten bereit. Produktive Mandantendaten dürfen dem Auftragnehmer nur nach gesonderter Freigabe zugänglich gemacht werden. Zugänge sind personenbezogen und nach Ende eines Abrufs zu löschen.",
                ),
                _section(
                    "Vergütung und Abrechnung",
                    "Der Stundensatz beträgt 105,00 EUR netto. Abgerechnet wird monatlich nach Tätigkeitsnachweis; Reisezeiten werden zu 50 Prozent, notwendige Reisekosten nach Beleg vergütet. Zahlungsziel sind 14 Kalendertage nach prüffähigem Rechnungseingang.",
                ),
                _section(
                    "Abnahme",
                    "Werkbezogene Ergebnisse werden nach Bereitstellung einer lauffähigen Fassung und der vereinbarten Tests innerhalb von zehn Werktagen geprüft. Beanstandungen sind mit reproduzierbaren Schritten mitzuteilen. Erfolgt keine Rückmeldung, gilt dies allein dann als Abnahme, wenn die Auftraggeberin bei Bereitstellung in Textform auf diese Folge hingewiesen wurde.",
                ),
                _section(
                    "Rechte an neu geschaffenen Ergebnissen",
                    "An den speziell aufgrund eines vergüteten Leistungsabrufs für TaxEngine Classic neu geschaffenen und abgenommenen Quelltexten, Tests und Dokumentationen räumt der Auftragnehmer der Auftraggeberin mit vollständiger Zahlung ein ausschließliches, weltweites und zeitlich unbeschränktes Recht zur Vervielfältigung, Bearbeitung, Verbindung, Verbreitung, öffentlichen Zugänglichmachung, Unterlizenzierung und Übertragung zusammen mit dem Produkt oder Unternehmen ein. Entwurfsstände werden erfasst, soweit sie übergeben und vergütet sind.",
                ),
                _section(
                    "Vorbestehende Bestandteile",
                    "Vorbestehende Werkzeuge, Bibliotheken und Regelbausteine des Auftragnehmers bleiben von der ausschließlichen Rechtseinräumung ausgenommen, wenn sie in Anlage 2 konkret bezeichnet sind. Soweit solche Bestandteile in ein Arbeitsergebnis eingebettet werden, räumt der Auftragnehmer der Auftraggeberin daran ein einfaches, unwiderrufliches, weltweites und zeitlich unbeschränktes Recht ein, sie als Teil von TaxEngine Classic zu nutzen, zu bearbeiten, zu vervielfältigen und mit dem Produkt an Kunden und Rechtsnachfolger weiterzugeben.",
                ),
                _section(
                    "Drittsoftware und Open Source",
                    "Drittsoftware darf nur nach vorheriger Zustimmung der Auftraggeberin eingesetzt werden. Der Auftragnehmer nennt Komponente, Version und Lizenz und übergibt die erforderlichen Lizenztexte. Komponenten, die eine Offenlegung von TaxEngine-Quellcode oder eine Lizenzierung des Gesamtwerks zu abweichenden Bedingungen verlangen können, bedürfen einer ausdrücklichen schriftlichen Zustimmung.",
                ),
                _section(
                    "Gewährleistung der Herkunft",
                    "Der Auftragnehmer erklärt, zur Einräumung der in diesem Vertrag beschriebenen Rechte befugt zu sein und keine ihm bekannten Rechte Dritter entgegenstehen zu lassen. Ansprüche wegen einer von ihm zu vertretenden Pflichtverletzung richten sich nach den gesetzlichen Vorschriften mit den Haftungsbegrenzungen dieses Vertrags.",
                ),
                _section(
                    "Vertraulichkeit",
                    "Quellcode, Fachkonzepte, Kundendaten und nicht veröffentlichte Geschäftsunterlagen sind vertraulich zu behandeln und ausschließlich für den Auftrag zu verwenden. Die Pflicht gilt fünf Jahre nach Vertragsende fort; Geschäftsgeheimnisse sind solange zu schützen, wie ihre Geheimniseigenschaft besteht.",
                ),
                _section(
                    "Haftung",
                    "Bei leichter Fahrlässigkeit haftet jede Partei nur für die Verletzung wesentlicher Vertragspflichten und begrenzt auf den vorhersehbaren vertragstypischen Schaden. Die Begrenzung gilt nicht bei Vorsatz, grober Fahrlässigkeit, Verletzung von Leben, Körper oder Gesundheit sowie zwingender Haftung.",
                ),
                _section(
                    "Laufzeit und Beendigung",
                    "Der Vertrag beginnt mit Unterzeichnung und kann mit vier Wochen Frist zum Monatsende gekündigt werden. Laufende Einzelaufträge werden geordnet abgeschlossen oder nach dokumentiertem Stand übergeben. Nach Vertragsende sind Zugänge, Daten und Arbeitsunterlagen zurückzugeben oder auf Weisung zu löschen.",
                ),
                _section(
                    "Schlussbestimmungen",
                    "Änderungen und Einzelaufträge bedürfen mindestens der Textform. Es gilt deutsches Recht. Gerichtsstand wird, soweit zulässig, Heidelberg vereinbart. Anlage 1 Leistungsbeschreibung und Anlage 2 Vorbestand sind Bestandteil des Vertrags.",
                ),
                _section(
                    "Unterschriften",
                    "Heidelberg, 14.06.2017 — Martin Reuter für die Kurpfalz Taxware GmbH, handschriftlich unterzeichnet.",
                    "Schwetzingen, 14.06.2017 — Lukas Binder, handschriftlich unterzeichnet. Beide Ausfertigungen tragen auf jeder Anlagenseite Paraphen, wobei die im Datenraum vorhandene Anlage 2 den Stand '2.4' ausweist.",
                ),
            ],
        ),
        _doc(
            "03_Personal_Rechtekette/09_Anlage_Vorbestand_BinderRules.pdf",
            "pdf",
            "Anlage 2 zum Freelancervertrag – vorbestehende BinderRules",
            sections=[
                _section(
                    "Zuordnung",
                    "Anlage 2 zum Rahmenvertrag vom 14. Juni 2017. Dateikopf: 'BinderRules – Vorbestand, Version 2.4, Export 12.06.2017'. Auf Seite 1 befinden sich die Paraphen MR und LB; Seite 2 trägt nur die Paraphe LB.",
                ),
                _section(
                    "Bezeichnete Bestandteile",
                    "Als Vorbestand werden RuleNormalizer, PeriodResolver, HolidayBridge und die generischen Testgeneratoren bezeichnet. Die Anlage nennt das private Repository binder/rules-v2, enthält aber weder vollständige Dateipfade noch Hashwerte.",
                    "Nicht als Vorbestand bezeichnet sind kundenspezifische Mappingtabellen, die Benutzeroberfläche, die Importvalidierung und die Dokumentation für TaxEngine Classic.",
                ),
                _section(
                    "Nutzung im Auftrag",
                    "Die Anlage wiederholt, dass eingebettete Vorbestandsbestandteile im Umfang des Rahmenvertrags als Teil von TaxEngine Classic verwendet, bearbeitet und zusammen mit dem Produkt weitergegeben werden dürfen. Eine eigenständige Vermarktung des Vorbestands durch die Auftraggeberin wird nicht erwähnt.",
                ),
                _section(
                    "Zusatzvermerk",
                    "Am unteren Rand der zweiten Seite steht handschriftlich: 'CalcSpline aus altem Uni-Projekt nicht benötigt; falls doch, vorher klären.' Unterschrift und Datum des Zusatzes sind nicht erkennbar.",
                ),
            ],
            tables=[
                {
                    "title": "Dateiliste laut Anlage",
                    "headers": ["Bezeichnung", "Sprache", "Version", "Einsatz laut Anlage"],
                    "rows": [
                        ["RuleNormalizer", "Java", "2.4", "Normalisierung eingehender Regelparameter"],
                        ["PeriodResolver", "Java", "2.3", "Zeitraum- und Fälligkeitslogik"],
                        ["HolidayBridge", "Groovy", "1.8", "Schnittstelle zu Feiertagskalendern"],
                        ["RuleFixtureFactory", "Java", "2.1", "generische Testdatengenerierung"],
                    ],
                }
            ],
        ),
        _mail(
            "03_Personal_Rechtekette/10_Mail_Binder_Altcode.eml",
            "E-Mail von Lukas Binder zum Altcode",
            sender="Lukas Binder <lukas@binder-software.example>",
            to=["Martin Reuter <martin.reuter@kurpfalz-taxware.example>"],
            cc=["Lena Vogt <lena.vogt@kurpfalz-taxware.example>"],
            date="Mon, 12 Nov 2018 18:42:00 +0100",
            subject="TaxEngine Übergabe / mein alter Normalizer",
            body=(
                "Hallo Martin, hallo Lena,\n\nfür die Übergabe habe ich den Stand classic-1.3 auf euren "
                "Server gepusht. Zur Erinnerung: Der Normalizer und der PeriodResolver kamen aus "
                "meiner BinderRules-Bibliothek. Ihr dürft die beiden natürlich in TaxEngine nutzen "
                "und weiterpflegen, so wie wir es 2017 vereinbart haben. Ich behalte mein privates "
                "Repository, weil ich ähnliche Grundlogik auch in einem Lagerprojekt verwende. Die "
                "kundenspezifischen USt-Mappings und die neuen Tests sind nur für euch entstanden.\n\n"
                "Im Ordner experimental liegt außerdem noch CalcSpline. Das war nie Teil der "
                "Abnahme und sollte nicht in einen Release. Bitte prüft beim Umzug, ob der Ordner "
                "überhaupt noch gebraucht wird.\n\nViele Grüße\nLukas"
            ),
            attachments=[],
        ),
        _doc(
            "03_Personal_Rechtekette/11_Rechnung_Freelancer_2018.pdf",
            "pdf",
            "Freelancer-Rechnung Binder Software Dezember 2018",
            paragraphs=[
                "Binder Software, Lukas Binder, Carl-Theodor-Straße 9, 68723 Schwetzingen. Rechnung BS-2018-119 vom 18. Dezember 2018 an Kurpfalz Taxware GmbH, Rohrbacher Straße 77, 69115 Heidelberg.",
                "Leistungszeitraum: 1. bis 14. Dezember 2018. Bezug: Rahmenvertrag vom 14. Juni 2017, Leistungsabruf 'Classic Übergabe und Migration'. Zahlungsziel: 1. Januar 2019. Bankverbindung endet auf 7714.",
                "Leistungsnachweis elektronisch bestätigt durch Martin Reuter am 17. Dezember 2018. Auf dem PDF befindet sich der Stempel 'bezahlt 28.12.2018'.",
            ],
            tables=[
                {
                    "title": "Abgerechnete Leistungen",
                    "headers": ["Datum", "Leistung", "Stunden", "Satz EUR", "Netto EUR"],
                    "rows": [
                        ["03.–05.12.2018", "Bereinigung Regelkern und Übergabekommentare", 18, 105, 1890],
                        ["06.–07.12.2018", "Migration USt-Mappings in Kundenstruktur", 12, 105, 1260],
                        ["10.12.2018", "Review mit Lena Vogt", 4, 105, 420],
                        ["11.–14.12.2018", "Tests und Übergabedokumentation", 16, 105, 1680],
                        ["", "Nettosumme", "", "", 5250],
                        ["", "Umsatzsteuer 19 %", "", "", 997.5],
                        ["", "Rechnungsbetrag", "", "", 6247.5],
                    ],
                }
            ],
        ),
    ]
)


CASE["documents"].extend(
    [
        _doc(
            "02_Unternehmen_Produkt/01_Unternehmensprofil_Produkt.docx",
            "docx",
            "Unternehmens- und Produktprofil Kurpfalz Taxware",
            sections=[
                _section(
                    "Unternehmen",
                    "Die Kurpfalz Taxware GmbH wurde 2017 in Heidelberg gegründet. Unternehmensgegenstand laut Handelsregisterauszug sind Entwicklung, Vertrieb und Betrieb kaufmännischer Software sowie verbundene Beratungs- und Unterstützungsleistungen. Das Stammkapital beträgt 50.000 EUR.",
                    "Bis August 2026 beschäftigte die Gesellschaft 23 Personen, davon 14 in Entwicklung und Betrieb, vier in Support und Kundenprojekten sowie fünf in Vertrieb und Verwaltung. Der Jahresumsatz 2025 betrug laut BWA 3,18 Mio. EUR.",
                ),
                _section(
                    "Produktfamilie FiscusPilot",
                    "FiscusPilot Kanzlei unterstützt Fristen- und Belegworkflows, Umsatzsteuervoranmeldungen, Jahresabschluss-Checklisten und den Datenaustausch mit Mandanten. Das Produkt wird überwiegend als private Cloud oder als kundenseitig betriebene Installation angeboten.",
                    "FiscusPilot Mittelstand stellt Liquiditätsübersichten, Buchungsimporte, Steuerterminkalender und Freigabeworkflows für Unternehmen bereit. Beide Produktlinien verwenden den gemeinsamen Regelkern tax-engine und die Dokumentenkomponente DocFlow.",
                ),
                _section(
                    "Technische Entwicklungslinie",
                    "Das frühe Produkt TaxEngine Classic entstand 2017 und 2018 unter Mitwirkung des Freelancers Lukas Binder. Ab 2019 wurde der Regelkern schrittweise in das Repository fiscuspilot-core überführt. Der historische Ordner legacy/binder-rules ist weiterhin Bestandteil des Build-Prozesses für Altmandate.",
                    "Die Weboberfläche wurde ab 2020 neu aufgebaut. Cloud-Betrieb und Infrastrukturcode kamen 2021 hinzu; der Datenimport LedgerFlow wurde 2022 und 2023 ergänzt. Seit 2024 wird eine mobile Belegerfassung erprobt.",
                ),
                _section(
                    "Kunden und Erlösmodell",
                    "Zum 31. August 2026 weist das CRM 146 aktive Kanzleikunden und 83 aktive Mittelstandskunden aus. Wiederkehrende Entgelte werden monatlich, quartalsweise oder jährlich berechnet. Daneben bestehen Projekt-, Migrations- und Schulungsleistungen.",
                    "Die zehn größten Kunden stehen nach der internen Auswertung für 38 Prozent des wiederkehrenden Jahresumsatzes. Vertragsfassungen und Bestellformulare sind nicht für alle Kunden zentral abgelegt.",
                ),
                _section(
                    "Betrieb und Datenhaltung",
                    "Die Cloud-Umgebung wird in zwei Rechenzentrumsregionen in Frankfurt am Main betrieben. Quellcode liegt in einer selbstverwalteten GitLab-Instanz; Artefakte werden in einer separaten Registry gespeichert. Signaturschlüssel für Desktop-Releases befinden sich nach Auskunft der Technik in einem Hardware-Sicherheitsmodul.",
                    "Die Gesellschaft verwendet Jira, Confluence und ein internes Release-Wiki. Die Exporte im Datenraum wurden zwischen 29. September und 9. Oktober 2026 erstellt.",
                ),
            ],
        ),
        _doc(
            "02_Unternehmen_Produkt/02_Systemarchitektur_FiscusPilot.pdf",
            "pdf",
            "Systemarchitektur FiscusPilot – Stand September 2026",
            sections=[
                _section(
                    "Zweck und Stand",
                    "Architekturübersicht der Engineering-Abteilung, Version 4.7 vom 3. September 2026. Die Darstellung beschreibt den produktiven Sollstand; Abweichungen einzelner Kundeninstallationen sind möglich.",
                ),
                _section(
                    "Anwendungsschichten",
                    "Die Browseranwendung web-portal kommuniziert über gateway-api mit den Diensten identity-service, case-workflow, tax-engine und document-service. Das Mittelstandsmodul verwendet zusätzlich ledger-flow für Importschnittstellen und cash-view für Liquiditätsdarstellungen.",
                    "Für On-Premise-Kunden werden gateway-api, tax-engine und document-service als signierte Container ausgeliefert. Cloud-Kunden greifen auf mandantengetrennte Instanzen derselben Dienste zu.",
                ),
                _section(
                    "Daten und externe Schnittstellen",
                    "PostgreSQL speichert Stamm- und Vorgangsdaten. Dokumente liegen verschlüsselt in einem S3-kompatiblen Objektspeicher. Schnittstellen bestehen zu DATEV-Exportformaten, Banken über FinTS/EBICS-Dienstleister, E-Mail-Gateways und kundeneigenen Verzeichnisdiensten.",
                    "Das Modul binder-rules-normalizer wird innerhalb von tax-engine vor Regelberechnungen aufgerufen. Das Repository enthält daneben neuere Java-Regeln, die von Lena Vogt und Marek Nowak verantwortet wurden.",
                ),
                _section(
                    "Build und Auslieferung",
                    "Merge Requests lösen Tests, Abhängigkeitsprüfung und Container-Builds aus. Freigegebene Artefakte werden mit einem Organisationszertifikat signiert. Die produktive Freigabe benötigt technisch zwei Freigaben, wobei eine Freigabe regelmäßig durch die Leitung Engineering erfolgt.",
                    "Die mobile Belegerfassung Receipt Capture ist als getrennte Flutter-Anwendung angebunden. Bildvorverarbeitung und OCR laufen in receipt-worker; das Pilotmodul wird nur bei 18 Kunden aktiviert.",
                ),
            ],
            tables=[
                {
                    "title": "Komponenten und Verantwortliche",
                    "headers": ["Komponente", "Repository", "Technik", "Hauptverantwortung", "Betriebsform"],
                    "rows": [
                        ["Regelkern", "fiscuspilot-core", "Java/Kotlin", "Dr. Lena Vogt", "Cloud und On-Premise"],
                        ["Webportal", "fiscuspilot-web", "TypeScript/React", "Jonas Eberle", "Browser"],
                        ["Infrastruktur", "platform-deploy", "Terraform/Helm", "Esra Kaya", "Cloud"],
                        ["Datenimport", "ledger-flow", "Python/Kotlin", "Marek Nowak", "Cloud und Connector"],
                        ["Mobile Erfassung", "receipt-capture", "Flutter/Dart", "Nina Scholl", "Mobile Pilot"],
                        ["Historische Regeln", "taxengine-legacy", "Java/Groovy", "Lukas Binder / später Vogt", "eingebettet"],
                    ],
                },
                {
                    "title": "Technische Schlüssel und Verwahrung",
                    "headers": ["Gegenstand", "System", "Verwahrung", "Letzter dokumentierter Zugriff"],
                    "rows": [
                        ["Container-Signaturschlüssel", "HSM Frankfurt", "Esra Kaya / Martin Reuter", "08.09.2026"],
                        ["Desktop-Code-Signing", "USB-HSM Tresor", "Nora Schenk", "21.08.2026"],
                        ["GitLab-Administrator", "git.kurpfalz-intern.example", "Esra Kaya / externer Hoster", "07.10.2026"],
                        ["Paket-Registry", "registry.kurpfalz-intern.example", "Engineering Team", "09.10.2026"],
                    ],
                },
            ],
        ),
        _xlsx(
            "02_Unternehmen_Produkt/03_Repositoryverzeichnis.xlsx",
            "Verzeichnis der Quellcode-Repositories und technischen Assets",
            [
                {
                    "name": "Repositories",
                    "headers": ["Repository", "Pfad", "Status", "Erstellt", "Letzter Commit", "Hauptsprache", "Owner", "Sicherheitenanlage"],
                    "rows": [
                        ["fiscuspilot-core", "git/platform/fiscuspilot-core", "aktiv", "12.02.2019", "18.09.2026", "Java/Kotlin", "Lena Vogt", "FiscusPilot Core / TaxEngine"],
                        ["fiscuspilot-web", "git/apps/fiscuspilot-web", "aktiv", "03.06.2020", "16.09.2026", "TypeScript", "Jonas Eberle", "Web-Client"],
                        ["platform-deploy", "git/ops/platform-deploy", "aktiv", "20.01.2021", "14.09.2026", "Terraform/Helm", "Esra Kaya", "Betriebssoftware und Skripte"],
                        ["ledger-flow", "git/modules/ledger-flow", "aktiv", "11.10.2022", "18.09.2026", "Python/Kotlin", "Marek Nowak", "Importmodule"],
                        ["receipt-capture", "git/apps/receipt-capture", "Pilot", "16.01.2024", "12.09.2026", "Dart/Python", "Nina Scholl", "Mobile Erweiterungen"],
                        ["taxengine-legacy", "git/archive/taxengine-legacy", "read-only", "30.06.2017", "04.04.2020", "Java/Groovy", "Lukas Binder / Lena Vogt", "Altversionen und Nachfolger"],
                        ["docs-customer", "git/docs/customer-docs", "aktiv", "08.05.2019", "17.09.2026", "Markdown", "Support", "Dokumentation"],
                        ["license-service-poc", "git/labs/license-service-poc", "archiviert", "02.05.2023", "29.09.2023", "Go", "Jonas Eberle", "nicht ausdrücklich benannt"],
                    ],
                },
                {
                    "name": "Domains_Marken_Doku",
                    "headers": ["Asset", "Typ", "Registriert auf", "Vertrag/Provider", "Status am 09.10.2026", "APA-Anlage"],
                    "rows": [
                        ["fiscuspilot.example", "Domain", "Kurpfalz Taxware GmbH", "RheinHost eG", "aktiv", "Anlage 2.3"],
                        ["FiscusPilot", "Wortmarke DE 302019114477", "Kurpfalz Taxware GmbH", "DPMA-Auszug", "eingetragen", "Anlage 2.2"],
                        ["FiscusPilot Handbuch 4.7", "Dokumentation", "Autorenteam Support", "docs-customer", "aktuell", "Anlage 2.1"],
                        ["TaxEngine Classic", "Produktname/Altcode", "uneinheitlich dokumentiert", "taxengine-legacy", "nur Wartung", "Anlage 2.1 Sammelposition"],
                        ["release-signing-2025", "Zertifikat", "Kurpfalz Taxware GmbH", "TrustSign Europe", "gültig bis 11.12.2027", "Anlage 2.4"],
                    ],
                },
                {
                    "name": "Zugriff_Export",
                    "headers": ["System", "Exportdatum", "Exporttyp", "Dateigröße", "Hash/Referenz", "Ersteller"],
                    "rows": [
                        ["GitLab", "09.10.2026", "Projektbundles acht Repositories", "4,8 GB", "sha256-Liste DR-T02", "Esra Kaya"],
                        ["Container Registry", "09.10.2026", "Manifestlisten", "18 MB", "REG-2026-10", "Esra Kaya"],
                        ["Confluence", "05.10.2026", "HTML/PDF Export Engineering", "620 MB", "CONF-ENG-05", "Nina Scholl"],
                        ["Jira", "06.10.2026", "CSV alle Produktprojekte", "94 MB", "JIRA-ALL-06", "Jonas Eberle"],
                        ["HSM", "noch offen", "Schlüsselübergabeprotokoll", "", "", "Verwalterteam"],
                    ],
                },
            ],
        ),
        _csv(
            "02_Unternehmen_Produkt/04_Git_Commit_Export.csv",
            "Auszug aus dem Git-Commit-Export",
            ["Datum", "Repository", "Kurz-ID", "Autor", "Betreff", "Pfadschwerpunkt", "Release"],
            [
                ["2017-07-03", "taxengine-legacy", "a31f0c2", "Lukas Binder", "initial rule normalizer import", "src/binder/rules", "Classic 0.8"],
                ["2018-02-16", "taxengine-legacy", "bc102ef", "Lukas Binder", "VAT period mapping for Kanzlei", "src/binder/rules/vat", "Classic 1.1"],
                ["2019-04-12", "fiscuspilot-core", "02fa8e1", "Lena Vogt", "migrate tax parser and add adapter", "core/parser; legacy-adapter", "2.0-beta"],
                ["2019-06-21", "fiscuspilot-core", "12d7a90", "Lena Vogt", "replace date rules with TaxParse tables", "core/parser", "2.0"],
                ["2020-08-14", "fiscuspilot-web", "77ad8f4", "Jonas Eberle", "bootstrap FormKit based dialog shell", "src/forms", "2.6"],
                ["2020-10-02", "fiscuspilot-web", "fb1304a", "Jonas Eberle", "add MIT notice for FormKit helpers", "NOTICE; src/forms", "2.7"],
                ["2021-03-05", "platform-deploy", "c8d22e7", "Esra Kaya", "baseline terraform and helm charts", "infra; charts", "3.0"],
                ["2021-11-19", "platform-deploy", "e0091ab", "Esra Kaya", "pin image digest and signing policy", "policy; charts", "3.3"],
                ["2022-11-11", "ledger-flow", "104acf9", "Marek Nowak", "add LedgerLens CSV prototype adapter", "imports/ledgerlens", "3.8"],
                ["2023-01-20", "ledger-flow", "913cad0", "Marek Nowak", "normalize booking fields before mapping", "imports/normalize", "3.9"],
                ["2023-05-05", "fiscuspilot-core", "ab34d61", "Lena Vogt", "extract legacy binder normalizer wrapper", "legacy/binder-rules", "4.0"],
                ["2024-02-09", "receipt-capture", "a98c301", "Nina Scholl", "initial camera flow and ReceiptCam crop", "mobile/camera", "4.3-pilot"],
                ["2024-03-01", "receipt-capture", "bb96d72", "Nina Scholl", "record SPDX metadata for image packages", "pubspec; NOTICE", "4.3-pilot"],
                ["2025-05-16", "fiscuspilot-core", "7ae415e", "Lena Vogt", "support 2025 advance VAT schema", "core/vat", "4.5.2"],
                ["2025-09-12", "fiscuspilot-web", "fc3e117", "Jonas Eberle", "replace table virtualization package", "src/components/table", "4.6.0"],
                ["2026-01-23", "platform-deploy", "33bdc04", "Esra Kaya", "SBOM attestation in release pipeline", "ci/release", "4.6.4"],
                ["2026-06-05", "receipt-capture", "616df22", "Nina Scholl", "OCR retry and crop fallback", "worker/ocr; mobile/camera", "4.7.0"],
                ["2026-09-18", "fiscuspilot-core", "4b786d0", "Lena Vogt", "prepare 2027 rule tables without release", "core/rules/2027", "unreleased"],
            ],
        ),
        _xlsx(
            "02_Unternehmen_Produkt/05_Releasehistorie.xlsx",
            "Releasehistorie und Auslieferungsstand",
            [
                {
                    "name": "Releases",
                    "headers": ["Version", "Datum", "Produktzweig", "Git-Tag", "Signiert", "Wesentliche Änderung", "Kundenstand"],
                    "rows": [
                        ["1.1", "20.02.2018", "TaxEngine Classic", "classic-1.1", "nein", "USt-Zeitraumregeln", "3 Altinstallationen"],
                        ["2.0", "28.06.2019", "FiscusPilot Kanzlei", "fp-2.0.0", "ja", "neuer Kern und Classic-Adapter", "außer Betrieb"],
                        ["2.7", "09.10.2020", "FiscusPilot Kanzlei", "fp-2.7.0", "ja", "Webformular-Framework", "7 On-Premise"],
                        ["3.0", "30.04.2021", "Cloud", "fp-3.0.0", "ja", "mandantenfähiger Cloudbetrieb", "außer Betrieb"],
                        ["3.8", "16.12.2022", "Mittelstand", "fp-3.8.0", "ja", "LedgerFlow Pilot", "12 Kunden"],
                        ["4.0", "30.06.2023", "beide", "fp-4.0.0", "ja", "vereinheitlichter Regelkern", "24 On-Premise"],
                        ["4.3-pilot", "22.03.2024", "Mobile", "receipt-0.7", "Pilot", "Belegerfassung", "6 Pilotkunden"],
                        ["4.5.2", "23.05.2025", "beide", "fp-4.5.2", "ja", "USt-Schema 2025", "41 On-Premise"],
                        ["4.6.4", "19.02.2026", "beide", "fp-4.6.4", "ja", "SBOM-Attestierung", "aktiver Mindeststand"],
                        ["4.7.0", "26.06.2026", "beide", "fp-4.7.0", "ja", "OCR und neue Freigaben", "Mehrheit der Kunden"],
                        ["4.7.1", "28.08.2026", "Cloud", "fp-4.7.1", "ja", "Sicherheitskorrekturen", "Cloud produktiv"],
                        ["4.8.0", "nicht freigegeben", "beide", "kein Tag", "nein", "Regeltabellen 2027", "Entwicklungszweig"],
                    ],
                },
                {
                    "name": "Kundenstaende",
                    "headers": ["Kundengruppe", "Anzahl", "Version", "Bereitstellung", "Updatefenster", "Hinweis"],
                    "rows": [
                        ["Cloud Kanzlei", 105, "4.7.1", "SaaS", "zentral", "gemeinsamer Tenant-Cluster"],
                        ["Cloud Mittelstand", 65, "4.7.1", "SaaS", "zentral", "LedgerFlow aktiv"],
                        ["On-Premise aktuell", 29, "4.7.0", "Container", "kundenseitig", "Support bis 30.06.2027"],
                        ["On-Premise 4.5.x", 12, "4.5.2", "Container", "kundenseitig", "Migration angeboten"],
                        ["Altinstallationen", 3, "Classic 1.1", "Java Paket", "kein reguläres Update", "Sonderpflege"],
                        ["Mobile Pilot", 18, "receipt 0.9", "App/Cloud", "monatlich", "keine allgemeine Freigabe"],
                    ],
                },
            ],
        ),
        _xlsx(
            "02_Unternehmen_Produkt/06_SBOM_Open_Source.xlsx",
            "Software Bill of Materials und Open-Source-Prüfliste",
            [
                {
                    "name": "Komponenten",
                    "headers": ["Komponente", "Version", "Lizenz", "Repository", "Einsatz", "Quelle", "Prüfstatus"],
                    "rows": [
                        ["Spring Boot", "3.3.2", "Apache-2.0", "fiscuspilot-core", "Backend Framework", "Maven Central", "Hinweise vorhanden"],
                        ["Kotlin", "2.0.10", "Apache-2.0", "fiscuspilot-core", "Sprache/Runtime", "JetBrains", "Hinweise vorhanden"],
                        ["PostgreSQL JDBC", "42.7.4", "BSD-2-Clause", "fiscuspilot-core", "Datenbankzugriff", "Maven Central", "Hinweise vorhanden"],
                        ["React", "18.3.1", "MIT", "fiscuspilot-web", "Weboberfläche", "npm", "Hinweise vorhanden"],
                        ["AG Grid Community", "32.0.2", "MIT", "fiscuspilot-web", "Tabellen", "npm", "Hinweise vorhanden"],
                        ["FormKit helpers", "commit 8f21", "MIT laut NOTICE", "fiscuspilot-web", "Formularhilfen", "Vorbestand Jonas Eberle", "Quellherkunft manuell prüfen"],
                        ["Terraform", "1.9.3", "BUSL-1.1", "platform-deploy", "Build/Deployment", "HashiCorp", "nur Werkzeug laut Technik"],
                        ["Helm", "3.15.4", "Apache-2.0", "platform-deploy", "Deployment", "CNCF", "Hinweise vorhanden"],
                        ["pandas", "2.2.2", "BSD-3-Clause", "ledger-flow", "Importverarbeitung", "PyPI", "Hinweise vorhanden"],
                        ["rapidfuzz", "3.9.6", "MIT", "ledger-flow", "Feldzuordnung", "PyPI", "Hinweise vorhanden"],
                        ["LedgerLens adapter", "0.4", "interne Vorarbeit laut Anlage", "ledger-flow", "Importadapter", "Marek Nowak", "Vertragsanlage abgleichen"],
                        ["Flutter", "3.24", "BSD-3-Clause", "receipt-capture", "Mobile App", "Google", "Hinweise vorhanden"],
                        ["ReceiptCam crop", "commit 1a77", "Vorbestand laut Personalakte", "receipt-capture", "Bildzuschnitt", "Nina Scholl", "Anlage nicht gegengezeichnet"],
                        ["Ghostscript wrapper", "1.2.0", "AGPL-3.0-only", "fiscuspilot-core", "pdf-merge-service", "vendored archive", "manuelle Prüfung offen"],
                        ["OpenSSL", "3.3.1", "Apache-2.0", "Container Base", "TLS", "Distribution package", "Hinweise im Image"],
                        ["BinderRules", "2.4/fortgeschrieben", "Freelancer-Anlage", "taxengine-legacy", "Regelnormalisierung", "Lukas Binder", "Bezeichnungen abgleichen"],
                    ],
                },
                {
                    "name": "Scanbefunde",
                    "headers": ["Fund-ID", "Datum", "Datei/Pfad", "Erkennung", "Teamkommentar", "Beleg", "Status"],
                    "rows": [
                        ["OSS-104", "07.10.2026", "services/pdf-merge/vendor/gs-wrapper.jar", "AGPL-3.0-only", "nur Build-Hilfsdienst, nicht kundenseitig ausgeliefert", "Pipeline-Log noch nicht exportiert", "offen"],
                        ["OSS-117", "07.10.2026", "web/src/forms/helpers", "Ähnlichkeit externes Git-Repository", "FormKit-Vorbestand mit MIT-Vermerk", "Arbeitsvertrag Eberle Anlage A", "offen"],
                        ["OSS-121", "07.10.2026", "legacy/binder-rules", "kein SPDX-Header", "historischer Freelancer-Code", "Vertrag Binder / Anlage Vorbestand", "offen"],
                        ["OSS-135", "07.10.2026", "mobile/camera/crop.dart", "kein externer Pakettreffer", "ReceiptCam-Vorbestand erwähnt", "Personalakte Scholl", "offen"],
                        ["OSS-142", "07.10.2026", "NOTICE.txt", "Lizenzliste älter als lock files", "Release 4.7.1 ohne aktualisierte Anlage", "SBOM Pipeline", "Nachführung geplant"],
                    ],
                },
                {
                    "name": "Policy_Stände",
                    "headers": ["Dokument", "Version", "Gültig ab", "Fundstelle", "Freigabestelle", "Bemerkung"],
                    "rows": [
                        ["Open-Source-Richtlinie", "1.2", "01.03.2021", "Confluence ENG-OSS-12", "CTO", "in Vertrag Kaya genannt"],
                        ["Open-Source-Richtlinie", "2.0", "01.07.2023", "Confluence ENG-OSS-20", "Geschäftsführung", "Copyleft-Ampel"],
                        ["Abhängigkeits-Allowlist", "2026-Q2", "04.04.2026", "GitLab compliance", "Security Lead", "letzter Export vorhanden"],
                        ["Release-Checkliste", "4.6", "15.01.2026", "Confluence REL-46", "Engineering Lead", "SBOM Attestierung"],
                    ],
                },
            ],
        ),
        _doc(
            "02_Unternehmen_Produkt/07_OSS_Pruefnotiz.docx",
            "docx",
            "Technische Notiz zu Open-Source-Befunden",
            sections=[
                _section(
                    "Metadaten",
                    "Erstellt von Meike Lorenz, CodeAudit Süd GmbH, am 8. Oktober 2026 auf Grundlage eines Dateisystem-Scans der am 6. Oktober bereitgestellten Repository-Exporte. Die Notiz beschreibt technische Funde; eine lizenzrechtliche Einordnung war nicht Gegenstand des Auftrags.",
                ),
                _section(
                    "Ghostscript wrapper",
                    "Im Repository fiscuspilot-core liegt unter services/pdf-merge/vendor die Datei gs-wrapper.jar. Die enthaltene Lizenzdatei bezeichnet Version 1.2.0 und AGPL-3.0-only. In der Containerdefinition wird die Datei in ein Image kopiert; aus den vorliegenden Exporten ist nicht sicher erkennbar, ob dieses Image nur in der Build-Umgebung oder auch in Kundenumgebungen betrieben wird.",
                    "Das Engineering-Team teilte im Scan-Call mit, der Dienst sei nach einem Pilotversuch im Jahr 2025 deaktiviert worden. Ein Deployment-Manifest mit deaktivierter Variable liegt vor; die vollständigen produktiven Pipeline-Logs wurden nicht bereitgestellt.",
                ),
                _section(
                    "FormKit helpers und ReceiptCam",
                    "Mehrere Dateien im Webformular-Verzeichnis tragen einen MIT-Hinweis und nennen Jonas Eberle als ursprünglichen Autor. Die Ähnlichkeit zu einem öffentlich erreichbaren früheren Repository wurde im Scan nicht anhand der Commit-Historie bewertet.",
                    "Der mobile Zuschnittcode ist Nina Scholl zugeordnet. Ein automatisierter Fremdcodeabgleich ergab keinen eindeutigen Pakettreffer. In der Personalakte wird jedoch eine private Vorarbeit ReceiptCam erwähnt.",
                ),
                _section(
                    "Historischer Regelkern",
                    "BinderRules enthält überwiegend Quelltexte ohne SPDX-Header. Kommentare nennen Lukas Binder, TaxEngine Classic und in späteren Dateien Dr. Lena Vogt. Die Dateien wurden über mehrere Repositories verschoben; ein gemeinsamer Ursprungs-Commit ist im Export nicht vollständig erhalten.",
                ),
                _section(
                    "Noch benötigte technische Belege",
                    "Benötigt werden die produktiven Deployment-Logs für pdf-merge, die vollständigen Git-Bundles mit Tags, die im Arbeitsvertrag Eberle genannte FormKit-Anlage, die ReceiptCam-Anlage aus der Personalakte sowie der ursprüngliche Export des taxengine-legacy-Repositories.",
                ),
            ],
        ),
    ]
)


CASE["documents"].extend(
    [
        _doc(
            "06_Insolvenz_AssetDeal/01_Insolvenzeroeffnungsbeschluss_AG_Heidelberg.pdf",
            "pdf",
            "Beschluss des Amtsgerichts Heidelberg zur Verfahrenseröffnung",
            sections=[
                _section(
                    "Gericht, Aktenzeichen und Schuldnerin",
                    "Amtsgericht Heidelberg, Insolvenzgericht, Aktenzeichen 51 IN 147/26. In dem Verfahren über das Vermögen der Kurpfalz Taxware GmbH, Im Neuenheimer Feld 583, 69120 Heidelberg, eingetragen im Handelsregister des Amtsgerichts Mannheim unter HRB 731944, gesetzlich vertreten durch Geschäftsführer Martin Reuter.",
                ),
                _section(
                    "Eröffnung",
                    "Das Insolvenzverfahren über das Vermögen der Schuldnerin wird wegen Zahlungsunfähigkeit und Überschuldung am 15. September 2026 um 09:00 Uhr eröffnet. Grundlage sind der Eigenantrag vom 11. August 2026 und das Gutachten der vorläufigen Insolvenzverwalterin vom 10. September 2026.",
                ),
                _section(
                    "Bestellung der Insolvenzverwalterin",
                    "Zur Insolvenzverwalterin wird Rechtsanwältin Dr. Friederike Mohn, Friedrich-Ebert-Anlage 22, 69117 Heidelberg, bestellt. Verfügungen der Schuldnerin über zur Masse gehörende Gegenstände sind nach Verfahrenseröffnung nur nach Maßgabe der gesetzlichen Zuständigkeitsordnung möglich.",
                ),
                _section(
                    "Forderungsanmeldung und Termine",
                    "Gläubiger werden aufgefordert, Forderungen bis zum 20. November 2026 bei der Insolvenzverwalterin anzumelden. Der Berichtstermin wird auf den 8. Dezember 2026 um 10:00 Uhr, der Prüfungstermin auf den 15. Dezember 2026 um 09:30 Uhr im Amtsgericht Heidelberg bestimmt.",
                ),
                _section(
                    "Gläubigerausschuss",
                    "Der mit Beschluss vom 13. August 2026 eingesetzte vorläufige Gläubigerausschuss bleibt bis zu einer Entscheidung der Gläubigerversammlung im Amt. Ihm gehören Vertreterinnen und Vertreter der Arbeitnehmer, der Bundesagentur für Arbeit, eines Lieferanten, der Rhenus Kreditbank AG und der ungesicherten Gläubiger an.",
                ),
                _section(
                    "Rechtsbehelfsbelehrung und Ausfertigung",
                    "Gegen die Eröffnungsentscheidung ist die sofortige Beschwerde nach Maßgabe der gesetzlichen Vorschriften zulässig. Die elektronische Ausfertigung trägt die qualifizierte Signatur der Richterin am Amtsgericht Dr. Amelie Hagedorn und den Prüfvermerk der Urkundsbeamtin K. Sauer vom 15. September 2026.",
                ),
            ],
            tables=[
                {
                    "title": "Verfahrensdaten",
                    "headers": ["Vorgang", "Datum", "Ort/Adressat"],
                    "rows": [
                        ["Eröffnung", "15.09.2026, 09:00 Uhr", "Amtsgericht Heidelberg"],
                        ["Anmeldefrist", "20.11.2026", "Dr. Friederike Mohn"],
                        ["Berichtstermin", "08.12.2026, 10:00 Uhr", "Saal 3, Kurfürsten-Anlage 15"],
                        ["Prüfungstermin", "15.12.2026, 09:30 Uhr", "Saal 3, Kurfürsten-Anlage 15"],
                    ],
                }
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/02_Inventurbericht_Verwalter.docx",
            "docx",
            "Vorläufiger Inventur- und Fortführungsbericht der Insolvenzverwalterin",
            sections=[
                _section(
                    "Auftrag und Stichtag",
                    "Bericht der Insolvenzverwalterin Dr. Friederike Mohn vom 28. September 2026, Stichtag 15. September 2026. Der Bericht dient der ersten Bestandsaufnahme für Gläubigerausschuss und Datenraum; Bewertungen und Rechtezuordnungen bleiben gesonderten Prüfungen vorbehalten.",
                ),
                _section(
                    "Geschäftsbetrieb",
                    "Der Cloudbetrieb und der Support werden mit 19 weiterbeschäftigten Personen fortgeführt. Vier Arbeitsverhältnisse ruhen oder sind beendet. Die Lohnzahlungen für August waren offen; Insolvenzgeldvorfinanzierung wurde mit der Agentur und einer Sparkasse abgestimmt.",
                    "Die Kundenplattform war seit Anordnung der vorläufigen Verwaltung ohne wesentliche Unterbrechung verfügbar. Releases sind bis auf kritische Fehlerbehebungen eingefroren. Das Entwicklungsteam pflegt eine Übergabeliste für Quellcode, Schlüssel und Rechenzentrumszugänge.",
                ),
                _section(
                    "Liquide Mittel und körperliche Gegenstände",
                    "Bankguthaben zum Eröffnungsstichtag beliefen sich nach vorläufiger Abstimmung auf 132.840,77 EUR. Der Bestand umfasst 31 Notebooks, 12 Monitore, drei Testserver, Büromöbel und zwei geleaste Fahrzeuge. Verkehrswert der freien körperlichen Gegenstände nach erster Schätzung: 84.000 EUR.",
                ),
                _section(
                    "Software und gewerbliche Positionen",
                    "Als zentrale immaterielle Positionen wurden Quellcode und Dokumentationen der Produktfamilie FiscusPilot, die Wortmarke FiscusPilot, Domains, Kundenbeziehungen, Konfigurationen, Release-Artefakte und betriebliche Geheimnisse erfasst. Die Repository-Liste nennt acht Projekte und mehrere externe Dienste.",
                    "Im Datenraum liegen fünf Arbeitsverträge und ein Freelancervertrag. Bei den Vorbestandsanlagen FormKit, LedgerLens und ReceiptCam bestehen Dokumentationslücken. Ein Open-Source-Scan wurde beauftragt und am 7. Oktober als Tabellenexport bereitgestellt.",
                ),
                _section(
                    "Sicherheitenhinweise",
                    "Die Rhenus Kreditbank AG hat am 18. August 2026 eine Kopie des Sicherungsvertrags über Software-Nutzungsrechte aus 2023 und der Sicherungsabtretung von Lizenzforderungen aus 2024 vorgelegt. Der Sicherungsvertrag ist im Vertragsregister der Schuldnerin vermerkt; eine getrennte Sicherheitenabrechnung liegt noch nicht vor.",
                    "Mehrere Kundenrechnungen enthalten einen Abtretungshinweis, andere nicht. Zahlungseingänge liefen nach Eröffnung zunächst auf die bisherigen Geschäftskonten und wurden von dort auf das Massekonto übertragen.",
                ),
                _section(
                    "Kundenverträge",
                    "Das CRM weist 229 aktive Kundenbeziehungen aus. Für 187 Kunden liegen unterzeichnete Hauptverträge im zentralen Ordner; bei 42 Kunden bestehen Bestellformulare, ältere Vertragsfassungen oder unvollständige Anlagen. Die zehn größten Vertragsbeziehungen werden gesondert geprüft.",
                ),
                _section(
                    "Fortführungsaufwand",
                    "Für Oktober werden Personal-, Hosting-, Miet- und Dienstleisterkosten von rund 318.000 EUR erwartet. Die laufenden Kundeneingänge decken diesen Betrag nach der rollierenden Planung knapp. Nicht enthalten sind Rechts- und Transaktionskosten sowie mögliche Einmalzahlungen für Schlüssel- oder Vertragsüberleitungen.",
                ),
                _section(
                    "M&A-Prozess",
                    "Nach Ansprache von zwölf strategischen Interessenten erhielten fünf Unternehmen Zugang zum Datenraum. Drei indikative Angebote gingen bis 25. September ein. Weinberg Digital Solutions GmbH legte das höchste verbindliche Barangebot vor und bot die Übernahme von mindestens 17 Beschäftigten an.",
                ),
                _section(
                    "Offene Bestandsfragen",
                    "Noch offen sind die vollständige Zuordnung historischer Quellcodebestandteile, die Reichweite einzelner Kundenübertragungsklauseln, der aktuelle Escrow-Stand, die Behandlung abgetretener Forderungen und die Übergabe des HSM. Diese Punkte wurden in die Transaktions- und Prüfungslisten aufgenommen.",
                ),
            ],
            tables=[
                {
                    "title": "Vorläufige Vermögensübersicht",
                    "headers": ["Position", "Buchwert EUR", "Vorläufiger Wert/Spanne EUR", "Bemerkung"],
                    "rows": [
                        ["Liquide Mittel", 132840.77, 132840.77, "vor Abgrenzung Sicherheiten"],
                        ["Offene Kundenforderungen", 616450, "410.000–505.000", "Einwendungen und Abtretungshinweise"],
                        ["Hardware und Büro", 274000, 84000, "teilweise Leasing"],
                        ["Software, Verträge, Marke, Goodwill", 1860000, "1.600.000–2.400.000", "gesonderte Bewertung"],
                        ["Sonstige Ansprüche", 92000, "25.000–60.000", "Kautionen und Erstattungen"],
                    ],
                }
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/03_Bewertung_Software_und_Vertraege.pdf",
            "pdf",
            "Bewertung FiscusPilot und zugehöriges operatives Geschäft",
            sections=[
                _section(
                    "Auftrag und Bewertungsstichtag",
                    "Bergstraße Advisory GmbH, Mannheim, Gutachterliche Stellungnahme BA-26-117 vom 12. Oktober 2026 im Auftrag der Insolvenzverwalterin. Bewertungsstichtag ist der 30. September 2026. Gegenstand ist ein Verkauf des fortgeführten FiscusPilot-Geschäfts im Asset Deal.",
                    "Die Stellungnahme ist keine rechtliche Due Diligence. Eigentum, Nutzungsrechte, Übertragbarkeit von Verträgen, Sicherheiten und Lizenzkonformität wurden auf Basis der Angaben im Datenraum unterstellt und als Sensitivitäten ausgewiesen.",
                ),
                _section(
                    "Informationsgrundlagen",
                    "Ausgewertet wurden BWA 2024 bis August 2026, Umsatzlisten, CRM-Export, Kundenvertragsmatrix, Personalübersicht, Repository-Liste, Releasehistorie, Darlehens- und Sicherheitenunterlagen, indikative Angebote sowie Management- und Technikgespräche.",
                    "Nicht vollständig vorlagen: alle Kundenanlagen, technische Originalarchive der Vorbestände, produktive Deployment-Logs, Freigabeerklärungen von Sicherheitennehmern und schriftliche Bindungszusagen der Beschäftigten.",
                ),
                _section(
                    "Ertragswertannahmen",
                    "Die Planung geht für 2027 von 2,76 Mio. EUR wiederkehrendem Umsatz, 0,44 Mio. EUR Projekt- und Migrationsumsatz sowie einer bereinigten EBITDA-Marge von 13 Prozent aus. Kundenabwanderung wird im Basisszenario mit 12 Prozent im ersten Jahr und 7 Prozent danach angesetzt.",
                    "Für die Barwertbetrachtung wurde ein Diskontierungssatz von 19,5 Prozent und ein langfristiges Wachstum von 1,5 Prozent verwendet. Ein zusätzlicher Abschlag bildet Integrationskosten und die kurze Transaktionsdauer ab.",
                ),
                _section(
                    "Lizenzpreis- und Wiederbeschaffungsansatz",
                    "Der Lizenzpreisansatz verwendet beobachtete Umsätze der Kernmodule und hypothetische Lizenzsätze zwischen 7 und 10 Prozent. Beim Wiederbeschaffungsansatz wurden 36 bis 48 Personenjahre für Regelkern, Portale, Infrastruktur, Dokumentation und Tests mit altersabhängiger Obsoleszenz berücksichtigt.",
                ),
                _section(
                    "Sensitivitäten",
                    "Die stärksten Werttreiber sind Fortbestand der zehn größten Kundenverträge, Verfügbarkeit des Entwicklungsteams, Nutzbarkeit des historischen Regelkerns, Übergabe der Signatur- und Betriebszugänge sowie Umfang erforderlicher Open-Source-Maßnahmen.",
                    "Die Werte reduzieren sich in den Modellrechnungen deutlich, wenn wichtige Verträge nicht übergeleitet werden, Kernpersonal ausfällt oder einzelne Module neu implementiert werden müssen. Diese Faktoren sind nicht abschließend verifiziert.",
                ),
                _section(
                    "Ergebnis der betriebswirtschaftlichen Bandbreite",
                    "Aus den angewandten Verfahren ergibt sich für die angebotene Gesamtheit aus Software, Kundenbeziehungen, Marke, Dokumentation und Übergangsleistungen eine indikative Bandbreite von 1,60 Mio. EUR bis 2,40 Mio. EUR. Der gewichtete Orientierungspunkt beträgt 1,95 Mio. EUR vor Transaktionskosten.",
                    "Die Bandbreite setzt eine geordnete technische Übergabe und die in den Szenarien jeweils bezeichnete Kunden- und Personalbindung voraus. Die Stellungnahme trifft keine Aussage dazu, welche Rechtspositionen wirksam übertragen werden können oder wem einzelne Erlöse zustehen.",
                ),
            ],
            tables=[
                {
                    "title": "Bewertungsverfahren",
                    "headers": ["Verfahren", "Niedrig EUR", "Basis EUR", "Hoch EUR", "Gewicht Basis"],
                    "rows": [
                        ["Discounted Cashflow operatives Geschäft", 1450000, 1980000, 2630000, "50 %"],
                        ["Relief-from-Royalty Software/Marke", 1180000, 1740000, 2310000, "30 %"],
                        ["Wiederbeschaffung abzüglich Obsoleszenz", 1660000, 2100000, 2480000, "20 %"],
                        ["Gewichteter Orientierungspunkt", "", 1950000, "", "100 %"],
                    ],
                },
                {
                    "title": "Szenarien",
                    "headers": ["Szenario", "Kundenbindung", "Kernteam", "Code ohne Ersatzaufwand", "Indikative Spanne EUR"],
                    "rows": [
                        ["A – stabile Überleitung", "90 % ARR", "mindestens 12 Entwickler", "ja", "2,10–2,40 Mio."],
                        ["B – Basisszenario", "80 % ARR", "mindestens 9 Entwickler", "überwiegend", "1,75–2,10 Mio."],
                        ["C – Reibungsverluste", "65 % ARR", "mindestens 7 Entwickler", "Ersatzaufwand 350.000", "1,20–1,60 Mio."],
                    ],
                },
                {
                    "title": "Nicht abschließend verifizierte Annahmen",
                    "headers": ["Annahme", "Datenquelle", "Auswirkung im Modell"],
                    "rows": [
                        ["verfügbare Rechte am Regelkern", "Verträge und Managementangabe", "keine vollständige Neuentwicklung"],
                        ["Überleitung Top-10-Kunden", "Vertragsmatrix", "ARR-Bindung"],
                        ["HSM und Release-Schlüssel verfügbar", "Technikgespräch", "keine Release-Verzögerung"],
                        ["OSS-Befunde technisch beherrschbar", "Scan vom 07.10.", "begrenzter Remediation-Aufwand"],
                        ["mindestens 17 Beschäftigte wechseln", "Bieterangebot", "Personalaufwand und Kontinuität"],
                    ],
                },
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx",
            "docx",
            "Asset Purchase Agreement Kurpfalz Taxware / Weinberg Digital",
            sections=[
                _section(
                    "Vertragsparteien",
                    "Dieser Asset Purchase Agreement wird am 19. Oktober 2026 geschlossen zwischen Rechtsanwältin Dr. Friederike Mohn, handelnd ausschließlich als Insolvenzverwalterin über das Vermögen der Kurpfalz Taxware GmbH, als Verkäuferin, und der Weinberg Digital Solutions GmbH, Weinstraße 61, 67146 Deidesheim, vertreten durch Geschäftsführer Leonhard Kern, als Käuferin.",
                ),
                _section(
                    "Präambel",
                    "Über das Vermögen der Kurpfalz Taxware GmbH wurde am 15. September 2026 das Insolvenzverfahren eröffnet. Die Verkäuferin führt das Softwaregeschäft FiscusPilot fort und hat einen strukturierten Investorenprozess durchgeführt.",
                    "Die Käuferin beabsichtigt, die in diesem Vertrag bestimmten Vermögensgegenstände und den operativen Geschäftsbetrieb zu übernehmen. Der Gläubigerausschuss hat dem Abschluss nach dem beigefügten Protokoll am 19. Oktober 2026 zugestimmt.",
                ),
                _section(
                    "Kaufgegenstände",
                    "Die Verkäuferin verkauft an die Käuferin mit wirtschaftlicher Wirkung zum Vollzugstag die in Anlage 2.1 bezeichnete Software, Quell- und Objektcodes, Dokumentationen, Build- und Testbestände, Produktnamen, die Marke FiscusPilot, Domains, Websites, Vertrags- und Kundenunterlagen, Supportwissen, ausgewählte Hardware sowie sonstige ausdrücklich bezeichnete betriebliche Unterlagen.",
                    "Rechtspositionen werden jeweils in dem Umfang verkauft und übertragen, in dem sie der Masse zustehen, übertragbar sind und die Verkäuferin darüber verfügen kann. Bei fortbestehenden Mitwirkungs- oder Zustimmungserfordernissen gilt Abschnitt 9.",
                ),
                _section(
                    "Ausgenommene Gegenstände",
                    "Nicht verkauft werden Bankguthaben, Kassenbestände, Steuererstattungsansprüche, Ansprüche aus Insolvenzanfechtung, Organhaftungsansprüche, gesellschaftsrechtliche Beteiligungen, nicht in Anlage 2.1 bezeichnete Forderungen sowie Bücher und Unterlagen, die die Verkäuferin zur Verfahrensführung benötigt.",
                    "Personenbezogene Daten werden nur im gesetzlich zulässigen und zur Vertragsdurchführung erforderlichen Umfang übergeben. Sicherungskopien für gesetzliche Aufbewahrungspflichten dürfen bei der Verkäuferin verbleiben.",
                ),
                _section(
                    "Kundenverträge und Vertragsangebote",
                    "Die Käuferin übernimmt die in Anlage 5.1 aufgeführten Kundenverträge mit Wirkung zum Vollzugstag, soweit die jeweilige Vertragsübernahme wirksam vollzogen werden kann. Die Parteien versenden abgestimmte Kundenmitteilungen und holen erforderliche Zustimmungen ein.",
                    "Bis zur wirksamen Überleitung eines Vertrags führt die Verkäuferin ihn, soweit rechtlich und tatsächlich möglich, im wirtschaftlichen Interesse und auf Rechnung der Käuferin fort. Eine solche Zwischenführung endet spätestens am 31. Januar 2027, sofern die Parteien keine schriftliche Verlängerung vereinbaren.",
                ),
                _section(
                    "Forderungen und Verbindlichkeiten",
                    "Die Käuferin erwirbt nur die in Anlage 6.1 einzeln aufgeführten Forderungen für Leistungszeiträume ab dem Vollzugstag. Forderungen für frühere Leistungszeiträume und sonstige Insolvenzforderungen oder Masseforderungen verbleiben bei der Verkäuferin, soweit Anlage 6.1 nichts Abweichendes festhält.",
                    "Die Käuferin übernimmt ausschließlich die in Anlage 6.2 bezeichneten Verpflichtungen, insbesondere laufende Hosting- und Supportpflichten ab dem Vollzugstag sowie ausgewählte Urlaubs- und Zeitguthaben. Andere Verbindlichkeiten werden nicht rechtsgeschäftlich übernommen.",
                ),
                _section(
                    "Kaufpreis und Zuordnung",
                    "Der Gesamtkaufpreis beträgt 1.850.000,00 EUR. Davon entfallen nach der vertraglichen Zuordnung 1.050.000,00 EUR auf Software und Dokumentation, 360.000,00 EUR auf Kundenbeziehungen und Vertragspositionen, 140.000,00 EUR auf Marke, Domains und Goodwill, 80.000,00 EUR auf Hardware und 220.000,00 EUR auf Übergangs- und Fortführungswerte.",
                    "Ein Betrag von 150.000,00 EUR wird bis 31. Januar 2027 auf einem Anderkonto zurückbehalten und nach den Regelungen zu fehlenden Kundenüberleitungen und nicht übergebenen technischen Schlüsseln abgerechnet.",
                ),
                _section(
                    "Kaufpreiszahlung",
                    "1.700.000,00 EUR sind spätestens am Vollzugstag um 12:00 Uhr auf das in der Closing-Notice bezeichnete Anderkonto der Verkäuferin zu zahlen. Der zurückbehaltene Betrag ist zeitgleich auf das gesonderte Anderkonto einzuzahlen. Zahlung an andere Konten erfüllt die Kaufpreispflicht nicht.",
                ),
                _section(
                    "Zustimmungen und nicht sofort übertragbare Positionen",
                    "Soweit eine Zustimmung, Freigabe oder Mitwirkung eines Kunden, Lizenzgebers, Sicherheitennehmers, Providers oder sonstigen Dritten erforderlich ist, wirken die Parteien auf deren Erhalt hin. Das wirtschaftliche Ergebnis soll bis dahin durch zulässige Zwischenregelungen abgebildet werden; keine Partei ist verpflichtet, an unzulässigen Handlungen mitzuwirken.",
                    "Die Käuferin ist über die in Anlage 9.2 aufgeführten Hinweise auf Sicherheitenverträge der Rhenus Kreditbank AG, Vorbestandsklauseln, Open-Source-Befunde und unvollständige Kundenanlagen informiert. Die rechtlichen Standpunkte der Verkäuferin, der Bank und Dritter werden durch diese Kenntnisnahme nicht festgelegt.",
                ),
                _section(
                    "Technische Übergabe",
                    "Am Vollzugstag werden Git-Bundles, Container-Manifeste, Dokumentationsarchive, Administrationskonten, Domain-Transfercodes und die in Anlage 10.1 bezeichneten Geräte übergeben. Signatur- und HSM-Zugänge werden in einem gesonderten Vier-Augen-Termin protokolliert.",
                    "Für jeden Export werden Dateigröße, Zeitstempel und SHA-256-Hash festgehalten. Die Verkäuferin behält eine versiegelte Kopie für Verfahrens- und Nachweiszwecke.",
                ),
                _section(
                    "Beschäftigte",
                    "Die Käuferin plant, den in Anlage 11.1 bezeichneten 17 Beschäftigten eine Fortsetzung ihrer Tätigkeit zu den dort beschriebenen Konditionen anzubieten beziehungsweise gesetzliche Übergänge zu berücksichtigen. Die Parteien erfüllen die jeweils anwendbaren Informations- und Beteiligungspflichten.",
                    "Individuelle Erklärungen der Beschäftigten zur Fortsetzung, zu Vorbeständen oder zu Nebentätigkeiten werden durch diesen Vertrag nicht ersetzt.",
                ),
                _section(
                    "Vollzugsvoraussetzungen",
                    "Vollzugsvoraussetzungen sind die Zustimmung des Gläubigerausschusses, Eingang der ersten Kaufpreisrate, Unterzeichnung der Übergangsleistungsvereinbarung, Vorliegen einer kartellrechtlichen Unbedenklichkeitserklärung, soweit erforderlich, und kein gerichtliches Verbot des Vollzugs.",
                    "Eine Freigabeerklärung der Rhenus Kreditbank AG wird in der von beiden Parteien unterzeichneten Fassung nicht als eigene Vollzugsvoraussetzung aufgeführt. Anlage 12.2 führt die Klärung der Bankposition als offenen Vollzugspunkt der Verkäuferin.",
                ),
                _section(
                    "Vollzugshandlungen",
                    "Der Vollzug ist für den 28. Oktober 2026 um 14:00 Uhr vorgesehen. Die Parteien tauschen eine Closing-Notice, Kaufpreisbestätigung, Übergabeprotokolle, Kundenmitteilungen, Domain-Transfers, Schlüsselprotokolle und die aktualisierten Anlagen aus. Der Vollzug wird durch beiderseitig unterzeichnete Closing Minutes festgestellt.",
                ),
                _section(
                    "Kenntnisstand und Beschaffenheit",
                    "Die Käuferin hatte Zugang zum Datenraum, hat technische und kaufmännische Gespräche geführt und erwirbt die Kaufgegenstände im bei Signing dokumentierten Zustand. Die Verkäuferin gibt nur die in diesem Vertrag ausdrücklich niedergelegten Erklärungen ab und übernimmt keine Garantie für künftige Umsätze, Kundenbindung oder lückenlose technische Dokumentation.",
                    "Die Verkäuferin erklärt nach ihrer tatsächlichen Kenntnis, keine im Datenraum nicht offengelegte ausschließliche Veräußerung der FiscusPilot-Produktlinie vorgenommen zu haben. Offengelegte Sicherheiten, Drittkomponenten, Vorbestände und Vertragsbeschränkungen bleiben von dieser Erklärung ausgenommen.",
                ),
                _section(
                    "Haftung und Rückbehalt",
                    "Die Haftung der Verkäuferin ist, soweit gesetzlich zulässig, auf vorsätzliche Pflichtverletzungen und ausdrücklich übernommene Garantien beschränkt. Ansprüche werden vorrangig aus dem Rückbehalt befriedigt; zwingende gesetzliche Haftung bleibt unberührt.",
                    "Die Käuferin meldet geltend gemachte Abzüge bis zum 15. Januar 2027 mit Belegen an. Streitige Beträge bleiben bis zur Einigung oder rechtskräftigen Entscheidung auf dem Anderkonto.",
                ),
                _section(
                    "Übergangsleistungen",
                    "Die Verkäuferin unterstützt für bis zu drei Monate Abrechnung, Kundenkommunikation, Datenexporte und Providerwechsel. Die Käuferin trägt ab Vollzug die laufenden Dritt- und Personalkosten der übernommenen Leistungen gemäß Anlage 16.1.",
                ),
                _section(
                    "Vertraulichkeit und Kommunikation",
                    "Bis zur gemeinsamen Mitteilung behandeln die Parteien Kaufpreis, Anlagen und Vollzugsablauf vertraulich, soweit Verfahrens-, Organ- oder gesetzliche Informationspflichten nicht entgegenstehen. Kunden- und Beschäftigteninformationen werden inhaltlich abgestimmt und mit den jeweils erforderlichen Vorbehalten versehen.",
                ),
                _section(
                    "Schlussbestimmungen",
                    "Es gilt deutsches Recht. Gerichtsstand ist, soweit zulässig, Heidelberg. Änderungen und Ergänzungen dieses Vertrags bedürfen der Textform, soweit keine strengere Form gilt. Die Anlagen 2.1 bis 18.3 sind Vertragsbestandteil.",
                ),
                _section(
                    "Unterschriften",
                    "Heidelberg, 19.10.2026 — Dr. Friederike Mohn, ausschließlich als Insolvenzverwalterin über das Vermögen der Kurpfalz Taxware GmbH, handschriftlich unterzeichnet um 17:46 Uhr.",
                    "Deidesheim, 19.10.2026 — Weinberg Digital Solutions GmbH, Leonhard Kern, Geschäftsführer, qualifiziert elektronisch unterzeichnet um 18:12 Uhr. Signaturprüfprotokoll und gegengezeichnete Anlagenliste sind beigefügt.",
                ),
            ],
            tables=[
                {
                    "title": "Anlage 2.1 – wesentliche Kaufgegenstände",
                    "headers": ["Position", "Gegenstand", "Fundstelle", "Übertragungsweg", "Offener Hinweis"],
                    "rows": [
                        ["2.1.1", "FiscusPilot Core/TaxEngine einschließlich legacy", "GitLab Bundle", "Rechtseinräumung und Datenübergabe", "BinderRules/Vorbestand"],
                        ["2.1.2", "FiscusPilot Web", "GitLab Bundle", "Rechtseinräumung und Datenübergabe", "FormKit-Anlage"],
                        ["2.1.3", "LedgerFlow", "GitLab Bundle", "Rechtseinräumung und Datenübergabe", "LedgerLens-Anlage"],
                        ["2.1.4", "Receipt Capture", "GitLab Bundle", "Rechtseinräumung und Datenübergabe", "ReceiptCam-Anlage"],
                        ["2.1.5", "Plattform- und Deploymentcode", "GitLab/Registry", "Daten- und Zugangübergabe", "HSM separat"],
                        ["2.1.6", "Marke FiscusPilot", "DE 302019114477", "Übertragungserklärung", "Registerumschreibung"],
                        ["2.1.7", "Domains", "Providerliste", "Auth-Codes", "Providerfreigaben"],
                        ["2.1.8", "Kunden- und Supportdokumentation", "Confluence Export", "Datenübergabe", "Autorenliste"],
                    ],
                },
                {
                    "title": "Anlage 9.2 – offengelegte Punkte",
                    "headers": ["ID", "Dokument/Punkt", "Datenraum", "Kenntnisnahme Käuferin"],
                    "rows": [
                        ["D-01", "IP-Sicherungsvertrag Rhenus Kreditbank 15.03.2023", "Finance/03", "Q&A-Antwort 14.10."],
                        ["D-02", "Sicherungsabtretung Forderungen 01.02.2024", "Finance/04", "Q&A-Antwort 14.10."],
                        ["D-03", "Freelancer Binder samt Anlage", "HR/IP/08-09", "Tech Call 12.10."],
                        ["D-04", "Personalakten-Auszüge fünf Entwickler", "HR/IP/01-07", "Q&A 15.10."],
                        ["D-05", "OSS-Scan mit offenen Befunden", "Tech/OSS/06-07", "Q&A 15.10."],
                        ["D-06", "Kundenvertragsmatrix", "Commercial/04", "Commercial Call 16.10."],
                    ],
                },
            ],
        ),
        _xlsx(
            "06_Insolvenz_AssetDeal/05_Closing_Checkliste.xlsx",
            "Closing-Checkliste Asset Deal – Stand 22. Oktober 2026",
            [
                {
                    "name": "Closing_Items",
                    "headers": ["ID", "Aufgabe/Dokument", "Verantwortlich", "Frist", "Status", "Beleg", "Kommentar"],
                    "rows": [
                        ["C-01", "APA beiderseits unterzeichnet", "Parteien", "19.10.2026", "erledigt", "Signaturpaket", "Anlagenliste gegengezeichnet"],
                        ["C-02", "Zustimmung Gläubigerausschuss", "Verkäuferin", "19.10.2026", "erledigt", "Protokoll GA-09", "4 Ja, 1 Enthaltung"],
                        ["C-03", "Kaufpreis 1,7 Mio. auf Anderkonto", "Käuferin", "28.10.2026 12:00", "offen", "", "Zahlungsavis 27.10. erwartet"],
                        ["C-04", "Rückbehalt 150.000 EUR", "Käuferin", "28.10.2026 12:00", "offen", "", "Anderkontodaten versandt"],
                        ["C-05", "Bankposition Rhenus Kreditbank klären", "Verkäuferin", "26.10.2026", "offen", "Mail 21.10.", "Verkäuferseite: keine Closing Condition; Bankantwort ausstehend"],
                        ["C-06", "Git-Bundles mit Hashliste", "Esra Kaya", "27.10.2026", "in Arbeit", "Export 09.10.", "Delta-Export nach Freeze"],
                        ["C-07", "Container Registry Manifest", "Esra Kaya", "27.10.2026", "in Arbeit", "REG-2026-10", "Signaturen prüfen"],
                        ["C-08", "HSM Vier-Augen-Übergabe", "Esra Kaya / Käuferin", "28.10.2026 09:00", "offen", "", "Treffpunkt Rechenzentrum"],
                        ["C-09", "Domain Auth-Codes", "Nora Schenk", "27.10.2026", "teilweise", "Providerliste", "zwei Domains gesperrt bis Rechnungsausgleich"],
                        ["C-10", "Markenübertragung unterzeichnet", "Verkäuferin/Käuferin", "28.10.2026", "Entwurf", "Anlage M-1", "Einreichung nach Closing"],
                        ["C-11", "Müller & Reiter Zustimmung", "Carlotta Frey", "27.10.2026", "offen", "Mail 21.10.", "Gespräch 23.10."],
                        ["C-12", "Top-10 Kundenmitteilungen", "Nora Schenk / Käuferin", "27.10.2026", "Entwurf", "COMM-01", "Klauseln je Kunde anpassen"],
                        ["C-13", "AVV und Unterauftragnehmerliste", "Käuferin", "23.10.2026", "in Arbeit", "DPA-Entwurf", "Hostingvertrag final fehlt"],
                        ["C-14", "Beschäftigteninformation", "Parteien", "23.10.2026", "Entwurf", "HR-Info v3", "Betriebsratsfrage geprüft"],
                        ["C-15", "Angebote an 17 Beschäftigte", "Käuferin", "26.10.2026", "teilweise", "Offer Tracker", "14 angenommen, 3 Gespräche"],
                        ["C-16", "OSS-Maßnahmenplan", "Käuferin/Engineering", "27.10.2026", "offen", "Scan 07.10.", "kein Closing-Hinderungsgrund im APA definiert"],
                        ["C-17", "Escrow-Status Müller & Reiter", "Verkäuferin", "26.10.2026", "offen", "Escrow-Anfrage", "Q3-Hinterlegung nicht bestätigt"],
                        ["C-18", "Forderungsanlage 6.1 aktualisieren", "Verkäuferin", "27.10.2026", "offen", "ERP 30.09.", "Zahlungen nach Eröffnung abgleichen"],
                        ["C-19", "Übergangsleistungsvertrag", "Parteien", "27.10.2026", "Entwurf abgestimmt", "TSA v7", "Kostenanlage offen"],
                        ["C-20", "Closing Minutes", "Parteien", "28.10.2026 14:00", "Entwurf", "CM v2", "Unterzeichnung im Video-Call"],
                    ],
                },
                {
                    "name": "Kunden_Consents",
                    "headers": ["Kunde", "Mechanismus laut Matrix", "Anfrage", "Rückmeldung", "Status", "Verantwortlich"],
                    "rows": [
                        ["Müller & Reiter", "vorherige Zustimmung", "noch keine formelle Anfrage", "Mail 21.10. mit Unterlagenwunsch", "offen", "Carlotta Frey"],
                        ["PfalzForm", "30-Tage-Information", "Entwurf 20.10.", "keine", "offen", "Nora Schenk"],
                        ["Auer & Hain", "Vorabmitteilung/Widerspruch", "nicht versandt", "keine", "offen", "Nora Schenk"],
                        ["Neckarblick Treuhand", "Zustimmung", "19.10.", "mündlich positiv laut Aktennotiz", "Schriftform offen", "Carlotta Frey"],
                        ["Rheinauer Pumpenbau", "Information", "Entwurf 20.10.", "keine", "offen", "Käuferin"],
                        ["Schwarz & Vetter", "Zustimmung", "20.10.", "Prüfung bis 26.10. angekündigt", "offen", "Carlotta Frey"],
                    ],
                },
                {
                    "name": "Technische_Uebergabe",
                    "headers": ["Asset", "Quelle", "Ziel", "Methode", "Prüfnachweis", "Status"],
                    "rows": [
                        ["Git-Repositories", "GitLab Kurpfalz", "GitLab Weinberg", "Bundle + Delta", "SHA-256 und Tagliste", "Delta offen"],
                        ["Container-Images", "Registry Kurpfalz", "Registry Weinberg", "OCI Export", "Digestliste", "Testimport erfolgt"],
                        ["HSM-Schlüssel", "Rechenzentrum Frankfurt", "HSM Käuferin", "kein Export; kontrollierter Austausch", "Vier-Augen-Protokoll", "Termin gebucht"],
                        ["Confluence", "Cloud Export", "Käufer-Wiki", "HTML/PDF/Anhänge", "Dateiliste", "Export vollständig"],
                        ["Domains", "RheinHost", "Käuferkonto", "Auth-Code", "Providerbestätigung", "teilweise"],
                        ["Kundendaten", "Produktivsystem", "gleiche Plattform bis Migration", "Betriebsübernahme", "Mandantenliste", "Datenschutzunterlagen offen"],
                    ],
                },
            ],
        ),
        _mail(
            "06_Insolvenz_AssetDeal/06_Mail_Verwalter_Vollzug.eml",
            "E-Mail der Insolvenzverwalterin an die Bank zum Vollzug",
            sender="Dr. Friederike Mohn <mohn@insolvenzkanzlei-mohn.example>",
            to=["Silke Brandt <silke.brandt@rhenus-kreditbank.example>"],
            cc=["Carlotta Frey <frey@insolvenzkanzlei-mohn.example>", "transaktion@weinberg-digital.example"],
            date="Wed, 21 Oct 2026 11:08:00 +0200",
            subject="Kurpfalz Taxware GmbH – unterzeichneter APA und Vollzug am 28. Oktober",
            body=(
                "Sehr geehrte Frau Brandt,\n\nanbei übersende ich den am 19. Oktober unterzeichneten "
                "Asset Purchase Agreement mit der Weinberg Digital Solutions GmbH. Der "
                "Gläubigerausschuss hat zugestimmt. Wir bereiten den Vollzug für den 28. Oktober, "
                "14:00 Uhr, vor.\n\nIhre Sicherheitenunterlagen sind im Datenraum offengelegt und im "
                "APA als offener Punkt bezeichnet. Nach unserem derzeitigen Stand ist eine "
                "Freigabe der Bank keine ausdrücklich vereinbarte Closing Condition. Die "
                "Übertragung erfolgt nach dem Vertrag jeweils nur in dem Umfang, in dem die Masse "
                "über die betreffenden Positionen verfügen kann. Damit ist keine Anerkennung oder "
                "Zurückweisung Ihres Rechtsstandpunkts verbunden.\n\nBitte senden Sie uns bis Montag, "
                "26. Oktober, 12:00 Uhr, Ihre konkrete Zuordnung der beanspruchten Rechte und "
                "Forderungen zu den Anlagen des APA sowie etwaige Vorschläge für eine "
                "Sicherheitenabrechnung. Für Freitag biete ich 15:30 Uhr für einen Datenraum-Call an.\n\n"
                "Mit freundlichen Grüßen\nDr. Friederike Mohn\nInsolvenzverwalterin"
            ),
            attachments=[
                "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx",
                "06_Insolvenz_AssetDeal/05_Closing_Checkliste.xlsx",
            ],
        ),
        _mail(
            "06_Insolvenz_AssetDeal/07_Mail_Erwerber_Vorfreude.eml",
            "E-Mail der Erwerberin an das FiscusPilot-Team",
            sender="Leonhard Kern <kern@weinberg-digital.example>",
            to=["fiscuspilot-team@kurpfalz-taxware.example"],
            cc=["Dr. Friederike Mohn <mohn@insolvenzkanzlei-mohn.example>", "people@weinberg-digital.example"],
            date="Tue, 20 Oct 2026 09:14:00 +0200",
            subject="Wir freuen uns auf FiscusPilot und auf das Kennenlernen",
            body=(
                "Liebe Kolleginnen und Kollegen,\n\ngestern haben Frau Dr. Mohn und ich den Kaufvertrag "
                "für das FiscusPilot-Geschäft unterzeichnet. Wir freuen uns sehr auf das Produkt, "
                "seine Kundinnen und Kunden und vor allem auf die Zusammenarbeit mit Ihnen. Unser "
                "Ziel ist, Entwicklung und Support in der Region fortzuführen und Heidelberg mit "
                "unserem Standort in Deidesheim zu verbinden.\n\nDer Vollzug ist für den 28. Oktober "
                "vorgesehen und steht noch unter den im Vertrag beschriebenen Schritten. Bis dahin "
                "ändert diese Nachricht weder Zuständigkeiten noch Arbeitsabläufe. Bitte folgen Sie "
                "für Releases, Kundenkommunikation und Zugänge weiterhin den Anweisungen des "
                "Verwalterteams. Am Donnerstag um 16:00 Uhr bieten wir ein freiwilliges "
                "Kennenlernen per Video an; individuelle Vertragsfragen besprechen wir getrennt.\n\n"
                "Herzliche Grüße aus Deidesheim\nLeonhard Kern\nGeschäftsführer"
            ),
            attachments=[],
        ),
    ]
)


_replaced_paths = {
    "01_Mandat/04_Beteiligte_und_Kontakte.xlsx",
    "03_Personal_Rechtekette/07_Uebergabeprotokoll_Marek_Nowak.pdf",
}
CASE["documents"] = [
    document for document in CASE["documents"] if document["path"] not in _replaced_paths
]
CASE["documents"].extend(
    [
        _mail(
            "02_Unternehmen_Produkt/08_Mail_Engineering_Uebergabe.eml",
            "Engineering-Mail zum Repository-Freeze und zur technischen Übergabe",
            sender="Esra Kaya <esra.kaya@kurpfalz-taxware.example>",
            to=[
                "Dr. Friederike Mohn <mohn@insolvenzkanzlei-mohn.example>",
                "tech-transition@weinberg-digital.example",
            ],
            cc=[
                "Dr. Lena Vogt <lena.vogt@kurpfalz-taxware.example>",
                "Carlotta Frey <frey@insolvenzkanzlei-mohn.example>",
            ],
            date="Thu, 22 Oct 2026 13:26:00 +0200",
            subject="FiscusPilot: Freeze, Delta-Export und HSM-Übergabe am 28.10.",
            body=(
                "Hallo zusammen,\n\nfür die geplante Übergabe kann ich am 27. Oktober um 18:00 Uhr "
                "einen Schreibstopp auf den sechs aktiven Repositories setzen und danach Bundle, "
                "Tagliste, Commit-Export sowie OCI-Manifeste mit SHA-256-Hashes erzeugen. Bitte "
                "bestätigt, ob kritische Hotfixes danach nur noch über ein gemeinsames Vier-Augen-"
                "Verfahren laufen sollen.\n\nZwei Punkte sind technisch noch offen: Im Core-Bundle liegt "
                "weiterhin legacy/binder-rules; ich kann die Historie bis zum Import 2019 zeigen, "
                "nicht aber das ursprüngliche private Repository von Lukas Binder. Außerdem ist der "
                "Ghostscript-Wrapper noch im Build-Kontext, obwohl das zugehörige Deployment in der "
                "Produktion deaktiviert ist. Ich hänge deshalb keinen bereinigten Export an, sondern "
                "den vorhandenen Stand mit Fundstellen.\n\nDer HSM-Termin im Frankfurter Rechenzentrum "
                "ist für 28. Oktober, 09:00 Uhr, reserviert. Der Schlüssel ist nicht exportierbar; wir "
                "können nur Zertifikate, Berechtigungen und den kontrollierten Wechsel protokollieren. "
                "Für den Zutritt brauche ich bis Montag die Namen und Ausweisnummern der zwei Personen "
                "von Weinberg Digital.\n\nViele Grüße\nEsra"
            ),
            attachments=[
                "02_Unternehmen_Produkt/03_Repositoryverzeichnis.xlsx",
                "02_Unternehmen_Produkt/04_Git_Commit_Export.csv",
                "02_Unternehmen_Produkt/06_SBOM_Open_Source.xlsx",
            ],
        ),
        _mail(
            "05_Finanzierung_Sicherheiten/11_Mail_Bankintern_Rechtekettenluecken.eml",
            "Bankinterne E-Mail zu offenen Rechteketten- und Forderungsdaten",
            sender="Silke Brandt <silke.brandt@rhenus-kreditbank.example>",
            to=[
                "Jan Küster <jan.kuester@rhenus-kreditbank.example>",
                "rechtsabteilung@rhenus-kreditbank.example",
            ],
            cc=["workout-team@rhenus-kreditbank.example"],
            date="Thu, 22 Oct 2026 07:42:00 +0200",
            subject="KTW/FiscusPilot: Unterlagenlücken vor externer Prüfung",
            body=(
                "Guten Morgen,\n\nbevor wir die Akte an die externe IP-Beratung geben, bitte ich um "
                "Abgleich der Tatsachen. Unser Sicherungsvertrag nennt FiscusPilot, TaxEngine und "
                "Nachfolgeversionen, aber nicht alle heutigen Repository-Namen. In der Personalakte "
                "sind TaxParse, FormKit, LedgerLens und ReceiptCam unterschiedlich behandelt; bei "
                "drei Anlagen fehlt entweder ein Archiv, eine Seite oder eine Gegenzeichnung. Beim "
                "Freelancer Binder scheint der Altcode nur teilweise als neu geschaffen bezeichnet.\n\n"
                "Bitte prüft außerdem, welche Debitoren die Abtretungsanzeige 2024 tatsächlich "
                "bestätigt haben. Die Oktoberrechnung PfalzForm weist keine Fußzeile auf, und mehrere "
                "Zahlungen nach Verfahrenseröffnung sind erst auf operative Konten und dann auf das "
                "Massekonto gelaufen. Ich möchte Software-Rechte und Forderungen in der Besprechung "
                "getrennt halten.\n\nDas ist noch keine rechtliche Bewertung. Markiert bitte bis 11:00 "
                "Uhr nur belegte Abweichungen und fehlende Originale; offene Rechtsfragen gehen gesammelt "
                "an die externe Kanzlei.\n\nDanke und viele Grüße\nSilke"
            ),
            attachments=[
                "03_Personal_Rechtekette/06_Rechte_und_Nebentaetigkeiten_Matrix.xlsx",
                "05_Finanzierung_Sicherheiten/03_Anlage_IP_Rechtebestand.xlsx",
                "05_Finanzierung_Sicherheiten/06_Rechnungen_und_Forderungen.xlsx",
            ],
        ),
    ]
)

CASE["documents"].sort(key=lambda document: document["path"])

__all__ = ["CASE"]
