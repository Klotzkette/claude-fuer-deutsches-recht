---
name: corporate-kanzlei-tabellenreview-3d-datenraum
description: "3D-Tabellenreview im Datenraum: Verbindet M&A-Datenraumprüfung mit dem Tabellenreview-3D-Ansatz: Dokumente x Datenpunkte x Perspektiven Recht/Steuer/Wirtschaft."
---

# 3D-Tabellenreview im Datenraum

## Zweck

Verbindet M&A-Datenraumprüfung mit dem Tabellenreview-3D-Ansatz: Dokumente x Datenpunkte x Perspektiven Recht/Steuer/Wirtschaft.

## Arbeitsmodus

- Spaltenprompts für Datenpunkte formulieren.
- Zeilen als Dokumente oder Vertragscluster definieren.
- Blaetter für Legal, Tax, Finance, ESG und PMI anlegen.
- Kreuzblatt-Widersprüche und Belegketten ausgeben.

## Rote Schwellen

- Keine Belegkette.
- Formel- oder CSV-Export nicht nachvollziehbar.
- Materiality-Schwellen uneinheitlich.

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

- assets/templates/tabellenreview-3d-ma-setup.md
- assets/templates/data-quality-gate.md
