# Betriebs- und Sicherheitskonzept für ein Satellitenbodensegment

Verbindliches Betriebskonzept für Missionskontrolle, Telemetrie, Telecommand, Schlüssel, Bodenstationen, Dienstleister, Notbetrieb und Sicherheitsvorfälle.

## Download

- [Bodensegment-Betriebs- und Sicherheitskonzept – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/weltraumrecht/bodensegment-betriebs-sicherheitskonzept-satellit/bodensegment-betriebs-sicherheitskonzept-satellit.odt) — Offene Bürofassung
- [Bodensegment-Betriebs- und Sicherheitskonzept – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/weltraumrecht/bodensegment-betriebs-sicherheitskonzept-satellit/bodensegment-betriebs-sicherheitskonzept-satellit.md.zip) — Bearbeitbare Markdown-Fassung

Vorschau im Repository: [`bodensegment-betriebs-sicherheitskonzept-satellit.odt`](bodensegment-betriebs-sicherheitskonzept-satellit.odt) · [`bodensegment-betriebs-sicherheitskonzept-satellit.md`](bodensegment-betriebs-sicherheitskonzept-satellit.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung oder Sicherheitszertifizierung. Missionsarchitektur, Bedrohungsmodell und gesetzliche Anforderungen sind für das konkrete System zu bestimmen. Mandats-, Betriebs- und Personaldaten sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Verwendung ausschließlich auf eigene Gewähr und auf eigene Gefahr.

Lizenz: Apache-2.0 OR MIT.

## Einschlägige Normen

- § 4 Abs. 1 Nr. 2 bis 4 SatDSiG — Schutz von Befehlsfolgen, Datenübermittlung, Räumen und Anlagen bei hochwertigen Erdfernerkundungssystemen
- §§ 5 und 6 SatDSiG — fünfjährige Kommandodokumentation und unverzügliche Anzeigen
- §§ 91 und 95 TKG — Frequenzzuteilung und Orbitpositionen
- Art. 5 Abs. 1 Buchst. f, Art. 24, 25 und 32 DSGVO — Integrität, Verantwortlichkeit, Technikgestaltung und Sicherheit personenbezogener Betriebsdaten

Amtliche Quellen: [SatDSiG](https://www.gesetze-im-internet.de/satdsig/), [TKG](https://www.gesetze-im-internet.de/tkg_2021/), [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## Anwendungsbereich

Die Vorlage gilt für ein missionskritisches Bodensegment aus Missionskontrollsystem, Bodenstationen, Netzen, Rechenzentren, Cloud-Diensten, Schlüsselverwaltung und Betriebspersonal. Die SatDSiG-Bausteine sind nur verbindlich, wenn dessen Anwendungsbereich eröffnet ist; sie eignen sich darüber hinaus als Sicherheitsreferenz. Betreiber eines hochwertigen Erdfernerkundungssystems benötigen zusätzlich `weltraumrecht/antrag-genehmigung-erdfernerkundungssystem-satdsig/`.

## Pflichtangaben

Benötigt werden Missionsphasen, Systemgrenzen, Betriebsstandorte, Rollen, Kommunikationsfenster, Befehlsfreigaben, Kryptografie und Schlüssel, Lieferanten, Protokollierung, Notfallmodi, Wiederanlaufziele, Anomalie- und Incident-Prozesse sowie Freigabe- und Änderungsverantwortung.

## Mustertext mit Platzhaltern

Das Konzept ordnet jeden betrieblichen Schritt einer Rolle, Freigabe, technischen Kontrolle, Aufzeichnung und Eskalation zu. Es trennt Routinebetrieb, kritische Kommandos, Notbetrieb und Sicherheitsvorfälle.

## Hinweise zur Verwendung

Das Konzept muss die reale Systemarchitektur abbilden. Ein allgemeines IT-Sicherheitskonzept genügt nicht, wenn Telecommand-Freigaben, Bodenstationswechsel, Kontaktfenster, Orbitmanöver, Safe Mode oder Schlüsselverlust ungeregelt bleiben.

Dienstleisterzugriff und Cloud-Betrieb sind als Teil der Kommandokette zu behandeln. Vertragliche Pflichten müssen Kontrollrechte, Unterauftragnehmer, Exit, Herausgabe von Protokollen und Notfallunterstützung abdecken. Frequenzzuteilung, SatDSiG-Genehmigung und Datenschutzprüfung bleiben eigenständige Verfahren.

## Taktische Hinweise

### Vorgehensreihenfolge

Systemgrenze, Mission Owner, Betriebsrollen, Standorte, Netze, Cloud-Dienste, Schlüssel und sämtliche Kommando- sowie Telemetriepfade werden zuerst inventarisiert. Danach sind Normalbetrieb, Vier-Augen-Freigaben, privilegierte Zugriffe, Schichtübergabe, Anomalie, Notbetrieb, Wiederanlauf, Änderungsmanagement und Protokollaufbewahrung mit konkreten Tests und Freigabeverantwortlichen zu verbinden.

### Typische Einwände und Antwortlinien

- Dem Einwand unkontrollierter Dienstleisterzugriffe ist mit benannten Konten, zeitlicher Freigabe, Sitzungsprotokollierung, Unterauftragnehmerkontrolle und Notfallentzug zu begegnen.
- Bei einem Single Point of Failure sind Ersatzstandort, Offline-Verfahren, Schlüsselwiederherstellung und regelmäßig protokollierte Übungen nachzuweisen.

### Häufige Fehler

- Architekturdiagramm, Berechtigungsmatrix und tatsächlich produktive Konten weisen unterschiedliche Systemgrenzen auf.
- Notfallkarten beschreiben Zuständigkeiten, enthalten aber keine getesteten technischen Schritte für sicheren Zustand und Wiederanlauf.

## Verwandte Vorlagen

- [Antrag auf Genehmigung eines hochwertigen Erdfernerkundungssystems (§§ 3, 4 SatDSiG)](../antrag-genehmigung-erdfernerkundungssystem-satdsig/) — für den regulatorischen Betreiberantrag.
- [Weltraumschrott-, Kollisionsvermeidungs- und End-of-Life-Plan](../weltraumschrott-kollisionsvermeidungs-end-of-life-plan/) — für Bahnüberwachung, Manöver und Missionsende.
- [Antrag auf Frequenzzuteilung für eine Erdfunkstelle oder Satellitenantenne](../antrag-frequenzzuteilung-erdfunkstelle-bnetza/) — für die Funkzulassung des Bodensegments.
