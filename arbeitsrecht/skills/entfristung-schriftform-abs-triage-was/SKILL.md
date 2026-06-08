---
name: entfristung-schriftform-abs-triage-was
description: "Entfristung Schriftform ABS Triage WAS im Plugin Arbeitsrecht: prüft konkret KERNSKILL, Einstieg Entfristungsklage-Workflow, Typische Vergleichsbausteine in der Entfristungsklage, Fristprüfung Kündigungsschutzklage. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Entfristung Schriftform ABS Triage WAS

## Arbeitsbereich

**Entfristung Schriftform ABS Triage WAS** ordnet den Fall über die tragenden Prüfungslinien: KERNSKILL, Einstieg Entfristungsklage-Workflow, Typische Vergleichsbausteine in der Entfristungsklage. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `entfristung-schriftform-14-abs-4-erkennen` | KERNSKILL: Schriftform nach § 14 Abs. 4 TzBfG für Befristungsabreden; Papierunterschrift nach § 126 BGB oder echte qualifizierte elektronische Signatur nach § 126a BGB prüfen; Scan/einfache Signatur genügt nicht; Rechtsfolge § 16 Satz 1 TzBfG Vertrag gilt als unbefristet. |
| `entfristung-triage-was-will-user` | Einstieg Entfristungsklage-Workflow: Erkennung ob Nutzer Befristungskontrollklage oder Entfristungsklage anstrebt; Abgrenzung zu Kündigungsschutzklage; Überblick Prüfprogramm TzBfG; Weiterleitung zu passenden Folge-Skills. |
| `entfristung-vergleichsverhandlung-checkliste` | Typische Vergleichsbausteine in der Entfristungsklage: Entfristungsbestätigung oder Beendigungsdatum mit Abfindung; Weiterbeschaeftigung oder Aufhebung; Zeugnis; Freistellung; Urlaubsabgeltung; Klageerledigung; Erledigungsklausel-Risiken. |
| `kueschk-frist-und-zugang-pruefen` | Fristprüfung Kündigungsschutzklage: § 4 KSchG drei Wochen ab Zugang; § 5 KSchG nachtraegliche Klagezulassung bei unverschuldeter Versaeumung; Zugangsbeweis-Fragen; Fristberechnung nach §§ 187 und 188 BGB. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `entfristung-schriftform-14-abs-4-erkennen`

**Fokus:** KERNSKILL: Schriftform nach § 14 Abs. 4 TzBfG für Befristungsabreden; Papierunterschrift nach § 126 BGB oder echte qualifizierte elektronische Signatur nach § 126a BGB prüfen; Scan/einfache Signatur genügt nicht; Rechtsfolge § 16 Satz 1 TzBfG Vertrag gilt als unbefristet.

### KERNSKILL: Schriftform § 14 Abs. 4 TzBfG — Die häufig übersehene Falle

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KERNSKILL: Schriftform § 14 Abs. 4 TzBfG — Die häufig übersehene Falle` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn

1. Wie wurde der Arbeitsvertrag unterzeichnet? (Papieroriginal / QES / einfache Signatur / Scan / E-Mail / einseitig)
2. Hat der Arbeitnehmer eine Originalurkunde mit eigenhändiger Unterschrift beider Parteien erhalten oder liegt ein prüfbares QES-Zertifikat vor?
3. Lag die wirksame Unterzeichnung beider Parteien vor dem ersten Arbeitstag vor?
4. Falls Verlängerungsvereinbarung: Wurde diese ebenfalls formwirksam geschlossen?
5. Gibt es Belege für die Art der Unterzeichnung (Original, E-Mail, Zertifikat, Audit-Trail, Signier-Portal)?

## Zentrale Normen

- § 14 Abs. 4 TzBfG — Schriftformerfordernis der Befristungsabrede (konstitutive Wirksamkeitsvoraussetzung)
- § 126 BGB — gesetzliche Schriftform: eigenhändige Namensunterschrift
- § 126 Abs. 3 BGB — elektronische Form kann Schriftform ersetzen, wenn gesetzlich nicht ausgeschlossen
- § 126a BGB — elektronische Form durch qualifizierte elektronische Signatur
- § 16 Satz 1 TzBfG — Rechtsfolge Formverstos: Vertrag gilt als unbefristet
- § 17 TzBfG — 3-Wochen-Klagefrist ab vereinbartem Vertragsende

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum: Schriftformmangel erkennen

```
Frage 1: Original-Urkunde mit eigenhändiger Unterschrift beider Parteien oder echte QES beider Parteien?
 ├── Nein → SCHRIFTFORMMANGEL → § 16 Satz 1 TzBfG: Vertrag gilt als unbefristet
 └── Ja → weiter zu Frage 2

Frage 2: Unterzeichnung vor Arbeitsaufnahme?
 ├── Nein (Unterschrift erst nach erstem Arbeitstag) → SCHRIFTFORMMANGEL
 └── Ja → weiter zu Frage 3

Frage 3: Einheitlichkeit/Formverbund? (dieselbe Urkunde oder jeweils für die andere Seite bestimmte gleichlautende Ausfertigung; bei QES nachvollziehbarer elektronischer Dokumentbezug?)
 ├── Nein (jede Seite hat eigene Kopie unterschrieben, kein Verbindungswille) → fraglich
 └── Ja → Schriftform gewahrt

Frage 4 (bei Verlängerung): Verlaengerungsvereinbarung ebenfalls formwirksam (Papier/QES)?
 ├── Nein (mündlich / per E-Mail) → SCHRIFTFORMMANGEL bei der Verlängerung
 └── Ja → Verlängerung wirksam
```

## Zweck

Dies ist der wichtigste Skill im Entfristungs-Bündel. § 14 Abs. 4 TzBfG legt fest, dass die **Befristungsabrede** — also die Klausel im Arbeitsvertrag, die eine zeitliche Begrenzung festlegt — der Schriftform bedarf. Fehlt diese Schriftform, gilt der Vertrag als unbefristet.

## Die Norm — § 14 Abs. 4 TzBfG

> Die Befristung eines Arbeitsvertrags bedarf zu ihrer Wirksamkeit der Schriftform.

## Was bedeutet Schriftform?

**§ 126 Abs. 1 BGB:** Die gesetzliche Schriftform erfordert eine **eigenhändige Unterschrift** (Namensunterschrift oder handschriftliches Kreuz) auf einer Urkunde.

**Nicht ausreichend für die Schriftform:**
- E-Mail (auch wenn PDF angehängt)
- Fax (str., aber h.M.: nicht ausreichend für § 14 Abs. 4 TzBfG)
- einfache elektronische Signatur, eingescannte Unterschrift, Signaturbild
- fortgeschrittene elektronische Signatur ohne QES-Qualität
- Mündliche Vereinbarung
- Bestätigung per Klick in einem Online-Portal

**Erforderlich:**
- Originalurkunde mit eigenhändiger Unterschrift beider Parteien oder elektronische Form nach § 126a BGB durch echte QES

## Elektronische Form richtig einordnen

§ 126 Abs. 3 BGB erlaubt es grundsätzlich, die gesetzliche Schriftform durch elektronische Form (§ 126a BGB — qualifizierte elektronische Signatur) zu ersetzen, wenn das Gesetz die elektronische Form nicht ausschließt. § 14 Abs. 4 TzBfG enthält in der aktuell geprüften Fassung keinen ausdrücklichen Ausschluss wie etwa § 623 BGB.

**Bedeutung in der Praxis:** Eine echte QES kann genügen; die meisten Alltagsfälle sind aber gerade keine QES, sondern Scan, Klicksignatur oder fortgeschrittene Signatur. Deshalb immer Zertifikat, Identifizierung, Audit-Trail, Dokumentbezug und Zugang prüfen.

**Abgrenzung:** Für Kündigung und Aufhebungsvertrag gilt § 623 BGB; dort ist elektronische Form ausdrücklich ausgeschlossen. Diese Wertung darf nicht unbesehen auf § 14 Abs. 4 TzBfG übertragen werden.

## Wann liegt ein Schriftformmangel vor?

**Häufige Szenarien:**
- Arbeitsvertrag wurde per E-Mail zugesandt und per E-Mail "unterschrieben" (eingescannte Unterschrift im PDF)
- Vertragsunterzeichnung über ein Online-Portal (z.B. Workday, DocuSign) ohne qualifizierte elektronische Signatur
- Nur der Arbeitgeber hat unterschrieben, der Arbeitnehmer nicht (oder umgekehrt)
- Die Befristungsklausel wurde per E-Mail vereinbart, der Grundvertrag ist zwar schriftlich, aber die Verlängerungsvereinbarung nicht

**Kritische Frage an den Nutzer:**
- Wie wurde der Arbeitsvertrag geschlossen?
- Hast du eine Originalurkunde mit echter Unterschrift erhalten?
- Wurde der Vertrag digital unterzeichnet, und falls ja: mit einfacher Signatur, fortgeschrittener Signatur oder echter QES?

## Wer muss unterschreiben?

Beide Parteien müssen das **selbe Dokument** unterzeichnen — Arbeitgeber und Arbeitnehmer. Tauschen die Parteien nur Kopien aus oder unterschreibt nur eine Seite, kann die Schriftform fehlen.

## Rechtsfolge bei Schriftformmangel

Fehlt die Schriftform bei der Befristungsabrede: **→ § 16 Satz 1 TzBfG** (Skill `entfristung-rechtsfolge-16-tzbfg-unbefristet`).

Der Arbeitsvertrag selbst bleibt wirksam — nur die Befristung ist unwirksam. Der Arbeitnehmer hat einen unbefristeten Arbeitsvertrag.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 2. `entfristung-triage-was-will-user`

**Fokus:** Einstieg Entfristungsklage-Workflow: Erkennung ob Nutzer Befristungskontrollklage oder Entfristungsklage anstrebt; Abgrenzung zu Kündigungsschutzklage; Überblick Prüfprogramm TzBfG; Weiterleitung zu passenden Folge-Skills.

### Entfristungsklage: Was will der Nutzer?

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Entfristungsklage: Was will der Nutzer?` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zentrale Normen (Überblick)

- § 17 TzBfG — 3-Wochen-Klagefrist (kritischste Frist; läuft auch bei Weiterbeschäftigung)
- § 14 Abs. 4 TzBfG — Schriftformerfordernis (häufig übersehener Unwirksamkeitsgrund)
- § 14 Abs. 2 Satz 2 TzBfG — Vorbeschäftigungsverbot
- § 16 TzBfG — Rechtsfolge: Vertrag gilt als unbefristet
- § 4 KSchG — Klagefrist Kündigungsschutz (zur Abgrenzung)
- § 623 BGB — Schriftformerfordernis Kündigung (zur Abgrenzung)

## Aktuelle Rechtsprechung (Kurzüberblick für Triage)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Dieser Skill ist der Einstieg in den Entfristungs-Workflow. Er klärt, ob das Ziel des Nutzers ist, festzustellen, dass ein angeblich befristeter Vertrag in Wirklichkeit **unbefristet** ist (Befristungskontrollklage / Entfristungsklage).

## Abgrenzung: Entfristungsklage vs. Kündigungsschutzklage

| | Entfristungsklage | Kündigungsschutzklage |
|---|---|---|
| Ausgangssituation | Befristeter Vertrag läuft aus | Kündigung durch Arbeitgeber |
| Ziel | Feststellung: Vertrag ist unbefristet | Feststellung: Kündigung ist unwirksam |
| Rechtsgrundlage | §§ 17, 16 TzBfG | § 4 KSchG |
| Frist | 3 Wochen ab vereinbartem Ende | 3 Wochen ab Zugang der Kündigung |
| Norm Schriftform | § 14 Abs. 4 TzBfG | § 623 BGB |

## Typische Einstiegssituation

Der Nutzer sagt zum Beispiel:
- "Mein befristeter Vertrag läuft am [DATUM] aus, ich glaube er war gar nicht wirksam befristet"
- "Mein Arbeitsvertrag wurde per E-Mail unterschrieben, gilt die Befristung überhaupt?"
- "Ich arbeite schon seit drei Jahren auf Basis aufeinanderfolgender befristeter Verträge"
- "Mein Arbeitgeber hat mir einen neuen Vertrag gegeben ohne dass ich unterschrieben habe"

## Erkennungsmerkmale Entfristungsklage

Das System erkennt den Entfristungs-Bedarf wenn:
- Ein schriftlicher (oder angeblich elektronischer) Vertrag mit Endtermin vorliegt
- Der Arbeitnehmer behauptet, die Befristung sei unwirksam
- Das Ende des Vertrags noch nicht eingetreten ist oder erst kürzlich eingetreten ist

## Kritische Sofortfrage: Dreiwochenfrist § 17 TzBfG

**Sofort prüfen:**

> § 17 TzBfG: Will der Arbeitnehmer geltend machen, dass die Befristung eines Arbeitsvertrags rechtsunwirksam ist, so muss er innerhalb von **drei Wochen nach dem vereinbarten Ende des befristeten Arbeitsvertrags** Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis auf Grund der Befristung nicht beendet ist.

**Wann läuft die Frist?** Ab dem **vereinbarten** (nicht tatsächlichen) Vertragsende. Sie läuft auch wenn der Arbeitnehmer tatsächlich weiterbeschäftigt wird.

## Folge-Skills

| Schritt | Skill |
|---|---|
| Laie oder Anwalt? | `entfristung-laie-oder-anwalt-frage` |
| Dreiwochenfrist § 17 TzBfG | `entfristung-grundwarnung-drei-wochen-frist` |
| Sachgrund prüfen | `entfristung-sachgrund-pruefen-14-abs-1` |
| Schriftform prüfen | `entfristung-schriftform-14-abs-4-erkennen` |
| Elektronische Signatur | `entfristung-elektronische-signatur-vorsicht` |
| Rechtsfolge | `entfristung-rechtsfolge-16-tzbfg-unbefristet` |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 3. `entfristung-vergleichsverhandlung-checkliste`

**Fokus:** Typische Vergleichsbausteine in der Entfristungsklage: Entfristungsbestätigung oder Beendigungsdatum mit Abfindung; Weiterbeschaeftigung oder Aufhebung; Zeugnis; Freistellung; Urlaubsabgeltung; Klageerledigung; Erledigungsklausel-Risiken.

### Vergleichsverhandlung: Checkliste Entfristungsklage

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vergleichsverhandlung: Checkliste Entfristungsklage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor der Vergleichsverhandlung

1. Will der Mandant Weiterbeschäftigung (unbefristetes Arbeitsverhältnis) oder Beendigung mit Abfindung?
2. Welche Abfindungsuntergrenze ist akzeptabel?
3. Stehen offene Urlaubstage, Überstunden oder Gehaltsansprüche aus?
4. Sperrzeit-Risiko: Auf wessen Veranlassung wird das AV beendet? (§ 159 SGB III)
5. Wird ein qualifiziertes Zeugnis benötigt? Welche Note?
6. Erledigungsklausel: Gibt es weitere offene Ansprüche aus dem Arbeitsverhältnis?

## Zentrale Normen

- §§ 9, 10 KSchG i.V.m. § 17 Satz 2 TzBfG — Auflösungsantrag auf Abfindung
- § 7 Abs. 4 BUrlG — Urlaubsabgeltung bei Beendigung
- § 615 BGB — Annahmeverzugslohn bei Weiterbeschäftigungsverweigerung
- § 159 SGB III — Sperrzeit bei Aufhebungsvertrag auf eigene Veranlassung
- § 34 EStG — Fünftel-Regelung für Abfindungen (steuerliche Behandlung prüfen)
- § 109 GewO — Zeugnisanspruch

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Ein Vergleich in der Entfristungsklage kann verschiedene Formen annehmen. Dieser Skill listet alle relevanten Punkte auf.

## Option A: Entfristungsbestätigung (Arbeitgeber gibt nach)

Der Arbeitgeber erkennt an, dass das Arbeitsverhältnis unbefristet ist. Dann:
- Keine Abfindung (es sei denn verhandelt)
- Weiterbeschäftigung zu unveränderten Bedingungen
- Klärung des Beschäftigungszeitraums und der Vergütung für die Zeit nach dem vereinbarten Ende

**Praxishinweis:** Selten im Vergleich, da Arbeitgeber dann die Konsequenzen (unbefristetes Arbeitsverhältnis, Kündigungsschutz) akzeptieren müssen.

## Option B: Beendigung mit Abfindung

Häufigere Vergleichsvariante: Beide Seiten einigen sich auf eine Beendigung des Arbeitsverhältnisses zu einem vereinbarten Datum gegen Abfindung.

### Checkliste Vergleichspunkte

**1. Beendigungsdatum**
- Wann endet das Arbeitsverhältnis?
- Rückwirkend zum vereinbarten Befristungsende, oder zu einem späteren Datum?
- Konsequenz für Sozialversicherung und Arbeitslosengeld beachten.

**2. Abfindung**
- Höhe der Abfindung (Orientierung an KüSchK-Faustformel auch hier möglich)
- Fälligkeit und Zahlungsweg
- Steuer- und sozialversicherungsrechtliche Behandlung (§ 34 EStG Fünftel-Regelung prüfen)

**3. Freistellung**
- Ab wann? Unwiderruflich oder widerruflich?
- Anrechnung offener Urlaub auf Freistellung?

**4. Urlaubsabgeltung**
- Offene Urlaubstage ermitteln und abgelten (§ 7 Abs. 4 BUrlG)

**5. Vergütung für Zeitraum nach vereinbartem Befristungsende**
- Falls Weiterbeschäftigung bis Vergleichsdatum: Vergütung regeln
- Falls keine Weiterbeschäftigung: Annahmeverzugslohn § 615 BGB

**6. Zeugnis**
- Welche Note wird erteilt?
- Formulierung konkret festlegen (Skill `kueschk-zeugnisanspruch-und-vergleich`)
- Ausstellungsdatum

**7. Klageerledigung**
- Klage wird erledigt durch Vergleich
- Wechselseitiger Verzicht auf alle weiteren Ansprüche aus dem Arbeitsverhältnis
- Vorsicht: Erledigungsklausel kann offene Lohnforderungen vernichten

**8. Geheimhaltung**
- Soll der Vergleichsinhalt geheim bleiben?

## Muster-Vergleich Entfristungsklage

Die Parteien schließen zur Erledigung des Rechtsstreits folgenden Vergleich:

1. Die Parteien sind sich einig, dass das Arbeitsverhältnis auf Veranlassung der Beklagten mit Ablauf des [DATUM] endet.

2. Die Beklagte zahlt an den Kläger eine Abfindung in Höhe von [BETRAG] EUR brutto.

3. Der Kläger erhält für den Zeitraum vom [DATUM BEFRISTUNGSENDE] bis [BEENDIGUNGSDATUM] eine Vergütung in Höhe von [BETRAG] EUR brutto, sofern er tatsächlich weiterbeschäftigt wurde [ANPASSEN].

4. Die Beklagte erteilt dem Kläger ein qualifiziertes Zeugnis mit der Note gut.

5. Damit sind alle wechselseitigen Ansprüche aus dem Arbeitsverhältnis und seiner Beendigung vollständig erledigt.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

<!-- AUDIT 27.05.2026 | Bundle 012 | Task 4
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund WRONG_TOPIC + falsche NZA-Fundstelle korrigiert.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
schriftliche Niederlegung; keine rückwirkende Heilung; Schwäche der Arbeitgeberposition nutzbar"
Das AZ betrifft nicht elektronische Signaturen sondern Unterzeichnung nach Arbeitsaufnahme.
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=7+AZR+1048%2F06
-->

## 4. `kueschk-frist-und-zugang-pruefen`

**Fokus:** Fristprüfung Kündigungsschutzklage: § 4 KSchG drei Wochen ab Zugang; § 5 KSchG nachtraegliche Klagezulassung bei unverschuldeter Versaeumung; Zugangsbeweis-Fragen; Fristberechnung nach §§ 187 und 188 BGB.

### Frist und Zugang prüfen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Frist und Zugang prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## KRITISCHE SOFORTPRÜFUNG — kläre als Erstes

1. **Wann** ist die Kündigung zugegangen? (genaues Datum, nicht Datum auf dem Schreiben)
2. Wie viele Tage sind noch bis zum Ablauf der Drei-Wochen-Frist?
3. Gibt es Beweise für das Zugangsdatum?
4. War die Frist bereits abgelaufen → § 5 KSchG nachträgliche Klagezulassung prüfen

## Zentrale Normen

- § 4 Satz 1 KSchG — 3-Wochen-Frist ab Zugang der schriftlichen Kündigung (absolute Ausschlussfrist)
- § 7 KSchG — Fiktion der Wirksamkeit bei Fristversäumnis (auch bei inhaltlich rechtswidriger Kündigung!)
- § 5 KSchG — Nachträgliche Klagezulassung bei unverschuldeter Versäumung
- § 130 Abs. 1 BGB — Zugangsbegriff: Gelangen in den Machtbereich des Empfängers
- § 187 Abs. 1 BGB — Tag des Ereignisses zählt nicht mit
- § 188 Abs. 2 BGB — Fristende: gleicher Wochentag nach 3 Wochen um 24:00 Uhr
- § 193 BGB — Fristende fällt auf Samstag/Sonntag/Feiertag → nächster Werktag

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## KRITISCHE SOFORTPRÜFUNG (Schritte)

### Schritt 1: Zugangsdatum feststellen

Der Fristlauf beginnt mit dem **Zugang** der schriftlichen Kündigung (§ 4 Satz 1 KSchG).

Zugang bedeutet (§ 130 Abs. 1 BGB): Die Willenserklärung ist in den **Machtbereich** des Empfängers gelangt und er hatte unter gewöhnlichen Umständen die Möglichkeit der Kenntnisnahme.

**Zugangsmöglichkeiten und Beweis:**

| Zustellweg | Beweisstärke |
|---|---|
| Übergabeeinschreiben mit Rückschein | Sehr stark (Datum urkundlich belegt) |
| Persönliche Übergabe mit Zeugen | Stark |
| Einwurf-Einschreiben | Mittelstark (Datum durch Postunternehmen) |
| Einwurf in Briefkasten durch Boten | Mittel (Zeuge erforderlich) |
| Briefumschlag mit Poststempel | Mittel |
| Eigene Erinnerung ohne Beleg | Schwach |

**Prüffrage:** An welchem Tag und auf welche Weise wurde die Kündigung erhalten? Gibt es Beweise?

### Schritt 2: Fristberechnung §§ 187, 188 BGB

- Tag des Zugangs zählt **nicht** mit (§ 187 Abs. 1 BGB)
- Die Frist endet genau 3 Wochen später um 24:00 Uhr (§ 188 Abs. 2 BGB)
- Fällt das Fristende auf einen Samstag, Sonntag oder gesetzlichen Feiertag, endet die Frist am nächsten Werktag (§ 193 BGB)

**Beispielrechnung:**
- Zugang: Freitag, 10.01.2025
- Fristbeginn: Samstag 11.01.2025 (Tag nach Zugang, § 187 Abs. 1)
- Fristende: Freitag 31.01.2025 um 24:00 Uhr

### Schritt 3: Restfrist abschätzen

Bei weniger als 5 Tagen verbleibender Frist: **HOCHDRINGLICHKEIT** — sofortiger Handlungsbedarf. Klage unverzüglich einreichen oder Klage zu Protokoll des Urkundsbeamten erklären.

## Nachträgliche Klagezulassung § 5 KSchG

Ist die Drei-Wochen-Frist bereits abgelaufen, gibt es einen Ausnahmeweg:

**§ 5 Abs. 1 KSchG:** War ein Arbeitnehmer trotz aller ihm nach Lage der Umstände zuzumutenden Sorgfalt verhindert, die Klage rechtzeitig zu erheben, so ist auf seinen Antrag hin die Klage nachträglich zuzulassen.

**Anerkannte Verhinderungsgründe:**
- Schwere Erkrankung mit Bettlägerigkeit (objektive Unfähigkeit zur Klage)
- Bewusstlosigkeit oder stationärer Krankenhausaufenthalt
- Urlaub im Ausland ohne Kenntnis der Kündigung (wenn Kündigung nachgesandt wurde und später ankam)
- Täuschung durch Arbeitgeber über die Rechtslage (selten anerkannt)

**Nicht anerkannte Gründe:**
- Finanzielle Schwierigkeiten bei der Anwaltsuche
- Unwissenheit über die Klagefrist
- Verzögerung durch Beratungstermine
- Urlaub im Inland bei Kenntnis der Kündigung

**Fristen für den Zulassungsantrag:**
- 2 Wochen nach Wegfall des Hindernisses (§ 5 Abs. 3 KSchG)
- Spätestens: 6 Monate nach Ablauf der Drei-Wochen-Frist

## Entscheidungsbaum: Frist-Triage

```
Kündigung zugegangen?
└─ Zugangsdatum feststellen
 └─ Frist abgelaufen?
 ├─ Nein → SOFORT Klage vorbereiten; Frist im Kalender eintragen
 └─ Ja → Verhinderungsgrund vorhanden? (§ 5 KSchG)
 ├─ Ja (Krankheit, Bettlägerigkeit, etc.) → Antrag auf nachträgliche Zulassung
 │ Frist: 2 Wochen nach Wegfall des Hindernisses; max. 6 Monate
 └─ Nein → Kündigung gilt nach § 7 KSchG als wirksam; andere Ansprüche prüfen
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
