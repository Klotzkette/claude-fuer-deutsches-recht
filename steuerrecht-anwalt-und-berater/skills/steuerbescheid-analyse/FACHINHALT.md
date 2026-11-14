---
name: steuerbescheid-analyse
description: "Für Steuerbescheid-Analyse: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen."
---

# Steuerbescheid-Analyse

## Fachlicher Anker

- **Normen:** § 6a, § 122 Abs. 2 AO, § 164 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — kläre vor der Analyse

1. Welche Steuerart und welches Veranlagungsjahr betrifft der Bescheid?
2. Liegt der Bescheid im Original vor (nicht nur Kopie oder Screenshot)?
3. Ist die Einspruchsfrist bereits abgelaufen? (Bekanntgabefiktion § 122 Abs. 2 AO — vier Tage seit 1.1.2025)
4. Wurde der Bescheid unter Vorbehalt der Nachprüfung (§ 164 AO) oder mit Vorläufigkeitsvermerk (§ 165 AO) erlassen? → andere Anpassungsmöglichkeiten
5. Liegt eine Außenprüfung zugrunde? → Schätzungsprobleme und Sicherheitszuschläge prüfen
6. Soll AdV beantragt werden? → Liquidität und Frist klären

## Eingaben

- Steuerbescheid (PDF Original; gescannt mit OCR).
- Steuererklärung des Veranlagungsjahres (zum Vergleich Soll-Ist).
- Bisheriger Mandatsstand.

## Prüfraster

### 1. Formale Prüfung

- **Behörde** zuständig (Wohnsitzfinanzamt § 19 AO; Betriebsstaettenfinanzamt § 18 AO)?
- **Adressat** korrekt (bei Eheleuten Zusammenveranlagung beide; bei Personengesellschaft gesonderte und einheitliche Feststellung — separater Bescheid)?
- **Steuerart** und **Veranlagungsjahr** klar?
- **Tenor** mit Steuerbetrag eindeutig?
- **Bekanntgabe** nach § 122 AO — Vier-Tages-Fiktion bei Postbescheiden (§ 122 Abs. 2 Nr. 1 AO n.F., seit 1.1.2025 PostModG; bei Aufgabe zur Post vor dem 1.1.2025: weiterhin Drei-Tages-Fiktion alter Fassung).
- **Rechtsbehelfsbelehrung** vollständig?

### 2. Inhaltliche Prüfung

- **Berechnung** der Steuer nachvollziehbar?
- **Einkünftearten** richtig zugeordnet (§§ 2 13–24 EStG)?
- **Werbungskosten / Betriebsausgaben** vollständig abgezogen?
- **Sonderausgaben Außergewöhnliche Belastungen** berücksichtigt?
- **Pauschalen** richtig?
- **Vorauszahlungen** richtig angerechnet (§ 36 EStG)?
- **Solidaritaetszuschlag Kirchensteuer** zutreffend?

### 3. Vorläufigkeit und Änderbarkeit

- **§ 164 AO** Vorbehalt der Nachprüfung — Bescheid jederzeit änderbar bis Festsetzungsverjährung.
- **§ 165 AO** Vorläufigkeitsvermerk — Bescheid teilweise vorläufig.
- **§ 172 ff. AO** Änderungsvorschriften nach Bestandskraft (z. B. § 173 neue Tatsachen § 175 Änderungsbescheid).
- **§ 129 AO** offenbare Unrichtigkeit (Schreib- Rechenfehler).

### 4. Schätzung (§ 162 AO)

Bei Schätzungsbescheid:
- Begründung für Schätzungsbefugnis (Nicht-Abgabe Erklärung verletzte Mitwirkungspflicht).
- Schätzungsgrundlagen schlüssig?
- Höhe wirtschaftlich plausibel?
- Sicherheitszuschlaege im Rahmen?

### 5. Festsetzungsverjährung

- **§ 169 AO** Festsetzungsfrist regelmäßig vier Jahre; bei Hinterziehung zehn Jahre; bei Leichtfertigkeit fünf Jahre.
- **§ 170 AO** Beginn — mit Ablauf des Kalenderjahrs in dem die Steuer entstanden ist; bei Erklärungspflicht mit Ablauf des Kalenderjahrs der Abgabe spätestens nach drei Jahren.

### 6. Vollziehung

- **Fälligkeit** der Steuerschuld (§ 220 AO).
- **Anordnung sofortiger Vollziehung** durch Steuerbehörde nicht erforderlich — Einspruch hat **keine aufschiebende Wirkung** (§ 361 Abs. 1 AO Satz 1). Daher Antrag auf Aussetzung der Vollziehung notwendig wenn nicht gezahlt werden soll.

## Ausgabe

Analyseprotokoll mit:

1. Stammdaten Bescheid (Behörde Az Steuerart Jahr Datum Zugang)
2. Festsetzungsbetrag Soll-Ist-Vergleich
3. Rechtsbehelfsbelehrung mit Einspruchsfrist (ein Monat § 355 Abs. 1 AO)
4. Formfehler
5. Angriffspunkte sortiert nach Erfolgsaussicht
6. Empfehlung: Einspruch / Antrag § 129 AO / Änderungsantrag / nichts
7. Antrag auf Aussetzung der Vollziehung erforderlich?
8. Frist im Fristenbuch eintragen (Skill `anw-fristenbuch-steuerrecht`)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
