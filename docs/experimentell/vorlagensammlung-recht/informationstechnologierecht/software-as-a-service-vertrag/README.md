# Software-as-a-Service-Vertrag (B2B; SLA)

Spezifischer B2B-Vertrag über die entgeltliche Bereitstellung einer cloudbasierten Softwarelösung mit Nutzerkreis, Service-Level-Agreement, API-Regeln, Auftragsverarbeitung, Unterauftragnehmersteuerung, Datenlokation und Exit-Export.

## Download
- [⬇ Software as a Service Vertrag (B2B; SLA) – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/software-as-a-service-vertrag/software-as-a-service-vertrag.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Software as a Service Vertrag (B2B; SLA) – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/software-as-a-service-vertrag/software-as-a-service-vertrag.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`software-as-a-service-vertrag.odt`](software-as-a-service-vertrag.odt) · [`software-as-a-service-vertrag.md`](software-as-a-service-vertrag.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage betrifft die zeitweise Nutzung einer bereitgestellten Software im B2B-Verhältnis. Nach BGH, Urteil vom 15. November 2006, XII ZR 120/04, ist die zentrale Gebrauchsüberlassung eines ASP-Vertrags mietrechtlich einzuordnen. Daraus folgt keine Einordnung jedes gemischten IT-Vertrags als Mietvertrag; eigenständige Entwicklungs- und Migrationsleistungen separat prüfen. [Amtlicher Entscheidungsvolltext](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=38367).

## Einschlägige Normen

- Paragrafen 535 und 536 ff. BGB für die entgeltliche, zeitweise Nutzung bereitgestellter Standardsoftware; Paragrafen 631 und 640 BGB nur für gesondert geschuldete Herstellungserfolge, etwa eine definierte Entwicklung oder Migration.
- Paragrafen 611 und 675 BGB für selbständige Beratungs- oder Unterstützungsleistungen ohne geschuldeten Erfolg. Paragraf 611a BGB betrifft Arbeitsverträge und ist keine allgemeine SaaS-Vertragsgrundlage.
- Paragrafen 327 ff. BGB gelten im einschlägigen Verbrauchervertrag, nicht unmittelbar für diesen B2B-Vertrag. Gesetzliche oder vertraglich vereinbarte Mängel- und Aktualisierungspflichten im B2B-Verhältnis eigenständig bestimmen.
- §§ 280, 281, 286, 307 BGB zu Pflichtverletzung, Nacherfüllung, Verzug und AGB-Kontrolle.
- Art. 28, Art. 32, Art. 33 DSGVO, wenn Betrieb, Hosting, Support oder Migration personenbezogene Daten betrifft.

## Hinweise zur Verwendung

IT-Verträge müssen Leistungsgegenstand, Servicegrenze, Mitwirkung, Change Request, Abnahme, Betrieb, Mängel, Datenexport, Exit und Sicherheit voneinander trennen. Pauschale Verfügbarkeits- oder Projektformulierungen tragen nicht, wenn Provider, Kunde, Unterauftragnehmer und Cloudplattform unterschiedliche Pflichten haben.

Fristen- und Beweisarchitektur: Meilenstein, Sprint, Abnahme, Incident-Reaktionszeit, Wiederherstellungszeit, Wartungsfenster, Exit-Start, Datenrückgabe und Löschung werden mit Messpunkt, Eskalation und Rechtsfolge geführt. Bei personenbezogenen Daten wird parallel ein AVV nach `informationstechnologierecht/auftragsverarbeitungsvertrag-dsgvo/` oder eine eigene Verantwortlichkeitsregel genutzt.

Abgrenzung: Für SaaS `informationstechnologierecht/software-as-a-service-vertrag/`; für agile Entwicklung `informationstechnologierecht/software-entwicklungsvertrag-agil/`; für Outsourcing und Exit `informationstechnologierecht/it-outsourcing-transition-vertrag/`.

## Taktische Hinweise

### Vorgehensreihenfolge

1. Vor der Preisverhandlung werden Mandant, Nutzergruppen, Funktionen, Schnittstellen, Datenkategorien und zulässige Nutzung verbindlich beschrieben. Erst danach werden Verfügbarkeit und Support auf die geschäftskritischen Funktionen zugeschnitten.
2. Service-Level-Messung, Ausschlusszeiten, Störungsklassen, Service Credits und Kündigungsrechte werden als abgestufte Rechtsfolgenkette formuliert. Datenschutz, Unterauftragnehmer und Datenlokation müssen dieselbe Betriebsarchitektur abbilden.
3. Vor Produktivsetzung werden Berechtigungskonzept, Exporttest und Wiederherstellungsnachweis dokumentiert. Preisänderung, Vertragsende und Exit werden so gestaltet, dass Daten und Prozesse ohne faktische Anbieterbindung migrierbar bleiben.

### Typische Gegnereinwände mit Antwortlinie

- Der Anbieter verweist bei Ausfällen auf pauschale Wartungs- oder Drittanbieter-Ausnahmen. Die Antwortlinie verlangt eng definierte Ausschlüsse, Vorankündigung und eine gesonderte Behandlung selbst gewählter Unterauftragnehmer.
- Der Kunde hält Service Credits für unzureichend. Die Antwortlinie kombiniert Gutschrift, Eskalation und Sonderkündigung und lässt weitergehende Rechte nur im vereinbarten Umfang unberührt.
- Der Anbieter beansprucht ein umfassendes Recht zur Funktionsänderung. Die Antwortlinie grenzt laufende Verbesserung von wesentlicher Leistungsreduktion ab und knüpft letztere an Ankündigung, Zumutbarkeit und Exit-Recht.

### Häufige Fehler

- Verfügbarkeit wird ohne Messpunkt, Messzeitraum, Rundungsregel und ausgeschlossene Zeit berechnet.
- Nutzer-, Speicher- oder API-Grenzen stehen nur in Preislisten und sind nicht mit Rechtsfolgen verknüpft.
- Der Exit nennt weder Exportformat, Frist, Kosten noch Löschung nach bestätigter Übernahme.

## Verwandte Vorlagen

- [Enterprise-SaaS-Rahmenvertrag](../enterprise-saas-rahmenvertrag/) — erweitert das Modell um konzernweite Abrufe, Governance und Leistungsscheine.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — vertieft Messmethoden, Störungsklassen und Rechtsfolgen.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — regelt die datenschutzrechtliche Auftragsverarbeitung neben dem Hauptvertrag.
- [Platform-as-a-Service-Vertrag B2B](../platform-as-a-service-b2b-vertrag/) — passt, wenn der Kunde eigene Anwendungen auf einer technischen Plattform betreibt.
