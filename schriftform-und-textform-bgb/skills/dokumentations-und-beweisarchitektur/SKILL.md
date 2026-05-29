---
name: dokumentations-und-beweisarchitektur
description: "Anwalt oder Kanzlei muss sicherstellen dass Formerklärungen beweissicher dokumentiert und archiviert werden. Beweissicherung Willenserklärungen Formrecht. Prüfraster: Zugang § 130 BGB nachweisen Originalurkunden aufbewahren qES-Validierungsprotokolle ersetzendes Scannen TR-RESISCAN Langzeitarchivierung. Output: Kanzlei-Dokumentationsstandard-Checkliste für formrelevante Vorgaenge. Abgrenzung zu zugang-empfangsbedürftiger-willenserklärung-paragraph-130-bgb (Zugangsprüfung) und elektronische-form-paragraph-126a-bgb-qes."
---

# Dokumentations- und Beweisarchitektur

## Triage — kläre vor der Dokumentation

1. **Erklärungsart:** Welche Willenserklärung oder welcher Vertragsschluss soll beweissicher dokumentiert werden (Kündigung, Bürgschaft, Mietvertrag)?
2. **Formerfordernis:** Gilt Schriftform (§ 126 BGB), Textform (§ 126b BGB), qES (§ 126a BGB) oder Formfreiheit?
3. **Zugangsbeleg:** Wie wird der Zugang beim Empfänger nachgewiesen (Bote, Einschreiben, qES-Protokoll)?
4. **Archivierungspflicht:** Wie lange müssen die Unterlagen aufbewahrt werden (steuerlich, handelsrechtlich, prozessual)?
5. **Ersatz-Scan:** Soll die Originalurkunde nach TR-RESISCAN eingescannt und vernichtet werden?

## Zentrale Normen (ergänzend)
- § 127 BGB (Abweichende Formvorschriften)
- § 415 ZPO (Beweiskraft öffentlicher Urkunden)
- § 416 ZPO (Beweiskraft privater Urkunden)
- § 419 ZPO (Vorlegungspflicht für Urkunden)
- § 420 ZPO (Pflicht zur Urkundenvorlage — Originalpflicht)
- § 257 HGB (Aufbewahrungspflichten kaufmännischer Unterlagen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rechtsgrundlagen

- **§ 130 BGB** — Zugang: Beweislast beim Erklärenden
- **§ 416 ZPO** — Privaturkunde: voller Beweis für Echtheit der Unterschrift bei Anerkennung
- **§ 440 ZPO** — Echtheitsbezeugung öffentlicher Urkunden
- **TR-RESISCAN** — BSI Technische Richtlinie 03138: ersetzendes Scannen von Papierdokumenten
- **eIDAS-Verordnung** VO (EU) Nr. 910/2014 — qualifizierte elektronische Signatur
- **§ 298 Abs. 3 ZPO** — Transfervermerk bei Gerichtsausdrucken (kein Zugangsersatz)

## BGH-Linie

### Beweislast Zugang

Der Erklärende trägt die Beweislast für den Zugang seiner Willenserklärung beim Empfänger (BGH-Dauerrechtsprechung). Kommt es zum Streit über den Zugang, muss der Erklärende beweisen:
- Dass die Erklärung abgeschickt wurde
- Dass sie im Machtbereich des Empfängers eingegangen ist
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Originalurkunde und Beweiskraft

**§ 416 ZPO**: Privaturkunden, die die Unterschrift des Ausstellers tragen, begründen vollen Beweis dafür, dass die Erklärung so abgegeben wurde, wenn die Echtheit der Unterschrift vom Empfänger anerkannt oder nachgewiesen wird.

**Originalurkunde**: Für den Beweis ist die Vorlage des Originals (§ 420 ZPO) in der Regel erforderlich, nicht lediglich einer Kopie.

## Workflow

### Dokumentations-Standards für formrelevante Erklärungen

```
PAPIER-ERKLÄRUNGEN:

□ Original-Exemplar erstellt und unterschrieben?
   → Vermieter bei Kündigung: eine Original-Kündigung, zugestellt an Mieter
   → Bei Vertrag: Original-Exemplar für jede Partei

□ Gegenstück-Exemplar aufbewahrt?
   → Kopie oder zweites Originalexemplar in Mandantenakte
   → Ggf. beglaubigte Kopie

□ Zugangs-Nachweis gesichert?
   → Boten-Quittung mit Unterschrift und Datum
   → Einschreiben-Rückschein (Sendebericht + Rückschein)
   → GV-Zustellungsurkunde

□ Frist berechnet und dokumentiert?
   → Zugangsdatum + Frist = Fristende
   → In Akte notiert

ELEKTRONISCHE ERKLÄRUNGEN (qES):

□ PDF/A-Datei mit eingebetteter qES erstellt?
□ Zertifikats-Gültigkeit zum Zeitpunkt der Signatur geprüft?
□ qES-Validierungsprotokoll erstellt (validator.bund.de o.ä.)?
□ Datei mit Validierungsprotokoll in Akte archiviert?
□ Datei elektronisch an Empfänger übermittelt (nicht ausgedruckt)?
□ Sendebericht / Auslieferungsnachweis E-Mail gesichert?
□ Eingangsbestätigung des Empfängers archiviert?
□ Datei-Hash dokumentiert (Integrität sichern)?

TEXTFORM (E-MAIL / WHATSAPP):

□ E-Mail mit Datum, Absender, Inhalt aus Postfach gesichert?
□ E-Mail als .eml oder PDF exportiert?
□ Bei WhatsApp: Screenshot und Chat-Export gesichert?
□ Lesebestätigung / Antwort des Empfängers archiviert?
```

### qES-Validierungsprotokoll erstellen

**Schritt-für-Schritt Validierung**:
- Dokument auf validator.bund.de hochladen (Prüfdienst der Bundesverwaltung)
- Alternativ: Adobe Acrobat, DocuSign-Validierung, eigene eIDAS-Prüftools
- Validierungsprotokoll als PDF herunterladen
- Protokoll enthält: Signaturstatus, Zertifikat, Zeitpunkt, Integrität
- Protokoll zusammen mit dem signierten Dokument in Akte aufbewahren

### Ersatz-Scanning und TR-RESISCAN

Wenn Papierurkunden eingescannt und die Originale vernichtet werden sollen (ersetzendes Scannen):
- BSI Technische Richtlinie TR-RESISCAN (BSI TR-03138) beachten
- Scan muss vollständig und originalgetreu sein
- Transfervermerk auf Scan (Datum des Einscannens, Vollständigkeit)
- Bei formrelevanten Urkunden empfiehlt sich die Aufbewahrung des Originals
  → Insbesondere: Originalkündigung, Bürgschaftsurkunde, Originalunterschrift

**Achtung**: Ersetzendes Scannen ist für formrelevante Urkunden mit Vorsicht zu behandeln. Wenn das Original vernichtet wird, kann der Nachweis der Echtheit der Unterschrift schwieriger werden.

## Templates

### Akte-Deckblatt für formrelevante Erklärungen

```
FORMRELEVANTE ERKLÄRUNG — DOKUMENTATION

Mandant:         [Name]
Sache:           [Beschreibung]
Erklärung:       [Art der Erklärung, z. B. Kündigung Wohnraummiete]
Datum:           [Datum der Erklärung]
Form:            [ ] Schriftform Papier
                 [ ] qES elektronisch
                 [ ] Textform E-Mail / WhatsApp

Zugang gesichert durch:
  [ ] Boten-Quittung vom [Datum]
  [ ] Einschreiben-Rückschein vom [Datum]
  [ ] Eingangsbestätigung Empfänger vom [Datum]
  [ ] Sendebericht E-Mail vom [Datum]

Dokumente in Akte:
  [ ] Originalurkunde / Kopie
  [ ] Quittung / Rückschein
  [ ] qES-Validierungsprotokoll
  [ ] E-Mail-Export (.eml oder PDF)
  [ ] Screenshot WhatsApp

Fristberechnung:
  Zugang: [Datum]        Frist: [Anzahl Tage/Monate]        Fristende: [Datum]
```

### Mandantenhinweis Beweissicherung

```
Wichtig: Sichern Sie den Nachweis wichtiger Erklärungen

Für rechtlich relevante Erklärungen (Kündigung, Widerruf, Mahnung, Vertragsabschluss)
gilt: Sie tragen die Beweislast dafür, dass die Erklärung dem Empfänger zugegangen ist.

Bitte sichern Sie daher:
- Boten-Quittungen und Einschreiben-Rückscheine
- Ausdrucke oder Exports von E-Mails mit Datum und Absender
- Screenshots und Chat-Exports von WhatsApp-Nachrichten
- Eingangsbestätigungen des Empfängers

Bei qES-Dokumenten: Sichern Sie die digitale Datei mit eingebetteter Signatur
und das Validierungsprotokoll — löschen Sie die Datei nicht.

Bitte leiten Sie alle diese Unterlagen zeitnah an unsere Kanzlei weiter.
```

## Fallstricke

- **Original vernichtet**: Wird das Original einer Kündigung oder Bürgschaft vernichtet, kann der Nachweis der Echtheit der Unterschrift erheblich schwieriger werden — auch wenn ein Scan vorhanden ist.
- **qES-Datei gelöscht**: Wenn die qES-PDF-Datei gelöscht wird und nur ein Ausdruck vorhanden ist, ist die Signatur nicht mehr prüfbar. Validierungsprotokoll vor Löschung erstellen.
- **E-Mail-Postfach gelöscht**: E-Mails im Spam-Ordner werden automatisch gelöscht. Wichtige E-Mails sofort in gesicherten Ordner oder in Aktenstruktur verschieben.
- **Fristbeginn unbekannt**: Wenn das genaue Zugangsdatum streitig ist, kann die Fristberechnung scheitern. Zugang immer mit Datum dokumentieren.

## Querverweise

- → `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb`
- → `prozessablauf-papier-vs-elektronisch`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`

---

<!-- AUDIT-HINWEIS 27.05.2026: Halluzinierte BGH-Zitate entfernt (NOT_FOUND oder WRONG_TOPIC gemaess dejure.org-Pruefung). Betroffene AZ siehe inline-Kommentare. Frontmatter unveraendert. -->