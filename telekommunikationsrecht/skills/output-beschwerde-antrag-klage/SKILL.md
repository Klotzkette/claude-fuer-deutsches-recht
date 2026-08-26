---
name: output-beschwerde-antrag-klage
description: "Für Output-Generator: Beschwerde, Antrag, Klage, Stellungnahme: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik."
---

# Output-Generator: Beschwerde, Antrag, Klage, Stellungnahme

## Norm- und Quellenanker

- **TKG:** § 2 TKG (Regulierungsziele), § 52 TKG (Streitbeilegung/Informationspflichten im Endnutzerkontext), § 68 TKG (Schlichtung bei der BNetzA), § 125 TKG (Wegerecht), § 127 TKG (Zustimmung des Wegebaulasttraegers).
- **Verwaltungsrecht:** §§ 22, 24, 37, 39 VwVfG fuer Antrag, Amtsermittlung, Bestimmtheit und Begruendung; §§ 68 ff., 74, 80 Abs. 5, 123 VwGO fuer Widerspruch, Klagefrist und Eilrechtsschutz.
- **Zivilrecht:** §§ 241, 280, 281, 323, 314, 536a analog nur vorsichtig, §§ 305 ff. BGB fuer AGB-/Providerklauseln; ZPO §§ 253, 256, 286, 940 ff. bei Klage, Feststellung und Eilrechtsschutz.
- **Quellen:** BNetzA-Formulare und TKG-Normstand live pruefen; bei Endnutzerfaellen immer unterscheiden zwischen Beschwerde, Schlichtungsantrag, zivilrechtlicher Forderung und verwaltungsrechtlichem Antrag.

## Red Flags

- falsche Behörde
- keine Anlagenlogik
- Begehren zu unbestimmt
- zivilrechtliche und öffentlich-rechtliche Anträge vermischt
- Schlichtungsantrag nach § 68 TKG wird mit einer Aufsichtsbeschwerde verwechselt
- Wegerechtsantrag nach § 125 TKG und kommunale Zustimmung nach § 127 TKG werden in einem unklaren Schreiben vermengt
- Fristen nach VwGO oder vertragliche Ausschluss-/Entstörungsfristen werden nicht getrennt

## Arbeitsprodukt

1. **Sachverhaltskopf:** Anschluss, Dienst, Anbieter, Kundentyp, Ort, Zeitachse, bisherige Tickets, Stoerungsnummern, Vertragsunterlagen.
2. **Rechtsweg-Router:** BNetzA-Schlichtung, BNetzA-Aufsicht, Verwaltungsverfahren, Zivilklage oder einstweilige Verfuegung.
3. **Antragssatz:** genau ein Hauptbegehren, danach Hilfsbegehren; keine Mischung von „bitte pruefen“ und vollstreckbarem Antrag.
4. **Anlagenlogik:** Vertrag, AGB, Rechnungen, Stoerungsprotokoll, Speedtests, Screenshots, Ticketverlauf, Fristsetzung.
5. **Output:** Beschwerde, Schlichtungsantrag, Verwaltungsantrag, Widerspruch, Klageentwurf, Klageerwiderung oder Vergleichsvorschlag.

## Anschluss-Skills

- tk-zuständigkeits-router-bnetza-vg-lg
- tk-beschwerde-dashboard-bnetza
