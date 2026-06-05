---
name: rechtsvergleich-usa-risikomatrix-ampel
description: "Rechtsvergleich USA Risikomatrix Ampel: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsvergleich USA Risikomatrix Ampel

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Rechtsvergleich USA Risikomatrix Ampel** im Plugin Meinungsfreiheit/Persönlichkeitsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsvergleich-usa-supreme-court` | Vergleicht deutsche Meinungsfreiheit mit der US-First-Amendment-Linie des Supreme Court: defamation, actual malice, opinion, parody, threats und incitement. |
| `risikomatrix-ampel` | Erzeugt eine verständliche Risikoampel für Äußerungen mit Strafrecht, Zivilrecht, Plattformrisiko, arbeits- oder schulbezogenem Risiko, Beleglage, Verteidigungslinie und empfohlenem nächsten Schritt. |

## Arbeitsweg

Im Plugin Meinungsfreiheit/Persönlichkeitsrecht gilt für **Rechtsvergleich USA Risikomatrix Ampel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsvergleich-usa-supreme-court`

**Fokus:** Vergleicht deutsche Meinungsfreiheit mit der US-First-Amendment-Linie des Supreme Court: defamation, actual malice, opinion, parody, threats und incitement.

# Rechtsvergleich USA: Supreme Court

## Zweck

Dieser Skill beantwortet die Frage: "Wie würde man so etwas grob in den USA denken?" Er ist ein Vergleichswerkzeug, kein Ergebnisimport. First Amendment und Art. 5 GG sind strukturell verschieden: Die US-Linie schützt öffentliche Rede oft robuster, arbeitet aber mit eigenen Kategorien wie defamation, actual malice, public concern, true threats und incitement.

## Wann einsetzen?

- Mandant fragt nach internationaler Kommunikationsstrategie.
- Unternehmen, Plattform oder Person agiert in Deutschland und den USA.
- Es geht um public figure, Amtsträgerkritik, Satire, Parodie, tatsächliche Falschbehauptung oder Drohung.
- Schriftsatz oder Memo soll zeigen, warum US-Recht nicht einfach deutsche Beleidigungsprüfung ersetzt.

## Vergleichsprogramm

1. **Deutsche Einordnung zuerst:** Meinung/Tatsache, Art. 5 GG, Ehrschutz, Strafrecht, Zivilrecht.
2. **US-Kategorie:** public official/public figure/private person, matter of public concern, defamation, opinion, parody, threat, incitement.
3. **Fault Standard:** actual malice, negligence oder besondere Nachweise je nach Klägerstatus und Streitgegenstand.
4. **Falsity und provable fact:** Ist die Aussage als beweisbare Tatsachenbehauptung lesbar oder rhetorische Übertreibung?
5. **Sanktion:** damages, injunctive relief, criminal sanction, platform decision.
6. **Vergleichssatz:** "Nach deutscher Prüfung ..., im US-Vergleich wäre besonders relevant ..."

## Supreme-Court-Anker

- **New York Times Co. v. Sullivan, 376 U.S. 254 (1964):** Public officials müssen bei defamation actual malice zeigen.
- **Gertz v. Robert Welch, Inc., 418 U.S. 323 (1974):** Private Kläger und public concern; Staaten haben Spielraum, aber First-Amendment-Grenzen bei Schäden.
- **Hustler Magazine, Inc. v. Falwell, 485 U.S. 46 (1988):** Parodie über public figures ist stark geschützt, wenn keine falsche Tatsachenbehauptung vernünftig verstanden wird.
- **Milkovich v. Lorain Journal Co., 497 U.S. 1 (1990):** Es gibt keinen pauschalen "opinion privilege"; eine Meinung kann haftungsträchtig sein, wenn sie beweisbar falsche Tatsachen impliziert.
- **Snyder v. Phelps, 562 U.S. 443 (2011):** Rede zu matters of public concern an öffentlichem Ort kann auch bei massiver Verletzungswirkung geschützt sein.
- **United States v. Alvarez, 567 U.S. 709 (2012):** Falsche Aussagen sind nicht allein wegen ihrer Falschheit stets ungeschützt.
- **Brandenburg v. Ohio, 395 U.S. 444 (1969):** Incitement verlangt Ausrichtung auf und Wahrscheinlichkeit unmittelbar bevorstehender rechtswidriger Handlung.
- **Counterman v. Colorado, 600 U.S. 66 (2023):** True-threat-Prosekution braucht mindestens reckless mental state zur bedrohlichen Bedeutung.

## Vergleichsausgabe

```text
USA-Vergleich
- Deutsche Kernprüfung:
- Entsprechende US-Kategorie:
- Supreme-Court-Anker:
- Vermutlicher Unterschied:
- Was daraus für die Strategie folgt:
- Warnung vor unzulässiger Übertragung:
```

## Typische Vergleichssätze

- "In Deutschland bleibt der Ehrschutz über §§ 185 ff. StGB und das APR deutlich präsenter; im US-Vergleich würde bei Amtsträgerkritik stärker nach public official, falsity und actual malice gefragt."
- "Der US-Supreme-Court-Vergleich hilft hier rhetorisch, trägt aber keine deutsche Strafbarkeits- oder Unterlassungsprüfung."
- "Milkovich zeigt: Auch in den USA schützt das Label 'opinion' nicht automatisch, wenn die Äußerung eine überprüfbar falsche Tatsache transportiert."

## Quellen

Nutze für Zitate die freien US-Reports- und Supreme-Court-Links aus `rechtsprechungsbank-verifiziert`. Keine US-Law-Review- oder Kommentarzitate aus Modellwissen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `risikomatrix-ampel`

**Fokus:** Erzeugt eine verständliche Risikoampel für Äußerungen mit Strafrecht, Zivilrecht, Plattformrisiko, arbeits- oder schulbezogenem Risiko, Beleglage, Verteidigungslinie und empfohlenem nächsten Schritt.

# Risikomatrix Ampel

## Zweck

Dieser Skill verdichtet die Vollprüfung in ein schnelles Entscheidungsdokument.

## Matrix

| Bereich | Ampel | Grund | Was senkt Risiko? |
|---|---|---|---|
| Strafrecht | | | |
| Zivilrecht | | | |
| Plattform | | | |
| Arbeitsplatz/Schule | | | |
| Reputationsrisiko | | | |

## Ampelmaßstab

- **Grün:** gute Verteidigungslinie, Belege tragfähig, Sachbezug stark.
- **Gelb:** kontextabhängig, Formulierungsrisiko, Belege lückenhaft.
- **Rot:** schwerer unbelegter Tatsachenvorwurf, Prangerwirkung, bewusste Unwahrheit, reine Herabsetzung.

## Output

Gib zusätzlich:

- Top-3-Risiken.
- Top-3-Verteidigungsargumente.
- beste nächste Handlung.
- sichere Alternativfassung.
- Hinweise auf passende Skills.

## Schneller Arbeitsmodus

- Starte mit Wortlaut, Medium, Adressat, Anlass, Vor- und Nachgeschichte, Reichweite, Betroffenem und vorhandenen Belegen.
- Trenne strikt: Tatsachenbehauptung, Werturteil, gemischte Aeusserung, Satire/Spott, Schmähungs- oder Prangerkontext.
- Gewichte meinungsfreiheitsfreundlich, aber nicht blind: Sachbezug, Machtkritik, Beleglage, Formalbeleidigung, Privatbereich und Eskalationsrisiko getrennt ausweisen.
- Keine erfundene Rechtsprechung. Entscheidungen nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle nennen; sonst Recherchebedarf markieren.

## Ausgabeformat

- Ampel mit einem Satz Begruendung.
- Beste Verteidigungslinie.
- Gefaehrlichster Gegeneinwand.
- Sichere Alternativformulierung.
- Naechste Handlung: nichts tun, belegen, loeschen, klarstellen, antworten, verteidigen oder anwaltlich eskalieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
