---
name: soldatengesetz-rechtsstellung
description: "Soldatengesetz Rechtsstellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Soldatengesetz Rechtsstellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Soldatengesetz Rechtsstellung** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `soldatengesetz-rechtsstellung-grundpflichten` | Soldatengesetz Rechtsstellung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `soldatenversorgungsgesetz-beschaedigtenversorgung` | Soldatenversorgungsgesetz Beschädigtenversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `status-soldat-beamter-zivilbeschaeftigter-klaeren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Status Soldat Beamter Zivilbeschäftigter klären. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Soldatengesetz Rechtsstellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `soldatengesetz-rechtsstellung-grundpflichten`

**Fokus:** Soldatengesetz Rechtsstellung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Soldatengesetz – Rechtsstellung und Grundpflichten

## Fachkern: Soldatengesetz – Rechtsstellung und Grundpflichten
- **Spezialgegenstand:** Soldatengesetz – Rechtsstellung und Grundpflichten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Das Soldatengesetz (SG) regelt das öffentlich-rechtliche Dienst- und Treueverhältnis des Soldaten zum Bund. Es definiert Status, Grundpflichten und Grundrechte des Soldaten. Anders als beim Beamten besteht keine Verwaltungsgerichtsbarkeit nach VwGO als Regelweg, sondern primär WBO-Beschwerdeweg und Truppendienstgericht. Der Skill ordnet ein, welche Pflicht aus dem SG einschlägig ist und welcher Rechtsweg eröffnet ist.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Status des Mandanten: Berufssoldat, Soldat auf Zeit (SaZ), freiwillig Wehrdienstleistender (FWDL), Reservist im Wehrdienstverhältnis?
- Welche Pflicht ist im Raum (§§ 7–17a SG)? Treuepflicht, Gehorsam, Wahrheitspflicht, Kameradschaft, Achtungs- und Vertrauenswürdigkeit, Mäßigung?
- Liegt bereits ein Hinweis, eine Anhörung, ein Disziplinarvorgang oder eine Beschwerde vor?
- Welche Frist läuft (WBO 1 Monat ab Kenntnis, WDO Verjährung)?
- Gibt es einen Bezug zu einer politischen oder presseöffentlichen Äußerung?

## Rechtlicher Rahmen

- § 6 SG: Staatsbürgerliche Rechte des Soldaten – Grundrechtsgenuss mit Einschränkungen.
- § 7 SG: Treuepflicht zur freiheitlichen demokratischen Grundordnung.
- § 8 SG: Eintreten für die demokratische Grundordnung (auch außerdienstlich).
- § 10 SG: Pflichten des Vorgesetzten (Fürsorge, Vorbildlichkeit, Aufsicht).
- § 11 SG: Gehorsam – Befehl nur in Grenzen der Menschenwürde, des Strafrechts und der dienstlichen Zwecke.
- § 12 SG: Kameradschaft.
- § 13 SG: Wahrheitspflicht in dienstlichen Angelegenheiten.
- § 14 SG: Verschwiegenheitspflicht.
- § 15 SG: Politische Betätigung – Mäßigungsgebot.
- § 17 SG: Verhalten im und außer Dienst – Achtungs- und Vertrauenswürdigkeit.
- § 17a SG: Gesundes Erscheinungsbild, Uniform.
- Rechtsschutz: WBO (Beschwerde, weitere Beschwerde, Antrag auf gerichtliche Entscheidung), WDO (Disziplinarverfahren).

## / Schritt für Schritt

1. **Status klären.** Berufssoldat oder SaZ? Datum der Ernennung, Dienstzeitende, Dienstgrad, Truppenteil, Disziplinarvorgesetzter.
2. **Pflichtenkollision identifizieren.** Welche Norm aus §§ 7–17a SG ist tangiert? Gegebenenfalls mehrere parallel (Mäßigung § 15 + Achtungswürdigkeit § 17).
3. **Sachverhalt minutengenau ordnen.** Wer hat wann was gesagt/getan, vor welchem Personenkreis (innerdienstlich, halböffentlich, öffentlich, social media)?
4. **Verfahrenslage prüfen.** Liegt schon ein disziplinargerichtliches Vorermittlungsverfahren vor (§ 92 WDO)? Anhörung erfolgt? Aussagebereitschaft?
5. **Frist setzen.** WBO-Beschwerde 1 Monat (§ 6 WBO), weitere Beschwerde 2 Wochen, Antrag auf gerichtliche Entscheidung 2 Wochen.
6. **Rechtsweg festlegen.** Truppendienstgericht (WBO/WDO), BVerwG Wehrdienstsenat (Revision/höhere Sache), Verwaltungsgericht ausnahmsweise (rein verwaltungsrechtliche Sachen ohne soldatischen Bezug, Versorgung).
7. **Dokumentenanforderung.** Personalakte (Einsicht § 29 SG), Beurteilungen, Disziplinarvorgänge, Befehl/Weisung schriftlich, Zeugenliste.

## Trade-off-Matrix

| Konflikt | Option A | Option B |
| --- | --- | --- |
| Treuepflicht vs. Meinungsfreiheit | Schweigen, Verfahren abwarten | Stellungnahme mit Rechtsbeistand |
| Befehl ausführen vs. Gehorsamsverweigerung | Befehl ausführen, danach Remonstration | Verweigerung mit Berufung auf § 11 II SG |
| Beschwerde sofort vs. erst Akteneinsicht | Frist sichern (Schutzschrift) | Akteneinsicht + qualifizierte Beschwerde |
| Disziplinar vs. WBO | WBO bei Maßnahme einfacher Art | Mündliche Verhandlung Truppendienstgericht |

## Praxistipps

- Frist 1 Monat ab Kenntnis ist absolut. Eine vorsorgliche Beschwerde mit dem Vorbehalt der Begründung sichert die Frist.
- Anhörung nach § 32 WDO immer wahrnehmen, aber zur Sache keine Spontanäußerung; schriftliche Stellungnahme.
- Personalakteneinsicht (§ 29 SG) ist kostenlos und voraussetzungsfrei. Nutzen Sie sie vor jeder Verteidigungsschrift.
- Politische Äußerungen außer Dienst nicht pauschal harmlos – § 15 II SG erfasst auch private Social-Media-Posts.
- Kameradschaftspflicht (§ 12) hat Drittschutzfunktion – Verstoß kann disziplinar- und strafrechtlich relevant sein.

## Mustertexte

**Frist sichernde Beschwerde nach WBO:**
"Sehr geehrte Damen und Herren, namens und im Auftrag meines Mandanten erhebe ich gegen die [Maßnahme] vom [Datum], zugegangen am [Datum], hiermit fristwahrend Beschwerde nach § 1 WBO. Die Begründung wird nach Akteneinsicht nachgereicht. Ich beantrage, mir die vollständige Vorgangsakte zur Einsicht zu überlassen."

**Remonstration bei Zweifel an der Rechtmäßigkeit:**
"Herr [Dienstgrad], ich melde Bedenken gegen den Befehl vom [Zeitpunkt] aus folgenden Gründen: [...]. Ich bitte um Bestätigung des Befehls und um Mitteilung der Rechtsgrundlage. Bis dahin werde ich den Befehl nicht ausführen, soweit dies mit der Dienstaufgabe vereinbar ist."

## Typische Fehler

- Sofort-Erklärung in der Anhörung ohne Akteneinsicht – führt zu Festlegung auf nachteilige Sachverhaltsfassung.
- Verwechslung von einfacher Disziplinarmaßnahme (Disziplinarvorgesetzter) und gerichtlicher Maßnahme (Truppendienstgericht).
- Übersehen, dass § 15 SG auch außerdienstliche Äußerungen erfassen kann.
- WBO-Frist versäumt, weil Zugang nicht dokumentiert.
- Verwaltungsgerichtsweg nach VwGO gewählt, obwohl WBO-Weg eröffnet und verbindlich ist.

## Querverweise

- gehorsam-befehl-und-rechtswidriger-befehl
- wehrbeschwerdeordnung-beschwerde-frist-form
- wehrdisziplinarordnung-einfache-disziplinarmassnahme
- status-soldat-beamter-zivilbeschaeftigter-klaeren
- politische-betaetigung-maessigung-neutralitaet
- presseaeusserung-meinungsfreiheit-soldat

## Quellen Stand 06/2026

- Soldatengesetz (SG) in der jeweils geltenden Fassung – Volltext: gesetze-im-internet.de.
- Wehrbeschwerdeordnung (WBO) – Volltext: gesetze-im-internet.de.
- Wehrdisziplinarordnung (WDO) in der ab 2025 geltenden Fassung.
- BVerwG, Wehrdienstsenate – ständige Rechtsprechung zu §§ 7, 11, 15, 17 SG (Az. nur nach Live-Verifikation in der BVerwG-Datenbank).
- Keine Kommentarstellen aus Modellwissen zitieren; Scherer/Alff/Poretschkin und Walz/Eichen nur bei konkretem Lizenzzugriff.

## 2. `soldatenversorgungsgesetz-beschaedigtenversorgung`

**Fokus:** Soldatenversorgungsgesetz Beschädigtenversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Soldatenversorgungsgesetz – Beschädigtenversorgung

## Fachkern: Soldatenversorgungsgesetz – Beschädigtenversorgung
- **Spezialgegenstand:** Soldatenversorgungsgesetz – Beschädigtenversorgung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Das SVG regelt Versorgung wegen Wehrdienstbeschädigung (WDB), Hinterbliebenenversorgung, Berufsförderung und ergänzende Versorgung. Eine Wehrdienstbeschädigung ist eine gesundheitliche Schädigung, die durch eine Wehrdienstverrichtung, durch einen während der Ausübung des Wehrdienstes erlittenen Unfall oder durch die dem Wehrdienst eigentümlichen Verhältnisse verursacht worden ist (§ 81 SVG). Der Skill ordnet Anspruchsgrundlagen, Verfahren und Bescheidstrategie.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche gesundheitliche Schädigung? Diagnose, Datum der Diagnose, behandelnde Ärzte.
- Welche Wehrdienstverrichtung war ursächlich? Datum, Ort, Zeugen, Einsatzbefehl.
- Liegt bereits ein Antrag, Bescheid, Widerspruchsbescheid vor?
- Frühere Erkrankungen / Vorschädigungen?
- Reine WDB-Versorgung oder zusätzlich Berufsförderung (§ 81 ff. SVG)?
- Hinterbliebenenversorgung (§§ 41 ff. SVG)?

## Rechtlicher Rahmen

- §§ 80 ff. SVG: Beschädigtenversorgung – Anspruchsgrundlage.
- § 81 SVG: Definition der Wehrdienstbeschädigung.
- § 81a SVG: Einsatzunfall – besondere Versorgung bei Auslandseinsatz und vergleichbarer Verwendung.
- § 81e SVG: Einsatzversorgungs-Verbesserungsgesetz – erhöhte einmalige Leistung.
- §§ 30 ff. BVG entsprechend: GdS (Grad der Schädigungsfolgen), Renten.
- § 88 SVG: Versorgung der Hinterbliebenen.
- §§ 4 ff. SVG: Berufsförderung der Soldaten auf Zeit (BFD).
- §§ 102 ff. SVG: Verfahren – Antrag bei der Wehrbereichsverwaltung/Bundesamt für Personalmanagement.
- § 4 SGB IX: Teilhabeleistungen.
- Beweismaß: Vollbeweis der Schädigung, Wahrscheinlichkeitsmaß der Kausalität (§ 81 VI SVG).

## / Schritt für Schritt

1. **Schädigung dokumentieren.** Diagnose, ärztliche Berichte, ggf. AU-Bescheinigung, Klinikentlassungsberichte, MRT/CT-Befunde.
2. **Kausalkette aufbauen.** Welche Wehrdienstverrichtung (Übung, Einsatz, dienstliche Tätigkeit) war ursächlich? Zeugen, Befehle, Einsatzberichte beibringen.
3. **Antragstellung.** Antrag beim Bundesamt für Personalmanagement der Bundeswehr (BAPersBw), Abteilung WDB. Formular BAPersBw.
4. **Beweisgrade prüfen.** Schädigung im Vollbeweis (medizinisch); Kausalität nach Wahrscheinlichkeit; bei mehrfacher Ursache Mitverursachung.
5. **Begutachtung.** Sachverständigengutachten – Recht auf Stellungnahme, eigenes Gutachten.
6. **Bescheid prüfen.** GdS-Festsetzung (Anlehnung an BVG-Anhalt, "Versorgungsmedizinische Grundsätze"), Rente, Pflegezulage, Berufsschadensausgleich.
7. **Widerspruch.** § 70 ff. VwGO entsprechend – 1 Monat ab Zustellung. Bei Erfolglosigkeit: Klage Sozialgericht (§§ 51 ff. SGG, Verweis aus § 88a SVG entsprechend) bzw. Verwaltungsgericht je nach Anspruchsart.
8. **Einsatzunfall.** § 81a SVG eröffnet höhere Leistung – wenn Auslandseinsatz oder gleichgestellte Verwendung. Einmalige Entschädigung.

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Klare Kausalität, akute Schädigung | Sofortantrag mit ärztlichen Befunden |
| Diffuse psychische Folgen (PTBS) | Gutachten plus Zeugen plus Einsatzberichte |
| Vorerkrankungen | Mitwirkungswahrscheinlichkeit nachweisen |
| Einsatzunfall vs. Truppenübungsunfall | § 81a SVG erfasst nur Einsatz iSd § 1a SG |

## Praxistipps

- Frist für den Antrag selbst gibt es nicht – jedoch je länger die Latenz, desto schwerer der Kausalitätsbeweis.
- Versorgungsmedizinische Grundsätze (VMG) – verbindlich für die Beurteilung des GdS; eigene Stellungnahme einreichen.
- Bei PTBS: spezifisches Schema – psychiatrisches Gutachten und Belastungsanamnese.
- Einsatzversorgung § 81e SVG: bis 150.000 Euro einmalig (Stand 06/2026) bei GdS 50 v.H. und mehr.
- Verbindung mit gesetzlicher Unfallversicherung beachten – BG-Bund subsidiär.

## Mustertexte

**Antrag auf WDB-Versorgung:**
"Beim Bundesamt für Personalmanagement der Bundeswehr beantrage ich Versorgung nach § 80 SVG wegen Wehrdienstbeschädigung. Sachverhalt: Am [Datum] erlitt mein Mandant während [Wehrdienstverrichtung/Übung/Einsatz] eine [Diagnose]. Beweismittel: 1. ärztliche Berichte (Anl. 1–3), 2. Einsatzbefehl/Übungsbefehl (Anl. 4), 3. Zeugen [...]. Es wird beantragt, einen GdS von [%] festzustellen und Beschädigtenrente nach § 30 BVG zu gewähren."

**Widerspruch gegen WDB-Bescheid:**
"Gegen den Bescheid vom [Datum] lege ich fristwahrend Widerspruch ein. Der angesetzte GdS von [%] ist zu niedrig. Die Schädigungsfolgen [...] führen nach den VMG zu einem GdS von mindestens [%]. Ich beantrage Einholung eines zweiten Gutachtens. Bis dahin ist die Begründung als vorläufig zu verstehen."

## Typische Fehler

- Antrag zu spät – Kausalitätsnachweis erschwert.
- Diagnose ohne Kausalbezug zur Wehrdienstverrichtung.
- VMG nicht herangezogen – GdS-Festsetzung nicht angreifbar.
- § 81a SVG übersehen – Einsatzunfall-Pauschale entgeht.
- Widerspruchsfrist mit Klagefrist verwechselt.

## Querverweise

- einsatzunfall-wehrdienstbeschaedigung
- einsatz-unfall-versorgung-dokumentenplan
- ptbs-einsatzfolge-beweisfuehrung
- aerztliche-begutachtung-dienstfaehigkeit
- sanitaetsdienst-heilfuersorge
- dienstunfaehigkeit-entlassung-zurruhesetzung

## Quellen Stand 06/2026

- SVG, BVG, SGB IX – Volltexte gesetze-im-internet.de.
- Versorgungsmedizinische Grundsätze – publik beim Bundesministerium für Arbeit und Soziales.
- BSG zu § 81 SVG – ständige Rechtsprechung zur Kausalitätsfrage.
- BAPersBw – Verwaltungspraxis und Antragsformulare.
- Einsatzversorgungs-Verbesserungsgesetz – BGBl. Eintrag und Folgenovellen verifizieren.

## 3. `status-soldat-beamter-zivilbeschaeftigter-klaeren`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Status Soldat Beamter Zivilbeschäftigter klären.

# Status klären: Soldat, Beamter oder Zivilbeschäftigter

## Fachkern: Status klären: Soldat, Beamter oder Zivilbeschäftigter
- **Spezialgegenstand:** Status klären: Soldat, Beamter oder Zivilbeschäftigter. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Innerhalb der Bundeswehr arbeiten drei Statusgruppen mit unterschiedlichen Rechtsregimen: Soldaten (SG, WBO, WDO), Beamte der Bundeswehrverwaltung (BBG, BDG, BLV) und Tarifbeschäftigte (TVöD-Bund, BPersVG). Verfahrenswege, Disziplinarrecht, Versorgung und Mitbestimmung unterscheiden sich grundsätzlich. Der Skill ordnet den Mandantenstatus zu, klärt parallel laufende Rechtswege und schützt vor Falschadressierung.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Berufsbezeichnung steht im aktuellen Vertrag/Bescheid?
- Wann erfolgten Ernennung oder Einstellung?
- Welche Dienststelle (Truppenteil, Bundesamt für Personalmanagement, BAAINBw, Bundesamt für Infrastruktur)?
- Liegt ein paralleles Statusverhältnis vor (Reservedienst neben Beamtenstatus, Soldat auf Zeit nach Beamtenlaufbahn)?
- Welches Rechtsproblem ist im Raum (Disziplinar, Versetzung, Versorgung, Mitbestimmung)?
- Welche Frist läuft – und welche Beschwerdeordnung gilt dafür?

## Rechtlicher Rahmen

- § 1 SG: Soldateneigenschaft – Berufssoldat, Soldat auf Zeit, freiwilliger Wehrdienstleistender, Reservist im Dienstverhältnis.
- BBG, BLV: Bundesbeamtenrecht für Beamte der Bundeswehrverwaltung.
- TVöD-Bund: Arbeitsverhältnisse mit dem Bund als Arbeitgeber.
- BPersVG: Mitbestimmung der zivilen Beschäftigten.
- SBG: Beteiligungsrechte der Soldaten (Vertrauensperson).
- § 17 SG, § 7 SG: Soldatische Treuepflicht – gilt nur für Soldaten.
- Truppendienstgericht (WDO/WBO) vs. Verwaltungsgericht (VwGO) vs. Arbeitsgericht (ArbGG) – Rechtsweg je nach Status.

## / Schritt für Schritt

1. **Status feststellen.** Ernennungs- oder Einstellungsurkunde, Arbeitsvertrag, Personalausweis (Truppenausweis vs. Dienstausweis).
2. **Reservistenstatus prüfen.** Beamte/Tarifbeschäftigte können gleichzeitig Reservisten sein (UWBO, WPflG, Reservistendienst). Bei Heranziehung gilt SG zeitweise neben Beamten-/Tarifrecht.
3. **Rechtsweg zuordnen.**
 - Soldat: WBO/WDO + Truppendienstgericht + BVerwG.
 - Beamter Bundeswehrverwaltung: BDG/BBG + Verwaltungsgericht.
 - Tarifbeschäftigter: TVöD + Arbeitsgericht.
4. **Mitbestimmung.** Soldat: SBG-Vertrauensperson. Beamter/Beschäftigter: BPersVG-Personalrat. Mischverhältnisse beachten.
5. **Versorgungsregime.** Soldat: SVG, BeamtVG (Versorgungslückenausgleich). Beamter: BeamtVG. Beschäftigter: gesetzliche Rente + ZVK.
6. **Disziplinarregime.** Soldat: WDO (Verweis bis Entfernung aus dem Dienstverhältnis). Beamter: BDG (Verweis bis Entfernung). Beschäftigter: Arbeitsrecht (Abmahnung, Kündigung).
7. **Doppelstatus dokumentieren.** Manche Soldaten wechseln in die Verwaltung – Übergangsregelungen prüfen.

## Trade-off-Matrix

| Mandat | Rechtsweg | Erste Maßnahme |
| --- | --- | --- |
| Versetzung Soldat | WBO § 17 → TDG | Beschwerde 1 Monat |
| Versetzung Beamter | VwGO § 42 → VG | Widerspruch 1 Monat |
| Kündigung Beschäftigter | KSchG → ArbG | Klage 3 Wochen |
| Reservist heranziehbar | WPflG/UWBO | Widerspruch |

## Praxistipps

- Erste Frage immer: "Sind Sie verbeamtet, Soldat oder im Tarifvertrag beschäftigt?" – Mandanten verwechseln häufig "Bundeswehrangehöriger" und "Soldat".
- Reservisten unterliegen während des Dienstes SG; sonst nur Reservistenrecht.
- Tarifbeschäftigte sind keine Soldaten – aber Sicherheitsüberprüfung (SÜG) gilt häufig auch.
- Bei doppeltem Mandat: getrennte Akten und Schriftsätze, klarer Hinweis im Briefkopf.
- Im Streit über den Status: Statusklage zum jeweiligen Gericht (VG oder ArbG; Statusklage beim TDG nicht statthaft).

## Mustertexte

**Statusfrage an Mandant:**
"Zur Klärung Ihres Rechtsstatus bitte ich um folgende Unterlagen: 1. Ernennungs- bzw. Einstellungsurkunde, 2. aktueller Arbeits-/Dienstvertrag, 3. Truppen- oder Dienstausweis (Kopie), 4. ggf. Reservistenbescheid und Heranziehungsbescheide, 5. Mitteilung über die zuständige Personalbearbeitungsstelle."

**Klarstellender Schriftsatz bei Statusunklarheit:**
"Vorsorglich weise ich darauf hin, dass mein Mandant zum maßgeblichen Zeitpunkt Soldat auf Zeit nach § 1 III SG war. Die [angerufene Stelle] ist daher zur Entscheidung nicht zuständig. Zuständig ist [...]. Hilfsweise bitte ich um Verweisung nach § 17a GVG entsprechend."

## Typische Fehler

- Soldatischen Mandanten beim Verwaltungsgericht klagen lassen – Klage unzulässig.
- Reservisten als reine Zivilbeschäftigte behandeln – während Heranziehung gilt SG.
- BDG-Vorschriften auf Soldaten anwenden – WDO ist abschließend.
- Personalrat statt Vertrauensperson einschalten oder umgekehrt.
- Versorgungsansprüche nach BeamtVG statt SVG prüfen.

## Querverweise

- soldatengesetz-rechtsstellung-grundpflichten
- beamtenrecht-bundeswehrverwaltung-abgrenzung
- arbeitsrecht-zivile-bundeswehrbeschaeftigte
- personalvertretung-zivile-beschaeftigte-schnittstelle
- soldatenbeteiligung-vertrauensperson-sbg
- reservistendienst-dienstleistungspflicht

## Quellen Stand 06/2026

- SG, WBO, WDO, SBG, SVG, WPflG – Volltexte gesetze-im-internet.de.
- BBG, BDG, BLV, BeamtVG – Volltexte gesetze-im-internet.de.
- BPersVG – Volltext gesetze-im-internet.de.
- TVöD-Bund – aktuelle Fassung beim Bundesinnenministerium.
- BVerwG zu Statusfragen – ständige Rechtsprechung (Az. nur verifiziert).
