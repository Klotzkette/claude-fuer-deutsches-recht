---
name: mieteranfragen-bearbeitung-projekt
description: "Mieteranfragen Bearbeitung Projekt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mieteranfragen Bearbeitung Projekt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mieteranfragen Bearbeitung Projekt** im Plugin Immobilienrechtspraxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mieteranfragen-bearbeitung` | Mieteranfragen im Immobilienportfolio bearbeiten: Mängel, Betriebskosten, Belegeinsicht, Kündigung, Mieterhöhung und Mietpreisbremse; mit Fristen, Zuständigkeit, Antwortentwurf, Aktenvermerk und Anschluss an die Betriebskosten-/WEG-Datenpaket-Skills. |
| `projekt-arbeitsweise` | Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan Immobilienrechtsmandat. Abgrenzung: nicht Einzelverfahren. |
| `sachverhaltsermittlung` | Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog. Output: Sachverhalts-Ermittlungsbericht. Abgrenzung: nicht rechtliche Bewertung. |

## Arbeitsweg

Im Plugin Immobilienrechtspraxis gilt für **Mieteranfragen Bearbeitung Projekt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mieteranfragen-bearbeitung`

**Fokus:** Mieteranfragen im Immobilienportfolio bearbeiten: Mängel, Betriebskosten, Belegeinsicht, Kündigung, Mieterhöhung und Mietpreisbremse; mit Fristen, Zuständigkeit, Antwortentwurf, Aktenvermerk und Anschluss an die Betriebskosten-/WEG-Datenpaket-Skills.

# Mieteranfragen Bearbeitung

## Fachkern: Mieteranfragen Bearbeitung
- **Spezialgegenstand:** Mieteranfragen Bearbeitung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Wiederkehrende Mieteranfragen werden in der Praxis manuell beantwortet,
obwohl die Antworten in 80 Prozent der Fälle musterhaft sind. Der Skill
klassifiziert, wählt das passende Muster, befüllt es mit den konkreten
Sachverhaltselementen und ergänzt aktuelle BGH-Rechtsprechung.

## Inputs

- Mieterschreiben (.pdf .docx Email-Export)
- Mietvertrag und gegebenenfalls Nachtraege
- Optional: Hausverwaltungs-Stellungnahme
- Briefkopf-Vorlage der Abteilung

## Klassifikationskategorien

- Mietmängelanzeige und Mietminderungsforderung §§ 536 ff. BGB
- Kündigung ordentlich § 573 BGB und außerordentlich § 543 BGB
- Eigenbedarfskündigung § 573 Abs. 2 Nr. 2 BGB
- Mieterhöhung nach § 558 BGB ortsübliche Vergleichsmiete
- Mieterhöhung nach § 559 BGB Modernisierung
- Widerspruch nach § 574 BGB Härteklausel
- Betriebskostenabrechnung — Prüfung Einwendungen § 556 Abs. 3 BGB
- Belegeinsicht Betriebskosten — Rechnungen, Verträge, Zahlungsbelege, Originale/Scans
- CO2-Kostenaufteilung — Mieter-/Vermieteranteil nach CO2KostAufG
- Untervermietung § 553 BGB
- Mietkautionsrückforderung § 551 BGB
- Schönheitsreparaturen und Endrenovierung
- Mietpreisbremse §§ 556d ff. BGB Auskunftsverlangen § 556g Abs. 3 BGB

## Methodik

1. Schreiben klassifizieren (Mehrfachkategorien möglich)
2. Sachverhalt verdichten (mittels Skill `sachverhaltsermittlung` oder
 direkt)
3. Musterantwort auswählen, Platzhalter befuellen
4. Rechtsprechung nur anhängen, wenn sie vor Ausgabe frei oder amtlich
 geprüft wurde; Datum und Aktenzeichen sind Pflicht
5. Argumentationslinie zweistufig: erst Rechtslage, dann konkrete
 Subsumtion
6. Aktenvermerk für interne Akte mit Kurzbegründung der gewählten
 Linie

## Output

- `Antwort_<Mieter>_<Datum>.docx` auf Briefkopf
- `Aktenvermerk_<Aktenzeichen>.md` — kurz und klar für die Akte

## Pinpoint-Zitierregel

BGH zitiert mit Datum Aktenzeichen Fundstelle Randnummer. Beispiel:
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rn. 17. Juengere Entscheidungen stehen oben.

## Anti-Risiko-Hinweis

Bei folgenden Konstellationen erzeugt der Skill nur einen Entwurf MIT
Warnsiegel, weil Einzelfallbewertung zwingend ist:

- Kündigung wegen Pflichtverletzung mit unklarer Beweislage
- Eigenbedarf mit Härteeinrede § 574 BGB
- Mietminderung mit Schimmel und Streit über Ursache
- Mietpreisbremse mit Bestandsschutz-Fragen
- Gewerbemiete mit Schriftform-Risiko § 550 BGB
- Betriebskosten mit verweigerter Belegeinsicht, Zahlungsbelegen oder WEG-Datenlücken

## Beispielformulierungen

- "Mieter ruegt Schimmel im Bad und mindert um 20 Prozent. Entwirf
 Antwort und Aktenvermerk."
- "Mieter widerspricht Kündigung mit Härte nach § 574 BGB. Welche
 Linie schlagen wir vor?"
- "Mietkautionsrückforderung mit Abrechnung anbei. Prüfe und
 antworte."
- "Mieter verlangt Zahlungsbelege zur Betriebskostenabrechnung 2025. Erstelle Antwort und Belegeinsichtsplan."
- "WEG-Verwalterabrechnung liegt vor; welche Positionen dürfen in die Mieterabrechnung?"

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Schimmel/Mangel: §§ 536, 536a BGB, § 538 BGB
- Kuendigung/Widerspruch: §§ 543, 573, 574 ff. BGB
- Kaution: § 551 BGB
- Mietpreisbremse: §§ 556d ff. BGB
- Betriebskosten: § 556 Abs. 3 BGB, BetrKV
- Betriebskosten-Schlüssel: § 556a BGB
- Heizkosten: HeizkostenV
- CO2-Kosten: CO2KostAufG

## Anschluss-Skills Betriebskosten

- `betriebskostenabrechnung-erstellen-asset-management`
- `betriebskostenabrechnung-pruefen-asset-management`
- `weg-abrechnung-mieterschnittstelle-datenpaket`

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `projekt-arbeitsweise`

**Fokus:** Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan Immobilienrechtsmandat. Abgrenzung: nicht Einzelverfahren.

# Projekt-Arbeitsweise Immobilienrecht

## Fachkern: Projekt-Arbeitsweise Immobilienrecht
- **Spezialgegenstand:** Projekt-Arbeitsweise Immobilienrecht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Freihaendiges Prompting funktioniert für einzelne Aufgaben aber
nicht für dauerhafte Mandate. Eine immobilienrechtliche
Rechtsabteilung arbeitet projektbezogen — pro Objekt pro
Transaktion pro Mietverhältnis. Der Skill legt Projekt-Skelette
an und fixiert die Vorgaben so dass eingehende Dokumente immer
gegen denselben Maßstab geprüft werden.

## Inputs

- Projekt-Bezeichnung (Objekt Aktenzeichen Transaktion)
- Optional: hauseigenes Playbook Musterverträge Klauselkatalog
- Optional: AVV-Anforderungen der Abteilung
- Optional: Compliance-Vorgaben (zB Geldwäschegesetz
 Sanktionslisten)

## Projekt-Skelett

```
<Projekt>/
 00_Projekt-Setup/
 vorgaben.md
 playbook.md
 musterklauseln.md
 avv-anforderungen.md
 zitierregeln.md
 01_Verträge/
 02_Korrespondenz/
 03_Schriftsätze/
 04_Recherche/
 05_Mandantenkontakt/
 06_Ablage/
 audit.md
```

`vorgaben.md` ist die zentrale Konfiguration. Sie nennt:

- Rechtsgebiet und Schwerpunkte
- Welche Skills bei welchem Dokumenttyp auslösen
- Welches Playbook gilt
- Welche Musterverträge als Referenz dienen
- Welche AVV-Anforderungen zwingend sind
- Welche Zitierregeln gelten

## AVV-Prüfung nach Art. 28 DSGVO

Eingehende AVV oder AV-Verträge werden gegen den Mindestkatalog
nach Art. 28 Abs. 3 DSGVO geprüft:

- Gegenstand und Dauer der Verarbeitung
- Art und Zweck der Verarbeitung
- Art der personenbezogenen Daten
- Kategorien betroffener Personen
- Pflichten und Rechte des Verantwortlichen
- Weisungsgebundenheit
- Vertraulichkeit
- Sicherheit der Verarbeitung Art. 32 DSGVO
- Unterauftragsverarbeiter
- Unterstützung bei Betroffenenrechten Art. 12-22 DSGVO
- Unterstützung bei Meldepflichten Art. 33 und 34 DSGVO
- Löschung oder Rückgabe nach Vertragsende
- Nachweise und Audit-Rechte

Ausgabe: Ampelmatrix mit Hinweis welche Pflichtangabe fehlt oder
abweicht.

## Interne Compliance-Vorgaben

Falls in `vorgaben.md` hinterlegt werden zusätzlich geprüft:

- Sanktionslisten und Embargo-Vorgaben
- Geldwäschegesetz — Kenntnis des wirtschaftlich Berechtigten bei
 Immobilien-Transaktionen § 3 GwG
- Mindest-Vertragsstrafen bei Geheimhaltungsverletzung
- Maximal akzeptierte Indexierungs-Schwellen bei
 Gewerbemietverträgen
- Schriftform-Mindestanforderungen Gewerbemiete § 550 BGB

## Auto-Routing

Der Skill ordnet eingehende Dokumente auf Basis von
Dateiname und Inhalt einem Unterordner zu. Auslöser-Regeln aus
`vorgaben.md`:

- Verträge mit Begriffen Mietvertrag Kaufvertrag in
 `01_Verträge/`
- Schreiben Email-Exports in `02_Korrespondenz/`
- Schriftsätze mit Begriffen Klage Erwiderung Berufung in
 `03_Schriftsätze/`

Pro eingehendem Dokument wird ein Eintrag in `audit.md` gesetzt:
Zeitpunkt Quelle Empfänger angewandte Pruefskills Ergebnis.

## Integration mit anderen Skills

Der Skill ist Hub für die anderen Skills des Plugins:

- Eingehender Vertrag → `vertragspruefung-playbook`
- Eingehende Mandanten-Korrespondenz mit Mängelanzeige →
 `mieteranfragen-bearbeitung`
- Grundbuch-PDFs → `grundbuchanalyse`
- Fragmentarische Sachverhalts-Unterlagen →
 `sachverhaltsermittlung`
- Komplette Mandats-Erstaufbereitung → `memorandums-ersteller`
 (separates Plugin)

## Agenten-Workflows

Der Skill ist so gebaut dass ein Agent auf einen Watch-Ordner
reagieren kann. Sobald ein PDF in `00_Inbox/` landet wird auf
Basis der `vorgaben.md` automatisch der passende Skill gestartet
und das Ergebnis in den richtigen Unterordner geschrieben.

## Nachvollziehbarkeit und Audit

Jede Änderung an `vorgaben.md` ist versioniert. Jede
Skill-Ausführung steht in `audit.md` mit Eingabe-Datei und
Ergebnis-Datei. Bei Prüfung durch Aufsicht oder Geschäftsleitung
ist nachvollziehbar wer wann mit welchen Vorgaben geprüft hat.

## Output beim Setup

- Projekt-Verzeichnisbaum
- `vorgaben.md` ausgefüllt mit den getroffenen Festlegungen
- `audit.md` mit Eintrag Setup
- Optional Vorlage-Dateien aus `00_Projekt-Setup/` befüllt

## Beispielformulierungen

- "Lege ein Projekt für das Bürogebäude Friedrichstraße 100
 an. Playbook Gewerbemiete Standard. AVV-Prüfung Pflicht."
- "Prüfe diesen eingehenden AVV nach Art. 28 DSGVO und unsere
 internen Vorgaben."
- "Routinge die letzten 30 eingehenden Mails in die richtigen
 Projekt-Ordner."
- "Erzeuge audit.md für den Quartalsbericht — welche Skills
 wurden im Projekt Erbpacht Tegel zwischen Januar und März
 angewandt?"

## Aktuelle Rechtsprechung — Projekt-relevante Normen



## Paragrafenkette Projekt-Setup

- Mandatsdokumentation: BRAO § 43, BORA § 1 ff.
- Datenschutz: Art. 6 DSGVO, Art. 28 DSGVO (AVV)
- GwG-Dokumentation: §§ 10 ff. GwG
- Aufbewahrungspflicht: § 50 StBerG analog, Steuerrecht 10 Jahre

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `sachverhaltsermittlung`

**Fokus:** Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog. Output: Sachverhalts-Ermittlungsbericht. Abgrenzung: nicht rechtliche Bewertung.

# Sachverhaltsermittlung

## Fachkern: Sachverhaltsermittlung
- **Spezialgegenstand:** Sachverhaltsermittlung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Der Engpass in Inhouse-Arbeit ist selten die rechtliche Bewertung. Es
ist die saubere Erfassung des Sachverhalts. Asset-Management und
Hausverwaltung liefern selten freiwillig den vollen Sachverhalt. Der
Skill fragt strukturiert ab und liefert dem Juristen ein konsolidiertes
Memo, das wirklich verwertbar ist.

## Inputs

- Eingangskorrespondenz (Mieterschreiben Anwaltsschreiben Email)
- Vorhandene Unterlagen (Vertrag Übergabeprotokoll Mahnungen
 Hausverwaltungsberichte)
- Optional: interne Kommentare aus der Akte

## Methodik in vier Stufen

### Stufe 1 — Extraktion aus Unterlagen

Aus jedem vorhandenen Dokument werden Datum Akteure Ereignisse und
behauptete Mängel extrahiert. Ergebnis ist eine erste rohe
Zeitleiste.

### Stufe 2 — Gezielter Fragenkatalog

Der Skill erzeugt einen Fragenkatalog für Asset-Management bzw.
Hausverwaltung. Fragen sind kurz, geschlossen wo möglich, jeweils
mit Begründung warum die Frage relevant ist (zB "Wann erfolgte
Mangelanzeige formell? Relevant für Beginn Minderungsrecht
§ 536 BGB").

### Stufe 3 — Zeitleisten-Rekonstruktion

Antworten werden in die Zeitleiste integriert. Konflikte zwischen
Aussagen werden markiert.

### Stufe 4 — Beweis und Lücken

Pro Tatsachenbehauptung wird vermerkt: durch welches Beweismittel
gesichert (Urkunde Zeuge Augenschein), bloss plausibel oder offen.

## Output

- `SV_Memo_<Aktenzeichen>.md` mit Abschnitten:
 - Gesicherter Sachverhalt
 - Plausible Annahmen mit Quelle
 - Offene Punkte mit Fragestellung
 - Zeitleiste in Tabellenform
 - Beweisübersicht
- `Fragenkatalog_<Adressat>.docx` — versendungsfertig an
 Asset-Management oder Hausverwaltung

## Anti-Halluzinations-Regel

Der Skill erfindet KEINE Sachverhaltsdetails. Wo eine Information
fehlt, steht "OFFEN" mit konkreter Frage. Inhouse-Juristen verlieren
sonst das Vertrauen — und das ist der teuerste Verlust.

## Typische Fallkonstellationen

- Mietmängel — wann angezeigt, wann besichtigt, welcher Mietzins,
 welche Minderungsquote behauptet
- Kündigung — Form, Zugang, Begründung, Widerspruch nach
 § 574 BGB
- Eigenbedarf — Bedarfsperson Verwandtschaftsgrad konkrete
 Nutzungsabsicht
- Betriebskostenabrechnung — Abrechnungszeitraum Zugang § 556
 Abs. 3 BGB Frist Einwendungen
- Schönheitsreparaturen Endrenovierung — Vertragsklausel
 Zeitpunkt der Vertragsbegründung Renovierungszustand bei
 Einzug
- Bauschäden — Erstanzeige Sachverständiger Beweissicherung

## Beispielformulierungen

- "Mieterschreiben mit Mietmängelanzeige liegt vor. Erstelle
 Sachverhalts-Memo und Fragenkatalog an Hausverwaltung."
- "Kündigungsstreit gegen Mieter Schmitt. Antworten der
 Hausverwaltung anbei. Konsolidiere zum Memo."
- "Ich habe nur eine halbe Akte. Welche Fragen muss ich stellen,
 bevor ich rechtlich prüfe?"

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Mangelanzeige/Mietminderung: §§ 536, 536a, 543 BGB
- Kuendigung: §§ 543, 569, 573 BGB
- Betriebskosten: § 556 Abs. 3 BGB, BetrKV

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
