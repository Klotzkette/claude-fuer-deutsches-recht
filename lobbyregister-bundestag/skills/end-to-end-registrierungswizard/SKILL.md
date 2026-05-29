---
name: end-to-end-registrierungswizard
description: "Geführter Gesamtworkflow mit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe."
---

# End-to-End Registrierungswizard

## Einsatz

Nutzer Schritt fuer Schritt bis zu einem prueffaehigen Registereintrag fuehren.

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
4. **Auftrag und Geld:** `auftraggeber-ermitteln`, `unterauftragnehmer-erfassen`, `finanzaufwendungen-berechnen`, `hauptfinanzierungsquellen`, `oeffentliche-zuwendungen`, `schenkungen-sponsoring`, `jahresabschluss-rechenschaftsbericht`.
5. **Portal und Freigabe:** `portal-account-rollen`, `erstregistrierung-ausfuellen`, `bestaetigungsdokument-freigabe`, `registereintrag-finalcheck`.
6. **Betrieb:** `fristen-und-quartalsmonitor`, `aktualisierung-unverzueglich`, `geschaeftsjahresaktualisierung`, `verhaltenskodex-integritaet`, `dokumentationsakte-revisionsspur`.
7. **Open Data und API:** `suche-open-data-monitor`, `benachrichtigungskonto-monitor`, Registerexport-Diff, Dublettencheck, API-Nachkontrolle und Watchlist.

## Stop-Regeln

- Stop, wenn der Pflichtgrund unklar ist und eine Registrierungspflicht realistisch sein kann.
- Stop, wenn Pflichtfelder auf Schaetzungen ohne Verantwortliche beruhen.
- Stop, wenn Finanzdaten nicht auf ein Geschaeftsjahr und eine Methode zurueckgefuehrt werden koennen.
- Stop, wenn die Freigabeperson nicht zur Rechtsform passt.
- Stop, wenn ein Regelungsvorhaben bereits kontaktrelevant ist, aber im Register noch fehlt.
- Stop, wenn die Nutzerin eine API-Einreichung erwartet, obwohl nur ein lesender Zugriff auf oeffentliche Registerdaten dokumentiert ist.
- Stop, wenn eine API-Abweichung rechtlich relevant sein kann und noch keine Portalaktion oder RfS-Anfrage definiert ist.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
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
