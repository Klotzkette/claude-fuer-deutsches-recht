# Software-Escrow-Vereinbarung

Dreiparteienvereinbarung über Hinterlegung von Quellcode, Release-Updates, Herausgabefälle und Prüfung.

## Download
- [⬇ Software Escrow Vereinbarung – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/software-escrow-vereinbarung/software-escrow-vereinbarung.odt) — OpenDocument-Arbeitsfassung
- [⬇ Software Escrow Vereinbarung – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/software-escrow-vereinbarung/software-escrow-vereinbarung.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`software-escrow-vereinbarung.odt`](software-escrow-vereinbarung.odt) · [`software-escrow-vereinbarung.md`](software-escrow-vereinbarung.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage dient einem IT-Vertrag mit Projekt-, Betriebs-, Lizenz-, Support-, Cloud-, API- oder Exit-Bezug. Sie passt, wenn technische Leistung, Service Level, Mitwirkung, Abnahme, Mängel, Sicherheit, Datenschutz und Exit konkret verhandelt werden.

## Einschlägige Normen

- §§ 631, 640 BGB für werkvertragliche Projekt-, Migrations-, Entwicklungs- und Abnahmepflichten.
- §§ 611, 611a, 675 BGB, wenn Beratung, Betrieb, Support oder laufende Dienste im Vordergrund stehen.
- §§ 327 ff. BGB bei digitalen Produkten gegenüber Verbrauchern; bei B2B als Prüfanker für Update-, Bereitstellungs- und Mängelmechanik.
- §§ 280, 281, 286, 307 BGB zu Pflichtverletzung, Nacherfüllung, Verzug und AGB-Kontrolle.
- Art. 28, Art. 32, Art. 33 DSGVO, wenn Betrieb, Hosting, Support oder Migration personenbezogene Daten betrifft.

## Hinweise zur Verwendung

IT-Verträge müssen Leistungsgegenstand, Servicegrenze, Mitwirkung, Change Request, Abnahme, Betrieb, Mängel, Datenexport, Exit und Sicherheit voneinander trennen. Pauschale Verfügbarkeits- oder Projektformulierungen tragen nicht, wenn Provider, Kunde, Unterauftragnehmer und Cloudplattform unterschiedliche Pflichten haben.

Fristen- und Beweisarchitektur: Meilenstein, Sprint, Abnahme, Incident-Reaktionszeit, Wiederherstellungszeit, Wartungsfenster, Exit-Start, Datenrückgabe und Löschung werden mit Messpunkt, Eskalation und Rechtsfolge geführt. Bei personenbezogenen Daten wird parallel ein AVV nach `informationstechnologierecht/auftragsverarbeitungsvertrag-dsgvo/` oder eine eigene Verantwortlichkeitsregel genutzt.

Abgrenzung: Für SaaS `informationstechnologierecht/software-as-a-service-vertrag/`; für agile Entwicklung `informationstechnologierecht/software-entwicklungsvertrag-agil/`; für Outsourcing und Exit `informationstechnologierecht/it-outsourcing-transition-vertrag/`.

## Taktische Hinweise

### Vorgehensreihenfolge

1. Zunächst werden Softwareversion, Quellcode, Build-Werkzeuge, Abhängigkeiten, Dokumentation und Zugangsmittel vollständig inventarisiert. Der Hinterlegungsgegenstand wird mit dem produktiv eingesetzten Release verknüpft.
2. Danach werden Aktualisierungsrhythmus, technische Vollständigkeitsprüfung und Herausgabefälle objektiv bestimmt. Für streitige Aktivierungsfälle wird ein beschleunigtes Prüfverfahren mit Anhörung und vorläufiger Materialsicherung festgelegt.
3. Vor jeder Hinterlegung werden Prüfsumme, Lesbarkeit und Reproduzierbarkeit dokumentiert. Nach Herausgabe werden Nutzungszweck, Geheimnisschutz und Rückgabe oder Vernichtung kontrolliert.

### Typische Gegnereinwände mit Antwortlinie

- Der Softwareanbieter lehnt eine Build-Prüfung wegen Geheimhaltungsrisiken ab. Die Antwortlinie begrenzt die Prüfung auf den neutralen Escrow-Agenten und sichert Zugriff und Protokollierung.
- Der Kunde hält Insolvenz oder dauerhafte Pflegeeinstellung für eingetreten. Die Antwortlinie verlangt objektive Nachweise und wendet das vereinbarte Anhörungs- und Entscheidungsverfahren an.
- Drittkomponenten dürften nicht mit herausgegeben werden. Die Antwortlinie unterscheidet hinterlegbares Material, notwendige Beschaffungsinformationen und bereits eingeräumte Dritt- oder Open-Source-Rechte.

### Häufige Fehler

- Hinterlegt wird nur Quellcode, obwohl Compiler, Abhängigkeiten, Schlüssel oder Deployment-Anweisungen fehlen.
- Aktualisierungspflichten haben keine Frist, keinen Versionsabgleich und keine Rechtsfolge.
- Das Nutzungsrecht nach Herausgabe ist enger als für Fehlerbehebung und Weiterbetrieb erforderlich.

## Verwandte Vorlagen

- [Quellcode-Herausgabe- und Datenexport-Notfallplan](../quellcode-herausgabe-und-datenexport-notfallplan/) — setzt Übergabe und technische Prüfung im Aktivierungsfall um.
- [Softwarelizenzvertrag On-Premise (Dauerlizenz; §§ 433, 453 BGB; §§ 69a ff. UrhG)](../softwarelizenzvertrag-on-premise/) — begründet die regulären Nutzungsrechte an der Software.
- [Agiler Softwareentwicklungsvertrag](../software-entwicklungsvertrag-agil/) — regelt Quellcodebestand und Aktualisierung während der Entwicklung.
- [Softwarepflege- und Supportvertrag (Maintenance; SLA)](../softwarepflege-und-supportvertrag/) — definiert Pflegeausfälle, die einen Herausgabefall auslösen können.
