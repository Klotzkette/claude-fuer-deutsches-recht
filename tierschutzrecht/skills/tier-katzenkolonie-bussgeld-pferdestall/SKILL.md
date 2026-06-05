---
name: tier-katzenkolonie-bussgeld-pferdestall
description: "Tier Katzenkolonie Bussgeld Pferdestall: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Tier Katzenkolonie Bussgeld Pferdestall

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Tier Katzenkolonie Bussgeld Pferdestall** im Plugin Tierschutzrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tier-036-katzenkolonie-bussgeld-verteidigen` | Tierschutzrecht: Katzenkolonie: Bußgeld verteidigen. Bußgeld verteidigen für Katzenkolonie im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `tier-046-pferdestall-bussgeld-verteidigen` | Tierschutzrecht: Pferdestall: Bußgeld verteidigen. Bußgeld verteidigen für Pferdestall im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `tier-056-rinderbetrieb-bussgeld-verteidigen` | Tierschutzrecht: Rinderbetrieb: Bußgeld verteidigen. Bußgeld verteidigen für Rinderbetrieb im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `tier-066-schweinehaltung-bussgeld-verteidigen` | Tierschutzrecht: Schweinehaltung: Bußgeld verteidigen. Bußgeld verteidigen für Schweinehaltung im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Tierschutzrecht gilt für **Tier Katzenkolonie Bussgeld Pferdestall**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tier-036-katzenkolonie-bussgeld-verteidigen`

**Fokus:** Tierschutzrecht: Katzenkolonie: Bußgeld verteidigen. Bußgeld verteidigen für Katzenkolonie im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Katzenkolonie Bussgeld Verteidigen

## Arbeitsauftrag

Katzenkolonie Bussgeld Verteidigen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Tierschutzrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tierwohl- und Haltungscheck
- Anordnungs-/Bescheidanalyse
- Eilantrag oder Behördenantwort
- Beweisplan mit Fotos, Vet-Befunden, Zeugen

## Red-Team-Fragen

- Tiere wie bloße Sachen behandeln
- Gefahr im Verzug übersehen
- Beweissicherung emotional statt fachlich
- Tierhalterrolle/Eigentum/Besitz unklar

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `tier-046-pferdestall-bussgeld-verteidigen`

**Fokus:** Tierschutzrecht: Pferdestall: Bußgeld verteidigen. Bußgeld verteidigen für Pferdestall im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Pferdestall Bussgeld Verteidigen

## Arbeitsauftrag

Pferdestall Bussgeld Verteidigen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Tierschutzrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tierwohl- und Haltungscheck
- Anordnungs-/Bescheidanalyse
- Eilantrag oder Behördenantwort
- Beweisplan mit Fotos, Vet-Befunden, Zeugen

## Red-Team-Fragen

- Tiere wie bloße Sachen behandeln
- Gefahr im Verzug übersehen
- Beweissicherung emotional statt fachlich
- Tierhalterrolle/Eigentum/Besitz unklar

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `tier-056-rinderbetrieb-bussgeld-verteidigen`

**Fokus:** Tierschutzrecht: Rinderbetrieb: Bußgeld verteidigen. Bußgeld verteidigen für Rinderbetrieb im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Rinderbetrieb Bussgeld Verteidigen

## Arbeitsauftrag

Rinderbetrieb Bussgeld Verteidigen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Tierschutzrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tierwohl- und Haltungscheck
- Anordnungs-/Bescheidanalyse
- Eilantrag oder Behördenantwort
- Beweisplan mit Fotos, Vet-Befunden, Zeugen

## Red-Team-Fragen

- Tiere wie bloße Sachen behandeln
- Gefahr im Verzug übersehen
- Beweissicherung emotional statt fachlich
- Tierhalterrolle/Eigentum/Besitz unklar

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `tier-066-schweinehaltung-bussgeld-verteidigen`

**Fokus:** Tierschutzrecht: Schweinehaltung: Bußgeld verteidigen. Bußgeld verteidigen für Schweinehaltung im Rahmen von Tierschutzrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Schweinehaltung Bussgeld Verteidigen

## Arbeitsauftrag

Schweinehaltung Bussgeld Verteidigen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Tierschutzrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tierwohl- und Haltungscheck
- Anordnungs-/Bescheidanalyse
- Eilantrag oder Behördenantwort
- Beweisplan mit Fotos, Vet-Befunden, Zeugen

## Red-Team-Fragen

- Tiere wie bloße Sachen behandeln
- Gefahr im Verzug übersehen
- Beweissicherung emotional statt fachlich
- Tierhalterrolle/Eigentum/Besitz unklar

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
