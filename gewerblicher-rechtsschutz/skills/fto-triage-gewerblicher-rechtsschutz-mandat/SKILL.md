---
name: fto-triage-gewerblicher-rechtsschutz-mandat
description: "FTO Triage Gewerblicher Rechtsschutz Mandat: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# FTO Triage Gewerblicher Rechtsschutz Mandat

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **FTO Triage Gewerblicher Rechtsschutz Mandat** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fto-triage` | Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und EP-Patente. Ergebnis Recherchepaket für Patentanwalt kein FTO-Gutachten. Output: Recherche-Bericht mit relevanten Patentfundstellen. Abgrenzung zu erfindungsmeldung-aufnahme (eigene Erfindung) und verletzungs-triage (fremde Schutzrechte). |
| `gewerblicher-rechtsschutz-anpassen` | Anpassung und Konfiguration des Plugins gewerblicher-rechtsschutz: Mandatsprofil, Kanzleipräferenzen, Normenauswahl, Sprachstil und Outputformat an konkreten Bedarf anpassen. Skill für Kanzleien, die den Plugin-Rahmen ihrem Arbeitsalltag anpassen wollen. |
| `gewerblicher-rechtsschutz-mandat-arbeitsbereich` | Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats Mandantenkontext für alle Folge-Skills. Output: aktives Mandat gesetzt und bestätigte Kontexttrennung. Abgrenzung zu gewerblicher-rechtsschutz-kaltstart-interview (Kanzlei-Profil) und allen Sach-Skills. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **FTO Triage Gewerblicher Rechtsschutz Mandat**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fto-triage`

**Fokus:** Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und EP-Patente. Ergebnis Recherchepaket für Patentanwalt kein FTO-Gutachten. Output: Recherche-Bericht mit relevanten Patentfundstellen. Abgrenzung zu erfindungsmeldung-aufnahme (eigene Erfindung) und verletzungs-triage (fremde Schutzrechte).

# Freedom-to-Operate-Triage (FTO)

## Zweck

Erste Triage möglicher Patenthindernisse vor Markteinführung eines Produkts oder einer Technologie. Der Skill recherchiert relevante DE- und EP-Patente, bewertet ihre Relevanz für den konkreten Anwendungsfall und erstellt ein Recherchepaket für einen Patentanwalt. **Kein formelles FTO-Gutachten** – die abschließende rechtliche Einschätzung, ob ein Produkt in den Schutzbereich eines Patents fällt, erfordert einen zugelassenen Patentanwalt.

## Eingaben

- Produkt-/Technologiebeschreibung (so detailliert wie möglich: technische Merkmale, Funktionsweise, Materialien, Verfahren)
- Zielmarkt / Vertriebsgebiet (Deutschland, EU, weltweit)
- Schlüsselwörter / Technologieklassifikation (IPC/CPC-Klassen, falls bekannt)
- Geplantes Markteinführungsdatum
- Ggf. bereits bekannte Patente (Wettbewerber)
- Relevanter Stand der Technik (falls vorhanden)

## Ablauf

### 1. Technologie charakterisieren

Produktbeschreibung in technische Merkmale übersetzen:
- Hauptfunktion / Kernerfindung
- Unterscheidungsmerkmale gegenüber bekanntem Stand der Technik
- Schlüsselkomponenten und ihre Funktion
- Verfahrensschritte (bei Verfahrenspatenten)
- Mögliche IPC/CPC-Klassifikationen (International Patent Classification / Cooperative Patent Classification)

Vorschlag für Suchstrategie aus Merkmalen entwickeln. `[prüfen]` – Klassifikation und Merkmalsdefinition mit Fachmann abstimmen.

### 2. Patentrecherche durchführen

**Pflicht-Datenbanken:**

| Datenbank | URL | Umfang |
|---|---|---|
| Espacenet | worldwide.espacenet.com | Weltweite Patente; DE, EP, WO; Volltextsuche |
| DPMApaplus | depatisnet.dpma.de | Deutsche Patente und Gebrauchsmuster (DE); amtliche DPMA-Datenbank |
| Google Patents | patents.google.com | Ergänzende Suche; maschinelle Übersetzungen |

**Für EP-Patente mit DE-Wirkung:**
- EP-Patent nach Erteilung und Validierung in DE gültig → nationale Verletzungsklage vor deutschen Gerichten möglich (LG Düsseldorf, LG München I, LG Mannheim)
- Prüfung, ob nationales DE-Patent oder EP-Validierung vorliegt

**Suchstrategie:**

```
Schritt 1 – Keyword-Suche: Technologiebegriffe in Titel, Abstract, Ansprüchen
Schritt 2 – IPC/CPC-Klassensuche: Klassifikation + Keyword-Filter
Schritt 3 – Anmeldersuche: Bekannte Wettbewerber als Inhaber
Schritt 4 – Zitationsanalyse: Von gefundenen relevanten Patenten rückwärts zitieren
Schritt 5 – Familiensuche: Internationaler Schutzumfang von Kernpatenten
```

### 3. Gefundene Patente analysieren

Für jedes potenziell sperrende Patent:

**Formelle Prüfung:**
- Status: In Kraft / erloschen / nichtig / anhängig? (DPMA-Register, Espacenet Legal Status)
- Inhaberschaft: Wer ist aktueller Inhaber? Lizenzbereitschaft?
- Prioritätsdatum, Anmeldetag, Erteilungstag
- Ablaufdatum (max. 20 Jahre ab Anmeldetag, § 16 Abs. 1 PatG; ggf. SPC-Verlängerung in Pharma/Pflanzenschutz nach VO (EG) 469/2009)
- Jahresgebühren bezahlt? (DPMA-Register)

**Sachliche Prüfung (Triage-Ebene):**
- Anspruch 1 lesen (Hauptanspruch bestimmt Schutzbereich)
- Wesentliche Merkmale des Anspruchs identifizieren
- Abgleich mit Produktmerkmalen: Fallen alle Merkmale des Anspruchs in das Produkt?

**Relevanzbewertung:**

🔴 **Blocking:** Alle Merkmale des Anspruchs im Produkt vorhanden; Patent in Kraft; keine eindeutige Äquivalenzlücke; anwaltliche FTO-Analyse dringend erforderlich vor Markteinführung.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

🟡 **Mittel:** Einige Überschneidungen; erhebliche Merkmale nicht vorhanden; Design-around möglich; patentanwaltliche Prüfung empfohlen.

🟢 **Niedrig:** Nur entfernte Ähnlichkeit; Schutzbereich klar nicht getroffen; verbleibende Unsicherheiten für anwaltliche Einschätzung vermerken.

### 4. Lizenz- und Design-around-Optionen

Falls 🔴/🟠-Ergebnisse:
- **Lizenzierung:** Patentinhaber identifizieren; Lizenzbereitschaft einschätzen (FRAND-Verpflichtungen bei SEPs prüfen)
- **Design-around:** Welches Merkmal könnte technisch vermieden werden ohne Funktionsverlust?
- **Nichtigkeitsangriff:** Gibt es Stand der Technik, der Neuheit oder erfinderische Tätigkeit des Patents zerstört? (§ 21 Abs. 1 PatG; Nichtigkeitsklage vor BPatG)
- **Prioritätsrecherche:** Ältere Veröffentlichungen des Anmelders als potenziellen Stand der Technik prüfen

### 5. Recherchebericht erstellen

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Normen:** §§ 9, 14, 16, 21 PatG; § 14 GebrMG; VO (EG) 469/2009 (SPC-VO Pharma); Art. 64 EPÜ (nationale Wirkung EP-Patent).

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Kraßer/Ann, Patentrecht, 7. Aufl. 2016, § 33 Rn. 45 ff. (Schutzbereichsbestimmung). `[Modellwissen – prüfen; neuere Auflage verwenden falls verfügbar]`
- Schulte/Moufang, PatG, 10. Aufl. 2017, § 14 Rn. 95 ff. (Äquivalenzlehre).

## Ausgabeformat

**FTO-Triage-Bericht:**
1. Technologieprofil (Kurzfassung der geprüften Merkmale)
2. Rechercheparameter (Datenbanken, Klassen, Suchterms, Datum)
3. Ergebnistabelle (Patent-Nr., Inhaber, Titel, Status, Ablauf, Bewertung 🔴🟠🟡🟢)
4. Detailanalyse der 🔴/🟠-Treffer (Merkmalsabgleich, Begründung)
5. Handlungsoptionen (Lizenz, Design-around, Nichtigkeitsangriff)
6. Offene Fragen für Patentanwalt
7. Entscheidungsbaum

## Beispiel (Gutachtenstil – Auszug)

**Produkt:** Neue Fertigungsmethode für Halbleiterbauteile mit bestimmter Schichtabfolge

**Gefundenes Patent:** EP 3 456 789 B1, Inhaber: TechCorp SE, in Kraft (Jahresgebühren bezahlt bis 2028), Ablauf 2033.

**Anspruch 1 (vereinfacht):** Verfahren zur Herstellung eines Halbleiterbauteils, umfassend: (a) Aufbringen einer Siliziumschicht, (b) Dotierung mit Phosphor, (c) thermische Aushärtung bei 800–900 °C.

**Merkmalsabgleich:**

| Anspruchsmerkmal | Im Produkt vorhanden? | Anmerkung |
|---|---|---|
| (a) Siliziumschicht | Ja | identisch |
| (b) Phosphordotierung | Ja | identisch |
| (c) Thermische Aushärtung 800–900 °C | Fraglich | Produkt verwendet 850 °C – innerhalb des Bereichs `[prüfen]` |

**Ergebnis:** 🔴 **Blocking.** Alle Merkmale zumindest prima facie im Produkt vorhanden. Keine Äquivalenzlücke erkennbar. Patentanwaltliche FTO-Analyse vor Markteinführung zwingend erforderlich.

## Risiken / typische Fehler

- **Nur DE-Patente prüfen:** EP-Patente mit DE-Validierung haben volle nationale Wirkung; EPO-Datenbank ist Pflicht.
- **Status nicht prüfen:** Erloschene Patente (nicht bezahlte Jahresgebühren, Nichtigerklärung) sind kein Hindernis mehr; DPMA-Register auf aktuellen Status prüfen.
- **SPC-Verlängerungen übersehen:** In Pharma- und Pflanzenschutzbereich können Ergänzende Schutzzertifikate (SPC) die Schutzdauer um bis zu 5 Jahre verlängern.
- **Kein FTO-Gutachten:** Diese Triage ersetzt kein formelles FTO-Gutachten durch einen Patentanwalt; bei 🔴/🟠-Ergebnissen ist patentanwaltliche Einschaltung zwingend.
- **Äquivalenz ist Recht, nicht Technik:** Die Äquivalenzprüfung erfordert rechtliche Wertung (BGH "Pemetrexed"); nicht dem Ingenieur überlassen.
- **Geheimhaltung:** Technologiebeschreibungen sind vertraulich (§ 43a Abs. 2 BRAO; Geschäftsgeheimnis § 2 GeschGehG); nur intern und über gesicherte Kanäle verarbeiten.

## 2. `gewerblicher-rechtsschutz-anpassen`

**Fokus:** Anpassung und Konfiguration des Plugins gewerblicher-rechtsschutz: Mandatsprofil, Kanzleipräferenzen, Normenauswahl, Sprachstil und Outputformat an konkreten Bedarf anpassen. Skill für Kanzleien, die den Plugin-Rahmen ihrem Arbeitsalltag anpassen wollen.

# Gewerblicher Rechtsschutz: Plugin anpassen

## Zweck und Mandatsbezug

Dieser Skill ermöglicht die **Anpassung des Plugins `gewerblicher-rechtsschutz`** an das spezifische Mandatsprofil einer Kanzlei, eines Rechtsabteilungsleiters oder eines spezialisierten Beratungsunternehmens. Er steuert, welche Normen vorrangig geprüft werden, welcher Sprachstil verwendet wird, welche Gerichte und Behörden typischerweise relevant sind und welches Outputformat bevorzugt wird.

Mandatsbezug: Kanzlei mit Schwerpunkt Markenrecht nutzt das Plugin anders als ein Patentanwalt im Maschinenbaubereich. Rechtsabteilung eines Software-Unternehmens benötigt andere Standardabfragen als ein auf Abmahnungen spezialisierter Klagenanwalt.

## Konfigurationsdimensionen

### 1. Mandatsprofil und Rollenstruktur

Das Plugin kann auf verschiedene Nutzerrollen kalibriert werden:

| Rolle | Fokus | Typische Aufgaben |
|---|---|---|
| Fachanwalt GewRS | Vollständiges IP-Recht | Abmahnung, Klage, Vergleich, Beratung |
| Patentanwalt | PatG, DesignG, ArbnErfG | Anmeldung, FTO, EV, Lizenz |
| Rechtsabteilung Industrie | UWG, MarkenG, PatG | Compliance, Lizenz, Abwehr |
| Startup-Berater | MarkenG, UWG, UrhG | Anmeldung, Erstschutz, Abmahnung-Reaktion |
| Richter/Rechtspfleger | Alle Normen | Verfahrensrechtliche Fragen |

**Konfigurationsabfrage:** Welche Rolle ist primär? Wird das Plugin von einer einzelnen Person oder einem Team genutzt?

### 2. Normenprioritäten

Je nach Kanzleiprofil können unterschiedliche Normengruppen priorisiert werden:

- **Markenrecht:** MarkenG, CTMR (VO (EU) 2017/1001), Madrider System, WIPO-UDRP
- **Patentrecht:** PatG, EPÜ, PCT, GebrMG, ArbnErfG
- **Lauterkeitsrecht:** UWG, Richtlinie 2005/29/EG (UGP-RL), Richtlinie 2006/114/EG (Vergleichende Werbung)
- **Urheberrecht:** UrhG, InfoSoc-Richtlinie (2001/29/EG), DSM-Richtlinie (2019/790)
- **Designrecht:** DesignG, Gemeinschaftsgeschmacksmuster-VO (6/2002)
- **Prozessrecht:** ZPO (einstweiliger Rechtsschutz §§ 916 ff.), GKG (Streitwert)

**Konfigurationsabfrage:** Welche Normengruppen dominieren im Alltag?

### 3. Gerichtsstands- und Behördenpräferenzen

Das Plugin kann auf bestimmte Gerichte und Behörden ausgerichtet werden:

- **Patentgericht:** Bundespatentgericht München, EPA (Einspruch, Beschwerde)
- **Markengerichte:** DPMA, EUIPO, LG Hamburg/München/Frankfurt/Düsseldorf für EV
- **Zivilgerichte:** LG mit Spezialkammer GewRS; OLG
- **Behörden:** DPMA (Anmeldung, Widerspruch, Löschung), EUIPO

**Konfigurationsabfrage:** Welche Gerichte und Behörden sind im Arbeitsalltag am häufigsten relevant?

### 4. Sprachstil und Fachtonalität

| Stil | Einsatz |
|---|---|
| Juristisch-präzise (Gutachtenstil) | Schriftsätze, Memos für Anwälte |
| Mandantenfreundlich | Mandantenbriefe, Erstgespräche |
| Tabellarisch-komprimiert | Interne Arbeitsmaterialien |
| Bilinguale Ausgabe (DE/EN) | Internationale Mandate |

**Konfigurationsabfrage:** In welchem Sprachstil sollen Outputs standardmäßig erzeugt werden?

### 5. Outputformat-Präferenzen

- **Memo:** Kurzgutachten, 1–3 Seiten, Ergebnis zuerst.
- **Checkliste:** Strukturierter Prüfpfad mit Abhakpunkten.
- **Schriftsatz-Entwurf:** Vollständiger Klage-, Antrags- oder Briefentwurf.
- **Tabelle/Matrix:** Normen × Tatbestandsmerkmale × Tatsachen.
- **Fristenplan:** Chronologischer Überblick mit Verantwortlichkeiten.
- **Red-Team:** Gegenargumente und Schwachstellenanalyse.

**Konfigurationsabfrage:** Welches Outputformat ist Standard, welches Ausnahme?

## Kaltstart-Konfigurationsgespräch

Zu Beginn eines neuen Kanzleiprofils:

1. **Kanzlei/Organisation:** Name, Größe, Standort, Fachgebiet-Schwerpunkte.
2. **Typisches Mandat:** Abmahner oder Abgemahnter? Anmelder oder Verletzer? International oder national?
3. **Normen-Ranking:** Welche drei Normengruppen kommen täglich vor?
4. **Bevorzugte Gerichte:** Welche LG/OLG/BGH-Kammern werden regelmäßig bespielt?
5. **Output-Präferenz:** Schriftsatz, Checkliste, Tabelle oder Kurzgutachten?
6. **Sprache:** Deutsch, Englisch oder bilingual?

## Anpassungsworkflow

### Schritt 1 – Profil dokumentieren

Aus dem Kaltstart-Gespräch ein kurzes Kanzleiprofil erzeugen:
```
Kanzleiprofil:
- Schwerpunkt: [Marken/Patent/UWG/Urheberrecht]
- Typische Mandantenrolle: [Antragsteller/Antragsgegner/Anmelder/Lizenznehmer]
- Primäre Gerichte: [LG …, OLG …, BGH]
- Normen-Priorität: [MarkenG, UWG, ZPO §§ 916 ff.]
- Outputformat-Standard: [Memo/Checkliste/Schriftsatz]
- Sprache: [Deutsch/Englisch]
```

### Schritt 2 – Skills-Routing anpassen

Basierend auf Profil empfehlen, welche Fachmodule bevorzugt genutzt werden sollten:
- Marken-Schwerpunkt → `markenrecherche`, `markenanmeldung-dpma`, `unterlassungsverlangen`
- Patent-Schwerpunkt → `fto-triage`, `erfindungsmeldung-aufnahme`, `schutzrechts-portfolio`
- UWG-Schwerpunkt → `gewr-uwg-abmahnung-checkliste`, `verletzungs-triage`
- EV-Schwerpunkt → `evvollzug-neu-001` bis `evvollzug-neu-008`

### Schritt 3 – Dauereinstellungen festhalten

- Häufig genutzte Streitwert-Tabellen: z.B. OLG Hamburg Streitwertpraxis.
- Regelmäßige Fristen: DPMA-Widerspruchsfrist 3 Monate, Neuheitsfrist PatG, EUIPO-Fristen.
- Vorlagen-Bibliothek: Welche Schriftsatz-Vorlagen wurden bereits angepasst?

## Qualitätssicherung nach Anpassung

- Nach Profilkonfiguration: Testfall mit einem typischen Mandat durchführen.
- Prüfen: Stimmen Normenreferenzen, Gerichtsstand, Outputformat?
- Anpassen: Falls Output nicht passt, Profil verfeinern.
- Periodisch: Plugin bei Gesetzesänderungen (z.B. neue UWG-Novelle, MarkenG-Reform) aktualisieren.

## Quellenregel

- Normänderungen über [gesetze-im-internet.de](https://www.gesetze-im-internet.de) live prüfen.
- DPMA-Praxis über [dpma.de](https://www.dpma.de) aktuell halten.
- EUIPO-Richtlinien über [euipo.europa.eu](https://www.euipo.europa.eu) nachverfolgen.
- Keine BeckRS-Blindzitate; bei spezifischen Gerichtspraxisfragen: Live-Check.

## Anschluss-Skills

- `workflow-kaltstart-und-routing` – Erstgesprächs-Router
- `mandat-triage-gewerblicher-rechtsschutz` – Mandatstriage
- `allgemein` – Plugin-Übersicht
- `gewerblicher-rechtsschutz-kaltstart-interview` – Kaltstart-Interview für neues Mandat

## 3. `gewerblicher-rechtsschutz-mandat-arbeitsbereich`

**Fokus:** Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats Mandantenkontext für alle Folge-Skills. Output: aktives Mandat gesetzt und bestätigte Kontexttrennung. Abgrenzung zu gewerblicher-rechtsschutz-kaltstart-interview (Kanzlei-Profil) und allen Sach-Skills.

# Mandatsarbeitsbereich

## Zweck

Anwälte und Patentanwälte arbeiten gleichzeitig an mehreren Mandaten. Ein Mandatsarbeitsbereich hält den Kontext eines Mandanten oder einer Angelegenheit von jedem anderen getrennt. Diese Skill verwaltet diese Bereiche.

Der Standardzustand ist **deaktiviert**. Syndikusrechtsanwälte und Inhouse-Teams (ein Mandant) arbeiten auf Praxisebene; Mandatsarbeitsbereiche sind für sie unsichtbar. Sie aktivieren sich beim Erstkonfigurationsgespräch für externe Anwälte (Einzel-, Klein- und Großkanzleien) oder durch manuelle Einrichtung.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

Befehlsargument (erstes Token):

- `neu <kurzzeichen>` — neuen Mandatsarbeitsbereich anlegen
- `liste` — alle Mandate mit Status und aktivem Mandat anzeigen
- `wechseln <kurzzeichen>` — aktives Mandat umstellen
- `schliessen <kurzzeichen>` — Mandat archivieren
- `kein` — von jedem Mandat trennen, auf Praxisebene arbeiten

## Rechtlicher Rahmen

### Berufsrechtliche Rahmenbedingungen

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht des Rechtsanwalts; Mandatsgeheimnis; Grundlage der Mandatskontexttrennung
- **§ 43a Abs. 4 BRAO** — Verbot der Vertretung widerstreitender Interessen (Interessenkonflikt); Mandate müssen getrennt geführt werden
- **§ 203 Abs. 1 Nr. 3 StGB** — Verletzung von Privatgeheimnissen durch Rechtsanwälte; strafrechtliche Absicherung der Vertraulichkeit
- **§ 50 BRAO** — Aufbewahrungspflichten für Handakten (mind. 5 Jahre); Archivierung schließt Mandatsarbeitsbereiche nicht; Löschung ist ausgeschlossen
- **§ 2 BORA** — Berufsrechtliche Pflichten; Grundsatz der anwaltlichen Unabhängigkeit

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Feuerich/Weyland/Böhnlein, BRAO, 10. Aufl. 2022, § 50 Rn. 1 ff. (Handaktenaufbewahrung)

## Ablauf

### Schritt 1: Vorbedingung prüfen

Praxiskonfigurationsdatei lesen. Falls `Mandatsarbeitsbereiche: ✗` (Standardeinstellung für Inhouse-Teams):

> Mandatsarbeitsbereiche sind deaktiviert — Sie sind als Inhouse-Praxis mit einem Mandanten konfiguriert; das Plugin arbeitet automatisch auf Praxisebene. Wenn Sie tatsächlich über mehrere externe Mandate hinweg arbeiten, führen Sie das Erstkonfigurationsgespräch erneut aus und wählen Sie die Kanzlei-Einstellung. Andernfalls benötigen Sie `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich` nicht.

Kein Fehler — der deaktivierte Zustand ist der erwartete für Inhouse-Nutzer.

### Schritt 2: Befehlsverarbeitung

Auf das erste Token des Arguments dispatchen.

---

#### Befehl `neu <kurzzeichen>`

1. Prüfen, ob das Kurzzeichen nicht bereits in `mandate/<kurzzeichen>/` oder `mandate/_archiv/<kurzzeichen>/` vorhanden ist. Bei Kollision: anderen Namen wählen lassen.
2. Aufnahmeinterview durchführen (in einem Durchgang):
 - **Mandant** — vertretene Partei oder interne Geschäftseinheit
 - **Gegenpartei** — andere Seite (kann mehrere umfassen; kann "unbekannter Drittverletzer" bei Watch-Treffern sein)
 - **Mandatstyp** — für gewerblichen Rechtsschutz: Markenschutz / Markenverletzung / Schutzrechtsübertragung / Patentverletzung / FTO-Gutachten / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges
 - **Vertraulichkeitsstufe** — standard | erhöht | Clean-Team (erhöht bei besonderer Sensibilität, Clean-Team häufig bei FTO-Gutachten und Patentkäufen)
 - **Wesentliche Tatsachen** — 2–5 Sätze: Worum geht es, wer sind die Beteiligten, was steht auf dem Spiel
 - **Mandatsspezifische Abweichungen von der Standardposition** (z. B. "Mandant wünscht nur schriftliche Kommunikation", "Gegenpartei ist Geschäftspartner — maßvoller Ton")
 - **Verbundene Mandate** — Kurzzeichen zusammenhängender Mandate
3. `mandate/<kurzzeichen>/mandat.md` mit der unten angegebenen Vorlage schreiben.
4. `mandate/<kurzzeichen>/verlauf.md` mit einem einzigen Eröffnungseintrag anlegen.
5. Leere `mandate/<kurzzeichen>/notizen.md` anlegen.
6. **Nicht** automatisch zum neuen Mandat wechseln. Fragen: "Möchten Sie jetzt zu `<kurzzeichen>` wechseln?"

---

#### Befehl `liste`

`mandate/*/mandat.md` aufzählen. Aus jeder Datei Status und Kurzzeichen entnehmen. Tabelle ausgeben:

| Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. `_archiv/*` unter gesonderter Überschrift "Archivierte Mandate" anführen.

---

#### Befehl `wechseln <kurzzeichen>`

1. Prüfen, ob `mandate/<kurzzeichen>/mandat.md` vorhanden. Falls nicht: `neu <kurzzeichen>` anbieten.
2. `Aktives Mandat:`-Zeile in der Praxiskonfigurationsdatei auf `<kurzzeichen>` aktualisieren.
3. Dem Nutzer die mandat.md-Zusammenfassung zeigen, damit er das richtige Mandat bestätigen kann.

---

#### Befehl `schliessen <kurzzeichen>`

1. `mandate/<kurzzeichen>/` auf Existenz prüfen.
2. "Geschlossen"-Eintrag mit aktuellem Datum an `mandate/<kurzzeichen>/verlauf.md` anhängen.
3. `mandate/<kurzzeichen>/` nach `mandate/_archiv/<kurzzeichen>/` verschieben.
4. War das geschlossene Mandat das aktive Mandat: `Aktives Mandat:` auf `kein — nur Praxisebene` setzen.

---

#### Befehl `kein`

`Aktives Mandat:` in der Praxiskonfigurationsdatei auf `kein — nur Praxisebene` setzen. Bestätigung an den Nutzer.

## Ausgabeformat

### Vorlage `mandat.md`

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Mandatsprofil]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Kurzzeichen:** [kurzzeichen]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / Clean-Team]

---

## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Mandatstyp

[Markenschutz / Markenverletzung / FTO-Gutachten / Patentverletzung / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges — mit einzeiliger Begründung]

## Wesentliche Tatsachen

[2–5 Sätze. Worum geht es. Wer sind die Beteiligten. Was steht auf dem Spiel. Was macht dieses Mandat vom Standard abweichend.]

## Mandatsspezifische Abweichungen

*Jede Abweichung von der Praxisstandposition, die nur für dieses Mandat gilt.*

- [z. B. "Durchsetzungsstrategie: hier maßvoll, obwohl Hausstandard aggressiv — Gegenpartei ist wichtiger Handelspartner."]
- [z. B. "Genehmigung für Abmahnungen: zusätzliche Freigabe durch Mandant erforderlich."]
- [z. B. "Clean-Team: Mandatsakten auch bei aktiviertem mandatsübergreifendem Kontext nicht lesbar."]

## Verbundene Mandate

- [kurzzeichen — einzeilige Begründung]

## Vertraulichkeitshinweise

[Bei erhöhter oder Clean-Team-Stufe: warum. Wer darf die Mandatsakten einsehen. Ob mandatsübergreifender Kontext zulässig ist.]
```

### Vorlage `verlauf.md`

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Kurzzeichen: `[kurzzeichen]`. Status: aktiv.
[Ggf. initialer Kontext — z. B. "Eröffnet nach Watch-Treffer auf `APEXLEAF` in Klasse 25."]
```

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich neu bmw-marke-2026`

**Verarbeitung:**
Kurzzeichen prüfen → Aufnahmeinterview starten → `mandat.md` erstellen → `verlauf.md` mit Eröffnungseintrag anlegen → Nutzer fragen, ob zum neuen Mandat gewechselt werden soll.

**Ausgabe (Auszug):**

> Mandatsarbeitsbereich `bmw-marke-2026` angelegt.
>
> | Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet |
> |---|---|---|---|---|
> | bmw-marke-2026 | BMW AG | Markenschutz | aktiv | 2025-07-15 |
>
> Möchten Sie jetzt zu `bmw-marke-2026` wechseln?

## Risiken und typische Fehler

- **Interessenkonflikte nicht erkennen:** Diese Skill führt keine Interessenkonfliktprüfung durch — das ist Aufgabe des Anwalts und der Kanzlei. Die Aufnahme erfasst nur, was der Nutzer angibt.
- **Archivierung ist keine Löschung:** Geschlossene Mandate bleiben lesbar (§ 50 BRAO — Aufbewahrungspflicht mindestens 5 Jahre). Retention-Policy ist außerhalb des Skill-Umfangs.
- **Mandatsübergreifender Kontext standardmäßig aus:** Die Praxiskonfiguration hat ein `Mandatsübergreifender Kontext:`-Flag. Standardmäßig `aus` — Skill A im Mandat X liest niemals Dateien aus Mandat Y. Das ist die Vertraulichkeitsgarantie.
- **Kurzzeichen-Kollision mit Archiv:** Wird ein Kurzzeichen wiederverwendet, das im Archiv liegt, wird das archivierte Mandat unter `_archiv/<kurzzeichen>/` bewahrt; das neue erhält einen anderen Namen.

## Quellenpflicht

Alle Aussagen zu Vertraulichkeit, Aufbewahrung und Interessenkonflikten müssen auf konkreten Normen beruhen:

- **§ 43a BRAO** (Verschwiegenheit), **§ 43a Abs. 4 BRAO** (widerstreitende Interessen), **§ 203 StGB** (Verletzung von Privatgeheimnissen), **§ 50 BRAO** (Handaktenaufbewahrung)
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen bei Mandatseröffnung

Bevor das Mandat angelegt wird, klaere:
1. Ist ein Interessenkonflikt-Check (§ 43a IV BRAO) durchgefuehrt worden?
2. Sind die wesentlichen Mandatsdaten vollstaendig (Mandant, Gegner, Rechtsgebiet, Streitgegenstand)?
3. Wurde der Mandant ueber Honorar und Kostenrisiko aufgeklaert (§ 49b BRAO, § 34 RVG)?
4. Laeuft bereits eine Frist (z.B. Widerspruchsfrist Marke, Abmahnungsfrist), die sofort ins Fristenbuch muss?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Korrektur: Zitat aus "Aktuelle Rechtsprechung"-Block entfernt (bei Zweifel loeschen).
-->
