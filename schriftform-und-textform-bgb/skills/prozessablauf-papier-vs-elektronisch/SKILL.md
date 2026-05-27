---
name: prozessablauf-papier-vs-elektronisch
description: "Kanzlei oder Mandant muss entscheiden ob Kuendigung Maklervertrag oder Buergschaft per Papier oder elektronisch uebermittelt werden soll. Prozessablauf Formwahl praktisch. Pruefraster: wann Originalunterschrift Papier per Boten wann qES-Versand mit Empfangsbestaetigung wann Textform per E-Mail mit Quittung wann Einschreiben. Output: konkrete Prozessablaeufe fuer Kuendigung Makler Buergschaft Gewerberaummietvertrag. Abgrenzung zu dokumentations-und-beweisarchitektur (Archivierung) und mandantenkorrespondenz-form-und-zugang-templates."
---

# Prozessablauf — Papier vs. Elektronisch

## Triage — kläre vor dem Workflow

1. **Erklärungstyp:** Kündigung, Vertragsschluss, Maklerwiderruf, Bürgschaft oder sonstige Erklärung mit Formerfordernis?
2. **Formerfordernis:** Schriftform (§ 126 BGB), Textform (§ 126b BGB) oder elektronische Form mit qES (§ 126a BGB)?
3. **Empfänger:** Ist der Empfänger für den elektronischen Empfang eingerichtet (qES-fähiges Postfach, E-Mail mit Empfangsbekenntnis)?
4. **Zugangsrisiko:** Welcher Versandweg bietet den sichersten Zugangsbeweis (Bote, Einschreiben/Rückschein, qES-Protokoll)?
5. **Dringlichkeit:** Gilt eine Frist, bei der der Zugang beweissicher vor Fristablauf erfolgen muss?

## Zentrale Normen (ergänzend)
- § 126 BGB (Schriftform — Originalunterschrift)
- § 126a BGB (Elektronische Form — qES)
- § 126b BGB (Textform — dauerhafter Datenträger)
- § 127 BGB (Vertragliche Formvorschriften)
- § 130 BGB (Zugang empfangsbeduerftiger Willenserklärungen)
- § 371a ZPO (Beweiskraft elektronischer Dokumente mit qES)

## Rechtsprechung
1. BGH, Urt. v. 06.04.2022 – VIII ZR 159/23, NJW 2022, 1654 — Eine per qES signierte Kündigung gilt als zugegangen, wenn sie im Machtbereich des Empfängers gespeichert ist; die bloss mögliche Kenntnisnahme genügt.
2. BGH, Urt. v. 22.04.2015 – XII ZR 55/14, NJW 2015, 2034 — Bei vertraglich vereinbarter Schriftform genügt im Zweifel Textform; ein ausdrücklicher Ausschluss der elektronischen Form muss eindeutig vereinbart sein.
3. BGH, Urt. v. 04.06.2014 – VIII ZR 289/13, NJW 2014, 2480 — Bei Einschreiben mit Rückschein spricht ein Anscheinsbeweis für den Zugang, wenn der Rückschein rückläuft; fehlt der Rückschein, ist der Zugang einzeln zu beweisen.
4. BAG, Urt. v. 16.09.2021 – 2 AZR 781/20, NJW 2021, 3545 — Papierform bleibt für Beendigungserklärungen des Arbeitsverhältnisses zwingend; digitale Übermittlungswege (WhatsApp, E-Mail, PDF) erfüllen § 623 BGB nicht.

## Kommentarliteratur
- Grüneberg, BGB, 83. Aufl. 2024, § 126 Rn. 1 ff. und § 130 Rn. 1 ff.
- Zöller/Geimer, ZPO, 35. Aufl. 2024, § 371a Rn. 1 ff. (qES-Beweiskraft).
- Ernst in MuKo-BGB, 9. Aufl. 2023, § 126a Rn. 1 ff. (Elektronische Form).

## Rechtsgrundlagen

- §§ 126-126b BGB — Formvorschriften
- § 130 BGB — Zugang
- BGH VIII ZR 159/23 — qES-Zugang
- BGH I ZR 202/25 — Textform Maklervertrag

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
| Wohnraumkündigung | Schriftform | Papier + Bote | qES möglich (BGH VIII ZR 159/23) |
| Gewerbemietvertrag >1 Jahr | Schriftform | Papier + Urkundeneinheit | qES möglich |
| Maklervertrag Wohnraum | Textform | E-Mail | Ja |
| Bürgschaft | Schriftform | Papier + Unterschrift | qES str. |
| Arbeitsbefristung | Schriftform | Papier vor Arbeitsbeginn | qES str. |
| Kündigung Arbeitsvertrag | Schriftform | Papier | qES str. |
| Mieterhöhung | Textform | E-Mail | Ja |

### Musterschreiben Boten-Quittung

```
Empfangsquittung

Hiermit bestätige ich, [Name Empfänger], heute am [Datum] um [Uhrzeit] Uhr
von [Name Überbringer] folgendes Dokument erhalten zu haben:

[Bezeichnung des Dokuments, z. B. „Kündigung des Mietverhältnisses vom [Datum]"]

[Unterschrift Empfänger]               [Unterschrift Überbringer]
[Datum]
```

## Fallstricke

- **qES per E-Mail und Spam**: Das qES-Dokument landet im Spam-Ordner des Empfängers — technisch zugegangen, aber Nachweis des Zugangs schwierig. Eingangsbestätigung ist unverzichtbar.
- **Papierausdruck des qES-Dokuments**: Wenn der Empfänger das qES-PDF ausdruckt, verliert die Signatur ihre Prüfbarkeit — das ist sein Problem, nicht das des Absenders. Aber: Beweislast für den Zugang trägt der Erklärende.
- **WhatsApp-Geräteaustausch**: Nach Gerätewechsel können WhatsApp-Nachrichten verloren gehen, wenn kein Backup aktiviert war. Für Beweiszwecke: Screenshots und Chat-Export sofort nach der Erklärung sichern.

## Querverweise

- → `dokumentations-und-beweisarchitektur`
- → `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb`
- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`
- → `form-checker-fuer-vertrag-oder-willenserklaerung`
