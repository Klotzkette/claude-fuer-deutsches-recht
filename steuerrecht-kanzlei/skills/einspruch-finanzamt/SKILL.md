---
name: einspruch-finanzamt
description: Entwirft einen begruendeten Einspruch gegen einen Steuerbescheid nach §§ 347 ff. AO. Frist ein Monat nach Bekanntgabe (§ 355 Abs. 1 AO; ein Jahr bei fehlender Rechtsbehelfsbelehrung § 356 AO). Einspruchsbefugnis (§ 350 AO) Adressat (Finanzamt das den Bescheid erlassen hat § 357 AO) Form (schriftlich elektronisch oder zur Niederschrift). Inkludiert hilfsweisen Antrag auf Aussetzung der Vollziehung (§ 361 Abs. 2 AO) und Antrag auf Akteneinsicht.
---

# Einspruch beim Finanzamt

## Eingaben

- Analyseprotokoll aus `steuerbescheid-analyse`.
- Steuererklärung des Veranlagungsjahres und Belege.
- Bescheid im Original.

## Struktur

### 1. Rubrum

- Einspruchsführer (Steuerpflichtiger) mit Anschrift und Steuernummer.
- Vertreter (RA mit beA-Adresse).
- Empfangsfinanzamt mit Aktenzeichen / Steuernummer.
- Bezug: Bescheid vom (Datum) über (Steuerart) (Veranlagungsjahr).

### 2. Antrag

"Hiermit lege ich Einspruch gegen den Bescheid vom (Datum) über (Steuerart) (Jahr) ein und beantrage:

1. den angefochtenen Bescheid aufzuheben;
2. die Steuer wie folgt festzusetzen: ... EUR;
3. hilfsweise Aussetzung der Vollziehung gemäß § 361 Abs. 2 AO;
4. Akteneinsicht in die Steuerakten gemäß § 364 AO im Einspruchsverfahren."

### 3. Begründung

- Formale Mangel zuerst (Bekanntgabe Begründung Adressat).
- Materielle Mangel:
  - Sachverhaltsfehler (Einkünftezuordnung Werbungskosten Sonderausgaben Außergewöhnliche Belastungen).
  - Rechtsanwendungsfehler.
  - Schätzung unrealistisch (§ 162 AO).
- BFH-Rechtsprechung mit Pinpoint.
- Verweis auf BMF-Schreiben falls einschlägig.
- Bei Schätzungsbescheid: bestreitete Schätzungsgrundlagen plus eigene plausible Berechnung.

### 4. Belege

- Anlagen mit Sigel E1 E2 E3.
- Vollständige Belegliste (Belegart Datum Inhalt).

### 5. Form und Frist

- **Frist** ein Monat nach Bekanntgabe (§ 355 Abs. 1 AO).
- **Drei-Tages-Fiktion** § 122 Abs. 2 Nr. 1 AO bei Postbescheiden.
- **Form** schriftlich elektronisch (beA / De-Mail / qualifizierte elektronische Signatur) oder zur Niederschrift.
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr (§ 356 AO).

### 6. Aussetzung der Vollziehung

Hilfsantrag im Einspruchsschreiben:

"Hilfsweise wird die Aussetzung der Vollziehung gemäß § 361 Abs. 2 AO beantragt. Es bestehen ernstliche Zweifel an der Rechtmäßigkeit des angefochtenen Bescheids; die Vollziehung würde für den Steuerpflichtigen eine unbillige nicht durch überwiegende öffentliche Interessen gebotene Härte zur Folge haben."

Bei Ablehnung Antrag durch FA: Antrag an Finanzgericht § 69 Abs. 3 FGO (siehe Skill `aussetzung-vollziehung`).

### 7. Akteneinsicht

Im Einspruchsverfahren Anspruch nach § 364 AO Steuerakten und Akten der Außenprüfung.

## Verfahrensgang

1. **Einspruch eingelegt** → Finanzamt prüft.
2. **Hinweis nach § 367 Abs. 2 AO** wenn das FA die Steuer verboesern (Verschlechtern) will → der Einspruch kann zurückgenommen werden um Verboeserung zu vermeiden.
3. **Einspruchsentscheidung** mit Rechtsbehelfsbelehrung → bei Ablehnung Klage zum FG (Skill `klage-finanzgericht`).
4. **Untätigkeit** des FA: nach sechs Monaten kann Klage erhoben werden (§ 46 FGO).

## Ausgabe

- `einspruch-<az>-<datum>.docx` und Markdown-Spiegel.
- Eintrag im Fristenbuch.
- Eintrag im Postausgang.

## Versand

Über beA (RA-Pflicht). Vor Versand `versand-vor-check` aus `kanzlei-cowork`.
