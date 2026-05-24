---
name: corporate-kanzlei-teaser-im-processdocs
description: "Teaser, IM und Prozessdokumente: Unterstuetzt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation."
---

# Teaser, IM und Prozessdokumente

## Zweck

Unterstützt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation.

## Arbeitsmodus

- Vorlagen aus Unternehmensdaten und Deal-Profil fuellen.
- Bieter-Markups in Key Issues zerlegen.
- Rote Linien und Konzessionsvorschlaege je Klausel darstellen.
- Mehrere Bieter parallel vergleichbar halten.

## Rote Schwellen

- Ungeprüfte Unternehmensangaben.
- Vertraulichkeit oder Insiderrecht unklar.
- Abweichende Zusagen an Bieter ohne Protokoll.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `corporate-kanzlei-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/teaser-im-draft-plan.md
- assets/templates/process-documents-redline-log.md
