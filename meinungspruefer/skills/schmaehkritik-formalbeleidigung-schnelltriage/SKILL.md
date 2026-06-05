---
name: schmaehkritik-formalbeleidigung-schnelltriage
description: "Schmaehkritik Formalbeleidigung Schnelltriage: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schmaehkritik Formalbeleidigung Schnelltriage

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Schmaehkritik Formalbeleidigung Schnelltriage** im Plugin Meinungsfreiheit/Persönlichkeitsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schmaehkritik-formalbeleidigung-menschenwuerde` | Prüft die engen Ausnahmefälle Schmähkritik, Formalbeleidigung und Menschenwürdeangriff. Verhindert, dass Fachgerichte oder Nutzer die Art 5 GG Normalabwägung vorschnell abschneiden. |
| `schnelltriage-aeusserung` | Schnelle Erstbewertung einer Äußerung mit Ampel für Strafrecht, Zivilrecht, Plattform, Arbeitsplatz, Schule und Öffentlichkeitsrisiko. Nutzt Wortlaut, Kontext, Medium, Reichweite, betroffene Person, Belege und Ziel der Nutzerin. |

## Arbeitsweg

Im Plugin Meinungsfreiheit/Persönlichkeitsrecht gilt für **Schmaehkritik Formalbeleidigung Schnelltriage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schmaehkritik-formalbeleidigung-menschenwuerde`

**Fokus:** Prüft die engen Ausnahmefälle Schmähkritik, Formalbeleidigung und Menschenwürdeangriff. Verhindert, dass Fachgerichte oder Nutzer die Art 5 GG Normalabwägung vorschnell abschneiden.

# Schmähkritik, Formalbeleidigung, Menschenwürde

## Ausgangspunkt

Diese Kategorien sind Ausnahmen. Sie dürfen nicht als Abkürzung genutzt werden, nur weil eine Äußerung grob, unhöflich oder verletzend ist. Im Normalfall bleibt eine Abwägung erforderlich.

## Schmähkritik

Schmähung liegt erst nahe, wenn die Diffamierung der Person im Vordergrund steht und der Sachbezug praktisch wegfällt. Ein äußerer Anlass reicht nicht, wenn er nur vorgeschoben ist. Umgekehrt verhindert ein echter Sachbezug regelmäßig den vorschnellen Schmähkritik-Stempel.

## Formalbeleidigung

Formalbeleidigung meint besonders krasse, aus sich heraus herabwürdigende und gesellschaftlich tabuisierte Beschimpfungen. Kontext ist nicht völlig egal, aber die Form kann so stark sein, dass sie kaum noch grundrechtlich tragfähig ist.

## Menschenwürdeangriff

Das ist die engste und schwerste Kategorie: Der Person wird der Würdekern abgesprochen, nicht nur Ehre oder soziale Anerkennung verletzt.

## Prüffragen

- Gibt es einen nachvollziehbaren Sachanlass?
- Wird noch ein Vorgang kritisiert oder nur die Person vernichtet?
- Ist die Wortwahl gesellschaftlich absolut tabuisiert?
- Wird der Mensch als Mensch herabgesetzt?
- Wurde die Einordnung konkret begründet?
- Sollte hilfsweise trotzdem abgewogen werden?

## Output

- Ausnahme geprüft:
- Ergebnis:
- Begründung:
- Falls keine Ausnahme: Rückkehr zur Normalabwägung mit `abwaegung-art-5-gg`.

## BVerfG-Linie und Trade-offs

- **BVerfG ständige Rspr.:** Schmähkritik ist eng auszulegen — nur bei reiner Diffamierung ohne Sachbezug. Sachbezug (auch über Ecken) verdrängt regelmäßig den Schmähvorwurf. Vgl. BVerfG, Beschl. v. 19.05.2020 — 1 BvR 2397/19 ("Sterbehilfeverein"), BVerfG, Beschl. v. 19.12.2021 — 1 BvR 1073/20 — Az. live verifizieren.
- **Formalbeleidigung (§ 192 StGB Schranke):** Hier hat BVerfG die Kategorie geschärft — Bezug zur Person, Form, gesellschaftliche Tabuisierung. Auch hier keine pauschale Sperre für Abwägung.
- **Menschenwürdeangriff (Art. 1 I GG):** Absolute Grenze. Beispiele: NS-Vergleiche mit Vernichtungsbezug, Entmenschlichung. Bei Menschenwürdeangriff entfällt jede Abwägung.
- **Stolpe-Linie (BVerfGE 114, 339):** Bei Mehrdeutigkeit gilt für Unterlassungsklage: jede vertretbare Variante muss bei Unterlassung verboten werden können — engerer Maßstab als bei Schadensersatz.
- **Echo (Persönlichkeit, Recht am eigenen Bild, allgemeines Persönlichkeitsrecht):** Art. 2 I iVm Art. 1 I GG; abzuwägen gegen Art. 5 I GG.
- **§ 188 StGB (Personen des politischen Lebens):** ab 22.09.2021 verschärft; Strafrahmen bis 5 Jahre Freiheitsstrafe.
- Falle: "Schmähkritik" wird vorgerichtlich oder im Schriftsatz als Kürzel verwendet, BVerfG fordert aber detaillierte Subsumtion. Bei Verstoß: Aufhebung durch BVerfG (Verfassungsbeschwerde lohnt regelmäßig).

## 2. `schnelltriage-aeusserung`

**Fokus:** Schnelle Erstbewertung einer Äußerung mit Ampel für Strafrecht, Zivilrecht, Plattform, Arbeitsplatz, Schule und Öffentlichkeitsrisiko. Nutzt Wortlaut, Kontext, Medium, Reichweite, betroffene Person, Belege und Ziel der Nutzerin.

# Schnelltriage Äußerung

## Aufgabe

Erstelle in wenigen Minuten ein belastbares Erstbild. Die Schnelltriage ersetzt keine Vollprüfung, verhindert aber, dass die Sache in die falsche Schublade fällt.

## Mindestdaten

- Exakter Wortlaut.
- Datum, Medium, Empfängerkreis.
- Betroffene Person oder Institution.
- Anlass und Vorgeschichte.
- Belege für tatsächliche Bestandteile.
- Gewünschter Output: Veröffentlichungscheck, Abwehr, Anzeige, Abmahnung, Plattformmeldung, Entschuldigung.

## Ampellogik

**Grün** bedeutet: Bei bekanntem Kontext spricht viel für zulässige Meinung, Sachkritik oder hinreichend belegte Tatsachenbehauptung. Formuliere trotzdem verbleibende Risiken.

**Gelb** bedeutet: Der Fall hängt an Kontext, Mehrdeutigkeit, Beleglage, Reichweite, Ton oder Person des Betroffenen. Empfiehl eine Vertiefung.

**Rot** bedeutet: konkrete Gefahr wegen bewusst unwahrer Tatsachenbehauptung, schwerer persönlicher Herabsetzung ohne Sachbezug, Prangerwirkung, wiederholter Veröffentlichung oder fehlender Belege bei strafrechtlich relevanten Vorwürfen.

## Prüfschritte

1. **Sinnermittlung:** Wie versteht ein unvoreingenommenes Publikum die Äußerung im Gesamtzusammenhang?
2. **Äußerungstyp:** Meinung, Tatsache, gemischt, Verdachtsäußerung, Satire, Zitat, Frage.
3. **Normpfad:** §§ 185, 186, 187, 188, 193, 194 StGB; zivilrechtlich APR, §§ 823, 824, 1004 BGB analog.
4. **Grundrechte:** Art. 5 GG zwingt im Normalfall zur Abwägung; Art. 10 EMRK und Art. 11 GRCh als europäische Leitplanken.
5. **Kontextfaktoren:** Machtkritik, Kampf ums Recht, Spontanität, Vorbedacht, Reichweite, Wiederholung, Bildnutzung, Anprangerung.

## Output

Gib aus:

- **Erste Einordnung:** Meinung/Tatsache/gemischt.
- **Hauptproblem:** ein Satz.
- **Ampel Strafrecht:**
- **Ampel Zivilrecht:**
- **Ampel Plattform/Arbeitsplatz/Schule:**
- **Was fehlt noch?**
- **Nächste Skills:** zwei bis fünf konkrete Vorschläge.

## Warnhinweis

Keine endgültige Bewertung, wenn der Wortlaut unvollständig ist oder nur berichtet wird, was "ungefähr" gesagt wurde. Dann zuerst `zitat-und-kontextaufnahme`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
