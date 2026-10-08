# Bug Hunt v2.10.0

Stand: 11.07.2026

## Ziel und Methode

Geprüft wurden 249 Skills, drei Pluginrollen, sieben Testakten, Promptgeneratoren, Navigation, Evaluationslogik und Release-Pipeline. Ein Befund zählt nur, wenn er auf eine konkrete Datei, Rechtsaussage oder reproduzierbare Prüflücke zurückgeführt und im selben Release behoben oder durch einen Regressionstest gesperrt wurde.

## 1. Skill-Erkennung: 98 Rollenfehler

In 30 Skillpaaren waren die Frontmatter-Beschreibungen von Bieter- und Auftraggeberseite identisch. Das ergab 60 einzelne Routingdefekte, weil die Auswahlfunktion die Perspektive nicht unterscheiden konnte:

| Befunde | Skillpaar |
| ---: | --- |
| 1-2 | `vergaberecht-tatbestand-beweis-und-belege` |
| 3-4 | `orientierung-mandat-anwaltliche-vertiefung` |
| 5-6 | `uvgo-fristen-form-und-zustaendigkeit` |
| 7-8 | `verg-rahmenvereinbarung-konzession-spezial` |
| 9-10 | `sektvo-dokumentenmatrix-und-lueckenliste` |
| 11-12 | `orientierung-fehlerkatalog` |
| 13-14 | `workflow-chronologie-und-belegmatrix` |
| 15-16 | `vertiefung-vergabesperre-korruption-selbstreinigung` |
| 17-18 | `quellen-livecheck` |
| 19-20 | `vergabesperre-korruption-selbstreinigung` |
| 21-22 | `bieterfragen-antworten-management` |
| 23-24 | `architektenrecht-compliance-dokumentation-und-akte` |
| 25-26 | `unterlagen-luecken` |
| 27-28 | `workflow-fristen-und-risikoampel` |
| 29-30 | `konzvgv-risikoampel-und-gegenargumente` |
| 31-32 | `schnittstelle-zahlen-schwellen-und-berechnung` |
| 33-34 | `vertiefung-orientierung` |
| 35-36 | `output-waehlen` |
| 37-38 | `de-facto-vergabe-135-gwb-fristen` |
| 39-40 | `it-sicherheits-vergabe-bsi-it-sig-2` |
| 41-42 | `erstpruefung-und-mandatsziel` |
| 43-44 | `vertiefung-it-sicherheits-vergabe-bsi-it-sig-2` |
| 45-46 | `angebotsoeffnung-formfehler-preisblatt` |
| 47-48 | `eu-schwelle-vergabeordnung-richtlinie-2014-24` |
| 49-50 | `vergabesenat-quellenkarte` |
| 51-52 | `verg-nachpruefungsverfahren-spezial` |
| 53-54 | `workflow-unterlagen-lueckenliste` |
| 55-56 | `ungewoehnlich-niedriges-angebot` |
| 57-58 | `verg-mehrparteien-konflikt-und-interessen` |
| 59-60 | `wettbewerbsregister-abfrage-selbstreinigung` |

Die Beschreibungen sind jetzt rollenfest. Zusätzlich waren 19 Skillpaare im Inhalt wortgleich; das ergab 38 weitere Rollenfehler. Sie erhielten spezifische Bieter- beziehungsweise Auftraggeberaufträge:

| Befunde | Skillpaar |
| ---: | --- |
| 61-62 | `vergaberecht-tatbestand-beweis-und-belege` |
| 63-64 | `orientierung-mandat-anwaltliche-vertiefung` |
| 65-66 | `uvgo-fristen-form-und-zustaendigkeit` |
| 67-68 | `verg-rahmenvereinbarung-konzession-spezial` |
| 69-70 | `sektvo-dokumentenmatrix-und-lueckenliste` |
| 71-72 | `orientierung-fehlerkatalog` |
| 73-74 | `vertiefung-vergabesperre-korruption-selbstreinigung` |
| 75-76 | `vergabesperre-korruption-selbstreinigung` |
| 77-78 | `architektenrecht-compliance-dokumentation-und-akte` |
| 79-80 | `workflow-fristen-und-risikoampel` |
| 81-82 | `konzvgv-risikoampel-und-gegenargumente` |
| 83-84 | `schnittstelle-zahlen-schwellen-und-berechnung` |
| 85-86 | `vergaberechtliche-pruefung-anwaltlich` |
| 87-88 | `vertiefung-orientierung` |
| 89-90 | `erstpruefung-und-mandatsziel` |
| 91-92 | `eu-schwelle-vergabeordnung-richtlinie-2014-24` |
| 93-94 | `vergabesenat-quellenkarte` |
| 95-96 | `verg-nachpruefungsverfahren-spezial` |
| 97-98 | `verg-mehrparteien-konflikt-und-interessen` |

`validate-skill-discovery.py` sperrt künftig sowohl pluginübergreifend identische Beschreibungen als auch identische Skilltexte.

## 2. Test- und Evaluationssystem: Befunde 99 bis 120

99. Sechs reale Testakten hatten keine `rubric.yaml`; alle sieben Akten besitzen nun fallbezogene Rubrics.
100. Die einzige vorhandene Rubric enthielt `plugin: tbd`; ersetzt durch `rollenverbund`.
101. Ein fachfremder BAG-Hinweis stand in einer Vergaberechtsrubric; entfernt.
102. Beschreibung und Mindestzahl des Dateichecks widersprachen sich; korrigiert.
103. Der Rubric-Generator behandelte `megaprompts` als Testakte; ausgeschlossen.
104. Der Generator konnte unbekannte Plugins als `tbd` ausgeben; geschlossenes Rollenmodell eingeführt.
105. Der Generator suchte Einzel-PDFs im falschen Ordner; auf `einzel-pdf` korrigiert.
106. Fehlende Rubrics führten im Eval-Lauf nicht zu einem Fehler; sie sind jetzt Release-Blocker.
107. Ein nicht existierender Testakten-Slug wurde nicht als eigener Strukturfehler dargestellt; behoben.
108. `yaml_field_equals` war dokumentiert, aber nicht implementiert; implementiert.
109. `json_field_equals` war dokumentiert, aber nicht implementiert; implementiert.
110. Der YAML-Fallback erkannte eingerückte Check-IDs nicht; Parser korrigiert.
111. Fehlerhaftes YAML erzeugte einen Traceback statt eines Testergebnisses; kontrollierte Fehlerausgabe ergänzt.
112. Doppelte Check-IDs wurden nicht erkannt; Schemaprüfung ergänzt.
113. Unbekannte Checktypen wurden erst spät behandelt; Schemaprüfung ergänzt.
114. Pflichtfelder je Checktyp fehlten; typbezogene Pflichtfelder ergänzt.
115. Eine Rubric konnte ohne automatischen Check bestehen; mindestens fünf werden verlangt.
116. Pfade konnten die Testakte verlassen; Pfadbegrenzung ergänzt.
117. Unsichere Glob-Muster konnten Elternpfade verwenden; gesperrt.
118. YAML- und JSON-Feldpfade konnten nicht verschachtelt sein; Punktpfade ergänzt.
119. Zeitstempel nutzten eine veraltete UTC-Schnittstelle; auf zeitzonenbewusste UTC-Zeit umgestellt.
120. Der Linkvalidator prüfte nur 18 Übersichtsdateien; er prüft jetzt den gesamten Markdown-Bestand.

## 3. Rechtsstand und Verfahren: Befunde 121 bis 157

121. Die kommunale Schweriner Vergabe war fälschlich der Vergabekammer des Bundes zugeordnet; auf die Landesvergabekammer korrigiert.
122. Der KRITIS-Bezug wurde als Zuständigkeitsgrund behandelt; § 159 Abs. 2 und 3 GWB richtig angewandt.
123. § 55 BSIG wurde als Zuständigkeitsnorm erfunden; entfernt.
124. § 1 Abs. 3 VgV wurde als Kammerzuständigkeit verwendet; entfernt.
125. Das OLG Düsseldorf war als Beschwerdegericht genannt; auf OLG Rostock korrigiert.
126. Drei Dateinamen enthielten falsche Gerichtszuständigkeiten; umbenannt und alle Verweise aktualisiert.
127. Eine De-facto-Vergabe wurde als Direktklage beim OLG behandelt; in einen VK-Nachprüfungsantrag überführt.
128. Der Dateiname `20_de_facto_vergabe_klage.md` schrieb den falschen Rechtsweg fest; umbenannt.
129. § 135 Abs. 2 GWB wurde auf 30 Tage ab bloßer Kenntnis verkürzt; qualifizierte Information, EU-Bekanntmachung und Sechsmonatsgrenze getrennt.
130. Eine Ex-ante-Transparenzbekanntmachung wurde mit der Ex-post-30-Tage-Frist verwechselt; § 135 Abs. 3 GWB mit zehn Tagen Wartezeit getrennt.
131. Die Rechtsfolge des § 135 GWB wurde als automatische bereicherungsrechtliche Rückabwicklung ausgegeben; Rechtsfolgenprüfung geöffnet.
132. Rügen wurden mit einer gesetzlichen Unverzüglichkeitsfrist begründet; feste Zehn-Kalendertage-Frist nach Nr. 1 eingesetzt.
133. Eine Drei-Werktage-Formel simulierte Fristwahrung; entfernt.
134. Eine erfundene Vier-Werktage-Antwortfrist der Vergabestelle wurde als Verfahrensstufe behandelt; als rein taktische Frist gekennzeichnet.
135. § 160 Abs. 3 Satz 1 Nr. 4 GWB wurde an Zuschlagsinformation statt Nichtabhilfe geknüpft; korrigiert.
136. Testakte 03 ordnete tatsächliche Kenntnis fälschlich Nr. 2 zu; als Unterlagenfehler Nr. 3 korrigiert.
137. Testakte 04 enthielt denselben Nr.-2-Fehler; als Unterlagenfehler Nr. 3 korrigiert.
138. Der Rügeschriftsatz nannte zehn Werktage; vollständig neu gefasst.
139. Der Rügeschriftsatz erfand eine 14-Tage-Reaktionsphase; entfernt.
140. Der Rügeschriftsatz empfahl trotz Präklusion pauschal den Nachprüfungsantrag; ersetzt durch fallbezogene Rechtswegprüfung.
141. Die aktuelle BSIG-Systematik fehlte in vier IT-Sicherheits-Skills; alle vier neu gefasst.
142. §§ 8a, 8b und 9b BSIG wurden als 2026 geltendes Recht verwendet; durch §§ 28 bis 33, 39 und 41 BSIG ersetzt.
143. Der alte Zweijahres-Nachweiszyklus wurde verwendet; § 39 BSIG mit Dreijahreszyklus und Übergang berücksichtigt.
144. Das NIS2-Umsetzungsgesetz wurde als künftig oder offen bezeichnet; Inkrafttreten am 06.12.2025 berücksichtigt.
145. Nicht-EU-Komponenten wurden pauschal einer BMI-Genehmigung unterstellt; risikobezogene Prüfung nach § 41 BSIG eingesetzt.
146. Ein 24/7-SOC wurde automatisch als System zur Angriffserkennung behandelt; Funktions- und Wirksamkeitsprüfung ergänzt.
147. Betreiberpflicht und Auftragnehmer-Zuarbeit wurden vermischt; in allen IT-Arbeitswegen getrennt.
148. C5 wurde pauschal als Zertifikat bezeichnet; Testat, Typ, Zeitraum und Scope werden nun getrennt geprüft.
149. § 126 GWB enthielt drei Jahre für § 123 und zwei Jahre für § 124; auf fünf beziehungsweise drei Jahre korrigiert.
150. Nicht belegte vermeintliche Praxis-Standardfristen zur Vergabesperre wurden entfernt.
151. Unterhalb der EU-Schwelle wurde Primärrechtsschutz pauschal ausgeschlossen; landesrechtliche Prüfstellen und gerichtliche Eilwege ergänzt.
152. § 181 GWB wurde als Grundlage für entgangenen Gewinn behandelt; auf Angebots- und Teilnahmekosten begrenzt.
153. Weiterreichende BGB-Ansprüche wurden nicht sauber getrennt; eigene Anspruchs-, Verschuldens- und Kausalitätsprüfung ergänzt.
154. Unterlassene Rüge wurde als automatischer Schadensersatzverlust behandelt; auf Kausalität und § 254 BGB zurückgeführt.
155. Der OLG-Streitwert wurde mit dem Nettoauftragswert gleichgesetzt; § 50 Abs. 2 GKG und Bruttoauftragssumme eingesetzt.
156. Kammermindestgebühr und Mindeststreitwert wurden vermischt; getrennt.
157. Eine frei erfundene lineare Gebührentabelle zu § 182 GWB wurde entfernt.

## 4. Aktenqualität und Release-Schutz: Befunde 158 bis 201

158. Das Schweriner Kostenmemo enthielt konkrete RVG-Beträge ohne belastbare Tabelle; durch freigabegesperrtes Rechenblatt ersetzt.
159. Die Kostenchronologie war nicht chronologisch; sortiert.
160. Das Schweriner Aktenzeichen war auf eine Bundeskammer zugeschnitten; konsistent auf `3 VK 4/26` umgestellt.
161. Das Beschwerdeaktenzeichen und Gericht waren inkonsistent; konsistent auf `17 Verg 2/26` und OLG Rostock umgestellt.
162. Die Schweriner BSIG-Analyse enthielt alte Registrierungstermine und Übergangsfristen; vollständig neu gefasst.
163. Die Reinigungsakte erklärte nicht, weshalb nicht das billigste Angebot gewinnt; Qualitätsbegründung ergänzt.
164. Die Laptopakte behandelte den Markenbezug nur implizit; Marken- und Gleichwertigkeitsfrage ausdrücklich gemacht.
165. Die Laptopwertung trennte Preis und Qualität sprachlich nicht klar; Matrix präzisiert.
166. Die Bauakte enthielt keinen ausdrücklichen Fristanker in der Rüge; § 160 Abs. 3 Satz 1 Nr. 3 GWB ergänzt.
167. Release-CI führte keine fallbezogenen Testakten-Evals aus; als Pflichtschritt ergänzt.
168. Release-CI kannte die neuen juristischen Regressionen nicht; Validator als Pflichtschritt ergänzt.
169. Bekannte Fehlerklassen waren nicht maschinell gesperrt; `validate-legal-regressions.py` schützt Fristen, BSIG, Zuständigkeit, Kosten, § 126, § 135, § 160, § 181 und Unterschwellenrechtsschutz.
170. Der Gesamt-PDF-Builder behandelte den Hilfsordner `testakten/megaprompts` als achte Testakte; der Ordner ist nun ausgeschlossen und das sachfremde PDF entfernt.
171. In der Reinigungsakte erhielten zwei unterschiedlich teure Angebote beide 70 Preis-Punkte; Formel, Punkte und Gesamtrang wurden korrigiert.
172. In der Laptop-Bieterfrage stimmte der Dokumentkopf nach der Präzisierung nicht mit der Überschrift überein; Betreff und Briefkopf synchronisiert.
173. Der CSV-Generator schrieb Plattformprotokolle mit systemabhängigen CRLF-Enden und erzeugte dadurch fehlerhafte Whitespace-Diffs; der Dialekt ist jetzt deterministisch auf LF festgelegt.
174. Nach der Korrektur von Vergabekammer und Beschwerdegericht blieben drei alte DOCX-Ableitungen mit Bundeskammer, OLG Düsseldorf und falschem Klageweg im Downloadbestand; der Builder migriert bekannte Quellumbenennungen und der Echtformat-Validator sperrt jedes Wiederauftreten.
175. Der neue Eval-Schalter `--allow-missing` versprach fehlende Rubrics zu tolerieren, wertete sie intern aber weiterhin als Fehlschlag; der widersprüchliche Nebenpfad wurde entfernt und die Release-Regel bleibt eindeutig strikt.
176. Fehlerhaftes YAML-Frontmatter in einer geprüften Markdown-Datei konnte den Eval-Lauf trotz kontrollierter Rubric-Fehlerbehandlung mit Traceback abbrechen; Parserfehler werden nun als reproduzierbares negatives Checkergebnis behandelt.
177. Der juristische Regressionsscan erfasste Plugins und Testakten, ließ aber gemeinsame Referenzen, Skill-Indizes und weitere Root-Dokumentation aus; der Scan deckt jetzt 417 relevante Markdown-Dateien ab.
178. Die Standard-Rubric zählte für die Mindestzahl der Aktenstücke jede Markdown-Datei einschließlich README und Beilagen; das Glob-Muster verlangt nun ausdrücklich drei nummerierte Quellen `NN_*.md`.
179. Die beiden Kurzskills zur De-facto-Vergabe nannten nur pauschal 30 Tage und sechs Monate, ohne die qualifizierten Fristauslöser des § 135 Abs. 2 GWB zu erklären; Information mit Gründen, EU-Bekanntmachung und absolute Grenze stehen nun ausdrücklich im Kernworkflow.
180. Das zentrale Skill-Routing verkürzte denselben Prüfpfad auf `Kenntnis, 30 Tage, sechs Monate` und konnte dadurch gerade die falsche Fristanknüpfung reaktivieren; der Router nennt jetzt die beiden qualifizierten Auslöser und die Ex-ante-Wartezeit.
181. Bieter- und Auftraggeber-Kurzskill unterschieden sich fachlich fast nur in Description und Anschlusslinks; sie besitzen nun getrennte Angriffs- beziehungsweise Freigabeketten, Beweisaufträge und Outputpakete.
182. Die mehrdeutige §-135-Kurzformel war vom Regressionsvalidator nicht erfasst; beide Varianten sind jetzt releaseblockierend gesperrt.
183. Der Bieter-Skill `ruegeschriftsatz-erstellen` ordnete die Antragsbefugnis § 160 Abs. 1 GWB zu; korrigiert auf § 160 Abs. 2 GWB mit Interesse, eigener Rechtsverletzung und Schaden.
184. Die Regression gegen diesen Normfehler erkannte nur die Wortfolge `Antragsbefugnis ... § 160 Abs. 1`, nicht die in Tabellen übliche umgekehrte Reihenfolge; beide Richtungen sind jetzt gesperrt.
185. Derselbe Skill ordnete den drohenden Schaden nochmals § 160 Abs. 1 statt Absatz 2 zu; die Gegenargumentmatrix ist korrigiert.
186. Die Rügeobliegenheit stand in der Normenkarte unter § 160 Abs. 2 statt Absatz 3; die Fristen werden anhand der Nummern 1 bis 4 des Absatzes 3 geprüft, Nummer 5 und Satz 2 zusätzlich als eigenständige Zulässigkeitsfragen.
187. Der Regressionsscan kannte die falsche Zuordnung des Schadensmerkmals nicht; beide Wortreihenfolgen werden jetzt erkannt.
188. Der Regressionsscan kannte auch die falsche Zuordnung von Rüge und Präklusion zu Absatz 2 nicht; beide Wortreihenfolgen werden jetzt erkannt.
189. Der Eignungsleitfaden vertauschte die Höchstzeiten des § 126 GWB und nannte drei Jahre für zwingende sowie fünf Jahre für fakultative Ausschlussgründe; richtig sind fünf Jahre für § 123 und drei Jahre für § 124.
190. Für diese ausgeschriebene Klammerform fehlte eine Regression; die vertauschte Kombination ist jetzt gesperrt.
191. `vertiefung-eignungspruefung` verwies für die Fünfjahresdauer auf § 123 Abs. 3 GWB statt § 126 Nr. 1 GWB; korrigiert.
192. `eignungspruefung` enthielt denselben falschen Normanker; korrigiert.
193. Der Regressionsscan sperrt künftig auch tabellarische Wirkungsdauern, die § 123 Abs. 3 statt § 126 Nr. 1 nennen.
194. Die neue Absatz-2-Regression erzeugte zunächst Fehlalarme, wenn eine Zeile Antragsbefugnis nach Absatz 2 und Präklusion korrekt nach Absatz 3 nebeneinander nannte; ein begrenzter Negativabgleich erhält diese zulässige Normenkette.
195. Der Eignungsleitfaden setzte die Tilgung im Bundeszentralregister pauschal mit dem Ablauf der vergaberechtlichen Ausschlussdauer gleich; Registerlage und § 126 Nr. 1 GWB werden nun getrennt geprüft.
196. Die unzulässige Gleichsetzung von BZRG-Tilgung und Ausschlussfrist ist jetzt als Regression gesperrt.
197. Derselbe Leitfaden verlangte bei erkennbaren Bekanntmachungsfehlern eine sofortige Rüge; korrigiert auf die Bewerbungs- oder Angebotsfrist nach § 160 Abs. 3 Satz 1 Nr. 2 beziehungsweise Nr. 3 GWB.
198. Der Regressionsscan sperrt künftig auch die pauschale Sofortformel für erkennbare Bekanntmachungs- und Unterlagenfehler.
199. Das Kernmodul zum Nachprüfungsverfahren ließ die neue Unzulässigkeit bei offensichtlichem Missbrauch nach § 160 Abs. 3 Satz 1 Nr. 5 GWB aus; Tatbestand, §-180-Verweisung und Abgrenzung zur Rügefrist sind ergänzt.
200. Der große Rüge- und Nachprüfungsworkflow enthielt denselben Reformstand nicht; Normenkarte und Prüfschritt erfassen jetzt falsche Angaben, Behinderungs- oder Schädigungsabsicht und entgeltliche Rücknahmeabsicht.
201. Für Nummer 5 und § 180 Abs. 2 GWB fehlte eine positive Aktualitätskontrolle; beide Kernskills müssen diese Normanker nun vor jedem Release enthalten.

## 5. Automatischer Review und Prüfinfrastruktur: Befunde 202 bis 204

202. Ein automatischer Codex-Reviewhinweis aus PR 4 war als veraltet, aber ungelöst zurückgeblieben. Der Fließtext erklärte den Fristbeginn nach §§ 15 bis 17 VgV inzwischen im Ansatz richtig, verwies für die 35-Tage-Frist aber auf § 15 Abs. 1 statt Abs. 2 VgV; zugleich verlangte die Dokumentationsliste weiterhin Fristen mit Bezug auf das TED-Veröffentlichungsdatum. Absendung der Bekanntmachung, Absendung der Angebotsaufforderung und Veröffentlichung werden nun getrennt belegt; die Fristberechnung knüpft ausschließlich an das jeweils maßgebliche Absendeereignis und die richtigen Absätze der §§ 15 bis 17 VgV an.
203. Für diese widersprüchliche Fristanknüpfung fehlte eine Regression. `validate-legal-regressions.py` sperrt jetzt Formeln, die VgV-Teilnahme-, Angebots- oder Mindestfristen an das Veröffentlichungsdatum knüpfen oder die 35-Tage-Frist § 15 Abs. 1 VgV zuordnen.
204. Der Smoke-Test-Runner verlor bei Unterprozessen die aktive virtuelle Python-Umgebung, weil seine Markdown-Befehle `python3` über den globalen `PATH` auflösten. Er stellt nun den eigenen Interpreter an den Anfang des Unterprozesspfads; dadurch bleiben DOCX-, XLSX-, PPTX- und PDF-Abhängigkeiten in der gesamten Prüfkette verfügbar.

## Ergebnis

- 204 konkret zugeordnete Befunde behoben.
- Keine pluginübergreifend identische Skillbeschreibung.
- Kein pluginübergreifend identischer Skilltext.
- Sieben von sieben Testakten mit vollständiger Rubric und All-Pass.
- Der vollständige Markdown-Bestand ohne kaputten lokalen Link.
- Juristische Regressionen werden vor jedem Release automatisch gesperrt.
