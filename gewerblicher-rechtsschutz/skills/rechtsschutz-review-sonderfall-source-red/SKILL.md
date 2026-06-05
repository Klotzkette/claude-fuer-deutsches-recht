---
name: rechtsschutz-review-sonderfall-source-red
description: "Review Sonderfall Source RED: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Review Sonderfall Source RED

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Review Sonderfall Source RED** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-rechtsschutz-tatbestand-beweis-und-belege` | Tatbestand, Beweis und Belegaufbau im gewerblichen Rechtsschutz: Wie IP-Verletzungen tatbestandsmäßig erfasst, Beweise gesichert und Belege für Abmahnung, EV und Klage aufbereitet werden. Checklisten für Marke, Patent, UWG und Urheberrecht. |
| `spezial-review-sonderfall-und-edge-case` | Sonderfälle und Edge Cases im gewerblichen Rechtsschutz: atypische Konstellationen bei Marke, Patent, Design, Urheberrecht und UWG. Erschöpfung, Verwirkung, FRAND, KI-generierte Inhalte, Open Source, Parallelimporte und weitere Grenzfälle. |
| `spezial-source-red-team-und-qualitaetskontrolle` | Red-Team und Qualitätskontrolle im gewerblichen Rechtsschutz: Systematische Überprüfung von Schriftsätzen, Memos und Rechtsanalysen auf Fehler, Quellenschwächen, Gegenargumente und blinde Flecken. Checkliste für interne Qualitätssicherung. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Review Sonderfall Source RED**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-rechtsschutz-tatbestand-beweis-und-belege`

**Fokus:** Tatbestand, Beweis und Belegaufbau im gewerblichen Rechtsschutz: Wie IP-Verletzungen tatbestandsmäßig erfasst, Beweise gesichert und Belege für Abmahnung, EV und Klage aufbereitet werden. Checklisten für Marke, Patent, UWG und Urheberrecht.

# Spezial: Tatbestand, Beweis und Belegaufbau im IP-Recht

## Zweck und Mandatsbezug

Dieser Skill behandelt die **tatbestandsmäßige Erfassung und Beweissicherung** bei IP-Verletzungen – die Grundlage für jede Abmahnung, jeden EV-Antrag und jede Klage. Wer gut belegt, gewinnt; wer Tatbestandsmerkmale nicht präzise erfasst, riskiert Zurückweisung des Antrags, Kostenfolgen und Verlust des Verfahrens.

Mandatsbezug: Anwalt hat Mandantenhinweis auf Verletzung; muss jetzt strukturiert den Tatbestand erfassen und Beweise sichern. Oder: EV-Antrag wird vorbereitet; Glaubhaftmachungspaket muss vollständig sein.

## Grundstruktur: Tatbestand im IP-Recht

### Allgemeines Prüfungsschema

Jede IP-Verletzung folgt demselben Grundschema:

1. **Schutzrecht:** Besteht, ist valide, gehört dem Antragsteller.
2. **Verletzungshandlung:** Tatbestandsmäßige Handlung des Verletzers.
3. **Keine Einwilligung / Lizenz:** Handlung ohne Erlaubnis des Schutzrechtsinhabers.
4. **Zurechnung:** Täterschaft oder Teilnahme des Verletzers.
5. **Kein Rechtfertigungsgrund:** Keine Erschöpfung, kein Schranken, keine Ausnahme.

## Tatbestandschecklisten nach Rechtsgebiet

### Markenrecht – § 14 Abs. 2 MarkenG

**Schutzrecht:**
- [ ] Marke eingetragen beim DPMA/EUIPO? Registerauszug mit aktuellem Datum?
- [ ] Anmelder = Kläger/Antragsteller oder exklusiver Lizenznehmer mit Klagerecht?
- [ ] Schutzdauer nicht abgelaufen? Jahresgebühren/Verlängerungsgebühren bezahlt?
- [ ] Keine Löschungsklage anhängig?

**Verletzungshandlung:**
- [ ] Zeichen des Verletzers identifiziert (Screenshot, Produktphoto, Werbematerial)?
- [ ] Verletzungshandlung nach § 14 Abs. 3 MarkenG (Anbringen, Anbieten, Einführen...)?
- [ ] Benutzt im geschäftlichen Verkehr (nicht privat)?
- [ ] Benutzt für Waren/Dienstleistungen (nicht dekorativ)?

**Ähnlichkeit:**
- [ ] Zeichenähnlichkeit (schriftbildlich, klanglich, begrifflich)?
- [ ] Warenähnlichkeit (Canon-Kriterien)?
- [ ] Verwechslungsgefahr im Rahmen der Gesamtabwägung?

### Patentrecht – § 9 PatG

**Schutzrecht:**
- [ ] Patent eingetragen, Patentschrift mit Ansprüchen vorhanden?
- [ ] Patent noch in Kraft? Jahresgebühren bezahlt?
- [ ] Kein Einspruchsverfahren oder Nichtigkeitsklage mit aufschiebender Wirkung?
- [ ] Kläger ist Inhaber oder exklusiver Lizenznehmer?

**Verletzungshandlung:**
- [ ] Alle Merkmale des Hauptanspruchs im Verletzungsobjekt?
- [ ] Wortsinngemäß oder äquivalent?
- [ ] Verletzungshandlung nach § 9 PatG: Herstellen, Anbieten, in Verkehr bringen, Gebrauchen, Einführen?
- [ ] Im Inland (Deutschland) oder im Schutzland (EP-Patent)?

**Kein Rechtfertigungsgrund:**
- [ ] Kein Vorbenutzungsrecht (§ 12 PatG)?
- [ ] Keine Forschungsausnahme (§ 11 Nr. 2 PatG)?
- [ ] Keine Erschöpfung (§ 10a PatG)?

### UWG – §§ 3, 5, 8 UWG

**Anspruchsberechtigung:**
- [ ] Mitbewerbereigenschaft: Mandant und Verletzer stehen in Wettbewerbsverhältnis?
- [ ] Oder: Klageberechtigter Verband (§ 8 Abs. 3 Nr. 2 UWG)?

**Verletzungshandlung:**
- [ ] Geschäftliche Handlung des Verletzers (§ 2 Abs. 1 Nr. 1 UWG)?
- [ ] Tatbestand: Irreführung (§ 5), Unterlassen (§ 5a), Rechtsbruch (§ 3a), Nachahmung (§ 4 Nr. 3)?
- [ ] Spürbarkeit (§ 3 Abs. 1 UWG)?

**Verletzungsbeleg:**
- [ ] Screenshot mit vollständiger URL, sichtbares Datum?
- [ ] Testkauf mit Beleg?
- [ ] Werbematerial (Flyer, Katalog, E-Mail)?

### Urheberrecht – §§ 97, 97a UrhG

**Schutzrecht:**
- [ ] Werkart: Text, Musik, Bild, Software, Film, Datenbankwerk?
- [ ] Schöpfungshöhe ausreichend (§ 2 Abs. 2 UrhG)?
- [ ] Urheber = Kläger oder Lizenznehmer mit Klagerecht?
- [ ] Schutzdauer: 70 Jahre p.m.a. (§ 64 UrhG) noch nicht abgelaufen?

**Verletzungshandlung:**
- [ ] Konkrete Verletzungshandlung: § 16 (Vervielfältigung), § 17 (Verbreitung), § 19a (Zugänglichmachung)?
- [ ] Ohne Einwilligung oder gesetzliche Schranke (§§ 44a ff. UrhG)?
- [ ] Nachweis der Identität oder substantiellen Ähnlichkeit?

## Beweissicherung: Technisches Vorgehen

### Screenshots als Beweismittel

- [ ] Vollständige URL in der Adressleiste sichtbar.
- [ ] Datum und Uhrzeit durch Betriebssystemuhr oder manuelle Notiz dokumentiert.
- [ ] Metadaten (EXIF) des Screenshots erhalten (nicht bearbeitet).
- [ ] Alternativ: Wayback Machine (archive.org) für zeitgestempelte Kopie.
- [ ] Bei Online-Shop: Screenshot des Angebots + Bestellseite.

### Testkauf

- [ ] Kaufbeleg / Quittung mit Datum, Verkäufer, Warenbezeichnung.
- [ ] Produkt selbst aufbewahren (Beweismittel für Gericht).
- [ ] Fotodokumentation des Produkts: Markierung, Verpackung, Produktbeschreibung.

### Eidesstattliche Versicherung

- [ ] Datum der Erstkenntnis.
- [ ] Wie die Verletzung entdeckt wurde.
- [ ] Zusammenfassung der Tatsachen des Verletzungsvorgangs.
- [ ] Bestätigung der Richtigkeit aller Anlagen.

## Belegpaket für EV-Antrag (Checkliste)

| Beleg | Zweck | Status |
|---|---|---|
| Registerauszug DPMA/EUIPO | Schutzrecht valide | [ ] |
| Screenshot Verletzung + URL + Datum | Verletzungshandlung belegt | [ ] |
| Eidesstattliche Versicherung | Glaubhaftmachung § 920 ZPO | [ ] |
| Testkauf mit Beleg (falls zutreffend) | Beweis Verletzungsprodukt | [ ] |
| Abmahnschreiben (falls vorhanden) | Reaktion der Gegenseite | [ ] |
| Vollstreckbare Ausfertigung EV (nach Erlass) | Vollzug § 929 ZPO | [ ] |

## Quellenregel

- [§ 14 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/14.html)
- [§ 9 PatG – dejure.org](https://dejure.org/gesetze/PatG/9.html)
- [§ 97 UrhG – dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 8 UWG – dejure.org](https://dejure.org/gesetze/UWG/8.html)
- Rechtsprechung zur Glaubhaftmachung: BGH auf [bgh.de](https://www.bundesgerichtshof.de); keine BeckRS-Blindzitate.

## Anschluss-Skills

- `spezial-klausel-beweislast-und-darlegungslast` – Beweislastverteilung
- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag
- `verletzungs-triage` – Erstentscheidung IP-Verletzung
- `spezial-freedom-schriftsatz-brief-und-memo-bausteine` – Schriftsatz-Bausteine

## 2. `spezial-review-sonderfall-und-edge-case`

**Fokus:** Sonderfälle und Edge Cases im gewerblichen Rechtsschutz: atypische Konstellationen bei Marke, Patent, Design, Urheberrecht und UWG. Erschöpfung, Verwirkung, FRAND, KI-generierte Inhalte, Open Source, Parallelimporte und weitere Grenzfälle.

# Spezial: Sonderfälle und Edge Cases im Gewerblichen Rechtsschutz

## Zweck und Mandatsbezug

Dieser Skill behandelt **atypische Konstellationen und Grenzfälle** im gewerblichen Rechtsschutz – Situationen, die außerhalb der Standardprüfung liegen und besondere Aufmerksamkeit erfordern. Edge Cases tauchen in der Praxis regelmäßig auf und können bei unsachgemäßer Behandlung zu teuren Fehlern führen.

Mandatsbezug: Mandant sagt „Das ist eine besondere Situation, ich bin nicht sicher, ob die normalen Regeln gelten." Anwalt erkennt, dass der Fall einen oder mehrere atypische Aspekte hat, die gesonderter Prüfung bedürfen.

## Edge Case 1: Erschöpfung (§ 24 MarkenG / Art. 15 EUTMR / § 10a PatG)

### Sachverhalt

Markeninhaber will Parallelimporteur stoppen, der Originalware aus einem anderen EU-Land importiert.

### Rechtslage

- **Erschöpfung:** Schutzrecht erlischt für konkrete Ware, sobald diese vom Inhaber oder mit seiner Zustimmung im EWR in Verkehr gebracht wurde.
- **Voraussetzungen:** Erstes Inverkehrbringen im EWR; durch Inhaber oder mit Zustimmung.
- **Ausnahmen (§ 24 Abs. 2 MarkenG):** Berechtigte Interessen des Inhabers: Zustand der Ware verändert; Ruf der Marke geschädigt (Umverpackung-Rechtsprechung EuGH).
- **Beweislast:** Parallelimporteur muss Erschöpfung nachweisen (EuGH „Van Doren + Q").

### Prüfpunkte

- Wurde Ware wirklich im EWR (nicht nur in EU) erstmals in Verkehr gebracht?
- Hat Markeninhaber Umverpackung durch Importeur zugestimmt oder berechtigtem Interesse widersprochen?
- EuGH-Rechtsprechung zu Pharmaprodukten: Hohe Anforderungen an Umverpackung.

## Edge Case 2: Verwirkung (§ 21 MarkenG / Art. 61 EUTMR)

### Sachverhalt

Markeninhaber hat 6 Jahre zugesehen, wie Verletzer identische Marke benutzt, ohne Widerspruch einzulegen.

### Rechtslage

- Verwirkung nach § 21 MarkenG: Ältere Marke verliert Anspruch gegen jüngere, wenn > 5 Jahre Duldung in Kenntnis der jüngeren Marke.
- Voraussetzungen: Duldung, Kenntnis, Zeitablauf 5 Jahre.
- Beweislast: Beklagter muss Verwirkung nachweisen.
- Wirkung: Älterer Markeninhaber verliert Durchsetzungsrechte; nicht die Marke selbst.

## Edge Case 3: FRAND bei standardessenziellen Patenten (SEP)

### Sachverhalt

Inhaber eines standardessenziellen Patents (SEP) verlangt überhöhte Lizenzgebühr oder droht mit Unterlassungsklage.

### Rechtslage

- **SEP:** Patent, das zur Implementierung eines Standards (z.B. 5G, Wi-Fi) technisch notwendig ist.
- **FRAND-Pflicht:** Inhaber hat ETSI/IETF-Lizenzbereitschaftserklärung abgegeben; muss faire, angemessene, nicht diskriminierende Bedingungen anbieten (FRAND).
- **EuGH „Huawei/ZTE" (2015):** Sechsstufiger Prozess vor Unterlassungsklage; SEP-Inhaber muss Lizenzbereitschaft des Verletzers prüfen.
- **Art. 102 AEUV:** Missbrauch einer marktbeherrschenden Stellung durch überhöhte FRAND-Konditionen.
- **Praxis:** Implementierer kann Lizenzbereitschaft erklären; dann kein Unterlassungsanspruch.

## Edge Case 4: KI-generierte Inhalte und IP-Schutz

### Sachverhalt

Mandant hat mit KI ein Bild, einen Text oder eine Musik erstellt und fragt, ob er Urheberrecht daran hat.

### Rechtslage

- **Urheberrecht UrhG § 2 Abs. 2:** Persönliche geistige Schöpfung erforderlich.
- Rein KI-generierter Inhalt ohne menschliche Schöpfung = **kein Urheberrechtsschutz** nach deutschem Recht.
- Wenn Mensch schöpferischen Beitrag leistet (Prompting, Selektion, Bearbeitung): Urheberrecht möglich – abhängig von Schöpfungshöhe des Beitrags.
- **Praktische Empfehlung:** Dokumentation des eigenen schöpferischen Beitrags; Prompt-Logs aufbewahren.
- **Training-Daten:** Verwendung urheberrechtlich geschützter Daten zum Training = potentielle Verletzung; stark diskutiert, noch nicht abschließend höchstrichterlich geklärt.

## Edge Case 5: Open Source und IP

### Sachverhalt

Mandant nutzt Open-Source-Software in kommerziellen Produkten und fragt, ob das IP-rechtlich problematisch ist.

### Relevante Lizenzen

| Lizenz | Copyleft-Effekt | Kommerzielle Nutzung |
|---|---|---|
| MIT/BSD | Kein Copyleft | Frei |
| Apache 2.0 | Schwaches Copyleft | Frei; Patentlizenz enthalten |
| LGPL | Eingeschränktes Copyleft | Frei bei dynamischem Linking |
| GPL v2/v3 | Starkes Copyleft | Derivate müssen GPL-konform bleiben |
| AGPL | Stärkstes Copyleft | Auch Netzwerknutzung erfasst |

- **GPL-Verletzung:** Quellcodeoffenlegungspflicht; Urheberrechtsverletzung bei Nichteinhaltung.
- **Patente:** Apache 2.0 enthält Patentverzicht; GPL v3 enthält Patentverzicht.
- Praktisch: Open-Source-Compliance-Prozess empfehlen (Lizenzscan, SBOM).

## Edge Case 6: Arbeitnehmererfindung (ArbnErfG)

### Sachverhalt

Mitarbeiter hat im Betrieb eine Erfindung gemacht; Arbeitgeber will sie anmelden.

### Rechtslage

- **§ 5 ArbnErfG:** Mitarbeiter muss Erfindung unverzüglich melden.
- **§ 6 ArbnErfG:** Arbeitgeber muss innerhalb 4 Monate Inanspruchnahme erklären.
- **Vergütung:** § 9 ArbnErfG; Erfinder hat Anspruch auf angemessene Vergütung.
- **Freie Erfindung:** Wenn Erfindung nicht betrieblich, kann Mitarbeiter Rechte behalten.
- **Fehler:** Arbeitgeber erklärt Inanspruchnahme nicht rechtzeitig → Erfindung wird frei.

## Edge Case 7: Domain-Grabbing und Cybersquatting

### Sachverhalt

Dritter hat Domain registriert, die Marke des Mandanten enthält.

### Handlungsoptionen

1. **WIPO-UDRP:** Für .com/.net/.org; Übertragung oder Löschung.
2. **DENIC-Dispute:** Für .de-Domains; DENIC-Streitbeilegungsordnung.
3. **Markenrechtliche Klage:** § 14 Abs. 2 MarkenG; Anspruch auf Übertragung.
4. **UWG-Klage:** § 4 Nr. 4 UWG; Abfangen von Kunden durch Verwechslungs-Domain.

## Quellenregel

- [§ 24 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/24.html)
- [§ 21 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/21.html)
- [§ 10a PatG – dejure.org](https://dejure.org/gesetze/PatG/10a.html)
- EuGH „Huawei/ZTE": [curia.europa.eu](https://curia.europa.eu) – C-170/13.
- ArbnErfG: [gesetze-im-internet.de/arbnerfg](https://www.gesetze-im-internet.de/arbnerfg/)
- WIPO-UDRP: [wipo.int/amc/en/domains](https://www.wipo.int/amc/en/domains/)
- Keine BeckRS-Blindzitate.

## Anschluss-Skills

- `open-source-pruefung` – Open Source Compliance
- `verletzungs-triage` – IP-Verletzung Erstentscheidung
- `erfindungsmeldung-aufnahme` – ArbnErfG Prozess
- `takedown-anweisung` – Domain-Takedown

## 3. `spezial-source-red-team-und-qualitaetskontrolle`

**Fokus:** Red-Team und Qualitätskontrolle im gewerblichen Rechtsschutz: Systematische Überprüfung von Schriftsätzen, Memos und Rechtsanalysen auf Fehler, Quellenschwächen, Gegenargumente und blinde Flecken. Checkliste für interne Qualitätssicherung.

# Spezial: Red-Team und Qualitätskontrolle

## Zweck und Mandatsbezug

Dieser Skill führt eine **systematische Red-Team-Prüfung** von IP-rechtlichen Analysen, Schriftsätzen, Memos und Abmahnungen durch. Er simuliert die Gegenperspektive: Was wird die Gegenseite einwenden? Welche Quellen sind schwach oder angreifbar? Wo sind die blinden Flecken der eigenen Argumentation?

Mandatsbezug: Anwalt hat EV-Antrag oder Abmahnschreiben fertiggestellt und will es vor Versand einem internen Review unterziehen. Kanzlei-Quality-Gate vor Einreichung von Schriftsätzen. Mandant fragt: Wie stark ist unser Fall wirklich?

## Red-Team-Grundprinzip

Das Red-Team versucht, die eigene Argumentation zu erschüttern – aus der Perspektive der Gegenseite, eines kritischen Richters oder eines neutralen Sachverständigen. Ziel ist nicht Pessimismus, sondern belastbare Qualität.

**Fünf Red-Team-Fragen:**
1. Was ist das schwächste Argument in unserem Schriftsatz?
2. Welche Gegenargumente hat die Gegenseite und warum könnten sie durchdringen?
3. Welche Quellen sind nicht verifizierbar oder könnten angegriffen werden?
4. Was haben wir möglicherweise übersehen?
5. Würde ein kritischer Richter unsere Argumentation als schlüssig bewerten?

## Checkliste: Red-Team-Prüfung Abmahnung

### Block A – Formale Überprüfung

- [ ] Aktivlegitimation des Abmahnenden klar begründet?
- [ ] Formvoraussetzungen §§ 13 UWG / 97a UrhG / 14 MarkenG vollständig?
- [ ] Verletzungshandlung präzise beschrieben (wann, wo, was genau)?
- [ ] Unterlassungserklärung beigefügt und inhaltlich korrekt?
- [ ] Frist angemessen (nicht zu kurz)?
- [ ] Streitwert / Kostenansatz korrekt und begründbar?

### Block B – Materielle Überprüfung

- [ ] Schutzrecht eingetragen, valide, nicht abgelaufen?
- [ ] Verletzung tatsächlich tatbestandsmäßig? Alle Merkmale geprüft?
- [ ] Spürbarkeit (UWG) oder Verwechslungsgefahr (MarkenG) ausreichend begründet?
- [ ] Keine offensichtliche Erschöpfung oder Verwirkungseinwand übersehen?
- [ ] Keine offensichtliche Missbrauchs-Indizien nach § 8c UWG?

### Block C – Quellen-Überprüfung

- [ ] Alle zitierten Normen in aktueller Fassung überprüft?
- [ ] Rechtsprechungszitate mit Gericht, Datum, AZ und prüfbarer Quelle?
- [ ] Kein BeckRS-Alleinzitat für tragende Aussagen?
- [ ] Keine Annahmen als gesicherte Fakten präsentiert?
- [ ] Offene Punkte explizit als solche markiert?

### Block D – Gegenargument-Analyse

| Gegenargument | Wahrscheinlichkeit | Antwort vorbereitet? |
|---|---|---|
| Kein Mitbewerberverhältnis (UWG) | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |
| Schutzrecht ungültig | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |
| Keine Verwechslungsgefahr | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |
| Erschöpfung | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |
| Verwirkung | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |
| § 8c UWG Missbrauch | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |
| Dringlichkeitsselbstwiderlegung | [ ] Hoch/Mittel/Gering | [ ] Ja/Nein |

## Checkliste: Red-Team-Prüfung EV-Antrag

### Block A – Verfügungsanspruch

- [ ] Schutzrechtsurkunde / Registerauszug aktuell und in Akte?
- [ ] Verletzungshandlung vollständig tatbestandsmäßig subsumiert?
- [ ] Keine wesentliche Voraussetzung übersehen?
- [ ] Tenor nicht zu weit formuliert (Risiko Gericht kürzt stark)?

### Block B – Verfügungsgrund

- [ ] Erstkenntnis-Datum belegt und in eidesstattlicher Versicherung genannt?
- [ ] Keine Selbstwiderlegung der Dringlichkeit (lange Wartezeit)?
- [ ] Wartezeit rational begründet (z.B. Zusammenstellnung Beweismittel)?

### Block C – Glaubhaftmachungspaket

- [ ] Eidesstattliche Versicherung vollständig und schlüssig?
- [ ] Alle genannten Anlagen tatsächlich beigefügt?
- [ ] Screenshots mit Datum und URL vollständig?
- [ ] Kein Widerspruch zwischen eidesstattlicher Versicherung und Anlagen?

### Block D – § 945 ZPO-Risiko

- [ ] Ist EV-Antrag tatsächlich begründet oder besteht erhebliches Risiko, dass EV ungerechtfertigt ist?
- [ ] Ist Mandant über § 945 ZPO-Schadensersatzrisiko informiert?
- [ ] Bei Zweifeln: Abmahnung statt EV als Alternative erwogen?

## Red-Team für Memos und Gutachten

### Quellen-Review

- [ ] Jede rechtliche Aussage auf Norm oder Rechtsprechung gestützt?
- [ ] Normen aktuell (kein veralteter Gesetzesstand)?
- [ ] Rechtsprechung: BGH/EuGH/BVerfG direkt zitiert (nicht Sekundärquelle)?
- [ ] Live-Check-Bedarf explizit markiert?

### Logik-Review

- [ ] Schlussfolgerungen aus den Prämissen logisch ableitbar?
- [ ] Keine verdeckten normativen Annahmen?
- [ ] Keine zirkulären Begründungen?
- [ ] Gegenposition fair dargestellt und widerlegt?

### Vollständigkeits-Review

- [ ] Alle relevanten Tatbestandsmerkmale geprüft?
- [ ] Alle einschlägigen Einwendungen behandelt?
- [ ] Offene Fragen explizit benannt (kein Totschweigen von Schwächen)?

## Ergebnis-Vorlage Red-Team

```
RED-TEAM ERGEBNIS
Dokument: _______________
Datum: _______________
Reviewer: _______________

Stärken:
1. _______________
2. _______________

Schwachstellen / offene Punkte:
1. _______________
2. _______________

Voraussichtliche Gegenargumente der Gegenseite:
1. _______________
2. _______________

Empfehlung vor Versand:
[ ] Keine Änderungen nötig
[ ] Kleinere Überarbeitungen (Details: _______)
[ ] Wesentliche Überarbeitung empfohlen (Details: _______)
[ ] Rücksprache mit Mandant erforderlich (Details: _______)
```

## Quellenregel

- [§ 8c UWG – dejure.org](https://dejure.org/gesetze/UWG/8c.html)
- [§ 945 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/945.html)
- Rechtsprechung immer mit Gericht, Datum, AZ und prüfbarer Quelle.
- Keine Aussagen aus Modellwissen ohne Live-Check bei tragenden Argumenten.

## Anschluss-Skills

- `workflow-redteam-qualitygate` – Red-Team-im Plugin
- `spezial-source-red-team-und-qualitaetskontrolle` – Dieser Skill (Selbstreferenz)
- `spezial-klausel-beweislast-und-darlegungslast` – Beweislastfragen
- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand und Beweis
