---
name: verl-druckvertrag-buchhandelsvertrag
description: "Verl 024 Druckvertrag Papier Krise Lieferverzug, Verl 032 Buchhandelsvertrag Konditionen Und Remission: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 024 Druckvertrag Papier Krise Lieferverzug, Verl 032 Buchhandelsvertrag Konditionen Und Remission

## Arbeitsbereich

Dieser Skill bündelt **Verl 024 Druckvertrag Papier Krise Lieferverzug, Verl 032 Buchhandelsvertrag Konditionen Und Remission** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-024-druckvertrag-papier-krise-lieferverzug` | Verlagsrecht: Druckverträge, Papierlieferengpässe, Lieferverzug der Druckerei — Werkvertragsrecht, höhere Gewalt, Schadensersatz, Preisklauseln und Notfallplanung. |
| `verl-032-buchhandelsvertrag-konditionen-und-remission` | Verlagsrecht: Buchhandelsvertrag zwischen Verlag und Buchhandel — Konditionenabkommen, Remissionsrecht, Retourenquoten, Auslieferungsverträge und Buchpreisbindungs-Compliance. |

## Arbeitsweg

Für **Verl 024 Druckvertrag Papier Krise Lieferverzug, Verl 032 Buchhandelsvertrag Konditionen Und Remission** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-024-druckvertrag-papier-krise-lieferverzug`

**Fokus:** Verlagsrecht: Druckverträge, Papierlieferengpässe, Lieferverzug der Druckerei — Werkvertragsrecht, höhere Gewalt, Schadensersatz, Preisklauseln und Notfallplanung.

# Verl-024 · Druckvertrag, Papierengpass und Lieferverzug

## Zweck dieses Skills

Druckverträge zwischen Verlagen und Druckereien sind **Werkverträge**, die eigene Mängelrechte, Fristen und Haftungsregeln kennen. Papierlieferengpässe (wie 2021–2023) und Logistikstörungen können erhebliche Verzögerungen verursachen. Dieser Skill klärt Rechte und Pflichten, Force-Majeure-Klauseln und Schadensersatz.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BGB § 631 | Werkvertrag: Druckerei schuldet Erfolg (fertige Druckerzeugnisse) | https://dejure.org/gesetze/BGB/631.html |
| BGB § 633 | Mangelfreiheit des Werks | https://dejure.org/gesetze/BGB/633.html |
| BGB § 634 | Rechte bei Mängeln: Nacherfüllung, Rücktritt, Schadensersatz | https://dejure.org/gesetze/BGB/634.html |
| BGB § 280 | Schadensersatz wegen Pflichtverletzung | https://dejure.org/gesetze/BGB/280.html |
| BGB § 275 | Unmöglichkeit der Leistung | https://dejure.org/gesetze/BGB/275.html |
| BGB § 313 | Wegfall der Geschäftsgrundlage (Force Majeure) | https://dejure.org/gesetze/BGB/313.html |
| CISG (für internationale Druckaufträge) | UN-Kaufrecht | https://www.cisg.law.pace.edu |

## Druckvertrag: Grundstruktur

### Vertragsinhalt
Ein Druckvertrag sollte enthalten:
1. **Auflagenangabe**: Anzahl Exemplare, ggf. Toleranz (± 5 %).
2. **Technische Spezifikationen**: Papiersorte, -grammatur, Druckverfahren (Offset, Digital), Bindung (Klebebindung, Fadenheftung), Farbraum (CMYK), Schnitt.
3. **Lieferdatum**: Festes Datum oder Zeitfenster.
4. **Druckvorlagen-Lieferpflicht des Verlags**: Verlag schuldet druckfertige PDF/X-4-Dateien.
5. **Preisvereinbarung**: Festpreis, Einheitspreis pro 1.000 Exemplare, Zuschläge für Eilaufträge.
6. **Qualitätsstandards**: PSO (Process Standard Offset), ISO 12647, Dichte- und Tonwert-Toleranzen.
7. **Mängelrügefrist**: Innerhalb von 5–10 Werktagen nach Lieferung.

### Abnahme
- Druckwerk gilt als abgenommen, wenn Verlag nach Lieferung nicht fristgerecht rügt (§ 640 Abs. 2 BGB).
- **Andruckmuster / Proof**: Vor dem Druck Farbproof zur Freigabe durch Verlag; nach Freigabe kein Mängelanspruch für freigegebene Qualität.
- Korrekturen nach Druckstart: Kostenpflichtig; Klausel im Vertrag.

## Mängelrechte bei Druckmängeln (§§ 633 ff. BGB)

### Mangeldefinition
- Druckfehler: Fehldrucke, Farbabweichungen außerhalb vereinbarter Toleranz, Seitenversatz, falsche Bindung.
- Quantitativer Mangel: Weniger Exemplare als bestellt geliefert (außerhalb Toleranz).
- Verpackungsmangel: Exemplare beschädigt durch unzureichende Verpackung beim Transport.

### Rechtsfolgen
1. **Nacherfüllung** (§ 635 BGB): Nachlieferung oder Nachbesserung der mangelhaften Exemplare.
2. **Rücktritt** (§ 323 BGB): Bei erheblichem Mangel und gescheiterter Nacherfüllung.
3. **Schadensersatz** (§ 280 BGB): Druckerei haftet für Folgeschäden (Erscheinungsverzögerung, entgangene Buchhandelsbestellungen, Kosten für Sonderlieferungen).
4. **Minderung** (§ 638 BGB): Reduzierung des Druckpreises proportional zum Mangel.

## Papierlieferengpässe und Force Majeure

### Force Majeure (§ 275 BGB, § 313 BGB)
- Wenn Druckerei nachweist, dass Papierlieferung durch unvorhersehbare, unvermeidbare externe Ereignisse unmöglich ist → Leistungsbefreiung (§ 275 Abs. 1 BGB).
- Reine Preissteigerung: Kein Force-Majeure-Fall; Druckerei bleibt zum vereinbarten Preis verpflichtet.
- **Wegfall der Geschäftsgrundlage** (§ 313 BGB): Bei extremer Kostenveränderung kann Vertragsanpassung verlangt werden.

### Preisgleitklauseln
- Druckverträge mit Papierpreisgleitklausel: Druckpreis wird angepasst, wenn Papierpreisindex (z.B. FOEX-Index für Druckpapier) um bestimmten Prozentsatz abweicht.
- Transparenz: Verlag muss Klausel verstehen und berechnende Indizes kennen.
- **AGB-Kontrolle**: Preisgleitklauseln in AGB der Druckerei: Wirksam, wenn Index neutral und Berechnungsformel klar.

## Lieferverzug der Druckerei

### Rechtliche Einordnung
- Druckerei gerät in Verzug, wenn vereinbarter Liefertermin verstreicht (§ 286 BGB).
- Bei Kalendertermin: Verzug ohne Mahnung.
- Folgen: Schadensersatz (§ 280 BGB); Verlag kann Rücktritt nach Fristsetzung (§ 323 BGB) erklären.

### Schadensberechnung bei Verzug
- Entgangene Buchhandelsbestellungen (wenn Erscheinungstermin verpassen).
- Mehrkosten für Eilversand/Kurierdienst.
- Kosten für Umbuchung von Werbeterminen.
- Werbeschäden (Rezensionen ohne Buch verfügbar).

### Saisonale Lieferkritikalität
- Weihnachtsgeschäft: Lieferverzug im Oktober/November besonders schädlich → Vertragsstrafe oder höherer Schadensersatz.
- Buchmesse-Termine: Frankfurt (Oktober), Leipzig (März) — knappe Produktionszeiten.

## Notfallplanung

- **Alternative Druckereien**: Liste von Backup-Druckereien (DE, AT, CH, PL, CZ) mit Kapazitäten.
- **Digital-on-Demand**: Notauflage über Book-on-Demand-Anbieter (wenn Qualität ausreichend).
- **Versicherung**: Produktionsausfallversicherung für kritische Titel.

## Typische Fallen

- **Keine feste Liefertermin-Klausel**: Druckerei liefert „circa Mitte November" → keine Verzugs-Grundlage ohne festes Datum.
- **Proof nicht abgenommen**: Verlag versäumt Proof-Freigabe → Druckerei verzögert; Verzug liegt beim Verlag.
- **Papierpreisgleitklausel nicht verstanden**: Verlag akzeptiert Klausel; Papierpreis steigt; Druckpreis wird um 30 % angehoben → unerwartete Kosten.
- **Mängelrügefrist vergessen**: Verlag rügt Druckfehler 3 Wochen nach Lieferung; Frist bereits abgelaufen → Mängelansprüche erloschen.

## Checkliste Druckvertrag

- [ ] Lieferdatum als fester Termin vereinbart
- [ ] Papiersorte und -grammatur spezifiziert
- [ ] Preisgleitklausel verstanden und Risiko eingewertet
- [ ] Proof-Freigabe-Verfahren geregelt
- [ ] Mängelrügefrist definiert (5–10 Werktage nach Lieferung)
- [ ] Backup-Druckerei in Notfallplan benannt
- [ ] Vertragsstrafe bei Verzug bei kritischen Terminen vereinbart

## Quellenreferenzen

- BGB §§ 631–651: https://dejure.org/gesetze/BGB/631.html
- BGB § 313: https://dejure.org/gesetze/BGB/313.html
- FOEX-Papierpreisindex: https://www.foex.fi
- Bundesverband Druck und Medien (bvdm): https://www.bvdm.de
- BGH, Urt. v. 28.10.2020 – VIII ZR 141/19 (Wegfall Geschäftsgrundlage Liefervertrag): https://www.bgh.de

## Output-Formate

- **Druckvertrag-Review**: Checkliste Mindestklauseln
- **Schadenskalkulation Lieferverzug**: Entgangene Bestellungen, Mehrkosten
- **Preisgleitklausel-Bewertung**: Index, Formel, Risiko
- **Mängelrüge-Entwurf** an Druckerei
- **Notfallplan Druck**: Backup-Optionen bei Ausfällen

## 2. `verl-032-buchhandelsvertrag-konditionen-und-remission`

**Fokus:** Verlagsrecht: Buchhandelsvertrag zwischen Verlag und Buchhandel — Konditionenabkommen, Remissionsrecht, Retourenquoten, Auslieferungsverträge und Buchpreisbindungs-Compliance.

# Verl-032 · Buchhandelsvertrag, Konditionen und Remission

## Zweck dieses Skills

Der **Buchhandelsvertrag** zwischen Verlag (oder Auslieferung) und Buchhandlung ist die Grundlage des Buchvertriebssystems. Er regelt Rabatte, Zahlungsbedingungen, Remissionsrechte und Buchpreisbindungs-Pflichten. Dieser Skill analysiert die typischen Konditionenmodelle und die Remissions-Praxis.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG §§ 3–5 | Preisbindung, Verpflichtung des Buchhandels zum gebundenen Preis | https://www.gesetze-im-internet.de/buchprg/ |
| BuchPrG § 4 | Buchhandel als Vertragspartner: Preisbindungsklausel | https://www.gesetze-im-internet.de/buchprg/__4.html |
| HGB §§ 343 ff. | Handelsrecht: Kaufmann, Handelsgeschäft | https://dejure.org/gesetze/HGB/343.html |
| HGB § 377 | Untersuchungs- und Rügeobliegenheit beim Handelskauf | https://dejure.org/gesetze/HGB/377.html |
| BGB §§ 305 ff. | AGB-Recht: Konditionenabkommen als AGB | https://dejure.org/gesetze/BGB/305.html |
| BGB § 448 | Gefahrübergang beim Kauf | https://dejure.org/gesetze/BGB/448.html |

## Konditionensystem im Buchhandel

### Barsortimentsrabatt vs. Direktbezug
- **Barsortiment** (Grossist: Libri, KNV/VVA, Umbreit): Buchhandel kauft beim Barsortiment; Verlag liefert an Barsortiment.
 - Verlagsrabatt an Barsortiment: 40–50 % des Ladenpreises.
 - Barsortiment verkauft an Buchhandel mit 20–25 % Buchhandelsrabatt.
- **Direktbezug**: Buchhandel bestellt direkt beim Verlag oder dessen Auslieferung.
 - Buchhandelsrabatt: Typisch 30–40 % je nach Bestellgröße.
 - Kleinbuchhandlungen: 25–30 %.
 - Großfilialketten: 35–45 %.

### Konditionenabkommen des Börsenvereins
- Konditionenabkommen zwischen Verlegerverbänden und Buchhandelsverbänden legt Grundrabattrahmen fest.
- Sonderkonditionen: Verhandlung möglich, aber darf nicht zu Buchpreisbindungsverstoß führen.

### Zahlungsbedingungen
- Netto-Zahlungsziel: 30–90 Tage nach Rechnungserhalt.
- Skonto: 2–3 % bei Zahlung innerhalb von 10 Tagen üblich.
- Factoring: Manche Verlage/Auslieferungen nutzen Factoring; Buchhandel zahlt an Factor.

## Remission (Rücksendungsrecht)

### Remissionsrecht des Buchhandels
- Buchhandel darf unverkaufte Bücher an Verlag/Auslieferung zurücksenden.
- Grundlage: Vertragsklausel (nicht gesetzlich); im Buchhandel historisch als „Kommissionsähnliches" Recht etabliert.
- **Remissionsquote**: Prozentsatz der Liefermenge, die zurückgesandt werden darf; üblich 30–60 %.
- Bedingung: Rücksendung in verkaufsfähigem Zustand; Buchhandel trägt Rücksendungskosten (oft).

### Remission und Buchpreisbindung
- Remittierte Exemplare werden vom Verlag als Remittenden reklassifiziert.
- Kennzeichnung bei Wiederverkauf als Remittend unter Ladenpreis (§ 6 BuchPrG) erforderlich.
- Verlag sollte keine Abmahnung riskieren, wenn Remittenden ohne Kennzeichnung erneut als Neuware verkauft werden.

### Remissionsklausel im Buchhandelsvertrag
- Klare Regelung: Remissionsfenster (z.B. Bücher die 2 Jahre oder mehr im Lager), maximale Remissionsquote, Konditionierung (gut verkaufte Titel: keine Remission).
- Beschädigte Remittenden: Buchhandel haftet für Schäden durch sachgemäßen Umgang; ungerechtfertigte Beschädigungen → Schadensersatz.

## Auslieferungsvertrag

### Typischer Inhalt
1. Lagerhaltung: Auslieferung lagert den Verlagsbestand.
2. Auftragsabwicklung: Bestellungen annehmen, kommissionieren, versenden.
3. Abrechnung: Wöchentliche oder monatliche Abrechnung über Umsatz, Remittenden, Bestände.
4. Versicherung: Lagerware versichert durch Auslieferung (oder Verlag trägt Risiko).
5. Lagerkostenmodell: Flat-Rate oder per-Exemplar-Kosten; Lagergebühren für Slow-Mover.
6. Exklusivität: Häufig exklusive Auslieferung in DACH; eigene Vertriebskanäle behalten.

### Kündigung des Auslieferungsvertrags
- Verlag trägt Lagerbestand aus; Auslieferung stellt neue Bestellungen ein.
- Übergangszeit: Typisch 3–6 Monate für geordneten Wechsel.
- Lagerbestandsübertragung: Dokumentation aller Exemplare, Zustand, ISBN; Inventar bei Übergabe.

## Buchpreisbindungs-Compliance im Buchhandelsvertrag

### Pflichten des Buchhandels (§ 4 BuchPrG)
- Buchhandel verpflichtet sich im Vertrag, den gebundenen Ladenpreis einzuhalten.
- Verlag kann Buchhandelsvertrag kündigen oder Belieferung einstellen, wenn Buchhandel systematisch Preisbindung verletzt.

### Meldesystem für Verstöße
- Verlag informiert Buchhandel über Preisänderungen rechtzeitig (EDI, VLB-Update, Preisliste).
- Bei Buchhandels-Verstoß: Abmahnung (intern) → Kündigungsandrohung → Kündigung des Liefervertrags.

## Typische Fallen

- **Remissionsrecht ohne Quoten-Klausel**: Buchhandel sendet beliebig zurück; Verlag hat keine Kontrolle.
- **Konditionenrabatt und Buchpreisbindung**: Höherer Rabatt an bevorzugte Buchhandlung → wenn Endkundenpeis trotzdem stimmt, kein Verstoß; Rabatt ist Verlagssache.
- **Auslieferungsvertrag ohne Versicherungsklausel**: Lager brennt ab; Verlag hat keinen Ersatzanspruch.
- **Beschädigte Remittenden als Neuware reklassifiziert**: Auslieferung verbucht zurückgesandtes beschädigtes Exemplar als neu → Verkauf ohne Mängelkennzeichnung → Preisbindungsverstoß.

## Checkliste Buchhandelsvertrag

- [ ] Rabattstaffel und Zahlungsbedingungen klar vereinbart
- [ ] Remissionsquote und Remissionsfenster begrenzt
- [ ] Buchpreisbindungsklausel (§ 4 BuchPrG) im Vertrag
- [ ] Auslieferungsvertrag: Versicherung, Lagerkosten, Kündigung geregelt
- [ ] Remittend-Kennzeichnungspflicht im Vertrag festgehalten
- [ ] Kommunikationswege für Preisänderungen definiert (EDI, E-Mail)

## Quellenreferenzen

- BuchPrG § 4: https://www.gesetze-im-internet.de/buchprg/__4.html
- HGB § 377: https://dejure.org/gesetze/HGB/377.html
- Börsenverein, Konditionenabkommen: https://www.boersenverein.de
- Barsortiment Libri: https://www.libri.de
- BGH, Urt. v. 29.05.2018 – I ZR 171/16 (Buchhandelsvertrag): https://www.bgh.de

## Output-Formate

- **Konditionenvergleich**: Aktueller Vertrag vs. Marktstandard
- **Remissions-Analyse**: Remissionsquoten und Kostenwirkung
- **Buchhandelsvertrag-Muster**: Mindestklauseln
- **Auslieferungsvertrag-Review**: Versicherung, Kündigung, Kosten
- **Preisbindungs-Compliance-Checkliste** für Buchhandel
