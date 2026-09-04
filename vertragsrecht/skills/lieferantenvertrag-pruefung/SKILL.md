---
name: lieferantenvertrag-pruefung
description: "Für Lieferanten-/Dienstleistervertrag-Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# Lieferanten-/Dienstleistervertrag-Prüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 305-310, 433, 434, 437, 438, 446, 474, 477, HGB § 377, bei Dienstleistungen/Werkleistungen BGB §§ 611, 631, 633 ff., bei Auslandslieferungen CISG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BGH-/EuGH-Datenbank und eur-lex.europa.eu live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Einen Lieferanten- oder Dienstleistervertrag gegen das tatsächlich verwendete Playbook der Rechtsabteilung prüfen (in `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`), jede abweichende Klausel identifizieren und dem Juristen mitteilen, was zu tun ist – mit konkreten Redline-Formulierungen, keinen vagen "Überarbeitung erwägen"-Empfehlungen. Maßgeblich: §§ 611, 631 BGB (Dienst-/Werkvertrag), §§ 434 ff. BGB (Kauf), §§ 305–310 BGB (AGB-Recht), LkSG, ggf. CISG.

## Eingaben

- Lieferanten- oder Dienstleistervertrag (Datei-Upload oder Direkteingabe)
- Ggf. Auftragsformular oder Leistungsbeschreibung separat
- Jahreswert/Gesamtvertragswert (für Eskalations-Routing erforderlich)
- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert, aktive Akte prüfen und Ausgaben dort speichern.

## Ablauf

### Schritt 1: Playbook laden

**Vor dem Vertragslesen** `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` lesen. Falls fehlend oder Platzhalter:

> Praxisprofil noch nicht konfiguriert.
>
> **Zwei Optionen:**
> - `/vertragsrecht:kaltstart-interview` ausführen (ca. 10 Minuten), dann Prüfung auf Ihr eigenes Playbook zugeschnitten.
> - "Provisorisch" sagen – dann Prüfung gegen generische Standardpositionen (deutsches Recht, mittlere Risikobereitschaft, Juristenrolle), alle Ausgaben mit `[PROVISORISCH – Praxisprofil für individuell zugeschnittene Ausgabe konfigurieren]` gekennzeichnet.

**Welche Seite?**
- Lieferant/Auftragnehmer liefert Waren/Leistungen → Käufer-/Auftraggeber-Seite
- Das Unternehmen verkauft Waren/Leistungen → Verkäufer-/Auftragnehmer-Seite
- Reseller, JV, Umsatzbeteiligung? → Fragen: "Auf welcher Seite steht [Unternehmen]?"

Zutreffenden Playbook-Abschnitt lesen. **Das K.-o.-Kriterium zuerst prüfen.** Falls vorhanden: am Anfang des Vermerks kennzeichnen und Detailprüfung einstellen – kein Sinn, 30 Minuten an Haftungsdeckeln zu arbeiten, wenn ein Vertragspartner IP-Rechte an unseren Produkten erhalten soll.

### Schritt 2: Orientierung

Den Vertrag einmal schnell lesen:

| Frage | Antwort |
|---|---|
| Vertragstyp | Werkvertrag (§ 631 BGB) / Dienstvertrag (§ 611 BGB) / Kaufvertrag (§ 433 BGB) / gemischt |
| Wer sind wir? | Auftraggeber / Auftragnehmer (Plugin geht von Auftraggeber aus – kennzeichnen falls abweichend) |
| Vertragspartner | Name; Groß-Konzern (verhandelt kaum) oder KMU (verhandelt)? |
| Jahreswert (ACV) | Betrag oder "nicht angegeben" → fragen |
| Laufzeit | Dauer, Verlängerungsmechanismus |
| AVV | beigefügt / referenziert / fehlt |
| Auftragsformular | separat / integriert |
| CISG anwendbar? | Auslandslieferant + Warenkauf → CISG prüfen, ggf. Abwahl-Klausel |

**Jahreswert fehlt:** Wenn der Hauptvertrag keinen Wert nennt:
> MSA nennt keinen Jahreswert; Preis steht im Auftragsformular. Eskalationsschwelle ist [Betrag aus CLAUDE.md]. Bitte Auftragsformular-Wert nennen oder mitteilen, ob der ACV über/unter dem Schwellenwert liegt.

### Schritt 3: Haftungsbegrenzung (§§ 276, 307, 309 Nr. 7 BGB)

Haftungsklauseln haben vier Dimensionen:

**a) Direktschäden-Deckel (§ 307 BGB):** Vielfaches der Vergütung; mit Playbook vergleichen.

**b) Mittelbare Schäden / Folgeschäden:**
- § 309 Nr. 7a BGB: Haftungsausschluss für Körperverletzung / Vorsatz gegenüber Verbrauchern absolut unwirksam.
- Im B2B: Ausschluss für leichte Fahrlässigkeit bei nicht wesentlichen Pflichten möglich; bei Kardinalpflichten nach BGH-Rspr. unwirksam.

**c) Ausnahmen vom Deckel:** Vorsatz, grobe Fahrlässigkeit, Verletzung von Leben/Körper/Gesundheit, Kardinalpflichten, Datenpannen, produkthaftungsrechtliche Ansprüche.

**d) Bemessungsgrundlage:** "im letzten Jahr gezahlte Vergütung" vs. "nach Vertrag insgesamt zu zahlende Vergütung" – prüfen.

### Schritt 4: Gewährleistung (§§ 433 ff., 631 ff. BGB)

**Werkvertrag (§§ 633 ff. BGB):**
- Mangelfreiheitspflicht § 633 BGB
- Nacherfüllungsrecht § 634 Nr. 1, § 635 BGB (Vorrang vor Rücktritt/Minderung)
- Verjährung § 634a BGB: 2 Jahre bei körperlichen Bauwerken/Sachen; 3 Jahre bei Arglist

**Kaufvertrag (§§ 434 ff. BGB; ggf. CISG):**
- Sachmangelfreiheit § 434 BGB; Beschaffenheitsvereinbarung prüfen
- Gefahrübergang § 446 BGB als Beweisstichtag bestimmen; der Käufer muss im Grundfall beweisen, dass der Mangel zu diesem Zeitpunkt vorhanden war
- Verjährung § 438 Abs. 1 Nr. 3 BGB: regelmäßig zwei Jahre, vertragliche Verkürzungen und Hemmung gesondert prüfen
- B2C-Sonderregel § 477 BGB nicht in B2B-Verträge übertragen: Nach BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, genügt im Verbrauchsgüterkauf eine binnen Jahresfrist auftretende Mangelerscheinung, wenn eine Verkäuferursache ernsthaft möglich ist; diese Vermutung gilt im Unternehmerverkehr nicht
- Rügepflicht im B2B (§ 377 HGB): Fristen für Untersuchung und unverzügliche Rüge; Wareneingangskontrolle als Vertragsprozess mit Dokumentationspflichten regeln
- Lieferantenvertrag aus Auftraggeber-Sicht sollte verlangen: Chargen-/Seriennummern, Prüfzeugnisse, CoC/CoA, Verpackungs- und Transportdaten, gemeinsame Befundsicherung, Musteraufbewahrung, unverzügliche Reaktionsfristen des Lieferanten und Anerkenntnis, dass Rügen über definierte Portale/E-Mail-Adressen zugehen
- CISG-Abwahl: Falls Lieferant im Ausland (Vertragsstaaten), CISG ausschließen oder bewusst einbeziehen

**B2B-Wareneingang als Klauselthema:**
- Der Vertrag darf die Wareneingangskontrolle nicht der operativen Zufälligkeit überlassen. Prüfe, ob ein Anhang oder eine Qualitätssicherungsvereinbarung festlegt, welche Stichproben, Messwerte, Fotos, Prüfintervalle und Sperrvermerke bei Lieferbeginn, Serienlieferung und Reklamation erstellt werden.
- Vermeide Klauseln, die § 377 HGB faktisch verschärfen, ohne dass die Fachabteilung dies leisten kann, etwa extrem kurze Rügefenster ab Lagerankunft bei komplexen technischen Gütern.
- Redline bei fehlendem Prozess: "Der Lieferant stellt für jede Lieferung prüffähige Chargen-, Serien- und Prüfunterlagen bereit. Beanstandungen können innerhalb der nach ordnungsgemäßem Geschäftsgang erforderlichen Untersuchungsfrist über das im Auftrag genannte Reklamationspostfach oder Lieferantenportal gerügt werden. Der Lieferant unterstützt die Befundsicherung unverzüglich, insbesondere durch technische Stellungnahme, Zugriff auf Prüfprotokolle und Sicherung von Rückstellmustern."

**Dienstvertrag (§§ 611 ff. BGB):**
- Kein Erfolg geschuldet; nur ordnungsgemäße Leistung
- Kündigung jederzeit möglich (§ 621 BGB bei Dauerschuldverhältnissen; § 314 BGB aus wichtigem Grund)

### Schritt 5: Datenschutz (Art. 28 DSGVO, BDSG)

- AVV vorhanden? Pflichtinhalt Art. 28 Abs. 3 DSGVO prüfen
- Sub-Auftragsverarbeiter: Genehmigungsmodell prüfen (Art. 28 Abs. 2, 4 DSGVO)
- Drittlandübermittlung: Standardvertragsklauseln (Art. 46 DSGVO) oder Angemessenheitsbeschluss
- Löschpflichten nach Vertragsende
- Meldepflichten bei Datenpannen (72-Stunden-Frist Art. 33 DSGVO; ggf. kürzere Vertragsfrist)
- Datenschutz-Schadensersatz Art. 82 DSGVO: Wechselwirkung mit Haftungsdeckel

### Schritt 6: LkSG – Lieferkettensorgfaltspflichten

Falls Lieferant in der Lieferkette und LkSG anwendbar (§ 1 LkSG: ab 1.000 AN seit 01.01.2024):

**Prüfpunkte:**
- Code of Conduct / Verhaltenskodex-Klausel vorhanden?
- Audit-/Inspektionsrecht des Auftraggebers (§ 6 LkSG)
- Meldepflicht bei Verstößen gegen menschenrechtliche/umweltbezogene Sorgfaltspflichten
- Außerordentliches Kündigungsrecht bei LkSG-Verstößen (§ 7 Abs. 3 LkSG)
- Weitergabepflicht an Unterlieferanten (§ 9 LkSG)

**Rechtsprechung und Quellenlage noch im Aufbau.** Prüfung anhand Gesetzestext, BAFA-Leitlinien und konkret bereitgestellter oder lizenziert verifizierter Quellen. Keine Kommentar- oder Aufsatzfundstellen aus Modellwissen.

### Schritt 7: IP und Nutzungsrechte (§§ 15 ff. UrhG, PatG)

- Wer ist Eigentümer von im Rahmen des Vertrags entwickelten Werken?
- Umfang der Nutzungsrechtseinräumung (§ 31 UrhG: einfach / ausschließlich; zeitlich, räumlich, inhaltlich)
- Rückruf-/Kündigungsrechte des Urhebers (§§ 41, 42 UrhG) – oft nicht abbedingbar
- Software: § 69a ff. UrhG; Open-Source-Lizenzen

### Schritt 8: Laufzeit und Kündigung (§§ 314, 620, 621 BGB)

- Laufzeit, Verlängerungsmechanismus, Kündigungsfristen
- § 314 BGB: außerordentliches Kündigungsrecht aus wichtigem Grund; nicht ausschließbar
- Auswirkungen der Kündigung: Vergütung, Datenrückgabe, Übergangshilfe

### Schritt 9: AGB-Kontrolle (§§ 305–310 BGB)

- Einbeziehung: § 305 Abs. 2 BGB – Hinweis + Kenntnisnahmemöglichkeit
- Überraschende Klauseln: § 305c BGB
- Transparenzgebot: § 307 Abs. 1 S. 2 BGB
- Klauselverbote §§ 308, 309 BGB; im B2B als Indiz-Wirkung
- Kollidierende AGB ("battle of forms"): §§ 154, 155 BGB; Konsenstheorie vs. Restgültigkeitslösung

## Abweichungsklassifikation

| Stufe | Kriterien | Maßnahme |
|---|---|---|
| **GRÜN** | Entspricht Playbook-Position oder liegt darüber; marktübliche kleinere Abweichungen | Zur Kenntnis |
| **GELB** | Außerhalb Standardposition, aber im verhandelbaren Marktbereich | Redline mit Fallback-Position; Geschäftsauswirkung schätzen |
| **ROT** | Außerhalb akzeptablem Bereich; materielles Risiko; löst Eskalation aus | Konkretes Risiko erläutern; marktübliche Alternative; Eskalationspfad |

## Verhandlungspriorität

| Tier | Bezeichnung | Beschreibung | Strategie |
|---|---|---|---|
| 1 | Must-Haves | Unbegrenzte/unzureichende Haftung; fehlender Datenschutz; IP-Gefährdung; regulatorische Konflikte | Nie ohne Eskalation nachgeben |
| 2 | Should-Haves | Haftungsdeckel-Anpassungen; Freistellungsumfang; Flexibilität bei Kündigung; Audit-Rechte | Firm verhandeln; Tier-3 opfern |
| 3 | Nice-to-Haves | Bevorzugter Gerichtsstand; Fristen-Präferenzen; kleinere Definitions-Verbesserungen | Konzessions-Kandidaten für Tier-2 |

```markdown
## Fazit
[2–3 Sätze: unterzeichnungsreif / [N] Punkte zu klären / blockiert durch [K.-o.-Kriterium]]

## Befunde

### 🔴 Blockierend
**[Klauseltitel]** – § [X.X]
> "[Zitat]"
**Rechtliches Risiko:** 🔴 | **Geschäftliche Reibung:** [Stufe]
Warum problematisch: [konkretes Risiko; Norm + BGH-Rspr.]
Empfohlener Redline: `[Streichung/Ersatz mit konkreter Formulierung]`
Eskalation an: [Person/Rolle aus CLAUDE.md]

### 🟠 Hoch
[…]

### 🟡 Mittel
[…]

### 🟢 Niedrig / Zur Kenntnis
[…]

---

## LkSG-Prüfung
[Ergebnis der LkSG-Punkte]

## CISG
[Anwendbar / abgewählt / Abwahlklausel empfohlen]

## Nächste Schritte
[Entscheidungsbaum gemäß CLAUDE.md]
```

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Normen und Rspr.:
- §§ 611, 631 BGB – Dienst-/Werkvertrag; § 433 BGB – Kaufvertrag
- §§ 305–310 BGB – AGB-Recht
- § 377 HGB – Rügepflicht Handelskauf
- §§ 1 ff. LkSG; §§ 15 ff. UrhG – Nutzungsrechte
- Art. 28 DSGVO – AVV; Art. 1, 6 CISG – Anwendbarkeit/Abwahl

Kommentare:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken / typische Fehler

- **CISG-Geltung vergessen:** Bei Auslands-Kaufverträgen CISG prüfen; Abwahl ggf. notwendig.
- **Rügepflicht § 377 HGB übersehen:** Im B2B-Handelskauf Mängel unverzüglich rügen, sonst Rechtsverlust.
- **AGB-Kollision (battle of forms):** Wenn beide Parteien AGB verwenden, prüfen, welche gilt.
- **LkSG-Kündigungsklausel fehlt:** Ohne vertragliches Recht faktisch eingeschränkte LkSG-Durchsetzung.
- **Mandantengeheimnis:** § 43a Abs. 2 BRAO, § 203 StGB bei jeder Weitergabe beachten.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
