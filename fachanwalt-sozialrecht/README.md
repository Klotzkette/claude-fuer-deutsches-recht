# Fachanwalt Sozialrecht

Vollumfaengliches Plugin fuer Fachanwaltschaft Sozialrecht inkl. Kanzleioperative. Fachanwalt fuer Sozialrecht nach FAO § 11. Widerspruch, Klage, Eilantrag, SGB-II-Bescheid, Erwerbsminderungsrente, GdB-Schwerbehinderung, Pflegegrad, Hilfsmittel, Eingliederungshilfe. Kanzleioperative: Bescheidanalyse, Akteneinsicht, PKH, Fristenbuch, Mandanten-Intake, Mandantenbrief Leichte Sprache.

## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **sozialrecht rollstuhl tannenberg** | [testakte-sozialrecht-rollstuhl-tannenberg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Fachanwalt Sozialrecht (`fachanwalt-sozialrecht`, dieses Plugin) | [fachanwalt-sozialrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-sozialrecht.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Familie Tannenberg - vier Sozialrechtsverfahren parallel** ([`testakten/sozialrecht-rollstuhl-tannenberg/`](../testakten/sozialrecht-rollstuhl-tannenberg/)).

Direkt-Download als ZIP: [testakte-sozialrecht-rollstuhl-tannenberg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig.

## Enthaltene Skills

### Fachanwaltschaft-Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-sozialrecht-orientierung` | FAO § 11, SGB I bis XII, Sozialgerichtsbarkeit, Quellenprüfung. |
| `fachanwalt-sozialrecht-widerspruch-sozialleistung` | Widerspruch gegen Sozialleistungsbescheid, § 84 SGG, Frist ein Monat. |
| `fachanwalt-sozialrecht-sgb-ii-bescheid` | Bürgergeld-Bescheid SGB II — Bedarfsberechnung, Regelbedarf, Sanktionen. |
| `fachanwalt-sozialrecht-erwerbsminderungsrente` | Volle / teilweise Erwerbsminderungsrente nach §§ 43, 240 SGB VI. |
| `fachanwalt-sozialrecht-gdb-schwerbehinderung` | GdB-Feststellung § 152 SGB IX, Merkzeichen, Widerspruchsbausteine. |
| `fachanwalt-sozialrecht-krankengeld-aussteuerung` | Krankengeldbezug, Aussteuerung, Anschlussleistungen. |
| `fachanwalt-sozialrecht-eu-rente-antrag` | EU-Rentenantrag, grenzüberschreitende Sozialversicherung. |
| `fachanwalt-sozialrecht-long-covid-bk-anerkennung-bg` | Long-COVID, Berufskrankheit, Berufsgenossenschaft. |
| `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` | Vergleichsstrategie Sozialgericht und Widerspruchsverhandlung. |

### Kanzleioperative-Skills

| Skill | Zweck |
| --- | --- |
| `bescheidanalyse` | Strukturierte Analyse von Sozialleistungsbescheiden. |
| `bescheid-frist-quick-check` | Schnellprüfung Widerspruchsfrist und Bekanntgabe. |
| `widerspruchsfrist-und-zustellung-sgb` | Fristberechnung Zustellung und SGB-Bekanntgaberegeln. |
| `fristenbuch-sozialrecht` | Fristenverwaltung für Sozialrechtsmandate. |
| `akteneinsicht-anfordern` | Akteneinsicht nach § 25 SGB X beantragen. |
| `akteneinsicht-auswerten` | Auswertung der Verwaltungsakte nach Akteneinsicht. |
| `eilantrag-sozialrecht` | Eilantrag § 86b SGG beim Sozialgericht. |
| `klage-sozialgericht` | Klage beim Sozialgericht nach Widerspruchsbescheid. |
| `pkh-erfolgsaussicht-pruefen` | Prozesskostenhilfe-Erfolgsaussicht prüfen. |
| `prozesskostenhilfe-antrag` | PKH-Antrag formulieren und einreichen. |
| `hilfsmittelantrag-pruefen` | Hilfsmittelantrag (Rollstuhl, Hörhilfe, Vorlesekraft) prüfen. |
| `pflegegrad-widerspruch` | Widerspruch gegen Pflegegrad-Einstufung. |
| `eingliederungshilfe-schule` | Eingliederungshilfe Schulbegleitung SGB IX. |
| `anlagen-erstellen` | Anlagenkonvolut für Schriftsätze erstellen. |
| `mandanten-intake` | Strukturierter Mandanten-Intake für Sozialrechtsfälle. |
| `mandat-triage-sozialrecht` | Triage und Priorisierung von Sozialrechtsmandaten. |
| `sozialrecht-fallaufnahme-routing` | Fallaufnahme-Routing an den richtigen Skill. |
| `sozialrecht-kanzlei-kaltstart-interview` | Kaltstart-Interview für neue Sozialrechtsfälle. |
| `mandantenbrief-leichte-sprache` | Mandantenbriefe in leichter Sprache. |
| `schulung-fallbesprechung` | Interne Fallbesprechung und Schulung. |
| `erstgespraech-mandatsannahme` | Erstgespräch und Mandatsannahme. |
| `schriftsatzkern-substantiierung` | Schriftsatz-Substantiierung für Klageverfahren. |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlung Strategie im Sozialrecht. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 33 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akteneinsicht-anfordern` | Mandant oder Anwalt benoetigt Einsicht in die Verwaltungsakte oder Gerichtsakte in einem laufenden Sozialrechtsverfahren. § 25 SGB X Akteneinsicht Verwaltungsverfahren § 120 SGG gerichtliches Verfahren Art. 15 DSGVO ergaenzend. Prüfraste... |
| `akteneinsicht-auswerten` | Anwalt hat Sozialrechts-Verwaltungs- oder Gerichtsakte erhalten und muss diese systematisch für Widerspruch oder Klage auswerten. § 25 SGB X § 120 SGG. Prüfraster: chronologische Sichtung Identifikation entscheidungserheblicher Aktenstue... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Sozialrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsp... |
| `anlagen-erstellen` | Anwalt muss Anlagenkonvolut zu Widerspruch Klage oder Schriftsatz in korrekter juristischer Konvention erstellen. Anlagenanhaenge Sozialrecht K1/W1/A1-Konvention. Prüfraster: Sigel Bezeichnung Quelle Datum Seitenzahl Bezug im Text. Erzeu... |
| `bescheid-frist-quick-check` | 60-Sekunden-Sofortprüfung der Frist eines sozialrechtlichen Bescheids. Eingabe Datum der Bekanntgabe (Zugang) und Datum des Bescheids und Status der Rechtsbehelfsbelehrung. Berechnung Widerspruchsfrist § 84 SGG ein Monat ab Bekanntgabe.... |
| `bescheidanalyse` | Mandant hat Sozialleistungsbescheid erhalten und Anwalt muss dessen Inhalt rechtlich aufschluesseln. §§ 33 35 SGB X Form und Begründungspflicht § 24 SGB X Anhoerung. Prüfraster: Behoerde Aktenzeichen Bescheiddatum Zugangsdatum Bescheidar... |
| `eilantrag-sozialrecht` | Mandant ist auf Sozialleistung angewiesen die sofort wegfaellt oder verweigert wird (Buergergeld Wohnungslosigkeit Krankenversicherung). § 86b SGG Eilrechtsschutz. Prüfraster: Abs. 1 SGG aufschiebende Wirkung bei Aufhebungs-/Rückforderun... |
| `eingliederungshilfe-schule` | Kind mit Behinderung benoetigt Schulbegleitung und Eltern oder Anwalt muessen Anspruch klaeren und durchsetzen. SGB IX Teil 2 §§ 90 ff. Eingliederungshilfe § 35a SGB VIII bei seelischer Behinderung. Prüfraster: Behinderungsbegriff § 99 S... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Sozialrecht (SGB I-XIV): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fachanwalt-sozialrecht-erwerbsminderungsrente` | Versicherter erhielt Ablehnung der Erwerbsminderungsrente oder ist ausgesteuert und fragt nach Rentenanspruch. §§ 43 240 SGB VI. Prüfraster: volle Erwerbsminderung unter 3 Stunden taeglich teilweise unter 6 Stunden Wartezeit 5 Jahre § 50... |
| `fachanwalt-sozialrecht-eu-rente-antrag` | Versicherter mit Beschaeftigungszeiten im EU-Ausland fragt nach Rente und wie die ausländischen Zeiten angerechnet werden. VO (EG) 883/2004 Sozialversicherungskoordinierung. Prüfraster: Antragstellung im Wohnsitzland Weiterleitung Pro-ra... |
| `fachanwalt-sozialrecht-gdb-schwerbehinderung` | Mandant hat Behinderung und moechte Schwerbehindertenausweis und Merkzeichen beantragen oder Ablehnungsbescheid anfechten. § 152 SGB IX Feststellungsverfahren Versorgungsmedizin-Verordnung. Prüfraster: GdB-Feststellung nach Versorgungsme... |
| `fachanwalt-sozialrecht-krankengeld-aussteuerung` | Mandant war langzeitkrank und Krankengeld laeuft nach 78 Wochen aus oder ist ausgelaufen und fragt nach Anschlusssicherung. § 44 SGB V Krankengeld Bezugsdauer 78 Wochen innerhalb 3 Jahren. Prüfraster: Anschluss ALG I § 145 SGB III Erwerb... |
| `fachanwalt-sozialrecht-long-covid-bk-anerkennung-bg` | Workflow-Skill zu fachanwalt sozialrecht long covid bk anerkennung bg. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-sozialrecht-orientierung` | Einstieg in den Skill-Verbund Sozialrecht. Orientierung im Sozialrecht Fachanwaltschaft nach § 14 FAO Weiterbildungspflicht. SGB I bis XIV im Überblick SGB II Buergergeld SGB VI Rente SGB V Krankenversicherung SGB IX Reha SGB XI Pflege.... |
| `fachanwalt-sozialrecht-sgb-ii-bescheid` | Workflow-Skill zu fachanwalt sozialrecht sgb ii bescheid. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` | Vergleich vor Sozialgericht § 101 SGG. Widerspruchsverhandlung Behoerde § 84 SGG. Mediation in Sozialleistungs-Streit zunehmend. Anhoerung GdB-Verfahren Vergleich Schwerbehinderung. Workflow Korrespondenz Behoerde Klagebegründung Verglei... |
| `fachanwalt-sozialrecht-widerspruch-sozialleistung` | Mandant hat Sozialleistungsbescheid erhalten und Anwalt formuliert Widerspruch. § 84 SGG Widerspruchsfrist ein Monat. Prüfraster: Frist (Bekanntgabe Vier-Tage-Fiktion § 37 Abs. 2 SGB X seit 1.1.2025 PostModG) aufschiebende Wirkung § 86a... |
| `fristenbuch-sozialrecht` | Anwalt oder Sekretariat muss Fristen in Sozialrechtsverfahren erfassen und ueberwachen. Fristenbuch Sozialrecht. Standardfristen: § 84 SGG Widerspruch 1 Monat § 87 SGG Klage 1 Monat § 173 SGG Beschwerde 1 Monat Untätigkeit § 88 SGG 6 Mon... |
| `hilfsmittelantrag-pruefen` | Mandant benoetigt Hilfsmittel (Rollstuhl Hoerhilfe Prothese Pflegebett Treppenlift) und fragt welcher Kostentraeger zuständig ist und wie Antrag und Widerspruch aussehen. § 33 SGB V Hilfsmittelverzeichnis § 139 SGB V § 40 SGB XI § 47 SGB... |
| `klage-sozialgericht` | Nach negativem Widerspruchsbescheid muss Klage zum Sozialgericht erhoben werden. §§ 87 ff. SGG Klagefrist. Prüfraster: Klagefrist 1 Monat nach Widerspruchsbescheid § 87 Abs. 1 SGG kein Anwaltszwang vor SG beA-Versandpflicht sachliche Zus... |
| `mandanten-intake` | Erstgespräch oder Telefon-Intake in einer Sozialrechtskanzlei — Stammdaten Mandant erfassen Fristen identifizieren und Akte anlegen. Sozialrechtliches Mandats-Intake. Prüfraster: Geburtsdatum Versichertennummer zuständige Behoerden Verfa... |
| `mandantenbrief-leichte-sprache` | Erklärung eines sozialrechtlichen Bescheids für den Mandanten in einfacher oder leichter Sprache. Drei Stufen Standardbrief (B1) Einfache Sprache (A2 nach GER) Leichte Sprache (Regeln Netzwerk Leichte Sprache und DIN SPEC 33429). Erfasst... |
| `mandat-triage-sozialrecht` | Neues sozialrechtliches Mandat: Sekretariat oder Anwalt muss Sachgebiet klaeren und zum richtigen Skill weiterleiten. Eingangs-Triage Sozialrecht SGB I-XIV. Prüfraster: Sachgebiet (SGB II Buergergeld SGB V Krankenversicherung SGB VI Rent... |
| `pflegegrad-widerspruch` | Mandant erhielt zu niedrigen Pflegegrad oder Pflegekasse verweigert Pflegegrad. Widerspruch gegen Pflegegrad-Bescheid nach SGB XI. Prüfraster: sechs Module § 15 SGB XI Mobilitaet Kognition Verhalten Selbstversorgung Krankheitsbewaeltigun... |
| `pkh-erfolgsaussicht-pruefen` | Workflow-Skill zu pkh erfolgsaussicht pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `prozesskostenhilfe-antrag` | Anwalt erstellt PKH-Antrag für Sozialgerichtsverfahren und muss alle Belege korrekt zusammenstellen. § 73a SGG iVm §§ 114 ff. ZPO. Prüfraster: Erklärung persoenliche und wirtschaftliche Verhältnisse Formular ZP1a Nachweise Einkommen Verm... |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Widerspruch + SG-Klage, Eilantrag § 86b SGG, Überprüfungsantrag § 44 SGB X: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `schulung-fallbesprechung` | Strukturierte Fallbesprechung für Schulung Inhouse-Fortbildung Referendariats-AG oder Prüfungs-Vorbereitung Fachanwalt Sozialrecht. Nimmt eine bestehende Akte (Bescheid plus medizinische Unterlagen plus Mandantenangaben) und führt die Te... |
| `sozialrecht-fallaufnahme-routing` | Master-Routing-Skill der sozialrechtlichen Kanzlei. Nimmt einen frischen Fall an und entscheidet in drei Schritten welche weiteren Skills wann gezogen werden. Schritt 1 Fristlage (bescheid-frist-quick-check) Schritt 2 Bescheidart und Rec... |
| `sozialrecht-kanzlei-kaltstart-interview` | Kaltstart-Interview für die sozialrechtliche Kanzlei. Erfragt Schwerpunktbereiche (Buergergeld SGB II / SGB IX Schwerbehinderung / SGB V Krankenversicherung / SGB XI Pflege / Asylbewerberleistungsgesetz) zuständige Sozialgerichte typisch... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Sozialrecht (SGB I-XIV): ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |
| `widerspruchsfrist-und-zustellung-sgb` | Anwalt muss bei eingehendem oder ausgehendem Bescheid klaeren ob und wann die Widerspruchsfrist laeuft und ob Zustellungsmaengel die Frist beeinflussen. § 37 SGB X Zustellung und Bekanntgabe-Fiktion. Prüfraster: Vier-Tage-Fiktion seit 1.... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
