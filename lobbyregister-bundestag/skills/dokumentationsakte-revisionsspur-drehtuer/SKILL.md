---
name: dokumentationsakte-revisionsspur-drehtuer
description: "Dokumentationsakte Revisionsspur Drehtuer: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dokumentationsakte Revisionsspur Drehtuer

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Dokumentationsakte Revisionsspur Drehtuer** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dokumentationsakte-revisionsspur` | Baut Aktenstruktur für Belege, Freigaben, Portal-Screenshots, Kontaktlogs, Kostenmethodik, RfS-Kommunikation und Jahresupdates. Output Aktenplan. |
| `drehtuer-angaben` | Führt durch Angaben zu Mandat, Amt oder Funktion in Bundestag, Bundesregierung oder Bundesverwaltung aktuell oder in den letzten fuenf Jahren. Output Drehtuer-Prüfprotokoll. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Dokumentationsakte Revisionsspur Drehtuer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dokumentationsakte-revisionsspur`

**Fokus:** Baut Aktenstruktur für Belege, Freigaben, Portal-Screenshots, Kontaktlogs, Kostenmethodik, RfS-Kommunikation und Jahresupdates. Output Aktenplan.

# Dokumentationsakte und Revisionsspur

## Einsatz

Die Registerarbeit spaeter nachvollziehbar beweisen koennen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Belege liegen wo?
2. Welche Entscheidungen wurden von wem freigegeben?
3. Welche Portalaktionen muessen dokumentiert werden?
4. Welche API- oder JSON-Exportantworten belegen den oeffentlichen Datenstand?

## API-Revisionsspur

Fuer jeden API- oder JSON-Export muss die Akte enthalten:

- Abrufdatum und `sourceDate`
- verwendeter Endpunkt, Suchparameter und Cursor
- Registernummer, Version, `detailsPageUrl` und `pdfUrl`
- Hash oder unveraenderte Rohdatei
- Bearbeiterin/Bearbeiter
- Zweck der Abfrage
- Verweis auf den dazugehoerigen Portalvorgang oder Monitoringlauf
- Bewertung, ob eine Abweichung rechtlich, technisch oder nur formal ist

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Aktenplan mit Ordnerstruktur, Namensschema, Mindestbelegen, API-Rohdatenablage, Aufbewahrung und Pruefspur.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- API-Antworten werden unveraendert archiviert und nicht mit internen Arbeitshypothesen vermischt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `drehtuer-angaben`

**Fokus:** Führt durch Angaben zu Mandat, Amt oder Funktion in Bundestag, Bundesregierung oder Bundesverwaltung aktuell oder in den letzten fuenf Jahren. Output Drehtuer-Prüfprotokoll.

# Drehtuer-Angaben

## Einsatz

Drehtuerangaben fuer alle namentlich genannten Personen konsistent erfassen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche aktuellen oder frueheren Aemter liegen vor?
2. Betreffen sie Bundestag, Bundesregierung oder Bundesverwaltung?
3. Seit wann und bis wann bestand die Funktion?

## Drehtür-Pflicht § 3 I Nr. 4 LobbyRG (Pflichtangabe)

**Anzugebende Personen** (für jede namentlich genannte natürliche Person):

1. **aktuelles Mandat** im Deutschen Bundestag oder im Europäischen Parlament,
2. **aktuelles Amt** als Bundesminister oder Parlamentarischer Staatssekretär oder Staatsminister,
3. **in den letzten 5 Jahren bestehende** Tätigkeit als Mitglied
 - der Bundesregierung,
 - des Deutschen Bundestages,
 - als Parlamentarischer Staatssekretär,
 - als Beamter/Soldat ab Besoldungsgruppe B 3 bzw. äquivalenter Funktion
4. Für **Beschäftigte und Beauftragte** (§ 1 III LobbyRG): die zur Interessenvertretung tätigen Personen (auch bei mittelbarer Beauftragung).

## Pflicht-Datensatz im Portal

- **Vor- und Nachname** der Person.
- **Funktion / Amt** der vergangenen Tätigkeit (z. B. „Staatssekretär im BMI", „MdB").
- **Zeitraum** der Tätigkeit (Beginn und Ende, ggf. „bis dato").
- Ggf. **Aktualität** (laufend / abgeschlossen).

## Rechtsfolgen / Sanktionen

- Verstoß = OWi § 7 I Nr. 1, 2 LobbyRG (bis 50.000 Euro Bußgeld).
- Eintragung im Register als „nicht vollständig" / "nicht aktuell" möglich (Reputationsrisiko).

## Karenzpflichten / Cooling-Off-Period

- **Ehemalige Bundesregierungsmitglieder** § 6b BMinG / KarenzG: Karenzzeit von bis zu 18 Monaten für Tätigkeiten, bei denen öffentliche Interessen betroffen sein können; Entscheidung Bundesregierung nach Anhörung beratenden Gremiums.
- **Ehemalige Beamte** § 105 BBG / § 41 BeamtStG: Anzeigepflicht bei beruflicher Tätigkeit im Anschluss an aktive Tätigkeit, soweit Bezug zu früherer Amtsführung.
- LobbyRG-Pflicht und Karenzpflichten sind unabhängig — beide können nebeneinander treten.

## Praxisfallen

- **Privatperson, die im Auftrag interessenvertretung macht**, ist „Beschäftigte" oder „Beauftragte" — Drehtür-Angaben fließen in das Profil der Organisation.
- **Bundestagspraktika, Wahlkreismitarbeit** unter Besoldungsgruppe sind grundsätzlich nicht meldepflichtig; aber Vorsicht bei Stellung als Geschäftsführer einer politischen Stiftung etc.
- **Beratungsverhältnis durch Berufsexpertin** (z. B. ehemalige Staatssekretärin als externe Beraterin): Drehtür-Angabe der Beraterin ist Pflicht, wenn sie als Beauftragte für die Lobbyorganisation tätig wird.
- **Aktualisierung** § 3 Abs. 3 LobbyRG: Änderungen innerhalb von 30 Tagen.
- **EU-Ebene**: Tätigkeit als ehemaliges Mitglied EP / Kommission separat zu vermelden.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Drehtuer-Pruefprotokoll mit Person, Funktion, Zeitraum, Quelle und Portalformulierung.

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
