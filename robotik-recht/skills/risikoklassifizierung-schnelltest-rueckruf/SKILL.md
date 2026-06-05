---
name: risikoklassifizierung-schnelltest-rueckruf
description: "Risikoklassifizierung Schnelltest Rueckruf: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Risikoklassifizierung Schnelltest Rueckruf

## Arbeitsbereich

Dieser Skill bündelt 6 sachlich verwandte Arbeitsschritte rund um **Risikoklassifizierung Schnelltest Rueckruf** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-risikoklassifizierung-schnelltest` | Führt durch Risikoklassen: Maschine, Sicherheitsbauteil, Hochrisiko-KI, Medizinprodukt, Verbraucherprodukt, kritische Infrastruktur, Beschäftigtendaten. |
| `workflow-rueckruf-und-field-action` | Plant freiwillige oder behördliche Korrekturmaßnahme: Risiko, Reichweite, Kundenliste, Software-Patch, Austausch, Stilllegung und Nachweisführung. |
| `workflow-sachverstaendigenbriefing` | Briefing für technische Sachverständige: Prüfgegenstand, Hypothesen, Logdaten, Testaufbau, Reproduzierbarkeit und Grenzen der rechtlichen Bewertung. |
| `workflow-security-by-design-sprint` | Führt Produktteam durch Security-by-Design: Bedrohungsmodell, Updatekanal, SBOM, Schwachstellenprozess, Logging und Notfallplan. |
| `workflow-unfall-incident-response` | Leitet nach Unfall, Beinaheunfall, Datenpanne oder Cybervorfall: Sicherung, Meldungen, Beweise, Kommunikation, Rückruf, Betreiber- und Herstellerfragen. |
| `workflow-update-und-change-control` | Prüft Softwareupdates, KI-Modellwechsel, Fine-Tuning, Parametrisierung und wesentliche Veränderung mit Dokumentationsspur. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Risikoklassifizierung Schnelltest Rueckruf**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-risikoklassifizierung-schnelltest`

**Fokus:** Führt durch Risikoklassen: Maschine, Sicherheitsbauteil, Hochrisiko-KI, Medizinprodukt, Verbraucherprodukt, kritische Infrastruktur, Beschäftigtendaten.

# Risikoklassifizierung Schnelltest

## Fachkern: Risikoklassifizierung Schnelltest
- **Spezialgegenstand:** Risikoklassifizierung Schnelltest; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftung, ProdSG/GPSR, AI Act, MDR/MPDG, DSGVO, NIS2/BSI, Arbeitsschutz, CE und Betreiberpflichten.
- **Entscheidende Weiche:** Robotikrolle, bestimmungsgemäße Verwendung, Autonomiegrad, Sicherheitsfunktion, Datenfluss, Haftungspfad, Konformität und Update-/Recall-Pflicht trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Workflow- und Einstiegsskill im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

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

Dieser Skill fokussiert: **Führt durch Risikoklassen: Maschine, Sicherheitsbauteil, Hochrisiko-KI, Medizinprodukt, Verbraucherprodukt, kritische Infrastruktur, Beschäftigtendaten.**

Quellen-/Normenanker: Quellenmatrix im Plugin, Uploads, Rollenprofil, Fristen, Produktakte.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 2. `workflow-rueckruf-und-field-action`

**Fokus:** Plant freiwillige oder behördliche Korrekturmaßnahme: Risiko, Reichweite, Kundenliste, Software-Patch, Austausch, Stilllegung und Nachweisführung.

# Rückruf und Field Action

## Fachkern: Rückruf und Field Action
- **Spezialgegenstand:** Rückruf und Field Action; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftung, ProdSG/GPSR, AI Act, MDR/MPDG, DSGVO, NIS2/BSI, Arbeitsschutz, CE und Betreiberpflichten.
- **Entscheidende Weiche:** Robotikrolle, bestimmungsgemäße Verwendung, Autonomiegrad, Sicherheitsfunktion, Datenfluss, Haftungspfad, Konformität und Update-/Recall-Pflicht trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Workflow- und Einstiegsskill im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

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

Dieser Skill fokussiert: **Plant freiwillige oder behördliche Korrekturmaßnahme: Risiko, Reichweite, Kundenliste, Software-Patch, Austausch, Stilllegung und Nachweisführung.**

Quellen-/Normenanker: Quellenmatrix im Plugin, Uploads, Rollenprofil, Fristen, Produktakte.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 3. `workflow-sachverstaendigenbriefing`

**Fokus:** Briefing für technische Sachverständige: Prüfgegenstand, Hypothesen, Logdaten, Testaufbau, Reproduzierbarkeit und Grenzen der rechtlichen Bewertung.

# Sachverständigenbriefing

## Fachkern: Sachverständigenbriefing
- **Spezialgegenstand:** Sachverständigenbriefing; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftung, ProdSG/GPSR, AI Act, MDR/MPDG, DSGVO, NIS2/BSI, Arbeitsschutz, CE und Betreiberpflichten.
- **Entscheidende Weiche:** Robotikrolle, bestimmungsgemäße Verwendung, Autonomiegrad, Sicherheitsfunktion, Datenfluss, Haftungspfad, Konformität und Update-/Recall-Pflicht trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Workflow- und Einstiegsskill im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

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

Dieser Skill fokussiert: **Briefing für technische Sachverständige: Prüfgegenstand, Hypothesen, Logdaten, Testaufbau, Reproduzierbarkeit und Grenzen der rechtlichen Bewertung.**

Quellen-/Normenanker: Quellenmatrix im Plugin, Uploads, Rollenprofil, Fristen, Produktakte.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 4. `workflow-security-by-design-sprint`

**Fokus:** Führt Produktteam durch Security-by-Design: Bedrohungsmodell, Updatekanal, SBOM, Schwachstellenprozess, Logging und Notfallplan.

# Security-by-Design-Sprint

## Fachkern: Security-by-Design-Sprint
- **Spezialgegenstand:** Security-by-Design-Sprint; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftung, ProdSG/GPSR, AI Act, MDR/MPDG, DSGVO, NIS2/BSI, Arbeitsschutz, CE und Betreiberpflichten.
- **Entscheidende Weiche:** Robotikrolle, bestimmungsgemäße Verwendung, Autonomiegrad, Sicherheitsfunktion, Datenfluss, Haftungspfad, Konformität und Update-/Recall-Pflicht trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Workflow- und Einstiegsskill im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

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

Dieser Skill fokussiert: **Führt Produktteam durch Security-by-Design: Bedrohungsmodell, Updatekanal, SBOM, Schwachstellenprozess, Logging und Notfallplan.**

Quellen-/Normenanker: Quellenmatrix im Plugin, Uploads, Rollenprofil, Fristen, Produktakte.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 5. `workflow-unfall-incident-response`

**Fokus:** Leitet nach Unfall, Beinaheunfall, Datenpanne oder Cybervorfall: Sicherung, Meldungen, Beweise, Kommunikation, Rückruf, Betreiber- und Herstellerfragen.

# Incident Response Robotik

## Fachkern: Incident Response Robotik
- **Spezialgegenstand:** Incident Response Robotik; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftung, ProdSG/GPSR, AI Act, MDR/MPDG, DSGVO, NIS2/BSI, Arbeitsschutz, CE und Betreiberpflichten.
- **Entscheidende Weiche:** Robotikrolle, bestimmungsgemäße Verwendung, Autonomiegrad, Sicherheitsfunktion, Datenfluss, Haftungspfad, Konformität und Update-/Recall-Pflicht trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Workflow- und Einstiegsskill im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

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

Dieser Skill fokussiert: **Leitet nach Unfall, Beinaheunfall, Datenpanne oder Cybervorfall: Sicherung, Meldungen, Beweise, Kommunikation, Rückruf, Betreiber- und Herstellerfragen.**

Quellen-/Normenanker: Quellenmatrix im Plugin, Uploads, Rollenprofil, Fristen, Produktakte.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 6. `workflow-update-und-change-control`

**Fokus:** Prüft Softwareupdates, KI-Modellwechsel, Fine-Tuning, Parametrisierung und wesentliche Veränderung mit Dokumentationsspur.

# Update und Change Control

## Fachkern: Update und Change Control
- **Spezialgegenstand:** Update und Change Control; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftung, ProdSG/GPSR, AI Act, MDR/MPDG, DSGVO, NIS2/BSI, Arbeitsschutz, CE und Betreiberpflichten.
- **Entscheidende Weiche:** Robotikrolle, bestimmungsgemäße Verwendung, Autonomiegrad, Sicherheitsfunktion, Datenfluss, Haftungspfad, Konformität und Update-/Recall-Pflicht trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Workflow- und Einstiegsskill im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

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

Dieser Skill fokussiert: **Prüft Softwareupdates, KI-Modellwechsel, Fine-Tuning, Parametrisierung und wesentliche Veränderung mit Dokumentationsspur.**

Quellen-/Normenanker: Quellenmatrix im Plugin, Uploads, Rollenprofil, Fristen, Produktakte.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.
