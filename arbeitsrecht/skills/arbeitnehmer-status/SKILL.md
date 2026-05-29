---
name: arbeitnehmer-status
description: "Statusfeststellung für eine geplante Beschaeftigung - Abgrenzung Arbeitnehmer/Selbständiger nach § 611a BGB, Scheinselbständigkeit, Clearingverfahren § 7a SGB IV, AUeG-Abgrenzung (Leiharbeit vs. Werkvertrag). Ausschließlich prospektiv - für bestehende Verhältnisse Aussenberater einschalten."
---

# /arbeitsrecht:arbeitnehmer-status

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
- Hinweis: BAG hat den Crowdworker-Status seitdem nicht generell ausgeweitet, jeder Einzelfall ist anhand der typusbildenden Merkmale (Weisungsgebundenheit, persoenliche Abhaengigkeit, Fremdbestimmung) zu pruefen. EuGH-Plattformarbeitsrichtlinie (RL 2024/2831) ist mit Umsetzungsfrist bis Dez. 2026 zu beobachten.
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

I.   § 611a BGB Gesamtbild
     Indizien für Arbeitnehmer: [Liste]
     Indizien für Selbständigen: [Liste]
     Gesamtbewertung: [Ergebnis]

II.  § 7 SGB IV (SV-rechtlich)
     Nachzahlungsrisiko: [Betrag] bei [N] Jahren rückwirkend
     Strafbarkeit § 266a StGB: [ja / nein / Prüfen]

III. AÜG-Relevanz (falls gegeben)
     Erlaubnis vorhanden: [ja / nein]
     Höchstüberlassungsdauer erreicht: [ja / nein / Datum]

IV.  Clearingverfahren empfohlen? [ja / nein – Begründung]

V.   Gestaltungsempfehlungen
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
