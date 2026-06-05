---
name: jahresabschluss-rechenschaftsbericht-konzern
description: "Jahresabschluss Rechenschaftsbericht Konzern: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Jahresabschluss Rechenschaftsbericht Konzern

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Jahresabschluss Rechenschaftsbericht Konzern** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jahresabschluss-rechenschaftsbericht` | Prüft Bereitstellung von Jahresabschluss oder Rechenschaftsbericht, Umgang mit noch nicht aufgestellten Unterlagen und Nachreichpflicht. Output Abschluss-Uploadplan. |
| `konzern-netzwerk-plattform` | Strukturiert Lobbyregisterfragen bei Konzernen, Verbaenden, losen Netzwerken, Plattformen und sonstigen kollektiven Tätigkeiten. Output Eintragungseinheiten-Map. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Jahresabschluss Rechenschaftsbericht Konzern**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jahresabschluss-rechenschaftsbericht`

**Fokus:** Prüft Bereitstellung von Jahresabschluss oder Rechenschaftsbericht, Umgang mit noch nicht aufgestellten Unterlagen und Nachreichpflicht. Output Abschluss-Uploadplan.

# Jahresabschluss und Rechenschaftsbericht

## Einsatz

Finanzdokumente frist- und portalfaehig vorbereiten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welches Geschaeftsjahr ist abgeschlossen?
2. Liegt der Abschluss bereits vor?
3. Welche Ersatzangaben oder Nachreichpflichten entstehen?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Abschluss-Uploadplan mit Datei, Stand, Nachreichtrigger, Freigabe und Risikohinweis.

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

## 2. `konzern-netzwerk-plattform`

**Fokus:** Strukturiert Lobbyregisterfragen bei Konzernen, Verbaenden, losen Netzwerken, Plattformen und sonstigen kollektiven Tätigkeiten. Output Eintragungseinheiten-Map.

# Konzern, Netzwerk und Plattform

## Einsatz

Mehrgliedrige Strukturen so aufbereiten, dass Eintragungseinheiten nicht verschwimmen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Einheit steuert Interessenvertretung?
2. Wer hat eigene Kontakte, Budgets, Auftraggeber oder Aussenauftritt?
3. Welche Netzwerkteilnehmer werden nur intern koordiniert?

## Quellenanker

## Spezialfall doppelte Sichtbarkeit ohne doppelte Rechtsperson

Bei Konzern, Netzwerk oder Zweigniederlassung kann Transparenz praktisch mehr als eine Anschrift oder Organisationseinheit verlangen, rechtlich aber nur ein Rechtstraeger handeln. Der Skill soll deshalb eine Eintragungseinheiten-Map erzeugen: Rechtstraeger, Niederlassung, betraute Personen, Auftraggeber, Kostenstelle und Kontaktkanal. Wenn Portal- oder Registerpraxis unklar ist, wird eine Anfrage an die registerfuehrende Stelle empfohlen.

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Eintragungseinheiten-Map mit Verantwortungsbereich, Rollen und offenen Strukturfragen.

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
