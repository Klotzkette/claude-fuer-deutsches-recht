---
name: stv-lieferzone-risiko-ladezone-regel-zeichen
description: "STV Lieferzone Risiko Ladezone Regel Zeichen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STV Lieferzone Risiko Ladezone Regel Zeichen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **STV Lieferzone Risiko Ladezone Regel Zeichen** im Plugin Strassenverkehrsrecht Stvo. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stv-080-lieferzone-risiko-erklaeren` | Straßenverkehrsrecht StVO: Lieferzone: Risiko erklären. Risiko erklären für Lieferzone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `stv-081-ladezone-regel-pruefen` | Straßenverkehrsrecht StVO: Ladezone: Regel prüfen. Regel prüfen für Ladezone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `stv-082-ladezone-zeichen-auslegen` | Straßenverkehrsrecht StVO: Ladezone: Zeichen auslegen. Zeichen auslegen für Ladezone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `stv-083-ladezone-anordnung-angreifen` | Straßenverkehrsrecht StVO: Ladezone: Anordnung angreifen. Anordnung angreifen für Ladezone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Strassenverkehrsrecht Stvo gilt für **STV Lieferzone Risiko Ladezone Regel Zeichen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stv-080-lieferzone-risiko-erklaeren`

**Fokus:** Straßenverkehrsrecht StVO: Lieferzone: Risiko erklären. Risiko erklären für Lieferzone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Lieferzone Risiko Erklaeren

## Arbeitsauftrag

Lieferzone Risiko Erklaeren wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 2. `stv-081-ladezone-regel-pruefen`

**Fokus:** Straßenverkehrsrecht StVO: Ladezone: Regel prüfen. Regel prüfen für Ladezone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Ladezone Regel Pruefen

## Arbeitsauftrag

Ladezone Regel Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 3. `stv-082-ladezone-zeichen-auslegen`

**Fokus:** Straßenverkehrsrecht StVO: Ladezone: Zeichen auslegen. Zeichen auslegen für Ladezone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Ladezone Zeichen Auslegen

## Arbeitsauftrag

Ladezone Zeichen Auslegen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 4. `stv-083-ladezone-anordnung-angreifen`

**Fokus:** Straßenverkehrsrecht StVO: Ladezone: Anordnung angreifen. Anordnung angreifen für Ladezone im Rahmen von Straßenverkehrsrecht StVO; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Ladezone Anordnung Angreifen

## Arbeitsauftrag

Ladezone Anordnung Angreifen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenverkehrsrecht und StVO: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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
