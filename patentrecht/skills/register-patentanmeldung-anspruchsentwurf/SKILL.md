---
name: register-patentanmeldung-anspruchsentwurf
description: "Register Patentanmeldung Anspruchsentwurf: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Register Patentanmeldung Anspruchsentwurf

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Register Patentanmeldung Anspruchsentwurf** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsstand-register-und-fristen` | Prüft Patentregister und Fristen: DPMAregister, EPO Register, nationale Validierungen, Einheitspatent, Jahresgebühren, Priorität, Veröffentlichung, Erteilung, Einspruch, Beschränkung, Nichtigkeit und Verlängerungen. |
| `spezial-patentanmeldung-fristen-form-und-zustaendigkeit` | Patentanmeldung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin patentrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `patentanmeldung-anspruchsentwurf` | Bereitet Patentansprüche vor: Anspruch 1, Unteransprüche, Alternativausführungen, Vorrichtung/Verfahren/System/Computerprogramm, Stütze in Beschreibung und Rückfragen zur Anspruchsbreite. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Register Patentanmeldung Anspruchsentwurf**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsstand-register-und-fristen`

**Fokus:** Prüft Patentregister und Fristen: DPMAregister, EPO Register, nationale Validierungen, Einheitspatent, Jahresgebühren, Priorität, Veröffentlichung, Erteilung, Einspruch, Beschränkung, Nichtigkeit und Verlängerungen.

# Rechtsstand, Register und Fristen

## Registerquellen

- DPMAregister für deutsche Schutzrechte.
- EPO Register für EP-Anmeldungen und EP-Patente.
- nationale Register für validierte EP-Teile.
- UPC/EPA/DPMA-Informationen, soweit Verfahrensstand betroffen ist.

## Fristenliste

| Frist | Startpunkt | Was prüfen? |
| --- | --- | --- |
| Prioritätsjahr | erste Anmeldung | Nachanmeldung/EP/PCT möglich? |
| Prüfungsbescheid | Zustellung/Amtsmitteilung | Antwortfrist, Verlängerung, Gebühren |
| Jahresgebühren | Anmeldetag/Jahr | gezahlt, Nachfrist, Erlöschen |
| Einspruch EP | Bekanntmachung der Erteilung | Fristende, Gebühr, Einspruchsgründe |
| Nichtigkeit | prozessuale Lage | Zulässigkeit, Parallelverfahren |
| Abmahnung | Zugang | Unterlassung/EV-Risiko |

## Output

- Registerauszug-Zusammenfassung mit Abrufdatum.
- Fristenkalender.
- Statusampel.
- offene Registerlücken.

## Regel

Nie allein aus einer Patentnummer schließen, dass ein Patent in Kraft ist. Immer Rechtsstand, Territory und geltende Anspruchsfassung prüfen.

## Konkrete Fristen

- **Prioritätsjahr Art. 87 EPÜ / § 41 PatG:** 12 Monate ab erster Hinterlegung; PCT-Frist ebenfalls 12 Monate.
- **PCT-Nationalisierung:** regelmäßig 30 oder 31 Monate ab Prioritätstag (Land-spezifisch; DE und EP: 31 Monate).
- **Recherchengebühr EPA:** mit Anmeldung; Prüfungsantrag binnen 6 Monaten nach Veröffentlichung des Recherchenberichts (Art. 94 (1) EPÜ).
- **Antwort auf Prüfungsbescheid EPA:** regelmäßig 4 Monate, verlängerbar.
- **DPMA-Prüfungsantrag (§ 44 PatG):** binnen 7 Jahren nach Anmeldetag.
- **Einspruch EPA:** **9 Monate** ab Veröffentlichung des Erteilungshinweises (Art. 99 EPÜ).
- **Beschränkungs-/Widerrufsantrag (Art. 105a EPÜ):** jederzeit.
- **Jahresgebühren EPA:** ab dem 3. Anmeldejahr; ab Erteilung an nationale Ämter.
- **Jahresgebühren DPMA (§ 17 PatG):** ab dem 3. Anmeldejahr; bei Nichtzahlung Erlöschen (§ 20 PatG); Wiedereinsetzungsfrist § 123 PatG.
- **Nichtigkeitsklage BPatG (§ 81 PatG):** keine starre Frist, aber nur gegen erteiltes Patent.
- **UPC Opt-out (Übergangszeit):** prüfen Sie aktuell unifiedpatentcourt.org -- Übergangszeitraum 7 Jahre ab Inkrafttreten UPCA (mit Verlängerungsoption auf 14 Jahre).

## Quellen live
- `register.dpma.de`, `register.epo.org`, `worldwide.espacenet.com`, `unifiedpatentcourt.org`, `wipo.int/portal/en/index.html` (PatentScope für PCT).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `spezial-patentanmeldung-fristen-form-und-zustaendigkeit`

**Fokus:** Patentanmeldung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin patentrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Patentanmeldung: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Patentanmeldung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Patentanmeldung: Fristen, Form, Zuständigkeit und Rechtsweg / patentanmeldung fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FTO ist eine Arbeitsmethode, keine Rechtsquelle. Je nach Teilfrage PatG §§ 1-5, 9, 10, 14, 34, 64; EPÜ Art. 52-57 und 69; UPCA Art. 32 und 62; UPC-Verfahrensordnung; nationale Patentgesetze/Patentämter live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Patentanmeldung** prüfen.
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

## 3. `patentanmeldung-anspruchsentwurf`

**Fokus:** Bereitet Patentansprüche vor: Anspruch 1, Unteransprüche, Alternativausführungen, Vorrichtung/Verfahren/System/Computerprogramm, Stütze in Beschreibung und Rückfragen zur Anspruchsbreite.

# Patentanmeldung — Anspruchsentwurf

## Arbeitsmodus

Der Skill entwirft keine endgültige Patentanmeldung, sondern einen belastbaren Arbeitsentwurf für Patentanwältinnen und Patentabteilungen.

## Schritte

1. **Erfindungskern formulieren:** ein Satz mit technischer Aufgabe, Lösung und Wirkung.
2. **Anspruchskategorie wählen:** Vorrichtung, Verfahren, Verwendung, System, computerimplementiertes Verfahren, Datenträger, Produkt-by-Process nur vorsichtig.
3. **Merkmale sortieren:** zwingend, bevorzugt, optional, Ausführungsbeispiel, bloßer Vorteil.
4. **Breite prüfen:** Anspruch so breit wie vertretbar; keine unnötige Einengung durch konkrete Maße, Materialien oder Herstellerteile.
5. **Unteransprüche bauen:** Varianten, fallback positions, kommerzielle Kernfeatures, Schutz gegen Design-around.
6. **Beschreibung koppeln:** jedes Anspruchsmerkmal braucht Offenbarungsstütze.
7. **Recherchebedarf markieren:** unbekannte Merkmale und voraussichtlich kritischer Stand der Technik.

## Outputstruktur

```text
Anspruch 1 (Arbeitsentwurf)
[Kategorie] umfassend:
a) ...
b) ...
dadurch gekennzeichnet, dass ...

Unteransprüche
2. ...
3. ...

Offene Punkte
- [noch zu klären: ...]

Risiken der Anspruchsfassung
- zu eng: ...
- zu breit: ...
- fehlende Stütze: ...
```

## Red Flags

- Claim liest sich wie Produktwerbung statt technische Lehre.
- Vorteil steht im Anspruch, aber kein technisches Merkmal.
- Nur ein Ausführungsbeispiel vorhanden, aber sehr breiter Anspruch gewünscht.
- Software/AI-Feature ohne technischen Beitrag.
- Vorveröffentlichung oder Verkauf vor Anmeldung ungeklärt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
