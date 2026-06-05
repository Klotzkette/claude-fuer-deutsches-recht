---
name: mehrfachvertreter-muster-provisionsabrechnung
description: "Mehrfachvertreter Muster Provisionsabrechnung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mehrfachvertreter Muster Provisionsabrechnung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Mehrfachvertreter Muster Provisionsabrechnung** im Plugin Handelsvertreterrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mehrfachvertreter` | Analysiert die Rechtsstellung des Mehrfachvertreters nach § 86 Abs. 1 HGB: Interessenkollisionen bei gleichzeitiger Vertretung konkurrierender Unternehmer, Offenlegungspflichten, Wettbewerbsverbotsklauseln für Mehrfachvertreter, Auswirkungen auf Ausgleichsansprüche und Abgrenzung zum Einfirmenvertreter nach § 92b HGB. |
| `muster-provisionsabrechnung` | Erstellt Musterprovisonionsabrechnungen für Handelsvertreter nach § 87c HGB: vollständige Abrechnung mit Nachweis vermittelter Geschäfte, Provisionsberechnung je Auftragsposition, Stornobuchungen mit Begründung sowie Prüfcheckliste für die Handelsvertreterseite zur Kontrolle erhaltener Abrechnungen. |
| `nachfolge-agenturverkauf` | Analysiert den Verkauf einer Handelsvertretungsagentur: Übertragung des Vertretervertrags mit Zustimmung des Unternehmers, Auswirkungen auf Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB, Kaufpreisermittlung für den Kundenstamm, Wettbewerbsklauseln im Agenturverkauf und Regelungen zur Nachfolge. |
| `ndas-und-geschaeftsgeheimnisse` | Analysiert den Schutz von Geschäftsgeheimnissen und NDA-Vereinbarungen im Handelsvertretervertrag nach § 88 HGB und GeschGehG: Umfang der Geheimhaltungspflicht, Verhältnis von § 88 HGB und GeschGehG, Vertragliche NDA-Klauseln, Schadensersatz bei Verletzung und strafrechtliche Konsequenzen. |

## Arbeitsweg

Im Plugin Handelsvertreterrecht gilt für **Mehrfachvertreter Muster Provisionsabrechnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mehrfachvertreter`

**Fokus:** Analysiert die Rechtsstellung des Mehrfachvertreters nach § 86 Abs. 1 HGB: Interessenkollisionen bei gleichzeitiger Vertretung konkurrierender Unternehmer, Offenlegungspflichten, Wettbewerbsverbotsklauseln für Mehrfachvertreter, Auswirkungen auf Ausgleichsansprüche und Abgrenzung zum Einfirmenvertreter nach § 92b HGB.

# Mehrfachvertreter nach § 86 HGB — Interessenkonflikte und Offenlegungspflichten

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Mehrfachvertreter nach § 86 HGB — Interessenkonflikte und Offenlegungspflichten.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.

## Mandantenfall

- Handelsvertreter X vertritt gleichzeitig drei Unternehmer, darunter zwei direkte Wettbewerber; einer der Unternehmer Y fordert Unterlassung der Doppelvertretung.
- Handelsvertreter X hat die gleichzeitige Vertretung konkurrierender Unternehmer nicht offengelegt; Unternehmer Y kündigt fristlos nach § 89a HGB.
- Handelsvertreter X ist als Mehrfachvertreter tätig; er fragt, ob er bei Beendigung eines der Verträge Ausgleich von jedem Unternehmer verlangen kann.

## Erste Schritte

1. Interessenlage analysieren: sind die vertretenen Unternehmer Wettbewerber?
2. Offenlegungspflicht nach § 86 Abs. 1 HGB gegenüber allen Unternehmen prüfen.
3. Vertragsklauseln auf Konkurrenzverbote für Mehrfachvertreter prüfen.
4. Kündigung wegen verschwiegener Konkurrenzvertretung auf Wirksamkeit prüfen.
5. Ausgleichsansprüche gegen jeden Unternehmer separat berechnen.
6. Wettbewerbsrechtliche Implikationen der Mehrfachvertretung analysieren.

## Rechtsrahmen

- § 86 Abs. 1 HGB — Interessenwahrungspflicht und Offenlegungspflicht
- § 86 Abs. 2 HGB — Geheimhaltungspflicht bei Mehrfachvertretung
- § 89a HGB — Fristlose Kündigung wegen Verletzung der Offenlegungspflicht
- § 92b HGB — Einfirmenvertreter als Gegenbegriff
- § 89b HGB — Ausgleichsanspruch für jeden Vertretervertrag
- § 242 BGB — Treu und Glauben bei Interessenkonflikten

## Prüfraster

- Sind die Unternehmen direkte Wettbewerber oder in verschiedenen Märkten tätig?
- Hat der Handelsvertreter die Mehrfachvertretung gegenüber allen Unternehmen offengelegt?
- Gibt es vertragliche Konkurrenzverbote, die eine Mehrfachvertretung ausschließen?
- Rechtfertigt verschwiegene Konkurrenzvertretung eine fristlose Kündigung nach § 89a HGB?
- Bestehen Ausgleichsansprüche gegen jeden der vertretenen Unternehmer separat?
- Ist die Mehrfachvertretung wettbewerbsrechtlich unbedenklich?

## Typische Fallstricke

- Konkurrenzvertretung ohne Offenlegung — Fristlosigkeitsgrund nach § 89a HGB.
- Interessenkonflikt bei Mehrfachvertretung nicht erkannt — Haftungsrisiko.
- Ausgleichsanspruch nur gegen einen Unternehmer geltend gemacht — weitere Ansprüche vergessen.
- Geheimhaltungspflicht nach § 86 Abs. 2 HGB gegenüber einem Unternehmer verletzt.

## Output

Interessenkonflikt-Analyse, Offenlegungsschreiben, Ausgleichsberechnung je Unternehmer.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben zentrale Rechtsfragen durch Leitentscheidungen geklärt.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter zwingend.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) und Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltung (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen den praxisrelevanten Rechtsrahmen.
Für internationale Sachverhalte gilt zudem die Rom-I-Verordnung für das anwendbare Recht.

## Quellen

- [§ 86 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__86.html)
- [§ 89a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89a.html)
- [§ 92b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92b.html)
- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [Dejure § 86 HGB](https://dejure.org/gesetze/HGB/86.html)

## 2. `muster-provisionsabrechnung`

**Fokus:** Erstellt Musterprovisonionsabrechnungen für Handelsvertreter nach § 87c HGB: vollständige Abrechnung mit Nachweis vermittelter Geschäfte, Provisionsberechnung je Auftragsposition, Stornobuchungen mit Begründung sowie Prüfcheckliste für die Handelsvertreterseite zur Kontrolle erhaltener Abrechnungen.

# Muster-Provisionsabrechnung nach § 87c HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Muster-Provisionsabrechnung nach § 87c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.

## Mandantenfall

- Handelsvertreter X möchte eine vollständige Musterabrechnung erstellen, die er von Unternehmer Y verlangen kann.
- Unternehmer Y möchte eine rechtssichere Provisionsabrechnung an Handelsvertreter X übermitteln und fragt nach den Mindestanforderungen nach § 87c HGB.
- Handelsvertreter X hat eine Abrechnung von Unternehmer Y erhalten und möchte diese auf Vollständigkeit und Richtigkeit prüfen.

## Erste Schritte

1. Vertragsgrundlagen für Provisionsabrechnung (Satz, Basis, Fälligkeit) sichten.
2. Vollständige Abrechnung aller im Abrechnungszeitraum abgeschlossenen Geschäfte erstellen.
3. Stornierungen und Rückbuchungen mit Begründung und Nachweis ausweisen.
4. Direktabschlüsse und Bezirksprovisionen separat ausweisen.
5. Abrechnung mit Buchauszug nach § 87c Abs. 1 HGB abstimmen.
6. Prüfcheckliste für die Kontrollseite des Handelsvertreters erstellen.

## Rechtsrahmen

- § 87c Abs. 1 HGB — Monatliche Provisionsabrechnung
- § 87c Abs. 2 HGB — Anspruch auf Buchauszug zur Überprüfung
- § 87 HGB — Provisionspflichtige Geschäfte
- § 87a HGB — Fälligkeit der Provision nach Ausführung
- § 87b HGB — Provisionsberechnung bei Teilleistungen
- Art. 12 RL 86/653/EWG — Provisionsabrechnungspflichten

## Prüfraster

- Sind alle provisionspflichtigen Geschäfte in der Abrechnung enthalten?
- Sind Stornierungen korrekt begründet und vertragskonform?
- Stimmen Provisionsätze und Berechnungsgrundlagen mit dem Vertrag überein?
- Sind Direktabschlüsse des Unternehmers im Bezirk ausgewiesen?
- Ist die Abrechnung monatlich und pünktlich nach § 87c Abs. 1 HGB?
- Welche Perioden wurden nie abgerechnet — Nachforderungsrisiko?

## Typische Fallstricke

- Fehlende Stornobegründungen ohne vertragliche Grundlage — Provision zu Unrecht gekürzt.
- Direktabschlüsse des Unternehmers nicht ausgewiesen — Bezirksprovision vergessen.
- Abrechnung nicht monatlich — Verzug des Unternehmers nach § 286 BGB.
- Provisionsabrechnungszeitraum nicht klar abgegrenzt — Doppelzählung oder Lücken.

## Output

Muster-Provisionsabrechnung (tabellarisch), Prüfcheckliste, Buchauszugs-Vergleich.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben zentrale Rechtsfragen durch Leitentscheidungen geklärt.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter zwingend.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) und Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltung (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen den praxisrelevanten Rechtsrahmen.
Für internationale Sachverhalte gilt zudem die Rom-I-Verordnung für das anwendbare Recht.

## Quellen

- [§ 87c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87c.html)
- [§ 87 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87.html)
- [§ 87a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87a.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87c HGB](https://dejure.org/gesetze/HGB/87c.html)

## 3. `nachfolge-agenturverkauf`

**Fokus:** Analysiert den Verkauf einer Handelsvertretungsagentur: Übertragung des Vertretervertrags mit Zustimmung des Unternehmers, Auswirkungen auf Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB, Kaufpreisermittlung für den Kundenstamm, Wettbewerbsklauseln im Agenturverkauf und Regelungen zur Nachfolge.

# Agenturverkauf und Nachfolge im Handelsvertreterrecht

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Agenturverkauf und Nachfolge im Handelsvertreterrecht.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.

## Mandantenfall

- Handelsvertreter X möchte seine Agentur an Nachfolger N verkaufen; Unternehmer Y muss zustimmen; X prüft, ob er danach noch Ausgleich verlangen kann.
- Handelsvertreter X übernimmt die Agentur von Vorgänger V; er fragt, welche Rechte und Pflichten auf ihn übergehen und ob er für Altschulden des V haftet.
- Unternehmer Y prüft, ob er die Zustimmung zum Agenturverkauf von X an N verweigern kann und unter welchen Bedingungen er zustimmen muss.

## Erste Schritte

1. Zustimmungserfordernis des Unternehmers für die Agenturübertragung im Vertrag prüfen.
2. Ausgleichsanspruch des Veräußerers nach § 89b Abs. 3 Nr. 3 HGB prüfen — erlischt er?
3. Kaufpreisermittlung: Kundenstammwert, Provisionshistorie, Goodwill bewerten.
4. Haftung des Erwerbers für Altverbindlichkeiten des Veräußerers klären.
5. Wettbewerbsverbot für Veräußerer nach Agenturverkauf vereinbaren.
6. Übergangszeitraum und Einarbeitungsunterstützung vertraglich regeln.

## Rechtsrahmen

- § 89b Abs. 3 Nr. 3 HGB — Erlöschen des Ausgleichs bei Vertragsübertragung
- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen des Ausgleichs
- § 413 BGB — Abtretung des gesamten Vertrags (Vertragsübernahme)
- § 25 HGB — Haftung des Erwerbers bei Firmenfortführung
- § 90a HGB — Nachvertragliches Wettbewerbsverbot für Veräußerer
- Art. 17 RL 86/653/EWG — Ausgleich bei Vertragsende

## Prüfraster

- Hat der Unternehmer der Agenturübertragung zugestimmt?
- Erlischt der Ausgleichsanspruch des Veräußerers nach § 89b Abs. 3 Nr. 3 HGB?
- Wie wird der Kaufpreis für die Agentur ermittelt?
- Haftet der Erwerber für Altverbindlichkeiten des Veräußerers?
- Ist ein Wettbewerbsverbot für den Veräußerer nach § 90a HGB notwendig und wirksam?
- Welche Rechte und Pflichten gehen auf den Erwerber über?

## Typische Fallstricke

- Agenturübertragung ohne Zustimmung des Unternehmers — unwirksam.
- Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB beim Verkauf erlischt — nicht erkannt.
- Haftung des Erwerbers für Altverbindlichkeiten nicht vertraglich ausgeschlossen.
- Wettbewerbsverbot für Veräußerer vergessen — sofortige Konkurrenz nach Verkauf.

## Output

Agenturkaufvertrag Entwurf, Kaufpreisberechnung, Wettbewerbsverbotsklausel für Veräußerer.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben zentrale Rechtsfragen durch Leitentscheidungen geklärt.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter zwingend.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) und Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltung (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen den praxisrelevanten Rechtsrahmen.
Für internationale Sachverhalte gilt zudem die Rom-I-Verordnung für das anwendbare Recht.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 413 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__413.html)
- [§ 25 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__25.html)
- [§ 90a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__90a.html)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

## 4. `ndas-und-geschaeftsgeheimnisse`

**Fokus:** Analysiert den Schutz von Geschäftsgeheimnissen und NDA-Vereinbarungen im Handelsvertretervertrag nach § 88 HGB und GeschGehG: Umfang der Geheimhaltungspflicht, Verhältnis von § 88 HGB und GeschGehG, Vertragliche NDA-Klauseln, Schadensersatz bei Verletzung und strafrechtliche Konsequenzen.

# Geschäftsgeheimnisse und NDA im Handelsvertretervertrag nach § 88 HGB und GeschGehG

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Geschäftsgeheimnisse und NDA im Handelsvertretervertrag nach § 88 HGB und GeschGehG.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.

## Mandantenfall

- Unternehmer Y stellt fest, dass Handelsvertreter X vertrauliche Preisinformationen an einen Wettbewerber weitergegeben hat; Y prüft Schadensersatz und strafrechtliche Konsequenzen.
- Handelsvertreter X soll eine umfangreiche NDA unterzeichnen, die alle Kundendaten, Produktstrategien und Geschäftsmodelle umfasst; er prüft, was davon nach Vertragsende bindend ist.
- Unternehmer Y bemerkt, dass sein früherer Handelsvertreter X mit Wissen aus dem Vertragsverhältnis ein konkurrierendes Unternehmen aufgebaut hat.

## Erste Schritte

1. Umfang der gesetzlichen Geheimhaltungspflicht nach § 88 HGB bestimmen.
2. NDA-Klausel auf Vereinbarkeit mit § 88 HGB und GeschGehG prüfen.
3. Geschäftsgeheimnis-Definition nach § 2 Nr. 1 GeschGehG auf konkrete Informationen anwenden.
4. Verletzungshandlungen nach § 4 GeschGehG identifizieren.
5. Schadensersatz nach § 10 GeschGehG berechnen und geltend machen.
6. Strafrechtliche Konsequenzen nach § 23 GeschGehG prüfen.

## Rechtsrahmen

- § 88 HGB — Gesetzliche Geheimhaltungspflicht des Handelsvertreters
- § 2 Nr. 1 GeschGehG — Begriff des Geschäftsgeheimnisses
- § 4 GeschGehG — Verbotene Handlungen (Erlangung, Nutzung, Offenbarung)
- § 10 GeschGehG — Schadensersatz bei Verletzung
- § 23 GeschGehG — Strafbarkeit von Geheimnisverrat
- § 307 BGB — AGB-Kontrolle weitreichender NDA-Klauseln

## Prüfraster

- Handelt es sich um ein Geschäftsgeheimnis nach § 2 Nr. 1 GeschGehG?
- Hat der Unternehmer angemessene Geheimhaltungsmaßnahmen ergriffen?
- Liegt eine verbotene Handlung nach § 4 GeschGehG vor?
- Welcher Schaden ist durch die Verletzung entstanden?
- Sind strafrechtliche Konsequenzen nach § 23 GeschGehG zu prüfen?
- Ist die vertragliche NDA über § 88 HGB hinausgehend wirksam vereinbart?

## Typische Fallstricke

- Kein Nachweis angemessener Schutzmaßnahmen — kein Geschäftsgeheimnis nach GeschGehG.
- Strafrechtliche Dimension nach § 23 GeschGehG nicht erkannt.
- NDA-Klausel zu weit — nach § 307 BGB teilweise nichtig.
- Schadensersatz nach § 10 GeschGehG nicht beziffert — Klage abgewiesen.

## Output

NDA-Prüfvermerk, Schadensersatzberechnung nach GeschGehG, Strafanzeige-Vorbereitung.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben zentrale Rechtsfragen durch Leitentscheidungen geklärt.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter zwingend.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) und Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltung (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen den praxisrelevanten Rechtsrahmen.
Für internationale Sachverhalte gilt zudem die Rom-I-Verordnung für das anwendbare Recht.

## Quellen

- [§ 88 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__88.html)
- [§ 2 GeschGehG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/__2.html)
- [§ 10 GeschGehG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/__10.html)
- [§ 23 GeschGehG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/__23.html)
- [Dejure § 88 HGB](https://dejure.org/gesetze/HGB/88.html)
