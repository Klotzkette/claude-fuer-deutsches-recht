---
name: kommunalrecht-laender-kom-schultraeger-zustaendigkeit-feuerwehr
description: "KOM Schultraeger Zustaendigkeit Feuerwehr: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KOM Schultraeger Zustaendigkeit Feuerwehr

## Arbeitsbereich

Dieser Skill bündelt 6 sachlich verwandte Arbeitsschritte rund um **KOM Schultraeger Zustaendigkeit Feuerwehr** im Plugin Kommunalrecht Laender. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kom-148-schultraeger-zustaendigkeit-pruefen` | Kommunalrecht der Länder: Schulträger: Zuständigkeit prüfen. Zuständigkeit prüfen für Schulträger im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `kom-158-feuerwehr-zustaendigkeit-pruefen` | Kommunalrecht der Länder: Feuerwehr: Zuständigkeit prüfen. Zuständigkeit prüfen für Feuerwehr im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `kom-010-kommunalabgaben-pruefen` | Kommunalrecht der Länder: Kommunalabgaben prüfen. Kommunalabgaben prüfen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `kom-117-kommunalabgabe-landesrecht-routen` | Kommunalrecht der Länder: Kommunalabgabe: Landesrecht routen. Landesrecht routen für Kommunalabgabe im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `kom-119-kommunalabgabe-beschluss-bauen` | Kommunalrecht der Länder: Kommunalabgabe: Beschluss bauen. Beschluss bauen für Kommunalabgabe im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `kom-120-kommunalabgabe-satzung-redlinen` | Kommunalrecht der Länder: Kommunalabgabe: Satzung redlinen. Satzung redlinen für Kommunalabgabe im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Kommunalrecht Laender gilt für **KOM Schultraeger Zustaendigkeit Feuerwehr**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kom-148-schultraeger-zustaendigkeit-pruefen`

**Fokus:** Kommunalrecht der Länder: Schulträger: Zuständigkeit prüfen. Zuständigkeit prüfen für Schulträger im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Schultraeger Zustaendigkeit Pruefen

## Arbeitsauftrag

Schultraeger Zustaendigkeit Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Kommunalrecht der Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Landesrechts-Navigator
- Beschluss-/Satzungscheck
- Bürgerbegehren-Fristenmatrix
- Kommunalaufsichts- und Haushaltsrisikoampel

## Red-Team-Fragen

- falsches Bundesland
- Organrolle verwechselt
- Satzungsbekanntmachung/Öffentlichkeit fehlt
- kommunale Finanzierung übersehen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `kom-158-feuerwehr-zustaendigkeit-pruefen`

**Fokus:** Kommunalrecht der Länder: Feuerwehr: Zuständigkeit prüfen. Zuständigkeit prüfen für Feuerwehr im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Feuerwehr Zustaendigkeit Pruefen

## Arbeitsauftrag

Feuerwehr Zustaendigkeit Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Kommunalrecht der Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Landesrechts-Navigator
- Beschluss-/Satzungscheck
- Bürgerbegehren-Fristenmatrix
- Kommunalaufsichts- und Haushaltsrisikoampel

## Red-Team-Fragen

- falsches Bundesland
- Organrolle verwechselt
- Satzungsbekanntmachung/Öffentlichkeit fehlt
- kommunale Finanzierung übersehen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `kom-010-kommunalabgaben-pruefen`

**Fokus:** Kommunalrecht der Länder: Kommunalabgaben prüfen. Kommunalabgaben prüfen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten.

# Kommunalabgaben Pruefen

## Arbeitsauftrag

Kommunalabgaben Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Kommunalrecht der Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Landesrechts-Navigator
- Beschluss-/Satzungscheck
- Bürgerbegehren-Fristenmatrix
- Kommunalaufsichts- und Haushaltsrisikoampel

## Red-Team-Fragen

- falsches Bundesland
- Organrolle verwechselt
- Satzungsbekanntmachung/Öffentlichkeit fehlt
- kommunale Finanzierung übersehen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `kom-117-kommunalabgabe-landesrecht-routen`

**Fokus:** Kommunalrecht der Länder: Kommunalabgabe: Landesrecht routen. Landesrecht routen für Kommunalabgabe im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Kommunalabgabe Landesrecht Routen

## Arbeitsauftrag

Kommunalabgabe Landesrecht Routen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Kommunalrecht der Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Landesrechts-Navigator
- Beschluss-/Satzungscheck
- Bürgerbegehren-Fristenmatrix
- Kommunalaufsichts- und Haushaltsrisikoampel

## Red-Team-Fragen

- falsches Bundesland
- Organrolle verwechselt
- Satzungsbekanntmachung/Öffentlichkeit fehlt
- kommunale Finanzierung übersehen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 5. `kom-119-kommunalabgabe-beschluss-bauen`

**Fokus:** Kommunalrecht der Länder: Kommunalabgabe: Beschluss bauen. Beschluss bauen für Kommunalabgabe im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Kommunalabgabe Beschluss Bauen

## Arbeitsauftrag

Kommunalabgabe Beschluss Bauen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Kommunalrecht der Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Landesrechts-Navigator
- Beschluss-/Satzungscheck
- Bürgerbegehren-Fristenmatrix
- Kommunalaufsichts- und Haushaltsrisikoampel

## Red-Team-Fragen

- falsches Bundesland
- Organrolle verwechselt
- Satzungsbekanntmachung/Öffentlichkeit fehlt
- kommunale Finanzierung übersehen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 6. `kom-120-kommunalabgabe-satzung-redlinen`

**Fokus:** Kommunalrecht der Länder: Kommunalabgabe: Satzung redlinen. Satzung redlinen für Kommunalabgabe im Rahmen von Kommunalrecht der Länder; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Kommunalabgabe Satzung Redlinen

## Arbeitsauftrag

Kommunalabgabe Satzung Redlinen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Kommunalrecht der Länder: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Landesrechts-Navigator
- Beschluss-/Satzungscheck
- Bürgerbegehren-Fristenmatrix
- Kommunalaufsichts- und Haushaltsrisikoampel

## Red-Team-Fragen

- falsches Bundesland
- Organrolle verwechselt
- Satzungsbekanntmachung/Öffentlichkeit fehlt
- kommunale Finanzierung übersehen

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
