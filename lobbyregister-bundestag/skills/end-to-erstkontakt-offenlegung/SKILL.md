---
name: end-to-erstkontakt-offenlegung
description: "END TO Erstkontakt Offenlegung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# END TO Erstkontakt Offenlegung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **END TO Erstkontakt Offenlegung** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `end-to-end-registrierungswizard` | Geführter Gesamtmit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe. |
| `erstkontakt-offenlegung` | Formuliert Offenlegung beim erstmaligen Kontakt: Identität, Anliegen, Auftraggeber, Registereintrag und Verhaltenskodizes. Output Kontaktbausteine. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **END TO Erstkontakt Offenlegung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `end-to-end-registrierungswizard`

**Fokus:** Geführter Gesamtmit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe.

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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `erstkontakt-offenlegung`

**Fokus:** Formuliert Offenlegung beim erstmaligen Kontakt: Identität, Anliegen, Auftraggeber, Registereintrag und Verhaltenskodizes. Output Kontaktbausteine.

# Erstkontakt Offenlegung

## Einsatz

Sicherstellen, dass der erste Kontakt transparent und nicht irrefuehrend erfolgt.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Ist die Organisation eingetragen?
2. Wird im eigenen Namen oder fuer Auftraggeber gehandelt?
3. Welcher Satz passt fuer E-Mail, Telefon, Termin oder Veranstaltung?

## Offenlegungspflichten beim Erstkontakt (§ 5 LobbyRG + Verhaltenskodex)

Der **Verhaltenskodex** (Anlage zu § 5 LobbyRG) verlangt bei Erstkontakt mit Mandatsträgern oder Verwaltungsangehörigen folgende Informationen:

1. **Identität** der vertretenden Person und der Organisation.
2. **Auftraggeber** (falls im fremden Namen tätig).
3. **Anliegen** in Grundzügen (welches Vorhaben, welche Regelung).
4. **Lobbyregister-Eintrag**: Hinweis und ggf. Registernummer.
5. **Keine Identitätsverschleierung** (Verbot der Tarnung als Bürgerinitiative o. Ä.).

## Bausteine für verschiedene Kommunikationskanäle

### E-Mail (Erstkontakt)

> Sehr geehrte/r [Name],
>
> mein Name ist [Vor- und Nachname], ich bin [Funktion] bei [Organisationsname]. Wir sind im Lobbyregister des Deutschen Bundestages mit der Registernummer [R...] eingetragen.
>
> Ich vertrete die Interessen [unseres Unternehmens / Auftraggebers Name] im Hinblick auf [Vorhaben / Regelung]. Ich würde mich freuen, mit Ihnen [Anliegen konkret] zu erörtern.
>
> Über einen kurzen Gesprächstermin freuen wir uns.
>
> Mit freundlichen Grüßen
> [Unterschrift]

### Telefonnotiz / Vorstellung

> "[Vorname Name] von [Organisation]; wir sind im Lobbyregister Nr. [R...] eingetragen. Ich rufe wegen [Vorhaben] an und vertrete [Auftraggeber / eigene Interessen]."

### Meeting-Eröffnung (Live)

> "Bevor wir inhaltlich beginnen: Mein Name ist [..], ich vertrete [..]. Wir sind im Lobbyregister eingetragen, Nummer [R..]. Heute geht es uns um [Vorhaben]."

### Veranstaltung / Empfang

> Stehauftritt mit kurzer Selbstvorstellung; Visitenkarte mit Registernummer; bei längeren Gesprächen Anliegen offenlegen.

## Verhaltenskodex-Pflichten im Erstkontakt

- **Wahrheitsgemäße Identitätsangabe** (keine Strohmänner / Fake-Initiativen).
- **Keine unzulässige Einflussnahme** (Geschenke, Versprechen von Vorteilen).
- **Keine Anwendung von Druck** oder Drohungen.
- **Vertraulichkeit** über Inhalte aus internen Beratungen.
- **Keine Pflicht zur Offenlegung** des Detailauftrags, aber Pflicht zur Identifikation des Auftraggebers.

## Praxisfallen

- **Identitätsverschleierung** (Verein der Bürger gegen X, der tatsächlich Industrie-finanziert ist) — verstößt klar gegen Verhaltenskodex und kann OWi sein (§ 7 I Nr. 3 LobbyRG).
- **Keine Registereintragung trotz Pflicht** = Erstkontakt rechtswidrig, möglicher Bußgeldgrund.
- **Adressaten verlangen Belegt** der Registereintragung: stets Nummer parat haben.
- **Anwaltliche Mandatsangelegenheit** (§ 2 II Nr. 9 LobbyRG): bei reiner Rechtsangelegenheit Ausnahme, aber nicht bei politischer Lobby für den Mandanten.
- **Dolmetscher / Mitarbeitende** bei Vertretung: zur Identifikation und Funktion benennen.
- **Schriftliche Nachfassung**: Inhalt der Kontaktaufnahme dokumentieren — bei Anfrage durch Aufsicht Beweis möglich.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Kontaktbausteine fuer E-Mail, Telefonnotiz, Meeting-Intro und Nachfassmail mit Pruefhinweis.

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
