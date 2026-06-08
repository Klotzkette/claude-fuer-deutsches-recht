---
name: ropa-konzernumlauf-und-multi-entity
description: "Verzeichnis von Verarbeitungstaetigkeiten in Konzern- und Multi-Entity-Strukturen. Konzernklausel-Mythos, Rollenverteilung (Verantwortlicher gemeinsam Verantwortlich Auftragsverarbeiter), zentrale vs. dezentrale Pflege, Intercompany-Datenfluesse, BCR-Verweis. Mit Strukturskizze und Vorlage für Master-RoPA und Entity-Anhaenge."
---

# RoPA im Konzern und in Multi-Entity-Strukturen

## Zweck

Dieser Skill behandelt das Verzeichnis von Verarbeitungstaetigkeiten in Konzernen und mehrgliedrigen Unternehmensgruppen. Er klaert, dass es **kein Konzernprivileg** im Datenschutzrecht gibt, ordnet Rollenverteilung und Datenfluesse zwischen Gruppenunternehmen und liefert eine Struktur für Master-RoPA mit Entity-Anhaengen.

## Wann dieses Modul hilft

- Konzernweiter RoPA-Roll-out (Mutter- und Tochtergesellschaften).
- Shared-Service-Center für HR, IT, Buchhaltung, Recht (typischerweise Processor-Konstellation).
- Intercompany Data Transfer Agreements (IDTA, hier deutscher Begriff: konzerninterne Datentransfer-Vereinbarung).
- Binding Corporate Rules (BCR) im Aufbau.
- M&A-Due-Diligence (Datenschutz-DD).
- Pruefung durch Aufsichtsbehoerde mit Bezug zu mehreren Konzernunternehmen.

## Rechtlicher Rahmen

### Kein Konzernprivileg

Die DSGVO kennt **kein Konzernprivileg** (Erwaegungsgrund 48 erlaubt nur ein **berechtigtes Interesse** an konzerninterner Datenuebermittlung im Rahmen von Art. 6 Abs. 1 lit. f DSGVO; keine pauschale Freistellung). Jede Datenuebermittlung zwischen rechtlich selbststaendigen Konzernunternehmen ist eine Uebermittlung im Sinne der DSGVO und braucht eine Rechtsgrundlage.

### Rollenverteilung

- **Verantwortlicher (Art. 4 Nr. 7 DSGVO):** entscheidet ueber Zwecke und Mittel.
- **Gemeinsam Verantwortliche (Art. 26 DSGVO):** gemeinsame Festlegung; Joint-Controllership-Vereinbarung erforderlich.
- **Auftragsverarbeiter (Art. 28 DSGVO):** im Auftrag, weisungsgebunden; AVV erforderlich.

Konzerninterne Shared-Service-Center sind typischerweise Auftragsverarbeiter (z. B. IT-Service-GmbH). HR-Daten an Mutter zur Karriereplanung koennen Joint-Controllership begruenden.

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
5. **Intercompany-Vertraege:** AVV oder Joint-Controllership-Vereinbarung verlinken.
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

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` für Basis.
- `avv-konzern-und-multi-party-konstellation` für Vertragsseite.
- `avv-art-26-joint-controllership-deutsch` für Joint Controllership.
- `bcr-binding-corporate-rules` (falls Skill existiert) für BCR-Verfahren.
- `tia-template-deutsch-vollvorlage` für Transferpruefung.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 4 Nr. 7, Art. 26, Art. 28, Art. 30, Art. 44–47, Erwaegungsgrund 48.
- Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021 (SCC).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021).
- EDPB Working Document on Approval Procedure for BCR (zuletzt aktualisiert 2022).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
