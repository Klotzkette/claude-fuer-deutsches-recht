---
name: forderungsschreiben-mahnung
description: "Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Schlichtung oder Klage zum Amtsgericht. Bei Reaktion der Airlin — Arbeitskontext: Fluggastrechte VO 261/2004, Schwerpunkt forderungsschreiben mahnung."
---

# Forderungsschreiben — Mahnung (zweite Stufe)

## Voraussetzung

Erstes Forderungsschreiben aus Skill `forderungsschreiben-erste-stufe` ist versendet — Frist ist abgelaufen oder Airline hat ablehnend reagiert.

## Struktur

```
Betreff: Mahnung — Forderung Ausgleichszahlung gemäß Art. 7 VO (EG)
 Nr. 261/2004 — Flug [Flugnummer] vom [Datum]
 Buchungscode [PNR]
 Mein voriges Schreiben vom [Datum erste Stufe]

Sehr geehrte Damen und Herren,

Sie haben auf mein Schreiben vom [Datum] [nicht reagiert / ablehnend
geantwortet]. Die hierin gestellten Forderungen sind weiterhin offen.

Zu Ihrer ablehnenden Begründung [bei Ablehnung]:

 "[Zitat Airline-Begründung]"

Diese Begründung verfaengt nicht. Bei [technischer Defekt / Streik der
eigenen Mitarbeiter / Crew-Engpass / sonstige Standardausrede] handelt es
sich nach ständiger EuGH-Rechtsprechung regelmäßig NICHT um
außergewöhnliche Umstaende im Sinn des Art. 5 Abs. 3 VO 261/2004:

 Bei technischem Defekt: EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — technische Defekte sind grundsaetzlich Teil der normalen Tätigkeit eines Luftfahrtunternehmens.
 [Volltext und Randnummer vor Versand in curia.europa.eu aufrufen
 und passende Aktenzeichen-Linie ergaenzen — z.B. bei Streik der
 eigenen Mitarbeiter EuGH-Linie, bei Personalmangel C-405/23
 (16.5.2024), bei Vorverlegung C-394/23 (9.1.2025).]

Die Beweislast für außergewöhnliche Umstaende und für die Ergreifung
aller zumutbaren Maßnahmen liegt bei Ihnen.

Ich setze hiermit eine letzte Frist zur Zahlung des offenen Betrags von

 [Gesamtbetrag] EUR
 zuzueglich Verzugszinsen seit [Datum erste Frist + 1] in Höhe von
 5 Prozentpunkten über dem Basiszinssatz gemäß § 288 Abs. 1 BGB

bis spaetestens [Datum + 10 Tage].

Sollten Sie die Zahlung nicht fristgerecht leisten werde ich:

 a) die Schlichtungsstelle für den öffentlichen Personenverkehr SOEP
 anrufen — kostenfrei für Verbraucher,
 b) anschliessend Klage zum zuständigen Amtsgericht erheben.

Im Klagefall werden Sie zudem die Gerichtskosten Anwaltskosten und alle
ueberfälligen Verzugszinsen zu tragen haben. Die sachliche Zuständigkeit
des Amtsgerichts ergibt sich aus § 23 Nr. 1 GVG bei Streitwerten bis
zehntausend Euro (i. d. F. seit 01.01.2026). Die oertliche Zuständigkeit
ergibt sich aus § 29 ZPO i.V.m. Art. 7 Nr. 1 lit. b VO (EU) 1215/2012
(Brüssel-Ia) wahlweise am Abflughafen oder am
Zielflughafen oder aus § 13 ZPO Ihrem Sitz / Niederlassung in Deutschland.

Mit freundlichen Grüßen

[Unterschrift]
[Name]
```

## Standard-Gegenargumente

Wenn die Airline mit einer typischen Begründung argumentiert siehe Skill
`airline-standardausreden-pruefen` — dort sind die EuGH-Pinpoints aufgelistet:

| Airline-Begründung | Kerngegenargument | Rspr. (offene Quelle curia.europa.eu) |
|---|---|---|
| "Technischer Defekt" | nicht außergewöhnlich | EuGH C-549/07 (Wallentin-Hermann, 22.12.2008) |
| "Crew-Engpass" | nicht außergewöhnlich | st. Rspr. — Teil normalen Betriebs |
| "Streik eigener Mitarbeiter" | nicht außergewöhnlich | EuGH-Linie zum Personal — konkrete Aktenzeichen in curia.europa.eu vor Versand verifizieren |
| "Vorverlegung um wenige Stunden" | bei mehr als 1 h: Annullierung | EuGH C-394/23 (9.1.2025); C-146/20 u.a. (21.12.2021) |
| "Sie haben uns nicht innerhalb von 30 Tagen informiert" | VO 261/2004 sieht keine solche Frist vor | Verjährung drei Jahre § 195 BGB |
| "Sie haben Umbuchung akzeptiert" | Akzeptanz schließt Ausgleichsanspruch nicht aus | EuGH ständig |
| "Sie haben Voucher erhalten" | wenn nicht ausdrücklich als Ausgleichszahlung gewidmet — kein Ausschluss | st. Rspr. |
| "Vorflug aus Vortag verspätet" | regelmäßig nicht außergewöhnlich (Kette aus Routine-Folge) | st. Rspr. EuGH |

## Versand

- **Einschreiben mit Rückschein** wie Erststufe.
- Parallel **E-Mail an Kundenservice** mit Bezugnahme auf die erste Mahnung.

## Nächster Schritt

- Bei weiterer Untätigkeit: **SOEP-Schlichtungsverfahren** oder **Klage** zum Amtsgericht.
- SOEP-Verfahren ist kostenfrei und oft erfolgreich. Voraussetzung: keine anhängige Klage.
- Klage als letzter Schritt — Skill `klage-amtsgericht-fluggast`.

## Ausgabe

- `mahnung-zweite-stufe-<datum>.docx` und PDF.
- Eintrag im Tagesplan — Reaktionsfrist gesetzt.

## Anlagen-Übergabe

Unmittelbar nach Erstellung des Schreibens den Skill `fluggastrechte-anlagen-bauen` aufrufen.

Übergabe-Schema:

```yaml
schriftsatz: mahnung-zweite-stufe-<datum>.docx
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold
bezeichnung: "Anlage K"
```

Wichtig: Die Mahnung nimmt regelmäßig dieselben Anlagen wie das Erstschreiben in Bezug **plus** das erste Forderungsschreiben selbst und ggf. die Antwort der Airline. Vor Übergabe sicherstellen, dass im Schriftsatz alle benötigten Anlagen mit "Anlage K N" benannt sind — der Skill zieht die Reihenfolge aus dem Text.

## Zentrale Anspruchsgrundlagen & Normen

- Art. 7 VO (EG) Nr. 261/2004 — Ausgleichszahlung 250/400/600 EUR je nach Distanz
- Art. 5 Abs. 3 VO (EG) Nr. 261/2004 — Entlastungsbeweis aussergewoehnliche Umstaende (Beweislast Airline)
- § 286 Abs. 1 BGB — Verzug bei fruchtlosem Fristablauf
- § 288 Abs. 1 BGB — Verzugszinsen 5 Prozentpunkte ueber Basiszinssatz
- § 195 BGB — Regelmäßige Verjährungsfrist drei Jahre
- § 199 Abs. 1 BGB — Verjährungsbeginn Schluss des Jahres der Kenntnis

## Aktuelle Rechtsprechung (Stand Mai 2026; offene Quelle curia.europa.eu)

- EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 (Sturgeon u.a.) — 3-Stunden-Schwelle
- EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — techn. Defekt kein außergewöhnlicher Umstand
- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspätung Anschlussflüge
- EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung als Annullierung
- EuGH, Urt. v. 13.6.2025, C-411/23 — versteckter Konstruktionsfehler Triebwerk
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag

## Triage vor Mahnung — Checkliste

1. Erste Stufe versendet und Frist abgelaufen? → Datum prüfen (typisch 14 Tage nach Erstschreiben)
2. Airline hat ablehnend geantwortet? → Antwort-Text kopieren und in Mahnung zitieren
3. Airline hat gar nicht geantwortet? → Hinweis auf Untätigkeit formulieren
4. Anspruch noch nicht verjährt? → § 195/199 BGB: drei Jahre ab Jahresende des Flugjahres
5. SOEP-Schlichtung bereits beantragt? → falls ja, Klage erst nach Abschluss

## Adressat & Tonfall

Adressat: Airline-Kundendienst / Rechtsabteilung — Tonfall scharf-fristsetzend, aber sachlich-juristisch; keine persönlichen Vorwuerfe
