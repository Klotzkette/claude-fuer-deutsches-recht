---
name: wandlungsausschluss-pruefung
description: "Pruefung Verfallklauseln, Erloeschen des Wandlungsrechts, Verzicht, Verjaehrung (§§ 194 ff. BGB, drei Jahre) und vertragliche Ausschlussgruende. Wann ist das Wandlungsrecht des Lenders nicht mehr ausuebbar? Auswirkung auf Rueckzahlungsanspruch."
---

# Wandlungsausschluss-Prüfung

## Zweck

Dieser Skill prüft, ob das Wandlungsrecht des Lenders erloschen, verfristet, verjährt oder durch Verzicht ausgeschlossen ist, bevor eine Wandlung durchgeführt wird. Phase C des Lebenszyklus.

## Eingaben

- Wandeldarlehensvertrag (§§ 4.4, 4.10)
- Datum der Wandlungsmitteilung
- Datum der Wandlungserklärung des Lenders
- Frühere Wandlungsereignisse und Ausübungserklärungen
- Etwaige Verzichtserklärungen des Lenders
- Gesellschaftervertrag (SHA) – enthält er weitere Ausschlüsse?

## Rechtlicher Rahmen

### Primärnormen
- § 194 BGB (Verjährung: drei Jahre ab Entstehung des Anspruchs, § 199 BGB)
- § 397 BGB (Erlasserklärung / Verzicht)
- § 4.4 Wandeldarlehensvertrag (Verfristung: ein Monat nach Wandlungsmitteilung)
- § 242 BGB (Treu und Glauben – Verwirkung nach langem Zuwarten)
- § 93 InsO (Anfechtung von Verfügungen über Wandlungsrechte)

### Rechtsprechung
- BGH, Urt. v. 26. September 1996 – III ZR 44/96 (Verwirkung von Optionsrechten)
- BGH, Urt. v. 11. Oktober 2005 – XI ZR 395/04 (Fristberechnung bei Optionsausübung)

## Vorgehen

### 1. Fristprüfung (§ 4.4)
Frist: ein Monat nach Zugang der Wandlungsmitteilung. Maßgeblicher Zeitpunkt: Eingang der Wandlungsmitteilung beim Lender (§ 130 BGB). Ist Wandlungserklärung innerhalb dieser Frist eingegangen? Wenn nein: Wandlungsrecht für dieses Ereignis erloschen.

### 2. Mehrfache Wandlungsereignisse
Gilt Fristversäumnis für ein Ereignis: Wandlungsrecht erlischt nur für dieses Ereignis (§ 4.4 Satz 2). Für spätere Wandlungsereignisse bleibt das Recht bestehen. Prüfen: Gibt es ein weiteres Wandlungsereignis?

### 3. Verjährungsprüfung
Reguläre Verjährung drei Jahre (§ 195 BGB) ab Entstehung. Wandlungsrecht entsteht mit Eintritt des Wandlungsereignisses. Prüfung: Liegt der Wandlungsereignis-Zeitpunkt mehr als drei Jahre zurück?

### 4. Verwirkung prüfen (§ 242 BGB)
Hat der Lender über längere Zeit nach Kenntnis des Wandlungsereignisses nicht reagiert? Hat die Gesellschaft berechtigterweise darauf vertraut, dass kein Wandlungsrecht mehr ausgeübt wird (Vertrauensgesichtspunkt)? BGH: Verwirkung erfordert Zeit- und Umstandsmoment.

### 5. Verzicht prüfen (§ 397 BGB)
Hat der Lender schriftlich auf sein Wandlungsrecht verzichtet? Enthält eine Vereinbarung (Side Letter, SHA, Änderungsvertrag) einen Ausschluss?

### 6. Ergebnis und Empfehlung
Wandlungsrecht besteht: Weiter zu `wandlungspreis-berechnung`. Wandlungsrecht erloschen: Rückzahlungsanspruch prüfen (§ 2.2 Wandeldarlehensvertrag – Rückzahlung fällig).

## Prüfmatrix

| Ausschlussgrund | Tatbestand | Rechtsfolge |
|---|---|---|
| Fristversäumnis § 4.4 | Erklärung nach einem Monat | Erlöschen für dieses Ereignis |
| Verjährung | Mehr als drei Jahre seit Ereignis | Anspruch nicht mehr durchsetzbar |
| Verwirkung | Zeit + Umstandsmoment | Recht verwirkt |
| Verzicht § 397 BGB | Schriftliche Verzichtserklärung | Wandlungsrecht endgültig erloschen |
| Gesellschaft insolvent | Keine Kapitalerhöhung möglich | Rangrücktritt, Wandlung faktisch unmöglich |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Wandlungsmitteilung nie verschickt | Fristlauf unklar | Mitteilung verspätet | Mitteilung dokumentiert |
| Lender drei Monate ohne Reaktion | Verwirkungsrisiko | Reaktion verzögert | Reaktion innerhalb Frist |
| SHA enthält weiteren Ausschluss | Wandlungsrecht eingeschränkt | SHA auslegungsbedürftig | Kein Ausschluss |
| Insolvenz Gesellschaft | Kapitalerhöhung unmöglich | Insolvenzantrag gestellt | Gesellschaft solvent |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandelereignis-eingang/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-maturity/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Verjährungsrecht aktualisieren.
