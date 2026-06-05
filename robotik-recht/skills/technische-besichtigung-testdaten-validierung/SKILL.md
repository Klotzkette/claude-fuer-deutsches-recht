---
name: technische-besichtigung-testdaten-validierung
description: "Technische Besichtigung Testdaten Validierung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Technische Besichtigung Testdaten Validierung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Technische Besichtigung Testdaten Validierung** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `technische-besichtigung-und-geheimnisschutz` | Plant gerichtliche oder außergerichtliche Besichtigung eines Roboters mit Geheimnisschutz, Sachverständigem und Testprotokoll. |
| `testdaten-und-validierung-vor-marktstart` | Prüft Testdaten, Validierungsplan, Feldtest, Pilotkunden, Beta-Betrieb und regulatorische Grenzen vor Marktstart. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Technische Besichtigung Testdaten Validierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `technische-besichtigung-und-geheimnisschutz`

**Fokus:** Plant gerichtliche oder außergerichtliche Besichtigung eines Roboters mit Geheimnisschutz, Sachverständigem und Testprotokoll.


# Technische Besichtigung und Geheimnisschutz

## Fachkern: Technische Besichtigung und Geheimnisschutz
- **Spezialgegenstand:** Technische Besichtigung und Geheimnisschutz wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Plant gerichtliche oder außergerichtliche Besichtigung eines Roboters mit Geheimnisschutz, Sachverständigem und Testprotokoll.**

Quellen-/Normenanker: ZPO, GeschGehG, Produkthaftung.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 2. `testdaten-und-validierung-vor-marktstart`

**Fokus:** Prüft Testdaten, Validierungsplan, Feldtest, Pilotkunden, Beta-Betrieb und regulatorische Grenzen vor Marktstart.


# Testdaten und Validierung

## Fachkern: Testdaten und Validierung
- **Spezialgegenstand:** Testdaten und Validierung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Prüft Testdaten, Validierungsplan, Feldtest, Pilotkunden, Beta-Betrieb und regulatorische Grenzen vor Marktstart.**

Quellen-/Normenanker: Maschinenverordnung, KI-VO, DSGVO, Vertragsrecht.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.
