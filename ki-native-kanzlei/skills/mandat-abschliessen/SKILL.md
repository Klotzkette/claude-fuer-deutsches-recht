---
name: mandat-abschliessen
description: "Verwenden, wenn ein Mandat oder eine Auftragsphase endet, ein Mandant kündigt, ein Nachfolger die Akte übernimmt oder Aufbewahrung und Löschung zu entscheiden sind. Liefert Abschlussbrief mit Restfristen, Schlussrechnung, Fremdgeldausgleich. Nicht für laufende Fristrechnung oder Rechnungsformat."
---

# Mandat abschließen und Wissen sichern

## 1. Zweck und Anwendungsfall

Dieser Skill führt ein beendetes oder zu beendendes Mandat zu einem nachvollziehbaren fachlichen, organisatorischen und wirtschaftlichen Abschluss: versandfertiger Abschlussbrief, Restpflichtenregelung, geprüfter Abrechnungsstand, Fremdgeldausgleich und eine nach Dokumentarten differenzierte Entscheidung über Herausgabe, Aufbewahrung und Löschung.

Ein gerichtliches Ergebnis, wirtschaftliche Erledigung und Ende des Auftrags sind verschiedene Zeitpunkte. Ein unterschriebener Vergleich kann noch Zahlungen, Bedingungen oder Widerrufsmöglichkeiten enthalten; ein erstinstanzliches Urteil kann Rechtsmittel, Kostenfestsetzung und Vollstreckung offenlassen; ein fertiges Gutachten schließt den Beratungsgegenstand ab, ohne dass die Kanzlei die Umsetzung überwacht. Archivierung ist kein Fristverzicht, Löschung keine Mandatsbeendigung und Zahlungsausgleich kein Nachweis vollständiger Leistung. Der Abschlussvermerk beantwortet deshalb, was erreicht wurde, was nicht erreicht wurde, welche Handlungen verbleiben, wer sie übernimmt und welche Unterlagen noch benötigt werden.

### 1.1. Auslöser, Abgrenzung und Nachbarskills

Der Skill startet in folgenden Situationen: Ein Urteil ist zugestellt und der Mandant bittet um die Schlussrechnung, ohne dass über ein Rechtsmittel entschieden ist. Ein Vergleich ist geschlossen, die Kanzlei soll die Akte schließen und zugleich Raten überwachen. Der Mandant hat gekündigt oder die Kanzlei will niederlegen. Eine andere Kanzlei verlangt wegen einer laufenden Begründungsfrist die Unterlagen. Ein Mandant verlangt nach Zahlung die Vernichtung aller Daten. Ein ausgeschiedener Partner nimmt ein Mandat mit. Eine Transaktion ist abgebrochen und das Mandat endet ohne Sachergebnis.

Die Fristberechnung mit Rechenvermerk erledigt [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md); dieser Skill übernimmt daraus nur geprüfte Datumsangaben. Die ausgegebene Rechnung erzeugt [Abrechnung und E-Rechnung](../abrechnung-e-rechnung/SKILL.md), Zahlungszuordnung und Fremdgeldbuchung liefert [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md). Berufspflichten ohne Abschlussbezug prüft [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md), schwierige Briefe unterstützt [Mandantenkommunikation](../mandantenkommunikation/SKILL.md), offene Zeiteinträge erfasst [Zeiten erfassen](../zeiten-erfassen/SKILL.md). Die Übergabe eines Mandatsstands steuert [Workflow-Übergabe](../workflow-uebergabe/SKILL.md); den Gesamtauftrag führt [KI-Kanzlei steuern](../ki-kanzlei-steuern/SKILL.md).

Dieser Skill versendet keinen Brief, legt kein Mandat nieder, zahlt kein Fremdgeld aus, übermittelt keine Akte und löscht keine Daten unwiderruflich ohne Autorisierung und konkrete rechtliche Prüfung. Eine erteilte Ermächtigung wird nicht erneut abgefragt; die Vorbereitung wird vollständig erledigt, damit die noch erforderliche Entscheidung an einem konkreten Ergebnis getroffen werden kann.

## 2. Eingaben

### 2.1. Auftrag und Beendigungsgrund

Lies Mandatsvertrag, Auftragsänderungen, Vollmacht, Honorarvereinbarung, letzte Sachstandsmitteilung und das Ergebnisdokument. Erfasse, welcher Auftrag beendet werden soll: gesamte Angelegenheit, einzelne Instanz, Vertragsverhandlung, Beratung oder Zahlungsüberwachung. Der Aktenname bestimmt den Umfang nicht; eine neue Teilaufgabe wird nicht unter „Abschlussarbeiten“ verborgen, wenn sie eine eigene Beauftragung verlangt.

Bestimme Beendigungsgrund und Zeitpunkt. Zielerreichung, vereinbarter Ablauf, Kündigung, Vertragsübernahme und tatsächliches Ruhen sind verschieden. Ein Mandant, der längere Zeit nicht antwortet, hat nicht gekündigt; eine Rechnung mit der Bezeichnung Schlussrechnung beendet den Mandatsvertrag nicht.

### 2.2. Restpflichten, Vermögen und Datenbestände

Benötigt werden aktuelle Fristen, Zustellungen, Rechtsmittelbelehrungen, Vergleichstermine, Zahlungsplan, Kostenentscheidungen, Titel, Originalurkunden, Sicherheiten und übernommene Überwachungsaufgaben. Lies Kalender und Akte zusammen: Eine Frist kann im Kalender fehlen und dennoch bestehen; eine offene interne Wiedervorlage ist umgekehrt nicht automatisch eine Mandatspflicht.

Erfasse sämtliche offenen Honorarposten, Zeiten, Auslagen, Vorschüsse, Rechnungen, Gutschriften, Zahlungen und Fremdgeld. Mandant, Rechnungsempfänger, Zahlender und Empfangsberechtigter können verschieden sein; ein Kontosaldo genügt nicht zur Zuordnung, benötigt werden Belege und Zahlungszwecke. Im Mandatsordner liefert `python3 scripts/kanzlei.py status --akte "<Mandatsordner>"` den Journalstand mit offenen Positionen; `draft` erzeugt den Rechnungsentwurf neu. Beide Befehle versenden nichts und buchen nichts.

Ermittle Originale, elektronische Handakte, Korrespondenz, signierte Dateien, Buchungsbelege, GwG-Unterlagen, Exporte, geteilte Links, Portale, lokale Arbeitskopien und KI-Dienstleisterbestände. Kläre Herausgabeverlangen, neue Vertretung, Vollmachten und legitime Empfänger; bei Organwechsel, Tod, Insolvenz oder Auflösung des Mandanten ist die berechtigte Person zu bestimmen.

### 2.3. Entscheidende Angaben

| Angabe | Warum entscheidend | Vorgehen, wenn sie fehlt |
|---|---|---|
| Genauer Auftragsumfang und Beendigungsgrund | Bestimmt, ob eine Phase oder das ganze Mandat endet und ob § 628 BGB oder § 8 RVG greifen | Aus Mandatsvertrag und letzter Korrespondenz ableiten; Umfang als Annahme kennzeichnen |
| Zustellungsdatum und Rechtsmittelbelehrung | Löst die Rechtsmittelfrist aus; ohne Datum keine Abschlussentscheidung | Abschlussbrief vorbereiten, Rechtsmittelteil offen lassen, Datum erfragen |
| Vergleichstext mit Zahlungsplan und Widerrufsfrist | Entscheidet über Titel, Raten, Verfall und Überwachungspflicht | Überwachung nicht als beendet darstellen; Text anfordern |
| Honorarmodell, Vorschüsse und Rechnungen | Schlussrechnung und Rückzahlung hängen davon ab | Entwurf mit Platzhaltern, Rechnung nicht ausgeben |
| Fremdgeldbestand mit Herkunft und Empfangsberechtigtem | § 43a Absatz 7 BRAO verlangt unverzügliche Weiterleitung | Keine Auszahlung; Betrag als ungeklärt führen |
| Herausgabeverlangen und Empfängerlegitimation | Ohne Vollmacht oder Organnachweis keine Übergabe | Register erstellen, Freigabe erst nach Nachweis |
| Offene Honorarforderung bei Herausgabe | § 50 Absatz 3 BRAO und § 17 BORA begrenzen die Zurückbehaltung | Fristrelevante Unterlagen vorrangig prüfen |
| Haftungsanzeichen, Beschwerden, Kammeranfrage | Sperrt Löschung und löst Versicherungsanzeige aus | Löschsperre setzen, Sachverhalt abfragen |
| GwG-Pflichten im Mandat | Eigene fünfjährige Aufbewahrung nach § 8 GwG | Als GwG-relevant behandeln, bis das Gegenteil feststeht |

### 2.4. Rückfragen in der richtigen Reihenfolge

Stelle nur Fragen, deren Antwort das Ergebnis ändert, gebündelt in dieser Reihenfolge:

1. „Welcher Auftrag soll beendet werden: die gesamte Angelegenheit, nur die erste Instanz oder nur die Vertragsverhandlung? Liegt eine Kündigung vor, und wann ist sie zugegangen?“
2. „Wann wurde das Urteil oder der Beschluss zugestellt, und ist die Prüfung eines Rechtsmittels beauftragt oder soll ich dafür eine Entscheidungsvorlage erstellen?“
3. „Hat die Kanzlei die Überwachung von Raten, Bedingungen oder Registervollzug übernommen, oder übernimmt der Mandant diese Aufgaben selbst?“
4. „Welches Fremdgeld liegt auf welchem Konto, aus welcher Quelle und für wen? Gibt es Treuhandauflagen oder streitige Berechtigungen?“
5. „Welche Honorargrundlage ist gespeichert, welche Vorschüsse und Rechnungen bestehen, und gibt es Arbeit, die noch nicht erfasst ist?“
6. „Wer verlangt die Herausgabe, mit welcher Vollmacht, und welche Unterlagen werden wegen einer laufenden Frist dringend benötigt?“
7. „Gibt es Beschwerden, Haftungsvorwürfe, Versicherungsmeldungen oder Anfragen der Kammer zu diesem Mandat?“
8. „Welche Systeme außer der Handakte enthalten Mandatsdaten, zum Beispiel Datenraum, Portal, Mailpostfach, KI-Werkzeug oder lokale Kopien?“

Ohne Antwort auf die Fragen 1 bis 3 wird kein Rechtsmittelverzicht und keine beendete Überwachung angenommen; Brief und Vermerk werden mit offenem Rechtsmittelteil vorbereitet. Ohne Antwort auf Frage 4 wird kein Fremdgeld ausgezahlt oder verrechnet. Ohne Antwort auf Frage 5 bleibt die Schlussrechnung Entwurf mit Platzhaltern; Brief, Handaktenregister und Aufbewahrungsvermerk werden trotzdem fertiggestellt. Ohne Antwort auf Frage 7 wird keine Löschung freigegeben; ohne Antwort auf Frage 8 nennt der Löschvermerk nur die bekannten Systeme.

## 3. Ablauf und Checkliste

### 3.1. Abschlussfähigkeit feststellen

Vergleiche ursprüngliches Ziel, vereinbarte Leistung und tatsächliches Ergebnis und benenne Abweichungen sachlich: Ein Vergleich über die Hälfte der Forderung ist kein vollständiges Obsiegen, eine Klagerücknahme nach Einigung kein rechtskräftiges Urteil. Der Mandant soll seine verbleibende Rechts- und Vermögenslage verstehen.

Prüfe, ob alle beauftragten Dokumente vorliegen und übermittelt wurden: Ein intern fertiger Vertragsentwurf ist keine unterschriftsreife Fassung, ein zugesagter Kostenfestsetzungsantrag entfällt nicht wegen erfolgreicher Hauptsache. Offene Punkte werden erledigt, übertragen oder als neuer Auftrag abgegrenzt.

Erstelle eine Abschlussentscheidung mit genau einer Kategorie: vollständig abgeschlossen, in Teilphase abgeschlossen, beendet mit Restpflichten oder noch nicht abschließbar; die letzte braucht Grund und nächsten Schritt. Ein fehlender Zeiteintrag hält die Akte nicht fachlich offen; die Abrechnung darf keine unerledigte Rechtsmittelfrage überdecken.

### 3.2. Urteil, Rechtskraft und Rechtsmittelbelehrung des Mandanten

Lies Tenor, Gründe, Kostenentscheidung, Vollstreckbarkeitsausspruch und Zustellungsnachweis; bestimme Rechtsmittel, Beschwer, Zulassung und Fristen und lasse die Berechnung im Fristenskill ausführen. Ein Urteil ist nicht rechtskräftig, weil der Mandant es akzeptiert; auch die Gegenseite kann ein Rechtsmittel haben. Rechtskraftzeugnis, Erklärung der Gegenseite und eigene Einschätzung haben unterschiedliche Beweisbedeutung.

Der Mandant erhält eine ausformulierte Belehrung mit Rechtsmittel, Fristende, Kosten und Erfolgsaussicht sowie einer Entscheidungsfrist, die der Kanzlei vor dem Fristende Bearbeitungszeit lässt; „Urteil anbei“ genügt nicht. Soll die Kanzlei das Rechtsmittel nicht übernehmen, wird dies unverzüglich erklärt; § 44 BRAO verlangt die unverzügliche Erklärung bei Ablehnung eines Auftrags und knüpft Schadensersatz an eine verspätete Ablehnung (Wortlaut am Volltext zu prüfen). Ein stillschweigendes Auslaufen des Mandats ist keine Ablehnung.

Verzicht, Rücknahme oder Nichteinlegung eines Rechtsmittels werden nicht aus einem allgemeinen Abschlusswunsch abgeleitet; dokumentiere die Entscheidung des Mandanten mit Datum und Form. Bei Fristablauf erhält der Erledigungsvermerk Beleg und rechtliche Bewertung; der Kalender wird nicht rückwirkend bereinigt, Änderungen bleiben sichtbar.

### 3.3. Vergleich und Erfüllungsüberwachung

Prüfe Zahlung, Raten, Bedingungen, Widerrufsfrist, Vollstreckungsvoraussetzungen, Freigaben, Zug-um-Zug-Leistungen und Kostenregelung. Ein gerichtlich protokollierter Vergleich ist Vollstreckungstitel nur für hinreichend bestimmte Pflichten; ein außergerichtlicher Vergleich ist nicht wegen anwaltlicher Beteiligung vollstreckbar. Der Abschlussbericht unterscheidet Anspruch und Titel.

Bestimme, wer die Erfüllung überwacht. Hat die Kanzlei dies übernommen, bleiben Zahlungstermine aktive Aufgaben mit Vertretung und Kalendereintrag; überwacht der Mandant selbst, erhält er Ratenplan, Verfallsfolgen und Reaktionsfrist erklärt. „Bitte melden Sie sich bei Problemen“ reicht nicht, wenn eine ausbleibende Rate Gesamtfälligkeit auslöst.

Bei Teilzahlung wird der Erfüllungsstand nach Tilgungsbestimmung, Zinsen, Kosten und Hauptforderung festgestellt, nicht proportional geschätzt. Der Skill bereitet Mahnung oder Vollstreckungsentscheidung vor, führt sie aber nur im bestehenden Auftrag aus.

### 3.4. Kündigung und Niederlegung

Der Anwaltsvertrag ist regelmäßig ein Dienstvertrag mit Geschäftsbesorgungscharakter. Für die Kündigung sind [§ 627 BGB](https://www.gesetze-im-internet.de/bgb/__627.html) und [§ 628 BGB](https://www.gesetze-im-internet.de/bgb/__628.html) zu prüfen, bei unentgeltlichem Auftrag [§ 671 BGB](https://www.gesetze-im-internet.de/bgb/__671.html). § 627 BGB erlaubt bei Vertrauensdiensten die Kündigung ohne Frist, verbietet dem Anwalt aber die Kündigung zur Unzeit, wenn sich der Mandant die Dienste nicht anderweitig beschaffen kann; § 671 BGB erlaubt dem Beauftragten die Kündigung nur so, dass der Auftraggeber anderweit Vorsorge treffen kann, außer bei wichtigem Grund (Tatbestände am Volltext zu prüfen). Eine Niederlegung nennt Grund, Zeitpunkt, laufende Fristen und die Zeit, die der Mandant für eine neue Vertretung braucht.

Bei Abrechnung nach vorzeitiger Beendigung untersuche nach § 628 BGB, welche Leistungen erbracht wurden und welches Interesse sie für den Mandanten noch haben; die Vorschrift regelt Teilvergütung, Rückerstattung und Schadensersatz bei veranlasster Kündigung. Weder ist entstandene Vergütung nie betroffen, noch entfällt sie automatisch; Ursache und Rechtsfolge werden im Vermerk begründet.

Die prozessuale Außenwirkung folgt [§ 87 ZPO](https://www.gesetze-im-internet.de/zpo/__87.html), der die Kündigung des Vollmachtvertrags und ihre Wirksamkeit gegenüber dem Gegner unterscheidet, im Anwaltsprozess mit besonderen Anforderungen. Ein internes Kündigungsdatum schaltet den beA-Posteingang für das Verfahren nicht ab; verbleibende Empfangs- und Übergabepflichten gehen an den Fristenskill.

### 3.5. Mandatswechsel und Aktenübergabe an die Nachfolgekanzlei

Ermittle, ob die Sache durch Kündigung und Neuauftrag, Vertragsübernahme oder Wechsel des Sachbearbeiters fortgeführt wird; die Entscheidung des Mandanten wird dokumentiert, eine Vereinbarung zwischen Partner und Kanzlei ersetzt sie nicht. Bei Vertragsübernahme werden Zustimmung, Stichtag, Übergang entstandener Honoraransprüche und offene Pflichten geklärt.

Die Übergabe enthält Sachstand, Originale, Fristauslöser, laufende Fristen mit Rechtsgrundlage, erfolgte Einreichungen, offene Beweise und nächste Handlungen; ein Downloadlink ohne Inhaltsübersicht genügt nicht. Bei knapper Frist werden Eingang der Unterlagen und Übernahme der Fristkontrolle schriftlich bestätigt; bis dahin bleibt die Frist im eigenen Kalender.

BGH, Urteil vom 15.01.2026 – Az. IX ZR 188/24 bestätigt für die dort festgestellte Vertragsübernahme den Anspruch auf vollständige auftragsbezogene Handakten aus Vertragsübernahme, § 667 BGB und § 50 BRAO. Prüfe die Voraussetzungen des konkreten Falls; fremde Mandatsgeheimnisse im selben Dokumentensystem werden vor der Übergabe abgetrennt.

### 3.6. Restfristen und nachvertragliche Hinweise

Gleiche Kalender, letzte Korrespondenz und Auftragsumfang ab; Rechtsmittel, Kostenfestsetzung, Vollstreckung, Vergleichserfüllung, Verjährung, Registervollzug und Meldepflichten können nebeneinander bestehen. Jede Restfrist wird mit Rechtsgrundlage, Ereignis, Ende, Handlung und Zuständigkeit geführt. Die Berechnung erfolgt im Fristenskill, bei Bedarf mit `python3 scripts/fristen.py --data <Profil.json> --out <neuer Ordner>`; der Abschluss übernimmt keine ungeprüften Datumsangaben.

§ 11 BORA verlangt, den Mandanten über alle für den Fortgang der Sache wesentlichen Vorgänge unverzüglich zu unterrichten (Wortlaut am Volltext der aktuellen BORA zu prüfen). Ein Mandatsende begründet keine künftige Rechtsüberwachung, beseitigt aber nicht den Hinweis auf erkennbar drohende Nachteile; formuliere Gefahr, Handlung und Zuständigen sachlich statt eines pauschalen Haftungsausschlusses.

Bekannte Verjährungsfristen des Mandanten gegen Dritte werden im Abschlussbrief konkret genannt. Die regelmäßige Verjährung beträgt drei Jahre ([§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html)) und beginnt nach [§ 199 Absatz 1 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) mit dem Schluss des Jahres, in dem der Anspruch entstanden ist und der Gläubiger Kenntnis erlangt hat oder grob fahrlässig nicht erlangt hat. Bei ruhendem Verfahren wird ausdrücklich entschieden, ob die Überwachung fortbesteht; ein Ruhen kann nach § 8 RVG die Fälligkeit auslösen, ohne das Mandat zu beenden.

### 3.7. Schlussabrechnung vorbereiten

Ermittle Vergütungsmodell und Rechtsstand. Bei RVG prüfe Angelegenheiten, Gegenstände, Gebühren, Anrechnung, Auslagen, Vorschüsse und das Übergangsrecht nach § 60 RVG; das Rechnungsdatum entscheidet nicht über die Tabelle. Bei Honorarvereinbarung bestimme Umfang, Sätze, Festpreis, Deckel, Erfolgskomponente und nachträgliche Änderungen ohne stillschweigende Umdeutung.

Die Fälligkeit folgt [§ 8 RVG](https://www.gesetze-im-internet.de/rvg/__8.html): Die Vergütung wird fällig, wenn der Auftrag erledigt oder die Angelegenheit beendet ist; im gerichtlichen Verfahren zusätzlich mit Kostenentscheidung, Ende des Rechtszugs oder längerem Ruhen (Dauer am Volltext zu prüfen). Die Berechnung muss [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html) genügen: Textform, Mitteilung durch den Anwalt oder auf seine Veranlassung, Beträge der Gebühren und Auslagen, Vorschüsse, Gebührentatbestand, Nummer des Vergütungsverzeichnisses und bei Wertgebühren der Gegenstandswert; eine eigenhändige Unterschrift ist nicht Voraussetzung.

Gleiche Zeitjournal und geleistete Arbeit ab, ohne aus einem gewünschten Endbetrag Stunden abzuleiten. Nach BGH, Urteil vom 19.02.2026 – Az. IX ZR 226/22 ist eine Klausel, nach der nicht binnen eines Monats beanstandete Zeitaufstellungen als anerkannt gelten, auch gegenüber Unternehmern unwirksam; der Leistungsnachweis stützt sich auf das Journal, nicht auf Schweigen. Ein Festpreis wird nicht rückwirkend zum Stundenhonorar; bei Zeithonorar wird keine hypothetische Zeit ohne KI angesetzt. Der Rechnungsentwurf geht mit Quellen an den Abrechnungsskill.

### 3.8. Vorschüsse, Erstattungen und Drittzahler

Ordne jeden Vorschuss der erfassten Angelegenheit zu und prüfe Rechnungen, Gutschriften und Zahlungen, damit kein Betrag doppelt angerechnet oder verlangt wird. Ein unverbuchter Kontoauszug beweist keine fehlende Zahlung; ein Rechnungssaldo genügt nicht, wenn eine Zahlung einer anderen Forderung zugeordnet wurde. Bei Überzahlung kläre den berechtigten Empfänger: Wer die Rechnung erhalten hat, ist nicht automatisch derjenige, dem der Überschuss zusteht; bei Rechtsschutzversicherung, Arbeitgeber oder Angehörigen entscheidet der Rechtsgrund der Zahlung. Eine neue Bankverbindung wird über einen bekannten Kanal verifiziert. Erstattungsansprüche gegen Gegner oder Staatskasse werden von der eigenen Vergütung getrennt; ein vereinbartes höheres Honorar ist nicht erstattungsfähig.

### 3.9. Fremdgeld und Sicherheiten

Stimme sämtliche Fremdgeldbestände mit Einzelmandaten, Empfangsberechtigten und Treuhandauflagen ab. [§ 43a Absatz 7 BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) verlangt die sorgfältige Behandlung anvertrauter Vermögenswerte und die unverzügliche Weiterleitung fremder Gelder an den Empfangsberechtigten oder die Einzahlung auf ein Anderkonto; § 4 BORA konkretisiert Pflicht und Abrechnung (Wortlaut am Volltext der aktuellen BORA zu prüfen). Die Mandatsbeendigung ändert die Zuordnung nicht. Eine Verrechnung mit Honorar setzt eine fällige, unstreitige oder vereinbarte Forderung und einen eindeutigen Rechtsgrund voraus und wird im Vermerk begründet.

Bei strittiger Berechtigung halte Betrag, Herkunft, Auflage, Streitpunkt und nächsten Schritt fest; eine Auszahlung an den früheren Ansprechpartner kann nach Organwechsel oder Insolvenz falsch sein, Hinterlegung wird nur nach Prüfung vorgeschlagen. Sicherheiten, vollstreckbare Ausfertigungen und Originaltitel werden gesondert inventarisiert mit der Entscheidung, ob Rückgabe, Entwertung, Freigabe oder Verwahrung geschuldet ist. Ein Titel wird nicht als Kopie vernichtet; die Übergabe wird mit Empfänger, Inhalt und Empfangsnachweis dokumentiert.

### 3.10. Handaktenherausgabe

Prüfe [§ 50 BRAO](https://www.gesetze-im-internet.de/brao/__50.html) sowie die vertraglichen Ansprüche aus [§ 666 BGB](https://www.gesetze-im-internet.de/bgb/__666.html) und [§ 667 BGB](https://www.gesetze-im-internet.de/bgb/__667.html). Der Umfang wird am konkreten Anspruch und Mandatsübergang beurteilt; die berufsrechtliche Beschreibung herauszugebender Dokumente begrenzt nicht zwingend jeden zivilrechtlichen Anspruch, und der Dateiname „interne Notiz“ entscheidet nicht über Herausgabe oder Schutz.

Erstelle ein Register der herauszugebenden Originale und elektronischen Dokumente mit bereits Übermitteltem und möglichen Lücken. Bei elektronischer Übergabe bleiben Dokumentbeziehungen, Anlagen und Metadaten lesbar; ein Export, der signierte Originaldateien durch Vorschaubilder ersetzt, ist unzureichend. Die Berechtigung des Empfängers wird vor der Freischaltung geprüft. Betreffen Unterlagen Rechte anderer Mandanten oder Dritter, prüfe Abtrennung und Schwärzung; weder Komplettverweigerung noch Komplettexport fremder Akten ist gerechtfertigt. Der Übergabevermerk erklärt Umfang und jede begründete Einschränkung.

### 3.11. Zurückbehaltungsrecht und unangemessene Nachteile

§ 50 Absatz 3 BRAO erlaubt die Zurückbehaltung der Handakte, bis der Anwalt wegen seiner Gebühren und Auslagen befriedigt ist, schließt sie aber aus, soweit die Vorenthaltung nach den Umständen unangemessen wäre. § 17 BORA nennt als Wege, berechtigten Interessen des Mandanten Rechnung zu tragen, Kopien oder die Übergabe von Originalen an den beauftragten Rechtsanwalt zu treuen Händen. Prüfe Höhe und Fälligkeit der Forderung, betroffene Dokumente und Dringlichkeit; ein streitiges geringes Honorar rechtfertigt nicht die Sperre einer Akte mit bevorstehender Rechtsmittelfrist.

Für die Fristwahrung benötigte Unterlagen werden vorrangig beurteilt; Teilherausgabe, Kopie oder Übergabe zu treuen Händen kann geboten sein. Die Entscheidung wird in vollständigen Sätzen begründet; Honorardurchsetzung und Schutz der Rechtspositionen bleiben getrennte Aufgaben. Eine bei Vertragsübernahme auf die neue Kanzlei übergegangene Forderung trägt kein Zurückbehaltungsrecht der alten. Ein Herausgabekonflikt wird nicht durch Löschen oder Verändern der Akte gelöst; gerichtliche Schritte erfolgen nur im Auftrag.

### 3.12. Aufbewahrung nach Kategorien

Ein einziges Löschdatum für die gesamte Akte ist zu grob. Die Handakte ist nach § 50 Absatz 1 BRAO sechs Jahre aufzubewahren; die Frist beginnt mit Ablauf des Kalenderjahres, in dem der Auftrag beendet wurde, und gilt entsprechend für elektronische Handakten (Absatznummer am Volltext zu prüfen). Maßgeblich ist das tatsächliche Auftragsende, nicht das Jahr der Schlussrechnung; bei fortbestehender Teilaufgabe endet der Auftrag erst mit ihr.

§ 50 Absatz 2 BRAO erlaubt, aus Anlass des Auftrags erhaltene Dokumente nach Aufforderung zur Abholung und sechsmonatigem Ausbleiben der Entgegennahme nicht länger aufzubewahren. Das erlaubt nicht, nach sechs Monaten die Handakte oder gesetzliche Nachweise zu vernichten; prüfe Zugang der Aufforderung und Dokumentumfang.

Steuerliche Unterlagen folgen [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html): zum Prüfstand zehn Jahre für Bücher, Aufzeichnungen und Abschlüsse, acht Jahre für Buchungsbelege, sechs Jahre für sonstige erfasste Unterlagen. Die Verkürzung auf acht Jahre stammt aus dem Vierten Bürokratieentlastungsgesetz; welche älteren Belege noch der zehnjährigen Frist unterliegen, ist am Übergangsrecht zu prüfen. Die Frist läuft nicht ab, soweit die Unterlagen für Steuern mit offener Festsetzungsfrist von Bedeutung sind. Bei eröffnetem Anwendungsbereich gilt daneben [§ 257 HGB](https://www.gesetze-im-internet.de/hgb/__257.html); eine Kanzlei ist nicht ohne Prüfung Kaufmann.

GwG-Unterlagen folgen [§ 8 GwG](https://www.gesetze-im-internet.de/gwg_2017/__8.html): Aufzeichnungen zur Identifizierung, zum wirtschaftlich Berechtigten und zu Transaktionen werden grundsätzlich fünf Jahre nach Ende der Geschäftsbeziehung oder der Transaktion aufbewahrt und danach unverzüglich vernichtet, soweit keine andere gesetzliche Pflicht entgegensteht; das gilt für die GwG-Aufzeichnungen, nicht für die Handakte als Ganzes.

| Dokumentart | Norm | Dauer | Beginn und Besonderheit |
|---|---|---|---|
| Handakte einschließlich elektronischer Akte | § 50 Absatz 1 BRAO | sechs Jahre | Ablauf des Jahres der Auftragsbeendigung |
| Erhaltene Originaldokumente des Mandanten | § 50 Absatz 2 BRAO | bis Abholung | Aufforderung und sechs Monate ohne Abholung; Zugang belegen |
| Ausgangsrechnungen und Buchungsbelege | § 147 AO | acht Jahre | Übergangsrecht und offene Festsetzungsfrist prüfen |
| Bücher, Aufzeichnungen, Abschlüsse | § 147 AO | zehn Jahre | Ablaufhemmung bei offener Festsetzung |
| Geschäftsbriefe ohne Belegcharakter | § 147 AO | sechs Jahre | Nur soweit steuerlich erfasst |
| GwG-Identifizierung und Transaktionsaufzeichnung | § 8 GwG | fünf Jahre | Ende der Geschäftsbeziehung; Vernichtungspflicht |
| Unterlagen zu Haftungsfall oder Beschwerde | Art. 17 Absatz 3 DSGVO | bis Verjährung | §§ 195, 199 BGB; Haftungsfrist dokumentieren |
| Arbeitskopien, Caches, KI-Ausgaben | Art. 5 Absatz 1 DSGVO | bis Abschluss | Keine eigene Aufbewahrungspflicht; nach Prüfung löschen |

### 3.13. Haftungsfall und Versicherungsanzeige

Prüfe, ob Haftungsansprüche, Beschwerden, Versicherungsfälle, Kammeranfragen oder andere Streitigkeiten bestehen oder erkennbar bevorstehen. Dann wird die Aufbewahrung zur Rechtsverteidigung gesondert bestimmt: Benenne Zweck, benötigte Daten und die Verjährungsfrist nach §§ 195, 199 BGB einschließlich der kenntnisunabhängigen Höchstfrist (Dauer am Volltext zu prüfen). Ein abstrakter Hinweis auf denkbare Haftung trägt keine unbegrenzte Speicherung sämtlicher Nebendaten.

Bei möglichem eigenem Fehler gelten vier getrennte Aufgaben: Der Mandant wird über Sachverhalt, Folgen und die Möglichkeit unabhängiger Beratung informiert; der Schaden wird begrenzt, etwa durch Wiedereinsetzungsantrag oder Rechtsmittel; der Fall wird dem Berufshaftpflichtversicherer nach den Bedingungen der Police mit ihren Anzeigefristen und Anerkenntnisverboten angezeigt; die Interessenkollision zwischen Kanzlei und Mandant wird geprüft und kann die Fortführung ausschließen. [§ 51 BRAO](https://www.gesetze-im-internet.de/brao/__51.html) regelt die Pflichtversicherung, der Versicherungsvertrag die Obliegenheiten im Schadenfall.

Sichere Mandatsumfang, Belehrungen, Entscheidungen, Freigaben, Fristnachweise und tatsächliche Leistung mit ursprünglichen Zeitstempeln. Eine nachträgliche Notiz wird als solche gekennzeichnet; belastende Informationen werden nicht entfernt. Der Abschlussbrief beschönigt den Schaden nicht und enthält weder Haftungsanerkenntnis noch Versicherungszusage.

### 3.14. Datenschutz und kontrollierte Löschung

Prüfe Speicherbegrenzung nach Artikel 5 Absatz 1 DSGVO und das Recht auf Löschung nach [Artikel 17 DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj/deu). Artikel 17 Absatz 3 nimmt die Verarbeitung aus, die zur Erfüllung einer rechtlichen Verpflichtung oder zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist: Handaktenpflicht, § 147 AO und § 8 GwG sind solche Verpflichtungen, die laufende Haftungsverjährung nach §§ 195, 199 BGB ein dokumentierter Rechtsverteidigungsgrund. Die Antwort auf ein Löschverlangen nennt je Kategorie Grund, Norm und Ende der Speicherung; vermieden werden „Anwaltsakten bleiben immer zehn Jahre“ ebenso wie „Auf Wunsch wird alles sofort gelöscht“.

Trenne aktive Nutzung, eingeschränkte Archivierung und tatsächliche Löschung; ein archivierter Bestand kann enger berechtigt und aus Suchindizes entfernt werden, ohne Nachweise zu vernichten. Bei externen Diensten prüfe Vertragsrechte, Löschfristen, Sicherungskopien und Bestätigung; behaupte keine Löschung aller Backups, wenn das System nur die sichtbare Datei entfernt. Irreversible Löschung erfolgt nur anhand der geprüften Kategorienentscheidung und Autorisierung nach Abgleich mit Fristen, Verfahren, Originalen und Haftungsanzeichen. Das Löschprotokoll nennt Umfang, Methode, Zeitpunkt und verbleibende Bestände, ohne den gelöschten Inhalt erneut zu speichern.

### 3.15. Elektronische Handakte und Dienstleisterbestände

Strukturierte Rechnungsdaten, signierte Dokumente, E-Mails mit Metadaten und gerichtliche Eingangsbestätigungen haben eigenständigen Beweiswert; ein PDF-Export ist nicht stets gleichwertig. Prüfe, welche Originalinformationen erhalten bleiben müssen und ob Lesbarkeit und Zugriff während der gesamten Aufbewahrungsdauer gesichert sind; ein Anbieterwechsel löst Exportfristen aus, die vor dem Vertragsende erledigt werden. Ein Mandatsabschluss beendet keine Freigabelinks in Portal, Datenraum oder KI-Werkzeug; entferne nicht mehr erforderliche Zugriffe im autorisierten Umfang, nachdem die erforderlichen Daten gesichert sind. Der Skill behauptet keine Kontrolle über Systeme, die ihm nicht zugänglich sind, und übergibt offene Maßnahmen dem Verantwortlichen.

### 3.16. Wissenssicherung ohne Geheimnisverlust

Die Verschwiegenheit nach § 43a Absatz 2 BRAO wirkt über das Mandatsende hinaus und erfasst auch die Tatsache der Beratung. Wähle für die Wissenssammlung nur zulässige und nützliche Inhalte; entferne Namen, Identifikatoren, Beträge und seltene Kombinationen, denn Buchstaben statt Namen lassen eine Transaktion identifizierbar. Geschäftsgeheimnisse und persönliche Details werden nicht übernommen.

Prüfe jede übernommene Rechtsaussage erneut am verifizierten Quellenstand; ein erfolgreicher Schriftsatz kann überholte Normen enthalten, ein Vergleich ist kein Präjudiz. Kennzeichne, ob der Baustein geprüfte Argumentation, Verhandlungsformulierung oder organisatorische Vorlage ist, mit Rechtsstand und Anwendungsbedingungen. Eine Zustimmung zur anonymisierten Fallbesprechung erlaubt keinen Upload der Originale in einen öffentlichen Dienst; die Originalakte bleibt unverändert.

### 3.17. Abschlusskommunikation

Der Abschlussbrief nennt Ergebnis, praktische Folge, verbleibende Handlungen mit Fristen, Zuständigkeit, Kostenstand, Umgang mit Originalen und den Aufbewahrungshinweis, verständlich und ohne Beschönigung. Archivpfade, Quellenprotokolle und Prüfmethoden gehören nicht hinein.

Bei negativem oder gemischtem Ergebnis erkläre, was erreicht wurde und welche Optionen bestehen, ohne Erfolgsgarantie und ohne die Behauptung, jeder Vergleich beende alle denkbaren Ansprüche. Der Mandant soll erkennen, ob weiteres Tätigwerden vereinbart ist oder eine Entscheidung ansteht. Eine Empfangsbestätigung wird nicht als Verzicht gestaltet; „alles erhalten und vollständig zufrieden“ darf keine Haftungsfreizeichnung enthalten.

### 3.18. Endkontrolle und Wiedereröffnung

Vor dem administrativen Abschluss werden Auftrag, Ergebnis, Fristen, Aufgaben, Honorar, Fremdgeld, Originale, Herausgabe und Datenentscheidung abgeglichen. Jede Restpflicht braucht Verantwortlichen und Überwachungssystem; der Status benennt, was versandt, ausgezahlt oder nur vorbereitet wurde.

Wiedereröffnung erfolgt bei neuer Beauftragung oder erheblicher neuer Tatsache; erhalte den Abschlussstand und dokumentiere Anlass, Umfang, Fristen und Honorarphase. Ein neuer Gegner verlangt erneute Kollisions- und GwG-Prüfung. Mandatsdaten werden nicht für Werbung, Training oder Produktdemonstrationen genutzt.

### 3.19. Honorar- und Zeitanschluss

Prüfe den gespeicherten Stand nach der [Arbeitsweise](../../references/arbeitsweise.md); eine bestätigte unveränderte Grundlage wird übernommen, nur echte Änderungen von Umfang, Instanz oder Vergütungsmodell führen zu erneuter Klärung. Fehlt die Grundlage, bestimme RVG, Stundenhonorar, Festpreis, Preiszusage oder Schätzung mit oder ohne Deckel, Netto- oder Bruttobezug und Auslagen. Abschlussarbeiten liegen nicht automatisch außerhalb eines Deckels.

Frage nach geleisteter, noch nicht erfasster Arbeit mit Datum, Dauer, Person, Abrechenbarkeit und Narrativ; fehlende Zeit bleibt offen, nicht null und nicht geschätzt. Bestätigte Einträge gehen mit `kanzlei.py time` in das Journal, Korrekturen mit `void`, Grund und neuer ID; `draft` aktualisiert den Rechnungsentwurf, ohne ausgegebene Rechnungen zu überschreiben. Offene Zeiterfassung hält Abschlussbrief und Aktenübergabe nicht auf.

### 3.20. Typische Fehler und Gegenkontrolle

| Fehler | Woran erkennbar | Gegenkontrolle |
|---|---|---|
| Schlussrechnung als Rechtsmittelverzicht gedeutet | Rechtsmittelfrist im Kalender gelöscht, keine Mandantenentscheidung dokumentiert | Entscheidung mit Datum und Form vorlegen; Frist bleibt bis dahin |
| Überwachung der Vergleichsraten still beendet | Akte archiviert, nächste Rate ohne Kalendereintrag | Ratenplan gegen Kalender und Brief abgleichen |
| Fremdgeld mit Honorar verrechnet | Auszahlung geringer als Eingang ohne Verrechnungsvermerk | Rechtsgrund, Fälligkeit und Unstreitigkeit der Forderung belegen |
| Akte wegen offener Rechnung komplett gesperrt | Nachfolgekanzlei meldet laufende Frist | § 50 Absatz 3 BRAO und § 17 BORA auf fristrelevante Dokumente anwenden |
| Einheitliches Löschdatum für die ganze Akte | Vermerk nennt nur ein Datum | Kategorientabelle mit Norm und Beginn je Dokumentart |
| Handaktenfrist ab Rechnungsdatum gerechnet | Beendigungsjahr fehlt im Vermerk | Tatsächliches Auftragsende feststellen und Jahr nennen |
| Löschung trotz Haftungsanzeichen | Beschwerde oder Kammeranfrage in Akte, keine Sperre | Haftungsverjährung dokumentieren, Sperre setzen |
| GwG-Aufzeichnungen nach Handaktenregel behandelt | Identifizierungsunterlagen ohne eigene Frist | § 8 GwG mit fünf Jahren und Vernichtungspflicht getrennt führen |
| Niederlegung ohne Rücksicht auf § 87 ZPO | beA-Zugang für das Verfahren abgeschaltet | Außenwirkung und Empfangspflichten bis zur Anzeige sichern |
| Vollständige Backup-Löschung behauptet | Löschprotokoll nennt nur die Produktivakte | Anbieterbestätigung und Rotationsfrist einholen |

### 3.21. Übergabe an Nachbarskills

An [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md) geht die Restfristenliste mit Ereignis, Beleg und vermuteter Norm; zurück kommt der Rechenvermerk mit Fristende und Vorfrist. An [Abrechnung und E-Rechnung](../abrechnung-e-rechnung/SKILL.md) geht der Rechnungsentwurf mit Honorargrundlage, Journalstand, Vorschüssen und offenen Punkten; zurück kommen ausgegebene Rechnung und Versandstatus. An [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md) gehen Fremdgeldabstimmung, Überzahlung und Erstattungen mit Belegen; zurück kommen Buchungsvorschläge und Auszahlungsbestätigung. An [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md) gehen streitige Zurückbehaltung, Kammeranfrage und Versicherungsanzeige mit Chronologie; zurück kommt die berufsrechtliche Entscheidung. An [Mandantenkommunikation](../mandantenkommunikation/SKILL.md) geht der Briefentwurf bei schwieriger Lage; zurück kommt die abgestimmte Fassung. An [Workflow-Übergabe](../workflow-uebergabe/SKILL.md) geht das Übergabepaket mit Register und Fristenliste; zurück kommt die Übernahmebestätigung. Bei Wiedereröffnung mit neuem Gegner gehen die Angaben an [Mandatsannahme und Interessenkollision](../mandatsannahme-interessenkollision/SKILL.md) und [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md).

## 4. Quellenpflicht

### 4.1. Tragende amtliche Normlinks

Prüfstand ist der 7. Oktober 2026. Heranzuziehen sind [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html), [§ 44 BRAO](https://www.gesetze-im-internet.de/brao/__44.html), [§ 50 BRAO](https://www.gesetze-im-internet.de/brao/__50.html), [§ 51 BRAO](https://www.gesetze-im-internet.de/brao/__51.html), [§ 627 BGB](https://www.gesetze-im-internet.de/bgb/__627.html), [§ 628 BGB](https://www.gesetze-im-internet.de/bgb/__628.html), [§ 671 BGB](https://www.gesetze-im-internet.de/bgb/__671.html), [§ 666 BGB](https://www.gesetze-im-internet.de/bgb/__666.html), [§ 667 BGB](https://www.gesetze-im-internet.de/bgb/__667.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html), [§ 87 ZPO](https://www.gesetze-im-internet.de/zpo/__87.html), [§ 8 RVG](https://www.gesetze-im-internet.de/rvg/__8.html), [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html), [§ 60 RVG](https://www.gesetze-im-internet.de/rvg/__60.html), [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html), [§ 257 HGB](https://www.gesetze-im-internet.de/hgb/__257.html), [§ 8 GwG](https://www.gesetze-im-internet.de/gwg_2017/__8.html) sowie Artikel 5 und 17 der [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj/deu). §§ 4, 11 und 17 BORA sind in der [Berufsordnung, Stand 01.12.2025](https://www.brak.de/fileadmin/02_fuer_anwaelte/berufsrecht/033-BORA_Stand_01.12.2025.pdf) nachzulesen. Der persönliche und sachliche Anwendungsbereich jeder Vorschrift wird geprüft; ihre Fristen werden nicht vermischt.

### 4.2. Verifizierte Entscheidungsanker

BGH, Urteil vom 15.01.2026 – Az. IX ZR 188/24, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2024/IX_ZR_188-24.pdf?__blob=publicationFile&v=1), Rn. 15–19, besonders Rn. 18. Trägt: Bei der dort festgestellten Vertragsübernahme folgt der Anspruch auf vollständige auftragsbezogene Handakten aus Vertragsübernahme, § 667 BGB und § 50 BRAO; nach Rn. 11 waren auch entstandene Vergütungsansprüche übergegangen. Trägt nicht: einen allgemeinen Anspruch jedes ausscheidenden Berufsträgers auf beliebige Mandatsdaten, die Weitergabe fremder Mandatsgeheimnisse oder ein Verbot begründeter Zurückbehaltungsrechte; Rn. 19 verneint das Rechtsschutzbedürfnis für eine zusätzliche Unterlassungsanordnung.

BGH, Urteil vom 19.02.2026 – Az. IX ZR 226/22, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1), Rn. 8–18 und 23–32. Trägt: Umfang und Textform der Honorarvereinbarung werden getrennt geprüft; eine Anerkenntnisfiktion für binnen eines Monats unbeanstandete Zeitaufstellungen ist auch im Unternehmerverkehr unwirksam (Rn. 31); die Darlegungs- und Beweislast für den Zeitaufwand bleibt beim Anwalt (Rn. 32). Trägt nicht: eine allgemeine Unwirksamkeit von Zeithonorarvereinbarungen oder der gesamten Vereinbarung wegen eines fehlerhaften Kostenerstattungshinweises.

BGH, Beschluss vom 04.03.2026 – Az. XII ZB 338/24, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2024/XII_ZB_338-24.pdf?__blob=publicationFile&v=1), Rn. 10–17, besonders Rn. 11–13. Trägt: Änderungen und Streichungen von Fristen müssen erkennbar und kontrollierbar bleiben; Archivierung und Erledigungsvermerke dürfen die Fristhistorie nicht unsichtbar machen. Trägt nicht: eine Aufbewahrungsdauer sämtlicher Aktenbestandteile oder ein Verbot elektronischer Kalender.

BVerwG, Beschluss vom 16.05.2025 – Az. 5 B 8.25, [amtlicher Volltext](https://www.bverwg.de/160525B5B8.25.0), Rn. 3–5. Trägt: Die automatisierte gerichtliche Eingangsbestätigung gehört zur Ausgangskontrolle; ein Signaturprotokoll genügt nicht, eine als erledigt markierte Einreichungsfrist braucht diesen Nachweis in der Akte. Trägt nicht: Aussagen zu anderen Verfahrensordnungen ohne deren eigene Norm; der Beschluss betrifft § 55a VwGO.

### 4.3. Belegdisziplin

Nutze [Rechtsquellen](../../references/rechtsquellen.md) und [Zitierweise](../../references/zitierweise.md). Zitiere nur gelesene Randnummern und keine Kommentar-, Handbuch- oder Aufsatzstellen. Die Aussagen zu § 50 BRAO, § 43a BRAO, § 8 und § 10 RVG, § 628 BGB, § 87 ZPO, § 147 AO, § 8 GwG und § 17 BORA beruhen auf den im Plugin dokumentierten Normprüfungen; mit „am Volltext zu prüfen“ gekennzeichnete Aussagen sind vor Verwendung in Brief oder Schriftsatz am amtlichen Text zu verifizieren. Eine gesetzliche Mindestaufbewahrung ist keine maximale Speicherdauer; eine mögliche Haftungsabwehr keine unbegrenzte Erlaubnis. Keine Präjudizienbindung: Jeder Anker trägt nur seinen entschiedenen Sachverhalt.

## 5. Ausgabeformat

### 5.1. Bestandteile

Das Ergebnis umfasst den Abschlussbrief, den internen Abschlussvermerk mit Abschlussentscheidung, die Restpflichtenübersicht mit Handlung, Verantwortlichem, Frist und Überwachungssystem, den Abrechnungs- und Fremdgeldstatus, das Handaktenregister mit Herausgabeentscheidung und den Aufbewahrungs- und Löschvermerk nach Dokumentarten. Tabellen ergänzen parallele Angaben; rechtliche Bewertung und Empfängertext bleiben Fließtext.

### 5.2. Ausformulierungspflicht und Formatstandard

Brief, Vermerk und Löschvermerk werden vollständig ausformuliert in ganzen Sätzen geliefert; Skelette, Halbsätze und reine Aufzählungsgerüste sind als Endprodukt unzulässig. Fehlende Angaben erhalten lesbare Platzhalter wie `[Datum der Zustellung TT.MM.JJJJ]`, der umgebende Satz bleibt vollständig. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Kann kein DOCX oder PDF erzeugt werden, steht der Exporthinweis „Times New Roman, 11 pt, dezimale Gliederung“ in einer getrennten Notiz an den Auftraggeber, nie im Brief; dort stehen auch technische Hinweise und Quellenprotokolle. Behaupte keine abgeschlossene Auszahlung, Löschung, Übergabe, Rechnungsausgabe oder Benachrichtigung ohne Vollzugsnachweis; eine vorbereitete Maßnahme heißt Entwurf oder noch auszuführen.

### 5.3. Abnahmekriterien

Das Produkt ist fertig, wenn der Abschlussvermerk genau eine der vier Abschlusskategorien mit Begründung nennt. Es ist fertig, wenn jede Restfrist mit Rechtsgrundlage, Ereignis, Ende aus dem Rechenvermerk, Handlung und Verantwortlichem geführt ist und im Kalender steht. Es ist fertig, wenn der Abschlussbrief Ergebnis, Restfristen, Kostenstand, Umgang mit Originalen und Aufbewahrungshinweis in Sie-Form enthält und keine interne Prüfnotiz. Es ist fertig, wenn Fremdgeld je Betrag mit Herkunft, Empfangsberechtigtem und Status ausgewiesen ist und keine unbegründete Verrechnung enthält. Es ist fertig, wenn das Handaktenregister Originale, elektronische Dokumente, bereits Übergebenes und begründete Einschränkungen nennt. Es ist fertig, wenn der Aufbewahrungsvermerk je Dokumentart Norm, Beginn, Dauer und Löschsperre angibt. Es ist fertig, wenn jede vorbereitete Maßnahme als Entwurf oder noch auszuführen gekennzeichnet ist.

## 6. Beispiele

### 6.1. Abschlussbrief nach Vergleich mit Raten

Sachverhalt: In Sachen Meierhofer gegen Lindqvist Bau GmbH wurde am 25.09.2026 (Freitag) ein gerichtlicher Vergleich über 18.000 Euro in sechs Monatsraten geschlossen; die Widerrufsfrist lief am 30.09.2026 (Mittwoch) ab, die erste Rate ging am 01.10.2026 (Donnerstag) ein. Die Kanzlei überwacht die Raten; eine Originalbürgschaft liegt in der Akte. Der Brief lautet:

> Sehr geehrte Frau Meierhofer,
>
> in dem Mandat Meierhofer gegen Lindqvist Bau GmbH ist der am 25.09.2026 geschlossene Vergleich seit Ablauf der Widerrufsfrist am 30.09.2026 wirksam. Die Gegenseite zahlt 18.000 Euro in sechs Raten zu je 3.000 Euro, jeweils zum Ersten eines Monats, beginnend mit dem 01.10.2026 und endend mit dem 01.03.2027. Die erste Rate ist am 01.10.2026 eingegangen. Der Vergleich ist ein Vollstreckungstitel; bleibt eine Rate länger als zehn Tage aus, wird nach Ziffer 3 des Vergleichs der gesamte Restbetrag sofort fällig.
>
> Die Vergleichsverhandlungen sind damit abgeschlossen. Die vereinbarte Überwachung der weiteren Raten führen wir bis zum Eingang der letzten Rate fort. Bleibt eine Rate aus, prüfen wir die Gesamtfälligkeit und stimmen die Vollstreckung mit Ihnen ab; ohne Ihre Entscheidung leiten wir keine Vollstreckung ein.
>
> Die Originalbürgschaftsurkunde der Sparkasse vom 12.03.2026 befindet sich in unserer Akte. Wir geben sie Ihnen gegen Empfangsbestätigung zurück oder verwahren sie bis zur vollständigen Zahlung; bitte teilen Sie uns bis zum 21.10.2026 mit, welche Lösung Sie wünschen.
>
> Unsere Vergütung richtet sich nach der Vergütungsvereinbarung vom 15.01.2026. Die Schlussrechnung übersenden wir nach Eingang der letzten Rate, da die Ratenüberwachung zum vereinbarten Umfang gehört. Der gezahlte Vorschuss von 2.500 Euro wird angerechnet.
>
> Nach Abschluss der Überwachung bewahren wir die Handakte entsprechend unserer berufsrechtlichen Pflicht sechs Jahre ab Ende des Jahres der Beendigung auf. Von Ihnen überlassene Originale erhalten Sie zurück.
>
> Mit freundlichen Grüßen
>
> [Name], Rechtsanwältin

Der interne Vermerk ordnet das Mandat als „in Teilphase abgeschlossen“ ein, führt die Raten bis 01.03.2027 als Kalendereinträge mit Vertretung und sperrt die Archivierung bis zum Ende der Überwachung.

### 6.2. Aufbewahrungs- und Löschvermerk nach Dokumentarten

Sachverhalt: Ein Nachfolgemandat mit GwG-Pflichten endete am 30.09.2026 (Mittwoch); die Schlussrechnung wurde am 05.10.2026 (Montag) ausgegeben. Der Vermerk lautet:

> Aufbewahrungs- und Löschvermerk, erstellt am 07.10.2026, Mandat Nachfolge Ebersberger KG.
>
> Der Auftrag endete am 30.09.2026 mit Übergabe des unterzeichneten Übertragungsvertrags; eine Umsetzungsbegleitung war nicht beauftragt. Maßgebliches Beendigungsjahr ist 2026.
>
> Die Handakte einschließlich der elektronischen Akte, der Korrespondenz, der Entwürfe und der Vermerke wird nach § 50 Absatz 1 BRAO bis zum 31.12.2032 aufbewahrt. Sie wird am 14.10.2026 in das eingeschränkt zugängliche Archiv überführt; der Zugriff ist auf die verantwortliche Anwältin und die Archivverwaltung beschränkt.
>
> Die Ausgangsrechnung vom 05.10.2026 und die Auslagenbelege sind Buchungsbelege nach § 147 AO und werden acht Jahre ab Ende des Jahres der Entstehung aufbewahrt, also bis zum 31.12.2034; die Frist verlängert sich, solange die Festsetzungsfrist der betroffenen Steuern nicht abgelaufen ist.
>
> Die Identifizierungsunterlagen der Komplementärin, die Angaben zum wirtschaftlich Berechtigten und die Transaktionsaufzeichnung unterliegen § 8 GwG. Sie werden fünf Jahre nach dem 30.09.2026 aufbewahrt und danach unverzüglich vernichtet, soweit bis dahin keine andere gesetzliche Pflicht entgegensteht; Wiedervorlage zum 01.10.2031.
>
> Die Originalurkunden der Mandantin wurden am 30.09.2026 gegen Empfangsbestätigung zurückgegeben; es verbleiben keine Originale.
>
> Haftungsanzeichen bestehen nicht. Die Arbeitskopien im Datenraum und die Ausgaben des KI-Werkzeugs werden nach Prüfung am 14.10.2026 gelöscht; die Löschung der Anbieter-Backups ist angefragt und bis zur Bestätigung als offen geführt. Löschungen sind vorbereitet, nicht ausgeführt.
>
> [Name], Rechtsanwältin

### 6.3. Negativbeispiel: Akte sechs Jahre pauschal gelöscht trotz laufender Haftungsfrage

Falsche Ausgabe: „Das Mandat endete 2019. Die sechsjährige Aufbewahrungsfrist nach § 50 BRAO ist am 31.12.2025 abgelaufen. Die gesamte Akte einschließlich Rechnungen, GwG-Unterlagen und Backups wurde am 15.01.2026 vollständig gelöscht. Die am 12.03.2026 eingegangene Haftungsanfrage des früheren Mandanten kann mangels Unterlagen nicht mehr beantwortet werden.“

Warum falsch: Die Handaktenfrist ist nur eine von mehreren Fristen. Die Rechnungen unterlagen als Buchungsbelege § 147 AO mit noch laufender Frist; die GwG-Aufzeichnungen folgen § 8 GwG mit eigenem Beginn. Vor allem war die Haftungsfrage vor der Löschung erkennbar, weil der Mandant im Dezember 2025 Rügen erhoben hatte; die Aufbewahrung zur Verteidigung von Rechtsansprüchen nach Artikel 17 Absatz 3 DSGVO und die laufende Verjährung nach §§ 195, 199 BGB verlangten eine Löschsperre. Die behauptete Backup-Löschung war nicht belegt. Die Löschung hat Verteidigung und Versicherungsanzeige erschwert.

Korrigierte Fassung: „Das Mandat endete am 30.11.2019; die Handaktenfrist nach § 50 Absatz 1 BRAO lief am 31.12.2025 ab. Die Ausgangsrechnungen bleiben als Buchungsbelege nach § 147 AO, die GwG-Aufzeichnungen nach § 8 GwG bis zum Ablauf ihrer jeweiligen Frist erhalten. Wegen der am 10.12.2025 erhobenen Rügen des Mandanten besteht eine Löschsperre für die gesamte Handakte bis zur Klärung der Haftungsfrage, längstens bis zum Ablauf der Verjährung; die Berufshaftpflichtversicherung wurde am 15.12.2025 informiert. Die Löschsperre ist mit Grund, Datum und Verantwortlicher im Archivsystem dokumentiert.“

### 6.4. Urteil ohne Rechtsmittelentscheidung

Ein klageabweisendes Urteil wurde am 02.10.2026 (Freitag) zugestellt; der Mandant bittet am 07.10.2026 um die Schlussrechnung. Daraus wird kein Rechtsmittelverzicht abgeleitet. Der Skill übergibt Zustellungsdatum und Verfahrensart an den Fristenskill, erstellt eine Entscheidungsvorlage mit Rechtsmittel, Fristende, Kosten und Erfolgsaussicht mit Antwortfrist zum 21.10.2026 (Mittwoch). Die Schlussrechnung für die Instanz wird vorbereitet; der Vermerk führt die Rechtsmittelfrist als Restpflicht. Will die Kanzlei das Rechtsmittel nicht übernehmen, erklärt sie dies im selben Brief.

### 6.5. Offene Gebühren und Aktenwechsel

Eine neue Kanzlei fordert am 07.10.2026 wegen einer am 16.11.2026 (Montag) ablaufenden Berufungsbegründungsfrist die Unterlagen; die bisherige Kanzlei hat eine bestrittene Honorarforderung von 1.800 Euro. Der Skill prüft § 50 Absatz 3 BRAO und § 17 BORA, bestimmt die fristrelevanten Dokumente (Urteil mit Zustellungsnachweis, Schriftsätze, Beweisangebote, Protokolle) und bereitet deren Übergabe als Kopie oder zu treuen Händen mit Register vor. Die Honorarforderung geht getrennt an den Abrechnungsskill. „Keine Akte vor Zahlung“ wird nicht erklärt; die eigene Fristkontrolle endet erst mit der schriftlichen Übernahmebestätigung.

### 6.6. Mandant verlangt sofortige Komplettlöschung

Der Mandant verlangt nach Zahlung die Vernichtung aller Daten. Der Skill antwortet nach Kategorien: Arbeitskopien, Freigabelinks und KI-Ausgaben werden nach Prüfung gelöscht; die Handakte bleibt sechs Jahre, die Rechnungen acht Jahre, etwaige GwG-Aufzeichnungen fünf Jahre im eingeschränkt zugänglichen Archiv, jeweils mit Norm und Ende der Speicherung im Brief. Pauschale Ablehnung und pauschale Zusage werden vermieden. Eine erfolgreiche Vertragsklausel geht erst nach Prüfung von Wiedererkennbarkeit, Geschäftsgeheimnissen und Rechtsstand als bereinigte Vorlage in die Wissenssammlung.
