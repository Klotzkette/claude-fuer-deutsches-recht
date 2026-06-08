---
name: arbeitnehmer-status-problem
description: "Arbeitnehmer Status Problem im Plugin Arbeitsrecht: prüft konkret Statusfeststellung für eine geplante Beschaeftigung -, Gezielte Anpassung des Arbeitsrechts-Praxisprofils –, Risiko, Mandatsakten verwalten – neu anlegen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Arbeitnehmer Status Problem

## Arbeitsbereich

**Arbeitnehmer Status Problem** ordnet den Fall über die tragenden Prüfungslinien: Statusfeststellung für eine geplante Beschaeftigung -, Gezielte Anpassung des Arbeitsrechts-Praxisprofils –, Risiko. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `arbeitnehmer-status` | Statusfeststellung für eine geplante Beschaeftigung - Abgrenzung Arbeitnehmer/Selbständiger nach § 611a BGB, Scheinselbständigkeit, Clearingverfahren § 7a SGB IV, AUeG-Abgrenzung (Leiharbeit vs. Werkvertrag). Ausschließlich prospektiv - für bestehende Verhältnisse Aussenberater einschalten. |
| `arbeitsrecht-anpassen` | Gezielte Anpassung des Arbeitsrechts-Praxisprofils – Standort-Fußabdruck, Risikoeinstellung, Eskalationskontakte, Einstellungsregeln, Kündigungsregeln, Handbuchpositionen oder Untersuchungseinstellungen ändern, ohne das gesamte Kaltstart-Interview neu zu durchlaufen. |
| `arbeitsrecht-mandat-arbeitsbereich` | Mandatsakten verwalten – neu anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen. Verhindert, dass Kontext von einem Mandat in ein anderes übergeht. Relevant für Kanzleien mit mehreren Mandanten; für Syndikusrechtsanwälte deaktiviert. |
| `arbeitsrecht-problem-sortieren` | Sehr allgemeiner Einstiegsskill für unklare arbeitsrechtliche Anliegen. Sortiert Gedanken, Rolle, Ziel, Dokumente, Fristen und Konfliktlage, bevor Spezialpruefungen beginnen. Output Problemkarte, Fristenampel, Arbeitsauftrag, passende Folge-Skills und eine entscheidende Rueckfrage. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `arbeitnehmer-status`

**Fokus:** Statusfeststellung für eine geplante Beschaeftigung - Abgrenzung Arbeitnehmer/Selbständiger nach § 611a BGB, Scheinselbständigkeit, Clearingverfahren § 7a SGB IV, AUeG-Abgrenzung (Leiharbeit vs. Werkvertrag). Ausschließlich prospektiv - für bestehende Verhältnisse Aussenberater einschalten.

### /arbeitsrecht:arbeitnehmer-status

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:arbeitnehmer-status` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Scheinselbständigkeit ist eines der teuersten Risiken im deutschen Arbeitsrecht. Nachentrichtung von Sozialversicherungsbeiträgen bis zu 4 Jahren rückwirkend (§ 25 SGB IV), Steuernachzahlungen, Bußgelder — und das Arbeitsverhältnis entsteht kraft Gesetzes (§ 10 AÜG bei unerlaubter Überlassung; ggf. § 611a BGB bei fehlerhafter Klassifizierung). Dieser Skill prüft prospektiv, ob die geplante Struktur hält.

## Triage-Frage — vor der Prüfung klären

Bevor losgelegt wird, kläre:
1. Ist die Tätigkeit bereits aufgenommen oder erst geplant? (Skill ist nur prospektiv)
2. Handelt es sich um eine Einzelperson oder eine Gesellschaft als Auftragnehmer?
3. Wie viele Auftraggeber hat der Auftragnehmer aktuell?
4. Werden eigene Betriebsmittel eingesetzt?
5. Soll ein Clearingverfahren nach § 7a SGB IV eingeleitet werden?

## Eingaben

- Beschreibung der geplanten Tätigkeit (Art, Umfang, Ort, Dauer)
- Entwurf des Honorar- oder Werkvertrags (falls vorhanden)
- Angaben zur Einbindung in betriebliche Abläufe (eigene Betriebsmittel? Weisungsabhängigkeit? Mehrere Auftraggeber?)
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Klassifizierungsrisiken

## Zentrale Anspruchsgrundlagen & Normen

- **§ 611a BGB** — Arbeitnehmereigenschaft; Gesamtbildbetrachtung; vertragliche Bezeichnung unerheblich
- **§ 7 Abs. 1 SGB IV** — sozialversicherungsrechtlicher Beschäftigungsbegriff; Weisungsgebundenheit und Eingliederung als Anknüpfungspunkte
- **§ 7a SGB IV** — Clearingverfahren Deutsche Rentenversicherung Bund
- **§ 25 SGB IV** — rückwirkende Nachzahlungspflicht bis 4 Jahre (bei Vorsatz 30 Jahre)
- **§ 28e SGB IV** — Haftung des Auftraggebers für nicht abgeführte Sozialversicherungsbeiträge
- **§ 266a StGB** — Vorenthalten und Veruntreuen von Arbeitsentgelt; Strafbarkeit bei Vorsatz
- **§§ 1, 10 AÜG** — Erlaubnispflicht Arbeitnehmerüberlassung; Entstehung des Arbeitsverhältnisses bei fehlender Erlaubnis kraft Gesetzes
- **§ 1 Abs. 1b AÜG** — Höchstüberlassungsdauer 18 Monate

## Aktuelle Rechtsprechung

- **BAG, Urteil vom 01.12.2020 - 9 AZR 102/20** (Crowdworker / Plattformarbeit): Auch ein Crowdworker, der ueber eine Smartphone-App Mikroauftraege erfuellt, kann Arbeitnehmer sein, wenn die organisatorische Einbindung (z.B. Anreizsystem mit Stufen / Level / Bewertung) ihn zur staendigen Auftragsannahme veranlasst und faktisch fremdbestimmte Arbeit erzwingt. Eine starre vertragliche Bezeichnung ist unerheblich; entscheidend ist die tatsaechliche Durchfuehrung. Quelle: dejure.org-Vernetzung BAG 01.12.2020 - 9 AZR 102/20.
- Hinweis: BAG hat den Crowdworker-Status seitdem nicht generell ausgeweitet, jeder Einzelfall ist anhand der typusbildenden Merkmale (Weisungsgebundenheit, persönliche Abhaengigkeit, Fremdbestimmung) zu pruefen.
- **EU-Plattformarbeitsrichtlinie (EU) 2024/2831 vom 23.10.2024** (ABl. L vom 11.11.2024; CELEX 32024L2831) - Umsetzungsfrist 02.12.2026:
 - **Widerlegbare gesetzliche Vermutung** eines Arbeitsverhaeltnisses (Art. 5): liegen Tatsachen vor, die auf Steuerung und Kontrolle hindeuten, wird ein Arbeitsverhaeltnis vermutet; **die Beweislast für das Nichtbestehen liegt bei der digitalen Arbeitsplattform**; gilt nur für Zeitraeume ab 02.12.2026 (keine Rueckwirkung).
 - **Algorithmisches Management (Kapitel III)**: Verbot der Verarbeitung bestimmter Daten (emotionaler Zustand, Privatgespraeche, Gewerkschaftszugehoerigkeit, sensible Merkmale, biometrische Identifizierung); Pflicht zur Datenschutz-Folgenabschaetzung mit Einbindung der Beschaeftigtenvertreter; Transparenzpflicht ueber Einsatz und Funktionsweise automatisierter Systeme.
 - **Menschliche Aufsicht**: Entscheidungen ueber **Kontosperrung oder Vertragsbeendigung** muessen zwingend von einem Menschen getroffen werden; Recht auf Erklaerung und Ueberpruefung automatisierter Entscheidungen innerhalb von zwei Wochen.
 - **Anwendungsbereich**: gilt für Plattformarbeitende mit Arbeitsvertrag/Arbeitsverhaeltnis; Vorschriften zum algorithmischen Management auch für Personen ohne Arbeitsvertrag.
 - Umsetzung in deutsches Recht (vermutlich Aenderung BGB, BetrVG, NachweisG) steht aus; Praxis sollte im Mandat bereits ab 2026 die Vermutungsregel mitdenken.
 - Quelle: eur-lex.europa.eu - https://eur-lex.europa.eu/eli/dir/2024/2831/oj
- Aktualisierungen vor Schriftsatzverwendung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de, bundessozialgericht.de) pruefen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 – Arbeitnehmereigenschaft (§ 611a BGB)

Seit 01.04.2017 kodifiziert (§ 611a BGB):

**Arbeitnehmer** ist, wer aufgrund eines privatrechtlichen Vertrags **im Dienste eines anderen** zu **weisungsgebundener, fremdbestimmter Arbeit** verpflichtet ist. Maßgeblich ist das Gesamtbild; kein einzelnes Merkmal ist allein entscheidend.

**Weisungsgebundenheit** (§ 611a Abs. 1 S. 2 BGB):
- Inhalt, Durchführung, Zeit, Dauer oder Ort der Tätigkeit
- In den Betrieb eingegliedert?
- Eigene unternehmerische Entscheidungsfreiheit? (eigene Betriebsmittel, eigenes unternehmerisches Risiko)

**Entscheidungsbaum Schritt 1:**
- Weisungsrecht zu Inhalt/Zeit/Ort? → Ja: starkes Indiz Arbeitnehmer → weiter zu Schritt 2
- Eigene Betriebsmittel und mehrere Auftraggeber? → Ja: Indiz Selbständiger → Gesamtbild trotzdem prüfen
- Kein unternehmerisches Risiko? → Ja: starkes Indiz Arbeitnehmer

**Prüfkatalog (BAG-Kriterienliste, Gesamtbild):**

| Indiz für Arbeitnehmer | Indiz für Selbständigen |
|---|---|
| Weisungsbefugnis bzgl. Arbeitszeit/-ort | Freie Zeiteinteilung |
| Eingliederung in Betriebsorganisation | Eigene Betriebsmittel |
| Kein unternehmerisches Risiko | Mehrere Auftraggeber |
| Keine eigenen Mitarbeiter | Eigene Werbung / Auftreten am Markt |
| Persönliche Leistungspflicht | Vertretung durch Dritte möglich |
| Betriebsmittel werden gestellt | Eigene Haftung für Ergebnis |
| Vergütung als festes Gehalt | Vergütung nach Projektergebnis |

### Schritt 2 – Sozialversicherungsrechtliche Bewertung (§ 7 SGB IV)

Gem. § 7 Abs. 1 SGB IV ist Beschäftigung die **nichtselbständige Arbeit**, insbesondere in einem Arbeitsverhältnis. Anhaltspunkte: Weisungsgebundenheit und Eingliederung (§ 7 Abs. 1 S. 2 SGB IV). Der SV-Begriff deckt sich weitgehend mit § 611a BGB, ist aber eigenständig auszulegen.

**Clearingverfahren § 7a SGB IV:**
- Jede der Beteiligten (Arbeitnehmer, Auftraggeber) kann vor Aufnahme der Tätigkeit Feststellung des Erwerbsstatus bei der **Deutsche Rentenversicherung Bund (Clearingstelle)** beantragen.
- Dauer: ca. 3–6 Monate
- Bei negativem Bescheid (Scheinselbständigkeit festgestellt): Nachzahlung Sozialversicherungsbeiträge bis zu 4 Jahre rückwirkend (§ 25 SGB IV); bei Vorsatz: 30 Jahre.
- **Empfehlung bei Grenzfällen:** Clearingverfahren proaktiv nutzen, bevor Tätigkeit beginnt.

### Schritt 3 – AÜG-Abgrenzung (§§ 1 ff. AÜG)

Falls Dienstleistung durch Dritte (Werkvertrag, Dienstleistungsvertrag):

**Echte Arbeitnehmerüberlassung (AÜG):**
- Erlaubnispflichtig (§ 1 AÜG)
- Höchstüberlassungsdauer: 18 Monate (§ 1 Abs. 1b AÜG)
- Equal Pay nach § 8 AÜG ab Monat 10 (tariflich verlängerbar bis 15 Monate)
- Kein "verdeckter" Arbeitnehmer – Offenlegungspflicht in Vertrag (§ 1 Abs. 1 S. 5 AÜG)

**Scheinselbständigkeit bei Werkvertrag:**
Wenn der Auftragnehmer nach Weisungen des Auftraggebers in dessen Betrieb eingegliedert ist, liegt verdeckte Arbeitnehmerüberlassung vor. Bei fehlender AÜG-Erlaubnis: Arbeitsverhältnis entsteht kraft Gesetzes (§ 10 Abs. 1 AÜG).

**10 Prüfpunkte Werkvertrag vs. Arbeitnehmerüberlassung:**
1. Schuldet Auftragnehmer einen Werkerfolg oder Dienste?
2. Trägt er das unternehmerische Werkrisiko (Nachbesserungspflicht, Gewährleistung)?
3. Setzt er eigene Betriebsmittel ein?
4. Bestimmt er Arbeitszeit und -ort selbst?
5. Erhält er Weisungen zu Inhalt und Durchführung?
6. Ist er in Teambesprechungen, Schichtpläne, EDV-Systeme des Auftraggebers eingebunden?
7. Muss er persönlich tätig sein oder kann er Erfüllungsgehilfen einsetzen?
8. Hat er mehrere Auftraggeber (Indiz für echte Selbständigkeit)?
9. Wie lange besteht die Geschäftsbeziehung? (Dauerschuldverhältnisse sind verdächtig)
10. Wie hoch ist der Anteil des Auftraggebers am Gesamtumsatz des Auftragnehmers? (> 75 %: hohes Risiko)

### Schritt 4 – Risikobewertung und Handlungsempfehlungen

**Risikoampel:**

🟢 **Kein Risiko:**
- Auftragnehmer hat mehrere Auftraggeber, eigene Betriebsmittel, trägt unternehmerisches Risiko, keine Eingliederung

🟡 **Grenzfall – Gestaltungsempfehlungen:**
- Vertrag überarbeiten: Werkvertrag mit klarem Werkerfolg und Gewährleistung
- Eingliederung reduzieren: keine fixen Arbeitszeiten, kein Büro beim Auftraggeber, eigene IT
- Clearingverfahren § 7a SGB IV einleiten

🔴 **Blockierend – Neustrukturierung oder reguläre Einstellung:**
- Vollständige Eingliederung in Betrieb, feste Arbeitszeiten, kein eigenes unternehmerisches Risiko
- Keine AÜG-Erlaubnis, aber Beschäftigung wie Leiharbeitnehmer

## Output-Template Statusanalyse

**Adressat:** Auftraggeber/Mandant — Tonfall: sachlich-juristisch, praxisorientiert

```
STATUSFESTSTELLUNG – [Tätigkeitsbeschreibung] – [Datum]
VERTRAULICH – MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

Ergebnis: [Selbständig / Grenzfall / Arbeitnehmerstatus wahrscheinlich]

I. § 611a BGB Gesamtbild
 Indizien für Arbeitnehmer: [Liste]
 Indizien für Selbständigen: [Liste]
 Gesamtbewertung: [Ergebnis]

II. § 7 SGB IV (SV-rechtlich)
 Nachzahlungsrisiko: [Betrag] bei [N] Jahren rückwirkend
 Strafbarkeit § 266a StGB: [ja / nein / Prüfen]

III. AÜG-Relevanz (falls gegeben)
 Erlaubnis vorhanden: [ja / nein]
 Höchstüberlassungsdauer erreicht: [ja / nein / Datum]

IV. Clearingverfahren empfohlen? [ja / nein – Begründung]

V. Gestaltungsempfehlungen
 1. [konkrete Maßnahme]
 2. [konkrete Maßnahme]

Risikobewertung: [🔴 / 🟡 / 🟢]
```

## Beispiele

**Beispiel – IT-Freelancer:**

*Sachverhalt:* Softwareentwickler K soll als "freier Mitarbeiter" für 12 Monate ausschließlich für einen Auftraggeber tätig sein, arbeitet täglich im Büro des Auftraggebers, nutzt dessen Laptop, nimmt an Daily-Standup-Meetings teil, erhält Aufgaben über das Jira-Board des Auftraggebers.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken / typische Fehler

- **Vertrag vs. Praxis:** § 611a Abs. 1 S. 5 BGB – Wie der Vertrag heißt, ist unerheblich; entscheidend ist die tatsächliche Durchführung.
- **Rückwirkende Sozialversicherungspflicht** – bis 4 Jahre (§ 25 SGB IV), bei Vorsatz 30 Jahre.
- **AÜG ohne Erlaubnis** – führt zur Entstehung eines Arbeitsverhältnisses kraft Gesetzes (§ 10 AÜG); erhebliche Haftungsrisiken.
- **Prospektiver Charakter** – dieses Plugin prüft nur geplante Strukturen; für bestehende Verhältnisse unbedingt Außenberater und ggf. Clearingstelle einschalten.
- **Gesamtbild-Falle:** Selbst wenn 7 von 10 Kriterien für Selbständigkeit sprechen, kann das Gesamtbild dennoch Arbeitnehmerstatus ergeben, wenn die überwiegende Weisungsgebundenheit faktisch vorliegt.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `arbeitsrecht-anpassen`

**Fokus:** Gezielte Anpassung des Arbeitsrechts-Praxisprofils – Standort-Fußabdruck, Risikoeinstellung, Eskalationskontakte, Einstellungsregeln, Kündigungsregeln, Handbuchpositionen oder Untersuchungseinstellungen ändern, ohne das gesamte Kaltstart-Interview neu zu durchlaufen.

### /arbeitsrecht:arbeitsrecht-anpassen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:arbeitsrecht-anpassen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Der Nutzer möchte etwas im Praxisprofil ändern – eine Jurisdiktion, eine Risikoeinstellung, einen Eskalationskontakt, eine Handbuchposition – ohne das gesamte Kaltstart-Interview zu wiederholen.

## Eingaben

- Beschreibung der gewünschten Änderung (Freitext oder Abschnittsname)
- Aktuelle Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md`

## Ablauf

### 1. Konfiguration lesen

`~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` und `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` einlesen.

Falls das Plugin noch nicht eingerichtet ist oder `[PLATZHALTER]` enthält:
> Das Plugin wurde noch nicht eingerichtet. Führen Sie `/arbeitsrecht:arbeitsrecht-kaltstart-interview` aus.

### 2. Gewünschte Änderung klären

Wenn die Angabe des Nutzers unklar ist, einen einzigen klärenden Prompt stellen – nicht mehrere Nachfragen hintereinander:

> Was möchten Sie ändern?
> - Neuen Standort / neues Bundesland hinzufügen
> - Tarifvertrag oder Betriebsratssituation aktualisieren
> - Eskalationskontakt ändern
> - Einstellungs- oder Kündigungsregeln anpassen
> - Handbuch-/Betriebsvereinbarungsreferenz aktualisieren
> - Integrationen neu prüfen (`--check-integrations`)
> - Anderes – bitte beschreiben

### 3. Nur den betroffenen Abschnitt aktualisieren

Den relevanten Abschnitt in der Konfigurationsdatei isolieren, die Änderung durchführen, den Rest unberührt lassen. Keine komplette Neugenerierung.

**Besonderheiten:**
- **Neuer Standort / Bundesland:** Eskalationstabelle um das neue Bundesland ergänzen. Auf besondere Landesgesetze hinweisen (z.B. Bayerisches Urlaubsgesetz, abweichendes Landesdatenschutzrecht). KSchG-Schwellenwert neu berechnen.
- **Neuer Tarifvertrag:** Nachwirkung (§ 4 Abs. 5 TVG) und Günstigkeitsprinzip (§ 4 Abs. 3 TVG) berücksichtigen. Ggf. Hinweis auf Allgemeinverbindlichkeit (§ 5 TVG).
- **Betriebsrat neu eingetragen:** § 102 BetrVG-Verpflichtung in Eskalationstabelle aufnehmen; Hinweis auf § 99 BetrVG (Einstellung) und § 87 BetrVG (Mitbestimmung).
- **Eskalationskontakt:** Nur dieses Feld ändern; Risikologik bleibt.

### 4. Änderung schreiben und bestätigen

Die geänderte Konfiguration zurückschreiben und dem Nutzer mitteilen, was geändert wurde (Vorher/Nachher, ein Diff).

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Relevante Normen je nach Änderungsbereich:
- Neues Bundesland: Landesurlaubsgesetze, LDSG des Landes, ggf. Tarifvertrag mit Landesbezug
- Betriebsrat: BetrVG §§ 1, 87, 99, 102, 111 ff.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
Profil-Änderung: [Kürzel der Änderung]
================================================
Geändert: [Abschnitt in CLAUDE.md]

Vorher:
 [Alt-Wert]

Nachher:
 [Neu-Wert]

Gespeichert: ~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md
```

## Beispiele

```
/arbeitsrecht:arbeitsrecht-anpassen
Neuen Standort Hamburg hinzufügen, ca. 25 Mitarbeiter, kein Betriebsrat.
```

```
/arbeitsrecht:arbeitsrecht-anpassen
Eskalationskontakt für betriebsbedingte Kündigungen auf Dr. Müller (GC) ändern.
```

```
/arbeitsrecht:arbeitsrecht-anpassen
Wir sind seit Januar diesem Jahr an den Tarifvertrag Einzelhandel NRW gebunden.
```

## Risiken / typische Fehler

- **Landesrecht übersehen.** Bayern, Brandenburg und andere Länder haben eigene Urlaubsgesetze mit abweichenden Mindesturlaubstagen. Bei neuem Bundesland immer Landesspezifika prüfen.
- **Tarifbindung durch Bezugnahmeklausel.** Auch ohne Verbandsmitgliedschaft kann ein Tarifvertrag vertraglich einbezogen sein. Prüfen, ob neue Tarifbindung auch bestehende Verträge erfasst.
- **Betriebsrat-Zuständigkeit.** Bei neuem Betriebsrat: § 102 BetrVG gilt für JEDE Kündigung, § 99 BetrVG für jede Einstellung – sofort in Eskalationstabelle aufnehmen.

## 3. `arbeitsrecht-mandat-arbeitsbereich`

**Fokus:** Mandatsakten verwalten – neu anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen. Verhindert, dass Kontext von einem Mandat in ein anderes übergeht. Relevant für Kanzleien mit mehreren Mandanten; für Syndikusrechtsanwälte deaktiviert.

### /arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

Anwälte und Kanzleien arbeiten für mehrere Mandanten gleichzeitig. Eine Mandatsakte hält den Kontext eines Mandanten strikt von allen anderen getrennt. Dieser Skill verwaltet diese Akten.

## Zweck

Für Kanzleien mit mehreren Mandanten (Einzelkanzlei, Mittelkanzlei, Großkanzlei). Für Syndikusrechtsanwälte mit einem Arbeitgeber ist diese Funktion standardmäßig **deaktiviert** – alle Skills nutzen automatisch den Kanzlei-/Unternehmenskontext.

Im Arbeitsrecht entspricht eine "Akte" typischerweise einem bestimmten Mandanten-Sachverhalt:
- Eine konkrete Kündigung oder Kündigungsschutzklage
- Eine interne Untersuchung
- Ein Entsendungsprojekt
- Ein Tarifvertragsstreit
- Eine Massenentlassung / Betriebsänderung

## Eingaben

- Befehl: `neu`, `auflisten`, `wechseln`, `schließen` oder `keine`
- Kürzel der Akte (Slug), z.B. `mueller-ksg-2024`
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` – Abschnitt `## Mandantenakten`

## Ablauf

### Vorabprüfung

`~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` lesen, Abschnitt `## Mandantenakten` prüfen.

Falls `Aktiviert: ✗` (Syndikus / in-house):
> Mandantenakten sind deaktiviert – Sie sind als [Kanzlei/in-house] konfiguriert und arbeiten mit einem einzigen Mandantenkontext. Falls Sie tatsächlich mehrere Mandanten betreuen, führen Sie `/arbeitsrecht:arbeitsrecht-kaltstart-interview --redo` aus und wählen Sie Kanzleibetrieb. Andernfalls benötigen Sie `/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich` nicht.

### Befehle

**`neu <kürzel>`** – Neue Mandatsakte anlegen.
1. Kürzel in Kleinbuchstaben, Bindestriche erlaubt (z.B. `mueller-ksg-2024`).
2. Kurzes Intake-Interview:
 > - Mandantenname (intern, nicht für Ausgaben)
 > - Sachverhalt in einem Satz (Kündigung / Untersuchung / Entsendung / Tarifstreit)
 > - Zuständiger Anwalt
 > - Aktenstatus: offen / ruhend / geschlossen
 > - Besondere Vertraulichkeitsstufe?
3. `mandat.md`, `verlauf.md` und `notizen.md` anlegen unter:
 `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/akten/<kürzel>/`

**`auflisten`** – Alle Akten tabellarisch mit Status und aktive-Akte-Flag anzeigen.

**`wechseln <kürzel>`** – Aktive Akte setzen. Alle folgenden Skill-Aufrufe arbeiten im Kontext dieser Akte.

**`schließen <kürzel>`** – Akte archivieren (in `_archiv/` verschieben, nie löschen). Keine Daten vernichten.

**`keine`** – Vom aktiven Mandat lösen; auf Kanzlei-Ebene-Kontext zurücksetzen.

### Aktenübergreifender Kontext

Bei `Aktenübergreifender Kontext: deaktiviert` (Standard): Ein Skill, der in Akte A arbeitet, liest niemals Dateien aus Akte B. Dies ist datenschutzrechtlich geboten (§ 43a Abs. 2 BRAO, § 26 BDSG): Personalakte eines Arbeitnehmers darf nicht in die Analyse eines anderen einfließen.

Lerneffekte, die mehrere Mandate betreffen, werden in die Kanzlei-CLAUDE.md geschrieben, nicht in eine Akten-Datei.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht des Rechtsanwalts)
- § 203 StGB (Verletzung von Privatgeheimnissen)
- § 26 BDSG (Beschäftigtendatenschutz; gilt auch für anwaltlich bearbeitete Personaldaten)
- § 53 StPO (Zeugnisverweigerungsrecht des Rechtsanwalts)

## Ausgabeformat

**Neu:**
```
Mandatsakte angelegt: mueller-ksg-2024
========================================
Mandant: [intern anonymisiert]
Sachverhalt: Kündigungsschutzklage nach betriebsbedingter Kündigung
Anwalt: [Name]
Status: offen
Ablage: ~/.../akten/mueller-ksg-2024/

Dateien erstellt:
 mandat.md – Akten-Stammdaten und Kontext
 verlauf.md – Chronologisches Protokoll
 notizen.md – Freie Notizen, entwürfe, Recherche-Ergebnisse
```

**Auflisten:**
```
Mandantenakten – Arbeitsrecht
=================================
● mueller-ksg-2024 [offen] Kündigungsschutzklage geändert: heute
 bayer-betriebsrat [ruhend] BR-Streitigkeit § 87 BetrVG geändert: vor 3 Wo.
 huber-entsendung [offen] Entsendung Frankreich geändert: gestern

● = aktive Akte
```

## Beispiele

```
/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich neu mueller-ksg-2024
Kündigung wegen betriebsbedingter Restrukturierung, Sozialauswahl streitig.
```

```
/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich wechseln bayer-betriebsrat
```

```
/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich auflisten
```

## Risiken / typische Fehler

- **Akten nicht schließen, wenn das Mandat endet.** Archivieren statt löschen – BRAO § 50 Abs. 2 schreibt 5 Jahre Aufbewahrung vor.
- **Mandant nicht anonymisieren.** Kürzel und interne Bezeichnung sollten nicht von Unbefugten identifiziert werden können.
- **Aktenübergreifende Suche ungewollt aktivieren.** Standardmäßig deaktiviert aus datenschutzrechtlichen Gründen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `arbeitsrecht-problem-sortieren`

**Fokus:** Sehr allgemeiner Einstiegsskill für unklare arbeitsrechtliche Anliegen. Sortiert Gedanken, Rolle, Ziel, Dokumente, Fristen und Konfliktlage, bevor Spezialpruefungen beginnen. Output Problemkarte, Fristenampel, Arbeitsauftrag, passende Folge-Skills und eine entscheidende Rueckfrage.

### Arbeitsrecht - Problem Sortieren

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Arbeitsrecht - Problem Sortieren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill ist der ruhige erste Tisch in einer unuebersichtlichen arbeitsrechtlichen Lage. Er beginnt nicht mit einem Schema, sondern mit Ordnung: Was ist passiert, was will die Person erreichen, was liegt als Dokument vor, was eilt und welcher Fachmodul hilft jetzt wirklich?

## Vier Pflichtbausteine

1. Ziel klaeren: Was soll entschieden, geprueft, entworfen, verbessert oder verhandelt werden?
2. Kontext sichern: Rolle, Frist, Dokumente, Beteiligte, Vorgeschichte und Belege.
3. Grenzen setzen: keine Blindzitate, keine erfundenen Tatsachen, keine ungewollten Zugestaendnisse.
4. Ausgabeformat bestimmen: Memo, Tabelle, Schriftsatz, Brief, Beschluss, TOP, Checkliste oder Red-Team-Liste.

## Arbeitsrechtliche Pflicht-Ersttriage (vor jeder Vertiefung)

- **KSchG-Anwendbarkeit:** § 23 Abs. 1 KSchG (i.d.R. mehr als 10 Arbeitnehmer im Betrieb, Schwellenwertberechnung pro Kopf nach BAG ständiger Rechtsprechung mit Teilzeitfaktor) und § 1 Abs. 1 KSchG (Wartezeit sechs Monate).
- **Kündigungsschutzklage-Frist:** § 4 KSchG drei Wochen ab Zugang. Versäumnis: § 7 KSchG Wirksamkeitsfiktion.
- **Sonderkündigungsschutz prüfen:** Schwangerschaft (§ 17 MuSchG), Elternzeit (§ 18 BEEG), Schwerbehinderung (§ 168 SGB IX), Betriebsrat (§ 15 KSchG, § 103 BetrVG), Datenschutzbeauftragter.
- **Massenentlassung:** § 17 KSchG Schwellen (z.B. mehr als 5 in Betrieb mit 21-59 AN, mehr als 10 % oder 25 in Betrieb mit 60-499 AN). Anzeige bei Bundesagentur vor Ausspruch der Kündigungen.
- **Betriebsratsanhörung:** § 102 BetrVG zwingend vor jeder Kündigung; ohne ordnungsgemäße Anhörung Kündigung gemäß § 102 Abs. 1 Satz 3 BetrVG unwirksam.
- **AGG-Bezug:** §§ 1, 3, 22 AGG bei verdachtsweiser Diskriminierung (Alter, Geschlecht, Behinderung, Religion etc.). Frist § 15 Abs. 4 AGG zwei Monate ab Kenntnis.

## Trade-off-Hinweis

Schnellfeuer-Klage spart Frist, aber ohne Sozialauswahl-Prüfung und ohne Betriebsratsanhörungs-Check verschenkt Mandantschaft Argumente. Lieber **3-Wochen-Frist sichern** mit knapper Klageschrift, dann nachschriftsätzlich substantiieren.

## Workflow

1. Material erfassen und sichtbar zwischen Tatsache, Behauptung und Bewertung trennen.
2. Eilige Punkte vorziehen — insbesondere § 4 KSchG, § 17 KSchG-Massenentlassungsanzeige, AGG-2-Monats-Frist und Verfall-/Ausschlussfristen aus Tarif- oder Arbeitsvertrag (z.B. zweistufige Ausschlussfrist).
3. Schwachstellen und Gegenargumente benennen (Betriebsratsanhörung, Sozialauswahl, Schriftform § 623 BGB).
4. Passende Folge-Skills aus demselben Plugin vorschlagen.
5. Einen verwendbaren Output liefern und offene Punkte mit `[noch klaeren]` markieren.

## Ausgabe

| Punkt | Befund | Risiko | Naechster Schritt |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Qualitaetsgate

Ist die Antwort handlungsorientiert, knapp, respektvoll, belegnah und ohne erfundene Quellen? Sind Fristen und offene Tatsachen sichtbar? Ist der naechste Schritt eindeutig?

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
