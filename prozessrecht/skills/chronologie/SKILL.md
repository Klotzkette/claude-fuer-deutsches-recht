---
name: chronologie
description: "Sachverhaltschronologie fuer Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Pruefraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabellarische Sachverhaltschronologie. Abgrenzung: nicht vollstaendige Klageschrift."
---

# Sachverhalts-Chronologie

## Triage — kläre vor der Erstellung

1. **Modus:** Arbeitschronologie (intern, vollständig), Schriftsatz-Chronologie (aufbereitet) oder Zeugenchronologie (gefültert)?
2. **Dokumentenbasis:** Liegen die Quellen vor (Verträge, E-Mails, Schriftsätze, Anlagen)?
3. **Zeitraum:** Welcher Zeitraum ist mandatsrelevant — gibt es einen frühesten relevanten Stichtag?
4. **Lücken:** Gibt es bekannte Zeiträume, für die keine Dokumente vorliegen?
5. **Prozessuale Funktion:** Für Sachverhaltsdarstellung (§ 253 ZPO), Zeugenvernehmung (§§ 373 ff. ZPO) oder Berufungsbegründung (§ 520 Abs. 3 ZPO)?

## Zentrale Normen
- § 253 Abs. 2 Nr. 1 ZPO (Anforderungen an die Klageschrift — vollständiger Sachvortrag)
- § 138 ZPO (Erklärungspflicht der Parteien — Vollständigkeit und Wahrheitspflicht)
- § 373 ff. ZPO (Zeugenbeweis — Grundlage der Zeugenchronologie)
- § 520 Abs. 3 ZPO (Berufungsbegründung — tatsächliche Angaben)
- § 286 ZPO (Freie Beweiswuerdigung — Chronologie als Hilfsmittel)

## Rechtsprechung (ergänzt)
1. BGH, Urt. v. 11.01.2023 – VIII ZR 153/21, NJW 2023, 843 Rn. 20 — Eine schlüssige Klageschrift erfordert vollständigen, widerspruchsfreien Sachvortrag; eine chronologisch geordnete Darstellung der anspruchsbegründenden Tatsachen ist dafür zwingend.
2. BGH, Urt. v. 07.03.2001 – X ZR 160/99, NJW 2001, 2398 Rn. 11 — Bei komplexen Sachverhalten kann ein Zeitstrahl die Darlegung des übereinstimmenden Willens der Parteien und den Ablauf von Fristen wesentlich vereinfachen.
3. BGH, Urt. v. 06.12.2017 – IV ZR 16/16, NJW 2018, 1162 — Die Beweiskraft einer Sachverhaltschronologie hängt davon ab, dass jede tatsächliche Angabe mit einer Quellenangabe verknüpft ist; unbelegt eingeflösste Tatsachen können als nicht vorgetragen behandelt werden.
4. BGH, Urt. v. 14.03.2014 – V ZR 115/13, NJW 2014, 2787 — Im Berufungsverfahren darf eine fehlerhafte Sachverhaltsdarstellung in der Vorinstanz durch geordneten, belegten Sachvortrag korrigiert werden (§ 529 Abs. 1 Nr. 1, § 531 Abs. 2 ZPO).

## Kommentarliteratur
- Zöller/Schultzky, ZPO, 35. Aufl. 2024, § 253 Rn. 1 ff. (Anforderungen an Klageschrift und Sachvortrag).
- MuKo-ZPO/Heinrich, 6. Aufl. 2023, § 138 Rn. 1 ff. (Erklärungspflicht).
- Stein/Jonas, ZPO, 23. Aufl. 2018, § 286 Rn. 1 ff. (Freie Beweiswuerdigung).

## Zweck

Aufbau einer mandatsbezogenen Sachverhalts-Chronologie aus vorliegenden Dokumenten, Schriftsätzen, Verträgen, E-Mails und Anlagen. Die Chronologie dient als Grundlage für Sachverhaltsdarstellungen im Schriftsatz (§ 253 Abs. 2 Nr. 1 ZPO), Zeugenvernehmungsvorbereitung (§§ 373 ff. ZPO), Berufungsbegründung (§ 520 Abs. 3 ZPO) und interne Mandatsbriefings.

Drei Modi:
- **Arbeitschronologie** – intern, vollständig, mit Lückenmarkierungen
- **Sachverhaltsdarstellungs-Chronologie** – aufbereitet für den Schriftsatz, urteilsstilgerecht
- **Zeugenchronologie** – gefiltert auf einen bestimmten Zeugen für Vernehmungsvorbereitung

## Eingaben

- Aktives Mandat (Slug)
- Hochgeladene Dokumente: Verträge, Korrespondenz, E-Mails, Protokolle, Rechnungen, Sachverständigengutachten, Gerichtsentscheidungen
- Wahl des Modus: `--arbeits` | `--sachverhalt` | `--zeuge=[Name]`
- Optional: bekannte Schlüsseldaten (z. B. Vertragsschluss, Fälligkeitsdatum, Kündigungserklärung)

## Ablauf

1. **Dokumente parsen:** Alle hochgeladenen Dateien auf datierte Ereignisse scannen. Datum, Uhrzeit (soweit angegeben), Ereignisbeschreibung, Quelle (Dokumentenbezeichnung, Anlage-Nr.) und beteiligte Personen extrahieren.

2. **Deduplizierung:** Gleiche Ereignisse aus verschiedenen Quellen zusammenführen; Widersprüche markieren als `[WIDERSPRUCH: Quelle A gibt X an, Quelle B gibt Y an]`.

3. **Mandatstheorien-Tagging:** Jedes Ereignis nach Relevanz für die Mandatstheorie markieren:
   - 🔑 Kernereig­nis (unmittelbar anspruchsbegründend oder -ausschließend)
   - ⚠️ Risikopunkt (könnte gegen Mandantin sprechen)
   - 📎 Hintergrundinformation
   - ❓ Ungeklärt / Beleg fehlt

4. **Lücken identifizieren:** Zeiträume ohne belegte Ereignisse und inhaltliche Lücken (z. B. fehlende Zugangsbestätigung, unklare Übergabe) als `[LÜCKE: Zeitraum MM/JJJJ bis MM/JJJJ – kein Beleg]` markieren.

5. **Modus anwenden:**
   - *Arbeitschronologie:* Vollständige Liste mit Quellenangaben und Anmerkungen.
   - *Sachverhaltsdarstellung:* Fließtext im Urteilsstil, Ereignisse in der dritten Person, Beweisquellen als Fußnoten.
   - *Zeugenchronologie:* Nur Ereignisse mit Beteiligung des Zeugen; Ergänzung um mögliche Wissenslücken des Zeugen.

6. **Versionierung:** Neue Chronologien als `chronology-v[N].md` im Mandatsordner speichern.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 253 Rn. 8 (Sachverhaltsdarstellung in der Klageschrift: vollständig, geordnet, widerspruchsfrei).
- BGH, Urt. v. 11.01.2023 – VIII ZR 153/21, NJW 2023, 843 Rn. 20 (Schlüssigkeit der Klageschrift erfordert vollständigen Sachvortrag aller anspruchsbegründenden Tatsachen).
- BGH, Urt. v. 07.03.2001 – X ZR 160/99, NJW 2001, 2398 Rn. 11 (Zeitstrahl als Hilfe bei komplexen Sachverhalten).
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 286 Rn. 14 (Verzugseintritt: Datum des Zugangs der Mahnung entscheidend – Chronologie muss Zugang belegen).
- Koch, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 286 Rn. 5 ff. (Beweismaß und Beweiswürdigung bei zeitlichen Abläufen).

## Ausgabeformat

### Arbeitschronologie (Tabelle)

| Datum | Ereignis | Quelle / Anlage | Beteiligte | Tag | Anmerkung |
|---|---|---|---|---|---|
| 12.03.2022 | Abschluss Werkvertrag | Anlage K1 (Vertrag v. 12.03.2022) | Kl., Bekl. | 🔑 | Unterschriften vorhanden |
| 15.04.2022 | Fristsetzung Mängelbeseitigung (Schreiben Kl.) | Anlage K3 | Kl. → Bekl. | 🔑 | Zugang streitig |
| [LÜCKE] | Zeitraum 16.04. – 30.05.2022 | – | – | ❓ | Keine Korrespondenz vorhanden |

### Sachverhaltsdarstellung (Fließtext-Modus)

> Am 12. März 2022 schlossen die Parteien einen Werkvertrag über die Erstellung einer Software (Anlage K1). Mit Schreiben vom 15. April 2022, dem Beklagten zugegangen am 17. April 2022 (Anlage K2: Rückschein), setzte die Klägerin eine Nachfrist zur Mängelbeseitigung bis zum 1. Mai 2022.
>
> *Beweis für Zugang: Zeugnis des Herrn Anton Mayer, [Anschrift]; Anlage K2 (Zustellungsnachweis).*

## Risiken / typische Fehler

- **Unklarer Zugangszeitpunkt:** Zugangsnachweis für Mahnungen und Fristsetzungen ist entscheidend für Verzugsbeginn (§ 286 Abs. 1 BGB); fehlende Belege zwingend als Lücke markieren.
- **Fehlende Chronologie im Schriftsatz:** Eine ungeordnete Sachverhaltsdarstellung kann zur Unschlüssigkeit führen; der BGH verlangt vollständigen, widerspruchsfreien Sachvortrag (BGH, Urt. v. 11.01.2023 – VIII ZR 153/21, NJW 2023, 843 Rn. 20).
- **Veraltete Chronologie:** Nach jedem Mandat-Update (`/mandat-update`) die Chronologie ergänzen; veraltete Versionen archivieren.
- **Zeugenchronologie zu weit gefasst:** Nur mandatsrelevante Ereignisse einbeziehen; nicht alle Ereignisse, an denen der Zeuge beteiligt war.
- **Datenschutz:** Personenbezogene Daten Dritter nur soweit erforderlich; DSGVO-Minimierungsgrundsatz (Art. 5 Abs. 1 lit. c DSGVO) beachten.
