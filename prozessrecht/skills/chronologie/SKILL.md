---
name: chronologie
description: Aufbau oder Aktualisierung einer Sachverhalts-Chronologie aus Dokumentenquellen und Uploads – datierte Ereignisse werden extrahiert, dedupliziert und nach Bedeutung für die Mandatstheorie markiert. Verwenden, wenn der Nutzer eine Chronologie oder einen Zeitstrahl aus einer Produktion oder Mandatsakte erstellen möchte, „Chronologie aus den Unterlagen" oder „was ist wann passiert" sagt oder einen Arbeits-, Sachverhaltdarstellungs- oder Zeugen-Zeitstrahl benötigt.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - chronologie
  - sachverhaltschronologie
  - zeitstrahl
  - was ist wann passiert
  - zeitablauf
  - ereignisübersicht
---

# Sachverhalts-Chronologie

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
