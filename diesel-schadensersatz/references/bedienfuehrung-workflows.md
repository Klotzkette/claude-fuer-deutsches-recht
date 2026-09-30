# Bedienführung und Workflow-Standards

Diese Referenz hält fest, wie Skills im Tagesgeschäft wirken sollen: wie eine gute Arbeitsmaske, nicht wie ein Lehrbuch. Zielgruppe sind Diesel-Geschädigte (Fahrzeugkäufer und Halter) sowie ihre Berater — Kanzleien, Verbraucherschutz und Legal-Tech-Dienste. Sie brauchen schnelle Orientierung, klare Rückfragen und verwertbare Zwischenergebnisse.

Die Perspektive ist verbraucherseitig, kritisch und respektvoll. Hersteller-, KBA- und Kanzleivortrag wird auf vollständige Unterlagen, technische Vergleichbarkeit, Widerspruch und Beweiswert geprüft; polemische Motive, Konzernkritik ohne Tatsachenbasis oder Vorwürfe zu Prozessbetrug werden nicht erfunden oder übernommen.

## 0. Zustands- und abhängigkeitsbasierter Skill-Router

Vor der Skill-Auswahl wird zuerst geprüft, ob ein valider Arbeitsstand nach [Promptketten-Schnelllauf](./promptketten-schnelllauf.md) vorliegt. Dann startet der ausdrücklich verlangte Fachskill direkt; erledigte Skills, belegte Tatsachen und bereits geprüfte Quellen werden nicht erneut geladen oder hergeleitet. Nur eine neue Datei, ein echter Widerspruch, eine geänderte Rechtslage oder eine ergebnisrelevante Gate-Lücke rechtfertigt einen Rücksprung.

Ohne validen Arbeitsstand wird aus dem Eingangssignal genau ein federführender Startskill gewählt. Skill 01 ist der Default für neue oder ungeordnete Akten; ein klar abgegrenzter Fachauftrag darf direkt beim zuständigen Skill beginnen. Höchstens zwei umfangreiche, wirklich unabhängige Vorprüfungen dürfen parallel laufen. Ihre Befunde werden getrennt belegt und erst danach über Fakten-IDs, Quellen und Gate-Änderungen zusammengeführt.

| Eingangssignal | Federführender Start | Nur bei offener Abhängigkeit | Nicht laden |
|---|---|---|---|
| Neuer Fall, gemischtes Upload-Bundle, Scan, E-Mail, Foto, Fahrzeugpapiere oder unklare Dateien | `01-kaltstart-aktenaufnahme` | `02` bei Vertrags-/Zahlungslücke; `03` bei Frist-/Zugangslücke; `04` bei Fahrzeug-/Rückruflücke; sonst direkt `06` | keine Klage- oder Anspruchsschreiben-Entwürfe vor belastbarem Inventar |
| Kaufvertrag, Rechnung, Finanzierung, Kontoauszug, Kilometerstand, Belege | `02-kaufvertrag-zahlungen-belege` | `03` nur bei Zeitachsenfrage; `08` nur für Bezifferung; `06` nur für Anspruchswahl | nicht direkt `14`, `15` oder `17` ohne deren Gates |
| Motor, Abschalteinrichtung, Thermofenster, EA189/EA288/OM651, KBA-Rückruf, Software-Update | `04-betroffenheit-motor-kba-rueckruf` | `05` nur bei konkreter Einrichtungs-/Updatefrage; `06` nur für Anspruchswahl | keine Klage ohne Anspruchsgrundlage und Schadenshöhe |
| Frage nach Anspruch, Strategie, Erfolgsaussicht oder Geld zurück | `06-anspruchstriage-fallstrategie` | `07` bei Fristspur; `08` bei Bezifferung; danach `09` oder `13` nach Ziel | kein Schriftsatz ohne tragfähige Triage |
| Altkauf, Verjährungsfrage, Restschadensersatz | `07-verjaehrung-restschadensersatz` | zurück an `06` | keine Klage ohne Fristenkarte |
| Anspruchsschreiben, Fristsetzung, Zustellung, Zugangsnachweis | `09-anspruchsschreiben-zugangsnachweis` | `18` bei Angebot, `13` bei Ablehnung | keine Klage ohne Zugangsnachweis |
| Anwalt, Rechtsschutz, Prozessfinanzierer, Legal-Tech-Abtretung, Deckungsanfrage | `10-vertretung-prozessfinanzierung-abtretung` | `13` oder `11` | keine Eigenbearbeitung bei Anwaltszwang |
| Musterfeststellungsklage, Sammelklage, VDuG, Verbandsklage | `11-musterfeststellung-vdug-kollektivklage` | `13` bei Einzelspur | kein Automatismus für eine Spur |
| Kfz-Darlehen, Leasing, Widerruf, Widerrufsjoker, verbundenes Geschäft | `12-finanzierungswiderruf-verbundgeschaeft` | `09`, ggf. `13` | keine Vermengung mit der Deliktsspur |
| Klage vorbereiten: Streitwert, Gericht, Klageform, Kostenrisiko | `13-klageweg-streitwert-zustaendigkeit` | `14` oder `15`, dann `21`, dann `16` | keine Klage ohne Verjährungsprüfung |
| Klageentwurf großer Schadensersatz, Rückabwicklung, Zug um Zug | `14-klage-rueckabwicklung-zug-um-zug` | `21`, dann `16` | nicht bei bloßem Thermofenster ohne Vorsatzlinie |
| Klageentwurf Differenzschaden, Fahrzeug behalten | `15-klage-differenzschaden` | `21`, dann `16` | keine Zug-um-Zug-Formel |
| beA-versandfertig, Anlagen K1/B1, PDF-Stempel, Anlagenverzeichnis, Dateinamen, Replikpaket | `21-bea-versandfertig-schriftsatz-anlagen` | bei grünem Paket `16` | kein Versand und kein Eingangsversprechen in Skill 21 |
| tatsächliche beA-Einreichung, Signatur, gerichtliche Eingangsbestätigung | `16-klage-einreichen-bea-egvp` | `03` und bei Erwiderung `17` | kein Versand ohne grünen Skill-21-Bericht |
| Klageerwiderung des Herstellers, gerichtlicher Hinweis, Widerklage, Replikfrist | `17-klageerwiderung-replik-beweis` | `21`, dann `16`; `18` bei Vergleichssignal | keine neue Klage als Standard |
| Vergleichsangebot, Abfindung, Zahlung des Herstellers nach Klage | `18-vergleich-abfindung-nachzahlung` | `19` | keine automatische Klagerücknahme |
| Urteil, Vergleich, KFB, Kostenfestsetzung, Vollstreckung, Zahlungsüberwachung | `19-kosten-vollstreckung-monitoring` | Monitoring bis Erledigung | keine neue Anspruchsprüfung als Hauptpfad |
| Export, E-Akte, Kanzleisoftware, RA-MICRO, SAP, DMS, XML, CSV, JSON | `20-eakte-export-kanzleisoftware` | zurück in den Fachpfad | kein Datei-Dump ohne Mapping-Vermerk |

Negativtrigger sind verbindlich: keine Vollstreckung ohne Titel, keine Rückabwicklung ohne wirksamen Anspruch und Rückgabeangebot, kein großer Schadensersatz ohne § 826 BGB (Vorsatz/Sittenwidrigkeit), kein Differenzschaden ohne Schutzgesetzverstoß, keine Klage ohne Verjährungsprüfung, kein Widerruf ohne Prüfung der verbundenen Verträge.

### Deterministischer Vorlauf bei Aktenordnern

Bei lokalem Ordnerzugriff läuft für einen neuen oder geänderten Dateibestand vor Skill 01 genau einmal `tools/diesel-aktenstart.py`. Ein zum unveränderten Bestand passendes Manifest wird wiederverwendet. Das Manifest trennt Maschinenbefunde (relativer Pfad, Größe, SHA-256, Dateikopf) von bloßen Dateinamenheuristiken (Kategorie, mögliche Beweisrolle). `BLOCKIERT` verhindert die Inhaltsanalyse der betroffenen Datei; `PRUEFUNG_NOETIG` lässt die Bearbeitung mit den ausdrücklich genannten Kontrollen weiterlaufen. Das Modell darf weder aus einem Dateinamen einen Dokumentinhalt noch aus Hashgleichheit Aktualität, Originalqualität oder Beweisrang ableiten.

Die Startstrecke liest identische Hash-Dubletten nicht mehrfach. Sie übernimmt Dokument-ID und relativen Pfad in jede spätere Fundstelle, fragt höchstens drei strategierelevante Lücken ab und übergibt danach genau einen Fachskill. Ohne lokalen Ordnerzugriff wird dieselbe Trennung auf die sichtbare Uploadliste angewandt.

## 0a. Korrektur bei falscher Skill-Auswahl

Wenn ein Modell trotz Aktenlage den falschen Fachskill lädt, wird nicht im falschen Skill weitergearbeitet. Die Bearbeitung wird auf eine Startkarte zurückgeführt:

1. Eingangssignal benennen: Welche Datei, welcher Satz oder welches Dokument hat den aktuellen Pfad ausgelöst?
2. Gegen die Router-Tabelle prüfen: passt das Signal wirklich zu diesem Skill?
3. Bei Fehlgriff genau einen neuen Skill nennen und kurz begründen.
4. Bisherige Zwischenergebnisse nur als Rohmaterial übernehmen, nicht als fachliche Entscheidung.
5. Bei zwei gleich starken Pfaden den Skill wählen, der die ergebnisrelevante offene Abhängigkeit verantwortet. Intake oder Triage werden nur wiederholt, wenn ihr eigener Befund fehlt oder durch neue Tatsachen überholt ist.

Typische Korrekturen:

| Falsch geladener Skill | Richtiger Neustart | Grund |
|---|---|---|
| `14` (Rückabwicklung) ohne tragfähige §-826-Spur | `05` -> `06` -> ggf. `15` | Differenzschaden nur bei fahrzeugbezogenem objektivem Verstoß, weiteren Voraussetzungen und positiver Netto-Aufzehrungsrechnung |
| `17` bei bloßem vorgerichtlichem Anwaltsschreiben | `09` | Prozessuale Replik erst nach Rechtshängigkeit; vorher Korrespondenz und Fristen |
| `19` bei bloßem Klageentwurf ohne Titel | `13` | Ohne Titel oder KFB keine Kosten- und Vollstreckungsarbeit |
| `02` bei gemischtem Upload-Bundle | `01` | Erst Dokumentenbestand, Lesbarkeit und Metadaten sortieren |
| `14` oder `15` ohne Verjährungsprüfung bei Altkauf | `07` | Bei Kauf vor mehreren Jahren zuerst Verjährung und Restschadensersatz klären |

## 0b. Profi-Modus und Schnelllauf

Bei Signalen wie "Profi-Modus", "Schnelllauf", "Bulk", "nur Ergebnis", "Klagepaket" oder "E-Akte fertig" wird die Ausgabe verdichtet, nicht die Prüfung. Startkarte, Inventar, Konflikte, Fristen, Quellenstatus und nächstes Arbeitsprodukt werden in einem Durchgang geliefert; Rückfragen beschränken sich auf tatsächlich blockierende Punkte.

Der Schnelllauf darf keine Sicherheitsstufe absenken. Verjährung, unklarer Hersteller oder Gegner, ungeklärte Betroffenheit, fehlender Titel, Anwaltszwang, RDG-Grenzen und Datenschutzverstöße bleiben rote Stopps. Wo mehrere Dateien oder Exporte verlangt sind, werden sie als konsistentes Paket mit Kontrollbericht statt als unkommentierter Rohdaten-Dump ausgegeben.

Liegt ein valider Arbeitsstand vor, bedeutet Schnelllauf: Arbeitsstand übernehmen, aktiven Skill und kleines Quellenpaket laden, nur das Delta bearbeiten und genau einen nächsten Schritt ausgeben. Er bedeutet nie, die lineare Anfangsstrecke erneut abzuarbeiten. Die ausführlichen Regeln zu Laufprofilen, Kontextschichten, Direkteinstiegen und Übergaben stehen in [Promptketten-Schnelllauf](./promptketten-schnelllauf.md).

## 0c. Kleiner Modellkontext

Kleinere Modelle laden nicht den vollständigen Rechtsprechungskorpus und nicht mehrere Fachskills vorsorglich. Sie erhalten den validen Arbeitsstand oder bei einem neuen Fall genau eine Startkarte, den aktiven Skill, die für ihn nötige Referenz und höchstens sechs Rechtsprechungstreffer aus `tools/diesel-fuenfjahre-query.py --arbeitsset`: bis zu zwei höchstrichterliche EuGH-/BGH-Anker, zwei vergleichbare Instanzanker, eine Gegenlinie und einen Behörden-/Statusanker. Jeder Treffer bleibt mit Quellenrang, Verifikationsstatus und Verwendungsgrenze verbunden; Rang C/D wird nie als Rechtsprechungsbeleg formuliert. Erledigte Prüfungen werden nicht neu hergeleitet.

## 0d. Einheitlicher Kanzlei-Arbeitskopf

Jeder Skill stellt seinem Arbeitsprodukt außerhalb des eigentlichen Dokuments den kompakten `Kanzlei-Arbeitskopf` aus `diesel-schadensersatz/assets/templates/kanzlei-arbeitskopf.md` voran. Die sechs Felder sind immer Status, Ampel mit fallbezogenem Grund, Frist, Quellenstand, genaue Bezeichnung des Arbeitsprodukts und genau ein nächster Schritt. Statuscodes werden exakt aus der Vorlage übernommen; Unterstriche werden nie durch Leerzeichen ersetzt. Unbekanntes wird als offene Prüfung bezeichnet; leere Felder, unverdientes Grün und mehrere konkurrierende nächste Schritte sind unzulässig.

Der Arbeitskopf ist ausschließlich Kontroll- und Begleitansicht. Er wird nie Teil eines Schriftsatzes, einer Anlage, eines Mandantenanschreibens oder einer Exportdatei. `VERSANDFERTIG` setzt den grünen Skill-21-Prüfbericht voraus; `EINGEREICHT` setzt zusätzlich die kontrollierte gerichtliche Eingangsbestätigung aus Skill 16 voraus.

## 1. Erste Antwort

Wenn ein neuer Fall eingeht, beginnt die Ausgabe mit einer Startkarte. Bei vorhandenem validem Arbeitsstand beginnt sie stattdessen mit Ergebnis oder konkretem Engpass und dem seit dem letzten Stand entstandenen Delta; Fallkarte und unveränderte Belege werden nicht erneut ausgeschrieben.

| Feld | Inhalt |
|---|---|
| Fallart | Großer Schadensersatz, Differenzschaden, Feststellung, Finanzierungswiderruf, Verteidigung, Kosten, Vollstreckung |
| Ampel | grün, gelb oder rot |
| Warum | ein Satz |
| Nächster Schritt | genau ein empfohlener Skill oder eine konkrete Rückfrage |
| Fehlendes Kernstück | höchstens drei Punkte |
| Frist | Datum, Vorfrist, Verjährungsrisiko |

## 2. Rückfragen

Rückfragen sind erlaubt und gewollt, aber sie müssen bedienbar bleiben:

1. Maximal drei Rückfragen auf einmal.
2. Jede Rückfrage muss sagen, warum sie gebraucht wird.
3. Wenn der Fall trotzdem bearbeitbar ist, wird mit gelber Ampel vorläufig weitergearbeitet.
4. Nur rote Lücken stoppen den Workflow: unklarer Hersteller/Gegner, unklare Betroffenheit, abgelaufene Verjährung, fehlender Titel, ungeklärte Abtretung an Legal-Tech oder Prozessfinanzierer.

## 3. Workflow-Menü

Ein Menü wird nur angeboten, wenn nach Intake oder Triage mehrere gleich tragfähige Ziele offen sind und die Auswahl das Ergebnis verändert. Ist das Ziel klar, startet der zuständige Skill direkt und nennt genau einen nächsten Schritt.

| Auswahl | Workflow | Start |
|---|---|---|
| 1 | Betroffenheit und Anspruch klären | `04`, `05`, `06` |
| 2 | Verjährung, Schadenshöhe und Anspruchsschreiben | `07`, `08`, `09` |
| 3 | Rückabwicklung Zug um Zug | `13`, `14`, `21`, `16` |
| 4 | Differenzschaden und EA288-Fahrlässigkeitslinie | `05`, `06`, `08`, `15`, `21`, `16` oder `17` |
| 5 | Finanzierung, Widerruf, Prozessfinanzierung | `10`, `11`, `12` |
| 6 | Klageerwiderung, Vergleich, Kosten und Vollstreckung | `17`, `18`, `19` |
| 7 | Unterlagen, E-Akte, Datenschutz und Schnittstellen | `01`, `02`, `03`, `20` |
| 8 | Anwaltliche Eskalation oder Prozessfinanzierer | `10` |
| 9 | Fertigen Schriftsatz und Anlagen für beA finalisieren | `21`, dann `16` |

## 3a. Risikobasierte Routing-Karte

Die folgenden Routen zeigen mögliche Abhängigkeiten, keine zwingend vollständig abzuarbeitenden Ketten. Bereits grün geprüfte Schritte entfallen. Die gerichtliche Strecke `13` -> `14` oder `15` -> `21` -> `16` und die Replikstrecke `17` -> `21` -> `16` bleiben wegen ihrer Fach-, Freigabe- und Versandgates sequenziell.

| Nutzerfall | Abhängigkeitsroute | Trigger |
|---|---|---|
| Unterlagen-Intake | `01`; nur bei konkreter Lücke `02`, `03` oder `04`; danach `06` | Kaufvertrag, Rechnung, Fahrzeugschein, Scan, fehlende Vertragsdaten, Rückrufschreiben |
| Zahlungs-/Nutzungsstand | `02`; für Bezifferung `08`; für Anspruchswahl `06` | Kaufpreis, Anzahlung, Raten, Kilometerstand, Restwert, Nutzungsvorteil |
| Betroffenheit prüfen | `04`; bei konkreter Einrichtung `05`; für Anspruchswahl `06` | Motorcode, Thermofenster, EA189/EA288, KBA-Rückruf, Software-Update, Typgenehmigung |
| EA288-Fall ohne klaren KBA-Rückruf | `04`; bei Einrichtungsfrage `05`; danach `06` und bei Prozessziel `15` oder `17` | Konfigurationsgruppe, Parallelrechtsprechung, sekundäre Darlegungslast, Sachverständiger |
| Großer Schadensersatz | `06` -> `07` -> `08` -> `13` -> `14` -> `21` -> `16` | § 826 BGB, Vorsatz, Rückgabe Zug um Zug, Nutzungsentschädigung |
| Differenzschaden | `06` -> `08` -> `13` -> `15` -> `21` -> `16` | § 823 II BGB, Fahrzeug behalten, 5 bis 15 Prozent Schätzung, Restwertanrechnung |
| Verjährungsfall | `03` -> `07` -> `06` -> ggf. `14`/`15` | Kauf lange her, Kenntnis 2015/2016, Restschadensersatz § 852 BGB |
| Finanzierungswiderruf | `02` -> `12` -> `06` oder `13` | Darlehen, Leasing, verbundenes Geschäft, fehlerhafte Widerrufsinformation |
| Vergleichsangebot | `18` -> ggf. `19` | Herstellerangebot, Abfindung, Quote, Kosten- und Risikoabwägung |
| Musterfeststellung/Sammelklage | `11` -> `06` -> ggf. `13` | VDuG-Abhilfeklage, Musterfeststellung, Abtretung, Prozessfinanzierung |
| Klageerwiderung/Replik | `17` -> `21` -> `16`, ggf. `18` | Klageerwiderung, Hinweisbeschluss, sekundäre Darlegungslast, Sachverständiger |
| beA-Paket finalisieren | `21` -> `16` | fertiger Schriftsatz, Anlagen K/B, PDF, Replik, Dateinamen, Versandfreigabe |
| Anwalt/Prozessfinanzierer | `10` | Berufung, Revision, Strafrecht, Sachverständiger, Kostenrisiko, Finanzierung |
| KFA/KFB/Vollstreckung | `19` -> ggf. `10` | Urteil, Vergleich, KFB, Klausel, Zustellung, Quote, Zahlung |
| Datenschutz/Datenaufbereitung | `01` -> `20` -> zurück in den Fachpfad | Fahrzeug- und Finanzierungsdaten, Gutachterdaten, Weitergabe an Dritte |

## 4. Ausgabequalität

Jedes Zwischenergebnis enthält:

1. Ergebnis oder konkreter Engpass zuerst.
2. Frist oder Wiedervorlage, falls relevant (insbesondere Verjährung).
3. Beleg- oder Quellenstatus.
4. Ampel mit Grund.
5. Genau ein nächster Schritt.
6. Entwurf nur dann, wenn genug Fakten vorliegen; sonst Entwurf mit klaren Platzhaltern.

Eine Tabelle oder Matrix wird nur verwendet, wenn mindestens drei vergleichbare Werte oder wiederkehrende Felder strukturiert gegenüberzustellen sind. Ein einzelner Befund, eine Fallbeschreibung und eine rechtliche Würdigung werden in vollständigen Absätzen oder einer kurzen Liste dargestellt.

## 5. Übergaben

Der valide Arbeitsstand ist die Quelle der Wahrheit. Übergaben zwischen Skills wiederholen ihn nicht vollständig, sondern ergänzen ein knappes maschinenlesbares Delta: neue oder geänderte Fakten mit stabilen IDs und Fundstellen, Konflikt- und Gate-Änderungen, neu verifizierte Rechtsanker, Ergebnis und genau einen aktiven oder nächsten Skill. Beträge, Daten, FIN, Fristen, Quellenstatus, Verwendungsgrenzen und bestehende rote Gates dürfen dabei nicht verloren gehen.

| Übergabe | Mindestinhalt |
|---|---|
| Intake an Klage | Stammdaten, Fahrzeugdaten, Kaufpreis, Betroffenheit, Belege, Verjährungsstand |
| Anspruch an Klage | Anspruchsgrundlage, Schadenshöhe, Nutzungsvorteil, Restwert, Antrag, Gericht |
| Klage an Replik | gegnerische Einwendungen, Antwortlinie, Beweise, Frist |
| Entwurf an beA-Paket | anwaltliche Endfassung, bestehende Anlagenfolge, Belege, Gericht, Aktenzeichen/Neueingang, Frist |
| beA-Paket an Versand | `versand/`, SHA-256-Liste, Prüfbericht ohne Fehler/Warnungen, verantwortende Person und Signaturweg |
| Versand an E-Akte | gerichtliche Eingangsbestätigung, bestätigte Dateinamen, Empfänger, Status und Zeitpunkt |
| Urteil an Kosten | Tenor, Quote, Vollstreckbarkeit, Fristen, KFA-Bedarf |
| Kosten an Vollstreckung | Titel, Forderung, Zinsen, Kosten, Zahlungen, Schuldnerdaten Hersteller |
