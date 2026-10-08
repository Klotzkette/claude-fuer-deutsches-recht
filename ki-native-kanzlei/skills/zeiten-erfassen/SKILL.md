---
name: zeiten-erfassen
description: "Verwenden, wenn tatsächliche menschliche Arbeitszeit mit Datum, Person, Minuten und Narrativ gespeichert, einem Honorarabschnitt zugeordnet, storniert oder korrigiert werden soll oder eine Zeitaufstellung als Rechnungsanlage gebraucht wird. Liefert belegte Zeiteinträge und fortgeschriebenen Rechnungsentwurf. Nicht für Honorarhöhe, Rechnung oder Zahlungen."
---

# Zeiten wahrheitsgemäß und nachprüfbar erfassen

## 1. Zweck und Anwendungsfall

### 1.1. Zeitnachweis als eigenständiges Arbeitsprodukt

Dieser Skill erzeugt einen belastbaren Zeitnachweis für eine konkret bestimmte Tätigkeit. Er verbindet Person, tatsächlichen Arbeitstag, tatsächliche Dauer, Leistungsinhalt, Mandat, Honorarphase, Abrechenbarkeit und Quelle. Er ersetzt weder die Vergütungsvereinbarung noch die rechtliche Prüfung der Rechnung. Eine tatsächlich geleistete Stunde kann nicht berechenbar sein; eine wirksam vereinbarte Pauschale kann unabhängig von der benötigten Stundenzahl geschuldet sein.

Die Zeiterfassung belegt gegenüber dem Mandanten die erbrachte Tätigkeit, ermöglicht der Kanzlei eine Nachkalkulation und liefert bestätigte Eingaben für den Rechnungsentwurf. Keine dieser Aufgaben gestattet eine Rekonstruktion vermeintlich üblicher Bearbeitungsdauern. Die Dauer wird aus tatsächlicher Angabe, zeitnaher Aufzeichnung oder ausdrücklich bestätigter Rekonstruktion übernommen. Ein langes Dokument beweist keine bestimmte Arbeitszeit; ein kurzer Text beweist nicht, dass seine Herstellung nur wenige Minuten dauerte.

### 1.2. Verantwortliche menschliche Leistung in der KI-nativen Kanzlei

Dokumentiert werden reale Tätigkeiten: Sachverhalt aufbereiten, Quellen lesen, Normfassung kontrollieren, Entwurf erarbeiten, Ergebnisse überprüfen, Besprechung führen oder Belege zuordnen. Die Laufzeit eines Modells ist keine Personenzeit. Während ein Werkzeug rechnet, kann die Person andere Arbeit erledigen; dieselben Minuten dürfen nicht zugleich als aktive Bearbeitung mehrerer Mandate angesetzt werden. Der bloße Hinweis „KI genutzt“ beantwortet keine dieser Fragen.

Eine mögliche Zeiteinsparung ist kein abrechenbarer Zeitbeleg. Erfordert eine Vertragsprüfung mit einem zugelassenen Werkzeug tatsächlich siebzig Minuten menschliche Arbeit, werden nicht die geschätzten vier Stunden einer manuellen Bearbeitung gebucht. Umgekehrt wird eine notwendige zwanzigminütige Quellenkontrolle nicht gestrichen, weil ein Modell bereits einen Entwurf geliefert hat. Maßgeblich sind wahrheitsgemäße Dauer, vereinbarter Leistungsumfang und vertretbare Bearbeitung, nicht ein Technikbonus oder Technikabschlag.

### 1.3. Auslöser, Abgrenzung und Nachbarskills

Der Skill beginnt, wenn eine Bearbeiterin nach Fertigstellung eines Schriftsatzes meldet, wie viele Minuten sie benötigt hat. Er beginnt, wenn im Journal ein Block „Bearbeitung, 180 Minuten“ steht, aus dem keine prüfbare Position entsteht, wenn ein Mandant eine Position von 95 Minuten beanstandet, wenn eine Besprechung zweimal unter verschiedenen Narrativen erfasst wurde, wenn ein Eintrag Tage nach dem Arbeitstag nachgetragen werden soll, wenn vor Rechnungsstellung eine Zeitaufstellung als Anlage benötigt wird oder wenn erfasste Minuten mit Deckel, Schätzung oder Festpreis abgeglichen werden sollen.

Die Honorargrundlage selbst wird hier nicht verhandelt oder geändert; fehlt sie oder soll ein neuer Auftrag erfasst werden, gehört das zu [honorar-budget-vereinbaren](../honorar-budget-vereinbaren/SKILL.md). Die Rechnung mit Nummer, Pflichtangaben und XRechnung erstellt [abrechnung-e-rechnung](../abrechnung-e-rechnung/SKILL.md). Zahlungseingänge, Vorschüsse und Fremdgeld ordnet [zahlungen-buchhaltung](../zahlungen-buchhaltung/SKILL.md) zu. Den versandfertigen Brief auf eine Beanstandung formuliert [mandantenkommunikation](../mandantenkommunikation/SKILL.md) auf Grundlage des hier erstellten Nachweises. Berufsrechtliche Fragen zu Dienstleistern, Werkzeugfreigabe und Verschwiegenheit prüft [anwaltsberufsrecht-pruefen](../anwaltsberufsrecht-pruefen/SKILL.md). Die Gesamtsteuerung eines Mandats liegt bei [ki-kanzlei-steuern](../ki-kanzlei-steuern/SKILL.md).

Dieser Skill schätzt keine Dauer, erfindet keine Verteilung innerhalb eines Sammelblocks, verändert keine verwendete Honorargrundlage, stellt keine Rechnung, versendet nichts und leitet kein Mahnverfahren ein.

## 2. Eingaben

### 2.1. Die kleinste vollständige Zeiteinheit

Ein Eintrag benötigt eine eindeutige ID, Mandatszuordnung, Arbeitstag, bearbeitende Person, tatsächliche ganze Minuten, verständliches Narrativ, Abrechenbarkeitsentscheidung, Bestätigungsstand, Quelle und die Honorarphase. Das Datum meint den tatsächlichen Arbeitstag; ein späterer Erfassungstag tritt nicht an seine Stelle. Bei über Mitternacht reichenden Tätigkeiten werden die Tagesanteile dokumentiert; die Zeitzone wird bei internationaler Zusammenarbeit oder widersprüchlichen Zeitstempeln geklärt.

Die Quelle kann eine zeitnahe persönliche Aufzeichnung, eine bestätigte Tätigkeitsmeldung oder eine anhand benannter Belege vorgenommene Rekonstruktion sein. Ein Kalendereintrag beweist eine geplante Besprechung, nicht deren Dauer. Ein Dateizeitstempel beweist eine Speicherung, nicht den Arbeitsbeginn. Eine Videokonferenzdauer stützt die Teilnahme, nicht die aktive Beteiligung. Die Quelle wird deshalb ihrem Beweiswert entsprechend bezeichnet.

### 2.2. Entscheidende Angaben und Vorgehen bei Lücken

| Angabe | Warum entscheidend | Vorgehen, wenn sie fehlt |
|---|---|---|
| Tatsächliche Minuten | Grundlage jedes Zeitwerts und jeder Darlegung im Streit | `minutes=null`, `confirmed=false`; Dauer gezielt erfragen, nie schätzen |
| Bearbeitende Person | Bestimmt Satz, Tagesplausibilität und Verantwortung | Eintrag nicht bestätigen; Person erfragen, nicht aus Dateiautor ableiten |
| Arbeitstag | Trennt Leistungszeitpunkt von Erfassungstag und Satzänderungen | Aus Beleg rekonstruieren; sonst offen lassen und kennzeichnen |
| Narrativ | Macht die Leistung für Mandant und Gericht prüfbar | Vorschlag aus Arbeitsprodukt formulieren, als Vorschlag kennzeichnen |
| Honorarphase (`terms_id`) | Entscheidet Satz, Deckel und Modell | `terms_id=null` setzen; Zuordnung als offene Position führen |
| Abrechenbarkeit (`billable`) | Trennt dokumentierte von berechenbarer Zeit | `billable=null`; Entscheidung der verantwortlichen Person einholen |
| Quelle | Beweiswert des Eintrags im Streitfall | Beleg benennen oder Eintrag als nachträglich rekonstruiert kennzeichnen |
| Bestätigung (`confirmed`) | Nur bestätigte Zeit fließt in den Entwurf | `false` belassen; Dokumentarbeit läuft weiter |
| Mandatsordner mit Journal | Ohne Journal keine Buchung | Eingabe als JSON vorbereiten; `init` nur bei tatsächlich neuem Mandat |
| Rolle bei Mehrfachbesetzung | Doppelbesetzung ist kein Honorarmultiplikator | Rolle erfragen; Teilnahme ohne Rolle als nicht bestätigt führen |
| Reise- oder Wartezeit | Eigener Satz oder eigene Regel möglich | Nach Vereinbarung fragen; Position vorläufig getrennt halten |
| Vorherige Rechnung zur Position | Entscheidet, ob Korrektur oder Rechnungsberichtigung | Rechnungsstand prüfen; Vermerk statt stiller Änderung |

### 2.3. Rückfragen in der richtigen Reihenfolge

Lies zuerst Akte, gespeicherten Honorarstand (Modell, Satz/Betrag, Umfang, Deckel, netto/brutto) und Zeitstand (bestätigte Minuten, offene Zeitfragen) über `status`. Stelle dann gebündelt nur die Fragen, deren Antwort fehlt, in dieser Reihenfolge. Die erste Frage lautet: „Welche Tätigkeit soll erfasst werden, und wer hat sie an welchem Tag ausgeführt?“ Die zweite Frage lautet: „Wie viele tatsächliche Minuten haben Sie aufgewendet, und worauf beruht die Angabe – zeitnahe Aufzeichnung, Erinnerung am selben Tag oder Rekonstruktion aus Kalender, Nachrichten und Versionen?“ Die dritte Frage lautet: „Gilt die gespeicherte Honorargrundlage [Phase, Modell, Satz, Deckel] für diese Tätigkeit unverändert, und ist die Zeit danach abrechenbar?“ Die vierte Frage lautet: „Ist das vorgeschlagene Narrativ zutreffend, und enthält es nichts, was der Rechnungsempfänger nicht erfahren darf?“

Ohne Antwort auf die erste Frage wird kein Eintrag angelegt. Ohne Antwort auf die zweite wird ein unbestätigter Eintrag mit `minutes=null` vorbereitet, und die beauftragte Dokumentarbeit wird abgeschlossen. Ohne Antwort auf die dritte bleibt die Zeit mit `terms_id=null` oder `billable=null` als offene Position im Entwurf. Ohne Antwort auf die vierte bleibt der Narrativvorschlag im internen Datensatz und gelangt nicht in eine Empfängerfassung. Bereits beantwortete Fragen werden nicht wiederholt.

### 2.4. Vorhandene Honorargrundlage knapp vorhalten

Lies zuerst den bestätigten Stand in der Akte und formuliere ihn knapp: „Für die außergerichtliche Prüfung gilt HV-1 mit 280 Euro netto je Stunde und einem Gesamtdeckel von 2.500 Euro netto nur für Gebühren. Der neue Eintrag betrifft die vereinbarte erste Änderungsfassung.“ Liegen alle Angaben vor, ist keine erneute Abfrage nötig. Ist die Aufgabe neu, prüfe, ob sie vom textförmig erkennbaren Anwendungsbereich der Vereinbarung umfasst ist; eine verwandte neue Aufgabe ist nicht automatisch erfasst.

Fehlt die Grundlage, klärt der Nachbarskill RVG, Zeithonorar, Festpreis, Preisangebot oder Schätzung mit oder ohne Deckel. Die Zeiterfassung wartet darauf nicht: Der Beleg wird mit `terms_id=null` angelegt, und die Zuordnung folgt später auf dem Korrekturweg.

### 2.5. Offene Zeiten sind keine Nullzeiten

Kann die Dauer noch nicht genannt werden, bleibt sie unbekannt. Ein leerer Wert wird weder als null Minuten noch als Standarddauer von fünfzehn Minuten behandelt. Ist nur die Abrechenbarkeit offen, bleibt die Dauer erhalten, während der Rechnungsbetrag noch nicht freigegeben wird. Ist die Honorarphase unbekannt, bleibt der Beleg unzugeordnet bestehen. Echte Nullminuten, etwa eine abgesagte Besprechung, werden mit `minutes=0` dokumentiert, wenn die Kanzlei den Vorgang festhalten will.

Eine spätere Bestätigung wird mit dem ursprünglichen Beleg verbunden; bereits geklärte Daten werden nicht erneut erhoben.

## 3. Ablauf und Checkliste

### 3.1. Leistung, Dauer und Berechenbarkeit nacheinander bestimmen

Prüfe zuerst, welche Leistung tatsächlich erbracht wurde. Ordne sie dem Auftrag zu und bestimme erst danach ihre wirtschaftliche Behandlung. Diese Reihenfolge verhindert, dass ein gewünschter Rechnungsbetrag rückwärts in vermeintliche Arbeitszeit übersetzt wird. Bei einem Festpreis bleiben Zeiten für Nachweis und Nachkalkulation sinnvoll, lösen aber keine Stundenforderung aus. Bei RVG belegen sie den Arbeitsablauf, begründen jedoch keinen Gebührentatbestand; das Werkzeug meldet für eine RVG-Phase ohne geprüfte manuelle Gebühr die offene Position „RVG-Berechnung fehlt; Zeiten ergeben keine RVG-Gebühr“.

Bei einem Stundensatz ergibt sich der vorläufige Zeitwert aus Minuten geteilt durch sechzig und multipliziert mit dem gültigen Satz. Ein Deckel begrenzt den berechenbaren Betrag, nicht die Wahrheit der Dauer. Ein Nachlass mindert den Rechnungsbetrag und wird nicht durch Verkürzen der Zeitaufzeichnung verdeckt. Eine nicht berechenbare Korrekturarbeit bleibt mit `billable=false` als Tätigkeit erkennbar.

### 3.2. Der Entscheidungsbaum für einen neuen Eintrag

Liegt eine konkrete Leistungsangabe vor, prüfe Person und Arbeitstag; fehlen beide, wird keine bestätigte Zeit angelegt. Stehen Leistung, Person und Tag fest, frage nach Dauer und Quelle. Ist die Dauer belegt, prüfe die Honorarzuordnung; ohne bestätigte passende Phase bleibt sie offen. Ist die Phase vorhanden, wird die Abrechenbarkeit anhand von Leistungsumfang, vertraglichen Regeln und etwaigen Zusatzfreigaben entschieden.

Sind alle Tatsachen bestätigt, erfolgt die Erfassung mit eindeutiger ID. Ergibt sich ein Widerspruch, wird nur der betroffene Eintrag zurückgestellt. Nach Speicherung werden Summen, offene Angaben und Budgetwirkung aus der Rückgabe des Werkzeugs kontrolliert. Die rechnerische Vollständigkeit (`complete=true`) ist keine Rechnungsreife; das Werkzeug gibt `invoice_ready` stets als `false` zurück.

### 3.3. Narrative so schreiben, dass die Leistung überprüfbar wird

Ein brauchbares Narrativ beschreibt Tätigkeit, Gegenstand und erforderlichen Zusammenhang. „Bearbeitung“ ist zu unbestimmt. „Prüfung der Haftungsobergrenze in Ziffer 12 des Liefervertrags und Überarbeitung der Ersatzklausel anhand der vereinbarten Risikoverteilung“ ermöglicht eine konkrete Einordnung. Die Darstellung muss keine Prozessstrategie offenlegen; der Mandant soll erkennen, welche Arbeit für sein Mandat erbracht wurde, ohne dass ein externer Prüfer unnötig sensible Informationen erhält.

Vermeide wertende Werbesprache. „Hochkomplexe strategische Analyse“ belegt weder eine Leistung noch eine Dauer. Ein präzises Narrativ kann kurz sein, wenn Gegenstand und Tätigkeit daraus klar werden. Gleichartige Tätigkeiten werden konsistent bezeichnet; der bloße Wechsel einiger Wörter macht doppelte Buchungen nicht zu unterschiedlichen Leistungen.

Ein zusammengefasster Eintrag ist nur sinnvoll, wenn die Tätigkeiten einen einheitlichen Vorgang bilden. Ein mehrstündiger Sammelblock aus Recherche, Telefonaten, E-Mails und Aktenorganisation erschwert die Kontrolle. Teile ihn anhand vorhandener Aufzeichnungen auf. Fehlen Einzelzeiten, erfinde keine Verteilung; dokumentiere die Gesamtdauer und die offene Aufschlüsselung, und die verantwortliche Person entscheidet, ob der Beleg für die Abrechnung ausreicht.

### 3.4. Rundungen und Zeittakte kontrollieren

Erfasse tatsächliche ganze Minuten ohne Aufrundung jedes einzelnen Vorgangs. Sieben Minuten sind sieben Sechzigstel einer Stunde, nicht 0,25 Stunden; zehn kurze E-Mails werden nicht jeweils zu einer Viertelstunde. Der BGH hat die formularmäßige Abrechnung jedes angefangenen Viertelstundenintervalls jedenfalls gegenüber Verbrauchern als unangemessene Benachteiligung beanstandet (BGH, Urt. v. 13.02.2020 – Az. IX ZR 140/19, Rn. 27–35). Eine vorhandene Taktklausel wird deshalb auf Verbraucher- oder Unternehmerverkehr, Formularcharakter und Reichweite geprüft, nicht wegen ihrer bisherigen Verwendung akzeptiert. Ob eine individuell ausgehandelte oder kürzere Taktung gegenüber Unternehmern Bestand hat, ist aus der Entscheidung nicht abzuleiten.

Unterscheide Zeitrundung und Geldrundung. Bei 280 Euro je Stunde ergeben siebzehn Minuten einen mathematischen Zeitwert von 79,333… Euro. Das Werkzeug rundet jeden einzelnen Eintragswert kaufmännisch auf Cent und summiert danach; bei vielen Positionen kann die Summe der gerundeten Einzelwerte um einzelne Cent vom Produkt aus Gesamtminuten und Satz abweichen. Die vereinbarte und tatsächlich verwendete Berechnungsweise wird konsistent angewendet und bei der Rechnung kontrolliert. Aus Centabweichungen werden keine zusätzlichen Minuten erzeugt.

Das Werkzeug akzeptiert nur ganze Minuten zwischen 0 und 1.440. Bei sekundengenauen Ursprungssystemen werden zusammengehörige Belege zunächst zusammengeführt und dann übertragen, ohne durch Aufrunden jeder Kleinigkeit Mehrzeit zu erzeugen; der ursprüngliche Nachweis bleibt erhalten und die Übertragungsmethode steht im Feld `source`.

### 3.5. Darlegungs- und Beweislast und Prüfbarkeit der Zeitaufstellung

Wer ein Zeithonorar verlangt, muss nach allgemeinen Grundsätzen darlegen und im Streitfall beweisen, welche Tätigkeit wann, von wem und mit welcher Dauer erbracht wurde und dass sie zur sachgerechten Bearbeitung des Auftrags gehörte. Die konkrete Nachprüfbarkeit des Zeitaufwands bleibt wesentlich (BGH, Urt. v. 12.09.2024 – Az. IX ZR 65/23, Rn. 20–35, 37 und 51). Eine Zeitaufstellung erfüllt diese Anforderung nur, wenn jede Position Datum, Person, Minuten und einen Leistungsinhalt enthält, aus dem ein sachkundiger Dritter Tätigkeit und Mandatsbezug erkennt; Zeilen wie „Recherche“ oder „Telefonat“ ohne Gegenstand genügen nicht. [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html) verlangt eine Berechnung in Textform, die der Anwalt mitteilt oder mitteilen lässt; bei vereinbartem Zeithonorar kommt die konkrete Leistungsdarstellung hinzu, weil sich der Betrag nur aus ihr ergibt.

Eine formularmäßige Klausel, nach der nicht binnen Monatsfrist beanstandete Zeitaufstellungen als anerkannt gelten, trägt diese Last nicht ab. Der BGH hält eine solche Anerkenntnisfiktion auch im unternehmerischen Verkehr für unwirksam (BGH, Urt. v. 19.02.2026 – Az. IX ZR 226/22, Rn. 29–32 und 34, insbesondere Rn. 31–32 zum Schweigen auf Zeitaufstellungen). Schweigen des Mandanten ist deshalb kein Beweis für Dauer oder Erforderlichkeit; die Kanzlei muss jede Position weiterhin belegen können. Regelmäßige Zwischenaufstellungen bleiben sinnvoll, weil sie Belege sichern und dem Mandanten eine laufende Kosteninformation geben, nicht weil sie Einwände abschneiden.

Die Prüfbarkeit ergibt sich aus dem Journal: Jeder Eintrag trägt seine Quelle, jede Korrektur bleibt mit Stornogrund in `zeiten.csv` lesbar. Eine Zeitaufstellung für den Empfänger wird aus diesem Stand erzeugt, nicht freihändig geschrieben; weichen beide voneinander ab, wird zuerst das Journal auf dem Korrekturweg berichtigt.

### 3.6. Mehrere Bearbeiter, Besprechungen und Doppelarbeit

Die Teilnahme mehrerer Personen kann vereinbart sein, ist aber kein Multiplikator des Honorars. Dokumentiere die konkrete Rolle: federführende Beratung, besondere Fachfrage, Protokollierung oder Einarbeitung. Prüfe, ob Doppelbesetzung vom Auftrag gedeckt, erforderlich und angekündigt war; eine Ausbildungssituation wird nicht ohne Grundlage berechnet und nicht in Qualitätssicherung umbenannt. Interne Abstimmung kann abrechenbar sein, wenn sie der sachgerechten Bearbeitung dient und nach der Vereinbarung erfasst ist. Bei einem Bearbeiterwechsel ist zu prüfen, ob zusätzliche Einarbeitung auf einer Kanzleientscheidung beruht und wer das Risiko trägt.

Das Werkzeug weist einen bestätigten Eintrag ab, wenn dieselbe Person am selben Tag innerhalb dieses Mandats mehr als 1.440 Minuten erreichen würde. Diese Unmöglichkeitskontrolle beweist weder Arbeitsfähigkeit noch die Abwesenheit mandatsübergreifender Doppelbuchungen. Überschneidungen, identische Besprechungen und doppelte Erfassung derselben Nachricht werden deshalb inhaltlich und gegebenenfalls über weitere zulässig zugängliche Erfassungen geprüft.

### 3.7. Reise, Wartezeit, Unterbrechung und Bereitschaft

Reisezeit und Wartezeit werden nach der tatsächlichen Vereinbarung behandelt. Ein Stundensatz für juristische Arbeit gilt nicht zwangsläufig für jede Fahrt. Prüfe, ob Reisezeit gesondert vergütet wird, ob während der Fahrt an einem anderen Mandat gearbeitet wurde und wie eine Doppelberechnung vermieden wird. Transportauslagen gehören in `expense`, nicht in `time`; eine Fahrtkostenrechnung beweist keine aktive Arbeitszeit.

Bei einer unterbrochenen Tätigkeit wird die Unterbrechung nicht mitgerechnet. Ein Rechner kann über Stunden ein Dokument geöffnet halten, während die Person eine andere Aufgabe bearbeitet; eine automatische Aktivitätserfassung ist nur ein Hinweis, der eine fachliche Bestätigung benötigt. Bereitschaftsvergütung setzt eine Grundlage voraus und wird nicht als aktive Recherche umetikettiert. Gerichtliche Wartezeiten werden mit Ankunft, Beginn, Ende und notwendiger Tätigkeit erfasst; dieselbe Belastung wird nicht als Zeithonorar und zusätzlich als Zuschlag angesetzt.

### 3.8. Rekonstruktion verspäteter Einträge

Ist eine zeitnahe Erfassung versäumt worden, sichere zunächst die objektiven Anhaltspunkte: Besprechungsprotokoll, Kalender, Nachrichten, Versionshistorie und persönliche Notizen. Rekonstruiere daraus den Arbeitsablauf, ohne Dateizeitstempel mit Arbeitsdauer gleichzusetzen. Die bearbeitende Person bestätigt, welche Dauer sie aus Erinnerung oder aus den benannten Belegen noch belastbar angeben kann. Kennzeichne den Eintrag im Feld `source` als nachträglich rekonstruiert und nenne Belege und Rekonstruktionszeitpunkt.

Branchenüblichkeit, ein früherer Vergleichsfall oder der Umfang des Enddokuments genügen nicht als Beweis tatsächlicher Dauer. Kann nur eine Bandbreite begründet werden, bleibt die Abrechnungsdauer offen, bis die verantwortliche Person eine vertretbare Behandlung festlegt; das System wählt nicht die obere Grenze. Bei einer bereits mitgeteilten Rechnung wird die Rekonstruktion nicht in den früheren Nachweis eingearbeitet, sondern in einem datierten Vermerk festgehalten; die Frage einer Rechnungsberichtigung geht an den Abrechnungsskill. Eine plausibilisierte Ergänzung wird nicht als zeitnah entstandener Originalbeleg bezeichnet.

### 3.9. KI-Nutzung, Verschwiegenheit und vertrauliche Leistungsbeschreibung

Beschreibe menschliche Arbeit so, dass die Verantwortung erkennbar bleibt: „Amtliche Quellen zum Formbedarf geprüft und Vertragsentwurf nach Abgleich der Ergebnisse überarbeitet.“ Eine Werkzeugbezeichnung kann intern ergänzt werden, sofern sie für Nachvollziehbarkeit oder Kostenfrage relevant ist. Der Rechnungsempfänger benötigt nicht automatisch Prompts, vertrauliche Eingaben oder Rechercheprotokolle. Ob die Mandantschaft über ein Werkzeug zu informieren ist oder dessen Einsatz erlaubt sein muss, klärt der Nachbarskill zum Berufsrecht; die Zeiterfassung behauptet keine Zustimmung und deklariert eine tatsächlich erfolgte Nutzung nicht um.

Die Verschwiegenheitspflicht aus [§ 43a Absatz 2 BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) und der Geheimnisschutz nach [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) gelten auch für Zeitaufstellungen. Geschützt sind nicht nur Akteninhalte, sondern auch die Tatsache einer Beratung, Geschäftsgeheimnisse und interne Vergleichslinien. Ein Narrativ darf deshalb gegenüber einem Rechtsschutzversicherer, einer Einkaufsabteilung, einem Kostenfestsetzungsorgan oder einem Prozessgegner keine vertrauliche Haftungsprüfung offenlegen. Für solche Empfänger wird ein abstrahiertes Narrativ erstellt, das Leistungsart und Zusammenhang erhält und dieselbe Dauer, Person und Datum nennt; das interne Protokoll bleibt zugriffsbeschränkt. Die Abstraktion verändert den Zeitbeleg nicht und täuscht keine andere Leistung vor. Dokumentiere, welche Fassung für welchen Empfänger vorgesehen ist, und gib sie nur bei Auftrag und geklärter Berechtigung weiter.

### 3.10. Parallelbearbeitung während einer Werkzeuglaufzeit

Startet eine Person einen Recherchelauf und arbeitet währenddessen an einem anderen Mandat, wird aktive menschliche Tätigkeit mandatsbezogen erfasst. Die drei Minuten zur Vorbereitung des Rechercheauftrags und die zwölf Minuten zur Prüfung des Ergebnisses gehören zum ersten Mandat; die zwanzig Minuten tatsächlicher Vertragsarbeit während der Laufzeit gehören zum zweiten. Die verstrichene halbe Stunde wird nicht zusätzlich als Recherchezeit des ersten Mandats gebucht. Abweichende ausdrücklich vereinbarte Vergütungsmodelle werden gesondert beurteilt, nicht durch unzutreffende Zeitangaben umgesetzt.

Kann die Person wegen einer notwendigen Liveüberwachung nichts anderes tun, wird die konkrete Überwachungsaufgabe dokumentiert und ihre vertragliche Berechenbarkeit geprüft; der offene Bildschirm genügt nicht. Download- und Konvertierungszeiten werden nicht zu anwaltlicher Bearbeitungszeit.

### 3.11. Das lokale Journal richtig benutzen

Die Schnittstelle steht in [Mandatsordner und CLI](../../references/mandatsordner-und-cli.md); das Werkzeug ist [`kanzlei.py`](../../scripts/kanzlei.py). Ein Zeiteintrag verwendet die Felder `id`, `terms_id`, `work_date`, `person`, `minutes`, `narrative`, `billable`, `confirmed` und `source`. Die ID besteht aus einem bis achtzig Zeichen aus Buchstaben, Ziffern, Punkt, Bindestrich und Unterstrich; `work_date` ist der Arbeitstag im Format `YYYY-MM-DD`. `terms_id=null` lässt eine Zeit unzugeordnet; eine unbekannte Phase wird mit „Unbekannte Honorargrundlage“ abgewiesen. `minutes=null`, `billable=null` oder `confirmed=false` halten Angaben offen; eine bestätigte Zeit benötigt Dauer und Abrechenbarkeit.

Bereite die Eingabe als UTF-8-JSON-Datei im Arbeitsordner vor und kontrolliere sie vor dem Aufruf `python3 "<Pluginordner>/scripts/kanzlei.py" time --akte "<Mandatsordner>" --data "<Eingabedatei.json>"`. `init` ist nur nötig, wenn der Ordner noch kein Journal unter `00_Mandat/mandatsjournal.sqlite` besitzt. Die Rückgabe ist ein JSON-Objekt mit `message`, `matter_id`, `journal_revision`, `complete`, `known_gross_eur`, `open_items` und `invoice_ready`; prüfe nach jedem Lauf Nachricht, Revision und offene Positionen. `status` liest denselben Stand ohne Schreibzugriff.

Eine identische Eingabe mit derselben ID erzeugt keine zweite Buchung („Unverändert; identische Buchung schon vorhanden“); dieselbe ID mit abweichendem Inhalt wird zurückgewiesen. Die Korrektur erfolgt mit `python3 "<Pluginordner>/scripts/kanzlei.py" void --akte "<Mandatsordner>" --id "<alte-ID>" --reason "<konkreter Grund>"` und einer neuen ID, deren `source` die ersetzte Buchung bezeichnet. Ein Storno mit identischem Grund ist wirkungslos; ein zweites Storno mit anderem Grund wird abgewiesen, damit die Historie eindeutig bleibt. Dies gilt auch, wenn eine zunächst unzugeordnete Zeit später einer Honorarphase zugewiesen wird.

### 3.12. Rechnungsentwurf, Deckel und Budgetabgleich fortschreiben

Nach erfolgreicher Erfassung wird der neue Stand gelesen. Der Entwurf enthält nur bestätigte, zugeordnete und abrechenbare Beträge; nicht abrechenbare Minuten erscheinen in `zeiten.csv`, aber nicht in den Phasenminuten. Bei `flat` werden Zeiten dokumentiert, aber nicht auf den Festpreis aufgeschlagen; der Hinweis „Festpreis ist Vereinbarungswert; Leistungsstand und Fälligkeit vor Rechnungsstellung prüfen“ bleibt stehen. Bei `rvg` entsteht aus Zeiten kein Gebührenbetrag.

Bei `capped` zeigt die Phase in `rechnungsentwurf.json` den vollen Zeitwert als `time_value_eur` und den begrenzten Ansatz als `fee_eur`; der Hinweis „Zeitwert oberhalb des Deckels nicht angesetzt“ nennt den nicht berechenbaren Betrag, und `cap_scope=fees_and_expenses` zieht Auslagen in den Deckel ein. Bei `estimate` meldet das Werkzeug „Schätzung überschritten; Kosteninformation und weiteren Auftrag klären“, ohne den Betrag zu kappen. Beide Hinweise sind Anlass für eine Kosteninformation über den Nachbarskill, nicht für eine Verkürzung der Zeiten und nicht für eine neue Phasen-ID, die den Gesamtdeckel umgeht.

Die Dateien `rechnungsentwurf.md`, `rechnungsentwurf.json` und `zeiten.csv` im Ordner `02_Honorar` werden aus dem führenden Journal erzeugt; `draft` erzeugt sie nach einer Unterbrechung erneut. Der CSV-Export (Spalten ID, Honorarphase, Datum, Person, Minuten, Narrativ, Abrechenbar, Bestätigt, Stornogrund) schützt Zellanfänge gegen Formeleinschleusung. Die Rechenhilfe unterstützt ausschließlich inländische Standardumsätze mit `vat_rate=19`; eine falsche Steuerangabe wird nicht gesetzt, um eine Zeit in einen Preisentwurf zu zwingen.

### 3.13. Mehrere Sätze innerhalb desselben Arbeitstags

Ändert sich ein Stundensatz wirksam ab einem bestimmten Zeitpunkt, werden alte und neue Leistungen getrennt zugeordnet. Ein am Vormittag erbrachter Arbeitsschritt wird nicht mit einem erst am Nachmittag vereinbarten höheren Satz bewertet, wenn keine rückwirkende Vereinbarung vorliegt. Eine geänderte Rate Card im Kanzleisystem ist keine Vertragsgrundlage für ein bestehendes Mandat. Das Werkzeug lässt eine bestätigte und bereits verwendete Phase nicht nachträglich umschreiben; es verlangt eine neue, klar abgegrenzte Phase.

Bei mehreren Bearbeitern mit unterschiedlichen Sätzen bleibt der Personenbezug erhalten; eine Zusammenfassung sämtlicher Stunden zum höchsten Satz ist ohne Vereinbarung unzulässig. Da eine Phase nur einen Satz kennt, wird für jeden Satz eine eigene Phase mit eigenem `scope` angelegt; es wird nicht mit falschen Personenangaben gearbeitet. Ein Gesamtdeckel, der mehrere Phasen umfasst, wird außerhalb des Werkzeugs gegengerechnet.

### 3.14. Beanstandungen sachlich bearbeiten

Widerspricht ein Mandant einem Eintrag, sichere zunächst Wortlaut und Zugang der Beanstandung. Vergleiche Originalnachweis, vertraglichen Umfang und das gelieferte Arbeitsergebnis. Trenne den Streit über die Dauer vom Streit über die Berechenbarkeit oder den Stundensatz. Ein zutreffender Zeitnachweis kann eine nicht beauftragte Tätigkeit betreffen; umgekehrt kann eine beauftragte Tätigkeit unzureichend nachgewiesen sein. Eine sachliche Erläuterung ist deshalb der erste Schritt.

Bei einer berechtigten Korrektur werden alter Eintrag, Stornogrund, neue Buchung und gegebenenfalls Rechnungsberichtigung verknüpft; bei einer unberechtigten Beanstandung erläutere Nachweis und Berechnungsgrundlage. Ein Entgegenkommen wird als Nachlass bezeichnet und nicht durch Änderung der Zeitbelege umgesetzt.

### 3.15. Abschließende Qualitätskontrolle

Kontrolliere, ob jedes bestätigte Feld auf einer tatsächlichen Angabe beruht, ob Person und Satz sowie Tätigkeit und erfasster Umfang zusammenpassen und ob Doppelbuchungen, Unterbrechungen, ungewöhnliche Dauern, identische Narrative oder ein erreichter Gesamtdeckel vorliegen. Die Gegenprobe fragt, ob eine außenstehende sachkundige Person aus dem Eintrag die konkrete Tätigkeit und ihren Bezug zum Mandat versteht, ohne dass anwaltliche Gedanken offengelegt werden. Bleibt nur „Recherche 480 Minuten“, ist eine Konkretisierung nötig; ein belegter ganztägiger Termin wird nicht wegen seiner Länge verworfen. Plausibilität und Beweis sind unterschiedliche Bewertungen und werden im Vermerk entsprechend bezeichnet.

### 3.16. Agentischer Lauf und Freigabestufe

Der Skill ist einer der drei führenden Skills der Phase `abrechnung` nach [Mandatslauf und Freigaben](../../references/mandatslauf-und-freigaben.md). Ein einzelner Zeiteintrag während der laufenden Sacharbeit verändert die Hauptphase nicht; der Skill liest den Lauf mit `status`, bucht und meldet. Erst wenn eine Zeitaufstellung als Rechnungsanlage bestellt ist, setzt er die Phase `abrechnung` mit Grund. Die Phase endet nicht mit seinem Produkt, sondern mit dem Rechnungsentwurf oder der freigegebenen Rechnung aus [abrechnung-e-rechnung](../abrechnung-e-rechnung/SKILL.md); sein eigenes Produkt ist der Zeitstand (bestätigte Minuten, offene Zeitfragen) mit der Zeitaufstellung in Empfängerfassung.

| Stufe | Ohne Rückfrage |
|---|---|
| 0 | Akte und Honorarstand lesen; Datensatz, Statusmeldung und Zeitaufstellung als Text; keine Datei |
| 1 | Eingabedatei, Prüf- oder Korrekturvermerk und Empfängerfassung unter `01_Bearbeitung`; kein Aufruf von `time` |
| 2 | Bestätigte Zeiten mit `time` buchen, `void` mit Grund, Ansichten mit `draft`, Produktregister und Mandatslauf fortschreiben |
| 3 | Übergabevermerk erstellen; abrechnung-e-rechnung oder honorar-budget-vereinbaren anstoßen |

Auf keiner Stufe bestätigt der Skill einen Eintrag ohne menschliche Meldung, schätzt er Minuten, gibt er eine Rechnung aus oder leitet er eine Zeitaufstellung an einen Empfänger außerhalb der Kanzlei weiter. Ein eigenes Gate öffnet er nicht. Er liefert den Zeitstand für G4 Rechnungsausgabe, das abrechnung-e-rechnung öffnet und ein Berufsträger namentlich freigibt; nach der Freigabe trägt er Rechnungsnummer und mitgeteilte Positionen zu den betroffenen Einträgen nach, damit spätere Korrekturen als Rechnungsberichtigung erkannt werden. Soll eine Zeitaufstellung einen externen Dienst erreichen, etwa ein Abrechnungsportal eines Rechtsschutzversicherers, bleibt er vor G6 Dienstleister stehen, das [workflow-uebergabe](../workflow-uebergabe/SKILL.md) führt.

Im Produktregister trägt er die Empfängerfassung unter der Kennung `zeitstand` im Zustand `entwurf` ein; `geprueft` wird sie erst, wenn die verantwortliche Person Narrative und Minuten der Empfängerfassung bestätigt hat. Ab Stufe 3 stößt er danach ohne Rückfrage abrechnung-e-rechnung an, wenn eine Rechnung bestellt ist, oder honorar-budget-vereinbaren, wenn das Werkzeug einen Deckel- oder Schätzungshinweis ausgegeben hat; der Helfer ist [`mandatslauf.py`](../../scripts/mandatslauf.py):

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/SI-2026-014" --phase abrechnung --grund "Zeitaufstellung als Rechnungsanlage bestellt"
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/SI-2026-014" --id zeitstand --pfad "01_Bearbeitung/Zeitaufstellung_Anlage1_v01.md" --skill zeiten-erfassen --zustand entwurf
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/SI-2026-014"
```

Der Skill bleibt stehen, wenn Dauer, Person, Arbeitstag oder Abrechenbarkeit einer Position unbestätigt sind oder wenn eine Position bereits in einer mitgeteilten Rechnung steht und die Kanzlei über die Rechnungsberichtigung noch nicht entschieden hat; er bucht dann nicht weiter, sondern trägt die Frage mit `question --akte "<Mandatsordner>" --text "<Frage>"` in den Lauf ein.

### 3.17. Typische Fehler und Gegenkontrolle

| Fehler | Woran erkennbar | Gegenkontrolle |
|---|---|---|
| KI-Ersparnis als Minuten gebucht | Dauer entspricht manuellem Vergleichswert, nicht der Meldung | Quelle verlangen; nur gemeldete tatsächliche Minuten übernehmen |
| Erfassungstag statt Arbeitstag | `work_date` gleich Buchungsdatum trotz älterem Beleg | Datum gegen Protokoll, Versionen und Nachrichten prüfen |
| Viertelstundentakt je Vorgang | Alle Minuten durch 15 teilbar, viele 15er-Positionen | Gegen Takt- und Verbraucherfrage prüfen; tatsächliche Minuten erfragen |
| Sammelblock ohne Aufschlüsselung | Ein Narrativ mit drei und mehr Tätigkeiten | Aufteilen nach Belegen; sonst Gesamtdauer mit offener Aufschlüsselung vermerken |
| Narrativ ohne Gegenstand | „Bearbeitung“, „Telefonat“, „Recherche“ | Tätigkeit, Gegenstand, Bezug ergänzen; Vorschlag bestätigen lassen |
| Vertrauliche Strategie im Narrativ | Haftungsprüfung, Vergleichslinie oder Dritter namentlich genannt | Empfängerfassung abstrahieren; interne Fassung zugriffsbeschränkt halten |
| Doppelbuchung mit Wortwechsel | Gleicher Tag, gleiche Person, ähnliche Dauer, zwei Narrative | Kalender und Meldung vergleichen; Storno mit Grund |
| Stille Änderung über neue Eingabe | Fehlermeldung „ID bereits verwendet“ oder Ansicht manuell editiert | `void` mit Grund, neue ID, Verweis in `source` |
| Werkzeuglaufzeit als Personenzeit | Minuten gleich Laufzeitprotokoll des Modells | Nur aktive menschliche Schritte erfassen; Parallelarbeit anderem Mandat zuordnen |
| Deckel durch neue Phase umgangen | Zweite Phase für denselben Umfang nach Deckelhinweis | Umfang vergleichen; Kosteninformation statt Phasensplit |
| Festpreis nachkalkuliert und nachgefordert | Stundenwert als Zusatzposition beim Modell `flat` | Festpreis bleibt Rechnungswert; Mehraufwand nur bei belegtem Zusatzauftrag |
| Schweigen als Anerkenntnis gewertet | Hinweis auf Monatsfrist statt Beleg | Position inhaltlich belegen; Fiktion nicht verwenden |

### 3.18. Übergabe an Nachbarskills

An [honorar-budget-vereinbaren](../honorar-budget-vereinbaren/SKILL.md) geht die Feststellung, dass eine Tätigkeit nicht vom gespeicherten Anwendungsbereich erfasst ist, dass ein Deckel oder eine Schätzung erreicht wird oder dass Effizienz prospektiv anders bepreist werden soll, zusammen mit dem Honorarstand (Modell, Satz/Betrag, Umfang, Deckel, netto/brutto), dem Zeitwert aus `rechnungsentwurf.json` und dem betreffenden Eintrag. Zurück kommt eine bestätigte neue oder ergänzte Phase, der die offene Zeit auf dem Korrekturweg zugeordnet wird.

An [abrechnung-e-rechnung](../abrechnung-e-rechnung/SKILL.md) gehen der Zeitstand (bestätigte Minuten, offene Zeitfragen) mit Journalrevision, die Zeitaufstellung in Empfängerfassung als führende Fassung mit Pfad und Hash, der Honorarstand, die offenen Gates und die offenen Fragen; zurück kommt, welche Positionen in welcher Rechnung mitgeteilt wurden, damit spätere Korrekturen als Rechnungsberichtigung erkannt werden. An [mandantenkommunikation](../mandantenkommunikation/SKILL.md) geht der Prüfvermerk zu einer Beanstandung mit Nachweislage; zurück kommt der versandfertige Brief, der hier auf Übereinstimmung mit dem Journal geprüft wird. An [anwaltsberufsrecht-pruefen](../anwaltsberufsrecht-pruefen/SKILL.md) geht die Frage, ob ein Narrativ oder ein Export an Dritte die Verschwiegenheit berührt; zurück kommt die fachliche Bewertung oder eine abstrahierte Fassung; eine Gatefreigabe bleibt menschlich. An [mandat-abschliessen](../mandat-abschliessen/SKILL.md) geht der vollständige Zeitstand, damit vor der Schlussrechnung nichts unbestätigt bleibt. Fristobjekte entstehen hier nicht; ein Zeiteintrag zu einer Fristsache nennt das Fristobjekt nur im Narrativ. In jeder Übergabe werden Honorarstand und Zeitstand kurz vorgehalten, und die im übernehmenden Skill anfallende Zeit wird nach denselben Regeln erfasst.

## 4. Quellenpflicht

### 4.1. Normen und Prüfstand

Nutze [Zitierweise](../../references/zitierweise.md) und [Rechtsquellen](../../references/rechtsquellen.md). Prüfstand ist der 08.10.2026. Tragend sind die konkrete Honorarvereinbarung und folgende amtliche Normtexte: [§ 3a RVG](https://www.gesetze-im-internet.de/rvg/__3a.html) für Textform, deutliche Bezeichnung und Absetzung der Vergütungsvereinbarung, [§ 4b RVG](https://www.gesetze-im-internet.de/rvg/__4b.html) für die Folgen einer formfehlerhaften Vereinbarung, [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html) für die Berechnung in Textform, [§§ 305 bis 310 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) für die Kontrolle formularmäßiger Takt-, Anerkenntnis- und Abrechnungsklauseln, [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) für die Verschwiegenheit und [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) für den Geheimnisschutz. § 4b Satz 1 RVG begrenzt den Anspruch bei den dort bezeichneten Verstößen gegen § 3a Absatz 1 Satz 1 und 2 sowie § 4a Absatz 1 und Absatz 3 Nummer 1 und 4 auf die gesetzliche Vergütung; Satz 2 lässt Bereicherungsrecht unberührt.

### 4.2. Verifizierte Entscheidungsanker

BGH, Urt. v. 19.02.2026 – Az. IX ZR 226/22, Rn. 8–18, 23–32 und 34. Trägt: Inhalt und Anwendungsbereich der Vergütungsvereinbarung sind zuerst auszulegen, dann ist die Textform zu prüfen; eine formularmäßige Anerkenntnisfiktion für nicht binnen eines Monats beanstandete Zeitaufstellungen ist auch im Unternehmerverkehr unwirksam (Rn. 31–32). Trägt nicht: eine pauschale Gewähr für andere Klauseln oder individuell ausgehandelte Einwendungsregeln; der Fortbestand der übrigen Abrede im entschiedenen Fall ist in Rn. 32 ausdrücklich begründet. [Amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1).

BGH, Urt. v. 19.02.2026 – Az. IX ZR 227/22, Rn. 8–13. Trägt: Die Zeitzuordnung setzt eine festgestellte Honorarreichweite voraus; eine verwandte neue Aufgabe oder ein gemeinsamer Aktenname erfasst sie nicht automatisch. Trägt nicht: eine Regel über die Höhe oder Angemessenheit einzelner Zeitpositionen. [Amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_227-22.pdf?__blob=publicationFile&v=1).

BGH, Urt. v. 12.09.2024 – Az. IX ZR 65/23, Rn. 16, 20–35, 37 und 51. Trägt: Eine formularmäßige Zeithonorarabrede ist nicht allein wegen fehlender Schätzung oder fehlender Pflicht zu Zwischenaufstellungen unwirksam; die konkrete Nachprüfbarkeit des Zeitaufwands bleibt wesentlich. Trägt nicht: die Ersetzung der Tatsachenprüfung jedes einzelnen Eintrags oder eine Freigabe unbestimmter Abrechnung. [Amtlicher Volltext im Curia-Archiv](https://curia.europa.eu/site/upload/docs/application/pdf/2025-04/ix_zr__65-23_2025-04-16_15-06-53_148.pdf).

BGH, Urt. v. 13.02.2020 – Az. IX ZR 140/19, Rn. 27–35. Trägt: Die formularmäßige Abrechnung jedes angefangenen Viertelstundenintervalls benachteiligt jedenfalls Verbraucher unangemessen. Trägt nicht: ein Verbot jedes Zeithonorars oder eine Freigabe anderer Taktklauseln gegenüber Unternehmern. [Amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2019/IX_ZR_140-19.pdf?__blob=publicationFile&v=1).

EuGH, Urt. v. 12.01.2023 – Az. C-395/21, EU:C:2023:14, Rn. 35–45 und 47–50. Trägt: Die bloße Angabe eines Stundensatzes genügt gegenüber Verbrauchern ohne weitere Erläuterung nicht dem Transparenzmaßstab; eine Schätzung oder regelmäßige Aufstellungen können die nötige wirtschaftliche Orientierung ermöglichen; der Skill kombiniert beides als Arbeitsstandard. Trägt nicht: eine gesetzliche Mindest- oder Höchstdauer je Tätigkeit oder ein allgemeines Verbot anwaltlicher Stundenhonorare. [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0395).

### 4.3. Belegdisziplin

Prüfstand ist der 08.10.2026. Die amtlichen Volltexte wurden für diese Fassung geöffnet und die einschlägigen Absätze beziehungsweise Randnummern gelesen; das Quellenprotokoll nennt Abrufdatum und gelesene Fundstellen. Bei der Mandatsbearbeitung wird der zum Sachverhalt passende Rechtsstand einschließlich Übergangsrecht erneut bestimmt. Eine ungeklärte Quelle bleibt eine interne Rechercheaufgabe und wird nicht als gesicherte Aussage in den Empfängertext übernommen. Jede Entscheidung nennt Gericht, Entscheidungsform, Datum, Aktenzeichen, amtliche Quelle und gelesene Randnummer. Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht als Nachweise verwendet. Jeder Anker behält seine positive Aussage und seine Übertragungsgrenze; eine Präjudizienbindung wird nicht behauptet.

## 5. Ausgabeformat

### 5.1. Zeitnachweis und kurze Statusmeldung

Das Ergebnis besteht aus dem Zeitbeleg, einem verständlichen Narrativ, dem Bestätigungsstand und der konkreten Wirkung auf den Rechnungsentwurf. Wenn gespeichert wurde, nenne Mandatsordner, Eintrags-ID und Journalrevision aus der Werkzeugrückgabe; wenn nur eine Eingabe vorbereitet wurde, benenne diesen Stand. Der Nutzer erhält die noch fehlende gezielte Angabe. Keine Behauptung einer nicht erfolgten Buchung oder externen Mitteilung.

Das Endprodukt – Zeitaufstellung, Korrekturvermerk, Prüfvermerk, Antwort auf eine Beanstandung – wird in vollständigen, ausformulierten Sätzen geliefert. Eine Tabelle darf Daten ordnen, ersetzt aber nicht die Erläuterung. Skelette, Halbsätze und reine Aufzählungsgerüste sind als juristisches Endprodukt verboten. Formatierte Dokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chattext steht der Formatwunsch in einem getrennten Exporthinweis außerhalb des Empfängertextes; ein Markdownentwurf wird nicht als formatiertes PDF oder DOCX ausgegeben.

### 5.2. Datensatz und Empfängertext getrennt halten

Der maschinenlesbare Datensatz darf technische Feldnamen enthalten. Die Zeitaufstellung für den Mandanten verwendet verständliche Bezeichnungen: Datum, Bearbeiterin oder Bearbeiter, Tätigkeit, Minuten, Zeitwert. Ein interner Quellenvermerk wie „bestätigt durch Nachricht vom 7. Oktober 2026“ wird als Nachweis vorgehalten, gehört aber nicht in jede Rechnung. Vertrauliche Detailprotokolle bleiben intern.

### 5.3. Abnahmekriterien

Zur Abnahme enthält jeder bestätigte Eintrag Person, Arbeitstag, ganze Minuten, Narrativ mit Tätigkeit und Gegenstand, Abrechenbarkeit und Quelle. Dauer, Verteilung eines Sammelblocks und Personenzeit dürfen nicht erfunden werden; Werkzeuglaufzeit wird getrennt behandelt. Korrekturen bestehen aus begründetem Storno und verknüpfter Ersatzbuchung, Ansichten bleiben unverändert. Die gelesene Werkzeugrückgabe liefert Revision und offene Positionen für die Statusmeldung. Die Empfängerfassung schützt vertrauliche Inhalte und stimmt bei Minuten, Personen und Tagen mit dem Journal überein. Deckel-, Schätzungs- und Festpreishinweise führen zu einer Handlungsempfehlung an den Nachbarskill, nicht zu Phasensplit oder Zeitkürzung. Offene Fragen werden wörtlich und zusammen mit dem bereits bearbeiteten Umfang benannt. Die führende Fassung wird mit Pfad und Hash im Mandatslauf eingetragen. Ohne Dateizugriff nennt der Übergabevermerk nur den vorgesehenen Pfad und weist den Hash als nicht ermittelbar aus. Offene Gates bleiben offen, bis die namentliche menschliche Freigabe der geprüften Fassung dokumentiert ist.

## 6. Beispiele

### 6.1. Vollständiger bestätigter Eintrag

Rechtsanwältin Dr. Lena Ahrens meldet am Mittwoch, dem 7. Oktober 2026: „Für die Prüfung der Haftungsklauseln habe ich heute 47 Minuten benötigt. Die Zeit ist nach HV-1 abrechenbar.“ Der Datensatz lautet:

```json
{
  "id": "Z-20261007-01",
  "terms_id": "HV-1",
  "work_date": "2026-10-07",
  "person": "RAin Dr. Lena Ahrens",
  "minutes": 47,
  "narrative": "Haftungsregelungen in Ziffer 12 des Liefervertrags geprüft und Ersatzklauseln für die erste Änderungsfassung ausgearbeitet.",
  "billable": true,
  "confirmed": true,
  "source": "Tätigkeitsmeldung der Bearbeiterin vom 07.10.2026 am Arbeitstag; Vertragsfassung vom 06.10.2026."
}
```

Bei 280 Euro netto je Stunde beträgt der Zeitwert nach Centrundung 219,33 Euro netto. Die Statusmeldung nach erfolgreichem Lauf lautet: „Die bestätigten 47 Minuten sind unter Z-20261007-01 der Honorarphase HV-1 zugeordnet; Journalrevision 14, keine offenen Positionen. Der Zeitwert von 219,33 Euro netto liegt innerhalb des Deckels von 2.500 Euro netto.“ Die Aussage über eine erfolgte Speicherung wird erst nach dem Werkzeuglauf verwendet.

### 6.2. Fehlende Dauer bei fertigem Dokument

Die Nutzerin verlangt nach Fertigstellung einer Klageerwiderung am Donnerstag, dem 8. Oktober 2026: „Bitte die Zeit gleich buchen.“ Eine Dauer ist nicht bekannt. Die Antwort lautet: „Die Klageerwiderung ist fertig. Für die Zeit gilt die bestätigte Honorarvereinbarung HV-2 mit 250 Euro netto je Stunde. Wie viele tatsächliche Minuten haben Sie heute für Prüfung und Überarbeitung aufgewendet, und soll der Eintrag als abrechenbar bestätigt werden? Als Narrativ ist vorgesehen: Prüfung des gegnerischen Vortrags zur Mängelrüge und Überarbeitung der Klageerwiderung.“

Bis zur Antwort wird ein Eintrag Z-20261008-01 mit `minutes=null`, `billable=null` und `confirmed=false` vorbereitet; das Werkzeug führt ihn als offene Position. Das System ergänzt nicht neunzig Minuten, weil der Schriftsatz lang ist. Nach der Antwort „72 Minuten, abrechenbar“ wird der bestätigte Stand unter Z-20261008-02 erfasst und der vorbereitete Eintrag Z-20261008-01 mit dem Grund „Dauer und Abrechenbarkeit nach Meldung vom 08.10.2026 bestätigt; ersetzt durch Z-20261008-02“ storniert.

### 6.3. Ausformulierte Zeitaufstellung als Rechnungsanlage

Für die Mandantin Nordlicht Maschinenbau GmbH (fiktiv) gilt HV-1 mit 280 Euro netto je Stunde und einem Deckel von 2.500 Euro netto für Gebühren. Aus dem Zeitstand des Journals wird die Anlage in Empfängerfassung erzeugt:

> Zeitaufstellung zur Rechnung [Rechnungsnummer] – Anlage 1
>
> Mandat: Liefervertrag mit der Hansa Komponenten AG, Prüfung und Änderungsfassung. Honorargrundlage: Vergütungsvereinbarung vom 28. September 2026, 280 Euro netto je Stunde, Höchstbetrag 2.500 Euro netto für Gebühren. Abgerechnet werden tatsächliche Minuten ohne Aufrundung.
>
> Am Freitag, dem 2. Oktober 2026, sichtete Rechtsanwältin Dr. Lena Ahrens den Entwurf des Liefervertrags und die von Ihnen übermittelten Lieferbedingungen und legte die Prüfreihenfolge fest; 20 Minuten, Zeitwert 93,33 Euro.
>
> Am Montag, dem 5. Oktober 2026, prüfte Rechtsanwältin Dr. Lena Ahrens die Gewährleistungsregelungen in den Ziffern 8 bis 11, verglich sie mit den von Ihnen übermittelten Lieferbedingungen und formulierte die Ersatzregelungen der Änderungsfassung; 95 Minuten, Zeitwert 443,33 Euro.
>
> Am Dienstag, dem 6. Oktober 2026, besprach Rechtsanwalt Jonas Brecht mit Ihrer Einkaufsleitung telefonisch die Reihenfolge der Verhandlungspunkte zu den Lieferbedingungen; 30 Minuten, Zeitwert 140,00 Euro.
>
> Am Mittwoch, dem 7. Oktober 2026, prüfte Rechtsanwältin Dr. Lena Ahrens die Haftungsregelungen in Ziffer 12 der Vertragsfassung vom 6. Oktober 2026 und arbeitete Ersatzklauseln für die erste Änderungsfassung aus; 47 Minuten, Zeitwert 219,33 Euro.
>
> Gesamt: 192 Minuten, Summe der centgerundeten Einzelwerte 895,99 Euro netto. Der Höchstbetrag von 2.500 Euro netto ist nicht erreicht. Umsatzsteuer und Auslagen weist die Rechnung gesondert aus.

Die interne Fassung nennt zusätzlich Quelle und Journal-ID jeder Position. Der getrennte Exporthinweis lautet: Times New Roman, 11 pt, dezimale Gliederung, Anlage ohne technische Feldnamen.

Auf Freigabestufe 3 setzt der Skill die Phase `abrechnung` mit dem Grund „Zeitaufstellung als Rechnungsanlage bestellt“, trägt die Empfängerfassung als Produkt `zeitstand` im Zustand `entwurf` ein und übergibt den Zeitstand (192 bestätigte Minuten, keine offenen Zeitfragen) mit Pfad und Hash an abrechnung-e-rechnung, das den Rechnungsentwurf erstellt und G4 Rechnungsausgabe öffnet. Dort bleibt der Lauf stehen, bis Rechtsanwältin Dr. Ahrens die Rechnung namentlich freigibt; die endgültige Nummer wird vor der Prüfung in Rechnung und Anlage eingesetzt. G4 bindet ihre unveränderte Fassung; nachträgliche Änderungen erfordern eine neue Freigabe.

### 6.4. Ausformulierter Korrekturvermerk nach Doppelbuchung

Eine Besprechung vom Dienstag, dem 6. Oktober 2026, wurde einmal als „Mandantentelefonat“ (Z-20261006-02) und einmal als „Abstimmung zum Vergleich“ (Z-20261006-03) mit jeweils dreißig Minuten erfasst. Kalender und Bearbeitermeldung bestätigen nur ein Gespräch. Der interne Vermerk lautet:

> Korrekturvermerk zu den Zeiteinträgen Z-20261006-02 und Z-20261006-03, Mandat SI-2026-014, erstellt am Donnerstag, dem 8. Oktober 2026, von Rechtsanwalt Jonas Brecht.
>
> Beide Einträge betreffen nach dem Kalendereintrag von 14.00 bis 14.30 Uhr und der Tätigkeitsmeldung vom selben Tag dasselbe Telefonat mit der Einkaufsleitung der Mandantin über die Reihenfolge der Verhandlungspunkte zu den Lieferbedingungen. Ein zweites Gespräch hat an diesem Tag nicht stattgefunden. Die tatsächliche Dauer beträgt dreißig Minuten.
>
> Der Eintrag Z-20261006-03 wird deshalb mit dem Befehl `python3 "<Pluginordner>/scripts/kanzlei.py" void --akte "/Mandate/SI-2026-014" --id "Z-20261006-03" --reason "Doppelbuchung desselben Telefonats vom 06.10.2026; Leistung ist in Z-20261006-02 erfasst"` storniert. Der Eintrag Z-20261006-02 bleibt bestehen; da sein Narrativ „Mandantentelefonat“ den Gegenstand nicht benennt, wird auch er mit dem Grund „Narrativ konkretisiert; ersetzt durch Z-20261006-04“ storniert und unter Z-20261006-04 mit dem Narrativ „Telefonat mit der Einkaufsleitung der Mandantin zur Reihenfolge der Verhandlungspunkte zu den Lieferbedingungen“ und unveränderten dreißig Minuten neu angelegt. Das Feld `source` der neuen Buchung verweist auf beide stornierten Einträge.
>
> Der Rechnungsentwurf wird aus dem neuen Journalstand regeneriert. Eine Rechnung über diese Position ist noch nicht mitgeteilt worden; eine Rechnungsberichtigung ist daher nicht erforderlich. Die stornierten Einträge bleiben in `zeiten.csv` mit ihrem Stornogrund lesbar.

Ein wirtschaftlicher Nachlass wäre kein Stornogrund „Doppelbuchung“, wenn tatsächlich zwei Leistungen erbracht wurden.

### 6.5. Negativbeispiel: KI-Ersparnis als Stunden gebucht

Ein Bearbeiter meldet am Freitag, dem 9. Oktober 2026: „Die AGB-Prüfung hätte manuell vier Stunden gedauert; mit dem Werkzeug habe ich 70 Minuten gebraucht. Bitte 240 Minuten buchen, der Mandant zahlt für das Ergebnis.“ Die falsche Ausgabe wäre ein Eintrag mit `"minutes": 240`, dem Narrativ „AGB-Prüfung (manuelles Äquivalent)“ und der Quelle „Schätzung des manuellen Aufwands“. Sie ist falsch, weil ein Zeithonorar die tatsächlich aufgewendete Zeit vergütet und die Rechnung eine unwahre Tatsache behaupten würde. Die Kanzlei könnte die 240 Minuten im Streitfall nicht darlegen und beweisen, weil es sie nicht gab; der Klammerzusatz verschleiert das zusätzlich, weil ein Rechnungsprüfer ihn nicht als Hinweis auf eine fiktive Dauer versteht.

Die korrigierte Fassung lautet: Eintrag mit `"minutes": 70`, dem Narrativ „Prüfung der Allgemeinen Geschäftsbedingungen der Gegenseite auf Klauselverbote und Abweichungen vom Angebot der Mandantin; Prüfvermerk erstellt“, `"billable": true`, `"confirmed": true` und der Quelle „Tätigkeitsmeldung vom 09.10.2026; werkzeuggestützte Erstdurchsicht, Ergebnis von der bearbeitenden Person kontrolliert“. Die Meldung an den Bearbeiter lautet: „Gebucht sind die gemeldeten 70 Minuten. Die Zeitersparnis gegenüber einer manuellen Bearbeitung ist keine geleistete Zeit. Wenn die Kanzlei den Wert der schnelleren Bearbeitung abbilden will, ist prospektiv ein Festpreis oder eine andere Vergütungsform mit der Mandantin zu vereinbaren; das übernimmt der Skill honorar-budget-vereinbaren.“

### 6.6. Festpreis und hoher tatsächlicher Aufwand

Für die erste Vertragsfassung sind 1.800 Euro netto fest vereinbart (`flat`). Wegen unerwarteter interner Rückfragen fallen zwölf tatsächliche Stunden an. Der Zeitnachweis nennt diese Stunden wahrheitsgemäß mit den Tätigkeiten; der Rechnungsentwurf bleibt beim Festpreis, soweit kein beauftragter Zusatzumfang vorliegt. Die Kanzlei nutzt den Aufwand für die Nachkalkulation künftiger Festpreise und wandelt die Pauschale nicht in eine Stundenforderung um.

Die Statusmeldung lautet: „Für die erste Vertragsfassung sind 720 Minuten dokumentiert; der bestätigte Festpreis von 1.800 Euro netto bleibt die Abrechnungsgrundlage. Die am Montag, dem 12. Oktober 2026, gewünschte zweite Vertragsart ist nicht erfasst; hierfür bereitet der Skill honorar-budget-vereinbaren einen gesonderten Leistungs- und Kostenvorschlag vor.“
