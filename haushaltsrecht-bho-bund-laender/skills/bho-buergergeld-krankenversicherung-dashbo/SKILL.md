---
name: bho-buergergeld-krankenversicherung-dashbo
description: "Buergergeld Krankenversicherung Dashbo: bündelt 11 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Buergergeld Krankenversicherung Dashbo

## Arbeitsbereich

Dieser Skill bündelt 11 sachlich verwandte Arbeitsschritte rund um **Buergergeld Krankenversicherung Dashbo** im Plugin Haushaltsrecht (BHO Bund/Länder). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bho-080-buergergeld-krankenversicherung-szenar` | Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Szenario rechnen. Szenario rechnen für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-081-buergergeld-krankenversicherung-dashbo` | Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Dashboard bauen. Dashboard bauen für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-082-buergergeld-krankenversicherung-risiko` | Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Risiko markieren. Risiko markieren für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-083-buergergeld-krankenversicherung-brh-fr` | Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: BRH-Frage formulieren. BRH-Frage formulieren für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-084-buergergeld-krankenversicherung-parlam` | Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Parlamentsfrage vorbereiten. Parlamentsfrage vorbereiten für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-085-buergergeld-krankenversicherung-vollzu` | Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Vollzug tracken. Vollzug tracken für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-086-verteidigungsausgaben-titel-pruefen` | Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Titel prüfen. Titel prüfen für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-087-verteidigungsausgaben-umschichtung-sim` | Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Umschichtung simulieren. Umschichtung simulieren für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-088-verteidigungsausgaben-sperre-bewerten` | Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Sperre bewerten. Sperre bewerten für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-089-verteidigungsausgaben-deckung-finden` | Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Deckung finden. Deckung finden für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `bho-090-verteidigungsausgaben-szenario-rechnen` | Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Szenario rechnen. Szenario rechnen für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Haushaltsrecht (BHO Bund/Länder) gilt für **Buergergeld Krankenversicherung Dashbo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bho-080-buergergeld-krankenversicherung-szenar`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Szenario rechnen. Szenario rechnen für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Buergergeld Krankenversicherung Szenar

## Arbeitsauftrag

Buergergeld Krankenversicherung Szenar wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `bho-081-buergergeld-krankenversicherung-dashbo`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Dashboard bauen. Dashboard bauen für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Buergergeld Krankenversicherung Dashbo

## Arbeitsauftrag

Buergergeld Krankenversicherung Dashbo wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `bho-082-buergergeld-krankenversicherung-risiko`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Risiko markieren. Risiko markieren für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Buergergeld Krankenversicherung Risiko

## Arbeitsauftrag

Buergergeld Krankenversicherung Risiko wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `bho-083-buergergeld-krankenversicherung-brh-fr`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: BRH-Frage formulieren. BRH-Frage formulieren für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Buergergeld Krankenversicherung Brh Fr

## Arbeitsauftrag

Buergergeld Krankenversicherung Brh Fr wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 5. `bho-084-buergergeld-krankenversicherung-parlam`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Parlamentsfrage vorbereiten. Parlamentsfrage vorbereiten für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Buergergeld Krankenversicherung Parlam

## Arbeitsauftrag

Buergergeld Krankenversicherung Parlam wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 6. `bho-085-buergergeld-krankenversicherung-vollzu`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Bürgergeld-Krankenversicherung: Vollzug tracken. Vollzug tracken für Bürgergeld-Krankenversicherung im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Buergergeld Krankenversicherung Vollzu

## Arbeitsauftrag

Buergergeld Krankenversicherung Vollzu wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 7. `bho-086-verteidigungsausgaben-titel-pruefen`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Titel prüfen. Titel prüfen für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Verteidigungsausgaben Titel Pruefen

## Arbeitsauftrag

Verteidigungsausgaben Titel Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 8. `bho-087-verteidigungsausgaben-umschichtung-sim`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Umschichtung simulieren. Umschichtung simulieren für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Verteidigungsausgaben Umschichtung Sim

## Arbeitsauftrag

Verteidigungsausgaben Umschichtung Sim wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 9. `bho-088-verteidigungsausgaben-sperre-bewerten`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Sperre bewerten. Sperre bewerten für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Verteidigungsausgaben Sperre Bewerten

## Arbeitsauftrag

Verteidigungsausgaben Sperre Bewerten wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 10. `bho-089-verteidigungsausgaben-deckung-finden`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Deckung finden. Deckung finden für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Verteidigungsausgaben Deckung Finden

## Arbeitsauftrag

Verteidigungsausgaben Deckung Finden wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 11. `bho-090-verteidigungsausgaben-szenario-rechnen`

**Fokus:** Haushaltsrecht BHO Bund und Länder: Verteidigungsausgaben: Szenario rechnen. Szenario rechnen für Verteidigungsausgaben im Rahmen von Haushaltsrecht BHO Bund und Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Verteidigungsausgaben Szenario Rechnen

## Arbeitsauftrag

Verteidigungsausgaben Szenario Rechnen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Haushaltsrecht BHO Bund und Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BHO, HGrG, Haushaltsgesetz, Haushaltsplan, VV-BHO
- Einzelplan, Kapitel, Titel, Verpflichtungsermächtigung, Deckungsfähigkeit
- Art. 109, 110, 115 GG, Schuldenbremse, Sondervermögen
- Landeshaushaltsordnungen und kommunale Haushaltsbezüge live prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Titel- und Szenariomatrix
- Umschichtungs-/Nachtragshaushaltsvermerk
- Wirtschaftlichkeitsprüfung § 7 BHO
- Dashboard mit Ist/Soll, Sperren, Risiken, Entscheidungsoptionen

## Red-Team-Fragen

- Titelbindung/Deckungsfähigkeit ignoriert
- Sondervermögen politisch statt haushaltsrechtlich behandelt
- Verpflichtungsermächtigung vergessen
- Bund/Land/Kommune vermischt

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
