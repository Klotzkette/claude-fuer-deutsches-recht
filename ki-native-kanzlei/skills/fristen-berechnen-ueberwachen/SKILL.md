---
name: fristen-berechnen-ueberwachen
description: "Verwenden, wenn Urteil, Beschluss, Bescheid, Strafbefehl, Kündigung oder Vertrag eine Rechtsmittel-, Begründungs-, Ausschluss-, Kündigungs- oder Verjährungsfrist auslöst oder eine Frist geändert, verlängert oder versäumt wurde. Liefert Rechenvermerk mit Norm, Beleg, Ende, Verschiebung, Kontrolle und Wiedervorlage. Nicht für Aktenanlage oder Schriftsatz."
---

# Fristen berechnen und überwachen

## 1. Zweck und Anwendungsfall

### 1.1. Ergebnis und Grenzen

Dieser Skill berechnet und überwacht Prozess-, Rechtsbehelfs-, materiellrechtliche, Verjährungs-, Ausschluss- und Vorfristen. Er liefert Rechenvermerk, Fristenübersicht oder einen ausformulierten fristwahrenden Entwurf.

Trenne Rechtsregel, Ereignisnachweis, Rechnung und wirksame Handlung. Ein Versandstatus beweist weder richtige Datei noch rechtzeitigen Eingang.

Asyl-, Aufenthalts-, Vergabe-, Insolvenz-, Wahl- und Registerrecht enthalten besondere Auslöser, die aus der konkreten Norm zu ergänzen sind. Externe Einreichung, Rechtsmittelerklärung, Verzicht, Rücknahme, Kündigung und Widerruf erfolgen nur im bestehenden Auftrag.

### 1.2. Auslöser, Abgrenzung und Nachbarskills

Starte bei fristauslösenden Urteilen, Beschlüssen, Bescheiden, Kündigungen und Verträgen, bei geändertem Zustellnachweis, Verjährungsverzicht, beendeten Verhandlungen, beantragter Verlängerung, Softwareänderungen oder möglicher Versäumung.

[Akte und Fristen anlegen](../akte-fristen-anlegen/SKILL.md) erhält das berechnete Fristobjekt mit Rechenvermerk; [Schriftsätze entwerfen](../schriftsaetze-entwerfen/SKILL.md) erhält Rechtsbehelf sowie Prüf- und Einreichungszeitpunkt. [beA-Anlagen vorbereiten](../bea-anlagen-vorbereiten/SKILL.md) übernimmt Datei- und Versandvorbereitung. Dieser Skill signiert und versendet nichts und legt keinen Rechtsbehelf ein. Ein Kalendereintrag setzt bestätigten Schreibzugriff voraus; dessen Status benötigt Rücklesung und verantwortliche Person.

## 2. Eingaben

### 2.1. Mindestdaten der Fristakte

Lies zunächst Entscheidung, Verfügung, Vertrag, Zustellnachweis, Empfangsbekenntnis, Nachricht und vorhandenen Kalender. Erfasse Aktenzeichen, Beteiligtenrolle, Gericht oder Behörde, Verfahrensart, Handlung, Auftrag und verantwortlichen Berufsträger. Ordne jedes Datum seiner Bedeutung zu: Unterzeichnung, Verkündung, Aufgabe zur Post, Abruf, Zustellung, Kenntnis und Weiterleitung an die Kanzlei sind verschiedene Ereignisse.

### 2.2. Entscheidende Angaben

| Angabe | Warum entscheidend | Vorgehen, wenn sie fehlt |
| --- | --- | --- |
| Vollständiges Dokument mit Rechtsbehelfsbelehrung | Bestimmt Rechtsbehelf, Dauer und Beginn; fehlerhafte Belehrung öffnet nach § 58 Abs. 2 VwGO oder § 233 Satz 2 ZPO eine andere Route | Erste Seite für Triage nutzen, Rest anfordern, Vermerk als vorläufig kennzeichnen |
| Zustell- oder Bekanntgabenachweis | Setzt die Frist in Gang; Empfangsbekenntnis, Zustellungsurkunde, Umschlag und Absendevermerk tragen verschiedene Daten | Früheste plausible Variante rechnen, Beleg anfordern, beide Rechnungen sichtbar halten |
| Verfahrensart und Instanz | Entscheidet über ZPO, ArbGG, VwGO, FGO, SGG, StPO, OWiG oder FamFG und damit über das Rechenprofil | Aus Gericht, Aktenzeichen und Belehrung ableiten; bei Zweifel beide Profile rechnen |
| Maßgeblicher Ort und Feiertagskalender | § 193 BGB und § 222 Abs. 2 ZPO verschieben nur bei Feiertagen am maßgeblichen Ort | Ort des Gerichts oder der Behörde zugrunde legen, Kalender mit Quelle belegen |
| Führendes Fristensystem und Verantwortliche | Ohne Eintragung im überwachten System besteht nur eine Berechnung | Status „berechnet, zur Eintragung übergeben“ führen, Person benennen |
| Bisherige Verlängerungen und Einwilligung des Gegners | § 520 Abs. 2 ZPO unterscheidet nach Einwilligung; § 66 Abs. 1 ArbGG erlaubt nur einmalige Verlängerung | Akte und Gerichtsschreiben lesen, bis dahin die ursprüngliche Frist führen |
| Auftragstiefe und Honorarstand | Berechnung, Entwurf, Einlegung und Verlängerungsantrag sind verschiedene Aufträge | Berechnung und Entwurf vorbereiten, externe Handlung nur nach Freigabe, Vergütung als offen führen |

### 2.3. Rückfragen in der richtigen Reihenfolge

Kläre gebündelt nur ergebnisrelevante Lücken: zuerst Zeitpunkt, Weg und Nachweis von Zustellung oder Bekanntgabe; danach Vollständigkeit einschließlich Belehrung sowie Verkündungs- oder Erlassdatum; sodann Partei, Bevollmächtigung und angezeigten Vertreterwechsel. Bestimme anschließend Auftragstiefe und Eintragungsperson; frage zuletzt nach beantragten oder bewilligten Verlängerungen und Gegnereinwilligung.

Bei ungeklärter Zustellung rechne vorläufig mit dem frühesten belegten oder behaupteten Datum. Bei unklarer Auftragstiefe werden Vermerk und zulässiger interner Entwurf vorbereitet, während die externe Handlung offenbleibt. Ohne Verlängerungsnachweis wird die ursprüngliche Frist weiter gesichert.

### 2.4. Quellen, Unsicherheit und Kalenderfähigkeit

Jeder Eingangsparameter erhält eine Belegreferenz und den Status belegt, plausible Angabe oder streitig. Bei mehreren Betroffenen ist für jede Person zu klären, wann ihr gegenüber wirksam zugestellt wurde; Ehegatten, Gesellschaft und Geschäftsführer haben nicht automatisch denselben Fristbeginn. Ermittele das führende Fristensystem, Schreibrechte und Eintragungsperson.

## 3. Ablauf und Checkliste

### 3.1. Soforttriage und Fristidentität

Bestimme zuerst, ob heute, innerhalb der nächsten zwei Arbeitstage oder nach einer möglichen Versäumung eine Handlung erforderlich ist; diese Risikoklassen sind keine gesetzlichen Fristen. Bei unklarer Zustellung rechne mehrere plausible Szenarien, ohne das ungünstigste als erwiesen auszugeben, und benenne den Beleg, der die Alternative entscheidet. Gib jeder Frist eine eigene Identität: Berufungseinlegung und Berufungsbegründung sind zwei Fristen; eine zweite Zustellung, ein Berichtigungsbeschluss oder ein neues Aktenzeichen ist nicht ohne Rechtsprüfung ein neuer Auslöser. Prüfe anschließend Rechtsbehelf, Statthaftigkeit, Beschwer, Zulassung, Vertretungszwang und zuständige Eingangsstelle.

Bei der Wertzuständigkeit gilt § 23 Nummer 1 GVG mit 10.000 Euro. Nach § 44 EGGVG bleibt für vor dem 01.01.2026 anhängige Verfahren die bisherige Wertregel maßgeblich; auch die dortigen Ausnahmen für neu zugewiesene Sachgebiete sind zu prüfen. Zuständigkeitswert und Rechtsmittelbeschwer werden getrennt bestimmt.

### 3.2. Rechenprofil statt Universalalgorithmus

Wähle die gesetzliche Verweisungskette ausdrücklich. Im Zivilprozess führt § 222 Abs. 1 ZPO zu den §§ 187 bis 193 BGB; § 222 Abs. 2 ZPO verschiebt ein Fristende an Sonntag, allgemeinem Feiertag oder Sonnabend auf den Ablauf des nächsten Werktags. § 57 Abs. 2 VwGO, § 54 Abs. 2 FGO und § 64 SGG führen in dieselbe Logik; § 16 FamFG verweist auf § 222 ZPO; §§ 42 und 43 StPO regeln eigenständig mit gleichlautender Endverschiebung in § 43 Abs. 2 StPO; § 108 Abs. 3 AO enthält dieselbe Verschiebung für das Steuerverfahren.

Dokumentiere die Art des Beginns. Bei einer Ereignisfrist nach § 187 Abs. 1 BGB wird der Ereignistag nicht mitgerechnet; knüpft der Beginn an den Tagesanfang an, zählt dieser Tag nach § 187 Abs. 2 BGB mit. Wochen-, Monats- und Jahresfristen enden nach § 188 Abs. 2 BGB bei Ereignisbeginn am korrespondierenden Wochentag oder Datum des Ereignisses, bei Tagesbeginn am Tag vor dem korrespondierenden Anfangstag; fehlt dieser Tag im Endmonat, endet die Frist nach § 188 Abs. 3 BGB mit dem letzten Tag dieses Monats. „Ein Monat“ ist weder dreißig Tage noch vier Wochen. Berechne erst das reguläre Ende, danach die Verschiebung. Bei nach Stunden bestimmten ZPO-Fristen werden nach § 222 Abs. 3 ZPO Sonntage, Feiertage und Sonnabende nicht mitgerechnet.

### 3.3. Feiertage, Endzeit und fest bestimmte Termine

Belege den gesetzlichen Feiertagskalender am rechtlich maßgeblichen Ort und für das betroffene Jahr. § 193 BGB stellt auf den am Erklärungs- oder Leistungsort staatlich anerkannten allgemeinen Feiertag ab; die Kanzleianschrift ist nicht maßgeblich, und ein Feiertag in Bayern wirkt nicht für ein Gericht in Berlin. Im Jahr 2026 fallen der Tag der Deutschen Einheit und der Reformationstag auf einen Samstag, Allerheiligen auf einen Sonntag.

Bei Kündigungen trenne den Beendigungstermin vom rechtzeitig erforderlichen Zugang. Prüfe, ob die konkrete Spezialregel eine Verschiebung zulässt; die Wochenendregel darf nicht ungeprüft auf einen rückwärts ermittelten letzten Zugangstag übertragen werden. Bei gerichtlicher Einreichung entscheidet der Eingang in der Empfangseinrichtung bis 24 Uhr des letzten Tages, nicht der Beginn des Uploads. Eine interne Versandreserve verkürzt die gesetzliche Frist nicht.

### 3.4. Zustellung und Bekanntgabe

Bei gerichtlichen Entscheidungen prüfe Zustellung an Bevollmächtigte, Empfangsbekenntnis, Zustellungsurkunde, Ersatzzustellung und Heilung. Ein elektronisches Empfangsbekenntnis muss das tatsächlich maßgebliche Empfangsdatum abbilden; es ist kein frei wählbarer Aufschub.

Bei Verwaltungsakten trenne einfache Bekanntgabe von förmlicher Zustellung. Nach § 41 Abs. 2 VwVfG gilt ein im Inland durch die Post übermittelter schriftlicher Verwaltungsakt am vierten Tag nach der Aufgabe zur Post als bekannt gegeben, ein elektronisch übermittelter am vierten Tag nach der Absendung; die Fiktion gilt nicht bei fehlendem oder späterem Zugang, den im Zweifel die Behörde nachzuweisen hat. Sie ist keine Regel „Bescheiddatum plus vier“; maßgeblich ist die belegte Aufgabe. Die Abrufbekanntgabe nach § 41 Abs. 2a VwVfG gilt am Tag nach dem Abruf als bewirkt; wird er nicht innerhalb von zehn Tagen nach Absendung der Benachrichtigung über die Bereitstellung abgerufen, wird die Bereitstellung beendet und die Bekanntgabe ist nicht bewirkt; § 37 Abs. 2 SGB X enthält dieselbe Viertagesregel.

Im Steuerrecht gilt nach § 122 Abs. 2 AO ein durch die Post übermittelter Verwaltungsakt im Inland am vierten Tag nach Aufgabe zur Post, bei Übermittlung ins Ausland einen Monat nach Aufgabe als bekannt gegeben; § 122 Abs. 2a AO regelt die elektronische Übermittlung mit derselben Viertagesregel, § 122a AO den Datenabruf. Trifft ein rechnerischer Bekanntgabetag auf ein Wochenende oder einen Feiertag, ist die Anwendbarkeit von § 108 Abs. 3 AO auf diese Bekanntgabefiktion gesondert zu klären; bis dahin bleibt das daraus abgeleitete Ende vorläufig und der frühere Termin wird vorsorglich gesichert. Bei privatrechtlichen Erklärungen prüfe den Zugang nach § 130 BGB.

### 3.5. Zivilprozess und Mahnverfahren

Die Berufungsfrist beträgt nach § 517 ZPO einen Monat; sie ist Notfrist und beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens mit Ablauf von fünf Monaten nach der Verkündung. Die Begründungsfrist beträgt nach § 520 Abs. 2 ZPO zwei Monate mit demselben Beginn und wird nicht vom Tag der Einlegung berechnet. Der Vorsitzende kann sie mit Einwilligung des Gegners verlängern, ohne Einwilligung um bis zu einen Monat, wenn der Rechtsstreit nicht verzögert wird oder erhebliche Gründe dargelegt werden.

Die Revisionsfrist beträgt nach § 548 ZPO einen Monat ab Zustellung des vollständigen Berufungsurteils, spätestens fünf Monate nach Verkündung; die Revisionsbegründungsfrist nach § 551 Abs. 2 ZPO zwei Monate mit demselben Beginn, ohne Einwilligung bei den Gründen des § 551 Abs. 2 Satz 6 ZPO um bis zu zwei Monate verlängerbar; bei nicht rechtzeitiger Akteneinsicht gilt die dortige Sonderregel bis zwei Monate nach Aktenübersendung. Die Nichtzulassungsbeschwerde nach § 544 ZPO setzt seit dem 01.01.2026 eine Beschwer von mehr als 25.000 Euro voraus, sofern das Berufungsgericht die Berufung nicht als unzulässig verworfen hat; die bisherige Grenze von 20.000 Euro gilt nach § 47 EGZPO weiter, wenn die anzufechtende Entscheidung bis einschließlich 31.12.2025 verkündet oder, falls nicht verkündet, der Geschäftsstelle übergeben wurde oder die mündliche Verhandlung bis dahin geschlossen wurde; im schriftlichen Verfahren zählt der letzte Schriftsatztermin. Sie ist binnen einer Notfrist von einem Monat ab Zustellung, spätestens sechs Monate nach Verkündung einzulegen und binnen zwei Monaten ab Zustellung, spätestens sieben Monate nach Verkündung zu begründen. Die Rechtsbeschwerde nach § 575 ZPO ist binnen einer Notfrist von einem Monat ab Zustellung einzulegen und binnen eines Monats ab Zustellung zu begründen; die sofortige Beschwerde nach § 569 Abs. 1 ZPO binnen einer Notfrist von zwei Wochen ab Zustellung, spätestens fünf Monate nach Verkündung des Beschlusses.

Der Einspruch gegen ein Versäumnisurteil unterliegt nach § 339 ZPO einer Notfrist von zwei Wochen ab Zustellung; muss im Ausland zugestellt werden, beträgt sie einen Monat, und das Gericht kann eine längere Frist bestimmen. Bei öffentlicher Zustellung bestimmt das Gericht die Einspruchsfrist (§ 339 Abs. 3 ZPO). Bei einer verjährungshemmenden Klage wirkt nach § 167 ZPO der Eingang zurück, wenn die Zustellung demnächst erfolgt; Kostenvorschuss und Zustellung erhalten deshalb eine eigene Kontrollaufgabe.

Wiedereinsetzung nach §§ 233 und 234 ZPO erfasst Notfristen, die Begründungsfristen für Berufung, Revision, Nichtzulassungsbeschwerde und Rechtsbeschwerde sowie die Wiedereinsetzungsfrist selbst; fehlendes Verschulden wird bei unterbliebener oder fehlerhafter Rechtsbehelfsbelehrung vermutet. Der Antrag ist binnen zwei Wochen ab Behebung des Hindernisses zu stellen, bei den Begründungsfristen binnen eines Monats; nach einem Jahr seit dem Ende der versäumten Frist ist Wiedereinsetzung ausgeschlossen.

### 3.6. Arbeitsgerichtliche und arbeitsrechtliche Fristen

Die Kündigungsschutzklage ist nach § 4 KSchG innerhalb von drei Wochen nach Zugang der schriftlichen Kündigung zu erheben; bei erforderlicher behördlicher Zustimmung gilt der besondere Beginn nach Satz 4; sonst gilt die Kündigung nach § 7 KSchG als von Anfang an rechtswirksam. Vergleichsverhandlungen oder eine Deckungsanfrage halten die Frist nicht auf; bei mehreren Kündigungen ist jede einzeln anzugreifen. Die nachträgliche Zulassung nach § 5 KSchG ist nur innerhalb von zwei Wochen nach Behebung des Hindernisses zulässig und nach sechs Monaten vom Ende der versäumten Frist an ausgeschlossen. Die Befristungskontrollklage ist nach § 17 TzBfG innerhalb von drei Wochen nach dem vereinbarten Ende zu erheben; bei Fortsetzung des Arbeitsverhältnisses beginnt die Frist mit Zugang der schriftlichen Beendigungserklärung des Arbeitgebers.

Ansprüche nach § 15 AGG sind nach Absatz 4 vorbehaltlich tariflicher Abweichung innerhalb von zwei Monaten schriftlich geltend zu machen, ab Zugang der Ablehnung oder sonst ab Kenntnis der Benachteiligung; die Entschädigungsklage ist nach § 61b ArbGG innerhalb von drei Monaten nach der schriftlichen Geltendmachung zu erheben. Berufung und Revision folgen §§ 66 und 74 ArbGG: ein Monat zur Einlegung, zwei Monate zur Begründung, jeweils ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung. Die Berufungsbegründungsfrist kann der Vorsitzende nach § 66 Abs. 1 ArbGG einmal auf Antrag verlängern, die Revisionsbegründungsfrist nach § 74 Abs. 1 ArbGG einmal bis zu einem weiteren Monat.

### 3.7. Verwaltungsrecht und Verwaltungsprozess

Kläre zuerst, ob ein Vorverfahren notwendig, ausgeschlossen oder landesrechtlich verändert ist. Der Widerspruch ist nach § 70 VwGO innerhalb eines Monats nach Bekanntgabe bei der Ausgangsbehörde oder fristwahrend bei der zuständigen Widerspruchsbehörde zu erheben; die Anfechtungsklage nach § 74 VwGO innerhalb eines Monats nach Zustellung des Widerspruchsbescheids, ohne Vorverfahren innerhalb eines Monats nach Bekanntgabe. Fehlende oder fehlerhafte Belehrung führt nach § 58 Abs. 2 VwGO in die Jahresfrist mit den dort genannten Ausnahmen; § 57 VwGO verweist für die Berechnung auf § 222 ZPO.

Nach § 124a VwGO ist die zugelassene Berufung innerhalb eines Monats einzulegen und innerhalb von zwei Monaten nach Zustellung des vollständigen Urteils zu begründen; ohne Zulassung ist der Zulassungsantrag innerhalb eines Monats zu stellen und innerhalb von zwei Monaten nach Zustellung zu begründen. Lässt erst das Oberverwaltungsgericht die Berufung zu, gilt die einmonatige Begründungsfrist ab Zustellung des Zulassungsbeschlusses nach § 124a Abs. 6 VwGO. Die Nichtzulassungsbeschwerde nach § 133 VwGO ist innerhalb eines Monats einzulegen und innerhalb von zwei Monaten nach Zustellung zu begründen. Die Beschwerde im Eilverfahren ist nach § 147 Abs. 1 VwGO innerhalb von zwei Wochen nach Bekanntgabe einzulegen und nach § 146 Abs. 4 VwGO innerhalb eines Monats nach Bekanntgabe beim Oberverwaltungsgericht zu begründen.

### 3.8. Finanzgerichtsbarkeit und Sozialgerichtsbarkeit

Der Einspruch ist nach § 355 Abs. 1 AO innerhalb eines Monats nach Bekanntgabe einzulegen, gegen eine Steueranmeldung innerhalb eines Monats nach deren Eingang, in Fällen des § 168 Satz 2 AO nach Bekanntwerden der Zustimmung. Wiedereinsetzung nach § 110 AO ist innerhalb eines Monats nach Wegfall des Hindernisses zu beantragen und nach einem Jahr ausgeschlossen, außer bei höherer Gewalt. Die Klage ist nach § 47 Abs. 1 FGO innerhalb eines Monats nach Bekanntgabe der Einspruchsentscheidung zu erheben. Die Revision ist nach § 120 FGO innerhalb eines Monats nach Zustellung einzulegen und innerhalb von zwei Monaten zu begründen, die Begründungsfrist auf vor Ablauf gestellten Antrag verlängerbar; die Nichtzulassungsbeschwerde nach § 116 FGO ist innerhalb eines Monats einzulegen und innerhalb von zwei Monaten zu begründen, die Begründungsfrist nur einmal um einen Monat verlängerbar.

Im Sozialrecht sind Widerspruch nach § 84 SGG und Klage nach § 87 SGG innerhalb eines Monats nach Bekanntgabe zu erheben, bei Bekanntgabe im Ausland innerhalb von drei Monaten; nach Vorverfahren beginnt die Klagefrist mit Bekanntgabe des Widerspruchsbescheids. Die Berechnung folgt § 64 SGG; Wiedereinsetzung nach § 67 SGG ist binnen eines Monats nach Wegfall des Hindernisses zu beantragen und nach einem Jahr ausgeschlossen, außer bei höherer Gewalt. Bei öffentlicher Bekanntgabe nach § 85 Abs. 4 SGG gilt eine Jahresfrist ab Ablauf von zwei Wochen seit letzter Veröffentlichung (§ 87 Abs. 1 Sätze 3 und 4 SGG). Nach § 91 SGG wahrt auch der fristgerechte Eingang bei einer anderen inländischen Behörde, einem Versicherungsträger oder einer deutschen Konsularbehörde die Klagefrist; diese Ausnahme gilt nicht in anderen Gerichtszweigen.

### 3.9. Strafprozess und Ordnungswidrigkeiten

Berufung und Revision sind nach §§ 314 und 341 StPO binnen einer Woche nach Verkündung beim Gericht des ersten Rechtszugs einzulegen; bei Verkündung in Abwesenheit beginnt sie grundsätzlich mit Zustellung; die Vertretungsausnahmen in § 314 Abs. 2 beziehungsweise § 341 Abs. 2 StPO sind gesondert zu prüfen. Die Revisionsbegründung ist nach § 345 StPO spätestens binnen eines Monats nach Ablauf der Einlegungsfrist anzubringen; die Frist verlängert sich kraft Gesetzes um einen Monat, wenn das Urteil später als einundzwanzig Wochen nach Verkündung zu den Akten gebracht wurde, und um einen weiteren Monat bei mehr als fünfunddreißig Wochen. War das Urteil bei Ablauf der Einlegungsfrist noch nicht zugestellt, beginnt die Begründungsfrist nach § 345 Abs. 1 Satz 3 StPO erst mit Zustellung, gegebenenfalls zusätzlich mit der Mitteilung des Zeitpunkts der Aktenbringung. Die sofortige Beschwerde ist nach § 311 Abs. 2 StPO binnen einer Woche ab Bekanntmachung einzulegen, der Einspruch gegen den Strafbefehl nach § 410 Abs. 1 StPO innerhalb von zwei Wochen nach Zustellung.

Die Berechnung folgt §§ 42 und 43 StPO. Wiedereinsetzung nach §§ 44 und 45 StPO ist binnen einer Woche nach Wegfall des Hindernisses zu beantragen; die versäumte Handlung ist innerhalb der Antragsfrist nachzuholen, und die Versäumung einer Rechtsmittelfrist gilt als unverschuldet, wenn die vorgeschriebene Belehrung unterblieben ist. Im Bußgeldverfahren ist der Einspruch nach § 67 OWiG innerhalb von zwei Wochen nach Zustellung bei der Verwaltungsbehörde einzulegen. Die Rechtsbeschwerde nach § 79 OWiG setzt unter anderem eine Geldbuße von mehr als 250 Euro voraus, bei geringerer Geldbuße sind zunächst die übrigen Zulässigkeitstatbestände des § 79 Abs. 1 und danach ein Zulassungsantrag nach § 80 OWiG zu prüfen; Fristen folgen über § 79 Abs. 3 OWiG der StPO.

### 3.10. FamFG und weitere freiwillige Gerichtsbarkeit

Prüfe zunächst, ob Familiensache, Ehesache, Familienstreitsache oder eine andere Angelegenheit der freiwilligen Gerichtsbarkeit vorliegt. Nach § 16 FamFG beginnt der Lauf einer Frist mit der Bekanntgabe; §§ 222, 224 Abs. 2 und 3 sowie 225 ZPO gelten entsprechend. Die Beschwerdefrist beträgt nach § 63 Abs. 1 FamFG einen Monat, nach Absatz 2 zwei Wochen gegen Endentscheidungen im Verfahren der einstweiligen Anordnung und gegen Entscheidungen über Anträge auf Genehmigung eines Rechtsgeschäfts; sie beginnt mit der schriftlichen Bekanntgabe; kann diese nicht bewirkt werden, beginnt sie spätestens fünf Monate nach Erlass. Die Beschwerde wird nach § 64 FamFG beim Ausgangsgericht eingelegt, in Ehesachen und Familienstreitsachen nicht zur Niederschrift.

In Ehesachen und Familienstreitsachen beträgt die Begründungsfrist nach § 117 Abs. 1 FamFG zwei Monate ab schriftlicher Bekanntgabe, spätestens fünf Monate nach Erlass; weder der Eingang der Beschwerde noch die Mitteilung des Beschwerdeaktenzeichens setzt eine neue Frist in Gang. Wiedereinsetzung nach §§ 17 und 18 FamFG ist grundsätzlich binnen zwei Wochen zu beantragen; für die Rechtsbeschwerdebegründung gilt ein Monat. In Ehesachen und Familienstreitsachen gilt für versäumte Begründungsfristen über § 117 Abs. 5 FamFG die Monatsfrist des § 234 Abs. 1 Satz 2 ZPO.

### 3.11. Verjährung und Hemmung

Erstelle eine Anspruchsliste. Die regelmäßige Verjährungsfrist beträgt nach § 195 BGB drei Jahre und beginnt nach § 199 Abs. 1 BGB mit dem Schluss des Jahres, in dem der Anspruch entstanden ist und der Gläubiger Kenntnis von den anspruchsbegründenden Umständen und der Person des Schuldners erlangt oder ohne grobe Fahrlässigkeit erlangen müsste; die Höchstfristen der Absätze 2 bis 4 laufen kenntnisunabhängig.

Bei Verhandlungen nach § 203 BGB tritt die Verjährung frühestens drei Monate nach dem Ende der Hemmung ein; dokumentiere Beginn, Gegenstand, Austausch und Ende, denn eine einseitige Mahnung begründet keine Verhandlungen. Für Rechtsverfolgung nach § 204 BGB ist jede Maßnahme dem Anspruch, Gegner und Tatbestand zuzuordnen; die Hemmung endet nach § 204 Abs. 2 BGB sechs Monate nach rechtskräftiger Entscheidung oder anderweitiger Beendigung, bei Stillstand sechs Monate nach der letzten Verfahrenshandlung. Nach § 212 BGB beginnt die Verjährung neu bei Anerkenntnis, etwa durch Abschlagszahlung oder Sicherheitsleistung, oder bei Vollstreckungshandlung. Ein Verjährungsverzicht ist nach Wortlaut, Dauer, Einreden und Ansprüchen auszulegen; notiere das Ende der Schonfrist und eine Vorfrist für die gerichtliche Sicherung.

### 3.12. Kündigung, Widerruf, Anfechtung und Ausschluss

Die Grundkündigungsfrist des § 622 Abs. 1 BGB beträgt vier Wochen zum Fünfzehnten oder zum Ende eines Kalendermonats; bei Kündigung durch den Arbeitgeber beträgt sie nach § 622 Abs. 2 BGB bei einem Bestand von zwei, fünf, acht, zehn, zwölf, fünfzehn und zwanzig Jahren einen bis sieben Monate zum Ende eines Kalendermonats, und während einer vereinbarten Probezeit von längstens sechs Monaten zwei Wochen (Abs. 3). Tarifliche und einzelvertragliche Abweichungen sind nach Absätzen 4 bis 6 getrennt zu prüfen. Die außerordentliche Kündigung ist nach § 626 Abs. 2 BGB nur innerhalb von zwei Wochen ab Kenntnis der kündigungsberechtigten Person von den maßgebenden Tatsachen möglich. Die Zurückweisung nach § 174 BGB muss unverzüglich erfolgen und ist ausgeschlossen, wenn der Vollmachtgeber die Bevollmächtigung mitgeteilt hatte.

Die Widerrufsfrist beträgt nach § 355 Abs. 2 BGB vierzehn Tage ab Vertragsschluss, soweit nichts anderes bestimmt ist; bei Fernabsatz- und Außergeschäftsraumverträgen erlischt das Widerrufsrecht nach § 356 Abs. 4 Satz 1 BGB spätestens zwölf Monate und vierzehn Tage nach dem maßgeblichen Zeitpunkt. Das Erlöschen bei entgeltlichen Dienstleistungen regelt § 356 Abs. 5 Nr. 2 BGB; es setzt vollständige Erbringung nach vorheriger ausdrücklicher Zustimmung und Kenntnisbestätigung voraus, bei Außergeschäftsraumverträgen die Zustimmung auf dauerhaftem Datenträger; eine Erklärung zum sofortigen Arbeitsbeginn ist noch keine vollständige Leistung.

Die Anfechtung nach § 121 BGB ist ohne schuldhaftes Zögern nach Kenntnis des Anfechtungsgrundes zu erklären und zehn Jahre nach Abgabe der Willenserklärung ausgeschlossen; bei Täuschung und Drohung gilt nach § 124 BGB die Jahresfrist ab Entdeckung der Täuschung oder Ende der Zwangslage mit derselben Zehnjahresgrenze. Vertragliche und tarifliche Ausschlussfristen werden vollständig gelesen: Ereignis, Form, Adressat, Zugang, Stufenfolge und Rechtsfolge; ein Anspruchsschreiben kann die erste Stufe wahren, ohne die Klagefrist zu erfüllen.

### 3.13. Kostenrecht und berufsbezogene Anschlussfristen

Die Erinnerung gegen den Kostenansatz nach § 66 GKG ist unbefristet. Die Beschwerde nach Absatz 2 setzt eine Beschwer über 300 Euro oder Zulassung voraus. § 72 GKG erhält das alte Recht bei vor dem 01.01.2026 anhängigen Zivilsachen, ausgenommen nach dem 31.12.2025 eingelegte Rechtsmittelverfahren. In Straf-, Bußgeld- und Strafvollzugssachen zählt die vor dem 01.01.2026 rechtskräftige Kostenentscheidung; in den dort genannten Insolvenz- und weiteren Verfahren die vorherige Kostenfälligkeit. Übergangsfall und Verfahrensart sind deshalb vor Anwendung der Grenze festzuhalten.

Die Streitwertbeschwerde nach § 68 Abs. 1 GKG verlangt ebenfalls über 300 Euro Beschwer oder Zulassung. Sie ist binnen sechs Monaten nach Rechtskraft oder anderweitiger Erledigung zulässig (§ 63 Abs. 3 Satz 2 GKG). Bei Festsetzung später als einen Monat vor Fristablauf gilt ein Monat nach Zustellung oder formloser Mitteilung; deren Vier-Tage-Fiktion und Zugangsausnahme stehen in § 68 Abs. 1. Die weitere Beschwerde nach Absatz 2 hat eine Monatsfrist. § 33 Abs. 3 RVG verlangt zwei Wochen ab Zustellung; § 56 Abs. 2 RVG verweist für die Beschwerde auf § 33 Abs. 3 bis 8, begründet aber keine entsprechende Erinnerungsfrist.

Vergütung wird nach § 8 Abs. 1 RVG bei Auftragserledigung oder Beendigung fällig, im gerichtlichen Verfahren auch bei Kostenentscheidung, Instanzende oder Ruhen über drei Monate. § 10 RVG verlangt eine mitgeteilte Berechnung in Textform. Die sechsjährige Handaktenfrist nach § 50 Abs. 1 BRAO beginnt mit Ablauf des Jahres der Auftragsbeendigung; andere Unterlagen haben eigene Aufbewahrungsregeln.

### 3.14. Unionsrecht, Ausland und EGMR

Bei unionsrechtlich bestimmten Fristen prüfe zuerst die Spezialregel, dann die Verordnung (EWG, Euratom) Nr. 1182/71. Nach deren Artikel 3 wird der Ereignistag nicht mitgerechnet; Feiertage, Sonntage und Samstage zählen mit, soweit die Frist nicht nach Arbeitstagen bestimmt ist; bei einem letzten Tag an Feiertag, Sonntag oder Samstag endet sie grundsätzlich am folgenden Arbeitstag, außer bei Stundenfristen und rückwärts berechneten Fristen nach Artikel 3 Absatz 4; eine Frist von zwei oder mehr Tagen umfasst mindestens zwei Arbeitstage.

Bei grenzüberschreitender Zustellung darf der Empfänger nach Artikel 12 der Verordnung (EU) 2020/1784 die Annahme verweigern, wenn das Schriftstück weder in einer ihm verständlichen Sprache noch in der Amtssprache des Empfangsorts abgefasst oder übersetzt ist; die Verweigerung kann bei Zustellung oder innerhalb von zwei Wochen danach schriftlich erklärt werden, worüber mit dem Formblatt zu belehren ist. Bei einer EGMR-Beschwerde sind Frist, Rechtswegerschöpfung und Form anhand der für den Fall geltenden amtlichen EMRK und Verfahrensordnung gesondert zu ermitteln. Ohne diesen Volltextabgleich wird hier kein Fristende ausgegeben; eine verantwortliche Anwältin übernimmt die sofortige Klärung und vorsorgliche Sicherung.

### 3.15. Fristenübersicht für die häufigsten Fälle

Die Tabelle beruht auf den am 08.10.2026 gelesenen Normen; die Sonderfälle der vorstehenden Abschnitte gelten mit; sie ersetzt nicht die Prüfung von Statthaftigkeit, Zustellung und Spezialrecht.

| Frist | Norm | Dauer und Beginn | Verlängerbar |
| --- | --- | --- | --- |
| Einspruch gegen Versäumnisurteil | § 339 ZPO | zwei Wochen ab Zustellung; Ausland ein Monat; öffentliche Zustellung gerichtliche Bestimmung | regulär nein; Ausland länger bestimmbar |
| Berufung Zivilsache | § 517 ZPO | ein Monat ab Zustellung des vollständigen Urteils, spätestens fünf Monate nach Verkündung | nein, Notfrist |
| Berufungsbegründung Zivilsache | § 520 Abs. 2 ZPO | zwei Monate, gleicher Beginn | ja; ohne Einwilligung bis zu ein Monat |
| Nichtzulassungs-beschwerde | § 544 ZPO | ein Monat ab Zustellung, spätestens sechs Monate nach Verkündung; Begründung zwei Monate, spätestens sieben Monate | Einlegung nein; Begründung nach § 551 Abs. 2 ZPO |
| Sofortige Beschwerde | § 569 Abs. 1 ZPO | zwei Wochen ab Zustellung, spätestens fünf Monate nach Verkündung | nein, Notfrist |
| Wiedereinsetzung Zivilprozess | § 234 ZPO | zwei Wochen ab Wegfall des Hindernisses; ein Monat bei Begründungsfristen; Ausschluss nach einem Jahr | nein |
| Widerspruch Verwaltungsakt | § 70 VwGO | ein Monat ab Bekanntgabe | nein |
| Anfechtungsklage | § 74 VwGO | ein Monat ab Zustellung des Widerspruchsbescheids, sonst ab Bekanntgabe | nein |
| Einspruch Steuerbescheid | § 355 Abs. 1 AO | ein Monat ab Bekanntgabe | nein |
| Klage Finanzgericht | § 47 Abs. 1 FGO | ein Monat ab Bekanntgabe der Einspruchsentscheidung | nein |
| Widerspruch und Klage Sozialrecht | §§ 84, 87 SGG | ein Monat ab Bekanntgabe; Ausland drei Monate; öffentliche Bekanntgabe nach § 87 Abs. 1 Sätze 3 und 4 SGG gesondert | nein |
| Berufung und Revision Strafsache | §§ 314, 341 StPO | eine Woche ab Verkündung; Abwesenheit und Vertretung nach jeweiligem Absatz 2 | nein |
| Einspruch Bußgeldbescheid | § 67 OWiG | zwei Wochen ab Zustellung | nein |
| Beschwerde FamFG | § 63 FamFG | ein Monat ab schriftlicher Bekanntgabe; zwei Wochen nach Absatz 2 | nein |
| Kündigungsschutzklage | § 4 KSchG | drei Wochen ab Zugang; Sonderbeginn § 4 Satz 4 KSchG | nein; nachträgliche Zulassung nach § 5 KSchG |

### 3.16. Kalenderhilfe und Kontrollkreislauf

Die lokale Hilfe [fristen.py](../../scripts/fristen.py) darf erst nach bewusster Wahl des Rechenprofils eingesetzt werden; lies die [Fristen-Rechenhilfe](../../references/fristen-rechenhilfe.md). Der Aufruf lautet `python3 scripts/fristen.py --data <datei.json> --out <neuer-ordner>`; ohne `--out` wird nur JSON ausgegeben, ein bestehender Zielordner wird nicht überschrieben. Die Eingabedatei enthält ein `profile` mit `mode` (`event`, `start`, `fixed` oder `hours`), `trigger`, `amount`, `unit`, `end_adjustment` und `adjustment_basis` sowie einen `calendar` mit belegter Liste `holidays`. Das Werkzeug bestimmt weder Rechtsbehelf noch streitigen Zugang, errät keine Feiertage und modelliert weder Hemmung noch Zugangsfiktion.

Prüfe den erzeugten Rechenvermerk gegen eine unabhängige Rechnung: Auslöser, erster Tag, reguläres Ende, Verschiebung, Endzeit. Die Eintragung wird mit Kalenderkennung, Datensatzkennung, Verantwortlichem, Vertretung und Rückleseprüfung dokumentiert; erst diese Rücklesung gibt Gate G2 frei. Vorfristen sind Aufgaben mit Zweck, nicht pauschal sieben Tage vor jeder Frist. Friständerungen erhalten Grund, Originalwert, neuen Wert, Bearbeiter und Kontrolle; aufgehobene Einträge bleiben erkennbar.

### 3.17. Fristverlängerung, Ausgangskontrolle und Ausfall

Bei Verlängerung prüfe gesetzliche Zulässigkeit, bisherige Verlängerungen, Einwilligung und Grund, und stelle den Antrag so rechtzeitig, dass eine Reaktion auf Ablehnung möglich bleibt. Ein Akteneinsichtsgesuch ist kein Verlängerungsantrag. Zur Erledigungskontrolle gehören signaturgerechte Fassung, richtige Anlagen, richtiges Gericht, richtige Empfangseinrichtung und gerichtliche Eingangsbestätigung.

Bei technischer Störung bleibt nach § 130d Satz 2 und 3 ZPO und § 55d Satz 3 und 4 VwGO die Übermittlung nach den allgemeinen Vorschriften zulässig, wenn die elektronische Übermittlung aus technischen Gründen vorübergehend nicht möglich ist; die Unmöglichkeit ist bei der Ersatzeinreichung oder unverzüglich danach glaubhaft zu machen, auf Anforderung ist ein elektronisches Dokument nachzureichen. Sichere Fehlermeldung, Zeitpunkt, Komponente und Versuche; „beA gestört“ genügt nicht.

### 3.18. Mögliche Versäumung und Wiederherstellung

Bestimme zuerst, ob die Frist tatsächlich verstrichen ist; prüfe Zustellung, Belehrung, Rechtsmittelart und gesetzliche Ausnahme. Ist eine Versäumung möglich, lege sofort die Antragsfrist des anwendbaren Rechts an: grundsätzlich zwei Wochen nach § 234 ZPO und § 18 FamFG, für die jeweils erfassten Begründungsfristen einen Monat, ein Monat nach § 110 AO und § 67 SGG, eine Woche nach § 45 StPO, zwei Wochen nach § 5 KSchG; zwei Wochen nach § 60 Abs. 2 VwGO und § 56 Abs. 2 FGO, jeweils ein Monat bei versäumten Begründungsfristen (VwGO: Berufung, Antrag auf Zulassung der Berufung, Revision, Nichtzulassungsbeschwerde, Beschwerde; FGO: Revision, Nichtzulassungsbeschwerde).

Der Entwurf enthält Chronologie, versäumte Handlung, zulässigen Antrag, tatsächliche Entlastungsumstände und Mittel der Glaubhaftmachung. Beschreibe Organisation und Kontrollablauf nur, soweit sie bestanden; erfundene Kanzleiregeln und rückdatierte Notizen sind unzulässig. Hole die Prozesshandlung innerhalb der Antragsfrist nach, soweit beauftragt. Prüfe unabhängig davon Haftungsinformation und Versicherungsanzeige.

### 3.19. Agentischer Lauf und Freigabestufe

Dieser Skill verantwortet die Phase `frist` des [Mandatslaufs](../../references/mandatslauf-und-freigaben.md). Sie läuft meist als Nebenlauf neben der Sacharbeit und endet mit dem Rechenvermerk im Status „berechnet, zur Eintragung übergeben“. Auf Freigabestufe 0 liefert der Skill Rechenvermerk, Fristobjekt und Mandatslaufstand als Text und schreibt keine Datei. Auf Stufe 1 legt er den Rechenvermerk unter `01_Bearbeitung` ab, führt das Dokumentregister und kopiert Empfangsbekenntnis oder Zustellungsurkunde unverändert. Auf Stufe 2 erfasst er das Fristobjekt mit Vorfristen, lässt die Rechenhilfe mit `--out` laufen, trägt den Rechenvermerk als Produkt ein, setzt den Nebenlauf `frist`, öffnet Gate G2 und bucht die bestätigten Minuten der Berechnung im Journal. Auf Stufe 3 erstellt er zusätzlich den Übergabevermerk, bereitet den Entwurf eines Verlängerungs- oder Wiedereinsetzungsantrags für die Versandvorbereitung vor und stößt die Nachbarskills ohne Rückfrage an. Ohne dokumentierte Rücklesung und menschliche Bestätigung kennzeichnet er keinen Kalendereintrag als eingetragen; er gibt G2 nicht selbst frei. Rechtsmitteleinlegung, Antragseinreichung und Versand erfordern die entsprechende Freigabe; erledigt ist eine Einreichungsfrist erst nach geprüfter gerichtlicher Eingangsbestätigung.

Der Skill öffnet Gate G2 Fristeintrag mit dem Rechenvermerk als Bezug. Frei gibt eine namentlich bezeichnete Person, in der Regel die fristverantwortliche Berufsträgerin, nachdem sie den Eintrag im führenden Kalender zurückgelesen hat; danach trägt der Skill Kalender- und Datensatzkennung, Rücklesedatum, Verantwortliche und Vertretung in das Fristobjekt nach und setzt es auf „eingetragen“. Ändert ein später eingehender Zustellnachweis die Rechnung, erhält der Rechenvermerk eine neue Fassung, und G2 wird mit `--aktion zuruecksetzen` erneut geöffnet.

Im Produktregister steht der Rechenvermerk je Fristobjekt, etwa als `rechenvermerk-F-0002`, zunächst als `entwurf`, nach dokumentierter unabhängiger Gegenrechnung als `geprueft` und erst mit der Freigabe von G2 als `freigegeben`. Nach dem Öffnen von G2 stößt der Skill [Akte und Fristen anlegen](../akte-fristen-anlegen/SKILL.md) für die Eintragung an; `next` priorisiert G2 mit zuständiger Person und betroffenem Produkt; unabhängige interne Sacharbeit läuft weiter. Beispiel auf Stufe 2 mit [mandatslauf.py](../../scripts/mandatslauf.py):

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/M-26-104" --phase frist --nebenlauf --grund "Urteil des Landgerichts zugestellt, Berufungsfristen"
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/M-26-104" --id rechenvermerk-F-0002 --pfad "01_Bearbeitung/Fristen/Rechenvermerk_F-0002_v01.md" --skill fristen-berechnen-ueberwachen --zustand entwurf
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-26-104" --gate G2 --aktion oeffnen --person "[zuständige Rechtsanwältin oder zuständiger Rechtsanwalt]" --bezug rechenvermerk-F-0002
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/M-26-104"
```

Die Freigabe trägt die Person mit `--aktion freigeben --person "RAin Dr. Lenz" --bezug "Rechenvermerk_F-0002_v01.md"` ein; Rollenbezeichnungen wie „System“ weist der Helfer ab. Stoppregel: Der Skill bleibt stehen, solange G2 offen ist und die nächste Handlung die Frist als gesichert voraussetzen würde, und vor der Mandantenentscheidung über die Einlegung des Rechtsmittels; ein streitiger Zustellbeleg hält ihn nicht an, weil er beide Varianten rechnet.

### 3.20. Typische Fehler und Gegenkontrolle

| Fehler | Woran erkennbar | Gegenkontrolle |
| --- | --- | --- |
| Begründungsfrist ab Einlegung gerechnet | Begründungsende liegt zwei Monate nach dem Einlegungsschriftsatz | Beginn ist die Zustellung des vollständigen Urteils (§ 520 Abs. 2 ZPO, § 66 ArbGG, § 117 FamFG) |
| Briefdatum als Zustellung | Vermerk nennt nur „Schreiben vom“, kein Zustellnachweis | Empfangsbekenntnis, Zustellungsurkunde oder Absendevermerk anfordern, Ereignisart benennen |
| Wochenendverschiebung auf Kündigungstermin | Kündigungstermin „verschoben auf Montag“ | Rückwärts vom Beendigungstermin rechnen; § 193 BGB gilt nur für Erklärungen innerhalb einer Frist |
| Viertagesfiktion trotz förmlicher Zustellung | Bescheid mit Zustellungsurkunde, Vermerk rechnet „plus vier Tage“ | Bei Zustellung gilt der Zustelltag; § 41 Abs. 2 VwVfG nur bei einfacher Postübermittlung |
| Verlängerungsantrag als Bewilligung behandelt | Kalender zeigt nur das verlängerte Datum | Ursprüngliche Frist bis zum geprüften Beschluss sichtbar halten |
| Signaturprotokoll als Eingang gewertet | Erledigungsvermerk ohne gerichtliche Eingangsbestätigung | Automatisierte Eingangsbestätigung prüfen (BVerwG 5 B 8.25) |
| Verhandlungen als Hemmung der KSchG-Frist | Klagefrist läuft, Akte vermerkt „Gespräche laufen“ | § 4 KSchG kennt keine Verhandlungshemmung; Klageentscheidung vor Ablauf einholen |
| AGG-Stufen zusammengezogen | Nur eine „AGG-Frist“ im Kalender | Zwei Monate nach § 15 Abs. 4 AGG und drei Monate nach § 61b ArbGG getrennt führen |
| Alte Frist bei Änderung überschrieben | Änderungsverlauf nicht erkennbar | Originalwert, neuen Wert, Grund und Prüfer dokumentieren (BGH XII ZB 338/24) |
| ZPO-Wiedereinsetzungsfrist im Strafverfahren | Antrag nach zwei Wochen geplant | § 45 StPO verlangt eine Woche mit Nachholung innerhalb der Antragsfrist |

### 3.21. Übergabe an Nachbarskills

Jede Übergabe enthält führende Fassung mit Pfad und Hash, Friststatus, Honorar- und Zeitstand sowie offene Gates, Personen und Fragen. [Akte und Fristen anlegen](../akte-fristen-anlegen/SKILL.md) erhält das berechnete Fristobjekt mit Norm, Auslöser, Beleg, regulärem Ende, Verschiebung, Endzeit, Vorfristen und Zuständigkeit; zurück kommen Eintrag, Kalenderkennung und Rücklesebeleg für die persönliche G2-Freigabe. [Schriftsätze entwerfen](../schriftsaetze-entwerfen/SKILL.md) erhält Rechtsbehelf, Gericht, Form, internen Prüfzeitpunkt und gesetzliches Ende und liefert den Schriftsatz. [beA-Anlagen vorbereiten](../bea-anlagen-vorbereiten/SKILL.md) erhält Frist, Paket und Empfänger; Versandmanifest und Eingangsbestätigung werden hier gegen Datei, Empfänger und Zeit geprüft. [Mandantenkommunikation](../mandantenkommunikation/SKILL.md) erhält die Fristinformation mit offenen Fragen und liefert die Mandantenentscheidung. [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md) erhält bei Versäumungsverdacht Chronologie und Belege und liefert die Haftungsbewertung. [Zeiten erfassen](../zeiten-erfassen/SKILL.md) übernimmt den Zeitstand; [Mandat abschließen](../mandat-abschliessen/SKILL.md) erhält Aufbewahrung und offene Fristen.

### 3.22. Honorar- und Zeitanschluss

Übernimm den bestätigten Honorarstand nach der [Arbeitsweise](../../references/arbeitsweise.md). Bei neuem Auftrag oder neuer Instanz kläre RVG, Stundenhonorar, Festpreis, Preiszusage oder Schätzung mit oder ohne Deckel, Umfang und Netto- oder Bruttobezug; Nach geleisteter Arbeit ergänze Datum, Person, wirkliche Dauer und Narrativ; keine hypothetisch eingesparte KI-Zeit, keine stille Erhöhung eines Deckels. Ein Fristenvermerk ist keine Rechnung.

## 4. Quellenpflicht

### 4.1. Normen und Prüfstand

Arbeitsstand ist der 8. Oktober 2026; maßgeblich bleibt der auf den Fall anwendbare Normstand einschließlich Übergangsrecht. Nutze die [Rechtsquellen](../../references/rechtsquellen.md) und die verbindliche [Zitierweise](../../references/zitierweise.md). Verlinke im Rechenvermerk Fristnorm, Berechnungsvorschrift und Zustellungsregel mit Absatz. Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht verwendet.

Tragende amtliche Normlinks: [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html), [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html), [§ 517 ZPO](https://www.gesetze-im-internet.de/zpo/__517.html), [§ 520 ZPO](https://www.gesetze-im-internet.de/zpo/__520.html), [§ 544 ZPO](https://www.gesetze-im-internet.de/zpo/__544.html), [§ 234 ZPO](https://www.gesetze-im-internet.de/zpo/__234.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 41 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__41.html), [§ 122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html), [§ 47 FGO](https://www.gesetze-im-internet.de/fgo/__47.html), [§ 87 SGG](https://www.gesetze-im-internet.de/sgg/__87.html), [§ 67 OWiG](https://www.gesetze-im-internet.de/owig_1968/__67.html), [§ 63 FamFG](https://www.gesetze-im-internet.de/famfg/__63.html), [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html), [§ 66 ArbGG](https://www.gesetze-im-internet.de/arbgg/__66.html), [§ 50 BRAO](https://www.gesetze-im-internet.de/brao/__50.html), [Verordnung (EWG, Euratom) Nr. 1182/71](https://eur-lex.europa.eu/eli/reg/1971/1182/oj/deu) und [Verordnung (EU) 2020/1784](https://eur-lex.europa.eu/eli/reg/2020/1784/oj/deu).

### 4.2. Verifizierte Entscheidungsanker

BGH, Beschl. v. 04.03.2026 – Az. XII ZB 338/24, Rn. 10–17, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2024/XII_ZB_338-24.pdf?__blob=publicationFile&v=1). Trägt: Auch geänderte und gestrichene Fristen müssen in der elektronischen Fristenorganisation erkennbar und überprüfbar bleiben; die Auswahl und Einrichtung der Software ist daran auszurichten, und die Wahl eines ungeeigneten Systems kann ein eigenes Organisationsverschulden begründen. Trägt nicht: Ein Verbot elektronischer Kalender, eine Aussage zu den Fristrechenregeln anderer Verfahrensordnungen oder die Entscheidung jedes Wiedereinsetzungsfalls; der Fall betrifft eine familienrechtliche Beschwerdebegründung.

BAG, Urt. v. 20.02.2025 – Az. 6 AZR 155/23, Rn. 22–23, [amtlicher Volltext](https://www.bundesarbeitsgericht.de/entscheidung/6-azr-155-23/). Trägt: Bei Vorlage zur fristgebundenen Handlung ist eigenverantwortliche Prüfung erforderlich; ohne erkennbare Zweifel kann die Kontrolle der Handaktenvermerke genügen. Trägt nicht: Eine Pflicht, jeden Kalendereintrag persönlich nachzutragen, oder eine Befreiung von ordnungsgemäßer Kanzleiorganisation.

BVerwG, Beschl. v. 16.05.2025 – Az. 5 B 8.25, Rn. 3–5, [amtlicher Volltext](https://www.bverwg.de/160525B5B8.25.0). Trägt: Die automatisierte Eingangsbestätigung nach § 55a Abs. 5 Satz 2 VwGO gehört zur anwaltlichen Übermittlungskontrolle; ein Signaturprotokoll bestätigt keinen gerichtlichen Eingang. Trägt nicht: Eine Aussage zu anderen Verfahrensordnungen ohne Prüfung der dort einschlägigen Einreichungsnorm.

BGH, Beschl. v. 09.02.2022 – Az. XII ZB 474/21, Rn. 9–13, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2021/XII_ZB_474-21.pdf?__blob=publicationFile&v=1). Trägt: Ein unbeschiedenes Akteneinsichtsgesuch ersetzt keinen ordnungsgemäßen Fristverlängerungsantrag. Trägt nicht: Einen allgemeinen Satz, dass jede gesetzliche Frist verlängerbar wäre; die Entscheidung betrifft die Beschwerdebegründung nach § 117 FamFG.

### 4.3. Belegdisziplin

Zitiere nur tatsächlich geprüfte Randnummern. Ergänze eine Entscheidung nur, wenn der amtliche Volltext abgerufen wurde, und benenne die Gegenposition. Keine Präjudizienbindung behaupten, keine „ständige Rechtsprechung“ ohne Quelle und kein „2026 bestätigt“, nur weil eine ältere Entscheidung 2026 abgerufen wurde. Ohne tragenden Volltext wird kein Ergebnis behauptet; benenne stattdessen die konkrete Recherchefrage und den für ihre Klärung verantwortlichen Berufsträger.

## 5. Ausgabeformat

### 5.1. Rechenvermerk

Der Vermerk benennt Mandat, Handlung, Rechtsgrundlage, belegtes Ereignis, Beginnart, Dauer, reguläres Ende, Verschiebung, maßgeblichen Ort, Kalenderquelle, Endzeit, Verantwortlichen und offene Tatsachen; die Subsumtion steht in vollständigen Sätzen. Eine Fristenliste ergänzt die Begründung streitiger Auslöser. Das Endprodukt wird vollständig ausformuliert; Satzskelette, Halbsätze und reine Aufzählungsgerüste sind als Vermerk, Antrag oder Mandantenbrief unzulässig.

### 5.2. Entscheidung und nächster Schritt

Benenne Prüfzeitpunkt, gesetzliches Ende und verantwortliche Person. Ohne bestätigte Eintragung lautet der Status „berechnet, zur Eintragung übergeben“.

### 5.3. Formatstandard und Exporthinweis

Verwende soweit technisch möglich Times New Roman, 11 pt, und dezimale Gliederung. Bei Markdown oder Chat steht der Exporthinweis außerhalb des Empfängertextes. Technische Hinweise, Systemrechte und Prüfprotokolle bleiben intern; nicht erzeugte Dateien oder Formatierungen werden nicht behauptet.

### 5.4. Abnahmekriterien

Das Produkt ist fertig, wenn jede Frist Kennung, Norm mit Absatz, belegten Auslöser und Beginnart trägt und reguläres Ende, Verschiebung sowie Endzeit unabhängig gegengerechnet sind. Der Status unterscheidet berechnete Übergabe und bestätigten Eintrag mit verantwortlicher Person. Der Mandantenbrief nennt Ergebnis, Entscheidungsbedarf und Zeitpunkt in vollständigen Sätzen, eine unbestätigte Frist ausdrücklich vorläufig. Tragende Normaussagen sind belegt; Recherchefragen enthalten kein vorweggenommenes Ergebnis. Honorar- und Zeitstand sind übernommen oder offen bezeichnet. Führende Fassung, Pfad und Hash stehen im Mandatslauf beziehungsweise bei fehlendem Dateizugriff im Übergabevermerk. Kein Gate, insbesondere G2, wird stillschweigend freigegeben.

## 6. Beispiele

### 6.1. Monatsfrist mit fehlendem Kalendertag und Feiertag am Fristende

Ein fristauslösendes Ereignis fällt auf Samstag, den 31.01.2026. Bei einer Ereignisfrist von einem Monat wird der 31. Januar nach § 187 Abs. 1 BGB nicht mitgerechnet; der Februar hat keinen 31. Tag, sodass das reguläre Ende nach § 188 Abs. 3 BGB auf Samstag, den 28.02.2026 fällt. Unter einem Profil mit § 222 Abs. 2 ZPO ergibt sich Montag, der 02.03.2026; ohne die rechtlich begründete Verschiebungsregel bleibt es beim 28.02.2026.

### 6.2. Berufung nach elektronischem Empfangsbekenntnis: vollständiger Rechenvermerk

Das Landgericht hat das Urteil am Donnerstag, dem 10.09.2026, verkündet; die Kanzlei hat das elektronische Empfangsbekenntnis für Donnerstag, den 24.09.2026, abgegeben. Der Vermerk lautet:

> Rechenvermerk Fristen, Mandat [Aktenzeichen], Berufung gegen das Urteil des Landgerichts [Ort] vom 10.09.2026, Az. [Aktenzeichen]. Das vollständig abgefasste Urteil wurde unserer Kanzlei als Prozessbevollmächtigter am 24.09.2026 zugestellt; Beleg ist das elektronische Empfangsbekenntnis mit diesem Datum und die beA-Nachricht mit Prüfprotokoll. Die Berufungsfrist beträgt nach § 517 ZPO einen Monat und beginnt mit der Zustellung; die Fünfmonatsgrenze ab Verkündung ist nicht erreicht. Der Zustelltag wird nach § 222 Abs. 1 ZPO, § 187 Abs. 1 BGB nicht mitgerechnet; das reguläre Ende ist nach § 188 Abs. 2 BGB Samstag, der 24.10.2026. Nach § 222 Abs. 2 ZPO endet die Frist mit Ablauf des nächsten Werktags, Montag, 26.10.2026, 24 Uhr. Die Berufungsbegründungsfrist beträgt nach § 520 Abs. 2 ZPO zwei Monate ab derselben Zustellung und endet Dienstag, 24.11.2026, 24 Uhr; eine Verschiebung ist nicht veranlasst. Eine Verlängerung ohne Einwilligung des Gegners ist um bis zu einen Monat möglich und muss vor Fristablauf beantragt werden. Vorfristen: Mandantenentscheidung über die Berufung bis 14.10.2026, Entwurf der Berufungsschrift zur Prüfung bis 19.10.2026, Entwurf der Begründung bis 13.11.2026. Verantwortlich ist Rechtsanwältin [Name], Vertretung Rechtsanwalt [Name]. Status: berechnet, zur Eintragung in das führende Fristensystem übergeben; die Eintragung ist noch nicht bestätigt.

Auf Stufe 2 registriert der Skill `rechenvermerk-F-0002`, setzt den Nebenlauf `frist` und öffnet G2 mit dieser Produktkennung und Rechtsanwältin [Name] als Zuständiger. Die Aktenführung übernimmt die Eintragung; erst nach persönlicher Rücklesebestätigung lautet der Status „eingetragen“. Der interne Berufungsentwurf läuft weiter; die Berufungsentscheidung der Mandantin bleibt offen.

### 6.3. Zwei unterschiedliche Zustellungsangaben

Der Mandant behauptet Zugang am Montag, dem 05.10.2026; die Zustellungsurkunde nennt Freitag, den 02.10.2026. Der interne Vermerk lautet: „Für die Sofortbearbeitung legen wir vorsorglich den 2. Oktober zugrunde; die Monatsfrist endet danach am Montag, 02.11.2026. Die Aussage zum späteren Zugang wird anhand der Zustellungsart und der Empfangssituation geprüft. Die frühere Rechnung bleibt bis zur abschließenden Entscheidung im Kalender sichtbar.“

### 6.4. Kündigungsschutz: Mandantenbrief zur Frist

Eine schriftliche Kündigung geht der Mandantin am Mittwoch, dem 07.10.2026, zu; die Dreiwochenfrist des § 4 KSchG endet am Mittwoch, 28.10.2026. Der Brief lautet:

> Sehr geehrte Frau [Name], in dem Mandat Kündigung durch die [Arbeitgeberin] vom 06.10.2026 teilen wir Ihnen den aktuellen Sachstand mit. Die Kündigung ist Ihnen nach Ihren Angaben am 7. Oktober 2026 durch Einwurf in Ihren Briefkasten zugegangen. Wenn Sie die Kündigung angreifen wollen, muss die Kündigungsschutzklage innerhalb von drei Wochen nach Zugang beim Arbeitsgericht eingehen. Nach Ihren bisherigen Angaben endet die Frist vorläufig am Mittwoch, dem 28. Oktober 2026; die Zustellungsprüfung und der bestätigte Kalendereintrag stehen noch aus. Wird sie versäumt, gilt die Kündigung nach dem Gesetz als von Anfang an wirksam; eine spätere Klage ist nur in eng begrenzten Ausnahmefällen möglich. Die für den 20. Oktober 2026 vereinbarten Gespräche über eine Abfindung halten diese Frist nicht an. Wir empfehlen, die Klage vorsorglich zu erheben und die Gespräche parallel zu führen; eine Klage kann später zurückgenommen werden, auf eine spätere Zulassung nach Fristversäumnis darf nicht vertraut werden. Wir bitten Sie, uns Ihre Entscheidung über die Klageerhebung bis spätestens Montag, 19. Oktober 2026, mitzuteilen, damit wir den Schriftsatz prüfen und rechtzeitig einreichen können. Die Vergütung richtet sich nach der mit Ihnen geschlossenen Vergütungsvereinbarung vom [Datum]; die Klageerhebung ist davon umfasst. Mit freundlichen Grüßen [Name], Rechtsanwältin

Die Einreichung erfolgt nur im erteilten Prozessauftrag. Der Brief enthält weder Rechenweg noch Kalenderkennung; diese stehen im internen Vermerk.

### 6.5. Negativbeispiel: Begründungsfrist ab Einlegung berechnet

Falsche Ausgabe: „Die Berufung wurde am 16.10.2026 eingelegt. Die Berufungsbegründung ist daher bis zum 16.12.2026 einzureichen.“ Diese Ausgabe ist falsch, weil § 520 Abs. 2 ZPO die Begründungsfrist an die Zustellung des vollständigen Urteils knüpft, nicht an die Einlegung; bei Zustellung am 24.09.2026 endet sie am 24.11.2026, und die Ausgabe hätte drei Wochen zu spät geführt.

Korrigierte Fassung: „Die Berufungsbegründungsfrist beträgt nach § 520 Abs. 2 ZPO zwei Monate ab Zustellung des vollständigen Urteils. Die Zustellung erfolgte ausweislich des elektronischen Empfangsbekenntnisses am 24.09.2026. Die Frist endet daher am Dienstag, 24.11.2026, 24 Uhr; eine Verschiebung ist nicht veranlasst. Das Datum der Berufungseinlegung am 16.10.2026 ist für diese Frist ohne Bedeutung. Ein Verlängerungsantrag ohne Einwilligung des Gegners um bis zu einen Monat ist möglich und müsste vor dem 24.11.2026 eingehen. Verantwortlich: Rechtsanwältin [Name]. Status: berechnet, zur Eintragung übergeben.“

### 6.6. Verjährungsverzicht und nicht nachgewiesener Eingang

Der Gegner verzichtet „bis zum 31.12.2026 auf die Einrede der Verjährung hinsichtlich der Rechnung 18/2023“; die Akte enthält zusätzlich einen Schadensersatzanspruch. Der Vermerk trennt beide Ansprüche, prüft, ob der Wortlaut den zweiten erfasst, und rechnet dessen Verjährung nach §§ 195 und 199 BGB gesondert. Der 31.12.2026 ist ein Donnerstag; die Vorfrist wird so gesetzt, dass Bezifferung, Kostenvorschuss und Zustellungsvorbereitung vor den Weihnachtsfeiertagen abgeschlossen sind, weil § 167 ZPO nur bei demnächst erfolgender Zustellung hilft.
