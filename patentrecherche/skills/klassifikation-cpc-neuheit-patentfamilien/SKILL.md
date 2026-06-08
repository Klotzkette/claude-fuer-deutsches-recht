---
name: klassifikation-cpc-neuheit-patentfamilien
description: "CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche muessen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC (Cooperative Patent Classification EPA/USPTO). Prüfraster: Technikgebiet aus Beschreibung extrahieren, Hauptklassen und Nebenklassen, CPC feiner als IPC, Verifikation per WIPO-IPC-Online und Espacenet-Classification-Browser. Output Klassifikations-Empfehlung mit Begründung je Klasse. Abgrenzung: Eigentliche Recherche siehe agentische-datenbank-recherche, stand-der-technik-recherche; FTO siehe freedom-to-operate-recherche im Patentrecherche: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# klassifikation-cpc-ipc

## Arbeitsbereich

CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche muessen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC (Cooperative Patent Classification EPA/USPTO). Prüfraster: Technikgebiet aus Beschreibung extrahieren, Hauptklassen und Nebenklassen, CPC feiner als IPC, Verifikation per WIPO-IPC-Online und Espacenet-Classification-Browser. Output Klassifikations-Empfehlung mit Begründung je Klasse. Abgrenzung: Eigentliche Recherche siehe agentische-datenbank-recherche, stand-der-technik-recherche; FTO siehe freedom-to-operate-recherche. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Damit die anschließende Datenbankrecherche zielgenau läuft, müssen die richtigen **Klassen** bestimmt werden. Eine schlecht gewählte Klasse erzeugt entweder Trefferchaos oder verfehlt einschlägige Treffer komplett.

## Grundlagen

- **CPC** — Cooperative Patent Classification, gemeinsame Klassifikation von EPA und USPTO. Etwa 250.000 Untergruppen, etwa zehnmal feiner als IPC. Verwendet ab 2013, abgelöst hat sie die alte ECLA und die alte USPC.
- **IPC** — International Patent Classification, WIPO-Klassifikation. Etwa 70.000 Untergruppen. Wird global an Patentschriften angebracht, auch von Ämtern, die keine CPC vergeben.
- Eine Anmeldung trägt typischerweise mehrere CPC- und mehrere IPC-Symbole — eine **Hauptklasse** und mehrere **Nebenklassen**.

## Klassen-Schema (Hauptsektionen)

| Sektion | Inhalt |
| --- | --- |
| A | Täglicher Lebensbedarf (Landwirtschaft, Lebensmittel, Bekleidung, Medizinprodukte, Sport) |
| B | Arbeitsverfahren, Transport (Mechanik, Trennen, Mischen, Formen, Drucken, Transport, Verpacken, Mikro/Nano) |
| C | Chemie, Hüttenwesen (anorganische und organische Chemie, Polymere, Metallurgie, Werkstoffe) |
| D | Textilien, Papier |
| E | Bauwesen (Hochbau, Erdarbeiten, Wasserbau, Bergbau) |
| F | Maschinenbau, Beleuchtung, Heizung, Waffen, Sprengen |
| G | Physik (Messen, Optik, Elektrik-Messung, Informatik G06, Akustik, Erkennung, Atomphysik) |
| H | Elektrotechnik (Schaltkreise, Halbleiter H01L, Energie H02, Nachrichtentechnik H04, Hochfrequenz) |
| Y | CPC-Querschnittsschemata (Y02 Klima/CO2, Y04 IoT/Smart Grid, Y10 Cross-Reference) — **nur CPC, nicht IPC** |

## Ablauf

### 1. Erfindungsmaterial einlesen

- Erfindungsbeschreibung
- Anspruchsentwurf
- Datenblatt
- Skizzen / Zeichnungen
- Memo der Patentanwältin

Wenn nur sehr knappes Material vorhanden ist: an `rueckfragen-mandant` weiterleiten.

### 2. Schlüsselbegriffe extrahieren

Maximal 10 Begriffe, gegliedert in:

- **Was tut die Erfindung** (Verfahren, Funktion, Wirkung)
- **Wie ist sie aufgebaut** (Vorrichtungsmerkmale, Komponenten)
- **Wo wird sie eingesetzt** (Anwendungsfeld)
- **Mit welchen Stoffen / Materialien** (bei chemischen Erfindungen)

### 3. Kandidatenklassen sammeln

Zwei Wege parallel:

**a) Espacenet Classification Browser.** Bei den Schlüsselbegriffen den [Espacenet Classification Search](https://worldwide.espacenet.com/patent/cpc-browser) öffnen und die Begriffe nacheinander eingeben. Trefferklassen mit jeweiliger Definition notieren.

**b) Top-Down über Sektion / Klasse.** Aus dem Technikgebiet (Kaltstart-Interview) die wahrscheinliche Sektion wählen, von dort über die [WIPO IPC Online Publication](https://www.wipo.int/classifications/ipc/ipcpub) bis zur Untergruppe navigieren.

### 4. Auswahl Haupt- und Nebenklassen

Vorschlag formulieren:

```
Hauptklasse CPC: H02J 3/00 — Schaltungsanordnungen oder Systeme für die Versorgung oder Verteilung elektrischer Energie
 Entsprechende IPC: H02J 3/00
Nebenklassen CPC:
 - H02J 3/14 — Anpassung der Leistung an den Verbrauch (Lastmanagement)
 - G06Q 50/06 — Energie-, Wasser- oder Gasversorgung
 - Y02E 60/00 — Technologies für die Reduktion von Treibhausgasen (CPC-only)
```

Pro Klasse zwei Sätze Begründung, **warum** sie passt — verankert in den Schlüsselbegriffen.

### 5. Verifikation

- Auf den Espacenet-Klassen-Definitionsseiten die **Anmerkungen** lesen (Hinweise "nicht hier, sondern dort").
- Eine Stichprobe (3–5 bekannte Patente der Mandantin) klassifizieren lassen und prüfen, ob die Klassen aus Schritt 4 dort tatsächlich angebracht sind.

### 6. Übergabe

Die endgültige Klassenliste übergibt das Skill in maschinenlesbarer Form an `agentische-datenbank-recherche`:

```yaml
klassen:
 cpc_haupt: H02J 3/00
 cpc_neben: [H02J 3/14, G06Q 50/06, Y02E 60/00]
 ipc_haupt: H02J 3/00
 ipc_neben: [H02J 3/14, G06Q 50/06]
```

## Hinweise

- **CPC ist feiner.** Wenn EPA-/USPTO-/CN-/KR-Patente recherchiert werden, immer CPC. Wenn ältere Patente vor 2013 oder Patente aus Ländern ohne CPC: zusätzlich IPC.
- **Y-Sektion.** Y02 ist ein CPC-Querschnittsschema für Klimatechnologien — relevant für Energietechnik, Bauwesen, Verkehr. Y04 IoT, Y10 Cross-Reference. **Nicht in IPC** vorhanden.
- **Mehrere Klassen sind die Regel.** Eine moderne Anmeldung hat oft 5–15 CPC-Symbole. Recherche-Klassenset darf großzügig sein; verengt wird über Schlüsselbegriffe und Volltext.
- **Symbol-Syntax.** Sektion (Buchstabe) + Klasse (zweistellig) + Unterklasse (Buchstabe) + Hauptgruppe (1–3 Ziffern) + `/` + Untergruppe (2–6 Ziffern). Beispiel `H04L 9/00` heißt H/H04/H04L/H04L 9/00.

## Disclaimer

> **Hinweis zur Klassifikation.** Die hier vorgeschlagenen CPC- und IPC-Klassen sind eine KI-gestützte **Vorklassifikation** zur Recherche-Steuerung und keine amtliche Klassifikation. Die endgültige Klasseneinordnung einer eigenen Anmeldung erfolgt durch das Patentamt. Für die Recherchesteuerung sind ergänzend Schlüsselbegriffe und Volltextsuchen einzusetzen — keine Klassenrecherche ohne Volltext.

## Triage-Fragen vor Klassifikations-Recherche

Bevor die CPC/IPC-Klassen festgelegt werden, klaere:
1. Welches technische Gebiet ist primaer betroffen (Hauptklasse) und welche Querschnittsklassen koennen relevant sein?
2. Sind Y-Klassen (CPC-spezifisch, Klimatechnologie, IoT) zutreffend?
3. Soll IPC zusaetzlich zu CPC eingesetzt werden (notwendig für Länder ohne CPC und aeltere Patente vor 2013)?
4. Wurde die Klassifikation anhand des naechstliegenden Anspruchsmerkmals (nicht des Funktionsergebnisses) bestimmt?

## Aktuelle Rechtsprechung

> **EPA, Technische Beschwerdekammer, T 0190/99 (Klassifikationsirrtum):** Ein Fehler in der Klassifikation einer Anmeldung beeintraichtigt die Neuheit und erfinderische Taetigkeit der Anmeldung nicht, solange der beanspruchte Gegenstand ordnungsgemaess offenbart ist; die Klassifikation ist eine verwaltungstechnische Einordnung, kein Schutzrechtsmerkmal.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **DPMA, Merkblatt Klassifikation 2023:** CPC-Klassen werden von Espacenet und Google Patents korrekt indexiert; für die agentische Recherche ist die Kombination von Klassen- und Schluessel-wort-Suche unverzichtbar, da Klassifikationsfehler der Aemter zu Luecken fuehren koennen.
