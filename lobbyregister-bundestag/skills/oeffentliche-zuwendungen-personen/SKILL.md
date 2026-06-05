---
name: oeffentliche-zuwendungen-personen
description: "Oeffentliche Zuwendungen Personen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Oeffentliche Zuwendungen Personen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Oeffentliche Zuwendungen Personen** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `oeffentliche-zuwendungen` | Prüft Zuwendungen und Zuschuesse der deutschen öffentlichen Hand, EU, Mitgliedstaaten oder Drittstaaten mit Schwelle je Geber. Output Zuwendungsliste. |
| `personen-organisationstyp` | Bestimmt, ob natuerliche Person, juristische Person, Personengesellschaft, Einzelkaufmann, Netzwerk, Plattform oder sonstige Organisation einzutragen ist. Output Typenentscheidung. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Oeffentliche Zuwendungen Personen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `oeffentliche-zuwendungen`

**Fokus:** Prüft Zuwendungen und Zuschuesse der deutschen öffentlichen Hand, EU, Mitgliedstaaten oder Drittstaaten mit Schwelle je Geber. Output Zuwendungsliste.

# Oeffentliche Zuwendungen

## Einsatz

Oeffentliche Finanzierungen richtig einzeln oder gesammelt erfassen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche oeffentlichen Stellen haben gezahlt?
2. Ueberschreiten Zahlungen je Geber den relevanten Schwellenwert?
3. Wie ist die Leistung kurz zu beschreiben?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Zuwendungsliste mit Geber, Betrag, Zweck, Beschreibung, Beleg und Portaltext.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `personen-organisationstyp`

**Fokus:** Bestimmt, ob natuerliche Person, juristische Person, Personengesellschaft, Einzelkaufmann, Netzwerk, Plattform oder sonstige Organisation einzutragen ist. Output Typenentscheidung.

# Personen- und Organisationstyp

## Einsatz

Den richtigen Registertraeger auswaehlen, damit nicht Einzelpersonen falsch registriert werden.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wer tritt nach aussen auf?
2. Handelt eine Person im eigenen Namen oder fuer eine Organisation?
3. Gibt es mehrere Traeger, Netzwerkpartner oder Plattformstrukturen?

## Quellenanker

## Spezialfall Auslandsrechtstraeger mit deutscher Zweigniederlassung

Bei einer unselbststaendigen Zweigniederlassung ist zuerst der Rechtstraeger zu bestimmen. Die Handelsregistereintragung der Zweigniederlassung macht sie nicht automatisch zu einer eigenen juristischen Person. Der Skill soll deshalb die Eintragungseinheit, die Frankfurter oder Berliner Anschrift, die betrauten Personen und die Kosten-/Taetigkeitszuordnung auseinanderhalten. Eine zweite Registrierung der Zweigniederlassung darf nur als Pruefoption vorbereitet werden, nicht als selbstverstaendlicher Portal-Schritt.

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Typenentscheidung mit Portal-Kategorie, Nachweisen und Abgrenzung zu betreuten Personen.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
