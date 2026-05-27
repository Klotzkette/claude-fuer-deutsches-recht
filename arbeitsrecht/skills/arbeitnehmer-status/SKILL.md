---
name: arbeitnehmer-status
description: "Statusfeststellung fuer eine geplante Beschaeftigung - Abgrenzung Arbeitnehmer/Selbstaendiger nach § 611a BGB, Scheinselbstaendigkeit, Clearingverfahren § 7a SGB IV, AUeG-Abgrenzung (Leiharbeit vs. Werkvertrag). Ausschliesslich prospektiv - fuer bestehende Verhaeltnisse Aussenberater einschalten."
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

- **BAG, Urt. v. 21.05.2019 – 9 AZR 295/18, NZA 2019, 1558** — Gesamtbildbetrachtung bei der Arbeitnehmereigenschaft: Das BAG stellt klar, dass für die Beurteilung nach § 611a BGB alle Umstände der tatsächlichen Durchführung maßgeblich sind; die vertragliche Bezeichnung als „Freelancer" ist unerheblich, wenn Weisungsgebundenheit und Eingliederung in der Praxis vorliegen.
- **BAG, Urt. v. 17.10.2017 – 9 AZR 792/16, NZA 2018, 173 Rn. 24** — Tatsächliche Durchführung entscheidend: Wie der Vertrag bezeichnet wird (Honorarvertrag, Werkvertrag), ist nach § 611a Abs. 1 S. 5 BGB nicht ausschlaggebend; es kommt auf die gelebte Wirklichkeit an.
- **BSG, Urt. v. 04.09.2018 – B 12 KR 11/17 R, NZA 2019, 275** — Statusfeststellung nach § 7 SGB IV: Das BSG betont, dass auch bei Vorliegen einzelner Selbständigkeitsmerkmale das Gesamtbild für abhängige Beschäftigung sprechen kann, wenn die faktische Eingliederung in die fremde Betriebsorganisation überwiegt.
- **BAG, Urt. v. 14.06.2016 – 9 AZR 305/15, NZA 2016, 1331** — IT-Freelancer in Großprojekten: Werden Softwareentwickler dauerhaft in Entwicklungsteams des Auftraggebers eingebunden und erhalten sie inhaltliche Weisungen über das Jira-System des Auftraggebers, begründet dies regelmäßig Arbeitnehmerstatus.

## Kommentarliteratur

- Wank, in: ErfK, 25. Aufl. 2025, § 611a BGB Rn. 1 ff. (Arbeitnehmerbegriff, Weisungsgebundenheit, tatsächliche Durchführung)
- Thüsing, in: MüKoBGB, 9. Aufl. 2024, § 611a BGB Rn. 80 ff. (Abgrenzungskriterien, Gesamtbildbetrachtung, Missbrauch durch Vertragsgestaltung)
- Schüren, in: HWK, 11. Aufl. 2024, § 1 AÜG Rn. 1 ff. (Abgrenzung Werkvertrag und Arbeitnehmerüberlassung)

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
- Kein „verdeckter" Arbeitnehmer – Offenlegungspflicht in Vertrag (§ 1 Abs. 1 S. 5 AÜG)

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

*Sachverhalt:* Softwareentwickler K soll als „freier Mitarbeiter" für 12 Monate ausschließlich für einen Auftraggeber tätig sein, arbeitet täglich im Büro des Auftraggebers, nutzt dessen Laptop, nimmt an Daily-Standup-Meetings teil, erhält Aufgaben über das Jira-Board des Auftraggebers.

*Ergebnis:* 🔴 Arbeitnehmerstatus sehr wahrscheinlich. Faktoren: Ausschließlichkeit, Eingliederung in Betriebsabläufe, kein eigenes unternehmerisches Risiko, Betriebsmittel gestellt (BAG, Urt. v. 14.06.2016 – 9 AZR 305/15, NZA 2016, 1331). Clearingverfahren § 7a SGB IV dringend empfohlen. Alternativ: reguläres Arbeitsverhältnis oder AÜG-konforme Leiharbeit (mit Erlaubnis).

## Risiken / typische Fehler

- **Vertrag vs. Praxis:** § 611a Abs. 1 S. 5 BGB – Wie der Vertrag heißt, ist unerheblich; entscheidend ist die tatsächliche Durchführung.
- **Rückwirkende Sozialversicherungspflicht** – bis 4 Jahre (§ 25 SGB IV), bei Vorsatz 30 Jahre.
- **AÜG ohne Erlaubnis** – führt zur Entstehung eines Arbeitsverhältnisses kraft Gesetzes (§ 10 AÜG); erhebliche Haftungsrisiken.
- **Prospektiver Charakter** – dieses Plugin prüft nur geplante Strukturen; für bestehende Verhältnisse unbedingt Außenberater und ggf. Clearingstelle einschalten.
- **Gesamtbild-Falle:** Selbst wenn 7 von 10 Kriterien für Selbständigkeit sprechen, kann das Gesamtbild dennoch Arbeitnehmerstatus ergeben, wenn die überwiegende Weisungsgebundenheit faktisch vorliegt.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Wank, in: ErfK, 25. Aufl. 2025, § 611a BGB Rn. 1 ff.
- Thüsing, in: MüKoBGB, 9. Aufl. 2024, § 611a BGB Rn. 80 ff.
- Schüren, in: HWK, 11. Aufl. 2024, § 1 AÜG Rn. 1 ff.
- BAG, Urt. v. 21.05.2019 – 9 AZR 295/18, NZA 2019, 1558
- BAG, Urt. v. 17.10.2017 – 9 AZR 792/16, NZA 2018, 173
- BSG, Urt. v. 04.09.2018 – B 12 KR 11/17 R, NZA 2019, 275
