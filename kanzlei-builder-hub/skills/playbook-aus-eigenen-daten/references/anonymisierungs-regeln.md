# Anonymisierungs-Regelsatz für die Playbook-Generierung

## Pflichtersetzungen (Stufe 1 — Direktidentifikatoren)

| Kategorie | Regex / Heuristik | Ersetzung |
|---|---|---|
| Personennamen | NER-Modell + Anrede-Heuristik (Herr/Frau X) | `[PERSON_<n>]` |
| Unternehmensnamen | NER + Suffix-Liste (GmbH, AG, KG, OHG, e.V., UG) | `[UNTERNEHMEN_<n>]` |
| Aktenzeichen | `\d+\s+[A-Z]+\s+\d+/\d+` | `[AZ_<n>]` |
| IBAN | `DE\d{20}` | `[IBAN_<n>]` |
| Steuer-ID | `\d{11}` (Kontextsensitiv) | `[STID_<n>]` |
| USt-IdNr. | `DE\d{9}` | `[USTID_<n>]` |
| Geburtsdatum | `\d{2}\.\d{2}\.\d{4}` (mit Geburtsdatum-Kontext) | `[GEBURT_<n>]` |
| Telefonnummern | `\+49 ...` Muster | `[TEL_<n>]` |
| E-Mail-Adressen | Standard-Regex | `[MAIL_<n>]` |
| Adressen | NER + PLZ-Heuristik | `[ADRESSE_<n>]` |

## Pflichtersetzungen (Stufe 2 — Quasi-Identifikatoren)

| Kategorie | Behandlung |
|---|---|
| Datumsangaben | Pseudonymisierung relativ (`T0`, `T0+14`, `T0+30`) — absolute Daten nur, wenn rechtlich erforderlich (Fristbezug). |
| Beträge | Auf nächsten 100/1.000-Schritt runden bei < 100.000 €, 10.000-Schritt darüber. |
| Standorte | Stadt → Bundesland-Aggregat („Mandantin in NRW") außer wo Gerichtsstand entscheidend. |
| Branchen | Auf Branchen-Cluster reduzieren (z. B. „Maschinenbau-Zulieferer" statt konkreter Firma). |
| Mitarbeiterzahlen | Auf KSchG-relevante Schwellen reduzieren (`> 10`, `> 20`, `> 500`). |

## Stufe 3 — Inhaltliche Schutzfilter

- **Geschäftsgeheimnisse** (i. S. v. § 2 Nr. 1 GeschGehG): jede explizite
  Kennzeichnung als „vertraulich", „strictly confidential",
  „Geschäftsgeheimnis" → automatischer Ausschluss der Passage aus dem
  Spielbuch.
- **Strafverfahren**: Verfahrensstand, Schuldfeststellungen,
  Persönlichkeitsdaten Beschuldigter werden vollständig entfernt
  (BVerfG, Beschl. v. 25.11.1999 – 1 BvR 348/98, NJW 2000, 1859 Rn. 38;
  Schutz aus Art. 6 EMRK).
- **Gesundheitsdaten** (Art. 9 DSGVO): Ersatz durch generische
  Beeinträchtigungsklassen, nie konkrete Diagnose.
- **Mandantenwortlaut**: nur generalisierte Paraphrasen — keine
  wortlautgetreuen Mandanten-Zitate über 5 Wörter Länge.

## Verifikationsschritte vor Spielbuchfreigabe

1. Reidentifikationstest gegen einen externen Vergleichsdatensatz
   (z. B. öffentliches Handelsregister) — keine Treffer zulässig.
2. Stichprobe von 10 % der ersetzten Token wird manuell durch
   Generierungs-Verantwortlichen geprüft.
3. Geschäftsgeheimnis-Filter wird gegen Stichwortliste der Kanzlei
   abgeglichen (z. B. Kundennamen aus dem CRM).
4. Freigabe im 4-Augen-Prinzip (Anwältin + IT-Beauftragte oder
   Datenschutzbeauftragte gem. Art. 37 DSGVO).

## Rechtsgrundlagen

- DSGVO Art. 6 Abs. 1 lit. f, Art. 32, Art. 35.
- BDSG § 26 Abs. 8 Satz 2 (anonymisiert ≠ pseudonymisiert).
- § 43a Abs. 2 BRAO; § 203 Abs. 1 Nr. 3 StGB.
- GeschGehG §§ 2, 3.
- BGH, Urt. v. 13.07.2021 – VI ZR 128/20, NJW 2021, 2956 Rn. 17
  (Anonymisierungsmaßstab).
- BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, BVerfGE 113, 29 Rn. 99
  (Vertrauensschutz Anwalt–Mandant).

## Kommentare

- Buchner/Tinnefeld, in: Kühling/Buchner, DS-GVO BDSG, 4. Aufl. 2024,
  Art. 4 Nr. 5 Rn. 8 (Pseudonymisierung vs. Anonymisierung).
- Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2024, § 43a Rn. 41 ff.
