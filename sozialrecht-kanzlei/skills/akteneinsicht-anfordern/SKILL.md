---
name: akteneinsicht-anfordern
description: Erstellt einen Akteneinsichtsantrag nach § 25 SGB X (Verwaltungsverfahren) bzw. § 120 SGG (gerichtliches Verfahren) Art. 15 DSGVO ergaenzend bei personenbezogenen Daten. Antrag richtet sich an die Verwaltungsbehoerde oder das Sozialgericht. Inhaltlich enthaelt der Antrag Bezeichnung des Verwaltungsverfahrens vollstaendige Vorgangs- bzw Bescheid-Akte alle medizinischen Gutachten Aktennotizen Stellungnahmen Sachverstaendigengutachten. Form ueber beA an Behoerde oder Gericht. Vorgehensweise bei Verweigerung oder Schwaerzung.
---

# Akteneinsicht anfordern

## Rechtsgrundlagen

- **§ 25 SGB X** — Akteneinsicht im Verwaltungsverfahren. Anspruch der Beteiligten in die das Verfahren betreffenden Akten.
- **§ 120 SGG** — Akteneinsicht im gerichtlichen Verfahren.
- **Art. 15 DSGVO** — Auskunftsrecht in eigene personenbezogene Daten (ergänzend).
- **§ 83 SGB X** — Auskunft des Sozialleistungsträgers an Betroffene.

## Antragsschritte

### Vor dem Bescheid (während Verfahren)

- § 25 SGB X: bei laufendem Verwaltungsverfahren. Akteneinsicht in die das Verfahren betreffenden Akten am Ort der Aktenführung oder über Abschriften.
- Bei medizinischen Gutachten in der Akte: ergänzender Anspruch aus § 25 SGB X auf vollständige Einsicht.

### Nach Widerspruch (im Vorverfahren)

- Pflichtschritt vor Widerspruchsbegründung. Ohne Akteneinsicht keine fundierte Widerspruchsbegründung.
- Vorlage der vollständigen Akte mit allen Gutachten Notizen Aktenvermerken Stellungnahmen.

### Im Klageverfahren

- § 120 SGG: Antrag beim Sozialgericht auf Beiziehung der Verwaltungsakte und Akteneinsicht in die Gerichtsakte.
- Beiziehung erfolgt regelmäßig von Amts wegen (§ 119 SGG iVm § 103 SGG Untersuchungsgrundsatz).

## Antragsmuster

```
An die Beklagte / das Sozialgericht XYZ

In dem Verfahren ...
gegen ...
Az ...

beantrage ich namens und im Auftrag des / der Klagepartei
Akteneinsicht in die vollständige Verwaltungsakte gemäß § 25 SGB X
(bzw. § 120 SGG iVm § 119 SGG) einschließlich
- aller Aktenvermerke
- saemtlicher medizinischer Gutachten und Stellungnahmen
- aller Aktenbestandteile zu vorangegangenen Verfahren soweit sie für das streitige Verfahren bedeutsam sind.

Versand der Akte digital über beA-Nachricht oder als Kopie an die Kanzleianschrift.
```

## Verweigerung oder Schwaerzung

- **Schutzwürdige Belange Dritter** (§ 25 Abs. 3 SGB X) — Behörde kann teilweise Akteneinsicht verweigern. Vertrauliche Behandlung von Drittinteressen.
- **Geheimnisse von Privatpersonen** (§ 25 Abs. 2 SGB X) — soweit erforderlich Schwaerzung.
- **Reaktion** bei umfangreicher Schwaerzung: Anforderung einer Begründung; ggf. Verfahren über § 86b SGG bei Eilbedürftigkeit.

## Frist

- Behörde soll unverzueglich Akteneinsicht gewähren — keine gesetzliche Frist.
- Im Klageverfahren: regelmäßig binnen weniger Wochen.

## Ausgabe

- `akteneinsichtsantrag-<az>-<datum>.docx`.
- Eintrag im Posteingang nach Eingang der Akte.
- Erinnerung bei Verzoegerung (zwei Wochen Nachfrage).

## Folgeschritt

Nach Eingang der Akte: Skill `akteneinsicht-auswerten`.
