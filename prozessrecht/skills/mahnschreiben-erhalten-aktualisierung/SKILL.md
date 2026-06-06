---
name: mahnschreiben-erhalten-aktualisierung
description: "Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwortschreiben auf Mahnschreiben. Abgrenzung: nicht Klageverteidigung im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Eingehendes Mahnschreiben / Abmahnung – Triage

## Arbeitsbereich

Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwortschreiben auf Mahnschreiben. Abgrenzung: nicht Klageverteidigung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Auswertung

1. **Schreibentyp:** Einfache Mahnung, Abmahnung (Wettbewerb/Urheberrecht), Forderungsschreiben eines Inkassos oder Klageankündigung?
2. **Frist:** Enthalt das Schreiben eine Zahlungsfrist oder Reaktionsfrist — wann läuft sie ab?
3. **Berechtigung:** Ist die behauptete Forderung dem Grunde und der Höhe nach berechtigt?
4. **Portfolio-Abgleich:** Liegt bereits ein Mandat oder ein Konflikt zu diesem Sachverhalt vor?
5. **Handlungspriorität:** Sofortige Reaktion (Unterlassung, Zahlung, Ablehnung) oder abwarten?

## Zentrale Normen
- § 286 BGB (Verzug durch Mahnung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)
- § 8 Abs. 1 UWG (Abmahnung im Wettbewerbsrecht)
- § 97a UrhG (Abmahnung im Urheberrecht)
- § 43a Abs. 1 BRAO (Interessenkonflikt bei eingehenden Forderungen)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Strukturierte Auswertung und Triage eingehender Mahnschreiben, Abmahnungen, Forderungsschreiben oder Klagedrohungen. Das Plugin extrahiert relevante Felder, prüft die Berechtigung der Forderung, gleicht mit dem Portfolio offener Mandate ab und erstellt eine priorisierte Handlungsübersicht mit Fristen.

## Eingaben

- Hochgeladenes oder einzufügendes Schreiben (Text, Scan, PDF)
- Optional: `--slug=custom-slug` für eigenes Aktenzeichen

## Ablauf

1. **Feldextraktion:**
 - Absender (Name, Kanzlei, Anschrift)
 - Empfänger (Mandant / Gesellschaft)
 - Datum des Schreibens
 - Aktenzeichen / Referenz des Absenders
 - Art des Schreibens (Mahnung, Abmahnung, Klagedrohung, Aufforderung zur Unterlassung, C&D-Äquivalent)
 - Geldforderung (Betrag, Währung, Fälligkeitsdatum)
 - Anspruchsgrundlage (soweit angegeben)
 - Gesetzte Frist (Datum extrahieren; wenn "2 Wochen ab Zugang" oder ähnlich: Frist anhand des Schreibdatums + Postlaufzeit schätzen)

2. **Portfolio-Abgleich:** Prüfen, ob zu Absender / Sachverhalt bereits ein Mandat in `mandate/_log.yaml` existiert. Wenn ja: Verknüpfung herstellen und History-Update vorschlagen.

3. **Berechtigungsprüfung (Kurzanalyse):**
 - Besteht das behauptete Schuldverhältnis dem Grunde nach?
 - Ist die Forderung bezifferbar und plausibel?
 - Sind Verjährungseinwände (§§ 195, 199 BGB) offensichtlich möglich?
 - Stehen Gegenansprüche (Aufrechnung § 387 BGB, Zurückbehaltungsrecht § 273 BGB) im Raum?
 - Besteht Verdacht auf unberechtigte Abmahnung (§ 8c UWG, § 97a Abs. 4 UrhG)?
 - Ist die Abmahnung formell vollständig (Unterlassungserklärung, Vertragsstrafe, Vollmacht)?

4. **Risikoeinschätzung:** Ampelschema:
 - 🔴 Hohe Berechtigung / akute Frist – sofortiger Handlungsbedarf
 - 🟡 Mittlere Berechtigung / prüfungsbedürftig
 - 🟢 Geringe Berechtigung / defensiv haltbar

5. **Handlungsoptionen mit Empfehlung:**
 - (a) Zahlung / Erfüllung (mit Vorbehalten)
 - (b) Modifizierte Unterlassungserklärung (bei Abmahnung)
 - (c) Abwehr / Zurückweisung mit Begründung
 - (d) Verhandlung / Vergleichsgespräch
 - (e) Schutzschrift hinterlegen (§ 945a ZPO) bei Gefahr einstweiliger Verfügung
 - (f) Mandat-Intake → neues Mandat anlegen

6. **Fristen-Alarm:**
 - Antwortfrist aus Schreiben extrahieren und als absolute Frist eintragen
 - Verjährungshemmung durch Verhandlung (§ 203 BGB) oder Mahnbescheid (§ 204 Abs. 1 Nr. 3 BGB) als Optionen nennen

7. **Datei speichern:** `inbound/[JJJJ-MM-TT]-[slug].md`

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8c Rn. 5 ff. (missbräuchliche Abmahnung).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
EINGEHENDES SCHREIBEN – TRIAGE-BERICHT
Slug: [automatisch generiert]
Datum Eingang: TT.MM.JJJJ
Absender: [Kanzlei / Gläubiger]
Art: [Mahnung | Abmahnung | Klagedrohung]

──────────────────────────────────────
KERNFELDER
──────────────────────────────────────
Forderungsbetrag: EUR X.XXX,XX
Anspruchsgrundlage: § 280 Abs. 1, 3, § 281 BGB
Frist gesetzt bis: TT.MM.JJJJ
Konsequenz: Klageandrohung

──────────────────────────────────────
RISIKOEINSCHÄTZUNG: 🟡 MITTEL
──────────────────────────────────────
Begründung: Forderung dem Grunde nach plausibel;
Zugang der Fristsetzung unklar; Verjährung prüfen.

──────────────────────────────────────
HANDLUNGSOPTIONEN
──────────────────────────────────────
Empfehlung: (c) Abwehr – fehlender Verjährungsverzicht
Alternativen: (d) Verhandlung, (e) Schutzschrift

──────────────────────────────────────
FRISTEN
──────────────────────────────────────
⚠️ Antwortfrist: TT.MM.JJJJ
📅 Verjährungsende: 31.12.JJJJ (§§ 195, 199 BGB)
```

## Risiken / typische Fehler

- **Fristüberschreitung:** Bei Abmahnungen im UWG/UrhG ist die Frist oft sehr kurz (3–10 Tage); plug-in markiert Schreiben mit kurzem Frist-Alert.
- **Schutzschrift vergessen:** Bei drohender einstweiliger Verfügung (z. B. Wettbewerbsrecht, Markenrecht) sofortige Schutzschrift-Hinterlegung im Zentralen Schutzschriftenregister (ZSSR, § 945a ZPO) erwägen.
- **Kostenfalle § 93 ZPO:** Wenn Berechtigung klar, Zahlung / Unterlassungserklärung vor Klagezustellung prüfen; sonst trägt Beklagter Kosten trotz sofortigem Anerkenntnis.
- **Unvollständige Vollmacht:** Abmahnung ohne beigefügte Vollmacht ist zurückweisbar (§ 174 BGB); Zurückweisung unverzüglich erklären.
