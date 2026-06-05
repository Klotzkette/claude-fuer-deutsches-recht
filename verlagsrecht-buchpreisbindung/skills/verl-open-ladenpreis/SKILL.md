---
name: verl-open-ladenpreis
description: "Verl 008 Open Access Creative Commons Und Verlagspolitik, Verl 009 Buchpreisbindung Ladenpreis Festsetzen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 008 Open Access Creative Commons Und Verlagspolitik, Verl 009 Buchpreisbindung Ladenpreis Festsetzen

## Arbeitsbereich

Dieser Skill bündelt **Verl 008 Open Access Creative Commons Und Verlagspolitik, Verl 009 Buchpreisbindung Ladenpreis Festsetzen** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-008-open-access-creative-commons-und-verlagspolitik` | Verlagsrecht: Open-Access-Modelle, Creative-Commons-Lizenzen und Verlagspolitik — Rechteabgrenzung, Buchpreisbindung bei OA, Förderauflagen und Vertragsgestaltung. |
| `verl-009-buchpreisbindung-ladenpreis-festsetzen` | Buchpreisbindungsgesetz: Ladenpreis rechtssicher festsetzen — BuchPrG §§ 3–5, Preismeldung, Ausnahmen, E-Book-Besonderheiten und Durchsetzungspraxis. |

## Arbeitsweg

Für **Verl 008 Open Access Creative Commons Und Verlagspolitik, Verl 009 Buchpreisbindung Ladenpreis Festsetzen** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-008-open-access-creative-commons-und-verlagspolitik`

**Fokus:** Verlagsrecht: Open-Access-Modelle, Creative-Commons-Lizenzen und Verlagspolitik — Rechteabgrenzung, Buchpreisbindung bei OA, Förderauflagen und Vertragsgestaltung.

# Verl-008 · Open Access, Creative Commons und Verlagspolitik

## Zweck dieses Skills

Open Access (OA) und Creative-Commons-Lizenzen (CC) verändern das traditionelle Verlagsrechtssystem grundlegend. Dieser Skill klärt, wie OA-Publikationen mit dem Urheberrecht, der Buchpreisbindung und den Verlagspflichten zusammengehen — insbesondere bei Wissenschaftsverlagen, geförderten Werken (DFG, BMBF, EU) und Hybridmodellen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 31 | Nutzungsrechtseinräumung; CC-Lizenzen als Standardlizenzen | https://dejure.org/gesetze/UrhG/31.html |
| UrhG § 38 | Zweitveröffentlichungsrecht bei Periodika (§ 38 Abs. 4 UrhG) | https://dejure.org/gesetze/UrhG/38.html |
| UrhG § 32 | Angemessene Vergütung: gilt auch bei OA | https://dejure.org/gesetze/UrhG/32.html |
| BuchPrG § 2 | Preisbindung nur für entgeltlich vertriebene Bücher | https://www.gesetze-im-internet.de/buchprg/__2.html |
| BuchPrG § 6 | Ausnahmen von der Preisbindung | https://www.gesetze-im-internet.de/buchprg/__6.html |
| DSM-RL Art. 17 | Upload-Filter und Haftung von Plattformen | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |
| DSM-RL Art. 25 | Verbot der Umgehung des Zweitveröffentlichungsrechts | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Open-Access-Modelle im Verlag

### 1. Gold Open Access
- Artikel oder Buch wird **sofort beim Erscheinen** öffentlich zugänglich gemacht (keine Embargofrist).
- Finanzierung: Artikel Processing Charge (APC) oder Book Processing Charge (BPC) vom Autor, Institution oder Förderer.
- Typische CC-Lizenz: CC BY 4.0 (freie Nachnutzung unter Namensnennung).
- Buchpreisbindung: Da kein Entgelt für das OA-Werk erhoben wird → BuchPrG greift nicht (§ 2 BuchPrG: preisgebundene Bücher müssen entgeltlich veräußert werden).

### 2. Green Open Access / Zweitveröffentlichung
- Erstveröffentlichung im Verlag (kostenpflichtig); Autor darf nach Embargofrist Zweitversion in Repositorium einstellen (§ 38 Abs. 4 UrhG).
- Embargofrist: 12 Monate bei Periodika.
- Einschränkung: Nur die **angenommene Manuskriptversion** (accepted manuscript), nicht die Verlagsversion (PDF mit Verlagslayout).
- Institutionelle Repositorien (OPUS, Zenodo, PubMed Central) als Veröffentlichungsort.

### 3. Hybrid Open Access
- Abonnement-Zeitschrift mit Option, einzelne Artikel OA freizuschalten (gegen APC).
- Kritik: „Double Dipping" (Verlag kassiert Abo-Gebühr und APC gleichzeitig).
- Transformationsverträge (DEAL-Vertrag in Deutschland): Verlage wie Springer, Wiley, Elsevier vereinbaren Nationwide-Deals mit Max Planck Digital Library.

## Creative-Commons-Lizenzen im Verlagsvertrag

### Lizenztypen und ihre Konsequenzen

| Lizenz | Nachnutzung | Kommerziell | Bearbeitung | Copyleft |
|--------|-------------|-------------|-------------|---------|
| CC BY | Frei | Ja | Ja | Nein |
| CC BY-SA | Frei | Ja | Ja | Ja (ShareAlike) |
| CC BY-NC | Eingeschränkt | Nein | Ja | Nein |
| CC BY-ND | Eingeschränkt | Ja | Nein | Nein |
| CC BY-NC-ND | Eingeschränkt | Nein | Nein | Nein |
| CC0 | Gemeinfreiheit | Ja | Ja | Nein |

### Vertragsrechtliche Einordnung
- CC-Lizenzen sind **bedingungslose Nutzungslizenzen** an alle Dritten; sie können nicht widerrufen werden (Unwiderruflichkeit per Lizenztext).
- Wenn Autor CC BY vergibt, räumt er dem Verlag und gleichzeitig aller Welt dieselben Nutzungsrechte ein → ausschließliche Lizenz im klassischen Sinne nicht mehr möglich.
- Konsequenz: Verlag verliert Exklusivität; wirtschaftlicher Wert des Verlagsvertrags sinkt → Honorar muss angepasst werden.

### Embargos und OA-Transformationsverträge
- DFG-Förderrichtlinie 2023: Geförderte Publikationen müssen CC BY veröffentlicht werden; kein ND oder NC.
- Horizon Europe (EU-Forschungsförderung): CC BY für Artikel, CC BY oder CC BY-SA für Datensätze.
- Verlagsverträge mit Förderempfängern müssen OA-Auflagen einschließen.

## Buchpreisbindung und Open Access

### Grundregel
- BuchPrG bindet den **Ladenpreis** von Büchern, die entgeltlich an Letztverbraucher abgegeben werden.
- Kostenloses OA-Buch (kein Kaufpreis) → kein Anwendungsbereich des BuchPrG.
- **Hybridfall**: OA-Version kostenlos, Printausgabe kostenpflichtig → Printausgabe ist preisgebunden; OA-PDF nicht.

### Risiko: Verdrängung des Printtitels
- Wenn OA-PDF zeitgleich mit Print erscheint und identisch ist → Preisbindung für Print läuft faktisch leer.
- Kein gesetzliches Verbot, aber wirtschaftliches Risiko für Buchhandel; ggf. Streit mit Börsenverein.

## Verlagspolitik und institutionelle Verhandlungen

### DEAL-Verträge
- Nationwide Open-Access-Abkommen zwischen dt. Hochschulen (MPDL/Allianz) und Verlagen (Springer Nature, Wiley, Elsevier).
- Autoren aus deutschen Institutionen können OA publizieren; Verlag erhält einheitliche Gebühr.
- Auswirkung auf Autorenverträge: Verlag ist zur OA-Freischaltung verpflichtet.

### Plan S (cOAlition S)
- Förderrichtlinie europäischer Forschungsorganisationen: Alle geförderten Publikationen ab sofort OA.
- CC BY zwingend; keine Embargo-Periode.
- Verlage müssen „Plan S-compliant"-Wege anbieten.

## Typische Fallen

- **Unwiderruflichkeit der CC-Lizenz**: Verlag, der CC BY bereits vergeben hat, kann keine exklusive Lizenz mehr einräumen.
- **Zweitveröffentlichungsrecht § 38 Abs. 4 UrhG falsch verstanden**: Gilt nur für Beiträge in Periodika; für Bücher kein gesetzliches Zweitveröffentlichungsrecht.
- **Förderauflagen vergessen**: Verlag schließt exklusiven Verlagsvertrag, obwohl Autor DFG-Mittel hatte und OA-Pflicht besteht.
- **OA und Plagiatsprüfung**: Frei zugängliche Versionen erhöhen Auffindbarkeit von Plagiaten; Verlag sollte Clearance-Klausel beibehalten.
- **BuchPrG bei Hybridverkauf**: Print und OA-PDF gleichzeitig; Buchpreisbindung für Print muss konsequent durchgesetzt werden.

## Checkliste OA-Verlagsvertrag

- [ ] OA-Pflicht aus Fördervertrag eruiert und dokumentiert
- [ ] CC-Lizenztyp und Einschränkungen (NC, ND) mit Förderbedingungen abgeglichen
- [ ] Embargofrist (falls keine Gold OA Pflicht) in Vertrag
- [ ] Zweitveröffentlichungsrecht (§ 38 Abs. 4 UrhG) geregelt
- [ ] BPC/APC-Finanzierung sichergestellt
- [ ] Printausgaben-Preisbindung separat geregelt
- [ ] DEAL-/transformativer Vertrag geprüft

## Quellenreferenzen

- UrhG § 38 Abs. 4: https://dejure.org/gesetze/UrhG/38.html
- BuchPrG §§ 2, 6: https://www.gesetze-im-internet.de/buchprg/
- DSM-RL 2019/790: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- Creative Commons Lizenzübersicht: https://creativecommons.org/licenses/
- DEAL-Vertrag Springer Nature: https://www.projekt-deal.de

## Output-Formate

- **OA-Compliance-Check**: Förderauflagen vs. Vertragsklauseln
- **CC-Lizenz-Matrix**: Lizenztyp, Konsequenzen für Verlag und Dritte
- **BuchPrG-Ampel für Hybridwerk**
- **Vertragsklausel OA**: Muster für Zweitveröffentlichungsrecht und Förderauflage
- **DEAL-Konformitätsprüfung**

## 2. `verl-009-buchpreisbindung-ladenpreis-festsetzen`

**Fokus:** Buchpreisbindungsgesetz: Ladenpreis rechtssicher festsetzen — BuchPrG §§ 3–5, Preismeldung, Ausnahmen, E-Book-Besonderheiten und Durchsetzungspraxis.

# Verl-009 · Buchpreisbindung: Ladenpreis festsetzen

## Zweck dieses Skills

Dieser Skill führt durch den **Prozess der Ladenpreisfestsetzung** nach dem Buchpreisbindungsgesetz (BuchPrG): Wer darf den Preis festsetzen, wie ist er zu melden, welche Produkte sind erfasst, welche Ausnahmen bestehen und wie wird die Preisbindung gegenüber dem Buchhandel durchgesetzt.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG § 1 | Zweck: kulturelle Vielfalt, Buchhandelsstruktur | https://www.gesetze-im-internet.de/buchprg/__1.html |
| BuchPrG § 2 | Geltungsbereich: Bücher, Noten, Landkarten, E-Books | https://www.gesetze-im-internet.de/buchprg/__2.html |
| BuchPrG § 3 | Festsetzungspflicht: Verleger und Importeur | https://www.gesetze-im-internet.de/buchprg/__3.html |
| BuchPrG § 4 | Preisbindungsklausel im Buchhandelsvertrag | https://www.gesetze-im-internet.de/buchprg/__4.html |
| BuchPrG § 5 | Bindung des Letztabnehmers | https://www.gesetze-im-internet.de/buchprg/__5.html |
| BuchPrG § 6 | Ausnahmen von der Preisbindung | https://www.gesetze-im-internet.de/buchprg/__6.html |
| BuchPrG § 7 | Änderung und Aufhebung des Preises | https://www.gesetze-im-internet.de/buchprg/__7.html |
| BuchPrG § 9 | Ansprüche bei Verstößen | https://www.gesetze-im-internet.de/buchprg/__9.html |

## Wer setzt den Preis fest?

### § 3 Abs. 1 BuchPrG — Festsetzungspflicht
- **Verleger**: Jede in Deutschland erscheinende Buchausgabe muss vom Verleger mit einem Ladenpreis versehen werden.
- **Importeur**: Wer Bücher aus dem Ausland nach Deutschland einführt und dort vertreibt, muss ebenfalls einen Preis festsetzen.
- **Self-Publishing-Plattformen** (BoD, KDP Print): Die Plattform übernimmt die Verlegerfunktion, wenn sie das Buch in Deutschland erscheinen lässt; Preisfestsetzung durch die Plattform im Namen des Autors.

### § 3 Abs. 2 BuchPrG — Inhalt der Preisfestsetzung
- Ladenpreis muss für **jede einzelne Ausgabe** (Hardcover, Paperback, E-Book) separat festgesetzt werden.
- Preis in Euro inkl. MwSt. (Endkundenpreis, Ladenpreis).
- Keine automatische Bindung des Importeurs an den ausländischen Preis des Verlags.

## Produkte im Geltungsbereich (§ 2 BuchPrG)

| Produkt | Preisgebunden | Bemerkungen |
|---------|--------------|-------------|
| Bücher (Sprachwerke) | Ja | Papiergebunden, alle Formate |
| Noten | Ja | Musiknoten, Liederbücher |
| Kartografische Erzeugnisse | Ja | Landkarten, Stadtpläne |
| E-Books | Ja (seit 2016) | Wenn Inhalt auch als Buch erscheint |
| Hörbücher (physisch) | Ja | CD, Kassette |
| Hörbücher (Download/Stream) | Nein | Kein Buch i.S.d. BuchPrG |
| Schulbücher | Ja | Besondere Konditionenregelungen |
| Taschenbücher | Ja | Auch Book-on-Demand |
| Zeitschriften | Nein | Kein Buch |
| Spiele, Apps | Nein | Selbst wenn buchähnlich |

## Preismeldung und VLB

- **VLB (Verzeichnis Lieferbarer Bücher)**: Branchen-Datenbank des Börsenvereins; Verlag meldet ISBN, Ladenpreis, Ausgabetyp.
- Nicht gesetzlich vorgeschrieben, aber faktisch Standard; ohne VLB-Eintrag ist Vertrieb über den regulären Buchhandel kaum möglich.
- **Datenmeldung**: Über VLB-Webportal oder EDI-Schnittstelle; ISBN 13-stellig, BISAC/Warengruppe, Erscheinungsdatum, Preis.
- Verlagsauslieferung (Prolit, KNV/VVA, Umbreit) übernimmt häufig die VLB-Meldung.

## Preisänderung und -aufhebung (§ 7 BuchPrG)

- Verleger darf den Preis **jederzeit ändern oder aufheben**.
- Preissenkung: Sofort wirksam; Buchhandel muss zum neuen Preis verkaufen.
- Preiserhöhung: Buchhandel muss neuen Preis anwenden, sobald er ihm mitgeteilt wird; bereits ausgepreiste Exemplare können zum alten Preis verkauft werden, sofern nicht anders vereinbart.
- **Vergriffserklärung**: Wenn der Titel nicht mehr lieferbar ist, kann der Preis aufgehoben werden (§ 7 Abs. 2 BuchPrG); danach kein Preisbindungsverstoß durch Buchhandel mehr.

## Ausnahmen von der Preisbindung (§ 6 BuchPrG)

1. **Beschädigte Exemplare**: Mängelexemplare mit deutlicher Kennzeichnung.
2. **Remittenden** (Remittierungs-Rückläufer): Vom Buchhandel zurückgesandte, ggf. beschädigte Exemplare.
3. **Bücher, die länger als 18 Monate beim Händler liegen** (Altexemplare mit Kenntlichmachung).
4. **Institutionelle Abnahmen**: Bibliotheken, Schulen — Sonderkonditionen zulässig, aber kein Unterschreiten des Ladenpreises ohne ausdrückliche Freistellung.
5. **Bücher zu wissenschaftlichen, kirchlichen oder staatlichen Zwecken** nach besonderer Regelung.
6. **Musterexemplare** für Rezensenten und Presse (Rezensionsexemplare).

## E-Book-Preisbindung

- E-Books unterliegen seit 2016 der Preisbindung, wenn sie in Deutschland erscheinen (BuchPrG § 2 Abs. 1 Nr. 3).
- **Separate Preisfestsetzung** für jedes Format (EPUB, MOBI, PDF) empfohlen.
- **Plattform-Rabatte**: Amazon, Apple Books dürfen keinen Preis unter dem gebundenen Ladenpreis anbieten; Plattformrabatte auf Kosten des Verlags sind zulässig, wenn Endkundenpreis stimmt.
- **Promotions-Ausnahmen**: Zeitlich begrenzte Aktionspreise sind nach § 7 BuchPrG als temporäre Preissenkung möglich.

## Typische Fallen

- **Preis nicht für E-Book gesondert festgesetzt**: E-Book erscheint ohne explizit gemeldeten E-Book-Preis → Preisbindungsverstoß des Verlags selbst.
- **Importeur übernimmt Auslandspreis ohne Umrechnung**: Preisbindung gilt für den deutschen Markt; EUR-Preis muss eigenständig festgesetzt werden.
- **Vergünstigungen an Institutionen ohne Freistellung**: Bibliotheksrabatt ohne § 6-Ausnahme → Verstoß.
- **Ladenpreis für Remittenden nicht gekennzeichnet**: Remittend ohne deutliche Kenntlichmachung kann nicht unter Ladenpreis verkauft werden.
- **VLB-Preis und Rechnungspreis weichen ab**: Händler meldet Preisverstoß; tatsächlich lag Irrtum im VLB-Eintrag vor.

## Checkliste Ladenpreisfestsetzung

- [ ] Preis für jede Ausgabe (Print, E-Book, Hörbuch) separat festgesetzt
- [ ] VLB-Meldung mit korrektem EUR-Preis und ISBN
- [ ] Preisänderungen dem Buchhandel schriftlich/elektronisch mitgeteilt
- [ ] Ausnahmen nach § 6 BuchPrG dokumentiert
- [ ] Remittenden-Kennzeichnung sichergestellt
- [ ] Plattformverträge auf Preisbindungs-Compliance geprüft

## Quellenreferenzen

- BuchPrG: https://www.gesetze-im-internet.de/buchprg/
- Börsenverein, Buchpreisbindung Erläuterungen: https://www.boersenverein.de/themen-positionen/buchmarkt/buchpreisbindung/
- BGH „Paperboy" I ZR 259/00 (Preisbindung Online): https://www.bgh.de
- LG Frankfurt, Urt. v. 02.12.2015 (E-Book-Preisbindung): https://openjur.de
- Börsenblatt, VLB-Datenmeldung: https://www.boersenblatt.net

## Output-Formate

- **Preisfestsetzungs-Memo**: Alle Ausgaben mit festgesetzten Preisen
- **VLB-Checkliste**: Pflichtfelder für korrekte Datenmeldung
- **Ausnahmen-Protokoll**: § 6 BuchPrG-Ausnahmen mit Belegen
- **Preisänderungsschreiben** an Buchhandel
- **E-Book-Plattform-Compliance-Check**
