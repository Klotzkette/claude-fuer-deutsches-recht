---
name: klagefreigabe-belegte-forderung
description: "Pruefraster ob eine Forderung klagefaehig ist. Verlangt Belegnachweis Faelligkeit Verzug Verjährung Zustellfaehigkeit und positive Aussicht. Pinpoints ZPO 253 ZPO 138 BGB 286 BGB 195 BGB 199 ZPO 167. Liefert binaere Klagefreigabe-Entscheidung mit Begruendung und Aktenvermerk."
---

# Klagefreigabe belegte Forderung

Bevor Klage eingereicht wird durchlaeuft die Forderung ein Pflicht-Pruefraster. Dieser Skill liefert das Raster und das Freigabe-Vermerksmuster.

## Pflicht-Raster

| Punkt | Pruefung | Pass-Kriterium |
|---|---|---|
| 1 Bestehen | Anspruchsgrundlage benennbar Vertrag oder Gesetz | Ja Norm benannt |
| 2 Faelligkeit | Datum Faelligkeit ermittelt | Ja Datum |
| 3 Verzug | Mahnung oder kalendarisches Datum | Ja Beleg |
| 4 Verjährung | Lauf gepruefte Hemmung dokumentiert | nicht eingetreten |
| 5 Beleg | Urkunde Rechnung Vertrag Lieferschein vorhanden | mindestens zwei voneinander unabhaengige Belege |
| 6 Schuldner-Identitaet | richtige Partei zustellfaehige Anschrift | bestaetigt |
| 7 Solvenz-Indiz | kein Insolvenzantrag bekannt | bestaetigt |
| 8 Aussicht | rechtlich begruendet | hoch oder mittel |
| 9 Mandantenfreigabe | Mandant kennt Kostenrisiko zugestimmt | ja schriftlich |

## Pruefung Aktenvermerk

```
Klagefreigabe Forderungssache [Schuldner] - Akte [...]

1. Anspruchsgrund
[Norm und Sachverhalt]

2. Faelligkeit
Faellig seit [Datum] aus Paragraph [...] BGB Vertrag.

3. Verzug
Mahnung vom [Datum] mit Fristsetzung bis [Datum].
Verzug seit [Datum] Paragraph 286 Absatz 1 BGB.

4. Verjährung
Anspruch entstanden [Jahr] Kenntnis seit [Jahr].
Verjährung tritt [Jahr] ein.
Restzeit [Monate].

5. Belege
Anlage K1 Rechnung
Anlage K2 Lieferschein
Anlage K3 Mahnschreiben

6. Schuldner
[Name Anschrift Rechtsform Handelsregister wenn vorhanden].

7. Aussicht
[hoch mittel mit Begruendung].

8. Kostenprognose
Streitwert [Euro] Gerichtsgebuehr ca [Euro]
Anwaltsgebuehr ca [Euro].

9. Mandantenfreigabe
Mandant am [Datum] zugestimmt schriftlich.

Klagefreigabe erteilt am [Datum].
```

## Stop-Bedingungen

- Aussicht gering und Streitwert hoch
- Verjährung bereits eingetreten ohne Hemmung
- Schuldner nicht greifbar verzogen ins Ausland ohne Bezug
- Belege nicht vorhanden nur Aussage von Mandant

## Norm-Pinpoints

- ZPO 138 253
- ZPO 167
- BGB 286 288
- BGB 195 199 204

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [BGB 199](https://www.gesetze-im-internet.de/bgb/__199.html)
