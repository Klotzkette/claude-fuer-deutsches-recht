---
name: ausnahmen-bundesregierung-bundestag
description: "Ausnahmen Bundesregierung, Ausnahmen Bundestag: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ausnahmen Bundesregierung, Ausnahmen Bundestag

## Arbeitsbereich

Dieser Skill bündelt **Ausnahmen Bundesregierung, Ausnahmen Bundestag** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ausnahmen-bundesregierung` | Prüft Ausnahmen bei Interessenvertretung gegenüber Bundesregierung und Ministerien nach § 2 Abs. 3 LobbyRG, einschließlich Buergeranfragen, Sachverständigengremien und Ersuchen. Output Ausnahmeprüfung. |
| `ausnahmen-bundestag` | Prüft die Ausnahmen von der Registrierungspflicht bei Interessenvertretung gegenüber Bundestagsadressaten nach § 2 Abs. 2 LobbyRG. Output Ausnahmegutachten kurz mit Restpflichten. |

## Arbeitsweg

Für **Ausnahmen Bundesregierung, Ausnahmen Bundestag** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `lobbyregister-bundestag` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ausnahmen-bundesregierung`

**Fokus:** Prüft Ausnahmen bei Interessenvertretung gegenüber Bundesregierung und Ministerien nach § 2 Abs. 3 LobbyRG, einschließlich Buergeranfragen, Sachverständigengremien und Ersuchen. Output Ausnahmeprüfung.

# Ausnahmen Bundesregierung

## Einsatz

Regierungs- und Ministerialkontakte nach eigenen Ausnahmevorschriften einordnen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Ausnahmenkanon § 2 LobbyRG (Stand prüfen)

- **§ 2 Abs. 2 LobbyRG — Tätigkeitsbezogene Ausnahmen:** u. a. Stellungnahmen aufgrund Beteiligung in Gesetzgebung (z. B. § 47 Abs. 3 GGO), Auskunft auf Verlangen von Bundestag/Bundesregierung, anwaltliche oder anwaltsähnliche Mandate in konkreten Verfahren, Sozialpartnerdialog, Petitionen.
- **§ 2 Abs. 3 LobbyRG — Persönliche/strukturelle Ausnahmen:** Hauptkommunal/-länderebenen, Religionsgemeinschaften des öffentlichen Rechts, politische Parteien, einzelne Bürgeranfragen, Wissenschaftsbetrieb auf Forschungsbasis.
- **§ 2 Abs. 1 LobbyRG — Registrierungsschwelle:** Eintragungspflicht bei regelmäßiger, auf Dauer angelegter, geschäftsmäßiger oder gegen Gegenleistung beauftragter Interessenvertretung sowie bei mehr als 30 unterschiedlichen Interessenvertretungskontakten in den jeweils letzten drei Monaten. Die alte 100.000-Euro-Schwelle nicht fortschreiben; aktuelle Fassung live prüfen.
- **Wichtig:** Auch nicht eintragungspflichtige Interessenvertretung kann freiwillig registriert werden; dafür den aktuellen § 2 LobbyRG und den Pflichtkanon nach § 3 LobbyRG live prüfen, nicht die Definitionsnorm für Interessenvertreter als Freiwilligkeitsnorm zitieren.
- **Strafe/Bußgeld:** Bei vorsätzlich falschen Angaben § 7 LobbyRG (bis 50.000 Euro); zusätzlich Verlust der Anhörungsmöglichkeit und Veröffentlichung im Register.

## Leitfragen

1. Welche Regierungsebene ist adressiert?
2. Liegt ein individuelles Ersuchen um Daten oder Fachwissen vor?
3. Ist die Taetigkeit Teil eines eingerichteten Expertengremiums?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Ausnahmepruefung mit Scope, verbleibenden Transparenzpflichten und Aktualisierungsbedarf.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.

## 2. `ausnahmen-bundestag`

**Fokus:** Prüft die Ausnahmen von der Registrierungspflicht bei Interessenvertretung gegenüber Bundestagsadressaten nach § 2 Abs. 2 LobbyRG. Output Ausnahmegutachten kurz mit Restpflichten.

# Ausnahmen Bundestag

## Einsatz

Bundestagskontakte sauber von Registrierungspflicht-Ausnahmen trennen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Geht es um persoenliche Interessen, Petition, oeffentliche Anhoerung oder Ersuchen um Sachinformation?
2. Ist das Anliegen ausschliesslich lokal?
3. Handelt eine Koerperschaft oeffentlichen Rechts oder ein Sozialpartner?

## Ausnahmekatalog § 2 II LobbyRG (Bundestag)

Keine Interessenvertretung im Sinne des LobbyRG (und damit keine Registrierungspflicht) bei:

- **Nr. 1**: Tätigkeit von **Sozialpartnern** (Gewerkschaften und Arbeitgebervereinigungen) im Rahmen der Tarifautonomie nach Art. 9 III GG.
- **Nr. 2**: Tätigkeit von **Kirchen und Religionsgemeinschaften** im Rahmen ihres Selbstbestimmungsrechts nach Art. 140 GG i. V. m. Art. 137 III WRV.
- **Nr. 3**: Tätigkeit von **politischen Parteien** im Sinne von Art. 21 GG / § 2 PartG, soweit sie ihre Aufgaben nach Art. 21 GG wahrnehmen.
- **Nr. 4**: **Petitionen** nach Art. 17 GG (an Volksvertretung); Anliegen gegenüber Bundestagsausschüssen.
- **Nr. 5**: **persönliche Anliegen** (z. B. Bürgerin schreibt an MdB in eigener Angelegenheit).
- **Nr. 6**: Ersuchen um **Sachinformation** durch Bundestag/Abgeordnete (z. B. öffentliche Anhörung als Sachverständiger).
- **Nr. 7**: ausschließlich **lokale Interessenvertretung** (Bezirk, Kommune, Region — nicht Bundesangelegenheit).
- **Nr. 8**: Tätigkeit von **Körperschaften und Anstalten des öffentlichen Rechts**.
- **Nr. 9**: Anwaltliche Tätigkeit der **anwaltlichen Vertretung** in konkreten Mandantenangelegenheiten gegenüber Bundestagsverwaltung (nicht aber politische Lobbyarbeit).
- **Nr. 10**: Tätigkeit von **diplomatischen Vertretungen** ausländischer Staaten und internationaler Organisationen.

## Restpflichten trotz Ausnahme

- **Verhaltenskodex** § 5 LobbyRG kann auch für Ausnahmefälle relevant sein (Identitätsoffenlegung beim Kontakt).
- **Freiwillige Registrierung** § 2 Abs. 5 LobbyRG bleibt möglich; kann Sichtbarkeit und Vertrauen erhöhen, löst aber eigene Richtigkeits- und Vollständigkeitspflichten aus.
- **PartG-Pflichten** (Spenden, Sponsoring) bleiben unberührt vom LobbyRG.
- **AbgG-Pflichten** für Adressaten (Abgeordnete) bleiben bestehen — insb. § 44a AbgG zur Veröffentlichung entgeltlicher Interessenvertretung.

## Praxisfallen

- **Gemischte Tätigkeit**: Wer teils unter Ausnahme fällt, teils nicht, muss insgesamt registrieren, soweit nicht ausnahmsweise tätig.
- **Lokales Anliegen** vs. Bundesangelegenheit: Sobald Wirkung über kommunalen Bereich hinausreicht, keine Ausnahme.
- **Petitionen** sind ausgenommen, aber: ständige systematische "Petitionsversendungen" als Lobbystrategie können in Pflicht fallen.
- **Stiftungen und Vereine** sind nicht per se ausgenommen; Pflicht zu prüfen.
- **Kirche** ist ausgenommen, **kirchliche Wohlfahrtsverbände** (Caritas, Diakonie) nicht zwingend — Selbstbestimmungsrecht reicht nur soweit Glaubens-/Kultusbezug.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Ausnahmepruefung mit Tatbestand, Reichweite, Belegen und freiwilliger Registrierung als Option.

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
