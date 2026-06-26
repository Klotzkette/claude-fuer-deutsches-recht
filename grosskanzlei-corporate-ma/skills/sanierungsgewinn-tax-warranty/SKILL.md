---
name: sanierungsgewinn-tax-warranty
description: "Strukturierung von Tax Warranty und Tax Indemnity im SPA für Transaktionen mit Sanierungsgewinn-Risiko nach Paragraf 3a EStG. Adressiert die Verteilung des Risikos zwischen Verkäufer und Käufer für den Fall, dass die Steuerbefreiung versagt wird, dass die zwingende Verrechnungsreihenfolge nach Paragraf 3a Abs...."
---

# Sanierungsgewinn – Tax Warranty und Tax Indemnity im SPA

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Sanierungsgewinn – Tax Warranty und Tax Indemnity im SPA
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Worum geht es

In Transaktionen mit Sanierungsbezug ist die klassische Tax-Indemnity-Architektur unzureichend. Drei Risikofelder treten zusätzlich auf: erstens die **Versagung der Steuerbefreiung nach Paragraf 3a EStG**; zweitens der **zwangsweise Verbrauch der Verlustvorträge** nach Paragraf 3a Abs. 3 EStG mit Wirkung auf zukünftige Steuerperioden; drittens das **Nichtergehen einer verbindlichen Auskunft** vor Closing. Wer hier nur eine Standard-Tax-Indemnity formuliert, lässt Risiko in Millionenhöhe ungeregelt.

Liefert die Architektur, mit der diese drei Risikofelder im SPA korrekt geregelt werden.

## Wann dieses Modul hilft

- SPA für eine Zielgesellschaft, deren Sanierungsmaßnahmen unmittelbar vor, zum oder kurz nach Signing wirksam werden.
- Carve-out aus einem Konzern mit Forderungsverzicht der Muttergesellschaft.
- Debt-Equity-Swap, der den Anteilserwerb mit dem Forderungsverzicht in einem Vorgang verbindet.
- Akquisitionsstrukturen, in denen der Käufer auf einen funktionierenden Verlustvortrag wirtschaftlich angewiesen ist.

Nicht dieser Skill ist primär, wenn die Sanierung bereits abgeschlossen ist und die Steuerbescheide bestandskräftig sind; dann genügt die Standard-Tax-Indemnity.

## Rechtlicher Rahmen

- **Paragraf 3a EStG** – Voraussetzungen der Steuerbefreiung, vier Tatbestandsmerkmale.
- **Paragraf 3a Abs. 3 EStG** – zwingende Verrechnungsreihenfolge; Verlustvorträge werden verbraucht, bevor die Steuerbefreiung wirkt.
- **Paragraf 7b GewStG i. V. m. Paragraf 36 Abs. 2c GewStG** – Gewerbesteuer.
- **Paragraf 8c KStG / Paragraf 8d KStG** – Verlustvortrag bei Anteilseignerwechsel.
- **Paragraf 89 AO** – verbindliche Auskunft.
- **Paragraf 233a AO** – Verzinsung.
- **Paragraf 280, 311 Abs. 2 BGB** – Allgemeines Schuldrecht für Garantie- und Freistellungsansprüche.
- **Paragraf 444, 461 BGB** – arglistige Verschweigung und vertragliche Beschaffenheitsangaben.

## / Schritt für Schritt

1. **Risikolandkarte erstellen.** Welche steuerlichen Risikofelder sind in diesem Deal aktiv: Versagung Steuerbefreiung, Verbrauch Verlustvortrag, Versagung verbindliche Auskunft, Paragraf 8c KStG-Trigger, Mindestbesteuerung?
2. **Locked Box vs. Closing Accounts.** Bei Sanierungs-Deals häufig Locked Box mit Effective Date vor Wirksamwerden der Sanierungsmaßnahme. Steuerliche Risiken aus der Sanierungsmaßnahme bleiben dann beim Verkäufer.
3. **Tax-Definition justieren.** Definition von „Tax" und „Tax Liability" auf die Sanierungsthematik anpassen; nicht nur tatsächlich gezahlte Steuer, sondern auch Verlustvortragsverbrauch einbeziehen, soweit wirtschaftlich relevant.
4. **Trennung Warranty vs. Indemnity.** Warranties als Beschaffenheitsangabe (etwa: „Die festgestellten Verlustvorträge bestehen"); Indemnity als unbedingter Freistellungsanspruch (etwa: „Versagung der Steuerbefreiung nach Paragraf 3a EStG").
5. **Haftungsregime.** De-Minimis, Basket, Cap, Sub-Cap für Tax. Standard ist 100 %-Cap für Tax-Indemnity, deutlich höher als die General-Warranty-Cap.
6. **Verjährung.** Verjährung der Tax-Indemnity klassisch sechs Monate nach Festsetzungsverjährung; bei Sanierungsthematik gegebenenfalls länger, weil Außenprüfungen oft erst Jahre später beginnen.
7. **Mitwirkungspflichten.** Verkäufer muss Außenprüfungen begleiten dürfen; Käufer muss vor Anerkenntnis Steuernachforderung den Verkäufer informieren (Tax Conduct).
8. **Verbindliche Auskunft als Closing Condition oder als Indemnity?** Beides möglich; konzeptionell sauberer ist die Closing Condition mit Long-Stop-Date.

## Trade-off-Matrix

| Risiko | Warranty | Indemnity | Closing Condition |
|---|---|---|---|
| Versagung Paragraf 3a EStG | – (zu allgemein) | empfohlen | denkbar bei verb. Auskunft |
| Verbrauch Verlustvortrag durch Paragraf 3a Abs. 3 EStG | nur als Beschaffenheit der Vortragshöhe | für späteren Verbrauch | – |
| Paragraf 8c KStG-Trigger durch Erwerb | – | empfohlen, aber strittig | – |
| Verbindliche Auskunft nicht erteilt | – | denkbar | empfohlen |
| Mindestbesteuerung Paragraf 10d EStG | – | empfohlen, weil streitig | – |

## Praxistipps der alten Hasen

Wer als Verkäuferseite in einen Sanierungs-SPA geht, sollte drei Verhandlungslinien beherrschen:

- **„Wir geben keine Steuerbefreiungs-Garantie ab, weil die Sanierungseignung wirtschaftliche Wertung ist."** Dieser Satz wehrt einen Vollservice-Indemnity ab. Stattdessen wird die Sanierungseignung in Anlagen mit dem IDW-S6-Gutachten und der verbindlichen Auskunft dokumentiert.
- **„Tax-Indemnity nur, soweit Sachverhalt vor Closing realisiert."** Das schützt davor, dass nachträgliche Sachverhalte (etwa Mantelkauf durch nachgelagerten Anteilserwerb) auf den Verkäufer zurückfallen.
- **„Verbindliche Auskunft als Closing Condition mit Long-Stop neun Monate."** Das diszipliniert beide Seiten und gibt dem Käufer Rechtssicherheit.

Auf Käuferseite gilt umgekehrt: Closing Condition ist die saubere Lösung, aber sie verzögert. Wer Geschwindigkeit braucht, geht in die Indemnity und akzeptiert eine sub-cap auf Tax in voller Kaufpreishöhe.

## SPA-/Plan-Klausel Mustertexte

**Vendor Warranty re Tax Position Sanierungsgewinn:**

> Verkäufergarantie Steuern Sanierungsgewinn: Der Verkäufer garantiert, dass nach bestem Wissen am Stichtag (i) keine Tatsachen bekannt sind, die der Anwendung von Paragraf 3a EStG auf den im Rahmen der Sanierungsmaßnahme entstehenden Ertrag entgegenstehen, (ii) der durch die Sanierungsmaßnahme entstehende Ertrag in dem in Anlage X aufgeführten Tax-Modell zutreffend prognostiziert ist und (iii) keine Außenprüfung läuft, die den festgestellten Verlustvortrag in Frage stellt.

**Indemnity for Paragraf 3a EStG Antragsversagen:**

> Steuerfreistellung Sanierungsertrag: Der Verkäufer stellt den Käufer frei von sämtlichen Steuern, Nebenleistungen, Zinsen nach Paragraf 233a AO und angemessenen Beratungskosten, die der Zielgesellschaft oder einer ihrer Tochtergesellschaften daraus entstehen, dass (i) die Finanzbehörde die Anwendung des Paragraf 3a EStG auf den durch die Sanierungsmaßnahme entstehenden Ertrag ganz oder teilweise versagt oder (ii) die mit Antrag vom [Datum] beantragte verbindliche Auskunft nach Paragraf 89 AO mit einem für den Käufer nachteiligen Inhalt erteilt oder versagt wird, jeweils ohne Rücksicht auf ein Verschulden des Verkäufers.

**Closing Condition Tax:**

> Closing Condition Tax: Wirksame Erteilung einer verbindlichen Auskunft der zuständigen Finanzbehörde gemäß Paragraf 89 AO mit dem Inhalt, dass der durch die Sanierungsmaßnahme entstehende Ertrag die Voraussetzungen des Paragraf 3a EStG erfüllt; Long-Stop-Date ist der [Datum].

**Tax Conduct:**

> Tax Conduct: Der Käufer benachrichtigt den Verkäufer unverzüglich, spätestens innerhalb von zehn Werktagen, über jede Außenprüfungsanordnung, jede Anhörung und jede Steuerfestsetzung, die einen indemnity-relevanten Sachverhalt betrifft. Vor Anerkennung, Vergleich oder Klagerücknahme bedarf es der vorherigen schriftlichen Zustimmung des Verkäufers, die nicht unbillig verweigert werden darf.

## Typische Fehler in komplexer Transaktion

- Tax-Indemnity erfasst nur tatsächlich gezahlte Steuer, nicht den Verlustvortragsverbrauch; der Käufer bleibt auf dem wirtschaftlichen Schaden sitzen.
- Closing Condition mit zu kurzem Long-Stop-Date; das Finanzamt schafft die verbindliche Auskunft nicht in der Zeit.
- Tax Conduct nicht geregelt; der Käufer macht Zugeständnisse, der Verkäufer wird trotzdem in Anspruch genommen.
- Sub-cap Tax wird auf die General-Cap gerechnet; dadurch ist die Tax-Indemnity wirtschaftlich wertlos.
- Verjährung Tax-Indemnity zu kurz; Außenprüfungen kommen oft erst nach fünf bis sieben Jahren.

## Quellen Stand 06/2026

- Paragraf 3a EStG; Paragraf 3a Abs. 3 EStG; Paragraf 7b GewStG i. V. m. Paragraf 36 Abs. 2c GewStG; Paragraf 8c KStG; Paragraf 8d KStG; Paragraf 89 AO; Paragraf 233a AO – prüfbar über gesetze-im-internet.de.
- BMF-Schreiben vom 27.04.2017 – Verifizierung im Bundessteuerblatt Stand 06/2026.
- FG Köln, Urteil vom 04.11.2025 – 12 K 1413/25 – prüfbar über dejure.org und NWB.
- BFH (Großer Senat), Beschluss vom 28.11.2016 – GrS 1/15 – prüfbar über bundesfinanzhof.de.
- BGH zu Garantie- und Freistellungsklauseln in SPA – ständige Rspr.; Verifizierung über dejure.org.
