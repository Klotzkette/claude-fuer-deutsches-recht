---
name: prozessablauf-papier-vs-elektronisch
description: "Kanzlei oder Mandant muss zwischen Papier, qES, Textform, beA-Schriftsatz oder Formfiktion wählen. Prüft Originalunterschrift, qES-Direktversand, § 130e ZPO, § 46h ArbGG, Textform per E-Mail, Zustellung und Beweisarchitektur. Output: konkrete Prozessabläufe und Entscheidungsmatrix im Schriftform Und Textform Bgb."
---

# Prozessablauf — Papier vs. Elektronisch

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor dem Workflow

1. **Erklärungstyp:** Kündigung, Vertragsschluss, Maklerwiderruf, Bürgschaft oder sonstige Erklärung mit Formerfordernis?
2. **Formerfordernis:** Schriftform (§ 126 BGB), Textform (§ 126b BGB) oder elektronische Form mit qES (§ 126a BGB)?
3. **Empfänger und Weg:** Direktzustellung, E-Mail, beA/EGVP, gerichtliche Zustellung oder Mitteilung?
4. **Zugangsrisiko:** Welcher Versandweg bietet den sichersten Zugangsbeweis (Bote, Einschreiben/Rückschein, qES-Protokoll)?
5. **Dringlichkeit:** Gilt eine Frist, bei der der Zugang beweissicher vor Fristablauf erfolgen muss?

## Zentrale Normen (ergänzend)
- § 126 BGB (Schriftform — Originalunterschrift)
- § 126a BGB (Elektronische Form — qES)
- § 126b BGB (Textform — dauerhafter Datenträger)
- § 127 BGB (Vertragliche Formvorschriften)
- § 130 BGB (Zugang empfangsbeduerftiger Willenserklärungen)
- § 130a ZPO (elektronisches Dokument im Zivilprozess)
- § 130e ZPO (Formfiktion bei elektronischen vorbereitenden Schriftsätzen)
- § 46h ArbGG (arbeitsgerichtliche Formfiktion)
- § 371a ZPO (Beweiskraft elektronischer Dokumente mit qES)

## Rechtsprechung
Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtsgrundlagen

- §§ 126-126b BGB — Formvorschriften
- § 130 BGB — Zugang
- §§ 130a, 130e ZPO — elektronischer Schriftsatz und Formfiktion
- § 46h ArbGG — arbeitsgerichtliche Formfiktion
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Referenzanker: `references/amtlicher-formkern-bgb-zpo.md`
- Fachmodul: `amtlicher-formkern-bgb-zpo-check`

## Workflow

### Prozess A — Papierdokument mit Originalunterschrift (klassischer Weg)

```
Schritt 1: Dokument erstellen
 → Vertragstext / Kündigung / Bürgschaft auf Papier erstellen
 → Ggf. in zwei gleichlautenden Exemplaren (bei Vertragsabschluss)

Schritt 2: Unterschrift
 → Eigenhändige Unterschrift mit Kugelschreiber oder Füller
 → Unterschrift räumlich unter dem gesamten Text
 → Bei Vertrag: beide Parteien auf demselben oder auf gleichlautenden Exemplaren

Schritt 3: Übergabe / Versand
 Option A — Bote (sicherste Methode):
 → Bote (ggf. angestellte Person oder Gerichtsvollzieher) übergibt Original
 → Empfänger unterschreibt Quittung oder Zeuge bestätigt Übergabe
 → Quittung / Zeugenprotokoll in Akte

 Option B — Einschreiben mit Rückschein:
 → Original einlegen, versiegeln, als Einschreiben/Rückschein aufgeben
 → Rückschein aufbewahren (beweist Übergabe, nicht Inhalt)
 → Kopie des Dokuments in Akte

 Option C — Gerichtlicher Gerichtsvollzieher (§ 132 BGB):
 → Bei streitigem Empfänger: Antrag auf Zustellung durch GV
 → Kostenpflichtig, aber höchster Beweiswert

Schritt 4: Zugang dokumentieren
 → Rückschein / Quittung / GV-Protokoll archivieren
 → Datum des Zugangs festhalten
```

### Prozess B — qES-Dokument (elektronische Form § 126a BGB)

```
Schritt 1: Dokument erstellen
 → Vertragstext als PDF/A erstellen (maschinenlesbares Format)
 → Alle Seiten nummerieren

Schritt 2: Qualifizierte Signatur anbringen
 → Zugang zu qualifiziertem Vertrauensdiensteanbieter (z. B. D-Trust, Swisscom)
 → Signatur in die PDF-Datei einbetten (nicht: Bild der Unterschrift einfügen)
 → Zertifikats-Gültigkeit prüfen (Ablaufdatum, OCSP-Status)
 → Dokument als PDF/A-LTV speichern (Langzeitvalidierung)

Schritt 3: Elektronische Übermittlung
 → PDF-Datei als E-Mail-Anhang an Empfänger senden
 → NICHT ausdrucken — nur digitale Übermittlung wahrt Formwirksamkeit
 → In der E-Mail deutlichen Hinweis: "Rechtliches Dokument mit qES"
 → Bei mehreren Empfängern: für jeden Empfänger separate Zustellung

Schritt 4: Zugangssicherung
 → Eingangsbestätigung des Empfängers per Antwort-E-Mail anfordern
 → Sendebericht der E-Mail (Auslieferungsnachweis) sichern
 → Beide in Akte aufnehmen
 → Alternativ: Plattform mit Lesebestätigung nutzen

Schritt 5: qES-Validierungsprotokoll erstellen
 → Signatur des gesendeten Dokuments in Validierungstool prüfen
 → Validierungsbericht (validator.bund.de oder eIDAS-konformes Tool) in Akte
```

### Prozess B2 — beA-Schriftsatz mit Formfiktion

```
Schritt 1: Anwendungsbereich klären
 → Zivilprozess: § 130e ZPO
 → Arbeitsgericht: § 46h ArbGG
 → andere Prozessordnung: ausdrückliche Grundlage suchen

Schritt 2: Erklärung im Schriftsatz formulieren
 → Willenserklärung klar und unübersehbar aufnehmen
 → nicht nur Tatsachenvortrag oder Rechtsansicht
 → Erklärungsträger und Vertretung offenlegen
 → Vollmacht und § 174 BGB gesondert absichern

Schritt 3: elektronisch einreichen
 → qES oder einfache Signatur plus sicherer Übermittlungsweg
 → bei beA: Versandjournal und Prüfprotokoll sichern
 → Schriftsatz als vorbereitenden Schriftsatz einordnen

Schritt 4: Zustellung oder Mitteilung nachweisen
 → gerichtliche Zustellung, eEB oder Mitteilung dokumentieren
 → Datum und Empfänger eindeutig in der Akte erfassen
 → bei Alt-Fällen vor 17.07.2024 nicht rückwirkend mit § 130e arbeiten

Schritt 5: Ergebnis trennen
 → prozessual ordnungsgemäß eingereicht
 → materielle Form direkt durch qES oder fiktiv durch § 130e/§ 46h
 → Zugang und Fristbeginn dokumentiert
```

### Prozess C — Textform per E-Mail (§ 126b BGB)

```
Schritt 1: E-Mail verfassen
 → Absender klar erkennbar (Name in E-Mail-Adresse oder Signatur)
 → Inhalt der Erklärung vollständig im E-Mail-Text oder als Anhang
 → Abschluss der Erklärung erkennbar (Name, Datum, Grußformel)

Schritt 2: Versand
 → E-Mail an Empfänger senden
 → Bei wichtigen Erklärungen: Lesebestätigung anfordern

Schritt 3: Zugang sichern
 → Sendebericht archivieren (Datum/Uhrzeit des Eingangs im Empfänger-Postfach)
 → Antwort-E-Mail (Bestätigung) des Empfängers archivieren
 → Screenshot der gesendeten E-Mail in Akte

Schritt 4: Physische Sicherung der E-Mail
 → E-Mail-Thread aus Postfach exportieren (z. B. .eml oder PDF-Export)
 → In Mandantenakte archivieren
```

### Prozess D — WhatsApp-Textform (§ 126b BGB, Sicherung)

```
Schritt 1: WhatsApp-Nachricht senden
 → Name erkennbar (WhatsApp-Profil mit Vor-/Nachname)
 → Text vollständig und abgeschlossen

Schritt 2: Lieferbestätigung beachten
 → Doppelter Haken = zugestellt (Empfänger-Gerät)
 → Blauer Doppelhaken = gelesen

Schritt 3: Sicherung
 → Screenshot der Konversation mit sichtbarem Datum/Uhrzeit
 → In Mandantenakte ablegen
 → WhatsApp-Chat-Export (als .txt oder .zip) über "Chat exportieren"

Schritt 4: Risikobewertung
 → WhatsApp-Zugang schwer nachweisbar bei Streit
 → Bei wichtigen Erklärungen: zusätzlich E-Mail oder Papier
```

## Templates

### Entscheidungsmatrix Formwahl

| Rechtsgeschäft | Zwingend | Empfohlen | Elektronisch möglich? |
|---------------|----------|-----------|----------------------|
| Grundstückskauf | Notar | Notar | Nein |
| Gewerbemietvertrag >1 Jahr | Schriftform | Papier + Urkundeneinheit | qES möglich |
| Maklervertrag Wohnraum | Textform | E-Mail | Ja |
| Bürgschaft | Schriftform | Papier + Unterschrift | qES nur nach Spezialprüfung |
| Arbeitsbefristung | Schriftform | Papier vor Arbeitsbeginn | qES möglich, aber technisch streng |
| Kündigung Arbeitsvertrag | Schriftform | Papier | direkt elektronisch nein; § 46h ArbGG als Prozesspfad prüfen |
| Mieterhöhung | Textform | E-Mail | Ja |

### Musterschreiben Boten-Quittung

```
Empfangsquittung

Hiermit bestätige ich, [Name Empfänger], heute am [Datum] um [Uhrzeit] Uhr
von [Name Überbringer] folgendes Dokument erhalten zu haben:

[Bezeichnung des Dokuments, z. B. "Kündigung des Mietverhältnisses vom [Datum]"]

[Unterschrift Empfänger] [Unterschrift Überbringer]
[Datum]
```

## Fallstricke

- **qES per E-Mail und Spam**: Das qES-Dokument landet im Spam-Ordner des Empfängers — technisch zugegangen, aber Nachweis des Zugangs schwierig. Eingangsbestätigung ist unverzichtbar.
- **Papierausdruck des qES-Dokuments**: Wenn der Empfänger das qES-PDF ausdruckt, verliert die Signatur ihre Prüfbarkeit — das ist sein Problem, nicht das des Absenders. Aber: Beweislast für den Zugang trägt der Erklärende.
- **beA mit einfacher Signatur**: Prozessual kann das genügen; materiell trägt es nur über eine gesetzliche Formfiktion wie § 130e ZPO oder § 46h ArbGG.
- **Schriftsatzkündigung vor 17.07.2024**: Alt-Fälle dürfen nicht vorschnell nach § 130e ZPO gelöst werden. Dort bleibt die BGH-Linie zum prüfbaren qES-Zugang maßgeblich.
- **WhatsApp-Geräteaustausch**: Nach Gerätewechsel können WhatsApp-Nachrichten verloren gehen, wenn kein Backup aktiviert war. Für Beweiszwecke: Screenshots und Chat-Export sofort nach der Erklärung sichern.

