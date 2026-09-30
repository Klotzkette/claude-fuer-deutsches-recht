# 1. Insolvenzgründe aus Liquiditätsdaten prüfen

Rechercheabgleich: 28.09.2026. Die [Entscheidungskarte mit amtlichen Volltexten](rechtsprechung/INDEX.md) enthält die Fundstellen und ihre Reichweite. Die Regeln gelten für die insolvenzrechtliche Bewertung in diesem Plugin; eine operative Wochenplanung bleibt ein eigenständiges Arbeitsprodukt. Bei historischen Stichtagen die damals geltende Gesetzesfassung verwenden.

## 1.1. Prüfziel und Datenqualität

Unterscheide vier Fragen: Welcher Zahlungsbedarf entsteht wann? Liegt Zahlungsunfähigkeit nach § 17 InsO vor? Droht Zahlungsunfähigkeit nach § 18 InsO? Liegt Überschuldung nach § 19 InsO vor? Ein gemeinsames Datenmodell darf diese Ergebnisse nicht gleichsetzen. Ein grüner Plan oder ein positiver Wochenendbestand ersetzt keine dieser rechtlichen Prüfungen.

Übernimm Stichtag, Gesellschaft, Rolle und Auftrag aus den Unterlagen. Bewahre je Zahl Originaldatei, Seite oder Tabellenzelle, Betrag, Währung, Vorzeichen, Fälligkeit, tatsächlichen oder erwarteten Zahlungstag und Verfügbarkeit. Bei OCR insbesondere Dezimalzeichen, abgeschnittene Zeilen, Salden und Dubletten gegenprüfen. Unsichere Lesungen nicht als bestätigte Beträge verwenden. Fehlende Daten sind unbekannt, nicht null; ein ungünstiges Szenario ist keine festgestellte Tatsache. Frage gezielt nach den Angaben, die Rechnung oder Ergebnis ändern, und verarbeite Antworten im bestehenden Stand.

## 1.2. Zahlungsunfähigkeit nach § 17 InsO

### 1.2.1. Stichtag und drei Wochen

Bestimme den tatsächlichen Prüfungstag. Beginne nicht automatisch am Montag und ende nicht automatisch am Freitag einer Kalenderwoche. Ermittle den vollständigen, taggenau abgegrenzten Dreiwochenzeitraum. Wochenbündel dürfen die Darstellung vereinfachen, aber keine Fälligkeiten, Wochenenden oder Randtage auslassen. Eine Freitagszahlung steht am vorausgehenden Dienstag noch nicht zur Verfügung.

Im reinen Stichtagsstatus stehen sofort verfügbare Mittel den am Stichtag fälligen und eingeforderten Verpflichtungen gegenüber. Bei der zeitraumbezogenen Liquiditätsbilanz getrennt erfassen:

| Position | Ansatz |
| --- | --- |
| Aktiva I | Am Stichtag frei verfügbare Zahlungsmittel einschließlich noch ungenutzter, tatsächlich abrufbarer Kreditmittel. |
| Aktiva II | Innerhalb des abgegrenzten Dreiwochenzeitraums belastbar zu erwartende, rechtzeitig verfügbare Zuflüsse. |
| Passiva I | Am Stichtag fällige und eingeforderte Verpflichtungen nach rechtlicher Prüfung. |
| Passiva II | Innerhalb desselben Zeitraums neu fällig werdende und eingeforderte Verpflichtungen. |

Für diese Bilanzmethode gilt: `Lücke = max(0, (Passiva I + Passiva II) − (Aktiva I + Aktiva II))`; `Lückenquote = Lücke / (Passiva I + Passiva II)`. Bei Nenner null keine Prozentquote berechnen; Bedeutung und Vollständigkeit der Daten erläutern. Die Zahlung einer bereits in Passiva I erfassten Altschuld ist kein neuer Passiva-II-Posten. Die Einbeziehung von Passiva II verhindert die Verschleierung fortlaufend erneuerter Rückstände; BGH, Urteil vom 19.12.2017 – II ZR 88/16, Rn. 50–62. Ein rechnerischer Endwert allein beantwortet nicht den Verlauf und den Eintrittszeitpunkt.

Eigene Forderungen, Verkaufserlöse oder Konzernmittel sind nicht bereits wegen Nominalwert, Buchwert, Fälligkeit, Kündbarkeit oder eines Titels liquide. Zeitpunkt, Einbringlichkeit, Zugriff und gegebenenfalls Zahlungsfähigkeit des Geldgebers belegen; BGH II ZR 88/16, Rn. 68–70. Einen Kontokorrentrahmen nicht zugleich als Anfangsguthaben und weiteren Zufluss zählen. Für unsichere Kundenzahlungen konkrete Zahlungs-/Ausfallszenarien bilden; ein mit 80 Prozent gewichteter Betrag ist nicht ohne Weiteres eine an einem bestimmten Tag verfügbare Zahlung.

### 1.2.2. Zehnprozentregel mit ihren Ausnahmen

BGH, Urteil vom 24.05.2005 – IX ZR 123/04, Leitsätze b und c, unterscheidet: Bei einer innerhalb von drei Wochen nicht beseitigbaren Lücke unter zehn Prozent ist regelmäßig Zahlungsfähigkeit anzunehmen, sofern nicht bereits absehbar ist, dass die Lücke demnächst zehn Prozent oder mehr erreichen wird. Ab zehn Prozent liegt regelmäßig Zahlungsunfähigkeit vor. Die Ausnahme verlangt die mit an Sicherheit grenzender Wahrscheinlichkeit zu erwartende baldige vollständige oder nahezu vollständige Schließung und die Zumutbarkeit des Zuwartens für die Gläubiger nach den besonderen Umständen.

Eine Lücke unter zehn Prozent bedeutet daher weder automatisch Zahlungsstockung noch eine dauerhafte Entwarnung. Ab zehn Prozent genügt eine bloß mögliche Finanzierung nicht zur Entlastung. Die Dreiwochenbetrachtung ist keine Wartefrist für eine bereits eingetretene Zahlungsunfähigkeit. Die rechtliche Bewertung schriftlich begründen; Rechenindikator, Datenqualität und Ergebnis getrennt ausweisen.

### 1.2.3. Andere Darlegungswege und Zahlungseinstellung

Eine Liquiditätsbilanz ist nicht der einzige zulässige Nachweisweg. BGH, Urteil vom 28.06.2022 – II ZR 112/21, Rn. 12–16, nennt den Stichtagsstatus mit tagesgenauem Finanzplan sowie mehrere tagesgenaue Status in aussagekräftiger Anzahl, die eine erhebliche, nicht relevant geschlossene Unterdeckung im Prognosezeitraum zeigen. Vier Stichproben oder ein bestimmter Abstand sind keine allgemeine Mindestregel. Die Methode darf erkennbare Zwischenereignisse nicht ausblenden. Die Anerkennung anderer Darlegungswege schafft die Einbeziehung von Passiva II bei Anwendung der Bilanzmethode nicht ab.

Die Zahlungseinstellung nach § 17 Abs. 2 Satz 2 InsO ist gesondert zu prüfen. Ein einziges starkes Indiz kann genügen; mehrere schwache Hinweise ersetzen keine Gesamtwürdigung. Erhebliche Rückstände, Erklärungen mangelnder Zahlungsfähigkeit, Rücklastschriften und Vollstreckungsdruck mit Betrag, Dauer, Ursache und Gegenindizien erfassen. Keine Regel „zwei Indizien = zahlungsunfähig“ verwenden. BGH, Urteil vom 28.04.2022 – IX ZR 48/21, Rn. 27–33: Gleichbleibend um einen bis weniger als zwei Monate verspätete, jeweils vollständige Sozialversicherungszahlungen reichen für sich allein nicht. Mehrmonatige Nichtabführung und hinzutretende Umstände können anders zu bewerten sein. BGH, Urteil vom 12.10.2006 – IX ZR 228/03, Rn. 12–24, behandelt Stundungsbitten, erhebliche Rückstände und die Grenzen einer Entlastung durch einzelne Zahlungen; die gewährte Stundung von einer bloßen Bitte unterscheiden. Objektive Insolvenzlage, Kenntnis und Gläubigerbenachteiligungsvorsatz nicht vermengen.

BGH, Urteil vom 12.03.2026 – [IX ZR 18/25](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZR__18-25.pdf?__blob=publicationFile&v=1), Rn. 24–32: Tatsächlich verfügbare Drittmittel zählen auch ohne einklagbaren Anspruch gegen den Geldgeber. Frage nach Kontoauszug, Zahlweg, Betrag und Zeitpunkt; eine bloße Hoffnung genügt nicht. Über längere Zeit bis zur Eröffnung unbezahlte erhebliche Schulden im Gesamtbild würdigen, einschließlich tatsächlicher Zahlungen von Angehörigen oder verbundenen Unternehmen. Ein außenstehender Prozessgegner muss keine ihm unbekannten Schuldnerfinanzen rekonstruieren; vorgelegte Urkunden werden nicht zu seiner eigenen Wahrnehmung. Das Urteil verweist insoweit zurück und stellt Zahlungsunfähigkeit nicht abschließend fest.

### 1.2.4. Streitige Verpflichtungen und Belege

Maßgeblich sind objektiver Bestand und Fälligkeit. Bloßes Bestreiten und eine geschätzte Prozessverlustquote rechtfertigen weder Herausnahme noch Teilansatz einer Verpflichtung. Bei einem vorläufig vollstreckbaren Titel, vorliegenden Vollstreckungsvoraussetzungen und eingeleiteter Vollstreckung ist die titulierte Forderung mit ihrem Nennwert zu berücksichtigen; BGH, Urteil vom 23.01.2025 – IX ZR 229/22, Rn. 34–43. Diese Regel betrifft Verbindlichkeiten der geprüften Gesellschaft, nicht ihre eigenen Aktivforderungen. BGH, Beschluss vom 11.03.2025 – II ZR 139/23, S. 2–3, bestätigt den objektiven Maßstab im Nichtzulassungsbeschwerdeverfahren; er ist kein neues Grundsatzurteil.

Titel, Klausel, Zustellung, Sicherheitsleistung, Vollstreckungsbeginn und Einstellungsentscheidung prüfen, soweit einschlägig. BGH, Beschluss vom 22.05.2025 – IX ZB 38/24, Rn. 10–18, behandelt die wirksam erreichte Vollstreckungseinstellung bei einem allein von dieser Titelforderung abhängigen Eröffnungsgrund. Der Wegfall einer prozessualen Beweiswirkung ist nicht automatisch der Wegfall einer materiell bestehenden fälligen Schuld. Stundung, Nichtbestehen, Aufrechnung, Rangrücktritt und Durchsetzungssperre jeweils anhand ihrer konkreten Voraussetzungen und Wirkung einordnen. Eine nur beantragte Stundung genügt nicht; umgekehrt besteht kein allgemeines zivilrechtliches Schriftformerfordernis für jede Stundungsabrede. Bloßes Stillhalten nicht mit einer wirksamen Vereinbarung verwechseln. Bei steuerlicher Aussetzung der Vollziehung, Vollstreckungsaufschub oder behördlicher Stundung konkrete Entscheidung und Wirkung auf Durchsetzbarkeit und insolvenzrechtliche Berücksichtigung prüfen; keine pauschale Gleichsetzung vornehmen.

Jede erhebliche Position mit Gläubiger, Rechtsgrund, Betrag, Fälligkeit, Beleg und Einwendung dokumentieren. BGH, Urteil vom 18.04.2024 – IX ZR 129/22, Leitsatz und Rn. 22–27, behandelt das Bestreiten durch einen außenstehenden Dritten bei pauschalem, nicht näher belegtem Vortrag. Daraus folgt kein allgemeiner Beweislastwechsel. Parteirolle, Wissensnähe, Schlüssigkeit und Beweisführung gesondert prüfen.

## 1.3. Drohende Zahlungsunfähigkeit nach § 18 InsO

Nach [§ 18 Abs. 2 InsO](https://www.gesetze-im-internet.de/inso/__18.html) beträgt der Prognosezeitraum in aller Regel 24 Monate. Untersuche die voraussichtliche Erfüllbarkeit der bestehenden Zahlungspflichten bei Fälligkeit und begründe etwaige Abweichungen vom Regelhorizont. Ein 13-, 26- oder 52-Wochen-Forecast deckt diesen Zeitraum nicht vollständig ab. Ein Stressszenario allein beweist noch nicht das wahrscheinliche Eintreten der Zahlungsunfähigkeit. Wahrscheinlichkeiten, belastbare Finanzierungsmaßnahmen und Gegeninformationen nachvollziehbar würdigen. Ein §-18-Befund löst nicht allein die Antragspflicht nach § 15a InsO aus; dessen Voraussetzungen und geeignete Restrukturierungsinstrumente gesondert prüfen.

## 1.4. Überschuldung und Fortbestehensprognose nach § 19 InsO

Nach [§ 19 Abs. 2 InsO](https://www.gesetze-im-internet.de/inso/__19.html) liegt Überschuldung vor, wenn das Vermögen die bestehenden Verbindlichkeiten nicht deckt, es sei denn, die Fortführung ist in den nächsten zwölf Monaten nach den Umständen überwiegend wahrscheinlich. Persönlichen Anwendungsbereich prüfen. Die zwölf Monate kalendergenau abdecken; 52 Wochen sind nicht stets zwölf Kalendermonate. Bei Altfällen Sonderregelungen und damalige Horizonte ermitteln.

Prüfe Fortführungswillen und ein schlüssiges, realisierbares Unternehmenskonzept mit Ertrags- und Finanzplan. Zahlungsfähigkeit muss im maßgeblichen Zeitraum überwiegend wahrscheinlich aufrechterhalten werden können. Beurteile aus damaliger Sicht; spätere Erkenntnisse nicht ungeprüft zurückprojizieren. BGH, Urteil vom 13.07.2021 – II ZR 84/20, Rn. 68–71, 77–85, erging zur damaligen Gesetzesfassung; der heutige Zwölfmonatszeitraum folgt aus der aktuellen Norm.

Für prognostizierte Sanierungsbeiträge Dritter ist nicht in jedem Fall ein einklagbarer Anspruch zwingend. Erforderlich sind belastbare Tatsachen für die überwiegende Wahrscheinlichkeit der Beiträge und des tragfähigen Gesamtkonzepts, einschließlich Leistungsfähigkeit, Leistungsbereitschaft, Umfang, Zeitpunkt und Bedingungen. Bisherige Hilfen oder eine weiche Patronatserklärung allein sichern die Finanzierung eines dauerhaft defizitären Unternehmens regelmäßig nicht; Rn. 77–82. Eine weiche Patronatserklärung ist mangels aktivierbaren Anspruchs auch kein Vermögenswert im Überschuldungsstatus; Rn. 74–75. Eine harte Erklärung auf Wirksamkeit, Reichweite und Werthaltigkeit prüfen. Laufend aktualisieren, bei Verschlechterung in kürzeren Abständen; Rn. 71, 85.

Fehlt eine positive Fortbestehensprognose, erstelle den eigenständigen insolvenzrechtlichen Überschuldungsstatus. Setze belegbare Verwertungswerte und die rechtlich zu berücksichtigenden Verbindlichkeiten an. Negatives handelsbilanzielles Eigenkapital ist ein Warnsignal, kein fertiger Status. Stille Reserven, selbstgeschaffene immaterielle Werte und stille Lasten brauchen eine konkrete rechtliche und wirtschaftliche Bewertung; behauptete Zukunftswerte nicht pauschal aktivieren. Die Rechnung „negatives Eigenkapital plus Gesellschafterdarlehen“ ersetzt dies nicht. Eine negative Prognose allein genügt ebenfalls nicht zur Feststellung des vollständigen Überschuldungstatbestands.

Handelsrechtliche Fortführungsannahme nach § 252 Abs. 1 Nr. 2 HGB, insolvenzrechtliche Fortbestehensprognose und nachhaltige Sanierungsfähigkeit unterscheiden. BGH II ZR 84/20, Rn. 87, warnt vor dem automatischen Schluss von HGB-Fortführungswerten auf eine positive insolvenzrechtliche Prognose. Eine positive Zwölfmonatsprognose ist keine pauschale Bescheinigung der Sanierungsfähigkeit.

## 1.5. Rangrücktritt im konkreten Wortlaut prüfen

BGH, Urteil vom 05.03.2015 – IX ZR 133/14, Rn. 15–24, 32, unterscheidet den bloßen Insolvenzrang von einer wirksamen vorinsolvenzlichen Durchsetzungssperre. Für [§ 19 Abs. 2 Satz 2 InsO](https://www.gesetze-im-internet.de/inso/__19.html) persönlichen und sachlichen Anwendungsbereich sowie einen vereinbarten Nachrang hinter § 39 Abs. 1 Nr. 1 bis 5 InsO prüfen. Bei anderen Gläubigern die tragende Vertragsgestaltung und rechtliche Grundlage benennen; nicht allein aus dem Etikett „qualifiziert“ folgern.

Erfasse betroffene Hauptforderung, Zinsen, Rangtiefe, Zahlung aus freiem Vermögen, Auslöser und Reichweite der vorinsolvenzlichen Zahlungssperre sowie Änderungen und Aufhebung. Die Forderung erlischt nicht. Ein Rangrücktritt erzeugt keinen Bankzufluss und tilgt das Darlehen nicht. Seine konkrete Wirkung auf Überschuldungsstatus und auf aktuell zu erfüllende Zahlungspflichten getrennt begründen. Nach Eintritt der Insolvenzreife kann die Abrede nicht beliebig zulasten geschützter Gläubiger aufgehoben werden; Rn. 35–42. Vertragsentwurf nur bei entsprechendem Auftrag erstellen.

## 1.6. Folgen, Aktualisierung und Ergebnis

Bei [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html) Verpflichtetenstellung, Insolvenzgrund und objektiven Eintritt prüfen. Der Antrag ist ohne schuldhaftes Zögern zu stellen, spätestens drei Wochen nach Eintritt der Zahlungsunfähigkeit beziehungsweise sechs Wochen nach Eintritt der Überschuldung. Das sind Höchstfristen, keine allgemeinen Wartezeiten. Ein Wochenetikett wie „KW 22“ genügt nicht zur taggenauen Fristberechnung. Verdachtsmomente sofort klären; nicht bis zur Fertigstellung einer idealen Tabelle abwarten. Einzelne Zahlungspflichten und § 15b InsO gesondert untersuchen, weder alles freigeben noch pauschal jede Zahlung stoppen.

Nach neuem Beleg Rechnung, Annahmen, Stichtagsbewertung, Prognose und davon abhängige Fristen aktualisieren. Änderungen, Gegenargumente und verbleibende Lücken dokumentieren. Liefere den beauftragten, ausformulierten Vermerk mit Rechenanlage; zusätzliche Vertrags-, Bank- oder Antragsdokumente nur im Auftrag. Tabellen erhalten ihre Formeln; formatierte Textdokumente verwenden Times New Roman 11 pt und dezimale Gliederung. Quellenprotokoll und technische Hinweise gehören in eine getrennte Arbeitsnotiz, nicht in einen versandfertigen Empfängertext.

IDW S 6 und IDW S 11 sind fachliche Standards, keine Gesetze. Konkrete Fassung und Textziffern nur aus tatsächlich zugänglicher, überprüfter Quelle verwenden. Ein standardkonformes Gesamtgutachten oder eine vollständige rechtliche Prüfung nicht allein aufgrund eines Vorlagennamens behaupten.
