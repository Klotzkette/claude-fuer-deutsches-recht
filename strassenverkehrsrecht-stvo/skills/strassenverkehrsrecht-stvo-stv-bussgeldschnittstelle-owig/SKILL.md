---
name: strassenverkehrsrecht-stvo-stv-bussgeldschnittstelle-owig
description: "STV Bussgeldschnittstelle Owig: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STV Bussgeldschnittstelle Owig

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **STV Bussgeldschnittstelle Owig** im Plugin Strassenverkehrsrecht Stvo. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stv-017-bussgeldschnittstelle-owig` | Straßenverkehrsrecht StVO: Bußgeldschnittstelle OWiG. Bußgeldschnittstelle OWiG im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `stv-026-haltverbot-bussgeld-abgrenzen` | Straßenverkehrsrecht StVO: Haltverbot: Bußgeld abgrenzen. Bußgeld abgrenzen für Haltverbot im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `stv-036-tempo-30-bussgeld-abgrenzen` | Straßenverkehrsrecht StVO: Tempo 30: Bußgeld abgrenzen. Bußgeld abgrenzen für Tempo 30 im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `stv-046-fahrradstrasse-bussgeld-abgrenzen` | Straßenverkehrsrecht StVO: Fahrradstraße: Bußgeld abgrenzen. Bußgeld abgrenzen für Fahrradstraße im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Strassenverkehrsrecht Stvo gilt für **STV Bussgeldschnittstelle Owig**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stv-017-bussgeldschnittstelle-owig`

**Fokus:** Straßenverkehrsrecht StVO: Bußgeldschnittstelle OWiG. Bußgeldschnittstelle OWiG im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Bussgeldschnittstelle Owig

## Arbeitsauftrag

Bussgeldschnittstelle Owig wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 2. `stv-026-haltverbot-bussgeld-abgrenzen`

**Fokus:** Straßenverkehrsrecht StVO: Haltverbot: Bußgeld abgrenzen. Bußgeld abgrenzen für Haltverbot im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Haltverbot Bussgeld Abgrenzen

## Arbeitsauftrag

Haltverbot Bussgeld Abgrenzen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 3. `stv-036-tempo-30-bussgeld-abgrenzen`

**Fokus:** Straßenverkehrsrecht StVO: Tempo 30: Bußgeld abgrenzen. Bußgeld abgrenzen für Tempo 30 im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Tempo 30 Bussgeld Abgrenzen

## Arbeitsauftrag

Tempo 30 Bussgeld Abgrenzen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 4. `stv-046-fahrradstrasse-bussgeld-abgrenzen`

**Fokus:** Straßenverkehrsrecht StVO: Fahrradstraße: Bußgeld abgrenzen. Bußgeld abgrenzen für Fahrradstraße im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Fahrradstrasse Bussgeld Abgrenzen

## Arbeitsauftrag

Fahrradstrasse Bussgeld Abgrenzen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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
