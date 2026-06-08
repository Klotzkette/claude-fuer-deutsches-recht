---
name: end-to-erstkontakt-offenlegung
description: "Geführter Gesamtmit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe im Lobbyregister Bundestag: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# End-to-End Registrierungswizard

## Arbeitsbereich

Geführter Gesamtmit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 3 LobbyRG Eintragung vor erster Interessenvertretung, § 5 LobbyRG jährliche Aktualisierung, Berichtspflicht ggf. innerhalb 3 Monaten nach Ende des Geschäftsjahres.
- Tragende Normen verifizieren: LobbyRG §§ 1, 2, 3, 5, 6, 7, 8 (i.d.F. Reform 2024), Verhaltenskodex Lobbyregister, GOBT, BGleiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Interessenvertreter, Bundestagsverwaltung (Lobbyregisterstelle), Geschäftsstelle, registrierte Verbände, Bundesregierung (zweiter Registerteil).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lobbyregistereintrag, Verhaltenskodex-Bestätigung, Tätigkeitsbericht, Hausausweisantrag, Finanzangaben, Verbandsmitgliederliste — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Einsatz

Nutzer Schritt für Schritt bis zu einem prueffaehigen Registereintrag fuehren.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Soll das System nur pruefen oder auch eine Registrierungsmappe erzeugen?
2. Welche Daten fehlen noch?
3. Wer gibt den Eintrag final frei?

## Wizard-Phasen

1. **Pflichtentscheidung:** `interessenvertretung-begriff`, `adressatenkreis-bundestag-bundesregierung`, `registrierungspflicht-schwellen`, danach Ausnahmen.
2. **Traeger und Personen:** `personen-organisationstyp`, `vertretungsberechtigte-personen`, `betraute-personen`, `drehtuer-angaben`.
3. **Inhalt der Interessenvertretung:** `taetigkeitsbeschreibung`, `interessen-und-vorhabenbereiche`, `regelungsvorhaben-erfassen`, `stellungnahmen-gutachten-upload`.
4. **Auftrag und Geld:** `auftraggeber-ermitteln`, `unterauftragnehmer-erfassen`, `finanzaufwendungen-berechnen`, `hauptfinanzierungsquellen`, `öffentliche-zuwendungen`, `schenkungen-sponsoring`, `jahresabschluss-rechenschaftsbericht`.
5. **Portal und Freigabe:** `portal-account-rollen`, `erstregistrierung-ausfuellen`, `bestaetigungsdokument-freigabe`, `registereintrag-finalcheck`.
6. **Betrieb:** `fristen-und-quartalsmonitor`, `aktualisierung-unverzueglich`, `geschaeftsjahresaktualisierung`, `verhaltenskodex-integritaet`, `dokumentationsakte-revisionsspur`.
7. **Open Data und API:** `suche-open-data-monitor`, `benachrichtigungskonto-monitor`, Registerexport-Diff, Dublettencheck, API-Nachkontrolle und Watchlist.

## Stop-Regeln

- Stop, wenn der Pflichtgrund unklar ist und eine Registrierungspflicht realistisch sein kann.
- Stop, wenn Pflichtfelder auf Schaetzungen ohne Verantwortliche beruhen.
- Stop, wenn Finanzdaten nicht auf ein Geschaeftsjahr und eine Methode zurueckgefuehrt werden koennen.
- Stop, wenn die Freigabeperson nicht zur Rechtsform passt.
- Stop, wenn ein Regelungsvorhaben bereits kontaktrelevant ist, aber im Register noch fehlt.
- Stop, wenn die Nutzerin eine API-Einreichung erwartet, obwohl nur ein lesender Zugriff auf öffentliche Registerdaten dokumentiert ist.
- Stop, wenn eine API-Abweichung rechtlich relevant sein kann und noch keine Portalaktion oder RfS-Anfrage definiert ist.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-für-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Registrierungsmappe mit Pflichtanalyse, Portaltexten, Anlagen, Fristen, Freigaben, JSON-Mapping, API-Nachkontrolle, Monitoringplan und Qualitaetsgate.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Der Wizard trennt Portalaktion, API-Kontrolle und Monitoring konsequent.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
