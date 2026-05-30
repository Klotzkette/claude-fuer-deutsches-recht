# 08 OLG Berufung 14 U 22/26 — Anlagensynchronisation

Datum: 10. März 2026
Bearbeiter: RA Dr. Bertram Söhnchen LL.M.
Az.: 14 U 22/26 (OLG Köln/Aachen)

---

## Verfahrenssituation

Das OLG-Berufungsverfahren 14 U 22/26 betrifft eine Teilforderung Werkmanns aus dem Stammverfahren — konkret Verzugsschäden wegen verspäteter Zahlung durch K+B, die das LG Aachen (5 O 244/25) dem Grunde nach anerkannt, der Höhe nach aber auf 290.000 EUR (von beantragten 380.000 EUR) begrenzt hatte. K+B hat wegen der 290.000 EUR Berufung eingelegt; Werkmann hat Anschlussberufung wegen der fehlenden 90.000 EUR eingelegt.

Im OLG-Verfahren gelten andere Anlagenpräfixe: K+B (als Berufungskläger) verwendet BK 1 ff., Werkmann (als Berufungsbeklagter und Anschlussberufungskläger) verwendet BB 1 ff.

---

## Das Synchronisationsproblem

### Problem 1: Doppelanlagen unter verschiedenen Bezeichnungen

Von den 247 für das LG-Verfahren (11 O 188/26) bestimmten Anlagen tauchen **38 Dokumente** auch im OLG-Verfahren auf, jedoch unter abweichenden Bezeichnungen:

| Dokument | LG-Bezeichnung | OLG-Bezeichnung |
|---|---|---|
| Abnahmeprotokoll 04.11.2024 | K3 | BB 12 |
| Schlussrechnung 18.11.2024 | K5 | BB 14 |
| Zahlungsnachweis 7,99 Mio. EUR | K8 | BB 17 |
| Nachtrag 47 (Verzögerung) | K15 | BB 31 |
| Bautagebuch 15.07.2024 | K51 | BB 22 |

Wenn im OLG-Schriftsatz auf ein Dokument Bezug genommen wird, das auch im LG-Verfahren eingereicht ist, darf der Schriftsatz nur die OLG-Anlagenbezeichnung (BB X) verwenden — eine Verwechslung mit K-Nummern wäre ein Formfehler.

### Problem 2: Unterschiedliche Dokumentversionen

In zwei Fällen liegen tatsächlich unterschiedliche Versionen desselben Dokuments vor: Das Aufmaßprotokoll K38 (LG) entspricht BB 21 (OLG) in der Druckversion 2, während das LG-Dokument die Druckversion 1 enthält. Ursache: Die Version 2 wurde nach dem LG-Verfahren erstellt, um einen Rechenfehler in der Massenermittlung zu korrigieren. Dr. Söhnchen muss im LG-Verfahren nach § 139 ZPO nachbessern (Aktenstück 15).

### Problem 3: OLG-spezifische Anlagen

Das OLG-Verfahren erfordert zusätzliche Anlagen, die im LG-Verfahren nicht relevant sind, weil sie erst nach der LG-Klage entstanden sind: das erstinstanzliche Urteil (BK 1 / BB 1), der Schriftsatz der Berufungsbegründung (nicht als Anlage, aber als prozessuale Grundlage) und die im Berufungsverfahren neu eingeholten Privatgutachten.

---

## Anlagensynchronisations-Matrix

Zur Lösung des Synchronisationsproblems wurde eine verfahrensübergreifende Master-Anlagenmatrix erstellt (Aktenstück 12, XLSX-Datei `anlagenmatrix_lg_aachen_3847_einzelanlagen.xlsx`). Diese Matrix enthält für jedes Dokument:

- Interne Dokument-ID (kanzleiübergreifend eindeutig)
- LG-Bezeichnung (K-Nummer oder B-Nummer)
- OLG-Bezeichnung (BK oder BB Nummer)
- DIS-Bezeichnung (S-W oder S-KB Nummer)
- Dateiname (aktuelle Version, mit Hash)
- Verweis auf Anspruchsposition

Die Matrix ist in allen drei Schriftsatz-Teams geteilt und wird täglich synchronisiert.

---

## OLG-Berufungsbegründung: Anlagenstrategie

Die Berufungsbegründung (Frist: 15.03.2026, eingereicht fristgerecht) enthält folgende Anlagen:

**BB 1–BB 5**: Erstinstanzliche Urteils- und Entscheidungsunterlagen
**BB 6–BB 20**: Belege zur Schadenshöhe (neu vorgelegt nach § 531 Abs. 2 ZPO)
**BB 21–BB 40**: Dokumente aus dem Bauablauf, die für die OLG-Berufungsfrage unmittelbar relevant sind

Der Senat hat in der Eingangskorrespondenz signalisiert, dass das OLG kein vollständiges Anlagenkonvolut erwartet — da das OLG als Berufungsinstanz die erstinstanzlichen Akten vollständig übernimmt (§ 525 ZPO i.V.m. § 299 ZPO), sind nur die neuen oder streitigen Anlagen vorzulegen.

---

## Prozessrechtliche Grundlage

- § 520 ZPO (https://dejure.org/gesetze/ZPO/520.html): Berufungsbegründung; Formvorschriften und Fristeinhaltung
- § 531 Abs. 2 ZPO (https://dejure.org/gesetze/ZPO/531.html): Neue Angriffs- und Verteidigungsmittel in der Berufungsinstanz — nur ausnahmsweise zulässig
- BGH, Urteil vom 19.03.2004 — V ZR 104/03 (bundesgerichtshof.de): Zur Präklusion neuer Anlagen in der Berufung

Die OLG-Berufungssituation ist prozessrechtlich damit anspruchsvoller als das LG-Verfahren, weil neue Anlagen nur unter den engen Voraussetzungen des § 531 Abs. 2 ZPO eingeführt werden dürfen. Die Kanzlei hat sorgfältig geprüft, ob alle BB-Anlagen bereits in erster Instanz angeboten wurden oder unter eine der Ausnahmen des § 531 Abs. 2 ZPO fallen.
