---
name: dfg-ki-ethik-forschungsdaten
description: "DFG-Antrag auf KI-Nutzung, Ethik, Datenschutz, Forschungsdatenmanagement und gute wissenschaftliche Praxis prüfen. Behandelt Vertraulichkeit in Begutachtung, Datenmanagementplan, sensible Daten, Open Access und Nachnutzung."
---

# KI, Ethik und Forschungsdaten

## Worum geht es

Seit etwa 2022 ist der **Datenmanagementplan (DMP)** Pflichtbestandteil jedes DFG-Antrags, in dem Forschungsdaten erhoben oder verarbeitet werden. KI-Nutzung wird in der DFG-Position klar geregelt — keine Verbote, aber Transparenz. Ethik, Datenschutz und gute wissenschaftliche Praxis bilden den Rahmen, in dem der Antrag formal genehmigungsfähig wird. Dieser Skill baut den Querschnittsabschnitt zu KI, Ethik und Daten so, dass er den Antrag nicht ausbremst — sondern als seriös und gut vorbereitet erscheinen lässt.

**Alte-Hasen-Faustregel:** Ein zu knapper DMP ist kein Beinbruch, ein **fehlender DMP** dagegen schon. KI-Nutzung darf — wer aber nicht transparent macht, was er mit KI tut, riskiert Rückfragen, die den Antrag in die nächste Sitzungsrunde schicken. Lieber zwei Sätze zur KI-Nutzung im Methodenteil als gar nichts.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen diesen Skill, wenn:

- Forschungsdaten erhoben, verarbeitet oder publiziert werden (das ist fast immer).
- KI-Werkzeuge im Projekt eingesetzt werden (Datenanalyse, NLP, Code-Generierung, Literaturrecherche).
- Humanforschung, Tierversuche, sensible Datenkategorien (Gesundheit, Genetik) im Spiel sind.
- Dual-Use-Aspekte denkbar sind.
- NFDI-Andocken sinnvoll ist.

Kaltstartfragen:

1. **Welche Daten entstehen?** Quantitativ, qualitativ, Bild, Audio, Genom, Text, Code, Simulationsoutput?
2. **Daten-Schutzgrad:** personenbezogen, urheberrechtlich geschützt, geheimhaltungsbedürftig, sicherheitsrelevant?
3. **KI im Projekt:** Wo wird KI eingesetzt? Eigene Modelle? Foundation Models? Cloud-Dienste?
4. **Ethikvotum nötig?** Menschen, Tiere, Gesundheitsdaten, vulnerable Gruppen?
5. **NFDI-Konsortium:** existiert eines im Fach? Wenn ja, welches?
6. **Archivierung:** wo werden Daten 10 Jahre vorgehalten?

## Programm- bzw. Sachrahmen

**DFG-Position zu KI in der Forschung.** Die DFG hat sich klar positioniert (DFG-Leitlinien zum Umgang mit generativen KI-Modellen): Nutzung ist nicht verboten, aber transparent zu machen. In Antragstexten dürfen KI-Tools unterstützend genutzt werden — der Antragsteller bleibt für jede Aussage und Quelle verantwortlich. **Erfundene Quellen, halluzinierte Zitate oder fremde vertrauliche Antragsunterlagen in Cloud-KI-Systemen sind ausgeschlossen.**

**Datenmanagementplan (DMP).** Pflichtbestandteil. Vordruck oder Anlage je nach Programm — die DFG verlangt typisch Auskunft zu:

1. Welche Daten entstehen (Art, Format, Größe)?
2. Wer hat Zugriff während der Projektlaufzeit?
3. Speicherung und Sicherung während der Laufzeit?
4. Metadaten und Standards (welche Schemata, welche kontrollierten Vokabulare)?
5. Archivierung nach Projektende (wo, wie lange, in welcher Form)?
6. Nachnutzung und Open Access (welche Daten werden publiziert, unter welcher Lizenz)?
7. Personenbezogene Daten, ethische und rechtliche Aspekte?

**FAIR-Prinzipien.** Findable, Accessible, Interoperable, Reusable. Im DMP sollten diese vier Aspekte explizit adressiert werden — auch wenn nicht alle Daten 100 Prozent FAIR werden können.

**NFDI-Konsortien.** Die Nationale Forschungsdateninfrastruktur (NFDI) bietet fachspezifische Konsortien (z. B. NFDI4Chem, NFDI4Health, Text+ für Geisteswissenschaften). Wer ein passendes NFDI-Konsortium andocken kann, gewinnt im DMP — die Infrastruktur ist bereits vorhanden.

**Ethikvotum.** Erforderlich bei:

- Forschung an und mit Menschen (auch Online-Befragungen mit personenbezogenen Daten).
- Tierversuchen (zusätzlich: Anzeige bzw. Genehmigung nach TierSchG).
- Sekundärnutzung von Gesundheitsdaten.
- Sensiblen Datenkategorien (Genetik, Religion, ethnische Herkunft).

**DSGVO bei Forschungsdaten.** Personenbezogene Daten brauchen Rechtsgrundlage (Einwilligung, gesetzliche Forschungsklausel nach Landesrecht oder § 27 BDSG). Pseudonymisierung und Anonymisierung als Standardpraxis. Verzeichnis von Verarbeitungstätigkeiten (VVT) und ggf. DSFA (Datenschutz-Folgenabschätzung).

**Archivierungsdauer.** Faustregel **10 Jahre** nach Projektende (DFG-Empfehlung in den Leitlinien zur guten wissenschaftlichen Praxis). Bei einigen Daten länger (z. B. klinische Studien). Storage-Kosten in Finanzplan einplanen.

## Praxisleitfaden

**Was schnelle Genehmigung produziert.**

- **DMP konkret, nicht generisch.** "Wir archivieren Daten an einem geeigneten Repository" ist generisch. "Wir archivieren Daten am [konkretes Repository, z. B. Zenodo, RADAR, fachspezifisches NFDI-Repository] unter [Lizenz, z. B. CC BY 4.0] für 10 Jahre" ist konkret.
- **KI-Nutzung kurz und transparent.** Ein Absatz im Methodenteil: "Im Projekt werden [konkrete KI-Tools] eingesetzt für [konkrete Aufgaben, z. B. Codierung qualitativer Daten, Generierung von Code-Snippets]. Die Ergebnisse werden manuell validiert. Trainingsdaten sind [Quelle]."
- **NFDI-Andocken** wenn passend — bringt sofort Glaubwürdigkeit.
- **Ethikvotum bei Bedarf rechtzeitig eingeholt** — die Ethikkommission braucht 4 bis 12 Wochen. Wer das Votum noch nicht hat, schreibt "in Beantragung bei [Kommission], Vorlage zur Bewilligung erfolgt nachträglich" — das ist üblich.

**Was Reviewer triggert.**

- **"DMP fehlt"** — fataler Formfehler, Antrag geht zurück.
- **"DMP generisch"** — kein konkretes Repository, keine Lizenz, keine Archivierungsdauer.
- **"Ethikvotum nicht erwähnt"** bei offensichtlich votumspflichtiger Forschung — Reviewer notiert grobe Nachlässigkeit.
- **"KI-Tools genutzt aber nicht erwähnt"** — wenn methodisch klar KI im Spiel ist (z. B. NLP-Pipeline) und nicht transparent gemacht.
- **"Personenbezogene Daten ohne Rechtsgrundlage"** — DSGVO-Frage offen.
- **"Open Access nicht adressiert"** — DFG-Empfehlung wird übergangen.

**Was schnell schief geht.**

- Antragsteller nimmt einen DMP aus einem alten Projekt copy-paste — Reviewer sieht die alten Datenarten.
- Ethikvotum wird in der Antragstextphase begonnen — kommt erst nach Bewilligung, das verzögert den Projektstart um Monate.
- KI-Nutzung wird unterschätzt ("Wir nutzen nur ChatGPT für Brainstorming, das ist nicht relevant") — wenn Daten der Probanden involviert sind, ist es relevant.

**Trade-off Open Access vs. Schutzinteresse.**

| Aspekt | Pfad A: Open Access | Pfad B: Geschützt | Empfehlung |
| --- | --- | --- | --- |
| Publikationen | Gold OA, Diamond OA | Hybrid OA, später nachgereicht | Gold OA wenn Mittel beantragt |
| Forschungsdaten | offen mit Lizenz | restringiert (z. B. Sensitive Data) | offen wo möglich, restringiert wo nötig |
| Code | offen auf GitHub/GitLab | proprietär | offen, fördert Nachnutzung |
| Material | offen | nicht teilbar (Urheber, Probanden-Schutz) | je nach Material |

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| DMP knapp vs. ausführlich | 1 Seite | 3-4 Seiten | Mittellang (1-2 Seiten), konkret |
| Eigenes Repository vs. NFDI | institutionell | NFDI-Konsortium | NFDI wenn passend — bessere Sichtbarkeit |
| KI im Antrag erwähnen vs. nicht | erwähnen | verschweigen | Immer erwähnen, transparent |
| Ethikvotum vor Antrag vs. parallel | bereits vorliegend (Anlage) | in Beantragung | Bereits vorliegend ist besser |
| Forschungsdaten OA vs. restringiert | offen | restringiert | Je nach Datenart — gut begründen |
| Storage-Kosten in Finanzplan vs. institutionell | beantragen | von Universität getragen | Institutionell wenn möglich, beantragen nur bei klarem Bedarf |

## Schritt für Schritt

1. **Datentypologie erfassen.** Welche Daten in welchem Format entstehen?
2. **Schutzbedarf bewerten.** Personenbezogen? Sensibel? Urheberrechtlich?
3. **NFDI-Match prüfen.** Existiert ein passendes Konsortium?
4. **Repository wählen.** Konkretes Repository, Lizenz, Archivierungsdauer.
5. **DMP schreiben** (1-2 Seiten, sieben Standardpunkte).
6. **KI-Nutzung dokumentieren** in Methodenteil (ein Absatz).
7. **Ethikvotum-Status klären.** Beantragen wenn nötig.
8. **DSGVO-Aspekte prüfen.** Rechtsgrundlage, Einwilligung, Pseudonymisierung.
9. **Open-Access-Strategie** für Publikationen.
10. **Anlagen ergänzen:** DMP, Ethikvotum (oder Bestätigung der Beantragung), Datenschutzkonzept.

## Mustertexte / Vorlagen

**DMP-Kerntext** (Vorlage, 1 Seite):

> **Datenmanagementplan**
>
> *Datenarten.* Im Projekt entstehen [a) qualitative Interviewdaten (Audio, Transkripte), b) quantitative Befragungsdaten (CSV), c) Code (Python-Skripte zur Auswertung)]. Geschätzter Umfang: [X] GB.
>
> *Datenerhebung und Speicherung während der Laufzeit.* Daten werden auf dem institutionellen Forschungsdaten-Server [Name] gespeichert, mit täglicher Sicherung. Zugriff: Antragsteller, WMA, designierte Hilfskräfte mit Vertraulichkeitserklärung.
>
> *Metadaten.* Beschreibung nach [Standard, z. B. DataCite, DDI, MARC]. Kontrolliertes Vokabular: [z. B. GND, MeSH].
>
> *Personenbezogene Daten und Ethik.* Schriftliche Einwilligung der Probanden mit informierter Zustimmung. Pseudonymisierung bereits bei Erhebung. Ethikvotum [vorliegend (Anlage X) / in Beantragung bei [Kommission]]. Verarbeitung nach DSGVO Art. 6 Abs. 1 lit. a (Einwilligung) und § 27 BDSG (Forschungszweck).
>
> *Archivierung und Nachnutzung.* Nach Projektende werden anonymisierte Daten am Repository [konkretes Repository, z. B. NFDI4Health, Zenodo, RADAR] unter [Lizenz CC BY 4.0] für 10 Jahre archiviert. Audiodaten und nicht anonymisierbare Transkripte bleiben restringiert und sind nur über kontrollierten Zugang verfügbar.
>
> *Open Access für Publikationen.* Die im Projekt entstehenden Publikationen werden Open Access publiziert (Gold OA, soweit Mittel verfügbar; sonst Green OA im institutionellen Repositorium).
>
> *Code und Software.* Auswertungs-Skripte werden auf [GitHub / GitLab] unter MIT-Lizenz veröffentlicht.

**KI-Nutzungs-Statement** (Vorlage, Methodenteil-Absatz):

> "Im Projekt werden generative KI-Modelle [konkrete Tools, z. B. GPT-4 über lokale API, eigenes BERT-Modell] eingesetzt für [konkrete Aufgaben, z. B. erste Codierungsschritte qualitativer Daten, Vorklassifikation von Texten]. Alle KI-generierten Ergebnisse werden durch das Forschungsteam manuell validiert. Trainingsdaten der eingesetzten Modelle: [Quelle / Begrenzung]. Cloud-KI-Dienste werden nur eingesetzt für nicht-personenbezogene Daten; für sensible Daten kommen ausschließlich lokal gehostete Modelle zum Einsatz."

**Open-Access-Statement** (Vorlage):

> "Sämtliche Publikationen aus dem Projekt werden Open Access verfügbar gemacht, vorzugsweise in Gold-OA-Journalen aus den DEAL-Vereinbarungen. Für Publikationsmittel sind [Zahl] Euro pro Jahr im Finanzplan vorgesehen. Manuskripte werden zusätzlich im institutionellen Repository [Name] hinterlegt."

## Typische Fehler

- DMP aus Vorprojekt copy-paste — Reviewer sieht alte Datentypen.
- "Daten werden archiviert" — ohne Repository, ohne Dauer, ohne Lizenz.
- KI-Tools genutzt, aber nicht erwähnt — Reviewer fragt nach.
- Ethikvotum vergessen bei offensichtlich votumspflichtiger Forschung.
- DSGVO-Rechtsgrundlage nicht genannt — bei personenbezogenen Daten Pflicht.
- "Wir nutzen ChatGPT für Antragsschreiben und laden dort Antragsunterlagen hoch" — Vertraulichkeitsverstoß.
- NFDI nicht geprüft, obwohl ein passendes Konsortium existiert — verschenkter Glaubwürdigkeitsgewinn.
- Open-Access-Strategie als ein Satz "wir publizieren Open Access" ohne Details.
- 10 Jahre Archivierungsdauer in 3-Jahres-Projekt-Finanzplan vergessen.

## Regelungs- und Quellenanker

Arbeitsfokus: **KI, Ethik und Forschungsdaten**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit als Ausgangspunkt.
- `Art. 89 Abs. 1 DSGVO` — Garantien für wissenschaftliche Forschungszwecke.
- `Art. 9 Abs. 2 lit. j DSGVO` — besondere Kategorien personenbezogener Daten in Forschungskontexten.
- `§ 27 Abs. 1 BDSG` — Datenverarbeitung zu wissenschaftlichen Forschungszwecken.
- `§ 7 Abs. 1 TierSchG` — Tierversuche nur bei gesetzlich anerkanntem Zweck und Erforderlichkeit.
- `§ 8 Abs. 1 TierSchG` — Genehmigungspflichtiger Tierversuch.
- `§ 69a UrhG` — Computerprogramme als Schutzgegenstand bei Forschungssoftware.
- `DFG-Kodex Leitlinie 10` — rechtliche und ethische Rahmenbedingungen.
- `DFG-Kodex Leitlinie 13` — Herstellung von öffentlichem Zugang zu Forschungsergebnissen.
- `DFG-Kodex Leitlinie 14` — Autorschaft und Verantwortung.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Output

- **DMP-Volltext** (1-2 Seiten, sieben Standardpunkte).
- **KI-Nutzungs-Statement** für Methodenteil.
- **Ethik-Risikoampel** mit Bedarf an Voten, Anzeigen, Beratungen.
- **Anlagenliste:** DMP, Ethikvotum, Datenschutzkonzept, ggf. NFDI-Andocken-Bestätigung.
- **Offene Prüfmarker** für Aspekte, die der Antragsteller live verifizieren muss.

## Querverweise

- Projektbeschreibung (Methodenteil): `dfg-projektbeschreibung-arbeitsprogramm`
- Finanzplan (Archivierungs- und Publikationskosten): `dfg-finanzplan-module-personal-geraete`
- Formalia (DMP als Anlage einreichen): `dfg-sachbeihilfe-elan-formalia`
- Reviewer-Brille (Lücken im DMP/Ethik): `dfg-reviewer-red-team`

## Quellen Stand 05/2026

- DFG-Leitlinien zum Umgang mit generativen KI-Modellen: dfg.de
- DFG-Kodex "Leitlinien zur Sicherung guter wissenschaftlicher Praxis": dfg.de
- DFG-Empfehlungen zum Forschungsdatenmanagement: dfg.de
- DFG-Open-Access-Position: dfg.de
- NFDI-Konsortien: nfdi.de
- FAIR-Prinzipien: go-fair.org
- DSGVO und BDSG: gesetze-im-internet.de

KI-Leitlinien und DMP-Anforderungen ändern sich — vor Einreichung aktuelle DFG-Position prüfen.
