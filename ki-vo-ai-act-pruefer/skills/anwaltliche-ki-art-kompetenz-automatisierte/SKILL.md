---
name: anwaltliche-ki-art-kompetenz-automatisierte
description: "Anwaltliche KI ART Kompetenz Automatisierte: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anwaltliche KI ART Kompetenz Automatisierte

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Anwaltliche KI ART Kompetenz Automatisierte** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anwaltliche-ki-nutzung-quellencheck-brao` | Anwaltliche KI-Nutzung ohne Halluzinationsschaden: Quellencheck, § 43a BRAO, Wahrheitspflicht/Sachlichkeit, Mandatsgeheimnis, DSGVO, Schriftsatzkontrolle, Prompt-Governance und Freigabevermerk fuer Kanzlei und Rechtsabteilung. |
| `art-4-ki-kompetenz-schulungsprogramm` | Art. 4 KI-VO als praktisches Schulungs- und Nachweissystem: Rollendifferenzierte AI-Literacy fuer Vorstand, Legal, IT, HR, Fachabteilung, Einkauf, Support und externe Dienstleister; mit Kompetenzmatrix, Pflichtenkalender, Schulungsnachweisen, Shadow-AI-Schnittstelle und Audit-Readiness. |
| `automatisierte-entscheidung-dsgvo-art-22-schnittstelle` | Schnittstelle KI-VO und DSGVO Art. 22: automatisierte Einzelentscheidung, Profiling, menschliche Beteiligung, Bewerber/Kredit/Kundenranking, Informationspflicht, DPIA, Rechtsgrundlage und technische Governance. |
| `begrenztes-risiko-art-50-transparenzpflichten` | Unternehmen setzt Chatbot Deepfake-Tool oder KI-Textgenerator ein und fragt: Welche Hinweispflichten treffen uns gegenüber Nutzern? Art. 50 KI-VO begrenztes Risiko. Prüfraster: Chatbot-Hinweispflicht Art. 50 Abs. 1 KI-VO Deepfake-Kennzeichnungspflicht Art. 50 Abs. 4 KI-VO KI-generierter Text bei öffentlichem Interesse Art. 50 Abs. 2 KI-VO Emotionserkennung Art. 50 Abs. 3 KI-VO. Output: Checkliste Pflichten und Musterkennzeichnungstexte. Abgrenzung zu verbotene-praktiken-art-5 (Hochrisiko-Verbote) und begrenztes-risiko ist kein Hochrisiko. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Anwaltliche KI ART Kompetenz Automatisierte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anwaltliche-ki-nutzung-quellencheck-brao`

**Fokus:** Anwaltliche KI-Nutzung ohne Halluzinationsschaden: Quellencheck, § 43a BRAO, Wahrheitspflicht/Sachlichkeit, Mandatsgeheimnis, DSGVO, Schriftsatzkontrolle, Prompt-Governance und Freigabevermerk fuer Kanzlei und Rechtsabteilung.

# Anwaltliche KI-Nutzung und Quellencheck

## Ziel

Der Skill verhindert, dass KI-generierte Texte mit erfundenen Fundstellen, fallfremden Textbausteinen oder ungeprüften Tatsachen in Schriftsätzen, Gutachten oder Mandantenkommunikation landen.

## Pflichtprüfung

1. **Tatsachen:** Stammt die Tatsache aus der Akte, aus Mandantenangaben oder aus eigener Recherche?
2. **Normen:** Ist die Norm aktuell und einschlägig?
3. **Rechtsprechung:** Gericht, Entscheidungsdatum, Aktenzeichen und frei prüfbare Fundstelle vorhanden?
4. **Literatur:** Nur nennen, wenn tatsächlich zugänglich und geprüft; sonst weglassen.
5. **Berufsrecht:** Keine bewusst unwahren Angaben, keine unsachliche Verzerrung, keine Quellenerfindung.
6. **Geheimnis:** Keine Mandatsdaten in nicht freigegebene KI-Systeme.
7. **Freigabe:** Menschliche juristische Endkontrolle dokumentieren.

## Red-Team-Fragen

- Gibt es Zitate, die zu schön klingen?
- Passen Aktenzeichen, Datum und Rechtsgebiet zusammen?
- Taucht dieselbe Entscheidung in einer offiziellen oder freien Datenbank auf?
- Sind Textbausteine aus einem anderen Mandat sichtbar?
- Hat die KI einen starken Vortrag erfunden, der nicht von der Akte getragen wird?

## Output

Erzeuge einen **KI-Nutzungsvermerk**:

- verwendetes Tool und Zweck;
- keine oder welche Mandatsdaten genutzt wurden;
- geprüfte Quellenliste;
- gestrichene unsichere Fundstellen;
- verantwortliche Endfreigabe.

## Merksatz

KI darf die Arbeit beschleunigen. Sie darf nie die anwaltliche Verantwortung ersetzen.

## 2. `art-4-ki-kompetenz-schulungsprogramm`

**Fokus:** Art. 4 KI-VO als praktisches Schulungs- und Nachweissystem: Rollendifferenzierte AI-Literacy fuer Vorstand, Legal, IT, HR, Fachabteilung, Einkauf, Support und externe Dienstleister; mit Kompetenzmatrix, Pflichtenkalender, Schulungsnachweisen, Shadow-AI-Schnittstelle und Audit-Readiness.

# Art. 4 KI-VO — KI-Kompetenz als Compliance-Programm

## Arbeitsauftrag

Dieser Skill baut aus Art. 4 KI-VO kein Folienversprechen, sondern ein beweisbares Schulungs- und Kompetenzsystem. Ziel ist ein kurzer, operationalisierbarer Plan, der zeigt, wer im Unternehmen KI nutzt, welche Risiken dort entstehen und wie die Organisation nachweist, dass die beteiligten Personen ausreichend angeleitet wurden.

## Normanker

- Art. 4 KI-VO: Anbieter und Betreiber muessen KI-Kompetenz sicherstellen.
- Art. 3 Nr. 1, 3, 4, 63 KI-VO: KI-System, Anbieter, Betreiber, GPAI.
- Art. 6, Art. 26, Art. 27, Art. 50 KI-VO: Folgepflichten je nach Einsatz.
- DSGVO, Geheimnisschutz, Urheberrecht und Berufsrecht nur als Schnittstellen markieren, nicht vermischen.

## Intake

Frage knapp:

1. Welche KI-Werkzeuge werden genutzt: freier Chatbot, Enterprise-Chat, Fachsoftware, Recruiting, Kredit, Medizin, Justiz, Verwaltung, Entwickler-Tool?
2. Wer nutzt sie: Vorstand, Legal, HR, Vertrieb, Produkt, IT, Support, Auszubildende, Externe?
3. Gibt es Anhang-III-Naehe: Personal, Bildung, Kredit, Justiz, Migration, Strafverfolgung, kritische Infrastruktur, Biometrie?
4. Welche Daten duerfen hinein und welche nie: personenbezogene Daten, Mandatsgeheimnisse, Betriebsgeheimnisse, Quellcode, Gesundheitsdaten?
5. Welche Nachweise existieren: Policy, Teilnahmeprotokoll, Rollenkonzept, Test, Freigabe, Incident-Log?

## Kompetenzmatrix

Erzeuge eine Tabelle:

| Rolle | Mindestwissen | Verbotene Nutzung | Pflichtskills | Nachweis |
|---|---|---|---|---|
| Geschäftsleitung | Haftungs- und Risikoklassenlogik, Budget, Governance | Blindfreigabe ohne Verantwortliche | Art. 3/6/99, Incident-Eskalation | Beschluss, Schulungszertifikat |
| Legal/Compliance | Rechtsrahmen, Quellencheck, Beweisakte | ungeprüfte Fundstellen, falsche Konformitätsaussagen | Evidence-Pack, Vendor-DD | Prüfvermerk |
| HR | Anhang III Beschäftigung, Diskriminierung, Mitbestimmung | Ranking/Screening ohne Zweckfreigabe | HR-Hochrisiko, Bias, Art. 22 DSGVO | Betriebsrats- und DPIA-Akte |
| IT/Security | Logging, Zugriff, Cyber, Modellgrenzen | offene API ohne Mandantentrennung | Art. 12/15, Security-Gate | Architektur- und Lognachweis |
| Fachabteilung | zulässige Prompts, Freigabegrenzen | Shadow-AI, personenbezogene Daten in Consumer-Tools | Use-Case-Check | Kurztest, Prompt-Policy |

## Output

Liefere:

- Schulungsplan fuer 30/60/90 Tage.
- Einseitige KI-Nutzungsregel fuer Mitarbeitende.
- Nachweismatrix fuer Audits und Marktaufsicht.
- Trigger, wann neu geschult werden muss: neues Tool, neuer Use Case, Anhang-III-Naehe, Incident, Rollenwechsel, neue Leitlinie/Norm.

## Qualitätsregel

Keine pauschale Aussage "alle muessen KI-Schulung machen". Immer Rolle, Risiko und tatsaechliche Nutzung verbinden. Bei Live-Output aktuelle KI-VO-Fassung und veroeffentlichte EU-Leitlinien pruefen.

## 3. `automatisierte-entscheidung-dsgvo-art-22-schnittstelle`

**Fokus:** Schnittstelle KI-VO und DSGVO Art. 22: automatisierte Einzelentscheidung, Profiling, menschliche Beteiligung, Bewerber/Kredit/Kundenranking, Informationspflicht, DPIA, Rechtsgrundlage und technische Governance.

# KI-VO und DSGVO Art. 22

## Warum dieser Skill

Ein KI-System kann nach KI-VO nicht Hochrisiko sein und trotzdem datenschutzrechtlich hochproblematisch. Umgekehrt ersetzt KI-VO-Compliance keine DSGVO-Prüfung.

## Prüfraster

1. Werden personenbezogene Daten verarbeitet?
2. Gibt es Profiling?
3. Gibt es eine ausschließlich automatisierte Entscheidung mit rechtlicher oder ähnlich erheblicher Wirkung?
4. Ist der Mensch nur formale Abnickstelle oder echte Kontrollinstanz?
5. Welche Rechtsgrundlage und Informationspflichten gelten?
6. Braucht es eine Datenschutz-Folgenabschätzung?
7. Welche Betroffenenrechte und Widerspruchswege gibt es?

## Typische Fälle

- Bewerberranking.
- Kredit-Scoring.
- Betrugsverdacht.
- Kundenkündigung.
- Studienzulassung.
- Versicherungsprämie.

## Output

- Schnittstellenvermerk KI-VO/DSGVO.
- Human-Review-Design.
- Betroffeneninformation.
- DPIA-Fragenkatalog.

## Warnung

"Mensch prüft final" reicht nur, wenn der Mensch reale Informationen, Zeit, Kompetenz und Befugnis hat, vom KI-Vorschlag abzuweichen.

## 4. `begrenztes-risiko-art-50-transparenzpflichten`

**Fokus:** Unternehmen setzt Chatbot Deepfake-Tool oder KI-Textgenerator ein und fragt: Welche Hinweispflichten treffen uns gegenüber Nutzern? Art. 50 KI-VO begrenztes Risiko. Prüfraster: Chatbot-Hinweispflicht Art. 50 Abs. 1 KI-VO Deepfake-Kennzeichnungspflicht Art. 50 Abs. 4 KI-VO KI-generierter Text bei öffentlichem Interesse Art. 50 Abs. 2 KI-VO Emotionserkennung Art. 50 Abs. 3 KI-VO. Output: Checkliste Pflichten und Musterkennzeichnungstexte. Abgrenzung zu verbotene-praktiken-art-5 (Hochrisiko-Verbote) und begrenztes-risiko ist kein Hochrisiko.

# Begrenztes Risiko — Transparenzpflichten nach Art. 50 KI-VO

## Zweck

KI-Systeme mit begrenztem Risiko unterliegen keinen umfangreichen Vorab-Pflichten wie Hochrisiko-Systeme, aber sie unterliegen Transparenzpflichten gegenüber den Nutzern. Art. 50 KI-VO enthält drei Kategorien von Transparenzpflichten.

## Kategorie 1 — Chatbot-Hinweispflicht (Art. 50 Abs. 1 KI-VO)

**Anwendungsbereich:** Anbieter von KI-Systemen, die direkt mit natürlichen Personen interagieren (Chatbots, virtuelle Assistenten).

**Pflicht:** Sicherstellen, dass natürliche Personen darüber informiert werden, dass sie mit einem KI-System interagieren — es sei denn, dies ist aufgrund der Umstände und des Kontexts offensichtlich.

**Prüffragen:**
- Handelt es sich um ein System, das in natürlicher Sprache mit Menschen interagiert?
- Wissen die Nutzer, dass sie mit einem KI-System sprechen?
- Ist es aus dem Kontext heraus offensichtlich (z.B. explizit als Chatbot vermarktet)?

**Ausnahme:** Wenn offensichtlich ist, dass ein KI-System interagiert (z.B. durch die Plattformgestaltung oder Produktbeschreibung), entfällt die aktive Hinweispflicht.

**Form des Hinweises:** Die KI-VO schreibt keine bestimmte Form vor. Der Hinweis muss jedoch klar und verständlich sein. Empfehlung: Hinweis zu Beginn der Interaktion, nicht in den AGB vergraben.

**Ausnahme für Strafverfolgung:** Art. 50 Abs. 5 KI-VO ermöglicht es Strafverfolgungsbehörden unter engen Voraussetzungen, den Hinweis nicht zu erteilen, wenn die Aufgabe dies erfordert.

## Kategorie 2 — Deepfake-Kennzeichnungspflicht (Art. 50 Abs. 2 KI-VO)

**Anwendungsbereich:** Betreiber (nicht Anbieter) von KI-Systemen, die Bild-, Audio-, Video- oder Textinhalte erzeugen, die täuschend echten echten Personen, Orten oder Gegenständen ähneln.

**Pflicht:** Die Inhalte als KI-generiert oder KI-manipuliert zu kennzeichnen, auf eine für den Empfänger der Inhalte erkennbare Weise — maschinell lesbar und erkennbar für Dritte.

**Ausnahmen (Art. 50 Abs. 2 Unterabsatz 2 KI-VO):**
- Inhalte, die zum offensichtlich künstlerischen, kreativen, satirischen oder fiktionalen Ausdruck gehören, wenn sie als solche eindeutig kenntlich gemacht sind
- Inhalte, die für Zwecke der öffentlichen Sicherheit oder nationalen Sicherheit genutzt werden

**Prüffragen:**
- Erzeugt das System Bilder, Videos, Audio oder Text, die als von realen Personen stammend wirken könnten?
- Wird der Inhalt öffentlich verbreitet?
- Handelt es sich um offensichtliche Satire oder Kunst (dann ggf. Ausnahme)?

## Kategorie 3 — KI-generierter Text bei öffentlichem Interesse (Art. 50 Abs. 3 KI-VO)

**Anwendungsbereich:** Anbieter und Betreiber von KI-Systemen, die Text in erheblichem Umfang generieren, der öffentliche Interessen berührt (insbesondere Wahlen, öffentliche Debatten, politische Propaganda).

**Pflicht:** Sicherstellung, dass KI-generierter Text als solcher erkennbar gemacht wird, wenn er öffentlich verbreitet wird.

**Prüffragen:**
- Generiert das System Texte, die öffentliche Interessen berühren?
- Werden die Texte öffentlich verbreitet, ohne als KI-generiert kenntlich gemacht zu sein?

## Kategorie 4 — Emotionserkennung und biometrische Kategorisierung (Art. 50 Abs. 4 KI-VO)

**Anwendungsbereich:** Anbieter und Betreiber von Emotionserkennungs- oder biometrischen Kategorisierungssystemen.

**Pflicht:** Unterrichtung der betroffenen natürlichen Personen über den Betrieb des Systems.

**Hinweis:** Emotionserkennung am Arbeitsplatz und in Bildungseinrichtungen ist verboten (Art. 5 Abs. 1 lit. f KI-VO). Art. 50 Abs. 4 KI-VO gilt nur für Einsatzszenarien, die nicht unter Art. 5 fallen.

## Technische Umsetzung

Für maschinell lesbare Kennzeichnung empfiehlt die Kommission den Einsatz von Standards wie C2PA (Content Credentials) oder ähnlichen Metadaten-Standards. Harmonisierte Normen sind noch in Entwicklung.

## Sanktionen bei Verstößen

Verstöße gegen Art. 50 KI-VO können mit Bußgeldern bis zu 15 Mio EUR oder drei Prozent des weltweiten Jahresumsatzes geahndet werden (Art. 99 Abs. 4 KI-VO).

## Faktische Updates (Stand 05/2026)

- **02.08.2026 — Anwendung Art. 50 KI-VO:** Die Transparenzpflichten nach Art. 50 KI-VO werden ab dem 02.08.2026 verbindlich (Art. 113 lit. c KI-VO). Anbieter und Betreiber muessen Kennzeichnungs- und Hinweissysteme bis zu diesem Stichtag implementiert haben.
- **C2PA-Standards / maschinenlesbare Kennzeichnung:** Fuer die maschinenlesbare Kennzeichnung von Deepfakes / synthetischen Inhalten (Art. 50 Abs. 2 KI-VO) sind harmonisierte Normen in Vorbereitung (CEN/CENELEC). C2PA Content Credentials gilt als de-facto-Standard, ist aber noch nicht harmonisiert. Stand live pruefen.
- **Schnittstelle zu UrhG, UWG, MStV:** Bei Deepfakes / Persoenlichkeitsbild beachten: § 22 KUG, § 823 BGB i.V.m. § 1004 BGB analog, §§ 5/5a UWG (Irrefuehrung), § 5 Abs. 6 MStV (medienrechtliche Kennzeichnungspflicht). KI-VO ergaenzt, ersetzt diese Vorschriften nicht.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — BEGRENZTES RISIKO ART 50 TRANSPARENZPFLICHTEN
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 50 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
