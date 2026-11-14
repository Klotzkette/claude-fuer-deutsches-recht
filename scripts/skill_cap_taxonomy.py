"""Fachliche Auswahlwege und überprüfbare Zuordnungshilfen für große Bestände.

Kein Laufzeitklassifikator: Die Migration verwendet ausschließlich die explizite
und anschließend überprüfte JSON-Registry. Alle Fachtexte bleiben vollständig.
"""
TOPICS = {
 'berufsrecht': [
  ('Berufszugang und Organisation: Zulassung, Status, Berufsausübungsgesellschaft, Syndikusstellung und grenzüberschreitende Tätigkeit prüfen.', r'zulassung|syndikus|berufszugang|gesellschaft|rechtsform|niederlass|berufsqualifikation|ausland|internation'),
  ('Mandat und Interessenkollision: Auftrag, Unabhängigkeit, Konflikt, Mehrfachvertretung und Mandatsbeendigung anhand der Beteiligten prüfen.', r'kollision|interessen|unabhaengig|mandats|mandat-|neben|mehrfach|parteiwechsel'),
  ('Verschwiegenheit und Daten: Geheimnisse, Akten, Datenschutz, KI, Cloud und Auslagerung im konkreten Arbeitsablauf absichern.', r'verschwiegen|geheim|datenschutz|daten|cloud|ki-|legal-tech|outsourc|akten|information|auskunft'),
  ('Vergütung und Vermögenspflichten: Honorar, Gebühren, Fremdgeld, Geldwäsche, Versicherung und wirtschaftliche Pflichten getrennt bearbeiten.', r'honorar|verguet|gebuehr|fremdgeld|geldwaesch|versicherung|steuer|vermoegen|rechnung|erfolgshonorar|rvg|gnotkg|stbvv|geld'),
  ('Außenauftritt und Kanzleipraxis: Werbung, Kommunikation, Fortbildung, Personal, Erreichbarkeit und Nachfolge an den Berufspflichten messen.', r'werbung|google|social|kommunikation|fortbildung|personal|kanzlei|bea|signatur|vertretung|nachfolge|unsachlichkeit'),
  ('Kammer und Berufsverfahren: Aufsichtsanfrage, Rüge, berufsgerichtlichen Vorwurf, Sanktion und Rechtsbehelf mit Beweisen und Fristen bearbeiten.', r'kammer|aufsicht|ruege|berufsgericht|verfahren|sanktion|widerruf|straf|rechtsschutz|frist|beschwerde'),
 ],
 'miet': [
  ('Mietvertrag und Gebrauchsrechte: Vertrag, Parteien, Wohnraum oder Gewerbe, Überlassung und Nutzungsgrenzen konkret prüfen.', r'vertrag|gewerbe|untermiet|gebrauch|tierhalt|rauch|wohnflaeche|vermiet|agb|besichtigung'),
  ('Miete und Betriebskosten: Miethöhe, Erhöhung, Mietpreisbremse, Index, Staffel, Abrechnung und Umlageschlüssel rechnerisch prüfen.', r'mietpreis|mieterhoeh|miete-|mietspiegel|index|staffel|betriebskosten|nebenkosten|umlage|heizkosten|kostenabrechnung'),
  ('Mangel und Instandhaltung: Mangel, Minderung, Erhaltung, Modernisierung und Schadensersatz mit Zustand und Zugang abgleichen.', r'mangel|maengel|minderung|instand|reparatur|modernis|schimmel|schoenheit|baulaerm|schaden'),
  ('Kündigung und Rückgabe: Kündigung, Eigenbedarf, Zahlungsrückstand, Räumung, Rückgabe und Kaution bis zum Schreiben oder Antrag führen.', r'kuendig|eigenbedarf|raeum|rueckgabe|kaution|zahlungsverzug|rueckstand|vollstreck'),
  ('WEG und Beschlüsse: Gemeinschaft, Eigentümer, Versammlung, Stimmrecht, Beschlussfassung und Anfechtung auf die konkrete Maßnahme anwenden.', r'weg|wohnungseigentum|gemeinschaft|eigentuem|beschluss|versammlung|verwalter|sonderumlage'),
  ('Rechtsschutz und Einigung: Anspruch, Beweis, Frist, Klage, Eilrechtsschutz und Vergleich bis zum nutzbaren Prozess- oder Einigungstext bearbeiten.', r'klage|gericht|prozess|beweis|frist|vergleich|verhandlung|rechtsmittel|anspruch|titel'),
 ],
 'ma_finanzierung': [
  ('Transaktion und Struktur: Share Deal, Asset Deal, Beteiligte, Erwerbsstruktur und maßgebliche Rechtsordnung festlegen.', r'asset-deal|share-deal|struktur|transaktion|rechtsform|carve|umwand|merger|fusions|public-ma|investitionskontrolle'),
  ('Due Diligence und Risikoprüfung: Datenraum, Verträge, Personal, IP, IT, Compliance und erkennbare Risiken belegen und für die Transaktion bewerten.', r'due-diligence|datenraum|dataroom|ip-|it-|compliance|personal|arbeits|dokument|disclosure|red-flag'),
  ('Kaufvertrag und Preis: Kaufgegenstand, Kaufpreis, Garantien, Freistellungen, Haftung und Anpassungsmechanik ausformulieren.', r'spa|purchase|kaufpreis|kaufvertrag|warranty|garant|indemnit|freistell|haftung|earn|locked|leakage|escrow|mac-|tax-covenant'),
  ('Finanzierung und Beteiligung: Equity, Darlehen, Wandlung, Sicherheiten, Gesellschafterdarlehen und Kapitalmaßnahmen anhand der Vertragsunterlagen gestalten.', r'finanz|financ|darlehen|loan|equity|venture|kapital|wand[e]?l|convert|mezzan|security|sicherheit|covenant|cap-table'),
  ('Governance und Gesellschafter: Beteiligungsrechte, Organe, Beirat, Management, Vergütung und Exit im Gesellschaftsvertrag abstimmen.', r'governance|beirat|organ|gesellschafter|shareholder|management|vesting|exit|leaver|tag-along|drag-along|stimm|sperrminor|satzung|hauptversammlung'),
  ('Signing und Vollzug: Bedingungen, Unterschriften, Notar, Register, Closing, Übertragung und Integration bis zur dokumentierten Umsetzung führen.', r'signing|closing|vollzug|notar|register|integration|uebertrag|vollmacht|resolution|cp-|conditions'),
  ('Krise und Streit: Sanierung, Insolvenz, Sanierungsgewinn, Organhaftung und Transaktionsstreit mit dem richtigen Anspruchsinhaber prüfen.', r'sanier|insolvenz|krise|distress|restruktur|streit|arbitrat|prozess|klage|rechtsschutz|organhaft'),
 ],
 'straf': [
  ('Tatvorwurf und materielles Recht: Tatbestand, Beteiligung, Irrtum, Rechtfertigung, Schuld und Konkurrenz am belegten Geschehen prüfen.', r'tatbestand|stgb|betrug|untreue|diebstahl|koerperverletz|toetung|mord|sexual|noetig|drohung|beleidig|drogen|betaeub|btm|kcan|cannabis|waffen|brandstift|umwelt|steuerstraf|korrupt|geldwaesch'),
  ('Ermittlungsverfahren und Eingriffe: Beschuldigung, Polizei, Staatsanwaltschaft, Durchsuchung, Beschlagnahme, Haft und Beschuldigtenrechte bearbeiten.', r'ermitt|durchsuch|beschlag|haft|polizei|staatsanwalt|beschuldigt|vernehm|schweige|zwangsmass|sicherstell|kontosperr'),
  ('Beweis und Aktenanalyse: Akteninhalt, Aussage, Sachverständige, digitale Daten und Beweisverwertung mit Widersprüchen und Grenzen auswerten.', r'beweis|zeuge|aussage|gutacht|sachverstaendig|digital|forens|akten|dna|identif|rekonstru|audio|video|chat'),
  ('Anklage und Hauptverhandlung: Anklage, Zwischenverfahren, Einlassung, Beweisantrag, Verhandlung und Verständigung bis zum Schriftsatz vorbereiten.', r'anklage|hauptverhandlung|zwischenverfahren|einlassung|verstaendig|beweisantrag|verfahrensruege|befangen|pl[ae]doyer|sitzung|verteidigung|dysfunk'),
  ('Entscheidung und Rechtsmittel: Einstellung, Strafbefehl, Urteil, Strafzumessung, Berufung und Revision mit Form und Frist bearbeiten.', r'einstellung|strafbefehl|urteil|strafzumess|berufung|revision|rechtsmittel|beschwerde|frist|wiedereinsetzung'),
  ('Sanktion und Vollstreckung: Strafe, Bewährung, Maßregel, Einziehung, Vollzug und nachträgliche Entscheidungen getrennt prüfen.', r'strafe|bewaehr|massregel|einzieh|vollstreck|vollzug|resozial|fuehrungsaufsicht'),
  ('Geschädigte und besondere Rollen: Opferrechte, Nebenklage, Adhäsion, Jugend, Unternehmen und Zeugenbeistand nach der tatsächlichen Rolle bearbeiten.', r'opfer|nebenklage|adhaesion|jugend|heranwachsend|unternehm|beistand|verletzte'),
 ],
 'regulierung': [
  ('Energie und Netze: Netzanschluss, Entgelte, Unbundling, Versorgung, Marktkommunikation und Aufsicht im konkreten Energiesektor prüfen.', r'energie|netzanschluss|netzentgelt|strom|gas|remit|messstelle|unbundling|ladesaeule|bilanzkreis'),
  ('Telekommunikation und Frequenzen: Marktzugang, Zugangspflichten, Entgelte, Nummern, Frequenzen und Endnutzerrechte bearbeiten.', r'^tk-|telekommun|frequenz|nummer|roaming|breitband|glasfaser'),
  ('Post und weitere Netzwirtschaft: Postmarkt, Universaldienst, Eisenbahn und andere regulierte Infrastruktur nach dem einschlägigen Regime prüfen.', r'post|paket|brief|universal|eisenbahn|schiene'),
  ('Digitale Dienste und Systeme: Plattformen, DSA, digitale Dienste, KI und Schnittstellen zur sektoralen Regulierung abgrenzen.', r'digital|dsa|dma|plattform|ki-|algorithm'),
  ('Regulierungsverfahren und Rechtsschutz: Antrag, Datenauskunft, Anhörung, Beschluss, Vollzug und gerichtlichen Rechtsschutz anhand der Regulierungsakte führen.', r'verfahren|antrag|beschluss|beschwerde|gericht|behoerd|anhoer|auskunft|frist|rechtsschutz'),
 ],
 'haushalt': [
  ('Haushaltsplanung und Ermächtigung: Ansatz, Titel, Zweckbindung, Deckung, Verpflichtungsermächtigung und Haushaltsgesetz vor der Entscheidung prüfen.', r'haushaltsplan|titel|ansatz|deck|verpflichtung|haushaltsgesetz|reste|globaler-minderausgabe|sperr|ueberplan|ausserplan'),
  ('Zuwendung und Förderung: Antrag, Zuwendungsbescheid, Nebenbestimmung, Mittelabruf, Verwendungsnachweis und Rückforderung an den Förderzweck binden.', r'zuwendung|foerder|verwendungsnachweis|institutionell|projektmittel|bewilligung|rueckford'),
  ('Beschaffung und Wirtschaftlichkeit: Bedarf, Wirtschaftlichkeitsuntersuchung, Vergabe, Vertrag und Leistungsabnahme auf haushaltsrechtliche Voraussetzungen prüfen.', r'wirtschaftlich|beschaff|vergabe|vertrag|leistung|bedarf|beschaff|wu-|kosten-nutzen'),
  ('Vermögen und Finanzierung: Grundstück, Beteiligung, Darlehen, Bürgschaft, Sondervermögen und Sicherheitsleistung bewerten und dokumentieren.', r'vermoegen|grundstueck|beteiligung|darlehen|buergschaft|finanzier|sicherheit|sondervermoegen'),
  ('Bund Länder und Europa: Zuständigkeiten, Finanzausgleich, kommunale Transfers, Landesrecht und EU-Mittel regimegerecht abgrenzen.', r'landeshaushalt|bund-laender|kommunal|eu-|finanzausgleich|landesrecht'),
  ('Sozial- und Fachhaushalte: Sozialversicherung, Bundeswehr und besondere Leistungsbereiche mit den jeweiligen gesetzlichen Bindungen prüfen.', r'sozial|buergergeld|krankenversicherung|bundeswehr|rente|gesundheit'),
  ('Vollzug und Kontrolle: Buchung, Zahlung, Beleg, Rechnungslegung, Prüfung, Bericht und Verantwortlichkeit bis zum belegten Abschluss führen.', r'vollzug|buchung|zahlung|beleg|rechnung|pruefung|kontroll|bericht|kasse|innenrevision'),
 ],
 'luftrecht': [
  ('Unternehmen und Luftfahrzeug: Betriebsgenehmigung, Eigentum, Register, Leasing, Zulassung und Finanzierung von Airline oder Luftfahrzeug prüfen.', r'airline|luftfahrzeug|leasing|register|eigentum|finanz|genehmigung|zulassung|kauf|flotte|insolvenz|sicherheit|pfand'),
  ('Flughafen und Bodenbetrieb: Flughafenrecht, Slots, Bodenabfertigung, Infrastruktur, Entgelte und Zugang am konkreten Standort bearbeiten.', r'flughafen|bodenabfertig|slot|airport|infrastruktur|entgelt|bodenverkehr|planung|laerm'),
  ('Flugbetrieb und Personal: Betrieb, Besatzung, Lizenz, Arbeitszeit, Wartung und technische Lufttüchtigkeit nach dem richtigen Regime prüfen.', r'flugbetrieb|besatzung|lizenz|personal|pilot|wartung|lufttuechtig|crew|easa|part-|maintenance|ersatzteil|flugdienst'),
  ('Sicherheit und besondere Einsätze: Luftsicherheit, Zuverlässigkeit, Gefahrgut, Drohnen, Hubschrauber und besondere Flüge getrennt bearbeiten.', r'luftsicherheit|zuverlaessig|acc3|gefahrgut|drohn|uas|hubschrauber|heli|rettung|sonderflug|security'),
  ('Beförderung und Haftung: Passagier, Gepäck, Fracht, Reise, Unfall und Versicherung mit Leistungs- und Schadensbelegen prüfen.', r'passagier|flugga|gepaeck|fracht|befoerder|reise|unfall|schaden|versicherung|haftung|montreal|verspaet|annull'),
  ('Umwelt und internationale Regeln: Emissionen, Klimaregeln, Verkehrsrechte, internationales Abkommen und grenzüberschreitende Aufsicht abgleichen.', r'emission|klima|corsia|ets|international|abkommen|verkehrsrecht|bilateral|europa'),
  ('Verfahren und Rechtsschutz: Behörde, Antrag, Nachforderung, Sanktion, Zuständigkeit und Rechtsbehelf bis zum konkreten Schreiben bearbeiten.', r'behoerd|antrag|verfahren|nachforder|sanktion|zustaendig|gericht|rechtsschutz|frist'),
 ],
 'robotik-recht': [
  ('Produkt und Rollen: Roboter, Maschine, Komponente, Betreiber, Hersteller, Einführer und Änderung anhand des konkreten Produkts einordnen.', r'rolle|hersteller|betreiber|einfuehr|haendler|komponente|maschine-oder|wesentliche-aender|systemgrenze|produktklasse'),
  ('Konformität und Sicherheit: Risikobeurteilung, Normen, technische Dokumentation, Prüfung, CE und Erklärung bis zum belastbaren Produktdossier bearbeiten.', r'konform|ce-|risikobeurteil|norm|sicherheit|pruefung|technisch|anleitung|dokumentation|kennzeich|maschinenrecht|maschinenverord'),
  ('KI und Daten: KI-Verordnung, Systemzweck, Daten, Biometrie, Überwachung, Datenschutz und menschliche Aufsicht getrennt prüfen.', r'ki-|daten|biometr|emotion|kamera|ueberwach|algorithm|modell|autonom|training|edge|cyber'),
  ('Vertrag und Rechte: Beschaffung, Leistung, Software, Lizenz, Open Source, IP und Updatepflichten bis zum Vertragstext gestalten.', r'vertrag|beschaff|leistung|software|lizenz|open-source|ip-|update|wartung|service|liefer'),
  ('Einsatz und Arbeitsorganisation: Montage, Integration, Kollaboration, Arbeitsschutz, Qualifikation und Verantwortlichkeit im Betrieb konkretisieren.', r'einsatz|montage|integrat|kollabor|cobot|arbeit|qualifik|smart-factory|produktion|betrieb|logistik|mobile'),
  ('Vorfall Haftung und Marktaufsicht: Fehler, Unfall, Schaden, Versicherung, Rückruf, Marktaufsicht und behördlichen Vollzug belegt bearbeiten.', r'fehler|unfall|schaden|versicherung|rueckruf|marktaufsicht|haftung|regress|vorfall|sanktion'),
  ('Spezialmarkt und Außenwirtschaft: Medizin, Verkehr, Raumfahrt, Dual Use, Export und besondere Anwendung nach dem einschlägigen Regime bearbeiten.', r'medizin|verkehr|raumfahrt|dual-use|export|drohn|militaer|pflege|agrar'),
 ],
 'agb-recht-pruefer': [
  ('Vertrag Einbeziehung und Auslegung: AGB-Eigenschaft, Einbeziehung, Individualabrede, Überraschung und maßgeblichen Inhalt bestimmen.', r'einbezieh|individual|ueberrasch|auslegung|geltung|vertragsschluss|305|mehrdeutig|abwehrklausel'),
  ('Leistung und Preis: Leistungsbeschreibung, Änderungsvorbehalt, Preis, Abrechnung, Laufzeit und Kündigung mit Transparenz und Vertragszweck abgleichen.', r'preis|leistung|laufzeit|kuendigung|aenderung|change|abrechnung|entgelt|renewal|abonnement|lieferzeit|verlaenger'),
  ('Haftung Gewährleistung und Sicherheiten: Haftungsausschluss, Mängelrechte, Verjährung, Garantie, Vertragsstrafe und Sicherheiten prüfen.', r'haftung|gewaehr|mangel|maengel|verjaehr|garant|strafe|sicherheit|freistell|indemnit|warranty|limitation'),
  ('Digitale Dienste und Daten: Software, Plattform, Cloud, Datenschutz, KI, Lizenzen und digitale Vertragsmodelle konkret bearbeiten.', r'digital|software|saas|cloud|plattform|daten|ki-|crypto|token|online|app-|ecommerce|lizenz|content|internet'),
  ('Verbraucher und Durchsetzung: Verbrauchervertrag, Information, Widerruf, Unterlassung, Verbandsklage und Massenverfahren trennen.', r'verbrauch|widerruf|information|unterlass|verband|massen|kollektiv|uklag|vdug|button'),
  ('Branchen und Vertragsparteien: Besondere Geschäftsmodelle, B2B, Arbeitsvertrag, Bau, Transport, Finanzprodukte und Gesellschaftsvertrag branchengerecht prüfen.', r'branche|b2b|arbeit|bau|transport|logistik|spedition|bank|finanz|gesellschaft|versicherung|miet|kauf|franchise|leasing|energie|gesundheit|telekom'),
  ('Redaktion und Streit: Unwirksame Regelung, Rechtsfolge, Ersatztext, Verhandlung, Prozessvortrag und Freigabe zusammenführen.', r'redaktion|unwirksam|rechtsfolge|ersatz|verhand|prozess|klage|gericht|freigabe'),
 ],
}

# Gleiche Arbeitsphasen, jeweils mit den Rollen aus dem eigenen Fachprofil.
TOPICS['strafjustiz'] = TOPICS['straf']

def add(key, rows):
    TOPICS[key] = []
    for row in rows.strip().splitlines():
        label, rest = row.split('|', 1)
        pattern, task = rest.rsplit('|', 1)
        TOPICS[key].append((f'{label}: {task}', pattern))

add('festlandchina-wirtschaftsverkehr', '''
Geschäftsmodell und Standort|entry|investor|wfoe|joint-venture|fabrik|factory|operations|strategy|strategie|de-risk|decoupl|china-plus|depend|single-source|local-counsel|Investition, Standort, Betriebsmodell und örtliche Beratung anhand des konkreten China-Geschäfts bestimmen.
Lieferkette und Produkt|supply|supplier|sourcing|product|ce-|market-surveillance|machinery|electronics|semiconductor|medical-device|automotive|textile|toy|battery|solar|Lieferanten, technische Produkte, Einfuhr und Marktüberwachung aus den tatsächlichen Warenströmen prüfen.
Zoll Sanktionen und Export|customs|tariff|origin|trade-defence|dumping|countervailing|dual-use|bafa|ear-|sanction|restricted|coercion|awg|awv|fdi|screening|export|Exportkontrolle, Investitionsprüfung, Handelsmaßnahmen, Zoll und Sanktionen voneinander trennen.
Verträge und Schutzrechte|contract|incoterm|freight|forwarder|broker|trademark|patent|utility|trade-secret|nda|nnn|tooling|mold|technology-transfer|ip-|Vertrag, Sprache, Rechtswahl, Eigentum, Marke, Patent und Know-how vor der Umsetzung absichern.
Daten und digitale Systeme|data|cyber|personal-information|cloud|erp|wechat|software|source-code|saas|Datenlokalisierung, Übermittlung, Software und technische Systeme nach tatsächlichem Einsatz prüfen.
Integrität und Menschenrechte|bribery|gift|whistleblow|human-right|forced-labour|lksg|csddd|environment|workplace|union|government-relations|Korruption, Arbeitsbedingungen, Umwelt, Meldesystem und Lieferkettenprüfung belegt bearbeiten.
Zahlung und Finanzierung|capital-control|payment|cash|repatriation|financ|asset-protection|tax|Zahlungsweg, Finanzierung, Steuern, Kapitalverkehr und Rückführung mit Verträgen und Belegen abgleichen.
Störung und Rechtsverfolgung|evidence|arbitrat|award|litigation|enforcement|incident|dawn-raid|inspection|taiwan|geopolit|crisis|Beweise, Streitbeilegung, Durchsetzung, Kontrollen und Unterbrechungsszenarien konkret vorbereiten.
''')

add('kartell', '''
Markt und Marktmacht|markt|market|ssnip|elastiz|diversion|cluster|systemmaerkte|nachfrage|angebots|Sachlichen und räumlichen Markt, Substitution, Marktanteile und Marktmacht anhand belastbarer Tatsachen prüfen.
Kooperation und Kartellverbot|101|kartellverbot|horizontal|kooper|information|cartel|collusion|hub-and-spoke|nachhaltig|no-poach|Wettbewerberkontakte, Vereinbarungen, Informationsaustausch und Freistellung im konkreten Zusammenhang prüfen.
Vertrieb und vertikale Bindungen|vertikal|vertrieb|vber|haendler|franchise|handelsvertreter|agentur|paritaet|plattform|selektiv|exklusiv|geoblock|Preisbindung, Vertriebsgebiet, Plattformklauseln und vertikale Freistellung bis zur Vertragsfassung bearbeiten.
Missbrauch und Zugang|102|missbrauch|abuse|dependence|relative|19a|essential|facilit|margin|predat|rabatt|datenzugang|interoper|dma|Marktbeherrschung, relative Marktmacht, Zugang, Konditionen und Verdrängungswirkung getrennt prüfen.
Zusammenschlusskontrolle|fusion|merger|zusammenschluss|anmelde|joint-venture|minority|gun-jumping|remed|ministererlaub|Anmeldepflicht, Kontrolle, Vollzugsverbot und Abhilfemaßnahmen mit der Transaktionsstruktur abgleichen.
Behörden und Verteidigung|dawn-raid|behoerd|bka|dgcomp|ftc|doj|leniency|settlement|bussgeld|sanktion|Kontrolle, Kronzeuge, Anhörung, Bußgeld und Zusammenarbeit mit zuständigen Behörden vorbereiten.
Schadensersatz und Unternehmen|33a|33g|schaden|follow-on|litigation|disclosure|liability|haftung|compliance|board|schulung|Ansprüche, Offenlegung, Verjährung, Unternehmensorganisation und Organverantwortung belegt bearbeiten.
''')
add('normsetzung', '''
Regelungsziel und Kompetenz|regelungsziel|kompetenz|verfass|gesetzgebung|ermächtig|ermaechtig|grundrecht|Regelungsbedarf, Gesetzgebungskompetenz, Ermächtigung und grundrechtliche Grenzen bestimmen.
Normtext und Rechtsförmlichkeit|rechtsfoerm|normtext|aenderungs|verweisung|definition|begriffs|inkraft|uebergang|geltung|Formulierungen, Änderungsbefehle, Verweisungen, Übergangsrecht und Inkrafttreten konsistent entwerfen.
Folgen Kosten und Evaluation|folgen|kosten|erfuellungs|nkr|evalu|rmap|nachhaltig|buerokratie|digitalcheck|Wirkung, Aufwand, Vollzug, digitale Tauglichkeit und Evaluation aus nachvollziehbaren Annahmen ableiten.
Verfahren und Abstimmung|verfahren|anhoer|abstimm|referenten|ressort|kabinet|bundesrat|bundestag|notifiz|Gesetzgebungsverfahren, Beteiligung, Abstimmung und Notifizierung mit Zuständigkeit und Frist vorbereiten.
Wirtschaft Finanzen und Infrastruktur|bmf-|bmwe-|bmwsb-|bmv-|wirtschaft|finanz|bau|verkehr|energie|steuer|Fiskal-, Wirtschafts-, Bau- und Verkehrsvorhaben anhand ihrer fachlichen Systematik bearbeiten.
Soziales Gesundheit und Bildung|bmas-|bmg-|bmbfsfj-|bmftr-|sozial|gesund|bildung|forschung|Sozial-, Gesundheits-, Bildungs- und Forschungsrecht mit Vollzug und Schnittstellen ausgestalten.
Sicherheit Verwaltung und Europa|aa-|bmi-|bmvg-|bmjv-|bmds-|eu-|voelker|verwalt|sicherheit|datenschutz|Verwaltungs-, Sicherheits-, Justiz-, Digital- und Außenrecht sowie europäische Vorgaben regimestimmig umsetzen.
Umwelt Ernährung und Ressourcen|bmukn-|bmleh|umwelt|klima|natur|wasser|abfall|agrar|tier|lebensmittel|Umwelt-, Agrar-, Lebensmittel- und Ressourcenrecht mit den einschlägigen Genehmigungs- und Kontrollsystemen entwerfen.
''')
add('datenbank', '''
Schutzgegenstand und Berechtigte|schutzgegenstand|berechtigt|hersteller|urheber|investition|datenbankwerk|sammlung|origin|Datenbankwerk, Datenbankherstellerrecht, Investition und Rechtsinhaber anhand der tatsächlichen Datenorganisation unterscheiden.
Entnahme Nutzung und Scraping|entnahme|weiterverwend|scrap|crawl|api|mining|tdm|abruf|zugang|Entnahme, Weiterverwendung, automatisierten Zugriff und Schranken mit Umfang und Zweck prüfen.
Lizenz und Datenvertrag|lizenz|vertrag|nutzungsrecht|verg[u]?et|sla|agb|pool|datenliefer|open-data|Datenlizenz, Nutzungsgrenzen, Zugangsbedingungen und Entgelt im konkreten Vertragsmodell gestalten.
Datenschutz und Regulierung|datenschutz|dsgvo|data-act|dga|gesundheits|personen|ki-|dma|dsa|Kartellrecht, Datenschutz, Datenregulierung und KI-Nutzung jeweils gesondert prüfen.
Verletzung und Durchsetzung|verletz|unterlass|schaden|abmahn|beweis|verjaehr|prozess|gericht|anspruch|Rechtsverletzung, Beweise, Unterlassung, Schadensersatz und prozessuale Durchsetzung ausarbeiten.
''')
add('vertragsgestaltung', '''
Abschluss Parteien und Auslegung|abschluss|partei|vertret|vollmacht|angebot|annahme|ausleg|form|rechtswahl|gerichtsstand|Vertragspartner, Abschluss, Vollmacht, Form und maßgeblichen Inhalt anhand des Fassungsverlaufs prüfen.
Leistung Vergütung und Abwicklung|leistung|verguet|preis|zahlung|abrechnung|liefer|abnahme|sla|service|leasing|franchise|Leistung, Gegenleistung, Abnahme, laufende Pflichten und Abrechnung konkret ausformulieren.
Geheimnis Daten und Rechte|geheim|verschwiegen|nda|vertraulich|daten|datenschutz|ip-|lizenz|know-how|open-source|Geheimnisse, Daten, Nutzungsrechte und Weitergabe im tatsächlichen Geschäftsvorgang absichern.
Haftung Sicherheiten und Störung|haftung|gew[a]?ehr|maengel|mangel|strafe|schaden|sicherheit|garantie|stoerung|force|risik|Haftung, Mängel, Sicherheit, Leistungsstörung und wirtschaftliche Risikozuordnung gestalten.
Laufzeit Beendigung und Streit|laufzeit|kuendig|beendig|exit|rueckgabe|ruecktritt|streit|verjaehr|prozess|vergleich|Laufzeit, Kündigung, Abwicklung, Rückgabe und Streitbeilegung mit den übrigen Klauseln abstimmen.
''')
add('bildung', '''
Zugang Zulassung und Status|zugang|zulass|aufnahme|kapazitaet|nc-|einschul|schulplatz|immatrik|status|Zulassung, Aufnahme, Kapazität, Zuordnung und Status im jeweiligen Landesrecht prüfen.
Lehre Alltag und Förderung|lehre|unterricht|foerder|inklusion|nachteilsausgleich|betreuung|ganztag|schulpflicht|fehlzeit|Unterricht, Lehre, Teilnahme, Förderung und Ausgleich nach tatsächlichem Bildungsweg bearbeiten.
Prüfung Bewertung und Abschluss|pruef|bewert|note|versetzung|abschluss|taeusch|plagiat|Prüfungsverfahren, Bewertungsfehler, Täuschung, Wiederholung und Abschluss belegt prüfen.
Personal Forschung und Organisation|personal|profess|berufung|forsch|drittmittel|promotion|habilit|gremi|organisation|Personalstatus, Wissenschaft, Forschung, Organisation und Beteiligungsrechte getrennt bearbeiten.
Konflikt Maßnahme und Rechtsschutz|konflikt|ordnungs|sanktion|ausschluss|widerspruch|klage|gericht|eil|rechtsschutz|Schulische oder hochschulische Maßnahmen, Beschwerde und gerichtlichen Rechtsschutz mit Fristen führen.
''')
add('bank', '''
Konto Zahlungsverkehr und Betrug|konto|zahlung|ueberweis|lastschrift|karte|phishing|betrug|psd|Konto, Zahlungsauftrag, Authentifizierung, Autorisierung und Erstattung anhand der Belege prüfen.
Kredit und Sicherheiten|kredit|darlehen|sicherheit|buergschaft|grundschuld|covenant|sanierung|Kreditvertrag, Auszahlung, Kündigung, Sicherheit und Verwertung getrennt bearbeiten.
Anlage und Kapitalmarkt|anlage|wertpapier|kapitalmarkt|prospekt|mifid|fonds|beratung|emission|Kundenberatung, Anlagevermittlung, Produktinformation und kapitalmarktrechtliche Pflichten im Geschäft prüfen.
Aufsicht Compliance und Organisation|aufsicht|bafin|kwg|wpig|compliance|geldwaesch|dora|outsourc|risiko|organisation|Bankaufsicht, Geschäftsorganisation, Auslagerung und Präventionspflichten auf den konkreten Vorgang anwenden.
Vertrag Haftung und Rechtsschutz|vertrag|agb|haftung|schaden|prozess|klage|vollstreck|Vertragsklausel, Haftungsanspruch, Rechtsbehelf und Durchsetzung bis zum nutzbaren Text bearbeiten.
''')
add('bgb', '''
Rechtsgeschäft und Wirksamkeit|rechtsgeschaeft|willenserklaer|geschaeftsfaeh|anfecht|irrtum|arglist|nichtig|form|vertret|vollmacht|bgb-at|Erklärung, Geschäftsfähigkeit, Vertretung, Form, Irrtum und Wirksamkeit anhand des Geschehens prüfen.
Vertrag und Leistungsstörung|vertrag|kauf|werk|dienst|leistung|pflicht|verzug|unmoeglich|ruecktritt|maengel|mangel|schaden|Vertragliche Ansprüche, Gegenleistung, Leistungsstörung, Mängel und Schadensersatz strukturiert bearbeiten.
Bereicherung und Rückabwicklung|bereicher|kondikt|812|816|818|leistungskond|eingriff|rueckabwick|Entreicherung, Leistungsbeziehung, Eingriff und Rückabwicklung nach dem richtigen Anspruch prüfen.
Delikt und gesetzliche Ansprüche|delikt|823|826|geschaeftsfuehrung|goa|verkehrssicher|produkthaft|gesetzlich|Delikt, Geschäftsführung ohne Auftrag und weitere gesetzliche Ansprüche mit Zurechnung und Schaden prüfen.
Sachen Sicherung und Forderungswechsel|sachen|eigentum|besitz|sicherheit|abtret|aufrechnung|schuldueber|pfand|Eigentum, Besitz, Sicherung, Abtretung, Aufrechnung und Schuldwechsel anhand der Rechtsbeziehungen klären.
Einwendungen Fristen und Durchsetzung|einwend|einrede|verjaehr|frist|beweis|durchsetz|klage|prozess|Einwendungen, Einreden, Fristen, Beweislast und Durchsetzung bis zum konkreten Arbeitsprodukt verbinden.
''')
add('migrations', '''
Einreise Aufenthalt und Erwerbstätigkeit|einreise|visum|aufenthalt|erwerb|fachkraeft|blue-card|arbeits|selbststaend|Zweck, Titel, Nebenbestimmung und Erwerbstätigkeit anhand der Aufenthaltsbiografie prüfen.
Familie Studium und Integration|famil|nachzug|studium|ausbildung|integration|sprache|Familiennachzug, Bildungsweg und Integrationsanforderungen mit den tatsächlichen Bindungen abgleichen.
Asyl und Schutz|asyl|schutz|fluecht|dublin|bamf|herkunft|Asyl, internationalen Schutz, Zuständigkeit und Herkunftsinformationen einzelfallbezogen bearbeiten.
Ausreise und Aufenthaltsbeendigung|ausreis|abschieb|ausweis|duldung|rueckkehr|einreiseverbot|Ausreisepflicht, Beendigung, Duldung, Hindernisse und Vollzug getrennt prüfen.
Staatsangehörigkeit und Rechtsschutz|staatsangehoer|einbuerger|rechtsschutz|klage|widerspruch|eil|frist|Staatsangehörigkeit, Einbürgerung und den jeweils passenden Rechtsbehelf mit Frist und Nachweisen bearbeiten.
''')
TOPICS['migration']=TOPICS.pop('migrations')
add('sozial', '''
Leistung und Anspruch|leistungs|anspruch|antrag|buergergeld|grundsicherung|sozialhilfe|sgb-ii|sgb-xii|Persönliche Voraussetzungen, Leistungstatbestand, Bedarf, Einkommen und Vermögen belegt prüfen.
Versicherung und Beiträge|versicherung|beitra|status|mitglied|freiwillig|pflicht|Versicherungsstatus, Mitgliedschaft, Beitrag und Zuständigkeit nach den Versicherungszweigen trennen.
Krankheit Pflege und Rehabilitation|krank|pflege|reha|hilfsmittel|behandlung|gesund|teillhabe|teilhabe|Versorgung, Pflege, Rehabilitation und Teilhabe mit medizinischen Unterlagen und Leistungsrecht abgleichen.
Rente Unfall und Erwerbsfähigkeit|rente|unfall|erwerbs|arbeitsunfall|berufskrank|schwerbehind|Rente, Unfallfolge, Erwerbsfähigkeit und Behinderung mit Versicherungsverlauf und Gutachten prüfen.
Bescheid Widerspruch und Gericht|bescheid|widerspruch|klage|gericht|eil|frist|ueberpruef|anhoer|Bescheid, Bekanntgabe, Anhörung, Rechtsbehelf und Eilrechtsschutz bis zum Schriftsatz bearbeiten.
''')
add('dienst', '''
Status und Dienstpflicht|status|dienstpflicht|wehrpflicht|wehrdienst|grundwehr|freiwillig|soldat|muster|Tatsächlichen Status, Einberufung, Dienstpflicht und Entscheidungszuständigkeit bestimmen.
Gewissen und Verweigerung|gewissen|verweiger|kdv|bafza|anerkenn|Gewissensentscheidung, Antrag, Begründung und Anerkennungsverfahren individuell bearbeiten.
Gesundheit Eignung und Zurückstellung|gesund|eignung|tauglich|muster|zurueckstell|haerte|medizin|Gesundheit, Eignung, Härte, Zurückstellung und Begutachtung anhand der Nachweise prüfen.
Verfahren Fristen und Rechtsbehelf|verfahren|frist|bescheid|widerspruch|klage|eil|rechtsschutz|Einberufung, Bescheid, Widerspruch und gerichtlichen Rechtsschutz mit Vollzugsrisiko führen.
Dienstalltag und Folgen|besold|versorgung|disziplin|arbeitsplatz|kuendig|sanktion|urlaub|Dienstliche Folgen, Arbeitsplatzschutz, Versorgung und Sanktionen gesondert ausarbeiten.
''')
add('kanzlei-mandant-lifecycle', '''
Mandat und Vereinbarung|mandatsannahme|konflikt|conflict|identity|vollmacht|onboard|intake|engagement|scope|outside-counsel|rfp|panel|beauty|Mandatsumfang, Konflikt, Identität, Vollmacht und Vereinbarung zuverlässig klären.
Akte Fristen und Zusammenarbeit|akte|frist|deadline|court-file|document|team|aufgabe|deleg|staffing|workbench|workplace|workspace|access-control|authority-matrix|dashboard|taxonomy|Arbeitsstand, Dokumente, Fristen und Verantwortliche im laufenden Mandat fortführen.
Beratung Kommunikation und Entscheidung|beratung|kommunikation|brief|email|decision|bericht|meet|gespraech|language|stakeholder|client-facing|expectation|business-review|report|summary|bad-news|expert|second-opinion|press|feedback|Mandanten verständlich informieren, offene Entscheidungen begründen und Antworten einarbeiten.
Vergütung Rechnung und Fremdgeld|verguet|honorar|rechnung|rvg|fremdgeld|kosten|zahlung|billing|budget|spend|fee|invoice|rate-card|time-entry|value-writing|vat|Abrechnung, Zahlung, Fremdgeld und Kosteninformation mit der Beauftragung abstimmen.
Rechtsdurchsetzung Risiko und Governance|appeal|enforcement|injunction|litigation|legal-hold|evidence|settlement|risk|investigation|regulatory|governance|insurance|ethics|privilege|datenschutz|redaction|Verfahrensschritte, Entscheidungen, Nachweise, Vertraulichkeit und Verantwortung auf Mandanten- und Kanzleiseite verbinden.
Abschluss Archiv und Weiterbetreuung|abschluss|archiv|retention|rueckgabe|closeout|handover|termination|post-mortem|lessons|renewal|satisfaction|knowledge|Mandatsabschluss, offene Schritte, Rückgabe, Aufbewahrung und Weiterbetreuung dokumentieren.
''')
add('nis2-cybersecurity-compliance', '''
Geltungsbereich und Pflichten|nis2|sektor|groessen|einrichtung|kritis|dora|cra-|public-sector|certification|Betroffenheit, Sektor, Größe, Rollen und konkurrierende Regulierungsregime anhand des Unternehmens bestimmen.
Governance und Risikoplan|governance|isms|leitung|vorstand|ciso|management|budget|massnahmen|maturity|risk-register|kpi|iso27001|nist|cis-controls|grundschutz|Risikomanagement, Leitungspflichten, Maßnahmenplan und Nachweise in den tatsächlichen Betrieb einordnen.
Identität Geräte und Netz|identity|access|mfa|passkey|admin|joiner|mover|offboard|device|mobile|mdm|iot|ot-|netz|wifi|vpn|usb|physische|Zugriffsrechte, Geräte, Netze, Fernzugang und physische Sicherheit konkret prüfen und Maßnahmen begründen.
Software Schwachstellen und Kryptografie|software|sbom|patch|vulnerability|open-source|devops|develop|code-signing|java|tls|pki|zertifikat|verschluessel|configuration|Softwareentwicklung, Schwachstellen, Patchprozess, Komponenten und kryptografische Nachweise auswerten.
Lieferkette Cloud und Beschaffung|liefer|supplier|third-party|cloud|saas|procurement|provider|souveraen|Provider, Wartung, Lieferkette, Cloud und Beschaffung mit überprüfbaren Vertragspflichten absichern.
Daten Beschäftigte und KI|daten|data-|arbeitnehmer|beschaeftigte|betriebsrat|dsgvo|datenschutz|ki-|chatgpt|copilot|byod|messenger|geheim|airtag|tracking|telematik|Sicherheitsmaßnahmen mit Datenschutz, Mitbestimmung, Geschäftsgeheimnissen und KI-Einsatz abstimmen.
Vorfall und Krisenreaktion|incident|vorfall|krisen|ransom|fraud|phish|deepfake|forens|logging|siem|soc|edr|xdr|backup|notfall|tabletop|pen-test|Angriff, Schaden, Sicherung, Wiederherstellung und Kommunikation anhand des festgestellten Vorfalls steuern.
Meldung Aufsicht und Versicherung|meldung|melde|registrierung|aufsicht|bussgeld|remediation|versicherung|Meldewege, Fristen, Registrierung, behördliche Reaktion und Versicherung mit dem Vorfallsstand abgleichen.
''')
add('softwarerecht-de-eu-us', '''
Projekt Leistung und Abnahme|projekt|implementation|customiz|agil|scrum|change-request|abnahme|acceptance|beta|pilot|poc|werkvertrag|dienstvertrag|Leistungsumfang, Projektmodell, Änderung, Implementierung und Abnahme im Softwareprojekt vereinbaren.
Urheberrecht und Rechtekette|copyright|urheber|69a|programs-directive|chain-of-title|ownership|work-made|assignment|freelancer|employee|employment|miturheber|Rechte an Code, Dokumentation und Beiträgen nach Entstehung, Beschäftigung und Rechtsordnung nachweisen.
Lizenzen Open Source und Daten|license|lizenz|open-source|gpl|agpl|mit-apache|bsd|copyleft|contributor|sdk|data-license|model-weights|metr|per-seat|Nutzungsumfang, Lizenzkette, Open Source, Daten und Lizenzmetriken auf die konkrete Verwendung anwenden.
Betrieb SaaS und Ausstieg|saas|cloud|on-prem|support|maintenance|sla|reseller|oem|marketplace|termination|exit|migration|escrow|repository|Betrieb, Support, Cloudwechsel, Unterauftrag, Datenrückgabe und Ausstieg vertraglich absichern.
Regulierung Sicherheit und KI|ai-|ki-|data-act|data-protection|gdpr|privacy|dpa|nis2|cyber|machine|dsa|dma|secure|vulnerability|sbom|Daten-, KI-, Produkt- und Cybersicherheitsregeln von der Vertragsprüfung unterscheiden und Pflichten konkretisieren.
Schutzrechte Streit und Haftung|patent|trade-secret|infringement|misappropriation|enforcement|injunction|liability|indemnity|warranty|defect|beweis|Schutzrechtsverletzung, Geheimnisschutz, Haftung, Gewährleistung und Beweisführung bis zum Rechtsprodukt bearbeiten.
Ausland Finanzierung und Beschaffung|us-|uk-|swiss|india|nearshore|offshore|export|sanction|investment|mna|foerder|procurement|Grenzüberschreitende Entwicklung, Finanzierung, Transaktion und Beschaffung auf ihre tatsächliche Rechtsordnung beziehen.
''')
add('franchiserecht-praxis', '''
System und vorvertragliche Aufklärung|kaltstart|vorvertrag|disclosure|pilotbetrieb|proof|systemakte|Systemkonzept, Rollen, Pilotbetrieb und vorvertragliche Angaben vor Vertragsabschluss prüfen.
Vertrag Gebühren und Gebiet|franchisevertrag|verguet|gebuehr|marketing-fee|gebietsschutz|territorial|mindestumsatz|vertragsstruktur|Vertrag, Gebühren, Mindestleistung, Gebiet und wirtschaftliche Pflichten konkret abstimmen.
Marke Handbuch und Vertrieb|marke|marken|handbuch|know-how|geheim|ci-|onlinevertrieb|social-media|influencer|werbung|bewertungen|Markennutzung, Handbuch, Know-how, Werbung und Vertrieb im System rechtlich gestalten.
Kartellrecht und Lieferbindung|kartell|bezugsbind|preisempfehl|preisbind|vertikal|lieferbind|einkaufsmacht|informationsaustausch|Bezugsbindung, Preise, Informationsaustausch und Wettbewerbsverbote getrennt prüfen.
Standort Betrieb und Fachregulierung|standort|ladenbau|bau-|arbeitsrecht|datenschutz|crm|it-system|kassendaten|qualitaetsaudit|mystery|lieferketten|lebensmittel|fitness|bildung|pflege|medizin|hotel|tankstelle|kfz|ghost|Standort, Personal, Daten, Audit und branchenspezifische Pflichten anhand des Betriebs bearbeiten.
Expansion und Transaktion|master|multi-unit|area-developer|international|usa-|m-a|Expansion, Master-Franchise, Gebietsentwicklung und Transaktion mit dem Systemvertrag abgleichen.
Beendigung Insolvenz und Streit|kuendig|exit|entbranding|nachvertrag|abwicklung|rueckbau|ausgleich|insolvenz|streit|schaden|verfueg|Beendigung, Fortführung, Rückbau, Ausgleich und Rechtsschutz bis zur konkreten Lösung bearbeiten.
''')
add('leasingrecht-praxis', '''
Leasingmodell und Vertragsparteien|finanzierungsleasing|operating|mietkauf|sale-back|sale-and|dreieck|leasingakte|Modell, Objekt, Beteiligte und wirtschaftliche Zuordnung anhand der Verträge bestimmen.
Vertrag Rate und Restwert|vertrag|redline|rate|restwert|andien|mehrerloes|agb|term-sheet|covenant|Leasingvertrag, Rate, Restwert, Klauseln und Rückkaufmechanik aufeinander abstimmen.
Objekt Abnahme und Mängel|objekt|abnahme|maengel|mangel|lieferant|equipment|maschine|cnc|wartung|medizintechnik|it-hardware|mobile-work|Objektübergabe, Mängel, Lieferantenrechte, Wartung und technische Nachweise prüfen.
Fahrzeug Immobilie und Spezialobjekt|fahrzeug|flotte|flugzeug|schiff|immobil|energieanlage|pv-|batterie|waermepump|Fahrzeug-, Immobilien-, Luftfahrzeug-, Schiffs- und Anlagenleasing mit Register- und Fachrecht abgleichen.
Steuer Bilanz und Daten|steuer|umsatzsteuer|bilanz|ifrs|hgb|datenschutz|telematik|tracking|esg|Bilanzielle, steuerliche, datenrechtliche und Nachhaltigkeitsfragen getrennt einordnen.
Störung Kündigung und Verwertung|stoer|kuendig|verwert|diebstahl|totalschaden|versicherung|untergang|rueckgabe|minderwert|Störung, Schaden, Kündigung, Rückgabe, Gutachten und Verwertung anhand der Objektakte bearbeiten.
Finanzierung Insolvenz und Durchsetzung|refinanz|abtret|servicing|npl|portfolio|insolvenz|sanier|restruktur|stund|inkasso|gericht|schieds|rechtsschutz|Leasingforderung, Refinanzierung, Krise und Durchsetzung mit Eigentum und Vertragsstand verbinden.
''')
add('wirtschaftsverwaltung', '''
Organisationsform und Verantwortung|organisationsform|unternehmen|oepp-struktur|public-corporate|rekommunal|scheinprivatis|daseinsvorsorge|Zulässigkeit wirtschaftlicher Betätigung, Organisationsform, Steuerung und Verantwortung prüfen.
Beschaffung Konzession und Vertrag|vergabe|konzession|inhouse|vertrag|betreiberpflicht|Auftrag, Konzession, Inhouse-Struktur, Betreiberpflicht und Vertrag regimestimmig gestalten.
Finanzierung Haushalt und Beihilfe|finanz|haushalt|beihilfe|buergschaft|patronat|gebuehr|Finanzierung, Freigabe, Beihilfe, Bürgschaft und Gebühren mit Zuständigkeit und Nachweisen abgleichen.
Wirtschaftlichkeit und Risiko|wirtschaftlichkeit|risiko|red-flags|Wirtschaftlichkeitsvergleich, Risikoallokation und Projektszenarien nachvollziehbar bewerten.
Kontrolle Kommunikation und Abwicklung|kontroll|kommunikation|transparenz|exit|rueckabwicklung|Kontrollrechte, Information, Umsetzung und Rückabwicklung bis zur konkreten Entscheidung ausarbeiten.
''')
add('kommunal', '''
Landesrecht und Zuständigkeit|landesrecht|kommunalrecht-|zustaendigkeit|organ-|gemeinde-stadt|Maßgebliches Landesrecht, Kommunalorgan, Kompetenz und Rechtsverhältnis bestimmen.
Beschluss Sitzung und Beteiligung|beschluss|sitzung|tagesordnung|befangen|beteilig|buergerbegehren|buergerentscheid|einwohnerantrag|information|Beschluss, Sitzung, Befangenheit, Informationsrecht und Bürgerbeteiligung verfahrensrichtig bearbeiten.
Satzung und öffentliche Einrichtung|satzung|benutzungsordnung|oeffentliche-einrichtung|feuerwehr|schultraeger|Einrichtung, Satzung, Benutzung und fachliche Aufgaben mit Landes- und Kommunalrecht abgleichen.
Abgaben Haushalt und Unternehmen|abgabe|gebuehr|haushalt|finanz|unternehmen|interkommunal|Gebühr, Abgabe, Haushalt, Unternehmen und interkommunale Zusammenarbeit nachvollziehbar prüfen.
Aufsicht und Rechtsschutz|aufsicht|eilantrag|eilrecht|kommunalstreit|beschwerde|Aufsicht, Kommunalstreit und Eilrechtsschutz mit Zuständigkeit, Antrag und Belegen vorbereiten.
''')
add('stvo', '''
Anordnung und Beschilderung|verkehrsrechtliche-anordnung|verkehrszeichen|tempo|zeichen|anordnung|Anordnung, Zeichen, Bekanntgabe und Voraussetzungen anhand der örtlichen Verkehrssituation prüfen.
Halten Parken und Lieferverkehr|haltverbot|bewohnerparken|parken|ladezone|lieferzone|Haltverbot, Bewohnerparken, Ladezone und Lieferverkehr mit Interessen und örtlichen Belegen bearbeiten.
Rad Bus und Schulweg|fahrrad|radverkehr|busspur|schulstrasse|schulweg|gefahrenstelle|Radverkehr, Busspur, Schulstraße und Verkehrsberuhigung mit dem konkreten Schutz- und Verkehrsziel prüfen.
Erlaubnis Sonderrecht und Fahreignung|ausnahme|schwertransport|sonderrecht|blaulicht|e-scooter|fahrerlaubnis|fahreignung|mpu|fahrtenbuch|Ausnahme, besondere Nutzung, Fahrerlaubnis, Fahreignung und Fahrtenbuch getrennt bearbeiten.
Behörde Beweis und Rechtsschutz|behoerde|beweis|karte|antrag|rechtsschutz|bussgeld|widerspruch|Risiko, örtliche Belege, Behördenkorrespondenz und passenden Rechtsbehelf bis zum Text ausarbeiten.
''')

add('bundesnetzagentur-verfahren', '''
Netzanschluss Ausbau und Entflechtung|netzanschluss|netzanbind|offshore|nabeg|bbplg|leitungsvorhaben|wasserstoff|unbundling|entflecht|Netzanschluss, Netzausbau, Planfeststellung, Entflechtung und Zugang am konkreten Energienetz prüfen.
Energieentgelte und Anreizregulierung|netzentgelt|anreizregulierung|erloesobergrenze|Entgelt, Erlösobergrenze, Kostenbasis und Anreizregulierung anhand der Regulierungsakte bearbeiten.
Energiemarkt und Versorgung|bilanzkreis|kapazitaetsvergabe|redispatch|regelenergie|remit|grosshandels|versorgung|lieferanten|messstellen|smart-meter|kwkg|ladesaeule|fernwaerme|Bilanzierung, Marktmissbrauch, Versorgung, Messung und weitere Energiemarktpflichten regimestimmig prüfen.
Telekommunikationsmarkt und Infrastruktur|tkg|marktregulierung|zugangsregulierung|entgeltgenehmigung|glasfaser|wegerecht|mitverlegung|gebaeudenetz|universal|Marktregulierung, Zugang, Entgelt, Infrastruktur und Universaldienst in der Telekommunikation bearbeiten.
Frequenzen Nummern und Endkunden|frequenz|nummer|campus|satellit|roaming|provider|router|netzneutral|notruf|mobilfunk|telekommunikation|tk-|Zuteilung, Nummern, Frequenz, Anbieterwechsel und Endnutzerrechte mit den zuständigen Verfahren verbinden.
Post und Eisenbahn|post-|eisenbahn|schiene|trasse|stationszugang|Postmarkt, Universaldienst, Eisenbahninfrastruktur, Entgelt und Zugang getrennt bearbeiten.
Digitale Dienste|digital-services|dsa|ddg|trusted-flagger|notice-and-action|vlop|Koordinator, Plattformpflicht, Beschwerde, Abhilfe und europäische Zuständigkeit im DSA-Kontext prüfen.
Verfahren und Rechtsschutz|verfahren|aktenzugang|anhoerung|auskunft|eilrechtsschutz|eilverfahren|beschwerde|vorstandsvorlage|stellungnahme|zustaendigkeit|konsultation|Akteneinsicht, Anhörung, Festlegung, Geheimnisschutz, Rechtsbehelf und Kommunikation bis zum konkreten Text führen.
''')
add('venture-capital-geber', '''
Investitionsziel und Auswahl|investorprofil|deal-sourcing|deal-triage|market-sizing|pitchdeck|teaser|pipeline|competitive|thesis|rookie|relationship|Investorenprofil, Geschäftsidee, Auswahl und Marktannahmen anhand der Unterlagen bewerten.
Due Diligence und Sektor|dd-|-dd$|data-room|founder-reference|health|medtech|climate|deep-tech|fintech|consumer|defense|esg|Regulatorische, technische und rechtliche Prüfung auf Zielunternehmen und Sektor zuschneiden.
Runde Bewertung und Beteiligung|seed|series-|growth|valuation|pre-post|cap-table|preference|anti-dilution|pro-rata|round|secondary|tokenis|Runde, Bewertung, Anteil, Verwässerung und Erlösverteilung rechnerisch und vertraglich abstimmen.
Finanzierungsvertrag und Vollzug|term-sheet|investment-agreement|shareholder-agreement|safe|kiss|wandeldarlehen|venture-debt|capital-call|funds-flow|kapitalerhoehung|notar|register|Finanzierung, Wandlung, Beteiligungsvertrag, Beschluss und Vollzug bis zur verwendbaren Fassung führen.
Founder Team und Rechte|founder|vesting|leaver|vsop|esop|arbeitsrecht|mitarbeiter|ip-chain|Team, Rechtekette, Beteiligung, Vesting, Ausscheiden und Konflikte mit Gesellschaftsrecht verbinden.
Governance und Portfoliosteuerung|board|beirat|observer|consent|protective|veto|information-right|reporting|kpi|portfolio|runway|milestone|quarterly|Governance, Information, Zustimmung, Reporting und Fortschritt auf die tatsächliche Beteiligung abstimmen.
Fonds Regulierung und Ausland|fonds|euveca|eltif|kagb|aif|bafin|gwg|ubo|kyc|aml|sanction|fdi|fusions|delaware|swiss|uk-us|international|us-securities|tax|funding|grants|Fondsstruktur, Aufsicht, Identität, Investitionsprüfung, Steuern und Auslandsbezug getrennt bearbeiten.
Krise Exit und Streit|exit|ma-sale|rescue|insolvency|crisis|dispute|drag-tag|rofr|transfer|Krise, Folgefinanzierung, Exit, Übertragung und Gesellschafterstreit mit den Rechten der Beteiligten prüfen.
Investitionsentscheidung und Kommunikation|ic-memo|committee|decision|follow-on|communication|email|feedback|ask-response|press|memo|task|reminder|watchlist|version|output|Entscheidungsvorlage, Beschluss, Kommunikation und offene Aufgaben aus demselben belegten Stand erstellen.
''')
add('bereicherungs-und-anfechtungsrecht-pruefer', '''
Leistungsbeziehung und Mehrpersonenfall|leistungsbegriff|leistungszweck|mehrpersonen|anweisungs|deckung|valuta|drittleistung|zahlstelle|fremde-schuld|kettenvertra|Bewusste Zuwendung, Zweck, Leistungsbeziehungen und Mehrpersonenverhältnis vor dem Anspruch bestimmen.
Leistungskondiktion und fehlender Rechtsgrund|leistungskondiktion|indebiti|causa|ob-rem|zweckverfehl|rechtsgrund|nichtiger-vertrag|ruecktritt|widerruf|anfechtung-142|Fehlenden oder entfallenen Rechtsgrund, Zweckverfehlung und Rückabwicklung des Vertrags prüfen.
Eingriff Verwendung und fremde Verfügung|nichtleistung|eingriff|816|verfuegung|eigentumsnutzung|ip-lizenz|verwendung|ebv|Eingriff, Rechtszuweisung, Verfügung eines Nichtberechtigten und Verwendungsersatz voneinander trennen.
Umfang Ausschluss und Haftung|818|819|822|entreicher|wertersatz|nutzung|surrogat|wertveraender|ersparte|814|817|gesetzesverstoss|schwarzarbeit|saldotheorie|boesglaeub|Haftungsumfang, Herausgabe, Wertersatz, Entreicherung und Ausschluss anhand der Tatsachen berechnen.
Einzelzwangsvollstreckung und Anfechtung|anfg-|Anfechtungsberechtigung, Tatbestand, Zeitraum, Benachteiligung und Rückgewähr nach dem Anfechtungsgesetz prüfen.
Insolvenzanfechtung|inso-|insolvenz|Insolvenzanfechtung nach Tatbestand, Rechtshandlung, Zeitraum, Benachteiligung und Kenntnis mit Gegenargumenten prüfen.
Spezielle Zuwendungen und Konkurrenz|arbeitsrecht|famil|partner|gesellschaft|miet|pacht|schenkung|leihe|kredit|darlehen|versicherung|oeffentlich|minderjaehr|konkurrenz|abgetreten|Rechtsgebietsbezogene Rückforderung und konkurrierende Ansprüche ohne Vermischung der Leistungswege behandeln.
Anspruchsaufbau und Durchsetzung|anspruchsziel|kondiktionskarte|triage|weichenstellung|beweis|darlegung|klage|verjaehr|vergleich|verteidigung|Vermögensverschiebung, Anspruch, Beweislast, Frist und Antrag bis zum konkreten Schreiben oder Schriftsatz führen.
''')
add('verbraucherschutzverband-durchsetzung', '''
Klageberechtigung und Verfahrenswahl|klageberechtigung|klageziele|quorum|verbandsstrategie|musterfeststellung|abhilfeklage|Klageberechtigung, Verfahrensart, Quorum und konkretes Rechtsschutzziel sauber bestimmen.
Anspruchsgruppen und Sammelfähigkeit|anspruchsgruppe|sammelfaehig|lebenssachverhalt|betroffenengruppe|Betroffenenkreis, einheitliche Tatsachen, Unterschiede und Sammelfähigkeit fallbezogen abgrenzen.
Materielle Verbraucherrechte|zustimmungsfiktion|uklag|uwg|bestellbutton|widerruf|diesel|schufa|scoring|Klauseln, Information, Widerruf, Schadensersatz und Datenschutz nach dem jeweiligen Lebenssachverhalt prüfen.
Beweise Betroffenenpool und Register|beweis|betroffenenformular|betroffenenpool|register|offenlegung|Belege, Datenschutz, Erfassung und Registerinformation so vorbereiten, dass die Anspruchsgruppen nachvollziehbar bleiben.
Klage Finanzierung und Risiko|klageschrift|kosten|finanzierung|interessenkonflikt|prozessrisiko|risiko-rot|individualklagen|Klage, Finanzierung, Kosten, Prozessrisiken und Parallelverfahren bis zum Schriftsatz bearbeiten.
Vergleich Umsetzung und Kontrolle|vergleich|austritt|umsetzung|sachwalter|erfolgsmonitor|Vergleich, Austritt, Umsetzungsverfahren und Erfolgskontrolle mit den tatsächlichen Ansprüchen abgleichen.
Kommunikation und Kampagne|kommunikation|presse|kampagnen|Verbraucher, Öffentlichkeit und Beteiligte verständlich informieren, ohne Ausgang oder Erstattung zu versprechen.
''')
