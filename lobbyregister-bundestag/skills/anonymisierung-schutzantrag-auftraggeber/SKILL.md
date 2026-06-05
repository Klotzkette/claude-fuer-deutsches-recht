---
name: anonymisierung-schutzantrag-auftraggeber
description: "Anonymisierung Schutzantrag Auftraggeber: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anonymisierung Schutzantrag Auftraggeber

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anonymisierung Schutzantrag Auftraggeber** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anonymisierung-schutzantrag` | Prüft Beschraenkung der Veröffentlichung bei schutzwürdigen Interessen nach § 4 Abs. 6 LobbyRG und Altfall-Anonymisierung. Output Schutzantrag-Skizze. |
| `auftraggeber-ermitteln` | Erfasst Auftraggeberinnen und Auftraggeber bei Interessenvertretung im Auftrag Dritter und die jeweils beauftragte Interessenvertretung. Output Auftraggebermatrix. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Anonymisierung Schutzantrag Auftraggeber**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anonymisierung-schutzantrag`

**Fokus:** Prüft Beschraenkung der Veröffentlichung bei schutzwürdigen Interessen nach § 4 Abs. 6 LobbyRG und Altfall-Anonymisierung. Output Schutzantrag-Skizze.

# Anonymisierung und Schutzantrag

## Einsatz

Nicht oeffentliche oder gefaehrdende Angaben rechtssicher behandeln.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Person oder Angabe soll nicht veroeffentlicht werden?
2. Welche konkrete Gefahr oder Altfall-Konstellation liegt vor?
3. Welche Nachweise koennen die Schutzbeduerftigkeit tragen?

## Schutzantrag § 4 LobbyRG — Rechtsrahmen

### 1. Anwendungsbereich
- **Antragsberechtigt**: Interessenvertreter selbst sowie betroffene natürliche und juristische Personen.
- **Antragsgegenstand**: Beschränkung der Veröffentlichung einzelner Angaben im Lobbyregister.
- **Antragsfrist**: Schutzantrag ist jederzeit möglich; bei Erstregistrierung empfohlen, **vor** Aktivschaltung der Eintragung.

### 2. Schutzgründe (typische Fallgruppen)
- **Existenzgefährdung** der natürlichen Person (z. B. konkrete Bedrohungslage, gerichtsfeste Drohungen).
- **Wesentlicher wirtschaftlicher Nachteil** durch Offenlegung (Geschäftsgeheimnisse § 1 GeschGehG; vertrauliche Geschäftsbeziehungen).
- **Persönlichkeitsrechte** (Art. 2 I iVm Art. 1 I GG): bei sensiblen persönlichen Verhältnissen.
- **Schutz Mitarbeiter** (§ 26 BDSG; nicht-leitende Beschäftigte erscheinen i.d.R. nicht namentlich).
- **Altfall-Anonymisierung** für Personen, deren Tätigkeit vor Inkrafttreten LobbyRG (1.1.2022) endete und für die Veröffentlichung unverhältnismäßig wäre.

### 3. Antragsinhalt — Pflichtangaben
- **Antragsteller** mit Identifikation.
- **Konkrete Angabe**, die zu beschränken ist (z. B. Name einer Person, Auftraggeber).
- **Tatsachenkern** der Schutzbedürftigkeit (konkret, individuell).
- **Nachweise**: z. B. Anzeigen (Polizei, Strafanzeige), Drohungen (Screenshots, Briefe), wirtschaftliche Belege.
- **Antragsbegehr**: "Es wird beantragt, die Angabe X nicht öffentlich darzustellen."

### 4. Verfahren bei der registerführenden Stelle
- **Bearbeitung** durch Bundestagsverwaltung (registerführende Stelle).
- **Anhörung** des Antragstellers § 28 VwVfG analog.
- **Entscheidung** mit Begründung; Rechtsbehelfsbelehrung.
- **Rechtsschutz**: gegen Ablehnung Widerspruch / Klage zum VG Berlin (Sitz Bundestagsverwaltung); im Eilfall § 80 V VwGO.

### 5. Wirkung
- **Beschränkung** auf Nicht-Veröffentlichung; Daten verbleiben im Register, sind aber nicht öffentlich abrufbar.
- **Bundestag selbst** sieht die Angaben (interne Verwendung).
- **Anpassung bei Änderung der Lage** (Schutzgrund entfällt) möglich.

## Antragstext-Skizze

> An die registerführende Stelle des Lobbyregisters beim Deutschen Bundestag
>
> Schutzantrag nach § 4 LobbyRG
>
> Antragsteller: [Name, Adresse, Registernummer]
>
> Betroffene Angabe: [konkrete Bezeichnung, z. B. "Name der Person Frau Dr. X als beauftragte Interessenvertreterin"]
>
> Begründung:
> 1. Tatsachenkern: [konkrete Schilderung, z. B. drohende Verfolgung im Ausland, dokumentierte Drohlage in DE]
> 2. Verhältnismäßigkeit: Die öffentliche Darstellung würde [konkreter Schaden] verursachen; eine Beschränkung gefährdet nicht den Transparenzzweck, weil [Begründung].
> 3. Nachweise: [Anlagen 1-3: Strafanzeige; Drohbrief; ärztliches Attest; Geschäftsführer-Erklärung].
>
> Antrag: Die Veröffentlichung der genannten Angabe wird beschränkt.
>
> Ort, Datum, Unterschrift

## Praxisfallen

- **Rein wirtschaftliche Erwägungen** (bloße Geschäftsbeziehung) reichen meist nicht; konkrete Gefährdung oder Geheimnischarakter erforderlich.
- **Pauschalanträge** (z. B. "alle Mitarbeiter anonymisieren") werden regelmäßig abgelehnt; individuell begründen.
- **Geschäftsgeheimnis § 1 GeschGehG** muss durch organisatorische Maßnahmen geschützt sein — bloße Behauptung reicht nicht.
- **Drohlage** mit Anzeige bei Polizei dokumentieren; mündliche Drohungen schwierig zu beweisen.
- **Veröffentlichungsschutz** ist nicht absolut: bei Anfragen mit überwiegendem öffentlichem Interesse (z. B. Untersuchungsausschuss) ggf. Offenlegung an Bundestag.
- **Rechtsweg gegen Ablehnung**: nicht zum BVerwG, sondern VG Berlin (1. Instanz Verwaltungsgerichtsbarkeit).
- **Verhältnismäßigkeit**: Antrag muss erforderlich und geeignet sein; weniger einschneidende Mittel (z. B. teilweise Beschränkung) zuerst prüfen.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Schutzantrag-Skizze mit Tatsachenkern, Nachweisen, Antragstext und Restrisiko.

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

## 2. `auftraggeber-ermitteln`

**Fokus:** Erfasst Auftraggeberinnen und Auftraggeber bei Interessenvertretung im Auftrag Dritter und die jeweils beauftragte Interessenvertretung. Output Auftraggebermatrix.

# Auftraggeber ermitteln

## Einsatz

Agentur-, Kanzlei- und Verbandsmandate registerfest strukturieren.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wer beauftragt die Interessenvertretung?
2. Welche Interessen, Vorhaben und Adressaten sind vom Auftrag umfasst?
3. Welche Angaben darf der Auftraggeber pruefen oder freigeben?

## Auftraggeber-Angabe § 3 Abs. 1 Nr. 9 LobbyRG

**Pflicht zur Angabe**, wenn Interessenvertretung **im Auftrag Dritter** erfolgt (Agentur, Kanzlei, Lobby-Beratung, PR-Agentur, Verband im Mandat):

- **Namentliche** Identifikation des Auftraggebers (natürliche oder juristische Person).
- **Anschrift / Sitz** des Auftraggebers.
- **Vorhaben / Regelungsbereich**, auf den die Vertretung sich bezieht.
- **Eingesetzte Personen** (zumindest die zur Interessenvertretung tätigen Beauftragten — § 3 I Nr. 4 LobbyRG, vgl. Skill `drehtuer-angaben`).

## Differenzierung Auftraggeber vs. Eigeninteresse

| Konstellation | LobbyRG-Pflicht |
|---|---|
| Unternehmen vertritt eigene Interessen | Selbst registrierungspflichtig (sofern Schwellen erreicht); keine Auftraggeber-Angabe |
| Branchenverband vertritt Mitgliederinteressen | Verband selbst registriert; Mitglieder nicht als Auftraggeber zu nennen, soweit Verbandstätigkeit als eigene |
| Lobby-Agentur (PR / Public Affairs) im Auftrag | Agentur registriert; **Auftraggeber als solche zu nennen** |
| Anwaltskanzlei: politische Lobbyarbeit im Mandat | Kanzlei pflichtig (sofern nicht klassische anwaltliche Mandantenvertretung ausgenommen § 2 II LobbyRG); **Mandant als Auftraggeber** |
| Anwaltskanzlei: konkrete Rechtsangelegenheit | § 2 II Nr. 9 LobbyRG: anwaltliche Vertretung in Mandantenangelegenheit ausgenommen |

## Schutzantrag (§ 4 LobbyRG)

Auftraggeber kann **Anonymisierung** der Registrierungsangaben verlangen, wenn schutzwürdige Interessen entgegenstehen — z. B.:
- **berufliche oder wirtschaftliche Existenzgefährdung** bei Offenlegung,
- **Schutz von Geschäftsgeheimnissen** (§ 1 GeschGehG-Maßstab analog),
- **Bedrohung Sicherheit** der Person.

Antrag formgebunden über das Portal mit Begründung; Entscheidung durch registerführende Stelle Bundestag; Recht auf gerichtliche Überprüfung.

## Verfahrensweise

1. **Mandatsbeschreibung** dokumentieren (Auftraggeber, Vorhaben, eingesetzte Personen).
2. **Erlaubnis Auftraggeber** zur Registereintragung einholen (oft AGB-Klausel oder Mandatsvereinbarung).
3. **Eintragung** im Portal: Auftraggebermatrix.
4. **Aktualisierung** bei neuen Aufträgen / Beendigung innerhalb 30 Tagen (§ 3 Abs. 3 LobbyRG).
5. **Schutzantrag § 4 LobbyRG** falls schutzwürdige Interessen.

## Praxisfallen

- **Anwaltsmandat** vs. **Politik-Mandat**: Wenn Kanzlei für Mandanten **Gesetzgebung beeinflussen** soll (auch im Wirtschaftsinteresse), ist das **Interessenvertretung** — nicht klassische anwaltliche Tätigkeit. § 2 II Nr. 9 LobbyRG-Ausnahme ist eng auszulegen.
- **Konzernmutter als Auftraggeber**: wenn Tochter für Mutter Lobbyarbeit macht — Mutter ist Auftraggeber.
- **Verband mit nur einem Mitglied**: Konstruktion als Vorwand, um Mitgliedsname zu verschleiern, wird kritisch geprüft (Verhaltenskodex).
- **Pro-Bono-Lobby**: auch unentgeltliche Interessenvertretung kann pflichtig sein, wenn systematisch erfolgt.
- **Geschäftsgeheimnis** vs. Transparenz: Schutzantrag § 4 LobbyRG ist eng; bloß Geschäftsbeziehung reicht nicht.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Auftraggebermatrix mit Identitaet, Auftrag, Regelungsvorhaben, eingesetzten Personen und Freigabestatus.

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
