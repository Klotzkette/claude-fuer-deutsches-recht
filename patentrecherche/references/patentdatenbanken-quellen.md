# Patentdatenbanken — Quellenübersicht für die agentische Recherche

> Pflichtreferenz für alle Recherche-Skills dieses Plugins. Jede Recherche dokumentiert in ihrem Bericht, welche Datenbanken in welcher Tiefe befragt wurden — und welche bewusst ausgelassen wurden.

## 1. Espacenet (Europäisches Patentamt)

- URL: <https://worldwide.espacenet.com>
- Abdeckung: ca. 150 Mio. Patentdokumente weltweit, über 100 Patentbehörden, Datenstand wöchentlich aktualisiert.
- Stärken: **INPADOC-Patentfamilie**, Citation-Map, automatische maschinelle Übersetzung (Patent Translate, basierend auf Google Translate für 32 Sprachen), Volltext-Suche in EP und PCT, kostenlos.
- Schwächen: Rechtsstand (Annuitäten, Lizenzen, Verfügungen) nur eingeschränkt; teils Latenz bei nicht-EP-Behörden; UI für Anfänger gewöhnungsbedürftig.
- Suchsyntax: **Smart Search** akzeptiert natürlichsprachliche Stichworte mit Feldoperatoren (`ti=` Titel, `ab=` Abstract, `pa=` Anmelder, `in=` Erfinder, `cpc=` CPC-Klasse, `pn=` Publikationsnummer). Boolean: `AND`, `OR`, `NOT`. Wildcards `*` und `?`. Trunkierung links und rechts möglich.
- Empfohlene Bedienung agentisch: Klassen-Suche mit `cpc=H02J3/14` AND Anmelder-Suche; anschließend Patentfamilie aufrufen für jedes Treffer-Dokument; Citation-Map exportieren für Stand-der-Technik-Erweiterung.

## 2. Google Patents

- URL: <https://patents.google.com>
- Abdeckung: ca. 120 Mio. Dokumente aus 100+ Behörden, einschließlich nicht-Patent-Literatur (NPL) über Google Scholar-Verknüpfung.
- Stärken: **Semantische Suche** (Google interpretiert natürliche Sprache), **Prior Art Finder** (Knopfdruck-Stand-der-Technik), Cross-Verknüpfung zu Google Scholar, schnelle Ladezeiten, gute Volltext-Recherche auch in nicht-englischen Dokumenten durch Übersetzung.
- Schwächen: Keine offizielle Rechtsstandsdatenbank (für Annuitäten/Erlöschen immer Originalregister konsultieren). Patentfamilie-Definition weicht teils von INPADOC ab. Algorithmus nicht transparent.
- Suchsyntax: Freitext plus Filter (Anmelder, Erfinder, Klasse, Datum). Operatoren: Anführungszeichen für Phrasen, `-` für Ausschluss, `OR`.
- Empfohlene Bedienung agentisch: Erste Triage natürlichsprachlich ("3-phase grid balancing inverter switching frequency"); danach Filter setzen (Anmelder/Datum); Prior Art Finder bei jedem relevanten Treffer als Erweiterungspunkt.

## 3. DPMAregister (Deutsches Patent- und Markenamt — Rechtsstand DE)

- URL: <https://register.dpma.de>
- Abdeckung: deutsche Patente, Gebrauchsmuster, Marken, Geschmacksmuster — vollständiger **Rechtsstand**, Akteneinsicht möglich (für veröffentlichte Akten).
- Stärken: **autoritative Quelle für Rechtsstand DE** (Annuitäten, Erlöschen, Übertragungen, Lizenzen, Einspruchsverfahren, Nichtigkeitsverfahren). Hier liegt die Wahrheit zur Frage "lebt das Patent noch?" für deutsche Schutzrechte.
- Schwächen: Nur DE; UI bürokratisch; kein Volltext der Patentschrift in der Standard-Recherche (dafür DEPATISnet).
- Suchsyntax: Aktenzeichen oder Publikationsnummer, dann "Akteneinsicht".
- Empfohlene Bedienung agentisch: Nach jeder Stand-der-Technik-Recherche, in der DE-Patente vorkommen, Rechtsstand jedes relevanten DE-Dokuments hier verifizieren. **Niemals nur auf Google Patents oder Espacenet verlassen.**

## 4. DEPATISnet (DPMA-Recherchedatenbank)

- URL: <https://depatisnet.dpma.de>
- Abdeckung: weltweit ca. 100 Mio. Patentdokumente, mit besonders gepflegtem DE-Bestand und ausgezeichneter klassifikatorischer Erschließung (IPC, CPC, DEKLA).
- Stärken: **Expertenrecherche mit IKOFAX-Syntax**, sehr präzise Feldsuche, hervorragend für strukturierte Klassen- und Anmelder-Recherchen, gepflegte Bibliographie.
- Schwächen: Bedienung deutlich technischer als Espacenet/Google Patents; volltextliche Suche in fremdsprachigen Patentschriften eingeschränkt; UI älter.
- Suchsyntax (IKOFAX): Feldcodes mit Schrägstrich: `H02J3/14/ICP` (IPC-Klasse), `Siemens/PA` (Anmelder), `2020/PD` (Veröffentlichungsdatum). Boolean: `AND`, `OR`, `NOT`. Wildcards `?` (ein Zeichen) `*` (beliebig viele).
- Empfohlene Bedienung agentisch: Wenn Espacenet/Google-Patents-Treffer zu unscharf sind und eine **enge** klassen-/anmelderbasierte Recherche nötig ist; oder wenn die DE-Bestände vollständig erschöpft werden sollen.

## 5. EPO Register (Europäisches Patentregister)

- URL: <https://register.epo.org>
- Abdeckung: alle **europäischen Patentanmeldungen und Patente** (EP-Schutzrechte), einschließlich Rechtsstand, Einspruchsverfahren, Beschwerdeverfahren, validierte nationale Phasen.
- Stärken: **autoritative Quelle für Rechtsstand EP**. Akteneinsicht (für veröffentlichte Akten) — alle Schriftsätze, Bescheide, Entgegenhaltungen einsehbar. Family-Information mit nationalen Validierungen pro EPC-Vertragsstaat.
- Schwächen: Nur EP; nationale Phase nach Validierung muss in den jeweiligen nationalen Registern (DPMAregister für DE, INPI für FR, etc.) verifiziert werden.
- Bedienung agentisch: Vor jedem FTO-Statement zu einem EP-Patent: Status in welchen Vertragsstaaten validiert? Aktenstand? Einspruch hängig? Beschwerde hängig? Aktive Lizenzen? Alle diese Fragen beantwortet das EPO Register.

## 6. WIPO PATENTSCOPE

- URL: <https://patentscope.wipo.int>
- Abdeckung: **PCT-Anmeldungen** (WO-Nummern) plus nationale Sammlungen von ca. 75 Behörden.
- Stärken: Wichtigste Quelle für die **internationale PCT-Phase**, einschließlich des International Search Report (ISR), der Written Opinion und der International Preliminary Report on Patentability (IPRP). Mehrsprachige Suche. Chemical Compound Search.
- Schwächen: Rechtsstand der nationalen Phasen liegt in den jeweiligen nationalen Registern, nicht hier.
- Bedienung agentisch: Wenn PCT-Anmeldungen im Treffer sind, hier den ISR und die Written Opinion abrufen — die enthalten bereits eine erste Patentamts-Bewertung zu Neuheit und erfinderischer Tätigkeit, oft mit Verweis auf wichtige Entgegenhaltungen.

## 7. USPTO Patent Public Search (PPUBS)

- URL: <https://ppubs.uspto.gov/pubwebapp/external.html>
- Abdeckung: US-Patente und US-Patentanmeldungen seit 1790. Vereinigt die früheren PatFT- und AppFT-Datenbanken.
- Stärken: **autoritative Quelle für US-Patente**, Volltext, Volltext-Suche, Citations forwards und backwards, Rechtsstand (Maintenance Fees).
- Schwächen: UI ungewöhnlich, eigene Suchsyntax mit Feldcodes (`.ABTX.`, `.AS.`, `.IS.`, `.IN.`), Lernkurve.
- Bedienung agentisch: Für US-spezifische FTO-Fragen, US-Rechtsstand, US-Akteneinsicht (Public PAIR / Patent Center).

## 8. J-PlatPat (Japan Platform for Patent Information)

- URL: <https://www.j-platpat.inpit.go.jp>
- Abdeckung: japanische Patente, Gebrauchsmuster, Marken, Geschmacksmuster.
- Stärken: maschinelle EN-Übersetzungen, AIPN für US/EP-Recherchen zu japanischen Gegenstücken. Volltext-Suche.
- Schwächen: UI nur teilweise EN. Für tiefe Recherchen JP-Volltextkompetenz oder spezialisiertes Übersetzungs-Tooling nötig.
- Bedienung agentisch: Falls Stand der Technik in JP zu vermuten ist (häufig in Elektronik, Robotik, Werkstoffen, Automotive).

## 9. CNIPA / China National Intellectual Property Administration

- URL: <https://english.cnipa.gov.cn> und für Recherche <http://english.cnipa.gov.cn/col/col3091/index.html>
- Abdeckung: CN-Schutzrechte. Volumen extrem hoch (über 4 Mio. Anmeldungen jährlich).
- Stärken: Pflicht für jede ernsthafte FTO-Recherche mit CN-Bezug (Produktherstellung oder -vertrieb in China).
- Schwächen: Suchsyntax und UI für CN-Muttersprachler ausgelegt; agentisch sind Espacenet (mit Patent-Translate) und Google Patents oft praktikabler für eine erste Triage.

## 10. KIPRIS (Korean Intellectual Property Rights Information Service)

- URL: <https://www.kipris.or.kr>
- Abdeckung: KR-Schutzrechte.
- Bedienung agentisch: Für KR-spezifischen Stand der Technik insbesondere in Elektronik, Mobilfunk, Display-Technik, Halbleiter.

## 11. Espacenet Global Patent Index (GPI)

- URL: <https://www.epo.org/de/searching-for-patents/business/gpi>
- **Kostenpflichtig**; für agentische Routine-Recherche nicht relevant. Wird hier nur erwähnt, damit klar ist, dass für **forensisch belastbare** Recherchen über die kostenfreien Tools hinaus auch das Premium-Tool des EPA in Betracht kommt.

## Methodisches Vorgehen — Default-Reihenfolge der Recherche

1. **Erste Triage** in Espacenet (Klasse + Anmelder) und Google Patents (semantisch).
2. **Vertiefung** in DEPATISnet (engere Klassenrecherche, IKOFAX) oder PATENTSCOPE (PCT-Search-Reports).
3. **Rechtsstand-Verifikation**:
   - DE-Patente: DPMAregister
   - EP-Patente: EPO Register plus nationale Register für die validierten Vertragsstaaten
   - US-Patente: USPTO Patent Center
   - JP/CN/KR/etc.: jeweiliges nationales Register, bei Bedarf über Espacenet-INPADOC-Hinweise quergeprüft
4. **Patentfamilien** über INPADOC (Espacenet) ziehen — niemals nur auf die Familiendefinition von Google Patents vertrauen für rechtliche Fragen.
5. **Citation-Maps** (Espacenet, Google Patents) für Backward-Citations (was zitiert das Dokument) und Forward-Citations (wer zitiert das Dokument).
6. **Recherchedokumentation** im Bericht: pro Datenbank — Suchstring(s), Datum, Trefferzahl, Auswahlkriterium.

## Was an dieser Stelle NICHT versprochen wird

- **Kein Volltext aller Welt-Patente**: Es gibt keine vollständige Volltext-Datenbank weltweit. Selbst Espacenet hat erhebliche Lücken bei älteren CN/JP/KR/RU-Dokumenten.
- **Keine vollständige Übersetzung**: Maschinelle Übersetzung (Patent Translate, Google Translate) ist hilfreich, aber nicht für rechtsverbindliche Aussagen geeignet. Für jede ernsthafte Entgegenhaltung in der Argumentation eines Bescheids muss die Übersetzungsqualität geprüft und ggf. ein menschlicher Übersetzer beauftragt werden.
- **Kein OCR-Garantierecht**: Ältere Patentschriften (vor ca. 1990) sind oft gescannt, nicht volltextlich. Volltext-Suche findet diese nicht zuverlässig.
- **Keine NPL-Vollständigkeit**: Nicht-Patent-Literatur (Fachartikel, Konferenzpapiere, Produkthandbücher, Open-Source-Code) ist über Patentdatenbanken nur partiell erschlossen. Für Software-Patente und chemische Synthesen ist eine zusätzliche Recherche in Scholar/Scopus/Web of Science/IEEE/ACM/Reaxys/SciFinder zwingend.

## Disclaimer

Diese Übersicht beschreibt die agentische Bedienung der genannten Datenbanken. Für rechtsverbindliche Recherchen (Nichtigkeitsklage, FTO-Gutachten für Investorenprüfung, Lizenzverhandlung) ist eine **menschliche** Patentanwältin oder ein menschlicher Patentanwalt einzubeziehen — die KI-Recherche ist Vorarbeit, keine Endabnahme.
