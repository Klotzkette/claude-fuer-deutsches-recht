---
name: verteidiger-beweislast-verkehrsowi
description: "Beweislast Verkehrsowi: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beweislast Verkehrsowi

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beweislast Verkehrsowi** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-verteidiger-beweislast-und-darlegungslast` | Verteidiger: Beweislast, Darlegungslast und Substantiierung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `verkehrsowi-aktenanlage` | Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgerät, Eichschein). Output Aktenstruktur, Fristen-Übersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch. |
| `verkehrsowi-akteneinsicht-messakte` | Prüffeld für verkehrsowi akteneinsicht messakte: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Beweislast Verkehrsowi**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-verteidiger-beweislast-und-darlegungslast`

**Fokus:** Verteidiger: Beweislast, Darlegungslast und Substantiierung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verteidiger: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Verteidiger: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Verteidiger: Beweislast, Darlegungslast und Substantiierung / verteidiger beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verteidiger** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Qualitätsanker: Messdaten, Messakte und faires Verfahren

- **Verifizierter Leitanker:** BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Verfahren zugänglich sein, wenn sie konkret und rechtzeitig verlangt werden.
- **Praktische Übersetzung:** Niemals nur pauschal „Messung bestreiten“. Immer präzise anfordern: Falldatei/Rohmessdaten, Messreihe soweit vorhanden und relevant, Token/Passwort, Eichschein, Gebrauchsanweisung, Schulungsnachweise, Wartungs-/Reparaturhinweise, Standort-/Beschilderungsunterlagen, Statistik und Auswerteprotokoll.
- **Angriffslinie:** Standardisiertes Messverfahren ist eine Beweiserleichterung, kein Denkverbot. Der Skill muss aus Unterlagen konkrete Einwendungen machen: falsches Gerät, fehlende Eichung, fehlerhafte Bedienung, unklare Fahreridentität, unplausible Messreihe, fehlende Einsicht, Frist-/Gehörsproblem.
- **Output-Pflicht:** Immer ein kurzes Anforderungsschreiben oder einen gerichtsfesten Begründungsbaustein anbieten, wenn Akteneinsicht, Messunterlagen oder Fristwahrung Thema sind.

## 2. `verkehrsowi-aktenanlage`

**Fokus:** Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Messakte, Korrespondenz, Fristen, HV-Termin, Beweismittelverzeichnis (Messgerät, Eichschein). Output Aktenstruktur, Fristen-Übersicht-Tabelle, Beweismittelverzeichnis. Abgrenzung: Akteneinsicht Messakte siehe verkehrsowi-akteneinsicht-messakte; Einspruchsfrist siehe verkehrsowi-fristen-einspruch.

# Aktenanlage OWi-Mandat

## Triage zu Beginn

1. **Vollmacht vorhanden?** — Ohne Vollmacht keine Akteneinsicht.
2. **Zustellungsdatum des Bescheids dokumentiert?** — Fristbeginn.
3. **Aktenzeichen und Delikt notiert?** — Grundlage fuer Schriftsaetze.
4. **Mandantenziel klar?** — Einspruch, Einstellung, Fahrverbot-Vermeidung.
5. **Sofortmassnahmen eingeleitet?** — Einspruch und Akteneinsicht.

## Aktenstruktur OWi-Mandat

```
01_MANDANT
 - Vollmacht Original
 - Personalien, Kontakt
 - Mandantenziel schriftlich

02_BUSSGELDBESCHEID
 - Bussgeldbescheid Original/Kopie
 - Zustellungsurkunde
 - § 66 OWiG-Pruefungsnotiz

03_FRISTEN
 - Einspruchsfrist: Zustellungsdatum + 14 Tage
 - Rechtsbeschwerde-Frist (wenn noetig): Urteil + 7 Tage
 - Verjaehrungs-Check

04_SCHRIFTSAETZE_AUSGEHEND
 - Einspruch (mit Eingangsbestaetigung)
 - Akteneinsichtsantrag (mit Messakte-Aufzaehlung)

05_MESSAKTE
 - Eichschein (Gueltigkeit geprueft: Datum markiert)
 - Messprotokoll
 - Schulungsnachweis
 - Rohmessdaten (falls vorhanden)
 - Messfoto hochaufloesend

06_BEWEISMITTELVERZEICHNIS
 (s. Vorlage unten)

07_KORRESPONDENZ
 - Bussgeldbehoerde, Amtsgericht, StA
 - Chronologisch

08_HAUPTVERHANDLUNG
 - Einlassung oder Schweigen-Notiz
 - Beweisantraege
 - Plaedoyer

09_URTEIL_RECHTSBEHELFE
 - Urteil Original
 - Rechtsbeschwerde
```

## Fristen-Uebersicht OWi

| Frist | Rechtsgrundlage | Datum | Erledigt |
|-------|----------------|-------|---------|
| Einspruch | § 67 Abs. 1 OWiG | [Zustellung + 14T] | □ |
| Akteneinsicht | § 49 OWiG | Sofort | □ |
| Wiedereinsetzung (falls noetig) | § 52 OWiG | [Kenntnis + 7T] | □ |
| Rechtsbeschwerde | § 79 Abs. 1 OWiG | [Urteil + 7T] | □ |
| Rechtsbeschwerde-Begruendung | § 79 Abs. 3 OWiG | [Zustellung Urteil + 1M] | □ |
| Vier-Monats-Frist Fahrverbot | § 25 Abs. 2a StVG | [Rechtskraft + 4M] | □ |

## Beweismittelverzeichnis Messakte

| Nr. | Dokument | Datum | Geprueft | Status |
|-----|---------|-------|---------|--------|
| 1 | Eichschein | [DATUM] | □ | Gueltig bis [DATUM] |
| 2 | Messprotokoll | [DATUM] | □ | Angriffspunkte? |
| 3 | Schulungsnachweis | [DATUM] | □ | Beamter [NAME] |
| 4 | Rohmessdaten | [DATUM] | □ | Vorhanden / Fehlt |
| 5 | Messfoto | [DATUM] | □ | Fahrer identifizierbar? |

## Harte Leitplanken

- Aktenanlage unmittelbar bei Mandatsuebernahme.
- Fristen immer als Erstes eintragen.
- Messakte-Vollstaendigkeitspruefung ist Pflicht.
- Bei Aktennachlieferungen: Verzeichnis aktualisieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `verkehrsowi-akteneinsicht-messakte`

**Fokus:** Prüffeld für verkehrsowi akteneinsicht messakte: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Akteneinsicht und Messakte im OWi-Verfahren

## Triage zu Beginn

1. **Ist ein Verteidiger bestellt?** — Akteneinsicht steht nach § 49 OWiG i.V.m. § 147 StPO dem Verteidiger zu; aber auch der Betroffene selbst hat eingeschraenktes Recht (§ 49 Abs. 1 OWiG).
2. **Welche Behoerde fuehrt das Verfahren?** — Im Vorverfahren: Verwaltungsbehoerde (Bussgeldstelle); nach Einspruch: Staatsanwaltschaft oder direkt Amtsgericht.
3. **Welches Messgeraet wurde eingesetzt?** — Beeinflusst welche Unterlagen kritisch sind.
4. **Liegt die Akte bereits beim Amtsgericht?** — Nach Einspruch leitet die Bussgeldstelle ab; Akteneinsicht dann beim Gericht.
5. **Digitale oder Papierakte?** — Zunehmend elektronische Akten (eAkte); Messunterlagen koennen als PDF oder separat vorliegen.

## Zentrale Normen

- **§ 49 OWiG** — Akteneinsicht im Bussgeldbescheidverfahren; entsprechende Anwendung § 147 StPO
- **§ 147 StPO** — Recht des Verteidigers auf Akteneinsicht
- **§ 147 Abs. 5 StPO i.V.m. § 49 Abs. 2 OWiG** — Rechtsbehelf bei Versagung
- **Art. 103 Abs. 1 GG** — Rechtliches Gehoer; Rohmessdaten-Recht
- **§ 6 MessEG** — Eichpflicht fuer Verkehrsueberwachungsgeraete
- **§ 77 OWiG** — Beweisaufnahme in der Hauptverhandlung des Amtsgerichts

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vollstaendige Messakte — Was muss enthalten sein?

```
TECHNISCHE UNTERLAGEN:
□ Eichschein (original oder beglaubigte Kopie) mit Eihdatum
□ Bedienungsanleitung des Messgeraets (Kurzanleitung oder Vollversion)
□ Schulungsnachweis des Messbeamten fuer dieses Geraet
□ Zulassungsbescheinigung der PTB (physikalisch-technische Bundesanstalt)

MESSDATEN:
□ Messprotokoll (Datum, Uhrzeit, Ort, Geraet, Beamter)
□ Messfoto hochaufloesend (Kennzeichen lesbar)
□ Rohmessdaten / Statistik-Dateien (falls gespeichert)
□ Kalibrierprotokoll (Vor-/Nach-Messung)

ORTSBEZOGEN:
□ Beschilderungsplan / Lageplan des Messstandorts
□ Entfernung zu Beschilderung
□ Eventuell: Sichtweiten-Protokoll

VERWALTUNG:
□ Anhoerungsbogen (Anschreiben an Betroffenen)
□ Ggf. Zeugenaussagen der Messbeamten
```

## Schritt-fuer-Schritt-Workflow

1. **Vollmacht des Betroffenen sichern.**
2. **Akteneinsichtsgesuch stellen** bei der Bussgeldstelle (vor Einspruch) oder dem Amtsgericht (nach Einspruch); explizit alle Messunterlagen aufzaehlen.
3. **Eingang kontrollieren:** Ist die Messakte vollstaendig? Fehlendes sofort schriftlich ruegen.
4. **Eichschein-Datum pruefen:** Eichgueltigkeit zum Messzeitpunkt?
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
6. **Messprotokoll auswerten:** Aufstellungsort korrekt? Messtechnik-Vorgaben eingehalten?
7. **Bei Verweigerung:** Beschwerde nach § 49 Abs. 2 OWiG i.V.m. § 147 Abs. 5 StPO.

## Output-Template Akteneinsichtsgesuch

```
An die Zentrale Bussgeldstelle [ORT] / Amtsgericht [ORT]

In der Bussgeldsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf vollstaendige Akteneinsicht nach § 49 OWiG

Ich fordere vollstaendige Akteneinsicht einschliesslich:
1. Messprotokoll
2. Eichschein (beglaubigte Kopie)
3. Bedienungsanleitung [MESSGERAET]
4. Schulungsnachweis des messenden Beamten
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
6. Messfoto hochaufloesend
7. Beschilderungsplan / Lageplan

Anlage: Vollmacht

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Rohmessdaten-Anforderung ist Pflichtbestandteil jedes OWi-Mandats.
- Unvollstaendige Messakte immer schriftlich ruegen.
- Verweigerung — Beschwerde sofort; nicht akzeptieren.
- Anwaltliche Endkontrolle bei jedem Schritt.
