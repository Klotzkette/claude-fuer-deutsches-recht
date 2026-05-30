# KI-Incident-Response-Playbook — Thalheim Industries SE

**Aktenzeichen:** TI-KI-2026-013
**Dokumentversion:** 1.0
**Freigegeben durch:** CCO Annegret Kühnhausen; CIO Dr. Sigrid Wolfsbacher
**Freigabedatum:** 01. März 2026
**Geltungsbereich:** Alle KI-Systeme im KI-Inventar der Thalheim Industries SE

---

## 1. Zweck und Anwendungsbereich

Dieses Playbook definiert den konzernweiten Prozess zur Erkennung, Klassifikation, Reaktion und Meldung von KI-bezogenen Sicherheits- und Compliance-Vorfällen (KI-Incidents). Es ergänzt das bestehende allgemeine IT-Incident-Response-Framework (IT-IRM-2024) und das Datenschutzverletzungs-Protokoll nach Art. 33/34 DSGVO.

**Rechtsgrundlagen:**
- Art. 73 KI-VO: Meldung schwerwiegender Vorfälle an Marktüberwachungsbehörde (https://dejure.org/gesetze/KIVO/73.html)
- Art. 33 DSGVO: Meldung von Datenschutzverletzungen an Aufsichtsbehörde (https://dejure.org/gesetze/DSGVO/33.html)
- Art. 26 Abs. 4 KI-VO: Betreiberpflicht zur Incident-Meldung

---

## 2. Incident-Klassifikation

### Klasse 1 — Kritisch (Sofortmaßnahmen erforderlich)

**Definition:** Schwerwiegender Vorfall nach Art. 3 Nr. 49 KI-VO, der eine ernsthafte Bedrohung für Gesundheit, Sicherheit oder Grundrechte darstellt oder zu einem Todesfall geführt hat oder hätte führen können.

**Beispiele bei Thalheim:**
- RecruitAI lehnt systematisch alle Bewerber einer bestimmten Nationalität ab (Diskriminierungsverdacht)
- CreditVision Score weist nachweisbaren Bias gegen bestimmte Bevölkerungsgruppen auf
- Datenpanne bei Synaptec: Bewerberdaten öffentlich zugänglich

**Reaktionspflicht:** Sofortiger Stopp des Systems + Meldung an BNetzA (Art. 73 KI-VO) binnen 15 Tagen (Todesfall: sofort).

---

### Klasse 2 — Schwerwiegend (Reaktion binnen 24 Stunden)

**Definition:** Fehlfunktion mit erheblichem Schaden für einzelne Personen; Compliance-Verstoß der KI-VO mit behördlichem Korrekturpotenzial.

**Beispiele:**
- RecruitAI generiert Score-Ausgaben jenseits des 0–100-Rahmens (Systemfehler)
- CodeAssist gibt Code mit kritischen Sicherheitslücken aus, der ungeprüft in Produktion überführt wird
- Schatten-KI in einem Fachbereich mit Personenbezug entdeckt (vgl. Strang 7)

**Reaktionspflicht:** CCO + CIO informieren, System isolieren, Sachverhaltsklärung, ggf. LfDI BW.

---

### Klasse 3 — Moderat (Reaktion binnen 72 Stunden)

**Definition:** Funktionsstörungen ohne unmittelbaren Personenschaden; Verstöße gegen interne Richtlinien.

**Beispiele:**
- Unberechtigter Zugriff auf Recruiting-Daten intern (Mitarbeiter ohne Berechtigung)
- ServiceBot gibt falsche Produktinformationen an Kunden aus
- PredictMaint empfiehlt Wartungsintervalle mit erheblicher Abweichung (wirtschaftlicher Schaden)

**Reaktionspflicht:** CDO + IT-Security; Dokumentation; ggf. Kundenbenachrichtigung.

---

### Klasse 4 — Gering (Reaktion binnen 1 Woche)

**Definition:** Qualitätsprobleme, Leistungsabfälle, Nutzerbeschwerden ohne Rechtsverletzung.

**Beispiele:**
- CodeAssist-Antwortqualität sinkt nach Modell-Update
- Bewerbungsportal-Chatbot versteht Fachjargon nicht

**Reaktionspflicht:** CDO, Ticketsystem, regulärer Betrieb.

---

## 3. Incident-Response-Prozess

### Schritt 1: Erkennung und Meldung

**Erkennungsquellen:**
- Automatische Monitoring-Alarme (KI-Dashboard, CDO-Bereich)
- Meldungen von Mitarbeitenden (Hinweisgebersystem, intern: ki-incident@thalheim.de)
- Kundenbeschwerden (Vertrieb, Kundenservice)
- Behördliche Anfragen (BaFin, LfDI BW)
- Revisionsfeststellungen (interne Revision, Hagedorn & Partner)

**Erstmeldung:** Jede Mitarbeiterin und jeder Mitarbeiter, der einen KI-Incident erkennt oder vermutet, ist verpflichtet, diesen unverzüglich über das interne Meldeformular (ki-incident@thalheim.de) oder mündlich an den IT-Service-Desk (intern: 4-4000) zu melden.

### Schritt 2: Erstklassifikation (ICO on Duty)

Der CDO oder sein Stellvertreter klassifiziert den Vorfall innerhalb von 2 Stunden nach Erstmeldung (Klasse 1–4). Bei Klasse 1 und 2: sofortige Eskalation an CCO, CIO, ggf. CEO.

### Schritt 3: Sofortmaßnahmen

| Klasse | Sofortmaßnahme | Verantwortlich |
|---|---|---|
| 1 | System stoppen; Notfallteam einberufen; Behörden informieren | CCO + CIO + CEO |
| 2 | System isolieren; Sachverhaltsklärung; Behörden nach 24h | CCO + CIO |
| 3 | Diagnose; ggf. System einschränken; Bericht in 72h | CDO + IT-Security |
| 4 | Ticket; Analyse; reguläres Verfahren | CDO |

### Schritt 4: Behördliche Meldepflichten

| Behörde | Pflicht | Frist | Voraussetzung |
|---|---|---|---|
| Bundesnetzagentur (BNetzA) | Art. 73 KI-VO — schwerwiegender Vorfall | 15 Tage ab Kenntnis | Klasse-1-Vorfall Hochrisiko-System |
| LfDI BW | Art. 33 DSGVO — Datenschutzverletzung | 72 Stunden | Datenpanne mit Risiko für Betroffene |
| BaFin | MaRisk / aufsichtsrechtlich | Nach MaRisk | CreditVision Score — Systemversagen |

**Zuständig für alle Behördenmeldungen:** CCO Annegret Kühnhausen in Abstimmung mit Kanzlei Borchmann Compliance.

### Schritt 5: Ursachenanalyse und Abschlussbericht

Innerhalb von 30 Tagen nach Incident-Schließung erstellt das CDO-Büro einen Abschlussbericht mit Root-Cause-Analyse und Maßnahmen zur Vermeidung von Wiederholungen. Der Bericht fließt in die jährliche KI-Governance-Review ein.

---

## 4. Spezialfall: Schatten-KI (nicht genehmigte Systeme)

Der Vorfall in der Marketingabteilung (identifiziert März 2026 durch Konzernrevision) zeigt, dass Schatten-KI als eigenständige Incident-Klasse zu behandeln ist:

**Vorgehen bei Schatten-KI-Entdeckung:**
1. Sofortige Abschaltung des nicht genehmigten Systems durch IT auf Anweisung CDO.
2. Sicherung der Nutzungsprotokolle (soweit zugänglich).
3. Datenschutzprüfung: Wurden personenbezogene Daten verarbeitet? → DSGVO Art. 33?
4. Disziplinarische Anhörung der verantwortlichen Person (Personalrecht, CCO + HR).
5. Analyse: Wie konnte das System eingesetzt werden? Technische Zugangskontrollen verschärfen.
6. Protokollierung im Incident-Register.

---

## 5. Incident-Register

Alle KI-Incidents werden im zentralen KI-Incident-Register (SharePoint, Zugriff: CCO, CDO, CIO, DSB) dokumentiert mit folgenden Feldern:
- Incident-ID; Datum; Klasse; betroffenes System; Beschreibung; Entdeckungsquelle; Sofortmaßnahmen; Behördliche Meldungen; Root Cause; Abschlussdatum; Maßnahmen.

**Aktueller Eintrag:**
- INC-2026-003: Schatten-KI Marketing (Midjourney-API); entdeckt 14.03.2026; Klasse 2; IT-Abschaltung 14.03.2026; Sachverhaltsklärung läuft.

---

*Aktenzeichen: TI-KI-2026-013. Freigegeben: A. Kühnhausen, Dr. S. Wolfsbacher. Stand: März 2026.*
