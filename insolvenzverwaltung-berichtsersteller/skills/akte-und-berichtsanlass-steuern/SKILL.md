---
name: akte-und-berichtsanlass-steuern
description: Ordnet Insolvenzakte und Berichtsanlass. Ermittelt Gericht, Rolle, Zeitraum, Stichtag, Frist, führende Fassung und Beleglücken und erzeugt die Verfahrenskarte für Zwischenbericht, Schlussbericht oder Nachtragsbericht.
---

# Akte und Berichtsanlass steuern

## 1. Zweck und Anwendungsfall

Dieser Skill eröffnet jeden Berichtslauf. Er verhindert, dass ein Bericht für das falsche Verfahren, den falschen Zeitraum, aus einer überholten Fassung oder ohne die konkrete gerichtliche Vorgabe erstellt wird. Er wird bei einer neuen Akte, einem gerichtlichen Berichtsauftrag, einer turnusmäßigen Fortschreibung, einem geplanten Abschluss oder einem nachträglich ermittelten Gegenstand verwendet.

Der Skill erstellt noch keine materielle Endfassung des Berichts. Er schafft eine belastbare Verfahrens- und Berichtskarte, eine Dokumentenmatrix und eine priorisierte Lückenliste. Bereits vorhandene Unterlagen werden zuerst gelesen. Nur Angaben, die weder aus der Akte hervorgehen noch ohne Einfluss auf das Ergebnis bleiben, werden erfragt.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-INT`. Die Fachroute übergibt an alle Fachrouten und `berichtserstellung-steuern`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Identität | Gericht, Aktenzeichen, Schuldner, Rechtsform, Anschrift und Verfahrensart | Eröffnungsbeschluss und Gerichtsakte |
| Rolle | Bestellung, berichtende Person, Vollmacht oder interne Zuständigkeit | Bestellungsbeschluss und Kanzleiorganisation |
| Berichtsauftrag | Zwischen-, Schluss-, Nachtrags- oder Fachbericht, Empfänger und Fragestellung | gerichtliche Verfügung oder dokumentierter Auftrag |
| Zeit | Berichtszeitraum, Stichtag, Einreichungsfrist, Vorfrist | Verfügung, Terminbeschluss und Fristenkontrolle |
| Vorfassung | letzte eingereichte und letzte interne Fassung samt Zugangsnachweis | Dokumentenmanagement und Gerichtsverkehr |
| Datenstände | Buchhaltung, Bank, Kasse, Tabelle, Verwertung, Steuern, Vergütung, Prozesse | jeweilige Fachakte |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Stichtags- und Deltaauftrag

Legen Sie drei Zeitmarken fest: `T0` ist der Stichtag der letzten tatsächlich eingereichten Fassung, `T1` der neue Berichts- oder Rechenstichtag und `N` der letzte Tag, bis zu dem Nachlaufbelege technisch eingegangen sind. Ein Beleg mit Dokumentdatum nach `T1` darf eine vor `T1` entstandene Tatsache belegen; er wird dann als nachgereichter Beleg gekennzeichnet. Ein erst nach `T1` eingetretenes Ereignis wird weder in Bestand noch Quote zum `T1` eingerechnet, sondern in einer gesonderten Nachlaufzeile mit seiner möglichen Folgewirkung ausgewiesen.

Die Verfahrenskarte enthält für jeden Datenbereich den Stand zu `T0`, die Veränderungen bis `T1`, den Stand zu `T1`, Nachlaufereignisse und die Kontrollbeziehung `Stand T0 + Zugänge - Abgänge ± Korrekturen = Stand T1`. Eine Korrektur früherer Daten wird von einer echten Periodenbewegung getrennt. Kann diese Überleitung nicht belegt werden, lautet der Status nicht „unverändert“, sondern `offen` mit der konkret gesperrten Aussage.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Lesen Sie zuerst Bestellungs- und Eröffnungsbeschluss sowie die aktuelle gerichtliche Verfügung. Trennen Sie tatsächliche Anordnung, kanzleiinterne Wiedervorlage und bloße Erwartung.
2. Bilden Sie eine eindeutige Verfahrenskennung. Prüfen Sie Namensvarianten, Registerdaten, frühere Firmierung und verbundene Verfahren, ohne Akten zu vermischen.
3. Bestimmen Sie den Berichtstyp aus Auftrag und Verfahrensstand. Ein Schlussbericht wird nicht allein deshalb gewählt, weil eine Schlussrechnung vorbereitet wurde.
4. Erfassen Sie für jede Quelle Dokumentenkennung, Datum, Absender, Zeitraum, Betrag, Speicherort, Fassung und Tatsachenstatus. Markieren Sie Dubletten und widersprechende Versionen.
5. Ermitteln Sie je Datenbereich den tatsächlichen Stichtag. Stellen Sie unterschiedliche Stände offen nebeneinander und schlagen Sie einen gemeinsamen Berichts- oder Rechenstichtag vor.
6. Erstellen Sie eine Lückenliste mit konkreter Auswirkung. Eine fehlende Bankauskunft kann den Kontenabgleich sperren; eine fehlende historische E-Mail muss nicht jeden Berichtsteil blockieren.
7. Vergeben Sie die führende Fassung nach dem Schema `BER-INT-[Verfahren]-[Stichtag]-v[Nummer]` und dokumentieren Sie Dateihash, Ersteller und Änderungsgrund.
8. Routen Sie jede Fachfrage an das passende Modul und bestimmen Sie das nächste prüfbare Produkt.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

### 3.3 Qualitätsgates

`G1 Auftrag` ist erst erfüllt, wenn Rolle, Berichtstyp, Zeitraum, `T0`, `T1`, Empfänger und Frist aus dem Bestellungsbeschluss, der konkreten Verfügung oder einem dokumentierten Auftrag auf dieselbe Verfahrensidentität zurückgeführt sind. Ein ungeklärter Schuldner, ein nicht belegter Fristauslöser oder ein widersprüchlicher Stichtag sperrt die Empfängerfassung. `G2 Belegbestand` ist erst prüfbereit, wenn jede wesentliche Berichtsaussage eine Aktenfundstelle oder einen ausdrücklich offenen Nachweisweg besitzt und die Deltaüberleitungen der zahlenführenden Bereiche vollständig sind. „Unterlagen liegen vor“ genügt als Nachweis nicht.

Der Gatevermerk enthält jeweils Prüffrage, Ergebnis, Nachweiskennung, Prüfer, Prüfzeitpunkt und Sperrfolge. Bei Nichterfüllung wird nicht der gesamte Lauf pauschal angehalten: Der Skill benennt genau, welche Passage, Zahl oder Anschlussroute weiterbearbeitet werden darf und welche gesperrt bleibt. Ohne `G1` entsteht keine Empfängerfassung; ohne `G2` darf nur eine als vorläufig gekennzeichnete Arbeitsfassung mit sichtbarer Lücke entstehen.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

Für jede Route wird ein eigener Übergabesatz erzeugt. An `zwischenbericht-erstellen` gehen `BER-INT`, die letzte eingereichte Berichtsfassung und die Veränderungsmatrix `T0/T1/N`. An `schlussbericht-erstellen` gehen zusätzlich die Abschlussreifematrix und die stichtagsgleichen Kennungen von `BER-MV`, `BER-FQ`, `BER-SKV`, `BER-PAH` und `BER-SR`. An `nachtragsverteilung-bearbeiten` gehen historischer Schlussbericht, Schlussrechnung, Schlussverzeichnis, Aufhebungsbeschluss und die neue Fundmeldung; eine bloße Ordnerfreigabe ist keine produktgenaue Übergabe.

## 4. Quellenpflicht

§ 58 InsO erklärt die gerichtliche Aufsicht, ersetzt aber nicht die konkrete Verfügung. § 66 InsO betrifft Schlussrechnung und Zwischenrechnungslegung; daraus folgt kein einheitliches gesetzliches Textschema für jeden Bericht. Prüfen Sie deshalb zusätzlich die tatsächliche gerichtliche Vorgabe.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** § 58 InsO trägt die Einordnung der gerichtlichen Aufsicht und § 66 InsO die Unterscheidung von Rechnungslegung und Berichtsanlass. Die Quellenkarte trägt außerdem die dort ausdrücklich abgegrenzten Anforderungen an Abschlussreife, Verteilung und Nachtrag, wenn die jeweilige Route eröffnet ist.

**Trägt nicht:** Diese Quellen bestimmen nicht ohne konkrete Verfügung Berichtsturnus, Empfänger, Stichtag oder Dateiformat. Sie belegen auch keine tatsächliche Bestellung, Frist, Einreichung oder Freigabe des einzelnen Verfahrens.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-INT`

1. Verfahrensidentität und Rolle
2. Berichtsanlass, Empfänger und Rechtsgrund
3. Zeitraum, Stichtag, Frist und Vorfrist
4. Führende Vorfassung und Einreichungsnachweis
5. Datenstands- und Dokumentenmatrix
6. Lücken, Sperrwirkungen und Beschaffungsplan
7. Fachrouting, Gates und nächste Produkte

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Turnusmäßiger Zwischenbericht

Das Gericht fordert einen Bericht zum 30. September. In der Akte liegen ein Bericht zum 31. März, Buchhaltung bis 30. September, Kontoauszüge nur bis 20. September und eine Verwertungskorrespondenz vom 4. Oktober. Der Skill setzt den Berichtszeitraum ab 1. April und kennzeichnet den Bankdatenstand als abweichend. Die spätere Korrespondenz wird als Ereignis nach dem Stichtag geführt. `G2` bleibt für eine abschließende Liquiditätsangabe offen, während Masse- und Prozessabschnitte weiterbearbeitet werden.

### 6.2 Falsche Vorakte

Ein Ordner enthält zwei Gesellschaften mit ähnlichem Namen. Der Bestellungsbeschluss betrifft nur eine Gesellschaft; einzelne Kontoauszüge gehören der Schwester. Der Skill trennt beide Verfahrenskennungen, sperrt die fremden Kontobelege und fordert keinen neuen Sachverhalt an, bevor vorhandene Register- und Beschlussdaten ausgewertet sind.

### 6.3 Nachlaufbeleg mit Wirkung vor dem Stichtag

Der Kontoauszug bis `T1` geht erst fünf Tage später ein und zeigt eine am `T1` valutierte Gutschrift. Der Skill nimmt den Betrag in den Bestand zu `T1` auf, bezeichnet den Auszug als nachgereichten Beleg und setzt `N` auf sein Eingangsdatum. Eine erst zwei Tage nach `T1` valutierte Zahlung bleibt dagegen Nachlaufereignis. Die Verfahrenskarte weist beide Sachverhalte getrennt aus und übergibt dem Rechenmodul genau diese Abgrenzung.
