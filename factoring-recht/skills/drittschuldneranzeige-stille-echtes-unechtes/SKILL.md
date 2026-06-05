---
name: drittschuldneranzeige-stille-echtes-unechtes
description: "Drittschuldneranzeige Stille Echtes Unechtes: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Drittschuldneranzeige Stille Echtes Unechtes

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Drittschuldneranzeige Stille Echtes Unechtes** im Plugin Factoring Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `drittschuldneranzeige-und-stille-zession` | Drittschuldneranzeige und stille Zession: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |
| `echtes-und-unechtes-factoring-risikoverteilung` | Echtes und unechtes Factoring Risikoverteilung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |
| `einziehungsbefugnis-debitoren-zahlungskanaele-treuhandkonto` | Einziehungsbefugnis Debitoren Zahlungskanäle Treuhandkonto: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |

## Arbeitsweg

Im Plugin Factoring Recht gilt für **Drittschuldneranzeige Stille Echtes Unechtes**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `drittschuldneranzeige-und-stille-zession`

**Fokus:** Drittschuldneranzeige und stille Zession: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Drittschuldneranzeige und stille Zession

## Fachkern: Drittschuldneranzeige und stille Zession
- **Spezialgegenstand:** Drittschuldneranzeige und stille Zession. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Eine **stille Zession** ist eine Forderungsabtretung, von der der Drittschuldner (Debitor) nichts weiß. Wirtschaftliches Motiv: Diskretion – der Markt soll nicht erfahren, dass der Kunde Forderungen verkauft (Liquiditätsindiz). Rechtlich ist die stille Zession zulässig und wirksam; § 398 BGB verlangt keine Anzeige. Die Anzeige ist nach § 409 BGB nur **Schutzinstrument für den Schuldner**: Er darf bis Kenntnis an den Altgläubiger zahlen mit befreiender Wirkung (§ 407 BGB).

Die Praxis kennt vier Modelle: (1) **stille Zession dauerhaft**, (2) **stille Zession mit Trigger** (Anzeige bei Krise), (3) **halboffene Zession** (Bankverbindung Factor, ohne Erläuterung), (4) **offene Zession** (vollständige Anzeige). Dieser Skill ordnet die Modelle und prüft die Risiken jedes Modells.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sie strukturieren ein Factoring, das vom Kunden vertraulich behandelt werden soll.
- Bei stiller Zession zahlt der Debitor weiter an den Kunden – Zahlungsumlenkung muss geregelt werden.
- Im Krisenszenario erwägen Sie, die stille Zession aufzudecken.
- DSGVO Art. 14: Information bei stiller Zession – ist das vereinbar?

Fragen zum Einstieg:
- Warum stille Zession? (Diskretion, Marketing, Kundenwunsch)
- Wer kassiert die Zahlungen? (Kunde mit Weiterleitungspflicht, Treuhandkonto)
- Welche Trigger sind im Vertrag definiert für die Aufdeckung?
- Wie wird der Debitor letztlich informiert, falls nötig?
- Was passiert in der Insolvenz des Kunden?

## Rechtlicher Rahmen

- **§ 398 BGB**: Abtretung – formfrei, Wirksamkeit unabhängig von Anzeige.
- **§ 407 BGB**: Leistung an Altgläubiger wirkt befreiend bis zur Kenntnis.
- **§ 409 BGB**: Anzeige der Abtretung – schützt Schuldner.
- **§ 410 BGB**: Schuldner kann Vorlage Abtretungsurkunde verlangen.
- **§ 354a HGB**: Trotz Abtretungsverbots wirksam, aber Debitor kann an Altgläubiger zahlen.
- **§ 80 InsO**: Verfügungsbeschränkung im Insolvenzverfahren – relevant bei späterer Aufdeckung.
- **DSGVO Art. 14**: Informationspflicht bei Erhebung aus dritter Hand – Art. 14 Abs. 5 lit. b kennt Ausnahmen.
- **§ 91 InsO**: Erwerb in der Insolvenz unwirksam.

## / Schritt für Schritt

1. **Modell wählen**: Stille Zession, halboffene Zession, offene Zession.
2. **Zahlungskanal definieren**: Bei stiller Zession leitet der Kunde weiter, idealerweise über Treuhandkonto.
3. **Trigger für Aufdeckung festlegen**: Krise, Reklamationsspitze, Verzug.
4. **Aufdeckungsverfahren vorbereiten**: Notifikationsschreiben mit Belegen, Vollmachtsnachweis.
5. **DSGVO-Risiko prüfen**: Art. 14 Information – Ausnahmen prüfen.
6. **Insolvenzrisiko abwägen**: Bei stiller Zession und Krise des Kunden Sondersituation (§ 80 InsO, § 91 InsO).
7. **Dokumentation**: Stille-Zessions-Vereinbarung, Treuhandvertrag, Trigger-Klausel.

## Trade-off-Matrix

| Modell | Diskretion | Sicherheit Factor | Aufwand |
|---|---|---|---|
| Stille Zession dauerhaft | Hoch | Niedrig (§ 407 BGB-Risiko) | Niedrig |
| Stille Zession mit Trigger | Hoch bis Trigger | Mittel | Mittel |
| Halboffene Zession (nur Bankverbindung Factor) | Mittel | Mittel | Niedrig |
| Offene Zession | Niedrig | Hoch | Hoch (Notifikationsmasse) |

## Praxistipps

- **Treuhandkonto vorhalten**: Bei stiller Zession kassiert idealerweise ein gemeinsames Treuhandkonto, auf das der Factor Zugriff hat.
- **Bankvollmacht Backup**: Vollmacht des Kunden für sein eigenes Konto, damit der Factor im Krisenfall direkt zugreifen kann.
- **Trigger eng definieren**: Reklamationsquote über 5 Prozent, Verzug über 30 Tage, Anzeichen einer Insolvenz.
- **Aufdeckungsbrief vorbereiten**: Im Vertrag bereits hinterlegt, sodass im Triggerfall sofort versendbar.
- **DSGVO-Ausnahme dokumentieren**: Wenn Art. 14-Information unverhältnismäßig wäre, schriftlich begründen.

## Mustertexte

**Klausel stille Zession**

"Die Abtretung erfolgt zunächst still im Sinne des § 398 BGB. Der Kunde behält die Einziehungsbefugnis. Eingehende Zahlungen werden auf das Treuhandkonto IBAN … (Inhaber Treuhänder) eingezogen. Der Factor ist berechtigt, jederzeit, insbesondere bei Reklamationsquote über 5 Prozent in einem Monat, bei Verzug einzelner Debitoren über 30 Tage, bei Krisensignalen des Kunden oder bei Anhaltspunkten für Insolvenzantragspflicht, die Abtretung offen zu legen und die Debitoren direkt zu notifizieren."

**Treuhandvertrag (Auszug)**

"Der Treuhänder eröffnet auf seinen Namen ein Treuhandkonto, auf das sämtliche Zahlungen der Debitoren des [Kunde] eingezahlt werden. Eingehende Beträge werden binnen drei Werktagen an den Factor weitergeleitet, soweit sie auf angekaufte Forderungen entfallen, und an den Kunden, soweit sie auf nicht angekaufte Forderungen entfallen. Der Treuhänder unterliegt der Schweigepflicht gegenüber Dritten."

**Aufdeckungsschreiben (Trigger)**

"Sehr geehrte Damen und Herren, in Sachen der Forderung gegen Sie aus Rechnung Nr. … vom … zeigen wir Ihnen gemäß § 409 BGB an, dass diese Forderung an die [Factor] abgetreten wurde. Bitte zahlen Sie ab sofort ausschließlich auf das Konto der [Factor], IBAN: …. Die Geschäftsbeziehung zu [Kunde] bleibt unverändert."

## Typische Fehler

- Stille Zession ohne Zahlungsumlenkung – Debitor zahlt an Kunde, Kunde verbraucht das Geld, Factor hat Anspruch nur gegen den Kunden.
- Keine Trigger-Klausel – im Krisenfall fehlt Aufdeckungsrecht.
- DSGVO Art. 14 ignoriert – Aufsichtsrisiko.
- Insolvenz des Kunden vor Aufdeckung – § 91 InsO blockiert nachträgliche Zugriffe.
- Treuhandkonto fehlt – kein Schutz vor Vermengung mit Kundenkonten.

## Querverweise

- `debitorenkommunikation-und-abtretungsanzeige`
- `einziehungsbefugnis-debitoren-zahlungskanaele-treuhandkonto`
- `insolvenz-des-factoringkunden-aussonderung-absonderung`
- `datenschutz-debitorendaten-dsgvo-informationspflichten`

## Quellen Stand 06/2026

- BGB §§ 398, 407, 409, 410 zur Abtretung und Schuldnerschutz.
- HGB § 354a zur Wirksamkeit trotz Abtretungsverbots.
- InsO §§ 80, 91 zur Verfügungsbeschränkung im Insolvenzverfahren.
- DSGVO Art. 14, insbesondere Abs. 5 lit. b zur Ausnahme von der Informationspflicht.
- BGH zur Wirksamkeit der stillen Zession und zur Auslegung der Anzeige (st. Rspr.).

## 2. `echtes-und-unechtes-factoring-risikoverteilung`

**Fokus:** Echtes und unechtes Factoring Risikoverteilung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Echtes und unechtes Factoring Risikoverteilung

## Fachkern: Echtes und unechtes Factoring Risikoverteilung
- **Spezialgegenstand:** Echtes und unechtes Factoring Risikoverteilung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die wichtigste Grundunterscheidung des Factoringrechts: **echtes Factoring** versus **unechtes Factoring**. Der Unterschied liegt im **Bonitätsrisiko** (Delkredere): Übernimmt der Factor das Risiko, dass der Debitor nicht zahlen kann (echt), oder bleibt das Risiko beim Kunden (unecht)? Diese Differenzierung entscheidet über die zivilrechtliche Vertragsnatur, die bilanzielle Behandlung, die steuerliche Behandlung und die Insolvenzwirkungen.

**BGH-Leitsätze**: Echtes Factoring ist Kauf nach § 433 BGB; unechtes Factoring ist Darlehen mit Sicherungsabtretung. Aus dieser Einordnung folgen unterschiedliche Rechtsfolgen für Vertragsstörungen, Insolvenzwirkungen, Bilanzierung (True Sale versus Verbleib) und steuerliche Behandlung (§ 4 Nr. 8c UStG).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sie strukturieren einen neuen Factoringvertrag und müssen die Risikoverteilung festlegen.
- Im Streitfall ist die zivilrechtliche Einordnung umstritten (Kauf oder Kredit?).
- Bilanzielle Frage: Soll Off-Balance erreicht werden (echtes Factoring) oder reicht Liquiditätszufluss (unechtes Factoring)?
- Insolvenzfall des Kunden: Kann der Factor die Forderungen aussondern (echtes) oder absondern (unechtes)?

Fragen zum Einstieg:
- Wer trägt das Bonitätsrisiko (Factor oder Kunde)?
- Wie ist die Rückgriffsmöglichkeit ausgestaltet (uneingeschränkt, eingeschränkt auf bestimmte Konstellationen)?
- Welche bilanzielle Behandlung wird angestrebt?
- Welche Insolvenzlage ist relevant (Kunde, Debitor)?
- Soll der Vertrag steuerlich umsatzsteuerfrei sein (§ 4 Nr. 8c UStG)?

## Rechtlicher Rahmen

- **§ 433 BGB**: Kaufvertrag – beim echten Factoring; Verkäufer haftet für Verität, nicht für Bonität.
- **§ 488 BGB**: Darlehensvertrag – beim unechten Factoring; Käufer "leiht" Geld gegen Sicherungsabtretung.
- **§ 437 BGB**: Mängelhaftung des Verkäufers – Veritätsmängel beim echten Factoring.
- **§ 365 BGB**: Haftung des Übertragenden bei Hingabe an Erfüllungs statt – relevant für unechtes Factoring.
- **§ 4 Nr. 8c UStG**: Umsatzsteuerbefreiung des Forderungskaufs (echtes Factoring) – nicht für unechtes Factoring.
- **BGH-st. Rspr.** zur Abgrenzung: Übergang des Bonitätsrisikos ist entscheidend.
- **§ 47 InsO**: Aussonderungsrecht des Factors beim echten Factoring.
- **§ 51 InsO**: Absonderungsrecht beim unechten Factoring.
- **HGB § 246**: Bilanzielle Behandlung (Vermögensgegenstand).

## / Schritt für Schritt

1. **Vertragstyp festlegen**: Echtes oder unechtes Factoring?
2. **Rückgriffsklauseln formulieren**: Veritätshaftung ja, Bonitätshaftung nein (echt) oder ja (unecht).
3. **Risikoabgrenzung präzisieren**: Was ist Bonitätsausfall, was ist Veritätsmangel?
4. **Bilanzielle Folge prüfen**: True-Sale-Test (HGB, IFRS) – echtes Factoring führt zu Ausbuchung.
5. **USt-Behandlung prüfen**: § 4 Nr. 8c UStG bei echtem Factoring; Beratungsleistung bei unechtem.
6. **Insolvenzfolge planen**: Aussonderung (echt) versus Absonderung (unecht).
7. **AGB-Kontrolle**: Klausel "Voll-Rückgriff im echten Factoring" wäre Vertragstyp-widrig.

## Trade-off-Matrix

| Aspekt | Echtes Factoring | Unechtes Factoring |
|---|---|---|
| Bonitätsrisiko | Factor | Kunde |
| Veritätsrisiko | Kunde | Kunde |
| Zivilrechtliche Natur | Kauf § 433 BGB | Darlehen § 488 BGB |
| Bilanzielle Ausbuchung | Ja (True Sale) | Nein |
| Insolvenzrecht | Aussonderung § 47 InsO | Absonderung § 51 InsO |
| Umsatzsteuer | Steuerfrei § 4 Nr. 8c UStG | Steuerbar als Leistung |
| Risikoprämie | Hoch | Niedrig |
| Kundenattraktivität | Hoch | Niedrig (Risiko bleibt) |

## Praxistipps

- **Hybridmodelle prüfen**: In der Praxis gibt es Mischformen mit Rückgriff nur bei bestimmten Ausfallgründen (Insolvenz des Debitors versus Reklamationen).
- **Bonitätsbegriff klar definieren**: Was ist Bonität (Insolvenz, dauerhafte Zahlungsunfähigkeit, Verzug über 90 Tage)?
- **Verzichtbar im Vertrag**: BGH lässt freie Vertragsgestaltung zu, soweit klar erkennbar, welches Risiko übernommen wird.
- **AGB-Kontrolle bei Mischformen**: Wenn echtes Factoring deklariert, aber Bonitätsrisiko durch Rückbelastung beim Kunden landet, droht § 307 BGB.
- **Umsatzsteuer mit Berater klären**: Die § 4 Nr. 8c UStG-Befreiung ist beim echten Factoring etabliert, aber Detailfragen (Servicegebühr, Inkasso) gesondert prüfen.

## Mustertexte

**Klausel echtes Factoring (Kaufvertrag)**

"Der Factor erwirbt die abgetretenen Forderungen mit allen Chancen und Risiken. Das Bonitätsrisiko des Debitors (insbesondere Insolvenz, dauerhafte Zahlungsunfähigkeit, Verzug länger als 120 Tage) geht vollständig auf den Factor über. Der Verkäufer haftet ausschließlich für die Verität der Forderungen (Bestand, Einredefreiheit, vereinbarte Höhe). Eine Bonitätshaftung des Verkäufers wird ausdrücklich ausgeschlossen."

**Klausel unechtes Factoring (Darlehen mit Sicherungsabtretung)**

"Die Übertragung der Forderungen erfolgt als Sicherungsabtretung zur Sicherung des durch den Factor an den Kunden gewährten Vorschusses. Bei Zahlungsausfall des Debitors – aus welchem Grund auch immer – ist der Factor berechtigt, den Vorschuss vom Kunden zurückzufordern (Rückgriffsrecht). Der Kunde haftet vollumfänglich für Bonität und Verität."

**Klausel Hybridmodell**

"Der Factor übernimmt das Bonitätsrisiko bei Insolvenz des Debitors. Bei sonstigen Zahlungsstörungen (Reklamation, Verzug ohne Insolvenz, Strittigstellung der Forderung) bleibt das Risiko beim Kunden, der zur Rückerstattung des Kaufpreises gegen Rückabtretung verpflichtet ist."

## Typische Fehler

- Vertrag deklariert echtes Factoring, schreibt aber faktisch Voll-Rückgriff vor – widersprüchlich.
- Unklare Definition des Bonitätsausfalls – Streit, ob Insolvenz, Verzug, Bestreiten.
- Bilanzierung mit echtem Factoring, obwohl Vertrag Voll-Rückgriff vorsieht – Ausbuchung fehlerhaft.
- USt-Behandlung übersehen – echtes Factoring ist § 4 Nr. 8c UStG-steuerfrei, unechtes nicht.
- Insolvenzfolgen falsch antizipiert – Aussonderung versus Absonderung.

## Querverweise

- `factoringvertrag-rahmenvertrag-forderungskauf-kaufpreis-sicherhe`
- `bilanzierung-true-sale-ausbuchung-wirtschaftliches-risiko`
- `factoringtyp-true-false-reverse-maturity`
- `insolvenz-des-factoringkunden-aussonderung-absonderung`

## Quellen Stand 06/2026

- BGB §§ 433, 437, 488, 365 zur Abgrenzung Kauf und Darlehen.
- BGH-st. Rspr. zur Abgrenzung echtes/unechtes Factoring (Übergang des Bonitätsrisikos als entscheidendes Kriterium).
- UStG § 4 Nr. 8c zur Umsatzsteuerbefreiung des Forderungskaufs.
- HGB § 246 zur bilanziellen Zurechnung.
- InsO §§ 47, 51 zu Aussonderungs- und Absonderungsrechten.

## 3. `einziehungsbefugnis-debitoren-zahlungskanaele-treuhandkonto`

**Fokus:** Einziehungsbefugnis Debitoren Zahlungskanäle Treuhandkonto: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Einziehungsbefugnis Debitoren Zahlungskanäle Treuhandkonto

## Fachkern: Einziehungsbefugnis Debitoren Zahlungskanäle Treuhandkonto
- **Spezialgegenstand:** Einziehungsbefugnis Debitoren Zahlungskanäle Treuhandkonto. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Wer darf das Geld vom Debitor einziehen? Wer hält das Konto, auf das gezahlt wird? Wer hat im Krisenfall Zugriff? Diese drei Fragen entscheiden über die operative Tauglichkeit jedes Factorings. Die zivilrechtliche Abtretung allein bringt dem Factor noch keinen Cent – es braucht eine **Einziehungsstruktur**, die Zahlungen verlässlich zum Factor leitet.

Drei Standardmodelle: (1) **Eigenes Konto Factor** – Debitoren zahlen direkt; (2) **Treuhandkonto** eines unabhängigen Treuhänders mit Verteilfunktion; (3) **Einziehungsermächtigung des Kunden** mit Weiterleitungspflicht. Jedes Modell hat insolvenz- und aufsichtsrechtliche Implikationen. Dieser Skill ordnet die Strukturen und liefert die Vertragsbausteine.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sie strukturieren das Zahlungs-Setup für ein neues Factoring.
- Der Kunde wünscht eine diskrete Lösung – Zahlungskanal soll für Debitoren unauffällig sein.
- Bei stiller Zession muss eine Zahlungsumlenkung organisiert werden.
- Im Krisenszenario will der Factor sofort auf die Zahlungseingänge zugreifen.

Fragen zum Einstieg:
- Wer eröffnet welches Konto (Kunde, Factor, Treuhänder)?
- Wer ist Kontoinhaber, wer hat Verfügungsbefugnis?
- Wie ist die insolvenzrechtliche Trennung gewährleistet?
- Welche Reportings zur Zahlungssteuerung sind nötig?
- Wie reagiert das Setup bei einer Krise des Kunden (Bankenkrise, Einleitung Insolvenzantrag)?

## Rechtlicher Rahmen

- **§ 362 BGB**: Erfüllung – Zahlung an Empfangsberechtigten.
- **§ 185 BGB**: Verfügung eines Nichtberechtigten – relevant bei Einziehungsermächtigung.
- **§ 666, 667 BGB**: Auskunft und Herausgabe im Geschäftsbesorgungsverhältnis.
- **§ 47 InsO**: Aussonderung – relevant bei Treuhandkonto.
- **§ 80 InsO**: Verlust der Verfügungsbefugnis des Schuldners.
- **§ 91 InsO**: Verfügungen nach Insolvenzantrag unwirksam.
- **BGH zur insolvenzfesten Treuhand**: Offenlegung und Bestimmtheit erforderlich.
- **§ 21 KWG**: Schutz von Kundengeldern bei Finanzdienstleistern.
- **§ 1 Abs. 22 ZAG**: Zahlungskonto – ZAG-Relevanz bei Drittgelderverwaltung.

## / Schritt für Schritt

1. **Setup wählen**: Eigenes Factor-Konto, Treuhandkonto, Kundenkonto mit Weiterleitung.
2. **Vertragstrennung**: Treuhandvertrag, Vollmacht, Weiterleitungspflicht.
3. **Insolvenzfestigkeit prüfen**: Treuhandbestand offen und bestimmt, sodass § 47 InsO greift.
4. **Bankvollmacht installieren**: Im Notfall direkter Zugriff Factor auf Konto.
5. **Reporting einrichten**: Tägliche oder wöchentliche Übersicht aller Zahlungseingänge.
6. **Krisenprotokoll**: Wann wechselt das Setup (Trigger), wer trifft die Entscheidung?
7. **Dokumentation**: Kontonummern, Vollmachten, Treuhandverträge in zentraler Akte.

## Trade-off-Matrix

| Modell | Diskretion | Insolvenzfestigkeit | Aufwand |
|---|---|---|---|
| Eigenes Factor-Konto | Niedrig (Faktor sichtbar) | Hoch | Niedrig |
| Treuhandkonto Notar/Anwalt | Mittel | Hoch (§ 47 InsO bei korrekter Konstruktion) | Hoch |
| Treuhandkonto Bank | Hoch | Mittel | Mittel |
| Kundenkonto mit Vollmacht Factor | Hoch | Niedrig (Mitarbeit Kunde nötig) | Niedrig |
| Hybrid: Stille Phase Kundenkonto, Trigger zu Factor | Hoch bis Trigger | Mittel | Mittel |

## Praxistipps

- **Treuhand mit Bank ist Marktstandard**: Banken stellen sogenannte "Faktorkonten" zur Verfügung, auf die der Factor zugreift, Schreiben aber Kundenname trägt.
- **Insolvenzfestigkeit kommt nicht von alleine**: Treuhandkonto muss offen, bestimmt und unmissverständlich dem Factor zugeordnet sein – sonst keine Aussonderung.
- **Bankvollmacht regelmäßig erneuern**: Vollmachten werden bei Geschäftsführerwechsel unwirksam – jährliches Update.
- **Lastschriftverfahren prüfen**: SEPA-Mandate können zugunsten Factor angepasst werden, wenn Debitoren via Lastschrift zahlen.
- **Tägliches Reporting**: Bei stiller Zession ohne tägliches Reporting verliert der Factor den Überblick.

## Mustertexte

**Klausel Treuhandkonto im Factoringvertrag**

"Sämtliche Zahlungen der Debitoren werden auf das Treuhandkonto IBAN … eingezahlt, Inhaber ist [Treuhänder] – Notar/Rechtsanwalt – als offener Treuhänder für den Factor. Der Treuhänder weist täglich die Zahlungseingänge dem Factor zu. Der Treuhandbestand ist insolvenzrechtlich aussonderungsfähig im Sinne § 47 InsO."

**Treuhandvertrag (Auszug)**

"Der Treuhänder verwaltet das Treuhandkonto offen als Treugutbestand für den Factor. Die Treugutfähigkeit ist offenkundig durch Kontobezeichnung "Treuhandkonto [Factor] / [Kunde]" und durch laufende Verbuchung getrennt vom Eigenvermögen des Treuhänders. Der Treuhänder kann nur nach schriftlicher Anweisung des Factors über das Konto verfügen."

**Bankvollmacht (Auszug)**

"Der Kontoinhaber [Kunde] erteilt der [Factor] hiermit unwiderrufliche Bankvollmacht über das Konto IBAN …. Die Vollmacht gilt insbesondere für Verfügungen über Zahlungseingänge der Debitoren. Die Bank ist unwiderruflich angewiesen, der [Factor] Auskünfte über Kontostand und Transaktionen zu erteilen."

**Weisung an Bank (Bankenanschreiben)**

"Sehr geehrte Damen und Herren, wir teilen Ihnen mit, dass das Konto IBAN … ab sofort als offenes Treuhandkonto für den Factor [X] geführt wird. Verfügungen nur nach gemeinsamer schriftlicher Anweisung von Kontoinhaber und Treugeber. Kontoauszüge gehen in Doppel an Kontoinhaber und Treugeber."

## Typische Fehler

- Treuhand ohne Offenlegung – § 47 InsO greift nicht, Insolvenzverwalter siedelt die Beträge an die Masse an.
- Bankvollmacht ohne Unwiderruflichkeitsklausel – Kunde widerruft kurz vor Insolvenz.
- Kundenkonto mit Weiterleitungspflicht ohne tägliches Reporting – Factor wird zu spät informiert.
- Mehrere Konten ohne Trennung – Vermengung von Kunden- und Factor-Geldern.
- Lastschriftmandate übersehen, Debitoren bezahlen via SEPA-Mandat an Kunden-Konto.

## Querverweise

- `drittschuldneranzeige-und-stille-zession`
- `debitorenkommunikation-und-abtretungsanzeige`
- `insolvenz-des-factoringkunden-aussonderung-absonderung`
- `factoringvertrag-rahmenvertrag-forderungskauf-kaufpreis-sicherhe`

## Quellen Stand 06/2026

- BGB §§ 185, 362, 666, 667 zu Verfügung und Geschäftsbesorgung.
- InsO §§ 47, 80, 91 zur Aussonderung und Insolvenzwirkung.
- BGH zur Anerkennung der offenen Treuhand als aussonderungsfähig (st. Rspr.).
- KWG § 21 zum Schutz von Kundengeldern.
- ZAG zur Behandlung von Zahlungskonten.
