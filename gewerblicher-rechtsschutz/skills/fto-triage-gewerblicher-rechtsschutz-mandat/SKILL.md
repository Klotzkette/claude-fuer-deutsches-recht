---
name: fto-triage-gewerblicher-rechtsschutz-mandat
description: "Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und EP-Patente. Ergebnis Recherchepaket für Patentanwalt kein FTO-Gutachten. Output: Recherche-Bericht mit relevanten Patentfundstellen. Abgrenzung zu erfindungsmeldung-aufnahme (eigene Erfindung) und verletzungs-triage (fremde Schutzrechte) im Gewerblicher Rechtsschutz: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Freedom-to-Operate-Triage (FTO)

## Arbeitsbereich

Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und EP-Patente. Ergebnis Recherchepaket für Patentanwalt kein FTO-Gutachten. Output: Recherche-Bericht mit relevanten Patentfundstellen. Abgrenzung zu erfindungsmeldung-aufnahme (eigene Erfindung) und verletzungs-triage (fremde Schutzrechte). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
