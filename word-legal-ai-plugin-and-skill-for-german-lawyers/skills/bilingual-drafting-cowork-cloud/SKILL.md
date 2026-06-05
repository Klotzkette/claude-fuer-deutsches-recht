---
name: bilingual-drafting-cowork-cloud
description: "Bilingual Drafting Cowork Cloud: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bilingual Drafting Cowork Cloud

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Bilingual Drafting Cowork Cloud** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bilingual-drafting-deutsch-englisch` | Drafting deutsch-englischer Vertraege in Side-by-Side- oder Stacked-Layout. Bestimmt den Anwendungsfall (true bilingual, sovereign language, courtesy translation), waehlt das Layout (Tabelle zweispaltig oder gestapelte Saetze), klaert die Sprachklausel (welche Fassung verbindlich), uebersetzt Boilerplate-Klauseln in beiden Richtungen, vermeidet False Friends (Indemnify, Reasonable, Consequential Damages, Best Efforts, Force Majeure, Severability, Schiedsklausel, Hauptleistung), waehlt Word-Tabellenformat oder gestapeltes Layout, behaelt Definitionen synchron und liefert eine Pruefcheckliste fuer Konsistenz. |
| `cowork-cloud-kollaboration-drafting` | Mandantengeheimnis-konformes Drafting in der Cloud (Claude Cowork; Office 365; Google Workspace). Rechtlicher Rahmen § 43a Abs. 2 BRAO; § 203 StGB; § 26 BORA und Art. 28 DSGVO. Auftragsverarbeitungsvertrag ist Voraussetzung. Sensible Daten: Mandantenname; Aktenzeichen; Sachverhalt. Pseudonymisierung im Entwurf; Mandantendaten erst in finaler Fassung. Versionierung. Zwei-Faktor-Authentifizierung. Mit Pitfall-Liste zu WhatsApp; E-Mail und Cloud ohne Auftragsverarbeitungsvertrag. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Bilingual Drafting Cowork Cloud**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bilingual-drafting-deutsch-englisch`

**Fokus:** Drafting deutsch-englischer Vertraege in Side-by-Side- oder Stacked-Layout. Bestimmt den Anwendungsfall (true bilingual, sovereign language, courtesy translation), waehlt das Layout (Tabelle zweispaltig oder gestapelte Saetze), klaert die Sprachklausel (welche Fassung verbindlich), uebersetzt Boilerplate-Klauseln in beiden Richtungen, vermeidet False Friends (Indemnify, Reasonable, Consequential Damages, Best Efforts, Force Majeure, Severability, Schiedsklausel, Hauptleistung), waehlt Word-Tabellenformat oder gestapeltes Layout, behaelt Definitionen synchron und liefert eine Pruefcheckliste fuer Konsistenz.

# Bilinguales Drafting Deutsch-Englisch

## Zweck

Im deutschen Wirtschaftsrecht sind bilinguale Vertraege Standard, sobald eine Partei nicht-deutschsprachig ist oder im internationalen Geschaeft taetig ist. Dieser Skill fuehrt durch die drei Hauptfragen:

1. **Anwendungsfall**: true bilingual (beide Fassungen gleichwertig), sovereign language (eine ist verbindlich), oder courtesy translation (eine ist nur informativ).
2. **Layout**: Tabelle zweispaltig (Side-by-Side) oder gestapelte Saetze (Stacked).
3. **Sprachklausel**: Welche Fassung gilt bei Widerspruch.

Er bietet Uebersetzungsvorlagen fuer alle Standardklauseln und warnt vor den False Friends, die in deutschen Anwaltsbueros regelmaessig zu falschen Uebersetzungen fuehren.

## Eingaben

- Vertragstyp und Branche
- Sprachen der Parteien (Muttersprache, Vertragsverhandlungssprache)
- Streitloesungsforum (deutsches Gericht, US-Court, ICC, DIS, neutraler dritter Staat)
- Vorgabe zur Verbindlichkeit der Fassungen
- Bestehende Vorlagen oder Mustervertraege

## Rechtlicher und methodischer Rahmen

- **Vertragssprache**: Privatautonomie. Parteien koennen frei waehlen.
- **Anwendbares Recht**: Rom I-VO. Bei B2C-Vertraegen Verbraucherschutz im Land des gewoehnlichen Aufenthalts (Art. 6 Rom I-VO).
- **§ 184 GVG**: Gerichtssprache deutscher Gerichte ist Deutsch. Bei englischen Vertraegen vor deutschen Gerichten: Uebersetzung erforderlich, Kosten regelmaessig zulasten der vorlegenden Partei. Vereinzelte Spezialkammern fuer englischsprachige Verfahren (Hamburg, Frankfurt, Stuttgart).
- **§ 293 ZPO**: Auslaendisches Recht muss bewiesen werden. Sachverstaendigengutachten regelmaessig erforderlich, Kosten 10.000 EUR aufwaerts.
- **CISG (UN-Kaufrecht)**: Bei grenzueberschreitendem Warenkauf automatisch anwendbar, soweit nicht ausgeschlossen.

## Drei Anwendungsfaelle

### True bilingual (beide Fassungen gleichwertig)

- Beide Sprachen rechtlich verbindlich.
- Bei Widerspruch: Auslegung nach Treu und Glauben (§§ 133, 157 BGB) oder vereinbarter Auslegungsregel.
- Hoechster Drafting-Aufwand: jede Aenderung in beiden Fassungen.
- Sinnvoll bei symmetrischen Partnerschaften, internationalen Joint Ventures.

**Sprachklausel:** "Dieser Vertrag ist in deutscher und englischer Sprache abgefasst. Beide Fassungen sind gleichermassen verbindlich. Im Falle eines Widerspruchs zwischen den beiden Fassungen sind die Bestimmungen so auszulegen, wie sie dem gemeinsamen wirtschaftlichen Zweck am besten entsprechen. // This Agreement is executed in both German and English. Both versions shall be equally binding. In the event of a conflict between the two versions, the provisions shall be interpreted in a manner that best reflects the common commercial purpose."

### Sovereign language (eine verbindlich, eine nachrangig)

- Standard im deutschen Wirtschaftsrecht: deutsche Fassung verbindlich, englische Fassung Nachrang.
- Bei US/UK-Vertragspartnern oft umgekehrt.
- Bei Widerspruch: Vorrang der bezeichneten Fassung.
- Sinnvoll bei klarer Verhandlungsmacht oder klarem Forum.

**Sprachklausel (deutsch verbindlich):** "Dieser Vertrag ist in deutscher und englischer Sprache abgefasst. Im Falle eines Widerspruchs zwischen den beiden Fassungen ist die deutsche Fassung verbindlich. // This Agreement is executed in both German and English. In the event of a conflict between the two versions, the German version shall prevail."

### Courtesy translation (eine nur informativ)

- Eine Sprache ist verbindlich, die andere wird ausschliesslich zur Information beigefuegt.
- Niedriger Drafting-Aufwand bei Aenderungen (nur die verbindliche Fassung ist relevant).
- Risiko: Uebersetzung kann irrefuehrend sein, der Mandant unterschreibt im Vertrauen auf die Uebersetzung.

**Sprachklausel:** "Dieser Vertrag ist in deutscher Sprache verbindlich. Die englische Fassung ist eine reine Hoeflichkeitsuebersetzung ohne Rechtswirkung. // This Agreement is binding in its German version. The English version is a courtesy translation only and has no legal effect."

## Layout

### Tabelle zweispaltig (Side-by-Side)

| Vorteil | Nachteil |
|---|---|
| Direkte Vergleichbarkeit | Schwierig bei langen Saetzen |
| Sauber druckbar | Word-Tabellen werden bei Track Changes unuebersichtlich |
| Klarheit fuer Verhandler | Hoeher Drafting-Aufwand |

Wenn Side-by-Side, dann zweispaltige Tabelle ohne Rahmen, Spaltenbreite 50:50, Zeilenabstand 1,15. Jeder Vertragsabschnitt ist eine Tabellenzeile.

### Gestapelt (Stacked)

| Vorteil | Nachteil |
|---|---|
| Track Changes-tauglich | Lesefluss zweimal unterbrochen |
| Word-natives Layout | Manchmal Verlust der Querreferenz |
| Standard bei DIS, ICC | Lange Vertraege werden unhandlich |

Gestapelt: Jeder Abschnitt erst auf Deutsch, dann auf Englisch. Englische Abschnitte in kursivem Schnitt oder mit "EN:"-Prefix.

**Empfehlung:** Side-by-Side bei kurzen Vertraegen (bis 30 Seiten) und symmetrischen Partnerschaften. Stacked bei langen Vertraegen (M&A SPAs, Lizenzvertraege mit vielen Anlagen).

## False Friends Deutsch-Englisch

Diese Begriffe werden im deutschen Anwaltsbuero regelmaessig falsch uebersetzt. Pruefen Sie jede Klausel.

| Englisch | Falsche dt. Uebersetzung | Korrekte dt. Uebersetzung | Anmerkung |
|---|---|---|---|
| **Indemnify** | Versichern | Freistellen | Konzept des § 257 BGB, weiter als dt. Schadensersatz |
| **Hold harmless** | Schadlos halten | Freistellen | Synonym zu indemnify in UK/US-Verstaendnis |
| **Reasonable** | Vernuenftig | Angemessen / verkehrsueblich | Common-Law-Standard, kein deutscher Begriff |
| **Best efforts** | Beste Bemuehungen | Aeusserste / hoechstmoegliche Anstrengungen | Im US-Recht haerter als "reasonable efforts" |
| **Reasonable best efforts** | (oft falsch uebersetzt) | Angemessene Anstrengungen | Verhandlungsformel zwischen "best" und "commercially reasonable" |
| **Consequential damages** | Folgeschaeden | Indirekte oder mittelbare Schaeden | Begriff im US-Recht enger als dt. mittelbarer Schaden |
| **Punitive damages** | Strafzahlungen | Strafschadensersatz | Im dt. Recht unbekannt, ordre public-relevant (§ 328 ZPO) |
| **Liquidated damages** | Verfluessigte Schaeden | Pauschalierter Schadensersatz | Naeher an § 309 Nr. 5 BGB als an Vertragsstrafe |
| **Penalty** | Strafe | Vertragsstrafe | Im US-Recht oft unzulaessig, in dt. Recht Pflicht zur Begrenzung |
| **Severability** | Trennbarkeit | Salvatorische Klausel | Erfordert in dt. Recht zwingend salvatorische Klausel im Vertrag |
| **Entire agreement** | Gesamte Vereinbarung | Vollstaendigkeitsklausel / Schlussklausel | Im dt. Recht: Pruefung an § 305b BGB |
| **No waiver** | Kein Verzicht | Kein Verzicht durch Untaetigkeit | Im dt. Recht: § 242 BGB Verwirkung trotzdem moeglich |
| **Force majeure** | Hoehere Gewalt | Hoehere Gewalt | OK, aber Reichweite oft anders verstanden |
| **Counterparts** | Gegenstuecke | Mehrere Ausfertigungen | Standardklausel bei US/UK-Vertraegen |
| **Notice** | Mitteilung | Zugang einer rechtsverbindlichen Erklaerung | § 130 BGB Zugang ist enger |
| **Arbitration** | Schiedsverfahren | Schiedsverfahren | OK, aber Schiedsfaehigkeit pruefen § 1030 ZPO |
| **Setoff** | Aufrechnung | Aufrechnung | Im US-Recht weiter, im dt. Recht § 387 BGB |
| **Assignment** | Abtretung | Forderungsabtretung oder Vertragsuebernahme | Im US-Recht oft beides, im dt. Recht § 398 ff. BGB vs. § 414 ff. BGB |
| **Subsidiary** | Tochter | Tochtergesellschaft / Beherrschtes Unternehmen | Pruefung an § 17 AktG |
| **Affiliate** | Affiliierter | Verbundenes Unternehmen | § 15 AktG verwenden |
| **Material adverse change (MAC)** | Materielle nachteilige Veraenderung | Wesentliche nachteilige Veraenderung | Kein dt. Standardbegriff, im Vertrag zu definieren |
| **Representations and warranties** | Erklaerungen und Gewaehrleistungen | Garantien | Im dt. Recht selbststaendige Garantien § 311 BGB |
| **Conditions precedent** | Vorhergehende Bedingungen | Aufschiebende Bedingungen (Closing Conditions) | § 158 BGB |
| **Conditions subsequent** | Folgende Bedingungen | Aufloesende Bedingungen | § 158 II BGB |

## Synchron halten

- Definitionen-Verzeichnis: parallel pflegen, gleiche Nummerierung in beiden Sprachen.
- Querverweise: in beiden Sprachen, gleiche Paragraphennummer.
- Anlagen: gleiche Bezeichnung (Anlage 1 / Schedule 1).
- Bei Aenderung einer Klausel: andere Sprache sofort mitziehen. Niemals nur eine Sprache bearbeiten.
- Pruefung am Ende: Word-Vergleich beider Sprachen (manuell) auf Synchronitaet.

## Ablauf / Checkliste

1. Anwendungsfall klaeren (true bilingual / sovereign / courtesy).
2. Layout entscheiden (Side-by-Side oder Stacked).
3. Sprachklausel formulieren (s. o.).
4. Definitionenverzeichnis aufbauen, beide Sprachen synchron.
5. Vertrag in der verbindlichen Sprache zuerst draften.
6. Uebersetzung erstellen, dabei jede der oben aufgefuehrten False Friends pruefen.
7. Konsistenz-Pruefung: jeder definierte Begriff in beiden Sprachen identisch.
8. Forum-Pruefung: Kosten und Risiken bei Streitfall im vereinbarten Gericht (§ 184 GVG, § 293 ZPO).
9. Versand mit beiden Fassungen im selben Word-Dokument.

## Ausgabeformat

- **Bilingualer Vertragsentwurf** als .docx (Side-by-Side oder Stacked je nach Wahl).
- **Definitionsverzeichnis** zweispaltig.
- **Memo zu Sprachklausel und Forum** fuer den Mandanten.

## Beispiel: Sprachklausel mit Forum-Hinweis

> ### § 28 Sprache, Anwendbares Recht, Gerichtsstand
>
> (1) Dieser Vertrag ist in deutscher und englischer Sprache abgefasst. Die deutsche Fassung ist verbindlich. Die englische Fassung dient ausschliesslich der Information.
>
> (2) Auf diesen Vertrag findet ausschliesslich das Recht der Bundesrepublik Deutschland Anwendung. Die Anwendung des UN-Kaufrechts (CISG) wird ausgeschlossen.
>
> (3) Ausschliesslicher Gerichtsstand fuer alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag ist Frankfurt am Main. Die Parteien koennen davon abweichend ein Schiedsverfahren nach der Schiedsordnung der DIS (Deutsche Institution fuer Schiedsgerichtsbarkeit) vereinbaren; Schiedsort ist in diesem Fall Frankfurt am Main, Schiedssprache Deutsch.
>
> ### Section 28 Language, Governing Law, Jurisdiction
>
> (1) This Agreement is executed in both German and English. The German version shall be binding. The English version is for information only.
>
> (2) This Agreement shall be exclusively governed by the laws of the Federal Republic of Germany. The application of the UN Convention on Contracts for the International Sale of Goods (CISG) is hereby excluded.
>
> (3) The exclusive place of jurisdiction for all disputes arising out of or in connection with this Agreement shall be Frankfurt am Main, Germany. The parties may agree on arbitration pursuant to the rules of the DIS (German Arbitration Institute); in such case, the seat of arbitration shall be Frankfurt am Main, Germany, and the language of arbitration shall be German.

## Querverweise

- `boilerplate-klauseln-katalog` fuer Schlussbestimmungen
- `klausel-bibliothek-katalog` fuer bilinguale Klauselbausteine
- `dokumentarchitektur-vertrag-und-schriftsatz`
- `word-dokument-finish-und-layout` für die Endkontrolle von Tabellen, Seitenumbrüchen und Versandfassung

## Quellen (Stand 05/2026)

- Art. 3, 6 Rom I-VO; §§ 133, 157, 158, 257, 305b, 309 Nr. 5, 387, 398, 414 BGB; §§ 17 AktG, 184 GVG, 293 ZPO, 328 ZPO, 1030 ZPO; § 15 AktG; CISG (UN-Kaufrechtsuebereinkommen).
- Zitierweise: `references/zitierweise.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `cowork-cloud-kollaboration-drafting`

**Fokus:** Mandantengeheimnis-konformes Drafting in der Cloud (Claude Cowork; Office 365; Google Workspace). Rechtlicher Rahmen § 43a Abs. 2 BRAO; § 203 StGB; § 26 BORA und Art. 28 DSGVO. Auftragsverarbeitungsvertrag ist Voraussetzung. Sensible Daten: Mandantenname; Aktenzeichen; Sachverhalt. Pseudonymisierung im Entwurf; Mandantendaten erst in finaler Fassung. Versionierung. Zwei-Faktor-Authentifizierung. Mit Pitfall-Liste zu WhatsApp; E-Mail und Cloud ohne Auftragsverarbeitungsvertrag.

# Cowork und Cloud-Kollaboration im Drafting

## Zweck

Cloud-Tools wie Claude Cowork, Microsoft Office 365 oder Google Workspace sind aus dem juristischen Drafting nicht mehr wegzudenken. Sie ermöglichen schnelle Zusammenarbeit, Versionierung, KI-Unterstützung. Sie sind aber zugleich der häufigste Angriffsvektor auf das Mandantengeheimnis. Dieser Skill klärt den rechtlichen Rahmen und liefert eine praktische Vorgehensweise für sicheres Drafting in der Cloud.

Er ist nicht nur Datenschutzbelehrung. Er gibt konkrete Drafting-Empfehlungen: Welche Daten dürfen in welcher Phase in welches Tool. Wann pseudonymisieren. Wann erst nach Abschluss des Drafts die Mandantendaten einfügen.

## Eingaben

- Genutzte Cloud-Tools in Ihrer Kanzlei
- Bestehende Auftragsverarbeitungsverträge mit den Anbietern
- Mandatscharakter (Standardmandat, Hochrisiko, internationale Beteiligung)
- Geräteumfeld (kanzleieigene Geräte, BYOD, Remote)
- Verteilungskreis (interne Co-Drafter, externe Kolleginnen, Mandant)

## Rechtlicher und methodischer Rahmen

- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht der Anwältin und des Anwalts.
- § 203 Abs. 1 Nr. 3 StGB: Strafbarkeit der Verletzung von Privatgeheimnissen.
- § 203 Abs. 3 und Abs. 4 StGB: Mitwirkende Personen und externe Dienstleister; Voraussetzungen der zulässigen Einbindung.
- § 26 BORA: Sorgfalt bei Mitarbeiterinnen und Mitarbeitern sowie Dritten.
- Art. 5 DSGVO: Grundsätze (Rechtmäßigkeit, Zweckbindung, Datenminimierung, Integrität und Vertraulichkeit).
- Art. 28 DSGVO: Auftragsverarbeitung; schriftlicher Vertrag mit allen Pflichtinhalten erforderlich.
- Art. 32 DSGVO: Sicherheit der Verarbeitung (Pseudonymisierung; Verschlüsselung; Belastbarkeit; Wiederherstellbarkeit; regelmäßige Überprüfung).
- Art. 44 ff. DSGVO: Drittlandübermittlungen; insbesondere Schrems-II-Risiken bei US-Anbietern.
- BSI-Grundschutz und Empfehlungen der Bundesrechtsanwaltskammer zur Nutzung von Cloud-Diensten in Kanzleien.

## Ablauf / Checkliste

1. **Vor Tool-Nutzung: Auftragsverarbeitungsvertrag prüfen.** Liegt ein schriftlicher Auftragsverarbeitungsvertrag nach Art. 28 DSGVO vor? Sonst keine Mandantendaten in dieses Tool.
2. **Datenklassifikation klären.** Welche Information ist sensibel? Mandantenname, Aktenzeichen, Sachverhalt, Gegenseite. Auch eine harmlos wirkende Mandatsbezeichnung kann den Identifizierungskreis offenbaren.
3. **Pseudonymisierung im Drafting-Prozess.** Während der Konzept- und Klauselarbeit: "Mandant", "Mandantin", "Gegenseite", "Anlage 1" statt Klarnamen. Konkrete Beträge ggf. durch Platzhalter ersetzen.
4. **Erst in finaler Fassung die Klarnamen einsetzen.** Vorher Mandantendaten in einer geschützten Umgebung halten (lokal oder in einer kanzleieigenen, klassifizierten Cloud).
5. **Versionsführung mit klaren Stempeln.** v0 lokal, v1 Cloud-Entwurf pseudonymisiert, v2 mit Mandantendaten in geschützter Umgebung, v-final unterschriftsreif.
6. **Zwei-Faktor-Authentifizierung verbindlich.** Für alle Cloud-Dienste; ohne Ausnahme.
7. **Geräte- und Pfadhygiene.** Keine Mandantendaten auf privaten Cloud-Speichern, nicht in privaten Mail-Konten, nicht auf privaten Handys ohne Mobile Device Management.
8. **Berechtigungskonzept Cowork-Räume.** Nur die Personen mit Zugang, die Zugang brauchen. Externe Drafter aus dem Cowork-Raum entfernen, sobald ihre Phase endet.
9. **Logging und Audit.** Aktivitätsprotokolle aktivieren; bei Bedarf Audit prüfen.
10. **Notfallplan.** Was ist zu tun bei Datenleck (Art. 33, 34 DSGVO Meldepflichten innerhalb von 72 Stunden)?

### Sensitivitäts-Matrix

| Datenkategorie | Sensitivität | Maßnahme |
|---|---|---|
| Mandantenname | hoch | Pseudonym im Entwurf |
| Aktenzeichen | hoch | nur in geschützter Umgebung |
| Sachverhalt mit personenbeziehbaren Daten | hoch | Pseudonym; finale Fassung lokal |
| Klauselrohling ohne Bezug | niedrig | unbedenklich in Cloud |
| Vergleichsbetrag | mittel | Platzhalter im Entwurf |
| Strafrechtliche Vorwürfe | sehr hoch | nur Onpremise oder klassifizierte Cloud |
| Gesundheitsdaten (Art. 9 DSGVO) | sehr hoch | nur Onpremise oder klassifizierte Cloud |

### Pseudonymisierungs-Konventionen

```
Mandant -> "Mandant" oder "M"
Gegenseite -> "Gegenseite" oder "G"
Aktenzeichen -> "AZ-001"
Datum konkret -> "TT.MM.JJJJ" als Platzhalter
Betrag konkret -> "[Betrag]" oder "X Euro"
Adressen -> "Anschrift M" / "Anschrift G"
```

## Typische Drafting-Fehler

- **WhatsApp, private E-Mail, Privat-Cloud.** Mandantendaten ohne Auftragsverarbeitungsvertrag und ohne Verschlüsselung sind ein Bruch von § 203 StGB.
- **Cloud-Anbieter ohne Auftragsverarbeitungsvertrag.** Selbst kostenlose Tools verarbeiten Daten; ohne Auftragsverarbeitungsvertrag tabu.
- **Klarnamen im Cowork-Raum von Anfang an.** Auch wenn der Anbieter geprüft ist, gehört das in die geschützte Umgebung.
- **Versionsdurcheinander.** Ohne klare Versionsstempel werden Entwürfe mit Klarnamen versehentlich extern geteilt.
- **Externe Drafter behalten Zugriff.** Nach Projektende vergessene Berechtigungen sind ein klassischer Fehler.
- **Keine Zwei-Faktor-Authentifizierung.** Passwort allein ist 2026 kein Schutz mehr.
- **Drittlandübermittlung übersehen.** Bei US-Cloud-Anbietern Schrems-II-Aspekte und Standardvertragsklauseln prüfen.
- **Bring-your-own-Device ohne Mobile Device Management.** Mandantendaten auf privaten Geräten ohne kontrollierten Trennungslogik.

## Ausgabeformat

- Sensitivitäts-Einschätzung für das konkrete Mandat.
- Empfehlung der Tool-Wahl pro Drafting-Phase.
- Pseudonymisierungsplan für Entwurfsphase.
- Checkliste vor Versand: Klarnamen ersetzt? Zwei-Faktor aktiv? Cowork-Berechtigungen aktuell?

## Beispiele

### Beispiel Cowork-Konzept für Vertragsdraft

```
Phase 1 (Konzept):
- Klauselbausteine in Cowork, vollständig pseudonymisiert.
- Mandant = "M", Gegenseite = "G", Beträge = "[Betrag]".

Phase 2 (Erstentwurf):
- Pseudonymisierter Entwurf in Cowork.
- Verweislogik und Versionen vor Versand bewusst kontrollieren.

Phase 3 (Mandantenfreigabe):
- Übernahme in lokale Word-Umgebung der Kanzlei.
- Klarnamen einsetzen, mit Mandant abstimmen.

Phase 4 (Versand an Gegenseite):
- Versand aus klassifizierter Kanzleiumgebung über beA, AnwaltsCloud oder verschlüsselte E-Mail.
- Metadaten vor Versand entfernen.
```

### Beispiel Verstoss-Szenario

Ein Anwalt schickt einen NDA-Entwurf für einen prominenten Mandanten über sein privates Gmail-Konto an einen externen Steuerberater. Folge: Verstoß gegen § 203 StGB (kein zulässiges Outsourcing nach § 203 Abs. 3 StGB), § 43a BRAO und Art. 32 DSGVO. Strafrechtliches Risiko, berufsrechtliche Maßnahme, Meldepflicht nach Art. 33, 34 DSGVO.

## Querverweise

- `word-dokument-finish-und-layout` für sichere Versandhygiene vor Upload oder Versand
- `revisions-prozess-redlines-comparison` für Versionsführung
- `orientierung-drafting-triage` für die Anfangsbewertung der Risikolage
- `geheimhaltung-nda-vertraulichkeit` für NDA-Klauseln, die das selbe Schutzgut adressieren

## Quellen (Stand 05/2026)

- § 43a Abs. 2 BRAO; § 203 Abs. 1 Nr. 3, Abs. 3 und Abs. 4 StGB; § 26 BORA; gesetze-im-internet.de und brak.de.
- Art. 5, 28, 32, 33, 34, 44 ff. DSGVO; dsgvo-gesetz.de.
- Empfehlungen der Bundesrechtsanwaltskammer zur Cloud-Nutzung: vom Nutzer zu prüfen, brak.de.
- Schrems-II-Urteil EuGH und Folgepraxis: vom Nutzer zu verifizieren (EuGH, Urt. v. 16. Juli 2020, Rs. C-311/18).
- `references/zitierweise.md` für Belegpflicht.
