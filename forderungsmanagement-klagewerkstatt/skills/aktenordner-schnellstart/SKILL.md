---
name: aktenordner-schnellstart
description: "Aktenordner-Schnellstart fuer Forderungsakten: liest zuerst vorhandene Dokumente, Dateinamen und sichtbare Aktenlogik, rekonstruiert Parteien, Forderung, Zahlungen, Mahnstand, Fristen und naechsten Prozessschritt und fragt danach nur noch gezielte Luecken ab."
---

# Aktenordner-Schnellstart

Dieser Skill ist der erste Griff, wenn eine Forderungsakte bereits als Ordner, ZIP, PDF-Buendel, E-Mail-Stapel oder Dateisammlung vorliegt. Er startet nicht mit einem allgemeinen Interview, sondern mit einer Aktenlekture: erst sehen, dann fragen.

## Startregel

Wenn der Nutzer einen Ordner, eine ZIP-Datei oder mehrere Dokumente zeigt, arbeite zuerst die Akte aus. Stelle am Anfang keine Standardfragen wie "Wer bist du?" oder "Was ist dein Ziel?", solange sich diese Punkte aus Vollmacht, Anschreiben, Rechnung, Mahnung, Kontoauszug, Mahnbescheid, Widerspruch oder Klageentwurf erschliessen lassen.

Beginne mit:

```text
Ich lese zuerst die Akte und bilde eine Arbeitshypothese. Danach frage ich nur noch die Punkte ab, die nicht sicher aus den Unterlagen folgen.
```

Wenn keine Unterlagen vorliegen, frage nur:

```text
Bitte lade die Forderungsakte, den Rechnungs-/Mahnordner oder die wichtigsten Dokumente hoch. Ich starte danach mit einer Aktenhypothese.
```

## Akteninventar

Erstelle sofort eine kurze Tabelle:

| Fund | Beispiel | Bedeutung |
|---|---|---|
| Vollmacht / Mandatsmail | `Vollmacht.pdf`, `Mandat_*.eml` | Wer vermutlich Mandant ist |
| Vertrag / Bestellung | `Auftrag`, `Bestellung`, `AGB`, `Angebot` | Rechtsgrund der Forderung |
| Leistungsbeleg | `Lieferschein`, `Abnahme`, `Stundenzettel` | Erfuellung der eigenen Leistung |
| Rechnung / Gutschrift | `Rechnung`, `Korrektur`, `Storno` | Hauptforderung, Faelligkeit, Umsatzsteuer |
| Kontoauszug / Zahlungsavis | `Konto`, `Zahlung`, `SEPA`, `Teilzahlung` | Erfuellung, Restforderung, § 362 BGB |
| Mahnung / Anwaltsschreiben | `Mahnung`, `Frist`, `Inkasso` | Verzug, § 286 BGB, Nebenforderungen |
| gerichtliche Dokumente | `Mahnbescheid`, `Widerspruch`, `VB`, `Klage` | ZPO-Spur und laufende Fristen |
| Register / Auskunft | `HRB`, `EMA`, `Insolvenz` | richtige Partei, Zustellung, Insolvenzrisiko |

## Arbeitshypothese statt Fragebogen

Gib nach der ersten Aktenlekture diese fuenf Zeilen aus:

| Punkt | Arbeitshypothese | Beleg | Sicherheit |
|---|---|---|---|
| Mandant / Auftraggeber | z. B. Verkaeuferin ModeFuchs GmbH | Vollmacht, Briefkopf, Rechnung | hoch/mittel/niedrig |
| Gegner / Schuldner | Name, Rechtsform, Anschrift | Rechnung, Mahnung, Registerauszug | hoch/mittel/niedrig |
| Forderung | Hauptforderung, Nebenforderung, Zinsen | Rechnung, Kontoauszug, Mahnung | hoch/mittel/niedrig |
| Verfahrensstand | Erinnerung, Mahnung, Mahnbescheid, Klage, Titel | Aktenfund | hoch/mittel/niedrig |
| Engpass | z. B. Zahlung schon erfolgt, Verjaehrung, falscher Schuldner | Widerspruch, Zahlung, Frist | hoch/mittel/niedrig |

Nur Punkte mit `mittel` oder `niedrig` werden danach abgefragt.

## Maximal drei Startfragen

Stelle im ersten Dialogblock hoechstens drei Fragen. Nutze sie nur für echte Luecken oder Widersprueche:

1. **Rolle:** "Ich vermute, du vertrittst [Gläubiger/Schuldner]. Stimmt das?"
2. **Ziel:** "Soll ich Zahlung eintreiben, Forderung abwehren, Vergleich vorbereiten oder nur die Akte sortieren?"
3. **Frist:** "Gibt es eine Frist, die in den Unterlagen nicht erkennbar ist, z. B. Widerspruch, Einspruch, Verjaehrung oder gerichtliche Verfuegung?"

Alles andere wird aus der Akte rekonstruiert und später als Lueckenliste gefuehrt.

## Forderungslogik

Prüfe aus der Akte in dieser Reihenfolge:

1. **Anspruchsgrund:** Kaufpreis, Werklohn, Miete, Honorar, Darlehen, Schadensersatz, Abtretung.
2. **Faelligkeit:** § 271 BGB, besondere Vertragsfrist, Rechnungsvoraussetzung, Abnahme bei Werkvertrag § 641 BGB.
3. **Erfuellung:** Zahlungen, Aufrechnung, Gutschrift, Storno, § 362 BGB.
4. **Verzug:** Mahnung § 286 Abs. 1 BGB, kalendermassige Bestimmung § 286 Abs. 2 BGB, 30-Tage-Regel § 286 Abs. 3 BGB.
5. **Zinsen und Kosten:** § 288 BGB, § 280 BGB, § 286 BGB, vorgerichtliche Kosten nur bei tragfaehigem Verzug.
6. **Verjaehrung:** §§ 195, 199 BGB, Hemmung § 204 BGB.
7. **Verfahrensspur:** Mahnung, Mahnbescheid §§ 688 ff. ZPO, Zahlungsklage § 253 ZPO, Vollstreckungsbescheid §§ 699, 700 ZPO.
8. **Zustaendigkeit:** §§ 12 ff., 29 ZPO, § 23 Nr. 1 GVG, § 71 GVG, Sonderzustaendigkeiten.

## Ausgabe nach zehn Minuten Aktenarbeit

Liefere keinen langen Fragenkatalog, sondern ein Arbeitsbrett:

```text
1. Aktenbefund
2. Parteien und Rollen mit Belegstellen
3. Forderungsmatrix: Hauptforderung / Nebenforderungen / Zahlungen / Rest
4. Mahn- und Verfahrenschronologie
5. Fristenampel
6. Blocker und Beweisluecken
7. Naechster sinnvoller Skill: [Skillname]
8. Drei konkrete Rueckfragen, falls noetig
```

## Anschluss

- Belegchaos: `dokumente-intake`
- Forderung rechnerisch unklar: `forderungsaufnahme`
- Verjaehrung oder Fristdruck: `verjaehrung-pruefen`
- Zahlung schon erfolgt oder Nebenforderungen fraglich: `klagefreigabe-belegte-forderung`
- Mahnbescheid sinnvoll: `mahnbescheid-online`
- Klage reif: `zahlungsklage-erstellen`
- Vollstreckungstitel vorhanden: `zwangsvollstreckung-ueberblick`
