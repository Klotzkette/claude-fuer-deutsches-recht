---
name: stv-schulstrasse-bussgeld-verkehrszeichen
description: "STV Schulstrasse Bussgeld Verkehrszeichen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STV Schulstrasse Bussgeld Verkehrszeichen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **STV Schulstrasse Bussgeld Verkehrszeichen** im Plugin Strassenverkehrsrecht Stvo. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stv-096-schulstrasse-bussgeld-abgrenzen` | Straßenverkehrsrecht StVO: Schulstraße: Bußgeld abgrenzen. Bußgeld abgrenzen für Schulstraße im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `stv-002-verkehrszeichen-lesen` | Straßenverkehrsrecht StVO: Verkehrszeichen lesen. Verkehrszeichen lesen im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `stv-003-verkehrsrechtliche-anordnung-pruefen` | Straßenverkehrsrecht StVO: Verkehrsrechtliche Anordnung prüfen. Verkehrsrechtliche Anordnung prüfen im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `stv-004-tempozone-und-beschilderung` | Straßenverkehrsrecht StVO: Tempozone und Beschilderung. Tempozone und Beschilderung im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |

## Arbeitsweg

Im Plugin Strassenverkehrsrecht Stvo gilt für **STV Schulstrasse Bussgeld Verkehrszeichen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stv-096-schulstrasse-bussgeld-abgrenzen`

**Fokus:** Straßenverkehrsrecht StVO: Schulstraße: Bußgeld abgrenzen. Bußgeld abgrenzen für Schulstraße im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Schulstrasse Bussgeld Abgrenzen

## Arbeitsauftrag

Schulstrasse Bussgeld Abgrenzen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- StVO, StVG, FeV, VwV-StVO, BKatV
- Verkehrszeichen, Anordnung, Halt-/Parken, Lieferzonen, Schulstraßen
- Fahrerlaubnis, Punkte, MPU, Gefahrenabwehr, Verkehrsüberwachung
- OWiG/StPO-Schnittstelle und Rechtsschutz gegen Anordnungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tat-/Anordnungscheck
- Verkehrszeichen- und Bekanntgabematrix
- Einspruchs-/Widerspruchsfahrplan
- Beweisplan mit Fotos, Messung, Zeugen, Akteneinsicht

## Red-Team-Fragen

- StVO-Verstoß und Verwaltungsakt vermischt
- Zeichen nicht wirksam bekanntgegeben
- Fahrer/Halter/Betroffener verwechselt
- Fristen und Fahrverbot nicht getrackt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `stv-002-verkehrszeichen-lesen`

**Fokus:** Straßenverkehrsrecht StVO: Verkehrszeichen lesen. Verkehrszeichen lesen im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Verkehrszeichen Lesen

## Arbeitsauftrag

Verkehrszeichen Lesen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- StVO, StVG, FeV, VwV-StVO, BKatV
- Verkehrszeichen, Anordnung, Halt-/Parken, Lieferzonen, Schulstraßen
- Fahrerlaubnis, Punkte, MPU, Gefahrenabwehr, Verkehrsüberwachung
- OWiG/StPO-Schnittstelle und Rechtsschutz gegen Anordnungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tat-/Anordnungscheck
- Verkehrszeichen- und Bekanntgabematrix
- Einspruchs-/Widerspruchsfahrplan
- Beweisplan mit Fotos, Messung, Zeugen, Akteneinsicht

## Red-Team-Fragen

- StVO-Verstoß und Verwaltungsakt vermischt
- Zeichen nicht wirksam bekanntgegeben
- Fahrer/Halter/Betroffener verwechselt
- Fristen und Fahrverbot nicht getrackt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `stv-003-verkehrsrechtliche-anordnung-pruefen`

**Fokus:** Straßenverkehrsrecht StVO: Verkehrsrechtliche Anordnung prüfen. Verkehrsrechtliche Anordnung prüfen im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Verkehrsrechtliche Anordnung Pruefen

## Arbeitsauftrag

Verkehrsrechtliche Anordnung Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- StVO, StVG, FeV, VwV-StVO, BKatV
- Verkehrszeichen, Anordnung, Halt-/Parken, Lieferzonen, Schulstraßen
- Fahrerlaubnis, Punkte, MPU, Gefahrenabwehr, Verkehrsüberwachung
- OWiG/StPO-Schnittstelle und Rechtsschutz gegen Anordnungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tat-/Anordnungscheck
- Verkehrszeichen- und Bekanntgabematrix
- Einspruchs-/Widerspruchsfahrplan
- Beweisplan mit Fotos, Messung, Zeugen, Akteneinsicht

## Red-Team-Fragen

- StVO-Verstoß und Verwaltungsakt vermischt
- Zeichen nicht wirksam bekanntgegeben
- Fahrer/Halter/Betroffener verwechselt
- Fristen und Fahrverbot nicht getrackt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `stv-004-tempozone-und-beschilderung`

**Fokus:** Straßenverkehrsrecht StVO: Tempozone und Beschilderung. Tempozone und Beschilderung im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Tempozone Und Beschilderung

## Arbeitsauftrag

Tempozone Und Beschilderung wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- StVO, StVG, FeV, VwV-StVO, BKatV
- Verkehrszeichen, Anordnung, Halt-/Parken, Lieferzonen, Schulstraßen
- Fahrerlaubnis, Punkte, MPU, Gefahrenabwehr, Verkehrsüberwachung
- OWiG/StPO-Schnittstelle und Rechtsschutz gegen Anordnungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Tat-/Anordnungscheck
- Verkehrszeichen- und Bekanntgabematrix
- Einspruchs-/Widerspruchsfahrplan
- Beweisplan mit Fotos, Messung, Zeugen, Akteneinsicht

## Red-Team-Fragen

- StVO-Verstoß und Verwaltungsakt vermischt
- Zeichen nicht wirksam bekanntgegeben
- Fahrer/Halter/Betroffener verwechselt
- Fristen und Fahrverbot nicht getrackt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
