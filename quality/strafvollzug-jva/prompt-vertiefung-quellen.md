# 1. Quellenprüfung zur Vertiefung der JVA-Prompts

Prüfdatum: **16.10.2026**. Ziel ist ein konkret belegter Werkstattablauf und ein lesbarer Mini-Prompt. Zwölf zusätzliche Entscheidungsanker ergänzen die sechs bereits geprüften Anker des Komponentenstands 1.0.0. Die ursprünglichen sechs Texte wurden in dieser Teilaufgabe nicht verändert; ihre Erstprüfung ist im bisherigen Prüfbericht dokumentiert. Die konsolidierte [Rechtsprechungsreferenz](../../strafvollzug-jva/references/rechtsprechung.md) enthält damit achtzehn Entscheidungen.

# 2. Tatsächlicher Abruf und Lesemethode

Die neue Recherche begann mit thematischen Suchen einschließlich gezielter Suchen nach 2024, 2025 und 2026. Suchauszüge und Pressemitteilungen wurden nur als Wegweiser benutzt. Alle zwölf übernommenen Quellen wurden danach als amtlicher HTML-Volltext unmittelbar von bundesverfassungsgericht.de beziehungsweise gesetze-bayern.de abgerufen. Einzelne Aufrufe im Webleser scheiterten; der direkte Abruf über HTTPS mit regulärer Zertifikatsprüfung lieferte den vollständigen Entscheidungstext. Die unten angegebenen Randnummern wurden tatsächlich gelesen und mit Tenor, Verfahrensart und Ausgangssachverhalt abgeglichen.

Die unveränderten HTML-Dateien und daraus extrahierte Arbeitsauszüge liegen im temporären Arbeitsverzeichnis `/tmp/jva-prompt-quellen`; die Originalbytes werden durch die nachfolgenden SHA-256-Werte bezeichnet. Diese lokalen Arbeitsspeicher sind keine dauerhaften Downloadangebote. Die nachprüfbaren amtlichen URLs bleiben daher der eigentliche Quellenzugang. Roh-HTML wird nicht in das Repository aufgenommen. Beim bayerischen Arbeitsauszug wurde eine fehlerhafte automatische Zeichensatzerkennung erkannt und durch ausdrückliche UTF-8-Decodierung berichtigt; Rn. 19–27 wurden anschließend nochmals lesbar geöffnet. Die Originaldatei und ihr Hash blieben unverändert.

Die Befunde sind eigenständig formuliert. Im Volltext genannte Literatur und weitere Gerichtsentscheidungen werden nicht als selbst geprüfte Nachweise übernommen. Jede Ergänzung enthält Sachbezug, „Trägt“, „Trägt nicht“ und eine konkrete Arbeitsfolge. Kein zusätzlicher Anker stammt aus bloßem Modellwissen.

# 3. Gelesene Quellen und Reichweitengrenzen

## 3.1. Familie und Langzeitbesuch

**BVerfG, Beschl. v. 21.09.2018 – Az. 2 BvR 1649/17, Rn. 28–43**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2018/09/rk20180921_2bvr164917.html).

Abruf: 16.10.2026. Dateigröße: 178682 Bytes. SHA-256: `a8ad5bb59ab44398d8d8a8e6f368f79a155b79c49450dfbed04b5713aa85d696`.

**Gelesener Befund:** Familienkontakt ist auch unabhängig von seinem konkreten Resozialisierungsnutzen grundrechtlich geschützt. Die Versagung eines Langzeitbesuchs benötigt nachvollziehbare tatsächliche Gründe. Bloß behauptete Unzuverlässigkeit und ungeklärte Vermutungen über Gefahren für den Besuch tragen die Entscheidung nicht. Bei begleiteten Ausführungen muss geprüft werden, ob die Begleitung das angeführte Risiko beherrscht; die Anforderungen sind nicht mit offenem Vollzug gleichzusetzen.

**Ausdrückliche Grenze:** Rn. 40 lässt ausdrücklich offen, ob aus der Verfassung ein unmittelbarer Anspruch auf unüberwachten Langzeitbesuch folgt. Historische Besuchszeiten werden nicht als Berliner Recht von 2026 übernommen. Auch langjährige Haft macht jede Besuchsgestaltung nicht automatisch zulässig.

## 3.2. Frauen und Männer: Ausstattung und Geschlechterstereotype

**BVerfG, Beschl. v. 07.11.2008 – Az. 2 BvR 1870/07, Rn. 18–28**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2008/11/rk20081107_2bvr187007.html).

Abruf: 16.10.2026. Dateigröße: 140935 Bytes. SHA-256: `226749aebef8c3e76b5932ad9ade286e13992e65e3bf96ad1506e68138b092c0`.

**Gelesener Befund:** Geschlechterstereotype und tradierte Rollenerwartungen rechtfertigen keine Benachteiligung. Auch neutral formulierte Ausstattungsvorgaben können eine mittelbare Benachteiligung bewirken. Die Anstalt darf Unterschiede nicht beliebig durch verschiedene Ausstattung erzeugen und anschließend damit begründen. Die behaupteten Sicherheitsunterschiede müssen konkret, erfahrungsbasiert und überprüfbar sein; eine gemeinsame hohe Sicherheitsstufe erklärt für sich keine unterschiedliche Behandlung.

**Ausdrückliche Grenze:** Keine ausnahmslos identische Ausstattung jeder Abteilung. Rn. 24 lässt sachgerecht belegte Sicherheitsunterschiede als Rechtfertigung mittelbar verschiedener Behandlung zu. Die Entscheidung legt weder aktuelle Telefonbudgets noch ein universelles Einkaufsrecht fest.

## 3.3. Ernährung aus religiösen und ethischen Gründen: aktueller Gegenanker

**BayObLG, Beschl. v. 04.09.2025 – Az. 203 StObWs 239/25, Rn. 19–27**; [amtlicher Volltext](https://www.gesetze-bayern.de/Content/Document/Y-300-Z-BECKRS-B-2025-N-28018).

Abruf: 16.10.2026. Dateigröße: 41218 Bytes. SHA-256: `369625a5f3de75cf18af81c9121f3568abfa674aacbe090957853705968a3cfb`.

**Gelesener Befund:** Der Senat akzeptiert im konkreten bayerischen Fall die Berücksichtigung ethischer Überzeugungen entsprechend religiösen Speisevorschriften, verlangt aber keine Umsetzung sämtlicher Ernährungsgebote durch eine zusätzliche Speiselinie. Er billigt die Kombination aus vegetarischer, laktosefreier Anstaltskost und ergänzendem Eigenerwerb. Ressourcen und Küchenorganisation gehören in die Einzelfallabwägung. Rn. 27 hebt die vorherige Befassung der JVA mit zusätzlich gewünschten Alternativen hervor.

**Ausdrückliche Grenze:** Kein bundesweites Verbot veganer Kost, keine ernährungsmedizinische Feststellung und kein Freibrief, Weltanschauungen zu ignorieren. Die Versorgung mittelloser Menschen darf nicht ohne Prüfung von Landesrecht, Gesundheitsbedarf und tatsächlichem Zugang als geklärt gelten. Die Aussage des Gerichts zur Finanzierung ist als dessen Rechtsauffassung, nicht als ungeprüfte bundesweite Regel wiederzugeben. Kein stattgebender Hauptsachetenor.

## 3.4. Gesundheitsdaten und Zugang zu Prozesskostenhilfe

**BVerfG, Beschl. v. 28.07.2022 – Az. 2 BvR 1814/21, Rn. 17–23**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2022/07/rk20220728_2bvr181421.html).

Abruf: 16.10.2026. Dateigröße: 139496 Bytes. SHA-256: `cad46cdfdebf167873b38e994d9937fa2e027d93e9e39dcd3bc06b2058ad9006`.

**Gelesener Befund:** Die Erfolgsaussichtsprüfung darf das Hauptsacheverfahren nicht vollständig vorwegnehmen. Die mögliche Verletzung informationeller Selbstbestimmung durch Offenbarung von Gesundheitsdaten kann Gegenstand eines Antrags nach § 109 StVollzG sein. Die Bezeichnung als bloße Wissenserklärung schließt Rechtsschutz nicht aus. Ob die konkrete Datenweitergabe durch eine Offenbarungsbefugnis gedeckt war, musste in der Hauptsache geklärt werden.

**Ausdrückliche Grenze:** Kein generelles Verbot jeder Mitteilung des medizinischen Dienstes an andere Anstaltsbereiche. Keine abschließende Entscheidung über die Zulässigkeit der konkreten Offenbarung und kein Urteil über einen Anspruch auf vegetarische Kost. Prozesskostenhilfe ist nicht schon wegen Inhaftierung automatisch zu bewilligen.

## 3.5. Durchsuchung: konkrete Prüfung statt bloßem Formularhaken

**BVerfG, Beschl. v. 23.09.2020 – Az. 2 BvR 1810/19, Rn. 21–32**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2020/09/rk20200923_2bvr181019.html).

Abruf: 16.10.2026. Dateigröße: 151398 Bytes. SHA-256: `c35bf01e2e2a636db467f6b7859064b37b2ddfc1612b5d3440f30850c69cfac5`.

**Gelesener Befund:** Einzelfall- und Allgemeinanordnung sind nach der jeweiligen gesetzlichen Grundlage zu unterscheiden. Die Entscheidung muss eine Abweichung erlauben, wenn Missbrauch fernliegt oder gleich geeignete mildere Mittel bestehen. Das bloße Ankreuzen eines Formblatts belegt keine sorgfältige Ermessensausübung. Eine zusätzliche anwesende Person zu Ausbildungszwecken erfordert eine am Persönlichkeitsrecht orientierte Prüfung. Organisatorische Alternativen dürfen nicht übergangen werden.

**Ausdrückliche Grenze:** Kein ausnahmsloses Verbot von Entkleidungsdurchsuchungen oder der Teilnahme von Auszubildenden. Nicht jede fehlende schriftliche Einzelbegründung beweist bereits die Rechtswidrigkeit; zu untersuchen ist die tatsächlich vorgenommene Prüfung. Die bayerischen Tatbestände werden nicht ungeprüft auf andere Länder übertragen.

## 3.6. Durchsuchung: rechtmäßige Sicherheitsentscheidung als Gegenprobe

**BVerfG, Beschl. v. 27.03.2019 – Az. 2 BvR 2294/18, Rn. 17–26**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2019/03/rk20190327_2bvr229418.html).

Abruf: 16.10.2026. Dateigröße: 141562 Bytes. SHA-256: `742ad6af9a2973124c32cdb3524a4cd5bef8a65658fa6ae06da49b1a27fa845c`.

**Gelesener Befund:** In gesetzlich besonders geregelten Gefahrensituationen kann eine abstrakte Gefahr für eine Allgemeinanordnung genügen; ein individueller Schmuggelverdacht ist dort nicht stets erforderlich. Auch ein persönlich unauffälliger Gefangener kann durch andere unter Druck geraten. Gleichzeitig müssen Ausnahmemöglichkeiten, schonende Durchführung und gleich geeignete mildere Mittel geprüft werden. Im konkreten Fall beanstandete das Gericht die Begründung nicht.

**Ausdrückliche Grenze:** Keine pauschale Unbedenklichkeit jeder Durchsuchung nach jedem Besuch. „Abstrakte Gefahr“ ersetzt weder die gesetzlich geregelte Situation noch die Prüfung des konkreten Ablaufs und der Ausnahmen. Nichtannahme bedeutet nicht, dass sämtliche denkbaren Alternativen materiell abschließend geprüft wurden; Rn. 26 lässt eine Frage mangels Substantiierung offen.

## 3.7. Disziplin: Schuld, Beweise und fortwirkende Nachteile

**BVerfG, Beschl. v. 07.04.2020 – Az. 2 BvR 1935/19, Rn. 25–35**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2020/04/rk20200407_2bvr193519.html).

Abruf: 16.10.2026. Dateigröße: 151820 Bytes. SHA-256: `38755d423b77a53c4a485154985bfdd6e430c6494b36fedce845221eda46ccb6`.

**Gelesener Befund:** Disziplinarmaßnahmen sind strafähnliche Sanktionen und setzen einen zweifelsfrei festgestellten schuldhaften Pflichtverstoß voraus. Substantiiertes Bestreiten darf nicht durch unkritische Übernahme knapper Anstaltsvermerke erledigt werden. Gesundheitszustand, Chronologie und konkret benannte Beweise können entscheidend sein. Auch nach Vollzug der Sanktion können Akteneintrag und mögliche Nachteile für Lockerungen oder Bewährung ein Rechtsschutzinteresse tragen.

**Ausdrückliche Grenze:** Kein Vorrang der Gefangenenschilderung und kein Zwang, jede offensichtlich unerhebliche Behauptung beliebig weiter zu erforschen. Das Gericht darf weitere Ermittlungen aus konkreten fallbezogenen Gründen für entbehrlich halten. Eine Disziplinarmaßnahme ist nicht allein wegen eines daneben geführten Strafverfahrens ausgeschlossen.

## 3.8. Disziplin: Eilrechtsschutz gegen den sofortigen Vollzug

**BVerfG, Beschl. v. 21.01.2015 – Az. 2 BvR 1856/13, Rn. 10–16**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2015/01/rk20150121_2bvr185613.html).

Abruf: 16.10.2026. Dateigröße: 132365 Bytes. SHA-256: `b77dc9fd86f85f5de5c6fd665a909098eed2da45439662608178c0aee26e062b`.

**Gelesener Befund:** Die Aussetzung einer belastenden Maßnahme ist nicht schon deshalb eine unzulässige Vorwegnahme der Hauptsache, weil sich der Zeitraum ihrer Aussetzung nicht rückgängig machen lässt. Entscheidend ist, dass die Maßnahme bei entsprechendem Ausgang der Hauptsache wieder in Geltung gesetzt werden kann. Erforderlich ist die für diese Antragsart vorgesehene Interessenabwägung. Das Gericht darf nicht die sanktionierte Handlung oder die tragenden Pflichtwidrigkeitsgründe durch andere ersetzen.

**Ausdrückliche Grenze:** Keine automatische Aussetzung jeder Disziplinarsanktion. Kein allgemeines Recht auf unbeschränkte Schreibhilfe. Ob im konkreten Fall zusätzlich die verzögerte Entscheidung und unzureichende Sachaufklärung selbstständig verfassungswidrig waren, ließ Rn. 16 offen.

## 3.9. Disziplin: keine gerichtliche Ersetzung der Anstaltsentscheidung

**BVerfG, Beschl. v. 24.10.2006 – Az. 2 BvR 30/06, Rn. 22–29**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2006/10/rk20061024_2bvr003006.html).

Abruf: 16.10.2026. Dateigröße: 149424 Bytes. SHA-256: `1059c5c1cdbfcb4166b4ca24a67265fffe8ebe00079814cd3efe304af80914f7`.

**Gelesener Befund:** Das Gericht kontrolliert die tatsächlich verhängte Sanktion einschließlich der zugehörigen Ermessensausübung. Es übt keine eigene Disziplinargewalt aus. Konkretes Verhalten und Schuld müssen festgestellt werden; ein bloßer Verdacht reicht nicht. Ein anderer plausibler Pflichtvorwurf kann die angegriffene Sanktion nicht nachträglich tragen.

**Ausdrückliche Grenze:** Keine Aussage, dass Rechtsdienstleistungen in Haft unbegrenzt erlaubt sind. Das damalige Rechtsberatungsgesetz ist kein heutiger Prüfungsmaßstab. Ein verlorener Prozess beweist für sich keinen Gehörsverstoß; die Entscheidung trennt fehlende Sachaufklärung von bloßer Unzufriedenheit mit dem Ergebnis.

## 3.10. Gerichtsuntätigkeit: aktueller Anker und Grenze des Verfassungseilverfahrens

**BVerfG, Beschl. v. 21.01.2025 – Az. 2 BvQ 2/25, Rn. 10–13**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/01/qk20250121_2bvq000225.html).

Abruf: 16.10.2026. Dateigröße: 110867 Bytes. SHA-256: `d964dcf69a5c9f3eac123f3fc1b391a1066b084a2b1d0a1697f9e65b55f64780`.

**Gelesener Befund:** Eine Verletzung effektiven Rechtsschutzes lag bei dem dokumentierten Stillstand nahe. Allgemeiner Personalmangel oder hohe Verfahrensbelastung rechtfertigen eine überlange Dauer nicht. Gerichte besitzen zwar Spielraum bei Prioritäten, der Staat muss aber angemessen zeitnahe Entscheidungen ermöglichen. Für den verfassungsgerichtlichen Eilrechtsschutz gelten deutlich engere Voraussetzungen als für den fachgerichtlichen.

**Ausdrückliche Grenze:** Keine allgemeine Entscheidungsfrist von 17 Monaten. Keine abschließende stattgebende Hauptsacheentscheidung und keine automatische Verfassungsbeschwerde wegen jeder Verzögerung. Die Behauptung eines Rechtsverstoßes ersetzt nicht die Darlegung schwerer Nachteile im Verfassungseilverfahren.

## 3.11. Fixierung: verfassungsrechtliche Leitlinie mit begrenzter Übertragung

**BVerfG, Urt. v. 24.07.2018 – Az. 2 BvR 309/15 und 2 BvR 502/16, Rn. 63–70 und 79–85**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2018/07/rs20180724_2bvr030915.html).

Abruf: 16.10.2026. Dateigröße: 317686 Bytes. SHA-256: `58c6da9e26c3fc1f20775243f8fac8d5489d432d0e63bc340beb7987700f0eec`.

**Gelesener Befund:** Nicht nur kurzfristige vollständige Fixierung kann eine eigenständige Freiheitsentziehung trotz bestehender Unterbringung sein. Gesetzliche Grundlage, erneuter Richtervorbehalt, strikte Verhältnismäßigkeit, Überwachung, Dokumentation und Hinweis auf nachträglichen Rechtsschutz sind wesentlich. Rn. 68 nennt für die dortige Fünf- beziehungsweise Siebenpunktfixierung als Regelorientierung die absehbare Unterschreitung von ungefähr einer halben Stunde. Isolation ist nicht automatisch ein milderes Mittel.

**Ausdrückliche Grenze:** Keine halbstündige Erlaubnis zur Fixierung ohne Rechtsgrundlage, keine Gleichsetzung jeder Fesselung mit vollständiger Fixierung und keine ungeprüfte Übernahme psychiatrischer Zuständigkeiten in die JVA. Die Anforderungen an ärztliche Anordnung und Eins-zu-eins-Betreuung stehen im konkreten Unterbringungskontext; das aktuelle Vollzugsgesetz bleibt zu prüfen.

## 3.12. Absonderung: Entscheidung aus 2026 als ausdrücklich begrenzter Schnittstellenanker

**BVerfG, Beschl. v. 20.04.2026 – Az. 2 BvR 1650/24, Rn. 32–46**; [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2026/04/rk20260420_2bvr165024.html).

Abruf: 16.10.2026. Dateigröße: 139641 Bytes. SHA-256: `d02e152062868ed679628de8c4fea9de61875ea0f5f06c9c1c83ac1a9943da4a`.

**Gelesener Befund:** Mit zunehmender Dauer wachsen Eingriffsgewicht und Anforderungen an Verhältnismäßigkeit und Rechtsschutz. Gesundheitsfolgen, tatsächliche Kontakte, Schutz Dritter, konkrete Gefahren, alternative Maßnahmen und laufende Überprüfung gehören in die Gesamtbetrachtung. Rn. 46 verlangt trotz Nichtannahme, jede Möglichkeit zur Reduzierung der Gefährlichkeit zu ergreifen; dazu können alternative diagnostische und therapeutische Ansätze gehören. Ein Rechtsbehelf muss sich mit den tragenden Sicherheitsgründen auseinandersetzen.

**Ausdrückliche Grenze:** Weder Billigung beliebiger jahrelanger Einzelhaft noch pauschaler Anspruch auf sofortige Aufhebung jeder Isolation. Keine Übertragung des bremischen Psychiatriegesetzes auf eine JVA. Die im Beschluss zitierten EGMR-Entscheidungen sind hier nicht selbst am Original geprüft und dürfen nicht als eigenständig verifizierte Zusatzanker erscheinen.

# 4. Bewusst nicht übernommene Recherchefunde

Der amtliche Beschluss vom 08.03.2024 – Az. 2 BvR 1480/23 wurde ebenfalls vollständig abgerufen und insbesondere in Rn. 25–47 gelesen. Er betrifft Fesselungen bei Ausführungen in der Sicherungsverwahrung. Er wurde nicht als zusätzlicher Anker aufgenommen, weil die bereits belegten Lockerungs- und Sicherheitslinien den Schwerpunkt der Erwachsenenstrafhaft besser abdecken. Die Abgrenzung verhindert eine Auffüllung der Sammlung allein mit aktuellen, aber anders gelagerten Fällen.

Weitere Suchtreffer über Auslieferung, ausländische Vollzugssysteme oder asylrechtliche Durchsuchungen wurden nicht in allgemeine Regeln für deutsche Strafgefangene umformuliert. Der tatsächlich aufgenommene Beschluss aus 2026 wird ausdrücklich als Maßregelvollzugsfall abgegrenzt. Er dient der Prüfung fortdauernder Sicherungsmaßnahmen, ihrer Gesundheitsfolgen und konkreter Möglichkeiten zur Risikoreduzierung; das Datum allein begründet keine Übertragung. Die psychiatrische Fixierungsentscheidung von 2018 erhält dieselbe klare Zuständigkeits- und Statusgrenze.

# 5. Inhaltlicher Selbsttest

1. Ein Familienbesuchsfall darf aus Rn. 40 des Beschlusses von 2018 keinen abschließend anerkannten unmittelbaren Anspruch auf unüberwachten Langzeitbesuch ableiten.
2. Ein Geschlechtervergleich darf weder Stereotype noch die Behauptung vollständiger Ausstattungsgleichheit übernehmen; tatsächliche Sicherheitsunterschiede bleiben prüfbar.
3. Beim veganen Essen muss der Text erkennen lassen, dass das BayObLG nach Erledigung über Kosten entschied. Seine Finanzierungsauffassung wird nicht zur ungeprüften bundesweiten Regel.
4. Der Gesundheitsdatenfall von 2022 begründet Zugang zur Hauptsachenprüfung, entscheidet aber nicht über vegetarische Kost und nicht abschließend über die Offenbarungsbefugnis.
5. Die Durchsuchungsanker von 2019 und 2020 werden gemeinsam gelesen: keine pauschale Erlaubnis und kein pauschales Verbot; Anlass, Ausnahmen, Alternativen und Dokumentation tragen die Prüfung.
6. Die Disziplinaranker verlangen konkrete Tat- und Schuldfeststellung. Die gerichtliche Kontrolle darf weder den Tatvorwurf austauschen noch die Darstellung einer Seite ungeprüft zur Wahrheit erklären.
7. Der abgelehnte Verfassungseilantrag aus 2025 wird nicht als stattgebende Entscheidung dargestellt. Die dort erwähnten 17 Monate sind keine allgemeine gesetzliche Entscheidungsfrist.
8. Die Fixierungsentscheidung begründet keine erlaubnisfreie halbe Stunde. Psychiatrische Unterbringung, Maßregelvollzug und Strafhaft bleiben getrennte Ausgangslagen.
9. Der Nichtannahmebeschluss von 2026 erlaubt keine jahrelange routinemäßige Isolation. Seine Forderung nach fortlaufender Prüfung von Reduktionsmöglichkeiten bleibt im Anker erhalten.
10. Die sechs bisherigen Entscheidungen bleiben erhalten. Keine ungeprüften Parallelfundstellen, Kommentarstellen oder neuen Entscheidungsaktenzeichen wurden ergänzt.

Ergebnis dieser Teilprüfung: Die zwölf neuen Anker bestehen die vorgenannten Reichweitenkontrollen. Die technische Prüfung der Prompt-Dateien, Lesefassungen, Hashes und Release-Pakete erfolgt im Gesamtprüfbericht; dieser Quellenbericht behauptet dafür keinen vorweggenommenen Testlauf.
