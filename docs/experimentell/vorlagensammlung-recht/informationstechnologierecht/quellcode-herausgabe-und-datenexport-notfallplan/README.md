# Quellcode-Herausgabe- und Datenexport-Notfallplan

Praxisvorlage für den geordneten Notfallvollzug bei Ausfall, Kündigung, Insolvenz oder schwerer Leistungsstörung eines IT-Dienstleisters.

## Download
- [⬇ Quellcode Herausgabe- und Datenexport Notfallplan – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/quellcode-herausgabe-und-datenexport-notfallplan/quellcode-herausgabe-und-datenexport-notfallplan.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Quellcode Herausgabe- und Datenexport Notfallplan – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/quellcode-herausgabe-und-datenexport-notfallplan/quellcode-herausgabe-und-datenexport-notfallplan.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`quellcode-herausgabe-und-datenexport-notfallplan.odt`](quellcode-herausgabe-und-datenexport-notfallplan.odt) · [`quellcode-herausgabe-und-datenexport-notfallplan.md`](quellcode-herausgabe-und-datenexport-notfallplan.md)

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

1. Zuerst wird der Aktivierungsfall anhand von Vertrag, Leistungsstörung und Fortführungsbedarf dokumentiert. Zugleich werden Repository-Stände, Build-Umgebung, Schlüssel, Datenbestände und verantwortliche Ansprechpartner beweissicher erfasst.
2. Danach wird das Herausgabepaket in Quellcode, Abhängigkeiten, Build-Anweisungen, Infrastrukturdefinitionen, Datenexport, Zugangsdaten und Betriebsdokumentation zerlegt. Für jede Einheit werden Format, Prüfsumme, Übergabekanal und Abnahmetest festgelegt.
3. Nach Übergabe werden Reproduzierbarkeit, Vollständigkeit und Importfähigkeit getestet. Erst das Prüfprotokoll löst Rückgabe, Sperrung alter Zugänge und datenschutzkonforme Löschung verbliebener Kopien aus.

### Typische Gegnereinwände mit Antwortlinie

- Der Anbieter hält den Aktivierungsfall für nicht eingetreten. Die Antwortlinie verknüpft Vertragsklausel, Fristsetzung, konkrete Leistungsstörung und dokumentierten Fortführungsbedarf.
- Der Quellcode sei vollständig, obwohl Build oder Deployment nicht reproduzierbar sind. Die Antwortlinie misst Vollständigkeit am vereinbarten Abnahmetest und verlangt alle benötigten Abhängigkeiten und Konfigurationen.
- Geheimhaltungs- oder Lizenzrechte Dritter stünden der Übergabe entgegen. Die Antwortlinie trennt nicht übertragbare Rechte von notwendigem Betriebswissen und aktiviert Ersatz-, Escrow- oder Unterlizenzmechanismen.

### Häufige Fehler

- Ein veralteter Repository-Snapshot wird akzeptiert, ohne Commit-ID, Releasebezug und produktive Version abzugleichen.
- Exporten fehlen Schema, Zeichensatz, Schlüsselbeziehungen oder Importanleitung.
- Zugangsdaten werden unverschlüsselt übertragen oder nach dem Kontrollwechsel nicht widerrufen.

## Verwandte Vorlagen

- [Software-Escrow-Vereinbarung](../software-escrow-vereinbarung/) — begründet Hinterlegung, Aktualisierung und Herausgabefälle vor Eintritt des Notfalls.
- [IT-Outsourcing-Transition-Vertrag](../it-outsourcing-transition-vertrag/) — plant eine reguläre Übernahme oder Rückübertragung mit längerer Transition.
- [Softwarelizenzvertrag On-Premise (Dauerlizenz; §§ 433, 453 BGB; §§ 69a ff. UrhG)](../softwarelizenzvertrag-on-premise/) — regelt die nach Herausgabe benötigten Nutzungsrechte.
- [Agiler Softwareentwicklungsvertrag](../software-entwicklungsvertrag-agil/) — stellt Quellcode, Build-Artefakte und Dokumentation bereits sprintweise bereit.
