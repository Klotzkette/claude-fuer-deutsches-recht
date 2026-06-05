---
name: auszahlungsvoraussetzungen-kaufpreis
description: "Auszahlungsvoraussetzungen Kaufpreis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Auszahlungsvoraussetzungen Kaufpreis

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Auszahlungsvoraussetzungen Kaufpreis** im Plugin Notariat Alltag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notariat-045-auszahlungsvoraussetzungen-kaufpreis-und-loeschungs` | Notariat im Alltag: Auszahlungsvoraussetzungen – Kaufpreis und Löschungsunterlagen. Vollständige Prüfung aller Fälligkeitsvoraussetzungen vor Fälligkeitsmitteilung, Löschungsunterlagen-Management und Direktzahlung an Grundpfandgläubiger. |
| `notariat-046-abwicklung-todesfall-beteiligter-vor-vollzug` | Notariat im Alltag: Abwicklung Todesfall eines Beteiligten vor Vollzug. Rechtliche Konsequenzen des Todes eines Käufers, Verkäufers oder GmbH-Gesellschafters während des laufenden Vollzugs und notarielle Schritte. |
| `notariat-047-gesellschafterstreit-im-notartermin-neutralitaet-un` | Notariat im Alltag: Gesellschafterstreit im Notartermin – Neutralität und Protokoll. Umgang mit streitigen Beschlüssen und Gesellschafterversammlungen, Beschlussmängelklage und Protokollpflichten. |

## Arbeitsweg

Im Plugin Notariat Alltag gilt für **Auszahlungsvoraussetzungen Kaufpreis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `notariat-045-auszahlungsvoraussetzungen-kaufpreis-und-loeschungs`

**Fokus:** Notariat im Alltag: Auszahlungsvoraussetzungen – Kaufpreis und Löschungsunterlagen. Vollständige Prüfung aller Fälligkeitsvoraussetzungen vor Fälligkeitsmitteilung, Löschungsunterlagen-Management und Direktzahlung an Grundpfandgläubiger.

# Notariat im Alltag: Auszahlungsvoraussetzungen – Kaufpreis, Löschungsunterlagen

## Zweck und Anwendungsbereich

Die Fälligkeitsmitteilung ist der kritischste Schritt im Grundstücksvollzug: Erst wenn alle Voraussetzungen lückenlos vorliegen, darf der Käufer den Kaufpreis zahlen. Dieser Skill prüft systematisch alle Voraussetzungen und strukturiert das Löschungsunterlagen-Management.

Rechtsgrundlagen: § 311b BGB (Kaufvertrag), §§ 19, 22 GBO (Grundbuchanforderungen), § 22 GrEStG (steuerliche Unbedenklichkeit), § 3 MaBV (Bauträger), §§ 883–888 BGB (Auflassungsvormerkung), § 54a BeurkG (Verwahrungsanweisung), § 1192 BGB (Grundschuld), GNotKG Kostenfälligkeitsregeln.

## Vollständige Fälligkeitsprüfung

Kein Kaufpreis ohne Abschluss ALLER dieser Punkte:

| Voraussetzung | Norm | Status |
|---|---|---|
| Auflassungsvormerkung Käufer eingetragen | § 883 BGB, § 13 GBO | □ |
| Vorkaufsrecht-Negativattest Gemeinde | § 28 BauGB | □ |
| GVO-Genehmigung (Landwirtschaft) | GrdstVG | □ (falls relevant) |
| Familiengerichtliche Genehmigung | § 1643 BGB n.F. | □ (falls Minderjährige) |
| Betreuerrechtliche Genehmigung | § 1821 BGB n.F. | □ (falls Betreuer) |
| Steuerliche Unbedenklichkeit | § 22 GrEStG | □ |
| Löschungsunterlagen für Abt. III | § 19 GBO | □ |
| Löschungsunterlagen für Abt. II (soweit relevant) | § 19 GBO | □ |
| GwG-Dokumentation vollständig | §§ 10–11 GwG | □ |
| MaBV-Voraussetzungen (Bauträger) | § 3 MaBV | □ (falls Bauträger) |

## Löschungsunterlagen-Management

Bestehende Grundschulden (Abt. III) müssen vor oder Zug-um-Zug mit der Eigentumsumschreibung gelöscht werden.

**Ablauf:**
1. Bestehende Grundschulden aus Abt. III listen (offene Valuta ermitteln)
2. Tilgungsbeträge aus Kaufpreis berechnen
3. Frühzeitig bei Bank anfordern (Vorlaufzeit 2–4 Wochen)
4. Löschungsunterlagen prüfen: Bewilligung + Quittung/Freistellung für richtigen Betrag und richtiges Grundstück
5. Direktzahlung aus Kaufpreis an Bank koordinieren (Zahlungsanweisung im Kaufvertrag)

## Direktzahlung an Grundpfandgläubiger

Wenn Grundschulden abgelöst werden:
- Kaufpreisteil wird direkt an die finanzierende Bank des Verkäufers gezahlt
- Notar koordiniert die Zahlungsplanung: Restbetrag an Verkäufer
- Löschungsunterlagen werden erst nach Zahlungsnachweis freigegeben
- Einzugsermächtigung im Kaufvertrag dokumentieren

## Fälligkeitsmitteilung

Die Fälligkeitsmitteilung ist das förmliche Schreiben, mit dem der Notar dem Käufer mitteilt, dass alle Voraussetzungen erfüllt sind und der Kaufpreis nun fällig ist.

**Inhalt der Fälligkeitsmitteilung:**
- Datum der Prüfung
- Bestätigung, dass alle vertraglich genannten Voraussetzungen erfüllt sind
- Zahlungsziel und Zahlungsempfänger
- Betrag (aufgeteilt: Bank/Verkäufer)

## Prüfprogramm

- Vollständige Checkliste vor jeder Fälligkeitsmitteilung abgehakt?
- Vier-Augen-Prüfung vor Versand?
- Sind Löschungsunterlagen inhaltlich korrekt (richtiger Name, richtiges Grundstück, richtiger Betrag)?
- Steuerliche Unbedenklichkeit aktuell (nicht älter als 3 Monate)?

## Typische Fallen

- Fälligkeitsmitteilung ohne steuerliche Unbedenklichkeit → § 22 GrEStG-Sperre.
- Löschungsunterlagen für falsches Grundstück → Löschung unmöglich.
- Direktzahlung an Bank vergessen → Bank gibt Löschungsunterlagen nicht heraus.
- Familiengericht-Genehmigung fehlt → Vollzug blockiert.
- Vier-Augen-Prüfung unterblieben → Fehler nicht bemerkt.

## Rechtsquellen

- § 22 GrEStG: https://dejure.org/gesetze/GrEStG/22.html
- § 28 BauGB: https://dejure.org/gesetze/BauGB/28.html
- § 883 BGB: https://dejure.org/gesetze/BGB/883.html
- § 19 GBO: https://dejure.org/gesetze/GBO/19.html
- BNotK Vollzugshinweise: https://www.bnotk.de

## Output-Formate

- **Fälligkeits-Vollprüfungs-Checkliste** (alle Voraussetzungen)
- **Löschungsunterlagen-Tabelle** (Grundschuld, Betrag, Status)
- **Fälligkeitsmitteilung** (Muster)
- **Direktzahlungs-Anweisung** (an Käufer)
- **Vier-Augen-Prüfprotokoll** (vor Versand)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

## 2. `notariat-046-abwicklung-todesfall-beteiligter-vor-vollzug`

**Fokus:** Notariat im Alltag: Abwicklung Todesfall eines Beteiligten vor Vollzug. Rechtliche Konsequenzen des Todes eines Käufers, Verkäufers oder GmbH-Gesellschafters während des laufenden Vollzugs und notarielle Schritte.

# Notariat im Alltag: Abwicklung Todesfall eines Beteiligten vor Vollzug

## Zweck und Anwendungsbereich

Der Tod eines Beteiligten vor Abschluss des Vollzugs wirft komplexe Rechtsfragen auf: Geht der Vertrag auf die Erben über? Wer ist jetzt handlungsfähig? Wie wird der Vollzug gesichert? Dieser Skill strukturiert die notariellen Sofortmaßnahmen.

Rechtsgrundlagen: § 1922 BGB (Gesamtrechtsnachfolge), §§ 2032–2063 BGB (Erbengemeinschaft), §§ 2353–2375 BGB (Erbschein), § 35 GBO (Grundbuchberichtigung), § 1629 BGB (Vertretung Minderjähriger durch überlebenden Elternteil), §§ 177–180 BGB (vollmachtloser Vertreter), § 130 Abs. 2 BGB (Tod des Erklärenden nach Abgabe der Willenserklärung).

## Wirkung beurkundeter Verträge bei Tod eines Beteiligten

Beurkundete Willenserklärungen wirken nach § 130 Abs. 2 BGB fort, auch wenn der Erklärende nach Abgabe der Erklärung stirbt. Das Verpflichtungsgeschäft (Kaufvertrag) bleibt wirksam und geht auf die Erben über (§ 1922 BGB).

Ausnahmen: Höchstpersönliche Rechtsgeschäfte (z.B. Ehevertrag) erlöschen mit dem Tod.

## Tod des Käufers

Der Kaufvertrag geht auf die Erben über. Die Erben treten in die Käuferposition ein.

**Konsequenzen:**
- Erbnachweis (Erbschein oder Testament + Eröffnungsprotokoll) muss vorgelegt werden
- Auflassungsvormerkung bleibt für die Erben-Käufer bestehen
- Vollzug läuft auf die Erben; ggf. müssen alle Erben handeln (§ 2040 BGB: gemeinschaftliche Verfügung)
- Finanzierung: Bank des Käufers prüft, ob Kredit auf Erben übertragen wird

## Tod des Verkäufers

Der Kaufvertrag geht auf die Erben über.

**Konsequenzen:**
- Erben sind zur Auflassung verpflichtet (§§ 433, 2032 BGB)
- Grundbuchberichtigung auf Erben nötig, bevor Auflassung an Käufer vollzogen werden kann (§ 40 GBO: Voreintragung)
- Alternativ: Erben lassen direkt auf Käufer auf (direkte Auflassung ohne Zwischeneintragung, wenn alle Erben mitwirken)
- Sterbeurkunde und Erbnachweis besorgen

## Tod eines GmbH-Gesellschafters

GmbH-Anteile gehen auf die Erben über (§§ 1922, 15 Abs. 1 GmbHG, sofern kein Einziehungsrecht).

**Konsequenzen:**
- Gesellschafterliste muss aktualisiert werden (§ 40 GmbHG)
- Falls Satzung eine Einziehungsklausel enthält: Einziehungsrecht der verbleibenden Gesellschafter prüfen
- Erbnachweis für die Erben als neue Gesellschafter
- Ggf. Abtretung der Anteile an verbleibende Gesellschafter (Kauf oder Schenkung)

## Vollzugsblockade und sofortige Maßnahmen

1. **Vollzug sofort stoppen:** Keine Fälligkeitsmitteilung bis Rechtslage geklärt.
2. **Alle Beteiligten informieren** (Käufer/Verkäufer, Bank, Gegenseite).
3. **Erbnachweis anfordern:** Erbschein beim Nachlassgericht oder Testament + Eröffnungsprotokoll.
4. **Bevollmächtigungsstatus prüfen:** Hatte der Verstorbene einen Bevollmächtigten? Postmortem-Vollmacht?
5. **Genehmigungen:** Ggf. neue Genehmigungen für Erben (Minderjährige, Betreuung?).

## Prüfprogramm

- Ist der Kaufvertrag noch erfüllbar (nicht höchstpersönlich)?
- Liegt Erbnachweis vor?
- Bei Verkäufertod: Voreintragung auf Erben nötig?
- Bei Käufertod: Erbengemeinschaft, alle müssen handeln?
- GmbH: Satzungsregelung für Erbfall beachtet?

## Typische Fallen

- Vollzug weitergeführt ohne Erbnachweis → Eigentumsumschreibung ohne Legitimation.
- Direktauflassung Verkäufererben an Käufer ohne alle Erben → Unwirksamkeit.
- GmbH-Gesellschafterliste nicht aktualisiert → Stimmrechtsprobleme.
- Minderjährige Erben: familiengerichtliche Genehmigung vergessen.

## Rechtsquellen

- § 1922 BGB: https://dejure.org/gesetze/BGB/1922.html
- § 130 Abs. 2 BGB: https://dejure.org/gesetze/BGB/130.html
- § 2040 BGB: https://dejure.org/gesetze/BGB/2040.html
- § 35 GBO: https://dejure.org/gesetze/GBO/35.html
- § 40 GmbHG: https://dejure.org/gesetze/GmbHG/40.html

## Output-Formate

- **Todesfall-Sofortmaßnahmen-Checkliste** (je nach Beteiligter-Rolle)
- **Erbnachweis-Anforderungsschreiben**
- **Vollzugscockpit-Update** (neuer Status nach Todesfall)
- **Mandantenmail** (Information Erben über Vertragsfortsetzung)
- **GmbH-Gesellschafterliste** (Erbfolge-Aktualisierung)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

## 3. `notariat-047-gesellschafterstreit-im-notartermin-neutralitaet-un`

**Fokus:** Notariat im Alltag: Gesellschafterstreit im Notartermin – Neutralität und Protokoll. Umgang mit streitigen Beschlüssen und Gesellschafterversammlungen, Beschlussmängelklage und Protokollpflichten.

# Notariat im Alltag: Gesellschafterstreit im Notartermin – Neutralität, Protokoll

## Zweck und Anwendungsbereich

Wenn Gesellschafter im Beurkundungstermin streiten, ist der Notar in einer schwierigen Lage. Dieser Skill klärt Neutralitätspflichten, Protokollierungsanforderungen und die Konsequenzen fehlerhafter Beschlussprotokolle.

Rechtsgrundlagen: § 14 BNotO (Unparteilichkeit), § 17 BeurkG (Willensermittlung), § 130 AktG (Beschlussprotokoll AG), § 53 GmbHG (Satzungsänderung GmbH), § 48 GmbHG (Gesellschafterversammlung GmbH), §§ 241–261 AktG (Beschlussmängel AG), FamFG §§ 375–406 (Registerverfahren).

## Beurkundung von Gesellschafterbeschlüssen

Bestimmte Gesellschafterbeschlüsse bedürfen der notariellen Beurkundung:
- GmbH: Satzungsänderung (§ 53 Abs. 2 GmbHG), Kapitalerhöhung/-herabsetzung
- AG: Satzungsänderung, Kapitalmaßnahmen (§§ 179, 182 AktG), Verschmelzungsbeschluss (§ 13 UmwG)
- Beschlussprotokolle: § 130 AktG für alle HV-Beschlüsse der AG

## Beschlussprotokoll: Pflichtinhalt

| Element | Norm |
|---|---|
| Ort und Datum der Versammlung | § 130 Abs. 1 AktG |
| Anwesende Aktionäre/Gesellschafter und Stimmzahl | § 130 Abs. 2 AktG |
| Beschlüsse mit Abstimmungsergebnis (Ja/Nein/Enthaltung) | § 130 Abs. 2 AktG |
| Unterschrift des Vorsitzenden und des Notars | § 130 Abs. 3 AktG |
| Anträge und Widersprüche | § 130 Abs. 2 S. 3 AktG |

## Neutralitätspflicht (§ 14 BNotO)

Der Notar protokolliert nur das, was tatsächlich beschlossen wird. Er gibt keine Bewertung über die Zweckmäßigkeit von Beschlüssen ab. Er kann auf formelle Mängel hinweisen (fehlende Beschlussfähigkeit, Einberufungsfehler), aber er verhindert nicht den Beschluss.

## Beschlussmängel: Was ist zu protokollieren?

Wenn ein Gesellschafter Widerspruch erhebt oder Beschlussmängel rügt:
- Widerspruch vollständig protokollieren (§ 130 Abs. 2 S. 3 AktG)
- Mängelrüge des Gesellschafters in das Protokoll aufnehmen
- Notar wertet den Mangel nicht in der Urkunde – das ist Sache des Gerichts

**Rechtsfolgen von Beschlussmängeln:**
- Anfechtbarkeit (§§ 243–255 AktG bei AG, § 51a GmbHG analog): 1-Monat-Frist
- Nichtigkeit (§§ 241–242 AktG): unbefristet

## Einberufungsmängel

Einberufungsfehler (zu kurze Frist, fehlende Tagesordnung) führen zur Anfechtbarkeit der Beschlüsse. Notar kann darauf hinweisen, aber nicht allein verhindern. Protokoll muss Einberufungsnachweis enthalten.

## Prüfprogramm

- Ist die Gesellschafterversammlung ordnungsgemäß einberufen (Frist, Form, Tagesordnung)?
- Sind alle Gesellschafter anwesend oder ordnungsgemäß vertreten?
- Ist die Beschlussfähigkeit (Quorum) erfüllt?
- Werden alle Widersprüche vollständig protokolliert?
- Beschlussfassung mit korrektem Stimmzählergebnis?

## Typische Fallen

- Beschlussprotokoll ohne Stimmzählung → Anfechtungsrisiko.
- Widerspruch nicht protokolliert → Gesellschafter verliert Anfechtungsrecht.
- Einberufungsfehler übersehen → alle Beschlüsse anfechtbar.
- Notar gibt inhaltliche Bewertung im Protokoll → Unparteilichkeitsverstoß.
- Nichterscheinen eines Gesellschafters bei Allstimmigkeitsbeschluss → Beschluss unwirksam.

## Rechtsquellen

- § 130 AktG: https://dejure.org/gesetze/AktG/130.html
- § 53 GmbHG: https://dejure.org/gesetze/GmbHG/53.html
- §§ 241–261 AktG: https://dejure.org/gesetze/AktG/241.html
- § 14 BNotO: https://dejure.org/gesetze/BNotO/14.html
- BGH zu Beschlussmängeln: https://www.bgh.de
- BNotK Gesellschaftsrecht: https://www.bnotk.de

## Output-Formate

- **Beschlussprotokoll-Muster** (GmbH / AG)
- **Beschlussfähigkeits-Prüfbogen**
- **Widerspruchs-Protokollierung** (Muster)
- **Beschlussmängel-Checkliste** (Anfechtbar vs. Nichtig)
- **Mandantenmail** (nach streitigem Termin)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de
