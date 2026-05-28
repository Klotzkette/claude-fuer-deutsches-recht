# selbstvertreter-amtsgericht

Plugin für Bürgerinnen und Bürger, die sich vor dem Amtsgericht **ohne Rechtsanwalt** selbst vertreten wollen. Es ist als geführter Begleiter gebaut: erst Fristen und Gericht klären, dann Streitwert, Antrag, Beweise und Kosten ordnen, dann den passenden Schriftsatz oder Terminplan vorbereiten.

## Für wen?

- Sie wollen eine Geldforderung bis zur Wertgrenze des § 23 Nr. 1 GVG einklagen (seit 01.01.2026: **10.000 EUR**, Anhebung von 5.000 EUR durch das Justizstandort-Stärkungsgesetz).
- Sie sind verklagt worden und wollen sich selbst verteidigen.
- Sie wollen Mietsachen, Reisemängel, Familienunterhalt oder andere AG-typische Streitigkeiten betreiben.
- Sie wollen vor einer möglichen Mandatierung verstehen, was rechtlich passiert.

## Was kann das Plugin?

Es liefert Skills zu:

- **Anfänger-Workflow**: geführter Modus mit kleinen Schritten, einfacher Sprache, Frist zuerst und klarer nächster Handlung.
- **Sanity-Check**: letzte Ampelprüfung vor Klage, Klageerwiderung, Replik, Termin, Vergleich oder Rechtsmittel.
- **Rechtsprechungschat**: Rechtsprechung finden, verstehen, nicht überdehnen und gerichtstauglich zitieren.
- **Zulassungsgrenzen-Check**: AG/LG-Zuständigkeit, § 23 GVG, § 495a ZPO, § 511 ZPO, Berufung und Anwaltszwang.
- **Zuständigkeit**: Sachlich (§ 23 GVG, § 23a-c GVG), örtlich (§§ 12 ff. ZPO), Verbrauchergerichtsstand (§ 29c ZPO).
- **Vor-Klage-Vorbereitung**: Erfolgsaussichten-Check, Anspruchsgrundlage finden, Verjährung prüfen, außergerichtliche Mahnung, Mahnverfahren, Beweismittel sammeln, Kostenrisiko berechnen.
- **Klageschrift erstellen**: Pflichtbestandteile, bestimmter Antrag, Tatsachenvortrag, Beweisangebote, Anlagen, Streitwert, vereinfachtes Verfahren § 495a ZPO.
- **Einreichung**: Mein Justizpostfach (MJP), § 130a ZPO elektronisch, Papierform, Fax-Grenzen, Rechtsantragsstelle, Versand durch Dritte (Risiko!), Gerichtskostenvorschuss.
- **PKH und Beratungshilfe**: Antrag, Ablehnung, Ratenzahlung, Beratungshilfe vor Klage.
- **Klageerwiderung**: Fristen, Checkliste, substantiiertes Bestreiten, Einreden, Widerklage, Säumnis vermeiden.
- **Replik, Duplik, Hinweise nach § 139 ZPO**, nachgereichter Schriftsatz, Wiedereinsetzung.
- **Beweis**: Beweislast, Zeuge, Urkunde, Sachverständiger, Augenschein, Parteivernehmung, eidesstattliche Versicherung, Folgen fehlenden Beweises.
- **Termin**: Ladung, Vorbereitung, Säumnis im Termin, Verhalten im Saal, Vergleich nach § 278 II ZPO.
- **Fristen**: Berechnung, eigenes Fristenbuch, Zustellung als Fristbeginn, Fristverlängerung.
- **Urteil und Rechtsmittel**: Verkündung, Urteilsprüfung, Berufung zum LG (Wertgrenze § 511 ZPO), Zulassung bei niedrigem Streitwert, Rechtsmittelfrist.
- **Vollstreckung-Querverweise**: Rechtskraft, Vollstreckungsklausel, Verweis auf separaten Substitutionsagenten für die Zwangsvollstreckung.
- **Spezielles**: Video-Verhandlung § 128a ZPO, Dolmetscher § 185 GVG, Kostenfestsetzung, typische Laien-Fehler, wann es sich lohnt, doch einen Anwalt einzuschalten.

## Sprache und Ton

- Sie-Form. Einfache, klare Sätze. Fachbegriffe werden beim ersten Vorkommen in einer Skill in 1-2 Sätzen erklärt.
- Direkte Schritt-fuer-Schritt-Anleitungen.
- Ehrlicher Hinweis, wo verifiziert werden muss (Reform-Lage, Aktenzeichen, Fundstellen).

## Was das Plugin **nicht** macht

- Keine Garantie, dass Sie gewinnen.
- Keine anwaltliche Mandatsführung. Bei komplexen Fällen, hohem Risiko, Landgericht, Familiengericht, Berufung oder unklarer Zustellung empfiehlt das Plugin deutlich Rechtsantragsstelle, Beratungshilfe, PKH oder Anwalt — siehe Skill `wann-doch-anwalt-grenzfaelle`.
- Keine Zwangsvollstreckung. Dafür existiert ein separater Substitutionsagent.

## Einstieg

Starten Sie mit `anfaenger-workflow-amtsgericht`, wenn Sie geführt werden möchten. Nutzen Sie `orientierung-selbstvertreter-amtsgericht`, wenn Sie nur eine schnelle Triage wollen, und `sanity-check-selbstvertretung-amtsgericht`, bevor etwas an das Gericht geht.
