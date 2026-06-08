---
name: tia-eu-us-data-privacy-framework-aktueller
description: "Aktueller Stand zum EU-US Data Privacy Framework (DPF) als Angemessenheitsbeschluss nach Art. 45 DSGVO. Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023, Grundlage Executive Order 14086, Listing-Verfahren, HR/Non-HR-Abdeckung, Onward Transfer, Schrems III. Pruefkriterien für DPF-Tragfaehigkeit und Restrisiko."
---

# EU-US Data Privacy Framework – Aktueller Stand für das TIA

## Zweck

Dieser Skill liefert die aktuelle Bewertung des EU-US Data Privacy Framework (DPF) als Transferinstrument nach Art. 45 DSGVO. Er erklaert Voraussetzungen, Pruefkriterien für die Tragfaehigkeit eines DPF-Listings im konkreten Fall, das Restrisiko angesichts FISA 702 / EO 12333 sowie die Beobachtung der Folgeentwicklungen (Schrems III, DPRC-Praxis, EU-Review).

## Wann dieses Modul hilft

- Pruefung, ob für einen US-Importeur ein TIA noch erforderlich ist.
- Dokumentation des DPF-Listings im RoPA / TIA.
- Strategische Entscheidung DPF vs. SCC.
- HR-Daten an US-Mutter; Pruefung der HR-Abdeckung im DPF.
- Vorbereitung auf moegliche Aufhebung durch EuGH (Schrems III).

## Rechtlicher Rahmen

### Grundlage

- **Durchfuehrungsbeschluss (EU) 2023/1795** der EU-Kommission vom **10.07.2023** ueber das angemessene Schutzniveau personenbezogener Daten im Rahmen des EU-US Data Privacy Framework.
- Basiert auf der US-seitigen **Executive Order 14086** vom 07.10.2022 und nachgelagerten Regulations (insbesondere Department of Commerce DPF Principles).
- US-Aufsicht: **Federal Trade Commission (FTC)** und in begrenztem Umfang **Department of Transportation (DOT)**.
- Rechtsschutz: zweistufiger Mechanismus aus **Civil Liberties Protection Officer (CLPO)** und **Data Protection Review Court (DPRC)**.

### Listing-Verfahren

- Antrag des US-Rechtstraegers beim US Department of Commerce.
- Self-Certification mit jaehrlicher Re-Zertifizierung.
- Veroeffentlichung in der offiziellen DPF-Liste unter dataprivacyframework.gov.
- Drei Track-Optionen: EU-US DPF, Swiss-US DPF, UK Extension – nicht jeder Antrag deckt alle drei ab.
- HR vs. Non-HR-Daten muessen separat angemeldet werden.

### Reichweite und Grenzen

- Greift **nur für aktiv gelistete** US-Rechtstraeger.
- Konzernverbundene Stellen sind nicht automatisch erfasst – jede juristische Person separat pruefen.
- Subprozessoren / Onward Transfer: DPF-Prinzipien verlangen vertragliche Weitergabe und Schutzpflichten.
- Daten ausserhalb des Listings (z. B. Produkt nicht in der Erklaerung erwaehnt) – DPF traegt **nicht**.

### Restrisiko

- FISA 702 und EO 12333 bestehen fort; EO 14086 schraenkt sie ein, hebt sie aber nicht auf.
- Schrems III-Verfahren (NOYB) anhaengig; Pruefung der Unabhaengigkeit des DPRC.
- Bei Aufhebung: DPF nicht mehr tragfaehig; SCC + TIA als Fallback noetig (Schrems-II-Lage in Reinform).

### EU-Review-Verfahren

- Die EU-Kommission ueberprueft die Wirksamkeit des DPF in regelmäßigen Abstaenden; **erster Review** im Sommer 2024 mit Bestaetigung des Beschlusses; weitere Reviews planmaessig alle vier Jahre, ggf. anlassbezogen frueher.

## Ablauf / Checkliste

1. **Exakte Schreibweise des US-Rechtstraegers** in der DPF-Liste suchen.
2. **Listing-Status** "Active" pruefen; bei "Inactive" -> kein DPF.
3. **Zertifizierungsdatum** und naechste Re-Zertifizierung notieren; Screenshot/PDF zur Akte.
4. **HR-/Non-HR-Coverage** pruefen; HR getrennt anmelden noetig.
5. **Produkt-/Dienst-Coverage** mit DPF-Erklaerung und Datenschutzhinweis abgleichen.
6. **Onward-Transfer-Klauseln** im AVV / DPA pruefen (Subprozessoren ausserhalb der USA bzw. ausserhalb des Listings).
7. **DPRC-Hinweis** an Betroffene aufnehmen (Auskunfts-/Beschwerde-Mechanismus).
8. **Restrisiko-Vermerk:** Auch bei DPF empfiehlt sich Erwaehnung des FISA-702/EO-12333-Restrisikos und der laufenden Schrems-III-Beobachtung.
9. **Fallback-Klausel** im Vertrag: bei Wegfall des Angemessenheitsbeschlusses Uebergang auf SCC + TIA.

## Mustertext / Template

DPF-Pruefvermerk:

```
DPF-Prufung – Importeur: [Exakter Name laut DPF-Liste]
Abrufdatum: [YYYY-MM-DD]
Abruf-URL: https://www.dataprivacyframework.gov/list
Aufruf durch: [Bearbeiter]
Listing-Status: Active / Inactive
Zertifizierungsdatum: [...]
Naechste Re-Zertifizierung: [...]
Track: EU-US DPF / Swiss-US DPF / UK Extension
HR-Daten abgedeckt: Ja / Nein
Non-HR-Daten abgedeckt: Ja / Nein
Im DPF gelistete Dienste: [aus DPF-Eintrag und Privacy Policy abgleichen]
Beschwerdemechanismus: [Independent Recourse Mechanism, z. B. AAA, JAMS, EU-DPA Panel]
Bewertung: DPF tragfaehig / nur teilweise / nicht tragfaehig
Restrisiko: [...]
Fallback-Klausel im DPA: [Verweis]
```

Hinweisbaustein im TIA-Schritt 2:

> Fuer den Transfer wird Art. 45 DSGVO i.V.m. dem Durchfuehrungsbeschluss (EU) 2023/1795 als Transferinstrument herangezogen. Der Importeur ist unter dem Namen "..." mit Zertifizierungsdatum [...] aktiv im EU-US Data Privacy Framework gelistet (Anhang DPF-Pruefvermerk). Das Listing umfasst [HR-/Non-HR-]Daten und die im konkreten Vertragsverhaeltnis erbrachten Dienste.
>
> Es bleibt das Restrisiko aus FISA Section 702 und Executive Order 12333. Die Klage Schrems III bei dem Gericht der EU ist anhaengig; bei Aufhebung des Angemessenheitsbeschlusses wird Vertragsgrundlage automatisch auf die Standardvertragsklauseln gemaess Beschluss (EU) 2021/914 umgeschaltet (siehe Anhang AVV-Klausel "Fallback-Transferinstrument").

## Typische Fehler

- "Unsere Konzernmutter ist gelistet" – Tochter ist separater Rechtstraeger und muss eigenstaendig gelistet sein.
- HR-Daten transferiert, aber Listing nur für Non-HR.
- DPF-Eintrag in der Liste, aber Privacy Policy weist auf Datenart, die nicht erfasst ist.
- Re-Zertifizierungsdatum verstrichen – Listing inaktiv, Transfer dennoch fortgesetzt.
- Onward Transfer in weiteres Drittland uebersehen.
- Keine Fallback-Klausel; bei Schrems-III-Aufhebung steht der Transfer ohne Grundlage.
- Verwechslung Swiss-US DPF und EU-US DPF.

## Querverweise

- `tia-schrems-ii-eugh-c-311-18-grundlagen` für Schrems II.
- `tia-us-fisa-702-und-eo-12333-bewertung` für US-Behörden.
- `tia-en-data-privacy-framework-status` für englische Fassung.
- `tia-template-deutsch-vollvorlage` für Vollvorlage.
- `us-transfer-tia-dokumentation` für das Output-Paket.
- `avv-eu-us-data-privacy-framework-bezug` für vertragliche Seite.

## Quellen Stand 06/2026

- Durchfuehrungsbeschluss (EU) 2023/1795 der Kommission vom 10.07.2023.
- US Executive Order 14086 vom 07.10.2022.
- Department of Commerce: DPF Principles und Supplemental Principles.
- EuGH C-311/18 vom 16.07.2020 (Schrems II).
- EU-Kommission, Erster Review des EU-US DPF (Sommer 2024) – Verifikation am amtlichen Bericht.
- Anhaengiges Verfahren Schrems III (NOYB) – Verfahrensstand am Gericht der EU pruefen.
- DPF-Liste: dataprivacyframework.gov.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
