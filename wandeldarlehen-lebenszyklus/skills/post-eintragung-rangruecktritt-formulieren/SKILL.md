---
name: post-eintragung-rangruecktritt-formulieren
description: "Post Eintragung Rangruecktritt Formulieren: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Post Eintragung Rangruecktritt Formulieren

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Post Eintragung Rangruecktritt Formulieren** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `post-eintragung-checkliste` | Nacharbeiten nach Handelsregistereintragung der Kapitalerhohung abschließen. §§ 57 40 GmbHG §§ 39 16 GmbHG Legitimationswirkung. Prüfraster: Eintragsbekanntmachung Gesellschafterliste Anteilsurkunden Investor-Cap-Table-Update Mitteilungspflichten. Output: Post-Closing-Checkliste Bestätigung. Abgrenzung: nicht für Anmeldung selbst (handelsregisteranmeldung-kapitalerhoehung). |
| `rangruecktritt-formulieren` | Rangrücktrittserklärung für Wandeldarlehen formulieren um insolvenzrechtliche Nachrang­wirkung herzustellen. § 39 InsO qualifizierter Rangrücktritt. Prüfraster: Formulierungsanforderungen BGH-Anforderungen qualifizierter Nachrang Masseverbindlichkeit Auffuellungspflicht. Output: Rangrücktrittserklärung Prüfmemo. Abgrenzung: nicht für allgemeine Darlehenskonditionen (darlehenshoehe-konditionen). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Post Eintragung Rangruecktritt Formulieren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `post-eintragung-checkliste`

**Fokus:** Nacharbeiten nach Handelsregistereintragung der Kapitalerhohung abschließen. §§ 57 40 GmbHG §§ 39 16 GmbHG Legitimationswirkung. Prüfraster: Eintragsbekanntmachung Gesellschafterliste Anteilsurkunden Investor-Cap-Table-Update Mitteilungspflichten. Output: Post-Closing-Checkliste Bestätigung. Abgrenzung: nicht für Anmeldung selbst (handelsregisteranmeldung-kapitalerhoehung).

# Post-Eintragung-Checkliste

## Zweck

Dieser Skill begleitet alle Nacharbeiten nach erfolgreicher Eintragung der Kapitalerhöhung im Handelsregister: Bestätigungen, Dokumentation, steuerliche Würdigung und Abschluss des Wandlungsprozesses. Phase D des Lebenszyklus.

## Eingaben

- Eintragungsbenachrichtigung des Handelsregisters
- Aktueller HR-Auszug (nach Eintragung)
- Neue Gesellschafterliste (wie eingereicht)
- Steuerberater-Kontakt für steuerliche Würdigung
- Lender (Empfänger der Abschlussbestätigung)

## Rechtlicher Rahmen

### Primärnormen
- § 16 Abs. 1 GmbHG (Wirksamkeit der Gesellschafterstellung ab Eintragung in HR-Gesellschafterliste)
- § 20 UmwStG (steuerliche Behandlung der Einbringung als Sacheinlage – soweit analog anwendbar)
- § 17 Abs. 1 EStG (Veräußerungsgewinn bei Anteilsübertragung – Sperrfrist-Thematik)
- § 22 UmwStG (Einbringungsgewinn – Sperrfrist sieben Jahre bei Buchwertansatz)
- § 147 AO (Aufbewahrung steuerrelevanter Unterlagen zehn Jahre)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Eintragungsbestätigung entgegennehmen
Amtliche Mitteilung des Handelsregisters dokumentieren. Datum der Eintragung ist Stichtag für: Beginn Gesellschafterrechte des Lenders, Beginn steuerliche Sperrfrist (§ 22 UmwStG).

### 2. Bestätigung an Lender senden
Schreiben: Bestätigung der Eintragung, beigefügter HR-Auszug (elektronisch), neue Gesellschafterliste, Anteilsquote, Hinweis auf Sperrfrist (§ 22 UmwStG ggf.).

### 3. Handakte aktualisieren
Kanzleiakte: Eintragungsdatum, HR-Auszug, neue Gesellschafterliste, Abschluss-Memo. Mandantenakte der Gesellschaft: vollständige Wandlungsdokumentation ablegen.

### 4. Steuerliche Behandlung klären
a) Für Lender: Einbringung der Forderung als Sacheinlage = tauschähnlicher Vorgang. Anschaffungskosten der neuen Anteile = Nennwert Forderung (EUR 275694). Sperrfrist § 22 UmwStG prüfen (falls Buchwert-Ansatz gewählt). b) Für Gesellschaft: Auflösung Verbindlichkeit Wandeldarlehen, Erhöhung Stammkapital + Kapitalrücklage → steuerneutral. c) Für Altgesellschafterinnen: Verwässerung ist keine steuerpflichtige Veräußerung.

### 5. Sperrfrist § 22 UmwStG beachten
Falls Lender die erhaltenen GmbH-Anteile innerhalb von sieben Jahren nach Einbringung veräußert, entsteht rückwirkend ein Einbringungsgewinn I (§ 22 Abs. 1 UmwStG). Lender sollte dies steuerlich planen.

### 6. Abschluss-Memo erstellen
Dokumentation: Zeitlinie (Darlehen → Wandlungsereignis → Erklärung → Beschluss → Eintragung), alle Schlüsseldaten, Beteiligte, Wandlungsberechnung, steuerliche Hinweise. Archivierung zehn Jahre.

## Abschluss-Checkliste

| Aufgabe | Erledigt |
|---|---|
| HR-Eintragung bestätigt | [ ] |
| Bestätigung an Lender versandt | [ ] |
| HR-Auszug archiviert | [ ] |
| Gesellschafterliste an alle Parteien | [ ] |
| Transparenzregister geprüft/aktualisiert | [ ] |
| Steuerberater informiert (Sacheinlage, Sperrfrist) | [ ] |
| Buchhaltung Abschluss-Buchung bestätigt | [ ] |
| Abschluss-Memo in Akte | [ ] |
| Folgevereinbarungen (SHA, IRA) eingeleitet | [ ] |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sperrfrist § 22 UmwStG nicht beachtet | Rückwirkender Einbringungsgewinn | Steuerberater nicht informiert | Lender informiert |
| Transparenzregister nach Eintragung nicht aktualisiert | GwG-Bußgeld | Verzögerung | Unmittelbar aktualisiert |
| Folgevereinbarungen (SHA/IRA) fehlen | Lender hat nur gesetzliche Rechte | In Verhandlung | Unterzeichnet |
| Keine Archivierung der Wandlungsdokumentation | Beweislosigkeit bei Streit | Teildokumentation | Vollständig archiviert |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/handelsregisteranmeldung-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung UmwStG § 22 oder EStG § 17 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, unverzügliche Einreichung) → § 16 GmbHG (Legitimationswirkung ab Listeneintragung) → § 53 GmbHG (Satzungsänderung falls erforderlich) → § 8 HGB (Handelsregisterpublizität) → § 57 Abs. 4 GmbHG (Haftung bei unrichtiger Kapitalerhöhungsanmeldung)

## 2. `rangruecktritt-formulieren`

**Fokus:** Rangrücktrittserklärung für Wandeldarlehen formulieren um insolvenzrechtliche Nachrang­wirkung herzustellen. § 39 InsO qualifizierter Rangrücktritt. Prüfraster: Formulierungsanforderungen BGH-Anforderungen qualifizierter Nachrang Masseverbindlichkeit Auffuellungspflicht. Output: Rangrücktrittserklärung Prüfmemo. Abgrenzung: nicht für allgemeine Darlehenskonditionen (darlehenshoehe-konditionen).

# Qualifizierten Rangrücktritt formulieren

## Zweck

Dieser Skill formuliert den qualifizierten Rangrücktritt für § 6 des Wandeldarlehensvertrags. Er stellt sicher, dass die Klausel sowohl die insolvenzliche Subordination (§ 39 Abs. 2 InsO) als auch die vorinsolvenzliche Durchsetzungssperre nach BGH-Rechtsprechung enthält und bilanzielle Entlastungswirkung erzielt. Phase A des Lebenszyklus.

## Eingaben

- Beteiligte Parteien (Darlehensgeber, Gesellschaft, Geschäftsführerinnen)
- Betrag des Wandeldarlehens und aufgelaufene Zinsen als Nachrangforderungen
- Gewünschte Reichweite: Zinsen miterfasst? Schadensersatz miterfasst?
- GIRA-Bestätigung an Wirtschaftsprüfer gewünscht?
- Bestehende Insolvenzreife der Gesellschaft bekannt?

## Rechtlicher Rahmen

### Primärnormen
- § 19 Abs. 2 Satz 2 InsO (Qualifizierter Rangrücktritt im Überschuldungsstatus)
- § 39 Abs. 1 Nr. 5 InsO (Nachrang eigenkapitalersetzender Gesellschafterdarlehen)
- § 39 Abs. 2 InsO (Vereinbarter Nachrang)
- § 15a InsO (Insolvenzantragspflicht – bleibt unberührt; nach SanInsFoG 2020/2021 erweitert auf alle juristischen Personen)
- § 15b InsO (Zahlungsverbote nach Insolvenzreife — durch SanInsFoG eingefügt, hat den früheren § 64 GmbHG abgelöst; Schutzklausel zwingend, da Geschäftsführerhaftung jetzt allein über § 15b InsO greift)
- § 17 InsO (Zahlungsunfähigkeit), § 19 InsO (Überschuldung; Prognosezeitraum modifiziert durch SanInsKG/SanInsFoG)
- § 44 InsO (Unwirksamkeit von Lösungsklauseln)
- § 328 BGB (Vertrag zugunsten Dritter – Aufhebungsverbot)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Insolvenzliche Subordination formulieren
Der Darlehensgeber tritt mit allen Nachrangforderungen (Rückzahlung, Zinsen, Schadensersatz) gemäß § 39 Abs. 2 InsO hinter alle Forderungen i.S.d. §§ 38 und 39 Abs. 1 Nr. 1 bis 5 InsO zurück. In einem Insolvenzverfahren: Befriedigungsrang § 39 Abs. 2 InsO.

### 2. Vorinsolvenzliche Durchsetzungssperre
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Klarstellungsklausel (BGH-Konformität)
Ausdrückliche Klarstellung, dass es sich um einen qualifizierten Rangrücktritt i.S.d. BGH-Rechtsprechung handelt, geeignet zur Beseitigung der Überschuldung gemäß § 19 Abs. 2 Satz 2 InsO.

### 4. Aufhebungsverbot (Drittschutz § 328 BGB)
Rangrücktritt als echter Vertrag zugunsten Dritter (§ 328 BGB) zugunsten aller Gläubiger i.S.d. §§ 38 / 39 Abs. 1 InsO. Aufhebung nur mit vorheriger schriftlicher Zustimmung der Gesellschaft und nur soweit keine Insolvenzreife entsteht.

### 5. § 15b InsO-Schutzklausel
Gesellschaft und Geschäftsführerinnen sind nicht zur Rückzahlung verpflichtet, soweit dies persönliche Haftung nach § 15b InsO auslösen würde. Bei verbotswidriger Rückzahlung: Rückgewährpflicht auf erstes Anfordern. Hintergrund: § 15b InsO wurde durch das SanInsFoG (Inkrafttreten 1.1.2021) eingefügt und löste § 64 GmbHG a.F. (Massesicherungspflicht) ab; die GF-Haftung für "verbotswidrige Zahlungen nach Insolvenzreife" knüpft seit der Reform allein an die InsO an. Klausel daher zwingend, sonst GF-persönliches Risiko.

### 6. GIRA-Bestätigungstext vorbereiten
Für den Wirtschaftsprüfer: kurze Bestätigungserklärung, dass qualifizierter Rangrücktritt vorliegt und Nachrangforderungen im Überschuldungsstatus nicht zu berücksichtigen sind (§ 19 Abs. 2 Satz 2 InsO; IDW S 11 Rn. 23 ff.).

## Beispielklausel (verkürzt)

```
§ 6.2 Vorinsolvenzliche Durchsetzungssperre. Außerhalb eines Insolvenzverfahrens darf der
Darlehensgeber Befriedigung der Nachrangforderungen nur aus künftigen Jahresüberschüssen,
aus einem Liquidationsüberschuss oder aus sonstigem freien Vermögen der Gesellschaft verlangen,
das die sonstigen Verbindlichkeiten der Gesellschaft übersteigt, und dies auch nur insoweit
und solange, als die teilweise oder vollständige Erfüllung weder eine Zahlungsunfähigkeit im
Sinne des § 17 InsO noch eine Überschuldung im Sinne des § 19 InsO verursacht, vertieft oder
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Keine vorinsolvenzliche Durchsetzungssperre | Rangrücktritt nur insolvenzrechtlich, nicht bilanziell wirksam | Klausel unklar formuliert | BGH-konforme Klausel vorhanden |
| Zinsen nicht in Nachrangforderungen einbezogen | Zinsen weiter fällig in Krise | Zinsen teilweise erfasst | Zinsen vollständig einbezogen |
| Aufhebungsverbot fehlt | Gläubiger nicht geschützt | Aufhebungsverbot nur schuldrechtlich | Echter Vertrag zugunsten Dritter |
| § 15b InsO-Klausel fehlt | GF-Haftungsrisiko | Klausel unvollständig | Vollständige Schutzklausel |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/sacheinlagebericht-werthaltigkeit/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/post-eintragung-checkliste/SKILL.md`

## Quellen und Updates

Stand: 05/2026.
- § 19 II 2 InsO (qualifizierter Rangruecktritt im Ueberschuldungsstatus): https://www.gesetze-im-internet.de/inso/__19.html
- § 39 I Nr. 5 InsO (Gesellschafterdarlehen-Nachrang): https://www.gesetze-im-internet.de/inso/__39.html
- § 39 II InsO (vereinbarter Nachrang): https://www.gesetze-im-internet.de/inso/__39.html
- § 15a InsO (Insolvenzantragspflicht, Hoechstfristen 3 Wochen ZU / 6 Wochen UE seit SanInsFoG): https://www.gesetze-im-internet.de/inso/__15a.html
- § 15b InsO (rechtsformneutrales Zahlungsverbot bei Insolvenzreife seit 01.01.2021 durch SanInsFoG, BGBl. I 2020, 3256; ersetzt § 64 GmbHG a.F. und § 92 II AktG a.F.): https://www.gesetze-im-internet.de/inso/__15b.html
- SanInsFoG-Gesetzgebungsmaterialien: https://www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger_BGBl&start=//*[@attr_id=%27bgbl120s3256.pdf%27]
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
