---
name: str-kreisstrasse-unterhaltung-dokumente
description: "STR Kreisstrasse Unterhaltung Dokumente: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STR Kreisstrasse Unterhaltung Dokumente

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **STR Kreisstrasse Unterhaltung Dokumente** im Plugin Strassenrecht Infrastruktur. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `str-058-kreisstrasse-unterhaltung-ruegen` | Straßenrecht und Infrastruktur: Kreisstraße: Unterhaltung rügen. Unterhaltung rügen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-059-kreisstrasse-dokumente-sortieren` | Straßenrecht und Infrastruktur: Kreisstraße: Dokumente sortieren. Dokumente sortieren für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-060-kreisstrasse-dashboard-erstellen` | Straßenrecht und Infrastruktur: Kreisstraße: Dashboard erstellen. Dashboard erstellen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-061-gemeindestrasse-baulast-pruefen` | Straßenrecht und Infrastruktur: Gemeindestraße: Baulast prüfen. Baulast prüfen für Gemeindestraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Strassenrecht Infrastruktur gilt für **STR Kreisstrasse Unterhaltung Dokumente**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `str-058-kreisstrasse-unterhaltung-ruegen`

**Fokus:** Straßenrecht und Infrastruktur: Kreisstraße: Unterhaltung rügen. Unterhaltung rügen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Kreisstrasse Unterhaltung Ruegen

## Arbeitsauftrag

Kreisstrasse Unterhaltung Ruegen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- FStrG, Landesstraßengesetze, Straßenbaulast, Widmung, Einziehung
- Planfeststellung, Plangenehmigung, Umweltprüfung, Grunderwerb
- Sondernutzung, Anlieger, Verkehrssicherung, Finanzierung
- VwGO-Rechtsschutz, Enteignung, Kreuzungen, Leitungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Straßenklassifizierungs- und Baulastcheck
- Planungs- und Genehmigungsfahrplan
- Sondernutzungs-/Anliegermatrix
- Rechtsschutz- und Fristenblatt

## Red-Team-Fragen

- Straßenklasse falsch
- Widmung/Sondernutzung verwechselt
- Umwelt- oder Grunderwerbsfolge übersehen
- Baulastträger falsch adressiert

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `str-059-kreisstrasse-dokumente-sortieren`

**Fokus:** Straßenrecht und Infrastruktur: Kreisstraße: Dokumente sortieren. Dokumente sortieren für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Kreisstrasse Dokumente Sortieren

## Arbeitsauftrag

Kreisstrasse Dokumente Sortieren wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- FStrG, Landesstraßengesetze, Straßenbaulast, Widmung, Einziehung
- Planfeststellung, Plangenehmigung, Umweltprüfung, Grunderwerb
- Sondernutzung, Anlieger, Verkehrssicherung, Finanzierung
- VwGO-Rechtsschutz, Enteignung, Kreuzungen, Leitungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Straßenklassifizierungs- und Baulastcheck
- Planungs- und Genehmigungsfahrplan
- Sondernutzungs-/Anliegermatrix
- Rechtsschutz- und Fristenblatt

## Red-Team-Fragen

- Straßenklasse falsch
- Widmung/Sondernutzung verwechselt
- Umwelt- oder Grunderwerbsfolge übersehen
- Baulastträger falsch adressiert

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `str-060-kreisstrasse-dashboard-erstellen`

**Fokus:** Straßenrecht und Infrastruktur: Kreisstraße: Dashboard erstellen. Dashboard erstellen für Kreisstraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Kreisstrasse Dashboard Erstellen

## Arbeitsauftrag

Kreisstrasse Dashboard Erstellen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- FStrG, Landesstraßengesetze, Straßenbaulast, Widmung, Einziehung
- Planfeststellung, Plangenehmigung, Umweltprüfung, Grunderwerb
- Sondernutzung, Anlieger, Verkehrssicherung, Finanzierung
- VwGO-Rechtsschutz, Enteignung, Kreuzungen, Leitungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Straßenklassifizierungs- und Baulastcheck
- Planungs- und Genehmigungsfahrplan
- Sondernutzungs-/Anliegermatrix
- Rechtsschutz- und Fristenblatt

## Red-Team-Fragen

- Straßenklasse falsch
- Widmung/Sondernutzung verwechselt
- Umwelt- oder Grunderwerbsfolge übersehen
- Baulastträger falsch adressiert

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `str-061-gemeindestrasse-baulast-pruefen`

**Fokus:** Straßenrecht und Infrastruktur: Gemeindestraße: Baulast prüfen. Baulast prüfen für Gemeindestraße im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Gemeindestrasse Baulast Pruefen

## Arbeitsauftrag

Gemeindestrasse Baulast Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- FStrG, Landesstraßengesetze, Straßenbaulast, Widmung, Einziehung
- Planfeststellung, Plangenehmigung, Umweltprüfung, Grunderwerb
- Sondernutzung, Anlieger, Verkehrssicherung, Finanzierung
- VwGO-Rechtsschutz, Enteignung, Kreuzungen, Leitungen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Straßenklassifizierungs- und Baulastcheck
- Planungs- und Genehmigungsfahrplan
- Sondernutzungs-/Anliegermatrix
- Rechtsschutz- und Fristenblatt

## Red-Team-Fragen

- Straßenklasse falsch
- Widmung/Sondernutzung verwechselt
- Umwelt- oder Grunderwerbsfolge übersehen
- Baulastträger falsch adressiert

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
