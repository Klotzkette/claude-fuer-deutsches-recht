---
name: verwr-verwaltungsverfahren-eilantrag-abs
description: "Verwr Verwaltungsverfahren Eilantrag ABS im Plugin Fachanwalt Verwaltungsrecht: prüft konkret Checkliste Verwaltungsverfahren VwVfG, Eilantrag auf Wiederherstellung oder Anordnung, Rechtsschutz gegen Planfeststellungsbeschluss für Strom-. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Verwr Verwaltungsverfahren Eilantrag ABS

## Arbeitsbereich

**Verwr Verwaltungsverfahren Eilantrag ABS** ordnet den Fall über die tragenden Prüfungslinien: Checkliste Verwaltungsverfahren VwVfG, Eilantrag auf Wiederherstellung oder Anordnung, Rechtsschutz gegen Planfeststellungsbeschluss für Strom-. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `verwr-verwaltungsverfahren-checkliste` | Checkliste Verwaltungsverfahren VwVfG: Anhörung § 28, Begruendung § 39, Bekanntgabe § 41, Anhörung bei Ermessensentscheidungen. Pruefraster Bescheid auf formelle Fehler. |
| `eilantrag-80-abs-5-vwgo` | Eilantrag auf Wiederherstellung oder Anordnung aufschiebender Wirkung nach § 80 Abs. 5 VwGO stellen: Mandant hat Widerspruch eingelegt oder Klage erhoben aber die Behörde hat sofortige Vollziehung angeordnet. Normen: § 80 Abs. 2 VwGO (gesetzlicher Entfall AW: öffentliche Abgaben, Polizei), § 80 Abs. 3 VwGO (Begründungspflicht sofortige Vollziehung). Prüfraster: Interessenabwaegung Vollziehungs- vs. Aussetzungsinteresse, Erfolgsaussichten Hauptsache, substantiierte Begründung. Output Schriftsatz Eilantrag § 80 Abs. 5 VwGO. Abgrenzung: § 123 VwGO (andere Antragsart) siehe einstweiliger-rechtsschutz-skill; Widerspruchsschrift siehe fachanwalt-verwaltungsrecht-widerspruchsschrift. |
| `energietrassen-planfeststellung-rechtsschutz` | Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen Netzausbau. Normen: § 43 EnWG, BBPlG, NABEG, EnLAG, LNG-Beschleunigungsgesetz; BVerwG als Erstinstanz. Prüfraster: Klagebefugnis, verkuerzte Klagefrist 1 Monat, UmwRG-Verbandsklage, Aarhus-Konvention, Erdkabel-Vorrang. Output Klageschrift-Entwurf, Klagebefugungs-Memo. Abgrenzung: BImSchG-Anlagen siehe energieanlagen-bimschg-genehmigung-verfahren; Planfeststellung allgemein VwVfG siehe schriftsatzkern-substantiierung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `verwr-verwaltungsverfahren-checkliste`

**Fokus:** Checkliste Verwaltungsverfahren VwVfG: Anhörung § 28, Begruendung § 39, Bekanntgabe § 41, Anhörung bei Ermessensentscheidungen. Pruefraster Bescheid auf formelle Fehler.

### VerwR: Verwaltungsverfahren-Checkliste

## Aufgabe
Checkliste Verwaltungsverfahren VwVfG: Anhörung § 28, Begruendung § 39, Bekanntgabe § 41, Anhörung bei Ermessensentscheidungen.

## Einstieg
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster Verwaltungsverfahren (formelle Rechtmaessigkeit des VA)

1. **Zuständigkeit** — sachlich, oertlich, instanziell (§§ 3, 4 VwVfG). Auch funktionelle Zuständigkeit pruefen.
2. **Verfahren**
 - **Anhörung Beteiligter** § 28 VwVfG vor Erlass eines belastenden VA; Heilung nach § 45 I Nr. 3, II VwVfG bis Abschluss letzte Tatsacheninstanz.
 - **Mitwirkung** Drittbetroffener (§ 13 VwVfG).
 - **Akteneinsicht** § 29 VwVfG; **Geheimhaltung** § 30 VwVfG.
 - **Befangenheit** §§ 20, 21 VwVfG (Mitwirkungsverbot, Besorgnis der Befangenheit).
 - Bei Massenverfahren / Planfeststellung: §§ 72 ff. VwVfG.
3. **Form**
 - Schriftform, elektronische Form, muendlich (§ 37 II VwVfG). Bei elektronischem VA: § 37 III, IV VwVfG.
 - **Begruendung** § 39 VwVfG (Ausnahmen § 39 II); fehlende/unzureichende Begruendung heilbar nach § 45 I Nr. 2 VwVfG.
 - **Rechtsbehelfsbelehrung** § 37 VI VwVfG; Folge fehlerhafter Belehrung: Jahresfrist (§ 58 II VwGO).
4. **Bekanntgabe** § 41 VwVfG — Zugang, Drei-Tages-Fiktion (§ 41 II VwVfG), öffentliche Bekanntgabe (§ 41 III, IV VwVfG); elektronische Bekanntgabe § 41 IIa VwVfG.

## Fehlerfolgen

- **Nichtigkeit** § 44 VwVfG: schwerer und offenkundiger Fehler (z. B. Erlass durch nicht existierende Behörde, Unmoeglichkeit).
- **Heilung** § 45 VwVfG: Antrag, Begruendung, Anhörung, Mitwirkung, Beschluss eines Ausschusses nachholbar bis zum Abschluss der letzten Tatsacheninstanz (§ 45 II VwVfG idF seit 1996).
- **Unbeachtlichkeit** § 46 VwVfG: bei gebundenen Entscheidungen, wenn offensichtlich, dass Fehler die Entscheidung in der Sache nicht beeinflusst hat. Bei Ermessen jedoch keine Unbeachtlichkeit.
- **Umdeutung** § 47 VwVfG.

## Praxisfallen

- **Anhörung** wird gerne uebersehen; im Klageverfahren regelmaessig erfolgreich rugbar, wenn keine Heilung nachgeholt wurde.
- **Begruendungstiefe**: bei Ermessensentscheidungen muss die Begruendung die wesentlichen Ermessensgesichtspunkte erkennen lassen (§ 39 I 3 VwVfG). Fehlende Ermessensausübung = Ermessensnichtgebrauch, nicht durch Begruendungsnachholung heilbar.
- **Drei-Tages-Fiktion** § 41 II VwVfG nur bei Versendung im Inland; bei Auslandszustellung andere Regeln (§ 41 II 4 VwVfG).

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `eilantrag-80-abs-5-vwgo`

**Fokus:** Eilantrag auf Wiederherstellung oder Anordnung aufschiebender Wirkung nach § 80 Abs. 5 VwGO stellen: Mandant hat Widerspruch eingelegt oder Klage erhoben aber die Behörde hat sofortige Vollziehung angeordnet. Normen: § 80 Abs. 2 VwGO (gesetzlicher Entfall AW: öffentliche Abgaben, Polizei), § 80 Abs. 3 VwGO (Begründungspflicht sofortige Vollziehung). Prüfraster: Interessenabwaegung Vollziehungs- vs. Aussetzungsinteresse, Erfolgsaussichten Hauptsache, substantiierte Begründung. Output Schriftsatz Eilantrag § 80 Abs. 5 VwGO. Abgrenzung: § 123 VwGO (andere Antragsart) siehe einstweiliger-rechtsschutz-skill; Widerspruchsschrift siehe fachanwalt-verwaltungsrecht-widerspruchsschrift.

### Eilantrag § 80 Abs. 5 VwGO

## Kernsachverhalt

Der Eilantrag nach § 80 Abs. 5 VwGO ist das zentrale Instrument, um den Vollzug eines belastenden Verwaltungsakts zu stoppen, wenn die aufschiebende Wirkung von Widerspruch oder Klage ausnahmsweise nicht besteht. Das Gericht nimmt eine summarische Prüfung der Erfolgsaussichten der Hauptsache und eine Interessenabwägung vor. Formelle Fehler in der Vollziehungsanordnung (§ 80 Abs. 3 VwGO) führen regelmäßig zur Wiederherstellung der aufschiebenden Wirkung, ohne dass es auf die materiellen Erfolgsaussichten ankommt.

## Kaltstart-Rückfragen

1. Liegt ein belastender Verwaltungsakt vor, gegen den Widerspruch oder Klage eingelegt wurde oder noch eingelegt wird?
2. Ist die aufschiebende Wirkung gesetzlich entfallen (§ 80 Abs. 2 Nr. 1–3 VwGO) oder behördlich angeordnet (Nr. 4)?
3. Ist die Begründung der Sofortvollziehung nach § 80 Abs. 3 VwGO einzelfallbezogen und substantiiert — oder nur floskelhaft?
4. Welche Erfolgsaussichten hat die Hauptsache — offensichtlich erfolglos, offen, oder offensichtlich erfolgreich?
5. Welche konkreten Schäden drohen bei sofortiger Vollziehung — Existenzgefährdung, Abschiebung, irreversible Bautätigkeit, Entziehung Berufserlaubnis?
6. Liegt ein Fall des § 80a VwGO vor (drittbetroffener Nachbar gegen Baugenehmigung)?
7. Wurde ein Aussetzungsantrag bei der Behörde nach § 80 Abs. 4 VwGO gestellt und abgelehnt?
8. Welches Gericht ist zuständig — VG, OVG, BVerwG (NABEG/EnLAG)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 80 Abs. 1 VwGO** — Widerspruch und Anfechtungsklage haben aufschiebende Wirkung.

**§ 80 Abs. 2 VwGO** — Die aufschiebende Wirkung entfällt bei öffentlichen Abgaben und Kosten (Nr. 1), unaufschiebbaren polizeilichen Maßnahmen (Nr. 2), gesetzlich bestimmten Fällen (Nr. 3), oder bei Anordnung der sofortigen Vollziehung im öffentlichen Interesse (Nr. 4).

**§ 80 Abs. 3 Satz 1 VwGO** — In den Fällen des Absatzes 2 Satz 1 Nr. 4 ist das besondere Interesse an der sofortigen Vollziehung des Verwaltungsakts schriftlich zu begründen.

**§ 80 Abs. 4 VwGO** — Die Behörde, die den Verwaltungsakt erlassen oder über den Widerspruch zu entscheiden hat, kann in den Fällen des Absatzes 2 die Vollziehung aussetzen.

**§ 80 Abs. 5 VwGO** — Das Gericht der Hauptsache kann auf Antrag die aufschiebende Wirkung in den Fällen des Absatzes 2 ganz oder teilweise anordnen oder wiederherstellen. Der Antrag ist schon vor Erhebung der Anfechtungsklage zulässig.

**§ 80a VwGO** — Bei einem Verwaltungsakt, der einen anderen begünstigt, kann ein Dritter, der durch den Verwaltungsakt beschwert wird, beim Gericht beantragen, die Vollziehbarkeit des Verwaltungsakts auszusetzen oder aufzuheben.

**§ 146 Abs. 4 VwGO** — Die Beschwerde ist innerhalb eines Monats nach Bekanntgabe der Entscheidung zu begründen. Die Begründung muss einen bestimmten Antrag enthalten, die Gründe darlegen, aus denen die Entscheidung abzuändern oder aufzuheben ist, und sich mit der angefochtenen Entscheidung auseinandersetzen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema § 80 Abs. 5 VwGO

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Statthaftigkeit | Anfechtungsklage-Situation; § 80 Abs. 2 VwGO einschlägig? Nr. 1–3 oder Nr. 4? Oder § 80a bei Drittbetroffenem? | Richtige Antragsform |
| 2 | Antragsbefugnis | Analog § 42 Abs. 2 VwGO; Adressat des VA oder Drittbetroffener | Eigenes Recht verletzt möglich? |
| 3 | Rechtsschutzbedürfnis | § 80 Abs. 4 VwGO-Antrag bei Behörde abgelehnt oder sinnlos? | Verfahrensvoraussetzung |
| 4 | Hauptsache anhängig | Widerspruch oder Klage parallel eingereicht? | Pflichtvoraussetzung |
| 5 | Begründungsmangel § 80 Abs. 3 | Vollziehungsanordnung floskelhaft? Kein Einzelfallbezug? | Eigenständiger Aufhebungsgrund |
| 6 | Begründetheits-Prüfung Erfolgsaussicht | Offensichtlich erfolglos / offen / offensichtlich erfolgreich | Hauptansatz der Entscheidung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 8 | Irreversibilität des Vollzugs | Schwere des Schadens; Nicht-Wiedergutzumachbarkeit | Je irreversibler, desto höher Aussetzungsinteresse |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 10 | Spezialfall Abgaben (Nr. 1) | Steuerbescheid; ernstliche Zweifel an Rechtmäßigkeit oder unbillige Härte | § 80 Abs. 4 Satz 3 VwGO |
| 11 | Streitwert | Hälfte Hauptsache-Streitwert; § 52 GKG | Im Antrag angeben |
| 12 | Entscheidungsform | Beschluss; ohne mündliche Verhandlung; Ausnahme Erörterung | Zeitplanung |
| 13 | Beschwerde § 146 Abs. 4 VwGO | 2 Wochen ab Beschluss; Begründungsfrist 1 Monat; Auseinandersetzungspflicht | OVG-Beschwerde |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 15 | Vollstreckung nach Stattgabe | Behörde zur Aussetzung verpflichtet; Zwangsgeld § 172 VwGO möglich | Vollstreckungsweg vorbereiten |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Formeller Mangel § 80 Abs. 3 VwGO | Antragsteller (Textanalyse des Bescheids) | Bescheid selbst; kein weiterer Beweis nötig |
| Erfolgsaussichten Hauptsache | Antragsteller (Substanziierung) / Behörde (Verteidigung) | Rechtliche Begründung, Sachverhaltsbelege |
| Existenzgefährdung / irreversibler Schaden | Antragsteller | Bilanzen, BWA, ärztliches Attest, Gutachten |
| Öffentliches Vollzugsinteresse | Behörde | Einzelfallbezogene Darlegung im Bescheid und Verfahren |
| Abgaben: ernstliche Zweifel § 80 Abs. 4 VwGO | Antragsteller | Steuerbescheid, Einspruchsschrift, Gutachten |
| § 80a: Bauherrn-Vollzugsinteresse | Beigeladener | Investitionspläne, Finanzierungsverträge |

## Fristen

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Antragstellung § 80 Abs. 5 VwGO | — | Unverzüglich nach Kenntnis; keine starre Frist; bei zu langem Warten Eilbedürftigkeit entfällt | Zu langes Zuwarten schadet |
| Hauptsachefrist parallel | § 70 VwGO / § 74 VwGO | 1 Monat ab Bekanntgabe VA | Pflicht; Versäumnis → Eilantrag unzulässig |
| Beschwerde § 146 VwGO | § 146 Abs. 1 VwGO | 2 Wochen ab Beschluss | Begründung: 1 Monat, § 146 Abs. 4 VwGO |
| § 80 Abs. 4 VwGO Behörde | — | Vor VG-Antrag; keine Frist; aber sinnvoll | Schneller als Gericht; Ablehnung öffnet VG-Weg |
| Notfallantrag außerhalb Dienstzeiten | — | Bei akuter Vollzugsgefahr; Bereitschaftsdienst anrufen | Fax + Telefon bei Gericht |

## Typische Gegenargumente

| Gegenargument der Behörde | Gegenstrategie |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Hauptsache hat keine Erfolgsaussichten" | Substanziierte Rechtsauffassung mit Normen und Rspr.; Behörde muss Gegendarstellung liefern |
| "Keine Existenzgefährdung" | Betriebswirtschaftliche Belege; BWA, Bilanzen; Liquiditätsplan; ggf. Steuerberater-Attest |
| "Zu spät gestellt — Eilbedürftigkeit entfallen" | Konkrete Handlungsaufnahme der Behörde als Auslöser benennen; Zeitachse darstellen |
| "Hauptsache nicht anhängig" | Widerspruch/Klage mit Datum belegen; ggf. parallel einreichen und im Antrag erwähnen |
| "§ 80a anstatt § 80 Abs. 5" | Konstellation klären: begünstigender VA für Dritten → § 80a; belastender VA für Antragsteller → § 80 Abs. 5 |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Eilantrag nach § 80 Abs. 5 VwGO gegen sofortvollziehbaren VA | Eilantragsschriftsatz nach Pruefschema; Template unten |
| Variante A — Aussetzung der Vollziehung direkt bei Behörde realistisch | Antrag bei Behörde § 80 Abs. 4 VwGO zuerst; Gericht nur bei Ablehnung |
| Variante B — Mandant akzeptiert VA aber nicht die sofortige Vollziehung | Nur Aussetzungsantrag ohne Widerspruch in der Hauptsache |
| Variante C — Eilantrag hat geringe Erfolgsaussichten Folgenabwaegung | Folgenabwaegung in den Vordergrund stellen statt summarischer Pruefung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Vollständiger Eilantrag mit § 80 Abs. 3-Rüge

```
Verwaltungsgericht [Ort]
[Anschrift]

In der Verwaltungsrechtssache

[Antragsteller / Name, Anschrift]
— Antragsteller —

Verfahrensbevollmächtigte: [Kanzlei]

gegen

[Behörde]
— Antragsgegnerin —

Az. Hauptsache: [Az.]

Antrag nach § 80 Abs. 5 VwGO

Namens und in Vollmacht stellen wir folgenden

Antrag

1. Die aufschiebende Wirkung des Widerspruchs [/ der Klage] des
 Antragstellers vom [Datum] gegen den Bescheid der
 Antragsgegnerin vom [Datum], Az. [Az.], wird wiederhergestellt.

2. Die Antragsgegnerin trägt die Kosten des Verfahrens.

3. Der Streitwert wird auf EUR [Betrag] (Hälfte des Hauptsache-
 Streitwerts von EUR [x]) festgesetzt.

Begründung

I. Sachverhalt
Mit Bescheid vom [Datum] hat die Antragsgegnerin [Inhalt des VA:
z.B. die Gaststättenerlaubnis widerrufen / die Baugenehmigung
versagt / die Abschiebungsanordnung erlassen]. Gleichzeitig hat
sie die sofortige Vollziehung angeordnet und wie folgt begründet:

"[Vollzitat der Vollziehungsbegründung]"

Der Antragsteller hat mit Schreiben vom [Datum] Widerspruch
eingelegt [/ Klage erhoben]. Der Eilantrag ist damit zulässig.

II. Formeller Mangel § 80 Abs. 3 VwGO

Die Begründung der sofortigen Vollziehung genügt den
Anforderungen des § 80 Abs. 3 Satz 1 VwGO nicht.

Nach der ständigen Rechtsprechung muss die Behörde in der
Begründung das besondere öffentliche Interesse an der
sofortigen Vollziehung auf den konkreten Einzelfall bezogen
darlegen. Allgemeine Formulierungen und abstrakte Verweise auf
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Die vorliegende Begründung beschränkt sich auf [Beschreibung
des Floskels: "im öffentlichen Interesse" / "Gefährdung der
Allgemeinheit" etc.]. Eine Auseinandersetzung mit den
individuellen Umständen des Antragstellers — insbesondere
[konkrete Aspekte] — fehlt vollständig.

Dieser Begründungsmangel allein rechtfertigt die Wiederherstellung
der aufschiebenden Wirkung.

III. Erfolgsaussichten der Hauptsache

Unabhängig vom Begründungsmangel hat der Widerspruch
überwiegende Erfolgsaussichten:

1. [Formeller Fehler: Anhörung unterblieben / Begründung mangelhaft]

2. Materieller Fehler: Die Tatbestandsvoraussetzungen des
 § [X] [Spezialgesetz] sind nicht erfüllt, weil [Subsumtion].

3. Ermessensfehler: Die Behörde hat relevante Belange wie
 [Belang] nicht berücksichtigt (§ 40 VwVfG).

IV. Interessenabwägung

Für das Aussetzungsinteresse des Antragstellers spricht:

— Die sofortige Vollziehung des Widerrufs der Gaststättenerlaubnis
 [/ Baugenehmigung / Berufserlaubnis] führt zur unmittelbaren
 Einstellung des Geschäftsbetriebs. [n] Arbeitnehmer verlieren
 ihren Arbeitsplatz. Die laufenden Verbindlichkeiten von
 EUR [x] monatlich können nicht mehr bedient werden.

— Der Schaden ist irreversibel: Auch bei späterem Klageerfolg
 kann der Betrieb nicht ohne Weiteres fortgeführt werden,
 da [Kundenstamm verloren / Verträge gekündigt / Vermögen
 liquidiert].

Das Vollzugsinteresse der Antragsgegnerin tritt zurück, weil:

— Keine unmittelbare Gefahr für Leib, Leben oder erhebliche
 öffentliche Güter besteht.

— Der Vollzug kann ohne wesentlichen Nachteil um die Dauer des
 Eilverfahrens (typisch 4–8 Wochen) verschoben werden.

Anlagen:
1. Bescheid vom [Datum] mit Vollziehungsanordnung
2. Widerspruch vom [Datum]
3. BWA / Liquiditätsplan zur Existenzgefährdung
4. Vollmacht
```

### Baustein 2: § 80a VwGO — Antrag Dritter gegen Baugenehmigung

```
Verwaltungsgericht [Ort]

Antrag nach § 80a Abs. 3 VwGO

[Antragsteller / Nachbar]
gegen
[Baugenehmigungsbehörde]
beigeladen: [Bauherr]

Antrag

Die Vollziehbarkeit der der Beigeladenen erteilten
Baugenehmigung vom [Datum], Az. [Az.], wird ausgesetzt.

Begründung

I. Drittanfechtungsbefugnis
Der Antragsteller ist Eigentümer des Nachbargrundstücks
[Flurstück] und durch die Baugenehmigung in seinen drittschützenden
Rechten aus [§ 15 Abs. 1 BauNVO / § 34 Abs. 1 BauGB /
Abstandsflächen § 6 LBO] verletzt.

II. Aussetzungsinteresse Nachbar
Die Vollziehung der Baugenehmigung führt zu irreversiblen
baulichen Maßnahmen, die bei einem Klageerfolg des
Antragstellers nicht mehr beseitigt werden können
(§ 35 Abs. 2 BauGB analog).

III. Erfolgsaussichten der Hauptsache
Die Baugenehmigung ist voraussichtlich rechtswidrig, weil
[Subsumtion: Abstandsflächen unterschritten / Rücksichtnahmegebot
verletzt / Nutzungsartfestsetzung missachtet].
```

### Baustein 3: Beschwerdeantrag nach § 146 VwGO

```
Oberverwaltungsgericht [Land]

In der Beschwerdesache

[Beschwerdeführer] — Beschwerdeführer —
gegen
[Beschwerdegegnerin] — Beschwerdegegnerin —

Az. OVG: [neu] / VG-Beschluss Az.: [Alt-Az]

Beschwerde nach § 146 VwGO

Gegen den Beschluss des Verwaltungsgerichts [Ort] vom [Datum]
legen wir form- und fristgerecht Beschwerde ein.

Begründung

I. Das Verwaltungsgericht hat den Begründungsmangel
§ 80 Abs. 3 VwGO unzutreffend verneint. Es hat die
Begründung: "[Zitat]" als ausreichend angesehen, obwohl sie
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
erforderliche einzelfallbezogene Auseinandersetzung fehlt.

II. Die Interessenabwägung ist fehlerhaft, weil das
Verwaltungsgericht die Existenzgefährdung des
Beschwerdeführers (BWA Anlage) nicht berücksichtigt hat.

III. Die Erfolgsaussichten der Hauptsache wurden unterschätzt,
weil [neue Tatsache / rechtliche Begründung].

Wir beantragen, den angefochtenen Beschluss aufzuheben
und die aufschiebende Wirkung wiederherzustellen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Eilantrag | Hälfte des Hauptsache-Streitwerts nach § 52 GKG | Auffangwert Hauptsache EUR 5.000 → Eilantrag EUR 2.500 |
| Gerichtskosten | GKG Anlage 1 Nr. 5210; bei EUR 2.500: ca. EUR 378 | Entfallen bei Stattgabe für Behörde |
| Anwaltsgebühren | RVG Nr. 3100 ff.; 1,3 Verfahrensgebühr; ggf. 1,2 Terminsgebühr | Bei Obsiegen Erstattung durch Gegenseite |
| Streitwert Beschwerde | Identisch mit VG-Streitwert | Keine eigene Festsetzung des OVG nötig |
| Notwendige Hinzuziehung | §§ 80 VwVfG, 162 VwGO | Antrag im Eilverfahren stellen |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Begründungsmangel § 80 Abs. 3 eindeutig | Formalfehler als eigenständigen Grund vorantreiben; kein Eingehen auf Hauptsache nötig |
| Hauptsache offensichtlich erfolgreich | Kurze, direkte Begründung Hauptsacheerfolg; Aufwand für Interessenabwägung gering |
| Hauptsache offen | Irreversibilität und Existenzgefährdung belegen; BWA einreichen; Risikodifferenz zwischen Aussetzung und Vollzug herausarbeiten |
| Fahrerlaubnissachen | VGH Bayern-Rspr. beachten: öffentliches Interesse an Verkehrssicherheit sehr hoch; Aussetzung nur bei klaren Fehlern |
| § 80a Nachbar-Situation | Drittschutznorm konkret benennen; Irreversibilität der Baumaßnahme betonen |
| Beschwerde nach Abweisung | Konkrete Fehler des VG-Beschlusses; neue Tatsachen; keine bloße Wiederholung |

## Anschluss-Skills

- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Überblick einstweiliger Rechtsschutz inkl. § 123 VwGO
- `fachanwalt-verwaltungsrecht-widerspruchsschrift` — Parallel-Einlegung Widerspruch
- `energieanlagen-bimschg-genehmigung-verfahren` — Eilrechtsschutz bei BImSchG
- `energietrassen-planfeststellung-rechtsschutz` — Eilrechtsschutz bei Planfeststellung

## Quellen

Stand 05/2026.

- VwGO §§ 42, 80, 80a, 113, 146, 172 — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwgo/)
- VwVfG §§ 28, 39, 80 — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwvfg/)
- GKG § 52; RVG Nr. 3100 ff. — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gkg_2004/)
- BVerwG, Beschlussdatenbank — [bverwg.de](https://www.bverwg.de)
- BVerfG (für Verhältnismäßigkeits- und Folgenabwägungslinie) — [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de)
- Rechtsprechung im Mandat live verifizieren — keine Aktenzeichen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## 3. `energietrassen-planfeststellung-rechtsschutz`

**Fokus:** Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen Netzausbau. Normen: § 43 EnWG, BBPlG, NABEG, EnLAG, LNG-Beschleunigungsgesetz; BVerwG als Erstinstanz. Prüfraster: Klagebefugnis, verkuerzte Klagefrist 1 Monat, UmwRG-Verbandsklage, Aarhus-Konvention, Erdkabel-Vorrang. Output Klageschrift-Entwurf, Klagebefugungs-Memo. Abgrenzung: BImSchG-Anlagen siehe energieanlagen-bimschg-genehmigung-verfahren; Planfeststellung allgemein VwVfG siehe schriftsatzkern-substantiierung.

### Energietrassen — Planfeststellung und Rechtsschutz

## Kernsachverhalt

Bei Stromtrassen, Erdgas-Pipelines, LNG-Terminals, Wasserstoff-Stammnetz und Offshore-Anbindungsleitungen gibt es verkürzte, beschleunigte Verfahren mit eingeschränktem Rechtsschutz. Die Klagefrist beträgt regelmäßig nur einen Monat. Mandanten auf Drittbetroffenen- und Verbandsseite haben dennoch erhebliche prozessuale Möglichkeiten, insbesondere über UVP-Fehler, Alternativenprüfung, Artenschutz und Entschädigungsansprüche.

## Kaltstart-Rückfragen

1. Welches Vorhabens-Typ — Stromtrasse (380 kV, HGÜ), Erdgas-Pipeline, LNG-Terminal, H2-Stammnetz, Offshore-Anbindungsleitung?
2. Welches Genehmigungsregime — NABEG, EnLAG, BBPlG, WindSeeG, LNG-Beschleunigungsgesetz?
3. Mandantenrolle — Grundeigentümer/Anlieger, anerkannter Umweltverband, Gemeinde?
4. Verfahrensstand — Bundesfachplanung, laufende Planfeststellung, Beschluss ergangen, Klagefrist läuft?
5. Wurde sofortige Vollziehung des Planfeststellungsbeschlusses angeordnet — Eilantrag nach § 80 Abs. 5 VwGO erforderlich?
6. Liegt Enteignung oder Entschädigungsanspruch des Grundeigentümers vor?
7. Hat der Verband im Planfeststellungsverfahren ordnungsgemäß mitgewirkt (Pflichtvoraussetzung UmwRG)?
8. Welche konkreten Fehler bestehen — Alternativenprüfung, UVP-Defizit, Artenschutz-saP, Lärmschutz, Erdkabel-Abwägung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 18 NABEG (Planfeststellungsbeschluss)** — Die zuständige Behörde stellt den Plan auf Antrag des Vorhabenträgers durch Planfeststellungsbeschluss fest. Der Beschluss ist für alle öffentlich-rechtlichen Beziehungen verbindlich.

**§ 1 EnLAG** — Zur Beschleunigung des Ausbaus der Höchstspannungsnetze sind die im Bedarfsplan zu EnLAG aufgeführten Vorhaben vordringlich zu realisieren. Klagefrist 1 Monat, erste Instanz BVerwG.

**§ 50 Abs. 1 Nr. 6 VwGO** — Das Bundesverwaltungsgericht entscheidet im ersten und letzten Rechtszug über Streitigkeiten aus den in NABEG und EnLAG genannten Vorhaben.

**§ 4 Abs. 1 EnLAG (Erdkabel-Vorrang)** — Auf Verlangen des Vorhabenträgers oder auf Antrag der betroffenen Gemeinde oder Einwohner ist bei bestimmten Leitungsabschnitten Erdkabel zu prüfen und bevorzugt einzusetzen.

**§ 2 UmwRG** — Anerkannte Umweltverbände können Klage gegen Entscheidungen erheben, die dem Anwendungsbereich des UmwRG unterliegen, ohne Verletzung eigener Rechte geltend machen zu müssen (altruistische Verbandsklage).

**Art. 9 Aarhus-Konvention** — Zugang zu Gerichten in Umweltangelegenheiten muss effektiv sein; Kostenbarrieren dürfen Klagerecht nicht aushöhlen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Planfeststellungs-Rechtsschutz

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Vorhabens-Regime bestimmen | NABEG / EnLAG / BBPlG / WindSeeG / LNG-G → Klagegericht und Klagefrist | BVerwG erste Instanz oder VG? |
| 2 | Klagefrist 1 Monat | Ab Zustellung des Planfeststellungsbeschlusses; keine Wiedereinsetzung außer bei unverschuldetem Fristversäumnis | Frist dokumentieren |
| 3 | Klagebefugnis Anlieger | Art. 14 GG Eigentumsgarantie; Enteignungs-Duldungspflicht; eigene Rechtsbetroffenheit aus Immissionsschutz | § 42 Abs. 2 VwGO analog |
| 4 | Klagebefugnis Verband | § 2 UmwRG; Beteiligung im Planfeststellungsverfahren erfolgt; keine Verletzung eigener Rechte nötig | Beteiligung dokumentieren |
| 5 | Sofortvollzug / Eilantrag | Anordnung sofortiger Vollziehung? Begründung § 80 Abs. 3 VwGO? | Eilantrag § 80 Abs. 5 VwGO |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 8 | saP / Artenschutz | Artenschutzrechtliche Prüfung nach § 44 BNatSchG; Erfassungsmethodik; Vermeidungsmaßnahmen | Methodenfehler geltend machen |
| 9 | Lärmschutz / TA Lärm | Bei Konverteranlagen, Umspannwerken; TA Lärm-Richtwerte; Schallgutachten korrekt? | Gegengutachten einsetzen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 12 | Entschädigungsanspruch | Enteignungs-Entschädigung nach § 18 EnWG; Wertgutachten Grundstück vor und nach | Eigene Verhandlungsführung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 14 | Aarhus-Kostenbarriere | Gerichtskosten dürfen effektiven Zugang nicht aushöhlen; Art. 9 Aarhus; EU-Recht | Kostenantrag bei Verband |
| 15 | Beschwerde bei Eilabweisung | § 146 VwGO 2 Wochen; OVG/BVerwG; neue Tatsachen zulässig | Beschwerdebegründung 1 Monat |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Vollständigkeit UVP-Bericht | Kläger (Rüge) / Behörde (Verteidigung) | UVP-Bericht, Planfeststellungsunterlagen |
| Methodische Fehler saP | Kläger | Eigene Artenschutz-Expertise, Gegenattest |
| Alternativenprüfung unvollständig | Kläger | Planfeststellungsbeschluss, Planunterlagen |
| Grundstückswertminderung | Anlieger (Entschädigung) | Wertgutachten vor/nach, Vergleichspreise |
| Härtung Klimaargument bei LNG | Verband (Kläger) | Emissionsberechnung, IPCC-Berichte, BVerfG |
| Kein effektiver Rechtsschutz Aarhus | Verband | Kostenaufstellung, Vergleich Streitwert vs. Verbandsbudget |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Klagefrist NABEG/EnLAG | § 74 VwGO i.V.m. NABEG/EnLAG | 1 Monat ab Zustellung Beschluss | Sehr kurz; sofort nach Erhalt des Beschlusses handeln |
| Eilantrag § 80 Abs. 5 VwGO | — | Innerhalb der Klagefrist; keine eigene Ausschlussfrist | Früh stellen, da Bau sofort beginnen kann |
| Beschwerde gegen Eilentscheidung | § 146 Abs. 4 VwGO | 2 Wochen; Begründung 1 Monat | BVerwG bei NABEG/EnLAG-Vorhaben |
| Beteiligung im Planfeststellungsverfahren | — | Auslegungszeitraum + Einwendungsfrist | Versäumnis → eingeschränkte Klagemöglichkeit |
| Entschädigungsklage | § 195 BGB | 3 Jahre ab Kenntnis des Eingriffs | Zivilgericht bei Entschädigungsstreit |
| Bundesfachplanung-Einwendung | NABEG § 9 | Innerhalb der Konsultationsfrist | Frühe Einbindung sichert spätere Klageposition |

## Typische Gegenargumente

| Gegenargument | Gegenstrategie |
|---|---|
| "Beschleunigungsgesetz schränkt Prüfung ein" | Grundrechtliche Mindestanforderungen bleiben; UVP-Richtlinie EU-Recht geht vor; Aarhus-Konvention Art. 9 |
| "Klimaschutz rechtfertigt sofortigen Bau" | § 80 Abs. 3 VwGO Begründung muss auf Einzelfall eingehen; fossiles Vorhaben: Klimaschluss wirkt gegen Sofortvollzug |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Verband nicht klagebefugt — zu spät beteiligt" | Beteiligung muss nur im Planfeststellungsverfahren erfolgt sein, nicht bereits in Bundesfachplanung; Beteiligung dokumentieren |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Enteignungsentschädigung angemessen" | Unabhängiges Wertgutachten beauftragen; Folgeschäden (Wertminderung, Nutzungseinschränkung) erfassen |
| "LNG-Terminal klimaneutral nutzbar" | Ohne verbindliche Wasserstoff-Umrüstungsklausel ist Klimaargument nicht tragfähig; BVerfG-Maßstab anlegen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Rechtsschutz gegen Planfeststellungsbeschluss Energietrasse | Anfechtungsklage nach Pruefschema; Schriftsatz unten |
| Variante A — Einwendung im Planfeststellungsverfahren noch moeglich | Einwendung im Verfahren zuerst; Klage nur nach Bestandskraft |
| Variante B — Mandant als Betroffener will nur Auflagen aendern | Teilanfechtung nur der belastenden Nebenbestimmungen |
| Variante C — Oeffentlichkeit will Gesamtprojekt verhindern | Normenkontrolle oder UVP-Ruege als staerkere Angriffspunkte |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Klage-Antrag BVerwG erste Instanz

```
Bundesverwaltungsgericht Leipzig
Simsonplatz 1
04107 Leipzig

Klage nach § 50 Abs. 1 Nr. 6 VwGO

In dem verwaltungsgerichtlichen Verfahren

[Kläger / Umweltverband]
— Kläger —

gegen

Bundesnetzagentur, Tulpenfeld 4, 53113 Bonn
— Beklagte —

beigeladen: [Vorhabenträger]

Klageziel

1. Der Planfeststellungsbeschluss der Bundesnetzagentur vom [Datum]
 Az. [Az.] für das Vorhaben [Bezeichnung] wird aufgehoben,
 hilfsweise für rechtswidrig und nicht vollziehbar erklärt.

2. Die Beklagte trägt die Kosten des Verfahrens.

Klagefrist: Der Planfeststellungsbeschluss wurde dem Kläger am
[Datum] zugestellt. Die Klagefrist von einem Monat ist gewahrt.

Begründung (vorläufig — wird vertieft nach Akteneinsicht)

A. Zulässigkeit
Der Kläger ist als anerkannter Umweltverband nach §§ 2, 3 UmwRG
klagebefugt. Er hat sich mit Einwendungsschreiben vom [Datum]
am Planfeststellungsverfahren beteiligt. Die Klagefrist ist gewahrt.

B. Begründetheit (vorläufig)

I. UVP-Defizite
Der UVP-Bericht weist folgende materielle Lücken auf:
— Alternativenprüfung unvollständig: Die Erdkabel-Variante
 entlang der Bestandsautobahn A[x] wurde nicht ernsthaft
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
— Artenschutzrechtliche Prüfung (saP) fehlerhaft: Rotmilan-
 Kartierung nur an [n] Terminen außerhalb der Hauptaktivitäts-
 zeiten.

II. Klimaschluss
Das Vorhaben [LNG-Terminal / Erdgas-Pipeline] erhöht die
Treibhausgasemissionen um [x] t CO2-Äquivalente p.a. und
konterkariert die Pflicht des Staates zum Schutz künftiger
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Wir beantragen die Gewährung von Akteneinsicht in die vollständige
Planfeststellungsakte sowie angemessene Verlängerung der
Begründungsfrist nach § 87b Abs. 1 VwGO.
```

### Baustein 2: Eilantrag gegen sofortige Vollziehung Planfeststellungsbeschluss

```
Bundesverwaltungsgericht Leipzig

Antrag nach § 80 Abs. 5 VwGO

In dem o.g. Verfahren [Az. Klage]

Antrag

Die aufschiebende Wirkung der Klage des Antragstellers vom [Datum]
gegen den Planfeststellungsbeschluss der Bundesnetzagentur vom
[Datum] wird wiederhergestellt.

Begründung

I. Formeller Mangel Vollziehungsanordnung § 80 Abs. 3 VwGO
Die Bundesnetzagentur hat die sofortige Vollziehung mit der
Begründung angeordnet, es bestehe ein dringendes öffentliches
Interesse an der zeitnahen Realisierung des Vorhabens. Diese
Begründung ist formell unzureichend, da sie keine
Auseinandersetzung mit den konkreten Umständen des Einzelfalls —
insbesondere den gerügten UVP-Fehlern und den Risiken
irreversibler Natureingriffe — enthält.

II. Erfolgsaussicht der Hauptsache
Die Klage hat wegen der oben dargelegten UVP-Defizite und der
mangelhaften saP erhebliche Erfolgsaussichten. Eine vollständige
Aufhebung des Planfeststellungsbeschlusses erscheint möglich.

III. Interessenabwägung
Beginnen die Bauarbeiten sofort, drohen irreversible Eingriffe in
FFH-Gebiete und in das Grundeigentum des Antragstellers. Diese
Schäden sind durch einen späteren Klageerfolg nicht mehr
rückgängig zu machen. Demgegenüber kann der Baubeginn um die
Dauer des Eilverfahrens (typisch 4–8 Wochen) verschoben werden,
ohne den Vorhabenerfolg dauerhaft zu gefährden.
```

### Baustein 3: Einwendung im Planfeststellungsverfahren (Anlieger)

```
An die [Planfeststellungsbehörde / Bundesnetzagentur]

Einwendungen im Planfeststellungsverfahren [Bezeichnung]

Einwender: [Name, Anschrift, Grundstück Flurstück]

Sehr geehrte Damen und Herren,

gegen das geplante Vorhaben erheben wir folgende Einwendungen:

1. Eigentumsbetroffenheit
Das Grundstück des Einwenders (Flurstück [x], Gemarkung [y])
liegt innerhalb des geplanten Schutzstreifens. Es wird durch
Dienstbarkeiten belastet, die die landwirtschaftliche Nutzung
erheblich einschränken. Eine angemessene Entschädigung nach
§ 18 EnWG ist sicherzustellen.

2. Erdkabel-Vorrang § 4 EnLAG
Im Bereich der Ortschaft [X] liegt Wohnbebauung in Sichtweite
der geplanten Freileitung. Der Einwender beantragt gemäß
§ 4 Abs. 1 EnLAG die Prüfung und bevorzugte Realisierung
als Erdkabel.

3. Lärm und elektromagnetische Felder
Die Schallstudie im UVP-Bericht berücksichtigt die Summenwirkung
mehrerer geplanter Umspannwerke und Schaltanlagen nicht.
Grenzwerte der 26. BImSchV (elektromagnetische Felder) sind
nachzuweisen.

Wir bitten um Berücksichtigung dieser Einwendungen und
vorherige Unterrichtung über den Erörterungstermin.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Verbandsklage | § 52 Abs. 1 GKG; Auffangwert EUR 5.000 oder Orientierungswert Streitwertkatalog Verwaltungsgerichtsbarkeit; BVerwG-Streitwerte bei Großvorhaben bis EUR 100.000 | Keine wirtschaftlichen Eigeninteressen des Verbands |
| Streitwert Anlieger | Wert der Eigentumsbeeinträchtigung; Entschädigungsforderung; typisch EUR 10.000–50.000 | § 52 Abs. 1 GKG nach wirtschaftlichem Interesse |
| Eilantrag Streitwert | Hälfte des Hauptsache-Streitwerts | Beschlussmäßige Entscheidung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
| Kostenprivileg Verbände | Art. 9 Abs. 4 Aarhus: Kosten dürfen nicht prohibitiv sein | Ermäßigung nach § 162 Abs. 3 VwGO beigeladener Verband |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Klagefrist 1 Monat läuft | Sofortige Klage mit vorläufiger Begründung; Akteneinsicht parallel beantragen; Frist unbedingt wahren |
| Sofortvollzug angeordnet | Eilantrag § 80 Abs. 5 VwGO; § 80 Abs. 3-Mangel als eigenständigen Aufhebungsgrund geltend machen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Anlieger Grundstück betroffen | Entschädigungsanspruch frühzeitig beziffern; Wertgutachten vor Baubeginn; ggf. zivilrechtliche Entschädigungsklage |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Anschluss-Skills

- `energieanlagen-bimschg-genehmigung-verfahren` — BImSchG-Genehmigung angrenzender Anlagen
- `eilantrag-80-abs-5-vwgo` — Vertiefung Eilantrag-Schriftsatz
- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Grundlagen einstweiliger Rechtsschutz

## Aktuelle Leitentscheidungen (v14.2 Ergaenzung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- EnLAG §§ 1, 4
- BBPlG, NABEG §§ 18, 50
- WindSeeG, LNG-Beschleunigungsgesetz
- EnWG § 28r (H2-Stammnetz), § 18 (Entschädigung)
- VwGO §§ 50, 74, 80, 80a, 113, 146
- UmwRG §§ 2, 3
- BNatSchG §§ 13, 44
- UVPG
- Aarhus-Konvention Art. 9 / EU-RL 2003/35
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
