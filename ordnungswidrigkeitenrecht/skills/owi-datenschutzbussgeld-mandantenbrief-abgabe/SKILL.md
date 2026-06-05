---
name: owi-datenschutzbussgeld-mandantenbrief-abgabe
description: "OWI Datenschutzbussgeld Mandantenbrief Abgabe: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# OWI Datenschutzbussgeld Mandantenbrief Abgabe

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **OWI Datenschutzbussgeld Mandantenbrief Abgabe** im Plugin Ordnungswidrigkeitenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `owi-030-datenschutzbussgeld-mandantenbrief-sch` | Ordnungswidrigkeitenrecht: Datenschutzbußgeld: Mandantenbrief schreiben. Mandantenbrief schreiben für Datenschutzbußgeld im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `owi-014-abgabe-an-staatsanwaltschaft` | Ordnungswidrigkeitenrecht: Abgabe an Staatsanwaltschaft. Abgabe an Staatsanwaltschaft im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `owi-002-tatbestand-fachgesetz-finden` | Ordnungswidrigkeitenrecht: Tatbestand Fachgesetz finden. Tatbestand Fachgesetz finden im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `owi-003-anhoerung-richtig-behandeln` | Ordnungswidrigkeitenrecht: Anhörung richtig behandeln. Anhörung richtig behandeln im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |

## Arbeitsweg

Im Plugin Ordnungswidrigkeitenrecht gilt für **OWI Datenschutzbussgeld Mandantenbrief Abgabe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `owi-030-datenschutzbussgeld-mandantenbrief-sch`

**Fokus:** Ordnungswidrigkeitenrecht: Datenschutzbußgeld: Mandantenbrief schreiben. Mandantenbrief schreiben für Datenschutzbußgeld im Rahmen von Ordnungswidrigkeitenrecht; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Datenschutzbussgeld Mandantenbrief Sch

## Arbeitsauftrag

Datenschutzbussgeld Mandantenbrief Sch wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 2. `owi-014-abgabe-an-staatsanwaltschaft`

**Fokus:** Ordnungswidrigkeitenrecht: Abgabe an Staatsanwaltschaft. Abgabe an Staatsanwaltschaft im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Abgabe An Staatsanwaltschaft

## Arbeitsauftrag

Abgabe An Staatsanwaltschaft wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 3. `owi-002-tatbestand-fachgesetz-finden`

**Fokus:** Ordnungswidrigkeitenrecht: Tatbestand Fachgesetz finden. Tatbestand Fachgesetz finden im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Tatbestand Fachgesetz Finden

## Arbeitsauftrag

Tatbestand Fachgesetz Finden wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 4. `owi-003-anhoerung-richtig-behandeln`

**Fokus:** Ordnungswidrigkeitenrecht: Anhörung richtig behandeln. Anhörung richtig behandeln im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Anhoerung Richtig Behandeln

## Arbeitsauftrag

Anhoerung Richtig Behandeln wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Ordnungswidrigkeitenrecht: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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
