---
name: vbr-smart-verbraucherrecht-abo
description: "Vbr 098 Smart Device Klagepfad Skizzieren, Vbr 099 Smart Device Vergleich Vorschlagen, Verbraucherrecht Abo Kündigung Button, Verbraucherrecht Behörden Beschwerden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Vbr 098 Smart Device Klagepfad Skizzieren, Vbr 099 Smart Device Vergleich Vorschlagen, Verbraucherrecht Abo Kündigung Button, Verbraucherrecht Behörden Beschwerden

## Arbeitsbereich

Dieser Skill bündelt **Vbr 098 Smart Device Klagepfad Skizzieren, Vbr 099 Smart Device Vergleich Vorschlagen, Verbraucherrecht Abo Kündigung Button, Verbraucherrecht Behörden Beschwerden** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `vbr-098-smart-device-klagepfad-skizzieren` | Verbraucherschutzrecht Prüfer: Smart Device: Klagepfad skizzieren. Klagepfad skizzieren für Smart Device im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `vbr-099-smart-device-vergleich-vorschlagen` | Verbraucherschutzrecht Prüfer: Smart Device: Vergleich vorschlagen. Vergleich vorschlagen für Smart Device im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `verbraucherrecht-abo-kuendigung-button` | Abo, Kündigungsbutton und Laufzeitfallen: Dauerschuldverhältnis, Online-Kündigung, Verlängerung und Nachweis.; Normanker: BGB § 312k, § 309 Nr. 9; UWG; liefert Verbraucher-Check, Beweisfragen, Anspruchsziel und Textbaustein. |
| `verbraucherrecht-behoerden-beschwerden` | Behörden- und Ombudsstellenrouter: Verbraucherzentrale, Schlichtung, BaFin, BNetzA, Datenschutz, Marktüberwachung.; Normanker: VSBG; Fachaufsichtsrecht; DSGVO; EnWG/BNetzA; liefert Verbraucher-Check, Beweisfragen, Anspruchsziel und Textbaustein. |

## Arbeitsweg

Für **Vbr 098 Smart Device Klagepfad Skizzieren, Vbr 099 Smart Device Vergleich Vorschlagen, Verbraucherrecht Abo Kündigung Button, Verbraucherrecht Behörden Beschwerden** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verbraucherschutzrecht-pruefer` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `vbr-098-smart-device-klagepfad-skizzieren`

**Fokus:** Verbraucherschutzrecht Prüfer: Smart Device: Klagepfad skizzieren. Klagepfad skizzieren für Smart Device im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Smart Device Klagepfad Skizzieren

## Arbeitsauftrag

Smart Device Klagepfad Skizzieren wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Verbraucherschutzrecht allgemein: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BGB-Verbrauchervertragsrecht, Widerruf, digitale Produkte
- UWG, UKlaG, VSBG, PAngV, Fernabsatz, E-Commerce
- Produktsicherheit, Right to Repair, Gewährleistung
- EU-Verbraucherrecht live gegen EUR-Lex/Bundesrecht prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Verbraucherrechte-Ampel
- Anspruchs- und Fristenmatrix
- Anschreiben an Unternehmer/Plattform
- Beweis- und Screenshotplan

## Red-Team-Fragen

- B2C/B2B-Rolle unklar
- Widerrufsfrist/Beweislast falsch gerechnet
- Plattform- und Händlerrolle vermischt
- AGB-Kontrolle ohne Einbeziehungskontrolle

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `vbr-099-smart-device-vergleich-vorschlagen`

**Fokus:** Verbraucherschutzrecht Prüfer: Smart Device: Vergleich vorschlagen. Vergleich vorschlagen für Smart Device im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Smart Device Vergleich Vorschlagen

## Arbeitsauftrag

Smart Device Vergleich Vorschlagen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Verbraucherschutzrecht allgemein: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BGB-Verbrauchervertragsrecht, Widerruf, digitale Produkte
- UWG, UKlaG, VSBG, PAngV, Fernabsatz, E-Commerce
- Produktsicherheit, Right to Repair, Gewährleistung
- EU-Verbraucherrecht live gegen EUR-Lex/Bundesrecht prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Verbraucherrechte-Ampel
- Anspruchs- und Fristenmatrix
- Anschreiben an Unternehmer/Plattform
- Beweis- und Screenshotplan

## Red-Team-Fragen

- B2C/B2B-Rolle unklar
- Widerrufsfrist/Beweislast falsch gerechnet
- Plattform- und Händlerrolle vermischt
- AGB-Kontrolle ohne Einbeziehungskontrolle

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `verbraucherrecht-abo-kuendigung-button`

**Fokus:** Abo, Kündigungsbutton und Laufzeitfallen: Dauerschuldverhältnis, Online-Kündigung, Verlängerung und Nachweis.; Normanker: BGB § 312k, § 309 Nr. 9; UWG; liefert Verbraucher-Check, Beweisfragen, Anspruchsziel und Textbaustein.

# Abo, Kündigungsbutton und Laufzeitfallen: Dauerschuldverhältnis, Online-Kündigung, Verlängerung und Nachweis.

## Fachkern: Abo, Kündigungsbutton und Laufzeitfallen: Dauerschuldverhältnis, Online-Kündigung, Verlängerung und Nachweis.

- **Verbraucherproblem (Abo, Kündigungsbutton und Laufzeitfallen: Dauerschuldverhältnis, Online-Kündigung, Verlängerung und Nachweis.):** Dauerschuldverhältnis, Online-Kündigung, Verlängerung und Nachweis.
- **Beleganker:** Vertrag, Screenshot, Rechnung, Widerrufsbelehrung, AGB, Plattformseite, Zahlungsfluss und Kommunikation müssen als Anspruchsbelege geordnet werden.
- **Normenanker:** BGB-Verbraucherrecht, EGBGB-Informationspflichten, UWG/UKlaG, DSGVO-Schnittstellen und Spezialrecht live prüfen.
- **Arbeitsprodukt:** Verbraucher-Check, Anspruchsziel, Beweisfragen und kurzer Textbaustein ohne unnötige Selbstbelastung.

## Normanker

BGB § 312k, § 309 Nr. 9; UWG. Der aktuelle Normtext, insbesondere BGB/EGBGB und Spezialrecht, ist bei frist- oder anspruchstragenden Punkten live zu prüfen.

## Prüfprogramm

1. Verbraucherstatus, Unternehmerseite, Vertragstyp und Zeitpunkt klären.
2. Pflichtinformation, Einwilligung, Widerruf, Preis, Lieferung/Bereitstellung und Mangel trennen.
3. Beweis sichern: Screenshot mit URL/Datum, Rechnung, Chat, E-Mail, Tracking, Produktfoto, Updatehistorie.
4. Anspruchsziel wählen: Rücktritt, Minderung, Nacherfüllung, Widerruf, Unterlassung, Beschwerde, Schlichtung oder Klage.
5. Textbaustein erstellen, der keine unnötigen Tatsachen zugibt und Fristen sauber setzt.

## 4. `verbraucherrecht-behoerden-beschwerden`

**Fokus:** Behörden- und Ombudsstellenrouter: Verbraucherzentrale, Schlichtung, BaFin, BNetzA, Datenschutz, Marktüberwachung.; Normanker: VSBG; Fachaufsichtsrecht; DSGVO; EnWG/BNetzA; liefert Verbraucher-Check, Beweisfragen, Anspruchsziel und Textbaustein.

# Behörden- und Ombudsstellenrouter: Verbraucherzentrale, Schlichtung, BaFin, BNetzA, Datenschutz, Marktüberwachung.

## Fachkern: Behörden- und Ombudsstellenrouter: Verbraucherzentrale, Schlichtung, BaFin, BNetzA, Datenschutz, Marktüberwachung.

- **Verbraucherproblem (Behörden- und Ombudsstellenrouter: Verbraucherzentrale, Schlichtung, BaFin, BNetzA, Datenschutz, Marktüberwachung.):** Verbraucherzentrale, Schlichtung, BaFin, BNetzA, Datenschutz, Marktüberwachung.
- **Beleganker:** Vertrag, Screenshot, Rechnung, Widerrufsbelehrung, AGB, Plattformseite, Zahlungsfluss und Kommunikation müssen als Anspruchsbelege geordnet werden.
- **Normenanker:** BGB-Verbraucherrecht, EGBGB-Informationspflichten, UWG/UKlaG, DSGVO-Schnittstellen und Spezialrecht live prüfen.
- **Arbeitsprodukt:** Verbraucher-Check, Anspruchsziel, Beweisfragen und kurzer Textbaustein ohne unnötige Selbstbelastung.

## Normanker

VSBG; Fachaufsichtsrecht; DSGVO; EnWG/BNetzA. Der aktuelle Normtext, insbesondere BGB/EGBGB und Spezialrecht, ist bei frist- oder anspruchstragenden Punkten live zu prüfen.

## Prüfprogramm

1. Verbraucherstatus, Unternehmerseite, Vertragstyp und Zeitpunkt klären.
2. Pflichtinformation, Einwilligung, Widerruf, Preis, Lieferung/Bereitstellung und Mangel trennen.
3. Beweis sichern: Screenshot mit URL/Datum, Rechnung, Chat, E-Mail, Tracking, Produktfoto, Updatehistorie.
4. Anspruchsziel wählen: Rücktritt, Minderung, Nacherfüllung, Widerruf, Unterlassung, Beschwerde, Schlichtung oder Klage.
5. Textbaustein erstellen, der keine unnötigen Tatsachen zugibt und Fristen sauber setzt.
