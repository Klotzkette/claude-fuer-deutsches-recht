---
name: redteam-qualitygate
description: "Red-Team- und Qualitätsgate für patentrechtliche Outputs: prüft Fristen, Registerstand, Anspruchsfassung, technische Annahmen, Quellen, Beweise, Zitierhygiene, offene Tatsachen und Mandantenrisiken."
---

# Patentrecht Red Team

## Prüfe jeden Output gegen diese Fragen

1. **Fristen:** Ist eine harte Frist übersehen?
2. **Register:** Ist der Rechtsstand live geprüft oder klar als ungeprüft markiert?
3. **Anspruchsfassung:** Wird die geltende Fassung verwendet?
4. **Technik:** Sind Merkmale und Wirkungen sauber getrennt?
5. **Beweise:** Sind Produktbefunde, Vorbenutzung oder Offenbarung belegbar?
6. **Territory:** Passt das Land zur Rechtsfolge?
7. **Quellen:** Keine erfundenen Fundstellen, keine Paywall-Zitate als eigene Quelle.
8. **Alternativen:** Anmeldung, Recherche, FTO, Lizenz, Einspruch, Nichtigkeit, Design-around bedacht?
9. **Mandantenkommunikation:** Ergebnis verständlich, entscheidungsfähig, ohne Scheingenauigkeit?

## Output

- Red-Team-Liste mit `kritisch / wichtig / optional`.
- korrigierte Kurzfassung.
- offene Rückfragen.
- nächste Handlung.

## Harte Stopps

- Abmahnfrist läuft und wurde nicht zuerst behandelt.
- Unterlassungserklärung wird ohne Umfangsprüfung empfohlen.
- FTO-Ergebnis ohne Registerstand.
- Claim Draft ohne Offenbarungsstütze.
- Rechtsprechung ohne Datum, Aktenzeichen und verifizierbare Quelle.

## Patent-spezifische Falle-Checks

- **§ 34 PatG / Art. 83 EPÜ Offenbarung:** Jedes Anspruchsmerkmal hat Stütze in der Beschreibung; intermediate generalisation vermeiden.
- **§ 38 PatG / Art. 123 (2) EPÜ Erweiterungsverbot:** Nachträgliche Änderungen dürfen Offenbarung nicht überschreiten.
- **§ 14 PatG / Art. 69 EPÜ Schutzbereich:** Wortsinn vor Äquivalenz; BGH "Schneidmesser"-Drittest (Wirkung/Auffindbarkeit/Gleichwertigkeit).
- **Frist § 59 PatG Einspruch:** 9 Monate ab Erteilung; danach nur noch Nichtigkeitsklage (§ 81 PatG).
- **§ 5 ArbEG Meldepflicht** beachtet, § 6 ArbEG In-Anspruchnahme dokumentiert, § 9 ArbEG Vergütung berechnet (Vergütungsrichtlinien)?
- **UPC vs. national:** Bei Einheitspatent UPC zentral; Opt-out für klassisches EP-Bundle prüfen.
- **DPMA-Registerstand abrufbar:** Datum des Abrufs in jeder Aussage festhalten.
- **Erfinderbenennung § 37 PatG:** richtig benannt? Sonst Vindikationsanspruch § 8 PatG.
- **Strategische Falle:** "Hat man auch an Vorbenutzungsrecht § 12 PatG gedacht?" — oft Schlüssel bei Verletzung gegen langjährig benutzte Lehre.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
