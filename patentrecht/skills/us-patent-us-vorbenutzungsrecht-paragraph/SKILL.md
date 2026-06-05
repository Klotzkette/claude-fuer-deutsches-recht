---
name: us-patent-us-vorbenutzungsrecht-paragraph
description: "US Patent US Vorbenutzungsrecht Paragraph: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# US Patent US Vorbenutzungsrecht Paragraph

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **US Patent US Vorbenutzungsrecht Paragraph** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `us-patent-law-pto-ptab` | Orientiert deutsche Teams im US-Patentrecht: Patentability, claim drafting, IDS, office action, continuation, reissue, reexamination, IPR/PGR vor PTAB und Local-Counsel-Briefing. |
| `us-patent-litigation-district-court-itc` | Bereitet US-Patentlitigation aus deutscher Sicht vor: complaint, answer, claim construction, discovery, Markman, damages, injunction, ITC exclusion order und Settlement-Druck. |
| `vorbenutzungsrecht-paragraph-12-patg` | Prüft Vorbenutzungsrecht nach § 12 PatG: Besitzstand vor Anmeldung/Priorität, Benutzung oder ernsthafte Veranstaltungen, Inland, Redlichkeit, Umfang, Beweisführung und Prozessstrategie. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **US Patent US Vorbenutzungsrecht Paragraph**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `us-patent-law-pto-ptab`

**Fokus:** Orientiert deutsche Teams im US-Patentrecht: Patentability, claim drafting, IDS, office action, continuation, reissue, reexamination, IPR/PGR vor PTAB und Local-Counsel-Briefing.

# US-Patentrecht: USPTO und PTAB

## Aufgabe

US-spezifische Patentamts- und PTAB-Themen ohne deutschen Automatismus.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **US-Ziel klären: Prosecution, FTO, PTAB-Angriff oder Litigation Support.**
2. **Claims auf US-Eligibility, novelty, non-obviousness und written description/external support sensibel prüfen.**
3. **IDS-/Prior-Art- und Family-Consistency-Fragen sammeln.**
4. **Office-Action-Response oder PTAB-Petition als Arbeitsauftrag strukturieren.**
5. **US Counsel Fragen, Deadlines und Dokumente vorbereiten.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- US Patent Issue List.
- Office Action Response Outline.
- PTAB Briefing Sheet.
- DE/EN Client Note.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 2. `us-patent-litigation-district-court-itc`

**Fokus:** Bereitet US-Patentlitigation aus deutscher Sicht vor: complaint, answer, claim construction, discovery, Markman, damages, injunction, ITC exclusion order und Settlement-Druck.

# US-Patentprozess: District Court und ITC

## Aufgabe

US-Durchsetzung und Verteidigung mit Discovery-, Claim-Construction- und Kostenrealität.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Forum klären: District Court, ITC oder PTAB-Kombination.**
2. **Accused products, asserted claims und prior art in Litigation Matrix bringen.**
3. **Discovery-Belastung, hold notices und privilege issues markieren.**
4. **Claim construction/Markman-Begriffe aus deutscher Akte übersetzen.**
5. **Damages, injunction und Settlement-Fenster modellieren.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- US Litigation Readiness Memo.
- Markman Term List.
- Discovery Risk Map.
- ITC/District Court Comparison.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `vorbenutzungsrecht-paragraph-12-patg`

**Fokus:** Prüft Vorbenutzungsrecht nach § 12 PatG: Besitzstand vor Anmeldung/Priorität, Benutzung oder ernsthafte Veranstaltungen, Inland, Redlichkeit, Umfang, Beweisführung und Prozessstrategie.

# Vorbenutzungsrecht § 12 PatG

## Prüfraster

1. **Zeitpunkt:** vor Anmelde- oder Prioritätstag.
2. **Inland:** Benutzung oder Veranstaltungen im Inland.
3. **Besitzstand:** tatsächliche Benutzung oder ernsthafte und greifbare Vorbereitung.
4. **Erfindungsidentität:** Benutzung muss die spätere geschützte Lehre betreffen.
5. **Redlichkeit:** keine unredliche Kenntniserlangung.
6. **Umfang:** Schutz nur im bisherigen oder durch Vorbereitung angelegten Umfang.
7. **Beweise:** alte Zeichnungen, Bestellungen, Laborbücher, Prototypen, Rechnungen, E-Mails, Zeugen, Lieferanten.

## Aktenarbeit

Baue eine Chronologie:

| Datum | Ereignis | Dokument/Zeuge | Beweisqualität | Bedeutung |
| --- | --- | --- | --- | --- |

## Output

- Vorbenutzungs-Memo.
- Beweismatrix.
- Risiken für Unterlassung und Auskunft.
- Vergleichs- und Prozessstrategie.

## Vorsicht

Vorbenutzungsrecht ist kein allgemeiner Freibrief. Es schützt nicht automatisch spätere Weiterentwicklungen, andere Konzernunternehmen oder neue Produktgenerationen.

## Pflicht-Normen und Praxisprobleme

- **§ 12 Abs. 1 PatG:** Wer die Erfindung im Inland vor dem Anmeldetag/Prioritätstag in Benutzung genommen oder die dazu erforderlichen Veranstaltungen getroffen hat, hat ein persönliches Recht zur Weiterbenutzung. Persönliches Recht — nicht übertragbar (§ 12 Abs. 2 PatG).
- **§ 12 Abs. 2 S. 2 PatG Ausnahme:** Im Falle der Veräußerung oder Verpachtung des Geschäftsbetriebs geht das Vorbenutzungsrecht auf den Erwerber/Pächter über.
- **"Im Inland":** § 12 PatG erfordert Inlandsbenutzung. Bei EP-Bundle: Vorbenutzung im jeweiligen Validierungsland; Einheitspatent UP: Vorbenutzung im jeweiligen UPC-Land Art. 28 UPCA.
- **"Ernsthafte Veranstaltungen":** mehr als bloße interne Vorbereitung; konkrete Produktentwicklung, Bestellungen, Werkzeugbau. BGH "Wundverband" GRUR 2010, 47 als Leitlinie (Az. live verifizieren).
- **Umfang § 12 Abs. 1 S. 2 PatG:** Nur im Umfang der bestehenden oder angelegten Benutzung. Erweiterungen ohne Erweiterung der Veranstaltungen sind nicht gedeckt.
- **Beweislast:** Vorbenutzer trägt sie. Schwierigkeitsgrad steigt mit zeitlichem Abstand.
- **Vorbenutzungsrecht als Einrede im Verletzungsprozess:** in § 12 PatG verankert; Vorbenutzungsrecht ist KEIN Nichtigkeitsgrund.
- **Internationale Strategie:** Im Schutzrechtsprozess das Vorbenutzungsrecht als prozessuale Einrede ausspielen; parallel die Nichtigkeitsklage erwägen (§ 22 PatG Nichtigkeit / EPÜ Einspruch).
- Falle: Konzern-internes Joint Venture als "ein Geschäftsbetrieb" einstufen — § 12 Abs. 2 PatG eng auslegen; Auseinanderfallen rechtlicher und wirtschaftlicher Zuordnung gefährdet Vorbenutzungsrecht.
