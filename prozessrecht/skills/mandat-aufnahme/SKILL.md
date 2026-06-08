---
name: mandat-aufnahme
description: "Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufnahme-Protokoll. Abgrenzung: nicht inhaltliche Klageschrift im Prozessrecht."
---

# Mandat-Intake

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Aufnahme

1. **Mandatstyp:** Klägerseite, Beklagtenseite, Beratungsmandat oder gemischtes Mandat?
2. **Interessenkonflikt:** Besteht ein Interessenkonflikt mit laufenden oder abgeschlossenen Mandaten (§ 43a Abs. 4 BRAO, § 3 BORA)?
3. **Verfahrensart:** Zivilverfahren, arbeitsgerichtliches Verfahren, Verwaltungsverfahren, Strafverfahren?
4. **Schlüsselfristen:** Gibt es laufende Fristen (Verjährung, Rechtsmittelfrist, Klagefrist) die sofort gesichert werden müssen?
5. **Außenmandat:** Wird ein Korrespondenzanwalt oder Fachanwalt benötigt?

## Zentrale Normen
- § 43a Abs. 4 BRAO (Interessenkonflikt — Vertretungsverbot)
- § 3 BORA (Interessenkonflikt — weitere Fallgruppen)
- § 49b BRAO (Vergütungsvereinbarung)
- § 204 BGB (Verjährungshemmung durch Klage)
- § 232 ff. ZPO (Fristen und Fristenberechnung)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Optional: Name oder Kurzbezeichnung des Mandats
- Hochgeladene Dokumente (z. B. Klageschrift, Abmahnung, Bescheid, Vertrag)

## Ablauf

### 1. Identifikation und Aktenzeichen

- Kanzlei-Aktenzeichen und interner Slug (URL-freundlich, z. B. `mueller-gmbh-werkvertrag-2024`)
- Mandantenname (juristische oder natürliche Person), Kontaktperson
- Mandantentyp: Unternehmer (§ 14 BGB) / Verbraucher (§ 13 BGB)
- Gegenseite: Vollständiger Name, Anschrift, Verfahrensbevollmächtigter (wenn bekannt)
- Mandats-Art: Klage / Verteidigung / Beratung / Rechtsmittel / Vollstreckung

### 2. Interessenkonflikt-Check (§ 43a Abs. 4 BRAO, § 3 BORA)

- Vertritt die Kanzlei bereits die Gegenseite in irgendeinem Mandat?
- Ist ein Anwalt der Kanzlei früher für die Gegenseite tätig gewesen?
- Bestehen sonstige Interessenkonflikte (persönliche Beziehungen, Eigeninteresse)?
- **Bei positivem Befund:** Mandat ablehnen oder um Einverständnis einholen; Plugin erstellt Interessenkonflikt-Vermerk.

### 3. Sachverhaltserfassung

- Kurzbeschreibung des Sachverhalts (wer, was, wann, wie viel?)
- Anspruchsgrundlage (vorläufig, z. B. § 280 BGB, § 823 BGB, § 1 UWG)
- Rechtliches Kernproblem (streitige Tat- oder Rechtsfrage)
- Vorhandene Dokumente: Liste und Anlage-Nummern

### 4. Verfahrensart und Zuständigkeit

- Verfahrensordnung: ZPO / ArbGG / VwGO / FGO / SGG / FamFG / StPO
- Sachlich zuständiges Gericht: AG (§§ 23 ff. GVG), LG (§§ 71 ff. GVG), Spezialgerichte (ArbG, VG, FG, SG)
- Örtliche Zuständigkeit: allgemeiner Gerichtsstand (§§ 12, 13 ZPO), besonderer Gerichtsstand (§ 29 ZPO: Erfüllungsort), ausschließlicher Gerichtsstand (§ 29a ZPO: Miete)
- Streitwert (vorläufig, nach GKG/RVG)

### 5. Risikotriage

- Erfolgsaussichten: stark / mittel / schwach (mit Kurzbereg)
- Worst-Case-Szenario (maximale Exposition inkl. Kosten § 91 ZPO)
- Wichtig: Prozesskostenrisiko nach § 91 ZPO; ggf. Rechtsschutzversicherung vorhanden?
- Verjährungsrisiko prüfen: Restlaufzeit (§§ 195, 199 BGB)

### 6. Außenanwalt / Korrespondenzanwalt

- Wird die Sache vollständig intern geführt oder von externer Kanzlei?
- Externer Anwalt: Name, Kanzlei, Kontakt
- Reporting-Intervall an Mandanten

### 7. Beweissicherung

- Ist sofortige Beweissicherung erforderlich? (z. B. Baumangel, drohende Sachzustandsveränderung)
- Aufbewahrungsanordnung erstellen? → Weiterleitung an Skill `beweissicherung`

### 8. Schlüsselfristen

- Klagefrist / Antwortfrist
- Verjährungsablauf
- Nächste Prozesshandlung

### 9. mandat.md und verlauf.md schreiben

```yaml
### mandat.md
slug: ""
kanzlei_az: ""
mandant:
 name: ""
 typ: "Unternehmer / Verbraucher"
gegenseite:
 name: ""
 anwalt: ""
verfahren:
 art: ""
 gericht: ""
 az_gericht: ""
 verfahrensordnung: ""
streitwert: 0
anspruchsgrundlage: ""
risiko: "hoch / mittel / gering"
exposition_max: 0
verjaehrung: ""
aussenanwalt: ""
status: "aktiv"
beweissicherung: false
angelegt: "TT.MM.JJJJ"
naechste_frist: "TT.MM.JJJJ"
```

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BRAO § 43a Abs. 4 (Interessenkonflikt: Verbot der Vertretung widerstreitender Interessen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken / typische Fehler

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Verjährung nicht geprüft:** Vor Intake stets Verjährungsablauf ermitteln; läuft die Verjährung in < 3 Monaten, sofort Hemmungsmaßnahmen (§ 204 BGB: Klageerhebung, Mahnbescheid) einleiten.
- **Zuständigkeit falsch:** Fehlerhafte sachliche Zuständigkeit führt zur Verweisung (§ 281 ZPO) und Zeitverlust; Streitwertgrenzen (AG: bis EUR 10.000; LG: über EUR 10.000, § 23 Nr. 1 GVG i. d. F. seit 1.1.2026) prüfen.
- **Mandant ist Verbraucher – besondere Pflichten:** Informationspflichten nach § 43d BRAO (Kostenmitteilung), § 13 RVG (Vergütungsvereinbarung).

