---
name: drittlandtransfer-behoerdenpaket-output
description: "Behördenfähiges Dokumentations- und Antwortpaket für Drittlandtransfers erstellen: Deckvermerk, Transferregister, DPF/SCC/TIA-Nachweise, TOMs, Subprozessoren, Maßnahmenplan und Antwort an deutsche Datenschutzaufsicht."
---

# Drittlandtransfer-Behördenpaket-Output

## Zweck

Dieser Skill erstellt aus vorhandenen Prüfungen ein geordnetes Paket für Datenschutzaufsichtsbehörden, interne Audits, DSB-Berichte oder Geschäftsführungsfreigaben. Er sammelt nicht nur Dokumente, sondern macht sichtbar, warum der Transfer erlaubt, eingeschränkt erlaubt oder vorläufig gestoppt ist.

## Startsignal

Dieses Fachmodul, wenn der Nutzer sagt:

- "Die Aufsichtsbehörde fragt nach dem US-Transfer."
- "Wir brauchen ein Paket, das wir vorlegen können."
- "Bitte druckreif dokumentieren."
- "Zeig, dass DPF/SCC/TIA geprüft wurden."
- "Wir müssen nachweisen, dass ein Anbieter gelistet oder nicht gelistet ist."

## Eingangslogik

1. Liegt bereits ein TIA vor? Wenn nein, `us-transfer-tia-dokumentation` vorschlagen und den fehlenden Kern extrahieren.
2. Liegen SCC vor? Wenn unklar, `standardvertragsklauseln-scc-paket` vorschlagen.
3. Liegt ein DPF-Nachweis vor? Wenn nein, Abruf/Prüfung als `nicht verifiziert` markieren und Nachholung als Sofortmaßnahme setzen.
4. Ist die Behördenfrist bekannt? Wenn ja, Ausgabe nach Frist priorisieren.

## Paketstruktur

### 1. Deckvermerk

Erstelle einen klaren Vermerk:

- Aktenzeichen/Behördenbezug.
- Verantwortliche Stelle und Datenschutzkontakt.
- Betroffener Dienst/Transfer.
- Kurzentscheidung: DPF / SCC + TIA / BCR / Art. 49 / Stop.
- Standdatum.
- Liste der beigefügten Nachweise.
- Offene Punkte und Nachreichungsangebot.

### 2. Entscheidungsmatrix

| Frage | Ergebnis | Nachweis | Risiko | Maßnahme |
|---|---|---|---|---|
| Gibt es einen Drittlandtransfer? | Ja/Nein | Transferregister | ... | ... |
| Ist ein Angemessenheitsbeschluss einschlägig? | Ja/Nein/Teilweise | DPF-Check | ... | ... |
| Sind SCC/BCR erforderlich? | Ja/Nein | Vertrag/Annex | ... | ... |
| Liegt ein TIA vor? | Ja/Nein | TIA-Vermerk | ... | ... |
| Sind Subprozessoren prüfbar? | Ja/Nein | Subprozessorliste | ... | ... |
| Sind ergänzende Maßnahmen ausreichend? | Ja/Nein/Offen | TOM-Matrix | ... | ... |

### 3. Anlagenverzeichnis

Nummeriere die Anlagen:

1. Transferregister-Auszug.
2. DPF-Prüfvermerk mit Abrufdatum.
3. AVV/DPA.
4. SCC mit Modul- und Annex-I-III-Übersicht.
5. TIA-Vermerk.
6. TOM-/Security-Anlage.
7. Subprozessoren-Archiv.
8. Datenschutzhinweis-/VVT-Auszug.
9. Managemententscheidung.
10. Review-Kalender und Maßnahmenplan.

### 4. Behördenantwort

Formuliere neutral, präzise und ohne Überbehauptung:

- Was geprüft wurde.
- Welche Rechtsgrundlage aktuell herangezogen wird.
- Warum Safe Harbor/Privacy Shield nicht als aktuelle Grundlage genutzt werden.
- Ob DPF trägt und für welchen Scope.
- Falls DPF nicht trägt: welche SCC/BCR/TIA-Maßnahmen greifen.
- Welche Lücken erkannt und bis wann geschlossen werden.

**Keine falsche Sicherheit:** Wenn ein Nachweis fehlt, schreibe nicht "liegt vor", sondern "wird bis [Datum] nachgereicht" oder "ist beim Anbieter angefordert".

## Drei Standardszenarien

### A. US-Anbieter aktiv DPF-gelistet

Output-Schwerpunkt:

- DPF-Check als Hauptnachweis.
- Scope-Abgleich.
- Transferregister und AVV.
- TOMs und Subprozessoren als Kontrollnachweise.
- Review alle 6 bis 12 Monate und bei Zertifizierungsablauf.

### B. US-Anbieter nicht oder nicht passend DPF-gelistet

Output-Schwerpunkt:

- SCC-Modulwahl.
- TIA mit Drittlandsrecht/Praxis und Zusatzmaßnahmen.
- Subprozessoren.
- Entscheidung "Freigabe mit Auflagen" oder "Stop".
- Keine Berufung auf DPF für diesen Transfer.

### C. Altfall Safe Harbor/Privacy Shield

Output-Schwerpunkt:

- Historische Grundlage ausdrücklich als überholt markieren.
- Zeitraum und Datenflüsse abgrenzen.
- Aktuelle Ersatzgrundlage festlegen.
- Nachbereinigung von Datenschutzhinweisen, AVV, VVT und Einkaufsakten.

## Druckreifes Ausgabeformat

Wenn der Nutzer "ausdrucken", "vorlegen", "Behörde" oder "Aktenvermerk" sagt, liefere:

1. **Einseitige Executive Summary**.
2. **Vollvermerk** mit Tabellen.
3. **Anlagenliste**.
4. **Antwortschreiben**.
5. **Offene-Punkte-Liste** mit Eigentümer und Datum.

## Qualitätsgate vor Abschluss

- Stimmen Rechtsträgernamen überall überein?
- Ist der genaue Transfer benannt, nicht nur der Anbieter?
- Sind DPF/SCC/TIA logisch konsistent?
- Gibt es keine Behauptung "Shield gültig"?
- Sind Dokumentstände datiert?
- Sind offene Punkte sichtbar statt versteckt?
- Ist die nächste Wiedervorlage gesetzt?

## Quellen und Aktualität

- Stand: 05/2026.
- DSGVO Art. 5 Abs. 2, Art. 24, Art. 28, Art. 30, Art. 44-49.
- EU-US Data Privacy Framework-Angemessenheitsbeschluss vom 10.07.2023.
- Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914.
- EDSA Recommendations 01/2020.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
