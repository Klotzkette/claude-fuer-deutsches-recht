---
name: dringlichkeitsmarker-einwilligung-hinweis
description: "Dringlichkeitsmarker Einwilligung Hinweis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dringlichkeitsmarker Einwilligung Hinweis

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Dringlichkeitsmarker Einwilligung Hinweis** im Plugin Mandantenanfragen-Assistent. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dringlichkeitsmarker` | Eingehende Mandantenanfrage enthaelt möglicherweise Fristenproblem oder dringenden Handlungsbedarf. Dringlichkeitscheck Kanzlei-Intake. Prüfraster: Signale Hauptverhandlung naechste Woche Kündigungsfrist Zwangsvollstreckung Insolvenzantrag. Dringlichkeitsstufen HOCH (sofortiger Anwalt-Anruf) MITTEL NIEDRIG. Output: Dringlichkeits-Einschaetzung mit konkreter Handlungsempfehlung. Abgrenzung zu anfrage-eingang-parser (Datenextraktion) und erstantwort-generator (Antwort). |
| `einwilligung-hinweis-datenschutz` | Kanzlei bietet telefonischen Transkriptionsservice an und muss DSGVO-konforme Einwilligung einholen. Art. 6 Abs. 1 lit. a DSGVO Art. 13 DSGVO Informationspflicht. Prüfraster: Rechtsgrundlage Einwilligung Informationspflicht Hinweis kein Mandatsverhältnis Widerrufsrecht. Output: DSGVO-konforme Einwilligungsklausel für Transkriptionsservice. Abgrenzung zu mandatsverhältnis-hinweis (Haftungsausschluss) und vertraulichkeit-erinnerung. |
| `erstantwort-generator` | Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Prüfraster: Dank für Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung Mandatsverhältnis-Disclaimer Schlussformel. Output: fertige Erstantwort-E-Mail mit allen Pflichthinweisen. Abgrenzung zu muster-erstantwort (Template-Vorlage) und anrede-uebernehmen. |

## Arbeitsweg

Im Plugin Mandantenanfragen-Assistent gilt für **Dringlichkeitsmarker Einwilligung Hinweis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dringlichkeitsmarker`

**Fokus:** Eingehende Mandantenanfrage enthaelt möglicherweise Fristenproblem oder dringenden Handlungsbedarf. Dringlichkeitscheck Kanzlei-Intake. Prüfraster: Signale Hauptverhandlung naechste Woche Kündigungsfrist Zwangsvollstreckung Insolvenzantrag. Dringlichkeitsstufen HOCH (sofortiger Anwalt-Anruf) MITTEL NIEDRIG. Output: Dringlichkeits-Einschaetzung mit konkreter Handlungsempfehlung. Abgrenzung zu anfrage-eingang-parser (Datenextraktion) und erstantwort-generator (Antwort).

# Dringlichkeitsmarker

Dieser Skill erkennt Eile- und Fristen-Signale in der Eingangsanfrage und setzt eine Dringlichkeitsstufe. Bei hoher Dringlichkeit ist ein sofortiger Anwaltsrückruf erforderlich — die anfragende Person darf nicht auf eine E-Mail-Antwort warten.

## Triage zu Beginn
1. Enthält die Anfrage eine konkrete Datumsangabe oder Fristnennung (Gerichtstermin, Kuendigungsfrist, Rechtsmittelfrist)?
2. Welches Rechtsgebiet ist betroffen — welche typischen Fristen gelten (KSchG 3 Wochen, § 517 ZPO 1 Monat Berufung)?
3. Gibt es Anzeichen fuer Zwangsvollstreckung, Insolvenzantrag oder strafrechtliche Eile?
4. Ist die Dringlichkeitsstufe HOCH — muss der Anwalt sofort anrufen statt auf E-Mail zu warten?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 KSchG — Kuendigungsschutzklage-Frist: 3 Wochen ab Zugang der Kuendigung (Notfrist)
- § 517 ZPO — Berufungsfrist: 1 Monat ab Urteilszustellung (Notfrist, unverlaengerbar)
- § 51 BRAO — Haftung: Fristversaeumnis durch mangelnde Dringlichkeits-Erkennung
- § 233 ZPO — Wiedereinsetzung: nur moeglich wenn Kanzlei keine Fahrlässigkeit trifft

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Dringlichkeitsstufen

| Stufe | Kriterium | Konsequenz |
|---|---|---|
| **HOCH** | Konkrete Frist, bevorstehender Termin, Haftungsrisiko | Anwalt ruft sofort zurück; Erstantwort enthält Sofortruf-Hinweis |
| **MITTEL** | Zeitdruck erkennbar, aber keine akute Frist | Rückmeldung innerhalb 24 Stunden |
| **NIEDRIG** | Kein Zeitdruck erkennbar | Normale Bearbeitungsreihenfolge |
| **UNBEKANNT** | Keine Zeitangaben in der Anfrage | Wie MITTEL behandeln |

## Eile-Signale: Explizite Nennungen (HOCH)

### Gerichtstermine und Verhandlungen

- "Hauptverhandlung nächste Woche" / "Termin beim Amtsgericht am [Datum]"
- "einstweilige Verfügung wurde zugestellt"
- "Versäumnisurteil droht" / "ich war nicht bei der Verhandlung"
- "Berufungsfrist läuft ab"
- "Einspruchsfrist gegen den Strafbefehl"

### Vertragsfristen

- "Kündigungsfrist läuft" / "Kündigung zum [Datum]"
- "Vertragsfrist endet diese Woche"
- "Widerspruchsfrist" / "Einspruchsfrist"
- "Rückgabefrist" / "Mängelrüge muss raus"

### Vollstreckung und Insolvenz

- "Zwangsvollstreckung eingeleitet" / "Gerichtsvollzieher war da"
- "Pfändung meines Kontos"
- "Insolvenzantrag wurde gestellt"
- "Pfändungs- und Überweisungsbeschluss erhalten"

### Strafrechtliche Ereignisse

- "bin vorgestern verhaftet worden" / "sitze in Untersuchungshaft"
- "Haftprüfungstermin" / "Haftbefehl"
- "Polizei hat mich heute befragt"
- "Vorladung als Beschuldigter erhalten"

### Behördliche Fristsetzungen

- "Behörde hat mir Frist bis [Datum] gesetzt"
- "Bescheid mit Rechtsmittelfrist erhalten"
- "Widerspruchsfrist gegen Bescheid läuft"
- "Abschiebungsandrohung" / "Ausreisefrist"

## Eile-Signale: Zeitwörter und Adverbien (HOCH oder MITTEL)

| Signal | Stufe |
|---|---|
| "sofort", "dringend", "heute noch", "jetzt" | HOCH |
| "diese Woche", "nächste Woche", "bis Freitag" | HOCH |
| "bald", "in Kürze", "demnächst" | MITTEL |
| "in den nächsten Wochen", "nächsten Monat" | MITTEL |
| "irgendwann", "wenn Sie Zeit haben" | NIEDRIG |

## Haftungsfall-Signale (immer HOCH)

- "Ich werde verklagt" / "mir wurde eine Klage angekündigt"
- "Abmahnung erhalten"
- "Schadensersatzforderung" über einem relevanten Betrag
- "Vertragsstrafe droht"
- "mein Unternehmen ist in Gefahr"

## Ausgabeformat

```
DRINGLICHKEIT
=============
Stufe: [HOCH / MITTEL / NIEDRIG / UNBEKANNT]
Frist/Termin: [Datum und Art oder "nicht erkannt"]
Signal: [Zitat des Eile-Signals aus der Anfrage oder "keins"]
Begründung: [Kurze Erklärung der Bewertung]

MASSNAHMEN:
 [x] Sofortiger Anwaltsrückruf erforderlich — NICHT auf E-Mail warten
 [ ] Rückmeldung innerhalb 24 Stunden
 [ ] Normale Bearbeitung
 [ ] Frist im Kalender eintragen: [Datum]
```

## Hinweis-Text für die Erstantwort-Mail (bei HOCH)

```
WICHTIG: Aus Ihrer Anfrage haben wir entnommen, dass möglicherweise eine
Frist oder ein wichtiger Termin unmittelbar bevorsteht. Bitte rufen Sie
uns umgehend unter [SEKRETARIATS-TELEFON] an. Warten Sie bitte nicht auf
eine Antwort per E-Mail — Fristen können nicht durch eine
Eingangsbestätigung gewahrt werden.
```

## Hinweis für das Sekretariat (Interne Notiz bei HOCH)

```
INTERN — SOFORTMASSNAHME ERFORDERLICH
Rechtsanwalt/Rechtsanwältin muss diese Person sofort zurückrufen.
Mögliche Frist: [Datum/Zeitfenster]
Mögliches Risiko: [Kurzbeschreibung aus dem Signal]
Telefon der anfragenden Person: [aus Parsing]
```

## Falsch-Negativ-Schutz

Bei Unsicherheit über die Dringlichkeit: Eher MITTEL als NIEDRIG. Bei Unsicherheit ob MITTEL oder HOCH: Eher HOCH. Der Schaden durch übersehene Fristen ist größer als der Aufwand eines unnötigen Sofortrückrufs.

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datenquelle
- `erstantwort-generator` — empfängt die Dringlichkeitsstufe und Hinweis-Texte
- `folgekorrespondenz-vorbereiten` — Dringlichkeitsstufe im CRM-Eintrag
- `mandatsverhaeltnis-hinweis` — bei HOCH: Langform mit Frist-Warnung

---
<!-- AUDIT 27.05.2026 | Bundle 036
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Aktion: Eintrag geloescht.
-->

## 2. `einwilligung-hinweis-datenschutz`

**Fokus:** Kanzlei bietet telefonischen Transkriptionsservice an und muss DSGVO-konforme Einwilligung einholen. Art. 6 Abs. 1 lit. a DSGVO Art. 13 DSGVO Informationspflicht. Prüfraster: Rechtsgrundlage Einwilligung Informationspflicht Hinweis kein Mandatsverhältnis Widerrufsrecht. Output: DSGVO-konforme Einwilligungsklausel für Transkriptionsservice. Abgrenzung zu mandatsverhältnis-hinweis (Haftungsausschluss) und vertraulichkeit-erinnerung.

# Einwilligung-Hinweis-Datenschutz

Dieser Skill formuliert die datenschutzrechtlich erforderliche Einwilligungsklausel für die Verarbeitung von Sprachdaten im Rahmen des Transkriptionsservices. Da zum Zeitpunkt der Erstanfrage noch kein Mandatsverhältnis besteht, ist die Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO die maßgebliche Rechtsgrundlage.


## Triage zu Beginn
1. Liegt die Anfrage vor Mandatsannahme (Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO noetig) oder nach Mandatserstellung (Art. 6 Abs. 1 lit. b DSGVO als Rechtsgrundlage)?
2. Enthaelt die Anfrage besondere Kategorien personenbezogener Daten (Gesundheit, Strafrecht — Art. 9 DSGVO)?
3. Soll der Hinweis in die Erstantwort-Mail eingebettet oder als separater Datenschutzhinweis gesandt werden?
4. Welcher Transkriptionsdienstleister wird eingesetzt — liegt ein AVV nach Art. 28 DSGVO vor?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. a DSGVO — Einwilligung als Rechtsgrundlage fuer Sprachdaten-Verarbeitung vor Mandatsannahme
- Art. 9 Abs. 2 lit. a DSGVO — Ausdrückliche Einwilligung fuer besondere Kategorien (Gesundheit, Strafrecht)
- Art. 13 DSGVO — Informationspflicht bei Ersterhebung: vollstaendige Transparenzpflicht
- Art. 7 Abs. 3 DSGVO — Widerrufsrecht: jederzeit ohne Nachteile

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rechtlicher Hintergrund

### Warum Einwilligung?

Bei einem bestehenden Mandatsverhältnis wäre die Verarbeitung von Mandantendaten zur Durchführung des Vertrags auf Art. 6 Abs. 1 lit. b DSGVO gestützt. Da im Stadium der Erstanfrage noch kein Mandat zustande gekommen ist, fehlt diese Rechtsgrundlage. Die einzige verbleibende, praxistaugliche Rechtsgrundlage ist die freiwillige, informierte und ausdrückliche Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO.

### Besonderes bei Sprachdaten

Sprachaufnahmen enthalten personenbezogene Daten (Art. 4 Nr. 1 DSGVO). Sofern aus dem Sachverhalt Gesundheitsdaten, Informationen über strafrechtliche Verurteilungen oder andere besondere Kategorien (Art. 9 DSGVO) hervorgehen, ist zusätzlich Art. 9 Abs. 2 lit. a DSGVO als Rechtsgrundlage heranzuziehen (ausdrückliche Einwilligung für besondere Kategorien).

### Informationspflichten nach Art. 13 DSGVO

Bei Erhebung personenbezogener Daten (hier: Sprachaufnahme) direkt bei der betroffenen Person sind nach Art. 13 DSGVO zu informieren über:

1. Name und Kontaktdaten der Verantwortlichen (Kanzlei)
2. Zweck und Rechtsgrundlage der Verarbeitung
3. Empfänger der Daten (ggf. Transkriptionsdienstleister als Auftragsverarbeiter)
4. Speicherdauer
5. Betroffenenrechte (Auskunft, Berichtigung, Löschung, Widerspruch)
6. Widerrufsrecht bei Einwilligung
7. Beschwerderecht bei der Aufsichtsbehörde

## Vollständige Einwilligungsklausel (Langform)

Für den Datenschutzhinweis, der auf Anfrage übersandt wird oder auf der Kanzlei-Website verfügbar ist:

---

**Datenschutzinformation zum Transkriptionsservice**
*(gemäß Art. 13 DSGVO)*

**Verantwortliche:** [KANZLEI-NAME], [KANZLEI-ADRESSE], [KANZLEI-E-MAIL]

**Zweck der Verarbeitung:** Automatisierte Verschriftung Ihrer mündlichen Sachverhaltsschilderung zur Vorbereitung einer anwaltlichen Ersteinschätzung.

**Rechtsgrundlage:** Ihre ausdrückliche Einwilligung gemäß Art. 6 Abs. 1 lit. a DSGVO. Soweit Ihre Schilderung besondere Kategorien personenbezogener Daten (z. B. Gesundheitszustand, strafrechtliche Vorwürfe) enthält, stützen wir uns zusätzlich auf Art. 9 Abs. 2 lit. a DSGVO.

**Kein Mandatsverhältnis:** Zum Zeitpunkt der Aufnahme besteht zwischen Ihnen und [KANZLEI-NAME] noch kein Mandatsverhältnis. Diese Informationsaufnahme begründet kein Anwalts-Mandantenverhältnis und stellt keine Rechtsberatung dar.

**Empfänger:** Das Transkript wird ausschließlich an [KANZLEI-NAME] übermittelt. Der Transkriptionsdienstleister ist als Auftragsverarbeiter (Art. 28 DSGVO) vertraglich zur Vertraulichkeit und Einhaltung der DSGVO verpflichtet.

**Speicherdauer:** Die Sprachaufnahme wird nach erfolgreicher Transkription unverzüglich gelöscht. Das Transkript wird bis zum Abschluss der Vorprüfung gespeichert, längstens [FRIST — z. B. 6 Monate], sofern kein Mandat zustande kommt.

**Ihre Rechte:** Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18) und Datenübertragbarkeit (Art. 20 DSGVO).

**Widerrufsrecht:** Sie können Ihre Einwilligung jederzeit ohne Angabe von Gründen mit Wirkung für die Zukunft widerrufen. Der Widerruf berührt nicht die Rechtmäßigkeit der bis dahin erfolgten Verarbeitung. Widerruf per E-Mail an: [KANZLEI-E-MAIL]

**Beschwerderecht:** Sie haben das Recht, sich bei der zuständigen Datenschutz-Aufsichtsbehörde zu beschweren.

---

## Kurzform (für die Erstantwort-Mail)

```
Wichtiger Datenschutzhinweis: Da zwischen uns noch kein Mandatsverhältnis
besteht, verarbeiten wir Ihre Sprachdaten ausschließlich auf Basis Ihrer
ausdrücklichen Einwilligung (Art. 6 Abs. 1 lit. a DSGVO). Zu Beginn des
Anrufs bestätigen Sie Ihr Einverständnis. Sie können es jederzeit widerrufen.
Die vollständige Datenschutzinformation senden wir Ihnen auf Anfrage zu.
```

## Pflicht-Ansage zu Beginn des Transkriptions-Anrufs

Der Transkriptionsservice muss zu Beginn jedes Anrufs folgende Ansage abspielen:

```
Guten Tag. Sie haben den automatisierten Transkriptionsservice von
[KANZLEI-NAME] erreicht. Ihre Schilderung wird aufgezeichnet und
automatisch verschriftlicht. Die Aufnahme wird ausschließlich zu diesem
Zweck verwendet und vertraulich behandelt. Da noch kein Mandatsverhältnis
besteht, basiert diese Verarbeitung auf Ihrer Einwilligung nach der
Datenschutz-Grundverordnung. Wenn Sie einverstanden sind, drücken Sie
bitte die Taste 1 oder sagen Sie laut und deutlich "Ja". Wenn Sie nicht
einverstanden sind, legen Sie bitte auf oder bleiben Sie in der Leitung
— wir verbinden Sie dann mit unserem Sekretariat.
```

Ohne Bestätigung: keine Aufnahme. Kein Einverständnis — kein Transkript.

## Verweise auf andere Skills

- `transkriptionsdienst-erklaerung` — bettet diese Klausel ein
- `mandatsverhaeltnis-hinweis` — ergänzender Disclaimer
- `erstantwort-generator` — Kurzform in der Antwortmail

## 3. `erstantwort-generator`

**Fokus:** Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Prüfraster: Dank für Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung Mandatsverhältnis-Disclaimer Schlussformel. Output: fertige Erstantwort-E-Mail mit allen Pflichthinweisen. Abgrenzung zu muster-erstantwort (Template-Vorlage) und anrede-uebernehmen.

# Erstantwort-Generator

Dieser Hauptskill erstellt die vollständige formelle Erstantwort-E-Mail an einen potenziellen Mandanten. Er koordiniert alle Teilskills und fügt deren Output zu einem druckfertigen Schreiben zusammen.


## Triage zu Beginn
1. Sind alle Teil-Skills bereits ausgefuehrt (Parsing, Spam-Check, Dringlichkeit, Anrede, Sprache)?
2. Welche Dringlichkeitsstufe wurde gesetzt — bei HOCH Sofortruf-Hinweis in der Mail einfuegen?
3. Besteht bereits ein Mandatsverhältnis oder handelt es sich um eine Erstanfrage (Kein-Mandat-Disclaimer erforderlich)?
4. Soll der Transkriptionsservice-Hinweis aktiviert werden (Trigger: Anfrage ist kurz/fragmentarisch oder Nutzer kann nicht schreiben)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: Hinweis auf voraussichtliche Gesamtkosten vor Mandatsannahme
- Art. 13 DSGVO — Informationspflicht: Ersterhebung personenbezogener Daten begruendet sofortige Informationspflicht
- § 43 BRAO — Sorgfaltspflicht: zeitnahe und vollstaendige Beantwortung eingehender Anfragen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch gegenueber dem potenziellen Mandanten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf (Koordination der Teil-Skills)

1. **Parsing:** Skill `anfrage-eingang-parser` läuft zuerst und liefert strukturierte Daten.
2. **Spam-Check:** Skill `spam-und-massen-anfrage-filter` — bei Spam: keine Antwort generieren, Aussortierungs-Flag setzen.
3. **Dringlichkeit:** Skill `dringlichkeitsmarker` — bei HOCH: sofortigen Anwaltsanruf priorisieren, Hinweis in der Mail einfügen.
4. **Anrede:** Skill `anrede-uebernehmen` — liefert die formelle Anredezeile.
5. **Sprache:** Skill `mehrsprachige-antwort` — bei nicht-deutschsprachiger Anfrage Sprachumschaltung.
6. **Mail-Aufbau:** Dieser Skill fügt alle Bausteine zusammen.
7. **CRM-Eintrag:** Skill `folgekorrespondenz-vorbereiten` wird parallel ausgelöst.

## Aufbau der Erstantwort-Mail

### Betreff

```
Re: [Original-Betreff der Eingangsmail]
```
oder falls kein Betreff vorhanden:
```
Ihre Anfrage an [KANZLEI-NAME] — Eingangsbestätigung
```

### Körper der Mail (Muster-Struktur)

```
[ANREDEZEILE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

[DRINGLICHKEITS-HINWEIS — nur wenn HOCH: Absatz einfügen, sonst weglassen]

Wir begleiten potenzielle Mandantinnen und Mandanten gern dabei, die richtigen
nächsten Schritte zu finden. Bitte beachten Sie, dass [MANDATSVERHAELTNIS-DISCLAIMER-KURZFORM].

Für eine erste Terminabsprache stehen wir Ihnen telefonisch zur Verfügung:

 Sekretariat: [SEKRETARIATS-TELEFON]
 Erreichbarkeit: [ERREICHBARKEITSZEITEN]

Um Ihren Fall bestmöglich vorzubereiten, bitten wir Sie, uns vorab Ihren
Sachverhalt in einer kurzen E-Mail zusammenzufassen:

 — Was ist der Kern Ihres Anliegens?
 — Wann hat das zugrunde liegende Ereignis stattgefunden?
 — Gibt es Fristen, Termine oder Bescheide, die wir kennen sollten?
 — Wer ist die Gegenseite (Person, Unternehmen, Behörde)?

[TRANSKRIPTIONS-ABSCHNITT — nur wenn Anfragende nicht schreiben kann/mag:]

Falls Ihnen eine schriftliche Schilderung schwerfällt, bieten wir Ihnen
einen automatisierten Transkriptionsservice an. Sie rufen dort an und schildern
Ihr Anliegen mündlich. Die Aufnahme wird automatisch verschriftlicht und uns
vertraulich übermittelt.

Wichtiger Hinweis zur Datenverarbeitung: [EINWILLIGUNGS-TEXT-KURZFORM]

Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

[/TRANSKRIPTIONS-ABSCHNITT]

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-TELEFON]
[KANZLEI-E-MAIL]

---
[MANDATSVERHAELTNIS-FUSSZEILE]
```

## Bausteine im Detail

### Dank-Formulierung

Standard: "vielen Dank für Ihre Anfrage, die uns heute zugegangen ist."

Varianten:
- Bei dringlicher Anfrage: "vielen Dank für Ihre Anfrage. Wir haben Ihr Anliegen als dringend zur Kenntnis genommen."
- Bei Empfehlung: "vielen Dank für Ihre Anfrage, die uns durch [Quelle, soweit genannt] zugegangen ist."

### Dringlichkeits-Hinweis (nur bei HOCH)

```
WICHTIG: Aus Ihrer Anfrage haben wir entnommen, dass möglicherweise eine
Frist oder ein Termin unmittelbar bevorsteht. Bitte rufen Sie uns
umgehend unter [SEKRETARIATS-TELEFON] an, damit wir die Situation sofort
einschätzen können. Warten Sie bitte nicht auf eine schriftliche Rückmeldung.
```

### Telefonische Terminvergabe

Pflichtbestandteil. Enthält:
- Telefonnummer des Sekretariats (aus Skill `telefon-konfiguration`)
- Erreichbarkeitszeiten (aus `kanzlei.json`)

### Bitte um Sachverhaltszusammenfassung

Formular-Fragen (s. oben). Alternativ freie Formulierung:
"Bitte schildern Sie uns Ihr Anliegen in einigen Sätzen — Datum des Ereignisses, beteiligte Parteien, bestehende Fristen und Ihr Ziel."

### Transkriptionsservice-Hinweis

Nur einfügen wenn:
- Die anfragende Person explizit schreibt, dass sie nicht schreiben kann/mag, oder
- Die Sekretariatsmitarbeiterin den Modus manuell aktiviert.

Enthält: Telefonnummer des Transkriptionsservices, kurze Ablauferklärung, DSGVO-Einwilligungshinweis in Kurzform (Langform aus Skill `einwilligung-hinweis-datenschutz`).

### Mandatsverhältnis-Disclaimer

Kurzform in der Mail: "Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis begründet und keine Rechtsberatung darstellt."

Langform in der Fußzeile: aus Skill `mandatsverhaeltnis-hinweis`.

### Schlussformel

Standard: "Mit freundlichen Grüßen"

Varianten bei Sprache:
- Englisch: "Yours sincerely," / "Kind regards,"
- Französisch: "Veuillez agréer l'expression de mes salutations distinguées,"
- Italienisch: "Distinti saluti,"

## Ausgabe

Der Skill gibt die fertige E-Mail als formatierten Text aus, bereit zum Kopieren in das E-Mail-Programm des Sekretariats. Zusätzlich:
- Interne Zusammenfassung der getroffenen Entscheidungen (welche Heuristiken, welche Abschnitte eingefügt/weggelassen)
- Hinweis auf ausstehende manuelle Prüfungen (z. B. wenn Name nicht ermittelbar war)

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datengrundlage
- `anrede-uebernehmen` — Anredezeile
- `telefon-konfiguration` — Telefonnummern
- `transkriptionsdienst-erklaerung` — Transkriptions-Abschnitt
- `einwilligung-hinweis-datenschutz` — DSGVO-Einwilligung
- `mandatsverhaeltnis-hinweis` — Disclaimer
- `dringlichkeitsmarker` — Dringlichkeits-Hinweis
- `spam-und-massen-anfrage-filter` — Vor-Filterung
- `folgekorrespondenz-vorbereiten` — CRM-Eintrag parallel
- `mehrsprachige-antwort` — Sprache der Antwort
- `muster-erstantwort` — Vorlagenschreiben als Referenz
