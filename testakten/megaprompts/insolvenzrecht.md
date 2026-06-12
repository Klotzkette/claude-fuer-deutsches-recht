# Megaprompt: insolvenzrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 89 Skills des Plugins `insolvenzrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Insolvenzrecht (Allgemein): ordnet Rolle (Schuldner GmbH/Person, Gläubiger, Verwalter),…
2. **mandat-triage-insolvenzrecht** — Eingangs-Abfrage für insolvenzrechtliche Mandate — Mandant ist Geschäftsführer mit Antragspflicht Gläubiger der Forderun…
3. **anfechtungsrechte-antragspflicht-15a** — Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. P…
4. **anschluss** — Einstieg, Schnelltriage und Fallrouting im Insolvenzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wu…
5. **antragspflicht-15a-inso** — Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§…
6. **do-versicherung-manager-haftung** — Insolvenzverwalter verklagt Geschäftsführer und D&O-Versicherung soll Deckung prüfen oder Manager fragt nach Versicherun…
7. **glaeubigerantrag-glaeubigerausschuss** — Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowoh…
8. **glaeubigerausschuss-mitwirkung** — Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichte…
9. **insolvenzgeld-165-sgb-iii** — Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzge…
10. **kaltstart-interview** — Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-d…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Insolvenzrecht (Allgemein): ordnet Rolle (Schuldner GmbH/Person, Gläubiger, Verwalter), markiert Frist (§ 15a Antragspflicht 3 Wochen), wählt Norm (InsO, EuInsVO, InsVV) und Zuständigkeit (Insolvenzgericht (AG)), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Insolvenzrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anfechtungsrechte-antragspflicht-15a` — Anfechtungsrechte Antragspflicht 15A
- `einstieg-schnelltriage-fallrouting` — Anschluss
- `antragspflicht-15a-17-19` — Antragspflicht 15A 17 19
- `antragspflicht-15a-inso` — Antragspflicht 15A Inso
- `auslaendischer-insolvenzverwalter-register-und-grundbuch` — Auslaendischer Insolvenzverwalter Register und Grundbuch
- `auslaendischer-office-holder-register-und-grundbuch` — Auslaendischer Office Holder Register und Grundbuch
- `belegmatrix-formular-portal-und-einreichung` — Belegmatrix Formular Portal und Einreichung
- `chronologie-internationaler-bezug-und-schnittstellen` — Chronologie Internationaler Bezug und Schnittstellen
- `do-versicherung-manager-haftung` — DO Versicherung Manager Haftung
- `einfuehrung-verhandlung-vergleich-und-eskalation` — Einfuehrung Verhandlung Vergleich und Eskalation
- `feststellung-sonderfall-glaeubigerantrag-inso` — Feststellung Sonderfall Glaeubigerantrag Inso
- `forderungsanmeldung-glaeubiger-174-177-inso` — Forderungsanmeldung Glaeubiger 174 177 Inso
- `glaeubigerantrag-glaeubigerausschuss` — Glaeubigerantrag Glaeubigerausschuss
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 15a Abs. 1 InsO Antragsfrist 3 Wochen bei ZU, 6 Wochen bei Überschuldung, § 28 InsO Anmeldefrist, § 188 InsO Schlusstermin.
- Fachpfad wählen: zentrale Anker im Insolvenzrecht sind InsO §§ 1, 13, 14, 15a, 17, 18, 19, 20, 21, 22, 27, 35, 39, 47, 55, 56, 60, 64, 80, 87, 97, 129, 133, 142, 174, 175, 179, 187, 199, 270, 270a-d, 286, 287, 295, 300, StaRUG §§ 1, 29, 31, 39, 49–55, 84, 100, 102. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Schuldner, IV/SV/Restrukturierungsbeauftragter, Gläubigerausschuss, Insolvenzgericht, Gläubiger, Geschäftsführer (§ 15a-Adressat).
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-insolvenzrecht`

_Eingangs-Abfrage für insolvenzrechtliche Mandate — Mandant ist Geschäftsführer mit Antragspflicht Gläubiger der Forderung anmelden will oder Arbeitnehmer der Insolvenzgeld beantragt. Klaert Mandantenrolle und Vorgang (Eroeffnungsantrag Eigenverwaltung Schutzschirm StaRUG Restschuldbefreiung). Sof..._

# Mandat-Triage Insolvenzrecht

## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Insolvenzrecht** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Insolvenzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsbereich

Eingangs-Abfrage für insolvenzrechtliche Mandate — Mandant ist Geschäftsführer mit Antragspflicht Gläubiger der Forderung anmelden will oder Arbeitnehmer der Insolvenzgeld beantragt. Klaert Mandantenrolle und Vorgang (Eroeffnungsantrag Eigenverwaltung Schutzschirm StaRUG Restschuldbefreiung). Sofort-Fristen Antragspflicht § 15a InsO drei Wochen Anmeldefristen Insolvenzgeld § 165 SGB III zwei Monate. Normen §§ 13 17 18 19 InsO Eroeffnungsantrag Insolvenzgründe. Eskalation Telefon-Sofort bei Antragspflicht-Verletzung Geschäftsführer-Haftung. Output Triage-Memo Fristen-Ampel Routing zu anfechtungsrechte-prüfen und anderen Skills. Abgrenzung zu insolvenzrecht-kaltstart-interview (Plugin-Profil-Befuellung). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Insolvenzrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Schuldner (Privatperson Selbstständig Gesellschaft)
- Geschäftsführer / Vorstand
- Gesellschafter
- Gläubiger einzelner
- Gläubiger-Banken
- Insolvenzverwalter
- Sachwalter (Eigenverwaltung)
- Arbeitnehmer
- Anfechtungs-Gegner

### Frage 2 — Vorgang?

- Antragspflicht-Prüfung § 15a InsO
- Eigenantrag stellen
- Gläubigerantrag erhalten — Reaktion
- Eigenverwaltung beantragen
- Schutzschirm § 270d InsO
- StaRUG-Verfahren
- Insolvenzgeld
- Forderungsanmeldung
- Insolvenzplan
- Anfechtungs-Verfahren
- Restschuldbefreiung
- Verbraucherinsolvenz
- Gesellschafter-Haftung
- Geschäftsführer-Haftung § 64 GmbHG a. F. / § 15b InsO

### Frage 3 — Akute Eilbedürftigkeit?

- **Antragspflicht** § 15a InsO drei Wochen — Strafbarkeit
- **Vermögensverschiebung** läuft / steht bevor
- **Massive Vermögensabflüsse** im Vorfeld
- **Gläubigerantrag** zugestellt
- **Insolvenzgericht** Termin morgen
- **Pfändung Konto** Existenz bedrohend
- **Arbeitnehmer Lohn-Ausstand**
- **Sanierungs-Krise** akut

### Frage 4 — Verfahrensstadium?

- Vor Antragspflicht — Beratung
- Antragspflicht akut
- Eröffnungsverfahren (vorläufiges Verfahren)
- Eröffnetes Verfahren
- Berichtstermin
- Prüfungstermin
- Schlussverteilung
- Aufhebung
- Wohlverhaltensphase

### Frage 5 — Schuldner-Form?

- Natürliche Person
- Selbstständig
- GmbH AG GmbH & Co. KG
- Personengesellschaft
- Verein
- Stiftung
- Genossenschaft
- Auslandsbezug (EuInsVO)

### Frage 6 — Wirtschaftliche Verhältnisse?

- Aktiva (Buchwert Verkehrswert)
- Passiva
- Liquidität-Stand
- Drohende Zahlungs-Unfähigkeit § 18 InsO
- Zahlungs-Unfähigkeit § 17 InsO
- Überschuldung § 19 InsO
- Fortbestehens-Prognose

### Frage 7 — Frist?

- **§ 15a InsO** drei Wochen Antragspflicht
- **Forderungsanmeldung** mit Anmeldefrist im Insolvenzgericht-Bekanntmachung
- **Anfechtungs-Verjährung** drei Jahre § 146 InsO
- **Restschuldbefreiungs-Antrag** mit Eigenantrag oder binnen einer Woche nach Aufforderung
- **Insolvenzgeld-Antrag** zwei Monate ab Insolvenz-Eröffnung § 165 SGB III

### Frage 8 — Besondere Konstellationen?

- Konzern-Insolvenz
- Eigenverwaltung möglich (Liquidität ausreichend Geschäftsführer geeignet)
- Schutzschirm-Verfahren möglich
- StaRUG vor Insolvenz?
- Auslandsbezug
- Familieninsolvenz

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Antragspflicht-Prüfung | `antragspflicht-15a-inso` |
| Gläubigerantrag erhalten | `glaeubigerantrag-pruefung` |
| Zahlungsunfähigkeit-Prüfung | `zahlungsunfaehigkeit-pruefung-17-inso` |
| Überschuldungs-Prüfung | `ueberschuldung-pruefung-19-inso` |
| Liquiditätsvorschau | `liquiditaetsvorschau-insolvenzrechtlich` |
| Anfechtungs-Verteidigung / -Aktivierung | `anfechtungsrechte-pruefen` |
| Fortbestehensprognose | weiter an `fortbestehensprognose`-Plugin |
| Plugin-Konfiguration | `kaltstart-interview` |
| Eigenverwaltung-Beratung | (Skill eigenverwaltung-beratung — perspektivisch) |
| StaRUG-Restrukturierung | (Skill starug-verfahren — perspektivisch) |
| Insolvenzplan | (Skill insolvenzplan — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** sehr strikt — Insolvenzverwalter Schuldner Gläubiger
- **Streitwert** bei Anfechtung Forderung Restmasse
- **Honorarvereinbarung** RVG / Insolvenzverwalter-Vergütung nach InsVV
- **Versicherungs-Deckung** D&O bei Geschäftsführer Berufshaftpflicht Insolvenzverwalter

## Eskalation

- **Telefon-Sofort** Antragspflicht-Frist Strafbarkeit
- **Binnen einer Stunde** Gläubigerantrag-Reaktion Vermögensverschiebung verhindern
- **Heute** Eigenantrag-Vorbereitung Forderungsanmeldung
- **Diese Woche** Insolvenzplan-Erstentwurf Anfechtungs-Klage

## Ausgabe

- `triage-protokoll-insolvenzrecht.md`
- Aktenanlage
- Frist im Fristenbuch (§ 15a InsO drei Wochen vorrangig)
- Sofort-Strategie-Vorschlag
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Quellen

- InsO §§ 1 ff. 15a 17 18 19 129 ff. 146 165 270 270d
- StaRUG
- GmbHG § 64 (a. F.) ersetzt durch § 15b InsO
- StGB §§ 283 ff.
- SGB III § 165
- BGH IX. Zivilsenat
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Weitere Leitentscheidungen — Mandats-Triage (Stand Mai 2026)

- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers; bei Wechsel der Geschäftsleitung Mandantenrolle und Verantwortlichkeit präzise abklären.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer; bei Hinweisen auf Strohmann-/Firmenbestattungs-Konstellation Mandantenrolle besonders sorgfältig prüfen.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung; bei Geschäftsführerhaftung Deckung gesondert prüfen.

---

## Skill: `anfechtungsrechte-antragspflicht-15a`

_Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche Benachteiligung § 133 unentgeltliche Leistung § 134 Gesellschafterdarlehen § 135. Anf..._

# Insolvenzanfechtungsrechte prüfen

## Arbeitsbereich

Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche Benachteiligung § 133 unentgeltliche Leistung § 134 Gesellschafterdarlehen § 135. Anfechtungsfrist drei Monate bis zehn Jahre Bargeschäfts-Privileg § 142 InsO. Berechnung Anfechtungsansprüche Beweislast Hin- und Herwirkung Forderungsanmeldung. Output Anfechtungs-Prüf-Memo mit Tatbestands-Checkliste Betrag und Verteidigungslinien. Abgrenzung: vorsatzanfechtung-133-inso für vertiefte § 133-Prüfung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzanfechtungsrechte prüfen` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Insolvenzantrags-Datum
- Insolvenzeröffnungs-Datum
- Eröffnungs-Beschluss
- Liste der zurückgeforderten Zahlungen / Vermögens-Bewegungen
- Buchhaltung Schuldner
- Korrespondenz Schuldner / Anfechtungs-Gegner
- Vertragsbasis (Werkvertrag Kaufvertrag Darlehen)
- Wissen des Anfechtungs-Gegners über Zahlungs-Schwierigkeiten

## Schritt 1 — Allgemeine Anfechtungs-Voraussetzungen § 129 InsO

- **Rechtshandlung** vor Verfahrenseröffnung
- **Gläubiger-Benachteiligung** (Aktivenminderung Passivmehrung)
- Beweislast für Benachteiligung beim Insolvenzverwalter

## Schritt 2 — Spezielle Anfechtungs-Tatbestände

### § 130 InsO — Kongruente Deckung

- Rechtshandlung in **letzten drei Monaten** vor Antrag
- Schuldner **zahlungsunfähig**
- Anfechtungs-Gegner **kannte** Zahlungsunfähigkeit oder Umstände die zwingend darauf schließen lassen
- "Kongruent" — Anfechtungs-Gegner hatte vertraglichen Anspruch auf das Erlangte

### § 131 InsO — Inkongruente Deckung

- Rechtshandlung in **letztem Monat** vor Antrag oder danach (Abs. 1 Nr. 1)
- In letzten drei Monaten — wenn Schuldner zahlungsunfähig (Abs. 1 Nr. 2)
- In letzten drei Monaten — wenn Anfechtungs-Gegner Benachteiligungs-Wissen (Abs. 1 Nr. 3)
- "Inkongruent" — Anfechtungs-Gegner hatte **keinen** vertraglichen Anspruch (Aufrechnungs-Möglichkeit Sicherheit-Leistung Vorauszahlung)

### § 132 InsO — Unmittelbar nachteilige Rechtshandlung

- Rechtshandlung in letzten drei Monaten
- Schuldner zahlungsunfähig
- Anfechtungs-Gegner kannte oder Anhaltspunkte für Zahlungsunfähigkeit Benachteiligungsvorsatz

### § 133 InsO — Vorsätzliche Benachteiligung

- Rechtshandlung in **letzten zehn Jahren** (vier Jahre für Deckungs-Konstellationen seit 2017-Reform)
- Schuldner mit **Vorsatz** Gläubiger zu benachteiligen
- Anfechtungs-Gegner kannte den Vorsatz

**Vermutung § 133 Abs. 1 Satz 2 InsO** — Vorsatzkenntnis vermutet wenn Anfechtungs-Gegner Zahlungsunfähigkeit drohende Zahlungsunfähigkeit und Gläubigerbenachteiligung kannte.

**BGH-Rechtsprechung dazu** restriktiver geworden mit § 133-Reform 2017 — bestätigt und konkretisiert:

- **BGH IX ZR 72/20 vom 06.05.2021** (Grundsatzentscheidung Neuausrichtung) — bloße objektive Zahlungsunfähigkeit lässt keinen automatischen Schluss auf Vorsatz zu.
- **BGH IX ZR 129/22 vom 18.04.2024** — Bestätigung der Linie: bei verifizierter Zahlungsunfähigkeit ist konkret darzulegen, ob der Schuldner wusste oder billigend in Kauf nahm, dass andere Gläubiger zu späterer Zeit nicht vollständig befriedigt werden können.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- Seit 2017 Vorsatz-Anfechtung gestaffelt:
 - **Vier Jahre** für Deckungs-Konstellationen (§ 133 Abs. 2 InsO) — kongruent
 - **Zehn Jahre** für sonstige Konstellationen (§ 133 Abs. 1 InsO)

### § 134 InsO — Unentgeltliche Leistung

- Rechtshandlung in **letzten vier Jahren**
- Unentgeltliche Leistung (Schenkung Verzicht)
- **Schenkung Verwandter** — auch Mittel-/Mittelbar
- Geringe Geschenke ausgenommen

### § 135 InsO — Gesellschafterdarlehen-Rückgewähr

- **Rückgewähr Gesellschafterdarlehen** im letzten Jahr vor Antrag
- **Anfechtbar auch bei Erfüllung** ohne weitere Voraussetzungen
- Auch wirtschaftlich gleichgestellte Forderungen

## Schritt 3 — Bargeschäft § 142 InsO

### Ausschluss der Anfechtung

- Bargeschäft = **gleichwertige Gegenleistung in unmittelbarem zeitlichem Zusammenhang**
- Anfechtbarkeit ausgeschlossen — außer bei Vorsatzanfechtung § 133 InsO; dann nur, wenn der Schuldner **unlauter** handelte und der andere Teil dies erkannte (§ 142 Abs. 1 Hs. 2 InsO).

### Unlauterkeit (BGH IX ZR 122/23 vom 05.12.2024)

Erstmalige höchstrichterliche Konkretisierung: Unlauterkeit erfordert ein gezielt schädigendes Verhalten gegenüber den übrigen Gläubigern; die Transaktion muss bewusst zur Benachteiligung anderer oder zur gezielten Bevorzugung des Empfängers genutzt werden. Bloße dauerhafte Verlustsituation genügt nicht.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>

### Anwendung

- Tausch sofortig
- Bezahlung gegen Lieferung
- Lohnzahlung gegen Arbeit (kein starres 30-Tage-Limit; enger zeitlicher Zusammenhang erforderlich, BGH IX ZR 122/23)

## Schritt 4 — Rechtshandlung Definition

- **Rechtsgeschäft** Vertrag Anfechtung Zustimmung
- **Realakt** mit rechtlicher Bedeutung (Ausübungs-Erklärung Vollstreckungs-Maßnahme)
- **Zwangsvollstreckung** zählt als Rechtshandlung § 131 Abs. 1 Nr. 1 / 2 InsO

## Schritt 5 — Bösgläubigkeit Anfechtungs-Gegner

### Kenntnis-Element

- **Tatsächliche Kenntnis** Zahlungs-Unfähigkeit
- **Umstände die zwingend darauf schließen lassen** § 130 Abs. 2 InsO
- Bei Geschäftspartnern mit häufigen Kontakten beobachtbar

### Bei Banken

- Sonderbeobachtung — Bank hat über Zahlungsverhalten Konto-Information
- Kündigung Kreditlinie → Bank musste Kenntnis haben

### Bei Steuerbehörden

- BGH-Linie: Vollstreckungs-Druck der Finanzbehörde indiziert regelmäßig Kenntnis der Zahlungsunfähigkeit
- §§ 130, 131 anwendbar bei Steuer-Beitreibung; konkrete BGH-Entscheidung (Datum, Aktenzeichen) vor Ausgabe über dejure.org/openjur.de verifizieren

## Schritt 6 — Rechtsfolge

### Verpflichtungs-Wirkung § 143 InsO

- **Rückgewähr** in Natur oder Wertersatz
- **Zinsen** gegen Anfechtungs-Gegner ab Eröffnung

### Rückforderung Gläubiger-Stellung § 144 InsO

- Anfechtungs-Gegner kann Forderung wieder geltend machen
- Anmeldung zur Insolvenz-Tabelle
- Insolvenzquote auf wieder aufgelebte Forderung

## Schritt 7 — Verjährung § 146 InsO

- **Drei Jahre** ab Verfahrenseröffnung
- Hemmung-Vorschriften BGB

## Schritt 8 — Strategische Überlegung — Insolvenzverwalter-Sicht

- **Vermögen-Aufnahme** vollständig
- **Identifikation Anfechtungs-Tatbestände** Massevergleich
- **Verfolgungs-Reihenfolge** je Aussicht
- **Vergleichs-Strategie** vs. Klage
- **Beweislast-Konstellation** Bereich § 133 InsO erschwert seit 2017
- **Anfechtungs-Klagen** zur Bestätigung Quote

## Schritt 9 — Strategische Überlegung — Anfechtungs-Gegner-Sicht

- **Bargeschäft-Verteidigung** prüfen
- **Kenntnis-Bestreitung**
- **Vergleichs-Verhandlung** häufig erfolgreich (50–70 Prozent Quote als Verhandlungsstand)
- **Sicherungseigentum** vs. unentgeltliche Leistung
- **Verjährung** § 146 InsO drei Jahre häufig vergessen

## Schritt 10 — Sonderfälle

### Anfechtbarkeit von Lohnzahlungen

- Arbeitnehmer-Lohn als Bargeschäft typisch
- Aber Vorausziehungen Sonderzahlungen ggf. anfechtbar

### Anfechtung Konzernsachverhalten

- Cash-Pool-Verbund
- Konzerndarlehen → Gesellschafterdarlehen § 135

### Anfechtung Familien-Übertragung

- Häufig § 134 — unentgeltliche Leistung Verwandter
- Vier-Jahres-Frist

## Schritt 11 — Anfechtungsklage

- Sachlich LG zuständig § 71 GVG
- Klageschrift mit Anfechtungs-Tatbestand
- Beweislast Insolvenzverwalter
- Beklagter: Anfechtungs-Gegner

## Ausgabe

- `anfechtung-pruefung.md` mit Anfechtungstatbestand-für-Tatbestand
- Tabelle der angefochtenen Vorgänge mit Erfolgsaussicht
- Bei Verteidigung: Bargeschäft-Analyse Kenntnis-Bestreitung
- Klageschrift-Entwurf oder Verteidigungs-Schriftsatz
- Frist im Fristenbuch (drei Jahre § 146 InsO)
- Vergleichs-Verhandlungs-Vorbereitung

## Quellen

- InsO §§ 129–147
- **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit beim Bargeschäft § 142 InsO
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung Vorsatzanfechtung
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Anfechtung wegen gesellschafterähnlicher Stellung (§ 135 InsO)
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- Ältere Leitentscheidungen (insb. BGH IX ZR 72/20 vom 06.05.2021, Liquiditätsstatus-Beweislast, § 138 InsO nahestehende Personen): vor Ausgabe konkretes Datum, Aktenzeichen, Randnummer in offener Quelle (dejure.org, openjur.de, bundesgerichtshof.de) prüfen.
- Literatur und Handbücher nur bei vorhandenem Live-Zugriff.

## Triage — Anfechtungs-Erstcheck

Bevor losgelegt wird, klaere:

1. **Tatbestandsbereich?** § 130/131 (3 Monate), § 132 (3 Monate), § 133 Abs. 1 (10 Jahre) / Abs. 2 (4 Jahre), § 134 (4 Jahre), § 135 (1 Jahr).
2. **Verjährung § 146 InsO?** 3 Jahre ab Kenntnis des IV, max. 10 Jahre ab Rechtshandlung — Frist sofort prüfen!
3. **Nahestehende Person § 138 InsO?** Gesellschafter >25%, GF, Ehegatte → Beweislastumkehr zugunsten IV.
4. **Bargeschäft § 142 InsO?** Bei kongruenten unmittelbaren Austauschen: Bargeschäft prüfen; Unlauterkeit nach BGH IX ZR 122/23 separat darlegen.
5. **Vorsatz § 133 InsO?** Nach BGH IX ZR 129/22 (18.04.2024): konkrete Bedrohungslage und Erwartung dauerhafter Unterdeckung, nicht bloß drohende ZU.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 266a StGB
- § 18 AktG
- § 64 GmbHG
- § 15 GmbHG
- § 40 GmbHG
- § 15 AktG
- Art. 17 DSGVO
- § 266 StGB
- § 3a EStG
- § 263 StGB
- § 94 StaRUG
- § 203 StGB

### Leitentscheidungen

- BGH IX ZR 122/23
- BGH IX ZR 129/22
- BFH II R 19/01
- BGH IV ZR 66/25
- BGH II ZR 206/22

---

## Skill: `anschluss`

_Einstieg, Schnelltriage und Fallrouting im Insolvenzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: or..._

# Insolvenzrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzrecht — Allgemein` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Insolvenzrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anfechtungsrechte-pruefen` | Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche… |
| `antragspflicht-15a-inso` | Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter… |
| `do-versicherung-manager-haftung` | Insolvenzverwalter verklagt Geschäftsführer und D&O-Versicherung soll Deckung prüfen oder Manager fragt nach Versicherungsschutz in der Krise. Prüfraster D&O-Versicherung Claims-made-Prinzip Schadensereignis vs.… |
| `forderungsanmeldung-glaeubiger-174-177-inso` | Gläubiger meldet Forderung im Insolvenzverfahren an §§ 174-177 InsO: Fristen Form Anlagen Rang § 39 InsO Vorsatz § 174 Abs. 2 InsO nachtraegliche Anmeldung § 177 InsO Prüfungstermin § 176 Bestreiten § 178 Tabelle § 179… |
| `glaeubigerantrag-pruefung` | Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowohl aus Gläubigerperspektive (Antragstellung) als auch aus Schuldnerperspektive (Abwehrstrategien).… |
| `glaeubigerausschuss-mitwirkung` | Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorläufiger Gläubigerausschuss § 22a… |
| `insolvenzgeld-165-sgb-iii` | Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei… |
| `insolvenzrecht-kaltstart-interview` | Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter /… |
| `konzerninsolvenz-koordination` | Mehrere Gesellschaften eines Konzerns sind insolvent und Koordination der Verfahren muss geplant werden. Prüfraster Konzerninsolvenz §§ 269a-269i InsO Konzern-Gerichtsstand § 3a InsO Gruppen-Folgeverfahren § 3d InsO.… |
| `liquiditaetsvorschau-insolvenzrechtlich` | Erstellt und bewertet die rollierende Liquiditätsvorschau als strukturierte Arbeitsgrundlage für insolvenzrechtliche Tatbestände nach § 17 InsO (Zahlungsunfähigkeit) und § 19 Abs. 2 InsO (Fortbestehensprognose). Lädt,… |
| `mandat-triage-insolvenzrecht` | Eingangs-Abfrage für insolvenzrechtliche Mandate — Mandant ist Geschäftsführer mit Antragspflicht Gläubiger der Forderung anmelden will oder Arbeitnehmer der Insolvenzgeld beantragt. Klaert Mandantenrolle und Vorgang… |
| `ueberschuldung-pruefung-19-inso` | Führt die zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO durch: Fortbestehensprognose (Stufe 1) und insolvenzrechtlicher Überschuldungsstatus auf Liquidationswertbasis (Stufe 2). Lädt, wenn Überschuldung… |
| `uebertragende-sanierung-und-asset-deals` | Insolvenzverwalter will Geschäftsbetrieb verkaufen oder Investor kauft aus der Insolvenz und braucht Prüfung des Asset-Deals. Prüfraster uebertragende Sanierung Asset Deal im Regelverfahren Zustimmung… |
| `vorsatzanfechtung-133-inso` | Insolvenzverwalter will Zahlungen nach § 133 InsO anfechten oder Gläubiger muss Vorsatzanfechtung abwehren. Prüfraster vorsaetzliche Gläubiger-Benachteiligung Kenntnis Gläubiger des Benachteiligungsvorsatzes. BGH-Linie… |
| `zahlungsunfaehigkeit-pruefung-17-inso` | Erstellt ein strukturiertes Prüfgutachten zum Eröffnungsgrund der Zahlungsunfähigkeit nach § 17 InsO. Berechnet den Liquiditätsstatus zum Stichtag, wendet das 10-%-/3-Wochen-Schema des BGH an und würdigt Indizien der… |

## Worum geht es?

Dieses Plugin deckt die insolvenzrechtlichen Grundfragen ab, die in der taeaglichen Beratungspraxis vor und waehrend eines Insolvenzverfahrens entstehen. Im Mittelpunkt stehen die Eroeffnungsgruende (Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit, Ueberschuldung), die Insolvenzantragspflicht des Geschaeftsleiters nach § 15a InsO, das Zahlungsverbot nach § 15b InsO, Anfechtungsrechte des Insolvenzverwalters, Forderungsanmeldung durch Glaeubiger, D-and-O-Haftungsfragen und die Koordination von Konzerninsolvenzen.

Das Plugin richtet sich an Anwaelte, Insolvenzverwalter, Sachwalter, Sanierungsberater und Unternehmensberater. Es ist ein strukturiertes Pruefwerkzeug für insolvenzrechtliche Triage-Situationen. Fuer vertiefte Planwerkstatt-Arbeit (Insolvenzplan, StaRUG) steht das Plugin `insolvenzplan-starug-planwerkstatt` zur Verfuegung.

## Wann brauchen Sie diese Skill?

- Geschaeftsfuehrer fragt, ob er einen Insolvenzantrag stellen muss und bis wann die Dreiwochenfrist laeuft.
- Glaeubiger moechte wissen, ob er einen Insolvenzantrag stellen kann und was dabei zu beachten ist.
- Arbeitnehmer eines insolventen Unternehmens fragt nach Insolvenzgeld.
- Insolvenzverwalter prueft Anfechtungsansprueche gegen Zahlungen vor Verfahrenseroffnung.
- Mandant ist Mitglied des Glaeubigerausschusses und fragt nach Rechten, Pflichten und Haftung.

## Fachbegriffe (kurz erklaert)

- **Zahlungsunfaehigkeit** — Schuldner kann faellige Zahlungspflichten nicht mehr erfuellen; § 17 InsO; BGH-Schema: zehn Prozent Liquiditaetslucke für mindestens drei Wochen.
- **Drohende Zahlungsunfaehigkeit** — Schuldner wird voraussichtlich faellige Zahlungspflichten nicht erfuellen koennen; § 18 InsO; Grundlage für freiwilligen Antrag und StaRUG.
- **Ueberschuldung** — Vermoegen des Schuldners deckt bestehende Verbindlichkeiten nicht, sofern keine positive Fortbestehensprognose (§ 19 InsO).
- **Antragspflicht** — Geschaeftsfuehrer und Vorstand muessen bei Zahlungsunfaehigkeit oder Ueberschuldung ohne schuldhaftes Zoegern, spaetestens drei Wochen nach Eintreten, Antrag stellen (§ 15a InsO).
- **Zahlungsverbot** — Nach Insolvenzreife sind Zahlungen nur noch zulasaig, die mit der Sorgfalt eines ordentlichen Kaufmanns vereinbar sind (§ 15b InsO).
- **Insolvenzverschleppung** — Verspaetete Antragstellung; Haftung gegenueber Neuglaeubigeern und Altglaeubigern aus § 823 Abs. 2 BGB iVm § 15a InsO.
- **Bargeschaeft** — Leistungsaustausch mit sofortiger Gegenleistung; schuetzt vor Insolvenzanfechtung nach § 142 InsO.
- **Glaeubigerausschuss** — Kontrollorgan des Insolvenzverfahrens nach §§ 67 ff. InsO; prueft und beaufsichtigt den Insolvenzverwalter.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit als Eroeffnungsgrund.
- § 18 InsO — Drohende Zahlungsunfaehigkeit.
- § 19 InsO — Ueberschuldung; zweistufige Pruefung.
- § 14 InsO — Glaeubigerantrag.
- § 15a InsO — Antragspflicht des Geschaeftsleiters; Dreiwochenfrist.
- § 15b InsO — Zahlungsverbot nach Insolvenzreife.
- §§ 67 ff. InsO — Glaeubigerausschuss.
- §§ 129 ff. InsO — Insolvenzanfechtung (Grundtatbestand, Deckungsanfechtung, Vorsatzanfechtung).
- § 142 InsO — Bargeschaeftsprivileg.
- §§ 165 ff. SGB III — Insolvenzgeld für Arbeitnehmer.
- §§ 174 bis 179 InsO — Forderungsanmeldung, Pruefungstermin, Tabelle.
- §§ 269a bis 269i InsO — Konzerninsolvenz.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenrolle klaeren: Geschaeftsfuehrer, Glaeubiger, Arbeitnehmer, Ausschussmitglied?
2. Triage-Interview durchfuehren: Skill `mandat-triage-insolvenzrecht`.
3. Sofort-Fristen sichern: Dreiwochenfrist § 15a InsO oder Anmeldefrist § 165 SGB III?
4. Eroeffnungsgruende pruefen: `zahlungsunfaehigkeit-pruefung-17-inso` und/oder `ueberschuldung-pruefung-19-inso`.
5. Anschluss-Skill auswaehlen nach Ergebnis der Triage.

## Skill-Tour (was gibt es hier?)

**Einstieg und Triage**

- `mandat-triage-insolvenzrecht` — Eingangsabfrage; Mandantenrolle und Sofort-Fristen klaeren.
- `insolvenzrecht-kaltstart-interview` — Kaltstart-Interview für Plugin-Profil und Praxiskonfiguration.

**Eroeffnungsgruende und Liquiditaet**

- `zahlungsunfaehigkeit-pruefung-17-inso` — Liquiditaetsstatus nach § 17 InsO; BGH-Schema zehn Prozent und drei Wochen.
- `ueberschuldung-pruefung-19-inso` — Zweistufige Ueberschuldungspruefung nach § 19 InsO; Fortbestehensprognose und Liquidationswerte.
- `liquiditaetsvorschau-insolvenzrechtlich` — Rollierende Liquiditaetsvorschau nach IDW S 11; 13-Wochen- und 24-Monats-Vorschau.

**Antragspflicht und Haftung**

- `antragspflicht-15a-inso` — Antragspflicht nach § 15a InsO; Dreiwochenfrist; Zahlungsverbot § 15b InsO; Insolvenzverschleppungshaftung.
- `do-versicherung-manager-haftung` — D-and-O-Versicherungsdeckung bei Insolvenzhaftung; Claims-made-Prinzip; Ausschluesse.

**Glaeubigerantrag und Glaeubigerrechte**

- `glaeubigerantrag-pruefung` — Zulaessigkeit und Begruendetheit des Glaeubigerantrags nach § 14 InsO.
- `glaeubigerausschuss-mitwirkung` — Rechte, Pflichten und Haftung des Glaeubigerausschussmitglieds.
- `forderungsanmeldung-glaeubiger-174-177-inso` — Forderungsanmeldung, Fristen, Form, Rang, Pruefungstermin.

**Anfechtung**

- `anfechtungsrechte-pruefen` — Uebersicht aller InsO-Anfechtungstatbestaende §§ 129 ff. InsO; Betrag, Verteidigungslinien.
- `vorsatzanfechtung-133-inso` — Vorsatzanfechtung nach § 133 InsO; Fassung seit 5. April 2017; Bargeschaeftsprivileg.

**Sanierung und Sondersituationen**

- `uebertragende-sanierung-und-asset-deals` — Unternehmensverkauf aus der Insolvenz; Asset-Deal, Glaeubigerausschuss-Zustimmung.
- `konzerninsolvenz-koordination` — Koordination mehrerer Konzerngesellschaften nach §§ 269a bis 269i InsO.

**Arbeitnehmer**

- `insolvenzgeld-165-sgb-iii` — Insolvenzgeld für Arbeitnehmer; Voraussetzungen, Antragsfrist zwei Monate, Vorfinanzierung.

## Worauf besonders achten

- **Dreiwochenfrist laeuft ab Eintritt des Eroeffnungsgrundes** — Nicht ab Kenntnis des Geschaeftsfuehrers; bei unklarem Eintrittszeitpunkt ist das Risiko gross.
- **Zahlungsverbot schon vor Antragstellung** — § 15b InsO greift mit Eintritt der Insolvenzreife, nicht erst mit Eroffnung; Einzelzahlungen muessen ab diesem Zeitpunkt geprueft werden.
- **Glaeubigerantrag: Glaubhaftmachung reicht nicht immer** — § 14 InsO verlangt Nachweis der Forderung und des Eroeffnungsgrundes; bloss drohende ZU genuegt dem Glaeubiger nicht.
- **Anfechtungsreform 2017 beachten** — § 133 InsO wurde durch das AnfRefG 2017 grundlegend geaendert; Fristen und Indizien unterscheiden sich für Sachverhalte vor und nach dem 5. April 2017.
- **Insolvenzgeld: Zweimonatsfrist ab Insolvenz-Ereignis** — Arbeitnehmer verlieren den Anspruch, wenn Antrag zu spaet gestellt wird.

## Typische Fehler

- Geschaeftsfuehrer errechnet Dreiwochenfrist ab dem Tag, an dem er Kenntnis erlangt, statt ab Eintritt der Insolvenzreife.
- Glaeubiger stellt Antrag nach § 14 InsO ohne vollstreckbaren Titel und laeuft in Zulaessigkeitsproblem.
- Forderungsanmeldung versaeumt, weil Anmeldefrist nicht im Blick war; nachtraegliche Anmeldung nach § 177 InsO noch moeglich, aber mit Kostenrisiko.
- D-and-O-Versicherung wird nicht informiert, bevor Insolvenzantrag gestellt wird; Claims-made-Risiko.
- Koordinationsplan für Konzerninsolvenz wird nicht erwaogen, obwohl mehrere Schwestergesellschaften betroffen sind.

## Quellen und Aktualitaet

- Stand: 05/2026
- InsO in der geltenden Fassung (insb. §§ 15a und 15b InsO; §§ 129 und 133 InsO Fassung seit 5. April 2017)
- SGB III §§ 165 ff. in der geltenden Fassung
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeroefffnungsgruenden)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 266a StGB
- § 18 AktG
- § 64 GmbHG
- § 15 GmbHG
- § 40 GmbHG
- § 15 AktG
- Art. 17 DSGVO
- § 266 StGB
- § 3a EStG
- § 263 StGB
- § 94 StaRUG
- § 203 StGB

### Leitentscheidungen

- BGH IX ZR 122/23
- BGH IX ZR 129/22
- BFH II R 19/01
- BGH IV ZR 66/25
- BGH II ZR 206/22

---

## Skill: `antragspflicht-15a-inso`

_Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter wie Antragspflicht, Insolvenzverschleppung, 3-Wochen-Frist, Zahlungsverbot oder..._

# § 15a InsO — Antragspflicht, Insolvenzverschleppung und § 15b InsO Zahlungsverbot

## Arbeitsbereich

Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter wie "Antragspflicht", "Insolvenzverschleppung", "3-Wochen-Frist", "Zahlungsverbot" oder "§ 15a InsO" auftreten. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 15a InsO — Antragspflicht, Insolvenzverschleppung und § 15b InsO Zahlungsverbot` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Rechtsform der Gesellschaft (GmbH, AG, GmbH & Co. KG, etc.)
- Festgestellter oder streitiger Eröffnungsgrund (Zahlungsunfähigkeit, drohende
 Zahlungsunfähigkeit, Überschuldung) — ggf. Verweis auf Schwester-Skills
 § 17 InsO und § 19 InsO
- Zeitpunkt des Eintritts des Eröffnungsgrundes (tatsächlich oder vorgeworfen)
- Zeitpunkt der Antragstellung bzw. deren Unterlassen
- Vorhandensein von Sanierungsbemühungen (StaRUG, außergerichtliche Einigung,
 Sanierungsmoderation § 94 ff. StaRUG) und deren Dokumentationsstand
- Zahlungen nach Eintritt des Eröffnungsgrundes (Art, Betrag, Datum)
- D&O-Versicherungsschutz (soweit relevant)

## Rechtlicher Rahmen

### § 15a InsO — Gesetzliche Grundlage

**Abs. 1:** Mitglieder des Vertretungsorgans einer juristischen Person sind
verpflichtet, ohne schuldhaftes Zögern, spätestens aber innerhalb von drei
Wochen nach Eintritt der Zahlungsunfähigkeit oder sechs Wochen nach Eintritt
der Überschuldung, Insolvenzantrag zu stellen. Die verlängerte Sechswochenfrist
für Überschuldung wurde durch das Sanierungs- und Insolvenzrechtsfortentwick-
lungsgesetz (SanInsFoG) zum 01.01.2021 eingeführt (zuvor ebenfalls drei
Wochen). Beide Fristen sind **Höchstfristen**, kein "Recht zu warten": Der
Antrag ist zu stellen, sobald ein Eröffnungsgrund vorliegt und ernsthafte,
objektiv erfolgversprechende Sanierungsbemühungen nicht nachgewiesen werden
können.

**Abs. 2:** Bei führerloser Gesellschaft (kein organschaftlicher Vertreter mehr
bestellt) trifft die Antragspflicht jeden Gesellschafter (GmbH) bzw. jedes
Mitglied des Aufsichtsrats (AG).

**Abs. 3:** Antragspflicht gilt entsprechend für Gesellschaften ohne
Rechtspersönlichkeit (GmbH & Co. KG), wenn keine natürliche Person unbeschränkt
haftet.

**Abs. 4–6 — Strafbarkeit:**
- Abs. 4: Vorsätzliche Verletzung der Antragspflicht — Freiheitsstrafe bis zu
 drei Jahren oder Geldstrafe.
- Abs. 5: Fahrlässige Verletzung — Freiheitsstrafe bis zu einem Jahr oder
 Geldstrafe.
- Abs. 6: Strafbarkeitsmilderung bei nachgeholtem Antrag; Abs. 4 bleibt
 Offizialdelikt.

### § 15b InsO — Zahlungsverbot (seit SanInsFoG 01.01.2021)

§ 15b InsO hat die vormaligen gesellschaftsrechtlichen Regelungen
(§ 64 GmbHG a.F., § 92 Abs. 2 AktG a.F., § 130a HGB a.F.) in einer
einheitlichen Norm konsolidiert.

**Abs. 1 S. 1:** Nach Eintritt der Zahlungsunfähigkeit oder Überschuldung darf
der Geschäftsleiter keine Zahlungen mehr leisten, die mit der Sorgfalt eines
ordentlichen und gewissenhaften Geschäftsleiters unvereinbar sind.

**Abs. 1 S. 2 (Sorgfaltsausnahme):** Zahlungen, die mit der gebotenen Sorgfalt
vereinbar sind, bleiben zulässig. Hierzu zählen insbesondere betriebsnotwendige
Zahlungen zur Aufrechterhaltung der Betriebsbereitschaft (Löhne, Miete,
Energie) im Antragszeitraum, sofern realistisch Masse erhalten wird.

**Abs. 8:** Steuerzahlungen und Zahlungen an die Sozialversicherungsträger
können auch nach Eintritt der Insolvenzreife privilegiert sein, wenn die
Nichtleistung zur persönlichen Haftung des Geschäftsführers (§ 69 AO) führen
würde.

> Hinweis: Die Privilegierung des § 15b Abs. 8 InsO (Steuerzahlungen,
> Sozialversicherungsbeiträge) ist eng auszulegen und schützt nicht vor
> Erstattungsansprüchen des Insolvenzverwalters, wenn die Zahlungen die Masse
> schmälern und keine gleichwertige Gegenleistung erlangt wurde.
> Verifizierung der konkreten BGH-Linie erforderlich (dejure.org, openjur.de): keine Entscheidung aus Modellwissen zitieren; Gericht, Datum, Aktenzeichen, Randnummer vor Ausgabe prüfen.

### Kanonische und aktuelle Rechtsprechung (Stand Mai 2026)

**BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des
ausgeschiedenen Geschäftsführers. Der II. Zivilsenat hat entschieden, dass ein
nach § 823 Abs. 2 BGB iVm § 15a InsO haftender ausgeschiedener
Geschäftsführer grundsätzlich auch für Neugläubigerschäden einzustehen hat,
die erst nach seinem Ausscheiden entstehen, sofern die durch seine
Antragspflichtverletzung geschaffene Gefährdungslage zum
Schadensentstehungszeitpunkt fortbesteht. Bruch der Kausalkette nur bei
nachhaltiger Sanierung. Praxisfolge: Haftung endet nicht mit der Amtsniederlegung.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>

**BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung.
Der 5. Strafsenat hat den Kriterienkatalog der faktischen Geschäftsführung iSd
§ 283 StGB / § 15a InsO neu kalibriert. Auch Hintermänner im
Firmenbestatter-Modell können als Täter haften, wenn sie die tatsächliche
Geschäftsführung ausüben; das bloße Nicht-Auftreten nach außen schließt
Strafbarkeit nicht aus.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>

**BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung / Wissentlichkeitsausschluss.
Der IV. Zivilsenat hat klargestellt, dass der D&O-Versicherer für jeden
einzelnen verbotswidrigen Zahlungsvorgang gesondert darlegen und beweisen
muss, dass der Geschäftsleiter positive Kenntnis von der konkreten
Pflichtverletzung hatte. Die Verletzung der Insolvenzantragspflicht
(§ 15a InsO) indiziert nicht automatisch eine wissentliche Verletzung der
Masseerhaltungspflicht (§ 15b InsO); ein "Aufkoppeln" verschiedener
Pflichtverletzungen ist unzulässig.
Quelle: Bundesgerichtshof Pressemitteilung 2025; <https://www.noerr.com/de/insights/bgh-zum-do-versicherungsschutz-verletzung-der-insolvenzantragspflicht-durch-geschaftsleiter-indiziert-keine-wissentliche-verletzung-der-masseerhaltungspflicht>

> **Grundsätze (aus älterer BGH-Rspr., vor Ausgabe live verifizieren):**
> - § 15a InsO ist Schutzgesetz iSd § 823 Abs. 2 BGB. Neugläubiger können
> ihren vollen Vertrauensschaden ersetzt verlangen; Altgläubiger sind auf
> den Quotenschaden beschränkt.
> - Feststellung der Zahlungsunfähigkeit über Liquiditätsbilanz; die
> Dreiwochenfrist dient nur der Abgrenzung zur vorübergehenden
> Zahlungsstockung — keine "Schonfrist".
> - Der Geschäftsführer muss die wirtschaftliche Lage laufend im Blick
> behalten; fahrlässige Unkenntnis schützt nicht.
> Verifizierung erforderlich: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe Gericht, Entscheidungsform, Datum, Aktenzeichen und tragende Aussage über offizielle oder frei zugängliche Quelle (dejure.org, openjur.de, bundesgerichtshof.de) prüfen.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### IDW-Standard

**IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen),
Tz. 7 ff.:** Der Standard definiert den Prüfungsauftrag und das methodische
Vorgehen für die Feststellung von Zahlungsunfähigkeit und Überschuldung. Der
IDW S 11 ist Maßstab für die Beurteilung, ob und wann ein Eröffnungsgrund
objektiv vorlag — mit unmittelbarer Relevanz für die Bestimmung des
Fristbeginns nach § 15a Abs. 1 InsO. Tz. 8 ff. regeln den Stichtag der
Feststellung; Tz. 16 ff. die Fortbestehensprognose im Überschuldungskontext.

## Ablauf

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Feststellung des Eröffnungsgrundes**
 Zunächst ist zu klären, ob Zahlungsunfähigkeit (§ 17 InsO — s. Schwester-
 Skill) oder Überschuldung (§ 19 InsO — s. Schwester-Skill) vorliegt.
 Maßgeblicher Zeitpunkt ist der objektive Eintritt; für die Haftung genügt
 Kennenmüssen (fahrlässige Unkenntnis). IDW S 11 liefert den methodischen
 Rahmen.

2. **Beginn der Antragsfrist**
 Die Frist beginnt mit dem objektiven Eintritt des Eröffnungsgrundes,
 frühestens jedoch mit dem Zeitpunkt, in dem der Geschäftsleiter diesen
 kannte oder bei pflichtgemäßer Sorgfalt kennen musste (fahrlässige
 Unkenntnis schützt nicht). Dreiwochenfrist bei Zahlungsunfähigkeit,
 Sechswochenfrist bei Überschuldung (seit 01.01.2021, SanInsFoG).
 Konkrete BGH-Entscheidungen zur Erkennbarkeit der Insolvenzreife vor Ausgabe verifizieren (dejure.org, openjur.de).

3. **Sanierungsversuche dokumentieren**
 Sanierungsbemühungen können den Fristablauf nicht hemmen, senken aber das
 Verschulden und können im Einzelfall belegen, dass keine Pflicht­verletzung
 vorlag. Voraussetzung ist ein belastbares Sanierungskonzept mit konkreter
 Erfolgsaussicht. Geeignete Instrumente: außergerichtliche Einigung,
 Sanierungsmoderation (§§ 94 ff. StaRUG), vorläufiger Restrukturierungs­rahmen
 (§§ 29 ff. StaRUG). Jede Maßnahme ist schriftlich mit Datum, Beteiligten und
 Ergebnis zu dokumentieren (Vorstands-/Geschäftsführerprotokoll).

4. **Antragstellung spätestens mit Ablauf der Höchstfrist**
 Bei Zahlungsunfähigkeit: Antrag spätestens am 21. Tag nach Fristbeginn.
 Bei Überschuldung: spätestens am 42. Tag. Jeder Tag der Überschreitung
 verlängert den Haftungszeitraum. Fristversäumnis begründet zugleich
 Strafbarkeit nach § 15a Abs. 4 oder Abs. 5 InsO.

5. **Haftungsdokumentation Geschäftsführer**
 Für die Haftungsabwehr ist eine lückenlose Dokumentation erforderlich:
 Bilanzen, Liquiditätspläne, Beratungsmandate (Steuerberater, Sanierungsberater),
 Gesellschafter­beschlüsse, Korrespondenz mit Gläubigern und Kreditinstituten.
 Bei Beauftragung eines Insolvenzberaters: Mandat, Stellungnahme und zeitlicher
 Ablauf festhalten. Bestehende D&O-Versicherungspolice prüfen (Coverage,
 Selbstbehalt, Ausschlussklauseln für wissentliche Pflichtverletzungen).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Antragspflicht § 15a InsO pruefend und Beratungsschreiben erstellen | Beratungsschreiben nach Pruefschema; Template unten |
| Variante A — Insolvenzreife strittig Gutachten noetig | Sachverstaendigen-Gutachten zuerst; Beratungsschreiben nach Klaerunm |
| Variante B — Sanierung noch moeglich StaRUG als Alternative | StaRUG-Option parallel pruefen; Antrag nicht zwingend sofort |
| Variante C — Gesellschafter kennen Lage bereits Haftungsrisiko | Haftungs-Beratung separat; Antragspflicht und Haftung unterscheiden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Ausgabeformat

Ausgabe in strukturierter Prosa oder tabellarischer Form, jeweils bestehend aus:

- **Sachverhaltszusammenfassung:** Eröffnungsgrund, Datum des Eintritts,
 Fristbeginn und -ende (konkrete Daten).
- **Haftungsprüfung:** Pflicht­verletzung (ja/nein, Begründung), Verschulden
 (Vorsatz/Fahrlässigkeit), Schaden (Neugläubiger: Vertrauensschaden;
 Altgläubiger: Quotenschaden). Bei ausgeschiedenem GF: BGH II ZR 206/22
 prüfen (fortwirkende Gefährdungslage).
- **Zahlungsverbot-Prüfung (§ 15b InsO):** Verbotene Zahlungen mit Datum und
 Betrag; Ausnahmen (§ 15b Abs. 1 S. 2, Abs. 8).
- **Strafrechtliches Risiko:** § 15a Abs. 4 oder Abs. 5 InsO; bei faktischer
 Geschäftsführung BGH 5 StR 287/24 vom 27.02.2025 beachten.
- **Handlungsempfehlungen:** Nachholung des Antrags, Dokumentation,
 D&O-Deckungsprüfung (BGH IV ZR 66/25 vom 19.11.2025: positive Kenntnis pro
 Pflichtverletzung erforderlich).
- **Belege:** Mindestens zwei einschlägige BGH-Entscheidungen mit Randnummer
 aus offener Quelle (dejure.org, openjur.de, bundesgerichtshof.de), IDW S 11.

## Beispiel

**Sachverhalt:** Geschäftsführer Müller der Müller Handels-GmbH erkennt am
22.04.2026, dass die Gesellschaft dauerhaft zahlungsunfähig ist (§ 17 InsO).
Ein Insolvenzantrag wird erst am 02.06.2026 gestellt.

**Fristberechnung:**
- Fristbeginn: 22.04.2026 (Kenntnis des Eröffnungsgrundes)
- Höchstfrist (3 Wochen): **13.05.2026**
- Antragstellung: 02.06.2026 — **Überschreitung um 20 Tage**

**Haftungsfolgen:**

1. *Zivilrechtlich (§ 823 Abs. 2 BGB iVm § 15a InsO):*
 Neugläubiger, die zwischen dem 13.05.2026 und dem 02.06.2026 Vertragsbeziehungen
 mit der GmbH eingegangen sind, können ihren Vertrauensschaden (vollständiger
 Forderungsausfall abzüglich etwaiger Insolvenzquote) von Müller persönlich
 ersetzt verlangen. Altgläubiger können den Quotenschaden geltend machen.
 Sollte Müller vor dem 02.06.2026 ausscheiden, bleibt nach **BGH II ZR 206/22
 vom 23.07.2024** die Haftung für danach hinzutretende Neugläubigerschäden
 bestehen, solange die ursprünglich geschaffene Gefährdungslage fortbesteht.

2. *Zahlungsverbot (§ 15b InsO):*
 Zahlungen, die Müller nach dem 22.04.2026 veranlasst hat und die nicht unter
 § 15b Abs. 1 S. 2 oder Abs. 8 fallen, sind erstattungsfähig. Der
 Insolvenzverwalter kann Müller auf Rückzahlung in Anspruch nehmen.

3. *Strafrechtlich (§ 15a Abs. 4 InsO):*
 Bei nachgewiesenem Vorsatz (Müller kannte den Eröffnungsgrund seit 22.04.2026):
 Freiheitsstrafe bis zu drei Jahren oder Geldstrafe. Bei Fahrlässigkeit
 (§ 15a Abs. 5 InsO): Freiheitsstrafe bis zu einem Jahr oder Geldstrafe.

## Risiken und typische Fehler

**1. Fristbeginn bei "wusste oder musste wissen"**
Der Fristbeginn ist objektiv. Es genügt, dass der Geschäftsleiter bei
pflichtgemäßer Sorgfalt — d.h. bei Führung einer ordnungsgemäßen Buchhaltung
und zeitnäher Aufstellung von Liquiditätsplänen — den Eröffnungsgrund hätte
erkennen müssen. Berufung auf Unkenntnis infolge mangelhafter interner
Kontrolle schützt nicht. Konkrete BGH-Linie über offene Quellen verifizieren.

**2. Sanierungsverhandlungen hemmen den Fristlauf nicht automatisch**
Der bloße Umstand, dass Gespräche mit Gläubigern oder Banken laufen,
unterbricht die Antragsfrist nicht. Nur ein belastbares, realistisches
Sanierungskonzept mit konkreter Finanzierungszusage kann im Einzelfall das
Verschulden mindern. Fehlt das Konzept, bleibt die Frist unberührt.

**3. Faktischer Geschäftsführer ist antragspflichtig**
§ 15a InsO erfasst auch faktische Geschäftsführer, d.h. Personen, die ohne
formale Bestellung die typischen Aufgaben der Geschäftsleitung tatsächlich
ausüben — z.B. Strohmann-Konstellationen, Firmenbestatter-Modelle, oder
Gesellschafter, die die Geschäfte an sich gezogen haben.
**BGH 5 StR 287/24 vom 27.02.2025** hat die Kriterien neu kalibriert: Auch
Hintermänner ohne Außenauftritt können als faktische Geschäftsführer haften;
maßgeblich ist die tatsächliche Ausübung leitender Tätigkeit.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>

**4. D&O-Versicherung — Deckungslücken**
Typische Ausschlüsse in D&O-Policen: wissentliche Pflichtverletzung,
vorsätzliche Tatbegehung, unrichtige Zusicherungen.
**BGH IV ZR 66/25 vom 19.11.2025** hat die Position des versicherten
Geschäftsleiters gestärkt: Der D&O-Versicherer muss für jede einzelne
verbotswidrige Zahlung gesondert positive Kenntnis des Geschäftsleiters von
der konkreten Pflichtverletzung darlegen und beweisen. Die Verletzung der
Antragspflicht (§ 15a InsO) indiziert nicht automatisch eine wissentliche
Verletzung der Masseerhaltungspflicht (§ 15b InsO); ein "Aufkoppeln"
verschiedener Pflichtverletzungen ist unzulässig.
Frühzeitige Anzeige an den D&O-Versicherer und Einholung einer
Deckungsbestätigung sind weiterhin unverzichtbar.
Quelle: <https://www.noerr.com/de/insights/bgh-zum-do-versicherungsschutz-verletzung-der-insolvenzantragspflicht-durch-geschaftsleiter-indiziert-keine-wissentliche-verletzung-der-masseerhaltungspflicht> (Aktenzeichen über offene Quelle verifizieren)

**5. Versäumnis bei mehrköpfiger Geschäftsführung**
In einer GmbH mit mehreren Geschäftsführern ist jeder einzeln antragspflichtig;
die Pflicht ist nicht delegierbar. Der ressortfremde Geschäftsführer kann sich
nicht auf den Ressortzuschnitt berufen, sondern muss sich ein eigenes Bild von
der Vermögens- und Liquiditätslage verschaffen. Konkrete BGH-Entscheidung über
offene Quelle (dejure.org) verifizieren.

**6. § 15b InsO — Irrtum über zulässige Zahlungen**
Verbreiteter Fehler: Geschäftsleiter nehmen an, Gehaltszahlungen an sich selbst
oder Darlehensrückführungen an Gesellschafter seien stets zulässig. Nach Eintritt
der Insolvenzreife sind auch diese Zahlungen vom Verbot erfasst, sofern sie
nicht unter die Ausnahmen fallen.

## Quellenpflicht

Bei jeder Ausgabe zu diesem Skill sind mindestens folgende Belege anzugeben (offene Quelle, vor Ausgabe live prüfen):

- BGH II ZR 206/22 vom 23.07.2024 (Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden)
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- BGH 5 StR 287/24 vom 27.02.2025 (Faktischer Geschäftsführer / Firmenbestattung)
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- BGH IV ZR 66/25 vom 19.11.2025 (D&O-Versicherung; wissentliche Pflichtverletzung erfordert positive Kenntnis pro Pflichtverletzung)
 Bundesgerichtshof Pressemitteilung 2025 (Verifikation über bundesgerichtshof.de / dejure.org)
- Altere BGH-Linie zur Antragspflichthaftung (Schutzgesetz, Vertrauensschaden Neugläubiger, Quotenschaden Altgläubiger) und zur Feststellung der Zahlungsunfähigkeit (Liquiditätsbilanz, Aktiva II / Passiva II): vor Ausgabe Gericht, Datum, Aktenzeichen, Randnummer in offener Quelle prüfen.
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen), Tz. 7 ff.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.

---
*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*

## Triage — Antragspflicht § 15a InsO

Bevor losgelegt wird, klaere:

1. **Rechtsform?** § 15a InsO gilt für GmbH, AG, UG, GmbH & Co. KG; natuerliche Personen: keine Antragspflicht, nur Antragsrecht.
2. **Eröffnungsgrund?** ZU § 17 InsO: Frist 3 Wochen. Ueberschuldung § 19 InsO: Frist 6 Wochen. Frist-Uhr laeuft ab erstem Kenntnistag.
3. **Faktischer Geschäftsführer?** Auch ohne formale Bestellung haftet, wer die Geschäftsführung tatsächlich ausübt — neu kalibriert durch BGH 5 StR 287/24 vom 27.02.2025 (Firmenbestattung). Hintermänner ohne Außenauftritt nicht ausgeschlossen.
4. **Sanierungsversuch?** Antragspflicht wird durch echten Sanierungsversuch NICHT beseitigt; Frist laeuft weiter; Eigenantrag sichert Sanierungszeit.
5. **Zahlungen nach Insolvenzreife?** § 15b InsO: Zahlungen nach Insolvenzreife von GF persoenlich erstattten; Ausnahme nur Betriebskostenentgeltsatz ohne Massebeeintraechtigung.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template Beratungsschreiben Antragspflicht

**Adressat:** Geschaeftsfuehrung [FIRMA] — Tonfall: klar-warnend mit Handlungsempfehlung

```
VERTRAULICH — ANWALTLICHES SCHREIBEN
[KANZLEI]
[DATUM]

Betreff: Dringende Hinweis — Insolvenzantragspflicht § 15a InsO

Sehr geehrte/r Frau/Herr [NAME],

nach unserer heutigen Beratung weise ich Sie ausdruecklich darauf hin:

Es besteht [Zahlungsunfaehigkeit § 17 InsO / Ueberschuldung § 19 InsO].
Die Antragsfrist des § 15a Abs. 1 InsO laeuft am [DATUM] ab.

Bei Ueberschreitung dieser Frist drohen:
- Strafbarkeit nach § 15a Abs. 4 InsO (Freiheitsstrafe bis 3 Jahre)
- Persoenliche Haftung nach § 15b InsO für alle Zahlungen nach Insolvenzreife
- Schadensersatzhaftung gegenueber Glaeubigern

Ich empfehle die sofortige Stellung des Insolvenzantrags, idealerweise mit Antrag auf
[Eigenverwaltung / Schutzschirm / Regelverfahren].

Bitte bestaetigen Sie schriftlich, dass Sie diesen Hinweis erhalten haben.

[UNTERSCHRIFT ANWALT]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

<!-- AUDIT Mai 2026 — Update Bundle 034 —
 Update aufgenommen: BGH II ZR 206/22 (23.07.2024) fortwirkende Haftung ausgeschiedener GF,
 BGH 5 StR 287/24 (27.02.2025) faktischer GF,
 BGH IV ZR 66/25 (19.11.2025) D&O-Wissentlichkeit.
 Rechtsprechung weiterhin live prüfen: dejure.org, openjur.de, bundesgerichtshof.de.
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 266a StGB
- § 18 AktG
- § 64 GmbHG
- § 15 GmbHG
- § 40 GmbHG
- § 15 AktG
- Art. 17 DSGVO
- § 266 StGB
- § 3a EStG
- § 263 StGB
- § 94 StaRUG
- § 203 StGB

### Leitentscheidungen

- BGH IX ZR 122/23
- BGH IX ZR 129/22
- BFH II R 19/01
- BGH IV ZR 66/25
- BGH II ZR 206/22

---

## Skill: `do-versicherung-manager-haftung`

_Insolvenzverwalter verklagt Geschäftsführer und D&O-Versicherung soll Deckung prüfen oder Manager fragt nach Versicherungsschutz in der Krise. Prüfraster D&O-Versicherung Claims-made-Prinzip Schadensereignis vs. Anspruchserhebung. Insolvenz-spezifische Pflichten § 15a InsO Antragspflicht § 15b In..._

# D&O-Versicherung bei Manager-Haftung

## Arbeitsbereich

Insolvenzverwalter verklagt Geschäftsführer und D&O-Versicherung soll Deckung prüfen oder Manager fragt nach Versicherungsschutz in der Krise. Prüfraster D&O-Versicherung Claims-made-Prinzip Schadensereignis vs. Anspruchserhebung. Insolvenz-spezifische Pflichten § 15a InsO Antragspflicht § 15b InsO Zahlungsverbot. Deckungs-Ausschluesse wissentliche Pflichtverletzung Vorsatz Selbstbedienung. BGH-Linie zur Insolvenz-Anfechtung Praemien-Zahlung. Output D&O-Deckungs-Memo mit Versicherungs-Lage und Pflichten des Versicherten. Abgrenzung: antragspflicht-15a-inso für die Haftung selbst. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `D&O-Versicherung bei Manager-Haftung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- D&O-Versicherungs-Vertrag (Police AVB)
- Versicherungs-Summe und Selbstbehalt
- Aktueller Anspruch (Klage Geschäftsführer durch Insolvenz-Verwalter Gesellschaft)
- Schadenslimit Ranges
- Datum-Linien (Versicherungs-Schluss Wirksamkeits-Zeitraum Tat-Zeitpunkt Anspruchserhebung)
- Bisherige Schadensanzeigen

## Schritt 1 — Versicherungs-Verhältnis-Struktur

### Drei Beteiligte

- **Versicherer** (z.B. Allianz AGCS, Chubb, AIG, Munich Re)
- **Versicherungs-Nehmer** typisch Gesellschaft (zahlt Prämie)
- **Versicherter** Geschäftsführer Vorstand Aufsichtsrat individuell

### Vertrags-Konstruktion

- **Fremdversicherung** § 43 ff. VVG
- **Versicherter** erwirbt Anspruch aus Vertrag (Eigenrecht § 44 VVG)
- **Versicherungs-Nehmer** zahlt Prämie

### Bei Insolvenz Versicherungs-Nehmer

- **Vertrag bleibt bestehen** wenn Prämien gezahlt
- Konkrete BGH-Linie zum Verhältnis Insolvenzverwalter / D&O-Versicherer (Direktanspruch nach Abtretung) vor Ausgabe über dejure.org / openjur.de verifizieren.
- **Rückwirkungs-Risiken** prüfen

## Schritt 2 — Claims-made-Prinzip

### Definition

- **Versicherungs-Fall** = Anspruchserhebung in Versicherungs-Zeitraum
- Nicht: Tat-Zeitpunkt
- Anspruch muss **während Versicherungs-Zeit** erhoben werden

### Praktische Konsequenz

- Bei Tat 2022, Klage 2024 — Versicherung 2024 muss vorliegen
- Bei Tat 2022, Versicherung beendet 2023, Klage 2024 — keine Deckung (außer Nachhaftungs-Klausel)
- **Nachhaftungs-Klausel** typisch 3 Jahre, optional bis 5 oder 10 Jahre

### Run-Off-Versicherung

- Bei Geschäftsbeendigung
- Deckung für späte Anspruchserhebung
- Vor Insolvenz häufig sinnvoll

## Schritt 3 — Versicherungs-Fall-Definition

### Standard-Klausel

- Schriftliche Schadensanzeige des Anspruch-Erhebenden
- An Versicherten
- Versicherter informiert Versicherer

### Beispiele Schadensanzeigen

- Insolvenz-Verwalter-Klage § 15b InsO
- Gesellschafter-Beschluss-Klage § 46 GmbHG
- Klage aus § 43 GmbHG (Geschäftsführer-Sorgfalts-Pflichten)
- Strafanzeige mit Schadensersatz-Vorhalt

## Schritt 4 — Insolvenz-spezifische Haftung

### § 15a InsO Antragspflicht-Verletzung

- **Drei-Wochen-Frist** ab Zahlungs-Unfähigkeit / Überschuldung
- **Strafbarkeit** § 15a Abs. 4 InsO (Freiheits-Strafe bis drei Jahre)
- **Zivilrechtliche Haftung** über § 823 Abs. 2 BGB iVm § 15a InsO
- **Klage durch Insolvenz-Verwalter** als Gläubigern-Vermögens-Schädigung

### § 15b InsO Zahlungsverbot (alt § 64 GmbHG)

- **Zahlungen nach Eintritt** Zahlungs-Unfähigkeit / Überschuldung verboten
- **Haftung Erstattung** durch Geschäftsführer
- **Ausnahme** Zahlungen mit Sorgfalt eines ordentlichen Geschäftsmanns vereinbar (z.B. zur Vermeidung größerer Schäden)

### BGH-Rechtsprechung

- **BGH IV ZR 66/25 vom 19.11.2025** — Wissentlichkeitsausschluss in D&O-Bedingungen erfordert positive Kenntnis des Versicherten von der konkreten Pflichtverletzung. Verletzung der Insolvenzantragspflicht (§ 15a InsO) indiziert nicht automatisch wissentliche Verletzung der Masseerhaltungspflicht (§ 15b InsO). Der Versicherer muss für jede einzelne verbotswidrige Zahlung gesondert darlegen und beweisen; "Aufkoppeln" verschiedener Pflichtverletzungen ist unzulässig.
 Quelle: <https://www.noerr.com/de/insights/bgh-zum-do-versicherungsschutz-verletzung-der-insolvenzantragspflicht-durch-geschaftsleiter-indiziert-keine-wissentliche-verletzung-der-masseerhaltungspflicht> (Az.-Verifizierung über bundesgerichtshof.de)
- **BGH II ZR 206/22 vom 23.07.2024** — Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden bleibt bestehen, solange die durch ihn geschaffene Gefährdungslage fortwirkt. Auswirkung auf D&O-Deckung in der Nachhaftungsphase.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>

## Schritt 5 — Deckungs-Ausschlüsse

### Standard-Ausschlüsse

- **Wissentliche Pflichtverletzung** — selbst bewusst gesetzte Schädigung
- **Vorsatz** — direkt gewollt
- **Strafrechtliche Verurteilung** rechtskräftig
- **Bereicherungs-Bezug** persönlicher Vorteil

### Insolvenz-spezifische Ausschlüsse (möglich)

- **Vor-Versicherungs-Zeitraum-Taten** wenn schon bekannt
- **Insolvenz-Anmeldungs-Versäumnis** nach Versicherungs-Beginn
- **Insolvenz-Reife** zum Versicherungs-Beginn schon vorliegend

### Praktische Auslegung

- Nach **BGH IV ZR 66/25 vom 19.11.2025** trägt der Versicherer für jede einzelne verbotswidrige Zahlung gesondert die Darlegungs- und Beweislast für positive Kenntnis des Versicherten von der konkreten Pflichtverletzung.
- **Wissentliches Pflichtverletzungs-Risiko** häufig streitig
- **Beweis-Last Versicherer** für Ausschluss; ein "Aufkoppeln" zwischen Antragspflicht (§ 15a InsO) und Zahlungsverbot (§ 15b InsO) ist unzulässig.

## Schritt 6 — Versicherer-Pflichten

### Verteidigungs-Übernahme

- Anwalts-Bestellung Versicherer-seitig (oder Versicherter-Wahl)
- Anwalts-Kosten Versicherer
- Sachverständigen-Kosten

### Schadensregulierung

- Bei Anerkanntem Anspruch: Zahlung an Schaden-Geltendmacher
- Bei Vergleich: Versicherer-Zustimmung erforderlich

### Versicherungs-Summe

- Pro Schadensfall Maximalbetrag
- Höchst-Deckungs-Summe Jahres-Aggregat
- Selbstbehalt typisch EUR 5.000–50.000

## Schritt 7 — Versicherten-Pflichten

### Anzeigepflicht § 30 VVG

- **Unverzüglich** nach Kenntnis
- **Versicherer informieren** schriftlich
- **Bei Versäumnis** Leistungs-Freiheit Versicherer

### Mitwirkungs-Pflichten

- Sachverhalts-Information
- Unterlagen-Bereitstellung
- Verteidigungs-Strategie mit Versicherer abstimmen
- Anerkenntnis nur mit Versicherer-Zustimmung

### Bei Verstoß

- **Leistungs-Kürzung** oder -Verweigerung
- **§ 28 VVG** bei Obliegenheits-Verletzung
- Praktische Konsequenz: bei Selbst-Anerkenntnis ohne Versicherer Versicherer kann Deckung verweigern

## Schritt 8 — Strategische Aspekte

### Frühe Versicherer-Information

- Schon bei Erkennbarkeit von Streit-Konstellation
- Schon bei Eröffnungs-Verfahren Insolvenz
- Schon bei Vor-Klage-Aufforderung
- Manchmal sind Vor-Information-Pflichten in AVB

### Verteidigungs-Anwalts-Wahl

- Versicherer hat Vorschlags-Recht
- Versicherter hat in vielen AVB Wahl-Recht
- **Vertrauens-Anwalt** des Versicherten ratsam

### Vergleichs-Bereitschaft

- Versicherer regelmäßig Vergleichs-orientiert (Kosten-Optimierung)
- Versicherter sollte Vergleich nur mit Versicherer-Zustimmung
- **Eigen-Anteil**: Selbstbehalt + ggf. nicht-gedeckte Spitzen

## Schritt 9 — Bei mehreren Versicherern

### Versicherungs-Kette

- Primär-Versicherer (z.B. EUR 5 Mio)
- Excess-Versicherer (z.B. weitere EUR 10 Mio bei Aktivierung Primär)
- Pyramide häufig

### Schadens-Eskalation

- Primär bezahlt bis Limit
- Excess greift bei Über-Schreiten

### Koordination

- Primär-Versicherer typisch federführend
- Information aller Versicherer

## Schritt 10 — Versicherer-Anfechtung Prämien-Zahlung

### Insolvenz-Anfechtung § 130 ff. InsO

- Insolvenz-Verwalter kann Prämien-Zahlung anfechten
- Bei kongruenten Prämienzahlungen ist die Anfechtung nach **BGH IX ZR 129/22 vom 18.04.2024** restriktiv zu prüfen; konkrete Bedrohungslage und Erwartung dauerhafter Unterdeckung sind darzulegen.
- Versicherer als Anfechtungs-Adressat

### Folge

- Bei erfolgreicher Anfechtung — Prämie an Insolvenz-Masse
- Vertrag bleibt bestehen wenn rechtzeitige Zahlung andernfalls
- Versicherer kann Rückgriff auf Versicherten erwägen

## Schritt 11 — Anspruchs-Verteidigungs-Strategie

### Insolvenz-Verwalter-Klage Geschäftsführer

#### Materielle Verteidigung

- **Antragspflicht-Versäumnis** dartun warum nicht erkennbar (Liquiditäts-Prüfung sorgfältig erfolgt, IDW S 11 angewendet)
- **Zahlungen mit Sorgfalt** vereinbar (Skill `liquiditaetsvorschau-insolvenzrechtlich`)
- **Sanierungs-Bemühungen** dokumentieren
- **Sachverständigen-Gegen-Gutachten**

#### Prozessual

- **Antrag auf Streit-Verkündung** Versicherer § 72 ZPO
- **Beweisangebot** umfassend
- **Beweis-Erleichterung** für Geschäftsführer in Krise

### Eil-Schritte

- Versicherer informieren
- Anwalts-Vertretung organisieren
- Dokumentation Sicher-stellen (Buchhaltung Banken Verträge)
- Sachverhalts-Memo vorbereiten

## Schritt 11a — Deckungs-Konzepte Inside / Outside / Side-A

### Inside-Coverage (Side-B)

- **Eigenschäden der Gesellschaft** gegen Geschäftsführer / Vorstand
- Klassische Innen-Haftung: Gesellschaft klagt eigene Organe (§ 43 GmbHG, § 93 AktG)
- In Insolvenz: **Insolvenz-Verwalter als Vermögens-Verwalter** der Gesellschaft
- Häufigster Anwendungs-Fall: § 15b InsO Klage Insolvenz-Verwalter
- Versicherungs-Nehmer = Gesellschaft erhält Deckung für ihren eigenen Anspruch

### Outside-Coverage (Side-C bei AG / Side-B bei GmbH)

- **Dritt-Ansprüche** gegen Geschäftsführer / Vorstand
- Gläubiger Lieferanten Banken Arbeitnehmer Sozialversicherungs-Träger Finanzamt
- Klassische Außen-Haftung: § 823 Abs. 2 BGB iVm § 15a InsO
- Strafrechtlich-zivilrechtliche Mischfälle
- Bei börsen-notierten AGs: zusätzlich Kapitalanleger-Klagen (Entity-Coverage)

### Side-A-Coverage (persönlicher Schutz Organ)

- **Schutz des Organs persönlich** wenn Gesellschaft nicht entschädigt
- Praktisch relevant bei: **Insolvenz der Gesellschaft** weil Gesellschaft Selbstbehalt / Eigenanteil nicht mehr aufbringen kann
- Auch bei rechtlichem Entschädigungs-Verbot (z.B. wissentliche Pflichtverletzung Gesellschaft gegenüber)
- **Kein oder reduzierter Selbstbehalt** typisch
- **Separate Versicherungs-Summe** zusätzlich zur Haupt-Police möglich (Excess-Side-A)
- In Insolvenz-Konstellation entscheidend — Innen-Verhältnis Gesellschaft/Organ bricht weg

### Praktische Konsequenz für Insolvenz-Mandat

- Side-A-Klausel prüfen ob vorhanden
- Bei fehlender Side-A — persönliches Vermögens-Risiko Geschäftsführer hoch
- Bei vorhandener Side-A — Direkt-Anspruch des Organs gegen Versicherer auch in Insolvenz
- **Gesellschafter-Beschluss / Anstellungs-Vertrag** auf Entschädigungs-Klausel prüfen (Indemnification)

## Schritt 12 — Vertrags-Optimierung

### Bei aktueller Police-Erneuerung

- **Nachhaftung verlängern** auf 5+ Jahre
- **Wissentliche Pflichtverletzung** möglichst eng definiert
- **Versicherungs-Summe** ausreichend
- **Selbstbehalt** akzeptabel
- **Run-Off-Option** bei Bedarf

### Bei mehreren Geschäftsführern

- **Personen-Limit** pro Geschäftsführer
- **Side-A-Coverage** für persönliche Haftung wenn Gesellschaft nicht entschädigt

## Schritt 13 — Schriftverkehr-Bausteine

### Schadens-Anzeige an Versicherer

```
Sehr geehrte Damen und Herren,

hiermit zeige ich gemaess § 30 VVG den Eingang eines
Anspruchsschreibens an.

Versicherungs-Police-Nr.: [Nr]
Versicherter: [Name Geschaeftsfuehrer]
Versicherungs-Nehmer: [Gesellschaft]

Schadens-Anlass:
Klage des Insolvenzverwalters [Name] vom [Datum] auf
Schadensersatz gem. § 15b InsO in Hoehe von EUR [Betrag].

Anlagen:
- Klageschrift in Kopie
- Versicherungs-Police in Kopie

Ich bitte um:
1. Bestaetigung des Deckungs-Schutzes
2. Beauftragung des Verteidigungs-Anwalts
3. Mitteilung der weiteren Verfahrens-Schritte

Mit freundlichen Gruessen
```

### Bei Deckungs-Streit Klage gegen Versicherer

- Versicherungs-Recht Klage Wahl Versicherter zu LG/AG je nach Streitwert
- Verzugs-Zinsen
- Vorgerichtliche Anwaltskosten

## Verzahnung mit anderen Skills

- `antragspflicht-15a-inso` — Antragspflicht-Detail
- `liquiditaetsvorschau-insolvenzrechtlich` — Liquiditäts-Prüfung
- `mandat-triage-insolvenzrecht` — Krisen-Einstieg
- `anfechtungsrechte-pruefen` — Anfechtungs-Risiko Prämien
- `fortbestehensprognose-zusammenfuehren` — Sanierungs-Prüfung

## Ausgabe

- `do-pruefung-{az}.md` mit Police-Audit Deckungs-Prüfung Anspruch-Analyse
- Schadens-Anzeige-Schriftsatz
- Verteidigungs-Strategie
- Vergleichs-Optionen-Bewertung
- Versicherungs-Vertrags-Optimierungs-Empfehlung
- Frist im Fristenbuch (Klage-Antwort Versicherer-Anzeige)

## Quellen

- VVG §§ 30 43 44 28
- InsO §§ 15a 15b 130 131 142
- GmbHG §§ 43 46
- BGB § 823 Abs. 2
- ZPO § 72
- **BGH IV ZR 66/25 vom 19.11.2025** — Wissentlichkeitsausschluss / D&O bei verspätetem Insolvenzantrag (Verifikation über bundesgerichtshof.de / dejure.org)
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle.

## Ergaenzende Leitentscheidungen

- Konkrete BGH-Linie zur Direkthaftung des D&O-Versicherers gegenüber dem Insolvenzverwalter (Abtretung, Deckungsanspruch) sowie BGH IV ZR 360/15 (NJW 2017, 2466) zum versicherungsrechtlichen Trennungsprinzip vor Ausgabe über dejure.org/openjur.de verifizieren.

<!-- AUDIT 27.05.2026: BGH VI ZR 111/12 (NOT_FOUND auf dejure.org) entfernt und ersetzt durch BGH IV ZR 360/15, NJW 2017, 2466 (verifiziert auf dejure.org). -->

---

## Skill: `glaeubigerantrag-glaeubigerausschuss`

_Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowohl aus Gläubigerperspektive (Antragstellung) als auch aus Schuldnerperspektive (Abwehrstrategien). Lädt, wenn ein Mandant als Gläubiger einen Insolvenzantrag stellen will, wenn e..._

# Prüfung Gläubigerantrag nach § 14 InsO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Prüfung Gläubigerantrag nach § 14 InsO` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Gläubigerseite: Art und Höhe der Forderung, Titulierungsstand, bisherige
 Vollstreckungsversuche, vorhandene Nachweise zum Eröffnungsgrund
- Schuldnerseite: Aktuelle Zahlungslage, verfügbare Liquidität, Stellungnahme zur
 bestrittenen Forderung, Bereitschaft zur sofortigen Zahlung oder zur Vorlage
 eines Sanierungskonzepts
- Verfahrensstatus: Liegt bereits ein Eigenantrag vor? Sind andere Gläubigeranträge
 anhängig? Gibt es ein laufendes StaRUG-Verfahren?

## Rechtlicher Rahmen

### Gesetzliche Grundlagen

**§ 14 Abs. 1 S. 1 InsO** legt die drei kumulativen Voraussetzungen des
Gläubigerantrags fest:

1. **Rechtliches Interesse** an der Eröffnung des Insolvenzverfahrens
2. **Glaubhaftmachung der Forderung** (Bestand, Fälligkeit, Höhe)
3. **Glaubhaftmachung des Eröffnungsgrundes** (§§ 17–19 InsO)

**§ 14 Abs. 1 S. 2 InsO** schützt das Antragsrecht bei vorausgegangener
Befriedigung: Wurde der Gläubiger in den letzten sechs Monaten vor Antragstellung
befriedigt, bleibt seine Antragsbefugnis gleichwohl bestehen, wenn die Befriedigung
als Insolvenzanfechtung nach §§ 129 ff. InsO angreifbar wäre. Dies verhindert den
"Taktikzahlungseinwand" des Schuldners, der kurz vor Verfahrenseröffnung
Teilzahlungen leistet, um den antragstellenden Gläubiger zu beseitigen, ohne die
Insolvenzlage zu beheben.

**§ 13 InsO** regelt Form und Inhalt des Antrags; für Gläubigeranträge gelten
ergänzend die §§ 14 ff. InsO.

**§ 26 InsO**: Weist das Gericht den Antrag mangels Deckung der Verfahrenskosten
ab (Abweisung mangels Masse), erfolgt die Eintragung im Schuldnerverzeichnis
(§ 882b ZPO) — eine eigenständige wirtschaftliche Sanktion.

**§ 56a InsO** gewährt dem Schuldner ein Vorschlagsrecht für den
Insolvenzverwalter, wenn er selbst Insolvenzantrag stellt. Dieses Recht entfällt
beim reinen Gläubigerantrag.

**§§ 17, 18, 19 InsO** definieren die antragsrelevanten Eröffnungsgründe:
Zahlungsunfähigkeit (§ 17), drohende Zahlungsunfähigkeit (§ 18, nur für
Schuldner-Eigenantrag) und Überschuldung (§ 19, juristische Personen).

### Rechtsprechung (Maßstab; Aktenzeichen vor Ausgabe über dejure.org / openjur.de verifizieren)

**Anforderungen an Glaubhaftmachung Forderung § 14 InsO:** Gläubiger muss Tatsachen darlegen, aus denen die überwiegende Wahrscheinlichkeit des Bestehens der Forderung folgt; vollständige Beweisführung nicht erforderlich. Zulässige Mittel: eidesstattliche Versicherung (§ 294 ZPO), Titel, Mahnbescheid, Kontoauszüge, Rechnungen mit Empfangsbestätigung.

**Indizien für Zahlungsunfähigkeit § 17 InsO:** fruchtlose Pfändungsversuche, Rückgabe von Lastschriften, Wechselproteste, Häufung von Mahnverfahren, Lohnsteuer- und SV-Rückstände, BWA mit negativem Saldo. Die Indizien dienen der Glaubhaftmachung der überwiegenden Wahrscheinlichkeit der ZU.

**Streitige Forderung:** Antrag zulässig, wenn nach § 294 ZPO glaubhaft gemacht; bloßes Bestreiten des Schuldners ohne substantiierten Gegenvortrag beseitigt die Glaubhaftmachung nicht.

**Missbräuchlicher Druckantrag:** Antrag, der allein der wirtschaftlichen Druckausübung dient, ist unzulässig; das rechtliche Interesse an der Eröffnung muss zur gerichtlichen Entscheidung noch bestehen.

Für aktuelle BGH-Linie zu allen vorgenannten Punkten Datum, Aktenzeichen und Randnummer vor Ausgabe über offene Quellen verifizieren.

### Quellen (nur verifiziert)

- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
 Antragsberechtigung, Glaubhaftmachung, Forderungserfordernis und Missbrauch)
- Hölzle, in: K. Schmidt, InsO, 20. Aufl. 2023, § 14 Rn. 1–55 (Dogmatik des
 rechtlichen Interesses, Zulässigkeit bei titulierter und nicht-titulierter
 Forderung, § 14 Abs. 1 S. 2 InsO)
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
 Indizienbeweis, Glaubhaftmachungsstandard im Gläubigerantrag)

### IDW S 11

Der **IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen,
Stand 2017)** liefert das fachliche Rüstzeug zur Feststellung der
Zahlungsunfähigkeit (Liquiditätsstatus, 10 %/3-Wochen-Grundsatz) und der
Überschuldung (Fortbestehensprognose + Überschuldungsstatus). Im Gläubigerantrag
ist IDW S 11 relevant, wenn ein Gutachter zur Glaubhaftmachung des Eröffnungsgrundes
beauftragt wird oder das Gericht einen vorläufigen Sachverständigen bestellt.

## Ablauf

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1 — Gläubigerprüfung: Forderung

- **Titulierungsstand**: Liegt ein vollstreckbarer Titel vor (Urteil, Beschluss,
 Vollstreckungsbescheid)? Wenn ja, entfällt das Glaubhaftmachungsproblem für
 die Forderung weitgehend.
- **Nicht-titulierte Forderung**: Belege zusammenstellen — Rechnung, Lieferschein,
 Empfangsbestätigung, Kontoauszug, eidesstattliche Versicherung nach § 294 ZPO.
- **Fälligkeit**: Die Forderung muss im Zeitpunkt der Antragstellung bestehen und
 fällig sein. Eine bedingte oder gestundete Forderung genügt grundsätzlich nicht
 (Ausnahme: Stundung durch Druckausübung, Sittenwidrigkeit der Stundung).
- **Höhe**: Für das rechtliche Interesse keine gesetzliche Mindestgrenze; jedoch
 prüft das Gericht implizit, ob die Forderungshöhe im Verhältnis zur
 Verfahrenserwartung steht. Bagatellbeträge können das rechtliche Interesse in
 Frage stellen.

### Schritt 2 — Glaubhaftmachung des Eröffnungsgrundes

Aufbau eines Indizienpakets für Zahlungsunfähigkeit (§ 17 InsO):

| Indiz | Beweismittel |
|---|---|
| Fruchtlose Pfändungsversuche | Pfändungsprotokoll des GV (nicht älter als 3 Monate) |
| Lastschriftrückgaben | Kontoauszüge des Gläubigers (Stichwort "nicht eingelöst") |
| Wechselproteste | Notarprotokoll |
| SV-Rückstand ≥ 3 Monate | Kontoauszug Krankenkasse, Rückstandsbescheinigung |
| Lohnsteuerrückstände | ELSTER-Mahnbescheide, Rückstandsmitteilung FA |
| Negative BWA | Betriebswirtschaftliche Auswertung mit kumuliertem Negativsaldo |
| Häufung von Mahnverfahren | SCHUFA-Auskunft, Registerauskunft gerichtlicher Mahnbescheide |

Mindestens zwei bis drei dieser Indizien sollten kombiniert werden, um die Gesamtschau der überwiegenden Wahrscheinlichkeit der Zahlungsunfähigkeit zu tragen (st. BGH-Rspr.; konkrete Aktenzeichen vor Ausgabe über offene Quellen verifizieren).

### Schritt 3 — Antragsschrift formal (§§ 13, 14 InsO)

Zwingender Inhalt:
- Bezeichnung Gläubiger (vollständiger Name/Firma, Anschrift)
- Bezeichnung Schuldner (Firma, Sitz, Registergericht/HRB-Nr.)
- Darlegung des rechtlichen Interesses
- Darlegung und Glaubhaftmachung der Forderung mit Belegen
- Darlegung und Glaubhaftmachung des Eröffnungsgrundes mit Indizienbelegen
- Antrag auf Anordnung vorläufiger Sicherungsmaßnahmen (§§ 21, 22 InsO),
 falls eilbedürftig (z. B. drohende Vermögensverschiebungen)
- Kostenvorschuss (§ 26 InsO; wird bei Behörden oft erlassen)

### Schritt 4 — Reaktion auf Anhörung des Schuldners (§ 14 Abs. 2 InsO)

Das Insolvenzgericht hört den Schuldner vor der Entscheidung an. Typische
Schuldnerreaktionen und die rechtliche Bewertung:

- **Bestreiten der Forderung**: Substantiiertes Bestreiten hemmt nicht automatisch das Verfahren; bei titulierter oder durch starke Indizien glaubhaft gemachter Forderung bleibt der Antrag zulässig (vgl. BGH-Linie; Az. vor Ausgabe verifizieren).
- **Sofortige Zahlung der titulierten Forderung**: Beseitigt das rechtliche
 Interesse grundsätzlich, außer § 14 Abs. 1 S. 2 InsO greift (Zahlung innerhalb
 von 6 Monaten als potenzielle Anfechtungszahlung).
- **Zahlungsplan/Ratenzahlungsvereinbarung**: Kein Anspruch des Schuldners auf
 Aussetzung; missbräuchlicher Druckantrag-Einwand bei kurzfristiger Rücknahme nach Einlenken (Az. vor Ausgabe verifizieren).
- **Einreichung Sanierungskonzept**: Kein verfahrensrechtlicher Aufschubgrund;
 jedoch kann das Gericht faktisch zögern, wenn ein plausibles Sanierungskonzept
 vorgelegt wird.

### Schritt 5 — Schutzschrift / Einstweiliger Rechtsschutz (Schuldnerseite)

- **Schutzschrift**: Vor oder unmittelbar nach Anhörung beim Insolvenzgericht
 hinterlegen; Inhalt: Bestreiten der Forderung mit Belegen, Bestreiten des
 Eröffnungsgrundes (aktuelle Liquiditätsübersicht, ggf. IDW S 11-Stellungnahme),
 Druckantrag-Einwand falls zutreffend.
- **StaRUG-Verfahren**: Einleitung eines Restrukturierungsverfahrens nach StaRUG
 kann faktisch den Insolvenzantrag überlagern; Anzeige der Restrukturierungssache
 hat keine automatische Sperrwirkung gegen Gläubigeranträge, kann aber gerichtlich
 koordiniert werden.
- **Eigenantrag des Schuldners**: Strategisch oft günstiger als Abwehr — der
 Schuldner erhält das Vorschlagsrecht für den Insolvenzverwalter (§ 56a InsO),
 kann Eigenverwaltung beantragen (§§ 270 ff. InsO) und behält größeren Einfluss
 auf das Verfahren, als wenn der Gläubigerantrag zur Eröffnung führt.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Glaeubiger-Insolvenzantrag pruefend und Kurzgutachten erstellen | Kurzgutachten nach Pruefschema; Template unten |
| Variante A — Forderung noch nicht tituliert Antrag riskant | Titulierung zuerst; Insolvenzantrag nach Urteil oder Vollstreckungstitel |
| Variante B — Schuldner bietet Zahlung an wenn Antrag zurueckgenommen | Rücknahme-Verhandlung pruefen; wirtschaftliches Ergebnis beachten |
| Variante C — Mehrere Glaeubiger koordinierter Antrag moeglich | Koordinierter Sammelantrag pruefen; Hauptglaeubiger bestimmen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Beispiel

**Sachverhalt:**
Das Finanzamt München stellt beim AG München — Insolvenzgericht — einen
Gläubigerantrag gegen die Muster GmbH (HRB 123456 AG München). Rückständig:
57.000 EUR Lohnsteuer (Zeitraum Jan–Jun 2024) + 30.000 EUR Umsatzsteuer
(Q1 und Q2 2024) = 87.000 EUR gesamt. Bisherige Vollstreckungsmaßnahmen:
drei Pfändungsversuche des Vollziehungsbeamten, alle fruchtlos (Protokolle
vom 15.04., 03.06. und 18.07.2024). Zusätzlich: Mahnbescheid wegen USt
rechtskräftig seit 12.03.2024; BWA-Auszüge April–Juni 2024 zeigen
kumulierten negativen Cash-flow von −38.000 EUR.

**Prüfung:**

*Zulässigkeit:*
- Rechtliches Interesse (+): Das Finanzamt ist öffentlich-rechtlicher Gläubiger;
 sein Interesse an der Verfahrenseröffnung folgt aus der Insolvenzquotenchance
 und der Anfechtungsmöglichkeit nach §§ 129 ff. InsO für zurückliegende Zahlungen.
 Behördengläubiger, insbesondere Finanzämter und Sozialversicherungsträger, stellen
 häufig Gläubigeranträge; im FA-Bereich oft im Zusammenhang mit einer
 Strafanzeige nach § 266a StGB (Vorenthalten von SV-Beiträgen), was das
 behördliche Interesse weiter objektiviert.
- Forderung glaubhaft gemacht (+): Rechtskräftiger Mahnbescheid für USt-Forderung;
 Steuerbescheide für LSt-Rückstände; Höhe belegbar durch Steuerkonto-Auszug.
- Fälligkeit (+): Steuerliche Fälligkeit nach § 41a EStG (LSt) und § 18 UStG (USt)
 jeweils eingetreten und unstreitig.

*Begründetheit:*
Eröffnungsgrund § 17 InsO durch Indizienkombination glaubhaft gemacht (st. BGH-Linie; Az. vor Ausgabe verifizieren):
- Drei fruchtlose Pfändungsversuche (schwergewichtiges Indiz)
- Negative kumulierte BWA (strukturelle Unterdeckung)
- 6-monatiger Lohnsteuerausfall (laufende Zahlungsunfähigkeit gegenüber FA)
- Rechtskräftiger Mahnbescheid ohne Zahlung (fehlende Zahlungsbereitschaft/-fähigkeit)

**Ergebnis:** Antrag zulässig und begründet; Eröffnung nach § 27 InsO zu erwarten.

## Risiken und typische Fehler

### Gläubigerseite

1. **Unzureichende Glaubhaftmachung der Forderung**: Bloße Behauptung ohne Belege
 genügt nicht; eidesstattliche Versicherung allein bei nicht-titulierter Forderung
 führt regelmäßig zur Unzulässigkeit (st. BGH-Linie; Az. vor Ausgabe verifizieren).

2. **Fehlende Aktualität der Indizienmittel**: Pfändungsprotokolle älter als drei
 bis vier Monate verlieren an Überzeugungskraft; aktuellere Beweismittel sind
 nachzuliefern.

3. **Missbräuchlicher Druckantrag**: Ein Antrag, der erkennbar nur zur
 Druckausübung gestellt und nach Zahlung sofort zurückgenommen wird, kann als
 rechtsmissbräuchlich eingestuft werden und Schadensersatzansprüche des
 Schuldners auslösen (Az. der einschlägigen BGH-Entscheidungen vor Ausgabe über
 offene Quellen verifizieren). Prüfen: hat der Mandant ein echtes
 Eröffnungsinteresse oder nur ein Zahlungsinteresse?

4. **§ 14 Abs. 1 S. 2 InsO — Taktikzahlung übersehen**: Befriedigt der Schuldner
 den antragstellenden Gläubiger kurz nach Antragstellung innerhalb der
 6-Monatsfrist, bleibt das Antragsrecht bestehen, wenn die Zahlung
 anfechtbar ist. Gläubiger darf Antrag bei anfechtbarer Befriedigung
 aufrechterhalten.

### Schuldnerseite

5. **Sofortige Zahlung als Anfechtungsrisiko**: Zahlt der Schuldner die
 antragsbegründende Forderung kurzfristig, um den Antrag zu Fall zu bringen,
 ist diese Zahlung nach § 133 Abs. 1 InsO (Vorsatzanfechtung) oder § 131 InsO
 (inkongruente Deckung) anfechtbar, wenn innerhalb der Anfechtungsfristen
 Insolvenz eröffnet wird. Der Schuldner "kauft" sich damit nur Zeit, ohne die
 Insolvenzlage zu beseitigen.

6. **Eigeninteresse vs. Gemeininteresse**: Der Gläubigerantrag dient nicht nur
 dem individuellen Gläubigerinteresse, sondern dem Schutz der
 Gläubigergesamtheit. Dies schränkt die Missbrauchsrechtsprechung auf klare
 Einzelfälle ein; der bloße Verdacht missbräuchlicher Motive genügt nicht.

7. **Zu späte Eigenantragsstellung**: Wartet der Schuldner zu lang mit dem
 Eigenantrag, verliert er das Vorschlagsrecht nach § 56a InsO und riskiert
 zudem eine persönliche Haftung der Geschäftsführer nach § 15a InsO
 (Insolvenzverschleppungshaftung).

8. **StaRUG-Verfahren ohne Sperrwirkung**: Das StaRUG-Restrukturierungsverfahren
 sperrt Gläubigeranträge nicht automatisch. Ohne gerichtliche Anordnung nach
 § 29 Abs. 2 Nr. 1 StaRUG bleibt der Gläubigerantrag vollständig wirksam.

## Quellenpflicht

Jede Handlungsempfehlung ist mit mindestens einer der nachstehenden Quellen
zu belegen. Pinpoint-Angaben (Randnummer) sind Pflicht.

| Quelle | Fundstelle |
|---|---|
| BGH IX. Zivilsenat zur Glaubhaftmachung der Forderung iSd § 14 InsO | Az., Datum, Randnummer vor Ausgabe über dejure.org / openjur.de verifizieren |
| BGH IX. Zivilsenat zur Indizienlinie der Zahlungseinstellung § 17 Abs. 2 S. 2 InsO | Az. vor Ausgabe verifizieren |
| BGH IX. Zivilsenat zum missbräuchlichen Druckantrag und rechtlichen Interesse | Az. vor Ausgabe verifizieren |
| Literatur (Kommentare, Handbücher) | nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle |
| IDW S 11 (Stand 2017) | Tz. 15–42 (Zahlungsunfähigkeit), Tz. 43–71 (Überschuldung) |

---

*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*

## Triage — Glaeubigerantrag

Bevor losgelegt wird, klaere:

1. **Forderung vollstreckbar?** Titel oder Glaubhaftmachung § 14 Abs. 1 InsO; eidesstattliche Versicherung ausreichend.
2. **Eröffnungsgrund glaubhaft?** Mindestens 2-3 Indizien für Zahlungsunfähigkeit iSd § 17 Abs. 2 S. 2 InsO oder Überschuldungsstatus iSd § 19 InsO.
3. **Rechtliches Interesse aktuell?** Kein missbräuchlicher Druckantrag; echtes Eröffnungsinteresse zum Zeitpunkt der gerichtlichen Entscheidung erforderlich.
4. **Sicherungsantrag § 21 InsO?** Sofort-Massnahmen bei Vermoegensgefaehrdung beantragen?
5. **Kostenvorschuss § 26 InsO?** Glaeubigerinteresse an Verfahren trotz Massearmut?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template Kurzgutachten Glaeubigerantrag

**Adressat:** Mandant (Glaeubiger) — Tonfall: sachlich-empfehlend

```
INTERNES GUTACHTEN — GLAEUBIGERANTRAG § 14 InsO
Datum: [DATUM] Mandant: [GLAEUBIGER] Schuldner: [SCHULDNER]

ERGEBNIS: Glaeubigerantrag [SINNVOLL / NICHT SINNVOLL]

BEGRUENDUNG:
Forderung: EUR [BETRAG], Faelligkeit [DATUM], Vollstreckbarkeit [JA/NEIN]
ZU-Nachweis: [Indizien aufzaehlen]
Rechtsschutzbeduernis: [Beurteilung]
Sicherungsantrag § 21 InsO: [EMPFOHLEN weil ...]
Kostenvorschuss: EUR [BETRAG] ggf. erforderlich (§ 26 InsO)

NAECHSTER SCHRITT: [Antrag einreichen bis DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

---

## Skill: `glaeubigerausschuss-mitwirkung`

_Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorläufiger Gläubigerausschuss § 22a InsO Schwellenwerte. Aufgaben Überwachung Insolvenzverwalter Beschlussfassung we..._

# Gläubigerausschuss-Mitwirkung

## Arbeitsbereich

Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorläufiger Gläubigerausschuss § 22a InsO Schwellenwerte. Aufgaben Überwachung Insolvenzverwalter Beschlussfassung wesentliche Verwertungs-Entscheidungen Verguetungsprüfung. Rechte Akteneinsicht Anhörung Beschlussantrag Kassen-Prüfung Haftung § 71 InsO. Output Ausschuss-Arbeitsmemo mit Checkliste laufender Pflichten und Risiko-Hinweisen. Abgrenzung: gläubigerantrag-prüfung für Eroefffnungsantrag des Gläubiger. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gläubigerausschuss-Mitwirkung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schritt 1 — Bestellung

### Endgültiger Gläubigerausschuss § 67 InsO

- **Bestellung durch Gläubigerversammlung** im Berichtstermin
- **Mitglieder** Vertreter unterschiedlicher Gläubiger-Gruppen (gesicherte/ungesicherte Gläubiger Arbeitnehmer Lieferanten Finanzamt)
- **Zahl** typisch drei bis sieben

### Vorläufiger Gläubigerausschuss § 22a InsO

- **Schon im Eröffnungsverfahren** durch Insolvenzgericht bestellt
- Pflicht bei größeren Unternehmen
 - **§ 22a Abs. 1 InsO** Bilanzsumme mehr als sechs Millionen Euro
 - oder Umsatz mehr als zwölf Millionen Euro
 - oder Mitarbeiter mehr als fünfzig
- **Antrag** beim Insolvenzgericht möglich
- **Eilbestellung** bei Eröffnungsantrag

### Mitgliederschaft

- Bereitschafts-Erklärung
- Gläubiger-Eigenschaft

## Schritt 2 — Aufgaben

### Überwachung Insolvenzverwalter § 69 InsO

- **Kassenprüfung** Aufzeichnungen Belege
- **Quartalsbericht** Verwalter
- **Berichts-Verlangen**

### Beschlussfassung über wichtige Verwalter-Entscheidungen

- **Veräußerung wesentlicher Vermögensgegenstände** § 160 Abs. 2 InsO
- **Stilllegung** Geschäftsbetrieb
- **Aufnahme oder Fortführung** wesentlicher Vertrags-Beziehungen
- **Personalmaßnahmen** in größeren Konstellationen
- **Vergleiche** mit größerem Volumen

### Vergütungsprüfung § 73 Abs. 1 InsO

- Verwalter-Vergütungs-Antrag nach InsVV
- Stellungnahme an Insolvenzgericht

### Gläubiger-Interessen-Vertretung

- Im Berichts-Termin
- In Gläubigerversammlung

## Schritt 3 — Rechte

### Akteneinsicht

- Vollumfänglich in Insolvenz-Akten
- Verwalter-Akten

### Anhörung

- Vor wesentlichen Beschlüssen
- Bei Verfügung über wesentliche Vermögensgegenstände

### Beschlussantrag

- Im Gläubigerausschuss
- An Gericht

### Verwalter-Abberufung

- Antrag bei wichtigem Grund § 59 InsO

## Schritt 4 — Pflichten und Haftung § 71 InsO

### Gewissenhafte Aufgabenwahrnehmung

- **Sorgfalt eines ordentlichen Geschäftsmanns**
- **Treuepflicht** gegenüber Gläubiger-Gesamtheit
- **Verschwiegenheits-Pflicht** gegenüber Dritten

### Haftung

- **Gegenüber Gläubigern und Insolvenzmasse**
- **Bei Pflichtverletzung** Schadensersatz
- **Mehrere Mitglieder** gesamtschuldnerisch

### D&O-Versicherung

- Häufig vom Mandanten als Mitglied vorgesehen
- Bei großen Unternehmen Standard

## Schritt 5 — Vergütung Mitglieder § 73 Abs. 1 InsO

- **Angemessene Vergütung** nach InsVV
- **Auslagen-Ersatz**
- Aus Insolvenzmasse

## Schritt 6 — Beschluss-Verfahren

### Beschlussfähigkeit

- Mehrheit der Mitglieder anwesend / vertreten

### Beschluss

- **Einfache Mehrheit** der Anwesenden
- Bei Stimmen-Gleichheit Stimme des Vorsitzenden

### Protokoll

- Schriftlich
- Bei wichtigen Beschlüssen Begründung

## Schritt 7 — Strategische Aspekte für Mitglied

### Aktive Mitwirkung

- **Regelmäßige Berichts-Anforderung** Verwalter
- **Kassen-Prüfung** alle drei bis sechs Monate
- **Beteiligung an wichtigen Entscheidungen**
- **Frage-Stellung**

### Konflikt mit Verwalter

- Bei Pflichtverletzung Antrag Abberufung
- Bei Schadensersatz-Ansprüchen Geltendmachung Gläubigerversammlung

### Konflikt im Gläubigerausschuss

- Bei systematischen Konflikten Rücktritts-Erklärung
- Ggf. neue Bestellung durch Gläubigerversammlung

## Schritt 8 — Spezielle Konstellationen

### Eigenverwaltung § 270 ff. InsO

- Gläubigerausschuss mit erhöhter Bedeutung
- Sachwalter überwacht
- Bei Schutzschirm § 270d InsO

### Konzern-Insolvenz § 269a ff. InsO

- Konzern-Gläubigerausschuss-Optionen
- Koordination

### StaRUG-Verfahren

- **Restrukturierungs-Beauftragter** statt Insolvenzverwalter
- **Restrukturierungs-Plan-Abstimmung** durch Gläubiger-Gruppen
- Andere Logik als InsO

## Schritt 9 — Berichtstermin § 156 InsO

- **Verwalter berichtet** über Vermögens-Stand, mögliche Sanierungs-Wege
- **Gläubiger entscheidet** über Fortführung Stilllegung
- **Gläubigerausschuss** vor entscheidet vor Versammlung

## Schritt 10 — Prüfungs-Termin § 175 InsO

- **Forderungs-Tabellen-Prüfung**
- **Bestreitungen** der Verwalter
- **Klageweg** für streitige Forderungen § 179 InsO

## Schritt 11 — Wahrnehmung als Anwalt für Mitglied

- **Vorbereitungs-Briefing** mit Mandant vor Sitzung
- **Aktenstudium** Verwalter-Bericht
- **Beschluss-Empfehlung** schriftlich
- **Bei Sitzung-Anwesenheit** Stimm-Vorbereitung

## Schritt 12 — Sonderpflichten Vorsitzende

- **Einladung** zur Sitzung
- **Tages-Ordnung** vorbereiten
- **Protokoll-Verantwortung**
- **Außenvertretung** des Ausschusses

## Checkliste vor Sitzung

- Sitzungs-Termin
- Tages-Ordnung
- Verwalter-Berichte gelesen
- Sachverhalts-Komplex verstanden
- Argumentations-Linie vorbereitet
- Beschluss-Vorschlag formuliert
- Stellvertreter bei Verhinderung

## Ausgabe

- `glaeubigerausschuss-mitwirkung-{az}.md`
- Sitzungs-Vorbereitungs-Memo
- Beschluss-Vorschlag-Entwurf
- Frist im Fristenbuch (Sitzungs-Termine)
- Bei Konflikt: Strategie-Memo

## Quellen

- InsO §§ 22a 59 67–73 156 160 175 270 270d
- StaRUG
- InsVV
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- HK-InsO

## Aktuelle Leitentscheidungen — Glaeubigerausschuss (Stand Mai 2026)

- Konkrete BGH/LG-Linien zu Haftung und Pflichten des Gläubigerausschusses (§§ 67–73, 160 InsO), insbesondere zur Mitwirkung bei bedeutenden Massnahmen, vor Ausgabe über dejure.org / openjur.de mit Datum und Aktenzeichen verifizieren.
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Bei AG-Insolvenzen mit großem Aktionärsanteil: Aktionärsforderungen sind nachrangig; Auswirkungen auf Stimmrechtsausübung und Ausschussbesetzung beachten.

## Paragrafenkette Glaeubigerausschuss

§ 67 InsO (Einsetzung) → § 68 InsO (Mitglieder) → § 69 InsO (Pflichten und Rechte) → § 70 InsO (Entlassung) → § 71 InsO (Haftung) → § 72 InsO (Verguetung) → § 73 InsO (Verguetung) → § 160 InsO (besonders bedeutsame Rechtshandlungen)

## Triage — Glaeubigerausschuss

Bevor losgelegt wird, klaere:
1. **Ausschuss obligatorisch?** § 67 Abs. 2 InsO: bei grossen Verfahren (>250 AN, >6 Mio. EUR Bilanzsumme oder >12 Mio. EUR Umsatz) ist vorläufiger Ausschuss zwingend.
2. **Zustimmungspflicht § 160 InsO?** Welche Geschaefte benoetigen Ausschuss-Zustimmung (Betriebsveraesserung, ungewoehnlich hohe Verbindlichkeiten, Rechtsstreitigkeiten ueber EUR 10.000)?
3. **Interessenkonflikt?** Ausschussmitglied ist gleichzeitig Glaeubiger und Bieter in Verwertung → § 71 InsO Haftungsrisiko.
4. **Informations-Hol-Pflicht?** Mitglieder muessen aktiv Informationen vom IV anfordern; passives Warten genuegt nicht.

---

## Skill: `insolvenzgeld-165-sgb-iii`

_Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei Monate vor Insolvenz-Ereignis. Insolvenz-Ereignis § 165 Abs. 1 SGB III Eroeffnu..._

# Insolvenzgeld nach § 165 SGB III

## Arbeitsbereich

Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei Monate vor Insolvenz-Ereignis. Insolvenz-Ereignis § 165 Abs. 1 SGB III Eroeffnung Abweisung mangels Masse Vollstreckungs-Aussichtslosigkeit. Antragsfrist zwei Monate § 324 SGB III Vor-Finanzierung Banken bis 75 Prozent. Output Antragsentwurf Bescheinigung Abrechnung Schnittstelle Sozialversicherungs-Beitraege. Abgrenzung: forderungsanmeldung-gläubiger für allgemeine Forderungsanmeldung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzgeld nach § 165 SGB III` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Insolvenz-Status Arbeitgeber (Antrag Eröffnung)
- Arbeitsverhältnis-Daten (Dauer Lohn Stunden)
- Lohnverzug-Zeitraum
- Bisher gezahlter Lohn
- Bei Mandant=Insolvenzverwalter: Mitarbeiter-Liste

## Schritt 1 — Anspruchs-Voraussetzungen § 165 SGB III

### Persönlich Berechtigte

- **Arbeitnehmer** im Sinne § 7 SGB IV
- **Auszubildende**
- **Heimarbeiter**
- Einschluss Mini-Job-Beschäftigte
- Einschluss Teilzeit

### Nicht berechtigt

- Geschäftsführer ohne Arbeitnehmer-Status
- Selbstständige
- Arbeitnehmer in Drittland-Filialen ohne deutschen Sozial-Versicherungs-Bezug

## Schritt 2 — Insolvenz-Ereignis § 165 Abs. 1 SGB III

### Drei Tatbestände

a) **Eröffnung des Insolvenz-Verfahrens** über Vermögen des Arbeitgebers

b) **Abweisung mangels Masse** § 26 InsO

c) **Vollständige Betriebs-Einstellung** im Inland, wenn ein Insolvenz-Antrag nicht gestellt worden ist und ein Insolvenz-Verfahren offensichtlich mangels Masse nicht in Betracht kommt

### Zeit-Punkt

- **Eröffnungs-Datum** als Insolvenz-Ereignis-Datum
- Bei Abweisung mangels Masse: Abweisungs-Beschluss
- Bei Betriebs-Einstellung: tatsächliche Einstellungs-Datum

## Schritt 3 — Anspruchs-Inhalt § 167 SGB III

### Lohn der letzten drei Monate

- **Rückwärts vom Insolvenz-Ereignis-Datum**
- Nur **noch nicht gezahltes Arbeitsentgelt**
- Brutto-Forderung bis Beitrags-Bemessungs-Grenze West / Ost

### Beispiel

```
Insolvenz-Ereignis (Eröffnung): 15.05.2026
Lohn-Forderungen:
- Februar 2026: bezahlt
- März 2026: nicht bezahlt (EUR 3.500)
- April 2026: nicht bezahlt (EUR 3.500)
- Mai 2026 anteilig: nicht bezahlt (EUR 1.700)

Anspruch Insolvenzgeld: 3 Monate
- Februar nicht relevant (bezahlt)
- Mitte Feb bis Mitte Mai = drei Monate
- Berechnung: EUR 3.500 × 2 + EUR 1.700 = EUR 8.700

Bei Beitrags-Bemessungs-Grenze (West EUR 7.550/Monat
in 2026) liegt EUR 3.500 darunter — voller Anspruch
```

### Brutto vs. Netto

- Insolvenzgeld in Höhe Netto-Anspruch
- Steuer und SV-Anteile separat berechnet
- Lohnsteuer-Klassen-bezogen

### Sonderzuwendungen

- Urlaubsgeld Weihnachtsgeld nur anteilig
- Bei Fälligkeit innerhalb der drei Monate
- Provisionen bei Fälligkeit

## Schritt 4 — Antragsverfahren

### Frist § 324 SGB III

- **Zwei Monate** ab Insolvenz-Ereignis
- **Nach-Antragsfrist sechs Monate** bei unverschuldeter Versäumnis
- Frist-Beginn bei Bekanntwerden Insolvenz-Ereignis

### Antragstellung

- **Agentur für Arbeit** zuständig
- **Online-Antrag** über BA-Webportal
- **Schriftlich** möglich

### Pflicht-Anlagen

- Arbeitsvertrag
- Lohn-Abrechnungen
- Bescheinigung Insolvenz-Verwalter (Lohn-Forderung)
- Lohn-Steuer-Karte / Identifikations-Nummer

### Bescheinigung Insolvenz-Verwalter

- **Pflicht** des Insolvenz-Verwalters auf Anfrage
- Inhalt: Lohn-Höhe Fälligkeit Erfüllungs-Stand
- Schnittstelle zur Forderungs-Anmeldung

## Schritt 5 — Insolvenzgeld-Anspruchs-Übergang § 169 SGB III

### Cessio Legis

- **Lohn-Forderung geht auf BA über** mit Zahlung Insolvenzgeld
- **Anmeldung zur Insolvenz-Tabelle** durch BA
- Insolvenz-Verwalter rechnet mit BA ab

### Folge für Insolvenz-Verwalter

- BA wird Gläubiger anstelle Arbeitnehmer
- Pflicht-Vermerk in Tabelle
- Quoten-Auszahlung an BA

### Folge für Arbeitnehmer

- **Insolvenzgeld** ohne Anmeldung in Tabelle
- Bei Differenz Lohn über Beitrags-Bemessungs-Grenze — Differenz selbst anmelden

## Schritt 6 — Vor-Finanzierung

### Praktische Konstellation

- Insolvenz-Verfahren dauert
- Arbeitnehmer braucht Geld sofort
- Vor-Finanzierung durch Bank

### Vor-Finanzierungs-Vereinbarung § 170 SGB III

- **Banken-Vorfinanzierung** bis 75 Prozent Insolvenzgeld
- **Abtretung** an Bank
- BA zahlt direkt an Bank

### Vorteil Arbeitnehmer

- Schnelle Liquidität
- Schon vor Insolvenz-Ereignis möglich (in der drei-Monats-Phase)

### Vorteil Insolvenz-Verfahren

- **Fortführungs-Möglichkeit** durch Lohn-Sicherung
- **Mitarbeiter-Bindung**
- Sanierungs-Chance

## Schritt 7 — Bei Eigenverwaltung

- Anspruch Insolvenzgeld bleibt
- Sachwalter unterstützt Anträge
- Schnellere Auszahlung möglich

## Schritt 8 — Sozial-Versicherungs-Beiträge § 173 SGB III

### Pflicht-Beiträge auf Insolvenzgeld

- **Renten-Versicherung** Krankenversicherung Pflege-Versicherung Arbeitslosen-Versicherung
- **BA übernimmt** Arbeitgeber-Anteil
- **Anwartschafts-Schutz** Arbeitnehmer

### Folge

- Keine Lücke in Sozial-Versicherungs-Karriere
- Renten-Punkte werden weitergeführt

## Schritt 9 — Anspruchs-Konkurrenz

### Kurzarbeitergeld

- Bei vor Insolvenz Kurzarbeit
- Anspruch Kurzarbeitergeld parallel möglich
- Anrechnung-Mechanismen

### Krankengeld

- Bei Erkrankung in Drei-Monats-Phase
- Krankengeld plus Insolvenzgeld theoretisch
- Vorrang-Regelungen

### Mutterschaftsgeld / Elterngeld

- Spezifische Regelungen
- Sozial-Versicherungs-Karten

### Vorruhestand / Frühverrentung

- Anspruch endet mit Renteneintritt
- Insolvenzgeld dazwischen möglich

## Schritt 10 — Praktische Konstellationen

### Konstellation A — Insolvenz-Verfahren eröffnet

- Klar: Antragsfrist läuft
- Insolvenz-Verwalter-Bescheinigung anfordern
- Antrag stellen

### Konstellation B — Insolvenz-Antrag gestellt aber noch nicht eröffnet

- Vor-Finanzierungs-Vereinbarung möglich
- Antragsfrist beginnt erst mit Eröffnung

### Konstellation C — Eröffnung verzögert sich

- Eilbedürftigkeits-Erklärung an Insolvenz-Gericht
- Vor-Finanzierung erwägen

### Konstellation D — Abweisung mangels Masse

- Insolvenz-Ereignis ist Abweisung
- Antragsfrist ab Abweisungs-Beschluss
- Häufig parallel zu fehlender Insolvenz-Verwalter-Bescheinigung — Eigenbescheinigung-Eskalation

### Konstellation E — Lohn-Verzug ohne Insolvenz-Antrag

- Kein Insolvenzgeld
- Lohn-Klage Arbeitsgericht
- Bei Vermögens-Aussichts-Losigkeit Insolvenz-Antrag möglicherweise

## Schritt 11 — Aufgaben Insolvenz-Verwalter

### Lohn-Erfassung

- Lohnkonten der letzten Monate prüfen
- Lohn-Forderungen exakt aufstellen
- Lohnsteuerkarten und SV-Daten besorgen

### Bescheinigung Insolvenzgeld

- Auf Anfrage Mitarbeiter
- Standardisiertes Formular
- Frist-eng (sieben Werktage)

### Lohn-Buchhaltung Übergang

- Übernahme der Lohn-Buchhaltung
- Steuer- und SV-Anmeldungen ggf.
- Pension-Verpflichtungen-Übergang an PSVaG

### Massearm-Konstellation

- Bei Abweisung mangels Masse keine Bescheinigung-Pflicht
- Arbeitnehmer-Eigenangabe möglich

## Schritt 12 — Bei Streit über Insolvenzgeld-Anspruch

### Widerspruch BA-Bescheid

- **Ein Monat** ab Bekanntgabe, § 84 Abs. 1 SGB X i. V. m. §§ 78 ff. SGG
- Begründung
- An BA selbst

### Klage SG

- Bei Widerspruchs-Bescheid abgelehnt
- **Ein Monat** Klage-Frist § 87 Abs. 1 SGG (drei Monate wäre § 88 SGG Untätigkeitsklage)
- PKH-Antrag empfohlen → Skill `pkh-erfolgsaussicht-pruefen`

### Häufige Streit-Punkte

- **Persönlicher Anwendungsbereich** (echte Arbeitnehmer-Eigenschaft?)
- **Berechnungs-Grundlage** (Pauschalen Provisionen)
- **Drei-Monats-Phase** korrekt berechnet?
- **Bezogen-Frist** § 324 versäumt?

## Schritt 13 — Schnittstelle Forderungs-Anmeldung Tabelle

### Forderungs-Anmeldung § 174 InsO

- Bei Insolvenzgeld-Übergang BA als Gläubiger
- Restbetrag Lohn (über Beitrags-Bemessungs-Grenze) Arbeitnehmer selbst
- Skill `glaeubigerantrag-pruefung`

### Rang (wichtige Korrektur)

- **Lohn-Forderungen aus der Zeit VOR Eröffnung** sind grundsätzlich **einfache Insolvenz-Forderungen** § 38 InsO mit Quoten-Risiko — auch wenn sie aus den letzten Monaten stammen
- **Masseverbindlichkeiten** sind nur:
 - Lohn aus **fortbestehendem** Arbeitsverhältnis NACH Verfahrens-Eröffnung → § 55 Abs. 1 Nr. 2 InsO
 - im Eröffnungs-Verfahren begründete Lohn-Ansprüche bei starkem vorläufigen Verwalter mit Verfügungs-Befugnis → § 55 Abs. 2 InsO
- Für Rückstände aus den drei Monaten vor Insolvenz-Ereignis greift das Insolvenzgeld § 165 SGB III; die Forderung selbst geht auf die BA über (§ 169 SGB III) und wird als § 38 InsO-Forderung angemeldet
- § 55 Abs. 2 InsO hilft NICHT pauschal für die "letzten sechs Monate vor Eröffnung" — das ist ein verbreiteter Irrtum

## Verzahnung mit anderen Skills

- `mandat-triage-insolvenzrecht` — Einstieg
- `arbeitsrecht-kaltstart-interview` — Arbeitsrechtliche Aspekte
- `kuendigungsschutzklage` — wenn parallel Kündigung
- `pkh-erfolgsaussicht-pruefen` — bei SG-Klage gegen BA-Bescheid
- `glaeubigerantrag-pruefung` — Forderungs-Anmeldung

## Ausgabe

- `insolvenzgeld-{az}.md` mit Anspruchs-Prüfung Antragsstellung
- BA-Antragsschrift
- Insolvenz-Verwalter-Bescheinigungs-Anforderung
- Bei Streit: Widerspruchs-/Klage-Vorbereitung
- Vor-Finanzierungs-Beratung
- Frist im Fristenbuch (zwei Monate Antrag, ein Monat Widerspruch, ein Monat Klage)

## Quellen

- SGB III §§ 165 167 169 170 173 324
- SGB IV § 7
- SGG §§ 87 88; SGB X § 84
- InsO §§ 26 38 55 174
- BSG-Linien zu Insolvenzgeld
- Standes-Vorgaben Insolvenz-Verwalter zu Lohn-Bescheinigung

## Aktuelle Leitentscheidungen — Insolvenzgeld

- Konkrete BSG- und LSG-Entscheidungen zum Insolvenzgeld (insb. Anspruchsberechtigung Gesellschafter-Geschäftsführer, Drei-Monats-Frist, Vorfinanzierung) vor Ausgabe über sozialgerichtsbarkeit.de oder dejure.org mit Datum und Aktenzeichen verifizieren.
- Zur Schnittstelle § 142 InsO (Bargeschäft Lohnzahlungen) und Anfechtung: **BGH IX ZR 122/23 vom 05.12.2024** stellt klar, dass Lohnzahlungen ohne starre 30-Tage-Grenze auf engen zeitlichen Zusammenhang zu prüfen sind; bei Anfechtung des Verwalters gegen vorinsolvenzliche Lohnzahlungen ist die Unlauterkeit konkret darzulegen.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>

## Paragrafenkette Insolvenzgeld

§ 165 SGB III (Anspruchsvoraussetzungen) → § 166 SGB III (Hoehe) → § 167 SGB III (Vorfinanzierung) → § 168 SGB III (Erloesch-Gruende) → § 26 InsO (Abweisung mangels Masse als Insolvenzereignis) → § 113 InsO (Kuendigungsrecht des IV)

## Triage — Insolvenzgeld

1. **Insolvenzereignis?** Datum der Verfahrenseroffnung oder Abweisung mangels Masse exakt festlegen.
2. **3-Monats-Zeitraum?** Welche Monate werden vom Insolvenzgeld abgedeckt? Lohnrueckstaende inventarisieren.
3. **Vorfinanzierung?** Haushausbank ansprechen; Abtretungserklaerungen der Arbeitnehmer einholen; Zeitplan Vorfinanzierung → Auszahlung BA.
4. **GF-Anspruch?** GF ist nur Arbeitnehmer wenn tatsaechlich weisungsgebunden; bei Gesellschafter-GF selten Insolvenzgeld.

---

## Skill: `kaltstart-interview`

_Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter / beratender Anwalt / Geschäftsleiter / Sanierungsberater / Wirtschaftsprüfer), ty..._

# /insolvenzrecht:insolvenzrecht-kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Insolvenzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/insolvenzrecht:insolvenzrecht-kaltstart-interview` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (Dokumentenspeicher, Forderungsanmeldung-Portal, Insolvenzbekanntmachungen-RSS, Buchhaltungs-MCP). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `✓` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren.

---

## Kaltstart-Interview: Insolvenzrecht

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Insolvenzverwalter (§ 56 InsO) / Sachwalter (§ 274 InsO) / Sanierungsmoderator (§ 94 StaRUG) / beratender Anwalt (Schuldner- oder Gläubigerseite) / Geschäftsleiter mit Antragspflicht (§ 15a InsO) / Sanierungsberater (außerhalb gerichtlicher Verfahren) / Wirtschaftsprüfer mit Insolvenzmandaten?
- **Anwaltlicher Ansprechpartner** (bei Nicht-Anwälten): Name, Kanzlei, Erreichbarkeit
- **Berufsverband:** VID (Verband Insolvenzverwalter), Gravenbrucher Kreis, DRSC, IDW, sonstige

### 2. Typische Mandate / Verfahren

- **Verfahrensarten:** Regelinsolvenz / Eigenverwaltung (§§ 270 ff. InsO) / Schutzschirmverfahren (§ 270d InsO) / StaRUG / Restrukturierungsbeauftragter / Konzerninsolvenzen / Verbraucherinsolvenz
- **Branchen-Schwerpunkte** (falls vorhanden): Baugewerbe / Handel / Dienstleistung / Industrie / Immobilien / Healthcare
- **Volumen** (für Sanierungsberater): typische Bilanzsumme der Mandanten

### 3. Gutachten- und Berichtsstandards

- **IDW S 6** (Sanierungskonzept): wird verwendet ja / nein
- **IDW S 9** (Anforderungen an Insolvenzpläne): ja / nein
- **IDW S 11** (Beurteilung Insolvenzeröffnungsgründe): ja / nein
- **Eigene Hausstandards:** zusätzliche Templates, Checklisten, Berichtsstrukturen

### 4. Zuständige Insolvenzgerichte

- **Hauptzuständigkeiten:** AG/LG nach Bezirk; bei Konzerninsolvenzen: § 3a InsO (Gruppen-Gerichtsstand)
- **Bekanntmachungen:** insolvenzbekanntmachungen.de — wird regelmäßig überwacht?

### 5. Antragspflicht-Prüfung

- **Wann konsultiert das Mandat / der Geschäftsleiter typischerweise:** schon bei drohender Zahlungsunfähigkeit (§ 18 InsO) / erst bei Zahlungsunfähigkeit (§ 17 InsO) / erst bei Überschuldung (§ 19 InsO)
- **Standard für Fortbestehensprognose:** 12 Monate (§ 19 Abs. 2 InsO) / Branchenstandard / einzelfallabhängig
- **3-Wochen-Frist (§ 15a InsO):** Eskalationspfad bei Annäherung

### 6. Vergütung

- **InsVV-Anwendung:** Regelvergütung nach §§ 1 ff. InsVV / Vergütungsvereinbarung mit Gericht
- **Honorarberatung:** Stundensatz / RVG / Pauschalen

### 7. Standort

- **Bundesland / Hauptgerichtsbezirk:** [Bayern / NRW / etc.]
- **Kanzleitypus:** Einzelkanzlei / Sozietät / Großkanzlei / Inhouse

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde
- Welche Skills jetzt sinnvoll als nächstes laufen können:
 - `/insolvenzrecht:zahlungsunfähigkeit-prüfung-17-inso` — bei Liquiditätsengpässen
 - `/insolvenzrecht:überschuldung-prüfung-19-inso` — bei bilanzieller Überschuldung mit Fortbestehensprognose
 - `/insolvenzrecht:antragspflicht-15a-inso` — bei drohender 3-Wochen-Frist
 - `/insolvenzrecht:gläubigerantrag-prüfung` — bei eingegangenem Gläubigerantrag
 - `/insolvenzrecht:liquiditätsvorschau-insolvenzrechtlich` — für 21-Tage-Liquiditätsstatus
- Hinweis auf Mandatsgeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB)

## Rechtlicher Rahmen

- **InsO** — Insolvenzordnung: §§ 15a, 17, 18, 19, 56, 270 ff. (Eigenverwaltung), 286 ff. (Restschuldbefreiung)
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz (seit 01.01.2021)
- **InsVV** — Insolvenzrechtliche Vergütungsverordnung
- **IDW-Standards:** S 6 (Sanierungskonzept), S 9 (Insolvenzplan), S 11 (Insolvenzeröffnungsgründe)
- **Maßgebliche Rspr.:** BGH IX. Zivilsenat (Insolvenz) und II. Zivilsenat (Gesellschaftsrecht/Geschäftsleiterhaftung)

## Hinweise

Dieses Plugin ersetzt keine anwaltliche Beratung. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang) zu prüfen. Insolvenzantragspflicht und Eröffnungsgründe sind hochkomplex; im Zweifel **immer** anwaltliche Begleitung.

## Rechtlicher Rahmen — Kaltstart-Orientierung (Stand Mai 2026)

- § 15a InsO (Antragspflicht 3 Wo. ZU / 6 Wo. Überschuldung), §§ 17–19 InsO (Eröffnungsgründe), §§ 129 ff. InsO (Anfechtung), §§ 174 ff. InsO (Forderungsanmeldung), §§ 270 ff. InsO (Eigenverwaltung / Schutzschirm), §§ 4 ff. StaRUG.
- Aktuelle BGH-Linie (vor Ausgabe über dejure.org / openjur.de verifizieren):
 - **BGH IX ZR 122/23 vom 05.12.2024** (Unlauterkeit Bargeschäft § 142 InsO).
 - **BGH IX ZR 129/22 vom 18.04.2024** (Vorsatzanfechtung § 133 InsO; konkrete Bedrohungslage).
 - **BGH II ZR 206/22 vom 23.07.2024** (Fortwirkende Haftung ausgeschiedener GF).
 - **BGH IV ZR 66/25 vom 19.11.2025** (D&O-Wissentlichkeitsausschluss).
 - **BGH 5 StR 287/24 vom 27.02.2025** (Faktischer GF).
 - **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard — Aktionärsforderungen nachrangig).
 - **BVerfG 1 BvR 418/25 vom 28.02.2025** (StaRUG / VARTA).

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

