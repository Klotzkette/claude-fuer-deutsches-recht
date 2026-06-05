---
name: owi-gewerberecht-frist-umwelt
description: "OWI Gewerberecht Frist Umwelt: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# OWI Gewerberecht Frist Umwelt

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **OWI Gewerberecht Frist Umwelt** im Plugin Ordnungswidrigkeitenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `owi-032-gewerberecht-frist-pruefen` | Ordnungswidrigkeitenrecht: Gewerberecht: Frist prüfen. Frist prüfen für Gewerberecht im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `owi-042-umwelt-owi-frist-pruefen` | Ordnungswidrigkeitenrecht: Umwelt-OWi: Frist prüfen. Frist prüfen für Umwelt-OWi im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `owi-052-lebensmittelrecht-frist-pruefen` | Ordnungswidrigkeitenrecht: Lebensmittelrecht: Frist prüfen. Frist prüfen für Lebensmittelrecht im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `owi-062-tierschutz-owi-frist-pruefen` | Ordnungswidrigkeitenrecht: Tierschutz-OWi: Frist prüfen. Frist prüfen für Tierschutz-OWi im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Ordnungswidrigkeitenrecht gilt für **OWI Gewerberecht Frist Umwelt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `owi-032-gewerberecht-frist-pruefen`

**Fokus:** Ordnungswidrigkeitenrecht: Gewerberecht: Frist prüfen. Frist prüfen für Gewerberecht im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Gewerberecht Frist Pruefen

## Arbeitsauftrag

Gewerberecht Frist Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- OWiG, StPO-Verweisung, Bußgeldbescheid, Einspruch, Verjährung
- Verbandsgeldbuße, Einziehung, Opportunität, Verwarnung
- Amtsgericht, Staatsanwaltschaft, Rechtsbeschwerde
- Spezialmaterien: Verkehr, Datenschutz, Gewerbe, Umwelt, Tier, Zoll

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Bußgeldbescheid-Check
- Verjährungs- und Fristenkalender
- Einspruch/Begründung/Terminplan
- Beweis- und Akteneinsichtsstrategie

## Red-Team-Fragen

- Zustellung/Frist falsch
- Verjährungsunterbrechung übersehen
- Straf- und OWi-Verfahren vermischt
- Nebenfolgen/Einziehung vergessen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `owi-042-umwelt-owi-frist-pruefen`

**Fokus:** Ordnungswidrigkeitenrecht: Umwelt-OWi: Frist prüfen. Frist prüfen für Umwelt-OWi im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Umwelt Owi Frist Pruefen

## Arbeitsauftrag

Umwelt Owi Frist Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- OWiG, StPO-Verweisung, Bußgeldbescheid, Einspruch, Verjährung
- Verbandsgeldbuße, Einziehung, Opportunität, Verwarnung
- Amtsgericht, Staatsanwaltschaft, Rechtsbeschwerde
- Spezialmaterien: Verkehr, Datenschutz, Gewerbe, Umwelt, Tier, Zoll

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Bußgeldbescheid-Check
- Verjährungs- und Fristenkalender
- Einspruch/Begründung/Terminplan
- Beweis- und Akteneinsichtsstrategie

## Red-Team-Fragen

- Zustellung/Frist falsch
- Verjährungsunterbrechung übersehen
- Straf- und OWi-Verfahren vermischt
- Nebenfolgen/Einziehung vergessen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `owi-052-lebensmittelrecht-frist-pruefen`

**Fokus:** Ordnungswidrigkeitenrecht: Lebensmittelrecht: Frist prüfen. Frist prüfen für Lebensmittelrecht im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Lebensmittelrecht Frist Pruefen

## Arbeitsauftrag

Lebensmittelrecht Frist Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- OWiG, StPO-Verweisung, Bußgeldbescheid, Einspruch, Verjährung
- Verbandsgeldbuße, Einziehung, Opportunität, Verwarnung
- Amtsgericht, Staatsanwaltschaft, Rechtsbeschwerde
- Spezialmaterien: Verkehr, Datenschutz, Gewerbe, Umwelt, Tier, Zoll

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Bußgeldbescheid-Check
- Verjährungs- und Fristenkalender
- Einspruch/Begründung/Terminplan
- Beweis- und Akteneinsichtsstrategie

## Red-Team-Fragen

- Zustellung/Frist falsch
- Verjährungsunterbrechung übersehen
- Straf- und OWi-Verfahren vermischt
- Nebenfolgen/Einziehung vergessen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `owi-062-tierschutz-owi-frist-pruefen`

**Fokus:** Ordnungswidrigkeitenrecht: Tierschutz-OWi: Frist prüfen. Frist prüfen für Tierschutz-OWi im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Tierschutz Owi Frist Pruefen

## Arbeitsauftrag

Tierschutz Owi Frist Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- OWiG, StPO-Verweisung, Bußgeldbescheid, Einspruch, Verjährung
- Verbandsgeldbuße, Einziehung, Opportunität, Verwarnung
- Amtsgericht, Staatsanwaltschaft, Rechtsbeschwerde
- Spezialmaterien: Verkehr, Datenschutz, Gewerbe, Umwelt, Tier, Zoll

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Bußgeldbescheid-Check
- Verjährungs- und Fristenkalender
- Einspruch/Begründung/Terminplan
- Beweis- und Akteneinsichtsstrategie

## Red-Team-Fragen

- Zustellung/Frist falsch
- Verjährungsunterbrechung übersehen
- Straf- und OWi-Verfahren vermischt
- Nebenfolgen/Einziehung vergessen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
