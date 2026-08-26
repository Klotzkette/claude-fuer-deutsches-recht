---
name: mahnschreiben-erhalten-aktualisierung
description: "Für Eingehendes Mahnschreiben / Abmahnung – Triage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Eingehendes Mahnschreiben / Abmahnung – Triage

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
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
- Paragraf 286 BGB (Verzug durch Mahnung)
- Paragraf 203 BGB (Verjährungshemmung durch Verhandlungen)
- Paragraf 8 Abs. 1 UWG (Abmahnung im Wettbewerbsrecht)
- Paragraf 97a UrhG (Abmahnung im Urheberrecht)
- Paragraf 43a Abs. 1 BRAO (Interessenkonflikt bei eingehenden Forderungen)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
 - Sind Verjährungseinwände (Paragrafen 195, 199 BGB) offensichtlich möglich?
 - Stehen Gegenansprüche (Aufrechnung Paragraf 387 BGB, Zurückbehaltungsrecht Paragraf 273 BGB) im Raum?
 - Besteht Verdacht auf unberechtigte Abmahnung (Paragraf 8c UWG, Paragraf 97a Abs. 4 UrhG)?
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
 - (e) Schutzschrift hinterlegen (Paragraf 945a ZPO) bei Gefahr einstweiliger Verfügung
 - (f) Mandat-Intake → neues Mandat anlegen

6. **Fristen-Alarm:**
 - Antwortfrist aus Schreiben extrahieren und als absolute Frist eintragen
 - Verjährungshemmung durch Verhandlung (Paragraf 203 BGB) oder Mahnbescheid (Paragraf 204 Abs. 1 Nr. 3 BGB) als Optionen nennen

7. **Datei speichern:** `inbound/[JJJJ-MM-TT]-[slug].md`

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, Paragraf 8c Rn. 5 ff. (missbräuchliche Abmahnung).
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
Anspruchsgrundlage: Paragraf 280 Abs. 1, 3, Paragraf 281 BGB
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
📅 Verjährungsende: 31.12.JJJJ (Paragrafen 195, 199 BGB)
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Risiken / typische Fehler

- **Fristüberschreitung:** Bei Abmahnungen im UWG/UrhG ist die Frist oft sehr kurz (3–10 Tage); plug-in markiert Schreiben mit kurzem Frist-Alert.
- **Schutzschrift vergessen:** Bei drohender einstweiliger Verfügung (z. B. Wettbewerbsrecht, Markenrecht) sofortige Schutzschrift-Hinterlegung im Zentralen Schutzschriftenregister (ZSSR, Paragraf 945a ZPO) erwägen.
- **Kostenfalle Paragraf 93 ZPO:** Wenn Berechtigung klar, Zahlung / Unterlassungserklärung vor Klagezustellung prüfen; sonst trägt Beklagter Kosten trotz sofortigem Anerkenntnis.
- **Unvollständige Vollmacht:** Abmahnung ohne beigefügte Vollmacht ist zurückweisbar (Paragraf 174 BGB); Zurückweisung unverzüglich erklären.
