---
name: inv-reporting-behoerdenstrategie
description: "Inv 011 Reporting, Inv 012 Behoerdenstrategie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 011 Reporting, Inv 012 Behoerdenstrategie

## Arbeitsbereich

Dieser Skill bündelt **Inv 011 Reporting, Inv 012 Behoerdenstrategie** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-011-reporting` | Strukturiert den Abschlussbericht einer Internal Investigation – Aufbau, Privilegierung, Adressaten, Versionen und Verwertbarkeit. |
| `inv-012-behoerdenstrategie` | Entwickelt die Behördenstrategie für Self-Reporting an BaFin, StA, DOJ/SEC – Zeitpunkt, Inhalt, Kooperationsanreize und Risikoabwägung. |

## Arbeitsweg

Für **Inv 011 Reporting, Inv 012 Behoerdenstrategie** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-011-reporting`

**Fokus:** Strukturiert den Abschlussbericht einer Internal Investigation – Aufbau, Privilegierung, Adressaten, Versionen und Verwertbarkeit.

# Abschlussbericht der Internal Investigation

## Rechtlicher Rahmen

Der Abschlussbericht ist das Herzstück jeder Internal Investigation. Er entscheidet darüber, ob Organe ihre Sorgfaltspflichten nach § 93 AktG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html)) erfüllt haben, ob Behörden die Untersuchung als ernsthaft ansehen und ob Regressansprüche gegen Verursacher durchsetzbar sind. Zugleich ist er das gefährlichste Dokument der Untersuchung: Er kann beschlagnahmt (§§ 94, 97 StPO), in US-Discovery herausverlangt oder durch einen Whistleblower weitergegeben werden. Das Anwaltsgeheimnis schützt ihn nur unter bestimmten Bedingungen (vgl. EuGH C-550/07 P, [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE)).

## Ziel dieses Skills

Dieser Skill strukturiert den Abschlussbericht so, dass er belastbar und verwertbar ist, das Unternehmen schützt und die privilegierten Teile von den nicht-privilegierten trennt.

## Arbeitsprogramm

### 1. Berichtsstruktur
- **Executive Summary** (max. 3 Seiten): Sachverhalt, Rechtsbewertung, Ergebnis, Empfehlungen.
- **Sachverhaltsteil**: chronologischer Tatsachenbericht mit Quellenangaben (Dokument, Interview, Seite/Zeitstempel).
- **Rechtsbewertung**: Normsubsumtion, Tatbestandsmerkmale, Indizien, Gegenargumente.
- **Appendices**: Dokumentenverweise, Interviewübersichten (kein Vollprotokoll im Hauptbericht), Forensik-Ergebnisse.
- **Empfehlungen und Remediation**: konkrete Maßnahmen mit Verantwortlichen und Fristen.

### 2. Privilegierungsstrategie: Versionsmodell
- **Vollbericht** (Full Report): unter Anwaltsgeheimnis; nur für Aufsichtsrat/Audit Committee.
- **Faktenbericht** (Fact Report): ohne rechtliche Bewertungen; kann ggf. an Behörden herausgegeben werden, ohne das rechtliche Privilege zu brechen.
- **Executive Summary**: für Vorlage bei Behörden oder Öffentlichkeit; keine Einzelfallinformationen über Beschuldigte ohne Einwilligung.
- Trennung strikt einhalten: Kein Rechtsgutachten im Faktenbericht; kein Faktendetail im Privilegierten Teil, der nicht dort hingehört.

### 3. Quellenangaben und Nachprüfbarkeit
- Jede Tatsachenbehauptung muss mit einer Quelle belegt sein (Dokument mit Bates-Nummer, Interview mit Datum und Person).
- Keine unbelegt gebliebenen Verdächtigungen im Bericht.
- Gegendarstellungen der betroffenen Personen dokumentieren.
- Rechtsprechungszitate: nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

### 4. Adressaten und Verteiler
- Wer erhält welche Version? Klare Verteilermatrix.
- Aufsichtsrat: Vollbericht.
- Vorstand (wenn nicht betroffen): Executive Summary.
- BaFin, Staatsanwaltschaft: nur Faktenbericht nach Privilegierungsprüfung.
- Betriebsrat: kein Anspruch auf Einsicht in privilegierte Untersuchungsunterlagen (§ 80 BetrVG reicht nicht für vollständige Offenlegung).

### 5. Persönlichkeitsrechte und DSGVO im Bericht
- Betroffene Mitarbeiter: Grundsatz der Verhältnismäßigkeit – nur erforderliche personenbezogene Daten im Bericht.
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten muss verhältnismäßig bleiben ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)).
- Unschuldsvermutung (Art. 6 Abs. 2 EMRK): im Bericht keine Verurteilung ohne rechtskräftige Entscheidung.
- Recht auf Gegendarstellung vor Abschluss des Berichts.

### 6. Qualitätssicherung
- Peer Review durch zweiten Anwalt (Four-Eyes-Prinzip).
- Faktencheck: sind alle im Bericht genannten Tatsachen durch Dokumente oder Interviews belegt?
- Falschangaben im Bericht gegenüber Behörden: Strafbarkeit nach § 145d StGB (Vortäuschen einer Straftat), § 164 StGB (falsche Verdächtigung).

### 7. Nachfolgende Verfahren
- Bericht als Grundlage für Kündigung: Verwertbarkeit im Kündigungsschutzverfahren (§ 1 KSchG).
- Bericht als Grundlage für Schadensersatz: § 93 Abs. 2 AktG, § 249 BGB.
- Bericht bei BaFin Self-Reporting: Inhalt und Zeitpunkt strategisch abstimmen (vgl. inv-012-behoerdenstrategie).

## Red-Team-Fragen

- Ist die Privilegierungsstrategie wasserdicht – sind Fakten- und Rechtsteil tatsächlich getrennt?
- Enthält der Bericht Behauptungen, die nicht durch Dokumente oder Interviews belegt sind?
- Wurden betroffene Mitarbeiter vor Fertigstellung des Berichts mit den Vorwürfen konfrontiert und hatten die Möglichkeit zur Gegendarstellung?
- Wer hat außer dem Anwalt Zugang zum Vollbericht gehabt, und hat das den Privilegeschutz gefährdet?
- Ist die Verteilermatrix dokumentiert und eingehalten worden?
- Könnten Formulierungen im Bericht als falsche Verdächtigung (§ 164 StGB) qualifizieren?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 93 AktG | Sorgfaltspflicht Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 97 StPO | Beschlagnahmeschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html) |
| § 164 StGB | Falsche Verdächtigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__164.html) |
| EuGH C-550/07 P | Akzo Nobel Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |

## Ausgabeformate

- **Berichtsstruktur-Template** (Executive Summary, Sachverhalt, Rechtsbewertung, Empfehlungen)
- **Verteilermatrix** (Version × Adressat × Privilegierungshinweis)
- **Quellenverzeichnis-Vorlage** (Bates-Nummern, Interviews, Dokumente)
- **Gegendarstellungs-Checkliste** für betroffene Mitarbeiter

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-012-behoerdenstrategie`

**Fokus:** Entwickelt die Behördenstrategie für Self-Reporting an BaFin, StA, DOJ/SEC – Zeitpunkt, Inhalt, Kooperationsanreize und Risikoabwägung.

# Behördenstrategie und Self-Reporting

## Rechtlicher Rahmen

Self-Reporting an Behörden ist eine der folgenschwersten Entscheidungen in einer Internal Investigation. Es gibt keine allgemeine gesetzliche Pflicht zum proaktiven Self-Reporting in Deutschland, aber zahlreiche sektorbezogene Meldepflichten (z. B. § 24 KWG für Banken, § 53 WpHG, MAR Art. 19 bei Insiderhandel). Proaktive Kooperation kann Bußgelder nach §§ 30, 17 Abs. 4 OWiG erheblich reduzieren ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__30.html)) und nach DOJ Corporate Enforcement Policy die Strafverfolgung abwenden. Falschinformationen gegenüber der BaFin können nach § 54 KWG oder § 119 WpHG strafbar sein.

## Ziel dieses Skills

Dieser Skill entwickelt eine maßgeschneiderte Behördenstrategie, die Kooperationsanreize nutzt, ohne unkontrolliert Zugeständnisse zu machen oder Privilegeschutz zu opfern.

## Arbeitsprogramm

### 1. Behördenlandschaft identifizieren
- **BaFin**: zuständig für Marktmissbrauch (MAR), Geldwäsche (GwG), Kapitalmarktrecht.
- **Staatsanwaltschaft**: Strafverfolgung nach StGB, insb. §§ 266 (Untreue), 263 (Betrug), 299 (Bestechung), 332 (Bestechlichkeit im Amt).
- **DOJ/SEC (USA)**: FCPA-Verstöße, Sanktionsverstöße (OFAC), Wertpapierbetrug.
- **Bundeskartellamt**: Kartellverstöße (§§ 1, 19 GWB).
- **Zollkriminalamt/BAFA**: Exportkontrolle.
- **Datenschutzbehörden**: DSGVO-Verstöße.

### 2. Meldepflichten prüfen
- §§ 43, 44 GwG: Verdachtsmeldepflicht bei Geldwäsche ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/__43.html)).
- Art. 19 MAR: Ad-hoc-Meldepflicht bei Insiderinformationen ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596)).
- § 24 KWG: Anzeigepflichten der Banken.
- HinSchG §§ 12, 13: Pflicht zur Einrichtung von Meldestellen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/)).
- DSGVO Art. 33: 72-Stunden-Meldung bei Datenpannen.

### 3. Kooperationsanreize
- **OWiG § 17 Abs. 4**: Abschöpfung kann das gesamte Unternehmensvermögen erfassen, aber bei Kooperation Ermessenssenkung.
- **§ 30 OWiG**: Unternehmensbußgeld bis 10 Mio. EUR (regulär), aber Kronzeugenregelung senkt Risiko.
- **DOJ Corporate Enforcement Policy (CEP)**: Voluntary disclosure + full cooperation + remediation = Abwägung zugunsten des Unternehmens (Declination möglich).
- **SEC Cooperation Framework**: Substantial assistance reduziert Sanktionen.
- **BaFin**: keine formelle Kronzeugenregel, aber Kooperationsbereitschaft fließt in Ermessensausübung ein.

### 4. Self-Reporting-Entscheidung
- Wann melden? Vor oder nach Abschluss der internen Untersuchung?
- Risiko des frühen Meldens: Behörde hat Wissensvorsprung und kann eigene Untersuchung ankündigen.
- Risiko des späten Meldens: Behörde entdeckt Verstoß selbst → Kooperationsbonus entfällt.
- „Race to the government": wenn Whistleblower droht, vorab zu melden, muss das Unternehmen handeln.

### 5. Inhalt der Meldung
- Was wird offenbart? Fakten, nicht Rechtsgutachten (Privilegeschutz wahren).
- Privileg-Waiver vermeiden: Mündliche Präsentation bevorzugen; kein vollständiger Bericht übergeben.
- Selective Waiver: in Deutschland möglich, in den USA umstritten – Abstimmung mit US Counsel zwingend.
- Proffer Agreement (USA): Schutz der offenbarten Informationen vor direkter Verwendung im Strafverfahren vereinbaren.

### 6. BaFin-Spezifika
- BaFin kann nach §§ 4, 6 WpHG eigene Ermittlungen einleiten.
- Beschränkung des Auskunftsrechts der BaFin durch Unternehmen möglich, wenn es sich selbst belasten würde (nemo tenetur).
- Praxis: schriftliche Mitteilung mit Faktenüberblick, gefolgt von Rechtsgespräch ([bafin.de](https://www.bafin.de/)).

### 7. Internationale Koordination
- DOJ/BaFin/StA müssen koordiniert werden – widersprechende Aussagen sind katastrophal.
- „One team" aus deutschen und US-Anwälten mit klarer Kommunikationslinie.
- Amnesty-Programme: Kartell (Bonusantrag), FCPA DPA/NPA als Ziel.

## Red-Team-Fragen

- Wurde eine Pflicht zum Self-Reporting geprüft, bevor proaktiv gemeldet wurde?
- Wurden Kooperationsvorteile konkret berechnet (Bußgeldreduktion vs. Offenbarungsrisiko)?
- Ist der Inhalt der Meldung so formuliert, dass der Privileg-Schutz erhalten bleibt?
- Besteht ein Whistleblower-Risiko, das das Timing der Meldung beeinflusst?
- Sind alle beteiligten Behörden (BaFin, StA, DOJ, SEC) koordiniert – insbesondere bei widersprüchlichen Anforderungen?
- Wurde der Vorstand über das Meldungsrisiko und die Entscheidungsoptionen vollständig informiert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 30 OWiG | Verbandsgeldbuße | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__30.html) |
| § 17 OWiG | Bußgeldbemessung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__17.html) |
| § 43 GwG | Verdachtsmeldung Geldwäsche | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/__43.html) |
| Art. 19 MAR | Ad-hoc-Meldepflicht | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596) |
| HinSchG | Hinweisgeberschutz 2023 | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |

## Ausgabeformate

- **Behördenmatrix** (Zuständigkeit × Meldepflicht × Kooperationsanreize)
- **Self-Reporting-Entscheidungsbaum**
- **Meldungs-Kurzfassung** (Fakten ohne Rechtsgutachten)
- **DOJ/SEC-Kooperationsplan**
- **BaFin-Gesprächsvorbereitung**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
