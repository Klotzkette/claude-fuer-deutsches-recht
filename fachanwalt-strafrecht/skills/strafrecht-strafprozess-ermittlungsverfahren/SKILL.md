---
name: strafrecht-strafprozess-ermittlungsverfahren
description: "Strafprozess Ermittlungsverfahren im Strafrecht: prüft konkret Sofortmaßnahmen im Ermittlungsverfahren, Rechtsmittel- und Notfristencockpit im Strafverfahren, BtMG-Verteidigungspraxis, Verteidigung in Verfahren mit dem Tatkomplex haeuslicher. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Strafprozess Ermittlungsverfahren

## Arbeitsbereich

**Strafprozess Ermittlungsverfahren** ordnet den Fall über die tragenden Prüfungslinien: Sofortmaßnahmen im Ermittlungsverfahren, Rechtsmittel- und Notfristencockpit im Strafverfahren, BtMG-Verteidigungspraxis. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `strafprozess-ermittlungsverfahren-sofortmassnahmen` | Sofortmaßnahmen im Ermittlungsverfahren: Polizei- oder StA-Kontakt, Vorladung, Durchsuchung, Beschlagnahme, Festnahme, Akteneinsicht, Schweigerecht, Pflichtverteidigung, Presse- und Familienkontakt in eine sichere Verteidigungsroutine bringen. |
| `strafprozess-rechtsmittel-und-notfristencockpit` | Rechtsmittel- und Notfristencockpit im Strafverfahren: prüft Strafbefehlseinspruch, Berufung, Revision, sofortige Beschwerde, einfache Beschwerde, Wiedereinsetzung, Zustellung, Empfangsbekenntnis, Fristbeginn und Mandantenentscheidung. |
| `strafrecht-spezial-btmg-strafverfahren-praxis` | BtMG-Verteidigungspraxis: Verdacht, Durchsuchung, Sicherstellung, Untersuchungshaft, V-Personen, Telekommunikationsueberwachung. Checkliste für Strafverteidiger im BtMG-Verfahren von der ersten Massnahme bis zur Hauptverhandlung. |
| `strafrecht-spezial-haeusliche-gewalt-im-strafverfahren` | Verteidigung in Verfahren mit dem Tatkomplex haeuslicher Gewalt: Tatbestandsbuendel (§ 223 KV, § 224 gefaehrliche KV, § 240 Noetigung, § 241 Bedrohung, § 238 Stalking, § 177 sexueller Uebergriff), Beweisproblematik der Aussage-gegen-Aussage-Konstellation, Glaubhaftigkeitspruefung methodisch korrekt (Hypothesen-gegen-Hypothesen), Strafantrag/öffentliches Interesse bei § 223 StGB sauber pruefen, GewSchG-Schnittstelle, Schutzanordnungen, Polizei-Wegweisung, Schutzraum-Konzepte, Strafzumessung und Aussetzung. |
| `strafrecht-spezial-markenrecht-144-markeng-strafverfahren` | Strafverfahren bei Markenstraftaten Paragraph 144 MarkenG. Antragsdelikt Privatklage besonderes öffentliches Interesse. Zuständigkeit AG LG. Verhaeltnis zu zivilrechtlicher Verletzungsklage. Strafantragsfrist Paragraph 77b StGB. Prozessuale Gestaltung Strafanzeige Verteidigung Adhaesion. Trade-offs Strafanzeige vs. zivilrechtliche Abmahnung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `strafprozess-ermittlungsverfahren-sofortmassnahmen`

**Fokus:** Sofortmaßnahmen im Ermittlungsverfahren: Polizei- oder StA-Kontakt, Vorladung, Durchsuchung, Beschlagnahme, Festnahme, Akteneinsicht, Schweigerecht, Pflichtverteidigung, Presse- und Familienkontakt in eine sichere Verteidigungsroutine bringen.

# Ermittlungsverfahren: Sofortmaßnahmen

## Zweck

Dieser Skill führt durch die ersten Stunden und Tage eines Strafmandats. Ziel ist nicht “alles erklären”, sondern Schaden verhindern: keine vorschnelle Aussage, keine verpasste Haftfrage, keine verlorenen Beweise, keine chaotische Kommunikation.

## Sofortcheck

1. Ist der Mandant Beschuldigter, Zeuge oder nur Auskunftsperson?
2. Hat eine Belehrung stattgefunden?
3. Gibt es eine Vorladung, Durchsuchung, Sicherstellung, Beschlagnahme oder Festnahme?
4. Ist der Mandant frei, vorläufig festgenommen oder in Untersuchungshaft?
5. Ist notwendige Verteidigung naheliegend?
6. Liegt Akteneinsicht vor oder muss sie beantragt werden?

## Verteidigungsroutine

- Mandant anweisen: keine Angaben zur Sache ohne Verteidiger.
- Akteneinsicht nach § 147 StPO beantragen; bei Haft wesentliche Informationen zur Freiheitsentziehung besonders einfordern.
- Vollmacht/Pflichtverteidigungsantrag klären.
- Kommunikationskanal festlegen: Mandant, Familie, Arbeitgeber, Presse nur nach Freigabe.
- Durchsuchungs-/Beschlagnahmeprotokolle sichern.
- Eigene Beweise sichern: Chats, Standortdaten, Kalender, Zeugen, Kontoauszüge, Videos.
- Wiedervorlage für Akteneinsicht und StA-Rückmeldung setzen.

## Keine-Aussage-Text

```text
Namens und in Vollmacht meines Mandanten teile ich mit, dass er derzeit
keine Angaben zur Sache machen wird. Ich beantrage Akteneinsicht nach § 147
StPO und bitte um Übersendung der Akte bzw. Bereitstellung der elektronischen
Akte. Nach Akteneinsicht werde ich unaufgefordert auf die Sache zurückkommen.
```

## Durchsuchung/ Beschlagnahme

Erzeuge:

- Fragenliste an Mandant: Was wurde wo gefunden?
- Liste beschlagnahmter Gegenstände.
- Prüfpfad Beschlagnahme/Sicherstellung.
- Herausgabe-/Widerspruchsstrategie.
- Schutz vertraulicher Mandatsunterlagen.

## Output

- `Sofortmaßnahmenplan`
- `Mandantenanweisung`
- `Akteneinsichtsantrag`
- `Beweissicherungsplan`
- `Wiedervorlagen`

## 2. `strafprozess-rechtsmittel-und-notfristencockpit`

**Fokus:** Rechtsmittel- und Notfristencockpit im Strafverfahren: prüft Strafbefehlseinspruch, Berufung, Revision, sofortige Beschwerde, einfache Beschwerde, Wiedereinsetzung, Zustellung, Empfangsbekenntnis, Fristbeginn und Mandantenentscheidung.

# Rechtsmittel- und Notfristencockpit

## Zweck

Dieser Skill sichert nach Strafbefehl, Beschluss oder Urteil die richtige Entscheidung in der richtigen Frist. Er zwingt zu getrennten Prüfungen: Statthaftigkeit, Form, Frist, Zuständigkeit, Mandantenwille, Risiko.

## Fristenkern

- Strafbefehl: Einspruch nach § 410 StPO binnen zwei Wochen ab Zustellung.
- Berufung: Einlegung nach § 314 StPO binnen einer Woche ab Verkündung.
- Revision: Einlegung nach § 341 StPO binnen einer Woche; Revisionsanträge und Begründung nach § 345 StPO grundsätzlich binnen eines Monats nach Ablauf der Einlegungsfrist, bei späterer Zustellung des Urteils ab Zustellung; Verteidiger-/Anwaltsunterschrift für die Begründung beachten.
- Sofortige Beschwerde: nur wo gesetzlich vorgesehen; Frist § 311 StPO.
- Einfache Beschwerde: Statthaftigkeit nach § 304 StPO prüfen.
- Wiedereinsetzung: § 44 StPO und Folgevorschriften streng prüfen.

## Entscheidungsblatt

```text
Rechtsmittelentscheidung

Entscheidung:
Datum Verkündung:
Datum Zustellung:
Rechtsbehelf:
Fristende:
Form:
Zuständiges Gericht:
Mandantenwille:
Risiken:
Empfehlung:
Sofortmaßnahme:
```

## Strafbefehl

Prüfe:

- vollständiger Einspruch oder Beschränkung,
- Tagessatzhöhe,
- Fahrverbot/Entziehung,
- Nebenfolgen,
- BZR/Führungszeugnis,
- Möglichkeit Entscheidung nach Aktenlage bei Beschränkung auf Tagessatzhöhe.

## Urteil

Prüfe:

- Berufung sinnvoll: neue Tatsacheninstanz.
- Revision sinnvoll: Rechtsfehler, Protokoll, Verfahrensrügen.
- Sprungrevision erwägen.
- Mandant schriftlich über Chancen, Risiken, Kosten und Frist informieren.

## Kanzlei-Routine

1. Rechtsmittel vorsorglich fristwahrend einlegen, wenn Mandantenwille noch nicht belastbar geklärt ist und kein Verzicht erklärt werden soll.
2. Sofort getrennte Wiedervorlagen anlegen: Einlegung, Urteilszustellung, Protokollfertigstellung, Begründung, Mandantenentscheidung.
3. Bei Revision sofort prüfen: vollständiges Urteil, Hauptverhandlungsprotokoll, Verständigungsdokumentation, Antrags-/Widerspruchslog, Protokollierungsanträge, letztes Wort.
4. Rücknahme nur mit dokumentierter ausdrücklicher Mandantenermächtigung; bei Verständigung Verzichtsfragen besonders vorsichtig behandeln.

## Output

- `Fristenblatt`
- `Mandantenentscheidung`
- `Rechtsmittelentwurf`
- `Risikoampel`
- `Wiedervorlage Begründung`

## 3. `strafrecht-spezial-btmg-strafverfahren-praxis`

**Fokus:** BtMG-Verteidigungspraxis: Verdacht, Durchsuchung, Sicherstellung, Untersuchungshaft, V-Personen, Telekommunikationsueberwachung. Checkliste für Strafverteidiger im BtMG-Verfahren von der ersten Massnahme bis zur Hauptverhandlung.

# BtMG-Strafverfahren: Verteidigungspraxis

## Worum geht es

Das BtMG-Verfahren hat eigene Eigenarten: hohe Bedeutung verdeckter Ermittlungen (V-Personen, TKUE, Observation), aufwaendige Sicherstellungs- und Analytik-Praxis, regelmaessig Untersuchungshaft wegen Fluchtgefahr und Wiederholungsgefahr (§ 112 Abs. 2, Abs. 3 StPO), enge Verbindung zur OK-Verfahrenspraxis.

Dieser Skill ist Checkliste für Strafverteidiger in BtMG-Verfahren — von der ersten Polizeikontaktnahme bis zur Hauptverhandlung.

## Tatbestand und Stoffliche Erfassung

(Der Skill ist nicht stoff-, sondern verfahrensorientiert. Stoffliche Erfassung siehe Schwester-Skills.)

**Anwendungsbereich:** alle Verfahren wegen §§ 29 bis 30a BtMG, §§ 34, 35 KCanG, § 4 NpSG.

## Mengen und Schwellen

(Verfahrensschwellen statt Stoffschwellen.)

| Massnahme | Voraussetzung | Norm |
|---|---|---|
| Durchsuchung | Anfangsverdacht, richterliche Anordnung | § 102, § 105 StPO |
| Vorlaeufige Festnahme | Festnahmegrund § 127 StPO | § 127 StPO |
| Untersuchungshaft | dringender Tatverdacht, Haftgrund | § 112 StPO |
| TKUE | Katalogtat erforderlich | § 100a StPO |
| Online-Durchsuchung | Schwere Straftat Katalog | § 100b StPO |
| V-Person-Einsatz | erhebliche Bedeutung Tat | § 110a StPO |
| Wohnraum-Ueberwachung | besonders schwere Straftat | § 100c StPO |

## Praktikertipps der Verteidigung

### Phase 1 — Erste Massnahme

1. **Durchsuchung:** Anordnungsbeschluss verlangen (§ 105 StPO). Bei Gefahr im Verzug Begruendung dokumentieren. Belehrung als Beschuldigter (§ 136 StPO)?
2. **Identitaetsfeststellung:** Mandant identifiziert sich, aber sagt zur Sache nichts. Keine erkennungsdienstliche Behandlung ohne Anordnung.
3. **Schweigen:** Beim ersten Kontakt regelmaessig schweigen. Anwalt einschalten — auch im Polizeigewahrsam.
4. **Sicherstellung:** Quittung verlangen. Probennahme protokollieren lassen. Zeugen benennen.

### Phase 2 — Akteneinsicht

5. **Akteneinsicht beantragen:** § 147 StPO. Auch in technische Aufzeichnungen (TKUE-Protokolle, V-Personen-Akten).
6. **Wirkstoffgutachten anfordern:** Probennahmeprotokoll, Eichschein der Waage, Laborakkreditierung pruefen.
7. **TKUE-Pruefung:** Anordnungsbeschluss, Verlaengerungen, Kreis der Beteiligten, Verwertbarkeit nach § 100a Abs. 4 StPO (Kernbereich).
8. **V-Person-Akte:** Identitaet bleibt regelmaessig anonym; aber Glaubwuerdigkeit, Vorstrafen, Vergueteung muessen offengelegt werden (BGH staendige Rspr.; verifizieren).

### Phase 3 — Untersuchungshaft

9. **Haftpruefung:** § 117 StPO Antrag. Fluchtgefahr begruendet? Wiederholungsgefahr § 112 Abs. 3 StPO (bei § 29a, § 30, § 30a BtMG vermutet, aber widerlegbar).
10. **Verhaeltnismaessigkeit:** Sechs-Monats-Frist § 121 StPO. Verlaengerung nur durch OLG.
11. **Haftbeschwerde:** § 304 StPO; Detail-Skill `fachanwalt-strafrecht-untersuchungshaft-haftpruefung`.

### Phase 4 — Vorbereitung Hauptverhandlung

12. **Beweisantraege:** § 244 StPO. Stoffanalysen-Gegengutachten, Zeugen, V-Personen-Aussage (zumindest Sperrerklaerung pruefen).
13. **Einlassungs-Vorbereitung:** Schweigen oder Gestaendnis? § 31 BtMG Aufklaerungshilfe? Verstaendigung § 257c StPO?
14. **Therapie-Anbahnung:** § 35 BtMG vorbereiten — Therapieplatz, Suchtgutachten, Krankenversicherung.

### Phase 5 — Hauptverhandlung

15. **Strafzumessung vortragen:** Mengenfrage, Wirkstoffgehalt, individueller Tatbeitrag, Aufklaerungshilfe, eigene Sucht, Vorstrafenstand.
16. **Schlussvortrag:** Verteidigerplaedoyer; Detail-Skill `plaedoyer-vorbereitung-strafverteidigung`.

## Trade-off-Matrix

| Strategie | Vorteil | Nachteil |
|---|---|---|
| Aktives Bestreiten | Hauptverhandlung mit voller Streitlust | Bei klarer Beweislage Strafschaerfung |
| Schweigen + Defensiv | Verteidigungsoptionen offen | Keine Aufklaerungshilfe-Bonifizierung |
| Frueh § 31 BtMG | Strafrahmenverschiebung | Belastung Mitbeschuldigter |
| § 257c StPO Verstaendigung | Planbare Strafe | Bindungswirkung, eingeschraenkte Revision |

## Konkurrenzen

(Verfahrensbezogen — Konkurrenzen siehe stoffbezogene Skills.)

## Strafzumessung und Therapie statt Strafe

- Strafzumessungsdaten im Verlauf des Verfahrens sammeln: Suchtbiografie, Therapiebereitschaft, soziales Umfeld, berufliche Perspektive.
- Therapieplatz vor Hauptverhandlung organisieren — beeinflusst Strafzumessung und § 35 BtMG.
- Aufklaerungshilfe nur nach reiflicher Beratung.

## Mustertexte

**Antrag Akteneinsicht TKUE-Protokolle:**
"In dem Verfahren gegen meinen Mandanten beantrage ich Akteneinsicht in
1. die TKUE-Anordnungsbeschluesse einschliesslich Verlaengerungen
2. die vollstaendigen TKUE-Protokolle (Wortprotokolle, Zusammenfassungen)
3. die Mitteilungen ueber die Massnahmen nach § 101 Abs. 4 StPO
4. die Akte zum V-Personen-Einsatz mit Sperrerklaerung gemaess § 96 StPO."

**Haftpruefungsantrag:**
"In der Strafsache gegen meinen Mandanten beantrage ich Haftpruefung gemaess § 117 StPO. Es fehlt am Haftgrund: Fluchtgefahr besteht nicht (Wohnsitz, Familie, Arbeit in Deutschland, Beschaffung Reisepass schwierig). Die Wiederholungsgefahr nach § 112 Abs. 3 StPO ist widerlegt durch [konkrete Umstaende: Therapieantritt, Wohnumfeld, soziales Netz]."

## Querverweise

- `strafrecht-spezial-btmg-29-grundtatbestand`
- `strafrecht-spezial-btmg-29a-nicht-geringe-menge`
- `strafrecht-spezial-btmg-30-handeltreiben`
- `strafrecht-spezial-btmg-30a-schwerer-bandenhandel`
- `strafrecht-spezial-btmg-31-aufklaerungshilfe-kronzeuge`
- `strafrecht-spezial-btmg-35-therapie-statt-strafe`
- `strafrecht-spezial-btmg-konsumeigenbedarf-verteidigung`
- `strafrecht-spezial-btmg-nicht-geringe-menge-grenzen`
- `fachanwalt-strafrecht-untersuchungshaft-haftpruefung`
- `fachanwalt-strafrecht-akteneinsicht-beantragen`
- `fachanwalt-strafrecht-verstaendigung-257c-toa-46a`
- `plaedoyer-vorbereitung-strafverteidigung`

## Quellen Stand 06/2026

- §§ 102 ff. StPO Durchsuchung.
- § 112 StPO Untersuchungshaft (mit Sonderhaftgrund § 112 Abs. 3 StPO bei § 29a, § 30, § 30a BtMG).
- §§ 100a, 100b, 100c, 110a StPO verdeckte Massnahmen.
- § 147 StPO Akteneinsicht.
- § 244 StPO Beweisantraege.
- § 257c StPO Verstaendigung.
- BGH staendige Rspr. zur Verwertbarkeit V-Personen-Aussagen, Anonymisierung (§§ 68, 110a ff. StPO; BGH-Linie verifizieren).
- BVerfG zur Kernbereichsschutz bei TKUE (BVerfG, BVerfG-Linie verifizieren).
- Methodik siehe `references/methodik-buergerliches-recht.md`.
- Zitierregeln siehe `references/zitierweise.md`.

## 4. `strafrecht-spezial-haeusliche-gewalt-im-strafverfahren`

**Fokus:** Verteidigung in Verfahren mit dem Tatkomplex haeuslicher Gewalt: Tatbestandsbuendel (§ 223 KV, § 224 gefaehrliche KV, § 240 Noetigung, § 241 Bedrohung, § 238 Stalking, § 177 sexueller Uebergriff), Beweisproblematik der Aussage-gegen-Aussage-Konstellation, Glaubhaftigkeitspruefung methodisch korrekt (Hypothesen-gegen-Hypothesen), Strafantrag/öffentliches Interesse bei § 223 StGB sauber pruefen, GewSchG-Schnittstelle, Schutzanordnungen, Polizei-Wegweisung, Schutzraum-Konzepte, Strafzumessung und Aussetzung.

# Haeusliche Gewalt im Strafverfahren — Verteidigerleitfaden

## Worum geht es konkret

"Haeusliche Gewalt" ist kein eigener Straftatbestand, sondern ein Tat-Kontext, der mehrere Strafnormen aktiviert. Verfahren sind kommunikativ, beweisrechtlich und strafprozessual besonders herausfordernd, weil die Beziehungsdynamik in die Beweisaufnahme hineinwirkt. Verteidiger muessen den Tatbestand sauber pruefen, die Aussage-gegen-Aussage-Konstellation methodisch behandeln und parallel die zivilrechtliche GewSchG-Schiene mitdenken.

## Tatbestandsbuendel im Detail

| Norm | Inhalt | Strafrahmen |
|---|---|---|
| § 223 StGB | einfache Koerperverletzung | bis 5 Jahre |
| § 224 StGB | gefaehrliche KV (Waffen, Bande, gefaehrl. Werkzeug, lebensgefaehrliche Behandlung, gemeinschaftlich) | 6 Monate bis 10 Jahre |
| § 225 StGB | Misshandlung von Schutzbefohlenen | 6 Monate bis 10 Jahre |
| § 226 StGB | schwere KV (Folge: Verlust Glied, dauernde Entstellung etc.) | 1 bis 10 Jahre |
| § 227 StGB | KV mit Todesfolge | mind. 3 Jahre |
| § 177 StGB | sexueller Uebergriff/Vergewaltigung (auch in Ehe) | 6 Monate bis 10 Jahre |
| § 238 StGB | Nachstellung (vgl. nach Trennung) | bis 3 Jahre |
| § 240 StGB | Noetigung | bis 3 Jahre |
| § 241 StGB | Bedrohung | bis 1 Jahr |
| § 4 GewSchG | Verstoss gegen zivilen Schutzbeschluss | bis 1 Jahr |

## Praktikertipps der Verteidigung

- **Strafantrag und öffentliches Interesse sauber trennen**: Bei reiner einfacher Koerperverletzung nach § 223 StGB gilt § 230 StGB. Die Tat wird grundsaetzlich nur auf Strafantrag verfolgt, es sei denn, die Staatsanwaltschaft haelt wegen besonderen öffentlichen Interesses ein Einschreiten von Amts wegen für geboten. Deshalb zuerst klaeren: Strafantrag gestellt? Frist und Berechtigung? Rücknahme nach § 77d StGB denkbar? Hat die StA das besondere öffentliche Interesse ausdruecklich oder der Sache nach bejaht? § 248a StGB gehoert nicht hierher; er betrifft geringwertige Vermoegensdelikte, nicht Koerperverletzung.
- **Aussage-gegen-Aussage**: regelmaessig methodische Glaubhaftigkeitspruefung erforderlich. Verteidigung sollte aussagepsychologisches SV-Gutachten anregen (§ 244 III StPO), wenn Realkennzeichen schwach sind oder Motiv zur Falschbelastung erkennbar (Trennungsdynamik, Sorgerechtsstreit).
- **Polizeiprotokoll als Beweismittel**: Sturmprotokolle der Polizei, Wegweisungs-/Rueckkehrverbote nach Polizeigesetz Land sind oft Schluesselbeweise. Verteidiger holt Protokoll im Original; Verzerrungen durch Stresssituation und Wahrnehmungslueken kommen vor.
- **Schutzraum-Akte**: Mandant darf wegen Aufnahme in Frauenhaus keine Annaeherung suchen. Adressfeststellung durch Verteidiger ueber Strafakte (§ 147 StPO) — diskret und ohne Verschriftlichung im Mandantenkontakt.
- **Beratungskette mit Familiengericht**: Schutzbeschluss § 1 GewSchG, Wohnungszuweisung § 2 GewSchG, Sorgerecht/Umgang — alle Verfahren parallel; ein Familienverfahren kann das Strafverfahren stark beeinflussen.
- **Tat-Provokation**: § 199 StGB Wechselseitigkeit bei Beleidigung; bei KV-Streit ohne klares Aggressor-Opfer-Verhaeltnis kann § 213 StGB (minder schwerer Fall Totschlag) bzw. Provokationsgrundsatz bei Strafzumessung argumentiert werden.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| Vollbestreiten vs. Teil-Einlassung mit Provokation | Komplettbestreiten | Anerkenntnis KV im Affekt + Provokation | Pfad B bei objektiv unzweifelhaftem Tatverhalten |
| Eigene Aussage Klient vs. Schweigen | Aussage zur Sache | Schweigen § 136 StPO | bei aussagepsy-relevanten Faellen i.d.R. Schweigen, bis Aussagebeweis verifiziert |
| § 153a StPO Einstellung mit Auflage | Therapie, Geldauflage, Vergleich Schmerzensgeld | Hauptverhandlung mit Freispruchsantrag | Pfad A bei Ersttaeter, mittlerer Schwere, gefestigter Trennung |
| Antraegen-/Schutzanordnungsverfahren | parallel mitkonfigurieren | abwarten | Pfad A — Familienverfahren wirkt sich auf Strafverfahren aus |

## Konkurrenzen

- § 223 und § 224 stehen in Spezialitaet (gefaehrliche KV verdraengt einfache).
- § 223 und § 240 oder § 241 stehen in Tateinheit, wenn die KV mit Zwang oder Drohung verbunden ist.
- § 177 und § 224 stehen in Tateinheit, wenn die sexuelle Handlung mit Gewalt verbunden ist.
- § 4 GewSchG und § 238 StGB Tatmehrheit.

## Strafzumessung und Folgen

- § 46 StGB: Beziehungsdynamik, Wiederholungsgefahr, Therapieeinsicht, Trennung vollzogen.
- Bei Ersttaeter mit Affektaspekt regelmaessig Geldstrafe oder Freiheitsstrafe zur Bewaehrung.
- Bei Wiederholungstaeter mit Polizeibewertung "hohes Risiko" tendenziell Vollzug; Praeventionspakete (TOA § 46a, antiviolence-Programm) als Strafzumessung-Mitigation.
- Bewaehrungsauflagen: Therapie, Kontaktverbot, Wohnungswechsel.
- Berufliche Folgen bei Polizei/Bundeswehr/Sicherheitsdienst — Berufsverbot § 70 StGB selten, aber arbeitsrechtliche Folgen.

## Mustertexte

**Einlassung-Entwurf** (Auszug, defensive Variante):
> Mein Mandant nimmt Stellung wie folgt: Die geschilderten Vorgaenge am [Datum] sind aus seiner Wahrnehmung anders verlaufen, als von der Geschaedigten dargestellt. Insbesondere hat ihn die Geschaedigte zuerst mit den im Polizeiprotokoll dokumentierten Worten beleidigt und einen Schlag in das Gesicht ausgefuehrt. Die nachfolgende reaktive Bewegung meines Mandanten stand im Spannungsverhaeltnis Notwehr § 32 StGB / Affekt. Im Uebrigen wird auf das Schweigerecht zurueckgegriffen, soweit Detailfragen die Beziehungsdynamik betreffen.

**Hilfsbeweisantrag aussagepsy-Gutachten**:
> Hilfsweise wird beantragt, ein aussagepsychologisches Sachverstaendigengutachten zu Frau [Geschaedigte] einzuholen. Es ist methodisch nach der Hypothesen-gegen-Hypothesen-Methode (BGH 30.07.1999 - 1 StR 618/98, BGHSt 45, 164) zu klaeren, ob die belastende Aussage erlebnisbasiert ist oder durch (a) Trennungs- und Sorgerechtskonflikt, (b) Loyalitaetskonflikt gegenueber Dritten, (c) konfliktreiche Vor-Vernehmungssituation suggestiv gepraegt ist.

## Querverweise

- `strafrecht-spezial-aussagepsychologie-bgh-grundsaetze`
- `strafrecht-spezial-aussagepsychologie-realkennzeichen`
- `strafrecht-spezial-aussagepsy-suggestion-falscherinnerung`
- `strafrecht-spezial-koerperverletzung-223-stgb-grund`
- `strafrecht-spezial-stalking-238-stgb`
- `fachanwalt-familienrecht` (GewSchG-Schnittstelle, Annaeherungsverbot, Wohnungszuweisung, Sorgerecht)

## Quellen Stand 06/2026

- §§ 223 ff., 177, 238, 240, 241 StGB.
- GewSchG, insb. §§ 1, 2, 4 GewSchG.
- Polizeigesetze der Länder (Wegweisung/Rueckkehrverbot je nach Bundesland unterschiedlich — z.B. § 31 PolG NRW).
- BGH staend. Rspr. zu Aussage-gegen-Aussage-Konstellation; methodische Standards der Aussagepsychologie BGH 30.07.1999 - 1 StR 618/98 (BGHSt 45, 164).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `strafrecht-spezial-markenrecht-144-markeng-strafverfahren`

**Fokus:** Strafverfahren bei Markenstraftaten Paragraph 144 MarkenG. Antragsdelikt Privatklage besonderes öffentliches Interesse. Zuständigkeit AG LG. Verhaeltnis zu zivilrechtlicher Verletzungsklage. Strafantragsfrist Paragraph 77b StGB. Prozessuale Gestaltung Strafanzeige Verteidigung Adhaesion. Trade-offs Strafanzeige vs. zivilrechtliche Abmahnung.

# Strafverfahren bei Markenstraftaten nach Paragraph 144 MarkenG

## Worum geht es

Paragraph 144 MarkenG ist die zentrale prozessuale Klammer für Markenstraftaten. Er regelt:

- Paragraph 144 Abs 1 MarkenG: **Antragsdelikt-Charakter** des Paragraph 143 MarkenG (Grundtatbestand) und ggf. weiterer Tatbestaende mit Ausnahme besonderes öffentliches Interesse.
- Paragraph 144 Abs 2 MarkenG: **Privatklageweg** Paragraph 374 StPO als alternative oder primaere Verfolgungsstrategie.
- Vereinfacht: Paragraph 143a MarkenG (bandenmaessig) bleibt davon unberuehrt; siehe `strafrecht-spezial-markenrecht-143a-markeng-bandenmaessig`.

Praxisrelevanz: Markeninhaber stehen vor der Wahl zwischen Strafanzeige (mit Strafverfolgung durch StA), Privatklage (eigene prozessuale Initiative bei eingeschraenktem StA-Interesse) und zivilrechtlicher Unterlassungsklage (gewoehnlicher Hauptweg). Verteidigung sollte das Zusammenspiel beider Verfahrensschienen aktiv steuern.

## Tatbestand und Geltungsbereich

Paragraph 144 Abs 1 MarkenG: Paragraph 143 MarkenG (Grundtatbestand) wird nur auf Antrag verfolgt, es sei denn, die Strafverfolgungsbehoerde haelt wegen des besonderen öffentlichen Interesses an der Strafverfolgung ein Einschreiten von Amts wegen für geboten. Praxistypische Indikatoren für besonderes öffentliches Interesse:

- Hoher Umsatz aus Verletzungshandlung.
- Vertrieb gefaehrlicher Faelschungen (Arzneimittel, Sicherheitsausruestung, Kinderspielzeug — Gesundheitsgefahr).
- Organisierter Vertrieb ueber Marktplaetze mit grosser Reichweite.
- Wiederholungstaeterschaft trotz vorausgegangener Verurteilung oder Unterlassungsverpflichtung.
- Verbindung mit weiteren Tatbestaenden (Steuerhinterziehung, Geldwaesche).

Paragraph 144 Abs 2 MarkenG: Privatklageweg eroeffnet. Paragraph 374 StPO fuehrt zur Privatklage des Verletzten; Anwaltszwang besteht nicht, doch in der Praxis stets anwaltliche Vertretung; Suehneversuch nach Paragraphen 380 ff. StPO erforderlich vor Privatklage; eingeschraenkte Beweismittel und keine StA-Sachaufklaerung.

## Strafantrag und Antragsbefugnis

Antragsfrist Paragraph 77b StGB drei Monate ab Kenntnis von Tat und Taeter durch den Antragsberechtigten. Bei juristischen Personen Vertretungsorgan; bei mehreren Antragsberechtigten genuegt der Antrag eines einzelnen.

Antragsberechtigt:
- Markeninhaber (Paragraph 4 MarkenG).
- Ausschliesslicher Lizenznehmer (Paragraph 30 Abs 3 MarkenG; Antrag mit Zustimmung des Markeninhabers).
- Rechtsnachfolger.

Praxiswichtig: Bei Unionsmarken (Verordnung 2017/1001) ist die Antragsberechtigung gleich; deutsches Strafrecht setzt nur an die Markenrechtsverletzung im deutschen Hoheitsgebiet an (Paragraph 9 StGB Tatort).

Der Antrag muss schriftlich (Paragraph 158 StPO; in Praxis ueber Strafanzeige mit Antragstellung verbunden) und in der dreimonatigen Frist gestellt werden. Antrag kann zurueckgenommen werden (Paragraph 77d StGB), Wiederholung dann ausgeschlossen.

## Praktikertipps der Verteidigung

- **Antragsfrist mathematisch pruefen.** Drei Monate ab Kenntnis von Tat und Taeter. Wann hatte das Vertretungsorgan tatsaechlich Kenntnis? Testkauf-Datum, Versandnachweis, interne Mitteilung dokumentieren. Verspaeteter Antrag fuehrt zur Einstellung Paragraph 170 Abs 2 StPO.
- **Besonderes öffentliches Interesse erschuettern.** Wenn StA Offizialverfolgung aufnimmt, ist die Annahme des besonderen öffentlichen Interesses zu pruefen. Bei nur einzelnen Verkaufstaten geringen Umfangs ist das Interesse nicht zu bejahen; Antragsmangel fuehrt zur Einstellung.
- **Privatklageverweis anregen.** Im Schriftsatz an die StA frueh anregen, dass keine besondere öffentliche Bedeutung gegeben sei und der Markeninhaber auf den Privatklageweg verwiesen werden moege. Markeninhaber scheut Privatklageweg wegen Kostenrisiko und Aufwand; oft Effekt der faktischen Einstellung.
- **Adhaesion vorbereiten oder verhindern.** Markeninhaber kann Adhaesionsantrag nach Paragraphen 403 ff. StPO stellen (Schadensersatz im Strafverfahren). Verteidigung sollte Bezifferung pruefen und ggf. Verweisung an Zivilverfahren beantragen (Paragraph 406 Abs 1 S 3 bis 6 StPO).
- **Zuständigkeit.** Amtsgericht regelmaessig bei Paragraph 143 MarkenG (Strafrahmen bis drei Jahre, Paragraph 24 GVG). Bei Paragraph 143a MarkenG (Verbrechen) Landgericht (Paragraph 74 Abs 1 GVG, sofern Erwartung ueber vier Jahre Strafe). Bei Bezug zur Wirtschaftsstrafkammer Paragraph 74c GVG pruefen (gewerblicher Rechtsschutz ist nach Auslegung erfasst).

## Trade-off-Matrix

| Pfad A Strafanzeige durch Markeninhaber | Pfad B Zivilrechtliche Unterlassungsklage allein | Empfehlung |
| --- | --- | --- |
| Strafanzeige loest StA-Ermittlung mit Beschlagnahme, Durchsuchung und Druck auf Beschuldigten aus; Adhaesion moeglich; Strafmass kann zivile Vergleichsbereitschaft erhoehen | Schnellere Wirkung durch einstweilige Verfuegung (Paragraph 935 ZPO); Unterlassungstitel direkt; keine StA-Wartezeit; geringere Reputationswirkung | Markeninhaber waehlt regelmaessig parallelen Weg: einstweilige Verfuegung sofort + Strafanzeige zur Drohkulisse + Hauptsacheklage zur Folge. Verteidigung muss alle drei Schienen synchron managen. |

Aus Sicht der Verteidigung: Wenn der Mandant kooperationsbereit ist, anwaltlich vor StA Schadensbezifferung mit Markeninhaber aushandeln und auf Antragsruecknahme Paragraph 77d StGB hinwirken; gegen Geldzahlung oft moeglich.

## Konkurrenzen

- **Paragraph 144 MarkenG ist prozessuale Norm**, keine eigenstaendige Strafnorm. Sie modifiziert die Verfolgbarkeit der Paragraph 143 MarkenG und (eingeschraenkt) Paragraph 143a MarkenG.
- **Paragraph 143a MarkenG** ist Offizialdelikt; Paragraph 144 MarkenG gilt insoweit nicht. Antragserfordernis entfaellt bei Bandentaten.
- **Verhaeltnis zum Zivilrecht.** Verfahren parallel; rechtskraeftiges Strafurteil entfaltet im Zivilverfahren Indizwirkung, aber keine Bindungswirkung (anders als bei Schaedigung im Sinne Paragraph 14 BGB nach KapMuG; in normalen Zivilverfahren herrscht freie Beweiswuerdigung nach Paragraph 286 ZPO).

## Strafzumessung

Strafrahmen ergibt sich aus dem materiellen Tatbestand: Paragraph 143 MarkenG bis drei Jahre, Paragraph 143a MarkenG drei Monate bis fuenf Jahre. Paragraph 144 MarkenG selbst enthaelt keinen Strafrahmen.

Praxistipps:
- Bei Antragsruecknahme Paragraph 77d StGB nach Vergleich mit Markeninhaber: Verfahren wird nach Paragraph 170 Abs 2 StPO eingestellt; keine Vorstrafe; Vermeidung von BZRG-Eintrag.
- Bei Verweis auf Privatklage durch StA: keine StA-Ermittlung mehr; Markeninhaber muss Suehneversuch und Privatklage selbst betreiben; in 80 Prozent der Faelle keine Privatklage tatsaechlich erhoben.
- Einziehung Paragraph 74 StGB iVm Paragraph 143 Abs 5 MarkenG; Gewinnabschoepfung Paragraph 73 StGB.

## Mustertexte

**Schriftsatz an StA — Verweis auf Privatklageweg:** "Namens des Beschuldigten beantrage ich, das Verfahren gegen meinen Mandanten nach Paragraph 170 Abs 2 StPO einzustellen. Mein Mandant hat das streitgegenstaendliche Verhalten nur einmalig vorgenommen; ein Umsatz von EUR X im Tatzeitraum belegt das Fehlen einer fortlaufenden Erwerbsabsicht. Ein besonderes öffentliches Interesse an der Strafverfolgung im Sinne Paragraph 144 Abs 1 MarkenG ist nicht erkennbar; die Markeninhaberin moege auf den Privatklageweg Paragraph 374 StPO iVm Paragraph 144 Abs 2 MarkenG verwiesen werden."

**Antragsrueckname-Vereinbarung (Verteidigerseite):** "Im Wege der gueltichen Streitbeilegung erkennt mein Mandant Schadensersatz an die X AG in Hoehe von EUR Y an. Die X AG verpflichtet sich, den Strafantrag gemaess Paragraph 77d StGB zurueckzunehmen, sobald die Zahlung erfolgt ist. Beide Parteien vereinbaren wechselseitige Stillschweigeverpflichtungen."

**Strafanzeige mit Antrag (Markeninhaber-Seite):** "Namens und mit Vollmacht der X AG, Inhaberin der Marke Y, erstatte ich Strafanzeige und stelle Strafantrag gemaess Paragraph 144 Abs 1 MarkenG iVm Paragraph 143 MarkenG. Die Mandantin hat am DD.MM.JJJJ erstmals Kenntnis von Tat und Taeter erlangt. Ein besonderes öffentliches Interesse besteht: Der Beschuldigte hat ueber die Plattform Z im Tatzeitraum [...] Stueck Counterfeit-Ware mit einem Umsatz von EUR W vertrieben; die Vertriebsstruktur weist auf Wiederholungsabsicht hin. Die Akte enthaelt: Testkaeufe (Anlage K1), Originalitaetsbegutachtung durch X AG (Anlage K2), Plattform-Verkaufsstatistik (Anlage K3)."

## Querverweise

- `strafrecht-spezial-markenrecht-143-markeng`
- `strafrecht-spezial-markenrecht-143a-markeng-bandenmaessig`
- `strafrecht-spezial-ip-strafrecht-grenzbeschlagnahme`
- `strafrecht-spezial-ip-strafrecht-verteidigung`
- `fachanwalt-strafrecht-adhaesionsverfahren`

## Quellen Stand 06/2026

- Paragraph 144 MarkenG im Wortlaut (gesetze-im-internet.de).
- Paragraphen 4, 14, 30, 142a MarkenG.
- Paragraphen 77, 77b, 77d StGB (Strafantrag, Antragsfrist, Antragsruecknahme).
- Paragraphen 158, 170, 374 StPO; Paragraphen 380 ff. StPO Suehneverfahren.
- Paragraphen 24, 74, 74c GVG Zuständigkeit.
- Paragraphen 403 ff. StPO Adhaesionsverfahren.
- VO (EU) 608/2013 (Produktpiraterieverordnung) für Grenzbeschlagnahme.
- BGH staendige Rspr. zum besonderen öffentlichen Interesse bei IP-Straftaten; Datum und konkrete Aktenzeichen vor Verwendung im Schriftsatz live verifizieren.
