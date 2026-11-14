---
name: tia-eu-us-data-privacy-framework-aktueller
description: "Prüft die Tragfähigkeit einer aktiven DPF-Zertifizierung im konkreten EU-US-Transfer, dokumentiert deren Reichweite und ordnet das Urteil T-553/23 sowie das anhängige Rechtsmittel C-703/25 P ohne falsche Verfahrensbezeichnung ein."
---

# EU-US Data Privacy Framework – Aktueller Stand für das TIA

## Wann dieses Modul hilft

- Prüfung, ob für einen US-Importeur ein TIA noch erforderlich ist.
- Dokumentation des DPF-Listings im RoPA / TIA.
- Strategische Entscheidung DPF vs. SCC.
- HR-Daten an US-Mutter; Prüfung der HR-Abdeckung im DPF.
- Beobachtung des anhängigen Rechtsmittels in Latombe gegen Kommission und Vorbereitung eines belastbaren Ausweichinstruments für den Fall, dass der Angemessenheitsbeschluss künftig wegfällt.

## Rechtlicher Rahmen

### Grundlage

- **Durchführungsbeschluss (EU) 2023/1795** der Europäischen Kommission vom **10. Juli 2023** über das angemessene Schutzniveau personenbezogener Daten im Rahmen des EU-US Data Privacy Framework.
- Basiert auf der US-seitigen **Executive Order 14086** vom 07.10.2022 und nachgelagerten Regulations (insbesondere Department of Commerce DPF Principles).
- US-Aufsicht: **Federal Trade Commission (FTC)** und in begrenztem Umfang **Department of Transportation (DOT)**.
- Rechtsschutz: zweistufiger Mechanismus aus **Civil Liberties Protection Officer (CLPO)** und **Data Protection Review Court (DPRC)**.

### Listing-Verfahren

- Antrag des US-Rechtsträgers beim US Department of Commerce.
- Selbstzertifizierung mit jährlicher Rezertifizierung.
- Veröffentlichung in der amtlichen DPF-Liste unter dataprivacyframework.gov.
- Drei Track-Optionen: EU-US DPF, Swiss-US DPF, UK Extension – nicht jeder Antrag deckt alle drei ab.
- HR vs. Non-HR-Daten müssen separat angemeldet werden.

### Reichweite und Grenzen

- Greift **nur für aktiv gelistete** US-Rechtsträger.
- Konzernverbundene Stellen sind nicht automatisch erfasst – jede juristische Person separat prüfen.
- Subprozessoren / Onward Transfer: DPF-Prinzipien verlangen vertragliche Weitergabe und Schutzpflichten.
- Daten außerhalb des Listings, etwa bei fehlender Erfassung der maßgeblichen juristischen Person oder Datenkategorie, werden vom DPF **nicht** getragen.

### Restrisiko

- FISA 702 und EO 12333 bestehen fort; EO 14086 schränkt sie ein, hebt sie aber nicht auf.
- Das Gericht der Europäischen Union wies am 3. September 2025 die Nichtigkeitsklage Latombe gegen Kommission, T-553/23, ECLI:EU:T:2025:831, ab. Es verwarf im Rahmen der geprüften Klagegründe insbesondere die Einwände gegen die Unabhängigkeit des DPRC und gegen die Regeln zur massenhaften Datenerhebung.
- Das am 31. Oktober 2025 eingelegte Rechtsmittel C-703/25 P ist beim Gerichtshof anhängig. Es handelt sich um das Verfahren Latombe, nicht um eine Klage von NOYB und nicht um ein amtlich als „Schrems III“ bezeichnetes Verfahren.
- Der Durchführungsbeschluss (EU) 2023/1795 bleibt während des Rechtsmittelverfahrens in Kraft. Sollte er künftig als Transfergrundlage entfallen, trägt eine bloß benannte Ausweichklausel den Transfer nicht; Standardvertragsklauseln, Transferprüfung und erforderliche zusätzliche Maßnahmen müssen vollständig umgesetzt sein.

### EU-Review-Verfahren

- Die Europäische Kommission veröffentlichte den Bericht über die erste regelmäßige Überprüfung am **9. Oktober 2024**. Der Bericht ist eine Monitoringquelle und keine gerichtliche Bestätigung des Angemessenheitsbeschlusses.

## Ablauf / Checkliste

1. **Exakte Schreibweise des US-Rechtsträgers** in der DPF-Liste suchen.
2. **Listing-Status** "Active" prüfen; bei "Inactive" -> kein DPF.
3. **Zertifizierungsdatum** und nächste Rezertifizierung notieren; Screenshot oder PDF zur Akte nehmen.
4. **HR-/Non-HR-Abdeckung** prüfen; HR-Daten müssen gesondert erfasst sein.
5. **Produkt- und Dienstabdeckung** mit DPF-Erklärung und Datenschutzhinweis abgleichen.
6. **Klauseln zur Weiterübermittlung** im AVV oder DPA prüfen, insbesondere bei Subprozessoren außerhalb der USA oder außerhalb des Listings.
7. **DPRC-Hinweis** an Betroffene aufnehmen (Auskunfts-/Beschwerde-Mechanismus).
8. **Restrisiko-Vermerk:** Auch bei DPF sind das FISA-702-/EO-12333-Risiko sowie der aktuelle Stand von T-553/23 und C-703/25 P zu dokumentieren.
9. **Ausweichklausel** im Vertrag: Standardvertragsklauseln nicht nur nennen, sondern richtiges Modul, Anlagen, Transferprüfung und erforderliche zusätzliche Maßnahmen vor einer Nutzung vollständig umsetzen.

## Mustertext / Template

DPF-Prüfvermerk:

```
DPF-Prüfung – Importeur: [Exakter Name laut DPF-Liste]
Abrufdatum: [YYYY-MM-DD]
Abruf-URL: https://www.dataprivacyframework.gov/list
Aufruf durch: [Bearbeiter]
Listing-Status: Active / Inactive
Zertifizierungsdatum: [...]
Nächste Rezertifizierung: [...]
Track: EU-US DPF / Swiss-US DPF / UK Extension
HR-Daten abgedeckt: Ja / Nein
Non-HR-Daten abgedeckt: Ja / Nein
Im DPF gelistete Dienste: [aus DPF-Eintrag und Privacy Policy abgleichen]
Beschwerdemechanismus: [Independent Recourse Mechanism, z. B. AAA, JAMS, EU-DPA Panel]
Bewertung: DPF tragfähig / nur teilweise tragfähig / nicht tragfähig
Restrisiko: [...]
Fallback-Klausel im DPA: [Verweis]
```

Hinweisbaustein im TIA-Schritt 2:

> Für den Transfer wird Artikel 45 DSGVO in Verbindung mit dem Durchführungsbeschluss (EU) 2023/1795 als Transferinstrument herangezogen. Der Importeur ist unter dem Namen "..." mit Zertifizierungsdatum [...] aktiv im EU-US Data Privacy Framework gelistet (Anhang DPF-Prüfvermerk). Das Listing umfasst [HR-/Non-HR-]Daten und die im konkreten Vertragsverhältnis erbrachten Dienste.
>
> Es bleibt das Restrisiko aus FISA Section 702 und Executive Order 12333. Das Gericht der Europäischen Union wies die Nichtigkeitsklage T-553/23 am 3. September 2025 ab; das Rechtsmittel C-703/25 P ist beim Gerichtshof anhängig. Der Durchführungsbeschluss (EU) 2023/1795 bleibt die gegenwärtige Transfergrundlage, soweit die aktive Zertifizierung des Importeurs den konkreten Transfer erfasst. Ein Ausweichen auf Standardvertragsklauseln nach dem Durchführungsbeschluss (EU) 2021/914 setzt voraus, dass Modul, Anlagen, Transferprüfung und erforderliche zusätzliche Maßnahmen vollständig umgesetzt sind.

## Typische Fehler

- "Unsere Konzernmutter ist gelistet" – die Tochter ist ein separater Rechtsträger und muss eigenständig gelistet sein.
- HR-Daten transferiert, aber Listing nur für Non-HR.
- DPF-Eintrag in der Liste, aber Privacy Policy weist auf Datenart, die nicht erfasst ist.
- Re-Zertifizierungsdatum verstrichen – Listing inaktiv, Transfer dennoch fortgesetzt.
- Weiterübermittlung in ein weiteres Drittland übersehen.
- Eine Ausweichklausel als automatisch wirksam behandeln, obwohl Modul, Anlagen und Transferprüfung noch nicht vollständig umgesetzt sind.
- Verwechslung Swiss-US DPF und EU-US DPF.

## Quellen Stand 09/2026

- [Durchführungsbeschluss (EU) 2023/1795 der Kommission vom 10. Juli 2023](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023D1795).
- US Executive Order 14086 vom 07.10.2022.
- Department of Commerce: DPF Principles und Supplemental Principles.
- EuGH C-311/18 vom 16.07.2020 (Schrems II).
- [Europäische Kommission, Bericht über die erste regelmäßige Überprüfung des EU-US DPF vom 9. Oktober 2024, COM(2024) 451 final](https://commission.europa.eu/document/download/25695177-8073-4ce3-bf81-eb816dc6b468_en?filename=Report+on+the+first+periodic+review+of+the+functioning+of+the+adequacy+decision+on+the+EU-US+Data+Privacy+Framework.pdf).
- [Gericht der Europäischen Union, Urteil vom 3. September 2025, Latombe gegen Kommission, T-553/23, ECLI:EU:T:2025:831](https://curia.europa.eu/juris/liste.jsf?num=T-553/23).
- [Gerichtshof der Europäischen Union, anhängiges Rechtsmittel vom 31. Oktober 2025, Latombe gegen Kommission, C-703/25 P](https://curia.europa.eu/juris/liste.jsf?num=C-703/25%20P).
- [Amtliche DPF-Liste](https://www.dataprivacyframework.gov/list).
