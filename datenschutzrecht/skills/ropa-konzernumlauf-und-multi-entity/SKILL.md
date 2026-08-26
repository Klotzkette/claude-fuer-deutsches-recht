---
name: ropa-konzernumlauf-und-multi-entity
description: "Für RoPA im Konzern und in Multi-Entity-Strukturen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# RoPA im Konzern und in Multi-Entity-Strukturen

## Wann dieses Modul hilft

- Konzernweiter RoPA-Roll-out (Mutter- und Tochtergesellschaften).
- Shared-Service-Center für HR, IT, Buchhaltung, Recht (typischerweise Processor-Konstellation).
- Intercompany Data Transfer Agreements (IDTA, hier deutscher Begriff: konzerninterne Datentransfer-Vereinbarung).
- Binding Corporate Rules (BCR) im Aufbau.
- M&A-Due-Diligence (Datenschutz-DD).
- Prüfung durch Aufsichtsbehoerde mit Bezug zu mehreren Konzernunternehmen.

## Rechtlicher Rahmen

### Kein Konzernprivileg

Die DSGVO kennt **kein Konzernprivileg** (Erwaegungsgrund 48 erlaubt nur ein **berechtigtes Interesse** an konzerninterner Datenuebermittlung im Rahmen von Art. 6 Abs. 1 lit. f DSGVO; keine pauschale Freistellung). Jede Datenuebermittlung zwischen rechtlich selbststaendigen Konzernunternehmen ist eine Uebermittlung im Sinne der DSGVO und braucht eine Rechtsgrundlage.

### Rollenverteilung

- **Verantwortlicher (Art. 4 Nr. 7 DSGVO):** entscheidet über Zwecke und Mittel.
- **Gemeinsam Verantwortliche (Art. 26 DSGVO):** gemeinsame Festlegung; Joint-Controllership-Vereinbarung erforderlich.
- **Auftragsverarbeiter (Art. 28 DSGVO):** im Auftrag, weisungsgebunden; AVV erforderlich.

Konzerninterne Shared-Service-Center sind typischerweise Auftragsverarbeiter (z. B. IT-Service-GmbH). HR-Daten an Mutter zur Karriereplanung können Joint-Controllership begruenden.

### Drittlandtransfer im Konzern

Konzerninterne Uebermittlungen in Drittlaender unterliegen Art. 44 ff. DSGVO. Loesungen:

- BCR (Art. 47 DSGVO) – aufwendig, aber genehmigungsfaehig.
- SCC (Beschluss (EU) 2021/914) zwischen den konzernzugehoerigen Stellen.
- Angemessenheitsbeschluss (z. B. EU-US DPF für US-Tochter im DPF).

### EDSA-Leitlinien

EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021) – grundlegend zur Rollenklaerung.

## Ablauf / Checkliste

1. **Strukturkarte:** Liste aller Konzerngesellschaften mit Sitz, Rechtsform, taetigem Personal, Datenkategorien.
2. **Rollen-Mapping:** Wer ist für welchen Datenfluss Controller, Joint Controller oder Processor?
3. **Master-RoPA:** zentrales Dokument für gruppenuebergreifende Prozesse (Konzern-HR, Konzern-CRM, Konzern-Compliance).
4. **Entity-Anhaenge:** pro Gesellschaft eigene Tabelle mit Spezifika.
5. **Intercompany-Verträge:** AVV oder Joint-Controllership-Vereinbarung verlinken.
6. **BCR-Status:** wenn vorhanden, in jedem Entity-RoPA als Garantie referenzieren; sonst SCC.
7. **Pflegemodell:** zentraler Datenschutzkoordinator oder dezentrale DSB?

## Mustertext / Template

### Master-RoPA-Deckblatt

```
Konzern: [Mutter AG]
Konzernweite DSB: [Name, Kontakt]
Geltungsbereich: [Liste der Tochtergesellschaften, EU/EWR + Drittlaender]
Konzerninterne Garantie: [BCR genehmigt YYYY-MM-DD durch Lead-Behörde XY] oder [SCC-Rahmenvertrag YYYY]
Erstellt: [Datum]
Letzte Aenderung: [Datum]
Version: [v1.0]
```

### Master-Tabelle (gruppenuebergreifende Prozesse)

| Nr. | Prozess | Verantwortlicher | Gemeinsam Verantwortliche | Auftragsverarbeiter im Konzern | Datenfluss | Garantie |
|---|---|---|---|---|---|---|
| 1 | Konzern-Identity-Provider | Mutter AG (DE) | – | IT-Service-GmbH (DE) | Mitarbeiter aller Entities -> IdP | AVV |
| 2 | Konzernweite Compliance-Hotline | Mutter AG (DE) und Tochter Inc. (US) | Joint-Controllership Vereinbarung vom YYYY | Hotline-Provider (Dritter) | Hinweise aus allen Standorten | SCC + TIA; US-Tochter im EU-US DPF |
| 3 | Talent-Pool / Karriereplattform | Mutter AG | Toechter EU/EWR | – | HR-Daten weltweit | BCR (genehmigt YYYY) |
| 4 | Konzern-CRM | Mutter AG | – | Vertriebs-GmbH (DE) | Kundendaten EU -> Konzernzentrale | AVV |

### Entity-Anhang (pro Tochter)

```
Tochter: [Name, Sitz, Rechtsform]
Lokal Verantwortlicher: [...]
Lokal DSB: [...]
Lokale Aufsichtsbehoerde: [...]
Lokale Prozesse: [Tabelle entsprechend Controller-Vorlage]
Bezug zu Master-RoPA: [Prozessnummern oben]
```

### Datenflussdiagramm (textuell)

```
DE (Mutter) <--AVV--> IT-Service-GmbH (DE)
DE (Mutter) <--Joint Controllership--> US (Tochter im DPF)
DE (Mutter) <--BCR--> IN (Tochter)
DE (Mutter) <--SCC--> BR (Tochter, kein Angemessenheitsbeschluss)
```

## Typische Fehler

- "Konzernprivileg" angenommen; keine eigene Rechtsgrundlage dokumentiert.
- Shared-Service-Center als Controller behandelt, obwohl weisungsgebunden -> Joint Controllership statt AVV unzutreffend gewaehlt.
- BCR vorhanden, aber im RoPA nicht referenziert.
- Intercompany-Datenfluesse nicht erfasst; nur lokale Prozesse dokumentiert.
- US-Konzerntochter als "EU-nahe" behandelt – DPF-Status nicht geprueft.
- M&A: Datenschutz-DD ohne Sichtung des RoPA der Target-Gesellschaft.
- Doppelte Pflege: Master-RoPA und Entity-RoPA divergieren; kein Versionsabgleich.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 4 Nr. 7, Art. 26, Art. 28, Art. 30, Art. 44–47, Erwaegungsgrund 48.
- Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021 (SCC).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021).
- EDPB Working Document on Approval Procedure for BCR (zuletzt aktualisiert 2022).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).
