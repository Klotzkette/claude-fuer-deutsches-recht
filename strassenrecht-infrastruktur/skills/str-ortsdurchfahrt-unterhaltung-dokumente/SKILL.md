---
name: str-ortsdurchfahrt-unterhaltung-dokumente
description: "STR Ortsdurchfahrt Unterhaltung Dokumente: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STR Ortsdurchfahrt Unterhaltung Dokumente

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **STR Ortsdurchfahrt Unterhaltung Dokumente** im Plugin Strassenrecht Infrastruktur. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `str-078-ortsdurchfahrt-unterhaltung-ruegen` | Straßenrecht und Infrastruktur: Ortsdurchfahrt: Unterhaltung rügen. Unterhaltung rügen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-079-ortsdurchfahrt-dokumente-sortieren` | Straßenrecht und Infrastruktur: Ortsdurchfahrt: Dokumente sortieren. Dokumente sortieren für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-080-ortsdurchfahrt-dashboard-erstellen` | Straßenrecht und Infrastruktur: Ortsdurchfahrt: Dashboard erstellen. Dashboard erstellen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `str-081-bruecke-baulast-pruefen` | Straßenrecht und Infrastruktur: Brücke: Baulast prüfen. Baulast prüfen für Brücke im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Im Plugin Strassenrecht Infrastruktur gilt für **STR Ortsdurchfahrt Unterhaltung Dokumente**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `str-078-ortsdurchfahrt-unterhaltung-ruegen`

**Fokus:** Straßenrecht und Infrastruktur: Ortsdurchfahrt: Unterhaltung rügen. Unterhaltung rügen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Ortsdurchfahrt Unterhaltung Ruegen

## Arbeitsauftrag

Ortsdurchfahrt Unterhaltung Ruegen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 2. `str-079-ortsdurchfahrt-dokumente-sortieren`

**Fokus:** Straßenrecht und Infrastruktur: Ortsdurchfahrt: Dokumente sortieren. Dokumente sortieren für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Ortsdurchfahrt Dokumente Sortieren

## Arbeitsauftrag

Ortsdurchfahrt Dokumente Sortieren wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 3. `str-080-ortsdurchfahrt-dashboard-erstellen`

**Fokus:** Straßenrecht und Infrastruktur: Ortsdurchfahrt: Dashboard erstellen. Dashboard erstellen für Ortsdurchfahrt im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Ortsdurchfahrt Dashboard Erstellen

## Arbeitsauftrag

Ortsdurchfahrt Dashboard Erstellen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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

## 4. `str-081-bruecke-baulast-pruefen`

**Fokus:** Straßenrecht und Infrastruktur: Brücke: Baulast prüfen. Baulast prüfen für Brücke im Rahmen von Straßenrecht und Infrastruktur; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Bruecke Baulast Pruefen

## Arbeitsauftrag

Bruecke Baulast Pruefen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Straßenrecht und Infrastruktur: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

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
